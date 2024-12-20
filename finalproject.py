
# Modules for the program
from tkinter import *
import math

# Main Window Setup
root = Tk()

root.title('Professional Calculator')
root.geometry('330x387')

#Entry field setup
e = Entry(root, width= 28, font="Arial,24", fg='black', bg='white', borderwidth=5)
e.grid(columnspan= 5)


# Function for numerical keys
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

# Function for clear key
def button_clear():
    e.delete(0,END)


# Function for equal sign after each operation
def button_equal():
    second_number = e.get()
    e.delete(0, END)
    try:
        second_number = float(second_number)
    except ValueError:
        e.insert(0, "Error")
        return


    if math == 'addition':
        e.insert(0,f_num + int(second_number))

    elif math == 'subtraction':
        e.insert(0,f_num - int(second_number))

    elif math == 'multiplication':
        e.insert(0,f_num * int(second_number))

    elif math == 'division':
        if second_number !=0:
            e.insert(0,f_num / int(second_number))
        else:
            e.insert(0, END)

    elif math == 'floor division':
        if second_number !=0:
            e.insert(0,f_num // int(second_number))
        else:
            e.insert(0, "Error")

    elif math == 'modulo':
        e.insert(0,f_num % int(second_number))

    elif math == 'decimal':
        e.insert(0,f_num + second_number)



#Functions for mathematical operations
def but_add():                   # Function for addition
    first_number = e.get()
    global f_num
    global math
    math = 'addition'
    try:
        f_num = float(first_number)
    except ValueError:
        e.insert(0,'Error')
        return
    e.delete(0, END)


def button_subtract():         # Function for subtraction
    first_number = e.get()
    global f_num
    global math
    math = 'subtraction'
    try:
        f_num = float(first_number)
    except ValueError:
        e.insert(0, 'Error')
        return
    e.delete(0, END)

def button_multiply():  # Multiplication function
    first_number = e.get()
    global f_num
    global math
    math = 'multiplication'
    try:
        f_num = float(first_number)  # Convert to float
    except ValueError:
        e.insert(0, "Error")
        return
    e.delete(0, END)

def button_divide():  # Division function
    first_number = e.get()
    global f_num
    global math
    math = 'division'
    try:
        f_num = float(first_number)  # Convert to float
    except ValueError:
        e.insert(0, "Error")
        return
    e.delete(0, END)

def button_floor_divide():  # Floor division function
    first_number = int(e.get())
    global f_num
    global math
    math = 'floor division'
    try:
        f_num = int(first_number)  # Convert to float
    except ValueError:
        e.insert(0, "Error")
        return
    e.delete(0, END)

def button_mod():  # Modulo function
    first_number = e.get()
    global f_num
    global math
    math = 'modulo'
    try:
        f_num = float(first_number)  # Convert to float
    except ValueError:
        e.insert(0, "Error")
        return
    e.delete(0, END)

def button_sin():              # Function for sin()
    angle = float(e.get())
    angle_rad = math.radians(angle)  # Convert degrees to radians
    result = math.sin(angle_rad)
    e.delete(0, END)
    e.insert(0, result)

def button_cos():               #Function for cos()
    angle = float(e.get())
    angle_rad = math.radians(angle)  # Convert degrees to radians
    result = math.cos(angle_rad)
    e.delete(0, END)
    e.insert(0, result)

def button_tan():     # FUnction for tan()
    angle = float(e.get())
    angle_rad = math.radians(angle)  # Convert degrees to radians
    result = math.tan(angle_rad)
    e.delete(0, END)
    e.insert(0, result)

def button_dec():
    current = e.get()
    if '.' not in current:  # Check if a decimal point is already in the current number
        e.delete(0, END)  # Clear the entry field
        e.insert(0, str(current) + '.')  # Insert the decimal point


def button_off():    # Function for OFF key
    quit()


# Setting up buttons for the calculator

But_divide_2 = Button(root, text='//', fg ="white",width=10, height= 3, bg='black', borderwidth=3, command=button_floor_divide) # floor division button
But_divide_2.grid(row=2, column=0)
But_off = Button(root, text='OFF', fg ="white",width=10, height= 3, bg='brown', borderwidth=3,command=button_off) # Off button
But_off.grid(row=2, column=1)
But_C = Button(root, text='C', fg ="white",width=10, height= 3, bg='brown', borderwidth=3,command= button_clear)  #Clear button
But_C.grid(row=2, column=2)
But_add = Button(root, text='+', fg ="white",width=10, height= 3, bg='black', borderwidth=3, command= but_add) # Addition button
But_add.grid(row=2, column=3)
But_1 = Button(root, text='1', fg ="white",width=10, height= 3, bg='black', borderwidth=3,command=lambda: button_click(1)) # Button 1
But_1.grid(row=3, column=0)
But_2 = Button(root, text='2', fg ="white",width=10, height= 3, bg='black', borderwidth=3, command=lambda: button_click(2)) # Button 2
But_2.grid(row=3, column=1)
But_3 = Button(root, text='3', fg ="white",width=10, height= 3, bg='black', borderwidth=3, command=lambda: button_click(3)) # Button 3
But_3.grid(row=3, column=2)
But_4 = Button(root, text='4', fg ="white",width=10, height= 3, bg='black', borderwidth=3,command=lambda: button_click(4)) # Button 4
But_4.grid(row=4, column=0)
But_5 = Button(root, text='5', fg ="white",width=10, height= 3, bg='black', borderwidth=3,command=lambda: button_click(5)) # Button 5
But_5.grid(row=4, column=1)
But_6 = Button(root, text='6', fg ="white",width=10, height= 3, bg='black', borderwidth=3,command=lambda: button_click(6)) # Button 6
But_6.grid(row=4, column=2)
But_7 = Button(root, text='7', fg ="white",width=10, height= 3, bg='black', borderwidth=3,command=lambda: button_click(7)) # Button 7
But_7.grid(row=5, column=0)
But_8 = Button(root, text='8', fg ="white",width=10, height= 3, bg='black', borderwidth=3,command=lambda: button_click(8)) # Button 8
But_8.grid(row=5, column=1)
But_9 = Button(root, text='9', fg ="white",width=10, height= 3, bg='black', borderwidth=3,command=lambda: button_click(9)) # Button 9
But_9.grid(row=5, column=2)
But_0 = Button(root, text='0', fg ="white",width=10, height= 3, bg='black', borderwidth=3,command=lambda: button_click(0)) # Button 0
But_0.grid(row=6, column=1)
But_sub = Button(root, text='-', fg ="white",width=10, height= 3, bg='black', borderwidth=3,command=button_subtract) # Subtraction button
But_sub.grid(row=3, column=3)
But_mult = Button(root, text='*', fg ="white",width=10, height= 3, bg='black', borderwidth=3,command=button_multiply) # Multiplication button
But_mult.grid(row=4, column=3)
But_div = Button(root, text='/', fg ="white",width=10, height= 3, bg='black', borderwidth=3,command=button_divide) # Division button
But_div.grid(row=5, column=3)
But_eq = Button(root, text='=', fg ="white",width=22, height= 3, bg='brown',command= button_equal) # Equal button
But_eq.grid(row=7, column=2, columnspan=4)
But_mod = Button(root, text='%', fg ="white",width=10, height= 3, bg='black',borderwidth=3,command=button_mod) # Modulo button
But_mod.grid(row=6, column=0)
But_tan = Button(root, text='tan', fg ="white",width=10, height= 3, bg='black',borderwidth=3,command=button_tan) # Tan() button
But_tan.grid(row=7, column=0)
But_cos = Button(root, text='cos', fg ="white",width=10, height= 3, bg='black', borderwidth=3,command=button_cos) # Cos() button
But_cos.grid(row=7, column=1)
But_sin = Button(root, text='sin', fg ="white",width=10, height= 3, bg='black',borderwidth=3,command=button_sin) # Sin() button
But_sin.grid(row=6, column=2)
But_dec = Button(root, text='.', fg ="white",width=10, height= 3, bg='black',borderwidth=3,command=button_dec) #
But_dec.grid(row=6, column=3)




root.mainloop()