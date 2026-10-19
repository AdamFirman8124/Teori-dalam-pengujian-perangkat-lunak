

# Generated at 2022-06-14 16:03:04.195178
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    IEClass = ArchiveOrgIE
    assert IEClass.__name__ == 'ArchiveOrgIE'
    assert IEClass.IE_NAME == 'archive.org'
    assert IEClass.IE_DESC == 'archive.org videos'
    assert hasattr(IEClass, '_VALID_URL')
    assert IEClass._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'
    assert hasattr(IEClass, '_TESTS')
    assert len(IEClass._TESTS) == 4
    # Check video extracting is working
    video_url = IEClass._TESTS[0]['url']
    video_id = IEClass._match_id(video_url)
    instance = IEClass()
    video_info

# Generated at 2022-06-14 16:03:04.941921
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    pass

# Generated at 2022-06-14 16:03:15.565157
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    """Unit test for ArchiveOrgIE.__init__()."""

    # Test ArchiveOrgIE.__init__() by instantiating an ArchiveOrgIE object.
    #
    # Example:
    #     ArchiveOrgIE(['--video-id=abc-def'])

    test = ArchiveOrgIE(['--video-id=XD300-23_68HighlightsAResearchCntAugHumanIntellect'])
    assert test.ie_key() == 'archive_org'
    assert test.ie_name() == 'archive.org'
    assert test.ie_desc() == 'archive.org videos'
    assert test.start_urls() == ['http://archive.org/embed/XD300-23_68HighlightsAResearchCntAugHumanIntellect']
    assert test.extractor_key() == 'ArchiveOrgIE'

# Generated at 2022-06-14 16:03:16.830033
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'

# Generated at 2022-06-14 16:03:17.745295
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    x = ArchiveOrgIE()

# Generated at 2022-06-14 16:03:19.257464
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    """
    Test constructor of ArchiveOrgIE class
    """
    _ = ArchiveOrgIE()

# Generated at 2022-06-14 16:03:22.081038
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'

# Generated at 2022-06-14 16:03:26.009570
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    info = ArchiveOrgIE()._real_extract(
        'http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    assert info['title'] == '1968 Demo - FJCC Conference Presentation Reel #1'

# Generated at 2022-06-14 16:03:28.212983
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE().IE_NAME == 'archive.org'

# Generated at 2022-06-14 16:03:28.838409
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
	assert ArchiveOrgIE()

# Generated at 2022-06-14 16:03:38.386597
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    """Unit test for class ArchiveOrgIE"""
    test_ArchiveOrgIE.run_test(ArchiveOrgIE)

# Generated at 2022-06-14 16:03:41.178185
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'

# Generated at 2022-06-14 16:03:43.410667
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    if not isinstance(ie, ArchiveOrgIE):
        raise AssertionError("ArchiveOrgIE() doesn't return an instance of ArchiveOrgIE")

# Generated at 2022-06-14 16:03:48.665204
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    import pickle
    with open(r'test.pickle', 'rb') as f:
        test_data = pickle.load(f)
    instance = ArchiveOrgIE()
    result = instance._real_extract(test_data['url'])
    assert result['id'] == test_data['id']
    assert result['description'] == test_data['description']


# Generated at 2022-06-14 16:03:59.656979
# Unit test for constructor of class ArchiveOrgIE

# Generated at 2022-06-14 16:04:00.661344
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    IETest.test_ArchiveOrgIE()

# Generated at 2022-06-14 16:04:01.277063
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    return ArchiveOrgIE()

# Generated at 2022-06-14 16:04:05.218604
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    a = ArchiveOrgIE()
    print(a._download_json('http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect',
                              'XD300-23_68HighlightsAResearchCntAugHumanIntellect')['metadata'])

# Generated at 2022-06-14 16:04:17.919910
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    a = ArchiveOrgIE()
    # Bypass "AttributeError: 'ArchiveOrgIE' object has no attribute '_PROTOCOL_RELATIVE_VALID_URL'"
    a._PROTOCOL_RELATIVE_VALID_URL = a._VALID_URL
    assert a.suitable("https://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect")
    assert a.suitable("https://archive.org/details/Cops1922")
    assert not a.suitable("https://archive.org/details/MSNBCW_20131125_040000_To_Catch_a_Predator/")
    assert a.suitable("http://archive.org/embed/XD300-23_68HighlightsAResearchCntAugHumanIntellect")

# Generated at 2022-06-14 16:04:22.812552
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:04:44.375401
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    obj = ArchiveOrgIE()
    assert obj.IE_NAME == 'archive.org'
    assert obj.IE_DESC == 'archive.org videos'
    assert obj._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:04:54.018568
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:04:57.021782
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE('http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')

# Generated at 2022-06-14 16:04:58.475611
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    ie.ie_key()

# Generated at 2022-06-14 16:05:01.346697
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE("")
    assert ie.IE_DESC == 'archive.org videos'

# Generated at 2022-06-14 16:05:03.912804
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    r = ArchiveOrgIE()
    assert r._check_ie(r.IE_NAME)
    assert r.IE_NAME in r.IE_DESC

# Generated at 2022-06-14 16:05:05.329276
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE("archive.org", "archive.org") == "archive.org"

# Generated at 2022-06-14 16:05:06.572881
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    A = ArchiveOrgIE()
    assert A.IE_NAME == 'archive.org'
    assert A.IE_DESC == 'archive.org videos'



# Generated at 2022-06-14 16:05:07.169165
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
	f = ArchiveOrgIE()

# Generated at 2022-06-14 16:05:07.880357
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    obj = ArchiveOrgIE()
    assert obj

# Generated at 2022-06-14 16:05:34.027775
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    try:
        import jinja2
        from youtube_dl.extractor import gen_extractors_table, list_extractors
        gen_extractors_table(list_extractors(), 'youtube-dl.org')
    except ImportError:
        pass

# Generated at 2022-06-14 16:05:34.661570
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    pass

# Generated at 2022-06-14 16:05:36.923383
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE._VALID_URL == 'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:05:37.462236
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE()

# Generated at 2022-06-14 16:05:39.276145
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'

# Generated at 2022-06-14 16:05:40.458014
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE();
    assert ie.IE_NAME == 'archive.org'

# Generated at 2022-06-14 16:05:41.259816
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:05:46.673964
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    """
    function to test ArchiveOrgIE -> __init__()
    """
    # Test case for ArchiveOrgIE -> __init__()
    # Test False
    ie = ArchiveOrgIE([])
    assert ie.signature == 'archive.org'
    # Test True
    ie = ArchiveOrgIE([])
    assert ie.signature == 'archive.org'

# Generated at 2022-06-14 16:05:57.686431
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE.suitable('http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    assert not ArchiveOrgIE.suitable('http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect/')
    assert not ArchiveOrgIE.suitable('https://archive.org/details/MSNBCW_20131125_040000_To_Catch_a_Predator/')
    assert ArchiveOrgIE.suitable('http://archive.org/embed/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    # Test regular expression of constructor of class ArchiveOrgIE

# Generated at 2022-06-14 16:05:58.962094
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE

# Generated at 2022-06-14 16:06:50.609301
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    try:
        ArchiveOrgIE(None)
        assert False
    except TypeError:
        pass

# Generated at 2022-06-14 16:06:52.841224
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    try:
        ArchiveOrgIE()
    except Exception as e:
        assert False, "Constructor of ArchiveOrgIE failed"

# Generated at 2022-06-14 16:06:54.880871
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    """ Test the constructor of class ArchiveOrgIE """
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == "archive.org"

# Generated at 2022-06-14 16:06:56.590472
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    from . import ArchiveOrgIE
    assert ArchiveOrgIE('archive.org')


# Generated at 2022-06-14 16:07:04.601403
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    from .common import InfoExtractor
    from ..utils import (
        clean_html,
        extract_attributes,
        unified_strdate,
        unified_timestamp,
    )
    ie = InfoExtractor( {'_downloader': None} )

    # test_basic
    test_basic_result_1 = ie._real_extract( 'https://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect' )
    assert( 'id' in test_basic_result_1 )
    assert( 'title' in test_basic_result_1 )
    assert( 'description' in test_basic_result_1 )
    assert( 'creator' in test_basic_result_1 )
    assert( 'release_date' in test_basic_result_1 )

# Generated at 2022-06-14 16:07:14.477326
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE().IE_NAME == 'archive.org'
    assert ArchiveOrgIE().IE_DESC == 'archive.org videos'
    assert ArchiveOrgIE()._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:07:17.905314
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:07:18.784392
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:07:21.403848
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert not ArchiveOrgIE(None)._WORKING  # pylint: disable=protected-access
    assert ArchiveOrgIE("")._WORKING  # pylint: disable=protected-access

# Generated at 2022-06-14 16:07:22.420393
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie_ArchiveOrgIE = ArchiveOrgIE()

# Generated at 2022-06-14 16:09:41.250091
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'

# Generated at 2022-06-14 16:09:43.235905
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'

# Generated at 2022-06-14 16:09:45.710292
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE()._VALID_URL == 'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'


# Generated at 2022-06-14 16:09:47.847347
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # Test for archived video
    ArchiveOrgIE()._real_extract("http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect")

# Generated at 2022-06-14 16:09:48.342743
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE()

# Generated at 2022-06-14 16:09:49.457828
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie= ArchiveOrgIE()
    return ie

# Generated at 2022-06-14 16:09:57.875875
# Unit test for constructor of class ArchiveOrgIE

# Generated at 2022-06-14 16:10:01.103291
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    inst = ArchiveOrgIE(None)

    assert inst._VALID_URL == 'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:10:12.497174
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:10:21.162406
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == ArchiveOrgIE.IE_NAME
    assert ie.IE_DESC == ArchiveOrgIE.IE_DESC
    assert ie._VALID_URL == ArchiveOrgIE._VALID_URL
    assert ie._TESTS == ArchiveOrgIE._TESTS
    assert ie._download == InfoExtractor._download
    assert ie._download_json == InfoExtractor._download_json
    assert ie._download_webpage == InfoExtractor._download_webpage
    assert ie._match_id == InfoExtractor._match_id
    assert ie._parse_jwplayer_data == InfoExtractor._parse_jwplayer_data
    assert ie._parse_html5_media_entries \
        == InfoExtractor._parse_html5_media_entries
    assert ie._search_