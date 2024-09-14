from tkinter import*
from PIL import Image, ImageTk


class LoginSystem:
    def __init__(self, root):
        self.root=root
        self.root.title("Login System | Team Third Axis")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")

        #==== images ==============
        self.phone_img=ImageTk.PhotoImage(file="Images/phone.png")
        self.lbl_phone_image=Label(self.root,image=self.phone_img,bd=0).place(x=200,y=50)

        #===== Login Frame ===============
        loginFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        loginFrame.place(x=650,y=90,width=350,height=460)


        title=Label(loginFrame,text="Login System",font=("Elephant", 30, "bold"),bg="white").place(x=0,y=30,relwidth=1)

        lbl_user=Label(loginFrame,text="Username",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=100)
        txt_username=Entry(loginFrame,font=("times new roman",15),bg="#ECECEC").place(x=50,y=140,width=250)
    


root=Tk()
obj=LoginSystem(root)
root.mainloop()