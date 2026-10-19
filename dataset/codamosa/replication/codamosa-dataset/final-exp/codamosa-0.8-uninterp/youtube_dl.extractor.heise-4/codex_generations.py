

# Generated at 2022-06-14 16:24:11.675984
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert isinstance(ie, InfoExtractor)
    assert ie.ie_key() == 'Heise'
    assert ie.server == 'www.heise.de'
    assert ie.channel_id == 'heise'
    assert ie.title == 'Heise'
    assert hasattr(ie, 'description')
    assert hasattr(ie, 'search_title')
    assert hasattr(ie, 'search_thumbnail')
    assert hasattr(ie, 'search_sort_query')

# Generated at 2022-06-14 16:24:12.366846
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()

# Generated at 2022-06-14 16:24:13.561421
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert 'HeiseIE' in globals()

# Generated at 2022-06-14 16:24:17.023864
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.site_name == 'Heise'
    assert ie.ie_key() == 'Heise'
    assert ie.ie_name == 'Heise'

# Generated at 2022-06-14 16:24:28.711434
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    IE = HeiseIE('www.heise.de')
    title = "c't uplink 3.3 – Owncloud / Tastaturen / Peilsender Smartphone"
    description = 'md5:c934cbfb326c669c2bcabcbe3d3fcd20'
    url = ('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-T'
           'astaturen-Peilsender-Smartphone-2404147.html')

# Generated at 2022-06-14 16:24:36.277401
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    from . import YoutubeIE
    from .kaltura import KalturaIE
    from .heise import HeiseIE
    assert HeiseIE.ie_key() == 'heise'
    assert HeiseIE.ie_key() in HeiseIE._WORKING_IE_CODECS
    assert HeiseIE.SUFFIX in HeiseIE._WORKING_IE_CODECS[HeiseIE.ie_key()]
    assert HeiseIE.SUFFIX == 'heise'
    assert HeiseIE.SUFFIX in HeiseIE._WORKING_IE_CODECS[YoutubeIE.ie_key()]
    assert HeiseIE.SUFFIX in HeiseIE._WORKING_IE_CODECS[KalturaIE.ie_key()]

# Generated at 2022-06-14 16:24:37.204764
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()

# Generated at 2022-06-14 16:24:39.092683
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Test heiseIE constructor
    heiseIE = HeiseIE()

# Generated at 2022-06-14 16:24:46.323272
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE("http://www.heise.de/ct/artikel/c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2403911.html", {}, None)
    HeiseIE("https://www.heise.de/ct/artikel/c-t-uplink-20-8-Staubsaugerroboter-Xiaomi-Vacuum-2-AR-Brille-Meta-2-und-Android-rooten-3959893.html", {}, None)

# Generated at 2022-06-14 16:24:47.591465
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    x = HeiseIE({})
    assert x


# Generated at 2022-06-14 16:25:06.782429
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.description == "c't uplink 20.8: Staubsaugerroboter Xiaomi Vacuum 2, AR-Brille Meta 2 und Android rooten"
    assert ie.ext == 'mp4'
    assert ie.id == '1_59mk80sf'
    assert ie.title == "c't uplink 20.8: Staubsaugerroboter Xiaomi Vacuum 2, AR-Brille Meta 2 und Android rooten"
    assert ie.timestamp == datetime.datetime(2018, 2, 2, 17, 40, 37)
    assert len(ie.formats) == 5


# Generated at 2022-06-14 16:25:13.326330
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    test_urls = [
                'https://www.heise.de/ct/artikel/c-t-uplink-20-8-Staubsaugerroboter-Xiaomi-Vacuum-2-AR-Brille-Meta-2-und-Android-rooten-3959893.html'
                ]
    for url in test_urls:
        heise_IE = HeiseIE(url)


if __name__ == "__main__":
    test_HeiseIE()

# Generated at 2022-06-14 16:25:15.444291
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heiseie = HeiseIE({})
    assert heiseie is not None

test_HeiseIE()

# Generated at 2022-06-14 16:25:28.143212
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:25:30.148735
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heiseie = HeiseIE()
    assert heiseie.ie_key() == 'Heise'

# Generated at 2022-06-14 16:25:42.571073
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    i = HeiseIE()
    assert i.ie_key() == 'heise'
    assert i.ie_name() == 'heise'
    assert i.suitable('') == False
    assert i.suitable('http://www.heise.de/newsticker/meldung/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html') == True

# Generated at 2022-06-14 16:25:46.378630
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    """Instantiation test.

    Just test basic instantiation and deletion of new object.
    """
    heise = HeiseIE()
    heise = heise.delete()


# Unit tests for HeiseIE._extract_url()

# Generated at 2022-06-14 16:25:48.904536
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    inst = HeiseIE()
    assert inst._VALID_URL == HeiseIE._VALID_URL
    assert inst._TESTS == HeiseIE._TESTS

# Generated at 2022-06-14 16:25:53.576299
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    example_url = 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
    assert ie.suitable(example_url)
    assert ie.IE_NAME == ie.get_info(example_url)['id']
    assert ie.IE_NAME == ie.ie_key()
    assert ie.IE_DESC == ie._meta_info(example_url)['title']

# Generated at 2022-06-14 16:26:02.716069
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    info_extractor = HeiseIE()
    assert info_extractor._VALID_URL == "https?://(?:www\\.)?heise\\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\\.html"

# Generated at 2022-06-14 16:26:22.180639
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE(None)
    assert ie

# Generated at 2022-06-14 16:26:23.215635
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()

# Generated at 2022-06-14 16:26:24.441477
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # HeiseIE is abstract, so we instantiate a child (HeiseIE)
    obj = YoutubeIE()
    assert obj.ie_key() == 'HeiseIE'

# Generated at 2022-06-14 16:26:25.774051
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.ie_key() == "Heise"

# Generated at 2022-06-14 16:26:26.353707
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()

# Generated at 2022-06-14 16:26:30.304580
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Verify correctness of HeiseIE constructor
    heiseIE = HeiseIE()

    # Check value of member variable _VALID_URL
    assert heiseIE._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:26:39.313586
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    obj = HeiseIE()
    assert obj.ie_key() == 'heise'
    assert obj.SUCCESS == 0
    assert obj._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:26:39.928891
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()

# Generated at 2022-06-14 16:26:40.925503
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise = HeiseIE()

# Generated at 2022-06-14 16:26:52.671393
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    instance = HeiseIE('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert instance.url == 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
    assert instance.video_id == '1_kkrq94sm'
    assert instance.title == "Podcast: c't uplink 3.3 – Owncloud / Tastaturen / Peilsender Smartphone"
    assert instance.id == '1_kkrq94sm'
    assert instance.timestamp == 1512734959

# Generated at 2022-06-14 16:27:11.522608
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise_ie = HeiseIE()

# Generated at 2022-06-14 16:27:13.131617
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie1 = HeiseIE()
    assert(not ie1._downloader)

# Generated at 2022-06-14 16:27:24.530085
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise_ie = HeiseIE()
    assert heise_ie._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:27:32.172306
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    """
    Test class HeiseIE
    """
    # Test with and without source_url
    url = "http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html"
    ie = HeiseIE(url)
    assert ie.url == url
    assert ie.source_url == url
    assert ie.extract_url() == url
    assert ie.extract_video_id() == "3814130"
    ie = HeiseIE(url, source_url="http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html")
   

# Generated at 2022-06-14 16:27:35.701051
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    """
    This function tests the constructor of the class HeiseIE
    """
    heiseie = HeiseIE()
    assert heiseie is not None


# Generated at 2022-06-14 16:27:36.648850
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    unit = HeiseIE()
    assert unit

# Generated at 2022-06-14 16:27:43.240659
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise_ie = HeiseIE()
    assert heise_ie.IE_NAME == "heise"
    assert heise_ie.IE_DESC == "heise online video"
    assert heise_ie.URL_PATTERN == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)*(?:artikel/)?(?P<id>[0-9]+(-[0-9]+(-[0-9]+)?(-[0-9]+)?)?).html'

# Generated at 2022-06-14 16:27:44.410663
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise = HeiseIE()
    assert heise is not None

# Generated at 2022-06-14 16:27:45.250248
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()

# Generated at 2022-06-14 16:27:48.978548
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE(None)
    assert ie.ie_key() == 'heise'
    assert ie.ie_name() == 'Heise'
    assert ie.SUITABLE_ALTERNATIVE_URL == 'self'

# Generated at 2022-06-14 16:28:30.513849
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise_test = HeiseIE()

test_HeiseIE()

# Generated at 2022-06-14 16:28:36.489681
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:28:37.347666
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()


# Generated at 2022-06-14 16:28:42.793370
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # test the constructor of HeiseIE
    webpage = 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
    info = HeiseIE()._real_extract(webpage)
    assert isinstance(info, dict)

# Generated at 2022-06-14 16:28:46.608497
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise_ie = HeiseIE(NO_DEFAULT)
    
    assert heise_ie is not None
    assert heise_ie.ie_key() == 'heise'
    assert heise_ie.ie_name() == 'heise'

# Generated at 2022-06-14 16:28:47.924580
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE()._VALID_URL == HeiseIE._VALID_URL

# Generated at 2022-06-14 16:28:51.038704
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise = HeiseIE()
    assert (heise.name == 'heise' and heise.ie_key() == 'heise' and heise.SITE_NAME == 'heise')

# Generated at 2022-06-14 16:28:59.327835
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise = HeiseIE()
    heise.extract("https://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html")
    heise.extract("http://www.heise.de/newsticker/meldung/c-t-uplink-Owncloud-Tastaturen-Peilsender-Smartphone-2404251.html?wt_mc=rss.ho.beitrag.atom")

# Generated at 2022-06-14 16:29:02.137017
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    infoExtractor = HeiseIE()
    assert infoExtractor._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'



# Generated at 2022-06-14 16:29:08.171292
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    """Unit test for constructor of class HeiseIE"""
    heise_ie = HeiseIE("http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html")
    assert(isinstance(heise_ie, HeiseIE))
    assert(isinstance(heise_ie, KalturaIE))

# Generated at 2022-06-14 16:30:50.468670
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.name == 'heise'
    assert ie.description == "heise online Video Center"
    assert ie.extractor_key == 'heise'
    assert ie.suitable(expect_suitable = ['https://www.heise.de/ct/ausgabe/2016-12-Spiele-3214137.html'])
    assert ie.suitable(expect_suitable = ['https://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html'])

# Generated at 2022-06-14 16:30:52.190083
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie._download_webpage.__name__ == '_download_webpage'

# Generated at 2022-06-14 16:30:59.498648
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE('http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html')
    assert ie.url == 'http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html'
    assert ie.video_id == '3814130'

# Generated at 2022-06-14 16:31:09.754451
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise_ie = HeiseIE()
    assert heise_ie.ie_key() == 'heise'
    assert heise_ie.ie_name() == 'Heise'

# Generated at 2022-06-14 16:31:19.194843
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # This iid is random
    iid = "2404147"
    # This is a dict that tests all of the methods in class HeiseIE
    # it is a test of the entire class
    test_urls = [
        ("http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html", iid)
    ]
    for url, iid2 in test_urls:
        info = HeiseIE()._real_extract(url)
        assert info['id'] == iid2

# Generated at 2022-06-14 16:31:23.591954
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # test if HeiseIE returns several videos
    result = HeiseIE()._real_extract("http://www.heise.de/ct/ausgabe/2016-12-Spiele-3214137.html")
    assert len(result["entries"]) != 0
    # test if HeiseIE returns a single video
    result = HeiseIE()._real_extract("http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html")
    assert "entries" not in result

# Generated at 2022-06-14 16:31:33.253151
# Unit test for constructor of class HeiseIE
def test_HeiseIE():    
    heise = HeiseIE()
    assert(heise.suitable("http://www.heise.de/ct/artikel/c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2403911.html"))
    assert(not heise.suitable("https://www.heise.de/ct/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html"))
    assert(heise.suitable("https://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html"))

# Generated at 2022-06-14 16:31:38.655675
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE().download(HeiseIE()._TESTS[0]["url"])
    HeiseIE().download(HeiseIE()._TESTS[1]["url"])
    HeiseIE().download(HeiseIE()._TESTS[2]["url"])
    HeiseIE().download(HeiseIE()._TESTS[3]["url"])

test_HeiseIE()

# eof

# Generated at 2022-06-14 16:31:43.195687
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE("http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html")
    assert ie.title() == "Podcast: c't uplink 3.3 – Owncloud / Tastaturen / Peilsender Smartphone"

# Generated at 2022-06-14 16:31:44.926125
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    h = HeiseIE()
    assert h.ie_key() == 'Heise'
    assert h.ie_name() == 'Heise'