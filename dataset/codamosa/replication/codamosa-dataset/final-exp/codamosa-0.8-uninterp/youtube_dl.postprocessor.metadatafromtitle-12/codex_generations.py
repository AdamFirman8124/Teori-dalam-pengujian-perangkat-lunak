

# Generated at 2022-06-14 17:58:32.228629
# Unit test for method format_to_regex of class MetadataFromTitlePP
def test_MetadataFromTitlePP_format_to_regex():
    pp = MetadataFromTitlePP(None, None)
    assert pp.format_to_regex('%(title)s - %(artist)s') == r'(?P<title>.+)\ \-\ (?P<artist>.+)'

# Generated at 2022-06-14 17:58:41.867858
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import youtube_dl
    import os
    import tempfile
    import shutil

    testdir = os.path.realpath(tempfile.mkdtemp(prefix='test_youtube_dl_'))

# Generated at 2022-06-14 17:58:51.841132
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import unittest
    class TestMetadataFromTitlePP(unittest.TestCase):
        class DownloaderMockup(object):
            class FakeToScreen(object):
                def __init__(self):
                    self.messages = []
                def __call__(self, txt):
                    self.messages.append(txt)
            def __init__(self):
                self.to_screen = TestMetadataFromTitlePP.DownloaderMockup.FakeToScreen()
        def test_should_return_empty_list_and_info_if_title_matches_format(self):
            info = {'title': 'This is a - test'}
            titleformat = '%(title)s - %(somethingelse)s'

# Generated at 2022-06-14 17:58:59.763433
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from types import ModuleType
    downloader = ModuleType('downloader')
    downloader.to_screen = print
    downloader.params = {'quiet': True}
    info = {'title': 'My best song'}
    pp = MetadataFromTitlePP(downloader, '%(title)s')
    title = info['title']
    match = re.match(pp._titleregex, title)
    if match is None:
        downloader.to_screen(
            '[fromtitle] Could not interpret title of video as "%s"'
            % pp._titleformat)
    for attribute, value in match.groupdict().items():
        info[attribute] = value
        downloader.to_screen(
            '[fromtitle] parsed %s: %s'
            % (attribute, value if value is not None else 'NA'))

# Generated at 2022-06-14 17:59:09.582670
# Unit test for method format_to_regex of class MetadataFromTitlePP
def test_MetadataFromTitlePP_format_to_regex():
    assert (MetadataFromTitlePP(None, '%(title)s - %(artist)s')
            ._titleregex == '(?P<title>.+)\\ \\-\\ (?P<artist>.+)')
    assert (MetadataFromTitlePP(None, '%(artist)s - %(title)s')
            ._titleregex == '(?P<artist>.+)\\ \\-\\ (?P<title>.+)')
    assert (MetadataFromTitlePP(None, '%(artist)s - %(title)s - %(year)s')
            ._titleregex
            == '(?P<artist>.+)\\ \\-\\ (?P<title>.+)\\ \\-\\ (?P<year>.+)')
    # regex is greedy, will take last title

# Generated at 2022-06-14 17:59:21.980130
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Create object
    mftpp = MetadataFromTitlePP(None, '%(artist)s - %(title)s')

    # Create dummy info
    info = {
        'title': 'artist - title',
        'artist': None,
        'album': 'album',
        'track_number': '1'
    }

# Generated at 2022-06-14 17:59:25.898963
# Unit test for method format_to_regex of class MetadataFromTitlePP
def test_MetadataFromTitlePP_format_to_regex():
    pp = MetadataFromTitlePP(None, '%(title)s - %(artist)s')
    expected_regex = (r'(?P<title>.+)\ \-\ (?P<artist>.+)')
    assert pp._titleregex == expected_regex


# Generated at 2022-06-14 17:59:37.117075
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # test with one missing %(..)s in titleformat
    downloader = YoutubeDL(None)
    pp = MetadataFromTitlePP(downloader, 'this %(title)s')
    info = {'title': 'is title'}
    pp.run(info)
    assert info['title'] == 'is title'

    # test with one %(..)s in titleformat
    downloader = YoutubeDL(None)
    pp = MetadataFromTitlePP(downloader, 'this %(title)s is title')
    info = {'title': 'is title'}
    pp.run(info)
    assert info['title'] == 'this is title is title'

    # test with two %(..)s in titleformat
    downloader = YoutubeDL(None)

# Generated at 2022-06-14 17:59:49.098486
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    from __main__ import FakeYDL

    dl = FakeYDL()
    pp = MetadataFromTitlePP(dl, '%(title)s - %(artist)s')

    # returns info unmodified if the regex doesn't match
    info = {'title': 'foobar'}
    pp.run(info)
    assert info == {'title': 'foobar'}

    # returns info with additional attributes if the regex matches
    info = {'title': 'some title - some artist'}
    pp.run(info)
    assert info == {'title': 'some title - some artist',
                    'artist': 'some artist',
                    'title': 'some title'}

    # Sometimes the title doesn't contain all the info we want
    # (as in the case of the

# Generated at 2022-06-14 18:00:01.931985
# Unit test for method format_to_regex of class MetadataFromTitlePP
def test_MetadataFromTitlePP_format_to_regex():
    i = MetadataFromTitlePP('','')

# Generated at 2022-06-14 18:00:12.980730
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import random
    import unittest

    class FakeDL:
        def __init__(self):
            self.played = []
            self.infos = []

        def to_screen(self, msg):
            self.played.append(msg)

    class FakeInfo:
        def __init__(self):
            self.title = ''
            self.uploader = ''
            self.upload_date = ''
            self.track = ''
            self.creator = ''
            self.location = ''
            self.album = ''
            self.extractor = ''
            self.webpage_url = ''
            self.id = ''
            self.display_id = ''
            self.ext = ''
            self.format = ''
            self.playlist = ''
            self.playlist_index = None
            self.playlist

# Generated at 2022-06-14 18:00:14.592242
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    pass

# Generated at 2022-06-14 18:00:26.148475
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class PostProcessor(object):
        def __init__(self):
            self.screen_output = []
        def to_screen(self, message):
            self.screen_output.append(message)
    d = PostProcessor()
    pp = MetadataFromTitlePP(d, '%(title)s - %(artist)s')
    result, info = pp.run({'title': 'Title - Artist'})
    assert info['title'] == 'Title'
    assert info['artist'] == 'Artist'
    assert d.screen_output == ['[fromtitle] parsed title: Title',
                               '[fromtitle] parsed artist: Artist']
    d.screen_output = []
    result, info = pp.run({'title': 'Silly Title - for test'})
    assert info['title'] == None

# Generated at 2022-06-14 18:00:37.044792
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Tests that a video title can be parsed correctly based on a given format
    class FakeYDL:
        def __init__(self):
            self.check_result = ''
            self.screen_result = ''

        def check_executable(self, program, fallback_program=None):
            return self.check_result

        def to_screen(self, message):
            self.screen_result = message

    class FakeDownloader:
        def __init__(self):
            self.player_executable = 'avconv'
            self.postprocessor_args = {'key': 'value'}

    mp4_video_title = '''
    <title>Test video - Nils Frahm - Says</title>
    '''

# Generated at 2022-06-14 18:00:46.989952
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    import mock

    sys.modules['youtube_dl.extractor.common'] = mock.MagicMock()
    sys.modules['youtube_dl.extractor.youtube'] = mock.MagicMock()
    from youtube_dl.postprocessor.metadatafromtitle import MetadataFromTitlePP

    info = {
        'title': 'test - title'
    }
    pproc = MetadataFromTitlePP(mock.MagicMock(), '%(title)s')
    assert pproc.run(info) == ([], {'title': 'test', 'title_o': 'test - title'})

    pproc = MetadataFromTitlePP(mock.MagicMock(), '%(title)s - %(artist)s')

# Generated at 2022-06-14 18:00:54.485461
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    def _get_info(title):
        return {'title':title}
    titleformat = '%(title)s - %(artist)s'
    titleregex = MetadataFromTitlePP.format_to_regex(titleformat)
    match = re.match(titleregex, 'Happy - Pharrell')
    title = 'Happy - Pharrell'
    assert match.group('artist') == 'Pharrell'
    assert match.group('title') == 'Happy'



# Generated at 2022-06-14 18:01:06.902761
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    PP = MetadataFromTitlePP(None, '%(artist)s - %(title)s')
    info = {'title': 'Metallica - Nothing Else Matters'}
    PP.run(info)
    assert info == {'title': 'Metallica - Nothing Else Matters',
                    'artist': 'Metallica'}
    info = {'title': 'Metallica - Nothing Else Matters - [Lyrics]'}
    PP.run(info)
    assert info == {'title': 'Metallica - Nothing Else Matters - [Lyrics]',
                    'artist': 'Metallica'}

    PP = MetadataFromTitlePP(None, '%(artist)s - %(title)s')
    info = {'title': 'Metallica - Nothing Else Matters - [Lyrics]'}
    PP.run(info)


# Generated at 2022-06-14 18:01:19.414080
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    info = {'title': 'Dolor sit amet'}
    pp =  MetadataFromTitlePP(None, '%(title)s')
    pp.run(info)
    assert(info['title'] == 'Dolor sit amet')

    info = {'title': 'Dolor sit amet'}
    pp =  MetadataFromTitlePP(None, '%(title)s consectetur')
    pp.run(info)
    assert(info['title'] == 'Dolor sit amet')

    info = {'title': 'Dolor sit amet consectetur'}
    pp =  MetadataFromTitlePP(None, '%(title)s')
    pp.run(info)
    assert(info['title'] == 'Dolor sit amet consectetur')


# Generated at 2022-06-14 18:01:28.455236
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    import ydl_core
    info_dict = {'title': 'Foo - Bar'}
    # Create a post-processor:
    pp = MetadataFromTitlePP(None, '%(title)s - %(artist)s')
    _, info_dict = pp.run(info_dict)
    if sys.version_info < (3, 0):
        assert info_dict['title'] == u'Foo'
        assert info_dict['artist'] == u'Bar'
    else:
        assert info_dict['title'] == 'Foo'
        assert info_dict['artist'] == 'Bar'


# Generated at 2022-06-14 18:01:37.923526
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys, os, shutil
    import json

    # Create dump_json.py fixture
    dump_json_py = """#!/usr/bin/env python
# coding: utf-8

import sys
import json

for line in sys.stdin.readlines():
    _, title, _, filename = line.split(' ')
    video_info = {
        'title': title,
    }
    json.dump(video_info, sys.stdout)
    print('')

"""
    with open('dump_json.py', 'w') as f:
        f.write(dump_json_py)

    class FakeYoutubeDL:
        def __init__(self):
            self.cache = {}
            self.caches = {}

        def to_screen(self, message):
            print

# Generated at 2022-06-14 18:01:47.309487
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    def run_test(titleformat, title):
        info = {'title': title}
        pp = MetadataFromTitlePP(None, titleformat)
        pp.run(info)

    titleformat = '%(artist)s - %(title)s'
    title = 'My favourite artist - My favourite song is this'
    info = {'title': title}
    MetadataFromTitlePP(None, titleformat).run(info)
    assert info['artist'] == 'My favourite artist'
    assert info['title'] == 'My favourite song is this'

    # Test that missing fields are simply ignored.
    titleformat = '%(artist)s - %(title)s'
    title = 'My favourite song is this'
    info = {'title': title}
    MetadataFromTitlePP(None, titleformat).run(info)

# Generated at 2022-06-14 18:01:58.729303
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class FakeInfoDict():
        def __init__(self):
            self.infodict = {'title': None, 'artist': None, 'format': None}
            self.infodict_modified = None

        def get(self, key, default=None):
            return self.infodict[key]

        def __setitem__(self, key, value):
            self.infodict[key] = value
            self.infodict_modified = True

    class FakeDownloader():
        def to_screen(self, msg):
            print('[fromtitle] ' + msg)

    class FakeYDL():
        def __init__(self):
            self.downloader = FakeDownloader()

    titleformat = '%(title)s - %(artist)s.%(ext)s'

# Generated at 2022-06-14 18:02:08.667150
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    """
    Test method MetadataFromTitlePP.run
    """
    return
    # if len(sys.argv) > 1:
    #     title = sys.argv[1]
    #     titleformat = sys.argv[2]
    # else:
    #     title = '"Never Gonna Give You Up" Rick Astley'
    #     titleformat = '"%(title)s" %(artist)s'

    # mftpp = MetadataFromTitlePP(None, titleformat)
    # print('title:       ', title)
    # print('titleformat: ', titleformat)
    # info = {}
    # info['title'] = title
    # mftpp._downloader = None
    # postprocessors, info = mftpp.run(info)
    # print('postprocessors: ',

# Generated at 2022-06-14 18:02:15.731958
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import ydl
    opts = {
        'format': 'bestaudio',
        'format_id': 'bestaudio',
        'postprocessors': [{
            'key': 'MetadataFromTitle',
            'titleformat': '%(title)s',
        }]
    }
    downloader = ydl.YoutubeDL(opts)
    info = {'title': 'The Greatest Title'}
    downloader.process_info(info)
    assert info['title'] == 'The Greatest Title'


# Generated at 2022-06-14 18:02:27.633829
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import pytest
    mftpp = MetadataFromTitlePP(None, '%(title)s - %(artist)s')
    info = {'title': 'Title'}
    res, info = mftpp.run(info)
    assert res == []
    assert info['title'] == 'Title'

    mftpp = MetadataFromTitlePP(None, '%(title)s')
    info = {'title': 'Title'}
    res, info = mftpp.run(info)
    assert res == []
    assert info['title'] == 'Title'

    mftpp = MetadataFromTitlePP(None, '%(artist)s - %(title)s - %(album)s')
    info = {'title': 'Title - Album'}
    res, info = mftpp.run(info)

# Generated at 2022-06-14 18:02:34.038953
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.compat import compat_str
    from youtube_dl.utils import DateRange
    from youtube_dl.downloader.common import FileDownloader

    assert (MetadataFromTitlePP(Downloader(compat_str('my/path/%(title)s.%(ext)s')), '%(title)s').run(
            {'title': 'test', 'ext': 'mp4'}) ==
            ([], {'title': 'test', 'ext': 'mp4'}))

# Generated at 2022-06-14 18:02:43.171899
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import youtube_dl
    metadata2 = {'title': 'foo - bar - baz'}
    metadata3 = {'title': 'foo - bar - baz'}
    metadata4 = {'title': 'foo - bar - baz'}
    ydl = youtube_dl.YoutubeDL({'writedescription': True})
    ydl.add_post_processor(
        MetadataFromTitlePP(ydl, '%(title)s - %(artist)s'))
    ydl.add_post_processor(
        MetadataFromTitlePP(ydl, '%(artist)s - %(title)s'))
    ydl.add_post_processor(
        MetadataFromTitlePP(ydl, '%(title)s - %(artist)s - %(album)s'))
    ydl.add

# Generated at 2022-06-14 18:02:49.641458
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Test MetadataFromTitlePP with regex "%(title)s" (put title in the title)
    pp = MetadataFromTitlePP(None, '%(title)s')
    video_info = {'title': 'Title of the video'}
    result = pp.run(video_info)
    assert result[1]['title'] == 'Title of the video'
    assert 'Title of the video' in result[0]

    # Test MetadataFromTitlePP with regex "%(title)s - %(artist)s"
    pp = MetadataFromTitlePP(None, '%(title)s - %(artist)s')
    video_info = {'title': 'This is  -  a  -  test (feat. Artist)'}
    result = pp.run(video_info)
    assert result[1]['title']

# Generated at 2022-06-14 18:03:01.913098
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import unittest
    class TestMetadataFromTitlePP(unittest.TestCase):
        def setUp(self):
            pass

        def test_run(self):
            app = TestApp()
            md = MetadataFromTitlePP(app, '%(artist)s - %(title)s')
            info = {'title': 'Foo - Bar'}
            md.run(info)
            self.assertEqual(info, {'title': 'Foo - Bar', 'artist': 'Foo'})

            info = {'title': '[Foo] Bar'}
            md = MetadataFromTitlePP(app, '%(artist)s %(title)s')
            md.run(info)

# Generated at 2022-06-14 18:03:09.140232
# Unit test for method run of class MetadataFromTitlePP

# Generated at 2022-06-14 18:03:13.171758
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    pass


if __name__ == '__main__':
    test_MetadataFromTitlePP_run()

# Generated at 2022-06-14 18:03:21.933578
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import pytest

    class DummyYoutubeDL():
        def to_screen(self, msg):
            pass

    dl = DummyYoutubeDL()
    p = MetadataFromTitlePP(dl, '%(title)s - %(artist)s')

    info = {'title': 'Lazy Town - Bing Bang'}
    p.run(info)

    assert info['title'] == 'Lazy Town - Bing Bang'
    assert info['artist'] == 'Lazy Town'

    pytest.raises(
        Exception,
        p.run,
        {'title': 'Lazy Town'})

# Generated at 2022-06-14 18:03:26.657361
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import pytest  # pylint: disable=import-error
    test = MetadataFromTitlePP(None, '%(title)s - %(artist)s')
    metadata_list = []
    info = {'title': 'March of the Resistance - John Williams'}
    test.run(info)
    assert(info["title"] == "March of the Resistance")
    assert(info["artist"] == "John Williams")

# Generated at 2022-06-14 18:03:37.563356
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Test MetadataFromTitlePP.format_to_regex method
    assert MetadataFromTitlePP(None, '%(title)s+%(artist)s')._titleregex == '(?P<title>.+)\+(?P<artist>.+)'

    # Test MetadataFromTitlePP.run method
    info = {'title': 'abc', 'ext': 'mp4'}
    # Expect empty list as output
    assert MetadataFromTitlePP(None, '%(title)s+%(artist)s').run(info) == ([], info)
    # Set 'title' and 'artist' attributes in info
    title = 'abc+def'
    info['title'] = title
    assert title in info['title'] and title in info['artist']
    # Expect 'title' attribute in info to be updated
    assert MetadataFrom

# Generated at 2022-06-14 18:03:47.601700
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Test with a simple title format
    title = 'Song - Artist'
    metadata = MetadataFromTitlePP(None, '%(title)s - %(artist)s').run({'title': title})[1]

    assert metadata['title'] == 'Song'
    assert metadata['artist'] == 'Artist'

    # Test with a normal title format
    title = 'Album - Song - Artist'
    metadata = MetadataFromTitlePP(None, '%(album)s - %(title)s - %(artist)s').run({'title': title})[1]

    assert metadata['album'] == 'Album'
    assert metadata['title'] == 'Song'
    assert metadata['artist'] == 'Artist'

    # Test with a complex title format
    title = 'Song - Singer ft. Rapper'
    metadata = MetadataFrom

# Generated at 2022-06-14 18:03:58.601739
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import pytest
    from collections import defaultdict
    pp = MetadataFromTitlePP(None, '%(title)s')
    # Test 1
    info = defaultdict(lambda: None)
    info['title'] = 'The title'
    (a, b) = pp.run(info)
    assert info['title'] == 'The title'
    # Test 2
    info = defaultdict(lambda: None)
    info['title'] = 'The new title'
    (a, b) = pp.run(info)
    assert info['title'] == 'The new title'
    # Test 3
    info = defaultdict(lambda: None)
    info['title'] = 'The new title with multiple words'
    (a, b) = pp.run(info)
    assert info['title'] == 'The new title with multiple words'

# Generated at 2022-06-14 18:04:10.347496
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ydl.YDL import YDL
    downloader = YDL()
    # test basic functionality
    titleformat = '%(title)s %(uploader)s %(duration)s'
    titleregex = r'(?P<title>.+)\ (?P<uploader>.+)\ (?P<duration>.+)'
    title = 'Test video uploader 1337'

# Generated at 2022-06-14 18:04:21.218841
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ..compat import compat_str, compat_urllib_request
    from ..extractor import youtube_dl
    from ..utils import *

# Generated at 2022-06-14 18:04:31.746058
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from collections import OrderedDict

    # Import here to avoid circular import problem
    from youtube_dl.YoutubeDL import YoutubeDL

    downloader = YoutubeDL({})
    # Create a mock info dictionary
    info = OrderedDict()
    info['title'] = 'Title'
    
    # Test default behavior
    infoPP = MetadataFromTitlePP(downloader, '%(title)s').run(info)[1]
    assert infoPP['title'] == 'Title'
    assert len(infoPP.keys()) == 1

    # Test the exact title
    infoPP = MetadataFromTitlePP(downloader, 'Title').run(info)[1]
    assert infoPP['title'] == 'Title'
    assert len(infoPP.keys()) == 1

    # Test with created regex

# Generated at 2022-06-14 18:04:44.323962
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    from .common import FileDownloader

    class Extractor(object):
        def extract(self, url):
            return {'title': 'title'}

    class YoutubeDLMock(YoutubeDL):
        def __init__(self, *args, **kwargs):
            self.params = {}
            self.result_dict = {'extractor': 'extractor'}
            self.extractors = [
                ('extractor', Extractor(), r'.*', lambda x: True)
            ]

    fd = FileDownloader(YoutubeDLMock())
    pp = MetadataFromTitlePP(fd, '%(title)s')
    result_dict = fd.process_ie_result(pp.run(fd.result))

# Generated at 2022-06-14 18:04:57.712502
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import tempfile
    import shutil
    import os
    import ydl_core

    video_id = '3qEt2Xm8Tb0'

    success = False
    temp_dir = tempfile.mkdtemp(prefix='youtubedl-test-fromtitle-')

# Generated at 2022-06-14 18:05:08.648129
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Import here to avoid import errors in non-test code
    from youtube_dl.YoutubeDL import YoutubeDL
    from mock import Mock
    from .testutils import MockYDL

    def mockprint(s):
        pass

    # arrange
    ydl = MockYDL()
    ydl.to_screen = Mock(side_effect=mockprint)
    ydl.add_post_processor = Mock()
    ydl.params = {}
    ydl.params['writethumbnail'] = True

    info = {'title': 'test - foo'}
    f = MetadataFromTitlePP(ydl, '%(title)s - %(artist)s')

    # act
    f.run(info)

    # assert
    assert info['title'] == 'test'
    assert info['artist'] == 'foo'




# Generated at 2022-06-14 18:05:18.925551
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class TestDownloader():
        def __init__(self):
            self.userMSG = []
        def to_screen(self, msg):
            self.userMSG.append(msg)
    fake_title = 'The title - foo bar - sub1 - sub2'
    fake_video_info = {'title': fake_title,
                       'categories': None,
                       'webpage_url': 'http://www.fake.url',
                       'ext': 'fake',
                       'format': 'fake',
                       'player_url': None}
    # test with titleformat that contains only static strings
    static_titleformat = 'The title - foo bar'
    d = TestDownloader()
    pp = MetadataFromTitlePP(d, static_titleformat)
    [], info = pp.run(fake_video_info)

# Generated at 2022-06-14 18:05:29.524253
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .test.test_utils import FakeYDL
    from .extractor.common import InfoExtractor

    info = {'title': 'Test - abc - youtube.mp3'}

    class FakeInfoExtractor(InfoExtractor):
        def __init__(self):
            super(FakeInfoExtractor, self).__init__()

        def _real_extract(self, url):
            return info

    ydl = FakeYDL()
    ydl.add_info_extractor(FakeInfoExtractor())

    pp = MetadataFromTitlePP(ydl, '%(title)s - %(ext)s')
    pp.run(info)
    assert 'title' in info
    assert info['title'] == 'Test - abc'
    assert 'ext' in info
    assert info['ext'] == 'mp3'

# Generated at 2022-06-14 18:05:41.930517
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    """
    Test case for testing the method run of the class MetadataFromTitlePP from module ytdl.
    """

    class DummyClass:
        """
        Dummy class for simulating youtube-dl.
        """

        def __init__(self):
            self.to_screen = None

        def simulation_to_screen(self, string):
            """
            In simulation, the class to_screen will print the string.
            """

            print(string)

    downloader = DummyClass()
    downloader.to_screen = downloader.simulation_to_screen
    
    info = dict([('title', 'Test_title'), ('description', 'Test_description'), ('formats', 'Test_formats')])
    titleformat = '%(title)s'

# Generated at 2022-06-14 18:05:48.152019
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import youtube_dl
    ydl = youtube_dl.YoutubeDL()
    titleformat = '%(title)s - %(artist)s'
    pp = MetadataFromTitlePP(ydl, titleformat)
    info = {'title': 'Bruno Mars - When I Was Your Man (Official Video)'}
    pp.run(info)
    assert info == {
        'title': 'Bruno Mars - When I Was Your Man (Official Video)',
        'artist': 'Bruno Mars',
               }

# Generated at 2022-06-14 18:05:55.723862
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import os
    import tempfile
    from youtube_dl.downloader.HttpFD import HttpFD

    # Create temp test file with no content
    (fd1, tfile1) = tempfile.mkstemp()
    os.close(fd1)

    # Create temp test file with title and description
    title = 'Le Chameau by Chris Zabriskie is licensed under a Creative Commons Attribution licence (https://creativecommons.org/licenses/...'
    description = 'Source: http://chriszabriskie.com/cormorant/Artwork: https://flic.kr/p/nhpSPH'
    (fd2, tfile2) = tempfile.mkstemp()

# Generated at 2022-06-14 18:06:03.476731
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.utils import DateRange
    from youtube_dl.utils import DateRange
    ydl = YoutubeDL({'simulate': True})
    pp = MetadataFromTitlePP(ydl, '%(title)s - %(artist)s')
    assert pp.run({'title': 'Can\'t Help Falling In Love - Elvis Presley'})[1] == {
        'title': "Can't Help Falling In Love",
        'artist': 'Elvis Presley',
    }
    assert pp.run({'title': 'Can\'t Help Falling In Love'})[1] == {'title': "Can't Help Falling In Love"}

# Generated at 2022-06-14 18:06:12.630759
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # When called with bad title, run() does nothing
    pp = MetadataFromTitlePP(None, '%(artist)s - %(song)s')
    info = {'title': 'badtitle', 'artist': 'oldartist', 'song': 'oldsong'}
    assert pp.run(info) == ([], info)
    assert info['artist'] == 'oldartist'
    assert info['song'] == 'oldsong'

    # When called with good title, run() parses title and updates info
    pp = MetadataFromTitlePP(None, '%(artist)s - %(song)s')
    info = {'title': 'Metallica - Nothing Else Matters', 'artist': 'oldartist', 'song': 'oldsong'}
    assert pp.run(info) == ([], info)

# Generated at 2022-06-14 18:06:23.867067
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Initialize
    import youtube_dl.YoutubeDL
    youtube_dl.YoutubeDL._setup_opener()

    # Prepare
    re_title = (r'(?P<year>\d{4}) MyTitle.+-(?P<season>\d+x?\d+)'
                r'(?P<episode>\d+\-?\d?\d?)(?P<extension>\.\w+)')
    mftpp = MetadataFromTitlePP(youtube_dl.YoutubeDL, re_title)
    info = {
        'title': '2016 MyTitle - 20170x17-18.mp4',
    }

# Generated at 2022-06-14 18:06:44.282536
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .downloader import Downloader
    from .extractor import GenYoutubeIE
    from .youtube_dl.PostProcessor import run_post_processors

# Generated at 2022-06-14 18:06:55.516352
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import pytest

    from youtube_dl.utils import DateRange
    class FakeInfo:
        def __init__(self, t):
            self.title = t
    class FakeYdl:
        def __init__(self):
            self.to_screen = print

    assert (MetadataFromTitlePP(
        FakeYdl(), '%(title)s - %(artist)s').run(
            FakeInfo('The title - The artist'))[1].title ==
            'The title - The artist')

    ydl = FakeYdl()
    assert (MetadataFromTitlePP(
        ydl, '%(artist)s - %(title)s').run(
            FakeInfo('The title - The artist'))[1].title ==
            'The title - The artist')

# Generated at 2022-06-14 18:07:05.408366
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class FakeInfo:
        def __init__(self, title):
            self.title = title
    class FakeYoutubeDL:
        def to_screen(self, *args):
            pass
    # Successfull matches
    mp = MetadataFromTitlePP(FakeYoutubeDL(), '%(artist)s - %(track)s')
    assert mp.run(FakeInfo('Coldplay - Magic')) == ([], {'artist': 'Coldplay', 'track': 'Magic'})
    mp = MetadataFromTitlePP(FakeYoutubeDL(), '%(title)s - %(artist)s')
    assert mp.run(FakeInfo('Magic - Coldplay')) == ([], {'title': 'Magic', 'artist': 'Coldplay'})

# Generated at 2022-06-14 18:07:15.830220
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ydl.postprocessor.metadatafromtitle import MetadataFromTitlePP
    from ydl.YDL import YDL
    # Init downloader
    downloader = YDL()
    # Init postprocessor
    pp = MetadataFromTitlePP(downloader, "%(title)s - %(artist)s")

    # Test: Match
    info = {'title': 'foo - bar'}
    assert pp.run(info) == ([],{'title': 'foo - bar', 'artist': 'bar'})

    # Test: No match
    info = {'title': 'foo bar'}
    assert pp.run(info) == ([],{'title': 'foo bar'})

if __name__ == '__main__':
    import sys

# Generated at 2022-06-14 18:07:23.233448
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.downloader.common import FileDownloader
    pp = MetadataFromTitlePP(FileDownloader({}), '%(title)s - %(artist)s')
    info = {
        'title': 'TITLE - ARTIST',
    }
    (info1, info2) = pp.run(info)
    assert info1 == []
    assert info2 == {
        'title': 'TITLE - ARTIST',
        'artist': 'ARTIST',
    }

# Generated at 2022-06-14 18:07:34.576553
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    import os
    import unittest
    from ydl.postprocessor import MetadataFromTitlePP
    from ydl.YDLDummy import YDLDummy

    def format_to_regex(fmt):
        lastpos = 0
        regex = ''
        # replace %(..)s with regex group and escape other string parts
        for match in re.finditer(r'%\((\w+)\)s', fmt):
            regex += re.escape(fmt[lastpos:match.start()])
            regex += r'(?P<' + match.group(1) + '>.+)'
            lastpos = match.end()
        if lastpos < len(fmt):
            regex += re.escape(fmt[lastpos:])
        return regex


# Generated at 2022-06-14 18:07:43.083796
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import ytdl_post_processor

    title_format_tests = {
        '%(title)s': {
            'title': 'test'
        },
        '%(title)s - %(artist)s': {
            'title': 'test',
            'artist': 'Agnes',
        },
        '%(title)s - %(artist)s [%(album)s] %(date)s': {
            'title': 'test',
            'artist': 'Agnes',
            'album': 'test',
            'date': '2018',
        },
    }


# Generated at 2022-06-14 18:07:53.898602
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import youtube_dl.YoutubeDL
    from youtube_dl.postprocessor.metadatafromtitle import MetadataFromTitlePP
    downloader = youtube_dl.YoutubeDL({})
    pp = MetadataFromTitlePP(downloader, '%(artist)s - %(title)s - %(track)s')

    info = {
        'title': 'Maroon 5 - Sugar - 3',
        'artist': None,
        'track': None
    }
    pp.run(info)
    assert info == {
        'title': 'Maroon 5 - Sugar - 3',
        'artist': 'Maroon 5',
        'track': '3'
    }

    info = {
        'title': 'Maroon 5 - Sugar - 33',
        'artist': None,
        'track': None
    }

# Generated at 2022-06-14 18:08:04.653893
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    """
    Example of MetadataFromTitlePP usage.
    """
    from youtube_dl import YoutubeDL
    from youtube_dl.postprocessor import MetadataFromTitlePP

    ydl = YoutubeDL({'outtmpl': '%(title)s.%(ext)s',
                     'postprocessors': [MetadataFromTitlePP(ydl,
                                                            '%(artist)s - %(title)s')],
                    })
    info = ydl.extract_info('http://www.youtube.com/watch?v=BaW_jenozKc', download=False)
    assert 'artist' in info
    assert info['artist'] == 'David'
    assert 'title' in info
    assert info['title'] == 'Guetta - Where Them Girls At ft. Nicki Minaj, Flo Rida'

# Generated at 2022-06-14 18:08:12.064221
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import pytest
    # The titleformat string doesn't contain any %(..)s patterns
    # so method format_to_regex doesn't do anything
    # and the method run takes the titleformat string as it is
    # and matches it against the title string

    # test for the positive case
    mftpp = MetadataFromTitlePP(None, 'Test - Title')
    info = { 'title': 'Test - Title' }
    assert mftpp.run(info) == ([], info)

    # test for the negative case
    mftpp = MetadataFromTitlePP(None, 'Test - Title')
    info = { 'title': 'Test - Title_Abcd' }
    assert mftpp.run(info) == ([], info)

    # The titleformat string contains %(..)s patterns
    # so method format_