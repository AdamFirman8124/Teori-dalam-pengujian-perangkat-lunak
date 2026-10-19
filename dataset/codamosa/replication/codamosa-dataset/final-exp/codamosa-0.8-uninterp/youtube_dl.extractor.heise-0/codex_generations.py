

# Generated at 2022-06-14 16:24:03.593646
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()

# Generated at 2022-06-14 16:24:05.463337
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE(InfoExtractor())
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, YoutubeIE)

# Generated at 2022-06-14 16:24:18.196601
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise = HeiseIE()
    heise._download_webpage = lambda *args: "foo"
    heise._search_regex = lambda *args: "bar"
    heise._html_search_meta = lambda *args: "baz"
    heise._html_search_regex = lambda *args: "biz"
    assert heise.test(URL, True) == True
    assert heise.test(URL) == True

test_list = [
    test_HeiseIE,
]

if __name__ == '__main__':
    import sys

    suite = unittest.TestSuite()
    for test_func in test_list:
        test_suite = unittest.makeSuite(test_func)
        suite.addTest(test_suite)
    result = unitt

# Generated at 2022-06-14 16:24:21.743111
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert(HeiseIE("http://www.heise.de/ct/artikel/c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2403911.html").extract() is not None)

# Generated at 2022-06-14 16:24:23.483146
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Test that no exception is raised
    HeiseIE()

# Generated at 2022-06-14 16:24:24.480240
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Test the constructor of class HeiseIE
    extractor = HeiseIE('https://www.heise.de')
    assert extractor is not None

# Generated at 2022-06-14 16:24:26.084364
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert isinstance(ie, KalturaIE)

# Generated at 2022-06-14 16:24:34.976566
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:24:38.262360
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert hasattr(ie, '_VALID_URL')
    assert ie._VALID_URL == r'https?://(?:www\.)?heise\.de/'

# Generated at 2022-06-14 16:24:39.374331
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()


# Generated at 2022-06-14 16:25:02.103709
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html', 
        'Heise')

# Generated at 2022-06-14 16:25:02.651210
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE()


# Generated at 2022-06-14 16:25:04.383038
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert 2 == HeiseIE._VALID_URL.count("%(id)")

# Generated at 2022-06-14 16:25:14.441529
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.SUCCESS == "SUCCESS"
    assert ie.FAIL == "FAIL"

    assert ie._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)*(?P<id>[^.]+\.(?:m3u8|xml|mp4|flv|webm|ogv))'


# Generated at 2022-06-14 16:25:15.035879
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    return HeiseIE()

# Generated at 2022-06-14 16:25:24.386156
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    #heise_de = 'https://www.heise.de/developer/artikel/Was-Java-8-verschlankt-und-was-es-neu-macht-2362347.html'
    heise_de = 'https://www.heise.de/ct/artikel/c-t-uplink-2-6-Kraftausdauer-Digitales-Gewinnspiel-3958596.html'
    from .test_downloads import real_download
    real_download(heise_de)

# Generated at 2022-06-14 16:25:26.250900
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE('')
    assert ie.ie_key() == 'heise'

# Generated at 2022-06-14 16:25:31.635563
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    try:
        instance = HeiseIE("https://www.heise.de/ct/artikel/c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2403911.html")
        assert(instance.__class__.__name__ == "HeiseIE")
    except Exception as e:
        raise e

# Generated at 2022-06-14 16:25:34.004419
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.get_info == HeiseIE._real_extract
    assert ie.ie_key == 'heise:video'

# Generated at 2022-06-14 16:25:37.151556
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    try:
        HeiseIE('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    except:
        raise AssertionError("HeiseIE not created")

# Generated at 2022-06-14 16:26:18.086672
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.ie_key() == 'heise'
    assert ie.suitable('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html') == True

# Generated at 2022-06-14 16:26:18.904454
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()



# Generated at 2022-06-14 16:26:21.409895
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    """
    Simple unit test for HeiseIE
    """
    heise_ie = HeiseIE()
    assert heise_ie



# Generated at 2022-06-14 16:26:24.302439
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE('HeiseIE', extract_title='extract_title', id_='id_', regex='regex', timestamp='timestamp')

# Generated at 2022-06-14 16:26:29.504501
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Test with a link to a video on Heise
    heise_test = HeiseIE({
        'url': 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html',
        'only_matching': True,
    })
    assert heise_test.suitable('Dummy') == True

# Generated at 2022-06-14 16:26:33.302637
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heiseie = HeiseIE()
    assert heiseie.ie._VALID_URL == heiseie._VALID_URL


# Generated at 2022-06-14 16:26:35.969127
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie._VALID_URL == "https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html"

# Generated at 2022-06-14 16:26:47.289866
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE("https://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html")
    assert ie.extract()
    assert ie.extract().get("title") == "nachgehakt: Wie sichert das c't-Tool Restric'tor Windows 10 ab?"
    assert ie.extract().get("description")
    assert ie.extract().get("description").find("c't-Fanenkeln und -Leser") >= 0
    assert ie.extract().get("thumbnail")
    assert ie.extract().get("timestamp")
    assert ie.extract().get("duration")

# Generated at 2022-06-14 16:26:49.784425
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    try:
        HeiseIE()
    except Exception as e:
        raise ValueError("Failed to initialize HeiseIE extractor: " + repr(e))

# Generated at 2022-06-14 16:26:54.914109
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise = HeiseIE("https://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html")
    heise.download("3700244")

# Generated at 2022-06-14 16:28:23.725232
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE()



# Generated at 2022-06-14 16:28:27.218851
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise_ie = HeiseIE()
    assert heise_ie.ie_key() == 'heise'
    assert heise_ie.ie_key() in InfoExtractor._WORKING_IE_KEY

# Generated at 2022-06-14 16:28:36.589542
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:28:38.568623
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ieObj = HeiseIE()

if __name__ == "__main__":
    test_HeiseIE()

# Generated at 2022-06-14 16:28:40.477674
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie
    assert ie.ie_key() == 'heise'

# Generated at 2022-06-14 16:28:41.512344
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()

# Generated at 2022-06-14 16:28:43.094943
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Tested by methods _test_kaltura_embed() and _test_youtube_embed() defined in YoutubeIE
    pass

# Generated at 2022-06-14 16:28:44.335495
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Simple test to avoid warnings
    HeiseIE()

# Generated at 2022-06-14 16:28:47.531442
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Test constructor with no argument.
    # For constructor, test if the result is an instance of youtube ie.
    ie = HeiseIE()
    assert isinstance(ie, InfoExtractor)


# Generated at 2022-06-14 16:28:48.553070
# Unit test for constructor of class HeiseIE
def test_HeiseIE():

    HeiseIE(InfoExtractor())

# Generated at 2022-06-14 16:30:40.579280
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    class_name = "HeiseIE"
    # check if class name has a corresponding class in youtube_dl.extractor

# Generated at 2022-06-14 16:30:42.234676
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    obj = HeiseIE()

if __name__ == '__main__':
    test_HeiseIE()

# Generated at 2022-06-14 16:30:45.983537
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Tests if the constructor works correctly
    try:
        HeiseIE()
    except Exception as e:
        print('ERROR: Constructor of HeiseIE failed!')
        print(e)
        return False
    return True


# Generated at 2022-06-14 16:30:48.446020
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    infoExtractor = HeiseIE();
    matched_url = infoExtractor._match_id(infoExtractor._VALID_URL);
    assert matched_url == "2404147";


# Generated at 2022-06-14 16:30:54.795756
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    global __test__
    __test__ = True
    # These tests should be always successful.
    # In order to always succeed we need to ensure that the class
    # we are testing does not use a random value (for the id parameter)
    # that can not be predicted at test time.
    assert HeiseIE('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')._match_id('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html') == '2404147'

# Generated at 2022-06-14 16:30:56.062603
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise_ie = HeiseIE()
    assert heise_ie is not None

# Generated at 2022-06-14 16:31:07.348976
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie._VALID_URL.match("http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html")
    assert ie._VALID_URL.match("https://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html")

# Generated at 2022-06-14 16:31:13.227667
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    """Class to test if the HeiseIE works."""
    ie = HeiseIE('https://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html')
    assert ie.url == 'https://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html'
    assert ie.valid_url == 'https://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html'

# Generated at 2022-06-14 16:31:23.079937
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Test HeiseIE.__init__()
    heise_ie = HeiseIE()
    assert heise_ie._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'
    # Test HeiseIE.suitable()
    assert heise_ie.suitable(r'https://www.heise.de/video/artikel/nachgehakt-Wie-sichert-das-c-t-Tool-Restric-tor-Windows-10-ab-3700244.html')

# Generated at 2022-06-14 16:31:23.954135
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    test_obj = HeiseIE({})
    assert test_obj is not None