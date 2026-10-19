

# Generated at 2022-06-14 16:24:13.034621
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert ie.get_title() == 'Podcast: c\'t uplink 3.3 – Owncloud / Tastaturen / Peilsender Smartphone'
    assert ie.get_description() == 'md5:c934cbfb326c669c2bcabcbe3d3fcd20'

# Generated at 2022-06-14 16:24:14.720881
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.ie_key() == 'heise'

# Generated at 2022-06-14 16:24:26.599038
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE(None)
    assert re.match(ie._VALID_URL, "http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html", re.VERBOSE) is not None
    url = "http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html"
    video_id = "1_kkrq94sm"
    assert ie._match_id(url) == video_id
    webpage = ie._download_webpage(url, video_id)
    assert webpage

# Generated at 2022-06-14 16:24:27.593197
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    extractor = HeiseIE(None)
    assert isinstance(extractor, InfoExtractor)

# Generated at 2022-06-14 16:24:28.185342
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()

# Generated at 2022-06-14 16:24:33.500504
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE("http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html")
    assert ie.ie_key() == 'Heise'
    assert ie.ie_name() == 'Heise'
    assert ie.description == """Heise Video, the German IT news website's video section."""
    assert ie.working

# Generated at 2022-06-14 16:24:35.237354
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()

# Generated at 2022-06-14 16:24:39.045975
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise_ie = HeiseIE()

    assert_equals(heise_ie.ie_key(), 'Heise')
    assert_equals(heise_ie.server_url, 'www.heise.de')


# Generated at 2022-06-14 16:24:48.456127
# Unit test for constructor of class HeiseIE

# Generated at 2022-06-14 16:24:54.868296
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE("www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html")
    assert ie._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'
    assert ie.__name__ == 'Heise'

# Generated at 2022-06-14 16:25:24.178506
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    url = "http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html"
    # The test will be removed if there is a test_kaltura.
    test_dict = {
        'timestamp': int,
        'description': 'md5:c934cbfb326c669c2bcabcbe3d3fcd20',
        'ext': 'mp4',
        'title': "Podcast: c't uplink 3.3 – Owncloud / Tastaturen / Peilsender Smartphone",
        'id': '1_kkrq94sm',
    }
    instance = HeiseIE()._real_extract(url)

# Generated at 2022-06-14 16:25:28.082417
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Test trigger (verify title of the video)
    heise_video_url = "https://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html"
    expected_title = "Podcast: c't uplink 3.3 – Owncloud / Tastaturen / Peilsender Smartphone"
    extractor = HeiseIE.from_url(heise_video_url)
    assert extractor is not None
    assert extractor.title == expected_title
    assert expected_title in extractor._html_search_meta('title', extractor._download_webpage(heise_video_url, extractor.ie_key()))

# Generated at 2022-06-14 16:25:33.527328
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    youtube_url = 'http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html'
    heise = HeiseIE(youtube_url)
    assert isinstance(heise, InfoExtractor)
    assert heise.ie_key() == 'heise'

# Generated at 2022-06-14 16:25:40.028973
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heiseie=HeiseIE()
    assert heiseie.ie_key() == 'Heise'
    assert heiseie.extract('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    
    heiseie=HeiseIE()
    assert heiseie.ie_key() == 'Heise'
    assert heiseie.extract('http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html')
    
    heiseie=HeiseIE()

# Generated at 2022-06-14 16:25:49.973432
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Test that HeiseIE.__init__ is working properly
    assert(HeiseIE.__init__ is not InfoExtractor.__init__)
    # Test that the class is instantiable
    instance = HeiseIE(None)
    # Test that it is an instance of InfoExtractor
    from youtube_dl.extractor.common import InfoExtractor
    assert(isinstance(instance, InfoExtractor))
    # Test that it inherits from YoutubeIE
    from youtube_dl.extractor.youtube import YoutubeIE
    assert(issubclass(HeiseIE, YoutubeIE))
    # Test that it belongs to the list of extractors
    assert(instance.ie_key() in globals()['InfoExtractors'])

# Generated at 2022-06-14 16:25:54.348094
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise = HeiseIE()
    assert heise._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:25:55.684020
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE.ie_key() == 'Heise'



# Generated at 2022-06-14 16:25:56.712774
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise = HeiseIE()

# Generated at 2022-06-14 16:25:57.721356
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()  # just for calling its constructor

# Generated at 2022-06-14 16:25:59.702202
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    unit = HeiseIE()
    # verify that this is the class the test should use
    assert isinstance(unit, HeiseIE)

# Generated at 2022-06-14 16:26:34.790860
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    mver = HeiseIE()
    assert mver

# Generated at 2022-06-14 16:26:44.563187
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heiseie = HeiseIE()
    heiseie.set_url('http://www.heise.de/newsticker/meldung/c-t-uplink-Owncloud-Tastaturen-Peilsender-Smartphone-2404251.html?wt_mc=rss.ho.beitrag.atom')
    heiseie.set_url('http://www.heise.de/ct/artikel/c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2403911.html')
    heiseie.set_url('http://www.heise.de/ct/ausgabe/2016-12-Spiele-3214137.html')

# Generated at 2022-06-14 16:26:54.797190
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert ie.__class__.__name__ == 'HeiseIE'
    assert ie.ie_key() == 'Heise'
    assert ie.video_id == '1_kkrq94sm'
    assert ie.url == 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
    assert ie.name == 'Heise'

# Generated at 2022-06-14 16:26:57.092262
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.ie_key() == 'heise'
    assert ie.ie_name() == 'Heise'


test_HeiseIE()

# Generated at 2022-06-14 16:27:04.503180
# Unit test for constructor of class HeiseIE

# Generated at 2022-06-14 16:27:15.453928
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    class_constructor = getattr(HeiseIE, '_initialize_class')
    class_constructor(HeiseIE)
    assert HeiseIE._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'
    assert HeiseIE.__name__ == 'HeiseIE'

# Generated at 2022-06-14 16:27:17.867863
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    from nose.tools import assert_equal  # pylint: disable=import-error,no-name-in-module

    instance = HeiseIE(None)
    assert_equal(instance._VALID_URL, HeiseIE._VALID_URL)  # pylint: disable=protected-access,no-member

# Generated at 2022-06-14 16:27:18.990863
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    inc = HeiseIE()
    inc.suite()

# Generated at 2022-06-14 16:27:24.567766
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE("http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html")
    name = ie.name
# Unit test end


# Generated at 2022-06-14 16:27:25.790112
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise = HeiseIE()
    assert heise




# Generated at 2022-06-14 16:28:59.999294
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    e = HeiseIE()
    assert e.IE_NAME == 'heise'
    assert e.IE_DESC == 'heise online'
    assert e.valid_url('https://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert e.valid_url('https://www.heise.de/ct/artikel/Die-Algorithmen-von-Amazon-3780279.html')
    assert e.valid_url('https://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html')


# Generated at 2022-06-14 16:29:09.670329
# Unit test for constructor of class HeiseIE

# Generated at 2022-06-14 16:29:10.860109
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    obj = HeiseIE()
    assert obj is not None

# Generated at 2022-06-14 16:29:12.650162
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    """
    Unit test for constructor of class HeiseIE.
    """
    f = HeiseIE()
    assert f != None


# Generated at 2022-06-14 16:29:13.229855
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE()

# Generated at 2022-06-14 16:29:16.777274
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    class_ = HeiseIE
    assert class_ is not None
    instance = class_()
    assert instance is not None
    # class_._super_class
    assert issubclass(class_, InfoExtractor)
    # class_._super_class._super_class
    assert issubclass(class_, YoutubeIE)

# Generated at 2022-06-14 16:29:22.930643
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE("https://www.heise.de/ct/artikel/c-t-uplink-20-8-Staubsaugerroboter-Xiaomi-Vacuum-2-AR-Brille-Meta-2-und-Android-rooten-3959893.html")

# Generated at 2022-06-14 16:29:24.260184
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise = HeiseIE()
    assert heise is not None

# Generated at 2022-06-14 16:29:27.507905
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE("http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html")

# Generated at 2022-06-14 16:29:37.570127
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'
    assert ie._TESTS[0]['url'] == 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'

# Generated at 2022-06-14 16:33:08.174140
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Tests for media.ccc.de
    instance = HeiseIE(None)
    assert instance._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'


test_HeiseIE()

# Generated at 2022-06-14 16:33:10.745099
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    infoExtractor = HeiseIE({"youtube_ie": YouTubeIE()})
    assert infoExtractor.suitable("http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html")

# Generated at 2022-06-14 16:33:21.942840
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:33:26.618050
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    """
    Unit test for constructor of class HeiseIE
    """
    heise = HeiseIE()

    assert heise._VALID_URL == HeiseIE._VALID_URL
    assert heise._TESTS == HeiseIE._TESTS

    print(heise.IE_DESC)

    assert heise.IE_NAME == 'Heise'
    assert heise.IE_DESC == 'Heise Online Videos (heise.de)'

# Generated at 2022-06-14 16:33:29.368376
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE.ie_key() == 'heise'
    assert HeiseIE.ie_key() == HeiseIE.ie_key() # test using cache
    assert HeiseIE.ie_key() == HeiseIE.ie_key() # test using cache again

# Generated at 2022-06-14 16:33:38.651633
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    """
    Test if constructor of HeiseIE class do its job.
    """
    input_values = ['https://www.heise.de/ct/artikel/c-t-uplink-20-8-Staubsaugerroboter-Xiaomi-Vacuum-2-AR-Brille-Meta-2-und-Android-rooten-3959893.html']

# Generated at 2022-06-14 16:33:49.495024
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie._VALID_URL.match('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert ie._VALID_URL.match('http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html')
    assert ie._VALID_URL.match('https://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html')
   

# Generated at 2022-06-14 16:33:55.778989
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()  # No error should occur during initialization

    obj = HeiseIE(create_default_opener())  # No error should occur

    url = "http://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html"
    ie = HeiseIE()
    assert ie.suitable(url)
    assert ie.ie_key() == "Heise"

    url = "http://golem.de/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html"
    ie = HeiseIE()