

# Generated at 2026-10-25 08:18:46.458402
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

# Generated at 2026-10-25 08:18:47.792179
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

# Generated at 2026-10-25 08:18:49.223947
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

# Generated at 2026-10-25 08:18:50.655001
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

# Generated at 2026-10-25 08:18:52.121986
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

# Generated at 2026-10-25 08:18:53.523181
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

# Generated at 2026-10-25 08:18:54.956194
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

# Generated at 2026-10-25 08:18:56.392234
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

# Generated at 2026-10-25 08:18:57.722082
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

# Generated at 2026-10-25 08:18:59.154591
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

# Generated at 2026-10-25 08:19:00.589316
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

# Generated at 2026-10-25 08:19:03.118148
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:19:05.534445
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:19:07.954525
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:19:09.343692
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

# Generated at 2026-10-25 08:19:10.730547
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

# Generated at 2026-10-25 08:19:12.099566
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

# Generated at 2026-10-25 08:19:13.425252
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

# Generated at 2026-10-25 08:19:15.027837
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

# Generated at 2026-10-25 08:19:16.460274
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

# Generated at 2026-10-25 08:19:17.792466
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

# Generated at 2026-10-25 08:19:19.178825
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

# Generated at 2026-10-25 08:19:20.660021
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

# Generated at 2026-10-25 08:19:21.990729
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

# Generated at 2026-10-25 08:19:23.427242
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

# Generated at 2026-10-25 08:19:24.750405
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

# Generated at 2026-10-25 08:19:26.078184
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

# Generated at 2026-10-25 08:19:27.658585
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

# Generated at 2026-10-25 08:19:29.022997
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

# Generated at 2026-10-25 08:19:30.358942
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

# Generated at 2026-10-25 08:19:31.731305
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

# Generated at 2026-10-25 08:19:33.154864
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

# Generated at 2026-10-25 08:19:34.489651
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

# Generated at 2026-10-25 08:19:37.128466
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:19:39.679782
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:19:42.096266
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:19:44.512439
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 08:19:47.392450
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 08:19:49.806859
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 08:19:52.221914
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 08:19:54.640072
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 08:19:57.291822
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 08:19:59.737350
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:20:02.123879
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:20:04.537030
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:20:07.252574
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:20:09.666395
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:20:12.081619
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:20:14.500602
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 08:20:16.919016
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 08:20:19.334387
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 08:20:21.749613
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:20:24.170368
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:20:26.580850
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:20:28.993741
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:20:31.409913
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:20:33.825437
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:20:36.237802
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:20:38.652043
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:20:41.068728
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:20:43.485030
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 08:20:45.902921
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 08:20:48.317738
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 08:20:50.734981
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:20:53.152657
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:20:55.568370
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:20:58.075793
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:21:00.460889
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:21:02.880149
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:21:05.298780
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 08:21:07.717126
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 08:21:10.129395
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 08:21:12.562108
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 08:21:14.978103
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 08:21:17.394129
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 08:21:21.678250
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:21:24.539991
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:21:27.320686
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:21:29.941244
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:21:32.874294
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:21:35.384793
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:21:38.201071
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:21:40.973190
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:21:43.267276
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:21:45.199020
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

# Generated at 2026-10-25 08:21:47.274973
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

# Generated at 2026-10-25 08:21:48.747280
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

# Generated at 2026-10-25 08:21:50.275856
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

# Generated at 2026-10-25 08:21:52.221870
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

# Generated at 2026-10-25 08:21:53.799831
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

# Generated at 2026-10-25 08:21:55.345890
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

# Generated at 2026-10-25 08:23:16.921709
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

# Generated at 2026-10-25 08:23:18.280472
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

# Generated at 2026-10-25 08:23:19.622875
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

# Generated at 2026-10-25 08:23:21.151508
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

# Generated at 2026-10-25 08:23:22.507201
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

# Generated at 2026-10-25 08:23:23.911508
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

# Generated at 2026-10-25 08:23:26.460070
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:23:28.877455
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:23:31.399491
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:23:33.810605
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 08:23:36.229971
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 08:23:38.676716
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 08:23:41.088157
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 08:23:43.511991
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 08:23:45.931673
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 08:23:48.351548
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:23:50.765647
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:23:53.185820
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:24:01.191120
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

# Generated at 2026-10-25 08:24:02.540540
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

# Generated at 2026-10-25 08:24:04.004544
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

# Generated at 2026-10-25 08:24:05.438476
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

# Generated at 2026-10-25 08:24:06.869772
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

# Generated at 2026-10-25 08:24:08.232481
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

# Generated at 2026-10-25 08:24:09.636927
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

# Generated at 2026-10-25 08:24:11.171151
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

# Generated at 2026-10-25 08:24:12.516059
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

# Generated at 2026-10-25 08:24:13.860374
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

# Generated at 2026-10-25 08:24:31.191195
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 08:24:33.613238
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 08:24:36.028315
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 08:24:38.444695
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 08:24:40.863781
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 08:24:43.365789
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 08:24:46.027326
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:24:48.443704
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:24:50.861462
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:24:53.282103
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:24:55.698623
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:24:58.117424
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:25:00.539267
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:25:02.957287
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:25:05.378099
# Unit test for constructor of class ITVIE

# Generated at 2026-10-25 08:25:07.794254
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 08:25:10.215527
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 08:25:12.629610
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 08:25:15.052304
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 08:25:17.467831
# Unit test for constructor of class ITVBTCCIE

# Generated at 2026-10-25 08:25:19.112413
# Unit test for constructor of class ITVBTCCIE
def test_ITVBTCCIE():ie = ITVBTCCIE()

# Generated at 2026-10-25 08:25:20.498182
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

# Generated at 2026-10-25 08:25:21.841718
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

# Generated at 2026-10-25 08:25:23.263056
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

# Generated at 2026-10-25 08:26:01.178993
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

# Generated at 2026-10-25 08:26:02.890413
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

# Generated at 2026-10-25 08:26:04.232497
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

# Generated at 2026-10-25 08:26:05.590652
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

# Generated at 2026-10-25 08:26:06.994770
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

# Generated at 2026-10-25 08:26:08.420577
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

# Generated at 2026-10-25 08:26:09.959268
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

# Generated at 2026-10-25 08:26:11.475458
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

# Generated at 2026-10-25 08:26:12.834389
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

# Generated at 2026-10-25 08:26:14.358553
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

# Generated at 2026-10-25 08:27:17.203945
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

# Generated at 2026-10-25 08:27:18.564839
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

# Generated at 2026-10-25 08:27:19.918756
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

# Generated at 2026-10-25 08:27:21.343278
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

# Generated at 2026-10-25 08:27:22.925281
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

# Generated at 2026-10-25 08:27:24.279331
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

# Generated at 2026-10-25 08:27:25.634647
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

# Generated at 2026-10-25 08:27:26.992536
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

# Generated at 2026-10-25 08:27:28.396161
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

# Generated at 2026-10-25 08:27:29.811196
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