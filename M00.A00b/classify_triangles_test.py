import math
import unittest
from classify_triangles import classify_triangle

def test_scalene_triangle_right():
    assert classify_triangle(3, 4, 5) == "scalene and right"

def test_scalene_triangle():
    assert classify_triangle(8, 9, 10) == "scalene"

def test_isosceles_triangle_right():
    hypotenuse = 5 * math.sqrt(2)
    assert classify_triangle(5, 5, hypotenuse) == "isosceles and right"

def test_isosceles_triangle_right_ac():
    hypotenuse = 5 * math.sqrt(2)
    assert classify_triangle(5, hypotenuse, 5) == "isosceles and right"

def test_isosceles_triangle():
    assert classify_triangle(5, 5, 10) == "isosceles"
    assert classify_triangle(5, 10, 5) == "isosceles"

def test_equilateral_triangle():
    assert classify_triangle(5, 5, 5) ==  "equilateral"