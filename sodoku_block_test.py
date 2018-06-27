#!/usr/bin/env python3

import unittest
import sodoku

class MyTestCase(unittest.TestCase):

    def test_blockIsEmpty(self):
        a = sodoku.Block()
        for square in a.squares:
            self.assertEqual(square, None)

    def test_setSquare(self):
        a = sodoku.Block()
        a.setSquare(3, 5)
        self.assertEqual(5, a.getSquare(3))

    def test_setSquareRowColumn(self):
        a = sodoku.Block()
        a.setSquareRowColumn(1, 1, 4)
        self.assertEqual(4, a.getSquare(4))

    def test_getSquareRowColumn(self):
        a = sodoku.Block()
        a.setSquareRowColumn(1, 1, 4)
        self.assertEqual(4, a.getSquareRowColumn(1, 1))

    def test_getRowSquares(self):
        a = sodoku.Block()
        for i in range(0, 10):
            a.setSquare(i, i)
        self.assertEqual([0, 1, 2], a.getRowSquares(0))
        self.assertEqual([3, 4, 5], a.getRowSquares(1))
        self.assertEqual([6, 7, 8], a.getRowSquares(2))

    def test_getColumnSquares(self):
        a = sodoku.Block()
        for i in range(0, 10):
            a.setSquare(i, i)
        self.assertEqual([0, 3, 6], a.getColumnSquares(0))
        self.assertEqual([1, 4, 7], a.getColumnSquares(1))
        self.assertEqual([2, 5, 8], a.getColumnSquares(2))

    def test_isNumberInRow(self):
        a = sodoku.Block()
        a.setSquareRowColumn(1, 1, 4)
        self.assertTrue(a.isNumberInRow(1, 4))
        self.assertFalse(a.isNumberInRow(0, 4))

    def test_isNumberInColumn(self):
        a = sodoku.Block()
        a.setSquareRowColumn(1, 1, 4)
        self.assertTrue(a.isNumberInColumn(1, 4))
        self.assertFalse(a.isNumberInColumn(0, 4))

if __name__ == '__main__':
    unittest.main()