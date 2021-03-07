import tkinter as tk


class MoveInfo(tk.Frame):
    _move = {"move": ["move_date", "move_size", "service", "floor_from", "floor_to", "zip_code_from", "zip_code_to"]}
    _services = ["full move", "loading", "unloading"]
    _move_size = ["Room",
                  "Studio",
                  "1 bedroom apt",
                  "2 bedrooms apt",
                  "3 bedrooms apt",
                  "4+ bedrooms apt",
                  "2 bedrooms house",
                  "3 bedrooms house",
                  "4+ bedrooms house"]
    _floor = ["1st floor", "2nd floor", "3rd floor", "4th floor", "5th floor", "house", "elevator"]

    def __init__(self, window, *args, **kwargs):
        super().__init__(window, *args, **kwargs)
        self.window = window
        self.add_button = tk.Button(self, text="Next", command=self.send_data)
        self.move_date_ent = tk.Entry(self, width=10)
        self.zip_code_from_ent = tk.Entry(self, width=10)
        self.zip_code_to_ent = tk.Entry(self, width=10)
        self.service = tk.StringVar()
        self.service_drop_box = tk.OptionMenu(self, self.service, *self._services)
        self.move_size = tk.StringVar()
        self.move_size_drop_box = tk.OptionMenu(self, self.move_size, *self._move_size)
        self.floor_from = tk.StringVar()
        self.floor_from_drop_box = tk.OptionMenu(self, self.floor_from, *self._floor)
        self.floor_to = tk.StringVar()
        self.floor_to_drop_box = tk.OptionMenu(self, self.floor_to, *self._floor)
        self.show_form()

    def show_form(self):
        for column, value in enumerate(self._move["move"]):
            tk.Label(self, text=f"{value.replace('_', ' ')}",
                     font=("Arial", 13, "bold"), bg='green').grid(row=0, column=column, padx=10)
        else:
            self.add_button.grid(row=2, column=column // 2, padx=10, pady=10)
        self.move_date_ent.grid(row=1, column=0, padx=10, pady=10)
        self.move_size_drop_box.grid(row=1, column=1, padx=10, pady=10)
        self.service_drop_box.grid(row=1, column=2, padx=10, pady=10)
        self.floor_from_drop_box.grid(row=1, column=3, padx=10, pady=10)
        self.floor_to_drop_box.grid(row=1, column=4, padx=10, pady=10)
        self.zip_code_from_ent.grid(row=1, column=5, padx=10, pady=10)
        self.zip_code_to_ent.grid(row=1, column=6, padx=10, pady=10)

    def send_data(self):
        self.window.user_flow.order["move_date"] = self.move_date_ent.get()
        self.window.user_flow.calculations["move_date"] = self.move_date_ent.get()
        self.window.user_flow.calculations["services"] = self.service.get()
        self.window.user_flow.calculations["move_size"] = self.move_size.get()
        self.window.get_move_info_id("zip_code", self.zip_code_from_ent.get())
        self.window.get_move_info_id("zip_code", self.zip_code_to_ent.get())
        self.window.get_move_info_id("floor_collection", self.floor_from.get().replace(" ", "_"))
        self.window.get_move_info_id("floor_collection", self.floor_to.get().replace(" ", "_"))
        self.window.get_move_info_id("services", self.service.get().replace(" ", "_"))
        self.window.get_move_info_id("move_size", self.move_size.get().replace(" ", "_"))
        self.window.user_flow.calculate()
