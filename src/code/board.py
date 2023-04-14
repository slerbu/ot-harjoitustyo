import pygame
from squares import Square

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
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


    
    def create_squares(self):
        square_board = []
        for y in range(8):
            for x in range(8):
                square_board.append(Square(x, y, self.width/8, self.height/8))
        
        return square_board

    def draw_board(self, screen):
        for square in self.create_squares():
            pygame.draw.rect(screen, square.square_color, (square.actual_x, square.actual_y, square.width, square.height ))

    

    