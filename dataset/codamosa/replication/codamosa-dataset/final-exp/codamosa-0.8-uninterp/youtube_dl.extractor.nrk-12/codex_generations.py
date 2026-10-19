

# Generated at 2022-06-14 16:45:57.558212
# Unit test for constructor of class NRKPlaylistBaseIE
def test_NRKPlaylistBaseIE():
    assert issubclass(NRKPlaylistBaseIE, InfoExtractor)



# Generated at 2022-06-14 16:46:05.737057
# Unit test for constructor of class NRKPlaylistBaseIE
def test_NRKPlaylistBaseIE():
    class MyPlaylistBase(NRKPlaylistBaseIE):
        _VALID_URL = 'https://example.com/playlist/%s'
        _ITEM_RE = r'https?://example\.com/(?:video|audio)/([^&"\']+)'

        def _extract_title(self, webpage):
            return self._og_search_title(webpage)

    ie = MyPlaylistBase()

# Generated at 2022-06-14 16:46:11.970318
# Unit test for constructor of class NRKTVSeriesIE
def test_NRKTVSeriesIE():
    import os, tempfile
    tempdir = tempfile.gettempdir()
    fd, temp_path = tempfile.mkstemp(suffix='.mp4', dir=tempdir)
    os.close(fd)
    unittest.TextTestRunner(verbosity=2).run(
        unittest.TestLoader().loadTestsFromTestCase(
            type('TestNRKTVSeriesIE', (NRKTVSeriesIE, unittest.TestCase),
                 {'TEMP_FILE_PATH': temp_path})))
    os.remove(temp_path)



# Generated at 2022-06-14 16:46:15.796388
# Unit test for constructor of class NRKPlaylistIE
def test_NRKPlaylistIE():
    assert NRKPlaylistIE.suitable('http://www.nrk.no/troms/gjenopplev-den-historiske-solformorkelsen-1.12270763')
    assert NRKPlaylistIE.suitable('http://www.nrk.no/troms/gjenopplev-den-historiske-solformorkelsen-1.12270763/')
    assert not NRKPlaylistIE.suitable('http://www.nrk.no/video/')
    assert not NRKPlaylistIE.suitable('http://www.nrk.no/skole/')



# Generated at 2022-06-14 16:46:24.745632
# Unit test for constructor of class NRKTVEpisodesIE
def test_NRKTVEpisodesIE():
    instance = NRKTVEpisodesIE()
    assert instance._VALID_URL == '^https?://tv\\.nrk\\.no/program/[Ee]pisodes/[^/]+/(?P<id>\\d+)$'
    assert instance._ITEM_RE == 'data-episode=\\["\'](?P<id>EP\\d+)(?:[^"]+)'
    assert instance.ie_key() == 'nrktv:episodes'
    assert instance.ie_key() == NRKTVEpisodesIE.ie_key()


# Generated at 2022-06-14 16:46:28.304455
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():
    instance = NRKTVIE("test_NRKTVIE")
    # testing the veriable _EPISODE_RE, which is used to identify  the episode id
    assert(instance._EPISODE_RE == r'(?P<id>[a-zA-Z]{4}\d{8})')

# Generated at 2022-06-14 16:46:29.788956
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    ie = NRKTVDirekteIE()



# Generated at 2022-06-14 16:46:35.274382
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    nrktvseriebaseie = NRKTVSerieBaseIE()
    assert nrktvseriebaseie.season_number is None
    assert nrktvseriebaseie.episode_number is None
    assert nrktvseriebaseie.episode_id is None
    assert nrktvseriebaseie.display_id is None
    assert nrktvseriebaseie._HOST is None
    assert nrktvseriebaseie._API_HOST is None
    assert nrktvseriebaseie._PROGRAM_SERIES_URL is None
    assert nrktvseriebaseie._PROGRAM_SERIES_NAME == 'series'


# Generated at 2022-06-14 16:46:38.727347
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    items = [
        {'url': 'https://tv.nrk.no/serie/da-vinci-koden-stjernekoden', 'only_matching': True}
    ]
    try:
        NRKTVSerieBaseIE()._real_extract('https://tv.nrk.no/serie/da-vinci-koden-stjernekoden')
    except ExtractorError:
        pass


# Generated at 2022-06-14 16:46:43.519431
# Unit test for constructor of class NRKPlaylistBaseIE
def test_NRKPlaylistBaseIE():
    test_url = 'https://tv.nrk.no/serie/daan-gravlykta/sesong/1/episode/2'
    test_playlist_id = 'daan-gravlykta/sesong/1/episode/2'

    NRKPlaylistBaseIE._download_webpage = lambda self, url, video_id = playlist_id: "The video id is %s" % url.split("/")[-1]
    NRKPlaylistBaseIE._extract_title = lambda self, webpage: "The title is %s" % webpage
    NRKPlaylistBaseIE._extract_description = lambda self, webpage: "The description is %s" % webpage
    NRKPlaylistBaseIE._match_id = lambda self, url: url.split("/")[-1]
    NRKPlay

# Generated at 2022-06-14 16:47:45.394041
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    constructor = NRKTVSeasonIE('NRKTVSeasonIE')


# Generated at 2022-06-14 16:47:46.295068
# Unit test for constructor of class NRKIE
def test_NRKIE():
    assert NRKIE._VALID_URL



# Generated at 2022-06-14 16:47:47.238297
# Unit test for constructor of class NRKTVEpisodeIE
def test_NRKTVEpisodeIE():
    assert NRKTVEpisodeIE()


# Generated at 2022-06-14 16:47:49.993171
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():
    url = 'https://tv.nrk.no/serie/tour-de-ski/MSPO40010515/06-01-2015#del=2'
    info = NRKTVIE()._real_extract(url)
    assert info['url'] == 'nrk:MSPO40010515'
    assert info['id'] == 'MSPO40010515'

# Generated at 2022-06-14 16:47:50.730400
# Unit test for constructor of class NRKRadioPodkastIE
def test_NRKRadioPodkastIE():
    ie = NRKRadioPodkastIE()
    ie._match_id('')

# Generated at 2022-06-14 16:47:53.050061
# Unit test for constructor of class NRKRadioPodkastIE
def test_NRKRadioPodkastIE():
    url = 'https://radio.nrk.no/podkast/ulrikkes_univers/l_96f4f1b0-de54-4e6a-b4f1-b0de54fe6af8'
    nrkpodkastIE = NRKRadioPodkastIE(NRKTVIE(), url)
    assert nrkpodkastIE



# Generated at 2022-06-14 16:47:54.838755
# Unit test for constructor of class NRKIE
def test_NRKIE():
    nrkie = NRKIE()
    nrkie._VALID_URL


# Generated at 2022-06-14 16:47:59.434174
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    ie = NRKTVDirekteIE('tv.nrk.no', None, None)
    print(str(ie))
    assert ie.get_live_index('nrk1') is not None
    assert ie.get_live_index('p1_oslo_akershus') is not None
    assert ie.get_live_index('unknown') is None

# Generated at 2022-06-14 16:48:01.854675
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():
    assert NRKTVIE('https://tv.nrk.no/serie/anno/KMTE50001317/sesong-3/episode-13')



# Generated at 2022-06-14 16:48:06.458950
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    """Test constructor of class NRKTVSeasonIE.
       It tests only initialization of NRKTVSeasonIE.
       It does not test extraction of NRKTVSeasonIE.
    """
    nrktvseason_ie = NRKTVSeasonIE()
    assert 'NRKTVSeasonIE' == type(nrktvseason_ie).__name__
    assert True == isinstance(nrktvseason_ie, NRKBaseIE)
    assert NRKBaseIE == type(nrktvseason_ie).__bases__[0]


# Generated at 2022-06-14 16:48:57.487162
# Unit test for constructor of class NRKIE
def test_NRKIE():
    return NRKIE(InfoExtractor())



# Generated at 2022-06-14 16:49:01.077149
# Unit test for constructor of class NRKIE
def test_NRKIE():
    ie = NRKIE()
    # test URL without scheme
    assert ie._match_id('nrk:ecc1b952-96dc-4a98-81b9-5296dc7a98d9') == 'nrk:ecc1b952-96dc-4a98-81b9-5296dc7a98d9'


# Generated at 2022-06-14 16:49:03.215690
# Unit test for constructor of class NRKPlaylistBaseIE
def test_NRKPlaylistBaseIE():
    m = NRKPlaylistBaseIE()
    assert m._downloader == None
    assert m._download_webpage == None
    assert repr(m) == '<NRKPlaylistBaseIE>'



# Generated at 2022-06-14 16:49:03.788968
# Unit test for constructor of class NRKIE
def test_NRKIE():
    NRKIE()

# Generated at 2022-06-14 16:49:06.542625
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():
    # Test that it's initialised with a region param and a user agent.
    ie = NRKTVIE()
    assert isinstance(ie, NRKTVIE)
    assert hasattr(ie, '_downloader')
    assert ie._downloader.params['geo_verification_headers']['User-Agent'] == 'NRK TV'

# Generated at 2022-06-14 16:49:07.765678
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    # Create instance
    NRKTVSeasonIE(NRKIE(nrkBaseIE=NRKBaseIE()), NRKTVSeasonIE.suitable, {})


# Generated at 2022-06-14 16:49:11.973104
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    inst = NRKTVSerieBaseIE()
    assert inst._ASSETS_KEYS == ('episodes', 'instalments',)
    assert inst._catalog_name('podcast') == 'podcast'
    assert inst._catalog_name('podkast') == 'podcast'
    assert inst._catalog_name('series') == 'series'


# Generated at 2022-06-14 16:49:12.788904
# Unit test for constructor of class NRKTVEpisodeIE
def test_NRKTVEpisodeIE():
    NRKTVEpisodeIE()


# Generated at 2022-06-14 16:49:13.366532
# Unit test for constructor of class NRKPlaylistBaseIE
def test_NRKPlaylistBaseIE():
    obj = NRKPlaylistBaseIE()



# Generated at 2022-06-14 16:49:16.517264
# Unit test for constructor of class NRKBaseIE
def test_NRKBaseIE():
    ie = NRKBaseIE()
    assert ie._call_api('/assets/%7B5CE39EB1-8029-2B9E-E053-D8C0B7332888%7D/images/mezzanine_16_9@1x.jpg',
                        'test', 'asset', 'Downloading asset JSON')

# Generated at 2022-06-14 16:51:39.927964
# Unit test for constructor of class NRKPlaylistIE
def test_NRKPlaylistIE():
    """Verify IE can be constructed"""
    ie = NRKPlaylistIE('http://www.nrk.no/troms/gjenopplev-den-historiske-solformorkelsen-1.12270763')
    assert ie.__class__ is NRKPlaylistIE



# Generated at 2022-06-14 16:51:44.184643
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():
    url = 'https://tv.nrk.no/serie/lindmo/2018/MUHU11006318/avspiller'
    video_id = 'MUHU11006318'
    video_url = 'nrk:%s' % video_id
    assert video_id == NRKTVIE._match_id(url)
    assert video_url == NRKTVIE._get_url_result(video_id)
    assert video_url == NRKTVIE._get_url_result(video_url)



# Generated at 2022-06-14 16:51:49.103568
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    ie = NRKTVSeasonIE
    assert ie.suitable('http://tv.nrk.no/serie/backstage/sesong/1')
    assert ie.suitable('http://radio.nrk.no/serie/dagsnytt/sesong/201509')
    assert ie.suitable('https://radio.nrk.no/podkast/hele_historien/sesong/diagnose-kverulant')
    assert not ie.suitable('http://tv.nrk.no/serie/brennpunkt/MUHH40002814/20-02-2014')
    assert not ie.suitable('http://radio.nrk.no/serie/dagsnytt/NPUB21019315/12-07-2015#')


# Generated at 2022-06-14 16:51:54.890222
# Unit test for constructor of class NRKTVEpisodesIE
def test_NRKTVEpisodesIE():
    assert(NRKTVEpisodesIE.__name__ == 'NRKTVEpisodesIE')
    assert(NRKTVEpisodesIE.__doc__ == 'NRK TV Episodes')
    assert(NRKTVEpisodesIE.ie_key() == 'NRKTVEpisodes')
    assert(NRKTVEpisodesIE.description == 'NRK TV Episodes')
    assert(NRKTVEpisodesIE.suitable('https://tv.nrk.no/program/episodes/nytt-paa-nytt/69031') == True)
    assert(NRKTVEpisodesIE.suitable('https://tv.nrk.no/serie/episodes/sesong/10/69031') == False)

# Generated at 2022-06-14 16:51:57.450929
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    result = NRKTVSeasonIE._TESTS[0]
    res = NRKTVSeasonIE()
    res.extract(result['url'])



# Generated at 2022-06-14 16:51:59.392768
# Unit test for constructor of class NRKTVEpisodesIE
def test_NRKTVEpisodesIE():
    obj = NRKTVEpisodesIE()
    assert obj._VALID_URL == r'https?://tv\.nrk\.no/program/[Ee]pisodes/[^/]+/(?P<id>\d+)'

# Generated at 2022-06-14 16:52:07.015267
# Unit test for constructor of class NRKIE
def test_NRKIE():
    import unittest
    class NRKIETest(unittest.TestCase):
        def test_construction(self):
            ie = NRKIE()
            self.assertEqual(ie.IE_NAME, 'NRK')
            self.assertEqual(ie.IE_DESC, 'Norwegian Broadcasting Corporation')
            self.assertEqual(ie._VALID_URL, NRKIE._VALID_URL)
            self.assertEqual(ie._GEO_COUNTRIES, ['NO'])
            self.assertEqual(ie._TESTS, NRKIE._TESTS)

# Generated at 2022-06-14 16:52:08.701091
# Unit test for constructor of class NRKSkoleIE
def test_NRKSkoleIE():
    nrk_skole_ie = NRKSkoleIE()
    assert nrk_skole_ie.__class__.__name__ == 'NRKSkoleIE'


# Generated at 2022-06-14 16:52:11.305959
# Unit test for constructor of class NRKPlaylistIE
def test_NRKPlaylistIE():
    # Test object constructed without errors
    url = 'http://www.nrk.no/troms/gjenopplev-den-historiske-solformorkelsen-1.12270763'
    nrk_playlist_ie_test_object = NRKPlaylistIE(NRKIE, url)
    assert nrk_playlist_ie_test_object is not None


# Generated at 2022-06-14 16:52:14.436689
# Unit test for constructor of class NRKRadioPodkastIE
def test_NRKRadioPodkastIE():
    NRKRadioPodkastIE().suitable('https://radio.nrk.no/podkast/ulrikkes_univers/l_96f4f1b0-de54-4e6a-b4f1-b0de54fe6af8')
    NRKRadioPodkastIE().suitable('https://radio.nrk.no/podkast/ulrikkes_univers/l_96f4f1b0-de54-4e6a-b4f1-b0de54fe6af8')

