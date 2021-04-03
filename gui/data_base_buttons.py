import tkinter as tk


class DataBaseButtons(tk.Frame):
    def __init__(self, window, menu_point=None, *args, **kwargs):
        super().__init__(window, *args, **kwargs)
        self.menu_point = menu_point
        self.crud = ""
        show_form_command = "self.master.show_form(self.menu_point, self.crud)"
        show_data_command = "self.master.show_data(self.menu_point)"
        show_many_to_many_command = "self.master.show_many_form(self.menu_point)"
        self._menu_mapper = {"inventory_collection": [("Add/delete Many to Many", show_many_to_many_command)],
                             "calendar": [("Add dates", show_form_command, "Add"),
                                          ("Get all dates", show_data_command),
                                          ("Delete date", show_form_command, "Delete"),
                                          ("Update date", show_form_command, "Update")],
                             "price_tag": [("Update Price tag", show_form_command, "Update"),
                                           ("Get all Price tags", show_data_command)],
                             "mover_price": [("Update Mover Price", show_form_command, "Update"),
                                             ("Get all Mover Prices", show_data_command)],
                             "truck": [("Add truck", show_form_command, "Add"),
                                       ("Get all truck", show_data_command),
                                       ("Delete truck", show_form_command, "Delete"),
                                       ("Update truck", show_form_command, "Update")],
                             "truck_type": [("Add Truck type", show_form_command, "Add"),
                                            ("Get all Truck types", show_data_command),
                                            ("Update Truck type", show_form_command, "Update"),
                                            ("Delete Truck type", show_form_command, "Delete")],
                             }

    def show_buttons(self):
        for column, label in enumerate(self._menu_mapper[self.menu_point]):
            if len(label) > 2:
                self.crud = label[2]
            tk.Button(self, text=label[0], width=30, height=2, command=eval(label[1])).grid(row=0, column=column,
                                                                                            padx=5, pady=10)
