class BaseAdvertising:
    """Docstring"""

    __last_id = 0

    def __init__(self, clicks=0, views=0):
        assert(clicks >= 0 and views >= 0), 'Clicks or Views should be positive!'
        self.__clicks = clicks
        self.__views = views
        BaseAdvertising.__last_id += 1
        self.__id = BaseAdvertising.__last_id

    def __str__(self):
        return f'ID: {self.__id}\tCLICKS: {self.__clicks}\tVIEWS: {self.__views}'

    @property
    def clicks(self):
        return self.__clicks

    def incClicks(self):
        self.__clicks += 1

    @property
    def views(self):
        return self.__views

    def incViews(self):
        self.__views += 1

    def describeMe(self):
        print(self)
