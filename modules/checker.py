'''
Author : Dhruv B Kakadiya

'''

import pygame as pg
from .checker_board import *
from .statics import *
from .pieces import *

class checker:
    def __init__(self, window):
        self._init()
        self.window = window

    def update (self):
        self.board.draw(self.window)
        pg.display.update()

    def _init(self):
        self.select = None
        self.board = checker_board()
        self.turn = black
        self.valid_moves = {}

    def reset (self):
        self._init()

    def selectrc(self, row, col):
        if (self.select):
            result = self._move(row, col)

    def _move(self, row, col):
        pass