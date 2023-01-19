from tkinter import*
from tkinter import ttk
import pygame
from list import items,mode
from tkinter import messagebox as msg
root=Tk()
root.title("Supermarket")
root.geometry()
frame=Frame(root)
frame.pack()









#header_frame
h_frame=Frame(frame,bd=3,relief="sunken",bg="whitesmoke",height=100)
h_frame.pack(side="top",padx=5,pady=5,fill=X)

#title frame
t_frame=Frame(h_frame,bg="whitesmoke",bd=0,relie="sunken",height=30)
t_frame.pack(side="top",padx=30,fill=X)

title=Label(t_frame,text="THE GARDENER SUPERMARKET",font=("arial",40,"bold"),fg="black")
title.pack(side="top")

#login label frame
login_frame=LabelFrame(h_frame,bg="whitesmoke",text="LOGIN",fg="black",font=("arial",15,"bold"),bd=3,relief="sunken",height=70)
login_frame.pack(side="bottom",fill=X,padx=50,pady=3)

#login details
lg_frame=Frame(login_frame,relief="sunken",bg="whitesmoke",width=300,height=50)
lg_frame.pack(side="left",padx=6,pady=2)

l1=Label(lg_frame,bg="whitesmoke",text="Cashier",font=("arial",15,"bold"),fg="black")
l1.grid(row=0,column=0)

l2=Label(lg_frame,bg="whitesmoke",text="Thomas",font=("arial",15,"bold"),fg="black")
l2.grid(row=0,column=1)

l3=Label(lg_frame,bg="whitesmoke",text="Password",font=("arial",15,"bold"),fg="black")
l3.grid(row=1,column=0)

ent=Entry(lg_frame,fg="black",bg="whitesmoke")
ent.grid(row=1,column=1)


sg_frame=Frame(login_frame,bd=0,relief="sunken",bg="whitesmoke",width=300,height=50)
sg_frame.pack(side="right",padx=2,pady=2)

b1=Button(sg_frame,text="LOGIN",fg="black",font=("arial",15,"bold"),bg="powder blue",width=15,height=2)
b1.grid(row=0,column=0,padx=5,pady=5)

b2=Button(sg_frame,text="LOGOUT",fg="black",font=("arial",15,"bold"),width=15,height=2)
b2.grid(row=0,column=1,padx=5,pady=5)


#items details

b_frame=Frame(frame,bd=1,relief="sunken",bg="whitesmoke",width=200,height=400)
b_frame.pack(side="left",padx=2,pady=5)

#item dropbox
i_frame=LabelFrame(b_frame,bd=3,fg="black",text="Name of item",font=("arial",15,"bold"),relief="sunken",width=200,bg="whitesmoke",height=100)
i_frame.pack(side="top",pady=3,padx=3)

dr=StringVar()

list_items=ttk.Combobox(i_frame,width=25,foreground="black",background="white",values=tuple(items.keys()))
list_items.grid(row=0,column=0,pady=5)

#main frame
m_frame=Frame(b_frame,bd=2,relief="sunken",bg="white",width=200,height=300)
m_frame.pack(side="top",pady=5,fill=X,)

#label,entries of the items and the quantity
la=Label(m_frame,text="Name of the item",bg="white",fg="black",font=("arial",13,"bold"))
la.grid(row=0,column=0,ipadx=3)

lb=Label(m_frame,text="QTY",fg="black",bg="white",font=("arial",13,"bold"))
lb.grid(row=0,column=1)

lc=Label(m_frame,text="Unit Price",bg="white",fg="black",font=("arial",13,"bold"))
lc.grid(row=0,column=2)

ld=Label(m_frame,text="Total",bg="white",fg="black",font=("arial",13,"bold"))
ld.grid(row=0,column=3)
    

e1=Entry(m_frame,bg="white",fg="black")
e1.grid(row=1,column=0)

e2=Entry(m_frame,bg="white",fg="black")
e2.grid(row=2,column=0)

e3=Entry(m_frame,bg="white",fg="black")
e3.grid(row=3,column=0)

e4=Entry(m_frame,bg="white",fg="black")
e4.grid(row=4,column=0)

e5=Entry(m_frame,bg="white",fg="black")
e5.grid(row=5,column=0)

e6=Entry(m_frame,bg="white",fg="black")
e6.grid(row=6,column=0)

e7=Entry(m_frame,bg="white",fg="black")
e7.grid(row=7,column=0)

e8=Entry(m_frame,bg="white",fg="black")
e8.grid(row=8,column=0)

values=[]
running=True
def add_list():
    global values
    while running:
        a=list_items.selection_get()
        values.append(a)
        for event in pygame.event.get():
            if event.type==pygame.K_UP:
                running=False
    
    if e1.get()=="":
        dr.set(values[0])
        e1.configure(textvariable=dr)
    if e2.get()=="":
        dr.set(values[1])
        e2.configure(textvariable=dr)
        
    
#add_list
ba=Button(i_frame,text="Add to list",fg="black",font=("arial",13,"bold"),command=add_list)
ba.grid(row=0,column=1,padx=2)


e9=Entry(m_frame,width=5,bg="white",fg="black")
e9.grid(row=1,column=1)

e10=Entry(m_frame,width=5,bg="white",fg="black")
e10.grid(row=2,column=1)

e11=Entry(m_frame,width=5,bg="white",fg="black")
e11.grid(row=3,column=1)

e12=Entry(m_frame,width=5,bg="white",fg="black")
e12.grid(row=4,column=1)

e13=Entry(m_frame,width=5,bg="white",fg="black")
e13.grid(row=5,column=1)

e14=Entry(m_frame,width=5,bg="white",fg="black")
e14.grid(row=6,column=1)

e15=Entry(m_frame,width=5,bg="white",fg="black")
e15.grid(row=7,column=1)

e16=Entry(m_frame,width=5,bg="white",fg="black")
e16.grid(row=8,column=1)

e17=Entry(m_frame,width=5,bg="white",fg="black")
e17.grid(row=1,column=2)

e18=Entry(m_frame,width=5,bg="white",fg="black")
e18.grid(row=2,column=2)

e19=Entry(m_frame,width=5,bg="white",fg="black")
e19.grid(row=3,column=2)

e20=Entry(m_frame,width=5,bg="white",fg="black")
e20.grid(row=4,column=2)

e21=Entry(m_frame,width=5,bg="white",fg="black")
e21.grid(row=5,column=2)

e22=Entry(m_frame,width=5,bg="white",fg="black")
e22.grid(row=6,column=2)

e23=Entry(m_frame,width=5,bg="white",fg="black")
e23.grid(row=7,column=2)

e24=Entry(m_frame,width=5,bg="white",fg="black")
e24.grid(row=8,column=2)

e25=Entry(m_frame,width=5,bg="white",fg="black")
e25.grid(row=1,column=3)

e26=Entry(m_frame,width=5,bg="white",fg="black")
e26.grid(row=2,column=3)

e27=Entry(m_frame,width=5,bg="white",fg="black")
e27.grid(row=3,column=3)

e28=Entry(m_frame,width=5,bg="white",fg="black")
e28.grid(row=4,column=3)

e29=Entry(m_frame,width=5,bg="white",fg="black")
e29.grid(row=5,column=3)

e30=Entry(m_frame,width=5,bg="white",fg="black")
e30.grid(row=6,column=3)

e31=Entry(m_frame,width=5,bg="white",fg="black")
e31.grid(row=7,column=3)

e32=Entry(m_frame,width=5,bg="white",fg="black")
e32.grid(row=8,column=3)


#PAYMENT DETAILS
p_frame=LabelFrame(b_frame,fg="black",text="PAYMENT METHODS",font=("arial",13,"bold"),bd=2,relief="sunken",bg="white",width=200,height=100)
p_frame.pack(side="bottom",pady=5,fill=X,)

le=Label(p_frame,text="Mode of Payment",bg="white",fg="black",font=("arial",13,"bold"))
le.grid(row=0,column=0)

lf=Label(p_frame,text="Amount Paid",bg="white",fg="black",font=("arial",13,"bold"))
lf.grid(row=0,column=1)

lh=Label(p_frame,text="Balance",bg="white",fg="black",font=("arial",13,"bold"))
lh.grid(row=0,column=2)

li=Label(p_frame,text="Label",bg="white",fg="black",font=("arial",13,"bold"))
li.grid(row=0,column=3)

dr1=StringVar()
list_items=ttk.Combobox(p_frame,width=10,textvariable=dr1,values=tuple(mode))
list_items.grid(row=1,column=0)

e33=Entry(p_frame,width=8,bg="white",fg="black")
e33.grid(row=1,column=1)

e34=Entry(p_frame,width=8,bg="white",fg="black")
e34.grid(row=1,column=2)

e35=Entry(p_frame,width=8,bg="white",fg="black")
e35.grid(row=1,column=3)

b3=Button(p_frame,text="Get Prices",fg="black",font=("arial",15,"bold"),width=6)
b3.grid(row=2,column=0,padx=0)

b5=Button(p_frame,text="Receipt",fg="black",font=("arial",15,"bold"),width=4)
b5.grid(row=2,column=1)

b6=Button(p_frame,text="Clear",fg="black",font=("arial",15,"bold"),width=4)
b6.grid(row=2,column=2)

b7=Button(p_frame,text="Total",fg="black",font=("arial",15,"bold"),width=4)
b7.grid(row=2,column=3)

r_frame=LabelFrame(frame,text="RECEIPT",fg="black",font=("arial",14,"bold"),bd=3,relief="sunken",bg="powder blue",width=400,height=400)
r_frame.pack(side="right",padx=3,pady=0)


root.mainloop()