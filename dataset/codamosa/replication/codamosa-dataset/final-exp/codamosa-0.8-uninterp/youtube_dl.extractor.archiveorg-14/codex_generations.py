

# Generated at 2022-06-14 16:03:00.818651
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    test_object = ArchiveOrgIE()
    assert test_object._VALID_URL == 'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'


# Generated at 2022-06-14 16:03:01.706288
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:03:12.082652
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    obj = ArchiveOrgIE()
    # test constructor of class ArchiveOrgIE
    assert obj._VALID_URL == ArchiveOrgIE._VALID_URL
    assert obj._TESTS == ArchiveOrgIE._TESTS
    # test constructor functions of class InfoExtractor
    assert obj._downloader == None
    assert obj._working_dir_spec == None
    assert obj._download_retcode == None
    assert obj._num_downloads == None
    assert obj._ies == None
    assert obj._pps == None
    assert obj._progress_hooks == None
    assert obj._download_counter == None
    assert obj._downloader == None
    assert obj._working_dir_spec == None
    assert obj._download_retcode == None
    assert obj._num_downloads == None
    assert obj._ies == None
    assert obj._pps

# Generated at 2022-06-14 16:03:14.660871
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    ie.set_downloader(None)
    ie.ie_key()
    assert ie.ie_key() == 'archive.org'



# Generated at 2022-06-14 16:03:17.441826
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:03:21.798346
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    print("testing ArchiveOrgIE with URL: %s" % ie.IE_DESC)
    assert("archive.org" in ie.IE_NAME)
    assert("archive.org" in ie.IE_DESC)
    assert("archive.org" in ie._VALID_URL)
    assert("archive.org" in ie._TESTS[0]['url'])
    assert("archive.org" in ie._TESTS[1]['url'])
    assert("archive.org" in ie._TESTS[2]['url'])
    assert("archive.org" in ie._TESTS[3]['url'])
    print("testing ArchiveOrgIE - done")

# Generated at 2022-06-14 16:03:24.964292
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie
    assert ie._VALID_URL == ArchiveOrgIE._VALID_URL
    assert ie._TESTS == ArchiveOrgIE._TESTS



# Generated at 2022-06-14 16:03:25.571521
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:03:26.578727
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    a = ArchiveOrgIE()

# Generated at 2022-06-14 16:03:30.798856
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    from .test_html5 import test_html5_media_info
    from .generic import GenericIE

    i = GenericIE.construct(test_html5_media_info['url'])
    assert isinstance(i, ArchiveOrgIE)

# Generated at 2022-06-14 16:03:41.980417
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    info = ArchiveOrgIE()
    assert ArchiveOrgIE.IE_NAME == info.ie_key()

# Generated at 2022-06-14 16:03:48.923413
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    """Unit test for ArchiveOrgIE."""
    from urllib2 import urlopen

    from .test_common_args import temp_filename

    # Create a fake URL for testing.
    url = 'http://test.test/test.test?test=test'

    # Construct an object.
    ie = ArchiveOrgIE(url)

    # Assert that the constructor sets the object's URL and query attributes
    # correctly.
    assert ie.url == url
    assert ie.query == 'test=test'

    # Assert that the constructor opens a connection to the URL and reads the
    # data.
    ie = ArchiveOrgIE(urlopen(url))

    # Assert that the constructor sets the object's URL and data attributes
    # correctly.
    assert ie.url == url
    assert ie.data == 'test'

    # Create an

# Generated at 2022-06-14 16:03:54.247506
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    video_id = 'XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    archie = ArchiveOrgIE()
    video_webpage = 'http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    archie._download_webpage(video_webpage, video_id)
    print(archie)

# Generated at 2022-06-14 16:03:56.768654
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
	ie = ArchiveOrgIE(None, {}, None)
	assert(isinstance(ie, ArchiveOrgIE))


# Generated at 2022-06-14 16:04:06.864944
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:04:19.253029
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # The original source
    video = "https://archive.org/details/MSNBCW_20131125_040000_To_Catch_a_Predator/"
    # The video should be extracted with ID "MSNBCW_20131125_040000_To_Catch_a_Predator"
    video_id = "MSNBCW_20131125_040000_To_Catch_a_Predator"
    # The video_id should be valid for the following URLs

# Generated at 2022-06-14 16:04:22.099056
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    infoExtractor = ArchiveOrgIE()
    assert infoExtractor.IE_NAME == 'archive.org'
    assert infoExtractor.IE_DESC == 'archive.org videos'

# Generated at 2022-06-14 16:04:33.117538
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE.IE_NAME == 'archive.org'
    assert ArchiveOrgIE.IE_DESC == 'archive.org videos'
    ie = ArchiveOrgIE()
    test_url = 'https://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    expected_output = 'XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    actual_output = ie._match_id(test_url)
    assert expected_output == actual_output
    test_url = 'http://archive.org/details/Cops1922'
    expected_output = 'Cops1922'
    actual_output = ie._match_id(test_url)
    assert expected_output == actual_output

# Generated at 2022-06-14 16:04:34.062578
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE().IE_NAME

# Generated at 2022-06-14 16:04:34.974195
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    archive_org_ie = ArchiveOrgIE()

# Generated at 2022-06-14 16:04:55.699171
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    aorg = ArchiveOrgIE()

# Generated at 2022-06-14 16:04:57.979285
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # TODO: Call the constructor of ArchiveOrgIE, and check that it works
    raise NotImplementedError

# Generated at 2022-06-14 16:04:58.920592
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ar = ArchiveOrgIE ()

# Generated at 2022-06-14 16:05:06.141016
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.ie_key() == 'archive.org'
    assert ie.ie_desc() == 'archive.org videos'
    assert ie.http_headers() == {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'
    }


# Generated at 2022-06-14 16:05:07.907204
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    """Test for constructor of class ArchiveOrgIE"""
    assert ArchiveOrgIE('www.archive.org') is not None

# Generated at 2022-06-14 16:05:17.181814
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:05:21.636971
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:05:32.995760
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE('archive.org')
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'
    assert len(ie._TESTS) == 4
    assert ie._TESTS[3]['url'] == 'https://archive.org/details/MSNBCW_20131125_040000_To_Catch_a_Predator/'
    assert ie._TESTS[3]['only_matching'] == True
    assert len(ie._TESTS[0]['info_dict']) == 13

# Generated at 2022-06-14 16:05:35.729870
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    #TODO: Add more tests for ArchiveOrgIE
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'

# Generated at 2022-06-14 16:05:43.650255
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    import extractor
    ie = extractor.gen_extractor_classes()['archive.org']()
    url = "http://archive.org/embed/XD300-23_68HighlightsAResearchCntAugHumanIntellect"
    webpage = ie._download_webpage(url, "XD300-23_68HighlightsAResearchCntAugHumanIntellect")
    attrs = extract_attributes(webpage)
    assert(attrs['class'] == 'js-play8-playlist')
    assert(attrs['value'] is not None)

# Generated at 2022-06-14 16:06:06.776571
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    # just a sanity check
    assert ie.IE_NAME == 'archive.org'
    # just make sure there's no exceptions thrown
    assert ie._VALID_URL

# Generated at 2022-06-14 16:06:09.062593
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE.IE_DESC == 'archive.org videos'
    assert ArchiveOrgIE.IE_NAME == 'archive.org'

# Generated at 2022-06-14 16:06:09.924410
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()

# Generated at 2022-06-14 16:06:17.611605
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    m = ArchiveOrgIE()
    assert m.IE_NAME == 'archive.org'
    assert m.IE_DESC == 'archive.org videos'
    assert m._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:06:18.725674
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.ie_key() == 'archive.org'

# Generated at 2022-06-14 16:06:21.363512
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    test_instance = ArchiveOrgIE()
    assert test_instance._VALID_URL == 'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:06:24.293545
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert(ie.IE_NAME == 'archive.org')
    assert(ie.IE_DESC == 'archive.org videos')

# Generated at 2022-06-14 16:06:28.286248
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:06:39.078038
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    from .common import InfoExtractor
    from .test_common import _get_mock_config, _search_regex
    from .youtube_playlists import YoutubePlaylist
    from .youtube_dl.utils import JsonMessageParserError
    from .youtube_dl.extractor import get_info_extractor

    # Test for old JW player
    info_extractor = get_info_extractor(
        ArchiveOrgIE.ie_key(), {})
    ie = info_extractor(
        YoutubePlaylist.url_result(
            'http://archive.org/embed/XD300-23_68HighlightsAResearchCntAugHumanIntellect',
            'http://archive.org/embed/XD300-23_68HighlightsAResearchCntAugHumanIntellect'))

# Generated at 2022-06-14 16:06:46.445553
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():

    testVideo = "https://archive.org/details/Cops1922"
    expected = { 
            'id': 'Cops1922', 
            'ext': 'mp4', 
            'title': "Buster Keaton's \"Cops\" (1922)",
            'description': 'md5:43a603fd6c5b4b90d12a96b921212b9c',
            'timestamp': 1387699629,
            'upload_date': '20131222'
    }
    testVideo1 = "XD300-23_68HighlightsAResearchCntAugHumanIntellect"

# Generated at 2022-06-14 16:07:38.789810
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    def archive_org_ie_test_constrcutor(archive_org_instance):
        assert isinstance(archive_org_instance, ArchiveOrgIE)
        ArchiveOrgIE.__init__(archive_org_instance)
        assert isinstance(archive_org_instance, InfoExtractor)

    archive_org_ie_test_constrcutor(ArchiveOrgIE())

# Generated at 2022-06-14 16:07:43.873772
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie._VALID_URL == "https?://(?:www\\.)?archive\\.org/(?:details|embed)/(?P<id>[^/?#&]+)"

# Generated at 2022-06-14 16:07:48.500329
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie._VALID_URL == ie.IE_NAME.lower() + ':' + ie._VALID_URL
    assert ie.ie_key() == ie.IE_NAME.lower()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'

# Generated at 2022-06-14 16:07:50.972722
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    ie = ArchiveOrgIE(info_extractors={'foo': 'bar'})


# Generated at 2022-06-14 16:07:51.777400
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()



# Generated at 2022-06-14 16:07:52.347048
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:07:54.564744
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    ie = ArchiveOrgIE()
    ie = ArchiveOrgIE()

# Generated at 2022-06-14 16:08:00.880135
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie=ArchiveOrgIE()
    ie.IE_NAME()
    ie.IE_DESC()
    ie._VALID_URL()
    ie._TESTS()
    ie._real_extract()
    ie._parse_html5_media_entries()
    ie._parse_jwplayer_data()
    ie._parse_json()
    ie._download_json()
    ie._download_webpage()
    ie._search_regex()
    ie._match_id()
    ie._html_search_meta()

# Generated at 2022-06-14 16:08:02.321170
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    ie._real_extract('http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')

# Generated at 2022-06-14 16:08:02.842512
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:10:01.456194
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == "archive.org"
    assert ie.IE_DESC == "archive.org videos"
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:10:06.577760
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    my_ie = ArchiveOrgIE()
    # Test the constructor of class ArchiveOrgIE
    assert(my_ie is not None)
    # Test the _real_extract method of class ArchiveOrgIE
    my_ie._real_extract()

if __name__ == '__main__':
    test_ArchiveOrgIE()

# Generated at 2022-06-14 16:10:09.409796
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie._VALID_URL == ie._downloader.troubleshoot.default_regex

# Generated at 2022-06-14 16:10:12.542289
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # Given
    # When
    ie = ArchiveOrgIE()
    # Then
    assert ie.IE_NAME == "archive.org"
    assert ie.IE_DESC == "archive.org videos"

# Generated at 2022-06-14 16:10:13.783681
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    pass


# Generated at 2022-06-14 16:10:21.738603
# Unit test for constructor of class ArchiveOrgIE

# Generated at 2022-06-14 16:10:26.506441
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE('https://archive.org/details/MSNBCW_20131125_040000_To_Catch_a_Predator/')
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:10:27.281108
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()

# Generated at 2022-06-14 16:10:35.691534
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    archiveorg_ie = ArchiveOrgIE('archiveorg')
    ie_object = archiveorg_ie.ie_obj()
    assert (ie_object._VALID_URL == 'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)')

# Generated at 2022-06-14 16:10:38.302025
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    archivorg_inst = ArchiveOrgIE()