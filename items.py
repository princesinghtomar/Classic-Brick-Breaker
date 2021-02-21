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
b_1 = "1-1-1-1-1-1-2-2-1-1-1" + " " + \
      "2-2-3-0-0-0-0-0-0-0-2"
b_2 = "1-1-1-0-1-1-3-3-1-2-1" + " " + \
      "0-0-0-0-0-0-0-2-1-1-2" + " " + \
      "0-0-0-0-0-2-1-2-3-2-2"
b_3 = "1-1-3-3-3-1-0-0-1-1-1" + " " + \
      "2-2-0-0-0-0-0-0-0-0-2"
brick_orientation = np.array([b_1,b_2,b_3])
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
    fred + "|" + all_reset + " > Press " + fred + "k" + all_reset + " to release ball                                                " + \
    "                                                                                         " + fred + "|\n" + all_reset + \
    fred + "|" + all_reset + " > Power " + bmagenta + "P" + all_reset + " Expand Paddle                                                  " + \
    "                                                                                         " + fred + "|\n" + all_reset + \
    fred + "|" + all_reset + " > Power " + bgreen + "P" + all_reset + " Shrink Paddle                                                  " + \
    "                                                                                         " + fred + "|\n" + all_reset + \
    fred + "|" + all_reset + " > Power " + bred + "P" + all_reset + " Ball Multiplier                                                " + \
    "                                                                                         " + fred + "|\n" + all_reset + \
    fred + "|" + all_reset + " > Power " + byellow + "P" + all_reset + " Fast Ball                                                      " + \
    "                                                                                         " + fred + "|\n" + all_reset + \
    fred + "|" + all_reset + " > Power " + bblue + "P" + all_reset + " Thru-ball                                                      " + \
    "                                                                                         " + fred + "|\n" + all_reset + \
    fred + "|" + all_reset + " > Power " + bcyan + "P" + all_reset + " Paddle Grab                                                    " + \
    "                                                                                         " + fred + "|\n" + all_reset + \
    fred + "*----------------------------------------------------------------------------------------------------------------------" + \
    "---------------------------------------------*\n"+ all_reset