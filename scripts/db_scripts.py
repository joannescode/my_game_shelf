import sqlite3
from tkinter import messagebox


def _validate_infos(name, platform, rating, duration):
    """Validation about information where was inserted through tkinter interface

    Args:
        name (str): games name for resgiter
        platform (str): plataform that was played for register
        rating (float): rating of player about game for register
        duration (str): game time of conclusion for register

    Returns:
        (str, float): values for insert in database
    """
    try:
        if name and platform and rating and duration:
            float_rating = float(rating)
            return name, platform, float_rating, duration
    except ValueError:
        messagebox.showwarning(
            title="Warning - Validate Infos",
            message="Invalid Input, Rating and Duration must be numbers.",
        )
    except Exception as e:
        messagebox.showerror(
            title="Critical Error - Validated Infos",
            message=f"Error during validation or insertion: {e}",
        )


def insert_game(name, platform, rating, duration):
    """Insert informations in database
    Args:
        name (str): games name for resgiter
        platform (str): plataform that was played for register
        rating (float): rating of player about game for register
        duration (str): game time of conclusion for register
    """
    try:
        name_validated, platform_validated, rating_validated, duration_validated = (
            _validate_infos(name, platform, rating, duration)
        )

        con = sqlite3.connect("db_games.sqlite3")
        cur = con.cursor()
        cur.execute(
            """insert into games_completed(name,platform,rating,duration) VALUES(?,?,?,?)""",
            (name_validated, platform_validated, rating_validated, duration_validated),
        )

        con.commit()
        messagebox.showinfo(
            title="Registered successfully", message="Game registered successfully!"
        )

    except Exception as e:
        messagebox.showerror(
            title="Critical Error - Insert Info",
            message=f"Error to try insert info: {e}",
        )
    finally:
        con.close()
