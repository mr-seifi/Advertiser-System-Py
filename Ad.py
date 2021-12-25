from BaseAdvertising import BaseAdvertising


class Ad(BaseAdvertising):
    """docstring"""

    __last_id = 0

    def __init__(self, title, advertiser, imgUrl='', link='', clicks=0, views=0):
        super().__init__(clicks, views)
        self.title = title
        self.advertiser = advertiser
        self.imgUrl = imgUrl
        self.link = link
        Ad.__last_id += 1
        self.__id = Ad.__last_id

    def __str__(self):
        return f'ID: {self.__id}\tTITLE: {self.title}\tADVERTISER_NAME: {self.advertiser.name}\tIMG_URL: {self.imgUrl}\tLINK: {self.link}\tCLICKS: {self.clicks}\tVIEWS: {self.views}'

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def imgUrl(self):
        return self.__imgUrl

    @imgUrl.setter
    def imgUrl(self, imgUrl):
        self.__imgUrl = imgUrl

    @property
    def link(self):
        return self.__link

    @link.setter
    def link(self, link):
        self.__link = link

    @property
    def advertiser(self):
        return self.__advertiser

    @advertiser.setter
    def advertiser(self, advertiser):
        self.__advertiser = advertiser

    def incClicks(self):
        super().incClicks()
        self.advertiser.incClicks()

    def incViews(self):
        super().incViews()
        self.advertiser.incViews()

    def describeMe(self):
        print(self)
