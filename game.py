#!/usr/bin/env python
# -- coding: UTF-8 --

from core.board import Board
from core.character import Player
from core.display import ConsoleBoard

board = ConsoleBoard(Board(20, 20), Player(50, 1))
spawn_cell = board.get_cell(0, 0)
board.move_player(spawn_cell)
while True:
    board.display()
    new_cell = board.wait_move()
    board.move_player(new_cell)
