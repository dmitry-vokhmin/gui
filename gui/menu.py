from tkinter import Menu


class MainMenu:
    _menu_mapper = {"Inventory Collection": "inventory_collection",
                    "Calendar": "calendar",
                    "Price tag": "price_tag",
                    "Mover Price": "mover_price",
                    "Truck": "truck",
                    "Truck type": "truck_type",
                    }

    def __init__(self, window):
        self.window = window
        self.init_ui()

    def init_ui(self):
        main_menu = Menu(self.window)
        self.window.config(menu=main_menu)

        file_menu = Menu(main_menu, tearoff=0)

        submenu = Menu(file_menu)
        for key, value in self._menu_mapper.items():
            submenu.add_command(label=key, command=self.call_data_base_frame(value))
        file_menu.add_cascade(label="Data Base", menu=submenu)
        file_menu.add_command(label="User Flow", command=self.call_user_flow)

        main_menu.add_cascade(label="Files", menu=file_menu)

    def call_data_base_frame(self, menu):
        def call_back():
            self.window.data_base_frame(menu)
        return call_back

    def call_user_flow(self):
        self.window.user_flow_session()
