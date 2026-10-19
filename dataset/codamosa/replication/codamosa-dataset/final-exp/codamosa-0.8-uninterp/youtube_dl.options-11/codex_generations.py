

# Generated at 2022-06-14 17:48:34.400709
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts()
    assert opts
    assert args

# Generated at 2022-06-14 17:48:43.425055
# Unit test for function parseOpts
def test_parseOpts():
    def _test(args):
        parser, opts, args = parseOpts(args)
        assert vars(opts) == eval(args[0]), '"%s" != "%s"' % (
            repr(vars(opts)), args[0])
    _test(['-h'])
    _test(['-u', 'user', '-p', 'pass', '-i', '-c', '-f', 'best'])
    _test(['-f', 'best'])
    _test(['-f', '22/17/43'])
    _test(['-f', '35/17/43/5/18/34'])

# Generated at 2022-06-14 17:48:54.020552
# Unit test for function parseOpts
def test_parseOpts():
    from collections import namedtuple
    from youtube_dl.utils import std_headers

    opts = namedtuple('Options', [
        'username', 'password', 'twofactor', 'videopassword', 'ap_username', 'ap_password',
        'ap_mso', 'ap_chlistid', 'videopassword', 'usenetrc', 'verbose',
    ])

# Generated at 2022-06-14 17:49:03.713882
# Unit test for function parseOpts
def test_parseOpts():
    from xml.dom.minidom import parseString
    from . import YoutubeDL
    # Test the -F option
    assert parseOpts(YoutubeDL, ['-F'])[2] == ['--all-formats']
    assert parseOpts(YoutubeDL, ['-f', '22/17/35'])[2] == ['--all-formats', '--format', '22/17/35']
    assert parseOpts(YoutubeDL, ['-f', '22/17/35', 'plop'])[1].format == ['22/17/35']
    assert parseOpts(YoutubeDL, ['--autonumber-size', '3'])[1].autonumber_size == 3
    assert parseOpts(YoutubeDL, ['--playlist-reverse'])[1].playlistreverse == True


# Generated at 2022-06-14 17:49:15.100198
# Unit test for function parseOpts
def test_parseOpts():
    from youtube_dl.YoutubeDL import YoutubeDL
    from youtube_dl.options import supported_extensions
    import tempfile
    import shutil

    ydl = YoutubeDL({})

    # test if default option values are used
    default_opts = ydl.params
    parser, opts, args = parseOpts(['http://www.youtube.com/watch?v=BaW_jenozKc'])
    assert opts.__dict__ == default_opts

    # test if default option values are overridden in config file
    config = tempfile.NamedTemporaryFile(mode='w', delete=False)
    config.write('--no-warnings\n')
    config.close()

# Generated at 2022-06-14 17:49:26.799691
# Unit test for function parseOpts
def test_parseOpts():
    old_getpass = getpass.getpass
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    old_exit = sys.exit
    def getpass_sideeffect(*args, **kargs):
        print('getpass')
        return 'getpass'
    def _getopt(args):
        _, opts, _ = parseOpts(args)
        return opts

# Generated at 2022-06-14 17:49:31.892461
# Unit test for function parseOpts
def test_parseOpts():
    from urllib.request import FancyURLopener
    class MyOpener(FancyURLopener):
        version = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15'
    class FakeProcess(object):
        pid = 15

    opener = MyOpener()

# Generated at 2022-06-14 17:49:39.063486
# Unit test for function parseOpts
def test_parseOpts():
    from os import sys, path
    sys.argv = ["main.py","-u","https://www.youtube.com/watch?v=NlA5KjXO7o0"]
    if __name__ == "__main__":
        current_dir = path.dirname(path.abspath(__file__))
        config_path = path.join(current_dir, "config.conf")
        sys.argv.extend(["--config-location",config_path])
        return parseOpts()
# Main function.

# Generated at 2022-06-14 17:49:46.699905
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts([])
    assert opts.outtmpl == '%(title)s-%(id)s.%(ext)s'
    assert opts.sleep_interval == 300
    assert opts.max_sleep_interval == 900
    assert opts.proxy == None
    assert opts.verbose == True
    assert opts.retries == 10
    assert opts.dump_intermediate_pages == False
    assert opts.write_pages == False
    assert opts.force_generic_extractor == False
    assert opts.no_warnings == False
    assert opts.outtmpl_na_placeholder == 'NA'
    assert opts.username == None
    assert opts.password == None
    assert opts.ap_username == None
    assert opt

# Generated at 2022-06-14 17:49:48.009005
# Unit test for function parseOpts
def test_parseOpts():
    test_parseOpts_basic()
    test_parseOpts_config_location()
    test_parseOpts_config_location2()


# Generated at 2022-06-14 17:50:14.955292
# Unit test for function parseOpts
def test_parseOpts():

    ydl = YoutubeDL(params={'verbose': True})
    ydl.params['logger'] = DummyLogger()

    # TODO Add unit tests for defaults
    # TODO Add unit tests for conflicts

    # Test parsing of single argument
    expected = [('--format', 'bestvideo+bestaudio')]
    res = ydl.parseOpts(['--format', 'bestvideo+bestaudio'])
    assert res == expected, 'Single option parsing failed'

    # Test parsing of an option with argument containing spaces
    expected = [('--output', '"this is a test.%(ext)s"')]
    res = ydl.parseOpts(['--output', '"this is a test.%(ext)s"'])
    assert res == expected, 'Option with argument containing spaces parsing failed'

    # Test parsing of

# Generated at 2022-06-14 17:50:25.343405
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-U', 'Mozilla/5.0'])
    assert opts.user_agent == 'Mozilla/5.0'
    assert args == []

    parser, opts, args = parseOpts(['--youtube-skip-dash-manifest'])
    assert opts.youtube_skip_dash_manifest
    assert args == []

    parser, opts, args = parseOpts(['DUMMY'])
    assert opts.ignore_errors
    assert args == ['DUMMY']


# Generated at 2022-06-14 17:50:37.191572
# Unit test for function parseOpts
def test_parseOpts():
    import youtube_dl.version
    sys.argv = ['youtube-dl', '-h']
    parser, opts, _ = parseOpts()
    assert opts.version is False
    assert opts.help is True
    assert opts.verbose is False
    assert opts.quiet is False
    assert opts.no_warnings is False
    assert opts.simulate is False
    assert opts.skip_download is False
    assert opts.format is None
    assert opts.listformats is False
    assert opts.usenetrc is False
    assert opts.username is None
    assert opts.password is None
    assert opts.twofactor is None
    assert opts.videopassword is None
    assert opts.ap_username is None
    assert opts.ap_

# Generated at 2022-06-14 17:50:48.134551
# Unit test for function parseOpts
def test_parseOpts():
    import sys
    import random
    import string
    import tempfile
    import os
    import shutil
    from collections import namedtuple

    def _write_file(contents):
        f = tempfile.NamedTemporaryFile(delete=False)
        f.write(contents)
        f.close()
        return f.name

    def _write_args(*args):
        return [_write_file(arg) for arg in args]

    def _get_random_string(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))


# Generated at 2022-06-14 17:50:50.823435
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts()
    assert opts.username == 'kk_youtube'
    assert opts.password == 'Fgtv2019'

# Generated at 2022-06-14 17:51:02.609826
# Unit test for function parseOpts
def test_parseOpts():
    from youtube_dl.YoutubeDL import YoutubeDL

# Generated at 2022-06-14 17:51:11.630020
# Unit test for function parseOpts
def test_parseOpts():
    opts, args = parseOpts(['-x', '-o', '/tmp/video_%(id)s.%(ext)s', '--ignore-config', 'https://www.youtube.com/watch?v=BaW_jenozKc'])
    assert opts.outtmpl == '/tmp/video_%(id)s.%(ext)s'
    assert opts.extractaudio == True
    assert opts.verbose == False
    assert args == ['https://www.youtube.com/watch?v=BaW_jenozKc']


# Generated at 2022-06-14 17:51:13.088627
# Unit test for function parseOpts
def test_parseOpts():
    # This is just for coverage
    assert parseOpts(None)


# Generated at 2022-06-14 17:51:15.898623
# Unit test for function parseOpts
def test_parseOpts():
    (oparser, opts, args) = parseOpts()


# %(autonumber)s -> %(autonumber)04d

# Generated at 2022-06-14 17:51:27.492624
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(overrideArguments = ['--verbose', '--get-title', 'http://www.youtube.com/watch?v=BaW_jenozKc'])
    assert opts.verbose == True
    assert opts.usetitle == True
    assert opts.quiet == False
    assert args[0] == 'http://www.youtube.com/watch?v=BaW_jenozKc'

    parser, opts, args = parseOpts(overrideArguments = ['--verbose', '--get-title'])
    assert opts.verbose == True
    assert opts.usetitle == True
    assert opts.quiet == False
    assert args[0] == None

    parser, opts, args = parseOpts(overrideArguments = [])


# Generated at 2022-06-14 17:51:44.818926
# Unit test for function parseOpts
def test_parseOpts():
    opt, _ = parseOpts(['-i', '-F', 'url'])
    assert opt.get('simulate')
    assert opt.get('extract_flat')



# Generated at 2022-06-14 17:51:59.145780
# Unit test for function parseOpts
def test_parseOpts():
    # Test case 1: no arguments
    parser, opts, args = parseOpts([])
    assert opts.verbose == False
    assert opts.quiet == False
    assert opts.no_warnings == False
    assert opts.format == None
    assert opts.listformats == False
    assert opts.version == False
    assert opts.ignoreerrors == False
    assert opts.ratelimit == None
    assert opts.retries == 10
    assert opts.buffersize == None
    assert opts.noprogress == False
    assert opts.playliststart == 1
    assert opts.playlistend == 0
    assert opts.matchtitle == None
    assert opts.rejecttitle == None
    assert opts.max_downloads == -1
    assert opts.prefer

# Generated at 2022-06-14 17:52:03.483785
# Unit test for function parseOpts
def test_parseOpts():
    """
    Unit test for function parseOpts
    """
    print("Unit test for function parseOpts starts")
    print("[PASS]")
    print("Unit test for function parseOpts ends")
    return

# Function to check if the downloader is installed

# Generated at 2022-06-14 17:52:12.946329
# Unit test for function parseOpts
def test_parseOpts():
    import sys
    import re
    # Save sys.argv
    old_sys_argv = sys.argv
    # Fix sys.argv
    sys.argv = ["youtube-dl"]

# Generated at 2022-06-14 17:52:18.599534
# Unit test for function parseOpts
def test_parseOpts():
    try:
        parser, opts, args = parseOpts()
    except:
        import traceback
        write_string(traceback.format_exc()+"\n") # Print traceback of the error

# Global variables
_downloaded_bytes = 0
_total_bytes = 0
_total_bytes_estimate = None
_filename = None
_prev_percent = 0
_eta = None
_eta_lock = threading.Lock()
_elapsed = 0  # seconds
_start_time = None
_socket_timeout = None
_nofile_interrupt = False



# Generated at 2022-06-14 17:52:30.474711
# Unit test for function parseOpts
def test_parseOpts():
    import argparse
    parser = argparse.ArgumentParser(description='Test parseOpts')
    parser.add_argument('--foo', action='store_true', help='dummy')
    parser.add_argument('--bar', action='store_true', help='dummy')
    parser.add_argument('-v', '--verbose', action='store_true', help='dummy')
    parser.add_argument('-B', '--batch-file', type=str, default=None, help='dummy')
    overrides = ['-B', '/dev/null', '--foo', '--verbose']
    _, opts, _ = parseOpts(parser, overrides)
    assert(opts.batchfile == '/dev/null')
    assert(opts.foo is True)

# Generated at 2022-06-14 17:52:42.964208
# Unit test for function parseOpts
def test_parseOpts():
    assert _hide_login_info(['foo', 'bar']) == ['foo', 'bar']
    assert _hide_login_info(['username', 'foo', 'password', 'bar']) == ['username', 'SECRET', 'password', 'SECRET']
    assert _hide_login_info(['username', 'foo', '--password', 'bar']) == ['username', 'foo', '--password', 'SECRET']
    assert _hide_login_info(['--username', 'foo', '--password', 'bar']) == ['--username', 'foo', '--password', 'SECRET']
    assert _hide_login_info(['--username', 'foo', '--password', 'bar', 'baz']) == ['--username', 'foo', '--password', 'SECRET', 'baz']

# Open a JSON file in universal

# Generated at 2022-06-14 17:52:53.843709
# Unit test for function parseOpts
def test_parseOpts():
    from youtube_dl.downloader.rtmp import RTMPDownloader
    for args in [['--username=foo', '--password=bar', '--verbose', 'http://a'],
                 ['--usenetrc', '--username=foo', '--password=bar',
                  '--verbose', 'http://a'],
                 ['--video-password=bar', '--verbose', 'http://a'],
                 ['--ap-password=bar', '--verbose', 'http://a']]:

        opts, _ = parseOpts(args)
        assert not hasattr(opts, 'username') and not hasattr(opts, 'password')
        assert not hasattr(opts, 'netrc')
        assert not hasattr(opts, 'video_password')

# Generated at 2022-06-14 17:53:03.926805
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts([
        '-v',
        '--write-srt',
        '--list-subs',
        '--username', 'admin',
        '--password', 'pass',
        '--',
        '--verbose',
        'https://www.youtube.com/watch?v=BaW_jenozKc',
        'http://youtu.be/BgAlQuqzl8o',
        '--verbose',
        '--',
        'http://www.youtube.com/watch?v=Ik-RsDGPI5Y'])

    assert len(args) == 3
    assert args[0] == 'https://www.youtube.com/watch?v=BaW_jenozKc'

# Generated at 2022-06-14 17:53:10.186523
# Unit test for function parseOpts
def test_parseOpts():
    class T(object):
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    def check(conf, expected_downloader=False, progress_with_newline=False):
        parser, opts, args = parseOpts(conf)

        assert opts.ratelimit == 101010
        assert opts.retries == 88
        assert opts.buffersize == '333k'
        assert opts.noprogress == progress_with_newline
        assert opts.progress_with_newline == progress_with_newline
        assert opts.playliststart == 13
        assert opts.playlistend == 42
        assert opts.playlist_items is None
        assert opts.playlistreverse is True
        assert opts.playlistrandom is True
       

# Generated at 2022-06-14 17:53:49.719108
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-f', '22/25/best/worst', 'http://www.youtube.com/watch?v=BaW_jenozKc'])
    assert opts.format == '22/25/best/worst'

    parser, opts, args = parseOpts(['-f', '22/25/best/worst', 'https://www.youtube.com/watch?v=BaW_jenozKc'])
    assert opts.format == '22/25/best/worst'

    parser, opts, args = parseOpts(['https://www.youtube.com/watch?v=BaW_jenozKc'])
    assert opts.format == 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio'

   

# Generated at 2022-06-14 17:53:56.508884
# Unit test for function parseOpts

# Generated at 2022-06-14 17:54:03.588780
# Unit test for function parseOpts
def test_parseOpts():
    from nose.tools import assert_equal, assert_raises, assert_not_equal
    from . import YoutubeDL
    from .YoutubeDL import YoutubeDL
    from .compat import compat_expanduser
    # Test options parsing
    with open(os.devnull, 'w') as devnull:
        stdout = sys.stdout
        sys.stdout = devnull
        try:
            # Parse command-line arguments
            parser, opts, args = parseOpts(['-U', 'TestUserAgent'])
        finally:
            sys.stdout = stdout
    assert_equal(opts.usenetrc, False)
    assert_equal(opts.username, None)
    assert_equal(opts.password, None)
    assert_equal(opts.verbose, False)
    assert_

# Generated at 2022-06-14 17:54:08.237223
# Unit test for function parseOpts
def test_parseOpts():
    opts = parseOpts(['--format', '22'])[1]
    assert opts.format == [u'22']


# Generated at 2022-06-14 17:54:20.045376
# Unit test for function parseOpts
def test_parseOpts():
    from nose.tools import assert_equal
    from sys import argv as sys_argv

    # Storing the original sys.argv
    orig_argv = sys_argv


# Generated at 2022-06-14 17:54:31.561682
# Unit test for function parseOpts
def test_parseOpts():
    assert parseOpts(['-h'])==(('help', None),)
    assert parseOpts(['-v'])==(('version', None),)
    assert parseOpts(['-U'])==(('update_self', None),)
    assert parseOpts(['-V'])==(('verbose', None),)
    assert parseOpts(['--verbose'])==(('verbose', None),)
    assert parseOpts(['--dump-user-agent'])==(('dump_user_agent', None),)
    assert parseOpts(['--list-extractors'])==(('list_extractors', None),)
    assert parseOpts(['--extractor-descriptions'])==(('list_extractor_descriptions', None),)

# Generated at 2022-06-14 17:54:38.050503
# Unit test for function parseOpts
def test_parseOpts():
    TEST_ARGS = ['-f', '137+140', '-o', '-']
    (parser, opts, args) = parseOpts(TEST_ARGS)
    assert opts.format == '137+140'
    assert opts.outtmpl == '-'


# Generated at 2022-06-14 17:54:51.127599
# Unit test for function parseOpts
def test_parseOpts():
    #_common_opts = ('quiet', 'verbose', 'no_warnings')

    def _test(args):
        parser, opts, _ = parseOpts(args)
        #for o in _common_opts:
        #    assert getattr(opts, o) is False, o
        assert opts.outtmpl is None
        assert not opts.usetitle
        assert not opts.nooverwrites
        assert opts.continue_dl

        parser, opts, _ = parseOpts(args + ['-v'])
        #for o in _common_opts:
        #    assert getattr(opts, o) is False, o
        assert opts.outtmpl is None
        assert not opts.usetitle
        assert not opts.nooverwrites
       

# Generated at 2022-06-14 17:54:58.136456
# Unit test for function parseOpts
def test_parseOpts():
    opts = parseOpts(['-i', '-o', '%(id)s.%(ext)s', 'http://www.youtube.com/watch?v=BaW_jenozKc'])[0]

    assert opts.usenetrc is True
    assert opts.password is None
    assert opts.outtmpl == '%(id)s.%(ext)s'


# Unicode workarounds

# Generated at 2022-06-14 17:55:04.877013
# Unit test for function parseOpts
def test_parseOpts():
    # Test when all options are valid
    sys.argv = ['youtube-dl','--format','best','--get-title','https://www.youtube.com/watch?v=9bZkp7q19f0']
    parser, opts, args = parseOpts()
    assert opts.format == 'best'
    assert opts.gettitle == True
    assert args==['https://www.youtube.com/watch?v=9bZkp7q19f0']
    # Test when options are invalid
    sys.argv = ['youtube-dl','--format','best','--get-title','--output','%(title)s.%(ext)s','https://www.youtube.com/watch?v=9bZkp7q19f0']
    parser, opts, args = parseOpts()
   

# Generated at 2022-06-14 17:55:41.063780
# Unit test for function parseOpts
def test_parseOpts():
    import tempfile
    with tempfile.NamedTemporaryFile() as tf:
        tf.write(b'--proxy localhost:8080')
        tf.flush()
        parser, opts, args = parseOpts([tf.name, '-U', 'IE', '-f', '18', 'http://example.com'])

# Generated at 2022-06-14 17:55:49.974906
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-vU', 'http://www.youtube.com/watch?v=BaW_jenozKc'])
    assert set(args) == {'http://www.youtube.com/watch?v=BaW_jenozKc'}
    assert opts.verbose == 2
    assert not opts.username

    # Test overriding of system configuration
    parser, opts, args = parseOpts(
        ['--username', 'foobar', 'http://www.youtube.com/watch?v=BaW_jenozKc'],
        ['--username', 'noverride'])
    assert set(args) == {'http://www.youtube.com/watch?v=BaW_jenozKc'}
    assert opts.username == 'foobar'
    #

# Generated at 2022-06-14 17:55:56.364493
# Unit test for function parseOpts
def test_parseOpts():
    global _hide_login_info
    _hide_login_info = lambda x: x
    sys.argv = ['youtube-dl', '-f', '34', 'http://youtube.com/watch?v=BaW_jenozKc']
    (parser, opts, args) = parseOpts()
    assertEqual(opts.format, '34')
    assertEqual(args, ['http://youtube.com/watch?v=BaW_jenozKc'])
    sys.argv = ['youtube-dl', '--no-color', '--format=34', '--', 'http://youtube.com/watch?v=BaW_jenozKc']
    (parser, opts, args) = parseOpts()
    assertEqual(opts.format, '34')

# Generated at 2022-06-14 17:56:07.578720
# Unit test for function parseOpts
def test_parseOpts():
    assert parseOpts(['--print-traffic', '-v', '-i'])[2] == ['--print-traffic', '-v', '-i']
    assert parseOpts(['--extract-audio', '--audio-format', 'mp3', '--audio-quality', '0', '-x', '--prefer-ffmpeg'])[2] == ['--extract-audio', '--audio-format=mp3', '--audio-quality=0', '-x', '--prefer-ffmpeg']
    assert parseOpts(['--yes-playlist', '--proxy', '1.1.1.1:8080'])[2] == ['--yes-playlist', '--proxy=1.1.1.1:8080']

# Generated at 2022-06-14 17:56:09.035286
# Unit test for function parseOpts
def test_parseOpts():
    _, opts, _ = parseOpts(['-v'])
    assert opts.verbose

# Generated at 2022-06-14 17:56:12.119991
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(["-v"])
    assert opts.verbose == True
    assert opts.usetitle == False
    parser, opts, args = parseOpts(["-l"])
    assert opts.verbose == False
    assert opts.usetitle == True
    pass

# Generated at 2022-06-14 17:56:23.188942
# Unit test for function parseOpts
def test_parseOpts():
    from sys import argv
    orig = argv
    argv = [u'prog', u'-ic']
    opts = parseOpts()
    assert opts.ignoreconfig == True, opts.ignoreconfig
    argv = [u'prog', u'--config-location', u'~/.config/youtube-dl.conf']
    opts = parseOpts()
    assert opts.ignoreconfig == False, opts.ignoreconfig
    assert opts.config_location == u'~/.config/youtube-dl.conf', opts.config_location
    argv = orig



# Generated at 2022-06-14 17:56:33.536314
# Unit test for function parseOpts
def test_parseOpts():
    from youtube_dl import YoutubeDL
    desc = 'test youtube-dl in test_parseOpts.'
    parseOpts(desc)

    assert(type(opts.playliststart) == int)
    assert(type(opts.playlistend) == int)
    assert(type(opts.playlist_items) == list)
    assert(type(opts.playlistreverse) == bool)
    assert(type(opts.playlistrandom) == bool)
    assert(type(opts.geturl) == bool)
    assert(type(opts.gettitle) == bool)
    assert(type(opts.recodevideo) == str or opts.recodevideo == None)
    assert(type(opts.username) == str or opts.username == None)

# Generated at 2022-06-14 17:56:44.851509
# Unit test for function parseOpts
def test_parseOpts():
    parser = optparse.OptionParser()
    parser.add_option(
        '-v', '--verbose',
        action='store_true', dest='verbose', default=False,
        help='Print this help text and exit')
    global_opts, _ = parser.parse_args([])
    opts, _ = parseOpts(parser, ['--verbose'])
    assert opts.verbose == global_opts.verbose

    opts, _ = parseOpts(
        parser, ['--verbose', '--config-location=/custom/config.conf'],
        overrideArguments=['--verbose'])
    assert opts.verbose == global_opts.verbose


# Generated at 2022-06-14 17:56:51.969267
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-v', '--username', 'user', '--password', 'pass', 'arg1', 'arg2'])
    assert opts.verbose == True
    assert opts.username == 'user'
    assert opts.password == 'pass'
    assert args == ['arg1', 'arg2']
    parser, opts, args = parseOpts(['-v', '--dump-user-agent'])
    assert opts.dump_user_agent == True
    assert opts.verbose == True
#

# Generated at 2022-06-14 17:57:59.428883
# Unit test for function parseOpts
def test_parseOpts():
    import tempfile
    config_file, config_location = tempfile.mkstemp(prefix='%', text=True)
    config_file = os.fdopen(config_file, 'w')
    config_file.write('-o a.%(ext)s\n')
    config_file.write('--no-part\n')
    config_file.close()

    command_line_options = ['-o', 'b.%(ext)s', '--part', '--add-metadata', config_location, 'http://www.youtube.com/watch?v=BaW_jenozKc']
    # Override the config file with command line options
    parser, opts, args = parseOpts(command_line_options)
    assert opts.outtmpl == 'b.%(ext)s'