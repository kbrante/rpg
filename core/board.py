#!/usr/bin/env python
# -- coding: UTF-8 --

class Board(object):
    def __init__(self, lig, col):
        self.grid = []
        for l in range(lig):
            self.grid.append([])
            for l in range(col):
                self.grid[l].append(Cell())

class Cell(object):
    def __init__(self):
        pass
