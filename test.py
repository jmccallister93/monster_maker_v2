from tkinter import *
import customtkinter

def main():
    root = Tk()
    window1 = Window(root, "Hi", "400x400")
    return None


class Window:
    n = 0

    def __init__(self, root, title, geometry) -> None:
        self.root = root
        self.root.title(title)
        self.root.geometry(geometry)
        
        self.root.mainloop()

main()