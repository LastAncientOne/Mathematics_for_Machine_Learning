# -*- coding: utf-8 -*-
"""
Created on Thu May 23 11:07:59 2019

@author: Tin
"""
import math

options = " Square, Rectangle, Triangle, Circle, Trapezoid, Quit".split(",")

def square():
    print("Enter Side of Sqaure:")
    side = input()
    Area = float(side) * float(side)
    Perimeter = 4 * float(side)
    print('Area of a Square: ', Area)
    print('Perimeter of a Square: ', Perimeter)
    return 

def rectangle():
    print("Enter Length of Rectangle:")
    length = float(input())
    print("Enter Width of Rectangle:")
    width = float(input())
    Area = float(length) * float(width)
    Perimeter = 2 * (length + width)
    print('Area of a Rectangle: ', Area)
    print('Perimeter of a Rectangle: ', Perimeter)
    return 

def triangle():
    print("Enter a of Triangle:")
    a = input()
    print("Enter b of Triangle:")
    b = input()
    print("Enter c of Triangle:")
    c = input()
    print("Enter h of Triangle:")
    h = input()
    Area = (float(b) * float(h))/2
    Perimeter = float(a) + float(b) + float(c)
    print('Area of a Triangle: ', Area)
    print('Perimeter of a Triangle: ', Perimeter)
    return 

def circle():
    print("Radius of a Circle:")
    r = input()
    Area = math.pi * float(r)**2
    Circumference = 2 * float(r) * math.pi
    print('Area of a Circle: ', Area)
    print('Circumference of a Circle:', Circumference)
    return 

def trapezoid():
    print("Trapezoid:")
    a = float(input('Enter the First Base of a Trapezoid: '))
    b = float(input('Enter the Second Base of a Trapezoid: '))
    h = float(input('Enter the Height of a Trapezoid: '))
    c = float(input('Enter the Side of a Trapezoid: '))
    d = float(input('Enter the Side of a Trapezoid: '))
    Area = 0.5 * (a + b) * h
    Perimeter = a + b + c + d
    print('Area of a Trapezoid: ', Area)
    print('Perimeter of a Trapeziod:', Perimeter)
    return 

def main():
    run_program = True
    while run_program:
        print("\n")
        print("Choose Option:")
        print("Area, Perimeter, Circumference of Shapes")
        for i in range(1, len(options)+1):
            print("{} - {}".format(i, options[i-1]))
        choice = int(input())
        
        if choice == 1:            
            print('_____Square_____') 
            square()
        elif choice == 2:
            print('_____Rectangle_____')
            rectangle()
        elif choice == 3:
            print('_____Triangle_____')
            triangle()
        elif choice == 4:
            print('_____Circle_____')
            circle()                
        elif choice == 5:
            print('_____Trapezoid_____')
            trapezoid()                            
        elif choice == 6:
             run_program = False             


if __name__ == "__main__":
    main()