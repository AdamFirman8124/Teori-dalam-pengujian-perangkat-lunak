

# Generated at 2022-06-14 16:46:03.625983
# Unit test for constructor of class NRKTVEpisodeIE
def test_NRKTVEpisodeIE():
    urls = [
        'https://tv.nrk.no/serie/hellums-kro/sesong/1/episode/2',
        'https://tv.nrk.no/serie/backstage/sesong/1/episode/8'
    ]

    for url in urls:
        result = NRKTVEpisodeIE().suitable(url)
        assert result



# Generated at 2022-06-14 16:46:12.195122
# Unit test for constructor of class NRKTVSerieBaseIE

# Generated at 2022-06-14 16:46:15.144560
# Unit test for constructor of class NRKPlaylistBaseIE
def test_NRKPlaylistBaseIE():
    nrk_playlist_base_ie = NRKPlaylistBaseIE()
    assert isinstance(nrk_playlist_base_ie, InfoExtractor)



# Generated at 2022-06-14 16:46:26.305590
# Unit test for constructor of class NRKBaseIE
def test_NRKBaseIE():
    ie = NRKBaseIE()
    assert ie._GEO_COUNTRIES == ['NO']
    assert ie._CDN_REPL_REGEX == '''(?x)://\n        (?:nhttpcache0-47115-cacheod0\.dna\.ip-only\.net/47115-cacheod0|nrkhd-osl-rr\.ntelenorcdn\.net|icdn-od\.nrk\.no/od/nrkhd-osl-rr\.netwerk\.no/no\n        )/'''
    assert ie._GEO_COUNTRIES == ['NO']

# Generated at 2022-06-14 16:46:33.150543
# Unit test for constructor of class NRKBaseIE
def test_NRKBaseIE():
    # Some tests for _extract_nrk_formats
    NRKBaseIE_instance = NRKBaseIE()
    asset_url = 'https://nrkod-httpcache01-fra.dna.ip-only.net/47115-cacheod0/no/playready/152/153/1525226.ism/manifest(format=mpd-time-csf).mpd?bw_low=300&bw_high=2500&no_audio_only=1'
    video_id = '1525226'
    formats = NRKBaseIE_instance._extract_nrk_formats(asset_url, video_id)

# Generated at 2022-06-14 16:46:36.016168
# Unit test for constructor of class NRKPlaylistBaseIE
def test_NRKPlaylistBaseIE():
    url = 'https://tv.nrk.no/serie/blank/sesong/1'
    web_page = '<div id="program-episodes"></div><div id="extra-material"></div>'
    NRKPlaylistBaseIE._real_extract(NRKTVSeasonIE(), url, web_page)



# Generated at 2022-06-14 16:46:40.437804
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    res = NRKTVSeasonIE._extract_entries("[{'prfId': 'ABC'}, {'whatever': 'qwerty'}]")
    assert len(res) == 1 and res[0]['url'] == 'nrk:ABC'
    assert NRKTVSeasonIE._extract_assets_key({"episodes": [1,2,3]}) == "episodes"
    assert NRKTVSeasonIE._extract_assets_key({"instalments": [1,2,3]}) == "instalments"
    assert NRKTVSeasonIE._extract_assets_key({"episodes": [1,2,3], "instalments": [1,2,3]}) == "episodes"

# Generated at 2022-06-14 16:46:45.481328
# Unit test for constructor of class NRKTVEpisodeIE
def test_NRKTVEpisodeIE():
    const = NRKTVEpisodeIE(FakeYDL())
    assert const.IE_DESC == 'NRK TV season episode'
    assert const._VALID_URL == r'https?://tv\.nrk\.no/serie/(?P<id>[^/]+/sesong/(?P<season_number>\d+)/episode/(?P<episode_number>\d+))'

NRKTVChannelIE = create_typed_class(
    'NRKTVChannelIE',
    {
        'Sport': 'NRKSportIE',
        'Super': 'NRKSuperIE',
    },
    dict,
    NRKTVIE.ie_key())



# Generated at 2022-06-14 16:46:47.061603
# Unit test for constructor of class NRKTVEpisodesIE
def test_NRKTVEpisodesIE():
    ie = NRKTVEpisodesIE('https://tv.nrk.no/program/episodes/nytt-paa-nytt/69031')


# Generated at 2022-06-14 16:46:48.705387
# Unit test for constructor of class NRKSkoleIE
def test_NRKSkoleIE():
    aide = NRKSkoleIE()
    assert isinstance(aide, NRKSkoleIE), 'Not of type NRKSkoleIE'

# Generated at 2022-06-14 16:47:55.818608
# Unit test for constructor of class NRKRadioPodkastIE
def test_NRKRadioPodkastIE():
    instance = NRKRadioPodkastIE()
    assert instance._VALID_URL == 'https?://radio\.nrk\.no/pod[ck]ast/(?:[^/]+/)+(?P<id>l_[\da-f]{8}-[\da-f]{4}-[\da-f]{4}-[\da-f]{4}-[\da-f]{12})'



# Generated at 2022-06-14 16:47:58.175484
# Unit test for constructor of class NRKTVSeriesIE
def test_NRKTVSeriesIE():
    with pytest.raises(AssertionError):
        x = NRKTVSeriesIE(None)
    with pytest.raises(Exception):
        x = NRKTVSeriesIE('http://example.com')


# Generated at 2022-06-14 16:48:03.628727
# Unit test for constructor of class NRKPlaylistIE
def test_NRKPlaylistIE():
    # Single entry
    page = """
    <html>
    <div class="featured-video rich" data-video-id="MUHH48000314AA" ...></div>
    </html>
    """
    assert len(list(NRKPlaylistIE()._extract_info_which_not_match_valid_url(page))) == 1

    # Multiple entries
    page = """
    <html>
    <div class="featured-video rich" data-video-id="MUHH48000314AA" ...></div>
    <div class="featured-video rich" data-video-id="MUHH48000315AA" ...></div>
    </html>
    """
    assert len(list(NRKPlaylistIE()._extract_info_which_not_match_valid_url(page))) == 2



# Generated at 2022-06-14 16:48:07.746933
# Unit test for constructor of class NRKPlaylistIE
def test_NRKPlaylistIE():
    url = 'https://www.nrk.no/troms/gjenopplev-den-historiske-solformorkelsen-1.12270763'
    info = NRKPlaylistIE()._real_extract(url)
    assert info['id'] == 'gjenopplev-den-historiske-solformorkelsen-1.12270763'
    assert info['title'] == 'Gjenopplev den historiske solformørkelsen'
    assert info['description'] == 'md5:c2df8ea3bac5654a26fc2834a542feed'
    assert len(info['entries']) == 2



# Generated at 2022-06-14 16:48:08.775095
# Unit test for constructor of class NRKSkoleIE
def test_NRKSkoleIE():
    try:
        ie = NRKSkoleIE
        assert False
    except Exception:
        pass

# Generated at 2022-06-14 16:48:12.262821
# Unit test for constructor of class NRKSkoleIE
def test_NRKSkoleIE():
    # Try to construct object from URL
    NRKSkoleIE("https://www.nrk.no/skole/?page=search&q=&mediaId=14099")
    # Check that object's URL is the same as in constructor
    assert NRKSkoleIE("https://www.nrk.no/skole/?page=search&q=&mediaId=14099")._VALID_URL == "https?://(?:www\.)?nrk\.no/skole/?\?.*\bmediaId=(?P<id>\d+)"


# Generated at 2022-06-14 16:48:16.765153
# Unit test for constructor of class NRKTVEpisodesIE

# Generated at 2022-06-14 16:48:21.284986
# Unit test for constructor of class NRKTVEpisodeIE
def test_NRKTVEpisodeIE():
    # Test constructor of class NRKTVEpisodeIE
    NRKTVEpisodeIE()._real_initialize()

# Generated at 2022-06-14 16:48:24.298563
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    ie = NRKTVSeasonIE()
    assert(str(ie) == "class NRKTVSeasonIE(NRKTVSerieBaseIE)")

# Generated at 2022-06-14 16:48:28.712385
# Unit test for constructor of class NRKPlaylistIE
def test_NRKPlaylistIE():
    ie = NRKPlaylistIE(None)
    assert ie.IE_NAME in NRKPlaylistIE._VALID_URL
    assert ie._VALID_URL == r'https?://(?:www\.)?nrk\.no/(?!video|skole)(?:[^/]+/)+(?P<id>[^/]+)'
    assert ie._TESTS[0]['url'] == 'http://www.nrk.no/troms/gjenopplev-den-historiske-solformorkelsen-1.12270763'
    assert ie._TESTS[0]['playlist_count'] == 2

# Generated at 2022-06-14 16:50:52.202065
# Unit test for constructor of class NRKTVEpisodesIE
def test_NRKTVEpisodesIE():
    def test_object(t, o):
        assert type(o) is t
        assert type(o) is NRKTVEpisodesIE
    test_object(NRKTVEpisodesIE, NRKTVEpisodesIE)



# Generated at 2022-06-14 16:50:55.315418
# Unit test for constructor of class NRKPlaylistBaseIE
def test_NRKPlaylistBaseIE():
    test_cases = ['nrk:ABC123', 'nrk:123456789012']
    for test_case in test_cases:
        nrk_playlistbase_ie = NRKPlaylistBaseIE()
        nrk_playlistbase_ie.url_result(test_case, 'NRKIE')



# Generated at 2022-06-14 16:51:02.533005
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    # pylint: disable=protected-access
    NRKTVDirekteIE._html_webpage_regex = re.compile(
        r'(?s).*?<a.*?href="(?P<url>%s)".+?</script>.*</a>.*' %
        re.escape(NRKTVDirekteIE._VALID_URL), re.DOTALL)
    test_cases = [
        'https://tv.nrk.no/direkte/nrk1',
        'https://tv.nrk.no/direkte/nrk2-tekst-tv',
        'https://radio.nrk.no/direkte/p1_oslo_akershus']

# Generated at 2022-06-14 16:51:03.385034
# Unit test for constructor of class NRKRadioPodkastIE
def test_NRKRadioPodkastIE():
    print(NRKRadioPodkastIE())


# Generated at 2022-06-14 16:51:08.210890
# Unit test for constructor of class NRKTVSeriesIE

# Generated at 2022-06-14 16:51:09.948741
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    ie = NRKTVSerieBaseIE()
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, NRKBaseIE)
    assert isinstance(ie, SearchInfoExtractor)



# Generated at 2022-06-14 16:51:18.496630
# Unit test for constructor of class NRKTVSeriesIE
def test_NRKTVSeriesIE():
    ie = NRKTVSeriesIE()
    assert ie.suitable('https://tv.nrk.no/serie/blank')
    assert ie.suitable('https://nrksuper.no/serie/labyrint')
    assert ie.suitable('https://radio.nrk.no/podkast/ulrikkes_univers')
    assert ie.suitable('https://radio.nrk.no/serie/dickie-dick-dickens/sesong/1/episode/1')
    assert ie.suitable('https://tv.nrk.no/serie/blank/sesong/1/episode/2')
    assert ie.suitable('https://tv.nrk.no/serie/blank/sesong/1')

# Generated at 2022-06-14 16:51:21.706497
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    # It should be possible to instantiate a subclass of NRKTVIE
    assert NRKTVDirekteIE is not None



# Generated at 2022-06-14 16:51:26.465217
# Unit test for constructor of class NRKPlaylistIE
def test_NRKPlaylistIE():
    def _test_NRKPlaylistIE(url, valid, playlist_title, playlist_description, playlist_count):
        nrk_playlist_ie = NRKPlaylistIE()
        assert nrk_playlist_ie.suitable(url) == valid
        nrk_playlist_ie_result = nrk_playlist_ie.extract(url)
        assert nrk_playlist_ie_result['title'] == playlist_title
        assert nrk_playlist_ie_result['description'] == playlist_description
        assert len(nrk_playlist_ie_result['entries']) == playlist_count


# Generated at 2022-06-14 16:51:27.788547
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    NRKTVDirekteIE(NRKTVIE)



# Generated at 2022-06-14 16:54:24.379310
# Unit test for constructor of class NRKIE
def test_NRKIE():
    NRKIE()


# Generated at 2022-06-14 16:54:24.970391
# Unit test for constructor of class NRKPlaylistBaseIE
def test_NRKPlaylistBaseIE():
    assert NRKPlaylistBaseIE



# Generated at 2022-06-14 16:54:26.010955
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    assert NRKTVSeasonIE.suitable('https://tv.nrk.no/serie/backstage/sesong/1')



# Generated at 2022-06-14 16:54:29.985444
# Unit test for constructor of class NRKTVSeriesIE
def test_NRKTVSeriesIE():
    url = 'https://tv.nrk.no/serie/groenn-glede'
    class_ = NRKTVSeriesIE
    assert class_.suitable(url)
    assert class_.suitable('https://tv.nrk.no/serie/blank')
    assert class_.suitable('https://nrksuper.no/serie/labyrint')
    assert class_.suitable('https://tv.nrksuper.no/serie/labyrint')
    assert class_.suitable('https://radio.nrk.no/serie/dickie-dick-dickens')
    assert class_.suitable('https://radio.nrk.no/podkast/ulrikkes_univers')


# Generated at 2022-06-14 16:54:33.521382
# Unit test for constructor of class NRKSkoleIE
def test_NRKSkoleIE():
    link = 'https://www.nrk.no/skole/?page=objectives&subject=naturfag&objective=K15114&mediaId=19355'
    assert NRKSkoleIE().suitable(link)


# Generated at 2022-06-14 16:54:35.682662
# Unit test for constructor of class NRKPlaylistBaseIE
def test_NRKPlaylistBaseIE():
    x = NRKPlaylistBaseIE()
    assert x.IE_DESC == 'NRK Playlist'


# Generated at 2022-06-14 16:54:37.239108
# Unit test for constructor of class NRKIE
def test_NRKIE():
    from . import NRKIE
    return NRKIE()

# Generated at 2022-06-14 16:54:43.753486
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    ie = NRKTVSeasonIE()
    assert ie.suitable('https://tv.nrk.no/serie/backstage/sesong/1')
    assert not ie.suitable('https://tv.nrk.no/serie/kommandoren')
    assert not ie.suitable('https://tv.nrk.no/serie/kommandoren/sesong/1/episode/3')
    assert not ie.suitable('https://radio.nrk.no/podkast/kommandoren/sesong/1')



# Generated at 2022-06-14 16:54:45.298321
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    """
        Test the constructor of class NRKTVSeasonIE
    """
    episode = NRKTVSeasonIE()
    assert isinstance(episode, NRKTVSeasonIE)

# Generated at 2022-06-14 16:54:48.392868
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    nrktv_season_ie = NRKTVSeasonIE()
    assert nrktv_season_ie._VALID_URL == NRKTVSeasonIE._VALID_URL
    assert nrktv_season_ie._TESTS == NRKTVSeasonIE._TESTS
