# Admission Management system
# 1.Add student
# 2.delete student
# 3.update student
# 4.show student
# 5.exit

import mysql.connector as m
# mydatabase=m.connect(host="localhost",user="root",password="root",database="student")
# cursor=mydatabase.cursor()
# cursor.execute("create database student")
mydatabase=m.connect(host="localhost",user="root",password="root",database="student")
cursor=mydatabase.cursor()
# cursor.execute("create table if not exits admission(rollno int primary key auto_increment,name varchar(30),gender varchar(10),age int,addr varchar(30),course varchar(10),contact varchar(10))")
# cursor.execute("alter table admission auto_increment=1200");
def addstu():
    try:
        query="insert into admission(name,gender,age,addr,course,contact) values(%s,%s,%s,%s,%s,%s)"
        name=input("Enter your FullName = ")
        gender=input("Enter your gender = ")
        age=int(input("Enter your age = "))
        addr=input("Enter your address = ")
        course=input("Enter in which division you want to take admission = ")
        contact=input("Enter your 10 digit contact no = ")
        if age>5 and age<60 and len(contact)==10 and gender==("male" or "female"):
            len(contact)==10
            mydatabase.cursor()
            cursor.execute(query,[name,gender,age,addr,course,contact])
            mydatabase.commit()
            query2=f"select rollno from admission where name='{name}' and gender='{gender}'"
            mydatabase.cursor()
            cursor.execute(query2)
            f=cursor.fetchall()
            print(f"Student is added successfully and your roll no is {f[0][0]}")
            start()
        else:
            print("\n")
            print("Enter Valid details")
            print("\n")
            addstu()
    except Exception:
        print("Invalid Input")
        start()
        
def delstu():
    try: 
        a=int(input("Enter rollno to remove a student  = "))
        name=input("Enter a name of student which you want to delete = ")
        query=f"delete from admission where rollno='{a}' and name='{name}'"
        mydatabase.cursor()
        cursor.execute(query)
        mydatabase.commit()
        print(f"{name} is successfully removed from the database")
        start()
    except Exception:
        print("Enter valid name and roll no of a student")
        delstu()

def updatestu():
    try:
        rollno=int(input("Enter rollno which of student which you want to update = "))
        print("1.For changing the age")
        print("2.For changing the contact")
        print("3.For changing the address")
        choice=int(input("Enter your choice = "))
        match choice:
            case 1:
                age=int(input("Enter a age you want to update = "))
                if age>4 and age<60:
                    query2=f"update admission set age='{age}' where rollno='{rollno}'"
                    mydatabase.cursor()
                    cursor.execute(query2)
                    mydatabase.commit()
                    print("Age is successfully updated")
                    start()
                else:
                    print("Invalid age,please try again")
                    start()
            case 2:
                contact=input("Enter a contact you want to update = ")
                print(contact)
            
                print(contact)
                if len(contact)==10:
                    query2=f"update admission set contact='{contact}' where rollno='{rollno}'"
                    mydatabase.cursor()
                    cursor.execute(query2)
                    mydatabase.commit()
                    print("Contact no is successfully updated")
                    start()
                else:
                    print("Invalid contact no,please try again")
                    start()
            case 3:
                add=input("Enter a address you want to update = ")
                query2=f"update admission set addr='{add}' where rollno='{rollno}'"
                mydatabase.cursor()
                cursor.execute(query2)
                mydatabase.commit()
                print("Address is successfully updated")
                start()
            case _:
                print("Try again")
                updatestu()
    except Exception:
        print("Invalid input,try again")
        start()
        
    
def showstu():
    try:
        rollno=int(input("Enter rollno of a student to show the details of the student = "))
        query=f"select * from admission where rollno='{rollno}'"
        mydatabase.cursor()
        cursor.execute(query)
        a=cursor.fetchall()
        print(f"Rollno = '{a[0][0]}'","\n",f"Name ='{a[0][1]}'","\n",f"Gender = '{a[0][2]}'","\n",f"Age = '{a[0][3]}'","\n",f"Address = '{a[0][4]}'","\n",f"Course = '{a[0][5]}'","\n",f"Contact no = '{a[0][6]}'")
        start()
    except Exception:
        print("Invalid lnput,try again")
        start()
        
def start():
    print("\n")
    print("\n")
    print("                 Admission Management System             ")
    print("=============================Menu==================================")
    print("1.Add Student")
    print("2.Delete Student")
    print("3.Update Student")
    print("4.Show Student")
    print("0.Exit")
 
    choice = int(input("Enter your choice : "))
    match choice:
        case 1:
            addstu()
        case 2:
            delstu()
        case 3:
            updatestu()
        case 4:
            showstu()
        case 0:
            exit()
        case _:
            print("Invalid Entry,Please try again")
            start()
start()