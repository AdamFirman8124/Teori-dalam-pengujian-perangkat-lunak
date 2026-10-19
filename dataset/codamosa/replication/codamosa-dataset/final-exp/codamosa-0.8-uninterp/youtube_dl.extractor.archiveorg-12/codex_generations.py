

# Generated at 2022-06-14 16:03:07.393856
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE()._VALID_URL == 'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'
    assert ArchiveOrgIE().IE_NAME == 'archive.org'
    assert ArchiveOrgIE().IE_DESC == 'archive.org videos'

# Generated at 2022-06-14 16:03:17.313552
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    import xml.etree.ElementTree as ET
    # initializing constructor
    o = ArchiveOrgIE()

    # testing regular expression
    # test one
    url = "http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect"
    assert o._VALID_URL == "https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)"
    assert o._match_id(url) == "XD300-23_68HighlightsAResearchCntAugHumanIntellect"
    # test two
    url = "https://archive.org/details/Cops1922"
    assert o._match_id(url) == "Cops1922"
    # test three

# Generated at 2022-06-14 16:03:21.764205
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # It's impossible to test private variables
    assert isinstance(ArchiveOrgIE()._VALID_URL, str)
    assert isinstance(ArchiveOrgIE().IE_NAME, str)
    assert isinstance(ArchiveOrgIE().IE_DESC, str)


# Generated at 2022-06-14 16:03:22.628341
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # To verify the signature of constructor
    assert callable(ArchiveOrgIE)

# Generated at 2022-06-14 16:03:27.555565
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():

    #Test case 1
    yt_url = 'http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    ie = ArchiveOrgIE(yt_url)
    ie.extract()

    print('Passed all tests')

if __name__ == '__main__':
    test_ArchiveOrgIE()

# Generated at 2022-06-14 16:03:33.605095
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    obj = ArchiveOrgIE(object,"https://archive.org/details/MSNBCW_20131125_040000_To_Catch_a_Predator/")
    assert obj._TESTS[3]['url'] == "https://archive.org/details/MSNBCW_20131125_040000_To_Catch_a_Predator/"

# Generated at 2022-06-14 16:03:34.685782
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()

# Generated at 2022-06-14 16:03:37.294890
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    instance = ArchiveOrgIE()
    pass

# Generated at 2022-06-14 16:03:38.564225
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()

# Generated at 2022-06-14 16:03:38.891728
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:03:51.200209
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    """
    Details of test:
        - constructor of class ArchiveOrgIE
    """
    aorg_ie = ArchiveOrgIE()
    assert aorg_ie.IE_NAME == 'archive.org'
    assert aorg_ie.IE_DESC == 'archive.org videos'
    assert aorg_ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:04:01.943712
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert(ie._VALID_URL == 'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)')

# Generated at 2022-06-14 16:04:03.498295
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    ie.extract(ie._TESTS[0]['url'])

# Generated at 2022-06-14 16:04:11.163858
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    url = 'https://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    ie = ArchiveOrgIE(url)
    assert ie.ie_key() == 'archive.org'
    assert ie.video_id == 'XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    assert ie._VALID_URL == 'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'
    assert ie.params['force_smuggle'] == True
    assert ie.params['smuggle_url'] == 'http://archive.org/smuggle-url/XD300-23_68HighlightsAResearchCntAugHumanIntellect'

# Generated at 2022-06-14 16:04:12.322523
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # Should not raise any exception
    ArchiveOrgIE()

# Generated at 2022-06-14 16:04:13.641172
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()


# Generated at 2022-06-14 16:04:15.585475
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE().IE_NAME == 'archive.org'

# Generated at 2022-06-14 16:04:17.860687
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    try:
        ArchiveOrgIE()
    except Exception as e:
        assert isinstance(e, TypeError)

# Generated at 2022-06-14 16:04:21.601524
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    ie_base = ie.test_test(ie)
    assert ie_base.IE_NAME == 'archive.org'
    assert ie_base.IE_DESC == 'archive.org videos'

# Generated at 2022-06-14 16:04:33.025457
# Unit test for constructor of class ArchiveOrgIE

# Generated at 2022-06-14 16:04:43.791075
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:04:46.246057
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE().IE_NAME == 'archive.org'
    assert ArchiveOrgIE().IE_DESC == 'archive.org videos'

# Generated at 2022-06-14 16:04:55.493784
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE("http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect");
    ArchiveOrgIE("http://archive.org/embed/XD300-23_68HighlightsAResearchCntAugHumanIntellect");
    ArchiveOrgIE("http://archive.org/details/Cops1922");
    ArchiveOrgIE("http://archive.org/embed/Cops1922");
    ArchiveOrgIE("http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect&output=xml");
    ArchiveOrgIE("http://archive.org/embed/XD300-23_68HighlightsAResearchCntAugHumanIntellect&output=xml");

# Generated at 2022-06-14 16:05:01.038902
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE('ArchiveOrg')
try:
    # Check to ensure that the constructor does not throw an exception
    test_ArchiveOrgIE()
    print("Constructor of class ArchiveOrgIE did not throw an exception.")
except:
    print("Constructor of class ArchiveOrgIE threw an exception.")

# Generated at 2022-06-14 16:05:06.417285
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    g = globals()
    # keyword arguments to be passed to the testcase
    # generated by _build_kwargs
    kw = {}
    g['test_ArchiveOrgIE'].__dict__.update(kw)
    test_ArchiveOrgIE.func_code = \
        g['test_ArchiveOrgIE'].__code__

# Generated at 2022-06-14 16:05:14.791570
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():

    url = 'https://archive.org/details/MSNBCW_20131125_040000_To_Catch_a_Predator/'

    result = ArchiveOrgIE()._real_extract(url)

    expected_result = {
        'id': 'MSNBCW_20131125_040000_To_Catch_a_Predator',
        'ext': 'mp4',
        'title': 'To Catch a Predator',
        'description': 'md5:aee1eb3c9b9caf0c6baf57ce1f3bc8bc',
        'creator': 'MSNBC',
        'release_date': '20071014',
        'upload_date': '20131125',
        'timestamp': 1385693622,
        'uploader': 'MSNBC'
    }


# Generated at 2022-06-14 16:05:25.022248
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    wm = ArchiveOrgIE()
    # check for class attributes
    attrs = ['IE_NAME', 'IE_DESC', '_VALID_URL', '_TESTS']
    for attr in attrs:
        assert hasattr(wm, attr) == True, 'hasattr({},{})'.format(wm, attr)
    # check for instance attributes

# Generated at 2022-06-14 16:05:31.561636
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    """
    Test ArchiveOrgIE
    """
    archive_org = ArchiveOrgIE()
    assert archive_org._VALID_URL == "https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)"
    assert archive_org.IE_NAME == 'archive.org'
    assert archive_org.IE_DESC == 'archive.org videos'
    
test_ArchiveOrgIE()

# Generated at 2022-06-14 16:05:32.948459
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    a = ArchiveOrgIE()
    print("Test done")


# Generated at 2022-06-14 16:05:39.619698
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE
    x = ArchiveOrgIE('test', 'http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    x.suitable('http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    x.extract('http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    x._real_extract('http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')

# Generated at 2022-06-14 16:06:01.179404
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # It should not fail if the input is a valid URL
    ArchiveOrgIE().suitable('')

# Generated at 2022-06-14 16:06:04.523344
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    instance = ArchiveOrgIE()
    instance.IE_NAME is not None
    instance.IE_DESC is not None
    instance._VALID_URL is not None
    instance._TESTS is not None
    


# Generated at 2022-06-14 16:06:13.945394
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie._VALID_URL == 'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:06:14.889027
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()


# Generated at 2022-06-14 16:06:15.926797
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # Verify that no exception is thrown when the constructor is executed
    ie = ArchiveOrgIE()

# Generated at 2022-06-14 16:06:18.419439
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    print("\nTesting ArchiveOrgIE class constructor...")
    ie = ArchiveOrgIE()
    assert(ie.IE_NAME == 'archive.org')
    assert(ie.IE_DESC == 'archive.org videos')
    print('done!')


# Generated at 2022-06-14 16:06:24.169094
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # When I call constructor of ArchiveOrgIE, I expect it to create an object.
    # Then I expect it to have a name, a description, and a callback for
    # _real_extract.
    return_value = ArchiveOrgIE()
    assert return_value.IE_NAME == 'archive.org'
    assert return_value.IE_DESC == 'archive.org videos'
    assert return_value._real_extract



# Generated at 2022-06-14 16:06:32.918361
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.suitable('http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    assert ie.suitable('https://archive.org/embed/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    assert not ie.suitable('http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect/')
    assert not ie.suitable('https://archive.org/details/MSNBCW_20131125_040000_To_Catch_a_Predator/')

# Generated at 2022-06-14 16:06:42.860433
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    from .common import InfoExtractor
    from .common import GeoRestrictedError
    from .common import RegexNotFoundError
    from .common import UnsupportedError
    from .common import ExtractorError

    # For test of function that is not related to IE
    assert(hasattr(InfoExtractor, '_sort_formats'))
    assert(hasattr(InfoExtractor, '_search_regex'))
    assert(hasattr(InfoExtractor, '_get_info_dict'))

    ie = InfoExtractor(GeoRestrictedError('Sorry', 'foo'))
    ie = InfoExtractor(RegexNotFoundError('Sorry', 'foo'))
    ie = InfoExtractor(UnsupportedError('Sorry', 'foo'))
    ie = InfoExtractor(ExtractorError('Sorry', 'foo'))
    ie = Info

# Generated at 2022-06-14 16:06:44.443163
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE().IE_NAME == 'archive.org'

# Generated at 2022-06-14 16:07:42.031007
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE('http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    ArchiveOrgIE('https://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    ArchiveOrgIE('https://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect/')
    ArchiveOrgIE('https://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect#39M1')
    ArchiveOrgIE('https://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect?q=foo')

# Generated at 2022-06-14 16:07:42.726314
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    archiveorg_ie = ArchiveOrgIE()

# Generated at 2022-06-14 16:07:47.912047
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    url = 'https://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    info = ArchiveOrgIE().extract(url)
    assert info['id'] == 'XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    assert info['title'] == '1968 Demo - FJCC Conference Presentation Reel #1'
    assert info['description'] == 'md5:da45c349df039f1cc8075268eb1b5c25'
    assert info['creator'] == 'SRI International'
    assert info['release_date'] == '19681210'
    assert info['uploader'] == 'SRI International'
    assert info['timestamp'] == 1268695290
    assert info['upload_date'] == '20100315'
   

# Generated at 2022-06-14 16:07:58.898587
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:08:06.273418
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:08:07.117520
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    return ArchiveOrgIE()

# Generated at 2022-06-14 16:08:11.592874
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:08:13.599969
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE.from_url("https://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect")

# Generated at 2022-06-14 16:08:14.950711
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()


# Generated at 2022-06-14 16:08:16.612970
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
	assert ArchiveOrgIE().IE_NAME == 'archive.org'


# Generated at 2022-06-14 16:10:22.575229
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE(object(), 'https://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    assert ArchiveOrgIE(object(), 'https://archive.org/embed/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    # Some URLs are not resolved successfully
    assert ArchiveOrgIE(object(), 'https://archive.org/details/MSNBCW_20131125_040000_To_Catch_a_Predator/')


# Generated at 2022-06-14 16:10:31.170713
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():

    # This doesn't actually download anything, instead trying to get an
    # ArchiveOrgIE object to see if the constructor is behaving properly and
    # will fail given an invalid URL.

    expected_data = {
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


# Generated at 2022-06-14 16:10:32.189299
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert(isinstance(ArchiveOrgIE({}, {}), InfoExtractor))

# Generated at 2022-06-14 16:10:41.099192
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == 'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:10:44.680583
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ies = ['ArchiveOrgIE()']
    assert ArchiveOrgIE._VALID_URL == 'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'
    assert len(ArchiveOrgIE._TESTS) == 4
    assert len(ies) == 1

# Generated at 2022-06-14 16:10:50.150432
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()

    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'

# Generated at 2022-06-14 16:10:54.674948
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # Test to see if given url is properly parsed by ArchiveOrgIE
    ArchiveOrgIE('http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    # Test for invalid url
    try:
        ArchiveOrgIE('http://www.archive.org/')
    except:
        return True
    return False


# Generated at 2022-06-14 16:10:56.061324
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE("www.archive.org", "archive.org videos", "archive.org")

# Generated at 2022-06-14 16:10:56.837432
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    rs = ArchiveOrgIE()
    assert rs is not None
    print(rs)

# Generated at 2022-06-14 16:10:57.329377
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()