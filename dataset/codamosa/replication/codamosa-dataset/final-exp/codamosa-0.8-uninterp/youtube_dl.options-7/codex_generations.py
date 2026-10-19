

# Generated at 2022-06-14 17:48:41.258290
# Unit test for function parseOpts
def test_parseOpts():
    import sys
    if sys.version_info < (3,):
        defaultencoding = sys.getdefaultencoding()
        if defaultencoding == 'ascii':
            raise ValueError('Please set PYTHONIOENCODING=utf-8 for python2 to run tests')
    parser, opts, args = parseOpts()
    assert opts.usenetrc == True
    opts, args = parseOpts(['--username', 'test', '--password', 'hunter2'])
    assert opts.usenetrc == False
    opts, args = parseOpts(['--usenetrc', 'test.netrc'])
    assert opts.usenetrc == 'test.netrc'

# Generated at 2022-06-14 17:48:46.565819
# Unit test for function parseOpts
def test_parseOpts():
    # Basic test
    parser, opts, args = parseOpts(['--verbose'])
    assert opts.verbose

    # --ignore-config flag should override config file
    def test_ignore_config(opts):
        assert opts.usenetrc
        assert not opts.username
        assert not opts.password

    parser, opts, args = parseOpts(
        ['--username', 'test', '--password', 'test', '--ignore-config'])
    test_ignore_config(opts)


# Generated at 2022-06-14 17:49:00.172731
# Unit test for function parseOpts
def test_parseOpts():
    class DummyClass():
        def __init__(self):
            self.ydl_opts = None
            self.params = None
            self.urls = None
    ydl = DummyClass()
    ydl.params = []
    ydl.urls = []
    #self.assertTrue(isinstance(ydl.ydl_opts, optparse.Values))
    #self.assertEqual(len(ydl.params), 0)
    parseOpts(ydl)

#def print_exc(func):
#    def wrapped_func(*args, **kwargs):
#        try:
#            res = func(*args, **kwargs)
#        except Exception:
#            print(traceback.format_exc())
#        else:
#            return res
#    return wrapped_func


# Generated at 2022-06-14 17:49:13.476933
# Unit test for function parseOpts
def test_parseOpts():
    print(parseOpts(['--format=22']))
    print(parseOpts(['-f', '22']))
    print(parseOpts(['-f', '22', '-f', 'mp4']))
    print(parseOpts(['-f', 'hd720']))
    print(parseOpts(['-f', 'hd720', '-f', 'mp4']))
    print(parseOpts(['-f', 'mp4']))
    print(parseOpts(['-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio']))
    print(parseOpts(['-F']))

# Generated at 2022-06-14 17:49:18.317641
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(None)
    assert type(parser) is optparse.OptionParser
    assert type(opts) is optparse.Values
    assert type(args) is list


# Generated at 2022-06-14 17:49:21.692114
# Unit test for function parseOpts
def test_parseOpts():
    import doctest
    doctest.testmod(sys.modules[__name__])

# }}}


# Generated at 2022-06-14 17:49:30.226607
# Unit test for function parseOpts
def test_parseOpts():
    """
    Unit test for function parseOpts
    """
    if not sys.platform.startswith('win'):
        import warnings
        warnings.filterwarnings('ignore', 'Your platform is not supported')

    def check_parse(args, expected_opts):
        parser, opts, _ = parseOpts(args)
        sys.stderr.write('Checking ' + repr(args) + '\n')

        if expected_opts.get('verbose') is True and not opts.verbose:
            sys.stderr.write('Expected verbosity, but it\'s not there\n')
            return False

        for option_name, option in expected_opts.items():
            if option is None:
                continue

# Generated at 2022-06-14 17:49:34.973340
# Unit test for function parseOpts
def test_parseOpts():
    from youtube_dl.utils import orderedSet
    from sys import argv, executable
    orig_argv = argv[:]
    orig_executable = executable

# Generated at 2022-06-14 17:49:43.983748
# Unit test for function parseOpts
def test_parseOpts():
    try:
        import nose.tools
    except ImportError as err:
        print('Module nose is required for running unit tests.')
        print('Please install it with: sudo pip install nose')
        return

    parser, opts, args = parseOpts(overrideArguments = ['--version'])
    assert opts.version
    parser, opts, args = parseOpts(overrideArguments = ['--help'])
    assert opts.help
    parser, opts, args = parseOpts(overrideArguments = ['-U', 'youtube-dl test'])
    assert opts.user_agent == 'youtube-dl test'

    # General
    parser, opts, args = parseOpts(overrideArguments = ['--ignore-config'])
    assert opts.ignoreconfig

# Generated at 2022-06-14 17:49:49.365817
# Unit test for function parseOpts
def test_parseOpts():
    from youtube_dl.utils import parseOpts
    from .compat import compat_expanduser, compat_getenv, compat_parse_qs, compat_shlex_split, compat_urllib_error, compat_urllib_parse_urlparse
    # check if the given config options override the default ones
    # probably not the best way to test it, but its a start
    opts = ['-o', '/tmp/test', '--verbose', '-v', '--default-search=best', '--format=best']
    parser, opts, args = parseOpts(opts)
    assert opts.outtmpl == '/tmp/test'
    assert opts.verbose == 2
    assert opts.default_search == 'best'
    assert opts.format == ['best']
    assert opts.ignore_

# Generated at 2022-06-14 17:50:15.052693
# Unit test for function parseOpts
def test_parseOpts():
    ydl = YoutubeDL()
    ydl._real_initialize()
    expected = ['youtube-dl', '--format', 'best', '-o', '/path/to/%(title)s-%(id)s.%(ext)s', '--restrict-filenames', '--sleep-interval', '1', '--max-quality', 'FORMAT']
    ydl._opts.format = 'best'
    ydl._opts.outtmpl = '/path/to/%(title)s-%(id)s.%(ext)s'
    ydl._opts.restrictfilenames = True
    ydl._opts.sleep_interval = 1
    ydl._opts.format_limit = 'FORMAT'
    expected_opts = Namespace
    expected_opts.format

# Generated at 2022-06-14 17:50:22.676305
# Unit test for function parseOpts
def test_parseOpts():
    from youtube_dl.utils import DateRange
    parser, opts, args = common_opts({'--dateafter': '20000101',
                                      '--datebefore': '20000201'})
    assert opts.daterange == DateRange('20000101', '20000201')

    parser, opts, args = common_opts({'--dateafter': '20150101',
                                      '--datebefore': '20150101'})
    assert opts.daterange is None



# Generated at 2022-06-14 17:50:36.053442
# Unit test for function parseOpts
def test_parseOpts():
    from youtube_dl.compat import stdoutencoding
    from io import BytesIO

    def parse(args):
        parser, opts, args = parseOpts(args)
        out = BytesIO()
        parser.print_help(out)
        return opts, out.getvalue().decode(stdoutencoding())

    opts, usage = parse([])
    assert opts.verbose == False
    assert opts.quiet == False
    assert opts.format == None
    assert opts.listformats == False
    assert opts.usenetrc == False
    assert opts.noprogress == True
    assert opts.nocheckcertificate == False
    assert opts.prefer_insecure == False
    assert opts.proxy == None
    assert opts.socket_timeout == None

# Generated at 2022-06-14 17:50:38.117086
# Unit test for function parseOpts
def test_parseOpts():
    pass


# Generated at 2022-06-14 17:50:39.630678
# Unit test for function parseOpts
def test_parseOpts():
    # TODO: Implement this if necessary
    pass


# Generated at 2022-06-14 17:50:50.952076
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, _ = parseOpts(['-u', 'user', '-p', 'passwd', '--',
        'http://www.youtube.com/watch?v=BaW_jenozKc'])
    assert opts.username == 'user'
    assert opts.password == 'passwd'
    parser, opts, _ = parseOpts(['--username', 'user', '--password', 'passwd', '--',
        'http://www.youtube.com/watch?v=BaW_jenozKc'])
    assert opts.username == 'user'
    assert opts.password == 'passwd'

    parser, opts, _ = parseOpts(['--verbose', 'http://www.youtube.com/watch?v=BaW_jenozKc'])
    assert opt

# Generated at 2022-06-14 17:50:57.796671
# Unit test for function parseOpts
def test_parseOpts():
    """This is a test unit for parseOpts function.
    """
    p, o, a = parseOpts()
    if a[1]== 'https://www.youtube.com/watch?v=BaW_jenozKc':
        print('[debug] Unit test for parseOpts function passed.')
    else:
        print('[debug] Unit test for parseOpts function failed.')



# Generated at 2022-06-14 17:51:04.193546
# Unit test for function parseOpts
def test_parseOpts():
        args = ['-i', '--format', 'best', '--no-playlist', 'test']
        (parser, opts, args) = parseOpts(args)
        assert opts.usenetrc == True
        assert opts.format == 'best'
        assert opts.noplaylist == True



# Generated at 2022-06-14 17:51:15.581439
# Unit test for function parseOpts
def test_parseOpts():
    from io import StringIO
    parser = optparse.OptionParser()
    opts, args = parseOpts(parser, ['--username=user', '--password=pass'])
    assert opts.username == 'user'
    assert opts.password == 'pass'
    parser = optparse.OptionParser()
    hide_login_info_fp = StringIO()
    parser, opts, args = parseOpts(
        parser, ['--username', 'user', '--password', 'pass'],
        hide_login_info_func=lambda s: hide_login_info_fp.write(s))
    assert opts.username == 'user'
    assert opts.password == 'pass'
    assert hide_login_info_fp.getvalue() == '[password]\n'



# Generated at 2022-06-14 17:51:27.263395
# Unit test for function parseOpts
def test_parseOpts():
    # Testing parseOpts requires a monkeypatch for getpass.getpass()
    # to avoid user input
    getpass_getpass_save = compat_getpass.getpass
    def getpass_getpass(*args, **kargs):
        return u"qu\xe2"
    compat_getpass.getpass = getpass_getpass

    def read_options(location):
        if location == 'youtube-dl.conf':
            return [
                '--username', 'user',
                '--password', 'pass',
                '--twofactor', '2fac',
                '-x',
                '--verbose']
        else:
            return []

    def read_user_conf():
        return []

    def test(*args):
        _readOptions = read_options
        _readUserConf = read_user_conf


# Generated at 2022-06-14 17:51:48.566122
# Unit test for function parseOpts
def test_parseOpts():
    try:
        parser, opts, args = parseOpts(['-U', 'UNITTEST'])
    except SystemExit:
        pass # The output of parseOpts is tested below
    assert(hasattr(opts, 'username'))
    assert(opts.username == 'UNITTEST')
    assert(hasattr(opts, 'noplaylist'))
    assert(opts.noplaylist)


# Generated at 2022-06-14 17:51:55.108744
# Unit test for function parseOpts
def test_parseOpts():
    opts = parseOpts(['-F', '-i', '--no-playlist'])[1]
    assert opts.usenetrc is False
    assert opts.password is None
    assert opts.format is None
    assert opts.listformats is True
    assert opts.noplaylist is True
    write_string('parseOpts: OK\n')



# Generated at 2022-06-14 17:52:07.971187
# Unit test for function parseOpts
def test_parseOpts():
    def test_conf(conf, expected):
        _, opts, _ = parseOpts(overrideArguments=conf)
        assert opts.verbose == expected

    test_conf(['--verbose'], True)
    test_conf(['--verbose', '--no-verbose'], False)
    test_conf(['--no-verbose'], False)

    test_conf(['--ignore-config', '--verbose'], True)
    test_conf(['--ignore-config', '--verbose', '--no-verbose'], False)
    test_conf(['--ignore-config', '--no-verbose'], False)
    test_conf([], False)

    test_conf(['--config-location=/dev/null', '--verbose'], True)

# Generated at 2022-06-14 17:52:19.395368
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts([
        '-i', '--no-warnings', '--no-check-certificate',
        '--max-filesize', '20M',
        '--output', '%(uploader)s/%(title)s-%(id)s-%(format_id)s.%(ext)s',
        'https://www.youtube.com/watch?v=BaW_jenozKc'])
    assert args == [u'https://www.youtube.com/watch?v=BaW_jenozKc']
    assert opts.ignoreerrors
    assert not opts.no_warnings
    assert opts.no_check_certificate
    assert opts.max_filesize == 20

# Generated at 2022-06-14 17:52:31.074402
# Unit test for function parseOpts
def test_parseOpts():
    from compat import parse_qs, parse_qsl, compat_getenv, compat_shlex_split
    from ssl import _create_unverified_context

    if compat_getenv('TRAVIS_EVENT_TYPE') == 'cron':
        raise unittest.SkipTest('Skip this test on Cron job')


# Generated at 2022-06-14 17:52:43.398405
# Unit test for function parseOpts
def test_parseOpts():
    os.environ['YOUTUBE_DL_SYSARG'] = '--hls-prefer-ffmpeg --user=test --password=test -i -v --no-warnings'
    opts, args = parseOpts()
    assert opts.hls_prefer_ffmpeg
    assert opts.username == 'test'
    assert opts.password == 'test'
    assert opts.ignoreerrors
    assert opts.verbose
    assert opts.no_warnings
    os.environ.pop('YOUTUBE_DL_SYSARG')
    opts, args = parseOpts([])
    assert opts.verbose == 0
    opts, args = parseOpts(['-v'])
    assert opts.verbose == 1
    opts, args = parseOpts

# Generated at 2022-06-14 17:52:46.460146
# Unit test for function parseOpts
def test_parseOpts():
    assert parseOpts(['-F', 'http://www.youtube.com/watch?v=BaW_jenozKc'])


# Generated at 2022-06-14 17:52:59.531289
# Unit test for function parseOpts
def test_parseOpts():
    assert 'http://example.com' in parseOpts(['--get-url', 'http://example.com'])[2]
    assert '--get-title' in parseOpts(['-e', '--get-title'])[1]
    assert '--get-id' in parseOpts(['--extract-audio', '--get-id'])[1]
    assert '--quiet' in parseOpts(['--newline', '--quiet'])[1]
    assert '--playlist-reverse' in parseOpts(['--sleep-interval', '60', '--playlist-reverse'])[1]
    assert '--no-mark-watched' in parseOpts(['--match-filter', 'regex', '--no-mark-watched'])[1]

# Generated at 2022-06-14 17:53:13.150097
# Unit test for function parseOpts
def test_parseOpts():
    # Downloaded files will be put in the user's home dir
    save_cwd = os.getcwd()
    os.chdir(os.path.expanduser('~'))

    # Make sure list formats are parsed correctly
    sys.argv = ['youtube-dl', '-F', 'https://www.youtube.com/watch?v=BaW_jenozKc']
    parser, opts, _ = parseOpts()
    assert opts.format == []

    # Make sure -f 17 works
    sys.argv = ['youtube-dl', '-f', '17', 'https://www.youtube.com/watch?v=BaW_jenozKc']
    parser, opts, _ = parseOpts()
    assert opts.format == ['17']

    # Make sure -f 17/44/35

# Generated at 2022-06-14 17:53:25.154470
# Unit test for function parseOpts
def test_parseOpts():
    class MockOpener(object):
        def open(self, *args, **kwargs):
            assert False, 'Should not open URL'
    # Test argv-based reading of config file
    parser, opts, args = parseOpts(['-U', '--config-location', 'test/test.conf', 'rg3/youtube-dl'])
    assert opts.usenetrc
    assert opts.username is None
    assert opts.password is None
    assert len(opts.extractaudio) == 2
    assert opts.quiet
    assert opts.simulate
    assert opts.ratelimit == '100k'
    assert opts.nooverwrites
    assert opts.playliststart == 1
    assert opts.playlistend == 3
    assert opts.playlistreverse

# Generated at 2022-06-14 17:54:07.649831
# Unit test for function parseOpts
def test_parseOpts():
    import re
    parser, opts, args = parseOpts([])

    assert opts.usenetrc is False
    assert opts.username is None
    assert opts.password is None

    assert opts.quiet is False
    assert opts.no_warnings is False
    assert opts.simulate is False
    assert opts.skip_download is False
    assert opts.format == []
    assert opts.listformats == False
    assert opts.outtmpl is None
    assert opts.autonumber_size is None
    assert opts.autonumber_start is 1
    assert opts.restrictfilenames is False
    assert opts.list_thumbnails is False
    assert opts.match_filter is None

    assert opts.ratelimit is None
    assert opts.noo

# Generated at 2022-06-14 17:54:17.353307
# Unit test for function parseOpts
def test_parseOpts():
    def parseOpts_test(cmdlineParams, expectedParams):
        parser, opts, args = parseOpts(cmdlineParams)
        params = vars(opts)
        for key, value in params.items():
            if key in expectedParams:
                assert params[key] == expectedParams[key], (key, params[key], expectedParams[key])
            else:
                assert params[key] is False, (key, params[key], expectedParams)
        assert args == [], args


# Generated at 2022-06-14 17:54:25.781922
# Unit test for function parseOpts
def test_parseOpts():
    try:
        parser, opts, args = parseOpts(['-v', '--extract-audio', '--audio-format', 'best', 'https://youtu.be/BaW_jenozKc'])
        assert opts.verbose == True
        assert opts.extractaudio == True
        assert opts.audioformat == 'best'
    except:
        pass


# Generated at 2022-06-14 17:54:27.126000
# Unit test for function parseOpts
def test_parseOpts():
    opts, args = parseOpts()
# End Unit test


# Generated at 2022-06-14 17:54:37.197316
# Unit test for function parseOpts
def test_parseOpts():
    if sys.version_info[0] == 3:
        from io import StringIO
        sys.stdout = StringIO()
        sys.stderr = StringIO()
        dummy_streams = [sys.stderr]
    else:
        from cStringIO import StringIO
        sys.stdout = sys.stderr = StringIO()
        dummy_streams = [sys.stdout, sys.stderr]
    # First test with no arguments at all
    parseOpts()
    for dummy_stream in dummy_streams:
        dummy_stream.seek(0)
        assert dummy_stream.read() == ''


# Generated at 2022-06-14 17:54:50.949780
# Unit test for function parseOpts
def test_parseOpts():
    from urllib import unquote
    from youtube_dl.utils import encodeArgument
    from youtube_dl.postprocessor.common import PostProcessor
    from sys import argv
    from shutil import rmtree
    from tempfile import mkdtemp

    class FakePostProcessor(PostProcessor):
        def run(self, info):
            return [], info


# Generated at 2022-06-14 17:54:52.163658
# Unit test for function parseOpts
def test_parseOpts():
    assert parseOpts(['-h'])[1] is None

# Generated at 2022-06-14 17:55:01.660838
# Unit test for function parseOpts
def test_parseOpts():
    # Test 1
    '''
    >>> orig = sys.argv
    >>> sys.argv = [orig[0], '-v']
    >>> parseOpts()
    Usage: youtube-dl [OPTIONS] URL [URL...]
    youtube-dl: error: You must provide at least one URL.
    Type youtube-dl --help to see a list of all options.
    >>> sys.argv = orig
    '''

    # Test 2

# Generated at 2022-06-14 17:55:06.405406
# Unit test for function parseOpts
def test_parseOpts():
    # check if the function is able to parse default arguments
    if __name__ == "__main__":
        parser, opts, unused_args = parseOpts()
        assert opts.limit_rate == '0'
# test parseOpts
test_parseOpts()


# Generated at 2022-06-14 17:55:15.273346
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-v', '--username', 'user', '--password', 'pass', '--ap-mso', 'dummy', '--ap-username', 'dummy', '--ap-password', 'dummy', 'http://example.com'])
    assert opts.verbose > 0
    # Login info is not echoed back
    assert opts.verbose_string == 'verbose=True'
    assert opts.username == 'user'
    assert opts.password == 'pass'
    assert opts.ap_mso == 'dummy'
    assert opts.ap_username == 'dummy'
    assert opts.ap_password == 'dummy'
    assert args == ['http://example.com']

test_parseOpts()



# Generated at 2022-06-14 17:55:44.738013
# Unit test for function parseOpts
def test_parseOpts():
    from types import ModuleType
    fake_module = ModuleType('__main__')
    fake_module.__file__ = '__main__'
    with patch('sys.modules', {'__main__': fake_module}):
        parser, _, _ = parseOpts()
    assert isinstance(parser, optparse.OptionParser)



# Generated at 2022-06-14 17:55:52.423966
# Unit test for function parseOpts
def test_parseOpts():
    def assert_args(script, expected):
        parser, opts, args = parseOpts(['--ignore-config', '--no-warnings', script])
        assert opts.ignore_config
        assert opts.no_warnings
        assert args == [script]
        assert expected == _get_configuration()

# Generated at 2022-06-14 17:56:05.183631
# Unit test for function parseOpts
def test_parseOpts():
    opts_parser, opts, args = parseOpts(['-u', 'user', '-p', 'passwd', 'url1', 'url2'])
    assert opts.username == 'user'
    assert opts.password == 'passwd'
    assert args == ['url1', 'url2']

    opts_parser, opts, args = parseOpts(['-u', 'user', '-p', 'passwd', '--min-filesize', '1MiB', 'url1', 'url2'])
    assert opts.username == 'user'
    assert opts.password == 'passwd'
    assert opts.min_filesize == '1MiB'
    assert args == ['url1', 'url2']

# #########################
# #                      # #
# #      Information     # #

# Generated at 2022-06-14 17:56:16.793489
# Unit test for function parseOpts
def test_parseOpts():
    opts_to_args = {
        '-s': ['--simulate'],
        '--format': ['bestvideo+bestaudio', 'best'],
        '--get-thumbnail': [],
        '-g': ['--get-title'],
        '--get-id': [],
        '--get-description': [],
        '--get-duration': [],
        '--get-filename': [],
        '--get-format': [],
        '--get-annotations': [],
        '--output': ['%(id)s.%(ext)s'],
    }
    opts_parsed = parseOpts(opts_to_args)
    assert opts_parsed.simulate
    assert opts_parsed.format == ['bestvideo+bestaudio','best']

# Generated at 2022-06-14 17:56:28.049462
# Unit test for function parseOpts
def test_parseOpts():
    from io import StringIO
    from youtube_dl.version import __version__

    parser, opts, args = parseOpts([])
    assert type(parser) is optparse.OptionParser
    assert type(opts) is optparse.Values
    assert type(args) is list
    assert args == []

    with captured_output() as (_, err):
        parser, opts, args = parseOpts(['--version'])
    assert 'youtube-dl version ' + __version__ in err.getvalue()
    assert type(parser) is optparse.OptionParser
    assert type(opts) is optparse.Values
    assert type(args) is list
    assert args == ['--version']

    with captured_output() as (out, _):
        parser, opts, args = parseOpts(['-h'])
   

# Generated at 2022-06-14 17:56:35.366381
# Unit test for function parseOpts
def test_parseOpts():
    try:
        import nose
    except ImportError:
        print('To run unit tests, you must install nose:  http://somethingaboutorange.com/mrl/projects/nose')
    else:
        nose.core.runmodule(argv=['-s', '--with-doctest'], exit=False)

# -- Playlist selection ---------------------------------------------------------------------------------
# Extracts a playlist id from a variety of YouTube URLs.

# Generated at 2022-06-14 17:56:46.758429
# Unit test for function parseOpts

# Generated at 2022-06-14 17:56:48.850764
# Unit test for function parseOpts
def test_parseOpts():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    test_parseOpts()

# Generated at 2022-06-14 17:56:51.939338
# Unit test for function parseOpts
def test_parseOpts():
    global write_string
    write_string = _create_write_string()
    _parseOpts([])
    _parseOpts(['-v'])
    _parseOpts(['--verbose'])
    _parseOpts(['--dump-user-agent'])



# Generated at 2022-06-14 17:57:03.733717
# Unit test for function parseOpts
def test_parseOpts():
    # Just ignore any command-line arguments
    sys.argv = sys.argv[:1]

    parser, opts, args = parseOpts()

    if opts.username is not None:
        sys.exit('youtube-dl username is "%s"' % opts.username)

    if opts.password is not None:
        sys.exit('youtube-dl password is "%s"' % opts.password)

    if opts.twofactor is not None:
        sys.exit('youtube-dl twofactor is "%s"' % opts.twofactor)

    if opts.videopassword is not None:
        sys.exit('youtube-dl videopassword is "%s"' % opts.videopassword)

# vim: expandtab:sw=4:ts=4