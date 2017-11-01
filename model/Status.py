import json


class Status(object):
    def __init__(self, j="{}"):
        self.__dict__ = json.load(j)

    def __repr__(self):
        return str(self.__dict__)
