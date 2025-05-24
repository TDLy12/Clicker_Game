import SimpleAreas

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

print("What kind of questions would you like to solve?")
Type = int(input("1. Shapes, 2. Solve for X"))

count = 0
fine = True

if Type == 1:
    questions = input("Which shape and what features?")

    if questions.find("area") != 0:
        if questions.find("square") != 0:
            x = int(input("enter the length"))
            result = SimpleAreas.area_square(x)
            print(result)

        if questions.find("rectangle") != 0:
            x = int(input("enter the length"))
            y = int(input("enter the height"))
            result = SimpleAreas.area_rectangle(x, y)
            print(result)

        if questions.find("triangle") != 0:
            x = int(input("enter the length"))
            y = int(input("enter the height"))
            result = SimpleAreas.area_triangle(x, y)
            print(result)

        if questions.find("circle") != 0:
            x = int(input("enter the radius"))
            result = SimpleAreas.area_circle(int(x))
            print(result)


def solve_linear(equation,var='x'):
    expression = equation.replace("=","-(")+")"
    grouped = eval(expression.replace(var,'1j'))
    return -grouped.real/grouped.imag




#What is the area of a square with length 4







