from tkinter import*
import random
import time

root = Tk()
root.geometry("1600x800+0+0")
root.title("Resaurant Management Systems")

text_Input = StringVar()
operator = ""

Tops = Frame(root, width = 1600, height = 50, bg='powder blue', relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width = 800, height = 700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width = 300, height = 700,  relief=SUNKEN)
f2.pack(side=RIGHT)

#==================time===========================
localtime = time.asctime(time.localtime(time.time())) #DateTime function

#========================Info=======================
lblInfo = Label(Tops, font=('arial',50,'bold'),text="Restaurant Management System",fg='steel blue',bd=10, anchor='w')
lblInfo.grid(row=0, column=0)
lblInfo = Label(Tops, font=('arial',20,'bold'),text=localtime, fg='steel blue',bd=10, anchor='w')
lblInfo.grid(row=1, column=0)

#========================Calculator===================
def btnClick(numbers):
    global operator
    operator= operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator= ""
    text_Input.set("")

def btnEqualInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator= ""

def Ref():
    x = random.randint(10908, 500876)
    randomRef = str(x)
    rand.set(randomRef)

    CoK = float(kajukatli.get())
    CoR = float(rasmalai.get())
    CoP = float(peda.get())
    CoG = float(gubaljamun.get())
    CoL = float(ladu.get())
    CoM = float(milk.get())

    CostofKaju = CoK * 500
    Costofras = CoR * 600
    Costofpeda = CoP * 480
    Costofgubal = CoG * 600
    Costofladu = CoL * 400
    Costofmilk = CoM * 560

    CostofGoods = str('%.2f'%(CostofKaju + Costofras + Costofpeda + Costofgubal + Costofladu + Costofmilk )),"/-"

    PayTax = ((CostofKaju + Costofras + Costofpeda + Costofgubal + Costofladu + Costofmilk) * 0.2)

    TotalCost = (CostofKaju + Costofras + Costofpeda + Costofgubal + Costofladu + Costofmilk)

    Ser_Charge = ((CostofKaju + Costofras + Costofpeda + Costofgubal + Costofladu + Costofmilk)/99)

    Service = str('%.2f' % Ser_Charge),"/-"
    OverAllCost = str('%.2f' % (PayTax + TotalCost + Ser_Charge)),"/-"
    PaidTax = str('%.2f' % PayTax),"/-"

    service.set(Service)
    cost.set(CostofGoods)
    statetax.set(PaidTax)
    subtotal.set(CostofGoods)
    totalcost.set(OverAllCost)
     
def qExit():
    root.destory()

def Reset():
    rand.set("")
    kajukatli.set("")
    rasmalai.set("")
    peda.set("")
    gubaljamun.set("")
    ladu.set("")
    milk.set("")
    cost.set("")
    service.set("")
    statetax.set("")
    subtotal.set("")
    totalcost.set("")
    
#------------------------Display Calculator----------------------------    
txtDisplay = Entry(f2, font=('arial',20,'bold'), textvariable=text_Input, bd=30, insertwidth=4,
                   bg='powder blue', justify = 'right')
txtDisplay.grid(columnspan=4)

#------------------------Row1----------------------------

btn7 = Button(f2, padx=16, bd=8, fg='black', font=('arial',20,'bold'),
              text="7", bg='powder blue',command=lambda:btnClick(7)).grid(row=2,column=0)

btn8 = Button(f2, padx=16, bd=8, fg='black', font=('arial',20,'bold'),
              text="8", bg='powder blue',command=lambda:btnClick(8)).grid(row=2,column=1)

btn9 = Button(f2, padx=16, bd=8, fg='black', font=('arial',20,'bold'),
              text="9", bg='powder blue',command=lambda:btnClick(9)).grid(row=2,column=2)

Addition = Button(f2, padx=16, bd=8, fg='black', font=('arial',20,'bold'),
              text="+", bg='powder blue',command=lambda:btnClick("+")).grid(row=2,column=3)

#----------------------Row2----------------------------------

btn4 = Button(f2, padx=16, bd=8, fg='black', font=('arial',20,'bold'),
              text="4", bg='powder blue',command=lambda:btnClick(4)).grid(row=3,column=0)

btn5 = Button(f2, padx=16, bd=8, fg='black', font=('arial',20,'bold'),
              text="5", bg='powder blue',command=lambda:btnClick(5)).grid(row=3,column=1)

btn6 = Button(f2, padx=16, bd=8, fg='black', font=('arial',20,'bold'),
              text="6", bg='powder blue',command=lambda:btnClick(6)).grid(row=3,column=2)

Subtration = Button(f2, padx=16, bd=8, fg='black', font=('arial',20,'bold'),
              text="-", bg='powder blue',command=lambda:btnClick("-")).grid(row=3,column=3)

#------------------------Row3-----------------------------------

btn1 = Button(f2, padx=16, bd=8, fg='black', font=('arial',20,'bold'),
              text="1", bg='powder blue',command=lambda:btnClick(1)).grid(row=4,column=0)

btn2 = Button(f2, padx=16, bd=8, fg='black', font=('arial',20,'bold'),
              text="2", bg='powder blue',command=lambda:btnClick(2)).grid(row=4,column=1)

btn3 = Button(f2, padx=16, bd=8, fg='black', font=('arial',20,'bold'),
              text="3", bg='powder blue',command=lambda:btnClick(3)).grid(row=4,column=2)
Multiply = Button(f2, padx=16, bd=8, fg='black', font=('arial',20,'bold'),
              text="*", bg='powder blue',command=lambda:btnClick("*")).grid(row=4,column=3)

#-------------------------Row4-------------------------------------

btn0 = Button(f2, padx=16, bd=8, fg='black', font=('arial',20,'bold'),
              text="0", bg='powder blue',command=lambda:btnClick(0)).grid(row=5,column=0)

btnClear = Button(f2, padx=16, bd=8, fg='black', font=('arial',20,'bold'),
              text="C", bg='powder blue',command=btnClearDisplay).grid(row=5,column=1)

btnEquals = Button(f2, padx=16, bd=8, fg='black', font=('arial',20,'bold'),
              text="=", bg='powder blue',command=btnEqualInput).grid(row=5,column=2)

Division = Button(f2, padx=16, bd=8, fg='black', font=('arial',20,'bold'),
              text="/", bg='powder blue',command=lambda:btnClick("/")).grid(row=5,column=3)

#--------------------------Restaurant Info 1----------------------------------------
rand = StringVar()
kajukatli = StringVar()
rasmalai = StringVar()
peda = StringVar()
gubaljamun = StringVar()
ladu = StringVar()
milk = StringVar()
cost = StringVar()
service = StringVar()
statetax = StringVar()
subtotal = StringVar()
totalcost = StringVar()

lb1Reference = Label(f1,font=('arial',16,'bold'),text="Reference",bd=16, anchor='w')
lb1Reference.grid(row=0, column=0)
txtReference = Entry(f1,font=('arial',16,'bold'),textvariable=rand, bd=10, insertwidth=4,
                     bg="powder blue", justify = 'right')
txtReference.grid(row=0, column=1)

lb1kajukatli = Label(f1,font=('arial',16,'bold'),text="Kajukatli Per Kg",bd=16, anchor='w')
lb1kajukatli.grid(row=1, column=0)
txtkajukatli = Entry(f1,font=('arial',16,'bold'),textvariable=kajukatli, bd=10, insertwidth=4,
                     bg="powder blue", justify = 'right')
txtkajukatli.grid(row=1, column=1)

lb1rasmalai = Label(f1,font=('arial',16,'bold'),text="Rasmalai Per Kg",bd=16, anchor='w')
lb1rasmalai .grid(row=2, column=0)
txtrasmalai = Entry(f1,font=('arial',16,'bold'),textvariable=rasmalai, bd=10, insertwidth=4,
                     bg="powder blue", justify = 'right')
txtrasmalai .grid(row=2, column=1)

lb1peda = Label(f1,font=('arial',16,'bold'),text="Peda Per Kg",bd=16, anchor='w')
lb1peda.grid(row=3, column=0)
txtpeda = Entry(f1,font=('arial',16,'bold'),textvariable=peda, bd=10, insertwidth=4,
                     bg="powder blue", justify = 'right')
txtpeda .grid(row=3, column=1)

lb1gubaljamun = Label(f1,font=('arial',16,'bold'),text="Gubaljamun Per kg",bd=16, anchor='w')
lb1gubaljamun.grid(row=4, column=0)
txtgubaljamun = Entry(f1,font=('arial',16,'bold'),textvariable=gubaljamun, bd=10, insertwidth=4,
                     bg="powder blue", justify = 'right')
txtgubaljamun.grid(row=4, column=1)

lb1ladu = Label(f1,font=('arial',16,'bold'),text="Ladu Per Kg",bd=16, anchor='w')
lb1ladu.grid(row=5, column=0)
txtladu = Entry(f1,font=('arial',16,'bold'),textvariable=ladu, bd=10, insertwidth=4,
                     bg="powder blue", justify = 'right')
txtladu.grid(row=5, column=1)

#----------------------------Restaurant Info 2-----------------------------------

lb1milk = Label(f1,font=('arial',16,'bold'),text="Chena Per Kg",bd=16, anchor='w')
lb1milk.grid(row=0, column=2)
txtmilk = Entry(f1,font=('arial',16,'bold'),textvariable=milk, bd=10, insertwidth=4,
                     bg="#ffffff", justify = 'right')
txtmilk.grid(row=0, column=3)

lb1cost = Label(f1,font=('arial',16,'bold'),text="Cost of Goods",bd=16, anchor='w')
lb1cost.grid(row=1, column=2)
txtcost = Entry(f1,font=('arial',16,'bold'),textvariable=cost, bd=10, insertwidth=4,
                     bg="powder blue", justify = 'right')
txtcost.grid(row=1, column=3)

lb1service = Label(f1,font=('arial',16,'bold'),text="Service Charge",bd=16, anchor='w')
lb1service .grid(row=2, column=2)
txtservice = Entry(f1,font=('arial',16,'bold'),textvariable=service, bd=10, insertwidth=4,
                     bg="#ffffff", justify = 'right')
txtservice.grid(row=2, column=3)

lb1statetax = Label(f1,font=('arial',16,'bold'),text="State Tax",bd=16, anchor='w')
lb1statetax.grid(row=3, column=2)
txtstatetax = Entry(f1,font=('arial',16,'bold'),textvariable=statetax, bd=10, insertwidth=4,
                     bg="powder blue", justify = 'right')
txtstatetax.grid(row=3, column=3)

lb1subtotal = Label(f1,font=('arial',16,'bold'),text="Sub Total",bd=16, anchor='w')
lb1subtotal.grid(row=4, column=2)
txtsubtotal = Entry(f1,font=('arial',16,'bold'),textvariable=subtotal, bd=10, insertwidth=4,
                     bg="#ffffff", justify = 'right')
txtsubtotal.grid(row=4, column=3)

lb1totalcost = Label(f1,font=('arial',16,'bold'),text="Total Cost",bd=16, anchor='w')
lb1totalcost.grid(row=5, column=2)
txttotalcost = Entry(f1,font=('arial',16,'bold'),textvariable=totalcost, bd=10, insertwidth=4,
                     bg="powder blue", justify = 'right')
txttotalcost.grid(row=5, column=3)

#==================================Button============================================

btnTotal = Button(f1, padx = 16, pady = 8, fg="black",font=('arial',16,'bold'),width=10,
                  text="Total", bg="powder blue", command=Ref).grid(row=7, column=1)

btnRest = Button(f1, padx = 16, pady = 8, fg="black",font=('arial',16,'bold'),width=10,
                  text="Reset", bg="powder blue", command=Reset).grid(row=7, column=2)

btnExit = Button(f1, padx = 16, pady = 8, fg="black",font=('arial',16,'bold'),width=10,
                  text="Exit", bg="powder blue", command=qExit).grid(row=7, column=3)

root.mainloop()
