import pandas as pd
from sqlite3 import connect
from tkinter import messagebox


def output_db_csv():
    """
    Exports the records from the 'games_completed' table in the SQLite database to a CSV file.

    This function connects to the 'db_games.sqlite3' database, retrieves all records from the 
    'games_completed' table, and saves them to a CSV file named 'registers.csv'. If the operation 
    is successful, a message box is displayed to inform the user.

    Raises:
        sqlite3.DatabaseError: If there is an issue connecting to the database or executing the query.
        pandas.io.sql.DatabaseError: If there is an issue reading the SQL query into a DataFrame.
        OSError: If there is an issue writing the DataFrame to a CSV file.
    """
    try:
        con = connect("db_games.sqlite3")
        query = """SELECT * FROM games_completed"""
        df = pd.read_sql(query, con)
        df.to_csv("registers.csv", index=False)
        messagebox.showinfo(
            title="Downloaded successfully",
            message="Downloaded table records with success!",
        )
    finally:
        con.close()
