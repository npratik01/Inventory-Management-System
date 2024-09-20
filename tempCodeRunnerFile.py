def update_datetime(self):
        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f"Welcome to Inventory Management System \t\t Date : {str(date_)} \t\t Time : {str(time_)} ")
        self.lbl_clock.after(200,self.update_datetime)