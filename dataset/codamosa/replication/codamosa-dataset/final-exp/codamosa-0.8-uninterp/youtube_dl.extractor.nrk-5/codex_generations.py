

# Generated at 2022-06-14 16:45:59.119685
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():
    url = 'http://tv.nrk.no/serie/lindmo/2014/MUHU11003314/avspiller'
    NRKTVIE(NRKTVIE._downloader)._real_extract(url)



# Generated at 2022-06-14 16:46:02.219992
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    ie = NRKTVSerieBaseIE('http://tv.nrk.no')
    print(ie)
    assert ie.downloader is not None
    assert ie.playlist_result_keys == ['id']


# Generated at 2022-06-14 16:46:03.257736
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():
    NRKTVIE('nrk:MDDP12000117')

# Generated at 2022-06-14 16:46:05.209205
# Unit test for constructor of class NRKSkoleIE
def test_NRKSkoleIE():
    ie = NRKSkoleIE('NRK Skole', 'https://www.nrk.no/skole/?page=objectives&subject=naturfag&objective=K15114&mediaId=19355')
    assert ie.ie_key() is NRKIE.ie_key()

# Generated at 2022-06-14 16:46:14.942050
# Unit test for constructor of class NRKTVSeriesIE
def test_NRKTVSeriesIE():
    obj = NRKTVSeriesIE()
    obj.suitable(url='https://tv.nrk.no/serie/backstage')
    obj.suitable(url='https://tv.nrk.no/serie/backstage/sesong/1')
    obj.suitable(url='https://tv.nrk.no/serie/backstage/sesong/1/episode/1')
    obj.suitable(url='https://tv.nrk.no/serie/blank')
    obj.suitable(url='https://tv.nrk.no/serie/blank/sesong/1')
    obj.suitable(url='https://tv.nrk.no/serie/blank/sesong/1/episode/1')

# Generated at 2022-06-14 16:46:16.435094
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():
    for test in NRKTVIE._TESTS:
        yield (test['url'])


# Generated at 2022-06-14 16:46:17.281876
# Unit test for constructor of class NRKRadioPodkastIE
def test_NRKRadioPodkastIE():
    ie = NRKRadioPodkastIE()
    ie.test_urls()


# Generated at 2022-06-14 16:46:19.673990
# Unit test for constructor of class NRKTVEpisodeIE
def test_NRKTVEpisodeIE():
    UnitTestBase(NRKTVEpisodeIE)


# Generated at 2022-06-14 16:46:21.215965
# Unit test for constructor of class NRKIE
def test_NRKIE():
    assert NRKIE('NRK').IE_NAME == NRKIE.IE_NAME



# Generated at 2022-06-14 16:46:24.745109
# Unit test for constructor of class NRKTVEpisodesIE
def test_NRKTVEpisodesIE():
    nrk = NRKTVEpisodesIE()
    assert nrk is not None, "Unable to get instance of NRKPlaylistBaseIE"
    assert nrk._ITEM_RE is not None


# Generated at 2022-06-14 16:47:22.704885
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    NRKTVDirekteIE()



# Generated at 2022-06-14 16:47:23.594550
# Unit test for constructor of class NRKBaseIE
def test_NRKBaseIE():
    NRKBaseIE()

# Generated at 2022-06-14 16:47:31.756421
# Unit test for constructor of class NRKTVSeriesIE
def test_NRKTVSeriesIE():
    t_old = 'https://tv.nrksuper.no/serie/labyrint'
    t_new = 'https://tv.nrk.no/serie/blank'
    u_list = (t_old, t_new)
    for url in u_list:
        m_url = re.match(NRKTVSeriesIE._VALID_URL, url)
        site, serie_kind, series_id = m_url.groups()
        if site == 'nrksuper.no':
            continue
        assert site == 'tv.nrk.no'
        assert series_id == 'blank'
        assert serie_kind == 'serie'
        nrk_series_ie = NRKTVSeriesIE(NRKTVSeriesIE.ie_key())
        nrk_series_ie._real_ext

# Generated at 2022-06-14 16:47:37.493591
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    nrkSeasonIE = NRKTVSeasonIE()

    assert nrkSeasonIE.suitable(NRKTVSeasonIE._TESTS[0]['url'])
    assert not nrkSeasonIE.suitable(NRKTVIE._TESTS[0]['url'])
    assert not nrkSeasonIE.suitable(NRKTVEpisodeIE._TESTS[0]['url'])



# Generated at 2022-06-14 16:47:41.194761
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    url = 'https://radio.nrk.no/podkast/hele_historien/sesong/diagnose-kverulant'
    NRKTVSeasonIE(NRKTVSeasonIE.suitable(url), url)



# Generated at 2022-06-14 16:47:42.638622
# Unit test for constructor of class NRKPlaylistBaseIE
def test_NRKPlaylistBaseIE():
    test_instantiation(NRKPlaylistBaseIE)



# Generated at 2022-06-14 16:47:44.697135
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():
    # Unit test with a dummy API key
    ie = NRKTVIE(api_key='test_api_key')
    assert ie.api_key == 'test_api_key'


# Generated at 2022-06-14 16:47:51.834431
# Unit test for constructor of class NRKPlaylistBaseIE

# Generated at 2022-06-14 16:47:53.700617
# Unit test for constructor of class NRKPlaylistIE
def test_NRKPlaylistIE():
    url = 'http://www.nrk.no/troms/gjenopplev-den-historiske-solformorkelsen-1.12270763'
    obj = NRKPlaylistIE()
    obj.suitable(url) is True


# Generated at 2022-06-14 16:47:54.360612
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    temp = NRKTVSerieBaseIE()



# Generated at 2022-06-14 16:49:56.926138
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    url = 'http://tv.nrk.no/direkte/nrk_super'

# Generated at 2022-06-14 16:50:02.095337
# Unit test for constructor of class NRKSkoleIE
def test_NRKSkoleIE():
    """
    Simple test to confirm that constructor of class NRKSkoleIE don't change
    """
    ie = NRKSkoleIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?nrk\.no/skole/?\?.*\bmediaId=(?P<id>\d+)'
    assert ie._TESTS[0]['url'] == 'https://www.nrk.no/skole/?page=search&q=&mediaId=14099'
    assert ie._TESTS[1]['url'] == 'https://www.nrk.no/skole/?page=objectives&subject=naturfag&objective=K15114&mediaId=19355'

# Generated at 2022-06-14 16:50:03.337867
# Unit test for constructor of class NRKPlaylistBaseIE
def test_NRKPlaylistBaseIE():
    ie = NRKPlaylistBaseIE('url', 'video_id')
    assert 'url' == ie._url
    assert 'video_id' == ie._video_id


# Generated at 2022-06-14 16:50:05.273329
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    serie = NRKTVSerieBaseIE.__new__(NRKTVSerieBaseIE)
    assert serie.__class__.__name__ == 'NRKTVSerieBaseIE'



# Generated at 2022-06-14 16:50:06.811480
# Unit test for constructor of class NRKTVEpisodesIE
def test_NRKTVEpisodesIE():
    instance = NRKTVEpisodesIE()
    assert type(instance) == NRKTVEpisodesIE



# Generated at 2022-06-14 16:50:07.877120
# Unit test for constructor of class NRKPlaylistBaseIE
def test_NRKPlaylistBaseIE():
    playlist_base_ie = NRKPlaylistBaseIE()
    assert isinstance(playlist_base_ie, InfoExtractor)


# Generated at 2022-06-14 16:50:16.145949
# Unit test for constructor of class NRKTVEpisodesIE

# Generated at 2022-06-14 16:50:17.841607
# Unit test for constructor of class NRKPlaylistIE
def test_NRKPlaylistIE():
    # just playing around
    url = "http://www.nrk.no/tema/sommeren-2016/sommerens-utposter-1.12414362"
    NRKPlaylistIE().suitable(url)

# Generated at 2022-06-14 16:50:19.125929
# Unit test for constructor of class NRKTVEpisodesIE
def test_NRKTVEpisodesIE():
    nrk_episodes_test = NRKTVEpisodesIE()
    assert nrk_episodes_test is not None

# Generated at 2022-06-14 16:50:20.820773
# Unit test for constructor of class NRKPlaylistIE
def test_NRKPlaylistIE():
    url = 'http://www.nrk.no/troms/gjenopplev-den-historiske-solformorkelsen-1.12270763'
    # assert that NRKPlaylistIE is constructed with url
    assert NRKPlaylistIE(url)

