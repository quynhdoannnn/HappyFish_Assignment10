# Name: Group HappyFish (Quynh Doan, Denise Huynh, Sarah Mahan)
# email: doanqb@mail.uc.edu, huynhd2@mail.uc.edu, mahansa@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 11/07/2024 
# Course #/Section: IS 4010-001
# Semester/Year: Fall Semester 2024
# Brief Description of the assignment: In this assignment you will work in teams to develop a VS project that accesses our SQL Server instance, extracts some data from the Grocery Store Simulator database, and produces some interesting results
# Brief Description of what this module does: The dbUtilities.py module contains the connect_to_database() function, which attempts to connect to a SQL Server database using pyodbc. If successful, it returns the connection object, allowing queries to be executed. If the connection fails, it returns None to signal an error.
# Citations: N/A
# Anything else that's relevant: N/A

# dbUtilities.py

import pyodbc

def connect_to_database():
    """
    Connect to the database
    @return Connection Object: the open connection, or None on error
    """
    try:
        conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                          'Database=GroceryStoreSimulator;'
                          'uid=IS4010Login;'
                          'pwd=P@ssword2;')
    except:
        conn = None

    return conn
