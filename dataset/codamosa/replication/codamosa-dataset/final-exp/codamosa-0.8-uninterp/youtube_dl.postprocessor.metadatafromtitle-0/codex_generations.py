

# Generated at 2022-06-14 17:58:40.955240
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.downloader.FakeDownloader import FakeDownloader
    from youtube_dl.utils import UnavailableExtension
    ydl = YoutubeDL(params={'outtmpl': '%(id)s.%(ext)s'})
    with FakeDownloader(ydl) as fd:
        pp = MetadataFromTitlePP(fd, '%(title)s - %(artist)s')

        fd.add_info_extractors({
            'youtube': {
                'id': 'OQSNhk5ICTI',
                'title': 'WALK THE MOON - Shut Up and Dance (Official Video)',
            },
        })

        # Test without 'artist' field in result.

# Generated at 2022-06-14 17:58:51.082093
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import youtube_dl.extractor.common as extractor_common
    import youtube_dl.extractor.youtube as youtube_extractor

    downloader = extractor_common.FileDownloader(None)
    info = {'title': 'Crazy Frog - Axel F', 'ext': 'mp4'}

    pp = MetadataFromTitlePP(downloader,
                             '%(artist)s - %(title)s')
    info = pp.run(info)[1]
    assert info['title'] == 'Crazy Frog - Axel F'
    assert info['artist'] == 'Axel F'

    pp = MetadataFromTitlePP(downloader,
                             '%(artist)s - %(title)s - %(extra)s')
    info = pp.run(info)[1]

# Generated at 2022-06-14 17:58:57.898642
# Unit test for method format_to_regex of class MetadataFromTitlePP
def test_MetadataFromTitlePP_format_to_regex():
    pp = MetadataFromTitlePP(None, "%(foo)s - %(bar)s")

    return pp.format_to_regex("%(foo)s - %(bar)s") == "(?P<foo>.+)\ \-\ (?P<bar>.+)"


if __name__ == '__main__':
    import sys
    print(test_MetadataFromTitlePP_format_to_regex())
    sys.exit(0)

# Generated at 2022-06-14 17:59:07.686560
# Unit test for method format_to_regex of class MetadataFromTitlePP
def test_MetadataFromTitlePP_format_to_regex():
    obj = MetadataFromTitlePP(None, '')

    assert obj.format_to_regex('%(title)s') == '(?P<title>.+)'
    assert obj.format_to_regex('%(title)s %(artist)s') == '(?P<title>.+)\ (?P<artist>.+)'
    assert obj.format_to_regex('%(title)s - %(artist)s - %(album)s') == '(?P<title>.+)\ \-\ (?P<artist>.+)\ \-\ (?P<album>.+)'
    assert obj.format_to_regex('%(title)s - %(artist)s') == '(?P<title>.+)\ \-\ (?P<artist>.+)'

# Generated at 2022-06-14 17:59:19.886621
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import os
    import tempfile
    import ydl_opts
    import ydl
    from youtube_dl.extractor.common import InfoExtractor
    from youtube_dl import YoutubeDL
    # we need to replace the _downloader attribute of InfoExtractor
    old_downloader = InfoExtractor._downloader
    InfoExtractor._downloader = YoutubeDL()
    # temporary file for testing purposes
    tmp_output_file = tempfile.NamedTemporaryFile(mode='w')

    # create an InfoExtractor that uses the MetadataFromTitlePP postprocessor
    class SomeIE(InfoExtractor):
        @classmethod
        def suitable(cls, url):
            return True

# Generated at 2022-06-14 17:59:31.276941
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    """
    Test method run of class MetadataFromTitlePP
    """
    import os
    import sys
    import tempfile
    import unittest

    # sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
    # from ydl.postprocessor import MetadataFromTitlePP

    sys.stdout = open(os.devnull, 'w')

    class TestMetadataFromTitlePP(unittest.TestCase):
        def setUp(self):
            fmt = '%(title)s - %(album)s'
            self.pp = MetadataFromTitlePP(downloader = None, titleformat = fmt)
            self.info = {
                'title': 'Tokyo - night',
                'album': 'N/A'
            }

# Generated at 2022-06-14 17:59:39.098781
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    assert MetadataFromTitlePP(
        '', '%(artist)s - %(title)s'
    ).run(
        {'title': 'video title - artist - random text'}
    ) == ([], {'title': 'video title - artist - random text',
               'artist': 'artist'}), (
        'Failed to correctly parse video title to extract artist'
    )
    assert not MetadataFromTitlePP(
        '', '%(title)s - %(artist)s'
    ).run(
        {'title': 'video title - random text'}
    )[1], (
        'Failed to return info dict not containing artist'
    )


# Generated at 2022-06-14 17:59:50.446146
# Unit test for method format_to_regex of class MetadataFromTitlePP
def test_MetadataFromTitlePP_format_to_regex():
    mftpp = MetadataFromTitlePP(None, '%(name)s-%(year)s')

# Generated at 2022-06-14 18:00:02.423947
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # This is a unit test for the MetadataFromTitlePP class
    # This unit test is run by the test_postprocessor.py script
    # It is executed with the following command:
    #  python -m unittest youtube_dl.postprocessor.test_postprocessor.test_MetadataFromTitlePP_run
    # The test_postprocessor.py script is a standalone test program and
    # should run with Python2.7 and Python3.5.
    # It requires the following modules to be installed: pytest and pytest-cov (optional)
    # The py.test framework is described at http://pytest.org/

    from collections import namedtuple
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.PostProcessor import PostProcessor
    from youtube_dl.compat import compat_str

    D

# Generated at 2022-06-14 18:00:12.429385
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from pytube import Downloader
    from pytube.extractors.youtube import YoutubeIE
    from pytube.compat import compat_urlparse

    youtube_ie = YoutubeIE(Downloader())
    info = youtube_ie.extract(compat_urlparse.urlparse(
        'http://www.youtube.com/watch?v=BaW_jenozKc'))
    titleformat = '%(title)s - %(artist)s'
    pp = MetadataFromTitlePP(Downloader(), titleformat)
    info = pp.run(info)[1]
    assert info['title'] == 'Avril Lavigne - Hello Kitty'
    assert info['artist'] == 'Avril Lavigne'



# Generated at 2022-06-14 18:00:26.070556
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    downloader = object()
    # Initialize MetadataFromTitlePP object
    metadata_from_title_pp = MetadataFromTitlePP(downloader, '%(title)s')

    # Test 1:
    #  input: title = 'hello world'
    #  output: info = {'title': 'hello world'}
    info = {'title': 'hello world'}
    output_info, _ = metadata_from_title_pp.run(info)
    assert(output_info == {})
    assert(info['title'] == 'hello world')
    # Test 2:
    #  input: title = 'hello world'
    #  output: info = {'title': 'hello world', 'artist': 'hello world'}
    info = {'title': 'hello world'}

# Generated at 2022-06-14 18:00:35.875009
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class MockDl(object):
        def to_screen(self, msg):
            print (msg)
    dl = MockDl()
    pp = MetadataFromTitlePP(dl, '%(title)s - %(artist)s')
    assert pp.format_to_regex(pp._titleformat) == '(?P<title>.+)\ \-\ (?P<artist>.+)'
    info = {'title': 'A song title - A song artist'}
    pp.run(info)
    assert info['title'] == 'A song title'
    assert info['artist'] == 'A song artist'

    # Test for None value in metadata
    pp = MetadataFromTitlePP(dl, '%(title)s - %(artist)s - %(album)s')

# Generated at 2022-06-14 18:00:46.156416
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .extractor import common
    ytdl = common.FakeYDL()
    ytdl.add_default_info_extractors()

    # one match
    titleformat = '%(title)s %(artist)s'
    title = 'T1 A1'
    info = {}
    info['title'] = title
    v = MetadataFromTitlePP(ytdl, titleformat)
    exp_res = ('[fromtitle] parsed title: T1',
               '[fromtitle] parsed artist: A1')
    assert v.run(info) == ([], {})
    assert exp_res == ytdl.msgs

    # no match
    titleformat = '%(title)s %(artist)s'
    title = 'T1'
    info = {}
    info['title'] = title
    v

# Generated at 2022-06-14 18:00:55.037317
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    import tempfile
    import youtube_dl
    metadata = {'title': 'Shakira ft. Rihanna - Can\'t Remember to Forget You', 'url': 'http://youtube.com/watch?v=xk-FnQ2bNLE'}
    postprocessor = MetadataFromTitlePP(youtube_dl.FileDownloader({'verbose': sys.stdout}), '%(artist)s - %(title)s')

    postprocessor.run(metadata)
    assert metadata['title'] == 'Shakira ft. Rihanna - Can\'t Remember to Forget You'
    assert metadata['artist'] == 'Shakira ft. Rihanna'
    assert metadata['url'] == 'http://youtube.com/watch?v=xk-FnQ2bNLE'


# Generated at 2022-06-14 18:01:03.670471
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    downloader = None
    titleformat = '%(artist)s - %(title)s'
    title = 'The New Groove - The Lion Sleeps Tonight'
    info = {'title': title}
    metadata_from_title_pp = MetadataFromTitlePP(downloader, titleformat)
    info = metadata_from_title_pp.run(info)[1]

    assert info['artist'] == 'The New Groove'
    assert info['title'] == 'The Lion Sleeps Tonight'


# Generated at 2022-06-14 18:01:12.848675
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Initialize class MetadataFromTitlePP
    metadata_from_titlePP = MetadataFromTitlePP(None, '[%(artist)s]-[%(title)s]-[%(album)s]-[%(tracknumber)s]')
    # Initialize info
    info = {
        'title': '[La Roux]-[Tigerlily]-[Trouble In Paradise (Deluxe Edition)]-[12]',
        'artist': None,
        'album': None,
        'tracknumber': None,
    }
    # Assert that info of class MetadataFromTitlePP is equal to info
    assert (metadata_from_titlePP.run(info)[1] == info), \
        'Assertion failed: MetadataFromTitlePP.run(%s) == %s' % (info, info)

# Generated at 2022-06-14 18:01:24.316763
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.PostProcessor import PostProcessor

    class MockInfo(object):
        def __init__(self, title):
            self.title = title

    class MockYDL(object):
        def to_screen(self, msg):
            print(msg)
        def trouble(self, msg):
            print(msg)

    ydl = MockYDL()
    ydl.params = {}

    def assert_title_matches(title, info_attribs):
        pp = MetadataFromTitlePP(
            ydl, '%(title)s - %(artist)s - %(track)s')
        info = MockInfo(title)
        unused_file, new_info = pp.run(info)

# Generated at 2022-06-14 18:01:34.345041
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FileDownloader
    from .extractor.youtube import YoutubeIE
    from .utils import format_bytes
    from .compat import compat_urlparse
    from .compat import compat_chr
    import os
    import shutil
    from hashlib import md5

    # Template for creating the test files to be used for testing
    # The files will be created in the current directory
    # Editable parameters to create the files
    filesize = 1024 * 64 + 65
    titleformat = '%(title)s - %(artist)s'
    title = 'Nepal - Pahilo Junma'
    artist = 'Anil Singh'
    regex = MetadataFromTitlePP.format_to_regex(titleformat)
    filename = 'Nepal Pahilo Junma.mp4'

# Generated at 2022-06-14 18:01:36.058975
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl import Youtub

# Generated at 2022-06-14 18:01:41.115893
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.downloader.common import FileDownloader
    from youtube_dl.YoutubeDL import YoutubeDL
    downloader = FileDownloader({'outtmpl': '%(title)s.%(ext)s'}, YoutubeDL())
    pp = MetadataFromTitlePP(downloader, '%(title)s - %(artist)s')
    # Test "Artist - Title"
    info = {'id': '123', 'title': 'Artist - Title', 'ext': 'mp3'}
    info, _ = pp.run(info)
    assert info['title'] == 'Title'
    assert info['artist'] == 'Artist'
    # Test "Artist - Title (Remix)"
    info = {'id': '123', 'title': 'Artist - Title (Remix)', 'ext': 'mp3'}
   

# Generated at 2022-06-14 18:01:51.896705
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    """Test the run method of MetadataFromTitlePP"""

    info = {'title': 'Ceci est un clip'}
    assert MetadataFromTitlePP(None, '%(title)s').run(info)[1] == info

    info = {'title': 'Ceci est un clip - Fred'}
    assert MetadataFromTitlePP(None, '%(title)s - %(artist)s').run(info)[1] == {'artist': 'Fred', 'title': 'Ceci est un clip'}

# Generated at 2022-06-14 18:02:01.730993
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.extractor.common import InfoExtractor
    from youtube_dl.utils import DownloadError

    class FakeInfoExtractor(InfoExtractor):
        def __init__(self, downloader):
            pass

        def _real_extract(self, url):
            return {'title': url}

    # Mock downloader
    downloader_mock = YoutubeDL({'cachedir': False})
    downloader_mock.to_screen = lambda s: None
    downloader_mock.params = {}
    downloader_mock.add_info_extractor(FakeInfoExtractor)

    # test with _titleformat without %(..)s

# Generated at 2022-06-14 18:02:09.304609
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from xml.etree.ElementTree import fromstring, tostring
    tree = fromstring('''
    <options>
    </options>
    ''')
    args = {}
    args['format'] = '%(title)s - %(artist)s'
    args['title'] = 'My Title'
    args['artist'] = 'My Artist'
    import sys
    import io
    import unittest.mock
    out = io.StringIO()
    err = io.StringIO()
    sys.stdout = out
    sys.stderr = err
    with unittest.mock.patch('ytdl_org.postprocessor.from_title.re.match') as patch:
        from ytdl_org.postprocessor.from_title import MetadataFromTitlePP
        metadata = {}
        metadata

# Generated at 2022-06-14 18:02:18.660999
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ._common import FakeYDL
    from .common import FileDownloader
    class FakeInfoDict(dict):
        pass
    ydl = FakeYDL()
    pp = MetadataFromTitlePP(ydl, '%(title)s - %(artist)s')
    info = FakeInfoDict()
    pp.run(info)
    assert info['title'] == 'The Title'
    assert info['artist'] == 'The Artist'
    pp = MetadataFromTitlePP(ydl, '%(title)s')
    info = FakeInfoDict()
    pp.run(info)
    assert info['title'] == 'The Title'
    assert 'artist' not in info

# Method run of class MetadataFromTitlePP in case of error

# Generated at 2022-06-14 18:02:24.883515
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import Downloader

    downloader = Downloader(None)
    pp = MetadataFromTitlePP(downloader, '%(title)s - %(artist)s')
    info = {}
    info['title'] = 'My Title - My Artist'
    expected_info = {
        'title': 'My Title',
        'artist': 'My Artist'
    }
    result = pp.run(info)
    assert not result[0]
    assert result[1] == expected_info


# Generated at 2022-06-14 18:02:33.032418
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    dl = None
    info = {'title': 'Test - Example'}

    pp = MetadataFromTitlePP(dl, '%(artist)s - %(title)s')
    assert pp.run(info)[1] == {'title': 'Example', 'artist': 'Test'}

    pp = MetadataFromTitlePP(dl, '%(artist)s - %(title)s - Extras %(extras)s')
    assert pp.run(info)[1] == {'title': 'Example', 'artist': 'Test', 'extras': '- Extras'}

    pp = MetadataFromTitlePP(dl, '%(randomname)s - %(artist)s - %(title)s')

# Generated at 2022-06-14 18:02:42.107347
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Test 1
    downloader, info = {}, {'title':'Foo Bar - Foo Bar Title'}
    metadata_from_title_pp = MetadataFromTitlePP(downloader,'%(artist)s - %(title)s')
    assert metadata_from_title_pp.run(info)[1] == {'title':'Foo Bar Title', 'artist':'Foo Bar'}

    # Test 2
    downloader, info = {}, {'title':'Foo Bar - Foo Bar Title'}
    metadata_from_title_pp = MetadataFromTitlePP(downloader,'%(artist)s - %(title)s')
    assert metadata_from_title_pp.run(info)[1] == {'title':'Foo Bar Title', 'artist':'Foo Bar'}

    # Test 3
    download

# Generated at 2022-06-14 18:02:54.142255
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import time
    from ..YoutubeDL import YoutubeDL

    ydl = YoutubeDL({'quiet':True})

    # YoutubeDL's version of time.strptime does not support %z
    #time.strptime('', '')


# Generated at 2022-06-14 18:03:03.695476
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .YoutubeDL import YoutubeDL
    from .extractor.youtube import YoutubeIE
    pp = MetadataFromTitlePP(YoutubeDL(), '%(artist)s - %(title)s')
    info = {'id': '123', 'url': 'http://youtube.com/watch?v=123',
            'webpage_url': 'http://youtube.com/watch?v=123',
            'title': 'artist - title'}
    ie = YoutubeIE()
    ie.set_downloader(YoutubeDL())
    ie.extract(info)
    pp.run(info)

# Generated at 2022-06-14 18:03:12.141858
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    import tempfile
    import shutil
    import os

    titleformat = '%(artist)s - %(title)s'
    video_info = {'title': 'A Great Example'}
    video_dwnldr = None
    video_post_processors = [MetadataFromTitlePP(video_dwnldr, titleformat)]

    temp_dir = tempfile.mkdtemp(prefix='youtubedl_test_')
    cwd = os.getcwd()
    os.chdir(temp_dir)

    try:
        for pp_name, info in video_post_processors:
            if pp_name:
                args, info = pp_name.run(info)

    finally:
        os.chdir(cwd)

# Generated at 2022-06-14 18:03:25.565382
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    import tempfile
    from .common import FileDownloader
    from .extractor import gen_extractors


    # Simulate options
    class Options(object):
        def __init__(self):
            self.quiet = True
            self.forcejson = True
            self.simulate = True
            self.format = None
            self.writeinfojson = True
            self.outtmpl = '%(id)s.%(ext)s'

    def _get_test_info(title_format, title):
        class YTDLSimpleInfo(dict):
            def __init__(self, title):
                self['title'] = title
                self['id'] = '1'
                self['ext'] = 'mp4'


# Generated at 2022-06-14 18:03:31.138906
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ydl.YoutubeDL import YoutubeDL

    downloader = YoutubeDL({'format': 'bestaudio/best'})
    info = {}
    info['title'] = 'Frank van der Plank - The Sound of Silence'
    p = MetadataFromTitlePP(downloader, '%(artist)s - %(track)s')
    metadata, info = p.run(info)
    assert metadata == []
    assert info['artist'] == 'Frank van der Plank'
    assert info['track'] == 'The Sound of Silence'

    # match
    p = MetadataFromTitlePP(downloader, '%(track)s - %(artist)s')
    metadata, info = p.run(info)
    assert metadata == []
    assert info['track'] == 'Frank van der Plank - The Sound of Silence'

    # no match

# Generated at 2022-06-14 18:03:41.420991
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .youtube_dl.YoutubeDL import YoutubeDL
    class DummyYDL:
        def __init__(self):
            self.my_info_dict = {'title': 'File name'}
        def to_screen(self, msg):
            print(msg)

    ydl = DummyYDL()

    p1 = MetadataFromTitlePP(ydl, '%(title)s')
    p1.run(ydl.my_info_dict)
    assert ydl.my_info_dict['title'] is None

    p2 = MetadataFromTitlePP(ydl, '%(title)s - %(artist)s')
    p2.run(ydl.my_info_dict)
    assert ydl.my_info_dict['title'] == 'File name'
    assert ydl.my_

# Generated at 2022-06-14 18:03:49.329637
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    pp = MetadataFromTitlePP(None, '%(title)s - %(artist)s')
    info = {}

    # Test parse successful
    info['title'] = 'Youtube Title - Youtube Artist'
    [], info = pp.run(info)
    assert info['title'] == 'Youtube Title'
    assert info['artist'] == 'Youtube Artist'

    # Test parse unsuccessful
    info['title'] = 'Youtube Title - Youtube Artist'
    [], info = pp.run(info)
    assert info['title'] == 'Youtube Title'

    # Test 5.4 style titleformat
    info['title'] = 'Youtube Title - Youtube Artist'
    pp = MetadataFromTitlePP(None, '%%(title)s - %%(artist)s')
    [], info = pp.run(info)

# Generated at 2022-06-14 18:04:00.951859
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.extractor.common import InfoExtractor

    ie = InfoExtractor({})
    titleformat = '%(title)s - %(artist)s'
    mp = MetadataFromTitlePP(ie, titleformat)

    test_inputs_outputs = [
        ('Title - Artist', {'title': 'Title', 'artist': 'Artist'}),
        ('Title - Artist - Album', {'title': 'Title', 'artist': 'Artist - Album'}),
        ('Artist - Title', {'title': 'Artist - Title'}),
        ('Artist - Title - Album', {}),
    ]

    for title, expected_metadata in test_inputs_outputs:
        metadata = {'title': title}
        results = mp.run(metadata)
        assert results[1] == expected_metadata

# Generated at 2022-06-14 18:04:09.542556
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Import method here because it has dependency on common
    from youtube_dl.postprocessor import FFmpegMetadataPP


# Generated at 2022-06-14 18:04:19.413369
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import unittest2
    class TestMetadataFromTitlePP(unittest2.TestCase):
        def setUp(self):
            self.info = {
                'title': 'Title - Artist - Album',
                'artist': 'Artist',
                'album': 'Album',
                'track': 'Track',}
            self.titleformat = '%(title)s - %(artist)s - %(album)s - %(track)s'

        def test_parse_title_with_all_values(self):
            processor = MetadataFromTitlePP(None, self.titleformat)

# Generated at 2022-06-14 18:04:30.695164
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .downloader import FileDownloader
    from .common import FileDownloader
    from .common import FileDownloader
    from .common import FileDownloader, PostProcessor
    class FakeInfo(object):
        _info = {}
        def __getitem__(self, key):
            return self._info[key]
        def __setitem__(self, key, value):
            self._info[key] = unicode(value)
    info = FakeInfo()
    _downloader = FileDownloader(None)
    _downloader.to_screen = lambda s: None
    metadata_from_titlePP = MetadataFromTitlePP(_downloader, '%(title)s - %(artist)s')
    info['title'] = 'foo - bar'
    metadata_from_titlePP.run(info)
    assert info['title']

# Generated at 2022-06-14 18:04:39.160467
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    pp = MetadataFromTitlePP(None, '%(track)s - %(artist)s')
    assert pp.run({'title': 'House of the Rising Sun - Animals'}) == ([],
        {'title': 'House of the Rising Sun - Animals', 'track': 'House of the Rising Sun', 'artist': 'Animals'})
    assert pp.run({'title': 'House of the Rising Sun - Animals - YouTube'}) == ([],
        {'title': 'House of the Rising Sun - Animals - YouTube', 'track': 'House of the Rising Sun', 'artist': 'Animals'})


# Generated at 2022-06-14 18:04:50.068116
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():

    info = { 'title' : 'my title' }

    # Test 1: titleformat does not contain the pattern %(..)s
    titleformat = 'no formatting'
    pp = MetadataFromTitlePP(None, titleformat)
    info_result = pp.run(info)[1]
    assert info == info_result, (
        'Expected info: %s, obtained info: %s' % (info, info_result))

    # Test 2: titleformat contains the pattern %(..)s and it matches
    info = { 'title' : 'my artist - my title' }
    titleformat = '%(artist)s - %(title)s'
    pp = MetadataFromTitlePP(None, titleformat)
    info_result = pp.run(info)[1]

# Generated at 2022-06-14 18:05:04.150995
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import unittest

    class TestMetadataFromTitlePP(unittest.TestCase):
        def setUp(self):
            self._downloader = FakeDownloader()
            self.processor = MetadataFromTitlePP(self._downloader, "%(title)s - %(artist)s")

        def test_simple(self):
            info = {'title': 'Smells like teen spirit - Nirvana'}
            expected_info = {
                'title': 'Smells like teen spirit',
                'artist': 'Nirvana'
            }
            actual_info = self.processor.run(info)[1]
            self.assertEqual(expected_info, actual_info)

        def test_case_insensitive(self):
            info = {'title': 'Smells like teen spirit - NIRVANA'}
            expected_info

# Generated at 2022-06-14 18:05:10.847299
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    sys.path.insert(0, '../bin/')
    import youtube_dl

    class DummyOut:
        def __init__(self):
            self.content = []

        def write(self, data):
            self.content.append(data)

    dummyout = DummyOut()

    ydl = youtube_dl.YoutubeDL({'verbose': True})
    ydl.to_screen = dummyout.write

    pp = MetadataFromTitlePP(ydl, '%(title)s - %(artist)s - %(release_date)s')

    info = {
        'id': 'abcde',
        'title': 'Title - Artist - 2010'
    }

# Generated at 2022-06-14 18:05:21.585106
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    delim = ' - '
    l = 3  # length of vars

    from .YoutubeDL import YoutubeDL
    from .YoutubeDL import YoutubeDLHandler
    from .update import update_self
    from .compat import compat_urllib_request

    def _download_webpage(url, video_id, note=None, errnote=None, fatal=True):
        handler = YoutubeDLHandler()
        request = compat_urllib_request.Request(url)
        request.add_header('Cookie', 'PREF=f1=50000000; f5=30')
        opener = compat_urllib_request.build_opener(handler)

# Generated at 2022-06-14 18:05:31.605926
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FileDownloader
    from .extractor import youtube
    from youtube_dl.utils import std_headers


# Generated at 2022-06-14 18:05:43.805882
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import youtube_dl.YoutubeDL
    ydl = youtube_dl.YoutubeDL()
    pp = MetadataFromTitlePP(ydl, '%(title)s - %(artist)s')
    assert pp.run({'title': 'foo - bar'}) == ([], {'title': 'foo', 'artist': 'bar'})
    assert pp.run({'title': 'foo - bar (quux)'}) == ([], {'title': 'foo', 'artist': 'bar (quux)'})
    assert pp.run({'title': 'baz - foo - bar'}) == ([], {'title': 'baz - foo', 'artist': 'bar'})

# Generated at 2022-06-14 18:05:50.874680
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import unittest
    import sys
    import inspect
    curr_frame = inspect.currentframe()
    dummy_pp = MetadataFromTitlePP(DummyYDL(), '%(title)s_%(artist)s_%(album)s_%(track)s_%(tracknumber)s')
    assert dummy_pp.run(
        {
            'title': 'title_artist_album_track_11',
            'tracknumber': '6',
            'track': '7',
            'album': '8'
        }
    ) == ([], {'title': 'title', 'tracknumber': '11', 'track': 'track', 'album': 'album', 'artist': 'artist'})

# Generated at 2022-06-14 18:05:58.790977
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FakeYDL
    from .extractor import get_info_extractor


    class FakeInfoExtractor(object):
        def extract(self, url):
            return {
                'id': 'test123',
                'ext': 'mp4',
                'title': 'Test Video Title'
            }

    ie = FakeInfoExtractor()
    ydl = FakeYDL()

    class FakeIE(object):
        def __init__(self, ie):
            self.ie = ie
        def suitable(self, url):
            return True
        def get_info_extractor(self, url):
            return self.ie
    ydl.add_info_extractor(FakeIE(ie))


# Generated at 2022-06-14 18:06:06.499331
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    try:
        from collections import defaultdict
    except ImportError:
        # not available in python 2.5
        print('Test MetadataFromTitlePP.run(1) not available in python 2.5')
        return

    from collections import defaultdict

    def mock_download_configuration(key):
        return {
            'embedthumbnail': False,
            'writethumbnail': False,
            'writeannotations': False,
            'writeinfojson': False,
            'outtmpl': defaultdict(lambda: '%(title)s.%(ext)s',
                                   {'oformat': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'}),
        }[key]


# Generated at 2022-06-14 18:06:14.192364
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FileDownloader
    from ..utils import DateRange
    from ..compat import compat_str

    # Initialize test case environment
    downloader = FileDownloader({})
    downloader.params.update({'writethumbnail': True, 'writeannotations': True})


# Generated at 2022-06-14 18:06:25.359909
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    original_title = 'Test_title - Test_artist'

# Generated at 2022-06-14 18:06:41.796696
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    metadata_from_title = MetadataFromTitlePP(None, '%(title)s - %(artist)s')
    test_dict = {
        'title': 'Test title - Artist test',
        'uploader': 'Test uploader'
    }
    metadata_from_title.run(test_dict)
    assert test_dict['title'] == 'Test title'
    assert test_dict['artist'] == 'Artist test'
    assert test_dict['uploader'] == 'Test uploader'

# Generated at 2022-06-14 18:06:51.197461
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import pytest

    expected_info = {'title': 'title',
                     'artist': 'artist'}

    result = MetadataFromTitlePP(None, '%(artist)s - %(title)s').run(expected_info)
    assert result[1] == expected_info


    assert MetadataFromTitlePP(None, '%(artist)s - %(title)s').run({'title': 'title - artist'})[1] == expected_info
    assert MetadataFromTitlePP(None, '%(title)s - %(title)s').run({'title': 'title - title'})[1] == {'title': 'title - title', 'title': 'title'}
    assert MetadataFromTitlePP(None, '%(artist)s - %(title)s').run({'title': 'title'})

# Generated at 2022-06-14 18:07:03.434344
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # MetadataFromTitlePP._titleregex

    # test '%(title)s - %(artist)s'
    test_titleformat = '%(title)s - %(artist)s'
    test_title = 'Title - Artist'
    test_titleregex = '(?P<title>.+)\ \-\ (?P<artist>.+)'
    test_expected_metadata = {'artist': 'Artist', 'title': 'Title'}

    mp = MetadataFromTitlePP(None, test_titleformat)
    
    regex = mp.format_to_regex(test_titleformat)
    assert regex == test_titleregex

    match = re.match(regex, test_title)
    if match is None:
        assert False

    metadata = {}

# Generated at 2022-06-14 18:07:15.546207
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import make_fake_downloader
    from ..utils import parse_filesize

    downloader = make_fake_downloader('.')

    # routine to check that all info fields are filled as expected
    def check_info_fields(info, title, album='', artist='', track='', track_total='', genre='', date='', location='', filesize=0, duration=0):
        # check that info fields have expected values
        assert info['title'] == title
        assert info['album'] == album
        assert info['artist'] == artist
        assert info['track'] == track
        assert info['track_total'] == track_total
        assert info['genre'] == genre
        assert info['date'] == date
        assert info['location'] == location
        assert info['filesize'] == filesize

# Generated at 2022-06-14 18:07:27.579667
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import youtube_dl
    from .downloader import YoutubeDL
    from .extractor.generic import YoutubeIE
    from .compat import compat_urllib_request
    from .postprocessor import FFmpegMetadataPP

    # mock up a youtube-dl object
    ydl = YoutubeDL({'simulate': True, 'format': 'best'})
    ydl.add_default_info_extractors()
    ydl.add_info_extractor(YoutubeIE())

    # create fake test.mp4 file to be downloaded and parsed
    video_ids = ('uLElZ8myjZw', 'bk_IEZl9ocI')
    video_info = {}

    def _test_download_video(video_id):
        filename = 'test.mp4'

# Generated at 2022-06-14 18:07:34.862609
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Check with a regex with no group defined
    pp = MetadataFromTitlePP(None, '%(title)s-%(artist)s')
    (formats, meta) = pp.run({'title': 'Some Title - Some artist'})
    assert meta['title'] == 'Some Title'
    assert meta['artist'] == 'Some artist'
    # Check with a regex with groups defined
    pp = MetadataFromTitlePP(None, '(?P<title>.+)\-(?P<artist>.+)')
    (formats, meta) = pp.run({'title': 'Some Title - Some artist'})
    assert meta['title'] == 'Some Title'
    assert meta['artist'] == 'Some artist'
    # Check with a regex with groups defined in a string format

# Generated at 2022-06-14 18:07:43.327125
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.utils import DateRange
    from youtube_dl.extractor.common import InfoExtractor

    class TestIE(InfoExtractor):
        def _real_extract(self, url):
            return {
                'id': 'testvideoid',
                'title': '%(title)s - %(artist)s [%(date)s]',
                'upload_date': '20120417',
                'description': 'testdescription',
                'categories': ['testcategory'],
                'tags': ['testtag1', 'testtag2'],
            }

    ie = TestIE()


# Generated at 2022-06-14 18:07:53.899667
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .compat import (compat_urllib_request, compat_urllib_parse,
                         compat_urllib_error, compat_http_client)
    from .extractor import get_info_extractor

    # Test with extractor_test json file
    ie_test = get_info_extractor('test')
    ie_test._downloader = object()
    ie_test.report_warning = lambda msg: None
    ie_test.to_screen = lambda msg, *args: None

    # Create a metadata from title postprocessor
    mft_postprocessor = MetadataFromTitlePP(ie_test._downloader, '%(season)sE%(episode)s')
    assert mft_postprocessor._titleformat == '%(season)sE%(episode)s'

    # Get info from test extractor

# Generated at 2022-06-14 18:08:03.879186
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    titleformat1 = '%(title)s - %(artist)s'
    titleformat2 = '%(artist)s - %(title)s'
    titleformat3 = '%(title)s%(artist)s'
    titleformat4 = '%(title)s%(title)s - %(artist)s'

    info1 = {'title' : 'darling - atom'}
    info2 = {'title' : 'atom - darling'}
    info3 = {'title' : 'atom'}
    info4 = {'title' : 'atom - atom'}


# Generated at 2022-06-14 18:08:11.597470
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ydl.extractor.common import InfoExtractor
    video_filename = 'test video.avi'
    video_url = 'http://bla.com/bla?format=avi'
    video_title = 'title of the test video'
    video_info = dict(title=video_title)
    test_downloader = InfoExtractor(None, None)
    test_downloader._screen_file = open('/dev/null', 'w')
    test_downloader._filesystem_encoding = 'utf-8'
    test_downloader.params = dict()
    test_downloader.params['simulate'] = True
    test_downloader.params['verbose'] = False

    post_processor = MetadataFromTitlePP(test_downloader, '%(title)')