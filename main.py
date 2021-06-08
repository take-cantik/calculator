from tkinter import *
from tkmacosx import *
from functools import partial

import my_calc as cl
import my_button as bt

w = 90
h = 50

button1 = Button(cl.win, text="1", font=("", "15"), width=w, height=h, command=partial(bt.num_btn, 1))
button2 = Button(cl.win, text="2", font=("", "15"), width=w, height=h, command=partial(bt.num_btn, 2))
button3 = Button(cl.win, text="3", font=("", "15"), width=w, height=h, command=partial(bt.num_btn, 3))
button4 = Button(cl.win, text="4", font=("", "15"), width=w, height=h, command=partial(bt.num_btn, 4))
button5 = Button(cl.win, text="5", font=("", "15"), width=w, height=h, command=partial(bt.num_btn, 5))
button6 = Button(cl.win, text="6", font=("", "15"), width=w, height=h, command=partial(bt.num_btn, 6))
button7 = Button(cl.win, text="7", font=("", "15"), width=w, height=h, command=partial(bt.num_btn, 7))
button8 = Button(cl.win, text="8", font=("", "15"), width=w, height=h, command=partial(bt.num_btn, 8))
button9 = Button(cl.win, text="9", font=("", "15"), width=w, height=h, command=partial(bt.num_btn, 9))
button0 = Button(cl.win, text="0", font=("", "15"), width=w, height=h, command=partial(bt.num_btn, 0))

buttonS = Button(cl.win, text="+", font=("", "15"), width=w, height=h, command=partial(bt.on_ope, "+"))
buttonD = Button(cl.win, text="-", font=("", "15"), width=w, height=h, command=partial(bt.on_ope, "-"))
buttonP = Button(cl.win, text="×", font=("", "15"), width=w, height=h, command=partial(bt.on_ope, "*"))
buttonQ = Button(cl.win, text="÷", font=("", "15"), width=w, height=h, command=partial(bt.on_ope, "/"))
buttonE = Button(cl.win, text="=", font=("", "15"), width=(2*w)+1, height=h, command=partial(bt.on_ope, "="))

buttonAC = Button(cl.win, text="AC", font=("", "15"), width=w, height=h, command=bt.on_ac)
buttonC = Button(cl.win, text="C", font=("", "15"), width=w, height=h, command=bt.on_clear)

buttonT10 = Button(cl.win, text="TAX(10%)", font=("", "15"), width=w, height=h, command=partial(bt.on_tax, 10))
buttonT8 = Button(cl.win, text="TAX(8%)", font=("", "15"), width=w, height=h, command=partial(bt.on_tax, 8))

x1 = 3
x2 = 115
x3 = 227
x4 = 339
y1 = 70
y2 = 168
y3 = 265
y4 = 362
y5 = 459

cl.label.place(x=2, y=1)

button7.place(x=x1, y=y1)
button8.place(x=x2, y=y1)
button9.place(x=x3, y=y1)
buttonS.place(x=x4, y=y1)

button4.place(x=x1, y=y2)
button5.place(x=x2, y=y2)
button6.place(x=x3, y=y2)
buttonD.place(x=x4, y=y2)

button1.place(x=x1, y=y3)
button2.place(x=x2, y=y3)
button3.place(x=x3, y=y3)
buttonP.place(x=x4, y=y3)

button0.place(x=x1, y=y4)
buttonC.place(x=x2, y=y4)
buttonAC.place(x=x3, y=y4)
buttonQ.place(x=x4, y=y4)

buttonT10.place(x=x1, y=y5)
buttonT8.place(x=x2, y=y5)
buttonE.place(x=x3, y=y5)

cl.win.mainloop()
