import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
import tkinter.messagebox
import requests

HEIGHT = 720
WIDTH = 1280

def test_function(entry):
	print("This is the entry:", entry)

def validate(uname, passwrd):
	creds_dict = {"sarthak":"sarthak", "kunal":"kunal", "vishu": "vishu"}
	if uname in creds_dict and creds_dict[uname] == passwrd:
		root.title("Welcome Back Learner!")
		canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
		canvas.pack()

		background_image = tk.PhotoImage(file='final.png')
		background_label = tk.Label(root, image=background_image)
		background_label.place(relwidth=1, relheight=1)
		root.mainloop()

	elif uname  not in creds_dict or creds_dict[uname] != passwrd:
		tkinter.messagebox.showinfo("Failed", "Invalid Creds")

root =Tk()
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
button = tk.Button(root, text = 'LOGIN', bg = '#a3def8', fg = '#0c3b6a', font= fontStyle, command=lambda : validate(entry.get(), entry2.get()))
button.place(relx=0.52,rely=0.695, relheight=0.05, relwidth=0.1)

root.mainloop()
