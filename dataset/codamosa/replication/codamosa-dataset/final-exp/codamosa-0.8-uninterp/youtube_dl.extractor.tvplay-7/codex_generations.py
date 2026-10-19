

# Generated at 2022-06-14 17:27:20.164918
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    """Unit test for constructor of class ViafreeIE.

    This test is designed to test if you have correctly defined an object
    of class ViafreeIE.
    """
    ViafreeIE(TVPlayIE())

# Generated at 2022-06-14 17:27:30.880211
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    t = TVPlayIE()
    assert t._VALID_URL == r'(?x)https?://(?:www\.)?(?:tvplay(?:\.skaties)?\.lv(?:/parraides)?|(?:tv3play|play\.tv3)\.lt(?:/programos)?|tv3play(?:\.tv3)?\.ee/sisu|(?:tv(?:3|6|8|10)play|viafree)\.se/program|(?:(?:tv3play|viasat4play|tv6play|viafree)\.no|(?:tv3play|viafree)\.dk)/programmer|play\.nova(?:tv)?\.bg/programi)/(?:[^/]+/)+(?P<id>\d+)'
    assert t.IE_NAME == 'mtg'
    assert t

# Generated at 2022-06-14 17:27:32.073782
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    tvph = TVPlayHomeIE()
    assert tvph is not None

# Generated at 2022-06-14 17:27:43.143931
# Unit test for constructor of class TVPlayIE

# Generated at 2022-06-14 17:27:48.949998
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    # test TVPlayIE constructor
    tvplay = TVPlayIE()

# Generated at 2022-06-14 17:27:56.949540
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    from .common import fake_TVPlayIE
    from ..utils import check_valid_url
    from ..compat import compat_str

    t = TVPlayIE()
    # Assert that constructing an instance of TVPlayIE doesn't fail
    TVPlayIE(fake_TVPlayIE(), compat_str(t))
    # Assert that constructor of TVPlayIE validates URL
    check_valid_url(TVPlayIE, 'https://www.tv3play.lt/')


# Generated at 2022-06-14 17:28:02.579994
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    url = 'https://tvplay.skaties.lv/vinas-melo-labak/418113/?autostart=true'
    TVPlayIE()._match_id(url)



# Generated at 2022-06-14 17:28:14.044045
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    # tvplay.lv
    assert TVPlayIE._build_url("418113", "tvplay.lv") == "http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true"
    assert TVPlayIE._build_url("418113", "tvplay.skaties.lv") == "http://tvplay.skaties.lv/parraides/vinas-melo-labak/418113?autostart=true"
    # tvplay.skaties.lv
    assert TVPlayIE._build_url("418113", "skaties.tvplay.lv") == "http://skaties.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true"
    # tv3play.lt

# Generated at 2022-06-14 17:28:17.262314
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    TVPlayHomeIE("https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/")


# Generated at 2022-06-14 17:28:22.143476
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    tvplay = TVPlayIE()
    assert tvplay.IE_NAME == 'mtg', 'instance needs to be named mtg'
    assert tvplay.IE_DESC == 'MTG services', 'instance needs to have description MTG services'
    assert len(tvplay._TESTS) > 0, 'instance needs to have unit tests'



# Generated at 2022-06-14 17:29:00.864543
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    """
    Unit test for constructor of class TVPlayHomeIE.
    """
    check_url = 'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/'
    TVPlayHome = TVPlayHomeIE(check_url)
    assert(TVPlayHome.suitable(check_url) == False)
    return

# Generated at 2022-06-14 17:29:14.120753
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    TVPlayIE('http://www.tv3play.lv/parraides/vinas-melo-labak/418113?autostart=true')
    TVPlayIE('http://play.tv3.lt/programos/moterys-meluoja-geriau/409229?autostart=true')
    TVPlayIE('http://www.tv3play.ee/sisu/kodu-keset-linna/238551?autostart=true')
    TVPlayIE('http://www.tv3play.se/program/husraddarna/395385?autostart=true')
    TVPlayIE('http://www.tv6play.se/program/den-sista-dokusapan/266636?autostart=true')

# Generated at 2022-06-14 17:29:15.477312
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ViafreeIE.suitable(None)

# Generated at 2022-06-14 17:29:20.702248
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    url = 'https://tvplay.skaties.lv/vinas-melo-labak/418113/?autostart=true'
    print(TVPlayIE._VALID_URL)
    print('url = ' + url)
    mobj = re.match(TVPlayIE._VALID_URL, url)
    print('mobj = ' + str(mobj))
    assert(mobj is not None)



# Generated at 2022-06-14 17:29:29.705956
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    TVPlayIE("http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true")
    TVPlayIE("http://play.tv3.lt/programos/moterys-meluoja-geriau/409229?autostart=true")
    TVPlayIE("http://www.tv3play.ee/sisu/kodu-keset-linna/238551?autostart=true")
    TVPlayIE("http://www.tv3play.se/program/husraddarna/395385?autostart=true")
    TVPlayIE("http://www.tv6play.se/program/den-sista-dokusapan/266636?autostart=true")

# Generated at 2022-06-14 17:29:33.133348
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():

    url = 'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/'
    extractor = TVPlayHomeIE()
    extractor._real_extract(url)

    # This will throw exception if constructor has any problem.

# Generated at 2022-06-14 17:29:44.869818
# Unit test for constructor of class ViafreeIE

# Generated at 2022-06-14 17:29:55.380856
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

# Generated at 2022-06-14 17:30:00.106885
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    tvplay_ie = TVPlayIE()
    assert TVPlayIE.IE_NAME in tvplay_ie.IE_NAME
    assert TVPlayIE.IE_DESC in tvplay_ie.IE_DESC


# Generated at 2022-06-14 17:30:11.962580
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert isinstance(ie._VALID_URL, type(re.compile('pattern')))
    assert ie._VALID_URL.pattern == r'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'

# Generated at 2022-06-14 17:30:57.694083
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    IE = TVPlayIE()

# Generated at 2022-06-14 17:31:10.274021
# Unit test for constructor of class ViafreeIE

# Generated at 2022-06-14 17:31:16.031586
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    name = 'TVPlayHome'
    klass = globals()[name + 'IE']
    instance = klass()
    yield (lambda: klass)
    yield (lambda: instance.suitable(klass._VALID_URL))
    yield (lambda: instance.IE_NAME == name)
    # Test for sign check
    url = 'https://play.tv3.pt/videos/9393572?auth=sometokensometokensometokensometokensometokensometokensometokensometoken'
    yield (lambda: not instance.suitable(url))

# Generated at 2022-06-14 17:31:20.225191
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()
    assert ie._VALID_URL == TVPlayIE._VALID_URL
    assert ie.IE_NAME == TVPlayIE.IE_NAME
    assert ie.IE_DESC == TVPlayIE.IE_DESC


# Generated at 2022-06-14 17:31:24.866187
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    url = 'http://www.viafree.no/programmer/reality/paradise-hotel/saeson-7/episode-5'
    test_ViafreeIE = ViafreeIE()
    assert_equals(test_ViafreeIE._VALID_URL, url)

# Generated at 2022-06-14 17:31:34.865344
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE('http://www.tv3play.lt/programos/moterys-meluoja-geriau/409229?autostart=true')
    assert ie.video_id == "409229"
    assert ie.url_info == {
        'age_limit': 0,
        'autostart': 'true',
        'id': '409229',
        'series': 'Moterys meluoja geriau',
    }
    assert ie.url_allowed == "http://play.tv3.lt/programos/moterys-meluoja-geriau/409229?autostart=true"
    assert ie.url_page == "http://www.tv3play.lt/programos/moterys-meluoja-geriau/409229?autostart=true"


# Generated at 2022-06-14 17:31:38.092577
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE('se')
    assert ie.VALID_URL == r'https?://(?:www\.)?viafree\.(?P<country>se)/(?P<id>program(?:mer)?/(?:[^/]+/)+[^/?#&]+)'



# Generated at 2022-06-14 17:31:40.834439
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    """Test constructor of class ViafreeIE."""
    url = 'http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5'
    viafree = ViafreeIE(url)
    assert viafree._VALID_URL == url


# Generated at 2022-06-14 17:31:42.743462
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert ie is not None


# Generated at 2022-06-14 17:31:54.203916
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert ie.IE_NAME == 'mtg'

# Generated at 2022-06-14 17:33:25.619256
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    assert TVPlayHomeIE._TEST.startswith('http://')



# Generated at 2022-06-14 17:33:30.122115
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    from .test import get_testcases
    for case in get_testcases(ViafreeIE, 'ViafreeIE'):
        yield case[0], case[1]

# Generated at 2022-06-14 17:33:40.641977
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    url = 'https://play.tv3play.lt/programos/moterys-meluoja-geriau/409229?autostart=true'
    os = TVPlayIE()
    # test check_url method
    assert os.check_url(url) == True
    # test extractor _match_id method
    video_id = os._match_id(url)
    assert video_id == '409229'
    # test extractor _initialize_geo_bypass method
    os._initialize_geo_bypass({"countries": ['LT']})
    video = os._download_json('http://playapi.mtgx.tv/v3/videos/%s' % video_id, video_id, 'Downloading video JSON')
    assert video['id'] == video_id
    # test

# Generated at 2022-06-14 17:33:41.982680
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    t = TVPlayIE()
    assert t == TVPlayIE()


# Generated at 2022-06-14 17:33:51.026274
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE('https://tvplay.tv3.ee/cool-d-ga-mehhikosse-10044354')
    assert ie.SUFFIX == '.ee'
    assert ie.GEO_COUNTRIES == ['EE']

    ie = TVPlayHomeIE('https://tvplay.tv3.lt/vinas-melo-labak-10280317')
    assert ie.SUFFIX == '.lt'
    assert ie.GEO_COUNTRIES == ['LT']

    ie = TVPlayHomeIE('https://tvplay.skaties.lv/vinas-melo-labak-10280317')
    assert ie.SUFFIX == '.lv'
    assert ie.GEO_COUNTRIES == ['LV']



# Generated at 2022-06-14 17:34:00.317287
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    """
    Test to verify that a valid Geo restricted TVPlayIE instance is created
    """
    _valid_url = "http://www.tv3play.se/program/husraddarna/395385?autostart=true"
    geo_restricted_ie = TVPlayIE(_valid_url)
    assert(geo_restricted_ie.name == 'mtg')
    assert(geo_restricted_ie.ie_key() == 'mtg')
    assert(geo_restricted_ie.geo_verification_headers()['X-Forwarded-For'] == '195.34.89.60')
    tvplay = TVPlayIE(_valid_url)
    tvplay._initialize_geo_bypass({'countries': ['SE']})

# Generated at 2022-06-14 17:34:09.316440
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    import re
    country = 'dk'
    path = 'program/livsstil/husraddarna/sasong-2/avsnitt-2'

# Generated at 2022-06-14 17:34:16.619409
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()
    ie._initialize_geo_bypass({'countries': ['LV']})
    tvplay_url = 'http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true'
    tvplay_url_geo = 'http://www.tvplay.ee/sisu/kodu-keset-linna/238551?autostart=true'
    tvplay_url_id = 'mtg:418113'

    assert ie._real_extract(tvplay_url) is not None
    assert ie._real_extract(tvplay_url_geo) is not None
    assert ie._real_extract(tvplay_url_id) is not None


# Generated at 2022-06-14 17:34:17.971847
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE(fake_systemd.FakeSystemd())
    assert ie.__class__.__name__ == 'ViafreeIE'

# Generated at 2022-06-14 17:34:18.557023
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()



# Generated at 2022-06-14 17:36:22.805361
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    assert ViafreeIE.suitable(ViafreeIE.ie_key())
    assert ViafreeIE.suitable('https://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')
    assert '/program/' in ViafreeIE.VALID_URL
    assert not ViafreeIE.suitable(TVPlayIE.VALID_URL)

# Generated at 2022-06-14 17:36:26.293121
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    fin = """<html><body></body></html>"""
    constructor_test(ViafreeIE, fin)


# Generated at 2022-06-14 17:36:28.753720
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    """Test if the constructor is working."""
    ie = TVPlayHomeIE()
    assert ie.__class__ == TVPlayHomeIE


# Generated at 2022-06-14 17:36:29.821211
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    TVPlayIE()



# Generated at 2022-06-14 17:36:31.755990
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    try:
        TVPlayHomeIE()
    except TypeError as e:
        assert False, str(e)

# Generated at 2022-06-14 17:36:36.028995
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    # Unit test for TVPlayHomeIE
    url = 'http://tvplay.skaties.lv/parraides/vinas-melo-labak/418113?autostart=true'
    ie = TVPlayHomeIE(url)
    if ie.suitable(url):
        ie.extract(url)

# Generated at 2022-06-14 17:36:47.181863
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'

# Generated at 2022-06-14 17:36:54.583489
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    assert TVPlayIE.IE_NAME == 'mtg'
    assert TVPlayIE.IE_DESC == 'MTG services'