

# Generated at 2022-06-14 17:37:58.960118
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ZDFIE('https://www.zdf.de/dokumentation/terra-x/die-magie-der-farben-von-koenigspurpur-und-jeansblau-100.html')

# Generated at 2022-06-14 17:37:59.893512
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ZDFIE()


# Generated at 2022-06-14 17:38:04.588307
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    i = InfoExtractor(None)
    assertequal(i.sdk.__module__, 'zdf_de.compat')
    assertequal(i.sdk.compat_str, str)
    assertequal(i.sdk._compat_kwargs, {})



# Generated at 2022-06-14 17:38:06.539483
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    instance = ZDFChannelIE()
    assert isinstance(instance, ZDFChannelIE)


# Generated at 2022-06-14 17:38:10.644605
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    zdfie = ZDFIE()
    assert zdfie.ie_key() == 'ZDF'
    assert zdfie.ie_key() != ZDFBaseIE.ie_key(), 'Wrong BASE class'


# Generated at 2022-06-14 17:38:21.563765
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    zdfChannelIE = ZDFChannelIE()
    zdfChannelIE._VALID_URL = r'https?://www\.zdf\.de/(?P<id>[^/?#&]+)'

    # first check for case where constructor of 2 parent classes are used
    assert zdfChannelIE.suitable('https://www.zdf.de/sport/das-aktuelle-sportstudio')
    assert not zdfChannelIE.suitable('https://www.zdf.de/filme/spielfilm/der-hauptmann-100.html')

    # second check for case where constructor of 1 parent class is used

# Generated at 2022-06-14 17:38:28.175426
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    assert ZDFChannelIE.suitable('http://www.zdf.de/sport/das-aktuelle-sportstudio')
    assert not ZDFChannelIE.suitable('http://www.zdf.de/dokumentation/planet-e/dokumentation-uebersicht-weitere-dokumentationen-von-planet-e-100.html')

# Generated at 2022-06-14 17:38:34.058535
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    # Test with explicit name
    ZDFChannelIE('ZDFChannel', 'zdf.de')
    # Test with class name
    ZDFChannelIE('ZDFChannel')
    # Test with abbreviated class name
    ZDFChannelIE('ZDF')
    # Test with name of subclass
    ZDFChannelIE('ZDFIE')

# Generated at 2022-06-14 17:38:36.033588
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ie = ZDFBaseIE()
    assert ie._call_api(None, None, None), -1

# Generated at 2022-06-14 17:38:40.241040
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ie = ZDFIE()
    assert ie.NAME != None
    assert ie.IE_NAME != None
    assert ie.ie_key() != None
    assert ie.IE_DESC != None

# Generated at 2022-06-14 17:39:32.199674
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    from ..modules import ZDF
    ZDF_obj = ZDF()
    assert ZDF_obj.ie_key() == 'zdf'
    assert ZDF_obj._GEO_COUNTRIES == ['DE']
    assert ZDF_obj._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')



# Generated at 2022-06-14 17:39:35.649766
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ie = ZDFBaseIE()
    assert isinstance(ie._QUALITIES, tuple)
    assert isinstance(ie._QUALITIES[0], compat_str)
    assert isinstance(ie._GEO_COUNTRIES, list)


# Generated at 2022-06-14 17:39:38.457599
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    # noinspection PyTypeChecker
    ZDFIE()

# Generated at 2022-06-14 17:39:47.106420
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    assert ZDFChannelIE.suitable('https://www.zdf.de/dokumentation/planet-e') == True
    assert ZDFChannelIE.suitable('https://www.zdf.de/filme/taunuskrimi/') == True
    assert ZDFChannelIE.suitable('https://www.zdf.de/filme/taunuskrimi/die-lebenden-und-die-toten-1---ein-taunuskrimi-100.html') == False
    # TODO write tests for get_info()


# Generated at 2022-06-14 17:39:48.067022
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ZDFBaseIE(None, None)



# Generated at 2022-06-14 17:39:49.343225
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    assert isinstance(ZDFIE(), ZDFIE)


# Generated at 2022-06-14 17:39:52.892419
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ie = ZDFBaseIE()
    assert ie is not None
    assert len(ie._GEO_COUNTRIES) is 1 and ie._GEO_COUNTRIES [0] == 'DE'
    assert ie._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')


# Generated at 2022-06-14 17:39:54.470724
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ZDFIE()


# Generated at 2022-06-14 17:39:58.646291
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    assert(ZDFIE.get_params == NO_DEFAULT)
    assert(ZDFIE.handle_error == NO_DEFAULT)
    assert(ZDFIE.get_info_dicts == NO_DEFAULT)

    ZDFIE_default = ZDFIE()



# Generated at 2022-06-14 17:40:03.176188
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    from youtube_dl.extractor import YoutubeDL
    from youtube_dl.downloader.common import FileDownloader
    from youtube_dl.utils import DateRange

    ydl = YoutubeDL({'outtmpl': '%(id)s%(ext)s'})
    ydl.add_default_info_extractors()
    ie = ydl._ies[ZDFBaseIE.ie_key()]()
    ie._downloader = FileDownloader(ydl)
    ie.download = ydl.download
    ie.report_warning = ydl.report_warning
    ie.report_error = ydl.report_error
    ie.params = ydl.params
    ie.to_screen = ydl.to_screen
    ie.get_iframe_url = None
    ie.set_downloader = ydl.set_

# Generated at 2022-06-14 17:41:49.542886
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    from .zdf import ZDFIE
    from .zdf_mediathek import ZDFMediathekIE
    from .tagesschau import TagesschauIE
    zdf = ZDFIE()
    zdf_mediathek = ZDFMediathekIE()
    tagesschau = TagesschauIE()
    assert zdf.ie_key() == 'ZDF'
    assert zdf_mediathek.ie_key() == 'ZDFMediathek'
    assert tagesschau.ie_key() == 'Tagesschau'
# End of test_ZDFBaseIE


# Generated at 2022-06-14 17:41:50.259620
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ZDFIE()

# Generated at 2022-06-14 17:42:00.410487
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    # Class object testing
    assert hasattr(ZDFIE, '_download_json') and callable(getattr(ZDFIE, '_download_json', None))
    assert hasattr(ZDFIE, '_TESTS')
    assert hasattr(ZDFIE, 'ie_key') and callable(getattr(ZDFIE, 'ie_key', None))
    assert hasattr(ZDFIE, 'suitable') and callable(getattr(ZDFIE, 'suitable', None))
    assert hasattr(ZDFIE, '_extract_subtitles') and callable(getattr(ZDFIE, '_extract_subtitles', None))
    assert hasattr(ZDFIE, '_extract_mobile') and callable(getattr(ZDFIE, '_extract_mobile', None))


# Generated at 2022-06-14 17:42:08.901639
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    test_instance = ZDFBaseIE()
    assert(test_instance._GEO_COUNTRIES == ['DE'])
#   assert(test_instance._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd'))
#   assert(test_instance._call_api(url, video_id, item, api_token, referrer) == 
#          test_instance._download_json(url, video_id, 'Downloading JSON %s' % item, headers=headers))
#   assert(_extract_subtitles(src) == subtitles)
#   assert(test_instance._extract_format(video_id, formats, format_urls, meta) == None)
#   assert(test_instance._extract_ptmd(ptmd_url, video_id, api_token,

# Generated at 2022-06-14 17:42:13.617198
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    # pylint: disable=import-outside-toplevel
    from .common import partial
    from .test_zdf import ZDFIE
    from .test_youtube import YoutubePlaylistIE
    url = 'https://www.zdf.de/dokumentation/planet-e'
    assert partial(ZDFChannelIE.suitable, url)()
    assert partial(ZDFIE.suitable, url)() == False
    assert partial(YoutubePlaylistIE.suitable, url)() == False

# Generated at 2022-06-14 17:42:23.767529
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    url = 'https://www.zdf.de/politik/frontal-21'
    playlist_id = 'frontal-21'
    webpage = """
    <div class="module__headline">
    <h1 id="main-title" class="headline__primary js-plusbar-title" data-plusbar-title="Frontal 21">
        Frontal 21
    </h1>
    </div>
    """
    zdf_channel_ie = ZDFChannelIE(ZDFChannelIE.suitable(url))
    zdf_channel_ie._download_webpage = lambda url, name: webpage
    info_dict = zdf_channel_ie._real_extract(url)
    assert info_dict['id'] == playlist_id
    assert info_dict['title'] == 'Frontal 21'


# Generated at 2022-06-14 17:42:27.641589
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    assert ZDFBaseIE._GEO_COUNTRIES == ['DE']
    assert ZDFBaseIE._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')



# Generated at 2022-06-14 17:42:36.984950
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    assert ZDFIE()._real_extract(
        'https://www.zdf.de/politik/phoenix-sendungen/die-gesten-der-maechtigen-100.html'
    ) == ZDFBaseIE._real_extract(
        None,
        'https://www.zdf.de/politik/phoenix-sendungen/die-gesten-der-maechtigen-100.html'
    )[0]

# Generated at 2022-06-14 17:42:46.677275
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    valid_url = "https://www.zdf.de/dokumentation/planet-e"
    invalid_url = "https://www.zdf.de/filme/taunuskrimi/die-lebenden-und-die-toten-1---ein-taunuskrimi-100.html"
    assert ZDFChannelIE.suitable(valid_url)
    assert ZDFChannelIE.suitable(invalid_url) == False
    zdf_channel = ZDFChannelIE()
    assert zdf_channel._match_id(valid_url) == "planet-e"
    zdf_channel._download_webpage = lambda url, video_id: ""
    zdf_channel._parse_json = lambda *args: {}
    zdf_channel._call_api = lambda *args: {}


# Generated at 2022-06-14 17:42:51.344831
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    assert ZDFIE({}).ie_key() == 'ZDF'


# Generated at 2022-06-14 17:45:08.154943
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    url = 'https://www.zdf.de/sport/das-aktuelle-sportstudio'
    ZDFChannelIE().suitable(url)
    ZDFChannelIE()._real_extract(url)


# Generated at 2022-06-14 17:45:15.933056
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    try:
        from unittest import mock  # python 3
    except ImportError:
        import mock  # python 2

    test_ZDFIE.patcher = mock.patch('zdf_downloader.InfoExtractor.geo_verification_headers', return_value={})
    test_ZDFIE.patcher.start()

    ZDFIE('zdf_downloader')
    test_ZDFIE.patcher.stop()

# Generated at 2022-06-14 17:45:17.816121
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    assert_raises_regex(ExtractorError, 'SCRIPT_URL must not be empty', ZDFChannelIE, '', '')

# Generated at 2022-06-14 17:45:20.907906
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    assert ZDFBaseIE._GEO_COUNTRIES == ['DE']
    assert ZDFBaseIE._QUALITIES == ('auto','low','med','high','veryhigh','hd')


# Generated at 2022-06-14 17:45:26.813418
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    """
    unit test to test the constructor of class ZDFChannelIE
    """
    url = 'https://www.zdf.de/sport/das-aktuelle-sportstudio'

    assert not ZDFIE.suitable(url)
    assert ZDFChannelIE.suitable(url)



# Generated at 2022-06-14 17:45:27.908272
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ZDFIE()


# Generated at 2022-06-14 17:45:33.794607
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    inst = ZDFBaseIE(ZDFIE.ie_key(), ZDFIE.ie_key())
    assert inst._GEO_COUNTRIES == ['DE']
    assert inst._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')


# Generated at 2022-06-14 17:45:36.052518
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ie = ZDFBaseIE()
    assert ie._GEO_COUNTRIES == ['DE']
    assert ie._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')


# Generated at 2022-06-14 17:45:42.732999
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    assert(ZDFIE(ZDFBaseIE)._VALID_URL == ZDFBaseIE._VALID_URL)
    assert(ZDFIE(ZDFBaseIE)._TESTS == ZDFBaseIE._TESTS)
    assert(ZDFIE(ZDFBaseIE)._GEO_COUNTRIES == ZDFBaseIE._GEO_COUNTRIES)
    assert(ZDFIE(ZDFBaseIE)._QUALITIES == ZDFBaseIE._QUALITIES)
    assert(ZDFIE(ZDFBaseIE)._call_api(ZDFBaseIE, None, None, None) == ['ZDFBaseIE'])
    assert(ZDFIE(ZDFBaseIE)._extract_subtitles(None) == ['ZDFBaseIE'])

# Generated at 2022-06-14 17:45:53.984703
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    # Test for mobile URL
    result = ZDFIE._extract_mobile("2a0a8aae-3ddc-4a63-ba62-b9c923fcdcec")
    assert 'formats' in result

    # Test for regular URL
    url = 'https://www.zdf.de/nachrichten/heute/zdfheute-sendung-vom-26-01-2017-100.html'
    webpage = {
        'url': url,
        'title': 'ZDFheute sendung vom 26.01.2017',
        '_type': 'html_webpage',
    }