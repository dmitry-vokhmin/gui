import tkinter as tk


class MoveInfo(tk.Frame):
    _move_info_data = {}
    _move = {"move": ["move_date", "move_size", "service", "zip_code_from", "zip_code_to", "floor_from", "floor_to"]}

    def __init__(self, window, *args, **kwargs):
        super().__init__(window, *args, **kwargs)
        entry_kwargs = {"master": self, "width": 10}
        self.field_mapper = {"move_date": {"field": tk.Entry, "kwargs": entry_kwargs},
                             "service": ({"field": tk.StringVar, "kwargs": {}},
                                          {"field": tk.OptionMenu, "args": self.get_data("service")}),
                             "move_size": ({"field": tk.StringVar, "kwargs": {}},
                                          {"field": tk.OptionMenu, "args": self.get_data("move_size")}),
                             "zip_code_from": {"field": tk.Entry, "kwargs": entry_kwargs},
                             "zip_code_to": {"field": tk.Entry, "kwargs": entry_kwargs},
                             "floor_collection_from": ({"field": tk.StringVar, "kwargs": {}},
                                          {"field": tk.OptionMenu, "args": self.get_data("floor_collection")}),
                             "floor_collection_to": ({"field": tk.StringVar, "kwargs": {}},
                                          {"field": tk.OptionMenu, "args": self.get_data("floor_collection")})
                             }
        self.add_button = tk.Button(self, text="Next", command=self.send_data)
        self.fields = {}
        for key, field in self.field_mapper.items():
            if isinstance(field, dict):
                self.fields[key] = field["field"](**field["kwargs"])
            elif isinstance(field, tuple):
                tmp = field[0]["field"](**field[0]["kwargs"])
                self.fields[key] = (field[1]["field"](self, tmp, *field[1]["args"]), tmp)
        self.show_form()

    def show_form(self):
        for column, value in enumerate(self._move["move"]):
            tk.Label(self, text=f"{value.replace('_', ' ')}",
                     font=("Arial", 13, "bold"), bg='green').grid(row=0, column=column, padx=10)
        else:
            self.add_button.grid(row=2, column=column // 2, padx=10, pady=10)
        for column, field in enumerate(self.fields.values()):
            if isinstance(field, tuple):
                field[0].grid(row=1, column=column, padx=10, pady=10)
            else:
                field.grid(row=1, column=column, padx=10, pady=10)

    def send_data(self):
        for key, field in self.fields.items():
            if key == "move_date":
                self._move_info_data[key] = field.get()
                continue
            elif isinstance(field, tuple):
                response_data = self.master.get_data(key, query_param=f"?q={field[1].get()}")
            else:
                response_data = self.master.get_data(key, query_param=f"?q={field.get()}")
            self._move_info_data[key + "_id"] = response_data["id"]
        self.master.next_step(self._move_info_data)

    def get_data(self, api_end_point):
        response_data = self.master.get_data(api_end_point)
        return [value for dicts in response_data for key, value in dicts.items() if key == "name"]
