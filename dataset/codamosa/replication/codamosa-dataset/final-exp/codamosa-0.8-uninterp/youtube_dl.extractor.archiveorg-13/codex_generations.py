

# Generated at 2022-06-14 16:03:06.374935
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'


# Generated at 2022-06-14 16:03:09.262877
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # Create an instance of ArchiveOrgIE for testing purposes
    ie = ArchiveOrgIE(None)
    assert hasattr(ie, 'IE_NAME') and ie.IE_NAME == 'archive.org'


# Generated at 2022-06-14 16:03:19.306160
# Unit test for constructor of class ArchiveOrgIE

# Generated at 2022-06-14 16:03:20.255383
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE

# Generated at 2022-06-14 16:03:22.348131
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    "Tests that ArchiveOrgIE can be constructed."

    # Constructor of ArchiveOrgIE requires no parameters
    assert ArchiveOrgIE

# Generated at 2022-06-14 16:03:23.825361
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE('archive.org', 'archive.org videos')

# Generated at 2022-06-14 16:03:25.270568
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert(isinstance(ArchiveOrgIE(), InfoExtractor))

# Generated at 2022-06-14 16:03:32.191034
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # Testing a simple URL
    ArchiveOrgIE('http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    # Testing a URL with embed at the beginning
    ArchiveOrgIE('http://archive.org/embed/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    # Testing a URL with a trailing forward slash
    ArchiveOrgIE('http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect/')
    # Testing a URL with a trailing forward slash and embed at the beginning
    ArchiveOrgIE('http://archive.org/embed/XD300-23_68HighlightsAResearchCntAugHumanIntellect/')

# Generated at 2022-06-14 16:03:33.653163
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'

# Generated at 2022-06-14 16:03:34.732026
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()

# Generated at 2022-06-14 16:03:50.695919
# Unit test for constructor of class ArchiveOrgIE

# Generated at 2022-06-14 16:03:55.389382
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # Test for issue https://github.com/rg3/youtube-dl/issues/8502
    # Test for issue https://github.com/rg3/youtube-dl/issues/9463
    assert ArchiveOrgIE._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:03:57.707475
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    try:
        ArchiveOrgIE()
    except:
        print("Unit test for constructor of class ArchiveOrgIE failed!")

# Generated at 2022-06-14 16:03:59.388108
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    constructor_test(ArchiveOrgIE)


# Generated at 2022-06-14 16:04:01.606551
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    obj = ArchiveOrgIE()
    assert obj.IE_NAME == 'archive.org'
    assert obj.IE_DESC == 'archive.org videos'

# Generated at 2022-06-14 16:04:11.736671
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    try:
        from cStringIO import StringIO
    except ImportError:
        from io import BytesIO as StringIO
    try:
        from collections import OrderedDict
    except ImportError:
        from ordereddict import OrderedDict
    from .common import _fake_extract

    def _help_test(cls, obj):
        assert len(str(obj).split('\n')) > 1
        return obj

    _help_test(ArchiveOrgIE('archive.org', 'archive.org'), ArchiveOrgIE('archive.org', 'archive.org'))

    _help_test(ArchiveOrgIE('archive.org', 'archive.org'), ArchiveOrgIE('archive.org', 'archive.org'))


# Generated at 2022-06-14 16:04:18.133950
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    infoExtractor = ArchiveOrgIE()
    assert(infoExtractor._VALID_URL ==
           r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)')
    assert(infoExtractor.IE_NAME == 'archive.org')
    assert(infoExtractor.IE_DESC == 'archive.org videos')

# Generated at 2022-06-14 16:04:20.028443
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE("XD300-23_68HighlightsAResearchCntAugHumanIntellect")

# Generated at 2022-06-14 16:04:21.652321
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    '''
    Test ArchiveOrgIE constructor
    '''
    ie = ArchiveOrgIE()

# Generated at 2022-06-14 16:04:25.122814
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE()._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'


# Generated at 2022-06-14 16:04:39.545855
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    """Constructor of class ArchiveOrgIE"""
    test1 = {'url': 'https://archive.org/details/MSNBCW_20131125_040000_To_Catch_a_Predator/', 'only_matching': True}
    test2 = {'url': 'http://archive.org/embed/XD300-23_68HighlightsAResearchCntAugHumanIntellect', 'only_matching': True}    
    _TESTS.append(test1)
    _TESTS.append(test2)
    ie = ArchiveOrgIE()
    ie.suitable('https://archive.org/details/MSNBCW_20131125_040000_To_Catch_a_Predator/')

# Generated at 2022-06-14 16:04:45.140868
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    """
    This function checks to see if ArchiveOrgIE constructor
    raises an exception when an invalid url is passed

    :raises ValueError

    """
    with pytest.raises(ValueError):
        ArchiveOrgIE('archive.org/deatils/XD300-23_68HighlightsAResearchCntAugHumanIntellect')

# Generated at 2022-06-14 16:04:48.171743
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    extractor = ArchiveOrgIE()
    assert extractor.IE_NAME == 'archive.org'
    assert extractor.IE_DESC == 'archive.org videos'
    assert extractor._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'


# Generated at 2022-06-14 16:04:48.899890
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie

# Generated at 2022-06-14 16:04:50.171872
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == "archive.org"

# Generated at 2022-06-14 16:04:51.664919
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # without installation of youtube_dl
    ie = ArchiveOrgIE()

# Generated at 2022-06-14 16:04:56.565760
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.name == 'archive.org'
    assert ie.description == 'archive.org videos'
    assert ie.ie_key() == 'archive.org'
    assert ie.file_id_key() == 'id'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:04:58.164447
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    info_extractor = ArchiveOrgIE()


# Generated at 2022-06-14 16:04:58.744792
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:05:00.781437
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()


# Generated at 2022-06-14 16:05:14.913690
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie._TESTS[0]['url'] == ie.IE_NAME + ':' + ie._TESTS[0]['url']


# Generated at 2022-06-14 16:05:25.163539
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:05:29.071130
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # This plugin should pass 7 test cases
    import doctest
    doctest.testmod(optionflags=doctest.IGNORE_EXCEPTION_DETAIL)

if __name__ == '__main__':
    test_ArchiveOrgIE()

# Generated at 2022-06-14 16:05:34.210333
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE.IE_NAME == 'archive.org'
    assert ArchiveOrgIE.IE_DESC == 'archive.org videos'
    assert ArchiveOrgIE._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'


# Generated at 2022-06-14 16:05:34.836649
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:05:36.424468
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = InfoExtractor(ArchiveOrgIE)
    for _ in ie._TESTS:
        pass

# Generated at 2022-06-14 16:05:38.959635
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'

# Generated at 2022-06-14 16:05:50.648077
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == 'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:06:00.775407
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert_equal(ie.ie_key(), 'archive.org')
    assert_equal(ie.IE_NAME, 'archive.org')
    assert_equal(ie.IE_DESC, 'archive.org videos')
    assert_equal(ie._VALID_URL, r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)')
    assert_equal(ie._TESTS[0]['url'], 'http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    assert_equal(ie._TESTS[0]['md5'], '8af1d4cf447933ed3c7f4871162602db')

# Generated at 2022-06-14 16:06:01.297705
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:06:28.497849
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'

# Generated at 2022-06-14 16:06:29.485066
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    obj = ArchiveOrgIE()
    return obj

# Generated at 2022-06-14 16:06:30.706560
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert isinstance(ArchiveOrgIE(), InfoExtractor)

# Generated at 2022-06-14 16:06:31.636091
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:06:32.282545
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ...

# Generated at 2022-06-14 16:06:42.315556
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    ie._parse_jwplayer_data('<div id="player">[{"sources":[{"file":"http://example.com/test.mp4"}]}]</div>', 'test')
    ie._parse_html5_media_entries('http://archive.org/details/test', '<video src="http://example.com/test.mp4"></video>', 'test')
    ie._parse_json('<div id="player">[{"sources":[{"file":"http://example.com/test.mp4"}]}]</div>', 'test', fatal=False)
    ie._parse_json([{"sources":[{"file":"http://example.com/test.mp4"}]}], 'test', fatal=False)

# Generated at 2022-06-14 16:06:44.628712
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'

# Generated at 2022-06-14 16:06:55.704272
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    video_id = 'XD300-23_68HighlightsAResearchCntAugHumanIntellect' 
    webpage = ie._download_webpage(
        'http://archive.org/embed/' + video_id, video_id)

    playlist = None
    play8 = ie._search_regex(
        r'(<[^>]+\bclass=["\']js-play8-playlist[^>]+>)', webpage,
        'playlist', default=None)
    if play8:
        attrs = extract_attributes(play8)
        playlist = attrs.get('value')

# Generated at 2022-06-14 16:07:04.021194
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    aoi = ArchiveOrgIE()
    assert aoi._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:07:07.172087
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE('archive.org', 'archive.org videos')
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'

# Generated at 2022-06-14 16:08:15.369184
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    global sri_international, buster_keaton, tv_show

# Generated at 2022-06-14 16:08:19.932727
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    archiveOrg = ArchiveOrgIE()
    archiveOrg.ie_key = "ArchiveOrg"
    archiveOrg.ie_slug = "archiveorg"
    archiveOrg.ie_code = IE_ArchiveOrg
    return archiveOrg

ie = test_ArchiveOrgIE()

# Generated at 2022-06-14 16:08:21.443030
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    try:
        ArchiveOrgIE()
    except:
        raise Exception("Unit test failure on ArchiveOrgIE() constructor!")

# Generated at 2022-06-14 16:08:29.574552
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():

    # 1. url = 'https://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    args = ['https://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect']
    kwargs = {}
    archiveorg = ArchiveOrgIE(*args, **kwargs)
    assert isinstance(archiveorg, ArchiveOrgIE)

    encoded_url = 'https%3A%2F%2Farchive.org%2Fdetails%2FXD300-23_68HighlightsAResearchCntAugHumanIntellect'
    assert archiveorg._download_webpage('http://archive.org/embed/' + encoded_url, 'XD300-23_68HighlightsAResearchCntAugHumanIntellect') is not None
    assert archiveorg

# Generated at 2022-06-14 16:08:30.839074
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE('archive.org')
    ie.IE_NAME

# Generated at 2022-06-14 16:08:42.286592
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    title = '1968 Demo - FJCC Conference Presentation Reel #1'
    assert ie._match_id(ie._VALID_URL % {'id': 'XD300-23_68HighlightsAResearchCntAugHumanIntellect'}) == 'XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    assert ie._match_id(ie._VALID_URL % {'id': 'MSNBCW_20131125_040000_To_Catch_a_Predator'}) == 'MSNBCW_20131125_040000_To_Catch_a_Predator'

# Generated at 2022-06-14 16:08:42.891808
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:08:44.859064
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_DESC == 'archive.org videos'

# Generated at 2022-06-14 16:08:45.825942
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()

# Generated at 2022-06-14 16:08:47.133033
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    """Unit test for constructor of class ArchiveOrgIE"""
    ArchiveOrgIE()

# Generated at 2022-06-14 16:11:04.001887
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    """test ArchiveOrgIE class constructor"""
    tester = "ArchiveOrgIE"
    archiveOrgIE = ArchiveOrgIE()

# Generated at 2022-06-14 16:11:14.118644
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    from .test_common import make_test_video_url  # pylint: disable=import-error
    from .test_common import make_test_playlist_url  # pylint: disable=import-error
    import tempfile
    import os
    import shutil
    import subprocess
    def make_test_archive(filename):
        with open(filename, 'w'):
            pass
    def make_test_movies(dname):
        dname = os.path.join(dname, 'movies')
        os.mkdir(dname)
        make_test_archive(os.path.join(dname, 'ArchiveTest.ogv'))
        make_test_archive(os.path.join(dname, 'ArchiveTest.mp4'))

# Generated at 2022-06-14 16:11:16.403288
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    inst = ArchiveOrgIE()
    assert inst.ie_key() == 'archive.org'
    assert inst.ie_desc() == 'archive.org videos'
    assert inst.ie_name() == 'archive.org'

# Generated at 2022-06-14 16:11:17.326278
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert(ArchiveOrgIE)

# Generated at 2022-06-14 16:11:17.932886
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE(): pass

# Generated at 2022-06-14 16:11:18.926943
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    info_extractor = ArchiveOrgIE()



# Generated at 2022-06-14 16:11:20.213652
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    ie.IE_NAME
    ie.IE_DESC

# Generated at 2022-06-14 16:11:21.646443
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    i = ArchiveOrgIE()
    assert i
    assert str(i).find("ArchiveOrgIE") > -1

# Generated at 2022-06-14 16:11:24.563362
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    i = ArchiveOrgIE()
    assert i.IE_NAME == 'archive.org'
    assert i.IE_DESC == 'archive.org videos'
    assert i._VALID_URL == 'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:11:25.390601
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE
