import tkinter as tk


class CalculationResult(tk.Frame):
    def __init__(self, window, user_flow, *args, **kwargs):
        super().__init__(window, *args, **kwargs)
        self.user_flow = user_flow

    def show_calc_result(self):
        column = 1
        for key, value in self.user_flow.calculations.items():
            tk.Label(self, text=f"{key}", font=("Arial", 13, "bold"),
                     bg='green').grid(row=0, column=column, padx=10)
            tk.Label(self, text=f"{value}").grid(row=1, column=column)
            column += 1
        tk.Button(self, text="Next", command=self.user_flow.address_info).grid(row=2, column=column // 2)
