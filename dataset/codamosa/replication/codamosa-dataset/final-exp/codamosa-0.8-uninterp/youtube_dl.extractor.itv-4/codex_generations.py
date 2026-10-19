

# Generated at 2022-06-14 16:34:44.431716
# Unit test for constructor of class ITVIE
def test_ITVIE():
    t = ITVIE()
    assert t.__class__.__name__ == 'ITVIE'
    

# Generated at 2022-06-14 16:34:54.288444
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    ITVBTCCIE_obj = ITVBTCCIE(url)
    assert ITVBTCCIE_obj.match.group('id') == 'btcc-2018-all-the-action-from-brands-hatch'
    assert ITVBTCCIE_obj.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:35:06.270239
# Unit test for constructor of class ITVIE
def test_ITVIE():
    info_extractor = ITVIE()
    test = {
        'url': 'https://www.itv.com/hub/liar/2a4547a0012',
        'info_dict': {
            'id': '2a4547a0012',
            'ext': 'mp4',
            'title': 'Liar - Series 2 - Episode 6',
            'description': 'md5:d0f91536569dec79ea184f0a44cca089',
            'series': 'Liar',
            'season_number': 2,
            'episode_number': 6,
        },
        'params': {
            # m3u8 download
            'skip_download': True,
        },
    }
    assert test == info_extractor.extract(test['url'])

# Generated at 2022-06-14 16:35:12.929261
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    t = ITVBTCCIE(ITVBTCCIE._downloader, 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert t.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:35:14.554008
# Unit test for constructor of class ITVIE
def test_ITVIE():
    """
    unit test for class ITVIE
    """
    init_class = ITVIE(InfoExtractor())
    assert init_class.name == 'ITV'

# Generated at 2022-06-14 16:35:17.643793
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    return ITVBTCCIE('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')

# Generated at 2022-06-14 16:35:20.911325
# Unit test for constructor of class ITVIE
def test_ITVIE():
    # pylint: disable=no-member
    ITVIE.setUp()
    # pylint: enable=no-member
    # check that there is no exception raised
    ITVIE()

# Generated at 2022-06-14 16:35:24.750967
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'



# Generated at 2022-06-14 16:35:35.029829
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    import sys
    import unittest
    import youtube_dl.extractor.common

    # in Python 3 there is no longer a "callable" function
    try:
        unicallable = callable
    except NameError:
        unicallable = lambda x: isinstance(x, collections.Callable)

    if sys.version_info.major >= 3:
        unicode_type = str
        basestring_type = str
        long_type = int
    else:
        unicode_type = unicode
        basestring_type = basestring
        long_type = long

    class TestInfoExtractor(unittest.TestCase):

        class MockYoutubeDl(object):
            def __init__(self):
                self.params = {}

            def prepare_filename(self, info_dict):
                return

# Generated at 2022-06-14 16:35:36.309776
# Unit test for constructor of class ITVIE
def test_ITVIE():
    itv_ie = ITVIE('test')
    assert itv_ie.country == 'GB'

# Generated at 2022-06-14 16:35:51.518645
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE()

# Generated at 2022-06-14 16:35:52.969187
# Unit test for constructor of class ITVIE
def test_ITVIE():
    for i in ITVIE._TESTS:
        yield ITVIE, i

# Generated at 2022-06-14 16:35:54.626731
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()
    assert ie.IE_DESC == 'ITV'

# Generated at 2022-06-14 16:35:57.317505
# Unit test for constructor of class ITVIE
def test_ITVIE():
    # Test constructor with the ITVIE class as parameter that is not used
    ITVIE(None, 'http://www.itv.com/hub/liar/2a4547a0012')

# Generated at 2022-06-14 16:36:00.559212
# Unit test for constructor of class ITVIE
def test_ITVIE():
    # This is a test for ITVIE
    # Create a new instance of ITVIE
    itvIE = ITVIE()
    # this is a test
    assert itvIE is not None, "Failed to create ITVIE"

# Generated at 2022-06-14 16:36:02.716604
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    itvbtcc = ITVBTCCIE()
    assert itvbtcc.BRIGHTCOVE_URL_TEMPLATE

# Generated at 2022-06-14 16:36:04.684419
# Unit test for constructor of class ITVIE
def test_ITVIE():
    test_obj = ITVIE(None)
    assert test_obj.ITVIE._VALID_URL == r'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'


# Generated at 2022-06-14 16:36:10.882101
# Unit test for constructor of class ITVIE
def test_ITVIE():
    """
    Example call to constructor of ITVIE class
    """
    # instantiate the class object
    itv = ITVIE()
    # set a webpage url
    url = 'https://www.itv.com/hub/liar/2a4547a0012'
    # call the method of the class object to get the webpage content
    webpage = itv._download_webpage(url)
    # print the content of the webpage
    print(webpage)
    # call the method to get the info dictionary
    info = itv._real_extract(url)
    print(json.dumps(info))



# Generated at 2022-06-14 16:36:14.377187
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    return ITVBTCCIE.static_test('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')


# Generated at 2022-06-14 16:36:18.445421
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    """Test ITVBTCCIE class constructor."""
    ITVBTCCIE("http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch")

# Generated at 2022-06-14 16:36:42.419499
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ITVBTCCIE(None)

# Generated at 2022-06-14 16:36:44.122391
# Unit test for constructor of class ITVIE
def test_ITVIE():
    inst = ITVIE()
    assert isinstance(inst, ITVIE)

# Generated at 2022-06-14 16:36:49.564133
# Unit test for constructor of class ITVIE
def test_ITVIE():
    itv = ITVIE('https://www.itv.com/hub/liar/2a4547a0012')
    assert itv._VALID_URL == r'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'
    assert itv._GEO_COUNTRIES == ['GB']

# Generated at 2022-06-14 16:36:57.136448
# Unit test for constructor of class ITVIE

# Generated at 2022-06-14 16:36:59.106409
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = "http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch"
    ie = ITVBTCCIE()
    assert ie.match_url(url)

# Generated at 2022-06-14 16:37:07.494959
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    class MockSel(object):
        def __init__(self, html):
            from ..compat import compat_str
            self.html = compat_str(html)

        def xpath(self, selector):
            return re.findall(selector, self.html)

        def __getitem__(self, item):
            if item is 0:
                return self
            raise IndexError()

    webpage = '<html><div data-video-id="5430123148001">...</div></html>'
    sel = MockSel(webpage)
    itvbtccie = ITVBTCCIE()
    itvbtccie._real_extract(itvbtccie._VALID_URL, sel)

# Generated at 2022-06-14 16:37:18.769975
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    itvBTCCIE = ITVBTCCIE("http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch")
    assert itvBTCCIE._VALID_URL == 'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert itvBTCCIE._TEST['url'] == 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    assert itvBTCCIE._TEST['info_dict']['id'] == 'btcc-2018-all-the-action-from-brands-hatch'
    assert itvBTCCIE._T

# Generated at 2022-06-14 16:37:19.743090
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVExtractor = ITVIE()


# Generated at 2022-06-14 16:37:27.280590
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    if not hasattr(ITVBTCCIE, '_download_webpage'):
        ITVBTCCIE._download_webpage = lambda self, *args, **kwargs: None

    info_extractor = ITVBTCCIE('test_ITVBTCCIE')

    assert info_extractor.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'
    assert info_extractor._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:37:34.434003
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    """
    Test test entry point to _real_extract.
    """
    url = "http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch"
    i = ITVBTCCIE()
    r = i._real_extract("http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch")
    assert r['id'] == "btcc-2018-all-the-action-from-brands-hatch"
    assert r['title'] == "BTCC 2018: All the action from Brands Hatch"
    assert r['playlist_mincount'] == 9

# Generated at 2022-06-14 16:38:34.355708
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE("https://www.itv.com/hub/all-star-musical-challenge/2a2698a0033")

# Generated at 2022-06-14 16:38:37.668119
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'
    assert ie.ie_key() == 'ITVBTCCIE'

# Generated at 2022-06-14 16:38:50.128352
# Unit test for constructor of class ITVIE
def test_ITVIE():
    inst = ITVIE()
    assert inst._VALID_URL == 'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'
    assert inst._GEO_COUNTRIES == ['GB']

# Generated at 2022-06-14 16:38:54.123125
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:39:06.713798
# Unit test for constructor of class ITVIE
def test_ITVIE():
    obj = ITVIE()
    assert obj._VALID_URL == r'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'
    assert obj._GEO_COUNTRIES == ['GB']

# Generated at 2022-06-14 16:39:07.369291
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE()

# Generated at 2022-06-14 16:39:15.321740
# Unit test for constructor of class ITVIE
def test_ITVIE():
    class ITVUE_unit_test(ITVIE):
        def _download_webpage(self, url, video_id):
            webpage = self._read_from_file(
                'itv.webpage',
                'https://www.itv.com/hub/liar/2a4547a0012')
            return webpage
            
        def _download_json(self, url, video_id, data, headers):
            ios_playlist = self._read_from_file(
                'itv.json',
                'https://www.itv.com/hub/liar/2a4547a0012')
            return ios_playlist

    itvue_unit_test = ITVUE_unit_test()
    itvue_unit_test.result.get('formats')
    itvue_

# Generated at 2022-06-14 16:39:15.929217
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ITVBTCCIE()

# Generated at 2022-06-14 16:39:17.724026
# Unit test for constructor of class ITVIE
def test_ITVIE():

    context = Context()
    
    itv_ie = ITVIE(context)
    assert itv_ie is not None

# Generated at 2022-06-14 16:39:26.401120
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    # Tested on 2019-06-29
    info = ITVBTCCIE()._real_extract(url)

# Generated at 2022-06-14 16:41:47.088924
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    """
    Basic test of ITVBTCCIE constructor
    """
    ITVBTCCIE()

# Generated at 2022-06-14 16:41:54.998736
# Unit test for constructor of class ITVIE
def test_ITVIE():
    test_video_id = '2a4547a0012'
    test_url = 'https://www.itv.com/hub/liar/' + test_video_id

    test_extractor = ITVIE()
    test_dict = test_extractor._real_extract(test_url)

    # Check instance variables
    assert test_dict['id'] == test_video_id
    assert test_dict['title'] == 'Liar - Series 2 - Episode 6'
    assert test_dict['description'] == 'md5:d0f91536569dec79ea184f0a44cca089'
    assert test_dict['series'] == 'Liar'
    assert test_dict['season_number'] == 2
    assert test_dict['episode_number'] == 6

# Generated at 2022-06-14 16:42:01.613588
# Unit test for constructor of class ITVIE
def test_ITVIE():
    info_extractor = ITVIE()
    url = 'https://www.itv.com/hub/liar/2a4547a0012'
    webpage = """<html>
    <body>
    <div id="video" data-video-playlist="http://playlist.itv.com/playlist/playlist.m3u8?network=itv.com" data-video-hmac="2e84baa79f2d3c8a3d3a9e9e1c0b1d44"></div>
    </html>
    """

# Generated at 2022-06-14 16:42:09.883578
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    import sys
    sys.path.append("tests/python")
    import testtools
    btccite = ITVBTCCIE()
    t = testtools.TestCase()
    t.assertEquals(btccite._VALID_URL, "https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)")
    t.assertEquals(btccite.BRIGHTCOVE_URL_TEMPLATE, "http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s")

# Generated at 2022-06-14 16:42:18.940410
# Unit test for constructor of class ITVIE
def test_ITVIE():
    itv_ie = ITVIE()

    # Test Inexistant Class
    assert itv_ie.__class__.__name__ == 'ITVIE'

    # Test Class
    assert hasattr(itv_ie, '_VALID_URL')
    assert hasattr(itv_ie, '_TESTS')
    assert hasattr(itv_ie, 'BROWSER')
    assert hasattr(itv_ie, 'SUCCESS_CODES')
    assert hasattr(itv_ie, 'IE_NAME')
    assert hasattr(itv_ie, '_TEST')
    assert hasattr(itv_ie, '_download_webpage_handle')
    assert hasattr(itv_ie, '_download_json')

# Generated at 2022-06-14 16:42:24.947831
# Unit test for constructor of class ITVIE
def test_ITVIE():
    itv = ITVIE()
    assert itv.extract('https://www.itv.com/hub/liar/2a4547a0012')
    assert itv.extract('https://www.itv.com/hub/through-the-keyhole/2a2271a0033')
    assert itv.extract('https://www.itv.com/hub/james-martins-saturday-morning/2a5159a0034')
    assert itv.extract('https://www.itv.com/hub/whos-doing-the-dishes/2a2898a0024')

# Generated at 2022-06-14 16:42:25.621153
# Unit test for constructor of class ITVIE
def test_ITVIE():
    assert ITVIE

# Generated at 2022-06-14 16:42:35.869907
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()
    assert ie.IE_NAME == 'ITV'
    assert ie.IE_DESC == 'ITV Player and ITV Hub'
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'
    assert ie._TESTS[0]['info_dict']['id'] == '2a4547a0012'

# Generated at 2022-06-14 16:42:43.977290
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:42:47.101295
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    ie = ITVBTCCIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE is not None