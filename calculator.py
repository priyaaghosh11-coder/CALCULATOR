from tkinter import *

def click(event):
    global scval
    text=event.widget.cget("text")
    print(text)
    if text=="=":
        if scval.get().isdigit():
            value=int(scval.get())
            print(value)
        else:
            value=eval(screen.get())#string evaluate krta hai-eval

            scval.set(value)
            screen.update()
    elif text=="AC":
        scval.set("")
        screen.update()
    else:
        scval.set(scval.get()+text)
        screen.update()


    
root=Tk()
root.geometry("400x650")
root.title("Calculator")

scval=StringVar()
scval.set("")
screen=Entry(root,textvariable=scval,font="lucida 25 bold",bg="grey",fg="black",relief=SUNKEN)
screen.pack(padx=8,pady=10)

#first row num
f=Frame(root,bg="grey")
b=Button(f,text="9",font="lucida 15 bold",padx=28,pady=18 )
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="8",font="lucida 15 bold",padx=28,pady=18 )
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)


b=Button(f,text="7",font="lucida 15 bold",padx=28,pady=18 )
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack(pady=10,padx=8,fill=X)

#second row num
f=Frame(root,bg="grey")
b=Button(f,text="6",font="lucida 15 bold",padx=28,pady=18 )
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="5",font="lucida 15 bold",padx=28,pady=18 )
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)


b=Button(f,text="4",font="lucida 15 bold",padx=28,pady=18 )
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack(pady=10,padx=8,fill=X)

#third row num
f=Frame(root,bg="grey")
b=Button(f,text="3",font="lucida 15 bold",padx=28,pady=18 )
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="2",font="lucida 15 bold",padx=28,pady=18)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="1",font="lucida 15 bold",padx=28,pady=18 )
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack(pady=10,padx=8,fill=X)

#fourth row calc
f=Frame(root,bg="grey")
b=Button(f,text="0",font="lucida 15 bold",padx=28,pady=18)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="-",font="lucida 15 bold",padx=28,pady=18)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="+",font="lucida 15 bold",padx=28,pady=18 )
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack(pady=10,padx=8,fill=X)

#fifth row calc
f=Frame(root,bg="grey")

b=Button(f,text="/",font="lucida 15 bold",padx=28,pady=18)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="*",font="lucida 15 bold",padx=28,pady=18 )
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="=",font="lucida 15 bold",padx=28,pady=18)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack(pady=10,padx=8,fill=X)

#sixth row calc
f=Frame(root,bg="grey")
b=Button(f,text="AC",font="lucida 15 bold",padx=28,pady=18 )
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="%",font="lucida 15 bold",padx=28,pady=18 )
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b=Button(f,text="00",font="lucida 15 bold",padx=30,pady=18 )
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack(pady=10,padx=8,fill=X)





root.mainloop()