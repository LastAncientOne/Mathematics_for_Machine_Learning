
import math

options = " Rectangular Prism, General Prisms, Right Circular Cylinder, Square Pyramid, Right Circular Cone, Sphere,Quit".split(",")

def Rectangular Prism():
    length = float(input(print("Enter the length:"))
    width = float(input(print("Enter the width:"))
    height = float(input(print("Enter the height:"))
    Volume = length * width * height
    SA = 2*(length*width) + 2*(height*width) + 2*(length*height)
    print('Volume of a Rectangular: ', Volume)
    print('Surface Area of a Rectangular: ', SA)
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
            Rectangular Prism()
        
        elif choice == 2:
             run_program = False             


if __name__ == "__main__":
    main()
