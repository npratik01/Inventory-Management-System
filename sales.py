from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3


class salesClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Team Third Axis")
        self.root.config(bg = "white")
        self.root.focus_force()

        self.var_invoice=StringVar()
        #==== Title=======
        lbl_title=Label(self.root,text="View Customer Bills",font=("goudy old style",30),bg="#184a45",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)

        lbl_invoice=Label(self.root,text="Invoice No. ",font=("times new roman",15),bg="white").place(x=50,y=100)

        txt_invoice=Entry(self.root,textvariable=self.var_invoice,font=("times new roman",15),bg="lightyellow").place(x=160,y=100,width=180,height=28)

        btn_search=Button(self.root,text="Search",font=("times new roman",15,"bold"),bg="#2196f3",fg="white",cursor="hand2").place(x=360,y=100,width=120,height=28)
        btn_clear=Button(self.root,text="Clear",font=("times new roman",15,"bold"),bg="lightgrey",cursor="hand2").place(x=490,y=100,width=120,height=28)

        #===== Bill List======
        salesFrame=Frame(self.root,bd=3,relief=RIDGE)
        salesFrame.place(x=50,y=140,width=200,height=330)

        scrolly=Scrollbar(salesFrame,orient=VERTICAL)
        self.salesList=Listbox(salesFrame,font=("goudy old style",15 ),bg="white",yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.salesList.yview)
        self.salesList.pack(fill=BOTH,expand=1)

        #===== Bill Area======
        billFrame=Frame(self.root,bd=3,relief=RIDGE)
        billFrame.place(x=280,y=140,width=410,height=330)

        lbl_title2=Label(billFrame,text="Customer Bill Area",font=("goudy old style",20),bg="orange").pack(side=TOP,fill=X  )


        scrolly2=Scrollbar(billFrame,orient=VERTICAL)
        self.billArea=Text(billFrame,font=("goudy old style",15 ),bg="lightyellow",yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT,fill=Y)
        scrolly2.config(command=self.billArea.yview)
        self.billArea.pack(fill=BOTH,expand=1)

        #=====Image==========
        self.billPhoto = Image.open("Images/cat2.jpg")
        self.billPhoto = self.billPhoto.resize((450,300),Image.LANCZOS)
        self.billPhoto = ImageTk.PhotoImage(self.billPhoto)

        lbl_image=Label(self.root,image=self.billPhoto,bd=0)
        lbl_image.place(x=700,y=110)







if __name__ == "__main__":
    root = Tk()
    obj = salesClass(root)
    root.mainloop()        