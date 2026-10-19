

# Generated at 2022-06-13 15:59:42.386954
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor(u'blue') == u'34'
    assert parsecolor(u'bright_red') == u'1;31'
    assert parsecolor(u'default') == u'39'
    assert parsecolor(u'color16') == u'38;5;16'
    assert parsecolor(u'rgb252') == u'38;5;184'
    assert parsecolor(u'gray8') == u'38;5;244'
    assert parsecolor(u'color0') == u'38;5;0'
    assert parsecolor(u'rgb555') == u'38;5;23'
    assert parsecolor(u'gray0') == u'38;5;232'


# --- end "pretty"

# ==============================================================
# action plugin

# Generated at 2022-06-13 15:59:47.419346
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor(u"color1") == u"38;5;1"
    assert parsecolor(u"rgb123") == u"38;5;197"
    assert parsecolor(u"gray1") == u"38;5;233"

# --- end of pretty


# Generated at 2022-06-13 15:59:55.756924
# Unit test for function parsecolor
def test_parsecolor():
    """Unit test for function parsecolor"""
    # Test standard colors
    assert parsecolor('white') == u'38;5;15'
    assert parsecolor('black') == u'38;5;16'
    assert parsecolor('blue') == u'38;5;19'
    assert parsecolor('cyan') == u'38;5;51'
    assert parsecolor('green') == u'38;5;22'
    assert parsecolor('magenta') == u'38;5;55'
    assert parsecolor('red') == u'38;5;9'
    assert parsecolor('yellow') == u'38;5;11'
    # Test 256 colors
    assert parsecolor('color4') == u'38;5;4'
    assert parsecolor('color29') == u

# Generated at 2022-06-13 15:59:58.387381
# Unit test for function colorize
def test_colorize():
    print(colorize(u"changed", 12, C.COLOR_CHANGED))
    print(colorize(u"darkred", 0, C.COLOR_ERROR))
    print(colorize(u"darkred", 1, None))
    print(colorize(u"darkred", 12, None))
# End of code from pretty
# ---



# Generated at 2022-06-13 16:00:05.415888
# Unit test for function colorize
def test_colorize():
    if not ANSIBLE_COLOR:
        print("\nNo color support detected, unable to run unit test, skipping...\n")
        return
    assert colorize('foo', 0, 'blue') == u"foo=0   "
    assert colorize('bar', 1, None) == u"bar=1   "
    assert colorize('baz', 42, 'red') == u"baz=42  "
    # Colorize should escape special chars
    assert colorize('b a z', '3 1"1', 'black') == u'b a z=3 1"1'
    print("colorize function: OK")

# end "pretty" ---

_HOST_COLUMN_WIDTH = 25


# Generated at 2022-06-13 16:00:14.960725
# Unit test for function hostcolor
def test_hostcolor():
    test_host = 'localhost'
    test_stats = dict(failures=0, unreachable=1, changed=0)
    assert hostcolor(test_host, test_stats, color=True) == u"\033[31m%-37s\033[0m" % test_host
    test_stats = dict(failures=0, unreachable=0, changed=1)
    assert hostcolor(test_host, test_stats, color=True) == u"\033[33m%-37s\033[0m" % test_host
    test_stats = dict(failures=0, unreachable=0, changed=0)
    assert hostcolor(test_host, test_stats, color=True) == u"\033[32m%-37s\033[0m" % test_host



# Generated at 2022-06-13 16:00:24.103074
# Unit test for function stringc
def test_stringc():
    # Test all the color variations
    print(u"test_stringc:")

# Generated at 2022-06-13 16:00:28.782997
# Unit test for function hostcolor
def test_hostcolor():
    # testing with color
    stats = dict(changed=10, failures=20, ok=30, skipped=40, unreachable=50)
    assert hostcolor('example.com', stats, color=True) == u'%-37s' % stringc('example.com', C.COLOR_ERROR)

    stats = dict(changed=10, failures=0, ok=30, skipped=40, unreachable=0)
    assert hostcolor('example.com', stats, color=True) == u'%-37s' % stringc('example.com', C.COLOR_CHANGED)

    stats = dict(changed=0, failures=0, ok=30, skipped=40, unreachable=0)
    assert hostcolor('example.com', stats, color=True) == u'%-37s' % stringc('example.com', C.COLOR_OK)

# Generated at 2022-06-13 16:00:40.260085
# Unit test for function parsecolor
def test_parsecolor():
    from nose.tools import assert_equals
    assert_equals(parsecolor("color0"), u'38;5;0')
    assert_equals(parsecolor("color1"), u'38;5;1')
    assert_equals(parsecolor("color15"), u'38;5;15')
    assert_equals(parsecolor("color16"), u'38;5;16')
    assert_equals(parsecolor("color255"), u'38;5;255')
    assert_equals(parsecolor("rgb000"), u'38;5;16')
    assert_equals(parsecolor("rgb444"), u'38;5;52')
    assert_equals(parsecolor("rgb555"), u'38;5;63')

# Generated at 2022-06-13 16:00:47.247739
# Unit test for function parsecolor
def test_parsecolor():
    for color in ('black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan',
                  'white'):
        assert parsecolor(color) == str(C.COLOR_CODES[color])
    for color, code in C.COLOR_CODES.items():
        assert parsecolor(color) == str(code)

# Generated at 2022-06-13 16:00:53.597257
# Unit test for function hostcolor

# Generated at 2022-06-13 16:01:04.471882
# Unit test for function stringc

# Generated at 2022-06-13 16:01:15.548761
# Unit test for function stringc
def test_stringc():
    assert u'\033[1;31mfoo\033[0m' == stringc(u'foo', u'RED', True)
    assert u'\001\033[1;31m\002foo\001\033[0m\002' == stringc(u'foo', u'RED', False)
    assert u'\033[1;31mfoo\033[0m' == stringc(u'foo', u'1;31', True)
    assert u'\001\033[1;31m\002foo\001\033[0m\002' == stringc(u'foo', u'1;31', False)
    assert u'\033[1;31mfoo\nbar\033[0m' == stringc(u'foo\nbar', u'RED', True)

# Generated at 2022-06-13 16:01:20.388920
# Unit test for function stringc

# Generated at 2022-06-13 16:01:27.984091
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('host', dict(
        ok=0, changed=0, unreachable=0, failures=0, skipped=0
    )) == u"host"

    assert hostcolor('host', dict(
        ok=0, changed=0, unreachable=0, failures=1, skipped=0
    )) == u"host"

    assert hostcolor('host', dict(
        ok=0, changed=1, unreachable=0, failures=0, skipped=0
    )) == u"host"

# --- end "pretty"

# Generated at 2022-06-13 16:01:35.345029
# Unit test for function stringc
def test_stringc():
    # Checking if a color name is converted to its SGR parameter
    assert parsecolor('blue') == u'34'
    # Checking if a color number is converted to its SGR parameter
    assert parsecolor('color16') == u'38;5;16'
    # Checking if a RGB specification is converted to its SGR parameter
    assert parsecolor('rgb123') == u'38;5;105'
    # Checking if a gray level is converted to its SGR parameter
    assert parsecolor('gray8') == u'38;5;240'
    # Checking if function stringc wraps a string in ANSI escape sequences
    assert stringc("string", "blue") == u"\033[34mstring\033[0m"
    # Checking if invisible chars wrapping is not present when ANSIBLE_COLOR=False

# Generated at 2022-06-13 16:01:46.529906
# Unit test for function stringc
def test_stringc():
    # Set up stream logging
    import logging
    logger = logging.getLogger('ansible.color')

    # If colors are enabled, make sure they work as expected,
    # otherwise, if colors are disabled, make sure they don't show up.
    if ANSIBLE_COLOR:
        assert stringc("test", 'green') == u"\033[32mtest\033[0m"
    else:
        assert stringc("test", 'green') == "test"

    # If colors are provided as variables, they should also work.
    assert stringc("test", C.COLOR_OK) == stringc("test", 'green')

    # Check that parsecolor returns a color code that works.
    assert parsecolor("CUSTOM") == u"38;5;208"

# Generated at 2022-06-13 16:01:56.238598
# Unit test for function stringc
def test_stringc():

    # Output without color
    ANSIBLE_COLOR = False
    assert stringc(text = u"Output without color", color = u"red") == u"Output without color"

    # Output with color
    ANSIBLE_COLOR = True
    assert stringc(text = u"Output with color", color = u"red") == u"\033[31mOutput with color\033[0m"

    # Output with color and wrap
    ANSIBLE_COLOR = True
    assert stringc(text = u"Output with color and wrap", color = u"red",
                   wrap_nonvisible_chars = True) == u"\001\033[31m\002Output with color and wrap\001\033[0m\002"


# Generated at 2022-06-13 16:02:00.880952
# Unit test for function stringc
def test_stringc():
    """Test the ANSI color functionality"""
    assert stringc(u"This is a test.", u"green") == \
        u"\033[38;5;2mThis is a test.\033[0m"
    assert stringc(u"This is a test.", u"color4") == \
        u"\033[38;5;4mThis is a test.\033[0m"
    assert stringc(u"This is a test.", u"gray1") == \
        u"\033[38;5;234mThis is a test.\033[0m"
    assert stringc(u"This is a test.", u"rgb255255255") == \
        u"\033[38;5;15mThis is a test.\033[0m"



# Generated at 2022-06-13 16:02:08.724144
# Unit test for function hostcolor
def test_hostcolor():
    # hostcolor return a string with color and padding
    assert hostcolor(u'localhost', dict(failures=0, unreachable=0, changed=0)) == u'%-37s' % stringc(u'localhost', C.COLOR_OK)
    # hostcolor return a string with color and padding
    assert hostcolor(u'localhost', dict(failures=1, unreachable=0, changed=0)) == u'%-37s' % stringc(u'localhost', C.COLOR_ERROR)
    # hostcolor return a string with color and padding
    assert hostcolor(u'localhost', dict(failures=0, unreachable=0, changed=1)) == u'%-37s' % stringc(u'localhost', C.COLOR_CHANGED)
    # hostcolor return a string with color and padding

# Generated at 2022-06-13 16:02:20.667217
# Unit test for function stringc
def test_stringc():
    """ Unit test to exercise function stringc() """
    assert u"\033[31mhello\033[0m" == stringc(u"hello", u"RED", False)
    assert u"\033[1;31mhello\033[0m" == stringc(u"hello", u"BRIGHT RED", False)
    assert u"\033[32mhello\033[0m" == stringc(u"hello", u"GREEN", False)
    assert u"\033[33mhello\033[0m" == stringc(u"hello", u"YELLOW", False)
    assert u"\033[34mhello\033[0m" == stringc(u"hello", u"BLUE", False)

# Generated at 2022-06-13 16:02:29.656052
# Unit test for function stringc
def test_stringc():
    """Unit test for function stringc"""
    assert stringc("foo", "green") == u"\033[32mfoo\033[0m"
    assert stringc("foo", "color1") == u"\033[38;5;1mfoo\033[0m"
    assert stringc("foo", "rgb255255255") == u"\033[38;5;15mfoo\033[0m"
    assert stringc("foo", "rgb000255000") == u"\033[38;5;2mfoo\033[0m"
    assert stringc("foo", "gray0") == u"\033[38;5;232mfoo\033[0m"
    assert stringc("foo", "gray24") == u"\033[38;5;255mfoo\033[0m"

# Generated at 2022-06-13 16:02:41.393314
# Unit test for function hostcolor
def test_hostcolor():
    host = 'testhost'
    stats = {'changed': 1, 'failures': 0, 'ok': 5, 'skipped': 0, 'unreachable': 0}
    assert hostcolor(host, stats, False) == '%-26s' % host
    assert hostcolor(host, stats, True) == u'%-37s' % stringc(host, C.COLOR_CHANGED)
    host = 'testhost'
    stats = {'changed': 0, 'failures': 0, 'ok': 5, 'skipped': 0, 'unreachable': 0}
    assert hostcolor(host, stats, False) == '%-26s' % host
    assert hostcolor(host, stats, True) == u'%-37s' % stringc(host, C.COLOR_OK)
    host = 'testhost'

# Generated at 2022-06-13 16:02:52.303193
# Unit test for function stringc
def test_stringc():
    for key in ['black', 'white', 'red', 'green', 'blue', 'cyan', 'yellow',
                'magenta', 'grey', 'gray', 'bright black', 'bright white',
                'bright red', 'bright green', 'bright blue', 'bright cyan',
                'bright yellow', 'bright magenta', 'bright grey',
                'black on yellow', 'white on blue', 'red on green',
                'yellow on red', 'bright white on green', 'yellow on magenta',
                'black on blue', 'white on grey', 'bright red on green']:
        try:
            print((u"%-25s" % key), end=' ')
        except UnicodeEncodeError:
            print((u"%-25s" % key.encode('utf-8')), end=' ')
        print(stringc(key, key))

# Generated at 2022-06-13 16:03:00.069818
# Unit test for function stringc

# Generated at 2022-06-13 16:03:03.697082
# Unit test for function colorize
def test_colorize():
    for color, value in (('red', '1'), ('green', '2'), ('yellow', '3'),
                         ('blue', '4')):
        yield check_colorize, color, value, '%s=%-4s' % (color, value)



# Generated at 2022-06-13 16:03:12.220054
# Unit test for function hostcolor
def test_hostcolor():
    # ANSIBLE_COLOR = False
    assert hostcolor(u'Dummy host1', {u'failed': 0, u'changed': 0}) == '%-26s' % u'Dummy host1'
    assert hostcolor(u'Dummy host2', {u'failed': 0, u'changed': 0}, color=False) == '%-26s' % u'Dummy host2'
    assert hostcolor(u'Dummy host3', {u'failed': 5, u'changed': 0}) == '%-37s' % u'Dummy host3'
    assert hostcolor(u'Dummy host4', {u'failed': 5, u'changed': 0}, color=False) == '%-26s' % u'Dummy host4'

# Generated at 2022-06-13 16:03:19.769238
# Unit test for function stringc
def test_stringc():
    assert stringc('foo', 'green') == u'\033[32mfoo\033[0m'
    assert stringc('foo', 'bad') == u'foo'
    assert stringc('foo', 'bold') == u'\033[1mfoo\033[0m'
    try:
        stringc('foo', 1)
        assert 0, "No error for invalid color"
    except TypeError:
        pass


# --- end of "pretty"



# Generated at 2022-06-13 16:03:21.867800
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('host', {'failures': 0, 'unreachable': 0, 'changed': 0}) == u'%-37s'



# Generated at 2022-06-13 16:03:25.766412
# Unit test for function colorize
def test_colorize():
    """
    >>> print colorize('foo', 0, 'blue')
    foo=0
    >>> print colorize('foo', 2, None)
    foo=2
    >>> print colorize('foo', 0, None)
    foo=0
    >>> print colorize('foo', 2, 'blue')
    foo=2
    """



# Generated at 2022-06-13 16:03:41.072983
# Unit test for function hostcolor
def test_hostcolor():
    if ANSIBLE_COLOR:
        assert hostcolor('localhost', dict(changed=0, failures=1, unreachable=1)) == u"\033[31mlocalhost\033[0m            "
        assert hostcolor('localhost', dict(changed=0, failures=1, unreachable=0)) == u"\033[31mlocalhost\033[0m            "
        assert hostcolor('localhost', dict(changed=1, failures=0, unreachable=1)) == u"\033[31mlocalhost\033[0m            "
        assert hostcolor('localhost', dict(changed=0, failures=0, unreachable=1)) == u"\033[31mlocalhost\033[0m            "

# Generated at 2022-06-13 16:03:50.867728
# Unit test for function hostcolor
def test_hostcolor():
    stats = {'skipped': 0, 'failures': 0, 'ok': 6,
             'changed': 0, 'unreachable': 0, 'processed': 6}
    print(u"OK:              %s" % hostcolor(u"test_host", stats))
    stats['changed'] = 3
    print(u"changed:         %s" % hostcolor(u"test_host", stats))
    stats['failures'] = 6
    stats['changed'] = 0
    print(u"failures:        %s" % hostcolor(u"test_host", stats))
    stats['unreachable'] = 6
    stats['failures'] = 0
    print(u"unreachable:     %s" % hostcolor(u"test_host", stats))

# Generated at 2022-06-13 16:04:02.653201
# Unit test for function stringc
def test_stringc():
    """Basic unit test for the stringc function"""
    # Regular usage (coloring a text for a given color)
    text = u'test'
    assert stringc(text, 'blue') == u'\033[34mtest\033[0m'

    # Handling exceptions (non-existing color)
    assert stringc(text, 'rainbow') == text

    # Handling new lines
    assert stringc(u'foo\nbar', 'red') == u'\033[31mfoo\nbar\033[0m'

    # Test whether the option to wrap non-visible chars works
    assert stringc(text, 'green', wrap_nonvisible_chars=True) == u'\001\033[32m\002test\001\033[0m\002'

    # Test if everything works with a non-ascii character


# Generated at 2022-06-13 16:04:08.117852
# Unit test for function hostcolor
def test_hostcolor():
    # Tests whether hostcolor works fine with all parameters to be 0 or None

    # checks whether the output is as expected when all parameters are 0
    def check_hostcolor(host, stats):
        assert True == hostcolor(host, stats).endswith(host)

    stats = {'ok': 0, 'changed': 0, 'unreachable': 0, 'failures': 0}
    host = 'localhost'
    check_hostcolor(host, stats)

    # checks whether the output is as expected when all parameters are None
    def check_hostcolor_none(host, stats):
        assert 'None' == hostcolor(host, stats)

    stats = {'ok': None, 'changed': None, 'unreachable': None, 'failures': None}
    host = None
    check_hostcolor_none(host, stats)



# Generated at 2022-06-13 16:04:17.634916
# Unit test for function stringc
def test_stringc():
    # no-color check
    ANSIBLE_COLOR = False
    color_codes = C.COLOR_CODES.copy()
    C.COLOR_CODES = {}
    assert stringc("text", "black") == "text"
    C.COLOR_CODES = color_codes

    # color check
    ANSIBLE_COLOR = True
    ansi_escape = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -/]*[@-~]')
    assert ansi_escape.search(stringc("text", "black"))

# --- end "pretty" ---


# Generated at 2022-06-13 16:04:28.230246
# Unit test for function hostcolor
def test_hostcolor():
    test_stats = dict(failures=0, unreachable=0, changed=0)
    # Test the happy path.
    assert hostcolor('localhost', test_stats, True) == u'%-26s' % stringc('localhost', C.COLOR_OK)

    # Test failures
    test_stats['failures'] = 1
    assert hostcolor('localhost', test_stats, True) == u'%-26s' % stringc('localhost', C.COLOR_ERROR)
    test_stats['failures'] = 0

    # Test unreachable
    test_stats['unreachable'] = 1
    assert hostcolor('localhost', test_stats, True) == u'%-26s' % stringc('localhost', C.COLOR_ERROR)
    test_stats['unreachable'] = 0

    # Test changed

# Generated at 2022-06-13 16:04:36.720732
# Unit test for function stringc
def test_stringc():
    """Test the stringc function."""
    print(stringc('hello world', 'green'))
    print(stringc('hello world', '31'))
    print(stringc('hello world', 'rgb123'))
    print(stringc('hello world', 'rgb111'))
    print(stringc('hello world', 'rgb222'))
    print(stringc('hello world', 'rgb333'))
    print(stringc('hello world', 'rgb444'))
    print(stringc('hello world', 'rgb555'))
    print(stringc('hello world', 'rgb666'))
    print(stringc('hello world', 'rgb123', True))

# Original test function

# Generated at 2022-06-13 16:04:41.790375
# Unit test for function hostcolor
def test_hostcolor():
    host = 'abc'
    stats = {'ok': 0, 'failures': 0, 'unreachable': 0, 'skipped': 0, 'changed': 0}
    assert hostcolor(host, stats, True) == u"%-37s" % stringc(host, C.COLOR_OK)

    stats = {'ok': 1, 'failures': 0, 'unreachable': 0, 'skipped': 0, 'changed': 0}
    assert hostcolor(host, stats, True) == u"%-37s" % stringc(host, C.COLOR_OK)

    stats = {'ok': 1, 'failures': 1, 'unreachable': 0, 'skipped': 0, 'changed': 0}

# Generated at 2022-06-13 16:04:53.432262
# Unit test for function stringc

# Generated at 2022-06-13 16:05:03.597736
# Unit test for function stringc
def test_stringc():
    assert stringc("test", "green") == "\033[32mtest\033[0m"
    assert stringc("test", "dark gray") == "\033[1;30mtest\033[0m"
    assert stringc("test", "color4") == "\033[38;5;4mtest\033[0m"
    assert stringc("test", "rgb132") == "\033[38;5;97mtest\033[0m"
    assert stringc("test", "gray5") == "\033[38;5;237mtest\033[0m"
    assert stringc("test", "LIGHT BLUE") == "\033[94mtest\033[0m"

# --- end "pretty"

# Generated at 2022-06-13 16:05:21.469280
# Unit test for function stringc
def test_stringc():

    def _check_color(text, color, expected):
        result = stringc(text, color)
        if result != expected:
            raise AssertionError("stringc(%r, %r) -> %r != %r" % (text, color, result, expected))

    _check_color('', 'black', '\033[30m\033[0m')
    _check_color('', 'dark gray', '\033[90m\033[0m')
    _check_color('', 'blue', '\033[34m\033[0m')
    _check_color('', 'bright blue', '\033[94m\033[0m')
    _check_color('', 'rgb123', '\033[38;5;42m\033[0m')

# Generated at 2022-06-13 16:05:29.028977
# Unit test for function hostcolor
def test_hostcolor():
    host = '127.0.0.1'
    ret = hostcolor(host, dict(changed=1))
    assert ret == u"%-37s" % stringc(host, C.COLOR_CHANGED)

    ret = hostcolor(host, dict(failed=1))
    assert ret == u"%-37s" % stringc(host, C.COLOR_ERROR)

    ret = hostcolor(host, dict(ok=1))
    assert ret == u"%-37s" % stringc(host, C.COLOR_OK)

    ret = hostcolor(host, dict(changed=1), color=False)
    assert ret == u"%-26s" % host



# Generated at 2022-06-13 16:05:39.624590
# Unit test for function colorize
def test_colorize():
    # Show all the possible color combinations
    # NOTE: it is possible that these may fail on certain terminals due
    # to terminal capabilities.
    # ANSIBLE_FORCE_COLOR can also be used to force color support.
    print((colorize(u"TASK", u"", None)))
    print((colorize(u"TASK", u"1", None)))
    print((colorize(u"TASK", u"0", None)))
    print((colorize(u"TASK", u"1", C.COLOR_CHANGED)))
    print((colorize(u"TASK", u"0", C.COLOR_CHANGED)))
    print((colorize(u"TASK", u"1", C.COLOR_OK)))

# Generated at 2022-06-13 16:05:46.986313
# Unit test for function stringc
def test_stringc():
    """
    >>> test_stringc()
    - pass colored
    - pass noncolored
    - fail colored
    - fail noncolored
    - changed colored
    - changed noncolored
    - unreachable colored
    - unreachable noncolored
    - ok colored
    - ok noncolored
    - bold colored
    - bold noncolored
    - header colored
    - header noncolored
    - debug colored
    - debug noncolored
    - verbose colored
    - verbose noncolored
    """
    colors = ['darkgray', 'blue', 'purple', 'green', 'red', 'yellow', 'black',
              'darkgray', 'darkgray', 'yellow', 'darkgray', 'cyan', 'pink',
              'white']

# Generated at 2022-06-13 16:05:53.683624
# Unit test for function colorize
def test_colorize():
    for color in ('red', 'green', 'blue', 'yellow', 'default'):
        for num in (0, 1, 2, 1024):
            print(u"   %s" % colorize('>', num, color))
# --- end "pretty"

HAS_ATTRIBUTE_HASHLIB = False
try:
    import hashlib
    HAS_ATTRIBUTE_HASHLIB = True
except ImportError:
    try:
        import sha
        HAS_ATTRIBUTE_HASHLIB = True
    except ImportError:
        pass


# Generated at 2022-06-13 16:06:01.798985
# Unit test for function stringc
def test_stringc():
    failed = False
    failed = failed or stringc("Hello", "red") != u"\033[31mHello\033[0m"
    failed = failed or stringc("Hello", "rgb255255255") != u"\033[37mHello\033[0m"
    failed = failed or stringc("Hello", "rgb000255255") != u"\033[34mHello\033[0m"
    failed = failed or stringc("Hello\nWorld!", "red") != u"\033[31mHello\nWorld!\033[0m"
    assert not failed



# Generated at 2022-06-13 16:06:14.517082
# Unit test for function stringc
def test_stringc():
    color_ansi_regex = re.compile(r"\x1b\[[0-9;]*m")

    # test default fg colors
    for color, color_code in C.COLOR_CODES.items():
        # test normal mode
        assert re.search(color_ansi_regex, stringc(color, color))
        if color in ('white', 'yellow', 'black'):
            # test bold mode
            assert re.search(color_ansi_regex, stringc(color, color, wrap_nonvisible_chars=True))

    # test rgb colors
    color_values = ('0', '1', '2', '3', '4', '5')

# Generated at 2022-06-13 16:06:25.579501
# Unit test for function hostcolor
def test_hostcolor():
    for color in C.COLOR_CODES:
        host = '127.0.0.1'
        stats = {}

        # test failures
        stats['unreachable'] = 1
        assert stringc(host, C.COLOR_ERROR) == hostcolor(host, stats)
        stats['unreachable'] = 0
        stats['failures'] = 1
        assert stringc(host, C.COLOR_ERROR) == hostcolor(host, stats)

        # test unreachables
        stats['failures'] = 0
        stats['unreachable'] = 1
        assert stringc(host, C.COLOR_ERROR) == hostcolor(host, stats)

        # test changed
        stats['unreachable'] = 0
        stats['changed'] = 1

# Generated at 2022-06-13 16:06:31.534958
# Unit test for function stringc
def test_stringc():
    # color names
    assert stringc("red", "red") == "\033[31mred\033[0m"
    assert stringc("green", "green") == "\033[32mgreen\033[0m"
    assert stringc("yellow", "yellow") == "\033[33myellow\033[0m"
    assert stringc("blue", "blue") == "\033[34mblue\033[0m"
    assert stringc("magenta", "magenta") == "\033[35mmagenta\033[0m"
    assert stringc("cyan", "cyan") == "\033[36mcyan\033[0m"
    assert stringc("white", "white") == "\033[37mwhite\033[0m"

# Generated at 2022-06-13 16:06:41.460863
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('local', dict(failures=1, unreachable=1, changed=1)) == u'\x1b[91mlocal\x1b[0m'
    assert hostcolor('local', dict(failures=1, unreachable=1, changed=0)) == u'\x1b[91mlocal\x1b[0m'
    assert hostcolor('local', dict(failures=1, unreachable=0, changed=1)) == u'\x1b[91mlocal\x1b[0m'
    assert hostcolor('local', dict(failures=0, unreachable=1, changed=1)) == u'\x1b[91mlocal\x1b[0m'

# Generated at 2022-06-13 16:07:09.391232
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor(host='host_foo', stats={'failures': 0, 'unreachable': 0, 'changed': 0}) == u'host_foo                     '
    assert hostcolor(host='host_bar', stats={'failures': 1, 'unreachable': 0, 'changed': 0}) == u'host_bar                     \033[31m\033[1m\033[5m\033[41m\033[37m\033[22m\033[25m\033[49m\033[39m\033[m'
    assert hostcolor(host='host_baz', stats={'failures': 0, 'unreachable': 0, 'changed': 1}) == u'host_baz                     \033[1m\033[38;5;208m\033[22m\033[39m'



# Generated at 2022-06-13 16:07:17.501750
# Unit test for function colorize
def test_colorize():
    """ Unit test for colorize() """
    def c(lead, num, color):
        """ Sample call to colorize() """
        print(colorize(lead, num, color))

    print("Testing colorize()")
    try:
        orig_stdout = sys.stdout
        sys.stdout = open("/dev/null", "w")
        c("a", 100, "green")
        c("b", 0, "green")
        c("c", 0, None)
        c("d", 1, None)
        c("e", 3, "thisisnotacolorname")
        c("f", 3, "red")
    finally:
        sys.stdout = orig_stdout

# end "pretty"

if __name__ == '__main__':
    test_colorize()

# Generated at 2022-06-13 16:07:25.836315
# Unit test for function colorize
def test_colorize():
    """Unit test for function colorize"""
    if ANSIBLE_COLOR:
        assert colorize('ok', 0, C.COLOR_OK) == u'\u001b[32mok=0   \u001b[0m'
        assert colorize('changed', 0, C.COLOR_CHANGED) == u'\u001b[33mchanged=0   \u001b[0m'
        assert colorize('unreachable', 0, C.COLOR_UNREACHABLE) == u'\u001b[31munreachable=0 \u001b[0m'
        assert colorize('failed', 0, C.COLOR_ERROR) == u'\u001b[31mfailed=0    \u001b[0m'

# --- end "pretty"

# --- begin RAW_MODULES

# AN

# Generated at 2022-06-13 16:07:36.803438
# Unit test for function hostcolor
def test_hostcolor():
    host = 'testhost'
    stats = dict(failures=0, unreachable=0, changed=0)
    assert hostcolor(host, stats) == u"testhost                      "
    stats = dict(failures=0, unreachable=0, changed=1)
    assert hostcolor(host, stats) != u"testhost                      "
    assert hostcolor(host, stats, color=False) == u"testhost                      "
    stats = dict(failures=1, unreachable=0, changed=0)
    assert hostcolor(host, stats) != u"testhost                      "
    assert hostcolor(host, stats, color=False) == u"testhost                      "
    stats = dict(failures=1, unreachable=1, changed=0)
    assert hostcolor(host, stats) != u"testhost                      "
   

# Generated at 2022-06-13 16:07:43.540386
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor("host1", {'failures': 1, 'unreachable': 0, 'changed': 1}) == u'\x1b[31mhost1               \x1b[0m'
    assert hostcolor("host1", {'failures': 0, 'unreachable': 1, 'changed': 1}) == u'\x1b[31mhost1               \x1b[0m'
    assert hostcolor("host1", {'failures': 0, 'unreachable': 0, 'changed': 1}) == u'\x1b[33mhost1               \x1b[0m'
    assert hostcolor("host1", {'failures': 0, 'unreachable': 0, 'changed': 0}) == u'\x1b[32mhost1               \x1b[0m'
    assert host

# Generated at 2022-06-13 16:07:54.590045
# Unit test for function stringc
def test_stringc():
    # check if the color codes are properly returned
    assert stringc("test", "red") == "\033[31mtest\033[0m"
    assert stringc("test", "blue") == "\033[34mtest\033[0m"
    assert stringc("test", "green") == "\033[32mtest\033[0m"
    # check if the color codes for "color234" were properly parsed
    assert stringc("test", "color234") == "\033[38;5;234mtest\033[0m"
    # check if the color codes for "gray10" were properly parsed
    assert stringc("test", "gray10") == "\033[38;5;242mtest\033[0m"
    # check if the color codes for "rgb123" were properly parsed

# Generated at 2022-06-13 16:08:05.241892
# Unit test for function colorize
def test_colorize():
    # Expected behavior:
    # lead_00, num_0, color_None       ==>  lead_00=0
    # lead_00, num_1, color_None       ==>  lead_00=1
    # lead_00, num_0, color_blue       ==>  lead_00=0
    # lead_00, num_1, color_blue       ==>  lead_00=1
    # lead_00, num_0, color_red        ==>  lead_00=0
    # lead_00, num_1, color_red        ==>  lead_00=1

    def test_function(lead, num, color, expected):
        if colorize(lead, num, color) == expected:
            return True
        else:
            return False


# Generated at 2022-06-13 16:08:07.180581
# Unit test for function stringc
def test_stringc():
    # Test 1
    assert stringc(u"test", u"red") == u"\033[31mtest\033[0m"



# Generated at 2022-06-13 16:08:09.206304
# Unit test for function stringc
def test_stringc():
    assert stringc(u"foo", u'red')


# --- end "pretty"

# --- begin "human_log"



# Generated at 2022-06-13 16:08:19.507767
# Unit test for function stringc
def test_stringc():
    if ANSIBLE_COLOR:
        assert u"\033[38;5;1mfoo\033[0m" == stringc('foo', 'red')
        assert u"\033[38;5;9mfoo\033[0m" == stringc('foo', 'bright red')
        assert u"foo" == stringc('foo', 'no color')
        assert u"\033[38;5;39mfoo\033[0m" == stringc('foo', 'rgb 5 0 5')
        assert u"\033[38;5;94mfoo\033[0m" == stringc('foo', 'gray 4')
    else:
        assert u"foo" == stringc('foo', 'red')
        assert u"foo" == stringc('foo', 'bright red')

# Generated at 2022-06-13 16:08:46.178621
# Unit test for function colorize
def test_colorize():
    """ test function colorize """
    s = colorize(u'foo', 1, C.COLOR_CHANGED)
    assert s == u'foo=1   '
    s = colorize(u'foo', 1234, C.COLOR_OK)
    assert s == u'foo=1234'
    s = colorize(u'foo', 1234, None)
    assert s == u'foo=1234'
    s = colorize(u'foo', 0, C.COLOR_OK)
    assert s == u'foo=0   '
    s = colorize(u'A' * 20, 1234, C.COLOR_OK)
    assert s == u'A' * 20 + '=1234'
    s = colorize(u'A' * 100, 1234, C.COLOR_OK)

# Generated at 2022-06-13 16:08:57.581737
# Unit test for function colorize
def test_colorize():
    """ Unit tests for colorize """
    print(colorize("Test", 0, None))
    print(colorize("Test", 0, "normal"))
    print(colorize("Test", 1, "normal"))
    print(colorize("Test", 1, "green"))  # Should be green
    print(colorize("Test", 2, "normal"))
    print(colorize("Test", 2, "yellow"))  # Should be yellow
    print(colorize("Test", 3, "normal"))
    print(colorize("Test", 3, "red"))  # Should be red
    print(colorize("Test", 4, "normal"))
    print(colorize("Test", 4, "blue"))  # Should be blue
    print(colorize("Test", 5, "normal"))
    print(colorize("Test", 5, "magenta"))  # Should

# Generated at 2022-06-13 16:09:01.320663
# Unit test for function colorize
def test_colorize():
    lead = 'foo'
    num = 42
    color = 'blue'
    result = colorize(lead, num, color)
    assert lead == 'foo'
    assert num == 42
    assert color == 'blue'
    assert result == '\x1b[94mfoo=42  \x1b[0m'

# Generated at 2022-06-13 16:09:12.527908
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('test_host', dict(failures=0, unreachable=0, changed=0), True) == 'test_host'
    assert hostcolor('test_host', dict(failures=1, unreachable=0, changed=0), True) == 'test_host'
    assert hostcolor('test_host', dict(failures=0, unreachable=1, changed=0), True) == 'test_host'
    assert hostcolor('test_host', dict(failures=0, unreachable=0, changed=1), True) == 'test_host'
    assert hostcolor('test_host', dict(failures=0, unreachable=0, changed=0), False) == 'test_host'

# Generated at 2022-06-13 16:09:16.409478
# Unit test for function hostcolor
def test_hostcolor():
    host_with_stats = 'hostname'
    stats = dict(
        ok=2,
        changed=1,
        unreachable=0,
        skipped=1,
        failed=0,
    )

    print(hostcolor(host_with_stats, stats))

test_hostcolor()

# Generated at 2022-06-13 16:09:21.347506
# Unit test for function hostcolor
def test_hostcolor():
    test_stats = dict(
        ok=1,
        failures=0,
        unreachable=0,
        skipped=0,
        changed=0
    )
    assert hostcolor("myhost", test_stats) == "myhost                        "
    test_stats = dict(
        ok=0,
        failures=1,
        unreachable=0,
        skipped=0,
        changed=0
    )
    assert hostcolor("myhost", test_stats) != "myhost                        "


# Generated at 2022-06-13 16:09:27.401233
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('host', dict(failures=0, unreachable=0, changed=0)) == 'host                     '
    assert hostcolor('host', dict(failures=0, unreachable=0, changed=1)) == 'host                     '
    assert hostcolor('host', dict(failures=1, unreachable=0, changed=0)) == 'host                     '
    assert hostcolor('host', dict(failures=0, unreachable=1, changed=0)) == 'host                     '



# Generated at 2022-06-13 16:09:31.637265
# Unit test for function stringc
def test_stringc():
    assert stringc('hello', 'blue') == '\033[34mhello\033[0m'
    assert stringc('hello', 'blue', wrap_nonvisible_chars=True) == '\001\033[34m\002hello\001\033[0m\002'
    assert stringc('hello', 'rgb255255255') == '\033[38;5;15mhello\033[0m'
    assert stringc('hello', 'rgb000255000') == '\033[38;5;34mhello\033[0m'
    assert stringc('hello', 'color16') == '\033[38;5;16mhello\033[0m'
    assert stringc('hello', 'color0') == '\033[38;5;0mhello\033[0m'