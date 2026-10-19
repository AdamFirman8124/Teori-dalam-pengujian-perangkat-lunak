

# Generated at 2022-06-14 16:34:43.911256
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # GIVEN a KonserthusetPlayIE object
    ie = KonserthusetPlayIE()

    # WHEN calling the constructor
    # THEN an object of KonserthusetPlayIE class is returned
    assert isinstance(ie, KonserthusetPlayIE)



# Generated at 2022-06-14 16:34:48.979941
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Test constructor
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    o = KonserthusetPlayIE()
    o.Suitable(url)
    o.extract(url)

# Generated at 2022-06-14 16:34:50.355727
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    newKonserthusetPlayIE = KonserthusetPlayIE()

# Generated at 2022-06-14 16:34:52.302789
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    pass

if __name__ == '__main__':
    test_KonserthusetPlayIE()

# Generated at 2022-06-14 16:34:53.946008
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie is not None

# Generated at 2022-06-14 16:34:58.642691
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()

    assert ie._VALID_URL == ie.VALID_URL
    assert ie._TESTS == ie.TESTS

    assert ie._match_id(ie._VALID_URL) == ie._match_id(ie.VALID_URL)
    assert ie._match_id(ie._TESTS[0]['url']) == ie._match_id(ie.TESTS[0]['url'])

# Generated at 2022-06-14 16:35:02.541795
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.ie_key() == 'KonserthusetPlay'
    assert ie.ie_name() == 'Konserthuset Play'

# Generated at 2022-06-14 16:35:08.130698
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    # check if KonserthusetPlayIE implements video_id
    assert KonserthusetPlayIE._match_id(url) == 'CKDDnlCY-dhWAAqiMERd-A'

# Generated at 2022-06-14 16:35:16.754872
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    ie._download_webpage = lambda x, y: 'KonserthusetPlayIE'
    ie._download_json = lambda x, y: 'KonserthusetPlayIE'
    ie._search_regex = lambda x, y, z: 'KonserthusetPlayIE'

    # Don't use test URL
    ie.extract('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')

# Generated at 2022-06-14 16:35:23.924340
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:35:36.627415
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    obj = KonserthusetPlayIE()

# Generated at 2022-06-14 16:35:38.176992
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie


# Generated at 2022-06-14 16:35:40.296967
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert issubclass(KonserthusetPlayIE, InfoExtractor)



# Generated at 2022-06-14 16:35:46.240420
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = InfoExtractor()
    url = 'http://konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    konserthuset_play_ie = KonserthusetPlayIE(ie._downloader, ie._downloader.params)
    assert konserthuset_play_ie._downloader is ie._downloader
    assert konserthuset_play_ie._downloader.params is ie._downloader.params
    konserthuset_play_ie._build_rtmp_app_data(url) == 'http://konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'

# Generated at 2022-06-14 16:35:51.334605
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    a = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    p = KonserthusetPlayIE()
    p.extract(a);
    p.extract(a);
    p.extract(a);

# Generated at 2022-06-14 16:35:55.984452
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    konserthusetplay_ie = KonserthusetPlayIE()
    assert konserthusetplay_ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:36:06.315889
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.ie_key() == 'KonserthusetPlay'
    assert ie.SUFFIX == 'Play'
    assert ie.info_dict == None
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:36:08.567883
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie is not None
    assert ie.IE_NAME == "konserthusetplay"
    assert ie.VALID_URL

# Generated at 2022-06-14 16:36:09.572820
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:36:12.316556
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    """Test the constructor of class KonserthusetPlayIE."""
    ie = KonserthusetPlayIE()

# Generated at 2022-06-14 16:36:47.208839
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    test_url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    konplay_IE = KonserthusetPlayIE()
    # Test if valid url is given
    assert konplay_IE._is_valid_url(test_url) == True
    # Test if valid url was returned
    assert konplay_IE._valid_url(test_url) == test_url
    # Test if invalid url is given
    assert konplay_IE._is_valid_url(None) == False
    # Test if correct video ID is obtained
    assert konplay_IE._match_id(test_url) == 'CKDDnlCY-dhWAAqiMERd-A'
    # Test if valid download url is returned

# Generated at 2022-06-14 16:36:48.867761
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert KonserthusetPlayIE(None)._VALID_URL == None



# Generated at 2022-06-14 16:36:56.676643
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'
    assert ie._TESTS[0]['url'] == 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    assert ie._TESTS[0]['md5'] == 'e3fd47bf44e864bd23c08e487abe1967'

# Generated at 2022-06-14 16:37:07.071508
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # prepare parameters
    url = "http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A"
    fd = open("lib/test/test.html")
    webpage = fd.read()
    fd.close()
    video_id = "CKDDnlCY-dhWAAqiMERd-A"

    # test constructor
    ie = KonserthusetPlayIE()


# Generated at 2022-06-14 16:37:07.991938
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:37:19.278473
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:37:23.469580
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A', {})
    KonserthusetPlayIE('http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw', {})

# Generated at 2022-06-14 16:37:25.047573
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    i = KonserthusetPlayIE()
    assert i == KonserthusetPlayIE

# Generated at 2022-06-14 16:37:28.024178
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    video_id = 'CKDDnlCY-dhWAAqiMERd-A'
    webpage = 'This webpage contains KonserthusetPlayIE video with id = {}'.format(video_id)
    return KonserthusetPlayIE()._real_extract(webpage, video_id)

# Generated at 2022-06-14 16:37:38.552453
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # test non existing URL
    assert KonserthusetPlayIE.suitable("http://www.konserthusetplay.se/") == False
    assert KonserthusetPlayIE.suitable("http://www.konserthusetplay.se/something/123") == False
    # test non existing URL with a query
    assert KonserthusetPlayIE.suitable("http://www.konserthusetplay.se/something/123?q=abc") == False
    # test existing video
    assert KonserthusetPlayIE.suitable("http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A") == True
    # test existing video with a query

# Generated at 2022-06-14 16:38:36.123800
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert isinstance(ie, KonserthusetPlayIE)

# Generated at 2022-06-14 16:38:40.382533
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.is_supported('https://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    assert not ie.is_supported('https://www.konserthusetplay.se/?')

# Generated at 2022-06-14 16:38:52.579693
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert isinstance(ie, KonserthusetPlayIE)
    assert hasattr(ie, '_VALID_URL')
    assert hasattr(ie, '_TESTS')
    assert hasattr(ie, '_extract_m3u8_formats')
    assert hasattr(ie, '_match_id')
    assert hasattr(ie, '_real_extract')
    assert hasattr(ie, '_PHISHING_URL')
    assert hasattr(ie, '_TESTS')
    assert hasattr(ie, '_download_webpage')
    assert hasattr(ie, '_search_regex')
    assert hasattr(ie, '_download_json')
    assert hasattr(ie, '_sort_formats')

# Generated at 2022-06-14 16:38:54.034598
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # check if the class could be instantiated
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:38:56.996703
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie is not None

# Generated at 2022-06-14 16:39:00.424484
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    ie.extract("http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A")

# Generated at 2022-06-14 16:39:03.736529
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    assert ie.SUFFIX == '.se'
    assert ie.VALID_URL == 'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'
    assert ie._TESTS[0]['url'] == 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'

# Generated at 2022-06-14 16:39:07.706777
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    result = KonserthusetPlayIE()._extract_info(url, url)
    assert result



# Generated at 2022-06-14 16:39:08.665718
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert KonserthusetPlayIE

# Generated at 2022-06-14 16:39:11.638777
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    """
    Basic test of constructor
    """
    ie = KonserthusetPlayIE()
    assert ie.ie_key() == 'konserthusetplay'
    assert ie.ie_desc() == 'KonserthusetPlay'

# Generated at 2022-06-14 16:41:26.728641
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.ie_key() == 'KonserthusetPlay'
    assert ie.suitable("https://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A")
    assert ie.suitable("http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A")
    assert not ie.suitable("http://www.konserthusetplay.se/?m=CKDDnlCY")

# Generated at 2022-06-14 16:41:27.934561
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:41:31.072854
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE(InfoExtractor('test'))

if __name__ == '__main__':
    test_KonserthusetPlayIE()

# Generated at 2022-06-14 16:41:34.242629
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    yt = KonserthusetPlayIE()
    yt.suitable('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')

# Generated at 2022-06-14 16:41:36.361690
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    ie = KonserthusetPlayIE(test=True)

test_KonserthusetPlayIE()

# Generated at 2022-06-14 16:41:37.903244
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    try:
        import pytest
        pytest.skip("Not implemented test")
    except ImportError:
        pass

# Generated at 2022-06-14 16:41:40.606095
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    try:
        KonserthusetPlayIE('www.konserthusetplay.se')
    except Exception as e:
        raise AssertionError("Not created KonserthusetPlayIE instance: " + str(e))


# Generated at 2022-06-14 16:41:51.889257
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    '''
    Method for testing the constructor of class KonserthusetPlayIE
    '''
    test_object = KonserthusetPlayIE()
    assert test_object._VALID_URL == 'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:41:55.667549
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE('konserthusetplay.se')
    assert ie.suitable('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')

# Generated at 2022-06-14 16:42:02.047116
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():

    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'

    ydl = Ydl()
    ydl.params['nooverwrites'] = True
    info = ydl.extract_info(url, download=False)

    assert info['id'] == 'CKDDnlCY-dhWAAqiMERd-A'
    assert info['title'] == 'Orkesterns instrument: Valthornen'
    assert info['ext'] == 'mp4'
    assert info['thumbnail'] == 're:^https?://.*$'
    assert info['duration'] == 398.76
    assert 'Orkesterns instrument: Valthornen' in info['description']