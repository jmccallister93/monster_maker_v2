from glob import glob
from msilib.schema import ComboBox
from tkinter.ttk import Combobox
import customtkinter
from tkinter import *
from tkinter import ttk
import random

customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue")
root = customtkinter.CTk()


#Funciton to add size
def add_size():
    #Delcare variable for choice 
    size_choice = StringVar()
    #get choice based on combobox
    size_choice = size_combobox.get()
    #Option for random variable
    random_size = random.choice(size_options_label)
    #If statement to set label display 
    if size_choice == "Random":
        display_size['text'] = random_size
    else:
        display_size['text'] = size_choice
    
#Create two lists 1 for choices on combobox 2 for label
size_options_combobox = ["Random", "Tiny", "Small"]
size_options_label = ["Tiny", "Small"]
#create combobox for size options
size_combobox = Combobox(root, values=size_options_combobox)
size_combobox.grid(row=0, column= 0)
size_combobox.set("Random")
#Display label and update text with choice 
display_size = Label(root,text="SIZE")
display_size.grid(row=0, column=2)
#Create button to add a size
add_size_btn = Button(root, text="Add Size", command=add_size)
add_size_btn.grid(row=0, column=1)


root.mainloop()