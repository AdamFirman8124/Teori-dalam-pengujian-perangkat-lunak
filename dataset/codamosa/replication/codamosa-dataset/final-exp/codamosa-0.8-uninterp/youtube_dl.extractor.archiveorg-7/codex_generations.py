

# Generated at 2022-06-14 16:02:59.692049
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    archive_org = ArchiveOrgIE()
    assert archive_org.IE_NAME == 'archive.org'
    assert archive_org.IE_DESC == 'archive.org videos'

# Generated at 2022-06-14 16:03:01.308138
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()

if __name__ == '__main__':
    test_ArchiveOrgIE()

# Generated at 2022-06-14 16:03:02.605686
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE(None)

# Generated at 2022-06-14 16:03:07.300034
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
	ie = ArchiveOrgIE()
	assert ie.ie_key() == 'archive.org'
	assert ie.ie_desc() == 'archive.org videos'
	assert ie.suitable('http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')

# Generated at 2022-06-14 16:03:08.658317
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE().IE_NAME == 'archive.org'


# Generated at 2022-06-14 16:03:09.221290
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:03:10.991585
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    inst = ArchiveOrgIE()
    assert type(inst) == ArchiveOrgIE

# Generated at 2022-06-14 16:03:11.892536
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()

# Generated at 2022-06-14 16:03:12.425039
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:03:13.362040
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()

# Generated at 2022-06-14 16:03:27.757985
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # Test constructor for ArchiveOrgIE
    ie = ArchiveOrgIE()
    if sys.version_info >= (3,):
        assert str(ie) == '<ArchiveOrgIE (archive.org)>'
    else:
        assert unicode(ie) == u'<ArchiveOrgIE (archive.org)>'

# Generated at 2022-06-14 16:03:30.390620
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    a = ArchiveOrgIE()
    assert a.IE_NAME == 'archive.org'
    assert a.IE_DESC == 'archive.org videos'

# Generated at 2022-06-14 16:03:33.803685
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    try:
        ArchiveOrgIE()
        print('Passed the test case successfully')
    except Exception as e:
        print('Cannot run any test cases')

# Generated at 2022-06-14 16:03:35.976979
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    """
    Checks if a valid archive.org instance can be constructed with a valid URL.
    """
    assert ArchiveOrgIE("http://archive.org")

# Generated at 2022-06-14 16:03:42.817450
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'
    ie = ArchiveOrgIE('archive.org')
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:03:43.836365
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE()

# Generated at 2022-06-14 16:03:53.981342
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    ie_name = ie.IE_NAME
    ie_name_re = '^' + ie_name + '$'
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie.VALID_URL == ie._VALID_URL
    assert ie.VALID_URL.find("IE_NAME") == -1
    assert ie.VALID_URL.find("IE_DESC") == -1
    assert ie.__name__.find("IE_NAME") == -1
    assert ie.__name__.find("IE_DESC") == -1
    assert hasattr(ie, '_real_initialize')

# Generated at 2022-06-14 16:04:04.906723
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE('archive.org')
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'
    assert ie._TESTS[0]['url'] == 'http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    assert ie._TESTS[0]['md5'] == '8af1d4cf447933ed3c7f4871162602db'

# Generated at 2022-06-14 16:04:06.012900
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:04:18.335832
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:04:44.613416
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'


# Generated at 2022-06-14 16:04:54.212449
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    test_string = '''<!DOCTYPE html><html><head><title>Title</title><script>
    window.archive_setup = {video:{url:"http://archive.org/videos/xyz.mp4"},
    x:"y", z:{}};
    </script>
    <script>
    window.archive_setup = {video:{url:"http://archive.org/videos/abc.mp4"},
    z:{y:"x"}};
    </script>
    <script>
    window.archive_setup = {video:{url:"http://archive.org/videos/123.mp4",
    extra:"extra data"}};
    </script></head></html>'''
    test_obj = ArchiveOrgIE()

# Generated at 2022-06-14 16:04:54.952759
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE()

# Generated at 2022-06-14 16:05:00.571076
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    # E.g. a video with a playlist of empty jwplayer.
    url = 'http://archive.org/details/MSNBCW_20131125_040000_To_Catch_a_Predator/'
    archiveOrg = ArchiveOrgIE()

    assert archiveOrg._real_extract(url)

# Generated at 2022-06-14 16:05:01.545568
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert ArchiveOrgIE()._VALID_URL == ArchiveOrgIE._VALID_URL

# Generated at 2022-06-14 16:05:04.909218
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.ie_key() == 'archive.org'
    assert ie.ie_name() == 'archive.org videos'
    assert ie.ie_desc() == 'archive.org videos'

# Generated at 2022-06-14 16:05:13.815749
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    from .common import InfoExtractor
    from .youtube import YoutubeIE
    from .common import FileDownloader
    from .aaaarg import AaaargIE
    from .adobetv import AdobeTVIE
    from .adultswim import AdultSwimIE
    from .airmozilla import AirMozillaIE
    from .alphaporno import AlphaPornoIE
    from .anitube import AnitubeIE
    from .anysex import AnySexIE
    from .archiveorg import ArchiveOrgIE
    from .aruodas import AruodasIE
    from .asiancrush import AsianCrushIE
    from .atresplayer import AtresPlayerIE
    from .bbc import BBCCoUkIE
    from .bdsmstreak import BDSMStreakIE
    from .beeg import BeegIE
    from .beeg import Beeg

# Generated at 2022-06-14 16:05:15.585069
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    'Test constructor of class ArchiveOrgIE'
    s = ArchiveOrgIE()
    assert s.IE_NAME == 'archive.org'

# Generated at 2022-06-14 16:05:26.065872
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:05:31.793859
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie._VALID_URL == ArchiveOrgIE._VALID_URL
    assert ie._TESTS == ArchiveOrgIE._TESTS
    assert ie.IE_NAME == ArchiveOrgIE.IE_NAME
    assert ie.IE_DESC == ArchiveOrgIE.IE_DESC
    assert ie._BASE_URL == archive.org

# Generated at 2022-06-14 16:05:53.527118
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'

# Generated at 2022-06-14 16:06:02.873819
# Unit test for constructor of class ArchiveOrgIE

# Generated at 2022-06-14 16:06:04.279608
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    o = ArchiveOrgIE()

# Generated at 2022-06-14 16:06:13.725528
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:06:14.544655
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    IE = ArchiveOrgIE('archive.org')
    IE

# Generated at 2022-06-14 16:06:16.155152
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert  ie.IE_NAME == "ArchiveOrg"
    assert ie.IE_DESC == "archive.org videos"

# Generated at 2022-06-14 16:06:21.153926
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    """
    Unit test for ArchiveOrgIE constructor
    """
    ie_archive_org = ArchiveOrgIE()
    assert ie_archive_org.IE_NAME == 'archive.org'
    assert ie_archive_org.IE_DESC == 'archive.org videos'
    assert ie_archive_org._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'
    assert ie_archive_org._TESTS
    assert ie_archive_org.BR_DESC
    assert ie_archive_org.SUFFIX
    assert ie_archive_org._TEST



# Generated at 2022-06-14 16:06:22.481662
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE().suite()

# Generated at 2022-06-14 16:06:33.099634
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'
    assert ie._TESTS[0]['url'] == 'http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    assert ie._TESTS[0]['md5'] == '8af1d4cf447933ed3c7f4871162602db'

# Generated at 2022-06-14 16:06:38.493236
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    info_extractor = ArchiveOrgIE()
    assert info_extractor.IE_NAME == 'archive.org'
    assert info_extractor.IE_DESC == 'archive.org videos'
    assert info_extractor._VALID_URL == 'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'

# Generated at 2022-06-14 16:07:27.743579
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:07:38.972017
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    from .common import InfoExtractor
    from ..downloader.common import FileDownloader
    from ..downloader.http import HttpRequest
    from ..utils import (
        clean_html,
        extract_attributes,
        unified_strdate,
        unified_timestamp,
    )
    from ..compat import compat_urllib_parse
        
    test_obj = ArchiveOrgIE()
    
    assert test_obj.REQUEST == HttpRequest()
    assert test_obj.FILE_DOWNLOADER_CLS == FileDownloader
    assert test_obj.IE_NAME == 'archive.org'
    assert test_obj.IE_DESC == 'archive.org videos'

# Generated at 2022-06-14 16:07:40.067132
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    arch = ArchiveOrgIE()
    assert arch.IE_NAME == 'archive.org'

# Generated at 2022-06-14 16:07:40.551511
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:07:46.743893
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    IE = ArchiveOrgIE(None)
    assert IE._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'
    assert IE._TESTS[1]['url'] == 'https://archive.org/details/Cops1922'
    assert IE._TESTS[1]['md5'] == '0869000b4ce265e8ca62738b336b268a'
    # Check the constructor of the InfoExtractor parent class
    assert ArchiveOrgIE.__bases__[0].__init__.__defaults__ == (None,)
    # Check the parameters of the constructor of the InfoExtractor
    assert ArchiveOrgIE.__init__.__defaults__ == (None,)
    assert 'Cops1922' in Archive

# Generated at 2022-06-14 16:07:52.216829
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    t = ArchiveOrgIE()
    assert t.IE_NAME == 'archive.org'
    assert t.IE_DESC == 'archive.org videos'
    assert t._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'



# Generated at 2022-06-14 16:07:53.160466
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:07:56.995527
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    IE = ArchiveOrgIE()
    assert IE.IE_NAME == 'archive.org'
    assert IE.IE_DESC == 'archive.org videos'
    assert isinstance(
        IE._VALID_URL,
        object
    )  # object because it's a compiled regular expression

# Generated at 2022-06-14 16:07:57.877517
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE(InfoExtractor())

# Generated at 2022-06-14 16:07:59.101020
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE('archive.org', 'archive.org videos')

# Generated at 2022-06-14 16:10:01.414864
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ArchiveOrgIE()

# Generated at 2022-06-14 16:10:03.530614
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    obj = ArchiveOrgIE()
    assert obj.ie_key() == 'ArchiveOrgIE'

# Generated at 2022-06-14 16:10:07.247796
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    aoi = ArchiveOrgIE()
    assert aoi.IE_NAME in aoi._VALID_URL
    assert aoi.IE_DESC in aoi._VALID_URL
    assert aoi._VALID_URL in aoi.IE_DESC

# Generated at 2022-06-14 16:10:18.114017
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    from ..utils import make_extractor_tests

# Generated at 2022-06-14 16:10:20.127723
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.ie_key() == 'ArchiveOrg'
    assert str(ie) == '<ArchiveOrg object>'

# Generated at 2022-06-14 16:10:25.174828
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_NAME == 'archive.org'
    assert ie.IE_DESC == 'archive.org videos'
    assert ie._VALID_URL == r'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'
    assert len(ie._TESTS) == 4

# Unit tests for _real_extract() of class ArchiveOrgIE

# Generated at 2022-06-14 16:10:26.730871
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie.IE_DESC == "archive.org videos"
    assert ie.IE_NAME == "archive.org"

# Generated at 2022-06-14 16:10:27.881261
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    assert(ArchiveOrgIE())

# Generated at 2022-06-14 16:10:32.195415
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    info = ArchiveOrgIE()._real_extract('http://archive.org/details/XD300-23_68HighlightsAResearchCntAugHumanIntellect')
    assert info['id'] == 'XD300-23_68HighlightsAResearchCntAugHumanIntellect'
    assert info['title'] == '1968 Demo - FJCC Conference Presentation Reel #1'
    assert info['ext'] == 'ogg'

# Generated at 2022-06-14 16:10:34.818110
# Unit test for constructor of class ArchiveOrgIE
def test_ArchiveOrgIE():
    ie = ArchiveOrgIE()
    assert ie is not None
    assert ie._VALID_URL == 'https?://(?:www\.)?archive\.org/(?:details|embed)/(?P<id>[^/?#&]+)'
