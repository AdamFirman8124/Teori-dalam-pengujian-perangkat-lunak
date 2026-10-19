

# Generated at 2022-06-14 16:45:57.835216
# Unit test for constructor of class NRKPlaylistBaseIE
def test_NRKPlaylistBaseIE():
    NRKPlaylistBaseIE(None, None)()


# Generated at 2022-06-14 16:46:02.693628
# Unit test for constructor of class NRKSkoleIE
def test_NRKSkoleIE():
    assert not NRKSkoleIE.suitable('https://www.nrk.no/troms/gjenopplev-den-historiske-solformorkelsen-1.12270763')
    assert NRKSkoleIE.suitable('https://www.nrk.no/skole/?page=search&q=&mediaId=14099')

# Unit test to check if the class NRKTVSerieBaseIE is callable

# Generated at 2022-06-14 16:46:09.310451
# Unit test for constructor of class NRKTVEpisodesIE
def test_NRKTVEpisodesIE():
    ie = NRKTVEpisodesIE()
    assert ie._VALID_URL == r'https?://tv\.nrk\.no/program/[Ee]pisodes/[^/]+/(?P<id>\d+)'
    assert ie._ITEM_RE == r'data-episode=["\']%s' % NRKTVIE._EPISODE_RE


# Generated at 2022-06-14 16:46:13.523161
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    assert issubclass(NRKTVSerieBaseIE, NRKBaseIE)
    assert hasattr(NRKTVSerieBaseIE, 'url_result')


# Generated at 2022-06-14 16:46:14.514672
# Unit test for constructor of class NRKPlaylistIE
def test_NRKPlaylistIE():
    NRKPlaylistIE(NRKPlaylistBaseIE(), 'www.nrk.no', 'test', 'http://')

# Generated at 2022-06-14 16:46:23.332479
# Unit test for constructor of class NRKBaseIE
def test_NRKBaseIE():
    ie = NRKBaseIE()
    assert ie
    assert ie._GEO_COUNTRIES == ['NO']
    assert ie._CDN_REPL_REGEX == r'(?x)://(?:nrkod\d{1,2}-httpcache0-47115-cacheod0\.dna\.ip-only\.net/47115-cacheod0|nrk-od-no\.telenorcdn\.net|minicdn-od\.nrk\.no/od/nrkhd-osl-rr\.netwerk\.no/no)/'

# Unit test _extract_nrk_formats

# Generated at 2022-06-14 16:46:25.467953
# Unit test for constructor of class NRKIE
def test_NRKIE():
    ie = NRKIE()
    ie.IE_NAME
    ie.IE_DESC
    ie.VALID_URL
    ie.BR_DESC
    ie.CAN_GEOLOCATE


# Generated at 2022-06-14 16:46:35.239561
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    assert NRKTVDirekteIE.suitable('https://tv.nrk.no/direkte/nrk1')
    assert not NRKTVDirekteIE.suitable('https://tv.nrk.no/serie/direkte/nrk1')
    assert not NRKTVDirekteIE.suitable('https://nrk.no/')
    assert not NRKTVDirekteIE.suitable('https://radio.nrk.no/serie/p1')
    assert not NRKTVDirekteIE.suitable('https://nrk.no/')
    assert not NRKTVDirekteIE.suitable('https://nrkbeta.no/')


# Generated at 2022-06-14 16:46:40.282474
# Unit test for constructor of class NRKSkoleIE
def test_NRKSkoleIE():
    ie = NRKSkoleIE()
    url_1 = 'https://www.nrk.no/skole/?page=search&q=&mediaId=14099'
    url_2 = 'https://www.nrk.no/skole/?page=objectives&subject=naturfag&objective=K15114&mediaId=19355'
    # Only URLs that contain 'skole/' are accepted by NRKSkoleIE
    assert NRKSkoleIE.suitable(url_1)
    assert NRKSkoleIE.suitable(url_2)
    # The 'skole/' part should be converted to '/skole/' in _VALID_URL
    assert len(NRKSkoleIE._VALID_URL) > 10

# Generated at 2022-06-14 16:46:46.292708
# Unit test for constructor of class NRKTVSeriesIE
def test_NRKTVSeriesIE():
    # Test basic class construction
    ie = NRKTVSeriesIE()
    assert ie.ie_key() == 'nrk'
    assert ie.ie_key() == 'NRK'
    assert ie.ie_key() == 'nrktv'
    assert ie.ie_key() == 'NrkTv'
    assert ie.ie_key() == 'NRKTV'
    assert ie.ie_key() == 'nrktv:series'
    assert ie.ie_key() == 'NrkTv:series'
    assert ie.ie_key() == 'NRKTV:series'
    assert ie.ie_key() == 'NrkTvSeries'
    assert ie.ie_key() == 'NRKTVSERIES'

    # Test if the NRKTVSeriesIE class is suitable when passed in a correct


# Generated at 2022-06-14 16:47:54.795341
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    ie = NRKTVDirekteIE('NRKTVDirekteIE')



# Generated at 2022-06-14 16:47:56.433283
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    if sys.version_info[:2] == (2, 6):
        return

    base_instance = NRKTVSerieBaseIE()



# Generated at 2022-06-14 16:47:59.910400
# Unit test for constructor of class NRKPlaylistBaseIE
def test_NRKPlaylistBaseIE():

    NRKPBIE = NRKPlaylistBaseIE("nrk")

    test_object = {
        '_match_id': 'test_url',
        '_download_webpage': 'webpage',
    }

    try:
        result = NRKPBIE._real_extract(test_object)
        assert result == "assert"
    except Exception:
        assert True



# Generated at 2022-06-14 16:48:02.482837
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():
    ie = NRKTVIE('http://tv.nrk.no/program/MDDP12000117')
    assert isinstance(ie, NRKTVIE)


# Generated at 2022-06-14 16:48:14.972854
# Unit test for constructor of class NRKBaseIE
def test_NRKBaseIE():
    ie = NRKBaseIE('test', 'other', 'test')
    b = type(ie)._GEO_COUNTRIES
    assert ('NO') in b
    assert ('US') not in b
    f = type(ie)._CDN_REPL_REGEX
    assert (f == r'''(?x)://
        (?:
            nrkod\d{1,2}-httpcache0-47115-cacheod0\.dna\.ip-only\.net/47115-cacheod0|
            nrk-od-no\.telenorcdn\.net|
            minicdn-od\.nrk\.no/od/nrkhd-osl-rr\.netwerk\.no/no
        )/''')



# Generated at 2022-06-14 16:48:24.344758
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    """Function is used to test the constructor of class NRKTVDirekteIE"""
    ie = NRKTVDirekteIE(NRKTVDirekteIE.ie_key())
    assert ie.name == 'NRKTVDirekteIE'
    assert ie._VALID_URL == r'https?://(?:tv|radio)\.nrk\.no/direkte/(?P<id>[^/?#&]+)'
    assert ie._EXTRACTOR_TYPE == NRKTVIE


# Generated at 2022-06-14 16:48:26.446826
# Unit test for constructor of class NRKBaseIE
def test_NRKBaseIE():
    try:
        assert(NRKBaseIE(None)._extract_dummy('foobar') is None)
    except:
        pass


# Generated at 2022-06-14 16:48:35.156555
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    import unittest
    from yt_dl.extractor import get_info_extractor
    from utils import get_minimal_extractor

    # Test for NRKTVSeasonIE.suitable
    class DummyExtractor(get_minimal_extractor(NRKTVSeasonIE)):
        def __init__(self, *args):
            super(DummyExtractor, self).__init__(*args)
            self._downloader.cache.store()

    class TestSuitable(object):
        def __init__(self):
            self.suitable_results = []
            self._url = 'nrk:%s' % 'a'

        def test_suitable(self):
            self.suitable_results.append(
                NRKTVSeasonIE.suitable(self._url))


# Generated at 2022-06-14 16:48:35.953506
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    ie = NRKTVSeasonIE()


# Generated at 2022-06-14 16:48:41.408299
# Unit test for constructor of class NRKTVSeriesIE
def test_NRKTVSeriesIE():
    tester = Tester()
    NRKTVSeriesIE.suitable = None
    tester.assertEqual(NRKTVSeriesIE.suitable('http://tv.nrk.no/serie/dagsrevyen/2015/09/01/00-00'), False)
    tester.assertEqual(NRKTVSeriesIE.suitable('http://tv.nrk.no/serie/blank/sesong/1/episode/1'), False)
    tester.assertEqual(NRKTVSeriesIE.suitable('https://radio.nrk.no/podkast/ulrikkes_univers'), True)

# Generated at 2022-06-14 16:50:01.904770
# Unit test for constructor of class NRKBaseIE
def test_NRKBaseIE():
    # Simple test to ensure that NRKBaseIE can be instantiated correctly
    ie = NRKBaseIE()
    assert isinstance(ie, NRKBaseIE)


# Generated at 2022-06-14 16:50:02.536286
# Unit test for constructor of class NRKSkoleIE
def test_NRKSkoleIE():
    test = NRKSkoleIE()
    assert test

# Generated at 2022-06-14 16:50:06.015116
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():
    ie = NRKTVIE()
    assert ie._VALID_URL == r'https?://(?:tv|radio)\.nrk(?:super)?\.no/(?:[^/]+/)*%s' % ie._EPISODE_RE

# Generated at 2022-06-14 16:50:12.770890
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():
    ie = NRKTVIE()
    assert isinstance(ie, InfoExtractor)
    assert ie.ie_key() == 'NRKTV'
    assert ie.server == 'https://tv.nrk.no/'
    assert ie.api_data['api_key'] == 'apikey.tv.nrk.no'
    assert ie.api_data['api_base'] == 'https://psapi.nrk.no'
    assert ie.api_data['api_path'] == '/mediaelement/%s'
    assert ie.api_data['api_key_auth'] == False

# Generated at 2022-06-14 16:50:16.153485
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():
    ext = NRKTVIE()
    ext.IE_DESC
    ext._VALID_URL
    ext._TESTS

# Generated at 2022-06-14 16:50:25.009088
# Unit test for constructor of class NRKIE
def test_NRKIE():
    # test that program urls and clip urls are both valid
    assert NRKIE._VALID_URL
    # test that it is a valid url

# Generated at 2022-06-14 16:50:34.137570
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    from .nrktv import NRKTVIE
    from .nrktv import NRKTVDirekteIE as nrkdirekte
    from .nrktv import NRKIE
    from .nrktv import NRKTVSeasonIE as nrkseasons
    from .nrktv import NRKTVSeriesIE as nrkseries
    from .nrktv import NRKTVLiveIE as nrklive
    from .nrktv import NRKTVEpisodeIE as nrkepisode
    from .nrktv import NRKTVSearchIE as nrksearch

    obj = NRKTVIE.ie_key()
    assert obj() == nrkdirekte
    obj = NRKIE.suitable(None)
    assert obj == False
    obj = NRKTVIE.suitable(None)


# Generated at 2022-06-14 16:50:38.371874
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():
    url = 'http://tv.nrk.no/serie/20-spoersmaal-tv/MUHH48000314/23-05-2014'
    regex = NRKTVIE._VALID_URL
    try:
        NRKTVIE(url, regex)
    except AssertionError:
        raise AssertionError('%s should match regex %s' % (url, regex))

# Generated at 2022-06-14 16:50:46.874179
# Unit test for constructor of class NRKTVSeriesIE
def test_NRKTVSeriesIE():
    parser = NRKTVSeriesIE()
    #NRKTVIE
    assert parser.suitable('https://tv.nrk.no/dyna/d/a/15/MUHH17004615/MUHH17004615-1561372549.json.html') == False
    #NRKTVEpisodeIE
    assert parser.suitable('https://tv.nrk.no/serie/hellums-kro/sesong/1/episode/2') == False
    #NRKTVSeasonIE
    assert parser.suitable('https://radio.nrk.no/serie/dagsnytt/sesong/201509') == False
    #NRKRadioPodkastIE
    assert parser.suitable('https://radio.nrk.no/podkast/ulrikkes_univers') == False
    #NRK

# Generated at 2022-06-14 16:50:47.281275
# Unit test for constructor of class NRKPlaylistIE
def test_NRKPlaylistIE():
    pass


# Generated at 2022-06-14 16:52:11.978930
# Unit test for constructor of class NRKIE
def test_NRKIE():
    assert NRKIE

# Generated at 2022-06-14 16:52:14.282434
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    url = 'https://tv.nrk.no/direkte/nrk1'
    ie = NRKTVDirekteIE(NRKTVDirekteIE.ie_key())
    assert ie.suitable(url)
    assert ie.IE_NAME == 'nrk:direkte'


# Generated at 2022-06-14 16:52:19.033248
# Unit test for constructor of class NRKTVEpisodeIE
def test_NRKTVEpisodeIE():
    # Test with a specified valid URL in _VALID_URL
    nrktv_episode_ie = NRKTVEpisodeIE('https://tv.nrk.no/serie/hellums-kro/sesong/1/episode/2')
    assert nrktv_episode_ie.VALID_URL == 'https?://tv\.nrk\.no/serie/(?P<id>[^/]+/sesong/(?P<season_number>\d+)/episode/(?P<episode_number>\d+))'
    assert nrktv_episode_ie.IE_DESC == 'NRK TV and NRK Radio'
    assert nrktv_episode_ie.video_id == 'hellums-kro/sesong/1/episode/2'
    assert nrktv_episode_ie.display_

# Generated at 2022-06-14 16:52:19.692350
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    NRKTVSerieBaseIE()


# Generated at 2022-06-14 16:52:23.080502
# Unit test for constructor of class NRKTVEpisodeIE
def test_NRKTVEpisodeIE():
    info_test = NRKTVEpisodeIE._real_extract(NRKTVEpisodeIE(), 'https://tv.nrk.no/serie/backstage/sesong/1/episode/8')
    assert info_test['id'] == 'MSUI14000816'
    assert info_test['season_number'] == 1
    assert info_test['episode_number'] == 8
    assert info_test['episode'] == '8. episode'


# Generated at 2022-06-14 16:52:23.967065
# Unit test for constructor of class NRKTVEpisodeIE
def test_NRKTVEpisodeIE():
    assert NRKTVEpisodeIE.__bases__ == (NRKTVSerieIE,)


# Generated at 2022-06-14 16:52:24.769409
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():
    nrk = NRKTVIE()
    assert nrk


# Generated at 2022-06-14 16:52:25.126668
# Unit test for constructor of class NRKBaseIE
def test_NRKBaseIE():
    pass

# Generated at 2022-06-14 16:52:27.462380
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    assert (NRKTVDirekteIE.suitable('https://tv.nrk.no/direkte/nrk1')
            or NRKTVDirekteIE.suitable('https://radio.nrk.no/direkte/p1_oslo_akershus'))



# Generated at 2022-06-14 16:52:28.504441
# Unit test for constructor of class NRKTVEpisodeIE
def test_NRKTVEpisodeIE():
    return NRKTVEpisodeIE()

