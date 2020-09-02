from tkinter import *
from PIL import ImageTk,Image
import tkinter.font as font
import tkinter as tk
from mainv2 import CRUD,totalInput
from alarm import Alarm
import threading
import os

class startPage:
	def __init__(self):
		window = Tk()
		window.title('Online class Bot')
		window.geometry("790x400+300+200")

		myFont = font.Font(weight="bold")

		#Image
		img = Image.open('bot.png')
		img = img.resize((100, 100), Image.ANTIALIAS)
		img = ImageTk.PhotoImage(img)
		panel = Label(window, image=img,bg='#87ceeb')
		panel.image = img
		panel.place(x=320,y=70)

		#Icon Image
		photo = PhotoImage(file = "bot.png")
		window.iconphoto(False, photo)

		#label
		heading = Label(window, text = "Welcome!",bg='#87ceeb',font='bold').place(x=340,y=40)

		#buttons
		btn=Button(window, text="Add Link and time",fg='white' ,bg='red',command=linkPage)
		btn.place(x=80, y=100)
		btn['font']=myFont

		btn1=Button(window, text="Add Gmail ID and Password",fg='white' , bg='red',command=CredsPage)
		btn1.place(x=450, y=100)
		btn1['font']=myFont

		btn=Button(window, text="Start Scheduler",fg='white' ,bg='red',command=runSchedulePage)
		btn.place(x=80, y=240)
		btn['font']=myFont

		#for Background Color
		window.configure(bg='#87ceeb')
		window.mainloop()


class linkPage:

	def submitDetails(self):
		self.Ti = totalInput()
		fromht = list(str(self.fromtime.get()).split(" "))
		toht = list(str(self.totime.get()).split(" "))
		self.Ti.formatInput(fromht,toht,str(self.link.get()))
		self.newwindow.destroy()

	def __init__(self):
		self.newwindow = Toplevel()
		self.newwindow.title("Enter Details")

		#geometry of the window
		self.newwindow.geometry("400x400+200+200")
		self.newwindow.configure(bg='#87ceeb')

		self.heading = Label(self.newwindow, text="Please enter the details",bg='#87ceeb',font='bold').place(x=70,y=40)

		#Labels
		self.fromlable = Label(self.newwindow,text="From Time (eg: 09:45 AM): ",bg='#87ceeb',font='bold').place(x=25,y=90)

		self.tolable = Label(self.newwindow,text="To Time (eg: 09:45 PM): ",bg='#87ceeb',font='bold').place(x=25,y=160)

		self.linklable = Label(self.newwindow,text="Link: ",bg='#87ceeb',font='bold').place(x=25,y=220)

		#Text Box
		self.fromtime = StringVar()
		Entry(self.newwindow,width=35,textvariable=self.fromtime).place(x=150,y=120)

		self.totime = StringVar()
		Entry(self.newwindow,width=35,textvariable=self.totime).place(x=150,y=190)

		self.link = StringVar()
		Entry(self.newwindow,width=35,textvariable=self.link).place(x=150,y=230)

		
		#submit Button
		self.submitbtn = Button(self.newwindow,text="Submit",fg='white' , bg='red',command=self.submitDetails).place(x=130,y=300)

class runSchedulePage:

	def closeIt(self):
		self.t1.stop()
		self.newwindow.destroy()

	def __init__(self):
		self.newwindow = Toplevel()
		self.newwindow.title("Running Scheduler")

		self.newwindow.geometry("400x400+200+200")
		self.newwindow.configure(bg="#87ceeb")

		self.schedule = Alarm()
		self.l = self.schedule.Checkalarm()
		# print(self.l)
		if(not self.l):
			self.runninglabel = Label(self.newwindow,text="Running...",bg='#87ceeb',font='bold',fg='green').pack()
			os.system("cmd /k python alarm.py -r")
		else:
			self.runninglabel = Label(self.newwindow,text=self.l,bg='#87ceeb',font='bold',fg='red').pack()

		self.btn = Button(self.newwindow,text="Close",fg="white",bg="red",command=self.closeIt).place(x=170,y=300)




class SchedulerPage:
	def closeIt(self):
		self.newwindow.destroy()

	def __init__(self):
		self.newwindow = Toplevel()

		self.newwindow.title("Running Scheduler")

		#geometry of the window
		self.newwindow.geometry("400x400+200+200")
		self.newwindow.configure(bg='#87ceeb')

		self.schedule = Alarm()
		self.l = self.schedule.Checkalarm()

		if(self.l is None):
			self.runninglabel = Label(self.newwindow,text="Running...",bg='#87ceeb',font='bold',fg='green').pack()
		else:
			self.runninglabel = Label(self.newwindow,text=self.l,bg='#87ceeb',font='bold',fg='red').pack()

		self.btn = Button(self.newwindow,text="Close",fg="white",bg="red",command=closeIt)


class CredsPage:

	# global email
	# global password

	def submitCreds(self):
		crud = CRUD()
		crud.userInsert(self.email.get(),self.password.get())
		self.newwindow.destroy()
		

	def __init__(self):
		self.newwindow = Toplevel()
		self.newwindow.title("Enter your Credentials")

		#geometry of the window
		self.newwindow.geometry("400x400+200+200")
		self.newwindow.configure(bg='#87ceeb')

		self.heading = Label(self.newwindow, text="Please enter your Credentials",bg='#87ceeb',font='bold').place(x=70,y=40)

		#Labels
		self.emaillabel = Label(self.newwindow,text="Email ID: ",bg='#87ceeb',font='bold').place(x=25,y=90)

		self.passlabel = Label(self.newwindow,text="Password: ",bg='#87ceeb',font='bold').place(x=25,y=160)

		#Text Box
		self.email = StringVar()
		Entry(self.newwindow,width=35,textvariable=self.email).place(x=150,y=95)

		self.password = StringVar()
		Entry(self.newwindow,show="*",width=35,textvariable=self.password).place(x=150,y=170)

		
		#submit Button
		self.submitbtn = Button(self.newwindow,text="Submit",fg='white' , bg='red',command=self.submitCreds).place(x=130,y=300)


app = startPage()
# app.mainloop()
