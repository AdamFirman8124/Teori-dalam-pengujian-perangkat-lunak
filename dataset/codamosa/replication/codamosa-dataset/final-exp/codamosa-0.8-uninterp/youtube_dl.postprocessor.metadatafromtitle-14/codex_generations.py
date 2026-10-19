

# Generated at 2022-06-14 17:58:40.581703
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ..YoutubeDL import YoutubeDL

    def test_run_assertions(title, expected_metadata, titleformat):
        downloader = YoutubeDL({})
        processor = MetadataFromTitlePP(downloader, titleformat)
        tmetadata = {'title': title}
        _, metadata = processor.run(tmetadata)
        for attribute in expected_metadata:
            expected = expected_metadata[attribute]
            if expected is not None:
                assert(metadata[attribute] == expected)
            else:
                assert(attribute not in metadata)

    # the following tests do not fully match the titleformat

# Generated at 2022-06-14 17:58:50.686793
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import inspect
    import unittest

    global MetadataFromTitlePP
    class TestDownloader(object):
        def to_screen(self, string):
            pass

    class TestMetadataFromTitlePP(MetadataFromTitlePP):
        def __init__(self):
            super(TestMetadataFromTitlePP, self).__init__(
                TestDownloader(), '%(title)s - %(artist)s')

        def test_run(self, info):
            return self.run(info)

    # Test titleformat: '%(title)s - %(artist)s'
    # Test title: 'Test title - Test artist'
    test_title = 'Test title - Test artist'
    test_info = {'title': test_title}
    TestMeta = TestMetadataFromTitlePP()
    result = TestMeta

# Generated at 2022-06-14 17:59:01.768163
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ytdl.YoutubeDL import YoutubeDL
    ydl = YoutubeDL({})
    ydl.add_info_extractor('youtube')


# Generated at 2022-06-14 17:59:06.217704
# Unit test for method format_to_regex of class MetadataFromTitlePP
def test_MetadataFromTitlePP_format_to_regex():
    metadata = MetadataFromTitlePP(None, '%(title)s - %(artist)s')
    assert metadata.format_to_regex('%(title)s - %(artist)s') == (
        '(?P<title>.+)\ \-\ (?P<artist>.+)')


# Generated at 2022-06-14 17:59:13.854740
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.postprocessor import MetadataFromTitlePP
    import re

    downloader = YoutubeDL()
    title_pp = MetadataFromTitlePP(
        downloader,
        '%(uploader)s - %(title)s - %(duration)s - %(id)s.%(ext)s')
    info = {'title': 'Developer - Something in the way - 00:01:10 - '
                      'blabla123.webm',
            'format': 'best',
            'ext': 'webm',
            'id': 'blabla123'}
    pp = title_pp.run(info)


# Generated at 2022-06-14 17:59:23.914379
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class Downloader:
        def __init__(self):
            self.to_screen_calls = []

        def to_screen(self, text):
            self.to_screen_calls.append(text)

    info = {
        'title': 'Title - Artist',
        'format': 'best',
    }
    downloader = Downloader()

    pp = MetadataFromTitlePP(downloader, '%(title)s - %(artist)s')

    new_info, _ = pp.run(info)

    assert new_info['title'] is None
    assert new_info['artist'] is None
    assert downloader.to_screen_calls == [
        '[fromtitle] parsed title: Title',
        '[fromtitle] parsed artist: Artist',
    ]

# Generated at 2022-06-14 17:59:31.325054
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    downloader = None
    titleformat = '%(artist)s - %(title)s'
    video_info = {'title': 'Tony Carreira - Sonhador'}
    MP = MetadataFromTitlePP(downloader, titleformat)
    res, out = MP.run(video_info)
    assert(res == [])
    assert(out == {'title': 'Tony Carreira - Sonhador', 'artist': 'Tony Carreira'})


# Generated at 2022-06-14 17:59:39.702247
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class Downloader:
        def to_screen(self, s):
            pass

    class Info:
        def __init__(self):
            self.title = 'A title'
            self.videoname = 'A video name'
            self.folder = 'A folder'

    p = MetadataFromTitlePP(Downloader(),
                            '%(title)s (%(videoname)s)')
    info = Info()
    p.run(info)
    assert info['title'] == 'A title'
    assert info['videoname'] == 'A video name'
    assert info['folder'] == 'A folder'

    p = MetadataFromTitlePP(Downloader(),
                            '%(title)s')
    info = Info()
    p.run(info)
    assert info['title'] == 'A title'

# Generated at 2022-06-14 17:59:51.019548
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    """
    Main method to test MetadataFromTitlePP class.
    """
    from .common import YoutubeDL
    from .extractor import get_info_extractor
    from .utils import DateRange

    # Fake downloader with fake downloader
    class FakeDownloader:
        def to_screen(self, message):
            print(message)

    # Fake InfoExtractor to retrieve video info
    class FakeIE(object):
        IE_NAME = 'fake'
        _TESTS = [{
            'url': 'http://example.com/video1',
            'info_dict': {
                'id': 'video1',
                'title': 'Video title',
            },
        }]
        def _real_extract(self, url):
            return self._TESTS[0]['info_dict']

    # Fake

# Generated at 2022-06-14 18:00:02.427754
# Unit test for method run of class MetadataFromTitlePP

# Generated at 2022-06-14 18:00:13.873968
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    """
    test method MetadataFromTitlePP.run
    """
    # Arrange
    class Options(object):
        def __init__(self):
            self.postprocessors = [
                {'key': 'MetadataFromTitlePP',
                 'titleformat': '%(title)s - %(artist)s'}]
            self.verbose = True
    class Downloader(object):
        def __init__(self):
            self.options = Options()
            self.to_screen = print


# Generated at 2022-06-14 18:00:26.028594
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    DOWNLOADER = 'test' # fake downloader
    TITLEFORMAT = '%(artist)s - %(title)s'
    TITLEREGEX = '^(?P<artist>.+) - (?P<title>.+)'
    TITLE = 'Lena - Satellite'
    # Test without metadata_from_title
    info = {'title': 'Lena - Satellite'}
    expected_result_1 = [], {'title': 'Lena - Satellite'}
    test_1 = MetadataFromTitlePP(DOWNLOADER, None).run(info)
    assert test_1 == expected_result_1
    # Test with metadata_from_title
    info = {'title': 'Lena - Satellite'}

# Generated at 2022-06-14 18:00:36.904617
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    downloader = 'dummy'
    titleformat = '%(title)s - %(artist)s'
    titleformat_plus = '%(title)s - %(artist)s - %(track)s'
    obj = MetadataFromTitlePP(downloader, titleformat)
    info = {}
    info['title'] = 'Oasis - Wonderwall'
    result = obj.run(info)
    assert result[1]['title'] == 'Wonderwall'
    assert result[1]['artist'] == 'Oasis'

    obj = MetadataFromTitlePP(downloader, titleformat_plus)
    info = {}
    info['title'] = 'Oasis - Wonderwall - 01'
    result = obj.run(info)
    assert result[1]['title'] == 'Wonderwall'

# Generated at 2022-06-14 18:00:46.882754
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    """
    MetadataFromTitlePP_run() should return info, downloads:
        info: the unchanged input info
        downloads: a list of downloads (should be empty)
    """
    # given
    from youtube_dl.YoutubeDL import YoutubeDL
    downloader = YoutubeDL()
    postprocessor = MetadataFromTitlePP(downloader, '%(artist)s - %(title)s')
    info = {
                'title': 'Foo Fighters - Learn to Fly',
                'id': 'testId',
                'url': 'testUrl'
            }

    # when
    returns = postprocessor.run(info)

    # then
    info.update({
                'artist': 'Foo Fighters',
                'title': 'Learn to Fly'
                })
    downloads = []
    assert returns == (downloads, info)



# Generated at 2022-06-14 18:00:57.882800
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():

    import json

    class DummyYtdl:

        def to_screen(self, text):
            print(text)

        def format_to_regex(self, fmt):
            return MetadataFromTitlePP(self, fmt).format_to_regex(fmt)

    class DummyInfo:

        def __init__(self, title):
            self.title = title

    yt = DummyYtdl()

    print('\nTesting format_to_regex #1')
    fmt = '%(title)s'
    regex = yt.format_to_regex(fmt)
    expected_regex = r'(?P<title>.+)'
    print('regex for fmt %s should be %s' % (fmt, expected_regex))
    assert regex == expected_regex

   

# Generated at 2022-06-14 18:01:04.273014
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    title = 'Nirvana - Heart-Shaped Box'
    info = dict(title=title, titleformat='%(artist)s - %(song)s')
    metadata = MetadataFromTitlePP(None, info['titleformat'])
    _, info = metadata.run(info)
    assert info['artist'] == 'Nirvana'
    assert info['song'] == 'Heart-Shaped Box'

# Generated at 2022-06-14 18:01:11.366502
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    def run(title, titleformat):
        downloader = object()
        pp = MetadataFromTitlePP(downloader, titleformat)
        info = {'title': title}
        return pp.run(info)

    title = 'title:3:5:1:21:na:ndjfs'
    titleformat = '%(title)s:%(order)s:%(partnumber)s:%(part)s:%(track)s:' \
            '%(artist)s:%(album)s'
    actual = run(title, titleformat)
    expected = ({}, {'title': 'title', 'order': '3', 'partnumber': '5',
              'part': '1', 'track': '21', 'artist': 'na', 'album': 'ndjfs'})

# Generated at 2022-06-14 18:01:12.453557
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    pass


# Generated at 2022-06-14 18:01:23.712703
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class TestDownloader():
        def to_screen(self, msg):
            pass
    class TestInfo():
        def __init__(self, title):
            self['title'] = title

    title_with_extension = 'Test title (subtitle) [tag1, tag2].mkv'
    titleformat = '%(title)s (%(subtitle)s) [%(tags)s]'
    expected = {
        'title': 'Test title',
        'subtitle': 'subtitle',
        'tags': 'tag1, tag2'
    }
    test_info = TestInfo(title_with_extension)
    test_downloader = TestDownloader()
    test_pp = MetadataFromTitlePP(test_downloader, titleformat)

    actual, _ = test_pp.run(test_info)


# Generated at 2022-06-14 18:01:34.344762
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.downloader import PostProcessingError
    pp = MetadataFromTitlePP(None, "%(title)s - %(artist)s")

    info = {'title': 'Video title - Artist name'}
    pp.run(info)
    assert info['title'] == 'Video title'
    assert info['artist'] == 'Artist name'

    # Only the named groups should be extracted
    info = {'title': 'Video title - Artist name'}
    pp = MetadataFromTitlePP(None, "%(title)s - %(artist)s - %(not_at_all)s")
    pp.run(info)
    assert info['title'] == 'Video title'
    assert info['artist'] == 'Artist name'
    assert 'not_at_all' not in info

    # Non-matching should fail

# Generated at 2022-06-14 18:01:41.468379
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    info = {'title': 'Title - Artist'}
    mp = MetadataFromTitlePP(None, '%(title)s - %(artist)s')
    mp.run(info)
    assert info.get('title') == 'Title'
    assert info.get('artist') == 'Artist'

# Generated at 2022-06-14 18:01:48.311048
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # MetadataFromTitlePP.run raises ValueError on wrong regex
    for titleformat in ('(?<title>[0-9]+)', '%(title)s - %(artist)s'):
        pp = MetadataFromTitlePP(None, titleformat)
        try:
            pp.run({})
        except ValueError:
            continue # correct behavior
        assert False # should raise ValueError

    # MetadataFromTitlePP.run raises ValueError on wrong title
    for titleformat, title in (('(?<title>[0-9]+)', 'a10b'), # wrong regex
                               ('%(title)s - %(artist)s', 'a - b - c')): # wrong titleformat
        pp = MetadataFromTitlePP(None, titleformat)
        assert pp.run({'title':title}) == ([], {})

# Generated at 2022-06-14 18:01:59.494414
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FileDownloader
    from .extractor import gen_extractors
    ydl = FileDownloader()
    exts = gen_extractors(ydl)
    ext = exts['Youtube']('youtube-dl', ydl)
    ext.set_downloader(ydl)
    ext._real_initialize()

    info = {'uploader': 'NA', 'title': 'NA', 'ext': 'mp4',
            'id': 'NA', 'duration': 10}
    info_fromtitle = {'uploader': 'NA', 'title': 'NA', 'ext': 'mp4',
                      'id': 'NA', 'duration': 10, 'from_title': 'from_title'}

# Generated at 2022-06-14 18:02:08.727721
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.extractor.youtube import YoutubeIE

    downloader = YoutubeDL({
        'quiet': True,
        'extract_flat': 'in_playlist',
        'format': 'bestvideo[ext=webm]+bestaudio[ext=webm]/best[ext=webm]/best',
        'noplaylist': True,
        'simulate': True,
    })
    downloader.add_info_extractor(YoutubeIE())

    info_dicts = downloader.extract_info(
        'https://www.youtube.com/watch?v=BaW_jenozKc', download=False)['entries']

    postprocessor = MetadataFromTitlePP(downloader, '%(artist)s - %(title)s')



# Generated at 2022-06-14 18:02:09.660405
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    pass

# Generated at 2022-06-14 18:02:18.365342
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Test makes sure run() method of class MetadataFromTitlePP
    # produces expected output.
    # Input data
    url = 'https://www.youtube.com/watch?v=Y9OeOidVAPo'
    title = 'Waltz No. 7 in C-sharp minor, Op. 64 No. 2 - Arthur Rubinstein'
    titleformat = '%(title)s - %(artist)s'
    # Expected output
    expected_title = title
    expected_titleformat = titleformat
    expected_titleregex = 'Waltz\ No\.\ 7\ in\ C\-sharp\ minor\,\ Op\.\ 64\ No\.\ 2\ \-\ Arthur\ Rubinstein'

# Generated at 2022-06-14 18:02:24.085266
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class DummyDownloader(object):
        def to_screen(self, msg):
            pass

    processor = MetadataFromTitlePP(DummyDownloader(), '%(artist)s - %(title)s')
    info = { 'title': 'Muse - Apocalypse Please' }
    assert [] == processor.run(info)[0]
    assert info == { 'title': 'Muse - Apocalypse Please', 'artist': 'Muse' }

# Generated at 2022-06-14 18:02:33.001397
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    """Unit test
    This function is executed when the test is launched
    """
    # We will create a temporary download object
    from __main__ import FileDownloader
    ydl_opts = {
    }
    ydl = FileDownloader(ydl_opts)

    # We will execute the class
    f = MetadataFromTitlePP(ydl, "%(title)s - %(artist)s")
    info = {"title": "My Title - Artist Name", "format": "mp4"}
    f.run(info)

    # We will check if the new title is present
    if not "title" in info:
        # If not, we will display it
        print(info)

# Generated at 2022-06-14 18:02:42.561308
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common_tests import DownloaderMock
    
    titleformat = '%(title)s - %(artist)s'
    ydl = DownloaderMock()
    mdftpp = MetadataFromTitlePP(ydl, titleformat)
    test_video = {'title': 'Test Title - Test Artist'}
    empty_video = {'title': 'abc'}
    
    assert mdftpp.run(test_video) == ([], {'title': 'Test Title - Test Artist',
                                           'artist': 'Test Artist'})
    assert mdftpp.run(empty_video) == ([], {'title': 'abc'})

# Generated at 2022-06-14 18:02:54.139595
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL

    class MockYoutubeDL(YoutubeDL):
        def process_info(self, info):
            self.infos.append(info)

    pp = MetadataFromTitlePP(
        MockYoutubeDL({}, {'outtmpl': '%(title)s-%(autonumber)s.%(ext)s'}),
        '%(title)s-%(season_number)s-%(episode_number)s.%(ext)s')

    pp.run({'title': 'Wiener Dog Nationals'})
    assert pp._downloader.infos == []

    pp.run({'title': 'Wiener Dog Nationals S02E01.mp4'})

# Generated at 2022-06-14 18:03:03.602696
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ytdl_data_tst import downloader
    from ytdl_data_tst import video_info
    from ytdl_data_tst import expected_info

    pp = MetadataFromTitlePP(downloader, expected_info['titleformat'])
    info = {}
    pp.run(video_info)

    pas = 0
    for i in info:
        if info[i] == expected_info[i]:
            pas += 1

    assert pas == 3
    assert len(info) == 3

if __name__ == '__main__':
    test_MetadataFromTitlePP_run()

# Generated at 2022-06-14 18:03:12.141897
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import youtube_dl.YoutubeDL
    import youtube_dl.extractor.youtube

    # create test string for the title
    # As this example is for testing, it will be easy to parse
    metadata = {
        'artist' : 'The Black Eyed Peas',
        'title' : 'The Time (Dirty Bit)',
        'album'  : 'The Beginning',
        'track'  : '1'
    }
    metadata_string = '%(track)s: %(artist)s - %(title)s (%(album)s)' % metadata

    # create downloader
    downloader = youtube_dl.YoutubeDL({})

    # create test video
    # copy some keys from real video

# Generated at 2022-06-14 18:03:24.469489
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():

    import ytdl_extract

    ydl_opts = {'writethumbnail': True, 'socket_timeout': 20}
    ydl = ytdl_extract.YoutubeDL(ydl_opts)
    dl = ydl.download

    # Testing with a title format composed of a string
    titleformat = 'Video'
    regex = titleformat
    metadata = MetadataFromTitlePP(dl, titleformat)
    info = {'title': titleformat}
    metadata.run(info)
    assert info == {'title':titleformat}

    # Testing with a title format composed of a string with unicode characters
    titleformat = 'String with unicode characters éèàùìòÇ'
    regex = titleformat
    metadata = MetadataFromTitlePP(dl, titleformat)

# Generated at 2022-06-14 18:03:36.125301
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class dummy_downloader:
        def to_screen(self, s):
            print(s)
    downloader = dummy_downloader()
    assert MetadataFromTitlePP(downloader, '%(title)s').run({'title': 'test_title'}) == ([], {'title': 'test_title'})
    assert MetadataFromTitlePP(downloader, '%(title)s - %(artist)s').run({'title': 'test_title - john'}) == ([], {'title': 'test_title', 'artist': 'john'})
    assert MetadataFromTitlePP(downloader, '%(title)s - %(artist)s').run({'title': 'test_title - john - doe'}) == ([], {'title': 'test_title - john', 'artist': 'doe'})
   

# Generated at 2022-06-14 18:03:45.355477
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    mp = MetadataFromTitlePP(None, '%(title)s - %(artist)s')
    info = {
        'title': 'Hello - Lionel Richie'
    }
    assert mp.run(info) == ([], {
        'title': 'Hello - Lionel Richie',
        'artist': 'Lionel Richie'
    })
    mp = MetadataFromTitlePP(None, '%(artist)s - %(genre)s - %(title)s')
    assert mp.run(info) == ([], {
        'title': 'Hello - Lionel Richie',
        'artist': 'Lionel Richie',
        'genre': None
    })

# Generated at 2022-06-14 18:03:57.377803
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import os
    import tempfile
    import sys
    from ydl.downloader.YoutubeDL import YoutubeDL
    from ydl.postprocessor.FFmpegMetadataPP import FFmpegMetadataPP

    ydl = YoutubeDL({})
    titleformat = '%(title)s - %(creator)s'
    ydl.add_post_processor(FFmpegMetadataPP(ydl))
    ydl.add_post_processor(MetadataFromTitlePP(ydl, titleformat))
    files = [os.path.join(tempfile.gettempdir(), 'foo-%05d.mp3' % i)
             for i in range(3)]
    for f in files:
        open(f, 'w').close()
    info = {'title': 'foo - bar',
            'creator': 'quux'}


# Generated at 2022-06-14 18:04:09.350713
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from . import YoutubeDL
    from .compat import compat_str

    # Create a YoutubeDL object with the given params and method to_screen
    ydl = YoutubeDL({'skip_download': True, 'quiet': True,
                     'writethumbnail': False, 'write_info_json': False})
    ydl.to_screen = lambda *x: x

    # Create a MetadataFromTitlePP object
    pp = MetadataFromTitlePP(ydl, '%(title)s - %(artist)s')

    # Define result info of run method
    result_info = {'title': 'Test'}

    # Call the run method with this info
    result_info = pp.run(result_info)[1]

    # Check if the result info are correct
    assert result_info['title'] == 'Test'
    assert result

# Generated at 2022-06-14 18:04:20.354896
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .extractor.common import InfoExtractor
    from .downloader.f4mtest import F4mTestDownloader

    class DummyInfoExtractor(InfoExtractor):
        def __init__(self, downloader=None, *args, **kargs):
            super(DummyInfoExtractor, self).__init__(downloader, *args, **kargs)
            self._count = 0

        def _real_extract(self, url):
            self._count += 1
            return {
                'id': 'test',
                'title': 'Test %d' % self._count,
                'formats': [],
            }

    downloader = F4mTestDownloader()
    downloader.add_info_extractor(DummyInfoExtractor(downloader))

# Generated at 2022-06-14 18:04:31.551423
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    fake_downloader = {
        'params': {
            'verbose': False,
        },
        'to_screen': None,
    }
    fake_info = {
        'title': 'foo - bar',
        'uploader': '',
        'url': 'https://example.com',
    }

    pp = MetadataFromTitlePP(fake_downloader, '%(title)s - %(uploader)s')
    assert pp._titleformat == '%(title)s - %(uploader)s'
    assert pp._titleregex == '(?P<title>.+)\ \-\ (?P<uploader>.+)'

    # If pattern matches, it should modify the info dict.
    _, info = pp.run(fake_info)
    assert info['title'] == 'foo'
    assert info

# Generated at 2022-06-14 18:04:44.271056
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ..YoutubeDL import YoutubeDL
    y = YoutubeDL()
    y.params['simulate'] = True

    # simple case
    pp = MetadataFromTitlePP(y, '%(title)s-%(artist)s')
    info = {'title': 'Summertime Sadness - lana del rey'}
    pp.run(info)
    assert info == {
        'title': 'Summertime Sadness-lana del rey',
        'title_guessed': True,
        'artist': 'lana del rey',
        'artist_guessed': False
    }

    # parentheses in title
    pp = MetadataFromTitlePP(y, '%(title)s-%(artist)s')

# Generated at 2022-06-14 18:04:55.828364
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    def assert_correct_result(titleformat, title, expected_info):
        downloader = object()
        pp = MetadataFromTitlePP(downloader, titleformat)
        result = pp.run({'title': title})
        assert result == ([], expected_info)
    # titleformat: old
    assert_correct_result(r'%(artist)s - %(song)s', 'John Smith - A Song',
                          {'artist': 'John Smith', 'song': 'A Song'})
    assert_correct_result(r'%(artist)s - %(song)s', 'John Smith - A Song (feat. Michael Jackson)',
                          {'artist': 'John Smith', 'song': 'A Song (feat. Michael Jackson)'})

# Generated at 2022-06-14 18:05:00.133953
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    postprocessor = MetadataFromTitlePP('dummy', '%(title)s - %(artist)s')
    info = {'title': 'Title - Artist'}
    result = postprocessor.run(info)
    assert info['title'] == 'Title - Artist'
    assert info['artist'] == 'Artist'


# Generated at 2022-06-14 18:05:09.484377
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import unittest

    mock_downloader = unittest.mock.Mock()
    mock_downloader.to_screen = print
    info = {
        'title': 'Youtube_Unknown - TestTrack01',
        'ext': 'ogg'
    }
    fmt = '%(title)s - %(tracknumber)s'
    metadata = MetadataFromTitlePP(mock_downloader, fmt)
    expected = {
        'title': 'Youtube_Unknown',
        'tracknumber': 'TestTrack01',
        'ext': 'ogg'
    }
    result = metadata.run(info)
    assert result[1] == expected



# Generated at 2022-06-14 18:05:11.286399
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    pass

if __name__ == '__main__':
    test_MetadataFromTitlePP_run()

# Generated at 2022-06-14 18:05:21.944929
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Test string with format like 'This is a title - This is an artist'
    title = 'This is a title - This is an artist'
    fmt = '%(title)s - %(artist)s'

    info = {'title': title}
    titleformat = fmt
    mf = MetadataFromTitlePP(None, titleformat)
    result_info = mf.run(info)[1]
    assert result_info is not None
    assert result_info['title'] == 'This is a title'
    assert result_info['artist'] == 'This is an artist'

    # Test string with format like '(Artist) - This is a title - Title'
    title = '(Artist) - This is a title - Title'
    fmt = r'%(artist)s - %(title)s - %(title)s'

    info

# Generated at 2022-06-14 18:05:31.830329
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    """
    Unit test for method run of class MetadataFromTitlePP.
    """
    from .extractor import YoutubeIE
    from .common import FileDownloader

    youtube_ie = YoutubeIE()
    downloader = FileDownloader({'outtmpl': '%(title)s.%(ext)s'}, youtube_ie)
    pp = MetadataFromTitlePP(downloader, '%(title)s%(asdf)s_%(uploader)s')
    info = {
        'title': 'my title_my uploader',
        'url': 'http://www.youtube.com/watch?v=BaW_jenozKc',
        'webpage_url': 'http://www.youtube.com/watch?v=BaW_jenozKc',
        'ext': 'mp4',
    }
   

# Generated at 2022-06-14 18:05:43.961160
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    expected_metadata = {
        'title': 'Video Title',
        'artist': 'Artist Name',
        'date': '2017',
        'location': 'United Kingdom, London',
        'extrafield': "00'00\"",
    }
    expected_info = {
        'title': 'Video Title - Artist Name [2017] [United Kingdom, London] [00\'00\"]',
        'formats': 'mp4'
    }
    downloader = object()
    pp = MetadataFromTitlePP(downloader,
                             "%(title)s - %(artist)s [%(date)s] [%(location)s] [%(extrafield)s]")
    metadata, info = pp.run(expected_info)
    assert metadata == []

# Generated at 2022-06-14 18:05:50.968912
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import os

    import subprocess

    from .compat import compat_urllib_request

    from .YoutubeDL import YoutubeDL
    from .PostProcessor import PostProcessor

    if os.name != 'nt':
        return

    titleformats = ['%(uploader)s - %(title)s',
                    '%(title)s - %(uploader)s',
                    '%(title)s',
                    '%(uploader)s - %(title)s.%(ext)s',
                    '%(title)s.%(ext)s',
                    '%(uploader)s - %(title)s[%(id)s].%(ext)s',
                    '%(title)s[%(id)s].%(ext)s']

# Generated at 2022-06-14 18:05:55.930653
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class YoutubeDLMock:
        def to_screen(self, message):
            print(message)
    ydl = YoutubeDLMock()
    pp = MetadataFromTitlePP(ydl, '%(artist)s - %(song)s')
    info = {'title': 'The Bad Example', 'duration': 5}

    try:
        pp.run(info)
        assert False
    except:
        assert True

    info = {'title': 'The Bad Example - Sludge Juice', 'duration': 5}
    try:
        pp.run(info)
        assert False
    except:
        assert True

    info = {'title': 'The Bad Example - Sludge Juice', 'duration': 5, 'upload_date': '20160102'}

# Generated at 2022-06-14 18:06:04.711527
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class FakeInfo(dict):
        def __init__(self):
            self['title'] = 'title'
            self['artist'] = 'artist'
            self['date'] = 'date'

    class FakeDownloader():
        def to_screen(self, msg):
            print(msg)

    dummy_titleformat = '%(title)s - %(artist)s [%(date)s]'
    pp = MetadataFromTitlePP(FakeDownloader(), dummy_titleformat)
    dummy_info = FakeInfo()
    dummy_info['title'] = 'A title - A artist [YYYY-MM-DD]'
    pp.run(dummy_info)
    assert dummy_info['title'] == 'A title'
    assert dummy_info['artist'] == 'A artist'

# Generated at 2022-06-14 18:06:12.540134
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    title_format = '%(title)s - %(artist)s [%(album)s]'
    title_regex = '(?P<title>.+)\ \-\ (?P<artist>.+)\ \[(?P<album>.+)\]'
    title = 'Lunchmoney Lewis - Bills [Debut Single]'
    info = {'title': title}
    mft = MetadataFromTitlePP('dummy', title_format)
    _, info_out = mft.run(info)
    m = re.match(title_regex, title)
    if m is None:
        raise Exception(
                'Test title did not match regex "{0}"'
                .format(title_regex))
    for key, value in m.groupdict().items():
        if info_out[key] != value:
            raise

# Generated at 2022-06-14 18:06:23.821488
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from collections import namedtuple
    from youtube_dl.extractor.youtube import YoutubeIE
    from youtube_dl.utils import DateRange
    from youtube_dl.utils import get_timebase_id
    from youtube_dl.utils import DateRange
    from youtube_dl.utils import DateRange
    from youtube_dl.utils import std_headers
    from youtube_dl.utils import make_HTTPS_handler
    from youtube_dl.postprocessor import FFmpegMetadataPP
    from youtube_dl.downloader import YoutubeDL
    from youtube_dl.downloader.http import HttpFD
    from youtube_dl.downloader.common import FileDownloader
    from youtube_dl.downloader.f4m import F4mFD
    from youtube_dl.postprocessor import FFmpegMergerPP
    from youtube_dl.postprocessor import FFmpegVideo

# Generated at 2022-06-14 18:06:32.994608
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import youtube_dl.YoutubeDL
    from youtube_dl.utils import DownloadReturnCode

    ydl = youtube_dl.YoutubeDL(params={'noprogress': True})
    ydl.params.update({'writedescription': False, 'writeinfojson': False,
                       'writeannotations': False, 'writeautomaticsub': False,
                       'skip_download': True})
    pp = MetadataFromTitlePP(ydl, '%(title)s - %(artist)s')

    # first test with input values
    res, info = pp.run({'title': 'mytitle - myartist'})
    assert res == []
    assert info['title'] == 'mytitle'
    assert info['artist'] == 'myartist'

    # next test with no entries in info dictionary
    res, info = pp.run

# Generated at 2022-06-14 18:06:43.645015
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    def run_test(expected_title, expected_artist, expected_album,
                 expected_track, expected_track_total, expected_track_info,
                 expected_track_total_info,
                 title, info):

        assert len(info) == 0

        downloader = MagicMock()
        downloader.to_screen = MagicMock()
        pp = MetadataFromTitlePP(downloader, titleformat)

        # Check the result of the run method
        video_info, ret_info = pp.run(info)
        assert len(video_info) == 0

# Generated at 2022-06-14 18:06:54.931507
# Unit test for method run of class MetadataFromTitlePP

# Generated at 2022-06-14 18:07:03.676474
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys

    class Dummy(object):
        def to_screen(self, s):
            sys.stdout.write(s + '\n')

    # pylint: disable=missing-docstring
    class Downloader(object):
        def __init__(self, to_screen):
            self.to_screen = to_screen

    info = {'title': 'foo'}

    object = MetadataFromTitlePP(Downloader(Dummy().to_screen), '%(title)s')
    assert object.run(info) == ([], {'title': 'foo'})

    info = {'title': 'bar - foo'}
    object = MetadataFromTitlePP(
        Downloader(Dummy().to_screen), '%(title)s - %(artist)s')
    assert object.run(info)

# Generated at 2022-06-14 18:07:15.665679
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ..YoutubeDL import YoutubeDL
    common_data = {'title': 'Video Title - Artist'}
    formats = ['%(title)s - %(artist)s',
               '(?P<title>.+)\ \-\ (?P<artist>.+)',
               '%(title)s']
    correct_data = [{'title': 'Video Title - Artist',
                     'artist': 'Artist'},
                    {'title': 'Video Title - Artist',
                     'artist': 'Artist'},
                    {'title': 'Video Title - Artist'}]
    for i in range(len(formats)):
        pp = MetadataFromTitlePP(YoutubeDL(), formats[i])
        data = common_data.copy()
        pp.run(data)
        assert data == correct_data[i]

# Generated at 2022-06-14 18:07:24.776706
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ytdl import YoutubeDL
    ytdl = YoutubeDL({})
    pp = MetadataFromTitlePP(ytdl, '%(title)s - %(artist)s')
    info = {
        'title': 'Title - Artist',
        'website_url': 'http://example.com/url',
    }
    exit_code, info = pp.run(info)

    assert exit_code == []
    assert info['title'] == 'Title'
    assert info['artist'] == 'Artist'
    assert info['website_url'] == 'http://example.com/url'

# Generated at 2022-06-14 18:07:35.692162
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    import pytest

    from ytdl.YoutubeDL import YoutubeDL
    from ytdl.PostProcessor import PostProcessor
    from ytdl.compat import is_py2

    class MockYDL(YoutubeDL):
        def __init__(self, *args, **kwargs):
            super(MockYDL, self).__init__(*args, **kwargs)
            self.to_screen_str = ''

        def to_screen(self, msg):
            self.to_screen_str += msg

    class MockPP(PostProcessor):
        def __init__(self, *args, **kwargs):
            super(MockPP, self).__init__(*args, **kwargs)


# Generated at 2022-06-14 18:07:43.928874
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    import os
    import unittest
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.utils import format_bytes

    class FakeYoutubeDL(YoutubeDL):

        def to_screen(self, msg):
            sys.stderr.write('%s\n' % msg)

        def to_stdout(self, s):
            sys.stdout.write('%s\n' % s)

        def to_stderr(self, s):
            sys.stderr.write('%s\n' % s)


# Generated at 2022-06-14 18:07:59.615194
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    import io

    if sys.version_info < (3, 0):
        from StringIO import StringIO
    else:
        from io import StringIO

    from youtube_dl import YoutubeDL

    # Mock YoutubeDL
    class MockYoutubeDL(YoutubeDL):
        def __init__(self, *args, **kwargs):
            self.to_screen_buffer = StringIO()
            self.params = {}

        def to_screen(self, message, skip_eol=False):
            self.to_screen_buffer.write(message + '\n')

    # Mock downloader
    class MockDownloader:
        def __init__(self, *args, **kwargs):
            self.ydl = MockYoutubeDL()

    # Let's test!
    downloader = MockDownloader()
    result

# Generated at 2022-06-14 18:08:08.996393
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import youtube_dl.YoutubeDL
    ydl = youtube_dl.YoutubeDL()
    # Extract all fields
    pp = MetadataFromTitlePP(ydl, '%(title)s - %(artist)s')
    info = {'title': 'hello - youtube'}
    pp.run(info)
    assert info == {
        'title': 'hello - youtube',
        'artist': 'hello',
    }
    # Some fields not extracted
    pp = MetadataFromTitlePP(ydl, '%(title)s - %(artist)s')
    info = {'title': 'hello'}
    pp.run(info)
    assert info == {'title': 'hello'}
    # Avoid extracting field twice

# Generated at 2022-06-14 18:08:16.443359
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import pytube
    from pytube.tests import get_testdata_path

    yt = pytube.YouTube('www.youtube.com/watch?v=BaW_jenozKc')
    yt.set_filename('%(title)s-%(id)s-%(uploader)s')
    yt.download(get_testdata_path())

# Generated at 2022-06-14 18:08:23.838215
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.utils import DateRange
    from youtube_dl.extractor import (
        YoutubeIE,
        YoutubePlaylistIE,
        YoutubeUserIE,
        YoutubeChannelIE,
    )
    from youtube_dl.downloader.common import FileDownloader
    from youtube_dl.downloader.http import HttpFD

    class FakeYoutubeDL(YoutubeDL):
        def __init__(self, *args, **kwargs):
            super(FakeYoutubeDL, self).__init__(*args, **kwargs)
            self.downloaded_info_dicts = []

# Generated at 2022-06-14 18:08:26.599354
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # TODO: mock tempfile.mkdtemp
    # TODO: mock downloader
    # TODO: mock prepare_filename
    # TODO: mock stdout
    pass
