from tkinter import *
root=Tk()
root.state('zoomed')
img=PhotoImage(file='Bus_for_project.png')
Label(root,image=img).grid(row=0,column=8,padx=600)
Label(root,text="Online Bus Booking System",font=("Ariel",40),bg="light blue",fg="red" ).grid(row=1,column=8,pady=30)
Label(root,text="Name:Abhishek Pandey",font=("Ariel",16),fg="blue" ).grid(row=2,column=8,pady=30)
Label(root,text="Er:211B014",font=("Ariel",16),fg="blue" ).grid(row=3,column=8,pady=20)
Label(root,text="Mobile:7024655061",font=("Ariel",16),fg="blue" ).grid(row=4,column=8,pady=20)
Label(root,text="Submitted to: Dr.Mahesh Kumar",font=("Ariel",16),bg="light blue",fg="red" ).grid(row=5,column=8,pady=10)
Label(root,text="Project Based Learning ",font=("Ariel",16),fg="red" ).grid(row=6,column=8,pady=5)
def close():
     root.destroy()
     import home
root.after(5000,close)     
root.mainloop()
