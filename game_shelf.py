import tkinter as tk
from tkinter import messagebox
from scripts.db_scripts import insert_game
from scripts.scripts_data import output_db_csv


def main():
    try:
        root = tk.Tk()
        root.title("Register your game")
        frm = tk.Frame(root, pady=5, padx=10)
        frm.grid()

        name = tk.Label(frm, text="Name game:")
        name.grid(row=0, column=0)
        input_name = tk.Entry(frm, width=30)
        input_name.grid(row=0, column=1)
        platform = tk.Label(frm, text="Platform:")
        platform.grid(row=1, column=0)
        input_platform = tk.Entry(frm, width=30)
        input_platform.grid(row=1, column=1)
        rating = tk.Label(frm, text="Rating:")
        rating.grid(row=2, column=0)
        input_rating = tk.Entry(frm, width=30)
        input_rating.grid(row=2, column=1)
        duration = tk.Label(frm, text="Duration:")
        duration.grid(row=3, column=0)
        input_duration = tk.Entry(frm, width=30)
        input_duration.grid(row=3, column=1)
        bt_register = tk.Button(
            frm,
            activebackground="snow",
            width=15,
            text="Register Game",
            padx=2,
            command=lambda: insert_game(
                input_name.get(),
                input_platform.get(),
                input_rating.get(),
                input_duration.get(),
            ),
        )
        bt_register.grid(row=5, column=0, columnspan=1, pady=15)

        bt_save_to_csv = tk.Button(
            frm,
            activebackground="snow",
            width=25,
            text="Download Registers in CSV",
            padx=2,
            command=output_db_csv,
        )
        bt_save_to_csv.grid(row=5, column=1, columnspan=1, pady=15)
        root.mainloop()

    except Exception as e:
        messagebox.showerror(
            title="Critical Error",
            message=f"Error to try start or interact with screen register: {e}",
        )
        raise


if __name__ == '__main__':
    main()
