import tkinter as tk


class Contents(tk.Frame):
    def __init__(self, window, *args, **kwargs):
        super().__init__(window, *args, **kwargs)

    def data_structure(self, data, row=1):
        if isinstance(data, list):
            for row, itm in enumerate(data, 1):
                self.data_structure(itm, row)
        if isinstance(data, dict):
            column = 1
            for key, value in data.items():
                if row == 1:
                    tk.Label(self, text=f"{key}", font=("Arial", 13, "bold"),
                             bg='green').grid(row=0, column=column, padx=10)
                    tk.Label(self, text="count", font=("Arial", 13, "bold"),
                             bg='green').grid(row=0, column=0, padx=10)
                tk.Label(self, text=f"{value}").grid(row=row, column=column)
                tk.Label(self, text=f"{row}").grid(row=row, column=0)
                column += 1
