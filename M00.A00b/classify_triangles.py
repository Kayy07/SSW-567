import math


def classify_triangle(a, b, c):
    if a == b and a == c:
        return 'equilateral'
    elif a == b:
        if a != c:
            c= c**2
            if a**2 + b**2 == math.trunc(c):
                return 'isosceles and right'
            else:
                return 'isosceles'
    elif a == c:
        b= b**2
        if a**2 + c**2 == math.trunc(b):
            return 'isosceles and right'
        else:
            return 'isosceles'
    else:
        if a**2 + b**2 == c**2:
            return 'scalene and right'
        return 'scalene'
    
#print(classify_triangle(8, 9, 10))