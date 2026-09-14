from tkinter import *
import tkinter.messagebox as tmsg

root=Tk()
root.geometry("400x400")
root.title("Student Login")

def check():
    name=name_var.get()
    mail=mail_var.get()
    dept=dept_var.get()
    yr=yr_var.get()
    ans=tmsg.askquestion("Submission",f"name is:{name}\n email is: {mail}\n dept is:{dept}\n year is:{yr}")
    print(ans)
    if ans=="yes":
        msg="Successful"
    else:
        msg="Chech Credentials"

    tmsg.showinfo("Verdict",msg)



Label(root,text="Student Login Information ",font="ariel 20 bold",fg="black").pack(fill=X,padx=8,pady=5)

#student's name
Label(root,text="Student' Name",font="ariel 11 bold").pack(padx=8,pady=5)
name_var=StringVar()
name_var.set("")
screen1=Entry(root,textvariable=name_var,font="ariel 10 bold")
screen1.pack(padx=9,pady=6)

#student email id
Label(root,text="Email I'd",font="ariel 11 bold").pack(padx=8,pady=5)
mail_var=StringVar()
mail_var.set("")
screen2=Entry(root,textvariable=mail_var,font="ariel 10 bold")
screen2.pack(padx=9,pady=7)

#dept?
Label(root,text="Department",font="ariel 11 bold").pack(padx=8,pady=5)
dept_var=StringVar()
dept_var.set("")
screen3=Entry(root,textvariable=dept_var,font="ariel 10 bold")
screen3.pack(padx=9,pady=7)

#year
Label(root,text="Year",font="ariel 11 bold").pack(padx=8,pady=5)
yr_var=StringVar()
yr_var.set("")
screen4=Entry(root,textvariable=yr_var,font="ariel 10 bold")
screen4.pack(padx=9,pady=7)

#submit button
f=Frame(root)
b=Button(f,text="Submit",font="ariel 10 bold",bg="grey",fg="white",command=check)
b.pack(padx=8,pady=6)
f.pack(side=LEFT)




root.mainloop()

