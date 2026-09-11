def classify_triangle(a, b, c):
    if a == b and a == c:
        return 'equilateral'
    elif a == b:
        if a != c:
            if a**2 + b**2 == c**2:
                return 'isosceles and right'
            else:
                return 'isosceles'
    elif a == c:
        if a**2 + b**2 == c**2:
            return 'isosceles and right'
        else:
            return 'isosceles'
    else:
        if a**2 + b**2 == c**2:
            return 'scalene and right'
        return 'scalene'
    
#print(classify_triangle(8, 9, 10))