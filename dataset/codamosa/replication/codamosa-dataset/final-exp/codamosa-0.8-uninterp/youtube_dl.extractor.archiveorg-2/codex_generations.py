

# Generated at 2022-06-14 16:03:04.587100
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE.IE_NAME == 'archive.org'


# Generated at 2022-06-14 16:03:06.526770
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    import sys
    import doctest
    doctest.testmod(sys.modules[__name__])

# Generated at 2022-06-14 16:03:07.918630
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    a = ArchiveOrgIE()
    assert a.IE_NAME == 'archive.org'

# Generated at 2022-06-14 16:03:08.900944
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()

# Generated at 2022-06-14 16:03:09.445777
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:03:12.449235
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    inst = ArchiveOrgIE()
    assert inst._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:03:16.962961
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    new_inst = ArchiveOrgIE()

# Generated at 2022-06-14 16:03:18.351065
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # Creation of object - should produce valid result
    ArchiveOrgIE()


# Generated at 2022-06-14 16:03:19.354471
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
        ie = ArchiveOrgIE()

# Generated at 2022-06-14 16:03:29.510908
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()

    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:03:38.385978
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    try:
        ArchiveOrgIE(None)
    except Exception as e:
        print(e)

# Generated at 2022-06-14 16:03:40.493986
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    info_extractor = ArchiveOrgIE()
    print (info_extractor)

# Generated at 2022-06-14 16:03:45.032811
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    """
    Unit test for constructor of ArchiveOrgIE.
    """
    ie = ArchiveOrgIE()
    ie.download("https://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect")
    ie.download("https://archive.org/details/MSNBCW_20131125_040000_To_Catch_a_Predator/")

# Generated at 2022-06-14 16:03:49.239399
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    from .test_cases.test_archiveorg import test_cases

    for test_case in test_cases:
        url = test_case["url"]
        class_inst = ArchiveOrgIE()
        assert class_inst.suitable(url) == test_case["expected"]

# Generated at 2022-06-14 16:03:50.654517
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    test_ArchiveOrgIE()

# Generated at 2022-06-14 16:04:01.325598
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    # Test class constructor
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == 'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

    # Test extraction of all videos in archive.org
    # Database: https://archive.org/advancedsearch.php#raw
    # Download the file "Main collection in the Internet Archive"
    # https://archive.org/download/metadata-main
    # Uncompress it (2.1 GB)
    # Then, run
    # find . -name \*.json | xargs cat | grep '"mediatype": "movies"' | grep '"title": '
    # with

# Generated at 2022-06-14 16:04:10.952584
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    ie.IE_NAME = 'archive.org'
    ie.IE_DESC = 'archive.org videos'
    ie._VALID_URL = r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

    assert ie.suitable(url='http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    assert ie.suitable(url='https://archive.org/details/Cops1922')
    assert ie.suitable(url='http://archive.org/embed/XD300-23_68HighlightsAResearchCntAugHumanIntellect')

# Generated at 2022-06-14 16:04:22.925745
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    url = 'http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    ie = ArchiveOrgIE()
    assert ie._VALID_URL is None
    assert ie._downloader is None
    assert ie.url is None
    assert ie.urls is None
    assert ie.required_files is None
    assert ie.optional_files is None
    assert ie.info_dict is None
    assert ie.params is None
    assert ie.filename is None
    assert ie.to_screen is None
    assert ie.pagedata is None
    assert ie.ie_key() == 'ArchiveOrg'
    assert ie.extractor_key() == 'ArchiveOrg'

# Generated at 2022-06-14 16:04:23.634281
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE();

# Generated at 2022-06-14 16:04:29.640204
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'
    assert ie.ie_key() == 'archive.org'
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'

# Generated at 2022-06-14 16:04:45.396883
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:04:47.846425
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE('http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    assert ie is not None

# Generated at 2022-06-14 16:04:56.550060
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    tester = ArchiveOrgIE()
    assert tester.IE_NAME == "ArchiveOrg"
    assert tester.IE_DESC == "ArchiveOrg videos"
    assert tester._VALID_URL == "https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)"

# Generated at 2022-06-14 16:05:08.166934
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    """Check ArchiveOrgIE constructor"""
    # ArchiveOrgIE should not accept other URLs
    with pytest.raises(AssertionError):
        ArchiveOrgIE('http://www.youtube.com/watch?v=1234567')
    # ArchiveOrgIE should construct the URL
    ie = ArchiveOrgIE('12345')
    assert ie._url == 'https://archive.org/details/12345'
    # ArchiveOrgIE should accept URLs with https
    ie = ArchiveOrgIE('https://archive.org/details/12345')
    assert ie._url == 'https://archive.org/details/12345'
    # ArchiveOrgIE should accept URLs starting with slash
    ie = ArchiveOrgIE('/details/12345')
    assert ie._url == 'https://archive.org/details/12345'
    # ArchiveOrgIE should accept URLs without

# Generated at 2022-06-14 16:05:17.588246
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE('https://archive.org/embed/Cops1922')
    assert ie._VALID_URL == 'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'
    assert ie._TESTS[0]['url'] == 'http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    assert ie._TESTS[0]['md5'] == '8af1d4cf447933ed3c7f4871162602db'
    assert ie._TESTS[0]['info_dict']['id'] == 'XD300-23_68HighlightsAResearchCntAugHumanIntellect'

# Generated at 2022-06-14 16:05:28.157139
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    url = 'http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    test_ArchiveOrgIE = ArchiveOrgIE()
    assert test_ArchiveOrgIE.suitable(url) == True
    assert test_ArchiveOrgIE.IE_NAME == 'archive.org'
    assert test_ArchiveOrgIE.IE_DESC == 'archive.org videos'
    test_ArchiveOrgIE.extract(url)
    assert test_ArchiveOrgIE._VALID_URL == 'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'
    # test_ArchiveOrgIE.test_suitable('http://archive.org/embed/XD300-23_68HighlightsAResearchCnt

# Generated at 2022-06-14 16:05:38.154950
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    # Test normal constructor
    assert(not ie.http_headers)
    assert(ie.ie_key() == 'ArchiveOrg')
    assert(ie.ie_desc() == 'archive.org videos')
    assert(ie.valid_url("http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect") == True)
    assert(ie.valid_url("https://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect") == True)
    assert(ie.valid_url("http://archive.org/details/test_video_1") == True)
    assert(ie.valid_url("https://archive.org/details/test_video_1") == True)

# Generated at 2022-06-14 16:05:50.048377
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    ie.IE_NAME = "archive.org"
    ie.IE_DESC = "archive.org videos"
    ie._VALID_URL = r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:05:51.773393
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie._VALID_URL == ie._TESTS[0]['url']

# Generated at 2022-06-14 16:05:54.461021
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE('archive.org', 'https://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')

# Generated at 2022-06-14 16:06:21.494259
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    url = "http://www.archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect"
    # Constructor of class InfoExtractor
    ie = ArchiveOrgIE()
    # Constructor of class ArchiveOrgIE
    aoie = ArchiveOrgIE(ie.working_dir, url)
    return aoie

# Generated at 2022-06-14 16:06:23.750585
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'


# Generated at 2022-06-14 16:06:34.307063
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # Constructor of class ArchiveOrgIE
    ie = ArchiveOrgIE()

    # test method _build_result()
    info = {
        'id': 'XD300-23_68HighlightsAResearchCntAugHumanIntellect',
        'ext': 'ogg',
        'title': '1968 Demo - FJCC Conference Presentation Reel #1',
        'description': 'md5:da45c349df039f1cc8075268eb1b5c25',
        'creator': 'SRI International',
        'release_date': '19681210',
        'uploader': 'SRI International',
        'timestamp': 1268695290,
        'upload_date': '20100315',
    }
    result, pid = ie._build_result(info)

# Generated at 2022-06-14 16:06:34.897115
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:06:38.789285
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    obj = ArchiveOrgIE()
    assert obj.NAME == IE_NAME
    assert obj.IE_NAME == IE_DESC
    assert obj.VALID_URL == _VALID_URL
    assert obj.TEST == _TESTS


# Generated at 2022-06-14 16:06:41.022536
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    ie._real_extract('http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')

# Generated at 2022-06-14 16:06:45.771071
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    '''
    Unit test for constructor of class ArchiveOrgIE
    '''

    # test for the function _real_extract
    aoie = ArchiveOrgIE()
    info_dict = aoie._real_extract(aoie.ie_key())

    # test for the function _parse_jwplayer_data
    info_dict = aoie._parse_jwplayer_data({aoie.ie_key(): {'playlist': []}}, None, 'http://www.archive.org')

# Generated at 2022-06-14 16:06:54.155371
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    test_obj = ArchiveOrgIE("http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect")
    assert test_obj is not None;
    assert test_obj.__class__ is ArchiveOrgIE;
    assert test_obj.IE_NAME == "archive.org";
    assert test_obj.IE_DESC == "archive.org videos";
    assert test_obj._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)';




# Generated at 2022-06-14 16:07:02.936319
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    def get_test_file(filename):
        test_file_template = '''{
    "test_cases": [
        {
            "expected": {
                "id": "test_id",
                "ext": "test_ext",
                "title": "test_title",
                "description": "test_description",
                "creator": "test_creator",
                "release_date": "test_release_date",
                "uploader": "test_uploader",
                "timestamp": "test_timestamp",
                "upload_date": "test_upload_date",
            },
            "url": "http://archive.org/details/{0}"
        }
    ]
}'''
        return test_file_template.format(filename)

    a = ArchiveOrgIE()
    # Test with a test_

# Generated at 2022-06-14 16:07:07.477642
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    url = 'https://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    x = ArchiveOrgIE()
    x.extract(url)
    assert(x.IE_NAME == 'archive.org')
    assert(x.IE_DESC == 'archive.org videos')

# Generated at 2022-06-14 16:08:06.486291
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:08:07.582543
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

test_ArchiveOrgIE()

# Generated at 2022-06-14 16:08:18.979050
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    import os
    os.environ['LANG'] = 'en_US.UTF-8'    # set environment variable LANG
    module = __import__('ytdl_archiveorg.archiveorg', globals(), locals(), ['ArchiveOrgIE'])
    class_members = dict(inspect.getmembers(module.ArchiveOrgIE))
    assert len(class_members) == 5, 'class ArchiveOrgIE should have 5 members'
    assert 'IE_NAME' in class_members, 'class ArchiveOrgIE should have member IE_NAME'
    assert 'IE_DESC' in class_members, 'class ArchiveOrgIE should have member IE_DESC'
    assert '_VALID_URL' in class_members, 'class ArchiveOrgIE should have member _VALID_URL'

# Generated at 2022-06-14 16:08:20.219667
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE(None)
    assert( ie != None)

# Generated at 2022-06-14 16:08:25.103580
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE('http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')

    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == 'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:08:26.895051
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE != '', 'ArchiveOrgIE class must be defined'

# Generated at 2022-06-14 16:08:28.286037
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie1 = ArchiveOrgIE()
    ie2 = ArchiveOrgIE(125)
    assert ie1 == ie2

# Generated at 2022-06-14 16:08:34.316476
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE(None).extractor_key() == 'archiveorg'
    assert ArchiveOrgIE(None).IE_DESC == 'archive.org videos'
    assert ArchiveOrgIE(None)._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:08:37.782848
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    a = ArchiveOrgIE()
    assert a.IE_NAME == 'archive.org'
    # assert a.IE_DESC == 'archive.org videos'
    assert a.IE_DESC == 'archive.org'

# Generated at 2022-06-14 16:08:39.025852
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'

# Generated at 2022-06-14 16:10:49.548741
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    # Test existence of a downloader in class ArchiveOrgIE
    assert ie.has_downloader()

# Generated at 2022-06-14 16:10:50.949104
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
  ie = ArchiveOrgIE()
  assert ie.IE_NAME == 'archive.org'

# Generated at 2022-06-14 16:10:53.992551
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    """ Unit testing for constructor of class ArchiveOrgIE """
    youtube_ie = ArchiveOrgIE()
    assert youtube_ie.ie_key() == 'ArchiveOrg'
    assert youtube_ie.ie_name() == 'archive.org'

# Generated at 2022-06-14 16:10:58.099001
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE("")
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:11:06.382048
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    c = ArchiveOrgIE()
    c.IE_NAME = 'some browser'
    c.IE_DESC = 'some description'
    c._TESTS = [{
        'url': 'http://archive.org/details/some_id',
        'md5': 'd41d8cd98f00b204e9800998ecf8427e',
        'info_dict': {
            'id': 'some_id',
            'ext': 'mov',
            'title': 'some title',
            'description': 'some description',
            'creator': 'some creator',
            'release_date': '20100101',
            'uploader': 'some uploader',
            'timestamp': 1268695290,
            'upload_date': '20100203',
        }
    }]
    # Test process

# Generated at 2022-06-14 16:11:16.115997
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._TESTS[0]['url'] == 'http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    assert ie._TESTS[0]['md5'] == '8af1d4cf447933ed3c7f4871162602db'
    assert ie._TESTS[0]['info_dict']['id'] == 'XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    assert ie._TESTS[0]['info_dict']['ext'] == 'ogg'

# Generated at 2022-06-14 16:11:24.281901
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    from .common import Options
    options = Options()
    options.merge_dict({'outtmpl': '%(title)s.%(ext)s'})

    ie = ArchiveOrgIE(options)
    assert ie.SCHEME == ['http', 'https']
    assert ie.netrc == True
    assert ie.age_limit == 0
    assert ie.geo_verification_headers == {}
    assert ie.params == {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'noplaylist': True,
    }
    assert ie.IE_NAME == 'archive.org'
    assert ie.ie_key() == 'ArchiveOrg'
    assert ie.IE_DESC == 'archive.org videos'

# Generated at 2022-06-14 16:11:31.327556
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():

    h = ArchiveOrgIE()
    assert h._download_webpage('http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect'
                               , 'XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    assert h._download_webpage('http://archive.org/embed/XD300-23_68HighlightsAResearchCntAugHumanIntellect'
                               , 'XD300-23_68HighlightsAResearchCntAugHumanIntellect')

# Generated at 2022-06-14 16:11:32.810798
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    test = ArchiveOrgIE()
    assert test.constructor('ArchiveOrgIE') is not None

# Generated at 2022-06-14 16:11:33.623839
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    IE = ArchiveOrgIE()