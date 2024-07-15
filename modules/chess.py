import json
from chessboard import Chessboard
from chessPieces import ChessPiece

# Retrieving the format informations from the json file --> piecesFormat.json
with open("src/files/piecesFormat.json") as jsonFile:
    piecesFormat = json.load(jsonFile)

# Function that gives back the right char to print
def getRightUnicodeChr(item:ChessPiece)->str:
    if item != None and item.name in piecesFormat["Unicode"].keys():
        return piecesFormat["Unicode"][item.name]
    
    return " "

# Function to print the chessboard on the terminal
def printOnCommenadLine(chessboard:Chessboard)->None:
    print("\n")
    print("    A  B  C  D  E  F  G  H")
    print("   —— —— —— —— —— —— —— ——")

    for i in range(0, len(chessboard.chessboard), 1):
        print(str(len(chessboard.chessboard) - i) + " |", end="")
        for item in chessboard.chessboard[i]:
            print(getRightUnicodeChr(item), end=" |")
        print("\n   —— —— —— —— —— —— —— ——")

def __main__():
    chessboard = Chessboard()

    printOnCommenadLine(chessboard)

if __name__ == "__main__":
    __main__()
