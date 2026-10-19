

# Generated at 2022-06-14 16:46:07.840569
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    # To verify that NRKTVDirekteIE inherits NRKTVIE, and that
    # NRKTVDirekteIE.suitable() works correctly.
    test_html = '''
        <html>
        <body>
        <h1>
        <a href="https://tv.nrk.no/direkte/nrk1">
            NRK1</a>
        <h1>
        </body>
        </html>
    '''
    assert NRKTVDirekteIE.suitable(NRKTVDirekteIE._html_search_meta(
        'tv:programId', test_html, 'nrk1'))

# Generated at 2022-06-14 16:46:10.356418
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    nrktvsb = NRKTVSerieBaseIE()
    nrktvsb._extract_entries([])
    nrktvsb._extract_assets_key({})
    nrktvsb._entries([], [])



# Generated at 2022-06-14 16:46:13.521293
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():
    url = 'https://radio.nrk.no/serie/dagsnytt/NPUB21019315/12-07-2015#'
    media_type = 'radio'
    NRKTVIE(media_type, url).match()

# Generated at 2022-06-14 16:46:14.702427
# Unit test for constructor of class NRKPlaylistBaseIE
def test_NRKPlaylistBaseIE():
    NRKPlaylistBaseIE(None, None)


# Generated at 2022-06-14 16:46:17.679145
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    ie = NRKTVDirekteIE(NRKTVDirekteIE._create_ie_instance())
    ie.suitable(NRKTVDirekteIE._VALID_URL)

    assert ie.IE_NAME == 'nrk:direkte'
    assert ie.IE_DESC == 'NRK TV Direkte and NRK Radio Direkte'

# Generated at 2022-06-14 16:46:23.865790
# Unit test for constructor of class NRKTVEpisodesIE
def test_NRKTVEpisodesIE():
    test_input = 'https://tv.nrk.no/program/episodes/nytt-paa-nytt/69031'
    expected_output = test_input
    actual_output = NRKTVEpisodesIE(NRKTVEpisodesIE())._VALID_URL
    assert actual_output == expected_output, "%s should be %s" % (actual_output,expected_output)

# Generated at 2022-06-14 16:46:27.351452
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    assert not NRKTVIE.suitable('https://tv.nrk.no/direkte/nrk1')
    assert NRKTVDirekteIE.suitable('https://tv.nrk.no/direkte/nrk1')



# Generated at 2022-06-14 16:46:37.117780
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    nrktvurl = 'https://tv.nrk.no/direkte/nrk1'
    assert NRKTVDirekteIE.suitable(nrktvurl)
    assert NRKTVDirekteIE.__name__ == 'NRKTVDirekteIE'
    assert NRKTVDirekteIE.ie_key() == 'nrk:direkte'
    assert NRKTVDirekteIE.ie() is NRKTVDirekteIE
    assert NRKTVDirekteIE.ie()._VALID_URL == r'https?://(?:tv|radio)\.nrk\.no/direkte/(?P<id>[^/?#&]+)'



# Generated at 2022-06-14 16:46:39.054879
# Unit test for constructor of class NRKSkoleIE
def test_NRKSkoleIE():
    class_instance = NRKSkoleIE('nrk:6021')
    assert class_instance.ie_key() == 'NRKSkole'
    assert class_instance.course_id == '6021'


# Generated at 2022-06-14 16:46:43.848879
# Unit test for constructor of class NRKRadioPodkastIE
def test_NRKRadioPodkastIE():
    nrkRadioPodkastIE = NRKRadioPodkastIE()
    nrkRadioPodkastIE.IE_DESC = 'NRK Radio Direkte'
    nrkRadioPodkastIE.IE_NAME = 'nrk'
    nrkRadioPodkastIE._VALID_URL = r'http://radio\.nrk\.no/podkast/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:47:49.313668
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    NRKTVSerieBaseIE('nrktvseriebase')

# Generated at 2022-06-14 16:47:50.357061
# Unit test for constructor of class NRKSkoleIE
def test_NRKSkoleIE():
    # The constructor should return a instance of NRKSkoleIE
    assert(NRKSkoleIE() is not None)

# Generated at 2022-06-14 16:47:52.123093
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    instance = NRKTVSeasonIE(NRKBaseIE())
    assert isinstance(instance, InfoExtractor)


# Generated at 2022-06-14 16:47:55.339255
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    # Basic test to assure that the constructor works
    NRKTVSeasonIE.suitable('https://radio.nrk.no/podkast/hele_historien/sesong/diagnose-kverulant')



# Generated at 2022-06-14 16:47:58.245423
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    try:
        NRKTVDirekteIE()._real_extract('')
    except NameError as e:
        assert '_live_title' in str(e)



# Generated at 2022-06-14 16:48:02.039852
# Unit test for constructor of class NRKIE
def test_NRKIE():
    return NRKIE()._call_api("playback/manifest/ecc1b952-96dc-4a98-81b9-5296dc7a98d9", "ecc1b952-96dc-4a98-81b9-5296dc7a98d9", "manifest")


# Generated at 2022-06-14 16:48:03.965075
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    url = 'https://tv.nrk.no/serie/backstage/sesong/1'
    NRKTVSeasonIE(None, url)


# Generated at 2022-06-14 16:48:08.286592
# Unit test for constructor of class NRKBaseIE
def test_NRKBaseIE():
    ie = NRKBaseIE()
    # Verify that _GEO_COUNTRIES is set correctly
    assert(ie._GEO_COUNTRIES == ['NO'])


# Generated at 2022-06-14 16:48:10.777147
# Unit test for constructor of class NRKSkoleIE
def test_NRKSkoleIE():
    ydl = YoutubeDL()
    ydl.add_default_info_extractors()
    ie = NRKSkoleIE(ydl)
    if ie.IE_DESC != 'NRK Skole':
        assert False, "Variable IE_DESC should be 'NRK Skole'. It is now: %s" % ie.IE_DESC

# Generated at 2022-06-14 16:48:15.956982
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():
    # Radio URL
    # Taken from
    # https://github.com/rg3/youtube-dl/issues/4993#issuecomment-203039015
    NRKTVIE('https://radio.nrk.no/serie/dagsnytt/NPUB21019315/12-07-2015#')


# Generated at 2022-06-14 16:49:10.963273
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    nrk_tv_season = NRKTVSeasonIE()
    assert nrk_tv_season.suitable('https://tv.nrk.no/serie/backstage/sesong/1')
    assert not nrk_tv_season.suitable('https://tv.nrk.no/program/80000280')


# Generated at 2022-06-14 16:49:15.923827
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    test_object = NRKTVSerieBaseIE()
    assert(test_object.__class__.__name__ == 'NRKTVSerieBaseIE')
    assert(test_object.ie_key() == 'NRKTVSerieBase')
    assert(test_object.ie_key() != 'nrk')


# Generated at 2022-06-14 16:49:25.271032
# Unit test for constructor of class NRKTVEpisodeIE
def test_NRKTVEpisodeIE():
    url = 'https://tv.nrk.no/serie/hellums-kro/sesong/1/episode/2'
    nrk_tv_episode = NRKTVEpisodeIE()
    assert nrk_tv_episode._VALID_URL == 'https?://tv\.nrk\.no/serie/(?P<id>[^/]+/sesong/(?P<season_number>\d+)/episode/(?P<episode_number>\d+))'
    assert nrk_tv_episode._match_id(url) == 'hellums-kro/sesong/1/episode/2'
    assert nrk_tv_episode._download_webpage(url, 'hellums-kro/sesong/1/episode/2') is not None
    assert nrk_tv_episode._search_

# Generated at 2022-06-14 16:49:26.897071
# Unit test for constructor of class NRKSkoleIE
def test_NRKSkoleIE():
    ok = NRKSkoleIE()

# Generated at 2022-06-14 16:49:30.649330
# Unit test for constructor of class NRKRadioPodkastIE
def test_NRKRadioPodkastIE():
    NRKRadioPodkastIE('http://radio.nrk.no/podkast/ulrikkes_univers/l_96f4f1b0-de54-4e6a-b4f1-b0de54fe6af8')

# Generated at 2022-06-14 16:49:31.363600
# Unit test for constructor of class NRKTVEpisodeIE
def test_NRKTVEpisodeIE():
    NRKTVEpisodeIE()


# Generated at 2022-06-14 16:49:34.912312
# Unit test for constructor of class NRKPlaylistIE
def test_NRKPlaylistIE(): 
    try:
        NRKPlaylistIE()
    except Exception as e:
        print( "Error is: ", e.args[0] )
        assert False, "Unexpected error in NRKPlaylistIE constructor"
    assert True, "Success in NRKPlaylistIE constructor"



# Generated at 2022-06-14 16:49:35.640681
# Unit test for constructor of class NRKBaseIE
def test_NRKBaseIE():
    assert NRKBaseIE()


# Generated at 2022-06-14 16:49:45.865604
# Unit test for constructor of class NRKPlaylistIE

# Generated at 2022-06-14 16:49:46.240518
# Unit test for constructor of class NRKIE
def test_NRKIE():
    NRKIE()

# Generated at 2022-06-14 16:52:05.126343
# Unit test for constructor of class NRKTVSeriesIE
def test_NRKTVSeriesIE():
    assert NRKTVSeriesIE.suitable(NRKTVEpisodeIE._VALID_URL) == False
    assert NRKTVSeriesIE.suitable(NRKTVEpisodeIE._VALID_URL2) == False
    assert NRKTVSeriesIE.suitable(NRKTVEpisodeIE._VALID_URL3) == False
    assert NRKTVSeriesIE.suitable(NRKTVSeasonIE._VALID_URL) == False

# Generated at 2022-06-14 16:52:11.206909
# Unit test for constructor of class NRKIE
def test_NRKIE():
    try:
        from pprint import pprint
    except ImportError:
        from six.moves import pprint

    # Create an instance of the IE
    nrk = NRKIE()

    # Download information about a video.
    pprint(nrk._call_api('programs/MDDP12000117', 'MDDP12000117', 'programs'))

    # Download information about a non-existen video.
    # pprint(nrk._call_api('programs/MDDP12000000', 'MDDP12000000', 'programs'))

    # Download a video.
    # info = nrk._real_extract('nrk:MDDP12000117')

    # Print some information about the video.
    # pprint(info)


# Generated at 2022-06-14 16:52:14.968134
# Unit test for constructor of class NRKIE
def test_NRKIE():
    ie = NRKIE()
    print(repr(ie))
    assert ie.IE_NAME == 'nrk'
    assert ie._VALID_URL == '''(?x)
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


# Generated at 2022-06-14 16:52:18.275386
# Unit test for constructor of class NRKIE
def test_NRKIE():
    assert NRKIE()._GEO_COUNTRIES == ['NO']
    assert NRKIE()._CDN_REPL_REGEX == r'(?x)://(?:nrkod\d{1,2}-httpcache0-47115-cacheod0\.dna\.ip-only\.net/47115-cacheod0|nrk-od-no\.telenorcdn\.net|minicdn-od\.nrk\.no/od/nrkhd-osl-rr\.netwerk\.no/no)/'


# Generated at 2022-06-14 16:52:21.816579
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    import unittest
    class TestNRKTVSeasonIE(unittest.TestCase):
        def setUp(self):
            self.constructor = NRKTVSeasonIE

        def test_instantiating_NRKTVSeasonIE_instantiates_NRKTVSeasonIE(self):
            my_NRKTVSeasonIE = self.constructor('my_NRKTVSeasonIE')
            assert isinstance(my_NRKTVSeasonIE,
                              NRKTVSeasonIE)
    unittest.main()



# Generated at 2022-06-14 16:52:24.087840
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    serie_base = NRKTVSerieBaseIE()
    assert serie_base._ASSETS_KEYS == ('episodes', 'instalments')
    assert serie_base._catalog_name('podcast') == 'podcast'
    assert serie_base._catalog_name('series') == 'series'


# Generated at 2022-06-14 16:52:28.535913
# Unit test for constructor of class NRKPlaylistIE
def test_NRKPlaylistIE():
    i = NRKPlaylistIE()
    assert i._VALID_URL == r'https?://(?:www\.)?nrk\.no/(?!video|skole)(?:[^/]+/)+(?P<id>[^/]+)'
    assert i._ITEM_RE == r'class="[^"]*\brich\b[^"]*"[^>]+data-video-id="([^"]+)"'

# Generated at 2022-06-14 16:52:30.053915
# Unit test for constructor of class NRKPlaylistIE
def test_NRKPlaylistIE():
    instance = NRKPlaylistIE('NRKPlaylistIE', 'http://www.nrk.no/kultur/bok/rivertonprisen-til-karin-fossum-1.12266449')



# Generated at 2022-06-14 16:52:33.376898
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    '''
    Constructor of class NRKTVDirekteIE
    '''
    # Only execute constructor, no assertions necessary
    NRKTVDirekteIE()

# Generated at 2022-06-14 16:52:34.477192
# Unit test for constructor of class NRKSkoleIE
def test_NRKSkoleIE():
    ie = NRKSkoleIE()
    obj = ie.ie_key()
    assert (obj == 'NRKSkole')