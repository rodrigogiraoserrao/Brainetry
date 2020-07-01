import os.path
import unittest
import brainetry
import interpreter

btry_path = os.path.dirname(__file__) + r'/btry/'
file_list = list(map(lambda s: str(s)[12:-2], os.scandir(btry_path)))


class TestAuto(unittest.TestCase):
    def test_hello_world(self):
        with open(btry_path + 'hello_world.btry', "r", encoding="utf8") as f:
            inp = f.read()
        f.close()
        i, p, m, o = interpreter.E(inp)
        self.assertEqual(o, 'Hello, World!')

    def test_pointer(self):
        i, p, m, o = interpreter.E('test test test test')
        self.assertEqual(p, 0)

    def test_to_sym(self):
        for k in range(len(interpreter.operations)):
            self.assertEqual(brainetry.btry2symb(' '.join(['test']*k)), interpreter.operations[k])
        self.assertEqual(brainetry.btry2symb('test test test test'), '+')



if __name__ == '__main__':
    unittest.main()

