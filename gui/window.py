import tkinter as tk
from PIL import Image, ImageTk
from .buttons import Buttons
from .menu import MainMenu
from .contents import Contents
from .forms import Forms


class Window(tk.Tk):
    def __init__(self, web_api):
        super().__init__()
        self.title("GUI example interface")
        self.geometry("800x600")
        self.load = Image.open("gui/image.jpg")
        self.render = ImageTk.PhotoImage(self.load)
        self.img = tk.Label(self, image=self.render)
        self.img.image = self.render
        self.img.place(x=0, y=0)
        self.web_api = web_api
        self.mainmenu = MainMenu(self)
        self.content_frame = Contents(self)
        self.forms_frame = Forms(self)

    def menu_frame(self, menu_point):
        menu_frame = Buttons(self, menu_point)
        menu_frame.grid(row=0, column=0, sticky=tk.N, padx=20)

    def show_data(self, api_f, api_end_point, api_id=None):

        def call_back():
            self.content_frame.destroy()
            self.forms_frame.destroy()
            self.content_frame = Contents(self)
            self.content_frame.grid(row=1, column=0, sticky=tk.S)
            if api_id:
                id = api_id.get()
                data = api_f(api_end_point, id)
            else:
                data = api_f(api_end_point)
            self.content_frame.data_structure(data)

        return call_back

    def show_form(self, form_type):
        def call_back():
            self.content_frame.destroy()
            self.forms_frame.destroy()
            self.forms_frame = Forms(self, form_type)
            self.forms_frame.grid(row=1, column=0, sticky=tk.S)
            self.forms_frame.show_form()
        return call_back

    def post_data(self, api_end_point, data):
        self.web_api.post_data(api_end_point, data)
