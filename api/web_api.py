import requests
from urllib.parse import urljoin


class WebApi:
    _paths = {"inventory": "/inventory/",
              "user": "/user/",
              "room_collection": "/room_collection/",
              "address": "/address/",
              "calendar": "/calendar/",
              "floor_collection": "/floor_collection/",
              "move_size": "/move_size/",
              "order": "/order/",
              "price_tag": "/price_tag/",
              "services": "/services/",
              "street": "/street/",
              "truck": "/truck/",
              "truck_type": "/truck_type/",
              "zip_code": "/zip_code/"}

    def __init__(self, api_url):
        self._api_url = api_url

    def get_data(self, end_point, api_id=None):
        if api_id:
            url = urljoin(self._api_url, self._paths[end_point] + api_id)
        else:
            url = urljoin(self._api_url, self._paths[end_point])
        resp = requests.get(url)
        return resp.status_code, resp.json()

    def post_data(self, end_point, data: dict):
        url = urljoin(self._api_url, self._paths[end_point])
        post = requests.post(url, json=data)
        return post.status_code, post.json()
