

# Generated at 2022-06-14 17:48:35.735743
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-v'])
    assert opts.verbose

    parser, opts, args = parseOpts(['-U', 'testitos'])
    assert opts.usergroup == 'testitos'


# Generated at 2022-06-14 17:48:44.340739
# Unit test for function parseOpts
def test_parseOpts():
    from io import StringIO
    from sys import stdout
    opts, args = parseOpts(['-o', 'test.%(ext)s', 'http://example.com/'])
    assert opts.outtmpl == 'test.%(ext)s'
    assert args == ['http://example.com/']

    sys.stdout = StringIO()
    opts, args = parseOpts(['-v', '--output', 'test.%(ext)s', 'http://example.com/'])

# Generated at 2022-06-14 17:48:45.925984
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts()
    assert opts.ratelimit == '1.0M', opts.ratelimit
# parseOpts()



# Generated at 2022-06-14 17:48:59.221458
# Unit test for function parseOpts
def test_parseOpts():
    import pprint

    print('Testing parseOpts() function')
    parser, opts, args = parseOpts(
        ['--username=user', '--password=pwd', 'http://example.com/watch?v=1'])


# Generated at 2022-06-14 17:49:06.735446
# Unit test for function parseOpts
def test_parseOpts():
    # --get-filename without --no-overwrites (default) overwrites the file
    # on disk
    parser, opts, args = parseOpts(['-o', '%(title)s-%(id)s.%(ext)s',
                                    '--get-filename', 'pl', 'pl12345'])
    assert opts.no_warnings
    assert opts.outtmpl == '%(title)s-%(id)s.%(ext)s'
    assert opts.restrictfilenames
    assert opts.getfilename
    assert not opts.nooverwrites
    assert opts.usenetrc
    assert opts.verbose == 1
    assert args == ['pl12345']

    # --get-filename with --no-overwrites does not overwrite the file on

# Generated at 2022-06-14 17:49:08.080607
# Unit test for function parseOpts
def test_parseOpts():
    # TODO add code
    pass

# -- 8< -- 8< -- 8< -- 8< -- 8< -- 8< -- 8< -- 8< -- 8< --


# Generated at 2022-06-14 17:49:10.330359
# Unit test for function parseOpts
def test_parseOpts():
    try:
        import youtube_dl.extractor.test
        youtube_dl.extractor.test.test_parseOpts()
    except Exception:
        import traceback
        traceback.print_exc()
    else:
        print()
        print('parseOpts unit test successful!')



# Generated at 2022-06-14 17:49:20.852862
# Unit test for function parseOpts

# Generated at 2022-06-14 17:49:34.291542
# Unit test for function parseOpts
def test_parseOpts():
    # run with -h to print help text
    parser, opts, args = parseOpts()

#def _match_entry(info_dict, url):
#    """ Returns true if an entry in the database matches url """
#    return any(re.match(pattern, url) for pattern in info_dict['url'])

#def _get_entry(url):
#    """ Returns the dict for an entry if it exists """
#    for entry in jdb:
#        if _match_entry(entry, url):
#            return entry

#def _update_entry(url, title):
#    """ Updates an entry in the database """
#    for entry in jdb:
#        if _match_entry(entry, url):
#            entry['title'] = title
#            return

#def _add_entry(url,

# Generated at 2022-06-14 17:49:40.853867
# Unit test for function parseOpts
def test_parseOpts():
    _, opts, _ = parseOpts()
    assert '-U' in opts.ignore_config
    if sys.version_info < (3, 0):
        _, opts, _ = parseOpts(overrideArguments=[a.encode('utf-8') for a in ['-U', '--ignore-config']])
    else:
        _, opts, _ = parseOpts(overrideArguments=['-U', '--ignore-config'])
    assert '-U' not in opts.ignore_config

# Generated at 2022-06-14 17:50:04.329554
# Unit test for function parseOpts
def test_parseOpts():
    line = sys.argv[0] + ' --geturl https://www.youtube.com/watch?v=BaW_jenozKc'
    parser, opts, args = parseOpts(line.split())
    assert opts.usenetrc is True


# Generated at 2022-06-14 17:50:11.933735
# Unit test for function parseOpts
def test_parseOpts():
    argv = ['--username=testfornewparseopts', '--password=testfornewparseopts', 'https://www.youtube.com/watch?v=BaW_jenozKc']
    opts = parseOpts(argv)[1]
    assert opts.username == 'testfornewparseopts'
    assert opts.password == 'testfornewparseopts'
    assert opts.outtmpl == '%(id)s'
    assert opts.usenetrc == False
#


# Generated at 2022-06-14 17:50:21.655855
# Unit test for function parseOpts
def test_parseOpts():
    _, opts, _ = parseOpts(['-f', '22/17/best', 'myvideo'])
    assert opts.format == ['22/17/best'], 'Wrong format'
    assert opts.usenetrc == False, 'Wrong usenetrc value'
    _, opts, _ = parseOpts(['--ignore-config', '--', '--usenetrc', '--', 'myvideo'])
    assert opts.usenetrc == True, 'Wrong usenetrc value 2'
    assert opts.ignoreconfig == True, 'Wrong ignoreconfig value'
    _, opts, _ = parseOpts(['--', '--usenetrc', '--', 'myvideo'])

# Generated at 2022-06-14 17:50:34.765450
# Unit test for function parseOpts
def test_parseOpts():
    def _test_parseOpts(args, expected_opts):
        parser, opts, args = parseOpts(args)
        assert opts.__dict__ == expected_opts
        return parser
    # Test updates
    _test_parseOpts(
        ['-U', '--update'],
        {'update_self': True, 'nooverwrites': False})
    _test_parseOpts(
        ['--update'],
        {'update_self': True, 'nooverwrites': False})
    _test_parseOpts(
        ['--update', '--no-overwrites'],
        {'update_self': True, 'nooverwrites': True})

# Generated at 2022-06-14 17:50:42.800218
# Unit test for function parseOpts
def test_parseOpts():

    # Testing default
    parser, opts, args = parseOpts(None, [])

    assert opts.outtmpl == '%(title)s-%(id)s.%(ext)s'
    assert opts.ignoreerrors is False
    assert opts.forceurl is None
    assert opts.forcetitle is None
    assert opts.forcedescription is None
    assert opts.forcefilename is None
    assert opts.forceformat is None
    assert opts.forceduration is None
    assert opts.forcejson is False
    assert opts.simulate is False
    assert opts.skip_download is False
    assert opts.format is None
    assert opts.listformats is False
    assert opts.dump_single_json is False
    assert opts.dump_json is False
   

# Generated at 2022-06-14 17:50:53.334361
# Unit test for function parseOpts
def test_parseOpts():
    from sys import argv as orig_argv, exit
    from tempfile import mkstemp
    from os import remove, fdopen, environ, devnull, dup
    from os.path import exists

    def parseOpts(overrideArguments=None):
        if overrideArguments is None:
            overrideArguments = []
        if '--ignore-config' not in overrideArguments:
            overrideArguments.append('--ignore-config')
        return _real_parseOpts(overrideArguments=overrideArguments)

    def parseArgs(args):
        return parseOpts(overrideArguments=args)[1:]

    tmpfd, tmpfile = mkstemp()
    f = fdopen(tmpfd, 'w')
    f.close()
    tmpfd1, tmpfile1 = mkstemp()
    f

# Generated at 2022-06-14 17:51:04.215532
# Unit test for function parseOpts
def test_parseOpts():
  parser, opts, args = parseOpts(['-v'])
  assert opts.verbose
  parser, opts, args = parseOpts(['-c', 'x', 'y'])
  assert opts.username == 'x' and opts.password == 'y'
  parser, opts, args = parseOpts(['-c', 'x', 'y', '-c', 'x2', 'y2'])
  assert opts.username == 'x2' and opts.password == 'y2'
  parser, opts, args = parseOpts(['-c', 'x', 'y', '-c', 'x2', 'y2'], overrideArguments=['-c', 'x3', 'y3'])

# Generated at 2022-06-14 17:51:06.018544
# Unit test for function parseOpts
def test_parseOpts():
    assert isinstance(parseOpts(None), tuple)


# Generated at 2022-06-14 17:51:09.605507
# Unit test for function parseOpts
def test_parseOpts():
    # Test with empty options
    parser, opts, args = parseOpts([])
    assert(isinstance(opts, object))
    assert(isinstance(args, list))

# Generated at 2022-06-14 17:51:19.975507
# Unit test for function parseOpts
def test_parseOpts():
    from sys import argv
    for opt in [[], ['-h'], ['--version'], ['--update'], ['--help-formats'], ['--ignore-config'], ['--get-url'], [
                '--username', 'nope', '--password', 'nope', '--verbose', 'http://www.youtube.com/watch?v=BaW_jenozKc']]:
        sys.argv = [argv[0]] + opt
        (parser, opts, args) = parseOpts()
        assert opts.version or opts.update or opts.help_format or opts.ignoreconfig or opts.geturl
# End of unit test


# Generated at 2022-06-14 17:51:40.758465
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-f', '43'])
    assert opts.format == '43', opts.format
    assert args == [], args

# TODO remove when the deprecation of the --no-check-certificate flag is complete

# Generated at 2022-06-14 17:51:47.188024
# Unit test for function parseOpts
def test_parseOpts():
    import tempfile
    tmp_dir = tempfile.mkdtemp(prefix='youtube-dl-test-').decode(preferredencoding())
    tmp_file = os.path.join(tmp_dir, b'config')
    atexit.register(lambda tmp_dir: shutil.rmtree(tmp_dir, ignore_errors=True), tmp_dir)

    def _test(cmdline, expected_opts, expected_args, msg=None, conf=None, override_opts=None):
        with tempfile.NamedTemporaryFile(delete=False, dir=tmp_dir) as conf_file:
            conf_file.write(conf.encode('utf-8'))
            conf_name = conf_file.name

# Generated at 2022-06-14 17:51:48.865068
# Unit test for function parseOpts
def test_parseOpts():
    from sys import argv
    assert parseOpts() == parseOpts(argv)


# Generated at 2022-06-14 17:51:56.427901
# Unit test for function parseOpts
def test_parseOpts():
    from io import StringIO
    from .compat import compat_str, compat_urllib_error

    class FakeStringIO(StringIO):
        def close(self):
            pass

    class FakeOpener(object):
        def open(self, *args, **kwargs):
            return FakeStringIO(u'--username=bar --password=blah')

    def test_readOptions(opener, *args, **kwargs):
        return compat_str(_readOptions(*args, opener=opener, **kwargs))

    def s(*args):
        return ' '.join(args)

    assert test_readOptions(None, '-f 22') == s('-f', '22')
    assert test_readOptions(None, 'http://example.com/asdf') == s('http://example.com/asdf')
   

# Generated at 2022-06-14 17:52:08.597312
# Unit test for function parseOpts
def test_parseOpts():
    a = YoutubeDL()
    # Test if the default call to parseOpts works
    parser, opts, args = parseOpts(a.params)
    for p in parser.option_groups:
        for o in p.option_list:
            assert getattr(opts, o.dest, None) == o.default
    # Test if overrideArguments works
    parser, opts, args = parseOpts(a.params, ['-U'])
    assert opts.usenetrc == True
    assert opts.username == None
    assert opts.password == None
    parser, opts, args = parseOpts(a.params, ['--username', 'foo', '--password', 'bar'])
    assert opts.username == 'foo'
    assert opts.password == 'bar'
    # Test if --help

# Generated at 2022-06-14 17:52:15.809539
# Unit test for function parseOpts
def test_parseOpts():
    test_encoding = 'ascii'
    if hasattr(test_encoding, 'decode'):
        test_encoding = test_encoding.decode('ascii')

    parser, opts, args = parseOpts(['-o', 'lol', '--no-warnings', '--restrict-filenames', '--youtube-skip-dash-manifest', 'plop', 'http://www.youtube.com/watch?v=BaW_jenozKc'])
    assertEqual(opts.outtmpl, 'lol')
    assertEqual(opts.noplaylist, True)
    assertEqual(opts.quiet, False)
    assertEqual(opts.no_warnings, True)
    assertEqual(opts.forceurl, False)
    assertEqual

# Generated at 2022-06-14 17:52:28.172602
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-v', '--ignore-config', '-a', '/dev/null', 'http://wwww.youtube.com/watch?v=BaW_jenozKc'])
    assert opts.verbose

    parser, opts, args = parseOpts(['-i', '-v', '--username', 'foouser', '--password', 'foopass', 'http://wwww.youtube.com/watch?v=BaW_jenozKc'])
    assert opts.username == 'foouser'
    assert opts.password == 'foopass'
    assert len(opts.password) == len(_hide_password(opts.password))


# Generated at 2022-06-14 17:52:35.131739
# Unit test for function parseOpts
def test_parseOpts():
    import tempfile
    (fd, filename) = tempfile.mkstemp()

    # parseOpts(overrideArguments)
    (parser, opts, args) = parseOpts(['-f', '1', '-4', 'http://www.youtube.com/watch?v=BaW_jenozKc'])
    assert opts.usenetrc == False
    assert opts.username == None
    assert opts.password == None
    assert opts.videoformat == '1'
    assert opts.noplaylist == True

    # parseOpts(overrideArguments=None)
    (parser, opts, args) = parseOpts(None)
    assert opts.usenetrc == False
    assert opts.username == None
    assert opts.password == None

    # parseOpt

# Generated at 2022-06-14 17:52:46.629704
# Unit test for function parseOpts
def test_parseOpts():
    from youtube_dl.utils import encodeArgument
    import tempfile
    from .compat import PY2
    from .compat import get_filesystem_encoding
    if PY2:
        encoding = get_filesystem_encoding()
    else:
        encoding = None

    opts, args = parseOpts(['-U', 'Foo/1.0', '--no-check-certificate', 'pl'])
    assert opts.user_agent == 'Foo/1.0'
    assert opts.nocheckcertificate
    assert args == ['pl']

    _, tmpfilename = tempfile.mkstemp(prefix='youtube-dl-test_')


# Generated at 2022-06-14 17:52:59.669507
# Unit test for function parseOpts
def test_parseOpts():
    # When there is a config-location argument specified in the command line,
    # the argument should be parsed.
    # This test is to verify that the parsing is done correctly.
    # A test site is used since the default value for config_location is
    # '~/.config/youtube-dl/config' which can't be set by a unit test.
    parser, opts, _ = _real_main(overrideArguments=['--config-location=youtube-dl.conf', '-o', '%(autonumber)s-%(title)s.%(ext)s', 'http://www.youtube.com/watch?v=BaW_jenozKc'])
    assert opts.verbose is False

# Generated at 2022-06-14 17:53:44.188229
# Unit test for function parseOpts
def test_parseOpts():
    command_line_conf = ['-o', '%(id)s', '-o', '%(upload_date)s.%(ext)s', 'https://www.youtube.com/watch?v=BaW_jenozKc']
    parser, opts, args = parseOpts(overrideArguments = command_line_conf)
    assert opts.outtmpl == '%(id)s.%(upload_date)s.%(ext)s'
    assert args == ['https://www.youtube.com/watch?v=BaW_jenozKc']
# test_parseOpts()


# Generated at 2022-06-14 17:53:46.709731
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['--help'])  # ne marche pas
    print(parser)
    print(opts)
    print(args)

# Generated at 2022-06-14 17:53:57.648271
# Unit test for function parseOpts
def test_parseOpts():
    sys.argv = ['youtube-dl', 'http://www.youtube.com/watch?v=BaW_jenozKc']
    (parser, opts, args) = parseOpts()
    print("test_parseOpts(): opts = %s" % repr(vars(opts)))
    assert opts.verbose == False, "opts.verbose = %s" % opts.verbose
    assert opts.quiet == False, "opts.quiet = %s" % opts.quiet
    assert opts.ignoreerrors == False, "opts.ignoreerrors = %s" % opts.ignoreerrors
    assert opts.simulate == False, "opts.simulate = %s" % opts.simulate
    assert opts.format == 'best', "opts.format = %s" % opt

# Generated at 2022-06-14 17:54:07.934210
# Unit test for function parseOpts
def test_parseOpts():
    # This is a routine to test parseOpts

    opts = {
        'usenetrc': True,
        'username': 'foo', 'password': 'bar',
        'writedescription': True, 'writeannotations': True,
        'writeinfojson': True, 'writethumbnail': True,
        'outtmpl': '%(stitle)s-%(id)s-%(format)s.%(ext)s',
        'autonumber_size': 5,
        'batchfile': 'batchfile.txt'}

    args = ['url1', 'url2', 'a third url']

    # Running the test
    parser, options, args = parseOpts(opts, args)
    parser, options, args = parseOpts(None, None, overrideArguments=['-i'])

    assert v

# Generated at 2022-06-14 17:54:13.280417
# Unit test for function parseOpts
def test_parseOpts():
    cmd = ["youtube-dl", "--proxy", "localhost:8087", "http://www.youtube.com/watch?v=BaW_jenozKc"]
    ret = parseOpts(overrideArguments=cmd)
    assert ret[1].proxy == "localhost:8087", 'Proxy not set to localhost:8087'
    return True

# Generated at 2022-06-14 17:54:23.712592
# Unit test for function parseOpts
def test_parseOpts():
    assert parseOpts([])[0].format_help()
    assert parseOpts(['-h'])[0].format_help()
    assert parseOpts(['-U', 'test'])[1].username == 'test'
    assert parseOpts(['-P', 'test'])[1].password == 'test'
    assert parseOpts(['-p', 'test'])[1].playliststart == 1
    assert parseOpts(['-p', '1-2'])[1].playlistend == 2
    assert parseOpts(['-p', '1-2,4'])[1].playlist_items == ['1', '2', '4']
    assert parseOpts(['-p', '1,4-5'])[1].playlist_items == ['1', '4', '5']

# Generated at 2022-06-14 17:54:31.651282
# Unit test for function parseOpts
def test_parseOpts():
    opts1 = ['-u', 'username', '-p', 'password', '-o', '%(id)s', '-v', 'http://youtube.com/blahblah']
    parser, opts, args = parseOpts(opts1)
    assert opts.verbose == True
    assert opts.usenetrc == False
    assert opts.username == 'username'
    assert opts.password == 'password'
    assert opts.outtmpl == '%(id)s'
    assert opts.add_metadata == False

# Hide login information in a string (used for printing debugging information)

# Generated at 2022-06-14 17:54:40.066374
# Unit test for function parseOpts
def test_parseOpts():
    from io import StringIO
    from sys import stdout, stderr

    saved_stdout = stdout
    saved_stderr = stderr
    stdout = stderr = StringIO()
    try:
        assert parseOpts(['--dump-pages'])[1].dump_pages
        assert parseOpts(['-i'])[1].ignoreerrors
    finally:
        stdout = saved_stdout
        stderr = saved_stderr


# Generated at 2022-06-14 17:54:52.018394
# Unit test for function parseOpts

# Generated at 2022-06-14 17:55:02.029513
# Unit test for function parseOpts
def test_parseOpts():
    from .extractor import gen_extractor_classes
    gen_extractor_classes()
    from .utils import DEFAULT_OUTTMPL, std_headers

    # Test help
    _, _, args = parseOpts(['-h'])
    assert args == []

    _, opts, args = parseOpts([])
    assert opts.verbose is False
    assert opts.quiet is False
    assert opts.no_warnings is False
    assert opts.simulate is False
    assert opts.format == 'best'
    assert opts.listformats == []
    assert opts.outtmpl == DEFAULT_OUTTMPL
    assert opts.ignoreerrors is False
    assert opts.ratelimit == '0'
    assert opts.retries == 10
    assert opts.buffersize

# Generated at 2022-06-14 17:56:16.793582
# Unit test for function parseOpts
def test_parseOpts():
    #Test if force ip is working
    write_string('Test force ip\n')
    parser, ydl_opts, args = parseOpts(overrideArguments = ['--force-ip','109.107.33.18','https://devscripts.wordpress.com/2012/09/27/youtube-dl-a-small-python-script-to-download-videos-from-youtube-and-other-sites'])
    assert(ydl_opts.forcetube == '109.107.33.18')
    write_string('Force ip test OK\n')
    #Test if force file extension is working
    write_string('Test force file extension\n')

# Generated at 2022-06-14 17:56:26.504867
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['--verbose', '--get-url', 'https://www.youtube.com/watch?v=BaW_jenozKc'])
    assert opts.verbose
    assert opts.geturl
    assert not opts.gettitle
    assert not opts.getid
    assert not opts.getthumbnail
    assert not opts.getdescription
    assert not opts.getfilename
    assert not opts.getformat
    assert args == ['https://www.youtube.com/watch?v=BaW_jenozKc']

    parser, opts, args = parseOpts(['-v', '-g', 'https://www.youtube.com/watch?v=BaW_jenozKc'])
    assert opts.verbose

# Generated at 2022-06-14 17:56:38.664978
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, _ = parseOpts(None)
    assert opts.username is None
    assert opts.password is None
    assert opts.twofactor is None
    assert opts.videopassword is None
    assert opts.ap_username is None
    assert opts.ap_password is None
    assert opts.ap_mso is None
    assert opts.ap_mpx_account_id is None
    parser, opts, _ = parseOpts(['--username', 'user'])
    assert opts.username == 'user'
    assert opts.password is None
    assert opts.twofactor is None
    assert opts.videopassword is None

# Generated at 2022-06-14 17:56:50.591382
# Unit test for function parseOpts
def test_parseOpts():
    """
    Integration test for function 'parseOpts'
    """
    
    # Testing empty list
    testOpts = []
    parser,opts,args = parseOpts(testOpts)
    assert opts.verbose == False
    assert opts.limit_rate == None
    assert opts.nooverwrites == False
    assert opts.format == None
    
    # Testing a list of strings
    testOpts2 = ["--limit-rate","10K","--no-overwrites", "--format","mp4"]
    parser,opts,args = parseOpts(testOpts2)
    assert opts.verbose == False
    assert opts.limit_rate == "10K"
    assert opts.nooverwrites == True
    assert opts.format == "mp4"


# Generated at 2022-06-14 17:57:03.219035
# Unit test for function parseOpts
def test_parseOpts():
    import io
    import sys

    def get_option_value(opts, key):
        value = getattr(opts, key, None)
        if value is None:
            return None
        if isinstance(value, (tuple, list)):
            return list(value)
        return value

    def test(arguments, expected_options, expected_args):
        expected_options = dict((k, get_option_value(v, k)) for k, v in expected_options.items())
        parser, opts, args = parseOpts(arguments)
        options = dict((k, get_option_value(opts, k)) for k in expected_options)
        print('Test for arguments %r' % arguments)
        print('Expected options %r' % expected_options)

# Generated at 2022-06-14 17:57:04.432054
# Unit test for function parseOpts
def test_parseOpts():
    import doctest
    doctest.testmod(verbose=True)

# Generated at 2022-06-14 17:57:14.033349
# Unit test for function parseOpts
def test_parseOpts():
    t = lambda s: s.encode('utf-8') if sys.version_info[0] == 2 else s

# Generated at 2022-06-14 17:57:25.092873
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(["https://www.youtube.com/watch?v=BaW_jenozKc"])
    assert opts.output == u"%(title)s.%(ext)s"

    parser, opts, args = parseOpts(["--no-check-certificate", "https://www.youtube.com/watch?v=BaW_jenozKc"])
    assert opts.nocheckcertificate == True
    assert opts.output == u"%(title)s.%(ext)s"

    parser, opts, args = parseOpts(["--output=test.%(ext)s", "https://www.youtube.com/watch?v=BaW_jenozKc"])

# Generated at 2022-06-14 17:57:37.300597
# Unit test for function parseOpts
def test_parseOpts():
    parser, opts, args = parseOpts(['-U', '-u', 'user', '-p', 'pass'])
    assert opts.usenetrc is True
    assert opts.username == 'user'
    assert opts.password == 'pass'


    # Ensure that -i can override config files
    parser, opts, args = parseOpts(['-i', '--no-check-certificate', '--youtube-skip-dash-manifest'])
    assert opts.nocheckcertificate is True
    assert opts.youtube_skip_dash_manifest is True

    # Ensure that --extract-audio doesn't require ffmpeg/avconv
    parser, opts, args = parseOpts(['--extract-audio', '--no-post-overwrites'])

# Generated at 2022-06-14 17:57:42.746921
# Unit test for function parseOpts
def test_parseOpts():
    def check(argv, expected):
        assert expected == parseOpts(argv)[0].get_prog_name()
    check(['-h'], 'youtube-dl')
    check(['--version'], 'youtube-dl')
    check(['--help'], 'youtube-dl')
    check([], 'youtube-dl')
    check(['--restrict-filenames', '-o', '-'], 'youtube-dl')
    check(['--output', '-'], 'youtube-dl')
    check(['-o', '-'], 'youtube-dl')
    check(['-f', '134+140'], 'youtube-dl')
    check(['http://www.youtube.com/watch?v=BaW_jenozKc'], 'youtube-dl')