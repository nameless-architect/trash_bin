from pymongo import MongoClient
import datetime


class MongoConnectionClient:

    def __init__(self):
        self._clinet = MongoClient(
            "mongodb+srv://sergey:GJ4aEoL5Bww3Aq2N@cluster0.lraqe.mongodb.net/")

    @property
    def client(self):
        return self._clinet
