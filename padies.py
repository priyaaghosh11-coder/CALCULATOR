from tkinter import *
import tkinter.messagebox as tmsg

root=Tk()
root.geometry("500x400")
root.title("Notes")

root.configure(bg="black")

def func():
    print("JHINGA LALA HU-HU")


#file menu
mymenu=Menu(root)
m1=Menu(mymenu,tearoff=0)
m1.add_command(label="New File")
m1.add_command(label="New Window")
m1.add_command(label="Open File")
m1.add_separator()
m1.add_command(label="Save")
m1.add_command(label="Save As")
root.config(menu=mymenu)
mymenu.add_cascade(menu=m1,label="File")

#edit menu
m2=Menu(mymenu,tearoff=0)
m2.add_command(label="Undo")
m2.add_command(label="Redo")
m2.add_separator()
m2.add_command(label="Cut")
m2.add_command(label="Copy")
m2.add_command(label="Paste")
root.config(menu=mymenu)
mymenu.add_cascade(menu=m2,label="Edit")

#help menu
m3=Menu(mymenu,tearoff=0)
m3.add_command(label="About",command=func)
m3.add_command(label="Contact Us")
m3.add_separator()
m3.add_command(label="Extension")
root.config(menu=mymenu)
mymenu.add_cascade(menu=m3,label="Help")

scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)

listbox=Listbox(root,yscrollcommand=scrollbar.get())

listbox.pack(fill="both")
scrollbar.config(command=listbox.yview)






root.mainloop()
