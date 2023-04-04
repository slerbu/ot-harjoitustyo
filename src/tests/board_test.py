import unittest
import pygame
import sys
sys.path.append("~/ot-harjoitustyo")

from squares import Square
from board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.gameboard = Board(640,640)
        

    #Tests that the create_squares function generates squares and gives them appropriate coordinates
    def test_appropriate_coordinates_x(self):
        assert (self.gameboard.create_squares()[4].x, self.gameboard.create_squares()[4].y) == (4,0)

    def test_appropriate_coordinates_y(self):
        assert (self.gameboard.create_squares()[17].x, self.gameboard.create_squares()[17].y) == (1,2)