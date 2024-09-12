from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3


class productClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Team Third Axis")
        self.root.config(bg = "white")
        self.root.focus_force()
        #============================================

        product_Frame=Frame(self.root,bd=3,relief=RIDGE)



if __name__ == "__main__":
    root = Tk()
    obj = productClass(root)
    root.mainloop()        