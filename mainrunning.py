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
from powerup import *

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
        self.paddle_array = np.array([])
        self.powerup_flag = [0,0,0,0,0,0]
        # self.expand_paddle_powerup = None
        # self.expand_paddle_powerup_bool = False

    def return_paddle_start_and_end(self):
        '''
        This function returns starting  and ending point of paddle
        '''
        half_size = int((paddle_size[self.paddle_array[2]])/2)
        paddle_start = self.paddle_array[0] - half_size-1
        paddle_end = self.paddle_array[0] + half_size+1
        return (half_size,paddle_start,paddle_end)

    def move(self):
        '''
        This function is responsible for detecting user input and responding accordingly
        '''
        key = input_to()
        (half_size,paddle_start,paddle_end) = self.return_paddle_start_and_end()
        print(clear_screen)
        if(key == 'q'):
            #os.system('clear')
            print(art.you_quit_art)
            return 0
        elif(key == 'a'):
            if(paddle_start > 4):
                self.paddle_array[0] -= 3
                if(self.sticky_ball_motion):
                    self.ball_class.ball_sticky_motion(self.screen_array,0,-3)
                self.Paddle.update_paddle_value(self.paddle_array[0],self.paddle_array[1],self.paddle_array[2])
        elif(key == 'd'):
            if(paddle_end < WIDTH-3):
                self.paddle_array[0] += 3
                if(self.sticky_ball_motion):
                    self.ball_class.ball_sticky_motion(self.screen_array,0,+3)
                self.Paddle.update_paddle_value(self.paddle_array[0],self.paddle_array[1],self.paddle_array[2])
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

    # def expand_paddle_function(self):
    #     # print("hel;lo")
    #     (vx,vy,x,y) = self.ball_class.return_class_init()
    #     if(not self.expand_paddle_powerup_bool):
    #         self.expand_paddle_powerup = expand_paddle(time.time(),x,y)
    #     self.expand_paddle_powerup_bool = True
    #     (half_size,paddle_start,paddle_end) = self.return_paddle_start_and_end()
    #     self.expand_paddle_powerup.make_powerup_active()
    #     self.expand_paddle_powerup.update_powerup_onscreen(self.screen_array,paddle_end,paddle_start,self.Paddle)

    # def powerup_flow(self,choosen_value):
    #     if(choosen_value == 1):
    #         # expand paddle
    #         self.expand_paddle_function()
    #     # elif(choosen_value == 2):
    #         # shrick paddle

    # def powerup_flag(self.choosen_value):

    def Go(self):
        '''
        This function has the main control flow of the game
        '''
        self.starting_instruction()
        screen_board = screen(HEIGHT,WIDTH)
        screen_board.create_scenery()
        self.screen_array = screen_board.return_screenarray()
        self.paddle_array = np.array([80,43,1])
        self.Paddle = paddle(self.paddle_array[0],self.paddle_array[1],self.paddle_array[2])
        self.Paddle.update_paddle_onscreen(self.screen_array)
        bricks = Bricks()
        (half_size,paddle_start,paddle_end) = self.return_paddle_start_and_end()
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
        power_up_x = 0
        power_up_y = 0
        powerups = []
        # powerups.append(power)
        while True:
            toc = time.time()
            frames = toc - tic_toc
            if(frames >= 0.11):
                tic_toc = toc
                move_return = self.move()
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
                    (half_size,paddle_start,paddle_end) = self.return_paddle_start_and_end()
                    (ball_return_value,score_,choosen_value) = self.ball_class.update_ball_motion(self.screen_array,bricks,paddle_start,paddle_end)
                    # self.powerup_flow(choosen_value)
                    if(choosen_value):
                        self.powerup_flag[choosen_value] = 1
                        print(self.powerup_flag)
                    score+=score_
                    # print(1)
                    score_ = 0
                    if(ball_return_value < 0):
                        livesleft -= 1
                        # print("livesleft : ",livesleft)
                        if(livesleft <= 0):
                            print("You loose")
                            break
                        temp_random = self.sys_random.choice([i for i in range(paddle_start,paddle_end)])
                        self.ball_class = Ball(ball_x_starting_constant_velocity,ball_y_starting_constant_velocity,42,temp_random,self.screen_array)
                        self.sticky_ball_motion = True
                # for i in range(0,6):
                #     if(self.powerup_flag[i]):

                # if(self.expand_paddle_powerup_bool):
                #     (half_size,paddle_start,paddle_end) = self.return_paddle_start_and_end()
                #     self.expand_paddle_powerup.update_powerup_onscreen(self.screen_array,paddle_end,paddle_start,self.Paddle)
                gametop_data.update_gametop(available_time,score,livesleft)
                gametop_data.update_gametop_onscreen(self.screen_array)
                self.Paddle.update_paddle_onscreen(self.screen_array)
                screen_board.showscreen()