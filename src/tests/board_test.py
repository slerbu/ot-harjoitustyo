from game_code.board import Board
import sys
import unittest

sys.path.append('/home/lindgseb/ot-harjoitustyo/src/game_code')
# print(sys.path)


if True:
    class TestBoard(unittest.TestCase):
        def setUp(self):
            self.gameboard = Board(640, 640)

        # Tests that the create_squares function generates squares and gives them appropriate coordinates

        def test_appropriate_coordinates_x(self):
            assert (self.gameboard.create_squares()[
                    4].file, self.gameboard.create_squares()[4].rank) == (4, 0)

        def test_appropriate_coordinates_y(self):
            assert (self.gameboard.create_squares()[
                    17].file, self.gameboard.create_squares()[17].rank) == (1, 2)

        # Tests that the mouse click works appropriate related to the coordinates of the scares and highlights the correct square

        # Tests the get_square function

        def test_get_square(self):
            board = Board(800, 800)
            square = board.get_square((0, 0))
            assert square.file == 0
            assert square.rank == 0

        def test_mouse_click(self):
            b = Board(800, 800)
            b.setup_pieces()
            assert b.get_square((0, 1)).occupying_piece.type == "Pawn"

        def test_piece_init(self):
            b = Board(800, 800)
            b.setup_pieces()
            piece = b.get_square((0, 0)).occupying_piece
            assert piece.type == "Rook"
