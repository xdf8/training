import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('Python Gui')

# button click event function
def click_me():
    action.configure(text = 'Hello ' + name.get())

# add label
ttk.Label(win, text = 'Enter your name:').grid(column = 0, row = 0)

# adding a Textbox entry widget
name = tk.StringVar()
name_entered = ttk.Entry(win, width = 12, textvariable = name)
name_entered.grid(column=0, row=1)

# Adding a button
action = ttk.Button(win, text = 'Click me!', command = click_me)
action.grid(column=1, row=1)

win.mainloop()
