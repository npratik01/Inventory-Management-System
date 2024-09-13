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


        product_Frame=Frame(self.root,bd=5,relief=RIDGE)
        product_Frame.place(x=10,y=10,width=650,height=800)

        #=======title=======
        title = Label(product_Frame,text="Manage Product Details",font=("goudy old style",20),bg="#0f4d7d",fg="white",).pack(side=TOP,fill=X)

        lbl_product_name = Label(product_Frame,text="Product Name",font=("goudy old style",20),bg="white").place(x=30,y=60)
        lbl_Invoice_number = Label(product_Frame,text="Invoice number",font=("goudy old style",20),bg="white").place(x=40,y=110)
        lbl_Invoice_date = Label(product_Frame,text="Invoice date",font=("goudy old style",20),bg="white").place(x=30,y=160)
        lbl_Price_of_the_item= Label(product_Frame,text="Price of the item",font=("goudy old style",20),bg="white").place(x=30,y=210)
        lbl_Invoice_Amount= Label(product_Frame,text="Total Invoice Amount",font=("goudy old style",20),bg="white").place(x=30,y=260)
        lbl_supplier_name = Label(product_Frame,text="Supplier Name",font=("goudy old style",20),bg="white").place(x=30,y=310)
        lbl_mobile_number = Label(product_Frame,text="Mobile Number of vendor",font=("goudy old style",20),bg="white").place(x=30,y=360)
        lbl_email_vendor= Label(product_Frame,text="Email of Vendor",font=("goudy old style",20),bg="white").place(x=30,y=410)
        lbl_received_by_student_name = Label(product_Frame,text="Received by student name",font=("goudy old style",20),bg="white").place(x=30,y=460)

        txt_category =Label(product_Frame,text="Category",font=("goudy old style",20),bg="white").place(x=30,y=60)

        #==== Column2 ====
        # cmb_cat = ttk.Combobox(product_Frame,textvariable=self.var_cat,values=("Select"),state="readonly",justify=CENTER,font=("gaudy old style",15))
        # cmb_cat.place(x=300,y=60,width=200)
        # cmb_cat.current(0)

        # cmb_sup = ttk.Combobox(product_Frame,textvariable=self.var_invoice_no,values=("Select"),state="readonly",justify=CENTER,font=("gaudy old style",15))
        # cmb_sup.place(x=300,y=110,width=200)
        # cmb_sup.current(0)

        self.var_cat=StringVar()
        self.var_invoice_no=StringVar()
        self.var_invoice_date=StringVar()
        self.var_price_item=StringVar()
        self.var_inovice_amount=StringVar()
        self.var_supp_name=StringVar()
        self.var_mo_no=StringVar()
        self.var_email_vendor=StringVar()
        self.var_received_std_name=StringVar()

        txt_name = Entry(product_Frame,textvariable=self.var_cat,font=("gaudy old style",15),bg='lightyellow').place(x=300,y=60,width=200)
        txt_name = Entry(product_Frame,textvariable=self.var_invoice_no,font=("gaudy old style",15),bg='lightyellow').place(x=300,y=110,width=200)
        txt_name = Entry(product_Frame,textvariable=self.var_invoice_date,font=("gaudy old style",15),bg='lightyellow').place(x=300,y=160,width=200)
        txt_name = Entry(product_Frame,textvariable=self.var_price_item,font=("gaudy old style",15),bg='lightyellow').place(x=300,y=210,width=200)
        txt_name = Entry(product_Frame,textvariable=self.var_inovice_amount,font=("gaudy old style",15),bg='lightyellow').place(x=300,y=260,width=200)
        txt_name = Entry(product_Frame,textvariable=self.var_supp_name,font=("gaudy old style",15),bg='lightyellow').place(x=300,y=310,width=200)
        txt_name = Entry(product_Frame,textvariable=self.var_mo_no,font=("gaudy old style",15),bg='lightyellow').place(x=300,y=360,width=200)
        txt_name = Entry(product_Frame,textvariable=self.var_email_vendor,font=("gaudy old style",15),bg='lightyellow').place(x=300,y=410,width=200)
        txt_name = Entry(product_Frame,textvariable=self.var_received_std_name,font=("gaudy old style",15),bg='lightyellow').place(x=300,y=460,width=200)

        




if __name__ == "__main__":
    root = Tk()
    obj = productClass(root)
    root.mainloop()        