#!/usr/bin/env python3

class Block:
    """1 sodoku block"""

    def __init__(self):
        self.squares = [None for i in range(9)]

    def setSquare(self, index, number):
        self.squares[index] = number

    def getSquare(self, index):
        return self.squares[index]

    def setSquareRowColumn(self, row, column, number):
        self.setSquare(row * 3 + column, number)

    def getSquareRowColumn(self, row, column):
        return self.getSquare(row * 3 + column)

    def getRowSquares(self, row):
        return [self.squares[row * 3 + 0], self.squares[row * 3 + 1], self.squares[row * 3 + 2]]

    def getColumnSquares(self, column):
        return [self.squares[column + 0], self.squares[column + 3], self.squares[column + 6]]

    def isNumberInRow(self, row, number):
        return number in self.getRowSquares(row)

    def isNumberInColumn(self, column, number):
        return number in self.getColumnSquares(column)


class Sodoku:

    def __init__(self):
        self.blocks = [Block() for i in range(9)]

    def calculateBlockRowColumn(self, row, column):
        sodokuRow = int(row / 3)
        sodokuColumn = int(column / 3)
        blockRow = row % 3
        blockColumn = column % 3
        return [sodokuRow * 3 + sodokuColumn, blockRow, blockColumn]

    def setSquareRowColumn(self, row, column, number):
        block, blockRow, blockColumn = self.calculateBlockRowColumn(row, column)
        self.blocks[block].setSquareRowColumn(blockRow, blockColumn, number)

    def getSquareRowColumn(self, row, column):
        block, blockRow, blockColumn = self.calculateBlockRowColumn(row, column)
        return (self.blocks[block].getSquareRowColumn(blockRow, blockColumn))

    def getRowSquares(self, row):
        return [self.getSquareRowColumn(row, i) for i in range(9)]

    def getColumnSquares(self, column):
        return [self.getSquareRowColumn(i, column) for i in range(9)]

if __name__ == "__main__":
    a = Sodoku()
