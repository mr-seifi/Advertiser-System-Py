class BaseAdvertising:
    """Docstring"""

    def __init__(self, clicks=0, views=0):
        assert(clicks >= 0 and views >= 0), 'Clicks or Views should be positive!'
        self._clicks = clicks
        self._views = views

    def __str__(self):
        return f'CLICKS: {self._clicks}\tVIEWS: {self._views}'

    @property
    def clicks(self):
        return self._clicks

    def incClicks(self):
        self._clicks += 1

    @property
    def views(self):
        return self._views

    def incViews(self):
        self._views += 1

    def describeMe(self):
        print(self)
