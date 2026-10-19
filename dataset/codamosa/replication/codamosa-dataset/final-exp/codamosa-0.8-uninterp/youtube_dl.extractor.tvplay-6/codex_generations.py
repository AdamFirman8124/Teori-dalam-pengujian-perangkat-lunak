

# Generated at 2022-06-14 17:27:29.881501
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    i = TVPlayHomeIE('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/')
    assert isinstance(i, TVPlayHomeIE)
    assert i.BASE_URL == 'https://tvplay.tv3.lt/'
    assert i.IE_NAME == 'tvplay.tv3.lt'
    assert i.COUNTRY == 'lt'
    
    i = TVPlayHomeIE('https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/')
    assert isinstance(i, TVPlayHomeIE)
    assert i.BASE_URL == 'https://tvplay.skaties.lv/'

# Generated at 2022-06-14 17:27:43.077660
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    TVPlayHomeIE('https://play.tv3.lt/aferistai-10047125')
    TVPlayHomeIE('https://tv3play.skaties.lv/vinas-melo-labak-10280317')
    TVPlayHomeIE('https://play.tv3.ee/cool-d-ga-mehhikosse-10044354')
    TVPlayHomeIE('https://tvplay.tv3.lt/amerikietiskas-siaubo-istorijos/amerikietiskas-siaubo-istorijos-10047282/')
    TVPlayHomeIE('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/')

# Generated at 2022-06-14 17:27:48.055731
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/')
    assert ie._VALID_URL == TVPlayHomeIE._VALID_URL
    assert ie._TESTS == TVPlayHomeIE._TESTS


# Generated at 2022-06-14 17:27:54.545356
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')
    assert ie._VALID_URL == 'https?://(?:www\.)?viafree\.(?:se)/(?:program(?:mer)?/(?:[^/]+/)+[^/?#&]+)'
    assert ie._GEO_BYPASS == False
    


# Generated at 2022-06-14 17:28:04.559278
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()
    ie._initialize_geo_bypass({"countries": ["SE", "DK", "NO", "LT", "LV", "EE", "BG"]})
    url = 'http://www.tv3play.lt/programos/moterys-meluoja-geriau/409229?autostart=true'
    res = ie._real_extract_se(url)
    assert res["age_limit"] == None
    assert res["duration"] == 1330
    assert res["formats"][0]["url"] == "http://fms.105.lt:1935/a1015/o10/playlist.m3u8?1405355355224001"
    assert res["formats"][0]["quality"] == 144
    assert res["subtitles"] == {}

# Generated at 2022-06-14 17:28:16.268004
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    from . import TVPlayHomeIE
    a = TVPlayHomeIE("http://tv3play.tv3.ee/cool-d-ga-mehhikosse/cool-d-ga-mehhikosse-10044354/")
    assert a.__class__ == TVPlayHomeIE
    assert a._VALID_URL == "https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)"
    # should not raise HTTPError(403 Forbidden)
    a._real_extract("https://tv3play.tv3.ee/cool-d-ga-mehhikosse/cool-d-ga-mehhikosse-10044354/")
    a._

# Generated at 2022-06-14 17:28:19.024036
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance = TVPlayHomeIE('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/')
    assert isinstance(instance, TVPlayHomeIE)



# Generated at 2022-06-14 17:28:24.352702
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    constructor_test(ViafreeIE, [
        'http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2',
        'http://www.viafree.se/program/underhallning/det-beste-vorspielet/sesong-2/episode-1',
        'http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5'
    ])

# Generated at 2022-06-14 17:28:25.111201
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    test_obj = TVPlayHomeIE()

# Generated at 2022-06-14 17:28:27.207542
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    try:
        TVPlayHomeIE()  # pylint:disable=abstract-class-instantiated
    except TypeError:
        pass
    else:
        raise AssertionError('Must raise TypeError')

# Generated at 2022-06-14 17:29:03.913966
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    assert isinstance(ViafreeIE(TVPlayIE()), type(TVPlayIE()))


# Generated at 2022-06-14 17:29:06.241091
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    from . import ViafreeIE



# Generated at 2022-06-14 17:29:16.178840
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    """Unit test for constructor of class TVPlayHomeIE."""
    # Creating an instance of the class to be tested
    ie = TVPlayHomeIE()

    # Valid URL
    url = 'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/'
    # Checking URL validity
    assert ie._match_id(url)

    # Invalid URL
    url = 'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/asdf'
    # Checking URL validity
    assert ie._match_id(url) is None

# Generated at 2022-06-14 17:29:23.878059
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE
    assert ie._VALID_URL == r'''(?x)
                    https?://
                        (?:www\.)?
                        viafree\.(?P<country>dk|no|se)
                        /(?P<id>program(?:mer)?/(?:[^/]+/)+[^/?#&]+)
                    '''
    assert ie._TESTS[0]['url'] == 'http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'
    assert ie._TESTS[0]['info_dict']['id'] == '757786'
    assert ie._TESTS[0]['info_dict']['ext'] == 'mp4'

# Generated at 2022-06-14 17:29:26.296131
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE({})
    assert ie.SUITES == {
        'fallback': TVPlayHomeFallbackIE,
        'mtg': TVPlayIE,
    }



# Generated at 2022-06-14 17:29:27.214183
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ViafreeIE()


# Generated at 2022-06-14 17:29:35.003424
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    tvplayhome_info_extractor = TVPlayHomeIE('TVPlayHomeIE')
    assert tvplayhome_info_extractor._VALID_URL == r'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'
    assert tvplayhome_info_extractor._TESTS[0]['url'] == 'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/'
    assert tvplayhome_info_extractor._TESTS[0]['info_dict']['id'] == '366367'

# Generated at 2022-06-14 17:29:38.967595
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    check_constructor(TVPlayHomeIE)



# Generated at 2022-06-14 17:29:47.588603
# Unit test for constructor of class TVPlayIE

# Generated at 2022-06-14 17:29:53.870162
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # test pattern extraction
    o = ViafreeIE._VALID_URL
    assert re.match(o, 'http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert re.match(o, 'http://www.viafree.no/programmer/reality/paradise-hotel/saeson-7/episode-5')
    assert re.match(o, 'http://www.viafree.se/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-2')
    assert re.match(o, 'http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')



# Generated at 2022-06-14 17:30:33.185879
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    try:
        import urllib2
    except ImportError:
        import urllib.request as urllib2

    try:
        urllib2.urlopen('http://www.tv3play.ee/sisu/kodu-keset-linna/238551?autostart=true')
        TVPlayIE()
    except urllib2.URLError:
        pass


# Generated at 2022-06-14 17:30:42.989169
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    for url in [
        'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/',
        'https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/',
        'https://tvplay.tv3.ee/cool-d-ga-mehhikosse/cool-d-ga-mehhikosse-10044354/',
        'https://play.tv3.lt/aferistai-10047125',
        'https://tv3play.skaties.lv/vinas-melo-labak-10280317',
        'https://play.tv3.ee/cool-d-ga-mehhikosse-10044354'
    ]:
        assertTVPlay

# Generated at 2022-06-14 17:30:50.344964
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    assert TVPlayHomeIE.suitable('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/')
    assert TVPlayHomeIE('TVPlayHome', 'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/')._VALID_URL == r'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'


# Generated at 2022-06-14 17:30:53.308741
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    instance = TVPlayIE()
    assert isinstance(instance, TVPlayIE)


# Generated at 2022-06-14 17:30:57.881485
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # Test URL
    url = str('http://www.viafree.se/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-1')
    # Create test class
    test = ViafreeIE()
    # Test constructor
    assert test.suitable(url) == True

# Generated at 2022-06-14 17:31:10.542989
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()
    ie._match_id('http://play.tv3play.lt/programos/moterys-meluoja-geriau/409229?autostart=true')
    ie._match_id('http://tvplay.skaties.lv/parraides/vinas-melo-labak/418113?autostart=true')
    ie._match_id('https://tvplay.skaties.lv/vinas-melo-labak/418113/?autostart=true')
    ie._match_id('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')
    # TODO
    # ie._match_id('http://www.tv3play.se/program/husraddarna/

# Generated at 2022-06-14 17:31:13.262789
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    assert isinstance(ViafreeIE(), ViafreeIE)

# Generated at 2022-06-14 17:31:22.479829
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    from .test_mtg import test_mtg
    videos_dict = test_mtg()
    for url, info in videos_dict.items():
        url_parts = urlparse(url)
        country = url_parts.netloc.rsplit('.', 1)[-1]
        path = url_parts.path.lstrip('/')
        viafree_url = 'http://www.' + url_parts.netloc + '/' + path
        info['url'] = viafree_url
        assert info == ViafreeIE()._real_extract(viafree_url)

# Generated at 2022-06-14 17:31:32.866656
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    viafree = ViafreeIE()
    assert viafree._VALID_URL == r'''(?x)
                    https?://
                        (?:www\.)?
                        viafree\.(?P<country>dk|no|se)
                        /(?P<id>program(?:mer)?/(?:[^/]+/)+[^/?#&]+)
                    '''

# Generated at 2022-06-14 17:31:34.110624
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE(None)
    assert bool(ie)

# Generated at 2022-06-14 17:33:09.170785
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ViafreeIE({})._real_initialize({})

# Generated at 2022-06-14 17:33:19.687820
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    url = 'http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'
    viafree = ViafreeIE()
    viafree._download_json = lambda url: {}
    assert viafree._call_api(url, '{}') == {}
    assert viafree._api_base_url == 'https://viafree-content.mtg-api.com/viafree-content/v1/'
    assert viafree._get_content_url(url) == 'https://viafree-content.mtg-api.com/viafree-content/v1/no/path/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'

# Generated at 2022-06-14 17:33:23.762559
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    obj = ViafreeIE()
    assert obj._VALID_URL is not None
    assert obj._TESTS is not None
    assert obj._GEO_BYPASS is not None
    assert obj.suitable(None) is not None
    assert obj._real_extract(None) is not None

# Generated at 2022-06-14 17:33:35.867119
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    i = TVPlayHomeIE()
    assert i._VALID_URL == r'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'

# Generated at 2022-06-14 17:33:46.205458
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2022-06-14 17:33:50.148128
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE().__class__(TVPlayHomeIE.__name__)
    assert ie.__name__ == 'TVPlayHomeIE'


# Generated at 2022-06-14 17:33:52.396820
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    #Constructor of TVPlayIE
    assert TVPlayIE('mtg', 'mtg services')

# Generated at 2022-06-14 17:33:54.225303
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    TVPlayHomeIE()



# Generated at 2022-06-14 17:33:56.668204
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    TestInfoExtractor(TVPlayHomeIE).test()



# Generated at 2022-06-14 17:33:59.432032
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    viafree_ie = ViafreeIE()
    # Just check if the construtor works
    checked = True
    assert checked == True
