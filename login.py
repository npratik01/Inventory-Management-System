from tkinter import*
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3


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

        lbl_user=Label(loginFrame,text="Member ID",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=100)
        self.username=StringVar()
        self.password=StringVar()
        txt_username=Entry(loginFrame,textvariable=self.username,font=("times new roman",15),bg="#ECECEC").place(x=50,y=140,width=250)

        lbl_pass=Label(loginFrame,text="Paassword",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=200)
        txt_pass=Entry(loginFrame,textvariable=self.password,show="*",font=("times new roman",15),bg="#ECECEC").place(x=50,y=240,width=250)

        btn_login=Button(loginFrame,command=self.login,text="Log In",font=("Arial Rounded MT Bold",15),bg="#00B0F0",activebackground="#00B0F0",fg="white",activeforeground="white",cursor="hand2").place(x=50,y=300,width=250,height=35)

        hr=Label(loginFrame,bg="lightgrey").place(x=50,y=370,width=250,height=2)
        or_=Label(loginFrame,text="OR",bg="white",fg="lightgrey",font=("times new roman",15, "bold")).place(x=155,y=355)

        btn_forget=Button(loginFrame,text="Forget Password ?",font=("times new roman",13),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E").place(x=100,y=390)

        #=====Frame2======
        registerFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        registerFrame.place(x=650,y=570,width=350,height=60)

        lbl_reg=Label(registerFrame,text="Team Third Axis | Beyond The Horizon",font=("times new roman",13),bg="white").place(x=40,y=18)
        
        #====Animation Images====== 
        self.im1=ImageTk.PhotoImage(file="Images/im1.png")
        self.im2=ImageTk.PhotoImage(file="Images/im2.png")
        self.im3=ImageTk.PhotoImage(file="Images/im3.png")

        self.lbl_change_image=Label(self.root,bg="white")
        self.lbl_change_image.place(x=367,y=153,width=240,height=428)

        self.animate()


    def animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000,self.animate)


    def login(self):
        if self.username.get()=="" or self.password.get()=="":
            messagebox.showerror("Erro","All Fields are required")
        elif self.username.get()!="Pratik" or self.password.get()!="123456":
            messagebox.showerror("Erro","Invalid Username or Password \n Try again with correct credentials")
        else:
            messagebox.showinfo("Information",f"Welcome :{self.username.get()}\n Your Password : {self.password.get()}")



root=Tk()
obj=LoginSystem(root)
root.mainloop()