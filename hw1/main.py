import math

def classify_triangle(a, b, c):
    if (a == b and a == c):
        ret = "equilateral"
    if ((a == b and b != c) or (a == c and b != c) or (c == b and b != a)):
        ret = "isosceles"
    if (a != b and a != c and b != c):
        ret = "scalene"
    if ((a*a + b*b) == c*c):
        ret = ret + " right"
    print(ret)
    return ret

def test():
    assert classify_triangle(3,4,5) == "scalene right"
    assert classify_triangle(4,7,8) == "scalene"
    assert classify_triangle(4,4,5) == "isosceles"
    assert classify_triangle(3,3,3) == "equilateral"
    assert classify_triangle(3,3,4) != "equilateral"

if __name__ == "__main__":
    test()