

# Generated at 2022-06-14 16:24:09.279151
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    try:
        HeiseIE("")
    except Exception as e:
        print("Failed to instantiate HeiseIE: %s %s" % (type(e), e))
        assert False

# Generated at 2022-06-14 16:24:10.074334
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()

# Generated at 2022-06-14 16:24:12.762986
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert(ie.ie_key() == 'Heise')
    assert(ie.ie_key() == 'Heise')

# Generated at 2022-06-14 16:24:22.977841
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE.ie_key() == 'heise'

    for test_case in HeiseIE._TESTS:
        info_dict = test_case.get('info_dict')

        # Test constructor by passing a URL
        heise_IE = HeiseIE(test_case['url'])
        assert heise_IE.ie_key() == 'heise'
        assert heise_IE.video_id == info_dict['id']

        # Test constructor by passing an info dict
        heise_IE = HeiseIE(info_dict)
        assert heise_IE.ie_key() == 'heise'
        assert heise_IE.video_id == info_dict['id']

# Generated at 2022-06-14 16:24:33.186131
# Unit test for constructor of class HeiseIE

# Generated at 2022-06-14 16:24:35.085327
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie

# Generated at 2022-06-14 16:24:36.519683
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # To check that the constructor of class doesn't throw an exception
    HeiseIE({})

# Generated at 2022-06-14 16:24:46.875490
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    try:
        assert HeiseIE
    except NameError:
        assert False, 'HeiseIE nicht definiert'
    try:
        assert KalturaIE
    except NameError:
        assert False, 'KalturaIE nicht definiert'
    try:
        assert YoutubeIE
    except NameError:
        assert False, 'YoutubeIE nicht definiert'
    try:
        assert determine_ext
    except NameError:
        assert False, 'determine_ext nicht definiert'
    try:
        assert int_or_none
    except NameError:
        assert False, 'int_or_none nicht definiert'
    try:
        assert NO_DEFAULT
    except NameError:
        assert False, 'NO_DEFAULT nicht definiert'

# Generated at 2022-06-14 16:24:48.875859
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    t = HeiseIE()
    assert t._TESTS
    assert t._VALID_URL
    assert t._download_webpage

# Generated at 2022-06-14 16:24:54.339186
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    from . import Extractor
    from .youtube import YoutubePlaylistIE
    from .common import InfoExtractor
    from .youtube import YoutubePlaylistIE


    ##################################################################
    # Tests for the YoutubePlaylistIE
    ##################################################################

    # Test for Extractor construction
    def test_Extractor_constructor():
        Extractor()
        InfoExtractor()
        YoutubePlaylistIE()

# Generated at 2022-06-14 16:25:03.562764
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()

# Generated at 2022-06-14 16:25:05.601325
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.ie_key() == 'Heise'

# Generated at 2022-06-14 16:25:06.090508
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE({})

# Generated at 2022-06-14 16:25:11.245003
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert ie._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:25:12.215592
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE() is not None

# Generated at 2022-06-14 16:25:13.778226
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    info_extractor = HeiseIE()
    assert info_extractor.ie_key() == 'heise'

# Generated at 2022-06-14 16:25:15.535632
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Create instance of class HeiseIE
    assert HeiseIE

# Generated at 2022-06-14 16:25:17.402400
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heiseIE = HeiseIE()
    assert heiseIE is not None


# Generated at 2022-06-14 16:25:30.255743
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # We test all permutations and combinations of the if and elif statements
    # in the _real_extract method of HeiseIE
    # First we test the if case
    url = ('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-'
           'Tastaturen-Peilsender-Smartphone-2404147.html')
    ie = HeiseIE(fetch_url_test=lambda x: '<xml></xml>',
                 fetch_html_test=lambda x: '<html></html>')

# Generated at 2022-06-14 16:25:31.018837
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()

# Generated at 2022-06-14 16:25:48.111507
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    test = HeiseIE()

# Generated at 2022-06-14 16:25:54.465890
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    """
    InfoExtractor unit test for ct-Heise
    """
    heise = HeiseIE()
    heise.extract('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    heise.extract('https://www.heise.de/video/artikel/c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')

# Generated at 2022-06-14 16:25:58.860381
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie_tester = InfoExtractor('HeiseIE')
    assert ie_tester.test_test('HeiseIE') == False # No test link
    assert ie_tester.test_test('https://www.heise.de/ct/artikel/c-t-uplink-20-8-Staubsaugerroboter-Xiaomi-Vacuum-2-AR-Brille-Meta-2-und-Android-rooten-3959893.html') == True # Test link
    assert ie_tester.test_test('https://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html') == False # Test link



# Generated at 2022-06-14 16:26:02.764546
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    url = "http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html"
    ie = HeiseIE()
    obj = ie.extract(url)
    assert obj != None

# Generated at 2022-06-14 16:26:04.733382
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    inst = HeiseIE(downloader=None)
    assert inst is not None

# Generated at 2022-06-14 16:26:15.796716
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    module = 'heise.heiseIE'
    klass = 'HeiseIE'
    url = 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'

# Generated at 2022-06-14 16:26:16.641165
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    h = HeiseIE()

# Generated at 2022-06-14 16:26:18.498920
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Test HeiseIE.__init__()
    instance = HeiseIE()
    assert isinstance(instance, HeiseIE)

# Generated at 2022-06-14 16:26:20.932586
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise_info_extractor = HeiseIE(None)
    assert isinstance(heise_info_extractor, InfoExtractor)

# Generated at 2022-06-14 16:26:25.685998
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    url = 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
    ie = HeiseIE()
    ie.download(url)

# Generated at 2022-06-14 16:27:04.717326
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise = HeiseIE()
    # Unit test for _VALID_URL
    test_1 = heise._VALID_URL.match('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert test_1.group('id') == '2404147'
    # Unit test for _extract_urls()
    test_2 = heise._html_extractor({'ie_key': 'Heise'})('<div id="video-player" data-youtube-id="AsVezgG0l0Y" class="videoplayer-youtube"></div>')

# Generated at 2022-06-14 16:27:06.501805
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
   heise = HeiseIE()
   assert isinstance(heise, InfoExtractor)

# Generated at 2022-06-14 16:27:07.120768
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()

# Generated at 2022-06-14 16:27:16.424810
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.suitable('https://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html')
    assert not ie.suitable('https://www.heise.de/kultur/meldung/Das-c-t-Forum-Diskussionen-ueber-gesellschaftliche-Themen-3700763.html')
    assert ie._VALID_URL == ie.VALID_URL
    assert ie._TESTS == ie.TESTS
    assert ie._download_webpage == ie._real_extract

# Generated at 2022-06-14 16:27:20.879878
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.ie_key() == 'heise'
    assert ie.ie_key() in globals()['InfoExtractor']._WORKING_IE_KEY

if __name__ == '__main__':
    test_HeiseIE()

# Generated at 2022-06-14 16:27:30.726872
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    inst = HeiseIE()
    assert inst._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:27:42.129625
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Set default value of option
    opts = {'extract_flat': True}
    # Set the url of class to be tested
    url = 'https://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html'
    
    # Create an instance of class to be tested
    ie = HeiseIE(opts)
    # Test the constructor of class by using function _download_webpage defined in YoutubeIE
    webpage = ie._download_webpage(url, '3700244')

    # Assert the result of the function _download_webpage
    assert 'nachgehakt: Wie sichert das c\'t-Tool Restric\'tor Windows 10 ab?'

# Generated at 2022-06-14 16:27:48.530671
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Test HeiseIE constructor
    testIE = HeiseIE('https://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html')
    assert testIE._VALID_URL == 'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:27:48.974784
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    pass


# Generated at 2022-06-14 16:27:50.164125
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert isinstance(ie, HeiseIE)

# Generated at 2022-06-14 16:29:21.626833
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE(None)._VALID_URL == HeiseIE._VALID_URL

# Generated at 2022-06-14 16:29:25.585047
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Note that this only tests the constructor of the class
    # by calling the classmethod responsible for creating it,
    # and not the actual extractor code.
    ie = HeiseIE.ie_key()
    # Check if the expected class is returned
    assert ie.__name__ == 'HeiseIE'
    assert issubclass(ie, InfoExtractor)

# Generated at 2022-06-14 16:29:32.000491
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    e = HeiseIE()
    e.suitable('https://www.heise.de/ct/artikel/c-t-uplink-20-8-Staubsaugerroboter-Xiaomi-Vacuum-2-AR-Brille-Meta-2-und-Android-rooten-3959893.html')

# Generated at 2022-06-14 16:29:35.319973
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Test if the constructor throws no exceptions
    TestHeiseIE = HeiseIE("http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html")
    assert TestHeiseIE

# Generated at 2022-06-14 16:29:40.391059
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    b = HeiseIE()
    b._real_extract(
        'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')

# Generated at 2022-06-14 16:29:41.926169
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()

# Generated at 2022-06-14 16:29:43.590860
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.ie_key() == 'heise'
    assert ie.ie_name() == 'heise.de'

# Generated at 2022-06-14 16:29:44.444811
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE() # noqa

# Generated at 2022-06-14 16:29:53.949518
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    """
        Method 'test_HeiseIE' tests the constructor of class 'HeiseIE'
    """

    init_test = HeiseIE(InfoExtractor())

    assert init_test._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:30:04.289389
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.suitable('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert ie.suitable('https://www.heise.de/ct/artikel/c-t-uplink-20-8-Staubsaugerroboter-Xiaomi-Vacuum-2-AR-Brille-Meta-2-und-Android-rooten-3959893.html')
    assert ie.suitable('http://www.heise.de/ct/artikel/c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2403911.html')


# Generated at 2022-06-14 16:33:33.440562
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    ie.suitable('http://www.heise.de/ct/ausgabe/2018-2-Service-3881756.html')
    assert 'constructor' in ie

# Generated at 2022-06-14 16:33:34.210854
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert isinstance(HeiseIE, InfoExtractor)

# Generated at 2022-06-14 16:33:36.077392
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    try:
        HeiseIE()
    except:
        assert False


# Generated at 2022-06-14 16:33:37.792477
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE()._VALID_URL == HeiseIE._VALID_URL

# Generated at 2022-06-14 16:33:38.967195
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert type(HeiseIE) == type(InfoExtractor)

# Generated at 2022-06-14 16:33:40.946767
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()

# Generated at 2022-06-14 16:33:50.553741
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise = HeiseIE()
    assert heise._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:33:51.115936
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()

# Generated at 2022-06-14 16:33:52.710384
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE("heise.de")

    assert(ie.name == "heise.de")


# Generated at 2022-06-14 16:33:53.624557
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    info_extractor = HeiseIE()
    assert info_extractor is not None