#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import time
from gameConfig import global_arr, Length, Width


# This class is making board which includes side Walls & Walls.
class Board:

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def make_board(self):
        #global_arr = []
        global_arr.clear()
        
        for x in range(self.row):
            global_arr.append([])
            for y in range(self.col):
                global_arr[x].append(' ')

        for x in range(2):
            for y in range(self.col):
                global_arr[x][y] = 'X'

        for x in range(self.row - 2, self.row):
            for y in range(self.col):
                global_arr[x][y] = 'X'

        for x in range(self.row):
            for y in range(2):
                global_arr[x][y] = 'X'
            for y in range(self.col - 2, self.col):
                global_arr[x][y] = 'X'

        for x in range(3, self.row - 2):
            if x % 4 >= 0 and x % 4 <= 1:
                for y in range(3, self.col - 2):
                    if (y - 2) % 8 <= 3 and (y - 2) % 8 >= 0:
                        global_arr[x][y] = ' '
                    elif (y - 2) % 8 >= 4 and (y - 2) % 8 <= 7:
                        global_arr[x][y] = 'X'


bp = Board(Length, Width)
