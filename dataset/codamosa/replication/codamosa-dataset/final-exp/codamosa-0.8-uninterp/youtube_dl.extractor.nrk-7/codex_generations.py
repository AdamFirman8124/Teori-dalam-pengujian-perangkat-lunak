

# Generated at 2022-06-14 16:46:02.785549
# Unit test for constructor of class NRKTVEpisodesIE
def test_NRKTVEpisodesIE():
    try:
        NRKTVEpisodesIE()
    except NotImplementedError:
        pass



# Generated at 2022-06-14 16:46:10.275115
# Unit test for constructor of class NRKBaseIE
def test_NRKBaseIE():
    # Testing the video url detection
    instance = InfoExtractor(NRKBaseIE.ie_key())
    video_url = instance._match_id(NRKBaseIE.ie_key(), 'http://tv.nrk.no/serie/dag')
    assert video_url is None
    video_url = instance._match_id(NRKBaseIE.ie_key(), 'http://tv.nrk.no/serie/alpint/dkxk12001812/18-12-2012#')
    assert video_url == 'dkxk12001812'
    url = instance._match_id(NRKBaseIE.ie_key(), 'http://tv.nrk.no/serie/jul-i-blaafarvevÃ¦rket')
    assert url is None
    url = instance._match_

# Generated at 2022-06-14 16:46:11.153390
# Unit test for constructor of class NRKBaseIE
def test_NRKBaseIE():
    pass



# Generated at 2022-06-14 16:46:12.220080
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    obj = NRKTVSeasonIE()
    obj.suitable(None)


# Generated at 2022-06-14 16:46:18.884003
# Unit test for constructor of class NRKIE
def test_NRKIE():
    assert NRKIE.IE_NAME == 'nrk:video'
    assert NRKIE.IE_DESC == 'NRK (video)'
    assert NRKIE._VALID_URL == r'''(?x)
                        (?:
                            nrk:|
                            https?://
                                (?:
                                    (?:www\.)?nrk\.no/video/(?:PS\*|[^_]+_)|
                                    v8[-.]psapi\.nrk\.no/mediaelement/
                                )
                            )
                            (?P<id>[^?\#&]+)
                        '''



# Generated at 2022-06-14 16:46:21.566995
# Unit test for constructor of class NRKPlaylistBaseIE
def test_NRKPlaylistBaseIE():
    ie = NRKPlaylistBaseIE()
    assert ie._match_id('https://tv.nrk.no/serie/krim/sesong/1/episode/1') != None
    assert ie.IE_DESC == 'NRK Playlist'


# Generated at 2022-06-14 16:46:26.806161
# Unit test for constructor of class NRKRadioPodkastIE
def test_NRKRadioPodkastIE():
    expected = [
        'nrk:l_96f4f1b0-de54-4e6a-b4f1-b0de54fe6af8',
        'nrk:l_774d1a2c-7aa7-4965-8d1a-2c7aa7d9652c'
    ]
    url1 = 'https://radio.nrk.no/podkast/ulrikkes_univers/l_96f4f1b0-de54-4e6a-b4f1-b0de54fe6af8'

# Generated at 2022-06-14 16:46:27.326175
# Unit test for constructor of class NRKPlaylistBaseIE
def test_NRKPlaylistBaseIE():
    pass


# Generated at 2022-06-14 16:46:35.197756
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():
    ie = NRKTVIE()
    assert ie.IE_DESC == 'NRK TV and NRK Radio'
    assert ie.IE_NAME == 'nrk'
    for url in (
            'https://tv.nrk.no/program/MDDP12000117',
            'https://tv.nrk.no/serie/tour-de-ski/MSPO40010515/06-01-2015#del=2'):
        assert ie.suitable(url), 'url %s is un-matchable' % url


# Generated at 2022-06-14 16:46:42.046900
# Unit test for constructor of class NRKTVSeriesIE
def test_NRKTVSeriesIE():
    nrk_tv_series_ie = NRKTVSeriesIE('NRKTVSeries', 'no', 'tv.nrk.no')

    assert nrk_tv_series_ie._VALID_URL == NRKTVSeriesIE._VALID_URL
    assert nrk_tv_series_ie._TESTS == NRKTVSeriesIE._TESTS
    assert nrk_tv_series_ie.ie_key() == 'NRKTVSeries'
    assert nrk_tv_series_ie.ie_key() == 'NRKTVSeries'
    assert nrk_tv_series_ie.ie_key() == 'NRKTVSeries'
    assert nrk_tv_series_ie.ie_key() == 'NRKTVSeries'
    assert nrk_tv_series_ie.ie_key

# Generated at 2022-06-14 16:48:11.356022
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():
    klass = NRKTVIE
    klass._TESTS[0].update({
        'expected_warnings': ['A URL appearing to be a playlist was given, '
                             'but no format found that matches nrk'],
    })
    nrk_tv_ie = klass()
    assert nrk_tv_ie.ie_key() == 'nrk'
    assert nrk_tv_ie.ie_key() == klass.ie_key()
    assert nrk_tv_ie.SUCCESS == klass.SUCCESS
    assert nrk_tv_ie.FAILED == klass.FAILED

# Generated at 2022-06-14 16:48:16.621195
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    nrk_tv_serie_base_ie = NRKTVSerieBaseIE()
    # Unit test for method _catalog_name
    assert nrk_tv_serie_base_ie._catalog_name('podcast') == 'podcast'
    assert nrk_tv_serie_base_ie._catalog_name('podcast_') == 'series'



# Generated at 2022-06-14 16:48:18.327852
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    NRKTVSerieBaseIE('NRKTVSerieBaseIE', 'nrk.no')


# Generated at 2022-06-14 16:48:22.920861
# Unit test for constructor of class NRKTVSeriesIE
def test_NRKTVSeriesIE():
    nrk_tv_series_ie = NRKTVSeriesIE()
    assert isinstance(nrk_tv_series_ie, NRKTVSeriesIE)


# Generated at 2022-06-14 16:48:23.738970
# Unit test for constructor of class NRKPlaylistBaseIE
def test_NRKPlaylistBaseIE():
    info = NRKPlaylistBaseIE()
    assert info



# Generated at 2022-06-14 16:48:26.620446
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    url = 'https://radio.nrk.no/podkast/hele_historien/sesong/diagnose-kverulant'
    assert NRKTVSeasonIE.suitable(url) == True


# Generated at 2022-06-14 16:48:31.003712
# Unit test for constructor of class NRKTVIE

# Generated at 2022-06-14 16:48:33.974492
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    assert 'NRKTVSerieBaseIE' == NRKTVSerieBaseIE.__name__


# Generated at 2022-06-14 16:48:39.659415
# Unit test for constructor of class NRKIE
def test_NRKIE():
    # Test constructor
    class_nrkie = NRKIE()
    assert class_nrkie._GEO_COUNTRIES == ['NO']
    assert class_nrkie._CDN_REPL_REGEX == r'''(?x)://
        (?:
            nrkod\d{1,2}-httpcache0-47115-cacheod0\.dna\.ip-only\.net/47115-cacheod0|
            nrk-od-no\.telenorcdn\.net|
            minicdn-od\.nrk\.no/od/nrkhd-osl-rr\.netwerk\.no/no
        )/'''


# Generated at 2022-06-14 16:48:40.377147
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    instance = NRKTVSeasonIE()


# Generated at 2022-06-14 16:51:35.356607
# Unit test for constructor of class NRKIE
def test_NRKIE():
    nrk = NRKIE()
    nrk._extract_nrk_formats('https://nrk-od-16.akamaized.net/no/150533/150533_hls-f-a1,600,1200,2500,5000,10000,25000,.m3u8', '150533')
    nrk._extract_nrk_formats('https://nrk-od-16.akamaized.net/no/150533-150533_hls-f-a1,600,1200,2500,5000,10000,25000,.m3u8', '150533')

# Generated at 2022-06-14 16:51:36.863591
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    # test constructor of class NRKTVSeasonIE
    assert NRKTVSeasonIE(NRKTVSeasonIE.suitable('NRKTVSeason'))


# Generated at 2022-06-14 16:51:41.119060
# Unit test for constructor of class NRKTVEpisodesIE
def test_NRKTVEpisodesIE():
    class_object = NRKTVEpisodesIE()
    assert (class_object.suitable("Some not valid URL")) == False
    assert (class_object.suitable("https://tv.nrk.no/program/episodes/nytt-paa-nytt/69031")) == True

# Generated at 2022-06-14 16:51:43.766706
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    def check_variables(NRKTVSerieBaseIE):
        assert NRKTVSerieBaseIE._ASSETS_KEYS == ('episodes', 'instalments',)

    check_variables(NRKTVSerieBaseIE)


# Generated at 2022-06-14 16:51:44.840822
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    obj = NRKTVSerieBaseIE()
    assert obj is not None


# Generated at 2022-06-14 16:51:49.272245
# Unit test for constructor of class NRKTVEpisodeIE
def test_NRKTVEpisodeIE():
    assert re.match(NRKTVEpisodeIE._VALID_URL, 'https://tv.nrk.no/serie/hellums-kro/sesong/1/episode/2') is not None
    assert re.match(NRKTVEpisodeIE._VALID_URL, 'https://tv.nrk.no/serie/backstage/sesong/1/episode/8') is not None
    assert re.match(NRKTVEpisodeIE._VALID_URL, 'https://tv.nrk.no/serie/jul_i_blaafarvevaerket/sesong/1/episode/1') is not None


# Generated at 2022-06-14 16:51:55.570391
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():
    nrktvie = NRKTVIE()
    assert nrktvie._EPISODE_RE == r'(?P<id>[a-zA-Z]{4}\d{8})'
    assert nrktvie._VALID_URL == r'https?://(?:tv|radio)\.nrk(?:super)?\.no/(?:[^/]+/)*%s' % nrktvie._EPISODE_RE

# Generated at 2022-06-14 16:51:56.596195
# Unit test for constructor of class NRKPlaylistIE
def test_NRKPlaylistIE():
    s = NRKPlaylistBaseIE()
    assert s

if __name__ == '__main__':
    test_NRKPlaylistIE()

# Generated at 2022-06-14 16:51:57.957030
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():
    NRKTVIE('nrk:MDDP12000117')

# Generated at 2022-06-14 16:51:59.129986
# Unit test for constructor of class NRKBaseIE
def test_NRKBaseIE():
    # Create an instance of NRKBaseIE
    NRKBaseIE()
