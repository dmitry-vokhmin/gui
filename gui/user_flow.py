import tkinter as tk
from collections import defaultdict
from .personal_info import PersonalInfo
from .move_info import MoveInfo
from calculator.calculator import Calculator
from .calculation_result import CalculationResult
from .address_info import AddressInfo


class UserFlow:
    order = defaultdict(list)
    calculations = {}

    def __init__(self, window):
        self.window = window
        self.per_info_frame = PersonalInfo(self.window)
        self.move_info_frame = MoveInfo(self.window)
        self.calculation_result_frame = CalculationResult(self.window, self)
        self.address_info_frame = AddressInfo(self.window, self)

    def personal_info(self):
        self.per_info_frame.grid(row=0, column=0, sticky=tk.N, padx=20)

    def move_info(self):
        self.per_info_frame.destroy()
        self.move_info_frame.grid(row=0, column=0, sticky=tk.N, padx=20)

    def calculate(self):
        self.move_info_frame.destroy()
        Calculator(self)
        self.calculation_result_frame.grid(row=0, column=0, sticky=tk.N, padx=20)
        self.calculation_result_frame.show_calc_result()

    def address_info(self):
        self.calculation_result_frame.destroy()
        self.address_info_frame.grid(row=0, column=0, sticky=tk.N, padx=20)
        self.address_info_frame.show_address_fields()