#!/usr/bin/python3
"""
Unittests for Square class
"""

import io
import unittest
import sys
from models.base import Base
from models.square import Square


class Test_Square(unittest.TestCase):
    """ validate test for Square """

    def test_Square1(self):
        """
        Validate the number of id
        """
        S1 = Square(5)
        self.assertEqual(S1.id, 9)
        S2 = Square(5, 2, 1, 48)
        self.assertEqual(S2.id, 48)

    def test_Square2(self):
        """
        Validate id with other types
        """
        S3 = Square(10, 2, 0, "hi")
        self.assertEqual(S3.id, "hi")
        S4 = Square(10, 2, 0, [12, 10])
        self.assertEqual(S4.id, [12, 10])
        S5 = Square(10, 2, 0, {"key": 12, "value": 20})
        self.assertEqual(S5.id, {'key': 12, 'value': 20})
        S6 = Square(10, 2, 0, (12, 10))
        self.assertEqual(S6.id, (12, 10))

    def test_Square3(self):
        """
        test Square without arguments
        """
        with self.assertRaises(TypeError):
            S7 = Square()

    def test_Square4(self):
        """
        test differents parameters
        """
        S8 = Square(24)
        self.assertEqual(S8.size, 24)
        self.assertEqual(S8.x, 0)
        self.assertEqual(S8.y, 0)

    def test_Square5(self):
        """
        test differents parameters1
        """
        S9 = Square(4, 2, 3)
        self.assertEqual(S9.size, 4)
        self.assertEqual(S9.x, 2)
        self.assertEqual(S9.y, 3)

    def test_Square6(self):
        """
        the numbers of arguments is five
        """
        with self.assertRaises(TypeError):
            S10 = Square(10, 5, 3, 1, 3)

    def test_Square7(self):
        """
        validate the type of arguments size
        """
        with self.assertRaises(TypeError):
            S11 = Square("Holberton")
        with self.assertRaises(TypeError):
            S13 = Square((4, 8))
        with self.assertRaises(TypeError):
            S14 = Square([2, 5])
        with self.assertRaises(TypeError):
            S15 = Square({"KEY": 10})

    def test_Square8(self):
        """
        validate the type of arguments x and y
        """
        with self.assertRaises(TypeError):
            S16 = Square(4, 8, "Holbie")
        with self.assertRaises(TypeError):
            S17 = Square(4, 8, [10, 4])
        with self.assertRaises(TypeError):
            S18 = Square(4, 8, (12, 20))
        with self.assertRaises(TypeError):
            S19 = Square(4, {10: 2}, 8)

    def test_Square9(self):
        """
        Validate the size of width
        """
        with self.assertRaises(ValueError):
            Square(-2)

    def test_Square10(self):
        """
        validate the position of x and y
        """
        with self.assertRaises(ValueError):
            Square(5, -1, 3)
        with self.assertRaises(ValueError):
            Square(5, 1, -3)

if __name__ == "__main__":
    unittest.main()
