

# Generated at 2022-06-14 16:45:55.753344
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():
    nrk_tv_ie = NRKTVIE()
    assert nrk_tv_ie.title('Nytt på nytt 27.01.2017') == 'Nytt på Nytt 27.01.2017'

# Generated at 2022-06-14 16:45:56.481468
# Unit test for constructor of class NRKPlaylistIE
def test_NRKPlaylistIE():
    NRKPlaylistIE('NRKPlaylist', 'nrk.no')


# Generated at 2022-06-14 16:46:07.690012
# Unit test for constructor of class NRKIE
def test_NRKIE():
    nrk = NRKIE()
    assert(nrk._VALID_URL == NRKIE._VALID_URL)
    assert(nrk._TESTS == NRKIE._TESTS)
    assert(nrk._GEO_COUNTRIES == NRKBaseIE._GEO_COUNTRIES)
    assert(nrk._CDN_REPL_REGEX == NRKBaseIE._CDN_REPL_REGEX)
    assert(nrk._downloader == None)
    assert(nrk._download_webpage == None)
    assert(nrk._download_json == None)
    assert(nrk._raise_error == None)
    assert(nrk._call_api == None)
    assert(nrk._real_extract == None)
    assert(nrk._match_id == None)

# Generated at 2022-06-14 16:46:14.525609
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    # Test with regular program
    nrktv_direkte = NRKTVDirekteIE("nrk1")
    assert nrktv_direkte.program_id == "p1-nrk1"
    assert nrktv_direkte.category == "p1"
    nrktv_direkte = NRKTVDirekteIE("nrk1", category="p2")
    assert nrktv_direkte.program_id == "p1-nrk1"
    assert nrktv_direkte.category == "p2" # Should be changed to "p1"
    # Test with radio program
    nrktv_direkte = NRKTVDirekteIE("p1_oslo_akershus")
    assert n

# Generated at 2022-06-14 16:46:25.659902
# Unit test for constructor of class NRKBaseIE
def test_NRKBaseIE():
    ie = NRKBaseIE()
    ie._GEO_COUNTRIES = ['NO']
    ie._CDN_REPL_REGEX = r'''(?x)://
        (?:
            nrkod\d{1,2}-httpcache0-47115-cacheod0\.dna\.ip-only\.net/47115-cacheod0|
            nrk-od-no\.telenorcdn\.net|
            minicdn-od\.nrk\.no/od/nrkhd-osl-rr\.netwerk\.no/no
        )/'''

# Generated at 2022-06-14 16:46:26.610050
# Unit test for constructor of class NRKIE
def test_NRKIE():
    assert callable(NRKIE)

# Generated at 2022-06-14 16:46:27.373591
# Unit test for constructor of class NRKSkoleIE
def test_NRKSkoleIE():
    assert type(NRKSkoleIE) == _NRKSkoleIE



# Generated at 2022-06-14 16:46:30.104210
# Unit test for constructor of class NRKRadioPodkastIE
def test_NRKRadioPodkastIE():
    # create instance of NRKRadioPodkastIE
    ie = NRKRadioPodkastIE()
    # Create a regex (regexp) object with the string to be searched in
    prog = re.compile(ie._VALID_URL)
    # Iterate over all matching patterns in the string
    for m in prog.finditer(ie.IE_DESC):
        # print the matched pattern
        print(m.groupdict())


# Generated at 2022-06-14 16:46:30.802275
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    assert NRKTVSeasonIE('test', 'test', 'test', 'test')


# Generated at 2022-06-14 16:46:31.314434
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    assert NRKTVSeasonIE()


# Generated at 2022-06-14 16:47:26.408576
# Unit test for constructor of class NRKRadioPodkastIE
def test_NRKRadioPodkastIE():
    radio_ie = NRKRadioPodkastIE()
    assert radio_ie.IE_NAME == 'nrk'
    assert radio_ie.IE_DESC == 'NRK.no'
    assert radio_ie.ie_key() == 'nrk'



# Generated at 2022-06-14 16:47:32.412195
# Unit test for constructor of class NRKTVEpisodeIE
def test_NRKTVEpisodeIE():
    # Test empty string as argument
    assert_raises(AttributeError, NRKTVEpisodeIE, '')
    # Test not valid URL
    assert_raises(RegexNotFoundError, NRKTVEpisodeIE, 'http://google.com')
    # Test valid URL
    NRKTVEpisodeIE('https://tv.nrk.no/serie/hellums-kro/sesong/1/episode/2')
    NRKTVEpisodeIE('https://tv.nrk.no/serie/backstage/sesong/1/episode/8')

# Generated at 2022-06-14 16:47:41.549219
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    # Test standard URL for NRK TV Direkte
    nrktvdirekte_ie = NRKTVDirekteIE('https://tv.nrk.no/direkte/nrk1')
    assert nrktvdirekte_ie.program_id == 'nrk1'
    # Test standard URL for NRK Radio Direkte
    nrktvdirekte_ie = NRKTVDirekteIE('https://radio.nrk.no/direkte/p1_oslo_akershus')
    assert nrktvdirekte_ie.program_id == 'p1_oslo_akershus'

# Generated at 2022-06-14 16:47:50.716394
# Unit test for constructor of class NRKBaseIE

# Generated at 2022-06-14 16:48:00.048402
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    ie = NRKTVDirekteIE('tv')
    assert isinstance(ie, InfoExtractor)
    for url in (
            'https://tv.nrk.no/direkte/nrk1',
            'https://tv.nrk.no/direkte/nrk2',
            'https://radio.nrk.no/direkte/p1_oslo_akershus',
            'https://radio.nrk.no/direkte/p2',
            'https://radio.nrk.no/direkte/nrk_mp3',
            'https://radio.nrk.no/direkte/nrk_super_mp3'):
        match = re.match(ie._VALID_URL, url, re.VERBOSE)
        assert match is not None

# Generated at 2022-06-14 16:48:05.244878
# Unit test for constructor of class NRKRadioPodkastIE
def test_NRKRadioPodkastIE():
    inst = NRKRadioPodkastIE()
    assert inst.suitable('https://radio.nrk.no/podkast/ulrikkes_univers/l_96f4f1b0-de54-4e6a-b4f1-b0de54fe6af8')
    assert inst.suitable('https://radio.nrk.no/podkast/ulrikkes_univers/l_96f4f1b0-de54-4e6a-b4f1-b0de54fe6af8')
    assert not inst.suitable('https://radio.nrk.no/podkcast/ulrikkes_univers/l_96f4f1b0-de54-4e6a-b4f1-b0de54fe6af8')
    assert not inst.su

# Generated at 2022-06-14 16:48:10.391224
# Unit test for constructor of class NRKSkoleIE
def test_NRKSkoleIE():
    temp_object = NRKSkoleIE('http://www.nrk.no/skole/?page=search&q=&mediaId=14099')
    assert(temp_object.IE_DESC == 'NRK Skole')
    assert(temp_object._VALID_URL == 'https?://(?:www\.)?nrk\.no/skole/?\?.*\bmediaId=(?P<id>\d+)')

# Generated at 2022-06-14 16:48:13.166358
# Unit test for constructor of class NRKPlaylistBaseIE
def test_NRKPlaylistBaseIE():
    with pytest.raises(TypeError):
        NRKPlaylistBaseIE()


# Generated at 2022-06-14 16:48:14.561149
# Unit test for constructor of class NRKTVEpisodeIE
def test_NRKTVEpisodeIE():
    ie = NRKTVEpisodeIE('')
    assert ie != None


# Generated at 2022-06-14 16:48:15.326008
# Unit test for constructor of class NRKSkoleIE
def test_NRKSkoleIE():
    nrkSkole = NRKSkoleIE()
    return

# Generated at 2022-06-14 16:50:26.322406
# Unit test for constructor of class NRKTVEpisodeIE
def test_NRKTVEpisodeIE():
    def test(url, result):
        # check if we are getting the correct object
        if isinstance(result, InfoExtractor):
            assert(result.__class__ == NRKTVEpisodeIE)
            assert(result.suitable(url) == True)
            assert(result._VALID_URL == NRKTVEpisodeIE._VALID_URL)
        else:
            assert(result == False)

    # No url passed
    test('', False)
    # wrong url
    test('https://tv.nrk.no/serie/anno/KMTE50001317', False)
    # valid url
    episode_class = extractor.gen_extractors(NRKTVEpisodeIE)[0]

# Generated at 2022-06-14 16:50:26.954201
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    NRKTVSerieBaseIE()



# Generated at 2022-06-14 16:50:30.193713
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    try:
        import unittest
        from unittest import main as ut_main
        from unittest.mock import patch

        from . import NRKTVSerieBaseIE

        class NRKTVSerieBaseIETest(unittest.TestCase):
            def setUp(self):
                self.serie_ie = NRKTVSerieBaseIE()
        ut_main()
    except ImportError:
        pass


# Generated at 2022-06-14 16:50:34.796277
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    from .test_download import TestDownload
    class TestNRKTVSeasonIE(TestDownload):
        def setUp(self):
            self.ie = NRKTVSeasonIE("")
    TestNRKTVSeasonIE("test_real_extract").runTest()



# Generated at 2022-06-14 16:50:43.912878
# Unit test for constructor of class NRKSkoleIE
def test_NRKSkoleIE():
    expected_info = 'https://nrkno-skole-prod.kube.nrk.no/skole/api/media/14099'

# Generated at 2022-06-14 16:50:45.545884
# Unit test for constructor of class NRKTVEpisodesIE
def test_NRKTVEpisodesIE():
    ie = NRKTVEpisodesIE(None, {})
    assert ie is not None

# Generated at 2022-06-14 16:50:48.761817
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    ie = NRKTVDirekteIE('NRK TV Direkte')
    ie.get_info(NRKTVDirekteIE._VALID_URL)



# Generated at 2022-06-14 16:50:57.518390
# Unit test for constructor of class NRKBaseIE
def test_NRKBaseIE():
    info_extractor = NRKBaseIE()
    assert info_extractor._GEO_COUNTRIES == ['NO']
    assert info_extractor._CDN_REPL_REGEX == '''(?x)://
        (?:
            nrkod\d{1,2}-httpcache0-47115-cacheod0\.dna\.ip-only\.net/47115-cacheod0|
            nrk-od-no\.telenorcdn\.net|
            minicdn-od\.nrk\.no/od/nrkhd-osl-rr\.netwerk\.no/no
        )/'''


# Generated at 2022-06-14 16:50:59.263731
# Unit test for constructor of class NRKPlaylistBaseIE
def test_NRKPlaylistBaseIE():
    assert hasattr(NRKPlaylistBaseIE, '_VALID_URL')
    assert hasattr(NRKPlaylistBaseIE, '_TESTS')
    assert hasattr(NRKPlaylistBaseIE, '_ITEM_RE')


# Generated at 2022-06-14 16:51:03.957685
# Unit test for constructor of class NRKTVEpisodesIE
def test_NRKTVEpisodesIE():
    k = NRKTVEpisodesIE()
    # check the global variables has been assigned a value
    try:
        assert k.IE_DESC
        assert k._VALID_URL
        assert k._TESTS
    except AssertionError as ae:
        assert -1, f"test_NRKTVEpisodesIE failed due to {ae}"
    except Exception as e:
        assert -1, f"test_NRKTVEpisodesIE failed due to {e}"
    else:
        assert 1, "test_NRKTVEpisodesIE passed"



# Generated at 2022-06-14 16:53:31.333609
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    with patch('nrktv.extractor.NRKTVSerieBaseIE'
               '._extract_entries',
               Mock(return_value=[Mock(spec=GenericIE)])):
        catalog_name = 'podcast'
        data = {'_embedded': {'podcast': None}}
        pagelist = NRKTVSerieBaseIE._entries(data, None)
        next(pagelist)
        assert next(pagelist)
        catalog_name = 'series'
        data = {'_embedded': {'series': None}}
        pagelist = NRKTVSerieBaseIE._entries(data, None)
        next(pagelist)
        assert next(pagelist)
        data = {'_embedded': {'instalments': None}}
        pagelist = NRKTVSerie

# Generated at 2022-06-14 16:53:33.690527
# Unit test for constructor of class NRKPlaylistBaseIE
def test_NRKPlaylistBaseIE():
    # Assert that NRKPlaylistBaseIE.__init__() doesn't raise an exception
    # and that NRKPlaylistBaseIE.suitable() doesn't fail.
    NRKPlaylistBaseIE(NRKPlaylistBaseIE._downloader).suitable('https://tv.nrk.no/programmer/')



# Generated at 2022-06-14 16:53:38.434032
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    for url in ('https://tv.nrk.no/program/MUHH36008517', 'https://tv.nrk.no/serie/hellums-kro'):
        nrk = NRKTVSerieBaseIE()
        nrk._download_webpage(url, 'test')
        nrk_tv = NRKTVIE()
        nrk_tv._download_webpage(url, 'test')
        print(nrk._extract_video_id() + ' ' + nrk_tv._extract_video_id())
        assert nrk._extract_video_id() == nrk_tv._extract_video_id()


# Generated at 2022-06-14 16:53:42.836811
# Unit test for constructor of class NRKSkoleIE
def test_NRKSkoleIE():
    instance = NRKSkoleIE('NRKSkoleIE', 'nrk.no')
    assert instance.IE_DESC == 'NRK Skole'
    assert instance._VALID_URL == r'https?://(?:www\.)?nrk\.no/skole/?\?.*\bmediaId=(?P<id>\d+)'

# Generated at 2022-06-14 16:53:46.741329
# Unit test for constructor of class NRKSkoleIE
def test_NRKSkoleIE():
    # Test 1
    nrk_skole_ie = NRKSkoleIE({})
    nrk_skole_ie.url = 'https://www.nrk.no/skole/?page=search&q=&mediaId=14099'
    info_dict = nrk_skole_ie._real_extract(nrk_skole_ie.url)
    assert info_dict['id'] == '6021'
    assert info_dict['title'] == 'Genetikk og eneggede tvillinger'
    assert info_dict['description'] == 'md5:3aca25dcf38ec30f0363428d2b265f8d'
    assert info_dict['duration'] == 399

# Generated at 2022-06-14 16:53:51.075072
# Unit test for constructor of class NRKRadioPodkastIE
def test_NRKRadioPodkastIE():
    instance = NRKRadioPodkastIE()
    assert NRKRadioPodkastIE.suitable('https://radio.nrk.no/podkast/ulrikkes_univers/l_96f4f1b0-de54-4e6a-b4f1-b0de54fe6af8')
    assert NRKRadioPodkastIE.suitable('http://radio.nrk.no/podkast/ulrikkes_univers/l_96f4f1b0-de54-4e6a-b4f1-b0de54fe6af8')

# Generated at 2022-06-14 16:53:51.977234
# Unit test for constructor of class NRKTVEpisodesIE
def test_NRKTVEpisodesIE():
    ie = NRKTVEpisodesIE()
    assert ie is not None
# Unit test

# Generated at 2022-06-14 16:53:53.700927
# Unit test for constructor of class NRKPlaylistBaseIE
def test_NRKPlaylistBaseIE():
    ie = NRKPlaylistBaseIE('NRKPlaylistBaseIE', 'https://www.nrk.no/');
    assert ie.IE_DESC == 'NRKPlaylistBaseIE'
    assert ie.ie_key() == 'NRKPlaylistBaseIE'


# Generated at 2022-06-14 16:53:56.570662
# Unit test for constructor of class NRKPlaylistBaseIE
def test_NRKPlaylistBaseIE():
    class MockNRKPlaylistBaseIE(NRKPlaylistBaseIE):
        IE_NAME = 'MockNRKPlaylistBaseIE'
        _VALID_URL = r'https?://(?:tv|radio).nrk.no/serie/.*/sesong/.*/avspiller'
        _ITEM_RE = r'data-media-id="(.*?)"'
    ie = MockNRKPlaylistBaseIE()
    assert ie.IE_NAME == 'MockNRKPlaylistBaseIE'



# Generated at 2022-06-14 16:53:58.141566
# Unit test for constructor of class NRKTVEpisodesIE
def test_NRKTVEpisodesIE():
    """
    Note: Result is not tested.
        Functionality of NRKTVEpisodesIE is tested with the other tests.
    """
    ie = NRKTVEpisodesIE()
    assert ie.IE_NAME == 'nrk:episodes'
