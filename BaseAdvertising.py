class BaseAdvertising:
    """Docstring"""

    __last_id = 0

    def __init__(self, clicks=0, views=0):
        BaseAdvertising.__last_id += 1
        self.__clicks = clicks
        self.__views = views
        self.__id = BaseAdvertising.__last_id

    def __str__(self):
        return f'ID: {self.__id}\tCLICKS: {self.__clicks}\tVIEWS: {self.__views}'

    def incClicks(self):
        self.__clicks += 1

    def incViews(self):
        self.__views += 1

    def describeMe(self):
        print(self)
