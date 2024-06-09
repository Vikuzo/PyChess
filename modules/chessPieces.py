class ChessPiece(object):
    def __init__(self, row:int, column:int, color:chr):
        self.row = row
        self.column = column
        self.color = color

    # Returns a string containing cooordinates of the piece
    def __str__(self)->str:
        return str(self.color) + ":(" + str(self.row) + ", " + str(self.column) + ")"

    # Declaration decorators for attribute: row
    @property
    def row(self)->int:
        return self.__row
    
    @row.setter
    def row(self, row:int)->None:
        if row not in range(0, 8) and not None:
            raise ValueError("Unacceptable index for a chess piece")
        self.__row = row
    
    # Declaration decorators for attribute: column
    @property
    def column(self)->int:
        return self.__column
    
    @column.setter
    def column(self, column:int)->None:
        if column not in range(0, 8) and not None:
            raise ValueError("Unacceptable index for a chess piece")
        self.__column = column

    # Declaration decorators for attribute: color
    @property
    def color(self)->chr:
        return self.__color
    
    @color.setter
    def color(self, color:chr)->None:
        if color != 'w' and color != 'b':
            raise ValueError("Unacceptable color for a chess piece")
        self.__color = color

    # Abstract method that will implement what moves can be made by a
    # player for that specific piece
    def allowedMoves(self, chessboard:list[list])->tuple:
        return (None, None)

    # Defines the modality in which the piece can move
    # column: the new column for the piece
    # row: the new row for the piece
    # returns true if the piece can be moved in the new position
    def move(self, row:int, column:int)->bool:
        if (row, column) in self.allowedMoves():
            self.row = row
            self.column = column
            return True
        return False

    # Returns a tuple consisting of the current row (index 0) and column
    # (index 1) of the piece
    def getPosition(self)->tuple[int, int]:
        return (self.row, self.column)
    
    # Returns True if the piece is still on the board,
    # False otherwise
    def isAlive(self)->bool:
        if self.getPosition() == (None, None):
            return False
        return True
    
class Pawn(ChessPiece):
    def __init__(self, row:int, column:int, color:chr):
        super().__init__(row, column, color)
        self.__firstMove = True
        self.__transformable = False

    # Get for transformable
    @property
    def transformable(self)->bool:
        return self.__transformable

    # Allowed moves for a pawn object
    def allowedMoves(self, chessboard:list[list])->tuple:
        allowedMoves = list()
        
        if self.color == 'w':
            direction = 1
        else:
            direction = -1
        
        try:
            if self.__firstMove:
                if chessboard[self.getPosition()[0]][self.getPosition()[1] + direction] == None \
                and chessboard[self.getPosition()[0]][self.getPosition()[1] + (direction * 2)] == None:
                    allowedMoves.append((self.getPosition()[0], self.getPosition()[1] + (2*direction)))
        except IndexError:
            raise IndexError("There should not be any error occurring at this state") 

        try:
            if chessboard[self.getPosition()[0]][self.getPosition()[1] + direction] == None:
                allowedMoves.append((self.getPosition()[0], self.getPosition()[1] + direction))
        except IndexError:
            self.__transformable = True
        
        # this two tries are split to guarantee that the corrispective if
        # is performed even if one of the two gives an error
        try:
            if chessboard[self.getPosition()[0] + direction][self.getPosition()[1] + direction].color != self.color:
                allowedMoves.append((self.getPosition()[0] + direction, self.getPosition()[1] + direction))
        except IndexError:
            pass

        try:
            if chessboard[self.getPosition()[0] - direction][self.getPosition()[1] + direction].color != self.color:
                allowedMoves.append((self.getPosition()[0] - direction, self.getPosition()[1] + direction))
        except IndexError:
            pass

        return tuple(allowedMoves)
    
    # We ensure that after the first time we cant move for more than two
    # tile a pawn
    def move(self, row:int, column:int):
        if super().move(row, column) and self.__firstMove:
            self.__firstMove = False

# TO IMPLEMENT
class Rook(ChessPiece):
    def __init__(self, row:int, column:int, color:chr):
        super().__init__(row, column, color)

# TO IMPLEMENT
class Knight(ChessPiece):
    def __init__(self, row:int, column:int, color:chr):
        super().__init__(row, column, color)

# TO IMPLEMENT
class Bishop(ChessPiece):
    def __init__(self, row:int, column:int, color:chr):
        super().__init__(row, column, color)

# TO IMPLEMENT
class Queen(ChessPiece):
    def __init__(self, row:int, column:int, color:chr):
        super().__init__(row, column, color)

#TO IMPLEMENT
class King(ChessPiece):
    def __init__(self, row:int, column:int, color:chr):
        super().__init__(row, column, color)
