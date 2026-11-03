

# Generated at 2026-11-02 22:11:32.855103
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    """Unit test for constructor of class ViafreeIE."""
    # Instantiate the extractor (InfoExtractor.__init__ accepts an optional downloader)
    ie = ViafreeIE()
    assert ie is not None

    # Basic identity checks
    assert ie.ie_key() == 'Viafree'
    assert ie.IE_DESC is not None or True

    # Geo bypass is explicitly disabled for this extractor
    assert ie._GEO_BYPASS is False

    # suitable() must accept viafree URLs
    assert ie.suitable(
        'http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert ie.suitable(
        'http://www.viafree.se/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-1')
    assert ie.suitable(
        'http://www.viafree.dk/programmer/reality/paradise-hotel/saeson-7/episode-5')

    # suitable() must reject URLs handled by TVPlayIE (including mtg: scheme)
    assert not ie.suitable(
        'http://www.tv3play.se/program/husraddarna/395385?autostart=true')
    assert not ie.suitable('mtg:418113')

    # suitable() must reject completely unrelated URLs
    assert not ie.suitable('https://www.youtube.com/watch?v=BaW_jenozKc')

    # _VALID_URL should capture country and path groups correctly
    m = ie._match_valid_url(
        'http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1')
    assert m is not None
    assert m.group('country') == 'no'
    assert m.group('id') == 'programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'

# Generated at 2026-11-02 22:13:48.330269
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    # Constructor should create a valid instance without errors
    ie = TVPlayHomeIE()
    assert ie is not None
    assert isinstance(ie, TVPlayHomeIE)

    # suitable() should accept URLs matching _VALID_URL
    assert TVPlayHomeIE.suitable('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/')
    assert TVPlayHomeIE.suitable('https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/')
    assert TVPlayHomeIE.suitable('https://tvplay.tv3.ee/cool-d-ga-mehhikosse/cool-d-ga-mehhikosse-10044354/')
    assert TVPlayHomeIE.suitable('https://play.tv3.lt/aferistai-10047125')
    assert TVPlayHomeIE.suitable('https://tv3play.skaties.lv/vinas-melo-labak-10280317')
    assert TVPlayHomeIE.suitable('https://play.tv3.ee/cool-d-ga-mehhikosse-10044354')

    # suitable() should reject URLs not matching _VALID_URL
    assert not TVPlayHomeIE.suitable('https://www.youtube.com/watch?v=BaW_jenozKc')
    assert not TVPlayHomeIE.suitable('https://tvplay.tv3.lt/program-without-id/')
    assert not TVPlayHomeIE.suitable('https://example.com/aferistai-10047125')

    # _match_id should extract the numeric id from valid URLs
    assert ie._match_id('https://play.tv3.lt/aferistai-10047125') == '10047125'
    assert ie._match_id('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/') == '10047125'
    assert ie._match_id('https://tv3play.skaties.lv/vinas-melo-labak-10280317') == '10280317'

# Generated at 2026-11-02 22:15:52.445187
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    '''Test class ViafreeIE constructor'''
    ie = ViafreeIE()
    assert isinstance(ie, ViafreeIE)
    assert isinstance(ie, InfoExtractor)

# Generated at 2026-11-02 22:18:20.923542
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    extractor = TVPlayHomeIE()

    # Constructor should initialize with default downloader (None)
    assert extractor._downloader is None

    # VALID_URL pattern should be defined
    assert extractor._VALID_URL is not None

    # IE_NAME should fall back to class name
    assert extractor.IE_NAME == 'TVPlayHome'

    # suitable() should accept valid URLs
    assert extractor.suitable('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/')
    assert extractor.suitable('https://play.tv3.lt/aferistai-10047125')
    assert extractor.suitable('https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/')
    assert extractor.suitable('https://tv3play.skaties.lv/vinas-melo-labak-10280317')
    assert extractor.suitable('https://play.tv3.ee/cool-d-ga-mehhikosse-10044354')
    assert extractor.suitable('https://tv3play.tv3.ee/cool-d-ga-mehhikosse-10044354')

    # suitable() should reject unrelated URLs
    assert not extractor.suitable('https://www.youtube.com/watch?v=BaW_jenozKc')
    assert not extractor.suitable('https://tvplay.tv3.lt/')

    # _match_id should extract the numeric id correctly
    assert extractor._match_id('https://tvplay.tv3.lt/aferistai-n-7/aferistai-10047125/') == '10047125'
    assert extractor._match_id('https://play.tv3.lt/aferistai-10047125') == '10047125'
    assert extractor._match_id('https://tvplay.skaties.lv/vinas-melo-labak/vinas-melo-labak-10280317/') == '10280317'
    assert extractor._match_id('https://play.tv3.ee/cool-d-ga-mehhikosse-10044354') == '10044354'