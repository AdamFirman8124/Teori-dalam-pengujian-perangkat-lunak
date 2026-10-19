

# Generated at 2022-06-14 16:24:12.763618
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE("http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html", "http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html")

# Generated at 2022-06-14 16:24:13.926502
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie is not None

# Generated at 2022-06-14 16:24:18.245189
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise = HeiseIE('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert heise

# Generated at 2022-06-14 16:24:18.879323
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()

# Generated at 2022-06-14 16:24:20.343365
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise_ie = HeiseIE()
    assert heise_ie._VALID_URL

# Generated at 2022-06-14 16:24:21.795557
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE.__name__ == "HeiseIE"

# Generated at 2022-06-14 16:24:26.346948
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE.suitable('http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html')

# Generated at 2022-06-14 16:24:27.509354
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    h = HeiseIE()
    return h

# Generated at 2022-06-14 16:24:28.447684
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise = HeiseIE()

# Generated at 2022-06-14 16:24:29.444940
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE.__init__(HeiseIE)

# Generated at 2022-06-14 16:24:42.006294
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert(HeiseIE.suitable(testHeiseIE.url) == True)
    assert(HeiseIE.suitable(testHeiseIE2.url) == True)
    assert(HeiseIE.suitable(testHeiseIE3.url) == True)



# Generated at 2022-06-14 16:24:50.169855
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # test heiseie with an article with a video
    heiseIE = HeiseIE()
    res = heiseIE.extract('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert res['title'] == 'Podcast: c\'t uplink 3.3 – Owncloud / Tastaturen / Peilsender Smartphone'
    assert res['id'] == '1_kkrq94sm'
    assert res['formats'][0]['ext'] == 'mp4'

    # test heiseie with article with multiple videos
    heiseIE = HeiseIE()

# Generated at 2022-06-14 16:24:55.997112
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE('http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html')
    assert ie.title == 'NEU IM SEPTEMBER | Netflix'
    assert ie.description == 'md5:2131f3c7525e540d5fd841de938bd452'
    assert ie.id == '6kmWbXleKW4'

# Generated at 2022-06-14 16:25:06.938979
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE('http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html')
    assert(ie.url == 'http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html')
    assert(ie.video_id == 'http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html')

# Generated at 2022-06-14 16:25:10.727798
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise_ie = HeiseIE()
    # The following variables have been defined in the class TestHeiseIE
    assert heise_ie.base_url == "http://www.heise.de/"
    assert heise_ie.videoplayer_re == '<div[^>]+class="videoplayerjw"[^>]+data-file="([^"]+)"'
    assert heise_ie.query_url == "http://www.heise.de/videout/feed"
    assert heise_ie.query_keys == ["container", "sequenz"]

# Generated at 2022-06-14 16:25:12.006973
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    obj = HeiseIE()
    assert(obj != None)

# Generated at 2022-06-14 16:25:24.178711
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # first test Kaltura
    url = 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
    # container id is given -> no need to parse xml feed -> go directly to Kaltura..
    temp = HeiseIE()
    temp.extract(url)
        
    # second test Youtube
    url = 'http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html'
    temp = HeiseIE()
    temp.extract(url)
    
    # third test Jwplayer

# Generated at 2022-06-14 16:25:25.583844
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.ie_key() == 'heise'

# Generated at 2022-06-14 16:25:35.515235
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    # check if all class attributes are initialized
    assert ie._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:25:38.051451
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
  ie = HeiseIE()
  assert ie.ie_key() == 'Heise'

# Generated at 2022-06-14 16:25:56.003880
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE._VALID_URL == HeiseIE._TESTS[0]['url']

# Generated at 2022-06-14 16:26:01.887887
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    ie.download('https://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html')
    ie.download('http://www.heise.de/ct/artikel/c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2403911.html')

# Generated at 2022-06-14 16:26:02.831618
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    pass


# Generated at 2022-06-14 16:26:09.105860
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heiseIE = HeiseIE()
    assert heiseIE._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:26:13.009697
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heiseIE = HeiseIE()
    assert heiseIE._VALID_URL == (r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html')

# Generated at 2022-06-14 16:26:16.242516
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # just check non-error
    HeiseIE('http://www.heise.de/ct/artikel/c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2403911.html')

# Generated at 2022-06-14 16:26:18.945991
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.ie_key() == 'Heise'
    assert ie.ie_key() in ie.extractor_keywords()
    assert ie.ie_key() in ie.working_ie_keys()

# Generated at 2022-06-14 16:26:29.504168
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Test regex matching
    url = 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
    assert HeiseIE._match_id(url) == '2404147'
    url = 'http://www.heise.de/ct/ausgabe/2016-12-Spiele-3214137.html'
    assert HeiseIE._match_id(url) == '3214137'
    # Test extract_title() and _og_search_description()
    webpage = '<title>c\'t uplink 3.3: Owncloud, Tastaturen, Peilsender Smartphone</title>'

# Generated at 2022-06-14 16:26:39.287314
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Test constructor with test video
    heise_ie = HeiseIE(
        'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')

    # Test constructor with valid video id
    heise_ie = HeiseIE('2404147')

    # Test constructor with invalid video id
    heise_ie = HeiseIE('240414')

# Test that constructor throws an exception if an empty or null url is given
#   def test_HeiseIE_invalid_url(self):
#       """Test constructor with invalid url"""
#       with self.assertRaises(AssertionError):
#           HeiseIE(None)

# Test that can_extract_ext

# Generated at 2022-06-14 16:26:51.056209
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    # A sample 'url'
    heise_url = 'https://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html'
    # The expected 'video id'
    heise_id = '1_ntrmio2s'

    # The expected values for each info of the video
    heise_title = "nachgehakt: Wie sichert das c't-Tool Restric'tor Windows 10 ab?"
    heise_description = 'md5:47e8ffb6c46d85c92c310a512d6db271'
    heise_timestamp = 1512470717
    heise_upload_

# Generated at 2022-06-14 16:27:33.934935
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    try:
        HeiseIE()
    except:
        raise Exception('Failed to instantiate class HeiseIE')

if __name__ == '__main__':
    test_HeiseIE()

# Generated at 2022-06-14 16:27:35.250317
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    r = HeiseIE()
    print(r._VALID_URL)

# Generated at 2022-06-14 16:27:36.568420
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
	t = HeiseIE()
	assert(t)

# Generated at 2022-06-14 16:27:38.099216
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    i = HeiseIE()
    assert i.ie_key() == 'Heise'

# Generated at 2022-06-14 16:27:46.525115
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    url = "http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html"
    s = HeiseIE()._real_extract(url)
    assert s["id"] == "1_kkrq94sm"
    assert s["title"] == "Podcast: c't uplink 3.3 – Owncloud / Tastaturen / Peilsender Smartphone"
    assert s["description"] == "md5:c934cbfb326c669c2bcabcbe3d3fcd20"

# Generated at 2022-06-14 16:27:48.045286
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    obj = HeiseIE()
    assert isinstance(obj, InfoExtractor)



# Generated at 2022-06-14 16:27:51.753694
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    class MockExtractor(HeiseIE):
        def _real_extract(self, url):
            return
    assert isinstance(MockExtractor(url='http://www.heise.de/ct/ausgabe/2016-12-Spiele-3214137.html'), MockExtractor)

# Generated at 2022-06-14 16:27:52.578862
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()

# Generated at 2022-06-14 16:27:53.423546
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie._VALID_URL == HeiseIE._VALID_URL

# Generated at 2022-06-14 16:27:53.793100
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()

# Generated at 2022-06-14 16:29:22.093677
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE(kaltura_url="http://blah.com/blah") is not None

# Generated at 2022-06-14 16:29:24.727318
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    the_class = HeiseIE
    # The constructor should not raise any error
    instance = the_class()
    # The instance should be an object of the class
    assert isinstance(instance, the_class)

# Generated at 2022-06-14 16:29:35.518622
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    from .common import fake_urlopen
    from .kaltura import KalturaIE
    from .youtube import YoutubeIE
    from ..utils import (determine_ext, int_or_none, NO_DEFAULT,
                         parse_iso8601, smuggle_url, xpath_text,
                         )
    def _fake_urlopen(request):
        return fake_urlopen(request)
    def _smuggle_url(url, extra_query):
        return smuggle_url(url,extra_query)
    def _get_dummy_kaltura_url():
        return KalturaIE._extract_url(webpage)

# Generated at 2022-06-14 16:29:39.658145
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE()._VALID_URL == HeiseIE._VALID_URL
    assert HeiseIE()._TESTS == HeiseIE._TESTS


# Generated at 2022-06-14 16:29:40.734738
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE(InfoExtractor()).ie_name == "Heise"

# Generated at 2022-06-14 16:29:46.242460
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    info_extractor = HeiseIE()
    # Test direct calls to the constructor
    # It is also possible to use methods to do the tests
    assert isinstance(info_extractor, HeiseIE)
    # Test if the class has been added to the list of extractors
    assert HeiseIE.ie_key() in InfoExtractor._available_ie_keys()

# Generated at 2022-06-14 16:29:47.700585
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heiseie = HeiseIE(None)
    assert heiseie is not None

# Generated at 2022-06-14 16:29:49.373155
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise = HeiseIE()
    assert heise == HeiseIE()

# Generated at 2022-06-14 16:29:59.930535
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise = HeiseIE()
    assert heise._VALID_URL == 'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:30:02.347178
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.ie_key() == 'heise'
    assert HeiseIE.ie_key() == 'heise'

# Generated at 2022-06-14 16:33:35.360581
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise = HeiseIE(InfoExtractor())
    heise._real_extract('https://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')

# Generated at 2022-06-14 16:33:46.617292
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    """
    Unit tests to check if HeiseIE is working properly
    """
    heise_ie = HeiseIE()
    assert heise_ie._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'
    # assert heise_ie.__name__ == 'Heise IE'
    # assert heise_ie.ie_key() == 'heise'
    # assert heise_ie.server_url() == 'heise.de'
    # assert heise_ie.url_result(
    #     'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-

# Generated at 2022-06-14 16:33:51.583759
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Note: These videos change every time
    heise = HeiseIE()
    heise._download_webpage = lambda x: 'some webpage'
    heise.extract_from_url = lambda y: 'something'
    # Test that the constructor works correctly

# Generated at 2022-06-14 16:33:58.790249
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    instr = HeiseIE()
    assert HeiseIE.__name__ == "HeiseIE"
    assert instr.__name__ == "HeiseIE"
    assert instr.ie_key() == "Heise"
    assert instr._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'
    assert instr._TESTS[0]['url'] == 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
    assert instr._TESTS[0]['info_dict']['id'] == '1_kkrq94sm'