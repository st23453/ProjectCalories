import tkinter as tk
from tkinter import ttk

def convert():
    print(entry_int.get())

# window
window = tk.Tk()
window.title('Demo')
window.geometry('300x150')

#title
title_label = ttk.Label(master = window, text = 'WELCOME TO CALORIE BURNER', font = 'Helvetica 24 bold')
title_label.pack()

# input field
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
button = ttk.Button(master = input_frame, text = 'Sign in', command = convert)
entry.pack(side = 'left', padx = 10)
button.pack(side = 'left')
input_frame.pack(pady = 10)

#output
output_label = tk.StringVar()
output_label = ttk.Label(
    master = window,
    text = 'Output',
    font = 'Calibri 24')
output_label.pack(pady = 5)

# run
window.mainloop()