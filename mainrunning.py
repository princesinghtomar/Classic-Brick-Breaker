import time
import os
import random
from headerfile import *
from items import *
from keypressed import *
from screen import *
from paddle import *
from gametop import *
from bricks import *
from ball import *

class Run:
    '''
    This is Main Game Class handling all the game flow
    '''
    def __init__(self):
        self.sys_random = random.SystemRandom()
        self.sticky_ball_motion = True
        self.ball_class = None
        self.screen_array = np.array([])
        self.Paddle = None

    def return_paddle_start_and_end(self,paddle_array):
        '''
        This function returns starting  and ending point of paddle
        '''
        half_size = int((paddle_size[paddle_array[2]])/2)
        paddle_start = paddle_array[0] - half_size-1
        paddle_end = paddle_array[0] + half_size+1
        return (half_size,paddle_start,paddle_end)

    def move(self,paddle_array):
        '''
        This function is responsible for detecting user input and responding accordingly
        '''
        key = input_to()
        (half_size,paddle_start,paddle_end) = self.return_paddle_start_and_end(paddle_array)
        print(clear_screen)
        if(key == 'q'):
            #os.system('clear')
            print(art.you_quit_art)
            return 0
        elif(key == 'a'):
            if(paddle_start > 4):
                paddle_array[0] -= 3
                if(self.sticky_ball_motion):
                    self.ball_class.ball_sticky_motion(self.screen_array,0,-3)
                self.Paddle.update_paddle_value(paddle_array[0],paddle_array[1],paddle_array[2])
        elif(key == 'd'):
            if(paddle_end < WIDTH-3):
                paddle_array[0] += 3
                if(self.sticky_ball_motion):
                    self.ball_class.ball_sticky_motion(self.screen_array,0,+3)
                self.Paddle.update_paddle_value(paddle_array[0],paddle_array[1],paddle_array[2])
        elif(key == 'k'):
            self.sticky_ball_motion = False
        return 1

    def starting_instruction(self):
        '''
        This function just gives instructions to the user
        '''
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
        os.system('clear')

    def Go(self):
        '''
        This function has the main control flow of the game
        '''
        self.starting_instruction()
        screen_board = screen(HEIGHT,WIDTH)
        screen_board.create_scenery()
        self.screen_array = screen_board.return_screenarray()
        paddle_array = np.array([80,43,0])
        self.Paddle = paddle(paddle_array[0],paddle_array[1],paddle_array[2])
        self.Paddle.update_paddle_onscreen(self.screen_array)
        bricks = Bricks()
        (half_size,paddle_start,paddle_end) = self.return_paddle_start_and_end(paddle_array)
        temp_random = self.sys_random.choice([i for i in range(paddle_start,paddle_end)])
        self.ball_class = Ball(ball_x_starting_constant_velocity,ball_y_starting_constant_velocity,42,temp_random,self.screen_array)
        bricks.update_brick_onscreen(self.screen_array)
        score = 0
        choosen_value = 0
        start_time = time.time()
        available_time = 1000
        livesleft = 3
        gametop_data = gametop(available_time,score,livesleft)
        gametop_data.update_gametop_onscreen(self.screen_array)
        screen_board.showscreen()
        tic_toc = time.time()
        while True:
            toc = time.time()
            frames = toc - tic_toc
            if(frames >= 0.11):
                tic_toc = toc
                move_return = self.move(paddle_array)
                if(not move_return):
                    break
                cur_time = time.time()
                available_time -= (cur_time - start_time)
                start_time = cur_time
                if(available_time < 0):
                    #os.system('clear')
                    print('Time_Over')
                    break
                
                if(not self.sticky_ball_motion):
                    (half_size,paddle_start,paddle_end) = self.return_paddle_start_and_end(paddle_array)
                    (ball_return_value,score_,choosen_value) = self.ball_class.update_ball_motion(self.screen_array,bricks,paddle_start,paddle_end)
                    score+=score_
                    score_ = 0
                    if(ball_return_value < 0):
                        livesleft -= 1
                        print("livesleft : ",livesleft)
                        if(livesleft <= 0):
                            print("You loose")
                            break
                        temp_random = self.sys_random.choice([i for i in range(paddle_start,paddle_end)])
                        self.ball_class = Ball(ball_x_starting_constant_velocity,ball_y_starting_constant_velocity,42,temp_random,self.screen_array)
                        self.sticky_ball_motion = True
                gametop_data.update_gametop(available_time,score,livesleft)
                gametop_data.update_gametop_onscreen(self.screen_array)
                self.Paddle.update_paddle_onscreen(self.screen_array)
                screen_board.showscreen()