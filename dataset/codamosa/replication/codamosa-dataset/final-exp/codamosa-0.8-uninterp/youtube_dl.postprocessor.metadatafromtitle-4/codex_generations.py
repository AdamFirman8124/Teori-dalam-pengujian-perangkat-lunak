

# Generated at 2022-06-14 17:58:35.810838
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    downloader = object()
    _ = downloader.to_screen
    info = {}

# Generated at 2022-06-14 17:58:42.344681
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ydl.extractor.common import InfoExtractor
    from ydl.utils import DateRange
    pp = MetadataFromTitlePP(None, '%(title)s - %(artist)s')
    info = {
        'title': 'Test Name - Test Artist',
        'end_date': DateRange(),
    }
    # info should now be {
    #     'title': 'Test Name',
    #     'artist': 'Test Artist',
    #     'end_date': DateRange(),
    #     }
    pp.run(info)
    assert info['title'] == 'Test Name'
    assert info['artist'] == 'Test Artist'

# Generated at 2022-06-14 17:58:46.897071
# Unit test for method format_to_regex of class MetadataFromTitlePP
def test_MetadataFromTitlePP_format_to_regex():
    p = MetadataFromTitlePP(None, '%(title)s')
    assert p._titleregex == '(?P<title>.+)'

    p = MetadataFromTitlePP(None, '%(title)s - %(artist)s')
    assert p._titleregex == '(?P<title>.+)\ \-\ (?P<artist>.+)'


# Generated at 2022-06-14 17:58:57.742846
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .YoutubeDL import YoutubeDL
    from .extractor.generic import UrlIE

    downloader = YoutubeDL(params={})
    # Initialize downloader with an empty cache (should not be necessary)
    downloader.cache = {}

    # Create a dummy subclass of InfoExtractor
    class UrlIE(UrlIE):
        def _real_extract(self, url):
            return {
                'id': 'abc123',
                'title': 'After School Special',
                'description': 'description',
                'uploader': 'uploader',
                'upload_date': '20170101',
                'timestamp': 1483225107,
            }
    downloader.add_info_extractor(UrlIE)

    # Create a PostProcessor for testing

# Generated at 2022-06-14 17:59:07.125470
# Unit test for method format_to_regex of class MetadataFromTitlePP
def test_MetadataFromTitlePP_format_to_regex():
    testcases = (('%(chapter)s/%(title)s', r'\(?P<chapter>.+\)\ \/\ \(?P<title>.+\)'),
                 ('%(class)s - %(title)s', r'\(?P<class>.+\)\ \-\ \(?P<title>.+\)'),
                 ('%(boyz)s', r'\(?P<boyz>.+\)'),
                 ('%(title)s (%(boyz)s)', r'\(?P<title>.+\)\ \(?P<boyz>.+\)'),
                 )
    pp = MetadataFromTitlePP(None, None)
    for fmt, regex in testcases:
        assert pp.format_to_regex(fmt) == regex

# Generated at 2022-06-14 17:59:12.308206
# Unit test for method format_to_regex of class MetadataFromTitlePP
def test_MetadataFromTitlePP_format_to_regex():
    class Dummy(object): pass
    downloader = Dummy()
    downloader.to_screen = lambda msg: msg
    pp = MetadataFromTitlePP(downloader, '')

    def test_case(fmt, expected):
        regex = pp.format_to_regex(fmt)
        assert re.match(regex, expected) is not None, 'Unexpected output of format_to_regex for fmt: "%s"' % fmt

    test_case('%(title)s - %(artist)s', 'This is the song - The artist')
    test_case('%(genre)s - %(album)s', 'Hi Hop - Greatest Hits')
    test_case('%(title)s - %(album)s - %(artist)s', 'Song title - Greatest Hits - The artist')

# Generated at 2022-06-14 17:59:23.599036
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    """
    Testing method run of class MetadataFromTitlePP
    """
    titleformat = '%(title)s - %(artist)s'
    titleregex = '(?P<title>.+)\ \-\ (?P<artist>.+)'
    title = 'One One Three - Nine Inch Nails'
    info = {'title': title}

    from .downloader import FakeDownloader
    downloader = FakeDownloader()
    downloader.to_screen = fakeToScreen

    metadata_from_title = MetadataFromTitlePP(downloader, titleformat)
    metadata_from_title._titleregex = titleregex
    metadata_from_title.run(info)

    assert info['title'] == 'One One Three'
    assert info['artist'] == 'Nine Inch Nails'


# Generated at 2022-06-14 17:59:31.422953
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    import unittest
    import test_routines
    import youtube_dl
    assert 'youtube_dl.postprocessor.MetadataFromTitlePP' in sys.modules

    class TestMetadataFromTitlePP(test_routines.TestDownloader):
        def pp_run(self, *args, **kwargs):
            postprocessor = MetadataFromTitlePP(self, '%(title)s')
            return postprocessor.run(*args, **kwargs)


# Generated at 2022-06-14 17:59:42.630276
# Unit test for method format_to_regex of class MetadataFromTitlePP
def test_MetadataFromTitlePP_format_to_regex():
    mpp = MetadataFromTitlePP(None, '%(title)s')
    assert mpp.format_to_regex('%(title)s') == '(?P<title>.+)'

    mpp = MetadataFromTitlePP(None, '%(title)s - %(artist)s')
    assert mpp.format_to_regex('%(title)s - %(artist)s') == '(?P<title>.+)\ \-\ (?P<artist>.+)'

    mpp = MetadataFromTitlePP(None, '[%(album)s] %(title)s - %(artist)s')

# Generated at 2022-06-14 17:59:52.811683
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    if sys.version_info[0] == 2:
        return
    import unittest
    import os
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                    '..', '..', '..')))
    from youtube_dl.extractor.common import InfoExtractor
    from youtube_dl.utils import DownloadError
    class FakeIE(InfoExtractor):
        IE_NAME = 'Fake'
    class TestMetadataFromTitlePP_run(unittest.TestCase):
        def setUp(self):
            self.ie = FakeIE(None)
            self.pp = MetadataFromTitlePP(self.ie, '%(title)s - %(artist)s')

# Generated at 2022-06-14 18:00:03.829506
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ydl.postprocessor import get_postprocessor
    from ydl.compat import compat_http_server
    from ydl import YDL
    from contextlib import closing
    from ydl.downloader.http.HTTPDownloader import HTTPDownloader
    from ydl.downloader.http.HTTPDownloader import Extractor

    class TitleServer(compat_http_server.HTTPServer):
        def __init__(self, server_address, handler, downloader):
            server = lambda *args: None
            setattr(server, 'ydl', downloader)
            super(TitleServer, self).__init__(server_address, handler, server)

    class TitleHandler(compat_http_server.BaseHTTPRequestHandler):
        def do_HEAD(s):
            s.send_response(200)


# Generated at 2022-06-14 18:00:12.906060
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    from youtube_dl.YoutubeDL import YoutubeDL

# Generated at 2022-06-14 18:00:25.495774
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.PostProcessor import PostProcessor
    from youtube_dl.compat import compat_urllib_parse
    ydl_opts = {
        'keepvideo': True,
        'writethumbnail': True,
        'writeinfojson': True,
        'writedescription': True,
        'writeannotations': True,
        'writesubtitles': True,
        'writeautomaticsub': True,
        'write_all_thumbnails': True,
        'format': 'bestvideo+bestaudio',
        'outtmpl': '%(id)s.%(ext)s',
    }
    ydl = YoutubeDL(ydl_opts)

    # Test with youtube_dl internal postprocessors (note:
    # metadatafromtitle

# Generated at 2022-06-14 18:00:36.371710
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import unittest
    from ydl import YoutubeDL
    class TestYDL(YoutubeDL):
        def __init__(self):
            super(TestYDL, self).__init__({})

        def to_screen(self, str):
            self.to_screen_cache += str + '\n'

        to_screen_cache = ''

    class TestMetadataFromTitlePP(MetadataFromTitlePP):
        def __init__(self, titleformat):
            super(TestMetadataFromTitlePP, self).__init__(TestYDL(), titleformat)

    def check_title(titleformat, title, attributes_output):
        test_pp = TestMetadataFromTitlePP(titleformat)
        test_pp.run({'title':title})
        for attribute, value in attributes_output.items():
            test_pp

# Generated at 2022-06-14 18:00:46.485621
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    testfiles_folder = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), 'testfiles'
    )
    video_title = 'MP3_sample_512kbps_44kHz_stereo_2m03s - YouTube.mp4'
    downloader = Dummy()
    downloader.params['format'] = 'default'
    downloader.params['titleformat'] = '%(title)s - %(artist)s'
    downloader.params['outtmpl'] = os.path.join(
        testfiles_folder, '%(title)s - %(artist)s.mp3'
    )
    downloader.to_screen('[fromtitle] Title of video: %s' % video_title)

    metadata_info = {'title': video_title}

# Generated at 2022-06-14 18:00:57.447071
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class TestDownloader:
        test_title = ['']
        def to_screen(self, message):
            TestDownloader.test_title.append(message)

    class TestYoutubeDL:
        def __init__(self, titleformat):
            self.format = titleformat
        def extract_info(self, url, download=False):
            return {'title': url}
        def to_screen(self, message):
            TestYoutubeDL.test_title.append(message)

    # Test without (...)s in title
    TestYoutubeDL.test_title = []
    titleformat = 'Welcome to the world of tomorrow'
    pp = MetadataFromTitlePP(TestYoutubeDL(titleformat), titleformat)
    title = 'Welcome to the world of tomorrow'

# Generated at 2022-06-14 18:01:09.075891
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    mp4 = 'The.Big.Bang.Theory.S03E01.HDTV.XviD-LOL.avi'
    title_format = '%(show)s.S%(season_num)02dE%(episode_num)02d.%(resolution)s.%(codec)s.%(ext)s'
    mp4_title = 'The.Big.Bang.Theory.S03E01.HDTV.XviD-LOL.avi'

    pp = MetadataFromTitlePP(None, title_format)
    pp_result = pp.run({'title': mp4})
    pp_info = pp_result[1]

    assert pp_info['title'] == mp4_title
    assert pp_info['show'] == 'The.Big.Bang.Theory'
    assert pp_

# Generated at 2022-06-14 18:01:20.187389
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    mock_downloader = type('MockDownloader', (object,), {
        'to_screen': lambda self, s: None,
        'to_stderr': lambda self, s: None,
        'report_warning': lambda self, s: None,
    })()
    pp_titleformat = r'%(artist)s - %(title)s'
    pp = MetadataFromTitlePP(mock_downloader, pp_titleformat)

    # Test case 1: No match
    info = {'title': 'Hello  -  World  - Test'}
    res = pp.run(info)
    assert info['title'] == res[1]['title']


    # Test case 2: Single match
    pp_titleformat = r'%(title)s'

# Generated at 2022-06-14 18:01:31.573607
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    title = 'First Name: David | Last Name: Hurley | Country: Ireland'
    format = 'First Name: %(first)s | Last Name: %(last)s | Country: %(country)s'
    info = {'title': title}

    p = MetadataFromTitlePP(None, format) # no downloader needed
    metadata, info = p.run(info)

    # No metadata are returned, because it's all stored in info
    assert metadata == []
    assert info['title'] == title
    assert 'first' in info and info['first'] == 'David'
    assert 'last' in info and info['last'] == 'Hurley'
    assert 'country' in info and info['country'] == 'Ireland'



# Generated at 2022-06-14 18:01:37.361345
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Test function
    def run_test(title, titleformat, expected_attributes):
        from youtube_dl.YoutubeDL import YoutubeDL
        from youtube_dl.compat import compat_str
        ydl = YoutubeDL()
        pp = MetadataFromTitlePP(ydl, titleformat)
        info = {'title': title, 'webpage_url': compat_str(title)}
        pp.run(info)
        for attribute, value in expected_attributes.items():
            assert info[attribute] == value
        return True

    # Test cases
    # format: %(key)s
    assert run_test(
        'title',
        '%(title)s',
        {'title': 'title'}
    )

# Generated at 2022-06-14 18:01:44.438314
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    downloader = object()
    pp = MetadataFromTitlePP(downloader, '%(title)s-%(artist)s')
    info = {
        'title': 'ololo-trololo',
    }
    res, new_info = pp.run(info)
    assert res == []
    assert info['title'] == 'ololo-trololo'
    assert info['artist'] == 'trololo'


# Generated at 2022-06-14 18:01:56.496127
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import unittest
    import sys

    class NullLogger(object):
        def debug(self, msg):
            pass
        def warning(self, msg):
            pass
        def error(self, msg):
            pass


# Generated at 2022-06-14 18:02:04.083639
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FakeYDL
    from .compat import compat_urllib_parse
    ydl = FakeYDL()
    ydl.add_default_info_extractors()
    ydl.add_post_processor(
        MetadataFromTitlePP(ydl, '%(title)s - %(uploader)s - %(id)s'))
    ydl.download(['http://www.youtube.com/watch?v=BaW_jenozKc'])

    assert ydl.extractor.title == 'youtube-dl test video \'BaW_jenozKc\''
    assert ydl.extractor.uploader == 'Philipp Hagemeister'
    assert ydl.extractor.id == 'BaW_jenozKc'


## ==========================================
##  Metadata From JSON
## =================================

# Generated at 2022-06-14 18:02:15.270229
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.utils import DateRange, DateRangeSkel
    from youtube_dl.YoutubeDL import YoutubeDL

    class FakeDownloader:
        def to_screen(self, msg):
            pass

    ydl = YoutubeDL({})
    ydl.add_info_extractor('youtube')
    ydl.add_post_processor(MetadataFromTitlePP(ydl, '%(title)s'))
    ydl.process_ie_result({
        '_type': 'url',
        'url': 'https://youtu.be/BaW_jenozKc',
    }, download=False)

# Generated at 2022-06-14 18:02:20.861531
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    ydl = object()
    pp = MetadataFromTitlePP(ydl, titleformat='%(artist)s - %(title)s')
    info = {
        'title': 'Example Artist - Example Title',
    }

    res, info_res = pp.run(info)
    assert res == []
    assert info_res == {
        'title': 'Example Artist - Example Title',
        'artist': 'Example Artist',
        'title': 'Example Title',
    }

    pp = MetadataFromTitlePP(ydl, titleformat='%(title)s - %(artist)s')
    info = {
        'title': 'Example Title - Example Artist',
    }

    res, info_res = pp.run(info)
    assert res == []

# Generated at 2022-06-14 18:02:32.336948
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from . import FakeYDL
    # when regex parses title successfully
    fake_ydl = FakeYDL({'title': 'Parsed title - Artist'})
    pp = MetadataFromTitlePP.new_from_config(fake_ydl, {
        'titleformat': '%(title)s - %(artist)s',
    })
    _, info = pp.run({'title': 'Parsed title - Artist'})
    assert 'title' in info
    assert info['title'] == 'Parsed title'
    assert 'artist' in info
    assert info['artist'] == 'Artist'
    # when title doesn't match the regex
    fake_ydl = FakeYDL({'title': 'Parsed title - Artists'})

# Generated at 2022-06-14 18:02:43.622144
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import ydl_test
    class MyDownloader(ydl_test.MockYDL):
        def __init__(self, *args, **kwargs):
            super(MyDownloader, self).__init__(*args, **kwargs)
            self._screen_file = self.file_descriptor

    mydl = MyDownloader()
    titleformat = '%(title)s - %(artist)s'
    meta_from_title_pp = MetadataFromTitlePP(mydl, titleformat)
    info = dict(title='foo')
    meta_from_title_pp.run(info)
    assert mydl.file_descriptor.getvalue() == (
        '[fromtitle] Could not interpret title of video as "%s"\n'
        % titleformat)
    mydl.file_descriptor

# Generated at 2022-06-14 18:02:54.240783
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    metadata_from_title_pp = MetadataFromTitlePP(
        downloader=None,
        titleformat='(?P<title2>.*)')
    test_title = 'Test'
    test_info = {
        'title': test_title
    }
    test_info_expected = {
        'title': test_title,
        'title2': test_title
    }
    err_list, info = metadata_from_title_pp.run(test_info)
    assert err_list == []
    assert info == test_info_expected

    metadata_from_title_pp = MetadataFromTitlePP(
        downloader=None,
        titleformat='%(title)s - %(artist)s')
    test_title = 'Test title - Test artist'

# Generated at 2022-06-14 18:03:04.413492
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Test case 1: parse: only %(title)s
    assert MetadataFromTitlePP(None, '%(title)s').run(
               {'title': 'this is the title of the video'}
           ) == ([],
               {'title': 'this is the title of the video',
                'title': 'this is the title of the video'})

    # Test case 2: parse: %(title)s and %(artist)s
    assert MetadataFromTitlePP(None, '%(artist)s - %(title)s').run(
               {'title': 'this is the title of the video'}
           ) == ([],
               {'title': 'this is the title of the video',
                'title': 'this is the title of the video',
                'artist': None})

    # Test case 3: parse:

# Generated at 2022-06-14 18:03:12.564828
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    import pytest
    def to_screen(msg):
        print(msg)

    metadata_from_titlePP = MetadataFromTitlePP(
        to_screen, '%(title)s - %(artist)s')
    # Case 1: MetadataFromTitlePP produces only expected outputs
    test_info = {'title': 'Someday - Mariah Carey'}
    expected_info = {'title': 'Someday', 'artist': 'Mariah Carey'}
    outputs, info = metadata_from_titlePP.run(test_info)
    assert info == expected_info
    assert outputs == []
    # Case 2: MetadataFromTitlePP produces warning msg
    test_info = {'title': 'Hello - Mariah Carey'}
    expected_info = {'title': 'Hello - Mariah Carey'}

# Generated at 2022-06-14 18:03:18.013336
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    postProcessor = MetadataFromTitlePP(None, "%(title)s")
    info = {'title': 'This Is A Test Title'}
    info_output = {'title': 'This Is A Test Title'}
    info_return, info_output_return = postProcessor.run(info)
    success = (info == info_return and info_output == info_output_return)
    assert success, 'Error in method run of class MetadataFromTitlePP'



# Generated at 2022-06-14 18:03:27.564310
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FileDownloader
    from .compat import compat_str
    from .extractor.youtube import YoutubeIE

    #Test 1
    youtubeie = YoutubeIE()
    fd = FileDownloader(None, None)
    fd.add_info_extractor(youtubeie)
    ffpp = MetadataFromTitlePP(fd, '%(uploader)s')
    ffd = {}
    ffd['title'] = 'uploader'
    ffd['url'] = 'http://youtu.be/XB3qhBddBL4'
    for i in range(10):
        ffd['id'] = compat_str(i)

# Generated at 2022-06-14 18:03:37.784566
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    assert MetadataFromTitlePP(None, '%(artist)s - %(title)s').run(
        dict(title='Track Title')) == ([], dict(title='Track Title'))
    assert MetadataFromTitlePP(None, '%(artist)s - %(title)s').run(
        dict(title='Artist - Track Title')) == ([], dict(
        artist='Artist', title='Track Title'))
    assert MetadataFromTitlePP(None, '%(artist)s - %(title)s').run(
        dict(title='Artist - Album - Track Title')) == ([], dict(
        artist='Artist', title='Album - Track Title'))

# Generated at 2022-06-14 18:03:47.732870
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys

    if sys.version_info < (3, 0):
        from StringIO import StringIO
    else:
        from io import StringIO

    # Set up data
    test_title = (
        '%(title)s - %(artist)s - %(catch_phrase)s'
    )
    test_title_alternative = (
        '%(title)s - %(album)s - %(artist)s'
    )
    video_title = 'Some video - Some album - Some artist - Some catch phrase'
    video_info = {'title': video_title}
    metadata = {}
    actual_output = ''
    expected_output = (
        '[fromtitle] Could not interpret title of video as "%s"\n'
        % test_title_alternative
    )

    # Redirect std

# Generated at 2022-06-14 18:03:58.749348
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    if sys.version_info < (3, 0):
        from io import BytesIO
        from types import UnicodeType
    else:
        from io import StringIO as BytesIO
        from builtins import str as UnicodeType
    from .common import FileDownloader
    from .extractor import gen_extractors
    from .postprocessor import gen_pp

    titleformat = '%(title)s - %(artist)s'
    _, pp = gen_pp(gen_extractors(), {'fromtitle': titleformat})
    title = 'Some TItle - Some Artist (with Brackets)'
    info = {'title': title}
    expected = {'title': 'Some TItle', 'artist': 'Some Artist (with Brackets)'}
    fd = FileDownloader(None)

# Generated at 2022-06-14 18:04:08.493418
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Test class initialization
    titleformat = '%(title)s - %(artist)s'
    titleregex = '(?P<title>.+)\ \-\ (?P<artist>.+)'
    # Test _format_to_regex()
    assert MetadataFromTitlePP({}, titleformat)._titleregex == titleregex

    # Test _run()
    assert MetadataFromTitlePP({}, titleformat).run({'title': 'a - b'}) == ([], {'title': 'a', 'artist': 'b'})

if __name__ == '__main__':
    test_MetadataFromTitlePP_run()

# Generated at 2022-06-14 18:04:18.132050
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    if sys.version_info < (2, 7):
        import unittest2 as unittest
    else:
        import unittest
    class FakeYoutubeDl(object):
        def to_screen(self, message):
            print(message)
    class FakeInfoDict():
        def __init__(self, title = ''):
            self['title'] = title
    fake_downloader = FakeYoutubeDl()
    fake_info = FakeInfoDict('ARandomTitle')

    # Test for a title format that does not contain any %()s
    titleFormat = 'ARandomTitle'
    pp = MetadataFromTitlePP(fake_downloader, titleFormat)
    info = pp.run(fake_info)[1]
    assert info['title'] == 'ARandomTitle'

    # Test for

# Generated at 2022-06-14 18:04:26.307044
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    sys.path.append("../")
    from ydl_downloader import YDLDownloader
    class MockDownloader(YDLDownloader):
        def to_screen(self, msg):
            pass

    downloader = MockDownloader()
    downloader.params = {'writeinfojson': True, 'format': 'best'}
    data = {'title': 'title - artist - album'}
    post_processor = MetadataFromTitlePP(downloader, '%(title)s - %(artist)s - %(album)s')
    result, data = post_processor.run(data)
    assert data['artist'] == 'artist'
    assert data['title'] == 'title'
    assert data['album'] == 'album'

# Generated at 2022-06-14 18:04:34.428555
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from . import YoutubeDL
    ydl = YoutubeDL()

    ydl.params['simulate'] = True
    ydl.params['skip_download'] = True
    ydl.params['quiet'] = True

    ydl.add_info_extractor(lambda x: {'id': 'foo'})

    # Test 1: match video title exactly
    metadata = {'title': 'Rammstein - Engel (Official Video)'}
    ydl.add_post_processor(MetadataFromTitlePP('foo', '%(title)s'))
    results, metadata = ydl.process_ie_result(metadata, download=False)
    assert metadata['title'] == metadata['title']

    # Test 2: match video title with regex group
    metadata = {'title': 'Rammstein - Engel (Official Video)'}
    ydl.add

# Generated at 2022-06-14 18:04:45.822457
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # test with simple
    class FakeInfo(object):
        def __init__(self, title):
            self.title = title

    class FakeDownloader(object):
        def to_screen(self, s):
            pass

    mp = MetadataFromTitlePP(FakeDownloader(), '%(title)s')
    info = FakeInfo('This is the title')
    _, info_out = mp.run(info)
    assert info_out['title'] == 'This is the title'

    # test with regex
    mp = MetadataFromTitlePP(FakeDownloader(), '%(title)s-%(artist)s')
    info = FakeInfo('This is the title - This is the artist')
    _, info_out = mp.run(info)
    assert info_out['title'] == 'This is the title'
   

# Generated at 2022-06-14 18:04:52.369371
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    d = {'title': 'house - something else'}
    p = MetadataFromTitlePP(None, '%(title)s - %(artist)s')
    e = {'title': 'house', 'artist': 'something else'}
    assert p.run(d)[1] == e

# Generated at 2022-06-14 18:05:03.315621
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FileDownloader
    from .extractor.common import InfoExtractor
    from .compat import compat_urllib_error

    class FakeInfoExtractor(InfoExtractor):
        def __init__(self, downloader=None, ie_key=None, ie_dir=None):
            self.ie_key = ie_key
            self.ie_dir = ie_dir
            super(FakeInfoExtractor, self).__init__(downloader)

    class FakeFileDownloader(FileDownloader):
        def __init__(self, params=None):
            self.params = params or {}

        def to_screen(self, *args, **kwargs):
            pass


# Generated at 2022-06-14 18:05:10.424303
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class DummyYDL():
        def to_screen(self, msg):
            print(msg)

    import unittest
    case = unittest.TestCase()


# Generated at 2022-06-14 18:05:17.660802
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ytdl_opener import youtube_dl
    # Create a fake downloader and pass a test title
    pp = MetadataFromTitlePP(youtube_dl(), '%(artist)s - %(title)s')
    test_title = 'Artist - Title (feat. Contributor)'
    (_, info) = pp.run({'title': test_title})
    # Check that the artist is correct
    assert info['artist'] == 'Artist'
    # Check that the title is correct
    assert info['title'] == 'Title (feat. Contributor)'

# Generated at 2022-06-14 18:05:28.509613
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys

    class test_downloader:
        def to_screen(self, output):
            print(output)

    def test_parsing_logic(titleformat, input, output):
        dler = test_downloader()
        pp = MetadataFromTitlePP(dler, titleformat)
        info = {'title': input}
        res, info = pp.run(info)
        assert res == []
        assert info['title'] == input
        for k,v in output.items():
            assert info[k] == v, 'Expected %s, got %s' % (repr(v), repr(info[k]))
        print('Test successful')


# Generated at 2022-06-14 18:05:37.734385
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import collections
    import unittest

    class MockDownloader(object):
        def to_screen(self, msg):
            pass

    class _MetadataFromTitlePPTestCase(unittest.TestCase):
        def setUp(self):
            self._downloader = MockDownloader()
            self._pp = MetadataFromTitlePP(self._downloader, '%(artist)s - %(title)s')

        def test_run_no_match(self):
            title = 'Metallica - Nothing Else Matters (HD Official Video)'
            exp_metadata = collections.defaultdict(set)
            exp_metadata['title'] = {title}
            metadata = collections.defaultdict(set, {'title': {title}})
            metadata, info = self._pp.run(metadata)

# Generated at 2022-06-14 18:05:47.989684
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL

    class FakeInfoDict(dict):
        def __init__(self, *args, **kwargs):
            super(FakeInfoDict, self).__init__(*args, **kwargs)
            self['title'] = 'testtitle'

    def test(titleformat):
        pp = MetadataFromTitlePP(YoutubeDL(), titleformat)
        info = FakeInfoDict()
        pp.run(info)
        return info

    assert test('%(title)s') == {'title': 'testtitle'}
    assert test('%(title)s - %(artist)s') == {
        'artist': 'NA', 'title': 'testtitle'}

# Generated at 2022-06-14 18:05:53.824453
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Importing methods directly
    from youtube_dl.downloader.common import FileDownloader
    from youtube_dl.postprocessor import run_postprocessors

    fd = FileDownloader()

    # Create test directory
    import tempfile
    tempdir = tempfile.mkdtemp()
    fd.outtmpl = tempdir + '/' + 'youtube_dl.%(ext)s'

    # Fill in data for file download
    info = {
        'title': 'artist - title',
        'ext': 'mp4',
        'filepath': tempdir + '/' + 'youtube_dl.mp4',
    }

    # Check that metadata from title are parsed as expected
    pp = MetadataFromTitlePP(fd, '%(artist)s - %(title)s')
    pp.run(info)


# Generated at 2022-06-14 18:06:03.113074
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    d = {'title': 'Video Title - YouTube',
         'test': 'original'}
    o = {'test': 'original'}
    MetadataFromTitlePP(None, '%(title)s').run(d)
    o.update({'title': 'Video Title'})
    assert(d == o)
    d = {'title': 'Video Title - YouTube',
         'test': 'original'}
    o = {'test': 'original'}
    MetadataFromTitlePP(None, '%(title)s - %(foo)s').run(d)
    o.update({'title': 'Video Title'})
    assert(d == o)
    d = {'title': 'Video Title - YouTube',
         'test': 'original'}

# Generated at 2022-06-14 18:06:10.256134
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class FakeDownloader(object):
        def to_screen(self, s): pass
    v = MetadataFromTitlePP(FakeDownloader(), '%(title)s - %(artist)s')
    assert v.run({'id': 'test', 'url': 'test',
                  'title': 'testtitle - testartist'})[1] == \
           {'id': 'test', 'url': 'test',
            'title': 'testtitle - testartist',
            'title_from_title': 'testtitle - testartist',
            'artist': 'testartist'}

# Generated at 2022-06-14 18:06:24.721123
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    def _test(result_info, title, titleformat):
        import YDLDownloader
        pp = MetadataFromTitlePP(YDLDownloader(), titleformat)
        info = {'title': title}
        _, info = pp.run(info)
        assert result_info == info
    _test({}, 'Artist - Title', 'artist - title')
    _test({'artist': 'Artist', 'title': 'Title'}, 'Artist - Title', 'artist - title')
    _test({}, 'Artist - Title', 'artist - title - year')
    _test({'artist': 'Artist', 'title': 'Title', 'year': '2016'}, 'Artist - Title (2016)', 'artist - title \(%(year)s\)')

# Generated at 2022-06-14 18:06:29.380806
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    dummy_downloader = object()
    pp = MetadataFromTitlePP(dummy_downloader, '%(title)s - %(artist)s')
    info = {'title': 'this is a title - this is an artist'}
    pp.run(info)
    assert info['title'] == 'this is a title'
    assert info['artist'] == 'this is an artist'

# Generated at 2022-06-14 18:06:41.563576
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ytdl_saver.common import FileDownloader
    from ytdl_saver.extractor.common import YoutubeIE

    # Test initialization and title format to regex conversion
    metadata_pp = MetadataFromTitlePP(FileDownloader(), '%(title)s')
    assert metadata_pp._titleformat == '%(title)s'
    assert metadata_pp._titleregex == '(?P<title>.+)'
    metadata_pp = MetadataFromTitlePP(FileDownloader(), '%(title)s - %(artist)s')
    assert metadata_pp._titleformat == '%(title)s - %(artist)s'
    assert metadata_pp._titleregex == '(?P<title>.+)\ \-\ (?P<artist>.+)'

    # Test regular expression matching

# Generated at 2022-06-14 18:06:51.047053
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    if sys.version_info[0] < 3:
        from urllib import unquote
    else:
        from urllib.parse import unquote
    from .common import Downloader
    from .compat import compat_urlparse
    from .extractor import gen_extractors

    fmt1 = '%(title)s - %(artist)s'
    fmt2 = '[%(webpage_url)s]%(title)s'

    url1 = 'https://www.youtube.com/watch?v=abcdefghij'
    url2 = 'http://www.example.com/'
    title1 = 'title - artist'
    title2 = '[%s]title' % unquote(url2)


# Generated at 2022-06-14 18:07:00.959518
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FileDownloader

    # Define test function for tests
    def testrun(title, titleformat, expected):
        downloader = FileDownloader({}, None)
        pp = MetadataFromTitlePP(downloader, titleformat)
        info = { 'title': title }
        pp.run(info)
        assert info == expected

    # Test run with simple format
    testrun('Testvideo', '%(title)s', {'title': 'Testvideo'})

    # Test run with simple format and additional info
    testrun('Testvideo', '%(title)s - %(id)s', {'title': 'Testvideo', 'id': ''})

    # Test run with simple format and additional info

# Generated at 2022-06-14 18:07:08.667129
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import pytest
    import ytdl

    @ytdl.hook.video_info
    def test_MetadataFromTitlePP_run_hook(info):
        info['title'] = 'Free Speech - Classical Music in Public Domain'
        return [
            ytdl.extractor.MetadataFromTitlePP(
                None, '%(title)s - %(artist)s')
                .run(info)
        ]
    downl = ytdl.YoutubeDL({'video_info_hooks': test_MetadataFromTitlePP_run_hook})
    res = downl.extract_info('somevideoid')
    assert res['artist'] == 'Classical Music in Public Domain'
    assert res['title'] == 'Free Speech'


# Generated at 2022-06-14 18:07:15.757468
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import unittest
    downloader = FakeDownloader()
    pp = MetadataFromTitlePP(downloader, '%(title)s-%(album)s')
    info = {
        'title' : 'Titulo',
        'album' : 'Album',
        'artist' : 'Artista'
    }
    res = pp.run(info)
    unittest.TestCase().assertEqual([], res[0])
    for k in info:
        unittest.TestCase().assertEqual(info[k], res[1][k])


# Generated at 2022-06-14 18:07:27.883880
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    sys.path = sys.path[1:]
    from youtube_dl.downloader.common import FileDownloader
    from youtube_dl.YoutubeDL import YoutubeDL

    downloader = FileDownloader({'postprocessors': [{
        'key': 'MetadataFromTitle',
        'titleformat': '%(artist)s - %(title)s',
    }]}, YoutubeDL({}))
    info = {'title': 'The Artist - The Title'}
    metadata, _ = downloader.postprocessor.run(info)
    assert metadata == {'artist': 'The Artist', 'title': 'The Title'}

    metadata, _ = downloader.postprocessor.run({'title': 'The Artist  -  The Title'})

# Generated at 2022-06-14 18:07:36.829851
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FileDownloader  # necessary to initialize post_processors
    import sys
    import os
    import tempfile

    temp_dir = tempfile.mkdtemp(prefix='youtube-dl.test_MetadataFromTitlePP_run.')

# Generated at 2022-06-14 18:07:46.699963
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.utils import DateRange, std_headers
    from youtube_dl.downloader.http import HttpFD
    from youtube_dl.YoutubeDL import YoutubeDL

    class YoutubeDLFake(YoutubeDL):
        def __init__(self, *args, **kargs):
            super(YoutubeDLFake, self).__init__(*args, **kargs)
            self.to_screen_result = []

        def to_screen(self, message, **kargs):
            self.to_screen_result.append(message)


# Generated at 2022-06-14 18:08:05.865106
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():

    from .common import FileDownloader

    with open('test.out', 'wb') as f:
        f.write(
            b'some metadata title - some other metadata artist (some more stuff)'
        )
    d = FileDownloader({
        'outtmpl': 'test.out',
        'retries': 0,
    })
    pp = MetadataFromTitlePP(d, '%(title)s - %(artist)s')
    info = {'title': 'some metadata title - some other metadata artist (some more stuff)'}
    pp.run(info)
    assert info['title'] == 'some metadata title'
    assert info['artist'] == 'some other metadata artist'
    d.to_screen('[fromtitle] could not interpret title of video as "%%(title)s - %%(artist)s"')
    d

# Generated at 2022-06-14 18:08:11.384289
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    ydl = type('FakeYDL', (), {
        'to_screen': lambda self, msg: msg,
    })()
    pp = MetadataFromTitlePP(ydl, '%(artist)s - %(title)s')
    info = {
        'title': 'Andromeda - Night Of The Dolphin'
    }

    pp.run(info)

    assert info['title'] == 'Night Of The Dolphin'
    assert info['artist'] == 'Andromeda'

# Generated at 2022-06-14 18:08:21.578960
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import pytube

    yt = pytube.Youtube('http://youtu.be/aBOTn1nlsA4', '720p')

    # Example:
    #   title: 'The Weeknd - Often (NSFW)'
    #   titleformat: '%(artist)s - %(song)s'
    #   returns: {'artist': 'The Weeknd', 'song': 'Often (NSFW)'}
    pp = MetadataFromTitlePP(yt, '%(artist)s - %(song)s')
    info = {'title': 'The Weeknd - Often (NSFW)'}
    assert pp.run(info)[1] == {'title': 'The Weeknd - Often (NSFW)',
                               'artist': 'The Weeknd',
                               'song': 'Often (NSFW)'}

    #

# Generated at 2022-06-14 18:08:33.109970
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.InfoExtractors import YoutubeIE

    def extract(url, **kwargs):
        ie = YoutubeIE()
        ie.extract(url)
        return ie.result

    ydl = YoutubeDL()
    ydl.add_default_info_extractors()
    ydl.add_post_processor(MetadataFromTitlePP(ydl, '%(title)s'))

    info = extract('http://www.youtube.com/watch?v=RZiMbyZBdwY')
    assert info['title'] == 'Title: YouTube Downloader'
    assert 'extractor' in info
    assert 'webpage_url' in info
    assert 'id' in info
    assert 'uploader' in info
    assert 'upload_date'