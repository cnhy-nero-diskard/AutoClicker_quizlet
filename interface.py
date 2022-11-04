#just a simple interface using tkinter


from tkinter import font
import keyboard
import AUTOCLICC as tapow
import tkinter as ttk
from tkinter import *
import pyperclip

def into_box(frm, text,root):
    frm.insert('0.0', text)
    root.after(100)

def main():
    scr = Tk()
    scr.resizable(False,False)
    frm = ttk.Frame(background='white',
                    highlightbackground='red',
                    padx=10,
                    pady=10)
    frm = scr
    text = Text(scr, height=1,width=30,borderwidth=4)
    scrollbar = Scrollbar(scr, orient='vertical', command=text.yview)



    frm.grid()
    text['yscrollcommand'] = scrollbar.set
    scr.title("Holabels")
    butt = ttk.Button(frm, text = "Start", command= lambda: tapow.moveandclick(),fg="green")
    qt = ttk.Button(frm, text = "Quit",  command= scr.destroy,fg="red")
    #title = ttk.Label(frm,text="Welcome to Scansky's automator",font=('Helvetica',12))
    #title.grid(column=0,row=0,sticky=W)
    butt.config(height=2,width=4,font = ('Helvetica',11))
    qt.config(height=2,width=4,font = ('Helvetica',11))
    butt.grid(column=0,row=2, sticky=W)
    qt.grid(column=1,row=2, sticky=NW)

    text.grid(row=2, column=2, sticky=W,columnspan=1)
    scr.after(100,into_box(text, pyperclip.paste(), scr))
    #listbox.grid(row=4, column=0, sticky=EW)
    #scrollbar.grid(row=4, column=0, sticky=NS)

    scr.mainloop()
main()

