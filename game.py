from board import *

def playGame():
    b = Board(3)
    print b

    while b.playCount < len(b.spaces):
        i = raw_input("Next Play: ")
        b.play(int(i))
        print b

    rc = False
    yn = raw_input("Play again? ")
    if yn.lower() == "y":
        rc = True

    return rc

# main
r = playGame()
while r:
    r = playGame()
