

# Generated at 2022-06-14 16:03:03.739345
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE().init()

# Generated at 2022-06-14 16:03:05.451345
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE().ie_key() == 'archive.org'

# Generated at 2022-06-14 16:03:10.234914
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie._VALID_URL == ArchiveOrgIE._VALID_URL
    assert ie._TESTS == ArchiveOrgIE._TESTS
    assert ie.ie_key() == 'archive.org'
    assert ie.IE_NAME == ArchiveOrgIE.IE_NAME
    assert ie.IE_DESC == ArchiveOrgIE.IE_DESC

# Generated at 2022-06-14 16:03:20.302045
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    webpage = ie._download_webpage(
        'http://archive.org/embed/XD300-23_68HighlightsAResearchCntAugHumanIntellect', 'xd300.23_68highlightsaresearchcntaughumanintellect')
    playlist = ie._search_regex(
        r'(<[^>]+\bclass=["\']js-play8-playlist[^>]+>)', webpage,
        'playlist', default=None)
    meta = extract_attributes(playlist)
    assert ('value', 'https://archive.org/download/XD300-23_68HighlightsAResearchCntAugHumanIntellect/XD300-23_68HighlightsAResearchCntAugHumanIntellect.mp4') in meta.items()

# Generated at 2022-06-14 16:03:29.920021
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    test = ArchiveOrgIE()
    test.IE_NAME
    test.IE_DESC

    # test _valid_url
    url = 'http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    assert 'XD300-23_68HighlightsAResearchCntAugHumanIntellect' == test._match_id(url)

    url = 'http://archive.org/embed/XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    assert 'XD300-23_68HighlightsAResearchCntAugHumanIntellect' == test._match_id(url)

    url = 'https://archive.org/details/MSNBCW_20131125_040000_To_Catch_a_Predator/'

# Generated at 2022-06-14 16:03:36.105161
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    """
    Unit test for constructor of ArchiveOrgIE, showing that if the constructor
    isn't invoked, then attributes won't be created.
    """
    ie = ArchiveOrgIE()
    assert hasattr(ie, '_VALID_URL')
    assert hasattr(ie, 'IE_NAME')
    assert hasattr(ie, 'IE_DESC')
    assert hasattr(ie, '_TESTS')

# Generated at 2022-06-14 16:03:46.009016
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # Test that a video can be played as a video.
    video_url = "https://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect"
    assert "1968 Demo - FJCC Conference Presentation Reel #1" in ArchiveOrgIE(video_url).title()
    # Test that a video can be played as a playlist.
    playlist_url = "https://archive.org/details/FreeBSD_4.4_Release_Party"
    assert "FreeBSD 4.4 Release Party" in ArchiveOrgIE(playlist_url).title()
    # Test that a video is recognized and can be played as a video.
    video_url = "https://archive.org/embed/XD300-23_68HighlightsAResearchCntAugHumanIntellect"

# Generated at 2022-06-14 16:03:46.783905
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:03:48.961738
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    from .test_dl import _set_doc
    _set_doc(ArchiveOrgIE.__doc__)

# Generated at 2022-06-14 16:03:50.313519
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    from .test_archiveorg import test_ArchiveOrgIE

# Generated at 2022-06-14 16:03:57.967719
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE().IE_NAME == 'archive.org'



# Generated at 2022-06-14 16:04:00.453434
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'

# Generated at 2022-06-14 16:04:01.850216
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    print(ie.IE_NAME)

# Generated at 2022-06-14 16:04:03.944344
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'

# Generated at 2022-06-14 16:04:06.586678
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    SetTestMode()
    url = "http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect"
    ie = ArchiveOrgIE()
    ie.extract(url)

# Generated at 2022-06-14 16:04:16.473241
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.ie_key() == 'ArchiveOrg'
    assert ie.ie_name() == 'ArchiveOrg'
    assert ie.ie_description() == 'archive.org videos'
    assert ie.valid_url('http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    assert ie.valid_url('https://archive.org/details/Cops1922')
    assert not ie.valid_url('http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect/')


# Generated at 2022-06-14 16:04:19.461733
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.host == 'archive.org'
    assert ie.name == 'archive.org'
    assert ie.title == 'archive.org videos'

# Generated at 2022-06-14 16:04:20.089049
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:04:26.229062
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == "archive.org"
    assert ie.IE_DESC == "archive.org videos"
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'
    assert len(ie._TESTS) == 4


# Generated at 2022-06-14 16:04:34.326085
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    testcases = [
        'http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect',
        'https://archive.org/details/Cops1922',
        'http://archive.org/embed/XD300-23_68HighlightsAResearchCntAugHumanIntellect',
        'https://archive.org/details/MSNBCW_20131125_040000_To_Catch_a_Predator/',
    ]

    for case in testcases:
        ArchiveOrgIE()._real_extract(case)

# Generated at 2022-06-14 16:04:46.445038
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # Needs to have unicode string, not bytes, as input
    ArchiveOrgIE(b'foo')

# Generated at 2022-06-14 16:04:49.227683
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie._VALID_URL == ie.VALID_URL
    assert ie._TESTS == ie.TESTS

# Generated at 2022-06-14 16:04:54.094883
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'
    assert len(ie._TESTS) > 0


# Generated at 2022-06-14 16:05:06.140635
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:05:07.112611
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert isinstance(ArchiveOrgIE(), ArchiveOrgIE)

# Generated at 2022-06-14 16:05:15.243069
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:05:16.057429
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # Test initialization
    assert ArchiveOrgIE() is not None

# Generated at 2022-06-14 16:05:16.629382
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE()

# Generated at 2022-06-14 16:05:21.909200
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    result = ie.extract('http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    assert 'title' in result
    assert 'description' in result
    assert 'creator' in result
    assert 'release_date' in result
    assert 'uploader' in result
    assert 'timestamp' in result

# Generated at 2022-06-14 16:05:23.088657
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE('archive.org')

# Generated at 2022-06-14 16:05:44.780642
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:05:45.738594
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()

# Generated at 2022-06-14 16:05:54.709812
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # Test _real_extract method of class ArchiveOrgIE
    test_cases = [('http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect'),
                  ('https://archive.org/details/Cops1922'),
                  ('https://archive.org/details/MSNBCW_20131125_040000_To_Catch_a_Predator/')]
    for url in test_cases:
        res = ArchiveOrgIE()._real_extract(url)
        assert res.get('id') == 'XD300-23_68HighlightsAResearchCntAugHumanIntellect'

# Generated at 2022-06-14 16:05:59.578877
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'

# Generated at 2022-06-14 16:06:01.264379
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE()._VALID_URL == ArchiveOrgIE._VALID_URL
    assert ArchiveOrgIE()._TESTS == ArchiveOrgIE._TESTS
    assert ArchiveOrgIE().IE_NAME == ArchiveOrgIE._IE_NAME

# Generated at 2022-06-14 16:06:04.402394
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    info_extractor = ArchiveOrgIE()
    assert info_extractor.ie_key() == 'ArchiveOrg'
    assert info_extractor.ie_desc() == 'archive.org videos'


# Generated at 2022-06-14 16:06:06.610129
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    import youtube_dl.extractor.archiveorg
    archiveorg = youtube_dl.extractor.archiveorg.ArchiveOrgIE()
    assert archiveorg

# Generated at 2022-06-14 16:06:07.484798
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()

# Generated at 2022-06-14 16:06:10.615337
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:06:11.480875
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
	ieObj = ArchiveOrgIE()

# Generated at 2022-06-14 16:07:01.163531
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert isinstance(ie, ArchiveOrgIE)
    #assert validate_guid('XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    #assert validate_guid(ie.__name__)

# Generated at 2022-06-14 16:07:11.213712
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert(ArchiveOrgIE._build_url_result("XD300-23_68HighlightsAResearchCntAugHumanIntellect")
           == "http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect")
    assert(ArchiveOrgIE._build_url_result("XD300-23_68HighlightsAResearchCntAugHumanIntellect", "archive.org/embed/")
           == "http://archive.org/embed/XD300-23_68HighlightsAResearchCntAugHumanIntellect")

# Generated at 2022-06-14 16:07:12.867074
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    IE = ArchiveOrgIE()
    assert(IE.__class__.__name__ == 'ArchiveOrgIE')

# Generated at 2022-06-14 16:07:15.061997
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    ie._real_extract('https://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')

# Generated at 2022-06-14 16:07:19.083173
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    import unittest

    # TODO: Fix tests
    # class FakeInfoExtractor(unittest.TestCase):
    #     def setUp(self):
    #         self._ie = ArchiveOrgIE()
    #     def tests_constructor(self):
    #         self.assertTrue(self._ie)

    # unittest.main(argv=['first-arg-is-ignored'], exit=False)
    # FIXME

# Generated at 2022-06-14 16:07:23.071895
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    url = 'https://archive.org/details/MSNBCW_20131125_040000_To_Catch_a_Predator/'
    assert ArchiveOrgIE._TESTS[2]['url'] == url
    assert ArchiveOrgIE._TESTS[2]['only_matching'] == True

# Generated at 2022-06-14 16:07:32.704508
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # First Test: Test constructor of class ArchiveOrgIE
    TestIE = ArchiveOrgIE()
    assert isinstance(TestIE, InfoExtractor)
    assert TestIE.IE_NAME == 'archive.org'
    assert TestIE.IE_DESC == 'archive.org videos'
    assert TestIE._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:07:34.647140
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert not ArchiveOrgIE()

# Generated at 2022-06-14 16:07:38.006240
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    """
    Simple unit test for the ability to detect class ArchiveOrgIE
    """
    ie = InfoExtractor.ie_key('archive.org')()
    assert isinstance(ie, ArchiveOrgIE)

# Generated at 2022-06-14 16:07:39.536692
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    x = ArchiveOrgIE()
    assert x.IE_NAME == 'archive.org'

# Generated at 2022-06-14 16:09:47.937818
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    archiveOrgIE = ArchiveOrgIE()

# Generated at 2022-06-14 16:09:52.010607
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    # The url must be http://archive.org/details/
    url = 'http://archive.org/details'
    # Test 1: The url is valid:
    assert ie.suitable(url)
    # Test 2: The url is not valid:
    assert not ie.suitable('')



# Generated at 2022-06-14 16:09:57.659204
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # test valid URL
    info = ArchiveOrgIE()._real_extract('http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    assert info['id'] == 'XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    # test invalid URL
    try:
        ArchiveOrgIE()._real_extract('http://archive.org/')
    except Exception as e:
        assert True, 'Expected Exception'

# Generated at 2022-06-14 16:10:09.361395
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # Arrange
    from .common import InfoExtractor
    from .ttvno import TTVNoIE
    from .youtube import YoutubeIE

    class DummyIE(InfoExtractor):
        IE_NAME = 'dummy'
        _VALID_URL = r'https?://(?:www\.)?dummy\.org/'

    class DummySubclass(DummyIE):
        IE_NAME = 'dummy_subclass'

    # Act
    ArchiveOrgIE._ALL_CLASSES = [YoutubeIE, TTVNoIE, ArchiveOrgIE, DummySubclass]
    ArchiveOrgIE._ALL_CLASSES_BY_IE_NAME['dummy'] = [DummyIE]
    ArchiveOrgIE._ALL_CLASSES_BY_IE_NAME['dummy_subclass'] = [DummySubclass]

    # Assert

# Generated at 2022-06-14 16:10:10.371677
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    test = ArchiveOrgIE()
    assert test is not None

# Generated at 2022-06-14 16:10:14.126030
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    class TestArchiveOrgIE (ArchiveOrgIE): pass
    ie = TestArchiveOrgIE()
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, InfoExtractor)
    assert isinstance(ie, InfoExtractor)

# Generated at 2022-06-14 16:10:15.848376
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    ie.set_downloader(None)
    assert ie != None and ie != 0

# Generated at 2022-06-14 16:10:22.853892
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    _download_webpage = lambda *a: (a, '_download_webpage')
    _parse_jwplayer_data = lambda *a: (a, '_parse_jwplayer_data')
    _parse_html5_media_entries = lambda *a: (a, '_parse_html5_media_entries')
    _download_json = lambda *a: (a, '_download_json')

    instance = ArchiveOrgIE()
    instance._download_webpage = _download_webpage
    instance._parse_jwplayer_data = _parse_jwplayer_data
    instance._parse_html5_media_entries = _parse_html5_media_entries
    instance._download_json = _download_json


# Generated at 2022-06-14 16:10:23.881837
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    x = ArchiveOrgIE()
    assert x != None

# Generated at 2022-06-14 16:10:25.136319
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie

