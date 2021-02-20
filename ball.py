import numpy as np
from items import *
from headerfile import *
from bricks import *
import math
import sys

# CHECK THIS PART :-/

#   *--------
#   | | | | |
#   *--------
#   | | | | |
#   *--------

class functionality_class:
    '''
    This class handles mathematical part of brick-ball collision
    and is inherited by the Ball class
    '''
    def __init__(self):
        self.flag = False

    def sign(self,n):
        '''
        Return sign of n
        '''
        return -1 if n < 0 else +1

    def s1(self,coeff,x,y):
        '''
        Return the sign of point with line
        '''
        return (y - coeff[0]*x - coeff[1])

    def s(self,coeff,x,y):
        '''
        Returns whether point lies between line or not
        '''
        val1 = (self.s1(coeff,x+1,y)) * (self.s1(coeff,x,y+1))
        val2 = (self.s1(coeff,x,y)) * (self.s1(coeff,x+1,y+1))
        return True if (val1 <= 1e-8 or val2 <= 1e-8 ) else False

    def sort_bydist(self,arr,x,y,flag_check):
        '''
        Returns sorted list accr to their distance by starting point
        '''
        a = []
        size = len(arr)
        j=0
        for i in arr:
            if(flag_check):
                if(j!=0 and j!=(size-1)):
                    dist = math.sqrt(math.pow(i[0]-x,2) + math.pow(i[1]-y,2))
                    a.append((dist,(i[0],i[1])))
            else:
                dist = math.sqrt(math.pow(i[0]-x,2) + math.pow(i[1]-y,2))
                a.append((dist,(i[0],i[1])))
            j+=1
        a.sort()
        val = []
        for i in a:
            val.append(i[1])
        return val

    def raytrace(self,A, B):
        ''' 
        Return all cells of the unit grid crossed by the line segment between
        A and B.
        '''
        # print(str(A) + " :A , B: " + str(B))
        flag_check = 0
        (xA, yA) = A
        (xB, yB) = B
        (dx, dy) = (xB - xA, yB - yA)
        coeff = []
        '''
        Never let vX be 0
        '''
        if(dy/dx < 0):
            flag_check = 1
            if(dy>0):
                yB+=1
                xA+=1
            else:
                yA+=1
                xB+=1
        (dx, dy) = (xB - xA, yB - yA)
        # print("(dx, dy) : " + str((dx, dy)))
        #
        #   If slope = -ve 
        #       then do (xA+1,yB) & (xB,yB+1)
        #   elif slope = +ve
        #       then do nothing
        #   elif slope == 0
        #       then do nothing
        #
        coeff.append(dy/dx)
        coeff.append(yA-coeff[0]*xA)
        sigvar = (sx, sy) = (self.sign(dx), self.sign(dy))
        grid_start = A
        result = []
        x = xA
        y = yA
        j = 0 
        while (x != xB+sx):
            y = yA
            while (y != yB+sy):
                if(self.s(coeff,x,y)):
                    result.append((x,y))
                y += sy
                j+=1
            x += sx
        result = self.sort_bydist(result,xA,yA,flag_check)
        return result


class Ball(functionality_class):
    ''' 
    This class contains all ball functions
    '''
    def __init__(self,velocity_x,velocity_y,x,y,screen_array):
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.ball_x = x
        self.bal_y = y
        self.thru_ball = False
        self.sticky_ball = False

        if(screen_array[x][y] == ' '):
            screen_array[x][y] = 'O'

    def return_class_init(self):
        return (self.velocity_x,self.velocity_y,self.ball_x,self.bal_y)

    def update_speed(self,vx,vy):
        self.velocity_y = vx
        self.velocity_x = vy

    def update_xandy(self,x,y):
        self.ball_x = x
        self.bal_y = y

    def update_thru_ball(self,value):
        self.thru_ball = value

    def increase_speed(self,dvx,dvy):
        self.velocity_x *= abs(dvx)
        self.velocity_y *= abs(dvy)

    def ball_sticky_motion(self,screen_array,dx,dy):
        screen_array[self.ball_x][self.bal_y] = ' '    
        self.ball_x += dx
        self.bal_y += dy
        screen_array[self.ball_x][self.bal_y] = 'O'

    def update_ball_motion(self,screen_array,bricks_class,paddle_start,paddle_end):
        ''' 
        This functions handle collision of ball with bricks
        '''
        temp_x = self.ball_x + self.velocity_x
        temp_y = self.bal_y + self.velocity_y
        previous_x = self.ball_x
        previous_y = self.bal_y
        size_x = abs(self.velocity_x)
        size_y = abs(self.velocity_y)
        score_= 0
        choosen_value = 0
        #
        # if went below paddle :
        #
        if(temp_x >= 43):
            if(( temp_x == 43 or self.ball_x <= 43 )):
                paddle_center = (paddle_start + paddle_end)/2
                if(temp_y >= paddle_start and temp_y <= paddle_end):
                    if(temp_y > paddle_center):
                        self.velocity_y += math.ceil(abs(temp_y - paddle_center))
                    else:
                        self.velocity_y -= math.ceil(abs(temp_y - paddle_center))
                    temp_x = previous_x
                    temp_y = previous_y
                    self.velocity_x = -self.velocity_x
                    return (1,score_,choosen_value)
                else:
                    screen_array[previous_x][previous_y] = ' '
                    return (-2,score_,choosen_value)
            else:
                screen_array[previous_x][previous_y] = ' '
                return (-2,score_,choosen_value)
        else:
            size = bricks.size
            array = [bricks_color[i]+bricks_font_color[i]+bricks[i][1]+all_reset for i in range(0,size)]
            screen_array[previous_x][previous_y] = ' '
            point_is = 1
            #
            # if collision with walls :
            #
            if(temp_x <= 5):
                self.velocity_x = -self.velocity_x
                temp_val = 5 - temp_x
                temp_x = 5 + temp_val
                if(temp_y <= 2):
                    self.velocity_y = -self.velocity_y
                    temp_val = 2 - temp_y
                    temp_y = 2 + temp_val
                elif(temp_y >= WIDTH-2):
                    self.velocity_y = -self.velocity_y
                    temp_val = (WIDTH - 2) - temp_y
                    temp_y = (WIDTH - 2) + temp_val
                self.ball_x = temp_x
                self.bal_y = temp_y
            elif(temp_y <=2 ):
                self.velocity_y = -self.velocity_y
                temp_val = 2 - temp_y
                temp_y = 2 + temp_val
            elif(temp_y >= (WIDTH-2)):
                self.velocity_y = -self.velocity_y
                temp_val = (WIDTH - 2) - temp_y
                temp_y = (WIDTH - 2) + temp_val
            else:
                sign_vx = self.sign(self.velocity_x)
                sign_vy = self.sign(self.velocity_y)
                ball_temp = self.raytrace((self.ball_x,self.bal_y),(temp_x,temp_y))
                cur_x = self.ball_x
                cur_y = self.bal_y
                if(not self.thru_ball):
                    #
                    # collision with bricks :
                    #
                    second_flag = 1
                    i =0
                    #
                    # while second_flag:
                    #
                    for i in range(1,len(ball_temp)):
                        if(screen_array[ball_temp[i][0]][ball_temp[i][1]]!=' '):
                            if((cur_x+1,cur_y+1)==(ball_temp[i][0],ball_temp[i][1]) or 
                                (cur_x-1,cur_y-1)==(ball_temp[i][0],ball_temp[i][1]) or 
                                (cur_x-1,cur_y+1)==(ball_temp[i][0],ball_temp[i][1]) or 
                                (cur_x+1,cur_y-1)==(ball_temp[i][0],ball_temp[i][1])):
                                self.velocity_x = -self.velocity_x
                                self.velocity_y = -self.velocity_y
                            elif((cur_x,cur_y+1)==(ball_temp[i][0],ball_temp[i][1]) or 
                                (cur_x,cur_y-1)==(ball_temp[i][0],ball_temp[i][1])):
                                self.velocity_y = -self.velocity_y
                            elif((cur_x+1,cur_y)==(ball_temp[i][0],ball_temp[i][1]) or
                                (cur_x-1,cur_y)==(ball_temp[i][0],ball_temp[i][1])):
                                self.velocity_x = -self.velocity_x
                            (score_,choosen_value) = bricks_class.remove_brick_onscreen(screen_array,ball_temp[i][0],ball_temp[i][1],False)
                            temp_x = cur_x
                            temp_y = cur_y
                            break
                        else:
                            cur_x = ball_temp[i][0]
                            cur_y = ball_temp[i][1]
                else:
                    for i in range(1,len(ball_temp)):
                        if(screen_array[ball_temp[i][0]][ball_temp[i][1]]!= 'O' or
                            screen_array[ball_temp[i][0]][ball_temp[i][1]]!= '-' or 
                            screen_array[ball_temp[i][0]][ball_temp[i][1]] != '|' or 
                            screen_array[ball_temp[i][0]][ball_temp[i][1]] != '*' or 
                            screen_array[ball_temp[i][0]][ball_temp[i][1]] != '=' or 
                            screen_array[ball_temp[i][0]][ball_temp[i][1]] != '>' or 
                            screen_array[ball_temp[i][0]][ball_temp[i][1]] != '<'):
                            if(screen_array[ball_temp[i][0]][ball_temp[i][1]]!=' '):
                                (score_,choosen_value) = bricks_class.remove_brick_onscreen(screen_array,ball_temp[i][0],ball_temp[i][1],True)

            if(screen_array[temp_x][temp_y] == ' ' and not self.thru_ball):
                self.ball_x = temp_x
                self.bal_y = temp_y
                screen_array[self.ball_x][self.bal_y] = 'O'
                return (1,score_,choosen_value)
            elif(self.thru_ball):
                self.ball_x = temp_x
                self.bal_y = temp_y
                screen_array[self.ball_x][self.bal_y] = 'O'
                return (1,score_,choosen_value)
