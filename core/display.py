#!/usr/bin/env python
# -- coding: UTF-8 --

from .board import Board, Cell
from .character import Character, Player, Chicken

class BoardDisplayer(Board):

    def __init__(self, board, player):
        self.board = board
        self.player = player

    def display(self,board):
        pass

    def wait_move(self):
        lig = self.player.position.lig
        col = self.player.position.col
        direction = raw_input("direction ? :")
        if direction == "z" and lig -1 >= 0 :
            lig -= 1
        elif direction == "q" and col -1 >=0 :
            col -= 1
        elif direction == "d" and col +1 < self.get_width() :
            col += 1
        elif direction == "s" and lig +1 < self.get_height() :
            lig += 1
        return self.get_cell(lig, col)


    def get_grid(self):
        return self.board.grid

    def get_width(self):
        return len(self.board.grid[0])

    def get_height(self):
        return len(self.board.grid)

    def get_cell(self, lig, col):
        return self.board.get_cell(lig, col)

class ConsoleBoard(BoardDisplayer):

    def display(self):
        res = ""
        for lig in range(self.get_height()):
            for col in range(self.get_width()):
                cell = self.get_cell(lig,col)
                if self.player in cell.characters:
                    res += "X"
                else :
                    res += "."
            res += "\n"
        print res

    def move_player(self,cell):
        self.player.move(cell)
