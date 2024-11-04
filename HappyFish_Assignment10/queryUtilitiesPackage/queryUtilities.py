#queryUtilities.py
from dbUtilitiesPackage.dbUtilities import connect_to_database

def fetch_query_results(query):
    """
    Fetch results from the database for a given query.
    This function uses the connection from dbUtilities.

    @param query: SQL query to be executed
    @return: List of rows fetched by the query, or None if there was an error
    """
    conn = connect_to_database()
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

