from tkinter import *
from PIL import ImageTk, Image
import pandas as pd
from csv import writer

ws = Tk()
ws.geometry('200x225+500+150')
ws.title('CodeWatch')
ws.config(bg='#299617')
ws.resizable(0,0)
ws.wm_attributes("-topmost", 1)


counter = -1
running = False
def counter_label(lbl):
    def count():
        if running:
            global counter
            if counter==-1:             
                display="00"
            else:
                display=str(counter)

            lbl['text']=display    
            
            lbl.after(1000, count)    
            counter += 1
    count()     

def StartTimer(lbl):
    global running
    running=True
    counter_label(lbl)
    start_btn['state']='disabled'
    stop_btn['state']='normal'
    reset_btn['state']='normal'

def StopTimer():
	global running
	start_btn['state']='normal'
	stop_btn['state']='disabled'
	reset_btn['state']='normal'
	secs=counter
	mins=secs/60
	row=[secs,mins]
	with open("problem_time.csv",'a') as f:
		writer_object = writer(f)
		writer_object.writerow(row)
	running = False

def ResetTimer(lbl):
    global counter
    counter=-1
    if running==False:      
        reset_btn['state']='disabled'
        lbl['text']='00'
    else:                          
        lbl['text']=''



lbl = Label(
    ws, 
    text="00", 
    fg="black", 
    bg='#299617', 
    font="Verdana 20 bold"
    )

label_msg = Label(
    ws, text="seconds", 
    fg="black", 
    bg='#299617', 
    font="Verdana 10 bold"
    )

lbl.place(x=80, y=50)
label_msg.place(x=70, y=90)

start_btn=Button(
    ws, 
    text='Start', 
    width=5, 
    font="Verdana 10 bold",
    command=lambda:StartTimer(lbl)
    )

stop_btn = Button(
    ws, 
    text='Stop', 
    width=5, 
    state='disabled',
    font="Verdana 10 bold",
    command=StopTimer
    )

reset_btn = Button(
    ws, 
    text='Reset', 
    width=5, 
    state='disabled', 
    font="Verdana 10 bold",
    command=lambda:ResetTimer(lbl)
    )

start_btn.place(x=15, y=155)
stop_btn.place(x=75, y=155)
reset_btn.place(x=135, y=155)



ws.mainloop()