
from tkinter import *
def show(search_results, root):
    root.fileName = "converted_" + search_results + ".en-us.srt"
    root.title(root.fileName)                                        # put filename into title bar
    text1 = open(root.fileName).read()
    T = Text(root)
    T.pack()                                                         # pack that textbox into the root window
    T.insert(END,text1)                                              #insert all the text up to just after the last charin:   text1
    T.place(relx = 0.2, rely = 0.3, relwidth = 0.6)
    root.mainloop()