import tkinter as tk


class Forms(tk.Frame):
    _data_structure = {"calendar": ["start_date", "end_date", "price_tag_id"],
                       "price_tag": ["name", "price"],
                       "mover_price": ["amount", "price"],
                       "truck": ["name", "truck_type_id", "truck_id"],
                       "truck_type": ["price", "length", "height", "width", "trucks_type_id"],
                       }

    def __init__(self, window, form_type=None, crud=None, *args, **kwargs):
        super().__init__(window, *args, **kwargs)
        self.form_type = form_type
        self.crud = crud
        self.entries = [tk.Entry(self, width=10) for _ in range(7)]
        self.add_button = tk.Button(self, text=self.crud, command=self.add_data(self.form_type, self.crud))

    def show_form(self):
        for entry_count, value in enumerate(self._data_structure[self.form_type]):
            tk.Label(self, text=value, font=("Arial", 13, "bold"), bg='green').grid(row=0, column=entry_count, padx=10)
            self.entries[entry_count].grid(row=1, column=entry_count, padx=10, pady=10)
        else:
            self.add_button.grid(row=2, column=entry_count // 2, padx=10, pady=10)

    def add_data(self, api_end_point, crud):
        def call_back():
            update_id = ""
            data = {}
            for entry_count, value in enumerate(self._data_structure[self.form_type]):
                if value == "truck_id" or value == "trucks_type_id":
                    update_id = self.entries[entry_count].get()
                else:
                    data[value] = self.entries[entry_count].get()
            if crud in ["Update", "Delete"]:
                self.master.put_data(api_end_point, data, update_id)
            else:
                self.master.post_data(api_end_point, data)
        return call_back
