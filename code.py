import mysql.connector
from mysql.connector import Error 

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="atm"
)
mycursor = mydb.cursor()

print("Welcome to ATM")
n = int(input("Press 1 for login and 0 for register: "))

if n == 0:
    name = input("Enter name: ")
    accn = int(input("Enter account no: "))
    deposit = int(input("Enter Deposit Amount: "))
    pw = input("Set Your Password: ")

    val = (name, pw, deposit, accn) 
    sql = """INSERT INTO user_data (my_name, pass_word, de_po, accn) 
             VALUES (%s, %s, %s, %s)"""

    mycursor.execute(sql, val)
    mydb.commit()
    print("Account created succesfully!!!")

if n == 1:
    info = int(input("Enter your account number: "))
    passw = input("Enter the password: ")

    # Execute the first query to check if the account exists and the password is correct
    mycursor.execute("SELECT * FROM atm.user_data WHERE accn = %s AND pass_word = %s", (info, passw))
    row = mycursor.fetchone()

    if row:
        print("Login successful")
        d = int(input("Enter 1 for withdrawal, 0 for deposit, and 2 for exit: "))

        if d == 1:
            withdrawal_amount = int(input("Enter the withdrawal amount: "))
            current_balance = row[3]
            if current_balance >= withdrawal_amount:
                new_balance = current_balance - withdrawal_amount
                mycursor.execute("UPDATE atm.user_data SET de_po = %s WHERE accn = %s", (new_balance, info))
                mydb.commit()
                print("Withdrawal successful")
                print("Remaining balance:", new_balance)
            else:
                print("Insufficient funds for withdrawal")
        elif d == 0:
            deposit_amount = int(input("Enter the deposit amount: "))
            new_balance = row[3] + deposit_amount
            mycursor.execute("UPDATE atm.user_data SET de_po = %s WHERE accn = %s", (new_balance, info))
            mydb.commit()
            print("Deposit successful")
            print("Remaining balance:", new_balance)
        elif d == 2:
            exit(0)
    else:
        print("Invalid account number or password")

    
    mydb.commit()
