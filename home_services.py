from tkinter import *
from tkcalendar import *
from PIL import ImageTk,Image
import pyttsx3
def calculation():
    listofcheck=[]
    if is_checked1.get():
        listofcheck.append(1500)
    if is_checked2.get():
        listofcheck.append(1000)
    if is_checked3.get():
        listofcheck.append(2800)
    if is_checked4.get():
        listofcheck.append(1200)
    if is_checked5.get():
        listofcheck.append(2000)
    if is_checked6.get():
        listofcheck.append(4000)
    global sumoflist
    sumoflist=sum(listofcheck)
    Label(work,text=sumoflist,font=("Arial 14",15,"bold"),fg="midnight blue").grid(row=7,column=4,padx=20)
def servantworkpack():
    global work
    work=Toplevel()
    work.geometry("1366x768")
    work.title("SERVANT WORK PACK")
    global is_checked1,is_checked2,is_checked3,is_checked4,is_checked5,is_checked6
    is_checked1=IntVar()
    is_checked2=IntVar()
    is_checked3=IntVar()
    is_checked4=IntVar()
    is_checked5=IntVar()
    is_checked6=IntVar()
    Label(work,text="**SERVANT WORK PACK**",font=("castellar",24,"underline","bold"),fg="midnight blue").grid(row=0,column=2,padx=50)
    Label(work,text="1.",font=("Arial 14",18,"bold"),fg="midnight blue").grid(row=1,column=0,pady=20,padx=50)
    Label(work,text="2.",font=("Arial 14",18,"bold"),fg="midnight blue").grid(row=2,column=0,pady=20,padx=50)
    Label(work,text="3.",font=("Arial 14",18,"bold"),fg="midnight blue").grid(row=3,column=0,pady=20,padx=50)
    Label(work,text="4.",font=("Arial 14",18,"bold"),fg="midnight blue").grid(row=4,column=0,pady=20,padx=50)
    Label(work,text="5.",font=("Arial 14",18,"bold"),fg="midnight blue").grid(row=5,column=0,pady=20,padx=50)
    Label(work,text="6.",font=("Arial 14",18,"bold"),fg="midnight blue").grid(row=6,column=0,pady=20,padx=50)
    Label(work,text="SWEEPING AND MOPING:-",font=("Arial 14",18,"underline","bold"),fg="midnight blue").grid(row=1,column=1,pady=20)
    Label(work,text="+ UTENSILS:-",font=("Arial 14",18,"underline","bold"),fg="midnight blue").grid(row=2,column=1,pady=20)
    Label(work,text="+ DUSTING:-",font=("Arial 14",18,"underline","bold"),fg="midnight blue").grid(row=3,column=1,pady=20)
    Label(work,text="+ BATHROOM:-",font=("Arial 14",18,"underline","bold"),fg="midnight blue").grid(row=4,column=1,pady=20)
    Label(work,text="+ WASHING CLOTHES:-",font=("Arial 14",18,"underline","bold"),fg="midnight blue").grid(row=5,column=1,pady=20)
    Label(work,text="+ IRONING:-",font=("Arial 14",18,"underline","bold"),fg="midnight blue").grid(row=6,column=1,pady=20)
    Label(work,text="1500",font=("Arial 14",18,"bold"),fg="midnight blue").grid(row=1,column=2,pady=20)
    Label(work,text="1000",font=("Arial 14",18,"bold"),fg="midnight blue").grid(row=2,column=2,pady=20)
    Label(work,text="2800",font=("Arial 14",18,"bold"),fg="midnight blue").grid(row=3,column=2,pady=20)
    Label(work,text="1200",font=("Arial 14",18,"bold"),fg="midnight blue").grid(row=4,column=2,pady=20)
    Label(work,text="2000",font=("Arial 14",18,"bold"),fg="midnight blue").grid(row=5,column=2,pady=20)
    Label(work,text="4000",font=("Arial 14",18,"bold"),fg="midnight blue").grid(row=6,column=2,pady=20)
    check1=Checkbutton(work,onvalue=1,offvalue=0,variable=is_checked1)
    check1.grid(row=1,column=3,pady=20)
    check2=Checkbutton(work,onvalue=1,offvalue=0,variable=is_checked2)
    check2.grid(row=2,column=3,pady=20)
    check3=Checkbutton(work,onvalue=1,offvalue=0,variable=is_checked3)
    check3.grid(row=3,column=3,pady=20)
    check4=Checkbutton(work,onvalue=1,offvalue=0,variable=is_checked4)
    check4.grid(row=4,column=3,pady=20)
    check5=Checkbutton(work,onvalue=1,offvalue=0,variable=is_checked5)
    check5.grid(row=5,column=3,pady=20)
    check6=Checkbutton(work,onvalue=1,offvalue=0,variable=is_checked6)
    check6.grid(row=6,column=3,pady=20)
    Button(work,text="TOTAL",borderwidth=4,relief="raised",command=calculation).grid(row=7,column=3)
    
    
def submit_customer():
    import mysql.connector
    sql=mysql.connector.connect(host="localhost",user="root",passwd="tanya1703",database="sercare")
    c=sql.cursor()
    variable="INSERT INTO customer(full_name,dob,mobile1,mobile2,address,customer_id,customer_password) VALUES(%s,%s,%s,%s,%s,%s,%s)"
    value=(customername.get().upper(),v,cusmobile1.get(),cusmobile2.get(),cusaddress.get(),cusid.get(),cuspwd.get())
    c.execute(variable,value)
    sql.commit()
    Label(page4,text="SUCCESSFULLY SIGNED UP!!",font=("candara light",15,"bold"),fg="midnight blue").grid(row=11,column=1)


def opencalendar():
    global cal
    global v
    v=StringVar()
    def opendate():
        global v
        v=StringVar()
        v=cal.get_date()
    cal=Calendar(page4,font=("Arial 14"), selectmode="day", month=1, day=1, year=2019)
    cal.grid(row=2,column=1)
    Button(page4,text="CLICK",command=opendate).grid(row=3,column=1)
def customerlogin():
    global page4
    page4=Toplevel()
    page4.geometry("1366x768")
    page4.title("CUSTOMER DETAILS")
    global customername,cusmobile1,cusmobile2,cusaddress,cusid,cuspwd
    customername=StringVar()
    cusmobile1=IntVar()
    cusmobile2=IntVar()
    cusaddress=StringVar()
    cusid=StringVar()
    cuspwd=StringVar()
    Label(page4,text="DETAILS OF CUSTOMER",font=("castellar",24,"underline","bold"),fg="midnight blue").grid(row=0,column=1)
    Label(page4,text="FULL NAME",font=("candara light",15,"bold"),fg="midnight blue").grid(row=1,column=0,pady=10)
    Label(page4,text="D.O.B",font=("candara light",15,"bold"),fg="midnight blue").grid(row=2,column=0,pady=10)
    Label(page4,text="MOBILE NUMBER",font=("candara light",15,"bold"),fg="midnight blue").grid(row=4,column=0,pady=10)
    Label(page4,text="MOBILE NUMBER(2)",font=("candara light",15,"bold"),fg="midnight blue").grid(row=5,column=0,pady=10)
    Label(page4,text="PERMANENT ADDRESS",font=("candara light",15,"bold"),fg="midnight blue").grid(row=6,column=0,pady=10)
    Label(page4,text="ID",font=("candara light",15,"bold"),fg="midnight blue").grid(row=7,column=0,pady=10)
    Label(page4,text="SET PASSWORD",font=("candara light",15,"bold"),fg="midnight blue").grid(row=8,column=0,pady=10)
    Entry(page4,textvariable=customername).grid(row=1,column=1)
    Button(page4,text="SELECT",borderwidth=4,relief="raised",command=opencalendar).grid(row=2,column=1)
    Entry(page4,textvariable=cusmobile1).grid(row=4,column=1)
    Entry(page4,textvariable=cusmobile2).grid(row=5,column=1)
    Entry(page4,textvariable=cusaddress).grid(row=6,column=1)
    Entry(page4,textvariable=cusid).grid(row=7,column=1)
    Entry(page4,textvariable=cuspwd).grid(row=8,column=1)
    Label(page4,text="**8 CHARACTERS ONLY",font=("candara light",15,"bold"),fg="midnight blue").grid(row=8,column=3)
    Button(page4,text="SUBMIT",command=submit_customer).grid(row=9,column=0,pady=20)
    Button(page4,text="RESET").grid(row=9,column=1,pady=20)

    
def submit_caretaker():
    import mysql.connector
    sql=mysql.connector.connect(host="localhost",user="root",passwd="tanya1703",database="sercare")
    c=sql.cursor()
    variable="INSERT INTO caretaker(full_name,age,mobile_no1,mobile_no2,relative_mobile,aadhar,address,caretaker_id,caretaker_password) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    value=(caretakername.get().upper(),c_age.get(),c_mobile1.get(),c_mobile2.get(),c_mobile3.get(),c_aadhar.get(),c_address.get(),idcaretaker.get(),pwdcaretaker.get())
    c.execute(variable,value)
    sql.commit()
    Label(page3,text="SUCCESSFULLY SIGNED UP!!",font=("candara light",15,"bold"),fg="midnight blue").grid(row=11,column=1)



def submit_servant():
    import mysql.connector
    sql=mysql.connector.connect(host="localhost",user="root",passwd="tanya1703",database="sercare")
    c=sql.cursor()
    variable="INSERT INTO servant(full_name,age,mobile_no1,mobile_no2,relative_mobile,aadhar,address,servant_id,servant_password) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    value=(servantname.get().upper(),age.get(),mobile1.get(),mobile2.get(),mobile3.get(),aadhar.get(),address.get(),idservant.get(),pwdservant.get())
    c.execute(variable,value)
    sql.commit()
    Label(page2,text="SUCCESSFULLY SIGNED UP!!",font=("candara light",15,"bold"),fg="midnight blue").grid(row=11,column=1)


def loginservant():
    global page2
    page2=Toplevel()
    page2.geometry("1366x768")
    page2.title("LOGIN PAGE")
    global servantname,age,mobile1,mobile2,mobile3,aadhar,address,idservant,pwdservant
    servantname=StringVar()
    age=IntVar()
    mobile1=IntVar()
    mobile2=IntVar()
    mobile3=IntVar()
    aadhar=IntVar()
    address=StringVar()
    idservant=StringVar()
    pwdservant=StringVar()
    Label(page2,text="**DETAILS OF SERVANT**",font=("castellar",24,"underline","bold"),fg="midnight blue").grid(row=0,column=1)
    Label(page2,text="FULL NAME",font=("candara light",15,"bold"),fg="midnight blue").grid(row=1,column=0)
    Label(page2,text="AGE",font=("candara light",15,"bold"),fg="midnight blue").grid(row=2,column=0)
    Label(page2,text="MOBILE NUMBER 1",font=("candara light",15,"bold"),fg="midnight blue").grid(row=3,column=0)
    Label(page2,text="MOBILE NUMBER 2",font=("candara light",15,"bold"),fg="midnight blue").grid(row=4,column=0)
    Label(page2,text="RELATIVE MOBILE NO.",font=("candara light",15,"bold"),fg="midnight blue").grid(row=5,column=0)
    Label(page2,text="AADHAR CARD",font=("candara light",15,"bold"),fg="midnight blue").grid(row=6,column=0)
    Label(page2,text="ADDRESS",font=("candara light",15,"bold"),fg="midnight blue").grid(row=7,column=0)
    Label(page2,text="ID",font=("candara light",15,"bold"),fg="midnight blue").grid(row=8,column=0)
    Label(page2,text="SET PASSWORD",font=("candara light",15,"bold"),fg="midnight blue").grid(row=9,column=0)
    Label(page2,text="**8 CHARACTERS ONLY",font=("candara light",15,"bold"),fg="midnight blue").grid(row=9,column=2)
    Entry(page2,textvariable=servantname).grid(row=1,column=1)
    Entry(page2,textvariable=age).grid(row=2,column=1)
    Entry(page2,textvariable=mobile1).grid(row=3,column=1)
    Entry(page2,textvariable=mobile2).grid(row=4,column=1)
    Entry(page2,textvariable=mobile3).grid(row=5,column=1)
    Entry(page2,textvariable=aadhar).grid(row=6,column=1)
    Entry(page2,textvariable=address).grid(row=7,column=1)
    Entry(page2,textvariable=idservant).grid(row=8,column=1)
    Entry(page2,textvariable=pwdservant).grid(row=9,column=1)
    Button(page2,text="SUBMIT",command=submit_servant).grid(row=10,column=0,pady=30)
    Button(page2,text="RESET").grid(row=10,column=1,pady=30)
def logincaretaker():
    global page3
    page3=Toplevel()
    page3.geometry("1366x768")
    page3.title("LOGIN PAGE")
    global caretakername,c_age,c_mobile1,c_mobile2,c_mobile3,c_aadhar,c_address,idcaretaker,pwdcaretaker
    caretakername=StringVar()
    c_age=IntVar()
    c_mobile1=IntVar()
    c_mobile2=IntVar()
    c_mobile3=IntVar()
    c_aadhar=IntVar()
    c_address=StringVar()
    idcaretaker=StringVar()
    pwdcaretaker=StringVar()
    Label(page3,text="**DETAILS OF CARETAKER**",font=("castellar",24,"underline","bold"),fg="midnight blue").grid(row=0,column=1)
    Label(page3,text="FULL NAME",font=("candara light",15,"bold"),fg="midnight blue").grid(row=1,column=0)
    Label(page3,text="AGE",font=("candara light",15,"bold"),fg="midnight blue").grid(row=2,column=0)
    Label(page3,text="MOBILE NUMBER 1",font=("candara light",15,"bold"),fg="midnight blue").grid(row=3,column=0)
    Label(page3,text="MOBILE NUMBER 2",font=("candara light",15,"bold"),fg="midnight blue").grid(row=4,column=0)
    Label(page3,text="RELATIVE MOBILE NO.",font=("candara light",15,"bold"),fg="midnight blue").grid(row=5,column=0)
    Label(page3,text="AADHAR CARD",font=("candara light",15,"bold"),fg="midnight blue").grid(row=6,column=0)
    Label(page3,text="ADDRESS",font=("candara light",15,"bold"),fg="midnight blue").grid(row=7,column=0)
    Label(page3,text="ID",font=("candara light",15,"bold"),fg="midnight blue").grid(row=8,column=0)
    Label(page3,text="SET PASSWORD",font=("candara light",15,"bold"),fg="midnight blue").grid(row=9,column=0)
    Label(page3,text="**8 CHARACTERS ONLY",font=("candara light",15,"bold"),fg="midnight blue").grid(row=9,column=2)
    Entry(page3,textvariable=caretakername).grid(row=1,column=1)
    Entry(page3,textvariable=c_age).grid(row=2,column=1)
    Entry(page3,textvariable=c_mobile1).grid(row=3,column=1)
    Entry(page3,textvariable=c_mobile2).grid(row=4,column=1)
    Entry(page3,textvariable=c_mobile3).grid(row=5,column=1)
    Entry(page3,textvariable=c_aadhar).grid(row=6,column=1)
    Entry(page3,textvariable=c_address).grid(row=7,column=1)
    Entry(page3,textvariable=idcaretaker).grid(row=8,column=1)
    Entry(page3,textvariable=pwdcaretaker).grid(row=9,column=1)
    Button(page3,text="SUBMIT",command=submit_caretaker).grid(row=10,column=0,pady=30)
    Button(page3,text="RESET").grid(row=10,column=1,pady=30)

def fetchcaretakerdetails():
    import mysql.connector as m
    obj=m.connect(host="localhost",user="root",passwd="tanya1703",database="sercare")
    c=obj.cursor()
    sql="SELECT full_name,age,mobile_no1,mobile_no2,aadhar,address FROM caretaker WHERE id='{}'".format(idno.get())
    c.execute(sql)
    y=c.fetchall()
    for i in y:
        Label(frame15,text=i[0],font=("Copperplate Gothic Bold",15),fg="midnight blue").grid(row=2,column=3,pady=15)
        Label(frame15,text=i[1],font=("Copperplate Gothic Bold",15),fg="midnight blue").grid(row=3,column=3,pady=15)
        Label(frame15,text=i[2],font=("Copperplate Gothic Bold",15),fg="midnight blue").grid(row=4,column=3,pady=15)
        Label(frame15,text=i[3],font=("Copperplate Gothic Bold",15),fg="midnight blue").grid(row=5,column=3,pady=15)
        Label(frame15,text=i[4],font=("Copperplate Gothic Bold",15),fg="midnight blue").grid(row=6,column=3,pady=15)
        Label(frame15,text=i[5],font=("Copperplate Gothic Bold",15),fg="midnight blue").grid(row=7,column=3,pady=15)



def fetchservantdetails():
    import mysql.connector as m
    obj=m.connect(host="localhost",user="root",passwd="tanya1703",database="sercare")
    c=obj.cursor()
    sql="SELECT full_name,age,mobile_no1,mobile_no2,aadhar,address FROM servant WHERE id='{}'".format(idnumber.get())
    c.execute(sql)
    y=c.fetchall()
    for i in y:
        Label(frame11,text=i[0],font=("Copperplate Gothic Bold",15),fg="midnight blue").grid(row=2,column=3,pady=15)
        Label(frame11,text=i[1],font=("Copperplate Gothic Bold",15),fg="midnight blue").grid(row=3,column=3,pady=15)
        Label(frame11,text=i[2],font=("Copperplate Gothic Bold",15),fg="midnight blue").grid(row=4,column=3,pady=15)
        Label(frame11,text=i[3],font=("Copperplate Gothic Bold",15),fg="midnight blue").grid(row=5,column=3,pady=15)
        Label(frame11,text=i[4],font=("Copperplate Gothic Bold",15),fg="midnight blue").grid(row=6,column=3,pady=15)
        Label(frame11,text=i[5],font=("Copperplate Gothic Bold",15),fg="midnight blue").grid(row=7,column=3,pady=15)

def caretakerinfo():
    global caredetails
    caredetails=Toplevel()
    caredetails.geometry("1366x768")
    caredetails.title("CARETAKER PERSONAL DETAILS")
    global idno
    idno=IntVar()
    global frame15
    frame14=Frame(caredetails)
    frame14.pack()
    frame15=Frame(caredetails)
    frame15.pack()
    Label(frame14,text="**CARETAKER PERSONAL DETAILS**",font=("castellar",28,"underline","bold"),fg="midnight blue").grid(row=0,column=1)
    Label(frame15,text="ENTER CARETAKER ID:",font=("candara light",15,"underline","bold"),fg="midnight blue").grid(row=1,column=1,pady=15)
    Entry(frame15,textvariable=idno).grid(row=1,column=2,pady=15,padx=30)
    Button(frame15,text="ENTER",command=fetchcaretakerdetails).grid(row=1,column=3,pady=15)
    Label(frame15,text="FULL NAME:",font=("Copperplate Gothic Bold",15),fg="midnight blue").grid(row=2,column=1,pady=15)
    Label(frame15,text="AGE:",font=("Copperplate Gothic Bold",15),fg="midnight blue").grid(row=3,column=1,pady=15)
    Label(frame15,text="MOBILE NUMBER 1:",font=("Copperplate Gothic Bold",15),fg="midnight blue").grid(row=4,column=1,pady=15)
    Label(frame15,text="MOBILE NUMBER 2:",font=("Copperplate Gothic Bold",15),fg="midnight blue").grid(row=5,column=1,pady=15)
    Label(frame15,text="AADHAR CARD:",font=("Copperplate Gothic Bold",15),fg="midnight blue").grid(row=6,column=1,pady=15)
    Label(frame15,text="ADDRESS:",font=("Copperplate Gothic Bold",15),fg="midnight blue").grid(row=7,column=1,pady=15)
        

        
def servantinfo():
    global serdetails
    serdetails=Toplevel()
    serdetails.geometry("1366x768")
    serdetails.title("SERVANT PERSONAL DETAILS")
    global idnumber
    idnumber=IntVar()
    global frame11
    frame10=Frame(serdetails)
    frame10.pack()
    frame11=Frame(serdetails)
    frame11.pack()
    Label(frame10,text="**SERVANT PERSONAL DETAILS**",font=("castellar",28,"underline","bold"),fg="midnight blue").grid(row=0,column=1)
    Label(frame11,text="ENTER SERVANT ID:",font=("candara light",15,"underline","bold"),fg="midnight blue").grid(row=1,column=1,pady=15)
    Entry(frame11,textvariable=idnumber).grid(row=1,column=2,pady=15,padx=30)
    Button(frame11,text="ENTER",command=fetchservantdetails).grid(row=1,column=3,pady=15)
    Label(frame11,text="FULL NAME:",font=("Copperplate Gothic Bold",15),fg="midnight blue").grid(row=2,column=1,pady=15)
    Label(frame11,text="AGE:",font=("Copperplate Gothic Bold",15),fg="midnight blue").grid(row=3,column=1,pady=15)
    Label(frame11,text="MOBILE NUMBER 1:",font=("Copperplate Gothic Bold",15),fg="midnight blue").grid(row=4,column=1,pady=15)
    Label(frame11,text="MOBILE NUMBER 2:",font=("Copperplate Gothic Bold",15),fg="midnight blue").grid(row=5,column=1,pady=15)
    Label(frame11,text="AADHAR CARD:",font=("Copperplate Gothic Bold",15),fg="midnight blue").grid(row=6,column=1,pady=15)
    Label(frame11,text="ADDRESS:",font=("Copperplate Gothic Bold",15),fg="midnight blue").grid(row=7,column=1,pady=15)

def forcomplaintcaretaker():
    ccomplaint=Toplevel()
    ccomplaint.geometry("1366x768")
    ccomplaint.title("COMPLAINT FOR CARETAKER")
    Label(ccomplaint,text="COMPLAINT FOR CARETAKER",font=("castellar",24,"underline","bold"),fg="midnight blue").pack()
    Text(ccomplaint,height=20,width=50).pack(pady=30)
    Button(ccomplaint,text="SEND",borderwidth=4,relief="raised").pack()
    
def caretakerdetails():
    import mysql.connector
    obj=mysql.connector.connect(host="localhost",user="root",passwd="tanya1703",database="sercare")
    c=obj.cursor()
    sql1="SELECT count(full_name) FROM caretaker"
    c.execute(sql1)
    y1=c.fetchall()
    global countofcaretaker
    countofcaretaker=y1[0][0]
    global customerpage2
    customerpage2=Toplevel()
    customerpage2.geometry("1366x768")
    customerpage2.title("customer page2")
    frame12=Frame(customerpage2)
    frame12.pack()
    global frame13
    frame13=Frame(customerpage2)
    frame13.pack()
    Label(frame12,text="**CARETAKER'S INFORMATION**",font=("castellar",28,"underline","bold"),fg="midnight blue").grid(row=0,column=1)
    Label(frame12,text="** id is provided for caretaker details",font=("Copperplate Gothic Bold",12),fg="purple").grid(row=1,column=1)
    sql2="SELECT full_name FROM caretaker"
    sql3="SELECT id FROM caretaker"
    c.execute(sql2)
    global y2
    y2=c.fetchall()
    c.execute(sql3)
    global y3
    y3=c.fetchall()
    for i in range(countofcaretaker):
        l6=Label(frame13,text=y2[i][0],font=("candara light",18,"underline","bold"),fg="midnight blue")
        l6.grid(row=2+i,column=0,pady=10)
        l6.bind("<Button-1>",lambda g:caretakerinfo())
        l7=Label(frame13,text="id:-",font=("candara light",18,"bold"),fg="midnight blue")
        l7.grid(row=2+i,column=1,pady=10)
        l8=Label(frame13,text=y3[i][0],font=("candara light",18,"bold"),fg="midnight blue")
        l8.grid(row=2+i,column=2,pady=10)
        b1=Button(frame13,text="BOOK",command=lambda i=i: onbuttonclick(i))
        b1.grid(row=2+i,column=3,pady=10,padx=50)
    
    label2=Label(frame13,text="HAVE ANY COMPLAINT? CLICK HERE",font=("Copperplate Gothic Bold",12,"underline"),fg="purple")    
    label2.grid(row=5+countofcaretaker,column=0,pady=10)
    label2.bind("<Button-1>",lambda com:forcomplaintcaretaker())

def onbuttonclick(j):
    print(customerid.get())
    print(y2[j][0])# name
    print(y3[j][0])# id
    print(j)
    import mysql.connector
    obj=mysql.connector.connect(host="localhost",user="root",passwd="tanya1703",database="sercare")
    c=obj.cursor()
    sql5="SELECT count(caretaker_booked) FROM booking_caretaker WHERE caretaker_id='{}'".format(y3[j][0])
    sql6="SELECT count(customer_name) FROM booking_caretaker WHERE customer_name='{}'".format(customerid.get())
    c.execute(sql5)
    y5=c.fetchall()
    c.execute(sql6)
    y6=c.fetchall()
    count_caretaker_booked=y5[0][0]
    if(count_caretaker_booked==0):
        if(y6[0][0]==0):
            sql4="INSERT INTO booking_caretaker(customer_name,caretaker_booked,caretaker_id) VALUES(%s,%s,%s)"
            val4=(customerid.get(),y2[j][0],y3[j][0])
            c.execute(sql4,val4)
            obj.commit()
            Label(frame13,text="YOUR CARETAKER IS SUCCESSFULLY BOOKED!!",font=("candara light",18,"bold"),fg="midnight blue").grid(row=4+countofcaretaker,column=0,pady=10)

        else:
            Label(frame13,text="YOU ALREADY BOOKED A CARETAKER!!",font=("candara light",18,"bold"),fg="midnight blue").grid(row=4+countofcaretaker,column=0,pady=10)
        

    else:
        Label(frame13,text="THIS CARETAKER IS ALREADY BOOKED!!",font=("candara light",18,"bold"),fg="midnight blue").grid(row=4+countofcaretaker,column=0,pady=10)
        

def forcomplaintservant():
    scomplaint=Toplevel()
    scomplaint.geometry("1366x768")
    scomplaint.title("COMPLAINT FOR SERVANT")
    Label(scomplaint,text="COMPLAINT FOR SERVANT",font=("castellar",24,"underline","bold"),fg="midnight blue").pack()
    Text(scomplaint,height=20,width=50).pack(pady=30)
    Button(scomplaint,text="SEND",borderwidth=4,relief="raised").pack()
    
           
def servantdetails():
    import mysql.connector
    obj=mysql.connector.connect(host="localhost",user="root",passwd="tanya1703",database="sercare")
    c=obj.cursor()
    sql8="SELECT count(full_name) FROM servant"
    c.execute(sql8)
    y8=c.fetchall()
    global countofservant
    countofservant=y8[0][0]
    global customerpage
    customerpage=Toplevel()
    customerpage.geometry("1366x768")
    customerpage.title("customer page")
    frame8=Frame(customerpage)
    frame8.pack()
    global frame9
    frame9=Frame(customerpage)
    frame9.pack()
    complaintframe=Frame(customerpage)
    complaintframe.pack()
    Label(frame8,text="**SERVANT'S INFORMATION**",font=("castellar",28,"underline","bold"),fg="midnight blue").grid(row=0,column=1)
    Label(frame8,text="** id is provided for servant details",font=("Copperplate Gothic Bold",12),fg="purple").grid(row=1,column=1)
    sql7="SELECT full_name FROM servant"
    sql9="SELECT id FROM servant"
    c.execute(sql7)
    global y7
    y7=c.fetchall()
    c.execute(sql9)
    global y9
    y9=c.fetchall()
    for i in range(countofservant):
        l6=Label(frame9,text=y7[i][0],font=("candara light",18,"underline","bold"),fg="midnight blue")
        l6.grid(row=2+i,column=0,pady=10)
        l6.bind("<Button-1>",lambda f:servantinfo())
        l7=Label(frame9,text="id:-",font=("candara light",18,"bold"),fg="midnight blue")
        l7.grid(row=2+i,column=1,pady=10)
        l8=Label(frame9,text=y9[i][0],font=("candara light",18,"bold"),fg="midnight blue")
        l8.grid(row=2+i,column=2,pady=10)
        b1=Button(frame9,text="BOOK",command=lambda i=i: onclick(i))
        b1.grid(row=2+i,column=3,pady=10,padx=50)
        b2=Button(frame9,text="CANCEL BOOK",command=lambda i=i: onclickdelete(i))
        b2.grid(row=2+i,column=4,pady=10,padx=50)
        b3=Button(frame9,text="SELECT PLAN",command=lambda :servantworkpack())
        b3.grid(row=2+i,column=5,pady=10,padx=50)

    label3=Label(complaintframe,text="HAVE ANY COMPLAINT? CLICK HERE",font=("Copperplate Gothic Bold",12,"underline"),fg="purple")
    label3.grid(row=6+countofservant,column=0,pady=10)
    label3.bind("<Button-1>",lambda com1:forcomplaintservant())

def onclick(j):
    #print(customerid.get())
    #print(y7[j][0])# name
    #print(y9[j][0])# id
    #print(j)
    import mysql.connector
    obj=mysql.connector.connect(host="localhost",user="root",passwd="tanya1703",database="sercare")
    c=obj.cursor()
    sql10="SELECT count(servant_booked) FROM booking_servant WHERE servant_id='{}'".format(y9[j][0])
    sql11="SELECT count(customer_name) FROM booking_servant WHERE customer_name='{}'".format(customerid.get())
    c.execute(sql10)
    y10=c.fetchall()
    c.execute(sql11)
    y11=c.fetchall()
    count_servant_booked=y10[0][0]
    if(count_servant_booked<3):
        if(y11[0][0]==0):
            sql12="INSERT INTO booking_servant(customer_name,servant_booked,servant_id,total_amount) VALUES(%s,%s,%s,%s)"
            val12=(customerid.get(),y7[j][0],y9[j][0],sumoflist)
            c.execute(sql12,val12)
            obj.commit()
            Label(frame9,text="YOUR SERVANT IS SUCCESSFULLY BOOKED!!",font=("candara light",18,"bold"),fg="midnight blue").grid(row=4+countofservant,column=0,pady=10)

        else:
            Label(frame9,text="YOU ALREADY BOOKED A SERVANT!!",font=("candara light",18,"bold"),fg="midnight blue").grid(row=4+countofservant,column=0,pady=10)
        

    else:
        Label(frame9,text="THIS SERVANT IS ALREADY BOOKED!!",font=("candara light",18,"bold"),fg="midnight blue").grid(row=4+countofservant,column=0,pady=10)
        

def onclickdelete(k):
    #print(y9[k][0])
    import mysql.connector
    obj=mysql.connector.connect(host="localhost",user="root",passwd="tanya1703",database="sercare")
    c=obj.cursor()
    sqlquery="DELETE FROM booking_servant WHERE customer_name='{}' and servant_id='{}'".format(customerid.get(),y9[k][0])
    c.execute(sqlquery)
    obj.commit()
    Label(frame9,text="THIS SERVANT IS CANCELLED!!",font=("candara light",18,"bold"),fg="midnight blue").grid(row=4+countofservant,column=0,pady=10)

def signupcustomer():
    import mysql.connector
    obj=mysql.connector.connect(host="localhost",user="root",passwd="tanya1703",database="sercare")
    c=obj.cursor()
    sql="SELECT customer_id,customer_password FROM customer WHERE customer_id='{}' and customer_password='{}' ".format(customerid.get(),customerpwd.get()) 
    c.execute(sql)
    y=c.fetchall()
    for k in y:
        if(k[0]==customerid.get() and k[1]==customerpwd.get()):
            choosen=Toplevel()
            choosen.geometry("1366x768")
            choosen.title("welcome")
            l9=Label(choosen,text="WANT TO BOOK A SERVANT?",font=("castellar",20,"underline","bold"),fg="midnight blue")
            l9.pack(pady=100)
            l9.bind("<Button-1>",lambda booking:servantdetails())
            l10=Label(choosen,text="WANT TO BOOK A CARETAKER?",font=("castellar",20,"underline","bold"),fg="midnight blue")
            l10.pack()
            l10.bind("<Button-1>",lambda booking:caretakerdetails())
                

            
def forcustomer():
    page=Toplevel()
    page.geometry("1366x768")
    page.title("Registration")
    global customerid,customerpwd
    customerid=StringVar()
    customerpwd=StringVar()
    Label(page,text="**CUSTOMER REGISTRATION**",font=("castellar",28,"underline","bold"),fg="midnight blue").grid(row=0,column=1)
    Label(page,text="CUSTOMER ID",font=("candara light",15,"bold"),fg="midnight blue").grid(row=1,column=0,pady=50)
    Label(page,text="CUSTOMER PASSWORD",font=("candara light",15,"bold"),fg="midnight blue").grid(row=2,column=0)
    Entry(page,textvariable=customerid).grid(row=1,column=1,pady=50)
    Entry(page,textvariable=customerpwd).grid(row=2,column=1)
    Button(page,text="SUMBIT",command=signupcustomer).grid(row=3,column=0,pady=40)
    Button(page,text="RESET",command=servantworkpack).grid(row=3,column=1,pady=40)
    l5=Label(page,text="CREATE ACCOUNT, IF NOT ANY",font=("candara light",12,"underline","bold"),fg="midnight blue")
    l5.grid(row=4,column=0,padx=40)
    l5.bind("<Button-1>",lambda t:customerlogin())

def signupcaretaker():
    import mysql.connector
    obj=mysql.connector.connect(host="localhost",user="root",passwd="tanya1703",database="sercare")
    c=obj.cursor()
    sql="SELECT caretaker_id,caretaker_password FROM caretaker WHERE caretaker_id='{}' and caretaker_password='{}' ".format(caretakerid.get(),caretakerpwd.get()) 
    c.execute(sql)
    y=c.fetchall()
    for k in y:
        if(k[0]==caretakerid.get() and k[1]==caretakerpwd.get()):
            caretakerpage=Toplevel()
            caretakerpage.geometry("1366x768")
            caretakerpage.title("caretaker page")

def signupservant():
    import mysql.connector
    obj=mysql.connector.connect(host="localhost",user="root",passwd="tanya1703",database="sercare")
    c=obj.cursor()
    sql="SELECT servant_id,servant_password,full_name FROM servant WHERE servant_id='{}' and servant_password='{}' ".format(servantid.get(),servantpwd.get()) 
    c.execute(sql)
    y=c.fetchall()
    for k in y:
        if(k[0]==servantid.get() and k[1]==servantpwd.get()):
            servantpage=Toplevel()
            servantpage.geometry("1366x768")
            servantpage.title("servant page")
            Label(servantpage,text="CUSTOMER INFORMATION WHO BOOKED YOU",font=("castellar 28 underline bold"),fg="midnight blue").pack()
            import mysql.connector
            obj=mysql.connector.connect(host="localhost",user="root",passwd="tanya1703",database="sercare")
            c=obj.cursor()
            sql_1="SELECT customer_name,total_amount FROM booking_servant WHERE servant_booked='{}'".format(k[2])
            sql_2="SELECT count(customer_name) FROM booking_servant WHERE servant_booked='{}'".format(k[2]) 
            c.execute(sql_1)
            global y_1
            y_1=c.fetchall()
            #print(y_1)
            c.execute(sql_2)
            y_2=c.fetchall()
            countcustomer=y_2[0][0]
            for i in range(countcustomer):
                sql_3="SELECT full_name FROM customer WHERE customer_id='{}'".format(y_1[i][0])
                c.execute(sql_3)
                y_3=c.fetchall()
                label1=Label(servantpage,text=y_3[0][0],font=("Copperplate Gothic Bold",15,"underline"),fg="midnight blue")
                label1.pack(pady=10)
                label1.bind("<Button-1>",lambda event,i=i: onclicklink(event,i))

def onclicklink(event,i):
    cusinfo=Toplevel()
    cusinfo.geometry("1366x768")
    cusinfo.title("customer details")
    Label(cusinfo,text="CUSTOMER DETAILS",font=("castellar 28 underline bold"),fg="midnight blue").grid(row=0,column=1)
    Label(cusinfo,text="FULL NAME",font=("Copperplate Gothic Bold",15,"bold"),fg="midnight blue").grid(row=1,column=0,pady=10)
    Label(cusinfo,text="D.O.B",font=("Copperplate Gothic Bold",15,"bold"),fg="midnight blue").grid(row=2,column=0,pady=10)
    Label(cusinfo,text="MOBILE NUMBER",font=("Copperplate Gothic Bold",15,"bold"),fg="midnight blue").grid(row=3,column=0,pady=10)
    Label(cusinfo,text="MOBILE NUMBER(2)",font=("Copperplate Gothic Bold",15,"bold"),fg="midnight blue").grid(row=4,column=0,pady=10)
    Label(cusinfo,text="PERMANENT ADDRESS",font=("Copperplate Gothic Bold",15,"bold"),fg="midnight blue").grid(row=5,column=0,pady=10)
    import mysql.connector
    obj=mysql.connector.connect(host="localhost",user="root",passwd="tanya1703",database="sercare")
    c=obj.cursor()
    sql="SELECT full_name,dob,mobile1,mobile2,address FROM customer WHERE customer_id='{}'".format(y_1[i][0]) 
    c.execute(sql)
    y=c.fetchall()
    for k in y:
        Label(cusinfo,text=k[0],font=("Copperplate Gothic Bold",15,"bold"),fg="midnight blue").grid(row=1,column=2,pady=10)
        Label(cusinfo,text=k[1],font=("Copperplate Gothic Bold",15,"bold"),fg="midnight blue").grid(row=2,column=2,pady=10)
        Label(cusinfo,text=k[2],font=("Copperplate Gothic Bold",15,"bold"),fg="midnight blue").grid(row=3,column=2,pady=10)
        Label(cusinfo,text=k[3],font=("Copperplate Gothic Bold",15,"bold"),fg="midnight blue").grid(row=4,column=2,pady=10)
        Label(cusinfo,text=k[4],font=("Copperplate Gothic Bold",15,"bold"),fg="midnight blue").grid(row=5,column=2,pady=10)

    Label(cusinfo,text="TOTAL AMOUNT PAID:",font=("Copperplate Gothic Bold",15,"bold"),fg="midnight blue").grid(row=6,column=1,pady=20)
    Label(cusinfo,text=y_1[i][1],font=("Copperplate Gothic Bold",15,"bold"),fg="midnight blue").grid(row=6,column=2,pady=20)


def forservant():
    page1=Toplevel()
    page1.geometry("1366x768")
    page1.title("Registration")
    frame4=Frame(page1)
    frame4.pack()
    frame5=Frame(page1)
    frame5.pack()
    global servantid,servantpwd,caretakerid,caretakerpwd
    servantid=StringVar()
    servantpwd=StringVar()
    caretakerid=StringVar()
    caretakerpwd=StringVar()
    Label(frame4,text="**SERVANT/CARETAKER REGISTRATION**",font=("castellar",28,"underline","bold"),fg="midnight blue").grid(row=0,column=1)
    Label(frame5,text="SERVANT ID",font=("candara light",15,"bold"),fg="midnight blue").grid(row=1,column=0,pady=50)
    Label(frame5,text="SERVANT PASSWORD",font=("candara light",15,"bold"),fg="midnight blue").grid(row=2,column=0)
    Entry(frame5,textvariable=servantid).grid(row=1,column=1,padx=50)
    Entry(frame5,textvariable=servantpwd).grid(row=2,column=1,padx=50)
    Label(frame5,text="CARETAKER ID",font=("candara light",15,"bold"),fg="midnight blue").grid(row=1,column=2,pady=50)
    Label(frame5,text="CARETAKER PASSWORD",font=("candara light",15,"bold"),fg="midnight blue").grid(row=2,column=2)
    Entry(frame5,textvariable=caretakerid).grid(row=1,column=3)
    Entry(frame5,textvariable=caretakerpwd).grid(row=2,column=3)
    Button(frame5,text="SUBMIT",command=signupservant).grid(row=3,column=0,pady=40)
    Button(frame5,text="RESET").grid(row=3,column=1,pady=40)
    Button(frame5,text="SUBMIT",command=signupcaretaker).grid(row=3,column=2,pady=40)
    Button(frame5,text="RESET").grid(row=3,column=3,pady=40)
    l3=Label(frame5,text="CREATE ACCOUNT,IF NOT ANY(SERVANT)",font=("Candara light",15,"underline","bold"),fg="purple")
    l3.grid(row=4,column=0)
    l3.bind("<Button-1>",lambda c:loginservant())
    l4=Label(frame5,text="CREATE ACCOUNT,IF NOT ANY(CARETAKER)",font=("candara light",15,"underline","bold"),fg="purple")
    l4.grid(row=4,column=2)
    l4.bind("<Button-1>",lambda d:logincaretaker())

root=Tk()
root.geometry("1366x768")
root.title("welcome")
frame1=Frame(root)
frame1.pack()
frame2=Frame(root)
frame2.pack()
frame3=Frame(root)
frame3.pack()
Label(frame1,text="HOME SERVICE FOR SERVANT AND CARETAKER",font=("castellar 28 underline bold"),fg="midnight blue").grid(row=0,column=0)
img1=ImageTk.PhotoImage(Image.open("servant.png"))
Label(frame2,image=img1).grid(row=1,column=0,pady=100)
img2=ImageTk.PhotoImage(Image.open("caretaker.jpg"))
Label(frame2,image=img2).grid(row=1,column=1,pady=100)
l1=Label(frame2,text="CLICK HERE, IF YOU ARE A CUSTOMER",font=("candara light",12,"underline","bold"),fg="midnight blue")
l1.grid(row=2,column=0,padx=50,pady=20)
l1.bind("<Button-1>",lambda a:forcustomer())
l2=Label(frame2,text="CLICK HERE, IF YOU ARE A SERVANT/CARETAKER",font=("candara light",12,"underline","bold"),fg="midnight blue")
l2.grid(row=2,column=1,pady=20)
l2.bind("<Button-1>",lambda b:forservant())
Label(frame3,text="FOR MORE HELP, CONTACT US AT: 8267958148, 9267856947",font=("Copperplate Gothic Bold",15,"bold"),fg="midnight blue").grid(row=3,column=1,pady=20)
'''var=pyttsx3.init()
var1=var.getProperty("voices")
var.setProperty("voice",var1[0].id)
var.setProperty("rate",140)
var.say("hello customer, we provide you the best services of servant and caretaker at your doorstep.")
var.runAndWait()'''
root.mainloop()

