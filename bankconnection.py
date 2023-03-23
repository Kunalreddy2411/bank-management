import mysql.connector as mysql
from tkinter import messagebox
con=mysql.connect(host="localhost",user="root",password="",db="sbi")
def Insert(a,b,c,d,e):
    if(con):
        cursor=con.cursor()
        cursor.execute("insert into bank_info(Name,Pancard_no,Amount,Account_no,Mobile_no)values('"+a+"','"+b+"',"+c+",'"+d+"',"+e+")")
        con.commit()
        messagebox.showinfo("info","Your Account has been created successfully")
    else:
        print("Error in Connection")
def Credit(id,b):
    if(con):
        cursor=con.cursor()
        cursor.execute("select Amount from bank_info where Account_no='"+id+"'")
        result=cursor.fetchall()
        amount=result[0]
        print(amount[0])
        amount=int(amount[0])+int(b)
        print(amount)
        cursor.execute("update bank_info set Amount="+str(amount)+" where Account_no='"+id+"'")
        con.commit()
        return True
def Debit(id,b):
    if(con):
        cursor=con.cursor()
        cursor.execute("select Amount from bank_info where Account_no='"+id+"'")
        result=cursor.fetchall()
        amount=result[0]
        print(amount[0])
        amount=int(amount[0])-int(b)
        print(amount)
        cursor.execute("update bank_info set Amount="+str(amount)+" where Account_no='"+id+"'")
        con.commit()
        return True
def Show(id):
    if(con):
        cursor=con.cursor()
        cursor.execute("select *from bank_info  where Account_no='"+id+"'")
        data=cursor.fetchall()
        return data
