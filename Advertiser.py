from BaseAdvertising import BaseAdvertising


class Advertiser(BaseAdvertising):
    """docstring"""

    _last_id = 0
    _totalClicks = 0

    def __init__(self, name, clicks=0, views=0):
        super().__init__(clicks, views)
        self.name = name
        Advertiser._last_id += 1
        self._id = Advertiser._last_id

    def __str__(self):
        return f'ID: {self._id}\tNAME: {self.name}\tCLICKS: {self.clicks}\tVIEWS: {self.views}'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, n):
        self._name = n

    def incClicks(self):
        super().incClicks()
        Advertiser._totalClicks += 1

    @staticmethod
    def help():
        return 'This is the responsibility of companies.'

    @staticmethod
    def getTotalClicks():
        return Advertiser._totalClicks



