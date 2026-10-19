

# Generated at 2022-06-14 17:48:40.968322
# Unit test for function parseOpts
def test_parseOpts():
    assert parseOpts(['--extract-audio', '--audio-format', 'best'])[1].extractaudio

    assert parseOpts(['--audio-quality', '0'])[1].audioquality == '0'

    assert parseOpts(['--audio-quality', '129K'])[1].audioquality == '129K'

    assert parseOpts(['-4'])[1].noplaylist is True
    assert parseOpts(['--no-playlist'])[1].noplaylist is True

    assert parseOpts(['--proxy', '1.1.1.1:8080'])[1].proxy == '1.1.1.1:8080'
    assert parseOpts(['--proxy', ''])[1].proxy is None

# Generated at 2022-06-14 17:48:47.729706
# Unit test for function parseOpts
def test_parseOpts():
    from unittest import TestCase
    from types import GeneratorType
    class ParseOptsTest(TestCase):
        def test_select_format(self):
            opts, args = parseOpts(['-f', '37/22/18'])
            self.assertEqual(opts.format, '37/22/18')

            opts, args = parseOpts(['-F'])
            self.assertEqual(type(opts.format), GeneratorType)

        def test_list_thumbnails(self):
            opts, args = parseOpts(['--list-thumbnails'])
            self.assertTrue(opts.list_thumbnails)
            opts, args = parseOpts(['--write-thumbnails'])
            self.assertFalse(opts.list_thumbnails)


# Generated at 2022-06-14 17:49:01.307635
# Unit test for function parseOpts
def test_parseOpts():
    (parser, opts, args) = parseOpts(['--youtube-skip-dash-manifest', '--flat-playlist', '--max-downloads', '1', '--no-continue', '--no-part', '--format', '137+140', 'https://www.youtube.com/watch?v=BaW_jenozKc&t=1s', 'https://www.youtube.com/watch?v=2gL-l4vwq3E'])

# Generated at 2022-06-14 17:49:13.623755
# Unit test for function parseOpts
def test_parseOpts():

    parser, opts, args = parseOpts(overrideArguments = ['--verbose','--extract-audio','--cut-at-time=00:50:00','--audio-quality=0','--audio-format=aac','--ignore-errors','--no-overwrites','--write-thumbnail','--write-all-thumbnails','--write-info-json','--write-annotations','-o=%(title)s.%(ext)s','-f=bestaudio[ext=m4a]/best','-i','https://www.youtube.com/watch?v=b8eF6n0py1U'])

# Generated at 2022-06-14 17:49:18.317680
# Unit test for function parseOpts
def test_parseOpts():
    opts, args = parseOpts()
    assert isinstance(opts, optparse.Values)
    assert isinstance(args, list)

# }}}

# {{{ actually download the video file

# Generated at 2022-06-14 17:49:22.318350
# Unit test for function parseOpts
def test_parseOpts():
    opts, args = parseOpts()
    assert opts.get('default_search') == 'auto', opts.get('default_search')

# Generated at 2022-06-14 17:49:35.520805
# Unit test for function parseOpts
def test_parseOpts():
    # TODO: move tests to seperate unit test
    assert(parseOpts(['-F', 'https://www.youtube.com/watch?v=BaW_jenozKc'])[2][0] ==
           'https://www.youtube.com/watch?v=BaW_jenozKc')
    assert(parseOpts(['-f', '22/18/17/best'])[1].format ==
           '22/18/17/best')
    assert(parseOpts(['-f', 'bestvideo+bestaudio/best'])[1].format ==
           'bestvideo+bestaudio/best')
    assert(parseOpts(['-f', 'best[height<=?480]'])[1].format ==
           'best[height<=?480]')



# Generated at 2022-06-14 17:49:37.460209
# Unit test for function parseOpts
def test_parseOpts():
    pass

# parseOpts = parse_opts
# test_parseOpts()

# The main function

# Generated at 2022-06-14 17:49:42.865767
# Unit test for function parseOpts
def test_parseOpts():
    sout = StringIO()
    sys.stdout = sout
    sys.argv[1:] = ['--verbose', '-i', 'http://www.youtube.com/watch?v=BaW_jenozKc']
    parser, opts, args = parseOpts()
    assert opts.verbose
    assert opts.simulate
    assert opts.no_warnings
    assert opts.quiet
    sys.stdout = sys.__stdout__


# Generated at 2022-06-14 17:49:48.172434
# Unit test for function parseOpts
def test_parseOpts():
    def assert_equal_opts(opts, d):# {{{
        for (k, v) in d.items():
            if isinstance(v, list):
                assert getattr(opts, k) == v, (k, getattr(opts, k), v)
            else:
                assert getattr(opts, k) == v, (k, getattr(opts, k), v)
    # }}}
    def assert_equal_args(args, list):# {{{
        assert args == list, args
    # }}}
    def assert_raises(err, func, *args, **kwargs):# {{{
        try:
            func(*args, **kwargs)
        except err:
            pass
        else:
            assert 0, 'Exception %s not raised' % err
    # }}}

# Generated at 2022-06-14 17:50:12.215946
# Unit test for function parseOpts
def test_parseOpts():
    opts, args = parseOpts(['--username', 'foo', '--password', 'bar', '"http://www.youtube.com/watch?v=BaW_jenozKc"'])
    assert opts.username == 'foo'
    assert opts.password == 'bar'
    assert opts.usenetrc == False
    assert opts.videopassword == None



# Generated at 2022-06-14 17:50:19.090859
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, _ = parseOpts(overrideArguments = ['--extract-audio', '--audio-quality', '0', '--audio-format', 'aac', '--list-thumbnails', 'https://www.youtube.com/watch?v=WQlwQ7VF-lk'])
    assert opts.extractaudio == True
    assert opts.audioquality == '0'
    assert opts.audioformat == 'aac'
    assert opts.list_thumbnails == True

# Generated at 2022-06-14 17:50:19.991458
# Unit test for function parseOpts
def test_parseOpts():
    opts.parseOpts()



# Generated at 2022-06-14 17:50:27.515749
# Unit test for function parseOpts
def test_parseOpts():
    from io import StringIO
    from sys import argv
    argv = [argv[0]]
    opts, args = parseOpts()
    assert opts.verbose == False
    assert args == []

    _stdout = StringIO()
    def _getvalue():
        _stdout.seek(0)
        return _stdout.read()
    argv.append('--verbose')
    opts, args = parseOpts()
    assert opts.verbose == True
    assert args == []
    assert _getvalue() == '[debug] System config: []\n[debug] User config: []\n[debug] Custom config: []\n[debug] Command-line args: [\'-v\']\n'

    _stdout = StringIO()

# Generated at 2022-06-14 17:50:38.071313
# Unit test for function parseOpts
def test_parseOpts():
    import os
    import shutil
    import tempfile
    import unittest

    def _create_config_file(contents):
        config_file = tempfile.NamedTemporaryFile(delete=False)
        config_file.write(contents.encode('utf-8'))
        config_file.close()
        return config_file.name

    class ParseOptsTest(unittest.TestCase):
        def setUp(self):
            self.temp_dirs = []

        def tearDown(self):
            for d in self.temp_dirs:
                shutil.rmtree(d)

        def test_location_option(self):
            config_contents = '--no-check-certificate\n--no-color'

# Generated at 2022-06-14 17:50:49.724391
# Unit test for function parseOpts
def test_parseOpts():
    import sys
    import tempfile
    import unittest

    class MockOptionParser(object):
        def __init__(self):
            self.opts = []

        def add_option(self, *args, **kwargs):
            self.opts.append((args, kwargs))

        def add_option_group(self, *args, **kwargs):
            pass

        def parse_args(self, args=None):
            return type('opts', (object,), dict(self.opts))(), []

    class MockConfigParser(object):
        def __init__(self):
            self.sections = []

        def read(self, filename):
            pass

        def add_section(self, section):
            self.sections.append(section)


# Generated at 2022-06-14 17:51:01.676441
# Unit test for function parseOpts
def test_parseOpts():
    import sys
    opts, args = parseOpts()
    assert isinstance(opts, optparse.Values) and isinstance(args, list)

# Generated at 2022-06-14 17:51:14.364392
# Unit test for function parseOpts
def test_parseOpts():
    from_stdin_args = ['-']
    from_url_args = ['https://www.youtube.com/watch?v=BaW_jenozKc']
    from_file_args = ['--batch-file', '-']
    player_url_args = ['https://www.youtube.com/watch?v=BaW_jenozKc', '--get-url']

    # Test 1:
    # Parser should not throw an exception without arguments
    try:
        parseOpts(None)
    except:
        assert False

    # Test 2:
    # Parser should return an error message for missing URL
    parser, _, _ = parseOpts(None)
    error_message = parser.error('Must provide at least one URL')
    assert len(error_message) != 0

    # Test 3:
   

# Generated at 2022-06-14 17:51:21.357824
# Unit test for function parseOpts
def test_parseOpts():
    # The initial, non-test values exist only to allow all of the strings
    # to be raw without the backslash-u Unicode encoding.
    hs = ['This is a full, yet short, help message.',
          'It should be exactly as long as this.']
    sys.argv = ['youtube-dl', '-h']
    try:
        parseOpts(hs)
    except (SystemExit, Exception) as err:
        assert(err.code == 0)
    sys.argv = ['youtube-dl']
    try:
        parseOpts(hs)
    except SystemExit as err:
        assert(err.code == 0)
    sys.argv = ['youtube-dl', '-h']

# Generated at 2022-06-14 17:51:30.271598
# Unit test for function parseOpts
def test_parseOpts():
    # Try to download from a completely invalid URL
    _, opts, _ = parseOpts(['foo'])
    assert(opts.verbose == False)
    assert(opts.quiet == False)
    #assert(opts.forceurl == False)
    assert(opts.forcetitle == False)
    assert(opts.simulate == False)
    assert(opts.geturl == False)
    assert(opts.gettitle == False)
    assert(opts.getid == False)
    assert(opts.getthumburl == False)
    assert(opts.getdescription == False)
    assert(opts.getfilename == False)
    assert(opts.getformat == False)
    assert(opts.usetitle == False)

# Generated at 2022-06-14 17:52:11.440932
# Unit test for function parseOpts
def test_parseOpts():
    if sys.version_info < (2, 7):
        raise unittest.SkipTest('python version < 2.7')
    import tempfile
    import shutil
    from os.path import join
    from textwrap import dedent
    from hashlib import md5

    def conf_hash(text):
        return md5(text.encode('utf-8')).hexdigest()

    def test_parse(overrideArguments, output_file_md5, global_option_md5, debug_md5, other_file_md5):
        # https://github.com/rg3/youtube-dl/issues/10476
        if sys.version_info < (3, 0):
            return

        parser, opts, args = parseOpts(overrideArguments)

# Generated at 2022-06-14 17:52:24.013601
# Unit test for function parseOpts
def test_parseOpts():
    args = ['-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio', '--merge-output-format', 'mkv', '-F', 'https://www.youtube.com/watch?v=TiaIW Neoq']

    # Check that opts and args are properly returned
    parser, opts, args = parseOpts(overrideArguments=args)
    assert opts.format == 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio'
    assert opts.merge_output_format == 'mkv'
    assert opts.list_formats is True
    assert args[0] == 'https://www.youtube.com/watch?v=TiaIW Neoq' 

    # Check that args with

# Generated at 2022-06-14 17:52:37.125142
# Unit test for function parseOpts
def test_parseOpts():
    import shlex
    from io import StringIO

    def _test_config(args, sample_output):
        stdout = sys.stdout
        sys.stdout = StringIO()

# Generated at 2022-06-14 17:52:48.726799
# Unit test for function parseOpts
def test_parseOpts():
    opts = parseOpts(['-x', '-o', '%(title)s.%(ext)s', '-f', '18', '--proxy', '1.1.1.1:3128', 'plop'])[1]
    assert opts.verbose is False
    assert opts.quiet is False
    assert opts.no_warnings is False
    assert opts.simulate is False
    assert opts.skip_download is False
    assert opts.format is None
    assert opts.listformats is False
    assert opts.outtmpl == '%(title)s.%(ext)s'
    assert opts.restrictfilenames is False
    assert opts.ignoreerrors is False
    assert opts.forcefilename is False
    assert opts.continuedl is True

# Generated at 2022-06-14 17:52:55.968898
# Unit test for function parseOpts
def test_parseOpts():
    print("test_parseOpts")
    # Test standard execution
    try:
        # This should not error
        parseOpts(["-h"])
    except:
        # Should not get here
        print("Error: unexpected error in test_parseOpts()")
        sys.exit(1)
# Test function parseOpts
test_parseOpts()

# filenameCEEncode

# Generated at 2022-06-14 17:53:04.248889
# Unit test for function parseOpts
def test_parseOpts():
    # No command line arguments
    (parser, opts, args) = parseOpts()
    assert not opts.verbose
    assert opts.username is None
    assert opts.password is None
    assert opts.usenetrc is False

    # Command line arguments
    (parser, opts, args) = parseOpts([
        '-v',
        '--username', 'spam',
        '--password', 'eggs',
        '--usenetrc'])
    assert opts.verbose
    assert opts.username == 'spam'
    assert opts.password == 'eggs'
    assert opts.usenetrc is True

test_parseOpts()

# Generated at 2022-06-14 17:53:14.741812
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-i', '-v', 'http://www.youtube.com/watch?v=BaW_jenozKc'])
    assert opts.verbose == True
    assert opts.simulate == True
    assert opts.quiet == False

    parser, opts, args = parseOpts(['--simulate', 'http://www.youtube.com/watch?v=BaW_jenozKc'])
    assert opts.verbose == False
    assert opts.simulate == True
    assert opts.quiet == False

    parser, opts, args = parseOpts(['-4', 'http://www.youtube.com/watch?v=BaW_jenozKc'])
    assert opts.ipv4 == True
    assert opts.prefer_

# Generated at 2022-06-14 17:53:26.287128
# Unit test for function parseOpts
def test_parseOpts():
    exitvalue = os.EX_OK
    (parser, opts, args) = parseOpts(['--version'])

# Generated at 2022-06-14 17:53:32.758722
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-i', '-o', '%(id)s.%(ext)s', '--', 'a', 'b'])
    assert opts.ignoreerrors is True
    assert opts.outtmpl == '%(id)s.%(ext)s'
    assert args == ['a', 'b']


# Generated at 2022-06-14 17:53:44.595115
# Unit test for function parseOpts
def test_parseOpts():
    import sys
    orig_stderr = sys.stderr
    orig_stdout = sys.stdout
    def restore():
        sys.stderr = orig_stderr
        sys.stdout = orig_stdout

# Generated at 2022-06-14 17:54:11.300502
# Unit test for function parseOpts
def test_parseOpts():
    # TODO
    pass


# Generated at 2022-06-14 17:54:19.446122
# Unit test for function parseOpts
def test_parseOpts():
    conf = ('--download-archive archive.txt '
            '--username testuser --password testpass')
    parser, opts, args = parseOpts(shlex.split(conf))
    assert opts.username == 'testuser'
    assert opts.password == 'testpass'
    assert opts.download_archive == 'archive.txt'

    conf = ('--download-archive archive.txt '
            '--username testuser --password testpass '
            '--config-location /test/youtube-dl.conf')
    parser, opts, args = parseOpts(shlex.split(conf))
    assert opts.username == 'testuser'
    assert opts.password == 'testpass'
    assert opts.download_archive == 'archive.txt'


# Generated at 2022-06-14 17:54:31.094746
# Unit test for function parseOpts
def test_parseOpts():
    opts, _ = parseOpts(['-F', '--yes-playlist', '-f', '22', 'http://www.youtube.com/watch?v=BaW_jenozKc'])
    assert opts.usenetrc == False
    assert opts.username == None
    assert opts.password == None
    assert opts.videopassword == None
    assert opts.ap_mso == None
    assert opts.ap_username == None
    assert opts.ap_password == None
    assert opts.usenetrc_machine == None
    assert opts.usenetrc_password == None
    assert opts.twofactor == None
    assert opts.twofactor_code == None
    assert opts.video_password == None
    assert opts.dump_single

# Generated at 2022-06-14 17:54:43.194557
# Unit test for function parseOpts
def test_parseOpts():
    print(
        "\n\n===\nFunction 'parseOpts' unit test\n===\n"
        "Testing 'parseOpts' with various combinations of arguments.\n"
        "If you find one that breaks, please report it at\n"
        "https://yt-dl.org/bug . Be sure to include the following test\n"
        "case information:\n"
        , file=sys.stderr)

    # Note: --simulate is the default option so we don't have to specify it.

# Generated at 2022-06-14 17:54:55.995445
# Unit test for function parseOpts
def test_parseOpts():
  import warnings
  warnings.filterwarnings('error')

  sample_args = ['ytuser:blahblah', '-i', '--min-sleep-interval=5', '--max-sleep-interval=10', \
     '--ignore-errors', '--abort-on-unavailable-fragment', '--fragment-retries=500']
  parser, opts, args = parseOpts(sample_args)
  assert opts.username == 'ytuser'
  assert opts.password == 'blahblah'
  assert opts.min_sleep_interval == 5
  assert opts.max_sleep_interval == 10
  assert opts.ignoreerrors
  assert opts.fragment_retries == 500
  assert opts.dump_intermediate_pages

# Generated at 2022-06-14 17:55:03.956969
# Unit test for function parseOpts

# Generated at 2022-06-14 17:55:13.893348
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-i'])
    assert opts.ignoreerrors
    parser, opts, args = parseOpts(['-x'])
    assert opts.extractaudio
    parser, opts, args = parseOpts(['-o', 'abc.%(ext)s'])
    assert opts.outtmpl == 'abc.%(ext)s'
    parser, opts, args = parseOpts(['--max-downloads', '20'])
    assert opts.max_downloads == 20
    parser, opts, args = parseOpts(['--match-filter', 'is_live=True'])
    assert opts.match_filter == 'is_live=True'

# Generated at 2022-06-14 17:55:20.043253
# Unit test for function parseOpts
def test_parseOpts():
    assert parseOpts(['--username', 'name', '--password', 'passwd', 'http://youtube.com/watch?v=BaW_jenozKc']).password == 'passwd'
    assert parseOpts(['--username', 'name', '--password', 'passwd', 'http://youtube.com/watch?v=BaW_jenozKc']).username == 'name'
    assert parseOpts(['--username', 'name', '--password', 'passwd', 'http://youtube.com/watch?v=BaW_jenozKc']).url == 'http://youtube.com/watch?v=BaW_jenozKc'

# Generated at 2022-06-14 17:55:31.520351
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-v', '-g', 'foobar'])
    assert opts.username == 'UNKNOWN'
    assert opts.verbose
    assert opts.extract_flat == 'in_path'
    assert opts.extract_flat == 'in_path'
    assert opts.writeinfojson
    assert opts.writedescription

    parser, opts, args = parseOpts(['-v', '-g', 'foobar', '-u', 'testuser', '--password', 'testpass'])
    assert opts.username == 'testuser'
    assert opts.password == 'testpass'


# Generated at 2022-06-14 17:55:41.625059
# Unit test for function parseOpts
def test_parseOpts():
    write_string = lambda s: None
    # Test no argument case
    parser, opts, args = parseOpts(None, write_string)
    assert not opts.usenetrc
    assert opts.noplaylist
    assert opts.download_archive == os.path.expanduser('~') + os.sep + '.youtube-dl-archive'
    assert opts.cookiefile == os.path.expanduser('~') + os.sep + '.youtube-dl-cookie'
    assert opts.nooverwrites
    assert opts.forcetitle
    assert opts.forceid
    assert opts.forcethumbnail
    assert opts.forcedescription
    assert opts.simulate
    assert not opts.geturl
    assert opts.gettitle
    assert opts

# Generated at 2022-06-14 17:56:34.787594
# Unit test for function parseOpts
def test_parseOpts():
    pass



# Generated at 2022-06-14 17:56:44.028518
# Unit test for function parseOpts
def test_parseOpts():
    from subprocess import PIPE, Popen
    from tempfile import mkstemp
    from os import remove
    from os.path import exists
    from shutil import move
    import youtube_dl.YoutubeDL
    import youtube_dl.postprocessor.ffmpeg

    def write_string(s):
        pass

    def download(ydl, *args, **kargs):
        ydl = youtube_dl.YoutubeDL.YoutubeDL(ydl)
        ydl.add_default_info_extractors()
        ydl.add_default_downloader()
        ydl.params['logger'] = MockLogger()
        ydl.params['writeinfojson'] = False
        ydl.params['simulate'] = True
        ydl.params['forcetitle'] = True

# Generated at 2022-06-14 17:56:47.856554
# Unit test for function parseOpts
def test_parseOpts():
    opts = parseOpts(['--username=foo', '--password=bar'])[1]
    assert('foo' == opts.username)
    assert('bar' == opts.password)

# vim: expandtab:ts=4:sw=4

# Generated at 2022-06-14 17:56:59.752503
# Unit test for function parseOpts
def test_parseOpts():
    # TEST1: Testing the proper handling of youtube-dl style options
    parser, opts, args = parseOpts(['-x','-f','bestvideo+bestaudio','--format=best','ytsearch:music'])
    assert opts.extractaudio == True
    assert opts.format == 'best'
    assert args == ['ytsearch:music']

    # TEST2: Testing the proper handling of getopt style options
    parser, opts, args = parseOpts(['-f','bestvideo+bestaudio','--disable-progress-bar','ytsearch:music'])
    assert opts.format == 'bestvideo+bestaudio'
    assert args == ['ytsearch:music']

    # TEST3: Testing the proper handling of getopt style options when they contain '='

# Generated at 2022-06-14 17:57:06.750132
# Unit test for function parseOpts
def test_parseOpts():
    res = parseOpts(['-F', '-f', 'best', '-a', 'test.txt', '-o', '\\%(uploader)\\%(uploader_id)s'])
    assert(res[0].format_set and res[0].format == 'best')
    assert(not res[0].usenetrc)
    assert(res[0].batchfile == 'test.txt')
    assert(res[0].outtmpl == '/%(uploader)s/%(uploader_id)s')

### Parse the command line.
# This is a generator that yields command line prior to the main
# downloader.

# Generated at 2022-06-14 17:57:10.374689
# Unit test for function parseOpts
def test_parseOpts():
    import doctest
    failed, tested = doctest.testmod()
    if not failed:
        print('Doctest: Passed')
    else:
        print('Doctest: Failed')
        sys.exit(1)

# Generated at 2022-06-14 17:57:23.111187
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts([])
    assert not opts.simulate
    assert opts.nooverwrites
    assert opts.format == '-1'
    assert not opts.geturl
    assert not opts.gettitle
    assert not opts.getid
    assert not opts.getthumb
    assert not opts.getdescription
    assert not opts.getfilename
    assert not opts.getformat
    assert not opts.skip_download
    assert opts.verbose
    assert opts.quiet
    assert opts.format
    assert opts.outtmpl
    assert not opts.usetitle
    assert opts.continuedl
    assert not opts.ratelimit
    assert not opts.noresizebuffer
    assert opts.no_warnings

# Generated at 2022-06-14 17:57:30.450944
# Unit test for function parseOpts
def test_parseOpts():
    opts, args = parseOpts(['--verbose', '--get-id', 'http://www.youtube.com/watch?v=BaW_jenozKc'])
    assert opts.verbose == True
    assert opts.geturl == False
    assert opts.gettitle == False
    assert opts.getid == True

    opts, args = parseOpts(['--get-url', '--get-title', '--get-thumbnail', '--get-description', '--get-filename', '--get-format', '--newline', 'http://www.youtube.com/watch?v=BaW_jenozKc'])
    assert opts.geturl == True
    assert opts.gettitle == True
    assert opts.getid == False
    assert opts.getthumbnail == True

# Generated at 2022-06-14 17:57:42.564511
# Unit test for function parseOpts
def test_parseOpts():
    """
    Unit test for parseOpts
    """
    parser, opts, args = parseOpts()
    # Testing defaults
    assert opts.verbose == False
    assert opts.username == None
    assert opts.password == None
    assert opts.noplaylist == False
    assert opts.forcetitles == False
    assert opts.forcethumbnail == False
    assert opts.forceid == False
    assert opts.forcedescription == False
    assert opts.forceusername == False
    assert opts.forcefilename == False
    assert opts.forcetotalvideos == False
    assert opts.updatetime == True
    assert opts.writedescription == False
    assert opts.writeinfojson == False
    assert opts.writeannotations == False
    assert opts.writ

# Generated at 2022-06-14 17:57:52.685295
# Unit test for function parseOpts
def test_parseOpts():
    from .extractor.common import InfoExtractor
    # setup
    def _parseOpts(args):
        parser, opts, _ = parseOpts(args)
        return opts

    def _test_parse_opts_equals(args, expected_opts):
        assert _parseOpts(args) == _parseOpts(expected_opts)

    opts = _parseOpts([])
    assert opts.verbose == False
    assert opts.quiet == False
    assert opts.simulate == False
    assert opts.geturl == False
    assert opts.gettitle == False
    assert opts.getid == False
    assert opts.getthumb == False
    assert opts.getdescription == False
    assert opts.getfilename == False
    assert opts.getformat == False
