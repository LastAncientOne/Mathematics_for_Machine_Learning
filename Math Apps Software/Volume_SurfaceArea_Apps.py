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
                   
def main():
    run_program = True
    while run_program:
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
             run_program = False             


if __name__ == "__main__":
    main()
