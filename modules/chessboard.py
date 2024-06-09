from chessPieces import *

class Chessboard(object):
    def __init__(self):
        self.restart()

    # Get the chessboard
    @property
    def chessboard(self)->list[list]:
        return self.__chessboard

    # Defines a new standard chessboard
    def restart(self)->None:
        self.__chessboard = [
            [Rook(0, 0, 'b'), Knight(0, 1, 'b'), Bishop(0, 2, 'b'), Queen(0, 3, 'b'), King(0, 4, 'b'), Bishop(0, 5, 'b'), Knight(0, 6, 'b'), Rook(0, 7, 'b')],
            [Pawn(1, 0, 'b'), Pawn(1, 1, 'b'), Pawn(1, 2, 'b'), Pawn(1, 3, 'b'), Pawn(1, 4, 'b'), Pawn(1, 5, 'b'), Pawn(1, 6, 'b'), Pawn(1, 7, 'b')],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [Pawn(6, 0, 'w'), Pawn(6, 1, 'w'), Pawn(6, 2, 'w'), Pawn(6, 3, 'w'), Pawn(6, 4, 'w'), Pawn(6, 5, 'w'), Pawn(6, 6, 'w'), Pawn(6, 7, 'w')],
            [Rook(7, 0, 'w'), Knight(7, 1, 'w'), Bishop(7, 2, 'w'), Queen(7, 3, 'w'), King(7, 4, 'w'), Bishop(7, 5, 'w'), Knight(7, 6, 'w'), Rook(7, 7, 'w')]
        ]
