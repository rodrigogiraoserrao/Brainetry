"""
This module tests the brainetry interpreter.
"""

import pathlib
import sys
import unittest

if __name__ == "__main__":
    sys.path.append(str(
        pathlib.Path(__file__).parent.parent.absolute()
    ))

from brainetry import symb2btry
from interpreter import E

class FakeStdin:
    """Simple class to act as a dummy stdin that reads a pre-defined string."""
    def __init__(self, string):
        self.string = string
    def read(self):
        return self.string

def save_stdin(func):
    """Decorator to wrap a function that might redirect stdin temporarily."""
    def wrapper(*args, **kwargs):
        stdin = sys.stdin
        ret = func(*args, **kwargs)
        sys.stdin = stdin
        return ret
    return wrapper

class TestBrainfuckOps(unittest.TestCase):
    """Test the eight operators that are inherited from brainf*ck."""

    def test_plus_minus(self):
        """Tests the usage of plus and minus."""

        for r in range(20):
            cases = [
                ("+"*r, [r]),
                ("+-"*r, [0]),
                ("+"*r+"-"*r, [0]),
                ("-+"*r, [0]),
                ("-"*r+"+"*r, [0]),
            ]
            for symb, mem in cases:
                _, code = symb2btry(symb)
                i, p, m, o = E(code)
                with self.subTest(symb=symb):
                    self.assertEqual(p, 0)
                    self.assertEqual(m, mem)
                    self.assertIsNone(i)
                    self.assertEqual(o, "")

    def test_right_left(self):
        """Tests the usage of the left/right operators."""

        for r in range(1, 20):
            cases = [
                (">"*r, [0]*(r+1), r),
                ("<"*r, [0]*(r+1), 0),
                ("><"*r, [0, 0], 0),
                ("<>"*r, [0, 0], 1),
                (">"*r+"<"*r, [0]*(r+1), 0),
                ("<"*r+">"*r, [0]*(r+1), r),
            ]
            for symb, mem, ptr in cases:
                _, code = symb2btry(symb)
                i, p, m, o = E(code)
                with self.subTest(symb=symb):
                    self.assertEqual(p, ptr)
                    self.assertEqual(m, mem)
                    self.assertIsNone(i)
                    self.assertEqual(o, "")

    @save_stdin
    def test_input(self):
        """Tests the input operator."""

        alphabet = "abcdefghijklmnopqrstuvwxyz"
        chars = [*alphabet]
        for k in range(len(alphabet)+5):
            sys.stdin = FakeStdin(alphabet)
            _, code = symb2btry(","*k)
            i, p, m, o = E(code)
            with self.subTest(k=k, input=alphabet[:k]):
                if k:
                    self.assertEqual(chars[k:], i)
                else:
                    self.assertIsNone(i)
                self.assertEqual(p, 0)
                if k and k <= len(alphabet):
                    self.assertEqual(m, [ord(alphabet[k-1])])
                elif k > len(alphabet):
                    self.assertEqual(m, [0])
                self.assertEqual(o, "")
