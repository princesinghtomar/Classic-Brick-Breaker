import time 
import signal
from colorama import Fore,Back,init,Style
import os
from headerfile import *
# from scenery import *
from items import *
from keypressed import *
from screen import *


print(instructions)

while True:
    pressed_key = input_to()
    if(pressed_key == 'g'):
        break
    elif(pressed_key == 'q'):
        exit()
    else : 
        pass

screen_board = screen(HEIGHT,WIDTH)
screen_board.create_scenery()
# print(screen_board.return_screenarray())
screen_board.showscreen()
while True:
    key = input_to()
    if(key == 'q'):
        print(art.you_quit_art)
        break


