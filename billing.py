from tkinter import*
from PIL import Image, ImageTk

class BilliClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | Team Third Axis")
        self.root.config(bg = "white")

        #== title ==
        # self.icon_title = PhotoImage(file="")
        self.icon_title = Image.open("Images/thirdaxislogo1.png")
        self.icon_title = self.icon_title.resize((70,70),Image.LANCZOS)
        self.icon_title = ImageTk.PhotoImage(self.icon_title)
        title = Label(self.root, text="Inventory Management System",image=self.icon_title,compound=LEFT, font=("times new roman", 40, "bold"),bg="red",fg="white",anchor="w", padx=20).place(x = 0, y = 0, relwidth=1, height= 70)

        


        #== button_logout ==
        btn_logout = Button(self.root, text="Logout", font=("times new roman", 15, "bold"), bg = "white",cursor="hand2").place(x=1350, y=10, height=50, width=150)

        # == Clock == 
        self.lbl_clock = Label(self.root, text="Welcome to Inventory Management System \t\t Date : DD-MM-YYYY \t\t Time : HH:MM:SS ", font=("times new roman", 15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x = 0, y = 70, relwidth=1, height= 30)

#==========Product Frame =================================================================================================================================================================================

        ProductFrame1 = Frame(self.root,bd=4,relief=RIDGE,bg="white")
        ProductFrame1.place(x=10,y=110,width=410,height=550)

        pTitle=Label(ProductFrame1,text="All Products",font=("goudy old style",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)

if __name__ == "__main__":
    root = Tk()
    obj = BilliClass(root)
    root.mainloop()