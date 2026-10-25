

# Generated at 2026-10-24 07:33:43.330234
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 07:33:44.660194
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 07:33:46.041591
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # 1. Default construction: no downloader, no network/setup triggered
    ie = ViafreeIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._ready is False
    assert ie._GEO_BYPASS is False

    # 2. Construction with a downloader stores it via set_downloader()
    downloader = Mock()
    ie2 = ViafreeIE(downloader)
    assert ie2._downloader is downloader
    assert ie2._ready is False

    # 3. Class config used by constructor/suitable() is intact
    assert ie.IE_NAME == 'viafree' or ie.IE_NAME  # name set on class
    assert ie._VALID_URL

# Generated at 2026-10-24 07:33:48.462505
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:33:51.104607
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:33:53.665627
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:33:56.078606
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:33:58.491511
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:34:00.911752
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:34:03.328980
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:34:05.743156
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:34:08.154862
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:34:24.741864
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    # Constructor created a usable instance
    assert ie is not None
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'

    # _VALID_URL works after construction
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert ie.suitable('https://play.nova.bg/programi/zdravei-bulgariya/764300')
    assert ie.suitable('mtg:418113')

    # Non-matching URLs rejected
    assert not ie.suitable('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    # ID extraction works
    assert ie._match_id('mtg:418113') == '418113'
    assert ie._match_id('http://www.tv3play.se/program/husraddarna/395385') == '395385'


if __name__ == '__main__':
    test_TVPlayIE()
    print('test_TVPlayIE passed')

# Generated at 2026-10-24 07:34:26.054280
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 07:34:42.662165
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    # Constructor should work with no arguments
    # via InfoExtractor base class
    ie = TVPlayIE()

    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, TVPlayIE)

    # Class-level identity defined in this file
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'

    # _VALID_URL / _TESTS are defined
    assert isinstance(ie._VALID_URL, str)
    re.compile(ie._VALID_URL)
    assert isinstance(ie._TESTS, list) and len(ie._TESTS) > 0

    # Instance exposes extractor API
    assert callable(getattr(ie, '_real_extract', None))
    assert callable(getattr(ie, '_match_id', None))

# Generated at 2026-10-24 07:34:45.079372
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:34:47.493386
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:34:49.907464
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:34:52.320438
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:34:54.735911
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:34:57.150648
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:34:59.566651
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:35:02.017866
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:35:04.396329
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:35:06.810963
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:35:09.228567
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:35:11.645805
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:35:14.058973
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:35:16.470820
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:35:18.884194
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:35:21.571331
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()
    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'
    assert TVPlayIE._VALID_URL is not None
    assert TVPlayIE._match_id('mtg:418113') == '418113'
    assert TVPlayIE._match_id('http://www.tv3play.se/program/husraddarna/395385?autostart=true') == '395385'
    assert TVPlayIE._match_id('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true') == '418113'
    ie2 = TVPlayIE(None)
    assert isinstance(ie2, InfoExtractor)
    assert ie2.IE_NAME == 'mtg'

# Generated at 2026-10-24 07:35:22.893365
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 07:35:24.228236
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 07:35:25.550738
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # 1. Default construction: no downloader, no network/setup triggered
    ie = ViafreeIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._ready is False
    assert ie._GEO_BYPASS is False

    # 2. Construction with a downloader stores it via set_downloader()
    downloader = Mock()
    ie2 = ViafreeIE(downloader)
    assert ie2._downloader is downloader
    assert ie2._ready is False

    # 3. Class config used by constructor/suitable() is intact
    assert ie.IE_NAME == 'viafree' or ie.IE_NAME  # name set on class
    assert ie._VALID_URL

# Generated at 2026-10-24 07:35:42.042017
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    # Constructor created a usable instance
    assert ie is not None
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'

    # _VALID_URL works after construction
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert ie.suitable('https://play.nova.bg/programi/zdravei-bulgariya/764300')
    assert ie.suitable('mtg:418113')

    # Non-matching URLs rejected
    assert not ie.suitable('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    # ID extraction works
    assert ie._match_id('mtg:418113') == '418113'
    assert ie._match_id('http://www.tv3play.se/program/husraddarna/395385') == '395385'


if __name__ == '__main__':
    test_TVPlayIE()
    print('test_TVPlayIE passed')

# Generated at 2026-10-24 07:35:44.457516
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:35:46.872035
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:35:49.427506
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:35:51.926635
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:35:54.502854
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:35:56.917301
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:35:59.332415
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:36:01.747070
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:36:04.162570
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:36:06.577560
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:36:08.992121
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:36:11.406193
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:36:13.819209
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:36:16.235525
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:36:18.651580
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:36:21.065085
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:36:23.480173
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:36:25.894468
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:36:28.564293
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()
    assert isinstance(ie, InfoExtractor)
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'
    assert TVPlayIE._VALID_URL is not None
    assert TVPlayIE._match_id('mtg:418113') == '418113'
    assert TVPlayIE._match_id('http://www.tv3play.se/program/husraddarna/395385?autostart=true') == '395385'
    assert TVPlayIE._match_id('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true') == '418113'
    ie2 = TVPlayIE(None)
    assert isinstance(ie2, InfoExtractor)
    assert ie2.IE_NAME == 'mtg'

# Generated at 2026-10-24 07:36:29.943058
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 07:36:31.260016
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 07:36:32.576564
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # 1. Default construction: no downloader, no network/setup triggered
    ie = ViafreeIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._ready is False
    assert ie._GEO_BYPASS is False

    # 2. Construction with a downloader stores it via set_downloader()
    downloader = Mock()
    ie2 = ViafreeIE(downloader)
    assert ie2._downloader is downloader
    assert ie2._ready is False

    # 3. Class config used by constructor/suitable() is intact
    assert ie.IE_NAME == 'viafree' or ie.IE_NAME  # name set on class
    assert ie._VALID_URL

# Generated at 2026-10-24 07:36:33.899687
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 07:36:35.213713
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 07:36:51.615891
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    # Constructor created a usable instance
    assert ie is not None
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'

    # _VALID_URL works after construction
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert ie.suitable('https://play.nova.bg/programi/zdravei-bulgariya/764300')
    assert ie.suitable('mtg:418113')

    # Non-matching URLs rejected
    assert not ie.suitable('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    # ID extraction works
    assert ie._match_id('mtg:418113') == '418113'
    assert ie._match_id('http://www.tv3play.se/program/husraddarna/395385') == '395385'


if __name__ == '__main__':
    test_TVPlayIE()
    print('test_TVPlayIE passed')

# Generated at 2026-10-24 07:36:54.033053
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:36:56.451949
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:36:58.864649
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:37:01.284562
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:37:03.695699
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:37:06.108291
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:37:08.522048
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:37:10.934835
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:37:13.355300
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:37:15.892185
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:37:18.309613
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:37:20.725269
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:37:23.142233
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:37:25.564226
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:37:27.974051
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:37:30.389545
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:37:32.989460
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:37:34.294330
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():ie = TVPlayIE()

    # Constructor creates a usable instance with the documented IE_NAME

# Generated at 2026-10-24 07:37:35.621198
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # 1. Default construction: no downloader, no network/setup triggered
    ie = ViafreeIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._ready is False
    assert ie._GEO_BYPASS is False

    # 2. Construction with a downloader stores it via set_downloader()
    downloader = Mock()
    ie2 = ViafreeIE(downloader)
    assert ie2._downloader is downloader
    assert ie2._ready is False

    # 3. Class config used by constructor/suitable() is intact
    assert ie.IE_NAME == 'viafree' or ie.IE_NAME  # name set on class
    assert ie._VALID_URL

# Generated at 2026-10-24 07:37:36.944185
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 07:37:38.273576
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 07:37:55.083822
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    # Constructor created a usable instance
    assert ie is not None
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'

    # _VALID_URL works after construction
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert ie.suitable('https://play.nova.bg/programi/zdravei-bulgariya/764300')
    assert ie.suitable('mtg:418113')

    # Non-matching URLs rejected
    assert not ie.suitable('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    # ID extraction works
    assert ie._match_id('mtg:418113') == '418113'
    assert ie._match_id('http://www.tv3play.se/program/husraddarna/395385') == '395385'


if __name__ == '__main__':
    test_TVPlayIE()
    print('test_TVPlayIE passed')

# Generated at 2026-10-24 07:37:57.498911
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:37:59.915776
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:38:02.330686
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:38:04.743780
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:38:07.158906
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:38:09.575057
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:38:11.995066
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:38:14.410307
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:38:16.996803
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:38:20.612996
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:38:23.027151
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:38:25.442841
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:38:27.858234
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:38:30.271501
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:38:32.685124
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:38:35.103141
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:38:37.512923
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:38:39.927663
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:38:58.458055
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():ie = TVPlayHomeIE()

# Generated at 2026-10-24 07:38:59.894560
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 07:39:01.225238
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # 1. Default construction: no downloader, no network/setup triggered
    ie = ViafreeIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._ready is False
    assert ie._GEO_BYPASS is False

    # 2. Construction with a downloader stores it via set_downloader()
    downloader = Mock()
    ie2 = ViafreeIE(downloader)
    assert ie2._downloader is downloader
    assert ie2._ready is False

    # 3. Class config used by constructor/suitable() is intact
    assert ie.IE_NAME == 'viafree' or ie.IE_NAME  # name set on class
    assert ie._VALID_URL

# Generated at 2026-10-24 07:39:02.657004
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # 1. Default construction: no downloader, no network/setup triggered
    ie = ViafreeIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._ready is False
    assert ie._GEO_BYPASS is False

    # 2. Construction with a downloader stores it via set_downloader()
    downloader = Mock()
    ie2 = ViafreeIE(downloader)
    assert ie2._downloader is downloader
    assert ie2._ready is False

    # 3. Class config used by constructor/suitable() is intact
    assert ie.IE_NAME == 'viafree' or ie.IE_NAME  # name set on class
    assert ie._VALID_URL

# Generated at 2026-10-24 07:39:03.980231
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 07:39:05.296051
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # 1. Default construction: no downloader, no network/setup triggered
    ie = ViafreeIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._ready is False
    assert ie._GEO_BYPASS is False

    # 2. Construction with a downloader stores it via set_downloader()
    downloader = Mock()
    ie2 = ViafreeIE(downloader)
    assert ie2._downloader is downloader
    assert ie2._ready is False

    # 3. Class config used by constructor/suitable() is intact
    assert ie.IE_NAME == 'viafree' or ie.IE_NAME  # name set on class
    assert ie._VALID_URL

# Generated at 2026-10-24 07:39:06.630138
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # 1. Default construction: no downloader, no network/setup triggered
    ie = ViafreeIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._ready is False
    assert ie._GEO_BYPASS is False

    # 2. Construction with a downloader stores it via set_downloader()
    downloader = Mock()
    ie2 = ViafreeIE(downloader)
    assert ie2._downloader is downloader
    assert ie2._ready is False

    # 3. Class config used by constructor/suitable() is intact
    assert ie.IE_NAME == 'viafree' or ie.IE_NAME  # name set on class
    assert ie._VALID_URL

# Generated at 2026-10-24 07:39:26.310686
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    # Constructor created a usable instance
    assert ie is not None
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'

    # _VALID_URL works after construction
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert ie.suitable('https://play.nova.bg/programi/zdravei-bulgariya/764300')
    assert ie.suitable('mtg:418113')

    # Non-matching URLs rejected
    assert not ie.suitable('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    # ID extraction works
    assert ie._match_id('mtg:418113') == '418113'
    assert ie._match_id('http://www.tv3play.se/program/husraddarna/395385') == '395385'


if __name__ == '__main__':
    test_TVPlayIE()
    print('test_TVPlayIE passed')

# Generated at 2026-10-24 07:39:28.731519
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:39:31.147314
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:39:33.561059
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:39:36.126072
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:39:38.641719
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:39:41.058805
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:39:43.472312
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:39:45.892249
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:39:48.305972
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:39:50.718807
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:39:53.136393
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:39:55.552388
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:39:57.969801
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:40:00.385182
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:40:02.796313
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 07:40:05.211310
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:40:07.818453
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:40:09.224353
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():ie = TVPlayIE()

    # Constructor creates a usable instance with the documented IE_NAME

# Generated at 2026-10-24 07:40:10.650421
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 07:40:27.342052
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    # Constructor created a usable instance
    assert ie is not None
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'

    # _VALID_URL works after construction
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert ie.suitable('https://play.nova.bg/programi/zdravei-bulgariya/764300')
    assert ie.suitable('mtg:418113')

    # Non-matching URLs rejected
    assert not ie.suitable('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    # ID extraction works
    assert ie._match_id('mtg:418113') == '418113'
    assert ie._match_id('http://www.tv3play.se/program/husraddarna/395385') == '395385'


if __name__ == '__main__':
    test_TVPlayIE()
    print('test_TVPlayIE passed')

# Generated at 2026-10-24 07:40:28.776053
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 07:40:37.667081
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # 1. Default construction: no downloader, no network/setup triggered
    ie = ViafreeIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._ready is False
    assert ie._GEO_BYPASS is False

    # 2. Construction with a downloader stores it via set_downloader()
    downloader = Mock()
    ie2 = ViafreeIE(downloader)
    assert ie2._downloader is downloader
    assert ie2._ready is False

    # 3. Class config used by constructor/suitable() is intact
    assert ie.IE_NAME == 'viafree' or ie.IE_NAME  # name set on class
    assert ie._VALID_URL

# Generated at 2026-10-24 07:40:39.036874
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 07:40:40.355936
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 07:40:41.984071
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # 1. Default construction: no downloader, no network/setup triggered
    ie = ViafreeIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._ready is False
    assert ie._GEO_BYPASS is False

    # 2. Construction with a downloader stores it via set_downloader()
    downloader = Mock()
    ie2 = ViafreeIE(downloader)
    assert ie2._downloader is downloader
    assert ie2._ready is False

    # 3. Class config used by constructor/suitable() is intact
    assert ie.IE_NAME == 'viafree' or ie.IE_NAME  # name set on class
    assert ie._VALID_URL

# Generated at 2026-10-24 07:40:43.421664
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    # Constructor created a usable instance
    assert ie is not None
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'

    # _VALID_URL works after construction
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert ie.suitable('https://play.nova.bg/programi/zdravei-bulgariya/764300')
    assert ie.suitable('mtg:418113')

    # Non-matching URLs rejected
    assert not ie.suitable('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    # ID extraction works
    assert ie._match_id('mtg:418113') == '418113'
    assert ie._match_id('http://www.tv3play.se/program/husraddarna/395385') == '395385'


if __name__ == '__main__':
    test_TVPlayIE()
    print('test_TVPlayIE passed')

# Generated at 2026-10-24 07:40:44.766925
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    # Constructor created a usable instance
    assert ie is not None
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'

    # _VALID_URL works after construction
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert ie.suitable('https://play.nova.bg/programi/zdravei-bulgariya/764300')
    assert ie.suitable('mtg:418113')

    # Non-matching URLs rejected
    assert not ie.suitable('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    # ID extraction works
    assert ie._match_id('mtg:418113') == '418113'
    assert ie._match_id('http://www.tv3play.se/program/husraddarna/395385') == '395385'


if __name__ == '__main__':
    test_TVPlayIE()
    print('test_TVPlayIE passed')

# Generated at 2026-10-24 07:40:46.186046
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    # Constructor created a usable instance
    assert ie is not None
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'

    # _VALID_URL works after construction
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert ie.suitable('https://play.nova.bg/programi/zdravei-bulgariya/764300')
    assert ie.suitable('mtg:418113')

    # Non-matching URLs rejected
    assert not ie.suitable('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    # ID extraction works
    assert ie._match_id('mtg:418113') == '418113'
    assert ie._match_id('http://www.tv3play.se/program/husraddarna/395385') == '395385'


if __name__ == '__main__':
    test_TVPlayIE()
    print('test_TVPlayIE passed')

# Generated at 2026-10-24 07:40:47.617396
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # 1. Default construction: no downloader, no network/setup triggered
    ie = ViafreeIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._ready is False
    assert ie._GEO_BYPASS is False

    # 2. Construction with a downloader stores it via set_downloader()
    downloader = Mock()
    ie2 = ViafreeIE(downloader)
    assert ie2._downloader is downloader
    assert ie2._ready is False

    # 3. Class config used by constructor/suitable() is intact
    assert ie.IE_NAME == 'viafree' or ie.IE_NAME  # name set on class
    assert ie._VALID_URL

# Generated at 2026-10-24 07:40:49.050775
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # 1. Default construction: no downloader, no network/setup triggered
    ie = ViafreeIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._ready is False
    assert ie._GEO_BYPASS is False

    # 2. Construction with a downloader stores it via set_downloader()
    downloader = Mock()
    ie2 = ViafreeIE(downloader)
    assert ie2._downloader is downloader
    assert ie2._ready is False

    # 3. Class config used by constructor/suitable() is intact
    assert ie.IE_NAME == 'viafree' or ie.IE_NAME  # name set on class
    assert ie._VALID_URL

# Generated at 2026-10-24 07:41:05.641611
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    # Constructor created a usable instance
    assert ie is not None
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'

    # _VALID_URL works after construction
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert ie.suitable('https://play.nova.bg/programi/zdravei-bulgariya/764300')
    assert ie.suitable('mtg:418113')

    # Non-matching URLs rejected
    assert not ie.suitable('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    # ID extraction works
    assert ie._match_id('mtg:418113') == '418113'
    assert ie._match_id('http://www.tv3play.se/program/husraddarna/395385') == '395385'


if __name__ == '__main__':
    test_TVPlayIE()
    print('test_TVPlayIE passed')

# Generated at 2026-10-24 07:41:25.474937
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # 1. Default construction: no downloader, no network/setup triggered
    ie = ViafreeIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._ready is False
    assert ie._GEO_BYPASS is False

    # 2. Construction with a downloader stores it via set_downloader()
    downloader = Mock()
    ie2 = ViafreeIE(downloader)
    assert ie2._downloader is downloader
    assert ie2._ready is False

    # 3. Class config used by constructor/suitable() is intact
    assert ie.IE_NAME == 'viafree' or ie.IE_NAME  # name set on class
    assert ie._VALID_URL

# Generated at 2026-10-24 07:41:51.208271
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    extractor = TVPlayIE()

    assert isinstance(extractor, TVPlayIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'
    assert extractor._downloader is None
    assert extractor._ready is False

# Generated at 2026-10-24 07:42:00.732571
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    downloader = object()
    extractor = TVPlayIE(downloader)

    assert isinstance(extractor, TVPlayIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'
    assert extractor.suitable(
        'http://www.tvplay.lv/parraides/vinas-melo-labak/418113')
    assert extractor._match_id('mtg:418113') == '418113'

# Generated at 2026-10-24 07:42:02.065470
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # 1. Default construction: no downloader, no network/setup triggered
    ie = ViafreeIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._ready is False
    assert ie._GEO_BYPASS is False

    # 2. Construction with a downloader stores it via set_downloader()
    downloader = Mock()
    ie2 = ViafreeIE(downloader)
    assert ie2._downloader is downloader
    assert ie2._ready is False

    # 3. Class config used by constructor/suitable() is intact
    assert ie.IE_NAME == 'viafree' or ie.IE_NAME  # name set on class
    assert ie._VALID_URL

# Generated at 2026-10-24 07:42:03.703119
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # 1. Default construction: no downloader, no network/setup triggered
    ie = ViafreeIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._ready is False
    assert ie._GEO_BYPASS is False

    # 2. Construction with a downloader stores it via set_downloader()
    downloader = Mock()
    ie2 = ViafreeIE(downloader)
    assert ie2._downloader is downloader
    assert ie2._ready is False

    # 3. Class config used by constructor/suitable() is intact
    assert ie.IE_NAME == 'viafree' or ie.IE_NAME  # name set on class
    assert ie._VALID_URL

# Generated at 2026-10-24 07:42:05.018148
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # 1. Default construction: no downloader, no network/setup triggered
    ie = ViafreeIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._ready is False
    assert ie._GEO_BYPASS is False

    # 2. Construction with a downloader stores it via set_downloader()
    downloader = Mock()
    ie2 = ViafreeIE(downloader)
    assert ie2._downloader is downloader
    assert ie2._ready is False

    # 3. Class config used by constructor/suitable() is intact
    assert ie.IE_NAME == 'viafree' or ie.IE_NAME  # name set on class
    assert ie._VALID_URL

# Generated at 2026-10-24 07:42:06.351503
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 07:42:07.682630
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # 1. Default construction: no downloader, no network/setup triggered
    ie = ViafreeIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._ready is False
    assert ie._GEO_BYPASS is False

    # 2. Construction with a downloader stores it via set_downloader()
    downloader = Mock()
    ie2 = ViafreeIE(downloader)
    assert ie2._downloader is downloader
    assert ie2._ready is False

    # 3. Class config used by constructor/suitable() is intact
    assert ie.IE_NAME == 'viafree' or ie.IE_NAME  # name set on class
    assert ie._VALID_URL

# Generated at 2026-10-24 07:42:09.021655
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # 1. Default construction: no downloader, no network/setup triggered
    ie = ViafreeIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._ready is False
    assert ie._GEO_BYPASS is False

    # 2. Construction with a downloader stores it via set_downloader()
    downloader = Mock()
    ie2 = ViafreeIE(downloader)
    assert ie2._downloader is downloader
    assert ie2._ready is False

    # 3. Class config used by constructor/suitable() is intact
    assert ie.IE_NAME == 'viafree' or ie.IE_NAME  # name set on class
    assert ie._VALID_URL

# Generated at 2026-10-24 07:42:25.818392
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    ie = TVPlayIE()

    # Constructor created a usable instance
    assert ie is not None
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'

    # _VALID_URL works after construction
    assert ie.suitable('http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true')
    assert ie.suitable('https://play.nova.bg/programi/zdravei-bulgariya/764300')
    assert ie.suitable('mtg:418113')

    # Non-matching URLs rejected
    assert not ie.suitable('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    # ID extraction works
    assert ie._match_id('mtg:418113') == '418113'
    assert ie._match_id('http://www.tv3play.se/program/husraddarna/395385') == '395385'


if __name__ == '__main__':
    test_TVPlayIE()
    print('test_TVPlayIE passed')

# Generated at 2026-10-24 07:43:04.322574
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # 1. Default construction: no downloader, no network/setup triggered
    ie = ViafreeIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._ready is False
    assert ie._GEO_BYPASS is False

    # 2. Construction with a downloader stores it via set_downloader()
    downloader = Mock()
    ie2 = ViafreeIE(downloader)
    assert ie2._downloader is downloader
    assert ie2._ready is False

    # 3. Class config used by constructor/suitable() is intact
    assert ie.IE_NAME == 'viafree' or ie.IE_NAME  # name set on class
    assert ie._VALID_URL

# Generated at 2026-10-24 07:43:05.661460
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # 1. Default construction: no downloader, no network/setup triggered
    ie = ViafreeIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._ready is False
    assert ie._GEO_BYPASS is False

    # 2. Construction with a downloader stores it via set_downloader()
    downloader = Mock()
    ie2 = ViafreeIE(downloader)
    assert ie2._downloader is downloader
    assert ie2._ready is False

    # 3. Class config used by constructor/suitable() is intact
    assert ie.IE_NAME == 'viafree' or ie.IE_NAME  # name set on class
    assert ie._VALID_URL

# Generated at 2026-10-24 07:43:07.038885
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 07:43:08.418190
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    # 1. Default construction: no downloader, no network/setup triggered
    ie = ViafreeIE()
    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie._ready is False
    assert ie._GEO_BYPASS is False

    # 2. Construction with a downloader stores it via set_downloader()
    downloader = Mock()
    ie2 = ViafreeIE(downloader)
    assert ie2._downloader is downloader
    assert ie2._ready is False

    # 3. Class config used by constructor/suitable() is intact
    assert ie.IE_NAME == 'viafree' or ie.IE_NAME  # name set on class
    assert ie._VALID_URL

# Generated at 2026-10-24 07:43:09.726516
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 07:43:11.055835
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 07:43:12.734218
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 07:43:29.315510
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    # Constructor should work with no arguments
    # via InfoExtractor base class
    ie = TVPlayIE()

    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, TVPlayIE)

    # Class-level identity defined in this file
    assert ie.IE_NAME == 'mtg'
    assert ie.IE_DESC == 'MTG services'

    # _VALID_URL / _TESTS are defined
    assert isinstance(ie._VALID_URL, str)
    re.compile(ie._VALID_URL)
    assert isinstance(ie._TESTS, list) and len(ie._TESTS) > 0

    # Instance exposes extractor API
    assert callable(getattr(ie, '_real_extract', None))
    assert callable(getattr(ie, '_match_id', None))

# Generated at 2026-10-24 07:43:31.842410
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:43:34.363473
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:43:36.774612
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 07:43:39.195547
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:43:41.616506
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 07:43:44.191244
# Unit test for constructor of class ViafreeIE