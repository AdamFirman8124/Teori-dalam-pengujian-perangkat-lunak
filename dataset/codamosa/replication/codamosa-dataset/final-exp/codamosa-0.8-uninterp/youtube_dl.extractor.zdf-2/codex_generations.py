

# Generated at 2022-06-14 17:37:55.666535
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ie = ZDFBaseIE()
    # Test whether class can be constructed
    assert isinstance(ie, InfoExtractor)
    # Test if class variables exist
    assert ie._GEO_COUNTRIES == ['DE']
    assert ie._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')



# Generated at 2022-06-14 17:38:02.039259
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ie = ZDFIE()
    result = ie.suitable(ie.ie_key())
    assert result is True, 'test_ZDFIE should return True, but returned ' + str(result) + '!!!'
    test_result = ie.get_loader()
    assert test_result.func.__name__ == 'load_jsmodule'
    assert test_result.name == 'ZDF'



# Generated at 2022-06-14 17:38:14.763687
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    from six import BytesIO
    from youtube_dl.utils import update_url_query
    from youtube_dl.compat import compat_urllib_request

    test_data = [
        ('https://www.zdf.de/sport/das-aktuelle-sportstudio', b'window.zdf.vjConfig = {', 'das aktuelle sportstudio'),
        ('https://www.zdf.de/dokumentation/planet-e', b'var planetE = {', 'planet e.'),
        ('https://www.zdf.de/filme/taunuskrimi', b'<h1 class="headline"', 'Taunuskrimi'),
    ]

# Generated at 2022-06-14 17:38:18.265262
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    assert ZDFBaseIE._GEO_COUNTRIES == ['DE']
    assert ZDFBaseIE._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')


# Generated at 2022-06-14 17:38:19.735316
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    test_player_object = InfoExtractor(ZDFBaseIE);
    assert test_player_object is not None


# Generated at 2022-06-14 17:38:25.062723
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    ie = ZDFChannelIE()
    assert ie.suitable(ZDFChannelIE._VALID_URL)
    assert ie.suitable(ZDFIE._VALID_URL)


# Generated at 2022-06-14 17:38:26.505202
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    extractor = ZDFIE()


# Generated at 2022-06-14 17:38:38.322775
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    """
    Returns:
        Unit test function
    """

    def test(case_url, channel_id, channel_title, min_count_entries):
        """
        Args:
            case_url (string): URL of test case
            channel_id (string): ID of channel
            channel_title (string): Title of channel
            min_count_entries (int): Minimal number of entries, that should be in the play list
        Returns:
            Unit test function
        """

        test_case_func = FuncTestCase(lambda: ZDFChannelIE._real_extract(
            ZDFChannelIE(), case_url), expect_return=None)
        test_case_func += FuncTestCase(lambda: test_case_func.result['id'], expect_return=channel_id)
        test_case_func

# Generated at 2022-06-14 17:38:42.626869
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    url = 'https://www.zdf.de/sport/das-aktuelle-sportstudio'
    ie = ZDFChannelIE.suitable(url)
    assert ie == ZDFChannelIE



# Generated at 2022-06-14 17:38:44.692382
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    new_ZDFBaseIE = ZDFBaseIE()
    return new_ZDFBaseIE


# Generated at 2022-06-14 17:39:13.948592
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    assert ZDFChannelIE._VALID_URL == '(?:https?://)?(?:www\.)?zdf\.de/(?:[^/]+/)*(?P<id>[^/?#&]+)'


# Generated at 2022-06-14 17:39:22.862597
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    from .test import get_testcases
    from .zdf import ZDFIE
    class_ = ZDFChannelIE
    for case in get_testcases(ZDFIE, suffix='url'):
        url, expected_title = case
        o = class_(url)
        assert o.IE_NAME == 'zdf:channel'
        assert o.ie_key() == 'ZDFChannel'
        assert o.SUITABLE_URLS == [class_._VALID_URL]
        assert o.get_url() == url
        assert o.get_channel_id() == 'unknown'
        assert o.get_channel_title() == 'unknown'
        assert o.get_channel_link() == url
        assert o.get_channel_description() == None



# Generated at 2022-06-14 17:39:25.813346
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    # pylint: disable=protected-access
    assert (ZDFBaseIE._GEO_COUNTRIES == ['DE'])
    assert (ZDFBaseIE._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd'))


# Generated at 2022-06-14 17:39:30.060858
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    obj = ZDFIE()
    assert isinstance(obj, ZDFBaseIE)
    assert str(ZDFBaseIE) == '<class \'youtube_dl.extractor.zdf.ZDFBaseIE\'>'



# Generated at 2022-06-14 17:39:39.044516
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    assert ZDFChannelIE._get_collection(0) == 'zdf-collection-default'
    assert ZDFChannelIE._get_collection(20) == 'zdf-collection-default'
    assert ZDFChannelIE._get_collection(21) == 'zdf-collection-default'
    assert ZDFChannelIE._get_collection(22) == 'zdf-collection-default'
    assert ZDFChannelIE._get_collection(23) == 'zdf-collection-23'
    assert ZDFChannelIE._get_collection(24) == 'zdf-collection-24'
    assert ZDFChannelIE._get_collection(25) == 'zdf-collection-25'

# Generated at 2022-06-14 17:39:42.338864
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ie = ZDFIE()
    assert ie.ie_key() == 'zdf'
    assert ie.working == False
    assert ie.extract('') == None


# Generated at 2022-06-14 17:39:43.029276
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    ZDFBaseIE()



# Generated at 2022-06-14 17:39:44.658993
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    z=ZDFIE()
    print(z)


# Generated at 2022-06-14 17:39:47.820904
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    zdfie = ZDFIE("test zdf", "test zdf", ZDFIE._VALID_URL, ZDFIE._TESTS, {}, {}, {}, {})
    assert zdfie


# Generated at 2022-06-14 17:39:51.981069
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    # this part is not really a test, but it ensures that the code is run
    # (and if an error occurs, the test will fail)
    zdfbase_ie = ZDFBaseIE(ZDFIE(), 'https://zdf.de/dummy')
    # this part is really a test
    assert zdfbase_ie._GEO_COUNTRIES == ['DE']



# Generated at 2022-06-14 17:40:50.648274
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    """A test to prove that we can construct a ZDFChannelIE object.

    There isn't really much to test, except that the constructor doesn't crash
    """
    ZDFChannelIE('ZDF', 'ZDF')



# Generated at 2022-06-14 17:41:00.237063
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    import unittest
    import inspect
    class ZDFIE_subclass(ZDFIE):
        provider = None
        provider_key = None
        provider_id = None
    ZDFIE_subclass = ZDFIE_subclass
    class ZDFIETest(unittest.TestCase):
        def test_class_constructor(self):
            ie = ZDFIE_subclass()
            self.assertIsNotNone(ie)
            self.assertEqual(ie.provider, ZDFIE_subclass.provider)
            self.assertEqual(ie.provider_key, ZDFIE_subclass.provider_key)
            self.assertEqual(ie.provider_id, ZDFIE_subclass.provider_id)

# Generated at 2022-06-14 17:41:03.706344
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    a = ZDFIE()
    print("ok")


# Generated at 2022-06-14 17:41:06.108324
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    test_instance = ZDFBaseIE()
    if not test_instance:
        raise Exception('Unit test for ZDFBaseIE failed!')


# Generated at 2022-06-14 17:41:07.396445
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    ZDFIE('test')

# Class for "Fernsehfilm der Woche"

# Generated at 2022-06-14 17:41:11.000599
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    instance = ZDFChannelIE()
    expected_suitable = False
    expected_ie_key = 'ZDF:channel'
    expected_playlist_title = None
    assert instance.suitable('https://www.zdf.de/service-und-hilfe/die-neue-zdf-mediathek/zdfmediathek-trailer-100.html') \
        == expected_suitable
    assert instance.ie_key() == expected_ie_key
    assert instance.playlist_title() == expected_playlist_title

# Generated at 2022-06-14 17:41:14.115544
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    return ZDFChannelIE('https://www.zdf.de/dokumentation/planet-e', {})

# Generated at 2022-06-14 17:41:14.990015
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    # on top of all kinds of tests here
    pass

# Generated at 2022-06-14 17:41:16.372281
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    assert ZDFIE.ie_key() == 'ZDF'


# Generated at 2022-06-14 17:41:24.711938
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    import json
    # Workaround for https://github.com/pytest-dev/pytest-sugar/issues/80
    from .common import record_succeeded, record_failed
    with record_succeeded(0), record_failed(0):
        ZDFChannelIE().url_result("https://www.zdf.de/sport/das-aktuelle-sportstudio")

# Generated at 2022-06-14 17:43:31.901457
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    sample = ZDFBaseIE()
    assert sample._GEO_COUNTRIES == ['DE']
    assert sample._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')


# Generated at 2022-06-14 17:43:37.140783
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    loader = ZDFChannelIE.construct_from_url_with_video_id(
        'https://www.zdf.de/filme/taunuskrimi/', 'dummy-video-id')
    assert '+https://www.zdf.de/filme/taunuskrimi' == loader.IE_NAME


# Generated at 2022-06-14 17:43:43.477396
# Unit test for constructor of class ZDFChannelIE

# Generated at 2022-06-14 17:43:47.413850
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    loader = ZDFBaseIE()
    assert loader._GEO_COUNTRIES == ['DE']
    assert loader._QUALITIES == ('auto', 'low', 'med', 'high', 'veryhigh', 'hd')


# Generated at 2022-06-14 17:43:49.000894
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    ZDFChannelIE(ZDFChannelIE.ie_key(), ZDFChannelIE._VALID_URL, {})

# Generated at 2022-06-14 17:43:54.544044
# Unit test for constructor of class ZDFChannelIE
def test_ZDFChannelIE():
    # The ID 'tatort' is used to check if the regular expression for _VALID_URL is correct.
    assert ZDFChannelIE._VALID_URL.match('https://www.zdf.de/filme/tatort/')

# Generated at 2022-06-14 17:43:56.338232
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    inst = ZDFBaseIE()
    assert isinstance(inst, InfoExtractor)


# Generated at 2022-06-14 17:44:04.456970
# Unit test for constructor of class ZDFIE
def test_ZDFIE():
    # Test object initialization
    obj = ZDFIE()
    assert obj._VALID_URL is ZDFIE._VALID_URL
    assert obj._TESTS == ZDFIE._TESTS
    assert obj._GEO_COUNTRIES == ZDFBaseIE._GEO_COUNTRIES
    assert obj._QUALITIES == ZDFBaseIE._QUALITIES
    assert obj._call_api is ZDFBaseIE._call_api
    assert obj._extract_subtitles is ZDFBaseIE._extract_subtitles
    assert obj._extract_format is ZDFBaseIE._extract_format
    assert obj._extract_ptmd is ZDFBaseIE._extract_ptmd
    assert obj._extract_entry is ZDFIE._extract_entry
    assert obj._extract_regular is ZDF

# Generated at 2022-06-14 17:44:05.298897
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    # Test the media id.
    ZDFBaseIE.ie_key()



# Generated at 2022-06-14 17:44:06.228722
# Unit test for constructor of class ZDFBaseIE
def test_ZDFBaseIE():
    assert ZDFBaseIE(None, {})

