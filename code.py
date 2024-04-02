import mysql.connector
from mysql.connector import Error 

mydb=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="atm"
)
mycursor = mydb.cursor()

print("Welcome to atm")
n=int(input("Press 1 for login and 0 for register"))

password=""
myname=""
depo=""
id=""

if n==0:
    name=input("Enter name: ")
    accn=int(input("Enter account no: "))
    t=int(input("Enter Deposit Amount"))
    pw=int(input("Set Your Password:"))

    myname=name
    password=pw
    deposit=t
    id=accn

    val=(myname,password,depo,id)

    sql= """insert into user_data(my_name, pass_word, de_po, i_d) 
           values(%s,%s,%s,%s) """

    mycursor.execute(sql,val)
    mydb.commit()
    print("successfully inserted data to table")

if n==1:
    info= int(input("Enter ur id: "))
    passw=int(input("Enter the password: "))
    mycursor.execute("select * from atm.user_data where i_d=%s"%(info)) 
    row=mycursor.fetchone()

    if mycursor.rowcount==1:
        mycursor.execute("select * from atm.user_data where pass_word= %s"%(passw))
        row=mycursor.fetchone()

        if mycursor.rowcount==1:
            print("login successful")
            d=int(input("Enter 1 for withdrawl or 0 for deposit and 3 for exit: "))

            if d==1:
                a= int(input("How much you want to withdrawl?: "))
                print(a)   
                mycursor.execute("select de_po from atm.user_data where pass_word=%s" %(passw))
                col=mycursor.fetchone()
                x=list(col)

                for i in x:
                    z=(int(i))
                    c=z-a
                    print(c)   
                mycursor.execute("update atm.user_data set de_po=%s where i_d=%s" %(c,info))

            if d==3:
                exit(0)

        else:
            print("invalid password")

    else:
        print("Account does't exist") 

    mydb.commit() 
