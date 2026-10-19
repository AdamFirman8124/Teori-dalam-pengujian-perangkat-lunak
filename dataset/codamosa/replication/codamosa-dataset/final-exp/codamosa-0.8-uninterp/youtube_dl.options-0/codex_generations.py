

# Generated at 2022-06-14 17:48:41.205987
# Unit test for function parseOpts
def test_parseOpts():
    from sys import argv
    from os import remove

    f = open('./youtube-dl-test.conf', 'w')

# Generated at 2022-06-14 17:48:47.881560
# Unit test for function parseOpts
def test_parseOpts():
    from youtube_dl.utils import DateRange
    parser, opts, args = parseOpts(['--min-views', '20', '--max-views', '30'])
    assert opts.min_views == 20
    assert opts.max_views == 30
    assert opts.matchtitle is None
    assert opts.datebefore == DateRange(None)
    assert opts.dateafter == DateRange(None)
    parser, opts, args = parseOpts(['--datebefore', '20010101', '--dateafter', '19991231'])
    assert opts.datebefore == '20010101'
    assert opts.dateafter == '19991231'

# Generated at 2022-06-14 17:49:01.307478
# Unit test for function parseOpts
def test_parseOpts():

    class FakeArgv(object):
        """
        Fake argv for tests
        """
        def __init__(self):
            # argv is specific to each test
            self.argv = []

        def __enter__(self):
            """
            Fake argv, save original
            """
            # save original sys.argv
            self.argv_original = sys.argv

        def __exit__(self, exc_type, exc_value, traceback):
            """
            Restore original argv
            """
            # debug: print new sys.argv
            #print('TEST: sys.argv: %s' % sys.argv)
            # restore original sys.argv
            sys.argv = self.argv_original
            # debug: print restored sys.argv
            #print('TEST:

# Generated at 2022-06-14 17:49:09.051804
# Unit test for function parseOpts
def test_parseOpts():
    args = ['--username', 'plop', '--password', 'plip']
    parser, opts, args = parseOpts(args)
    assert opts.username == 'plop'
    assert opts.password == 'plip'
    args = ['-v']
    parser, opts, args = parseOpts(args)
    assert opts.verbose
    return True

# Result is False, None

# Generated at 2022-06-14 17:49:15.043821
# Unit test for function parseOpts
def test_parseOpts():
    def set_to_str(d):
        return '\n'.join('%s=%s' % (k, v) for (k, v) in sorted(d.items()))

    jobs = []

# Generated at 2022-06-14 17:49:24.573306
# Unit test for function parseOpts
def test_parseOpts():
    from youtube_dl.YoutubeDL import YoutubeDL
    from collections import namedtuple
    args = namedtuple('args', ['test'])
    # Test 1
    args.test = '--test'
    opts = namedtuple('opts', ['quiet'])
    opts.quiet = True
    opts = parseOpts(args, opts)
    assert(opts.quiet == False)
    # Test 2
    ydl = YoutubeDL()
    ydl = parseOpts(args, ydl)
    assert(ydl.params['test'] == True)

# ------------------------------------------------------------------------------- CONFIG -------------------------------------------------------------------------


# Generated at 2022-06-14 17:49:36.404124
# Unit test for function parseOpts
def test_parseOpts():
    assert parseOpts({'username': 'user@server.com'})[1].username == 'user@server.com'
    assert parseOpts({'username': 'user@server.com', 'password': 'pwd'})[1].password == 'pwd'
    assert parseOpts({'username': 'user@server.com', 'password': 'pwd'})[1].nopassword == False

    assert parseOpts({})[1].playliststart == 1
    assert parseOpts({'playliststart': '3'})[1].playliststart == 3
    assert parseOpts({'playlistend': '4'})[1].playlistend == 4

    assert parseOpts({'username': 'user@server.com', 'password': 'pwd'})[1].usenetrc == 'AUTO'


# Generated at 2022-06-14 17:49:44.923873
# Unit test for function parseOpts
def test_parseOpts():
    import doctest
    parser, opts, args = parseOpts(['-v'])
    assert opts.verbose == True
    assert args == []

    parser, opts, args = parseOpts(['http://localhost/'])
    assert opts.verbose == False
    assert args == ['http://localhost/']

    parser, opts, args = parseOpts(['-o', 'myfile.flv', 'http://localhost/'])
    assert opts.verbose == False
    assert opts.outtmpl == 'myfile.flv'
    assert args == ['http://localhost/']

    parser, opts, args = parseOpts(['-c', 'http://localhost/'])
    assert opts.continue_dl == True
    assert args == ['http://localhost/']

# Unit test

# Generated at 2022-06-14 17:49:50.323254
# Unit test for function parseOpts
def test_parseOpts():
    from tempfile import mkstemp
    from shutil import move

    def opts2str(opts):
        def is_str(obj):
            if sys.version_info < (3,):
                return isinstance(obj, basestring)
            else:
                return isinstance(obj, str)

        return ''.join([' --%s' % k + (' "%s"' % v if is_str(v) and ' ' in v else ' %s' % v) if v is not True else '' for k, v in vars(opts).items()])

    fd, fname = mkstemp(prefix='yt-dl.', suffix='.conf')

# Generated at 2022-06-14 17:49:54.554790
# Unit test for function parseOpts
def test_parseOpts():
    args = ['--proxy', 'http://foo.bar.com', 'http://www.youtube.com/watch?v=BaW_jenozKc']
    parser, opts, args = parseOpts(args)
    assert opts.proxy == 'http://foo.bar.com'
    assert args == ['http://www.youtube.com/watch?v=BaW_jenozKc']


# Generated at 2022-06-14 17:50:21.500251
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-v', '--write-thumbnail', '--sleep-interval', '1', '-g', 'http://www.youtube.com/watch?v=BaW_jenozKc'])
    assert parser
    assert opts
    assert args
    assert opts.writethumbnail
    assert opts.verbose



# Generated at 2022-06-14 17:50:28.530936
# Unit test for function parseOpts
def test_parseOpts():
    # Test if --version and --help work as expected
    assert(parseOpts(['--version']) is None)
    assert(parseOpts(['-h']) is None)
    assert(parseOpts(['--help']) is None)

    # Test for verbose option
    assert(parseOpts([])[1].verbose is False)
    assert(parseOpts(['-v'])[1].verbose is True)
    assert(parseOpts(['--verbose'])[1].verbose is True)
    assert(parseOpts(['-vv'])[1].verbose is False)
    assert(parseOpts(['--verbose', '--verbose'])[1].verbose is False)
    assert(parseOpts(['-q'])[1].verbose is False)
   

# Generated at 2022-06-14 17:50:38.647809
# Unit test for function parseOpts

# Generated at 2022-06-14 17:50:43.752974
# Unit test for function parseOpts
def test_parseOpts():
    sampleArguments = ['--output', '%(upload_date)s', '--verbose', '--test']
    parser, opts, args = parseOpts(sampleArguments)
    assert opts.outtmpl == '%(upload_date)s'
    assert opts.verbose == True
    assert opts.test == True

# }}}

# Generated at 2022-06-14 17:50:56.103671
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts()
    # Test for --version
    sys.argv = [sys.argv[0], "--version"]
    try:
        parseOpts()
        raise Exception('parseOpts() should exit')
    except SystemExit as e:
        assert(e.code == 0)
    sys.argv = [sys.argv[0]]

    # Test for missing URLs
    try:
        parseOpts()
        raise Exception('parseOpts() should exit')
    except SystemExit as e:
        assert(e.code == 1)
    sys.argv = [sys.argv[0]]

    # Test for missing URLs and download first format
    sys.argv = [sys.argv[0], "--format", "1"]

# Generated at 2022-06-14 17:51:06.763138
# Unit test for function parseOpts
def test_parseOpts():
    # Test the parsing.
    # First the boilerplate code to create a fake
    # class and module.
    class FakeModule(object):
        def __init__(self):
            self.version = '1.2.3'
            self.__dict__ = {}
    class FakeOptParse(object):
        def __init__(self):
            self.__dict__ = {}
        def OptionGroup(self, *args, **kwargs):
            return None
        def OptionParser(self, *args, **kwargs):
            return None
        def OptionValueError(self, *args, **kwargs):
            return None
        def SUPPRESS_HELP(self, *args, **kwargs):
            return None
        def SUPPRESS_USAGE(self, *args, **kwargs):
            return None
        # Fake

# Generated at 2022-06-14 17:51:17.013449
# Unit test for function parseOpts
def test_parseOpts():
    import os
    import tempfile
    # With no argument, parseOpts returns a subset of
    # sys.argv[1:].
    # Check that we return at least one argument
    parser, opts, args = parseOpts(['-x'])
    assert len(args) == 0

    # Check basic parsing
    parser, opts, args = parseOpts(
        ['--username', 'username', '-p', 'password', 'url'])
    assert opts.username == 'username'
    assert opts.password == 'password'
    assert args == ['url']

    # Check that credentials are hidden
    parser, opts, args = parseOpts(
        ['--username', 'username', '-p', 'password', '--verbose', 'url'])

# Generated at 2022-06-14 17:51:28.177615
# Unit test for function parseOpts
def test_parseOpts():
    def fn():
        pass
    fn.__name__ = 'fake_main'
    parser, options, args = parseOpts(fn, ['--no-check-certificate', '--verbose', '--ignore-config', '--', 'foo', 'bar'])
    assert not options.nocheckcertificate
    assert options.verbose
    assert options.ignoreconfig

    # Test long option merging (see https://github.com/rg3/youtube-dl/issues/7107)
    parser, options, args = parseOpts(fn, ['--no-check-certificate', '--verbose', '--get-url'])
    assert options.geturl

    parser, options, args = parseOpts(fn, ['-i', '-v', '--no-progress'])
    assert options.ignoreconfig

# Generated at 2022-06-14 17:51:37.890370
# Unit test for function parseOpts
def test_parseOpts():
    import pytest

# Generated at 2022-06-14 17:51:44.163498
# Unit test for function parseOpts
def test_parseOpts():
    def test_option(option, expected_value):
        argv = ['-o', '%(id)s.%(ext)s', '--verbose']
        if option.startswith('-'):
            argv.append(option)
        else:
            argv.extend(option.split())
        opts, args = parseOpts(argv)
        assert opts.__dict__[option.lstrip('-').replace('-', '_')] == expected_value

    test_option('-o', '%(id)s.%(ext)s')
    test_option('--output', '%(id)s.%(ext)s')

    test_option('--verbose', True)
    test_option('--no-verbose', False)

# Generated at 2022-06-14 17:52:00.628874
# Unit test for function parseOpts
def test_parseOpts():
    print('Unit test for parseOpts')
    parser, opt, args = parseOpts(None)
    print('Passed')


# Generated at 2022-06-14 17:52:11.072608
# Unit test for function parseOpts
def test_parseOpts():
    from collections import namedtuple

    def test(args, expected_opts, expected_args, strip_prog=False):
        # Build expected opts
        Opts = namedtuple('Opts', expected_opts.keys())
        parser, opts, args = parseOpts(args)
        expected_opts = Opts(**expected_opts)
        if strip_prog:
            sys.argv = ['youtube-dl']
        elif sys.version_info < (3,):
            sys.argv = [a.encode(preferredencoding(), 'replace') for a in sys.argv]
        assertEqual(str(opts), str(expected_opts))
        assertEqual(args, expected_args)


# Generated at 2022-06-14 17:52:12.497913
# Unit test for function parseOpts
def test_parseOpts():
    opts, _ = parseOpts(['-v'])
    assert opts.verbose

# Generated at 2022-06-14 17:52:13.833379
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts()
# Test: parseOpts


# Generated at 2022-06-14 17:52:20.341788
# Unit test for function parseOpts
def test_parseOpts():
    output = getTestdataPath('-o')

    def _run(args):
        conf = ['--ignore-config'] + args
        parser, opts, _ = parseOpts(overrideArguments=conf)
        return parser, opts, output in opts.__dict__.values()

    parser, opts, hasOutput = _run([
        '--extract-audio', '--audio-format', 'best', '-o', output,
        'http://www.youtube.com/watch?v=BaW_jenozKc'])
    assertIsNone(parser.get_option_by_opt_string('-o').deprecated_opts)
    assertEqual(opts.outtmpl, output)
    assertTrue(hasOutput)


# Generated at 2022-06-14 17:52:31.470887
# Unit test for function parseOpts
def test_parseOpts():
    import optparse
    from pytube import opts
    try:
        validate = optparse.Option.__getattribute__(opts, "check_value")
        assert validate(opts, 'outtmpl', 'foo') == None
        assert validate(opts, 'outtmpl', 'foo%(bar)s') == None
        assert validate(opts, 'outtmpl', 'foo%(id)s') == None
        assert validate(opts, 'outtmpl', 'foo%(invalid)s') == None
    except AttributeError:  # python 2.6
        validate = optparse.Option.__getattribute__(opts, "checker")
        assert validate(opts, 'outtmpl', 'foo') == None
        assert validate(opts, 'outtmpl', 'foo%(bar)s')

# Generated at 2022-06-14 17:52:39.858650
# Unit test for function parseOpts
def test_parseOpts():
    class MockOp(object):
        def __init__(self, x):
            self.x = x

        def __str__(self):
            return str(self.x)

    parser, opts, args = parseOpts([MockOp(0), '--username', MockOp(1), MockOp(2)])
    assert opts.username == MockOp(1) and args == [MockOp(0), MockOp(2)]



# Generated at 2022-06-14 17:52:47.498955
# Unit test for function parseOpts

# Generated at 2022-06-14 17:52:59.899732
# Unit test for function parseOpts
def test_parseOpts():
    from youtube_dl.YoutubeDL import YoutubeDL
    import youtube_dl.extractor.youtube
    youtube_dl.extractor.youtube.YoutubeIE.extract()
    import youtube_dl.extractor.common
    youtube_dl.extractor.common.InfoExtractor.extract()
    
    
    parser, opts, args = parseOpts()
    print(parser)
    print(opts)
    print(args)
    
    
    
    
    
    
    
    
    ydl = YoutubeDL(opts)
    a = YouTubeVideo()
    print(ydl.extract_info('https://www.youtube.com/watch?v=XevU0ydoU3M', download=False))
    
    

# Generated at 2022-06-14 17:53:13.150000
# Unit test for function parseOpts
def test_parseOpts():
    from tempfile import NamedTemporaryFile
    from distutils.spawn import find_executable

    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO

    def _to_str(s):
        if isinstance(s, bytes):
            return s.decode()
        return s

    def _from_str(s):
        if isinstance(s, str):
            return s.encode()
        return s

    def _readOutput(buf, out=False):
        out_str = err_str = ''
        if out:
            out_str = buf.read()
        else:
            err_str = buf.read()
        return _from_str(out_str), _from_str(err_str)


# Generated at 2022-06-14 17:53:41.892750
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-l', 'example.com'])
    assert opts.usetitle
    assert args == ['example.com']
    parser, opts, args = parseOpts(['--playlist-start', '1', '-l', 'example.com'])
    assert opts.playliststart == 1


# Generated at 2022-06-14 17:53:53.148758
# Unit test for function parseOpts
def test_parseOpts():
    import glob
    import shutil
    import tempfile
    from youtube_dl.compat import compat_expanduser, compat_opener

    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        f.write('-o ~/test%%\n')

# Generated at 2022-06-14 17:54:01.754401
# Unit test for function parseOpts
def test_parseOpts():
    from sys import argv as sys_argv
    from test.helper import FakeYDL
    from io import StringIO

    def parseOpts(opts):
        def hide_passwords(l):
            return [(opt if opt[:8] != '--password' else '--password PASSWORD') for opt in l]

        orig_stdout = sys.stdout
        try:
            sys.stdout = StringIO()
            fake_ydl = FakeYDL()
            fake_ydl.params = {}
            fake_ydl.parseOpts(opts)
            output = sys.stdout.getvalue()
        finally:
            sys.stdout.close()
            sys.stdout = orig_stdout

# Generated at 2022-06-14 17:54:15.435808
# Unit test for function parseOpts
def test_parseOpts():
    def _test(args, expected):
        parser, opts, args = parseOpts(args)
        assert vars(opts) == expected, '%s instead of %s' % (vars(opts), expected)

# Generated at 2022-06-14 17:54:21.748458
# Unit test for function parseOpts
def test_parseOpts():
    def test(args, expected_opts):
        parser, opts, args = parseOpts(args)
        for key, expected_value in expected_opts.items():
            value = getattr(opts, key)
            assert value == expected_value, (
                '%s: expected %r, got %r' % (key, expected_value, value))
    test(
        ['--format', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'],
        {'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'})

# Generated at 2022-06-14 17:54:32.557792
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts([])
    assert(opts.verbose == False)
    parser, opts, args = parseOpts([u'--verbose', u'-v'])
    assert(opts.verbose == True)
    parser, opts, args = parseOpts([u'--no-verbose', u'--verbose'])
    assert(opts.verbose == False)
    parser, opts, args = parseOpts([u'-h'])
    assert(opts.help == True)
    parser, opts, args = parseOpts([u'--help'])
    assert(opts.help == True)
    parser, opts, args = parseOpts([u'--no-check-certificate'])
    assert(opts.nocheckcertificate == True)

# Generated at 2022-06-14 17:54:41.654503
# Unit test for function parseOpts
def test_parseOpts():
    try:
        from urllib.request import parse_http_list # python 3
    except:
        from mimetools import Message # python 2
    def parse_http_list(x):
        return Message(StringIO(x)).headers

# Generated at 2022-06-14 17:54:52.913334
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-U', 'MyUserAgent', '-f', '18/22/37', 'http://www.youtube.com/watch?v=BaW_jenozKc'])
    assertEqual(opts.usenetrc, False)
    assertEqual(opts.username, None)
    assertEqual(opts.password, None)
    assertEqual(opts.video_password, None)
    assertEqual(opts.ap_username, None)
    assertEqual(opts.ap_password, None)
    assertEqual(opts.quiet, False)
    assertEqual(opts.no_warnings, False)
    assertEqual(opts.forceurl, False)

# Generated at 2022-06-14 17:54:55.478164
# Unit test for function parseOpts
def test_parseOpts():
    print(('\n' + '=' * 60 + '\n' + 'parseOpts tests\n' + '=' * 60 + '\n'))
    return

# Generated at 2022-06-14 17:55:03.707619
# Unit test for function parseOpts
def test_parseOpts():
    from youtube_dl.YoutubeDL import YoutubeDL
    parser, opts, args = parseOpts(['-i', '--yes-playlist', '-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio',
                                    '--no-mtime', '--all-subs', '--write-sub', '--write-auto-sub',
                                    '--write-thumbnail', '--list-thumbnails', '--merge-output-format', 'mkv'])
    assert opts.get('ignoreerrors') is True
    assert opts.get('noplaylist') is False
    assert opts.get('no_color') is True
    assert opts.get('geo_bypass') is False
    assert opts.get('usenetrc') is False

# Generated at 2022-06-14 17:55:58.626891
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts()
    assert opts.username == 'test'
    assert opts.password == 'test_password'
    assert opts.usenetrc == False

    parser, opts, args = parseOpts(['--username', 'test_2'])
    assert opts.username == 'test_2'
    assert opts.password == 'test_password'
    assert opts.usenetrc == False

    parser, opts, args = parseOpts(['--password', 'test_password_2'])
    assert opts.username == 'test'
    assert opts.password == 'test_password_2'
    assert opts.usenetrc == False

    parser, opts, args = parseOpts(['--usenetrc'])

# Generated at 2022-06-14 17:56:08.866938
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts()
    assert opts.verbose == False
    assert opts.version == False
    assert opts.quiet == False
    assert opts.simulate == False
    assert opts.skip_download == False
    assert opts.format == None
    assert opts.listformats == False
    assert opts.outtmpl == '%(title)s-%(id)s.%(ext)s'
    assert opts.autonumber_size == None
    assert opts.autonumber_start == 1
    assert opts.usetitle == False
    assert opts.autonumber == False
    assert opts.useid == False
    assert opts.writedescription == False
    assert opts.writeinfojson == False
    assert opts.writeannotations

# Generated at 2022-06-14 17:56:17.949312
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-o', 'foobar', 'foo'])
    assert opts.outtmpl == 'foobar'
    assert args == ['foo']

    parser, opts, args = parseOpts(['-o', '%(uploader)s-%(title)s-%(id)s.%(ext)', 'foo'])
    assert opts.outtmpl == '%(uploader)s-%(title)s-%(id)s.%(ext)'
    assert args == ['foo']

    parser, opts, args = parseOpts(['-o', 'foobar', '-f', 'best', 'foo'])
    assert opts.outtmpl == 'foobar'
    assert opts.format == 'best'
    assert args == ['foo']

# Generated at 2022-06-14 17:56:27.094842
# Unit test for function parseOpts
def test_parseOpts():
    assert parseOpts(['-o', '%(uploader)s', '-o', '%(uploader)s2', 'url']) == (
        'youtube-dl -o %(uploader)s -o %(uploader)s2 url',
        OrderedDict([('o', '%(uploader)s'), ('o', '%(uploader)s2')]), ['url'])
    assert parseOpts(['-o%(uploader)s', 'url']) == (
        'youtube-dl -o%(uploader)s url', OrderedDict([('o', '%(uploader)s')]), ['url'])

# Generated at 2022-06-14 17:56:30.697864
# Unit test for function parseOpts
def test_parseOpts():
    global _availableEncodings
    _availableEncodings = ['utf-8','utf-16']
    _parseOpts(['-h'])
#
# end of _parseOpts


# Generated at 2022-06-14 17:56:41.927345
# Unit test for function parseOpts
def test_parseOpts():
    opts, args = parseOpts(['-f', 'mp4', 'https://www.youtube.com'])
    assert 'https://www.youtube.com' in args
    assert opts.usenetrc is False
    assert opts.noplaylist is False
    assert opts.ratelimit == '0'
    assert opts.nooverwrites is False
    assert opts.ignoreerrors is False
    assert opts.forceurl is False
    assert opts.forcethumbnail is False
    assert opts.forceduration is False
    assert opts.forcefilename is False
    assert opts.simulate is False
    assert opts.skip_download is False
    assert opts.format is None
    assert opts.listformats is False
    assert opts.outtmpl is None
    assert opt

# Generated at 2022-06-14 17:56:51.389465
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-h'])
    assert not args
    parser, opts, args = parseOpts(['--help'])
    assert not args
    parser, opts, args = parseOpts(['-U', 'user', '-P', 'passwd', 'https://youtube.com/watch?v=BaW_jenozKc'])
    assert opts.username == 'user'
    assert opts.password == 'passwd'
    assert args == ['https://youtube.com/watch?v=BaW_jenozKc']



# Generated at 2022-06-14 17:57:03.123237
# Unit test for function parseOpts
def test_parseOpts():
    import tempfile
    fd, filename = tempfile.mkstemp('.conf')
    filename = compat_expanduser(filename)
    try:
        os.write(fd, b'--format mp4\n--username abc\n--password def')
        os.close(fd)
        parser, opts, args = parseOpts([
            '--config-location', filename,
            '--username', 'ghi',
            '--password', 'jkl',
            '--verbose'])
        assert opts.username == 'abc'
        assert opts.password == 'def'
        assert opts.format == 'mp4'
    finally:
        os.remove(filename)
test_parseOpts()

# Generated at 2022-06-14 17:57:04.883307
# Unit test for function parseOpts
def test_parseOpts():
    return



# Generated at 2022-06-14 17:57:10.583631
# Unit test for function parseOpts
def test_parseOpts():
    success = True

    # making sure --version doesn't raise any exception
    try:
        parseOpts(['--version'])
        parseOpts(['--help'])
        parseOpts(['-h'])
    except:
        success = False
    return success


try:
    import argcomplete
except ImportError:
    argcomplete = None

# Command line argument completion