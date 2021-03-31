import tkinter as tk
from collections import defaultdict


class Contents(tk.Frame):
    # TODO: Сравнение нового inventory с preset и загрузить его в базу
    inventory = []

    def __init__(self, window, *args, **kwargs):
        super().__init__(window, *args, **kwargs)
        self.inv_listbox = tk.Listbox(self, selectmode="multiple")
        self.inv_listbox.grid(row=0, column=0)
        self.selected = tk.Listbox(self, selectmode="multiple")
        self.selected.grid(row=0, column=2)
        self.add_button = tk.Button(self, text="Add", command=self.add_inventory).grid(row=1, column=0)
        self.del_button = tk.Button(self, text="Delete", command=self.delete_inventory).grid(row=1, column=1)
        self.submit_button = tk.Button(self, text="Submit", command=self.submit_inventory).grid(row=1, column=2)
        self.selected_inventory()

    def data_structure(self, data, move_size):
        for inventory in data:
            self.inv_listbox.insert("end", inventory["name"])
        response_data = self.master.master.get_data("room_inventory", move_size)
        for inventory in response_data:
            self.inventory.append(inventory.get("name", []))
        self.selected_inventory()

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
        dict_inventory = defaultdict(int)
        for itm in self.inventory:
            dict_inventory[itm] += 1
        self.master.master.user_flow.inventory.clear()
        # Возможно поменять \/
        self.master.master.user_flow.inventory.update(dict_inventory)
        self.master.destroy()

    def selected_inventory(self):
        size = self.selected.size()
        self.selected.delete(0, size)
        for itm in self.inventory:
            self.selected.insert("end", itm)
