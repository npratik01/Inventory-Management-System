from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3
import time
import os
import tempfile


class BillClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | Team Third Axis")
        self.root.config(bg = "white")
        self.cart_list=[]
        self.chk_print=0

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
        ProductFrame1.place(x=6,y=110,width=410,height=550)

        pTitle=Label(ProductFrame1,text="All Products",font=("goudy old style",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)

        #======Product search Frame ===============
        self.var_search=StringVar()
        self.var_mem_searchtxt = StringVar()
        ProductFrame2 = Frame(ProductFrame1,bd=2,relief=RIDGE,bg="white")
        ProductFrame2.place(x=2,y=42,width=398,height=90)

        lbl_search=Label(ProductFrame2,text="Search Product | By Name",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=2,y=5)

        lbl_search=Label(ProductFrame2,text="Product Name",font=("times new roman",15,"bold"),bg="white").place(x=2,y=43)
        txt_search=Entry(ProductFrame2,textvariable=self.var_search,font=("times new roman",15,),bg="lightyellow").place(x=130,y=47,width=150,height=22)
        btn_search=Button(ProductFrame2,text="Search",command=self.search,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=285,y=45,width=100,height=25)
        btn_showAll=Button(ProductFrame2,text="Show All",command=self.show,font=("goudy old style",15),bg="#083531",fg="white",cursor="hand2").place(x=285,y=10,width=100,height=25)

        #======Product Details Frame ===============
        productFrame3 = Frame(ProductFrame1,bd=3,relief=RIDGE)
        productFrame3.place(x=2,y=140,width=398,height=375)

        scrolly = Scrollbar(productFrame3,orient=VERTICAL)
        scrollx = Scrollbar(productFrame3,orient=HORIZONTAL)

        self.product_Table=ttk.Treeview(productFrame3,columns=("Invoice_number","[Product Name]","price","qty"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_Table.xview)
        scrolly.config(command=self.product_Table.yview)

        self.product_Table.heading("Invoice_number",text="Invoice No")
        self.product_Table.heading("[Product Name]",text="Product Name")
        self.product_Table.heading("price",text="Price")
        self.product_Table.heading("qty",text="QTY")

        self.product_Table["show"]="headings"

        self.product_Table.column("Invoice_number",width=90)
        self.product_Table.column("[Product Name]",width=100) 
        self.product_Table.column("price",width=100)
        self.product_Table.column("qty",width=100)
        self.product_Table.pack(fill=BOTH,expand=1)
        self.product_Table.bind("<ButtonRelease-1>",self.get_data)
        lbl_note=Label(ProductFrame1,text="Note: 'Enter 0 Quantity to remove product from the cart'",font=("goudy old style",12),anchor='w',bg="white",fg="red").pack(side=BOTTOM,fill=X)

        #========== Customer Frame =================
        self.var_cname=StringVar()
        self.var_contact=StringVar()
        customerFrame = Frame(self.root,bd=4,relief=RIDGE,bg="white")
        customerFrame.place(x=420,y=110,width=530,height=70)

        cTitle=Label(customerFrame,text="Customer Details",font=("goudy old style",15),bg="lightgrey").pack(side=TOP,fill=X)
        lbl_name=Label(customerFrame,text="Name",font=("times new roman",15),bg="white").place(x=5,y=35)
        txt_name=Entry(customerFrame,textvariable=self.var_cname,font=("times new roman",13),bg="lightyellow").place(x=80,y=35,width=180)

        lbl_contact=Label(customerFrame,text="Contact No.",font=("times new roman",15),bg="white").place(x=270,y=35)
        txt_contact=Entry(customerFrame,textvariable=self.var_contact,font=("times new roman",13),bg="lightyellow").place(x=380,y=35,width=140)

        #======Cal Cart Frame ===============
        calCartFrame = Frame(self.root,bd=2,relief=RIDGE,bg="white")
        calCartFrame.place(x=420,y=190,width=530,height=360)

        #======Calculator Frame  ===============
        self.var_cal_input=StringVar()
        calFrame = Frame(calCartFrame,bd=9,relief=RIDGE,bg="white")
        calFrame.place(x=5,y=10,width=268,height=340)


        txt_cal_input=Entry(calFrame,textvariable=self.var_cal_input,font=('arial',15,'bold'),width=21,bd=10,relief=GROOVE,state='readonly',justify=RIGHT)
        txt_cal_input.grid(row=0,columnspan=4)

        btn_7=Button(calFrame,text="7",font=('arial',15,'bold'),command=lambda:self.get_input(7),cursor="hand2",bd=5,width=4,pady=10).grid(row=1,column=0)
        btn_8=Button(calFrame,text="8",font=('arial',15,'bold'),command=lambda:self.get_input(8),cursor="hand2",bd=5,width=4,pady=10).grid(row=1,column=1)
        btn_9=Button(calFrame,text="9",font=('arial',15,'bold'),command=lambda:self.get_input(9),cursor="hand2",bd=5,width=4,pady=10).grid(row=1,column=2)
        btn_sum=Button(calFrame,text="+",font=('arial',15,'bold'),command=lambda:self.get_input("+"),cursor="hand2",bd=5,width=4,pady=10).grid(row=1,column=3)

        btn_4=Button(calFrame,text="4",font=('arial',15,'bold'),command=lambda:self.get_input(4),cursor="hand2",bd=5,width=4,pady=10).grid(row=2,column=0)
        btn_5=Button(calFrame,text="5",font=('arial',15,'bold'),command=lambda:self.get_input(5),cursor="hand2",bd=5,width=4,pady=10).grid(row=2,column=1)
        btn_6=Button(calFrame,text="6",font=('arial',15,'bold'),command=lambda:self.get_input(6),cursor="hand2",bd=5,width=4,pady=10).grid(row=2,column=2)
        btn_sub=Button(calFrame,text="-",font=('arial',15,'bold'),command=lambda:self.get_input("-"),cursor="hand2",bd=5,width=4,pady=10).grid(row=2,column=3)

        btn_1=Button(calFrame,text="1",font=('arial',15,'bold'),command=lambda:self.get_input(1),cursor="hand2",bd=5,width=4,pady=10).grid(row=3,column=0)
        btn_2=Button(calFrame,text="2",font=('arial',15,'bold'),command=lambda:self.get_input(2),cursor="hand2",bd=5,width=4,pady=10).grid(row=3,column=1)
        btn_3=Button(calFrame,text="3",font=('arial',15,'bold'),command=lambda:self.get_input(3),cursor="hand2",bd=5,width=4,pady=10).grid(row=3,column=2)
        btn_mul=Button(calFrame,text="*",font=('arial',15,'bold'),command=lambda:self.get_input("*"),cursor="hand2",bd=5,width=4,pady=10).grid(row=3,column=3)

        btn_0=Button(calFrame,text="0",font=('arial',15,'bold'),command=lambda:self.get_input(0),cursor="hand2",bd=5,width=4,pady=15).grid(row=4,column=0)
        btn_c=Button(calFrame,text="C",font=('arial',15,'bold'),command=self.clear_cal,cursor="hand2",bd=5,width=4,pady=15).grid(row=4,column=1)
        btn_equal=Button(calFrame,text="=",font=('arial',15,'bold'),command=self.perform_cal,cursor="hand2",bd=5,width=4,pady=15).grid(row=4,column=2)
        btn_div=Button(calFrame,text="/",font=('arial',15,'bold'),command=lambda:self.get_input("/"),cursor="hand2",bd=5,width=4,pady=15).grid(row=4,column=3)


        #======Cart Frame ===============
        cartFrame = Frame(calCartFrame,bd=3,relief=RIDGE)
        cartFrame.place(x=280,y=8,width=245,height=342)
        self.cTitle=Label(cartFrame,text="Cart \tTotal Product : [0]",font=("goudy old style",15),bg="lightgrey")
        self.cTitle.pack(side=TOP,fill=X)


        scrolly = Scrollbar(cartFrame,orient=VERTICAL)
        scrollx = Scrollbar(cartFrame,orient=HORIZONTAL)

        self.cart_Table=ttk.Treeview(cartFrame,columns=("Invoice_number","[Product Name]","price","qty"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.cart_Table.xview)
        scrolly.config(command=self.cart_Table.yview)

        self.cart_Table.heading("Invoice_number",text="Invoice No")
        self.cart_Table.heading("[Product Name]",text="Product Name")
        self.cart_Table.heading("price",text="Price")
        self.cart_Table.heading("qty",text="QTY")

        self.cart_Table["show"]="headings"

        self.cart_Table.column("Invoice_number",width=80)
        self.cart_Table.column("[Product Name]",width=100) 
        self.cart_Table.column("price",width=80)
        self.cart_Table.column("qty",width=40)
        self.cart_Table.pack(fill=BOTH,expand=1)
        self.cart_Table.bind("<ButtonRelease-1>",self.get_data_cart)
    

        #======Add Cart Widgets Frame ===============
        self.var_Invoice_number=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar() 
        addCartButtonWidgetsFrames = Frame(self.root,bd=2,relief=RIDGE,bg="white")
        addCartButtonWidgetsFrames.place(x=420,y=550,width=530,height=110)

        lbl_pName=Label(addCartButtonWidgetsFrames,text="Product Name",font=("times new roman",15),bg="white").place(x=5,y=5)
        lbl_pName=Entry(addCartButtonWidgetsFrames,textvariable=self.var_pname,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=5,y=35,width=190,height=22)

        lbl_pPrice=Label(addCartButtonWidgetsFrames,text="Price Per QTY",font=("times new roman",15),bg="white").place(x=230,y=5)
        lbl_pPrice=Entry(addCartButtonWidgetsFrames,textvariable=self.var_price,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=230,y=35,width=150,height=22)

        lbl_pPrice=Label(addCartButtonWidgetsFrames,text="Quantity",font=("times new roman",15),bg="white").place(x=390,y=5)
        lbl_pPrice=Entry(addCartButtonWidgetsFrames,textvariable=self.var_qty,font=("times new roman",15),bg="lightyellow").place(x=390,y=35,width=120,height=22)

        self.lbl_inStock=Label(addCartButtonWidgetsFrames,text="In Stock",font=("times new roman",15),bg="white")
        self.lbl_inStock.place(x=5,y=70)

        btn_clearCart=Button(addCartButtonWidgetsFrames,text="Clear",command=self.clear_cart,font=("times new roman",15, "bold"),bg="lightgrey",cursor="hand2").place(x=180,y=70,width=150,height=30)
        btn_addCart=Button(addCartButtonWidgetsFrames,text="Add | Update Cart",command=self.add_update_cart,font=("times new roman",15, "bold"),bg="orange",cursor="hand2").place(x=340,y=70,width=180,height=30)


#============= Billing Area=================

        billFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        billFrame.place(x=953,y=110,width=400,height=410)

        bTitle=Label(billFrame,text="Customer Bills",font=("goudy old style",20,"bold"),bg="#f44336",fg="white").pack(side=TOP,fill=X)
        scrolly=Scrollbar(billFrame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)
        self.txt_billArea=Text(billFrame,font=("goudy old style",20,"bold"),yscrollcommand=scrolly.set)
        self.txt_billArea.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_billArea.yview)


#=========== Billing Buttons ==================
        billMenuFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        billMenuFrame.place(x=953,y=520,width=400,height=140)

        self.lbl_amt=Label(billMenuFrame,text="Bill Amount\n[0]",font=("goudy old style",15,"bold"),bg="#3f51b5",fg="white")
        self.lbl_amt.place(x=2,y=5,width=120,height=70)

        self.lbl_discount=Label(billMenuFrame,text="Discount \n[5%]",font=("goudy old style",15,"bold"),bg="#8bc34a",fg="white")
        self.lbl_discount.place(x=124,y=5,width=120,height=70)

        self.lbl_net_pay=Label(billMenuFrame,text="Net Pay\n[0]",font=("goudy old style",15,"bold"),bg="#607d8b",fg="white")
        self.lbl_net_pay.place(x=246,y=5,width=145,height=70)

        btn_print=Button(billMenuFrame,text="Print",command=self.print_bill,cursor="hand2",font=("goudy old style",15,"bold"),bg="lightgreen",fg="white")
        btn_print.place(x=2,y=80,width=100,height=50)

        btn_clearAll=Button(billMenuFrame,text="Clear All",command=self.clearAll,cursor="hand2",font=("goudy old style",15,"bold"),bg="grey",fg="white")
        btn_clearAll.place(x=105,y=80,width=110,height=50)

        btn_generate=Button(billMenuFrame,text="Generate/Save Bill",command=self.generate_bill,cursor="hand2",font=("goudy old style",15,"bold"),bg="#009688",fg="white")
        btn_generate.place(x=219,y=80,width=172,height=50)

        footer=Label(self.root,text="Inventory Management System | Team Third Axis",font=("times new roman",11),bg="#4d636d").pack(side=BOTTOM,fill=X)

        self.show()
        # self.bill_Top()
        self.update_datetime()


#============== All Functions=========================

    def get_input(self,num):
        xnum=self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)
        

    def clear_cal(self):
        self.var_cal_input.set('')

    def perform_cal(self):
        result=self.var_cal_input.get()
        self.var_cal_input.set(eval(result))


    def show(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            cur.execute("select Invoice_number,[Product Name],price,qty from product")
            rows=cur.fetchall()
            self.product_Table.delete(*self.product_Table.get_children())
            for row in rows:
                self.product_Table.insert('',END,values=row)


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            
    def search(self):
        invoice_number = self.var_search.get().strip()
        product_name = self.var_mem_searchtxt.get().strip()

        # Build the SQL query based on the presence of input values
        query = "SELECT Invoice_number, [Product Name], price, qty FROM product WHERE 1=1"
        params = []

        if invoice_number:
            query += " AND Invoice_number LIKE ?"
            params.append(f"%{invoice_number}%")

        if product_name:
            query += " AND [Product Name] LIKE ?"
            params.append(f"%{product_name}%")

        con = sqlite3.connect('ims.db')
        cur = con.cursor()
        try:
            cur.execute(query, params)
            rows = cur.fetchall()
            self.product_Table.delete(*self.product_Table.get_children())
            for row in rows:
                self.product_Table.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

    def get_data(self, ev):
        f = self.product_Table.focus()
        content = self.product_Table.item(f)
        row = content['values']
        self.var_Invoice_number.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.lbl_inStock.config(text=f"In Stock[{str(row[3])}]")  
        self.var_stock.set(row[3])
        self.var_qty.set('1')  

    def get_data_cart(self, ev):
        f = self.cart_Table.focus()
        content = self.cart_Table.item(f)
        row = content['values']
        self.var_Invoice_number.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.var_qty.set(row[3])
        self.lbl_inStock.config(text=f"In Stock[{str(row[4])}]")  
        self.var_stock.set(row[4])
          

    def add_update_cart(self):
        if self.var_Invoice_number.get()=='':
            messagebox.showerror('Error',"Please select Product from the list",parent=self.root)

        elif self.var_qty.get()=='':
            messagebox.showerror('Error',"Quantity is Required",parent=self.root)
        elif (int(self.var_qty.get()) > int(self.var_stock.get())):
            messagebox.showerror('Error',"Invalid Quantity",parent=self.root)
        else:
           #price_cal=float(int(self.var_qty.get())*float(self.var_price.get()))
            price_cal=self.var_price.get()
            cart_data=[self.var_Invoice_number.get(),self.var_pname.get(),price_cal,int(self.var_qty.get()),self.var_stock.get()]

            #====== Update Cart============
            present='no'
            index_ = -1
            for row in self.cart_list:
                if self.var_Invoice_number.get()==row[0]:
                    present='yes'
                    break
                index_+=1
            if present=='yes':
                op=messagebox.askyesno("Confirm","Product already present\nDo you want to Update | Remove from the Cart List",parent=self.root)
                if op==True:
                    if self.var_qty.get()=="0":
                        self.cart_list.pop(index_)
                    else:
                        # self.cart_list[index_][2]=price_cal #price
                        self.cart_list[index_][3]=self.var_qty.get() #quantity

            else:   
                self.cart_list.append(cart_data)
            self.show_cart()
            self.bill_update()
    def bill_update(self):
        self.bill_amt=0
        self.net_pay=0
        self.discount=0
        for row in self.cart_list:
            self.bill_amt=self.bill_amt+(float(row[2])*int(row[3]))
        self.discount=(self.bill_amt*5)/100
        self.net_pay=self.bill_amt-self.discount 
        self.lbl_amt.config(text=f'Bill Amt\n{str(self.bill_amt)}')
        self.lbl_net_pay.config(text=f'Net Pay\n{str(self.net_pay)}')
        self.cTitle.config(text=f"Cart \tTotal Product : [{str(len(self.cart_list))}]")



    def show_cart(self):
        try:
            self.cart_Table.delete(*self.cart_Table.get_children())
            for row in self.cart_list:
                self.cart_Table.insert('',END,values=row)


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    
    def generate_bill(self):
        if self.var_cname.get()=='' or self.var_contact.get()=='':
            messagebox.showerror("Error",f"Customer Details are required",parent=self.root)
        elif len(self.cart_list)==0:
            messagebox.showerror("Error",f"Please Add the product to the Cart",parent=self.root)

        else:
            #==============Bill Top================
            self.bill_Top()
            #==============Bill Middle================
            self.bill_middle()
            #==============Bill Bottom================
            self.bill_bottom()

            self.chk_print=1
            fp=open(f'bill/{str(self.invoice)}.txt','w')
            fp.write(self.txt_billArea.get('1.0',END))
            fp.close()
            messagebox.showinfo("Saved", "Bill has beenn Generated Successfully",parent=self.root)

           
           
    def bill_Top(self):
        self.invoice=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%Y"))
        bill_top_temp=f''' 
\tGCOEJ
  Inventory Management System
Phone No. 74994***** ,\nJalgaon-425001
{str("="*52)}
Customer Name : {self.var_cname.get()}
Ph No. : {self.var_contact.get()}
Bill No. {str(self.invoice)}\nDate : {str(time.strftime("%d%m%Y"))}
{str("="*52)}
Product Name\tQTY\t  Price
{str("="*52)}
        '''
        self.txt_billArea.delete('1.0',END)
        self.txt_billArea.insert('1.0',bill_top_temp)

    def bill_bottom(self):
        bill_bottom_temp=f'''
{str("="*52)} 
Bill Amount\t\tRs.{self.bill_amt}
Discount\t\tRs.{self.discount}
Net Pay\t\tRs{self.net_pay }
{str("="*52)}\n
        '''
        self.txt_billArea.insert(END,bill_bottom_temp)

    def bill_middle(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            for row in self.cart_list:
                
                 
                name=row[1]
                qty=int(row[3])
                price=float((row[2])*int(row[3]))
                price=str(price)
                self.txt_billArea.insert(END,"\n"+name+"\t"+str(qty)+"\tRs."+price)
                # ======update quantity in product table
                cur.execute('Update product set qty=? where pid=?',(
                    qty
                ))
                con.commit()
            con.close()
            self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            

    def clear_cart(self):
        self.var_Invoice_number.set('')
        self.var_pname.set('')
        self.var_price.set('')
        self.var_qty.set('')
        self.lbl_inStock.config(text="In Stock")  
        self.var_stock.set('')

    def clearAll(self):
        del self.cart_list[:]
        self.var_cname.set('')
        self.var_contact.set('')
        self.txt_billArea.delete('1.0',END)
        self.cTitle.config(text=f"Cart \tTotal Product : [0]")
        self.var_search.set('')
        self.clear_cart()
        self.show()
        self.show_cart()
        self.chk_print=0

    def update_datetime(self):
        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f"Welcome to Inventory Management System \t\t Date : {str(date_)} \t\t Time : {str(time_)} ")
        self.lbl_clock.after(200,self.update_datetime)

    def print_bill(self):
        if self.chk_print==1:
            messagebox.showinfo("Print","Please wait while Printing",parent=self.root)
            newfile=tempfile.mktemp('.txt')
            open(newfile,'w').write(self.txt_billArea.get('1.0',END))
            os.startfile(newfile,'print')
        else:
            messagebox.showinfo("Print","Please generate bill, to print the reciept",parent=self.root)
            


if __name__ == "__main__":
    root = Tk()
    obj = BillClass(root)
    root.mainloop()