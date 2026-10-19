

# Generated at 2022-06-14 17:27:19.864994
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ViafreeIE.suitable('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')
    ViafreeIE.suitable('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869?autostart=true')
    ViafreeIE.suitable('mtg:676869')

# Generated at 2022-06-14 17:27:29.926920
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    assert TVPlayIE.IE_NAME is not None
    assert TVPlayIE.IE_DESC is not None
    assert TVPlayIE._VALID_URL is not None
    assert TVPlayIE._TESTS is not None
    ie = TVPlayIE()
    ie._initialize_geo_bypass('Countries')
    ie._initialize_geo_bypass({'countries': ['LT', 'LV', 'EE']})
    ie._real_extract('mtg:418113')
    ie._match_id('mtg:418113')
    ie._match_id('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')


# Generated at 2022-06-14 17:27:33.226046
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    klass = TVPlayHomeIE({})
    klass._initialize_geo_bypass({})

# Generated at 2022-06-14 17:27:37.050909
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE("https://play.tv3.ee/cool-d-ga-mehhikosse-10044354")
    assert ie is not None

# Generated at 2022-06-14 17:27:39.536684
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    viafreeIE = ViafreeIE()
    assert TVPlayIE.suitable('') == False
    assert viafreeIE.suitable('') == True

# Generated at 2022-06-14 17:27:42.322615
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    """
    Test for constructor of class TVPlayHomeIE.
    """
    ie = TVPlayHomeIE()
    print('Test for constructor of class TVPlayHomeIE.')


# Generated at 2022-06-14 17:27:42.977112
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    TVPlayHomeIE()

# Generated at 2022-06-14 17:27:46.992134
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    viafree = ViafreeIE(None)
    assert viafree.suitable('http://www.viafree.dk/programmer/underholdning/det-beste-vorspielet/saeson-2/episode-1')


# Generated at 2022-06-14 17:27:50.015740
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    _ViafreeIE = ViafreeIE(None)
    assert(isinstance(_ViafreeIE, ViafreeIE))

# Generated at 2022-06-14 17:27:50.568312
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    pass


# Generated at 2022-06-14 17:28:19.727592
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    tplay_ie = TVPlayIE()


# Generated at 2022-06-14 17:28:22.372562
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    """
    Test correct construct of class ViafreeIE
    """
    try:
        assert(ViafreeIE.suitable(''))
    except AssertionError:
        return False
    return True


# Generated at 2022-06-14 17:28:32.533000
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    import unittest

    class TestViafreeIE(unittest.TestCase):
        class MyExtractor(ViafreeIE):
            _VALID_URL = None

        def test_geo_restriction(self):
            self.assertEqual(
                ViafreeIE._geo_bypass,
                TestViafreeIE.MyExtractor._geo_bypass)
            TestViafreeIE.MyExtractor._GEO_BYPASS = False
            self.assertEqual(
                ViafreeIE._geo_bypass,
                TestViafreeIE.MyExtractor._geo_bypass)
            TestViafreeIE.MyExtractor._GEO_BYPASS = True

# Generated at 2022-06-14 17:28:33.602296
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    assert TVPlayIE is InfoExtractor



# Generated at 2022-06-14 17:28:46.293513
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    """Unit test for class ViafreeIE"""
    class TestClass(ViafreeIE):
        def _real_extract(self, url):
            return self.suitable(url)
    def test_normal(url):
        assert TestClass().suitable(url)
    def test_unsuitable(url):
        assert not TestClass().suitable(url)
    test_normal('http://www.viafree.se/program/underhallning/det-beste-vorspielet/sesong-2/episode-1')
    test_unsuitable('http://www.tv3play.se/program/husraddarna/395385?autostart=true')

# Generated at 2022-06-14 17:28:49.061562
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    assert isinstance(ViafreeIE.suitable('http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2'), bool)


# Generated at 2022-06-14 17:29:00.968881
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    from youtube_dl.extractor import YoutubeIE
    from youtube_dl.extractor.MTG import TVPlayIE, ViafreeIE


# Generated at 2022-06-14 17:29:03.564399
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    class_ = globals()['TVPlayIE']
    instance = class_(None)
    assert isinstance(instance, TVPlayIE)



# Generated at 2022-06-14 17:29:14.051499
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    from .test.test_youtube_dl import setUp as test_youtube_dl_setUp
    test_youtube_dl_setUp()
    # from . import TVPlayIE
    # tvplay = TVPlayIE('http://play.tv3.ee/sisu/kodu-keset-linna/238551?autostart=true')
    # assert tvplay.url=='http://play.tv3.ee/sisu/kodu-keset-linna/238551?autostart=true'
    # assert tvplay.video_id=='238551'


# Generated at 2022-06-14 17:29:25.258762
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    # Test list of domain patterns
    assert TVPlayIE._DOMAIN_PATTERNS == [
        r'(?:tv3(?:3|6|8|10)play|viasat4play|tv6play|viafree)\.se',
        r'(?:(?:tv3play|viasat4play|tv6play|viafree)\.no|(?:tv3play|viafree)\.dk)',
        r'play\.tv3\.lt',
        r'tvplay(?:\.skaties)?\.lv',
        r'tvplay\.ee',
        r'tvplay\.tv3\.ee',
        r'viafree\.se',
        r'play\.nova(?:tv)?\.bg',
    ]

    # Test info extraction with sample url and video id:
    # "http://www.tv3play

# Generated at 2022-06-14 17:30:01.663009
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    TVPlayHomeIE()

# Generated at 2022-06-14 17:30:14.406436
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE("https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/")
    assert ie.IE_NAME == "TVPlayHome"
    assert ie.SUFFIX == "https://tvplay.skaties.lv/vinas-melo-labak/"
    assert ie.VALID_URL == "https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/"
    assert ie._VALID_URL == r'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'



# Generated at 2022-06-14 17:30:17.136383
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    try:
        temp = ViafreeIE()
    except:
        assert False, "Should not raise exception."
    assert(temp is not None)

# Generated at 2022-06-14 17:30:22.428015
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    # Create an instance of the class
    class_instance = TVPlayIE()

    # Check that the _VALID_URL matches the URL given in the extractor.
    assert class_instance._match_id("http://www.tv3play.ee/sisu/kodu-keset-linna/238551?autostart=true") == '238551'


# Generated at 2022-06-14 17:30:28.673165
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    """
    TVPlayIE uses a bit more complex url regex than YoutubeIE.
    This is a unit test to verify that the regex matches.
    """
    ie = TVPlayIE()
    regex = re.compile(ie._VALID_URL)

    search_test = lambda x: re.search(regex, x)
    assert search_test('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert search_test('http://play.tv3.lt/programos/moterys-meluoja-geriau/409229?autostart=true')
    assert search_test('http://www.tv3play.ee/sisu/kodu-keset-linna/238551?autostart=true')
    assert search_

# Generated at 2022-06-14 17:30:30.259091
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    """Test constructor of class ViafreeIE."""
    ViafreeIE(None)



# Generated at 2022-06-14 17:30:32.546620
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    url = 'https://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2'
    assert ViafreeIE.suitable(url)

# Generated at 2022-06-14 17:30:39.469102
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE("https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/")
    assert ie.VALID_URL == 'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'
    assert ie.IE_NAME == 'tvplay'
    assert ie.SHORT_NAME == 'tvplay'

# Generated at 2022-06-14 17:30:41.049250
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    IE = ViafreeIE
    assert(IE.suitable(IE._VALID_URL) == False)

# Generated at 2022-06-14 17:30:47.065291
# Unit test for constructor of class ViafreeIE

# Generated at 2022-06-14 17:32:06.277636
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    tvplay_home_ie = TVPlayHomeIE()

    assert isinstance(tvplay_home_ie, TVPlayHomeIE)
    assert tvplay_home_ie._VALID_URL == r'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'


# Generated at 2022-06-14 17:32:08.328594
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()
    assert ie and ie.IE_NAME == 'mtg' and ie.IE_DESC == 'MTG services'


# Generated at 2022-06-14 17:32:13.141641
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    obj_1 = TVPlayIE()
    # Test for regex match function
    obj_1._match_id('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')

if __name__ == '__main__':
    test_TVPlayIE()

# Generated at 2022-06-14 17:32:19.745428
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    url = 'https://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'
    m = ViafreeIE._VALID_URL_TEMPLATE.search(url)
    assert(m.group(1) == 'https')
    assert(m.group(2) == 'viafree.no')
    assert(m.group(3) == 'programmer')
    assert(m.group(4) == 'underholdning/det-beste-vorspielet')
    assert(m.group(5) == 'sesong-2/episode-1')
    assert(ViafreeIE.suitable(url))

# Generated at 2022-06-14 17:32:22.574371
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    tv = TVPlayIE()
    assert tv._VALID_URL == r'(?x)tvplay[^/]+/\d+'
    assert tv._TESTS
    assert tv._download_json

# Generated at 2022-06-14 17:32:24.971399
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()
    assert ie._VALID_URL == '''(?x)
        https?://
            (?:www\.)?
            viafree\.(dk|no|se)
            /(program(?:mer)?/(?:[^/]+/)+[^/?#&]+)
        '''


# Generated at 2022-06-14 17:32:36.601266
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    viafree = ViafreeIE()
    assert viafree.suitable('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1') == True
    assert viafree.suitable('https://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5') == True
    assert viafree.suitable('http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2') == True
    assert viafree.suitable('http://play.novatv.bg/programi/zdravei-bulgariya/624952?autostart=true') == False


# Generated at 2022-06-14 17:32:40.295815
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    tvplay_test_inst = TVPlayIE()
    assert tvplay_test_inst.IE_NAME == 'mtg'
    assert tvplay_test_inst.IE_DESC == 'MTG services'
    assert len(tvplay_test_inst._TESTS) == 23



# Generated at 2022-06-14 17:32:48.092846
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    tvplay_inst = TVPlayIE()
    viafree_inst = ViafreeIE()
    assert_equal(tvplay_inst._TESTS, viafree_inst._TESTS)
    assert_equal(tvplay_inst.GEO_COUNTRIES, viafree_inst.GEO_COUNTRIES)
    assert_equal(tvplay_inst.BRIGHTCOVE_URL_TEMPLATE, viafree_inst.BRIGHTCOVE_URL_TEMPLATE)


# Generated at 2022-06-14 17:32:56.666232
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2022-06-14 17:36:27.202408
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    viafree = ViafreeIE()
    assert isinstance(viafree, InfoExtractor)

# Generated at 2022-06-14 17:36:30.060486
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    viafreeIE = ViafreeIE()
    assert viafreeIE is not None

# Generated at 2022-06-14 17:36:38.114179
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    a = TVPlayHomeIE()
    assert a._VALID_URL == 'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'

# Generated at 2022-06-14 17:36:40.068249
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    if isinstance(ie, TVPlayHomeIE):
        pass


# Generated at 2022-06-14 17:36:41.848322
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    from . import tvplayhome
    assert isinstance(tvplayhome.TVPlayHomeIE(), TVPlayHomeIE)

# Generated at 2022-06-14 17:36:51.996117
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    assert TVPlayIE._VALID_URL == 'https?://(?:www\\.)?(?:tvplay(?:\\.skaties)?\\.lv(?:/parraides)?|(?:tv3play|play\\.tv3)\\.lt(?:/programos)?|tv3play(?:\\.tv3)?\\.ee/sisu|(?:tv(?:3|6|8|10)play|viafree)\\.se/program|(?:(?:tv3play|viasat4play|tv6play|viafree)\\.no|(?:tv3play|viafree)\\.dk)/programmer|play\\.nova(?:tv)?\\.bg/programi)/(?:[^/]+/)+(?P<id>\\d+)'