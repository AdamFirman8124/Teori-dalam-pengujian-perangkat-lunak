

# Generated at 2022-06-14 17:27:28.163460
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    IE = TVPlayIE()
    assert isinstance(IE, TVPlayIE)
    assert IE.IE_NAME == 'mtg'
    assert IE.IE_DESC == 'MTG services'

# Generated at 2022-06-14 17:27:29.205160
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    return TVPlayIE()


# Generated at 2022-06-14 17:27:31.208565
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()
    assert ie._VALID_URL
    assert ie._TESTS
    assert ie._GEO_BYPASS



# Generated at 2022-06-14 17:27:33.055118
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    raise NotImplementedError


# Generated at 2022-06-14 17:27:44.006327
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    TVPlayIE('mtg:418113')
    TVPlayIE('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')
    TVPlayIE('http://play.tv3.lt/programos/moterys-meluoja-geriau/409229?autostart=true')
    TVPlayIE('http://www.tv3play.ee/sisu/kodu-keset-linna/238551?autostart=true')
    TVPlayIE('http://www.tv3play.se/program/husraddarna/395385?autostart=true')
    TVPlayIE('http://www.tv6play.se/program/den-sista-dokusapan/266636?autostart=true')
    TVPlay

# Generated at 2022-06-14 17:27:49.710302
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    """
    Unit test for constructor of class ViafreeIE
    """
    regex = re.compile(ViafreeIE._VALID_URL)

    def test_valid_urls():
        """
        It should return True for valid urls
        """


# Generated at 2022-06-14 17:27:52.819862
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    instance = TVPlayIE()
    assert instance._VALID_URL == TVPlayIE._VALID_URL



# Generated at 2022-06-14 17:27:57.878271
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    assert ViafreeIE.suitable('http://www.viafree.se/program/barn/dagens-tommy/sasong-1/avsnitt-14') == True
    assert ViafreeIE.suitable('http://tvplay.skaties.lv/parraides/tv3-zinas/760183') == False
    assert ViafreeIE.suitable('foo') == False
    assert ViafreeIE.suitable('') == False
    assert ViafreeIE.suitable(None) == False



# Generated at 2022-06-14 17:28:11.093207
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():

    import requests
    import tempfile

    from .common import HEADRequest, USER_AGENTS

    from .utils import (compat_urllib_error, compat_urllib_request,
                        compat_urllib_parse, compat_urllib_parse_urlparse,
                        ExtractorError, RegexNotFoundError,
                        compat_str)


# Generated at 2022-06-14 17:28:23.168667
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE
    assert ie.IE_NAME == 'mtg', 'TVPlayIE: IE_NAME should be mtg'
    assert ie.IE_DESC == 'MTG services', 'TVPlayIE: IE_DESC should be MTG services'

# Generated at 2022-06-14 17:28:46.760200
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    class_ = globals()[TVPlayHomeIE.ie_key()]
    class_._VALID_URL = r'(?P<VALID_URL>.+)'
    instance = class_(None)
    assertEqual(
        instance._VALID_URL,
        class_._VALID_URL)


# Generated at 2022-06-14 17:28:47.771107
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ViafreeIE()
    TVPlayIE()

# Generated at 2022-06-14 17:28:50.154647
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    try:
        test_TVPlayIE = TVPlayIE()
        assert type(test_TVPlayIE) == TVPlayIE
    except:
        print("Failed to create class object")
        print("Line number of error: ", sys.exc_info()[-1].tb_lineno)
        print("Error: ", sys.exc_info())
        return False



# Generated at 2022-06-14 17:29:01.920265
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    assert TVPlayHomeIE.suitable('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/')
    assert TVPlayHomeIE.suitable('https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/')
    assert TVPlayHomeIE.suitable('https://tvplay.tv3.ee/cool-d-ga-mehhikosse/cool-d-ga-mehhikosse-10044354/')
    assert TVPlayHomeIE.suitable('https://play.tv3.lt/aferistai-10047125')
    assert TVPlayHomeIE.suitable('https://tv3play.skaties.lv/vinas-melo-labak-10280317')

# Generated at 2022-06-14 17:29:09.912448
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert ie.tvplay_id == 'tv3'
    assert ie.tvplay_home_country == 'lv'
    assert ie.tvplay_home_urls == [
        'https://tvplay.skaties.lv',
    ]
    assert ie.tvplay_api_urls == [
        'https://api.skaties.lv'
    ]



# Generated at 2022-06-14 17:29:10.695051
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    # TODO
    pass



# Generated at 2022-06-14 17:29:12.371368
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    inst = TVPlayHomeIE("")
    assert isinstance(inst, TVPlayHomeIE)

# Generated at 2022-06-14 17:29:21.834281
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2022-06-14 17:29:30.703802
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    tvplay = TVPlayIE('test')
    assert tvplay.IE_NAME == 'mtg'
    assert tvplay.IE_DESC == 'MTG services'

# Generated at 2022-06-14 17:29:32.920633
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    construct_classes = ['TVPlayHomeIE']
    instance = TVPlayHomeIE()
    assert (instance.ie_key() in construct_classes)


# Generated at 2022-06-14 17:30:20.086975
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    from . import ViafreeIE as test_ViafreeIE
    from . import InfoExtractor as test_InfoExtractor
    from . import TVPlayIE as test_TVPlayIE
    from . import mtvservicesInfoExtractor as test_mtvservicesInfoExtractor
    from . import GeoRestrictedError as test_GeoRestrictedError

    assert test_ViafreeIE.__bases__[0] is test_InfoExtractor
    assert test_ViafreeIE.__bases__[1] is test_mtvservicesInfoExtractor
    assert test_ViafreeIE.geo_country.__doc__ == 'Returns the two-letter ISO 3166-2 country code.'
    assert not hasattr(test_ViafreeIE, '_mpx_account_id')

    tvplay_ie = test_TVPlayIE()
    assert not test_Via

# Generated at 2022-06-14 17:30:23.247951
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE('url')
    assert ie.playpath == 'url'

# Generated at 2022-06-14 17:30:26.940393
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    url = 'https://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5'
    viafree = ViafreeIE(FakeYDL())
    p = viafree.suitable(url)
    # print(p)
    assert p is False


# Generated at 2022-06-14 17:30:27.618402
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    TVPlayIE()


# Generated at 2022-06-14 17:30:32.269310
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    video_id = '366367'
    video_url = 'https://tvplay.tv3.lt/aferistai-10047125/'
    TVPlayHomeIE().suitable(video_url)
    TVPlayHomeIE()._real_extract(video_url)
    TVPlayHomeIE()._real_extract(video_url.replace(video_id, '10047125'))


# Generated at 2022-06-14 17:30:38.834700
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    IE = TVPlayHomeIE(None)
    assert isinstance(IE, TVPlayHomeIE)
    # Test if _VALID_URL can successfully extract the video id from url
    url = "https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/"
    m = IE._VALID_URL_RE.match(url)
    assert m.group('id') == '10280317'

# Generated at 2022-06-14 17:30:40.731348
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    try:
        ViafreeIE(1, 2, 3)
    except TypeError:
        pass
    else:
        assert False

# Generated at 2022-06-14 17:30:47.762021
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    TVPlayIE('http://www.tv3play.lv/parraides/vinas-melo-labak/418113?autostart=true')
    TVPlayIE('http://www.tv3play.ee/sisu/kodu-keset-linna/238551?autostart=true')
    TVPlayIE('http://www.tv3play.tv/sisu/kodu-keset-linna/238551?autostart=true')
    TVPlayIE('http://www.tv3play.se/program/husraddarna/395385?autostart=true')
    TVPlayIE('http://tv3play.tv3.ee/sisu/kodu-keset-linna/238551?autostart=true')

# Generated at 2022-06-14 17:30:49.264756
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    """Test the constructor of class TVPlayIE"""
    TVPlayIE()

# Generated at 2022-06-14 17:30:53.304419
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    if not TVPlayIE.suitable('mtg:757786'):
        raise AssertionError('ViafreeIE should be suitable if TVPlayIE is suitable')

# Generated at 2022-06-14 17:32:13.467228
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    t = TVPlayIE()
    assert t.ie_name() == 'mtg'
    assert t.ie_key() == 'mtg'
    assert t.get_info(
        'http://www.tv3play.ee/sisu/kodu-keset-linna/238551?autostart=true')



# Generated at 2022-06-14 17:32:20.600748
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    url = 'https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/'
    assert TVPlayHomeIE._VALID_URL == re.compile(r'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)').pattern
    assert re.match(TVPlayHomeIE._VALID_URL, url)
    url = 'https://play.tv3.lt/aferistai-10047125'
    assert re.match(TVPlayHomeIE._VALID_URL, url)

# Generated at 2022-06-14 17:32:25.515935
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert ie.suitable('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/') is True
    assert ie.suitable('https://tvplay.tv3.lt/aferistai-10047125') is True
    assert ie.suitable('https://tv3play.skaties.lv/vinas-melo-labak-10280317') is True
    assert ie.suitable('https://play.tv3.ee/cool-d-ga-mehhikosse-10044354') is True
    assert ie.suitable('https://play.tvplay.ee/cool-d-ga-mehhikosse-10044354') is False

# Generated at 2022-06-14 17:32:37.209893
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    from mpy_ipynb_playground_test import write_test_json, get_test_json
    from mpy_ipynb_playground_test import test_class_instance, test_no_class_instance
    from mpy_ipynb_playground_test import get_test_urls, get_test_ids, get_test_libs, get_test_cases
    # e.g. url = ['http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1', 'http://www.viafree.se/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-2', 'http://www.viafree.se/program/reality/sommaren-med-youtube

# Generated at 2022-06-14 17:32:39.608523
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    try:
        new_ie = TVPlayIE('')
    except TypeError:
        pass
    else:
        assert(new_ie is None)



# Generated at 2022-06-14 17:32:40.681261
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ViafreeIE('es', 'se')

# Generated at 2022-06-14 17:32:43.522029
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    TVPlayHomeIE(TVPlayHomeIE.ie_key());



# Generated at 2022-06-14 17:32:44.868310
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    # Check that constructor doesn't raise any exception
    TVPlayHomeIE()

# Generated at 2022-06-14 17:32:46.246236
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    temp = ViafreeIE()
    assert temp.country == None


# Generated at 2022-06-14 17:32:50.609480
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    # This code returns an instance of TVPlayIE,
    # with the url as "http://www.tv3play.no/programmer/anna-anka-soker-assistent/230898?autostart=true"
    ie = TVPlayIE()



# Generated at 2022-06-14 17:36:14.357741
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2022-06-14 17:36:21.541138
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    vid = TVPlayIE()._real_extract('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert(vid['id'] == '418113')
    assert(len(vid['formats']) == 2)

# Generated at 2022-06-14 17:36:26.270478
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    tvplayIE = TVPlayIE(None)
    assert tvplayIE.IE_NAME == 'mtg'
    assert tvplayIE.IE_DESC == 'MTG services'

# Generated at 2022-06-14 17:36:29.087571
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    assert(ViafreeIE.suitable('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1') )

# Generated at 2022-06-14 17:36:34.685580
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    """ Unit test for constructor of class TVPlayHomeIE """
    url = "https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/"
    TVPlayHomeIE(params={'test': 'test'})
    TVPlayHomeIE()
    # This is the right call, the constructor will call the right method in InfoExtractor
    TVPlayHomeIE(url)
    return 0


# Generated at 2022-06-14 17:36:40.292510
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    t = TVPlayIE()
    assert t._VALID_URL is TVPlayIE._VALID_URL
    assert t._TESTS is TVPlayIE._TESTS
    assert t.IE_NAME is TVPlayIE.IE_NAME
    assert t.IE_DESC is TVPlayIE.IE_DESC

# Generated at 2022-06-14 17:36:41.362893
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()



# Generated at 2022-06-14 17:36:51.002447
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    instance = TVPlayIE()
    assert hasattr(instance, '_VALID_URL'), 'No _VALID_URL in TVPlayIE'
    assert re.match(instance._VALID_URL, 'http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true'), 'Bad _VALID_URL'
    assert type(instance.IE_NAME) == str, 'Bad IE_NAME'
    assert type(instance.IE_DESC) == str, 'Bad IE_DESC'
    assert 'timestamp' in instance._TESTS[0]['info_dict'], 'Bad info_dict'

if __name__ == '__main__':
    test_TVPlayIE()

# Generated at 2022-06-14 17:36:57.942594
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    class_cstr_params = inspect.getargspec(ViafreeIE.__init__)
    assert len(class_cstr_params.args) == 2
    assert class_cstr_params.args[0] == 'name'
    assert class_cstr_params.args[1] == 'ie'
    assert class_cstr_params.varargs is None
    assert class_cstr_params.keywords is None
    assert class_cstr_params.defaults is None