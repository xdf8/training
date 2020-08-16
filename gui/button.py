import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('Python Gui')

#add a label
a_label = ttk.Label(win, text = 'A Label')
a_label.grid(column = 0, row = 0)

# button click event function
def click_me():
    action.configure(text = '** I have been clicked! **')
    a_label.configure(foreground = 'red')
    a_label.configure(text = 'A red label')

# create button and  add it to win
action = ttk.Button(win, text = 'Click me!', command = click_me)
action.grid(column=0, row=1)

win.mainloop()
