import unittest
import sodoku

class MyTestCase(unittest.TestCase):

    def test_allIsEmpty(self):
        a = sodoku.Sodoku()
        for block in a.blocks:
            for square in block.squares:
                self.assertEqual(None, square)

    # def test_onlyOneEdited(self):
    #     a = sodoku.Sodoku()
    #     a.blocks[1].squares[0] = 1
    #     for y, block in enumerate(a.blocks):
    #         print(y)
    #         for x, square in enumerate(block.squares):
    #             print("    ", x, ":", square)

    def test_calculateBlockFromRowColumn(self):
        a = sodoku.Sodoku()
        self.assertEqual([0, 0, 0], a.calculateBlockRowColumn(0, 0))
        self.assertEqual([0, 1, 0], a.calculateBlockRowColumn(1, 0))
        self.assertEqual([0, 2, 0], a.calculateBlockRowColumn(2, 0))
        self.assertEqual([0, 0, 1], a.calculateBlockRowColumn(0, 1))
        self.assertEqual([0, 1, 1], a.calculateBlockRowColumn(1, 1))
        self.assertEqual([0, 2, 1], a.calculateBlockRowColumn(2, 1))
        self.assertEqual([0, 0, 2], a.calculateBlockRowColumn(0, 2))
        self.assertEqual([0, 1, 2], a.calculateBlockRowColumn(1, 2))
        self.assertEqual([0, 2, 2], a.calculateBlockRowColumn(2, 2))

        self.assertEqual([1, 0, 0], a.calculateBlockRowColumn(0, 3))
        self.assertEqual([1, 1, 0], a.calculateBlockRowColumn(1, 3))
        self.assertEqual([1, 2, 0], a.calculateBlockRowColumn(2, 3))
        self.assertEqual([1, 0, 1], a.calculateBlockRowColumn(0, 4))
        self.assertEqual([1, 1, 1], a.calculateBlockRowColumn(1, 4))
        self.assertEqual([1, 2, 1], a.calculateBlockRowColumn(2, 4))
        self.assertEqual([1, 0, 2], a.calculateBlockRowColumn(0, 5))
        self.assertEqual([1, 1, 2], a.calculateBlockRowColumn(1, 5))
        self.assertEqual([1, 2, 2], a.calculateBlockRowColumn(2, 5))

        self.assertEqual([3, 0, 0], a.calculateBlockRowColumn(3, 0))
        self.assertEqual([3, 1, 0], a.calculateBlockRowColumn(4, 0))
        self.assertEqual([3, 2, 0], a.calculateBlockRowColumn(5, 0))
        self.assertEqual([3, 0, 1], a.calculateBlockRowColumn(3, 1))
        self.assertEqual([3, 1, 1], a.calculateBlockRowColumn(4, 1))
        self.assertEqual([3, 2, 1], a.calculateBlockRowColumn(5, 1))
        self.assertEqual([3, 0, 2], a.calculateBlockRowColumn(3, 2))
        self.assertEqual([3, 1, 2], a.calculateBlockRowColumn(4, 2))
        self.assertEqual([3, 2, 2], a.calculateBlockRowColumn(5, 2))

        self.assertEqual([6, 0, 2], a.calculateBlockRowColumn(6, 2))

    def test_setSquareRowColumn(self):
        a = sodoku.Sodoku()
        a.setSquareRowColumn(6, 2, 5)
        self.assertEqual(5, a.blocks[6].getSquareRowColumn(0, 2))

    def test_getSquareRowColumn(self):
        a = sodoku.Sodoku()
        a.setSquareRowColumn(6, 2, 5)
        self.assertEqual(5, a.getSquareRowColumn(6, 2))

    def test_getRowSquares(self):
        a = sodoku.Sodoku()
        a.setSquareRowColumn(0, 0, 5)
        self.assertEqual([5, None, None, None, None, None, None, None, None], a.getRowSquares(0))
        a.setSquareRowColumn(3, 4, 5)
        self.assertEqual([None, None, None, None, 5, None, None, None, None], a.getRowSquares(3))

    def test_getColumnSquares(self):
        a = sodoku.Sodoku()
        a.setSquareRowColumn(0, 0, 5)
        self.assertEqual([5, None, None, None, None, None, None, None, None], a.getColumnSquares(0))
        a.setSquareRowColumn(3, 4, 5)
        self.assertEqual([None, None, None, 5, None, None, None, None, None], a.getColumnSquares(4))

if __name__ == '__main__':
    unittest.main()