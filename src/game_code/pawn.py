import pygame
from game_code.piece import Piece


class Pawn(Piece):
    """
    Class representing a pawn chess piece
    Attributes:
        color: Color of pawn, "white" or "black"
        pos: Position on board
        board: The board where pawn is placed
        type: type of chess piece -> pawn
        image: image of pawn
        rect: rectangular area of pawn image

    """

    def __init__(self, color, position, board):
        """
        Class constructor, initializes pawn object
        Args:
            color: color of pawn, "black" or "white"
            position: position on board
            board: board where pawn is placed
        """
        super().__init__(color, position, board)
        self.type = "Pawn"
        self.image = pygame.image.load(
            f"src/game_code/imgs/{self.color}_{self.type.lower()}.png")
        self.image = pygame.transform.scale(
            self.image, (int(board.tile_width), int(board.tile_height)))
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0] * board.tile_width
        self.rect.y = self.pos[1] * board.tile_height

    def get_legal_moves(self, board):
        """
        Function to get a list of legal positions for pawn to move to on chess board

        Args:
            board: board to check positions on

        Returns:
            list of legal positions to move to
        """

        legal_moves = []
        change = 1
        if self.color == "white":
            change *= (-1)
            if board.mapping[self.pos[1]+change][self.pos[0]-1][0] == "b":
                legal_moves.append((self.pos[0]-1, self.pos[1]+change))
            if self.pos[0] < 7 and board.mapping[self.pos[1]+change][self.pos[0]+1][0] == "b":
                legal_moves.append((self.pos[0]+1, self.pos[1]+change))

        if not self.has_moved:
            legal_moves.append((self.pos[0], self.pos[1]+change))
            legal_moves.append((self.pos[0], self.pos[1]+2*change))
        else:
            legal_moves.append((self.pos[0], self.pos[1]+change))

            if board.mapping[self.pos[1]+change][self.pos[0]-1][0] == "w":
                legal_moves.append((self.pos[0]-1, self.pos[1]+change))
            if self.pos[0] < 7 and board.mapping[self.pos[1]+change][self.pos[0]+1][0] == "w":
                legal_moves.append((self.pos[0]+1, self.pos[1]+change))

        return legal_moves
