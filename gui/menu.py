from tkinter import Menu


class MainMenu:
    def __init__(self, window):
        self.window = window
        self.initui()

    def initui(self):
        mainmenu = Menu(self.window)
        self.window.config(menu=mainmenu)

        filemenu = Menu(mainmenu, tearoff=0)

        submenu = Menu(filemenu)
        submenu.add_command(label="Inventory", command=self.call_menu_frame("inventory"))
        submenu.add_command(label="User", command=self.call_menu_frame("user"))
        submenu.add_command(label="Service", command=self.call_menu_frame("services"))
        submenu.add_command(label="Address", command=self.call_menu_frame("address"))
        submenu.add_command(label="Calendar", command=self.call_menu_frame("calendar"))
        submenu.add_command(label="Floor Collections", command=self.call_menu_frame("floor_collection"))
        submenu.add_command(label="Move size", command=self.call_menu_frame("move_size"))
        submenu.add_command(label="Order", command=self.call_menu_frame("order"))
        submenu.add_command(label="Price tag", command=self.call_menu_frame("price_tag"))
        submenu.add_command(label="Room Collections", command=self.call_menu_frame("room_collection"))
        submenu.add_command(label="Street", command=self.call_menu_frame("street"))
        submenu.add_command(label="Truck", command=self.call_menu_frame("truck"))
        submenu.add_command(label="Truck type", command=self.call_menu_frame("truck_type"))
        submenu.add_command(label="Zipcode", command=self.call_menu_frame("zip_code"))
        filemenu.add_cascade(label="Data Base", menu=submenu)

        mainmenu.add_cascade(label="Files", menu=filemenu)

    def call_menu_frame(self, menu):
        def call_back():
            self.window.menu_frame(menu)
        return call_back
