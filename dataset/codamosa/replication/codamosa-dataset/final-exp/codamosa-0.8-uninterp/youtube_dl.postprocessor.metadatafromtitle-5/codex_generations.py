

# Generated at 2022-06-14 17:58:36.036216
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    dl = type('Dummy', (object,), {'to_screen': print})()
    pp = MetadataFromTitlePP(dl, r'%(author)s\ -\ %(title)s')
    info = {
        'title': r'Author - Title - More title',
        'upload_date': r'20120101',
    }
    pp.run(info)
    assert info == {
        'title': r'Title - More title',
        'upload_date': r'20120101',
        'author': r'Author',
    }


# Generated at 2022-06-14 17:58:44.467286
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    """ Unit test for run method of class MetadataFromTitlePP """
    # Create instance of downloader and MetadataFromTitlePP
    params = {'verbose': False, 'simulate': True, 'playliststart': 1,
              'playlistend': 2, 'outtmpl': '%(id)s'}
    downloader = YouTubeDL(params)
    metadata_from_title = MetadataFromTitlePP(downloader, '%(title)s')

    # Test run method
    info = {'title': 'test title', 'id': 'video-id'}
    result = metadata_from_title.run(info)
    assert(result == ([], {'title': 'test title', 'id': 'video-id'}))
    # Other parameters than title should be passed unchanged

# Generated at 2022-06-14 17:58:56.910848
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():

    # Importing module
    import youtube_dl
    import sys
    import re

    # Creating a mock class
    class MockYoutubeDL(object):
        @staticmethod
        def to_screen(string):
            pass

    # Creating a mock class
    class MockInfo(object):

        def __init__(self, title):
            self.title = title

        def __getitem__(self, key):
            return self.__dict__[key]

        def __setitem__(self, key, value):
            self.__dict__[key] = value

    # Testing
    # format: %(title)s - %(artist)s - %(year)s
    # title:  Example Title - Example Artist - 2019
    # metadata:
    #   title:  Example Title
    #   artist: Example Artist
    #

# Generated at 2022-06-14 17:59:06.653031
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys

    class MockInfoDict():
        def __init__(self):
            self.infodict = {}

        def __getitem__(self, key):
            return self.infodict[key]

        def __setitem__(self, key, value):
            self.infodict[key] = value

    class MockDownloader():
        def to_screen(self, str):
            print(str)

    downloader = MockDownloader()
    info = MockInfoDict()
    info.infodict = {
        'title': 'A - B - C - D - E'
    }

    pp = MetadataFromTitlePP(downloader, '%(a)s - %(b)s - %(c)s - %(d)s - %(e)s')
    info, new_info

# Generated at 2022-06-14 17:59:14.146118
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    import unittest
    import YTDLS.extractor.common

    class MockYTDLS(YTDLS.YTDLS):
        def __init__(self):
            self.cache = dict()

    def _print_result(title, info):
        print(title)
        for key, value in info.items():
            if value is None:
                print('  %s: NA' % key)
            else:
                print('  %s: %s' % (key, value))
        print()

    class TestPP(unittest.TestCase):
        def setUp(self):
            self.downloader = MockYTDLS()

        def run_test(self, titleformat, title, info):
            pp = MetadataFromTitlePP(self.downloader, titleformat)
            _, new

# Generated at 2022-06-14 17:59:24.547296
# Unit test for method run of class MetadataFromTitlePP

# Generated at 2022-06-14 17:59:35.584963
# Unit test for method run of class MetadataFromTitlePP

# Generated at 2022-06-14 17:59:46.131399
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from sys import stderr
    from types import GeneratorType
    
    from .compat import compat_str
    from .downloader import Downloader
    from .extractor import Gen_Extractor, SearchInfoExtractor, YoutubeIE
    
    print('Unit Test for Method run of Class MetadataFromTitlePP', file=stderr)
    
    def genExtractor(downloader, ie_result):
        def lazy_extract_info(url):
            return ie_result
        def lazy_search(query, count=None):
            return
        gen_extractor = Gen_Extractor(downloader)
        gen_extractor.extract_info = lambda url: lazy_extract_info(url)
        gen_extractor.search = lambda query, count=None: lazy_search(query, count)
        return gen_extractor

# Generated at 2022-06-14 17:59:53.470425
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .test import _downloader

    def check_res(downloader, info, res, titleformat):
        assert isinstance(res, (list, tuple))
        assert len(res) == 2
        assert isinstance(res[0], list)
        assert isinstance(res[1], dict)
        assert ('title' in res[1]) and ('artist' in res[1]), (
               'Missing title or artist')
        assert res[1]['title'] == 'some title' and res[1]['artist'] == 'some artist', (
               'Title or artist were not parsed from title')

    info = {'title': 'some title - some artist'}
    downloader = _downloader({})
    pp = MetadataFromTitlePP(downloader, '%(title)s - %(artist)s')

# Generated at 2022-06-14 18:00:02.672213
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ydl.postprocessor.ffmpeg import FFmpegMetadataPP
    from ydl.downloader.youtube import YoutubeDL

    # set up objects
    opts = {'writethumbnail': True, 'writesubtitles': True, 'writeautomaticsub': True}
    ydl = YoutubeDL(opts)
    mp = MetadataFromTitlePP(ydl, '%(title)s')
    ff = FFmpegMetadataPP(ydl)

    # test that it works
    info = {'title': 'Test Title [Foo] - Artist Name'}
    # info['title'] = 'Test Title [Foo] - Artist Name'
    (info, tmpfilename) = mp.run(info)
    assert info['title'] == 'Test Title'
    assert info['artist'] == 'Artist Name'
    # info

# Generated at 2022-06-14 18:00:16.185996
# Unit test for method format_to_regex of class MetadataFromTitlePP
def test_MetadataFromTitlePP_format_to_regex():
    pp = MetadataFromTitlePP(None, None)
    assert pp.format_to_regex(r'%(title)s - %(artist)s') == \
           r'(?P<title>.+)\ \-\ (?P<artist>.+)'
    assert pp.format_to_regex(r'%(artist)s - %(title)s') == \
           r'(?P<artist>.+)\ \-\ (?P<title>.+)'
    assert pp.format_to_regex(r'S%(episode_number)02dE%(season_number)02d') == \
           r'S(?P<episode_number>.+)E(?P<season_number>.+)'

# Generated at 2022-06-14 18:00:26.861866
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class TestDownloader(object):
        @staticmethod
        def to_screen(msg):
            raise msg

    class TestInfo(object):
        def __init__(self, title):
            self['title'] = title

        def __setitem__(self, key, value):
            self.__dict__[key] = value

    title_fmt = '%(title)s - %(artist)s'
    info1 = TestInfo('The Title - The Artist')
    info2 = TestInfo('Not matching the format')

    testee = MetadataFromTitlePP(TestDownloader, title_fmt)

    try:
        testee.run(info1)
        success = True
    except Exception:
        success = False
    if not success:
        raise RuntimeError('Should not have thrown exception')


# Generated at 2022-06-14 18:00:35.721062
# Unit test for method format_to_regex of class MetadataFromTitlePP
def test_MetadataFromTitlePP_format_to_regex():
    metadata = MetadataFromTitlePP(None, None)
    assert metadata.format_to_regex('%(title)s') == '(?P<title>.+)'
    assert metadata.format_to_regex('%(title)s - %(artist)s') == '(?P<title>.+)\ \-\ (?P<artist>.+)'
    assert metadata.format_to_regex('%(title)s - %% - %(artist)s') == '(?P<title>.+)\ \-\ \%\ \-\ (?P<artist>.+)'
    assert metadata.format_to_regex('%(title)s%%') == '(?P<title>.+)%'
    assert metadata.format_to_regex('%%(title)s') == '%(title).+'
    assert metadata.format_to

# Generated at 2022-06-14 18:00:45.916991
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Test basic case
    p = MetadataFromTitlePP(None, '%(title)s - %(artist)s')
    info = {'title': 'Video Title - Artist Name'}
    [], info = p.run(info)
    assert info['title'] == 'Video Title'
    assert info['artist'] == 'Artist Name'

    # Test case when regex doesn't match
    p = MetadataFromTitlePP(None, '%(artist)s - %(title)s')
    info = {'title': 'Video Title - Artist Name'}
    [], info = p.run(info)
    assert info['title'] == 'Video Title - Artist Name'
    assert 'artist' not in info

    # Test case when info is empty

# Generated at 2022-06-14 18:00:54.911416
# Unit test for method format_to_regex of class MetadataFromTitlePP
def test_MetadataFromTitlePP_format_to_regex():
    assert ('(?P<video_id>.+)\ \-\ (?P<uploader>.+)'
            == MetadataFromTitlePP(None, '%(video_id)s - %(uploader)s').format_to_regex(
                '%(video_id)s - %(uploader)s'))
    assert ('(?P<video_id>.+)'
            == MetadataFromTitlePP(None, '%(video_id)s').format_to_regex(
                '%(video_id)s'))

# Generated at 2022-06-14 18:01:07.540061
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.utils import DownloadReturnCode
    from .testutils import FakeYDL

    def _test_run(titleformat, title, expected_dict, expected_code=DownloadReturnCode.SUCCESS):
        ydl = YoutubeDL(params={'writedescription': True})
        ydl = FakeYDL({
            'info_dict': {
                'title': title,
                'description': title,
            }
        }, ydl)
        pp = MetadataFromTitlePP(ydl, titleformat)
        _, _ = pp.run({})
        return ydl.infos[0]['entries'][0]['info_dict'], ydl.return_code


# Generated at 2022-06-14 18:01:19.402750
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import copy

    class InfoContainer:
        def __init__(self, info):
            self.original = copy.copy(info)
            self.info = info

    info = {
        'title': "L'empereur Napoléon en 1815 - Épisode 1: La campagne de France",
        'alt_title': "Napoleon in 1815 - Episode 1: The French Campaign",
        'artist': 'Arnaud Sélignac',
        'year': 2016,
        'season': 1,
        'episode': 1,
    }

    info_c = InfoContainer(info)

    def to_screen(s):
        print(s)

    titleformat = "%(title)s"
    pp = MetadataFromTitlePP(None, titleformat)
    pp.run(info_c.info)

# Generated at 2022-06-14 18:01:31.660496
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.YoutubeDLHandler import YoutubeDLHandler
    from youtube_dl.PostProcessor import PostProcessor

    ydl = YoutubeDL({})
    ydl.add_post_processor(MetadataFromTitlePP(ydl, '%(title)s - %(artist)s'))

    class FakeInfoDict(object):
        def __init__(self, title):
            self.title = title
            self.myattribute = None

        def __getitem__(self, key):
            return getattr(self, key)

        def __setitem__(self, key, value):
            setattr(self, key, value)

    # Case 1: title equals titleformat
    info = FakeInfoDict('QQQ - AAA')
    ydl.process_

# Generated at 2022-06-14 18:01:39.170410
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    f = MetadataFromTitlePP(None, '%(track)s-%(artist)s-%(title)s')
    assert f.run({
        'title': 'bla',
    }) == ([], {})

    f = MetadataFromTitlePP(None, '%(track)s-%(artist)s-%(title)s')
    assert f.run({
        'title': '1-me-title',
    }) == ([], {
        'track': '1',
        'artist': 'me',
        'title': 'title',
    })

    f = MetadataFromTitlePP(None, '%(track)s-%(artist)s-%(title)s')

# Generated at 2022-06-14 18:01:47.356227
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import ydl_opts
    import ydl_process

    opts = {
        'metadatafromtitle': '%(title)s - %(artist)s'
    }
    ydl = ydl_process.YDLProcessor(ydl_opts.parseOpts(opts))
    pp = MetadataFromTitlePP(ydl, opts['metadatafromtitle'])

    info = dict()
    info['title'] = 'my title - my artist'
    pp.run(info)
    correct_result = dict()
    correct_result['title'] = 'my title'
    correct_result['artist'] = 'my artist'
    assert info == correct_result, "unexpected result for %s" % info['title']

    info = dict()
    info['title'] = 'my title - my artist - my album'

# Generated at 2022-06-14 18:02:00.243977
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.downloader.http import HttpFD
    from youtube_dl.YoutubeDL import YoutubeDL

    class DummyYoutubeDL(YoutubeDL):
        def __init__(self, params):
            super(DummyYoutubeDL, self).__init__(params)

        def to_screen(self, s):
            print(s)

        def process_ie_result(self, ie_result, downloaded=False,
            extra_info={}):
            res = PostProcessor(self).run(ie_result)

    out_dict = {}

    # Test with a title not matching the regex
    title = 'foobar123'
    titleregex = r'(?P<title>\w+)(?P<number>\d+)'

# Generated at 2022-06-14 18:02:08.812736
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import io
    from .extractor import get_info_extractor, YoutubeIE
    from .compat import compat_urllib_request

    # Mock objects
    fake_downloader = object()
    fake_downloader.to_screen = print

    # Loading data
    fake_http_server = io.BytesIO()
    fake_http_server.write(compat_urllib_request.urlopen(
        'https://gist.githubusercontent.com/drorata/d59064fbd0cf0c8a9f9c/raw/a0f2a554a0b72b7c256dd6f5df5f5e4967cd9f53/test_title_metadata.txt'
    ).read())
    fake_http_server.seek(0)

    # Running test

# Generated at 2022-06-14 18:02:19.166410
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .extractor import YoutubeIE
    t1 = '%(artist)s - %(title)s'
    pp1 = MetadataFromTitlePP(None, t1)
    assert pp1._titleregex == '(?P<artist>.+)\ \-\ (?P<title>.+)'

    t2 = '%(artist)s - %(title)s [%(id)s]'
    pp2 = MetadataFromTitlePP(None, t2)
    assert pp2._titleregex == '(?P<artist>.+)\ \-\ (?P<title>.+)\ \[(?P<id>.+)\]'
    d = {'_type': 'url', 'url': 'https://www.youtube.com/watch?v=WKsjaOqDXgg', 'ie_key': 'Youtube'}


# Generated at 2022-06-14 18:02:31.582154
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FileDownloader
    ydl = FileDownloader({})
    pp = MetadataFromTitlePP(ydl, '%(artist)s - %(title)s')
    assert pp.run({'title': 'Elton John - Your Song'}) == ([], {'title': 'Elton John - Your Song', 'artist': 'Elton John'})
    pp = MetadataFromTitlePP(ydl, '%(artist)s - %(title)s')
    assert pp.run({'title': 'Elton John - Your Song - (Official Video)'}) == ([], {'title': 'Elton John - Your Song - (Official Video)', 'artist': 'Elton John'})
    pp = MetadataFromTitlePP(ydl, '%(track_number)02.d - %(title)s')
    assert pp

# Generated at 2022-06-14 18:02:43.238416
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    titleformat = '%(artist)s - %(track)s - %(title)s'
    titleregex = (r'(?P<artist>.+)\ \-\ (?P<track>.+)\ \-\ (?P<title>.+)')

    expected_info = {
        'artist': 'Artist',
        'track': 'Track',
        'title': 'Title',
    }

    class DummyDownloader:
        def __init__(self):
            self.to_screen_log = []

        def to_screen(self, text):
            self.to_screen_log.append(text)

    import youtube_dl.extractor
    downloader = DummyDownloader()
    p = MetadataFromTitlePP(downloader, titleformat)
    title = 'Artist - Track - Title'

# Generated at 2022-06-14 18:02:49.678968
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import Downloader
    from .extractor import InfoExtractor
    from .compat import compat_basestring

    class YoutubeIE(InfoExtractor):
        def __init__(self, downloader=None, ie=None, ie_key=None, **kwargs):
            super(YoutubeIE, self).__init__(downloader, ie, ie_key, **kwargs)

        def _real_extract(self, url):
            return {'title': 'Lunar Phase - A Lunar Eclipse Explained',
                    'id': '58722f98d6d87'}

    # Create the downloader object used by MetadataFromTitlePP
    downloader = Downloader()
    downloader.add_info_extractor(YoutubeIE)

    # Create a MetadataFromTitlePP object and test its run method
   

# Generated at 2022-06-14 18:02:58.152712
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from . import YoutubeDL
    ydl = YoutubeDL(dict())
    pp = MetadataFromTitlePP(ydl, '%(artist)s - %(track)s')
    info = {'title': 'Jimmy Barnes - Too Much Ain\'t Enough Love'}
    assert pp.run(info) == ([], {'artist': 'Jimmy Barnes',
                                 'track': 'Too Much Ain\'t Enough Love',
                                 'title': 'Jimmy Barnes - Too Much Ain\'t Enough Love'})



# Generated at 2022-06-14 18:03:07.032120
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import YoutubeDL
    from .compat import compat_str
    from .extractor import YoutubeIE

    class MockInfoExtractor:
        def __init__(self, ie_name):
            self._ie_name = ie_name

    class MockDownloader:
        def __init__(self):
            self.to_screen_messages = []

        def to_screen(self, msg):
            self.to_screen_messages.append(msg)

    def test_ie(test_self, ie_name):
        return MockInfoExtractor(ie_name)

    def test_format_to_regex_specialchars():
        test_self = MetadataFromTitlePP(MockDownloader(), '%(title)s - %(artist)s')

# Generated at 2022-06-14 18:03:16.303550
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import pytube
    test_yt = pytube.YouTube(r'https://www.youtube.com/watch?v=VLf-MT1ujLA')
    test_video = test_yt.get('mp4', '360p')
    test_pp = MetadataFromTitlePP(test_yt, r'%(title)s')
    test_info = test_video.__dict__
    empty_result, metadata = test_pp.run(test_info)
    assert metadata['title'] == 'Toad\'s Wild Ride'
    assert test_info['title'] != metadata['title']


# Generated at 2022-06-14 18:03:26.706245
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    import unittest
    class MockYDL:
        def to_screen(*args):
            pass
    ydl = MockYDL()

    class MockInfo:
        def __init__(self, *args, **kwargs):
            self.__dict__.update(*args, **kwargs)
    ydl.to_screen = lambda *args: sys.stderr.write(args[0]+'\n')

    def testMetadataFromTitlePP(titleformat, title, exp_info):
        sys.stderr.write('titleformat: '+titleformat+'\n')
        sys.stderr.write('title: '+title+'\n')
        sys.stderr.write('exp_info: '+str(exp_info)+'\n')

# Generated at 2022-06-14 18:03:40.203846
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    from .compat import compat_urlparse

    from .common import FileDownloader
    from .extractor import get_info_extractor
    from .utils import encodeArgument

    from .compat import compat_struct_unpack

    class FakeYDL(FileDownloader):
        def __init__(self):
            FileDownloader.__init__(self, {})
            self.to_screen = sys.stderr.write

# Generated at 2022-06-14 18:03:47.022946
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class DummyDownloader:
        def to_screen(self, text):
            pass
    ydl = DummyDownloader()
    pp = MetadataFromTitlePP(ydl, '%(artist)s - %(title)s')
    info = {'id': 'a1b2c3', 'title': 'artist - title'}
    pp.run(info)
    assert info['artist'] == 'artist'
    assert info['title'] == 'title'
    assert not pp.format_to_regex('eas%(artist)s - %(title)sy') is None

# Generated at 2022-06-14 18:03:58.213701
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FileDownloader
    from .extractor import gen_extractors
    import sys

    instrumented_extractors = {}
    for ie in gen_extractors():
        instrumented_extractors[ie.IE_NAME] = ie
        ie.old_suitable = ie.suitable
        def new_suitable(self, *args, **kargs):
            if self.IE_NAME == 'Youtube':
                return False
            return self.old_suitable(*args, **kargs)
        ie.suitable = new_suitable.__get__(ie, ie.__class__)
        ie.old_real_initialize = ie.real_initialize
        def new_real_initialize(self, *args, **kargs):
            # Just to prevent any real download
            self._download

# Generated at 2022-06-14 18:04:09.964653
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ytdl.YoutubeDL import YoutubeDL
    ydl = YoutubeDL({})
    mdftpp = MetadataFromTitlePP(ydl, '%(artist)s - %(title)s')
    info = {
        'title': 'Hello',
        'artist': 'World',
    }
    mdftpp.run(info)
    assert info == {
        'title': 'Hello',
        'artist': 'World',
    }
    info = {
        'title': 'Hello - World',
    }
    mdftpp.run(info)
    assert info == {
        'title': 'Hello - World',
        'artist': 'World',
    }
    info = {
        'title': 'Hello - World - Test',
    }
    mdftpp.run(info)

# Generated at 2022-06-14 18:04:20.837349
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    import mock
    import unittest

    sys.modules['pytube'] = mock.Mock()
    sys.modules['pytube.extractor'] = mock.Mock()
    sys.modules['pytube.extractor.common'] = mock.Mock()
    sys.modules['pytube.extractor.youtube'] = mock.Mock()
    sys.modules['pytube.extractor.youtube_dl'] = mock.Mock()

    from pytube.postprocessor import metadatafromtitle

    class MockDownloader(object):
        def to_screen(self, msg):
            print(msg)

    title_format = '%(title)s - %(artist)s'

# Generated at 2022-06-14 18:04:21.620618
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    pass

# Generated at 2022-06-14 18:04:28.958420
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    downloader = MockYDL()
    pp = MetadataFromTitlePP(downloader, '%(title)s - %(artist)s - %(album)s')
    info = {'title': 'some title',
            'artist': 'some artist',
            'album': 'some album'}
    info = pp.run(info)[1]
    assert info['title'] == 'some title'
    assert info['artist'] == 'some artist'
    assert info['album'] == 'some album'


# Generated at 2022-06-14 18:04:35.611423
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import YoutubeDL
    from .postprocessor import PostProcessor
    ydl = YoutubeDL({})
    pp = PostProcessor(ydl, {})
    postprocessor = MetadataFromTitlePP(ydl, '%(title)s')
    result = [], {'title': 'test title'}
    assert postprocessor.run(result[1]) == result
    postprocessor = MetadataFromTitlePP(ydl, '%(title)s %(test)s')
    result = [], {'title': 'test title'}
    assert postprocessor.run(result[1]) == result
    postprocessor = MetadataFromTitlePP(ydl, '%(title)s - %(test)s')
    result = [], {'title': 'test title'}

# Generated at 2022-06-14 18:04:46.821899
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    import time
    import os.path
    import tempfile
    import pytest
    import shutil

    # set up initial constants
    exit_code = 0
    info = {'title': 'hello world'}
    save_stdout = sys.stdout

    # patch sys.stdout so that we can capture the output
    sys.stdout = open(os.path.devnull, 'w')

    # create downloader and postprocessor
    class MockDownloader:
        def __init__(self):
            self.to_screen = lambda x: sys.stdout.write(x+'\n')
    class MockToScreen:
        def __init__(self):
            self.messages = []
        def __call__(self, message):
            self.messages.append(message)
    downloader

# Generated at 2022-06-14 18:04:55.399975
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():

    class TestDownloader():
        def to_screen(self, message):
            print(message)

    pp = MetadataFromTitlePP(TestDownloader(), '%(artist)s - %(title)s')

    expected_info = {
        'title': 'Test MetadataFromTitlePP'
    }

    assert pp.run(expected_info)[1] == {
        'title': 'Test MetadataFromTitlePP'
    }

    expected_info = {
        'title': 'MetadataFromTitlePP - Test'
    }

    assert pp.run(expected_info)[1] == {
        'artist': 'MetadataFromTitlePP',
        'title': 'Test'
    }



# Generated at 2022-06-14 18:05:10.686920
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class FakeInfoDict:
        def __init__(self):
            self.update = self.__setitem__

        def __setitem__(self, key, value):
            self.__dict__[key] = value

    class FakeYdl:
        def __init__(self):
            self.to_screen = print

    import unittest

    class TestRun(unittest.TestCase):

        def test_basic(self):
            info = FakeInfoDict()
            info.update({"title": "Foo Bar - Sample Video"})
            postprocessor = MetadataFromTitlePP(FakeYdl(), "%(title)s - %(artist)s")
            postprocessor.run(info)
            self.assertEqual(info.title, "Foo Bar")

# Generated at 2022-06-14 18:05:21.447871
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    _tests = (
        ('%(title)s - %(artist)s', 'hello world - abc',
            {'title': 'hello world', 'artist': 'abc'}),
        ('(?P<title>.*) - (?P<artist>.*)', 'hello world - abc',
            {'title': 'hello world', 'artist': 'abc'}),
        ('%(title)s - %(artist)s and %(artist)s', 'hello world - abc and abc',
            {'title': 'hello world', 'artist': 'abc and abc'}),
        ('%(title)s - %(artist)s', '%(title)s - %(artist)s',
            {'title': '%(title)s - %(artist)s', 'artist': None}),
    )

# Generated at 2022-06-14 18:05:31.530254
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Assumes that %(title)s is required by the MetadataFromTitlePP class
    test_cases = [
        ('{}', '', {}),
        ('%(title)s', 'test', {'title' : 'test'}),
        ('%(artist)s - %(title)s', 'test - it', {'artist' : 'test', 'title': 'it'}),
        ('%(artist)s - %(title)s', 'test', {}),
        ]

    class MockDownloader:
        def __init__(self):
            self.to_screen_output = []

        def to_screen(self, output):
            self.to_screen_output.append(output)


# Generated at 2022-06-14 18:05:42.606427
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Instantiate MetadataFromTitlePP object with input
    #   titleformat = '%(artist)s - %(title)s'
    copy_titlePP = MetadataFromTitlePP(None, "%(artist)s - %(title)s")
    # Input and expected output
    input_info = {'title': 'Metallica - Nothing Else Matters'}
    expected_output_info = {
        'title': 'Metallica - Nothing Else Matters',
        'artist': 'Metallica',
        'title': 'Nothing Else Matters'}
    expected_return_info = ([], expected_output_info)
    # Perform methods run and check output
    assert copy_titlePP.run(input_info) == expected_return_info

# Generated at 2022-06-14 18:05:51.656661
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import pytest

    # Test data
    expected_title_info = dict(artist='Echosmith', title='Cool Kids - Official Video',
                               album='Talking Dreams (Deluxe Version)', duration='307',
                               genre='Pop', explicit='false', disc_number='1',
                               track_number='6')
    expected_failed_title_info = dict(title='Unknown title', duration='-1')
    expected_failed_title_regex_info = dict(title='Unknown title', duration='-1')

    # Success: Test the case that title of video is a valid string for parsing.
    title_info = dict(title='Echosmith - Cool Kids - Official Video')
    info = dict()
    pp = MetadataFromTitlePP(None, '%(artist)s - %(title)s')
    result,

# Generated at 2022-06-14 18:06:02.713864
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import pytube
    tester01 = MetadataFromTitlePP(pytube.YoutubeDL({"quiet":True}), "%(artist)s - %(title)s")
    assert(tester01._titleregex == '(?P<artist>.+)\ \-\ (?P<title>.+)')
    res, _ = tester01.run({'title': 'Michael Jackson - Billy Jean'})
    assert(res == [])
    assert(_ == {'artist': 'Michael Jackson', 'title': 'Billy Jean'})
    res, _ = tester01.run({'title': 'Michael Jackson - Billy Jean', 'autonumber': '2'})
    assert(res == [])
    assert(_ == {'artist': 'Michael Jackson', 'title': 'Billy Jean', 'autonumber': '2'})
    res, _ = t

# Generated at 2022-06-14 18:06:08.293493
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    dl = None
    pp = MetadataFromTitlePP(dl, '%(artist)s - %(title)s')

    info = {
        'title': 'Crazy - Gnarls Barkley'
    }

    assert pp.run(info) == ([], {
        'title': 'Crazy - Gnarls Barkley',
        'artist': 'Gnarls Barkley',
    })



# Generated at 2022-06-14 18:06:12.110946
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class FakeInfoDict():
        def __init__(self, title):
            self.title = title
        def __setitem__(self, k, v):
            self.__dict__[k] = v
    class FakeYoutubeDl():
        def to_screen(self, msg):
            print(msg)

    titleformat = '%(title)s - %(artist)s'
    title = 'How To Basic - How To Eat Cereal'

    pp = MetadataFromTitlePP(FakeYoutubeDl(), titleformat)
    pp.run(FakeInfoDict(title))

# Generated at 2022-06-14 18:06:20.762472
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.downloader import YoutubeDL
    class FakeDict(dict):
        def __getitem__(self, key):
            return 'foo'
    ydl = YoutubeDL({'writethumbnail': True, 'skip_download': True})
    pp = MetadataFromTitlePP(ydl, '%(title)s - %(artist)s')
    info = FakeDict()
    assert pp.run(info) == ([], info)
    assert info['title'] is 'foo'
    assert info['artist'] is 'foo'


# Generated at 2022-06-14 18:06:30.622751
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import unittest
    class MockYoutubeDL():
        def to_screen(self, s):
            pass
    downloader = MockYoutubeDL()

    info = {'title':'Lloyd - Dedication To My Ex (Miss That) ft. Andre 3000, Lil Wayne'}
    pp = MetadataFromTitlePP(downloader, '%(artist)s - %(song)s (%(featuring)s)')
    pp.run(info)
    assert info == {'title': 'Lloyd - Dedication To My Ex (Miss That) ft. Andre 3000, Lil Wayne',
                    'artist': 'Lloyd',
                    'song': 'Dedication To My Ex (Miss That)',
                    'featuring': 'Andre 3000, Lil Wayne'}

    info = {'title':'Me - Myself - I'}


# Generated at 2022-06-14 18:06:51.830084
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.downloader import VideoInfo, Downloader
    from youtube_dl.utils import format_bytes
    from youtube_dl.extractor import YoutubeIE
    from collections import defaultdict
    from io import BytesIO

    # Initialize downloader
    ie = YoutubeIE()
    ie.extract_info(ie._real_initialize(), '7Z1Syi2uWvg') # Extract info from a realistic example
    info = ie.url_result('7Z1Syi2uWvg')
    video = VideoInfo(ie.extractor.name, info, 'Taken from description')
    video['title'] = '%(title)s by %(uploader)s - %(duration)s duration'
    video['id'] = '7Z1Syi2uWvg'

    # Initialize postprocessor
    pp

# Generated at 2022-06-14 18:07:03.465912
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Input
    import YoutubeDL
    downloader = YoutubeDL.YoutubeDL({'writethumbnail': True, 'writeinfojson': True, 'writedescription': True, 'simulate': True})
    postprocessor = MetadataFromTitlePP(downloader, '%(artist)s - %(title)s - %(creator)s - %(id)s')
    info = {'title': '\\Test - Title - Creator - XYZ'}
    # Expected output
    exp_info = {'title': '\\Test - Title - Creator - XYZ', 'artist': '\\Test', 'creator': 'Creator', 'id': 'XYZ'}

    # Run test
    res = postprocessor.run(info)

    # Check results
    assert(res[1] == exp_info)


# Generated at 2022-06-14 18:07:11.420017
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    metadata = {'title': 'name - artist', 'format': 'webm'}
    post_processor_instance = MetadataFromTitlePP(None, '%(title)s')
    assert post_processor_instance.format_to_regex('%(title)s') == '(?P<title>.+)'
    info_dicts = post_processor_instance.run(metadata)
    assert len(info_dicts) == 0
    assert metadata['title'] == 'name - artist'

# Generated at 2022-06-14 18:07:21.477109
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    def _check_entries(entries, info, expected_entries, expected_info):
        assert expected_entries == entries
        assert expected_info == info

    class _DummyYoutubeDL(object):
        def __init__(self):
            self.to_screen_called = False
            self.to_screen_args = ()

        def to_screen(self, msg):
            self.to_screen_called = True
            self.to_screen_args = msg

    #
    # Test1
    #
    dummy_YoutubeDL = _DummyYoutubeDL()
    process_title_from_metadata = MetadataFromTitlePP(
        dummy_YoutubeDL,
        '%(title)s - %(artist)s - %(year)s')

    # input value

# Generated at 2022-06-14 18:07:32.055368
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import pytest

    # Simple test
    info = {'id': 'abcdef-0123', 'title': 'Song by Artist'}
    titleformat = '%(title)s by %(artist)s'
    titleregex = '(?P<title>.+) by (?P<artist>.+)'
    pp = MetadataFromTitlePP(None, titleformat)
    assert pp._titleformat == titleformat
    assert pp._titleregex == titleregex
    result = pp.run(info)
    assert info['artist'] == 'Artist'
    assert info['title'] == 'Song'
    assert result == ([], info)

    # Test regex, regexmatch and error
    info = {'id': 'abcdef-0123', 'title': 'Song by Artist'}

# Generated at 2022-06-14 18:07:40.900375
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FileDownloader
    from .extractor.youtube import YoutubeIE
    downloader = FileDownloader({'outtmpl': '%(id)s'})
    youtubeIE = YoutubeIE(downloader)
    info = {
        'id': 'videoId',
        'title': 'My video - me@domain.com',
        'extractor': 'youtube'
    }
    titleformat = '%(title)s - %(creator)s'
    downloader.add_info_extractor(youtubeIE)
    pp = MetadataFromTitlePP(downloader, titleformat)
    pp.run(info)
    attribute = 'creator'
    assert info[attribute] == 'me@domain.com'
    assert info['title'] == 'My video'
    attribute = 'title'

# Generated at 2022-06-14 18:07:47.635795
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import YoutubeDL
    from .extractor import YoutubeIE
    ie1 = YoutubeIE(YoutubeDL())
    ie1.extract('http://www.youtube.com/watch?v=BaW_jenozKc')
    t1 = MetadataFromTitlePP(None, '%(title)s - %(artist)s')
    t1.run(ie1.result)
    t2 = MetadataFromTitlePP(None, '%(title)s - %(artist)s')
    t2.run(ie1.result)
    t3 = MetadataFromTitlePP(None, '%(artist)s - %(title)s')
    t3.run(ie1.result)
    assert ie1.result['artist'] is None
    assert ie1.result['title'] is not None

    ie2

# Generated at 2022-06-14 18:07:56.325060
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    ydl = FakeYdl()

    # With valid %(xxx)s in titleformat
    pp = MetadataFromTitlePP(ydl, '%(artist)s - %(title)s')
    assert pp.run({'title': 'FooBar - FooBar'}) == ([], {
        'artist': 'FooBar',
        'title': 'FooBar - FooBar',
    })

    # With invalid %(xxx)s in titleformat
    pp = MetadataFromTitlePP(ydl, '%(artist)s - %(title')
    assert pp.run({'title': 'FooBar - FooBar'}) == ([], {
        'title': 'FooBar - FooBar',
    })

    # With valid regex in titleformat

# Generated at 2022-06-14 18:08:06.372257
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    fmt = '%(title)s - %(artist)s'
    regex = MetadataFromTitlePP(None, fmt)._titleregex
    title = 'ABC - DEF'
    assert re.match(regex, title).groupdict() == {'title': 'ABC', 'artist': 'DEF'}

    fmt = '%(title)s - %(artist)s - %(year)s'
    regex = MetadataFromTitlePP(None, fmt)._titleregex
    title = 'ABC - DEF - 2017'
    assert re.match(regex, title).groupdict() == {'title': 'ABC', 'artist': 'DEF', 'year': '2017'}

    fmt = '%(title)s - %(artist)s - %(year)s - %(weekday)s'
    regex = MetadataFromTitle

# Generated at 2022-06-14 18:08:12.220266
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    """test MetadataFromTitlePP with run method"""
    pp = MetadataFromTitlePP(None, '%(title)s - %(artist)s - %(album)s')
    info = {'title': 'title - artist - album'}
    pp.run(info)
    assert('title' in info)
    assert(info['title'] == 'title')
    assert('artist' in info)
    assert(info['artist'] == 'artist')
    assert('album' in info)
    assert(info['album'] == 'album')

