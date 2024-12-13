import os # Library used to call upon the operating system
import json # A library that allows the translation of json files

with open("src/files/ObjectlessPiecesInfo.json") as jsonfile:
    piecesInfo = json.load(jsonfile)

# Maps the piece from the character representing it to UNICODE that represents tha actual piece (or space)
def chessboardMapper(piece:chr)->chr:
    return piecesInfo["name"][piece]

# Returns a freshly created chessboard
def chessboardGenerator()->list[list]:
    return [["2", "4", "3", "1", "0", "3", "4", "2"],
            ["5", "5", "5", "5", "5", "5", "5", "5"],
            ["v", "v", "v", "v", "v", "v", "v", "v"],
            ["v", "v", "v", "v", "v", "v", "v", "v"],
            ["v", "v", "v", "v", "v", "v", "v", "v"],
            ["v", "v", "v", "v", "v", "v", "v", "v"],
            ["b", "b", "b", "b", "b", "b", "b", "b"],
            ["8", "a", "9", "7", "6", "9", "a", "8"]]

# Prints the chessboard on the terminal
def chessboardPrinter(chessboard:list[list])->None:
    print("\n")
    print("    A  B  C  D  E  F  G  H")
    print("   —— —— —— —— —— —— —— ——")

    c = 0

    for list in chessboard:
        print(str(len(chessboard) - c) + " |", end="")
        for item in list:
            print(chessboardMapper(item), end=" |")
        print("\n   —— —— —— —— —— —— —— ——")
        c += 1
    return None

# Function used to clean the terminal, it enables us to avoid importing the os library to our main program aswell
def chessboardClearer()->None:
    os.system("cls")

# Definition of single moves handlers for every piece
def pawnAllowedMoves(chessboard: list[list], r: int, c: int, dir: int)->tuple:
    moves = list()

    # Checking if the pawn is in the last row -> allow transformation
    if(r == 0 or r == 7):
        return (-1,-1) # flag for transformation
    
    # Checking for the pieces possibility to move up 2 when first moving from original position
    if((r == 1 and dir == 1) or (r == 6 and dir == -1)):
        if(chessboard[r + dir][c] == "v" and chessboard[r + (dir*2)][c] == "v"):
            moves.append((r+(dir*2), c))
    
    # Checking if the piece can move forward for a single square
    if(chessboard[r + dir][c] == "v"):
        moves.append((r + dir, c))

    # Finding out enemy pieces
    if(chessboard[r][c] in piecesInfo["color"]["white"]):
        eatable = list(piecesInfo["color"]["black"])
    elif(chessboard[r][c] in piecesInfo["color"]["black"]):
        eatable = list(piecesInfo["color"]["white"])
    
    # Checking for eatable pieces and en passant
    if(c + 1 < 8):
        if(chessboard[r + dir][c + 1] in eatable):
            moves.append((r + dir, c + 1))
        if(chessboard[r][c + 1] in eatable and chessboard[r + dir][c + 1] == "v"):
            moves.append((-2, c + 1)) # -2 on the row is a flag to signal that the move is an en passant and needs to be handled specifically
    if(c - 1 > -1):    
        if(chessboard[r + dir][c - 1] in eatable):
            moves.append((r + dir, c - 1))
        if(chessboard[r][c - 1] in eatable and chessboard[r + dir][c - 1] == "v"):
            moves.append((-2, c - 1))

    return tuple(moves)

def rookAllowedMoves(chessboard: list[list], r: int, c: int)->tuple:
    moves = list()

    return tuple(moves)

def knightAllowedMoves(chessboard: list[list], r: int, c: int)->tuple:
    moves = list()
    eatable = list()

    # Selects what are the squares where a piece can move if they are not empty (and if they are empty)
    if(chessboard[r][c] in piecesInfo["color"]["white"]):
        eatable = list(piecesInfo["color"]["black"])
    elif(chessboard[r][c] in piecesInfo["color"]["black"]):
        eatable = list(piecesInfo["color"]["white"])
    eatable.append("v")

    # Checks up + right
    if(r + 2 < 8 and c + 1 < 8):
        if(chessboard[r + 2][c + 1] in eatable):
            moves.append((r + 2, c + 1))

    # Checks up + left
    if(r + 2 < 8 and c - 1 > -1):
        if(chessboard[r + 2][c - 1] in eatable):
            moves.append((r + 2, c - 1))
    
    # Checks left + up
    if(r + 1 < 8 and c - 2 > -1):
        if(chessboard[r + 1][c - 2] in eatable):
            moves.append((r + 1, c - 2))
    
    # Checks left + down
    if(r - 1 > -1 and c - 2 > -1):
        if(chessboard[r - 1][c - 2] in eatable):
            moves.append((r - 1, c - 2))

    # Checks right + up
    if(r + 1 < 8 and c + 2 < 8):
        if(chessboard[r + 1][c + 2] in eatable):
            moves.append((r + 1, c + 2))

    # Checks right + down
    if(r - 1 > -1 and c + 2 < 8):
        if(chessboard[r - 1][c + 2] in eatable):
            moves.append((r - 1, c + 2))

    # Checks down + right
    if(r - 2 > -1 and c + 1 < 8):
        if(chessboard[r - 2][c + 1] in eatable):
            moves.append((r - 2, c + 1))

    # Checks down + left
    if(r - 2 > -1 and c - 1 > -1):
        if(chessboard[r - 2][c - 1] in eatable):
            moves.append((r - 2, c - 1))

    return tuple(moves)

def bishopAllowedMoves(chessboard: list[list], r: int, c: int)->tuple:
    moves = list()

    return tuple(moves)

def queenAllowedMoves(chessboard: list[list], r: int, c: int)->tuple:
    moves = list()

    return tuple(moves)

def kingAllowedMoves(chessboard: list[list], r: int, c: int)->tuple:
    moves = list()

    return tuple(moves)

# Checks if the inserted couple of index is in the valid range
def checkIndex(indexes: tuple)->int:
    if(indexes[0] >= 8 or indexes[0] <= -1 or indexes[1] >= 8 or indexes[1] <= -1):
        return -1
    return 0

# Swaps the value of the square start with the one in square end and vice versa
def swap(chessboard:list[list], start:tuple, end:tuple):
    # Checks if the pieces if in the square I want to move there is a piece I'm eating up
    if(chessboard[end[0]][end[1]] != "v"):
        chessboard[end[0]][end[1]] = "v"

    # Swap
    temp = chessboard[start[0]][start[1]]
    chessboard[start[0]][start[1]] = chessboard[end[0]][end[1]]
    chessboard[end[0]][end[1]] = temp

# Function that decides what function to use to give the allowed possible moves of a piece
def allowedMovesSelector(chessboard: list[list], r: int, c: int)->tuple:
    if chessboard[r][c] == "v":
        return ()

    if chessboard[r][c] == "0" or chessboard[r][c] == "6":
        return kingAllowedMoves(chessboard, r, c)
    if chessboard[r][c] == "1" or chessboard[r][c] == "7":
        return queenAllowedMoves(chessboard, r, c)
    if chessboard[r][c] == "2" or chessboard[r][c] == "8":
        return rookAllowedMoves(chessboard, r, c)
    if chessboard[r][c] == "3" or chessboard[r][c] == "9":
        return bishopAllowedMoves(chessboard, r, c)
    if chessboard[r][c] == "4" or chessboard[r][c] == "a":
        return knightAllowedMoves(chessboard, r, c)
    if chessboard[r][c] == "5":
        return pawnAllowedMoves(chessboard, r, c, 1)
    if chessboard[r][c] == "b":
        return pawnAllowedMoves(chessboard, r, c, -1)
    
    input("Something went not as expected!")
    os._exit()

# Verifies and applies, where possible, the moves the player wants to make
def move(chessboard: list[list], start: tuple, end: tuple)->int:
    if(checkIndex(start) == -1 or checkIndex(end) == -1):
        return -1 # not a valid set of indexes
    
    moves = allowedMovesSelector(chessboard, start[0], start[1])
    print(moves)
    if(end in moves):
        swap(chessboard, start, end)
        return 0 # Successfully moved
    elif moves != ():
        return -2 # not a valid move
    return -3 # It is not possible to move an empty square around!"