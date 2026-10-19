

# Generated at 2022-06-14 16:45:58.735917
# Unit test for constructor of class NRKIE
def test_NRKIE():
    print('Construct an instance of class NRKIE')
    NRKIE()

if __name__ == '__main__':
    test_NRKIE()

# Generated at 2022-06-14 16:46:10.585597
# Unit test for constructor of class NRKTVSeriesIE
def test_NRKTVSeriesIE():
    ie = NRKTVSeriesIE()
    assert ie.suitable('https://tv.nrk.no/serie/groenn-glede')
    assert ie.suitable('https://tv.nrk.no/serie/blank')
    assert ie.suitable('https://tv.nrk.no/serie/backstage')
    assert ie.suitable('https://radio.nrk.no/serie/dickie-dick-dickens')
    assert ie.suitable('https://nrksuper.no/serie/labyrint')
    assert ie.suitable('https://radio.nrk.no/podkast/ulrikkes_univers')

# Generated at 2022-06-14 16:46:14.971565
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    parrent = {'_fallback_host': 'tv'}
    serie = NRKTVSerieBaseIE(parrent)
    assert serie._fallback_host == 'tv'



# Generated at 2022-06-14 16:46:20.348876
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    ie = NRKTVDirekteIE(None)
    assert ie.IE_NAME == 'nrk:direkte'
    assert ie.ie_key() == 'NRKTVDirekte'
    assert ie.CLASS_NAME == 'NRKTVDirekteIE'
    assert ie.NAME == 'NRK'
    assert ie.DESCRIPTION == 'NRK TV Direkte and NRK Radio Direkte'
    assert ie.webpage_url_regex() == r'https?://(?:tv|radio)\.nrk\.no/direkte/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:46:28.893575
# Unit test for constructor of class NRKTVEpisodesIE
def test_NRKTVEpisodesIE():
    ie = NRKTVEpisodesIE()
    assert ie.suitable("https://tv.nrk.no/program/episodes/nytt-paa-nytt/69031")
    assert not ie.suitable("https://tv.nrk.no/program/episodes/nytt-paa-nytt/69031/")
    assert not ie.suitable("https://tv.nrk.no/program/episodes/nytt-paa-nytt/")
    assert not ie.suitable("https://tv.nrk.no/program/episodes/")
    assert not ie.suitable("https://tv.nrk.no/program/")


# Generated at 2022-06-14 16:46:30.715103
# Unit test for constructor of class NRKIE
def test_NRKIE():
    url = 'http://www.nrk.no/video/PS*150533'
    nrkie = NRKIE(url).IE_NAME
    assert nrkie == 'NRK'

# Generated at 2022-06-14 16:46:32.741068
# Unit test for constructor of class NRKSkoleIE
def test_NRKSkoleIE():
    info_extractor = NRKSkoleIE()
    assert info_extractor._VALID_URL == r'https?://(?:www\.)?nrk\.no/skole/?\?.*\bmediaId=(?P<id>\d+)'
    assert info_extractor.IE_DESC == 'NRK Skole'

# Generated at 2022-06-14 16:46:33.779708
# Unit test for constructor of class NRKRadioPodkastIE
def test_NRKRadioPodkastIE():
    ie = NRKRadioPodkastIE()
    assert ie.suitable(NRKRadioPodkastIE._VALID_URL)


# Generated at 2022-06-14 16:46:38.072103
# Unit test for constructor of class NRKBaseIE
def test_NRKBaseIE():
    def test_init(cls):
        inst = cls()
        assert inst.IE_NAME.lower() == re.sub(r'IE$', '', inst.__class__.__name__).lower()
        assert inst.IE_NAME == re.sub(r'IE$', '', inst.__class__.__name__)
        assert inst._VALID_URL.startswith('http://tv.nrk.no/program/')
    for cls in (NRKIE,) + NRKIE.__bases__:
        test_init(cls)



# Generated at 2022-06-14 16:46:40.682057
# Unit test for constructor of class NRKBaseIE
def test_NRKBaseIE():
    try:
        NRKBaseIE(None, None)
        assert False
    except:
        assert True

# Generated at 2022-06-14 16:47:46.866752
# Unit test for constructor of class NRKTVEpisodeIE
def test_NRKTVEpisodeIE():
    IE = NRKTVEpisodeIE(None)
    assert IE._VALID_URL == r'https?://tv\.nrk\.no/serie/(?P<id>[^/]+/sesong/(?P<season_number>\d+)/episode/(?P<episode_number>\d+))'

# Generated at 2022-06-14 16:47:52.015989
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    url = 'https://tv.nrk.no/direkte/nrk1'
    direkte_ie = NRKTVDirekteIE(NRKTVDirekteIE._create_get_urls_extractor(url))
    direkte_ie._downloader = None
    direkte_ie.urls = [url]
    direkte_ie.get_urls = lambda x: direkte_ie.urls
    direkte_ie._download_webpage = lambda *args, **kwargs:''
    direkte_ie._extract_stream_info = lambda *args, **kwargs: {'episodes': [{'url': url, 'title': 'title'}]}

# TODO:
# - https://tv.nrk.no/serie/arvingene

# Generated at 2022-06-14 16:47:52.825494
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():
    NRKTVIE(nrktvNRKBaseIE())._real_extract("")

# Generated at 2022-06-14 16:47:59.270362
# Unit test for constructor of class NRKPlaylistBaseIE
def test_NRKPlaylistBaseIE():
    test_url = 'https://tv.nrk.no/serie/barnas-superjul/barnas-superjul-sommer-2016'
    ie = NRKPlaylistBaseIE()
    assert ie.suitable(test_url)
    assert ie._VALID_URL == 'https?://(?:tv\.nrk|nrksuper)\.no/(?:serie/(?:[^/]+/)*(?:[^/?#&]+))'
    assert ie._ITEM_RE == 'data-media-content-id=["\']([^"\']+)'
    assert ie._match_id(test_url) == 'barnas-superjul-sommer-2016'
    assert ie.ie_key() == 'NRKPlaylistBase'


# Generated at 2022-06-14 16:48:00.932118
# Unit test for constructor of class NRKRadioPodkastIE
def test_NRKRadioPodkastIE():
    try:
        NRKRadioPodkastIE(NRKRadioPodkastIE.ie_key())
        return True
    except:
        return False


# Generated at 2022-06-14 16:48:01.933044
# Unit test for constructor of class NRKPlaylistBaseIE
def test_NRKPlaylistBaseIE():
    NRKPlaylistBaseIE.__doc__


# Generated at 2022-06-14 16:48:15.107943
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    nrkseriebase = NRKTVSerieBaseIE()
    nrk_id = 'PSDJ23209914'
    assert nrkseriebase._match_id(nrk_id) == nrk_id
    assert nrkseriebase._extract_assets_key({'episodes': None}) == 'episodes'
    assert nrkseriebase._extract_assets_key({'instalments': None}) == 'instalments'
    assert nrkseriebase._entries({'_embedded': None}, nrk_id) is not None
    assert nrkseriebase._catalog_name('podcast') == 'podcast'
    assert nrkseriebase._catalog_name('podkast') == 'podcast'
    assert nrkseriebase._catalog_name('sometype')

# Generated at 2022-06-14 16:48:19.600256
# Unit test for constructor of class NRKPlaylistIE
def test_NRKPlaylistIE():
    """ Unit test for constructor of class NRKPlaylistIE """
    url = 'https://www.nrk.no/troms/gjenopplev-den-historiske-solformorkelsen-1.12270763'
    ie = NRKPlaylistIE(NRKIE(), url)
    assert ie.url == url
    assert ie.playlist_id == 'gjenopplev-den-historiske-solformorkelsen-1.12270763'
    assert ie.playlist_title == 'Gjenopplev den historiske solformørkelsen'
    assert ie.playlist_description == 'md5:c2df8ea3bac5654a26fc2834a542feed'
    assert ie.player_url == None
    assert ie._player_cache == {}
    assert ie

# Generated at 2022-06-14 16:48:30.852015
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    """
    Check that tests for NRK TV Direkte works
    """
    def _test_from_json(json_url):
        url = json_url + '?callback=some.callback.function'
        info_dict = NRKTVDirekteIE._call_api_for_info(json_url, 'testdir')
        assert info_dict == {
            '_type': 'url',
            'id': 'testdir',
            'url': 'nrk:testdir',
            'ie_key': NRKIE.ie_key(),
        }

    # test empty response
    assert not NRKTVDirekteIE._call_api_for_info('https://tv.nrk.no/direkte/dummy', 'dummy')
    # test that the API function named "some.callback.

# Generated at 2022-06-14 16:48:37.065052
# Unit test for constructor of class NRKTVEpisodeIE
def test_NRKTVEpisodeIE():
    url_a = 'https://tv.nrk.no/serie/hellums-kro/sesong/1/episode/2'
    url_b = 'https://tv.nrk.no/serie/backstage/sesong/1/episode/8'
    ie_a = NRKTVEpisodeIE()
    ie_b = NRKTVEpisodeIE()
    assert ie_a != ie_b
    assert ie_a.suitable(url_a)
    assert ie_b.suitable(url_b)
    assert ie_a.suitable(url_b)
    assert ie_b.suitable(url_a)



# Generated at 2022-06-14 16:49:47.834111
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    object = NRKTVSerieBaseIE()



# Generated at 2022-06-14 16:49:48.888440
# Unit test for constructor of class NRKSkoleIE
def test_NRKSkoleIE():
    NRKSkoleIE()

# Generated at 2022-06-14 16:49:51.610014
# Unit test for constructor of class NRKTVSeriesIE
def test_NRKTVSeriesIE():
    _nrktvseriesie = NRKTVSeriesIE
    class TestNRKTVSeriesIE(_nrktvseriesie):
        def _entries(self, data, display_id):
            return []
    test_nrktvseriesie = TestNRKTVSeriesIE.suitable('https://tv.nrk.no/serie/dummy')
    assert test_nrktvseriesie



# Generated at 2022-06-14 16:49:53.029843
# Unit test for constructor of class NRKTVEpisodesIE
def test_NRKTVEpisodesIE():
    """Unit test for constructor of class NRKTVEpisodesIE
    """
    NRKTVEpisodesIE()



# Generated at 2022-06-14 16:49:57.189615
# Unit test for constructor of class NRKTVSeriesIE
def test_NRKTVSeriesIE():
    url = 'https://tv.nrk.no/serie/blank'
    ie = NRKTVSeriesIE(url)
    assert isinstance(ie, NRKTVSeriesIE), 'Not instance of NRKTVSeriesIE'
    assert ie.ie_key() == 'NRKTV', 'Incorrect ie_key()'
    assert ie.url_result.type == 'url', 'Incorrect url_result.type'
    assert ie.url_result.ie_key() == 'NRK', 'Incorrect url_result.ie_key()'



# Generated at 2022-06-14 16:50:05.081641
# Unit test for constructor of class NRKTVEpisodesIE
def test_NRKTVEpisodesIE():
    try:
        with open('test.txt', 'rb') as f:
            html = f.read()
            #html = bytes(map(ord, html))
    except IOError:
        print("File not found")
    else:
        obj = NRKTVEpisodesIE()
        value = obj._TESTS[0]['url']
        result = obj._match_id(value)
        assert result == "69031"


# Generated at 2022-06-14 16:50:14.270422
# Unit test for constructor of class NRKTVSeriesIE
def test_NRKTVSeriesIE():  # type: ignore
    """Test method for NRKTVSeriesIE"""
    url = 'https://tv.nrk.no/serie/dagsrevyen'
    expected_id = 'dagsrevyen'
    expected_title = 'Dagsrevyen'
    ie = NRKTVSeriesIE()
    assert ie.suitable(url)
    ie = ie.suitable(url)()
    # Test that the method of construction of an instance of NRKTVSeriesIE,
    # ie = ie.suitable(url)(), returns an object of the right class
    assert ie.__class__ == NRKTVSeriesIE
    assert expected_id in ie._real_extract(url)  # pylint: disable=W0212
    assert expected_title in ie._real_extract(url)  # pylint:

# Generated at 2022-06-14 16:50:24.114799
# Unit test for constructor of class NRKTVEpisodeIE
def test_NRKTVEpisodeIE():
    obj = NRKTVEpisodeIE()
    assert obj.__class__.__name__ == 'NRKTVEpisodeIE'
    assert isinstance(obj.item_url, compat_str)
    assert obj.item_url == 'https://tv.nrk.no/serie/hellums-kro/sesong/1/episode/2'
    assert isinstance(obj.video_id, compat_str)
    assert obj.video_id == 'MUHH36005220'
    assert isinstance(obj.display_id, compat_str)
    assert obj.display_id == 'hellums-kro/sesong/1/episode/2'
    assert isinstance(obj.display_name, compat_str)

# Generated at 2022-06-14 16:50:24.881253
# Unit test for constructor of class NRKSkoleIE
def test_NRKSkoleIE():
	nrkSKoleIE = NRKSkoleIE()


# Generated at 2022-06-14 16:50:26.243571
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    _ = NRKTVSerieBaseIE('NRKTVSerieBaseIE','nrk.no', 'NRKTV')


# Generated at 2022-06-14 16:51:29.080582
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    NRKTVDirekteIE()



# Generated at 2022-06-14 16:51:39.589983
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    instance = NRKTVSerieBaseIE()
    assert instance._format_id({'foo': 'bar'}) == 'bar'
    assert instance._extract_entries([]) == []

    prf_id = 'MDDP13000210'
    nrk_episode = {'prfId': prf_id}
    episode_id = 'MDDP21000092'
    nrk_episode_bis = {'episodeId': episode_id}
    assert instance._extract_entries([nrk_episode])[0].url == 'nrk:%s' % prf_id
    assert instance._extract_entries([nrk_episode_bis])[0].url == 'nrk:%s' % episode_id

    assert instance._extract_assets_key({'foo': 'bar'}) is None


# Generated at 2022-06-14 16:51:44.808428
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    # Test whether the constructor is able to parse the required arguments
    kwargs = {'video_id': 'test'}
    if isinstance(InfoExtractor.__init__, types.MethodType):
        assert_raises(TypeError, NRKTVSerieBaseIE, **kwargs)
    else:
        nrktvseriebaseie = NRKTVSerieBaseIE(**kwargs)
    assert nrktvseriebaseie and nrktvseriebaseie.video_id == 'test'



# Generated at 2022-06-14 16:51:48.941985
# Unit test for constructor of class NRKIE
def test_NRKIE():
    # Test old URL format
    NRKIE({'url': 'http://www.nrk.no/video/PS*150533'})._real_extract({})
    # Test new URL format
    NRKIE({'url': 'http://www.nrk.no/video/dompap-og-andre-fugler-i-piip-show_150533'})._real_extract({})


# Generated at 2022-06-14 16:51:55.437498
# Unit test for constructor of class NRKPlaylistBaseIE
def test_NRKPlaylistBaseIE():
    nrk_playlist_base_ie = NRKPlaylistBaseIE()
    nrk_playlist_base_ie._extract_title("<title>NRK TV – Se Alle de beste programmene fra NRK</title>")
    nrk_playlist_base_ie._extract_title("<title>NRK TV – Se Alle de beste programmene fra NRK</title>")


# Generated at 2022-06-14 16:51:56.341473
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    ie = NRKTVSerieBaseIE()
    assert ie._AS

# Generated at 2022-06-14 16:52:03.882426
# Unit test for constructor of class NRKTVSeriesIE
def test_NRKTVSeriesIE():
    serie = NRKTVSeriesIE._call_api('tv/catalog/series/besteforeldre', 'besteforeldre', 'serie')
    seriestype = serie['seriesType']
    assert seriestype == 'seriesWithDynamicSeasons'
    
    seasons_json = serie['_embedded']['seasons']
    
    for season in seasons_json:
        season_nrk_id = season['nrkId']
        titles = season['titles']
        title = titles['title']
        season_season = season['season']
        assert season_nrk_id == 'sesong/' + str(season_season)
        assert title == 'Sesong ' + str(season_season)

# Generated at 2022-06-14 16:52:04.782196
# Unit test for constructor of class NRKTVEpisodesIE
def test_NRKTVEpisodesIE():
    from youtube_dl.utils import SearchInfoExtractor

    assert NRKTVEpisodesIE._isinstance(SearchInfoExtractor)

# Generated at 2022-06-14 16:52:06.340668
# Unit test for constructor of class NRKSkoleIE
def test_NRKSkoleIE():
    assert NRKSkoleIE(NRKSkoleIE())._VALID_URL == NRKSkoleIE._VALID_URL


# Generated at 2022-06-14 16:52:12.445698
# Unit test for constructor of class NRKTVSeriesIE