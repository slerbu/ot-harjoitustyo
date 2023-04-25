import pygame
from game_code.squares import Square
from game_code.piece import Piece


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tile_width = width/8
        self.tile_height = height/8
        self.mapping = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["0",  "0",  "0",  "0",  "0",  "0",  "0",  "0"],
            ["0",  "0",  "0",  "0",  "0",  "0",  "0",  "0"],
            ["0",  "0",  "0",  "0",  "0",  "0",  "0",  "0"],
            ["0",  "0",  "0",  "0",  "0",  "0",  "0",  "0"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        self.squares = self.create_squares()
        self.clicked_piece = None
        self.turn = "white"

    def create_squares(self):
        square_board = []
        for rank in range(8):
            for file in range(8):
                square_board.append(
                    Square(file, rank, self.tile_width, self.tile_height))
        return square_board

    def draw_board(self, screen):
        for square in self.squares:
            square.draw(screen)
            if square.occupying_piece:
                square.occupying_piece.draw(screen)

    def setup_pieces(self):
        for y in range(len(self.mapping)):
            for x in range(len(self.mapping)):
                if self.mapping[y][x][0] != "0":
                    square = self.get_square((x, y))
                    if self.mapping[y][x][1] == "R":
                        square.occupying_piece = Piece(
                            "black" if self.mapping[y][x][0] == "b" else "white", (x, y), self, "Rook")
                    elif self.mapping[y][x][1] == "N":
                        square.occupying_piece = Piece(
                            "black" if self.mapping[y][x][0] == "b" else "white", (x, y), self, "Knight")
                    elif self.mapping[y][x][1] == "B":
                        square.occupying_piece = Piece(
                            "black" if self.mapping[y][x][0] == "b" else "white", (x, y), self, "Bishop")
                    elif self.mapping[y][x][1] == "Q":
                        square.occupying_piece = Piece(
                            "black" if self.mapping[y][x][0] == "b" else "white", (x, y), self, "Queen")
                    elif self.mapping[y][x][1] == "K":
                        square.occupying_piece = Piece(
                            "black" if self.mapping[y][x][0] == "b" else "white", (x, y), self, "King")
                    elif self.mapping[y][x][1] == "P":
                        square.occupying_piece = Piece(
                            "black" if self.mapping[y][x][0] == "b" else "white", (x, y), self, "Pawn")

    def get_square(self, pos):
        for square in self.squares:
            if square.pos == pos:
                return square

    def mouse_click(self, mouse_x, mouse_y):
        file = mouse_x // self.tile_width
        rank = mouse_y // self.tile_height
        clicked_square = self.get_square((file, rank))
        #clicked_square.highlight = True
        if clicked_square.occupying_piece:
            print("lol")

            if clicked_square.occupying_piece.color == self.turn and not self.clicked_piece:
                print("ebin")
                self.clicked_piece = clicked_square.occupying_piece
                return
        if self.clicked_piece:
            # if clicked_square.pos in self.clicked_piece.legal_moves:
            
            self.clicked_piece.move(clicked_square.pos)
            self.get_square(self.clicked_piece.pos).occupying_piece = None
            clicked_square.occupying_piece = self.clicked_piece
            self.clicked_piece = None
           
            if self.turn == "white":
                self.turn = "black"
            else:
                self.turn = "white"


        print(self.mapping)
