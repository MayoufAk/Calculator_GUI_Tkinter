from tkinter import *
from tkinter import Button

wind=Tk()
wind.geometry("415x645")
wind.title("calculator")
wind.configure(bg="#3399ff")
wind.iconbitmap("calculator.ico")
#we create a frame for Entry then we onna create a frame for buttons
ex=Frame(wind,bg="#3399ff")
ex.pack()
#font has 3 options type ,size and style
ft=("ariel",25,"bold")
eq=StringVar()
eq.set("0")
En=Entry(ex,textvariable=eq,font=ft,justify="right")
En.pack(ipadx=15,ipady=30,pady=2)
x=""
def press(n):
    global x
    x+=str(n)
    eq.set(x)
#eval takes the string argunent input which our expression then it process it and dynamically evaluate it and return it as integer
def equal():
   try:
     global x
     total=str(eval(x))
     eq.set(total)
     x=""
   except:
    eq.set("ERORR")
    x=""
def clear():
    global x
    x=""
    eq.set("0")
def backspace():
    global x
    x=x.rstrip(x[-1]) # rstip gets code in string and takes a carachecter from the right and delete it from the string
    eq.set(x)

bf=Frame(wind,bg="#3399ff")
bf.pack()
# there are tow kibd of font varriables font for Entry and button 1st one takes 3 arguments and 2 ones takes 2
#the shape type of button relief ridge or sold
b1=Button(bf,height=5,width=10,borderwidth=1,text="1",relief="ridge",bg="#80bfff",font=("times new roman",12),command=lambda:press(1))
b2=Button(bf,height=5,width=10,borderwidth=1,text="2",relief="ridge",bg="#80bfff",font=("times new roman",12),command=lambda:press(2))
b3=Button(bf,height=5,width=10,borderwidth=1,text="3",relief="ridge",bg="#80bfff",font=("times new roman",12),command=lambda:press(3))
b4=Button(bf,height=5,width=10,text="4",borderwidth=1,relief="ridge",bg="#80bfff",font=("times new roman",12),command=lambda:press(4))
b5=Button(bf,height=5,width=10,text="5",borderwidth=1,relief="ridge",bg="#80bfff",font=("times new roman",12),command=lambda:press(5))
b6=Button(bf,height=5,width=10,text="6",borderwidth=1,relief="ridge",bg="#80bfff",font=("times new roman",12),command=lambda:press(6))
b7=Button(bf,height=5,width=10,text="7",borderwidth=1,relief="ridge",bg="#80bfff",font=("times new roman",12),command=lambda:press(7))
b8=Button(bf,height=5,width=10,text="8",borderwidth=1,relief="ridge",bg="#80bfff",font=("times new roman",12),command=lambda:press(8))
b9=Button(bf,height=5,width=10,text="9",borderwidth=1,relief="ridge",bg="#80bfff",font=("times new roman",12),command=lambda:press(9))
b0=Button(bf,height=5,width=10,text="0",relief="ridge",borderwidth=1,bg="#80bfff",font=("times new roman",12),command=lambda:press(0))
b10=Button(bf,height=5,width=10,text="+",relief="ridge",borderwidth=1,bg="#80bfff",font=("times new roman",12),command=lambda:press("+"))
b11=Button(bf,height=5,width=10,text="-",relief="ridge",bg="#80bfff",borderwidth=1,font=("times new roman",12),command=lambda:press("-"))
b12=Button(bf,height=5,width=10,borderwidth=1,text="/",relief="ridge",bg="#80bfff",font=("times new roman",12),command=lambda:press("/"))
b13=Button(bf,height=5,width=10,borderwidth=1,text="*",relief="ridge",bg="#80bfff",font=("times new roman",12),command=lambda:press("*"))
b14=Button(bf,height=5,width=10,borderwidth=1,text="=",relief="ridge",bg="#80bfff",font=("times new roman",12),command=equal)
b15=Button(bf,height=5,width=10,borderwidth=1,text="C",relief="ridge",bg="#80bfff",font=("times new roman",12),command=clear)
b16=Button(bf,height=5,width=10,borderwidth=1,text="<<",relief="ridge",bg="#80bfff",font=("times new roman",12),command=backspace)


b1.grid(row=4,column=0)
b2.grid(row=4,column=1)
b3.grid(row=4,column=2)
b4.grid(row=3,column=0)
b5.grid(row=3,column=1)
b6.grid(row=3,column=2)
b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)

b10.grid(row=1,column=1)
b11.grid(row=4,column=3)
b12.grid(row=3,column=3)
b13.grid(row=2,column=3)
b15.grid(row=5,column=0)
b0.grid(row=5,column=1)
b10.grid(row=5,column=2)
b16.grid(row=5,column=3)
b14.grid(row=6,column=0,columnspan=4,sticky="nsew")





#
#
#
#
#
#
#
# #defi
#
#
#
#

#main loop to run tkinter evnents
wind=mainloop()