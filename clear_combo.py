from msilib.schema import ComboBox
from tkinter.ttk import Combobox
import customtkinter
from tkinter import *
from tkinter import ttk

customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue")
root = customtkinter.CTk()
size_label = ttk.Label(root)

def size_selected(event):
    global size_label
    size_label.destroy()
    size_label = ttk.Label(root, text=size_combobox.get())
    size_label.pack()
    

size_combobox = ttk.Combobox(root, values=["1","2","3"])
size_combobox.bind("<<ComboboxSelected>>", size_selected)
size_combobox.pack()


root.mainloop()