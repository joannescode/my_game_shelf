import pandas as pd
from sqlite3 import connect
from tkinter import messagebox


def output_db_csv():
    """Retorna as informações preenchidas no banco em formato CSV"""
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
