import numpy as np
from items import *
from headerfile import *

# CHECK THIS PART :-/

def sign(n):
    return (n > 0) - (n < 0)

def raytrace(A, B):
    """ Return all cells of the unit grid crossed by the line segment between
        A and B.
    """
    (xA, yA) = A
    (xB, yB) = B
    (dx, dy) = (xB - xA, yB - yA)
    (sx, sy) = (sign(dx), sign(dy))

    grid_A = ((A[0]), (A[1]))
    grid_B = ((B[0]), (B[1]))
    (x, y) = grid_A
    traversed=[grid_A]

    tIx = dy * (x + sx - xA) if dx != 0 else float("+inf")
    tIy = dx * (y + sy - yA) if dy != 0 else float("+inf")

    while (x,y) != grid_B:
        # NB if tIx == tIy we increment both x and y
        (movx, movy) = (tIx <= tIy, tIy <= tIx)
        
        if movx:
            # intersection is at (x + sx, yA + tIx / dx^2)
            x += sx
            tIx = dy * (x + sx - xA)

        if movy:
            # intersection is at (xA + tIy / dy^2, y + sy)
            y += sy
            tIy = dx * (y + sy - yA)

        traversed.append( (x,y) )
        
    return traversed

class Ball:
    def __init__(self,velocity_x,velocity_y,x,y,screen_array):
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self._x = x
        self._y = y
        if(screen_array[x][y] == ' '):
            screen_array[x][y] = 'O'

    def update_ball_motion(self,screen_array):
        temp_x = self._x + self.velocity_x
        temp_y = self._y + self.velocity_y
        previous_x = self._x
        previous_y = self._y
        size_x = abs(self.velocity_x)
        size_y = abs(self.velocity_y)
        # if went below paddle :
        if(temp_x >= 42):
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
            # else:
                # collision with bricks :

            if(screen_array[temp_x][temp_y] == ' '):
                self._x = temp_x
                self._y = temp_y
            if(point_is):
                screen_array[self._x][self._y] = 'O'
                return 1
            else:
                return -2

    def update_ball_onscreen(self,screen_array):
        if(screen_array[self._x][self._y] == ' '):
            screen_array[self._x][self._y] = 'O'

