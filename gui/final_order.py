import tkinter as tk


class FinalOrder(tk.Frame):
    def __init__(self, window, *args, **kwargs):
        super().__init__(window, *args, **kwargs)

    def show_order(self, data, row=0, column=0):
        for key, value in data.items():
            if isinstance(value, dict):
                tk.Label(self, text=f"{key}", font=("Arial", 15, "bold"),
                         bg='Blue').grid(row=0, column=column + 1, padx=10)
                column = self.show_order(value, row=1, column=column + 1)
            elif key == "id":
                continue
            elif key == "name":
                tk.Label(self, text=f"{value}").grid(row=row, column=column)
                row += 1
            else:
                tk.Label(self, text=f"{key}", font=("Arial", 13, "bold"),
                         bg='green').grid(row=row, column=column, padx=10)
                tk.Label(self, text=f"{value}").grid(row=row + 1, column=column)
                row += 2
        return column

    def post_order(self, data):
        response_data = self.master.post_data("order", data)
        self.show_order(response_data)
