

# Generated at 2022-06-14 16:03:02.356609
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    instance = ArchiveOrgIE()
    expected_name = 'archive.org'
    expected_description = 'archive.org videos'
    assert instance.ie_key() == expected_name
    assert instance.IE_NAME == expected_name
    assert instance.IE_DESC == expected_description

# Generated at 2022-06-14 16:03:05.179667
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'

# Generated at 2022-06-14 16:03:12.220450
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    ie._download_json = lambda *args, **kwargs: {'metadata': {}}
    ie._parse_jwplayer_data = lambda *args, **kwargs: {}

    class DummyIE(object):
        def __init__(self):
            self.ie_key = 'archiveorg'
            self._download_webpage = lambda *args: ''
    ie.add_ie(DummyIE())

    ie.suitable('http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')


# Generated at 2022-06-14 16:03:13.100240
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    from .. import ArchiveOrgIE


# Generated at 2022-06-14 16:03:23.929975
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
	ie = ArchiveOrgIE('http://archive.org/embed/XD300-23_68HighlightsAResearchCntAugHumanIntellect', 'archive.org')
	page = ie.downloader._download_webpage('http://archive.org/embed/XD300-23_68HighlightsAResearchCntAugHumanIntellect', 'XD300-23_68HighlightsAResearchCntAugHumanIntellect')
	assert page is not None
	metadata = ie.downloader._download_json('http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect', 'XD300-23_68HighlightsAResearchCntAugHumanIntellect', query={ 'output': 'json' })['metadata']
	assert metadata is not None
	assert metadata['title'] is not None

# Generated at 2022-06-14 16:03:29.957922
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # Test basic case
    ArchiveOrgIE()

    # Test invalid url
    invalid_url = 'https://vidzi.tv/aoeu.html'
    try:
        ArchiveOrgIE(invalid_url)
    except AssertionError:
        print('caught invalid url exception')

    # Test no idurl
    noid_url = 'https://vidzi.tv/'
    try:
        ArchiveOrgIE(noid_url)
    except RegexNotFoundError:
        print('caught no id exception')



# Generated at 2022-06-14 16:03:39.416433
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():

    # test for parameters of __init__
    ie = ArchiveOrgIE("http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect")
    assert ie.url == "http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect"
    assert ie.video_id == "XD300-23_68HighlightsAResearchCntAugHumanIntellect"

    # test for constructor of InfoExtractor
    ie = ArchiveOrgIE("http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect", InfoExtractor())
    assert ie.url == "http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect"
    assert ie.video_

# Generated at 2022-06-14 16:03:39.986615
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE(None)


# Generated at 2022-06-14 16:03:40.883536
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()

# Generated at 2022-06-14 16:03:41.434961
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:03:48.711341
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'

# Generated at 2022-06-14 16:03:55.689400
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # Test constructor of class ArchiveOrgIE.
    # In the testing part, the test uses the name of class
    # ArchiveOrgIE directly, so the test must be put into
    # the same file with it.
    ie = ArchiveOrgIE()
    # test for method _real_extract()
    ie._real_extract('https://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    ie._real_extract('https://archive.org/details/Cops1922')

# Generated at 2022-06-14 16:03:56.507321
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    return

# Generated at 2022-06-14 16:04:06.750464
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:04:08.335472
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE.__name__ == 'ArchiveOrgIE'

# Generated at 2022-06-14 16:04:11.000221
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    TestClass=ArchiveOrgIE
    TestClass('archive.org')

if __name__ == '__main__':
    test_ArchiveOrgIE()

# Generated at 2022-06-14 16:04:11.620100
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:04:20.173602
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    archiveorg = ArchiveOrgIE()
    url = "https://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect"
    res = archiveorg._real_extract(url)
    assert res['id'] == 'XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    assert res['title'].startswith(
        '1968 Demo - FJCC Conference Presentation Reel #1')
    assert res['description'].startswith("A compilation of four demo movies, from SRI")

# Generated at 2022-06-14 16:04:21.397277
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    i = ArchiveOrgIE()

# Generated at 2022-06-14 16:04:26.465208
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == "archive.org"
    assert ie.IE_DESC == "archive.org videos"
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:04:39.424188
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    i = ArchiveOrgIE()
    assert i._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

test_ArchiveOrgIE()

# Generated at 2022-06-14 16:04:43.139460
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    infoExtractor = ArchiveOrgIE()
    assert infoExtractor._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:04:44.474245
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()


# Generated at 2022-06-14 16:04:49.263972
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    from ..test import _equals

    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:04:53.167866
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    info = ie._real_extract('https://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    assert info['id'] == 'XD300-23_68HighlightsAResearchCntAugHumanIntellect'



# Generated at 2022-06-14 16:04:55.072659
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

## Unit tests for private methods of class ArchiveOrgIE

## Unit tests for public methods of class ArchiveOrgIE

# Generated at 2022-06-14 16:04:56.073540
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
	assert ArchiveOrgIE != None

# Generated at 2022-06-14 16:04:58.341872
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    """ test for constructor of class ArchiveOrgIE"""

    # Constructor of ArchiveOrgIE should have no exception
    ArchiveOrgIE()

# Generated at 2022-06-14 16:05:00.276044
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    obj = ArchiveOrgIE()
    assert obj is not None

# Generated at 2022-06-14 16:05:00.937304
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:05:22.810990
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE('archive.org', 'archive.org videos')

# Generated at 2022-06-14 16:05:25.068840
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
	ArchiveOrgIE()
	return ("Success","Implementation of constructor of class ArchiveOrgIE")


# Generated at 2022-06-14 16:05:35.687141
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    obj = ArchiveOrgIE()
    assert obj._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:05:47.157343
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE();
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:05:47.831395
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:05:50.478300
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'

# Generated at 2022-06-14 16:05:51.198111
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:05:57.480433
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    url = "https://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect"
    video_id = ie._match_id(url)
    webpage = ie._download_webpage(
        'http://archive.org/embed/' + video_id, video_id)
    assert(video_id == 'XD300-23_68HighlightsAResearchCntAugHumanIntellect')

# Generated at 2022-06-14 16:06:04.890247
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    tester = object()
    ie = ArchiveOrgIE(tester)
    assert ie._downloader is tester
    assert ie.ie_key() == 'archive.org'
    assert ie.ie_desc() == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:06:06.694396
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'



# Generated at 2022-06-14 16:06:52.518081
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie._VALID_URL == ie._TESTS[0]['url']

# Generated at 2022-06-14 16:06:55.737980
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'


# Generated at 2022-06-14 16:07:04.053265
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    """Unit test for constructor of class ArchiveOrgIE."""
    
    # URL template for unit test.
    url_temp = "http://archive.org/details/{ID}"

    # Construct a sample test case.
    test_case = (
        "Buster Keaton's Cops",
        "Cops1922",
        "http://archive.org/details/Cops1922",
        "Cops1922",
        "Cops1922",
        "http://www.archive.org/download/Cops1922/Cops1922.mp4",
        "mp4",
        "c8a3df2f3a3a841254b88d23f9e9b21c"
    )

    # Test ArchiveOrgIE constructor.
    ydl = youtube_dl.YoutubeDL({})
    ie

# Generated at 2022-06-14 16:07:14.085462
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:07:15.212599
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'

# Generated at 2022-06-14 16:07:16.027965
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    o = ArchiveOrgIE(InfoExtractor)



# Generated at 2022-06-14 16:07:17.091346
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    ie.IE_NAME



# Generated at 2022-06-14 16:07:18.097864
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    instance = ArchiveOrgIE()
    assert instance.ie_key() == 'archive.org'

# Generated at 2022-06-14 16:07:21.716124
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert isinstance(ie.server_url, str)
    assert ie.server_url != ''

# Test ArchiveOrgIE._real_initialize (called by ArchiveOrgIE.__init__)

# Generated at 2022-06-14 16:07:23.772197
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    ie.browser = ie.get_browser()
    assert ie.browser is not None

# Generated at 2022-06-14 16:09:23.592626
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert isinstance(ArchiveOrgIE(),InfoExtractor)

# Generated at 2022-06-14 16:09:27.012350
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie._downloader == None
    assert ie._working_dir_spec == None
    assert ie._working_dir == None
    assert ie._download_retcode == 0


# Generated at 2022-06-14 16:09:31.522196
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'
    assert ie._TESTS[0]['url'] == 'http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect'

# Generated at 2022-06-14 16:09:33.383096
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()

# Generated at 2022-06-14 16:09:34.869327
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    print(ie)


# Generated at 2022-06-14 16:09:38.088130
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL
    assert ie._TESTS

# Generated at 2022-06-14 16:09:41.811023
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:09:50.613014
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    objIE = ArchiveOrgIE()

    # print objIE
    # print objIE.__dict__
    # print objIE.__class__
    # print objIE.__class__.__bases__[0]
    # print objIE.__class__.__mro__
    # print objIE.__class__.__subclasses__()

    # info
    # print 'URL: ', objIE._VALID_URL
    # print 'IE_NAME: ', objIE.IE_NAME
    # print 'IE_DESC: ', objIE.IE_DESC

    # download
    # objIE._download_webpage('https://www.youtube.com/watch?v=BaW_jenozKc')
    # objIE._download_webpage('https://www.youtube.com/feed/subscriptions?flow=2

# Generated at 2022-06-14 16:09:58.549934
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    sample_url = 'http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    extractor = ArchiveOrgIE()
    assert extractor.IE_NAME == 'archive.org'
    assert extractor.IE_DESC == 'archive.org videos'
    assert extractor._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'
    assert extractor._TESTS[0]['url'] == sample_url
    assert extractor._TESTS[0]['md5'] == '8af1d4cf447933ed3c7f4871162602db'

# Generated at 2022-06-14 16:10:00.727032
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    ie.IE_NAME
    ie.IE_DESC
    ie._VALID_URL
    ie._TESTS