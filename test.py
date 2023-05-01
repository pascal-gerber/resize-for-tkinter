import tkResizer
from tkinter import *


window = Tk()

text = Label(window, text=tkResizer.adapt(10), width = tkResizer.adapt(10), height = tkResizer.adapt(5))
text.grid()

window.mainloop()
