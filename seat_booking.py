from tkinter import *
from tkinter.messagebox import*
root=Tk()
root.state('zoomed')
img=PhotoImage(file=".\\Bus_for_project.png")
img1=PhotoImage(file=".\\home (1).png")
Label(root,image=img).grid(row=0,column=0,columnspan=40)
Label(root,text="Online Bus Booking System",font=("Ariel",40),bg="light blue",fg="red" ).grid(row=1,column=0,columnspan=30,padx=440)
Label(root,text="Enter Journey Details",font=("Ariel",20),bg="green",fg="light green" ).grid(row=2,column=0,columnspan=30,padx=400,pady=50)
def fun1():
    if To.get()=='':
        showerror('value error ','enter To ')
    elif From.get()=='':
        showerror('value error','enter From ')
    elif Jd.get()=='':
        showerror('value error','enter Journey date')
    

To=Label(root,text="To",font=("Ariel")).grid(row=3,column=1,columnspan=1,padx=70)
To=Entry(root,font=("Ariel",16))
To.grid(row=3,column=3)
Label(root,text="From",font=("Ariel")).grid(row=3,column=4)
From=Entry(root,font=("Ariel",16))
From.grid(row=3,column=5)
Label(root,text="Journey Date",font=("Ariel")).grid(row=3,column=6)
Jd=Entry(root,font=("Ariel",16))
Jd.grid(row=3,column=7)
Button(root,text="Seat Booking",command=fun1,font=('Ariel',16),bg="light green").grid(row=3,column=8)
def close():
    root.destroy()
    import home
Button(root,image=img1,font=('Ariel',16),bg="light green",command=close).grid(row=3,column=9)
root.mainloop()

    

     
     




