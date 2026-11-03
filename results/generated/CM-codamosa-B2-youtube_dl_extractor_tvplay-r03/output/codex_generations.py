

# Generated at 2026-11-03 04:09:25.710232
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    from yt_dlp.extractor.generic import InfoExtractor

    ie = TVPlayHomeIE()

    # Instance should be created and be an InfoExtractor
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, TVPlayHomeIE)

    # The downloader should be unset by default
    assert ie._downloader is None

    # The _VALID_URL pattern should be correctly defined
    assert ie._VALID_URL == r'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'

    # suitable() should work based on the constructed state
    assert ie.suitable('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/')
    assert ie.suitable('https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/')
    assert ie.suitable('https://play.tv3.lt/aferistai-10047125')
    assert ie.suitable('https://tv3play.skaties.lv/vinas-melo-labak-10280317')
    assert ie.suitable('https://play.tv3.ee/cool-d-ga-mehhikosse-10044354')

    # Non-matching URLs should not be suitable
    assert not ie.suitable('https://example.com/some-video-12345')
    assert not ie.suitable('https://tvplay.tv3.lt/aferistai-n-7/aferistai/')

    # _match_id should extract the trailing numeric id
    assert ie._match_id('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/') == '10047125'
    assert ie._match_id('https://play.tv3.ee/cool-d-ga-mehhikosse-10044354') == '10044354'

# Generated at 2026-11-03 04:11:42.417482
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    # Class attributes set in constructor / class definition
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'
    assert ie.ie_key() == 'mtg'
    assert ie._VALID_URL is not None

    # URLs that should match, together with expected extracted ids
    matching_urls = {
        'http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true': '418113',
        'http://play.tv3.lt/programos/moterys-meluoja-geriau/409229?autostart=true': '409229',
        'http://www.tv3play.ee/sisu/kodu-keset-linna/238551?autostart=true': '238551',
        'http://www.tv3play.se/program/husraddarna/395385?autostart=true': '395385',
        'http://www.tv6play.se/program/den-sista-dokusapan/266636?autostart=true': '266636',
        'http://www.tv8play.se/program/antikjakten/282756?autostart=true': '282756',
        'http://www.tv3play.no/programmer/anna-anka-soker-assistent/230898?autostart=true': '230898',
        'http://www.viasat4play.no/programmer/budbringerne/21873?autostart=true': '21873',
        'http://www.tv6play.no/programmer/hotelinspektor-alex-polizzi/361883?autostart=true': '361883',
        'http://play.novatv.bg/programi/zdravei-bulgariya/624952?autostart=true': '624952',
        'https://play.nova.bg/programi/zdravei-bulgariya/764300?autostart=true': '764300',
        'http://tvplay.skaties.lv/parraides/vinas-melo-labak/418113?autostart=true': '418113',
        'https://tvplay.skaties.lv/vinas-melo-labak/418113/?autostart=true': '418113',
        'http://tvplay.skaties.lv/parraides/tv3-zinas/760183': '760183',
        'http://tv3play.tv3.ee/sisu/kodu-keset-linna/238551?autostart=true': '238551',
        'http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869': '676869',
        'mtg:418113': '418113',
    }
    for url, expected_id in matching_urls.items():
        assert ie.suitable(url), 'URL should match: %s' % url
        assert ie._match_id(url) == expected_id, 'Wrong id for URL: %s' % url

    # URLs that should not match
    non_matching_urls = [
        'https://www.youtube.com/watch?v=BaW_jenozKc',
        'http://www.tvplay.lv/',
        'http://play.tv3.lt/programos/moterys-meluoja-geriau/',
        'mtg:',
        'mtg:abc',
    ]
    for url in non_matching_urls:
        assert not ie.suitable(url), 'URL should not match: %s' % url

# Generated at 2026-11-03 04:12:50.003339
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    # Constructor should instantiate without arguments
    ie = TVPlayHomeIE()

    # _VALID_URL should be set to the expected pattern
    assert ie._VALID_URL == r'https?://(?:tv3?)?play\.(?:tv3\.lt|skaties\.lv|tv3\.ee)/(?:[^/]+/)*[^/?#&]+-(?P<id>\d+)'

    # suitable() should accept valid URLs from all supported domains
    assert TVPlayHomeIE.suitable('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/')
    assert TVPlayHomeIE.suitable('https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/')
    assert TVPlayHomeIE.suitable('https://tvplay.tv3.ee/cool-d-ga-mehhikosse/cool-d-ga-mehhikosse-10044354/')
    assert TVPlayHomeIE.suitable('https://play.tv3.lt/aferistai-10047125')
    assert TVPlayHomeIE.suitable('https://tv3play.skaties.lv/vinas-melo-labak-10280317')
    assert TVPlayHomeIE.suitable('https://play.tv3.ee/cool-d-ga-mehhikosse-10044354')

    # suitable() should reject URLs from other sites
    assert not TVPlayHomeIE.suitable('http://www.tv6play.no/programmer/hotelinspektor-alex-polizzi/361883')
    assert not TVPlayHomeIE.suitable('https://viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')

    # _match_id should extract the trailing numeric id
    assert ie._match_id('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/') == '10047125'
    assert ie._match_id('https://play.tv3.ee/cool-d-ga-mehhikosse-10044354') == '10044354'
    assert ie._match_id('https://tv3play.skaties.lv/vinas-melo-labak-10280317') == '10280317'

# Generated at 2026-11-03 04:14:08.557261
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    # The extractor should be instantiated successfully
    assert ie is not None
    assert isinstance(ie, InfoExtractor)

    # Check basic metadata defined on the class
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'
    assert ie.ie_key() == 'mtg'
    assert ie._VALID_URL is not None
    assert isinstance(ie._TESTS, list) and len(ie._TESTS) > 0

    # suitable() should accept valid service URLs and the mtg: scheme
    assert ie.suitable('mtg:418113')
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert ie.suitable('http://play.tv3.lt/programos/moterys-meluoja-geriau/409229?autostart=true')
    assert ie.suitable('http://www.tv3play.ee/sisu/kodu-keset-linna/238551?autostart=true')
    assert ie.suitable('http://www.tv3play.se/program/husraddarna/395385?autostart=true')
    assert ie.suitable('http://www.tv6play.se/program/den-sista-dokusapan/266636?autostart=true')
    assert ie.suitable('http://www.tv8play.se/program/antikjakten/282756?autostart=true')
    assert ie.suitable('http://www.tv3play.no/programmer/anna-anka-soker-assistent/230898?autostart=true')
    assert ie.suitable('http://www.viasat4play.no/programmer/budbringerne/21873?autostart=true')
    assert ie.suitable('http://www.tv6play.no/programmer/hotelinspektor-alex-polizzi/361883?autostart=true')
    assert ie.suitable('http://play.novatv.bg/programi/zdravei-bulgariya/624952?autostart=true')
    assert ie.suitable('https://play.nova.bg/programi/zdravei-bulgariya/764300?autostart=true')
    assert ie.suitable('http://tvplay.skaties.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert ie.suitable('https://tvplay.skaties.lv/vinas-melo-labak/418113/?autostart=true')
    assert ie.suitable('http://tv3play.tv3.ee/sisu/kodu-keset-linna/238551?autostart=true')
    assert ie.suitable('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')

    # suitable() should reject unrelated URLs
    assert not ie.suitable('http://www.youtube.com/watch?v=BaW_jenozKc')
    assert not ie.suitable('http://www.tvplay.lv/')
    assert not ie.suitable('https://play.novatv.bg/programi/')

    # _match_id should extract the numeric video id
    assert ie._match_id('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true') == '418113'
    assert ie._match_id('http://play.tv3.lt/programos/moterys-meluoja-geriau/409229?autostart=true') == '409229'
    assert ie._match_id('mtg:418113') == '418113'
    assert ie._match_id('https://play.nova.bg/programi/zdravei-bulgariya/764300?autostart=true') == '764300'

# Generated at 2026-11-03 04:16:55.568785
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    # Verify the extractor can be instantiated without a downloader
    ie = TVPlayHomeIE()
    assert ie is not None
    assert ie.ie_key() == 'TVPlayHome'
    assert ie.IE_NAME == 'tvplayhome'

    # Verify suitable() accepts known valid URLs
    assert TVPlayHomeIE.suitable('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/')
    assert TVPlayHomeIE.suitable('https://play.tv3.lt/aferistai-10047125')
    assert TVPlayHomeIE.suitable('https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/')
    assert TVPlayHomeIE.suitable('https://tv3play.skaties.lv/vinas-melo-labak-10280317')
    assert TVPlayHomeIE.suitable('https://play.tv3.ee/cool-d-ga-mehhikosse-10044354')
    assert TVPlayHomeIE.suitable('https://tvplay.tv3.ee/cool-d-ga-mehhikosse/cool-d-ga-mehhikosse-10044354/')

    # Verify suitable() rejects non-matching URLs
    assert not TVPlayHomeIE.suitable('http://www.viafree.se/program/underhallning/i-like-radio-live/sasong-1/676869')
    assert not TVPlayHomeIE.suitable('mtg:418113')
    assert not TVPlayHomeIE.suitable('https://play.nova.bg/programi/zdravei-bulgariya/764300?autostart=true')

    # Verify the id capture group is extracted correctly
    m = re.match(TVPlayHomeIE._VALID_URL, 'https://play.tv3.lt/aferistai-10047125')
    assert m is not None
    assert m.group('id') == '10047125'

    m = re.match(TVPlayHomeIE._VALID_URL, 'https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/')
    assert m is not None
    assert m.group('id') == '10047125'

    m = re.match(TVPlayHomeIE._VALID_URL, 'https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/')
    assert m is not None
    assert m.group('id') == '10280317'

    m = re.match(TVPlayHomeIE._VALID_URL, 'https://play.tv3.ee/cool-d-ga-mehhikosse-10044354')
    assert m is not None
    assert m.group('id') == '10044354'

    # Verify URL without a trailing numeric id does not match
    assert re.match(TVPlayHomeIE._VALID_URL, 'https://play.tv3.lt/aferistai') is None