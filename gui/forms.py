import tkinter as tk


class Forms(tk.Frame):
    _data_structure = {"inventory": ["name", "height", "weight", "width", "deep", "dimension", "unit"],
                       "user": ["firstname", "lastname", "email", "phone_number"],
                       "room_collection": ["name"],
                       "order": ["!!!!!"],
                       "move_size": ["name"],
                       "address": ["house_number", "apartment", "zip_code_id", "street"],
                       "calendar": ["start_date", "end_date", "price_tag_id"],
                       "floor_collection": ["name"],
                       "price_tag": ["name", "price"],
                       "services": ["name"],
                       "street": ["street_name"],
                       "zip_code": ["zip_code", "city", "state"],
                       "truck": ["name", "truck_type_id"],
                       "truck_type": ["price", "length", "height", "width"],
                       }

    def __init__(self, window, form_type=None, *args, **kwargs):
        super().__init__(window, *args, **kwargs)
        self.window = window
        self.form_type = form_type
        self.ent_1 = tk.Entry(self, width=10)
        self.ent_2 = tk.Entry(self, width=10)
        self.ent_3 = tk.Entry(self, width=10)
        self.ent_4 = tk.Entry(self, width=10)
        self.ent_5 = tk.Entry(self, width=10)
        self.ent_6 = tk.Entry(self, width=10)
        self.ent_7 = tk.Entry(self, width=10)
        self.add_button = tk.Button(self, text="Add", command=self.add_data(self.form_type))

    def show_form(self):
        column = 0
        entry_count = 1
        for value in self._data_structure[self.form_type]:
            tk.Label(self, text=f"{value.replace('_', ' ')}",
                     font=("Arial", 13, "bold"), bg='green').grid(row=0, column=column, padx=10)
            eval("self.ent_" + str(entry_count)).grid(row=1, column=column, padx=10, pady=10)
            entry_count += 1
            column += 1
        self.add_button.grid(row=2, column=column // 2, padx=10, pady=10)

    def add_data(self, api_end_point):
        def call_back():
            data = {}
            entry_count = 1
            for value in self._data_structure[self.form_type]:
                data[value] = eval("self.ent_" + str(entry_count) + ".get()")
                entry_count += 1
            self.window.post_data(api_end_point, data)
        return call_back
