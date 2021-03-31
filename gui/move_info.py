from datetime import timedelta, datetime
from collections import defaultdict
import tkinter as tk
from inventory.inventory_window import InventoryWindow


class MoveInfo(tk.Frame):
    _move_info_data = {}
    _move = {"move": ["move_date", "service", "move_size", "zip_code_from", "zip_code_to", "floor_from", "floor_to"]}

    def __init__(self, window, *args, **kwargs):
        super().__init__(window, *args, **kwargs)
        entry_kwargs = {"master": self, "width": 10}
        self.field_mapper = {"move_date": ({"field": tk.StringVar, "kwargs": {}},
                                           {"field": tk.OptionMenu, "args": self.get_data("calendar")}),
                             "service": ({"field": tk.StringVar, "kwargs": {}},
                                         {"field": tk.OptionMenu, "args": self.get_data("service")}),
                             "move_size": ({"field": tk.StringVar, "kwargs": {}},
                                           {"field": tk.OptionMenu, "args": self.get_data("move_size")}),
                             "zip_code_from": {"field": tk.Entry, "kwargs": entry_kwargs},
                             "zip_code_to": {"field": tk.Entry, "kwargs": entry_kwargs},
                             "floor_collection_from": ({"field": tk.StringVar, "kwargs": {}},
                                                       {"field": tk.OptionMenu,
                                                        "args": self.get_data("floor_collection")}),
                             "floor_collection_to": ({"field": tk.StringVar, "kwargs": {}},
                                                     {"field": tk.OptionMenu,
                                                      "args": self.get_data("floor_collection")})
                             }
        self.add_button = tk.Button(self, text="Next", command=self.send_data)
        self.fields = {}
        for key, field in self.field_mapper.items():
            if isinstance(field, dict):
                self.fields[key] = field["field"](**field["kwargs"])
            elif isinstance(field, tuple):
                string_var = field[0]["field"](**field[0]["kwargs"])
                if key == "move_size":
                    self.fields[key] = (field[1]["field"](self, string_var, *field[1]["args"],
                                                          command=self.trace_selection), string_var)
                else:
                    self.fields[key] = (field[1]["field"](self, string_var, *field[1]["args"]), string_var)
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
                self._move_info_data[key] = field[1].get()
                continue
            elif isinstance(field, tuple):
                response_data = self.master.get_data(key, query_param=f"?q={field[1].get()}")
            else:
                response_data = self.master.get_data(key, query_param=f"?q={field.get()}")
            if key == "move_size":
                self._move_info_data["inventory"] = self.get_inventory(field[1].get())
            self._move_info_data[key + "_id"] = response_data["id"]
        self.master.next_step(self._move_info_data)

    def get_data(self, api_end_point):
        response_data = self.master.get_data(api_end_point)
        if api_end_point == "calendar":
            calendar = []
            for dicts in response_data:
                start_date = datetime.strptime(dicts["start_date"], "%Y-%m-%d")
                end_date = datetime.strptime(dicts["end_date"], "%Y-%m-%d")
                delta = end_date - start_date
                calendar.extend([(start_date + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(delta.days + 1)])
            return calendar
        return [value for dicts in response_data for key, value in dicts.items() if key == "name"]

    def add_inventory(self, selection):
        def call_back():
            InventoryWindow(self.master, selection)
        return call_back

    def trace_selection(self, *args):
        selection = self.fields["move_size"][1].get()
        inventory_button = tk.Button(self, text="Add Inventory", command=self.add_inventory(selection))
        inventory_button.grid(row=2, column=2, padx=10, pady=10)

    def get_inventory(self, move_size):
        inventory = defaultdict(int)
        response_data = self.master.get_data("room_inventory", move_size)
        for elem in response_data:
            inventory[elem.get("name", [])] += 1
        return inventory
