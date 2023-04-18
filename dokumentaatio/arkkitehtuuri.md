```mermaid
classDiagram

    class Board {
        generate_squares
        draw_squares
        in_check
    }

    class Square {
        create_square
    }

    class Piece {
        color
        pos(square)
        get_legal_moves
    }


    

    class King {
        has_legal_moves
    }

    Board <--> Square
    Board <--> Piece
    King <--> Piece
 
