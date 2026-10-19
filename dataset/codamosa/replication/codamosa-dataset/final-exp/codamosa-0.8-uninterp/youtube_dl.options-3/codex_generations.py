

# Generated at 2022-06-14 17:48:37.999292
# Unit test for function parseOpts
def test_parseOpts():
    from youtube_dl.YoutubeDL import YoutubeDL
    ydl = YoutubeDL({})
    with youtube_dl.utils.temp_dir() as tmp_dir:
        outtmpl = os.path.join(tmp_dir, '%(title)s.%(ext)s')
        assert outtmpl == parseOpts(ydl, ['--output', outtmpl])[1].outtmpl


# Generated at 2022-06-14 17:48:38.620898
# Unit test for function parseOpts
def test_parseOpts():
    pass


# Generated at 2022-06-14 17:48:41.018504
# Unit test for function parseOpts
def test_parseOpts():
    v = ['--cookies']
    parser, opts, args = parseOpts(v)
    assert opts.cookiefile is not None

test_parseOpts()

# Generated at 2022-06-14 17:48:47.755575
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts([])
    assert opts.outtmpl == '%(title)s-%(id)s.%(ext)s'
    parser, opts, args = parseOpts(['--output', '%(upload_date)s/%(title)s-%(id)s.%(ext)s'])
    assert opts.outtmpl == '%(upload_date)s/%(title)s-%(id)s.%(ext)s'
    parser, opts, args = parseOpts(['--format', 'bestvideo[height<800][height>=600][ext=mp4]+bestaudio/best[ext=mp4]/best'])

# Generated at 2022-06-14 17:48:56.366047
# Unit test for function parseOpts
def test_parseOpts():
    argv = ['--no-progress', '--simulate', 'http://youtube.com/watch?v=BaW_jenozKc']
    parser, opts, args = parseOpts(argv)
    assert opts.verbose == False
    assert opts.simulate == True
    assert args[0] == 'http://youtube.com/watch?v=BaW_jenozKc'


# Generated at 2022-06-14 17:49:05.443485
# Unit test for function parseOpts
def test_parseOpts():
    def get_parser_args(myargs):
        class Dummy(object):
            pass
        args = Dummy()
        args.__dict__['current_version'] = '2016.11.10.1'
        return parseOpts(myargs, args)

    def test(myargs, expected):
        parser, opts, args = get_parser_args(myargs)
        assert vars(opts) == expected, (vars(opts), expected)

# Generated at 2022-06-14 17:49:16.047552
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(
        ['--user-agent', 'ytdl-test', '-v',
         '--ignore-config', '--dump-user-agent', '--no-check-certificate',
         '-o', 'dummy_output', 'dummy_url'])
    assert opts.usenetrc == False
    assert opts.username == None
    assert opts.password == None
    assert opts.video_password == None
    assert opts.quiet == False
    assert opts.no_warnings == False
    assert opts.dump_user_agent == True
    assert opts.forceurl == False
    assert opts.forcetitle == False
    assert opts.forceid == False
    assert opts.forceduration == False
    assert opts.force

# Generated at 2022-06-14 17:49:27.553025
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-h'])
    assert parser and opts and args

    parser, opts, args = parseOpts(['--dump-pages', 'true'])
    assert parser and opts and args
    assert opts.dump_pages == True

    parser, opts, args = parseOpts(['-h', 'true'])
    assert parser and opts and args
    assert opts.help == True

    parser, opts, args = parseOpts(['--help', 'true'])
    assert parser and opts and args
    assert opts.help == True

    parser, opts, args = parseOpts(['--username', 'testuser'])
    assert parser and opts and args
    assert opts.username == 'testuser'


# Generated at 2022-06-14 17:49:29.988991
# Unit test for function parseOpts
def test_parseOpts():
    try:
        # executing the following line should throw the ValueError exception
        opts, args = parseOpts(['--foo', '--list-extractors'])
    except ValueError:
        return

    assert(False)
# Use this function to make a POST request.
# It takes a URL and a dictionary of name value pairs as its parameters

# Generated at 2022-06-14 17:49:40.601449
# Unit test for function parseOpts
def test_parseOpts():
    opts, _, _ = parseOpts(['-q'])
    assert not opts.verbose
    _, opts, _ = parseOpts(['-vvvvv'])
    assert opts.verbose == 4

    # Username and password should not be in the output
    opts, _, _ = parseOpts(['-u', 'user', '-p', 'pass', '--'])
    assert opts.username == 'user'
    assert opts.password == 'pass'
    assert 'user' not in repr(opts)
    assert 'pass' not in repr(opts)
    opts, _, _ = parseOpts(['-u', 'user', '-p', 'pass', 'url'])
    assert opts.username == 'user'

# Generated at 2022-06-14 17:50:04.765903
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts()
    if not args:
        parser.print_usage()
        sys.exit(1)


# Generated at 2022-06-14 17:50:14.650103
# Unit test for function parseOpts
def test_parseOpts():
    from nose.tools import assert_equal, assert_raises
    from compat import unicode

    # Test for videos
    urls = ['https://www.youtube.com/watch?v=BaW_jenozKc']
    parser, opts, args = parseOpts(urls)
    assert_equal(args, urls)

    # Test for playlists
    urls = ['https://www.youtube.com/playlist?list=PLwiyx1dc3P2JR9N8gQaQN_BCvlSlap7re']
    parser, opts, args = parseOpts(urls)
    assert_equal(args, urls)

    # Test for URLs with special characters

# Generated at 2022-06-14 17:50:23.491449
# Unit test for function parseOpts
def test_parseOpts():
    from youtube_dl.YoutubeDL import YoutubeDL
    myOpener = YoutubeDL(params = {'writedescription': True})

    (opts, _args) = myOpener.parseOpts(['--username=user','--password=pass'])
    assert opts.username == 'user'
    assert opts.password == 'pass'

    (opts, _args) = myOpener.parseOpts(['--proxy=127.0.0.1:8080'])
    assert opts.proxy == "127.0.0.1:8080"

    (opts, _args) = myOpener.parseOpts(['--geo-bypass'])
    assert opts.geo_bypass == True


# Generated at 2022-06-14 17:50:36.783508
# Unit test for function parseOpts
def test_parseOpts():
    '''
    Unit test for function parseOpts
    '''
    from youtube_dl.utils import encodeArgument
    from youtube_dl.utils import prepend_extension

    from youtube_dl import FileDownloader
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.extractor.common import InfoExtractor
    from youtube_dl.extractor.generic import GenericIE
    from youtube_dl.extractor.youtube import YoutubeIE

    _real_extract = YoutubeIE._real_extract
    _real_prepare_filename = FileDownloader.prepare_filename

    def _fake_extract(self, url):
        id_mock = 'RaW_tRaX_00'

# Generated at 2022-06-14 17:50:42.940227
# Unit test for function parseOpts
def test_parseOpts():
    assert parseOpts([])
    assert parseOpts(["--verbose"])
    conf_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "youtube_dl", "parseOpts.conf")
    assert parseOpts(["--config-location=" + conf_file])

# Parse arguments
parser, opts, args = parseOpts()



# Generated at 2022-06-14 17:50:50.489223
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-m', '-o', '/dev/null', 'http://youtube.com/watch?v=BaW_jenozKc'])
    assert(len(args) == 1)
    assert(opts.simulate)
    assert(opts.outtmpl == '/dev/null')
    assert(args[0] == 'http://youtube.com/watch?v=BaW_jenozKc')


# Generated at 2022-06-14 17:51:02.326666
# Unit test for function parseOpts
def test_parseOpts():

    # Parse opts with specific arguments
    override = '-i -u test -p pass --verbose'.split()
    parser, opts, args = parseOpts(overrideArguments=override)
    assert opts.usenetrc
    assert opts.username == 'test'
    assert opts.password == 'pass'
    assert opts.verbose
    assert not opts.quiet

    # Parse opts when youtube-dl is called from another directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    x = os.path.basename(sys.argv[0])
    sys.argv[0] = os.path.join('tests', 'test_files', x)
    parser, opts, args = parseOpts()

    # Par

# Generated at 2022-06-14 17:51:07.025015
# Unit test for function parseOpts
def test_parseOpts():
    from sys import argv
    try:
        argv[1:] = ['-U', 'abc']
        assert parseOpts()[1].username == 'abc'
    finally:
        argv[1:] = []

# Generated at 2022-06-14 17:51:15.423888
# Unit test for function parseOpts
def test_parseOpts():
    for overrideArguments in [
            None,
            ['--get-filename'],
            ['--username', 'foo', '--password', 'bar'],
            ['--extract-audio', '--audio-format', 'mp3', 'foo']]:
        parser, opts, args = parseOpts(overrideArguments)
        print(opts, args)
        # This will raise if something is wrong
        parser.error('test_parseOpts: %s\n  opts: %s\n  args: %s' % (overrideArguments, opts, args))


# Generated at 2022-06-14 17:51:27.143333
# Unit test for function parseOpts
def test_parseOpts():
    try:
        parser, opts, args = parseOpts(['-i', '-q'])
        assert(opts.verbose == 0), opts.verbose
        assert(opts.quiet == True), opts.quiet
        assert(opts.no_warnings == False), opts.no_warnings
        assert(args == []), args
    except (SystemExit, Exception) as err:
        print('test parseOpts FAIL')
        print(err)
        traceback.print_exc()
        assert(False)
    else:
        print('test parseOpts ok')

test_parseOpts()

# def parseOpts(overrideArguments=None):
#     """
#     Parse the command line options returning a tuple with an
#     OptionParser object, options and arguments.
#

# Generated at 2022-06-14 17:52:01.353420
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-x', '-v', '-g', 'asd--efg', '-f', '22'])
    assert(opts.verbose)
    assert(opts.username is None)
    assert(opts.password is None)
    assert(opts.usenetrc)
    assert(opts.ratelimit is None)
    assert(opts.retries == 10)
    assert(opts.buffersize is None)
    assert(opts.noresizebuffer)
    assert(opts.playliststart == 1)
    assert(opts.playlistend == -1)
    assert(opts.matchtitle == 'asd--efg')
    assert(opts.rejecttitle == '')

# Generated at 2022-06-14 17:52:11.646275
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-f', '37', 'http://youtube.com/watch?v=BaW_jenozKc'])

    assert opts.format == '37'
    assert len(args) == 1
    assert args[0] == 'http://youtube.com/watch?v=BaW_jenozKc'
    assert opts.noplaylist is True

    parser, opts, args = parseOpts(['-f', '37/18', 'http://youtube.com/watch?v=BaW_jenozKc'])

    assert opts.format == '37/18'
    assert len(args) == 1
    assert args[0] == 'http://youtube.com/watch?v=BaW_jenozKc'
    assert opts.noplaylist

# Generated at 2022-06-14 17:52:19.160255
# Unit test for function parseOpts
def test_parseOpts():
    def create_config_file(name, content):
        with open(name, 'w') as f:
            f.write(content)

    config_file = mkstemp(prefix='youtube-dl-', suffix='.conf')[1]
    create_config_file(config_file, '-o foo\n')


# Generated at 2022-06-14 17:52:30.873784
# Unit test for function parseOpts
def test_parseOpts():
    from sys import argv
    from unittest import TestCase
    class FakePopen:
        def __init__(self, *args, **kwargs):
            self.communicate_args = args
            self.communicate_kwargs = kwargs
        def communicate(self, *args, **kwargs):
            self.communicate_args = args
            self.communicate_kwargs = kwargs
            return (b'youtube-dl version 2016.02.03\n', b'')
    class ParseOptsTest(TestCase):
        def test_noargs(self):
            class Result(dict):
                def __init__(self):
                    self['input'] = []
                    self['output'] = []
                    self['returncode'] = 0

# Generated at 2022-06-14 17:52:33.811817
# Unit test for function parseOpts
def test_parseOpts():
    logger.debug('Calling function parseOpts')
    parser, opts, args = parseOpts()
    logger.debug('Function parseOpts returned')
    for key, value in opts.__dict__.items():
        logger.debug('Option %s => %s' % (repr(key), repr(value)))


# Generated at 2022-06-14 17:52:37.803898
# Unit test for function parseOpts
def test_parseOpts():
    write_string('Testing parseOpts\n')
    assert parseOpts() is not None

 
# getdownloader
# Function to select downloader
# @param downloader list of downloader
# @param extractor list of extractor

# Generated at 2022-06-14 17:52:49.633786
# Unit test for function parseOpts
def test_parseOpts():
    args = ['-i', '--yes-playlist']
    parser, opts, args = parseOpts(args)
    assert opts.noplaylist is False
    assert opts.ignoreerrors is True
    assert opts.simulate is False
    assert opts.format == 'bestvideo+bestaudio/best'
    assert opts.outtmpl == '%(title)s-%(id)s.%(ext)s'
    assert opts.restrictfilenames is False
    assert opts.ignoreconfig is True
    assert opts.listsubtitles is False
    assert opts.listsubtitles is False
    assert opts.writeautomaticsub is False
    assert opts.allsubtitles is False
    assert opts.subtitleslangs == []
    assert opts.match

# Generated at 2022-06-14 17:52:55.558120
# Unit test for function parseOpts
def test_parseOpts():
    assert parseOpts(['-v'])[1].verbose == True
    assert parseOpts(['--ignore-config'])[1].ignoreconfig == True
    assert parseOpts(['--output', 'abc.txt'])[1].outtmpl == 'abc.txt'

# Generated at 2022-06-14 17:53:04.742532
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts()
    assert opts.get('username') is None
    assert opts.get('password') is None
    assert opts.get('usenetrc') is False
    assert opts.get('verbose') is False
    assert opts.get('quiet') is False
    assert opts.get('no_warnings') is False
    assert opts.get('forceurl') is False
    assert opts.get('forcetitle') is False
    assert opts.get('forceid') is False
    assert opts.get('forceduration') is False
    assert opts.get('forcethumbnail') is False
    assert opts.get('forcedescription') is False
    assert opts.get('forcefilename') is False
    assert opts.get('forceformat') is None

# Generated at 2022-06-14 17:53:10.788892
# Unit test for function parseOpts
def test_parseOpts():
    (_, opts, _) = parseOpts()
    assert opts.username is None

# downloader options

# Generated at 2022-06-14 17:54:01.350767
# Unit test for function parseOpts
def test_parseOpts():
    options = ['--username=test',
               '--password=test',
               '--verbose']

    class _UnsupportedOption(object):
        def __init__(self, opts):
            self.opts = opts.split()

        def parse_args(self, args):
            return self.opts, args

    parser = _UnsupportedOption(options)
    options, args = parseOpts(parser)
    assert options.username == 'test'
    assert options.password == 'test'
    assert options.verbose

    # Test for hidden login info
    assert not _hide_login_info(['--username=test', '--password=test', '--verbose']).count('test')


# Generated at 2022-06-14 17:54:03.019326
# Unit test for function parseOpts
def test_parseOpts():
    # FIXME
    return


# -- Helpers


# Generated at 2022-06-14 17:54:15.832550
# Unit test for function parseOpts

# Generated at 2022-06-14 17:54:21.967869
# Unit test for function parseOpts
def test_parseOpts():
    # For testing purposes only
    opts, args = parseOpts(shlex.split(u'--username=foo --password=bar --extract-audio --audio-format best --audio-quality 0 -x --verbose'.encode('utf-8')))
    assert 'foo' == opts.username
    assert 'bar' == opts.password
    assert True == opts.extractaudio
    assert 'best' == opts.audioformat
    assert 0 == opts.audioquality
    assert True == opts.verbose
    assert [] == args

    opts, args = parseOpts(shlex.split(u'--format mp4 -f 22/17/best/18'.encode('utf-8')))
    assert ['22', '17', 'best', '18'] == opts.format
    assert [] == args



# Generated at 2022-06-14 17:54:28.428667
# Unit test for function parseOpts
def test_parseOpts():
    print('[Running] test_parseOpts')
    parser, opts, _ = parseOpts()
    assert opts.username == 'u'
    assert opts.password == 'p'
    assert opts.usenetrc == True
    assert opts.verbose == True
    print('[Passed] test_parseOpts')


# Generated at 2022-06-14 17:54:39.304345
# Unit test for function parseOpts
def test_parseOpts():
    def _test_parser_state(parser, options, positional, hidden_login_info=False):
        write_string = get_write_string()
        parser.print_help = lambda file=None: file.write('help\n')
        help_shown = []
        def _write_help(msg):
            help_shown.append('help' in msg)
        get_write_string()(lambda *args, **kargs: _write_help(args[0]))
        parser.error = lambda msg: _write_help('error: ' + msg)
        if hidden_login_info:
            options = ['--username', 'foo', '--password', 'bar', '--video-password', 'baz']

# Generated at 2022-06-14 17:54:43.852605
# Unit test for function parseOpts
def test_parseOpts():
    print('testing parseOpts')
    assert parseOpts(overrideArguments=['--playlist-start', '5', '--playlist-end', '10'])[2] == ['--playlist-start', '5', '--playlist-end', '10']


# Generated at 2022-06-14 17:54:56.442564
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts()
    if opts.verbose:
        write_string('[debug] System config: ' + repr(_hide_login_info(['--ignore-config'] + _readOptions('/etc/youtube-dl.conf'))) + '\n')
        write_string('[debug] User config: ' + repr(_hide_login_info(_readUserConf())) + '\n')
        write_string('[debug] Custom config: ' + repr(_hide_login_info(opts.config_location)) + '\n')
        write_string('[debug] Command-line args: ' + repr(_hide_login_info(sys.argv)) + '\n')


# Generated at 2022-06-14 17:55:04.174783
# Unit test for function parseOpts
def test_parseOpts():
    opts, args = parseOpts([
        '-i', 'http://www.youtube.com/watch?v=BaW_jenozKc',
        '--',
        '--youtube-include-dash-manifest',
        '-v'
    ])
    assert opts.verbose
    assert opts.usenetrc
    assert opts.username is None
    assert opts.password is None
    assert opts.youtube_include_dash_manifest
    assert opts.noplaylist

    opts, args = parseOpts(['-u', 'foo', '-p', 'bar',
                            '--', '--youtube-include-dash-manifest',
                            '-v'])
    assert opts.verbose
    assert opts.username == 'foo'

# Generated at 2022-06-14 17:55:14.057293
# Unit test for function parseOpts
def test_parseOpts():
    from youtube_dl.compat import parseOpts
    from tempfile import NamedTemporaryFile
    from copy import deepcopy
    import os


# Generated at 2022-06-14 17:56:51.807190
# Unit test for function parseOpts
def test_parseOpts():
    from YoutubeDL.compat import compat_shlex_quote
    from YoutubeDL import __main__ # pylint: disable=no-name-in-module

# Generated at 2022-06-14 17:57:02.178199
# Unit test for function parseOpts
def test_parseOpts():
    from .__main__ import parseOpts
    def get_opts(overrideArguments):
        parser, opts, args = parseOpts(overrideArguments)
        return opts
    assert get_opts(['--no-check-certificate', '-v', '--list-formats']).listformats
    assert get_opts(['--no-check-certificate', '-v', '--list-formats', '--verbose']).verbose
    assert get_opts(['--no-check-certificate', '-v', '--list-formats', '--verbose', '-v']).verbose > 1
    assert not get_opts([]).noprogress
    assert get_opts([]).format == 'best'
    assert get_opts([]).outtmpl

# Generated at 2022-06-14 17:57:10.275784
# Unit test for function parseOpts
def test_parseOpts():
    opts, args = parseOpts()
    assert opts.quiet is False
    opts, args = parseOpts(["--quiet"])
    assert opts.quiet is True
    opts, args = parseOpts(["--output", "output-%(autonumber)s.%(ext)s"])
    assert opts.outtmpl == "output-%(autonumber)s.%(ext)s"

# Generated at 2022-06-14 17:57:17.124648
# Unit test for function parseOpts
def test_parseOpts():
    from optparse import OptionParser
    from optparse import Values
    from .compat import compat_str

    original_sys_argv = sys.argv
    original_user_agent = std_headers['User-Agent']
    original_preferredencoding = preferredencoding


# Generated at 2022-06-14 17:57:21.509438
# Unit test for function parseOpts
def test_parseOpts():
    # parseOpts returns tuple (OptionParser, Options, args)
    parser, opts, args = parseOpts()
    assert type(parser) is optparse.OptionParser
    assert type(opts) is optparse.Values
    assert type(args) is list


# Generated at 2022-06-14 17:57:22.150034
# Unit test for function parseOpts
def test_parseOpts():
    assert parseOpts([]) == False


# Generated at 2022-06-14 17:57:28.317746
# Unit test for function parseOpts
def test_parseOpts():
    import tempfile
    tmp = tempfile.NamedTemporaryFile(delete=False)
    with open(tmp.name, 'wb') as f:
        f.write(b'--username=test\n')
    # sys.argv is required to parse the default config file
    sys.argv += ['--username=blabla', '--config-location=' + tmp.name]
    parser, opts, args = parseOpts()
    assert opts.username == 'test'
    os.unlink(tmp.name)
    sys.argv.pop()
    sys.argv.pop()



# Generated at 2022-06-14 17:57:33.662003
# Unit test for function parseOpts
def test_parseOpts():
    from .utils import encodeArgument

    parser, options, args = parseOpts(['--default-search', 'ytsearch', 'test'])
    assert options.default_search == 'ytsearch'
    assert args == ['test']

    parser, options, args = parseOpts([encodeArgument('--default-search'), encodeArgument('ytsearch'), encodeArgument('test')])
    assert options.default_search == 'ytsearch'
    assert args == ['test']

    parser, options, args = parseOpts([encodeArgument('--default-search'), encodeArgument('ytsearch'), encodeArgument('test')], ['--default-search', 'gvsearch', 'test2'])
    assert options.default_search == 'gvsearch'
    assert args == ['test2']



# Generated at 2022-06-14 17:57:34.745575
# Unit test for function parseOpts
def test_parseOpts():
    #TODO write unit test
    pass


# Generated at 2022-06-14 17:57:46.744278
# Unit test for function parseOpts
def test_parseOpts():
    # Check if the parser does not crash with -h
    parser, _, _ = parseOpts(['-h'])

    # Check if the usage message is shown correctly
    parser, _, _ = parseOpts(['-h'])
    usage = parser.format_help()
    assert 'Generic Options' in usage
    assert 'URL' in usage
    assert 'youtube-dl' in usage
    assert 'positional arguments' in usage
    assert 'optional arguments' in usage

    # Check if the output template is shown correctly
    parser, _, _ = parseOpts(['-h'])
    usage = parser.format_help()
    assert '%(upload_date)s' in usage
    assert '%(extractor)s' in usage
    assert '%(uploader)s' in usage