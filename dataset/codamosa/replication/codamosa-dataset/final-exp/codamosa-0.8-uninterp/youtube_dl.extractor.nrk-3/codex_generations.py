

# Generated at 2022-06-14 16:46:01.562752
# Unit test for constructor of class NRKTVEpisodeIE
def test_NRKTVEpisodeIE():
    return NRKTVEpisodeIE()._real_extract('https://tv.nrk.no/serie/hellums-kro/sesong/1/episode/2')

# Generated at 2022-06-14 16:46:03.391051
# Unit test for constructor of class NRKPlaylistBaseIE
def test_NRKPlaylistBaseIE():
    # It's not possible to test the constructor of NRKPlaylistBaseIE class, because it takes
    # 2 abstract methods download_webpage and timeline_result as parameters.
    pass



# Generated at 2022-06-14 16:46:05.955579
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():
    url = 'https://tv.nrk.no/serie/lindmo/2018/MUHU11006318/avspiller'
    NRKTVIE(NRKTVIE._downloader, url)

# Generated at 2022-06-14 16:46:14.739760
# Unit test for constructor of class NRKBaseIE
def test_NRKBaseIE():
    ie = InfoExtractor(None)
    assert ie;
    assert ie.IE_NAME == 'nrk'
    assert ie._GEO_COUNTRIES == ['NO']
    assert ie._CDN_REPL_REGEX == '''(?x)://
        (?:
            nrkod\d{1,2}-httpcache0-47115-cacheod0\.dna\.ip-only\.net/47115-cacheod0|
            nrk-od-no\.telenorcdn\.net|
            minicdn-od\.nrk\.no/od/nrkhd-osl-rr\.netwerk\.no/no
        )/'''
    assert ie.format_url == ''



# Generated at 2022-06-14 16:46:19.786394
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    assert (NRKTVSerieBaseIE._catalog_name('serie') == 'series')
    assert (NRKTVSerieBaseIE._catalog_name('program') == 'series')
    assert (NRKTVSerieBaseIE._catalog_name('kortfilm') == 'series')
    assert (NRKTVSerieBaseIE._catalog_name('podkast') == 'podcast')
    assert (NRKTVSerieBaseIE._catalog_name('podcast') == 'podcast')
    assert (NRKTVSerieBaseIE._catalog_name('netflix') == 'series')



# Generated at 2022-06-14 16:46:29.789754
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():
    from youtube_dl.downloader.f4m import F4M
    from youtube_dl.downloader.http import HttpFD
    from youtube_dl.utils import FileDownloader
    from youtube_dl.compat import compat_expanduser

    ydl = FileDownloader()
    ydl.params.update({
        'username': 'test_username',
        'password': 'test_password',
        'outtmpl': '%(id)s',
        'nooverwrites': True,
        'continue_dl': False,
    })
    f4m_destpath = tempfile.mkstemp(suffix='.f4m')[1]
    f4m_info_destpath = tempfile.mkstemp(suffix='.json')[1]

# Generated at 2022-06-14 16:46:34.791022
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():
    def call_NBKTVIE(url):
        return NRKTVIE()._real_extract(url)
    assert call_NBKTVIE('https://tv.nrk.no/serie/anno/KMTE50001317/sesong-3/episode-13')['episode'] == '13. episode'

# Generated at 2022-06-14 16:46:39.778546
# Unit test for constructor of class NRKPlaylistIE
def test_NRKPlaylistIE():
    ie = NRKPlaylistIE('http://www.nrk.no/xxxx/yyyy', {'id': 'gjenopplev-den-historiske-solformorkelsen-1.12270763'})
    assert ie._VALID_URL == 'https?://(?:www\.)?nrk\.no/(?!video|skole)(?:[^/]+/)+(?P<id>[^/]+)'
    assert ie._ITEM_RE == r'class="[^"]*\brich\b[^"]*"[^>]+data-video-id="([^"]+)"'
    assert ie._TESTS[0]['url'] == 'http://www.nrk.no/troms/gjenopplev-den-historiske-solformorkelsen-1.12270763'
   

# Generated at 2022-06-14 16:46:47.191459
# Unit test for constructor of class NRKBaseIE
def test_NRKBaseIE(): 
    e = NRKBaseIE();
    assert e._GEO_COUNTRIES == ['NO'];
    assert e._CDN_REPL_REGEX == r'(?x)://\s*(?:nrkod\d{1,2}-httpcache0-47115-cacheod0\.dna\.ip-only\.net/47115-cacheod0|nrk-od-no\.telenorcdn\.net|minicdn-od\.nrk\.no/od/nrkhd-osl-rr\.netwerk\.no/no)/';



# Generated at 2022-06-14 16:46:58.958741
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    media_url = 'https://nrk-media.akamaized.net/NRK/Publikum/2015/05/03/nrk_hoerselboken_leif_35_dager_i_hanusa_2015_02_18_01_22_13_00_medium.mp3?null=0'
    webpage = fake_webpage(media_url, r'<script>var mediaUrl = \'(?P<media_url>[^\']+)\'</script>')

    # The param 'media_url' is a none empty string
    nrk_direkte_ie = NRKTVDirekteIE('http://tv.nrk.no/direkte/nrk1')
    assert nrk_direkte_ie._real_extract(webpage)

    # The

# Generated at 2022-06-14 16:48:09.124063
# Unit test for constructor of class NRKPlaylistIE
def test_NRKPlaylistIE():
    NRKPlaylistIE()

# Generated at 2022-06-14 16:48:10.339682
# Unit test for constructor of class NRKIE
def test_NRKIE():
    return NRKIE()



# Generated at 2022-06-14 16:48:14.837260
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    """Unit test for constructor of class NRKTVSeasonIE"""
    url = 'https://radio.nrk.no/serie/test/season/test'
    info_expected = {
        '_type': 'url',
        'url': 'nrk:test',
        'ie_key': 'NRK',
        'id': 'test'
    }
    nrk = NRKTVSeasonIE(info_expected)
    assert nrk._match_id(url) == 'test'
    assert nrk.suitable(url) is True
    assert nrk.IE_NAME == 'nrk'



# Generated at 2022-06-14 16:48:16.000073
# Unit test for constructor of class NRKSkoleIE
def test_NRKSkoleIE():
    NRKSkoleIE('nrk', 'https://www.nrk.no/skole/?page=search&q=&mediaId=14099')

# Generated at 2022-06-14 16:48:17.731851
# Unit test for constructor of class NRKTVEpisodeIE
def test_NRKTVEpisodeIE():
    # Exercise constructor NRKTVEpisodeIE.__init__
    NRKTVEpisodeIE()

# Generated at 2022-06-14 16:48:23.905793
# Unit test for constructor of class NRKTVSeriesIE
def test_NRKTVSeriesIE():
    # Test for both domain in constructor
    try:
        NRKTVSeriesIE('tv.nrk.no', 'serie', 'serienavn')
        NRKTVSeriesIE('nrksuper.no', 'serie', 'serienavn')
    except AssertionError:
        raise AssertionError('NRKTVSeriesIE constructor does not work with domains tv.nrk.no and nrksuper.no')
    # Test for domain not tv.nrk.no or nrksuper.no
    try:
        NRKTVSeriesIE('radio.nrk.no', 'podkast', 'serienavn')
    except AssertionError:
        raise AssertionError('NRKTVSeriesIE constructor does not work with domain radio.nrk.no')


# Generated at 2022-06-14 16:48:27.224907
# Unit test for constructor of class NRKTVSerieBaseIE
def test_NRKTVSerieBaseIE():
    # Test that it's not possible to create an instance of
    # NRKTVSerieBaseIE without giving it's kind in the constructor
    with pytest.raises(TypeError):
        NRKTVSerieBaseIE()
    # Test that it's possible to create an instance of
    # NRKTVSerieBaseIE with kind specified in the constructor
    with pytest.raises(AssertionError):
        NRKTVSerieBaseIE('series')
    with pytest.raises(AssertionError):
        NRKTVSerieBaseIE('podcast')



# Generated at 2022-06-14 16:48:31.842630
# Unit test for constructor of class NRKBaseIE
def test_NRKBaseIE():
    info = NRKBaseIE().extract_info(NRKBaseIE(), {'url': 'https://tv.nrk.no/serie/gullrekka/sesong/3/episode/1', 'play_path': '1'})
    print(info)
    assert info['title'] == 'Gullrekka 3:1'



# Generated at 2022-06-14 16:48:38.555377
# Unit test for constructor of class NRKTVSeriesIE
def test_NRKTVSeriesIE():
    instance = NRKTVSeriesIE()
    assert not instance.suitable("https://tv.nrk.no/serie/blank/sesong/1/episode/2")
    assert NRKTVSeasonIE("https://radio.nrk.no/podkast/hele_historien/sesong/diagnose-kverulant").suitable("https://radio.nrk.no/podkast/hele_historien/sesong/diagnose-kverulant")
    assert not NRKTVSeasonIE("https://radio.nrk.no/podkast/hele_historien/sesong/diagnose-kverulant").suitable("https://radio.nrk.no/serie/dickie-dick-dickens/sesong/1")



# Generated at 2022-06-14 16:48:39.755906
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():
    ie = NRKTVIE()
    expected_ie_desc = ie.IE_DESC
    assert expected_ie_desc == 'NRK TV and NRK Radio'

# Generated at 2022-06-14 16:51:26.868263
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():
    ie = NRKTVIE()
    assert ie.IE_DESC == "NRK TV and NRK Radio"
    assert NRKTVIE._EPISODE_RE == r'(?P<id>[a-zA-Z]{4}\d{8})'
    assert NRKTVIE._VALID_URL == r'https?://(?:tv|radio)\.nrk(?:super)?\.no/(?:[^/]+/)*%s' % ie._EPISODE_RE

# Generated at 2022-06-14 16:51:31.468085
# Unit test for constructor of class NRKTVEpisodeIE
def test_NRKTVEpisodeIE():
    ie = NRKTVEpisodeIE()
    assert ie.IE_NAME == 'nrk:episode'
    assert ie.IE_DESC == 'NRK TV and NRK Radio episodes'
    assert ie._VALID_URL == 'https?://tv\.nrk\.no/serie/(?P<id>[^/]+/sesong/(?P<season_number>\d+)/episode/(?P<episode_number>\d+))'



# Generated at 2022-06-14 16:51:34.007450
# Unit test for constructor of class NRKIE
def test_NRKIE():
    nrk = NRKIE()
    nrk.extract('nrk:150533')
    print('Successful creation')

# Generated at 2022-06-14 16:51:36.746788
# Unit test for constructor of class NRKTVEpisodesIE
def test_NRKTVEpisodesIE():
    nrk_tv_episodes_ie = NRKTVEpisodesIE()
    nrk_tv_ie = NRKTVIE()
    assert nrk_tv_episodes_ie._TESTS == nrk_tv_ie._TESTS

# Generated at 2022-06-14 16:51:39.059037
# Unit test for constructor of class NRKPlaylistIE
def test_NRKPlaylistIE():
    # test all subclasses of NRKPlaylistIE
    playlist_classes = [
        NRKPlaylistIE,
        NRKTVPlaylistIE,
        NRKRadioPlaylistIE,
    ]
    for cls in playlist_classes:
        yield check_nrk_playlist_ie, cls


# test the constructor of NRKPlaylistIE class

# Generated at 2022-06-14 16:51:40.004541
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():
    assert NRKTVIE.ie_key() == 'nrktv'


# Generated at 2022-06-14 16:51:46.079404
# Unit test for constructor of class NRKTVSeasonIE
def test_NRKTVSeasonIE():
    url = 'https://tv.nrk.no/serie/lindmo/2016'
    mobj = re.match(NRKTVSeasonIE._VALID_URL, url)
    domain = mobj.group('domain')
    serie_kind = mobj.group('serie_kind')
    serie = mobj.group('serie')
    season_id = mobj.group('id') or mobj.group('id_2')
    display_id = '%s/%s' % (serie, season_id)
    assert NRKTVSeasonIE._catalog_name(serie_kind) == 'series'
    assert domain == 'tv'
    assert serie_kind == 'serie'
    assert serie == 'lindmo'
    assert season_id == '2016'
    assert display_

# Generated at 2022-06-14 16:51:47.906906
# Unit test for constructor of class NRKTVIE
def test_NRKTVIE():
    nrktvie = NRKTVIE()
    if nrktvie._EPISODE_RE != "([a-zA-Z]{4}\\d{8})":
        pass


# Generated at 2022-06-14 16:51:58.351042
# Unit test for constructor of class NRKTVDirekteIE
def test_NRKTVDirekteIE():
    channel = NRKTVDirekteIE._download_json(
        'https://www.nrk.no/nett-tv/api/channels',
        None)['channels'][0]
    radio_channel = NRKTVDirekteIE._download_json(
        'https://www.nrk.no/radio/api/channels',
        None)['channels'][0]
    TVIE = NRKTVDirekteIE.__name__ + '._download_json'
    RadioIE = NRKTVDirekteIE.__name__ + '._download_json'

# Generated at 2022-06-14 16:52:00.613893
# Unit test for constructor of class NRKTVEpisodeIE
def test_NRKTVEpisodeIE():
    assert re.match(NRKTVEpisodeIE._VALID_URL, 'https://tv.nrk.no/serie/hellums-kro/sesong/1/episode/2')