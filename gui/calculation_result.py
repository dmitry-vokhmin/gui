import tkinter as tk


class CalculationResult(tk.Frame):
    def __init__(self, window, *args, **kwargs):
        super().__init__(window, *args, **kwargs)

    def send_data(self, data):
        response_data = self.master.post_data("calculate", data)
        self.show_calc_result(response_data)

    def show_calc_result(self, response_data):
        column = 1
        for key, value in response_data.items():
            tk.Label(self, text=f"{key}", font=("Arial", 13, "bold"),
                     bg='green').grid(row=0, column=column, padx=10)
            tk.Label(self, text=f"{value}").grid(row=1, column=column)
            column += 1
        tk.Button(self, text="Next", command=self.next_step(response_data)).grid(row=2, column=column // 2)

    def next_step(self, data):
        def call_back():
            self.master.next_step(data)
        return call_back
