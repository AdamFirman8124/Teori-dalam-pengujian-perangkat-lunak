

# Generated at 2022-06-14 17:48:38.172327
# Unit test for function parseOpts
def test_parseOpts():
    opts = parseOpts()
    argv = opts[2]
    for argument in ['--write-info-json', '--write-description', '--write-annotations', '-x']:
        assert argument in argv


# Generated at 2022-06-14 17:48:45.968789
# Unit test for function parseOpts
def test_parseOpts():
    try:
        __builtins__.input = lambda x: 42
    except AttributeError:
        __builtins__.raw_input = lambda x: 42


    input_strs = ['https://www.youtube.com/watch?v=BaW_jenozKc', '', '', 'yes']
    def input_callback(prompt):
        return input_strs.pop(0)

    def parseOpts_test():
        args = ['--username', 'foo', '--password', 'bar',
                '--extract-audio', '--audio-format', 'mp3',
                '--format', 'best', '--verbose']
        parser, opts, args = parseOpts(args)

        assert opts.username == 'foo'
        assert opts.password == 'bar'

# Generated at 2022-06-14 17:48:59.312885
# Unit test for function parseOpts
def test_parseOpts():
    import re
    from optparse import OptionValueError
    def getopts(args):
        try:
            _, retval, _ = parseOpts(args)
        except OptionValueError as err:
            return (str(err),)
        return tuple(retval.__dict__.values())
    assert getopts([]) == ('', '', False, False, False, False)
    assert getopts(['--username', 'foo', '--password', 'bar', '--video-password', 'baz']) == ('bar', 'foo', 'baz', False, False, False)
    assert getopts(['-u', 'foo', '-p', 'bar', '--video-password', 'baz']) == ('bar', 'foo', 'baz', False, False, False)

# Generated at 2022-06-14 17:49:06.035059
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts()

    assert(opts.ratelimit == 'N/A')
    assert(opts.retries == 10)
    assert(opts.buffersize == 'N/A')
    assert(opts.noresizebuffer == False)

    assert(opts.playliststart == 1)
    assert(opts.playlistend == None)
    assert(opts.matchtitle == None)
    assert(opts.rejecttitle == None)
    assert(opts.max_downloads == None)
    assert(opts.min_filesize == None)
    assert(opts.max_filesize == None)
    assert(opts.date == None)
    assert(opts.datebefore == None)
    assert(opts.dateafter == None)
   

# Generated at 2022-06-14 17:49:10.606271
# Unit test for function parseOpts
def test_parseOpts():
    import sys
    import tempfile

    def _write_config_file(contents):
        fd, filename = tempfile.mkstemp()
        if sys.version_info < (3,):
            filename = filename.encode(preferredencoding())
        os.write(fd, contents.encode('utf-8'))
        os.close(fd)
        return filename

    def _read_config_file(filename):
        with io.open(filename, 'r', encoding='utf-8') as f:
            return f.read()


# Generated at 2022-06-14 17:49:15.901466
# Unit test for function parseOpts
def test_parseOpts():
    try:
        import unittest2 as unittest
    except ImportError:
        import unittest
    opts, args = parseOpts([])
    class TestParseOpts(unittest.TestCase):
        def test_opt_int(self):
            self.assertEqual(type(opts.verbose), int)
        
        def test_opt_bool(self):
            self.assertEqual(type(opts.call_home), bool)
        
        def test_opt_none(self):
            self.assertEqual(type(opts.abrt), type(None))

    unittest.main()
#test_parseOpts()


# Generated at 2022-06-14 17:49:17.981075
# Unit test for function parseOpts
def test_parseOpts():
    pass
#parseOpts()


# Generated at 2022-06-14 17:49:28.255916
# Unit test for function parseOpts
def test_parseOpts():
    def check_opts_defaults(opts):
        assert opts.noplaylist is False
        assert opts.usenetrc is False
        assert opts.username is None
        assert opts.password is None
        assert opts.twofactor is None
        assert opts.videopassword is None
        assert opts.quiet is False
        assert opts.no_warnings is False
        assert opts.forceurl is False
        assert opts.forcethumbnail is False
        assert opts.forcetitle is False
        assert opts.forcedescription is False
        assert opts.forcefilename is False
        assert opts.forcejson is False
        assert opts.dump_single_json is False
        assert opts.simulate is False
        assert opts.skip_download is False


# Generated at 2022-06-14 17:49:38.857069
# Unit test for function parseOpts
def test_parseOpts():
    args = ['--username=foo', '--password=bar', '-F', 'http://a.com', 'http://b.com']
    parser, opts, args = parseOpts(overrideArguments=args)
    assert opts.username == 'foo'
    assert '--username=foo' not in args
    assert opts.password == 'bar'
    assert '--password=bar' not in args
    assert opts.usenetrc is False
    assert '--usenetrc' not in args
    assert opts.quiet is False
    assert '--quiet' not in args
    assert opts.format == 'best'
    assert '-F' not in args
    assert args == ['http://a.com', 'http://b.com']


# Generated at 2022-06-14 17:49:46.560054
# Unit test for function parseOpts
def test_parseOpts():
    print('Testing parseOpts')
    from youtube_dl.extractor import gen_extractors
    args = ['--extractor-descriptions']
    parser, opts, args = parseOpts(args)
    assert opts.print_version and not opts.simulate
    gen_extractors()

    args = ['--dump-intermediate-pages']
    parser, opts, args = parseOpts(args)
    assert opts.dump_intermediate_pages

    args = ['-v']
    parser, opts, args = parseOpts(args)
    assert opts.verbose == 1

    args = ['--no-warnings']
    parser, opts, args = parseOpts(args)
    assert not opts.verbose

    args = ['--quiet', '--no-warnings']


# Generated at 2022-06-14 17:50:14.722407
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts()

    # Test config file reading
    system_conf = user_conf = custom_conf = []
    system_conf = _readOptions('/etc/youtube-dl.conf')
    if '--ignore-config' not in system_conf:
        user_conf = _readUserConf()
    
    argv = system_conf + user_conf + custom_conf
    opts, args = parser.parse_args(argv)
    assert(opts.download_archive == "~/.config/youtube-dl/archive")
    assert(opts.extract_audio == True)
    assert(opts.audioformat == "best")
    assert(opts.audioquality == "5")
    
    # Test --output-na-placeholder

# Generated at 2022-06-14 17:50:23.541422
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts([])
    assert opts.simulate is False, "--no-simulate should be default"
    assert opts.geturl is False, "--get-url should be default"
    assert opts.gettitle is False, "--get-title should be default"
    assert opts.getid is False, "--get-id should be default"
    assert opts.getthumb is False, "--get-thumbnail should be default"
    assert opts.getdescription is False, "--get-description should be default"
    assert opts.getfilename is False, "--get-filename should be default"
    assert opts.getformat is False, "--get-format should be default"

    parser, opts, args = parseOpts(['--no-simulate'])
   

# Generated at 2022-06-14 17:50:27.093357
# Unit test for function parseOpts
def test_parseOpts(): parseOpts(['-i', '-v'])


# Generated at 2022-06-14 17:50:28.941228
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts()
test_parseOpts()



# Generated at 2022-06-14 17:50:38.953281
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-i', '-u', 'user', '-p', 'pwd', 'http://www.youtube.com/watch?v=BaW_jenozKc'])
    assert opts.username == 'user'
    assert opts.password == 'pwd'
    assert opts.usenetrc == True
    assert opts.verbose == False
    assert opts.quiet == False
    assert opts.ignoreerrors == False
    assert opts.forceurl == False
    assert opts.forcetitle == False
    assert opts.simulate == False
    assert opts.skip_download == False
    assert opts.format == None
    assert opts.listformats == False
    assert opts.list_thumbnails == False
    assert opts.matchtitle

# Generated at 2022-06-14 17:50:51.304614
# Unit test for function parseOpts
def test_parseOpts():
    from functools import partial
    from collections import namedtuple

    # Note: We only test the "hidden" arguments, but not the normal
    # ones, since it would require a big amount of work to keep them in
    # sync with the optparse-generated help message.

    # namedtuple to contain actual and expected values
    testValue = namedtuple('testValue', 'actual, expected')

    # define tests for various arguments

# Generated at 2022-06-14 17:51:00.429691
# Unit test for function parseOpts
def test_parseOpts():
    assert parseOpts(['-f', 'bestvideo+bestaudio'])[1].format == 'bestvideo+bestaudio'
    assert parseOpts(['--format', 'bestvideo+bestaudio'])[1].format == 'bestvideo+bestaudio'
    assert parseOpts(['--format', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'])[1].format == 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'


# Generated at 2022-06-14 17:51:01.448773
# Unit test for function parseOpts
def test_parseOpts():
    return parseOpts(['-F'])


# Generated at 2022-06-14 17:51:14.308842
# Unit test for function parseOpts
def test_parseOpts():
    assert parseOpts(['--version']) == 0
    assert parseOpts(['-U', 'foobar', 'fie']) == 0
    assert parseOpts(['-U', 'foobar', '-f', '22', 'fie']) == 0
    assert parseOpts(['-U', 'foobar', '-f', '22/44/45', 'fie']) == 0
    assert parseOpts(['-U', 'foobar', '-f', '-1/mp4/45', 'fie']) == 0
    # Subtitle
    assert parseOpts(['-U', 'foobar', '--write-sub', '--sub-lang', 'en', '--', 'fie']) == 0

# Generated at 2022-06-14 17:51:26.351387
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts([
        '--no-warnings',
        '--verbose',
        '--default-search', 'auto',
        '--ignore-config',
        '--extract-audio',
        '--audio-format', 'best',
        '--audio-quality', '5',
        '--recode-video', 'mp4',
        '--prefer-avconv',
        '--embed-thumbnail',
        '--add-metadata',
        '--metadata-from-title', '%(artist)s - %(title)s',
        '--convert-subs', 'srt'
        ])
    assert opts.ignoreerrors == False
    assert opts.dump_intermediate_pages == False
    assert opts.write_pages == False

# Generated at 2022-06-14 17:51:59.150195
# Unit test for function parseOpts
def test_parseOpts():
    from optparse import Values

    def assertEqualOpts(msg, a, b):
        for key in a.__dict__:
            if key in ['password', 'username', 'usenetrc']:
                continue
            assert a.__dict__[key] == b.__dict__[key], '%s: %r != %r in key %r' % (msg, a.__dict__[key], b.__dict__[key], key)

    p, opts, args = parseOpts(['-U', 'Unit Test User Agent', '--videopassword', 'ping', 'blahblah'])
    assert isinstance(opts, Values)

# Generated at 2022-06-14 17:52:05.077580
# Unit test for function parseOpts
def test_parseOpts():
    import youtube_dl.YoutubeDL
    options = ['--playlist-start','324']
    ydl = YoutubeDL.YoutubeDL(options)
    opts = ydl.parseOpts()
    print('playlist-start:' + str(opts.playliststart))
    print('outtmpl:' + opts.outtmpl)
    print('verbose:' + str(opts.verbose))

# Generated at 2022-06-14 17:52:17.916756
# Unit test for function parseOpts
def test_parseOpts():
    from .extractor.common import InfoExtractor
    def my_readOptions(self, filename):
        return ['-o', 'mytemplate']

    if getattr(InfoExtractor, 'real_readOptions', None) is None:
        InfoExtractor.real_readOptions = InfoExtractor.readOptions
        InfoExtractor.readOptions = my_readOptions
    try:
        parser, opts, args = parseOpts([
            '--download-archive', 'archive',
            'http://www.youtube.com/watch?v=BaW_jenozKc'])
    finally:
        InfoExtractor.readOptions = InfoExtractor.real_readOptions
        InfoExtractor.real_readOptions = None

    assert opts.download_archive == 'archive'
    assert opts.outtmpl == 'mytemplate'
   

# Generated at 2022-06-14 17:52:29.880136
# Unit test for function parseOpts
def test_parseOpts():
    def check(options, option_name, option_value):
        def _check_set(_option_value):
            if not hasattr(options, option_name):
                raise AssertionError('%s is not set' % option_name)
            if getattr(options, option_name) != _option_value:
                raise AssertionError(
                    '%s is not set to %r but to %r' % (
                        option_name, _option_value, getattr(options, option_name)))
        def _check_not_set():
            if hasattr(options, option_name):
                raise AssertionError('%s is set' % option_name)
        if option_value is None:
            _check_not_set()

# Generated at 2022-06-14 17:52:42.554326
# Unit test for function parseOpts
def test_parseOpts():
    class MockOptionParser(object):
        def __init__(self, parser, opts, args):
            self.parser = parser
            self.opts = opts
            self.args = args

        def add_option(self, *args, **kwargs):
            self.parser.add_option(*args, **kwargs)
        def add_option_group(self, *args, **kwargs):
            self.parser.add_option_group(*args, **kwargs)
        def parse_args(self, args):
            return self.parser.parse_args(args)
    class MockGetProxies(object):
        def getproxies(self):
            return {}
    MockGetProxies.getproxies = getproxies
    class MockOptParse(object):
        SUPPRESS_HELP

# Generated at 2022-06-14 17:52:53.541038
# Unit test for function parseOpts
def test_parseOpts():
    # Test calling with no options
    parser, opts, _ = parseOpts(None)

    # Test calling with empty options
    parser, opts, _ = parseOpts([])
    assert opts.__dict__ == parser.get_default_values().__dict__

    # Test calling with a single option
    parser, opts, _ = parseOpts(['-v'])
    assert opts.verbose
    parser, opts, _ = parseOpts(['--verbose'])
    assert opts.verbose

    # Test calling with a single option and a value
    parser, opts, _ = parseOpts(['--verbose'])
    assert opts.verbose
    parser, opts, _ = parseOpts(['-o', 'filename'])

# Generated at 2022-06-14 17:53:03.767355
# Unit test for function parseOpts
def test_parseOpts():
    import sys
    import getopt
    from io import StringIO
    from youtube_dl.utils import encodeFilename

    class OptError(Exception):
        pass

    _old_opterr = getopt.GetoptError
    _old_opt_parse = getopt.gnu_getopt
    _old_write = sys.stderr.write
    _old_out = sys.stdout
    _old_encode = encodeFilename

# Generated at 2022-06-14 17:53:14.443428
# Unit test for function parseOpts
def test_parseOpts():
    from youtube_dl.utils import encodeArgument
    args = ['--username', 'foo', '--password', 'bar']
    parser, opts, _ = parseOpts(args)
    assert opts.username == 'foo'
    # Password is not filled in
    assert opts.password is None
    # But it is in help description
    _, _, desc = parser.format_option_help(encodeArgument('--username'))
    assert '--username=USERNAME' in desc
    _, _, desc = parser.format_option_help(encodeArgument('--password'))
    assert '--password=PASSWORD' in desc

    args = ['--username', 'foo', '--password', 'bar', '--no-call-home']
    # Parse args once again to test --no-call-home


# Generated at 2022-06-14 17:53:26.071159
# Unit test for function parseOpts
def test_parseOpts():
    assert parseOpts(['-F', '-f', 'bestvideo+bestaudio'])[1].format == 'bestvideo+bestaudio'
    assert parseOpts(['-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]'])[1].format == 'bestvideo[ext=mp4]+bestaudio[ext=m4a]'
    assert parseOpts(['-F', '-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]'])[1].format == 'bestvideo[ext=mp4]+bestaudio[ext=m4a]'

# Generated at 2022-06-14 17:53:37.982009
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts([])
    assert opts.usenetrc is False
    assert opts.forcetitle is False
    assert opts.forceid is False
    assert opts.forcedescription is False
    assert opts.forcefilename is False
    assert opts.forcethumbnail is False
    assert opts.forceduration is False
    assert opts.forcejson is False
    assert opts.dump_user_agent is False
    assert opts.no_warnings is False
    assert opts.simulate is False
    assert opts.skip_download is False
    assert opts.format is None
    assert opts.listformats is False
    assert opts.youtube_include_dash_manifest is False
    assert opts.match_filter is None
    assert opts.no

# Generated at 2022-06-14 17:54:24.080069
# Unit test for function parseOpts
def test_parseOpts():
    from sys import argv
    from io import StringIO
    from contextlib import contextmanager
    from unittest import main, TestCase
    from tempfile import NamedTemporaryFile
    from os import remove
    from time import time
    from datetime import timedelta

    @contextmanager
    def stdoutIO(stdout=None):
        old = sys.stdout
        if stdout is None:
            stdout = StringIO()
        sys.stdout = stdout
        yield stdout
        sys.stdout = old


# Generated at 2022-06-14 17:54:26.246174
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts([])


# Generated at 2022-06-14 17:54:36.691745
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(
        overrideArguments=[
            '-v',
            'https://www.youtube.com/user/Scishow',
            '-o', '%(uploader)s/%(upload_date)s - %(title)s - %(id)s.%(ext)s'
        ]
    )
    assert opts.verbose == 2
    assert args == ['https://www.youtube.com/user/Scishow']
    assert opts.outtmpl == '%(uploader)s/%(upload_date)s - %(title)s - %(id)s.%(ext)s'


# Generated at 2022-06-14 17:54:50.905928
# Unit test for function parseOpts
def test_parseOpts():
    global sys
    fake_sys = FakeSys(['-v'])
    with patch.object(sys, 'argv', fake_sys.argv):
        parser, opts, _ = parseOpts()
        assert opts.verbose == True
    with patch.object(sys, 'argv', fake_sys.argv):
        fake_sys.argv = ['--version']
        parser, opts, _ = parseOpts()
        assert opts.version == True
    with patch.object(sys, 'argv', fake_sys.argv):
        fake_sys.argv = ['--verbose']
        parser, opts, _ = parseOpts()
        assert opts.verbose == True
    with patch.object(sys, 'argv', fake_sys.argv):
        fake_sys.arg

# Generated at 2022-06-14 17:55:01.929429
# Unit test for function parseOpts
def test_parseOpts():
    opts = optparse.Values()
    opts.username = None
    opts.password = None
    opts.usenetrc = False
    opts.verbose = False
    opts.quiet = False
    opts.no_warnings = False
    opts.forceurl = False
    opts.forcetitle = False
    opts.forceid = False
    opts.forcethumbnail = False
    opts.forcedescription = False
    opts.simulate = False
    opts.skip_download = False
    opts.format = None
    opts.listformats = False
    opts.outtmpl = '%(id)s'
    opts.autonumber_size = None
    opts.autonumber_start = 1
    opts.restrictfilen

# Generated at 2022-06-14 17:55:12.842006
# Unit test for function parseOpts
def test_parseOpts():
    def _do_test(args, exp_opts):
        class _FakeOption(object):
            def __getattr__(self, attr):
                return None
        exp_opts = {k if k != 'usenetrc' else 'use_netrc': v for k, v in exp_opts.items()}
        exp_opts = _FakeOption() if exp_opts is None else _FakeOption(**exp_opts)
        _, opts, _ = parseOpts(args)
        eq_(opts.__dict__, exp_opts.__dict__)
    _do_test(['--no-check-certificate'],
        {'nocheckcertificate': True})
    _do_test(['-r', '1'],
        {'ratelimit': '1'})


# Generated at 2022-06-14 17:55:16.013110
# Unit test for function parseOpts
def test_parseOpts():
    '''
    >>> assert parseOpts
    >>> parser, opts, args = parseOpts(['-i', '--verbose', '--dump-intermediate-pages'])
    >>> opts.verbose
    True
    >>> opts.dump_intermediate_pages
    True
    '''



# Generated at 2022-06-14 17:55:26.086513
# Unit test for function parseOpts
def test_parseOpts():
    def _test_parseOpts(overrideArguments, expected):
        (parser, opts, args) = parseOpts(overrideArguments)
        assert len(args) == len(expected), '%s %s' % (args, expected)
        for index, value in enumerate(args):
            assert value == expected[index], '%s %s' % (value, expected[index])

    _test_parseOpts(None, ['https://www.youtube.com/watch?v=BaW_jenozKc'])
    _test_parseOpts(['https://www.youtube.com/watch?v=BaW_jenozKc'],
        ['https://www.youtube.com/watch?v=BaW_jenozKc'])

# Generated at 2022-06-14 17:55:28.679785
# Unit test for function parseOpts
def test_parseOpts():
    import doctest
    doctest.run_docstring_examples(parseOpts, globals())
# parseOpts end


# Generated at 2022-06-14 17:55:40.986032
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-v'])
    assert opts.verbose == True
    assert opts.outtmpl == '%(id)s'
    parser, opts, args = parseOpts(['-i', '-v'])
    assert opts.verbose == False
    assert opts.ignoreerrors == True
    parser, opts, args = parseOpts(['--ignore-errors'])
    assert opts.ignoreerrors == True
    parser, opts, args = parseOpts(['-a', '-', '-v'])
    assert opts.verbose == True
    assert opts.batchfile == '-'
    parser, opts, args = parseOpts(['--batch-file', '-'])
    assert opts.batchfile == '-'
    parser,

# Generated at 2022-06-14 17:56:58.409447
# Unit test for function parseOpts
def test_parseOpts():
    # Test for --no-check-certificate option
    try:
        _, opts, args = parseOpts()
        assert opts.nocheckcertificate
    except OptionError:
        assert False
    else:
        assert True
# End of unit test for function parseOpts



# Generated at 2022-06-14 17:57:06.910683
# Unit test for function parseOpts
def test_parseOpts():
    if hasattr(sys, 'frozen'):
        return
    from sys import path
    from os.path import dirname
    if not isinstance(path[0], compat_str):
        return
    path[0] = dirname(path[0]).encode(preferredencoding())
    if path[0].decode(preferredencoding()).endswith('.zip'):
        path[0] = dirname(path[0])

    def parse(args):
        parser, opts, args = parseOpts(args)

# Generated at 2022-06-14 17:57:15.510735
# Unit test for function parseOpts
def test_parseOpts():
    opts, args = parseOpts([
        '--proxy=proxy.server', '-o', 'myvideo.flv',
        'http://www.youtube.com/watch?v=BaW_jenozKc'])
    assert opts.format == None
    assert opts.proxy == 'proxy.server'
    assert opts.outtmpl == 'myvideo.flv'
    assert args == ['http://www.youtube.com/watch?v=BaW_jenozKc']
    opts, args = parseOpts([
        '-f', '34/35/18',
        'http://www.youtube.com/watch?v=BaW_jenozKc'])
    assert opts.format == ['34', '35', '18']
    assert opts.proxy == None
    assert opts

# Generated at 2022-06-14 17:57:25.681923
# Unit test for function parseOpts
def test_parseOpts():
    from collections import namedtuple

    import six
    from six.moves.urllib.parse import parse_qsl

    def parse_qs_bytes(qs):
        if six.PY2 and isinstance(qs, six.text_type):
            qs = qs.encode('ascii')
        return parse_qsl(qs, keep_blank_values=True)

    Option = namedtuple('Option', ['short_name', 'long_name', 'dest', 'default', 'choices', 'type'])

    def check_option(name, value, option):
        parser, options, _ = parseOpts([], overrideArguments=[name])
        if (value is None) == (getattr(options, option.dest) is None):
            return

# Generated at 2022-06-14 17:57:37.482364
# Unit test for function parseOpts
def test_parseOpts():
    if sys.version_info < (2, 7, 3):
        raise unittest.SkipTest('https://github.com/rg3/youtube-dl/issues/6115')

    def parse(args, overrideArguments=None):
        parser, opts, args = parseOpts(overrideArguments=overrideArguments)
        opts.__dict__.update(dict(args=args))
        return parser, opts, args

    def assertEqual(opts1, opts2):
        assert isinstance(opts1, Namespace)
        assert isinstance(opts2, Namespace)
        od1 = opts1.__dict__
        od2 = opts2.__dict__

# Generated at 2022-06-14 17:57:41.460124
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts('-F 22 https://www.youtube.com/watch?v=BaW_jenozKc'.split())
    assert opts.format == '22', opts.format
    assert opts.username is None, opts.username


# Generated at 2022-06-14 17:57:47.596614
# Unit test for function parseOpts
def test_parseOpts():
    old_argv = sys.argv
    sys.argv = ['yt-dl']
    try:
        parser, opts, args = parseOpts()
    finally:
        sys.argv = old_argv

    assert isinstance(parser, optparse.OptionParser)
    assert isinstance(opts, optparse.Values)
    assert isinstance(args, list)


# Generated at 2022-06-14 17:57:49.599923
# Unit test for function parseOpts
def test_parseOpts():
    """Generate a dummy opts and args"""
    parser, opts, args = parseOpts()
    return opts, args


# Generated at 2022-06-14 17:57:59.620666
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-i', 'MyLogin', '-p', 'MyPassword', '-u', 'MyUsername', '-f', 'best', 'https://www.youtube.com/watch?v=BaW_jenozKc'])
    assert opts.username == 'MyUsername'
    assert opts.password == 'MyPassword'
    assert opts.login_pass == 'MyLogin'
    assert opts.format == 'best'
    assert args == ['https://www.youtube.com/watch?v=BaW_jenozKc']
    
    parser, opts, args = parseOpts(['-F', 'https://www.youtube.com/watch?v=BaW_jenozKc'])
    assert opts.format == 'best'