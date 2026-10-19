

# Generated at 2022-06-14 17:48:42.683639
# Unit test for function parseOpts
def test_parseOpts():
    def parseOpts():
        parser, opts, _ = readOptions()

        opts.username = 'u'
        opts.password = 'p'
        opts.twofactor = 't'
        opts.ap_username = 'apu'
        opts.ap_password = 'app'

        if opts.verbose:
            write_string('[debug] System config: %s\n' % repr(sys.argv))
            write_string('[debug] User config: %s\n' % repr(opts))
            write_string('[debug] Custom config: %s\n' % repr(opts))
            write_string('[debug] Command-line args: %s\n' % repr(opts))

    if __name__ == '__main__':
        parseOpts()


# Generated at 2022-06-14 17:48:45.212842
# Unit test for function parseOpts
def test_parseOpts():
    from .extractor import gen_extractors
    gen_extractors()

    parser, opts, args = parseOpts(
        ['--list-extractors', '--usenetrc', '--username', 'ali', '--password', 'pass'])

    print(repr([opts, args]))


# Generated at 2022-06-14 17:48:57.751722
# Unit test for function parseOpts
def test_parseOpts():
    from io import StringIO
    from sys import version_info, stdout, stderr

    if version_info[0] == 2:
        from io import BytesIO as StringIO

    def _get_stdout(f, *args, **kwargs):
        stdout = sys.stdout
        stderr = sys.stderr
        sys.stdout = StringIO()
        sys.stderr = StringIO()
        try:
            ret = f(*args, **kwargs)
        finally:
            out = sys.stdout.getvalue()
            err = sys.stderr.getvalue()
            sys.stdout = stdout
            sys.stderr = stderr
        return ret, out, err

    # simple positional

# Generated at 2022-06-14 17:49:04.709181
# Unit test for function parseOpts
def test_parseOpts():
 print(parseOpts())
#test_parseOpts()

# BELOW: Functions for determining if a particular video is for a show that you have already downloaded.
# For example, I have already downloaded all the videos from https://www.youtube.com/user/YongBui.  I don't feel like downloading them all again, so I want to skip the videos that are already downloaded.
# The following functions will determine if a particular video is one that has already been downloaded or not.
# This function takes a URL as input, and returns a boolean value indicating if the video has been downloaded.

# Generated at 2022-06-14 17:49:10.179905
# Unit test for function parseOpts
def test_parseOpts():
    try:
        import xml.etree.ElementTree
    except ImportError:
        import elementtree.ElementTree
    class FakeOptparseOption(object):
        def __init__(self, short, long, dest=None, default=None, action=None):
            self.short = short
            self.long = long
            self.dest = dest
            self.default = default
            self.action = action
    class FakeOptparseOptionContainer(object):
        def __init__(self, title):
            self.title = title
            self.options = []
        def add_option(self, *args, **kwargs):
            self.options.append(FakeOptparseOption(*args, **kwargs))
    class FakeOptparse(object):
        def __init__(self, usage):
            self.usage = usage

# Generated at 2022-06-14 17:49:20.737696
# Unit test for function parseOpts
def test_parseOpts():
    if sys.version_info >= (3,):
        def isstr(s):
            return isinstance(s, str)
    else:
        def isstr(s):
            return isinstance(s, basestring)  # noqa: F821

    parser, opts, args = parseOpts(['-i', '--username', 'myuser', '--password', 'mypass', 'https://example.org', 'https://example.com'])
    assert len(args) == 2
    assert args[0] == 'https://example.org'
    assert args[1] == 'https://example.com'
    assert isstr(opts.username)
    assert isstr(opts.password)
    assert opts.username == 'myuser'
    assert opts.password == 'mypass'
    assert opt

# Generated at 2022-06-14 17:49:22.277042
# Unit test for function parseOpts
def test_parseOpts():
    # TODO: Implement unittest for this method
    pass


# Generated at 2022-06-14 17:49:30.532792
# Unit test for function parseOpts
def test_parseOpts():
    from youtube_dl.utils import encodeArgument
    from youtube_dl.compat import compat_shlex_split

    # Test if the help message doesn't fail
    #test(lambda: parseOpts(['-h']), expected_exc=SystemExit)
    #test(lambda: parseOpts(['--help']), expected_exc=SystemExit)
    test(lambda: parseOpts(['--extractor-descriptions']), expected_exc=SystemExit)

    # Test all the options

# Generated at 2022-06-14 17:49:40.975903
# Unit test for function parseOpts
def test_parseOpts():
    command_line_conf = ['--output=%(title)s-%(id)s-%(format_id)s.%(ext)s', 'https://youtu.be/BaW_jenozKc']
    opts, args = parseOpts(overrideArguments=command_line_conf)
    assert opts.outtmpl == '%(title)s-%(id)s-%(format_id)s.%(ext)s'
    assert args == ['https://youtu.be/BaW_jenozKc']

    command_line_conf = ['--output=%(title)s-%(id)s-%(format_id)s.%(ext)s', 'https://youtu.be/BaW_jenozKc', '--yes-playlist']
    opts, args = parse

# Generated at 2022-06-14 17:49:45.845086
# Unit test for function parseOpts
def test_parseOpts():
    try:
        if sys.argv[1] == 'parseOpts':
            if len(sys.argv) > 2:
                sys.argv[2:] = ['--%s' % a.replace('_', '-', 1) for a in sys.argv[2:]]
            print(parseOpts())
            return

    except IndexError:
        pass

    raise ValueError('Unit test only')

if __name__ == '__main__':
    print(test_parseOpts())


# Generated at 2022-06-14 17:50:11.766945
# Unit test for function parseOpts
def test_parseOpts():
    parser = _real_parseOpts(['--version'])[0]
    assert parser.has_option('--version')

    opts = _real_parseOpts(['--username=user', '--password=pwd', '--verbose'])[1]
    assert opts.username == 'user'
    assert opts.password == 'pwd'
    assert opts.verbose

    sys.argv = ['youtube-dl']
    opts = _real_parseOpts(['--get-title'])[1]
    assert opts.geturl
    assert opts.gettitle
    assert opts.getid
    assert opts.getthumbnail
    assert opts.getdescription

    opts = _real_parseOpts(['-4', '--add-metadata'])[1]

# Generated at 2022-06-14 17:50:21.514886
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-v'])
    assert vars(opts) == {'verbose': True}

    parser, opts, args = parseOpts(['--dump-user-agent'])
    assert vars(opts) == {'dump_user_agent': True}

    parser, opts, args = parseOpts(['--version'])
    assert vars(opts) == {'print_version': True}

    parser, opts, args = parseOpts(['-U', 'someuser', '--password', 'somepasswd'])
    assert vars(opts) == {
        'username': 'someuser',
        'password': 'somepasswd',
    }


# Generated at 2022-06-14 17:50:34.628154
# Unit test for function parseOpts
def test_parseOpts():
    from youtube_dl.utils import compose_request

# Generated at 2022-06-14 17:50:42.711541
# Unit test for function parseOpts
def test_parseOpts():
    from sys import argv
    from os import remove
    from tempfile import mkstemp

    opts1 = ['-v', '--username', 'a', '-p', 'b', '--']
    opts2 = ['--config-location', '/tmp/youtube-dl.conf', '--']
    with open('/tmp/youtube-dl.conf', 'w') as f:
        f.write('\n'.join(['--proxy', 'user:pass@host']))
    opts3 = ['--config-location', '/tmp/youtube-dl.conf', '--ignore-config', '--']
    opts4 = ['--max-downloads', '100', '--']
    opts5 = ['--yes-playlist', '--']
    opts6 = []

# Generated at 2022-06-14 17:50:47.151208
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts()
    assert '-h' in opts.default_search
    assert 'mp4' in opts.extract_flat
# Unit tests for function _check_executable

# Generated at 2022-06-14 17:50:58.988565
# Unit test for function parseOpts
def test_parseOpts():
    from six.moves import input
    # new argparser
    argparser = argparse.ArgumentParser(
        prog='youtube-dl',
        description="YouTube video downloader")
    argparser.add_argument(
        dest='urls', metavar='URL', nargs='+',
        help='URLs of the video(s) to be downloaded')
    argparser.add_argument(
        '-v', '--verbose',
        dest='verbose', action='store_true',
        help='Be verbose. Print various debugging information.')
    argparser.add_argument(
        '--version',
        action='store_true',
        help='Print program version')

    # Convert the old optparse into argparse

# Generated at 2022-06-14 17:51:09.098249
# Unit test for function parseOpts
def test_parseOpts():
    _downloader = YoutubeDL(params={})
    parser, opts, args = parseOpts(['-4', '--verbose', '-o', 'testing.%(ext)s', 'https://www.youtube.com/watch?v=BaW_jenozKc'])
    assert opts.prefer_insecure is True
    assert opts.verbose is True
    assert opts.simulate is False
    assert opts.format is None
    assert opts.outtmpl == 'testing.%(ext)s'
    assert opts.quiet is False
    assert opts.no_warnings is False
    assert args == ['https://www.youtube.com/watch?v=BaW_jenozKc']

# Generated at 2022-06-14 17:51:10.653876
# Unit test for function parseOpts
def test_parseOpts():
    pass
# }}}

# {{{ updateversion

# Generated at 2022-06-14 17:51:19.427836
# Unit test for function parseOpts
def test_parseOpts():
    from youtube_dl.utils import encodeArgument
    parser, opts, args = parseOpts(['-U', 'FooBar'])
    assert opts.user_agent == 'FooBar'
    parser, opts, args = parseOpts(['-3', 'FooBar'])
    assert opts.m3u8_prefer_native
    parser, opts, args = parseOpts(['--m3u8-prefer-native'])
    assert opts.m3u8_prefer_native
    parser, opts, args = parseOpts(['--external-downloader', encodeArgument('foo bar')])
    assert opts.external_downloader == 'foo bar'
    parser, opts, args = parseOpts(['-u', 'FooBar'])
    assert opts

# Generated at 2022-06-14 17:51:20.538487
# Unit test for function parseOpts
def test_parseOpts():
    # TODO
    pass



# Generated at 2022-06-14 17:51:51.221420
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts()
    assert(opts.outtmpl=='%(id)s-%(title)s.%(ext)s')
    assert(opts.no_warnings==False)
    assert(opts.version==False)

# test_parseOpts()

# Generated at 2022-06-14 17:52:01.163566
# Unit test for function parseOpts
def test_parseOpts():
    (parser, opts, args) = parseOpts(
        ['--username', 'foo', '--password', 'bar', '--verbose', '--quiet', '--format', '22', 'http://www.youtube.com/watch?v=BaW_jenozKc'])
    assert(opts.username == 'foo')
    assert(opts.password == 'bar')
    assert(opts.format == '22')
    assert(opts.verbose == True)
    assert(opts.quiet == True)
    assert('http://www.youtube.com/watch?v=BaW_jenozKc' in args)


# Generated at 2022-06-14 17:52:02.760325
# Unit test for function parseOpts
def test_parseOpts():
    parser,opts,args = parseOpts()

# Generated at 2022-06-14 17:52:12.531190
# Unit test for function parseOpts
def test_parseOpts():
    from collections import OrderedDict
    from sys import version_info as sys_version_info

    from .utils import prepend_extension, platform_name

    from .extractor import gen_extractors
    gen_extractors()

    # output_template
    parser, opts, _ = parseOpts(['-o', '%(title)s.%(ext)s'])
    assert opts.outtmpl == '%(title)s.%(ext)s'

    parser, opts, _ = parseOpts(['-o', 'test.%(ext)s'])
    assert opts.outtmpl == 'test.%(ext)s'

    parser, opts, _ = parseOpts(['-o', 'test.%(width)s-%(ext)s'])

# Generated at 2022-06-14 17:52:19.692022
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-U', 'UnitTestUserAgent'])
    assertEqual(opts.usenetrc, False)
    assertEqual(opts.username, None)
    assertEqual(opts.password, None)
    assertEqual(opts.video_password, None)
    assertEqual(opts.ap_username, None)
    assertEqual(opts.ap_password, None)
    assertEqual(opts.quiet, False)
    assertEqual(opts.no_warnings, False)
    assertEqual(opts.simulate, False)
    assertEqual(opts.skip_download, False)
    assertEqual(opts.format, None)
    assertEqual(opts.listformats, False)

# Generated at 2022-06-14 17:52:31.107135
# Unit test for function parseOpts
def test_parseOpts():
    try:
        from nose.tools import eq_
    except ImportError:
        raise
    parser, opts, args = parseOpts(['-v'])
    eq_(opts.verbose, True)
    parser, opts, args = parseOpts(['--verbose'])
    eq_(opts.verbose, True)
    parser, opts, args = parseOpts(['-v', '--username', 'name', '--password', 'pass'])
    eq_(opts.verbose, True)
    eq_(opts.username, 'name')
    eq_(opts.password, 'pass')
    parser, opts, args = parseOpts(['--username', 'name', '--password', 'pass', '--'])
    eq_(opts.username, None)

# Generated at 2022-06-14 17:52:39.914350
# Unit test for function parseOpts
def test_parseOpts():
    from .utils import encodeFilename, parse_resolution
    def test_parse_resolution(res):
        return parse_resolution(res) == parse_resolution(encodeFilename(res))

    assert test_parse_resolution('360')
    assert test_parse_resolution('360p')
    assert test_parse_resolution('0')
    assert test_parse_resolution('0p')
    assert test_parse_resolution('1920x1080')
    assert test_parse_resolution('1920x1080p')



# Generated at 2022-06-14 17:52:43.077615
# Unit test for function parseOpts
def test_parseOpts():
    import optparse
    parser, opts, args = parseOpts()
# end of unit test for function parseOpts


# Generated at 2022-06-14 17:52:43.823621
# Unit test for function parseOpts
def test_parseOpts():
    pass



# Generated at 2022-06-14 17:52:55.125193
# Unit test for function parseOpts
def test_parseOpts():
    print("##### Begin tests_parseOpts #####")
    class Object(object):
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    opts = Object(verbose=True)
    args = []
    if not os.path.exists("../temp/youtube-dl.conf"):
        open("../temp/youtube-dl.conf", "w+")
    _config_opts = ['--config-location', '../temp/youtube-dl.conf']
    _parseOpts(overrideArguments=_config_opts)
    print("##### End tests_parseOpts #####")



# Generated at 2022-06-14 17:53:54.874851
# Unit test for function parseOpts
def test_parseOpts():
    """
        Function to test options that are parsed by parseOpts()
    """
    import shlex
    opts = parseOpts(shlex.split("--proxy http://localhost:8080 -f bestvideo+bestaudio"))[1]
    assert opts.proxy == "http://localhost:8080"
    assert opts.format == "bestvideo+bestaudio"
    opts = parseOpts(shlex.split("--proxy"))[1]
    assert opts.proxy == None


# Generated at 2022-06-14 17:54:07.415893
# Unit test for function parseOpts
def test_parseOpts():
    sys.argv = ['youtube-dl']
    parser, opts, args = parseOpts()

    assert opts.quiet == False
    assert opts.verbose == False
    assert opts.simulate == False
    assert opts.get_url == False
    assert opts.get_title == False
    assert opts.get_id == False
    assert opts.get_thumbnail == False
    assert opts.get_description == False
    assert opts.get_duration == False
    assert opts.get_filename == False
    assert opts.get_format == False
    assert opts.dump_pages == False
    assert opts.write_pages == False
    assert opts.dump_json == False
    assert opts.write_json == False
    assert opts.write_srt == False


# Generated at 2022-06-14 17:54:17.219754
# Unit test for function parseOpts
def test_parseOpts():
    import youtube_dl.YoutubeDL
    import sys

# Generated at 2022-06-14 17:54:30.445995
# Unit test for function parseOpts
def test_parseOpts():
    # Run parseOpts with no arguments
    testargs = []
    ret = parseOpts(testargs)

    # Check if ret is a tuple
    assert isinstance(ret, tuple)

    # Check if ret is a tuple of three elements
    assert len(ret) == 3

    # Check if ret[0] is an optparse.OptionParser
    assert isinstance(ret[0], optparse.OptionParser)

    # Check if ret[1] is a optparse.Values
    assert isinstance(ret[1], optparse.Values)

    # Check if ret[2] is a list
    assert isinstance(ret[2], list)

    # # Run parseOpts with arguments
    # testargs = ['-v', '--get-title', '--get-description']
    # ret = parseOpts(testargs)

    #

# Generated at 2022-06-14 17:54:40.336571
# Unit test for function parseOpts

# Generated at 2022-06-14 17:54:50.532730
# Unit test for function parseOpts
def test_parseOpts():
    downloader_simulate = [
        '--simulate',
    ]
    parser, opts, args = parseOpts(downloader_simulate)
    assert opts.simulate == True

    verbosity_simulate = [
        '--verbose',
    ]
    parser, opts, args = parseOpts(verbosity_simulate)
    assert opts.verbose == True

    verbosity_simulate = [
        '-v',
    ]
    parser, opts, args = parseOpts(verbosity_simulate)
    assert opts.verbose == True

# 'main' starts here


# Generated at 2022-06-14 17:54:51.462506
# Unit test for function parseOpts
def test_parseOpts():
    import youtube_dl.extractor.test



# Generated at 2022-06-14 17:55:01.997660
# Unit test for function parseOpts
def test_parseOpts():
    assert parseOpts(['--verbose'])[1].verbose
    assert not parseOpts(['--no-verbose'])[1].verbose
    opts, _args = parseOpts(['--min-sleep-interval', '10'])
    assert opts.min_sleep_interval >= 10
    opts, _args = parseOpts(['--max-sleep-interval', '5'])
    assert opts.max_sleep_interval <= 5
    opts, _args = parseOpts(['--sleep-interval', '1'])
    assert opts.min_sleep_interval == 1
    assert opts.max_sleep_interval == 1
    assert opts.call_home
    assert not parseOpts(['--no-call-home'])[1].call_home

# Generated at 2022-06-14 17:55:12.880839
# Unit test for function parseOpts
def test_parseOpts():
    t_opts, t_args = parseOpts(['-u', 'user', '-p', 'passwd', '-F', 'best', '--write-info-json', 'some_video'])
    assert_equals(t_opts.username, 'user')
    assert_equals(t_opts.password, 'passwd')
    assert_equals(t_opts.format, 'best')
    assert_equals(t_opts.writeinfojson, True)



# Generated at 2022-06-14 17:55:18.674348
# Unit test for function parseOpts
def test_parseOpts():

    def _parse_opts(args):
        return parseOpts(overrideArguments=args)[1]

    # No option/argument at all
    opts = _parse_opts([])
    assert opts.usenetrc is False
    assert opts.username is None
    assert opts.password is None
    assert opts.video_password is None

    # Specify --username
    opts = _parse_opts(['--username', 'foo'])
    assert opts.username == 'foo'
    assert opts.password is None
    assert opts.video_password is None

    # Specify --username and --password
    opts = _parse_opts(['--username', 'foo', '--password', 'bar'])
    assert opts.username == 'foo'
    assert opts.password

# Generated at 2022-06-14 17:57:24.330917
# Unit test for function parseOpts
def test_parseOpts():
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.postprocessor import FFmpegEmbedSubtitlePP
    def check_opts(opts, expected):
        ret_opts = {}
        for o in expected:
            ret_opts[o] = getattr(opts, o)
        return ret_opts

    parser, options, _ = parseOpts(['-f', 'best',
        '--add-metadata', '--embed-thumbnail', '--convert-subs', 'srt',
        '--write-all-thumbnails', '--write-description', '--write-info-json'])
    youtube_dl = YoutubeDL(params=options)
    assert youtube_dl.params['outtmpl'] == '%(title)s-%(id)s.%(ext)s'

# Generated at 2022-06-14 17:57:36.478255
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts([])
    assert not opts.verbose
    assert not opts.quiet
    assert not opts.no_warnings
    assert not opts.ignore_errors
    assert not opts.skip_unavailable_fragments
    assert opts.default_search == 'auto'
    assert not opts.playliststart
    assert not opts.playlistend
    assert not opts.matchtitle
    assert not opts.rejecttitle
    assert not opts.max_downloads
    assert not opts.prefer_free_formats
    assert not opts.abr
    assert not opts.vb
    assert not opts.keepvideo
    assert not opts.no_postoverwrites
    assert not opts.listformats
    assert not opts

# Generated at 2022-06-14 17:57:47.467949
# Unit test for function parseOpts
def test_parseOpts():
    from xml.etree.ElementTree import fromstring
    from io import StringIO
    import json

    def parse_default_opts(override_args=None):
        parser, opts, args = parseOpts(override_args)
        if len(args) > 1:
            parser.error('too many arguments')
        if args:
            opts.url = args[0]
        if not opts.usenetrc:
            opts.username = opts.password = None
        return opts

    def _test_parse_opts(arg_str, expected_opts):
        opts = parse_default_opts(arg_str.split())

# Generated at 2022-06-14 17:57:56.042794
# Unit test for function parseOpts
def test_parseOpts():
    from sys import argv
    parser, opts, args = parseOpts()
    for o in parser.option_list:
        if o.dest is not None:
            print(o.dest, getattr(opts, o.dest))

# PATCHES

# Bypass web proxy when downloading web pages
if sys.version_info[0] >= 3:
    # in python 3, urllib.request.build_opener takes the handler class (ProxyHandler)
    # instead of an instance of the handler.
    class ProxyHandler(urllib.request.ProxyHandler):
        pass
    
    ProxyHandler_orig = urllib.request.ProxyHandler
    urllib.request.ProxyHandler = ProxyHandler
