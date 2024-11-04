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
