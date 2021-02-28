from api.web_api import WebApi
from gui.window import Window


def main(window):
    pass


if __name__ == '__main__':
    web_api = WebApi("http://127.0.0.1:8080/")
    root = Window(web_api)

    root.mainloop()
