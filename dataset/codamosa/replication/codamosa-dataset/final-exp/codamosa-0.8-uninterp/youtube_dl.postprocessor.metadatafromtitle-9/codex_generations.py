

# Generated at 2022-06-14 17:58:38.008189
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # For testing, 'test' is the only extractor supported.
    info = {'title': 'Testing passed!'}
    downloader = FakeDownloader()

    #Title format has no %(..)s. This is invalid.
    pp = MetadataFromTitlePP(downloader, 'title')
    res, info = pp.run(info)
    assert pp._titleregex == 'title'
    # Returned info is unmodified.
    assert info['title'] == 'Testing passed!'
    assert len(res) == 0

    #Title format has %(title)s.
    pp = MetadataFromTitlePP(downloader, '%(title)s')
    res, info = pp.run(info)
    assert pp._titleregex == r'(?P<title>.+)'
    # Returned info has 'title' attribute

# Generated at 2022-06-14 17:58:44.294961
# Unit test for constructor of class MetadataFromTitlePP
def test_MetadataFromTitlePP():
    assert re.match(MetadataFromTitlePP(None, '%(title)s')._titleregex, 'test')
    assert re.match(MetadataFromTitlePP(None, '%(title)s - %(artist)s')._titleregex, 'test - test')
    assert re.match(MetadataFromTitlePP(None, '%(title)s - %(artist)s')._titleregex, 'test - test - test - test')
    assert re.match(MetadataFromTitlePP(None, '%(title)s')._titleregex, 'test - test - test')
    assert re.match(MetadataFromTitlePP(None, '%(title)s')._titleregex, 'test-test')



# Generated at 2022-06-14 17:58:47.280729
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import Downloader
    f = Downloader(params={})
    t = MetadataFromTitlePP(f, '%(title)s - %(artist)s')
    inf = {'title': 'title - artist'}
    t.run(inf)
    assert inf['title'] == 'title'
    assert inf['artist'] == 'artist'


# Generated at 2022-06-14 17:58:58.010084
# Unit test for constructor of class MetadataFromTitlePP
def test_MetadataFromTitlePP():
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.PostProcessor import PostProcessor

    ydl = YoutubeDL()
    ydl.add_post_processor(MetadataFromTitlePP(ydl, '%(title)s'))
    ydl.add_post_processor(MetadataFromTitlePP(ydl, '%(title)s - %(artist)s'))
    ydl.add_post_processor(MetadataFromTitlePP(ydl, '%(artist)s - %(title)s'))
    ydl.add_post_processor(MetadataFromTitlePP(ydl, '%(artist)s'))
    ydl.add_post_processor(MetadataFromTitlePP(ydl, '(?P<artist>.+?)\ -\ (?P<title>.+)'))


# Generated at 2022-06-14 17:59:08.227171
# Unit test for method format_to_regex of class MetadataFromTitlePP
def test_MetadataFromTitlePP_format_to_regex():
    assert 'a\?b' == MetadataFromTitlePP(None, 'a?b').format_to_regex('a?b')
    assert 'a\\|b' == MetadataFromTitlePP(None, 'a|b').format_to_regex('a|b')
    assert r'(?P<title>.+) (?P<artist>.+) \- (?P<composer>.+)' == MetadataFromTitlePP(None, '%(title)s %(artist)s - %(composer)s').format_to_regex('%(title)s %(artist)s - %(composer)s')

# Generated at 2022-06-14 17:59:13.287937
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    ydl = YoutubeDL({'writethumbnail': True})
    ydl.add_post_processor(MetadataFromTitlePP(ydl, '%(title)s - %(artist)s'))
    result = ydl.extract_info('http://www.youtube.com/watch?v=6v2L2UGZJAM', download=False)
    assert result['title'] == 'Foster The People - Pumped up Kicks'
    assert result['artist'] == 'Foster The People'

# Generated at 2022-06-14 17:59:23.820968
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FileDownloader
    import sys
    import tempfile

    with tempfile.TemporaryFile(mode='w+t') as f:
        fd = FileDownloader({
            'outtmpl': 'test',
            'quiet': True
        }, {}, f, f)

        mftpp = MetadataFromTitlePP(fd, '%(artist)s - %(title)s')
        assert mftpp.format_to_regex(mftpp._titleformat) == \
            '(?P<artist>.+)\ \-\ (?P<title>.+)'
        assert mftpp.format_to_regex('%(foo)s %(bar)s') == \
            '(?P<foo>.+)\ (?P<bar>.+)'
        assert mftpp.format_to_regex

# Generated at 2022-06-14 17:59:31.549553
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL


# Generated at 2022-06-14 17:59:42.664057
# Unit test for method format_to_regex of class MetadataFromTitlePP
def test_MetadataFromTitlePP_format_to_regex():
    tests = [('%(title)s - %(artist)s', r'(?P<title>.+)\ \-\ (?P<artist>.+)'),
             (r'%(title)s - %(artist)s', r'(?P<title>.+)\ \-\ (?P<artist>.+)'),
             (r'%(title)s - %(artist)s', r'(?P<title>.+)\ \-\ (?P<artist>.+)'),
             ('%(title)s - %(artist)s',  r'(?P<title>.+)\ \-\ (?P<artist>.+)')]

    for fmt, expected in tests:
        actual = MetadataFromTitlePP(object(), fmt).format_to_regex(fmt)
        assert actual == expected

# Generated at 2022-06-14 17:59:52.815921
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Create a test downloader
    downloader = None
    class MockYoutubeDL(object):
        def __init__(self, params):
            self.params = params
            self.to_screen_called_with = []

        def to_screen(self, msg):
            self.to_screen_called_with.append(msg)

    pp = MetadataFromTitlePP(
        downloader,
        '%(title)s - %(artist)s - %(genre)s - %(tracknumber)s - %(date)s')

    # Video info with title of 'Lana Del Rey - Video Games - 3 - 2011'
    info = {
        'title': 'Lana Del Rey - Video Games - 3 - 2011',
    }

# Generated at 2022-06-14 18:00:03.682431
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    metadataFromTitlePP = MetadataFromTitlePP(downloader=None,
                                              titleformat='%(title)s - %(artist)s')

    info_test1 = metadataFromTitlePP.run(info={'title': 'Test title - Test artist'})
    assert info_test1[1]['title'] == 'Test title'
    assert info_test1[1]['artist'] == 'Test artist'

    info_test2 = metadataFromTitlePP.run(info={'title': 'Test title - Test artist - Test album'})
    assert info_test2[1]['title'] == 'Test title - Test artist'
    assert info_test2[1]['artist'] == 'Test album'

    info_test3 = metadataFromTitlePP.run(info={'title': 'Test title'})
    assert info_test3

# Generated at 2022-06-14 18:00:12.758421
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    metadata_from_title = MetadataFromTitlePP(None, '%(song)s - %(band)s')
    metadata = {'title':'the song - the band'}
    assert metadata_from_title.run(metadata)[1] == {'title':'the song - the band',
                                                   'song':'the song',
                                                   'band':'the band'}
    metadata_from_title = MetadataFromTitlePP(None, '%(band)s - %(song)s')
    metadata = {'title':'the song - the band'}
    assert metadata_from_title.run(metadata)[1] == {'title':'the song - the band',
                                                   'song':'the song',
                                                   'band':'the band'}
    metadata_from_title = Metadata

# Generated at 2022-06-14 18:00:25.248808
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import pytest

    metadata = {  # simulate the video already downloaded metadata (e.g. from youtube)
        'title': 'The Amazing',
        'artist': 'Peter Parker',
        'album': 'SuperHero',
        'track': '4',
        'year': '2001',
        'comment': 'with vocals',
        'genre': 'Country',
        'location': '/home/user/music/TheAmazing',
    }

    # test expected behavior

# Generated at 2022-06-14 18:00:29.363478
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FileDownloader
    pp = MetadataFromTitlePP(FileDownloader(None), '%(artist)s - %(track)s')
    info = dict(title="Feist - 1234")
    [], info = pp.run(info)
    assert info['artist'] == 'Feist'
    assert info['track'] == '1234'


# Generated at 2022-06-14 18:00:37.757094
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from mock import Mock
    from sys import version_info
    from ..YoutubeDL import YoutubeDL
    from .common import FileDownloader
    from .postprocessor import FFmpegMergerPP


# Generated at 2022-06-14 18:00:48.001211
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    import core


# Generated at 2022-06-14 18:00:58.424478
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .downloader import Downloader
    from .extractor import InfoExtractor
    from .extractor.common import InfoExtractor
    from .common import InfoDict
    from .common import FileDownloader
    from .cache import Cache
    from .compat import compat_urllib_request, compat_http_server
    from .compat import compat_http_server
    from .utils import format_bytes
    from shutil import rmtree

    # Setup test case
    fd = FileDownloader()
    fd.params.update({'cachedir': False,
                      'noplaylist': True})
    fd.add_default_info_extractors()
    fd.add_info_extractor(InfoExtractor('https://youtu.be/BaW_jenozKc'))
    fd.add_

# Generated at 2022-06-14 18:01:09.206504
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Test if MetadataFromTitlePP can parse title to metadata.
    class TestDownloader():
        def __init__(self):
            self.screen = []
        def to_screen(self, msg):
            if msg not in self.screen:
                self.screen.append(msg)

    test_downloader = TestDownloader()
    test_pp = MetadataFromTitlePP(test_downloader,
                                  '%(title)s - %(creator)s')
    info = {'title': 'example - test'}
    expected_info = {
        'title': 'example',
        'creator': 'test'
    }
    expected_screen = [
        '[fromtitle] parsed title: example',
        '[fromtitle] parsed creator: test'
    ]
    _, info = test_pp.run(info)

# Generated at 2022-06-14 18:01:20.334716
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ..extractor import gen_extractors
    downloader = gen_extractors()['youtube'].ie
    info = {
        'title': 'Hello World!',
    }
    pp = MetadataFromTitlePP(downloader, '%(title)s')
    assert pp.run(info) == ([], info)
    pp = MetadataFromTitlePP(downloader, 'Hello World!')
    assert pp.run(info) == ([], info)
    pp = MetadataFromTitlePP(downloader, 'Hello World!!')
    assert pp.run(info) == ([], info)
    pp = MetadataFromTitlePP(downloader, '%(title)s - %(title)s')
    assert pp.run(info) == ([], {
        'title': 'Hello World!',
    })

# Generated at 2022-06-14 18:01:32.459253
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import ydl
    ydl = ydl

    pp = MetadataFromTitlePP(ydl, titleformat='%(title)s')
    info = {'title': 'Python Test', 'ext': 'mkv'}
    assert pp.run(info)[1]['title'] == 'Python Test'

    pp = MetadataFromTitlePP(ydl, titleformat='%(title)s - %(artist)s')
    info = {'title': 'Python Test - Unit Test', 'ext': 'mkv'}
    assert pp.run(info)[1]['artist'] == 'Unit Test'

    pp = MetadataFromTitlePP(ydl, titleformat='%(title)s - %(artist)s')
    info = {'title': 'Python Test - ', 'ext': 'mkv'}

# Generated at 2022-06-14 18:01:34.932582
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    pass

# Generated at 2022-06-14 18:01:45.411445
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import unittest
    import time
    import sys

    class _FakeInfoDict(dict):
        pass

    class _FakeYDL(object):
        def to_screen(self, msg):
            pass

    class _FakeProgress(object):
        def hook(self):
            pass

    class TestMetadataFromTitlePP(unittest.TestCase):
        def test_00(self):
            titleformat = '%(artist)s - %(title)s'
            title = 'artist_00 - title'
            info = _FakeInfoDict(title=title)
            ppp = MetadataFromTitlePP(_FakeYDL(), titleformat)
            ppp.run(info)
            self.assertEqual(info['artist'], 'artist_00')

# Generated at 2022-06-14 18:01:51.015734
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Create an object
    postprocessor = MetadataFromTitlePP(None,'%(title)s - %(artist)s')
    # Make a test
    test_info = {'title':'This is the title - This is the artist'}
    # Test
    assert postprocessor.run(test_info) == ([],test_info)

# Generated at 2022-06-14 18:02:01.051040
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl import YoutubeDL, FileDownloader

    class FakeYDL:
        def __init__(self, titleformat, url, outtmpl):
            self.titleformat = titleformat
            self.url = url
            self.outtmpl = outtmpl
            self.file_dl = FileDownloader(self)

        def to_screen(self, s):
            pass

    # Test normal retrieve of metadata
    # Test with one single attribute
    titleformat = '%(uploader)s'
    title = 'Youtuber'
    url = 'https://www.youtube.com/watch?v=123456'
    fake_ydl = FakeYDL(titleformat, url, '%(title)s-%(id)s.%(ext)s')

# Generated at 2022-06-14 18:02:13.635790
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Test format_to_regex method first
    pp = MetadataFromTitlePP(None, None)
    assert pp.format_to_regex('%(title)s - %(artist)s') == r'(?P<title>.+)\ \-\ (?P<artist>.+)'
    assert pp.format_to_regex('%(title)s - %(artist)s%(artist)s') == r'(?P<title>.+)\ \-\ (?P<artist>.+)(?P<artist>.+)'

    # Define test strings
    info = { 'title': 'Test video (12.9 MB)' }
    expected_info = { 'title': 'Test video (12.9 MB)', 'format': '12.9 MB' }


# Generated at 2022-06-14 18:02:19.905030
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    import tempfile
    import unittest

    # stubs
    class DL(object):
        def to_screen(self, message):
            pass

    class YDL(object):
        def __init__(self):
            self.postproc = []
            self.params = {
                    'username': None,
                    'password': None,
                    'usenetrc': False,
                    'verbose': False,
                    'quiet': False,
                    'no_warnings': False
                }
            self.cache = None
            self.pu = None
            self.params['outtmpl'] = tempfile.mkstemp()[1]
            self.params['format'] = 'bestvideo'

    # set up
    ydl = YDL()

# Generated at 2022-06-14 18:02:31.801907
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.downloader.common import FileDownloader
    from youtube_dl.utils import FileDownloader
    from tempfile import NamedTemporaryFile

    # Prepare a FileDownloader instance, it is not necessary to set its
    # parameter 'ydl' to an instance of YoutubeDL
    fd = FileDownloader(params={'nopart': True, 'continuedl': False, 'nocheckcertificate': False, 'ratelimit': None, 'retries': 10, 'buffersize': '16384'}, std_in=None, std_out=None, std_err=None)

    # Create a test video with title 'Hello World'
    with NamedTemporaryFile() as f:
        f.write(b'Test Video')
        f.flush()

# Generated at 2022-06-14 18:02:43.238671
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Test substituing %(artist)s in %(title)s - %(artist)s - %(album)s
    titleformat = "%(title)s - %(artist)s - %(album)s"
    title = "This Title - This Artist - This Album"
    title_regex = '(?P<title>.+)\ \-\ (?P<artist>.+)\ \-\ (?P<album>.+)'
    metadata = []
    info = {'title': title}
    postprocessor = MetadataFromTitlePP(None, titleformat)
    assert(postprocessor._titleformat == titleformat)
    assert(postprocessor._titleregex == title_regex)
    expected_output = []
    expected_info = {'title': 'This Title', 'artist': 'This Artist', 'album': 'This Album'}


# Generated at 2022-06-14 18:02:53.399798
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    ydl = YoutubeDL()
    ydl.add_default_info_extractors()
    info = {'id': 'test',
            'title': 'test - test',
            'ext': 'test',
            'url': 'test',
            'format': 'test',
            'player_url': 'test',
            '_type': 'url',
            'ie_key': 'Youtube',
            }
    pp = MetadataFromTitlePP(ydl, '%(artist)s - %(title)s')
    res = pp.run(info)

# Generated at 2022-06-14 18:03:03.726722
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class FakeDl(object):
        def to_screen(self, s):
            pass
    titleformat = '%(artist)s - %(title)s'
    titles = (
        'foo - bar',
        '  foo  -  bar',
        'foo -  bar',
        '  foo   - bar',
        'foo  -  bar',
        '  foo  - bar',
        ' nicks - bar ',
        '  nicks - bar ',
        '  nicks  - bar ',
        '  nicks  -  bar '
    )
    for title in titles:
        info = {'title': title}
        metadata_from_title_pp = MetadataFromTitlePP(FakeDl(), titleformat)
        [], info = metadata_from_title_pp.run(info)

# Generated at 2022-06-14 18:03:16.195509
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import pytest
    mftpp = MetadataFromTitlePP(None, "%(a)s-%(b)s.%(c)s")
    metadata = {}
    info = {'title': 'abc-def.ghi'}
    assert mftpp.run(info) == ([], {'title': 'abc-def.ghi', 'a': 'abc', 'b': 'def', 'c': 'ghi'})

    mftpp = MetadataFromTitlePP(None, "a title")
    info = {'title': 'a title'}
    assert mftpp.run(info) == ([], {'title': 'a title'})

    mftpp = MetadataFromTitlePP(None, "%(a)s")
    info = {'title': 'abc'}

# Generated at 2022-06-14 18:03:26.647335
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class DownloaderMock:
        def __init__(self):
            self.to_screen_output = []
        def to_screen(self, msg):
            self.to_screen_output.append(msg)

    # Test 1: Matches
    pp = MetadataFromTitlePP(DownloaderMock(), '%(title)s - %(artist)s')
    info = {'title': 'My Title - My Artist'}
    _, info = pp.run(info)
    assert info['title'] == 'My Title'
    assert info['artist'] == 'My Artist'

    # Test 2: Does not match
    pp = MetadataFromTitlePP(DownloaderMock(), '%(title)s - %(artist)s')
    info = {'title': 'My Title'}
    _, info = pp.run

# Generated at 2022-06-14 18:03:33.420946
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class null_Downloader(object):
        def to_screen(self, msg):
            return
    downloader = null_Downloader()
    postprocessor = MetadataFromTitlePP(downloader, '%(title)s - %(artist)s')
    info = {'title': 'A title - An artist'}
    postprocessor.run(info)
    assert info == {'title': 'A title - An artist', 'artist': 'An artist'}


# Generated at 2022-06-14 18:03:43.125581
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Build fake downloader
    class FakeDownloader:
        def to_screen(self, msg):
            #print(msg)
            return
    dl = FakeDownloader()

    # Build MetadataFromTitlePP instance
    mftpp = MetadataFromTitlePP(dl, '%(artist)s - %(title)s')
    info = {
        'title': 'Pablo Picasso - El guernica'
    }
    result, info = mftpp.run(info)
    assert result == []
    assert info['title'] == 'Pablo Picasso - El guernica'
    assert info['artist'] == 'Pablo Picasso'

    # Test method format_to_regex
    assert mftpp.format_to_regex('A string') == 'A string'
    assert mftpp.format_

# Generated at 2022-06-14 18:03:51.458742
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.utils import sanitize_open
    class FakeInfoDict(dict):
        def __init__(self, *args, **kwargs):
            super(FakeInfoDict, self).__init__(*args, **kwargs)
            self['title'] = None

    ydl = YoutubeDL({'writethumbnail': True})
    ydl.add_post_processor(MetadataFromTitlePP(ydl, '%(title)s - %(artist)s'))
    with ydl:
        info = FakeInfoDict({
            'url': 'http://www.example.com/video',
            'title': 'The title - with an artist',
        })
        pp_result = ydl.post_process(info, {})
    assert pp_

# Generated at 2022-06-14 18:03:52.186242
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    pass

# Generated at 2022-06-14 18:04:03.372365
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .YoutubeDL import YoutubeDL
    from .PostProcessor import PostProcessor
    from .InfoExtractors import YoutubeIE
    from .compat import compat_urlparse

    class _FakeInfoExtractor(YoutubeIE):
        def _real_extract(self, url):
            return {'id': compat_urlparse.parse_qs(url).get('v', [None])[0]}

    def _fake_info(url):
        return _FakeInfoExtractor()._real_extract(url)

    ydl = YoutubeDL({'quiet': True})
    pp = MetadataFromTitlePP(ydl, '%(title)s - %(track_number)s - %(artist)s')

# Generated at 2022-06-14 18:04:14.127861
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import pytest

    # mock:
    class Downloader:
        def to_screen(self, *args):
            pass
    downloader = Downloader()

    # test:
    pp_match_title = MetadataFromTitlePP(downloader,
                                         '%(title)s - %(artist)s')
    info_match_title = {'title': 'test - song'}
    [], match_title = pp_match_title.run(info_match_title)
    try:
        assert info_match_title['title'] == 'test - song'
        assert info_match_title['artist'] == 'song'
    except AssertionError:
        pytest.fail("Test failed: MetadataFromTitlePP failed to extract metadata from title")


# Generated at 2022-06-14 18:04:23.856805
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    downloader = {'to_screen': lambda *args: None}
    titleformat = '%(title)s - %(artist)s'
    titleregex = r'(?P<title>.+)\ \-\ (?P<artist>.+)'
    pp = MetadataFromTitlePP(downloader, titleformat)
    pp._titleregex = titleregex
    info = {
        'title': 'Song Title - Artist Name',
        'uploader': 'Uploader Name',
        'description': 'Video description'
    }
    expected_result_info = {
        'title': 'Song Title',
        'artist': 'Artist Name',
        'uploader': 'Uploader Name',
        'description': 'Video description'
    }
    assert pp.run(info) == ([], expected_result_info)

    info

# Generated at 2022-06-14 18:04:33.134081
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    sys.modules['pytube.extractor.common'] = sys.modules[__name__]
    sys.modules['pytube.extractor.youtube'] = sys.modules[__name__]
    from pytube.extractor.youtube import YoutubeIE
    from pytube.compat import compat_b64encode


# Generated at 2022-06-14 18:04:47.007318
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    if sys.version_info < (2, 7, 0):
        # Using so named tuple instead of dict, as dict order is not stable
        # in python 2.6
        Info = collections.namedtuple(
            'Info', ['title', 'uploader', 'track', 'album', 'artist', 'genre'])
    else:
        Info = dict


# Generated at 2022-06-14 18:04:56.440574
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # normal case
    title = '%(title)s - %(artist)s'
    metadata_from_titlepp = MetadataFromTitlePP(None, title)
    album_title = 'The Beautiful South - Blue Is The Colour'
    info = {'title': album_title}
    [], info = metadata_from_titlepp.run(info)
    assert info['title'] == 'Blue Is The Colour'
    assert info['artist'] == 'The Beautiful South'
    assert info['ext'] == '.webm'
    # case with % in title
    album_title = 'The Beautiful South - Blue Is The Colour %'
    info = {'title': album_title}
    [], info = metadata_from_titlepp.run(info)
    assert info['title'] == 'Blue Is The Colour %'

# Generated at 2022-06-14 18:05:07.733690
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    title_video = 'test_title - author (test_year)'
    title_format = '%(title)s - %(author)s (%(year)s)'
    title_format_error = '%(title)s - %(author)s'

    downloader = type('Downloader', (object,), {
        'report_warning': lambda self, msg: msg,
        'to_screen': lambda self, msg: msg,
    })
    downloader = downloader()

    # Test with good title format
    pp = MetadataFromTitlePP(downloader, title_format)
    info = {
        'title': title_video,
        'year': None,
        'author': None,
        }
    pp_result, info_result = pp.run(info)
    assert len(pp_result) == 0


# Generated at 2022-06-14 18:05:18.660906
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL

    import collections
    import unittest
    import os

    youtube_dl = YoutubeDL({})

    video = collections.namedtuple('Video', ['title'])

    # Test titleformat to regex
    # Test regular titleformat
    titlestr = '[%(uploader)s]%(title)s'
    regex = youtube_dl.pp_ytdl.format_to_regex(titlestr)
    assert regex == \
        '(?P<uploader>.+)\[(?P<title>.+)'
    # Test titleformat with escaped brackets
    titlestr = '[%(uploader)s]%(title)s\[\]'
    regex = youtube_dl.pp_ytdl.format_to_regex(titlestr)
   

# Generated at 2022-06-14 18:05:29.265899
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL

# Generated at 2022-06-14 18:05:41.472513
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import pytube
    import unittest

    class MetadataFromTitlePPRunTest(unittest.TestCase):
        def setUp(self):
            self.title = 'Lily Allen - Fuck you'
            self.titleformat = '%(artist)s - %(title)s'

        def test_run(self):
            try:
                info = dict()
                info['title'] = self.title
                pytube.postprocessor.MetadataFromTitlePP(
                    pytube.downloader.FileDownloader({}),
                    self.titleformat).run(info)
                self.assertEqual(info['artist'], 'Lily Allen')
                self.assertEqual(info['title'], 'Fuck you')
            except Exception:
                self.fail('should not throw exception')

    unittest.main()


# Generated at 2022-06-14 18:05:49.752416
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import youtube_dl
    ydl = youtube_dl.YoutubeDL({})
    mftPP = MetadataFromTitlePP(ydl, '%(artist)s - %(title)s')
    info = {}
    info['title'] = 'Elton John - Goodbye Yellow Brick Road'
    [formats, info] = mftPP.run(info)
    assert info['artist'] == 'Elton John'
    assert info['title'] == 'Goodbye Yellow Brick Road'
    [formats, info] = mftPP.run(info)
    assert info['artist'] == 'Elton John'
    assert info['title'] == 'Goodbye Yellow Brick Road'

    mftPP = MetadataFromTitlePP(ydl, ' %(artist)s - %(title)s')
    info = {}

# Generated at 2022-06-14 18:05:57.011924
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.postprocessor import PostProcessor
    ydl = YoutubeDL({})
    pp = PostProcessor(ydl, {})
    pp.add_info_extractor({'_type': 'none'})
    pp.add_post_processor(MetadataFromTitlePP(ydl, '%(title)s - %(artist)s'))
    pp.add_post_processor(MetadataFromTitlePP(ydl, '%(foo)s - %(bar)s'))

    info = {'title': 'artist - title',
            '_filename': 'x'}
    pp.run(info)
    assert info['title'] == 'artist - title'
    assert info['artist'] == 'artist'


# Generated at 2022-06-14 18:06:05.296422
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FileDownloader
    from ytdl_server.config import ytdl_opts
    ytdl_opts.__dict__.update({'format': 'best'})
    ydl = FileDownloader({'format': 'best', 'noplaylist': True,
                          'simulate': True, 'quiet': True})
    from .options import extract_format
    # Test run() method with formats containing %(title)s etc.

# Generated at 2022-06-14 18:06:13.365251
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ytdl.YoutubeDL import YoutubeDL

    ydl = YoutubeDL()
    ydl.add_post_processor(MetadataFromTitlePP(ydl, '%(title)s - %(artist)s'))
    info = {'ext': 'mkv', 'upload_date': '20160221', 'id': 'uw7VYgQsmYc',
            'uploader_id': 'SnoopDoggVEVO', 'title': 'Snoop Dogg - Point Seen Money Gone ft. Jeremih'}
    ydl.process_ie_result(info)
    assert info['title'] == 'Snoop Dogg - Point Seen Money Gone ft. Jeremih'
    assert info['artist'] == 'Snoop Dogg'



# Generated at 2022-06-14 18:06:28.435816
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class fake_downloader:
        def to_screen(self, text):
            pass
    video_data = {'title': 'Orchestra Martin & Andrea Bocelli - Con Te Partirò (Original)'}
    pp = MetadataFromTitlePP(fake_downloader(), '%(artist)s - %(title)s')
    pp.run(video_data)
    assert video_data['artist']=='Orchestra Martin & Andrea Bocelli'
    assert video_data['title']=='Con Te Partirò (Original)'
    video_data = {'title': 'Vasco Rossi - Sally (Original)'}
    pp = MetadataFromTitlePP(fake_downloader(), '%(artist)s - %(song)s')
    pp.run(video_data)
    assert video_data['artist']

# Generated at 2022-06-14 18:06:33.314171
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    postprocessor = MetadataFromTitlePP(None, '%(title)s - %(artist)s')
    assert (postprocessor.run({'title': 'hello world'}) ==
            ([], {'title': 'hello world'}))
    assert (postprocessor.run({'title': 'hello world - it\'s me'}) ==
            ([], {'title': 'hello world - it\'s me',
                  'artist': 'it\'s me'}))



# Generated at 2022-06-14 18:06:43.929538
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ytdl.YoutubeDL import YoutubeDL
    ydl = YoutubeDL()
    ydl.add_post_processor(
        MetadataFromTitlePP(ydl, '%(artist)s - %(title)s'))
    ydl.prepare_filename('http://example.org/video.mp4', {})
    assert ydl.info_dict['artist'] == 'NA'
    assert ydl.info_dict['title'] == 'NA'

    ydl.add_post_processor(
        MetadataFromTitlePP(ydl, '%(title)s - %(artist)s'))
    ydl.prepare_filename('http://example.org/video.mp4', {})
    assert ydl.info_dict['artist'] == 'NA'

# Generated at 2022-06-14 18:06:52.428635
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.postprocessor import unescapeHTML
    from .common import FakeYDL

    pp = MetadataFromTitlePP(FakeYDL(), '%(title)s - %(artist)s')
    info = {'title': unescapeHTML('My &amp;&amp;lt;title&gt;'),
            'ext': 'mp4'}
    assert pp.run([], info) == ([], {
        'title': 'My &&lt;title>',
        'artist': 'NA',
        'ext': 'mp4'})

# Generated at 2022-06-14 18:07:03.493919
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    title = 'Metadata from title Test'
    fromtitle = MetadataFromTitlePP(PostProcessor(None), title)
    info_out = {'title': title}
    assert fromtitle.run(info_out) == ([], info_out)

    title = 'Metadata from title Test - Youtuber'
    fromtitle = MetadataFromTitlePP(PostProcessor(None),
                                    '%(title)s - %(artist)s')
    info_out = {'title': title}
    assert fromtitle.run(info_out) == ([], {'title': 'Metadata from title Test',
                                            'artist': 'Youtuber'})

    title = 'Metadata from title Test'

# Generated at 2022-06-14 18:07:15.626412
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    def test(title, fmt, testcases):
        pp = MetadataFromTitlePP(None, fmt)
        info = {'title': title}
        # TODO: would be nice to have this method available as a test method
        pp.run(info)

        # Remove keys that start with '_'
        info = dict((k, v) for (k, v) in info.items() if not k.startswith('_'))

        for testcase in testcases:
            assert testcase in info.items()

    test('Video Title', '', [('title', 'Video Title')])
    test('Video Title', '%(title)s', [('title', 'Video Title')])
    test('Video Title', '%(title)s', [('title', 'Video Title')])

# Generated at 2022-06-14 18:07:26.066018
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class Downloader:
        def to_screen(self, message):
            print(message)

    titleformat = '%(artist)s - %(title)s (feat. %(featured_artists)s) -- %(year)s'
    regex = MetadataFromTitlePP(Downloader(), titleformat).format_to_regex(titleformat)
    print('regex:', regex)
    title = 'Imagine Dragons - Thunder (feat. K.Flay) -- 2017'
    match = re.match(regex, title)
    if match is not None:
        for attribute, value in match.groupdict().items():
            print(attribute + ':', value)

# Generated at 2022-06-14 18:07:34.030238
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl import YoutubeDL
    from youtube_dl.compat import compat_str

    # Test case 1: title without metadata
    info1 = {
        'title': 'A title without metadata',
        }
    ydl = YoutubeDL()
    ydl.add_post_processor(MetadataFromTitlePP(ydl, '%(title)s - %(artist)s'))
    pp_result1 = ydl.process_ie_result(info1, download=False)
    assert pp_result1[1]['title'] == compat_str('A title without metadata')
    assert pp_result1[1]['artist'] == compat_str(None)
    assert isinstance(pp_result1[0], list)
    assert len(pp_result1[0]) == 0

    # Test case 2: title with metadata


# Generated at 2022-06-14 18:07:42.608130
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import unittest
    import ydl_test

    class FakeDownloader():
        def __init__(self):
            self.to_screen_out = []
        def to_screen(self, message):
            self.to_screen_out.append(message)

    class TestMetadataFromTitlePP(
            unittest.TestCase,
            ydl_test.TestYDLUtilsAsserts,
            ydl_test.TestYDLUtilsSetupBeforeEachTest):

        def setUp(self):
            self.processor = MetadataFromTitlePP(FakeDownloader(), '%(title)s - %(artist)s - %(album)s - %(genre)s')

# Generated at 2022-06-14 18:07:53.912669
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import youtube_dl
    import inspect

    info = {'title': 'Prunoideae - Wikipedia, the free encyclopedia[HD]'}
    posts = MetadataFromTitlePP(youtube_dl, "%(title)s").run(info)[0]

    assert len(posts) == 0
    assert info == {'title': 'Prunoideae - Wikipedia, the free encyclopedia[HD]'}

    info = {'title': 'Prunoideae - Wikipedia, the free encyclopedia[HD]'}
    posts = MetadataFromTitlePP(youtube_dl, "%(artist)s - %(title)s").run(info)[0]

    assert len(posts) == 0
    assert info == {'title': 'Prunoideae - Wikipedia, the free encyclopedia[HD]', 'artist': 'Prunoideae'}


# Generated at 2022-06-14 18:08:09.271474
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    import os
    import shutil
    import tempfile
    import collections
    import unittest
    import youtube_dl
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.downloader.PostProcessor import PostProcessor


    class FFmpegDownloaderStub(object):
        def __init__(self):
            self.downloaded_infos = collections.defaultdict(list)

        def to_screen(self, str):
            print(str)

        def to_console_title(self, str):
            pass

        def to_stdout(self, str):
            pass

        def to_stderr(self, str):
            pass

        def trouble(self, str):
            pass

        def report_warning(self, str):
            pass


# Generated at 2022-06-14 18:08:20.706514
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FakeYDL
    from .compat import compat_str
    ydl = FakeYDL()
    # Test with a single match
    pp = MetadataFromTitlePP(ydl, '%(title)s')
    info = dict(title='test')
    pp.run(info)
    # Test with multiple matches
    pp = MetadataFromTitlePP(ydl, '%(title)s - %(uploader)s')
    info = dict(title='test - testuser')
    pp.run(info)
    # Test with a single match group spanning over multiple words
    pp = MetadataFromTitlePP(ydl, '%(title)s')
    info = dict(title='test test')
    pp.run(info)
    # Test with multiple match groups spanning over multiple words
    pp = MetadataFrom

# Generated at 2022-06-14 18:08:28.911267
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ..compat import compat_urllib_request

    class DummyInfoDict(object):
        def __init__(self, title=None):
            self['title'] = title

    def _getinfo(url):
        class InfoProperties(object):
            def __init__(self):
                self.filename = b'filename.mp4'
                self.url =  b'http://example.com/video.mp4'

        class Info(object):
            def __init__(self):
                self.status = 200
                self.info = InfoProperties()

        return Info()

    # Titleformat with regex group
    titleformat = r'%(title)s - %(artist)s'
