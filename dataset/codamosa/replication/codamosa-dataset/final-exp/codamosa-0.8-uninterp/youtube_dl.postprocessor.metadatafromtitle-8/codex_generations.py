

# Generated at 2022-06-14 17:58:39.839768
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FileDownloader
    from .extractor import gen_extractors
    from .compat import compat_str
    entry = {'title': 'Video title'}
    info = {}
    pp = MetadataFromTitlePP(FileDownloader({}), '%(title)s')
    expected_info = {'title': 'Video title'}
    pp.run(entry)
    assert expected_info == entry

# Unit tests for method format_to_regex of class MetadataFromTitlePP
# depends on test_run

# Generated at 2022-06-14 17:58:50.628684
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .downloader import Downloader
    from .extractor import gen_extractors


# Generated at 2022-06-14 17:58:59.163310
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class FakeDownloader:
        def to_screen(self, msg):
            pass
    fakeDownloader = FakeDownloader()

    # test with a regex without capturing groups
    metadataFromTitlePP = MetadataFromTitlePP(fakeDownloader, '%(artist)s - %(title)s')
    videoInfo = {'title': 'Anime - Name of Song'}
    metadataFromTitlePP.run(videoInfo)
    assert videoInfo.get('title') == 'Name of Song'
    assert videoInfo.get('artist') == 'Anime'

    # test with a regex with capturing groups
    metadataFromTitlePP = MetadataFromTitlePP(fakeDownloader, '%(title)s - %(artist)s')
    videoInfo = {'title': 'Name of Song - Anime'}

# Generated at 2022-06-14 17:59:09.204196
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():

    from collections import namedtuple
    from unittest import TestCase
    from unittest.mock import Mock
    from youtube_dl_server.utils.downloader import downloader

    test_info = {
        'title': 'A song - An artist',
        'uploader': 'An uploader'
    }

    # class FakeConfig(dict):
    #     def __init__(self, postprocessing):
    #         self.postprocessing = postprocessing

    # class FakeArgs(dict):
    #     def __init__(self, titleformat):
    #         self.titleformat = titleformat

    FakeYDL = namedtuple('FakeYDL', ['params'])


# Generated at 2022-06-14 17:59:21.282251
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import ytdl_config
    import ytdl_postprocessor

    ytdl = ytdl_config.YtdlFakeYoutubeDL(
        ytdl_postprocessor._plugins.__dict__)
    pp = MetadataFromTitlePP(ytdl, '%(title)s - %(artist)s')

    info = dict(title='blah')
    pp.run(info)
    assert info == dict(title='blah')

    info = dict(title='foo - bar')
    pp.run(info)
    assert info == dict(title='foo - bar', artist='bar')

    info = dict(title='foo - bar - baz')
    pp.run(info)
    assert info == dict(title='foo - bar - baz', artist='bar')

# Generated at 2022-06-14 17:59:30.095635
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    assert MetadataFromTitlePP.run(MetadataFromTitlePP(None, '%(title)s'),
                                   {'title': 'test'}) == ([], {'title': 'test'})
    assert MetadataFromTitlePP.run(MetadataFromTitlePP(None, '%(title)s - %(artist)s'),
                                   {'title': 'test - test'}) == ([], {'title': 'test - test',
                                                                     'artist': 'test'})
    assert MetadataFromTitlePP.run(MetadataFromTitlePP(None, '%(title)s -%(artist)s'),
                                   {'title': 'test- test'}) == ([], {'title': 'test- test',
                                                                     'artist': 'test'})

# Generated at 2022-06-14 17:59:41.895879
# Unit test for method format_to_regex of class MetadataFromTitlePP

# Generated at 2022-06-14 17:59:52.265277
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    import os

    # Init the downloader
    downloader = YoutubeDL(params={'outtmpl': 'test.%(ext)s'})
    # Creating a video info objet
    video_info = {'title': 'Bruno Mars - Grenade [OFFICIAL VIDEO]'}
    # Creating a MetadataFromTitlePP object
    pp = MetadataFromTitlePP(downloader, '%(artist)s - %(track)s')
    # Testing run with a metadata that can be parsed
    assert pp.run(video_info) == ([], {'title':'Bruno Mars - Grenade [OFFICIAL VIDEO]',
                                       'artist': 'Bruno Mars',
                                       'track': 'Grenade'})
    # Testing run with a metata that cannot be parsed

# Generated at 2022-06-14 17:59:57.074512
# Unit test for constructor of class MetadataFromTitlePP
def test_MetadataFromTitlePP():
    # Test1: %(..)s expression in titleformat
    from youtube_dl.YoutubeDL import YoutubeDL
    youtubeDL = YoutubeDL({})

    test_titleformat = '%(title)s - %(artist)s'
    test_titleregex = r'(?P<title>.+)\ \-\ (?P<artist>.+)'
    mftpp = MetadataFromTitlePP(youtubeDL, test_titleformat)
    assert mftpp._titleformat == test_titleformat
    assert mftpp._titleregex == test_titleregex

    # Test2: Non-%(..)s expression in titleformat
    test_titleformat = '%(title)s - %(artist)s'
    test_titleregex = test_titleformat

# Generated at 2022-06-14 18:00:08.598426
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .downloader import FileDownloader
    from .extractor import GenYoutubeIE
    from .common import FileDownloader
    from .compat import compat_etree_fromstring
    from .extractor import YoutubeIE
    from .postprocessor import FFmpegMetadataPP

    downloader = FileDownloader()
    downloader.params.update({
        'format': 'best',
        'quiet': True,
    })

    info = {}
    ie = YoutubeIE(downloader)

# Generated at 2022-06-14 18:00:21.053567
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    """
    Unit test for method run of class MetadataFromTitlePP
    """
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.utils import DateRange
    dl = YoutubeDL({'writedescription': True,
                    'dates': DateRange('20150801', '20150831')})
    dl.params['outtmpl'] = '%(title)s-%(uploader)s-%(upload_date)s'

    pp = MetadataFromTitlePP(dl, '%(title)s - %(uploader)s')

    info = {'title': 'Mozart - Symphony No. 40'}
    pp.run(info)

# Generated at 2022-06-14 18:00:29.986467
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    import json

    obj = MetadataFromTitlePP(YoutubeDL({}), '%(title)s - %(artist)s -')
    info = {'title': 'Beautiful Liar - Beyoncé - Shakira'}
    #test1 = obj.run(info)
    #test1 = obj.run(dict(info))

    test2 = obj.run(dict(info))
    #print json.dumps(info)

# Generated at 2022-06-14 18:00:30.877599
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    pass


# Generated at 2022-06-14 18:00:43.311749
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Test method run of class MetadataFromTitlePP

    # create a downloader
    downloader = None

    # create a PP
    pptype = MetadataFromTitlePP
    pp = pptype(downloader, '%(title)s - %(artist)s')

    # test on several strings

# Generated at 2022-06-14 18:00:53.352700
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    downloader = None
    titleformat = None
    metadata_from_title = MetadataFromTitlePP(downloader, titleformat)

    class ParsedInfo:
        def __init__(self, title, artist, default_key):
            self.title = title
            self.artist = artist
            self.default_key = default_key
            self.extra_attributes = {}
        def __setitem__(self, key, value):
            setattr(self, key, value)

    parsed_info = ParsedInfo(
        'Song title - Band name',
        'Band name',
        'Default value')
    # Execute method
    metadata_from_title.run(parsed_info)
    # Test
    assert parsed_info.title == 'Song title'
    assert parsed_info.artist == 'Band name'


# Generated at 2022-06-14 18:01:06.189419
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    """
    Tests result of MetadataFromTitlePP().run with different input data.
    """
    assert MetadataFromTitlePP('', '').run({}) == ([], {})
    inputs = [{'title': 'hello world - title'}, {'title': 'hello world - title - artist'}]
    outputs = [([], {'title': 'hello world', 'titleext': 'title'}), ([], {'title': 'hello world', 'titleext': 'title', 'artist': 'artist'})]
    for item in zip(inputs, outputs):
        assert MetadataFromTitlePP('', '%(title)s - %(titleext)s').run(item[0]) == item[1]
        assert MetadataFromTitlePP('', '%(title)s - %(titleext)s - %(artist)s').run

# Generated at 2022-06-14 18:01:13.462719
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    # Mock a youtube-dl instance
    ydl = YoutubeDL({'postprocessors': [{
        'key': 'MetadataFromTitle',
        'titleformat': '%(title)s [%(author)s]'
    }]})
    # Mock download_result
    dl_res = {'title': 'Foo Bar [Author]'}
    pp_res = ydl.postprocessor.run(dl_res)
    assert pp_res[1] is dl_res
    assert pp_res[1] == {
        'title': 'Foo Bar [Author]',
        'author': 'Author'
    }

# Generated at 2022-06-14 18:01:24.949525
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FileDownloader
    from .extractor import YoutubeIE
    from .utils import DateRange
    from .compat import compat_str

    try:
        import json
    except ImportError:
        import simplejson as json

    # pylint:disable=too-many-locals
    # pylint:disable=protected-access

    # fake downloader

# Generated at 2022-06-14 18:01:33.018657
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import youtube_dl
    test_video_title = 'Video title - Artist (Track #1) [Album]'

    pp = MetadataFromTitlePP(youtube_dl.YoutubeDL(),
                             '%(title)s - %(artist)s (%(track)s) [%(album)s]')
    info = {'title': test_video_title}

    # Test if run return the correct Metadata
    assert pp.run(info) == ([], {'title': test_video_title, 'artist': 'Artist',
        'track': '#1', 'album': 'Album'})

# Generated at 2022-06-14 18:01:44.891568
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import os
    import tempfile
    import ydl_info
    from .common import FileDownloader
    from .extractor import gen_extractors

    def extract_info(title):
        with tempfile.NamedTemporaryFile(delete=False) as tmpfile:
            os.unlink(tmpfile.name)
        downloader = FileDownloader({})
        downloader.add_info_extractor(gen_extractors())
        downloader.add_post_processor(MetadataFromTitlePP(downloader,
                                      titleformat))
        downloader.to_stdout = lambda *x: None
        return downloader.extract_info(ydl_info.YoutubeIE.ie_key(),
                                       'https://www.youtube.com/watch?v=id',
                                       {'title': title})

   

# Generated at 2022-06-14 18:02:01.735404
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    import tempfile
    import youtube_dl.version
    sys.modules['pycryptodomex'] = sys.modules['Crypto']
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.extractor.youtube import YoutubeIE


    def _mocked_downloader_to_screen(self, message):
        if 'parsed' in message:
            print(message)
    YoutubeDL.to_screen = _mocked_downloader_to_screen

    ydl_opts = {}
    ydl = YoutubeDL(ydl_opts)
    ydl.add_default_info_extractors()
    ie = YoutubeIE(ydl)

    # Test with a pattern that has named groups
    temp_file = tempfile.NamedTemporaryFile(delete=False)

# Generated at 2022-06-14 18:02:04.435778
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    pass


# Generated at 2022-06-14 18:02:13.022412
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .utils import prepare_mock_downloader
    from .youtube import YoutubeDL

    ydl = YoutubeDL(prepare_mock_downloader({
        'title': 'Foo - Bar'
    }))

    pp = MetadataFromTitlePP(ydl, '%(artist)s - %(title)s')
    metadata, unused_info = pp.run({
        'title': 'Foo - Bar'
    })

    assert metadata == []
    assert unused_info == {
        'artist': 'Foo',
        'title': 'Bar',
    }

# Generated at 2022-06-14 18:02:21.949693
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import youtube_dl
    import os

    # test on titleformat '%(artist)s-%(track)s'
    ydl = youtube_dl.YoutubeDL() # with default options
    ydl.add_post_processor(MetadataFromTitlePP(ydl, '%(artist)s-%(track)s'))
    info = {'title':'Queen-Bohemian Rhapsody'}
    ydl.post_process([], info)
    assert info['artist'] == 'Queen'
    assert info['track'] == 'Bohemian Rhapsody'

    # test on titleformat '%(track)s by %(artist)s'
    ydl = youtube_dl.YoutubeDL() # with default options

# Generated at 2022-06-14 18:02:32.666737
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import copy
    import youtube_dl

    def test_sample(titleformat, info, expected_info):
        # create a new title object
        pp = MetadataFromTitlePP(
            youtube_dl.YoutubeDL(),
            titleformat
        )

        # test the method
        unused_info_dicts, result_info_dict = pp.run(copy.copy(info))

        # check the result
        assert result_info_dict == expected_info

    #
    # Test code
    #

    info_dict = {
        'title':'This-is a test --- !@#$%^&*()',
        'id': 'testvideo'
    }

    # test with simple format string
    titleformat = '%(title)s'
    expected_info = copy.copy(info_dict)
    expected_info

# Generated at 2022-06-14 18:02:42.670859
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Create a MetadataFromTitlePP object
    t = MetadataFromTitlePP(None, '%(title)s - %(artist)s')

    # Create a test info dict
    info = {
        'title': 'Test Title - Test Artist',
        'uploader': None,
        'upload_date': None
    }

    # Execute the run method and check if the expected info dict is returned
    # and the title, artist, uploader and upload_date are parsed
    assert t.run(info)[1] == {
        'title': 'Test Title',
        'artist': 'Test Artist',
        'uploader': None,
        'upload_date': None
    }

# Generated at 2022-06-14 18:02:49.585812
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    downloader = Downloader({})
    downloader.to_screen = lambda x: x
    pp = MetadataFromTitlePP(downloader, '%(title)s - %(artist)s')
    info = {'title': 'hello - world', 'upload_date': '20001201'}
    assert pp.run(info)[1]['artist'] == 'world'

# Generated at 2022-06-14 18:03:01.908473
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    """
    Test for method run of class MetadataFromTitlePP
    """

    # Initialization of test variables
    # (instantiate objects with default test arguments)
    test_metadata_from_titlePP = MetadataFromTitlePP(
        'test_youtubeDL', '%(title)s - %(artist)s')

    # Define test variables
    # (construct test arguments to be used in test)

    # Define expected test results
    expected_output = (
        '[fromtitle] parsed title: Title\n'
        '[fromtitle] parsed artist: Artist\n'
        '[]\n'
        '{\'title\': \'Title\', \'artist\': \'Artist\'}')

    # Initialize test method and perform test
    test_input = {}
    test_input['title'] = 'Title - Artist'
   

# Generated at 2022-06-14 18:03:10.971394
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.utils import DateRange
    from youtube_dl.postprocessor.ffmpeg import FFmpegMetadataPP
    from collections import Counter
    import datetime

    testvid = "https://www.youtube.com/watch?v=MqSZ5mWHbLA"

# Generated at 2022-06-14 18:03:22.219550
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ydl.postprocessor import PostProcessor
    # Unit test class that implements abstract class PostProcessor
    class TestPostProcessor(PostProcessor):
        def __init__(self):
            self.in_out = {}
            self.out_in = {}

        def run(self, info):
            return self.in_out[info], self.out_in[info]

        def add_test_mapping(self, in_info, out_info):
            self.in_out[in_info] = out_info
            self.out_in[out_info] = in_info

    tpp = TestPostProcessor()

# Generated at 2022-06-14 18:03:34.785852
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import tempfile
    filename = tempfile.mkstemp(suffix='.tmp')[1]
    print(filename)
    from .extractor import FileDownloader
    downloader = FileDownloader({'outtmpl': filename})
    processor = MetadataFromTitlePP(downloader, '%(title)s-%(artist)s')
    info = {'title': 'This is Title-byArtist'}
    processor.run(info)
    assert info == {'title': 'This is Title-byArtist',
                    'artist': 'byArtist'}

# Generated at 2022-06-14 18:03:46.670179
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Input
    from youtube_dl.downloader import Downloader
    from youtube_dl.utils import FileDownloader
    from youtube_dl.postprocessor import FFmpegMetadataPP
    downloader = Downloader(FileDownloader())
    titleformat = '%(title)s - %(artist)s'
    titleregex  = '(?P<title>.+)\ \-\ (?P<artist>.+)'
    postprocessor = MetadataFromTitlePP(downloader, titleformat).run
    information = { 'title': 'Could Be Mine - Guns N\' Roses' }

    # Expected output
    information_expected = {
        'title': 'Could Be Mine',
        'artist': 'Guns N\' Roses',
    }

    # Test
    result = postprocessor(information)

    # Compare results
    assert information == information_expected

# Generated at 2022-06-14 18:03:57.844994
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    downloader = object()
    pp = MetadataFromTitlePP(downloader, "%(title)s-%(artist)s")

    # Title format regular expression does not contain any named group
    # Thus, title and artist are expected to be None in the output
    info = {'title': "Test title"}
    title, info = pp.run(info)

    assert info['title'] == "Test title"
    assert info['artist'] is None, 'Expected artist to be None'
    assert title == [], 'Expected empty list'

    # Title format regular expression contains named group for artist
    # Thus, title and artist are expected to have expected value in the output
    info = {'title': "Test title-Test artist"}
    title, info = pp.run(info)

    assert info['title'] == "Test title"
    assert info

# Generated at 2022-06-14 18:04:09.533501
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import os
    from .common import YoutubeDL
    from .extractor import gen_extractors
    from .utils import DateRange

    def _test_run(title, titleformat, expected):
        ydl = YoutubeDL({'usenetrc': False, 'quiet': True, 'forcejson': True,
            'logger': YoutubeDL.logger_class('error', 'error')})
        gen_extractors(ydl)
        pp = MetadataFromTitlePP(ydl, titleformat)
        d = {
            'id': 'dummyid',
            'thumbnail': 'dummyurl',
            'title': title,
            'upload_date': '20130806',
            'uploader': 'dummyuploader',
            'uploader_id': 'dummyuploaderid'
        }
        # run

# Generated at 2022-06-14 18:04:19.373997
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    pp = MetadataFromTitlePP(None, '%(artist)s-%(title)s')

    info = {'title': 'Testing - Test123'}
    assert (pp.run(info)[1]
            == {'title': 'Testing - Test123', 'artist': 'Testing'})

    info = {'title': 'Testing - Test123 - Test'}
    assert (pp.run(info)[1]
            == {'title': 'Testing - Test123 - Test', 'artist': 'Testing'})

    info = {'title': 'Testing - Test123 - Test - Test'}
    assert (pp.run(info)[1]
            == {'title': 'Testing - Test123 - Test - Test', 'artist': 'Testing'})

    info = {'title': 'Testing Test123 Test'}

# Generated at 2022-06-14 18:04:30.653053
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.utils import dict_representation
    from youtube_dl.YoutubeDL import YoutubeDL
    from collections import namedtuple

    def s(*args):
        print(args)

    class FakeDownloader(YoutubeDL):
        def __init__(self):
            super(FakeDownloader, self).__init__()
            self.toscreen_file = namedtuple(
                'toscreen_file',
                ['write', 'writelines'])
            self.toscreen_file.write = s

        def to_screen(self, msg):
            self.toscreen_file.writelines(map(self._print_message, msg.splitlines()))

    mp = MetadataFromTitlePP(None, '%(title)s-%(artist)s')
    mp._downloader = FakeDownloader

# Generated at 2022-06-14 18:04:41.091788
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Without regexes
    info = {
        'title': 'Title artist',
    }
    pp = MetadataFromTitlePP(None, '%(title)s %(artist)s')
    _, newinfo = pp.run(info)
    assert newinfo['title'] == 'Title'
    assert newinfo['artist'] == 'artist'
    # With regexes
    info = {
        'title': 'Title artist',
    }
    pp = MetadataFromTitlePP(None, '%(title)s %(artist)s')
    _, newinfo = pp.run(info)
    assert newinfo['title'] == 'Title'
    assert newinfo['artist'] == 'artist'
    # Without regexes but with non-matching title
    info = {
        'title': 'Title - artist',
    }


# Generated at 2022-06-14 18:04:51.836963
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import ydl_opts
    from .extractor.youtube import YoutubeIE
    # Generate info dictionary that would result from extracting
    # the meta-data on a video named
    # 'Example Title - Artist Name [YouTube]'

# Generated at 2022-06-14 18:05:02.942056
# Unit test for method run of class MetadataFromTitlePP

# Generated at 2022-06-14 18:05:11.257636
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():

    info = {'title': ''}
    expected = ([], {})

    titleformat = '%(id)s-%(len)s'
    titleregex = '(?P<id>.+)-(?P<len>.+)'

    # Test 1
    downloader, metadata_from_titlepp = get_instance(titleformat)
    info['title'] = '123456-012345'
    expected = ([], {'id': '123456', 'len': '012345'})
    assert expected == metadata_from_titlepp.run(info)

    # Test 2
    downloader, metadata_from_titlepp = get_instance(titleformat)
    info['title'] = '123456-0123456'
    expected = ([], {'id': '123456', 'len': '0123456'})
   

# Generated at 2022-06-14 18:05:29.898126
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.postprocessor import PostProcessor
    from youtube_dl.compat import compat_merge_dicts

    class TestPP(PostProcessor):
        def run(self, info):
            return [], info

    test_pp = MetadataFromTitlePP(TestPP(None), '%(title)s - %(artist)s')
    info = {
        'title': 'my title - my artist',
        'webpage_url': 'http://myurl.com',
        }
    titles, parsed_info = test_pp.run(info)
    assert parsed_info == compat_merge_dicts(info, {'title': 'my title', 'artist': 'my artist'})


# Generated at 2022-06-14 18:05:42.171458
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # init MetadataFromTitlePP
    downloader = None
    titleformat = '%(title)s - %(artist)s'
    metadataFromTitlePP = MetadataFromTitlePP(downloader, titleformat)

    # test with invalid title format
    titleformat = '%(title)s - unknown'
    metadataFromTitlePP._titleregex = metadataFromTitlePP.format_to_regex(titleformat)
    info = {'title': 'test title'}
    result = metadataFromTitlePP.run(info)
    assert len(result[1]) == 1           # result[1] is info
    assert 'title' in result[1]
    assert result[1]['title'] == 'test title'

    # test with valid title format and title
    title = 'rocking all over the world - Status Quo'
    info

# Generated at 2022-06-14 18:05:49.795002
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class MockedYDL:
        def __init__(self):
            self.to_screen = self.to_screen_impl
        def to_screen_impl(self, msg):
            print(msg)

    pp = MetadataFromTitlePP(MockedYDL(), '%(title)s - %(artist)s')
    assert pp._titleregex == '(?P<title>.+)\ \\-\ (?P<artist>.+)'
    info = { 'title': 'Zaalig - De Mens' }
    pp.run(info)
    assert info == { 'title': 'Zaalig', 'artist': 'De Mens' }



# Generated at 2022-06-14 18:05:56.117326
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    """
    Test for method run of class MetadataFromTitlePP
    """
    downloader = DummyYDL()
    mp = MetadataFromTitlePP(downloader, '%(title)s - %(artist)s')
    info = {
        'title': 'This is a title',
        'duration': '10:00'
    }
    res, info = mp.run(info)
    assert 'This is a title' in info['title']
    assert 'This is a title' in info['artist']
    assert '10:00' == info['duration']


# Generated at 2022-06-14 18:06:04.824211
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    import pytest
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.compat import compat_str
    from .common import FakeYDL

    # Test 1
    ydl = FakeYDL()
    ydl.process_info = {'title': 'testing :)'}
    pp = MetadataFromTitlePP(ydl, '%(title)s')
    results = pp.run(ydl.process_info)
    assert results[1]['title'] == 'testing :)'

    # Test 2
    ydl = FakeYDL()
    ydl.process_info = {'title': 'test with percent %'}
    pp = MetadataFromTitlePP(ydl, '%(title)s')
    results = pp.run(ydl.process_info)

# Generated at 2022-06-14 18:06:13.337451
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL

    DL = YoutubeDL({'writedescription': True, 'writeinfojson': True})
    DL.add_post_processor(MetadataFromTitlePP(DL, '%(artist)s - %(title)s'))

    info = {'title': 'Artist - Title'}
    [], info = DL._post_processors[0].run(info)
    assert info['artist'] == 'Artist'
    assert info['title'] == 'Title'

    info = {'title': 'Artist - Title   '}
    [], info = DL._post_processors[0].run(info)
    assert info['artist'] == 'Artist'
    assert info['title'] == 'Title'

    info = {'title': 'Artist'}
    [], info = DL._post_process

# Generated at 2022-06-14 18:06:24.570121
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class Downloader():
        def to_screen(self, msg):
            print("\n[fromtitle] " + msg)

    # Test checks if method run of class MetadataFromTitlePP
    # can handle empty strings
    titleRegex = r'(?P<title1>.*) - (?P<title2>.*)'
    titleFormat = '%(title1)s - %(title2)s'
    title = ''
    pp = MetadataFromTitlePP(None, titleFormat)
    info = {'title': title}
    expected = {}
    received = pp.run(info)
    assert not received

    # Test checks if method run of class MetadataFromTitlePP
    # finds all groups defined in titleFormat
    title = 'Final Fantasy - VI'
    pp = MetadataFromTitlePP(None, titleFormat)

# Generated at 2022-06-14 18:06:32.363488
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import youtube_dl
    from youtube_dl.postprocessor.compat import compat_str
    ydl = youtube_dl.YoutubeDL({})
    pp = MetadataFromTitlePP(ydl, u'%(artist)s - %(track)s')

    # test valid title
    info = {'title': u'Abba - Money Money Money'}
    pp.run(info)
    assert info['artist'] == 'Abba'
    assert info['track'] == 'Money Money Money'

    # test invalid title
    info = {'title': u'Abba'}
    pp.run(info)
    assert 'artist' not in info
    assert 'track' not in info



# Generated at 2022-06-14 18:06:43.272970
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    mp = MetadataFromTitlePP(None, '%(artist)s - %(title)s')

    # Test with correct and incorrect input title
    for i in [('vocaloid - nadeshiko',
               {'artist': 'vocaloid', 'title': 'nadeshiko'}),
              ('vocaloid - nadeshiko.mp3',
               {'artist': 'vocaloid', 'title': 'nadeshiko.mp3'}),
              ('nadeshiko', {})]:
        assert mp.run({'title': i[0]})[1] == i[1]

    # Test with format without parentheses
    mp = MetadataFromTitlePP(None, 'vocaloid - %(title)s')

# Generated at 2022-06-14 18:06:52.372451
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    def run_with_title(title):
        postprocessor = MetadataFromTitlePP(None, '%(title)s - %(artist)s')
        info = {'title': title}
        return postprocessor.run(info)

    # testcase: title matches exactly -> attributes title and artist
    info = run_with_title('Strawberries and Cream - Zara Larsson')
    assert 'title' in info[1] and info[1]['title'] == 'Strawberries and Cream'
    assert 'artist' in info[1] and info[1]['artist'] == 'Zara Larsson'

    # testcase: title does not match -> no new attributes
    info = run_with_title('Strawberries and Cream')
    assert 'title' not in info[1]
    assert 'artist' not in info[1]


# Generated at 2022-06-14 18:07:21.657273
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    downloader = object()

    valid_fmt = '%(title)s - %(artist)s'
    valid_regex = '(?P<title>.+)\ \-\ (?P<artist>.+)'
    pp = MetadataFromTitlePP(downloader, valid_fmt)
    assert pp._titleregex == valid_regex

    invalid_fmt = '%(title)s -- %(artist)s'
    invalid_regex = valid_fmt # no regex in this case
    pp = MetadataFromTitlePP(downloader, invalid_fmt)
    assert pp._titleregex == invalid_regex

    info = {'title': 'This is a title'}
    res, info = pp.run(info)
    assert len(res) == 0

# Generated at 2022-06-14 18:07:32.169984
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.downloader import MockYoutubeDL
    from youtube_dl.compat import compat_str


# Generated at 2022-06-14 18:07:40.903373
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FileDownloader
    from .YoutubeDL import YoutubeDL

    info = {'title': 'Video title - Artist'}
    titleformat = '%(title)s - %(artist)s'

    class FakeYoutubeDL(YoutubeDL):
        def to_screen(self, msg):
            self._screen_msg = msg

    downloader = FileDownloader(FakeYoutubeDL(), {})
    pp = MetadataFromTitlePP(downloader, titleformat)
    output, info = pp.run(info)
    assert info['title'] == 'Video title'
    assert info['artist'] == 'Artist'
    assert downloader._screen_msg == (
        '[fromtitle] parsed title: Video title'
        '\n[fromtitle] parsed artist: Artist')



# Generated at 2022-06-14 18:07:44.914360
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class Downloader:
        def to_screen(self, *args, **kargs):
            pass

    pp = MetadataFromTitlePP(Downloader(), '%(title)s - %(artist)s')
    info = {'title': 'Song Title - Artist Name'}
    pp.run(info)

    assert info == {'title': 'Song Title', 'artist': 'Artist Name'}

# Generated at 2022-06-14 18:07:54.745003
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # pylint: disable=W0612
    import sys
    downloader = sys
    # pylint: enable=W0612
    pp = MetadataFromTitlePP(downloader, '%(artist)s - %(song)s')
    info = {
        'title': 'Abba - Gimme gimme gimme',
        '_filename': 'Abba - Gimme gimme gimme.mp3',
        }
    pp.run(info)
    assert info['artist'] == 'Abba'
    assert info['song'] == 'Gimme gimme gimme'
    assert info['title'] == 'Abba - Gimme gimme gimme'
    assert info['_filename'] == 'Abba - Gimme gimme gimme.mp3'



# Generated at 2022-06-14 18:08:04.814876
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # instance of info to test
    info = {'title': 'Python 101 - Episode 1'}
    # first test instanciation of MetadataFromTitlePP
    x = MetadataFromTitlePP("", "%(title)s - %(episode)s %(episode_number)s")
    assert x._titleformat == "%(title)s - %(episode)s %(episode_number)s"
    assert x._titleregex == r'(?P<title>.+)\ \-\ (?P<episode>.+)\ (?P<episode_number>.+)'
    # testing run method of class MetadataFromTitlePP
    info = x.run(info)[1]
    # test if the title is extracted and assingted to the right field
    assert info['title'] == 'Python 101'
    assert info['episode'] == 'Episode'

# Generated at 2022-06-14 18:08:12.517612
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    import pytest

    class DummyYDL(object):
        def to_screen(self, msg):
            sys.stderr.write(msg + '\n')

    class DummyPP(MetadataFromTitlePP):
        def __init__(self, downloader, titleformat):
            super(DummyPP, self).__init__(downloader, titleformat)

    dl = DummyYDL()
    pp = DummyPP(dl, '%(title)s - %(artist)s')

    info = {'_filename': 'The_Video_Title.mp4', 'title': 'The Video Title'}
    files, info = pp.run(info)
    assert info['title'] == 'The_Video_Title'
    assert info['artist'] == None
    assert len(files) == 0

# Generated at 2022-06-14 18:08:20.874608
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    downloader = type('FakeYDL', (object,), {
        'to_screen': lambda *args: sys.stdout.write(' '.join(args[1:]) + '\n'),
    })()
    pp = MetadataFromTitlePP(downloader, '%(artist)s - %(title)s')
    info = {
        'title': 'Foo - Bar',
        'extractor': 'Foo',
        'webpage_url': 'https://www.youtube.com/watch?v=BAr',
    }
    # The only info key that should remain unchanged is extractor.
    assert len(pp.run(info)[1]) == 1
    assert info['extractor'] == 'Foo'

# Generated at 2022-06-14 18:08:29.029985
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    """
    This is a unit test method for method run of class MetadataFromTitlePP. It
    assumes that the method works on a string, where the regular expression
    matches the string, and a blank map object is passed. It tests whether the
    method outputs a blank array, and the map object contains the parsed
    results. This method takes the value of the unit test method as the
    argument. If the returned array of strings and map object in this method
    are as required, it will return True. Otherwise it will return False.
    """
    from ytdl_pp.postprocessor import PostProcessor
