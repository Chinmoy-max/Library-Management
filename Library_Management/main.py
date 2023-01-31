import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="lmanage"
)


def addbook():
    bname = input("Enter the book name: ")
    bcode = input("Enter book code: ")
    total = input("Total Books: ")
    sub = input("Enter Subject: ")
    data = (bname, bcode, total, sub)
    sql = "insert into addbook values(%s,%s,%s,%s)"
    c = mydb.cursor()
    c.execute(sql, data)
    mydb.commit()
    print(".............")
    print("Data entered successfully")
    main()


def issue():
    name = input("Enter name:")
    rno = input("Enter rno:")
    code = input("Enter book code:")
    date = input("Enter date:")
    data = (name, rno, code, date)
    sql = "insert into issueb values(%s,%s,%s,%s)"

    c = mydb.cursor()
    c.execute(sql, data)
    mydb.commit()
    print("...............")
    print("Book issued to :", name)
    main()
    bookup(code, -1)


def submitb():
    name = input("Enter name:")
    regno = input("Enter rno:")
    code = input("Enter book code:")
    sdate = input("Enter date:")
    sql = "insert into submit(name,regno,bcode,sdate) values(%s,%s,%s,%s)"
    data = (name, regno, code, sdate)
    c = mydb.cursor()
    c.execute(sql, data)
    mydb.commit()
    print("...............")
    print("Book submitted from :", name)
    bookup(code, 1)


def bookup(co, u):
    sql = "select TOTAL from addbook where BCODE = %s"
    data = (co,)
    c = mydb.cursor()
    c.execute(sql, data)
    myresult = c.fetchone()
    t = myresult[0] + u
    sql = "update addbook set TOTAL = %s where BCODE = %s"
    d = (t, co)
    c.execute(sql, d)
    mydb.commit()
    main()


def dbook():
    ac = input("Enter book code:")
    sql = "delete from addbook where BCODE = %s"
    data = (ac,)
    c = mydb.cursor()
    c.execute(sql, data)
    mydb.commit()
    main()


def dispbook():
    sql = "select * from addbook;"
    c = mydb.cursor()
    c.execute(sql)
    myresult = c.fetchall()
    for i in myresult:
        print("Book name:", i[0])
        print("Book code:", i[1])
        print("Total:", i[2])
        print("................")
    main()

def exit():
    print("Thank you for using the system!")



def main():
    print("""............LIBRARY MANAGEMENT.............
        1.Add book
        2.Issue book
        3.Submit book
        4.Delete book
        5.Display book
        6.Exit
        """)
    choice = input("Enter task no:")
    print("............................")
    if choice == '1':
        addbook()
    elif choice == '2':
        issue()
    elif choice == '3':
        submitb()
    elif choice == '4':
        dbook()
    elif choice == '5':
        dispbook()
    elif choice == '6':
        exit()
    else:
        print("wrong choice")
        main()


def password():
    import random
    ps = random.randint(000000, 100000)

    user = input("Enter Username: ")
    print("Your password is:", ps)

    verify = input("Enter password:")

    if verify == str(ps):
        main()
    else:
        verify != str(ps)
        print("wrong password")
        password()


password()


