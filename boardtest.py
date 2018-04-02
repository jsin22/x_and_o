from board import *

b = Board(3)

b.play(4)
assert b.spaces[4] == 'X'

assert b.play(4) == False

b.play(3) 
assert b.spaces[3] == 'O'

b.play(5)
assert b.spaces[4] == 'X'

assert b.play(12) == False

print "All tests passed!"
