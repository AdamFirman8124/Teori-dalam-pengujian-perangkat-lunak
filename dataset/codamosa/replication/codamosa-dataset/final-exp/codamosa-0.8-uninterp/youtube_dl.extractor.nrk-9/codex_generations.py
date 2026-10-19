

# Generated at 2022-06-14 16:46:03.358116
# Unit test for constructor of class NRKPlaylistBaseIE
def test_NRKPlaylistBaseIE():
    ie = NRKPlaylistBaseIE()
    assert ie.suitable('https://tv.nrk.no/programoversikt/kategorier')
    assert ie.suitable('https://radio.nrk.no/kategori/lokalradioer')
    assert not ie.suitable('https://tv.nrk.no')
    assert not ie.suitable('https://tv.nrk.no/programoversikt/kategorier/default.html')
    assert not ie.suitable('https://radio.nrk.no/')
    assert not ie.suitable('https://radio.nrk.no/programoversikt/kategorier/default.html')



# Generated at 2022-06-14 16:46:04.094708
# Unit test for constructor of class NRKPlaylistBaseIE
def test_NRKPlaylistBaseIE():
    assert(NRKPlaylistBaseIE)


# Generated at 2022-06-14 16:46:13.794721
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():
    instance = NRKTVIE('https://tv.nrk.no/program/MDDP12000117')
    assert isinstance(instance, NRKTVIE)
    assert instance.IE_NAME == 'NRK'
    assert instance.IE_DESC == 'NRK TV and NRK Radio'

# Generated at 2022-06-14 16:46:15.003111
# Unit test for constructor of class NRKRadioPodkastIE
def test_NRKRadioPodkastIE():
    ie = NRKRadioPodkastIE()
    ie.suitable(NRKRadioPodkastIE._VALID_URL)



# Generated at 2022-06-14 16:46:23.527794
# Unit test for constructor of class NRKTVEpisodeIE
def test_NRKTVEpisodeIE():
    url = "https://tv.nrk.no/serie/hellums-kro/sesong/1/episode/2"
    inst = NRKTVEpisodeIE()
    assert inst._VALID_URL == "https?://tv\.nrk\.no/serie/(?P<id>[^/]+/sesong/(?P<season_number>\d+)/episode/(?P<episode_number>\d+))"
    assert inst._TESTS[0]["url"] == url

# Test for constructor of class NRKTVIE

# Generated at 2022-06-14 16:46:24.815451
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():
    try:
        from IPython import embed; embed()
    except ImportError:
        pass


# Generated at 2022-06-14 16:46:35.327581
# Unit test for constructor of class NRKTVEpisodesIE
def test_NRKTVEpisodesIE():
    ie = NRKTVEpisodesIE()
    assert ie._VALID_URL == 'https?://tv\.nrk\.no/program/[Ee]pisodes/[^/]+/(?P<id>\d+)'
    assert ie._ITEM_RE == r'data-episode=["\']%s' % NRKTVIE._EPISODE_RE
    assert ie._TESTS == [{
        'url': 'https://tv.nrk.no/program/episodes/nytt-paa-nytt/69031',
        'info_dict': {
            'id': '69031',
            'title': 'Nytt på nytt, sesong: 201210',
        },
        'playlist_count': 4,
    }]

# Generated at 2022-06-14 16:46:38.264651
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    # Make sure NRKTVDirekteIE also has a constructor for the abstract class NRKBaseIE
    direkte = NRKTVDirekteIE.suitable('https://tv.nrk.no/direkte/nrk1')
    assert direkte

# Generated at 2022-06-14 16:46:44.164832
# Unit test for constructor of class NRKTVEpisodesIE
def test_NRKTVEpisodesIE():
    from youtube_dl.extractor import InfoExtractor
    from youtube_dl.extractor import gen_extractors
    from urllib.parse import urlparse, parse_qs
    from youtube_dl.utils import ExtractorError

    extractors = gen_extractors()
    exclude_ie = [NRKTVIE]
    extractors = [e for e in extractors if e.ie_key() not in exclude_ie]

    # TODO: Better check than just checking the constructor
    #       since not all extractors are realized with NRKTVEpisodesIE,
    #       sometimes with general NRKPlaylistIE

    # Resolves the problem with:
    #   1. NRKTVIE.suitable() is True, so NRKTVIE should be chosen
    #   2. NRKTVEpisodesIE.suitable() is also True

# Generated at 2022-06-14 16:46:46.734395
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():
    # This is a simple test for constructing a NRKTVIE object
    instance = NRKTVIE('https://radio.nrk.no/serie/dagsnytt/NPUB21019315/12-07-2015#')
    assert instance is not None

# Generated at 2022-06-14 16:48:02.297985
# Unit test for constructor of class NRKRadioPodkastIE
def test_NRKRadioPodkastIE():
    nrkRadioPodkastIE = NRKRadioPodkastIE()
    assert nrkRadioPodkastIE.suitable("https://radio.nrk.no/podkast/ulrikkes_univers/l_96f4f1b0-de54-4e6a-b4f1-b0de54fe6af8") == True
    assert nrkRadioPodkastIE.suitable("https://radio.nrk.no/podkast") == False
    assert nrkRadioPodkastIE.suitable("https://radio.nrk.no/podkast/") == False

# Generated at 2022-06-14 16:48:02.861153
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    pass



# Generated at 2022-06-14 16:48:13.307925
# Unit test for constructor of class NRKIE
def test_NRKIE():
    # Given
    non_valid_url1 = 'https://www.nrk.no/sfasdfsafasf'
    non_valid_url2 = 'https://www.nrk.no/sfasdfsafasf_150533'

    # When
    instance1 = NRKIE()
    instance2 = NRKIE()

    # Then
    assert (not instance1._VALID_URL_RE.match(non_valid_url1))
    assert (not instance2._VALID_URL_RE.match(non_valid_url2))



# Generated at 2022-06-14 16:48:15.412473
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():
    ie = NRKTVIE()
    expected_instance = NRKTVIE
    assert(ie.__class__ == expected_instance)

# Generated at 2022-06-14 16:48:21.388093
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    info = NRKTVSeasonIE()._real_extract('https://tv.nrk.no/serie/backstage/sesong/1')
    assert info['id'] == 'backstage/1'
    assert info['title'] == 'Sesong 1'



# Generated at 2022-06-14 16:48:32.017506
# Unit test for constructor of class NRKTVSeriesIE

# Generated at 2022-06-14 16:48:33.246382
# Unit test for constructor of class NRKTVEpisodesIE
def test_NRKTVEpisodesIE():
    obj = NRKTVEpisodesIE()
    obj.suitable('https://tv.nrk.no/program/episodes/nytt-paa-nytt/69031')

# Generated at 2022-06-14 16:48:35.262244
# Unit test for constructor of class NRKBaseIE
def test_NRKBaseIE():
    ie = NRKBaseIE('NrkBaseIE', 'NrkBaseIE/1.0.0')


# Generated at 2022-06-14 16:48:37.685134
# Unit test for constructor of class NRKTVEpisodesIE
def test_NRKTVEpisodesIE():
    epiIE = NRKTVEpisodesIE(None)
    assert epiIE._ITEM_RE == r'data-episode=["\']%s' % NRKTVIE._EPISODE_RE
    assert epiIE._VALID_URL == r'https?://tv\.nrk\.no/program/[Ee]pisodes/[^/]+/(?P<id>\d+)'



# Generated at 2022-06-14 16:48:45.996777
# Unit test for constructor of class NRKIE
def test_NRKIE():
    a = NRKIE()
    assert a._GEO_COUNTRIES == ['NO']
    assert a._CDN_REPL_REGEX == '://nrkod\\d{1,2}-httpcache0-47115-cacheod0\\.dna\\.ip-only\\.net/47115-cacheod0|' + \
                                '://nrk-od-no\\.telenorcdn\\.net|' + \
                                '://minicdn-od\\.nrk\\.no/od/nrkhd-osl-rr\\.netwerk\\.no/no/'


# Generated at 2022-06-14 16:51:20.137198
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():
    ie = NRKTVIE()

# Generated at 2022-06-14 16:51:24.806893
# Unit test for constructor of class NRKRadioPodkastIE
def test_NRKRadioPodkastIE():
    video_id = 'l_96f4f1b0-de54-4e6a-b4f1-b0de54fe6af8'
    result = NRKRadioPodkastIE()._real_extract(
        'https://radio.nrk.no/podcast/ulrikkes_univers/l_96f4f1b0-de54-4e6a-b4f1-b0de54fe6af8')
    assert result['id'] == 'nrk:' + video_id
    assert result['video_id'] == video_id
    assert result['url'] == 'nrk:%s' % video_id
    assert result['ie_key'] == 'NRK'

# Generated at 2022-06-14 16:51:26.358491
# Unit test for constructor of class NRKBaseIE
def test_NRKBaseIE():
    assert NRKBaseIE().IE_NAME == 'nrk'

# Generated at 2022-06-14 16:51:35.070767
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    ie = NRKTVDirekteIE()
    assert ie.ie_key() == 'NRKTVDirekte'
    assert ie.ie_desc() == 'NRK TV Direkte and NRK Radio Direkte'
    assert ie.ie_key() == 'NRKTVDirekte'
    assert ie.IE_DESC == 'NRK TV Direkte and NRK Radio Direkte'
    assert ie.suitable(
        'https://tv.nrk.no/direkte/nrk1'
    ) == True
    assert ie.suitable(
        'https://tv.nrk.no/direkte/nrk1ss'
    ) == False
    assert ie.suitable(
        'https://tv.nrk.no/program/'
    ) == False



# Generated at 2022-06-14 16:51:41.335363
# Unit test for constructor of class NRKTVSeriesIE
def test_NRKTVSeriesIE():
    import requests_mock

# Generated at 2022-06-14 16:51:47.350761
# Unit test for constructor of class NRKTVEpisodeIE
def test_NRKTVEpisodeIE():
    assert NRKTVEpisodeIE()._VALID_URL == 'https?://tv\.nrk\.no/serie/(?P<id>[^/]+/sesong/(?P<season_number>\\d+)/episode/(?P<episode_number>\\d+))'
    assert NRKTVEpisodeIE()._TESTS[0]['url'] == 'https://tv.nrk.no/serie/hellums-kro/sesong/1/episode/2'

# Generated at 2022-06-14 16:51:49.739122
# Unit test for constructor of class NRKIE
def test_NRKIE():
    url = "http://www.nrk.no/video/PS*150533"
    NRKIE()
    NRKBaseIE()



# Generated at 2022-06-14 16:51:53.093633
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    nrktvseason_ie = NRKTVSeasonIE(NRKTVSeasonIE._VALID_URL)
    nrktvseason_ie.suitable(NRKTVSeasonIE._VALID_URL)



# Generated at 2022-06-14 16:51:55.037319
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    assert isinstance(NRKTVSeasonIE()._VALID_URL, re._pattern_type)



# Generated at 2022-06-14 16:52:00.579380
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    test_url = 'https://tv.nrk.no/serie/bonderomantikk'
    url_object = urlparse(test_url)
    nrktvseriebase_object = NRKTVSerieBaseIE()
    # test _VALID_URL
    assert nrktvseriebase_object._VALID_URL == None
    # test _TESTS
    assert nrktvseriebase_object._TESTS == [{
        'url': 'https://tv.nrk.no/serie/bonderomantikk',
        'info_dict': {
            'id': 'serie/bonderomantikk',
            'title': 'Bonderomantikk',
        },
        'playlist_count': 500,
    }]
    # test _PAGE_COUNT
