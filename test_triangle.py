import pytest

def classify_triangle(a,b,c):
    sides = [a,b,c]
    sides.sort()

    if a<=0 or b<=0 or c<=0 or sides[0]+sides[1]<=sides[2]:
        return "Invalid Triangle"
    if a==b==c:
        triangle = "Equilateral"
    elif a==b or b==c or a==c:
        triangle = "Isosceles"
    else:
        triangle = "Scalene"
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        triangle += " and Right"
    
    return triangle

def test_classify_triangle():
    assert classify_triangle(3,4,5) == "Scalene and Right"
    assert classify_triangle(1,1,1) == "Equilateral"
    assert classify_triangle(3,3,4) == "Isosceles"
    assert classify_triangle(0,0,0) == "Invalid Triangle"
    assert classify_triangle(1,1,2) == "Invalid Triangle"