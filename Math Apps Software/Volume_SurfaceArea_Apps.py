# -*- coding: utf-8 -*-
"""
Created on Thu May 31 10:08:59 2019
@author: Tin
"""

import math

options = " Rectangular Prism, Triangle Prism, Trapezoidal Prism, Right Circular Cylinder, Square Pyramid, Right Circular Cone, Sphere,Quit".split(",")

def Rectangular_Prism():
    length = float(input(print("Enter the length:"))
    width = float(input(print("Enter the width:"))
    height = float(input(print("Enter the height:"))
    Volume = length * width * height
    SA = 2*(length*width) + 2*(height*width) + 2*(length*height)
    print('Volume of a Rectangular: ', Volume)
    print('Surface Area of a Rectangular: ', SA)
    return
                   

def Triangle_Prism():
    side1 = float(input(print("Enter the side1:"))
    side2 = float(input(print("Enter the side2:"))
    side3 = float(input(print("Enter the side3:")) 
    height = float(input(print("Enter the height:"))
    base = (length * width) /2
    Volume = base * height
    SA = (base * 2) + (side1 * height) + (side2 * height) + (side3 * height) 
    print('Volume of a Triangle_Prisms: ', Volume)
    print('Surface Area of a Triangle_Prisms: ', SA)
    return                 
                   
def Trapezoidal_Prism():
    base1 = float(input(print("Enter the base1:"))
    base2 = float(input(print("Enter the base2:"))              
    side1 = float(input(print("Enter the side1:"))
    side2 = float(input(print("Enter the side2:"))
    ab = float(input(print("Enter the altitude of the base:")) 
    height = float(input(print("Enter the height:"))
    p = base1 + base2 + side1 + side2 # perimeter of the base is the sum of the lengths of the sides
    B = 0.5*ab*(base1+base2)
    Volume = base * height
    SA = p*height + 2*B
    print('Volume of a Triangle_Prisms: ', Volume)
    print('Surface Area of a Triangle_Prisms: ', SA)
    return  

                   
def Square_Pyramid():             
    side1 = float(input(print("Enter the side1 of a square:"))
    side2 = float(input(print("Enter the side2 of a square:"))
    sh = float(input(print("Enter the slant height:")) 
    height = float(input(print("Enter the height:"))
    p = side1 + side2 + side1 + side2 # perimeter of the base is the sum of the lengths of the sides
    B = side1 * side2 # Area of Base
    area_4_triangle = 4 * ((sh*1)/2)
    Volume = 1/3 * B * height
    SA = B + 0.5 * p * sh 
    print('Volume of a Triangle_Prisms: ', Volume)
    print('Surface Area of a Triangle_Prisms: ', SA)
    return 
                   
                   
def Right_Circular_Cylinder():
    radius = float(input(print("Enter the radius:"))
    height = float(input(print("Enter the height:"))
    area = math.pi * radius**2
    c = 2 * math.pi * radius               
    Volume = area * height
    SA = (2*area) + (c * height)
    print('Volume of a Triangle_Prisms: ', Volume)
    print('Surface Area of a Triangle_Prisms: ', SA)
    return  

                   
def Sphere():
    radius = float(input(print("Enter the radius:"))
    # area = math.pi * radius**2
    # c = 2 * math.pi * radius               
    Volume = 4/3 * math.pi * r**3
    SA = 4 * math.pi* r**2
    print('Volume of a Triangle_Prisms: ', Volume)
    print('Surface Area of a Triangle_Prisms: ', SA)
    return  
                   
def main():
    run_program = True
    while run_program:
        print("______Calculation______")
        print("Volume and Area Surface")
        print("\n")
        print("Choose Option:")
        for i in range(1, len(options)+1):
            print("{} - {}".format(i, options[i-1]))
        choice = int(input())
        
        if choice == 1:            
            print('_____Rectangular Prism_____') 
            Rectangular_Prism()
        elif choice == 2:
            print('_____Triangle Prism_____')
            Triangle_Prism()
        elif choice == 3:
            print('_____Trapezoidal Prism_____')
            Trapozid_Prism()   
        elif choice == 4:
            print('_____Square Pyramid_____')
            Square_Pyramid()   
        elif choice == 5:
            print('_____Right Circular Cylinder_____')
            Right_Circular_Cylinder()  
        elif choice == 6:
            print('_____Sphere_____')
            Sphere()  
        elif choice == 7:
             run_program = False             


if __name__ == "__main__":
    main()
