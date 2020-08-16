import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('Python Gui')

#add a label
a_label = ttk.Label(win, text = 'A Label')
a_label.grid(column = 0, row = 0)

win.mainloop()
