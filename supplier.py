from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3

class supplierClass:
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

        self.var_sup_invoice = StringVar()
        self.var_mem_name = StringVar()
        self.var_mem_contact = StringVar()
        self.var_mem_email = StringVar()

        #==== Seaarch Frame ====
        SearchFrame = LabelFrame(self.root,text="Search Member",font=("goudy old style",12,"bold"),bd=2,bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)

        #==== Options ====
        cmb_search = ttk.Combobox(SearchFrame,textvariable=self.var_mem_searchby,values=("Select","Email","Name","PRN"),state="readonly",justify=CENTER,font=("gaudy old style",15))
        cmb_search.place(x=10,y=10,width=100)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_mem_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search = Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=410,y=8,width=150,height=30)

        #===== Title =====
        title = Label(self.root,text="Supplier Details",font=("goudy old style",15),bg="#0f4d7d",fg="white",).place(x=50,y=100,width=1000)

        #====== Content =====
        #===== Row 1 =====
        lbl_supplierInvoice = Label(self.root,text="Invoice No.",font=("goudy old style",15),bg="white").place(x=50,y=150)
        txt_lbl_supplier_invoice = Entry(self.root,textvariable=self.var_sup_invoice,font=("goudy old style",15),bg="lightyellow").place(x=150,y=150,width=100)
        
        #===== Row 2 =====
        lbl_name = Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=190)
        txt_name = Entry(self.root,textvariable=self.var_mem_name,font=("goudy old style",15),bg="lightyellow").place(x=150,y=190,width=180)

        #===== Row 3 =====
        lbl_contact = Label(self.root,text="Contact",font=("goudy old style",15),bg="lightyellow").place(x=850,y=190,width=180)
        txt_contact = Entry(self.root,textvariable=self.var_mem_contact,font=("goudy old style",15),bg="lightyellow").place(x=850,y=190,width=180)

        #==== Row 4 ==========
        lbl_desc= Label(self.root,text="Description",font=("goudy old style",15),bg="white").pack()
        self.txt_desc=Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.txt_desc.place(x=150,y=270,width=300,height=60)

        #==== Buttons =====
        btn_add = Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=500,y=305,width=110,height=28)
        btn_update = Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=620,y=305,width=110,height=28)
        btn_delete = Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=740,y=305,width=110,height=28)
        btn_clear = Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=860,y=305,width=110,height=28)


        #==== Member Details =====

        mem_frame = Frame(self.root,bd=3,relief=RIDGE)
        mem_frame.place(x=0,y=350,relwidth=1,height=150)

        scrolly = Scrollbar(mem_frame,orient=VERTICAL)
        scrollx = Scrollbar(mem_frame,orient=HORIZONTAL)

        self.supplierTable=ttk.Treeview(mem_frame,columns=("invoice","name","contact","email","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)
        self.supplierTable.heading("invoice",text="Member ID")
        self.supplierTable.heading("name",text="Name")
        self.supplierTable.heading("contact",text="Email")
        self.supplierTable.heading("email",text="Gender")
        self.supplierTable.heading("desc",text="Contact")
      
        self.supplierTable["show"]="headings"

        self.supplierTable.column("invoice",width=90)
        self.supplierTable.column("name",width=100)
        self.supplierTable.column("contact",width=100)
        self.supplierTable.column("email",width=100)
        self.supplierTable.column("desc",width=100)
        self.supplierTable.pack(fill=BOTH,expand=1)
        self.supplierTable.bind("<ButtonRelease-1>",self.get_data)


#=====================================================================

    def add(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice Must be required",parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "This Invoice Number already assigned , try different",parent=self.root)
                else:
                    cur.execute("Insert into supplier (invoice,name,contact,email,desc) values(?,?,?,?,?)",(
                                self.var_sup_invoice.get(),
                                self.var_mem_name.get(),
                                self.var_mem_contact.get(),
                                self.var_mem_email.get(),
                                self.var_mem_desc.get('1.0',END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Added Successfully",parent=self.root)
                    self.show()

                
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            

    def show(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from member")
            rows=cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
                self.supplierTable.insert('',END,values=row)


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            

    def get_data(self,ev):
        f=self.supplierTable.focus()
        content=(self.supplierTable.item(f))
        row=content['values']
        # print(row)
        self.var_sup_invoice.set(row[0])
        self.var_mem_name.set(row[1])
        self.var_mem_email.set(row[2])
        self.var_mem_gender.set(row[3])
        self.var_mem_contact.set(row[4])
        self.var_mem_dob.set(row[5])
        self.var_mem_pass.set(row[6])
        self.var_mem_usertype.set(row[7])


#======== UPDATE DATA =======================================================================================

    def update(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Member ID Must be required",parent=self.root)
            else:
                cur.execute("SELECT * FROM member WHERE memid=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Member ID",parent=self.root)
                else:
                    cur.execute("Update member set name=?,email=?,gender=?,contact=?,dob=?,pass=?,utype=? where memid=?",(
                
                        self.var_mem_name.get(),
                        self.var_mem_email.get(),
                        self.var_mem_gender.get(),
                        self.var_mem_contact.get(),
                        self.var_mem_dob.get(),
                        self.var_mem_pass.get(),
                        self.var_mem_usertype.get(),
                        self.var_sup_invoice.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Member Updated Successfully",parent=self.root)
                    self.show()

                
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
#============ DELETE Button =========================================================================

    def delete(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Member ID Must be required",parent=self.root)
            else:
                cur.execute("SELECT * FROM member WHERE memid=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Member ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm", "Do you really want to delete ?",parent=self.root)
                    if op == True:
                        cur.execute("delete from member where memid=? ",(self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Member Deleted Successfully",parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

#======= Clear Button ================================================================================================

    def clear(self):
        self.var_sup_invoice.set(r"")
        self.var_mem_name.set("")
        self.var_mem_email.set("")
        self.var_mem_gender.set("Select")
        self.var_mem_contact.set("")
        self.var_mem_dob.set("")
        self.var_mem_pass.set("")
        self.var_mem_usertype.set("Admin")
        self.var_mem_searchtxt.set("")
        self.var_mem_searchby.set("Select")

        self.show()

#======= Search Button ===============================
    def search(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_mem_searchby.get()=="Select":
                messagebox.showerror("Erro","Select Search By Option",parent=self.root)
            elif self.var_mem_searchtxt.get()=="":
                messagebox.showerror("Error","Search input should be required ",parent=self.root)
                cur.execute("select * from member")
            else:
                cur.execute("Select * from member where "+self.var_mem_searchby.get()+" LIKE '%"+self.var_mem_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!= 0:
                    self.supplierTable.delete(*self.supplierTable.get_children())
                    for row in rows:
                        self.supplierTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record Found",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            


if __name__ == "__main__":
    root = Tk()
    obj = supplierClass(root)
    root.mainloop()