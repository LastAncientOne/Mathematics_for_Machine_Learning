# -*- coding: utf-8 -*-
"""
Created on Fri May 24 18:26:44 2019

@author: Tin
"""

from tkinter import *
import math

window=Tk()
window.title('Calculation of Area, Perimeter, & Circumference')
window.configure(bg='black')
length=IntVar()
width=IntVar()
radius=IntVar()

def calculateArea():
    l = length.get()
    w = width.get()
    area= l*w
    e4.insert(0,float(area))
    
def calculatePerimeter():
    l = length.get()
    w = width.get()
    perimeter = 2*(l+w)
    e5.insert(0,float(perimeter))
    
def calculateAreaC():
    r = radius.get()
    area_c = math.pi * r**2
    e6.insert(0,float(area_c))   
    
def calculateCC():
    r = radius.get()
    c_c = 2*math.pi*r
    e7.insert(0,float(c_c))       

def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)

Label(text='Area, Perimeter, & Circumference',pady=20,font=('arial',20,'bold'),fg='white',bg='black').grid(row=0, column=1)

Label(text='Enter Length:',padx=100,font=('arial',15,'bold'),bg='black',fg='white').grid(row=1,sticky=W)
e1= Entry(width=40,font=('arial',15,'bold'),textvariable=length)
e1.grid(row=1,column=1)

Label(text='Enter Width:',padx=100,font=('arial',15,'bold'),bg='black',fg='white').grid(row=2,sticky=W)
e2= Entry(width=40,font=('arial',15,'bold'),textvariable=width)
e2.grid(row=2,column=1)

Label(text='Enter Radius:',padx=100,font=('arial',15,'bold'),bg='black',fg='white').grid(row=3,sticky=W)
e3= Entry(width=40,font=('arial',15,'bold'),textvariable=radius)
e3.grid(row=3,column=1)

Label(text='CALCULATE AREA:',padx=0,font=('arial',15,'bold'),bg='black',fg='white').grid(row=4,sticky=W)
e4= Entry(width=40,font=('arial',15,'bold'))
e4.grid(row=4,column=1)

Label(text='CALCULATE PERIMETER:',padx=0,font=('arial',15,'bold'),bg='black',fg='white').grid(row=5,sticky=W)
e5= Entry(width=40,font=('arial',15,'bold'))
e5.grid(row=5,column=1)

Label(text='CALCULATE AREA OF CIRCLE:',padx=0,font=('arial',15,'bold'),bg='black',fg='white').grid(row=6,sticky=W)
e6= Entry(width=40,font=('arial',15,'bold'))
e6.grid(row=6,column=1)

Label(text='CALCULATE CIRCUMFERENCE:',padx=0,font=('arial',15,'bold'),bg='black',fg='white').grid(row=7,sticky=W)
e7= Entry(width=40,font=('arial',15,'bold'))
e7.grid(row=7,column=1)

clear()

Button(text='Calculate Area',font=('arial',15,'bold'),width=20,command=calculateArea,bg='blue',fg='white').grid(row=8,column=1,sticky=W)
Button(text='Calculate Perimeter',font=('arial',15,'bold'),width=20,command=calculatePerimeter,bg='blue',fg='white').grid(row=9,column=1,sticky=W)
Button(text='Calculate Area of Circle',font=('arial',15,'bold'),width=20,command=calculateAreaC,bg='blue',fg='white').grid(row=10,column=1,sticky=W)
Button(text='Calculate Circumference',font=('arial',15,'bold'),width=20,command=calculateCC,bg='blue',fg='white').grid(row=11,column=1,sticky=W)
Button(text='Clear',font=('arial',15,'bold'),width=20,command=clear,bg='blue',fg='white').grid(row=12,column=1,sticky=W)

window.mainloop()
