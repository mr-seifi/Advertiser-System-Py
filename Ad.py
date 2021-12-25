from BaseAdvertising import BaseAdvertising


class Ad(BaseAdvertising):
    """docstring"""

    _last_id = 0

    def __init__(self, title, advertiser, imgUrl='', link='', clicks=0, views=0):
        super().__init__(clicks, views)
        self.title = title
        self.advertiser = advertiser
        self.imgUrl = imgUrl
        self.link = link
        Ad._last_id += 1
        self._id = Ad._last_id

    def __str__(self):
        return f'ID: {self._id}\tTITLE: {self.title}\tADVERTISER_NAME: {self.advertiser.name}\tIMG_URL: {self.imgUrl}\tLINK: {self.link}\tCLICKS: {self.clicks}\tVIEWS: {self.views}'

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def imgUrl(self):
        return self._imgUrl

    @imgUrl.setter
    def imgUrl(self, imgUrl):
        self._imgUrl = imgUrl

    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, link):
        self._link = link

    @property
    def advertiser(self):
        return self._advertiser

    @advertiser.setter
    def advertiser(self, advertiser):
        self._advertiser = advertiser

    def incClicks(self):
        super().incClicks()
        self.advertiser.incClicks()

    def incViews(self):
        super().incViews()
        self.advertiser.incViews()

    def describeMe(self):
        print(self)
