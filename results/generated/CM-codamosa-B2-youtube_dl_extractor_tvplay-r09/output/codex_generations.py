

# Generated at 2026-11-03 00:17:36.697303
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    # Instantiate the extractor
    ie = TVPlayHomeIE()
    assert ie is not None
    assert isinstance(ie, TVPlayHomeIE)
    assert ie.ie_key() == 'TVPlayHome'
    assert ie._VALID_URL == r'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+'

    # URL matching
    assert ie.suitable('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/')
    assert ie.suitable('https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/')
    assert ie.suitable('https://tvplay.tv3.ee/cool-d-ga-mehhikosse/cool-d-ga-mehhikosse-10044354/')
    assert ie.suitable('https://play.tv3.lt/aferistai-10047125')
    assert ie.suitable('https://tv3play.skaties.lv/vinas-melo-labak-10280317')
    assert ie.suitable('https://play.tv3.ee/cool-d-ga-mehhikosse-10044354')
    assert not ie.suitable('https://www.youtube.com/watch?v=BaW_jenozKc')
    assert not ie.suitable('https://tvplay.tv3.lt/')

    # ID extraction
    assert ie._match_id('https://play.tv3.lt/aferistai-10047125') == '10047125'
    assert ie._match_id('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/') == '10047125'
    assert ie._match_id('https://play.tv3.ee/cool-d-ga-mehhikosse-10044354') == '10044354'

    # Test metadata is defined
    assert isinstance(TVPlayHomeIE._TESTS, list)
    assert len(TVPlayHomeIE._TESTS) > 0
    assert 'url' in TVPlayHomeIE._TESTS[0]
    assert 'info_dict' in TVPlayHomeIE._TESTS[0]

# Generated at 2026-11-03 00:19:28.929984
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    # Basic attributes set by the constructor / class definition
    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'
    assert ie._VALID_URL is not None
    assert ie._WORKING is not False

    # Valid URLs (taken from _TESTS) must match and yield a numeric id
    valid_urls = [
        'http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true',
        'http://play.tv3.lt/programos/moterys-meluoja-geriau/409229?autostart=true',
        'http://www.tv3play.ee/sisu/kodu-keset-linna/238551?autostart=true',
        'http://www.tv3play.se/program/husraddarna/395385?autostart=true',
        'http://www.tv6play.se/program/den-sista-dokusapan/266636?autostart=true',
        'http://www.tv8play.se/program/antikjakten/282756?autostart=true',
        'http://www.tv3play.no/programmer/anna-anka-soker-assistent/230898?autostart=true',
        'http://www.viasat4play.no/programmer/budbringerne/21873?autostart=true',
        'http://www.tv6play.no/programmer/hotelinspektor-alex-polizzi/361883?autostart=true',
        'http://play.novatv.bg/programi/zdravei-bulgariya/624952?autostart=true',
        'https://play.nova.bg/programi/zdravei-bulgariya/764300?autostart=true',
        'http://tvplay.skaties.lv/parraides/vinas-melo-labak/418113?autostart=true',
        'https://tvplay.skaties.lv/vinas-melo-labak/418113/?autostart=true',
        'http://tvplay.skaties.lv/parraides/tv3-zinas/760183',
        'http://tv3play.tv3.ee/sisu/kodu-keset-linna/238551?autostart=true',
        'http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869',
        'mtg:418113',
    ]
    for url in valid_urls:
        assert ie.suitable(url), 'should match: %s' % url
        video_id = ie._match_id(url)
        assert video_id is not None and video_id.isdigit(), url

    # Spot-check specific id extraction
    assert ie._match_id('mtg:418113') == '418113'
    assert ie._match_id(
        'http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true') == '418113'
    assert ie._match_id(
        'https://play.nova.bg/programi/zdravei-bulgariya/764300?autostart=true') == '764300'

    # Invalid URLs must not match
    invalid_urls = [
        'https://www.youtube.com/watch?v=BaW_jenozKc',
        'http://www.tvplay.lv/',
        'http://www.tvplay.lv/parraides/vinas-melo-labak/notanumber',
        'mtg:',
        'mtg:abc',
    ]
    for url in invalid_urls:
        assert not ie.suitable(url), 'should not match: %s' % url

# Generated at 2026-11-03 00:21:33.136934
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    # Constructor should initialize the InfoExtractor properly
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'
    assert ie._VALID_URL is not None
    assert ie._downloader is None

    # URLs from _TESTS must match _VALID_URL and yield the correct id
    matching = [
        ('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true', '418113'),
        ('http://play.tv3.lt/programos/moterys-meluoja-geriau/409229?autostart=true', '409229'),
        ('http://www.tv3play.ee/sisu/kodu-keset-linna/238551?autostart=true', '238551'),
        ('http://www.tv3play.se/program/husraddarna/395385?autostart=true', '395385'),
        ('http://www.tv6play.se/program/den-sista-dokusapan/266636?autostart=true', '266636'),
        ('http://www.tv8play.se/program/antikjakten/282756?autostart=true', '282756'),
        ('http://www.tv3play.no/programmer/anna-anka-soker-assistent/230898?autostart=true', '230898'),
        ('http://www.viasat4play.no/programmer/budbringerne/21873?autostart=true', '21873'),
        ('http://www.tv6play.no/programmer/hotelinspektor-alex-polizzi/361883?autostart=true', '361883'),
        ('http://play.novatv.bg/programi/zdravei-bulgariya/624952?autostart=true', '624952'),
        ('https://play.nova.bg/programi/zdravei-bulgariya/764300?autostart=true', '764300'),
        ('http://tvplay.skaties.lv/parraides/vinas-melo-labak/418113?autostart=true', '418113'),
        ('https://tvplay.skaties.lv/vinas-melo-labak/418113/?autostart=true', '418113'),
        ('http://tv3play.tv3.ee/sisu/kodu-keset-linna/238551?autostart=true', '238551'),
        ('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869', '676869'),
        ('mtg:418113', '418113'),
    ]
    for url, video_id in matching:
        assert ie.suitable(url), 'should match: %s' % url
        assert ie._match_id(url) == video_id, 'bad id for: %s' % url

    # Invalid URLs must not match
    non_matching = [
        'http://www.tvplay.lv/parraides/vinas-melo-labak/',
        'http://play.novatv.bg/programi/zdravei-bulgariya/abc',
        'mtg:',
        'https://www.youtube.com/watch?v=aBcDeFgHiJk',
    ]
    for url in non_matching:
        assert not ie.suitable(url), 'should not match: %s' % url