#!/usr/local/bin/python3
import mysql.connector

con = mysql.connector.connect(host="localhost",
                              database="mydb",
                              user="root",
                              password="toor")

if con.is_connected():
    print("Connected to database.")
else:
    print("Failed to connect to database.")


def addEmployee(id, name, salary):
    cursor = con.cursor()
    try:
        cursor.execute("INSERT INTO emp values(%i, '%s', %i);" %
                       (id, name, salary))
        con.commit()
        print("Employee added to database.")
    except:
        con.rollback()
    finally:
        cursor.close()


def deleteEmployee(id):
    cursor = con.cursor()
    try:
        cursor.execute("DELETE from emp where id=%i" % id)
        con.commit()
        print("Employee removed from the database.")
    except:
        con.rollback()
    finally:
        cursor.close()


def updateSalary(id, salary):
    cursor = con.cursor()
    try:
        cursor.execute("UPDATE emp SET sal=%i WHERE id=%i" % (salary, id))
        con.commit()
        print("Employee salary has been updated.")
    except:
        con.rollback()
    finally:
        cursor.close()


def getEmployee(id):
    cursor = con.cursor()
    try:
        cursor.execute("SELECT * from emp where id=%i" % id)
        row = cursor.fetchone()
        print(row)
    except:
        print("Unable to retrieve employee.")
    finally:
        cursor.close()


def getAllEmployees():
    cursor = con.cursor()
    cursor.execute("SELECT * from emp")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()


getAllEmployees()
addEmployee(4, "Clyde", 0)
updateSalary(3, 75000)
getEmployee(4)
deleteEmployee(4)
getAllEmployees()

con.close()
