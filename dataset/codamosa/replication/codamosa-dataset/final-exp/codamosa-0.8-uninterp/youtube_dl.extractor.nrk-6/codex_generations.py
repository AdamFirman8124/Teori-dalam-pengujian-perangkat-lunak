

# Generated at 2022-06-14 16:46:01.974052
# Unit test for constructor of class NRKIE
def test_NRKIE():
    url = 'http://www.nrk.no/video/PS*150533'
    ie = NRKIE()
    ie._real_extract(url)
    return ie


# Generated at 2022-06-14 16:46:05.928112
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    """ test if the constructor of NRKTVSerieBaseIE works """
    from .. import NRKTVSerieBaseIE
    assert NRKTVSerieBaseIE(NRKTVSerieBaseIE.ie_key())._VALID_URL == 'https?://(?:tv|radio)\.nrk(?:super)?\.no/(?:[^/]+/)*$'


# Generated at 2022-06-14 16:46:08.241662
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():
    assert(NRKTVIE.__dict__.get('_VALID_URL')) # pylint: disable=W0104

NRKPlaylistIE = NRKTVIE  # pylint: disable=C0103



# Generated at 2022-06-14 16:46:09.484297
# Unit test for constructor of class NRKPlaylistIE
def test_NRKPlaylistIE():
    nrkplaylistie = NRKPlaylistIE()
    assert nrkplaylistie is not None



# Generated at 2022-06-14 16:46:11.441856
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():
    test = NRKTVIE()
    assert test.IE_DESC == 'NRK TV and NRK Radio'

# Generated at 2022-06-14 16:46:14.348394
# Unit test for constructor of class NRKTVSeriesIE
def test_NRKTVSeriesIE():
    nrk_tv_series_ie = NRKTVSeriesIE()
    nrk_tv_series_ie._real_extract(
        'https://radio.nrk.no/podkast/ulrikkes_univers')



# Generated at 2022-06-14 16:46:15.884281
# Unit test for constructor of class NRKSkoleIE
def test_NRKSkoleIE():
    test_url = 'https://www.nrk.no/skole/?page=search&q=&mediaId=14099'
    assert NRKSkoleIE().suitable(test_url) == True


# Generated at 2022-06-14 16:46:17.390507
# Unit test for constructor of class NRKTVEpisodesIE
def test_NRKTVEpisodesIE():
    ie = NRKTVEpisodesIE()
    assert ie

# Generated at 2022-06-14 16:46:24.124049
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    ie = NRKTVDirekteIE()
    assert ie._VALID_URL == r'https?://(?:tv|radio)\.nrk\.no/direkte/(?P<id>[^/?#&]+)'
    assert ie.IE_NAME == 'NRK TV Direkte and NRK Radio Direkte'
    assert ie.IE_DESC == 'NRK TV Direkte and NRK Radio Direkte'



# Generated at 2022-06-14 16:46:34.790624
# Unit test for constructor of class NRKBaseIE
def test_NRKBaseIE():
    ie = NRKBaseIE('NRK', 'no')
    assert ie._GEO_COUNTRIES == ['NO']
    assert ie._CDN_REPL_REGEX == r'''(?x)://
        (?:
            nrkod\d{1,2}-httpcache0-47115-cacheod0\.dna\.ip-only\.net/47115-cacheod0|
            nrk-od-no\.telenorcdn\.net|
            minicdn-od\.nrk\.no/od/nrkhd-osl-rr\.netwerk\.no/no
        )/'''
    assert ie.IE_NAME == 'NRKBase'

# Generated at 2022-06-14 16:47:40.989021
# Unit test for constructor of class NRKTVSeriesIE
def test_NRKTVSeriesIE():
    ie = NRKTVSeriesIE()
    assert ie.suitable('https://tv.nrk.no/serie/blank')
    assert not ie.suitable('https://tv.nrk.no/program/NRK_141514141414')
    assert not ie.suitable('https://tv.nrk.no/serie/blank/sesong/1/episode/1')
    assert not ie.suitable('https://tv.nrk.no/serie/blank/sesong/1')
    assert not ie.suitable('https://radio.nrk.no/podkast/dickie-dick-dickens/sesong/1')

# Generated at 2022-06-14 16:47:45.644177
# Unit test for constructor of class NRKPlaylistBaseIE
def test_NRKPlaylistBaseIE():
    NRKPlaylistBaseIE._ITEM_RE = r'nrk:([\da-f]{8}-[\da-f]{4}-[\da-f]{4}-[\da-f]{4}-[\da-f]{12})'
    playlist_obj = NRKPlaylistBaseIE(NRKPlaylistBaseIE._create_ie())
    assert playlist_obj._VALID_URL
    assert playlist_obj._ITEM_RE



# Generated at 2022-06-14 16:47:46.812111
# Unit test for constructor of class NRKSkoleIE
def test_NRKSkoleIE():
    # Check if creation of NRKSkoleIE class creates an NRKSkoleIE instance
    assert isinstance(NRKSkoleIE(), NRKSkoleIE)

# Generated at 2022-06-14 16:47:56.290094
# Unit test for constructor of class NRKIE
def test_NRKIE():
    NRKIE_instance = NRKIE()
    assert NRKIE_instance.geo_countries == ['NO']
    assert NRKIE_instance.IE_NAME == 'nrk'
    assert NRKIE_instance.VALID_URL == 'https?://(?:(?:www\.)?nrk\.no/video/(?:PS\*|[^_]+_)|v8[-.]psapi\.nrk\.no/mediaelement/)(?P<id>[^?\#&]+)'
    assert NRKIE_instance._TESTS[0]['url'] == 'http:http://www.nrk.no/video/PS*150533'
    assert NRKIE_instance._TESTS[0]['md5'] == 'f46be075326e23ad0e524edfcb06aeb6'


# Generated at 2022-06-14 16:47:59.599501
# Unit test for constructor of class NRKSkoleIE
def test_NRKSkoleIE():
    ie = NRKSkoleIE()
    assert ie.name == 'nrkskole'
    assert ie.description == ie.IE_DESC
    assert ie.url_re == NRKSkoleIE._VALID_URL
    assert ie.provider == 'nrkskole'
    assert ie.ie_key() == 'NRKSkole'
    assert ie.app_version is None
    assert ie.app_revision is None
    assert ie.app_revision is None

# Generated at 2022-06-14 16:48:06.628497
# Unit test for constructor of class NRKIE
def test_NRKIE():
    test = NRKIE()
    test._GEO_COUNTRIES = ['NO']
    test._CDN_REPL_REGEX = r'(?x)://(?:nrkod\d{1,2}-httpcache0-47115-cacheod0\.dna\.ip-only\.net/47115-cacheod0|nrk-od-no\.telenorcdn\.net|minicdn-od\.nrk\.no/od/nrkhd-osl-rr\.netwerk\.no/no)/'
    nrk_id = '157026'
    url = 'https://www.nrk.no/video/PS*%s' % nrk_id

# Generated at 2022-06-14 16:48:11.781250
# Unit test for constructor of class NRKSkoleIE
def test_NRKSkoleIE():
    nrkSkole = NRKSkoleIE()
    nrkSkole.suitable("https://nrk.no/skole/?page=objectives&subject=naturfag&objective=K15114&mediaId=19355")
    assert nrkSkole.IE_DESC == 'NRK Skole'
    assert nrkSkole._VALID_URL == r'https?://(?:www\.)?nrk\.no/skole/?\?.*\bmediaId=(?P<id>\d+)'
    assert nrkSkole._TESTS[0]['url'] == 'https://www.nrk.no/skole/?page=search&q=&mediaId=14099'

# Generated at 2022-06-14 16:48:13.626694
# Unit test for constructor of class NRKTVEpisodesIE
def test_NRKTVEpisodesIE():
    # Test construction
    if __name__ == "__main__":
        tvepi_ie = NRKTVEpisodesIE('https://tv.nrk.no/program/episodes/nytt-paa-nytt/69031');
        print(tvepi_ie.extract());

# Generated at 2022-06-14 16:48:15.099132
# Unit test for constructor of class NRKIE
def test_NRKIE():
    '''Test constructor of class NRKIE'''
    nrk = NRKIE()
    assert nrk == NRKIE()
    assert nrk is not None

# Generated at 2022-06-14 16:48:19.775809
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    assert NRKTVDirekteIE(NRKTVDirekteIE.ie_key())._VALID_URL == NRKTVDirekteIE._VALID_URL


# Generated at 2022-06-14 16:50:39.352559
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():
    nrktvie = NRKTVIE()
    assert nrktvie._VALID_URL == r'https?://(?:tv|radio)\.nrk(?:super)?\.no/(?:[^/]+/)*(?P<id>[a-zA-Z]{4}\d{8})'



# Generated at 2022-06-14 16:50:47.439226
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    # Note: This is an important test
    # Because this test can statically detect whether these code is correct
    import inspect
    for key in NRKTVSerieBaseIE._ASSETS_KEYS:
        assert hasattr(NRKTVSerieBaseIE, '_%s_search' % key), \
            '%s does not override _%s_search' % (NRKTVSerieBaseIE.__name__, key)
        assert inspect.getargspec(getattr(NRKTVSerieBaseIE, '_%s_search' % key)[0])[0] == ['self', 'serie'], \
            '_%s_search has wrong arguments' % key

# Generated at 2022-06-14 16:50:48.748488
# Unit test for constructor of class NRKPlaylistBaseIE
def test_NRKPlaylistBaseIE():
    return NRKPlaylistBaseIE (
        "NRKPlaylistBaseIE",
        {},
    )



# Generated at 2022-06-14 16:50:57.256703
# Unit test for constructor of class NRKTVEpisodeIE
def test_NRKTVEpisodeIE():
    # Given we have a valid url.
    url = 'https://tv.nrk.no/serie/hellums-kro/sesong/1/episode/2'
    # When we construct the NRKTVEpisodeIE object.
    nrktv_episode_ie_object = NRKTVEpisodeIE()
    # Then the object is valid.
    assert nrktv_episode_ie_object
    # And a valid display_id is extracted.
    assert 'hellums-kro/sesong/1/episode/2' == nrktv_episode_ie_object._match_id(url)


# Generated at 2022-06-14 16:51:02.217976
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    x = NRKTVSeasonIE()
    assert x._TESTS[0]['playlist_mincount'] > 0

# Generated at 2022-06-14 16:51:04.105009
# Unit test for constructor of class NRKTVEpisodeIE
def test_NRKTVEpisodeIE():
    from nrktv import _parse_episode_info
    _parse_episode_info(NRKTVIE, NRKTVEpisodeIE, NRKTVIE._TESTS[0]['info_dict'])

# Generated at 2022-06-14 16:51:06.397599
# Unit test for constructor of class NRKSkoleIE
def test_NRKSkoleIE():
    url = 'https://www.nrk.no/skole/?page=search&q=&mediaId=14099'
    webpage = "<html></html>"
    NRKSkoleIE(NRKPlaylistBaseIE(), url, webpage)

# Generated at 2022-06-14 16:51:11.352767
# Unit test for constructor of class NRKRadioPodkastIE
def test_NRKRadioPodkastIE():
    ie = NRKRadioPodkastIE('https://radio.nrk.no/podkast/ulrikkes_univers/l_96f4f1b0-de54-4e6a-b4f1-b0de54fe6af8')
    assert ie._VALID_URL == r'https?://radio\.nrk\.no/pod[ck]ast/(?:[^/]+/)+(?P<id>l_[\da-f]{8}-[\da-f]{4}-[\da-f]{4}-[\da-f]{4}-[\da-f]{12})'
    assert ie.IE_NAME == 'nrk'
    assert ie.IE_DESC == 'NRK'



# Generated at 2022-06-14 16:51:23.213036
# Unit test for constructor of class NRKTVSeriesIE
def test_NRKTVSeriesIE():
    nrk_series = NRKTVSeriesIE()
    nrk_series._call_api = lambda _: {'_embedded': {'episodes': [{ 'prfId': 'MSUI14000116'}]}}
    result = nrk_series._entries({}, 'series')
    assert result[0].url == 'nrk:MSUI14000116'
    assert result[0].ie_key == 'NRK'
    assert result[0].video_id == 'MSUI14000116'
    nrk_series = NRKTVSeriesIE()
    nrk_series._call_api = lambda _: {'_embedded': {'instalments': [{ 'episodeId': 'MSUI14000116'}]}}
    result = nrk_series._entries({}, 'series')

# Generated at 2022-06-14 16:51:26.913249
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    try:
        NRKTVSerieBaseIE()
    except Exception as e:
        _, _, exc_traceback = sys.exc_info()
        print('Type "%s" not expected.' % type(e).__name__)
        raise exc_traceback

