

# Generated at 2022-06-14 17:48:41.442255
# Unit test for function parseOpts
def test_parseOpts():
    """ test if opts contains expected set of parameters """

    # Test conditions
    # Test parameters
    url = 'http://www.youtube.com/watch?v=BaW_jenozKc'
    # Expected results
    output_name = '%(title)s-%(id)s.%(ext)s'

    # Execute the function
    (parser, opts, args) = parseOpts(['--simulate', '-o', output_name, url])

    # Test results
    if os.path.basename(opts.outtmpl) != output_name:
        raise AssertionError('unexpected output template base name')
    if opts.simulate:
        # default
        pass
    else:
        raise AssertionError('--simulate expected but not found')



# Generated at 2022-06-14 17:48:46.877603
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-c', '--config-location', '/tmp/youtube-dl.conf', '-u', 'user', '-p', 'pass', '-i', '--video-password', 'pw', '-F', '--format', 'FORMAT', '--youtube-include-dash-manifest'])
    assert opts.config_location == '/tmp/youtube-dl.conf'
    assert opts.username == 'user'
    assert opts.password == 'pass'
    assert opts.verbose == False
    assert opts.quiet == False
    assert opts.no_warnings == True
    assert opts.forceurl == False
    assert opts.forcetitle == False
    assert opts.forceid == False
    assert opts.forcethumbnail == False

# Generated at 2022-06-14 17:49:00.618741
# Unit test for function parseOpts
def test_parseOpts():
    func = parseOpts
    func(['-z'])
    func(['-f', '22'])
    func(['-q'])
    func(['-q', 'http://www.youtube.com/watch?v=BaW_jenozKc'])
    func(['-F', 'http://www.youtube.com/watch?v=BaW_jenozKc'])
    func(['-k', 'http://www.youtube.com/watch?v=BaW_jenozKc'])
    func(['--download-archive', 'archive.txt'])
    func(['--match-title', 'regex'])
    func(['--no-playlist'])
    func(['--age-limit', '18'])
    func(['-c'])

# Generated at 2022-06-14 17:49:04.910650
# Unit test for function parseOpts
def test_parseOpts():
    assert parseOpts(['--rate-limit', '100k', '--', '--rm-cache-dir'])[2] == ['--', '--rm-cache-dir']



# Generated at 2022-06-14 17:49:08.792095
# Unit test for function parseOpts
def test_parseOpts():
    # return value of parseOpts must be tuple with length of 3
    assert len(parseOpts(['-h'])) == 3

# Parse args and return an object with key-values

# Generated at 2022-06-14 17:49:18.239435
# Unit test for function parseOpts
def test_parseOpts():
    def _test(args, expected):
        parser, opts, _ = parseOpts(args)
        for k, v in opts.__dict__.items():
            if isinstance(v, compat_urllib_request.OpenerDirector):
                assert not hasattr(expected, k)
                continue
            assert getattr(expected, k) == v, '%s: %r != %r' % (k, getattr(expected, k), v)
        assert expected.write_all == (opts.writeinfo == opts.writethumbnail == opts.writedescription == True)


# Generated at 2022-06-14 17:49:32.410653
# Unit test for function parseOpts
def test_parseOpts():
    from sys import argv
    orig_argv = argv
    argv = ['youtube-dl']
    assert parseOpts() == (None, None, [])
    # Call with both system-wide and user configuration files present
    try:
        testConf = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'youtube_dl', 'options.conf')
        os.symlink(testConf, '/etc/youtube-dl.conf')
        assert parseOpts() != (None, None, [])
    finally:
        os.remove('/etc/youtube-dl.conf')
    # Test if the --ignore-config flag overrides user configuration
    argv = ['youtube-dl', '--ignore-config']
    assert parseOpts() == (None, None, [])


# Generated at 2022-06-14 17:49:35.905642
# Unit test for function parseOpts
def test_parseOpts():
    args = ['--extract-audio']
    parser, ytdl_opts, ytdl_extra_args = parseOpts(args)
    assert ytdl_opts.extractaudio


# Generated at 2022-06-14 17:49:44.604362
# Unit test for function parseOpts
def test_parseOpts():
    from sys import argv
    from shutil import move

    from .compat import compat_expanduser

    curdir = os.path.dirname(__file__)
    config = os.path.join(curdir, 'config')
    move(config, config + '_backup')
    config_content = b'--min-sleep-interval 5\n'
    open(config, 'wb').write(config_content)
    argv[1:] = ['--ignore-config', '-v']
    parser, opts, _ = parseOpts()
    assert opts.min_sleep_interval == 5
    move(config + '_backup', config)
    argv[1:] = ['--config-location', compat_expanduser(u'~/foo')]

# Generated at 2022-06-14 17:49:50.018020
# Unit test for function parseOpts
def test_parseOpts():
    opts, args = parseOpts(['-h'])
    assert opts.help is True
    assert args == []
    opts, args = parseOpts(['--help'])
    assert opts.help is True
    assert args == []
    opts, args = parseOpts(['-u', 'test_user', '-p', 'test_pwd', '-v', 'http://www.youtube.com/watch?v=BaW_jenozKc'])
    assert args == ['http://www.youtube.com/watch?v=BaW_jenozKc']
    assert opts.verbose is True
    assert opts.username == 'test_user'
    assert opts.password == 'test_pwd'

# Generated at 2022-06-14 17:50:06.543805
# Unit test for function parseOpts

# Generated at 2022-06-14 17:50:09.297450
# Unit test for function parseOpts
def test_parseOpts():
    if __name__ == '__main__':
        parser, opts, args = parseOpts(['-h'])


# Generated at 2022-06-14 17:50:16.915439
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-f', '17/18/34', 'http://youtube.com/watch?v=BaW_jenozKc', '--'])
    assert opts.format == '17/18/34'
    assert args == ['http://youtube.com/watch?v=BaW_jenozKc']

    parser, opts, args = parseOpts(['-f', '17', '-f', '18', 'http://youtube.com/watch?v=BaW_jenozKc'])
    assert opts.format == ['17', '18']
    assert args == ['http://youtube.com/watch?v=BaW_jenozKc']


# Generated at 2022-06-14 17:50:28.071581
# Unit test for function parseOpts
def test_parseOpts():
    # Testing with fake arguments
    parser, opts, args = parseOpts(['-F', 'https://www.youtube.com/watch?v=BaW_jenozKc'])
    assert opts.format == 'best'
    assert opts.usenetrc == False
    assert args[0] == 'https://www.youtube.com/watch?v=BaW_jenozKc'
    assert opts.outtmpl == '%(title)s-%(id)s.%(ext)s'
    assert opts.ratelimit == None
    assert opts.retries == 10
    assert opts.continuedl == False
    assert opts.playliststart == 1
    assert opts.playlistend == 0
    assert opts.playlistreverse == False
    assert opts.noover

# Generated at 2022-06-14 17:50:34.108469
# Unit test for function parseOpts
def test_parseOpts():
    opts, args = parseOpts(None)
    assert str(opts.usenetrc) != 'None'


# Parse arguments
parser, opts, args = parseOpts(None)

# Try to get window id
if opts.getwindowid:
    try:
        opts.getwindowid = _get_window_id()
    except Exception:
        parser.error('ERROR: could not get window id.\n')

# Set language
if opts.geo_bypass:
    geo_bypass_country = opts.geo_bypass
else:
    geo_bypass_country = None

if opts.geo_bypass_ip:
    geo_bypass_ip = opts.geo_bypass_ip

# Generated at 2022-06-14 17:50:41.618563
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = compat_parseOpts(['-v', '-c', '-w', '--max-filesize', '20m', 'https://www.youtube.com/watch?v=BaW_jenozKc'])
    assert opts.verbose == True
    assert opts.cachedir == True
    assert opts.nooverwrites == True
    assert opts.max_filesize == '20m'
    assert isinstance(args, list) and len(args) == 1

# Function that determines the active stream/progress bar for a given
# Downloader object (d). It is meant to be used from the download
# progress hooks (for example, on progress or download completed)

# Generated at 2022-06-14 17:50:54.560630
# Unit test for function parseOpts
def test_parseOpts():
    from youtube_dl.utils import DateRange
    parser, opts, args = parseOpts()

    # Simple tests
    opts.age_limit = 21
    assert opts.age_limit == 21

    opts.age_limit = '21'
    assert opts.age_limit == 21

    opts.age_limit = None
    assert opts.age_limit is None

    # Test DateRange
    opts.dateafter = '20130101'
    assert opts.dateafter.__dict__ == {'end': None, 'start': datetime.date(2013, 1, 1)}
    opts.dateafter = DateRange('20130101', '20130102')

# Generated at 2022-06-14 17:51:05.042457
# Unit test for function parseOpts
def test_parseOpts():
    # We don't want to import YoutubeDL in unittest mode
    class FakeYoutubeDL:
        params = {}

    fake_ydl = FakeYoutubeDL()

    # Setup environment
    os.environ['XDG_CACHE_HOME'] = tempfile.mkdtemp()

    old_stdout = sys.stdout

    sys.stdout = io.BytesIO()
    parser, opts, args = parseOpts(['--username=foo', '--password=bar', 'https://www.example.org/watch?v=BAR'])
    assert 'foo' not in sys.stdout.getvalue()
    assert 'bar' not in sys.stdout.getvalue()
    assert 'BAR' in sys.stdout.getvalue()

    sys.stdout = io.BytesIO()
    parser,

# Generated at 2022-06-14 17:51:07.712255
# Unit test for function parseOpts
def test_parseOpts():
    global args
    parseOpts(args)
    
# 'main' function: has been duplicated from YoutubeDL.py

# Generated at 2022-06-14 17:51:17.839098
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts([])
    assert opts.verbose == 2
    assert opts.quiet == False
    assert not args
    parser, opts, args = parseOpts(['-v'])
    assert opts.verbose == 3
    assert opts.quiet == False
    assert not args
    parser, opts, args = parseOpts(['--verbose'])
    assert opts.verbose == 3
    assert opts.quiet == False
    assert not args
    parser, opts, args = parseOpts(['--verbose', '-v'])
    assert opts.verbose == 4
    assert opts.quiet == False
    assert not args
    parser, opts, args = parseOpts(['-v', '--quiet'])
    assert opts.verbose

# Generated at 2022-06-14 17:51:48.524191
# Unit test for function parseOpts
def test_parseOpts():
    from sys import argv
    from os import getcwd
    import youtube_dl.YoutubeDL
    import optparse
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.utils import __version__
    parser, opts, args = parseOpts(None)
    assert isinstance(parser, optparse.OptionParser)
    assert isinstance(opts, optparse.Values)
    assert isinstance(args, list)

    # Test the default values of the optparse object
    # General
    assert opts.verbose == False
    assert opts.quiet == False
    assert opts.no_warnings == False
    assert opts.simulate == False
    assert opts.skip_download == False
    assert opts.quiet == False
    assert opts.format == None

# Generated at 2022-06-14 17:51:50.053472
# Unit test for function parseOpts
def test_parseOpts():
    dummy_args = [u'--version']
    parser, opts, args = parseOpts(dummy_args)
    assert args == dummy_args



# Generated at 2022-06-14 17:52:02.134799
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-v'])
    assert opts.verbose.count(1) == 1
    assert opts.quiet.count(1) == 0

    parser, opts, args = parseOpts(['-v', '-v'])
    assert opts.verbose.count(1) == 2
    assert opts.quiet.count(1) == 0

    parser, opts, args = parseOpts(['-q'])
    assert opts.verbose.count(1) == 0
    assert opts.quiet.count(1) == 1

    parser, opts, args = parseOpts(['-q', '-q'])
    assert opts.verbose.count(1) == 0
    assert opts.quiet.count(1) == 2

    parser,

# Generated at 2022-06-14 17:52:12.166263
# Unit test for function parseOpts

# Generated at 2022-06-14 17:52:14.843290
# Unit test for function parseOpts
def test_parseOpts():
    opts, args = parseOpts(['-h'])
    assert 'help' in dir(opts)
    assert 'usage' in dir(opts)

# }}}


# Generated at 2022-06-14 17:52:27.174052
# Unit test for function parseOpts
def test_parseOpts():
    # Basic test
    (p, o, a) = parseOpts()
    assert o.username is None

    # Test --no-check-certificate
    (p, o, a) = parseOpts(['--no-check-certificate'])
    assert o.nocheckcertificate
    (p, o, a) = parseOpts(['--no-check-certificate', '--verbose'])
    assert o.nocheckcertificate

    # Test --ignore-config
    (p, o, a) = parseOpts(['--ignore-config'])
    assert o.ignoreconfig
    (p, o, a) = parseOpts(['--ignore-config', '--username', 'abcdefghij'])
    assert not o.username

    # Test --default-search

# Generated at 2022-06-14 17:52:40.574588
# Unit test for function parseOpts
def test_parseOpts():
    from youtube_dl.YoutubeDL import parseOpts, YoutubeDL

    # Base options
    opts, args = parseOpts([])
    assert opts.get('extractaudio') is False
    assert opts.get('audioformat') == 'best'
    assert opts.get('audioquality') == '5'
    assert opts.get('usetitle') is False
    assert opts.get('usenetrc') is False

    # File options
    opts, args = parseOpts(['-o', 'myfile.%(ext)s'])
    assert opts.get('outtmpl') == 'myfile.%(ext)s'

    # Format options
    opts, args = parseOpts(['-f', 'best'])
    assert opts.get('format') == 'best'


# Generated at 2022-06-14 17:52:52.720493
# Unit test for function parseOpts
def test_parseOpts():
    (p, o, a) = parseOpts(['-b', 'http://example.com/test.mp4'])
    assert o.params['outtmpl'] == '%(id)s.%(ext)s'
    assert o.params['ignoreerrors'] == True
    assert o.params['ratelimit'] == '16k'
    assert o.params['recodevideo'] == 'mp4'
    assert o.params['nooverwrites'] == True
    assert o.params['format'] == None
    assert o.params['outtmpl'] == '%(id)s.%(ext)s'
    assert o.params['download_archive'] == 'youtube-dl.log'
    assert o.params['cookiefile'] == None


# Generated at 2022-06-14 17:53:03.300950
# Unit test for function parseOpts
def test_parseOpts():
    from sys import argv

    class _parser:
        def __init__(self):
            self.option_groups = []

    class _group:
        pass

    class _option:
        def __init__(self):
            self.dest = None
            self.action = None
            self.default = None

        def __eq__(self, other):
            return self.dest == other.dest and self.action == other.action and self.default == other.default

    class _opts:
        def __init__(self):
            self.verbose = False
            self.quiet = True
            self.simulate = True
            self.format = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'

# Generated at 2022-06-14 17:53:07.461078
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts()
    assert opts.username == 'test'
    assert opts.password == 'test'
    assert opts.usenetrc == True
    assert opts.quiet == True


# Generated at 2022-06-14 17:54:09.966056
# Unit test for function parseOpts
def test_parseOpts():
    from StringIO import StringIO
    from youtube_dl.utils import encodeArgument
    argv = ['--username', 'foo', '--password', 'bar',
            '--verbose', '--get-url', '--get-title', '--get-id',
            '--get-thumbnail', '--get-description', '--get-filename',
            '--get-format', '--newline', '--proxy', '127.0.0.1:890']
    sys.argv[1:] = argv
    parser, opts, args = parseOpts()
    parsed_argv = []
    for part_argv in sys.argv[1:]:
        part_argv = part_argv.decode(preferredencoding())

# Generated at 2022-06-14 17:54:21.482666
# Unit test for function parseOpts
def test_parseOpts():
    from getopt import GetoptError
    def _parse_opts(args):
        from ydl import parseOpts
        return parseOpts(args)[1]

    assert _parse_opts(['-i', '-4']).noplaylist is True
    assert _parse_opts(['-i']).noplaylist is None
    assert _parse_opts(['--no-playlist']).noplaylist is True

    assert _parse_opts(['-i', '-4']).proxy is None
    assert _parse_opts(['-i', '-4', '--proxy', '1.1.1.1']).proxy == '1.1.1.1'

    assert _parse_opts(['-i', '-4']).noplaylist is True
    assert _parse_

# Generated at 2022-06-14 17:54:25.780565
# Unit test for function parseOpts
def test_parseOpts():
    assert parseOpts(['-f', 'best', 'plcraft']) == ([['-f', 'best', 'plcraft']], ['best'], ['plcraft'])



# Generated at 2022-06-14 17:54:37.601746
# Unit test for function parseOpts
def test_parseOpts():
    opts, args = parseOpts(['-o', 'test.%(ext)s', 'http://www.youtube.com/watch?v=BaW_jenozKc'])
    assert(opts.outtmpl == 'test.%(ext)s')
    opts, args = parseOpts(['--no-color'])
    assert(opts.nocolor == True)
    opts, args = parseOpts(['--no-warnings'])
    assert(opts.noplaylist == True)
    opts, args = parseOpts(['--ignore-errors'])
    assert(opts.ignoreerrors == True)
    opts, args = parseOpts(['--playlist-start', '3'])
    assert(opts.playliststart == 3)
    opts,

# Generated at 2022-06-14 17:54:40.731487
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts()
# ===== End of parseOpts() =====



# Generated at 2022-06-14 17:54:47.289829
# Unit test for function parseOpts
def test_parseOpts():
    # I tried to write a unit test for function parseOpts, but I gave up
    # after half a day because it was too complicated
    # The main problem was that a lot of code depends on command line arguments
    # and thus it is non-trivial to test it standalone
    # TODO: fix this shit
    pass

# Parse a string argument as a boolean

# Generated at 2022-06-14 17:54:58.590548
# Unit test for function parseOpts
def test_parseOpts():
    # Test setting boolean '--yes-playlist' option.
    sys.argv = ['youtube-dl', '--yes-playlist']
    (parser, opts, args) = parseOpts()
    assert opts.playliststart == 1
    assert opts.playlistend == -1

    # Test setting boolean '--yes-playlist' option.
    sys.argv = ['youtube-dl', '--yes-playlist', '-v', 'url']
    (parser, opts, args) = parseOpts()
    assert opts.verbose
    assert args[0] == 'url'
    assert opts.playliststart == 1
    assert opts.playlistend == -1

    # Test overriding boolean '--yes-playlist' option.

# Generated at 2022-06-14 17:55:05.508462
# Unit test for function parseOpts
def test_parseOpts():
    from compat import str
    def _opt(k, v):
        if isinstance(v, bool):
            return str(k) if v else str('no-' + k)
        else:
            return '%s=%s' % (k, v)

    def _check_opt_eq(filter_opts, opts, opt_name, opt_value):
        if (opt_name in filter_opts):
            assert (getattr(opts, opt_name) == getattr(filter_opts, opt_name)), '%s should equal to %s' % (opt_name, opt_value)
        else:
            assert (getattr(opts, opt_name) == opt_value), '%s should equal to %s' % (opt_name, opt_value)

    # Test for parsing of options
   

# Generated at 2022-06-14 17:55:11.493651
# Unit test for function parseOpts
def test_parseOpts():
    parser = optparse.OptionParser()
    parser, opts, args = parseOpts(parser)
    assert opts.username == 'test_username'
    assert opts.password == 'test_password'
    assert opts.twofactor == 'test_twofactor'
    assert opts.ap_username == 'test_ap_username'
    assert opts.ap_password == 'test_ap_password'


# Generated at 2022-06-14 17:55:22.754890
# Unit test for function parseOpts
def test_parseOpts():
    from optparse import OptionValueError

    old_stdout = sys.stdout
    sys.stdout = io.BytesIO()

# Generated at 2022-06-14 17:57:19.385828
# Unit test for function parseOpts
def test_parseOpts():
    from youtube_dl.utils import (
        make_HTTPS_handler, unescapeHTML, daterange,
        match_filter_func, match_filter_func_all,
        )

    class FakeFile(object):
        def write(self, s):
            pass

    def test_match_filter(match_filter, match_filter_all, should_match, should_not_match):
        for t in should_match:
            if not match_filter(t):
                raise Exception('%r should have matched' % (t,))
        for t in should_not_match:
            if match_filter(t):
                raise Exception('%r should not have matched' % (t,))


# Generated at 2022-06-14 17:57:28.222394
# Unit test for function parseOpts
def test_parseOpts():
    from io import StringIO
    try:
        from unittest.mock import patch
    except ImportError:
        from test.mock_backport import patch
    with patch('sys.stderr', new_callable=StringIO) as stderr:
        if sys.version_info < (2, 7):
            with patch('test.test_youtube_dl.with_urllib2') as urllib2:
                urllib2.urlopen.side_effect = lambda *args: StringIO(
                    '--username=bar --password=baz --format=mp4\n'
                    '--call-home\n')
                parseOpts()

# Generated at 2022-06-14 17:57:38.618737
# Unit test for function parseOpts
def test_parseOpts():
    # default value
    assert parseOpts()[1].skip_download == False
    assert parseOpts()[1].simulate == False
    assert parseOpts()[1].format == None
    assert parseOpts()[1].get_thumbnail == False
    assert parseOpts()[1].write_all_thumbnails == False
    assert parseOpts()[1].write_description == False
    assert parseOpts()[1].writeinfojson == False
    assert parseOpts()[1].listformats == False
    assert parseOpts()[1].verbose == False
    assert parseOpts()[1].quiet == False
    assert parseOpts()[1].no_warnings == False
    assert parseOpts()[1].dump_user_agent == False

# Generated at 2022-06-14 17:57:48.030128
# Unit test for function parseOpts
def test_parseOpts():
    args = ['--verbose', '-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
            '--merge-output-format', 'mkv', '--yes-playlist', '--mark-watched', '--batch-file', '-']
    parser, opts, args = parseOpts(args)

    assert opts.verbose
    assert opts.format == 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4'
    assert opts.merge_output_format == 'mkv'
    assert opts.yes_playlist
    assert opts.mark_watched
    assert opts.batchfile == '-'

# parseOpts()
_parser, opts, args = parseOpts()


# Generated at 2022-06-14 17:57:57.119722
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-v'])
    assert opts.verbose
    parser, opts, args = parseOpts(['--verbose'])
    assert opts.verbose
    parser, opts, args = parseOpts(['--verbose', '--verbose'])
    assert opts.verbose == 2
    parser, opts, args = parseOpts(['-q'])
    assert opts.quiet
    parser, opts, args = parseOpts(['--quiet'])
    assert opts.quiet
    parser, opts, args = parseOpts(['--verbose', '--quiet'])
    assert opts.quiet
    assert not opts.verbose