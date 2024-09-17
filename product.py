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

        
        lbl_Invoice_number = Label(product_Frame,text="Invoice Number :",font=("goudy old style",20)).place(x=30,y=60)
        lbl_product_name = Label(product_Frame,text="Product Name :",font=("goudy old style",20)).place(x=30,y=110)
        lbl_Invoice_date = Label(product_Frame,text="Invoice Date :",font=("goudy old style",20)).place(x=30,y=160)
        lbl_Price_of_the_item= Label(product_Frame,text="Price of the Item :",font=("goudy old style",20)).place(x=30,y=210)
        lbl_Invoice_Amount= Label(product_Frame,text="Total Invoice Amount :",font=("goudy old style",20)).place(x=30,y=260)
        lbl_supplier_name = Label(product_Frame,text="Supplier Name :",font=("goudy old style",20)).place(x=30,y=310)
        lbl_mobile_number = Label(product_Frame,text="Mobile Number of Vendor :",font=("goudy old style",20)).place(x=30,y=360)
        lbl_email_vendor= Label(product_Frame,text="Email of Vendor :",font=("goudy old style",20)).place(x=30,y=410)
        lbl_received_by_student_name = Label(product_Frame,text="Received by Student Name :",font=("goudy old style",20)).place(x=30,y=460)
        lbl_received_mo_no = Label(product_Frame,text="Received by Student Mob No. :",font=("goudy old style",20)).place(x=30,y=510)
        lbl_curr_posi_name = Label(product_Frame,text="Currently Position :",font=("goudy old style",20)).place(x=30,y=560)
        lbl_curr_posi_no = Label(product_Frame,text="Currently Number :",font=("goudy old style",20)).place(x=30,y=610)



        #txt_category =Label(product_Frame,text="Category",font=("goudy old style",20),bg="white").place(x=30,y=60)

        #==== Column2 ====
        # cmb_cat = ttk.Combobox(product_Frame,textvariable=self.var_cat,values=("Select"),state="readonly",justify=CENTER,font=("gaudy old style",15))
        # cmb_cat.place(x=300,y=60,width=200)
        # cmb_cat.current(0)

        # cmb_sup = ttk.Combobox(product_Frame,textvariable=self.var_invoice_no,values=("Select"),state="readonly",justify=CENTER,font=("gaudy old style",15))
        # cmb_sup.place(x=300,y=110,width=200)
        # cmb_sup.current(0)

        
        txt_name = Entry(product_Frame,textvariable=self.var_invoice_no,font=("gaudy old style",15),bg='lightyellow').place(x=370,y=60,width=200)
        txt_name = Entry(product_Frame,textvariable=self.var_cat,font=("gaudy old style",15),bg='lightyellow').place(x=370,y=110,width=200)
        txt_name = Entry(product_Frame,textvariable=self.var_invoice_date,font=("gaudy old style",15),bg='lightyellow').place(x=370,y=160,width=200)
        txt_name = Entry(product_Frame,textvariable=self.var_price_item,font=("gaudy old style",15),bg='lightyellow').place(x=370,y=210,width=200)
        txt_name = Entry(product_Frame,textvariable=self.var_inovice_amount,font=("gaudy old style",15),bg='lightyellow').place(x=370,y=260,width=200)
        txt_name = Entry(product_Frame,textvariable=self.var_supp_name,font=("gaudy old style",15),bg='lightyellow').place(x=370,y=310,width=200)
        txt_name = Entry(product_Frame,textvariable=self.var_mo_no,font=("gaudy old style",15),bg='lightyellow').place(x=370,y=360,width=200)
        txt_name = Entry(product_Frame,textvariable=self.var_email_vendor,font=("gaudy old style",15),bg='lightyellow').place(x=370,y=410,width=200)
        txt_name = Entry(product_Frame,textvariable=self.var_received_std_name,font=("gaudy old style",15),bg='lightyellow').place(x=370,y=460,width=200)
        txt_name = Entry(product_Frame,textvariable=self.var_received_mo_no,font=("gaudy old style",15),bg='lightyellow').place(x=370,y=510,width=200)
        txt_name = Entry(product_Frame,textvariable=self.var_curr_posi,font=("gaudy old style",15),bg='lightyellow').place(x=370,y=560,width=200)
        txt_name = Entry(product_Frame,textvariable=self.var_curr_mo_no,font=("gaudy old style",15),bg='lightyellow').place(x=370,y=610,width=200)

         #==== Buttons =====
        btn_add = Button(product_Frame,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=10,y=700,width=100,height=40)
        btn_update = Button(product_Frame,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=120,y=700,width=100,height=40)
        btn_delete = Button(product_Frame,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=230,y=700,width=100,height=40)
        btn_clear = Button(product_Frame,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=340,y=700,width=100,height=40)

        #==== Seaarch Frame ====
        SearchFrame = LabelFrame(self.root,text="Search Member",font=("goudy old style",12,"bold"),bd=2,bg="white")
        SearchFrame.place(x=680,y=30,width=700,height=80)

        #==== Options ====
        cmb_search = ttk.Combobox(SearchFrame,textvariable=self.var_mem_searchby,values=("Select","Invoice No","Name"),state="readonly",justify=CENTER,font=("gaudy old style",15))
        cmb_search.place(x=20,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_mem_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=220,y=10,width=280)
        btn_search = Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=530,y=8,width=150,height=30)



        #==== Product Details =====

        p_frame = Frame(self.root,bd=3,relief=RIDGE)
        p_frame.place(x=680,y=100,width=700,height=390)

        scrolly = Scrollbar(p_frame,orient=VERTICAL)
        scrollx = Scrollbar(p_frame,orient=HORIZONTAL)
        
        self.product_tabel=ttk.Treeview(p_frame,columns=("Invoice_number","Product Name","Invoice date","Price","Total Invoice Amount","Supplier Name","Vendor MO NO","Email of vendor","R Student Name","R Std Mo No","Current position","Current Mo No"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_tabel.xview)
        scrolly.config(command=self.product_tabel.yview)
        
        self.product_tabel.heading("Invoice_number",text="Invoice Number")
        self.product_tabel.heading("Product Name",text="Product Name")
        self.product_tabel.heading("Invoice date",text="Invoice Date")
        self.product_tabel.heading("Price",text="Price")
        self.product_tabel.heading("Total Invoice Amount",text="Total Invoice Amount")
        self.product_tabel.heading("Supplier Name",text="Supplier Name")
        self.product_tabel.heading("Vendor MO NO",text="Vendor Mob No.")
        self.product_tabel.heading("Email of vendor",text="Email of vendor")
        self.product_tabel.heading("R Student Name",text="Rec. Student Name")
        self.product_tabel.heading("R Std Mo No",text="Rec. Std Mob No")
        self.product_tabel.heading("Current position",text="Current Position")
        self.product_tabel.heading("Current Mo No",text="Current Mob No")

        

        self.product_tabel["show"]="headings"

        
        self.product_tabel.column("Invoice_number",width=100)
        self.product_tabel.column("Product Name",width=90)
        self.product_tabel.column("Invoice date",width=100)
        self.product_tabel.column("Price",width=100)
        self.product_tabel.column("Total Invoice Amount",width=100)
        self.product_tabel.column("Supplier Name",width=100)
        self.product_tabel.column("Vendor MO NO",width=100)
        self.product_tabel.column("Email of vendor",width=100)
        self.product_tabel.column("R Student Name",width=100)
        self.product_tabel.column("R Std Mo No",width=100)
        self.product_tabel.column("Current position",width=100)
        self.product_tabel.column("Current Mo No",width=100)
        self.product_tabel.pack(fill=BOTH,expand=1)
        self.product_tabel.bind("<ButtonRelease-1>",self.get_data)

        self.show()


    def add(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_invoice_no.get()=="":
                messagebox.showerror("Error","INVOICE NUMBER Must be required",parent=self.root)
            else:               # "Product Name","Invoice number","Invoice date","Price","Total Invoice Amount","Supplier Name","Vendor MO NO","Email of vendor","R Student Name","R Std Mo No","Current position","Current Mo No"
                cur.execute("SELECT * FROM product WHERE [Invoice_number]=?",(self.var_invoice_no.get(),))
                row=cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Product already present , try different",parent=self.root)
                else:
                    cur.execute("""
                        INSERT INTO product (
                            [Invoice_number],[Product Name], [Invoice date], [Price], 
                            [Total Invoice Amount], [Supplier Name], [Vendor MO NO], 
                            [Email of vendor], [R Student Name], [R Std Mo No], 
                            [Current position], [Current Mo No]
                        ) 
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """, (
                        
                        self.var_invoice_no.get(),
                        self.var_cat.get(),
                        self.var_invoice_date.get(),
                        self.var_price_item.get(),
                        self.var_inovice_amount.get(),
                        self.var_supp_name.get(),
                        self.var_mo_no.get(),
                        self.var_email_vendor.get(),
                        self.var_received_std_name.get(),
                        self.var_received_mo_no.get(),
                        self.var_curr_posi.get(),
                        self.var_curr_mo_no.get()
                    ))
                    
                    # cur.execute("Insert into product (Product Name,Invoice_number,Invoice date,Price,Total Invoice Amount,Supplier Name,Vendor MO NO,Email of vendor,R Student Name,R Std Mo No,Current position,Current Mo No) values(?,?,?,?,?,?,?,?,?,?,?,?)",(
                    #     self.var_cat.get(),
                    #     self.var_invoice_no.get(),
                    #     self.var_invoice_date.get(),
                    #     self.var_price_item.get(),
                    #     self.var_inovice_amount.get(),
                    #     self.var_supp_name.get(),
                    #     self.var_mo_no.get(),
                    #     self.var_email_vendor.get(),
                    #     self.var_received_std_name.get(),
                    #     self.var_received_mo_no.get(),
                    #     self.var_curr_posi.get(),
                    #     self.var_curr_mo_no.get(),
                    # ))
                    con.commit()
                    messagebox.showinfo("Success","Product Added Successfully",parent=self.root)
                    self.show()

                
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            

    def show(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            rows=cur.fetchall()
            self.product_tabel.delete(*self.product_tabel.get_children())
            for row in rows:
                self.product_tabel.insert('',END,values=row)


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            

    # def get_data(self,ev):
    #     f=self.product_tabel.focus()
    #     content=(self.product_tabel.item(f))
    #     row=content['values']
        
    #     # print(row)


        # Updated get_data method
    def get_data(self, ev):
        f = self.product_tabel.focus()
        content = self.product_tabel.item(f)
        row = content['values']
        # if row:
        # Assuming correct order and existing database schema alignment
        
        self.var_invoice_no.set(row[0])
        self.var_cat.set(row[1])
        self.var_invoice_date.set(row[2])
        self.var_price_item.set(row[3])
        self.var_inovice_amount.set(row[4])
        self.var_supp_name.set(row[5])
        self.var_mo_no.set(row[6])
        self.var_email_vendor.set(row[7])
        self.var_received_std_name.set(row[8])
        self.var_received_mo_no.set(row[9])
        self.var_curr_posi.set(row[10])
        self.var_curr_mo_no.set(row[11])

#======== UPDATE DATA =======================================================================================

    def update(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_invoice_no.get()=="":
                messagebox.showerror("Error","Please Select Product Invoice No From List",parent=self.root)
            else:
                cur.execute("SELECT * FROM product WHERE [Invoice_number]=?",(self.var_invoice_no.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Product Invoice Number",parent=self.root)
                else:
                    #cur.execute("Update member set name=?,email=?,gender=?,contact=?,dob=?,pass=?,utype=? where memid=?",(
                    cur.execute("""
                        UPDATE product 
                        SET 
                            [Product Name]=?, 
                            [Invoice date]=?, 
                            [Price]=?, 
                            [Total Invoice Amount]=?, 
                            [Supplier Name]=?, 
                            [Vendor MO NO]=?, 
                            [Email of vendor]=?, 
                            [R Student Name]=?, 
                            [R Std Mo No]=?, 
                            [Current position]=?, 
                            [Current Mo No]=?
                        WHERE 
                            [Invoice_number]=?
                    """,(
                
                    self.var_cat.get(),
                    self.var_invoice_date.get(),
                    self.var_price_item.get(),
                    self.var_inovice_amount.get(),
                    self.var_supp_name.get(),
                    self.var_mo_no.get(),
                    self.var_email_vendor.get(),
                    self.var_received_std_name.get(),
                    self.var_received_mo_no.get(),
                    self.var_curr_posi.get(),
                    self.var_curr_mo_no.get(),
                    self.var_invoice_no.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","product Updated Successfully",parent=self.root)
                    self.show()

                
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
#============ DELETE Button =========================================================================

    def delete(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_invoice_no.get()=="":
                messagebox.showerror("Error","Select the product from the list",parent=self.root)
            else:
                cur.execute("SELECT * FROM product WHERE [Invoice_number]=?",(self.var_invoice_no.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid product Invoice number",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm", "Do you really want to delete ?",parent=self.root)
                    if op == True:
                        cur.execute("delete from product where [Invoice_number]=? ",(self.var_invoice_no.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Product Deleted Successfully",parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

#======= Clear Button ================================================================================================

    def clear(self):
        
        self.var_invoice_no.set(""),
        self.var_cat.set(""),
        self.var_invoice_date.set(""),
        self.var_price_item.set(""),
        self.var_inovice_amount.set(""),
        self.var_supp_name.set(""),
        self.var_mo_no.set(""),
        self.var_email_vendor.set(""),
        self.var_received_std_name.set(""),
        self.var_received_mo_no.set(""),
        self.var_curr_posi.set(""),
        self.var_curr_mo_no.set("")
        self.var_mem_searchtxt.set("")
        self.var_mem_searchby.set("Select")

        self.show()

#======= Search Button ===============================
    def search(self):
        con = sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            # Validate the 'Search By' option
            if self.var_mem_searchby.get() == "Select":
                messagebox.showerror("Error", "Please select a valid search category", parent=self.root)
                return
            
            # Validate the search input
            if self.var_mem_searchtxt.get() == "":
                messagebox.showerror("Error", "Search input is required", parent=self.root)
                return

            # Map the search field to actual column names
            search_by_column = self.var_mem_searchby.get()
            if search_by_column == "Invoice No":
                search_by_column = "Invoice_number"
            elif search_by_column == "Name":
                search_by_column = "[Product Name]"

            # Use LIKE for text fields, and = for numeric fields
            if search_by_column == "Invoice Number":
                query = f"SELECT * FROM product WHERE {search_by_column} = ?"
                cur.execute(query, (self.var_mem_searchtxt.get(),))
            else:
                query = f"SELECT * FROM product WHERE LOWER({search_by_column}) LIKE LOWER(?)"
                cur.execute(query, ('%' + self.var_mem_searchtxt.get().lower() + '%',))
                

            # Fetch and display results
            rows = cur.fetchall()

            # Populate the table with search results
            if rows:
                self.product_tabel.delete(*self.product_tabel.get_children())
                for row in rows:
                    self.product_tabel.insert('', END, values=row)
            else:
                messagebox.showerror("Error", "No records found", parent=self.root)
        
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        
        finally:
            # Ensure the connection is closed after the operation
            con.close()


        




if __name__ == "__main__":
    root = Tk()
    obj = productClass(root)
    root.mainloop()        