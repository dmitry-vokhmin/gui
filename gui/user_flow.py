import tkinter as tk
from .personal_info import PersonalInfo
from .move_info import MoveInfo
from .calculation_result import CalculationResult
from .address_info import AddressInfo
from .final_order import FinalOrder


class UserFlowIter:
    def __init__(self, steps):
        self.steps = steps
        self.idx = 0

    def __next__(self):
        try:
            return self.steps[self.idx]
        except IndexError:
            raise StopIteration
        finally:
            self.idx += 1


class UserFlow:
    order = {}
    zip_codes = {}

    def __init__(self, window):
        self.window = window
        self.per_info_frame = PersonalInfo(self.window)
        self.move_info_frame = MoveInfo(self.window)
        self.calculation_result_frame = CalculationResult(self.window)
        self.address_info_frame = AddressInfo(self.window)
        self.final_order_frame = FinalOrder(self.window)

    def personal_info(self, data=None):
        self.per_info_frame.grid(row=0, column=0, sticky=tk.N, padx=20)

    def move_info(self, personal_info):
        self.order.update(personal_info)
        self.per_info_frame.destroy()
        self.move_info_frame.grid(row=0, column=0, sticky=tk.N, padx=20)

    def calculate(self, move_info):
        for key, value in move_info.items():
            if key == "zip_code_from_id" or key == "zip_code_to_id":
                self.zip_codes[key] = value
            else:
                self.order[key] = value
        self.move_info_frame.destroy()
        self.calculation_result_frame.grid(row=0, column=0, sticky=tk.N, padx=20)
        self.calculation_result_frame.send_data(self.order)

    def address_info(self, calculate):
        self.order.update(calculate)
        self.calculation_result_frame.destroy()
        self.address_info_frame.grid(row=0, column=0, sticky=tk.N, padx=20)
        self.address_info_frame.get_zip_code_info(self.zip_codes)

    def final_order(self, address_info):
        self.order.update(address_info)
        self.address_info_frame.destroy()
        self.final_order_frame.grid(row=0, column=0, sticky=tk.N, padx=20)
        self.final_order_frame.post_order(self.order)

    def __iter__(self):
        return UserFlowIter([self.personal_info, self.move_info, self.calculate, self.address_info, self.final_order])





