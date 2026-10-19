

# Generated at 2022-06-14 16:46:00.060565
# Unit test for constructor of class NRKBaseIE

# Generated at 2022-06-14 16:46:02.758479
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    NRKTVSeasonIE.suitable('https://tv.nrk.no/serie/backstage/sesong/1')

# Generated at 2022-06-14 16:46:08.765326
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():
    nrktvie = NRKTVIE()
    _EPISODE_RE = r'(?P<id>[a-zA-Z]{4}\d{8})'
    _VALID_URL = r'https?://(?:tv|radio)\.nrk(?:super)?\.no/(?:[^/]+/)*%s' % _EPISODE_RE
    assert nrktvie.IE_DESC == 'NRK TV and NRK Radio'
    assert nrktvie._VALID_URL == _VALID_URL
    assert hasattr(nrktvie, '_TESTS')


# Generated at 2022-06-14 16:46:19.769231
# Unit test for constructor of class NRKBaseIE
def test_NRKBaseIE():
    """
    Constructor test for class NRKBaseIE
    """
    test_obj = NRKBaseIE()
    # Confirm _GEO_COUNTRIES has correct value
    assert(test_obj._GEO_COUNTRIES == ['NO'])
    # Confirm _CDN_REPL_REGEX has correct value

# Generated at 2022-06-14 16:46:20.944710
# Unit test for constructor of class NRKRadioPodkastIE
def test_NRKRadioPodkastIE():
    ie = NRKRadioPodkastIE()
    assert ie.ie_key() == 'nrk:podkast'



# Generated at 2022-06-14 16:46:22.189390
# Unit test for constructor of class NRKRadioPodkastIE
def test_NRKRadioPodkastIE():
    nrk_radio_podkast = NRKRadioPodkastIE()
    assert(nrk_radio_podkast != None)

# Generated at 2022-06-14 16:46:25.246978
# Unit test for constructor of class NRKTVEpisodesIE
def test_NRKTVEpisodesIE():
    url = 'https://tv.nrk.no/program/episodes/nytt-paa-nytt/69031'
    NRKTVEpisodesIE.suitable(url)



# Generated at 2022-06-14 16:46:29.936404
# Unit test for constructor of class NRKRadioPodkastIE
def test_NRKRadioPodkastIE():
    test_url = 'https://radio.nrk.no/podkast/ulrikkes_univers/l_96f4f1b0-de54-4e6a-b4f1-b0de54fe6af8'
    test_result = {
        'id': 'MUHH48000314AA',
        'ext': 'mp4',
        'title': '20 spørsmål 23.05.2014',
        'description': 'md5:bdea103bc35494c143c6a9acdd84887a',
        'duration': 1741,
        'series': '20 spørsmål',
        'episode': '23.05.2014'
    }

# Generated at 2022-06-14 16:46:31.489807
# Unit test for constructor of class NRKPlaylistBaseIE
def test_NRKPlaylistBaseIE():
    assert(repr(NRKPlaylistBaseIE('NRKPlaylistBaseIE')) ==
           '<NRKPlaylistBaseIE()>')


# Generated at 2022-06-14 16:46:34.884575
# Unit test for constructor of class NRKTVEpisodesIE
def test_NRKTVEpisodesIE():
    # Make sure that constructor of NRKTVEpisodesIE is equal to constructor of NRKIE
    assert NRKTVEpisodesIE.__init__ == NRKIE.__init__

# Generated at 2022-06-14 16:47:30.123962
# Unit test for constructor of class NRKRadioPodkastIE
def test_NRKRadioPodkastIE():
    from ytdl.extractor.nrk import NRKRadioPodkastIE
    sample_url = "https://radio.nrk.no/podkast/ulrikkes_univers/l_96f4f1b0-de54-4e6a-b4f1-b0de54fe6af8"
    NRKRadioPodkastIE(NRKRadioPodkastIE.create_ie(), sample_url)


# Generated at 2022-06-14 16:47:33.619084
# Unit test for constructor of class NRKTVSeriesIE
def test_NRKTVSeriesIE():
    info_dict = {
        'id': 'blank',
        'title': 'Blank',
        'description': 'md5:7664b4e7e77dc6810cd3bca367c25b6e',
    }
    assert (NRKTVSeriesIE()._real_extract('https://tv.nrk.no/serie/blank')
            == info_dict)



# Generated at 2022-06-14 16:47:38.793808
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    nrktvseriebase_obj = NRKTVSerieBaseIE()
    assert nrktvseriebase_obj._extract_entries(
        [{'prfId': '123'}, {'episodeId': '456'}]) == [{
        '_type': 'url', 
        'ie_key': 'NRK', 
        'id': '123', 
        'url': 'nrk:123'}, 
        { 
            '_type': 'url', 
            'ie_key': 'NRK', 
            'id': '456', 
            'url': 'nrk:456'
    }]
    assert nrktvseriebase_obj._extract_assets_key({}) is None

# Generated at 2022-06-14 16:47:39.645195
# Unit test for constructor of class NRKTVEpisodesIE
def test_NRKTVEpisodesIE():
    ie = NRKTVEpisodesIE()
    assert ie


# Generated at 2022-06-14 16:47:46.601217
# Unit test for constructor of class NRKTVSeriesIE
def test_NRKTVSeriesIE():
    url = 'https://tv.nrk.no/serie/groenn-glede'
    ie = NRKTVSeriesIE()
    if not ie.suitable(url):
        raise Exception("url should be suitable")
    site, serie_kind, series_id = re.match(ie._VALID_URL, url).groups()
    is_radio = site == 'radio.nrk'
    domain = 'radio' if is_radio else 'tv'
    size_prefix = 'p' if is_radio else 'embeddedInstalmentsP'

# Generated at 2022-06-14 16:47:48.411354
# Unit test for constructor of class NRKTVEpisodeIE
def test_NRKTVEpisodeIE():
    urlTest = 'https://tv.nrk.no/serie/hellums-kro/sesong/1/episode/2'
    nrkIE = NRKTVEpisodeIE()
    nrkIE._real_extract(urlTest)

# Generated at 2022-06-14 16:47:53.209356
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    instance = NRKTVDirekteIE()
    channel_id = 'nrk1'
    url = instance._VALID_URL % channel_id
    assert instance._real_extract(url)
    channel_id = 'p1_oslo_akershus'
    url = instance._VALID_URL % channel_id
    assert instance._real_extract(url)


# Generated at 2022-06-14 16:47:55.033165
# Unit test for constructor of class NRKBaseIE
def test_NRKBaseIE():
    ie = NRKBaseIE()
    assert ie._GEO_COUNTRIES == ['NO']

# Generated at 2022-06-14 16:47:58.935262
# Unit test for constructor of class NRKPlaylistBaseIE
def test_NRKPlaylistBaseIE():
    # NRKPlaylistBaseIE.__init__(NRKPlaylistBaseIE, InfoExtractor)
    assert NRKPlaylistBaseIE.suitable('aa') == False
    NRKPlaylistBaseIE._VALID_URL = 'https?://tv.nrk.no/serie/blank'
    assert NRKPlaylistBaseIE.suitable('http://tv.nrk.no/serie/blank') == True


# Generated at 2022-06-14 16:48:01.815168
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():
    instance = NRKTVIE()
    instance = NRKTVIE("https://tv.nrk.no/serie/anno/KMTE50001317/sesong-3/episode-13")
test_NRKTVIE()

# Generated at 2022-06-14 16:50:23.149201
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    class test_class(NRKTVSerieBaseIE):
        def _call_api(self, path, display_id, note, fatal=True):
            return 'next'
        def _extract_entries(self, entry_list):
            return entry_list
    class test_case(unittest.TestCase):
        def test_NRKTVSerieBaseIE(self):
            test_class({}, 'test_class')._real_extract('test_case')
    unittest.main(test_case)


# Generated at 2022-06-14 16:50:26.426095
# Unit test for constructor of class NRKIE
def test_NRKIE():
    ie = NRKIE()
    # add test for NRKIE
    assert ie._VALID_URL



# Generated at 2022-06-14 16:50:30.785578
# Unit test for constructor of class NRKTVEpisodesIE
def test_NRKTVEpisodesIE():
    a = NRKTVEpisodesIE()
    assert (a._VALID_URL == 'https?://tv\.nrk\.no/program/[Ee]pisodes/[^/]+/(?P<id>\d+)')

# Generated at 2022-06-14 16:50:31.807300
# Unit test for constructor of class NRKIE
def test_NRKIE():
    NRKIE()


# Generated at 2022-06-14 16:50:37.121767
# Unit test for constructor of class NRKSkoleIE
def test_NRKSkoleIE():
    url = 'https://www.nrk.no/skole/?page=objectives&subject=naturfag&objective=K15114&mediaId=19355'
    NRKSkoleIE(url, {}, {}, {}, {})


# Generated at 2022-06-14 16:50:37.692577
# Unit test for constructor of class NRKSkoleIE
def test_NRKSkoleIE():
    print(NRKSkoleIE)

# Generated at 2022-06-14 16:50:46.348681
# Unit test for constructor of class NRKTVEpisodeIE
def test_NRKTVEpisodeIE():
    ie = NRKTVEpisodeIE()

    webpage_url = 'https://tv.nrk.no/serie/hellums-kro/sesong/1/episode/2'
    webpage = ie._download_webpage(webpage_url, 'MUHH36005220')
    info = ie._search_json_ld(webpage, 'MUHH36005220', default={})
    assert info.get('@id') == 'MUHH36005220'
    assert ie._html_search_meta('nrk:program-id', webpage, default=None) == 'MUHH36005220'

    webpage_url = 'https://tv.nrk.no/serie/backstage/sesong/1/episode/8'

# Generated at 2022-06-14 16:50:50.740185
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    from youtube_dl.extractor.nrk import NRKTVSeasonIE
    # Test to check the constructor of the class
    test_url = 'https://tv.nrk.no/serie/blandet-blandet/sesong/1'
    test_result = NRKTVSeasonIE(
        NRKTVSeasonIE.suitable, test_url)
    assert test_result.url == test_url

# Unit test to check extractor is working fine

# Generated at 2022-06-14 16:50:51.476206
# Unit test for constructor of class NRKPlaylistIE
def test_NRKPlaylistIE():
    # Only construct object NRKPlaylistIE
    NRKPlaylistIE()


# Generated at 2022-06-14 16:50:54.083219
# Unit test for constructor of class NRKTVEpisodeIE
def test_NRKTVEpisodeIE():
    ie = NRKTVEpisodeIE('https://tv.nrk.no/serie/backstage/sesong/1/episode/8')
