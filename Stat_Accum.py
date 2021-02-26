#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Team Members:
#Malibiran, Jerry U.
#Melegrito, Aaron Joshua B.
#Ramos, Dexyn B.
#Talipnao, Kate Shiery P.

import tkinter
from tkinter import messagebox
from tkinter import *
import pandas as pd
#Use prettytable in formatting output instead
from prettytable import PrettyTable

#Variables: 
#p=number of parts,n=number of parts that passed through queue
#wq=waiting time,wqm=max waiting time, swq=sum waiitngt time
#ts=total time in system,tsm=max total time in system, sts=sum total time in system
#iq=in queue,is=in service
#qt=number of parts in queue,bt=busy/idle
#et=event type
#aq=area under Q(t)curve,qm=maximum value Q(t)

#table1=pd.read_csv("Desktop/table1.csv")

#Calculate
def stat_accum():
    #functions
    try:
        prd=int(inp.get())
        #Format output or prettytable
        table.grid(row=3, column=0, pady=5)
        Label(table, text="{:^15} {:^15} {:^18} {:^12} {:^12} {:^28} {:^18} {:^8} {:^8} {:^8} {:^8} {:^8} {:^8} {:^8} {:^7}"
              .format("0","0","Init","0","0","(1.20,1.30,6.30)","0","0","0","0","0","0","0","0","0"), 
              bg=bgc).grid(row=0, column=0, sticky="nw", padx=3)
    except:
        messagebox.showerror("Invalid Input", "Please input a valid simulation period (int).")

#def wq():
    
        
#Create window
root=Tk()
root.title("Statistical Accumulators")
root.maxsize(1135,510)

#Colors
bgc='peach puff'
fg='dim gray'

#Input and output frame
input_frame = Frame(root, width=200, height=500)
input_frame.grid(row=0, column=0, padx=10, pady=5)
output_frame = Frame(root, width=905, height=500, bg=bgc)
output_frame.grid(row=0, column=1, padx=10, pady=5)
table = Frame(output_frame, width=905, height=420, bg=bgc)
output_frame.grid_propagate(0)
table.grid_propagate(0)

#Input text box and buttons
Label(input_frame, text="Enter Simulation Period:").grid(row=0)
intVar = IntVar()
inp = Entry(input_frame)
inp.grid(row=1, column=0)
Button(input_frame, text='Okay', command=stat_accum).grid(row=2, column=0, pady=4)
Button(input_frame, text='Clear', command=table.grid_remove).grid(row=3, column=0, pady=4)

#Labels for the output
Label(output_frame, text="Table Simulation of the System", bg=bgc).grid(row=0,column=0, sticky='n')
Label(output_frame, text="{:^45} {:^18} {:^55} {:^63}"
          .format("Just Finished Event","Variables","Attributes","Statistical Accumulators"), 
          relief=GROOVE, bg=bgc).grid(row=1, column=0, sticky="nw", padx=3)
Label(output_frame, text="{:^13} {:^10} {:^13} {:^9} {:^9} {:^30} {:^20} {:^6} {:^6} {:^6} {:^6} {:^6} {:^6} {:^6} {:^6}"
          .format("Entity No.","Time(t)","Event Type","Q(t)","B(t)","In Queue","In Service","P","N","∑WQ","WQ*","∑TS","TS*","∫Q","Q*"), 
          bg=bgc,foreground=fg).grid(row=2, column=0, sticky="nw", padx=3)

root.mainloop()


# In[ ]:





# In[ ]:




