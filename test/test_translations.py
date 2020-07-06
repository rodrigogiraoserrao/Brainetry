"""
This module tests the translation capabilities of brainetry.
"""

import pathlib
import random
import sys
import unittest

if __name__ == "__main__":
    sys.path.append(str(
        pathlib.Path(__file__).parent.parent.absolute()
    ))

from brainetry import btry2symb, symb2btry, golf
from interpreter import O

class TestTranslations(unittest.TestCase):
    """Tests that the symb2btry function is invertible."""

    def setUp(self):
        self.ops = [o for o in O if o != " "]

    def translate(self, idx):
        """Given a sequence of operator hex indices, build the symbolic code."""

        return "".join(O[int(i, 16)] for i in idx)

    def test_single_op(self):
        """Test translations with code containing a single operator."""

        for op in self.ops:
            for i in range(1, 5):
                code = op*i
                idx, btry = symb2btry(code)
                golfed = golf(btry)
                with self.subTest(code=code):
                    self.assertEqual(btry2symb(btry), code)
                    self.assertEqual(self.translate(idx), code)
                    self.assertEqual(btry2symb(golfed), code)
                    if btry.count("\n") < len(btry):
                        self.assertLess(len(golfed), len(btry))

    def test_several_ops(self):
        """Test translations with larger programs."""

        for k in range(5, 10):
            for i in range(len(self.ops)-k+1):
                code = "".join(self.ops[i:i+k]*3)
                idx, btry = symb2btry(code)
                with self.subTest(code=code):
                    self.assertEqual(btry2symb(btry), code)
                    self.assertEqual(self.translate(idx), code)

    def test_examples(self):
        """Test translations on the example programs available."""

        mainpath = pathlib.Path(__file__).absolute().parent.parent / "btry"
        paths = [
            p for p in mainpath.iterdir() if not p.is_dir() and p.name.endswith(".btry")
        ]

        for path in paths:
            with open(path, "r") as f:
                btry = f.read()
            if not btry:
                continue
            golfed = golf(btry)
            symb = btry2symb(btry)
            idx, _ = symb2btry(symb)
            with self.subTest(example=path.name):
                self.assertEqual(symb, btry2symb(golfed))
                self.assertLess(len(golfed), len(btry))
                self.assertEqual(self.translate(idx), symb)

    def test_monte_carlo(self):
        """Create random symbolic programs and translate them."""

        N = 100
        for _ in range(N):
            code = ""
            for _ in range(random.randint(25, 35)):
                code += random.choice(self.ops)
            idx, btry = symb2btry(code)
            golfed = golf(btry)
            with self.subTest(code=code):
                self.assertEqual(btry2symb(btry), code)
                self.assertEqual(self.translate(idx), code)
                self.assertEqual(btry2symb(golfed), code)
                if btry.count("\n") < len(btry):
                    self.assertLess(len(golfed), len(btry))


if __name__ == "__main__":
    unittest.main()
