

# Generated at 2022-06-14 16:24:07.882476
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise_ie = HeiseIE()
    assert heise_ie._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:24:12.851741
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert ie.SUFFIX == "heise"
    assert ie.info_dict['title'] == "c't uplink 3.3 – Owncloud / Tastaturen / Peilsender Smartphone"
    assert ie.info_dict['description'] == "In der neuen Folge des c't uplink Podcasts besprechen wir Owncloud, Tastaturen und Peilsender für Smartphones."


# Generated at 2022-06-14 16:24:14.459081
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise = HeiseIE()
    assert isinstance(heise, InfoExtractor)

# Generated at 2022-06-14 16:24:19.135383
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise_ie = HeiseIE()
    heise_ie.extract('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')

# Generated at 2022-06-14 16:24:20.597250
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise_test = HeiseIE()

test_HeiseIE()

# Generated at 2022-06-14 16:24:31.730230
# Unit test for constructor of class HeiseIE
def test_HeiseIE():

    # Test with a specific URL to test the parsing of the page
    test_url = 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'

    # Test the extraction of url of specific page
    test_obj = HeiseIE()
    test_info_dict = test_obj._real_extract(test_url)


# Generated at 2022-06-14 16:24:32.647598
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    instance = HeiseIE(None)
    result = instance

# Generated at 2022-06-14 16:24:42.493811
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    test_url = "http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html"
    res = HeiseIE()._real_extract(test_url)
    assert res["id"] == "1_kkrq94sm"
    assert res["title"] == "Podcast: c't uplink 3.3 – Owncloud / Tastaturen / Peilsender Smartphone"
    assert res["ext"] == "mp4"
    assert res["timestamp"] == 1512734959

# Generated at 2022-06-14 16:24:50.453232
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    infoExtractor = HeiseIE()
    # Test calling _real_extract() when kaltura_url exists
    infoExtractor._real_extract('http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html')
    # Test calling _real_extract() when kaltura_url does not exist
    infoExtractor._real_extract('http://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html')

# Generated at 2022-06-14 16:24:58.245808
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, YoutubeIE)
    assert ie.IE_NAME == 'heise:video'
    assert ie._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'
    assert ie.ie_key() == 'Heise'
    assert ie.thumbnail == 're:https?://.*\.jpg'
    assert ie.uploader == 'heise video'
    assert ie.upload_date == 're:2017[12]\d{4}'

# Generated at 2022-06-14 16:25:23.970088
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Note that this test function is originally defined
    # outside a class, but to make it work, we added the
    # enclosing class definition.
    # The test (which is the only one) works, but we
    # suppress the 'too few public methods' warning
    # pylint: disable=no-self-use
    from .common import InfoExtractor
    # pylint: enable=no-self-use
    ie = InfoExtractor.for_site('heise')
    assert ie == HeiseIE

# Generated at 2022-06-14 16:25:27.458034
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.ie_key() == 'Heise'
    assert ie.ie_name() == "Heise (c't)"
    assert ie.description() == "The technology magazine Heise (c't) / heise.de"

# Generated at 2022-06-14 16:25:36.823762
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    h = HeiseIE()
    assert h.extract('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')['id'] == '1_kkrq94sm'
    assert h.extract('http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html')['id'] == '6kmWbXleKW4'

# Generated at 2022-06-14 16:25:42.759857
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    url = "http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html"
    with HeiseIE() as ie:
        ie.extract(url)



# Generated at 2022-06-14 16:25:43.568590
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()

# Generated at 2022-06-14 16:25:45.182924
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    instance = HeiseIE()
    assert(instance != None)


# Generated at 2022-06-14 16:25:46.967542
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    test = HeiseIE()
    assert test._VALID_URL == HeiseIE._VALID_URL

# Generated at 2022-06-14 16:25:48.081551
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()

# Generated at 2022-06-14 16:25:54.444849
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise = HeiseIE()
    assert heise._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:25:56.945587
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ''' In this test all the constructor variables are tested.
        The test is in the form of {constructor_arg: return value}
    '''
    assert HeiseIE({}) is not None

# Generated at 2022-06-14 16:26:25.729042
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.ie_key() == 'heise'
    assert ie.ie_name() == 'heise'
    assert ie.suitable('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert ie.suitable('https://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html')

# Generated at 2022-06-14 16:26:26.307921
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()

# Generated at 2022-06-14 16:26:33.033794
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    obj = HeiseIE('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html',
            {'skip_download': True})
    assert obj.url == 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
    assert obj.video_id == '1_kkrq94sm'
    assert obj.params == {'skip_download': True}

# Generated at 2022-06-14 16:26:35.797814
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')

# Generated at 2022-06-14 16:26:36.542175
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE

# Generated at 2022-06-14 16:26:47.926567
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    v = HeiseIE()
    assert v._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:26:57.604030
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE
    url1 = 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
    assert ie._VALID_URL == ie.valid_url(url1, ie.ie_key())
    assert 'zRM5yOa8xwr' == ie._extract_feed_id(
        'http://www.heise.de/video/embed/zRM5yOa8xwr')
    assert 'zRM5yOa8xwr' == ie._extract_feed_id(
        'http://www.heise.de/video/embed/zRM5yOa8xwr/')

# Generated at 2022-06-14 16:27:04.623146
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    url = 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
    assert ie._match_url(url)

    url = 'https://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html'
    assert ie._match_url(url)


# Generated at 2022-06-14 16:27:06.807155
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
	t = HeiseIE()
	t = t.__class__.__name__
	assert t == 'HeiseIE'

# Generated at 2022-06-14 16:27:07.458609
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()

# Generated at 2022-06-14 16:27:54.647949
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE().extract()

# Generated at 2022-06-14 16:28:06.683393
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE()._VALID_URL == r'^https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:28:09.244498
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Unit test: HeiseIE
    assert HeiseIE()._VALID_URL == HeiseIE._VALID_URL

# Generated at 2022-06-14 16:28:18.517094
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    url = 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
    # Testing constructor
    test_object = HeiseIE()
    assert test_object._VALID_URL == HeiseIE._VALID_URL
    assert test_object._TESTS == HeiseIE._TESTS
    assert test_object._download_webpage == InfoExtractor._download_webpage
    assert test_object._match_id == HeiseIE._match_id
    assert test_object._real_extract == HeiseIE._real_extract
    assert test_object.suitable == InfoExtractor.suitable
    assert test_object.IE_NAME == 'heise'
   

# Generated at 2022-06-14 16:28:28.961505
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE('http://www.heise.de/ct/artikel/c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2403911.html')
    assert ie.url == 'http://www.heise.de/ct/artikel/c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2403911.html'
    assert ie.video_id == 'http://www.heise.de/ct/artikel/c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2403911.html'
    assert isinstance(ie._real_extract(ie.url), dict)

# Generated at 2022-06-14 16:28:30.513355
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE._VALID_URL

# Generated at 2022-06-14 16:28:33.239305
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    try:
        assert(HeiseIE() == None)
    except AssertionError:
        raise AssertionError("HeiseIE instance not created properly: " + err)


# Generated at 2022-06-14 16:28:34.100944
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE(InfoExtractor())

# Generated at 2022-06-14 16:28:40.531685
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.name == 'heise'
    assert ie.ie_key() == 'heise'
    assert ie.host == 'heise.de'
    assert ie.description == 'heise online'
    assert ie._VALID_URL == 'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:28:41.562757
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()

# Generated at 2022-06-14 16:29:45.429557
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    hie = HeiseIE()
    assert hie._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:29:52.580874
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    from .generic import GenericIE
    # Constructor of class HeiseIE
    HeiseIE("http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html")
    # Constructor of class GenericIE
    GenericIE("http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html")

# Generated at 2022-06-14 16:29:53.166396
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()

# Generated at 2022-06-14 16:30:03.191108
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE(None)
    assert ie.ie_key() != "HeiseIE"
    assert ie.ie_key() == 'Heise'
    assert ie.ie_name() is not None
    assert ie.ie_description() is not None
    assert ie.is_enabled()
    # Tests for real extractors
    ie = HeiseIE(None)
    url = "http://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html"
    info = ie.extract(url)
    assert info['id']
    assert info['title']
    assert info['description']
    assert info['timestamp']

# Generated at 2022-06-14 16:30:05.133154
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    def test_class_instance():
        ie = HeiseIE()
        assert ie.ie_key() == 'Heise'

    test_class_instance()


# Generated at 2022-06-14 16:30:15.708222
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    print('test HeiseIE constructor')
    heise_ie = HeiseIE()
    assert heise_ie._VALID_URL.search('https://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')

    print('test HeiseIE._real_extract')
    kaltura_id = '1_kkrq94sm'
    kaltura_url = 'kaltura:2238431:' + kaltura_id

# Generated at 2022-06-14 16:30:25.404094
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    from mock import Mock
    from unittest import TestCase

    _part = Mock()
    _part.get = Mock(return_value = 'some_value')

    _entry = Mock()
    _entry.findall = Mock(return_value = [_part])

    _doc = Mock()
    _doc.findall = Mock(return_value = [_entry])

    _download_xml = Mock(return_value=_doc)

    _match_id = Mock(return_value='matchID')
    _html_search_regex = Mock(return_value='html_searched_value')
    _search_regex = Mock(return_value='searched_value')
    _og_search_description = Mock(return_value='some_og_description')

# Generated at 2022-06-14 16:30:31.998512
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Heiser address
    url = 'http://www.heise.de/ct/ausgabe/2016-12-Spiele-3214137.html'
    test_url = HeiseIE(url)
    assert test_url.match(url)
    assert test_url._VALID_URL == url


# Smoke test for constructor of class HeiseIE

# Generated at 2022-06-14 16:30:34.881573
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE.suitable(HeiseIE._VALID_URL)
    heise_ie = HeiseIE(HeiseIE._VALID_URL)
    assert heise_ie.extract() != None



# Generated at 2022-06-14 16:30:38.886758
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE('https://www.heise.de/ct/artikel/c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2403911.html?wt_mc=rss.ho.beitrag.atom')
    print(ie)

# Generated at 2022-06-14 16:32:34.323789
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE._VALID_URL == 'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:32:35.411413
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heiseIE = HeiseIE()
    assert heiseIE.ie_key()

# Generated at 2022-06-14 16:32:45.988552
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    info_dict = HeiseIE()._real_extract("http://www.heise.de/ct/artikel/c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2403911.html")

# Generated at 2022-06-14 16:32:52.835817
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # create an instance of the class to test
    hie = HeiseIE()
    # test the method
    assert hie._VALID_URL.match('https://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert hie._VALID_URL.match('https://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html')

# Generated at 2022-06-14 16:32:54.555052
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    IE = HeiseIE({})
assert isinstance(IE._TESTS, list)

# Generated at 2022-06-14 16:32:58.365814
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE('http://www.heise.de/ct/artikel/c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2403911.html')
    ie.download()

# Generated at 2022-06-14 16:32:58.847288
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()

# Generated at 2022-06-14 16:33:08.733152
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    ie_result = ie.extract('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')

    assert ie_result['id'] == '1_kkrq94sm'
    assert ie_result['title'] == "Podcast: c't uplink 3.3 – Owncloud / Tastaturen / Peilsender Smartphone"
    assert ie_result['timestamp'] == 1512734959
    assert ie_result['upload_date'] == '20171208'
    assert ie_result['description'] == 'md5:c934cbfb326c669c2bcabcbe3d3fcd20'

# Generated at 2022-06-14 16:33:10.402714
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Construct an instance of HeiseIE
    HeiseIE_instance = HeiseIE()
    # Check that it is an instance of InfoExtractor
    assert (isinstance(HeiseIE_instance, InfoExtractor))

# Generated at 2022-06-14 16:33:21.438915
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    i = HeiseIE()
    assert i._VALID_URL == 'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'