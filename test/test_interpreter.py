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
                ("-"*r+"+"*r, [0])
            ]
            for symb, mem in cases:
                _, code = symb2btry(symb)
                i, p, m, o = E(code)
                with self.subTest(symb=symb):
                    self.assertEqual(p, 0)
                    self.assertEqual(m, mem)
                    self.assertIsNone(i, None)
                    self.assertEqual(o, "")
