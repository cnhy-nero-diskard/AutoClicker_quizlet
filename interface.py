from tkinter import font
import keyboard
import AUTOCLICC as tapow
import tkinter as ttk
from tkinter import *

def main():
    scr = Tk()
    frm = ttk.Frame(background='grey',
                    highlightbackground='red',
                    padx=10,
                    pady=10)
    frm.grid()
    scr.title("Holabels")
    butt = ttk.Button(frm, text = "Start", command= lambda: tapow.moveandclick(),fg="green")
    quit = ttk.Button(frm, text = "Quit",  command= scr.destroy,fg="red")
    title = ttk.Label(frm,text="Welcome to Scansky's automator",bg='grey',font=('Helvetica',14))
    title.grid(column=0,row=0)
    butt.config(height=2,width=4,font = ('Helvetica',18),activebackground='#f4f4ea')
    quit.config(height=2,width=4,font = ('Helvetica',18))
    butt.grid(column=1,row=3)
    quit.grid(column=4,row=3)
    scr.mainloop()
main()

