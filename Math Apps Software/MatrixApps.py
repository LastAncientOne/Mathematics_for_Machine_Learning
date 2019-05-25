# -*- coding: utf-8 -*-
"""
Created on Thu May 23 12:13:20 2019

@author: Tin
"""

import numpy as np
from numpy.linalg import inv

options = " Matrix Addition, Matrix Subtraction, Matrix Multiplication, Matrix Division, Dot Product, Matrix Scalar, Matrix Transpose, Matrix Inverse, Pseudo Inverse Matrix, Quit".split(",")

def input_X_matrix():
    R = int(input("Enter the number of rows: ")) 
    C = int(input("Enter the number of columns: ")) 
    print("Input the entries in a single line (separated by space): ") 
    x = list(map(int, input().split())) 
    X_matrix = np.array(x).reshape(R, C) 
    print(X_matrix) 
    return X_matrix

def input_Y_matrix():
    R = int(input("Enter the number of rows: ")) 
    C = int(input("Enter the number of columns: ")) 
    print("Input the entries in a single line (separated by space): ") 
    y = list(map(int, input().split())) 
    Y_matrix = np.array(y).reshape(R, C) 
    print(Y_matrix) 
    return Y_matrix

def matrix_addition():
    add = input_X_matrix() + input_Y_matrix()
    return add

def matrix_subtraction():
    sub = input_X_matrix() - input_Y_matrix()
    return sub

def matrix_multiplication(): 
    multiply = input_X_matrix() * input_Y_matrix()
    return multiply

def matrix_divison(): 
    divison = input_X_matrix() / input_Y_matrix()
    return divison

def dot_product(): 
    A = input_X_matrix()
    B = input_Y_matrix()
    C = A.dot(B)
    print('___Dot Product___')  
    print(C)
    return C

def matrix_scalar():
    A = input_X_matrix()
    b = float(input("Enter a number: "))
    c = A*b
    print('__Matrix-Scalar Multiplication___')
    print(c)
    return c

def matrix_transpose():
    mt = input_X_matrix()
    T_m = mt.T 
    print('___Matrix Transpose___')
    print(T_m)
    return

def matrix_inverse():
    mt = input_X_matrix()
    I_m = inv(mt) 
    print('___Matrix Inverse___')
    print(I_m)
    return

def p_inverse():
    m = input_X_matrix()
    pim = np.linalg.pinv(m)
    print('___Pseudo Inverse Matrix___')
    print(pim)
    return

def main():
    run_program = True
    while run_program:
        print("\n")
        print("Choose Option:")
        print("Mathematics for Machine Learning Linear Algebra")
        for i in range(1, len(options)+1):
            print("{} - {}".format(i, options[i-1]))
        choice = int(input())
        
        if choice == 1:     
             print('___Matrix Addition___')                  
             matrix_addition()
        elif choice == 2:
             print('___Matrix Subtraction___')            
             matrix_subtraction()
        elif choice == 3:
             print('___Matrix Multiplication___')               
             matrix_multiplication()
        elif choice == 4:
             print('___Matrix Division___')               
             matrix_divison()             
        elif choice == 5:    
             dot_product()
        elif choice == 6:    
             matrix_scalar()
        elif choice == 7:            
             matrix_transpose()             
        elif choice == 8:            
             matrix_inverse()
        elif choice == 9:            
             p_inverse()    
        elif choice == 10:
             run_program = False             


if __name__ == "__main__":
    main()