import sys
import unittest

sys.path.append('/home/lindgseb/ot-harjoitustyo/src/game_code')
#print(sys.path)

from game_code.board import Board

if True:
    class TestBoard(unittest.TestCase):
        def setUp(self):
            self.gameboard = Board(640,640)
            

        #Tests that the create_squares function generates squares and gives them appropriate coordinates
        def test_appropriate_coordinates_x(self):
            assert (self.gameboard.create_squares()[4].file, self.gameboard.create_squares()[4].rank) == (4,0)

        def test_appropriate_coordinates_y(self):
            assert (self.gameboard.create_squares()[17].file, self.gameboard.create_squares()[17].rank) == (1,2)