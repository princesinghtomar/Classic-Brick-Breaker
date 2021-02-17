''' This file contains color defination and some needed variable 
'''
import numpy as np
# parameters :
GROUND = 1
SKY = 4
HEIGHT = 45
WIDTH = 165
clear_screen = "\033[0;0H"
paddle_size = [5,7,11]
random_paddle_array = [77,78,79,80,81,82,83]
ball_x_starting_constant_velocity = -1
ball_y_starting_constant_velocity = -1

#NOTE Colors 
# Foreground Colors :
fblack = "\033[30m"
fred = "\033[31m"
fgreen = "\033[32m"
fyellow = "\033[33m"
fblue = "\033[34m"
fmagenta = "\033[35m"
fcyan = "\033[36m"
fwhite = "\033[37m"

# Bright Versions :
fbrightblack = "\033[90m"
fbrightred = "\033[91m"
fbrightgreen = "\033[92m"
fbrightyellow = "\033[93m"
fbrightblue = "\033[94m"
fbrightmagenta = "\033[95m"
fbrightcyan = "\033[96m"
fbrightwhite = "\033[97m"

# Background Colors :
bblack = "\033[40m"
bred = "\033[41m"
bgreen = "\033[42m"
byellow = "\033[43m"
bblue = "\033[44m"
bmagenta = "\033[45m"
bcyan = "\033[46m"
bwhite = "\033[47m"

# Bright Versions :
bbrightblack = "\033[100m"
bbrightred = "\033[101m"
bbrightgreen = "\033[102m"
bbrightyellow = "\033[103m"
bbrightblue = "\033[104m"
bbrightmagenta = "\033[105m"
bbrightcyan = "\033[106m"
bbrightwhite = "\033[107m"

# reset :
all_reset = "\033[0m"
back_rest = "\033[49m"
fore_reset = "\033[39m"

# print(bcyan + "bcyan"+ all_reset + bbrightcyan + "bbrightcyan" + all_reset)
bricks_color = np.array([bred,byellow,bcyan,bgreen])
bricks_font_color = np.array([fbrightred,fbrightyellow,fbrightblue,fbrightgreen])
powerup_temper = [bmagenta+"E",bmagenta + "S",bmagenta + "M",bmagenta + "F",bmagenta + "T",bmagenta + "P"]