

# Generated at 2022-06-14 16:03:04.736060
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert len(ArchiveOrgIE()) > 0

# Test the extractor

# Generated at 2022-06-14 16:03:05.408098
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:03:06.783022
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie

# Generated at 2022-06-14 16:03:07.940431
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert isinstance(ArchiveOrgIE(None, None), InfoExtractor)

# Generated at 2022-06-14 16:03:17.876616
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
	# Test instantiation
	ie = ArchiveOrgIE()
	assert isinstance(ie, ArchiveOrgIE)
	# Test case 1
	url = 'http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect'

# Generated at 2022-06-14 16:03:18.620501
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:03:28.964050
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    IE = ArchiveOrgIE()
    from .. import _downloader

    assert isinstance(IE, InfoExtractor)
    assert isinstance(IE, _downloader.InfoExtractor)
    assert hasattr(IE, 'report_download_page')
    assert hasattr(IE, 'MSG_NO_FORMAT')
    assert hasattr(IE, '_real_initialize')
    assert hasattr(IE, '_real_extract')
    assert hasattr(IE, '_download_webpage_handle')
    assert hasattr(IE, '_html_search_meta')
    assert hasattr(IE, '_html_search_regex')
    assert hasattr(IE, '_get_available_subtitles')
    assert hasattr(IE, '_sort_formats')

# Generated at 2022-06-14 16:03:31.607638
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'

# Generated at 2022-06-14 16:03:34.737311
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    search_obj = ArchiveOrgIE({})
    assert search_obj.IE_DESC == 'archive.org videos'
    assert search_obj.IE_NAME == 'archive.org'

# Generated at 2022-06-14 16:03:37.959595
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE('archive.org', 'archive.org videos')

# Generated at 2022-06-14 16:03:51.153236
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE(InfoExtractor())

# Generated at 2022-06-14 16:03:52.397435
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE().ie_key() == 'archive.org'

# Generated at 2022-06-14 16:03:53.274422
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()

# Generated at 2022-06-14 16:03:53.821945
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:03:55.475702
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    info_extractor = ArchiveOrgIE()


# Generated at 2022-06-14 16:03:56.651344
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE();

# Generated at 2022-06-14 16:03:58.428476
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert isinstance(ArchiveOrgIE().ie_key(), str)

# Generated at 2022-06-14 16:04:01.323587
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'

# Generated at 2022-06-14 16:04:02.679504
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    IE = ArchiveOrgIE()
    assert IE.ie_key() == 'archive.org'
    assert IE.ie_desc() == 'archive.org videos'

# Generated at 2022-06-14 16:04:07.640107
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    # Test the regular expression for extracting info from the url
    url = 'https://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    match = ie._VALID_URL.match(url)
    assert match is not None
    assert match.group('id') == 'XD300-23_68HighlightsAResearchCntAugHumanIntellect'

# Generated at 2022-06-14 16:04:33.439132
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # Test successful import of ArchiveOrgIE
    assert ArchiveOrgIE.IE_NAME == 'archive.org'
    assert ArchiveOrgIE.IE_DESC == 'archive.org videos'


# Generated at 2022-06-14 16:04:34.073506
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()

# Generated at 2022-06-14 16:04:41.297455
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    res = ArchiveOrgIE('test', 'http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    assert res.__class__.__name__ == 'ArchiveOrgIE'
    assert res._VALID_URL == 'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'
    assert res._TESTS[0]['md5'] == '8af1d4cf447933ed3c7f4871162602db'

# Generated at 2022-06-14 16:04:44.734399
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # Create instance
    result = ArchiveOrgIE()
    assert(result.IE_NAME == 'archive.org')


if __name__ == '__main__':
    test_ArchiveOrgIE()

# Generated at 2022-06-14 16:04:50.424884
# Unit test for constructor of class ArchiveOrgIE

# Generated at 2022-06-14 16:04:58.045500
# Unit test for constructor of class ArchiveOrgIE

# Generated at 2022-06-14 16:05:05.993690
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'
    assert ie._TESTS[0]['url'] == 'http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect'

# Generated at 2022-06-14 16:05:14.494169
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ao = ArchiveOrgIE()
    assert ao.IE_NAME == 'archive.org'
    assert ao.IE_DESC == 'archive.org videos'
    assert ao._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:05:24.609940
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:05:27.610021
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:05:50.858556
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:05:51.772045
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    instance = ArchiveOrgIE()
    assert instance

# Generated at 2022-06-14 16:06:01.381198
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE('https://archive.org/details/MSNBCW_20131125_040000_To_Catch_a_Predator/')
    assert not ArchiveOrgIE('http://example.com').suitable(
        'https://archive.org/details/MSNBCW_20131125_040000_To_Catch_a_Predator/')
    assert ArchiveOrgIE('http://archive.org').suitable(
        'https://archive.org/details/MSNBCW_20131125_040000_To_Catch_a_Predator/')
    assert not ArchiveOrgIE('http://archive.org').suitable(
        'http://archive.org/details/MSNBCW_20131125_040000_To_Catch_a_Predator/')

# Generated at 2022-06-14 16:06:02.741326
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    test_obj = ArchiveOrgIE()
    assert type(test_obj) == ArchiveOrgIE

# Generated at 2022-06-14 16:06:04.522930
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    """Unit test for ArchiveOrgIE
    """
    assert ArchiveOrgIE

# Generated at 2022-06-14 16:06:08.480151
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE();
    assert(ie.IE_DESC == 'archive.org videos')
    assert(ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)')

# Generated at 2022-06-14 16:06:16.642889
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    from .test_utils import TEST_DATA_DIR
    from .test_utils import get_filesystem_cookie, get_filesystem_cookie_path
    from .test_utils import set_cookie

    # The following file(s) have their cookie saved in a file
    cookie_file = get_filesystem_cookie_path('archive.org')
    if os.path.isfile(cookie_file):
        cookie = get_filesystem_cookie('archive.org')
        set_cookie(cookie)

    js = open(os.path.join(TEST_DATA_DIR, 'archive.org.json'), 'r').read()
    jwplayer_data = json.loads(js)

    #__init__(self, _downloader=None, js_to_json=None, jwplayer_data=None, jwplayer_play

# Generated at 2022-06-14 16:06:18.887549
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # This test ensures archive.org videos can be downloaded by using the
    # constructor of ArchiveOrgIE class. It fails if constructor throws an
    # error.
    ArchiveOrgIE()

# Generated at 2022-06-14 16:06:20.222481
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    
    # test constructor 
    ie = ArchiveOrgIE()

# Generated at 2022-06-14 16:06:30.748807
# Unit test for constructor of class ArchiveOrgIE

# Generated at 2022-06-14 16:07:23.732683
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:07:34.117172
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    import os
    import pytest

    from youtube_dl.utils import DownloadError

    from .common import MyProxyHandler

    ret = ArchiveOrgIE()
    assert ret != None
    assert isinstance(ret, ArchiveOrgIE)
    assert ret.IE_NAME == "archive.org"
    assert ret.IE_DESC == "archive.org videos"

    # test argument to constructor
    with pytest.raises(DownloadError):
        ArchiveOrgIE(proxy_handler="invalid_handler")
    ret = ArchiveOrgIE(proxy_handler=MyProxyHandler())
    assert ret != None
    assert isinstance(ret, ArchiveOrgIE)

    # test https://archive.org/details/Cops1922
    url = "https://archive.org/details/Cops1922"
    ret = ret.url_result(url)


# Generated at 2022-06-14 16:07:34.649819
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE()

# Generated at 2022-06-14 16:07:35.821032
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    InfoExtractor('archive.org')

# Generated at 2022-06-14 16:07:44.069931
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    from .common import InfoExtractor
    from .ooyala import OoyalaIE
    from .scivee import SciVeeIE
    from .vidme import VidmeIE
    from .zype import ZypeIE
    from ..utils import (
        extract_attributes,
        urlencode_postdata,
        unified_strdate,
        unified_timestamp,
    )


# Generated at 2022-06-14 16:07:48.981468
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    me = ArchiveOrgIE()
    assert me.IE_NAME == 'archive.org'
    assert me.IE_DESC == 'archive.org videos'
    assert me._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:07:50.070480
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE('archive.org')

# Generated at 2022-06-14 16:08:00.517744
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    import os
    import re
    import unittest
    import yaml
    from collections import OrderedDict

    def read_yaml(file):
        with open(file, 'r') as f:
            return yaml.load(f)

    known_urls = OrderedDict()

    # Read in all known URLs
    for entry in os.listdir('test/data/archiveorg_urls'):
        if not re.match(r'^.*\.yml$', entry): continue
        data = read_yaml('test/data/archiveorg_urls/' + entry)
        known_urls[data['url']] = data

    # Add in URLs provided by archive.org feeds for some videos
    feeds_urls = read_yaml('test/data/feeds_urls.yml')


# Generated at 2022-06-14 16:08:07.240858
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert(ArchiveOrgIE.__name__ == 'ArchiveOrgIE')
    assert(ArchiveOrgIE.__doc__ == 'archive.org videos')
    assert(ArchiveOrgIE._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)')

# Generated at 2022-06-14 16:08:17.586450
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.ie_key() == 'archive.org'
    assert ie.ie_desc() == 'archive.org videos'
    assert ie.has_base_url() == False
    assert ie.has_caps() == False
    assert ie.has_metadata() == False
    assert ie.has_workaround() == False
    assert ie.has_referer() == False
    assert ie.has_login() == False
    assert ie.has_geo_restriction() == False
    assert ie.accept_webpage() == True
    assert ie.accept_host() == None
    assert ie.accept_scheme() == None
    assert ie.accept_netloc() == None
    assert ie.accept_url() == True
    assert ie.match_url(ie.valid_url()) == True


# Generated at 2022-06-14 16:10:41.505010
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    """
    Ensure that a constructor of a new class object runs without exception
    """
    ArchiveOrgIE()

# Generated at 2022-06-14 16:10:42.700822
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'

# Generated at 2022-06-14 16:10:44.996014
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # Ensure that no error is raised for the URL
    ArchiveOrgIE()._real_extract("http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect")

# Generated at 2022-06-14 16:10:49.045423
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    """Unit test for ArchiveOrgIE class (constructor)."""
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'


# Generated at 2022-06-14 16:10:52.555237
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    result = ArchiveOrgIE._build_url_result(
        InfoExtractor._WORKING_URL, r'https://archive.org/embed/Cops1922')
    assert result == 'https://archive.org/details/Cops1922'

# Generated at 2022-06-14 16:10:53.319627
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    InfoExtractor.test()

# Generated at 2022-06-14 16:10:55.657504
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    ie._parse_jwplayer_data("{}", "video_id")
    ie._parse_json("{}", "video_id")

# Generated at 2022-06-14 16:10:57.083112
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ai = ArchiveOrgIE()
    assert ai.IE_NAME == 'archive.org'

# Generated at 2022-06-14 16:10:58.695440
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    '''
    Test constructor of class ArchiveOrgIE
    '''
    archive_org_ie = ArchiveOrgIE('archive.org')

    assert archive_org_ie.ie_name == 'archive.org'
    assert archive_org_ie.ie_desc == 'archive.org videos'


# Generated at 2022-06-14 16:11:00.112804
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE().IE_NAME == 'archive.org'