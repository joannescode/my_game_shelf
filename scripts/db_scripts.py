import sqlite3
from tkinter import messagebox


def _validate_infos(name, platform, rating, duration):
    """Validação das informações inseridas via interface tkintetr

    Args:
        name (str): nome do jogo a ser registrado
        platform (str): plataforma em que foi jogado o jogo a ser registrado
        rating (float): avaliação do jogador referente ao jogo a ser registrado
        duration (str): tempo de jogo até a conclusão a ser registrado

    Returns:
        (str, float): valores a serem inseridas na tabela do banco de dados
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
    """Inserção das informações dentro do banco de dados

    Args:
        name (str): nome do jogo a ser registrado
        platform (str): plataforma em que foi jogado o jogo a ser registrado
        rating (float): avaliação do jogador referente ao jogo a ser registrado
        duration (str): tempo de jogo até a conclusão a ser registrado
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
        messagebox.showinfo(title="Registered successfully", message="Game registered successfully!")

    except Exception as e:
        messagebox.showerror(
            title="Critical Error - Insert Info",
            message=f"Error to try insert info: {e}",
        )
    finally:
        con.close()
