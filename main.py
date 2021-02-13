import time
import os
import random
from headerfile import *
from items import *
from keypressed import *
from screen import *
from paddle import *
from gametop import *
from  bricks import *
from ball import *

# random.seed(0)
sys_random = random.SystemRandom()
print(instructions)

# Selecting loop :
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
screen_array = screen_board.return_screenarray()
paddle_array = np.array([80,43,0])
paddle = paddle(paddle_array[0],paddle_array[1],paddle_array[2])
paddle.update_paddle_onscreen(screen_array)
bricks = Bricks()
ball = Ball(ball_x_starting_constant_velocity,ball_y_starting_constant_velocity,42,sys_random.choice(random_paddle_array),screen_array)
bricks.update_brick_onscreen(screen_array)
score = 0
start_time = time.time()
available_time = 1000
livesleft = 3
gametop_data = gametop(available_time,score,livesleft)
gametop_data.update_gametop_onscreen(screen_array)
screen_board.showscreen()
while True:
    key = input_to()
    half_size = (int)(paddle_size[paddle_array[2]]+2)/2
    paddle_start = paddle_array[0] - half_size
    paddle_end = paddle_array[0] + half_size + 1
    print(clear_screen)
    if(key == 'q'):
        #os.system('clear')
        print(art.you_quit_art)
        break
    if(key == 'a'):
        if(paddle_start > 2):
            paddle_array[0] -= 1
            paddle.update_paddle_value(paddle_array[0],paddle_array[1],paddle_array[2])
        
    if(key == 'd'):
        if(paddle_end < WIDTH-2):
            paddle_array[0] += 1
            paddle.update_paddle_value(paddle_array[0],paddle_array[1],paddle_array[2])
    cur_time = time.time()
    available_time -= (cur_time - start_time)
    start_time = cur_time
    if(available_time < 0):
        #os.system('clear')
        print('Time_Over')
        break
    ball_return_value = ball.update_ball_motion(screen_array)
    if(ball_return_value < 0):
        livesleft -= 1
        if(livesleft <= 0):
            print("You loose")
            break
        ball = Ball(-1,-1,42,80,screen_array)
    gametop_data.update_gametop(available_time,score,livesleft)
    gametop_data.update_gametop_onscreen(screen_array)
    paddle.update_paddle_onscreen(screen_array)
    screen_board.showscreen()