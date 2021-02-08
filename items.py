import numpy as  np
from headerfile import *
from art import *

# bricks shape & sizes :
bricks = np.array(["[####]","[$$$$]","[++++]","[IIII]"])

# Ball :
Ball = "O"

# Paddle :
paddle = np.array(["<=====>","<=======>","<===========>"])

# Brick Orientations :
o_1 = "1-1-1-1-1-1-1-1-1-1-1" + " " + \
      "2-2-2-2-2-2-2-2-2-2-2"
brick_orientation = np.array(o_1)

# instructions :
instructions = fred + art.instructions_art + all_reset + "\n" + \
    " Press " + fred + "q" + all_reset + " to quit the game\n" + \
    " Press " + fred + "d" + all_reset + " to move paddle to right\n" + \
    " Press " + fred + "a" + all_reset + " to move paddle to right\n" + \
    " Press " + fred + "j" + all_reset + " to fire the ball\n" + \
    " Press " + fred + "g" + all_reset + " to start the game\n"