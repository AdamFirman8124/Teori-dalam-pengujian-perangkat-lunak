

# Generated at 2022-06-14 17:48:57.482255
# Unit test for function parseOpts
def test_parseOpts():
    from ytdl.YoutubeDL import YoutubeDL
    ydl = YoutubeDL()
    ydl_opts = ydl.params

    for opt, expected_val in ydl_opts.items():
        config_args = ['--%s' % opt]

        if expected_val is True:
            parser, opts, _ = parseOpts(config_args)
            assert getattr(opts, opt) is True
        elif expected_val is False:
            parser, opts, _ = parseOpts(config_args)
            assert getattr(opts, opt) is False
        else:
            config_args.append(str(expected_val))
            parser, opts, _ = parseOpts(config_args)
            assert getattr(opts, opt) == expected_val



# Generated at 2022-06-14 17:49:04.161617
# Unit test for function parseOpts
def test_parseOpts():
    class Object(object): pass
    args = []
    for i in range(0, len(sys.argv)):
        t = Object()
        t.name = sys.argv[i]
        if i < len(sys.argv)-1:
            t.value = sys.argv[i+1]
        args.append(t)

    parser, opts, _ = parseOpts(args)
    assert opts.usenetrc != True

test_parseOpts()


# Generated at 2022-06-14 17:49:07.250791
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts()
    assert(opts.username == None)
# test_parseOpts()


# Generated at 2022-06-14 17:49:17.178789
# Unit test for function parseOpts
def test_parseOpts():
    # Test with complete options
    base_args = ['--verbose', '--proxy', '1.2.3.4:3128',
                 '--socket-timeout', '10', '--outtmpl', '%(id)s.%(ext)s']
    parser, opts, _ = parseOpts(base_args)
    assert opts.proxy == '1.2.3.4:3128'
    assert opts.socket_timeout == 10
    assert opts.outtmpl == '%(id)s.%(ext)s'

    # Test with a missing argument for --proxy
    incomplete_args = ['--verbose', '--proxy']
    parser, opts, _ = parseOpts(incomplete_args)
    assert opts.proxy is None

    # Test with --version
    version_args

# Generated at 2022-06-14 17:49:19.304391
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-i'])
    assert opts.ignoreerrors is True


# Generated at 2022-06-14 17:49:29.020904
# Unit test for function parseOpts
def test_parseOpts():
    from .utils import encodeFilename
    from .extractor import gen_extractors

    parser, opts, args = parseOpts(['-v'])
    assert opts.verbose

    parser, opts, args = parseOpts(['--verbose'])
    assert opts.verbose

    parser, opts, args = parseOpts(['--output', '%(title)s-%(id)s.%(ext)s'])
    assert opts.outtmpl == encodeFilename('%(title)s-%(id)s.%(ext)s')

    # Test --ignore-config option
    parser, opts, args = parseOpts(['--ignore-config'])
    assert not opts.verbose

    # Test --ignore-config option
    parser, opts, args = parseOpts

# Generated at 2022-06-14 17:49:30.261316
# Unit test for function parseOpts
def test_parseOpts():
    import doctest
    ret = doctest.testmod()
    if ret.failed:
        sys.exit(ret.failed)


# Warnings

# Generated at 2022-06-14 17:49:40.813446
# Unit test for function parseOpts
def test_parseOpts():
    # No output
    assert(parseOpts([])[1].verbose==False)
    # Verbose output
    assert(parseOpts(['-v'])[1].verbose==True)
    # Quiet output
    assert(parseOpts(['-q'])[1].quiet==True)
    assert(parseOpts(['--quiet'])[1].quiet==True)
    # Verbose, quiet, and "noprogress" all off
    assert(parseOpts(['-v', '-q', '--no-progress'])[1].verbose==False)
    assert(parseOpts(['-v', '-q', '--no-progress'])[1].quiet==False)

# Generated at 2022-06-14 17:49:47.719735
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts([
        '-i', 'https://www.youtube.com/watch?v=BaW_jenozKc',
        '--get-id',
        '-o', '%(autonumber)s-%(id)s-%(upload_date)s-%(title)s.%(ext)s',
        '--autonumber-size=4',
        '--max-downloads=4',
        '--prefer-free-formats',
        '-f', 'bestvideo[height<=?1080]+bestaudio/best',
        '--retries', '10',
        '--sleep-interval', '5',
        '-v',
    ])
    assert parser
    assert opts
    assert args == []

    assert opts.noplay

# Generated at 2022-06-14 17:49:54.034788
# Unit test for function parseOpts

# Generated at 2022-06-14 17:50:20.385679
# Unit test for function parseOpts
def test_parseOpts():
    print(parseOpts('--help')[0])
    print(parseOpts('--recode-video mkv')[0])
    print(parseOpts('--no-mtime')[0])
    print(parseOpts('--call-home')[0])
    print(parseOpts('--no-call-home')[0])
    print(parseOpts('-o "/mnt/ytdl/%(uploader)s/%(title)s (%(upload_date)s)%(ext)s" --autonumber-size 4 --embed-thumbnail --metadata-from-title "(?P<artist>.+?) - (?P<title>.+)"')[0])
    print(parseOpts('--extract-audio --audio-format best')[0])

# Generated at 2022-06-14 17:50:22.653288
# Unit test for function parseOpts
def test_parseOpts():
    from youtube_dl.YoutubeDL import YoutubeDL
    YoutubeDL(['--username', 'foouser', '--password', 'foopass', '--version'])

# Retrieve info for URLs

# Generated at 2022-06-14 17:50:34.583040
# Unit test for function parseOpts
def test_parseOpts():
    from sys import argv
    # The options can be set by command line arguments as well
    # Any argument that is not a youtube-dl specific argument (i.e.
    # does not start with '--') is considered to be a URL to be
    # downloaded
    # Below command line arguments are used to test the function
    argv = ['--username', 'arun', '--password', 'pwd', '--verbose']
    assert(parseOpts()[2] == ['--username', 'arun', '--password', 'pwd', '--verbose'])
    argv = []


# Returns the preferred encoding, which should be used to
# decode command line arguments.

# Generated at 2022-06-14 17:50:48.053157
# Unit test for function parseOpts
def test_parseOpts():
    test_argv = ['--username=foo', '--password=bar', '--get-url', '--get-title', 'http://www.youtube.com/watch?v=BaW_jenozKc']
    parser, opts, args = parseOpts(test_argv)
    assert opts.username == 'foo' and opts.password == 'bar'
    assert opts.usenetrc is False and opts.noplaylist is True and opts.geturl is True and opts.gettitle is True and opts.getid is False and opts.getthumbnail is False and opts.getdescription is False and opts.getfilename is False and opts.get_format is False

# Generated at 2022-06-14 17:51:00.010735
# Unit test for function parseOpts
def test_parseOpts():
    from . import __main__

# Generated at 2022-06-14 17:51:10.016783
# Unit test for function parseOpts
def test_parseOpts():
    from tempfile import NamedTemporaryFile
    from urllib import quote_plus

    def test(args, result):
        try:
            _, opts, _ = parseOpts(args)
            for key, value in result.items():
                assert getattr(opts, key) == value
        except Exception:
            print('Error while testing args %r' % args)
            raise

    # Allow to run the test even if ~ maps to a non-existing directory (--ignore-config)
    test(['--ignore-config'], {'noplaylist': False})

    # Test relative path
    test(['.'], {'noplaylist': False})

    # Test whether options work without a parameter
    test(['--no-playlist'], {'noplaylist': True})

    # Test for aliases
    test

# Generated at 2022-06-14 17:51:22.228474
# Unit test for function parseOpts
def test_parseOpts():
    with pytest.raises(SystemExit):
        parseOpts(overrideArguments=['-h'])
    with pytest.raises(SystemExit):
        parseOpts(overrideArguments=['--help'])
    with pytest.raises(SystemExit):
        parseOpts(overrideArguments=['-U'])
    with pytest.raises(SystemExit):
        parseOpts(overrideArguments=['--update'])
    with pytest.raises(SystemExit):
        parseOpts(overrideArguments=['-i'])
    with pytest.raises(SystemExit):
        parseOpts(overrideArguments=['--ignore-config'])

# Generated at 2022-06-14 17:51:28.973303
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(["-h"])
    assert parser.description == __doc__.split("\n")[0].strip()
    opts, args = parseOpts(["-h", "--username", "foo", "--password", "bar"])
    assert parser.description == __doc__.split("\n")[0].strip()
    opts, args = parseOpts(["-U", "foo", "-P", "bar", "-h"])
    assert parser.description == __doc__.split("\n")[0].strip()



# Generated at 2022-06-14 17:51:37.950945
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts([])
    assert not opts.usenetrc
    assert opts.username == ''
    assert opts.password == ''
    assert not opts.noprogress
    assert not opts.quiet
    assert opts.verbose == 0
    assert opts.outtmpl == '%(id)s.%(ext)s'
    assert opts.ignoreerrors
    assert not opts.forceurl

    parser, opts, args = parseOpts(['-v'])
    assert opts.verbose == 1
    parser, opts, args = parseOpts(['-vvvvv'])
    assert opts.verbose == 5

    parser, opts, args = parseOpts(['-q'])
    assert opts.quiet
    assert not opt

# Generated at 2022-06-14 17:51:48.954855
# Unit test for function parseOpts
def test_parseOpts():
    test_example = ['--verbose', '--username', 'test1', '--password', 'test2', '--format', 'best']
    parser, opts, args = parseOpts(overrideArguments=test_example)

    assert opts.verbose == True
    assert opts.username == 'test1'
    assert opts.password == 'test2'
    assert opts.format == 'best'
    assert args == []

    # Check hide_login_info
    test_example = ['--verbose', '--username', 'test1', '--password', 'test2', '--format', 'best']
    parser, opts, args = parseOpts(overrideArguments=test_example)
    assert opts.verbose == True
    # assert hide_login_info(test_example[1:]) ==

# Generated at 2022-06-14 17:52:09.958756
# Unit test for function parseOpts
def test_parseOpts():
    empty = parseOpts([])
    assert empty.get('outtmpl') == '%(id)s.%(ext)s'

    identifier = parseOpts(['plop'])
    assert identifier.get('outtmpl') == '%(id)s.%(ext)s'

    url = parseOpts(['https://www.youtube.com/watch?v=BaW_jenozKc'])
    assert url.get('outtmpl') == '%(id)s.%(ext)s'

    url_plus = parseOpts(['https://www.youtube.com/watch?v=BaW_jenozKc',
                          '--no-call-home'])
    assert url_plus.get('nocheckcertificate') == False


# End of parseOptions basics


# Generated at 2022-06-14 17:52:11.840930
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts()
    assert(opts and args)

# Parse the command line arguments and return them as a dictionary

# Generated at 2022-06-14 17:52:16.788474
# Unit test for function parseOpts
def test_parseOpts():
    from io import StringIO
    sys.stdout = StringIO()
    sys.argv = ['--rm-cache-dir', '--cache-dir', '/tmp/test']
    parser, opts, args = parseOpts(None)
    assert opts.rm_cachedir
    assert opts.cachedir == '/tmp/test'
    # Restore the sys.stdout to its normal value
    sys.stdout = sys.__stdout__


# Generated at 2022-06-14 17:52:28.996983
# Unit test for function parseOpts
def test_parseOpts():
    from youtube_dl.utils import encodeArgument
    from youtube_dl.YoutubeDL import YoutubeDL

    # Test with an empty argument list
    parser, opts, args = parseOpts([])
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
    assert opts.autonumber_size is None
    assert opts.autonumber_start is 1
    assert opts.dump_user_agent is False
    assert opts.dump_intermediate_

# Generated at 2022-06-14 17:52:41.889557
# Unit test for function parseOpts
def test_parseOpts():
    from sys import version_info
    from youtube_dl.utils import encodeArgument

# Generated at 2022-06-14 17:52:52.131407
# Unit test for function parseOpts
def test_parseOpts():
    _LOGGER.setLevel(logging.DEBUG)
    parser, opts, args = parseOpts()

# Generated at 2022-06-14 17:53:02.893527
# Unit test for function parseOpts
def test_parseOpts():
    import tempfile
    from os.path import join, isfile
    from .compat import compat_expanduser
    from .extractor import gen_extractors
    from .utils import std_headers

    temp_dir = tempfile.mkdtemp(prefix='youtube-dl-test-')
    std_headers['User-Agent'] += ' unitest'

    def reset_opts():
        std_headers['User-Agent'] = std_headers['User-Agent'].rstrip(' unitest')
        for ie in gen_extractors():
            ie.options = ie.IE._initialize_options()
        return

    def write_config(filename, config):
        with open(filename, 'w') as f:
            f.write(config)
        return


# Generated at 2022-06-14 17:53:13.888016
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts()


# Generated at 2022-06-14 17:53:25.633245
# Unit test for function parseOpts
def test_parseOpts():
    # You need to modify the name of the configuration file to test other errors
    parser, opts, args = parseOpts(overrideArguments = ['--config-location=test/test_files/youtube-dl.conf'])
    print(opts.username)
    print(opts.password)
    print(opts.age_limit)
    print(opts.outtmpl)
    print(opts.geturl)
    print(opts.gettitle)
    print(opts.getid)
    print(opts.getthumbnail)
    print(opts.getdescription)
    print(opts.getfilename)
    print(opts.get_format)
    print(opts.get_format_id)
    print(opts.list_formats)

# Generated at 2022-06-14 17:53:27.964996
# Unit test for function parseOpts
def test_parseOpts():
    from youtube_dl.YoutubeDL import YoutubeDL
    parser, opts, args = parseOpts()
    assert isinstance(YoutubeDL(opts), YoutubeDL)

# Generated at 2022-06-14 17:54:00.506999
# Unit test for function parseOpts
def test_parseOpts():
    """
    This function returns True if parseOpts() works as expected, else it
    returns False.
    """
    # Test 1: Test parsing with no extra options
    parser, opts, args = parseOpts([])
    if not (opts.verbose == False and opts.quiet == False and opts.simulate == False):
        print('[fail] Test 1 failed.')
        return False
    print('[ok] Test 1 succeeded.')

    # Test 2: Test parsing with all booleans set to True
    parser, opts, args = parseOpts(['-v', '-q', '-s'])
    if not (opts.verbose == True and opts.quiet == True and opts.simulate == True):
        print('[fail] Test 2 failed.')
        return False

# Generated at 2022-06-14 17:54:10.377022
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['--verbose', '-F'])
    assert opts.verbose
    assert opts.format == 'best'
    parser, opts, args = parseOpts(['--no-warnings', '--format=22/17/5/36', '-F', '-f 22'])
    assert not opts.verbose
    assert not opts.dump_user_agent
    assert opts.format == 'best'
    assert opts.listformats == [22, 17, 5, 36]
    parser, opts, args = parseOpts(['-vf', '24/18', '-f', '22/17/5/36', '--yes-playlist'])
    assert opts.format == 'best'

# Generated at 2022-06-14 17:54:19.036250
# Unit test for function parseOpts
def test_parseOpts():
    res1 = parseOpts(['-v'])[2]
    assert(res1 == [])
    res2 = parseOpts(['-o', 'test'])[2]
    assert(res2 == [])
    res3 = parseOpts(['-o', 'test', 'http://www.youtube.com/watch?v=BaW_jenozKc'])[2]
    assert(res3 == ['http://www.youtube.com/watch?v=BaW_jenozKc'])



# Generated at 2022-06-14 17:54:20.399288
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts()

# Generated at 2022-06-14 17:54:31.719979
# Unit test for function parseOpts
def test_parseOpts():
    import pprint

# Generated at 2022-06-14 17:54:43.006940
# Unit test for function parseOpts
def test_parseOpts():
    # pylint: disable=missing-docstring
    parser, opts, args = parseOpts(['--username', 'foo', '--password', 'bar', 'https://youtu.be/BaW_jenozKc'])
    assert opts.username == 'foo'
    assert opts.password == 'bar'
    assert 'https://youtu.be/BaW_jenozKc' in args

    parser, opts, args = parseOpts([])
    assert opts.username is None
    assert opts.password is None

    parser, opts, args = parseOpts(['--get-url'])
    assert opts.username is None
    assert opts.password is None
    assert opts.usenetrc
    assert args == []


# Generated at 2022-06-14 17:54:55.810416
# Unit test for function parseOpts
def test_parseOpts():
    from sys import argv, executable
    from tempfile import mkstemp

    # Expand sys.argv before calling parseOpts.
    # This achieves the same effect as parseOpts doing it internally.
    argv[1:] = _expand_paths(argv[1:])

    # Test parseOpts() with exact clone of the original function.
    parser, opts, args = compat_parseOpts()
    assert opts.default_search == 'auto'
    outtmpl_files = glob.glob(opts.outtmpl.replace('*', '*'))
    assert len(outtmpl_files) == 0

    # Test parseOpts() with function patched to use custom outtmpl.
    # This is a very simple test that just tests if the value is honored.
    # It doesn't actually test if the

# Generated at 2022-06-14 17:55:03.861971
# Unit test for function parseOpts
def test_parseOpts():
    config = ['--username', 'user', '--password', 'pwd']
    parser, opts, args = parseOpts(config)
    config = ['--username', 'user', '--password', 'pwd']
    assert config == opts.__dict__['username'] + opts.__dict__['password']

test_parseOpts()


# The following option groups are hidden and can be used from the command line
# or in a config file only.
hidden_general = optparse.OptionGroup(parser, 'General Options')
hidden_general.add_option(
    '--autoupdate', action='store_true',
    dest='autoupdate', default=False,
    help='Update to the latest version automatically and exit')

# Generated at 2022-06-14 17:55:08.836224
# Unit test for function parseOpts
def test_parseOpts():
    # Test for issue #1023
    expected = [
        'youtube-dl',
        '-c',
        'youtube-dl',
        '--format=bestvideo+bestaudio'
    ]
    parser, opts, args = parseOpts(expected)
    assert args == expected[1:]



# Generated at 2022-06-14 17:55:16.787776
# Unit test for function parseOpts
def test_parseOpts():
    terminator = '--'

    # Default parameters
    opts, args = parseOpts([terminator])
    assert(opts.usenetrc == False)
    assert(opts.username == None)
    assert(opts.password == None)
    assert(opts.verbose == False)
    assert(opts.quiet == False)
    assert(opts.format == None)
    assert(opts.outtmpl == None)
    assert(opts.batchfile == None)
    assert(args == [])
    assert(opts.simulate == False)
    assert(opts.noplaylist == False)
    assert(opts.match_filter == None)
    assert(opts.no_warnings == False)
    assert(opts.skip_download == False)

# Generated at 2022-06-14 17:55:49.515592
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['--flat-playlist', 'https://www.youtube.com/watch?v=BaW_jenozKc'])
    assert vars(opts)['flat_playlist'] == True

    parser, opts, args = parseOpts(['--ignore-errors', 'https://www.youtube.com/watch?v=BaW_jenozKc'])
    assert vars(opts)['ignoreerrors'] == True

    parser, opts, args = parseOpts(['--proxy', '127.0.0.1:8118'])
    assert vars(opts)['proxy'] == '127.0.0.1:8118'

test_parseOpts()

# Generated at 2022-06-14 17:55:56.108563
# Unit test for function parseOpts
def test_parseOpts():
    from io import StringIO
    import sys

    def _get_parser():
        sys.argv = ['youtube-dl']
        parser, _, _ = parseOpts()
        return parser

    parser = _get_parser()
    # parser.format_help() does not give consistent result
    parser.print_help()

    assert parser.has_option('-p')
    assert parser.has_option('--format')
    assert parser.has_option('--get-url')

    # Test --rm-cache-dir
    sys.argv = ['youtube-dl', '--rm-cache-dir']
    parser, opts, _ = parseOpts()
    assert opts.rm_cachedir is True

    assert len(sys.argv) == 2

    # Test --no-mtime (must be last option)


# Generated at 2022-06-14 17:56:07.423974
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(None)
    assert opts.username is None
    assert opts.password is None
    assert opts.twofactor is None
    assert opts.videopassword is None

    parser, opts, args = parseOpts(['--username', 'plop'])
    assert opts.username == 'plop'
    assert opts.password is None
    assert opts.twofactor is None
    assert opts.videopassword is None

    parser, opts, args = parseOpts(['--username', 'anonymous', '--password', 'plip'])
    assert opts.username == 'anonymous'
    assert opts.password == 'plip'
    assert opts.twofactor is None
    assert opts.videopassword

# Generated at 2022-06-14 17:56:17.290769
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-U', 'myuser', '-P', 'mypass', 'http://youtube.com/watch?v=BaW_jenozKc'])
    assert opts.username == 'myuser'
    assert opts.password == 'mypass'
    assert args == ['http://youtube.com/watch?v=BaW_jenozKc']

    parser, opts, args = parseOpts([])
    assert opts.verbose is False
    assert opts.quiet is False

    parser, opts, args = parseOpts(['-v'])
    assert opts.verbose == 1
    assert opts.quiet is False

    parser, opts, args = parseOpts(['-v', '--verbose'])
    assert opts.verbose == 2

# Generated at 2022-06-14 17:56:24.669912
# Unit test for function parseOpts
def test_parseOpts():
    opts, args = parseOpts(['-U', 'user:pass', '-i', 'www.youtube.com'])
    assert opts.username == 'user'
    assert opts.password == 'pass'
    assert opts.ignoreerrors == True

    opts, args = parseOpts(['-t', '--max-downloads=10', 'www.youtube.com', 'www.google.com'])
    assert opts.max_downloads == '10'
    assert len(args) == 2


# Generated at 2022-06-14 17:56:34.018945
# Unit test for function parseOpts
def test_parseOpts():
    # Write a sample config file to a temporary directory
    tmpdir = tempfile.mkdtemp()

# Generated at 2022-06-14 17:56:43.911017
# Unit test for function parseOpts
def test_parseOpts():
    from tempfile import mkstemp
    from random import randint
    from getpass import getuser
    from shutil import rmtree
    from os.path import exists, isdir, dirname
    from os import close, remove
    from sys import executable, stdout

    def my_rand():
        return '%x' % randint(0, 2**32)

    # Create temporary python executable
    null_fd = stdout.fileno()
    tmppath = mkstemp(suffix='.py')[1]
    tmpexe = tmppath[0:-3]
    close(null_fd)

# Generated at 2022-06-14 17:56:48.726962
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-i', '--retries', '5'])
    assert opts.usenetrc == True
    assert opts.retries == '5'
    assert args == []


# Generated at 2022-06-14 17:56:52.899843
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts()
    assert getattr(opts, 'username', None) is None
# And we patch it.
monkeypatch.setattr(cmdline.parseOpts, test_parseOpts)
from pytube import YouTube
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import os
import urllib.parse as up
import requests
import string


# Generated at 2022-06-14 17:57:03.410238
# Unit test for function parseOpts
def test_parseOpts():
    opts = OptionParser()
    opts, _ = parseOpts(opts)
    assert opts.username == "test"
    assert opts.password == "test"
    assert opts.username == "test"
    assert opts.password == "test"
    assert opts.nocheckcertificate == True
    assert opts.videopassword == "test"
    assert opts.download_archive == "test"
    assert opts.min_filesize == "1k"
    assert opts.max_filesize == "1k"
    assert opts.match_filter == "test"
    assert opts.no_color == True
    assert opts.format == "test"
    assert opts.listformats == True
    assert opts.usetitle == True

# Generated at 2022-06-14 17:58:02.523300
# Unit test for function parseOpts
def test_parseOpts():

    def test_parse(args, expected_opts, expected_args):
        parser, opts, youtube_dl_args = parseOpts(args)
        assert vars(opts) == expected_opts
        assert youtube_dl_args == expected_args
