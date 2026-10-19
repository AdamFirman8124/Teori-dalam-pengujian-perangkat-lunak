

# Generated at 2022-06-14 16:46:03.837980
# Unit test for constructor of class NRKTVSeriesIE
def test_NRKTVSeriesIE():
    """Test constructor of NRKTVSeriesIE with correct URL.

    It should be able to construct the correct class.
    """
    url = 'https://tv.nrk.no/serie/blank'
    assert re.match(NRKTVSeriesIE._VALID_URL, url)
    assert NRKTVSeriesIE.suitable(url)
    concrete_class = NRKTVSeriesIE.get_ie(url)
    assert concrete_class == NRKTVSeriesIE
    extractor = concrete_class()
    assert extractor._VALID_URL == NRKTVSeriesIE._VALID_URL
    assert extractor.suitable(url)
    assert extractor._real_initialize() is None



# Generated at 2022-06-14 16:46:04.826518
# Unit test for constructor of class NRKPlaylistBaseIE
def test_NRKPlaylistBaseIE():
    ie = NRKPlaylistBaseIE()
    assert ie != undefined

# Generated at 2022-06-14 16:46:09.365867
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():
    nrktvie = NRKTVIE('NRKTVIE','NRK TV','','0')
    assert(nrktvie.ie_key() == 'nrktvil')

# Generated at 2022-06-14 16:46:14.212775
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    # Test the constructor of NRKTVSerieBaseIE class.
    # The constructor has no argument, so no input is needed.
    # The test should pass if it does not throw an exception
    NRKTVSerieBaseIE()



# Generated at 2022-06-14 16:46:15.815525
# Unit test for constructor of class NRKPlaylistBaseIE
def test_NRKPlaylistBaseIE():
    ie = NRKPlaylistBaseIE()
    assert ie.__class__.__name__ == 'NRKPlaylistBaseIE'


# Generated at 2022-06-14 16:46:21.215950
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    ie = NRKTVSerieBaseIE()
    entry_list = next(iter(ie.test_data))
    entries = ie._extract_entries(entry_list)
    nrk_id = entries[0]['video_id']
    assert re.match(NRKTVIE._EPISODE_RE, nrk_id) is not None
    assert ie._extract_assets_key(entries[0]) == 'episodes'
    assert ie._catalog_name('series') == 'series'
    assert ie._catalog_name('podcast') == 'podcast'



# Generated at 2022-06-14 16:46:26.471867
# Unit test for constructor of class NRKSkoleIE
def test_NRKSkoleIE():
    url = 'https://www.nrk.no/skole/?page=search&q=&mediaId=14099'
    nrk_skole_ie = NRKSkoleIE()

    assert nrk_skole_ie._match_id(url) == '14099'                                  # Test for NRKSkoleIE._match_id()

    assert nrk_skole_ie._real_extract(url) == {'id': '6021', 'ext': 'mp4',         # Test for NRKSkoleIE._real_extract()
        'title': 'Genetikk og eneggede tvillinger',
        'description': 'md5:3aca25dcf38ec30f0363428d2b265f8d',
        'duration': 399,
    }

# Generated at 2022-06-14 16:46:29.200357
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    assert isinstance(NRKTVDirekteIE(NRKTVDirekteIE, NRKTVDirekteIE._VALID_URL), NRKTVIE)


# Generated at 2022-06-14 16:46:34.285557
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    from youtube_dl.extractor import gen_extractors_map
    NRKTVSerieBaseIE_map = gen_extractors_map([NRKTVSerieBaseIE])
    # Test with empty input
    NRKTVSerieBaseIE(None)
    # Test invalid URL
    NRKTVSerieBaseIE('https://tv.nrk.no/serie/123')._real_initialize()
    # Test with valid URL
    NRKTVSerieBaseIE_map['https://tv.nrk.no/serie/123']._real_extract('https://tv.nrk.no/serie/123')



# Generated at 2022-06-14 16:46:37.393162
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    """ Test whether NRKTVSeasonIE is able to handle TV seasons """
    url = 'https://tv.nrk.no/serie/lindmo/2016'
    nrktv_serie_ie = NRKTVSeasonIE(NRKTVSeasonIE.suitable(url))
    result = nrktv_serie_ie.extract(url)
    assert result['id'] == 'lindmo/2016'
    assert result['title'] == '2016'
    assert len(result['entries']) == 29


# Generated at 2022-06-14 16:48:32.472613
# Unit test for constructor of class NRKBaseIE
def test_NRKBaseIE():
    '''
    Unit test for constructor of class NRKBaseIE
    '''
    from ..ytdl import YoutubeDL
    ydl = YoutubeDL({})
    ie = NRKBaseIE(ydl)
    assert ie._GEO_COUNTRIES == ['NO']
    assert ie._CDN_REPL_REGEX == r'''(?x)://
            nrkod\d{1,2}-httpcache0-47115-cacheod0\.dna\.ip-only\.net/47115-cacheod0|
            nrk-od-no\.telenorcdn\.net|
            minicdn-od\.nrk\.no/od/nrkhd-osl-rr\.netwerk\.no/no
        /'''

# Generated at 2022-06-14 16:48:32.997716
# Unit test for constructor of class NRKIE
def test_NRKIE():
    pass


# Generated at 2022-06-14 16:48:35.420642
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    extractor = NRKTVSerieBaseIE()
    assert extractor._ASSETS_KEYS == ('episodes', 'instalments',)


# Generated at 2022-06-14 16:48:36.709585
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    assert('NRKTVIE' in repr(NRKTVDirekteIE()))



# Generated at 2022-06-14 16:48:46.756967
# Unit test for constructor of class NRKBaseIE
def test_NRKBaseIE():
    # Test the parameter: _GEO_COUNTRIES
    nrk = NRKBaseIE([], {})
    assert nrk._GEO_COUNTRIES == ['NO']

    # Test the function: _extract_nrk_formats
    # 1. Test when asset_url is not matched
    formats = nrk._extract_nrk_formats(
        'https://nrk.no/bw_low=10.mp4', 'video_id')
    assert formats != None
    # 2. Test when asset_url is matched
    formats = nrk._extract_nrk_formats(
        'https://nrk-od-no.telenorcdn.net/bw_low=10.mp4', 'video_id')
    assert formats != None

    # Test the function:

# Generated at 2022-06-14 16:48:48.458700
# Unit test for constructor of class NRKPlaylistBaseIE
def test_NRKPlaylistBaseIE():
    inst = NRKPlaylistBaseIE()
    assert inst is not None


# Generated at 2022-06-14 16:48:50.061467
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    nrktvseason = NRKTVSeasonIE()
    assert nrktvseason.suitable('http://tv.nrk.no/serie/spangas/sesong/1')


# Generated at 2022-06-14 16:48:59.985991
# Unit test for constructor of class NRKIE
def test_NRKIE():
    parse = lambda x: NRKIE()._match_id(x)
    assert parse('nrk:ecc1b952-96dc-4a98-81b9-5296dc7a98d9') == 'ecc1b952-96dc-4a98-81b9-5296dc7a98d9'
    assert parse('nrk:ecc1b952-96dc-4a98-81b9-5296dc7a98d9/foobar') == 'ecc1b952-96dc-4a98-81b9-5296dc7a98d9'
    assert parse('nrk:clip/150533') == '150533'
    assert parse('nrk:150533') == '150533'

# Generated at 2022-06-14 16:49:01.396158
# Unit test for constructor of class NRKSkoleIE
def test_NRKSkoleIE():
    # Call the constructor of class NRKSkoleIE to create an instance
    inst = NRKSkoleIE()
    # Check if the instance is not None
    assert inst is not None


# Generated at 2022-06-14 16:49:11.313883
# Unit test for constructor of class NRKBaseIE
def test_NRKBaseIE():
    test_cases = [{'url': 'http://www.nrk.no/skole/kroppen/', 'playlist_title': 'Kroppen', 'playlist_mincount': 14},
                  {'url': 'http://www.nrk.no/programmer/radio/p3_urort/', 'playlist_title': 'P3 Urørt', 'playlist_mincount': 29}
    ]
    for test_case in test_cases:
        nrk = NRKBaseIE()
        playlist = nrk.extract(test_case['url'])
        assert playlist['id'] == 're:%s' % test_case['url']
        assert playlist['_type'] == 'playlist'
        assert playlist['title'] == test_case['playlist_title']

# Generated at 2022-06-14 16:51:50.348454
# Unit test for constructor of class NRKBaseIE
def test_NRKBaseIE():
    assert NRKBaseIE('NRK')._CDN_REPL_REGEX is not None



# Generated at 2022-06-14 16:51:56.135351
# Unit test for constructor of class NRKBaseIE
def test_NRKBaseIE():
    assert len(NRKBaseIE._GEO_COUNTRIES) == 1
    assert NRKBaseIE._GEO_COUNTRIES[0] == 'NO'
    assert NRKBaseIE._CDN_REPL_REGEX[0:7] == r'(?x)://'
    assert len(NRKBaseIE._CDN_REPL_REGEX[7:]) == 68



# Generated at 2022-06-14 16:51:57.803533
# Unit test for constructor of class NRKBaseIE
def test_NRKBaseIE():
    assert NRKBaseIE(InfoExtractor())._GEO_COUNTRIES == ['NO']


# Generated at 2022-06-14 16:52:00.475540
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    serie_base_ie = NRKTVSerieBaseIE()
    assert serie_base_ie is not None
    assert isinstance(serie_base_ie, NRKTVSerieBaseIE)


# Generated at 2022-06-14 16:52:07.508080
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():
    url = 'https://tv.nrk.no/serie/tour-de-ski/MSPO40010515/06-01-2015'
    ie = NRKTVIE(NRKIE())
    webpage = ie._download_webpage(url, None)
    assert(ie.PROGRAM_RE.match(webpage))
    assert(ie.PROGRAMSERIE_RE.match(webpage))
    constr_url = ie.PROGRAMSERIE_RE.match(webpage).group('url')
    assert(ie._real_extract(constr_url) == ie.url_result(
        'nrk:MSPO40010515', ie=NRKIE.ie_key(), video_id='MSPO40010515'))

# Generated at 2022-06-14 16:52:09.711085
# Unit test for constructor of class NRKSkoleIE
def test_NRKSkoleIE():
    url = 'https://www.nrk.no/skole/?page=search&q=&mediaId=14099'
    nrkSkoleIE = NRKSkoleIE(NRKSkoleIE._create_ie(), url)
    print(repr(nrkSkoleIE))



# Generated at 2022-06-14 16:52:10.506776
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    NRKTVSeasonIE('NRKTVSeasonIE')



# Generated at 2022-06-14 16:52:12.176502
# Unit test for constructor of class NRKSkoleIE
def test_NRKSkoleIE():
    a = NRKSkoleIE()

# Generated at 2022-06-14 16:52:17.323141
# Unit test for constructor of class NRKPlaylistBaseIE
def test_NRKPlaylistBaseIE():
    sub = unittest.TestSuite()
    sub.addTest(test_test_NRKPlaylistBaseIE('test_NRKPlaylistBaseIE'))
    suite = unittest.TestSuite([sub])
    runner = unittest.TextTestRunner()
    try:
        runner.run(suite)
    except:
        return False
    return True


# Generated at 2022-06-14 16:52:19.653360
# Unit test for constructor of class NRKPlaylistBaseIE
def test_NRKPlaylistBaseIE():
    # Construct object
    instance = NRKPlaylistBaseIE()
    # Ensure that it is instance of NRKPlaylistBaseIE
    assert isinstance(instance, NRKPlaylistBaseIE)

