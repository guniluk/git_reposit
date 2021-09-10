# Hex Color code
from tkinter import *
from tkinter import colorchooser

def click():
    color = colorchooser.askcolor()
    hexa_color = color[1]
    window.config(bg=hexa_color)
    label.config(text=hexa_color)

window = Tk()
window.geometry("420x300")

button = Button(window, text='Select color', command = click,
                width=30, height=2)
button.pack(padx=30, pady=30)

label = Label(window, text = 'Hexa color code', 
              width=30, height=3, 
              font =('arial', 30)
              )
label.pack(padx=30, pady=30)

window.mainloop()