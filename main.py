# Libraries used
from tkinter import *
import utilities

root=Tk()
root.title("Tours and Travels Management System")
root.iconbitmap("C:\\Users\\raj31\\Downloads\\python tkinter\\images\\icon1.ico")


# Welcome Page

# Welcome Messager  

label = Label(root, text ="~"*60, font=("Helvetica",15, "bold","italic"),fg="green")
label.grid(row=0,column=0,columnspan=2)
label2 = Label(root, text ="="*60, font=("Helvetica",15, "bold","italic"),fg="green")
label2.grid(row=1,column=0,columnspan=2)
label3 = Label(root, text ="WELCOME TO TOURS AND TRAVELS MANAGEMENT SYSTEM", font=("Helvetica",18, "bold","italic"),fg="blue")
label3.grid(row=2,column=0,columnspan=2)
label4 = Label(root, text ="="*60, font=("Helvetica",15, "bold","italic"),fg="green")
label4.grid(row=3,column=0,columnspan=2)
label5 = Label(root, text ="~"*60, font=("Helvetica",15, "bold","italic"),fg="green")
label5.grid(row=4,column=0,columnspan=2)

# Welcome Options

traveller = Label(root, text ="IF YOU ARE A TRAVELLER : ", font=("times new roman",12,"bold"), fg="brown",bd=1)
traveller.grid(row=5,column=0,sticky=E,pady=10)
agent = Label(root, text ="IF YOU ARE A TRAVEL AGENT : ", font=("times new roman",12,"bold"), fg="brown", bd=1)
agent.grid(row=6,column=0,sticky=E)

traveller_btn = Button(root, text = "TRAVELLER...",font=("times new roman",10,"bold"), command = utilities.traveller_Func)
agent_btn = Button(root, text = "TRAVEL AGENT...",font=("times new roman",10,"bold"), command= utilities.agent_Func)
exit_btn = Button(root, text= "EXIT", command= root.quit,padx=20,font=("times new roman",10,"bold"))
traveller_btn.grid(row=5,column=1,sticky=W)
agent_btn.grid(row=6,column=1,sticky=W)
exit_btn.grid(row=7,column=0,columnspan=2,pady=10)



root.mainloop()