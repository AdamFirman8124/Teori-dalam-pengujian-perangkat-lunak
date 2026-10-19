

# Generated at 2022-06-14 16:24:04.860444
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
  """Test the HeiseIE constructor."""
  # None of these are in the test set, so we just check the constructor.
  i = HeiseIE()
  i.suite()

# Generated at 2022-06-14 16:24:06.012886
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE(InfoExtractor())

# Generated at 2022-06-14 16:24:18.611851
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    video = HeiseIE()._real_extract(url = 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    title = video.get('title')
    assert title == "Podcast: c't uplink 3.3 – Owncloud / Tastaturen / Peilsender Smartphone"
    timestamp = video.get('timestamp')
    assert timestamp == 1512734959
    formats = video.get('formats')

# Generated at 2022-06-14 16:24:20.818715
# Unit test for constructor of class HeiseIE
def test_HeiseIE():

    url = "http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html"

    # Unit test without youtube_ie
    ie = HeiseIE()
    ie.extract(url)

    # Unit test with youtube_ie
    ie = HeiseIE(YoutubeIE)
    ie.extract(url)

# Generated at 2022-06-14 16:24:26.243035
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    url = 'https://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html'
    ie = HeiseIE()
    ie._real_extract(url)

# Generated at 2022-06-14 16:24:30.030393
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ff = HeiseIE()
    ff._match_id('https://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html')

# Generated at 2022-06-14 16:24:37.507492
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Test the url is valid or not
    assert HeiseIE._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'
    # Test the main page of the website
    assert HeiseIE._TESTS[0]['url'] == 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
    # Test that the webpage is available for downloading
    webpage_test = HeiseIE._download_webpage(HeiseIE._TESTS[0]['url'], HeiseIE._TESTS[0]['info_dict'])
   

# Generated at 2022-06-14 16:24:38.493667
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    instance = HeiseIE()
    instance.suitable("https://heise.de")



# Generated at 2022-06-14 16:24:39.935154
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Test constructor calls the InfoExtractor constructor
    assert HeiseIE() is not None

# Generated at 2022-06-14 16:24:48.262727
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.IE_NAME == "heise"
    assert ie._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == None
    assert ie.IE_KEY == 'Heise'
    assert ie.webpage == None
    assert ie.extract == None
    assert ie.HEISE_BASE_URL == r'https?://www\.heise\.de/(?:[^/]+/)+[^/]+'
    assert ie.webpage_url == None

# Generated at 2022-06-14 16:25:10.606313
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE().extract('https://www.heise.de/ct/artikel/c-t-uplink-20-8-Staubsaugerroboter-Xiaomi-Vacuum-2-AR-Brille-Meta-2-und-Android-rooten-3959893.html')

# Generated at 2022-06-14 16:25:12.163141
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    class_ = globals()['HeiseIE']
    instance = class_()
    assert instance.IE_NAME == 'heise'

# Generated at 2022-06-14 16:25:15.829194
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Test case 1: Successful instantiation of class HeiseIE.
    heise = HeiseIE()
    # Test case 2: Successful type check of instance of class HeiseIE.
    assert isinstance(heise, HeiseIE)
    # Test case 3: Successful instance check of instance of class HeiseIE.
    assert isinstance(heise, InfoExtractor)

# Generated at 2022-06-14 16:25:28.572630
# Unit test for constructor of class HeiseIE

# Generated at 2022-06-14 16:25:36.190503
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heiseie = HeiseIE()
    heiseie.extract('http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html')
    heiseie.extract('https://www.heise.de/ct/artikel/c-t-uplink-20-8-Staubsaugerroboter-Xiaomi-Vacuum-2-AR-Brille-Meta-2-und-Android-rooten-3959893.html')

# Test for all methods of class HeiseIE

# Generated at 2022-06-14 16:25:46.425147
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE("https://www.heise.de/ct/artikel/c-t-uplink-20-8-Staubsaugerroboter-Xiaomi-Vacuum-2-AR-Brille-Meta-2-und-Android-rooten-3959893.html")
    assert ie.url == "https://www.heise.de/ct/artikel/c-t-uplink-20-8-Staubsaugerroboter-Xiaomi-Vacuum-2-AR-Brille-Meta-2-und-Android-rooten-3959893.html"


# Generated at 2022-06-14 16:25:49.921807
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    ie.extract('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')

# Generated at 2022-06-14 16:25:53.244689
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    from .test_dm_common import TestDmCommon
    from .test_youtube import TestYoutube

    TestDmCommon.test_constructor(HeiseIE)


# Generated at 2022-06-14 16:25:54.490446
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie

# Generated at 2022-06-14 16:25:58.501944
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert ie.ie_key() == 'Heise'

# Generated at 2022-06-14 16:26:36.231136
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    x = HeiseIE()
    assert(x is not None)

# Generated at 2022-06-14 16:26:41.542517
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    url = 'https://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
    obj = HeiseIE(url)
    assert obj._VALID_URL == HeiseIE._VALID_URL
    assert obj._TESTS == HeiseIE._TESTS

# Generated at 2022-06-14 16:26:42.710928
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    example = HeiseIE()
    assert example

# Generated at 2022-06-14 16:26:48.436348
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    print("test for Heise")
    url = 'http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html'
    # instanciate HeiseIE
    HeiseIE(url)

# Generated at 2022-06-14 16:26:52.365459
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ydl = HeiseIE()
    for case in ydl.cases:
        print('Testing {url}'.format(url=case['url']))
        assert case['info_dict'] == ydl.extract_info(case['url'], download=False)

# Generated at 2022-06-14 16:26:55.158069
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE(HeiseIE, None).video_id == '1_kkrq94sm'

# Generated at 2022-06-14 16:26:55.732792
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()

# Generated at 2022-06-14 16:26:58.124248
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Constructor of class HeiseIE
    instance = HeiseIE()
    assert isinstance(instance, HeiseIE)


if __name__ == '__main__':
    test_HeiseIE()

# Generated at 2022-06-14 16:27:01.870935
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    """
    This test checks that HeiseIE constructor is correct
    """
    url='https://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html'
    HeiseIE(url)

# Generated at 2022-06-14 16:27:03.934788
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE().ie_key() == 'heise'

# Generated at 2022-06-14 16:28:38.417231
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert str(ie) == '<HeiseIE valid:%r>' % HeiseIE._VALID_URL.pattern

# Generated at 2022-06-14 16:28:39.998497
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heiseIE = HeiseIE()
    print(heiseIE)

# Generated at 2022-06-14 16:28:42.037918
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE(None)
    assert ie._VALID_URL == HeiseIE._VALID_URL

# Generated at 2022-06-14 16:28:44.335449
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    from . import gen_extractors_test
    gen_extractors_test.test_info_extractor_constructor_for(HeiseIE)

# Generated at 2022-06-14 16:28:54.092386
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE(HeiseIE.ie_key())
    initial_result = ie.extract('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert not isinstance(initial_result, Exception)
    assert isinstance(initial_result, dict)
    assert len(initial_result) == 9
    assert initial_result['id'] == '1_kkrq94sm'
    assert initial_result['ext'] == 'mp4'
    assert initial_result['title'] == "Podcast: c't uplink 3.3 – Owncloud / Tastaturen / Peilsender Smartphone"
    assert initial_result['timestamp'] == 1512734959
   

# Generated at 2022-06-14 16:29:01.401466
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    #Test for constructor of class HeiseIE
    #Test for assertRaises of NameError
    try:
        raise NameError('Hi There')
    except NameError:
        print('An expected NameError')
    #Test for assertRaises of TypeError
    try:
        print(1+'hello')
    except TypeError:
        print('An expected TypeError')
    #Test for assertRaises of SyntaxError
    try:
        eval('1+')
    except SyntaxError:
        print('An expected SyntaxError')
    #Test for assertRaises of ValueError
    try:
        print(int('a'))
    except ValueError:
        print('An expected ValueError')

# Generated at 2022-06-14 16:29:08.631312
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    constructor = HeiseIE.__new__(HeiseIE)
    instance = constructor("http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html")
    assert instance._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:29:12.789173
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE(InfoExtractor())
    ie.extract('https://www.heise.de/ct/artikel/c-t-uplink-20-8-Staubsaugerroboter-Xiaomi-Vacuum-2-AR-Brille-Meta-2-und-Android-rooten-3959893.html')

# Generated at 2022-06-14 16:29:13.991715
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise = HeiseIE()

# Generated at 2022-06-14 16:29:15.229806
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    _ie = HeiseIE()
    print(_ie.SUFFIX)

# Generated at 2022-06-14 16:31:03.147282
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    try:
        HeiseIE("")
    except:
        pass # OK
    return

# Generated at 2022-06-14 16:31:07.387292
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    url = 'http://www.heise.de/ct/artikel/c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2403911.html'
    HeiseIE()._real_extract(url)

# Generated at 2022-06-14 16:31:16.324278
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie=HeiseIE()
    test_url="http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html"
    # youtube expected id:
    yt_id="6kmWbXleKW4"
    # kaltura expected id:
    kaltura_id="1_kkrq94sm"
    assert yt_id not in ie._real_extract(test_url)['title']
    assert kaltura_id in ie._real_extract(test_url)['title']

# Generated at 2022-06-14 16:31:18.066402
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Smoke tests:
    assert HeiseIE._VALID_URL
    assert HeiseIE._TESTS

# Generated at 2022-06-14 16:31:23.110252
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    h = HeiseIE()
    assert h.suitable('https://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert not h.suitable('http://www.heise.de/ct/ausgabe/2016-12-Spiele-3214137.html')

# Generated at 2022-06-14 16:31:28.754913
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert ie.video_id == '1_kkrq94sm'
    assert ie.name == 'heise'
    assert ie.title == "Podcast: c't uplink 3.3 – Owncloud / Tastaturen / Peilsender Smartphone"
    assert ie.timestamp == 1512734959
    assert ie.thumbnail == 'http://cdnapisec.kaltura.com/p/2238431/thumbnail/entry_id/1_kkrq94sm/width/640/quality/100'

# Generated at 2022-06-14 16:31:38.880729
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.ie_key() == 'heise'
    assert ie.LOGIN_URL == 'https://www.heise.de/forum/login.php'
    assert ie.CSRF_TOKEN_RE == 'csrf_token\s*=\s*"([^"]+)"'
    assert ie.LOGIN_URL == 'https://www.heise.de/forum/login.php'
    assert ie.SUBMITPAYWALL_URL == 'https://www.heise.de/user/submitpaywall.php'
    assert ie._LOGIN_SIZE == (375, 512)
    assert ie._LOGIN_SUCCESS_STATUS is None
    assert ie.MAX_COMMENT_PAGE == 0
    assert ie.COMMENTS_START_RE == ''
   

# Generated at 2022-06-14 16:31:41.763443
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.suitable('https://www.heise.de/ct/artikel/c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2403911.html')

# Generated at 2022-06-14 16:31:45.394014
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE('https://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html')
    assert ie is not None

# Generated at 2022-06-14 16:31:50.095449
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Create a dummy test case
    class TestCase:
        def __init__(self, name):
            self.name = name

    # Create an instance of HeiseIE and call it's _real_extract method
    heise = HeiseIE()
    heise._real_extract(TestCase('test'), 'https://heise.de/test.html')