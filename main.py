from BaseAdvertising import BaseAdvertising
from Advertiser import Advertiser
from Ad import Ad

if __name__ == '__main__':
    baseAdvertising = BaseAdvertising()
    advertiser1, advertiser2 = Advertiser('name1'), Advertiser('name2')
    ad1, ad2 = Ad(title='title1', imgUrl='img-url1', link='link1', advertiser=advertiser1), \
               Ad(title='title2', imgUrl='img-url2', link='link2', advertiser=advertiser2)
    baseAdvertising.describeMe()
    ad2.describeMe()
    advertiser1.describeMe()
    ad1.incViews()
    ad1.incViews()
    ad1.incViews()
    ad1.incViews()
    ad2.incViews()
    ad1.incClicks()
    ad1.incClicks()
    ad2.incClicks()
    print("Advertiser2 Name:", advertiser2.name)
    advertiser2.name = "new name"
    print("Advertiser2 Name:", advertiser2.name)
    print("Ad1 Clicks:", ad1.clicks)
    print("Advertiser2 Clicks:", advertiser2.clicks)
    print("Advertiser Total Clicks:", Advertiser.getTotalClicks())
    print("Advertiser Help:", Advertiser.help())
