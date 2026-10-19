

# Generated at 2022-06-13 15:59:42.852171
# Unit test for function parsecolor
def test_parsecolor():
    values = {
        "black": u"38;5;0",
        "color0": u"38;5;0",
        "rgb111": u"38;5;16",
        "rgb222": u"38;5;28",
        "rgb333": u"38;5;54",
        "rgb123": u"38;5;18",
        "gray0": u"38;5;232",
        "gray1": u"38;5;233",
        "gray2": u"38;5;234",
        }
    for name in values:
        assert parsecolor(name) == values[name]
    for name in C.COLOR_CODES:
        assert parsecolor(name) == C.COLOR_CODES[name]

test_parsecolor()

# Generated at 2022-06-13 15:59:53.143013
# Unit test for function hostcolor
def test_hostcolor():
    name = "my.domain.example.com"
    tests = (
        {"failed": 0, "changed": 0, "unreachable": 0},  # all good
        {"failed": 1, "changed": 0, "unreachable": 0},  # 1 failure
        {"failed": 0, "changed": 1, "unreachable": 0},  # 1 change
        {"failed": 0, "changed": 0, "unreachable": 1},  # 1 unreachable
        {"failed": 1, "changed": 1, "unreachable": 0},  # 1 failure and change
        {"failed": 0, "changed": 0, "unreachable": 0},  # 1 failure and unreachable
        {"failed": 1, "changed": 0, "unreachable": 0},  # 1 change and unreachable
    )

# Generated at 2022-06-13 16:00:02.462628
# Unit test for function hostcolor
def test_hostcolor():
    def test(host, stats, color):
        assert hostcolor(host, stats) == hostcolor(host, stats, color)

    test("host1", {"failures": 0, "unreachable": 0, "changed": 0}, False)
    test("host2", {"failures": 0, "unreachable": 0, "changed": 0}, True)
    test("host3", {"failures": 0, "unreachable": 1, "changed": 0}, False)
    test("host4", {"failures": 0, "unreachable": 1, "changed": 0}, True)
    test("host5", {"failures": 0, "unreachable": 0, "changed": 1}, False)
    test("host6", {"failures": 0, "unreachable": 0, "changed": 1}, True)

# Generated at 2022-06-13 16:00:09.078526
# Unit test for function stringc
def test_stringc():
    ANSIBLE_COLOR = True
    try:
        import curses
        curses.setupterm()
        if curses.tigetnum('colors') < 0:
            ANSIBLE_COLOR = False
    except ImportError:
        # curses library was not found
        pass
    except curses.error:
        # curses returns an error (e.g. could not find terminal)
        ANSIBLE_COLOR = False
    for color in C.COLOR_CODES:
        print("%s %s" % (stringc("%s" % color, color, wrap_nonvisible_chars=True), color))
        if ANSIBLE_COLOR:
            print("%s %s" % (stringc("%s" % color, color, wrap_nonvisible_chars=False), color))

# Generated at 2022-06-13 16:00:19.112889
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor('red') == '31'
    assert parsecolor('color1') == '38;5;1'
    assert parsecolor('color15') == '38;5;15'
    assert parsecolor('color16') == '38;5;16'
    assert parsecolor('color255') == '38;5;255'
    assert parsecolor('color256') is None
    assert parsecolor('rgb123') == '38;5;39'
    assert parsecolor('rgb321') == '38;5;197'
    assert parsecolor('rgb333') == '38;5;231'
    assert parsecolor('rgb444') == '38;5;254'
    assert parsecolor('rgb555') is None

# Generated at 2022-06-13 16:00:29.907730
# Unit test for function hostcolor
def test_hostcolor():
    host = 'localhost'
    stats = dict(changed=0, failures=0, unreachable=0, skipped=0, ok=0)
    assert hostcolor(host, stats, color=True) == stringc(host, C.COLOR_OK)
    assert hostcolor(host, stats, color=False) == host

    stats = dict(changed=1, failures=0, unreachable=0, skipped=0, ok=0)
    assert hostcolor(host, stats, color=True) == stringc(host, C.COLOR_CHANGED)
    assert hostcolor(host, stats, color=False) == host

    stats = dict(changed=0, failures=0, unreachable=1, skipped=0, ok=0)
    assert hostcolor(host, stats, color=True) == stringc(host, C.COLOR_ERROR)

# Generated at 2022-06-13 16:00:34.312462
# Unit test for function colorize
def test_colorize():
    for C in ('black', 'red', 'green', 'yellow', 'blue', 'purple', 'cyan', 'white'):
        print('%-9s' % C, colorize('VAR', 7, C))



# Generated at 2022-06-13 16:00:40.834950
# Unit test for function stringc
def test_stringc():
    assert stringc('test', 'normal') == 'test'
    assert stringc('test', 'black') == '\033[30mtest\033[0m'
    assert stringc('test', 'green') == '\033[32mtest\033[0m'
    assert stringc('test', '0') == '\033[30mtest\033[0m'
    assert stringc('test', 'rgb255255255') == '\033[97mtest\033[0m'



# Generated at 2022-06-13 16:00:42.689059
# Unit test for function stringc
def test_stringc():
    print(stringc("hello", "brown", wrap_nonvisible_chars=True))
# --- end "pretty"



# Generated at 2022-06-13 16:00:48.628170
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor("foobar.example.org", dict(skipped=1, ok=1, failures=2, unreachable=0, changed=3)) == stringc("foobar.example.org", C.COLOR_CHANGED)
    assert hostcolor("foobar.example.org", dict(skipped=1, ok=1, failures=2, unreachable=3, changed=0)) == stringc("foobar.example.org", C.COLOR_ERROR)
    assert hostcolor("foobar.example.org", dict(skipped=1, ok=1, failures=0, unreachable=0, changed=0)) == stringc("foobar.example.org", C.COLOR_OK)

# Generated at 2022-06-13 16:01:03.952540
# Unit test for function stringc

# Generated at 2022-06-13 16:01:15.234510
# Unit test for function hostcolor
def test_hostcolor():
    if C.ANSIBLE_NOCOLOR:
        assert hostcolor("test", {'failures': 0, 'unreachable': 0, 'changed': 0}) == u"test               "
        assert hostcolor("test", {'failures': 2, 'unreachable': 0, 'changed': 0}) == u"test               "
        assert hostcolor("test", {'failures': 0, 'unreachable': 0, 'changed': 1}) == u"test               "
        assert hostcolor("test", {'failures': 0, 'unreachable': 1, 'changed': 0}) == u"test               "
    else:
        assert hostcolor("test", {'failures': 0, 'unreachable': 0, 'changed': 0}) == u"test                          "

# Generated at 2022-06-13 16:01:21.378680
# Unit test for function hostcolor
def test_hostcolor():
    print(hostcolor('www1.example.com', {'failures': 0, 'unreachable': 0, 'changed': 0}))
    print(hostcolor('www2.example.com', {'failures': 0, 'unreachable': 0, 'changed': 1}))
    print(hostcolor('www3.example.com', {'failures': 0, 'unreachable': 1, 'changed': 0}))
    print(hostcolor('www4.example.com', {'failures': 1, 'unreachable': 0, 'changed': 0}))
    print(hostcolor('www5.example.com', {'failures': 1, 'unreachable': 1, 'changed': 1}))

# --- end of "pretty"



# Generated at 2022-06-13 16:01:31.500440
# Unit test for function stringc
def test_stringc():
    import ansible.utils.color as c
    from ansible.utils.color import stringc
    from ansible.utils.color import ANSIBLE_COLOR
    from ansible.utils.color import parsecolor

    ANSIBLE_COLOR = True  # force on for these tests

    print("%-20s: %s" % ("Input String", "Output String"))
    print("%-20s- %s" % ("-"*20, "-"*20))
    print("%-20s: %s" % ("'Hello World'", stringc("Hello World", "GREEN")))
    print("%-20s: %s" % ("'Hello World'", stringc("Hello World", "0;32")))

    print("%-20s: %s" % ("parsecolor('green')", parsecolor("green")))

# Generated at 2022-06-13 16:01:36.006985
# Unit test for function stringc
def test_stringc():
    """Test ANSI color string wrapper"""

    assert stringc("foo", "red", False) == "\033[31mfoo\033[0m"
    assert stringc("bar", "blue", False) == "\033[34mbar\033[0m"
    assert stringc("baz", "green", False) == "\033[32mbaz\033[0m"
    assert stringc("blah", "purple", False) == "\033[35mblah\033[0m"

# end "pretty"
# ---

# Generated at 2022-06-13 16:01:47.176496
# Unit test for function colorize

# Generated at 2022-06-13 16:01:57.938085
# Unit test for function colorize
def test_colorize():
    # Color codes dict
    codes = dict(list(C.COLOR_CODES.items()) + list({
        'black':   "0;30",
        'red':     "0;31",
        'green':   "0;32",
        'yellow':  "0;33",
        'blue':    "0;34",
        'magenta': "0;35",
        'cyan':    "0;36",
        'white':   "0;37",
        'default': "0;39",
    }.items()))
    # SGR parameters used
    used = set()
    # Loop through all the codes

# Generated at 2022-06-13 16:02:04.785609
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor("localhost", {'ok': 1, 'changed': 0, 'unreachable': 0, 'failures': 0, 'skipped': 0}) == u"localhost                  "
    assert hostcolor("localhost", {'ok': 1, 'changed': 0, 'unreachable': 0, 'failures': 1, 'skipped': 0}) == u"localhost                  "
    assert hostcolor("localhost", {'ok': 1, 'changed': 0, 'unreachable': 0, 'failures': 2, 'skipped': 0}) == u"localhost                  "
    assert hostcolor("localhost", {'ok': 1, 'changed': 1, 'unreachable': 0, 'failures': 0, 'skipped': 0}) == u"localhost                  "


# Generated at 2022-06-13 16:02:14.816398
# Unit test for function colorize
def test_colorize():
    from ansible.utils.display import Display

    display = Display()
    for color in ('normal', 'bold red', 'on_red',
                  'from_file black bold on_magenta', 'from_file yellow',
                  'from_file underline cyan', 'underline from_file cyan'):
        print(display.colorize('foo', color))

    print('Colorizing numbers...')
    for pct in range(-11, 120, 10):
        if pct < 0:
            color = None
        elif pct < 50:
            color = 'green'
        elif pct < 90:
            color = 'yellow'
        else:
            color = 'red'
        print('%5d%% is %s' % (pct, display.colorize(pct, color, '%')))

# end "

# Generated at 2022-06-13 16:02:25.595028
# Unit test for function hostcolor
def test_hostcolor():
    stats = {'failures': 0, 'unreachable': 0, 'changed': 0}
    assert (hostcolor('localhost', stats, True) == u'localhost'.ljust(37, ' '))

    stats = {'failures': 1, 'unreachable': 1, 'changed': 0}
    assert (hostcolor('localhost', stats, True) == u'\x1b[31mlocalhost\x1b[0m'.ljust(37, ' '))

    stats = {'failures': 0, 'unreachable': 0, 'changed': 1}
    assert (hostcolor('localhost', stats, True) == u'\x1b[33mlocalhost\x1b[0m'.ljust(37, ' '))

    assert (hostcolor('localhost', stats, False) == u'localhost              ')



# Generated at 2022-06-13 16:02:42.473946
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor("TEST.example.com", dict(failures=1, unreachable=0, changed=0)) == u"TEST.example.com             "
    assert hostcolor("TEST.example.com", dict(failures=0, unreachable=0, changed=0)) == u"TEST.example.com             "
    assert hostcolor("TEST.example.com", dict(failures=0, unreachable=2, changed=0)) == u"TEST.example.com             "
    assert hostcolor("TEST.example.com", dict(failures=0, unreachable=0, changed=2)) == u"TEST.example.com             "



# Generated at 2022-06-13 16:02:43.889577
# Unit test for function stringc
def test_stringc():
    # FIXME: add assert and tests...
    pass
# --- end "pretty" ---

# Generated at 2022-06-13 16:02:55.263921
# Unit test for function stringc
def test_stringc():
    correct = "\033[38;5;%dm%s\033[0m"
    assert parsecolor("green") == "32"
    assert parsecolor("dark gray") == "38;5;232"
    assert parsecolor("color1") == "38;5;1"
    assert parsecolor("rgb000") == "38;5;16"
    assert parsecolor("rgb555") == "38;5;7"
    assert parsecolor("rgb444") == "38;5;234"
    assert parsecolor("rgb321") == "38;5;38"

    assert stringc("hello", "green") == correct % 32 + "hello" + correct % 0
    assert stringc("hello", "dark gray") == correct % 232 + "hello" + correct % 0

# Generated at 2022-06-13 16:03:05.194135
# Unit test for function stringc
def test_stringc():
    """Tests for stringc()."""

    def _test(text, color):
        """Test that stringc(text, color) equals the expected string."""
        expected = text
        if ANSIBLE_COLOR:
            expected = "\033[%sm%s\033[0m" % (parsecolor(color), text)
        if not (stringc(text, color) == expected):
            raise AssertionError("stringc(%r, %r) != %r" % (text, color, expected))

    _test("foo", "black")
    _test("foo", u"color0")
    _test("foo", "grey")
    _test("foo", "white")
    _test("foo", u"color15")
    _test("foo", "red")

# Generated at 2022-06-13 16:03:10.623259
# Unit test for function hostcolor
def test_hostcolor():
    host = "localhost"
    stats = {'changed': 0, 'unreachable': 1, 'failures': 0}
    print(hostcolor(host, stats, True))

    stats = {'changed': 0, 'unreachable': 0, 'failures': 0}
    print(hostcolor(host, stats, True))

    stats = {'changed': 1, 'unreachable': 0, 'failures': 0}
    print(hostcolor(host, stats, True))

# Generated at 2022-06-13 16:03:21.911156
# Unit test for function hostcolor
def test_hostcolor():
    class Test(object):
        name = 'test'

    stats = Test()
    stats.failures = 0
    stats.unreachable = 0
    stats.changed = 0

    # success
    assert hostcolor('test', stats) == u"%-26s" % 'test'

    # changed
    stats.changed = 1
    assert hostcolor('test', stats) == u"%-37s" % stringc('test', C.COLOR_CHANGED)

    # unreachable
    stats.changed = 0
    stats.unreachable = 1
    assert hostcolor('test', stats) == u"%-37s" % stringc('test', C.COLOR_ERROR)

    # failures
    stats.unreachable = 0
    stats.failures = 1

# Generated at 2022-06-13 16:03:29.447551
# Unit test for function hostcolor
def test_hostcolor():
    stats = dict(ok=1, changed=0, unreachable=0, failures=0)
    print(u"expect green:", end=u" ")
    print(hostcolor(u"some_host", stats, True))
    stats = dict(ok=0, changed=0, unreachable=0, failures=1)
    print(u"expect red:", end=u" ")
    print(hostcolor(u"some_host", stats, True))
    stats = dict(ok=0, changed=1, unreachable=0, failures=0)
    print(u"expect yellow:", end=u" ")
    print(hostcolor(u"some_host", stats, True))
    stats = dict(ok=0, changed=0, unreachable=5, failures=0)

# Generated at 2022-06-13 16:03:36.986515
# Unit test for function parsecolor
def test_parsecolor():
    for color in 'black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21':
        print(stringc('  %-10s ' % color, color))

# Generated at 2022-06-13 16:03:44.805083
# Unit test for function stringc
def test_stringc():
    try:
        import curses
        curses.setupterm()
        if curses.tigetnum('colors') < 0:
            raise unittest.SkipTest("Terminal doesn't support colors, skipping")
    except ImportError:
        raise unittest.SkipTest("Curses library not found, skipping")
    except curses.error:
        raise unittest.SkipTest("Failed to initialize terminal to get number of colors, skipping")

    # Test regular colors
    assert stringc("ERROR", "ERROR") == "\033[31mERROR\033[0m"
    assert stringc("OK", "OK") == "\033[32mOK\033[0m"
    assert stringc("WARN", "WARN") == "\033[33mWARN\033[0m"

# Generated at 2022-06-13 16:03:52.945893
# Unit test for function stringc
def test_stringc():
    """
    Basic unit test for function stringc
    Checks following cases:
        - color string representation is returned when ANSIBLE_COLOR is True
        - empty string is returned when ANSIBLE_COLOR is False
        - color string representation is returned with the non-visible chars
          wrap option if ANSIBLE_COLOR is True
    """
    color = 'blue'
    text = u'foo'
    ANSIBLE_COLOR = True
    assert stringc(text, color) == u'\x1b[34mfoo\x1b[0m'
    ANSIBLE_COLOR = False
    assert stringc(text, color) == u''
    ANSIBLE_COLOR = True

# Generated at 2022-06-13 16:04:04.296963
# Unit test for function stringc
def test_stringc():
    # Default foreground color test
    assert '\x1b[0;31mfoo\x1b[0m' == stringc('foo', 'red')
    # Default background color test
    assert '\x1b[0;41mbar\x1b[0m' == stringc('bar', 'on_red')
    # Custom color test
    assert '\x1b[0;38;5;202mqux\x1b[0m' == stringc('qux', 'rgb520')



# Generated at 2022-06-13 16:04:09.442067
# Unit test for function parsecolor
def test_parsecolor():
    # basic colors
    assert parsecolor("white") == "0"
    assert parsecolor("black") == "30"
    assert parsecolor("red") == "31"
    assert parsecolor("green") == "32"
    assert parsecolor("blue") == "34"
    # bright colors
    assert parsecolor("brightred") == "91"
    assert parsecolor("brightgreen") == "92"
    assert parsecolor("brightblue") == "94"
    # xterm color numbers
    assert parsecolor("color2") == "38;5;2"
    assert parsecolor("color26") == "38;5;26"
    assert parsecolor("color186") == "38;5;186"
    # xterm color rgb

# Generated at 2022-06-13 16:04:11.414779
# Unit test for function stringc
def test_stringc():
    stringc('test', color='red')
# --- end "pretty"



# Generated at 2022-06-13 16:04:23.295482
# Unit test for function stringc

# Generated at 2022-06-13 16:04:33.048785
# Unit test for function hostcolor

# Generated at 2022-06-13 16:04:40.685281
# Unit test for function hostcolor
def test_hostcolor():
    u"""Test hostcolor function"""
    tty_stats = {'ok': 10, 'failures': 0, 'dark': 0, 'changed': 0, 'skipped': 0, 'unreachable': 0}
    assert "testhost            " == hostcolor("testhost", tty_stats, color=False)
    assert 'testhost            ' == hostcolor("testhost", tty_stats, color=False)
    assert u'\033[38;5;76mt-est\x08hos-\x1b[0m' == hostcolor(u"t\x08hos", tty_stats, color=True)



# Generated at 2022-06-13 16:04:46.920557
# Unit test for function parsecolor
def test_parsecolor():
    print(parsecolor('red') == '38;5;160')
    print(parsecolor('black') == '38;5;16')
    print(parsecolor('blue') == '38;5;21')
    print(parsecolor('cyan') == '38;5;14')
    print(parsecolor('green') == '38;5;28')
    print(parsecolor('magenta') == '38;5;201')
    print(parsecolor('yellow') == '38;5;226')
    print(parsecolor('white') == '38;5;231')
    print(parsecolor('rgb255255255') == '38;5;231')
    print(parsecolor('rgb000255000') == '38;5;40')

# Generated at 2022-06-13 16:04:57.157617
# Unit test for function stringc
def test_stringc():
    assert stringc(u"foo", "red") == u"\033[31mfoo\033[0m"
    assert stringc(u"foo", "blue") == u"\033[34mfoo\033[0m"
    assert stringc(u"foo", "on_red") == u"\033[41mfoo\033[0m"
    assert stringc(u"foo", "on_blue") == u"\033[44mfoo\033[0m"
    assert stringc(u"foo", "red", True) == u"\001\033[31m\002foo\001\033[0m\002"
    assert stringc(u"foo", "blue", True) == u"\001\033[34m\002foo\001\033[0m\002"

# Generated at 2022-06-13 16:05:09.408650
# Unit test for function stringc

# Generated at 2022-06-13 16:05:19.415310
# Unit test for function colorize
def test_colorize():
    cdict = {
        'green': '\033[32m',
        'blue': '\033[34m',
        'yellow': '\033[33m',
        'red': '\033[31m',
        'end': '\033[0m',
        'bold': '\033[1m',
        'underline': '\033[4m',
    }

    s = colorize('>>', 'OK', 'green')
    assert u'\x1b[32m>>=OK\x1b[0m' == s or '%s>>=OK%s' % (cdict['green'], cdict['end']) == s
    s = colorize('>>', 'WARNING', 'yellow')
    assert u'\x1b[33m>>=WARNING\x1b[0m' == s

# Generated at 2022-06-13 16:05:44.083772
# Unit test for function stringc
def test_stringc():
    assert stringc("foo", "green") == u"\033[32mfoo\033[0m"
    assert stringc("foo", "color1") == u"\033[38;5;1mfoo\033[0m"
    assert stringc("foo", "rgb255") == u"\033[38;5;231mfoo\033[0m"
    assert stringc("foo", "gray10") == u"\033[38;5;250mfoo\033[0m"
    assert stringc("foo", "none") == u"foo"
    assert stringc("foo", "this color doesn't exist") == u"foo"
    assert stringc("foo\nbar", "green") == u"\033[32mfoo\nbar\033[0m"

# Generated at 2022-06-13 16:05:47.505883
# Unit test for function stringc
def test_stringc():
    assert stringc("test", "black") == u"\033[30mtest\033[0m"
    assert stringc("test", "red", wrap_nonvisible_chars=True) == u"\001\033[38;5;095m\002test\001\033[0m\002"

# Generated at 2022-06-13 16:05:58.515190
# Unit test for function hostcolor
def test_hostcolor():
    host = 'host'
    stats = {'failures': 0, 'unreachable': 0, 'changed': 0}
    assert hostcolor(host, stats) == u"%-37s" % host
    stats = {'failures': 1, 'unreachable': 0, 'changed': 0}
    assert hostcolor(host, stats) == u"%-37s" % stringc('host', C.COLOR_ERROR)
    stats = {'failures': 0, 'unreachable': 1, 'changed': 0}
    assert hostcolor(host, stats) == u"%-37s" % stringc('host', C.COLOR_ERROR)
    stats = {'failures': 0, 'unreachable': 0, 'changed': 1}

# Generated at 2022-06-13 16:06:06.882353
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor('red') == u'38;5;9'
    assert parsecolor('lightred') == u'38;5;9'
    assert parsecolor('darkred') == u'38;5;1'
    assert parsecolor('0') == u'38;5;0'
    assert parsecolor('1') == u'38;5;1'
    assert parsecolor('2') == u'38;5;2'
    assert parsecolor('3') == u'38;5;3'
    assert parsecolor('4') == u'38;5;4'
    assert parsecolor('5') == u'38;5;5'
    assert parsecolor('6') == u'38;5;6'
    assert parsecolor('7') == u'38;5;7'

# Generated at 2022-06-13 16:06:17.174403
# Unit test for function parsecolor
def test_parsecolor():
    def test_colorize_color(color_code, color, wrap_nonvisible_chars=False):
        output = stringc(u"string", color, wrap_nonvisible_chars=wrap_nonvisible_chars)
        assert output == u"\033[%smstring\033[0m" % color_code
        output = stringc(u"string\nstring", color, wrap_nonvisible_chars=wrap_nonvisible_chars)
        assert output == u"\033[%smstring\033[0m\n\033[%smstring\033[0m" % (color_code, color_code)

    def test_colors(color_code, color):
        test_colorize_color(color_code, color)
        test_colorize_color(color_code, color)

    test_

# Generated at 2022-06-13 16:06:26.950991
# Unit test for function stringc
def test_stringc():
    assert stringc(u"hello", u"blue", False) == u"\033[34mhello\033[0m"
    assert stringc(u"hello\nworld", u"blue", False) == u"\033[34mhello\033[0m\n\033[34mworld\033[0m"
    assert stringc(u"hello", u"color10", False) == u"\033[38;5;10mhello\033[0m"
    assert stringc(u"hello", u"rgb222", False) == u"\033[38;5;82mhello\033[0m"
    assert stringc(u"hello", u"rgb200", False) == u"\033[38;5;76mhello\033[0m"

# Generated at 2022-06-13 16:06:37.184593
# Unit test for function stringc
def test_stringc():
    C.COLOR_NONE = None
    assert stringc("text", "black") == u'\033[30mtext\033[0m'
    assert stringc("text", "bold black") == u'\033[1;30mtext\033[0m'
    assert stringc("text", "underline black") == u'\033[4;30mtext\033[0m'
    assert stringc("text", "inverse black") == u'\033[7;30mtext\033[0m'
    assert stringc("text", "bg-black") == u'\033[40mtext\033[0m'
    assert stringc("text", "bg-bold black") == u'\033[1;40mtext\033[0m'

# Generated at 2022-06-13 16:06:45.538508
# Unit test for function hostcolor
def test_hostcolor():
    stats = dict(failures=0, unreachable=0, changed=0)
    assert hostcolor('foo', stats) == "%-37s" % "foo"
    stats = dict(failures=1, unreachable=0, changed=0)
    assert hostcolor('foo', stats) == "%-37s" % stringc("foo", C.COLOR_ERROR)
    stats = dict(failures=0, unreachable=1, changed=0)
    assert hostcolor('foo', stats) == "%-37s" % stringc("foo", C.COLOR_ERROR)
    stats = dict(failures=0, unreachable=0, changed=1)
    assert hostcolor('foo', stats) == "%-37s" % stringc("foo", C.COLOR_CHANGED)

# Generated at 2022-06-13 16:06:46.808191
# Unit test for function colorize
def test_colorize():
    pass


# --- end of "pretty" ---


# Generated at 2022-06-13 16:06:56.807620
# Unit test for function stringc
def test_stringc():
    ''' test stringc function '''
    test_str = "test string"
    cur_color = ANSIBLE_COLOR
    color_codes = C.COLOR_CODES

# Generated at 2022-06-13 16:07:34.420536
# Unit test for function hostcolor
def test_hostcolor():
    from ansible.callbacks.default import CallbackModule
    stats = CallbackModule()
    stats.set_host_var('testhost', 'ansible_ssh_host', '10.20.30.40')
    stats.set_host_var('testhost', 'ansible_ssh_port', '22')

    for failed_hosts in [[], [('testhost', 100)], [('testhost', 101)], [('testhost', 200)]]:
        stats.failures += failed_hosts
        stats.unreachable += failed_hosts

        for changed_hosts in [[], [('testhost', 100)], [('testhost', 101)], [('testhost', 200)]]:
            stats.changed += changed_hosts
            stats.failed_when_result += changed_hosts

            # We are forcing all parameters since

# Generated at 2022-06-13 16:07:41.304852
# Unit test for function stringc
def test_stringc():
    print("Testing function stringc")
    # TODO: unittest this
    print("- ansible_color is %s" % ANSIBLE_COLOR)
    print("- ANSIBLE_NOCOLOR is %s" % C.ANSIBLE_NOCOLOR)
    print("- ANSIBLE_FORCE_COLOR is %s, %s, %s" % (C.ANSIBLE_FORCE_COLOR, type(C.ANSIBLE_FORCE_COLOR), C.ANSIBLE_FORCE_COLOR))
    print("- ANSIBLE_COLOR is %s, %s, %s" % (ANSIBLE_COLOR, type(ANSIBLE_COLOR), ANSIBLE_COLOR))

# Generated at 2022-06-13 16:07:45.839725
# Unit test for function hostcolor
def test_hostcolor():
    from ansible.compat.six import b
    """ Test host color functions """
    fake_stdout = b('abcdefg')
    (out, err) = capsys.readouterr()
    assert out == b'abcdefg'



# Generated at 2022-06-13 16:07:55.700324
# Unit test for function hostcolor
def test_hostcolor():
    given_data = {'failures': 0, 'unreachable': 0, 'ok': 1, 'skipped': 0, 'changed': 1}
    assert hostcolor(u"test.example.org", given_data, True) == u"%-37s" % stringc("test.example.org", C.COLOR_CHANGED)
    given_data = {'failures': 0, 'unreachable': 0, 'ok': 1, 'skipped': 0, 'changed': 0}
    assert hostcolor(u"test.example.org", given_data, True) == u"%-37s" % stringc("test.example.org", C.COLOR_OK)
    given_data = {'failures': 1, 'unreachable': 0, 'ok': 0, 'skipped': 0, 'changed': 0}
    assert host

# Generated at 2022-06-13 16:08:05.923988
# Unit test for function hostcolor
def test_hostcolor():
    good = { "ok": 10, "changed": 0, "unreachable": 0, "failures": 0 }
    bad = { "ok": 0, "changed": 0, "unreachable": 4, "failures": 10 }
    warn = { "ok": 10, "changed": 4, "unreachable": 0, "failures": 0 }

    assert '\x1b[' not in hostcolor("localhost", good)
    assert '\x1b[' not in hostcolor("localhost", good, color=False)

    assert '\x1b[0;31m' in hostcolor("localhost", bad)
    assert '\x1b[0;31m' not in hostcolor("localhost", bad, color=False)

    assert '\x1b[0;33m' in hostcolor("localhost", warn)

# Generated at 2022-06-13 16:08:09.616297
# Unit test for function stringc
def test_stringc():
    def f(s):
        return s

    def g(s):
        return ansible.utils.stringc(s, 'blue')

    text = ("foo", "bar", "baz")
    assert [f(s) for s in text] == [g(s) for s in text]



# Generated at 2022-06-13 16:08:20.217175
# Unit test for function stringc

# Generated at 2022-06-13 16:08:29.783523
# Unit test for function hostcolor
def test_hostcolor():
    colorize_func = hostcolor

    results = dict(
        successes=0,
        skipped=0,
        failed=0,
        unreachable=0,
        changed=0,
        dark=0)

    results_dict = dict(
        successes=dict(color=C.COLOR_OK),
        skipped=dict(color=C.COLOR_SKIP),
        failed=dict(color=C.COLOR_ERROR),
        unreachable=dict(color=C.COLOR_UNREACHABLE),
        changed=dict(color=C.COLOR_CHANGED),
        dark=dict(color=None))

    # Create a new colorize function without ANSIBLE_COLOR
    global ANSIBLE_COLOR
    ANSIBLE_COLOR = False

    host = "testhost"


# Generated at 2022-06-13 16:08:37.743964
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('host', dict(failed=0, unreachable=0, changed=0)) == u"%-37s" % hostcolor('host', dict(failed=0, unreachable=0, changed=0))
    assert hostcolor('host', dict(failed=1, unreachable=0, changed=0)) == u"%-37s" % hostcolor('host', dict(failed=1, unreachable=0, changed=0))
    assert hostcolor('host', dict(failed=0, unreachable=1, changed=0)) == u"%-37s" % hostcolor('host', dict(failed=0, unreachable=1, changed=0))

# Generated at 2022-06-13 16:08:47.116005
# Unit test for function stringc
def test_stringc():

    assert stringc(u"foo", u"red") == u"\x1b[31mfoo\x1b[0m"
    assert stringc(u"foo", u"rEd") == u"\x1b[31mfoo\x1b[0m"
    assert stringc(u"foo", u"red", wrap_nonvisible_chars=True) == u"\x01\x1b[31m\x02foo\x01\x1b[0m\x02"

    # Test some valid `color` values
    assert stringc(u"foo", u"blue") == u"\x1b[34mfoo\x1b[0m"