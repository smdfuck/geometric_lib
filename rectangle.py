def area(a, b): 
    '''Function get a, b sides of rectangle and return a*b
        - area t'''
    if a < 0 or b < 0: return 0
    return a * b

def perimeter(a, b):
    '''Function get a, b sides and return 2*(a+b)
        - perimeter of rectangle'''
    if a < 0 or b < 0: return 0
    if a == 0 or b == 0: return 0
    return 2 * (a + b)
