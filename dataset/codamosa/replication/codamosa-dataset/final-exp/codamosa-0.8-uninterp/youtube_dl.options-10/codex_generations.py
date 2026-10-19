

# Generated at 2022-06-14 17:48:37.700167
# Unit test for function parseOpts
def test_parseOpts():
    opts = parseOpts([])
    assert type(opts) == tuple
    assert len(opts) == 3
    assert all(type(o) == optparse.OptionParser for o in opts)

    opts = parseOpts(['--version'])
    assert type(opts) == tuple
    assert len(opts) == 3
    assert opts[0].get_option('-v')
# End unit test

# begin login info filter function

# Generated at 2022-06-14 17:48:45.628998
# Unit test for function parseOpts
def test_parseOpts():
    from nose.tools import assert_equal
    from collections import namedtuple
    Test = namedtuple('Test', ['argv', 'expected_opts', 'expected_args'])

# Generated at 2022-06-14 17:48:58.762830
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts()
    assert isinstance(opts, optparse.Values)
    assert opts.verbose == False
    assert opts.quiet == False
    assert opts.dump_user_agent == False
    assert opts.list_extractors == False
    assert opts.dump_intermediate_pages == False
    assert opts.write_pages == False
    assert opts.print_traffic == False
    assert opts.simulate == False
    assert opts.skip_download == False
    assert opts.format == None
    assert opts.format_limit == None
    assert opts.listformats == False
    assert opts.merge_output_format == None
    assert opts.outtmpl == None
    assert opts.outtmpl_na_placeholder

# Generated at 2022-06-14 17:49:06.707450
# Unit test for function parseOpts
def test_parseOpts():
    args = ['--download-archive', '/tmp/blah.txt', '-v', 'http://www.youtube.com/watch?v=BaW_jenozKc']
    parser, opts, args = parseOpts(args)
    assert opts.download_archive == '/tmp/blah.txt'
    assert opts.verbose

    # Loading user defaults
    args = ['-i', 'http://www.youtube.com/watch?v=BaW_jenozKc']
    parser, opts, args = parseOpts(args)
    assert opts.format == 'best'

    # Loading system defaults
    args = ['-i', 'http://www.youtube.com/watch?v=BaW_jenozKc']
    parser.set_defaults(format='worst')
    parser, opts,

# Generated at 2022-06-14 17:49:12.280206
# Unit test for function parseOpts
def test_parseOpts():
    from io import StringIO

    class FakeFile(StringIO):
        """
        A StringIO that supports fileno()
        """
        def fileno(self):
            return -1

    out = FakeFile()
    sys.stdout = out

    parser, opts, args = parseOpts(['--default-search', 'gvsearch'])
    assert opts.default_search == 'gvsearch'
    assert '--default-search' in out.getvalue()

    parser, opts, args = parseOpts(['--no-color'])
    assert opts.no_color

    parser, opts, args = parseOpts(['-4'])
    assert opts.prefer_ipv4
    assert opts.nopart


# Generated at 2022-06-14 17:49:17.819358
# Unit test for function parseOpts
def test_parseOpts():
    error = 0

    try:
        parser, opts, args = parseOpts(['-h'])
        print('[PASS] Parse -h without error.')
    except SystemExit as e:
        error = e.code

    if error == 0:
        print('[PASS] Parse -h without error.')
    else:
        print('[FAIL] Parse -h meet error: %d' % error)

    error = 0
    try:
        parser, opts, args = parseOpts(['--help'])
        print('[PASS] Parse --help without error.')
    except SystemExit as e:
        error = e.code

    if error == 0:
        print('[PASS] Parse --help without error.')

# Generated at 2022-06-14 17:49:25.801221
# Unit test for function parseOpts
def test_parseOpts():
    try:
        parser, opts, args = parseOpts(overrideArguments=['-U', '-u', 'username', '-p', 'password', 'https://www.youtube.com/watch?v=BaW_jenozKc'])
        assert opts.usenetrc == True
        assert opts.username == 'username'
        assert opts.password == 'password'
    except SystemExit as e:
        write_string('[error] ' + str(e) + '\n')
        return
    assert True

# Command line argument processing functions

# Generated at 2022-06-14 17:49:32.518152
# Unit test for function parseOpts
def test_parseOpts():
    from tempfile import mkstemp
    _, config_filename = mkstemp(text=True)

# Generated at 2022-06-14 17:49:42.482126
# Unit test for function parseOpts
def test_parseOpts():
    from .utils import calc_expected_size
    from .extractor import gen_extractors
    m_extractors = gen_extractors()
    m_parser, m_opts, m_args = parseOpts(overrideArguments=['kvGG7W4g6S4', '-f', '34/35/43/22', '-w', '--no-part', '-o', 'f.%(format)s.%(ext)s', '-k', '--no-post-overwrites', '--ignore-config'])
    assert m_opts.simulate == False
    assert m_opts.skip_download == False
    assert m_opts.quiet == False
    assert m_opts.format == ['34/35/43/22']
    assert m_opts.write

# Generated at 2022-06-14 17:49:47.684188
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-i', '--username', 'foo'])

    assert opts.usenetrc is True, 'Expected usenetrc=True'
    assert opts.username == 'foo', 'Expected username=foo'
    assert args == [], 'Expected args=[]'

    # Opaque arguments
    parser, opts, args = parseOpts(['--extract-audio', '--audio-format', 'mp3', '-4', '-b', '128K', '--embed-thumbnail'])

    assert opts.extractaudio == True, 'Expected extractaudio=True'
    assert opts.audioformat == 'mp3', 'Expected audioformat=mp3'
    assert opts.audioquality == '128K', 'Expected audioquality=128K'

# Generated at 2022-06-14 17:50:12.329240
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-v']);
    assert opts.verbose == True
    parser, opts, args = parseOpts(['--verbose']);
    assert opts.verbose == True
    parser, opts, args = parseOpts(['-h']);
    assert opts.help == True
    parser, opts, args = parseOpts(['--help']);
    assert opts.help == True
    parser, opts, args = parseOpts(['--version']);
    assert opts.version == True
    parser, opts, args = parseOpts(['--ignore-config']);
    assert opts.ignoreconfig == True
    parser, opts, args = parseOpts(['--no-check-certificate']);
    assert opts.nocheck

# Generated at 2022-06-14 17:50:13.678551
# Unit test for function parseOpts
def test_parseOpts():
    assert parseOpts() is not None


# Generated at 2022-06-14 17:50:14.790744
# Unit test for function parseOpts
def test_parseOpts():
    pass

# parseOpts()


# Generated at 2022-06-14 17:50:23.581472
# Unit test for function parseOpts
def test_parseOpts():
    import sys
    sys.argv = ['youtube-dl']
    assert parseOpts()[0].format_help() == parseOpts(['--help'])[0].format_help()
    assert parseOpts(['--version'])[0].version == __version__
    assert parseOpts(['-U', 'test'])[1].updatetime
    assert parseOpts(['--no-updates'])[1].updatetime == False
    assert parseOpts(['--proxy', '1.1.1.1:8080'])[1].proxy == '1.1.1.1:8080'
    assert parseOpts(['--no-check-certificate'])[1].nocheckcertificate == True
    assert parseOpts(['--user-agent', 'test'])[1].user

# Generated at 2022-06-14 17:50:36.922649
# Unit test for function parseOpts
def test_parseOpts():
    from sys import argv
    argv_saved = argv

# Generated at 2022-06-14 17:50:42.694054
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, _ = parseOpts(['-q', '--extract-audio', '--audio-format', 'mp3', 'plOpKm4A4i8&amp;feature=related', '--verbose'])
    assert opts.quiet
    assert opts.extractaudio
    assert opts.audioformat == 'mp3'
    assert parser.get_usage()
    assert parser.get_prog_name()


# Generated at 2022-06-14 17:50:55.425725
# Unit test for function parseOpts
def test_parseOpts():
    import tempfile

# Generated at 2022-06-14 17:51:05.532564
# Unit test for function parseOpts
def test_parseOpts():
    from youtube_dl.utils import DateRange
    from datetime import date, datetime
    # Check the basic command-line options
    parser, opts, args = parseOpts([])
    assert opts.verbose is False
    assert opts.quiet is False
    assert opts.simulate is False
    assert opts.format is None
    assert opts.outtmpl is None
    assert opts.ignoreerrors is False
    assert opts.forceurl is False
    assert opts.forceratelimit is False
    assert opts.noplaylist is False
    assert opts.playlistreverse is False
    assert opts.playliststart is 1
    assert opts.playlistend is -1
    assert opts.matchtitle is None
    assert opts.rejecttitle is None
    assert opts.max_

# Generated at 2022-06-14 17:51:17.208362
# Unit test for function parseOpts
def test_parseOpts():
    # Very simple unit test for parseOpts
    # More comprehensive tests are in test.py
    #
    # parseOpts can be tested either with or without
    # the command line parameters. Since this is a
    # convenience function, not testing it with
    # command line parameters is fine.
    parser, opts, args = parseOpts()

    assert opts.verbose is False
    assert opts.quiet is False
    assert opts.no_warnings is True

    parser, opts, args = parseOpts(['-v'])
    assert opts.verbose is True
    assert opts.quiet is False
    assert opts.no_warnings is True

    parser, opts, args = parseOpts(['-q'])
    assert opts.verbose is False
    assert opts.quiet is True


# Generated at 2022-06-14 17:51:21.233428
# Unit test for function parseOpts
def test_parseOpts():
    opts, args = parseOpts(['-i', '-o', 'test'])
    if __name__ == '__main__':
        print(opts.ignoreerrors, args)


# Generated at 2022-06-14 17:51:47.737364
# Unit test for function parseOpts
def test_parseOpts():
    optionString = ['-i','-u','tsai.hanhan@gmail.com','-p','qwertyuiop0123456789','-v']
    parser, opts, args = parseOpts(optionString)
    assert opts.username == 'tsai.hanhan@gmail.com'
    assert opts.password == 'qwertyuiop0123456789'
    assert opts.verbose == True

    optionString = ['-i','-u','tsai.hanhan@gmail.com','-p','qwertyuiop0123456789']
    parser, opts, args = parseOpts(optionString)
    assert opts.username == 'tsai.hanhan@gmail.com'
    assert opts.password == 'qwertyuiop0123456789'
    assert opts

# Generated at 2022-06-14 17:51:55.468758
# Unit test for function parseOpts
def test_parseOpts():
    def test(args, expected_error=0, expected_warning=0, expected_result=None, override_arguments=None):
        if override_arguments is None:
            override_arguments = args

        parser, opts, args = parseOpts(override_arguments=override_arguments)
        error_count, warning_count = extract_count(opts)

        assert error_count == expected_error
        assert warning_count == expected_warning

        if expected_result is not None:
            for k, v in expected_result.items():
                assert hasattr(opts, k)
                assert getattr(opts, k) == v

        return opts, args

    # No option

# Generated at 2022-06-14 17:52:08.103683
# Unit test for function parseOpts
def test_parseOpts():
    # TODO: move these tests to a separate file
    def test(args, want_opts, want_leftover, want_errcode = 0, override_config = False):
        # Retrieve opts and leftover

        old_stdout = sys.stdout
        old_stderr = sys.stderr
        sys.stdout = io.StringIO()
        sys.stderr = sys.stdout

        if override_config:
            opts, leftover = parseOpts(overrideArguments = args)
        else:
            opts, leftover = parseOpts(args)

        sys.stdout = old_stdout
        sys.stderr = old_stderr

        # Test opts

# Generated at 2022-06-14 17:52:15.523220
# Unit test for function parseOpts
def test_parseOpts():
    from .utils import group_dict
    from .compat import str, compat_shlex_split

    def check_parseOpts(args_str, expected_opts_dict, expected_args):
        parser, actual_opts, actual_args = parseOpts(
            compat_shlex_split(args_str))
        assert group_dict(actual_opts) == expected_opts_dict
        assert actual_args == expected_args


# Generated at 2022-06-14 17:52:16.969974
# Unit test for function parseOpts
def test_parseOpts():
    import doctest
    doctest.testmod()



# Generated at 2022-06-14 17:52:23.612087
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-i', '--get-title', '-v', 'http://www.youtube.com/watch?v=BaW_jenozKc'])
    assert parser
    assert opts
    assert args
    assert opts.verbose
    assert opts.usenetrc
    assert opts.gettitle



# Generated at 2022-06-14 17:52:32.762970
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts([])
    assert hasattr(opts, 'version')
    assert hasattr(opts, 'max_sleep')
    assert hasattr(opts, 'max_sleep')
    assert hasattr(opts, 'max_tries')
    assert hasattr(opts, 'min_sleep')
    assert hasattr(opts, 'retries')
    assert hasattr(opts, 'progress_with_newline')
    assert hasattr(opts, 'dump_intermediate_pages')
    assert hasattr(opts, 'write_pages')
    assert hasattr(opts, 'write_info_json')
    assert hasattr(opts, 'write_description')
    assert hasattr(opts, 'write_annotations')

# Generated at 2022-06-14 17:52:34.927348
# Unit test for function parseOpts
def test_parseOpts():
    opts, args = parseOpts()


# Generated at 2022-06-14 17:52:38.421720
# Unit test for function parseOpts
def test_parseOpts():
    '''
    unit test for parseOpts()
    '''
    #import youtube_dl
    #youtube_dl.main()
    #print('hello')
    #parseOpts()
    pass



# Generated at 2022-06-14 17:52:46.299865
# Unit test for function parseOpts
def test_parseOpts():
    try:
        import __main__
        __main__.args = sys.argv[1:]
    except ImportError:
        sys.stderr.write('Error: Please run unit tests with python2 -m unittest youtube_dl.YoutubeDL\n')
        sys.exit(1)


# Generated at 2022-06-14 17:53:23.971704
# Unit test for function parseOpts

# Generated at 2022-06-14 17:53:35.348570
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-F', 'http://www.youtube.com/watch?v=BaW_jenozKc'])
    assert opts.usenetrc is False
    assert opts.username is None
    assert opts.password is None
    assert opts.video_password is None

    parser, opts, args = parseOpts(['--username', 'foo', '--password', 'bar',
                                    '--video-password', 'baz',
                                    'http://www.youtube.com/watch?v=BaW_jenozKc'])
    assert opts.usenetrc is False
    assert opts.username == 'foo'
    assert opts.password == 'bar'
    assert opts.video_password == 'baz'

    parser, opts,

# Generated at 2022-06-14 17:53:47.563505
# Unit test for function parseOpts
def test_parseOpts():
    opts = parseOpts([__file__, '-v'])[1]
    assert opts.verbose
    opts = parseOpts([__file__, '--ignore-config'])[1]
    assert opts.ignore_config
    opts = parseOpts([__file__, '--config-location=/path/to/config'])[1]
    assert opts.config_location == '/path/to/config'
    opts = parseOpts([__file__, '-a', 'test.txt'])[1]
    assert opts.batchfile == 'test.txt'
    opts = parseOpts([__file__, '--batch-file=-'])[1]
    assert opts.batchfile == '-'

# Generated at 2022-06-14 17:53:57.691837
# Unit test for function parseOpts
def test_parseOpts():
    from youtube_dl.extractor import get_info_extractor
    from youtube_dl.version import __version__
    import tempfile
    import shutil
    import os

    def _count_supported(ydl):
        return len(ydl._ies)

    # Parsing config
    with tempfile.NamedTemporaryFile(mode='w+') as cf:
        cf.write('-i --download-archive archive -o "%%(title)s" -f bestvideo[height<=?720]+bestaudio/best')
        cf.flush()

        parser, opts, args = parseOpts(['-c', cf.name, 'http://youtube.com/watch?v=BaW_jenozKc'])
        ydl = YoutubeDL(opts)
        assert ydl.params['simulate']
        assert y

# Generated at 2022-06-14 17:54:02.179282
# Unit test for function parseOpts
def test_parseOpts():
    arguments = ['--get-id', '--max-filesize', '20m']
    parser, opts, _ = parseOpts(arguments)
    assert opts.getid is True
    assert opts.max_filesize == 20 * 1000 * 1000



# Generated at 2022-06-14 17:54:09.804666
# Unit test for function parseOpts
def test_parseOpts():
    sys.argv = [sys.argv[0], 'http://www.youtube.com/watch?v=BaW_jenozKc']
    parser, opts, args = parseOpts()
    assert(opts.username is None)
    assert(opts.password is None)


# Generated at 2022-06-14 17:54:11.595781
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-v'])
    assert opts.verbose
test_parseOpts()


# Generated at 2022-06-14 17:54:17.033210
# Unit test for function parseOpts
def test_parseOpts():
    import sys
    import doctest
    doctest.testmod(sys.modules[__name__])

parseOpts.__test__ = False

if __name__ == '__main__':
    test_parseOpts()

# Generated at 2022-06-14 17:54:30.443082
# Unit test for function parseOpts
def test_parseOpts():
    from .utils import preferredencoding

    from .compat import (
        compat_expanduser, compat_configparser, compat_str,
        compat_str_str)

    parser, opts, args = _parseOpts()

    # General tests
    assert parser
    assert opts
    assert args
    assert isinstance(opts.username, compat_str_str)
    assert isinstance(opts.password, compat_str_str)
    assert isinstance(opts.twofactor, compat_str_str)
    assert isinstance(opts.videopassword, compat_str_str)
    assert isinstance(opts.ap_username, compat_str_str)
    assert isinstance(opts.ap_password, compat_str_str)

# Generated at 2022-06-14 17:54:35.963996
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts()
    assert isinstance(parser, optparse.OptionParser)
    assert isinstance(opts, optparse.Values)
    assert isinstance(args, list)
    assert 'youtube-dl.py' not in args
    # Simple test for parseOpts
    def test_parseOpts():
        parser, opts, args = parseOpts()
        assert isinstance(parser, optparse.OptionParser)
        assert isinstance(opts, optparse.Values)
        assert isinstance(args, list)
        assert 'youtube-dl.py' not in args
        # Test --version
        with captureStdout() as stdout:
            parseOpts(['--version'])
        assert stdout_endswith('youtube-dl %s\n' % __version__)
       

# Generated at 2022-06-14 17:55:33.274918
# Unit test for function parseOpts
def test_parseOpts():
    import doctest
    doctest.testmod(verbose=False)
# Unit test execution
if __name__ == "__main__":
    test_parseOpts()

"""Entry Point"""


# Generated at 2022-06-14 17:55:37.631172
# Unit test for function parseOpts
def test_parseOpts():
    try:
        _, _ = parseOpts(['-U', 'unituser', '-P', 'unitpass', '-w', 'www.youtube.com', '--get-title', 'unit_test'])
    except (TypeError, SystemExit):
        pass
    else:
        assert False



# Generated at 2022-06-14 17:55:48.273242
# Unit test for function parseOpts
def test_parseOpts():
    """Test the default behavior of the option parser."""
    parser, opts, _ = parseOpts([])

    assert opts.username is None

    assert opts.password is None

    assert opts.usenetrc is False

    assert opts.verbose is False

    assert opts.quiet is False

    assert opts.no_warnings is False

    assert opts.forceurl is False

    assert opts.forcethumbnail is False

    assert opts.forcetitle is False

    assert opts.forceid is False

    assert opts.forceduration is False

    assert opts.forcefilename is False

    assert opts.forcejson is False

    assert opts.dump_single_json is False


# Generated at 2022-06-14 17:55:57.504594
# Unit test for function parseOpts
def test_parseOpts():
    import mock
    from ydl.argparser import parseOpts
    from ydl.const import PTS_VER

    for param in (['ytuser:blahblah'], ['-u', 'ytuser:blahblah'], ['--username', 'ytuser:blahblah']):
        with mock.patch('ydl.argparser.getpass') as mock_getpass:
            mock_getpass.return_value = 'blahblah'
            parseOpts(param)
            mock_getpass.assert_called_with('YouTube account password: ', '')

    for param in (['--username', 'blahblah'], ['-u', 'blahblah']):
        with mock.patch('ydl.argparser.getpass') as mock_getpass:
            parseOpts(param)
            mock_

# Generated at 2022-06-14 17:56:08.155858
# Unit test for function parseOpts
def test_parseOpts():
    orig_environ = os.environ.copy()

    os.environ.clear()
    os.environ['LANG'] = 'C'
    os.environ['HOME'] = os.path.realpath('.')
    try:
        parser, opts, args = parseOpts(['--usenetrc', '-u', 'user', '-p', 'pass', '-q', 'rutube.ru/video/id'])
    finally:
        os.environ.clear()
        os.environ.update(orig_environ)

    assert opts.usenetrc is True
    assert opts.username == 'user'
    assert opts.password == 'pass'
    assert opts.quiet is True
    assert args == ['rutube.ru/video/id']


# Generated at 2022-06-14 17:56:10.540122
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts()

    # TODO: assert opts and args
# parseOpts() is used in main()


# Generated at 2022-06-14 17:56:18.735018
# Unit test for function parseOpts
def test_parseOpts():
    def argv(l):
        return [a.encode(preferredencoding()) if isinstance(a, str) else a for a in l]


# Generated at 2022-06-14 17:56:31.469347
# Unit test for function parseOpts
def test_parseOpts():
    from sys import argv, executable

    opts, args = parseOpts(['--call-home'])
    assert opts.call_home

    opts, args = parseOpts(['--username', '--password', '--video-password', '--ap-username', '--ap-password'])
    assert opts.username is None
    assert opts.password is None
    assert opts.videopassword is None
    assert opts.ap_username is None
    assert opts.ap_password is None

    opts, args = parseOpts(['--no-call-home'])
    assert not opts.call_home

    argv = ['--username', 'user']
    opts, args = parseOpts(argv)
    assert opts.username == 'user'

# Generated at 2022-06-14 17:56:42.373211
# Unit test for function parseOpts
def test_parseOpts():
    def assertOpts(opts, conf, args, override=None):
        _args = list(conf) + args
        if override:
            _args += override
        parser, _opts, _args = parseOpts(_args)
        opts.update(conf)
        if override:
            opts.update(override)
        for attr, value in opts.items():
            assert getattr(_opts, attr) == value, (attr, getattr(_opts, attr))
        assert _args == args

    system_conf = ['--username', 'system', '--password', 'system', '--verbose']
    user_conf = ['--username', 'user', '--password', 'user', '--output', '/tmp/%(title)s.%(ext)s']

# Generated at 2022-06-14 17:56:53.359614
# Unit test for function parseOpts
def test_parseOpts():
    from youtube_dl.utils import DateRange

    # no stack trace on test fail
    old_stderr = sys.stderr
    sys.stderr = open(os.devnull, 'w')

    # optparse isn't tested as it is deprecated in Python 2.7 and removed in Python 3