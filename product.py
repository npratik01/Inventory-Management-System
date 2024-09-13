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
        self.var_cat=StringVar()
        self.var_invoice_no=StringVar()
        self.var_invoice_date=StringVar()
        self.var_price_item=StringVar()
        self.var_inovice_amount=StringVar()
        self.var_supp_name=StringVar()
        self.var_mo_no=StringVar()
        self.var_email_vendor=StringVar()
        self.var_received_std_name=StringVar()
        self.var_received_mo_no=StringVar()
        self.var_curr_posi=StringVar()
        self.var_curr_mo_no=StringVar()

        self.var_mem_searchby = StringVar()
        self.var_mem_searchtxt = StringVar()


        product_Frame=Frame(self.root,bd=5,relief=RIDGE)
        product_Frame.place(x=10,y=10,width=650,height=800)

        #=======title=======
        title = Label(product_Frame,text="Manage Product Details",font=("goudy old style",20),bg="#0f4d7d",fg="white",).pack(side=TOP,fill=X)

        lbl_product_name = Label(product_Frame,text="Product Name",font=("goudy old style",20),bg="white").place(x=30,y=60)
        lbl_Invoice_number = Label(product_Frame,text="Invoice number",font=("goudy old style",20),bg="white").place(x=30,y=110)
        lbl_Invoice_date = Label(product_Frame,text="Invoice date",font=("goudy old style",20),bg="white").place(x=30,y=160)
        lbl_Price_of_the_item= Label(product_Frame,text="Price of the item",font=("goudy old style",20),bg="white").place(x=30,y=210)
        lbl_Invoice_Amount= Label(product_Frame,text="Total Invoice Amount",font=("goudy old style",20),bg="white").place(x=30,y=260)
        lbl_supplier_name = Label(product_Frame,text="Supplier Name",font=("goudy old style",20),bg="white").place(x=30,y=310)
        lbl_mobile_number = Label(product_Frame,text="Mobile Number of vendor",font=("goudy old style",20),bg="white").place(x=30,y=360)
        lbl_email_vendor= Label(product_Frame,text="Email of Vendor",font=("goudy old style",20),bg="white").place(x=30,y=410)
        lbl_received_by_student_name = Label(product_Frame,text="Received by student name",font=("goudy old style",20),bg="white").place(x=30,y=460)
        lbl_received_mo_no = Label(product_Frame,text="Received by student MO NUMBER",font=("goudy old style",20),bg="white").place(x=30,y=510)
        lbl_curr_posi_name = Label(product_Frame,text="Currently Position",font=("goudy old style",20),bg="white").place(x=30,y=560)
        lbl_curr_posi_no = Label(product_Frame,text="Currently Number",font=("goudy old style",20),bg="white").place(x=30,y=610)

    

        #txt_category =Label(product_Frame,text="Category",font=("goudy old style",20),bg="white").place(x=30,y=60)

        #==== Column2 ====
        # cmb_cat = ttk.Combobox(product_Frame,textvariable=self.var_cat,values=("Select"),state="readonly",justify=CENTER,font=("gaudy old style",15))
        # cmb_cat.place(x=300,y=60,width=200)
        # cmb_cat.current(0)

        # cmb_sup = ttk.Combobox(product_Frame,textvariable=self.var_invoice_no,values=("Select"),state="readonly",justify=CENTER,font=("gaudy old style",15))
        # cmb_sup.place(x=300,y=110,width=200)
        # cmb_sup.current(0)

        txt_name = Entry(product_Frame,textvariable=self.var_cat,font=("gaudy old style",15),bg='lightyellow').place(x=300,y=60,width=200)
        txt_name = Entry(product_Frame,textvariable=self.var_invoice_no,font=("gaudy old style",15),bg='lightyellow').place(x=300,y=110,width=200)
        txt_name = Entry(product_Frame,textvariable=self.var_invoice_date,font=("gaudy old style",15),bg='lightyellow').place(x=300,y=160,width=200)
        txt_name = Entry(product_Frame,textvariable=self.var_price_item,font=("gaudy old style",15),bg='lightyellow').place(x=300,y=210,width=200)
        txt_name = Entry(product_Frame,textvariable=self.var_inovice_amount,font=("gaudy old style",15),bg='lightyellow').place(x=300,y=260,width=200)
        txt_name = Entry(product_Frame,textvariable=self.var_supp_name,font=("gaudy old style",15),bg='lightyellow').place(x=300,y=310,width=200)
        txt_name = Entry(product_Frame,textvariable=self.var_mo_no,font=("gaudy old style",15),bg='lightyellow').place(x=300,y=360,width=200)
        txt_name = Entry(product_Frame,textvariable=self.var_email_vendor,font=("gaudy old style",15),bg='lightyellow').place(x=300,y=410,width=200)
        txt_name = Entry(product_Frame,textvariable=self.var_received_std_name,font=("gaudy old style",15),bg='lightyellow').place(x=300,y=460,width=200)
        txt_name = Entry(product_Frame,textvariable=self.var_received_mo_no,font=("gaudy old style",15),bg='lightyellow').place(x=300,y=510,width=200)
        txt_name = Entry(product_Frame,textvariable=self.var_curr_posi,font=("gaudy old style",15),bg='lightyellow').place(x=300,y=560,width=200)
        txt_name = Entry(product_Frame,textvariable=self.var_curr_mo_no,font=("gaudy old style",15),bg='lightyellow').place(x=300,y=610,width=200)

         #==== Buttons =====
        btn_add = Button(product_Frame,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=10,y=700,width=100,height=40)
        btn_update = Button(product_Frame,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=120,y=700,width=100,height=40)
        btn_delete = Button(product_Frame,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=230,y=700,width=100,height=40)
        btn_clear = Button(product_Frame,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=330,y=700,width=100,height=40)

        #==== Seaarch Frame ====
        SearchFrame = LabelFrame(self.root,text="Search Member",font=("goudy old style",12,"bold"),bd=2,bg="white")
        SearchFrame.place(x=680,y=30,width=700,height=80)

        #==== Options ====
        cmb_search = ttk.Combobox(SearchFrame,textvariable=self.var_mem_searchby,values=("Select","Invoice_no","Name"),state="readonly",justify=CENTER,font=("gaudy old style",15))
        cmb_search.place(x=20,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_mem_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=220,y=10,width=280)
        btn_search = Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=530,y=8,width=150,height=30)



        #==== Product Details =====

        p_frame = Frame(self.root,bd=3,relief=RIDGE)
        p_frame.place(x=680,y=100,width=700,height=390)

        scrolly = Scrollbar(p_frame,orient=VERTICAL)
        scrollx = Scrollbar(p_frame,orient=HORIZONTAL)
        
        self.product_tabel=ttk.Treeview(p_frame,columns=("Product Name","Invoice number","Invoice date","Price",
    "Total Invoice Amount","Supplier Name","Vendor MO NO","Email of vendor","R Student Name","R Std Mo No",
    "Current position","current Mo no"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_tabel.xview)
        scrolly.config(command=self.product_tabel.yview)
        self.product_tabel.heading("Product Name",text="Member ID")
        self.product_tabel.heading("Invoice number",text="Name")
        self.product_tabel.heading("Invoice date",text="Email")
        self.product_tabel.heading("Price",text="Gender")
        self.product_tabel.heading("Total Invoice Amount",text="Contact")
        self.product_tabel.heading("Supplier Name",text="DOB")
        self.product_tabel.heading("Vendor MO NO",text="Password")
        self.product_tabel.heading("Email of vendor",text="User Type")
        self.product_tabel.heading("R Student Name",text="User Type")
        self.product_tabel.heading("R Std Mo NoE",text="User Type")
        self.product_tabel.heading("Current positionE",text="User Type")
        self.product_tabel.heading("Ecurrent Mo no",text="User Type")

        self.product_tabel["show"]="headings"

        self.product_tabel.column("memid",width=90)
        self.product_tabel.column("name",width=100)
        self.product_tabel.column("email",width=100)
        self.product_tabel.column("gender",width=100)
        self.product_tabel.column("contact",width=100)
        self.product_tabel.column("dob",width=100)
        self.product_tabel.column("pass",width=100)
        self.product_tabel.column("utype",width=100)
        self.product_tabel.pack(fill=BOTH,expand=1)
        self.product_tabel.bind("<ButtonRelease-1>",self.get_data)

        self.show()


    def add(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_mem_prn.get()=="":
                messagebox.showerror("Error","Member ID Must be required",parent=self.root)
            else:
                cur.execute("SELECT * FROM member WHERE memid=?",(self.var_mem_prn.get(),))
                row=cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "This Member ID already assigned , try different",parent=self.root)
                else:
                    cur.execute("Insert into member (memid,name,email,gender,contact,dob,pass,utype) values(?,?,?,?,?,?,?,?)",(
                        self.var_mem_prn.get(),
                        self.var_mem_name.get(),
                        self.var_mem_email.get(),
                        self.var_mem_gender.get(),
                        self.var_mem_contact.get(),
                        self.var_mem_dob.get(),
                        self.var_mem_pass.get(),
                        self.var_mem_usertype.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Member Added Successfully",parent=self.root)
                    self.show()

                
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            

    def show(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from member")
            rows=cur.fetchall()
            self.product_tabel.delete(*self.product_tabel.get_children())
            for row in rows:
                self.product_tabel.insert('',END,values=row)


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            

    def get_data(self,ev):
        f=self.product_tabel.focus()
        content=(self.product_tabel.item(f))
        row=content['values']
        # print(row)
        self.var_mem_prn.set(row[0])
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
            if self.var_mem_prn.get()=="":
                messagebox.showerror("Error","Member ID Must be required",parent=self.root)
            else:
                cur.execute("SELECT * FROM member WHERE memid=?",(self.var_mem_prn.get(),))
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
                        self.var_mem_prn.get()
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
            if self.var_mem_prn.get()=="":
                messagebox.showerror("Error","Member ID Must be required",parent=self.root)
            else:
                cur.execute("SELECT * FROM member WHERE memid=?",(self.var_mem_prn.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Member ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm", "Do you really want to delete ?",parent=self.root)
                    if op == True:
                        cur.execute("delete from member where memid=? ",(self.var_mem_prn.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Member Deleted Successfully",parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

#======= Clear Button ================================================================================================

    def clear(self):
        self.var_mem_prn.set(r"")
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
                    self.product_tabel.delete(*self.product_tabel.get_children())
                    for row in rows:
                        self.product_tabel.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record Found",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            


        




if __name__ == "__main__":
    root = Tk()
    obj = productClass(root)
    root.mainloop()        