

# Generated at 2022-06-14 17:58:40.881086
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Test the format_to_regex method
    pp = MetadataFromTitlePP(None, '')
    assert pp.format_to_regex('%(title)s') == r'(?P<title>.+)'
    assert pp.format_to_regex('%(one)s:%(two)s:%(three)s') == r'(?P<one>.+):(?P<two>.+):(?P<three>.+)'
    assert pp.format_to_regex('%%(title)s') == '%%(title)s'
    assert pp.format_to_regex('%(title)s%%') == r'(?P<title>.+)%'

# Generated at 2022-06-14 17:58:51.080867
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import youtube_dl
    import copy
    import re
    # Create an instance of MetadataFromTitlePP
    parser = MetadataFromTitlePP(youtube_dl, '%(artist)s - %(title)s')
    # test regex conversion
    regex = r'(?P<artist>.+)\ \-\ (?P<title>.+)'
    assert parser._titleregex == regex
    # test that regex is a substitute for format
    parser.run(
        {'title': 'Kendrick Lamar - Bitch Don\'t Kill My Vibe [Official Video]'})
    parser.run(
        {'title': 'Kendrick Lamar - Bitch Dont Kill My Vibe Official Video'})
    # test for status messages

# Generated at 2022-06-14 17:59:01.809065
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    import os.path
    import unittest
    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
    from you_get.common import FileDownloader
    from you_get.extractors import youtube as youtube_extractor

    # For this unit test, we need a real URL available
    test_url = 'https://www.youtube.com/watch?v=BaW_jenozKc'

    class TestDownloader(FileDownloader):
        def __init__(self):
            FileDownloader.__init__(self, params={})
            self.to_screen = lambda msg: None
        def report_warning(self, msg):
            self.warning_msg = msg


# Generated at 2022-06-14 17:59:11.112871
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    # YoutubeDL does not exist anymore, so we use a mock instead
    downloader = type('YoutubeDLMock_test_MetadataFromTitlePP_run', (object,), {})
    def to_screen(self, msg):
        print('to_screen: ' + str(msg))
    downloader.to_screen = to_screen
    downloader.to_stderr = downloader.to_screen


# Generated at 2022-06-14 17:59:22.551171
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class FakeDl(object):
        def __init__(self):
            self.to_screen_calls = []
        def to_screen(self, arg):
            self.to_screen_calls.append(arg)

    title_format = '%(artist)s - %(song)s'

    title_match_artist = 'Test Title - Test Artist'
    title_match_artist_song = 'Test Title - Test Artist - Test Song'
    title_match_artist_song_2 = 'Test Title - Test Artist - Test Song 2'
    title_match_song = 'Test Title - Test Song'
    title_match_song_2 = 'Test Title - Test Song 2'
    title_match_nothing = 'Test Title'

    dl = FakeDl()

# Generated at 2022-06-14 17:59:30.833881
# Unit test for constructor of class MetadataFromTitlePP
def test_MetadataFromTitlePP():
    pp = MetadataFromTitlePP(None, '%(title)s')
    assert pp._titleformat == '%(title)s'
    assert pp._titleregex == '(?P<title>.+)'

    pp = MetadataFromTitlePP(None, '%(title)s - %(artist)s')
    assert pp._titleformat == '%(title)s - %(artist)s'
    assert pp._titleregex == '(?P<title>.+)\ \-\ (?P<artist>.+)'

    pp = MetadataFromTitlePP(None, '%(artist)s - %(title)s')
    assert pp._titleformat == '%(artist)s - %(title)s'
    assert pp._titleregex == '(?P<artist>.+)\ \-\ (?P<title>.+)'



# Generated at 2022-06-14 17:59:42.381014
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import unittest
    class _FakeYDL:
        def to_screen(self, *args, **kwargs):
            pass

    class ParsingTest(unittest.TestCase):
        def runTest(self):
            ydl = _FakeYDL()
            p = MetadataFromTitlePP(ydl, '%(title)s - %(artist)s')
            info = {
                'title': 'Bach: Brandenburg Concerto No. 4 in G, Movement I (Allegro), BWV 1049'
            }
            p.run(info)
            self.assertEqual(
                info, {
                    'title': 'Bach: Brandenburg Concerto No. 4 in G',
                    'artist': 'Movement I (Allegro), BWV 1049'
                })
            # Test parsing of escaped characters

# Generated at 2022-06-14 17:59:48.923462
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl import YoutubeDL
    ydl = YoutubeDL({'quiet': True, 'simulate': True})
    pp = MetadataFromTitlePP(ydl, '%(title)s - %(artist)s')
    info_dict = {'title': 'title - artist', 'artist': 'original artist'}
    pp.run(info_dict)
    assert info_dict['artist'] == 'title'



# Generated at 2022-06-14 17:59:56.043762
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    sys.path.insert(0, '../..')
    from ydl.downloader.YDLDownloader import YDLDownloader
    from ydl.postprocessors.MetadataFromTitlePP import MetadataFromTitlePP
    dl = YDLDownloader()
    dl.params['writethumbnail'] = True
    dl.params['writeinfojson'] = True
    dl.params['outtmpl'] = '%(title)s %(uploader)s %(height)s'
    dl.params['ignoreerrors'] = True
    dl.to_screen = lambda x: sys.stderr.write(x + '\n')

    pp = MetadataFromTitlePP(dl, '%(title)s %(uploader)s')

# Generated at 2022-06-14 18:00:03.526073
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    ydl = YoutubeDL()
    titleformat = '%(title)s - %(artist)s'
    pp = MetadataFromTitlePP(ydl, titleformat)
    info = {'title': 'Test - ydl'}
    assert pp.run(info) == ([], {'artist': 'ydl', 'title': 'Test'})

    ydl = YoutubeDL()
    titleformat = '%(title)s @ %(upload_date)s'
    pp = MetadataFromTitlePP(ydl, titleformat)
    info = {'title': 'Test @ 2014'}
    assert pp.run(info) == ([], {'upload_date': '2014', 'title': 'Test'})

# Generated at 2022-06-14 18:00:14.104455
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Test command line
    classOptions = {'titleformat': '%(uploader)s'}
    ydl = None
    pp = MetadataFromTitlePP(ydl, classOptions['titleformat'])
    # Test title
    title = 'Test title'
    # Test interpretation without any format
    info = {'title': title}
    (formats, new_info) = pp.run(info)
    assert(new_info['title'] == title)
    # Test interpretation with a format that is the same as the title
    info = {'title': title}
    (formats, new_info) = pp.run(info)
    assert(new_info['title'] == title)
    assert(new_info['uploader'] is None)
    # Test interpretation with a format that is different to the title

# Generated at 2022-06-14 18:00:25.672925
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class FakeInfo(dict):
        pass

    class FakeConfig(object):
        pass

    class FakeYDL(object):
        def __init__(self):
            self.params = FakeConfig()
            self.params.get = lambda _: None


# Generated at 2022-06-14 18:00:36.529452
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    assert MetadataFromTitlePP(None, '%(title)s - %(artist)s').run(
        {'title': 'VIDEO TITLE - ARTIST NAME'}) == ([],
        {'title': 'VIDEO TITLE', 'artist': 'ARTIST NAME'})
    assert MetadataFromTitlePP(None, '%(title)s - %(artist)s').run(
        {'title': 'VIDEO TITLE - ARTIST NAME - YEAR'}) == ([],
        {'title': 'VIDEO TITLE', 'artist': 'ARTIST NAME'})

# Generated at 2022-06-14 18:00:46.626491
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    titlefmt = '%(title)s [%(quality)s] [%(ext)s]'
    PP = MetadataFromTitlePP(None, titlefmt)

# Generated at 2022-06-14 18:00:57.578594
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.downloader.common import FileDownloader

    pp = MetadataFromTitlePP(FileDownloader(None), '%(title)s - %(format)s')
    assert pp.format_to_regex('%(title)s - %(format)s') == \
        r'(?P<title>.+)\ \-\ (?P<format>.+)'
    info = {'title': 'Test - 1'}
    _, info = pp.run(info)
    assert info == {'title': 'Test', 'format': '1'}
    info['title'] = 'Test - 1s'
    _, info = pp.run(info)
    assert info == {'title': 'Test', 'format': '1s'}
    info['title'] = 'Test - 1 - 2'
    _

# Generated at 2022-06-14 18:01:09.116419
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FileDownloader
    from .extractor import gen_extractors
    gen_extractors()

    class FakeYDL:
        def __init__(self, downloader):
            self.downloader = downloader
        def to_screen(self, *args, **kargs):
            pass

    fd = FileDownloader({})
    fd.add_info_extractor(FakeIE())
    fydl = FakeYDL(fd)
    fd.add_post_processor(MetadataFromTitlePP(fydl, '%(title)s'))

    assert fd.post_process([{"format":"hi"}]) == ([{"format":"hi", "title":"title_in_json"}], {})
    assert fd.post_process([{}]) == ([{}], {})

# Generated at 2022-06-14 18:01:20.237547
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ytdl_server.compat import compat_urllib_request

    # Mocking the downloader class to easily access the info dictionary
    class DummyDL(object):
        def __init__(self, title, titleformat):
            self.info = {
                'title': title,
            }
            self.to_screen('')  # supresses the info message

        def to_screen(self, msg):
            pass  # supress to_screen messages

    # Test data

# Generated at 2022-06-14 18:01:32.022934
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys

    # Create an instance of MetadataFromTitlePP
    metadata_from_title_pp = MetadataFromTitlePP(
        'dummy_downloader', '%(artist)s - %(title)s')

    # Create result video info to test
    video_info = {
        'title': 'Title A - Title B',
    }

    # Unparsed info should be returned as is and no output
    # to stderr
    result = metadata_from_title_pp.run(video_info)

    assert 'artist' in video_info
    assert video_info['artist'] == 'Title A'

    assert 'title' in video_info
    assert video_info['title'] == 'Title B'

    assert result == ([], video_info)

# Generated at 2022-06-14 18:01:39.409337
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    title = 'Bach: Violin Concertos 1 & 2'
    titleformat = '%(artist)s: %(title)s'
    titleformat_regex = (
        '(?P<artist>.+)\: (?P<title>.+)')

    metadata_from_title_pp = MetadataFromTitlePP(
        downloader = None,
        titleformat = titleformat)

    # call the run method of MetadataFromTitlePP
    info = {}
    info['title'] = title
    [], info = metadata_from_title_pp.run(info)

    assert info['artist'] == 'Bach'
    assert info['title'] == 'Violin Concertos 1 & 2'
    assert metadata_from_title_pp._titleformat == titleformat
    assert metadata_from_title_pp._titleregex == titleformat_

# Generated at 2022-06-14 18:01:47.720974
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from collections import namedtuple
    from youtube_dl.downloader.common import FileDownloader
    info = {'title':'123 - 456 - 789'}
    fd = FileDownloader()
    mft = MetadataFromTitlePP(fd, '%(title)s - %(artist)s')
    new_info = mft.run(info)
    assert info['title'] == '123 - 456 - 789'
    assert info['artist'] == '123 - 456'


# Generated at 2022-06-14 18:01:59.834990
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import os
    import tempfile

    from ..YoutubeDL import YoutubeDL
    from ..utils import DateRange

    class Result:
        def __init__(self, info):
            self.info = info

    def _run_MetadataFromTitlePP(title, titleformat, expected_info,
                                 expected_warnings):
        tfn = tempfile.NamedTemporaryFile(delete=False).name
        info = {
            'title': title,
            'display_id': 'dummy_id',
            '_filename': tfn,
        }
        downloader = YoutubeDL(params={'writethumbnail': True})
        downloader.add_info_extractor(DummyIE(info))
        downloader.add_post_processor(MetadataFromTitlePP(downloader, titleformat))

# Generated at 2022-06-14 18:02:08.784239
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Init mocks
    class TestDownloader(object):
        def __init__(self):
            self.to_screen_messages = []

        def to_screen(self, message):
            self.to_screen_messages.append(message)

    testDownloader = TestDownloader()

    # Init postprocessor
    pp = MetadataFromTitlePP(testDownloader, '%(name)s - %(family)s')

    # Test empty info
    info = {}
    info = pp.run(info)[1]
    assert info == {}, 'Output info should be empty when no title is set'
    assert len(testDownloader.to_screen_messages) == 0, \
        'Should not output any messages when no title is set'

    # Test not a match

# Generated at 2022-06-14 18:02:19.131109
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import unittest
    import sys
    # pylint: disable=unused-import
    from youtube_dl.compat import compat_str
    # pylint: enable=unused-import

    if sys.version_info < (2, 7):
        import unittest2 as unittest

    class Info:
        def __init__(self, title):
            self['title'] = title

    class MessageLogger:
        def __init__(self):
            self._msgs = []

        def to_screen(self, msg):
            self._msgs.append(msg)

    class Downloader:
        pass

    class FakePostProcessor(PostProcessor):
        def __init__(self, downloader, titleformat):
            super(FakePostProcessor, self).__init__(downloader)
           

# Generated at 2022-06-14 18:02:31.531061
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import time
    import unittest
    class MockYDL(object):
        def to_screen(self, *args):
            pass
    class MockInfoDict(dict):
        def __init__(self, *args, **kwargs):
            dict.__init__(self, *args, **kwargs)
    class MockFD(object):
        def __init__(self, size=1):
            self.size = size
    info = MockInfoDict(title='Peter Gabriel - Sledgehammer - OFFICIAL Music Video')
    ydl = MockYDL()
    fd = MockFD()
    pp = MetadataFromTitlePP(ydl, '%(title)s - %(artist)s - %(musicvideo)s')
    t0 = time.time()
    [fd], info = pp.run(info)

# Generated at 2022-06-14 18:02:43.238334
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.utils import DateRange

    class FakeInfo(object):
        pass

    class FakeYdl(object):
        def to_screen(self, msg):
            pass

    class FakeInfoDict(dict):
        get = None

    class FakeDate(object):
        pass

    fake_downloader = FakeYdl()
    fake_info = FakeInfo()
    fake_info.title = 'C.R.A.Z.Y. - Trailer'
    fake_info.date = DateRange(datetime(2005, 1, 1), datetime(2006, 1, 1))

    fake_downloader.to_screen = (
        lambda msg: print(msg)
    )

    pp = MetadataFromTitlePP(fake_downloader, '%(title)s - %(artist)s')

# Generated at 2022-06-14 18:02:49.679237
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    """Unit test, testing class MetadataFromTitlePP"""
    from youtube_dl.utils import DateRange
    # Test case: given a title format, videos are parsed correctly
    class FakeDownloader:
        def __init__(self):
            self.to_screen_content = []

        def to_screen(self, str):
            self.to_screen_content.append(str)

    fake_downloader = FakeDownloader()
    fake_post_processor_1 = MetadataFromTitlePP(
        fake_downloader,
        '%(artist)s-%(title)s-%(track)s-%(album)s-%(year)s-%(month)s-%(day)s')

    # Case 1: All fields are in a title

# Generated at 2022-06-14 18:02:58.152784
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import youtube_dl.YoutubeDL
    ydl = youtube_dl.YoutubeDL({})
    ydl.params['writethumbnail'] = False
    titleformat = '%(title)s - %(artist)s'
    title = 'Test - TestTest'
    info = {'title': title}

    pp = MetadataFromTitlePP(ydl, titleformat)
    pp.run(info)

    assert info['title'] == 'Test'
    assert info['artist'] == 'TestTest'


# Generated at 2022-06-14 18:03:07.032843
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.downloader import YoutubeDL
    downloader = YoutubeDL()
    # Test format with no substitution
    pp = MetadataFromTitlePP(downloader, 'title')
    info = {'title': 'Test title'}
    res = pp.run(info)
    assert res == ([], info)
    # Test format with no substitution and title does not match
    pp = MetadataFromTitlePP(downloader, 'title')
    info = {'title': 'Test title does not match'}
    res = pp.run(info)
    assert res == ([], info)
    # Test format with no substitution but still incorrect due to the presence of a %
    pp = MetadataFromTitlePP(downloader, '%title')
    info = {'title': 'Test title'}
    res = pp.run(info)
   

# Generated at 2022-06-14 18:03:16.722319
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    """
    Test that video title is correctly parsed.
    """
    from collections import namedtuple
    from ytdl.YoutubeDL import YoutubeDL
    # Video object for test
    Video = namedtuple('Video', ['id_', 'title'])

    # Test parsing
    titleformat = '%(title)s - %(artist)s'
    title = 'Video - Artist'
    pp = MetadataFromTitlePP(YoutubeDL(), titleformat)
    result = pp.run({'id': 'videoid', 'title': title})[1]

    # Check result
    assert result['title'] == 'Video'
    assert result['artist'] == 'Artist'

    # Test title format that cannot be matched
    titleformat = '%(title)s. %(artist)s'
    title = 'Video - Artist'
   

# Generated at 2022-06-14 18:03:27.239114
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import youtube_dl
    metadata = {'title': 'title - artist - album'}
    downloader = youtube_dl.YoutubeDL({})
    pp = MetadataFromTitlePP(downloader, '%(title)s - %(artist)s - %(album)s')
    pp.run(metadata)
    assert metadata == {'title': 'title', 'artist': 'artist', 'album': 'album'}

    metadata = {'title': 'title - artist'}
    pp = MetadataFromTitlePP(downloader, '%(title)s - %(artist)s - %(album)s')
    pp.run(metadata)
    assert metadata == {'title': 'title', 'artist': 'artist', 'album': None}

    metadata = {'title': 'title - artist'}
    pp = MetadataFromTitle

# Generated at 2022-06-14 18:03:40.053765
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .extractor.common import InfoExtractor
    import logging
    import unittest

    class FakeDownloader(object):
        def to_screen(self, msg):
            pass

    class FakeInfoExtractor(InfoExtractor):

        IE_NAME = 'FakeInfoExtractor'

        def _real_extract(self, url):
            return {'id': url}

    class TestMetadataFromTitlePP(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
            cls._log_handler = logging.StreamHandler()
            cls._log_handler.setLevel(logging.DEBUG)

        def setUp(self):
            self._downloader = FakeDownloader()


# Generated at 2022-06-14 18:03:49.083832
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .youtube_dl import YoutubeDL
    from .extractor.youtube import YoutubeIE
    from .postprocessor.ffmpeg import FFmpegMetadataPP


# Generated at 2022-06-14 18:04:00.824034
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    sys.argv = ['youtube-dl', '--print-json', 'https://www.youtube.com/watch?v=ZBK9Ucmd-Og']
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.postprocessor.common import PostProcessor
    import json
    import unittest
    import re

    class MockPostProcessor(PostProcessor):

        def __init__(self, downloader):
            super(MockPostProcessor, self).__init__(downloader)

        def run(self, info):
            assert info['title'] == 'Metallica - Nothing else matters (video)'

    class MockYoutubeDL(YoutubeDL):

        def __init__(self):
            super(MockYoutubeDL, self).__init__()


# Generated at 2022-06-14 18:04:10.420963
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # test information about a video
    info = {'title': 'Music Video - North Korea - 2012'}
    # init class MetadataFromTitlePP
    t = MetadataFromTitlePP(None, '%(title)s - %(country)s - %(year)s')
    # run class MetadataFromTitlePP
    t.run(info)
    # check results
    check = {'title': 'Music Video', 'country': 'North Korea', 'year': '2012'}
    assert info == check

    # test information about a video
    info = {'title': 'Music Video - North Korea - NA'}
    # init class MetadataFromTitlePP
    t = MetadataFromTitlePP(None, '%(title)s - %(country)s - %(year)s')
    # run class MetadataFromTitlePP


# Generated at 2022-06-14 18:04:21.307483
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.postprocessor import FFmpegMetadataPP

    downloader = YoutubeDL(params={'quiet': True})
    downloader.add_post_processor(FFmpegMetadataPP(downloader, {'artist': 'artist', 'title': 'title'}))

    mp3_format = {'ext': 'mp3', 'preferredcodec': 'mp3', 'preferredquality': '0', 'container': 'mp3'}
    mp4_format = {'ext': 'mp4', 'preferredcodec': 'mp4', 'preferredquality': '0', 'container': 'mp4'}

    formats = [mp3_format, mp4_format]

# Generated at 2022-06-14 18:04:31.782465
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ..compat import compat_urllib_error
    from ..downloader import FakeYDL
    from ..extractor import get_info_extractor
    from ..utils import parse_query
    from .common import FileDownloader
    from .embedthumbnail import EmbedThumbnailPP
    from .execafterdownload import ExecAfterDownloadPP
    from .metadatafromtitle import MetadataFromTitlePP
    from .xattrpp import XAttrMetadataPP

    # In this test we verify that 'run' of class MetadataFromTitlePP
    # works fine. When 'run' method is called, it is passed an info
    # dictionary 'info' as argument. When it finishes, it returns
    # a tuple with an empty list (first element) and the same info
    # dictionary that it was passed as argument (second element).
    # Therefore, we can use this

# Generated at 2022-06-14 18:04:38.765225
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    mp = MetadataFromTitlePP(None, '%(title)s - %(artist)s')
    mp._titleregex = '(?P<title>.+)\ \-\ (?P<artist>.+)'
    info = {'title': 'abc - def'}
    assert mp.run(info) == ([], {'title': 'abc', 'artist': 'def'})

# Generated at 2022-06-14 18:04:49.266718
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class FakeInfo:
        def __init__(self, title, videoid, uploader):
            self.title = title
            self.videoid = videoid
            self.uploader = uploader
    class FakeDownloader:
        def to_screen(self, message):
            print('to_screen: %s' % message)

    # Test with a regex that matches
    titleformat = '%(title)s - %(uploader)s [%(videoid)s]'
    title = 'Test Title - Test Uploader [TestVideoId]'
    assert MetadataFromTitlePP.format_to_regex(titleformat) == title
    info = FakeInfo(title, 'TestVideoId', 'Test Uploader')
    downloader = FakeDownloader()
    pp = MetadataFromTitlePP(downloader, titleformat)
    infos

# Generated at 2022-06-14 18:04:56.405787
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ..compat import compat_str
    pp = MetadataFromTitlePP(None, '%(artist)s - %(title)s')
    assert pp.run({'title': 'foo'}) == ([], {'title': 'foo'})
    
    assert pp.run({'title': 'foo - bar - baz'}) == ([], {'title': 'foo - bar - baz'})
    
    assert pp.run({'title': 'foo - bar'}) == ([], {'title': 'foo - bar', 'artist': 'foo', 'title': 'bar'})
    
    assert pp.run({'title': compat_str('foo - bar')}) == ([], {'title': compat_str('foo - bar'), 'artist': compat_str('foo'), 'title': compat_str('bar')})

# Unit test

# Generated at 2022-06-14 18:05:07.734503
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # testclass that implements method to_screen
    class DummyDownloader(object):
        def to_screen(self, text):
            pass

    # testclass that implements method run of class PostProcessor
    class DummyPP(object):
        def __init__(self, downloader):
            self.downloader = downloader

    pp = MetadataFromTitlePP(DummyDownloader(), '%(title)s - %(artist)s')

# Generated at 2022-06-14 18:05:23.009403
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class FakeDownloader:
        def to_screen(self, msg):
            pass

    # Testing object MetadataFromTitlePP for titleformat '%(title)s - %(artist)s'
    # where title is 'MyTitle - MyArtist'
    titleformat = '%(title)s - %(artist)s'
    title = 'MyTitle - MyArtist'
    info = {'title': title}
    metadata_from_title_pp = MetadataFromTitlePP(FakeDownloader(), titleformat)
    expected = {'title': 'MyTitle', 'artist': 'MyArtist'}
    res = metadata_from_title_pp.run(info)
    # Check that all values of expected are found in info, ignoring others
    for attribute, value in expected.items():
        assert info[attribute] == value

# Generated at 2022-06-14 18:05:31.223344
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    dl = {'ydl': None}
    # Build fake info object
    info = {'title': 'foo - bar'}
    # Format title to regex
    pp = MetadataFromTitlePP(dl, '%(title)s - %(artist)s')
    # Get regex
    regex = pp._titleregex
    # Should match
    assert re.match(regex, info['title'])
    # Run postprocessor
    res = pp.run(info)
    # Separator and attribute name removed
    assert info['title'] == 'foo'
    assert info['artist'] == 'bar'
    # No warnings
    assert res[0] == []

# Generated at 2022-06-14 18:05:36.638905
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    title = 'FooBar - Baz'
    info = {'title': title}
    fromtitlepp = MetadataFromTitlePP(object, '%(artist)s - %(song)s')
    info = fromtitlepp.run(info)[1]
    assert info['artist'] == 'FooBar'
    assert info['song'] == 'Baz'


# Generated at 2022-06-14 18:05:46.408210
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from six.moves import UserDict
    # create dummy downloader object
    class DummyDownloader(object):
        def to_screen(self, message):
            print(message)
    downloader = DummyDownloader()
    # create dummy info dict
    info = UserDict.UserDict()
    # test
    pp = MetadataFromTitlePP(downloader, '%(artist)s - %(title)s')
    info['title'] = 'Groove Coverage - Poison (Official Video)'
    pp.run(info)
    # expect
    assert info['artist'] == 'Groove Coverage'
    assert info['title'] == 'Poison (Official Video)'


# Generated at 2022-06-14 18:05:55.781876
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    testcases = [
        # (title, result)
        ('once - north atlantic drift [9m2i]', {'title': 'once', 'artist': 'north atlantic drift', 'something': '9m2i'}),
        ('once', None),
        ('[9m2i] once - north atlantic drift', {'title': 'once', 'artist': 'north atlantic drift', 'something': '9m2i'}),
        ('once - north atlantic drift', None),
    ]

    from youtube_dl.YoutubeDL import YoutubeDL
    ydl = YoutubeDL(dict(writeinfojson=True, logtostderr=True))
    pp = MetadataFromTitlePP(ydl, '%(something)s %(title)s - %(artist)s')

# Generated at 2022-06-14 18:06:04.356639
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ..YoutubeDL import YoutubeDL
    titleformat = r'%(artist)s - %(track)s - %(title)s'
    title = r'The Who - Baba O\'Riley - Who Are You?'

    test_downloader = YoutubeDL()
    test_downloader.params['simulate'] = True
    test_downloader.params['quiet'] = True

    mftpp = MetadataFromTitlePP(test_downloader, titleformat)
    info = {}
    info['title'] = title
    mftpp.run(info)

    expected_result = {
        'artist': 'The Who',
        'track': r"Baba O'Riley",
        'title': 'Who Are You?',
    }
    assert(expected_result == info)

# Generated at 2022-06-14 18:06:12.527086
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FakeYDL
    fakeydl = FakeYDL()
    mp = MetadataFromTitlePP(fakeydl, '%(title)s - %(artist)s')

    info = {'title': 'my title', 'artist': 'my artist'}
    result = mp.run(info)
    match = re.match(mp._titleregex, info['title'])
    assert mp._titleformat == '%(title)s - %(artist)s'
    assert mp._titleregex == '(?P<title>.+)\ \-\ (?P<artist>.+)'
    assert match.groupdict() == {'title': 'my title', 'artist': 'my artist'}
    assert result == ([], info)


# Generated at 2022-06-14 18:06:19.948434
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    """
    Tests method run of class MetadataFromTitlePP
    """
    downloader = None
    info = {'title': 'The title'}
    titleformat = '%(title)s'
    PP = MetadataFromTitlePP(downloader, titleformat)
    result, more_info = PP.run(info)
    assert result == []
    assert type(more_info) is dict
    assert more_info['title'] == 'The title'


# Generated at 2022-06-14 18:06:29.908255
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    import unittest

    if sys.version_info.major == 2:
        import mock
    else:
        from unittest import mock

    class FakeYDL(object):
        def to_screen(self, value):
            print(value)
    pp = MetadataFromTitlePP(FakeYDL(), '%(artist)s - %(song)s')

    expected_first = {}
    info = {'title': 'Test Artist - Test Song'}
    actual = pp.run(info)
    expected = ([], expected_first)
    assert actual == expected

    expected_first = {'artist': 'Test Artist', 'song': 'Test Song'}
    info = {'title': 'Test Artist - Test Song'}
    actual = pp.run(info)
    expected = ([], expected_first)


# Generated at 2022-06-14 18:06:30.465395
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    pass

# Generated at 2022-06-14 18:06:49.989242
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # parameter of method run (class MetadataFromTitlePP)
    info = {'title': 'name of video'}
    # parameters of constructor
    titleformat = '%(name)s of %(thing)s'
    titleregex = '(?P<name>.+)\ of\ (?P<thing>.+)'

    # Create instance of PostProcessor
    metadata_from_title_pp = MetadataFromTitlePP(None, titleformat)

    # Set private variable _titleregex with regex
    metadata_from_title_pp._titleregex = titleregex

    # Call run method
    res = metadata_from_title_pp.run(info)

    assert(res[1]['name'] == 'name' and res[1]['thing'] == 'video')

# Generated at 2022-06-14 18:06:55.417872
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # init PostProcessor instance
    from youtube_dl.YoutubeDL import YoutubeDL
    ydl = YoutubeDL()
    pp = MetadataFromTitlePP(ydl, '%(artist)s - %(title)s')
    # init test values
    info = {'title': 'Suede - Attitude'}
    # verify that video title is not set from metadata
    assert 'artist' not in info
    assert 'title' not in info
    # process with PostProcessor
    pp.run(info)
    # verify that video title is set from metadata
    assert info['artist'] == 'Suede'
    assert info['title'] == 'Attitude'

# Generated at 2022-06-14 18:07:01.055206
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    downloader = object()
    METADATA_FROM_TITLE_PP = MetadataFromTitlePP(downloader, '%(title)s - %(artist)s')
    info = {'title': 'Hello, World - Paul McCartney'}
    METADATA_FROM_TITLE_PP.run(info)
    assert info['title'] == 'Hello, World'
    assert info['artist'] == 'Paul McCartney'

# Generated at 2022-06-14 18:07:08.911450
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    """
    Tests for method run of class MetadataFromTitlePP
    """
    from ytdl.YoutubeDL import YoutubeDL

    # Known title and titleformat
    titleformat = '%(album)s - %(artist)s - %(title)s'
    info = {'title': 'Some Album - Some Artist - Some Title'}
    parser = MetadataFromTitlePP(YoutubeDL(), titleformat)
    info = parser.run(info)[1]
    expected = {
        'album': 'Some Album',
        'artist': 'Some Artist',
        'title': 'Some Title'
    }
    assert(info == expected)

    # Unknown title
    titleformat = '%(album)s - %(artist)s - %(title)s'

# Generated at 2022-06-14 18:07:18.603211
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import unittest
    import sys

    if sys.version_info < (2, 7):
        import unittest2 as unittest
    else:
        import unittest

    class TestPostProcessor(unittest.TestCase):
        def setUp(self):
            # Create a PostProcessor with a format string
            self.test_pp = MetadataFromTitlePP(None, "%(artist)s - %(title)s")
            # Create sample info dictionaries
            self.test_info = {
                "title": "Artist - Title",
            }

        def testFormatToRegex(self):
            regex = self.test_pp.format_to_regex(
                "%(artist)s - %(title)s")

# Generated at 2022-06-14 18:07:29.828939
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import unittest
    import sys
    # silence output
    if sys.version_info < (3, 0):
        import logging
    else:
        import logging.handlers
    stream = logging.StreamHandler(open('/dev/null', 'w'))
    logger = logging.getLogger('youtube_dl')
    logger.addHandler(stream)
    logger.setLevel(logging.DEBUG)
    class DummyYTDLLogger(object):
        def to_screen(self, *args):
            pass
    class DummyYTDL(object):
        def __init__(self):
            self.logger = DummyYTDLLogger()

# Generated at 2022-06-14 18:07:38.302047
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import Downloader
    from .extractor import YoutubeIE

    # Create a Downloader object that only saves the processed information
    class DummyDl(Downloader):
        def to_screen(self, text):
            self.output = text

        def to_stderr(self, text):
            self.output = text

    dl = DummyDl(params={})
    dl.add_info_extractor(YoutubeIE())

    # Test for an invalid format string
    dl.params['writesubtitles'] = True
    dl.params['subtitleslang'] = 'en'
    pp = MetadataFromTitlePP(dl, titleformat='%(title)s')
    info = {'title': 'VIDEO_TITLE'}
    pp.run(info)
    print(info)


# Generated at 2022-06-14 18:07:45.524611
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FileDownloader
    from .extractor import gen_extractors
    youtubeDL = FileDownloader({})
    youtubeDL.add_info_extractor(gen_extractors())

# Generated at 2022-06-14 18:07:55.152896
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    """
    Unit test for method run of class MetadataFromTitlePP
    """
    from youtube_dl.YoutubeDL import YoutubeDL

    class FakeDLA:
        def __init__(self):
            self.to_screen_value = ''

        def to_screen(self, msg):
            self.to_screen_value += msg

    ydl = YoutubeDL({})

    # empty title
    info = {'title': '', 'format': 'mp3'}
    ydl.add_post_processor(MetadataFromTitlePP(FakeDLA(), '%(title)s - %(artist)s'))
    pp_result = ydl.post_process(info, {'f': '-'})
    assert pp_result[1].get('title', None) is None

    # title without metadata

# Generated at 2022-06-14 18:08:03.061937
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Given
    from youtube_dl.YoutubeDL import YoutubeDL
    class FakeInfoDict(dict):
        def __init__(self, d):
            self.update(d)
    info = FakeInfoDict({'title': 'foo - bar'})
    p = MetadataFromTitlePP(YoutubeDL(), '%(title)s - %(artist)s')
    # When
    p.run(info)
    # Then
    expected_result = FakeInfoDict({
        'title': 'foo',
        'artist': 'bar',
    })
    assert info == expected_result

# Generated at 2022-06-14 18:08:35.731007
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    """
    Tests the method run of class MetadataFromTitlePP
    """
    # Imports
    from tempfile import mkstemp
    from youtube_dl.downloader import FileDownloader

    # Arrange
    # Create a FileDownloader
    downloader = FileDownloader({'format': 'bestaudio/best',
                                'outtmpl': '%(title)s-%(id)s.%(ext)s'})

    # Create an instance of MetadataFromTitlePP
    pp = MetadataFromTitlePP(downloader, '%(title)s-%(artist)s')
    info = {
        'title': '[MV] IU(아이유) _ BBIBBI(삐삐)',
    }

    # Act