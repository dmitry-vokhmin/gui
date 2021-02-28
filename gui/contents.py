import tkinter as tk


class Contents(tk.Frame):
    def __init__(self, window, *args, **kwargs):
        super().__init__(window, *args, **kwargs)
        self.window = window

    def data_structure(self, data, row=1):
        column = 1
        if isinstance(data, list):
            for itm in data:
                row = self.data_structure(itm, row=row)
        if isinstance(data, dict):
            for key, value in data.items():
                if row == 1:
                    tk.Label(self, text=f"{key}", font=("Arial", 13, "bold"),
                             bg='green').grid(row=0, column=column, padx=10)
                    tk.Label(self, text="count", font=("Arial", 13, "bold"),
                             bg='green').grid(row=0, column=0, padx=10)
                tk.Label(self, text=f"{value}").grid(row=row, column=column)
                tk.Label(self, text=f"{row}").grid(row=row, column=0)
                column += 1
            row += 1
        return row
