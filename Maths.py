#Version 1.0.0, Created By Dylan Richards
# -*- coding: utf-8 -*-
import Tkinter, sys, tkMessageBox
from Tkinter import *
from decimal import Decimal
import random
from random import *

def addition():
    rootadd = Tk(className = " Addition")
    rootadd.geometry("{}x{}".format(300, 300))
    def home():
        rootadd.destroy()
        root.lift()
    homeadd = Button(rootadd, text="Home", command=home)
    homeadd.grid(row=4, column=0)
    add_onel = Label(rootadd, text="Digit")
    add_onel.grid(row=1, column=0)
    add_onee = Entry(rootadd, bd=1, bg="blue")
    add_onee.grid(row=1, column=1)
    add_twol = Label(rootadd, text="Digit")
    add_twol.grid(row=2, column=0)
    add_twoe = Entry(rootadd, bd=1, bg="blue")
    add_twoe.grid(row=2, column=1)
    def addsolve():
        x = add_onee.get()
        y = add_twoe.get()
        z = int(x) + int(y)
        tkMessageBox.showinfo("Answer", "The answer is " + str(z))    
    add_solveb = Button(rootadd, text="Solve", command=addsolve)
    add_solveb.grid(row=3, column=0)

def subtraction():
    rootsub = Tk(className=" Subtraction")
    rootsub.geometry("{}x{}".format(300, 300))
    def home():
        rootsub.destroy()
        root.lift()
    homesub = Button(rootsub, text="Home", command=home)
    homesub.grid(row=4, column=0)
    sub_onel = Label(rootsub, text="First Digit")
    sub_onel.grid(row=1, column=0)
    sub_onee = Entry(rootsub, bd=1, bg="blue")
    sub_onee.grid(row=1, column=1)
    sub_twol = Label(rootsub, text="Second Digit")
    sub_twol.grid(row=2, column=0)
    sub_twoe = Entry(rootsub, bd=1, bg="blue")
    sub_twoe.grid(row=2, column=1)
    def subsolve():
        x = sub_onee.get()
        y = sub_twoe.get()
        z = int(x) - int(y)
        tkMessageBox.showinfo("Answer", "The answer is " + str(z))
    sub_solveb = Button(rootsub, text="Solve", command=subsolve)
    sub_solveb.grid(row=3, column=0)

def multiplication():
    rootmulti = Tk(className=" Multiplication")
    rootmulti.geometry("{}x{}".format(300, 300))
    def home():
        rootmulti.destroy()
        root.lift()
    homemulti = Button(rootmulti, text="Home", command=home)
    homemulti.grid(row=4, column=0)
    multi_onel = Label(rootmulti, text="First Digit")
    multi_onel.grid(row=1, column=0)
    multi_onee = Entry(rootmulti, bd=1, bg="blue")
    multi_onee.grid(row=1, column=1)
    multi_twol = Label(rootmulti, text="Second Digit")
    multi_twol.grid(row=2, column=0)
    multi_twoe = Entry(rootmulti, bd=1, bg="blue")
    multi_twoe.grid(row=2, column=1)
    def multisolve():
        x = multi_onee.get()
        y = multi_twoe.get()
        z = int(x) * int(y)
        tkMessageBox.showinfo("Answer", "The answer is " + str(z))
    multi_solveb = Button(rootmulti, text="Solve", command=multisolve)
    multi_solveb.grid(row=3, column=0)

def division():
    rootdiv = Tk(className=" Division")
    rootdiv.geometry("{}x{}".format(300, 300))
    def home():
        rootdiv.destroy()
        root.lift()
    homediv = Button(rootdiv, text="Home", command=home)
    homediv.grid(row=4, column=0)
    div_onel = Label(rootdiv, text="First Digit")
    div_onel.grid(row=1, column=0)
    div_onee = Entry(rootdiv, bd=1, bg="blue")
    div_onee.grid(row=1, column=1)
    div_twol = Label(rootdiv, text="Second Digit")
    div_twol.grid(row=2, column=0)
    div_twoe = Entry(rootdiv, bd=1, bg="blue")
    div_twoe.grid(row=2, column=1)
    def divsolve():
        x = div_onee.get()
        y = div_twoe.get()
        z = int(x) / int(y)
        tkMessageBox.showinfo("Answer", "The answer is " + str(z))
    div_solveb = Button(rootdiv, text="Solve", command=divsolve)
    div_solveb.grid(row=3, column=0)

def square():
    rootsq = Tk(className=" Square")
    rootsq.geometry("{}x{}".format(300, 300))
    def home():
        rootsq.destroy()
        root.lift()
    homesq = Button(rootsq, text="Home", command=home)
    homesq.grid(row=3, column=0)
    sq_onel = Label(rootsq, text="Enter Digit")
    sq_onel.grid(row=1, column=0)
    sq_onee = Entry(rootsq, bd=1, bg="Blue")
    sq_onee.grid(row=1, column=1)
    def sqsolve():
        x = int(sq_onee.get())
        z = x ** 2
        tkMessageBox.showinfo("Answer", "The answer is " + str(z))
    sq_solveb = Button(rootsq, text="Solve", command=sqsolve)
    sq_solveb.grid(row=2, column=0)

def cube():
    rootcu = Tk(className=" Cube")
    rootcu.geometry("{}x{}".format(300, 300))
    def home():
        rootcu.destroy()
        root.lift()
    homecu = Button(rootcu, text="Home", command=home)
    homecu.grid(row=3, column=0)
    cu_onel = Label(rootcu, text="Enter Digit")
    cu_onel.grid(row=1, column=0)
    cu_onee = Entry(rootcu, bd=1, bg="Blue")
    cu_onee.grid(row=1, column=1)
    def cusolve():
        x = int(cu_onee.get())
        z = x ** 3
        tkMessageBox.showinfo("Answer", "The answer is " + str(z))
    cu_solveb = Button(rootcu, text="Solve", command=cusolve)
    cu_solveb.grid(row=2, column=0)

def power():
    rootpwr = Tk(className=" Power")
    rootpwr.geometry("{}x{}".format(300, 300))
    def home():
        rootpwr.destroy()
        root.lift()
    homepwr = Button(rootpwr, text="Home", command=home)
    homepwr.grid(row=4, column=0)
    pwronel = Label(rootpwr, text="Enter Digit")
    pwronel.grid(row=1, column=0)
    pwronee = Entry(rootpwr, bd=1, bg="Blue")
    pwronee.grid(row=1, column=1)
    pwrtwol = Label(rootpwr, text="Enter Power")
    pwrtwol.grid(row=2, column=0)
    pwrtwoe = Entry(rootpwr, bd=1, bg="Blue")
    pwrtwoe.grid(row=2, column=1)
    def pwrsolve():
        x = int(pwronee.get())
        y = int(pwrtwoe.get())
        z = x ** y
        tkMessageBox.showinfo("Answer", "The answer is " + str(z))
    pwrsolveb = Button(rootpwr, text="Solve", command=pwrsolve)
    pwrsolveb.grid(row=3, column=0)

def stanfrm():
    rootsf = Tk(className=" Standard Form")
    rootsf.geometry("{}x{}".format(300, 300))
    def home():
        rootsf.destroy()
        root.lift()
    homesf = Button(rootsf, text="Home", command=home)
    homesf.grid(row=3, column=0)
    sfonel = Label(rootsf, text="Enter Digit")
    sfonel.grid(row=1, column=0)
    sfonee = Entry(rootsf, bd=1, bg="blue")
    sfonee.grid(row=1, column=1)
    def sfsolve():
        x = float(sfonee.get())
        z = '%.4E' % Decimal(x)
        tkMessageBox.showinfo("Answer", "The answer is " + str(z))
    sfsolveb = Button(rootsf, text="Solve", command=sfsolve)
    sfsolveb.grid(row=2, column=0)

def pythag():
    rootpythag = Tk(className=" Pythagarus")
    rootpythag.geometry("{}x{}".format(300, 300))
    def home():
        rootpythag.destroy()
        root.lift()
    homepythag = Button(rootpythag, text="Home", command=home)
    homepythag.grid(row=4, column=0)
    al = Label(rootpythag, text="Enter a")
    al.grid(row=0, column=0)
    ee = Entry(rootpythag, bd=1, bg="Blue")
    ae.grid(row=0, column=1)
    
    
def main():
    global root
    root = Tk(className = " Home")
    root.geometry("{}x{}".format(300, 300))
    start_add = Button(root, text="Addition", command=addition)
    start_add.pack(fill=X)
    start_minus = Button(root, text="Subtraction", command=subtraction)
    start_minus.pack(fill=X)
    start_multiply = Button(root, text="Multiplication", command=multiplication)
    start_multiply.pack(fill=X)
    start_divide = Button(root, text="Division", command=division)
    start_divide.pack(fill=X)
    start_square = Button(root, text="Square", command=square)
    start_square.pack(fill=X)
    start_cube = Button(root, text="Cube", command=cube)
    start_cube.pack(fill=X)
    start_power = Button(root, text="Power", command=power)
    start_power.pack(fill=X)
    def QUIT():
        if tkMessageBox.askyesno("Quit", "Are you sure you want to quit?"):
            root.destroy()
    start_sf = Button(root, text="Number to S.F.", command=stanfrm)
    start_sf.pack(fill=X)
    start_pythag = Button(root, text="Pythagarus", command=pythag)
    start_pythag.pack(fill=X)
    start_quit = Button(root, text="Quit", command=QUIT)
    start_quit.pack(fill=X)
    root.mainloop()

main()
