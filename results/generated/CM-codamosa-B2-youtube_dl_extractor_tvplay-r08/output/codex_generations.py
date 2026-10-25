

# Generated at 2026-10-24 05:33:20.959888
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 05:33:37.641066
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

# Generated at 2026-10-24 05:33:39.073128
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 05:34:05.495837
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    downloader = object()
    extractor = TVPlayIE(downloader)

    assert isinstance(extractor, TVPlayIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'

# Generated at 2026-10-24 05:34:06.815294
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 05:34:19.225064
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    downloader = object()

    extractor = ViafreeIE(downloader)

    assert isinstance(extractor, ViafreeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False
    assert extractor._GEO_BYPASS is False

# Generated at 2026-10-24 05:34:20.862626
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 05:34:37.342330
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

# Generated at 2026-10-24 05:35:14.513990
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 05:35:19.733763
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():extractor = TVPlayHomeIE()

# Generated at 2026-10-24 05:35:44.094293
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    extractor = TVPlayIE()

    assert isinstance(extractor, TVPlayIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'

# Generated at 2026-10-24 05:35:52.912908
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    extractor = ViafreeIE()

    assert isinstance(extractor, ViafreeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor._ready is False

# Generated at 2026-10-24 05:35:54.225427
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 05:36:04.690024
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    downloader = object()

    extractor = ViafreeIE(downloader)

    assert isinstance(extractor, ViafreeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader

# Generated at 2026-10-24 05:36:06.122455
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 05:36:16.361764
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    ie = ViafreeIE()

    assert isinstance(ie, InfoExtractor)
    assert ie._downloader is None
    assert ie.ie_key() == 'Viafree'
    assert ie._GEO_BYPASS is False
    assert ie.suitable(
        'https://www.viafree.se/program/reality/'
        'sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-1'
    )

# Generated at 2026-10-24 05:36:17.693481
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 05:36:34.385637
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

# Generated at 2026-10-24 05:36:47.493176
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    downloader = object()

    extractor = ViafreeIE(downloader)

    assert isinstance(extractor, ViafreeIE)
    assert extractor._downloader is downloader
    assert extractor._ready is False

# Generated at 2026-10-24 05:36:48.822775
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 05:37:02.374749
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    downloader = object()
    extractor = ViafreeIE(downloader)

    assert isinstance(extractor, ViafreeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.ie_key() == 'Viafree'

# Generated at 2026-10-24 05:37:11.763886
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    downloader = object()
    extractor = ViafreeIE(downloader)

    assert isinstance(extractor, ViafreeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor._ready is False

# Generated at 2026-10-24 05:37:25.239253
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    downloader = object()
    extractor = ViafreeIE(downloader)

    assert isinstance(extractor, ViafreeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader

# Generated at 2026-10-24 05:37:26.558689
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 05:37:29.100032
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 05:37:31.615441
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 05:37:34.031312
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 05:37:36.448854
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 05:37:39.032902
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 05:37:41.450951
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 05:37:43.863245
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 05:37:50.907769
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():extractor = TVPlayHomeIE()

# Generated at 2026-10-24 05:37:52.414873
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 05:38:02.176919
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    extractor = ViafreeIE()

    assert isinstance(extractor, ViafreeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor.ie_key() == 'Viafree'
    assert extractor.suitable(
        'https://www.viafree.se/program/reality/'
        'sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-1'
    )
    assert not extractor.suitable('https://example.com/video/123')

# Generated at 2026-10-24 05:38:11.768614
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    extractor = ViafreeIE()

    assert isinstance(extractor, ViafreeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor.ie_key() == 'Viafree'

# Generated at 2026-10-24 05:38:13.090949
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 05:38:29.444740
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

# Generated at 2026-10-24 05:38:31.951179
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 05:38:34.500052
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 05:38:36.987712
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 05:38:39.528579
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 05:38:41.991619
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 05:38:44.505052
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 05:38:45.876044
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 05:39:10.700321
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    extractor = TVPlayIE()

    assert isinstance(extractor, TVPlayIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'
    assert extractor._match_id('mtg:418113') == '418113'

# Generated at 2026-10-24 05:39:12.010900
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 05:39:28.460692
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

# Generated at 2026-10-24 05:39:30.981792
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 05:39:33.505333
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 05:39:36.026545
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 05:39:38.439960
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 05:39:40.854281
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 05:39:43.273180
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 05:39:59.117399
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

# Generated at 2026-10-24 05:40:24.025213
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    downloader = object()
    extractor = TVPlayIE(downloader)

    assert isinstance(extractor, TVPlayIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is downloader
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'
    assert extractor._match_id('mtg:418113') == '418113'

# Generated at 2026-10-24 05:40:26.441233
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 05:40:28.854908
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 05:40:31.268811
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 05:40:33.685583
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 05:40:36.100532
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 05:40:38.514895
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 05:40:40.927371
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 05:40:43.342482
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 05:40:45.755303
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 05:40:48.168337
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 05:40:50.583516
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 05:40:52.996428
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 05:40:56.168813
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 05:41:02.966177
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():extractor = TVPlayIE()

# Generated at 2026-10-24 05:41:29.713194
# Unit test for constructor of class TVPlayIE
def test_TVPlayIE():
    downloader = object()
    extractor = TVPlayIE(downloader)

    assert isinstance(extractor, TVPlayIE)
    assert extractor._downloader is downloader
    assert extractor.IE_NAME == 'mtg'
    assert extractor.IE_DESC == 'MTG services'

# Generated at 2026-10-24 05:41:31.040296
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():
    ie = TVPlayHomeIE()

    # Constructor works and regex is valid
    assert ie._VALID_URL
    assert ie.IE_NAME == 'TVPlayHome' or ie.IE_NAME

    # Positive matches (all URL variants from the tests)

# Generated at 2026-10-24 05:41:33.457217
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 05:41:35.870827
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 05:41:38.387336
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 05:41:40.803012
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 05:41:43.217526
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 05:41:45.782639
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 05:41:48.287801
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 05:41:50.702363
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 05:41:53.116577
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 05:41:55.531011
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 05:41:57.945102
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 05:42:13.448813
# Unit test for constructor of class TVPlayHomeIE
def test_TVPlayHomeIE():ie = TVPlayHomeIE()

# Generated at 2026-10-24 05:42:24.591557
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    extractor = ViafreeIE()

    assert isinstance(extractor, ViafreeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor._GEO_BYPASS is False
    assert extractor._VALID_URL

# Generated at 2026-10-24 05:42:32.994810
# Unit test for constructor of class ViafreeIE
def test_ViafreeIE():
    extractor = ViafreeIE()

    assert isinstance(extractor, ViafreeIE)
    assert isinstance(extractor, InfoExtractor)
    assert extractor._downloader is None
    assert extractor._ready is False

# Generated at 2026-10-24 05:42:35.410873
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 05:42:37.827038
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 05:42:40.241491
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 05:42:45.348238
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 05:42:47.893851
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 05:42:50.308647
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 05:42:53.269389
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 05:42:55.682329
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 05:42:58.097163
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 05:43:00.513267
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 05:43:02.924554
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 05:43:05.337630
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 05:43:07.766712
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 05:43:10.185263
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 05:43:12.597311
# Unit test for constructor of class TVPlayHomeIE

# Generated at 2026-10-24 05:43:15.010156
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 05:43:17.426191
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 05:43:19.841849
# Unit test for constructor of class TVPlayIE

# Generated at 2026-10-24 05:43:22.257278
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 05:43:24.684393
# Unit test for constructor of class ViafreeIE

# Generated at 2026-10-24 05:43:27.097240
# Unit test for constructor of class ViafreeIE