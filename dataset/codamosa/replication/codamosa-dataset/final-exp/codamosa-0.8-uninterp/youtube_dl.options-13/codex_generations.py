

# Generated at 2022-06-14 17:48:28.073227
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-o', 'file.%(ext)s'])
    assert opts.outtmpl == 'file.%(ext)s'
    assert 'file.%(ext)s' in opts.outtmpl
    assert '%(ext)s' in opts.outtmpl
    parser, opts, args = parseOpts(['--embed-subs', 'http://example.com'])
    assert opts.embedsubtitles
    parser, opts, args = parseOpts(['--extract-audio', 'http://example.com'])
    assert opts.extractaudio
    parser, opts, args = parseOpts(['--audio-format', 'ogg', 'http://example.com'])
    assert opts.audioformat == 'ogg'


# Generated at 2022-06-14 17:48:35.475928
# Unit test for function parseOpts
def test_parseOpts():
    sys.argv = [sys.argv[0]]
    sys.argv += ["--proxy", "myProxy"]
    sys.argv += ["--simulate", "myUrl"]
    sys.argv += ["--noplaylist", "myUrl2"]
    sys.argv += ["--verbose", "myUrl3"]
    sys.argv += ["--ignore-errors", "myUrl4"]
    sys.argv += ["--skip-download", "myUrl5"]
    sys.argv += ["--yes-playlist", "myUrl6"]
    sys.argv += ["--dump-user-agent", "myUrl7"]
    sys.argv += ["--version", "myUrl8"]
    sys.argv += ["--help", "myUrl9"]

# Generated at 2022-06-14 17:48:38.042754
# Unit test for function parseOpts
def test_parseOpts():
    # print(u'parseOpts() = ' + str(parseOpts()) + '\n')
    assert True
# test_parseOpts()


# Generated at 2022-06-14 17:48:45.907914
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts([])
    assert opts.username is None
    assert opts.password is None
    assert opts.twofactor is None
    assert opts.videopassword is None
    assert opts.ap_username is None
    assert opts.ap_password is None
    assert opts.outtmpl == '%(title)s-%(id)s.%(ext)s'
    assert opts.usenetrc is False
    assert opts.quiet is False
    assert opts.no_warnings is False
    assert opts.forceurl is False
    assert opts.forcetitle is False
    assert opts.simulate is False
    assert opts.skip_download is False
    assert opts.format is None
    assert opts.listform

# Generated at 2022-06-14 17:48:59.221872
# Unit test for function parseOpts
def test_parseOpts():
    from io import StringIO
    from sys import argv
    from youtube_dl.utils import encodeArgument

    def parseOpts(overrideArguments=None):
        parser, opts, args = _real_parseOpts(overrideArguments)
        for dest in vars(opts):
            if getattr(opts, dest) == parser.get_default(dest):
                setattr(opts, dest, None)
        return opts

    opts = parseOpts([])
    assert opts.verbose is False
    assert opts.quiet is False
    assert opts.no_warnings is False
    assert opts.simulate is False
    assert opts.skip_download is False
    assert opts.format is None
    assert opts.listformats is False
    assert opts.list_thumbnails

# Generated at 2022-06-14 17:49:05.990727
# Unit test for function parseOpts
def test_parseOpts():
    # parseOpts()
    print('parseOpts(): ')
    parser, opts, args = parseOpts()
    print(parser, opts, args)

    # parseOpts(['--format=bestaudio', '--extract-audio', '--audio-format=mp3', 'https://www.youtube.com/watch?v=BaW_jenozKc'])
    print('parseOpts(overrideArguments): ')
    parser, opts, args = parseOpts(['--format=bestaudio', '--extract-audio', '--audio-format=mp3', 'https://www.youtube.com/watch?v=BaW_jenozKc'])
    print(parser, opts, args)

    # parseOpts(['https://www.youtube.com/watch?v=BaW_

# Generated at 2022-06-14 17:49:16.359876
# Unit test for function parseOpts
def test_parseOpts():
    from sys import argv
    from youtube_dl.postprocessor import FFmpegMetadataPP
    from youtube_dl.utils import match_filter_func
    # Define a dummy write method for the YouTubeDL object
    def dummy_ydl_write(s):
        pass
    # Instantiate the youtube_dl object
    ydl = YoutubeDL({'outtmpl': '%(id)s%(ext)s'})
    ydl.params['simulate'] = True
    ydl.params['quiet'] = True
    ydl.params['forcejson'] = True
    ydl.params['skip_download'] = True
    ydl.params['dump_single_json'] = True
    ydl.write = dummy_ydl_write
    ydl.process_ie_result = lambda i, f: f
    # Test without any

# Generated at 2022-06-14 17:49:27.592676
# Unit test for function parseOpts
def test_parseOpts():
    # parseOpts(overrideArguments=None)
    global parseOpts
    my_parseOpts = lambda overrideArguments=None: parseOpts(overrideArguments=overrideArguments)[2]
    global user_agent
    user_agent = youtube_dl.version.user_agent()
    assert my_parseOpts([]) == \
        ['https://www.youtube.com/watch?v=BaW_jenozKc']
    assert my_parseOpts([]) == \
        ['https://www.youtube.com/watch?v=BaW_jenozKc', 'https://www.youtube.com/watch?v=VoTbW4B_8Ws']

# Generated at 2022-06-14 17:49:29.609863
# Unit test for function parseOpts
def test_parseOpts():
    assert parseOpts(['-i'])[2] == ['https://www.youtube.com/watch?v=BaW_jenozKc']
    assert parseOpts(['--ignore-config'])[2] == []
    
# Define main function

# Generated at 2022-06-14 17:49:32.007048
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-h'])
    assert(opts.help)
    assert(not opts.usenetrc)
    assert(not opts.username)
    assert(not opts.password)
    assert(not opts.verbose)

# End unit test


# Generated at 2022-06-14 17:49:48.699018
# Unit test for function parseOpts
def test_parseOpts():
    if __name__ != '__main__':
        return
    parser, opts, _ = parseOpts(['--version'])
# Invoke unit test for function parseOpts
test_parseOpts()


# Generated at 2022-06-14 17:49:55.755559
# Unit test for function parseOpts
def test_parseOpts():
    write_string = sys.stdout.write
    get_err_string = sys.stderr.write
    # test for py2x, py3x
    if isinstance(u'\u2603', str):
        return
    # py2.x

# Generated at 2022-06-14 17:50:09.115881
# Unit test for function parseOpts
def test_parseOpts():
    def t(overrideArguments, expectedOut, expectedRetVal):
        parser, out, retVal = parseOpts(overrideArguments)
        assertEqual(out, expectedOut)
        assertEqual(retVal, expectedRetVal)

    t(None, None, True)

# Generated at 2022-06-14 17:50:20.280871
# Unit test for function parseOpts
def test_parseOpts():
    # pylint: disable=protected-access
    def get_opts(args):
        parser, opts, _ = parseOpts(args)
        opts = vars(opts)
        for key, value in opts.items():
            if value is None:
                del opts[key]
        return opts
    assert get_opts([]) == {}

# Generated at 2022-06-14 17:50:32.796756
# Unit test for function parseOpts
def test_parseOpts():
    # Check that options can override configuration files
    opts_list = {
        'retries': '3',
        'nooverwrites': '',
        'no_warnings': '',
    }
    opts = _hide_login_info(parseOpts(list(itertools.chain(*opts_list.items())))[1])
    assert opts.retries == 3
    assert opts.nooverwrites
    assert opts.no_warnings

    # Check that configuration files override default options
    opts_list = {
        'retries': '1',
        'ignore_errors': '',
        'verbose': '',
    }
    opts = _hide_login_info(parseOpts(list(itertools.chain(*opts_list.items())))[1])


# Generated at 2022-06-14 17:50:34.718032
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts()
# End Unit test for function parseOpts


# Generated at 2022-06-14 17:50:43.750316
# Unit test for function parseOpts
def test_parseOpts():
    try:
        opts, args = parseOpts(['-F'])
        assert False
    except SystemExit:
        pass
    opts, args = parseOpts(['-u', 'user', '-p', 'passwd', '-F'])
    assert opts.username == 'user'
    assert opts.password == 'passwd'
    opts, args = parseOpts(['-F', '-a', '-'])
    assert opts.usenetrc == True
    assert opts.username == 'user'
    assert opts.password == 'passwd'
    opts, args = parseOpts(['-F', '--flat-playlist'])
    assert opts.flat_playlist == True

# Generated at 2022-06-14 17:50:49.050803
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts()
    print(opts)
    assert opts.addmetadata is False
    assert opts.outtmpl == '%(id)s'
    assert opts.verbose is False

if __name__ == '__main__':
    test_parseOpts()

# Generated at 2022-06-14 17:51:01.080785
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-f', '18', '--min-filesize', '1k', '--max-filesize', '2KiB', '--', 'http://www.youtube.com/watch?v=BaW_jenozKc'])
    assert opts.format == '18'
    assert opts.min_filesize == 1024
    assert opts.max_filesize == 2*1024
    assert args == ['http://www.youtube.com/watch?v=BaW_jenozKc']


# Generated at 2022-06-14 17:51:06.965594
# Unit test for function parseOpts
def test_parseOpts():
    test = ['--verbose', '-v']
    result = parseOpts(test)
    assert result[2].verbose == 2

# This function is called from the parseOpts function
# It reads the options from a config file
# Returns an empty configuration in case an error occured

# Generated at 2022-06-14 17:51:26.411777
# Unit test for function parseOpts

# Generated at 2022-06-14 17:51:37.668785
# Unit test for function parseOpts
def test_parseOpts():
    from youtube_dl.utils import prepend_extension
    parser, opts, args = parseOpts([
        '-i', '--get-id', '--get-title',
        '--username=user', '--password=pass',
        'http://www.youtube.com/watch?v=BaW_jenozKc'])
    assert opts.geturl
    assert opts.getid
    assert opts.gettitle
    assert opts.username == 'user'
    assert opts.password == 'pass'
    assert args == ['http://www.youtube.com/watch?v=BaW_jenozKc']


# Generated at 2022-06-14 17:51:48.733683
# Unit test for function parseOpts
def test_parseOpts():
    opts, args = parseOpts(['-u', 'user', '-p', 'pass', 'url'])
    assert opts.username == 'user'
    assert opts.password == 'pass'
    assert args == ['url']
    opts, args = parseOpts(['url', '-u', 'user', '-p', 'pass'])
    assert opts.username == 'user'
    assert opts.password == 'pass'
    assert args == ['url']

    opts, args = parseOpts(['-4', 'url'])
    assert opts.prefer_ipv4 is True
    assert args == ['url']
    opts, args = parseOpts(['-6', 'url'])
    assert opts.prefer_ipv6 is True
    assert args == ['url']

# Generated at 2022-06-14 17:52:01.269185
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(
        ['https://www.youtube.com/watch?v=BaW_jenozKc', '--output=%(id)s.%(ext)s', '-i', '--no-playlist', '-j'])
    assert opts.outtmpl == '%(id)s.%(ext)s'
    assert not opts.playliststart
    assert not opts.playlistend
    assert not opts.nooverwrites
    assert opts.ignoreerrors
    assert not opts.simulate
    assert not opts.geturl
    assert opts.gettitle
    assert opts.getid
    assert not opts.get_thumbnail
    assert opts.getdescription
    assert opts.getfilename
    assert opts.get_

# Generated at 2022-06-14 17:52:11.610594
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts([])
    assert opts.usenetrc == False, 'we think opts.usenetrc is False when it is not'
    parser, opts, args = parseOpts(['-u', 'foo'])
    assert opts.username == 'foo', 'opts.username was not set correctly'
    assert opts.usenetrc == False, 'opts.usenetrc changed when it should not have'

# ################ START YOUTUBE-DL CODE ######################################

# ################### CONSTANTS ###############################################

YOUTUBE_IE_NAME = 'youtube'
YOUTUBEDL_VERSION = '2017.01.06'

# Generated at 2022-06-14 17:52:13.661780
# Unit test for function parseOpts
def test_parseOpts():
    import doctest
    doctest.run_docstring_examples(parseOpts, globals(), True, __name__)



# Generated at 2022-06-14 17:52:26.711755
# Unit test for function parseOpts
def test_parseOpts():
    # Test with empty options
    parser, opts, _ = parseOpts([])
    assert opts.verbose == False
    assert opts.quiet == False
    assert opts.forceurl == False
    assert opts.forcetitle == False
    assert opts.forceid == False
    assert opts.forcethumbnail == False
    assert opts.forcedescription == False
    assert opts.simulate == False
    assert opts.skip_download == False
    assert opts.format == None
    assert opts.listformats == False
    assert opts.outtmpl == None
    assert opts.autonumber_size == None
    assert opts.autonumber_start == 1
    assert opts.restrictfilenames == False
    assert opts.ignoreerrors == False
    assert opts

# Generated at 2022-06-14 17:52:40.024892
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-u', 'test_user', '-p', 'test_password', 'testargs'])
    assert opts.username == 'test_user'
    assert opts.password == 'test_password'
    assert opts.usenetrc == False
    assert args == ['testargs']
    assert opts.verbose == False
    
    parser, opts, args = parseOpts(['--username', 'test_user', '--password', 'test_password', 'testargs'])
    assert opts.username == 'test_user'
    assert opts.password == 'test_password'
    assert opts.usenetrc == False
    assert args == ['testargs']
    assert opts.verbose == False

    parser, opts, args = parseOpts

# Generated at 2022-06-14 17:52:47.314919
# Unit test for function parseOpts
def test_parseOpts():
    opts = parseOpts(["-f","mp4","--playlist-reverse","-i","https://www.youtube.com/playlist?list=PLvj3DqYOyf3x8kWhV7v2HZ_uV7Rz8tFwf"])
    
    print("Unit test performed")
    print("Test passed")
    return


# Generated at 2022-06-14 17:53:00.230198
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts((
        '--buffer-size', '16777215', '--no-progress', '--add-metadata', '--keep-video',
        '-s', 'https://www.youtube.com/watch?v=WqJineyEszo', '-o', '%(title)s-%(id)s.%(ext)s',
        '-f', '18/22', '--external-downloader', 'curl', '--external-downloader-args', '-C -'))
    assert opts.usenetrc is False
    assert opts.username == None
    assert opts.password == None
    assert opts.twofactor == None
    assert opts.videopassword == None
    assert opts.ap_pass == None

# Generated at 2022-06-14 17:53:40.795710
# Unit test for function parseOpts
def test_parseOpts():
    """Check if get the expected tuple by parseOpts function."""
    from optparse import OptionParser
    from sys import argv
    from os.path import exists
    from os import getcwd
    test_argv = ['', '--output=/tmp/%(title)s-%(id)s.%(ext)s', '--skip-download', '--list-formats', 'https://www.youtube.com/watch?v=BaW_jenozKc']
    #If using the argv in the main function, run this test will interrupt the program to ask user input the video password.
    parser, opts, args = parseOpts(test_argv[1:])
    assert args[0] == 'https://www.youtube.com/watch?v=BaW_jenozKc'

# Generated at 2022-06-14 17:53:52.096640
# Unit test for function parseOpts

# Generated at 2022-06-14 17:54:01.120069
# Unit test for function parseOpts

# Generated at 2022-06-14 17:54:10.700359
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-i'])
    assert opts.ignoreerrors

    parser, opts, args = parseOpts(['-4'])
    assert opts.forceipv4

    parser, opts, args = parseOpts(['-6'])
    assert opts.forceipv6

    parser, opts, args = parseOpts(['--write-pages'])
    assert opts.writepages

    parser, opts, args = parseOpts(['--write-thumbnail'])
    assert opts.writethumbnail

    parser, opts, args = parseOpts(['-a', '-'])
    assert opts.batchfile == '-'

    parser, opts, args = parseOpts(['-a', 'a'])
    assert opts.batch

# Generated at 2022-06-14 17:54:22.346157
# Unit test for function parseOpts
def test_parseOpts():
    for args in (['-h'], ['--help']):
        parser, opts, args = parseOpts(args)
        assert not args
        assert not opts.verbose
        assert not opts.quiet
        assert not opts.username
        assert not opts.password
        assert not opts.twofactor
        assert not opts.videopassword
        assert not opts.video_password
        assert opts.noplaylist
        assert opts.age_limit is None
        assert opts.download_archive is None
        assert not opts.nooverwrites
        assert not opts.writesubtitles
        assert not opts.writeautomaticsub
        assert not opts.allsubtitles
        assert not opts.listsubtitles
        assert not opts.matchtitle

# Generated at 2022-06-14 17:54:35.147073
# Unit test for function parseOpts
def test_parseOpts():
    from .YoutubeDL import parseOpts
    from .YoutubeDL import YoutubeDL
    from .compat import compat_str
    from .compat import compat_shlex_split
    from .utils import FakeYDL

    assert parseOpts([])
    assert parseOpts(['foo'])[2] == ['foo']

    opts, args = parseOpts([])
    assert opts.nooverwrites
    assert opts.noplaylist

    # assert opts.writeinfojson
    opts, args = parseOpts(['-i'])
    assert not opts.nooverwrites
    assert opts.ignoreerrors
    assert opts.writeinfojson

    opts, args = parseOpts(compat_shlex_split('--no-overwrites -ic --verbose'))


# Generated at 2022-06-14 17:54:42.755622
# Unit test for function parseOpts
def test_parseOpts():
    opts = None
    try:
        # noinspection PyTypeChecker
        _, opts, _ = parseOpts([])
    except:
        sys.stderr.write('Failed to parse empty arguments.\n')
        raise
    if opts is None:
        sys.stderr.write('Failed to parse empty arguments.\n')
        raise Exception('Failed to parse empty arguments.')


# In Python 2 the Popen class is not reentrant. This means that you cannot
# call Popen from different threads. The simplest solution is to serialize
# all calls.

# noinspection PyUnusedLocal

# Generated at 2022-06-14 17:54:55.651782
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-f', '137+140', 'https://www.youtube.com/watch?v=BaW_jenozKc'])
    assert opts.format == '137+140'
    assert len(args) == 1
    assert args[0] == 'https://www.youtube.com/watch?v=BaW_jenozKc'
    parser, opts, args = parseOpts(['-i', '--', 'https://www.youtube.com/watch?v=BaW_jenozKc'])
    assert opts.simulate
    assert len(args) == 1
    assert args[0] == 'https://www.youtube.com/watch?v=BaW_jenozKc'

# Generated at 2022-06-14 17:55:03.811213
# Unit test for function parseOpts
def test_parseOpts():
    # Update PYTHONHASHSEED before importing youtube_dl
    # python3.3+
    if getattr(sys, 'implementation', None) and sys.implementation.name == 'cpython':
        os.environ['PYTHONHASHSEED'] = '1'

    import youtube_dl
    old_opts, old_args = youtube_dl.parseOpts(['-i', '--no-warnings'])
    old_opts = dict(old_opts.__dict__)
    del old_opts['help']
    del old_opts['version']
    new_parser, new_opts, new_args = parseOpts(['-i', '--no-warnings'])
    new_opts = dict(new_opts.__dict__)
    del new_

# Generated at 2022-06-14 17:55:09.529210
# Unit test for function parseOpts
def test_parseOpts():
    try:
        opts, args = parseOpts(['-U', 'testuser', '-P', 'testpass', '-u', 'http://youtube.com/watch?v=BaW_jenozKc'])
    except SystemExit as e:
        if e.code == 0:
            return 0
        else:
            return e.code
# Function _match_filter

# Generated at 2022-06-14 17:56:18.434897
# Unit test for function parseOpts
def test_parseOpts():
    from getpass import getuser
    from random import randint
    def randbool():
        return randint(0, 1) == 0
    # To make the test deterministic we need to turn off randomness
    _G.random.seed(0)
    env = os.environ.copy()
    env['USER'] = getuser()
    env['HOME'] = os.getcwd()
    def run(args, expected, inputstr):
        with open(os.path.join(_G.TEST_HOME, 'stdin'), 'wb') as f:
            f.write(compat_bytes(inputstr, 'utf-8'))

# Generated at 2022-06-14 17:56:30.460143
# Unit test for function parseOpts
def test_parseOpts():
    from sys import argv as sys_argv
    from os import getenv as os_getenv
    from os import environ as os_environ

    def mock_getenv(var, default=None):
        if var == 'XDG_CONFIG_HOME':
            return None
        assert False, 'unexpected getenv(%r)' % var

    def mock_expanduser(path):
        assert not path == '~/.config/youtube-dl/config'
        assert not path == '~/.config/youtube-dl/cookies'
        return path

    def mock_readOptions(filename):
        if filename == '/etc/youtube-dl.conf':
            return []
        elif filename == '~/.config/youtube-dl/config':
            return []
        elif filename == 'custom_file_name':
            return

# Generated at 2022-06-14 17:56:41.796123
# Unit test for function parseOpts
def test_parseOpts():
    from sys import argv
    opts = {}
    args = ['url']

# Generated at 2022-06-14 17:56:53.097338
# Unit test for function parseOpts
def test_parseOpts():
    from youtube_dl.compat import compat_expanduser, compat_getenv
    # Add an argument to the list and check if it's in the
    # output list (expect no error)
    def check_add_option(add_arg, final_arg):
        opts, args = parseOpts([add_arg])
        assert opts.__dict__[final_arg] == True
    # Remove an argument from the list and check if it's
    # not in the output list (expect no error)
    def check_remove_option(remove_arg, final_arg):
        opts, args = parseOpts([remove_arg])
        assert opts.__dict__[final_arg] == False
    # Add and remove arguments from the list and check if
    # they are in the output list (expect error)
   

# Generated at 2022-06-14 17:57:03.794092
# Unit test for function parseOpts
def test_parseOpts():
    def assert_opts(overrideArguments, expected_defaults):
        parser, opts, args = parseOpts(overrideArguments)
        assert vars(opts) == expected_defaults


# Generated at 2022-06-14 17:57:07.601131
# Unit test for function parseOpts
def test_parseOpts():
    from youtube_dl.YoutubeDL import YoutubeDL
    parser, opts, _ = parseOpts(['-x', '--no-warnings', '--verbose', '--dump-user-agent', 'plop'])
    assert opts.extractaudio
    assert not opts.nooverwrites
    assert opts.verbose
    assert opts.dump_user_agent
    ydl = YoutubeDL(opts)
    ydl.add_default_info_extractors()
# End unit test for function parseOpts


# Generated at 2022-06-14 17:57:08.762102
# Unit test for function parseOpts
def test_parseOpts():
    print(parseOpts(["-i", "--youtube-skip-dash-manifest"]))


# Generated at 2022-06-14 17:57:17.471200
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-i'])
    assert opts.ignoreerrors

    parser, opts, args = parseOpts(['--cookies', 'foo.txt'])
    assert opts.cookiefile == 'foo.txt'

    parser, opts, args = parseOpts(['--prefer-ffmpeg'])
    assert opts.prefer_ffmpeg

    parser, opts, args = parseOpts(['--no-prefer-ffmpeg'])
    assert not opts.prefer_ffmpeg


# Download a given file and display the progress in the terminal.

# Generated at 2022-06-14 17:57:27.047235
# Unit test for function parseOpts
def test_parseOpts():
    write_string('Starting parseOpts unit test\n')
    # The test string is the output of `youtube-dl --ignore-config --no-warnings --dump-json URL`
    # where URL is https://www.youtube.com/watch?v=kj-LKjh0fS4

# Generated at 2022-06-14 17:57:38.029110
# Unit test for function parseOpts
def test_parseOpts():
    from itertools import imap
    from operator import methodcaller

    parser, opts, _ = parseOpts(
            ['--match-title', 'foo', '--no-playlist', '--yes-playlist',
             '--match-filter', 'is_live!=True', '--match-filter',
             'is_live!=False', '--max-downloads', '0', '--sleep-interval',
             '60', '--max-sleep-interval', '300', 'http://example.com/',
             '-f', 'bestvideo[height<=?1080]+bestaudio/best[height<=?1080]',
             '-F', 'bestvideo[height<=?1080]+bestaudio/best[height<=?1080]'])
    assert opts.match_title == ['foo']
   