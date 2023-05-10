from tkinter import *
root=Tk()
root.state('zoomed')
img=PhotoImage(file="Bus_for_Project.png")
Label(root,image=img).grid(row=0,column=0,columnspan=10)
Label(root,text="Online Bus Booking System",font=("Ariel",40),bg="light blue",fg="red" ).grid(row=1,column=0,columnspan=10,padx=440)
def close():
    root.destroy()
    import seat_booking
b1=Button(root,text="Seat Booking",font=('Ariel',20),bg="light green",command=close).grid(row=2,column=1,pady=100,columnspan=4)
def close1():
    root.destroy()
    import check_booking
b2=Button(root,text="Check Booked Seat",font=('Ariel',20),bg="green3",command=close1).grid(row=2,column=4,pady=100,columnspan=2)
def close2():
    root.destroy()
    import add_new_detail
b3=Button(root,text="Add Bus Details",font=('Ariel',20),bg="green",command=close2).grid(row=2,column=6,columnspan=3)
Label(root,text="For Admin Only",font=("Ariel",12),fg="red").grid(row=4,column=5,columnspan=10)

root.mainloop()
