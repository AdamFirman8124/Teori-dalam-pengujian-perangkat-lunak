

# Generated at 2022-06-14 16:46:00.782619
# Unit test for constructor of class NRKTVEpisodesIE
def test_NRKTVEpisodesIE():
    # pylint: disable=protected-access
    assert NRKTVEpisodesIE._VALID_URL



# Generated at 2022-06-14 16:46:04.999883
# Unit test for constructor of class NRKRadioPodkastIE
def test_NRKRadioPodkastIE():
    # Given
    valid_url = 'https://radio.nrk.no/podkast/ulrikkes_univers/l_96f4f1b0-de54-4e6a-b4f1-b0de54fe6af8'
    # When
    result = NRKRadioPodkastIE._match_id(valid_url)
    # Then
    assert result == 'l_96f4f1b0-de54-4e6a-b4f1-b0de54fe6af8'

# Generated at 2022-06-14 16:46:09.841902
# Unit test for constructor of class NRKRadioPodkastIE
def test_NRKRadioPodkastIE():
    assert re.match(NRKRadioPodkastIE._VALID_URL, 'https://radio.nrk.no/podkast/ulrikkes_univers/l_96f4f1b0-de54-4e6a-b4f1-b0de54fe6af8')
    assert not re.match(NRKRadioPodkastIE._VALID_URL, 'https://radio.nrk.no/podkast/ulrikkes_univers/a_96f4f1b0-de54-4e6a-b4f1-b0de54fe6af8')

# Generated at 2022-06-14 16:46:15.575595
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    from youtube_dl.utils import parse_iso8601
    from datetime import timedelta, datetime
    assert parse_iso8601('2017-01-02T01:10:00+01:00') == datetime(
        2017, 1, 2, 1, 10, 0, tzinfo=timedelta(hours=1))


# Generated at 2022-06-14 16:46:19.754231
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    NRKTVIE_instance = NRKTVDirekteIE()
    # Check if the IE is a subclass of NRKTVIE
    assert(issubclass(NRKTVDirekteIE, NRKTVIE))
    # Verify that the _VALID_URL class attribute is defined
    assert(issubclass(NRKTVDirekteIE, NRKTVIE))
    # Verify that the IE's overridden _real_extract() method
    # is called when URL is extracted
    assert(NRKTVDirekteIE._real_extract != NRKTVIE._real_extract)


# Generated at 2022-06-14 16:46:23.645301
# Unit test for constructor of class NRKTVEpisodesIE
def test_NRKTVEpisodesIE():
    global NRKTVEpisodesIE
    assert NRKTVEpisodesIE is not None
    # Test NRKTVEpisodesIE constructor without arguments
    nrk_tv_episodes_ie = NRKTVEpisodesIE()
    assert nrk_tv_episodes_ie is not None

# Generated at 2022-06-14 16:46:27.171018
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():
    # Verify that a subclass of InfoExtractor can be constructed
    ie = NRKTVIE()
    # Verify that the initialized object has the right class
    assert(isinstance(ie, NRKTVIE))
    # Verify that the created object has the right type
    assert(type(ie) is NRKTVIE)


# Generated at 2022-06-14 16:46:28.092904
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    assert NRKTVSeasonIE.suitable(NRKTVSeasonIE._VALID_URL)



# Generated at 2022-06-14 16:46:28.950842
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    NRKTVSeasonIE('https://tv.nrk.no/serie/backstage/sesong/1')


# Generated at 2022-06-14 16:46:36.662289
# Unit test for constructor of class NRKTVEpisodeIE
def test_NRKTVEpisodeIE():
    obj = NRKTVEpisodeIE()
    url = "https://tv.nrk.no/serie/hellums-kro/sesong/1/episode/2"
    result = obj._real_extract(url)
    assert(result['id'] == 'MUHH36005220')
    assert(result['url'] == 'nrk:MUHH36005220')
    assert(result['ie_key']() == 'NRKTV')
    assert(result['season_number'] == 1)
    assert(result['episode_number'] == 2)


# Generated at 2022-06-14 16:47:42.570042
# Unit test for constructor of class NRKBaseIE
def test_NRKBaseIE():
    nrkbase_ie = NRKBaseIE("")
    assert(isinstance(nrkbase_ie, InfoExtractor))

# Generated at 2022-06-14 16:47:43.458773
# Unit test for constructor of class NRKIE
def test_NRKIE():
    nrk = NRKIE()



# Generated at 2022-06-14 16:47:48.156156
# Unit test for constructor of class NRKPlaylistIE
def test_NRKPlaylistIE():
    """Unit test for constructor of class NRKPlaylistIE"""

    url = "http://www.nrk.no/kultur/bok/rivertonprisen-til-karin-fossum-1.12266449"
    playlist = NRKPlaylistIE(NRKPlaylistIE.ie_key())
    result = playlist._real_extract(url)
    playlist_id = result['id']
    playlist_title = result['title']
    playlist_desc = result['description']
    playlist_count = len(result['entries'])

    assert playlist_id == 'rivertonprisen-til-karin-fossum-1.12266449'
    assert playlist_title == 'Rivertonprisen til Karin Fossum'

# Generated at 2022-06-14 16:47:51.955704
# Unit test for constructor of class NRKTVEpisodeIE
def test_NRKTVEpisodeIE():
    url = 'https://tv.nrk.no/serie/hellums-kro/sesong/1/episode/2'
    NRKTVEpisodeIE(None).suitable(url)
    #NRKTVEpisodeIE(None)._real_extract(url)

# Generated at 2022-06-14 16:47:52.954967
# Unit test for constructor of class NRKPlaylistIE
def test_NRKPlaylistIE():
    instance = NRKPlaylistIE()
    assert instance.IE_NAME == 'nrk:playlist'


# Generated at 2022-06-14 16:47:59.688846
# Unit test for constructor of class NRKTVIE

# Generated at 2022-06-14 16:48:02.754251
# Unit test for constructor of class NRKRadioPodkastIE
def test_NRKRadioPodkastIE():
    """Test for constructor of class NRKRadioPodkastIE"""
    # Test all three extractors
    for cls in [NRKTVIE, NRKTVEpisodeIE, NRKRadioPodkastIE, NRKTVSeasonIE, NRKTVSeriesIE, NRKTVDirekteIE]:
        assert issubclass(cls, InfoExtractor), '%r should be an InfoExtractor subclass' % cls

# Generated at 2022-06-14 16:48:06.736535
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    assert NRKTVSerieBaseIE._catalog_name('podkast') == 'podcast'
    assert NRKTVSerieBaseIE._catalog_name('series') == 'series'


# Generated at 2022-06-14 16:48:13.166507
# Unit test for constructor of class NRKTVEpisodeIE
def test_NRKTVEpisodeIE():
    ie = NRKTVEpisodeIE()
    assert ie._VALID_URL == r'https?://tv\.nrk\.no/serie/(?P<id>[^/]+/sesong/(?P<season_number>\d+)/episode/(?P<episode_number>\d+))'

# Generated at 2022-06-14 16:48:21.088837
# Unit test for constructor of class NRKIE
def test_NRKIE():
    # Check that NRKIE generates the correct URL for an original series
    url = 'http://www.nrk.no/video/PS*150533'
    nrk = NRKIE()
    nrk._real_extract(url)
    series_id = "MDDP12000117"
    nrk_url = "http://www.nrk.no/video/PS*%s" % series_id
    assert nrk_url == nrk.url_result(series_id,"NRKIE",fatal=True)['url']
    # Check that NRKIE generates the correct URL for a clip
    url = 'http://www.nrk.no/video/PS*150533'
    nrk = NRKIE()
    nrk._real_extract(url)

# Generated at 2022-06-14 16:51:02.246500
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    ie = NRKTVDirekteIE()
    assert ie.ie_key() == 'NRKTVDirekte'
    assert ie.ie_key() == NRKTVDirekteIE.ie_key()
    assert ie.IE_NAME == 'NRKTVDirekte'
    assert ie.IE_NAME == NRKTVDirekteIE.IE_NAME
    assert ie.IE_DESC == 'NRK TV Direkte and NRK Radio Direkte'
    assert ie.IE_DESC == NRKTVDirekteIE.IE_DESC
    assert ie.BRIGHTCOVE_URL_TEMPLATE == 'http://players.brightcove.net/%s/index_apollo_secure.min.js'
    assert ie.BRIGHTCOVE_URL_TEM

# Generated at 2022-06-14 16:51:03.420628
# Unit test for constructor of class NRKPlaylistIE
def test_NRKPlaylistIE():
    print("In test_NRKPlaylistIE")
    assert True



# Generated at 2022-06-14 16:51:06.310127
# Unit test for constructor of class NRKSkoleIE
def test_NRKSkoleIE():
    item = NRKSkoleIE()
    assert item.IE_DESC == 'NRK Skole'
    assert item._VALID_URL == r'https?://(?:www\.)?nrk\.no/skole/?\?.*\bmediaId=(?P<id>\d+)'

# Generated at 2022-06-14 16:51:13.177636
# Unit test for constructor of class NRKBaseIE
def test_NRKBaseIE():
    ie = NRKBaseIE()
    assert ie._GEO_COUNTRIES == ['NO']
    assert ie._CDN_REPL_REGEX == r'://nrkod\d{1,2}-httpcache0-47115-cacheod0\.dna\.ip-only\.net/47115-cacheod0|nrk-od-no\.telenorcdn\.net|minicdn-od\.nrk\.no/od/nrkhd-osl-rr\.netwerk\.no/no/'


# Generated at 2022-06-14 16:51:17.542362
# Unit test for constructor of class NRKPlaylistIE
def test_NRKPlaylistIE():
    url = 'http://www.nrk.no/urort/leoncamp-feirer-pris-med-ny-musikk-1.12273352'
    playlist_id = 'leoncamp-feirer-pris-med-ny-musikk-1.12273352'
    webpage = 'class="rich" data-video-id="MUHH48000314AA"'
    # Test extractor of playlist
    nrk_playlist_ie = NRKPlaylistIE()
    assert nrk_playlist_ie._match_id(url) == 'leoncamp-feirer-pris-med-ny-musikk-1.12273352'
    assert nrk_playlist_ie._extract_title(webpage) == None
    assert nrk_playlist_ie._extract_

# Generated at 2022-06-14 16:51:25.902637
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    if sys.version_info.major >= 3:
        with pytest.raises(TypeError):
            NRKTVSerieBaseIE('NRKTVSerieBaseIE', True)
    else:
        assert NRKTVSerieBaseIE('NRKTVSerieBaseIE', True)
        assert NRKTVSerieBaseIE('NRKTVSerieBaseIE', True) == \
            NRKTVSerieBaseIE('NRKTVSerieBaseIE', True)



# Generated at 2022-06-14 16:51:30.705720
# Unit test for constructor of class NRKIE
def test_NRKIE():

    NRKIE_test = NRKIE()

    # Note that these tests cannot be run on CI, since they access an external API.
    # Please copy them to your computer and run them locally by commenting in the
    # following line (remove the hashtags).
    #from .test_downloads import run_downloader_tests
    #run_downloader_tests(NRKIE_test, [NRKIE])

    return NRKIE_test



# Generated at 2022-06-14 16:51:33.123279
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    ie = NRKTVDirekteIE()
    assert isinstance(ie, NRKTVIE)


# Generated at 2022-06-14 16:51:34.471231
# Unit test for constructor of class NRKSkoleIE
def test_NRKSkoleIE():
    ie = NRKSkoleIE()
    assert ie.constructor == NRKSkoleIE


# Generated at 2022-06-14 16:51:38.435881
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    from youtube_dl.downloader.common import FileDownloader
    ydl = FileDownloader()
    result = ydl.extract_info(
        url='https://tv.nrk.no/direkte/nrk1', download=False
    )
    assert result['id'] == 'VFA0490817'
    assert result['title'] == 'Direkte: NRK1'
    assert result['url'].startswith('rtmp')
