

# Generated at 2022-06-14 17:27:18.819430
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    obj = TVPlayHomeIE('test', 'test')
    assert obj is not None

# Generated at 2022-06-14 17:27:20.936977
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE(None)
    assert isinstance(ie, ViafreeIE)
    assert isinstance(ie, InfoExtractor)

# Generated at 2022-06-14 17:27:31.530671
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert ie.name == 'TVPlayHome'
    assert ie.IE_NAME == 'TVPlayHome'
    assert ie.valid_url('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/')
    assert ie.valid_url('https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/')
    assert ie.valid_url('https://tvplay.tv3.ee/cool-d-ga-mehhikosse/cool-d-ga-mehhikosse-10044354/')
    assert ie.valid_url('https://play.tv3.lt/aferistai-10047125')

# Generated at 2022-06-14 17:27:43.055830
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    IE = TVPlayIE()
    assert (IE.IE_NAME == 'mtg')
    assert (IE.IE_DESC == 'MTG services')

# Generated at 2022-06-14 17:27:49.092671
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    try:
        ViafreeIE()
    except UnsupportedError:
        # --- skipped test ---
        # It raises an exception since the test is not executed in the suitable geographical area.
        #
        # The following exception is thrown:
        #
        # UnsupportedError: This content might not be available in your country due to copyright reasons
        pass


# Generated at 2022-06-14 17:28:01.076478
# Unit test for constructor of class TVPlayIE

# Generated at 2022-06-14 17:28:12.739035
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    url1 = b'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/'
    url2 = b'https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/'
    url3 = b'https://tvplay.tv3.ee/cool-d-ga-mehhikosse/cool-d-ga-mehhikosse-10044354/'
    # test valid URL
    assert TVPlayHomeIE.suitable(url1)
    assert TVPlayHomeIE.suitable(url2)
    assert TVPlayHomeIE.suitable(url3)
    # test invalid URL

# Generated at 2022-06-14 17:28:17.603720
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    import unittest
    import sys
    import json
    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO
    import httpretty
    from httpretty import HTTPretty
    from httpretty import httprettified

    url = 'https://tvplay.tv3.lv/fermeri-10051323/'
    data = json.load(open('test/test_TVPlayHomeIE.json', 'rb'))
    expected_id = '368104'
    expected_title = 'Fermēri'

    @httprettified
    def do_test():
        HTTPretty.register_uri(HTTPretty.GET, url,
                body=json.dumps(data),
                content_type='application/json')
        ie = TVPlayHomeIE()
        url = url
        res

# Generated at 2022-06-14 17:28:18.229051
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    TVPlayHomeIE()

# Generated at 2022-06-14 17:28:28.018269
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    tvplay = TVPlayIE()
    assert tvplay.IE_NAME == 'mtg'
    assert tvplay.IE_DESC == 'MTG services'
    assert tvplay.valid_url.__doc__ == 'Regex for valid URLs'

# Generated at 2022-06-14 17:29:10.711800
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()
    try:
        ie.suitable('')
        raise AssertionError('No exception thrown')
    except RegexNotFoundError as e:
        pass
    assert ie.suitable('https://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')
    assert ie.suitable('https://www.viafree.se/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-2')
    assert not ie.suitable('https://play.tv3.lt/programa/sekmadienio-magija/624952')

# Generated at 2022-06-14 17:29:17.764454
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    all_formats_before_transformation = [{
        'url': 'https://tv3play-vh.akamaihd.net/i/filmas/skaties-tv3/vinas_melo_labak/vinas_melo_labak_s01_ep04_hd_11639914_,1280,720,360,22,50,000001.mp4.csmil/master.m3u8'
    }]

# Generated at 2022-06-14 17:29:18.712257
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    TVPlayIE(None)


# Generated at 2022-06-14 17:29:26.065056
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    old_mtg_init_func = TVPlayIE.__init__
    def mtg_init_func(self, *args, **kwargs):
        old_mtg_init_func(self, *args, **kwargs)
        self.tvplay_test_result = 'mtg_test_ok'

    TVPlayIE.__init__ = mtg_init_func
    ie = TVPlayIE()
    TVPlayIE.__init__ = old_mtg_init_func

    assert ie.tvplay_test_result == 'mtg_test_ok'



# Generated at 2022-06-14 17:29:26.936434
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance = TVPlayHomeIE()

# Generated at 2022-06-14 17:29:34.822381
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE('http://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/')
    assert ie._VALID_URL == 'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'
    assert ie.suitable('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/')
    assert ie.suitable('https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/')

# Generated at 2022-06-14 17:29:46.764088
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    assert re.match(ViafreeIE._VALID_URL, 'http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2')
    assert not ViafreeIE.suitable('http://tvplay.skaties.lv/parraides/tv3-zinas/760183')
    assert ViafreeIE.suitable('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')
    assert not re.match(ViafreeIE._VALID_URL, 'http://tvplay.skaties.lv/parraides/tv3-zinas/760183')

# Generated at 2022-06-14 17:29:48.173172
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    TVPlayIE('http://playapi.mtgx.tv/v3/videos/418113')


# Generated at 2022-06-14 17:29:54.351278
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    """
    construction of class ViafreeIE.
    """
    assert_raises(ValueError, ViafreeIE, {}, 'http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2')
    assert_raises(ValueError, ViafreeIE, {}, 'http://www.tv3play.no/programmer/anna-anka-soker-assistent/230898?autostart=true')
    assert_raises(ValueError, ViafreeIE, {}, 'http://tv3play.tv3.ee/sisu/kodu-keset-linna/238551?autostart=true')

# Generated at 2022-06-14 17:29:57.924526
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()
    assert ie.suitable('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')
    assert ie_key('ViafreeIE') in globals().keys()



# Generated at 2022-06-14 17:31:16.586069
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    IE = TVPlayHomeIE(None)
    obj = TVPlayHomeIE(IE)
    obj_2 = TVPlayHomeIE(TVPlayHomeIE)
    assert object == type(obj)
    assert TVPlayHomeIE == type(obj_2)

# Generated at 2022-06-14 17:31:17.848198
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    e = TVPlayHomeIE()

# Generated at 2022-06-14 17:31:19.544922
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ViafreeIE.suitable(ViafreeIE._VALID_URL)

# Generated at 2022-06-14 17:31:24.997126
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    url = 'http://www.tv3play.ee/sisu/kodu-keset-linna/238551?autostart=true'
    TVPlayIE()._real_extract(url)

# Test for videos only available from geo-restricted regions
# Currently disabled as this test has been failing for a long time

# Generated at 2022-06-14 17:31:34.982583
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # pylint: disable=no-member
    # No need to test geo-restrictedness or output format
    class FakeInfoExtractor(ViafreeIE):
        def _real_extract(self, url):
            return {
                'id': 'test_id',
                'formats': [],
            }
    class FakeChannelIE(FakeInfoExtractor, ChannelIE):
        pass
    class FakeProgramIE(FakeInfoExtractor, ProgramIE):
        pass

    for class_ in (FakeChannelIE, FakeProgramIE):
        ie = class_.suitable(None) and class_(None) or None
        assert ie

        assert ie._GEO_BYPASS == FakeInfoExtractor._GEO_BYPASS
        assert ie._VALID_URL == FakeInfoExtractor._VALID_URL
        assert ie.IE_NAME == FakeInfo

# Generated at 2022-06-14 17:31:36.006877
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    TVPlayHomeIE()


# Generated at 2022-06-14 17:31:38.723019
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    params = {
        'url': 'https://tv3play.skaties.lv/vinas-melo-labak-10280317',
    }
    ie = TVPlayHomeIE(params)
    assert ie.can_extract(params) == True


# Generated at 2022-06-14 17:31:45.253857
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    _tvplay_home_ies = [
        TVPlayHomeIE,
        TV3PlayLTIE,
        SkatiesLVIE,
        TV3PlayEEIE
    ]
    for _tvplay_home_ie in _tvplay_home_ies:
        tvplay_home_ie = _tvplay_home_ie()
        assert tvplay_home_ie._VALID_URL == r'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'

# Generated at 2022-06-14 17:31:54.206134
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    viafree_ie = ViafreeIE()
    assert viafree_ie.suitable('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert viafree_ie.suitable('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert not viafree_ie.suitable('http://www.tv3play.se/kanaler/tv3/kanal-9/program/nyhetsmorgon-i-tv4/372629?autostart=true')

# Generated at 2022-06-14 17:32:00.452873
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    a = ViafreeIE()
    assert TVPlayIE.suitable('http://tvplay.skaties.lv/parraides/vinas-melo-labak/418113?autostart=true') == False
    assert ViafreeIE.suitable('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5') == True
    assert ViafreeIE.suitable('http://tvplay.skaties.lv/parraides/vinas-melo-labak/418113?autostart=true') == False
    assert ViafreeIE.suitable('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5') == True

# Generated at 2022-06-14 17:35:30.167049
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    from .test_htmlparser import MockHTMLParser
    from .test_m3u8_native import MockM3U8
    from .test_rottentomatoes import MockRottenTomatoesIE

    mock_html_parser = MockHTMLParser()

# Generated at 2022-06-14 17:35:37.370616
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE('http://play.tv3.ee/cool-d-ga-mehhikosse-10044354/')
    assert ie._VALID_URL == r'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'


# Generated at 2022-06-14 17:35:42.361713
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    x = TVPlayHomeIE()
    assert x.SUITABLE == 'universal'
    assert x._VALID_URL == r'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'

# Generated at 2022-06-14 17:35:45.031055
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    TVPlayIE('some url')



# Generated at 2022-06-14 17:35:49.495074
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    tvplay = TVPlayIE()
    assert tvplay.IE_NAME == 'tvplay'
    assert tvplay.IE_DESC == 'tvplay'
    assert tvplay._VALID_URL == r'(?x)http://(?:www\.)?tvplay\.lv/parraides/.+?/(?P<id>\d+)'



# Generated at 2022-06-14 17:35:50.431518
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()



# Generated at 2022-06-14 17:35:55.018025
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE('TVPlayHome', 'tv3play-skaties.lv')
    assert ie.VALID_URL == TVPlayHomeIE._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome'
    assert ie.country == 'skaties.lv'

# Generated at 2022-06-14 17:35:58.783796
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # This will run the constructor of this class
    ie =  ViafreeIE('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')
    assert ie.geo_verification_headers() == None



# Generated at 2022-06-14 17:36:01.869531
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    url = "http://www.viafree.se/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-2"
    TestViafreeIE = ViafreeIE(url, True)

    assert TestViafreeIE.url == url
    assert TestViafreeIE.country == "se"
    assert TestViafreeIE.path == "program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-2"

# Generated at 2022-06-14 17:36:02.892097
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    assert TVPlayHomeIE(TVPlayHomeIE.ie_key()) is not None

