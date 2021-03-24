import tkinter as tk
from .room_buttons import RoomButtons
from .contents import Contents


class InventoryWindow(tk.Toplevel):
    def __init__(self, window, *args, **kwargs):
        super().__init__(window, *args, **kwargs)
        self.title("Inventory")
        self.geometry("800x600")
        self.room_buttons = RoomButtons(self)
        self.contents_frame = Contents(self)
        self.show_rooms()

    def show_rooms(self):
        self.room_buttons.grid(row=0, column=0, sticky=tk.N, padx=20)
        self.room_buttons.show_buttons()

    def show_data(self, room_name):
        def call_back():
            self.contents_frame.destroy()
            self.contents_frame = Contents(self)
            self.contents_frame.grid(row=1, column=0, sticky=tk.S, padx=20)
            response_data = self.master.get_data("room_inventory", room_name)
            self.contents_frame.data_structure(response_data)
        return call_back
