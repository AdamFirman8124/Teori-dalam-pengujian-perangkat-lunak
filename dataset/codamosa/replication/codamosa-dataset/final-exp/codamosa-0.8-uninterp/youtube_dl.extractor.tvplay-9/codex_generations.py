

# Generated at 2022-06-14 17:27:28.069848
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():

    # Test case 1
    url = 'http://tvplay.skaties.lv/parraides/vinas-melo-labak/418113?autostart=true'
    tvplayIE = TVPlayIE()
    tvplayIE.extract(url)
    assert tvplayIE.get_video_id() == '418113'
    assert tvplayIE.get_country_code() == 'lv'

    # Test case 2
    url = 'http://tvplay.skaties.lv/parraides/tv3-zinas/760183'
    tvplayIE = TVPlayIE()
    tvplayIE.extract(url)
    assert tvplayIE.get_video_id() == '760183'
    assert tvplayIE.get_country_code() == 'lv'

    # Test case 3
    url

# Generated at 2022-06-14 17:27:35.880506
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    def check_suitable(test_url, result):
        test_instance = ViafreeIE(params=None)
        assert test_instance.suitable(test_url) == result
    check_suitable('http://play.novatv.bg/programi/zdravei-bulgariya/624952?autostart=true', False)
    check_suitable('http://www.tv8play.se/program/antikjakten/282756?autostart=true', False)
    check_suitable('http://www.tv3play.se/program/husraddarna/395385?autostart=true', False)
    check_suitable('http://www.tv6play.se/program/den-sista-dokusapan/266636?autostart=true', False)


# Generated at 2022-06-14 17:27:43.055083
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()
    url = 'http://www.tv3play.lt/programos/moterys-meluoja-geriau/409229?autostart=true'
    id = '409229'
    assert ie._match_id(url) == id
    test = {
        'url': url,
        'only_matching': True,
    }
    test_res = ie.suitable(test)
    assert test_res

# Generated at 2022-06-14 17:27:46.795367
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    c = TVPlayIE()
    c._initialize_geo_bypass(
        {'countries': ['LV', 'LT', 'EE', 'SE', 'BG'],
         'proxies': None})


# Generated at 2022-06-14 17:27:58.839360
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()
    assert ie.IE_NAME == 'mtg'

# Generated at 2022-06-14 17:28:06.920931
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    site_url = 'http://play.tv3.lt/programos/moterys-meluoja-geriau/409229?autostart=true'
    tvplayie = TVPlayIE()
    tvplayie._match_id(site_url)
    from collections import namedtuple
    args = namedtuple('args', 'site,site_url')
    args.site = 'mtg: TV3.lt, TV3play.lv, TV6.se, TV6play.se, TV8.se, TV8play.se, TV10.se, TV10play.se, TV3play.dk, TV3play.no, Viasat4play.no, TV3play.ee'
    args.site_url = site_url
    rv = tvplayie.test(args)
    assert rv




# Generated at 2022-06-14 17:28:14.798636
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()
    ie.suitable('https://play.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    ie.suitable('https://play.viafree.se/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-1')
    ie.suitable('https://play.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')

# Generated at 2022-06-14 17:28:19.779410
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    from .. import TVPlayIE
    t = TVPlayIE("http://tvplay.skaties.lv/parraides/vinas-melo-labak/418113?autostart=true")
    t.run()


# Generated at 2022-06-14 17:28:26.047715
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    # Check that the class constructor raises an error when given an empty url
    assert_raises(AssertionError, TVPlayIE, 'http://www.test.com/test', {})
    # Check that the class constructor doesn't raise an error when given a valid url
    assert_raises(AssertionError, TVPlayIE, 'http://www.skaties.lv/parraides/vinas-melo-labak/418113?autostart=true', {})



# Generated at 2022-06-14 17:28:28.720490
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    TVPlayHomeIE('http://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/')

# Generated at 2022-06-14 17:29:13.142928
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    # a simple test
    # test FeedParserIE
    assert TVPlayIE._VALID_URL == r'(?x)(?:mtg:|https?://(?:www\.)?(?:tvplay(?:\.skaties)?\.lv(?:/parraides)?|(?:tv3play|play\.tv3)\.lt(?:/programos)?|tv3play(?:\.tv3)?\.ee/sisu|(?:tv(?:3|6|8|10)play|viafree)\.se/program|(?:(?:tv3play|viasat4play|tv6play|viafree)\.no|(?:tv3play|viafree)\.dk)/programmer|play\.nova(?:tv)?\.bg/programi)/(?:[^/]+/)+)(?P<id>\d+)'
    assert TV

# Generated at 2022-06-14 17:29:24.570003
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()
    ie._initialize_geo_bypass({'countries': ['LV']})

    url = "https://play.tv3.lt/programos/moterys-meluoja-geriau/409229"
    actual = ie._real_extract(url)

# Generated at 2022-06-14 17:29:27.014899
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    # This test is only for code coverage (to handle case when TVPlayHomeIE is called),
    # It's not a real test for matching URL (because it can't be done for class TVPlayHomeIE).
    TVPlayHomeIE()

# Generated at 2022-06-14 17:29:27.610624
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    assert 'ViafreeIE' in globals()



# Generated at 2022-06-14 17:29:36.303384
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    info_dict = TVPlayHomeIE('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/')._real_extract('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/')
    assert info_dict['id'] == '366367'
    assert info_dict['ext'] == 'mp4'
    assert info_dict['title'] == 'Aferistai'
    assert info_dict['description'] == 'Aferistai. Kalėdinė pasaka.'
    assert info_dict['series'] == 'Aferistai [N-7]'
    assert info_dict['season'] == '1 sezonas'
    assert info_dict['season_number'] == 1
    assert info_dict['duration'] == 4

# Generated at 2022-06-14 17:29:37.350992
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    """Unit test for constructor of class TVPlayIE"""
    ie = TVPlayIE()
    ie.to_screen('Nothing to test')
    return


# Generated at 2022-06-14 17:29:47.262879
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE('https://play.tv3.lt/aferistai-10047125')
    assert ie.SUBCLASS == TVPlayHomeIE
    assert ie.VALID_URL == 'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'

# Generated at 2022-06-14 17:29:53.150290
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    """
    Unit test for constructor of ViafreeIE.
    """
    url = 'http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'
    ie = ViafreeIE(ViafreeIE.suitable(url))
    if ie.suitable(url) is False:
        return 'suitable is not functioning properly'
    if ie._VALID_URL is None:
        return '_VALID_URL is not functioning properly'
    if ie._TESTS is None:
        return '_TESTS is not functioning properly'
    if ie._GEO_BYPASS is None:
        return '_GEO_BYPASS is not functioning properly'
    return None


# Generated at 2022-06-14 17:29:57.999219
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    assert ViafreeIE.suitable('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1') is True
    assert ViafreeIE.suitable('http://play.tv2.no/programmer/humor/rubicon/633') is False
    assert ViafreeIE.suitable('http://www.tv3play.se/program/husraddarna/395385?autostart=true') is False

# Generated at 2022-06-14 17:29:59.743734
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE('', {})
    assert isinstance(ie, TVPlayIE)

# Generated at 2022-06-14 17:30:49.719322
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'

# Generated at 2022-06-14 17:30:54.758819
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'



# Generated at 2022-06-14 17:30:59.694977
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    IE = TVPlayHomeIE(None)
    assert "play.tv3.lt" in IE._VALID_URL
    assert "tv3play.skaties.lv" in IE._VALID_URL
    assert "play.tv3.ee" in IE._VALID_URL
    assert "tv3play.tv3.ee" in IE._VALID_URL



# Generated at 2022-06-14 17:31:11.365139
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # Test empty constructor
    viafreeIE = ViafreeIE()
    assert viafreeIE

    # Test to ensure that the _VALID_URL is valid
    url = viafreeIE._VALID_URL
    url = url.replace("http://", "").replace("https://", "")
    url = url.split("/")
    try:
        socket.gethostbyname(url[0])
    except socket.gaierror as e:
        assert False, "Error %s for url %s" % (e.strerror, url[0])
    chrome = webdriver.Chrome()
    chrome.get("http://"+url[0]+"/"+url[1])
    assert chrome.title != "404 Not Found"
    chrome.quit()

# Generated at 2022-06-14 17:31:24.651555
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    video_url = 'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/'
    video_id = ie._match_id(video_url)
    # test TVPlayHomeIE._match_id
    assert video_id == '10047125', 'video_id is %s' % video_id
    # test TVPlayHomeIE._real_extract
    ie_real_extract = ie._real_extract(video_url)
    assert ie_real_extract['id'] == '10047125', 'id is %s' % ie_real_extract['id']
    assert ie_real_extract['title'] == 'Aferistai', 'title is %s' % ie_real_extract['title']

# Generated at 2022-06-14 17:31:35.710691
# Unit test for constructor of class ViafreeIE

# Generated at 2022-06-14 17:31:42.325144
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    """
    Unit tests for constructor of class TVPlayHomeIE.
    """
    def _test_asset_id(asset_id):
        """
        Helper function for the unit test.
        """
        # Initialize the class.
        class_instance = TVPlayHomeIE()

        # Assert that the asset_id is contained in the class URL pattern.
        assert re.search(class_instance._VALID_URL, asset_id)

    # Create a list of asset ids.

# Generated at 2022-06-14 17:31:44.381872
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    from . import unit_test_TVPlayIE
    unit_test_TVPlayIE(TVPlayIE)



# Generated at 2022-06-14 17:31:46.990979
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert ie._VALID_URL == r'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'


# Generated at 2022-06-14 17:31:48.493050
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ViafreeIE()



# Generated at 2022-06-14 17:33:13.030742
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    result = TVPlayIE()._real_extract('http://play.tv3.lt/programos/moterys-meluoja-geriau/409229?autostart=true')
    assert result['id'] == '409229'
    assert result['ext'] == 'flv'
    assert result['timestamp'] == 1403769181

# Generated at 2022-06-14 17:33:14.577365
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    TVPlayHomeIE()


# Generated at 2022-06-14 17:33:20.953547
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE(None)
    assert ie._VALID_URL == r'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'
    assert ie.IE_NAME == 'tvplay:home'

# Generated at 2022-06-14 17:33:32.700125
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/')
    assert ie.__name__ == 'TVPlayHome'
    assert ie.country == 'lt'
    ie = TVPlayHomeIE('https://play.tv3.lt/aferistai-10047125')
    assert ie.country == 'lt'
    ie = TVPlayHomeIE('https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/')
    assert ie.country == 'lv'
    ie = TVPlayHomeIE('https://tv3play.skaties.lv/vinas-melo-labak-10280317')
    assert ie.country == 'lv'
    ie = TVPlayHome

# Generated at 2022-06-14 17:33:44.269160
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    tvplayie = TVPlayIE()

# Generated at 2022-06-14 17:33:56.633638
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    url = 'https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/'
    ie._real_extract(url)
    assert ie._VALID_URL is not None
    assert ie._TESTS is not None
    assert ie._GEO_BYPASS is False
    assert ie.IE_NAME is not None
    assert ie.IE_DESC is not None
    assert ie.webpage_url_basename(url) == 'vinas-melo-labak-10280317'
    assert ie._search_regex(re.compile(r'^(.*)$'), url, '1') == url

# Generated at 2022-06-14 17:34:02.509992
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    class TestTVPlayIE(TVPlayIE):

        def _real_initialize(self):
            TVPlayIE._real_initialize(self)

        def _real_extract(self, url):
            TVPlayIE._real_extract(self, url)

    TestTVPlayIE()._real_extract("http://tv3.dk/")



# Generated at 2022-06-14 17:34:13.273776
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    """Test that we can create a TVPlayHomeIE by calling its constructor"""

    # Create instance without calling its constructor
    ie = type('TVPlayHomeIE', (TVPlayHomeIE,), {})
    # Assert that it's an instance of InfoExtractor
    assert isinstance(ie, InfoExtractor)
    # Assert that it's not an instance of TVPlayHomeIE
    assert not isinstance(ie, TVPlayHomeIE)
    # Assert that it is registered
    assert ie.ie_key() in InfoExtractor._download_info_extractors
    # Assert that it's suitable
    assert ie.suitable('https://play.tv3play.lv/sona-daugavas-tilti/sona-daugavas-tilti-10228892/')
    # Assert that it's not suitable

# Generated at 2022-06-14 17:34:21.110180
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    test_url = 'http://www.viasat4play.no/programmer/budbringerne/21873?autostart=true'
    info_dict = TVPlayIE._real_extract(TVPlayIE(), test_url)
    assert info_dict['id'] == '21873'
    assert info_dict['title'] == 'Budbringerne program 10'
    assert info_dict['description'] == 'md5:4db78dc4ec8a85bb04fd322a3ee5092d'
    assert info_dict['duration'] == 1297
    assert info_dict['timestamp'] == 1254205102
    assert info_dict['upload_date'] == '20090929'


# Generated at 2022-06-14 17:34:24.486665
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert ie.suitable('https://tvplay.tv3.ee/cool-d-ga-mehhikosse/cool-d-ga-mehhikosse-10044354/')
    assert not ie.suitable('https://www.tv3play.lt/pirmininkavimas/pirmininkavimas-10280249/')

