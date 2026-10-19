

# Generated at 2022-06-14 17:58:42.607420
# Unit test for method format_to_regex of class MetadataFromTitlePP
def test_MetadataFromTitlePP_format_to_regex():
    from .common import Downloader

    ydl = Downloader()
    # test one from MetadataFromTitlePP.__doc__
    print(MetadataFromTitlePP(ydl, "%(title)s - %(artist)s").format_to_regex(
        "%(title)s - %(uploader)s"))
    # test another one
    print(MetadataFromTitlePP(ydl, "%(title)s - %(artist)s").format_to_regex(
        "%(artist)s-%(title)s"))
    # test with a simple string
    print(MetadataFromTitlePP(ydl, "%(title)s - %(artist)s").format_to_regex(
        "blabla"))

if __name__ == '__main__':
    test_MetadataFromTitlePP_format

# Generated at 2022-06-14 17:58:52.218192
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FileDownloader
    from .extractor import gen_extractors
    info = {'title': 'some title [abc]'}
    downloader = FileDownloader({})
    extractor = gen_extractors(downloader)[0]
    # MetadataFromTitlePP expects the extractor to be added to the info dictionary
    info['extractor'] = extractor
    metadata_from_title_pp = MetadataFromTitlePP(downloader, '%(title)s [%(id)s]')
    expected_info = {'title': 'some title [abc]',
                     'extractor': extractor,
                     'id': 'abc'}
    assert metadata_from_title_pp.run(info) == ([], expected_info)

# Generated at 2022-06-14 17:58:58.862312
# Unit test for method format_to_regex of class MetadataFromTitlePP
def test_MetadataFromTitlePP_format_to_regex():
    pp = MetadataFromTitlePP(None, None)
    assert pp.format_to_regex('%(title)s - %(artist)s') == '(?P<title>.+)\ \-\ (?P<artist>.+)'
    assert pp.format_to_regex('%(title)s - %(artist)s - %(foo)d') == '(?P<title>.+)\ \-\ (?P<artist>.+)\ \-\ (?P<foo>.+)'

# Generated at 2022-06-14 17:59:08.985069
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ytdl.YoutubeDL import YoutubeDL
    import unittest

    class TestMetadataFromTitlePP(unittest.TestCase):
        def test_run_artist_title(self):
            ydl = YoutubeDL()
            ydl.params['verbose'] = True
            ydl.add_post_processor(MetadataFromTitlePP(ydl, "%(artist)s - %(title)s"))
            # youtube video title:
            #   Various Artists - I Just Can't Wait To Be King (From "The Lion King"/Audio Only)
            (infos, _) = ydl.extract_info('http://www.youtube.com/watch?v=xMxDS2sMwYI',
                                          download=False)

# Generated at 2022-06-14 17:59:21.516994
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():

    # When we feed MetadataFromTitlePP object with a title and a format, it returns the metadata
    # of the title that matched the format.
    class FakeInfo:
        def __init__(self, title):
            self._title = title
        def __getitem__(self, key):
            if key == 'title':
                return self._title
            else:
                raise KeyError
    assert MetadataFromTitlePP('', '%(title)s - %(artist)s').run(FakeInfo('Metadata From Title')) == ([], {'title': 'Metadata From Title'})

# Generated at 2022-06-14 17:59:30.398456
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class _MockInfoExtractor(object):
        def to_screen(self, str):
            print(str)

    # Exemple of to_screen:
    #   [fromtitle] parsed icon_url: https://www.youtube.com/yts/img/artist_fluid_120x120.png
    #   [fromtitle] parsed title: Ninho - Destin (Clip Officiel)
    #   [fromtitle] parsed track: Destin (Clip Officiel)
    #   [fromtitle] parsed artist: Ninho
    #   [fromtitle] parsed album: Destin
    #   [fromtitle] parsed album_artist: Ninho

    postprocessor = MetadataFromTitlePP(_MockInfoExtractor(),
                                        '%(artist)s - %(title)s')

# Generated at 2022-06-14 17:59:42.287176
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import unittest
    from collections import Mapping

    class DummyDownloader():
        def to_screen(self, string):
            pass

    downloader = DummyDownloader()
    postprocessor = MetadataFromTitlePP(downloader,
            '%(artist)s - %(song)s')

    info = {'track': '24', 'album': 'The Room',
            'artist': 'Perturbator', 'title': 'Sexualizer'}
    result = postprocessor.run(info)
    assert(result == ([], info))
    assert(isinstance(result, tuple))
    assert(isinstance(result[0], list))
    assert(isinstance(result[1], Mapping))

    info = {'title': 'Perturbator - Sexualizer'}
    result = postprocessor.run(info)


# Generated at 2022-06-14 17:59:52.600939
# Unit test for constructor of class MetadataFromTitlePP
def test_MetadataFromTitlePP():
    from .common import FileDownloader
    from .extractor import gen_extractors
    downloader = FileDownloader({})
    def _parseinfo(titleformat):
        ydl = FileDownloader({})
        ppost = MetadataFromTitlePP(ydl, titleformat)
        # directly set the video title without depending on YoutubeDL
        ydl.result_queue = [{
            'title': 'my_title',
            'extractor': 'my_extractor',
            'webpage_url': 'my_webpage_url',
            '_filename': 'my_filename'
        }]
        ppost.run(ydl.result_queue[0])
        return ydl.result_queue[0]

    assert 'title' not in _parseinfo('')


# Generated at 2022-06-14 17:59:57.751273
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class Info:
        pass

    info = Info()
    info.title = 'test - my title'
    info.ext = 'flv'
    downloader = Info()
    downloader.to_screen = lambda a: print(a)

    pp = MetadataFromTitlePP(downloader, '%(artist)s - %(title)s')
    pp.run(info)

    if info.artist != 'test':
        raise AssertionError('artist: %s' % info.artist)
    if info.title != 'my title':
        raise AssertionError('title: %s' % info.title)



# Generated at 2022-06-14 18:00:04.445024
# Unit test for method format_to_regex of class MetadataFromTitlePP

# Generated at 2022-06-14 18:00:10.267369
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    pass

# Generated at 2022-06-14 18:00:20.624585
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import unittest
    import os
    import sys
    import hashlib
    if sys.version_info[0] == 2:
        import urllib
    else:
        import urllib.parse as urllib
    from ..YoutubeDL import YoutubeDL
    from .common import FakeYDL
    from .test_downloader import TestDownloader

    class FakeYDL(YoutubeDL):
        def __init__(self, params, *_args, **_kwargs):
            YoutubeDL.__init__(self, params)
            self.downloaded_info_dicts = []

        def process_info(self, info_dict):
            self.downloaded_info_dicts.append(info_dict)


# Generated at 2022-06-14 18:00:32.502745
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import pytest

# Generated at 2022-06-14 18:00:43.822517
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import json
    class MockYoutubeDL():
        def __init__(self):
            self.to_screen_log = []
        def to_screen(self, msg):
            self.to_screen_log.append(msg)

    titleformat = '%(title)s - %(creator)s'
    title = 'Title - Creator'
    video_info = {
        'title': title,
        'creator': None,
        'description': 'description',
    }
    expected_video_info = {
        'title': 'Title',
        'creator': 'Creator',
        'description': 'description',
    }
    ydl = MockYoutubeDL()
    pp = MetadataFromTitlePP(ydl, titleformat)
    pp.run(video_info)
    assert expected_video_info == video_

# Generated at 2022-06-14 18:00:53.524664
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FileDownloader
    from .extractor import YoutubeIE

    # Extracting title from "%(title)s - %(artist)s"
    info = {
        'title': "Testvideo - Testartist",
        'ext': "mp4",
    }
    ie = YoutubeIE({})
    dl = FileDownloader(params={})
    pp = MetadataFromTitlePP(dl, "%(title)s - %(artist)s")
    pp.run(info)

    assert info['title'] == 'Testvideo'
    assert info['artist'] == 'Testartist'

    # Fail to extract title from "%(title)s - %(artist)s"
    info = {
        'title': "Testvideo",
        'ext': "mp4",
    }
    ie = YoutubeIE({})
    dl

# Generated at 2022-06-14 18:01:05.895068
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ytdl.YoutubeDL import YoutubeDL
    ydl = YoutubeDL()
    ydl.add_download({
        'id': 'abcd',
        'title': 'Music video - X - Song Title'
    })
    # should not raise any exception
    pp = MetadataFromTitlePP(ydl, '%(title)s - %(artist)s')
    pp.run(ydl.downloader.downloaded_info_dicts[0])
    pp = MetadataFromTitlePP(ydl, '%(title)s - %(artist)s - %(album)s')
    pp.run(ydl.downloader.downloaded_info_dicts[0])

if __name__ == '__main__':
    test_MetadataFromTitlePP_run()

# Generated at 2022-06-14 18:01:14.293323
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    import collections
    from .common import FileDownloader
    from .extractor import gen_extractors
    from .downloader import YoutubeDL


# Generated at 2022-06-14 18:01:25.529796
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ytdl_server.compat import compat_urllib_request
    from .common import FakeYoutubeDl

    downloader = FakeYoutubeDl()
    downloader.params = {'writedescription' : True, 'writeinfojson' : True}
    info = {
        'title' : 'Test title',
        'description' : 'Test description',
    }

    # Test with a simple titleformat that doesn't include any group
    # and with the title being equal to the titleformat
    titleformat = 'Video %(title)s'
    processor = MetadataFromTitlePP(downloader, titleformat)
    expected_titles = {
        'Video Test title' : True,
        'Subtitle Test title' : False,
    }
    for title in expected_titles.keys():
        info['title']

# Generated at 2022-06-14 18:01:34.424180
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FileDownloader
    dl = FileDownloader({'outtmpl': '%(id)s'})
    metadata_pp = MetadataFromTitlePP(dl, '%(artist)s - %(title)s')

    info = {'title': 'Red Hot Chili Peppers - Otherside'}
    assert metadata_pp.run(info)[1] == {
        'title': 'Otherside',
        'artist': 'Red Hot Chili Peppers'
    }

    info = {'title': 'Red Hot Chili Peppers - Otherside - YouTube'}
    assert metadata_pp.run(info)[1] == {
        'title': 'Otherside - YouTube',
        'artist': 'Red Hot Chili Peppers'
    }

    metadata_pp = MetadataFromTitlePP(dl, '%(title)s')



# Generated at 2022-06-14 18:01:45.033765
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    import youtube_dl

    class Opts(object):
        pass

    opts = Opts()

    dl = youtube_dl.YoutubeDL(opts)
    pp = MetadataFromTitlePP(dl, '%(title)s - %(artist)s')

    info = {}
    info['title'] = '54321 - 54321'
    ret, info = pp.run(info)
    assert ret == []
    assert info['title'] == '54321'
    assert info['artist'] == '54321'

    info['title'] = '54321 - 54321 - 54321'
    ret, info = pp.run(info)
    assert ret == []
    assert info['title'] == '54321 - 54321'

# Generated at 2022-06-14 18:01:59.421108
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    import json

    _TEST_CASES = [
        ('%(title)s', 'My title - My artist', {'title': 'My title', 'artist': 'My artist'}),
        ('%(title)s', 'My title', {'title': 'My title'}),
        ('%(title)s - %(artist)s', 'My title', {}),
        ('%(artist)s - %(title)s', 'My title - My artist', {}),
        ('%(artist)s - %(title)s', 'My title', {'artist': 'My title'}),
    ]

    for titleformat, title, expected_result in _TEST_CASES:
        downloader = YoutubeDL({})

# Generated at 2022-06-14 18:02:08.725509
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Arguments for MetadataFromTitlePP
    titleformat = '%(title)s_%(artist)s' # the format we want
    title_not_formatted = 'This is a video title' # the title of the video
    attributes = ['artist', 'title'] # the attributes of the video

    # Creating a downloader without the need of arguments
    class FakeDownloader():
        def __init__(self):
            self.to_screen_count = 0
        def to_screen(self, message):
            self.to_screen_count +=1
            pass
    downloader = FakeDownloader()

    # Creating an info object
    info = {}
    info['title'] = title_not_formatted


    # Creating the post processor
    pp = MetadataFromTitlePP(downloader, titleformat)

    # Test the run

# Generated at 2022-06-14 18:02:19.093903
# Unit test for method run of class MetadataFromTitlePP

# Generated at 2022-06-14 18:02:31.530110
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    ydl = YoutubeDL({})
    info_dict = {
        'title': 'The title',
        'format': 'mp4'
    }
    p = MetadataFromTitlePP(ydl, '%(title)s - %(format)s')
    expected_info_dict = {
        'title': 'The title',
        'format': 'mp4'
    }
    actual_info_dict = p.run(info_dict)
    assert expected_info_dict['title'] == actual_info_dict['title']
    assert expected_info_dict['format'] == actual_info_dict['format']

    ydl = YoutubeDL({})

# Generated at 2022-06-14 18:02:43.238487
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.extractor import YoutubeIE

    ydl = YoutubeDL({'noprogress': True, 'dry_run': True})
    ydl.add_default_info_extractors()
    ydl._ies = [YoutubeIE()]
    ydl.add_post_processor(MetadataFromTitlePP(ydl, '%(title)s - %(artist)s'))

    info = {
        'id': 'Test',
        'title': 'Test - Test Artist'
    }
    pp = ydl._pps[0]
    pp.run(info)
    assert info['id'] == 'Test'
    assert info['title'] == 'Test - Test Artist'
    assert info['artist'] == 'Test Artist'

# Generated at 2022-06-14 18:02:53.400632
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    """
    Tests for class MetadataFromTitlePP
    """
    import sys
    import ydl_opts
    import ydl_opts

    downloader = ydl_opts.FakeYdl(ydl_opts)
    pp = MetadataFromTitlePP(downloader, '%(title)s - %(artist)s')
    # test for matching title
    info1 = {'title': 'how to test - a test'}
    pp.run(info1)
    assert info1 == {'title': 'how to test - a test', 'artist': 'a test'}
    # test for not matching title
    info2 = {'title': 'how to test - a test - another test'}
    pp.run(info2)

# Generated at 2022-06-14 18:03:01.951151
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class FakeDownloader():
        def to_screen(self, s):
            print(s)

    pp = MetadataFromTitlePP(FakeDownloader(), '%(title)s - %(artist)s')
    info = {
        'title': 'This is a Title - Artist',
    }
    pp.run(info)
    assert info['title'] == 'This is a Title'
    assert info['artist'] == 'Artist'

    info = {
        'title': 'This is a Title',
    }
    pp.run(info)
    assert info['title'] == 'This is a Title'
    assert 'artist' not in info

# Generated at 2022-06-14 18:03:11.005530
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    import logging

    class FakeYDL:
        def to_screen(text):
            print('[fromtitle] ' + text)

    if sys.version_info < (3, 0):
        from urllib2 import URLError
    else:
        from urllib.error import URLError


# Generated at 2022-06-14 18:03:15.413219
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    """
    Unit test for method run of class MetadataFromTitlePP.
    This test is only run if module doctest is available.
    """
    import doctest
    if not doctest.testmod()[0] == 0:
        raise Exception('Unit test failed!')

# Generated at 2022-06-14 18:03:26.214081
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FileDownloader
    from .YoutubeDL import YoutubeDL
    from .extractor import gen_extractors
    downloader = FileDownloader(params={})
    downloader.add_info_extractor(gen_extractors()[0])
    downloader.to_screen = print
    downloader.params.update({'metafromtitle':True, 'titleformat':'%(title)s - %(artist)s'})
    pp = MetadataFromTitlePP(downloader, downloader.params['titleformat'])
    # Test a simple case
    test_url = 'http://www.youtube.com/watch?v=BaW_jenozKc'
    info_dict = YoutubeDL(downloader).extract(test_url)

# Generated at 2022-06-14 18:03:38.537439
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    info = {
        'title': 'Sample - Title',
        'artist': 'Sample Artist',
        'upload_date': '20190623',
        'comment_count': '1234',
    }
    titleformat = '%(title)s - %(artist)s'
    mp = MetadataFromTitlePP(None, titleformat)
    wanted_info = {}
    for attr in 'title', 'artist':
        wanted_info[attr] = info[attr]
    assert wanted_info == mp.run(info)[1]

# Generated at 2022-06-14 18:03:48.122243
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import os
    import tempfile
    import unittest
    import youtube_dl

    class FakeInfoDict(dict):
        pass

    class FakeYDL(object):
        def to_screen(self, msg):
            pass

    class TestMetadataFromTitlePP_run(unittest.TestCase):
        def setUp(self):
            self.ydl = youtube_dl.YoutubeDL(params={})
            self.temp_dir = tempfile.mkdtemp()
            self.info = FakeInfoDict({'title': 'Song Title - Artist Name', 'filepath': os.path.join(self.temp_dir, 'Song Title - Artist Name.mp4')})

        def tearDown(self):
            self.ydl.to_screen = lambda msg: None
            self.ydl.cache.remove()


# Generated at 2022-06-14 18:03:55.421781
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class DummyDownloader:
        def __init__(self, to_screen):
            self.to_screen = to_screen

    titleformat = '%(title)s - %(artist)s'
    info = {
        'title': 'Some title - Some artist'
    }
    pp = MetadataFromTitlePP(DummyDownloader(print), titleformat)
    pp.run(info)
    assert info['title'] == 'Some title'
    assert info['artist'] == 'Some artist'


# Generated at 2022-06-14 18:04:05.776452
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # pylint: disable=W0212
    import youtube_dl
    import youtube_dl.postprocessor

    postprocessor = MetadataFromTitlePP(youtube_dl, '%(title)s - %(artist)s')
    assert postprocessor._titleregex == r'(?P<title>.+)\ \-\ (?P<artist>.+)'

    info = {'title': 'test - a'}
    assert postprocessor.run(info) == ([], {'title': 'test', 'artist': 'a'})

    info = {'title': 'test - a\ntest b - c'}
    assert postprocessor.run(info) == ([], {'title': 'test - a', 'artist': 'test b - c'})

    info = {'title': 'test'}

# Generated at 2022-06-14 18:04:16.697504
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Arrange
    from youtube_dl.YoutubeDL import YoutubeDL
    info = {
        'title': 'foo - bar',
        'description': 'bar is a table',
        'tags': 'table,desk,chair',
    }
    ydl = YoutubeDL(params={
        'download_archive': './tests/testdata/test_archive.txt',
        'download_archive_from': 'test_archive.txt',
        'writedescription': 'True',
        'writeinfojson': 'True',
        'writethumbnail': 'True',
        'writeannotations': 'True',
    })
    ydl.add_info_extractor(None)
    pp = ydl.add_post_processor(MetadataFromTitlePP(ydl, '%(foo)s - %(bar)s'))



# Generated at 2022-06-14 18:04:25.182113
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import pytest

    class FakeDownloader(object):
        def to_screen(self, text):
            pass

    class FakeInfo(dict):
        pass

    class MetadataFromTitlePP(PostProcessor):
        def __init__(self, downloader, titleformat):
            super(MetadataFromTitlePP, self).__init__(downloader)
            self._titleformat = titleformat
            self._titleregex = (self.format_to_regex(titleformat)
                                if re.search(r'%\(\w+\)s', titleformat)
                                else titleformat)

    def run_metadatafromtitlepp_test(format, title, expected):
        downloader = FakeDownloader()
        info = FakeInfo({'title': title})
        pp = MetadataFromTitlePP(downloader, format)
       

# Generated at 2022-06-14 18:04:33.912863
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Mock for class PostProcessor
    class Downloader:
        def to_screen(self, content):
            if content == '[fromtitle] Could not interpret title of video as "foo"':
                raise AssertionError(
                    'Unexpected to_screen call with Could not interpret...')
        def to_screen(self, content):
            if content in ('[fromtitle] parsed foo: bar',
                         '[fromtitle] parsed xyz: NA'):
                pass
            else:
                raise AssertionError(
                    'Unexpected to_screen call with %s'
                    % content)

    downloader = Downloader()
    postprocessor = MetadataFromTitlePP(downloader, '%(foo)s - %(xyz)s')
    info = {'title': 'bar'}
    result = postprocessor.run(info)

# Generated at 2022-06-14 18:04:45.323372
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .utils import FakeYDL
    from .aes import aes_decrypt

    titleformat = '%(track)s - %(artist)s'
    titleformat = '%(category)s: %(track)s - %(artist)s'
    titleformat = '%(category)s/%(track)s - %(artist)s'
    titleformat = '%(category)d/%(track)d - %(artist)s'
    titleformat = '%(track)s - %(artist)s.%(ext)s'
    titleformat = '%(track)s - %(artist)s.flv'
    titleformat = '[%(category)s][%(track)s][%(ext)s]'

# Generated at 2022-06-14 18:04:55.400145
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    # titleformat = '%(title)s - %(artist)s'
    # title = 'I Feel It Coming - The Weeknd ft. Daft Punk'
    # expected = {'artist': 'The Weeknd ft. Daft Punk', 'title': 'I Feel It Coming'}
    # titleformat = '%(title)s'
    # title = 'I Feel It Coming - The Weeknd ft. Daft Punk'
    # expected = {'title': 'I Feel It Coming - The Weeknd ft. Daft Punk'}
    # titleformat = '%(artist)s'
    # title = 'I Feel It Coming - The Weeknd ft. Daft Punk'
    # expected = {'artist': 'I Feel It Coming - The Weeknd ft. Daft Punk'}
    #

# Generated at 2022-06-14 18:05:07.102753
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import dict_to_string
    from .downloader import Downloader
    from .FileDownloader import FileDownloader
    from .compat import compat_urllib_request


# Generated at 2022-06-14 18:05:29.270696
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FileDownloader
    from .utils import get_cachedir

    import os
    import tempfile


# Generated at 2022-06-14 18:05:41.460071
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from collections import namedtuple
    from youtube_dl.downloader.PostProcessor import PendingPP
    from youtube_dl.utils import encode_compat_str

    # helper method
    def _test(title, titleformat, expected_result):
        pp = MetadataFromTitlePP(FakeYDL(), titleformat)
        info = {'title': title}
        actual_result = pp.run([], info)[1]
        assert actual_result == expected_result, \
            'titleformat: %r, title: %r, expected_result: %r, actual_result: %r' \
            % (titleformat, encode_compat_str(title), expected_result, actual_result)


# Generated at 2022-06-14 18:05:50.628895
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import youtube_dl
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s',
                                'verbose': True,
                                'writesubtitles': True,
                                'writeautomaticsub': True,
                                'subtitleslangs': ['en', 'es', 'ar'],
                                })
    info = {}
    title = 'test title'
    info['title'] = title
    titleformat0 = '%(title)s'
    titleformat1 = '%(title)s - %(artist)s'
    metadatafromtitlePP0 = MetadataFromTitlePP(ydl, titleformat0)
    metadatafromtitlePP1 = MetadataFromTitlePP(ydl, titleformat1)
    # Test case 0: titleformat is '%

# Generated at 2022-06-14 18:05:58.173473
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Setup test
    import youtube_dl
    import os

    # Make sure to read the output of the application and then verify the contents
    class FakeLogger(object):
        def debug(self, msg, *args): pass
        def warning(self, msg, *args): pass
        def error(self, msg, *args): pass
        def to_screen(self, msg, *args): print(msg % args)

    def FakeDownloader(*args, **kwargs):
        return {'logger': FakeLogger()}

    # Test: valid title and format, except showing NA for artist
    expected = {'title': 'abc - def', 'artist': None, 'id': 'xyz'}

# Generated at 2022-06-14 18:06:08.977093
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FileDownloader
    downloader = FileDownloader({})
    downloader.params = {'outtmpl': '%(title)s', 'usetitle': True}
    downloader.add_info_extractor('test')

    title_format = '%(title)s song test'
    pp = MetadataFromTitlePP(downloader, title_format)

    info = {'title': 'Music video - Sunday is funday'}
    infos, info = pp.run(info)
    assert info['title'] == 'Music video'

    info = {'title': 'Music video - Sunday is funday'}
    title_format = '%(title)s - Sunday is funday'
    pp = MetadataFromTitlePP(downloader, title_format)

# Generated at 2022-06-14 18:06:21.457805
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    from collections import defaultdict
    from youtube_dl.utils import DateRange


# Generated at 2022-06-14 18:06:31.163290
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FileDownloader
    from .compat import compat_str
    from .extractor import get_info_extractor
    from .extractor import gen_extractors

    def str2infodict(fmt, title):
        info = {'url': 'http://foo/bar', 'title': title}
        pp = MetadataFromTitlePP(FileDownloader({}), fmt)
        infos, info = pp.run(info)
        return info

    def assert_title(fmt, title, exp_info):
        info = str2infodict(fmt, title)
        for field, exp_value in exp_info.items():
            assert info[field] == exp_value

    # test if all registered extractors set a value in the returned info dict
    # if they are able to extract the value out of

# Generated at 2022-06-14 18:06:36.367143
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class TestDownloader:
        @staticmethod
        def to_screen(*args, **kargs):
            pass
    class TestInfo:
        title = ''
    test_downloader = TestDownloader()
    test_info = TestInfo()

    mf_title_pp = MetadataFromTitlePP(test_downloader, '%(title)s')
    test_info.title = 'title'
    entries, info = mf_title_pp.run(test_info)
    assert (info['title'] == 'title')
    test_info.title = 'title - artist'
    entries, info = mf_title_pp.run(test_info)
    assert (info['artist'] == 'artist')

# Generated at 2022-06-14 18:06:46.130303
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    import os
    import tempfile
    with tempfile.NamedTemporaryFile(delete=False) as output:
        output.write(b'youtube-dl test video')
        output.close()
        ydl_opts = {
            'logger': YoutubeDL.std_logger(),
            'outtmpl': output.name
        }
        ydl = YoutubeDL(ydl_opts)
        pp = MetadataFromTitlePP(ydl, '%(title)s')
        ie_result = {
            'id': 'VIDEOID',
            'title': 'The Prancing Elites Project - Season 1 Episode 1'
        }

# Generated at 2022-06-14 18:06:54.219730
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.utils import DateRange
    from youtube_dl import YoutubeDL
    from datetime import datetime, timedelta
    from tests.testhelper import TestHelper

    # Create a YoutubeDL object for test purposes
    ydl = YoutubeDL(TestHelper.get_params())

    # Define the input test info (used a dictionary because it is mutable)
    info = { 'uploader': 'unknown', 'upload_date': '20140421', 'description': 'dummy description',
             'title': 'Testing title - ChannelName' }

    # Create a MetadataFromTitlePP object with a given dateformat
    dateformat = '%Y%m%d'
    titleformat = '%(title)s - %(uploader)s'
    metadata_from_title_pp = MetadataFromTitlePP(ydl, titleformat)

# Generated at 2022-06-14 18:07:29.539071
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ytdl.YoutubeDL import YoutubeDL
    class TestYDL(YoutubeDL):
        def __init__(self):
            self.to_screen_called = False
            self.to_screen_args = []

        def to_screen(self, msg):
            self.to_screen_called = True
            self.to_screen_args.append(msg)

    ydl = TestYDL()
    ydl.params['dump_single_json'] = True

    titleformat = '%(title)s %(artist)s'

# Generated at 2022-06-14 18:07:37.984076
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    """
        Test for method run
    """
    class FakeDownloader(): pass
    downloader = FakeDownloader()
    pp = MetadataFromTitlePP(downloader, '%(title)s')
    info = {}
    info['title'] = 'A Title'
    assert pp.run(info) == ([], {'title': 'A Title'})
    info['title'] = 'A Title - An Artist'
    assert pp.run(info) == ([], {'title': 'A Title - An Artist'})
    pp = MetadataFromTitlePP(downloader, '%(title)s - %(artist)s')
    assert pp.run(info) == ([], {'title': 'A Title', 'artist': 'An Artist'})

# Generated at 2022-06-14 18:07:45.974800
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    import unittest
    class MockDownloader():
        def __init__(self, to_screen_output):
            self.to_screen_output = to_screen_output

        def to_screen(self, text):
            self.to_screen_output.append(text)

    class TestCase(unittest.TestCase):

        def setUp(self):
            self.to_screen_output = []
            self.downloader = MockDownloader(self.to_screen_output)

        def test_regex_format_to_regex_converts_string_with_named_matches_to_regex(self):
            titleformat = '%(title)s - %(artist)s'

# Generated at 2022-06-14 18:07:55.402719
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    """
    This test case tests that MetadataFromTitlePP is able to extract
    metadata from the titles using regex with named groups.
    """
    from youtube_dl.downloader.PostProcessor import run_pp
    import sys

    class DummyDownloader():
        pass

    dl = DummyDownloader()

    pp_tokens = {
        '%(title)s': 'The.Beatles - Yesterday',
        '%(id)s': 'video_id',
        '%(title)s': 'Yesterday',
        '%(artist)s': 'The.Beatles'
    }


# Generated at 2022-06-14 18:08:05.508298
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import json
    from .testutils import FakeInfoExtractor
    from .extractor import YoutubeIE

    yt_ie = YoutubeIE()
    ie = FakeInfoExtractor(yt_ie)
    pp = MetadataFromTitlePP(ie, '%(artist)s: %(track)s')

    # Parse single track
    track_info = {
        'track': 'Some track',
        'artist': 'Some artist',
        'title': 'Some artist: Some track',
    }
    new_info, _ = pp.run(track_info)

    assert new_info == {
        'track': track_info['track'],
        'artist': track_info['artist'],
        'title': track_info['title'],
    }

    # Parse single track without regex
    pp = MetadataFromTitlePP

# Generated at 2022-06-14 18:08:13.608439
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    #
    # Test method MetadataFromTitlePP.run
    #
    import sys
    import unittest
    reload(sys)
    sys.setdefaultencoding('utf-8')


# Generated at 2022-06-14 18:08:22.183857
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.downloader.common import FileDownloader

    def my_exit():
        pass

    def writeinfo(message):
        return

    pp = MetadataFromTitlePP(FileDownloader({}),'%(title)s - %(artist)s')
    pp.to_screen = writeinfo
    pp.report_error = writeinfo
    pp.trouble = writeinfo
    pp.report_warning = writeinfo
    pp.exit = my_exit
    assert pp.run({'title':'Something - Something Else'}) == ([], {'title':'Something - Something Else', 'artist':'Something Else'})
    assert pp.run({'title':'Something -'}) == ([], {'title':'Something -'})

# Generated at 2022-06-14 18:08:33.518497
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class MockDownloader():
        def __init__(self):
            self._messages = []
        def to_screen(self, msg):
            self._messages.append(msg)
    class MockInfo():
        def __init__(self, title):
            self.title = title
        def __getitem__(self, key):
            return self.__dict__[key]
        def __setitem__(self, key, value):
            self.__dict__[key] = value
        def __contains__(self, key):
            return key in self.__dict__
        def __repr__(self):
            return '<MockInfo: %s>' % self.__dict__

    titleformat = r'%(title)s\ -\ %(artist)s'