from tkinter import messagebox


class MessageBox:
    def __init__(self, response_code, response_data, api_end_point):
        self.message_box(response_code, response_data, api_end_point)

    @staticmethod
    def message_box(response_code, response_data, api_end_point):
        if isinstance(response_data, dict):
            if response_code > 399:
                for value in response_data.values():
                    for data in value:
                        messagebox.showerror("Error", f"Field: '{data['loc'][1]}' message: '{data['msg']}'")
            else:
                messagebox.showinfo("Ok", f"{api_end_point} added")
        else:
            messagebox.showerror("Error", f"Field: '{api_end_point}' message: '{response_data}'")
