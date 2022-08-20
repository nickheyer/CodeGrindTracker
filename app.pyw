import os
from tkinter import *
from csv import writer, QUOTE_MINIMAL
from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter.messagebox import askyesno
from datetime import date, datetime

#Initialization
def get_root_dir():
	return os.path.dirname(__file__)

def generate_csv():	
	with open("problem_time.csv",'w+') as f:
		writer_object=writer(f)
		row=["Problem Link","Date","Time","Time Taken(s)","Time Taken(m)","Attempted before","Solved"]
		writer_object.writerow(row)
		f.close()	
	return

if not os.path.exists(os.path.join(get_root_dir(), "problem_time.csv")):
	generate_csv()



ws = Tk()
ws.geometry('245x225+500+150')
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
				if counter<10:
					display="0"+str(counter)
				else:
					display=str(counter)
			lbl['text']=display    
			lbl.after(1000, count)    
			counter += 1
	count()     

def StartTimer(lbl):
	global prob_link,attempted
	prob_link=""
	while prob_link=="":
		prob_link=askstring('Problem Link', 'Enter Problem Link')
		if(prob_link==""):
			messagebox.showinfo(title="Error", message="Please input link")
		else:
			attempted = askyesno(title='Attempted?',message='Have You attempted this before?')
				


	global date,time
	date=date.today()
	time=datetime.now()
	time = time.strftime("%H:%M:%S")

	global running
	running=True
	counter_label(lbl)
	start_btn['state']='disabled'
	stop_btn['state']='normal'
	reset_btn['state']='normal'
	save_btn['state']='normal'


def StopTimer():
	global running
	start_btn['state']='normal'
	stop_btn['state']='disabled'
	reset_btn['state']='normal'
	save_btn['state']='normal'
	running = False
	SaveTimer(lbl)
	answer = askyesno(title='Confirmation',message='Do you want to Reset this time')
	if answer:
		ResetTimer(lbl)


def ResetTimer(lbl):
    global counter
    counter=-1
    if running==False:      
        reset_btn['state']='disabled'
        lbl['text']='00'
    else:                          
        lbl['text']=''

def SaveTimer(lbl):
	answer = askyesno(title='Confirmation',message='Do you want to save this data')
	if answer:
		solved = askyesno(title='Confirmation',message='Were you able to solve this problem?')
		secs=counter
		mins=secs/60
		mins='%.2f' % mins
		row=[prob_link,date,time,secs,mins,attempted,solved]
		with open("problem_time.csv",'a') as f:
			writer_object = writer(f)
			writer_object.writerow(row)
	running = False

def ResetCSV():
	answer = askyesno(title='Confirmation',message='Do you want to RESET the CSV file')
	if answer:
		generate_csv()
	running = False



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

lbl.place(x=100, y=50)
label_msg.place(x=90, y=90)

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
    command=lambda:StopTimer()
    )

reset_btn = Button(
    ws, 
    text='Reset', 
    width=5, 
    state='disabled', 
    font="Verdana 10 bold",
    command=lambda:ResetTimer(lbl)
    )
save_btn = Button(
    ws, 
    text='Save', 
    width=5, 
    state='disabled', 
    font="Verdana 10 bold",
    command=lambda:SaveTimer(lbl)
    )
RESET_CSV_btn = Button(
    ws, 
    text='Reset CSV', 
    width=10, 
    state='normal', 
    font="Verdana 10 bold",
    command=lambda:ResetCSV()
    )

start_btn.place(x=15, y=155)
stop_btn.place(x=75, y=155)
RESET_CSV_btn.place(x=135, y=155)



ws.mainloop()
