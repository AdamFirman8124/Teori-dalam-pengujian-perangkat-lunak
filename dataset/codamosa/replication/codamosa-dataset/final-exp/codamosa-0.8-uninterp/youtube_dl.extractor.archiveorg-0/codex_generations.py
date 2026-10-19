

# Generated at 2022-06-14 16:03:02.698194
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    instance = ArchiveOrgIE()
    instance.suitable('http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    instance.suitable('https://archive.org/details/Cops1922')
    instance.suitable('http://archive.org/embed/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    instance.suitable('https://archive.org/details/MSNBCW_20131125_040000_To_Catch_a_Predator/')

# Generated at 2022-06-14 16:03:03.427190
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE()

# Generated at 2022-06-14 16:03:12.867235
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    info = ie._real_extract('http://archive.org/embed/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    assert info['id'] == 'XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    assert info['title'] == '1968 Demo - FJCC Conference Presentation Reel #1'

# Generated at 2022-06-14 16:03:14.765024
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    """Test ArchiveOrgIE's constructor"""
    try:
        ArchiveOrgIE(None)
    except TypeError:
        pass

# Generated at 2022-06-14 16:03:25.521559
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    import re
    from six import assertRegex
    # Testing for multiple use cases of URL
    # Test case 1: Video: Sample_MTS_video_file.mp4
    url = 'https://archive.org/details/Sample_MTS_video_file.mp4'
    # Test case 2: Video: Cops1922
    url = 'https://archive.org/details/Cops1922'
    # Test case 3: Video: XD300-23_68HighlightsAResearchCntAugHumanIntellect
    url = 'http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    # Test case 4: Playlist: MSNBCW_20131125_040000_To_Catch_a_Predator

# Generated at 2022-06-14 16:03:26.840303
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE(None).IE_NAME == ArchiveOrgIE.IE_NAME

# Generated at 2022-06-14 16:03:35.322546
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    test_cases = [
        {"url": "https://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect"},
        {"url": "http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect"},
        ]
    for case in test_cases:
        result = ArchiveOrgIE()._real_extract(case["url"])
        assert(result["id"] == 'XD300-23_68HighlightsAResearchCntAugHumanIntellect')

# Generated at 2022-06-14 16:03:45.131431
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ytdl = YoutubeDL()
    ytdl_opts = ytdl.params.copy()
    # When running the test individually, we need to set the correct path for FFmpeg
    ytdl_opts['ffmpeg_location'] = 'C:\\ffmpeg\\bin\\ffmpeg.exe' if sys.platform == 'win32' else 'ffmpeg'

    constructor_test(
        ArchiveOrgIE,
        {'ytdl_opts': ytdl_opts,
         'ytdl': ytdl,
         'ie_key': 'ArchiveOrg'
        }
    )

if __name__ == '__main__':
    sys.exit(test_ArchiveOrgIE())

# Generated at 2022-06-14 16:03:45.678354
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:03:49.237007
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    archive_org = ArchiveOrgIE()
    archive_org.IE_NAME
    archive_org.IE_DESC
    archive_org._VALID_URL
    archive_org._TESTS

# Generated at 2022-06-14 16:04:00.573747
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # Create an instance of ArchiveOrgIE
    ArchiveOrgIE()

if __name__ == '__main__':
    test_ArchiveOrgIE()

# Generated at 2022-06-14 16:04:05.653742
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE();
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'
    assert ie._TESTS[0]['url'] == 'http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect';


# Generated at 2022-06-14 16:04:06.353660
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE

# Generated at 2022-06-14 16:04:06.941477
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:04:19.305582
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # Test class ArchiveOrgIE
    with open('test/testdata/archive.org/XD300-23_68HighlightsAResearchCntAugHumanIntellect.webpage') as f:
        webpage = f.read().replace('\n', '')
    video_id = 'XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    ie = ArchiveOrgIE()

# Generated at 2022-06-14 16:04:19.933141
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:04:31.577200
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE().IE_NAME == 'archive.org'
    assert ArchiveOrgIE().IE_DESC == 'archive.org videos'
    assert ArchiveOrgIE()._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:04:40.033664
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:04:42.222659
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    try:
        ArchiveOrgIE()
    except:
        assert False, 'Unit test for constructor of class ArchiveOrgIE failed'

# Generated at 2022-06-14 16:04:46.289356
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    video_id = "MSNBCW_20131125_040000_To_Catch_a_Predator"
    url = "https://archive.org/details/"+video_id
    ao = ArchiveOrgIE()
    ao._real_extract(url)

# Generated at 2022-06-14 16:04:57.424218
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:05:04.097465
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    TestArchiveOrgIE = ArchiveOrgIE()
    assert TestArchiveOrgIE._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'
    assert TestArchiveOrgIE.IE_NAME == 'archive.org'
    assert TestArchiveOrgIE.IE_DESC == 'archive.org videos'

# Generated at 2022-06-14 16:05:05.517328
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert 'archive.org' == ArchiveOrgIE('archive.org').ie_key

# Generated at 2022-06-14 16:05:06.560683
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE(object)

# Generated at 2022-06-14 16:05:07.907259
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'

# Generated at 2022-06-14 16:05:09.137561
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'

# Generated at 2022-06-14 16:05:09.714841
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:05:10.677414
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:05:19.670016
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    arg = 'http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    m = ArchiveOrgIE(arg)
    assert m is not None
    assert m.url == arg
    assert m.video_id == 'XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    path = m.ie_key()
    assert path == 'ArchiveOrg'
    assert m.display_id() == 'XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    assert m.description() == 'archive.org videos'
    assert m.webpage_url == 'http://archive.org/embed/XD300-23_68HighlightsAResearchCntAugHumanIntellect'

# Generated at 2022-06-14 16:05:26.816334
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE('http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    ArchiveOrgIE('https://archive.org/details/Cops1922')
    ArchiveOrgIE('http://archive.org/embed/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    ArchiveOrgIE('https://archive.org/details/MSNBCW_20131125_040000_To_Catch_a_Predator/')

# Generated at 2022-06-14 16:05:49.345852
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE().IE_NAME == ArchiveOrgIE.IE_NAME

# Generated at 2022-06-14 16:05:50.352396
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    ie.IE_NAME

# Generated at 2022-06-14 16:05:52.476957
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE('http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')

# Generated at 2022-06-14 16:06:02.149071
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # test_public_video
    ie = ArchiveOrgIE()
    public_video_url = 'http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect'

# Generated at 2022-06-14 16:06:02.815997
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE()

# Generated at 2022-06-14 16:06:06.897610
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:06:08.853661
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE(0)
    assert ie.IE_NAME == 'archive.org'

# Generated at 2022-06-14 16:06:09.476024
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE()

# Generated at 2022-06-14 16:06:11.880291
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == ie.ie_key()
    assert ie.IE_DESC == ie.ie_desc()



# Generated at 2022-06-14 16:06:14.581668
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    """
    This test is to verify that the constructor of class ArchiveOrgIE
    is able to create an instance of it.
    """
    ae = ArchiveOrgIE();
    assert(ae.expect_success());
    return;


# Generated at 2022-06-14 16:07:07.211205
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert 'archive.org' in globals()

# Generated at 2022-06-14 16:07:07.802966
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:07:16.918002
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    t = ArchiveOrgIE()
    assert t.IE_NAME == 'archive.org'
    assert t.IE_DESC == 'archive.org videos'
    assert t._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:07:17.410211
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE()

# Generated at 2022-06-14 16:07:19.768477
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    found = ArchiveOrgIE._WORKING_IE_NAME_RE.search('http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    assert found.group(1) == 'archive.org'

# Generated at 2022-06-14 16:07:21.017182
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    instance = ArchiveOrgIE()
    instance.extract('')

# Generated at 2022-06-14 16:07:24.048719
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # Test url construction
    url= 'http://www.archive.org/details/apollo11-blu-ray'
    ie = ArchiveOrgIE()
    assert ie.suitable(ie._build_url(url))

# Generated at 2022-06-14 16:07:25.274099
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    # import pdb; pdb.set_trace()

# Generated at 2022-06-14 16:07:29.175493
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_DESC == 'archive.org videos'
    assert ie.IE_NAME == 'archive.org'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:07:32.272760
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    """Unit test for constructor of class ArchiveOrgIE"""
    test_obj = ArchiveOrgIE()
    assert test_obj.ie_key() == 'archive.org'

# Generated at 2022-06-14 16:09:36.194284
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE(None)
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'

# Generated at 2022-06-14 16:09:37.066027
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:09:37.640849
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE

# Generated at 2022-06-14 16:09:43.880261
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert hasattr(ie, '_VALID_URL')
    assert hasattr(ie, '_TESTS')
    assert hasattr(ie, '_real_extract')
    assert hasattr(ie, '_parse_json')
    assert hasattr(ie, '_parse_jwplayer_data')
    assert hasattr(ie, '_parse_html5_media_entries')
    assert hasattr(ie, '_download_webpage')


# Generated at 2022-06-14 16:09:52.490410
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    from urllib2 import urlopen
    from urllib import quote
    from urlparse import urlparse
    import sys
    
    methods = [
        'md5',
        'sha1',
        'sha256',
        'sha512',
        'hashlib_md5',
        'hashlib_sha1',
        'hashlib_sha256',
        'hashlib_sha512',
        ]
    
    if sys.version_info >= (2,7):
        methods.append('hashlib_sha3_512')
    
    #video_id = 'https://archive.org/details/' + quote('XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    video_id = 'https://archive.org/details/' + quote('Cops1922.mp4')
   

# Generated at 2022-06-14 16:09:59.765859
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:10:00.858979
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    o = ArchiveOrgIE()
    o.ie_name

# Generated at 2022-06-14 16:10:03.251735
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    '''Test ArchiveOrgIE constructor'''
    t = ArchiveOrgIE()
    assert t.IE_NAME == 'archive.org'

# Generated at 2022-06-14 16:10:03.921414
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE()

# Generated at 2022-06-14 16:10:14.909441
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.ie_key() == 'archive.org'
    assert ie.ie_desc() == 'archive.org videos'
    assert ie.valid_url('http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    assert ie.valid_url('http://archive.org/embed/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    assert ie.valid_url('https://archive.org/details/MSNBCW_20131125_040000_To_Catch_a_Predator/')
    assert not ie.valid_url('https://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect/doesnotexist')