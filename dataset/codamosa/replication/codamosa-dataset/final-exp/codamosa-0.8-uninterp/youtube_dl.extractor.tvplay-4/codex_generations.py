

# Generated at 2022-06-14 17:27:21.549819
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    try:
        TVPlayIE("https://play.tv3play.lt/programos/moterys-meluoja-geriau/409229?autostart=true")
    except Exception as e:
        assert False, "Constructor Test for TVPlayIE failed!"



# Generated at 2022-06-14 17:27:27.880816
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    class MockExtractor(ViafreeIE):
        def _real_extract(self, url):
            return url

    url = 'https://www.viafree.se/program/underhallning/det-beste-vorspielet/sesong-2/episode-1'
    assert MockExtractor().suitable(url)
    assert MockExtractor()._real_extract(url) == url

# Generated at 2022-06-14 17:27:35.759401
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    tvplay_home_ie = TVPlayHomeIE(None)
    assert_equal(tvplay_home_ie._VALID_URL, 'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)')
    assert_equal(tvplay_home_ie.IE_NAME, 'tvplayhome')
    assert_equal(tvplay_home_ie.IE_DESC, 'TVPlay Home')

# Generated at 2022-06-14 17:27:47.117453
# Unit test for constructor of class TVPlayIE

# Generated at 2022-06-14 17:27:59.245081
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    test = Test()

    vid_url = 'https://www.tv3play.lt/programos/moterys-meluoja-geriau/409229?autostart=true'
    vid_id = '409229'
    tvplay_ie = TVPlayIE()

    # test video id parsing function
    vid_id_parsed = tvplay_ie._match_id(vid_url)
    test.assertEqual(vid_id_parsed, vid_id, 'TVPlayIE._match_id')

    # test video page downloading
    page = tvplay_ie._download_webpage(vid_url, vid_id)
    test.assertIsNotNone(page, 'TVPlayIE._download_webpage')

    # test video page parsing function
    vid_info = tvplay

# Generated at 2022-06-14 17:28:03.487401
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ViafreeIE._VALID_URL = r'https://www\.viafree\.no.*'  # To be changed when this issue is fixed: https://github.com/rg3/youtube-dl/pull/10343#issuecomment-224247563
    viafree = ViafreeIE()
    viafree._download_json = lambda w, x: 'fakejson'
    viafree._download_webpage = lambda w, x: '<html></html>'
    viafree.ie = MagicMock()
    viafree.ie.result = 'test'
    result = viafree._real_extract({})
    assert result['id'] == 'test'

# Generated at 2022-06-14 17:28:14.817616
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    example = 'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/'
    ie = TVPlayHomeIE(MockIE(example))
    assert ie._VALID_URL == 'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\\d+)'

# Generated at 2022-06-14 17:28:17.399236
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ViafreeIE('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')

# Generated at 2022-06-14 17:28:20.649115
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()
    assert ie.get_geo_restricted() == False
    ie2 = ViafreeIE()
    ie2.set_geo_restricted()
    assert ie2.get_geo_restricted() == True


# Generated at 2022-06-14 17:28:23.052124
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    video_id = '10044354'
    url = 'https://tvplay.tv3.ee/cool-d-ga-mehhikosse/cool-d-ga-mehhikosse-10044354/'

    tvplay_home = TVPlayHomeIE._build_request(url)
    assert tvplay_home.url == url
    assert tvplay_home.video_id == video_id

# Generated at 2022-06-14 17:28:51.463342
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # Viafree website has no public API. This test is just to make sure this
    # implementation doesn't break the API.
    ViafreeIE._download_json = lambda _, __: None
    ViafreeIE._extract_m3u8_formats = lambda _, __: None

    ie = ViafreeIE('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert ie.country == 'no'
    assert ie.path == 'programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'
    assert ie._VALID_URL == ViafreeIE._VALID_URL
    assert ie._GEO_BYPASS == ViafreeIE._GEO_BYPASS

    ie = ViafreeIE

# Generated at 2022-06-14 17:29:02.985976
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    assert TVPlayHomeIE.suitable('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/') is True
    assert TVPlayHomeIE.suitable('https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/') is True
    assert TVPlayHomeIE.suitable('https://tvplay.tv3.ee/cool-d-ga-mehhikosse/cool-d-ga-mehhikosse-10044354/') is True
    assert TVPlayHomeIE.suitable('https://play.tv3.lt/aferistai-10047125') is True

# Generated at 2022-06-14 17:29:08.018570
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    x = TVPlayHomeIE('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/')
    assert x.__class__.__name__ == 'TVPlayHomeIE'

# Generated at 2022-06-14 17:29:19.064483
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    def _extract_match_info(url):
        ie = TVPlayHomeIE(FakeIE(), {})
        match = re.match(ie._VALID_URL, url)
        return match.groupdict(), ie._real_extract(url)


# Generated at 2022-06-14 17:29:29.243298
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert isinstance(ie, TVPlayHomeIE)
    assert hasattr(ie, '_VALID_URL')
    assert hasattr(ie, '_TESTS')
    assert hasattr(ie, '_GEO_BYPASS')
    assert hasattr(ie, '_MAX_RETRIES')
    assert hasattr(ie, '_TEST')
    assert hasattr(ie, 'IE_NAME')
    assert hasattr(ie, '_NETRC_MACHINE')
    assert hasattr(ie, 'BROKEN_BY_DASH')
    assert hasattr(ie, '_downloader')
    assert hasattr(ie, '_download_webpage_handle')
    assert hasattr(ie, '_download_webpage')

# Generated at 2022-06-14 17:29:32.029525
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # The test is used to check whether the url can be processed by ViafreeIE, if so, the test will be passed
    assert ViafreeIE.suitable(ViafreeIE._VALID_URL) == True

# Generated at 2022-06-14 17:29:35.445412
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    init = TVPlayIE()
    assert init.IE_NAME == "mtg"
    assert init.IE_DESC == "MTG services"
    assert init.VALID_URL == "http://www.tvplay.lv/parraides/vinas-melo-labak/418113"
    assert init.dest_filename == "vinas-melo-labak-418113"
    assert init.out_container == "flv"
    assert init.owner_key == "TVPlay"

# Generated at 2022-06-14 17:29:39.597527
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    return ViafreeIE({})._extract_viafree('', '', None, None)

# Generated at 2022-06-14 17:29:47.978820
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    i = TVPlayIE()
    # Validate regular expression - _VALID_URL
    tv_regex = i._VALID_URL
    # This URL should match
    assert re.match(tv_regex, "http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true")
    assert re.match(tv_regex, "http://www.tv3play.lt/programos/moterys-meluoja-geriau/409229?autostart=true")
    assert re.match(tv_regex, "http://www.tv3play.ee/sisu/kodu-keset-linna/238551?autostart=true")

# Generated at 2022-06-14 17:29:51.488160
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    e = ViafreeIE(None)
    assertViafreeIE(e, 'http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assertViafreeIE(e, 'https://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')


# Generated at 2022-06-14 17:30:12.299013
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    with pytest.raises(ExtractorError):
        ViafreeIE('javascript:void(0)').result()



# Generated at 2022-06-14 17:30:18.824527
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    viafree_ie = ViafreeIE()
    assert viafree_ie.suitable("https://www.viafree.se/program/nyheter/") == False
    assert viafree_ie.suitable("http://tvplay.skaties.lv/parraides/tv3-zinas/760183") == False

# Generated at 2022-06-14 17:30:26.846184
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/')
    assert ie._VALID_URL == 'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\\d+)'

# Generated at 2022-06-14 17:30:36.095281
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()
    assert ie.country == 'SE'
    content = ie._download_json(
        'https://viafree-content.mtg-api.com/viafree-content/v1/%s/path/program/underhallning/sa-senast-i-helvetet-sasong-2/' % ie.country, 'asdf')
    program = content['_embedded']['viafreeBlocks'][0]['_embedded']['program']
    guid = program['guid']
    assert ie.country == ie._search_regex(
        r'https?://[^/]+\.([a-z]{2})', content['meta']['url'],
        'geo country', default=None)

# Generated at 2022-06-14 17:30:41.159098
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    url = 'http://www.tv3play.lv/parraides/vinas-melo-labak/418113?autostart=true'
    _ = TVPlayIE()._real_extract(url)

# Generated at 2022-06-14 17:30:47.105839
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    record = TVPlayHomeIE.suitable(TVPlayHomeIE._VALID_URL)
    assert record == True
    record = TVPlayHomeIE.suitable(TVPlayHomeIE._VALID_URL + "?autostart=true")
    assert record == True
    record = TVPlayHomeIE.suitable("https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/?autostart=true")
    assert record == True
    record = TVPlayHomeIE.suitable("http://tv3play.tv3.ee/cool-d-ga-mehhikosse/cool-d-ga-mehhikosse-10044354/?autostart=true")
    assert record == True

# Generated at 2022-06-14 17:30:57.881411
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    assert ViafreeIE.suitable('http://www.tv3play.se/program/husraddarna/395385?autostart=true') == True
    assert ViafreeIE.suitable('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1') == True
    assert ViafreeIE.suitable('http://tvplay.skaties.lv/parraides/vinas-melo-labak/418113?autostart=true') == True
    assert ViafreeIE.suitable('http://play.tv2.no/programmer/kultur/musikk/kristen-musikkpris/339017') == False



# Generated at 2022-06-14 17:31:10.543760
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert(ie._VALID_URL == 'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)')
    assert(ie.IE_NAME == 'tvplayhome')
    assert(ie.IE_DESC == 'TVPlayHome')
    assert(ie.BR_DESC == 'TVPlayHome')
    assert(ie.BR_IE_NAME == 'tvplayhome')
    assert(ie._build_br_ie_name() == 'tvplayhome')
    assert(ie.BUILD_BR_IE_NAME == [ie._build_br_ie_name()])

# Generated at 2022-06-14 17:31:24.323509
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    # Specific tvplay.lv video
    url = "http://tvplay.skaties.lv/parraides/vinas-melo-labak/418113?autostart=true"
    tvplay = TVPlayIE(url)._real_extract(url)
    assert tvplay['id'] == "418113"
    assert tvplay['title'] == "Kādi ir īri? - Viņas melo labāk"
    assert tvplay['description'] == "Baiba apsmej īrus, kādi tie ir un ko viņi dara."
    assert tvplay['series'] == "Viņas melo labāk"
    assert tvplay['duration'] == 25
    assert tvplay['timestamp'] == 1406097056
    assert tvplay['age_limit'] == 0

   

# Generated at 2022-06-14 17:31:35.469095
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    from . import ViafreeIE
    fake_url = 'http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'
    ie = ViafreeIE()
    ie._initialize_geo_bypass({'countries': ['DK']})
    assert ie.suitable(fake_url), fake_url
    ie._initialize_geo_bypass({'countries': ['NO']})
    assert ie.suitable(fake_url), fake_url
    ie._initialize_geo_bypass({'countries': ['SE']})
    assert ie.suitable(fake_url), fake_url
    ie._initialize_geo_bypass({'countries': ['AT']})

# Generated at 2022-06-14 17:32:30.880201
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    assert isinstance(TVPlayHomeIE('example.com/tv3/skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/'), TVPlayHomeIE)
    assert isinstance(TVPlayHomeIE('example.com/tv3/skaties.lv/vinas-melo-labak-10280317'), TVPlayHomeIE)
    assert isinstance(TVPlayHomeIE('example.com/skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/'), TVPlayHomeIE)
    assert isinstance(TVPlayHomeIE('example.com/skaties.lv/vinas-melo-labak-10280317'), TVPlayHomeIE)

# Generated at 2022-06-14 17:32:36.320019
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    assert TVPlayIE.IE_NAME == 'mtg'
    assert TVPlayIE.IE_DESC == 'MTG services'

# Generated at 2022-06-14 17:32:47.354050
# Unit test for constructor of class ViafreeIE

# Generated at 2022-06-14 17:32:50.648435
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    TVPlayIE('http://tvplay.skaties.lv/parraides/vinas-melo-labak/418113?autostart=true') == '418113'


# Generated at 2022-06-14 17:32:57.511821
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    test_tvplay_ie = TVPlayIE()

# Generated at 2022-06-14 17:33:02.281267
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    url = 'http://www.tv3play.ee/sisu/kodu-keset-linna/238551?autostart=true'

    downloader = InfoExtractor()
    tvplayIE = TVPlayIE()
    tvplayIE._initialize_geo_bypass({'countries': ['EE']})
    downloader.add_info_extractor(tvplayIE)

    try:
        downloader.extract(url)
    except ExtractorError as e:
        a = e.cause
        id = a.code
        if not id == 403:
            raise AssertionError('Expected ExtractorError with code 403 but got %s' % id)
        msg = a.read().decode('utf-8')
        msg = json.loads(msg)
        id = msg['msg']

# Generated at 2022-06-14 17:33:05.972933
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()
    assert ie.tvplay_id() == 'viafree'


# Generated at 2022-06-14 17:33:08.513963
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    tvplay = TVPlayIE()
    assert tvplay.IE_NAME == 'mtg'
    assert tvplay.IE_DESC == 'MTG services'


# Generated at 2022-06-14 17:33:19.103224
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()
    ie._VALID_URL = ViafreeIE._VALID_URL
    ie._TESTS = ViafreeIE._TESTS
    ie._GEO_BYPASS = ViafreeIE._GEO_BYPASS

    for i, case in enumerate(ie._TESTS):
        if 'only_matching' in case:
            continue

        url = case['url']
        column_guide = url.split('/')
        program_name = column_guide[3]
        assert program_name, 'Program name should not be empty'
        assert len(column_guide[4]) == 7, 'Season # should have 7 letters, format: sasong-'

        viafree_module = __import__('youtube_dl.extractor.viafree', fromlist=['Viasat'])

# Generated at 2022-06-14 17:33:22.790643
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    IEClasses = TVPlayHomeIE._build_matches()

    # test generating documentation
    for ie_class in IEClasses.values():
        ie = ie_class()
        ie.suitable()
        ie.working()



# Generated at 2022-06-14 17:35:09.569313
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    tv = TVPlayIE()
    assert("tvplay.lv" in tv._VALID_URL)
    assert("play.tv3.lt" in tv._VALID_URL)
    assert("tv3play.tv3.ee" in tv._VALID_URL)
    assert("tv3play.se" in tv._VALID_URL)
    assert("viasat4play.no" in tv._VALID_URL)
    assert("tv6play.se" in tv._VALID_URL)
    assert("play.nova.bg" in tv._VALID_URL)

# Generated at 2022-06-14 17:35:11.681047
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # ViafreeIE inherits from TVPlayIE
    assert issubclass(ViafreeIE, TVPlayIE)


# Generated at 2022-06-14 17:35:13.705358
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ViafreeIE("http://www.viafree.no")


# Generated at 2022-06-14 17:35:16.971768
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE("https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/")
    assert "TVPlayHomeIE" == ie.ie_key()


# Generated at 2022-06-14 17:35:21.866200
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    TVPlayIE()._initialize_geo_bypass({'countries': ['LV', 'LT', 'EE', 'SE', 'NO', 'DK', 'BG']})


# Generated at 2022-06-14 17:35:26.667921
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE('TVPlayHomeIE', 'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/')
    assert isinstance(ie, TVPlayHomeIE)
    assert ie._VALID_URL == r'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'



# Generated at 2022-06-14 17:35:28.008743
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    assert TVPlayHomeIE()._VALID_URL.pattern == TVPlayHomeIE._VALID_URL

# Generated at 2022-06-14 17:35:29.206754
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    try:
        TVPlayHomeIE()
        assert(False)
    except TypeError:
        pass



# Generated at 2022-06-14 17:35:40.375175
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance = TVPlayHomeIE('https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/')
    assert instance.suitable('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/_play/')
    assert instance.suitable('https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/_play/')
    assert instance.suitable('https://tvplay.tv3.ee/cool-d-ga-mehhikosse/cool-d-ga-mehhikosse-10044354/_play/')

# Generated at 2022-06-14 17:35:43.513045
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # Test empty URLs
    for url in ('', ' '):
        with pytest.raises(AttributeError):
            ViafreeIE(url)

    # Test mocked URL
    url = 'http://www.viafree.se/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-1'
    with mock.patch('%s.ViafreeIE._download_json' % __name__) as viafree_instance:
        viafree_instance.return_value = {}
        ViafreeIE(url)