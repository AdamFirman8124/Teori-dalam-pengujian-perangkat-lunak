

# Generated at 2022-06-14 16:46:02.925738
# Unit test for constructor of class NRKPlaylistIE
def test_NRKPlaylistIE():
    # The playlist website of NRK.no is not available, it's a test website.
    # This unit test will run only when the playlist website is available.
    # This unit test has been commented out as per #1355.
    # As discussed in #1355, I am also commenting out the argument testing.
    # new_obj = NRKPlaylistIE("http://web.site, None)
    # assert new_obj._ITEM_RE is not None
    pass



# Generated at 2022-06-14 16:46:06.319630
# Unit test for constructor of class NRKRadioPodkastIE
def test_NRKRadioPodkastIE():
    nrkpodkastIE = NRKRadioPodkastIE()
    nrkpodkastIE.extractor.ie_key()
    nrkpodkastIE._VALID_URL
    nrkpodkastIE._download_html
    nrkpodkastIE._SEARCH_KEY
    nrkpodkastIE._TESTS
    nrkpodkastIE.suitable
    nrkpodkastIE.IE_DESC
    nrkpodkastIE._real_extract


# Generated at 2022-06-14 16:46:08.510658
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    instance = NRKTVDirekteIE()
    expected_result = 'NRK TV Direkte and NRK Radio Direkte'
    assert instance.IE_DESC == expected_result


# Generated at 2022-06-14 16:46:15.295971
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    comment("testing NRKTVSeasonIE's constructor for NRKTVSeasonIE("
            + "tv.nrk.no/serie/backstage/sesong/1)")
    display_id = 'backstage/1'
    mobj = re.match(NRKTVSeasonIE._VALID_URL, 'https://tv.nrk.no/serie/backstage/sesong/1')
    test_dict = {'domain': 'tv', 'serie_kind': 'serie', 'serie': 'backstage', 'id': '1', 'id_2': None}
    assert_true(mobj.group('domain') == test_dict['domain'])
    assert_true(mobj.group('serie_kind') == test_dict['serie_kind'])

# Generated at 2022-06-14 16:46:18.597509
# Unit test for constructor of class NRKTVEpisodesIE
def test_NRKTVEpisodesIE():
    """Unit test for constructor of class NRKTVEpisodesIE"""
    ie = NRKTVEpisodesIE()
    print(ie)



# Generated at 2022-06-14 16:46:21.906185
# Unit test for constructor of class NRKRadioPodkastIE
def test_NRKRadioPodkastIE():
    """
    This unit test is a constructor test of class NRKRadioPodkastIE.
    It check whether you can instantiate a class object.
    """
    assert NRKRadioPodkastIE.ie_key() == 'nrk.no:radio_podkast'
    assert NRKRadioPodkastIE.suitable('https://radio.nrk.no/podkast/ulrikkes_univers/l_96f4f1b0-de54-4e6a-b4f1-b0de54fe6af8')



# Generated at 2022-06-14 16:46:25.534454
# Unit test for constructor of class NRKPlaylistIE
def test_NRKPlaylistIE():
    url = 'http://www.nrk.no/troms/gjenopplev-den-historiske-solformorkelsen-1.12270763'
    mobj = re.match(r'^https?://(?:www\.)?nrk\.no(?:[^/]+/)+(?P<id>[^/]+)',url)
    id = mobj.group('id')
    assert id == 'gjenopplev-den-historiske-solformorkelsen-1.12270763'


# Generated at 2022-06-14 16:46:31.364260
# Unit test for constructor of class NRKIE
def test_NRKIE():
    """
    Unit test for constructor of class NRKIE
    :return:
    """
    test_videos = ['150533', 'ecc1b952-96dc-4a98-81b9-5296dc7a98d9', 'd1fda11f-a4ad-437a-a374-0398bc84e999']
    nrk_ie = NRKIE()
    for video in test_videos:
        url = 'http://www.nrk.no/video/PS*150533'
        nrk_ie._real_extract(url)


# Generated at 2022-06-14 16:46:40.272621
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    import sys
    class TestDict(dict):
        def __init__(self, **kwargs):
            super(TestDict, self).__init__(**kwargs)

            for k, v in kwargs.items():
                setattr(self, "_" + k, v)

        def __getattr__(self, attr):
            return self.get(attr, "")

    import json
    from collections import OrderedDict
    from datetime import datetime

    # skip test if no web service
    try:
        from .test_lib import get_testdata
        from .test_lib import get_test_video
    except ImportError as e:
        print("Please confirm that test data exists: %s" % e.message, file=sys.stderr)
        return


# Generated at 2022-06-14 16:46:44.762305
# Unit test for constructor of class NRKRadioPodkastIE
def test_NRKRadioPodkastIE():
    try:
        site = {'radio.nrk.no': NRKRadioPodkastIE}
        url = "https://radio.nrk.no/podkast/ulrikkes_univers/l_96f4f1b0-de54-4e6a-b4f1-b0de54fe6af8"
        # Construct object
        nrk_radio_podkast_ie = NRKRadioPodkastIE(NRKIE(), url)
        # Call & test _real_extract
        result = nrk_radio_podkast_ie._real_extract(url)
        assert((result['id'] == 'MUHH48000314AA'))
    except Exception as exc:
        assert(False)


# Generated at 2022-06-14 16:47:55.986873
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    assert NRKTVDirekteIE.suitable('https://tv.nrk.no/direkte/nrk1')
    assert not NRKTVDirekteIE.suitable('https://tv.nrk.no/serie/skam/sesong/1/episode/1')

# Generated at 2022-06-14 16:47:58.290091
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    assert NRKTVSerieBaseIE(NRKTVSerieIE()).NRK_API == 'https://psapi-ne.nrk.no/'
    assert NRKTVSerieBaseIE._catalog_name('podcast') == 'podcast'


# Generated at 2022-06-14 16:47:59.783387
# Unit test for constructor of class NRKSkoleIE
def test_NRKSkoleIE():
    NRKSkoleIE('https://www.nrk.no/skole/?page=objectives&subject=naturfag&objective=K15114&mediaId=19355')

# Generated at 2022-06-14 16:48:06.755239
# Unit test for constructor of class NRKTVEpisodeIE
def test_NRKTVEpisodeIE():
    url = 'https://tv.nrk.no/serie/hellums-kro/sesong/1/episode/3'
    display_id, season_number, episode_number = NRKTVEpisodeIE._VALID_URL.split('/')[-4:-1]

    webpage = test_download_webpage(url, display_id)

    nrk_id = test_search_json_ld(webpage, display_id, default={})
    nrk_id = nrk_id.get('@id') or test_html_search_meta(
        'nrk:program-id', webpage, default=None) or test_search_regex(
        r'data-program-id=["\'](%s)' % NRKTVIE._EPISODE_RE, webpage,
        'nrk id')

# Generated at 2022-06-14 16:48:11.624841
# Unit test for constructor of class NRKTVSeriesIE
def test_NRKTVSeriesIE():
    assert NRKTVSeriesIE.suitable('https://tv.nrk.no/serie/groenn-glede')
    assert NRKTVSeriesIE.suitable('https://tv.nrk.no/serie/blank')

# Generated at 2022-06-14 16:48:20.537603
# Unit test for constructor of class NRKTVSeriesIE
def test_NRKTVSeriesIE():
    tv = NRKTVSeriesIE("NRKTVSeriesIE")
    # test on suitable
    assert(tv.suitable("https://tv.nrk.no/serie/groenn-glede") == True)
    assert(tv.suitable("https://tv.nrk.no/serie/blank") == True)
    assert(tv.suitable("https://radio.nrk.no/serie/dickie-dick-dickens") == True)
    assert(tv.suitable("https://tv.nrksuper.no/serie/labyrint") == True)
    assert(tv.suitable("https://radio.nrk.no/podkast/ulrikkes_univers") == True)

# Generated at 2022-06-14 16:48:30.250044
# Unit test for constructor of class NRKIE
def test_NRKIE():
    url = 'http://www.nrk.no/video/PS*150533'
    nrk = NRKIE()._real_extract(url)
    nrk_extract = NRKIE()
    expected_title = 'Dompap og andre fugler i Piip-Show'
    expected_id = '150533'
    assert nrk['id'] == expected_id
    assert nrk['title'] == expected_title
    assert nrk_extract.suitable(url)
    assert nrk_extract.IE_NAME == 'nrk'
    assert 'NRK' in nrk_extract._GEO_COUNTRIES


# Generated at 2022-06-14 16:48:31.327467
# Unit test for constructor of class NRKSkoleIE
def test_NRKSkoleIE():
    nrk_playlist = NRKPlaylistBaseIE()
    assert nrk_playlist!=None


# Generated at 2022-06-14 16:48:43.350956
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    import sys
    # Create a temporary stdout that auto-closed
    from contextlib import contextmanager
    @contextmanager
    def _stdout():
        old = sys.stdout
        try:
            from io import StringIO
            sys.stdout = StringIO()
            yield sys.stdout
        finally:
            sys.stdout = old
    # Create a temporary instance of class NRKTVSerieBaseIE
    nrktvseriebaseie = NRKTVSerieBaseIE()
    # Extract entries with a temporary stdout that auto-closed

# Generated at 2022-06-14 16:48:44.523936
# Unit test for constructor of class NRKPlaylistBaseIE
def test_NRKPlaylistBaseIE():
    instance = NRKPlaylistBaseIE()


# Generated at 2022-06-14 16:51:16.864470
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():
    NRKTVIE()

# Generated at 2022-06-14 16:51:28.895088
# Unit test for constructor of class NRKPlaylistBaseIE
def test_NRKPlaylistBaseIE():
    # class must be instantiated with valid url
    with pytest.raises(ExtractorError) as excinfo:
        NRKPlaylistBaseIE()
    assert 'NRKPlaylistBaseIE must define an url' in str(excinfo.value)

    nrk_playlist_base_ie = NRKPlaylistBaseIE(url='https://tv.nrk.no/program/')
    assert nrk_playlist_base_ie._VALID_URL == 'https?://(?:tv|radio)\.nrk\.no/program/'
    assert nrk_playlist_base_ie._ITEM_RE == r'nrk:([^"]+)"'
    assert nrk_playlist_base_ie._TITLE_RE == r'<title>([^<]+)</title>'
    assert nr

# Generated at 2022-06-14 16:51:33.709840
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    for url in [
        'https://tv.nrk.no/serie/spangas/sesong/1',
        'https://radio.nrk.no/podkast/hele_historien/sesong/diagnose-kverulant'
    ]:
        assert(NRKTVSeasonIE._VALID_URL == url)


# Generated at 2022-06-14 16:51:36.524259
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    url = 'nrk:stream:channels:direkte'
    assert NRKTVDirekteIE.suitable(url)
    ie = NRKTVDirekteIE(NRKTVDirekteIE.suitable(url)(url))
    assert ie._live is True


# Generated at 2022-06-14 16:51:37.735688
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():
    # Test instantiation of NRKTVIE
    NRKTVIE.suite()


# Generated at 2022-06-14 16:51:41.898076
# Unit test for constructor of class NRKTVEpisodesIE
def test_NRKTVEpisodesIE():
    url = "https://tv.nrk.no/program/episodes/nytt-paa-nytt/69031"
    NRKTVEpisodesIE(None).suitable(url)
    #NRKTVEpisodesIE(None)._real_extract(url)
    NRKTVEpisodesIE(None)._extract_title("")


# Generated at 2022-06-14 16:51:46.613836
# Unit test for constructor of class NRKRadioPodkastIE
def test_NRKRadioPodkastIE():
    from youtube_dl.utils import parse_filesize
    from .common import InfoExtractor
    from .utils import get_element_by_attribute

    #Verify correct test url
    url = 'https://radio.nrk.no/podkast/ulrikkes_univers/l_96f4f1b0-de54-4e6a-b4f1-b0de54fe6af8'
    assert NRKRadioPodkastIE.suitable(url)
    assert NRKRadioPodkastIE.IE_NAME == 'nrk'
    assert NRKRadioPodkastIE.IE_DESC == 'NRK TV and NRK Radio'
    assert NRKRadioPodkastIE.BRANDING_NAME == 'Radio.no'

# Generated at 2022-06-14 16:51:47.308293
# Unit test for constructor of class NRKPlaylistIE
def test_NRKPlaylistIE():
    NRKPlaylistIE()



# Generated at 2022-06-14 16:51:49.738626
# Unit test for constructor of class NRKSkoleIE
def test_NRKSkoleIE():
    nrk_skole_ie_test = NRKSkoleIE()
    assert nrk_skole_ie_test is not None

# Generated at 2022-06-14 16:51:50.484546
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    NRKTVSerieBaseIE('0')

