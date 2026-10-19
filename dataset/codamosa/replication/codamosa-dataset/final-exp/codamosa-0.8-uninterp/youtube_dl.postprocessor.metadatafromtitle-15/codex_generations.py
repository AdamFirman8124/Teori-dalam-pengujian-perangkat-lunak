

# Generated at 2022-06-14 17:58:35.614602
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Create a mocked downloader instance
    class MockDownloader(object):
        def to_screen(self, msg):
            pass

    # Create a mocked info dictionary
    info = {
        'title': 'Foo & Bar - Baz [Tag]',
        'format': 'Tag',
    }

    # Create a instance of MetadataFromTitlePP
    pp = MetadataFromTitlePP(MockDownloader(), '%(title)s [%(format)s]')

    # Execute method
    pp.run(info)

    # Compare original title with title from run method
    assert info['title'] == 'Foo & Bar - Baz [Tag]'

# Generated at 2022-06-14 17:58:43.385230
# Unit test for method format_to_regex of class MetadataFromTitlePP
def test_MetadataFromTitlePP_format_to_regex():
    class Test:
        def format_to_regex(self, fmt):
            return MetadataFromTitlePP(None, fmt).format_to_regex(fmt)

    obj = Test()

# Generated at 2022-06-14 17:58:49.123001
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class FakeDownloader:
        def to_screen(self, msg):
            pass
    class FakeInfo:
        def __getitem__(self, key):
            return self.__dict__[key]
        def __setitem__(self, key, value):
            self.__dict__[key] = value
    metadataFromTitlePP = MetadataFromTitlePP(FakeDownloader(), '%(artist)s - %(title)s - %(album)s')
    info = FakeInfo()
    info.title = 'Ludovico Einaudi - Nuvole Bianche [Live at Le Poisson Rouge, NYC] (2016)'
    metadataFromTitlePP.run(info)
    assert info.artist == 'Ludovico Einaudi'

# Generated at 2022-06-14 17:59:00.276959
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import unittest

    def build_info():
        return {'title': 'a title', 'track': '2', 'artist': 'b artist'}

    def build_downloader(to_screen):
        class DummyDownloader:
            def to_screen(dummy_self, x):
                to_screen(x)
        return DummyDownloader()

    # setup downloader
    dl = build_downloader(to_screen=print)

    # Test match with regex
    pp = MetadataFromTitlePP(dl, '%(track)s-%(artist)s-%(title)s')
    info = build_info()
    info['title'] = '2-b artist-a title'
    run_result = pp.run(info)
    assert len(run_result) == 2            # 2 elements in

# Generated at 2022-06-14 17:59:07.293286
# Unit test for method format_to_regex of class MetadataFromTitlePP
def test_MetadataFromTitlePP_format_to_regex():
    from .common import FileDownloader
    mp = MetadataFromTitlePP(FileDownloader(None), '')
    assert mp.format_to_regex('%(title)s - %(artist)s') == r'(?P<title>.+)\ \-\ (?P<artist>.+)'
    assert mp.format_to_regex('%(title)s') == r'(?P<title>.+)'
    assert mp.format_to_regex('%(title)d') == r'(?P<title>\d+)'

# Generated at 2022-06-14 17:59:19.349710
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.utils import DateRange
    from youtube_dl.compat import compat_urllib_request
    import youtube_dl.extractor.common as common


# Generated at 2022-06-14 17:59:30.095851
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    video_info = {'title': 'Test1 - Test2 - Test3'}
    title_format = '%(test1)s - %(test2)s - %(test3)s'
    result = MetadataFromTitlePP(None, title_format).run(video_info)
    assert result == ([], {'test1': 'Test1', 'test2': 'Test2', 'test3': 'Test3', 'title': 'Test1 - Test2 - Test3'})

    video_info = {'title': 'Test1 - Test2 - Test3'}
    title_format = '%(test1)s - %(test2)s'
    result = MetadataFromTitlePP(None, title_format).run(video_info)

# Generated at 2022-06-14 17:59:41.841020
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.utils import DateRange
    from youtube_dl.extractor.common import InfoExtractor
    from datetime import datetime

    NOP = lambda *args, **kargs: None

    # Test parse of title:
    #     '%(artist)s - %(title)s'
    # by setting:
    #     titleformat='%(artist)s - %(title)s'
    # and verifying that attribute artist and title
    # of the info-dictionary have been set according
    # to the video title.
    class TestIE(InfoExtractor):
        def __init__(self, titleformat):
            self._titleformat = titleformat
            InfoExtractor.__init__(self, 'testie')


# Generated at 2022-06-14 17:59:52.219397
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    info = {
        'title': 'Test title - Test artist - Test genre'
    }
    from_title = MetadataFromTitlePP(None, '%(title)s - %(artist)s - %(genre)s')
    _, info = from_title.run(info)
    assert info['artist'] == 'Test artist'
    assert info['genre'] == 'Test genre'

    info = {
        'title': 'Test title (Test artist) [Test genre]'
    }
    from_title = MetadataFromTitlePP(None, '%(title)s (%(artist)s) [%(genre)s]')
    _, info = from_title.run(info)
    assert info['artist'] == 'Test artist'
    assert info['genre'] == 'Test genre'


# Generated at 2022-06-14 17:59:58.378726
# Unit test for method format_to_regex of class MetadataFromTitlePP
def test_MetadataFromTitlePP_format_to_regex():
    pp = MetadataFromTitlePP(None, None)
    '%(title)s - %(artist)s'
    assert '^(?P<title>.+)\\ \-\\ (?P<artist>.+)$' == pp.format_to_regex(
        '%(title)s - %(artist)s')
    '%(title)s-%(artist)s'
    assert '^(?P<title>.+)\\-(?P<artist>.+)$' == pp.format_to_regex(
        '%(title)s-%(artist)s')
    '%(title)s-%(artist)s-%(year)04d'

# Generated at 2022-06-14 18:00:09.829551
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    mftpp = MetadataFromTitlePP(None, '%(title)s - %(artist)s')
    assert mftpp._titleregex == r'(?P<title>.+)\ \-\ (?P<artist>.+)'

    info = {'title': 'my title - my artist'}
    info_out = dict(info)
    info_out['title'] = 'my title'
    info_out['artist'] = 'my artist'

    retval = mftpp.run(info)
    assert set(retval[1].keys()) == set(info_out.keys())
    assert retval[1] == info_out

    info['title'] = 'my title - my artist - my year'
    info_out['year'] = 'my year'

# Generated at 2022-06-14 18:00:20.587049
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import pytube

    class FakeYT:
        def __init__(self, title):
            self._title = title

        @property
        def title(self):
            return self._title


# Generated at 2022-06-14 18:00:21.748003
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # TODO
    pass

# Generated at 2022-06-14 18:00:30.514865
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import pytest

    class TestPP(MetadataFromTitlePP):
        def run(self, info):
            return super(TestPP, self).run(info)

    pp = TestPP(None, '%(title)s - %(artist)s')
    assert pp.format_to_regex('%(title)s - %(artist)s') == r'(?P<title>.+)\ \-\ (?P<artist>.+)'
    assert pp._titleregex == r'(?P<title>.+)\ \-\ (?P<artist>.+)'

    # Scenario 1: match
    result, info = pp.run({'title': 'this is the title - and the artist'})
    assert result == []
    assert info == {'title': 'this is the title', 'artist': 'and the artist'}

# Generated at 2022-06-14 18:00:39.821671
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Arrange
    info = {
        'title': 'a - b - c',
    }
    pp = MetadataFromTitlePP(None, '%(a)s - %(b)s - %(c)s')
    # Act
    [], actual = pp.run(info)
    # Assert
    expected = {
        'title': 'a - b - c',
        'a': 'a',
        'b': 'b',
        'c': 'c',
    }
    assert expected == actual


# Generated at 2022-06-14 18:00:45.130937
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ..YoutubeDL import YoutubeDL
    postprocessor = MetadataFromTitlePP(YoutubeDL(), '%(title)s')
    info = {'title': 'Unit test passing'}
    postprocessor.run(info)
    assert info['title'] == 'Unit test passing'
    info = {'title': 'Unit test passing - But very motly'}
    postprocessor.run(info)
    assert info['title'] == 'Unit test passing'

# Generated at 2022-06-14 18:00:54.413834
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FileDownloader
    from .extractor import get_info_extractor
    class FakeInfoExtractor(get_info_extractor(None)):
        def _real_extract(self, url):
            return {
                'id': 'test',
                'title': title
            }

    downloader = FileDownloader({
        'outtmpl': 'test',
        'postprocessors': [
            MetadataFromTitlePP(downloader, '%(title)s - %(id)s')
        ],
        'quiet': True
    })

    extractor = FakeInfoExtractor()
    title = 'title - test'
    result = downloader.extract_info(extractor, 'url', {})
    assert (title == result['title'])

    title = 'title - test - abc'


# Generated at 2022-06-14 18:01:06.903707
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ytdl.utils import create_downloader

    downloader = create_downloader()
    pp = MetadataFromTitlePP(downloader, '%(title)s by %(artist)s')
    info = {'title': 'My title'}
    pp.run(info)
    assert info == {'title': 'My title'}, 'test_MetadataFromTitlePP_run1'

    downloader = create_downloader()
    pp = MetadataFromTitlePP(downloader, '%(title)s - %(artist)s')
    info = {'title': 'My title - My artist'}
    pp.run(info)
    assert info == {
        'artist': 'My artist',
        'title': 'My title - My artist',
    }, 'test_MetadataFromTitlePP_run2'

   

# Generated at 2022-06-14 18:01:19.355771
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL

    class DummyYDL(YoutubeDL):
        def __init__(self, params):
            self.params = params
            self.downloaded_info_dicts = []

        def to_screen(self, s):
            pass

        def download(self, info):
            self.downloaded_info_dicts.append(info)

    ydl = DummyYDL({
        'writedescription': True,
        'writeannotations': True,
        'writethumbnail': True,
        'writeinfojson': True,
        'writesubtitles': True,
        'writeautomaticsub': True,
        'nooverwrites': False,
        'ignoreerrors': False,
    })

# Generated at 2022-06-14 18:01:26.513766
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl import YoutubeDL
    from youtube_dl.YoutubeDL import YoutubeDL
    ydl = YoutubeDL({})
    ydl.add_post_processor(MetadataFromTitlePP)
    info = {
        'title': 'My new title - by Me!',
    }
    ydl.process_ie_result(info, download=False)
    assert info['title'] == 'My new title'
    assert info['creator'] == 'Me!'


# Generated at 2022-06-14 18:01:38.174579
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():

    # Import standard modules
    import os
    import sys
    import unittest
    import tempfile
    from collections import namedtuple

    # Import from testfixture
    from .testfixture import FakeYDL

    # Import from classes
    from .fromtitle import MetadataFromTitlePP

    # Class variables
    tmpdir = tempfile.gettempdir()
    tmpfile = os.path.join(tmpdir, 'tmp.txt')
    outfile = os.path.join(tmpdir, 'out.mp3')
    titleformat = (r'%(title)s - %(tracknumber)s - %(artist)s - %(album)s '
                   r'- %(albumartist)s - %(date)s - %(genre)s')
    url = 'https://fake1.com/abc.mp3'


# Generated at 2022-06-14 18:01:46.589774
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    assert MetadataFromTitlePP(None, '%(artist)s - %(title)s').run({'title': 'Santana - Oye Como Va'})[1] == {'artist': 'Santana', 'title': 'Oye Como Va'}
    assert MetadataFromTitlePP(None, '%(artist)s - %(title)s').run({'title': 'Santana -'})[1] == {'artist': 'Santana', 'title': ''}
    assert MetadataFromTitlePP(None, '%(artist)s - %(title)s').run({'title': 'Santana - Oye Como Va -'})[1] == {'artist': 'Santana', 'title': 'Oye Como Va -'}


# Generated at 2022-06-14 18:01:58.412284
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.compat import compat_etree_fromstring
    from youtube_dl.downloader import Downloader
    from youtube_dl.extractor import YoutubeIE

# Generated at 2022-06-14 18:02:04.953404
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    import youtube_dl.YoutubeDL

    class InfoDict(dict):
        def __setitem__(self, key, value):
            if key in ('title', 'artist', 'track', 'album', 'year'):
                super(InfoDict, self).__setitem__(key, value)

    class YoutubeDL(youtube_dl.YoutubeDL):
        def __init__(self, *args, **kwargs):
            super(YoutubeDL, self).__init__(*args, **kwargs)
            self.to_screen = lambda *args, **kwargs: None

    p = MetadataFromTitlePP(YoutubeDL({}), '%(title)s - %(artist)s')
    info = InfoDict()

    info = InfoDict()

# Generated at 2022-06-14 18:02:15.659443
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    import pytest
    from youtube_dl.YoutubeDL import YoutubeDL
    from fake_pytest import FakeYDL

    ydl = FakeYDL()
    ydl.add_info_extractor("fake_IE")
    ydl.add_post_processor(MetadataFromTitlePP(ydl, '%(track)s - %(artist)s'))

    ydl.process_ie_result(
        {'id': '12345', 'extractor': 'fake_IE', 'title': 'Audio Title - Artist Name'},
        download=False)
    assert ydl.get_download_result()['track'] == 'Audio Title'
    assert ydl.get_download_result()['artist'] == 'Artist Name'


# Generated at 2022-06-14 18:02:27.634747
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FakeYDL
    from .compat import compat_str

    METADATA = {
        'title': 'test'
    }
    ydl = FakeYDL(METADATA)
    pp = MetadataFromTitlePP(ydl, "%(title)s")
    pp.run(METADATA)
    assert METADATA['metadataFromTitle'] == {'title': 'test'}
    pp = MetadataFromTitlePP(ydl, "%(title)s - %(artist)s")
    METADATA['title'] = 'mytitle - myartist'
    pp.run(METADATA)
    assert METADATA['metadataFromTitle'] == {'title': 'mytitle', 'artist': 'myartist'}
    METADATA['title'] = 'mytitle - myartist feat. bob'
    pp

# Generated at 2022-06-14 18:02:34.031063
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FakeYDL
    from .compat import compat_str

    tformat = '%(track)s - %(artist)s - %(album)s'
    title = 'Mamushi - Anna Tsuchiya - Spin me round'
    regex = '^(?P<track>.+)\ \-\ (?P<artist>.+)\ \-\ (?P<album>.+)$'

    mftpp = MetadataFromTitlePP(FakeYDL(), tformat)
    mftpp._titleregex = regex

    # usual case: title matches the regex
    info = {'title': title}
    [], info = mftpp.run(info)
    assert info['track'] == 'Mamushi'
    assert info['artist'] == 'Anna Tsuchiya'

# Generated at 2022-06-14 18:02:43.138444
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import json
    import tempfile

    with tempfile.NamedTemporaryFile(mode='w+t') as f:
        f.write(json.dumps([
            {
                "title": "title1 - artist1 - album1",
                "url": "url1",
                "webpage_url": "webpage_url1",
            },
            {
                "title": "title2 - artist2",
                "url": "url2",
                "webpage_url": "webpage_url2",
            },
        ]))
        f.flush()

        from .common import FileDownloader
        outtmpl = '%(title)s-%(artist)s-%(album)s.%(ext)s'

# Generated at 2022-06-14 18:02:51.994443
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class DummyDownloader:
        def to_screen(self, message):
            print(message)

    dummydownloader = DummyDownloader()
    titleformat = '%(title)s - %(artist)s'
    metadatafromtitle = MetadataFromTitlePP(dummydownloader, titleformat)
    title = 'My Beautiful Song - Mysterious Composer'
    info = {'title': title}
    metadatafromtitle.run(info)
    assert info['title'] == 'My Beautiful Song'
    assert info['artist'] == 'Mysterious Composer'


# Generated at 2022-06-14 18:03:02.715010
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .test import get_testcases_skip_online, fake_formats
    YDStreamExtractor = None
    try:
        from ydl.extractor import get_info as YDStreamExtractor
    except ImportError:
        pass

    testcases = get_testcases_skip_online(YDStreamExtractor)
    _downloader = PostProcessor(None)


    def _t(titleformat, expected):
        _downloader.to_screen = print
        pp = MetadataFromTitlePP(_downloader, titleformat)
        result_info = {
            'title': 'Random title'
        }
        result = []
        pp.run(result_info)
        for key, value in expected.items():
            assert result_info[key] == value, key + ": " + repr(result_info[key])

# Generated at 2022-06-14 18:03:17.534069
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # https://github.com/rg3/youtube-dl/pull/19264
    from .downloader import Downloader
    from .extractor.common import InfoExtractor

    class FakeIE(InfoExtractor):
        def __init__(self, *args, **kwargs):
            pass

        @classmethod
        def suitable(cls, *args):
            return True

    ie = FakeIE('http://example.com')
    ie._downloader = Downloader({})

    def run_test(titleformat, title):
        pp = MetadataFromTitlePP(ie._downloader, titleformat)
        info = {'title': title}
        out, target = pp.run(info)
        assert target == {'title': title}
        return target

    # Normal title

# Generated at 2022-06-14 18:03:27.341963
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    '''
    Test for method run of class MetadataFromTitlePP
    '''
    from ytdl.YoutubeDL import YoutubeDL
    class MockYoutubeDL(YoutubeDL):
        def __init__(self):
            self.cache_fn = None
            self.params = {}
            self.to_screen_called_with = []

        def to_screen(self, msg):
            self.to_screen_called_with.append(msg)

        def report_warning(self, msg):
            self.to_screen_called_with.append(msg)

    ydl = MockYoutubeDL()
    pp = MetadataFromTitlePP(ydl, '%(uploader)s - %(title)s')
    title = 'foo'
    uploader = 'bar'

# Generated at 2022-06-14 18:03:29.030333
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # TODO: Add tests for method run of class MetadataFromTitlePP
    #assert (False, "Not implemented yet")
    return True


# Generated at 2022-06-14 18:03:35.609259
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    downloader = None
    fromtitle = MetadataFromTitlePP(downloader, '%(title)s - %(artist)s')
    info = {'title': 'test title - test artist', 'uploader': 'test uploader'}
    expected = (['', info])
    result = fromtitle.run(info)
    assert result == expected
    assert result[1]['title'] is None
    assert result[1]['artist'] == 'test artist'


# Generated at 2022-06-14 18:03:46.708991
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class TestDownloader(object):
        def to_screen(self, message):
            print(message)
    class TestInfo(dict):
        pass
    titleformat = '%(title)s - %(artist)s'
    for title in ['Title - Artist', 'Title -Artist', 'Title-Artist', 'Title- Artist', 'Title - Artist ', 'Title - Artist-', 'Title - Artist-0']:
        info = TestInfo({'title': title})
        MetadataFromTitlePP(TestDownloader(), titleformat).run(info)
        if title == 'Title- Artist':
            assert info['title'] == 'Title-'
            assert info['artist'] == 'Artist'
        elif title == 'Title - Artist ':
            assert info['title'] == 'Title'
            assert info['artist'] == 'Artist'

# Generated at 2022-06-14 18:03:57.845022
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    from types import ModuleType
    from unittest.case import TestCase
    from ..YoutubeDL import YoutubeDL

    dl_class = ModuleType('YoutubeDL')
    dl_class.__dict__ = YoutubeDL.__dict__
    dl_class.to_screen = lambda self, msg: sys.stdout.write(msg + '\n')
    dl_class.params = {}

    class Downloader(object):
        ydl = dl_class

        def to_screen(self, msg):
            sys.stdout.write(msg + '\n')

    class Test(TestCase):
        def setUp(self):
            self.d = Downloader()

        def run_and_compare(self, info, format, infoout_dict={}):
            p = MetadataFrom

# Generated at 2022-06-14 18:04:09.533508
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ytdl.YoutubeDL import YoutubeDL
    ydl = YoutubeDL()
    ydl.params = {'verbose': True}
    def get_title(title):
        return {'title': title}
    failed_titles = []
    def assert_title(title, **res):
        info = get_title(title)
        result, info = MetadataFromTitlePP(ydl, '%(artist)s - %(title)s').run(info)
        assert info == res, repr((title, info))

    assert_title(
        'a',
        title='a')
    assert_title(
        'a - b',
        artist='a', title='b')
    assert_title(
        'a - b - c',
        artist='a', title='b - c')
    assert_title

# Generated at 2022-06-14 18:04:19.373619
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import pytube.extract
    from pytube.exceptions import RegexMatchError

    # Test with ``%(title)s``
    titleformat = '%(title)s'
    mfpp = MetadataFromTitlePP(None, titleformat)
    assert mfpp._titleregex == r'(?P<title>.+)'

    title = '1 2 3 4 5 6 7 8 9 0'
    info = { 'title': title }
    [], info = mfpp.run(info)
    assert info['title'] == title

    # Test with ``%(title)s - %(artist)s - %(album)s - %(track)s``
    titleformat = '%(title)s - %(artist)s - %(album)s - %(track)s'
    mfpp = Metadata

# Generated at 2022-06-14 18:04:30.653664
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Python 2 and 3 compatible test.
    # The first element of the tuple is the input and the second element is the expected output.
    tests = [
        ('%(title)s-%(artist)s', (' - ', {})),
        ('%(artist)s - %(title)s', ('', {})),
        ('%(title)s %(artist)s', ('', {'title': '%(title)s', 'artist': '%(artist)s'})),
        ('%(title)s', ('', {'title': '%(title)s'})),
        ('%(title)s%(artist)s', ('', {'title': '%(title)s', 'artist': '%(artist)s'})),
    ]

# Generated at 2022-06-14 18:04:41.091950
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ..extractor.common import InfoExtractor
    from ..compat import compat_urllib_request
    from .common import FileDownloader

    fmt = '%(title)s - %(artist)s'
    title_fmt = 'Artist Name - Title of the Video'
    title_nonmatch = 'Title of the Video'
    regex = r'(?P<title>.+)\ \-\ (?P<artist>.+)'
    good_data = '[{"format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]"}]'

    # Create mocks
    ie = InfoExtractor()
    ie.set_downloader(FileDownloader())
    title = title_fmt

# Generated at 2022-06-14 18:05:03.314970
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    def method_run(downloader, titleformat, title, result_expected):
        downloader.to_screen = lambda a: None
        pp = MetadataFromTitlePP(downloader, titleformat)
        result_obtained = pp._titleregex
        pp.run({'title': title})
        assert result_obtained == result_expected
        
    # Test 1:
    # Input:
    #    titleformat = %(artist)s - %(track)s
    #    title = Eminem - Lose Yourself
    # Expected output:
    #    (?P<artist>.+)\ \-\ (?P<track>.+)

# Generated at 2022-06-14 18:05:10.419172
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.utils import DateRange
    from datetime import date

    # required for tests
    from youtube_dl.utils import DateRange
    from datetime import date


# Generated at 2022-06-14 18:05:21.061610
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    from .YoutubeDL import YoutubeDL
    from .extractor.youtube import YoutubeIE

    class MyYoutubeDL(YoutubeDL):
        def process_ie_result(self, ie_result):
            return ie_result

    ydl = MyYoutubeDL({'outtmpl': '%(uploader)s-%(upload_date)s-%(id)s.%(ext)s'})
    ie = YoutubeIE(ydl)

    # First test YoutubeIE

# Generated at 2022-06-14 18:05:31.216682
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import pytest
    from __main__ import FakeDownloader

    titleformat = '%(title)s - %(artist)s'
    title = 'Lilac Blossom - Tokuhiko Saigusa'
    info = {'title': title, 'artist': None}

    pp = MetadataFromTitlePP(FakeDownloader(), titleformat)
    assert pp._titleregex is '(?P<title>.+)\ \-\ (?P<artist>.+)'

    metadata, new_info = pp.run(info)
    assert metadata == []
    assert new_info['artist'] == 'Tokuhiko Saigusa'

    # no titleformat
    pp = MetadataFromTitlePP(FakeDownloader(), '')
    metadata, new_info = pp.run(info)

# Generated at 2022-06-14 18:05:43.511522
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    def _create_downloader_object(to_screen_val):
        class MockYDL:
            def to_screen(self, msg_string):
                to_screen_val.append(msg_string)
        return MockYDL()


# Generated at 2022-06-14 18:05:52.026319
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    import unittest
    import data

    class TestMetadataFromTitlePP(unittest.TestCase):
        def setUp(self):
            self.pp = MetadataFromTitlePP(None, '%(test)s')
            self.pp._downloader = DummyDownloader()

        def test_extract_test(self):
            info = {
                'title': 'abcd',
            }
            self.pp.run(info)
            self.assertEqual(info, {
                'title': 'abcd',
                'test': 'abcd',
            })

        def test_extract_test_with_spaces(self):
            info = {
                'title': 'ab cd',
            }
            self.pp.run(info)

# Generated at 2022-06-14 18:06:02.713415
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import mock
    import os

    # Setup the test dependencies
    info = mock.Mock()
    info.title = 'Youtube-DL Test Video'
    info.fromtitle = False
    ffmpeg = mock.Mock()
    to_screen = mock.Mock(return_value='')
    postprocessor = MetadataFromTitlePP(None, 'Lorem %(ipsum)s dolor')
    postprocessor._downloader.to_screen = to_screen

    # test results
    results, info = postprocessor.run(info)
    assert info.fromtitle == True
    assert info.ipsum == 'Lorem Youtube-DL Test Video dolor'
    to_screen.assert_called_with('[fromtitle] parsed ipsum: Lorem Youtube-DL Test Video dolor')



# Generated at 2022-06-14 18:06:03.958394
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from test import get_test_config
    from youtube_dl import Youtub

# Generated at 2022-06-14 18:06:09.015258
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    pp = MetadataFromTitlePP('fake_downloader', '%(title)s - %(artist)s')
    assert pp.run({'title': 'foo - bar'}) == ([], {'title': 'foo - bar', 'artist': 'bar'})
    assert pp.run({'title': 'foo'}) == ([], {'title': 'foo'})



# Generated at 2022-06-14 18:06:21.460406
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    from collections import defaultdict
    from youtube_dl.compat import compat_str

    TestYDL = type('TestYDL', (YoutubeDL,), {'to_screen': lambda *args: None})
    testydl = TestYDL({})
    pp = MetadataFromTitlePP(testydl, '%(field)s')
    testcases = [
        # Testcase: titleformat, title, expected field value, expected info
        ('(test) %(test)s', 'abc', 'abc', defaultdict(str, field=str(None), test=str('abc'))),
    ]
    for titleformat, title, expected, expectedinfo in testcases:
        info = defaultdict(str, title=compat_str(title))
        pp = MetadataFromTitle

# Generated at 2022-06-14 18:06:52.401438
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # test case 1:
    metadata_from_titlepp = MetadataFromTitlePP(None, '%(title)s - %(artist)s')
    info = {'title': 'Test Title - Test Artist'}
    metadata_from_titlepp.run(info)
    assert info['title'] == 'Test Title - Test Artist'
    assert info['artist'] == 'Test Artist'
    
    # test case 2:
    metadata_from_titlepp = MetadataFromTitlePP(None, '%(title)s - %(artist)s')
    info = {'title': 'Test Title - Test Artist - Test Album'}
    metadata_from_titlepp.run(info)
    assert info['title'] == 'Test Title - Test Artist - Test Album'
    assert 'artist' not in info
    
    # test case 3:

# Generated at 2022-06-14 18:07:03.493567
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .ytdl_mocks import MockYoutubeDL
    from .ytdl_mocks import MockYoutubeDLFile

    # Mocks the following test run:
    #
    # ydl -j --metadata-from-title "%(artist)s - %(song)s" https://website.org/videoplay?v=videoid
    #
    # Expected outcome:
    #
    #   [fromtitle] Could not interpret title of video as "%(artist)s - %(song)s"
    #   [fromtitle] parsed artist: NA
    #   [fromtitle] parsed song: NA

# Generated at 2022-06-14 18:07:15.626394
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import gc
    from .common import FileDownloader
    downloader = FileDownloader(params={})
    downloader.params.update({
        'outtmpl': '%(id)s',
        'usetitle': True})

    # Tests for miscellaneous video title formats

# Generated at 2022-06-14 18:07:27.681047
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ytdl_gen.downloader import Downloader
    from ytdl_gen.extractor.common import InfoExtractor

    class DummyExtractor(InfoExtractor):
        def get_info(self, uri):
            return {
                '_type': 'url',
                'title': 'Some Title',
                'uploader': 'Somebody',
                'ext': 'mp4',
                'format_id': '18',
                'url': 'http://dummy/12345.mp4',
            }

    dl = Downloader({'noprogress': True, 'quiet': True})
    dl._extractors['youtube'] = DummyExtractor(dl).suitable
    dl._download_retcode = 'ffmpeg'
    dl._num_downloads = 1


# Generated at 2022-06-14 18:07:34.933494
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    import tempfile
    import shutil

    # For now, since we don't know how to test the output of the to_screen
    # function and what it is outputting, we will test to see if the info
    # dictionary is correct.
    ydl = YoutubeDL({})
    titleformat = '%(title)s - %(artist)s'
    pp = MetadataFromTitlePP(ydl, titleformat)

    # Case 1: Test to see if the info dictionary is correct.

# Generated at 2022-06-14 18:07:41.933781
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Given
    titleformat = '%(title)s - %(artist)s'
    title = 'Loreen - Euphoria - Live - Grand Final - 2012 Eurovision Song Contest'
    title_info = { 'title': title }
    mfrtp = MetadataFromTitlePP(None, titleformat)

    # When
    result_extracted, result_title_info = mfrtp.run(title_info)

    # Then
    assert result_extracted == []
    assert result_title_info == {
        'title': 'Loreen',
        'artist': 'Euphoria - Live - Grand Final - 2012 Eurovision Song Contest'
    }

# Generated at 2022-06-14 18:07:53.379087
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.postprocessor.embedthumbnail import EmbedThumbnailPP

    #
    # Test 1
    #

    # We need to use a subclass of YoutubeDL, otherwise the YDL instance
    # will not allow adding postprocessors.
    class DummyYDL(YoutubeDL):
        def __init__(self, *args, **kargs):
            super(DummyYDL, self).__init__(*args, **kargs)

            # We need to add a PostProcessor to the ydl instance, otherwise
            # the all_files attribute will be None and the code won't be executed
            self.add_post_processor(EmbedThumbnailPP())

    ydl = DummyYDL()

# Generated at 2022-06-14 18:08:04.190774
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.downloader import YoutubeDL
    from youtube_dl.postprocessor.common import PostProcessor
    from youtube_dl.InfoExtractors import YoutubeIE

    # Construct youtube-dl object
    ydl = YoutubeDL({'no-color': True, 'quiet': True})

    # Add URL to the list of URLs
    ydl.add_info_extractor(YoutubeIE())

    ydl.add_post_processor(MetadataFromTitlePP(ydl, '%(title)s'))
    ydl.params['skip_download'] = True
    result = ydl.extract_info(
        'http://www.youtube.com/watch?v=BaW_jenozKc',
        download=False
    )

    print(result)

# Generated at 2022-06-14 18:08:11.784169
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.extractor.youtube import YoutubeIE

    ydl = YoutubeDL({})
    ie = YoutubeIE(ydl)

    pp = MetadataFromTitlePP(ydl, '%(title)s')
    info = { 'title' : 'foo' }
    results = pp.run(info)
    assert results == ([], info), results

    pp = MetadataFromTitlePP(ydl, '%(upload_date)s')
    info = { 'title' : '20160101' }
    results = pp.run(info)
    assert results == ([], {'upload_date': '20160101', 'title': '20160101'}), results


# Generated at 2022-06-14 18:08:16.641244
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    v_info = dict()
    v_info['title'] = 'This-is-title'
    pp = MetadataFromTitlePP(None, '%(title)s')
    processed_info, info_dict = pp.run(v_info)
    assert info_dict['title'] == 'This-is-title'
