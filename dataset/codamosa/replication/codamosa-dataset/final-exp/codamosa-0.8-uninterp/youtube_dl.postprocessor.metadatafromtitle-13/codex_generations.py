

# Generated at 2022-06-14 17:58:41.126868
# Unit test for method format_to_regex of class MetadataFromTitlePP
def test_MetadataFromTitlePP_format_to_regex():
    metadata_from_title_pp = MetadataFromTitlePP(None, None)

    assert metadata_from_title_pp.format_to_regex('%(a)s') == r'(?P<a>.+)'
    assert metadata_from_title_pp.format_to_regex('%(a)s%(b)s') == r'(?P<a>.+)(?P<b>.+)'
    assert metadata_from_title_pp.format_to_regex('%(a)s%(b)s%(c)s') == r'(?P<a>.+)(?P<b>.+)(?P<c>.+)'
    assert metadata_from_title_pp.format_to_regex('%(a)s%(b)s%(c)s%(d)s')

# Generated at 2022-06-14 17:58:46.775948
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FileDownloader
    from .extractor import GenYoutubeIE
    # Run on fake file
    ydl = FileDownloader()
    ydl.add_info_extractor(GenYoutubeIE())
    mpp = MetadataFromTitlePP(ydl, '%(title)s - %(artist)s')
    info = {'title': 'Video name - Artist name', 'webpage_url': 'dummy'}
    # Run post-processing on the info dictionary
    mpp.run(info)
    # Check that it parsed the title successfully
    assert info['title'] == 'Video name'
    assert info['artist'] == 'Artist name'



# Generated at 2022-06-14 17:58:54.811477
# Unit test for constructor of class MetadataFromTitlePP
def test_MetadataFromTitlePP():
    """Test constructor of MetadataFromTitlePP."""
    from .common import FileDownloader
    metadata_from_title_pp = MetadataFromTitlePP(
        FileDownloader({}), '%(title)s - %(artist)s')
    assert metadata_from_title_pp._titleformat == '%(title)s - %(artist)s'
    assert metadata_from_title_pp._titleregex == '(?P<title>.+)\ \-\ (?P<artist>.+)'


# Generated at 2022-06-14 17:59:02.274040
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FileDownloader
    metadata = {}
    assert MetadataFromTitlePP(
        FileDownloader(None), '%(title)s - %(artist)s').run(metadata) == ([], {})
    assert MetadataFromTitlePP(
        FileDownloader(None), '%(title)s - %(artist)s').run({
            'title': 'Metallica - Fade to Black',
            'artist': 'Metallica'}) == ([], {
                'title': 'Fade to Black',
                'artist': 'Metallica'})


# Generated at 2022-06-14 17:59:09.092498
# Unit test for method format_to_regex of class MetadataFromTitlePP
def test_MetadataFromTitlePP_format_to_regex():
    pp = MetadataFromTitlePP(None, '%(title)s - %(artist)s')
    assert pp._titleregex == '(?P<title>.+)\ \-\ (?P<artist>.+)'
    pp = MetadataFromTitlePP(None, '%(title)s')
    assert pp._titleregex == '(?P<title>.+)'
    pp = MetadataFromTitlePP(None, '%(title)s - 100%%')
    assert pp._titleregex == '(?P<title>.+)\ \-\ 100%'

# Generated at 2022-06-14 17:59:21.564810
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Test imports and constants
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.postprocessor import FFmpegMetadataPP


# Generated at 2022-06-14 17:59:32.320128
# Unit test for method run of class MetadataFromTitlePP

# Generated at 2022-06-14 17:59:43.955817
# Unit test for method format_to_regex of class MetadataFromTitlePP
def test_MetadataFromTitlePP_format_to_regex():
    import unittest
    import unittest.mock

    class MockYoutubeDL: pass
    ydl = MockYoutubeDL()

    class MyTest(unittest.TestCase):
        def setUp(self):
            self.ydl = ydl

    pp = MetadataFromTitlePP(ydl, '%(title)s - %(artist)s')

    unittest.TestLoader().loadTestsFromTestCase(MyTest).run(
        unittest.TestResult())

    # run the test
    mtt = MyTest('test_format_to_regex')
    mtt.setUp()

# Generated at 2022-06-14 17:59:51.539566
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FileDownloader
    from .extractor import gen_extractors
    from .utils import parse_duration

    # Build fake downloader
    downloader = FileDownloader({})
    downloader.params.update({'format': '', 'outtmpl': '%(title)s.%(ext)s'})
    downloader.add_info_extractor(gen_extractors())

    # Test with empty title
    pp = MetadataFromTitlePP(downloader, '%(title)s')
    _, info = pp.run({'id': '123', 'title': '', 'uploader': 'video', 'ext': 'flv'})
    assert info['title'] == ''
    assert info['track'] == ''
    assert info['artist'] == ''
    assert info['album'] == ''

# Generated at 2022-06-14 18:00:02.419419
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from pytube.compat import compat_str
    from pytube.extract import Video
    from pytube.extract import VideoEntry
    from pytube.extract import watch_url
    from pytube import extract
    from pytube import request
    from pytube import util

    url = 'https://www.youtube.com/watch?v=voqOYj_2N-c'
    titleformat = '%(title)s.%(ext)s'

    title_mets = ['A sample video by pytube', 'Another sample video by pytube']
    title_mets_old_format = ['Sample Video by pytube', 'Sample Video by pytube']

    response = request.get(url, parse_qs=True)

# Generated at 2022-06-14 18:00:14.132552
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import random

    class DummyDownloader(object):
        def to_screen(self, str):
            # print(str),  # Python 2
            print(str)    # Python 3

    # test data
    title_in_1 = 'sample title'
    titleformat_1 = '%(title)s'

    title_in_2 = 'sample title - sample artist'
    titleformat_2 = '%(title)s - %(artist)s'

    title_in_3 = 'sample title - sample artist - sample album'
    titleformat_3 = '%(title)s - %(artist)s - %(album)s'

    title_in_4 = 'something - sample title - sample artist - sample album'

# Generated at 2022-06-14 18:00:26.070430
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Test case #1
    downloader = None
    titleformat = '%(artist)s - %(title)s'
    pp = MetadataFromTitlePP(downloader, titleformat)
    info = {'title': 'Nirvana - About A Girl'}
    result = pp.run([], info)
    expected = ([], {'artist': 'Nirvana', 'title': 'About A Girl'})
    #print(result)
    assert result == expected

    # Test case #2
    downloader = None
    titleformat = '%(artist)s_%(title)s'
    pp = MetadataFromTitlePP(downloader, titleformat)
    info = {'title': 'Alpine_-_Gasoline'}
    result = pp.run([], info)

# Generated at 2022-06-14 18:00:36.948850
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FileDownloader


# Generated at 2022-06-14 18:00:43.426807
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    titleformat = '%(title)s - %(alt_title)s - %(artist)s'
    pp = MetadataFromTitlePP('dummy', titleformat)
    info = {}
    info['title'] = 'title - alt_title - artist'
    info = pp.run(info)[1]
    assert info['title'] == 'title'
    assert info['alt_title'] == 'alt_title'
    assert info['artist'] == 'artist'


# Generated at 2022-06-14 18:00:53.349326
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    info = {'title': 'dummy'}
    pp = MetadataFromTitlePP(None, '%(title)s - %(artist)s')
    pp.run(info)
    assert info['title'] == 'dummy'
    assert info['artist'] == 'NA'

    info = {'title': 'dummy - foo'}
    pp.run(info)
    assert info['title'] == 'dummy'
    assert info['artist'] == 'foo'

    info = {'title': 'dummy - foo - bar'}
    pp.run(info)
    assert info['title'] == 'dummy'
    assert info['artist'] == 'foo - bar'

    # Handle special characters
    info = {'title': 'dummy - foo-._+'}
    pp.run(info)

# Generated at 2022-06-14 18:01:06.194189
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    d = {'title': 'abcd efg hijk'}
    fmt = '%(title)s'
    pp = MetadataFromTitlePP(None, fmt)
    assert pp.run(d) == ([], {'title': 'abcd efg hijk'})

    fmt = '%(title)s - %(artist)s'
    pp = MetadataFromTitlePP(None, fmt)
    assert pp.run(d) == ([], {'title': 'abcd efg hijk'})

    d = {'title': 'abcd - efg - hijk'}
    assert pp.run(d) == ([], {'title': 'abcd - efg - hijk'})

    d = {'title': 'abcd - efg hijk'}

# Generated at 2022-06-14 18:01:11.290482
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.downloader import Downloader
    from youtube_dl.extractor import YoutubeDL
    from youtube_dl.utils import prepend_extension

    ydl = YoutubeDL({
        'postprocessors': [MetadataFromTitlePP(Downloader(['']), 'Test - %(title)s')],
    })

    title = 'Test - test_title'
    info = {'title': title, 'ext': '.webm'}
    pp = MetadataFromTitlePP(Downloader(['']), 'Test - %(title)s')
    pp.run(info)

    assert info['title'] == 'test_title'

# Generated at 2022-06-14 18:01:22.079399
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ydl.__main__ import YoutubeDL
    from ydl.postprocessor.ffmpeg import FFmpegFixupPP
    from ydl.postprocessor.ffmpeg import FFmpegMetadataPP
    from ydl.postprocessor.xattrpp import XAttrMetadataPP

    from .common import FakeYDL
    from .common import Match
    from .common import mock

    ydl = FakeYDL()
    ydl.params['format'] = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4'


# Generated at 2022-06-14 18:01:33.311710
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    ydl = YoutubeDL({})
    ydl.add_post_processor(MetadataFromTitlePP(ydl, '%(uploader)s'))
    info = {'title': 'Some random uploader - some random title'}
    ydl.post_process(info)
    assert info['uploader'] == 'Some random uploader'
    ydl.add_post_processor(MetadataFromTitlePP(ydl, '%(uploader)s - %(title)s'))
    info = {'title': 'Some random uploader - some random title'}
    ydl.post_process(info)
    assert info['uploader'] == 'Some random uploader'
    assert info['title'] == 'some random title'

# Generated at 2022-06-14 18:01:44.892711
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.postprocessor.common import FFmpegMetadataPP
    import copy
    import unittest

    class TestMetadataFromTitlePP(unittest.TestCase):
        def setUp(self):
            self.downloader = MockYDL()
            self.downloader.to_screen = lambda x: x
            self.postprocessor = MetadataFromTitlePP.create_instance(
                self.downloader, titleformat='%(artist)s - %(title)s')

        def test_MetadataFromTitlePP_run(self):
            info = {
                'title': 'The Artist - The Title'
            }


# Generated at 2022-06-14 18:01:58.359162
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FileDownloader
    from .compat import compat_urlparse

    # Initialize a fake FileDownloader for testing
    class FakeYDL(FileDownloader):
        def __init__(self):
            super(FakeYDL, self).__init__()
            self.to_screen_count = 0

        def to_screen(self, msg):
            self.to_screen_count += 1

    # Initialize a FakeYDL instance
    fydl = FakeYDL()

    # Initialize a MetadataFromTitlePP instance
    mftpp = MetadataFromTitlePP(fydl,
                                '%(title)s - %(artist)s')

    # Initialize a test info dictionary

# Generated at 2022-06-14 18:02:04.494509
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Test method run by generating a sample of all possible outputs for each
    # of the supported formats
    import sys
    class SampleDownloader(object):
        def __init__(self):
            self._screen_buffer = []

        def to_screen(self, s):
            self._screen_buffer.append(s)

        def _screen(self):
            return self._screen_buffer

    datestamp = '20131122'
    uploader = 'exampleuser'
    uploader_id = None
    track = 'Track'
    artist = 'Artist'
    album = 'Album'
    title = '{title}-{uploader}-{upload_date}'.format(title=track, uploader=uploader, upload_date=datestamp)

# Generated at 2022-06-14 18:02:15.584484
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import unittest
    class TestMetadataFromTitlePP(unittest.TestCase):
        def setUp(self):
            self._downloader = object()
        def test_run(self):
            pp = MetadataFromTitlePP(self._downloader, '%(artist)s - %(title)s')
            info = {'title': 'Test Artist - Test Title'}
            #pp.run(info)
            self.assertEqual(pp.format_to_regex('%(artist)s - %(title)s'), '(?P<artist>.+)\ \-\ (?P<title>.+)')
            self.assertDictEqual(info, {'title': 'Test Artist - Test Title', 'artist': 'Test Artist'})


# Generated at 2022-06-14 18:02:27.597108
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    """
    Run unit tests for method run of class MetadataFromTitlePP
    """
    class TestDownloader():
        @staticmethod
        def to_screen(msg):
            print(msg)

    class TestInfo():
        def __init__(self, title):
            self.title = title

        @property
        def __getitem__(self, key):
            return self.__dict__[key]

        @property
        def __setitem__(self, key, value):
            self.__dict__[key] = value

        @property
        def __contains__(self, key):
            return key in self.__dict__

    downloader = TestDownloader()

    # Format string containing both named and unnamed fields

# Generated at 2022-06-14 18:02:36.681863
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    from ytdl_info import YtdlFileInfo
    from ytdl_opts import Opts
    from ytdl_extractor import YoutubeIE
    from ytdl_postprocessor import YtdlPostProcessor


# Generated at 2022-06-14 18:02:44.950021
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.downloader.common import FileDownloader
    from youtube_dl.postprocessor.metadatafromtitle import MetadataFromTitlePP

    # Test data - YouTube video uploaded by user "UFC - Ultimate Fighting Championship"
    # on 2016-08-12

# Generated at 2022-06-14 18:02:54.745534
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    import doctest
    # Test a set of inputs and expected outputs

# Generated at 2022-06-14 18:03:04.818475
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    if sys.version_info >= (3, 0):
        from io import StringIO
        class FakeDownloader(object):
            def to_screen(self, msg):
                print(msg)
        fd = StringIO()
        sys.stdout = fd
    else:
        from StringIO import StringIO
        class FakeDownloader(object):
            def to_screen(self, msg):
                print(msg)
        fd = StringIO()
        sys.stdout = fd


# Generated at 2022-06-14 18:03:12.766734
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    from collections import OrderedDict
    from .common import Downloader

    titleformat = '%(episode)s - %(show)s - S%(season)sE%(episode_number)s - %(title)s'
    title = 'Episode 6 - Show 1 - S1E6 - The Title of Episode 6'
    mp = MetadataFromTitlePP(Downloader(params=OrderedDict()), titleformat)

    # test regex conversion
    expected_regex = '(?P<episode>.+)\ \-\ (?P<show>.+)\ \-\ S(?P<season>.+)E(?P<episode_number>.+)\ \-\ (?P<title>.+)'
    assert mp._titleregex == expected_regex


# Generated at 2022-06-14 18:03:24.625128
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    downloader = object()
    titleformat = '%(title)s - %(artist)s'
    titleregex = '(?P<title>.+)\ \-\ (?P<artist>.+)'
    pp = MetadataFromTitlePP(downloader, titleformat)
    assert pp._titleformat == titleformat
    assert pp._titleregex == titleregex
    # No match
    info = {'title': 'MetadataFromTitlePP test failed'}
    res = pp.run(info)
    assert res[-1] == info
    # Match
    info = {'title': 'MetadataFromTitlePP test passed - test_user'}
    res = pp.run(info)
    assert res[-1] == info
    assert info['title'] == 'MetadataFromTitlePP test passed'

# Generated at 2022-06-14 18:03:37.715178
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .downloader import YoutubeDL
    from .extractor import YoutubeIE
    from .utils import DateRange
    from .compat import compat_str
    from .extractor.common import InfoExtractor

    class TestIE(InfoExtractor):
        def search_key(self, keyword):
            return [
                {
                    'id': 'abc_123',
                    'title': 'Abc 123',
                    'url': 'http://nothing/abc-123',
                },
                {
                    'id': 'xyz_789',
                    'title': 'Xyz 789',
                    'url': 'http://nothing/xyz-789',
                }
            ]


# Generated at 2022-06-14 18:03:47.700852
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FileDownloader
    from .compat import compat_http_client
    from .extractor import GenYoutubeIE
    from .extractor.common import InfoExtractor

    # Dummy Youtube extractor
    class DummyYoutubeIE(InfoExtractor):
        @staticmethod
        def suitable(url):
            return False

        def _real_extract(self, url):
            return {
                'id': 'papokNtE9y8',
                'url': 'https://www.youtube.com/watch?v=papokNtE9y8',
                'title': 'TEST - This is a test video'
            }

    InfoExtractor._call_downloader = FileDownloader(
        None,
        None,
        compat_http_client.HTTPDefaultErrorHandler())


# Generated at 2022-06-14 18:03:58.700687
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .subtitles import SubtitlesPP
    from .make_md5 import MakeMd5PP
    from .fixup import FixupPP
    from .ffmpeg import FFmpegMetadataPP
    from .getThumbnailPP import GetThumbnailPP
    from .embedsubtitlePP import EmbedSubtitlePP
    from .execafterdownload import ExecAfterDownloadPP
    downloader = 'test_downloader'

# Generated at 2022-06-14 18:04:10.392021
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import Downloader
    from .extractor import gen_extractors
    from .downloader import gen_extractor_classes
    from .postprocessor import gen_pp_classes

    downloader = Downloader({})
    for ie in gen_extractors(downloader):
        ie.extractor_type = 'test'
    downloader.extractor_classes = gen_extractor_classes(downloader)
    downloader.pp_classes = gen_pp_classes()

    pp = MetadataFromTitlePP(downloader, '%(title)s - %(artist)s')
    info = {'title': 'abc - def'}
    assert pp.run(info)[1] == {'title': 'abc', 'artist': 'def'}


# Generated at 2022-06-14 18:04:15.915222
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import youtube_dl.YoutubeDL
    # Test with a Python-interpolable titleformat
    ydl = youtube_dl.YoutubeDL({})
    pp = MetadataFromTitlePP(ydl, '%(title)s')
    info = {'title': 'Toto - Africa'}
    infod = pp.run(info)[1]
    assert infod.get('title') == 'Toto'
    # Test with a regex titleformat
    ydl = youtube_dl.YoutubeDL({})
    pp = MetadataFromTitlePP(ydl, r'(?P<title>.+)\ \-\ .+')
    info = {'title': 'Toto - Africa'}
    infod = pp.run(info)[1]
    assert infod.get('title') == 'Toto'

# Generated at 2022-06-14 18:04:24.872619
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FileDownloader
    from .common import FakeYDL
    from .compat import str

    ydl = FakeYDL()
    ydl.params['simulate'] = True
    ydl.params['writethumbnail'] = False
    ydl.params['writeinfojson'] = False
    format = '%(title)s by %(artist)s'
    
    pp = MetadataFromTitlePP(ydl, format)

    info = {
        'title': 'The Title with a tag in <br> format'
    }
    
    # test default values
    pp.run(info)
    assert info['title'] == 'The Title with a tag in &lt;br&gt; format'
    assert info['artist'] == 'NA'
    

# Generated at 2022-06-14 18:04:33.399270
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    import os

    os.chdir(sys.path[1])

    # Test titleformat "%(title)s" and title "Test"
    pp = MetadataFromTitlePP(None, titleformat="%(title)s")
    assert pp.run({'title':'Test'})[1] == {'title':'Test'}
    # Test titleformat "%(title)s - %(artist)s" and title "Test - Artist"
    pp = MetadataFromTitlePP(None, titleformat="%(title)s - %(artist)s")
    assert pp.run({'title':'Test - Artist'})[1] == {'title':'Test', 'artist':'Artist'}
    # Test titleformat "%(title)s - %(artist)s" and title "Test - Artist - Foo"
   

# Generated at 2022-06-14 18:04:44.773454
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import unittest

    import sys
    sys.modules.update({
        'youtube_dl.YoutubeDL': type('YoutubeDL', (object,), {}),
    })

    from youtube_dl.postprocessor.metadata_from_title import MetadataFromTitlePP

    class TestCase(unittest.TestCase):
        def setUp(self):
            self.pp = MetadataFromTitlePP('testDL', r'%(uploader)s-%(title)s')

        def test_run_with_success(self):
            info = {
                'title': 'testUser-testTitle',
                'ext': '.mp4',
                'format': 'mp4'
            }


# Generated at 2022-06-14 18:04:54.897368
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .downloader import FakeDownloader

    # Test 1: %(title)s - %(artist)s
    #  title: 'SOME_TITLE - SOME_ARTIST' (match)
    # expected: {'title': 'SOME_TITLE', 'artist': 'SOME_ARTIST'}
    dl = FakeDownloader('%(title)s - %(artist)s')
    pp = MetadataFromTitlePP(dl, '%(title)s - %(artist)s')
    assert pp.format_to_regex('%(title)s - %(artist)s') == \
        r'(?P<title>.+)\ \-\ (?P<artist>.+)'
    assert pp._titleregex == r'(?P<title>.+)\ \-\ (?P<artist>.+)'

# Generated at 2022-06-14 18:05:04.263426
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    title = 'Song Name - Singer Name'
    info = {'title': title}
    metadata_from_titlepp = MetadataFromTitlePP(None, '%(title)s - %(artist)s')
    _, new_info = metadata_from_titlepp.run(info)
    assert 'artist' in new_info.keys()
    assert 'title' in new_info.keys()

    title_incorrect = 'Song Name - Singer Name - This is not present in Format'
    info = {'title': title_incorrect}
    metadata_from_titlepp = MetadataFromTitlePP(None, '%(title)s - %(artist)s')
    _, new_info = metadata_from_titlepp.run(info)
    assert 'artist' in new_info.keys()
    assert 'title' in new

# Generated at 2022-06-14 18:05:18.774974
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.downloader.common import FileDownloader
    from youtube_dl.YoutubeDL import YoutubeDL
    ydl = YoutubeDL({})

# Generated at 2022-06-14 18:05:29.393921
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class MockYDL:
        def __init__(self):
            self.to_screen = self.add_info = self.report_error = self.report_warning = lambda x: x

    # Test 1: Correct metadata parsed from title
    # ----------------------------------------
    mp = MetadataFromTitlePP(MockYDL(), '%(uploader)s - %(title)s')
    info = {
        'title': 'Uploader - Title'
    }
    mp.run(info)
    assert info['uploader'] == 'Uploader'
    assert info['title'] == 'Title'

    # Test 2: Some metadata not found
    # -------------------------------
    mp = MetadataFromTitlePP(MockYDL(), '%(uploader)s - %(title)s')

# Generated at 2022-06-14 18:05:41.730804
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .downloader import FakeDownloader

    def check(titlefmt, title, expinfo):
        pp = MetadataFromTitlePP(FakeDownloader('.'), titlefmt)
        info = {'title': title}
        infos = pp.run(info)
        assert infos[1] == expinfo

    check(
        '%(title)s', 'Test Video',
        {'title': 'Test Video'}
    )
    check(
        '%(id)s', 'Test Video',
        {}
    )
    check(
        '%(title)s - %(artist)s', 'Test Video - Artists',
        {'title': 'Test Video', 'artist': 'Artists'}
    )

# Generated at 2022-06-14 18:05:50.899146
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FileDownloader

# Generated at 2022-06-14 18:06:02.559247
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    pp = MetadataFromTitlePP(None, '%(title)s - %(artist)s')
    assert(pp._titleregex == '(?P<title>.+)\ \-\ (?P<artist>.+)')
    info = { 'title': 'a - b' }
    new_info = { 'title': 'a - b', 'artist': 'b' }
    assert(pp.run(info)[1] == new_info)
    info = { 'title': 'a - b - c' }
    new_info = { 'title': 'a - b - c'}
    assert(pp.run(info)[1] == new_info)
    # Adding a character to title will break its regex
    info = { 'title': 'a - b - c' }

# Generated at 2022-06-14 18:06:11.917276
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .extractor.common import InfoExtractor
    from .downloader.common import FileDownloader
    from .compat import compat_str

    def run_test(titleformat, title, expectedresult):
        downloader = FileDownloader({})
        ie = InfoExtractor({})
        info = {'title': title}
        pp = MetadataFromTitlePP(downloader, titleformat)
        info = pp.run(info)[1]
        for attribute, value in expectedresult.items():
            if info[attribute] != value:
                print('Attribute %s expected: %s got: %s'
                      % (attribute, value, info[attribute]))
                return False
        return True

    titleformat = '%(artist)s - %(track)s - %(title)s'
    # regex

# Generated at 2022-06-14 18:06:20.192468
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FileDownloader

    m = MetadataFromTitlePP(FileDownloader({}),
                            u'%(title)s [%(asdf)s] %(asdf)s [%(uploader)s]')
    info = {'title': 'foo [bar] baz [asdf]'}
    (info, ) = m.run(info)
    assert info['title'] == 'foo [bar] baz [asdf]'
    assert info['asdf'] == 'bar'
    assert info['uploader'] == 'asdf'

# Generated at 2022-06-14 18:06:30.758255
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ..compat import compat_http_server
    from ..downloader import YoutubeDL
    import sys
    import threading

    # Prepare a youtube-dl object needed by the post processor
    class MyYoutubeDL(YoutubeDL):
        def __init__(self, *args, **kargs):
            YoutubeDL.__init__(self, *args, **kargs)
            self.to_screen_list = []
            self.to_stderr_list = []

        def to_screen(self, msg):
            self.to_screen_list.append(msg)

        def to_stderr(self, msg):
            self.to_stderr_list.append(msg)
    ydl = MyYoutubeDL()

    # Prepare a server to serve two videos with a title

# Generated at 2022-06-14 18:06:42.785933
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import youtube_dl
    import json

    # Use an instance of YoutubeDL to test
    ydl = youtube_dl.YoutubeDL()

    # Construct an instance of MetadataFromTitlePP
    metadata_from_title_pp = MetadataFromTitlePP(ydl, '%(title)s.%(ext)s')

    # Create a dummy info dict
    # FIXME: We need a function to create this from a YoutubeDL object (copy of to_screen method)
    info = {'title': 'test_title'}
    info['ext'] = 'mp4'

    # Run the run method
    metadata_from_title_pp.run(info)

    # Check result
    expected_result = {'title': 'test_title', 'ext': 'mp4'}
    result = info

    assert result == expected_result

# Generated at 2022-06-14 18:06:51.965827
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    """ Tests the method run of MetadataFromTitlePP.
        Tests the following format strings:
            "%(artist)s - %(title)s"
            "%(title)s"
            "%(title)s - %(artist)s"
            "%(artist)s - %(title)s - %(id)s"
        Tests with the following titles:
            "Artist - Title"
            "Title"
            "Title - Artist"
            "Artist - Title - id"
    """
    from youtube_dl.YoutubeDL import YoutubeDL
    from six import StringIO
    from .common import make_fake_info_dict
    from .extractors import get_info_extractor
    import urlparse

# Generated at 2022-06-14 18:07:08.692624
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Create a Mock downloader
    downloader = MockDownloader()

    # Create the pp and call its run
    pp = MetadataFromTitlePP(downloader, '%(title)s')
    assert pp.run({})[1] == {}
    assert pp.run({'title':'abc'})[1] == {'title':'abc'}
    pp = MetadataFromTitlePP(downloader, '%(title)s - %(artist)s')
    assert pp.run({'title':'abc'})[1] == {'title':'abc'}
    assert pp.run({'title':'abc - def'})[1] == {'title':'abc','artist':'def'}

# Generated at 2022-06-14 18:07:17.815222
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.utils import sanitize_open
    from tests.testhelper import (
        FakeYDL,
        unwatch_urlretrieve,
        retcode,
        force_print
    )

    # Setting up the test
    test_ydl = FakeYDL()
    test_ydl.params['writethumbnail'] = True
    test_ydl.params['writeinfojson'] = True
    test_ydl.params['writedescription'] = True
    test_ydl.params['writeannotations'] = True
    test_ydl.params['no_warnings'] = True
    test_ydl.params['noplaylist'] = True
    test_ydl.params['format'] = 'best'

# Generated at 2022-06-14 18:07:29.399011
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    title = 'Bieber - Baby ft. Ludacris'
    _downloader = None
    titleformat = '%(artist)s - %(title)s'
    pp = MetadataFromTitlePP(_downloader, titleformat)
    info = {'title': title}
    assert (pp.run(info) == ([], {'title': title, 'artist': 'Bieber',
                                  'title': 'Baby ft. Ludacris'}))
    title = 'Bieber - Baby ft. Ludacris (Official Music Video)'
    _downloader = None
    titleformat = '%(artist)s - %(title)s'
    pp = MetadataFromTitlePP(_downloader, titleformat)
    info = {'title': title}

# Generated at 2022-06-14 18:07:37.779206
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    """Unit test for method run of class MetadataFromTitlePP."""

    # Arrange
    from youtube_dl.YoutubeDL import YoutubeDL
    ydl = YoutubeDL()
    ydl.add_default_info_extractors()
    pp = MetadataFromTitlePP(ydl, '%(title)s - %(artist)s')
    pp.downloader = ydl
    info = {
        'title': 'Catch My Breath - Kelly Clarkson',
        'artist': '',
        'track': '',
        'album': ''
    }

    # Act
    pp.run(info)

    # Assert
    assert info['title'] == 'Catch My Breath'
    assert info['artist'] == 'Kelly Clarkson'
    assert info['track'] == ''
    assert info['album'] == ''


# Generated at 2022-06-14 18:07:46.911852
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .extractor.common import InfoExtractor
    from .downloader.fakedl import FakeFD

    class FakeInfo(InfoExtractor):
        def __init__(self):
            pass

        @classmethod
        def suitable(cls, url):
            return True


# Generated at 2022-06-14 18:07:57.671501
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import youtube_dl
    from youtube_dl.utils import sanitize_filename
    testYdl = youtube_dl.YoutubeDL({'outtmpl': '%(title)s-%(id)s-%(ext)s'})
    testYdl.add_info_extractor(youtube_dl.FileDownloader({'title': 'test'}))
    testYdl._ies = []

    # sample test videos

# Generated at 2022-06-14 18:08:07.638783
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import Downloader
    from .extractor import YoutubeIE
    from .compat import compat_urllib_parse_unquote


# Generated at 2022-06-14 18:08:19.740357
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    pp = MetadataFromTitlePP(None, '%(title)s - %(artist)s')
    # Test with simple title
    info = {'title': 'Python - The Queen'}
    expected_info = {'title': 'Python', 'artist': 'The Queen'}
    assert pp.run(info)[1] == expected_info
    # Test with extra brackets
    info = {'title': 'Python (Beginners Tutorial) - The Queen'}
    expected_info = {'title': 'Python (Beginners Tutorial)',
                     'artist': 'The Queen'}
    assert pp.run(info)[1] == expected_info
    # Test with unknown attribute
    pp = MetadataFromTitlePP(None, '%(title)s - %(xyz)s')

# Generated at 2022-06-14 18:08:24.221825
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ..YoutubeDL import YoutubeDL
    postprocessor = MetadataFromTitlePP(YoutubeDL(), '%(title)s - %(artist)s')
    info = {
        'title': 'TITLE - ARTIST',
        'other_attribute': 'SOME_VALUE',
    }
    postprocessor.run(info)
    return info



# Generated at 2022-06-14 18:08:31.292749
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.downloader import YoutubeDL
    from youtube_dl.utils import DateRange
    from youtube_dl.compat import compat_str
    import nose.tools

    # Set up
    downloader = YoutubeDL(params={'writesubtitles': True,
                                   'writeautomaticsub': True,
                                   'skip_download': True})
    titleformat = '%(title)s (%(codec)s)'
    title = 'Title (codec)'
    info = {'title': title}
    postprocessor = MetadataFromTitlePP(downloader, titleformat)

    # Run
    result, info = postprocessor.run(info)
    nose.tools.assert_equal(result, [])
    nose.tools.assert_equal(info['title'], title)
    nose.tools.assert_equal