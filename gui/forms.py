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
        self.form_type = form_type
        self.entries = [tk.Entry(self, width=10) for _ in range(7)]
        self.add_button = tk.Button(self, text="Add", command=self.add_data(self.form_type))

    def show_form(self):
        for entry_count, value in enumerate(self._data_structure[self.form_type]):
            tk.Label(self, text=f"{value.replace('_', ' ')}",
                     font=("Arial", 13, "bold"), bg='green').grid(row=0, column=entry_count, padx=10)
            self.entries[entry_count].grid(row=1, column=entry_count, padx=10, pady=10)
        else:
            self.add_button.grid(row=2, column=entry_count // 2, padx=10, pady=10)

    def add_data(self, api_end_point):
        def call_back():
            data = {}
            for entry_count, value in enumerate(self._data_structure[self.form_type]):
                data[value] = self.entries[entry_count].get()
            self.master.post_data(api_end_point, data)
        return call_back
