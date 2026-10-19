

# Generated at 2022-06-14 16:34:54.770406
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ITVExtractor = ITVBTCCIE()
    ITVExtractor.BRIGHTCOVE_URL_TEMPLATE = 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'
    ITVExtractor.BRIGHTCOVE_VIDEO_RE = re.compile(r'''(?x)
<meta[^>]+?itemprop=["']contentUrl["'][^>]+?content=["'](?P<id>[0-9]+)["']
''')
    ITVExtractor.BRIGHTCOVE_URL_TEMPLATE = 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'
    IT

# Generated at 2022-06-14 16:34:57.104983
# Unit test for constructor of class ITVIE
def test_ITVIE():
    from . import fetch_extractor
    fetch_extractor('https://www.itv.com/hub/liar/2a4547a0012')

# Generated at 2022-06-14 16:35:00.563034
# Unit test for constructor of class ITVIE
def test_ITVIE():
	url = 'http://www.itv.com/hub/liar/2a4547a0012'
	ie = ITVIE(url)
	assert ie is not None


# Generated at 2022-06-14 16:35:12.777431
# Unit test for constructor of class ITVIE
def test_ITVIE():
    i = ITVIE()
    assert i._VALID_URL == r'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'
    assert i._GEO_COUNTRIES == ['GB']
    assert i._TESTS[0]['url'] == 'https://www.itv.com/hub/liar/2a4547a0012'

# Generated at 2022-06-14 16:35:14.654255
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    class ITVBTCCIE_test(ITVBTCCIE):
        def __init__(self):
            super(ITVBTCCIE_test,self).__init__()

    ITVBTCCIE_test()

# Generated at 2022-06-14 16:35:16.074666
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE.__init__()

# Generated at 2022-06-14 16:35:19.591125
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:35:26.364060
# Unit test for constructor of class ITVIE
def test_ITVIE():
    constructor = ITVIE('http://www.itv.com/hub/liar/2a4547a0012')
    assert constructor.url == 'http://www.itv.com/hub/liar/2a4547a0012'
    assert constructor.source == 'itv.com'
    assert constructor.video_id == '2a4547a0012'
    assert constructor.source_type == 'itv'
    

# Generated at 2022-06-14 16:35:28.537827
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    # Here is the testing of unit test for constructor of class ITVBTCCIE
    assert ITVBTCCIE('test')

# Generated at 2022-06-14 16:35:31.008029
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    try:
        from .brightcove import BrightcoveNewIE
        BrightcoveNewIE
    except ImportError:
        pass
    else:
        ITVBTCCIE()

# Generated at 2022-06-14 16:35:53.864395
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    instance = ITVBTCCIE('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert instance.url == 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    assert instance.playlist_id == 'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2022-06-14 16:35:56.415937
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ITVBTCCIE('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')

# Generated at 2022-06-14 16:35:58.583522
# Unit test for constructor of class ITVIE
def test_ITVIE():
    try:
        ITVIE()
    except:
        pass
    try:
        ITVIE(downloader=None)
    except:
        pass
    try:
        ITVIE(downloader=None, params=None)
    except:
        pass
    try:
        ITVIE(downloader=None, params=None, ui=None)
    except:
        pass

# Generated at 2022-06-14 16:36:08.489270
# Unit test for constructor of class ITVIE
def test_ITVIE():
    # Lowest level
    url = 'https://www.itv.com/hub/liar/2a4547a0012'
    # ITVIE doesn't accept data-video-playlist-url
    webpage = '<script data-playlist-url=...>...</script>'
    video_id = '2a4547a0012'
    params = {
        'data-video-hmac': '1fcf303c-0c2b-4326-8c99-96fc677dae56',
        'data-video-id': '2a4547a0012',
    }
    def extract_attributes_(html, name, fatal=True):
        assert html == '<div id=video>...</div>'
        assert name == 'video'
        assert fatal
        return params

# Generated at 2022-06-14 16:36:20.245318
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    from .common import get_testdata_files
    from .brightcove import BrightcoveNewIE
    from .itv import ITVIE
    from .adobepass import (
        AdobePassIE,
    ) # unit test for constructor of class ITVBTCCIE
    file_paths = get_testdata_files('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert file_paths
    itv_btcc = ITVBTCCIE()
    itv = ITVIE()
    brightcove_new = BrightcoveNewIE()
    adobepass = AdobePassIE()
    playlist = itv_btcc.extract(file_paths[0])
    entry = playlist.get('entries')[0]


# Generated at 2022-06-14 16:36:23.934772
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    IE = ITVBTCCIE()
    assert IE._VALID_URL
    assert IE._TEST
    assert IE.BRIGHTCOVE_URL_TEMPLATE
    assert IE._real_extract
    assert IE.ie_key()

# Generated at 2022-06-14 16:36:27.355851
# Unit test for constructor of class ITVIE
def test_ITVIE():
    url = 'https://www.itv.com/hub/james-martins-saturday-morning/2a5159a0034'
    AssertISNotNone(re.compile(ITVIE.VALID_URL).match(url))

# Generated at 2022-06-14 16:36:28.895210
# Unit test for constructor of class ITVIE
def test_ITVIE():
    s = ITVIE()
    assert s

# Generated at 2022-06-14 16:36:30.961655
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE('https://www.itv.com/hub/liar/2a4547a0012')


# Generated at 2022-06-14 16:36:31.993610
# Unit test for constructor of class ITVIE
def test_ITVIE():
    #assert ITVIE
    abc = ITVIE()

# Generated at 2022-06-14 16:37:03.461826
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    imp = ITVBTCCIE()
    assert imp.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:37:05.555621
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    # Verify that we can create an instance of class ITVBTCCIE
    assert ITVBTCCIE(None)

# Generated at 2022-06-14 16:37:07.117555
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert isinstance(ie, ITVBTCCIE)

# Generated at 2022-06-14 16:37:15.060624
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE._TEST['url'] == 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch' 
    assert ITVBTCCIE._TEST['info_dict'] == {'id': 'btcc-2018-all-the-action-from-brands-hatch', 'title': 'BTCC 2018: All the action from Brands Hatch'}
    assert ITVBTCCIE._TEST['playlist_mincount'] == 9


# Generated at 2022-06-14 16:37:16.532396
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    c = ITVBTCCIE()
    assert c == c


# Generated at 2022-06-14 16:37:21.029081
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    constructor_input_output = [
        (
            {'url': 'http://www.itv.com/btcc/races', 'args': [], 'note': 'Default url'},
            {'return_value': 'races'}
        )
    ]
    return ITVBTCCIE, constructor_input_output



# Generated at 2022-06-14 16:37:23.690596
# Unit test for constructor of class ITVIE
def test_ITVIE():
    # Given
    itv_ie = ITVIE(ITVIE(), "https://www.itv.com/hub/liar/2a4547a0012", {})
    assert itv_ie is not None

# Generated at 2022-06-14 16:37:24.590582
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert(repr(ITVBTCCIE(None)))

# Generated at 2022-06-14 16:37:26.371628
# Unit test for constructor of class ITVIE
def test_ITVIE():
    # test if ITVIE class could be created by constructor of InfoExtractor
    ie.InfoExtractor.get_info_extractor("ITVIE")

# Generated at 2022-06-14 16:37:27.642546
# Unit test for constructor of class ITVIE
def test_ITVIE():
    info_extractor = ITVIE()
    assert info_extractor is not None


# Generated at 2022-06-14 16:37:58.140304
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    info_extractor = ITVBTCCIE()
    assert info_extractor.IE_NAME == 'itv:btcc'
    assert info_extractor._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:38:00.348593
# Unit test for constructor of class ITVIE
def test_ITVIE():
    itv_ie = ITVIE()
    assert isinstance(itv_ie, ITVIE)


# Generated at 2022-06-14 16:38:06.658009
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()
    ie.url = "https://www.itv.com/hub/liar/2a4547a0012"
    ie.video_id = "2a4547a0012"
    ie.webpage = "ITV sample webpage"
    ie.params = "ITV sample params"
    ie.ios_playlist_url = "ITV sample ios_playlist_url"
    ie.hmac = "ITV sample hmac"
    ie.headers = "ITV sample headers"
    ie.ios_playlist = "ITV sample ios_playlist"
    ie.video_data = "ITV sample video_data"
    ie.ios_base_url = "ITV sample ios_base_url"
    ie.formats = "ITV sample formats"

# Generated at 2022-06-14 16:38:13.419974
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    from ..utils import get_testdata
    content = get_testdata('itv/btcc/list/url.html')
    list = ITVBTCCIE()._get_list(content, "http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch")
    assert list == ['5798348092001', '5797981507001', '5797879050001', '5797707014', '5796642290001']

# Generated at 2022-06-14 16:38:15.431091
# Unit test for constructor of class ITVIE
def test_ITVIE():
    itvIE = ITVIE('http://www.itv.com/hub/the-x-factor/1a1293a0083')
    assert itvIE.__name__ == 'ITV'

# Generated at 2022-06-14 16:38:15.861572
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE

# Generated at 2022-06-14 16:38:18.259756
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
	import unittest
	res = ITVBTCCIE()._real_extract('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
	assert len(res['entries']) == 9
	#print(res)

# Generated at 2022-06-14 16:38:27.779519
# Unit test for constructor of class ITVIE
def test_ITVIE():
    get = ITVIE.init_get(ITVIE())
    info_dict = get('https://www.itv.com/hub/liar/2a4547a0012')
    assert info_dict['id'] == '2a4547a0012'
    assert info_dict['ext'] == 'mp4'
    assert info_dict['title'] == 'Liar - Series 2 - Episode 6'
    info_dict = get('https://www.itv.com/hub/through-the-keyhole/2a2271a0033')
    assert info_dict['id'] == '2a2271a0033'
    assert info_dict['ext'] == 'mp4'
    assert info_dict['title'] == 'Through The Keyhole - Series 5 - Episode 4'

# Generated at 2022-06-14 16:38:28.655014
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE(InfoExtractor())

# Generated at 2022-06-14 16:38:32.226151
# Unit test for constructor of class ITVIE
def test_ITVIE():
	assert ITVIE._VALID_URL == r'(?P<domain>https?://(?:www\.)?)itv\.com/hub/(?P<id>[0-9a-zA-Z]+)'


# Generated at 2022-06-14 16:39:36.666414
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    info_extractor_name = "itv:btcc"
    ip_blocks = ['193.113.0.0/16', '54.36.162.0/23', '159.65.16.0/21']
    url = "http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch"
    yt_url = "http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=5590763771001"
    assert ITVBTCCIE(info_extractor_name, ip_blocks, url).construct_yt_url() == yt_url

# Generated at 2022-06-14 16:39:38.317096
# Unit test for constructor of class ITVIE
def test_ITVIE():
    assert ITVIE()._VALID_URL == ITVIE._VALID_URL



# Generated at 2022-06-14 16:39:39.058634
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE('http://www.itv.com')

# Generated at 2022-06-14 16:39:40.301851
# Unit test for constructor of class ITVIE
def test_ITVIE():
    try:
        ITVIE()
        success = True
    except Exception:
        success = False
    assert success

# Generated at 2022-06-14 16:39:42.870957
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch' 
    assert ITVBTCCIE()._real_extract(url)

# Generated at 2022-06-14 16:39:45.426904
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE.__name__ == 'ITVBTCCIE'
    for v in ITVBTCCIE._TEST.values():
        assert v

# Generated at 2022-06-14 16:39:46.870910
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE(ITVBTCCIE.IE_NAME)

# Generated at 2022-06-14 16:39:50.286456
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:39:52.403120
# Unit test for constructor of class ITVIE
def test_ITVIE():
    # No configuration, default constructor, args = 1
    ITVIE_test = ITVIE(1)



# Generated at 2022-06-14 16:40:01.113050
# Unit test for constructor of class ITVIE
def test_ITVIE():
    url = "https://www.itv.com/hub/this-morning/2a3a38a0001"


# Generated at 2022-06-14 16:42:37.778910
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ITVBTCCIE()._real_extract(
        "http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch")


# Generated at 2022-06-14 16:42:41.888241
# Unit test for constructor of class ITVIE
def test_ITVIE():
    assert ITVIE()._SINGLE_PAGE[0] == {'ie': 'ITVIE'}
    assert ITVIE()._SINGLE_PAGE[1] == {'ie': 'BrightcoveNew'}
    assert ITVIE()._SINGLE_PAGE[2] == ''
    assert ITVIE()._SINGLE_PAGE[3] == ''

# Generated at 2022-06-14 16:42:44.148200
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = "http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch"
    ITVBTCCIE(url)

# Generated at 2022-06-14 16:42:46.628680
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    # URL that has 1 video
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    inst = ITVBTCCIE()
    inst._real_extract(url)

# Generated at 2022-06-14 16:42:48.849217
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'


# Generated at 2022-06-14 16:42:50.029706
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    # Make sure it can be constructed without raising errors
    ITVBTCCIE(InfoExtractor())

# Generated at 2022-06-14 16:42:55.936141
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ievideo = ITVIE('https://www.itv.com/hub/liar/2a4547a0012')
    assert(ievideo.id == '2a4547a0012')
    assert(ievideo.url == 'https://www.itv.com/hub/liar/2a4547a0012')

# Generated at 2022-06-14 16:43:01.361329
# Unit test for constructor of class ITVIE
def test_ITVIE():
    import json
    a = ITVIE(None)

    if a.GEO_BYPASS:
        assert(True)
    else:
        assert(False)

    assert(a.geo_verification_headers()["X-Forwarded-For"] in
        "193.113.0.0/16,54.36.162.0/23,159.65.16.0/21")


# Generated at 2022-06-14 16:43:09.511672
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    class UnitTester(object):

        def fake_download_webpage(url, *args):
            return {
                'url': 'http://www.itv.com/btcc/races/btcc-2014-action-from-brands-hatch',
                'webpage': '<html>'
            }

        # Mocking object of class ITVBTCCIE
        def mock_ITVBTCCIE(self, url):
            self._download_webpage = self.fake_download_webpage
            return ITVBTCCIE(url, 0, 0)
    assert UnitTester().mock_ITVBTCCIE('url')._match_id('url') == 'btcc-2014-action-from-brands-hatch'

# Generated at 2022-06-14 16:43:14.260187
# Unit test for constructor of class ITVIE
def test_ITVIE():
    url = 'https://www.itv.com/hub/liar/2a4547a0012'
    itvIE = ITVIE()
    IE_NAME = itvIE.ie_key()
    assert IE_NAME == 'itv'
    assert itvIE.suitable(url) == True
