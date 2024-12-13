# External libraries used
import pygame # Library for GUI im plementation

# Custom imports
import ObjectlessChessModule as OC

# Version that utilizes a non Objective-oriented approach
def ObjectlessVers()->None:
    run = True
    status = 1
    start = tuple()
    end = tuple()
    chessboard = OC.chessboardGenerator()

    while(run):
        OC.chessboardPrinter(chessboard)

        temp = list(input("Piece to move (coordinates separated by space): ").split(" "))
        start = tuple([int(temp[0]), int(temp[1])])
        temp = list(input("Where to move: ").split(" "))
        end = tuple([int(temp[0]), int(temp[1])])

        moves = OC.allowedMovesSelector(chessboard, start[0], start[1])
        status = OC.move(chessboard, start, end)
        OC.chessboardClearer()
        if status == 0:
            print("Successfully moved %s from %d %d to %d %d" % (OC.chessboardMapper(chessboard[end[0]][end[1]]), start[0], start[1], end[0], end[1]))
        elif status == -1:
            print("Not a valid set of indexes")
        elif status == -2:
            print("Not a valid move")
        elif status == -3:
            print("It is not possible to move an empty square or a blocke piece around!")
        print(moves)
        

def __main__():
    ObjectlessVers()


if(__name__ == "__main__"):
    __main__()