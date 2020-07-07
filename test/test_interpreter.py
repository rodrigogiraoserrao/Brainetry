"""
This module tests the brainetry interpreter.
"""

import io
import pathlib
import sys
import unittest

if __name__ == "__main__":
    sys.path.append(str(
        pathlib.Path(__file__).parent.parent.absolute()
    ))

from brainetry import symb2btry
from interpreter import E


def save_stdin(func):
    """Decorator to restore default stdin after we leave the function."""
    def wrapper(*args, **kwargs):
        stdin = sys.stdin
        ret = func(*args, **kwargs)
        sys.stdin = stdin
        return ret
    return wrapper

def mute_stdout(func):
    """Decorator to redirect stdout during the function call."""
    def wrapper(*args, **kwargs):
        stdout = sys.stdout
        sys.stdout = io.StringIO()
        ret = func(*args, **kwargs)
        sys.stdout = stdout
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
                p, m, o = E(code)
                with self.subTest(symb=symb):
                    self.assertEqual(p, 0)
                    self.assertEqual(m, mem)
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
                p, m, o = E(code)
                with self.subTest(symb=symb):
                    self.assertEqual(p, ptr)
                    self.assertEqual(m, mem)
                    self.assertEqual(o, "")

    @save_stdin
    def test_input(self):
        """Tests the input operator."""

        alphabet = "abcdefghijklmnopqrstuvwxyz"
        chars = [*alphabet]
        ords = [ord(char) for char in chars] + [0]*5
        for k in range(len(alphabet)+5):
            sys.stdin = io.StringIO(alphabet)
            symb = ","*k
            _, code = symb2btry(symb)
            p, m, o = E(code)
            with self.subTest(k=k, symb=symb, input=alphabet):
                self.assertEqual(p, 0)
                if k and k <= len(alphabet):
                    self.assertEqual(m, [ords[k-1]])
                elif k > len(alphabet):
                    self.assertEqual(m, [0])
                self.assertEqual(o, "")

            sys.stdin = io.StringIO(alphabet)
            symb = ",>"*k
            _, code = symb2btry(symb)
            p, m, o = E(code)
            with self.subTest(k=k, symb=symb, input=alphabet):
                self.assertEqual(p, k)
                self.assertEqual(m, ords[:k]+[0])
                self.assertEqual(o, "")

    @save_stdin
    @mute_stdout
    def test_output(self):
        """Test the output operator."""

        _, code = symb2btry("...")
        p, m, o = E(code)
        self.assertEqual(p, 0)
        self.assertEqual(m, [0])
        self.assertEqual(o, "\u0000"*3)

        strings = [
            "head",
            "shoulders",
            "knees and toes, knees and toes!"
        ]
        for string in strings:
            for k in range(1, len(string)+5):
                sys.stdin = io.StringIO(string)
                symb = ",."*k
                _, code = symb2btry(symb)
                p, m, o = E(code)
                with self.subTest(k=k, symb=symb, input=string):
                    self.assertEqual(p, 0)
                    if k > len(string):
                        self.assertEqual(m, [0])
                        self.assertEqual(o, string + "\u0000"*(k-len(string)))
                    else:
                        self.assertEqual(m, [ord(string[k-1])])
                        self.assertEqual(o, string[:k])
