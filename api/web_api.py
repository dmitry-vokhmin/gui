import requests
from urllib.parse import urljoin


class WebApi:
    _paths = {"inventory": "/inventory/",
              "room_inventory": "/inventory/all/",
              "user": "/user/",
              "room_collection": "/room_collection/",
              "inventory_collection": "/inventory_collection/",
              "address": "/address/",
              "calendar": "/calendar/",
              "floor_collection": "/floor_collection/",
              "floor_collection_from": "/floor_collection/",
              "floor_collection_to": "/floor_collection/",
              "move_size": "/move_size/",
              "order": "/order/",
              "price_tag": "/price_tag/",
              "service": "/service/",
              "street": "/street/",
              "truck": "/truck/",
              "truck_type": "/truck_type/",
              "zip_code": "/zip_code/",
              "zip_code_from": "/zip_code/",
              "zip_code_to": "/zip_code/",
              "calculate": "/calculate/"}

    def __init__(self, api_url):
        self._api_url = api_url

    def get_data(self, end_point, api_id=0, query_param=""):
        if api_id or query_param:
            url = urljoin(self._api_url, self._paths[end_point] + str(api_id) + str(query_param))
        else:
            url = urljoin(self._api_url, self._paths[end_point])
        resp = requests.get(url)
        return resp.status_code, resp.json()

    def post_data(self, end_point, data: dict, api_id=None):
        if api_id:
            url = urljoin(self._api_url, self._paths[end_point] + str(api_id))
        else:
            url = urljoin(self._api_url, self._paths[end_point])
        post = requests.post(url, json=data)
        return post.status_code, post.json()

    def put_data(self, end_point, data: dict, api_id=None):
        if api_id:
            url = urljoin(self._api_url, self._paths[end_point] + str(api_id))
        else:
            url = urljoin(self._api_url, self._paths[end_point])
        put = requests.put(url, json=data)
        return put.status_code, put.json()
