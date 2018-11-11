# coding: utf8
import requests


class BasePasteService(object):
    def __init__(self, token, url):
        self.token = token
        self.url = url

    def paste(self, **kwargs):
        pass

    def post(self, url, payload):
        return requests.post(self.url, data=payload)

