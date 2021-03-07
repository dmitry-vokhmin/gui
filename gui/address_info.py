import tkinter as tk


class AddressInfo(tk.Frame):
    _address_fields = ["from_address", "from_apt", "to_address", "to_apt"]
    address = {}

    def __init__(self, window, user_flow, *args, **kwargs):
        super().__init__(window, *args, **kwargs)
        self.window = window
        self.user_flow = user_flow
        self.entries = [tk.Entry(self, width=10) for _ in range(4)]
        self.add_button = tk.Button(self, text="Next", command=self.post_data)

    def show_address_fields(self):
        column = 0
        row = 0
        for entry_count, field in enumerate(self._address_fields):
            if entry_count == 2:
                column += 1
                row = 0
            tk.Label(self, text=f"{field}", font=("Arial", 13, "bold"),
                     bg='green').grid(row=row, column=column, padx=10)
            self.entries[entry_count].grid(row=row + 1, column=column, padx=10, pady=10)
            row += 2
        column = 0
        for zip_id in self.user_flow.order["zip_code"]:
            row_zip = row
            response_code, response_data = self.window.web_api.get_data("zip_code", str(zip_id))
            for key, value in response_data.items():
                if key != "id":
                    tk.Label(self, text=f"{key}", font=("Arial", 13, "bold"),
                             bg='green').grid(row=row_zip, column=column, padx=10)
                    tk.Label(self, text=f"{value}").grid(row=row_zip + 1, column=column)
                    row_zip += 2
            column += 1
        else:
            self.add_button.grid(row=row_zip, column=0)

    def post_data(self):
        count = 0
        for idx, entry in enumerate(self.entries):
            if idx % 2 == 0:
                house, street = entry.get().split(" ", 1)
                self.address["house_number"] = house
                self.address["street"] = street
            else:
                apartment = entry.get()
                if apartment:
                    self.address["apartment"] = apartment
                self.address["zip_code_id"] = self.user_flow.order["zip_code"][count]
                response_code, response_data = self.window.web_api.post_data("address", self.address)
                self.user_flow.order["address_id"].append(response_data["id"])
                count += 1
