import json
from chessboard import Chessboard
from chessPieces import ChessPiece

# Retrieving the format informatino from the json file --> piecesFormat.json
with open("src/files/piecesFormat.json") as jsonFile:
    piecesFormat = json.load(jsonFile)

# Function that gives back the right char to print
def getRightUnicodeChr(item:ChessPiece)->str:
    if item != None and item.name in piecesFormat["Unicode"].keys():
        return piecesFormat["Unicode"][item.name]
    
    return " "

# Function to print the chessboard on the terminal
def printOnCommenadLine(chessboard:Chessboard)->None:
    print("\n\n")
    print(" —— —— —— —— —— —— —— ——")

    for list in chessboard.chessboard:
        print("|", end="")
        for item in list:
            print(getRightUnicodeChr(item), end=" |")
        print("\n —— —— —— —— —— —— —— ——")

def __main__():
    chessboard = Chessboard()

    printOnCommenadLine(chessboard)

if __name__ == "__main__":
    __main__()
