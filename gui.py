from tkinter import *
import requests


def get_inventory():
    response = requests.get("http://127.0.0.1:8080/inventory/")
    m = response.text.split(",")
    m.reverse()
    for itm in m:
        text.insert(1.0, f"{itm}\n")


def open_inventory_window():
    inv_window = Toplevel()
    inv_window.geometry('200x400+200+100')

    def post_inventory():
        requests.post("http://127.0.0.1:8080/inventory/", json={"name": name.get(),
                                                                "height": int(height.get()),
                                                                "weight": int(weight.get()),
                                                                "width": int(width.get()),
                                                                "deep": int(deep.get()),
                                                                "dimension": int(dimension.get()),
                                                                "unit": int(unit.get())})
    inv_win_top = Frame(inv_window)
    inv_win_top.pack()
    Label(inv_win_top, text="Name").pack(side=TOP)
    name = Entry(inv_win_top, width=30)
    name.pack(side=TOP)
    Label(inv_win_top, text="Height").pack(side=TOP)
    height = Entry(inv_win_top, width=30)
    height.pack(side=TOP)
    Label(inv_win_top, text="Weight").pack(side=TOP)
    weight = Entry(inv_win_top, width=30)
    weight.pack(side=TOP)
    Label(inv_win_top, text="Width").pack(side=TOP)
    width = Entry(inv_win_top, width=30)
    width.pack(side=TOP)
    Label(inv_win_top, text="Deep").pack(side=TOP)
    deep = Entry(inv_win_top, width=30)
    deep.pack(side=TOP)
    Label(inv_win_top, text="Dimension").pack(side=TOP)
    dimension = Entry(inv_win_top, width=30)
    dimension.pack(side=TOP)
    Label(inv_win_top, text="Unit").pack(side=TOP)
    unit = Entry(inv_win_top, width=30)
    unit.pack(side=TOP)
    Button(inv_win_top, text="Add", width=15, height=3, command=post_inventory).pack(side=TOP)







root = Tk()
root.title("Show inventory")

root_top = Frame(root)
root_top.pack()
text = Text(root_top, width=30, height=15)
text.pack(side=LEFT)

scroll = Scrollbar(root_top, command=text.yview)
scroll.pack(side=LEFT, fill=Y)

text.config(yscrollcommand=scroll.set)

root_bot = Frame(root)
root_bot.pack()
show_inv = Button(root_bot, text="Show Inventory", width=15, height=3, command=get_inventory)
show_inv.pack(side=LEFT)
Button(root_bot, text="Add Inventory", width=15, height=3, command=open_inventory_window).pack(side=LEFT)

root.update_idletasks()
s = root.geometry()
s = s.split('+')
s = s[0].split('x')
width_root = int(s[0])
height_root = int(s[1])

w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w // 2
h = h // 2
w = w - width_root // 2
h = h - height_root // 2
root.geometry('+{}+{}'.format(w, h))

root.mainloop()
