import numpy as np
from items import *
from headerfile import *
from bricks import *
from math import floor

# CHECK THIS PART :-/

def sign(n):
    """ Return value: Sign of input value
    """
    return (n > 0) - (n < 0)

# def raytrace(A, B):
#     """ Return all cells of the unit grid crossed by the line segment between
#         A and B.
#     """
#     (xA, yA) = A
#     (xB, yB) = B
#     (dx, dy) = (xB - xA, yB - yA)
#     (sx, sy) = (sign(dx), sign(dy))

#     grid_A = ((A[0]), (A[1]))
#     grid_B = ((B[0]), (B[1]))
#     (x, y) = grid_A
#     traversed=[grid_A]

#     tIx = dy * (x + sx - xA) if dx != 0 else float("+inf")
#     tIy = dx * (y + sy - yA) if dy != 0 else float("+inf")

#     while (x,y) != grid_B:
#         # NB if tIx == tIy we increment both x and y
#         (movx, movy) = (tIx <= tIy, tIy <= tIx)
        
#         if movx:
#             # intersection is at (x + sx, yA + tIx / dx^2)
#             x += sx
#             tIx = dy * (x + sx - xA)

#         if movy:
#             # intersection is at (xA + tIy / dy^2, y + sy)
#             y += sy
#             tIy = dx * (y + sy - yA)

#         traversed.append( (x,y) )
        
#     return traversed

class Ball:
    """ This class contains all ball functions
    """
    def __init__(self,velocity_x,velocity_y,x,y,screen_array):
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self._x = x
        self._y = y
        if(screen_array[x][y] == ' '):
            screen_array[x][y] = 'O'

    def for_velocity_one(self,screen_array,temp_x,temp_y,bricks_class):
        """ This function constains final position if velocity given is 1
        """
        sign_vx = sign(self.velocity_x)
        sign_vy = sign(self.velocity_y)
        previous_x = self._x
        previous_y = self._y
        if(screen_array[temp_x-sign_vx][temp_y]!=' ' and screen_array[temp_x][temp_y-sign_vy]!=' '):
            self.velocity_y = -self.velocity_y
            self.velocity_x = -self.velocity_x
            bricks_class.remove_brick_onscreen(screen_array,temp_x-sign_vx,temp_y)
            bricks_class.remove_brick_onscreen(screen_array,temp_x,temp_y-sign_vy)
            temp_x = previous_x
            temp_y = previous_y
        elif(screen_array[temp_x-sign_vx][temp_y] != ' '):
            bricks_class.remove_brick_onscreen(screen_array,temp_x-sign_vx,temp_y)
            self.velocity_y = -self.velocity_y
            temp_x = temp_x - sign_vx
        elif(screen_array[temp_x][temp_y-sign_vy] != ' '):
            bricks_class.remove_brick_onscreen(screen_array,temp_x,temp_y-sign_vy)
            self.velocity_x = -self.velocity_x
            temp_y = temp_y - sign_vy
        elif(screen_array[temp_x][temp_y]!=' '):
            bricks_class.remove_brick_onscreen(screen_array,temp_x,temp_y)
            self.velocity_x = -self.velocity_x
            self.velocity_y = -self.velocity_y
        return (temp_x,temp_y)

    def update_ball_motion(self,screen_array,bricks_class,paddle_start,paddle_end):
        """ This functions handle collision of ball with bricks
        """
        temp_x = self._x + self.velocity_x
        temp_y = self._y + self.velocity_y
        previous_x = self._x
        previous_y = self._y
        size_x = abs(self.velocity_x)
        size_y = abs(self.velocity_y)
        # if went below paddle :
        if(temp_x >= 43):
            if(temp_x == 43):
                if(temp_y >= paddle_start and temp_y <= paddle_end):
                    sizepaddle = paddle_end - paddle_start
                    bythree = floor(sizepaddle/3)
                    arr = [paddle_start+bythree,paddle_end-bythree]
                    # speed change
                    # if(temp_y<arr[0]):
                    #     self.velocity_y -= 1
                    # elif(temp_y>arr[1]):
                    #     self.velocity_y += 1
                    temp_x = previous_x
                    temp_y = previous_y
                    self.velocity_x = -self.velocity_x
                    return 1
                else:
                    screen_array[previous_x][previous_y] = ' '
                    return -2
            else:
                screen_array[previous_x][previous_y] = ' '
                return -2
        else:
            size = bricks.size
            array = [bricks_color[i]+bricks_font_color[i]+bricks[i][1]+all_reset for i in range(0,size)]
            screen_array[previous_x][previous_y] = ' '
            point_is = 1
            # if collision with walls :
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
                self._x = temp_x
                self._y = temp_y
            elif(temp_y <=2 ):
                self.velocity_y = -self.velocity_y
                temp_val = 2 - temp_y
                temp_y = 2 + temp_val
            elif(temp_y >= (WIDTH-2)):
                self.velocity_y = -self.velocity_y
                temp_val = (WIDTH - 2) - temp_y
                temp_y = (WIDTH - 2) + temp_val
            else:
                # collision with bricks :
                sign_vx = sign(self.velocity_x)
                sign_vy = sign(self.velocity_y)
                if(abs(self.velocity_x)==0):
                    if(screen_array[temp_x][temp_y] != ' ' ):
                        self.velocity_y = -self.velocity_y
                        bricks_class.remove_brick_onscreen(screen_array,temp_x,temp_y)
                        temp_y = previous_y
                elif(abs(self.velocity_x)==1):
                    val = self.for_velocity_one(screen_array,temp_x,temp_y,bricks_class)
                    temp_x = val[0]
                    temp_y = val[1]
                elif(abs(self.velocity_x)==2):
                    if(screen_array[self._x][self._y+sign_vy]!= ' '):
                        self.velocity_y = -self.velocity_y
                        temp_y = temp_y - 2*sign_vy
                        val = self.for_velocity_one(screen_array,temp_x,temp_y,bricks_class)
                        temp_x = val[0]
                        temp_y = val[1]
                    elif(screen_array[self._x+sign_vx][temp_y]!= ' '):
                        self.velocity_x = -self.velocity_x
                        temp_x = temp_x - sign_vx
                        if(screen_array[temp_x][temp_y]!=' '):
                            temp_y = self._y + sign_vy
                    elif(screen_array[temp_x][temp_y]!=' '):
                        self.velocity_y = -self.velocity_y
                        temp_y = temp_y-sign_vy

            if(screen_array[temp_x][temp_y] == ' '):
                self._x = temp_x
                self._y = temp_y
            if(point_is):
                screen_array[self._x][self._y] = 'O'
                return 1
            else:
                return -2

    def update_ball_onscreen(self,screen_array):
        """ This function updates ball on screen :)
        """
        if(screen_array[self._x][self._y] == ' '):
            screen_array[self._x][self._y] = 'O'

