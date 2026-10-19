

# Generated at 2022-06-14 17:27:21.679545
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE("")
    # print ie.extract('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/')
    assert ie.suitable(
        'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/') == True


# Generated at 2022-06-14 17:27:32.154744
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()
    assert ie.suitable('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/')
    assert ie.suitable('https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/')
    assert ie.suitable('https://tvplay.tv3.ee/cool-d-ga-mehhikosse/cool-d-ga-mehhikosse-10044354/')
    assert ie.suitable('https://play.tv3.lt/aferistai-10047125')
    assert ie.suitable('https://tv3play.skaties.lv/vinas-melo-labak-10280317')

# Generated at 2022-06-14 17:27:36.031604
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    assert ViafreeIE(ViafreeIE.ie_key()).ie_key() == ViafreeIE.ie_key()


# Generated at 2022-06-14 17:27:47.131297
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    assert ViafreeIE.suitable("http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1")
    assert ViafreeIE.suitable("http://www.viafree.se/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-1")
    assert ViafreeIE.suitable("http://www.viafree.se/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-2")
    assert ViafreeIE.suitable("http://www.viafree.se/program/livsstil/husraddarna/sasong-2/avsnitt-2")

# Generated at 2022-06-14 17:27:59.245784
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    # Test for parsing correct URL
    correct_url_test = 'http://www.tv3play.se/program/husraddarna/395385?autostart=true'
    info_dict = {
    'id': '395385',
    'ext': 'mp4',
    'title': 'Husräddarna S02E07',
    'description': 'md5:f210c6c89f42d4fc39faa551be813777',
    'duration': 2574,
    'timestamp': 1400596321,
    'upload_date': '20140520',
    }
    tvplay = TVPlayIE()
    result = tvplay._real_extract(correct_url_test)
    assert(result['id'] == info_dict['id'])

# Generated at 2022-06-14 17:28:00.736866
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    extractor = ViafreeIE()
    assert extractor is not None


# Generated at 2022-06-14 17:28:11.258617
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    assert not ViafreeIE.suitable(TVPlayIE._VALID_URL)
    assert ViafreeIE.suitable(ViafreeIE._VALID_URL)
    assert not ViafreeIE.suitable('http://tv3play.tv3.ee/sisu/kodu-keset-linna/238551?autostart=true')
    assert ViafreeIE.suitable('http://www.viafree.se/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-1')
    assert ViafreeIE.suitable('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')

# Generated at 2022-06-14 17:28:13.829028
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE("https://tvplay.skaties.lv/parraides/tv3-zinas/760183/")
    assert ie is not None


# Generated at 2022-06-14 17:28:18.855518
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    for embed in [
        'mtgplayer',
        'tv3play',
    ]:
        try:
            __import__('.'.join(('jwplatform', embed, 'extractor')), globals(), locals(), ['*'])
        except ImportError:
            continue
        assert ViafreeIE.suitable(embed + ':url')

# Generated at 2022-06-14 17:28:20.692053
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    try:
        ViafreeIE()
        assert True
    except:
        assert False


# Generated at 2022-06-14 17:28:53.498662
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    TVPlayIE()

# Generated at 2022-06-14 17:28:59.050638
# Unit test for constructor of class TVPlayIE

# Generated at 2022-06-14 17:29:07.927927
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert ie._VALID_URL == r'''(?x)
                    https?://
                        (?:www\.)?
                        viafree\.(?P<country>dk|no|se)
                        /(?P<id>program(?:mer)?/(?:[^/]+/)+[^/?#&]+)
                    '''
    assert ie._GEO_BYPASS == False
    assert ie.IE_NAME == 'TVPlay'

# Generated at 2022-06-14 17:29:13.194166
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    test_urls = [
        ('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1',
         ViafreeIE),
    ]
    for url, ie in test_urls:
        assert isinstance(ViafreeIE.suitable(url), bool)

# Generated at 2022-06-14 17:29:14.895735
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    viafree_ie = ViafreeIE('http://tvplay.skaties.lv/parraides/tv3-zinas/760183')
    assert viafree_ie.name == 'viafree'

# Generated at 2022-06-14 17:29:26.065121
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

# Generated at 2022-06-14 17:29:30.450314
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    _GLOBAL_SESSION = requests.Session()
    ua = 'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'
    _GLOBAL_SESSION.headers.update({"User-Agent": ua})

    ie = ViafreeIE()
    ie.set_downloader(_GLOBAL_SESSION)
    ie.set_options(ie.default_options)

    assert(ie._VALID_URL == 'https?://(?:www\\.)?viafree\\.(dk|no|se)/(program(?:mer)?/(?:[^/]+/)+[^/?#&]+)')

# Generated at 2022-06-14 17:29:31.924312
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'

# Generated at 2022-06-14 17:29:33.853468
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    TVPlayHomeIE('https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/')


# Generated at 2022-06-14 17:29:34.372986
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    TVPlayHomeIE()

# Generated at 2022-06-14 17:30:46.130805
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    viafree_ie = ViafreeIE()
    url = "http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1"
    country, path = re.match(viafree_ie._VALID_URL, url).groups()
    content = viafree_ie._download_json(
        'https://viafree-content.mtg-api.com/viafree-content/v1/%s/path/%s' % (country, path), path)
    program = content['_embedded']['viafreeBlocks'][0]['_embedded']['program']
    guid = program['guid']
    meta = content['meta']
    title = meta['title']


# Generated at 2022-06-14 17:30:48.619141
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    assert TVPlayIE.IE_NAME == 'mtg'
    assert TVPlayIE.IE_DESC == 'MTG services'


# Generated at 2022-06-14 17:30:53.060985
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    """
    Trivial unit test for constructor of class TVPlayHomeIE.
    """
    tvplayhome = TVPlayHomeIE()
    assert isinstance(tvplayhome, TVPlayHomeIE)


# Generated at 2022-06-14 17:30:56.763858
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE('whatever')
    # ie.ie_key is not None
    assert(ie.ie_key is not None)
    # ie.ie_key is not an empty string
    assert(ie.ie_key != '')


# Generated at 2022-06-14 17:31:00.475097
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    """
    Tests constructor of class TVPlayIE
    """
    ie = TVPlayIE()
    ie._initialize_geo_bypass()
    assert ie._GEO_BYPASS == False

    ie = TVPlayIE()
    ie._initialize_geo_bypass()
    assert ie._GEO_BYPASS == True



# Generated at 2022-06-14 17:31:05.952476
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    """test to see if TVPlayHomeIE works"""
    regex_test = TVPlayHomeIE()
    assert regex_test._VALID_URL == r'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'



# Generated at 2022-06-14 17:31:10.729065
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    URL = 'https://tvplay.skaties.lv/vinas-melo-labak/418113/?autostart=true'
    tvplay = TVPlayIE()
    tvplay.download(URL)


# Generated at 2022-06-14 17:31:23.484736
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    assert (TVPlayHomeIE.suitable('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/'))
    assert (not TVPlayHomeIE.suitable('https://tvplay.tv3.lt/'))
    assert (not TVPlayHomeIE.suitable('https://tvplay.tv3.lt/aferistai-n-7/10047125/'))
    assert (not TVPlayHomeIE.suitable('https://tvplay.tv3.lt/aferistai-n-7/10047125'))
    assert (not TVPlayHomeIE.suitable('https://play.tv3.lt/aferistai-10047125'))

# Generated at 2022-06-14 17:31:26.691917
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    tvplay_ie = TVPlayIE()
    assert TVPlayIE.IE_NAME == 'mtg'
    assert TVPlayIE.IE_DESC == 'MTG services'


# Generated at 2022-06-14 17:31:30.222899
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    TVPlayIE(None, 'https://play.tv3.lt/programos/moterys-meluoja-geriau/409229?autostart=true')


# Generated at 2022-06-14 17:32:56.060029
# Unit test for constructor of class TVPlayIE

# Generated at 2022-06-14 17:33:00.003036
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    url = 'https://viafree-content.mtg-api.com/viafree-content/v1/dk/path/programmer/novelle-film/sommer-i-tyrol'
    content = download_webpage(url, None)
    info = json.loads(content)
    ViafreeIE._real_extract('http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5', info)

# Generated at 2022-06-14 17:33:04.956704
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    infoExtractor = TVPlayHomeIE()
    infoExtractor.extract(
        'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/') == {
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

# Generated at 2022-06-14 17:33:08.282494
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    """Test the constructor of class TVPlayHomeIE"""
    TVPlayHomeIE(TVPlayIE(), 'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/')
    raise ExtractorError('Test failed!')

# Generated at 2022-06-14 17:33:09.004753
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    pass

# Generated at 2022-06-14 17:33:10.351038
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()
    assert isinstance(ie, InfoExtractor)

# Generated at 2022-06-14 17:33:18.598684
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE('https://play.tv3.lt/aferistai-10047125')
    # This method shouldn't be called
    ie._download_webpage('https://play.tv3.lt/aferistai-10047125', 'VIDEO_ID', 'Downloading webpage')
    # Unit test for constructor from parent class InfoExtractor should pass
    ie = InfoExtractor('https://play.tv3.lt/aferistai-10047125')
    # And this method shouldn't be called
    ie._real_extract('https://play.tv3.lt/aferistai-10047125')



# Generated at 2022-06-14 17:33:26.504373
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    assert ViafreeIE.suitable('https://www.viafree.no/programmer/reality/paradise-hotel/sesong-7/episode-5') == True
    assert ViafreeIE.suitable('https://play.tv3.lt/programa/18-savaites/s01e180-laidos-atgarsis') == False
    assert ViafreeIE.suitable('http://www.priaidahomeloader.com/') == False
    assert ViafreeIE.suitable('http://tv.nrk.no/serie/stormen/dhms33000615/01-03-2015') == False

# Generated at 2022-06-14 17:33:30.011933
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    viafreeIE = ViafreeIE()
    assert isinstance(viafreeIE, ViafreeIE)

# Generated at 2022-06-14 17:33:31.183374
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ViafreeIE([''])

# Generated at 2022-06-14 17:36:54.747596
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    from .raiplay import RaiPlayIE
    from .rai import RaiIE
    from .svt import SVTPlayIE
    from .drtv import DRTVIE
    from .rtvnh import RTVNHIE
    from .rtvslovakia import RTVSlovakiaIE
    from .tvn import TVNIE
    from .tvp import TVPIE

    assert TVPlayHomeIE.__bases__[0] == TVPlayIE

    tvplay_home_ie = TVPlayHomeIE()

    assert tvplay_home_ie.ie_key() == 'tvplayhome'

    assert tvplay_home_ie.ie_short_name() == 'TVPlayHome'
