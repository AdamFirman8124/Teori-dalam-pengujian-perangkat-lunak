

# Generated at 2022-06-14 16:24:06.860028
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE._VALID_URL == HeiseIE._TESTS[0]['info_dict']['id']

# Generated at 2022-06-14 16:24:09.172977
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE._VALID_URL
    assert HeiseIE._TESTS

# Generated at 2022-06-14 16:24:12.874095
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    class TestHeiseIE(HeiseIE):
        def _real_extract(self, url):
            return self

    ie = TestHeiseIE()
    assert ie.ie_key() == 'heise'

# Generated at 2022-06-14 16:24:24.943290
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    """Tests for HeiseIE"""
    # test 1: regex: article with youtube video
    url = 'http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html'
    info = HeiseIE()._extract_info(url)
    assert info["id"] == "6kmWbXleKW4"

    # test 2: regex: article with kaltura video
    url = 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
    info = HeiseIE()._extract_info(url)

# Generated at 2022-06-14 16:24:25.604680
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie=HeiseIE()

# Generated at 2022-06-14 16:24:26.580480
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert('<class HeiseIE at' in str(HeiseIE))

# Generated at 2022-06-14 16:24:35.043291
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Skip tests on class instantiation if not available
    from ..utils import skip_if_not_missing_optional
    try:
        from .youtube import YoutubeBaseInfoExtractor
    except (AttributeError, ImportError):
        skip_if_not_missing_optional('youtube', __name__)
    try:
        from .kaltura import KalturaIE
    except (AttributeError, ImportError):
        skip_if_not_missing_optional('kaltura', __name__)
    # Declare class instantiation
    HeiseIE("http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html")


# Generated at 2022-06-14 16:24:39.233524
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    obj = HeiseIE(None)

# Generated at 2022-06-14 16:24:48.588967
# Unit test for constructor of class HeiseIE

# Generated at 2022-06-14 16:24:49.598575
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heiseie = HeiseIE()

# Generated at 2022-06-14 16:25:03.352962
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE.ie_key() == 'heise'
    assert HeiseIE.ie_key() == 'HeiseIE'
    assert HeiseIE.ie_key() == 'Heise'
    assert HeiseIE.ie_key() == 'Heiseie'

# Generated at 2022-06-14 16:25:04.534011
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    # pass

# Generated at 2022-06-14 16:25:14.576999
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # test instantiation
    ie = HeiseIE()
    # test URL
    filename = 'HeiseIE'
    url = 'http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html'
    assert ie.suitable(url)
    assert ie.url_result(url)['id'] == '1_kkrq94sm'
    yt_url = 'http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html'
    assert ie.suitable(yt_url)
    assert ie.url_result(yt_url)

# Generated at 2022-06-14 16:25:15.675714
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()


# Generated at 2022-06-14 16:25:17.176374
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE(None)._VALID_URL == HeiseIE._VALID_URL

# Generated at 2022-06-14 16:25:30.038198
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Test if can construct a HeiseIE and if it founds the correct kaltura videoID
    # from a demo page.
    from .kaltura import KalturaIE
    from .youtube import YoutubeIE
    from .matchtv import MatchTVIE

    page_url = ('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Ownclou'
                'd-Tastaturen-Peilsender-Smartphone-2404147.html')

    HEISE = HeiseIE()
    heise_result = HEISE.extract(page_url)

    # kaltura:2238431:1_kkrq94sm
    assert(heise_result['id'] == '1_kkrq94sm')

    KALTURA = KalturaIE

# Generated at 2022-06-14 16:25:32.288717
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert isinstance(ie, HeiseIE) == True


# Generated at 2022-06-14 16:25:35.561665
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:25:48.037943
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    """Test HeiseIE."""
    from youtube_dl.compat import compat_str
    from youtube_dl.utils import (
        ExtractorError,
    )

    url = 'http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html'
    url_not_found = 'http://www.heise.de/ct/artikel/c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2403911.html'

    # Test: download with type=url
    obj = HeiseIE()
    obj.extract(url)

    # Test: download with type=url_transparent
    obj = HeiseIE()

# Generated at 2022-06-14 16:25:49.614465
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise_ie = HeiseIE()
    assert isinstance(heise_ie, InfoExtractor)

# Generated at 2022-06-14 16:26:14.226131
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE("https://www.heise.de/ct/artikel/c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2403911.html")
    assert ie.URL == "https://www.heise.de/ct/artikel/c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2403911.html"

# Generated at 2022-06-14 16:26:23.171690
# Unit test for constructor of class HeiseIE

# Generated at 2022-06-14 16:26:25.321786
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    assert HeiseIE.ie_key() == 'heise'

# Generated at 2022-06-14 16:26:31.240215
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    h = HeiseIE()
    assert h.suitable('https://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')
    assert h.suitable('https://www.heise.de/ct/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')


# Generated at 2022-06-14 16:26:37.565763
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    IE = HeiseIE()

    assert IE.ie_key() == 'heise'
    assert IE.server_url() == 'http://www.heise.de'
    assert IE.base_url() == 'http://www.heise.de/video'
    assert IE.title() == 'heise'
    assert IE.description() == 'Heise Medien GmbH & Co. KG [DE]'
    assert IE.short_name() == 'heise'
    assert IE.extractor_keywords() == ['heise']
    assert IE.age_limit() == 0

# Generated at 2022-06-14 16:26:39.078116
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.name in ie.IE_NAME

# Generated at 2022-06-14 16:26:50.883535
# Unit test for constructor of class HeiseIE
def test_HeiseIE():

    assert HeiseIE._extract_url('https://www.heise.de/video/artikel/Der-c-t-uplink-im-Dezember-im-Videopodcast-3785331.html') == 'https://www.heise.de/video/artikel/Der-c-t-uplink-im-Dezember-im-Videopodcast-3785331.html'

# Generated at 2022-06-14 16:26:52.982919
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    sut = HeiseIE()
    assert sut.name == "heise"
    assert sut.ie_key() == "heise"

# Generated at 2022-06-14 16:26:56.770655
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    """Test the HeiseIE constructor"""
    heise = HeiseIE()
    assert( heise._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html')

# Generated at 2022-06-14 16:27:00.644808
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    result = HeiseIE("http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html")
    assert result != None

# Generated at 2022-06-14 16:27:54.517382
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    sut = HeiseIE()
    assert sut._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:27:56.237482
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    inst = HeiseIE()
    inst.suite()

# Generated at 2022-06-14 16:28:08.161167
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    # Test of url "https://www.heise.de/ct/artikel/c-t-uplink-20-8-Staubsaugerroboter-Xiaomi-Vacuum-2-AR-Brille-Meta-2-und-Android-rooten-3959893.html"
    url = 'https://www.heise.de/ct/artikel/c-t-uplink-20-8-Staubsaugerroboter-Xiaomi-Vacuum-2-AR-Brille-Meta-2-und-Android-rooten-3959893.html'
    # Test of return value of function "_real_extract()"
    heise_extractor = HeiseIE()
    info = heise_extractor.extract(url)

    # Test of a return value of

# Generated at 2022-06-14 16:28:09.033686
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()

# Generated at 2022-06-14 16:28:09.953508
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE(None)

# Generated at 2022-06-14 16:28:10.877576
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE(InfoExtractor)

# Generated at 2022-06-14 16:28:12.106056
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    return


# Generated at 2022-06-14 16:28:16.273947
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert HeiseIE.suitable('http://www.heise.de/video/artikel/Podcast-c-t-uplink-3-3-Owncloud-Tastaturen-Peilsender-Smartphone-2404147.html')

# Generated at 2022-06-14 16:28:27.351827
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:28:27.930182
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()

# Generated at 2022-06-14 16:30:10.701717
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    import unittest
    testClass = unittest.TestCase()
    HeiseIE()
    HeiseIE(testClass)
    HeiseIE(testClass)._real_initialize()

# Generated at 2022-06-14 16:30:13.162531
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.ie_key() == 'HeiseIE'
    assert ie.ie_key() in ie._WORKING_IE

# Generated at 2022-06-14 16:30:14.905668
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    heise = HeiseIE()
    assert heise.ie_key() == 'heise'

# Generated at 2022-06-14 16:30:15.754537
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()

# Generated at 2022-06-14 16:30:19.711631
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.ie_key() == 'Heise'
    assert ie.ie_key() in IE_NAME_TO_CLASS.keys()
    assert IE_NAME_TO_CLASS['Heise'] == HeiseIE

# Generated at 2022-06-14 16:30:27.248236
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    # Test for URL https://www.youtube.com/watch?v=nAnSQopgRrc
    url = 'https://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html'
    info_dict = ie._real_extract(url)
    assert info_dict['url'] == '6kmWbXleKW4'
    # Test for URL https://www.youtube.com/watch?list=PLMx28u8W02KF7n3TRrEeInh1a8HZ9XDZ0&v=yH-7CkUTR2Q

# Generated at 2022-06-14 16:30:38.257558
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    ie = HeiseIE()
    assert ie.name == "heise"
    assert ie.ie_key() == "heise"
    assert ie.url_re == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'
    assert ie.video_id_re == r'(?P<prefix>[^-]+)-(?P<id>[0-9]+)'
    assert ie.file_id_re == r'(?P<id>[0-9]+)'
    assert ie.mediatype == "video"
    assert ie.extract_format == "mp4"
    assert ie.skip_download == False

# Generated at 2022-06-14 16:30:40.502368
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    HeiseIE()._download_webpage(url='',
                                video_id='',
                                headers=None)



# Generated at 2022-06-14 16:30:44.481511
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    test_HeiseIE = HeiseIE()
    assert test_HeiseIE._VALID_URL == r'https?://(?:www\.)?heise\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\.html'

# Generated at 2022-06-14 16:30:48.446500
# Unit test for constructor of class HeiseIE
def test_HeiseIE():
    url = 'http://www.heise.de/newsticker/meldung/Netflix-In-20-Jahren-vom-Videoverleih-zum-TV-Revolutionaer-3814130.html'
    heise = HeiseIE()
    heise_result = heise.extract(url)
    assert heise_result