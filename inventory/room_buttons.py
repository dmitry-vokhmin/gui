import tkinter as tk


class RoomButtons(tk.Frame):
    def __init__(self, window, *args, **kwargs):
        super().__init__(window, *args, **kwargs)

    def show_buttons(self):
        response_data = self.master.master.get_data("room_collection")
        column = 0
        for inventory in response_data:
            room_name = inventory.get("name")
            tk.Button(self, text=room_name, width=20, height=2, command=self.master.show_data(room_name))\
                .grid(row=0, column=column, padx=5, pady=10)
            column += 1
