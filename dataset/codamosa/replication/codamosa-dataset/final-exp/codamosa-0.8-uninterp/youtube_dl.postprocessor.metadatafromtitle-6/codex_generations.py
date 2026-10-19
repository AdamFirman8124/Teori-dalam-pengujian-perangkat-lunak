

# Generated at 2022-06-14 17:58:37.485709
# Unit test for method format_to_regex of class MetadataFromTitlePP
def test_MetadataFromTitlePP_format_to_regex():
    from .__main__ import ytdl_format
    from .compat import compat_str
    from .extractor import gen_extractors
    from .utils import prepend_extension
    ytdlfmt = ytdl_format('bestvideo[ext=webm]+bestaudio[ext=m4a]')
    ie = gen_extractors().next()
    ie._downloader = None
    ie.set_downloader(None)
    ytdlfmt.set_downloader(ie)
    assert(ytdlfmt._format_to_regex('%(title)s.%(ext)s')
           == '(?P<title>.+)\.(?P<ext>.+)')

# Generated at 2022-06-14 17:58:45.388442
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    errStr = 'MetadataFromTitlePP test failed'
    from . import YoutubeDL

    class DummyDownloader(YoutubeDL):
        def __init__(self, params):
            super(DummyDownloader, self).__init__(params)
            self.to_screen = lambda *args: None

    # titleformat does not contain regex
    ydl = DummyDownloader({'writedescription': True, 'outtmpl': r'%(title)s-%(id)s.%(ext)s'})
    metadataFromTitlePP = MetadataFromTitlePP(ydl, '%(artist)s - %(title)s - %(album)s')

# Generated at 2022-06-14 17:58:57.493218
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FakeYDL
    from youtube_dl.extractor import YoutubeIE

    def test_run_pp(titleformat, title, expected_result):
        pp = MetadataFromTitlePP(FakeYDL(), titleformat)
        info = {
            'title': title,
            'timestamp': '1414485422',
            'extractor': YoutubeIE.ie_key(),
            'id': 'test_id',
            'ext': 'test_ext',
            'format_id': 'test_fmt',
            'format': 'test_format',
            'url': '',
            'player_url': '',
        }
        _, result = pp.run(info)

# Generated at 2022-06-14 17:59:03.395790
# Unit test for method format_to_regex of class MetadataFromTitlePP
def test_MetadataFromTitlePP_format_to_regex():
    obj = MetadataFromTitlePP(None, '%(artist)s - %(title)s')
    assert obj.format_to_regex('%(artist)s - %(title)s') == '(?P<artist>.+)\ \-\ (?P<title>.+)'
    assert obj.format_to_regex('%(title)s - %(artist)s') == '(?P<title>.+)\ \-\ (?P<artist>.+)'

# Generated at 2022-06-14 17:59:12.022924
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    def assert_info_fields(info, fields):
        for key, value in fields.items():
            assert key in info
            assert value == info[key]

    youtube_dl = YoutubeDL()
    metadata_pp = MetadataFromTitlePP(youtube_dl, '%(title)s - %(artist)s')

    info = {
        'id': 'test_id',
        'title': 'test_title',
        'ext': 'test_extension',
        'webpage_url': 'test_url',
        'playlist_index': '0',
        '_filename': 'test_filename',
        'format': 'bestvideo[ext=webm]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    }

   

# Generated at 2022-06-14 17:59:23.327039
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import pytest
    from .common import FakeYDL
    from .test_extractor_common import TestIE, TestInfoExtractor

    class MockExtractor(TestIE):
        def __init__(self, url, title):
            super(MockExtractor, self).__init__(url)
            self.test_title = title

        def _real_extract(self, url):
            return {'id': '123', 'title': self.test_title}

    class TestInfoExtractor(TestInfoExtractor):
        def _real_extract(self, url):
            return {'id': '123', 'title': self.test_title}

    patcher = pytest.importorskip('youtube_dl.extractor.common')
    patcher.InfoExtractor = TestInfoExtractor
    patcher.Youtube

# Generated at 2022-06-14 17:59:34.080375
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    """Verify conversion from title format string to regex"""
    assert MetadataFromTitlePP(None, '%(title)s')._titleregex == '(?P<title>.+)'
    assert MetadataFromTitlePP(None, '%(title)s - %(artist)s')._titleregex == '(?P<title>.+)\ \-\ (?P<artist>.+)'
    assert MetadataFromTitlePP(None, r'%(title)s - %(artist)s')._titleregex == '(?P<title>.+)\ \-\ (?P<artist>.+)'
    assert MetadataFromTitlePP(None, r'%(title)s - %(artist)s')._titleregex == '(?P<title>.+)\ \-\ (?P<artist>.+)'

# Generated at 2022-06-14 17:59:43.955804
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    metadata_dict = {'title': 'shani shingnapur - shani dev jayanti - shani dev songs - bhakti songs'}
    metadata_from_titlepp = MetadataFromTitlePP('downloader',
                                                'shani shingnapur - shani dev jayanti - shani dev songs - bhakti songs')
    metadata_dict = metadata_from_titlepp.run(metadata_dict)
    assert metadata_dict[0] == {}
    assert metadata_dict[1]['title'] == 'shani shingnapur - shani dev jayanti - shani dev songs - bhakti songs'


# Generated at 2022-06-14 17:59:47.846027
# Unit test for method format_to_regex of class MetadataFromTitlePP
def test_MetadataFromTitlePP_format_to_regex():
    fmt = '%(title)s - %(artist)s'
    re = '(?P<title>.+)\ \-\ (?P<artist>.+)'
    assert MetadataFromTitlePP(None,None).format_to_regex(fmt) == re
    assert MetadataFromTitlePP(None,None).format_to_regex(re) == re

# Generated at 2022-06-14 17:59:55.104857
# Unit test for method format_to_regex of class MetadataFromTitlePP
def test_MetadataFromTitlePP_format_to_regex():
    mftpp = MetadataFromTitlePP(None, None)


# Generated at 2022-06-14 18:00:08.612541
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FileDownloader
    from .extractor import get_info_extractor
    from .extractor.youtube import YoutubeIE
    from .utils import HEADRequest
    import shutil
    import tempfile

    tempdir = tempfile.mkdtemp()
    downloader = FileDownloader({'outtmpl': '%(title)s', 'verbose': True, 'quiet': True, 'format': 'bestaudio', 'extractaudio': True, 'audioformat': 'mp3', 'audioquality': 9, 'nooverwrites': True, 'noplaylist': True, 'outtmpl': os.path.join(tempdir, '%(title)s')})
    downloader.add_info_extractor(get_info_extractor(YoutubeIE.ie_key()))
    downloader.add_post_processor

# Generated at 2022-06-14 18:00:13.515809
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    mp = MetadataFromTitlePP(None, '%(artist)s - %(song)s')
    info = {'title': 'A-Ha - Take On Me'}
    assert mp.run(info) == ([], info)


# Generated at 2022-06-14 18:00:25.970200
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .test import get_test_instance
    from .extractor.youtube import YoutubeIE
    from .jsinterp import JSInterpreter

    def _test_interp(code):
        return JSInterpreter(code, YoutubeIE.js_to_json)('id').encode('ascii', 'ignore')

    ydl = get_test_instance()
    titleformat = '%(artist)s - %(title)s'
    title_regex = ('(?P<artist>.+) - (?P<title>.+)'
                   if re.search(r'%\(\w+\)s', titleformat)
                   else titleformat)
    pp = MetadataFromTitlePP(ydl, titleformat)
    title = 'Chance The Rapper ft. Saba - Angels (Official Video)'

# Generated at 2022-06-14 18:00:36.811969
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    info = {'title': 'Foo - Bar'}
    pp = MetadataFromTitlePP(None, '%(artist)s - %(title)s')
    pp.run(info)
    assert info['title'] == 'Bar'
    assert info['artist'] == 'Foo'

    info = {'title': 'Foo - Bar - Baz'}
    pp = MetadataFromTitlePP(None, '%(artist)s - %(title)s')
    pp.run(info)
    assert info['title'] == 'Bar'
    assert info['artist'] == 'Foo - Baz'

    info = {'title': 'Foo - Bar - Baz'}
    pp = MetadataFromTitlePP(None, '%(artist)s - %(title)s - %(test)s')

# Generated at 2022-06-14 18:00:46.294923
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Test method run of class MetadataFromTitlePP
    # MetadataFromTitlePP (class) object (object of type 'type')
    # Test method run of class MetadataFromTitlePP with different arguments
    # Test method run of class MetadataFromTitlePP with different arguments
    # Test method run of class MetadataFromTitlePP with different arguments
    # Test method run of class MetadataFromTitlePP with different arguments
    # Test method run of class MetadataFromTitlePP with different arguments
    # Test method run of class MetadataFromTitlePP with different arguments
    # Test method run of class MetadataFromTitlePP with different arguments
    # Test method run of class MetadataFromTitlePP with different arguments
    # Test method run of class MetadataFromTitlePP with different arguments

    _titleformat = '%(title)s - %(artist)s'
    _titlere

# Generated at 2022-06-14 18:00:54.146977
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    """
    Tests that MetadataFromTitlePP correctly parses the title
    """
    class FakeDownloader:
        def to_screen(self, message):
            print(message)

    fake_downloader = FakeDownloader()
    fake_info = {'title': 'Test-title - testartist'}
    metadata_from_title_PP = MetadataFromTitlePP(fake_downloader, '%(title)s - %(artist)s')
    metadata_from_title_PP.run(fake_info)
    assert fake_info.get('title') == 'Test-title'
    assert fake_info.get('artist') == 'testartist'



# Generated at 2022-06-14 18:01:06.815081
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.postprocessor import FFmpegMetadataPP

    info = {'title': 'test video'}
    postprocessors = [
        {
            'key': 'FFmpegMetadataPP'
        },
        {
            'key': 'MetadataFromTitlePP',
            'format': 'test - %(title)s'
        }
    ]
    ydl = YoutubeDL({'postprocessors': postprocessors})
    ydl.add_post_processor(FFmpegMetadataPP(ydl))
    ydl.add_post_processor(MetadataFromTitlePP(ydl, 'test - %(title)s'))
    res = ydl.process_ie_result(info)
    assert res is True

# Generated at 2022-06-14 18:01:12.326548
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ytdl.extractor.common import InfoExtractor
    from ytdl.utils import DateRange

    # Test with a title like 'abc - xyz'
    ie = InfoExtractor('youtube')
    pp = MetadataFromTitlePP(ie, '%(title)s - %(artist)s')
    info = {'title': 'abc - xyz'}
    pp.run(info)
    assert info == {
        'title': 'abc',
        'artist': 'xyz',
    }

    # Test with a title like 'Artist - Title'
    ie = InfoExtractor('youtube')
    pp = MetadataFromTitlePP(ie, '%(artist)s - %(title)s')
    info = {'title': 'Artist - Title'}
    pp.run(info)

# Generated at 2022-06-14 18:01:23.555860
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import unittest

    class MetadataFromTitlePPTest(unittest.TestCase):
        def test_run_method(self):
            # assert at the end of this function if valid
            # empty info dict
            info = {}

            # empty title
            postprocessor = MetadataFromTitlePP(None, '')
            postprocessor.run(info)
            self.assertEquals({}, info)

            # title not matching
            info = {}
            postprocessor = MetadataFromTitlePP(None, '%(v0)s')
            postprocessor.run(info)
            self.assertEquals({}, info)

            # title matching single group
            info = {'title': 'v0'}
            postprocessor = MetadataFromTitlePP(None, '%(v0)s')
            postprocessor.run(info)


# Generated at 2022-06-14 18:01:33.154236
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.postprocessor import run_pp
    result = run_pp(['%(artist)s - %(track)s - %(title)s'],
            'Rammstein - Ich Will - Official Video', {})
    assert result['artist'] == 'Rammstein'
    assert result['track'] == 'Ich Will'
    assert result['title'] == 'Official Video'
    error_result = run_pp(['%(artist)s - %(track)s - %(title)s'],
            'Rammstein - Official Video', {})
    assert error_result['errorcount'] == 1
    assert 'Could not interpret title' in error_result['errormessage']

# Generated at 2022-06-14 18:01:42.477264
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    title = 'Metallica - Hero of the Day (Live in Paris)'
    titleformat = '%(artist)s - %(title)s (%(live)s in %(location)s)'
    info = {'title': title}
    pp = MetadataFromTitlePP(None, titleformat)
    pp.run(info)
    assert info['artist'] == 'Metallica'
    assert info['title'] == 'Hero of the Day'
    assert info['live'] == 'Live'
    assert info['location'] == 'Paris'


# Generated at 2022-06-14 18:01:55.819026
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from . import YoutubeDL
    from collections import namedtuple

    # create mock objects
    downloader = YoutubeDL(params={})
    class MockInfo: pass
    info = MockInfo()
    # set 'title' attribute of info
    info.title = 'test title'

    # test with invalid titleformat
    with youtube_dl.utils.bug_reports.catch_logs() as logs:
        pp = MetadataFromTitlePP(downloader, 'invalid titleformat')
        pp.run(info)
        assert len(logs) == 1

    # set 'title' attribute of info
    info.title = 'test title'

    # test with valid titleformat
    pp = MetadataFromTitlePP(downloader, '%(title)s')
    info_result, info_mock = pp.run(info)

    #

# Generated at 2022-06-14 18:02:03.745318
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import youtube_dl
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.utils import DateRange
    from youtube_dl.compat import compat_str

    class DummyYDL(YoutubeDL):
        def __init__(self, *args, **kwargs):
            self.extractors = []
            self.params = {}
            self.cache = {}
            self.to_screen = print

    def test():
        ydl = DummyYDL()
        ydl.add_post_processor(
            MetadataFromTitlePP(ydl, '%(title)s - %(artist)s'))


# Generated at 2022-06-14 18:02:15.142618
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():

    import json
    import six
    import sys

    json_info = {
        'title': 'Test title - Test artist',
        'alt_title': 'Alt test title - Alt test artist',
    }

    # Save sys.stderr (to restore later)
    old_stderr = sys.stderr

    # Mock methods
    class MockScreen(object):
        def __init__(self):
            self._lines = []

        def to_screen(self, line):
            self._lines.append(line)

    class MockDownloader(object):
        def __init__(self):
            self._screen = MockScreen()

        @property
        def to_screen(self):
            return self._screen.to_screen


# Generated at 2022-06-14 18:02:27.244664
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Test case with two groups: %(title)s, %(artist)s
    downloader = PostProcessor()
    pp = MetadataFromTitlePP(downloader, '%(title)s - %(artist)s')
    info = {'title': 'Video title - Video artist'}
    result = pp.run(info)
    assert result == ([], {'title': 'Video title - Video artist', 'artist': 'Video artist'})

    # Test case with only one group: %(title)s
    pp = MetadataFromTitlePP(downloader, '%(title)s')
    info = {'title': 'Video title'}
    result = pp.run(info)
    assert result == ([], {'title': 'Video title', 'title': 'Video title'})

    # Test case with group that is not in the

# Generated at 2022-06-14 18:02:33.881436
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    titleformat = '%(title)s - %(artist)s'
    titleformat2 = '%(artist)s - %(title)s - %(album)s - %(track)s'

    pp = MetadataFromTitlePP(None, titleformat)
    assert pp.format_to_regex(titleformat) == '(?P<title>.+)\\ \\-\\ (?P<artist>.+)'
    assert pp.format_to_regex(titleformat2) == '(?P<artist>.+)\\ \\-\\ (?P<title>.+)\\ \\-\\ (?P<album>.+)\\ \\-\\ (?P<track>.+)'

    # Test with titleformat with 0 fields
    info = {'title': 'test'}
    titleformat = ''
    pp = MetadataFromTitlePP(None, titleformat)

# Generated at 2022-06-14 18:02:38.817220
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    '''
    Test method MetadataFromTitlePP.run
    '''
    pp = MetadataFromTitlePP(None, '%(title)s - %(artist)s')
    info = {'title': 'MyTitle - MyArtist'}
    [], returned_info = pp.run(info)
    assert returned_info['title'] == 'MyTitle'
    assert returned_info['artist'] == 'MyArtist'


# Generated at 2022-06-14 18:02:47.039525
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    downloader = YoutubeDL()
    pp = MetadataFromTitlePP(downloader, "%(artist)s - %(track)s")
    assert pp.run({'title': 'foo - bar'}) == ([], {'artist': 'foo', 'track': 'bar'})
    assert pp.run({'title': 'foo - bar - baz'}) == ([], {'artist': 'foo', 'track': 'bar - baz'})
    assert pp.run({'title': 'foo - bar'}) == ([], {'artist': 'foo', 'track': 'bar'})
    assert pp.run({'title': 'foo - bar - baz'}) == ([], {'artist': 'foo', 'track': 'bar - baz'})
    
    downloader = YoutubeDL()

# Generated at 2022-06-14 18:02:52.832056
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    youtube_dl = YoutubeDLMock({'title': 'Test - Test'})
    pp_obj = MetadataFromTitlePP(youtube_dl, '%(title)s - %(artist)s')
    assert pp_obj.run({})[1]['artist'] == 'Test'
    assert pp_obj.run({'title': 'Test - Test2'})[1]['artist'] == 'Test2'


# Generated at 2022-06-14 18:03:03.268664
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # interface of class InfoExtractingPP subclasses requires this to be set
    downloader = None

    # no regex
    pp = MetadataFromTitlePP(downloader, 'mytitle')
    assert pp._titleregex == 'mytitle'

    # regex
    pp = MetadataFromTitlePP(downloader, '%(title)s - %(artist)s')
    assert pp._titleregex == '(?P<title>.+)\\ \\-\\ (?P<artist>.+)'

    # test run
    info = {
        'title': 'mytitle',
        'other': 'other',
    }
    assert len(pp.run(info)[0]) == 0
    assert pp.run(info)[1] == info
    assert pp.run(info)[1]['title'] == 'mytitle'
    assert pp.run

# Generated at 2022-06-14 18:03:12.613396
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    """Unit test for method test_MetadataFromTitlePP_run"""

    from .YoutubeDL import YoutubeDL
    from .extractor.generic import GenericIE
    from .postprocessor.ffmpeg import FFmpegPostProcessor

    class MyGenericIE(GenericIE):

        _VALID_URL = r'http://(?:www\.)?example\.com/.*'

    def _download(url):
        return """
        {
            "id": "testid",
            "title": "%s",
            "formats": [
                {
                    "format": "mp4",
                    "filesize": 1024,
                    "url": "http://example.com/test.mp4"
                }
            ]
        }
        """ % url


# Generated at 2022-06-14 18:03:21.848542
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ytdl_server import YoutubeDL
    info = {'title': 'abcd'}
    pp = MetadataFromTitlePP(YoutubeDL(), '%(title)s')
    assert pp.run(info) == ([], info)

    pp = MetadataFromTitlePP(YoutubeDL(), '%(title)s - %(name)s')
    info = {'title': 'abcd - efgh'}
    assert pp.run(info) == ([], {'title': 'abcd', 'name': 'efgh'})
    assert pp.run(info) == ([], {'title': 'abcd', 'name': 'efgh'})

# Generated at 2022-06-14 18:03:29.602240
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ..YoutubeDL import YoutubeDL
    from ..extractor.common import InfoExtractor
    from ..utils import DateRange

    class FakeYoutubeDL(YoutubeDL):
        def __init__(self, *args, **kwargs):
            self.params = kwargs
            self._screen_file = None

        def to_screen(self, message):
            print(message)

    class FakeInfoExtractor(InfoExtractor):
        def __init__(self, ydl, *args, **kwargs):
            self.ydl = ydl
            self.ydl.add_default_info_extractors()

        def _real_extract(self, url):
            return {'id': 'test_id', 'title': 'Test title'}


# Generated at 2022-06-14 18:03:40.145284
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Preparation
    import sys
    import time
    import youtube_dl
    from youtube_dl.utils import DownloadError

    class MockYoutubeDL(object):
        def __init__(self):
            self.download_retcode = 0
            self.to_screen_list = []

        class FileDownloader(object):
            def __init__(self, ydl, filename, info_dict):
                self.ydl = ydl
                self.filename = filename
                self.info_dict = info_dict

            def to_screen(self, msg):
                self.ydl.to_screen_list.append(msg)

            def report_error(self, msg, tb=None):
                raise YoutubeDLHandlerError(msg)

        def to_screen(self, msg):
            self.to_screen_list.append

# Generated at 2022-06-14 18:03:46.337919
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FakeYDL

    downloader = FakeYDL()
    downloader.add_info_extractor('youtube', {'extractor': 'Generic'})
    pp = MetadataFromTitlePP(downloader, '%(title)s - %(creator)s')
    info = pp.run({'title': 'Check this out - YouTubers'})[1]
    assert info == {
        'creator': 'YouTubers',
        'title': 'Check this out',
    }

# Generated at 2022-06-14 18:03:48.230906
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    import os
    import tempfile
    import io

# Generated at 2022-06-14 18:03:59.182732
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import pytest
    from ..compat import compat_urllib_error

    class FakeInfoDict(dict):
        def __init__(self, title, **kw):
            super(FakeInfoDict, self).__init__(**kw)
            self['title'] = title

    class FakeYDL(object):
        def __init__(self):
            self.to_screen_called = False

        def to_screen(self, msg):
            # self.to_screen_called = True
            pass

    class TestException(compat_urllib_error.HTTPError):
        def __init__(self, *args, **kwargs):
            super(TestException, self).__init__(*args, **kwargs)
            self.code = 500
            self.msg = 'Internal Server Error'
            self.hd

# Generated at 2022-06-14 18:04:10.900583
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys

    if sys.version_info >= (3, 0):
        from io import StringIO
        import html
    else:
        from StringIO import StringIO
        import HTMLParser as html

    # The try/except block is just to get around a Python bug.
    # See http://bugs.python.org/issue6122
    try:
        from yt_dl.extractor.common import InfoExtractor
    except ImportError:
        class InfoExtractor(object):
            pass
    try:
        from yt_dl.downloader import Downloader
    except ImportError:
        class Downloader(object):
            pass

    from yt_dl.postprocessor import MetadataFromTitlePP

    class MockIE(InfoExtractor):

        def __init__(self, info):
            self._info = info


# Generated at 2022-06-14 18:04:21.750963
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ..compat import parse_qs
    from ..utils import encodeArgument

    downloader = object()
    info = {
        'title': 'Adele - Rolling in the Deep',
        'format': 'audio',
        'fulltitle': 'Adele - Rolling in the Deep',
        'id': 'jkFhLo7Veds',
    }

    # Extract only title and artist
    pp = MetadataFromTitlePP(downloader, '%(title)s - %(artist)s')
    formats, info = pp.run(info)
    assert formats == []
    assert info['title'] == 'Rolling in the Deep'
    assert info['artist'] == 'Adele'
    assert info['format'] == 'audio'
    assert info['fulltitle'] == 'Adele - Rolling in the Deep'

# Generated at 2022-06-14 18:04:32.196795
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Test regex matching
    regex = MetadataFromTitlePP.format_to_regex('foo%(bar)s')
    m = re.match(regex, 'foo1')
    assert m is not None
    assert m.groupdict() == {'bar': '1'}
    m = re.match(regex, 'foo')
    assert m is None
    m = re.match(regex, 'fooaabb')
    assert m is not None
    assert m.groupdict() == {'bar': 'aabb'}
    m = re.match(regex, '1')
    assert m is None

    # Test dict merging
    metadata = {}
    title = 'foo - bar'
    title_format = '%(foo)s - %(bar)s'
    metadata_from_title = MetadataFrom

# Generated at 2022-06-14 18:04:45.921273
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import youtube_dl
    import unittest

    class TestYDL(youtube_dl.YoutubeDL):
        def to_screen(self, msg):
            print(msg)


# Generated at 2022-06-14 18:04:53.870214
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    ydl = MockYdl()
    pp = MetadataFromTitlePP(ydl, '%(title)s - %(artist)s - %(album)s (%(year)s)')
    info = {'title': 'Metropolis - Blue Man Group - The Complex (2003)'}
    errlist = []
    pp.run(info)
    assert len(errlist) == 0
    assert info['title'] == 'Metropolis'
    assert info['artist'] == 'Blue Man Group'
    assert info['album'] == 'The Complex'
    assert info['year'] == '2003'



# Generated at 2022-06-14 18:05:03.412750
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # test with a single group
    titleformat = "%(title)s"
    title = 'Test'
    ydl = object()
    pp = MetadataFromTitlePP(ydl, titleformat)
    info = {'title': title}
    pp.run(info)
    if info['title'] != title:
        raise Exception('test_MetadataFromTitlePP_run failed - error in test with a single group')
    info = {}
    pp.run(info)
    if info['title'] == title:
        raise Exception('test_MetadataFromTitlePP_run failed - single group worked but should not')

    # test with several groups
    titleformat = "%(title)s-%(artist)s"
    title = 'Test-Artist'
    ydl = object()

# Generated at 2022-06-14 18:05:10.487559
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Init class at first
    import youtube_dl
    import os
    import tempfile

    # Create a temporary directory with file url.txt inside
    tempdir = tempfile.mkdtemp()
    with open(os.path.join(tempdir, 'urls.txt'), 'w') as f:
        f.write('https://www.youtube.com/watch?v=DkfLXCQ9QKQ\n')
        f.write('http://www.dailymotion.com/video/x3q3h93\n')
        f.write('http://www.dailymotion.com/playlist/x2mn2y\n')
        f.write('https://soundcloud.com/baz')

    # Dummy options

# Generated at 2022-06-14 18:05:15.611486
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    assert MetadataFromTitlePP.run(None,
      { 'title': 'Song - Artist' }, # Info for an arbitrary video
      '%(title)s - %(artist)s'     # Title format that should parse the above
    ) == ( # Info with parsed title, artist and date.
       [],
       { 'title': 'Song',
         'artist': 'Artist',
      })

# Generated at 2022-06-14 18:05:26.679879
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import os
    import tempfile
    from .xattrfile import XAttrMetadataPP
    from .execafterdownload import ExecAfterDownloadPP

    def file_len(fname):
        with open(fname) as f:
            for i, l in enumerate(f):
                pass
        return i + 1

    def compare_file_contents(fname, contents):
        with open(fname, 'r') as f:
            actual = ''.join(f.readlines())
        return actual == contents

    def compare_file_attributes(fname, attr_dict):
        return all(attr_dict[attr] == XAttrMetadataPP.get_xattr(fname, attr)
                   for attr in attr_dict)


# Generated at 2022-06-14 18:05:32.510522
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    downloader = []

# Generated at 2022-06-14 18:05:44.475058
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import youtube_dl
    pp = MetadataFromTitlePP(youtube_dl.YoutubeDL(), 'Something %(artist)s - %(title)s')
    info = {'title': 'xxxc', 'uploader': 'xxxa', 'uploader_url': 'xxxb', 'title': 'yyyc', 'artist': 'yyya', 'album': 'yyyb'}
    # change the title to 'Something yyya - yyyc'
    videoinfo, newinfo = pp.run(info)
    assert info == {'title': 'xxxc', 'uploader': 'xxxa', 'uploader_url': 'xxxb', 'title': 'yyyc', 'artist': 'yyya', 'album': 'yyyb'}

# Generated at 2022-06-14 18:05:55.514793
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():

    class DummyDownloader:
        def __init__(self):
            self._screen = ''

        def to_screen(self, msg):
            self._screen += msg + '\n'

        @property
        def screen(self):
            return self._screen

    info = {'title': 'mytitle'}
    assert not MetadataFromTitlePP(
        DummyDownloader(),
        r'%(title)s - %(artist)s'
    ).run(info)[1]

    info = {'title': 'mytitle - myartist'}
    assert MetadataFromTitlePP(
        DummyDownloader(),
        r'%(title)s - %(artist)s'
    ).run(info)[1] == info

    info = {'title': 'myartist - mytitle'}
    assert MetadataFrom

# Generated at 2022-06-14 18:06:04.459447
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL

    # Test 1: Test string with all the supported fields
    ydl = YoutubeDL()
    ydl.add_post_processor(MetadataFromTitlePP(ydl, '%(title)s-%(artist)s-%(album)s-%(track)s-%(track_number)s-%(genre)s-%(release_date)s-%(release_year)s'))
    info = dict(title='A-B-C-D-12-E-F-1979')
    infos, info = ydl.post_process(info)
    assert(info['title'] == 'A-B-C-D-12-E-F-1979')
    assert(info['artist'] == 'A')
    assert(info['album'] == 'B')

# Generated at 2022-06-14 18:06:21.458537
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.downloader.common import FileDownloader
    fd = FileDownloader(YoutubeDL({'outtmpl': '%(title)s-%(id)s-%(format_id)s.%(ext)s'}), {})
    pp = MetadataFromTitlePP(fd, '%(id)s - %(title)s')
    info = {'title': 'y3o5by5p5yA - yt_dummy_title'}
    (r1, r2) = pp.run(info)
    assert r1 == []
    assert r2['id'] == 'y3o5by5p5yA'
    assert r2['title'] == 'yt_dummy_title'

    pp = MetadataFromTitle

# Generated at 2022-06-14 18:06:31.223094
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.PostProcessor import PostProcessor
    post_processor = MetadataFromTitlePP(YoutubeDL(), '%(artist)s - %(title)s')
    info = {'title': 'John Doe - Song Title'}
    assert post_processor.run(([], info)) == (([], {'artist': 'John Doe', 'title': 'Song Title'}))
    info = {'title': 'John Doe - Song Title'}
    assert post_processor.run(([], info)) == (([], {'artist': 'John Doe', 'title': 'Song Title'}))
    info = {'title': 'John Doe - Song Title ft. Jane Doe'}

# Generated at 2022-06-14 18:06:42.872238
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FILE_EXISTS_SINGLE, postprocessors

    class DummyIE:
        def __init__(self):
            self.ie_key = 'DummyIE'

    pp = postprocessors.get('metadatafromtitle', DummyIE())
    assert pp is not None, 'no PostProcessor found'

    info_in = {'title': 'Dummy Title'}
    assert pp.run(info_in) == ([],info_in)

    pp = postprocessors.get('metadatafromtitle:%(title)s', DummyIE())
    assert pp is not None, 'no PostProcessor found'

    info_in = {'title': 'Dummy Title'}
    info_out = {'title': 'Dummy Title'}

# Generated at 2022-06-14 18:06:52.035859
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class FakeInfoDict(dict):
        pass

    class FakeInfoExtractor(object):
        @staticmethod
        def _print_warning(message):
            pass

        def to_screen(self, message):
            pass

    titleformats = ['%(title)s',
                    '%(artist)s/%(title)s',
                    '%(artist)s-%(album)s-%(title)s',
                    '%(artist)s-%(album)s-%(disc)s-%(track)s-%(title)s',
                    '%(artist)s-%(album)s-%(disc)s-%(track)s-%(artist)s-%(title)s']

# Generated at 2022-06-14 18:07:03.464864
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .dummy_downloader import DummyDownloader
    from .dummy_extractor import DummyExtractor
    from .extractor.common import InfoExtractor

    class DummyIE(InfoExtractor):
        _TITLE_RE = r'(?P<year>\d{4}) - (?P<month>\d{2}) - (?P<day>\d{2})'
        def _real_extract(self, url):
            return { 'id': 'dummy', 'title': url }

    InfoExtractor.register_class(DummyIE)
    downloader = DummyDownloader()

    titleformat = '%(year)s - %(month)s - %(day)s'
    title = '2013 - 04 - 07'

# Generated at 2022-06-14 18:07:15.587268
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class Downloader:
        def to_screen(self, msg):
            print(msg)

    pp = MetadataFromTitlePP(Downloader(), '%(artist)s - %(title)s')
    assert pp._titleregex == '(?P<artist>.+)\ \-\ (?P<title>.+)'

    info = {'title': 'Max Richter - Infra'}
    result, info = pp.run(info)
    assert result == []
    assert info == {'title': 'Max Richter - Infra', 'artist': 'Max Richter'}

    info = {'title': 'Max Richter - Infra and 5'}
    result, info = pp.run(info)
    assert result == []

# Generated at 2022-06-14 18:07:27.630494
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class TestClass:
        def __init__(self):
            self.titles = []
            self.titles.append(('TestTitle - TestArtist',
                               {'title': 'TestTitle - TestArtist',
                                'artist': 'TestArtist',
                                'track': 'TestTitle'}))
            self.titles.append(('TestTitle ft. TestArtist - TestTrack',
                               {'title': 'TestTitle ft. TestArtist - TestTrack',
                                'track': 'TestTitle ft. TestArtist',
                                'artist': 'TestTrack'}))
            self.titles.append(('TestTitle - TestArtist - TestTrack',
                               {'title': 'TestTitle - TestArtist - TestTrack',
                                'artist': 'TestArtist - TestTrack',
                                'track': 'TestTitle'}))

# Generated at 2022-06-14 18:07:34.893120
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    mft = MetadataFromTitlePP(None, '%(title)s (%(artist)s)')
    # test title parsing
    assert mft.run({'title': 'song (artist)'})[1] == {'title': 'song', 'artist': 'artist'}
    assert mft.run({'title': 'audio (artist)'})[1] == {'title': 'audio', 'artist': 'artist'}
    # test string escaping
    mft = MetadataFromTitlePP(None, '%(title)s \& %(artist)s')
    assert mft.run({'title': 'normal'})[1] == {'title': 'normal'}
    assert mft.run({'title': 'song & artist'})[1] == {'title': 'song', 'artist': 'artist'}

# Generated at 2022-06-14 18:07:43.360599
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import pytube
    yt = pytube.YouTube('https://www.youtube.com/watch?v=n9rujYng1-k')
    video = yt.get('mp4', '720p')

    class MockDownloader:
        def to_screen(self, message):
            assert message is not None

    # Test with '%(artist)s - %(title)s' format
    pp = MetadataFromTitlePP(MockDownloader(), '%(artist)s - %(title)s')
    assert pp._titleformat == '%(artist)s - %(title)s'
    assert pp._titleregex == '(?P<artist>.+)\ \-\ (?P<title>.+)'
    info = video._video_referrer

# Generated at 2022-06-14 18:07:53.931299
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    import StringIO

    _stdout = sys.stdout
    sys.stdout = StringIO.StringIO()

    from .common import FakeYDL
    from .downloader import Downloader

    # tag_only
    data = [
        {'title': 'Something'},
        {'title': 'Artist - Something'},
        {'title': 'Artist - Something feat. Someone'},
        {'title': 'Artist - Something feat. Someone, Someone else'},
        {'title': 'Artist - Something (feat. Someone)'},
        {'title': 'Artist - Something ft. Someone'},
        {'title': 'Artist - Something (ft. Someone)'},
    ]

# Generated at 2022-06-14 18:08:11.670931
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import Downloader
    downloader = Downloader()
    from .YoutubeDL import YoutubeDL
    ydl = YoutubeDL(downloader=downloader)
    post_processor = MetadataFromTitlePP(downloader=downloader,
                                         titleformat='%(artist)s - %(title)s')
    info = {}
    info['title'] = 'Jamiroquai - Space Cowboy'
    new_info = {}
    new_info['title'] = 'Jamiroquai - Space Cowboy'
    new_info['artist'] = 'Jamiroquai'
    expected_result = ([], new_info)
    result = post_processor.run(info)
    assert result == expected_result


# Generated at 2022-06-14 18:08:22.007702
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # import needed modules
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.utils import DateRange
    from youtube_dl.compat import compat_os_name

    # setup the debug logger
    class Logger(object):
        def debug(self, *args):
            # python3 compatibility: all strings in logs are converted to unicode,
            # so we must take this into account.
            return print(args[0] % args[1:])


# Generated at 2022-06-14 18:08:33.517518
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.downloader import common
    pp = MetadataFromTitlePP(common.Downloader(), '%(title)s')
    info = {'title': 'test title'}

    file_infos, new_info = pp.run(info)
    assert new_info == {'title': 'test title'}

    pp = MetadataFromTitlePP(common.Downloader(), '%(artist)s - %(title)s')
    info = {'title': 'test title'}

    file_infos, new_info = pp.run(info)
    assert new_info == {'title': 'test title'}

    pp = MetadataFromTitlePP(common.Downloader(), '%(artist)s - %(title)s')
    info = {'title': 'test artist - test title'}

    file