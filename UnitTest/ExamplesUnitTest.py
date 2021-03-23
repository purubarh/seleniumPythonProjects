import unittest
from Examples import Example


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("This will run once before all the methods")

    @classmethod
    def tearDownClass(cls):
        print("This will run once after all the methods")

    def setUp(self):
        print("This will run before every method")

    def tearDown(self):
        print("This will run after every method")

    def test_add(self):
        self.assertEqual(Example.add(self, 20, 10), 30)
        self.assertEqual(Example.add(self, 0, 0), 0)
        self.assertEqual(Example.add(self, -1, 1), 0)

    def test_substraction(self):
        self.assertEqual(Example.substraction(self, 20, 10), 10)
        self.assertEqual(Example.substraction(self, -1, 1), -2)
        self.assertEqual(Example.substraction(self, 0, 0), 0)


if __name__ == '__main__':
    unittest.main()
