'''
Author : Dhruv B Kakadiya

'''

import pygame as pg
from .statics import *
from .pieces import *

class checker_board:
    def __init__(self):
        self.board = []
        self.selected = None
        self.black_l = self.white_l = 12
        self.black_k = self.white_k = 0
        self.create_board()

    def draw_cubes(self, window):
        window.fill(green)
        for row in range(rows):
            for col in range(row % 2, cols, 2):
                pg.draw.rect(window, yellow, (row * sq_size, col * sq_size, sq_size, sq_size))

    def move (self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)
        if (row == rows and row == 0):
            piece.make_king()
            if (piece.color == white):
                self.white_k += 1
            else:
                self.black_k += 1

    def get_piece (self, row, col):
        return self.board[row][col]

    def create_board(self):
        for row in range(rows):
            self.board.append([])
            for col in range(cols):
                if ( col % 2 == ((row + 1) % 2) ):
                    if (row < 3):
                        self.board[row].append(pieces(row, col, white))
                    elif (row > 4):
                        self.board[row].append(pieces(row, col, black))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw (self, window):
        self.draw_cubes(window)
        for row in range(rows):
            for col in range(cols):
                piece = self.board[row][col]
                if (piece != 0):
                    piece.draw(window)