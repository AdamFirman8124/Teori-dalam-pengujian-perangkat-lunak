

# Generated at 2022-06-14 16:24:06.266613
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise_ie = HeiseIE()
    assert heise_ie._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'



# Generated at 2022-06-14 16:24:08.122987
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    obj = HeiseIE()

# Generated at 2022-06-14 16:24:10.706216
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    yt = HeiseIE()
    assert yt.ie_key() == 'Heise'
    assert yt.ie_key() in YoutubeIE.ies

# Generated at 2022-06-14 16:24:20.908965
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE('https://www.heise.de/ct/artikel/c-t-uplink-20-8-Staubsaugerroboter-Xiaomi-Vacuum-2-AR-Brille-Meta-2-und-Android-rooten-3959893.html')
    assert ie.url == 'https://www.heise.de/ct/artikel/c-t-uplink-20-8-Staubsaugerroboter-Xiaomi-Vacuum-2-AR-Brille-Meta-2-und-Android-rooten-3959893.html'
    assert ie.video_id == '1_59mk80sf'


# Generated at 2022-06-14 16:24:23.483406
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    """Test constructor of HeiseIE"""
    # Initialize class
    _ = HeiseIE(InfoExtractor())

# Generated at 2022-06-14 16:24:24.357375
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Initialize object
    # It is checked that its constructor doesn't raise an exception
    HeiseIE()

# Generated at 2022-06-14 16:24:28.404470
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    info = HeiseIE('https://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')


# Generated at 2022-06-14 16:24:30.121546
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE({})
    assert ie._VALID_URL == HeiseIE._VALID_URL

# Generated at 2022-06-14 16:24:37.561930
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    # Test URL
    assert ie._VALID_URL == HeiseIE._VALID_URL
    # Test whether it raises an exception when you try to extract a YouTube video
    info = ie.extract(ie._TESTS[1]["url"])
    assert info["uploader_id"] == "netflixdach"
    # Test whether it raises an exception when you try to extract a non existent video
    info = ie.extract(ie._TESTS[0]["url"])
    assert info["id"] == "1_kkrq94sm"
    # Test whether it raises an exception when you try to extract a Kaltura video
    info = ie.extract(ie._TESTS[2]["url"])
    assert info["id"] == "1_ntrmio2s"


# Generated at 2022-06-14 16:24:42.444374
# Unit test for constructor of class HeiseIE

# Generated at 2022-06-14 16:25:06.093896
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    string = "https://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html?seite=3"
    match = ie._VALID_URL.match(string)
    ie._real_extract(string)

# Generated at 2022-06-14 16:25:15.417622
# Unit test for constructor of class HeiseIE

# Generated at 2022-06-14 16:25:16.472321
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    instance = HeiseIE()

# Generated at 2022-06-14 16:25:27.099624
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
        # This can be any url of we want to test
        url = 'http://www.heise.de/ct/artikel/c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2403911.html'
        heise_ie = HeiseIE()

        # We check if the expected class, in this case HeiseIE,
        # is returned
        assert(heise_ie is not None)

        # If the call to _download_webpage is working the returned value will
        # not be none
        assert(heise_ie._download_webpage(url, None) is not None)

# Generated at 2022-06-14 16:25:27.711733
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE

# Generated at 2022-06-14 16:25:32.166039
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    file = 'heise_video.html'
    url = 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
    HeiseIE().download(url)

# Generated at 2022-06-14 16:25:39.288054
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise_ie = HeiseIE()
    assert heise_ie._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'
    assert heise_ie._TESTS[0]['url'] == 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
    assert heise_ie._TESTS[0]['md5'] == 'c415a44a7a1c9f9f76e099c6fda81b1f'

# Generated at 2022-06-14 16:25:45.854036
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    url_for_testing = 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
    heise = HeiseIE(True)
    heise._real_extract(url_for_testing)
    return heise

# Generated at 2022-06-14 16:25:49.112420
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise_ie = HeiseIE()
    assert (heise_ie._VALID_URL ==
            "https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-[0-9]+.html")

# Generated at 2022-06-14 16:25:50.877278
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    try:
        assert HeiseIE() is not None
    except Exception as e:
        print("\n Test of HeiseIE constructor failed: ", e)
        raise e


# Generated at 2022-06-14 16:26:10.031119
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE.ie_key() == 'heise'
    assert HeiseIE(None)._VALID_URL == HeiseIE._VALID_URL

# Generated at 2022-06-14 16:26:19.352928
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise = HeiseIE()
    assert heise.suitable("http://www.heise.de/ct/artikel/c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2403911.html")
    assert heise.suitable("http://www.heise.de/newsticker/meldung/c-t-uplink-Owncloud-Tastaturen-Peilsender-Smartphone-2404251.html?wt_mc=rss.ho.beitrag.atom")
    assert heise.suitable("http://www.heise.de/ct/ausgabe/2016-12-Spiele-3214137.html")
    # BBC homepage news

# Generated at 2022-06-14 16:26:21.320930
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    '''
    Test whether the HeiseIE constructor can be called
    '''
    HeiseIE()

# Generated at 2022-06-14 16:26:24.204400
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE.__name__ == 'HeiseIE'
    assert HeiseIE.__doc__ != None


# Generated at 2022-06-14 16:26:25.549841
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    g = globals()
    for key in g:
        if key.startswith('Heise') and isinstance(g[key], type):
            assert g[key] != HeiseIE
            assert issubclass(g[key], HeiseIE)

# Generated at 2022-06-14 16:26:25.993176
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()

# Generated at 2022-06-14 16:26:33.755914
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Test class instance HeiseIE(InfoExtractor)
    assert HeiseIE != None
    assert hasattr(HeiseIE, '_VALID_URL')
    assert HeiseIE._VALID_URL != ''
    assert HeiseIE._VALID_URL == HeiseIE.__module__.split('.')[-1]
    assert hasattr(HeiseIE, '_TESTS')
    assert HeiseIE._TESTS != []
    assert hasattr(HeiseIE, '_download_webpage')
    assert callable(HeiseIE._download_webpage)
    assert hasattr(HeiseIE, '_match_id')
    assert callable(HeiseIE._match_id)
    # Test object instance HeiseIE(InfoExtractor)
    ie = HeiseIE()
    assert ie != None

# Generated at 2022-06-14 16:26:34.731579
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE()._VALID_URL == HeiseIE._VALID_URL

# Generated at 2022-06-14 16:26:41.245179
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie
    assert ie._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:26:50.251509
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    extractor = HeiseIE()
    url = HeiseIE._VALID_URL
    url = url.replace('http', 'https')
    url_m = extractor._match_id('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert(url_m == 'Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147')

# Generated at 2022-06-14 16:27:30.754332
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE('heise.de')
    assert ie.name == 'heise.de'

# Generated at 2022-06-14 16:27:37.015087
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    test_class = HeiseIE('Heise', False)
    assert test_class._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'
    assert test_class._TESTS is not None
    assert test_class._download_webpage is not None



# Generated at 2022-06-14 16:27:38.759467
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE().extractor_key == "HeiseIE"

# Generated at 2022-06-14 16:27:39.319028
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE

# Generated at 2022-06-14 16:27:46.107489
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Prepare input arguments for instantiating a HeiseIE object
    url = 'https://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html'
    ie = InfoExtractor(configure=False)
    # Instantiate an HeiseIE object for an extraction test
    HeiseIE(ie)
    # Run unit test
    ie.extract(url)

# Generated at 2022-06-14 16:27:49.392261
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:27:49.927676
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()

# Generated at 2022-06-14 16:27:51.300246
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE()._VALID_URL == HeiseIE._VALID_URL
    assert HeiseIE()._TESTS == HeiseIE._TESTS
    assert HeiseIE().__name__ == "HeiseIE"

# Generated at 2022-06-14 16:27:53.192471
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE().ie_key() == 'Heise'

if __name__ == '__main__':
    test_HeiseIE()

# Generated at 2022-06-14 16:27:59.181932
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    """Unit test for constructor of class HeiseIE."""
    # Here are unit tests to test if all kinds of articles are correctly handled by the constructor.
    # Each subtest opens a specific kind of article and should pass, if the constructor can see
    # that there is no video embedded in the article.
    # The subtest fails, if the constructor finds video embeddings that were not expected. This is
    # either an error in the constructor or a change in the article structure at the webpage.
    webpage = 'http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html'
    ie = HeiseIE(webpage)
    # If the constructor finds a video in the article, the entry contains a _type that indicates a video

# Generated at 2022-06-14 16:29:33.974452
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    url = 'http://www.heise.de/ct/artikel/Exklusiv-c-t-uplink-Britische-Spionage-Affaere-britische-Spionagetechnik-3779196.html'
    __name__ = 'heise'
    ie = HeiseIE(url, __name__)

# Generated at 2022-06-14 16:29:37.865753
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert ie.url_result['_type'] == 'url_transparent'
    assert ie.url_result['ie_key'] == 'Kaltura'

# Generated at 2022-06-14 16:29:40.607427
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE(None)
    assert ie.VALID_URL == HeiseIE._VALID_URL
    assert ie._TESTS == HeiseIE._TESTS

# Generated at 2022-06-14 16:29:47.047422
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    """
    It behaves as a video extractor for the Heise website.
    It extracts title, description and thumbnail.
    It downloads and extracts the video formats (m3u8) from the container and sequenz ids.
    """
    from .test_video_download import libtbx_env
    libtbx_env.setUp()
    url = 'http://www.heise.de/ct/ausgabe/2016-12-Spiele-3214137.html'
    HeiseIE().download_and_extract(url)
    libtbx_env.tearDown()

# Generated at 2022-06-14 16:29:50.764414
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE("http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html")
    assert ie != None

# Generated at 2022-06-14 16:30:01.475209
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:30:06.052140
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'
    assert ie._TESTS[1]['md5'] == 'e403d2b43fea8e405e88e3f8623909f1'
    assert ie._TESTS[1]['info_dict']['id'] == '6kmWbXleKW4'
    assert ie._TESTS[1]['info_dict']['ext'] == 'mp4'
    assert ie._TESTS[1]['info_dict']['title'] == 'NEU IM SEPTEMBER | Netflix'

# Generated at 2022-06-14 16:30:16.809058
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heiseIE = HeiseIE()
    assert heiseIE._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'
    assert heiseIE._TESTS[0]['url'] == 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
    assert heiseIE._TESTS[0]['info_dict']['id'] == '1_kkrq94sm'
    assert heiseIE._TESTS[0]['info_dict']['ext'] == 'mp4'
    assert heiseIE._TES

# Generated at 2022-06-14 16:30:25.978570
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    t = HeiseIE(InfoExtractor())  # noqa
    assert HeiseIE.ie_key() == 'heise'
    assert HeiseIE.suitable('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert HeiseIE._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:30:27.509121
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE(None)._VALID_URL == HeiseIE._VALID_URL