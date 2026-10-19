

# Generated at 2022-06-14 16:24:04.138677
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie._VALID_URL == HeiseIE._VALID_URL

# Generated at 2022-06-14 16:24:08.506318
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:24:09.446805
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    """
    Simple test case to check if the constructor still works
    """
    HeiseIE()

# Generated at 2022-06-14 16:24:21.133004
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    inst = HeiseIE()
    assert inst.suitable('https://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert inst.suitable('http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html')
    assert inst.suitable('http://www.heise.de/newsticker/meldung/c-t-uplink-Owncloud-Tastaturen-Peilsender-Smartphone-2404251.html?wt_mc=rss.ho.beitrag.atom')

# Generated at 2022-06-14 16:24:25.667064
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Test HeiseIE initialization
    ie = HeiseIE()
    assert ie.ie_key() == 'Heise'
    assert ie.ie_name() == 'Heise'
    assert ie.SUFFIX == '.html'

# Generated at 2022-06-14 16:24:35.869640
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Constructor without arguments
    instance = HeiseIE()
    # For coverage we call the method
    instance.suitable('http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html')
    # Constructor with one argument
    instance = HeiseIE('http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html')
    # For coverage we call the method

# Generated at 2022-06-14 16:24:42.042931
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Test for failed initialization
    ret_obj = HeiseIE(
        HeiseIE._download_webpage,
        r'https://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html')
    assert ret_obj._downloader.params['skip_download'] == True

# Generated at 2022-06-14 16:24:44.363123
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    from .test_videos_private import TestVideosPrivate as TestVideosBase
    class TestHeiseIE(TestVideosBase):
        IE = HeiseIE
    return TestHeiseIE

# Generated at 2022-06-14 16:24:45.347697
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE(None)
    assert ie

# Generated at 2022-06-14 16:24:46.629798
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    """Simple unit test for HeiseIE"""
    heise_ie = HeiseIE()

# Generated at 2022-06-14 16:25:07.424999
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    url = "http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html"
    h = HeiseIE(url)
    assert h is not None
    assert h.get_URL() == url
    assert h.get_VIDEO_ID() == "http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html"
    assert h.get_VIDEO_TITLE(force_download=True) == "Podcast: c't uplink 3.3 – Owncloud / Tastaturen / Peilsender Smartphone"

# Generated at 2022-06-14 16:25:08.457398
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE is not None

# Generated at 2022-06-14 16:25:10.606652
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise_ie = HeiseIE()
    assert heise_ie.ext == "mp4"

# Generated at 2022-06-14 16:25:11.921891
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Just to make sure it does not crash
    HeiseIE()

# Generated at 2022-06-14 16:25:12.686292
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()

# Generated at 2022-06-14 16:25:25.143274
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    from mock import Mock, patch
    from testtools import TestCase
    from testtools.matchers import Equals

    def assert_equals(name, expected, actual):
        mismatch = Equals(expected).match(actual)
        if mismatch:
            raise AssertionError(mismatch.describe_difference())

    class MockClass(Mock):
        pass

    class MockInfoExtractor(MockClass):
        def __init__(self, *args, **kwargs):
            super(MockInfoExtractor, self).__init__()
            self.ie_key = MockClass()
            self.ie_key.return_value = "MockInfoExtractor"
            self.playlist_result = MockClass()
            self.playlist_result.id = "playlist_id"
            self.playlist_result

# Generated at 2022-06-14 16:25:29.043004
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heiseIE = HeiseIE('https://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html')

# Generated at 2022-06-14 16:25:36.228242
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
	url = "http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html"
	x = HeiseIE()
	x.geo_verification_headers = None
	test = x._real_extract(url)
	assert test["id"] == "1_kkrq94sm"
	assert test["title"] == "Podcast: c't uplink 3.3 – Owncloud / Tastaturen / Peilsender Smartphone"
	return

# Generated at 2022-06-14 16:25:38.969081
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE != None
    return True

if __name__ == "__main__":
    test_HeiseIE()

# Generated at 2022-06-14 16:25:42.195126
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise = HeiseIE()
    url = heise._VALID_URL
    assert heise._match_id(url), 'Test failed'

# Generated at 2022-06-14 16:26:01.079548
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    url = 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
    video_id = '1_kkrq94sm'
    title = "Podcast: c't uplink 3.3 – Owncloud / Tastaturen / Peilsender Smartphone"
    test_obj = HeiseIE()
    assert test_obj._VALID_URL == HeiseIE._VALID_URL
    assert test_obj._TESTS == HeiseIE._TESTS
    assert test_obj._download_webpage(url, video_id) is not None
    assert test_obj._real_extract(url)['title'] == title

# Generated at 2022-06-14 16:26:02.640023
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE is not None

if __name__ == '__main__':
    test_HeiseIE()

# Generated at 2022-06-14 16:26:04.859226
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # pylint: disable=too-many-function-args
    assert isinstance(HeiseIE(), InfoExtractor)

# Generated at 2022-06-14 16:26:10.673591
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie= HeiseIE('https://www.heise.de/ct/artikel/c-t-uplink-20-8-Staubsaugerroboter-Xiaomi-Vacuum-2-AR-Brille-Meta-2-und-Android-rooten-3959893.html')
    assert ie.IE_NAME == 'heise'

# Generated at 2022-06-14 16:26:12.306552
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE.__name__ == 'HeiseIE'

# Generated at 2022-06-14 16:26:20.576136
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise = HeiseIE()
    url = 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
    assert heise.suitable(url)
    url = 'http://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html'
    assert heise.suitable(url)
    url = 'http://www.heise.de/ct/ausgabe/2016-12-Spiele-3214137.html'
    assert not heise.suitable(url)

# Generated at 2022-06-14 16:26:24.204407
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.ie_key() == 'heise'
    assert ie.ie_key() == 'Heise'
    assert ie.ie_key() == 'Heise.de'

# Generated at 2022-06-14 16:26:25.493885
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE('id')
    assert ie.info_extractors == {
        'kaltura': KalturaIE,
        'youtube': YoutubeIE,
    }

# Generated at 2022-06-14 16:26:27.577343
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.[^/]+'



# Generated at 2022-06-14 16:26:33.951587
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    h = HeiseIE()
    url = 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
    info_dict = {
        'id': '1_kkrq94sm',
        'ext': 'mp4',
        'title': "Podcast: c't uplink 3.3 – Owncloud / Tastaturen / Peilsender Smartphone",
        'timestamp': 1512734959,
        'upload_date': '20171208',
        'description': 'md5:c934cbfb326c669c2bcabcbe3d3fcd20',
    }

# Generated at 2022-06-14 16:26:59.207460
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE('https://www.heise.de/ct/artikel/c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2403911.html')
    assert ie._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:27:11.896331
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    class_ = globals()['HeiseIE']
    instance = class_('http://www.heise.de/')
    assert instance._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:27:22.047437
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    h = HeiseIE()
    url = 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
    assert isinstance(h, InfoExtractor)
    assert h.suitable(url)
    assert h._VALID_URL == 'https?://(?:www\\.)?heise\\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\\.html'
    assert h._TESTS[0]['url'] == url
    assert h._TESTS[0]['info_dict']['id'] == '1_kkrq94sm'

# Generated at 2022-06-14 16:27:22.853127
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()

# Generated at 2022-06-14 16:27:24.444999
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
  ie = HeiseIE()

# Generated at 2022-06-14 16:27:25.663630
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # As of 25.10.17, HeiseIE is functional
    pass

# Generated at 2022-06-14 16:27:31.255167
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heiseIE = HeiseIE(InfoExtractor())
    assert heiseIE._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:27:33.423990
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    """ Unit test for constructor of class HeiseIE """
    assert HeiseIE().ie != None

# Generated at 2022-06-14 16:27:43.536097
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heiseie = HeiseIE('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert heiseie._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:27:44.688310
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise = HeiseIE()
    test_instance = heise.test()

# Generated at 2022-06-14 16:28:34.063709
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    webpage = 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
    instance = HeiseIE()
    assert instance._VALID_URL == 'https?://(?:www\\.)?heise\\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\\.html'
    assert instance._match_id('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')

# Generated at 2022-06-14 16:28:35.194683
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Test constructor of class HeiseIE
    heise = HeiseIE()

# Generated at 2022-06-14 16:28:36.283407
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    class_ = globals()['HeiseIE']
    instance = class_(None)
    print(instance)

# Generated at 2022-06-14 16:28:41.668650
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    try:
        import youtube_dl
        youtube_dl.core.YoutubeDL({}).add_default_info_extractors()
    except Exception:
        # Skip test if youtube_dl can't be imported
        return
    assert HeiseIE.suitable('https://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert HeiseIE.suitable('http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html')

# Generated at 2022-06-14 16:28:51.253400
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Test initialization of HeiseIE instance
    heise = HeiseIE()
    assert isinstance(heise, InfoExtractor)
    # Test parameter _VALID_URL
    assert re.search(
        HeiseIE._VALID_URL, 'http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html')
    # Test parameter _TESTS
    urls = []
    for t in HeiseIE._TESTS:
        urls.append(t['url'])
    for url in urls:
        assert re.match(
            HeiseIE._VALID_URL, url)

# Generated at 2022-06-14 16:28:53.747251
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.IE_NAME == 'heise'
    assert ie.IE_DESC == 'heise Video'
    assert ie._VALID_URL is HeiseIE._VALID_URL

# Generated at 2022-06-14 16:29:01.856312
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    #For unit testing
    from .test_robot import MockRobotFileParser
    class MockOpener(object):
        def __init__(self, robot_file_parser):
            self.robot_file_parser = robot_file_parser
        def open(self, url, data=None):
            return url
        def addheaders(self, headers):
            return headers
    class MockHttpHandler(object):
        def default_open(self, req):
            return MockOpener(MockRobotFileParser())
    def test_data_downloader(self, url, data=None):
        return url

# Generated at 2022-06-14 16:29:04.718357
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    my_heiseie = HeiseIE()
    assert my_heiseie.ie_key() == 'Heise'


# Unit test of class HeiseIE

# Generated at 2022-06-14 16:29:14.550183
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.IE_NAME == 'heise'
    assert ie.IE_DESC == 'heise online'
    assert ie.VALID_URL == 'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:29:21.426268
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:30:55.453260
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    h = HeiseIE()
    assert h.extract("https://www.heise.de/ct/artikel/c-t-uplink-20-8-Staubsaugerroboter-Xiaomi-Vacuum-2-AR-Brille-Meta-2-und-Android-rooten-3959893.html")

# Generated at 2022-06-14 16:31:03.554084
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    instance = HeiseIE('/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert instance._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'
    assert instance.ie_key() == 'Heise'
    assert instance.ie_name() == 'heise.de'


# Generated at 2022-06-14 16:31:04.719126
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert(HeiseIE)


# Generated at 2022-06-14 16:31:09.421866
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert ie == "Podcast: c't uplink 3.3 – Owncloud / Tastaturen / Peilsender Smartphone"
test_HeiseIE()

# Generated at 2022-06-14 16:31:20.376544
# Unit test for constructor of class HeiseIE

# Generated at 2022-06-14 16:31:22.580751
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert issubclass(HeiseIE, InfoExtractor)
# Unit test to test if a valid URL is recognized by
# get_video_info() of class HeiseIE

# Generated at 2022-06-14 16:31:23.645645
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE(InfoExtractor())._VALID_URL == HeiseIE._VALID_URL

# Generated at 2022-06-14 16:31:25.440617
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert isinstance(HeiseIE(), InfoExtractor)
# Test for _real_extract method of class HeiseIE with kaltura embed

# Generated at 2022-06-14 16:31:28.092243
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise_ie = HeiseIE()
    assert heise_ie.ie_key() == 'heise'
    assert heise_ie.IE_NAME == 'heise'
    assert heise_ie.IE_DESC == 'heise online'

# Generated at 2022-06-14 16:31:30.466510
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Just check that the class can be created
    HeiseIE()