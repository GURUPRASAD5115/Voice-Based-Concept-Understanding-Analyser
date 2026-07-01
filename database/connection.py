import pyodbc

SERVER = "DEVIL"
DATABASE = "VBCUA_DB"

connection_string = f"""
DRIVER={{ODBC Driver 17 for SQL Server}};
SERVER={SERVER};
DATABASE={DATABASE};
Trusted_Connection=yes;
"""

def get_connection():
    try:
        conn = pyodbc.connect(connection_string)
        return conn
    except Exception as e:
        print("Database Connection Error:", e)
        return None