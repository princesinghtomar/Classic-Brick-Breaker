from math import floor
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

    grid_A = (floor(A[0]), floor(A[1]))
    grid_B = (floor(B[0]), floor(B[1]))
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

if __name__ == '__main__':
    print("value 1 :",raytrace( (0,0) , (2,3) ))
    #print("value 2 :",raytrace( (1,1.5) , (5,2.5) ))
    
