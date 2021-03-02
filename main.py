#Team Members:
#Malibiran, Jerry U.
#Melegrito, Aaron Joshua B.
#Ramos, Dexyn B.
#Talipnao, Kate Shiery P.

import tkinter
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import pandas as pd
import functions
from functions import *

#GUI
prd=0
def show_table():
    try:
        prd=int(inp.get())
        min_time = 1
        max_time = 10
        entities = generate_entities(min_time,max_time,prd)
        matrix = create_matrix(entities, prd)
        #Format output
        table.grid(row=3, column=0, pady=5)
        rows=[]
        i=0
        for row in matrix:
            cols=[]
            j=0
            for col in row:
                space="{:>8}"
                cols.append(col)
                if (j==5):
                    cols[j] = listToString(cols[j])
                    space="{:^35}"
                if (j>7):
                    space="{:^5}"
                if(j<5):
                    space="{:>10}"
                Label(table,text=space.format(cols[j]),bg=bgc).grid(row=i, column=j, padx=3)
                j=j+1
            i = i+1
    except:
        messagebox.showerror("Invalid Input", "Please input a valid simulation period (int).")

#Convert lists to string
def listToString(s):
    listToStr = ' '.join([str(elem) for elem in s]) 
    return listToStr

#Combine functions
def clear():
    table.grid_remove

#Create window
root=Tk()
root.title("Statistical Accumulators")


#Colors
bgc='peach puff'
fg='dim gray'

#Input and output frame configuration to make frames resizeable
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
input_frame = Frame(root)
input_frame.rowconfigure(0, weight=1)
input_frame.columnconfigure(0, weight=1)
input_frame.grid(row=0, column=0, padx=10, pady=5)
output_frame = Frame(root, bg=bgc)
output_frame.grid(row=0, column=1, padx=10, pady=5)
output_frame.rowconfigure(0, weight=1)
output_frame.columnconfigure(1, weight=1)
table = Frame(output_frame, bg=bgc)


#Input text box and buttons
Label(input_frame, text="Enter Simulation Period:").grid(row=0)
intVar = IntVar()
inp = Entry(input_frame)
inp.grid(row=1, column=0)
Button(input_frame, text='Okay', command=show_table).grid(row=2, column=0, pady=4)
Button(input_frame, text='Clear', command=table.grid_remove).grid(row=3, column=0, pady=4)

#Labels for the output
Label(output_frame, text="Table Simulation of the System", bg=bgc).grid(row=0,column=0, sticky='n')
root.mainloop()