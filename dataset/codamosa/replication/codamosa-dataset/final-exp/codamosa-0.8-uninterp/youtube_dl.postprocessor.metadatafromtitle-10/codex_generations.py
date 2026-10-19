

# Generated at 2022-06-14 17:58:41.296907
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL

    ydl = YoutubeDL()
    ydl.params['skip_download'] = True
    pp = MetadataFromTitlePP(ydl, '%(upload_date)s - %(id)s - %(title)s')

    info = {'title': '20140101 - xyz - test'}
    pp.run(info)

    assert info == {
        'title': '20140101 - xyz - test',
        'upload_date': '20140101',
        'id': 'xyz',
    }

    info = {'title': 'xyz - test'}
    pp.run(info)

    assert info == {'title': 'xyz - test'}

# Generated at 2022-06-14 17:58:47.752423
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import YoutubeDL
    from .extractor.youtube import YoutubeIE

    # Test with '%(title)s - %(artist)s'
    ydl = YoutubeDL({})
    ie = YoutubeIE(ydl)
    title = 'title - artist'
    metadataFromTitlePP = MetadataFromTitlePP(ydl, '%(title)s - %(artist)s')
    (formats, info) = metadataFromTitlePP.run(
        ie._extract_info(ie._download_webpage(ie._VALID_URL, ie._VIDEO_RE, {'id': 'video_id'}),
        video_id = 'video_id',
        url = ie._VALID_URL,
        title = title))
    assert info['title'] == 'title'
    assert info['artist'] == 'artist'

# Generated at 2022-06-14 17:58:58.261108
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ydl.base import FakeYDL

    ydl = FakeYDL()
    pp = MetadataFromTitlePP(ydl, '%(title)s - %(artist)s')
    info = {'title': 'video title'}
    assert pp.run(info) == ([], info)

    ydl = FakeYDL()
    pp = MetadataFromTitlePP(ydl, '%(artist)s - %(title)s')
    info = {'title': 'video title'}
    assert pp.run(info) == ([], {'artist': 'video title',
                                 'title': None})

    ydl = FakeYDL()
    pp = MetadataFromTitlePP(ydl, '%(artist)s - %(title)s')
    info = {'title': 'video title - with dash'}

# Generated at 2022-06-14 17:59:08.438701
# Unit test for constructor of class MetadataFromTitlePP
def test_MetadataFromTitlePP():
    from .extractor import gen_extractors

    titleformat = '%(title)s - %(artist)s'
    extractor = gen_extractors(downloader=None)[0]()
    pp = MetadataFromTitlePP(downloader=None, titleformat=titleformat)
    title = 'Song Title - Artist Name'
    info = {'title': title}
    info = pp.run(info)[1]
    assert info['title'] == 'Song Title'
    assert info['artist'] == 'Artist Name'

    titleformat = '%(title)s'
    extractor = gen_extractors(downloader=None)[0]()
    pp = MetadataFromTitlePP(downloader=None, titleformat=titleformat)
    title = 'Song Title'
    info = {'title': title}
    info

# Generated at 2022-06-14 17:59:14.019925
# Unit test for method format_to_regex of class MetadataFromTitlePP
def test_MetadataFromTitlePP_format_to_regex():
    pp = MetadataFromTitlePP(None, '%(first)s - %(second)s')
    assert pp.format_to_regex('%(first)s - %(second)s') == '(?P<first>.+)\ \-\ (?P<second>.+)'

# Generated at 2022-06-14 17:59:24.428021
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.postprocessor import ffmpegmetadata
    from youtube_dl.postprocessor.metadatafromtitle import MetadataFromTitlePP
    import pickle

# Generated at 2022-06-14 17:59:34.964611
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    postprocessor = MetadataFromTitlePP(None, '%(artist)s - %(title)s')

# Generated at 2022-06-14 17:59:46.131337
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    info1 = {
        'title': 'This is a title'}
    pp = MetadataFromTitlePP(None, '%(title)s')
    pp.run(info1)
    assert info1['title'] == 'This is a title'
    info2 = {
        'title': 'This is a title - Artist'}
    pp = MetadataFromTitlePP(None, '%(title)s - %(artist)s')
    pp.run(info2)
    assert info2['title'] == 'This is a title'
    assert info2['artist'] == 'Artist'
    info3 = {
        'title': 'This is a title - Artist - Album'}
    pp = MetadataFromTitlePP(None, '%(title)s - %(artist)s - %(album)s')
    pp.run

# Generated at 2022-06-14 17:59:50.986834
# Unit test for constructor of class MetadataFromTitlePP
def test_MetadataFromTitlePP():
    """
    Creates an instance of MetadataFromTitlePP with titleformat and
    calls format_to_regex() method to test the conversion of the titleformat to
    the expected regex
    """
    mft = MetadataFromTitlePP(None, '%(title)s - %(artist)s')
    assert mft._titleformat == '%(title)s - %(artist)s'
    assert mft._titleregex == '(?P<title>.+)\ \-\ (?P<artist>.+)'

# Generated at 2022-06-14 18:00:02.419631
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import io
    import os
    import sys
    import tempfile
    import unittest

    from youtube_dl import YoutubeDL

    # Simulate the downloader class in YoutubeDL (noop methods)
    class NoopYoutubeDL(YoutubeDL):
        def __init__(self, params):
            self.params = params
        def to_screen(self, message):
            #print(message)
            pass

    class TestMetadataFromTitlePP(unittest.TestCase):
        def setUp(self):
            self.postprocessor = MetadataFromTitlePP(NoopYoutubeDL(None),
                                                     '%(artist)s - %(title)s')
            self.fname = None


# Generated at 2022-06-14 18:00:13.180450
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FileDownloader
    from .compat import compat_str
    downloader = FileDownloader(params={
        'noprogress': True,
        'format': 'bestaudio/best',
        'outtmpl': False,
        'quiet': False,
        'ignoreerrors': False,
        'forceurl': False,
        'forcetitle': False,
        'forcethumbnail': False,
        'forcedescription': False,
        'forcefilename': False,
        'forceduration': False,
        'forceformat': False,
        'forcejson': False,
        'simulate': True,
        'skip_download': True,
    })
    postprocessor = MetadataFromTitlePP(downloader,
                                        titleformat='%(title)s - %(artist)s')


# Generated at 2022-06-14 18:00:25.968401
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class DummyDownloader:
        def __init__(self):
            self.screen_output = []
        def to_screen(self, message):
            self.screen_output.append(message)
    dummy_downloader = DummyDownloader()

    pp = MetadataFromTitlePP(dummy_downloader, '%(title)s - %(artist)s')

    info = {'title': 'Hello - World'}
    pp.run(info)
    assert info['title'] == 'Hello'
    assert info['artist'] == 'World'
    assert dummy_downloader.screen_output == [
        '[fromtitle] parsed title: Hello',
        '[fromtitle] parsed artist: World',
    ]

    info = {'title': 'Hello World'}
    pp.run(info)
    assert info['title']

# Generated at 2022-06-14 18:00:36.811072
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.downloader.common import FileDownloader
    from youtube_dl.YoutubeDL import YoutubeDL

    test_url = 'http://host.tld/path/to/video'
    test_title = 'Test - Title'
    test_attrs = {'title': 'Test', 'artist': 'Title'}
    # Test '%(title)s - %(artist)s' format
    test_format = '%(title)s - %(artist)s'
    fd = FileDownloader(YoutubeDL({}), {'usenetrc': False, 'username': None, 'password': None, 'videopassword': None})
    pp = MetadataFromTitlePP(fd, test_format)
    result = pp.run({'title': test_title, 'url': test_url})
   

# Generated at 2022-06-14 18:00:46.295097
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.downloader.common import FileDownloader
    from youtube_dl.YoutubeDL import YoutubeDL

    # Test with empty title attribute
    video = {'title': '', 'ext': 'mp4'}
    file_downloader = FileDownloader(YoutubeDL(), {}, {}, {}, {}, None)
    metadata_from_title_pp = MetadataFromTitlePP(file_downloader, '%(title)s')
    assert metadata_from_title_pp.run(video)[1] == {'title': '', 'ext': 'mp4'}

    # Test with non-empty title attribute and invalid titleformat
    video.update({'title': 'artist1 - track1'})
    metadata_from_title_pp = MetadataFromTitlePP(file_downloader, '%(artist)s')
   

# Generated at 2022-06-14 18:00:54.413525
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.compat import compat_str

    class DummyDownloader(object):
        def to_screen(self, msg):
            pass

    titleformat = compat_str('%(title)s - %(artist)s')
    info = {
        'title': 'foobar - the foo and the bar',
    }

    pp = MetadataFromTitlePP(DummyDownloader(), titleformat)

    expect_info = info.copy()
    expect_info.update({
        'title': 'foobar',
        'artist': 'the foo and the bar',
    })
    expect_result = ([], expect_info)

    actual_result = pp.run(info)

    assert actual_result == expect_result

# Generated at 2022-06-14 18:01:04.973808
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    from tempfile import NamedTemporaryFile
    from xml.etree import ElementTree
    downloader = YoutubeDL({})
    info = {}
    info['title'] = 'Hedningarna - Svedjebruk'
    fmt = '%(artist)s - %(title)s'
    pp = MetadataFromTitlePP(downloader, fmt)
    # run test
    info = pp.run(info)[1]
    # check results
    assert info['title'] == 'Svedjebruk'
    assert info['artist'] == 'Hedningarna'



# Generated at 2022-06-14 18:01:15.315700
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .youtube_dl.YoutubeDL import YoutubeDL
    from .youtube_dl.utils import DateRange

    ################
    # Dummy file

    class DummyFile(object):
        @staticmethod
        def read(*args, **kwargs):
            return b''

    ################
    # Dummy downloader
    class DummyDownloader(object):
        def __init__(self):
            self._progress_hooks = []

        def to_screen(self, *args, **kwargs):
            pass

        def add_progress_hook(self, hook):
            self._progress_hooks.append(hook)

    ################
    # Dummy info
    class DummyInfo(object):
        pass
    info = DummyInfo()

    #################
    d = DummyDownloader()

# Generated at 2022-06-14 18:01:20.740218
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import yt_dl.extractor.common as common
    from yt_dl.utils import DateRange

    dl = common.FileDownloader({})
    titleformat = '%(title)s - %(artist)s (%(id)s)'
    info = {
        'title': 'Title - Artist (Id)',
        'upload_date': DateRange('19990101')
    }
    expected = {
        'title': 'Title',
        'artist': 'Artist',
        'id': 'Id',
        'upload_date': DateRange('19990101')
    }
    pp = MetadataFromTitlePP(dl, titleformat)
    assert expected == pp.run(info)[1]

    # test optional attributes
    titleformat = '%(title)s - %(artist)s (%(id)s)'


# Generated at 2022-06-14 18:01:26.465033
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ytdl_server.server import Downloader
    pp = MetadataFromTitlePP(Downloader(), titleformat='%(title)s - %(artist)s')
    info = {'title': 'track title - artist name'}
    pp.run(info)
    assert info['title'] == 'track title'
    assert info['artist'] == 'artist name'

# Generated at 2022-06-14 18:01:34.546182
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from pytube import YouTube
    from pytube.compat import str, bytes
    from pytube.helpers import install_proxy
    from pytube.exceptions import VideoUnavailable

    # Install proxy globally
    install_proxy('11.11.11.11', '1234')

    # Construct a YouTube object and extract metadata
    video_url = 'https://www.youtube.com/watch?v=Ik-RsDGPI5Y'
    yt = YouTube(video_url)
    info1 = yt.get_videos()[0].__dict__

    # Construct a MetadataFromTitlePP object and parse the title
    # to extract the metadata
    format = "%(title)s [%(id)s] %(resolution)s [%(ext)s]"
    pp = MetadataFromTitlePP(yt, format)


# Generated at 2022-06-14 18:01:45.573367
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Create a fake downloader
    class FakeDownloader:
        def to_screen(self, text):
            print('to_screen:', text)

    downloader = FakeDownloader()

    # Create a titleformat and a MetadataFromTitlePP object
    titleformat = '%(artist)s - %(title)s'
    metadata_from_title_pp = MetadataFromTitlePP(downloader, titleformat)

    # Create info object
    info = {
        'title': 'artist-test - title-test',
    }

    # Call run method
    metadata_from_title_pp.run(info)

    assert info['artist'] == 'artist-test'
    assert info['title'] == 'title-test'



# Generated at 2022-06-14 18:01:53.815504
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    mftpp = MetadataFromTitlePP(None, '%(title)s - %(artist)s')

    info = {
        'title': 'Test - Artist',
        'uploader': '',
        'location': '',
        'age_limit': '',
        'formats': ''
    }

    new_info = mftpp.run(info)[1]

    assert new_info['title'] == 'Test'
    assert new_info['artist'] == 'Artist'



# Generated at 2022-06-14 18:02:01.683305
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl import YoutubeDL
    filename = 'test.mp3'
    titleformat = '%(title)s - %(artist)s'
    title = 'title - artist'
    # get_test_filename is a private member of YoutubeDL; it returns the paths to the files on the hard drive.
    get_test_filename = lambda fn: YoutubeDL.get_test_filename(fn)
    result = MetadataFromTitlePP(YoutubeDL({}), titleformat).run(
        {'title': title, '_filename': get_test_filename(filename)})
    infodict = result[1]
    assert infodict['title'] == 'title'
    assert infodict['artist'] == 'artist'

# Generated at 2022-06-14 18:02:09.285698
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .compat import compat_str
    from .downloader import FakeYDL
    from .extractor import get_info_extractor
    from .utils import sanitize_open

    youtube_ie = get_info_extractor('Youtube')
    youtube_ie.extract = lambda x: {'title': 'Test title'}
    youtube_ie.suitable = lambda x: True

    ydl = FakeYDL()
    ydl.add_info_extractor(youtube_ie)
    ydl.add_post_processor(MetadataFromTitlePP(
        ydl, '%(title)s [%(id)s]'))

    with open('test.%(ext)s', 'w') as f:
        f.write('test')

    ydl.download = lambda *a, **kw: sanitize_

# Generated at 2022-06-14 18:02:18.365744
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL

    class Opts:
        pass

    class Downloader:
        params = None
        to_screen_calls = []
        def to_screen(self, msg):
            self.to_screen_calls.append(msg)

    opts = Opts()
    opts.metadatafromtitle = '%(title)s - %(artist)s'
    downloader = Downloader()
    with YoutubeDL(downloader) as ydl:
        ydl.post_processors['metadatafromtitle'] = MetadataFromTitlePP(ydl, opts.metadatafromtitle)
        # Test parsing
        info = {
            'title': 'Some Title - Some Artist',
            'artist': None,
            'title1': 'Dont overwrite me!',
        }
        ydl

# Generated at 2022-06-14 18:02:24.085186
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ..YoutubeDL import YoutubeDL
    downloader = YoutubeDL(params={})
    pp = MetadataFromTitlePP(downloader, "%(artist)s - %(title)s")
    info = {}
    info['title'] = "Metallica - Enter Sandman"
    pp.run(info)
    assert info['artist'] == "Metallica"
    assert info['title'] == "Enter Sandman"


# Generated at 2022-06-14 18:02:34.174959
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    info = {
        'title': 'Luna - It\'s Only A Paper Moon',
        'ext': '3gp',
        'format': 'DVQ, 3gp, 360x240, small',
        'format_id': 'DVQ',
        'url': 'http://www.youtube.com/watch?v=qX-ZKFpHwns'
    }
    pp = MetadataFromTitlePP(None, '%(artist)s - %(song)s')
    info = pp.run(info)[1]

# Generated at 2022-06-14 18:02:43.271265
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():

    import tempfile
    import os
    from .downloader import YoutubeDL

    # create YouTubeDL object
    ydl = YoutubeDL(params={'quiet': True, 'simulate': True})

    # create temporary output file
    (output_fd, output_filename) = tempfile.mkstemp(prefix='test_', suffix='.mp4')
    os.close(output_fd)

    # download single video using temporary output file
    info = ydl.extract_info('https://www.youtube.com/watch?v=BaW_jenozKc', download=False)
    assert(info['title'] == 'Hachinohe JAPAN, Tsugaru-jamisen, 3 cats')
    extractor = MetadataFromTitlePP(ydl, '%(title)s')

# Generated at 2022-06-14 18:02:47.501390
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    pp = MetadataFromTitlePP(None, '%(title)s - %(artist)s')
    info = {'title': 'Violet Hill - Coldplay'}
    [], info_new = pp.run(info)
    assert info_new['title'] == 'Violet Hill - Coldplay'
    assert info_new['artist'] == 'Coldplay'


# Generated at 2022-06-14 18:02:58.708579
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ..__main__ import exe_ydl

    tester = MetadataFromTitlePP(exe_ydl, '%(title)s - %(artist)s')
    info = {'title': 'test-title - test-artist'}
    assert tester.run(info) == ([], {
        'title': 'test-title',
        'artist': 'test-artist',
    })

    tester = MetadataFromTitlePP(exe_ydl, '%(artist)s - %(title)s')
    info = {'title': 'test-title - test-artist'}
    assert tester.run(info) == ([], {
        'title': 'test-title',
        'artist': 'test-artist',
    })


# Generated at 2022-06-14 18:03:12.025506
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # setup
    import youtube_dl
    dl = youtube_dl.YoutubeDL({})
    pp = MetadataFromTitlePP(dl, '%(title)s - %(artist)s')
    info = {'title': 'foo - bar'}
    # run
    pp.run(info)
    # test
    assert info == {
        'title': 'foo',
        'artist': 'bar'
    }

    info = {'title': 'foo - bar - baz'}
    pp.run(info)
    assert info == {
        'title': 'foo',
        'artist': 'bar - baz'
    }

    info = {'title': 'foo - bar - baz - qux'}
    pp.run(info)

# Generated at 2022-06-14 18:03:24.469302
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    ydl = None
    ff = MetadataFromTitlePP(ydl, '%(title)s-%(artist)s')
    # Test video with format title - artist
    # Check if attribute title and artist are set
    assert ff.run({'id': '123', 'title': 'The Unit - Test Video', 'url': 'http://www.example.com/123'})[1]['title'] == 'The Unit'
    assert ff.run({'id': '123', 'title': 'The Unit - Test Video', 'url': 'http://www.example.com/123'})[1]['artist'] == 'Test Video'
    # Test video without format
    # Check if attribute title and artist are not set

# Generated at 2022-06-14 18:03:36.181463
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # TEST 1:
    #   Given titleformat: '%(title)s - %(artist)s'
    #   and title: 'Test - Title'
    #   when run is called,
    #   then title is returned as '%(title)s'
    #   and artist is returned as '%(artist)s'
    assert MetadataFromTitlePP_run_helper('%(title)s - %(artist)s',
                                          'Test - Title',
                                          {'title': 'Test',
                                           'artist': 'Title'})

    # TEST 2:
    #   Given titleformat: '%(artist)s - %(title)s'
    #   and title: 'Title - Test'
    #   when run is called,
    #   then title is returned as '%(title)s

# Generated at 2022-06-14 18:03:46.895295
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.postprocessor import FFmpegExtractAudioPP
    from youtube_dl.downloader.http import HttpFD
    from tempfile import NamedTemporaryFile

    # Set up a dummy downloader
    ydl = YoutubeDL({'outtmpl': '%(title)s.%(ext)s', 'postprocessors': [FFmpegExtractAudioPP()]})
    ydl.to_screen = lambda x: x

    # Test 1: Test the regex creation
    pp = MetadataFromTitlePP(ydl, '%(title)s - %(artist)s')

    regex = '(?P<title>.+)\ \-\ (?P<artist>.+)'
    assert regex == pp._titleregex

    # Test 2: Test the format parsing

# Generated at 2022-06-14 18:03:52.973731
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Arrange
    from youtube_dl import YoutubeDL
    downloader = YoutubeDL()
    pp = MetadataFromTitlePP(downloader, '%(title)s - %(artist)s')

    # Act
    info = pp.run({'title': 'Title'})[1]

    # Assert
    assert info['title'] == 'Title'
    assert info['artist'] == 'NA'


# Generated at 2022-06-14 18:04:03.992975
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import unittest
    class TestMetadataFromTitlePP_run(unittest.TestCase):
        def setUp(self):
            class MockDownloader():
                def to_screen(self, message):
                    self._to_screen_message = message
            self._downloader = MockDownloader()

        def tearDown(self):
            self._downloader = None

        def test_simple_title(self):
            title_format = '%(title)s'
            post_processor = MetadataFromTitlePP(self._downloader, title_format)

            title = 'Foo Title'
            info = { 'title': title }
            self.assertEqual(post_processor.run(info), ([], info))
            self.assertEqual(info, { 'title': title, 'title': title })
            self.assertE

# Generated at 2022-06-14 18:04:14.881716
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    """
    Test for cases that should pass.
    """
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.utils import std_headers
    from .extractor.common import InfoExtractor

    class TestIE(InfoExtractor):
        def report_video_info_webpage_download(self, video_id):
            return {
                'id': video_id,
                'title': '%(artist)s - %(song)s [%(genre)s]'
            }

    title_regex = (r'\(?(?P<genre>[^\]]+)\)?\ '
                   r'\[?(?P<song>.+?)\]?\ '
                   r'-\ '
                   r'(?P<artist>[^\[]+)')

# Generated at 2022-06-14 18:04:25.080579
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    """ Unit test for method run of class MetadataFromTitlePP """
    from youtube_dl.utils import DateRange
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.Downloader import Downloader
    from youtube_dl.PostProcessor import PostProcessor
    from youtube_dl.InfoExtractors import YoutubeIE
    ydl = YoutubeDL({})
    ydl.add_info_extractor(YoutubeIE())
    d = Downloader(ydl)
    p = MetadataFromTitlePP(d, '%(uploader)s - %(title)s')
    info = {
        'title': 'Meine Lieblingslieder - Compilation'
    }
    infos, result = p.run(info)
    assert result['uploader'] == 'Meine Lieblingslieder'

# Generated at 2022-06-14 18:04:33.859939
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ..YoutubeDL import YoutubeDL
    from ..compat import compat_str

    def verify_run(title, titleformat, expected_metadata):
        pp = MetadataFromTitlePP(YoutubeDL(), titleformat)
        _, info = pp.run({'title': title, '_filename': 'NA'})
        for attribute, value in expected_metadata.items():
            if info[attribute] != value:
                raise AssertionError(
                    'test_MetadataFromTitlePP_run failed - '
                    'got %s, expected %s for attribute %s of %s'
                    % (info[attribute], value, attribute, title))

    # with regex

# Generated at 2022-06-14 18:04:40.574811
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Test
    info = {'title': 'abc - def'}
    fmt = '%(foo)s - %(bar)s'
    # Expect
    expect_info = {'title': 'abc - def', 'foo': 'abc', 'bar': 'def'}

    # Run
    pp = MetadataFromTitlePP('', fmt)
    _, info_after = pp.run(info)
    assert info_after == expect_info

# Generated at 2022-06-14 18:04:56.660579
# Unit test for method run of class MetadataFromTitlePP

# Generated at 2022-06-14 18:05:05.951980
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    fmt = '%(title)s - %(artist)s'
    regex = r'(?P<title>.+)\ \-\ (?P<artist>.+)'
    pp = MetadataFromTitlePP(None, fmt)
    assert regex == pp._titleregex
    title = 'Test title, more words - Test artist, more words'
    info = {'title': title}
    pp.run(info)
    assert info['title'] == 'Test title, more words'
    assert info['artist'] == 'Test artist, more words'


if __name__ == '__main__':
    test_MetadataFromTitlePP_run()

# Generated at 2022-06-14 18:05:16.168473
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Test function is an example of how to use MetadataFromTitlePP
    # It uses class TestDownloader as downloader
    from .test import TestDownloader

    t = TestDownloader()
    f = MetadataFromTitlePP(t, "%(title)s by %(artist)s")

    # Test for no match
    info = {'title': 'some video title'}
    f.run(info)
    assert info == {'title': 'some video title'}

    # Test for match
    info = {'title': 'some video title by some artist'}
    f.run(info)
    assert info == {'title': 'some video title', 'artist': 'some artist'}

# Generated at 2022-06-14 18:05:22.364709
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Simulate a downloader, needed to call PostProcessor.__init__()
    class FakeYoutubeDL(object):
        def to_screen(self, s):
            print('>' + s)
    fake_downloader = FakeYoutubeDL()


# Generated at 2022-06-14 18:05:31.942268
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ..compat import compat_urllib_request

    downloader = compat_urllib_request.Request('')
    title = '"The title" - author'
    expect_result = {'title': 'The title', 'author': 'author', 'no': None}

    tmppp = MetadataFromTitlePP(downloader, '"%(title)s" - %(author)s')
    assert tmppp._titleformat == '"%(title)s" - %(author)s'
    assert tmppp._titleregex == r'"(?P<title>.+)"\ \-\ (?P<author>.+)'
    result = tmppp.run({'title': title})
    assert result[0] == []

# Generated at 2022-06-14 18:05:44.068967
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    fake_info = {'title': 'a song title - 2014 - with a bit of ID3 16/10'}
    assert MetadataFromTitlePP(None,
                     '%(title)s - %(year)s - %(id3)s').run(fake_info)[1] == {
                                         'title': 'a song title',
                                         'year': '2014',
                                         'id3': '16/10'}
    # test if format string does not match
    assert MetadataFromTitlePP(None, '%(title)s - %(no_match)s').run(
                                                            fake_info)[1] == {}
    # test if format string is not valid regex
    assert MetadataFromTitlePP(None, '%(').run(fake_info)[1] == {}


# Generated at 2022-06-14 18:05:51.013656
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ytdl.YoutubeDL import YoutubeDL
    from ytdl.PostProcessor import PostProcessor
    from ytdl.FileDownloader import FileDownloader
    from ytdl.compat import compat_os_name
    from ytdl.hook import YoutubeDLHook

    print('Test MetadataFromTitlePP - Run')

    # Initialize dummy downloader
    ydl = YoutubeDL({'writeinfojson': True})
    ydl.add_post_processor(MetadataFromTitlePP(ydl, '%(title)s'))

    # Create dummy video

# Generated at 2022-06-14 18:05:55.960540
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import unittest
    import youtube_dl.downloader
    import youtube_dl.utils
    class TestInfo(dict): pass
    class TestYDL(youtube_dl.downloader.FileDownloader):
        def __init__(self, info):
            self.my_info = info
            youtube_dl.downloader.FileDownloader.__init__(self, TestYDL.params)
        def to_screen(self, msg):
            TestYDL.to_screen_msg = msg
        def report_warning(self, msg):
            TestYDL.report_warning_msg = msg
        params = TestInfo({'cachedir': False, 'noplaylist': False})

    def test_run(self, title, titleformat, expected):
        self.my_info['title'] = title
        postprocessor = Metadata

# Generated at 2022-06-14 18:06:04.739565
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from __main__ import downloader
    from .extractor import YoutubeIE
    from .extractor.common import InfoExtractor

    InfoExtractor.download = lambda s, url: url
    downloader.params['simulate'] = True
    downloader.params['format'] = 'bestvideo+bestaudio'
    downloader.params['nooverwrites'] = True

    # test run with title format
    #   "%(uploader)s - %(title)s (%(id)s, %(upload_date)s)"
    #   at https://youtu.be/KHZ8ek-6ccc

# Generated at 2022-06-14 18:06:13.279782
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .youtube_dl.YoutubeDL import YoutubeDL
    ydl_opts = {
        'writethumbnail': True,
        'writeautomaticsub': True,
        'subtitleslangs': ['en'],
    }
    ydl = YoutubeDL(ydl_opts)

    pp = MetadataFromTitlePP(ydl, '%(uploader)s - %(title)s')
    info = {'title': 'Miranda Sings - Deck The Halls'}
    actual = pp.run(info)[1]
    expected = {'title': 'Deck The Halls', 'uploader': 'Miranda Sings'}
    assert actual == expected

    pp = MetadataFromTitlePP(ydl, '%(title)s - %(uploader)s')

# Generated at 2022-06-14 18:06:42.951269
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import Downloader

    # Downloader() requires an argument that is not None
    downloader = Downloader(params={})

    # Test 1
    info1 = {
        'title': 'Test Title - Test Artist'
    }
    titleformat1 = '%(title)s - %(artist)s'
    pp1 = MetadataFromTitlePP(downloader, titleformat1)
    assert pp1._titleregex == '(?P<title>.+)\\ \\-\\ (?P<artist>.+)'
    assert pp1.run(info1) == ([], {'title': 'Test Title', 'artist': 'Test Artist'})

    # Test 2
    info2 = {
        'title': 'Another Test Title - Another Test Artist'
    }

# Generated at 2022-06-14 18:06:51.268965
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Having a title format: '%(title)s - %(artist)s'
    titleformat = '%(title)s - %(artist)s'

    # And a youtube title: 'My title - My artist'
    youtube_title = 'My title - My artist'

    # When Post-Processing title
    metadata = MetadataFromTitlePP(None, titleformat).run({'title': youtube_title})

    # Then metadata should be equal to
    expected_metadata = {'title': 'My title', 'artist': 'My artist'}

    # And new title should be equal to
    expected_new_title = 'My artist - My title'

    assert metadata[1] == expected_metadata



# Generated at 2022-06-14 18:07:02.090127
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class D:
        def to_screen(self,*a,**ka):
            print(a[0]%a[1:])
        def to_stderr(self,*a,**ka):
            print(a[0]%a[1:])
    class I:pass
    d = D()
    i = I()
    i.title = 'title - artist'
    p = MetadataFromTitlePP(d, '%(title)s - %(artist)s')
    assert p.run(i) == ([],i)

if __name__ == '__main__':
    test_MetadataFromTitlePP_run()

# Generated at 2022-06-14 18:07:14.211004
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    metadata = {}
    metadata_format = '%(artist)s - %(title)s'
    metadata_regex = r'(?P<artist>.+)\ \-\ (?P<title>.+)'
    title = 'Cher - Believe (Official Music Video)'
    expected_artist = 'Cher'
    expected_title = 'Believe (Official Music Video)'
    args = []
    kwargs = {'downloader': '', 'titleformat': metadata_format}
    metadata_from_title_processor = MetadataFromTitlePP(*args, **kwargs)
    metadata_from_title_processor._titleformat = metadata_format
    metadata_from_title_processor._titleregex = metadata_regex

# Generated at 2022-06-14 18:07:20.975663
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import unittest

    import sys
    sys.modules['__main__'].YTDLSafeException = Exception
    from youtube_dl.YoutubeDL import YoutubeDL

    from .common import InfoExtractorMock

    ie = InfoExtractorMock({'title': 'valid title'})
    ydl = YoutubeDL({})
    ydl.add_info_extractor(ie)

    class DummyFileDownloader():
        def to_screen(self, *args, **kwargs):
            pass

    class DummyFFmpegPostProcessor():
        def __init__(self, *args, **kwargs):
            pass

        def run(self, info):
            pass

        @classmethod
        def available(cls):
            pass

        @classmethod
        def enabled(cls):
            return False

    ydl

# Generated at 2022-06-14 18:07:27.327460
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    downloader = MockYDL()
    pp = MetadataFromTitlePP(downloader, '%(title)s - %(artist)s')
    info = {'title':'test title - test artist - more stuff'}
    pp.run(info)
    assert info['title'] == 'test title - test artist - more stuff'
    assert info['artist'] == 'test artist'


# Generated at 2022-06-14 18:07:34.627849
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL

    class YoutubeDLMock(YoutubeDL):
        def __init__(self, *args, **kwargs):
            super(YoutubeDLMock, self).__init__(*args, **kwargs)
            self.to_screen_buffer = []

        def to_screen(self, msg):
            self.to_screen_buffer.append(msg)

        def pop_to_screen(self):
            return self.to_screen_buffer.pop()

    ydl = YoutubeDLMock({})
    ydl.add_post_processor(MetadataFromTitlePP(ydl,
                                                '%(title)s - %(artist)s'))
    info = {'title': 'Fade into Darkness - AVICII'}
    info_return, info_modified

# Generated at 2022-06-14 18:07:43.155853
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class InfoDict():
        def __init__(self):
            self.clear()

        def clear(self):
            self.__dict__.clear()
            self.__dict__['title'] = None

        def __contains__(self, key):
            return key in self.__dict__

        def __setitem__(self, key, value):
            self.__dict__[key] = value

        def __getitem__(self, key):
            return self.__dict__[key]

        def get(self, key, default=None):
            return self.__dict__[key] if key in self.__dict__ else default

    class MyLogger():
        def to_screen(self, msg):
            print(msg)


# Generated at 2022-06-14 18:07:45.602155
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    pass


# Generated at 2022-06-14 18:07:50.247304
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    assert(MetadataFromTitlePP(None, '%(title)s')._titleregex == '(?P<title>.+)')
    assert(MetadataFromTitlePP(None, '%(title)s - %(artist)s')._titleregex == '(?P<title>.+)\ \-\ (?P<artist>.+)')

# Generated at 2022-06-14 18:08:39.084236
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    r"""
    Make sure run function works properly
    """
    import unittest
    import unittest.mock
    from ydl.postprocessor.common import PostProcessingError

    class DummyYDL(object):
        def to_screen(self, *args, **kargs):
            pass

    class DummyIE(object):
        ie_key = 'dummy_ie'

    class DummyInfoDict(dict):
        pass

    DummyYDLObj = DummyYDL()
    DummyInfoDictObj = DummyInfoDict()
    DummyInfoDictObj['title'] = 'foo'