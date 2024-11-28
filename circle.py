import math

def area(r):
    '''Function get r radius of circle and return 2 * math.pi(3,14) * r^2
        - area'''
    if r < 0: return 0
    return math.pi * r * r


def perimeter(r):
    '''Function get r radius and return 2 * math.pi(3,14) * r
        - perimeter of circle'''
    if r < 0: return 0
    return 2 * math.pi * r

