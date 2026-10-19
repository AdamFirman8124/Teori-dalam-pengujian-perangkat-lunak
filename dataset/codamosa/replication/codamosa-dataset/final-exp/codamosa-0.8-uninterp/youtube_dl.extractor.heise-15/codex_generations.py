

# Generated at 2022-06-14 16:24:03.859894
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE(InfoExtractor())

# Generated at 2022-06-14 16:24:04.354579
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE()

# Generated at 2022-06-14 16:24:13.290003
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heiseIE = HeiseIE()
    # test valid URL
    valid_url = 'https://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html'
    url_info = heiseIE._real_extract(valid_url)
    assert 'nachgehakt: Wie sichert das c\'t-Tool Restric\'tor Windows 10 ab?' == url_info['title']

# Generated at 2022-06-14 16:24:14.930359
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Test constructor that ensures that HeiseIE is created
    HeiseIE()

# Generated at 2022-06-14 16:24:26.757527
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    i = HeiseIE()
    assert i._VALID_URL == 'https?://(?:www\\.)?heise\\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\\.html'
    assert i._TESTS[0].get('url') == 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
    assert i._TESTS[0].get('info_dict').get('id') == '1_kkrq94sm'
    assert i._TESTS[0].get('info_dict').get('ext') == 'mp4'

# Generated at 2022-06-14 16:24:31.856743
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.ie_key() == 'heise'
    assert ie.ie_name() == 'heise'
    assert ie.suitable()
    assert ie._VALID_URL == 'https?://(?:www\\.)?heise\\.de/(?:[^/]+/)*[^/]+-(?P<id>[0-9]+)\\.html'

# Generated at 2022-06-14 16:24:43.463575
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
	# 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
	url = 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
	# '1_kkrq94sm'
	# 'Podcast: c't uplink 3.3 – Owncloud / Tastaturen / Peilsender Smartphone'

# Generated at 2022-06-14 16:24:47.762440
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    n = HeiseIE('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert n is not None


# Generated at 2022-06-14 16:24:48.401317
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert True

# Generated at 2022-06-14 16:24:57.420905
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # test urls
    url = "http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html"
    ie = HeiseIE()
    assert isinstance(ie, HeiseIE)
    result = ie.extract(url)
    assert result['id'] == '6kmWbXleKW4'
    assert result['title'] == 'NEU IM SEPTEMBER | Netflix'
    assert result['uploader'] == 'Netflix Deutschland, Österreich und Schweiz'
    assert result['uploader_id'] == 'netflixdach'
    assert result['upload_date'] == '20170830'

# Generated at 2022-06-14 16:25:07.471869
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heiseIE = HeiseIE('heise.de')
    assert heiseIE is not None

# Generated at 2022-06-14 16:25:10.410647
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.suitable(HeiseIE._VALID_URL)
    assert ie.IE_NAME == 'heise'

# Generated at 2022-06-14 16:25:11.382828
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    instance = HeiseIE() 
    instance.match()

# Generated at 2022-06-14 16:25:15.581369
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    before = HeiseIE.__dict__.copy()
    HeiseIE()
    after = HeiseIE.__dict__.copy()
    # Make sure instance attributes are not created
    keys_before = set(before.keys())
    keys_after  = set(after.keys())
    assert after == before
    assert keys_before == keys_after

# Generated at 2022-06-14 16:25:17.992256
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    inst = HeiseIE()
    assert inst.ie_key() == 'Heise'
    assert inst.ie_name() == 'heise'

# Generated at 2022-06-14 16:25:30.609216
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE.suitable('https://www.heise.de/video/artikel/c-t-uplink-Owncloud-Tastaturen-Peilsender-Smartphone-2404251.html?wt_mc=rss.ho.beitrag.atom')
    assert HeiseIE.suitable('https://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert not HeiseIE.suitable('https://www.heise.de/ct/artikel/c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2403911.html')

# Generated at 2022-06-14 16:25:31.376377
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()

# Generated at 2022-06-14 16:25:37.986552
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    h = HeiseIE()

    input = "http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html"
    output = "1_kkrq94sm"
    assert(h._match_id(input) == output)

    input = "https://www.heise.de/ct/artikel/c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2403911.html"
    assert(h._match_id(input) == output)

# Generated at 2022-06-14 16:25:46.192997
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Construct an instance of HeiseIE
    heise_ie = HeiseIE()
    # test whether it's an instance of InfoExtractor
    assert isinstance(heise_ie, InfoExtractor)
    # test whether it's the correct class
    assert isinstance(heise_ie, HeiseIE)
    # test whether it's not an instance of the other classes
    assert not isinstance(heise_ie, KalturaIE)
    assert not isinstance(heise_ie, YoutubeIE)

# Generated at 2022-06-14 16:25:56.463013
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # URL missing trailing slash
    # test_constructor_2
    test = HeiseIE('http://www.heise.de/ct/ausgabe/2016-12-Spiele-3214137.html')
    assert 'https://www.heise.de/ct/ausgabe/2016-12-Spiele-3214137.html' == test._VALID_URL
    assert '3214137' == test._match_id('http://www.heise.de/ct/ausgabe/2016-12-Spiele-3214137.html')
    assert '<div[^>]+class="videoplayerjw"[^>]+data-title="([^"]+)"' == test._TESTS[0]['info_dict']['title']

# Generated at 2022-06-14 16:26:22.887352
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    _test_HeiseIE = HeiseIE()
    assert _test_HeiseIE._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:26:25.786913
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    obj = HeiseIE()
    assert obj.ie_key() == 'Heise'
    assert obj.ie_name() == 'Heise'

# Generated at 2022-06-14 16:26:32.709930
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    info_dict = HeiseIE()._real_extract(
        'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert info_dict['id'] == '1_kkrq94sm'
    assert info_dict['title'] == "Podcast: c't uplink 3.3 – Owncloud / Tastaturen / Peilsender Smartphone"
    assert info_dict['description'] == 'md5:c934cbfb326c669c2bcabcbe3d3fcd20'

# Generated at 2022-06-14 16:26:42.330272
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    test_1 = ie._real_extract(
        "https://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html")
    print(test_1)
    test_2 = ie._real_extract(
        "https://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html")
    print(test_2)

# Generated at 2022-06-14 16:26:43.268290
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()

# Generated at 2022-06-14 16:26:54.434723
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    info_extractor = HeiseIE()
    assert info_extractor._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:27:00.225116
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    """Test if we can find the url of Heise's video."""
    heise_ie = HeiseIE('https://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html')
    video_url = heise_ie.extract()
    assert video_url['id'] == '1_ntrmio2s'
    assert video_url['title'] == "nachgehakt: Wie sichert das c't-Tool Restric'tor Windows 10 ab?"

# Generated at 2022-06-14 16:27:02.273121
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    a = HeiseIE()
    assert(isinstance(a, HeiseIE))
    return a

# Generated at 2022-06-14 16:27:03.364296
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert(HeiseIE('heise').ie_key() == HeiseIE.ie_key())

# Generated at 2022-06-14 16:27:04.811143
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE.__name__ == 'HeiseIE'

# Generated at 2022-06-14 16:27:49.639805
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    r = HeiseIE()

# Generated at 2022-06-14 16:27:57.034467
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    h = HeiseIE('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')

    assert(h._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html')
    assert(h._TESTS[1].get('url') == 'http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html')

# Generated at 2022-06-14 16:28:09.241102
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    test_obj = HeiseIE(InfoExtractor())

    assert test_obj._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:28:10.529582
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    t = HeiseIE()
    assert t == HeiseIE()

# Generated at 2022-06-14 16:28:12.105981
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE == InfoExtractor.loader.get_class(HeiseIE.ie_key())

# Generated at 2022-06-14 16:28:14.169501
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, YoutubeIE)

# Generated at 2022-06-14 16:28:18.013465
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    u = 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
    assert HeiseIE._info(u) != None

# Generated at 2022-06-14 16:28:22.770607
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert(ie.ie_key() == 'heise')
    assert(ie.ie_key() in ie.GENERIC_IE_KEY_MAP.keys())
    assert(ie.ie_key() not in ie.WRONG_IE_KEY_MAP.keys())

# Generated at 2022-06-14 16:28:23.561964
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE.ie_key() is not None

# Generated at 2022-06-14 16:28:24.832435
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.ie_key() == 'heise'

# Generated at 2022-06-14 16:30:08.494219
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    url = "http://www.heise.de/ct/artikel/c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2403911.html"
    heise_ie = HeiseIE()
    assert heise_ie._VALID_URL == heise_ie.valid_url
    assert (isinstance(heise_ie._VALID_URL, (str, type(None))))
    assert heise_ie._TESTS == heise_ie.tests
    assert (isinstance(heise_ie._TESTS, list))
    assert heise_ie._real_extract == heise_ie._real_extract
    assert (isinstance(heise_ie._real_extract, (classmethod, types.MethodType, types.FunctionType)))

# Generated at 2022-06-14 16:30:10.243767
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert isinstance(ie, InfoExtractor)

# Generated at 2022-06-14 16:30:20.916751
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    video_url = 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
    ie = HeiseIE(video_url)
    assert ie.__class__.__name__ == 'HeiseIE'
    assert ie.valid_url(video_url) == True
    assert ie.get_url() == video_url
    assert ie.get_id() == 'Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147'


# Generated at 2022-06-14 16:30:25.696495
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
     assert HeiseIE('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')._VALID_URL == 'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'


# Generated at 2022-06-14 16:30:31.606416
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE('http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html')
    assert isinstance(ie, HeiseIE)

# Generated at 2022-06-14 16:30:32.892659
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert(repr(HeiseIE('id', 'url')) != None)

# Generated at 2022-06-14 16:30:42.235797
# Unit test for constructor of class HeiseIE

# Generated at 2022-06-14 16:30:43.324632
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ieobj = HeiseIE()

# Generated at 2022-06-14 16:30:47.734773
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    ie.extract(test_HeiseIE.url)

test_HeiseIE.url = 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'

# Generated at 2022-06-14 16:30:48.346904
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE(None, None)