import tkinter as tk


class DataBaseButtons(tk.Frame):
    def __init__(self, window, menu_point=None, *args, **kwargs):
        super().__init__(window, *args, **kwargs)
        if menu_point:
            self.menu_point = menu_point
            self.show_buttons()

    def show_buttons(self):
        show_all_button = tk.Button(self, text=f"Show all {self.menu_point.replace('_', ' ')}", width=20, height=2,
                                    command=self.master.show_data(self.master.web_api.get_data, f"{self.menu_point}"))
        show_all_button.grid(row=0, column=0, padx=5, pady=10)
        tk.Label(self, text="Type in id number").grid(row=1, column=1)
        id_entry = tk.Entry(self, width=10)
        id_entry.grid(row=2, column=1, padx=5, pady=10)
        show_single_button = tk.Button(self, text=f"Show single {self.menu_point.replace('_', ' ')}", width=20, height=2,
                                       command=self.master.show_data(self.master.web_api.get_data, f"{self.menu_point}",
                                                                     id_entry))
        show_single_button.grid(row=0, column=1, padx=5, pady=10)
        add_button = tk.Button(self, text=f"Add {self.menu_point.replace('_', ' ')}", width=20, height=2,
                               command=self.master.show_form(f"{self.menu_point}"))
        add_button.grid(row=0, column=2, padx=5, pady=10)
