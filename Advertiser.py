from BaseAdvertising import BaseAdvertising


class Advertiser(BaseAdvertising):
    """docstring"""

    __last_id = 0
    __totalClicks = 0

    def __init__(self, name, clicks=0, views=0):
        super().__init__(clicks, views)
        self.name = name
        Advertiser.__last_id += 1
        self.__id = Advertiser.__last_id

    def __str__(self):
        return f'ID: {self.__id}\tNAME: {self.name}\tCLICKS: {self.clicks}\tVIEWS: {self.views}'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        self.__name = n

    def incClicks(self):
        super().incClicks()
        Advertiser.__totalClicks += 1

    @staticmethod
    def help():
        return 'This is the responsibility of companies.'

    @staticmethod
    def getTotalClicks():
        return Advertiser.__totalClicks



