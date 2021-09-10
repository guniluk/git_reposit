from tkinter import *
from tkinter.colorchooser import askcolor

DEFAULT_PEN_SIZE = 1.0
DEFAULT_COLOR = "black"

mode = "pen"
old_x = None
old_y = None
mycolor = DEFAULT_COLOR
erase_on = False

def use_pen():
    global mode
    mode = "pen"
def use_brush():
    global mode
    mode = "brush"
def choose_color():
    global mycolor
    mycolor = askcolor(color=mycolor)[1]
def use_eraser():
    global mode
    mode = "erase"

def paint(event):
    global var, earse_on, mode, old_x, old_y
    fill_color = "white" if mode == "erase" else mycolor
    if old_x and old_y:
        canvas.create_line(old_x, old_y, event.x, event.y,\
            capstyle = ROUND, width = var.get(), fill=fill_color)
    old_x = event.x
    old_y = event.y
    
def reset(event):
    global old_x, old_y
    old_x, old_y = None, None

def clear_all():
    global canvas
    canvas.delete('all')

window = Tk()
var = DoubleVar()

penButton = Button(window, text='펜', command=use_pen)
penButton.grid(row=0, column=0, sticky=W+E)
brushButton = Button(window, text='브러쉬', command=use_brush)
brushButton.grid(row=0, column=1, sticky=W+E)
colorButton = Button(window, text='색상선택', command=choose_color)
colorButton.grid(row=0, column=2, sticky=W+E)
eraseButton = Button(window, text='지우개', command=use_eraser)
eraseButton.grid(row=0, column=3, sticky=W+E)
clearButton = Button(window, text='모두삭제', command=clear_all)
clearButton.grid(row=0, column=4, sticky=W+E)

scale=Scale(window, variable=var, orient=VERTICAL)
scale.grid(row=1, column=5, sticky=N+S)

canvas = Canvas(window, bg='white', width=600, height=400)
canvas.grid(row=1, columnspan=5)
canvas.bind('<B1-Motion>', paint)
canvas.bind('<ButtonRelease-1>', reset)

window.mainloop()