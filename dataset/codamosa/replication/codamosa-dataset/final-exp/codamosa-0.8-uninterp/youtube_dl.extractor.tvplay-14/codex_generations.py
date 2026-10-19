

# Generated at 2022-06-14 17:27:29.051009
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():

    class TestTVPlayIE(TVPlayIE):

        def _download_json(self, url, video_id, note='Downloading JSON metadata'):
            pass

    test = TestTVPlayIE(None)


# Generated at 2022-06-14 17:27:31.792603
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    test = TVPlayIE()
    assert test.IE_NAME == 'mtg'
    assert test.IE_DESC == 'MTG services'



# Generated at 2022-06-14 17:27:34.625333
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()
    assert isinstance(ie, ViafreeIE)



# Generated at 2022-06-14 17:27:40.434655
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    print("constructor ViafreeIE")
    url = "https://www.viafree.dk"
    viafree_ie = ViafreeIE(url)

    # Test for viafree_ie.country
    if viafree_ie.country != "DK":
        raise TestFailed("constructor ViafreeIE failed")
    print("constructor ViafreeIE success")


# Generated at 2022-06-14 17:27:42.363687
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    assert TVPlayHomeIE()._VALID_URL == TVPlayHomeIE._VALID_URL



# Generated at 2022-06-14 17:27:46.229483
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    """
    Create class TVPlayIE and test if it is constructed correctly
    """
    test = TVPlayIE()
    assert test.ie_key() == 'mtg'
    assert test.ie_desc() == 'MTG services'

# Generated at 2022-06-14 17:27:47.922352
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    viafree = ViafreeIE()
    assert viafree is not None


# Generated at 2022-06-14 17:27:52.219636
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    t = TVPlayIE('url')
    assert set(t.GEO_COUNTRIES) == set([None])
    assert t._VALID_URL == TVPlayIE._VALID_URL



# Generated at 2022-06-14 17:27:59.418762
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    assert TVPlayHomeIE.suitable('https://tvplay.tv3.lt/aferistai-10047125/')
    assert TVPlayHomeIE.suitable('https://tvplay.skaties.lv/vinas-melo-labak-10280317')
    assert TVPlayHomeIE.suitable('https://tvplay.tv3.ee/cool-d-ga-mehhikosse-10044354')
    assert TVPlayHomeIE.suitable('https://play.tv3.lt/aferistai-10047125')
    assert TVPlayHomeIE.suitable('https://tv3play.skaties.lv/vinas-melo-labak-10280317')

# Generated at 2022-06-14 17:28:00.626907
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

# Generated at 2022-06-14 17:28:18.356486
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    TVPlayHomeIE()

# Generated at 2022-06-14 17:28:25.987479
# Unit test for constructor of class ViafreeIE

# Generated at 2022-06-14 17:28:30.161290
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert ie._name == 'Viafree'


# Generated at 2022-06-14 17:28:39.143139
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    obj = TVPlayIE()
    assert obj._VALID_URL == r'(?x)^(?:mtg:|https?://(?:www\.)?(?:tvplay(?:\.skaties)?\.lv(?:/parraides)?|(?:tv3play|play\.tv3)\.lt(?:/programos)?|tv3play(?:\.tv3)?\.ee/sisu|(?:tv(?:3|6|8|10)play|viafree)\.se/program|(?:(?:tv3play|viasat4play|tv6play|viafree)\.no|(?:tv3play|viafree)\.dk)/programmer|play\.nova(?:tv)?\.bg/programi)/(?:[^/]+/)+)[0-9]+$'

# Generated at 2022-06-14 17:28:43.126926
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    assert hasattr(ViafreeIE(), '_VALID_URL')
    assert hasattr(ViafreeIE(), '_TESTS')
    assert hasattr(ViafreeIE(), '_GEO_BYPASS')


# Generated at 2022-06-14 17:28:43.678551
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    TVPlayIE


# Generated at 2022-06-14 17:28:44.563526
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert ie is not None, "TVPlayHomeIE constructor failed."

# Generated at 2022-06-14 17:28:51.232859
# Unit test for constructor of class ViafreeIE

# Generated at 2022-06-14 17:28:56.135305
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()
    assert ie.IE_NAME == "mtg"
    assert ie.IE_DESC == "MTG services"
    assert ie._VALID_URL == "http://www.tv3play.se/program/husraddarna/395385"
    assert ie._TESTS[0]['url'] == "http://www.tvplay.lv/parraides/vinas-melo-labak/418113"
    assert ie._TESTS[0]['info_dict']['id'] == "418113"
    assert ie._TESTS[0]['info_dict']['ext'] == "mp4"
    assert ie._TESTS[0]['info_dict']['title'] == "Kādi ir īri? - Viņas melo labāk"


# Generated at 2022-06-14 17:29:03.219952
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    import json
    import responses
    from .fake_oembed import FakeOEmbed

    TVPlay = 'http://tvplay.skaties.lv'
    program = 'parraides/vinas-melo-labak'
    video_id = '418113'
    url = '%s/%s/%s?autostart=true' % (TVPlay, program, video_id)
    content_json = json.loads(FakeOEmbed.content_json(url))

    headers = {
        'Content-Type': content_json['type']
    }

    with responses.RequestsMock() as m:
        m.add(responses.GET, content_json['json_url'], status=200,
              adding_headers=headers)

# Generated at 2022-06-14 17:29:46.139334
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    from . import copy_to_clipboard as test_TVPlayHomeIE_copy_to_clipboard
    from . import print_json as test_TVPlayHomeIE_print_json
    from . import test_json as test_TVPlayHomeIE_test_json
    from . import test_info_dict as test_TVPlayHomeIE_test_info_dict

    test_TVPlayHomeIE_copy_to_clipboard(TVPlayHomeIE)
    test_TVPlayHomeIE_print_json(TVPlayHomeIE, end=-1)
    test_TVPlayHomeIE_test_json(TVPlayHomeIE)
    test_TVPlayHomeIE_test_info_dict(TVPlayHomeIE)

# Generated at 2022-06-14 17:29:50.292262
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    url = 'http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'
    info_extractor = ViafreeIE()
    info_extractor._real_initialize()
    info_extractor.suitable(url)
    info_extractor._real_extract(url)

if __name__ == '__main__':
    test_ViafreeIE()


# Generated at 2022-06-14 17:29:52.642370
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    IE = TVPlayHomeIE()
    assert IE.SUCCESS == "https://tvplay.tv3.ee/vinas-melo-labak-10184855/"
    assert IE.FAILURE == "https://tvplay.tv3.lt/tv1a/"


# Generated at 2022-06-14 17:29:57.365791
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    m = TVPlayIE('http://play.tv3.lt/programos/moterys-meluoja-geriau/409229?autostart=true', None)
    print(m)



# Generated at 2022-06-14 17:30:00.761036
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # Test creating an instance of the class
    test_ie = ViafreeIE(None)
    # This is the only inheritor class with a different name of _VALID_URL
    assert hasattr(test_ie, '_VALID_URL')



# Generated at 2022-06-14 17:30:06.410977
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    url = url_for('TVPlayHomeIE', 'https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/')
    ie = TVPlayHomeIE(url)
    assert ie.extractor_key() == 'TVPlayHomeIE'

# Generated at 2022-06-14 17:30:18.981851
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    from .test_html import fake_http_response_args
    from .extractor import extractor_factory
    from .common import compat_str
    from .compat import compat_urlparse

    def check_IE(ie_name, url, expected_result):
        extractor = extractor_factory(url)
        assert extractor is not None and isinstance(extractor, extractor_factory(ie_name))
        assert extractor.suitable(url) == expected_result

    TVPlay_Home_IE = extractor_factory('TVPlayHome')

    # test match cases
    assert TVPlay_Home_IE.suitable('https://tvplay.tv3.lt/aferistai-10047125')

# Generated at 2022-06-14 17:30:26.922070
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()
    # Matching
    assert ie._match_id('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true') == '418113'
    assert ie._match_id('http://play.tv3.lt/programos/moterys-meluoja-geriau/409229?autostart=true') == '409229'
    assert ie._match_id('http://www.tv3play.ee/sisu/kodu-keset-linna/238551?autostart=true') == '238551'
    assert ie._match_id('http://www.tv3play.se/program/husraddarna/395385?autostart=true') == '395385'

# Generated at 2022-06-14 17:30:28.416320
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert ie.__class__ == TVPlayHomeIE


# Generated at 2022-06-14 17:30:33.167028
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE('https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/')
    assert ie._VALID_URL == r'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'


# Generated at 2022-06-14 17:31:11.872707
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE("http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5")
    assert ie.__class__.__name__ == 'ViafreeIE', 'ViafreeIE could not be instantiated'

# Generated at 2022-06-14 17:31:24.694939
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    # Test if constructor is successful for url by skaties.lv
    TVPlayHomeIE('https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/')
    # Test if constructor is successful for url by tv3.ee
    TVPlayHomeIE('https://tvplay.tv3.ee/cool-d-ga-mehhikosse/cool-d-ga-mehhikosse-10044354/')
    # Test if constructor is successful for url by tv3.lt
    TVPlayHomeIE('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/')
    # Test if constructor is successful for url by play.tv3.lt

# Generated at 2022-06-14 17:31:32.740269
# Unit test for constructor of class ViafreeIE

# Generated at 2022-06-14 17:31:35.257790
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    # This should not fail even if the class is not implemented
    ie = TVPlayIE(None)
    assert ie.IE_NAME == 'mtg'


# Generated at 2022-06-14 17:31:41.912818
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE('https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/')
    assert ie.playlist_title == 'Vīnu, sveiku!'
    assert ie.playlist_index == '10280317'
    assert ie.playlist_id == '157166'

    ie = TVPlayHomeIE('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/')
    assert ie.playlist_title == 'Aferistai [N-7]'
    assert ie.playlist_index == '10047125'
    assert ie.playlist_id == '155675'


# Generated at 2022-06-14 17:31:43.567807
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    assert TVPlayIE.__name__ == 'TVPlayIE'

# Generated at 2022-06-14 17:31:46.132978
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE('test_TVPlayHomeIE')
    assert ie.__class__ == TVPlayHomeIE
    assert ie._VALID_URL == TVPlayHomeIE._VALID_URL


# Generated at 2022-06-14 17:31:57.911992
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    x = TVPlayHomeIE()
    x._match_id('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/') == '10047125'
    x._match_id('https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/') == '10280317'
    x._match_id('https://play.tv3.lt/aferistai-10047125') == '10047125'
    x._match_id('https://tv3play.skaties.lv/vinas-melo-labak-10280317') == '10280317'

# Generated at 2022-06-14 17:31:59.606305
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    TVPlayHomeIE('https://tv3play.skaties.lv/vinas-melo-labak-10280317')

# Generated at 2022-06-14 17:32:01.499760
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    IE = TVPlayHomeIE(None)
    assert len(IE._TESTS) > 0


# Generated at 2022-06-14 17:33:00.847243
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    tvplay = TVPlayIE()
    assert tvplay.IE_NAME == 'mtg'
    assert tvplay.IE_DESC == 'MTG services'

# Generated at 2022-06-14 17:33:12.837819
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    IE = TVPlayIE()
    x = IE
    assert x.IE_NAME == 'mtg'
    assert x.IE_DESC == 'MTG services'

# Generated at 2022-06-14 17:33:24.042801
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    assert_raises(RegexNotFoundError, TVPlayHomeIE._match_id, TVPlayHomeIE, 'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125')
    assert TVPlayHomeIE._match_id(TVPlayHomeIE, 'https://tv3play.tv3.lt/aferistai-10047125') == '10047125'
    assert TVPlayHomeIE._match_id(TVPlayHomeIE, 'https://play.tv3.lt/aferistai-10047125') == '10047125'

# Generated at 2022-06-14 17:33:31.030822
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    viafreeie = ViafreeIE()
    assert viafreeie.suitable('https://www.tv3play.se/program/husraddarna/395385?autostart=true') == False
    assert viafreeie.suitable('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')



# Generated at 2022-06-14 17:33:40.695019
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    viafree = ViafreeIE()
    tvplay = TVPlayIE()
    assert viafree.suitable('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5') == True
    assert viafree.suitable('http://tvplay.skaties.lv/parraides/vinas-melo-labak/418113?autostart=true') == False
    assert tvplay.suitable('http://tvplay.skaties.lv/parraides/vinas-melo-labak/418113?autostart=true') == True

# Generated at 2022-06-14 17:33:44.999449
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    try:
        TVPlayIE("https://tvplay.skaties.lv/parraides/vinas-melo-labak/418113?autostart=true")
    except Exception as e:
        print("Error: " + str(e))
        print("Test failed!")
        return False
    print("Test passed!")

    return True



# Generated at 2022-06-14 17:33:46.358072
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ViafreeIE()



# Generated at 2022-06-14 17:33:50.303500
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE('www.viafree.dk')
    assert ie.playlist_title is None, 'playlist_title should be None by default'


# Generated at 2022-06-14 17:33:59.932042
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    tvp_ie = TVPlayIE()

    tvp_ie.IE_NAME == 'mtg'
    tvp_ie.IE_DESC == 'MTG services'

# Generated at 2022-06-14 17:34:05.466367
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')
    assert ie._VALID_URL == r'''(?x)
                    https?://
                        (?:www\.)?
                        viafree\.(?P<country>dk|no|se)
                        /(?P<id>program(?:mer)?/(?:[^/]+/)+[^/?#&]+)
                    '''
    assert ie._geo_bypass is False
    assert ie.GEO_COUNTRIES == ['DK', 'NO', 'SE']
    assert ie.IE_NAME == 'Viafree'
    assert ie.IE_DESC == 'Viafree'


# Generated at 2022-06-14 17:36:18.681527
# Unit test for constructor of class TVPlayIE

# Generated at 2022-06-14 17:36:29.268501
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    tv_play = TVPlayIE()
    assert tv_play.IE_NAME == 'mtg'
    assert tv_play.IE_DESC == 'MTG services'

# Generated at 2022-06-14 17:36:37.638937
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert ie.get_host_and_id('https://tv3play.skaties.lv/vinas-melo-labak-10280317') == ('tv3play.skaties.lv', '10280317')
    assert ie.get_host_and_id('https://play.tv3.lt/aferistai-10047125') == ('play.tv3.lt', '10047125')
    assert ie.get_host_and_id('https://tvplay.tv3.ee/cool-d-ga-mehhikosse-10044354') == ('tvplay.tv3.ee', '10044354')

# Generated at 2022-06-14 17:36:39.745476
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    from .test_TVPlayIE import test_TVPlayIE
    test_TVPlayIE(TVPlayHomeIE())

# Generated at 2022-06-14 17:36:41.541712
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    # Multiple classes inherit TVPlayHomeIE
    assert TVPlayHomeIE.__name__ == 'TVPlayHomeIE'



# Generated at 2022-06-14 17:36:43.267442
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    # Test constructor of TVPlayHomeIE class
    TVPlayHomeIE(None)


# Generated at 2022-06-14 17:36:44.924581
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    _ = ViafreeIE('http://www.tv3play.se/program/husraddarna/395385?autostart=true')


# Generated at 2022-06-14 17:36:50.170325
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    # This is the path which extracted videos have
    assert TVPlayHomeIE._VALID_URL == r'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'

    # Check if it really is a regex
    assert re.match(TVPlayHomeIE._VALID_URL, "https://tvplay.tv3.ee/cool-d-ga-mehhikosse/cool-d-ga-mehhikosse-10044354/")

# Generated at 2022-06-14 17:36:53.298202
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert ie.country == 'no'



# Generated at 2022-06-14 17:37:02.592971
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    m = TVPlayIE()
    assert m.IE_NAME == m.ie_key()
    assert m.IE_DESC == m.ie_key()
    assert re.match(m._VALID_URL, 'http://play.tv3play.lt/programos/moterys-meluoja-geriau/409229?autostart=true', re.VERBOSE)
    assert not re.match(m._VALID_URL, 'http://play.tv3play.lt/programos/moterys-meluoja-geriau', re.VERBOSE)

