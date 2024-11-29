def area(a, h): 
    '''Function get a side and h tall and return (a*h)/2 
        - area of trinangle'''
    if a < 0 or h < 0: return 0
    return a * h / 2

def perimeter(a, b, c):
    '''Function get a, b, c sides of triangle and return a+b+c
        - perimeter t'''
    if a < 0 or b < 0 or c < 0: return 0
    if a == 0 or b == 0 or c == 0: return 0
    return a + b + c