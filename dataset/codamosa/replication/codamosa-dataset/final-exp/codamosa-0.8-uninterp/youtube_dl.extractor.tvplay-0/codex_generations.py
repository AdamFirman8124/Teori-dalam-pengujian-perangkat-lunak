

# Generated at 2022-06-14 17:27:19.560535
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    assert not ViafreeIE.suitable(TVPlayIE._VALID_URL)
    assert TVPlayIE.suitable(TVPlayIE._VALID_URL)

# Generated at 2022-06-14 17:27:20.980302
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    a = TVPlayIE()
    return True


# Generated at 2022-06-14 17:27:31.570380
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    info = {
        'id': '366367',
        'ext': 'mp4',
        'title': 'Aferistai',
        'description': 'Aferistai. Kalėdinė pasaka.',
        'series': 'Aferistai [N-7]',
        'season': '1 sezonas',
        'season_number': 1,
        'duration': 464,
        'timestamp': 1394209658,
        'upload_date': '20140307',
        'age_limit': 18,
    }
    url = 'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/'
    ie = TVPlayHomeIE()
    assert ie.extractor(ie.suitable(url))(url).extract() == info




# Generated at 2022-06-14 17:27:35.880137
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    class_ = globals()['TVPlayIE']
    instance = class_()
    assert isinstance(instance, InfoExtractor)
    # test if the _VALID_URL matches the regex:
    # checks if the url is valid
    url = 'http://play.tv3play.lt/programos/moterys-meluoja-geriau/409229?autostart=true'
    assert re.match(instance._VALID_URL, url) is not None

# Generated at 2022-06-14 17:27:47.024622
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert ie.suitable("https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/")
    assert ie.suitable("https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/")
    assert ie.suitable("https://tvplay.tv3.ee/cool-d-ga-mehhikosse/cool-d-ga-mehhikosse-10044354/")
    assert ie.suitable("https://play.tv3.lt/aferistai-10047125")
    assert ie.suitable("https://tv3play.skaties.lv/vinas-melo-labak-10280317")

# Generated at 2022-06-14 17:27:54.456626
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    assert (TVPlayHomeIE()._VALID_URL ==
            'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\\d+)')

test_test_class_TVPlayHomeIE = type('test_test_class_TVPlayHomeIE', (unittest.TestCase,), {'test_TVPlayHomeIE': test_TVPlayHomeIE})



# Generated at 2022-06-14 17:27:57.747005
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    first_subclass = None
    for subclass in BaseIE.__subclasses__():
        if subclass.__name__ == ViafreeIE.__name__:
            if first_subclass is None:
                first_subclass = subclass
            else:
                return False
    return first_subclass.__name__ == ViafreeIE.__name__


# Generated at 2022-06-14 17:28:00.349491
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    TVPlayHomeIE(new=1)

# Generated at 2022-06-14 17:28:12.133510
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():

    ts_url = 'http://playapi.mtgx.tv/v3/videos/stream/418113'
    content = '{"streams":{"medium":"http://playertest.longtailvideo.com/adaptive/bipbop/gear4/prog_index.m3u8","hls":"http://playertest.longtailvideo.com/adaptive/bipbop/gear4/prog_index.m3u8","high":"http://playertest.longtailvideo.com/adaptive/bipbop/gear4/prog_index.m3u8"},"_links":{"self":{"href":"/v3/videos/stream/418113"}}}'

    ts_url2 = 'http://playapi.mtgx.tv/v3/videos/418113'

# Generated at 2022-06-14 17:28:16.111976
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    from .test_mtg import test_url_results
    results = test_url_results(ViafreeIE)
    for result in results:
        print('%s: %s' % (result['url'], result['passed']))


# Generated at 2022-06-14 17:29:04.200266
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    instance = TVPlayHomeIE()
    assert isinstance(instance, TVPlayHomeIE)
    # Assert that the regex works for valid and invalid URLs

# Generated at 2022-06-14 17:29:07.484054
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    pass
    # print(TVPlayIE.__doc__)



# Generated at 2022-06-14 17:29:18.713237
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE('123')
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'

# Generated at 2022-06-14 17:29:20.630150
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2022-06-14 17:29:30.587922
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    """
    Run the constructor for ViareeIE.
    """
    ie = ViafreeIE("ViareeIE.test_ViafreeIE")
    assert ie.suitable("http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5")
    assert ie.suitable("http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1")
    assert ie.suitable("http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869")
    assert not ie.suitable("http://play.tv2.no/programmer/underholdning/pah/sesong-9/episode-7/")

# Generated at 2022-06-14 17:29:34.425412
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    viafree = ViafreeIE()
    assert not viafree.suitable('http://www.tv3play.se/program/husraddarna/395385?autostart=true')
    assert viafree.suitable('http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2')

# Generated at 2022-06-14 17:29:39.854416
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE('http://')
    assert isinstance(ie, TVPlayHomeIE)
    assert isinstance(ie, TVPlayIE)



# Generated at 2022-06-14 17:29:47.393392
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # package = '__main__'
    # class_name = 'ViafreeIE'
    # kwargs = {
    #     '_VALID_URL': r'^https?://(?:www\.)?tv3play\.no/(?:video|program)/(?:[^/]+/)*?(?P<id>[^/?#&]+)$',
    #     'ie_key': 'TV3PlayIE',
    # }
    # test_module = __import__(package)
    # class_ = getattr(test_module, class_name)
    # class_(**kwargs)
    from .test_ViafreeIE import test_ViafreeIE
    test_ViafreeIE()



# Generated at 2022-06-14 17:29:51.900795
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE('http://tv3play.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/')
    # when url contains dashes, url_result should be 'tv3play.skaties.lv'
    assert ie._VALID_URL == r'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'

# Generated at 2022-06-14 17:29:54.402788
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    from tests import parse_mock_args
    url = 'https://play.tv3.lt/aferistai-10047125'
    args = parse_mock_args(url)[0]
    assert TVPlayHomeIE(*args)._VALID_URL == TVPlayHomeIE._VALID_URL



# Generated at 2022-06-14 17:30:38.060542
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    def _assert_url(url, expected):
        tv_play = TVPlayIE()
        assert tv_play._VALID_URL == expected
        assert tv_play._match_id(url) == '418113'

    _assert_url('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true', r'https?://(?:www\.)?tvplay\.lv(?:/parraides)?/(?:[^/]+/)+\d+')
    _assert_url('https://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true', r'https?://(?:www\.)?tvplay\.lv(?:/parraides)?/(?:[^/]+/)+\d+')
    _

# Generated at 2022-06-14 17:30:42.821396
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    try:
        global ViafreeIE
        return
    except NameError:
        pass

    from .test_common import TestCase
    from .test_video_common import get_testcases
    from . import extractor

    class TestViafreeIE(TestCase, extractor.ExtractorTest):

        extractor = ViafreeIE
        testcases = get_testcases(extractor)

    ViafreeIE = TestViafreeIE



# Generated at 2022-06-14 17:30:46.598101
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    assert re.match(ViafreeIE._VALID_URL, 'http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2').groups() == ('se', 'program/livsstil/husraddarna/sasong-2/avsnitt-2')

# Generated at 2022-06-14 17:30:48.885594
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    t = TVPlayIE()
    assert t.IE_NAME == 'mtg'
    assert t.IE_DESC == 'MTG services'


# Generated at 2022-06-14 17:31:00.815318
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE
    url = "https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/"
    video_id = "10280317"
    m3u8_url = "https://vod-play.skaties.lv/public/video/smil/vinas_melo_labak_10280317.smil/playlist.m3u8"
    title = "Viņas mēlo labāk"

# Generated at 2022-06-14 17:31:01.876907
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    t = TVPlayIE()


# Generated at 2022-06-14 17:31:04.101318
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # ViafreeIE should not be used for TVPlayIE urls
    for url in TVPlayIE._TESTS:
        assert not ViafreeIE.suitable(url['url'])
    # TVPlayIE should not be used for ViafreeIE urls
    for url in ViafreeIE._TESTS:
        assert not TVPlayIE.suitable(url['url'])


# Generated at 2022-06-14 17:31:06.165966
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    try:
        ViafreeIE('test', 'http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    except ExtractorError as e:
        assert 'This content might not be available in your coun' in str(e)
        pass
    return True


# Generated at 2022-06-14 17:31:10.590325
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie_obj = ViafreeIE(None)
    assert isinstance(ie_obj, GenericIE)
    assert ie_obj.ie_key() == 'Viafree'



# Generated at 2022-06-14 17:31:12.248507
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()
    assert ie._VALID_URL == ie.VALID_URL


# Generated at 2022-06-14 17:32:44.401336
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    c = TVPlayIE()
    assert c.IE_NAME != None
    assert c.IE_DESC != None
    assert c._VALID_URL != None
    assert c._TESTS != None

# Generated at 2022-06-14 17:32:54.034405
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    tvplay_ie = TVPlayIE()

    assert tvplay_ie.IE_NAME == 'mtg'
    assert tvplay_ie.IE_DESC == 'MTG services'


# Generated at 2022-06-14 17:32:56.100953
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    c = TVPlayIE()
    c._real_extract('http://play.tv3play.lt/programos/moterys-meluoja-geriau/409229?autostart=true')


# Generated at 2022-06-14 17:33:05.857881
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    """
    Test instantiation of the class TVPlayIE
    """
    def test_constructor(video_id, geo_country = None):
        """
        Test constructor of class TVPlayIE
        """
        tv_play_ie = TVPlayIE(TVPlayIE.IE_NAME, TVPlayIE.IE_DESC)
        tv_play_ie._initialize_geo_bypass({'countries': [geo_country]})
        tv_play_ie.IE_NAME = TVPlayIE.IE_NAME
        tv_play_ie.IE_DESC = TVPlayIE.IE_DESC
        tv_play_ie.video_id = video_id

# Generated at 2022-06-14 17:33:06.920435
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    TVPlayIE()


# Generated at 2022-06-14 17:33:12.541314
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE(None)

    url = 'https://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5'
    program = 'reality/paradise-hotel/saeson-7/episode-5'

    assert ie.suitable(url)
    assert ie._VALID_URL in url
    assert ie._match_id(url) == program
    assert ie._match_id(None) == None



# Generated at 2022-06-14 17:33:17.554091
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    assert TVPlayHomeIE._VALID_URL == r'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'

# Generated at 2022-06-14 17:33:29.185580
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    import sys
    import unittest
    try:
        import youtube_dl.extractor.mtg
        import youtube_dl.extractor.tvplay
        import youtube_dl.extractor.viafree
    except ImportError:
        sys.exit()

    class TVPlayIE_TestCase(unittest.TestCase):
        def __init__(self, *args, **kwargs):
            super(TVPlayIE_TestCase, self).__init__(*args, **kwargs)
            self.ie = youtube_dl.extractor.mtg.TVPlayIE()

        def test_TVPlayIE_is_suitable(self):
            self.assertTrue(self.ie.suitable('http://www.tv3play.se/program/husraddarna/395385?autostart=true'))

# Generated at 2022-06-14 17:33:33.738501
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    """Unit test for constructor of class TVPlayHomeIE"""
    test_url = "https://tvplay.tv3.lt/aferistai-10047125/"
    expected_result = {
        'id': '366367',
        'ext': 'mp4',
        'title': 'Aferistai',
        'description': 'Aferistai. Kalėdinė pasaka.',
        'series': 'Aferistai [N-7]',
        'season': '1 sezonas',
        'season_number': 1,
        'duration': 464,
        'timestamp': 1394209658,
        'upload_date': '20140307',
        'age_limit': 18
    }
    class_ = TVPlayHomeIE

# Generated at 2022-06-14 17:33:44.937043
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    from .test_common import with_fake_resources
    from .test_youtube import fake_http_response
    from ..compat import StringIO

    response = StringIO(fake_http_response)
