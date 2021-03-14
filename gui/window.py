import tkinter as tk
from PIL import Image, ImageTk
from .data_base_buttons import DataBaseButtons
from .menu import MainMenu
from .contents import Contents
from .forms import Forms
from .message_box import MessageBox
from .user_flow import UserFlow


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
        self.db_frame = DataBaseButtons(self)
        self.main_menu = MainMenu(self)
        self.content_frame = Contents(self)
        self.forms_frame = Forms(self)
        self.user_flow = UserFlow(self)
        self.steps = iter(self.user_flow)

    def user_flow_session(self):
        self.db_frame.destroy()
        self.content_frame.destroy()
        self.forms_frame.destroy()
        self.next_step(data=None)

    def next_step(self, data):
        step = next(self.steps)
        step(data)

    def data_base_frame(self, menu_point):
        self.db_frame.destroy()
        self.db_frame = DataBaseButtons(self, menu_point)
        self.db_frame.grid(row=0, column=0, sticky=tk.N, padx=20)

    def show_form(self, form_type):
        def call_back():
            self.content_frame.destroy()
            self.forms_frame.destroy()
            self.forms_frame = Forms(self, form_type)
            self.forms_frame.grid(row=1, column=0, sticky=tk.S)
            self.forms_frame.show_form()

        return call_back

    def show_data(self, api_f, api_end_point, api_id=None):

        def call_back():
            self.content_frame.destroy()
            self.forms_frame.destroy()
            self.content_frame = Contents(self)
            self.content_frame.grid(row=1, column=0, sticky=tk.S)
            if api_id:
                id = api_id.get()
                response_code, response_data = api_f(api_end_point, api_id=id)
            else:
                response_code, response_data = api_f(api_end_point)
            self.content_frame.data_structure(response_data)

        return call_back

    def get_data(self, api_end_point, api_id=0, query_param=""):
        response_code, response_data = self.web_api.get_data(api_end_point, api_id=api_id, query_param=query_param)
        if response_code > 399:
            MessageBox(response_code, response_data, api_end_point)
        else:
            return response_data

    def post_data(self, api_end_point, data):
        response_code, response_data = self.web_api.post_data(api_end_point, data)
        if response_code > 399:
            MessageBox(response_code, response_data, api_end_point)
        else:
            return response_data
