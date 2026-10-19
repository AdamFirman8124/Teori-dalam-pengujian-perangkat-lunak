

# Generated at 2022-06-14 16:45:50.740816
# Unit test for constructor of class NRKPlaylistIE
def test_NRKPlaylistIE():
    assert NRKPlaylistIE is not None


# Generated at 2022-06-14 16:45:53.421914
# Unit test for constructor of class NRKTVSeriesIE
def test_NRKTVSeriesIE():
    ie = NRKTVSeriesIE()
    assert ie.suitable(NRKTVSeriesIE._VALID_URL)



# Generated at 2022-06-14 16:45:57.521405
# Unit test for constructor of class NRKBaseIE
def test_NRKBaseIE():
    assert NRKBaseIE()


# Generated at 2022-06-14 16:46:01.306030
# Unit test for constructor of class NRKIE
def test_NRKIE():
    assert NRKIE.IE_NAME == 'NRK'
    assert NRKIE.VALID_URL == NRKIE._VALID_URL
    assert NRKIE.IE_DESC == 'NRK'
    assert NRKIE.TEST == NRKIE._TESTS


# Generated at 2022-06-14 16:46:02.590691
# Unit test for constructor of class NRKPlaylistBaseIE
def test_NRKPlaylistBaseIE():
    # This function should return None because it is just a constructor
    return NRKPlaylistBaseIE()


# Generated at 2022-06-14 16:46:09.819680
# Unit test for constructor of class NRKPlaylistBaseIE

# Generated at 2022-06-14 16:46:14.810678
# Unit test for constructor of class NRKPlaylistBaseIE
def test_NRKPlaylistBaseIE():
    ie = NRKPlaylistBaseIE()
    assert ie.suitable('https://tv.nrk.no/programmer') is False
    assert ie.suitable('https://tv.nrk.no/programmer/spill') is True


# Generated at 2022-06-14 16:46:15.756168
# Unit test for constructor of class NRKIE
def test_NRKIE():
    assert(NRKIE.__name__ == "NRKIE")


# Generated at 2022-06-14 16:46:19.257405
# Unit test for constructor of class NRKTVSeriesIE
def test_NRKTVSeriesIE():
    try:
        unit_test = NRKTVSeriesIE("", "", "")
    except:
        failed = True
    assert not failed



# Generated at 2022-06-14 16:46:22.067398
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    url = 'https://radio.nrk.no/podkast/hele_historien/sesong/diagnose-kverulant'
    season_ie = NRKTVSeasonIE()
    obj = season_ie.suitable(url)
    # The answer should be false due to NRKTVSeasonIE is not suitable
    assert not obj
    # The class should not be able to extract any data from this url
    assert not season_ie._real_extract(url)


# Generated at 2022-06-14 16:47:28.027171
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    ie = NRKTVSerieBaseIE()
    assert ie._NRK_API_QUERY == 'https://www.nrk.no/%s/api/%s'
    assert ie._NRK_API_URL == 'https://www.nrk.no/ver/program/%s'
    assert ie._VALID_URL == 'https?://(?:tv|radio)\.nrk\.no/serie/(?P<id>[^/]+)'

# Generated at 2022-06-14 16:47:34.584640
# Unit test for constructor of class NRKBaseIE
def test_NRKBaseIE():
	nrk_base_ie = NRKBaseIE('extractor');
	assert nrk_base_ie.IE_NAME == 'NRKBase'
	assert nrk_base_ie._GEO_COUNTRIES == ['NO']
	assert nrk_base_ie._CDN_REPL_REGEX == '(?x)://\n            nrkod\\d{1,2}-httpcache0-47115-cacheod0\\.dna\\.ip-only\\.net/47115-cacheod0|\n            nrk-od-no\\.telenorcdn\\.net|\n            minicdn-od\\.nrk\\.no/od/nrkhd-osl-rr\\.netwerk\\.no/no\n        /'


# Generated at 2022-06-14 16:47:37.171436
# Unit test for constructor of class NRKTVSeriesIE
def test_NRKTVSeriesIE():
    url = 'https://tv.nrk.no/serie/blank'
    playlist = NRKTVSeriesIE()._real_extract(url)['entries']

    count = 0
    for e in playlist:
        try:
            count += 1
            video = e['_type']
        except KeyError:
            pass
    assert count == 30


# Generated at 2022-06-14 16:47:41.635014
# Unit test for constructor of class NRKTVEpisodesIE
def test_NRKTVEpisodesIE():
    nrktvepisodesie = NRKTVEpisodesIE()
    assert nrktvepisodesie._VALID_URL == r'https?://tv\.nrk\.no/program/[Ee]pisodes/[^/]+/(?P<id>\d+)'
    assert nrktvepisodesie._TESTS == [
        {'url': 'https://tv.nrk.no/program/episodes/nytt-paa-nytt/69031',
         'info_dict': {'id': '69031', 'title': 'Nytt på nytt, sesong: 201210'},
         'playlist_count': 4}
    ]
    assert nrktvepisodesie._ITEM_RE == r'data-episode=["\']%s' % NRKTVIE._

# Generated at 2022-06-14 16:47:46.311234
# Unit test for constructor of class NRKPlaylistIE
def test_NRKPlaylistIE():
    playlist = NRKPlaylistIE()
    assert playlist._VALID_URL == r'https?://(?:www\.)?nrk\.no/(?!video|skole)(?:[^/]+/)+(?P<id>[^/]+)'
    assert playlist._ITEM_RE == r'class="[^"]*\brich\b[^"]*"[^>]+data-video-id="([^"]+)"'
    assert playlist.IE_NAME == 'nrk'
    assert playlist.IE_DESC == 'NRK, NRK Sport and NRK Skole'
    assert playlist.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/1068170485001/default_default/index.html?videoId=%s'
    assert playlist.BRIGHTCOVE_L

# Generated at 2022-06-14 16:47:51.343233
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    # TODO: figure out how to handle live streams
    import httpretty
    from ..utils import fake_httpretty_http
    httpretty.reset()
    fake_httpretty_http(type='live')
    url = 'https://tv.nrk.no/direkte/nrk1'
    with httpretty.activate():
        NRKTVDirekteIE()._real_extract(url)



# Generated at 2022-06-14 16:47:54.900157
# Unit test for constructor of class NRKTVEpisodeIE
def test_NRKTVEpisodeIE():
    assert NRKTVEpisodeIE(None)._VALID_URL == r'https?://tv\.nrk\.no/serie/(?P<id>[^/]+/sesong/(?P<season_number>\d+)/episode/(?P<episode_number>\d+))'

# Generated at 2022-06-14 16:47:57.162215
# Unit test for constructor of class NRKIE
def test_NRKIE():
    tester = NRKIE()
    with pytest.raises(ValueError):
        tester.extract('foo')



# Generated at 2022-06-14 16:47:58.169250
# Unit test for constructor of class NRKPlaylistIE
def test_NRKPlaylistIE():
    try:
        NRKPlaylistIE()
    except Exception as e:
        assert(False)

# Generated at 2022-06-14 16:48:09.597036
# Unit test for constructor of class NRKTVSeriesIE
def test_NRKTVSeriesIE():
    test_input = 'https://tv.nrk.no/serie/blank'

# Generated at 2022-06-14 16:50:10.369254
# Unit test for constructor of class NRKSkoleIE
def test_NRKSkoleIE():
    with pytest.raises(TypeError, message="Constructor of NRKSkoleIE should take 3 arguments."):
        ie = NRKSkoleIE()


# Generated at 2022-06-14 16:50:11.896235
# Unit test for constructor of class NRKIE
def test_NRKIE():
    try:
        NRKIE._extract_nrk_formats(None, None)
    except:
        pass
    else:
        raise Exception('NRKIE._extract_nrk_formats(None, None) should fail')

# Generated at 2022-06-14 16:50:15.008255
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    season = NRKTVSeasonIE()
    print(season)

# Generated at 2022-06-14 16:50:18.702151
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    test_NRKTVSerieBaseIE = NRKTVSerieBaseIE('NRKTVSerieBaseIE','NRK','NRKTV','test_NRKTVSerieBaseIE')
    return test_NRKTVSerieBaseIE


# Generated at 2022-06-14 16:50:24.351205
# Unit test for constructor of class NRKTVEpisodeIE
def test_NRKTVEpisodeIE():
    # Asserts that invalid url url is rejected by constructor
    with pytest.raises(RegexNotFoundError):
        # Invalid url
        NRKTVEpisodeIE('https://tv.nrk.no/serie/backstage/sesong/1/episode/8/')

    # Asserts that valid url is accepted by constructor
    assert NRKTVEpisodeIE.suitable('https://tv.nrk.no/serie/backstage/sesong/1/episode/8') is True



# Generated at 2022-06-14 16:50:26.017614
# Unit test for constructor of class NRKPlaylistBaseIE
def test_NRKPlaylistBaseIE():
    try:
        nrk_playlist = NRKPlaylistBaseIE('https://nrk.no/playlist')
    except:
        pass



# Generated at 2022-06-14 16:50:29.162750
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    ie = NRKTVDirekteIE('nrk1')
    assert ie.IE_KEY == 'nrk:direkte'

# Generated at 2022-06-14 16:50:38.272142
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    ie = NRKTVSerieBaseIE()
    info = ie._extract_entries(None)
    assert not info
    info = ie._extract_entries([])
    assert not info
    info = ie._extract_entries([{'prfId': 'MUHH36005215'}])
    assert len(info) == 1
    assert info[0].video_id == 'MUHH36005215'
    for asset_key in ie._ASSETS_KEYS:
        assert ie._extract_assets_key({asset_key: [1]}) == asset_key
    assert ie._catalog_name('podcast') == 'podcast'
    assert ie._catalog_name('Serie') == 'series'


# Generated at 2022-06-14 16:50:43.285874
# Unit test for constructor of class NRKRadioPodkastIE
def test_NRKRadioPodkastIE():
    # A basic test for constructor of class NRKRadioPodkastIE
    b = NRKRadioPodkastIE('https://radio.nrk.no/podkast/ulrikkes_univers/l_96f4f1b0-de54-4e6a-b4f1-b0de54fe6af8')
    # Test that we get correct video id
    assert(b.video_id == 'l_96f4f1b0-de54-4e6a-b4f1-b0de54fe6af8')
    # Test that we get correct match group

# Generated at 2022-06-14 16:50:47.165466
# Unit test for constructor of class NRKPlaylistIE
def test_NRKPlaylistIE():
    nrkPlaylistIE = NRKPlaylistIE()
    url = "http://www.nrk.no/troms/gjenopplev-den-historiske-solformorkelsen-1.12270763"
    assert nrkPlaylistIE.suitable(url)
    assert not NRKTVIE.suitable(url)
    assert not NRKTVEpisodeIE.suitable(url)
    assert not NRKTVSeasonIE.suitable(url)
    assert not NRKTVSeriesIE.suitable(url)
    assert not NRKTVDirekteIE.suitable(url)
    assert not NRKRadioPodkastIE.suitable(url)
    


# Generated at 2022-06-14 16:51:51.502520
# Unit test for constructor of class NRKIE
def test_NRKIE():
    ie = NRKIE()
    assert re.match(ie._VALID_URL, "http://www.nrk.no/video/PS*150533") is not None

# Generated at 2022-06-14 16:51:53.396719
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    assert NRKTVSeasonIE.__name__ == 'NRKTVSeasonIE'


# Generated at 2022-06-14 16:51:54.738507
# Unit test for constructor of class NRKRadioPodkastIE
def test_NRKRadioPodkastIE():
    ie = NRKRadioPodkastIE('http://radio.nrk.no/podkast/ulrikkes_univers/')
    assert ie.__class__.__name__ == 'NRKRadioPodkastIE'

# Generated at 2022-06-14 16:51:55.904957
# Unit test for constructor of class NRKBaseIE
def test_NRKBaseIE():
    NRKBaseIE(NRKIE())


# Generated at 2022-06-14 16:52:02.049630
# Unit test for constructor of class NRKSkoleIE
def test_NRKSkoleIE():
    class_obj = NRKSkoleIE
    class_obj._TESTS[0]['url']
    nrk_skole_ie_obj = class_obj()
    # The class_obj.suitable function should return TRUE against the URL from class_obj._TESTS[0]['url']
    class_obj.suitable(class_obj._TESTS[0]['url'])
    return nrk_skole_ie_obj._real_extract(class_obj._TESTS[0]['url'])

# Generated at 2022-06-14 16:52:02.883812
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    NRKTVSerieBaseIE()



# Generated at 2022-06-14 16:52:04.516595
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    nrktv_season_ie = NRKTVSeasonIE()
    assert nrktv_season_ie is not None


# Generated at 2022-06-14 16:52:06.255539
# Unit test for constructor of class NRKRadioPodkastIE
def test_NRKRadioPodkastIE():
    if __debug__:
        NRKRadioPodkastIE('https://radio.nrk.no/podkast/bortfoert-i-bergen/l_774d1a2c-7aa7-4965-8d1a-2c7aa7d9652c')

# Generated at 2022-06-14 16:52:07.014866
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    s = NRKTVSeasonIE('')

# Generated at 2022-06-14 16:52:08.456717
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    base_ie = NRKTVSerieBaseIE(NRKTVSerieBaseIE._downloader)
    assert isinstance(base_ie, NRKTVSerieBaseIE)

