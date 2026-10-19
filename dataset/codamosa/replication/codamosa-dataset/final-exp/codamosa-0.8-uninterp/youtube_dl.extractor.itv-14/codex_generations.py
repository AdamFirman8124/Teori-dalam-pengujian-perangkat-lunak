

# Generated at 2022-06-14 16:34:43.593935
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ITVBTCCIE("http://www.itv.com/btcc/ho-ho-honda-hatch-on-top-again")

# Generated at 2022-06-14 16:34:48.676343
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    video = ITVBTCCIE()
    assert video.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'



# Generated at 2022-06-14 16:34:50.168277
# Unit test for constructor of class ITVIE
def test_ITVIE():
    x = ITVIE()
    assert isinstance(x, ITVIE)

# Generated at 2022-06-14 16:34:51.229467
# Unit test for constructor of class ITVIE
def test_ITVIE():
    assert ITVIE is not None

# Generated at 2022-06-14 16:34:59.513117
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    from . import util
    from .common import SocksProxyServer
    from .socks import Socks5Auth
    from .devtools import run_server

    def _run_proxy_server(h, p):
        SocksProxyServer(
            h, p, socket_options=[
                Socks5Auth('u', 'p'),
            ]).serve_forever()


# Generated at 2022-06-14 16:35:00.150108
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE()

# Generated at 2022-06-14 16:35:00.933154
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ITVIE()

# Generated at 2022-06-14 16:35:04.306595
# Unit test for constructor of class ITVIE
def test_ITVIE():
    """
    This video is used for testing the ITVIE constructor
    """
    ITVIE('https://www.itv.com/hub/liar/2a4547a0012')

# Generated at 2022-06-14 16:35:11.938935
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()
    assert ie.IE_NAME == 'itv'
    assert ie.IE_DESC == 'ITV'
    assert ie._VALID_URL == ITVIE._VALID_URL
    assert ie._GEO_COUNTRIES == ITVIE._GEO_COUNTRIES
    assert ie._TESTS == ITVIE._TESTS
    assert ie.BRIGHTCOVE_URL_TEMPLATE == ITVIE.BRIGHTCOVE_URL_TEMPLATE


# Generated at 2022-06-14 16:35:13.354279
# Unit test for constructor of class ITVIE
def test_ITVIE():
    assert ITVIE({})._SITE_NAME == 'ITV'

# Generated at 2022-06-14 16:35:28.999594
# Unit test for constructor of class ITVIE
def test_ITVIE():
    assert ITVIE._VALID_URL is not None
    example_object_1 = ITVIE(ITVIE._VALID_URL)
    print(example_object_1)

test_ITVIE()

# Generated at 2022-06-14 16:35:30.687378
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    a = ITVBTCCIE()
    assert a._json_ld(None, None) is None

# Generated at 2022-06-14 16:35:34.840782
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    ie = ITVBTCCIE()
    info = ie.extract(url)
    assert info['playlist'][0]['id'] == '5824128968001'

# Generated at 2022-06-14 16:35:41.437934
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    playlist_id = ITVBTCCIE._match_id(url)
    webpage = ITVBTCCIE._download_webpage(url, playlist_id)


# Generated at 2022-06-14 16:35:44.123586
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE._TEST['url'] == ITVBTCCIE._VALID_URL % ITVBTCCIE._TEST['info_dict']['id']

# Generated at 2022-06-14 16:35:45.845784
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ibi= ITVIE()
    return ibi;

# Generated at 2022-06-14 16:35:48.149965
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ITVBTCCIE().run_test('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')

# Generated at 2022-06-14 16:35:59.410453
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    url = url_or_none('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert url == 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    assert ITVBTCCIE._VALID_URL == 'https?://(?:www\.)?itv\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    assert ITVBTCCIE.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:36:02.526229
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    from . import ITVBTCCIE
    ITVBTCCIE(ITVBTCCIE._downloader, ITVBTCCIE._VALID_URL)._real_initialize(ITVBTCCIE._VALID_URL)

# Generated at 2022-06-14 16:36:09.356736
# Unit test for constructor of class ITVIE
def test_ITVIE():
    # See https://github.com/ytdl-org/youtube-dl/pull/20234#issuecomment-701864503
    # for the request for this test
    for url in [
        'https://www.itv.com/hub/catch-up/2a4547a0012/player',
        'https://www.itv.com/itvplayer/catch-up/2a4547a0012/player',
    ]:
        ie = ITVIE()
        assert ie.suitable(url)
        assert ie.ie_key() == 'ITV'

# Generated at 2022-06-14 16:36:38.872300
# Unit test for constructor of class ITVIE
def test_ITVIE():
    url = 'https://www.itv.com/hub/liar/2a4547a0012'
    ie = ITVIE('')
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'

# Generated at 2022-06-14 16:36:42.757300
# Unit test for constructor of class ITVIE
def test_ITVIE():
    info_extractor = ITVIE()
    info_extractor.extract('https://www.itv.com/hub/liar/2a4547a0012')

# Generated at 2022-06-14 16:36:47.119782
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ive = ITVIE(ITVIE._downloader)
    assert ive
    assert ive._URL_TEMPLATE == "https://www.itv.com/hub/%s/%s"
    assert ive._VALID_URL == ITVIE._VALID_URL

# Generated at 2022-06-14 16:36:51.178880
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    i = ITVBTCCIE()
    video_id = '5886611235001'
    assert i.BRIGHTCOVE_URL_TEMPLATE % video_id == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=5886611235001'



# Generated at 2022-06-14 16:36:53.086447
# Unit test for constructor of class ITVIE
def test_ITVIE():
    # Test that the url can be successfully constructed from the valid url passed into the constructor
    url = "https://www.itv.com/hub/liar/2a4547a0012"
    ITV_VIDEO_URL = ITVIE(url).video_url
    assert url == ITV_VIDEO_URL


# Generated at 2022-06-14 16:36:57.668953
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    import sys
    try:
        if sys.version_info.major >= 3:
            import unittest.mock as mock
            raise mock.patch('unittest.TestCase.assertIn', side_effect=AssertionError)
        else:
            import mock
            raise mock.patch('unittest.TestCase.assertIn', side_effect=AssertionError)
    except AssertionError:
        pass
    except (NameError, ImportError) as e:
        raise unittest.SkipTest(e)

# Generated at 2022-06-14 16:36:58.971595
# Unit test for constructor of class ITVIE
def test_ITVIE():
    try:
        ITVIE()
    except Exception as e:
        # Assert that no exceptions are raised..
        print(e)
        assert(False)

# Generated at 2022-06-14 16:37:05.079596
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    IE = ITVBTCCIE(ITVBTCCIE._downloader)._real_extract
    result = IE(ITVBTCCIE._TEST['url'])
    wanted = ITVBTCCIE._TEST['info_dict']
    assert result['title'] == wanted['title']
    assert result['id'] == wanted['id']
    assert len(result['entries']) == ITVBTCCIE._TEST['playlist_mincount']

# Generated at 2022-06-14 16:37:05.995414
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ITVBTCCIE()

# Generated at 2022-06-14 16:37:08.441088
# Unit test for constructor of class ITVIE
def test_ITVIE():
    """
    The constructor of the base class InfoExtractor only accepts a string.
    Thus the ITVIE class cannot be tested.
    """
    assert ITVIE is not None

# Generated at 2022-06-14 16:38:03.802482
# Unit test for constructor of class ITVIE
def test_ITVIE():
    hex_id = '8d88e0016b'
    video_url = 'http://www.itv.com/hub/%s' % hex_id
    ext = ITVIE()
    ext._download_json = lambda *a: {'Playlist': {'Video': {}}}
    ext._real_extract(video_url)
    assert ext._download_json.call_count == 1

# Generated at 2022-06-14 16:38:09.788114
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    #assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:38:13.270711
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    t = ITVBTCCIE()
    assert ITVBTCCIE._TEST['info_dict'] == t._real_extract(
        ITVBTCCIE._TEST['url'])['entries'][0]['_type']

# Generated at 2022-06-14 16:38:15.800520
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'

# Generated at 2022-06-14 16:38:17.243636
# Unit test for constructor of class ITVIE
def test_ITVIE():
    url = 'https://www.itv.com/hub/liar/2a4547a0012'
    assert ITVIE(URLIE())._match_id(url) is not None

# Generated at 2022-06-14 16:38:22.152044
# Unit test for constructor of class ITVIE
def test_ITVIE():
    assert(json.loads('{"objectID": "2a4547a0012", "recordType": "Episode", "title": "Liar - Series 2 - Episode 6", "description": "md5:d0f91536569dec79ea184f0a44cca089", "tags": {"tag": [{"value": "Liar", "type": "Genre"}, {"value": "Liar Series 2", "type": "Series"}]}, "seriesNumber": 2, "episodeNumber": 6}') == ITVIE()._json_ld('Liar - Series 2 - Episode 6', 'md5:d0f91536569dec79ea184f0a44cca089', 'Liar', 2, 6, '2a4547a0012'))

# Generated at 2022-06-14 16:38:25.033124
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    instance = ITVBTCCIE()
    expected_message = "Constructor of ITVBTCCIE() took 0.00 seconds"
    assert expected_message in instance._downloader.report_warning.call_args[0][0]

# Generated at 2022-06-14 16:38:26.408243
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    assert ITVBTCCIE._TEST['url'] == ITVBTCCIE(None)._TEST['url']

# Generated at 2022-06-14 16:38:31.493095
# Unit test for constructor of class ITVBTCCIE

# Generated at 2022-06-14 16:38:33.705657
# Unit test for constructor of class ITVIE
def test_ITVIE():
    url = 'https://www.itv.com/hub/liar/2a4547a0012'
    ITVIE().suitable(url)

# Generated at 2022-06-14 16:40:27.498928
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?itv\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'

# Generated at 2022-06-14 16:40:28.996873
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    class ITVBTCCIE_test(ITVBTCCIE):
        pass
    # This should be the constructor of the inherited class
    assert ITVBTCCIE_test

# Generated at 2022-06-14 16:40:31.895736
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    instance = ITVBTCCIE('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert isinstance(instance, ITVBTCCIE)

# Generated at 2022-06-14 16:40:36.098673
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    video_urls = ['http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=5827729810001']
    for url in video_urls:
        ITVBTCCIE(url)

# Generated at 2022-06-14 16:40:46.649704
# Unit test for constructor of class ITVBTCCIE

# Generated at 2022-06-14 16:40:48.878103
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    video = ITVBTCCIE().url_result('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert video is not None

# Generated at 2022-06-14 16:40:54.248183
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s'
    assert ie.BRIGHTCOVE_URL_TEMPLATE
    assert ie.BRIGHTCOVE_URL_TEMPLATE

# Generated at 2022-06-14 16:40:55.535913
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()
    # TODO: Fix testing of constructed class

# Generated at 2022-06-14 16:40:58.063323
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    constructor_test(ITVBTCCIE, ["http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch"])



# Generated at 2022-06-14 16:40:59.114166
# Unit test for constructor of class ITVIE
def test_ITVIE():
    from .itv import ITVIE
    assert ITVIE
