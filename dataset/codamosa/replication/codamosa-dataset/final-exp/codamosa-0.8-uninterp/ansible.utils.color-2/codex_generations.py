

# Generated at 2022-06-13 15:59:41.437707
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('localhost', dict(changed=2, unreachable=0, failures=0)) == u"localhost                "
    assert hostcolor('localhost', dict(changed=0, unreachable=0, failures=0)) == u"localhost                "
    assert hostcolor('localhost', dict(changed=0, unreachable=1, failures=0)) == u"localhost                "
    assert hostcolor('localhost', dict(changed=0, unreachable=0, failures=1)) == u"localhost                "


# Generated at 2022-06-13 15:59:52.237650
# Unit test for function colorize
def test_colorize():
    from nose.tools import assert_equals
    assert_equals(colorize('foo', 0, 'black'), 'foo=0   \033[30m\033[0m')
    assert_equals(colorize('\x1b[31mfoo', 0, 'black'), '\x1b[31mfoo=0  \033[30m\033[0m')
    assert_equals(colorize('foo\033[0m', 0, 'black'), 'foo\033[0m=0  \033[30m\033[0m')
    assert_equals(colorize('foo=0', 0, 'black'), 'foo=0  \033[30m\033[0m')

# Generated at 2022-06-13 15:59:55.893647
# Unit test for function stringc
def test_stringc():
    print('Test function stringc:')
    for color in C.COLOR_CODES:
        print('  %s' % stringc('This is color "%s"' % color, color))


# Generated at 2022-06-13 16:00:04.291246
# Unit test for function hostcolor
def test_hostcolor():
    # Make sure that we print something no matter what
    assert hostcolor('foo', {}) != ''
    # Make sure that color is always false on Windows
    if sys.platform == 'win32':
        assert hostcolor('foo', {}, color=True) == hostcolor('foo', {}, color=False)
    assert hostcolor('foo', {}) == '%-26s' % 'foo'
    assert hostcolor('foo', {}) == '%-26s' % 'foo'
    assert hostcolor('foo', {'dark': 'magic'}) == '%-26s' % 'foo'
    assert hostcolor('foo', {'dark': 'magic'}) == '%-26s' % 'foo'
    assert hostcolor('foo', {'dark': 'magic'}) == '%-26s' % 'foo'
    # These tests depend on ANS

# Generated at 2022-06-13 16:00:10.229889
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor("color0") == u"38;5;0"
    assert parsecolor("color1") == u"38;5;1"
    assert parsecolor("color2") == u"38;5;2"
    assert parsecolor("color8") == u"38;5;8"
    assert parsecolor("color9") == u"38;5;9"
    assert parsecolor("color15") == u"38;5;15"
    assert parsecolor("color16") == u"38;5;16"
    assert parsecolor("color17") == u"38;5;17"
    assert parsecolor("color231") == u"38;5;231"
    assert parsecolor("color232") == u"38;5;232"
    assert parsecolor("color233")

# Generated at 2022-06-13 16:00:20.059337
# Unit test for function colorize
def test_colorize():
    try:
        import curses
        curses.setupterm()
        if curses.tigetnum('colors') < 0:
            ANSIBLE_COLOR = False
    except ImportError:
        # curses library was not found
        ANSIBLE_COLOR = False
    except curses.error:
        # curses returns an error (e.g. could not find terminal)
        ANSIBLE_COLOR = False
    if ANSIBLE_COLOR:
        assert colorize('ok', 0, 'green') == 'ok=0   '
        assert colorize('changed', 0, 'yellow') == 'changed=0   '
        assert colorize('darkred', 0, 'darkred') == 'darkred=0  '
        assert colorize('fail', 0, 'red') == 'fail=0    '

# Generated at 2022-06-13 16:00:27.777989
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor("RED") == u'31'
    assert parsecolor("GREEN") == u'32'
    assert parsecolor("yellow") == u'33'
    assert parsecolor("blue") == u'34'
    assert parsecolor("magenta") == u'35'
    assert parsecolor("cyan") == u'36'
    assert parsecolor("WHITE") == u'37'
    assert parsecolor("color0") == u'38;5;0'
    assert parsecolor("color1") == u'38;5;1'
    assert parsecolor("color2") == u'38;5;2'
    assert parsecolor("color3") == u'38;5;3'
    assert parsecolor("color4") == u'38;5;4'
    assert par

# Generated at 2022-06-13 16:00:34.880022
# Unit test for function parsecolor
def test_parsecolor():
    tests = {
        "color0": "38;5;0",
        "color1": "38;5;1",
        "color9": "38;5;9",
        "color10": "38;5;10",
        "color15": "38;5;15",
        "color16": "38;5;16",
        "color21": "38;5;21",
        "rgb000": "38;5;16",
        "rgb555": "38;5;23",
        "rgb555": "38;5;23",
        "rgb333": "38;5;59",
        "gray0": "38;5;232",
        "gray24": "38;5;255",
        "yellow": "33",
        "bold yellow": "33;01",
    }

# Generated at 2022-06-13 16:00:44.073790
# Unit test for function stringc

# Generated at 2022-06-13 16:00:47.791924
# Unit test for function hostcolor
def test_hostcolor():
    # If ANSIBLE_COLOR is False, don't colorize
    ANSIBLE_COLOR = False
    assert hostcolor(u"localhost", {}) == u"localhost                "
    assert hostcolor(u"localhost", {}, False) == u"localhost                "
    assert hostcolor(u"localhost", {}, True) == u"localhost                "

    # If color is False, don't colorize
    ANSIBLE_COLOR = True
    assert hostcolor(u"localhost", {}, False) == u"localhost                "
    assert hostcolor(u"localhost", {}, True) == u"\033[0;32mlocalhost\033[0m     "



# Generated at 2022-06-13 16:00:53.704212
# Unit test for function colorize
def test_colorize():
    pass
# --- end of "pretty"



# Generated at 2022-06-13 16:01:04.594343
# Unit test for function parsecolor
def test_parsecolor():
    if ANSIBLE_COLOR:
        u"\033[%sm%s\033[0m" % (parsecolor("green"), "GREEN")
        u"\033[%sm%s\033[0m" % (parsecolor("bright green"), "BRIGHT GREEN")
        u"\033[%sm%s\033[0m" % (parsecolor("bold green"), "BOLD GREEN")
        u"\033[%sm%s\033[0m" % (parsecolor("yellow"), "YELLOW")
        u"\033[%sm%s\033[0m" % (parsecolor("bright yellow"), "BRIGHT YELLOW")
        u"\033[%sm%s\033[0m" % (parsecolor("red"), "RED")

# Generated at 2022-06-13 16:01:15.661371
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('127.0.0.1', {'failures': 0, 'unreachable': 0, 'changed': 0}, True) == u'%-37s' % stringc('127.0.0.1', C.COLOR_OK)
    assert hostcolor('127.0.0.1', {'failures': 0, 'unreachable': 0, 'changed': 1}, True) == u'%-37s' % stringc('127.0.0.1', C.COLOR_CHANGED)
    assert hostcolor('127.0.0.1', {'failures': 1, 'unreachable': 0, 'changed': 0}, True) == u'%-37s' % stringc('127.0.0.1', C.COLOR_ERROR)

# Generated at 2022-06-13 16:01:22.113297
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor('red') == '31'
    assert parsecolor('yellow') == '33'
    assert parsecolor('0') == '38;5;0'
    assert parsecolor('15') == '38;5;15'
    assert parsecolor('16') == '38;5;16'
    assert parsecolor('17') == '38;5;17'
    assert parsecolor('23') == '38;5;23'
    assert parsecolor('24') == '38;5;24'
    assert parsecolor('25') == '38;5;25'
    assert parsecolor('rgb524') == '38;5;196'
    assert parsecolor('rgb444') == '38;5;136'

# Generated at 2022-06-13 16:01:31.799294
# Unit test for function colorize
def test_colorize():
    """
    Colorize unit test
    """
    # pylint: disable=unused-variable
    if ANSIBLE_COLOR:
        c = (u'\033[0;30;41mFAILED! => {', u"u'rc': 1,", u"'failed': True}", u'\033[0m')
    else:
        c = (u'FAILED! => {', u"u'rc': 1,", u"'failed': True}", u'')
    assert colorize('FAILED! => ', {'rc': 1, 'failed': True}, 'dark red') == ''.join(c)

# end "pretty" code
# ---

# Code below this point is a stripped-down version of code from
# http://stackoverflow.com/questions/22886353/printing-col

# Generated at 2022-06-13 16:01:40.041886
# Unit test for function parsecolor
def test_parsecolor():
    """Test the color parsing function."""

    # Check a color name
    assert(parsecolor('blue') == u'34')

    # Check a 16-color value
    assert(parsecolor('color1') == u'31')
    assert(parsecolor('color4') == u'34')

    # Check RGB colors
    assert(parsecolor('rgb000') == u'38;5;16')
    assert(parsecolor('rgb123') == u'38;5;31')
    assert(parsecolor('rgb321') == u'38;5;60')

    # Check grayscale
    assert(parsecolor('gray1') == u'38;5;232')
    assert(parsecolor('gray9') == u'38;5;244')
# --- end "pretty"

# Generated at 2022-06-13 16:01:48.709701
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('HOSTNAME', {}) == "%-26s" % "HOSTNAME"
    assert hostcolor('HOSTNAME', {'failures': 1}) == "%-37s" % \
           stringc('HOSTNAME', C.COLOR_ERROR)
    assert hostcolor('HOSTNAME', {'changed': 1}) == "%-37s" % \
           stringc('HOSTNAME', C.COLOR_CHANGED)
    assert hostcolor('HOSTNAME', {'failures': 0, 'changed': 0}) == "%-37s" % \
           stringc('HOSTNAME', C.COLOR_OK)


# --- end "pretty"

TOWER_LOCALHOST = "localhost (Tower)"



# Generated at 2022-06-13 16:01:59.393632
# Unit test for function colorize
def test_colorize():
    from ansible.utils.color import colorize
    from ansible import constants as C

    # Tests when ANSIBLE_COLOR is turned off
    ANSIBLE_COLOR_SAVE = ANSIBLE_COLOR
    ANSIBLE_COLOR = False
    assert colorize('test', 'success', C.COLOR_OK) == 'test=success'
    assert colorize('test', 0, C.COLOR_OK) == 'test=0'
    ANSIBLE_COLOR = ANSIBLE_COLOR_SAVE

    # Test when color is none
    assert colorize('test', 'success', None) == 'test=success'
    assert colorize('test', 0, None) == 'test=0    '

    # Tests when ANSIBLE_COLOR is turned on
    save_stdout = sys.stdout

# Generated at 2022-06-13 16:02:07.422728
# Unit test for function stringc

# Generated at 2022-06-13 16:02:16.738645
# Unit test for function stringc
def test_stringc():
    """Test function of stringc."""
    # color code should be interpreted
    assert stringc(u"test", u"blue") == u"\033[34mtest\033[0m"
    assert stringc(u"test", u"Color8") == u"\033[38;5;18mtest\033[0m"
    assert stringc(u"test", u"rgb123") == u"\033[38;5;135mtest\033[0m"
    assert stringc(u"test", u"gray9") == u"\033[38;5;241mtest\033[0m"

    # empty color code should not change the string
    assert stringc(u"test", u"") == u"\033[0mtest\033[0m"

# Generated at 2022-06-13 16:02:29.733118
# Unit test for function stringc
def test_stringc():
    # Basic colours
    assert stringc("test", "blue") == u"\033[34mtest\033[0m"
    assert stringc("test", "black") == u"\033[30mtest\033[0m"
    assert stringc("test", "red") == u"\033[31mtest\033[0m"
    assert stringc("test", "green") == u"\033[32mtest\033[0m"
    assert stringc("test", "yellow") == u"\033[33mtest\033[0m"
    assert stringc("test", "magenta") == u"\033[35mtest\033[0m"
    assert stringc("test", "cyan") == u"\033[36mtest\033[0m"
    assert stringc("test", "white")

# Generated at 2022-06-13 16:02:41.393152
# Unit test for function colorize
def test_colorize():
    assert colorize('ok', 0, C.COLOR_OK) == 'ok=0   '
    assert colorize('changed', 0, C.COLOR_CHANGED) == 'changed=0   '
    assert colorize('unreachable', 0, C.COLOR_UNREACHABLE) == 'unreachable=0   '
    assert colorize('failed', 0, C.COLOR_ERROR) == 'failed=0   '
    assert colorize('ok', 1, C.COLOR_OK) == stringc('ok=1   ', C.COLOR_OK)
    assert colorize('changed', 2, C.COLOR_CHANGED) == stringc('changed=2   ', C.COLOR_CHANGED)

# Generated at 2022-06-13 16:02:46.021821
# Unit test for function stringc
def test_stringc():
    assert stringc(u"hello", u"red") == u"\033[31mhello\033[0m"
    assert stringc(u"hello", u"bright red", True) == u"\001\033[91m\002hello\001\033[0m\002"
    assert stringc(u"hello", u"green") == u"\033[32mhello\033[0m"
    assert stringc(u"hello", u"bright green", True) == u"\001\033[92m\002hello\001\033[0m\002"
    assert stringc(u"hello", u"yellow") == u"\033[33mhello\033[0m"

# Generated at 2022-06-13 16:02:55.818866
# Unit test for function hostcolor
def test_hostcolor():
    ''' hostcolor() returns strings that match the specified regexes '''
    p_ok = re.compile('\x1b\[32m\S+\x1b\[0m')
    p_error = re.compile('\x1b\[31m\S+\x1b\[0m')
    p_changed = re.compile('\x1b\[33m\S+\x1b\[0m')
    p_host = re.compile('\S+')


# Generated at 2022-06-13 16:03:05.275209
# Unit test for function stringc
def test_stringc():
    if ANSIBLE_COLOR:
        assert stringc("these are tests", C.COLOR_ERROR) == u'\033[31mthese are tests\033[0m'
        assert stringc("these are tests", "color3") == u'\033[38;5;3mthese are tests\033[0m'
        assert stringc("these are tests", "rgb255") == u'\033[38;5;231mthese are tests\033[0m'
        assert stringc("these are tests", "rgb250") == u'\033[38;5;145mthese are tests\033[0m'
        assert stringc("these are tests", "rgb220") == u'\033[38;5;109mthese are tests\033[0m'

# Generated at 2022-06-13 16:03:15.784220
# Unit test for function hostcolor
def test_hostcolor():
    host = 'fake_host'
    stats = dict(failures=0, unreachable=0, changed=0)
    assert hostcolor(host, stats) == u"%-37s" % stringc(host, C.COLOR_OK)
    stats = dict(failures=4, unreachable=0, changed=0)
    assert hostcolor(host, stats) == u"%-37s" % stringc(host, C.COLOR_ERROR)
    stats = dict(failures=0, unreachable=4, changed=0)
    assert hostcolor(host, stats) == u"%-37s" % stringc(host, C.COLOR_ERROR)
    stats = dict(failures=0, unreachable=0, changed=4)

# Generated at 2022-06-13 16:03:24.268887
# Unit test for function stringc
def test_stringc():
    BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)
    # These are the sequences need to get colored ouput
    RESET_SEQ = u"\033[0m"
    COLOR_SEQ = u"\033[1;%dm"
    BOLD_SEQ = u"\033[1m"

    def formatter_message(message, use_color=True):
        if use_color:
            message = message.replace(u"$RESET", RESET_SEQ).replace(u"$BOLD", BOLD_SEQ)
        else:
            message = message.replace(u"$RESET", u"").replace(u"$BOLD", u"")
        return message


# Generated at 2022-06-13 16:03:30.660076
# Unit test for function hostcolor
def test_hostcolor():
    stats = { 'failures':0, 'changed':0, 'unreachable':0, 'ok':1 }

    if hostcolor(u'foo', stats) != u"%-37s" % u"foo":
        print(u'hostcolor fails on C.COLOR_OK')
    if hostcolor(u'foo', stats, False) != u"%-26s" % u"foo":
        print(u'hostcolor fails on C.COLOR_OK when color is set to False')

    stats = { 'failures':1, 'changed':0, 'unreachable':0, 'ok':1 }
    if hostcolor(u'foo', stats) != u"%-37s" % stringc(u'foo', C.COLOR_ERROR):
        print(u'hostcolor fails on C.COLOR_ERROR.')

# Generated at 2022-06-13 16:03:41.492806
# Unit test for function stringc
def test_stringc():
    test_strings = {'colors': ['red', 'green', 'yellow', 'blue', 'magenta',
                               'cyan', 'white'],
                    'colornums': [16, 17, 18, 19, 20, 21, 22],
                    'grays': [232, 233, 234, 235, 236, 237, 238, 239]}
    print('=' * 76)
    for color in test_strings['colors']:
        print(stringc("This is %s text" % color, color))
    for color in test_strings['colornums']:
        print(stringc("This is color %d." % color, "color%d" % color))
    for color in test_strings['grays']:
        print(stringc("This is gray %d" % color, "gray%d" % color))
        print

# Generated at 2022-06-13 16:03:51.151225
# Unit test for function colorize
def test_colorize():
    # Print a simple string of text using all of the available colors
    for color in ['black', 'red', 'green', 'yellow', 'blue', 'purple', 'cyan', 'white']:
        print(stringc("stringc color test for %s" % color, color))
    # Print a simple string of text using all of the available gray shades
    for shade in ['gray0', 'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9']:
        print(stringc("stringc gray test for %s" % shade, shade))
    # Print a simple string of text using all of the available rgb colors

# Generated at 2022-06-13 16:04:06.498824
# Unit test for function hostcolor
def test_hostcolor():
    # No color
    assert hostcolor(u"localhost", {u"ok": 1, u"changed": 0, u"dark": 0, u"failures": 0}) == u"localhost            "
    # Color
    for color in (C.COLOR_ERROR, C.COLOR_CHANGED):
        for res in (u"unreachable", u"failures"):
            stats = {u"ok": 1, u"changed": 0, u"dark": 0, res: 1}
            assert hostcolor(u"localhost", stats, color=True).lstrip().startswith(u"\033")
            assert hostcolor(u"localhost", stats, color=True).rstrip().endswith(u"m")

# Generated at 2022-06-13 16:04:17.992590
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor("localhost", dict(failures=1, unreachable=0, changed=0, ok=0)) == stringc("localhost", C.COLOR_ERROR)
    assert hostcolor("localhost", dict(failures=0, unreachable=1, changed=0, ok=0)) == stringc("localhost", C.COLOR_ERROR)
    assert hostcolor("localhost", dict(failures=0, unreachable=0, changed=1, ok=0)) == stringc("localhost", C.COLOR_CHANGED)
    assert hostcolor("localhost", dict(failures=0, unreachable=0, changed=0, ok=1)) == stringc("localhost", C.COLOR_OK)

    assert hostcolor("localhost", dict(failures=1, unreachable=1, changed=1, ok=0), False) == "localhost                "

# Generated at 2022-06-13 16:04:28.564140
# Unit test for function hostcolor
def test_hostcolor():
    stats = dict(failures=0, unreachable=0, changed=0)
    assert hostcolor('foo', stats, False) == '%-26s' % 'foo'
    assert hostcolor('foo', stats, True) == '%-37s' % stringc('foo', C.COLOR_OK)

    stats['failures'] = stats['changed'] = 1
    stats['unreachable'] = 0
    assert hostcolor('foo', stats, True) == '%-37s' % stringc('foo', C.COLOR_CHANGED)

    stats['failures'] = stats['unreachable'] = 1
    stats['changed'] = 0
    assert hostcolor('foo', stats, True) == '%-37s' % stringc('foo', C.COLOR_ERROR)

# --- end "pretty"


# --- begin task status ---



# Generated at 2022-06-13 16:04:37.783552
# Unit test for function stringc
def test_stringc():
    # Tests with foreground colors
    assert stringc("test", "blue") == u"\033[34mtest\033[0m"
    assert stringc("test", "red") == u"\033[31mtest\033[0m"
    assert stringc("test", "green") == u"\033[32mtest\033[0m"
    assert stringc("test", "yellow") == u"\033[33mtest\033[0m"
    assert stringc("test", "purple") == u"\033[35mtest\033[0m"
    assert stringc("test", "cyan") == u"\033[36mtest\033[0m"
    assert stringc("test", "white") == u"\033[37mtest\033[0m"

    # Tests with gray colors
   

# Generated at 2022-06-13 16:04:42.783977
# Unit test for function stringc
def test_stringc():
    """Tests for the stringc function"""
    data = 'black red green yellow blue magenta cyan white'.split()
    for x in range(0, 8):
        assert stringc(data[x], str(x + 30)) == '\033[3%dm%s\033[0m' % (x, data[x])
    assert stringc('gray0', '0') == '\033[30mgray0\033[0m'
    assert stringc('gray1', '1') == '\033[30mgray1\033[0m'
    assert stringc('gray0', 'gray0') == '\033[38;5;232mgray0\033[0m'
    assert stringc('gray1', 'gray1') == '\033[38;5;233mgray1\033[0m'

# Generated at 2022-06-13 16:04:54.361840
# Unit test for function colorize
def test_colorize():
    """Test colorize()"""
    import sys
    if sys.platform != 'win32':
        assert colorize('foo', 0, 'normal') == '\x1b[0mfoo=0   \x1b[0m'
        assert colorize('foo', 0, 'black') == '\x1b[30mfoo=0   \x1b[0m'
        assert colorize('foo', 0, 'red') == '\x1b[31mfoo=0   \x1b[0m'
        assert colorize('foo', 0, 'green') == '\x1b[32mfoo=0   \x1b[0m'
        assert colorize('foo', 0, 'yellow') == '\x1b[33mfoo=0   \x1b[0m'

# Generated at 2022-06-13 16:05:01.346834
# Unit test for function colorize
def test_colorize():
    host = 'host'
    sdict = dict(skipped=0, ok=0, failures=1, unreachable=0, changed=0)
    print(hostcolor(host, sdict))
    sdict = dict(skipped=0, ok=1, failures=1, unreachable=0, changed=0)
    print(hostcolor(host, sdict))
    sdict = dict(skipped=0, ok=0, failures=0, unreachable=1, changed=0)
    print(hostcolor(host, sdict))
    sdict = dict(skipped=0, ok=0, failures=0, unreachable=0, changed=1)
    print(hostcolor(host, sdict))



# Generated at 2022-06-13 16:05:06.875851
# Unit test for function stringc
def test_stringc():
    """Unit test for function stringc
    """
    if not ANSIBLE_COLOR:
        print("(can't test ANSIBLE_COLOR=False, just assume it works)")
        return

    def assert_test(text, color, wrap_nonvisible_chars=False):
        # print("text='%s', color='%s', wrap='%s'" % (text, color, wrap_nonvisible_chars))
        res = stringc(text, color, wrap_nonvisible_chars=wrap_nonvisible_chars)
        assert res.endswith("\033[0m"), "term code not reset: %s" % res

    # basename
    text = u"foo"
    color = u"red"
    assert_test(text, color)

    # basename
    text = u"foo"


# Generated at 2022-06-13 16:05:15.959424
# Unit test for function hostcolor
def test_hostcolor():
    host = 'testhost'
    stats1 = {}
    stats1['failures'] = 0
    stats1['unreachable'] = 0
    stats1['changed'] = 0
    assert hostcolor(host, stats1, False) == u"%-26s" % host
    assert hostcolor(host, stats1, True) == u"%-26s" % host

    stats2 = {}
    stats2['failures'] = 1
    stats2['unreachable'] = 0
    stats2['changed'] = 0
    assert hostcolor(host, stats2, False) == u"%-26s" % host
    assert hostcolor(host, stats2, True) == u"%-37s" % stringc(host, C.COLOR_ERROR)

    stats3 = {}
    stats3['failures'] = 0

# Generated at 2022-06-13 16:05:27.000157
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('test', { 'failures': 1, 'changed': 1, 'ok': 1, 'dark': 1 }) == u'\u001b[31mtest                               \u001b[0m   \n'
    assert hostcolor('test', {'failures': 1, 'changed': 1, 'ok': 1, 'dark': 0}) == u'\u001b[31mtest                               \u001b[0m   \n'
    assert hostcolor('test', {'failures': 1, 'changed': 0, 'ok': 1, 'dark': 0}) == u'\u001b[31mtest                               \u001b[0m   \n'

# Generated at 2022-06-13 16:05:40.298549
# Unit test for function hostcolor
def test_hostcolor():
    color = C.COLOR_ERROR
    host = u'test_host'
    stats = dict(
        unreachable=1,
        skipped=0,
        failed=0,
        ok=0,
        changed=0
    )

    expected = u"%-37s" % stringc(host, color)
    actual = hostcolor(host, stats, True)

    assert expected == actual, "Wrong host color"

# Generated at 2022-06-13 16:05:47.440941
# Unit test for function hostcolor
def test_hostcolor():
    assert(hostcolor("One", {'changed': 0, 'dark': 0, 'failures': 0, 'ok': True, 'skipped': 0, 'unreachable': 0}) == "One")
    assert(hostcolor("Two", {'changed': 1, 'dark': 0, 'failures': 0, 'ok': True, 'skipped': 0, 'unreachable': 0}) == C.COLOR_CHANGED + "Two" + C.COLOR_RESET)
    assert(hostcolor("Three", {'changed': 0, 'dark': 0, 'failures': 1, 'ok': True, 'skipped': 0, 'unreachable': 0}) == C.COLOR_ERROR + "Three" + C.COLOR_RESET)

# Generated at 2022-06-13 16:05:49.580889
# Unit test for function stringc
def test_stringc():
    assert stringc('foo', 'red', False) == '\033[31mfoo\033[0m'



# Generated at 2022-06-13 16:05:54.260778
# Unit test for function hostcolor
def test_hostcolor():
    # pylint: disable=unused-argument
    def mock_failures(self):
        return 0
    def mock_changed(self):
        return 0
    def mock_unreachable(self):
        return 0
    # pylint: enable=unused-argument

    host = u"localhost"
    stats = type("obj", (object,), {})()
    stats.failures = mock_failures
    stats.changed = mock_changed
    stats.unreachable = mock_unreachable
    rst = hostcolor(host, stats)
    assert type(rst) == unicode
    assert rst.endswith(host)



# Generated at 2022-06-13 16:06:04.121649
# Unit test for function stringc

# Generated at 2022-06-13 16:06:14.560698
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('localhost', dict(failures=0, unreachable=0, changed=0)) == u'localhost               '
    assert hostcolor('localhost', dict(failures=0, unreachable=0, changed=1)) == u'\x1b[0;32mlocalhost\x1b[0m               '
    assert hostcolor('localhost', dict(failures=2, unreachable=0, changed=0)) == u'\x1b[0;31mlocalhost\x1b[0m               '
    assert hostcolor('localhost', dict(failures=0, unreachable=2, changed=0)) == u'\x1b[0;31mlocalhost\x1b[0m               '

# Generated at 2022-06-13 16:06:25.589529
# Unit test for function hostcolor
def test_hostcolor():
    #pylint: disable=missing-docstring
    stats = dict(failures=0, unreachable=0, changed=0)
    assert hostcolor('host.example.org', stats, True) == u"host.example.org            "
    stats['changed'] = 1
    assert hostcolor('host.example.org', stats, True) == u"host.example.org            "
    stats['changed'] = 0
    stats['unreachable'] = 1
    assert hostcolor('host.example.org', stats, True) == u"host.example.org            "
    stats['unreachable'] = 0
    stats['failures'] = 1
    assert hostcolor('host.example.org', stats, True) == u"host.example.org            "
    stats['failures'] = 0

# --- end "pretty"


# Generated at 2022-06-13 16:06:30.735249
# Unit test for function hostcolor
def test_hostcolor():
    test_host = 'foobar_host'
    color = True
    stats = {'failures': 0, 'unreachable': 0, 'changed': 0}
    assert hostcolor(test_host, stats, color) == u'%-37s' % stringc(test_host, C.COLOR_OK), 'Unit test for hostcolor function failed'

# --- end "pretty"

# --- begin "termcap"

import fcntl
import struct
import termios
import termios




# Generated at 2022-06-13 16:06:40.946719
# Unit test for function hostcolor
def test_hostcolor():
    assert(hostcolor('localhost', dict(failures=0, unreachable=0, changed=0)) == u'localhost                    ')  # no color
    assert(hostcolor('localhost', dict(failures=1, unreachable=0, changed=0), color=True) == u'\x1b[31m\x1b[1mlocalhost\x1b[0m                    ')  # red
    assert(hostcolor('localhost', dict(failures=0, unreachable=1, changed=0), color=True) == u'\x1b[31m\x1b[1mlocalhost\x1b[0m                    ')  # red

# Generated at 2022-06-13 16:06:52.024810
# Unit test for function hostcolor
def test_hostcolor():
    host = "foobar"
    stats = {"failures": 0, "unreachable": 0, "changed": 0}
    print(hostcolor(host, stats, True))
    stats = {"failures": 1, "unreachable": 0, "changed": 0}
    print(hostcolor(host, stats, True))
    stats = {"failures": 0, "unreachable": 1, "changed": 0}
    print(hostcolor(host, stats, True))
    stats = {"failures": 0, "unreachable": 0, "changed": 1}
    print(hostcolor(host, stats, True))
    stats = {"failures": 1, "unreachable": 1, "changed": 0}
    print(hostcolor(host, stats, True))

# Generated at 2022-06-13 16:07:17.435788
# Unit test for function hostcolor
def test_hostcolor():
    stats = {
        'changed': 0,
        'unreachable': 0,
        'failures': 0
    }
    assert hostcolor('hostkeys-fetch', stats) == 'hostkeys-fetch          '

    stats = {
        'changed': 1,
        'unreachable': 0,
        'failures': 0
    }
    assert hostcolor('hostkeys-fetch', stats) == u'\n'.join(
        [u'\033[0;33mhostkeys-fetch\033[0m'])

    stats = {
        'changed': 0,
        'unreachable': 0,
        'failures': 1
    }

# Generated at 2022-06-13 16:07:25.835765
# Unit test for function hostcolor
def test_hostcolor():
    o = hostcolor('my-ssh-host', {'failures': 0, 'unreachable': 0, 'changed': 0}, False)
    n = u"%-26s" % 'my-ssh-host'
    assert o == n
    o = hostcolor('my-ssh-host', {'failures': 0, 'unreachable': 0, 'changed': 1}, False)
    n = u"%-26s" % 'my-ssh-host'
    assert o == n
    o = hostcolor('my-ssh-host', {'failures': 0, 'unreachable': 0, 'changed': 0}, True)
    n = u"%-37s" % 'my-ssh-host'
    assert o == n

# Generated at 2022-06-13 16:07:31.850156
# Unit test for function hostcolor
def test_hostcolor():
    host = 'somename'
    stats = dict(
        ok=10,
        failures=0,
        unreachable=0,
        changed=0,
        skipped=0,
    )

    assert hostcolor(host, stats) == '%-37s' % stringc(host, C.COLOR_OK)


# --- end "pretty"

__all__ = ['stringc', 'colorize', 'hostcolor']

# Generated at 2022-06-13 16:07:38.551279
# Unit test for function colorize
def test_colorize():
    """
    >>> import sys
    >>> real_stdout = sys.stdout
    >>> try:
    ...     sys.stdout = open('/dev/null', 'w')
    ...     colorize('foo', 0, 'blue')
    ...     colorize('bar', 1, 'blue')
    ...     colorize('baz', 2, 'yellow')
    ... except:
    ...     pass
    >>> sys.stdout.flush()
    >>> sys.stdout = real_stdout
    """


# --- end "pretty"



# Generated at 2022-06-13 16:07:44.555722
# Unit test for function colorize
def test_colorize():
    # The lead string is printed literally. If a color is given, the
    # number is printed in the specified color. Rather than generate a
    # separate test for each color, just test that a color produces the
    # expected ANSI escape sequence.
    #
    # If no color is specified then the number should be printed literally
    # with no color.
    #
    # The output is run through the `strip` method to remove all of the
    # leading, trailing and embedded whitespace. This leaves only the
    # numeric value or, possibly, the ANSI escape sequence if a color was
    # given.
    assert colorize('foo', 3, None).strip() == 'foo=3'  # no color
    assert colorize('foo', 3, 'red').strip() != 'foo=3'  # color given
    # color given with no number -- the

# Generated at 2022-06-13 16:07:52.454475
# Unit test for function stringc
def test_stringc():
    """Unit test for function stringc."""
    for color in C.COLOR_CODES:
        s = stringc("colored %s text" % color, color)
        print(u"%s\n" % s)
    # test rgb color
    s = stringc("colored rgb text", 'rgb123')
    print(u"%s\n" % s)
    # test gray color
    s = stringc("colored gray text", 'gray5')
    print(u"%s\n" % s)

# Generated at 2022-06-13 16:08:04.180472
# Unit test for function parsecolor
def test_parsecolor():
    from ansible.utils.color import parsecolor

# Generated at 2022-06-13 16:08:14.204607
# Unit test for function colorize
def test_colorize():
    lead = "test"
    color = 'yellow'
    for num in [0, 1, 2]:
        result = colorize(lead, num, color)
        assert result.startswith(lead + '=')


# --- end of "pretty"

# --- start of "repr"
#
# repr - a repr() replacement for non-ascii strings

# Copyright (C) 2013, 2014  Red Hat, Inc.
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# the GNU General Public License v.2, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY expressed or implied, including the implied warranties of
# MERCHANTABILITY or FITNESS

# Generated at 2022-06-13 16:08:22.433921
# Unit test for function hostcolor
def test_hostcolor():
    print(hostcolor(u"host1", {'unreachable': 0, 'failures': 0, 'changed': 0}, color=True))
    print(hostcolor(u"host1", {'unreachable': 1, 'failures': 0, 'changed': 0}, color=True))
    print(hostcolor(u"host1", {'unreachable': 0, 'failures': 1, 'changed': 0}, color=True))
    print(hostcolor(u"host1", {'unreachable': 0, 'failures': 0, 'changed': 1}, color=True))

# --- end "pretty"



# Generated at 2022-06-13 16:08:30.356047
# Unit test for function hostcolor
def test_hostcolor():
    stats = {}

    stats['changed'] = 0
    stats['failures'] = 0
    stats['unreachable'] = 0

    host = 'localhost.localdomain'

    assert hostcolor(host, stats) == u"%-26s" % host

    stats['changed'] = 1

    assert hostcolor(host, stats) \
        == u"%-37s" % stringc(host, C.COLOR_CHANGED)

    stats['changed'] = 0
    stats['failures'] = 1

    assert hostcolor(host, stats) \
        == u"%-37s" % stringc(host, C.COLOR_ERROR)



# Generated at 2022-06-13 16:09:17.687427
# Unit test for function stringc

# Generated at 2022-06-13 16:09:20.839924
# Unit test for function colorize
def test_colorize():
    lead = 'foo'
    num = 42
    color = 'red'
    print("%s colorize(%s,%s,%s) = %s" % (ANSIBLE_COLOR and u'\u2713' or 'X',lead, num, color, colorize(lead, num, color)))


# Generated at 2022-06-13 16:09:22.631071
# Unit test for function hostcolor
def test_hostcolor():
    return True

ALL_OK = 0
CHANGED = 1
ERROR = 2



# Generated at 2022-06-13 16:09:31.327302
# Unit test for function stringc
def test_stringc():

    def assertEqual(a, b):
        if a != b:
            raise AssertionError('%r != %r' % (a, b))

    for i in (0, 7, 15, 231, 255):
        assertEqual(stringc('stringc', i), '\033[38;5;%dmstringc\033[0m' % i)
    assertEqual(stringc('stringc', 'white'), '\033[38;5;15mstringc\033[0m')
    assertEqual(stringc('stringc', 'rgb123'), '\033[38;5;18mstringc\033[0m')
    assertEqual(stringc('stringc', 'gray0'), '\033[38;5;16mstringc\033[0m')