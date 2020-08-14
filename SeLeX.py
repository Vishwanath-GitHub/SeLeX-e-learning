import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
import tkinter.messagebox

import goto
import label as label
from goto import with_goto
import requests

HEIGHT = 720
WIDTH = 1280

def validate(uname, passwrd, root):
	creds_dict = {"sarthak":"sarthak", "kunal":"kunal", "vishu": "vishu"}
	if uname in creds_dict and creds_dict[uname] == passwrd:
		root.destroy()
		search_page()


	elif uname  not in creds_dict or creds_dict[uname] != passwrd:
		tkinter.messagebox.showinfo("Failed", "Invalid Creds")

def login_page():
	root = Tk()
	root.title("SeLeX Login")
	canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
	canvas.pack()

	background_image = tk.PhotoImage(file='final.png')
	background_label = tk.Label(root, image=background_image)
	background_label.place(relwidth=1, relheight=1)


	fontStyle = tkFont.Font(family="Times New Roman", size=10)

	frame1 = tk.Frame(root, bg='#80c1ff', bd=5)
	frame1.place(relx=0.34, rely=0.66, relwidth=0.25, relheight=0.05, anchor='n')
	uname = Label(frame1, text = "Username").place(x = 30,y = 50)

	entry = tk.Entry(frame1, font=100)
	entry.place(relx=0,relwidth=1, relheight=1)

	frame2 = tk.Frame(root, bg='#3b5249', bd=5)
	frame2.place(relx=0.34, rely=0.735, relwidth=0.25, relheight=0.05, anchor='n')

	entry2 = tk.Entry(frame2, font=100,show="*")
	entry2.place(relx=0	,relwidth=1, relheight=1)
	fontStyle = tkFont.Font(family="Berlin Sans FB", size=25)
	button = tk.Button(root, text = 'LOGIN', bg = '#a3def8', fg = '#0c3b6a', font= fontStyle, command=lambda : validate(entry.get(), entry2.get(), root))
	button.place(relx=0.52,rely=0.695, relheight=0.05, relwidth=0.1)

	root.mainloop()

def search_page():
	root1 = Tk()
	root1.title("Welcome Back Learner!")
	canvas = tk.Canvas(root1, height=HEIGHT, width=WIDTH)
	canvas.pack()
	fontStyle = tkFont.Font(family="Berlin Sans FB", size=25)
	background_image = tk.PhotoImage(file='search_page.png')
	background_label = tk.Label(root1, image=background_image)
	background_label.place(relwidth=1, relheight=1)
	button1 = tk.Button(root1, text='BACK', bg='#a3def8', fg='#0c3b6a', font=fontStyle, command=lambda: login_page())
	button1.place(relheight=0.05, relwidth=0.1)

	frame = tk.Frame(root1, bg='#454545', bd=5)
	frame.place(relx=0.5, rely=0.3, relwidth=0.6, relheight=0.07, anchor='n')

	entry = tk.Entry(frame, font=100)
	entry.place(relx=0	,relwidth=1, relheight=1)


	button = tk.Button(root1, text = "LET'S GO", bg = '#a3def8', fg = '#0c3b6a', font= fontStyle, command = lambda : values())
	button.place(relx=0.45,rely=0.8, relheight=0.09, relwidth=0.12)

	CheckVar1 = IntVar()
	C1 = Checkbutton(root1, variable=CheckVar1, onvalue=1, offvalue=0, height=1, width=10).place(relx = 0.15, rely = 0.62)

	CheckVar2 = IntVar()
	C2 = Checkbutton(root1, variable=CheckVar2, onvalue=1, offvalue=0, height=1, width=10).place(relx=0.436, rely=0.62)

	CheckVar3 = IntVar()
	C3 = Checkbutton(root1, variable=CheckVar3, onvalue=1, offvalue=0, height=1, width=10).place(relx=0.775, rely=0.62)

	def values():
		if CheckVar1.get() == 1:
			print("You Searched For",entry.get(),"Basic")
			str1 = entry.get() + " Basic"
			root1.destroy()
			results(str1)

		elif CheckVar2.get() == 1:
			print("You Searched For",entry.get(),"Advanced")
			str2 = entry.get() + " Advanced"
			root1.destroy()
			results(str2)

		elif CheckVar3.get() == 1:
			print("You Searched For",entry.get(),"Certification")
			str3 = entry.get() + " Certification"
			root1.destroy()
			results(str3)
		else:
			tkinter.messagebox.showinfo("Error", "Please Make A Valid Selection")

	root1.mainloop()


def results(search_results):
	disp_text = "You searched for " + search_results
	root2 = Tk()
	root2.title("Search Results")
	canvas = tk.Canvas(root2, height=HEIGHT, width=WIDTH)
	canvas.pack()
	fontStyle = tkFont.Font(family="Segoe Print Bold", size=30)
	background_image = tk.PhotoImage(file='results.png')
	background_label = tk.Label(root2, image=background_image)
	background_label.place(relwidth=1, relheight=1)

	uname = Label(root2, text=disp_text, height=2, font=fontStyle, bg = '#0d2d44', fg = 'white').place(relx = 0.25,rely =0.058)
	root2.mainloop()
login_page()