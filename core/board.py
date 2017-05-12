#!/usr/bin/env python
# -- coding: UTF-8 --

class Board(object):
    def __init__(self, lig, col):
        self.grid = []
        for l in range(lig):
            self.grid.append([])
            for c in range(col):
                self.grid[l].append(Cell(l, c))

    def get_grid(self):
        return self.grid

    def get_cell(self, lig, col):
        return self.grid[lig][col]

    def get_width(self):
        return len(self.grid[0])


    def get_height(self):
        return len(self.grid)

class Cell(object):
    def __init__(self, lig, col):
        self.items = []
        self.characters = []
        self.lig = lig
        self.col = col
