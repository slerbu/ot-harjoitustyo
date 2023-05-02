import pygame


class Square:
    # Square class that allows handling of squares for chessboard
    """Represents a square on the chessboard,"""

    def __init__(self, file, rank, width, height):
        self.width = width
        self.height = height
        # Coordinates
        self.file = file
        self.rank = rank
        # Position
        self.width_pos = rank*width
        self.height_pos = file*height
        self.pos = (rank, file)
        self.res_pos = (self.width_pos, self.height_pos)
        self.occupying_piece = None
        self.highlight = False
        # Square colors
        self.light_color = (255, 255, 255)
        self.highlight_color = (255, 0, 0)
        self.dark_color = (0, 0, 0)
        if (file + rank) % 2 == 0:
            self.color = "light"
        else:
            self.color = "dark"
        self.tile = pygame.Rect(
            self.width_pos, self.height_pos, self.width, self.height)

    def draw(self, screen):
        if self.highlight:
            pygame.draw.rect(screen, self.highlight_color, (self.tile))
        elif self.color == "light":
            pygame.draw.rect(screen, self.light_color, (self.tile))
        else:
            pygame.draw.rect(screen, self.dark_color, (self.tile))


class Square:
    """Represents a square on a chessboard.

    Attributes:
        -file: The file (column) index of the square, from 0 to 7
        -rank: The rank (row) index of the square, from 0 to 7
        -width: The width of the square in pixels
        -height: The height of the square in pixels
        -width_pos: The x-coordinate of the top-left corner of the square in pixels
        -height_pos: The y-coordinate of the top-left corner of the square in pixels
        -pos: The (rank, file) position of square
        -res_pos: The squares top left corner (x,y) in pixels
        -occupying_piece: Piece occupying square, None if empty
        -highlight: If square is highlighted
        -light_color: The color of the light squares
        -highlight_color: The color of the highlighted squares
        -dark_color: The color of the dark squares
        -color: The color of the square, either "light" or "dark" depending on position
        -tile: The rectangular shape of the square.


    """

    def __init__(self, file, rank, width, height):
        """Initializes a new Square instance with the given position and dimensions.

        Args:
            file: file (column) of square
            rank: rank (row) of square
            width: width of square in pixels
            height: height of square in pixels
        """
        self.width = width
        self.height = height
        self.file = file
        self.rank = rank
        self.width_pos = rank * width
        self.height_pos = file * height
        self.pos = (rank, file)
        self.res_pos = (self.width_pos, self.height_pos)
        self.occupying_piece = None
        self.highlight = False
        self.light_color = (255, 255, 255)
        self.highlight_color = (255, 0, 0)
        self.dark_color = (0, 0, 0)
        self.color = "light" if (file + rank) % 2 == 0 else "dark"
        self.tile = pygame.Rect(
            self.width_pos, self.height_pos, self.width, self.height)

    def draw(self, screen):
        """Draws the square on the given Pygame screen.
        Args:
            screen: pygame surface where you want square to be drawn
        """
        if self.highlight:
            pygame.draw.rect(screen, self.highlight_color, self.tile)
        elif self.color == "light":
            pygame.draw.rect(screen, self.light_color, self.tile)
        else:
            pygame.draw.rect(screen, self.dark_color, self.tile)
