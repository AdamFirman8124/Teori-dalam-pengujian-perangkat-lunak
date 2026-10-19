

# Generated at 2022-06-14 16:34:52.928563
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # xpath is a utility function to get nodes in html
    from lxml.html import soupparser, fromstring

    def xpath(expr):
        return fromstring(html).xpath(expr)

    # first unit test: check if a valid URL is accepted
    valid_url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    ie = KonserthusetPlayIE(dict(url=valid_url))
    # check if the initialized instance of InfoExtractor contains the URL
    assert ie._match_id(ie.url) == 'CKDDnlCY-dhWAAqiMERd-A'

    # second unit test: check if a non-valid URL is rejected

# Generated at 2022-06-14 16:34:55.446477
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert KonserthusetPlayIE()._VALID_URL == "^https?://(www\.)?konserthusetplay\.se/\?.*\bm=([^&]+)"

# Generated at 2022-06-14 16:34:57.924941
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Run this if this file is run directly
    if __name__ == '__main__':
        KonserthusetPlayIE()

# Generated at 2022-06-14 16:35:10.338928
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    khp = KonserthusetPlayIE()
    assert khp._VALID_URL == "http://(www\.)?konserthusetplay\.se/\?.*\bm=([^&]+)"

# Generated at 2022-06-14 16:35:15.469376
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    test_instance = KonserthusetPlayIE()
    assert test_instance._VALID_URL == "^https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=([^&]+)"

# Generated at 2022-06-14 16:35:17.409381
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    obj = KonserthusetPlayIE()
    assert obj.ie_key() == 'KonserthusetPlay'

# Generated at 2022-06-14 16:35:29.433988
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    """ Test case for constructor of class KonserthusetPlayIE 
    """

    # Instantiate unit test class
    instance = KonserthusetPlayIE()

    # Test for _VALID_URL
    assert instance._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

    # Test for _TESTS

# Generated at 2022-06-14 16:35:37.611015
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:35:45.528102
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE("http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A")
    assert ie.url == 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    assert ie.video_id == 'CKDDnlCY-dhWAAqiMERd-A'
    assert ie.playlist_id is None
    assert ie.playlist_title is None
    assert ie.playlist_description is None
    assert ie.playlist_thumbnail is None
    assert ie.playlist_uploader is None
    assert ie.playlist_uploader_id is None
    assert ie.playlist_extractor is None
    assert ie.playlist_external

# Generated at 2022-06-14 16:35:46.333128
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    return KonserthusetPlayIE()

# Generated at 2022-06-14 16:36:09.432946
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Tests that the class could be initialized
    assert KonserthusetPlayIE

# Generated at 2022-06-14 16:36:13.105079
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    test_obj = KonserthusetPlayIE()
    print('Object: ' + str(test_obj))
    assert isinstance(test_obj, KonserthusetPlayIE)


# Generated at 2022-06-14 16:36:14.582706
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    raise NotImplementedError("test_KonserthusetPlayIE is not implemented")

# Generated at 2022-06-14 16:36:20.927082
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    url = 'http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw'
    ie = KonserthusetPlayIE(url)
    assert(ie._match_id(url) == 'elWuEH34SMKvaO4wO_cHBw')
# End of unit test for class KonserthusetPlayIE

# Generated at 2022-06-14 16:36:26.573797
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Create a new KonserthusetPlayIE instance
    k = KonserthusetPlayIE()
    assert isinstance(k, KonserthusetPlayIE)


# Test video with id e3039b24-a0e8-4dbd-84a2-1c941f2ea1b5
# Test with pytest -v -s test_konserthuset.py

# Generated at 2022-06-14 16:36:32.250944
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.IE_NAME == KonserthusetPlayIE.IE_NAME
    assert ie.IE_DESC == KonserthusetPlayIE.IE_DESC
    assert ie.URL_PATTERN == KonserthusetPlayIE.URL_PATTERN
    assert ie.VALID_URL == KonserthusetPlayIE.VALID_URL

# Generated at 2022-06-14 16:36:38.715589
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    url = 'https://video.konserthuset.se/v/326323'
    konserthuset_play_ie = KonserthusetPlayIE()
    konserthuset_play_ie.extract(url)
    assert konserthuset_play_ie._downloader != None
    assert konserthuset_play_ie._match_id(url) == '326323'
    assert len(konserthuset_play_ie._TESTS) > 0
    assert konserthuset_play_ie._VALID_URL == 'https?://(?:www\\.)?(?:konserthusetplay|rspoplay)\\.se/\\?.*\\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:36:48.049761
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # A unit test for class KonserthusetPlayIE
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    konserthusetplayIE = KonserthusetPlayIE()
    konserthusetplayIE.url = url

# Generated at 2022-06-14 16:36:50.689574
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    ie.extract("http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A")

# Generated at 2022-06-14 16:36:54.823685
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    match = ie._VALID_URL.match(
        'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    assert match
    assert ie.suitable(match)
    # assert ie.IE_NAME == 'KonserthusetPlay'

# Generated at 2022-06-14 16:37:21.117223
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    obj = KonserthusetPlayIE()
    assert obj.ie_key() == 'KonserthusetPlay'
    assert obj.ie_name() == 'KonserthusetPlay'
    assert obj.ie_id() == 'konserthusetplay.se'
    assert obj.next_page() is None

# Generated at 2022-06-14 16:37:25.759019
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    try:
        video_id = 'CKDDnlCY-dhWAAqiMERd-A'
        url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
        KonserthusetPlayIE(url).extract()
    except:
        print('The URL of KonserthusetPlayIE is invalid')

# Generated at 2022-06-14 16:37:26.781649
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    yt = KonserthusetPlayIE()
    assert yt != None

# Generated at 2022-06-14 16:37:28.790282
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')

# Generated at 2022-06-14 16:37:36.290689
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.suitable("http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A")
    assert ie.suitable("http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw")
    assert not ie.suitable("http://www.konserthuset.se/?m=CKDDnlCY-dhWAAqiMERd-A")
    assert not ie.suitable("http://www.konserthusetplay.se/")

# Generated at 2022-06-14 16:37:38.198488
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:37:42.000048
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    # Instantiation
    KonserthusetPlayIE('KonserthusetPlay');
    # No assert statements (see https://github.com/rg3/youtube-dl/blob/master/youtube_dl/extractor/youtube.py)

# Generated at 2022-06-14 16:37:43.011860
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE()

# Generated at 2022-06-14 16:37:50.765286
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    if __name__ == '__main__':
        url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
        video_id = 'CKDDnlCY-dhWAAqiMERd-A'
        url2 = 'http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw'
        video_id2 = 'elWuEH34SMKvaO4wO_cHBw'
        ie = KonserthusetPlayIE()
        ie.get_url(url) == 'https://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'

# Generated at 2022-06-14 16:37:55.322626
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():

    # Unit test should not fail
    try:
        KonserthusetPlayIE("https://www.youtube.com/watch?v=3qnDPAGxoZw")
        assert True
    except:
        assert False

# Generated at 2022-06-14 16:38:52.884853
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    from .common import KonserthusetPlayIE
    ie = KonserthusetPlayIE(KonserthusetPlayIE._VALID_URL)
    assert ie._VALID_URL == KonserthusetPlayIE._VALID_URL

# Generated at 2022-06-14 16:38:55.171419
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie_konserthuset_play = KonserthusetPlayIE()
    print(ie_konserthuset_play)


# Generated at 2022-06-14 16:39:01.348358
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert ie.IE_NAME == "KonserthusetPlay"
    assert ie.IE_DESC == "KonserthusetPlay"
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'
    assert ie.BRANDING_NAME == "KonserthusetPlay"
    assert ie.LOGO_URL == "http://www.konserthusetplay.se/assets/images/player/logo.png"

# Generated at 2022-06-14 16:39:04.623407
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    IE = KonserthusetPlayIE
    ie = IE()
    assert ie.IE_NAME == 'konserthusetplay'
    assert ie.IE_DESC == 'Konserthuset Play'

# Generated at 2022-06-14 16:39:05.756903
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE();

# Generated at 2022-06-14 16:39:14.392654
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A', 'Mozilla/5.0 (X11; Linux i686; rv:31.0) Gecko/20100101 Firefox/31.0 Iceweasel/31.6.0')
    # Test IE is KonserthusetPlay
    if ie != None and ie != 'KonserthusetPlay':
        ie = None
    # Test download webpage is valid
    if ie != None:
        webpage = ie._download_webpage('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A', 'CKDDnlCY-dhWAAqiMERd-A')

# Generated at 2022-06-14 16:39:16.701202
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    """ Test constructor of class KonserthusetPlayIE

    """
    instance = KonserthusetPlayIE()

# Generated at 2022-06-14 16:39:18.467783
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    assert isinstance(ie, InfoExtractor)

# Generated at 2022-06-14 16:39:22.381759
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    try:
        url = 'https://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
        KonserthusetPlayIE(url)
        assert True
    except:
        assert False

# Generated at 2022-06-14 16:39:23.697965
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    str(ie)


# Generated at 2022-06-14 16:41:22.187431
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert KonserthusetPlayIE()._VALID_URL == KonserthusetPlayIE.__bases__[0]._VALID_URL

# Generated at 2022-06-14 16:41:23.318020
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    try:
        KonserthusetPlayIE()
    except:
        return False
    return True


# Generated at 2022-06-14 16:41:26.976229
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    url = 'http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A'
    ie.extract(url)
    url = 'http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw'
    ie.extract(url)

# Generated at 2022-06-14 16:41:28.752829
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    assert(KonserthusetPlayIE().get_instance() is not None)

# Generated at 2022-06-14 16:41:38.557158
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    k = KonserthusetPlayIE()
    if k.SUFFIX != "IE_NAME.ie_key":
        raise AssertionError("Unit test for KonserthusetPlayIE.SUFFIX failed")
    if k.ie_key() != "KonserthusetPlay":
        raise AssertionError("Unit test for KonserthusetPlayIE.ie_key failed")
    if k.ie_key() != k.name:
        raise AssertionError("Unit test for KonserthusetPlayIE.name failed")
    if k.name == "KonserthusetPlay":
        raise AssertionError("Unit test for KonserthusetPlayIE.name failed")

# Generated at 2022-06-14 16:41:39.370890
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    k = KonserthusetPlayIE()

# Generated at 2022-06-14 16:41:48.198363
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    KonserthusetPlayIE('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    KonserthusetPlayIE('http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw')
    with pytest.raises(ExtractorError):
        KonserthusetPlayIE('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A', expected=True)

# Generated at 2022-06-14 16:41:56.131772
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    assert ie._VALID_URL == r'https?://(?:www\.)?(?:konserthusetplay|rspoplay)\.se/\?.*\bm=(?P<id>[^&]+)'

# Generated at 2022-06-14 16:41:58.613927
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    konserthusetPlayIE = KonserthusetPlayIE()
    konserthusetPlayIE.extract('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')

# Generated at 2022-06-14 16:42:02.837619
# Unit test for constructor of class KonserthusetPlayIE
def test_KonserthusetPlayIE():
    ie = KonserthusetPlayIE()
    ie.extract('http://www.konserthusetplay.se/?m=CKDDnlCY-dhWAAqiMERd-A')
    ie.extract('http://rspoplay.se/?m=elWuEH34SMKvaO4wO_cHBw')