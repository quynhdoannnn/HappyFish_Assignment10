# Name: Group HappyFish (Quynh Doan, Denise Huynh, Sarah Mahan)
# email: doanqb@mail.uc.edu, huynhd2@mail.uc.edu, mahansa@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 11/07/2024 
# Course #/Section: IS 4010-001
# Semester/Year: Fall Semester 2024
# Brief Description of the assignment: In this assignment you will work in teams to develop a VS project that accesses our SQL Server instance, extracts some data from the Grocery Store Simulator database, and produces some interesting results
# Brief Description of what this module does: The queryUtilities.py module defines the fetch_query_results() function, which executes a provided SQL query and retrieves the results from the database. It uses a connection established by connect_to_database(), runs the query, and returns the fetched rows. If an error occurs during the process, the function handles the exception by printing an error message and returning None.
# Citations: N/A
# Anything else that's relevant: N/A

#queryUtilities.py
from dbUtilitiesPackage.dbUtilities import connect_to_database

def fetch_query_results(query):
    """
    Fetch results from the database for a given query.
    This function uses the connection from dbUtilities.

    @param query: SQL query to be executed
    @return: List of rows fetched by the query, or None if there was an error
    """
    conn = connect_to_database() # conn is a connection object or assigned None 
    if conn is None:
        print("Failed to connect to the database.")
        return None

    try:
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result
    except Exception as e:
        print(f"Error executing query: {e}")
        return None

