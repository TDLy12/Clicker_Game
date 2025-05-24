import math
import numpy as np

def area_square(length):
    return round(length * length, 3)

def area_rectangle(length, width):
    return round(length * width, 3)

def area_triangle(base, height):
    return round((base * height) / 2, 3)

def area_circle(radius):
    radius = radius * radius
    return round(math.pi * radius, 3)

def linear(a,b,c,d,e,f):
    A = np.array([[a, b], [c, d]])
    print(a,"x + ", b,"y = ", e)
    B = np.array([e,f])
    print(c, "x + ", d, "y = ", f)
    return np.linalg.solve(A, B)