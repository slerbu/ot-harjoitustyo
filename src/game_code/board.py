import pygame
from squares import Square

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tile_width = width/8
        self.tile_height = height/8
        self.board = [
            ["dR", "dN", "dB", "dQ", "dK", "dB", "dN", "dR" ],
            ["dP", "dP", "dP", "dP", "dP", "dP", "dP", "dP"],
            ["0",  "0",  "0",  "0",  "0",  "0",  "0",  "0"],
            ["0",  "0",  "0",  "0",  "0",  "0",  "0",  "0"],
            ["0",  "0",  "0",  "0",  "0",  "0",  "0",  "0"],
            ["0",  "0",  "0",  "0",  "0",  "0",  "0",  "0"],
            ["lP", "lP", "lP", "lP", "lP", "lP", "lP", "lP"],
            ["lR", "lN", "lB", "lQ", "lK", "lB", "lN", "lR" ]
        ]
        self.squares = self.create_squares()

    def create_squares(self):
        square_board = []
        for rank in range(8):
            for file in range(8):
                square_board.append(Square(file, rank, self.tile_width, self.tile_height))
        return square_board

    def draw_board(self, screen):
        for square in self.squares:
            square.draw(screen)
    
    def get_square(self, pos):
        for square in self.squares:
            if square.pos == pos:
                return square
            
    def mouse_click(self, mouse_x, mouse_y):
        file = mouse_x // self.tile_width
        rank = mouse_y // self.tile_height
        clicked_square = self.get_square((file, rank))
        clicked_square.highlight = True
        