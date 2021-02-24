import time
import os
import random
import logging
from headerfile import *
from items import *
from keypressed import *
from screen import *
from paddle import *
from gametop import *
from bricks import *
from ball import *
from powerup import *

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s',level=logging.DEBUG)
logging.debug('This will get logged to a file')

class Run:
    '''
    This is Main Game Class handling all the game flow
    '''
    def __init__(self):
        self.sys_random = random.SystemRandom()
        self.sticky_ball_motion = True
        self.sticky_ball_powerup = False
        self.ball_class = []
        self.screen_array = np.array([])
        self.Paddle = None
        self.paddle_array = np.array([])
        self.powerup_flag = [0,0,0,0,0,0]
        # self.ball_index = []

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
            os.system('clear')
            # ----
            print(art.you_quit_art)
            return 0
        elif(key == 'a'):
            if(paddle_start > 4):
                self.paddle_array[0] -= 3
                if(self.sticky_ball_motion):
                    self.ball_class[0].ball_sticky_motion(self.screen_array,0,-3)
                self.Paddle.update_paddle_value(self.paddle_array[0],self.paddle_array[1],self.paddle_array[2])
        elif(key == 'd'):
            if(paddle_end < WIDTH-3):
                self.paddle_array[0] += 3
                if(self.sticky_ball_motion):
                    self.ball_class[0].ball_sticky_motion(self.screen_array,0,+3)
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
        self.ball_class.append(Ball(ball_x_starting_constant_velocity,ball_y_starting_constant_velocity,42,temp_random,self.screen_array))
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
        powerups.append(power0(0,0))
        powerups.append(power1(0,0))
        powerups.append(power2(0,0))
        powerups.append(power3(0,0))
        powerups.append(power4(0,0))
        powerups.append(power5(0,0))
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
                    os.system('clear')
                    # --------
                    print(fmagenta + art.game_over + all_reset)
                    break
                
                if(not self.sticky_ball_motion):
                    (half_size,paddle_start,paddle_end) = self.return_paddle_start_and_end()
                    some_temp_val= self.ball_class[0].update_ball_motion(self.screen_array,bricks,paddle_start,paddle_end)
                    if(some_temp_val is None):
                        (bavx,bavy,bax,bay) = self.ball_class[0].return_class_init()
                        self.ball_class[0].update_speed(-bavx,bavy)
                        val_zero = (0,0,0)
                        # print("(bavx,bavy,bax,bay) : " + str((bavx,bavy,bax,bay)))
                        logging.debug("(bavx,bavy,bax,bay) : " + str((bavx,bavy,bax,bay)))
                        bricks.remove_brick_onscreen(self.screen_array,bax-1,bay,powerups[4].check_time())
                        (ball_return_value,score_,choosen_value)  = val_zero
                    else:
                        (ball_return_value,score_,choosen_value) = some_temp_val
                    if(len(self.ball_class) > 1):
                        for i in range(1,len(self.ball_class)):
                            some_temp_val_2 = self.ball_class[i].update_ball_motion(self.screen_array,bricks,paddle_start,paddle_end)
                    # --------  choosen_value 
                    logging.debug("choosen_value : " + str(choosen_value))
                    if(choosen_value!=0):
                        # ---------
                        logging.debug("choosen_value!=0 : " + str(choosen_value!=0))
                        if(self.powerup_flag[choosen_value-1] == 1):
                            logging.debug("self.powerup_flag[choosen_value-1] :" + str(self.powerup_flag[choosen_value-1]))
                            # powerups[choosen_value-1].update_time_activated()
                        else:
                            self.powerup_flag[choosen_value-1] = 1
                        # -------  self.powerup_flag - 
                        logging.debug("self.powerup_flag : " + str(self.powerup_flag))
                    score+=score_
                    score_ = 0
                    if(ball_return_value < 0):
                        livesleft -= 1
                        if(livesleft <= 0):
                            os.system('clear')
                            print(fred + art.you_loose + all_reset)
                            break
                        temp_random = self.sys_random.choice([i for i in range(paddle_start,paddle_end)])
                        self.ball_class[0] = Ball(ball_x_starting_constant_velocity,ball_y_starting_constant_velocity,42,temp_random,self.screen_array)
                        for i in range(0,6):
                            if(self.powerup_flag[i] == 1): 
                                powerups[i].update_status(0)
                                powerups[i].deactivate_time()
                                self.powerup_flag[i] = 0
                                if(i == 0 or i ==1):
                                    # -------- ( i == 0 or 1 )
                                    logging.debug("Here at i == 0 & i == 1  -- undo part")
                                    powerups[i].undo(self.Paddle)
                                elif(i == 2):
                                    powerups[i].undo(self.ball_class,self.screen_array)
                                elif(i == 3 or i == 4):
                                    # -------- ( i == 3 or 4 )
                                    logging.debug("Here at i == 0 & i == 1  -- undo part")
                                    powerups[i].undo(self.ball_class[0])
                                elif(i==5):
                                    # -------- ( i == 5 )
                                    logging.debug("Here at i == 5 -- undo part")
                                    self.sticky_ball_powerup = powerups[i].undo()
                        self.sticky_ball_motion = True
                for i in range(0,6):
                    # ------- self.powerup_flag[i]
                    logging.debug("self.powerup_flag[i] : " + str(self.powerup_flag[i]))
                    if(self.powerup_flag[i]):
                        # ---------  powerups[i].return_status() -
                        logging.debug("powerups[i].return_status() : " + str(powerups[i].return_status()))
                        if(powerups[i].return_status() == 0):
                            (bavx,bavy,bax,bay) = self.ball_class[0].return_class_init()
                            # -------- (bavx,bavy,bax,bay) -
                            logging.debug("(bavx,bavy,bax,bay) : " + str((bavx,bavy,bax,bay)))
                            powerups[i].update_xy(bax,bay)
                            powerups[i].make_powerup_active()
                        elif(powerups[i].return_status() == 1):
                            (half_size,paddle_start,paddle_end) = self.return_paddle_start_and_end()
                            # ---------  (half_size,paddle_start,paddle_end)
                            logging.debug("(half_size,paddle_start,paddle_end) : " + str((half_size,paddle_start,paddle_end)))
                            ret_value = powerups[i].update_powerup_onscreen(self.screen_array,paddle_end,paddle_start,self.Paddle)
                            # --------- ret _value 
                            logging.debug("ret_value : " + str(ret_value))
                            if(ret_value == True):
                                if(i == 0 or i == 1):
                                    # -------- ( i == 0 or 1 )
                                    logging.debug("Here at i == 0 & i == 1  -- do part")
                                    powerups[i].do(self.Paddle)
                                elif(i == 2):
                                    # -------- ( i == 2)
                                    logging.debug("Here at i == 2  -- do part")
                                    powerups[i].do(self.ball_class,self.screen_array)
                                elif(i == 3 or i ==4):
                                    # -------- ( i == 3 or 4 )
                                    logging.debug("Here at i == 0 & i == 1  -- do part")
                                    powerups[i].do(self.ball_class[0])
                                elif(i==5):
                                    # -------- ( i == 5 )
                                    logging.debug("Here at i == 5 -- do part")
                                    self.sticky_ball_powerup = powerups[i].do()
                            if(powerups[i].return_status() == 0):
                                self.powerup_flag[i]=0
                        elif(powerups[i].return_status() == 2):
                            # -------- powerups[i].return_status() == 2
                            logging.debug("powerups[i].return_status() == 2 " + str(powerups[i].return_status() == 2))
                            if(i == 0 or i ==1):
                                # --------- ( i == 0 or i ==1 )
                                logging.debug("Here at i == 0 & i == 1  -- do part")
                                powerups[i].do(self.Paddle)
                            if(not powerups[i].check_time()):
                                self.powerup_flag[i] = 0
                                powerups[i].update_status(0)
                                powerups[i].deactivate_time()
                                if(i == 0 or i ==1):
                                    # -------- ( i == 0 or 1 )
                                    logging.debug("Here at i == 0 & i == 1  -- undo part")
                                    powerups[i].undo(self.Paddle)
                                elif(i == 2):
                                    # -------- ( i == 2)
                                    logging.debug("Here at i == 2  -- undo part")
                                    powerups[i].undo(self.ball_class,self.screen_array)
                                elif(i == 3 or i == 4):
                                    # -------- ( i == 0 or 1 )
                                    logging.debug("Here at i == 0 & i == 1  -- undo part")
                                    powerups[i].undo(self.ball_class[0])
                                    powerups[i].update_status(0)
                                elif(i==5):
                                    # -------- ( i == 5 )
                                    logging.debug("Here at i == 5 -- undo part")
                                    self.sticky_ball_powerup = powerups[i].undo()
                                    powerups[i].update_status(0)

                gametop_data.update_gametop(available_time,score,livesleft)
                gametop_data.update_gametop_onscreen(self.screen_array)
                self.Paddle.update_paddle_onscreen(self.screen_array)
                screen_board.showscreen()
                
                if(self.sticky_ball_powerup):
                    (bavx,bavy,bax,bay) = self.ball_class[0].return_class_init()
                    (half_size,paddle_start,paddle_end) = self.return_paddle_start_and_end()
                    if(bax >= 42):
                        if(bay>=paddle_start and bay <= paddle_end):
                            self.sticky_ball_motion = True
