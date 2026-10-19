

# Generated at 2022-06-14 16:03:04.419239
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    from .common import InfoExtractor, expected_warnings
    from ..compat import compat_HTTPError

    ie = ArchiveOrgIE()

    assert ie.ie_key() == 'archive.org'
    assert ie.ie_name() == 'archive.org videos'

    # Valid URL
    info = ie.extract('https://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')

# Generated at 2022-06-14 16:03:05.058242
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    return ArchiveOrgIE()

# Generated at 2022-06-14 16:03:06.167561
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
	y = ArchiveOrgIE()

# Generated at 2022-06-14 16:03:10.451824
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie._VALID_URL == ie.VALID_URL
    assert ie._TESTS == ie.TESTS
    assert ie.__name__ == 'archive.org'
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'

# Generated at 2022-06-14 16:03:13.507154
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    """Constructor should init fields."""
    ie = ArchiveOrgIE()

    # Assert that _VALID_URL was registered.
    assert ie._VALID_URL == ie.VALID_URL.match(ie._VALID_URL).groupdict()

# Generated at 2022-06-14 16:03:14.963599
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert type(ArchiveOrgIE({})) == ArchiveOrgIE

# Generated at 2022-06-14 16:03:25.720710
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE("archiveorg")
    dest = (ie.IE_NAME, ie.IE_DESC, ie._VALID_URL, ie._TESTS)

# Generated at 2022-06-14 16:03:30.339098
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    if ie:
        raise Exception("Object %s cannot be instantiated without IE name and description" % repr(ie))
    ie = ArchiveOrgIE("IE_NAME", "IE_DESC")
    if ie.ie_name() != "IE_NAME" or ie.ie_desc() != "IE_DESC":
        raise Exception("Object %s cannot be constructed with IE name and description" % repr(ie))

# Generated at 2022-06-14 16:03:31.679448
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE('')

# Generated at 2022-06-14 16:03:32.106930
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:03:44.462076
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    instance = ArchiveOrgIE()
    assert isinstance(instance, ArchiveOrgIE)

# Generated at 2022-06-14 16:03:45.950239
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE({})

# Test def _real_extract(self, url)

# Generated at 2022-06-14 16:03:51.647249
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    test_class = ArchiveOrgIE()
    assert test_class.IE_NAME == 'archive.org'
    assert sorted(test_class.IE_DESC) == sorted('archive.org videos')
    assert test_class._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:03:55.345285
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    from .common import InfoExtractor

    ie = InfoExtractor()

    ie.add_info_extractor(ArchiveOrgIE)

    ie.extract("http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect")

# Generated at 2022-06-14 16:03:56.030234
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE()

# Generated at 2022-06-14 16:04:03.274312
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE('http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    expected_output = "http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect"
    assert ie._url == expected_output
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:04:04.208182
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    i = ArchiveOrgIE()

# Generated at 2022-06-14 16:04:11.822273
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    from .common import InfoExtractor

    root_ie = InfoExtractor(None, None)
    ie = ArchiveOrgIE(root_ie)


# Generated at 2022-06-14 16:04:16.207006
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE("https://archive.org/details/MSNBCW_20131125_040000_To_Catch_a_Predator/")

if __name__ == "__main__":
    test_ArchiveOrgIE()

# Generated at 2022-06-14 16:04:18.022377
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'

# Generated at 2022-06-14 16:04:39.435366
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE()

# Generated at 2022-06-14 16:04:47.209346
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # first argument is a url while the second argument is the expected result
    expected_results = [
        ("http://www.archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect",
         "XD300-23_68HighlightsAResearchCntAugHumanIntellect"),
    ]


# Generated at 2022-06-14 16:04:54.822265
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    def extract(url):
        return ArchiveOrgIE()._real_extract(url)

    assert extract('https://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    assert extract('http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    assert extract('https://archive.org/embed/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    assert extract('http://archive.org/embed/XD300-23_68HighlightsAResearchCntAugHumanIntellect')


# Generated at 2022-06-14 16:04:55.833216
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()

# Generated at 2022-06-14 16:05:00.569737
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    yt = ArchiveOrgIE()
    assert(yt.ie_key() == 'archive.org')
    assert(yt.ie_desc() == 'archive.org videos')
    assert(yt.ie_name() == 'archive.org')

# Generated at 2022-06-14 16:05:01.619573
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert 'archive.org' not in IE_DESCS

# Generated at 2022-06-14 16:05:09.137443
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # Set up unittest
    options = {
        'quiet': True,
        'no_warnings': True,
    }
    creator = unittest.TestSuite()
    creator.addTest(unittest.TestLoader().loadTestsFromTestCase(ArchiveOrgIE))
    runner = unittest.TextTestRunner(resultclass=unittest.TestResult)
    result = runner.run(creator)
    if not result.wasSuccessful():
        print("ERROR: ArchiveOrgIE failed tests")
        sys.exit(1)


# Generated at 2022-06-14 16:05:12.964660
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ao = ArchiveOrgIE()
    assert (ao.IE_NAME == "archive.org")
    assert (ao.IE_DESC == "archive.org videos")
    assert (ao._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)')

# Generated at 2022-06-14 16:05:15.704509
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie._VALID_URL == 'https?://(?:www\\.)?archive\\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:05:16.626186
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    x = ArchiveOrgIE()

# Generated at 2022-06-14 16:05:40.451987
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    try:
        url = 'http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect'
        ie = ArchiveOrgIE(url)
        assert ie != None
    except:
        assert False


# Generated at 2022-06-14 16:05:50.007210
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    archive = ArchiveOrgIE()
    assert archive.IE_NAME == 'archive.org'
    assert archive.IE_DESC == 'archive.org videos'
    assert archive._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'
    assert archive.test_url == 'https://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    assert archive.test_md5 == '8af1d4cf447933ed3c7f4871162602db'

# Generated at 2022-06-14 16:05:51.058511
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie

# Generated at 2022-06-14 16:05:55.742131
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE('')
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'

# Generated at 2022-06-14 16:05:57.523047
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie._VALID_URL == ArchiveOrgIE._VALID_URL

# Generated at 2022-06-14 16:05:59.129726
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    obj = ArchiveOrgIE()
    assert obj._VALID_URL is not None

# Generated at 2022-06-14 16:06:01.156438
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    url = 'http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    assert ArchiveOrgIE._VALID_URL == 'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:06:01.688559
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:06:07.071624
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE('archive.org')
    assert ie.ie_key() == 'archive.org'
    assert ie.ie_desc() == 'archive.org videos'
    assert ie.url_re() == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'



# Generated at 2022-06-14 16:06:13.515477
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    """Unit test for constructor of class ArchiveOrgIE"""
    # valid URL
    archiveOrgIE = ArchiveOrgIE('archive.org', 'XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    assert archiveOrgIE is not None, 'archiveOrgIE must not be none'

    # invalid URL
    invalidURLIE = ArchiveOrgIE('archive.org', 'XD300-23_68HighlightsAResearchCntAugHumanIntellect2')
    assert invalidURLIE is None, 'invalidURLIE must be none'

# Generated at 2022-06-14 16:07:05.999516
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == 'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'
    assert ie._TESTS[1]['url'] == 'https://archive.org/details/Cops1922'
    assert ie._TESTS[1]['md5'] == '0869000b4ce265e8ca62738b336b268a'

# Generated at 2022-06-14 16:07:09.695929
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    url = "https://www.archive.org/embed/XD300-23_68HighlightsAResearchCntAugHumanIntellect"
    ie_objects = ArchiveOrgIE._get_ie(url)
    assert ie_objects.ie_key() == 'archive.org'

# Generated at 2022-06-14 16:07:14.125475
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:07:17.610982
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    """test constructor of class ArchiveOrgIE"""
    url_test = "http://archive.org/details/Cops1922"
    obj = ArchiveOrgIE(url_test)
    assert obj._VALID_URL == "https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)"

# Generated at 2022-06-14 16:07:21.764056
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    test_url = 'http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    test_obj = ArchiveOrgIE()
    test_obj.initialize()
    test_obj.extract(test_url)

# Generated at 2022-06-14 16:07:22.900342
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ieTest = ArchiveOrgIE()

# Generated at 2022-06-14 16:07:24.008764
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE(None)

# Generated at 2022-06-14 16:07:25.234629
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    url = 'contexturl'
    ArchiveOrgIE(url)

# Generated at 2022-06-14 16:07:32.351001
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert(ie.name == 'archive.org')
    assert(ie.description == 'archive.org videos')
    assert(ie.valid_url('https://archive.org/details/Cops1922'))
    assert(not ie.valid_url('https://archive.org/details/'))
    assert(not ie.valid_url('https://archive.org/details'))
    assert(not ie.valid_url('https://archive.org/details/MSNBCW_20131125_040000_To_Catch_a_Predator/'))

# Generated at 2022-06-14 16:07:34.524102
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # No warning when constructed with no parameters
    assert ArchiveOrgIE()

# Generated at 2022-06-14 16:09:42.690026
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    """Unit test for ArchiveOrgIE"""

    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'

if __name__ == '__main__':
    test_ArchiveOrgIE()

# Generated at 2022-06-14 16:09:43.770251
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # Test a constructor of ArchiveOrgIE class
    assert True

# Generated at 2022-06-14 16:09:45.897460
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():

    from .extractor import class_for_url

    result = class_for_url(ArchiveOrgIE._VALID_URL)
    assert result == ArchiveOrgIE

# Generated at 2022-06-14 16:09:51.252569
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
	ie = ArchiveOrgIE()
	print (ie._TESTS)
	assert ie._TESTS[0]['url'] == 'http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect'
	print (ie._TESTS)
	assert ie._TESTS[2]['url'] == 'http://archive.org/embed/XD300-23_68HighlightsAResearchCntAugHumanIntellect'

# Generated at 2022-06-14 16:09:51.978889
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    video = ArchiveOrgIE()
    assert video

# Generated at 2022-06-14 16:09:53.277960
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:09:59.312870
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    res = ie.extract('https://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    assert res['id'] == 'XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    assert res['ext'] == 'ogg'
    assert res['title'] == '1968 Demo - FJCC Conference Presentation Reel #1'
    assert res['creator'] == 'SRI International'
    assert res['release_date'] == '19681210'
    assert res['uploader'] == 'SRI International'
    assert res['timestamp'] == 1268695290

# Generated at 2022-06-14 16:10:05.597396
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
	ie = ArchiveOrgIE('archive.org','http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect','68HighlightsAResearchCntAugHumanIntellect')
	print(ie.name)
	print(ie.ie_key())
	print(ie.url)
	print(ie.video_id)

if __name__ == '__main__':
	test_ArchiveOrgIE()

# Generated at 2022-06-14 16:10:09.159742
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    try:
        ArchiveOrgIE()
    except AssertionError as e:
        assert False, "Failed to create ArchiveOrgIE. The reason is: '{0}'".format(e.message)

# Generated at 2022-06-14 16:10:15.717074
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    html = '<div class="jw8-playlist-wrapper" data-playlist="file://xyz/jw8-playlist.json" data-player="Bx1bxbXd9"></div>'
    playlist = ie._search_regex('(<[^>]+\bclass=["\']js-play8-playlist[^>]+>)', html, 'playlist', default=None)