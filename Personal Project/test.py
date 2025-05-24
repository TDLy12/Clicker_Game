import SimpleAreas
import numpy as np

stop = False

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

while stop == False:
    print("What kind of questions would you like to solve?")
    Type = int(input("1. Shapes, 2. Solve for X and Y (2 equations) 3.Stop"))

    count = 0
    fine = True


    if Type == 1:
        questions = input()

        if questions.find("area") != -1:
            if questions.find("square") != -1:
                x = float(input("enter the length"))
                result = SimpleAreas.area_square(x)
                print(result)

            if questions.find("rectangle") != -1:
                x = float(input("enter length 1"))
                y = float(input("enter length 2"))
                result = SimpleAreas.area_rectangle(x, y)
                print(result)


            if questions.find("triangle") != -1:
                x = float(input("enter length"))
                y = float(input("enter height"))
                result = SimpleAreas.area_triangle(x, y)
                print(result)


            if questions.find("circle") != -1:
                x = float(input("enter radius"))
                result = SimpleAreas.area_circle(x)
                print(result)

    elif Type == 2:
        a = float(input("Enter the value of the first x coefficient"))
        b = float(input("Enter the value of the first y coefficient"))
        c = float(input("Enter the value of the second x coefficient"))
        d = float(input("Enter the value of the second y coefficient"))
        e = float(input("Enter the value of the result of the first equation"))
        f = float(input("Enter the value of the result of the second equation"))
        print(SimpleAreas.linear(a, b, c, d, e, f))

    elif Type == 3:
        stop = True






