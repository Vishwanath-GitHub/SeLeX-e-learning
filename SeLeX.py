import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
import tkinter.messagebox
import os
import sys
from Vid_Player2 import *
from autosub import *
from Database import *
HEIGHT = 720
WIDTH = 1280

def close_everything():
    sys.exit()
def validate(uname, passwrd, root):
    value= checker(uname, passwrd)
    if value:
        root.destroy()
        search_page()

    elif not value:
        tkinter.messagebox.showinfo("Failed", "Invalid Creds")


def register():

    font = tkFont.Font(family="Times New Roman", size=10)
    window = Tk()
    window.title("Register Your Self Here")
    #wind.geometry('200x150 + 400 + 300')
    canvas = tk.Canvas(window, height=HEIGHT / 2, width=WIDTH / 2)
    canvas.pack()

    uname_label = Label(window, text="Enter Username :",font = font ).place(relx=0.06, rely=0.1)
    uname_entry = tk.Entry(window, font = 100)
    uname_entry.place(relx = 0.35, rely = 0.108, relwidth = 0.6, relheight = 0.07)

    password_label = Label(window, text="Enter Password :", font=font).place(relx=0.06, rely=0.3)
    password_entry = tk.Entry(window, font=100, show = '*')
    password_entry.place(relx=0.35, rely=0.308, relwidth=0.6, relheight=0.07)

    cnfpass_label = Label(window, text="Confirm Password :", font=font).place(relx=0.06, rely=0.5)
    cnfpass_entry = tk.Entry(window, font=100, show = '*')
    cnfpass_entry.place(relx=0.35, rely=0.508, relwidth=0.6, relheight=0.07)

    reg_button = tk.Button(window, text='REGISTER NOW!', bg='#a3def8', fg='#0c3b6a', font = font, command = lambda : valid_or_not(uname_entry.get(), password_entry.get(),cnfpass_entry.get()))
    reg_button.place(relx=0.33, rely=0.8, relheight=0.09, relwidth=0.35)


    def valid_or_not(uname, password , cnfpassword):
        if password == cnfpassword:
            value = sql_register(uname, password)
            if value:
                tkinter.messagebox.showinfo("SUCCESS", "Account Created Successfully")
                window.destroy()
            elif not value:
                tkinter.messagebox.showinfo("ERROR", "Username Already Exists!")

        else:
            tkinter.messagebox.showinfo("Error", "Passwords do not match!")

    window.mainloop()


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
    frame1.place(relx=0.34, rely=0.67, relwidth=0.25, relheight=0.05, anchor='n')
    uname = Label(frame1, text="Username").place(x=30, y=50)

    entry = tk.Entry(frame1, font=100)
    entry.place(relx=0, relwidth=1, relheight=1)

    frame2 = tk.Frame(root, bg='#3b5249', bd=5)
    frame2.place(relx=0.34, rely=0.752, relwidth=0.25, relheight=0.05, anchor='n')

    entry2 = tk.Entry(frame2, font=100, show="*")
    entry2.place(relx=0, relwidth=1, relheight=1)
    fontStyle = tkFont.Font(family="Berlin Sans FB", size=25)
    button = tk.Button(root, text='LOGIN', bg='#a3def8', fg='#0c3b6a', font=fontStyle,command=lambda: validate(entry.get(), entry2.get(), root))
    button.place(relx=0.52, rely=0.67, relheight=0.05, relwidth=0.1)
    register_button = tk.Button(root, text='REGISTER', bg='#a3def8', fg='#0c3b6a', font=fontStyle,command=lambda: register())
    register_button.place(relx=0.52, rely=0.752, relheight=0.05, relwidth=0.13)

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
    button1 = tk.Button(root1, text='LOG OUT', bg='#a3def8', fg='#0c3b6a', font=fontStyle, command=lambda: close_everything())
    button1.place(relheight=0.05, relwidth=0.1)

    frame = tk.Frame(root1, bg='#454545', bd=5)
    frame.place(relx=0.5, rely=0.3, relwidth=0.6, relheight=0.07, anchor='n')

    entry = tk.Entry(frame, font=100)
    entry.place(relx=0, relwidth=1, relheight=1)

    button = tk.Button(root1, text="LET'S GO", bg='#a3def8', fg='#0c3b6a', font=fontStyle, command=lambda: values())
    button.place(relx=0.45, rely=0.8, relheight=0.09, relwidth=0.12)

    CheckVar1 = IntVar()
    C1 = Checkbutton(root1, variable=CheckVar1, onvalue=1, offvalue=0, height=1, width=10).place(relx=0.15, rely=0.62)

    CheckVar2 = IntVar()
    C2 = Checkbutton(root1, variable=CheckVar2, onvalue=1, offvalue=0, height=1, width=10).place(relx=0.436, rely=0.62)

    CheckVar3 = IntVar()
    C3 = Checkbutton(root1, variable=CheckVar3, onvalue=1, offvalue=0, height=1, width=10).place(relx=0.775, rely=0.62)

    def values():
        if CheckVar1.get() == 1:
            print("You Searched For", entry.get(), "Basic")
            str1 = entry.get() + " Basic"
            root1.destroy()
            results(str1)

        elif CheckVar2.get() == 1:
            print("You Searched For", entry.get(), "Advanced")
            str2 = entry.get() + " Advanced"
            root1.destroy()
            results(str2)

        elif CheckVar3.get() == 1:
            print("You Searched For", entry.get(), "Certification")
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
    button1 = tk.Button(root2, text='LOG OUT', bg='#a3def8', fg='#0c3b6a', font=fontStyle, command=lambda: close_everything())
    button1.place(relheight=0.05, relwidth=0.1)
    def find_files(filename, search_path):
        result = []

        # Wlaking top-down from the root
        for root, dir, files in os.walk(search_path):
            if filename in files:
                result.append(os.path.join(root, filename))
        return result

    show = find_files(search_results + ".mp4", "C:\\Users\sarth\Desktop")
    uname = Label(root2, text=disp_text, height=2, font=fontStyle, bg='#0d2d44', fg='white').place(relx=0.25,rely=0.058)
    y = 0.3
    for file in show:
        file_string = file.lower()
        fil = Label(root2, text=file_string, font=fontStyle).place(relx=0.1, rely=y)
        play_button = tk.Button(root2, text="PLAY", bg='#a3def8', fg='#0c3b6a', font=fontStyle,command=lambda: my_Player(file_string))
        play_button.place(relx=0.8, rely=y + 0.2, relheight=0.09, relwidth=0.12)
        next_button = tk.Button(root2, text="NEXT", bg='#a3def8', fg='#0c3b6a', font=fontStyle,command=lambda: play_sub(file_string, root2))
        next_button.place(relx=0.9, rely=0, relheight=0.09, relwidth=0.12)
        y = y + 0.15
    root2.mainloop()


def play_sub(file_string, root2):
    root2.destroy()
    root3 = Tk()
    root3.title("Subtitles")
    canvas = tk.Canvas(root3, height=HEIGHT, width=WIDTH)
    canvas.pack()
    fontStyle = tkFont.Font(family="Segoe Print Bold", size=30)
    background_image = tk.PhotoImage(file='subtitles.png')
    background_label = tk.Label(root3, image=background_image)
    background_label.place(relwidth=1, relheight=1)
    button1 = tk.Button(root3, text='LOG OUT', bg='#a3def8', fg='#0c3b6a', font=fontStyle,command=lambda: close_everything())
    button1.place(relheight=0.05, relwidth=0.1)
    autosub(file_string)
    root3.mainloop()


login_page()
