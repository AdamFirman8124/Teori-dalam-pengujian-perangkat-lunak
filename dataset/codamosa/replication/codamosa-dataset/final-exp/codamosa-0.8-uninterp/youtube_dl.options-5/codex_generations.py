

# Generated at 2022-06-14 17:48:23.928532
# Unit test for function parseOpts
def test_parseOpts():
    print()
    print('# Starting unit test for function parseOpts')

    try:
        parser, opts, args = parseOpts()
    except:
        write_string('ERROR: parseOpts raised an exception\n')
        return False

    write_string('# Unit test for function parseOpts completed')
    return True


# Generated at 2022-06-14 17:48:30.559559
# Unit test for function parseOpts
def test_parseOpts():
    # Test different ways of overriding configs
    # Test default config
    parser, opts, args = parseOpts(None)
    assert opts.verbose == 2
    assert opts.outtmpl == '%(title)s-%(id)s.%(ext)s'
    assert opts.writeannotations == False
    assert opts.simulate == False
    assert opts.writethumbnail == False
    assert opts.call_home == True
    # Test system config
    parser, opts, args = parseOpts(['-v', '--no-call-home', '--verify-ip'])
    assert opts.verbose == 3
    assert opts.call_home == False
    assert opts.verify_ip == True
    # Test override config

# Generated at 2022-06-14 17:48:32.584958
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, _ = parseOpts(['-U', 'testtt', '-P', 'testpp'])
    assert opts.username == 'testtt'
    assert opts.password == 'testpp'



# Generated at 2022-06-14 17:48:42.248523
# Unit test for function parseOpts
def test_parseOpts():
    from youtube_dl.utils import DateRange
    parser, opts, args = parseOpts(['-i', '-R0', '--dateafter', '20000704', '--datebefore', '200010011'])
    assert opts.playliststart == 1
    assert opts.playlistend == 0
    assert opts.daterange == DateRange(after='20000704', before='200010011')
    assert args == []

    parser, opts, args = parseOpts(['--playlist-start', '1', '--playlist-end', '2', '--dateafter', '20000704', '--datebefore', '200010011'])
    assert opts.playliststart == 1
    assert opts.playlistend == 2

# Generated at 2022-06-14 17:48:51.082063
# Unit test for function parseOpts
def test_parseOpts():
    def parse(overrideArguments):
        return parseOpts(overrideArguments=overrideArguments)[1].__dict__
    def remove_volatile_keys(d):
        volatile = (
            'username', 'password', 'twofactor', 'videopassword', 'ap_password', 'ap_username')
        return dict((k, v) for k, v in d.items() if k not in volatile)

    assert parse([]) == remove_volatile_keys({})
    assert parse(['-U', 'Foo']) == remove_volatile_keys({'updatetime': True})
    assert parse(['--no-check-certificate']) == remove_volatile_keys({'nocheckcertificate': True})

# Generated at 2022-06-14 17:48:53.263109
# Unit test for function parseOpts
def test_parseOpts():
    # Some tests are in test_YoutubeDL.test_parseOpts
    return True



# Generated at 2022-06-14 17:49:03.230833
# Unit test for function parseOpts
def test_parseOpts():
    from youtube_dl.compat import compat_shlex_split

    def test_parse(args, result):
        parser, opts, args = parseOpts(overrideArguments=args)
        assert vars(opts) == result

    def test_parse_all(args, result):
        args = compat_shlex_split(args)
        test_parse(args, result)

    # General

# Generated at 2022-06-14 17:49:07.392492
# Unit test for function parseOpts
def test_parseOpts():
    from sys import argv
    argv = ['-v', '-o', '%(id)s.%(ext)s', 'https://www.youtube.com/watch?v=BaW_jenozKc']
    res = parseOpts(argv)
    print(res)
# test: -v -o %(id)s.%(ext)s https://www.youtube.com/watch?v=BaW_jenozKc
# test_parseOpts()


# Generated at 2022-06-14 17:49:10.355557
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts()
    assert opts.username == 'testusername'
    assert opts.password == 'testpassword'
# Retrieve content from a URL

# Generated at 2022-06-14 17:49:14.462205
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, _ = parseOpts([
        '--format=22',
        '--verbose',
        '--ignore-config',
        '--config-location=/tmp/foo.conf',
        'https://www.youtube.com/watch?v=BaW_jenozKc'
    ])
    assert opts.format == '22'
    assert opts.verbose == True
    assert opts.ignoreconfig == True
    assert opts.config_location == '/tmp/foo.conf'


# Generated at 2022-06-14 17:49:35.298480
# Unit test for function parseOpts
def test_parseOpts():
    def _test_parsing(args, expected):
        assert parseOpts(args)[1].__dict__ == expected

    _test_parsing([], {})
    _test_parsing(['-o', '%(title)s.%(ext)s', '-a', 'my-title.txt', '--foo-bar'], {
        'outtmpl': u'%(title)s.%(ext)s',
        'batchfile': u'my-title.txt',
        'foo_bar': True})
    _test_parsing(['--', '--foo-bar'], {'foo_bar': True})


# Generated at 2022-06-14 17:49:44.183391
# Unit test for function parseOpts
def test_parseOpts():
    if sys.version_info < (3,):
        return

    if not os.path.exists('youtube-dl.conf'):
        with open('youtube-dl.conf', 'w') as f:
            f.write('''
--proxy 127.0.0.1:1080
--proxy 127.0.0.2:1081
-f mp4
-f m4a
-f flv
''')
    parser, opts, args = parseOpts(['-f', 'avi', 'https://www.youtube.com/watch?v=BaW_jenozKc'])
    assert opts.format == ['avi']
    assert args == ['https://www.youtube.com/watch?v=BaW_jenozKc']


# Generated at 2022-06-14 17:49:49.734656
# Unit test for function parseOpts
def test_parseOpts():
    import sys
    import os
    import tempfile

    (fd, config_location) = tempfile.mkstemp()
    os.write(fd, b'--extract-audio\n')
    os.close(fd)

    def clean():
        os.remove(config_location)

    sys.argv = ['youtube-dl', '--ignore-config', '--no-mtime', '--3d', '--sleep-interval', '120', '-f', '22/17/43', '--hls-prefer-native', '-o', '%(autonumber)s.%(ext)s', 'https://www.youtube.com/watch?v=BaW_jenozKc', 'http://www.youtube.com/watch?v=yZ_4lgv-vEs']
    parser,

# Generated at 2022-06-14 17:49:57.407161
# Unit test for function parseOpts

# Generated at 2022-06-14 17:50:10.980291
# Unit test for function parseOpts
def test_parseOpts():
    # NOTE: unit tests should use None to ensure no overrideArguments are passed
    #       and thus produce the same results as in actual usage
    #       parseOpts(['-U', 'foobar']) # is the same as parseOpts(['-U', 'foobar'], overrideArguments=['-U', 'foobar'])
    parser, opts, args = parseOpts(['-U', 'foobar'])
    assert opts.username == 'foobar'
    assert args == []
    parser, opts, args = parseOpts(['--no-call-home'])
    assert opts.call_home == False
    assert opts.username is None
    assert opts.password is None
    assert args == []
    parser, opts, args = parseOpts(['-R', '123456'])


# Generated at 2022-06-14 17:50:20.975757
# Unit test for function parseOpts
def test_parseOpts():
    from youtube_dl.utils import preferredencoding
    import sys

    if sys.version_info >= (3, 0):
        from io import StringIO
    else:
        from StringIO import StringIO

    s = StringIO()
    sys.stdout = s

    old_stdout = sys.stdout
    sys.stdout = StringIO()


# Generated at 2022-06-14 17:50:28.182052
# Unit test for function parseOpts
def test_parseOpts():
    """Unit test for function parseOpts."""
    parser, opts, args = parseOpts([])
    checkEqual(args, [])
    checkEqual(opts.verbose, False)
    checkEqual(opts.quiet, False)
    checkEqual(opts.no_warnings, False)
    checkEqual(opts.simulate, False)
    checkEqual(opts.format, None)
    checkEqual(opts.listformats, False)
    checkEqual(opts.usagestats, False)
    checkEqual(opts.dump_user_agent, False)
    checkEqual(opts.dump_intermediate_pages, False)
    checkEqual(opts.write_pages, False)

# Generated at 2022-06-14 17:50:38.432313
# Unit test for function parseOpts
def test_parseOpts():
    def test_parseOpts_string(overrideArguments, expectedArguments):
        parser, actualArguments, args = parseOpts({'overrideArguments': overrideArguments})
        assert_equal(actualArguments, expectedArguments)

    def test_parseOpts_list(overrideArguments, expectedArguments):
        parser, actualArguments, args = parseOpts({'overrideArguments': overrideArguments})
        assert_equal(actualArguments.__dict__, expectedArguments)

    ##
    # Specific tests
    #
    # --no-check-certificate
    test_parseOpts_string(
        ['--no-check-certificate'],
        {'nocheckcertificate': True})
    # -4

# Generated at 2022-06-14 17:50:50.032526
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(overrideArguments=['-U', 'test_user', '-P', 'test_password', '-i', 'http://www.youtube.com/watch?v=BaW_jenozKc'])
    assert opts.username == 'test_user'
    assert opts.password == 'test_password'
    assert args == ['http://www.youtube.com/watch?v=BaW_jenozKc']
    assert not opts.quiet
    assert opts.format == 'best'
    assert opts.restrictfilenames # restrictfilenames by default
    assert opts.cachedir is not None

# Generated at 2022-06-14 17:50:57.538673
# Unit test for function parseOpts
def test_parseOpts():
    def testopt(arguments, name, value):
        if value == True:
            assert arguments.name == value, 'parseOpts failed at --name option'
        elif value == False:
            assert arguments.name == value, 'parseOpts failed at --no-name option'
        else:
            assert arguments.name == value, 'parseOpts failed at --name=' + value

    arguments = parseOpts(['--username=dos', '--no-call-home', '--write-sub'])[1]
    testopt(arguments, username, 'dos')
    testopt(arguments, call_home, False)
    testopt(arguments, writesub, True)

    arguments = parseOpts(['--username=dos', '--no-username', '--call-home'])[1]

# Generated at 2022-06-14 17:51:17.871518
# Unit test for function parseOpts
def test_parseOpts():
    class Namespace(object):
        pass
    opts = Namespace()
    args = []
    opts.username = 'foo'
    opts.password = 'bar'
    opts.ap_username = 'bla'
    opts.ap_password = 'baz'
    argv = sys.argv[1:]
    argv = _hide_login_info(argv)
    assert argv != sys.argv[1:]
    parser, opts, args = parseOpts(argv, opts, args)
    assert opts.username != 'foo'
    assert opts.password != 'bar'
    assert opts.ap_username != 'bla'
    assert opts.ap_password != 'baz'


# User interaction stuff


# Generated at 2022-06-14 17:51:28.470410
# Unit test for function parseOpts
def test_parseOpts():
    from .compat import parse_qs, parse_qsl


# Generated at 2022-06-14 17:51:33.289377
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['--username=foo', '--password=bar', '--', '-v', '--output=-', 'https://www.youtube.com/watch?v=BaW_jenozKc'])
    assert opts.username == 'foo'
    assert opts.password is None
    assert opts.verbose
    assert opts.outtmpl == '-'
    assert 'BaW_jenozKc' in args


# Generated at 2022-06-14 17:51:38.902530
# Unit test for function parseOpts
def test_parseOpts():
    from .YoutubeDL import YoutubeDL
    ydl = YoutubeDL()
    ydl.params = dict()
    parser, opts, args = parseOpts(ydl, None)
    return parser, opts, args


# Extracts the available formats of a URL

# Generated at 2022-06-14 17:51:49.522587
# Unit test for function parseOpts
def test_parseOpts():
    from collections import namedtuple
    Options = namedtuple('Options', ['outtmpl', 'postprocessor_args', 'format', 'usenetrc', 'username', 'password', 'videopassword', 'verbose', 'simulate', 'skip_download', 'nooverwrites', 'forcetitle', 'forceurl', 'forcedescription', 'forcethumbnail', 'forceduration', 'forcefilename', 'forcejson', 'dump_intermediate_pages'])
    Options.__new__.__defaults__ = (None,) * len(Options._fields)

# Generated at 2022-06-14 17:51:59.895418
# Unit test for function parseOpts
def test_parseOpts():
    from sys import argv
    opts, args = parseOpts(['--usenetrc', '--username', 'foo', '--password', 'bar', 'youtube.com'])
    assert 'usenetrc' in opts
    assert opts.usenetrc
    assert 'username' in opts
    assert opts.username == 'foo'
    assert 'password' in opts
    assert opts.password == 'bar'
    opts, args = parseOpts(['youtube.com'])
    assert 'usenetrc' not in opts
    assert not opts.usenetrc
    assert 'username' not in opts
    assert 'password' not in opts



# Generated at 2022-06-14 17:52:10.568574
# Unit test for function parseOpts
def test_parseOpts():
    # Disable log messages to keep unittest output clean
    disable_debug_loggin()
    # Unit test requires print_debug to be available
    global print_debug

    def _parseOpts(argv, overrideArguments=None):
        if argv is None:
            argv = []
        parser, opts, args = parseOpts(argv, overrideArguments)
        return {k: v for k, v in vars(opts).items() if k in parser.option_list}

    def _parseOptsError(argv):
        try:
            _parseOpts(argv)
        except (optparse.OptionValueError, TypeError, ValueError) as err:
            return str(err)
        raise AssertionError('No exception raised')


# Generated at 2022-06-14 17:52:11.603929
# Unit test for function parseOpts
def test_parseOpts():
    _ = parseOpts()

# Generated at 2022-06-14 17:52:19.100495
# Unit test for function parseOpts
def test_parseOpts():
    import tempfile
    class Object(object):
        pass
    opts = Object()
    opts.verbose = 0
    opts.quiet = False
    opts.username = None
    opts.password = None
    opts.twofactor = None
    opts.videopassword = None
    opts.ap_mso = None
    opts.ap_username = None
    opts.ap_password = None
    opts.usenetrc = False
    opts.ratelimit = None
    opts.retries = 10
    opts.fragment_retries = 10
    opts.skip_unavailable_fragments = False
    opts.buffersize = 1024
    opts.noresizebuffer = True
    opts.test = False
    opts.play

# Generated at 2022-06-14 17:52:30.801475
# Unit test for function parseOpts

# Generated at 2022-06-14 17:52:46.401314
# Unit test for function parseOpts
def test_parseOpts():
    import doctest
    fails, _ = doctest.testmod()
    assert fails == 0


# Generated at 2022-06-14 17:52:58.622657
# Unit test for function parseOpts
def test_parseOpts():
    from youtube_dl.utils import match_filter_func
    _, opts, args = parseOpts(['--playlist-start', '23', '--playlist-end', '42', 'xkcd'])
    assert opts.playlist_start == 23
    assert opts.playlist_end == 42
    assert args == ['xkcd']
    _, opts, args = parseOpts(['--match-filter', 'duration > 600', 'xkcd'])
    assert opts.match_filter == 'duration > 600'
    assert match_filter_func('duration > 600')('duration', 600) is False
    assert match_filter_func('duration > 600')('duration', 601) is True


# Generated at 2022-06-14 17:53:04.720745
# Unit test for function parseOpts
def test_parseOpts():
    opt = parseOpts.parseOpts(['--flat-playlist', '--extract-audio'])
    assert opt.flat_playlist
    assert opt.extract_audio

    opt = parseOpts.parseOpts(['-o', 'myvideo.mp4'])
    assert opt.outtmpl == 'myvideo.mp4'
    assert opt.noplaylist is True

    opt = parseOpts.parseOpts(['--format', 'bestvideo+bestaudio'])
    assert opt.format_limit == 'bestvideo+bestaudio'

    opt = parseOpts.parseOpts(['https://www.youtube.com/watch?v=BaW_jenozKc'])
    assert opt.url == ['https://www.youtube.com/watch?v=BaW_jenozKc']

   

# Generated at 2022-06-14 17:53:15.000887
# Unit test for function parseOpts
def test_parseOpts():
    from sys import argv
    from io import StringIO
    from youtube_dl.utils import decode_compat_str
    from json import loads
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    stdout = StringIO()
    stderr = StringIO()
    sys.stdout = stdout
    sys.stderr = stderr
    argv = ['youtube-dl']
    old_argv = argv[:]

# Generated at 2022-06-14 17:53:26.450529
# Unit test for function parseOpts
def test_parseOpts():
    from io import StringIO
    from sys import argv
    # We know that --video-format is not a valid option, so if we get an error
    # there it's OK
    with StringIO() as err:
        with noStderr():
            opts, args = parseOpts(['--config-location', 'test/testconf.conf', '--video-format', '22'], err)
        assert ('--video-format' in err.getvalue())
    assert (opts.format == '0')
    assert (opts.username == 'testuser')
    assert (opts.password == 'testpass')
    assert (opts.outtmpl == 'test value')
    assert (opts.ap_mso == 'test mso')
    assert (opts.ap_username == 'test apuser')
   

# Generated at 2022-06-14 17:53:29.416630
# Unit test for function parseOpts
def test_parseOpts():
    print('Testing parseOpts')
    parser, opts, args = parseOpts([])
    assert opts.usenetrc

# Processes the query passed by the user

# Generated at 2022-06-14 17:53:33.656580
# Unit test for function parseOpts
def test_parseOpts():
    sys.argv = [
        sys.argv[0],
        '-i',
        'ytuser:hellworld']
    try:
        parseOpts()
    except (compat_optparse.OptionValueError, optparse.OptionValueError):
        pass

# Generated at 2022-06-14 17:53:45.649244
# Unit test for function parseOpts
def test_parseOpts():
    import sys

    # In order to test ydl.parseOpts() via command line,
    # sys.argv must not contain any argument.
    try:
        sys.argv.remove('--noplaylist')
    except:
        pass

    parser, opts, args = parseOpts({'verbose': True})

    # Test parseOpts()
    parser.parse_args(['-4', '--max-downloads=10'])

    if not opts.noplaylist:
        playliststart = opts.playliststart
        playlistend = opts.playlistend
        matchtitle = opts.matchtitle
        rejecttitle = opts.rejecttitle
        logger.debug('playlist start: ' + str(playliststart))

# Generated at 2022-06-14 17:53:49.451011
# Unit test for function parseOpts
def test_parseOpts():
    assert parseOpts( ['--username', 'foo', '--password', 'bar'] )[1].username == 'foo'


_ENV_HEADERS = ['X-Forwarded-For', 'User-Agent', 'Cookie']



# Generated at 2022-06-14 17:53:54.333925
# Unit test for function parseOpts
def test_parseOpts():
    from youtube_dl.compat import compat_configparser
    from youtube_dl.utils import _hide_login_info


# Generated at 2022-06-14 17:54:37.955368
# Unit test for function parseOpts
def test_parseOpts():
    # Use parseOpts to obtain the parser and other parameters
    parser, opts, args = parseOpts()
    # Test if the parser is correctly generated
    assert(opts.usenetrc is True)
    assert(opts.youtube_include_dash_manifest is True)
    assert(opts.nooverwrites is False)
    assert(opts.cachedir is None)
    # Test if argument is added correctly
    opts1, args1 = parseOpts(overrideArguments=['--usenetrc', 'false'])
    assert(opts1.usenetrc is False)
    opts2, args2 = parseOpts(overrideArguments=['--cachedir', '.'])
    assert(opts2.cachedir == '.')
    # Test if non-existent

# Generated at 2022-06-14 17:54:51.127953
# Unit test for function parseOpts
def test_parseOpts():
    args = ['-U', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:13.0) Gecko/20100101 Firefox/13.0.1', '--verbose', '--no-progress', '--max-downloads', '2', '--', 'rtmp://host/path/to']
    # Testing parseOpts
    _, opts, args = parseOpts(args)
    sys.argv = sys.argv[:1]
    assert opts.max_downloads == 2
    assert opts.noprogress is True
    assert opts.verbose is True
    assert opts.usenetrc is False
    assert opts.username is None
    assert opts.password is None
    assert opts.quiet is False
    assert opts.simulate

# Generated at 2022-06-14 17:55:01.964172
# Unit test for function parseOpts

# Generated at 2022-06-14 17:55:08.418947
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-h'])
    assert not args
    parser, opts, args = parseOpts(['-U', 'test user agent'])
    assert opts.user_agent == 'test user agent'
    parser, opts, args = parseOpts(['--proxy', 'test proxy'])
    assert opts.proxy == 'test proxy'
    parser, opts, args = parseOpts(['-u', 'test username', '-p', 'test passwd', '-n', 'test netrc_machine'])
    assert opts.username == 'test username'
    assert opts.password == 'test passwd'
    assert opts.usenetrc == False
    assert not opts.nopart

# Generated at 2022-06-14 17:55:21.484988
# Unit test for function parseOpts
def test_parseOpts():
    """Test for function parseOpts"""
    
    # Initialize parser
    parser = optparse.OptionParser()
    parser.add_option('-v', '--verbose', action='store_true', dest='verbose', default=False)
    general = optparse.OptionGroup(parser, 'General Options')
    general.add_option('--version', action='store_true', help='Print program version')
    general.add_option('--ignore-config', action='store_true', help='Do not read configuration files')
    general.add_option('--config-location', metavar='PATH', help='Location of the configuration file; either the path to the file or its containing directory.')

# Generated at 2022-06-14 17:55:31.935512
# Unit test for function parseOpts
def test_parseOpts():
    def _test(args, overrideArguments=None, expected=None):
        parser, opts, args = parseOpts(args, overrideArguments)
        if expected is None:
            expected = {'opts': {}, 'args': []}
        assertEquals(expected['opts'], opts.__dict__)
        assertEquals(expected['args'], args)
    # empty args
    _test([], expected={'opts': {}, 'args': []})
    # boolean options
    _test(['--yes-playlist'], expected={'opts': {'noplaylist': False, 'yes_playlist': True}, 'args': []})

# Generated at 2022-06-14 17:55:41.910080
# Unit test for function parseOpts
def test_parseOpts():
    from collections import namedtuple
    TestOption = namedtuple('TestOption', ['dest', 'default', 'metavar', 'nargs', 'action'])
    TestArgument = namedtuple('TestArgument', ['option_strings', 'dest', 'nargs', 'const', 'default', 'type', 'choices', 'required', 'help', 'metavar'])

    def _testOption(**kwargs):
        return TestOption(**kwargs)


    def _testArgument(*option_strings, **kwargs):
        return TestArgument(option_strings, **kwargs)


    # Test option groups

# Generated at 2022-06-14 17:55:43.624754
# Unit test for function parseOpts
def test_parseOpts():
    # parser, opts, args = parseOpts()
    pass


# Generated at 2022-06-14 17:55:55.473204
# Unit test for function parseOpts
def test_parseOpts():
    # Simple test for parseOpts
    opts = parseOpts([])[1]
    assert opts.username is None
    assert opts.password is None
    assert opts.usenetrc is False
    assert opts.verbose is False
    assert opts.quiet is False
    assert opts.no_warnings is False
    assert opts.simulate is False
    assert opts.skip_download is False
    assert opts.format is None
    assert opts.listformats is False
    assert opts.outtmpl is None
    assert opts.ignoreerrors is False
    assert opts.forceurl is False
    assert opts.forcedownload is False
    assert opts.ratelimit is None
    assert opts.nooverwrites is False
    assert opts.retries is 10


# Generated at 2022-06-14 17:56:01.631707
# Unit test for function parseOpts
def test_parseOpts():
    if not hasattr(sys, 'frozen'):
        parser, opts, args = parseOpts(['-h'])
        assert not args
        parser, opts, args = parseOpts(
            ['-u', 'user', '-p', 'pass', '-f', '22/best', 'https://www.youtube.com/watch?v=BaW_jenozKc', '--get-url'])
        assert args == ['https://www.youtube.com/watch?v=BaW_jenozKc']
        assert opts.username == 'user'
        assert opts.password == 'pass'
        assert opts.format == '22/best'
        assert opts.usenetrc is False
        assert opts.geturl is True
        assert opts.forcetitle is True
       

# Generated at 2022-06-14 17:57:14.948622
# Unit test for function parseOpts
def test_parseOpts():
    for optstr in [['-o', 'abc'], ['-oabc']]:
        parser, opts, args = parseOpts(optstr)
        assert opts.outtmpl == 'abc'

        parser, opts, args = parseOpts(optstr, ['--outtmpl', 'def'])
        assert opts.outtmpl == 'def'

        parser, opts, args = parseOpts(optstr, overrideArguments=['--no-config-location'])
        assert opts.outtmpl == 'abc'

        parser, opts, args = parseOpts(optstr, ['--config-location', '/dev/null'])
        assert opts.outtmpl == 'def'


# Parse arguments
parser, opts, args = parseOpts()


# Generated at 2022-06-14 17:57:25.489145
# Unit test for function parseOpts
def test_parseOpts():
    # Test with -h and -v options
    parser, opts, args = parseOpts(['-h', '-v'])
    assert opts.verbose == 1
    assert args == []
    parser, opts, args = parseOpts(['-h', '-v', '-v'])
    assert opts.verbose == 2
    assert args == []

    # Test with --extract-audio option
    # Test with command line or config file arguments
    parser, opts, args = parseOpts(['--extract-audio'])
    assert opts.extractaudio == True
    parser, opts, args = parseOpts(['--extract-audio'], ['-x', 'True'])
    assert opts.extractaudio == True

    # Test with bool argument at command line
    parser, opt

# Generated at 2022-06-14 17:57:37.481152
# Unit test for function parseOpts
def test_parseOpts():
    sys.argv = ['youtube-dl', 'http://www.youtube.com/watch?v=BaW_jenozKc']
    ret = parseOpts()
    assert ret[0] == 'http://www.youtube.com/watch?v=BaW_jenozKc'
    assert ret[1] == []
    assert not ret[2].__dict__.get('ignoreerrors')
    assert not ret[2].__dict__.get('verbose')
    assert not ret[2].__dict__.get('forceurl')
    assert not ret[2].__dict__.get('forcetitle')

    sys.argv = ['youtube-dl', '-v', 'http://www.youtube.com/watch?v=BaW_jenozKc']
    ret = parseOpts()

# Generated at 2022-06-14 17:57:47.982328
# Unit test for function parseOpts
def test_parseOpts():
    from .extractor import gen_extractors, list_extractors

    all_extractors = list_extractors()
    ie = gen_extractors()

    # Merge options in IE and their tests
    ie_opts = {}
    ie_opts_tests = {}
    for ie in all_extractors:
        ie_opts.update(ie.options)
        if hasattr(ie, 'test'):
            ie_opts_tests.update(ie.test)

    parser, opts, args = parseOpts(['--verbose'])

    # Check if all options are present in the help and in _ALL_OPTIONS

# Generated at 2022-06-14 17:57:53.897843
# Unit test for function parseOpts
def test_parseOpts():
    import sys
    argv = sys.argv
    sys.argv = [
        'youtube-dl',
        '--proxy', '127.0.0.1:9',
        '--username', 'user',
        '--password', 'pass',
        '--video-password', 'videopassword',
        'https://www.youtube.com/watch?v=BaW_jenozKc']
    parser, opts, args = parseOpts()
    assert opts.proxy == '127.0.0.1:9'
    assert opts.username == 'user'
    assert opts.password == 'pass'
    assert opts.videopassword == 'videopassword'
    assert args == ['https://www.youtube.com/watch?v=BaW_jenozKc']