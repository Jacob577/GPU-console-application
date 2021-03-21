import tkinter
from tkinter import messagebox

# This code is to hide the main tkinter window
root = tkinter.Tk()
root.withdraw()

# Message Box
messagebox.showinfo("Title", "This is a url")