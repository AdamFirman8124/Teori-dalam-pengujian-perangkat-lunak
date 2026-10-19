

# Generated at 2022-06-14 16:24:05.689804
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.url_patterns()

# Generated at 2022-06-14 16:24:10.898199
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    url = 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
    HeiseIE(url)

# Generated at 2022-06-14 16:24:12.571193
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    test_class = HeiseIE([], {}, None)
    assert test_class

# Generated at 2022-06-14 16:24:24.651893
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise = HeiseIE()
    assert(heise.suitable('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'))
    assert(heise.suitable('http://www.heise.de/ct/artikel/c-t-uplink-20-8-Staubsaugerroboter-Xiaomi-Vacuum-2-AR-Brille-Meta-2-und-Android-rooten-3959893.html'))

# Generated at 2022-06-14 16:24:33.795518
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise = HeiseIE()
    assert heise._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'
    assert heise._TESTS[0]['url'] == 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
    assert heise._TESTS[0]['info_dict']['id'] == '1_kkrq94sm'
    assert heise._TESTS[0]['info_dict']['ext'] == 'mp4'

# Generated at 2022-06-14 16:24:44.654828
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # unit test for the constructor of class HeiseIE
    # override _download_webpage to avoid network access
    # override _search_regex to avoid dependence on web page content
    def heise_search_regex(pattern, string, name, default=None, fatal=True, flags=0, group=None):
        # override _search_regex to avoid dependence on web page content
        return str(name)
    heise_ie = HeiseIE()
    heise_ie._download_webpage = lambda url, video_id, note=None, errnote=None, fatal=True: url
    heise_ie._search_regex = heise_search_regex

# Generated at 2022-06-14 16:24:47.591855
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert(ie.ie_key())
    assert(ie.ie_key() == 'Heise')

test_cases = [
    (test_HeiseIE()),
]

# Generated at 2022-06-14 16:24:48.134420
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE

# Generated at 2022-06-14 16:24:57.279424
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    h = HeiseIE()
    assert h.suitable('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert not h.suitable('https://www.heise.de/ct/artikel/c-t-uplink-20-8-Staubsaugerroboter-Xiaomi-Vacuum-2-AR-Brille-Meta-2-und-Android-rooten-3959893.html')

# Generated at 2022-06-14 16:24:58.907298
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    expect = HeiseIE
    assert HeiseIE.constructor() == expect

# Generated at 2022-06-14 16:25:11.382382
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.IE_NAME == 'heise'
    assert ie._VALID_URL == HeiseIE._VALID_URL
    assert ie._TESTS == HeiseIE._TESTS

# Generated at 2022-06-14 16:25:20.589527
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    url = 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
    obj = HeiseIE()
    assert obj._VALID_URL == HeiseIE._VALID_URL
    assert obj._TESTS == HeiseIE._TESTS
    assert obj.IE_NAME == HeiseIE.IE_NAME
    assert obj.ie_key() == HeiseIE.ie_key()
    assert obj._extract_url(url) == HeiseIE._extract_url(url)

# Generated at 2022-06-14 16:25:22.657167
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise = HeiseIE()
    assert heise
    return heise

# Generated at 2022-06-14 16:25:26.630690
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    query_string = 'container=2365&sequenz=3314'
    assert ie._download_xml(
        'http://www.heise.de/videout/feed', query=query_string
    ) is not None

# Generated at 2022-06-14 16:25:27.305593
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()

# Generated at 2022-06-14 16:25:31.435819
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    url = 'http://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html'
    HeiseIE(url)

# Generated at 2022-06-14 16:25:38.907542
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # function to check a constructor of class HeiseIE
    info_heise = heise_url_handler('https://www.heise.de/ct/artikel/c-t-uplink-20-8-Staubsaugerroboter-Xiaomi-Vacuum-2-AR-Brille-Meta-2-und-Android-rooten-3959893.html')

    # check if the right URL was returned
    assert info_heise['url'] == 'https://www.heise.de/ct/artikel/c-t-uplink-20-8-Staubsaugerroboter-Xiaomi-Vacuum-2-AR-Brille-Meta-2-und-Android-rooten-3959893.html'
    # check if the right extractor was returned
    assert info

# Generated at 2022-06-14 16:25:39.474051
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert True

# Generated at 2022-06-14 16:25:48.390468
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise = HeiseIE()
    assert isinstance(heise, InfoExtractor)
    assert hasattr(heise, '_VALID_URL')
    assert heise._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'
    assert hasattr(heise, '_TESTS')
    assert len(heise._TESTS) == 7
    # assert hasattr(heise, '_real_extract')

# Generated at 2022-06-14 16:25:50.600838
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # check if the dictionary contains the necessary attributes
    ie = HeiseIE({})
    assert ie.IE_NAME == 'heise'
    assert ie.IE_DESC == 'heise video'

# Generated at 2022-06-14 16:26:18.201839
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.get_info('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert ie.get_info('https://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html')

# Generated at 2022-06-14 16:26:28.752983
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    """ Unit test for HeiseIE. """
    url = 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
    info_dict = {
            'id': '1_kkrq94sm',
            'ext': 'mp4',
            'title': "Podcast: c't uplink 3.3 – Owncloud / Tastaturen / Peilsender Smartphone",
            'timestamp': 1512734959,
            'upload_date': '20171208',
            'description': 'md5:c934cbfb326c669c2bcabcbe3d3fcd20',
        }
    params = {'skip_download': True}

    ie_

# Generated at 2022-06-14 16:26:33.212684
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Make a unit test
    # Test - class HeiseIE
    # Construct a video url to be used in unit test
    video_url = 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
    # Construct a instance of class HeiseIE
    instit = HeiseIE()
    instit._real_extract(video_url)

# Generated at 2022-06-14 16:26:34.371150
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE()._VALID_URL == HeiseIE._VALID_URL

# Generated at 2022-06-14 16:26:35.292777
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE != None

# Generated at 2022-06-14 16:26:36.592383
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()

# Generated at 2022-06-14 16:26:47.983311
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    url = "http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html"
    heiseIE = HeiseIE()
    assert(heiseIE._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html')

# Generated at 2022-06-14 16:26:57.636793
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    myIE = HeiseIE()
    assert myIE._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:26:58.133352
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE()

# Generated at 2022-06-14 16:27:01.059474
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    e = HeiseIE()
    # check that regex matches urls
    # assert e._VALID_URL.search(url)
    assert HeiseIE._match_id(e, "https://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html") == "2404147"

# Generated at 2022-06-14 16:27:47.306178
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE.__name__ == 'HeiseIE'

# Generated at 2022-06-14 16:27:50.748200
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    import unittest
    class TestHeiseIE(unittest.TestCase):
        def test_constructor(self):
            try:
                heiseIE = HeiseIE()
            except Exception as inst:
                self.fail(inst)

    unittest.main()

# Generated at 2022-06-14 16:27:52.978003
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Construct an instance of HeiseIE
    ie = HeiseIE()
    # Make sure that the HeiseIE constructor does not throw any exception
    assert ie



# Generated at 2022-06-14 16:28:01.698191
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    obj1 = HeiseIE('www.heise.de/ct/ausgabe/2017-3-Das-Test-UzuoOkyEynUtF7fjG2Q27C7Vk.html', 'http://www.heise.de/ct/ausgabe/2017-3-Das-Test-UzuoOkyEynUtF7fjG2Q27C7Vk.html', '3713119')
    assert obj1.get_id() == '3713119'
    assert obj1.get_url() == 'http://www.heise.de/ct/ausgabe/2017-3-Das-Test-UzuoOkyEynUtF7fjG2Q27C7Vk.html'

# Generated at 2022-06-14 16:28:05.141424
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    hs = HeiseIE()


# Test: https://github.com/ytdl-org/youtube-dl/pull/16042

# Generated at 2022-06-14 16:28:09.548547
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE().extract(('http://www.heise.de/video/artikel/'
                              'Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'))

# Generated at 2022-06-14 16:28:10.839690
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    test = HeiseIE()
    assert test


# Generated at 2022-06-14 16:28:11.783489
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    e = HeiseIE()
    assert e

# Generated at 2022-06-14 16:28:14.876751
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    class_ = globals()['HeiseIE']
    instance = class_()
    assert isinstance(class_, type)
    assert isinstance(instance, class_)

# Generated at 2022-06-14 16:28:22.899279
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Instantiate class to test constructor
    heise = HeiseIE()
    assert heise is not None
    # Instantiate class to test _check_existance_of_url()
    heise = HeiseIE('http://www.heise.de/ct/artikel/c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2403911.html')
    assert heise is not None
    # Instantiate class to test _check_existance_of_url()
    heise = HeiseIE('not a real url')
    assert heise is None

# Generated at 2022-06-14 16:30:06.096345
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE._TESTS

# Generated at 2022-06-14 16:30:16.852049
# Unit test for constructor of class HeiseIE

# Generated at 2022-06-14 16:30:24.822731
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert(HeiseIE._VALID_URL==r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html')
    assert(HeiseIE.ie_key()== 'heise')
    assert(HeiseIE.ie_key()== 'Heise')
    assert(HeiseIE._TESTS[0]['url']=='http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')

# Generated at 2022-06-14 16:30:25.848709
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE(None)

# Generated at 2022-06-14 16:30:29.408798
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.ie_key() == 'heise'
    assert ie.video_id == '1_ntrmio2s'



# Generated at 2022-06-14 16:30:39.599049
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'
    assert ie._TESTS[0]['url'] == 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
    assert ie._TESTS[0]['info_dict']['id'] == '1_kkrq94sm'
    assert ie._TESTS[0]['info_dict']['ext'] == 'mp4'

# Generated at 2022-06-14 16:30:41.549563
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    test = HeiseIE()
    assert(test.extract.__func__.__name__ == '_real_extract')

# Generated at 2022-06-14 16:30:43.021967
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
	test = HeiseIE()
	test.suite()


# Generated at 2022-06-14 16:30:44.024595
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()

# Generated at 2022-06-14 16:30:52.131790
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE.__name__ == "HeiseIE"
    assert HeiseIE._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'
    assert HeiseIE.__doc__ is None
    assert len(HeiseIE._TESTS) > 0
    assert len(HeiseIE._TESTS[0]) > 0
    assert len(HeiseIE._TESTS[0]['url']) > 0
    t = HeiseIE._TESTS[0]['url']