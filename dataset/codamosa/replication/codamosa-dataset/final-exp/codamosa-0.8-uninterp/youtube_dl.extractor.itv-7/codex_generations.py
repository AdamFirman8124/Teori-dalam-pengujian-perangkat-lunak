

# Generated at 2022-06-14 16:34:46.721902
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ITVBTCCIE(InfoExtractor())._real_extract('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')

# Generated at 2022-06-14 16:34:48.455258
# Unit test for constructor of class ITVIE
def test_ITVIE():
    t = ITVIE()
    assert t is not None


# Generated at 2022-06-14 16:34:52.511391
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    itvbtccie = ITVBTCCIE("http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch")
    assert isinstance(itvbtccie, ITVBTCCIE)

# Generated at 2022-06-14 16:35:00.096700
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()

# Generated at 2022-06-14 16:35:12.419284
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    e = ITVBTCCIE()
    assert e.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'
    assert e._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:35:13.468761
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    i = ITVBTCCIE()

# Generated at 2022-06-14 16:35:17.349418
# Unit test for constructor of class ITVIE
def test_ITVIE():
    instance = ITVIE('https://www.itv.com/hub/james-martins-saturday-morning/2a5159a0034')
    assert instance

# Generated at 2022-06-14 16:35:21.887305
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE == (
        'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'
    )

# Generated at 2022-06-14 16:35:23.985392
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE("http://www.itv.com/hub/liar/2a4547a0012")

# Generated at 2022-06-14 16:35:28.279613
# Unit test for constructor of class ITVIE
def test_ITVIE():
    # Unit-tests/smoke tests.
    # The ITVIE constructor is called by ITVIE and ITVBTCCIE,
    # so we test all the code in one place.
    assert ITVIE._download_webpage is ITVBTCCIE._download_webpage

# Generated at 2022-06-14 16:35:45.430325
# Unit test for constructor of class ITVIE
def test_ITVIE():
    result = ITVIE().url_result('http://www.itv.com/hub/jekyll-and-hyde/2a4547a0012')
    result == ITVIE().extract(result.entries[0].url)

# Generated at 2022-06-14 16:35:56.244977
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    IE = ITVBTCCIE()

    # Test an example url with a single video
    url = 'https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    assert IE.url_result(url) == {
        '_type': 'url',
        'url': 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=5905093893001',
        'ie_key': 'BrightcoveNew',
        'video_id': '5905093893001',
    }

    # Test an example url with multiple videos

# Generated at 2022-06-14 16:35:58.598988
# Unit test for constructor of class ITVIE
def test_ITVIE():
    new_obj = ITVIE()
    assert new_obj.__class__.__name__ == ITVIE.__name__

# Generated at 2022-06-14 16:36:03.228444
# Unit test for constructor of class ITVIE
def test_ITVIE():
    assert ITVIE._VALID_URL

    # Test the test
    assert ITVIE._TESTS[0]['url'] == 'https://www.itv.com/hub/liar/2a4547a0012'
    assert ITVIE._TESTS[0]['info_dict']['id'] == '2a4547a0012'

# Generated at 2022-06-14 16:36:07.663553
# Unit test for constructor of class ITVIE
def test_ITVIE():
    # For debugging purpose only
    video_id = '2a4547a0012'
    url = 'https://www.itv.com/hub/liar/2a4547a0012'
    ie = ITVIE()
    try:
        ie._download_webpage(url, video_id)
    except:
        pass

# Generated at 2022-06-14 16:36:08.617781
# Unit test for constructor of class ITVIE
def test_ITVIE():
    assert ITVIE.__name__ == 'ITVIE'

# Generated at 2022-06-14 16:36:14.742506
# Unit test for constructor of class ITVIE
def test_ITVIE():
    # Test for correct parsing of id from ITV url
    url = 'http://www.itv.com/hub/liar/2a4547a0012'
    instance = ITVIE()
    assert instance.ie_key() == 'ITV'
    assert re.match(instance._VALID_URL, url) is not None
    assert instance._match_id(url) == '2a4547a0012'

# Generated at 2022-06-14 16:36:26.153349
# Unit test for constructor of class ITVIE

# Generated at 2022-06-14 16:36:31.051521
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    class_ITVBTCCIE_instance = ITVBTCCIE("", "", "")
    assert class_ITVBTCCIE_instance.BRIGHTCOVE_URL_TEMPLATE == "http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s"

# Generated at 2022-06-14 16:36:31.726242
# Unit test for constructor of class ITVIE
def test_ITVIE():
    obj = ITVIE()

# Generated at 2022-06-14 16:37:07.880462
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    from cStringIO import StringIO
    from .test_brightcove import BrightcoveNewTest

    sample_url = 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=5856398068001'
    btcc_url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'

    def _download_webpage(url, *args):
        if url != btcc_url:
            raise ValueError(url)
        return '<div class="artwork" data-video-id="5856398068001"></div>'
    InfoExtractor._download_webpage = _download_webpage


# Generated at 2022-06-14 16:37:11.140363
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    return ITVBTCCIE('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')

# Generated at 2022-06-14 16:37:12.404864
# Unit test for constructor of class ITVIE
def test_ITVIE():
    pass


# Generated at 2022-06-14 16:37:14.434221
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE('https://www.itv.com/hub/liar/2a4547a0012')

# Generated at 2022-06-14 16:37:24.130368
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    itvbtccie = ITVBTCCIE('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert itvbtccie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'
    assert itvbtccie._VALID_URL == 'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:37:26.691424
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    """Verify if the constructor methods of ITVBTCCIE class has been defined properly"""
    assert ITVBTCCIE.__bases__[0].__name__ == 'InfoExtractor'
    o = ITVBTCCIE(None)
    fields_dict = ITVBTCCIE.__init__.__func__.__code__.co_varnames
    for field in fields_dict:
        assert hasattr(o, field)

# Generated at 2022-06-14 16:37:28.679810
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:37:31.727676
# Unit test for constructor of class ITVIE
def test_ITVIE():
    iTVIE = ITVIE("https://www.itv.com/hub/liar/2a4547a0012")
    iTVIE._real_extract("https://www.itv.com/hub/liar/2a4547a0012")

# Generated at 2022-06-14 16:37:34.097889
# Unit test for constructor of class ITVIE
def test_ITVIE():
    test = ITVIE()
    assert test._VALID_URL == r'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'


# Generated at 2022-06-14 16:37:35.612775
# Unit test for constructor of class ITVIE
def test_ITVIE():
    itvie = ITVIE(None)
    assert itvie != None

# Generated at 2022-06-14 16:38:43.067754
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE = 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    playlist_id = 'btcc-2018-all-the-action-from-brands-hatch'
    video_id = '5901253505001'

# Generated at 2022-06-14 16:38:54.336030
# Unit test for constructor of class ITVIE
def test_ITVIE():
    video_urls = [
        "https://www.itv.com/hub/dancing-on-ice/2a1947a0015",
        "https://www.itv.com/hub/dancing-on-ice/2a1947a0015",
        "https://www.itv.com/hub/dancing-on-ice/2a1947a0015",
        "https://www.itv.com/hub/dancing-on-ice/2a1947a0015",
    ]

    for video_url in video_urls:
        print("\n" + video_url + "\n")
        itv = ITVIE()
        test_info_dict = itv._real_extract(video_url)
        print(test_info_dict)


# Generated at 2022-06-14 16:39:00.322949
# Unit test for constructor of class ITVIE
def test_ITVIE():
    test_ITVIE = ITVIE(1)
    assert test_ITVIE.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:39:10.632093
# Unit test for constructor of class ITVIE
def test_ITVIE():
    instance = ITVIE({})

    assert instance._GEO_COUNTRIES == ['GB']

# Generated at 2022-06-14 16:39:13.286064
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    """
    Simple test of ITVBTCCIE constructor
    """
    assert ITVBTCCIE('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')

# Generated at 2022-06-14 16:39:21.879327
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'
    assert ie._TESTS[0]['url'] == 'https://www.itv.com/hub/liar/2a4547a0012'
    assert ie._TESTS[0]['info_dict']['id'] == '2a4547a0012'
    assert ie._TESTS[0]['params']['skip_download'] == True


# Generated at 2022-06-14 16:39:24.265669
# Unit test for constructor of class ITVIE
def test_ITVIE():
    """
    Unit test for constructor of class ITVIE
    """
    assert ITVIE(InfoExtractor)._VALID_URL == ITVIE._VALID_URL


# Generated at 2022-06-14 16:39:27.736526
# Unit test for constructor of class ITVIE
def test_ITVIE():
    from . import ITVIE as cls
    inst = cls()
    assert hasattr(inst, '_download_json')
    assert hasattr(inst, '_download_webpage')

# Generated at 2022-06-14 16:39:31.084676
# Unit test for constructor of class ITVIE
def test_ITVIE():
	url='https://www.itv.com/hub/the-owner/2a4621a0013'
	video_object = ITVIE()
	video_object._real_extract(url)


# Generated at 2022-06-14 16:39:37.695526
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    expected_video_id = '5834368913001'
    ITVBTCCIE(ITVBTCCIE.create_ie()).url_result(url)
    video_url = ITVBTCCIE(ITVBTCCIE.create_ie()).url_result(url).url
    assert expected_video_id in video_url

# Generated at 2022-06-14 16:42:16.661951
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'
    assert ie.IE_NAME == 'itv'
    assert ie.GEO_COUNTRIES == ['GB']
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:42:19.217029
# Unit test for constructor of class ITVIE
def test_ITVIE():
    assert ITVIE._TESTS[0]['info_dict']['id'] == '2a4547a0012'
    assert ITVIE._TESTS[0]['params']['skip_download'] is True

# Generated at 2022-06-14 16:42:27.061729
# Unit test for constructor of class ITVIE
def test_ITVIE():
    constructor = ITVIE('ITVIE')

# Generated at 2022-06-14 16:42:36.880427
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    test = ITVBTCCIE('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert test._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert test._TEST.get('url') == 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    assert test._TEST.get('info_dict').get('id') == 'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2022-06-14 16:42:44.800004
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    info_extractor = ITVBTCCIE()
    assert info_extractor._VALID_URL == r'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert info_extractor._TEST == {
        'url': 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch',
        'info_dict': {
            'id': 'btcc-2018-all-the-action-from-brands-hatch',
            'title': 'BTCC 2018: All the action from Brands Hatch',
        },
        'playlist_mincount': 9,
    }
    assert info_extractor.BRIGHTCOVE_URL_T

# Generated at 2022-06-14 16:42:50.029706
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    result = ITVBTCCIE()._real_extract(ITVBTCCIE()._TEST['url'])
    assert result is not None
    assert result['id'] == ITVBTCCIE()._TEST['info_dict']['id']
    assert result['title'] == ITVBTCCIE()._TEST['info_dict']['title']
    assert len(result['entries']) >= ITVBTCCIE()._TEST['playlist_mincount']

# Generated at 2022-06-14 16:42:53.124534
# Unit test for constructor of class ITVIE
def test_ITVIE():
    assert re.search(ITVIE._VALID_URL, 'http://www.itv.com/hub/liar/2a4547a0012')


# Generated at 2022-06-14 16:42:54.102354
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ITVBTCCIE()

# Generated at 2022-06-14 16:42:55.991740
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE.ie_key() == "ITVBTCC"

# Generated at 2022-06-14 16:42:57.501950
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE._TEST['url'] == ITVBTCCIE._VALID_URL