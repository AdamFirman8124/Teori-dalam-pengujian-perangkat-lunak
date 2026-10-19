

# Generated at 2022-06-14 16:03:02.991634
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert isinstance(ie, InfoExtractor)

# Generated at 2022-06-14 16:03:05.566592
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    print(ie.__class__)
    print(ie.__class__.__bases__)

# Generated at 2022-06-14 16:03:08.846819
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    test_ArchiveOrgIE = ArchiveOrgIE()
    if test_ArchiveOrgIE.IE_NAME != 'archive.org':
        return 'IE name is not archive.org: %s' % test_ArchiveOrgIE.IE_NAME
    return True

# Generated at 2022-06-14 16:03:09.414466
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:03:19.402245
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    mock_download_webpage = ExtractorMock.mock_download_webpage
    mock_download_webpage.expect_call(
        'http://archive.org/embed/XD300-23_68HighlightsAResearchCntAugHumanIntellect',
        'XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    mock_download_json = ExtractorMock.mock_download_json
    mock_download_json.expect_call(
        'http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect',
        'XD300-23_68HighlightsAResearchCntAugHumanIntellect',
        {'output': 'json'})
    # Test ArchiveOrgIE.__init__(), ArchiveOrgIE._real_ext

# Generated at 2022-06-14 16:03:21.350198
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE("ArchiveOrg")
    return True


# Generated at 2022-06-14 16:03:23.275818
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    obj = ArchiveOrgIE()
    assert obj.IE_NAME == 'archive.org'


# Generated at 2022-06-14 16:03:31.523546
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    """Unit test for constructor of class ArchiveOrgIE"""
    ie = ArchiveOrgIE()
    # Test a valid url
    url = "https://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect"
    info = ie.extract(url)
    assert info['id'] == "XD300-23_68HighlightsAResearchCntAugHumanIntellect"
    assert info['uploader'] == "SRI International"
    assert info['title'] == "1968 Demo - FJCC Conference Presentation Reel #1"
    assert info['release_date'] == "19681210"
    assert info['upload_date'] == "20100315"
    assert info['description'] == "SRI International"
    assert info['creator'] == "SRI International"
    # Test a invalid url


# Generated at 2022-06-14 16:03:33.803658
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert hasattr(ie, 'geo_verification_proxy')


# Generated at 2022-06-14 16:03:36.310276
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie._VALID_URL == ie.VALID_URL
    assert ie._TESTS == ie.TESTS

# Generated at 2022-06-14 16:03:50.040611
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    ie.IE_NAME
    ie.IE_DESC
    (ie._VALID_URL)

# Generated at 2022-06-14 16:03:51.808252
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    """Test module ArchiveOrgIE"""
    temp = ArchiveOrgIE()
    assert temp is not None

# Generated at 2022-06-14 16:03:52.689731
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert 'archives' == ArchiveOrgIE().ie_key()

# Generated at 2022-06-14 16:03:55.349822
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    result = ArchiveOrgIE().extract('https://archive.org/details/MSNBCW_20131125_040000_To_Catch_a_Predator/')

# Generated at 2022-06-14 16:03:56.026568
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:04:01.374126
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == ArchiveOrgIE.IE_NAME
    assert ie.IE_DESC == ArchiveOrgIE.IE_DESC
    assert repr(ie)
    assert ie._VALID_URL == ArchiveOrgIE._VALID_URL
    assert ie._TESTS == ArchiveOrgIE._TESTS

# Generated at 2022-06-14 16:04:09.735108
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.ie_key() == 'archive.org'
    assert ie.ie_desc() == 'archive.org videos'
    assert ie.valid_url('http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    assert ie.valid_url('https://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    assert ie.valid_url('https://archive.org/embed/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    assert ie.valid_url('https://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect/')

# Generated at 2022-06-14 16:04:21.702371
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    url = 'http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    id = 'XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    inst = ArchiveOrgIE(None)
    inst._real_extract(url)
    assert inst.IE_NAME == 'archive.org'
    assert inst._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'
    assert inst._TESTS[0]['url'] == url
    assert inst._TESTS[0]['md5'] == '8af1d4cf447933ed3c7f4871162602db'

# Generated at 2022-06-14 16:04:22.671685
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()

# Generated at 2022-06-14 16:04:34.106617
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    # TODO: ssl not supported by the current build of wget on travis
    #assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'
    #assert ie._TESTS == [{
    #    'url': 'http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect',
    #    'md5': '8af1d4cf447933ed3c7f4871162602db',
    #    'info_dict': {
    #        'id': 'XD300-

# Generated at 2022-06-14 16:04:59.393590
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE().extract('https://archive.org/details/test_video')
    assert ArchiveOrgIE().extract('http://archive.org/details/test_video')

# Generated at 2022-06-14 16:05:10.244523
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'
    assert ie._TESTS[0]['url'] == 'http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    assert ie._TESTS[0]['md5'] == '8af1d4cf447933ed3c7f4871162602db'
    assert ie._TESTS[0]['info_dict']['id'] == 'XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    assert ie._TESTS[0]['info_dict']['ext'] == 'ogg'
    assert ie

# Generated at 2022-06-14 16:05:19.802698
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    instance = ArchiveOrgIE()
    assert instance._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:05:22.900376
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    a = ArchiveOrgIE()
    url = 'http://archive.org/embed/mothradiohour_pod_2013-01-18T16_19_27-08_00'
    a._real_extract(url)

# Generated at 2022-06-14 16:05:27.948795
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE().IE_NAME == 'archive.org'
    assert ArchiveOrgIE().IE_DESC == 'archive.org videos'
    assert ArchiveOrgIE()._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:05:32.773270
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    class_name = ArchiveOrgIE.__name__
    archive_org = globals()[class_name]()
    assert class_name == archive_org.ie_key()
    assert archive_org.ie_key() == 'ArchiveOrg'
    assert archive_org.extractor_key == 'archive.org'

# Generated at 2022-06-14 16:05:33.694454
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()._real_initialize()

# Generated at 2022-06-14 16:05:35.049086
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    """
    Construction test of class ArchiveOrgIE
    """
    ie = ArchiveOrgIE()

# Generated at 2022-06-14 16:05:35.446274
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:05:36.469159
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    if ie._NAME != 'archive.org':
        raise ValueError('Something went wrong!')

# Generated at 2022-06-14 16:06:25.301570
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    ie.IE_NAME

# Generated at 2022-06-14 16:06:26.274353
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:06:30.955060
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
	global ie 
	ie = ArchiveOrgIE()
	video_id = ie._match_id("http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect")
	assert video_id == "XD300-23_68HighlightsAResearchCntAugHumanIntellect" 


# Generated at 2022-06-14 16:06:41.265116
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE('test', 'test')
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'
    assert ie._TESTS[0]['url'] == 'http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    assert ie._TESTS[0]['md5'] == '8af1d4cf447933ed3c7f4871162602db'
    assert ie._TESTS[1]['url'] == 'https://archive.org/details/Cops1922'
    assert ie._TESTS[1]['md5'] == '0869000b4ce265e8ca62738b336b268a'

# Generated at 2022-06-14 16:06:42.315513
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE().IE_NAME

# Generated at 2022-06-14 16:06:44.326141
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    try:
        ArchiveOrgIE()
    except TypeError as e:
        raise Exception(e)

# Generated at 2022-06-14 16:06:45.142179
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE(None)

# Generated at 2022-06-14 16:06:46.816340
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    instance = ArchiveOrgIE()
    assert instance.ie_key() == 'archive.org'

# Generated at 2022-06-14 16:06:57.473014
# Unit test for constructor of class ArchiveOrgIE

# Generated at 2022-06-14 16:07:04.178152
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie.__name__ == 'archive.org'
    assert ie.supported_extensions() == ['3gp', 'avi', 'flv', 'm4a', 'm4v', 'mkv', 'mov', 'mp3', 'mp4', 'ogv', 'ogx', 'ogg', 'wav', 'webm']

# Generated at 2022-06-14 16:09:10.974913
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'Archive.Org videos'

# Generated at 2022-06-14 16:09:14.802430
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:09:16.620103
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE(None, None).IE_NAME == "archive.org"
    assert ArchiveOrgIE(None, None).IE_DESC == "archive.org videos"

# Generated at 2022-06-14 16:09:18.129837
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    class_name = "ArchiveOrgIE"
    obj = globals()[class_name]()
    obj.ie_key()

test_ArchiveOrgIE()

# Generated at 2022-06-14 16:09:29.518300
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    test_ArchiveOrgIE.playlist = None
    test_ArchiveOrgIE.url = None
    test_ArchiveOrgIE.page = None
    test_ArchiveOrgIE.info = None

    # Default constructor of class ArchiveOrgIE
    def __init__(self):
        pass

    # constructor with values of class ArchiveOrgIE
    test_ArchiveOrgIE.playlist = '{}'
    test_ArchiveOrgIE.url = 'https://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    test_ArchiveOrgIE.id = ArchiveOrgIE._match_id(test_ArchiveOrgIE.url)
    # test_ArchiveOrgIE.page = self._download_webpage(
    #     'http://archive.org/embed/' + test

# Generated at 2022-06-14 16:09:30.301611
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert isinstance(ArchiveOrgIE(), ArchiveOrgIE)

# Generated at 2022-06-14 16:09:41.810460
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE.suitable('archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    assert ArchiveOrgIE.suitable('archive.org/embed/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    assert ArchiveOrgIE.suitable('https://archive.org/details/MSNBCW_20131125_040000_To_Catch_a_Predator/')
    assert not ArchiveOrgIE.suitable('https://archive.org/details/MSNBCW_20131125_040000_To_Catch_a_Predator')
    assert not ArchiveOrgIE.suitable('https://archive.org/details/MSNBCW_20131125_040000_To_Catch_a_Predator/filedesc.xml')

# Unit

# Generated at 2022-06-14 16:09:43.476908
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # Test for the "videoId" variable for being a string
    assert(type("videoId") == str)

# Generated at 2022-06-14 16:09:51.916198
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE('http://archive.org/~details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    assert(ie._download_webpage_method == 'http_get')
    assert(ie._VALID_URL == 'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)')

# Generated at 2022-06-14 16:09:52.613632
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE

# Generated at 2022-06-14 16:12:19.229915
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
  # Test for second argument: _downloader
  # Its value will be passed to InfoExtractor constructor
  # None is default value, it means that downloader = None
  ie_test = ArchiveOrgIE(None, None)

  # Test for return of method _download_webpage
  # The method takes three arguments:
  # url - string, page to download
  # video_id - string, id of video
  # note - string, description of error (default value: None)
  # The method returns an object of class 'compat_urllib_request.Request'
  # Request has entities - headers and data
  # If method return None, it means that error was ocurred
  url_test = 'http://archive.org/details/test'
  webpage_test = ie_test._download_webpage(url_test, 'test')

# Generated at 2022-06-14 16:12:29.098644
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # extract video with multiple subtitles
    video_id = "AmigaWDTVLIVE"

# Generated at 2022-06-14 16:12:36.659317
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:12:39.280262
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    unit_test_obj = ArchiveOrgIE()
    assert unit_test_obj._VALID_URL == 'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:12:48.270243
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # Base class test cases
    ie = ArchiveOrgIE()
    ie_obj = ie.ie_key()
    assert ie_obj == ArchiveOrgIE, "Object not an instance of class ArchiveOrgIE"
    assert ie.ie_desc() == 'archive.org videos'
    assert ie.ie_name() == "archive.org"
    assert ie.valid_url("http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect") == True
    assert ie.valid_url("https://archive.org/details/Cops1922") == True
    assert ie.valid_url("http://archive.org/embed/XD300-23_68HighlightsAResearchCntAugHumanIntellect") == True

# Generated at 2022-06-14 16:12:49.827052
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # Test the constructor of class ArchiveOrgIE
    _ = ArchiveOrgIE(None, None)

# Generated at 2022-06-14 16:12:52.019541
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # test that class constructor works and creates an instance of ArchiveOrgIE
    archive = ArchiveOrgIE()
    assert isinstance(archive, ArchiveOrgIE)
