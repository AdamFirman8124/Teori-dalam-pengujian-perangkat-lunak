

# Generated at 2022-06-14 16:24:16.602734
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # To test HeiseIE, it is used a file saved from www.heise.de/video
    fp = open("test_files/test_heise.html", "r")
    webpage = fp.read()
    fp.close()
    article = HeiseIE._build_entry(webpage)
    # Should have title, description and link
    assert article["title"] == "Von Gefahren bei Windows 10 und eigenen Servern"

# Generated at 2022-06-14 16:24:19.818841
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    i = HeiseIE()
    assert i.ie_key() == 'heise'
    assert i.ie_name() == 'heise'
    assert i.ie() == 'heise'
    

# Generated at 2022-06-14 16:24:20.857387
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    h = HeiseIE()

# Generated at 2022-06-14 16:24:23.311781
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = InfoExtractor("heise", "heise.de")
    assert isinstance(ie, HeiseIE)

# Generated at 2022-06-14 16:24:27.177783
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heiseie = HeiseIE()
    assert heiseie._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:24:38.775073
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE('https://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html')
    assert ie.SUFFIX == '.html'
    assert ie.FAKE_URL == 'https://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html'

# Generated at 2022-06-14 16:24:42.583978
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    from .youtube import YoutubeIE
    from .kaltura import KalturaIE
    heise = HeiseIE(YoutubeIE(), KalturaIE())
    assert heise._YOUTUBE_IE == YoutubeIE
    assert heise._KALTURA_IE == KalturaIE

# Generated at 2022-06-14 16:24:46.451839
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    x = HeiseIE('https://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html')
    assert x.ie_key() == 'Heise'
    assert x.info_dict['id'] == '1_ntrmio2s'
    assert x.info_dict['ext'] == 'mp4'
    assert x.info_dict['description'] == 'md5:47e8ffb6c46d85c92c310a512d6db271'
    assert x.info_dict['title'] == "nachgehakt: Wie sichert das c't-Tool Restric'tor Windows 10 ab?"

# Generated at 2022-06-14 16:24:47.764730
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    """Unit test for class HeiseIE."""
    return HeiseIE(InfoExtractor())

# Generated at 2022-06-14 16:24:50.217553
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    '''
    Call the constructor of class HeiseIE.
    '''
    heiseIE = HeiseIE()
    return heiseIE

# Generated at 2022-06-14 16:25:09.872237
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE.IE_NAME == "heise"


# Generated at 2022-06-14 16:25:10.519880
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()

# Generated at 2022-06-14 16:25:14.193790
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE("http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html")
    assert type(ie) == HeiseIE
    

# Generated at 2022-06-14 16:25:26.999288
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Check if HeiseIE can be constructed correctly
    ie = HeiseIE({'extractor': 'heise'})
    assert ie._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:25:32.256367
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    """Unit test for constructor of class HeiseIE"""
    url = 'http://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html'
    ie = HeiseIE()
    assert isinstance(ie, HeiseIE)

# Generated at 2022-06-14 16:25:35.514668
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    ie.extract_url('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')

# Generated at 2022-06-14 16:25:48.004070
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    def test_heise_ie_init():
        i = HeiseIE("http://www.heise.de/ct/artikel/c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2403911.html")
        assert i.url == "http://www.heise.de/ct/artikel/c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2403911.html"
        assert i.video_id == "2403911"
        assert i.title == "c't uplink 3.3 – Owncloud / Tastaturen / Peilsender Smartphone"

# Generated at 2022-06-14 16:25:51.567131
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    ie.extract('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')

# Generated at 2022-06-14 16:25:54.632713
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    from . import gen_extractors_test
    gen_extractors_test.gen_class_test(HeiseIE)


# Generated at 2022-06-14 16:25:56.757245
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert isinstance(ie, InfoExtractor)
    assert hasattr(ie, '_VALID_URL')

# Generated at 2022-06-14 16:26:18.241534
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    x = HeiseIE()
    assert isinstance(x, __builtins__.type(HeiseIE)) == True

# Generated at 2022-06-14 16:26:24.439137
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()

    assert ie.suitable('https://www.heise.de/ct/artikel/c-t-uplink-20-8-Staubsaugerroboter-Xiaomi-Vacuum-2-AR-Brille-Meta-2-und-Android-rooten-3959893.html') == True, "URL is not marked as suitable."



# Generated at 2022-06-14 16:26:29.583540
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.suitable('https://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert ie.suitable('http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html')
    assert ie.suitable('https://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html')

# Generated at 2022-06-14 16:26:32.398470
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise = HeiseIE()

# Generated at 2022-06-14 16:26:33.886468
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert isinstance(ie, HeiseIE)

# Generated at 2022-06-14 16:26:37.437368
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heiseIE = HeiseIE()
    heiseIE.extract("https://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html")

# Generated at 2022-06-14 16:26:49.122433
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    hie = HeiseIE('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html') # noqa
    assert hie
    assert hie.IE_NAME == 'heise'
    assert hie._VALID_URL == 'https?://(?:www\\.)?heise\\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\\.html' # noqa

# Generated at 2022-06-14 16:26:50.373549
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert isinstance(ie, HeiseIE)

# Generated at 2022-06-14 16:26:58.503951
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Check if HeiseIE could be instantiated
    HeiseIE(None)
    # Check if HeiseIE can handle the expected URL
    HeiseIE(None).suitable('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    # Check if HeiseIE can handle the unexpected URL
    HeiseIE(None).suitable('http://www.bild.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html') == False


# Generated at 2022-06-14 16:26:59.825749
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    IE = HeiseIE()

    assert(IE.ie_key() == 'heise')
    assert(IE.ie_desc() == 'heise video')

# Generated at 2022-06-14 16:27:50.786897
# Unit test for constructor of class HeiseIE

# Generated at 2022-06-14 16:27:55.475557
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.suitable('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert ie.suitable('https://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html')
    assert not ie.suitable('http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html')

# Generated at 2022-06-14 16:28:07.563115
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    u = HeiseIE()
    assert u._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:28:08.489519
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()

# Generated at 2022-06-14 16:28:09.746056
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()

# Generated at 2022-06-14 16:28:10.692024
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise = HeiseIE()

# Generated at 2022-06-14 16:28:11.608379
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    isinstance(HeiseIE(), InfoExtractor)

# Generated at 2022-06-14 16:28:13.120090
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.ie_key() == "Heise"

# Generated at 2022-06-14 16:28:13.772908
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE()

# Generated at 2022-06-14 16:28:18.383127
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    result = HeiseIE()._extract_url('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert result['url'] == '1_kkrq94sm'

# Generated at 2022-06-14 16:30:02.610225
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert ie.NAME == 'heise'
    assert ie.VALID_URL == 'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:30:03.757942
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Tests that the HeiseIE object can be initialized without issues
    HeiseIE()

# Generated at 2022-06-14 16:30:05.784122
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Create instance of HeiseIE
    heise_ie = HeiseIE()
    # Check if HeiseIE implements the _real_extract()
    assert hasattr(heise_ie, '_real_extract')

# Generated at 2022-06-14 16:30:08.327990
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    config = {'skip_download': True}
    # Test that the heiseie instance is created succesfully
    assert ie.suitable(config)

# Generated at 2022-06-14 16:30:08.892683
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()

# Generated at 2022-06-14 16:30:10.899246
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE();
    assert ie.ie_key() in ie.generate_ie_instance()

# Generated at 2022-06-14 16:30:16.767360
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    test_url = 'http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html'
    heise = HeiseIE()
    video = heise._real_extract(test_url)
    assert video['title'] == 'NEU IM SEPTEMBER | Netflix'

# Generated at 2022-06-14 16:30:22.447724
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    url = 'https://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html'
    id = ie._match_id(url)
    assert ie._VALID_URL.match(url)
    assert id == '3700244'

# Generated at 2022-06-14 16:30:25.783742
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    from .test_kaltura import KalturaIE_test
    from .test_youtube import YoutubeIE_test

    # Test constructor for KalturaIE
    KalturaIE_test(HeiseIE)

    # Test constructor for YoutubeIE
    YoutubeIE_test(HeiseIE)

    # Check for new HeiseIE
    instance = HeiseIE()

# Generated at 2022-06-14 16:30:26.921570
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie is not None