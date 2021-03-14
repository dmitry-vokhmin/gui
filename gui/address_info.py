import tkinter as tk


class AddressInfo(tk.Frame):
    address = {}
    field_mapper = {"From address": "street",
                    "To address": "street",
                    "From apartment": "apartment",
                    "To apartment": "apartment",
                    "id": "zip_code_id"}

    def __init__(self, window, *args, **kwargs):
        super().__init__(window, *args, **kwargs)
        entry_kwargs = {"master": self, "width": 10}
        self._address_fields = {"address_from_id": {"From address": tk.Entry(**entry_kwargs),
                                                    "From apartment": tk.Entry(**entry_kwargs)},
                                "address_to_id": {"To address": tk.Entry(**entry_kwargs),
                                                  "To apartment": tk.Entry(**entry_kwargs)}}
        self.add_button = tk.Button(self, text="Next", command=self.post_data)

    def get_zip_code_info(self, data):
        for key, zip_code_id in data.items():
            if key == "zip_code_from_id":
                response_data = self.master.get_data("zip_code", api_id=zip_code_id)
                self._address_fields["address_from_id"].update(response_data)
            elif key == "zip_code_to_id":
                response_data = self.master.get_data("zip_code", api_id=zip_code_id)
                self._address_fields["address_to_id"].update(response_data)
        self.show_address_fields()

    def show_address_fields(self):
        column = 0
        for point, values in self._address_fields.items():
            row = 0
            for key, value in values.items():
                if isinstance(value, tk.Entry):
                    tk.Label(self, text=f"{key}", font=("Arial", 13, "bold"),
                             bg='green').grid(row=row, column=column, padx=10)
                    value.grid(row=row + 1, column=column, padx=10, pady=10)
                else:
                    if key != "id":
                        tk.Label(self, text=f"{key}", font=("Arial", 13, "bold"),
                                 bg='green').grid(row=row, column=column, padx=10)
                        tk.Label(self, text=f"{value}").grid(row=row + 1, column=column)
                row += 2
            column += 1
        self.add_button.grid(row=row, column=0)

    def post_data(self):
        for point, values in self._address_fields.items():
            data = {}
            for key, value in values.items():
                if isinstance(value, tk.Entry):
                    data[self.field_mapper[key]] = value.get()
                else:
                    if key == "id":
                        data[self.field_mapper[key]] = value
            response_data = self.master.post_data("address", data)
            self.address[point] = response_data["id"]
        self.master.next_step(self.address)
