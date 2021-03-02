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
import statistics as st

#GUI
prd=0
def show_table():
        table.grid_remove
    #try:
        prd=int(inp.get())
        min_time = 1
        max_time = 10
        entities = generate_entities(min_time,max_time,prd)
        matrix = create_matrix(entities, prd)
        #Format output
        table.grid(row=3, column=0, pady=5)
        summary.grid(row=4, column=0, pady=5)
        i=0
        for row in matrix:
            j=0
            cols=[]
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
        Label(summary,text="Summary of Statistical Accumulators" +
                "\n1. The number of parts produced so far: " + str(matrix[len(matrix)-1][7]) +
                "\n2. The total of the waiting times in queue so far: " + str(matrix[len(matrix)-1][9]) +
                "\n3. The number of parts that have passed through the queue so far: " + str(matrix[len(matrix)-1][8]) +
                "\n4. The longest time spent in queue we’ve seen so far: " + str(matrix[len(matrix)-1][10]) +
                "\n5. The total of the time spent in the system by all parts that have departed so far: " +
                "\n6. The longest time in system we’ve seen so far: " + str(matrix[len(matrix)-1][12]) +
                "\n7. The area so far under the queue-length curve Q(t): " +
                "\n8. The highest level that Q (t) has so far attained: "  +
                "\n9. The area so far under the server-busy function B (t): " + str(matrix[len(matrix)-1][15])
                ,bg=bgc, justify=LEFT).grid(row=0, column=0, sticky='W', padx=3)
        Label(summary,text="Output Performance Measures" +
                "\n1. Total production" +
                "\n2. Average waiting time in queue: "  +
                "\n3. Maximum waiting time in queue: " + str(matrix[len(matrix)-1][10]) +
                "\n4. Average total time in system: " + str(round(st.fmean(column(matrix,11)),2)) +
                "\n5. Maximum total time in system: " + str(matrix[len(matrix)-1][12]) +
                "\n6. Time-average number of parts in queue: " +
                "\n7. Maximum number of parts in queue: " + 
                "\n8. Drill-press utilization: "
                ,bg=bgc, justify=LEFT).grid(row=0, column=1, sticky='W', padx=3)
    #except:
        #messagebox.showerror("Invalid Input", "Please input a valid simulation period (int).")

#Convert lists to string
def listToString(s):
    listToStr = ' '.join([str(elem) for elem in s]) 
    return listToStr

#Combine functions
def clear():
    table.grid_remove

#Extract column
def column(matrix, i):
    return [int(row[i]) for row in matrix[1:]]

#Create window
root=Tk()
root.title("Statistical Accumulators")


#Colors
bgc='peach puff'
fg='dim gray'

#Input and output frame configuration to make frames resizeable
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
input_frame = Frame(root, width=180)
input_frame.rowconfigure(0, weight=1)
input_frame.grid(row=0, column=0, padx=10, pady=5)
output_frame = Frame(root, bg=bgc)
output_frame.grid(row=0, column=1, padx=10, pady=5)
output_frame.rowconfigure(0, weight=1)
output_frame.columnconfigure(1, weight=1)
table = Frame(output_frame, bg=bgc)
summary = Frame(output_frame, bg=bgc)


#Input text box and buttons
Label(input_frame, text="Enter Simulation Period:").grid(row=0)
intVar = IntVar()
inp = Entry(input_frame)
inp.grid(row=1, column=0)
Button(input_frame, text='Okay', command=show_table).grid(row=2, column=0, pady=4)

#Labels for the output
Label(output_frame, text="Table Simulation of the System", bg=bgc).grid(row=0,column=0, sticky='n')
root.mainloop()
