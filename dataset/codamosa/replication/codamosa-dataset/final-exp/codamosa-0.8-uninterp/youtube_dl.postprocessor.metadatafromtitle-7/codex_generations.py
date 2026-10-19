

# Generated at 2022-06-14 17:58:41.462757
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ytdl.YoutubeDL import YoutubeDL
    downloader = YoutubeDL({}) # Empty option dict
    mftpp = MetadataFromTitlePP(downloader, '%(artist)s - %(title)s')
    info = {
        'title': 'Artist - Title',
    }
    mftpp.run(info)
    assert info['artist'] == 'Artist'
    assert info['title'] == 'Title'

    info = {
        'title': 'Artist - Album (year) - Title',
    }
    mftpp = MetadataFromTitlePP(downloader, '%(artist)s - %(title)s')
    mftpp.run(info)
    assert info['artist'] == 'Artist - Album (year)'
    assert info['title'] == 'Title'


# Generated at 2022-06-14 17:58:51.754252
# Unit test for method run of class MetadataFromTitlePP

# Generated at 2022-06-14 17:58:59.739420
# Unit test for constructor of class MetadataFromTitlePP
def test_MetadataFromTitlePP():
    def check(titleformat, title, attributes):
        """Test constructor with given parameters.

        titleformat - format string parameter
        title - test title string
        attributes - expected dictionary of attributes

        """
        pp = MetadataFromTitlePP(None, titleformat)
        assert pp._titleformat == titleformat
        match = re.match(pp._titleregex, title)
        assert match is not None, (
            "Title '%s' does not match regex '%s'"
            % (title, pp._titleregex))
        assert match.groupdict() == attributes, (
            "Title '%s' expected to have attributes %s; got %s"
            % (title, attributes, match.groupdict()))

    # test attribute title

# Generated at 2022-06-14 17:59:09.541547
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    torrent_file = {'format': 'HD', 'height': '1080', 'width': '1920',
                    'fps': '24', 'vcodec': 'h264', 'acodec': 'aac',
                    'abr': '192', 'tbr': '1150', 'ext': 'mp4',
                    'title': 'Test Video (720p) - Artist 1',
                    'upload_date': '20170101'}
    downloader = YoutubeDL({'writesubtitles': True})
    metadata_pp = MetadataFromTitlePP(downloader, '%(title)s - %(artist)s')
    # Case 1: Downloading torrent metadata
    metadata_pp.run(torrent_file)
    assert torrent_file['artist'] == 'Artist 1'


# Generated at 2022-06-14 17:59:19.167333
# Unit test for method format_to_regex of class MetadataFromTitlePP
def test_MetadataFromTitlePP_format_to_regex():
    mf = MetadataFromTitlePP(None, None)
    assert b'(?P<a>.+)' == mf.format_to_regex(b'%(a)s')
    assert b'(?P<a>.+)\\ \-\ (?P<b>.+).*' == mf.format_to_regex(b'%(a)s - %(b)s.*')
    assert b'.*' == mf.format_to_regex(b'.*')
    assert b'huge\ regex' == mf.format_to_regex(b'huge regex')

# Generated at 2022-06-14 17:59:30.608322
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.extractor.common import InfoExtractor
    from youtube_dl.utils import DateRange

    ie = InfoExtractor({})
    ie.add_default_info_extractors()
    ie.set_downloader(YoutubeDL({'usenetrc': False}))
    ie.set_info_extractor(lambda x: x)

    title = 'Youtube Video - Artist  -  Song (Lyrics)'
    info = {'id': '12345',
            'title': title
            }
    titleformat = '%(title)s - %(artist)s - %(song)s (%(lyrics)s)'
    format_to_regex = MetadataFromTitlePP.format_to_regex(None, titleformat)

# Generated at 2022-06-14 17:59:34.621500
# Unit test for method format_to_regex of class MetadataFromTitlePP
def test_MetadataFromTitlePP_format_to_regex():
    titleformat='%(title)s - %(artist)s'
    expected=r'(?P<title>.+)\ \-\ (?P<artist>.+)'
    actual=MetadataFromTitlePP.format_to_regex(titleformat)
    return (actual == expected)

# Generated at 2022-06-14 17:59:41.395550
# Unit test for constructor of class MetadataFromTitlePP
def test_MetadataFromTitlePP():
    from .common import FakeYDL
    downloader = FakeYDL()
    pp = MetadataFromTitlePP(downloader, '%(title)s - %(artist)s')
    info = { 'title': 'Gangnam Style - PSY' }
    _, info = pp.run(info)
    assert info['title'] == 'Gangnam Style'
    assert info['artist'] == 'PSY'



# Generated at 2022-06-14 17:59:49.956631
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    ff = MetadataFromTitlePP(None, '%(title)s_%(artist)s')
    ff._titleregex = '(?P<title>.*)_(?P<artist>.*)'
    # Test that a title can be parsed
    info = {'title': 'mytitle_myartist'}
    res = ff.run(info)
    assert info['title'] == 'mytitle'
    assert info['artist'] == 'myartist'
    # Test that a title can be parsed when it contains regex-special characters
    info = {'title': 'mytitle_.*.myartist'}
    res = ff.run(info)
    assert info['title'] == 'mytitle_.*'
    assert info['artist'] == 'myartist'
    # Test that a title cannot be parsed

# Generated at 2022-06-14 18:00:02.052151
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ..youtube_dl.YoutubeDL import YoutubeDL

    info = {
        'id': 'FwUZep5N5xI'
    }
    titleformat = '%(title)s'
    regex = '%(title)s'
    match_dict = {
        'title': 'Bill Gates Talks At MIT: Innovation & Poverty'
    }

    def to_screen(s):
        print(s)
    downloader = YoutubeDL()
    downloader.to_screen = to_screen
    pp = MetadataFromTitlePP(downloader, titleformat)
    info_out = dict()
    for key in info:
        info_out[key] = info[key]
    info_out['title'] = 'Bill Gates Talks At MIT: Innovation & Poverty'


# Generated at 2022-06-14 18:00:12.941979
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.extractor import youtube
    from youtube_dl.utils import sanitize_title
    from youtube_dl.downloader import YoutubeDL
    from youtube_dl.postprocessor.metadatafromtitle import MetadataFromTitlePP

    ydl = YoutubeDL()
    ydl.add_default_info_extractors()

    def test_title_regex(title, regex, expected):
        video = {
            'id': title,
            'title': title,
        }
        pp = MetadataFromTitlePP(ydl, regex)
        _, info = pp.run(video)
        for key, value in expected.items():
            assert info[key] == value,\
                    '%s: got %s instead of %s' % (key, info[key], value)


# Generated at 2022-06-14 18:00:25.577300
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():

    # the test case
    class Test:
        def to_screen(self, msg):
            print(msg)

    # test run
    pp = MetadataFromTitlePP(Test(), '%(title)s by %(artist)s - %(album)s')
    info = {'title': 'title by artist - album'}
    _, info = pp.run(info)
    assert info.get('title', None) == 'title'
    assert info.get('artist', None) == 'artist'
    assert info.get('album', None) == 'album'

    # test run with no match
    pp = MetadataFromTitlePP(Test(), '%(title)s by %(artist)s - %(album)s')
    info = {'title': 'title - album'}

# Generated at 2022-06-14 18:00:29.324789
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Create an empty object of class MetadataFromTitlePP
    metadata_from_title_pp = MetadataFromTitlePP('dummy_downloader', 'dummy_titleformat')

    # Test if it runs successfully (returns empty array in this case)
    assert metadata_from_title_pp.run('dummy_info') == ([], 'dummy_info')

# Generated at 2022-06-14 18:00:35.953734
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Test string
    title = 'Justin Bieber - Baby ft. Ludacris'
    # Create a PostProcessor and run method
    pp = MetadataFromTitlePP(None, '%(artist)s - %(title)s')
    assert pp.run({'title': title}) == ([], {'artist': 'Justin Bieber',
                                             'title': 'Baby ft. Ludacris'})
    # Test regex
    pp = MetadataFromTitlePP(None, '^Justin Bieber - (?P<title>.*)$')
    assert pp.run({'title': title}) == ([], {'title': 'Baby ft. Ludacris'})

# Generated at 2022-06-14 18:00:46.234617
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # import sys
    from youtube_dl.downloader import Downloader
    from youtube_dl.postprocessor.ffmpeg import FFmpegExtractAudioPP
    from utils import fake_info_dict, fake_file


# Generated at 2022-06-14 18:00:51.442952
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import unittest
    import sys

    class _Downloader():
        def __init__(self):
            self.to_screen_calls = []

        def to_screen(self, msg):
            self.to_screen_calls.append(msg)


# Generated at 2022-06-14 18:00:52.991483
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # TODO
    pass

# Generated at 2022-06-14 18:01:06.142871
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    import os
    if sys.version_info < (3, 0):
        from StringIO import StringIO
    else:
        from io import StringIO
    if sys.version_info >= (3, 6):
        from unittest.mock import MagicMock
    else:
        # done this way to work with python < 3.6
        from mock import MagicMock
    import pytest
    from ytdl.PostProcessors import MetadataFromTitlePP


# Generated at 2022-06-14 18:01:15.025635
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import unittest
    import sys

    class TestPP(unittest.TestCase):
        def test(self):
            enabled = sys.stdout.isatty()
            title = 'I want to match %(artist)s and %(title)s but not this %(album)s'
            fmt = '%(artist)s - %(title)s'

            class FakeInfo(object):
                def __init__(self):
                    self.title = 'this is my title'
                    self.artist = 'this is my artist'

            class FakeDownloader(object):
                def __init__(self):
                    self.to_screen = lambda *_: None

                def to_screen(self, msg):
                    if enabled:
                        super(FakeDownloader, self).to_screen(msg)
                    else:
                        self

# Generated at 2022-06-14 18:01:24.760467
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Test object creation
    downloader = TestYoutubeDL()
    metadataFromTitlePP = MetadataFromTitlePP(downloader, ('%(title)s - '
                                                            '%(artist)s'))

    # Test without match
    retval, info = metadataFromTitlePP.run({'title': 'title 1'})
    assert [] == retval
    assert {'title': 'title 1'} == info

    # Test with match
    retval, info = metadataFromTitlePP.run({'title': 'title 2 - artist 2'})
    assert [] == retval
    assert {'title': 'title 2', 'artist': 'artist 2'} == info



# Generated at 2022-06-14 18:01:34.774511
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # TODO: use test instances instead of mocking
    class Info(dict):
        # disable upper case to enable use of static dictionary below
        def __init__(self, the_dict=None):
            self._ = lambda x: x
        def __setitem__(self, key, value):
            super(Info, self).__setitem__(key, value)
    class Downloader(object):
        def to_screen(self, msg):
            pass
    info = Info({'title': 'My Title'})
    downloader = Downloader()

    pp = MetadataFromTitlePP(downloader, '%(title)s')
    pp.run(info)
    assert 'title' in info and info['title'] == 'My Title'

    info = Info({'title': 'My Title'})
    pp = MetadataFromTitlePP

# Generated at 2022-06-14 18:01:45.272150
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FileDownloader
    class FakeInfoDict(dict):
        pass
    class FakeExtractor(object):
        def __init__(self, downloader, *args):
            pass

        @classmethod
        def suitable(cls, *args):
            return True

    downloader = FileDownloader({})
    downloader.add_info_extractor(FakeExtractor)
    titleformat = '%(title)s - %(artist)s'
    metadatapp = MetadataFromTitlePP(downloader, titleformat)
    # Test cases

# Generated at 2022-06-14 18:01:56.812422
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FileDownloader
    from .extractor.common import InfoExtractor
    from .compat import compat_urllib_parse_urlencode

    class DummyIE(InfoExtractor):
        def _real_extract(self, url):
            return {
                'id': 'abc123',
                'title': '"%(artist)s - %(song)s"' % {
                    'song': '"Song"',
                    'artist': 'Artist',
                }
            }

    ie = DummyIE(FileDownloader())
    ie.add_info_extractor(DummyIE())
    postprocessor = MetadataFromTitlePP(ie._downloader, '%(artist)s - %(song)s')

    # Test that run returns the info

# Generated at 2022-06-14 18:02:03.788783
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import pytest
    from ytdl.extractor.common import InfoExtractor
    from ytdl.downloader import YoutubeDL
    from ytdl.compat import compat_str


# Generated at 2022-06-14 18:02:15.142448
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():

    class FakeInfo:
        pass

    class FakeYDL:
        def to_screen(self, msg):
            print(msg)

    title = 'Deutsche Bahn: BahnCard 50 Commercial'
    titleformat = '%(title)s'
    fakeinfo = FakeInfo()
    fakeinfo['title'] = title
    fakeydl = FakeYDL()
    mfTPP = MetadataFromTitlePP(fakeydl, titleformat)
    mfTPP.run(fakeinfo)

    assert fakeinfo['title'] == title, 'FakeInfo has wrong title attribute.'

    titleformat = '%(artist)s - %(title)s'
    mfTPP.__init__(fakeydl, titleformat)
    mfTPP.run(fakeinfo)

# Generated at 2022-06-14 18:02:27.242992
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    downloader = YoutubeDL()
    pp = MetadataFromTitlePP(downloader, '%(title)s - %(artist)s')
    info = {'title': 'Title - Artist'}
    result = pp.run(info)
    assert result == ([], info)
    assert info == {'title': 'Title - Artist', 'artist': 'Artist'}

    info = {'title': 'Title'}
    result = pp.run(info)
    assert result == ([], info)
    assert info == {'title': 'Title'}

    pp = MetadataFromTitlePP(downloader, '%(title)s - %(artist)s')
    info = {'title': 'Title - Artist', 'artist': 'My artist'}

# Generated at 2022-06-14 18:02:33.881217
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    import unittest
    class Mock(object):
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)
    class MockDownloader(Mock):
        def to_screen(self, text):
            sys.stdout.write(text + '\n')
    class MockYDL(Mock):
        def __init__(self, **kwargs):
            super(MockYDL, self).__init__(**kwargs)
            self.postprocessors = [MetadataFromTitlePP(self, '%(title)s - %(artist)s - %(track)s')]
    class TestMFT(unittest.TestCase):
        def test_na(self):
            ydl = MockYDL(params={'no_color': True})


# Generated at 2022-06-14 18:02:42.992753
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import InfoExtractor
    from .extractor import YoutubeIE
    from .utils import compat_urllib_request

    # Initialize test class
    downloader = YoutubeIE()
    downloader.http_test = True
    downloader.test_result_username = 'test_username'
    downloader.test_result_single_title = 'test_title'
    MetadataFromTitlePP = MetadataFromTitlePP(downloader, '%(title)s - %(uploader)s')

    # Test 1
    single_title = 'test_title - test_username'
    info = {
        'id': 'test_id1',
        'url': 'http://www.youtube.com/watch?v=test_id1',
        'title': single_title
    }

# Generated at 2022-06-14 18:02:52.276638
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import youtube_dl

    video_url = 'http://video.example.com/xxx'
    formats = []
    video_info = {'id': 'xxx', 'title': 'title'}
    titleformat = '%(title)s - %(artist)s'
    expected = {'id': 'xxx', 'title': 'title', 'artist': 'NA'}

    ydl = youtube_dl.YoutubeDL()
    pp = MetadataFromTitlePP(ydl, titleformat)
    info = pp.run(video_info)[1]
    assert info == expected


# Generated at 2022-06-14 18:03:02.801052
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL

    # Create a dummy downloader
    class FakeDownloader(object):
        def __init__(self):
            self.to_screen_message = ''

        def to_screen(self, msg):
            self.to_screen_message += msg

    downloader = FakeDownloader()

    # Create a dummy info dictionary
    info = {
        'title': 'title: %(title)s - %(artist)s',
    }

    # Create a MetadataFromTitlePP and execute run
    pp = MetadataFromTitlePP(downloader, '%(title)s - %(artist)s')
    pp.run(info)

    # Check the expected results
    assert info['title'] == 'title: %(title)s - %(artist)s'

# Generated at 2022-06-14 18:03:17.044674
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    try:
        from urllib.parse import urlparse, parse_qs
    except ImportError:
        from urlparse import urlparse, parse_qs
    import youtube_dl
    import youtube_dl.postprocessor
    import json

    old_urlparse = youtube_dl.downloader.urlparse

    testdata_dir = os.path.dirname(__file__)
    with open(os.path.join(testdata_dir, 'test.json')) as f:
        TEST_DATA = json.load(f)

    def new_urlparse(url):
        return old_urlparse(url.encode('utf-8'))

    class MockYDL(object):
        def __init__(self):
            self._screen_file = io.StringIO()

        @property
        def params(self):
            return

# Generated at 2022-06-14 18:03:27.306648
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ytdl_now.YoutubeDL import YoutubeDL
    import json

    # initialize fake downloader
    downloader = YoutubeDL()
    # initialize postprocessor
    postprocessor = MetadataFromTitlePP(downloader, '%(title)s - %(artist)s')
    # expected output
    info_exp = {'title': 'test title'}
    # test case 1
    info_act = {
            'title': 'test title - test artist',
            '_filename': 'test filename.mp3',
            '_type': 'audio',
            'ext': 'mp3'
    }
    # run postprocessor
    [], info = postprocessor.run(info_act)
    # check expected output
    assert(info == info_exp)

    # test case 2

# Generated at 2022-06-14 18:03:37.974674
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class DummyInfo(dict):
        def get(self, key):
            return self[key]

    from .common import FileDownloader
    from .YoutubeDL import YoutubeDL
    titleformat = r'^(?P<artist>[^-]+)\s*-\s*(?P<title>[^-]+)'
    infos = [{'title':'Abcdef - Ghijkl'},
             {'title':'Abcdef -G hijkl'},
             {'title':'Abcdef Ghijkl'},
             {'title':'abcdef ghijkl'}]
    infos = [DummyInfo(i) for i in infos]

    pp = MetadataFromTitlePP(FileDownloader(YoutubeDL()), titleformat)

# Generated at 2022-06-14 18:03:42.668323
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    import os
    import tempfile
    import io

    # override sys.stdout and sys.stderr to capture output
    oldstdout = sys.stdout
    oldstderr = sys.stderr
    sys.stdout = io.BytesIO()
    sys.s

# Generated at 2022-06-14 18:03:51.135033
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import os.path
    import sys
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
    import unittest
    import youtube_dl
    # since downloader is already created in __init__, it
    # cannot be mocked, so we have to instantiate a new one
    downloader = youtube_dl.YoutubeDL({})
    # fake video info
    video_info = {'title': 'My video title'}
    # create and run pp
    pp = MetadataFromTitlePP(downloader, '%(title)s')
    assert pp.run(video_info)[1] == {'title': 'My video title'}
    # check that unittest is working
    assert 2+2 == 4


# Generated at 2022-06-14 18:04:02.538520
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import unittest

    def pass_info(info):
        return [], info

    class FakeYoutubeDL(object):
        def __init__(self):
            self.to_screen_messages = []

        def to_screen(self, message):
            self.to_screen_messages.append(message)

    class TestCase(unittest.TestCase):
        def setUp(self):
            self.downloader = FakeYoutubeDL()

    class Test_with_titledict_format(TestCase):
        def setUp(self):
            super(Test_with_titledict_format, self).setUp()
            self.postprocessor = MetadataFromTitlePP(
                self.downloader, '%(title)s - %(artist)s')

# Generated at 2022-06-14 18:04:13.469224
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ydl.YoutubeDL import YoutubeDL
    from ydl.postprocessor.common import FFmpegMetadataPP

    def test(titleformat, title, expected):
        pp_class = MetadataFromTitlePP.__name__
        ffmpeg_class = FFmpegMetadataPP.__name__
        print('Testing %s with title "%s" and titleformat "%s"'
              % (pp_class, title, titleformat))
        ydl = YoutubeDL({'postprocessors': [
            {'key': 'FFmpegMetadata'},
            {'key': 'MetadataFromTitle', 'titleformat': titleformat}]})
        ydl.add_default_info_extractors()
        ie = ydl.build_video_info_extractor({'title': title, 'id': 'dummy'})
        ie.extract

# Generated at 2022-06-14 18:04:21.171597
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class FakeInfoDict:
        title = 'The Dog & the Squirrel - Acme Inc.'
        pass


# Generated at 2022-06-14 18:04:31.668677
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Test1: The title is in the format '%(artist)s - %(title)s'
    info = {'id': 'h2mDzRmjKpc',
            'title': 'Jon Bellion - Human (Official Music Video)'}
    metadatafromtitle = MetadataFromTitlePP(None, '%(artist)s - %(title)s')
    infos_expected = [{'id': 'h2mDzRmjKpc',
                       'title': 'Jon Bellion - Human (Official Music Video)',
                       'artist': 'Jon Bellion',
                       'title': 'Human (Official Music Video)'}]
    infos_actual = metadatafromtitle.run(info)
    assert infos_expected == infos_actual, \
        "testMetadataFromTitlePP_run: Test1"
   

# Generated at 2022-06-14 18:04:44.270332
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ytdl.YoutubeDL import YoutubeDL
    ydl = YoutubeDL()
    ydl.params['writethumbnail'] = False
    ydl.params['writesubtitles'] = False
    ydl.params['writeautomaticsub'] = False
    ydl.params['skip_download'] = True
    ydl.params['format'] = 'bestaudio/best'
    ydl.params['logger'] = YoutubeDL.TO_SCREEN_NO_PRINT

# Generated at 2022-06-14 18:05:03.314821
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from . import YoutubeDL
    from .extractor.youtube import YoutubeIE

    title_only_format = '%(title)s'
    test_only_format = '%(title)s - TEST'
    test_format = '%(title)s - %(artist)s - TEST'

    url = 'https://www.youtube.com/watch?v=BaW_jenozKc'
    expected_title = 'Hatsune Miku - tell your world  -Project DIVA- F 2nd'
    expected_artist = 'kz(livetune)'

    yd = YoutubeDL()
    yd.add_info_extractor(YoutubeIE())

    yd.add_post_processor(MetadataFromTitlePP(yd, title_only_format))
    info = yd.extract_info(url)

# Generated at 2022-06-14 18:05:07.189318
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    import yaml
    from .common import FileDownloader

    class FakeYDL:
        def __init__(self):
            self.params = {
                'noplaylist': True,
                'cachedir': False,
            }
            self.cache = {}

        def to_screen(self, msg):
            sys.stderr.write(msg + '\n')


# Generated at 2022-06-14 18:05:18.455841
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    from ydl.downloader.common import FakeYDL
    from ydl.extractor import get_info_extractor

    class FakeInfoExtractor(object):
        def __init__(self, ie_info):
            self._info = ie_info

        @classmethod
        def suitable(cls, url):
            return True

        @classmethod
        def _real_extract(cls, url):
            return cls._info

    class FakeInfo(dict):
        pass
    info = FakeInfo({'id': 'someid', 'title': 'something'})
    ydl = FakeYDL()

    # test MetadataFromTitlePP with a regex
    pp = MetadataFromTitlePP(ydl, '%(title)s %(id)s')

# Generated at 2022-06-14 18:05:28.608775
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FakeYDL

    ydl = FakeYDL()
    mftpp = MetadataFromTitlePP(ydl, '%(id)s Test %(title)s')
    info = {'title': '111222333 Test Test Test', 'id': '111222333'}

    # Without pattern (%(title)s)
    mftpp._titleformat = '%(id)s'
    mftpp._titleregex = '%(id)s'
    mftpp.run(info)
    assert ydl.msgs == [
        "[fromtitle] Could not interpret title of video as '%(id)s'"]

    # Without pattern (%(title)s)
    mftpp._titleformat = '%(id)s'

# Generated at 2022-06-14 18:05:39.895203
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .downloader import downloader
    from .extractor import YoutubeIE

    class DummyIE(YoutubeIE):
        def _real_initialize(self):
            return

        def _real_extract(self, url):
            return {
                'id': '12345',
                'title': 'Coldplay - Hymn For The Weekend (Official Video)',
                'ext': 'webm',
                'duration': 254
            }
        @property
        def IE_NAME(self):
            return 'DummyIE'

        @classmethod
        def suitable(cls, url):
            return False

    def _assert_title(title, expected_metadata, titleformat='%(title)s'):
        d = downloader.HeadlessFD()
        pp = MetadataFromTitlePP(d, titleformat)
        pp

# Generated at 2022-06-14 18:05:47.955034
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # init downloader
    downloader = object()
    downloader.to_screen = object()
    # init MetadataFromTitlePP
    test_format = r'%(title)s - %(artist)s'
    metadatafromtitle = MetadataFromTitlePP(downloader, test_format)
    # init test data
    info = dict()
    info['title'] = r'Test title - Test artist'
    expected_return = (True, dict())
    # call method run
    returned_value = metadatafromtitle.run(info)
    # check returned value
    assert(returned_value == expected_return)


# Generated at 2022-06-14 18:05:56.790933
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():

    m = MetadataFromTitlePP(None, '%(title)s. (%(artist)s)')

    info1 = {'title': 'Das Hier. (Shazam)'}
    info2 = {'title': 'Das Hier. (Shazam)', 'artist': 'Bert, Ernie und Shazam'}
    info3 = {'title': 'Das Hier. (Shazam)', 'artist': 'Bert, Ernie und Shazam', 'genre': 'Rock'}

    r1, i1 = m.run(info1)
    r2, i2 = m.run(info2)
    r3, i3 = m.run(info3)

    assert i1 == {'artist': 'Shazam', 'title': 'Das Hier. (Shazam)'}
    assert i

# Generated at 2022-06-14 18:06:04.749837
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    """
    Test method run with a format of "%(title)s - %(artist)s"

    The test is performed with a string that must be matched and not matched
    """
    pp = MetadataFromTitlePP(None, '%(title)s - %(artist)s')
    info = {'title': 'Video title'}
    result = pp.run(info)
    assert result == ([], info)
    assert info['title'] == 'Video title'
    assert info['artist'] == 'Video title'
    info = {'title': 'Video'}
    result = pp.run(info)
    assert result == ([], info)
    assert info['title'] == 'Video'
    assert info['artist'] is None


# Generated at 2022-06-14 18:06:13.279376
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.utils import DateRange
    downloader = object
    class MockDownloader:
        @staticmethod
        def to_screen(msg):
            pass
    downloader.to_screen = MockDownloader.to_screen
    # Subclasses PostProcessor, so we have to set some attributes
    downloader.params = {}
    downloader.params['writesubtitles'] = True
    downloader.params['outtmpl'] = '%(title)s.%(ext)s'
    downloader.params['outtmpl'] = '%(id)s%(format_id)s'
    downloader.params['writethumbnail'] = True
    downloader.params['writeinfojson'] = True
    downloader.params['writedescription'] = True
    downloader.params['writeannotations'] = True


# Generated at 2022-06-14 18:06:24.306666
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():

    class DummyDownloader(object):
        def to_screen(self, msg):
            print(msg)

    downloader = DummyDownloader()

    # Tests for format_to_regex()
    print('format_to_regex() tests:')
    metadatafromtitlepp = MetadataFromTitlePP(downloader, '%(title)s - %(artist)s')
    print(metadatafromtitlepp.format_to_regex('%(title)s - %(artist)s') ==
          r'(?P<title>.+)\ \-\ (?P<artist>.+)')
    print(metadatafromtitlepp.format_to_regex('test - %(artist)s') ==
          r'test\ \-\ (?P<artist>.+)')

# Generated at 2022-06-14 18:06:51.161179
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # create a downloader
    downloader = object()
    # create a titleformat like '%(title)s - %(artist)s'
    titleformat = '%(title)s - %(artist)s'
    # create a title like 'abc - def'
    title = titleformat % {'title': 'abc', 'artist': 'def'}
    # create an info
    info = {'title': title}
    # create a MetadataFromTitlePP object
    pp = MetadataFromTitlePP(
        downloader, titleformat)
    # run method run of MetadataFromTitlePP
    downloaded_tuple, info = pp.run(info)
    # check if downloaded_tuple is []
    assert downloaded_tuple == []
    # check if info is like '{'title': 'abc - def', 'artist': '

# Generated at 2022-06-14 18:07:03.433230
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    import unittest

    class MockDownloader(object):
        def __init__(self, result):
            self.result = result
            self.screen_messages = []

        def to_screen(self, message):
            self.screen_messages.append(message)

        def format_to_screen(self, message, *args, **kwargs):
            self.screen_messages.append(message % (args, kwargs))

        def format_resolution(self, *args, **kwargs):
            return self.result

    class TestFunctions(unittest.TestCase):
        def setUp(self):
            self.downloader = MockDownloader('format_resolution_result')
            self.downloader.to_screen('test message')
            self.metadata_from_title = MetadataFromTitle

# Generated at 2022-06-14 18:07:12.159904
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class Downloader:
        def to_screen(self, msg):
            print(msg)

    pp = MetadataFromTitlePP(Downloader(), '%(title)s')
    info = {'title': 'Something'}
    pp.run(info)
    assert info['title'] == 'Something'

    pp = MetadataFromTitlePP(Downloader(), '%(id)s: %(title)s')
    info = {'title': 'Something'}
    pp.run(info)
    assert info['title'] == 'Something'

    pp = MetadataFromTitlePP(Downloader(), 'Bad title')
    info = {'title': 'Something'}
    pp.run(info)
    assert info['title'] == 'Something'


# Generated at 2022-06-14 18:07:19.587151
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .YoutubeDL import YoutubeDL
    from .FileDownloader import FileDownloader

    # Unit testing BasePostProcessor (abstract class) is not trivial as its constructor
    # raises an exception. So we create a FileDownloader instance,
    # which expects a FileDownloaderProcessor for the postprocessor.
    # FileDownloaderProcessor is a subclass of BaseProcessor, which is a subclass of BasePostProcessor.
    # In the unit tests, we just instantiate FileDownloaderProcessor directly,
    # which we should get away with because FileDownloaderProcessor is not supposed to be abstract.
    # And we call FileDownloaderProcessor.run() directly, which we should get away with because
    # FileDownloaderProcessor.run() just calls BaseProcessor.run(),
    # which encapsulates BasePostProcessor.run() with some basic error handling

# Generated at 2022-06-14 18:07:30.607590
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # We have a downloader object, but don't need it
    downloader = object()

    # Assume the titleformat is '%(title)s' and use a title with only the title
    titleformat = '%(title)s'
    title = 'my_title'
    info = {'title': title}
    pp = MetadataFromTitlePP(downloader, titleformat)
    _, info = pp.run(info)
    assert title in info, 'title not properly parsed'

    # Assume the titleformat is '%(title)s - %(artist)s' and use a title with the
    # title and the artist
    titleformat = '%(title)s - %(artist)s'
    title = 'my_title - my_artist'
    info = {'title': title}
    pp = Metadata

# Generated at 2022-06-14 18:07:39.291820
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.Downloader import Downloader
    downloader = Downloader()
    info = {
        'title': 'MyTitle - MyArtist - MyAlbum',
    }
    titleformat = '%(title)s - %(artist)s - %(album)s'
    pp = MetadataFromTitlePP(downloader, titleformat)
    assert pp.run(info) == ([],
        {
            'title': 'MyTitle',
            'artist': 'MyArtist',
            'album': 'MyAlbum',
        }
    )

    info = {
        'title': 'MyTitle - ',
    }
    titleformat = '%(title)s -'
    pp = MetadataFromTitlePP(downloader, titleformat)

# Generated at 2022-06-14 18:07:46.382769
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import Downloader
    from .compat import compat_urllib_request
    from .extractor import YoutubeIE
    from .compat import mock

    url = 'http://www.youtube.com/watch?v=BaW_jenozKc'
    titleformat = '%(artist)s - %(title)s'
    title = 'Herr Mannelig - Garmarna'
    artist = 'Garmarna'
    song = 'Herr Mannelig'

    ydl = Downloader()
    ydl._opener = compat_urllib_request.build_opener(compat_urllib_request.ProxyHandler(dict()))
    mock_ie = mock.Mock()
    mock_ie.extract.return_value = {'title': title}

# Generated at 2022-06-14 18:07:57.672736
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FileDownloader
    from .extractor import YoutubeIE

    downloader = FileDownloader({})
    # test video with an embedded video
    test_video_info = downloader.extract_info(YoutubeIE(), {'id': '_HSylqgVYQI'})
    # test video with no embedded video
    test_video_info2 = downloader.extract_info(YoutubeIE(), {'id': '_HSylqgVYQI', 'title': 'testVideo'})
    info = test_video_info['entries'][1]
    titleformat = '%(title)s - %(artist)s'
    metadatfromtitle = MetadataFromTitlePP(downloader, titleformat)
    empty_info = {}

# Generated at 2022-06-14 18:08:07.645357
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ytdl_config import config
    import sys
    import StringIO

    def get_test_info(title):
        info = {
            'title': title,
            'url': 'testurl',
            'site_name': 'testwebsite',
            'playlist': 'testplaylist',
        }
        return info

    def run_test(title, titleformat, expected_output=True, **kwargs):
        # mock downloader object
        from youtube_dl.downloader.common import FileDownloader
        downloader = FileDownloader(config.get_config())
        # mock stdout
        sys.stdout = out = StringIO.StringIO()
        # run test and get actual result
        test_info = get_test_info(title)
        pp = MetadataFromTitlePP(downloader, titleformat)

# Generated at 2022-06-14 18:08:14.394244
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    import os
    import unittest
    import tempfile
    from youtube_dl import YoutubeDL
    from youtube_dl.extractor import gen_extractors
    from youtube_dl.postprocessor import gen_pp_formats
    from youtube_dl.postprocessor import gen_pp_confs

    gen_extractors()
    gen_pp_formats()
    gen_pp_confs()
