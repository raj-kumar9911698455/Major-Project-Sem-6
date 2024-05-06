from tkinter import *
from tkinter import messagebox
import sqlite3
import matplotlib.pyplot as plt

# Database

conn = sqlite3.connect('T&T_Management_System.db')
c = conn.cursor()

# Tables in database
'''
c.execute("""CREATE TABLE dest_Info(
    dest_Name text,
    famous_Place text,
    famous_Food text
    )""")
c.execute("""CREATE TABLE ticket_Booking(
    Cust_Name text,
    Age INTEGER,
    Gender text,
    Booking_Date INTEGER,
    Journey_Date INTEGER,
    Starting_Location text,
    Destination text,
    Email_Id text,
    Contact_No INTEGER,
    Mode_Of_Transport text,
    Payment_Mode text
    )""")
c.execute("""CREATE TABLE agent_Info(
    First_Name text,
    Last_Name text,
    Username text PRIMARY KEY,
    Password text NOT NULL
    )""")'''

conn.commit()
conn.close()


# Fuction for booking Tickets

def book_tickets():
    ticket = Toplevel()
    ticket.title("Ticket Booking")
    def booking_Confirmation():
        submit_response = messagebox.askyesno("CONFIRMATION!!!", """(Please check your entries before Submitting)
                                          DO YOU WANT TO SUBMIT ? """,parent=ticket)
    
        if submit_response == 1:
            conn = sqlite3.connect('T&T_Management_System.db')
            c = conn.cursor()
            c.execute("INSERT INTO ticket_Booking VALUES(:Cust_Name, :Age, :Gender, :Booking_Date, :Journey_Date, :Starting_Location, :Destination, :Email_Id, :Contact_No, :Mode_Of_Transport, :Payment_Mode)",
                  {
                      'Cust_Name':Cust_Name.get().capitalize(),
                      'Age':Age.get(),
                      'Gender':gender_Value.get(),
                      'Booking_Date':Booking_Date.get(),
                      'Journey_Date':Journey_Date.get(),
                      'Starting_Location':Starting_Location.get().capitalize(),
                      'Destination':Destination.get().capitalize(),
                      'Email_Id':Email_Id.get(),
                      'Contact_No':Contact_No.get(),
                      'Mode_Of_Transport':Mode_Of_Transport.get().capitalize(),
                      'Payment_Mode':Payment_Mode.get().capitalize()
                   })
            conn.commit()
            conn.close()
            confirmation = messagebox.showinfo("Thanks for Visiting", "BOOKING SUCCESSFULL !!!",parent=ticket)
            if confirmation == "ok":
                ticket.destroy()
        else:
            pass
        
    
    def clear_Form():
        Cust_Name.delete(0, END)
        Age.delete(0, END)
        Booking_Date.delete(0, END)
        Journey_Date.delete(0, END)
        Starting_Location.delete(0, END)
        Destination.delete(0, END)
        Email_Id.delete(0, END)
        Contact_No.delete(0, END)
        Mode_Of_Transport.delete(0, END)
        Payment_Mode.delete(0, END)

    # Heading for the ticket booking window
    
    label1 = Label(ticket, text ="="*65, font=("Helvetica",15, "bold","italic"),fg="green")
    label1.grid(row=0,column=0,columnspan=4)
    label2 = Label(ticket, text ="BOOK YOUR TICKETS !!!", font=("Helvetica",18, "bold","italic"),fg="blue")
    label2.grid(row=1,column=0,columnspan=4)
    label3 = Label(ticket, text ="="*65, font=("Helvetica",15, "bold","italic"),fg="green")
    label3.grid(row=2,column=0,columnspan=4)
    label4 = Label(ticket, text ="="*65, font=("Helvetica",15, "bold","italic"),fg="green")
    label4.grid(row=15,column=0,columnspan=4)
    
    #Form Widgets
    
    Cust_Name = Entry(ticket, width=30)
    Cust_Name.grid(row=3,column=1,padx=10, pady= 5, columnspan=3, sticky=W)
    Cust_Name_Label = Label(ticket, text ="ENTER NAME : ", font=("times new roman",12,"bold"), fg="brown",bd=1)
    Cust_Name_Label.grid(row=3,column=0,sticky=E,pady=5)
    Age = Entry(ticket, width=30)
    Age.grid(row=4,column=1,padx=10, columnspan=3, sticky=W)
    Age_Label = Label(ticket, text ="ENTER AGE : ", font=("times new roman",12,"bold"), fg="brown",bd=1)
    Age_Label.grid(row=4,column=0,sticky=E)
    
    #Gender Radio buttons
    gender_Value = StringVar()
    gender_Value.set("Male")
    Gender_Label = Label(ticket, text ="GENDER : ", font=("times new roman",12,"bold"), fg="brown",bd=1)
    Gender_Label.grid(row=5,column=0,sticky=E,pady=5)
    Radiobutton(ticket, text="Male", variable=gender_Value, value="Male").grid(row=5, column=1, sticky=W)
    Radiobutton(ticket, text="Female", variable=gender_Value, value="Female").grid(row=5, column=2, sticky=W)
    Radiobutton(ticket, text="Other", variable=gender_Value, value="Other").grid(row=5, column=3, sticky=W)
    
    Booking_Date = Entry(ticket, width=30)
    Booking_Date.grid(row=6,column=1,padx=10, columnspan=3, sticky=W)
    Booking_Date_Label = Label(ticket, text ="DATE OF BOOKING : ", font=("times new roman",12,"bold"), fg="brown",bd=1)
    Booking_Date_Label.grid(row=6,column=0,sticky=E)
    Journey_Date = Entry(ticket, width=30)
    Journey_Date.grid(row=7,column=1,padx=10, pady=5, columnspan=3, sticky=W)
    Journey_Date_Label = Label(ticket, text ="DATE OF JOURNEY : ", font=("times new roman",12,"bold"), fg="brown",bd=1)
    Journey_Date_Label.grid(row=7,column=0,sticky=E, pady=5)
    Starting_Location = Entry(ticket, width=30)
    Starting_Location.grid(row=8,column=1,padx=10, columnspan=3, sticky=W)
    Starting_Location_Label = Label(ticket, text ="ENTER STARTING LOCATION : ", font=("times new roman",12,"bold"), fg="brown",bd=1)
    Starting_Location_Label.grid(row=8,column=0,sticky=E)
    Destination = Entry(ticket, width=30)
    Destination.grid(row=9,column=1,padx=10, pady=5, columnspan=3, sticky=W)
    Destination_Label = Label(ticket, text ="ENTER DESTINATION : ", font=("times new roman",12,"bold"), fg="brown",bd=1)
    Destination_Label.grid(row=9,column=0,sticky=E, pady=5)
    Email_Id = Entry(ticket, width=30)
    Email_Id.grid(row=10,column=1,padx=10, columnspan=3, sticky=W)
    Email_Id_Label = Label(ticket, text ="ENTER EMAIL ID : ", font=("times new roman",12,"bold"), fg="brown",bd=1)
    Email_Id_Label.grid(row=10,column=0,sticky=E)
    Contact_No = Entry(ticket, width=30)
    Contact_No.grid(row=11,column=1,padx=10, pady=5, columnspan=3, sticky=W)
    Contact_No_Label = Label(ticket, text ="ENTER CONTACT NO. : ", font=("times new roman",12,"bold"), fg="brown",bd=1)
    Contact_No_Label.grid(row=11,column=0,sticky=E, pady=5)
    Mode_Of_Transport = Entry(ticket, width=30)
    Mode_Of_Transport.grid(row=12,column=1,padx=10, columnspan=3, sticky=W)
    Mode_Of_Transport_Label = Label(ticket, text ="ENTER MODE OF TRANSPORT : ", font=("times new roman",12,"bold"), fg="brown",bd=1)
    Mode_Of_Transport_Label.grid(row=12,column=0,sticky=E)
    Payment_Mode = Entry(ticket, width=30)
    Payment_Mode.grid(row=13,column=1,padx=10, pady=5, columnspan=3, sticky=W)
    Payment_Mode_Label = Label(ticket, text ="""ENTER MODE OF PAYMENT (UPI, CARD, NET BANKING) : """, font=("times new roman",12,"bold"), fg="brown",bd=1)
    Payment_Mode_Label.grid(row=13,column=0,sticky=E, pady=5)
    
    #Buttons
    submit_btn = Button(ticket, text= "BOOK TICKET", command= booking_Confirmation,padx=20,font=("times new roman",10,"bold"))
    submit_btn.grid(row=14,column=0,pady=5,sticky=E,padx=8)
    clear_btn = Button(ticket, text= "CLEAR ENTRIES", command= clear_Form,padx=20,font=("times new roman",10,"bold"))
    clear_btn.grid(row=14,column=1,pady=5)
    exit_btn = Button(ticket, text= "EXIT", command= ticket.destroy,padx=20,font=("times new roman",10,"bold"))
    exit_btn.grid(row=14,column=2,sticky=W,pady=5, padx=8)
    
# Function to list the places user can visit

def list_locations():
    loc_List = Toplevel()
    loc_List.title("Locations for you to visit.")
    
    # Function to search more about a specific destination
    
    def search_Dest():
        conn = sqlite3.connect('T&T_Management_System.db')
        c = conn.cursor()
        c.execute("SELECT * from dest_Info WHERE dest_Name = (:dest_Name)",{'dest_Name':dest_Name.get().capitalize()})
        records = c.fetchall()
        print_records1=''
        print_records2=''
        print_records3=''
        for record in records:
            print_records1 += str(record[0]) + "\n"
            print_records2 += str(record[1]) + "\n"
            print_records3 += str(record[2]) + "\n"
        print(records)
        
        dest_Name.delete(0, END)
        
        search_Label1 = Label(loc_List, text ='Destination Name : ', font=("times new roman",10,"bold"), fg="brown")
        search_Label1.grid(row=6,column=0,sticky=E)
        search_Label_value = Label(loc_List, text =print_records1, font=("times new roman",10,"bold"))
        search_Label_value.grid(row=6,column=1,sticky=W)
        search_Label2 = Label(loc_List, text ='Famous Place To Visit : ', font=("times new roman",10,"bold"), fg="brown",bd=1)
        search_Label2.grid(row=7,column=0,sticky=E)
        search_Label2_value = Label(loc_List, text =print_records2, font=("times new roman",10,"bold"), bd=1)
        search_Label2_value.grid(row=7,column=1,sticky=W)
        search_Label3 = Label(loc_List, text ='Famous Food : ', font=("times new roman",10,"bold"), fg="brown",bd=1)
        search_Label3.grid(row=8,column=0,sticky=E)
        search_Label3_value = Label(loc_List, text =print_records3, font=("times new roman",10,"bold"), bd=1)
        search_Label3_value.grid(row=8,column=1,sticky=W)
        
        conn.commit()
        conn.close()
        
    
    
    label2 = Label(loc_List, text ="="*55, font=("Helvetica",15, "bold","italic"),fg="green")
    label2.grid(row=0,column=0,columnspan=2)
    label3 = Label(loc_List, text =" Here's Where We Can Take You", font=("Helvetica",18, "bold","italic"),fg="blue")
    label3.grid(row=1,column=0,columnspan=2)
    label4 = Label(loc_List, text ="="*55, font=("Helvetica",15, "bold","italic"),fg="green")
    label4.grid(row=2,column=0,columnspan=2)
    
    conn = sqlite3.connect('T&T_Management_System.db')
    c = conn.cursor()
    c.execute("SELECT * from dest_Info")
    records = c.fetchall()
    print(records)
    
    print_records = ''
    for record in records:
        print_records += str(record[0]) + "\n"
        
    loc_List_Label = Label(loc_List, text=print_records, font=("Helvetica",10, "bold"))
    loc_List_Label.grid(row=3, column=0, columnspan=2)
    
    loc_Check = Label(loc_List, text ="ENTER THE NAME OF THE PLACE YOU WANT TO VISIT : ", font=("times new roman",12,"bold"), fg="brown",bd=1)
    loc_Check.grid(row=4,column=0,sticky=E,pady=10)
    dest_Name = Entry(loc_List, width=30)
    dest_Name.grid(row=4,column=1, sticky=W)
    
    
    submit_btn = Button(loc_List, text= "CHECK", command= search_Dest,padx=20,font=("times new roman",10,"bold"))
    submit_btn.grid(row=5,column=0,pady=10,sticky=E,padx=8)
    exit_btn = Button(loc_List, text= "EXIT", command= loc_List.destroy,padx=20,font=("times new roman",10,"bold"))
    exit_btn.grid(row=5,column=1,sticky=W,pady=10)
    
    
    
    label5 = Label(loc_List, text ="="*55, font=("Helvetica",15, "bold","italic"),fg="green")
    label5.grid(row=9,column=0,columnspan=2)
    
    conn.commit()
    conn.close()

# Traveller Portal

def traveller_Func():
    traveller_Sec = Toplevel()
    traveller_Sec.title("Tours and Travels Management System-Traveller's Portal")
    
# Welcome Message
    
    label = Label(traveller_Sec, text ="~"*60, font=("Helvetica",15, "bold","italic"),fg="green")
    label.grid(row=0,column=0,columnspan=2)
    label2 = Label(traveller_Sec, text ="="*60, font=("Helvetica",15, "bold","italic"),fg="green")
    label2.grid(row=1,column=0,columnspan=2)
    label3 = Label(traveller_Sec, text =" WELCOME TO TRAVELLER'S PORTAL", font=("Helvetica",18, "bold","italic"),fg="blue")
    label3.grid(row=2,column=0,columnspan=2)
    label4 = Label(traveller_Sec, text ="="*60, font=("Helvetica",15, "bold","italic"),fg="green")
    label4.grid(row=3,column=0,columnspan=2)
    label5 = Label(traveller_Sec, text ="="*60, font=("Helvetica",15, "bold","italic"),fg="green")
    label5.grid(row=4,column=0,columnspan=2)
    label6 = Label(traveller_Sec, text =" HERE's WHAT WE CAN DO FOR YOU", font=("Helvetica",18, "bold","italic"),fg="blue")
    label6.grid(row=5,column=0,columnspan=2)
    label7 = Label(traveller_Sec, text ="="*60, font=("Helvetica",15, "bold","italic"),fg="green")
    label7.grid(row=6,column=0,columnspan=2)
    label8 = Label(traveller_Sec, text ="~"*60, font=("Helvetica",15, "bold","italic"),fg="green")
    label8.grid(row=7,column=0,columnspan=2) 
    
#Traveller Options

    loc_List = Label(traveller_Sec, text ="TO SEE THE PLACES YOU CAN VISIT : ", font=("times new roman",12,"bold"), fg="brown",bd=1)
    loc_List.grid(row=8,column=0,sticky=E,pady=10)
    booking = Label(traveller_Sec, text ="TO BOOK YOUR JOURNEY : ", font=("times new roman",12,"bold"), fg="brown", bd=1)
    booking.grid(row=9,column=0,sticky=E)
    
    loc_List_btn = Button(traveller_Sec, text = "TRAVEL LOCATIONS",font=("times new roman",10,"bold"), command= list_locations)
    booking_btn = Button(traveller_Sec, text = "TICKET BOOKING",font=("times new roman",10,"bold"), command=book_tickets)
    exit_btn = Button(traveller_Sec, text= "EXIT", command= traveller_Sec.destroy,padx=20,font=("times new roman",10,"bold"))
    loc_List_btn.grid(row=8,column=1,sticky=W)
    booking_btn.grid(row=9,column=1,sticky=W)
    exit_btn.grid(row=10,column=0,columnspan=2,pady=10)
    
# Travel Agent Portal

def agent_Func():
    agent_Sec = Toplevel()
    agent_Sec.title("Tours and Travels Management System-Travel Agent's Portal")
    
    # Function to Delete Records from ticket_Booking table
    def delete_Records():
        
        def delete_Entry():
            conn = sqlite3.connect('T&T_Management_System.db')
            c = conn.cursor()
            c.execute("DELETE FROM ticket_Booking WHERE oid = (:oid)",{'oid':record.get()})
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","ENTRY DELETED SUCCESSFULLY", parent=login)
            delete.destroy()
            
            
        delete = Toplevel()
        delete.title("Delete Records")
        label1 = Label(delete, text ="="*70, font=("Helvetica",12, "bold","italic"),fg="green")
        label1.grid(row=0,column=0,columnspan=2)
        label2 = Label(delete, text ="DELETE RECORDS", font=("Helvetica",15, "bold","italic"),fg="blue")
        label2.grid(row=1,column=0,columnspan=2)
        label3 = Label(delete, text ="="*70, font=("Helvetica",12, "bold","italic"),fg="green")
        label3.grid(row=2,column=0,columnspan=2)
        
        record = Entry(delete, width=30)
        record.grid(row=3,column=1,padx=10, pady= 5, columnspan=3, sticky=W)
        record_Label = Label(delete, text ="ENTER OID OF RECORD YOU WANT TO DELETE : ", font=("times new roman",12,"bold"), fg="brown",bd=1)
        record_Label.grid(row=3,column=0,sticky=E,pady=5)
        
        delete_btn = Button(delete, text= "DELETE",padx=20,font=("times new roman",10,"bold"), command=delete_Entry)
        delete_btn.grid(row=4,column=0,pady=(5,10),sticky=E,padx=8)
        exit_btn = Button(delete, text= "EXIT", command= delete.destroy,padx=20,font=("times new roman",10,"bold"))
        exit_btn.grid(row=4,column=1,sticky=W,pady=(5,10))
        
    # Function for searching for a specific record in ticket_Booking table
    def search_Records():
        def search_Entry():
            conn = sqlite3.connect('T&T_Management_System.db')
            c = conn.cursor()
            c.execute("SELECT *,oid FROM ticket_Booking WHERE oid = (:oid)",{'oid':record.get()})
            records = c.fetchall()
            conn.commit()
            conn.close()
            if records == []:
                messagebox.showerror("Error", "No Entry Found",parent=search)
            else:
                OID = ''
                NAME = ''
                AGE = ''
                GENDER = ''
                BOOKING_DATE = ''
                JOURNEY_DATE = ''
                STARTING_LOCATION = ''
                DESTINATION = ''
                EMAIL_ID = ''
                CONTACT_NO = ''
                TRANSPORT = ''
                PAYMENT = ''
                for r in records:
                    NAME += r[0] + "\n"
                    AGE += str(r[1]) + "\n"
                    GENDER += r[2] + "\n"
                    BOOKING_DATE += str(r[3]) + "\n"
                    JOURNEY_DATE += str(r[4]) + "\n"
                    STARTING_LOCATION += r[5] + "\n"
                    DESTINATION += r[6] + "\n"
                    EMAIL_ID += r[7] + "\n"
                    CONTACT_NO += str(r[8]) + "\n"
                    TRANSPORT += r[9] + "\n"
                    PAYMENT += r[10] + "\n"
                    OID += str(r[11]) + "\n"
                    
                entry_Found = Toplevel()
                entry_Found.title("Record Found")
                
                label1 = Label(entry_Found, text ="="*50, font=("Helvetica",12, "bold","italic"),fg="green")
                label1.grid(row=0,column=0,columnspan=2)
                label2 = Label(entry_Found, text ="="*50, font=("Helvetica",12, "bold","italic"),fg="green")
                label2.grid(row=15,column=0,columnspan=2)
                
                OID_Label = Label(entry_Found, text ="OID : ", font=("times new roman",12,"bold"), fg="brown",bd=1)
                OID_Label.grid(row=2,column=0,sticky=E,pady=5)
                OID_Label_Value = Label(entry_Found, text =OID, font=("times new roman",12,"bold"), fg="blue",bd=1)
                OID_Label_Value.grid(row=2,column=1,sticky=W,pady=5)
                Cust_Name_Label = Label(entry_Found, text ="NAME : ", font=("times new roman",12,"bold"), fg="brown",bd=1)
                Cust_Name_Label.grid(row=3,column=0,sticky=E,pady=5)
                Cust_Name_Label_Value = Label(entry_Found, text =NAME, font=("times new roman",12,"bold"), fg="blue",bd=1)
                Cust_Name_Label_Value.grid(row=3,column=1,sticky=W,pady=5)
                Age_Label = Label(entry_Found, text ="AGE : ", font=("times new roman",12,"bold"), fg="brown",bd=1)
                Age_Label.grid(row=4,column=0,sticky=E,pady=5)
                Age_Label_Value = Label(entry_Found, text =AGE, font=("times new roman",12,"bold"), fg="blue",bd=1)
                Age_Label_Value.grid(row=4,column=1,sticky=W,pady=5)
                Gender_Label = Label(entry_Found, text ="GENDER : ", font=("times new roman",12,"bold"), fg="brown",bd=1)
                Gender_Label.grid(row=5,column=0,sticky=E,pady=5)
                Gender_Label_Value = Label(entry_Found, text =GENDER, font=("times new roman",12,"bold"), fg="blue",bd=1)
                Gender_Label_Value.grid(row=5,column=1,sticky=W,pady=5)
                Booking_Date_Label = Label(entry_Found, text ="DATE OF BOOKING : ", font=("times new roman",12,"bold"), fg="brown",bd=1)
                Booking_Date_Label.grid(row=6,column=0,sticky=E,pady=5)
                Booking_Date_Label_Value = Label(entry_Found, text =BOOKING_DATE, font=("times new roman",12,"bold"), fg="blue",bd=1)
                Booking_Date_Label_Value.grid(row=6,column=1,sticky=W,pady=5)
                Journey_Date_Label = Label(entry_Found, text ="DATE OF JOURNEY : ", font=("times new roman",12,"bold"), fg="brown",bd=1)
                Journey_Date_Label.grid(row=7,column=0,sticky=E,pady=5)
                Journey_Date_Label_Value = Label(entry_Found, text =JOURNEY_DATE, font=("times new roman",12,"bold"), fg="blue",bd=1)
                Journey_Date_Label_Value.grid(row=7,column=1,sticky=W,pady=5)
                Starting_Location_Label = Label(entry_Found, text ="STARTING LOCATION : ", font=("times new roman",12,"bold"), fg="brown",bd=1)
                Starting_Location_Label.grid(row=8,column=0,sticky=E,pady=5)
                Starting_Location_Label_Value = Label(entry_Found, text =STARTING_LOCATION, font=("times new roman",12,"bold"), fg="blue",bd=1)
                Starting_Location_Label_Value.grid(row=8,column=1,sticky=W,pady=5)
                Destination_Label = Label(entry_Found, text ="DESTINATION : ", font=("times new roman",12,"bold"), fg="brown",bd=1)
                Destination_Label.grid(row=9,column=0,sticky=E,pady=5)
                Destination_Label_Value = Label(entry_Found, text =DESTINATION, font=("times new roman",12,"bold"), fg="blue",bd=1)
                Destination_Label_Value.grid(row=9,column=1,sticky=W,pady=5)
                Email_Id_Label = Label(entry_Found, text ="E_MAIL ID : ", font=("times new roman",12,"bold"), fg="brown",bd=1)
                Email_Id_Label.grid(row=10,column=0,sticky=E,pady=5)
                Email_Id_Label_Value = Label(entry_Found, text =EMAIL_ID, font=("times new roman",12,"bold"), fg="blue",bd=1)
                Email_Id_Label_Value.grid(row=10,column=1,sticky=W,pady=5)
                Contact_No_Label = Label(entry_Found, text ="CONTACT NO. : ", font=("times new roman",12,"bold"), fg="brown",bd=1)
                Contact_No_Label.grid(row=11,column=0,sticky=E,pady=5)
                Contact_No_Label_Value = Label(entry_Found, text =CONTACT_NO, font=("times new roman",12,"bold"), fg="blue",bd=1)
                Contact_No_Label_Value.grid(row=11,column=1,sticky=W,pady=5)
                Mode_Of_Transport_Label = Label(entry_Found, text ="MODE OF TRANSPORT : ", font=("times new roman",12,"bold"), fg="brown",bd=1)
                Mode_Of_Transport_Label.grid(row=12,column=0,sticky=E,pady=5)
                Mode_Of_Transport_Label_Value = Label(entry_Found, text =TRANSPORT, font=("times new roman",12,"bold"), fg="blue",bd=1)
                Mode_Of_Transport_Label_Value.grid(row=12,column=1,sticky=W,pady=5)
                Payment_Mode_Label = Label(entry_Found, text ="MODE OF PAYMENT : ", font=("times new roman",12,"bold"), fg="brown",bd=1)
                Payment_Mode_Label.grid(row=13,column=0,sticky=E,pady=5)
                Payment_Mode_Label_Value = Label(entry_Found, text =PAYMENT, font=("times new roman",12,"bold"), fg="blue",bd=1)
                Payment_Mode_Label_Value.grid(row=13,column=1,sticky=W,pady=5)
                
                exit_btn = Button(entry_Found, text= "OK", command= entry_Found.destroy,padx=20,font=("times new roman",10,"bold"))
                exit_btn.grid(row=14,column=0,columnspan=2,pady=(5,10))
                
            
            
        search = Toplevel()
        search.title("Search Records")
        label1 = Label(search, text ="="*70, font=("Helvetica",12, "bold","italic"),fg="green")
        label1.grid(row=0,column=0,columnspan=2)
        label2 = Label(search, text ="SEARCH RECORDS", font=("Helvetica",15, "bold","italic"),fg="blue")
        label2.grid(row=1,column=0,columnspan=2)
        label3 = Label(search, text ="="*70, font=("Helvetica",12, "bold","italic"),fg="green")
        label3.grid(row=2,column=0,columnspan=2)
        
        record = Entry(search, width=30)
        record.grid(row=3,column=1,padx=10, pady= 5, columnspan=3, sticky=W)
        record_Label = Label(search, text ="ENTER OID OF RECORD YOU WANT TO SEARCH : ", font=("times new roman",12,"bold"), fg="brown",bd=1)
        record_Label.grid(row=3,column=0,sticky=E,pady=5)
        
        search_btn = Button(search, text= "SEARCH",padx=20,font=("times new roman",10,"bold"), command=search_Entry)
        search_btn.grid(row=4,column=0,pady=(5,10),sticky=E,padx=8)
        exit_btn = Button(search, text= "EXIT", command= search.destroy,padx=20,font=("times new roman",10,"bold"))
        exit_btn.grid(row=4,column=1,sticky=W,pady=(5,10))
    
    # Function to add new Destinations to dest_Info table
    def add_Destinations():
        def add_New_Dest():
            response = messagebox.askyesno("CONFIRMATION!!!","""(Please Check all the details before Submitting)
                                           DO YOU WANT TO CONTINUE ?""",parent=new_Dest)
            if response == 1:
                conn = sqlite3.connect('T&T_Management_System.db')
                c = conn.cursor()
                c.execute("INSERT INTO dest_Info VALUES(:dest_Name, :famous_Place, :famous_Food)",
                          {
                              'dest_Name': dest_Name.get().capitalize(),
                              'famous_Place': famous_Place.get().capitalize(),
                              'famous_Food': famous_Food.get().capitalize()
                          })
                conn.commit()
                conn.close()
                confirmation = messagebox.showinfo("Sone", "NEW DESTINATION ADDED SUCCESSFULLY !!!",parent=new_Dest)
                if confirmation == "ok":
                    new_Dest.destroy()
                else:
                    pass
        new_Dest = Toplevel()
        new_Dest.title("Add New Destination")
        
        label1 = Label(new_Dest, text ="="*50, font=("Helvetica",12, "bold","italic"),fg="green")
        label1.grid(row=0,column=0,columnspan=2)
        label2 = Label(new_Dest, text ="ADD DESTINATION DETAILS", font=("Helvetica",15, "bold","italic"),fg="blue")
        label2.grid(row=1,column=0,columnspan=2)
        label3 = Label(new_Dest, text ="="*50, font=("Helvetica",12, "bold","italic"),fg="green")
        label3.grid(row=2,column=0,columnspan=2)
        
        dest_Name = Entry(new_Dest, width=30)
        dest_Name.grid(row=3,column=1,padx=10, pady= 5, columnspan=3, sticky=W)
        dest_Name_Label = Label(new_Dest, text ="ENTER DESTINATION NAME : ", font=("times new roman",12,"bold"), fg="brown",bd=1)
        dest_Name_Label.grid(row=3,column=0,sticky=E,pady=5)
        famous_Place = Entry(new_Dest, width=30)
        famous_Place.grid(row=4,column=1,padx=10, columnspan=3, sticky=W)
        famous_Place_Label = Label(new_Dest, text ="ENTER FAMOUS PLACE : ", font=("times new roman",12,"bold"), fg="brown",bd=1)
        famous_Place_Label.grid(row=4,column=0,sticky=E)
        famous_Food = Entry(new_Dest, width=30)
        famous_Food.grid(row=5,column=1,padx=10, columnspan=3, sticky=W)
        famous_Food_Label = Label(new_Dest, text ="ENTER FAMOUS FOOD : ", font=("times new roman",12,"bold"), fg="brown",bd=1)
        famous_Food_Label.grid(row=5,column=0,sticky=E)
        
        submit_btn = Button(new_Dest, text= "OK",padx=20,font=("times new roman",10,"bold"), command=add_New_Dest)
        submit_btn.grid(row=6,column=0,pady=(5,10),sticky=E,padx=8)
        exit_btn = Button(new_Dest, text= "EXIT", command= new_Dest.destroy,padx=20,font=("times new roman",10,"bold"))
        exit_btn.grid(row=6,column=1,sticky=W,pady=(5,10))
    
    # Function for data Visualization
    def view_Statistics():
        
        def age_Bar_Graph():
            conn = sqlite3.connect('T&T_Management_System.db')
            c = conn.cursor()
            c.execute("SELECT Age,Destination FROM ticket_Booking")
            responses = c.fetchall()
            print(responses)
            conn.commit()
            conn.close()
            AGE = []
            DEST = []
            for response in responses:
                AGE.append(response[0])
                DEST.append(response[1])
                 
            plt.bar(DEST,AGE,facecolor='lime')
            #plt.xticks(rotation='vertical')
            plt.xlabel('DESTINATIONS')
            plt.ylabel('AGE GROUPS VISITING')
            plt.title('DESTINATIONS VISITED BY DIFFERENT AGE GROUPS')
            plt.show()
            
        def dest_Hist():
            conn = sqlite3.connect('T&T_Management_System.db')
            c = conn.cursor()
            c.execute("SELECT Destination FROM ticket_Booking")
            responses = c.fetchall()
            print(responses)
            conn.commit()
            conn.close()
            DEST = []
            for response in responses:
                DEST.append(response[0])
            
            plt.hist(DEST,facecolor='red')
            #plt.xticks(rotation='vertical')
            plt.xlabel('DESTINATIONS')
            plt.ylabel('FREQUENCY')
            plt.title('FREQUENCY OF DESTINATIONS VISITED BY PEOPLE')
            plt.show()

        stats = Toplevel()
        stats.title("Data Visualization")
        
        label1 = Label(stats, text ="="*85, font=("Helvetica",12, "bold","italic"),fg="green")
        label1.grid(row=0,column=0,columnspan=2)
        label2 = Label(stats, text ="STATISTICS", font=("Helvetica",15, "bold","italic"),fg="blue")
        label2.grid(row=1,column=0,columnspan=2)
        label3 = Label(stats, text ="="*85, font=("Helvetica",12, "bold","italic"),fg="green")
        label3.grid(row=2,column=0,columnspan=2)
        
        age_Dest_Graph = Label(stats, text ="BAR GRAPH OF DESTINATIONS VISITED BY DIFFERENT AGE GROUPS : ", font=("times new roman",12,"bold"), fg="brown", bd=1)
        age_Dest_Graph.grid(row=3,column=0,sticky=E,pady=(5,0))
        age_Dest_Graph_btn = Button(stats, text = "SHOW GRAPH",font=("times new roman",10,"bold"), command=age_Bar_Graph,padx=20)
        age_Dest_Graph_btn.grid(row=3,column=1,sticky=W,pady=(5,0))
        dest_Histogram = Label(stats, text ="HISTOGRAM FOR MOST VISITED DESTINATION : ", font=("times new roman",12,"bold"), fg="brown", bd=1)
        dest_Histogram.grid(row=4,column=0,sticky=E,pady=(5,0))
        dest_Histogram_btn = Button(stats, text = "SHOW HISTOGRAM",font=("times new roman",10,"bold"), command=dest_Hist,padx=7)
        dest_Histogram_btn.grid(row=4,column=1,sticky=W,pady=(5,0))
        exit_btn = Button(stats, text= "EXIT", command= stats.destroy,padx=20,font=("times new roman",10,"bold"))
        exit_btn.grid(row=5,column=0,columnspan=2,pady=10)

    
    # Agent Login Function
    def agent_login():
        login = Toplevel()
        login.title("Agent Login")
        
        def user_Authentication():
            conn = sqlite3.connect('T&T_Management_System.db')
            c = conn.cursor()
            c.execute("SELECT First_Name,Last_Name FROM agent_Info WHERE Username = (:Username) AND Password = (:Password)",{'Username':Username.get(),'Password':Password.get()})
            responses = c.fetchall()
            conn.commit()
            conn.close() 
        
            if responses == []:
                messagebox.showerror("Error","Invalid Username or Password", parent=login)
                login.destroy()
            else:
                agent_Sec.destroy()
                login.destroy()
                agent_Options = Toplevel()
                agent_Options.title("Welcome Agent")
                firstname=''
                lastname=''
                for response in responses:
                    firstname += response[0]
                    lastname += response[1]
                label1 = Label(agent_Options, text ="="*50, font=("Helvetica",12, "bold","italic"),fg="green")
                label1.grid(row=0,column=0,columnspan=2)
                label2 = Label(agent_Options, text ="WELCOME"+" "+firstname.upper()+" "+lastname.upper(), font=("Helvetica",15, "bold","italic"),fg="blue")
                label2.grid(row=1,column=0,columnspan=2)
                label3 = Label(agent_Options, text ="="*50, font=("Helvetica",12, "bold","italic"),fg="green")
                label3.grid(row=2,column=0,columnspan=2)
                
                booking = Label(agent_Options, text ="TO BOOK TICKETS : ", font=("times new roman",12,"bold"), fg="brown", bd=1)
                booking.grid(row=3,column=0,sticky=E,pady=(5,0))
                booking_btn = Button(agent_Options, text = "TICKET BOOKING",font=("times new roman",10,"bold"), command=book_tickets,padx=8)
                booking_btn.grid(row=3,column=1,sticky=W,pady=(5,0))
                delete = Label(agent_Options, text ="TO DELETE RECORDS : ", font=("times new roman",12,"bold"), fg="brown", bd=1)
                delete.grid(row=4,column=0,sticky=E,pady=(5,0))
                delete_btn = Button(agent_Options, text = "DELETE RECORDS",font=("times new roman",10,"bold"), command=delete_Records,padx=7)
                delete_btn.grid(row=4,column=1,sticky=W,pady=(5,0))
                search = Label(agent_Options, text ="TO SEARCH A SPECIFIC RECORD : ", font=("times new roman",12,"bold"), fg="brown", bd=1)
                search.grid(row=5,column=0,sticky=E,pady=(5,0))
                search_btn = Button(agent_Options, text = "SEARCH RECORD",font=("times new roman",10,"bold"), command=search_Records, padx= 8)
                search_btn.grid(row=5,column=1,sticky=W,pady=(5,0))
                destination = Label(agent_Options, text ="TO ADD NEW DESTINATIONS : ", font=("times new roman",12,"bold"), fg="brown", bd=1)
                destination.grid(row=6,column=0,sticky=E,pady=(5,0))
                destination_btn = Button(agent_Options, text = "ADD DESTINATION",font=("times new roman",10,"bold"), command=add_Destinations,padx=3)
                destination_btn.grid(row=6,column=1,sticky=W,pady=(5,0))
                statistics = Label(agent_Options, text ="TO VIEW STATISTICS : ", font=("times new roman",12,"bold"), fg="brown", bd=1)
                statistics.grid(row=7,column=0,sticky=E,pady=(5,0))
                statistics_btn = Button(agent_Options, text = "STATS",font=("times new roman",10,"bold"), command=view_Statistics, padx=40)
                statistics_btn.grid(row=7,column=1,sticky=W,pady=(5))
                exit_btn = Button(agent_Options, text= "EXIT", command= agent_Options.destroy,padx=20,font=("times new roman",10,"bold"))
                exit_btn.grid(row=8,column=0,columnspan=2,pady=10)
                
                 
            
        label1 = Label(login, text ="="*50, font=("Helvetica",12, "bold","italic"),fg="green")
        label1.grid(row=0,column=0,columnspan=2)
        label2 = Label(login, text ="AGENT LOGIN", font=("Helvetica",15, "bold","italic"),fg="blue")
        label2.grid(row=1,column=0,columnspan=2)
        label3 = Label(login, text ="="*50, font=("Helvetica",12, "bold","italic"),fg="green")
        label3.grid(row=2,column=0,columnspan=2)
        
        Username = Entry(login, width=30)
        Username.grid(row=3,column=1,padx=10, pady= 5, columnspan=3, sticky=W)
        Username_Label = Label(login, text ="ENTER USERNAME : ", font=("times new roman",12,"bold"), fg="brown",bd=1)
        Username_Label.grid(row=3,column=0,sticky=E,pady=5)
        Password = Entry(login, width=30)
        Password.grid(row=4,column=1,padx=10, columnspan=3, sticky=W)
        Password_Label = Label(login, text ="ENTER PASSWORD : ", font=("times new roman",12,"bold"), fg="brown",bd=1)
        Password_Label.grid(row=4,column=0,sticky=E)
                
        submit_btn = Button(login, text= "LOGIN",padx=20,font=("times new roman",10,"bold"), command=user_Authentication)
        submit_btn.grid(row=7,column=0,pady=5,sticky=E,padx=8)
        exit_btn = Button(login, text= "EXIT", command= login.destroy,padx=20,font=("times new roman",10,"bold"))
        exit_btn.grid(row=7,column=1,sticky=W,pady=5)
    
    
    # Agent Registration Function
    def agent_registration():
        admin = Toplevel()
        admin.title("Admin Authentication...")
        
        def admin_Authentication():
            def registration_Confirmation():
                submit_response = messagebox.askyesno("CONFIRMATION!!!", """(Please check your entries before Submitting)
                                          DO YOU WANT TO SUBMIT ? """,parent=registration)
    
                if submit_response == 1:
                    conn = sqlite3.connect('T&T_Management_System.db')
                    c = conn.cursor()
                    c.execute("INSERT INTO agent_Info VALUES(:First_Name, :Last_Name, :Username, :Password)",
                    {
                      'First_Name':First_Name.get().capitalize(),
                      'Last_Name':Last_Name.get().capitalize(),
                      'Username':Username.get(),
                      'Password':Password.get(),
                      })
                    conn.commit()
                    conn.close()
                    confirmation = messagebox.showinfo("Thanks for Registration", "RESTRATION SUCCESSFULL !!!",parent=registration)
                    if confirmation == "ok":
                        registration.destroy()
                    else:
                        pass
                    
            if admin_Password_Entry.get() == "Travel@123":
                admin.destroy()
                registration = Toplevel()
                registration.title("Agent Registration...")
                
                label1 = Label(registration, text ="="*50, font=("Helvetica",12, "bold","italic"),fg="green")
                label1.grid(row=0,column=0,columnspan=2)
                label2 = Label(registration, text ="REGISTRATION", font=("Helvetica",15, "bold","italic"),fg="blue")
                label2.grid(row=1,column=0,columnspan=2)
                label3 = Label(registration, text ="="*50, font=("Helvetica",12, "bold","italic"),fg="green")
                label3.grid(row=2,column=0,columnspan=2)
                
                First_Name = Entry(registration, width=30)
                First_Name.grid(row=3,column=1,padx=10, pady= 5, columnspan=3, sticky=W)
                First_Name_Label = Label(registration, text ="ENTER FIRST NAME : ", font=("times new roman",12,"bold"), fg="brown",bd=1)
                First_Name_Label.grid(row=3,column=0,sticky=E,pady=5)
                Last_Name = Entry(registration, width=30)
                Last_Name.grid(row=4,column=1,padx=10, columnspan=3, sticky=W)
                Last_Name_Label = Label(registration, text ="ENTER LAST NAME : ", font=("times new roman",12,"bold"), fg="brown",bd=1)
                Last_Name_Label.grid(row=4,column=0,sticky=E)
                Username = Entry(registration, width=30)
                Username.grid(row=5,column=1,padx=10, pady= 5, columnspan=3, sticky=W)
                Username_Label = Label(registration, text ="ENTER USERNAME : ", font=("times new roman",12,"bold"), fg="brown",bd=1)
                Username_Label.grid(row=5,column=0,sticky=E,pady=5)
                Password = Entry(registration, width=30)
                Password.grid(row=6,column=1,padx=10, columnspan=3, sticky=W)
                Password_Label = Label(registration, text ="ENTER PASSWORD : ", font=("times new roman",12,"bold"), fg="brown",bd=1)
                Password_Label.grid(row=6,column=0,sticky=E)
                
                submit_btn = Button(registration, text= "REGISTER", command= registration_Confirmation,padx=20,font=("times new roman",10,"bold"))
                submit_btn.grid(row=7,column=0,pady=5,sticky=E,padx=8)
                exit_btn = Button(registration, text= "EXIT", command= registration.destroy,padx=20,font=("times new roman",10,"bold"))
                exit_btn.grid(row=7,column=1,sticky=W,pady=5)
                
            else:
                messagebox.showerror("Authentication Failed!","Invalid Password",parent=admin)
                admin.destroy()
                
        label1 = Label(admin, text ="="*60, font=("Helvetica",12, "bold","italic"),fg="green")
        label1.grid(row=0,column=0,columnspan=2)
        label2 = Label(admin, text ="AUTHENTICATION", font=("Helvetica",15, "bold","italic"),fg="blue")
        label2.grid(row=1,column=0,columnspan=2)
        label3 = Label(admin, text ="="*60, font=("Helvetica",12, "bold","italic"),fg="green")
        label3.grid(row=2,column=0,columnspan=2)
        
        admin_Password = Label(admin, text ="ENTER ADMIN PASSWORD : ", font=("times new roman",12,"bold"), fg="brown",bd=1)
        admin_Password.grid(row=3, column=0, sticky=E,padx=10)
        admin_Password_Entry = Entry(admin, width=30)
        admin_Password_Entry.grid(row=3,column=1,padx=10, pady= 5, columnspan=3, sticky=W)
        
        submit_btn = Button(admin, text= "ENTER", command= admin_Authentication,padx=20,font=("times new roman",10,"bold"))
        submit_btn.grid(row=4,column=0,pady=5,sticky=E,padx=8)
        exit_btn = Button(admin, text= "EXIT", command= admin.destroy,padx=20,font=("times new roman",10,"bold"))
        exit_btn.grid(row=4,column=1,sticky=W,pady=5, padx=8)
        
    
    # Welcome Message
    
    label = Label(agent_Sec, text ="~"*60, font=("Helvetica",15, "bold","italic"),fg="green")
    label.grid(row=0,column=0,columnspan=2)
    label2 = Label(agent_Sec, text ="="*60, font=("Helvetica",15, "bold","italic"),fg="green")
    label2.grid(row=1,column=0,columnspan=2)
    label3 = Label(agent_Sec, text =" WELCOME TO TRAVEL AGENT PORTAL", font=("Helvetica",18, "bold","italic"),fg="blue")
    label3.grid(row=2,column=0,columnspan=2)
    label4 = Label(agent_Sec, text ="="*60, font=("Helvetica",15, "bold","italic"),fg="green")
    label4.grid(row=3,column=0,columnspan=2)
    label5 = Label(agent_Sec, text ="~"*60, font=("Helvetica",15, "bold","italic"),fg="green")
    label5.grid(row=4,column=0,columnspan=2)
    
    #Travel Agent Login/Signup

    login = Label(agent_Sec, text ="IF YOU ARE AN EXISTING TRAVEL AGENT : ", font=("times new roman",12,"bold"), fg="brown",bd=1)
    login.grid(row=8,column=0,sticky=E,pady=10)
    sign_Up = Label(agent_Sec, text ="IF YOU ARE A NEW TRAVEL AGENT : ", font=("times new roman",12,"bold"), fg="brown", bd=1)
    sign_Up.grid(row=9,column=0,sticky=E)
    
    login_btn = Button(agent_Sec, text = "LOGIN",font=("times new roman",10,"bold"),command=agent_login)
    sign_Up_btn = Button(agent_Sec, text = "SIGN UP",font=("times new roman",10,"bold"), command=agent_registration)
    exit_btn = Button(agent_Sec, text= "EXIT", command= agent_Sec.destroy,padx=20,font=("times new roman",10,"bold"))
    login_btn.grid(row=8,column=1,sticky=W)
    sign_Up_btn.grid(row=9,column=1,sticky=W)
    exit_btn.grid(row=10,column=0,columnspan=2,pady=10)