'''
Author : Dhruv B Kakadiya

'''

from .statics import *
import pygame as pg

class pieces:

    padding = 17
    outline  = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False

        '''if (self.color == yellow):
            self.direction = -1
        else:
            self.direction = 1'''

        self.x = self.y = 0
        self.calculate_pos()

    def calculate_pos (self):
        self.x = ((sq_size * self.col) + (sq_size // 2))
        self.y = ((sq_size * self.row) + (sq_size // 2))

    def make_king (self):
        self.king = True

    def draw (self, window):
        radd = ((sq_size // 2) - self.padding)
        pg.draw.circle(window, gray, (self.x, self.y), radd + self.outline)
        pg.draw.circle(window, self.color, (self.x, self.y), radd)
        if (self.king):
            window.blit(crown, ((self.x - crown.get_width() // 2), (self.y - crown.get_height() // 2)))

    def move (self, row, col):
        self.row = row
        self.col = col
        self.calculate_pos()

    def __repr__(self):
        return str(self.color)

