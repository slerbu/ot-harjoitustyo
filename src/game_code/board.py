from game_code.squares import Square
from game_code.rook import Rook
from game_code.bishop import Bishop
from game_code.knight import Knight
from game_code.queen import Queen
from game_code.pawn import Pawn
from game_code.king import King


class Board:

    """
    A class representing the chess board and responsible for most of the games logic. Other classes are utilized here.

    Attributes:
    - width: the width of the board in pixels
    - height: the height of the board in pixels
    - tile_width: the width of a single square in pixels
    - tile_height: the height of a single square in pixels
    - mapping: a list representing the starting positions of the pieces on the board
    - squares: list of square objects representing the board
    - clicked_piece: currently selected piece
    - turn: the color of the player whose turn it is (alternating between "white" and "black" (white first))) 


    """

    def __init__(self, width, height):
        """
        Class constructor, initialized a new board
        Args:
            width: width of board in pixels
            height: height of board in pixels
        """
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
        """
        Generates squares for the entire chess board

        Returns: list of squares in chess board
        """
        square_board = []
        for rank in range(8):
            for file in range(8):
                square_board.append(
                    Square(file, rank, self.tile_width, self.tile_height))
        return square_board

    def draw_board(self, screen):
        """
        Draws board onto given pygame surface

        Args:
            screen: Pygame surface to draw board on

        """
        for square in self.squares:
            square.draw(screen)
            if square.occupying_piece:
                square.occupying_piece.draw(screen)

    def setup_pieces(self):
        """
        Adds appropriate pieces to appropriate squares on board (list of squares)
        """

        for file in range(len(self.mapping)):
            for rank in range(len(self.mapping)):
                if self.mapping[file][rank][0] != "0":
                    square = self.get_square((rank, file))
                    if self.mapping[file][rank][1] == "R":
                        square.occupying_piece = Rook(
                            "black" if self.mapping[file][rank][0] == "b" else "white", (rank, file), self)
                    elif self.mapping[file][rank][1] == "N":
                        square.occupying_piece = Knight(
                            "black" if self.mapping[file][rank][0] == "b" else "white", (rank, file), self)
                    elif self.mapping[file][rank][1] == "B":
                        square.occupying_piece = Bishop(
                            "black" if self.mapping[file][rank][0] == "b" else "white", (rank, file), self)
                    elif self.mapping[file][rank][1] == "Q":
                        square.occupying_piece = Queen(
                            "black" if self.mapping[file][rank][0] == "b" else "white", (rank, file), self)
                    elif self.mapping[file][rank][1] == "K":
                        square.occupying_piece = King(
                            "black" if self.mapping[file][rank][0] == "b" else "white", (rank, file), self)
                    elif self.mapping[file][rank][1] == "P":
                        square.occupying_piece = Pawn(
                            "black" if self.mapping[file][rank][0] == "b" else "white", (rank, file), self)

    def attacking_squares(self, color, board):
        """
        NOT DONE. 
        Checks what squares are attacked by a player. To be utilized in function that checks for checks.
        Args:
            color: color of pieces to to checks attacks for
            board: ?
        """
        attacked_squares = []
        for square in self.squares:
            if square.occupying_piece and square.occupying_piece.color != self.turn:
                return "bruh"

    def get_square(self, pos):
        """
        Get square in given position on board
        Args:
            pos: (file, rank) position on board
        Returns:
            Square in given position
        """
        for square in self.squares:
            if square.pos == pos:
                return square

    def update_pieces(self):
        """
        Updates the location of pieces on the UI
        """
        for square in self.squares:
            if square.occupying_piece:
                square.occupying_piece.rect.x = square.occupying_piece.pos[0] * \
                    self.tile_width
                square.occupying_piece.rect.y = square.occupying_piece.pos[1] * \
                    self.tile_height

    def mouse_click(self, mouse_x, mouse_y, board):
        """
        Handles mouseclicks. Moves pieces appropriately between Square objects.

        Args:
            mouse_x: mouse x position in pixels
            mouse_y: mouse y position in pixels
            board: board which squares to handle (with some thought seems pretty useless? probs gonna change to self in future)

        """
        file = mouse_x // self.tile_width
        rank = mouse_y // self.tile_height
        clicked_square = self.get_square((file, rank))
        if clicked_square.occupying_piece:
            for square in self.squares:

                if square.pos in clicked_square.occupying_piece.get_legal_moves(board):
                    square.highlight = True

        # clicked_square.highlight = True anda
        if clicked_square.occupying_piece and not self.clicked_piece:
            self.old_square = clicked_square

            # print(clicked_square.occupying_piece.type)
            # print(clicked_square.occupying_piece.color)

            if clicked_square.occupying_piece.color == self.turn and not self.clicked_piece:
                self.clicked_piece = clicked_square.occupying_piece
                self.old_piece = self.clicked_piece
                return
        if self.clicked_piece:

            if clicked_square.pos in self.clicked_piece.get_legal_moves(board):
                clicked_square.occupying_piece = self.old_piece
                # print(self.clicked_piece.pos)

                self.clicked_piece.move(clicked_square.pos)
                if not self.old_piece.has_moved:
                    self.old_piece.has_moved = True
                self.old_square.occupying_piece = None
                # print(self.clicked_piece.pos)

                self.clicked_piece = None
                self.clicked_square = None
                self.old_piece = None
                for square in self.squares:
                    square.highlight = False

                if self.turn == "white":
                    self.turn = "black"
                else:
                    self.turn = "white"

            else:
                self.clicked_piece = None
                self.clicked_square = None
                self.old_piece = None
                for square in self.squares:
                    square.highlight = False

        board.update_pieces()
