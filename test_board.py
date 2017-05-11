#!/usr/bin/env python
# -- coding: UTF-8 --
from core.board import Board, Cell

import unittest

class TestBoard(unittest.TestCase):

    def testBoardInitialisation(self):
        board = Board(50, 50)
        self.assertTrue(len(board.grid) == 50)
        for lig in range(50):
            self.assertTrue(len(board.grid[lig]) == 50)
            for col in range(50):
                cell = board.grid[lig][col]
                self.assertTrue(isinstance(cell, Cell))


if __name__ == '__main__':
    unittest.main()
