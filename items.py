import numpy as  np
from headerfile import *
from art import *

# bricks shape & sizes :
bricks = np.array(["[####]","[$$$$]","[++++]","[IIII]"])

# Ball :
ball_graphic = "O"

# Paddle :
paddle_size = np.array([5,7,11])

# Brick Orientations :
b_1 = "1-1-1-1-1-1-1-1-1-1-1" + " " + \
      "2-2-2-2-2-2-2-2-2-2-2"
brick_orientation = np.array([b_1])
brick_life_store = [0,1,2,5000]

# instructions :
instructions = fred + art.instructions_art + all_reset + "\n" + \
    fred + "|" + all_reset + " > Press " + fred + "q" + all_reset + " to quit the game                                               " + \
    "                                                                                         " + fred + "|\n" + all_reset + \
    fred + "|" + all_reset + " > Press " + fred + "d" + all_reset + " to move paddle to right                                        " + \
    "                                                                                         " + fred + "|\n" + all_reset + \
    fred + "|" + all_reset + " > Press " + fred + "a" + all_reset + " to move paddle to right                                        " + \
    "                                                                                         " + fred + "|\n" + all_reset + \
    fred + "|" + all_reset + " > Press " + fred + "j" + all_reset + " to fire the ball                                               " + \
    "                                                                                         " + fred + "|\n" + all_reset + \
    fred + "|" + all_reset + " > Press " + fred + "g" + all_reset + " to start the game                                              " + \
    "                                                                                         " + fred + "|\n" + all_reset + \
    fred + "*----------------------------------------------------------------------------------------------------------------------" + \
    "---------------------------------------------*\n"+ all_reset