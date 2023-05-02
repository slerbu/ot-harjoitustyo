class Piece:
    """
    Class to for chess pieces.
    To be inherited by each type of piece

    Attributes:
        -color: color of piece
        -pos: position of piece
        -has_moved: whether piece has from starting position or not
    """

    def __init__(self, color, position, board):
        """Class constructor, initializes piece

        Args:
            color: color of piece
            position: position of piece on board
            board: board which piece shall be attached to

        """
        self.color = color
        self.pos = position
        self.has_moved = False

        self.board = board

    def draw(self, screen):
        """
        Draw piece onto UI

        Args:
            screen: pygame surface to draw piece on
        """

        screen.blit(self.image, self.rect)

    def move(self, new_pos):
        """
        Move piece on the mapping array (now noticing that probably not needed with the utilization of board and square objects, might get deleted in future)
        Args:
            new_pos: new position of piece that is to be moved
        """

        old_y, old_x = self.pos
        new_y, new_x = new_pos
        self.board.mapping[old_x][old_y] = "0"
        if self.type == "Knight":
            self.board.mapping[new_x][new_y] = f"{self.color[0]}N"
        else:
            self.board.mapping[new_x][new_y] = f"{self.color[0]}{self.type[0]}"
        self.pos = new_pos
