import tkinter as tk


class PersonalInfo(tk.Frame):
    _user = {"user": ["firstname", "lastname", "email", "phone_number"]}
    user_data = {}

    def __init__(self, window, *args, **kwargs):
        super().__init__(window, *args, **kwargs)
        self.entries = [tk.Entry(self, width=10) for _ in range(4)]
        self.add_button = tk.Button(self, text="Next", command=self.add_data("user"))
        self.show_form()

    def show_form(self):
        for entry_count, value in enumerate(self._user["user"]):
            tk.Label(self, text=f"{value.replace('_', ' ')}",
                     font=("Arial", 13, "bold"), bg='green').grid(row=0, column=entry_count, padx=10)
            self.entries[entry_count].grid(row=1, column=entry_count, padx=10, pady=10)
        else:
            self.add_button.grid(row=2, column=entry_count // 2, padx=10, pady=10)

    def add_data(self, api_end_point):
        def call_back():
            data = {}
            for entry_count, value in enumerate(self._user["user"]):
                data[value] = self.entries[entry_count].get()
            response_data = self.master.post_data(api_end_point, data)
            self.user_data[api_end_point + "_id"] = response_data["id"]
            self.master.next_step(self.user_data)
        return call_back
