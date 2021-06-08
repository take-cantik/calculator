from tkinter import *
from tkmacosx import *
# from on_btn import *
import my_button
from functools import partial

win = Tk()
win.title("Calculator")
win.configure(bg="#000000")
win.geometry('432x512')

label = Label(win, text="0", font=("", "15"), width=42, height=3, bg="#FFFFFF")

