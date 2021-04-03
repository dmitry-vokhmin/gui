import tkinter as tk


class ManyForm(tk.Frame):
    inventory = []

    def __init__(self, window, api_end_point=None, *args, **kwargs):
        super().__init__(window, *args, **kwargs)
        self.api_end_point = api_end_point
        self.api_id = ""
        self.inv_listbox = tk.Listbox(self, selectmode="multiple")
        self.inv_listbox.grid(row=1, column=0)
        self.selected = tk.Listbox(self, selectmode="multiple")
        self.selected.grid(row=1, column=2)
        self.add_button = tk.Button(self, text="Add", command=self.add_inventory).grid(row=2, column=0)
        self.del_button = tk.Button(self, text="Delete", command=self.delete_inventory).grid(row=2, column=1)
        self.submit_button = tk.Button(self, text="Submit", command=self.submit_inventory).grid(row=2, column=2)
        self.selected_inventory()

    def data_structure(self):
        response_data = self.master.get_data("room_inventory", "all")
        for inventory in response_data:
            self.inv_listbox.insert("end", inventory["name"])
        response_data = self.master.get_data(self.api_end_point)
        self.show_buttons(response_data)

    def show_buttons(self, response_data):
        for column, data in enumerate(response_data):
            tk.Button(self, text=data["move_size"]["name"], width=15, height=2,
                      command=self.get_button_choice(data["move_size"]["id"])).grid(row=0, column=column)

    def add_inventory(self):
        for line in self.inv_listbox.curselection():
            self.inventory.append(self.inv_listbox.get(line))
        self.selected_inventory()

    def delete_inventory(self):
        for line in self.selected.curselection():
            a = self.selected.get(line)
            self.inventory.pop(self.inventory.index(a))
            self.selected.delete(line)

    def submit_inventory(self):
        self.master.post_data(self.api_end_point, self.inventory, self.api_id)

    def selected_inventory(self):
        size = self.selected.size()
        self.selected.delete(0, size)
        for itm in self.inventory:
            self.selected.insert("end", itm)

    def get_button_choice(self, api_id):
        def call_back():
            self.api_id = api_id
            response_data = self.master.get_data("room_inventory", api_id)
            for inventory in response_data:
                self.inventory.append(inventory.get("name", []))
            self.selected_inventory()
        return call_back
