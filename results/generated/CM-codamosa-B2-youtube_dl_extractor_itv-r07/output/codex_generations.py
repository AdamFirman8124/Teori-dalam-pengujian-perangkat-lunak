

# Generated at 2026-10-25 07:13:44.078953
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()

    # Constructor creates an instance of the correct class
    assert isinstance(ie, ITVBTCCIE)
    assert isinstance(ie, InfoExtractor)

    # Class-level attributes set on the constructor
    assert ie.ie_key() == 'ITVBTCC'
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie.suitable('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert not ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')

    # _match_id extracts the playlist id from a valid URL
    assert ie._match_id('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch') == \
        'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2026-10-25 07:14:02.099337
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:14:04.746247
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:14:07.499922
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:14:09.918524
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:14:12.617687
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:14:15.034828
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:14:17.448174
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:14:19.870249
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:14:22.289405
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:14:25.026916
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:14:27.444607
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:14:29.863197
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:14:32.279771
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:14:34.713312
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:14:37.129588
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:14:39.754325
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    """
    Unit test for the constructor of class ITVBTCCIE.

    Verifies that:
    - The extractor can be instantiated without arguments (inherited from InfoExtractor).
    - Core class attributes are correctly defined.
    - The _VALID_URL regex matches a known BTCC hub URL and extracts the playlist id.
    """
    # Instantiate the extractor (constructor requires no arguments)
    ie = ITVBTCCIE()

    # The instance should be an InfoExtractor
    assert isinstance(ie, InfoExtractor)

    # Class-level attributes must be present and non-empty
    assert ie.ie_key() == 'ITVBTCC'
    assert ie.IE_NAME == 'itv:btcc'
    assert ie._VALID_URL is not None

    # _WORKING should default to True (extractor marked as functional)
    assert ie._WORKING is True

    # The Brightcove URL template used by this extractor must be defined
    assert ie.BRIGHTCOVE_URL_TEMPLATE == (
        'http://players.brightcove.net/1582188683001/HkiHLnNRx_default/index.html?videoId=%s')

    # _VALID_URL must match the test URL and capture the playlist id
    test_url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    match = ie._match_valid_url(test_url)
    assert match is not None
    assert match.group('id') == 'btcc-2018-all-the-action-from-brands-hatch'

    # _match_id convenience wrapper should return the same captured id
    assert ie._match_id(test_url) == 'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2026-10-25 07:14:46.131532
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()

    # Valid URLs â should extract the correct video id
    assert ie._match_id('https://www.itv.com/hub/liar/2a4547a0012') == '2a4547a0012'
    assert ie._match_id('https://www.itv.com/hub/through-the-keyhole/2a2271a0033') == '2a2271a0033'
    assert ie._match_id('http://www.itv.com/hub/james-martins-saturday-morning/2a5159a0034') == '2a5159a0034'

    # Invalid URLs â should not match
    for url in (
        'https://www.itv.com/hub/liar/',            # missing id
        'https://www.itv.com/hub/2a4547a0012',      # missing title segment
        'https://www.example.com/hub/liar/2a4547a0012',  # wrong domain
        'https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch',  # ITVBTCC, not ITV
    ):
        assert ie.suitable(url) is False, url

# Generated at 2026-10-25 07:14:47.459756
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()

    # Constructor creates an instance of the correct class
    assert isinstance(ie, ITVBTCCIE)
    assert isinstance(ie, InfoExtractor)

    # Class-level attributes set on the constructor
    assert ie.ie_key() == 'ITVBTCC'
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie.suitable('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert not ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')

    # _match_id extracts the playlist id from a valid URL
    assert ie._match_id('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch') == \
        'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2026-10-25 07:14:48.895955
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()

    # Valid URLs â should extract the correct video id
    assert ie._match_id('https://www.itv.com/hub/liar/2a4547a0012') == '2a4547a0012'
    assert ie._match_id('https://www.itv.com/hub/through-the-keyhole/2a2271a0033') == '2a2271a0033'
    assert ie._match_id('http://www.itv.com/hub/james-martins-saturday-morning/2a5159a0034') == '2a5159a0034'

    # Invalid URLs â should not match
    for url in (
        'https://www.itv.com/hub/liar/',            # missing id
        'https://www.itv.com/hub/2a4547a0012',      # missing title segment
        'https://www.example.com/hub/liar/2a4547a0012',  # wrong domain
        'https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch',  # ITVBTCC, not ITV
    ):
        assert ie.suitable(url) is False, url

# Generated at 2026-10-25 07:14:50.331298
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()

    # Valid URLs â should extract the correct video id
    assert ie._match_id('https://www.itv.com/hub/liar/2a4547a0012') == '2a4547a0012'
    assert ie._match_id('https://www.itv.com/hub/through-the-keyhole/2a2271a0033') == '2a2271a0033'
    assert ie._match_id('http://www.itv.com/hub/james-martins-saturday-morning/2a5159a0034') == '2a5159a0034'

    # Invalid URLs â should not match
    for url in (
        'https://www.itv.com/hub/liar/',            # missing id
        'https://www.itv.com/hub/2a4547a0012',      # missing title segment
        'https://www.example.com/hub/liar/2a4547a0012',  # wrong domain
        'https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch',  # ITVBTCC, not ITV
    ):
        assert ie.suitable(url) is False, url

# Generated at 2026-10-25 07:14:51.770305
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()

    # Valid URLs â should extract the correct video id
    assert ie._match_id('https://www.itv.com/hub/liar/2a4547a0012') == '2a4547a0012'
    assert ie._match_id('https://www.itv.com/hub/through-the-keyhole/2a2271a0033') == '2a2271a0033'
    assert ie._match_id('http://www.itv.com/hub/james-martins-saturday-morning/2a5159a0034') == '2a5159a0034'

    # Invalid URLs â should not match
    for url in (
        'https://www.itv.com/hub/liar/',            # missing id
        'https://www.itv.com/hub/2a4547a0012',      # missing title segment
        'https://www.example.com/hub/liar/2a4547a0012',  # wrong domain
        'https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch',  # ITVBTCC, not ITV
    ):
        assert ie.suitable(url) is False, url

# Generated at 2026-10-25 07:14:53.102135
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()

    # Constructor creates an instance of the correct class
    assert isinstance(ie, ITVBTCCIE)
    assert isinstance(ie, InfoExtractor)

    # Class-level attributes set on the constructor
    assert ie.ie_key() == 'ITVBTCC'
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie.suitable('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert not ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')

    # _match_id extracts the playlist id from a valid URL
    assert ie._match_id('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch') == \
        'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2026-10-25 07:14:54.826141
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()

    # Valid URLs â should extract the correct video id
    assert ie._match_id('https://www.itv.com/hub/liar/2a4547a0012') == '2a4547a0012'
    assert ie._match_id('https://www.itv.com/hub/through-the-keyhole/2a2271a0033') == '2a2271a0033'
    assert ie._match_id('http://www.itv.com/hub/james-martins-saturday-morning/2a5159a0034') == '2a5159a0034'

    # Invalid URLs â should not match
    for url in (
        'https://www.itv.com/hub/liar/',            # missing id
        'https://www.itv.com/hub/2a4547a0012',      # missing title segment
        'https://www.example.com/hub/liar/2a4547a0012',  # wrong domain
        'https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch',  # ITVBTCC, not ITV
    ):
        assert ie.suitable(url) is False, url

# Generated at 2026-10-25 07:14:56.115233
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()

    # Constructor creates an instance of the correct class
    assert isinstance(ie, ITVBTCCIE)
    assert isinstance(ie, InfoExtractor)

    # Class-level attributes set on the constructor
    assert ie.ie_key() == 'ITVBTCC'
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie.suitable('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert not ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')

    # _match_id extracts the playlist id from a valid URL
    assert ie._match_id('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch') == \
        'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2026-10-25 07:14:57.600188
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()

    # Constructor creates an instance of the correct class
    assert isinstance(ie, ITVBTCCIE)
    assert isinstance(ie, InfoExtractor)

    # Class-level attributes set on the constructor
    assert ie.ie_key() == 'ITVBTCC'
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie.suitable('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert not ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')

    # _match_id extracts the playlist id from a valid URL
    assert ie._match_id('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch') == \
        'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2026-10-25 07:14:59.137168
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()

    # Constructor creates an instance of the correct class
    assert isinstance(ie, ITVBTCCIE)
    assert isinstance(ie, InfoExtractor)

    # Class-level attributes set on the constructor
    assert ie.ie_key() == 'ITVBTCC'
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie.suitable('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert not ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')

    # _match_id extracts the playlist id from a valid URL
    assert ie._match_id('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch') == \
        'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2026-10-25 07:15:00.569270
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()

    # Constructor creates an instance of the correct class
    assert isinstance(ie, ITVBTCCIE)
    assert isinstance(ie, InfoExtractor)

    # Class-level attributes set on the constructor
    assert ie.ie_key() == 'ITVBTCC'
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie.suitable('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert not ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')

    # _match_id extracts the playlist id from a valid URL
    assert ie._match_id('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch') == \
        'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2026-10-25 07:15:02.003546
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()

    # Constructor creates an instance of the correct class
    assert isinstance(ie, ITVBTCCIE)
    assert isinstance(ie, InfoExtractor)

    # Class-level attributes set on the constructor
    assert ie.ie_key() == 'ITVBTCC'
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie.suitable('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert not ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')

    # _match_id extracts the playlist id from a valid URL
    assert ie._match_id('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch') == \
        'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2026-10-25 07:15:03.440920
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()

    # Constructor creates an instance of the correct class
    assert isinstance(ie, ITVBTCCIE)
    assert isinstance(ie, InfoExtractor)

    # Class-level attributes set on the constructor
    assert ie.ie_key() == 'ITVBTCC'
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie.suitable('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert not ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')

    # _match_id extracts the playlist id from a valid URL
    assert ie._match_id('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch') == \
        'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2026-10-25 07:15:04.937664
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()

    # Constructor creates an instance of the correct class
    assert isinstance(ie, ITVBTCCIE)
    assert isinstance(ie, InfoExtractor)

    # Class-level attributes set on the constructor
    assert ie.ie_key() == 'ITVBTCC'
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie.suitable('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert not ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')

    # _match_id extracts the playlist id from a valid URL
    assert ie._match_id('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch') == \
        'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2026-10-25 07:15:06.304640
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()

    # Constructor creates an instance of the correct class
    assert isinstance(ie, ITVBTCCIE)
    assert isinstance(ie, InfoExtractor)

    # Class-level attributes set on the constructor
    assert ie.ie_key() == 'ITVBTCC'
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie.suitable('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert not ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')

    # _match_id extracts the playlist id from a valid URL
    assert ie._match_id('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch') == \
        'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2026-10-25 07:15:07.737557
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()

    # Constructor creates an instance of the correct class
    assert isinstance(ie, ITVBTCCIE)
    assert isinstance(ie, InfoExtractor)

    # Class-level attributes set on the constructor
    assert ie.ie_key() == 'ITVBTCC'
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie.suitable('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert not ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')

    # _match_id extracts the playlist id from a valid URL
    assert ie._match_id('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch') == \
        'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2026-10-25 07:15:09.273469
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()

    # Valid URLs â should extract the correct video id
    assert ie._match_id('https://www.itv.com/hub/liar/2a4547a0012') == '2a4547a0012'
    assert ie._match_id('https://www.itv.com/hub/through-the-keyhole/2a2271a0033') == '2a2271a0033'
    assert ie._match_id('http://www.itv.com/hub/james-martins-saturday-morning/2a5159a0034') == '2a5159a0034'

    # Invalid URLs â should not match
    for url in (
        'https://www.itv.com/hub/liar/',            # missing id
        'https://www.itv.com/hub/2a4547a0012',      # missing title segment
        'https://www.example.com/hub/liar/2a4547a0012',  # wrong domain
        'https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch',  # ITVBTCC, not ITV
    ):
        assert ie.suitable(url) is False, url

# Generated at 2026-10-25 07:15:10.770023
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()

    # Constructor creates an instance of the correct class
    assert isinstance(ie, ITVBTCCIE)
    assert isinstance(ie, InfoExtractor)

    # Class-level attributes set on the constructor
    assert ie.ie_key() == 'ITVBTCC'
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie.suitable('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert not ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')

    # _match_id extracts the playlist id from a valid URL
    assert ie._match_id('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch') == \
        'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2026-10-25 07:15:12.141191
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()

    # Valid URLs â should extract the correct video id
    assert ie._match_id('https://www.itv.com/hub/liar/2a4547a0012') == '2a4547a0012'
    assert ie._match_id('https://www.itv.com/hub/through-the-keyhole/2a2271a0033') == '2a2271a0033'
    assert ie._match_id('http://www.itv.com/hub/james-martins-saturday-morning/2a5159a0034') == '2a5159a0034'

    # Invalid URLs â should not match
    for url in (
        'https://www.itv.com/hub/liar/',            # missing id
        'https://www.itv.com/hub/2a4547a0012',      # missing title segment
        'https://www.example.com/hub/liar/2a4547a0012',  # wrong domain
        'https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch',  # ITVBTCC, not ITV
    ):
        assert ie.suitable(url) is False, url

# Generated at 2026-10-25 07:15:14.906694
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:15:17.325907
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:15:19.791888
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:15:22.206356
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:15:24.826216
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:15:27.241663
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:15:29.656747
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:15:32.276597
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:15:34.691577
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:15:37.129476
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:15:39.720851
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:15:42.137449
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:15:44.553715
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:15:46.970425
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:15:49.441442
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:15:51.854494
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:15:54.268829
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:16:11.496501
# Unit test for constructor of class ITVIE
def test_ITVIE():ie = ITVIE()

# Generated at 2026-10-25 07:16:12.883024
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()

    # Constructor creates an instance of the correct class
    assert isinstance(ie, ITVBTCCIE)
    assert isinstance(ie, InfoExtractor)

    # Class-level attributes set on the constructor
    assert ie.ie_key() == 'ITVBTCC'
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie.suitable('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert not ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')

    # _match_id extracts the playlist id from a valid URL
    assert ie._match_id('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch') == \
        'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2026-10-25 07:16:14.216761
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()

    # Valid URLs â should extract the correct video id
    assert ie._match_id('https://www.itv.com/hub/liar/2a4547a0012') == '2a4547a0012'
    assert ie._match_id('https://www.itv.com/hub/through-the-keyhole/2a2271a0033') == '2a2271a0033'
    assert ie._match_id('http://www.itv.com/hub/james-martins-saturday-morning/2a5159a0034') == '2a5159a0034'

    # Invalid URLs â should not match
    for url in (
        'https://www.itv.com/hub/liar/',            # missing id
        'https://www.itv.com/hub/2a4547a0012',      # missing title segment
        'https://www.example.com/hub/liar/2a4547a0012',  # wrong domain
        'https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch',  # ITVBTCC, not ITV
    ):
        assert ie.suitable(url) is False, url

# Generated at 2026-10-25 07:16:15.674240
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()

    # Constructor creates an instance of the correct class
    assert isinstance(ie, ITVBTCCIE)
    assert isinstance(ie, InfoExtractor)

    # Class-level attributes set on the constructor
    assert ie.ie_key() == 'ITVBTCC'
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie.suitable('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert not ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')

    # _match_id extracts the playlist id from a valid URL
    assert ie._match_id('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch') == \
        'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2026-10-25 07:16:16.960903
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()

    # Constructor creates an instance of the correct class
    assert isinstance(ie, ITVBTCCIE)
    assert isinstance(ie, InfoExtractor)

    # Class-level attributes set on the constructor
    assert ie.ie_key() == 'ITVBTCC'
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie.suitable('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert not ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')

    # _match_id extracts the playlist id from a valid URL
    assert ie._match_id('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch') == \
        'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2026-10-25 07:16:18.393773
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()

    # Constructor creates an instance of the correct class
    assert isinstance(ie, ITVBTCCIE)
    assert isinstance(ie, InfoExtractor)

    # Class-level attributes set on the constructor
    assert ie.ie_key() == 'ITVBTCC'
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie.suitable('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert not ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')

    # _match_id extracts the playlist id from a valid URL
    assert ie._match_id('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch') == \
        'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2026-10-25 07:16:19.757173
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()

    # Valid URLs â should extract the correct video id
    assert ie._match_id('https://www.itv.com/hub/liar/2a4547a0012') == '2a4547a0012'
    assert ie._match_id('https://www.itv.com/hub/through-the-keyhole/2a2271a0033') == '2a2271a0033'
    assert ie._match_id('http://www.itv.com/hub/james-martins-saturday-morning/2a5159a0034') == '2a5159a0034'

    # Invalid URLs â should not match
    for url in (
        'https://www.itv.com/hub/liar/',            # missing id
        'https://www.itv.com/hub/2a4547a0012',      # missing title segment
        'https://www.example.com/hub/liar/2a4547a0012',  # wrong domain
        'https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch',  # ITVBTCC, not ITV
    ):
        assert ie.suitable(url) is False, url

# Generated at 2026-10-25 07:16:21.112821
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()

    # Valid URLs â should extract the correct video id
    assert ie._match_id('https://www.itv.com/hub/liar/2a4547a0012') == '2a4547a0012'
    assert ie._match_id('https://www.itv.com/hub/through-the-keyhole/2a2271a0033') == '2a2271a0033'
    assert ie._match_id('http://www.itv.com/hub/james-martins-saturday-morning/2a5159a0034') == '2a5159a0034'

    # Invalid URLs â should not match
    for url in (
        'https://www.itv.com/hub/liar/',            # missing id
        'https://www.itv.com/hub/2a4547a0012',      # missing title segment
        'https://www.example.com/hub/liar/2a4547a0012',  # wrong domain
        'https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch',  # ITVBTCC, not ITV
    ):
        assert ie.suitable(url) is False, url

# Generated at 2026-10-25 07:16:22.488677
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()

    # Valid URLs â should extract the correct video id
    assert ie._match_id('https://www.itv.com/hub/liar/2a4547a0012') == '2a4547a0012'
    assert ie._match_id('https://www.itv.com/hub/through-the-keyhole/2a2271a0033') == '2a2271a0033'
    assert ie._match_id('http://www.itv.com/hub/james-martins-saturday-morning/2a5159a0034') == '2a5159a0034'

    # Invalid URLs â should not match
    for url in (
        'https://www.itv.com/hub/liar/',            # missing id
        'https://www.itv.com/hub/2a4547a0012',      # missing title segment
        'https://www.example.com/hub/liar/2a4547a0012',  # wrong domain
        'https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch',  # ITVBTCC, not ITV
    ):
        assert ie.suitable(url) is False, url

# Generated at 2026-10-25 07:16:23.914182
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()

    # Constructor creates an instance of the correct class
    assert isinstance(ie, ITVBTCCIE)
    assert isinstance(ie, InfoExtractor)

    # Class-level attributes set on the constructor
    assert ie.ie_key() == 'ITVBTCC'
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie.suitable('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert not ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')

    # _match_id extracts the playlist id from a valid URL
    assert ie._match_id('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch') == \
        'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2026-10-25 07:16:25.251371
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()

    # Valid URLs â should extract the correct video id
    assert ie._match_id('https://www.itv.com/hub/liar/2a4547a0012') == '2a4547a0012'
    assert ie._match_id('https://www.itv.com/hub/through-the-keyhole/2a2271a0033') == '2a2271a0033'
    assert ie._match_id('http://www.itv.com/hub/james-martins-saturday-morning/2a5159a0034') == '2a5159a0034'

    # Invalid URLs â should not match
    for url in (
        'https://www.itv.com/hub/liar/',            # missing id
        'https://www.itv.com/hub/2a4547a0012',      # missing title segment
        'https://www.example.com/hub/liar/2a4547a0012',  # wrong domain
        'https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch',  # ITVBTCC, not ITV
    ):
        assert ie.suitable(url) is False, url

# Generated at 2026-10-25 07:16:26.681061
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()

    # Constructor creates an instance of the correct class
    assert isinstance(ie, ITVBTCCIE)
    assert isinstance(ie, InfoExtractor)

    # Class-level attributes set on the constructor
    assert ie.ie_key() == 'ITVBTCC'
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie.suitable('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert not ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')

    # _match_id extracts the playlist id from a valid URL
    assert ie._match_id('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch') == \
        'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2026-10-25 07:16:28.208606
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()

    # Valid URLs â should extract the correct video id
    assert ie._match_id('https://www.itv.com/hub/liar/2a4547a0012') == '2a4547a0012'
    assert ie._match_id('https://www.itv.com/hub/through-the-keyhole/2a2271a0033') == '2a2271a0033'
    assert ie._match_id('http://www.itv.com/hub/james-martins-saturday-morning/2a5159a0034') == '2a5159a0034'

    # Invalid URLs â should not match
    for url in (
        'https://www.itv.com/hub/liar/',            # missing id
        'https://www.itv.com/hub/2a4547a0012',      # missing title segment
        'https://www.example.com/hub/liar/2a4547a0012',  # wrong domain
        'https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch',  # ITVBTCC, not ITV
    ):
        assert ie.suitable(url) is False, url

# Generated at 2026-10-25 07:16:29.678620
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()

    # Constructor creates an instance of the correct class
    assert isinstance(ie, ITVBTCCIE)
    assert isinstance(ie, InfoExtractor)

    # Class-level attributes set on the constructor
    assert ie.ie_key() == 'ITVBTCC'
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie.suitable('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert not ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')

    # _match_id extracts the playlist id from a valid URL
    assert ie._match_id('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch') == \
        'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2026-10-25 07:16:32.390751
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:16:34.806801
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:16:37.221016
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:16:39.779086
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:16:42.192401
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:16:44.606568
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:16:47.022324
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:16:49.437335
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:16:51.849266
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:16:54.266203
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:16:55.924206
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():ie = ITVBTCCIE()

# Generated at 2026-10-25 07:16:57.309047
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()

    # Valid URLs â should extract the correct video id
    assert ie._match_id('https://www.itv.com/hub/liar/2a4547a0012') == '2a4547a0012'
    assert ie._match_id('https://www.itv.com/hub/through-the-keyhole/2a2271a0033') == '2a2271a0033'
    assert ie._match_id('http://www.itv.com/hub/james-martins-saturday-morning/2a5159a0034') == '2a5159a0034'

    # Invalid URLs â should not match
    for url in (
        'https://www.itv.com/hub/liar/',            # missing id
        'https://www.itv.com/hub/2a4547a0012',      # missing title segment
        'https://www.example.com/hub/liar/2a4547a0012',  # wrong domain
        'https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch',  # ITVBTCC, not ITV
    ):
        assert ie.suitable(url) is False, url

# Generated at 2026-10-25 07:16:58.653064
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()

    # Valid URLs â should extract the correct video id
    assert ie._match_id('https://www.itv.com/hub/liar/2a4547a0012') == '2a4547a0012'
    assert ie._match_id('https://www.itv.com/hub/through-the-keyhole/2a2271a0033') == '2a2271a0033'
    assert ie._match_id('http://www.itv.com/hub/james-martins-saturday-morning/2a5159a0034') == '2a5159a0034'

    # Invalid URLs â should not match
    for url in (
        'https://www.itv.com/hub/liar/',            # missing id
        'https://www.itv.com/hub/2a4547a0012',      # missing title segment
        'https://www.example.com/hub/liar/2a4547a0012',  # wrong domain
        'https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch',  # ITVBTCC, not ITV
    ):
        assert ie.suitable(url) is False, url

# Generated at 2026-10-25 07:16:59.997091
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()

    # Valid URLs â should extract the correct video id
    assert ie._match_id('https://www.itv.com/hub/liar/2a4547a0012') == '2a4547a0012'
    assert ie._match_id('https://www.itv.com/hub/through-the-keyhole/2a2271a0033') == '2a2271a0033'
    assert ie._match_id('http://www.itv.com/hub/james-martins-saturday-morning/2a5159a0034') == '2a5159a0034'

    # Invalid URLs â should not match
    for url in (
        'https://www.itv.com/hub/liar/',            # missing id
        'https://www.itv.com/hub/2a4547a0012',      # missing title segment
        'https://www.example.com/hub/liar/2a4547a0012',  # wrong domain
        'https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch',  # ITVBTCC, not ITV
    ):
        assert ie.suitable(url) is False, url

# Generated at 2026-10-25 07:17:01.341466
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()

    # Valid URLs â should extract the correct video id
    assert ie._match_id('https://www.itv.com/hub/liar/2a4547a0012') == '2a4547a0012'
    assert ie._match_id('https://www.itv.com/hub/through-the-keyhole/2a2271a0033') == '2a2271a0033'
    assert ie._match_id('http://www.itv.com/hub/james-martins-saturday-morning/2a5159a0034') == '2a5159a0034'

    # Invalid URLs â should not match
    for url in (
        'https://www.itv.com/hub/liar/',            # missing id
        'https://www.itv.com/hub/2a4547a0012',      # missing title segment
        'https://www.example.com/hub/liar/2a4547a0012',  # wrong domain
        'https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch',  # ITVBTCC, not ITV
    ):
        assert ie.suitable(url) is False, url

# Generated at 2026-10-25 07:17:02.669618
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()

    # Constructor creates an instance of the correct class
    assert isinstance(ie, ITVBTCCIE)
    assert isinstance(ie, InfoExtractor)

    # Class-level attributes set on the constructor
    assert ie.ie_key() == 'ITVBTCC'
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie.suitable('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert not ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')

    # _match_id extracts the playlist id from a valid URL
    assert ie._match_id('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch') == \
        'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2026-10-25 07:17:04.030785
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()

    # Constructor creates an instance of the correct class
    assert isinstance(ie, ITVBTCCIE)
    assert isinstance(ie, InfoExtractor)

    # Class-level attributes set on the constructor
    assert ie.ie_key() == 'ITVBTCC'
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie.suitable('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert not ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')

    # _match_id extracts the playlist id from a valid URL
    assert ie._match_id('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch') == \
        'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2026-10-25 07:17:06.010662
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()

    # Valid URLs â should extract the correct video id
    assert ie._match_id('https://www.itv.com/hub/liar/2a4547a0012') == '2a4547a0012'
    assert ie._match_id('https://www.itv.com/hub/through-the-keyhole/2a2271a0033') == '2a2271a0033'
    assert ie._match_id('http://www.itv.com/hub/james-martins-saturday-morning/2a5159a0034') == '2a5159a0034'

    # Invalid URLs â should not match
    for url in (
        'https://www.itv.com/hub/liar/',            # missing id
        'https://www.itv.com/hub/2a4547a0012',      # missing title segment
        'https://www.example.com/hub/liar/2a4547a0012',  # wrong domain
        'https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch',  # ITVBTCC, not ITV
    ):
        assert ie.suitable(url) is False, url

# Generated at 2026-10-25 07:17:07.443197
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()

    # Constructor creates an instance of the correct class
    assert isinstance(ie, ITVBTCCIE)
    assert isinstance(ie, InfoExtractor)

    # Class-level attributes set on the constructor
    assert ie.ie_key() == 'ITVBTCC'
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie.suitable('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert not ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')

    # _match_id extracts the playlist id from a valid URL
    assert ie._match_id('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch') == \
        'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2026-10-25 07:17:08.778469
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()

    # Constructor creates an instance of the correct class
    assert isinstance(ie, ITVBTCCIE)
    assert isinstance(ie, InfoExtractor)

    # Class-level attributes set on the constructor
    assert ie.ie_key() == 'ITVBTCC'
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie.suitable('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert not ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')

    # _match_id extracts the playlist id from a valid URL
    assert ie._match_id('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch') == \
        'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2026-10-25 07:17:10.208166
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()

    # Constructor creates an instance of the correct class
    assert isinstance(ie, ITVBTCCIE)
    assert isinstance(ie, InfoExtractor)

    # Class-level attributes set on the constructor
    assert ie.ie_key() == 'ITVBTCC'
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie.suitable('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert not ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')

    # _match_id extracts the playlist id from a valid URL
    assert ie._match_id('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch') == \
        'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2026-10-25 07:17:11.661505
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()

    # Valid URLs â should extract the correct video id
    assert ie._match_id('https://www.itv.com/hub/liar/2a4547a0012') == '2a4547a0012'
    assert ie._match_id('https://www.itv.com/hub/through-the-keyhole/2a2271a0033') == '2a2271a0033'
    assert ie._match_id('http://www.itv.com/hub/james-martins-saturday-morning/2a5159a0034') == '2a5159a0034'

    # Invalid URLs â should not match
    for url in (
        'https://www.itv.com/hub/liar/',            # missing id
        'https://www.itv.com/hub/2a4547a0012',      # missing title segment
        'https://www.example.com/hub/liar/2a4547a0012',  # wrong domain
        'https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch',  # ITVBTCC, not ITV
    ):
        assert ie.suitable(url) is False, url

# Generated at 2026-10-25 07:17:12.992360
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()

    # Constructor creates an instance of the correct class
    assert isinstance(ie, ITVBTCCIE)
    assert isinstance(ie, InfoExtractor)

    # Class-level attributes set on the constructor
    assert ie.ie_key() == 'ITVBTCC'
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie.suitable('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert not ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')

    # _match_id extracts the playlist id from a valid URL
    assert ie._match_id('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch') == \
        'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2026-10-25 07:17:15.746728
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:17:18.394252
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:17:20.807171
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:17:23.227849
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:17:25.644428
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:17:28.062322
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:17:30.479610
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:17:32.894275
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:17:35.444870
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:17:37.860205
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:17:40.279574
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:17:42.689332
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:17:46.666104
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:17:49.100906
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:17:51.517747
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:17:53.935134
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:17:56.348800
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:17:58.792149
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:18:01.208454
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:18:03.625200
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:18:06.038760
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:18:08.457501
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:18:10.874630
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:18:13.288145
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:18:15.706911
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:18:18.125317
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:18:20.539610
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:18:22.954844
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:18:25.369846
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:18:27.783835
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:18:30.200648
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:18:32.619455
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:18:35.033480
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:18:37.452817
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:18:39.866694
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:18:42.279219
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:18:44.692528
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:18:47.111386
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:18:49.528665
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:18:51.941348
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:18:54.359965
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:18:56.777605
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:19:03.986153
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:19:06.400221
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:19:08.816990
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:19:11.233345
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:19:13.651235
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:19:16.061513
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:19:18.479968
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:19:20.897335
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:19:23.310023
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:19:25.728926
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:19:28.144255
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:19:30.563891
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:19:32.980794
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:19:35.429328
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:19:37.812083
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:19:40.269355
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:19:42.688061
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:19:45.118099
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:19:47.531470
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:19:49.950631
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:19:52.364851
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:19:54.880023
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:19:57.267892
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:19:59.685412
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:20:02.097741
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:20:04.514217
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:20:06.931773
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:20:09.344133
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:20:11.762414
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:20:14.179685
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:20:27.130468
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:20:29.547741
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:20:31.963956
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:20:34.378902
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:20:36.797298
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:20:39.216429
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:20:41.630447
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:20:44.050900
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:20:46.465835
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:20:48.915462
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:20:51.334700
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:20:53.751940
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:20:56.166148
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:20:58.583434
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:21:01.001036
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:21:03.449459
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:21:05.858924
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:21:08.273409
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:21:10.690745
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:21:13.103886
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:21:15.522059
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:21:17.938114
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:21:20.352486
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:21:22.767744
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:21:25.183557
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:21:27.598119
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:21:30.014407
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 07:21:32.432385
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:21:34.846122
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:21:37.260759
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:22:01.243278
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()

    # Valid URLs â should extract the correct video id
    assert ie._match_id('https://www.itv.com/hub/liar/2a4547a0012') == '2a4547a0012'
    assert ie._match_id('https://www.itv.com/hub/through-the-keyhole/2a2271a0033') == '2a2271a0033'
    assert ie._match_id('http://www.itv.com/hub/james-martins-saturday-morning/2a5159a0034') == '2a5159a0034'

    # Invalid URLs â should not match
    for url in (
        'https://www.itv.com/hub/liar/',            # missing id
        'https://www.itv.com/hub/2a4547a0012',      # missing title segment
        'https://www.example.com/hub/liar/2a4547a0012',  # wrong domain
        'https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch',  # ITVBTCC, not ITV
    ):
        assert ie.suitable(url) is False, url

# Generated at 2026-10-25 07:22:02.665877
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()

    # Constructor creates an instance of the correct class
    assert isinstance(ie, ITVBTCCIE)
    assert isinstance(ie, InfoExtractor)

    # Class-level attributes set on the constructor
    assert ie.ie_key() == 'ITVBTCC'
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie.suitable('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert not ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')

    # _match_id extracts the playlist id from a valid URL
    assert ie._match_id('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch') == \
        'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2026-10-25 07:22:04.001800
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()

    # Constructor creates an instance of the correct class
    assert isinstance(ie, ITVBTCCIE)
    assert isinstance(ie, InfoExtractor)

    # Class-level attributes set on the constructor
    assert ie.ie_key() == 'ITVBTCC'
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie.suitable('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert not ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')

    # _match_id extracts the playlist id from a valid URL
    assert ie._match_id('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch') == \
        'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2026-10-25 07:22:05.537292
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()

    # Constructor creates an instance of the correct class
    assert isinstance(ie, ITVBTCCIE)
    assert isinstance(ie, InfoExtractor)

    # Class-level attributes set on the constructor
    assert ie.ie_key() == 'ITVBTCC'
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie.suitable('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert not ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')

    # _match_id extracts the playlist id from a valid URL
    assert ie._match_id('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch') == \
        'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2026-10-25 07:22:06.968437
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()

    # Valid URLs â should extract the correct video id
    assert ie._match_id('https://www.itv.com/hub/liar/2a4547a0012') == '2a4547a0012'
    assert ie._match_id('https://www.itv.com/hub/through-the-keyhole/2a2271a0033') == '2a2271a0033'
    assert ie._match_id('http://www.itv.com/hub/james-martins-saturday-morning/2a5159a0034') == '2a5159a0034'

    # Invalid URLs â should not match
    for url in (
        'https://www.itv.com/hub/liar/',            # missing id
        'https://www.itv.com/hub/2a4547a0012',      # missing title segment
        'https://www.example.com/hub/liar/2a4547a0012',  # wrong domain
        'https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch',  # ITVBTCC, not ITV
    ):
        assert ie.suitable(url) is False, url

# Generated at 2026-10-25 07:22:08.328298
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()

    # Valid URLs â should extract the correct video id
    assert ie._match_id('https://www.itv.com/hub/liar/2a4547a0012') == '2a4547a0012'
    assert ie._match_id('https://www.itv.com/hub/through-the-keyhole/2a2271a0033') == '2a2271a0033'
    assert ie._match_id('http://www.itv.com/hub/james-martins-saturday-morning/2a5159a0034') == '2a5159a0034'

    # Invalid URLs â should not match
    for url in (
        'https://www.itv.com/hub/liar/',            # missing id
        'https://www.itv.com/hub/2a4547a0012',      # missing title segment
        'https://www.example.com/hub/liar/2a4547a0012',  # wrong domain
        'https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch',  # ITVBTCC, not ITV
    ):
        assert ie.suitable(url) is False, url

# Generated at 2026-10-25 07:22:09.731335
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()

    # Constructor creates an instance of the correct class
    assert isinstance(ie, ITVBTCCIE)
    assert isinstance(ie, InfoExtractor)

    # Class-level attributes set on the constructor
    assert ie.ie_key() == 'ITVBTCC'
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie.suitable('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert not ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')

    # _match_id extracts the playlist id from a valid URL
    assert ie._match_id('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch') == \
        'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2026-10-25 07:22:11.266320
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()

    # Valid URLs â should extract the correct video id
    assert ie._match_id('https://www.itv.com/hub/liar/2a4547a0012') == '2a4547a0012'
    assert ie._match_id('https://www.itv.com/hub/through-the-keyhole/2a2271a0033') == '2a2271a0033'
    assert ie._match_id('http://www.itv.com/hub/james-martins-saturday-morning/2a5159a0034') == '2a5159a0034'

    # Invalid URLs â should not match
    for url in (
        'https://www.itv.com/hub/liar/',            # missing id
        'https://www.itv.com/hub/2a4547a0012',      # missing title segment
        'https://www.example.com/hub/liar/2a4547a0012',  # wrong domain
        'https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch',  # ITVBTCC, not ITV
    ):
        assert ie.suitable(url) is False, url

# Generated at 2026-10-25 07:22:12.700487
# Unit test for constructor of class ITVIE
def test_ITVIE():
    ie = ITVIE()

    # Valid URLs â should extract the correct video id
    assert ie._match_id('https://www.itv.com/hub/liar/2a4547a0012') == '2a4547a0012'
    assert ie._match_id('https://www.itv.com/hub/through-the-keyhole/2a2271a0033') == '2a2271a0033'
    assert ie._match_id('http://www.itv.com/hub/james-martins-saturday-morning/2a5159a0034') == '2a5159a0034'

    # Invalid URLs â should not match
    for url in (
        'https://www.itv.com/hub/liar/',            # missing id
        'https://www.itv.com/hub/2a4547a0012',      # missing title segment
        'https://www.example.com/hub/liar/2a4547a0012',  # wrong domain
        'https://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch',  # ITVBTCC, not ITV
    ):
        assert ie.suitable(url) is False, url

# Generated at 2026-10-25 07:22:14.058210
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():
    ie = ITVBTCCIE()

    # Constructor creates an instance of the correct class
    assert isinstance(ie, ITVBTCCIE)
    assert isinstance(ie, InfoExtractor)

    # Class-level attributes set on the constructor
    assert ie.ie_key() == 'ITVBTCC'
    assert ie.IE_NAME == 'ITVBTCC'
    assert ie.suitable('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch')
    assert not ie.suitable('https://www.itv.com/hub/liar/2a4547a0012')

    # _match_id extracts the playlist id from a valid URL
    assert ie._match_id('http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch') == \
        'btcc-2018-all-the-action-from-brands-hatch'

# Generated at 2026-10-25 07:23:06.866296
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:23:09.283263
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:23:11.699174
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:23:14.113747
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:23:16.531482
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:23:18.948759
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:23:21.365147
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:23:23.774613
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:23:26.191446
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:23:28.606340
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:23:31.055730
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:23:33.473292
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:23:35.921056
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:23:38.341150
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 07:23:40.748835
# Unit test for constructor of class ITVIE