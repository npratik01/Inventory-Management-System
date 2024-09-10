from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
class memberClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Team Third Axis")
        self.root.config(bg = "white")
        self.root.focus_force()
        #============================================
        #All variables =====
        self.var_mem_searchby = StringVar()
        self.var_mem_searchtxt = StringVar()

        self.var_mem_prn = StringVar()
        self.var_mem_gender = StringVar()
        self.var_mem_contact = StringVar()
        self.var_mem_name = StringVar()
        self.var_mem_dob = StringVar()
        self.var_mem_email = StringVar()
        self.var_mem_pass = StringVar()
        self.var_mem_usertype = StringVar()

        #==== Seaarch Frame ====
        SearchFrame = LabelFrame(self.root,text="Search Member",font=("goudy old style",12,"bold"),bd=2,bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)

        #==== Options ====
        cmb_search = ttk.Combobox(SearchFrame,textvariable=self.var_mem_searchby,values=("Select","Email","Name","PRN"),state="readonly",justify=CENTER,font=("gaudy old style",15))
        cmb_search.place(x=10,y=10,width=100)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_mem_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search = Button(SearchFrame,text="Search",font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=410,y=8,width=150,height=30)

        #===== Title =====
        title = Label(self.root,text="Member Details",font=("goudy old style",15),bg="#0f4d7d",fg="white",).place(x=50,y=100,width=1000)

        #====== Content =====
        #===== Row 1 =====
        lbl_memid = Label(self.root,text="Member ID",font=("goudy old style",15),bg="white").place(x=50,y=150)
        lbl_gender = Label(self.root,text="Gender",font=("goudy old style",15),bg="white").place(x=350,y=150)
        lbl_contact = Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=750,y=150)

        txt_memid = Entry(self.root,textvariable=self.var_mem_prn,font=("goudy old style",15),bg="lightyellow").place(x=150,y=150,width=100)
        cmb_gender = ttk.Combobox(self.root,textvariable=self.var_mem_gender,values=("Select","Male","Female","Other"),state="readonly",justify=CENTER,font=("gaudy old style",15))
        cmb_gender.place(x=500,y=150,width=100)
        cmb_gender.current(0)
        txt_contact = Entry(self.root,textvariable=self.var_mem_contact,font=("goudy old style",15),bg="lightyellow").place(x=850,y=150,width=100)

        #===== Row 2 =====
        lbl_name = Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=190)
        lbl_dob = Label(self.root,text="Date Of Birth",font=("goudy old style",15),bg="white").place(x=350,y=190)
        lbl_email = Label(self.root,text="Email",font=("goudy old style",15),bg="white").place(x=750,y=190)

        txt_name = Entry(self.root,textvariable=self.var_mem_name,font=("goudy old style",15),bg="lightyellow").place(x=150,y=190,width=180)
        txt_dob = Entry(self.root,textvariable=self.var_mem_dob,font=("goudy old style",15),bg="lightyellow").place(x=500,y=190,width=180)
        txt_email = Entry(self.root,textvariable=self.var_mem_email,font=("goudy old style",15),bg="lightyellow").place(x=850,y=190,width=180)

        #===== Row 2 =====
        lbl_password = Label(self.root,text="Password",font=("goudy old style",15),bg="white").place(x=50,y=230)
        lbl_utype = Label(self.root,text="User Type",font=("goudy old style",15),bg="white").place(x=350,y=230)

        txt_pass = Entry(self.root,textvariable=self.var_mem_pass,font=("goudy old style",15),bg="lightyellow").place(x=150,y=230,width=180)
        cmb_utype = ttk.Combobox(self.root,textvariable=self.var_mem_usertype,values=("Admin","Member"),state="readonly",justify=CENTER,font=("gaudy old style",15))
        cmb_utype.place(x=500,y=230,width=180)
        cmb_utype.current(0)


        #==== Buttons =====
        btn_add = Button(self.root,text="Save",font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=500,y=305,width=110,height=28)
        btn_update = Button(self.root,text="Update",font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=620,y=305,width=110,height=28)
        btn_delete = Button(self.root,text="Delete",font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=740,y=305,width=110,height=28)
        btn_clear = Button(self.root,text="Clear",font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=860,y=305,width=110,height=28)


        #==== Member Details =====

        mem_frame = Frame(self.root,bd=3,relief=RIDGE)
        mem_frame.place(x=0,y=350,relwidth=1,height=150)

        scrolly = Scrollbar(mem_frame,orient=VERTICAL)
        scrollx = Scrollbar(mem_frame,orient=HORIZONTAL)

        self.MemberTable=ttk.Treeview(mem_frame,columns=("memid","name","email","gender","contact","dob","pass","utype"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.MemberTable.xview)
        scrolly.config(command=self.MemberTable.yview)
        self.MemberTable.heading("memid",text="Member ID")
        self.MemberTable.heading("name",text="Name")
        self.MemberTable.heading("email",text="Email")
        self.MemberTable.heading("gender",text="Gender")
        self.MemberTable.heading("contact",text="Contact")
        self.MemberTable.heading("dob",text="DOB")
        self.MemberTable.heading("pass",text="Password")
        self.MemberTable.heading("utype",text="User Type")

        self.MemberTable["show"]="headings"

        self.MemberTable.column("memid",width=90)
        self.MemberTable.column("name",width=100)
        self.MemberTable.column("email",width=100)
        self.MemberTable.column("gender",width=100)
        self.MemberTable.column("contact",width=100)
        self.MemberTable.column("dob",width=100)
        self.MemberTable.column("pass",width=100)
        self.MemberTable.column("utype",width=100)

        self.MemberTable.pack(fill=BOTH,expand=1)





if __name__ == "__main__":
    root = Tk()
    obj = memberClass(root)
    root.mainloop()