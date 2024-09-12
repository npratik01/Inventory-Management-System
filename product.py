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

        product_Frame=Frame(self.root,bd=2,relief=RIDGE)
        product_Frame.place(x=10,y=10,width=450,height=480)

        #=======title=======
        title = Label(product_Frame,text="Product Details",font=("goudy old style",20),bg="#0f4d7d",fg="white",).pack(side=TOP,fill=X)

        lbl_category = Label(product_Frame,text="Category",font=("goudy old style",20),bg="white").place(x=30,y=60)
        lbl_category = Label(product_Frame,text="Category",font=("goudy old style",20),bg="white").place(x=30,y=60)
        lbl_category = Label(product_Frame,text="Category",font=("goudy old style",20),bg="white").place(x=30,y=60)
        lbl_category = Label(product_Frame,text="Category",font=("goudy old style",20),bg="white").place(x=30,y=60)
        lbl_category = Label(product_Frame,text="Category",font=("goudy old style",20),bg="white").place(x=30,y=60)
        lbl_category = Label(product_Frame,text="Category",font=("goudy old style",20),bg="white").place(x=30,y=60)
        lbl_category = Label(product_Frame,text="Category",font=("goudy old style",20),bg="white").place(x=30,y=60)
        lbl_category = Label(product_Frame,text="Category",font=("goudy old style",20),bg="white").place(x=30,y=60)

if __name__ == "__main__":
    root = Tk()
    obj = productClass(root)
    root.mainloop()        