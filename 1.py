import numpy as np
import math

def sign(n):
    return (n > 0) - (n < 0)

#   *-------
#   | | | | |
#   *-------
#   | | | | |
#   *-------

def s1(coeff,x,y):
    return (y - coeff[0]*x - coeff[1])

def s(coeff,x,y):
    val1 = (s1(coeff,x+1,y)) * (s1(coeff,x,y+1))
    val2 = (s1(coeff,x,y)) * (s1(coeff,x+1,y+1))
    return True if (val1 <= 1e-8 or val2 <= 1e-8 ) else False

def sort_bydist(arr,x,y,flag_check):
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
    # print("a : ",a)
    val = []
    for i in a:
        val.append(i[1])
    return val

def raytrace(A, B):
    ''' Return all cells of the unit grid crossed by the line segment between
        A and B.
    '''
    flag_check = 0
    (xA, yA) = A
    (xB, yB) = B
    # yA += 1
    # xB += 1
    (dx, dy) = (xB - xA, yB - yA)
    coeff = []
    """ Never let vX be 0
    """
    # never make x-velocty as zero
    if(dy/dx < 0):
        flag_check = 1
        if(dy>0):
            yB+=1
            xA+=1
        else:
            yA+=1
            xB+=1
    (dx, dy) = (xB - xA, yB - yA)

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
    sigvar = (sx, sy) = (sign(dx), sign(dy))
    # coeff = np.polyfit([A[0]+1,B[0]],[A[1],B[1]+1],1)
    print("coeff : ",coeff)
    # print("coeff : ",np.polyfit([A[0]+1,B[0]],[A[1],B[1]+1],1))
    grid_start = A
    result = []
    x = xA
    y = yA
    # result.append((x,math.floor (coeff[0]*A[0]+coeff[1])))
    # print("xA yA : ",(xA,yA))
    # print("xB yB : ",(xB,yB))
    j = 0 
    while (x != xB+sx):
        # print("x : ",x)
        y = yA
        while (y != yB+sy):
            # print("y : ",y)
            print("(x,y) : ",(x,y))
            # print("coeff : ",coeff)
            print("s(coeff,x,y) : ",(s(coeff,x,y)))
            if(s(coeff,x,y)):
                result.append((x,y))
            y += sy
            j+=1
        x += sx
    # print("j : ",j)
    result = sort_bydist(result,xA,yA,flag_check)
    return result

x = (19, 88)
y = (20, 90)
print("raytrace : ",raytrace(x,y))



# def raytrace1(A, B):
#     ''' Return all cells of the unit grid crossed by the line segment between
#         A and B.
#     '''
#     (xA, yA) = A
#     (xB, yB) = B
#     (dx, dy) = (xB - xA, yB - yA)
#     (sx, sy) = (sign(dx), sign(dy))
#     # print("A : " + str(A) + "\n")
#     # print("B : " + str(B) + "\n")
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
#         print("(x,y) : ",(x,y))
#         traversed.append( (x,y) )
        
#     return traversed
