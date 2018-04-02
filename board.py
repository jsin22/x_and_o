from platform import system as system_name
import os

class Board(object):
    def __init__(self, size):
        self.size = size
        self.spaces = dict()
        self.playCount = 0
        for i in range(1, (size * size) + 1):
            self.spaces[i] = str(i)

    def __str__(self):
        if system_name().lower() == 'windows':
            os.system('cls')
        else:
            os.system('clear')

        s = str()
        for i in range(self.size):
            for j in range(i*self.size+1, (i*self.size)+(self.size+1)):
                if j < 10:
                    s+=self.spaces[j] + " |"
                else:
                    s+=self.spaces[j] + "|"
            s+="\n"
        return s

    def play(self, i):
        if i > len(self.spaces):
            print "Pay attention, invalid play!"
            return False
        if self.spaces[i] == 'X' or self.spaces[i] == 'O':
            print "Space has been taken, try again!"
            return False
        else:
            self.playCount += 1
            self.spaces[i] = 'X' if self.playCount%2 else 'O'
