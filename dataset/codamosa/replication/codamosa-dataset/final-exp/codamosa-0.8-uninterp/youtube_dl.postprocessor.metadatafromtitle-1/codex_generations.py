

# Generated at 2022-06-14 17:58:38.561945
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class test_downloader():

        def __init__(self):
            self.to_screen_buffer = []

        def to_screen(self, msg):
            self.to_screen_buffer.append(msg)

    d = test_downloader()
    p = MetadataFromTitlePP(d, '%(title)s - %(artist)s')

    title = 'foo'
    info = {'title': title}
    p.run(info)
    assert info == {'title': title}
    assert d.to_screen_buffer == ['[fromtitle] Could not interpret title of video as "%(title)s - %(artist)s"']

    title = 'foo - bar'
    info = {'title': title}
    p.run(info)

# Generated at 2022-06-14 17:58:50.481551
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    """ Unit test for method run of class MetadataFromTitlePP"""

    # Example of video title "TestTitle - TestArtist"
    # with the next formats:
    #    1: "%(title)s - %(artist)s"
    #    2: "TestTitle - TestArtist"
    #    3: "ErrorFormatTest"
    #    4: "NoFormatTest - %(artist)s"
    #    5: "%(title)s - NoFormatTest"
    #    6: "%(unknown_attribute)s - %(artist)s"

    # Test for format 1: "%(title)s - %(artist)s"
    downloader = None
    titleformat = "%(title)s - %(artist)s"
    postprocessor = MetadataFromTitlePP(downloader, titleformat)

# Generated at 2022-06-14 17:59:01.687381
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():

    # Test if we detect invalid titleformat
    titleformat = '%(title)s - %(artist)s'
    try:
        instance = MetadataFromTitlePP(None, titleformat)
        assert False, \
            'test #1: not detected that title of video is not in the format %s %s' % (titleformat, instance._titleformat)
    except ValueError as e:
        assert str(e) == 'Could not interpret %s of video' % titleformat, \
            'test #2: not detected that title of video is not in the format %s' % titleformat

    # Test for erroneous regex in titleformat
    titleformat = '%(title)s - %(artist)s'
    regex = '(?P<title>.+)\ \-\ (?P<artist>.+)'

# Generated at 2022-06-14 17:59:11.000555
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # pylint: disable=protected-access
    downloader = object()
    fromtitle = MetadataFromTitlePP(downloader, '%(title)s')
    info = {
        'title': 'title'
    }
    infos, info = fromtitle.run(info)
    assert infos == []
    assert info['title'] == 'title'
    info = {
        'title': 'title - author'
    }
    infos, info = fromtitle.run(info)
    assert infos == []
    assert info['title'] == 'title - author'
    assert info['author'] == 'author'
    fromtitle = MetadataFromTitlePP(downloader, '%(title)s - %(author)s')
    info = {
        'title': 'title'
    }
    infos, info

# Generated at 2022-06-14 17:59:22.471609
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FileDownloader
    downloader = FileDownloader()
    p = MetadataFromTitlePP(downloader, '%(title)s - %(artist)s')

    # Test 1: only title and artist
    info = {'title': 'An Example'}
    p.run(info)
    assert info == {'title': 'An Example', 'format': 'NA', 'uploader': 'NA', 'ext': 'NA', 'id': 'NA', 'artist': 'NA', 'upload_date': 'NA', 'thumbnail': 'NA'}

    # Test 2: title, artist and format
    info = {'title': 'An Example - An Artist - mp4'}
    p.run(info)

# Generated at 2022-06-14 17:59:27.035396
# Unit test for constructor of class MetadataFromTitlePP
def test_MetadataFromTitlePP():
    titleformat = '%(title)s - %(artist)s'

    expected_titleregex = (r'(?P<title>.+)\ \-\ (?P<artist>.+)')

    pp = MetadataFromTitlePP(None, titleformat)
    assert pp._titleformat == titleformat
    assert pp._titleregex == expected_titleregex



# Generated at 2022-06-14 17:59:37.490296
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():

    video_info = {'ext': 'mp4', 'uploader': '', 'upload_date': '20160926',
                  'title': 'Czechia is GREAT! - Praha, Kutna Hora, and Cesky Krumlov',
                  'webpage_url': '', 'id': 'M6HHZU6EzQA',
                  'thumbnail': 'https://i.ytimg.com/vi/M6HHZU6EzQA/hqdefault.jpg'}

    
    # Test with a pattern of "%(title)s - %(uploader)s"
    metadata_from_title_pp = MetadataFromTitlePP(None, "%(title)s - %(uploader)s")
    info = metadata_from_title_pp.run(video_info)

    print(info)
    


# Generated at 2022-06-14 17:59:46.827176
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import pytube
    pp = MetadataFromTitlePP(None, '%(title)s - %(artist)s')
    info = {'title': 'some title - some artist'}
    [], info = pp.run(info)
    assert info['title'] == info['artist'] == 'some artist'

    pp = MetadataFromTitlePP(None, '%(title)s')
    info = {'title': 'some title - some artist'}
    [], info = pp.run(info)
    assert info['title'] == 'some title - some artist'

# Generated at 2022-06-14 17:59:54.207748
# Unit test for constructor of class MetadataFromTitlePP
def test_MetadataFromTitlePP():
    downloader = object()
    # test simple cases
    mftpp = MetadataFromTitlePP(downloader, '%(title)s.mp3')
    assert mftpp._titleformat == '%(title)s.mp3'
    assert mftpp._titleregex == r'(?P<title>.+).mp3'
    # test %(..)s conversion
    mftpp = MetadataFromTitlePP(downloader, '%(title)s - %(artist)s')
    assert mftpp._titleformat == '%(title)s - %(artist)s'
    assert mftpp._titleregex == r'(?P<title>.+)\ \-\ (?P<artist>.+)'
    # test no conversion

# Generated at 2022-06-14 18:00:03.014094
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # test data
    video_data = {'title': 'The video'}
    expected_info = {'title': 'The video'}
    # test case 1: no %(..)s in titleformat
    titleformat = 'The titleformat'
    leftovers, info = MetadataFromTitlePP(None, titleformat).run(video_data)
    # test case 1: check the expected result
    assert leftovers == []
    assert info == expected_info
    # test case 2: %(..)s in titleformat
    titleformat = 'This is %(title)s'
    expected_info = {'title': 'This is The video'}
    leftovers, info = MetadataFromTitlePP(None, titleformat).run(video_data)
    # test case 2: check the expected result
    assert leftovers == []


# Generated at 2022-06-14 18:00:13.961269
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import unittest
    import sys
    import hashlib
    from dl_ytd.downloader.common import FileDownloader
    from dl_ytd.extractor.common import YoutubeIE
    from dl_ytd.utils import encodeFilename

    class MockYoutubeIE(YoutubeIE):
        def __init__(self, downloader, ie_key):
            YoutubeIE.__init__(self, ie_key)
            self._downloader = downloader


# Generated at 2022-06-14 18:00:22.315805
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    downloader = lambda: 0
    downloader.to_screen = lambda x: None
    title = 'Video title - 6:30'
    info = {'title': title}
    pp = MetadataFromTitlePP(downloader, '%(title)s - %(minutes)s:%(seconds)s')
    pp.run(info)
    assert info['title'] == title
    assert info['minutes'] == '6'
    assert info['seconds'] == '30'

# Generated at 2022-06-14 18:00:24.094320
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    pass



# Generated at 2022-06-14 18:00:32.122993
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    m = MetadataFromTitlePP(None, '%(title)s - %(artist)s')
    assert m._titleregex == r'(?P<title>.+)\ \-\ (?P<artist>.+)'

    info = {
        'title': 'The Meaning of Life - Monty Python'
    }
    with_metadata, info = m.run(info)
    assert with_metadata == []
    assert info['title'] == 'The Meaning of Life'
    assert info['artist'] == 'Monty Python'

# Generated at 2022-06-14 18:00:38.279661
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    '''Test method run of class MetadataFromTitlePP
    with titleformat '%(title)s - %(artist)s'
    '''
    # setup dummy downloader
    class DummyDownloader(object):
        def to_screen(self, msg):
            pass

    # setup mock info variable
    info = {
        'title': 'my_title - my_artist',
        }

    # setup and run processor
    titleformat = '%(title)s - %(artist)s'
    pp = MetadataFromTitlePP(DummyDownloader(), titleformat)
    info_merged, info_returned = pp.run(info)

    # see if info dicts match expectations
    expected_returned = {
        'title': 'my_title',
        'artist': 'my_artist'
        }
   

# Generated at 2022-06-14 18:00:48.258737
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    def fake_downloader(to_screen):
        class FakeInfoDict(dict):
            def __init__(self):
                super(FakeInfoDict, self).__init__()
                self['title'] = 'title1 - title2 - title3'
                self['artist'] = None
                self['track'] = None
        return FakeInfoDict(), to_screen

    to_screen = []
    downloader = fake_downloader(to_screen.append)
    metadata_from_title = MetadataFromTitlePP(downloader, '%(track)s - %(artist)s - %(title)s')
    nfo, info = metadata_from_title.run(info={})
    assert info['title'] is None
    assert info['artist'] == 'title2'
    assert info['track'] == 'title1'

# Generated at 2022-06-14 18:00:58.639786
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    pp = MetadataFromTitlePP(None, 'blah-%(title)s')
    info = {'title': 'blah-title'}
    assert pp.run(info) == ([], {'title': 'blah-title', 'title': 'title'})

    pp = MetadataFromTitlePP(None, '%(blah)s')
    info = {'title': 'blah-title'}
    assert pp.run(info) == ([], {'title': 'blah-title'})

    pp = MetadataFromTitlePP(None, 'blah-%(title)s')
    info = {'title': 'blah'}
    assert pp.run(info) == ([], {'title': 'blah'})


# Generated at 2022-06-14 18:01:08.503438
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # create fake downloader
    class FakeInfo:
        def __init__(self, info):
            self.info = info

    class FakeYdl:
        def __init__(self, info):
            self.info = info

        def to_screen(self, string):
            print(string)

    title = 'Foo - Bar'
    info = {'title': title}
    format = '%(title)s - %(artist)s'
    mftpp = MetadataFromTitlePP(FakeYdl(FakeInfo(info)), format)
    info = mftpp.run(info)[1]
    assert info['title'] == 'Foo'
    assert info['artist'] == 'Bar'

# Generated at 2022-06-14 18:01:19.562830
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import youtube_dl.YoutubeDL
    downloader = youtube_dl.YoutubeDL()
    pp = MetadataFromTitlePP(downloader, '%(title)s - %(artist)s')
    info = {}
    info['title'] = 'title'
    info['id'] = 'id'
    (res, meta) = pp.run(info)
    assert meta['title'] == 'title'
    assert meta['artist'] == 'artist'
    info['title'] = 'title - artist'
    (res, meta) = pp.run(info)
    assert meta['title'] == 'title'
    assert meta['artist'] == 'artist'
    info['title'] = 'wrongtitle - artist'
    (res, meta) = pp.run(info)
    assert meta['title'] == 'wrongtitle'

# Generated at 2022-06-14 18:01:24.950079
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    pp = MetadataFromTitlePP(None, '%(title)s - %(artist)s')
    info = {'title': 'Documentary Title - Artist Name'}
    pp.run(info)
    assert info == {'title': 'Documentary Title - Artist Name',
                    'artist': 'Artist Name'}

# Generated at 2022-06-14 18:01:34.449979
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():

    class DummyDownloader(object):
        def to_screen(self, msg):
            self.msg = msg

    downloader = DummyDownloader()

    info = {'title': 'Download video - Unit test'}
    pp = MetadataFromTitlePP(downloader, 'Download video - %(title)s')
    pp.run(info)
    assert downloader.msg == '[fromtitle] parsed title: Unit test'
    assert info == {
        'title': 'Download video - Unit test',
        'title_url': 'Unit test'}

    info = {'title': 'Download video - Unit test - Part 1'}
    pp = MetadataFromTitlePP(downloader, 'Download video - %(title)s - %(part)s')
    pp.run(info)

# Generated at 2022-06-14 18:01:45.034634
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    if sys.version_info.major == 2:
        import mock
    elif sys.version_info.major == 3:
        from unittest import mock

    def run_PostProcessor(downloader, info):
        pp = MetadataFromTitlePP(downloader, '%(title)s - %(artist)s')
        new_info, _ = pp.run(info)
        return new_info

    info = {'ext': 'mp4', 'title': 'Hello - My First Video  ', 'webpage_url': 'some_url'}
    expected_new_info = {'ext': 'mp4', 'title': 'Hello - My First Video  ', 'webpage_url': 'some_url', 'artist': 'My First Video', 'title': 'Hello'}
    downloader = mock.Mock

# Generated at 2022-06-14 18:01:57.051132
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class FakeDownloader:
        def __init__(self):
            self.to_screen_calls = []
        def to_screen(self, msg):
            self.to_screen_calls.append(msg)

    title_to_artist_fmt = '%(artist)s - %(title)s'
    info_with_artist_title = {
        'title': 'Beck - Colors'
    }
    info_with_artist_title_extracted = {
        'title': 'Beck - Colors',
        'artist': 'Beck'
    }
    info_only_with_title = {
        'title': 'Colors'
    }

    downloader = FakeDownloader()
    pp = MetadataFromTitlePP(downloader, title_to_artist_fmt)
    downloaded, updated_info = pp

# Generated at 2022-06-14 18:02:03.939635
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ytdl.YoutubeDL import YoutubeDL
    def test_assert(fmt, title, expected_info, expected_warnings):
        pp = MetadataFromTitlePP(YoutubeDL(), fmt)
        info = {'title': title}
        res_info = {}
        res_warnings = {}
        pp.run(info)
        assert info == expected_info
        assert res_warnings == expected_warnings
    # Test that all groups in titleformat are parsed
    test_assert(fmt='%(title)s - %(artist)s [%(id)s]',
                title='song - artist [id]',
                expected_info={'title': 'song', 'artist': 'artist', 'id': 'id'},
                expected_warnings={})
    # Test that all groups in titleformat are parsed (

# Generated at 2022-06-14 18:02:15.183222
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .YoutubeDL import YoutubeDL

    ydl = YoutubeDL()
    ydl.params['simulate'] = True
    ydl.add_post_processor(MetadataFromTitlePP(ydl, '%(title)s - %(artist)s'))

    assert ydl.extract_info(
        'http://www.youtube.com/watch?v=BaW_jenozKc',
        download=False)['artist'] == 'Hans Zimmer and James Newton Howard'

    ydl.add_post_processor(MetadataFromTitlePP(ydl, '%(title)s - %(artist)s'))


# Generated at 2022-06-14 18:02:20.818895
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import pycurl
    import shutil
    import tempfile
    from .common import FileDownloader
    import youtube_dl.YoutubeDL
    import unittest

    # Create dummy files in temporary directory
    tmpdir = tempfile.mkdtemp()
    pristine_filename = 'pristine.mp4'
    test_filename = 'test.mp4'
    with open(tmpdir + '/' + pristine_filename, 'wb') as f:
        f.write(b'\x09\x0A')

    # Create a downloader object
    class DummyYoutubeDL(youtube_dl.YoutubeDL):
        def __init__(self, params):
            self.params = params
            self.to_screen = lambda s: None
            self.to_stderr = lambda s: None
    downloader = FileDownload

# Generated at 2022-06-14 18:02:29.732923
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():

    class FakeDownloader:
        def to_screen(self, message):
            pass

    pp = MetadataFromTitlePP(FakeDownloader(), '%(title)s - %(artist)s')
    resultinfo = pp.run({'title': 'Yukon - (Official Video) - Charlie Puth [Furious 7 Soundtrack]'})
    assert resultinfo == ([],
        {'title': 'Yukon - (Official Video) - Charlie Puth [Furious 7 Soundtrack]', 'artist': 'Charlie Puth'}), \
        'resultinfo has wrong value %s' % resultinfo

# Generated at 2022-06-14 18:02:41.966295
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class DummyDownloader(object):
        def __init__(self):
            self.screen_data = ''
        def to_screen(self, msg):
            self.screen_data += msg + '\n'
    titlestr = '%(title)s - %(artist)s - %(album)s'
    md_title = 'I love music'
    md_artist = 'dj otzi'
    md_album = 'the album'
    info = {'title': md_title + ' - ' + md_artist + ' - ' + md_album}
    expected_info = {'title': md_title, 'artist': md_artist, 'album': md_album}

    downloader = DummyDownloader()
    pp = MetadataFromTitlePP(downloader, titlestr)

    output = pp.run

# Generated at 2022-06-14 18:02:54.140231
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class FakeDownloader():
        def __init__(self):
            self.to_screenlog = []
        def to_screen(self, msg):
            self.to_screenlog.append(msg)

    # Using a series of different title formats and title strings, this test
    # determines if the expected info is extracted from the video title
    # and if the expected output is generated by the to_screen method

# Generated at 2022-06-14 18:02:57.733368
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    titleformat = '%(title)s - %(artist)s'
    title = 'Title - Artist'

    import youtube_dl
    downloader = youtube_dl.YoutubeDL()
    pp = MetadataFromTitlePP(downloader, titleformat)

    info = {'title': title}
    new_info = pp.run(info)

    assert info.get('title') == 'Title'
    assert info.get('artist') == 'Artist'

# Generated at 2022-06-14 18:03:10.699402
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    # Mock values
    title = 'The Muppets - Bohemian Rhapsody'
    titleformat = '%(title)s - %(artist)s'
    titleregex = '^(?P<title>.+)\ \-\ (?P<artist>.+)$'
    groupdict = {'title': 'The Muppets', 'artist': 'Bohemian Rhapsody'}
    info = {'title': title}

    class MockYoutubeDL():
        to_screen = lambda self, msg: sys.stdout.write('[fromtitle] ' + msg + '\n')

    downloader = MockYoutubeDL()

    pp = MetadataFromTitlePP(downloader, titleformat)
    assert pp._titleregex == titleregex

    res = pp.run(info.copy())
    expres

# Generated at 2022-06-14 18:03:22.018531
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    # sys.argv = ['', '-v', '--from-title', '%(title)s - %(artist)s', '%(title)s - %(artist)s.mp4']
    from youtube_dl.YoutubeDL import YoutubeDL
    ydl = YoutubeDL()
    ydl.add_default_info_extractors()
    ydl.add_post_processor(MetadataFromTitlePP(ydl, '%(title)s - %(artist)s'))
    info = {'title':'love somebody - maroon 5'}
    mftpp = MetadataFromTitlePP(ydl, '%(title)s - %(artist)s')
    postprocessors, info = mftpp.run(info)
    assert postprocessors == []

# Generated at 2022-06-14 18:03:29.625549
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class FakeDL:
        def __init__(self):
            self.screen = []

        def to_screen(self, message):
            self.screen.append(message)

    dl = FakeDL()

    # test regex with named groups
    titleformat = '%(artist)s - %(track)s'
    title = 'Sia - Chandelier'
    info = {'title': title}
    pp = MetadataFromTitlePP(dl, titleformat)
    pp.run(info)
    assert info['artist'] == 'Sia'
    assert info['track'] == 'Chandelier'
    assert dl.screen[0] == \
        '[fromtitle] parsed artist: Sia'
    assert dl.screen[1] == \
        '[fromtitle] parsed track: Chandelier'
    dl

# Generated at 2022-06-14 18:03:40.175436
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FileDownloader
    import sys
    import tempfile

    program = 'youtube-dl'

    info = {'title': 'Adele - Rolling in the Deep'}
    out, err = tempfile.TemporaryFile(), tempfile.TemporaryFile()

    pp = MetadataFromTitlePP(FileDownloader(downloader_options=[]), '%(artist)s - %(title)s')

    # test parse of artist and title
    pp.run(info)
    assert info['artist'] == 'Adele'
    assert info['title'] == 'Rolling in the Deep'

    # test print of artist and title
    oldstdout = sys.stdout
    sys.stdout = out
    pp.run(info)
    sys.stdout = oldstdout
    out.seek(0)

# Generated at 2022-06-14 18:03:49.195666
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    pp = MetadataFromTitlePP(None, '%(title)s - %(artist)s')

# Generated at 2022-06-14 18:04:00.958558
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import sys
    import unittest
    import youtube_dl.extractor.common as common
    from functools import partial

    class DownloaderStub(object):
        """
        Minimal stub class which implements to_screen.
        """
        def to_screen(self, message, skip_eol=False):
            print(message)

    class FakeInfoExtractor(common.InfoExtractor):
        def __init__(self, downloader):
            self.downloader = downloader

    class FakeInfo(object):
        def __init__(self, title):
            self.title = title

    def build_postprocessor(titleformat):
        """
        Helper method to build a MetadataFromTitlePP object.
        """
        downloader = DownloaderStub()
        ie = FakeInfoExtractor(downloader)
       

# Generated at 2022-06-14 18:04:10.526496
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    titleformat = '%(artist)s - %(title)s'
    downloader = None
    pp = MetadataFromTitlePP(downloader, titleformat)
    info = {'title': 'artist - title'}
    [], info2 = pp.run(info)
    assert info2['artist'] == 'artist'
    assert info2['title'] == 'title'

    info = {'title': 'artist - title - album'}
    [], info2 = pp.run(info)
    assert info2['artist'] == 'artist'
    assert info2['title'] == 'title'

    info = {'title': 'artist - title - '}
    [], info2 = pp.run(info)
    assert info2['artist'] == 'artist'
    assert info2['title'] == 'title'


# Generated at 2022-06-14 18:04:19.906229
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class DummyYDL(object):
        def to_screen(self, msg):
            pass

    titleformat = r'^(?P<artist>.*) - (?P<title>.*)$'
    title = 'Artist - Title'
    info = {
        'title': title,
        'artist': 'NA',
        'title': 'NA'
    }
    pp = MetadataFromTitlePP(DummyYDL(), titleformat)
    infolist = pp.run(info)

    assert(len(infolist) == 0)
    assert(info['artist'] == 'Artist')
    assert(info['title'] == 'Title')


# Generated at 2022-06-14 18:04:29.372327
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .YoutubeDL import YoutubeDL
    info = {
        'title': 'Le tourbillon de la vie - Isabelle Boulay, Garou, Jean-Francois Breau',
        'id': 'test'
    }
    downloader = YoutubeDL(params={})
    pp = MetadataFromTitlePP(downloader, titleformat='%(title)s - %(artist)s')
    result = pp.run(info)
    assert result[1]['title'] == 'Le tourbillon de la vie'
    assert result[1]['artist'] == 'Isabelle Boulay, Garou, Jean-Francois Breau'

# Generated at 2022-06-14 18:04:41.015207
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    fttpp = MetadataFromTitlePP(None, '%(title)s - %(artist)s - %(album)s')
    info1 = {'title': 'One Song - Artist - Album'}
    info2 = {'title': 'One Song - Artist - Album - Extra'}
    info3 = {'title': 'One Song - Artist'}

    out, ret = fttpp.run(info1)
    assert ret == {'title': 'One Song', 'artist': 'Artist', 'album': 'Album'}
    out, ret = fttpp.run(info2)
    assert ret == {'title': 'One Song', 'artist': 'Artist', 'album': 'Album - Extra'}
    out, ret = fttpp.run(info3)

# Generated at 2022-06-14 18:04:55.439915
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FakeYDL
    from .downloader import FakeDownloader

    downloader = FakeDownloader({})
    ydl = FakeYDL({'title': 'foo'})
    ydl.add_post_processor(MetadataFromTitlePP(ydl, '%(title)s'))
    ydl.process_info({'title': 'foo'})
    assert downloader.get_info_dict()['title'] == 'foo'
    assert ydl.get_info_dict()['title'] == 'foo'

    downloader = FakeDownloader({})
    ydl = FakeYDL({'title': 'foo'})
    ydl.add_post_processor(MetadataFromTitlePP(ydl, '%(title)s - %(test)s'))

# Generated at 2022-06-14 18:05:07.101026
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.downloader import common
    from youtube_dl.extractor import YoutubeIE
    downloader = common.FileDownloader(params={'quiet': True, 'simulate': True},
                                       downloader_opts={'forceduration': True})
    downloader.add_info_extractor(YoutubeIE())
    pp = MetadataFromTitlePP(downloader, '%(artist)s - %(title)s')
    from youtube_dl.YoutubeDL import YoutubeDL
    ydl = YoutubeDL(params={'quiet': True})
    info = {'title': 'Dolly Parton - I Will Always Love You'}
    ydl.add_post_processor(pp)
    ydl.process_ie_result(info, downloader=downloader)
    assert info['artist'] == 'Dolly Parton'


# Generated at 2022-06-14 18:05:18.402923
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FileDownloader
    from .extractor import YoutubeIE
    from .extractor import get_info_extractor
    # Mock FileDownloader class for unit test
    class mock_FileDownloader(FileDownloader):
        def __init__(self, params):
            self.params = params
        def to_screen(self, msg):
            print(msg)
    # Mock YoutubeIE class for unit test
    class mock_YoutubeIE(YoutubeIE):
        def __init__(self, *args, **kwargs):
            self.urls = []
            self.parameters = []
            self.infos = []
        def report_video_webpage(self, video_id, video_url, video_title):
            self.urls.append(video_url)

# Generated at 2022-06-14 18:05:29.131296
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import inspect
    from ..common import Downloader
    from ..utils import DateRange

    def mock_downloader(url, params={}):
        pass

    mock_downloader.params = {
        'download_archive': None,
        'match_filter': DateRange(),
        'max_downloads': None,
        'min_filesize': None,
        'max_filesize': None,
    }

    titleformat = '[%(artist)s] %(title)s'
    titleregex = r'\[(?P<artist>.+)\] (?P<title>.+)'

    pp = MetadataFromTitlePP(mock_downloader, titleformat)
    pp._titleregex = titleregex
    pp.run({'id': 'test', 'title': '[test] video'})


# Unit test

# Generated at 2022-06-14 18:05:38.926199
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import youtube_dl
    pp = MetadataFromTitlePP(
        object(),  # downloader
        '%(episode)s.%(track)s - %(artist)s - %(title)s')
    assert pp.run({
        'title': '',
    }) == ([], {
        'episode': None,
        'track': None,
        'artist': None,
        'title': ''})
    assert pp.run({
        'title': '1.2 - foo - bar',
    }) == ([], {
        'episode': '1',
        'track': '2',
        'artist': 'foo',
        'title': 'bar',
    })

# Generated at 2022-06-14 18:05:48.766019
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class Dummy:
        def __init__(self):
            self.params = {
                'prefer_free_formats': False,
                'verbose': True
            }

        def to_screen(self, msg):
            print(msg)

    # Test 1: no regex matching
    ydl = Dummy()
    pp = MetadataFromTitlePP(ydl, '%(title)s - %(artist)s')
    results, info = pp.run({'title': 'abc'})
    assert info == {'title': 'abc'}

    # Test 2: regex matching
    ydl = Dummy()
    pp = MetadataFromTitlePP(ydl, '%(title)s - %(artist)s')
    results, info = pp.run({'title': 'xyz - abc'})
   

# Generated at 2022-06-14 18:05:57.319292
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import FakeYDL
    from .compat import compat_basestring

    def test(title, result):
        """
        title: string that we want to put in the 'title' field of info dict
        result: {field_name: field_value, ...}
                 It should contains the values that should be extracted from
                 title or missing values should be None.
        """
        def test_1(titleformat):
            ydl = FakeYDL()
            pp = MetadataFromTitlePP(ydl, titleformat)
            info = {'title': title}
            pp.run(info)
            assert sorted(result.items()) == sorted(info.items())
        test_1('Title: %(title)s')
        test_1('Artist: %(artist)s')

# Generated at 2022-06-14 18:06:08.621453
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Test regexp interpretation
    # Test with regexp with named groups
    titleregex = 'TEST - (?P<artist>.+) - (?P<title>.+)'
    title = 'TEST - test-artist - test-title'
    expected = {
        'title': 'test-title',
        'artist': 'test-artist'
    }
    result = re.match(MetadataFromTitlePP.format_to_regex(titleregex), title)
    assert expected == result.groupdict()

    # Test with regexp without named groups
    titleregex = 'TEST - (.+) - (.+)'
    title = 'TEST - test-artist - test-title'
    expected = {
        'title': 'test-title',
        'artist': 'test-artist'
    }

# Generated at 2022-06-14 18:06:21.418269
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from ytdl.YoutubeDL import YoutubeDL
    downloader = YoutubeDL()

    def test(title, format, exp_info):
        pp = MetadataFromTitlePP(downloader, format)
        info = {'title': title}
        pp.run(info)
        assert info == exp_info, 'unexpected metadata'

    test('Gratisography - Free high-resolution pictures you can use on your personal and commercial projects.',
         '%(title)s',
         {'title': 'Gratisography - Free high-resolution pictures you can use on your personal and commercial projects.'})


# Generated at 2022-06-14 18:06:26.561625
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # Create instance of MetadataFromTitlePP
    mftpp = MetadataFromTitlePP(None, '%(title)s')

    # Generate info
    info = {'title': 'This title was extracted'}

    # Run method run of class MetadataFromTitlePP
    mftpp.run(info)

    # Test if method run returned the correct metadata
    assert info['title'], 'This title was extracted'

# Generated at 2022-06-14 18:06:46.029006
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.downloader.common import FileDownloader
    from youtube_dl.postprocessor import FFmpegMetadataPP
    dl = YoutubeDL({'verbose': True})
    dl.add_post_processor(FFmpegMetadataPP(dl))
    dldr = FileDownloader(dl, {'outtmpl': '%(title)s-%(id)s.%(ext)s', 'format': 'bestaudio'})

    test_title_value = 'Foo - Bar'

# Generated at 2022-06-14 18:06:55.922670
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import ydl_config
    from pytube.compat import compat_urllib_parse_unquote

    optmap = {
        'format': 'mp4',
        'ignoreerrors': True,
        'outtmpl': '',
        'restrictfilenames': True,
    }
    # Test with default format string to get a regex
    pp = MetadataFromTitlePP(ydl_config.YDL_DEFAULT_OPTS, optmap)
    info = {'title': '%(artist)s - %(song)s'}
    pp.run(info)
    assert info['artist'] == 'NA'
    assert info['song'] == 'NA'

    # Test with just a format string (no regex)
    optmap['format'] = '%(artist)s - %(song)s'
    pp

# Generated at 2022-06-14 18:07:02.110409
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .common import Downloader
    downloader = Downloader(params={})
    pp = MetadataFromTitlePP(downloader, '%(title)s - %(artist)s')
    assert ({'title': 'title', 'artist': 'artist'}, {}) == pp.run({'title': 'title - artist'})
    assert ({'title': 'title'}, {}) == pp.run({'title': 'title - artist2'})


# Generated at 2022-06-14 18:07:14.223336
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    class info_dummy:
        def __init__(self, title, filename):
            self._filename = filename
            self.title = title
            self.metadata = {}
    class options_dummy:
        def __init__(self, format_string):
            self.writemetadata = True
            self.metafromtitle = format_string


# Generated at 2022-06-14 18:07:24.438527
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    video_info = {
        'title': 'short video title',
        'artist': 'unknown artist',
        'uploader': 'unknown uploader'
    }

    pp = MetadataFromTitlePP(None, '%(artist)s - %(title)s')
    expected = {
        'title': 'short video title',
        'artist': 'unknown artist',
        'uploader': 'unknown uploader'
    }
    assert pp.run(video_info)[1] == expected

    pp = MetadataFromTitlePP(None, '%(title)s by %(artist)s')
    expected = {
        'title': 'short video title',
        'artist': 'unknown artist',
        'uploader': 'unknown uploader'
    }
    assert pp.run(video_info)[1] == expected


# Generated at 2022-06-14 18:07:35.464063
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # init a downloader
    downloader = object()
    # init a postprocessor
    postprocessor = MetadataFromTitlePP(downloader, r'%(artist)s - %(title)s')
    # prepare the info
    info = {}
    info['title'] = 'Foobar - Test'
    # run the postprocessor
    no_download, new_info = postprocessor.run(info)
    if new_info.get('title') != 'Test':
        print('test_MetadataFromTitlePP_run failed: Test title not found. (%s)' % info.get('title'))
    if new_info.get('artist') != 'Foobar':
        print('test_MetadataFromTitlePP_run failed: Test artist not found. (%s)' % info.get('artist'))

# Generated at 2022-06-14 18:07:42.558214
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    # To test the method run of class MetadataFromTitlePP, we will test the
    # following cases
    # - Trying to parse a title that does not fit the format given
    #       PostProcessor must log a message.
    # - Trying to parse a title that does fit the format given and has info
    #   for all key of %(..)s in format
    #       PostProcessor must log a messagefor each attribute
    # - Trying to parse a title that does fit the format given and has info
    #   for only some keys of %(..)s in format
    #       PostProcessor must log a message for each attribute that has
    #       information
    from .common import FakeDownloader
    from .compat import compat_str, compat_etree_fromstring

    title = 'foo - bar'

# Generated at 2022-06-14 18:07:46.282700
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.YoutubeDL import YoutubeDL
    info = {
        'title': 'Unknown Artist - Unknown Title',
    }
    p = MetadataFromTitlePP(None, '%(artist)s - %(title)s')
    assert p.run(info) == ([], {
        'title': 'Unknown Artist - Unknown Title',
        'artist': 'Unknown Artist',
        'title': 'Unknown Title',
    })

# Generated at 2022-06-14 18:07:55.600538
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    import unittest
    import sys

    class _FakeInfo(object):
        def __init__(self, title):
            self.__title = title

        @property
        def title(self):
            return self.__title

        def __setitem__(self, key, value):
            setattr(self, key, value)

    class _FakeDownloader(object):
        def __init__(self, to_screen_message):
            self._to_screen_message = to_screen_message

        def to_screen(self, message_prefix, message):
            self._to_screen_message(message_prefix, message)

    class _TestCase(unittest.TestCase):
        def setUp(self):
            self.__to_screen_log = []

# Generated at 2022-06-14 18:08:04.063242
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from .pyext import downloader

    opts = {'metadatafromtitle': {'titleformat': '%(title)s - %(artist)s'}}
    downloader.FD = downloader.FakeDownloader(params=opts)
    info = {'title': 'The Title - By The Artist'}

    metadata_from_title_pp = MetadataFromTitlePP(downloader.FD, opts['metadatafromtitle']['titleformat'])
    result = metadata_from_title_pp.run(info)

    assert result == ([], {'title': 'The Title', 'artist': 'By The Artist'}), "test_MetadataFromTitlePP_run failed"

# Generated at 2022-06-14 18:08:31.016288
# Unit test for method run of class MetadataFromTitlePP
def test_MetadataFromTitlePP_run():
    from youtube_dl.downloader.common import FileDownloader
    from youtube_dl.YoutubeDL import YoutubeDL

    ydl = YoutubeDL({'outtmpl': '%(uploader)s/%(upload_date)s/%(title)s-%(id)s.%(ext)s'})
    ydl.add_post_processor(MetadataFromTitlePP(ydl, '%(uploader)s/%(title)s'))
