

# Generated at 2022-06-13 15:59:40.879765
# Unit test for function stringc
def test_stringc():
    """Unit tests for function stringc"""
    assert parsecolor(u'blue') == u'34'
    assert parsecolor(u'bold') == u'1'
    assert parsecolor(u'green') == u'32'
    assert parsecolor(u'lightblue') == u'94'
    assert parsecolor(u'lightcyan') == u'96'
    assert parsecolor(u'lightgray') == u'37'
    assert parsecolor(u'lightgreen') == u'92'
    assert parsecolor(u'lightmagenta') == u'95'
    assert parsecolor(u'lightred') == u'91'
    assert parsecolor(u'magenta') == u'35'
    assert parsecolor(u'red') == u'31'
    assert parsec

# Generated at 2022-06-13 15:59:51.833144
# Unit test for function colorize
def test_colorize():
    # For the following tests, we assume that if the ANSIBLE_COLOR
    # environment variable is set to false that no color will be printed.
    # That is a reasonable assumption because that is what ANSIBLE_COLOR
    # is currently used for.

    # ensure that color is printed if ANSIBLE_COLOR is set to true.
    old_ac = C.ANSIBLE_NOCOLOR
    C.ANSIBLE_NOCOLOR = False
    lead = 'foo'
    num = 42
    color = 'blue'
    result = colorize(lead, num, color)
    expected = '\x1b[38;5;21mfoo=42  \x1b[0m'  # blue
    assert result == expected
    # restore the value of ANSIBLE_COLOR
    C.ANSIBLE_NOCOLOR = old

# Generated at 2022-06-13 16:00:02.020036
# Unit test for function stringc
def test_stringc():
    # Can't really test the output of curses since it is terminal dependent.
    # Just check that it doesn't throw an error.
    assert(stringc("test", "blue"))
    assert(stringc("test", "blue", True))
    assert(stringc("test", "blue", False))
    assert(stringc("test", "color10"))
    assert(stringc("test", "color10", True))
    assert(stringc("test", "color10", False))
    assert(stringc("test", "rgb100"))
    assert(stringc("test", "rgb100", True))
    assert(stringc("test", "rgb100", False))
    assert(stringc("test", "rgb001"))
    assert(stringc("test", "rgb001", True))

# Generated at 2022-06-13 16:00:04.531226
# Unit test for function hostcolor
def test_hostcolor():
    hc_result = hostcolor("test_host_name", dict(ok=1, changed=0, unreachable=0, failures=0))
    assert hc_result == 'test_host_name             \n', 'hostcolor produces invalid string'



# Generated at 2022-06-13 16:00:13.972791
# Unit test for function hostcolor
def test_hostcolor():
    # Host with no failure, no unreachable and no change
    stats_test1 = {'failures': 0, 'unreachable': 0, 'changed': 0}
    host_test1 = 'test1'
    assert (hostcolor(host_test1, stats_test1, True) == u"\x1b[32m%-37s\x1b[0m")

    # Host with unreachable
    stats_test2 = {'failures': 0, 'unreachable': 1, 'changed': 0}
    host_test2 = 'test2'
    assert (hostcolor(host_test2, stats_test2, True) == u"\x1b[31m%-37s\x1b[0m")

    # Host with failures

# Generated at 2022-06-13 16:00:21.404040
# Unit test for function parsecolor
def test_parsecolor():
    def _check_colors(color_func, color_name, color_value):
        if color_func == parsecolor:
            color_func(color_name) == color_value
            return
        color_func(color_name) == color_value
        color_func(color_name) == color_value

# Generated at 2022-06-13 16:00:27.385512
# Unit test for function stringc
def test_stringc():
    test_string = u"This is a test"
    test_color = u"red"
    test_colored_string = u'\x1b[31mThis is a test\x1b[0m'
    if stringc(test_string, test_color) == test_colored_string:
        return 0
    else:
        return 1

# --- end "pretty"



# Generated at 2022-06-13 16:00:32.633428
# Unit test for function colorize
def test_colorize():
    mock_stdout = []
    msg = 'This is a test'

    # First verify "not colorized"
    C.ANSIBLE_COLOR = False
    mock_stdout.append(colorize('LEAD', 'NUM', 'COLOR'))
    assert mock_stdout[0] == 'LEAD=NUM'

    # Now verify colorized
    C.ANSIBLE_COLOR = True
    mock_stdout.append(colorize('LEAD', 1, 'COLOR'))
    assert mock_stdout[1] == u"\u001b[38;5;208mLEAD=1   \u001b[0m"
# --- end "pretty"

# Generated at 2022-06-13 16:00:39.594122
# Unit test for function colorize
def test_colorize():
    def _(lead, num, color):
        return "%s=%-4s" % (lead, str(num))
    assert colorize(u'ok', 0, None) == _(u'ok', 0, None)
    assert colorize(u'ok', 1, u'blue') == stringc(_(u'ok', 1, None), u'blue')
    assert colorize(u'ok', 1, None) == _(u'ok', 1, None)



# Generated at 2022-06-13 16:00:46.201459
# Unit test for function hostcolor
def test_hostcolor():
    p = dict(unreachable=0, changed=0, failures=0)
    assert hostcolor('green', p) == '%-37s' % u'green'
    p1 = dict(unreachable=0, changed=1, failures=0)
    assert hostcolor('yellow', p1) == u'%-37s' % stringc(u'yellow', C.COLOR_CHANGED)
    p2 = dict(unreachable=1, changed=0, failures=0)
    assert hostcolor('red', p2) == u'%-37s' % stringc(u'red', C.COLOR_ERROR)



# Generated at 2022-06-13 16:00:54.772775
# Unit test for function stringc
def test_stringc():
    assert stringc('Keyboard not present', 'yellow') == '\x1b[33mKeyboard not present\x1b[0m'
    assert stringc('Keyboard not present', 'color255') == '\x1b[38;5;255mKeyboard not present\x1b[0m'
    assert stringc('Keyboard not present', 'rgb255255255') == '\x1b[38;5;15mKeyboard not present\x1b[0m'
    assert stringc('Keyboard not present', 'rgb000') == '\x1b[38;5;16mKeyboard not present\x1b[0m'

# Generated at 2022-06-13 16:01:05.183018
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('abc.example.com', {'ok': 0, 'changed': 0, 'unreachable': 0, 'failures': 0}) == u"%-26s" % 'abc.example.com'
    assert hostcolor('abc.example.com', {'ok': 1, 'changed': 0, 'unreachable': 0, 'failures': 0}) == u"%-37s" % u"abc.example.com"
    assert hostcolor('abc.example.com', {'ok': 0, 'changed': 1, 'unreachable': 0, 'failures': 0}) == u"%-37s" % u"abc.example.com"
    assert hostcolor('abc.example.com', {'ok': 0, 'changed': 0, 'unreachable': 1, 'failures': 0}) == u"%-37s" % u

# Generated at 2022-06-13 16:01:15.072380
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('localhost', {'failures': 2, 'changed': 0}) == u'localhost                '
    assert hostcolor('localhost', {'failures': 0, 'changed': 0}) == u'localhost                '
    assert hostcolor('localhost', {'failures': 0, 'unreachable': 0}) == u'localhost                '
    assert hostcolor('localhost', {'failures': 0, 'changed': 1}) == u'localhost                '
# --- end "pretty"

# --- begin "wrap"
#
# wrap - Wraps text at the specified column using the first space/tab/etc
# after the column.
#
# Copyright (C) 2008 Brian Nez <thedude at bri1 dot com>



# Generated at 2022-06-13 16:01:20.895531
# Unit test for function hostcolor
def test_hostcolor():
    class TestHostColor:
        def __init__(self):
            self.stats = {}

    host = 'example.com'
    hc = TestHostColor()
    # Test all cases
    for state in ('ok', 'changed', 'unreachable', 'failures'):
        for val in (0, 1):
            hc.stats = {state: val}
            yield (hostcolor, host, hc.stats, False, '{0:<26}'.format(host))
            yield (hostcolor, host, hc.stats, True,
                   stringc('{0:<26}'.format(host), C.COLOR_CODES[state]))



# Generated at 2022-06-13 16:01:29.457267
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor("localhost", dict(failures=0, unreachable=0, changed=0)) == u"localhost                      "
    assert hostcolor("localhost", dict(failures=1, unreachable=0, changed=0)) == u"\033[91mlocalhost\033[0m              "
    assert hostcolor("localhost", dict(failures=0, unreachable=1, changed=0)) == u"\033[91mlocalhost\033[0m              "
    assert hostcolor("localhost", dict(failures=0, unreachable=0, changed=1)) == u"\033[93mlocalhost\033[0m              "



# Generated at 2022-06-13 16:01:36.077197
# Unit test for function parsecolor
def test_parsecolor():
    print(u"Test parsecolor: all the sequences below should be the same color.")

# Generated at 2022-06-13 16:01:42.554814
# Unit test for function stringc
def test_stringc():
    if sys.version_info.major >= 3:
        try:
            unicode
        except NameError:
            unicode = str
        assert unicode(stringc('foo', 'red')) == u"\x1b[31mfoo\x1b[0m"
    else:
        assert stringc('foo', 'red') == '\x1b[31mfoo\x1b[0m'



# Generated at 2022-06-13 16:01:50.751457
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor(color=None) == u"38;5;16"
    # Test cases for parsecolor
    # Semicolon-separated parameter string matching the regex
    # pattern "color[0-9]+"
    assert parsecolor(color="color16") == u"38;5;16"
    assert parsecolor(color="color255") == u"38;5;255"
    # Semicolon-separated parameter string matching the regex
    # pattern "rgb([0-5])([0-5])([0-5])"
    assert parsecolor(color="rgb555") == u"38;5;231"
    assert parsecolor(color="rgb000") == u"38;5;16"
    # Semicolon-separated parameter string matching the regex
    # pattern "gray

# Generated at 2022-06-13 16:01:53.472832
# Unit test for function colorize
def test_colorize():
    assert colorize("x", 0, "green") == 'x=0   '
    assert colorize("x", 0, "red") == 'x=0   '


# Generated at 2022-06-13 16:02:02.544030
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor('red') == u'31'
    assert parsecolor('green') == u'32'
    assert parsecolor('yellow') == u'33'
    assert parsecolor('blue') == u'34'
    assert parsecolor('magenta') == u'35'
    assert parsecolor('cyan') == u'36'
    assert parsecolor('white') == u'37'
    assert parsecolor('dark red') == u'31'
    assert parsecolor('dark green') == u'32'
    assert parsecolor('dark yellow') == u'33'
    assert parsecolor('dark blue') == u'34'
    assert parsecolor('dark magenta') == u'35'
    assert parsecolor('dark cyan') == u'36'

# Generated at 2022-06-13 16:02:14.421503
# Unit test for function stringc
def test_stringc():
    """ tests the stringc function """
    print(stringc("This is the default color.", 'default'))
    print(stringc("This is black.", 'black'))
    print(stringc("This is red.", 'red'))
    print(stringc("This is green.", 'green'))
    print(stringc("This is yellow.", 'yellow'))
    print(stringc("This is blue.", 'blue'))
    print(stringc("This is magenta.", 'magenta'))
    print(stringc("This is cyan.", 'cyan'))
    print(stringc("This is white.", 'white'))



# Generated at 2022-06-13 16:02:25.147545
# Unit test for function parsecolor
def test_parsecolor():
    # This testcase is not exhaustive, it is a sanity check.
    assert parsecolor('black') == u'30'
    assert parsecolor('red') == u'31'
    assert parsecolor('green') == u'32'
    assert parsecolor('yellow') == u'33'
    assert parsecolor('blue') == u'34'
    assert parsecolor('magenta') == u'35'
    assert parsecolor('cyan') == u'36'
    assert parsecolor('lightgray') == u'37'
    assert parsecolor('gray0') == u'38;5;16'
    assert parsecolor('gray1') == u'38;5;232'
    assert parsecolor('gray9') == u'38;5;255'
    assert parsecolor('darkred') == u

# Generated at 2022-06-13 16:02:31.255800
# Unit test for function parsecolor
def test_parsecolor():
    for color in ('RANDOM', 'BLACK', 'WHITE', 'RED', 'GREEN', 'YELLOW',
                  'BLUE', 'MAGENTA', 'CYAN', 'BOLD_RED', 'BOLD_GREEN', 'BOLD_YELLOW',
                  'BOLD_BLUE', 'BOLD_MAGENTA', 'BOLD_CYAN', 'DARK_GRAY', 'LIGHT_GRAY'):
        assert parsecolor(color) == C.COLOR_CODES[color], "Unexpected color code for color %s" % color

    # Test gray colors
    gray_codes = [232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244]

# Generated at 2022-06-13 16:02:39.024927
# Unit test for function colorize
def test_colorize():
    "pytest unit test for colorize"
    assert colorize("foo", 0, None) == "foo=0   "
    assert colorize("foo", 1, None) == "foo=1   "
    assert colorize("foo", 2, True) == "foo=2   "
    assert colorize("foo", 3, False) == "foo=3   "
    assert colorize("foo", 4, "red") == "foo=4   "
    assert colorize("foo", 5, "blue") == "foo=5   "



# Generated at 2022-06-13 16:02:47.932609
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('foo', {'failures': 1, 'unreachable': 0, 'ok': 1, 'skipped': 0, 'changed': 0}) == u"foo\033[91m                \033[0m"
    assert hostcolor('foo', {'failures': 0, 'unreachable': 1, 'ok': 1, 'skipped': 0, 'changed': 0}) == u"foo\033[91m                \033[0m"
    assert hostcolor('foo', {'failures': 0, 'unreachable': 0, 'ok': 1, 'skipped': 0, 'changed': 1}) == u"foo\033[93m                \033[0m"
    assert hostcolor('foo', {'failures': 0, 'unreachable': 0, 'ok': 1, 'skipped': 0, 'changed': 0})

# Generated at 2022-06-13 16:02:55.672489
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor(u"foo", dict(failures=1, unreachable=0, changed=0)) == u"\033[31mfoo                \033[0m"
    assert hostcolor(u"foo", dict(failures=0, unreachable=1, changed=0)) == u"\033[31mfoo                \033[0m"
    assert hostcolor(u"foo", dict(failures=0, unreachable=0, changed=1)) == u"\033[33mfoo                \033[0m"
    assert hostcolor(u"foo", dict(failures=0, unreachable=0, changed=0), False) == u"foo                "



# Generated at 2022-06-13 16:03:05.234457
# Unit test for function colorize
def test_colorize():

    def _test(expected, lead, num, color):
        actual = colorize(lead, num, color)
        if expected != actual:
            raise AssertionError("colorize(%r, %r, %r) == %r != %r" %
                                 (lead, num, color, actual, expected))


# Generated at 2022-06-13 16:03:11.129091
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('localhost', dict(failures=1), True) == u'localhost'.ljust(37, ' ')
    assert hostcolor('localhost', dict(changed=1), True) == u'localhost'.ljust(37, ' ')
    assert hostcolor('localhost', dict(ok=1), True) == u'localhost'.ljust(37, ' ')



# Generated at 2022-06-13 16:03:19.344539
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('host.domain.tld', dict(changed=1), True) == u'\x1b[0;36mhost.domain.tld\x1b[0m      '
    assert hostcolor('host.domain.tld', dict(changed=1), False) == u'host.domain.tld             '
    assert hostcolor('host.domain.tld', dict(unreachable=1), True) == u'\x1b[0;31mhost.domain.tld\x1b[0m      '
    assert hostcolor('host.domain.tld', dict(unreachable=1), False) == u'host.domain.tld             '

# Generated at 2022-06-13 16:03:27.796177
# Unit test for function hostcolor
def test_hostcolor():
    def test(expected, ansible_color, color, stats):
        global ANSIBLE_COLOR
        ANSIBLE_COLOR = ansible_color
        assert expected == hostcolor('host', stats, color)

    # No color
    test(u"host                    ", False, True, {'failures': 0, 'unreachable': 0, 'changed': 0})
    test(u"host                    ", False, False, {'failures': 0, 'unreachable': 0, 'changed': 0})

    # Use default random color for odd stats, even with color enabled
    test(u"host                    ", True, True, {'failures': 1, 'unreachable': 1, 'changed': 1})
    test(u"host                    ", True, True, {'failures': 2, 'unreachable': 2, 'changed': 2})

   

# Generated at 2022-06-13 16:03:42.500050
# Unit test for function parsecolor
def test_parsecolor():
  assert(parsecolor('black') == '30')
  assert(parsecolor('red') == '31')
  assert(parsecolor('green') == '32')
  assert(parsecolor('yellow') == '33')
  assert(parsecolor('blue') == '34')
  assert(parsecolor('magenta') == '35')
  assert(parsecolor('cyan') == '36')
  assert(parsecolor('white') == '37')
  assert(parsecolor('default') == '39')
  assert(parsecolor('black_bold') == '30;1')
  assert(parsecolor('red_bold') == '31;1')
  assert(parsecolor('green_bold') == '32;1')
  assert(parsecolor('yellow_bold') == '33;1')

# Generated at 2022-06-13 16:03:50.783458
# Unit test for function hostcolor
def test_hostcolor():
    def check(host, stats, color=True):
        assert hostcolor(host, stats, color)

    check("test.example.org", {"failures": 0, "unreachable": 0, "changed": 0})
    check("test.example.org", {"failures": 1, "unreachable": 0, "changed": 0})
    check("test.example.org", {"failures": 0, "unreachable": 1, "changed": 0})
    check("test.example.org", {"failures": 0, "unreachable": 0, "changed": 1})
    check("test.example.org", {"failures": 0, "unreachable": 0, "changed": 0}, False)

# Generated at 2022-06-13 16:04:02.544852
# Unit test for function stringc
def test_stringc():
    """Test function stringc."""
    # Standard colors
    assert stringc('success', 'green') == '\033[32msuccess\033[0m'
    assert stringc('error', 'red') == '\033[31merror\033[0m'
    assert stringc('warning', 'yellow') == '\033[33mwarning\033[0m'
    assert stringc('info', 'blue') == '\033[34minfo\033[0m'

    # Foreground colors
    for i in range(0, 256):
        assert stringc(str(i), 'color%d' % i)

    # RGB colors

# Generated at 2022-06-13 16:04:07.208026
# Unit test for function stringc
def test_stringc():
    assert stringc(u"test", "green") == (
        u"\n".join([u"\033[38;5;2mtest\033[0m"])
    )
    assert stringc(u"test\ntest", "green") == (
        u"\n".join([u"\033[38;5;2mtest\033[0m",
                    u"\033[38;5;2mtest\033[0m"])
    )
    assert stringc(u"test", "rgb255255255") == (
        u"\n".join([u"\033[38;5;15mtest\033[0m"])
    )

# Generated at 2022-06-13 16:04:17.026100
# Unit test for function stringc
def test_stringc():
    """Test cases for function stringc."""

    assert stringc(u"foo", u"blue") == u"\033[94mfoo\033[0m"
    assert stringc(u"bar", u"rgb124") == u"\033[38;5;69mbar\033[0m"
    assert stringc(u"quux", u"gray8") == u"\033[38;5;244mquux\033[0m"
    assert stringc(u"foo\nbar", u"blue") == u"\033[94mfoo\nbar\033[0m"


# --- end "pretty"

# for backwards compatibility
stringc = stringc

# Generated at 2022-06-13 16:04:23.119470
# Unit test for function hostcolor
def test_hostcolor():
    stats = {
        'changed': 0,
        'dark': 0,
        'failures': 1,
        'ok': 1,
        'processed': 2,
        'skipped': 0,
        'unreachable': 0
    }
    assert hostcolor(u"Test 1", stats, color=False) == u"Test 1               "
    assert hostcolor(u"Test 2", stats, color=True) == u"\033[31mTest 2          \033[0m"

    stats = {
        'changed': 1,
        'dark': 0,
        'failures': 0,
        'ok': 1,
        'processed': 2,
        'skipped': 0,
        'unreachable': 0
    }

# Generated at 2022-06-13 16:04:32.934126
# Unit test for function stringc
def test_stringc():
    """Test that stringc produces the expected result for the most
    common colors.  The purpose of these test cases is not to exhaustively
    test the SGR sequences produced by stringc, but rather to test that the
    most common colors are being produced.

    As a side effect, this test case exhaustively tests the colors
    available for the 'color' color argument to stringc.

    """
    # The colors here were chosen by taking the colors from colors/*.py.

# Generated at 2022-06-13 16:04:42.007563
# Unit test for function colorize
def test_colorize():

    # Test for colorize without color
    ANSIBLE_COLOR = False
    assert colorize('foo1', 0, None) == 'foo1=0   '
    assert colorize('foo2', 0, 'blue') == 'foo2=0   '
    assert colorize('foo3', 10, 'blue') == 'foo3=10  '

    # Test for colorize with color
    ANSIBLE_COLOR = True
    assert colorize('foo1', 0, 'blue') == 'foo1=0   '
    assert colorize('foo2', 0, 'red') == 'foo2=0   '
    assert colorize('foo3', 10, 'blue') == '\n'.join(['\x1b[94mfoo3=10  \x1b[0m'])


# Generated at 2022-06-13 16:04:51.477458
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor(u'color254')           == u'38;5;254'
    assert parsecolor(u'rgb255255255')       == u'38;5;231'
    assert parsecolor(u'rgb000255000')       == u'38;5;34'
    assert parsecolor(u'rgb255000100')       == u'38;5;202'
    assert parsecolor(u'gray0')              == u'38;5;232'
    assert parsecolor(u'gray23')             == u'38;5;255'



# Generated at 2022-06-13 16:04:55.201664
# Unit test for function stringc
def test_stringc():
    import unittest
    from nose.plugins.skip import SkipTest

    try:
        assert stringc('test', 'blue') == '\x1b[34mtest\x1b[0m'
    except AssertionError:
        raise SkipTest()

# --- end of "pretty"



# Generated at 2022-06-13 16:05:02.563952
# Unit test for function stringc
def test_stringc():
    print(stringc(u"Hello World", u"red") +
          stringc(u"Hello World", u"white on_red"))


# Generated at 2022-06-13 16:05:12.975056
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor("localhost", dict(changed=1, failures=0, unreachable=0),
                     True) == u"\033[92m%-37s\033[0m" % u"localhost"
    assert hostcolor("localhost", dict(changed=0, failures=1, unreachable=0),
                     True) == u"\033[91m%-37s\033[0m" % u"localhost"
    assert hostcolor("localhost", dict(changed=0, failures=0, unreachable=1),
                     True) == u"\033[91m%-37s\033[0m" % u"localhost"
    assert hostcolor("localhost", dict(changed=0, failures=0, unreachable=0),
                     True) == u"\033[92m%-37s\033[0m" % u"localhost"
    assert host

# Generated at 2022-06-13 16:05:22.114922
# Unit test for function colorize
def test_colorize():
    """The colorize function should return a string with the correct color code
    when ANSIBLE_COLOR is turned on, and not otherwise."""
    import ansible.constants as C
    import ansible.utils as utils

    P = utils.defaults.__play_context_wrapper__ # Shorthand
    T = utils.defaults.__task_wrapper__ # Shorthand

    # This is a pretty hackish way to do it, but we need to test colorize()
    # in the context of a class which has the color constants defined, so
    # we'll just reuse the task class and play class wrappers

    # Turn ANSIBLE_COLOR on
    utils.defaults.ANSIBLE_COLOR = True

    # Define some tasks for testing

# Generated at 2022-06-13 16:05:31.304091
# Unit test for function stringc
def test_stringc():
    '''Unit test for function stringc'''
    if ANSIBLE_COLOR:
        assert stringc('text', 'blue') == u"\033[34mtext\033[0m"
        assert stringc('text', 'rgb255') == u"\033[38;5;231mtext\033[0m"
        assert stringc('text', 'rgb125') == u"\033[38;5;21mtext\033[0m"
        assert stringc('text', 'rgb050') == u"\033[38;5;11mtext\033[0m"
        assert stringc('text', 'rgb125', True) == u"\001\033[38;5;21m\002text\001\033[0m\002"
    else:
        assert stringc('text', 'blue')

# Generated at 2022-06-13 16:05:40.855355
# Unit test for function stringc
def test_stringc():
    class A(object):
        def __str__(self):
            return "A"

    assert 'ABC' == stringc('ABC', 'black')
    assert '\x1b[1;31mABC\x1b[0m' == stringc('ABC', 'red', wrap_nonvisible_chars=True)
    assert '\n'.join(['\x1b[38;5;124mfoo', 'bar\x1b[0m']) == stringc("foo\nbar", 'color124')
    assert '\x1b[38;5;124mA\x1b[0m' == stringc(A(), 'color124')

# --- end of "pretty" ---

__all__ = ['stringc', 'colorize', 'hostcolor']

# Generated at 2022-06-13 16:05:49.814433
# Unit test for function hostcolor
def test_hostcolor():
    stats_ok = {'ok': 1, 'failures': 0, 'skipped': 0,
                'unreachable': 0, 'changed': 0}
    stats_changed = {'ok': 0, 'failures': 0, 'skipped': 0,
                     'unreachable': 0, 'changed': 1}
    stats_failure = {'ok': 0, 'failures': 1, 'skipped': 0,
                     'unreachable': 0, 'changed': 0}
    stats_unreachable = {'ok': 0, 'failures': 0, 'skipped': 0,
                         'unreachable': 1, 'changed': 0}
    assert u'localhost' == hostcolor(u'localhost', stats_ok, False)
    assert u'localhost' == hostcolor(u'localhost', stats_changed, False)

# Generated at 2022-06-13 16:06:00.802619
# Unit test for function hostcolor
def test_hostcolor():
    ''' hostcolor() returns string with non-printing color control chars '''
    class struct:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    host = "test.example.com"
    stats = dict(
        failures=0,
        unreachable=0,
        changed=0,
    )
    expected_color = u"\u001b[0;32m%-37s\u001b[0m" % host
    assert hostcolor(host, stats) == host

    stats = dict(
        failures=1,
        unreachable=0,
        changed=0,
    )
    assert hostcolor(host, stats) == expected_color


# Generated at 2022-06-13 16:06:08.054268
# Unit test for function hostcolor
def test_hostcolor():
    test_data = [
        ('127.0.0.1', {'failures': 0, 'unreachable': 0, 'changed': 0}, u'127.0.0.1'),
        ('127.0.0.1', {'failures': 1, 'unreachable': 1, 'changed': 0}, u'\x1b[31m127.0.0.1\x1b[0m'),
        ('127.0.0.1', {'failures': 0, 'unreachable': 0, 'changed': 1}, u'\x1b[32m127.0.0.1\x1b[0m'),
    ]
    for host, stats, expected in test_data:
        assert(hostcolor(host, stats) == expected)

# -- end "pretty"

# Generated at 2022-06-13 16:06:16.494326
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor("host1", {"failures": 1, "changed": 0, "unreachable": 0, "ok": 0}) == u"host1                    "
    assert hostcolor("host2", {"failures": 0, "changed": 1, "unreachable": 0, "ok": 0}) == u"host2                    "
    assert hostcolor("host3", {"failures": 0, "changed": 0, "unreachable": 1, "ok": 0}) == u"host3                    "
    assert hostcolor("host4", {"failures": 0, "changed": 0, "unreachable": 0, "ok": 1}) == u"host4                    "

# Generated at 2022-06-13 16:06:26.842585
# Unit test for function stringc

# Generated at 2022-06-13 16:06:44.067417
# Unit test for function stringc
def test_stringc():
    """Test function stringc."""

    # Test foreground colors
    fg_colors = [
        'black',
        'red',
        'green',
        'yellow',
        'blue',
        'magenta',
        'cyan',
        'white',
    ]
    for fg_color in fg_colors:
        # use write directly to sys.stdout in order to avoid NL transformation
        sys.stdout.write(stringc("stringc(fg='%s')\n" % fg_color, fg_color))

    # Test foreground color codes

# Generated at 2022-06-13 16:06:54.874712
# Unit test for function stringc
def test_stringc():
    assert stringc("hello", 'red') == u"\033[31mhello\033[0m"
    assert stringc("hello\nworld", 'red') == u"\033[31mhello\033[0m\n\033[31mworld\033[0m"
    assert stringc("hello\nworld", 'rgb255255255') == u"\033[38;5;15mhello\033[0m\n\033[38;5;15mworld\033[0m"
    assert stringc("hello\nworld", 'rgb000255000') == u"\033[38;5;34mhello\033[0m\n\033[38;5;34mworld\033[0m"

# Generated at 2022-06-13 16:07:03.314228
# Unit test for function hostcolor
def test_hostcolor():
    '''Test hostcolor'''
    # No changes, no failures, no unreachable
    host = u'testhost'
    stats = {
        'changed': 0,
        'failures': 0,
        'ok': 1,
        'skipped': 0,
        'unreachable': 0
    }

    # No changes, no failures, no unreachable, color on
    assert hostcolor(host, stats) == u'%-37s' % stringc(host, C.COLOR_OK)

    # Changes, no failures, no unreachable
    stats['changed'] = 1

    # Changes, no failures, no unreachable, color on
    assert hostcolor(host, stats) == u'%-37s' % stringc(host, C.COLOR_CHANGED)

    # No changes, failures, no unreachable

# Generated at 2022-06-13 16:07:12.010594
# Unit test for function hostcolor
def test_hostcolor():
    """ Unit tests for function hostcolor
    """
    assert hostcolor("localhost", {"failures": 0, "unreachable": 0, "changed": 0}, True) == u"%-37s" % stringc("localhost", C.COLOR_OK)
    assert hostcolor("localhost", {"failures": 0, "unreachable": 0, "changed": 1}, True) == u"%-37s" % stringc("localhost", C.COLOR_CHANGED)
    assert hostcolor("localhost", {"failures": 0, "unreachable": 1, "changed": 0}, True) == u"%-37s" % stringc("localhost", C.COLOR_ERROR)

# --- end "pretty"

# Generated at 2022-06-13 16:07:23.272254
# Unit test for function stringc
def test_stringc():
    # failure cases
    assert not re.match(r"(\x1b|\\x1b)\[", stringc('hello world', 'blue'))
    assert not re.match(r"(\x1b|\\x1b)\[", stringc('hello world', 'red'))
    assert not re.match(r"(\x1b|\\x1b)\[", stringc('hello world', 'foo'))

    # success cases
    assert re.match(r"(\x1b|\\x1b)\[1;36m", stringc('hello world', 'blue'))
    assert re.match(r"(\x1b|\\x1b)\[1;31m", stringc('hello world', 'red'))

# Generated at 2022-06-13 16:07:33.728703
# Unit test for function colorize
def test_colorize():
    ansible_color = ANSIBLE_COLOR
    nocolor_results = (
        u"ok=3   ",
        u"changed=2  ",
        u"unreachable=1 ",
        u"failed=0         ",
    )
    color_results = (
        u"ok=3   ",
        u"\x1b[0;32;49mchanged=2  \x1b[0m",
        u"\x1b[0;31;49munreachable=1 \x1b[0m",
        u"\x1b[0;33;49mfailed=0         \x1b[0m",
    )


# Generated at 2022-06-13 16:07:39.772927
# Unit test for function hostcolor
def test_hostcolor():
    """
    >>> stats = dict(failures=0, unreachable=0, changed=0)
    >>> hostcolor('foobar', stats, False)
    'foobar             '
    >>> hostcolor('foobar', stats)
    '\\x1b[32mfoobar             \\x1b[0m'
    >>> stats['failures'] = 1
    >>> stats['unreachable'] = 1
    >>> hostcolor('foobar', stats)
    '\\x1b[31mfoobar             \\x1b[0m'
    >>> stats['failures'] = 0
    >>> hostcolor('foobar', stats)
    '\\x1b[33mfoobar             \\x1b[0m'
    """



# Generated at 2022-06-13 16:07:45.635742
# Unit test for function hostcolor
def test_hostcolor():
    host1 = 'example1.com'
    stats1 = {'ok': 0, 'changed': 0, 'unreachable': 0, 'failures': 0}
    host2 = 'example2.com'
    stats2 = {'ok': 0, 'changed': 1, 'unreachable': 0, 'failures': 0}
    host3 = 'example3.com'
    stats3 = {'ok': 0, 'changed': 0, 'unreachable': 0, 'failures': 1}
    host4 = 'example4.com'
    stats4 = {'ok': 0, 'changed': 2, 'unreachable': 0, 'failures': 0}
    host5 = 'example5.com'
    stats5 = {'ok': 0, 'changed': 0, 'unreachable': 0, 'failures': 2}

# Generated at 2022-06-13 16:07:55.577046
# Unit test for function colorize
def test_colorize():
    print("colorize() should print 'ok' in green if ANSIBLE_COLOR=True")
    print("ok" if (stringc("ok", 'green', wrap_nonvisible_chars=True) == u"\001\033[32m\002ok\001\033[0m\002") else "not ok")


# --- end "pretty"

# --- begin "ansible-playbook"
#
#  Ansible is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with Ansible.  If not, see <http://www.gnu.

# Generated at 2022-06-13 16:08:05.823320
# Unit test for function hostcolor
def test_hostcolor():
    test_string = u"test.example.com"
    color = "error"
    assert hostcolor(test_string, dict(changed=0, failures=1), color=True) == u'%-37s' % stringc(test_string, C.COLOR_ERROR)
    color = "ok"
    assert hostcolor(test_string, dict(changed=0, failures=0), color=True) == u'%-37s' % stringc(test_string, C.COLOR_OK)
    color = "changed"
    assert hostcolor(test_string, dict(changed=1, failures=0), color=True) == u'%-37s' % stringc(test_string, C.COLOR_CHANGED)
    color = None

# Generated at 2022-06-13 16:08:23.361923
# Unit test for function hostcolor
def test_hostcolor():

    assert hostcolor('server01.example.com', dict(changed=2), color=False) == u'server01.example.com         '
    assert hostcolor('server02.example.com', dict(changed=0), color=False) == u'server02.example.com         '

    assert hostcolor('server03.example.com', dict(changed=2), color=True) == u'\033[0;32mserver03.example.com   \033[0m'
    assert hostcolor('server04.example.com', dict(changed=0), color=True) == u'\033[0;32mserver04.example.com   \033[0m'


# Generated at 2022-06-13 16:08:32.482250
# Unit test for function stringc

# Generated at 2022-06-13 16:08:40.547199
# Unit test for function stringc
def test_stringc():
    assert stringc("foo", "blue") == u"\033[34mfoo\033[0m"
    assert stringc("foo", "rgb204") == u"\033[38;5;204mfoo\033[0m"
    assert stringc("foo", "rgb220", wrap_nonvisible_chars=True) == u"\001\033[38;5;220m\002foo\001\033[0m\002"



# Generated at 2022-06-13 16:08:48.434305
# Unit test for function colorize
def test_colorize():
    s = colorize("foo", 0, None)
    if s != "foo=0   ":
        raise AssertionError()
    s = colorize("foo", 0, 'black')
    if s != "foo=0   ":
        raise AssertionError()
    s = colorize("foo", 123, 'black')
    if s != "foo=123 ":
        raise AssertionError()
    s = colorize("foo", 1234, 'black')
    if s != "foo=1234":
        raise AssertionError()



# Generated at 2022-06-13 16:08:59.211110
# Unit test for function colorize
def test_colorize():
    # needs 'from __future__ import print_function'
    import sys

    def _print(*args, **kwargs):
        print(*args, **kwargs)
        sys.stdout.flush()

    # Retrieve the current terminal width

# Generated at 2022-06-13 16:09:04.686741
# Unit test for function hostcolor
def test_hostcolor():
    if ANSIBLE_COLOR:
        # COLOR_ERROR
        assert hostcolor('test_host', {'failures':1, 'unreachable':0, 'ok':0, 'changed':0, 'skipped':0}, True) == stringc('test_host', C.COLOR_ERROR)

        # COLOR_CHANGED
        assert hostcolor('test_host', {'failures':0, 'unreachable':0, 'ok':0, 'changed':1, 'skipped':0}, True) == stringc('test_host', C.COLOR_CHANGED)

        # COLOR_OK

# Generated at 2022-06-13 16:09:15.056728
# Unit test for function stringc
def test_stringc():
    """Unit test for function stringc"""
    assert stringc('foo', 'blue') == u'\033[34mfoo\033[0m'
    assert stringc('foo', 'color3') == u'\033[38;5;11mfoo\033[0m'
    assert stringc('foo', 'rgb255') == u'\033[38;5;231mfoo\033[0m'
    assert stringc('bar', 'rgb255') == u'\033[38;5;231mbar\033[0m'
    assert stringc('foo', 'gray3') == u'\033[38;5;245mfoo\033[0m'
#
# --- end of "pretty"
#

# FIXME: make this a class, with color names as members,
#        and make it look up the

# Generated at 2022-06-13 16:09:22.782981
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor("test.example.com", dict(failures=0, unreachable=0, changed=0)) == u"test.example.com            "
    assert hostcolor("test.example.com", dict(failures=1, unreachable=0, changed=0)) == u"test.example.com            "
    assert hostcolor("test.example.com", dict(failures=0, unreachable=1, changed=0)) == u"test.example.com            "
    assert hostcolor("test.example.com", dict(failures=0, unreachable=0, changed=1)) == u"test.example.com            "
    assert hostcolor("test.example.com", dict(failures=1, unreachable=0, changed=1)) == u"test.example.com            "

# Generated at 2022-06-13 16:09:31.020879
# Unit test for function stringc
def test_stringc():
    # ANSIBLE_COLOR is zero, no color should be printed
    global ANSIBLE_COLOR
    ANSIBLE_COLOR = False
    assert ANSIBLE_COLOR is False
    assert stringc('This is a test', 'black') == 'This is a test'

    # ANSIBLE_COLOR is one, color should be printed
    ANSIBLE_COLOR = True
    assert stringc('This is a test', 'black') == '\033[30mThis is a test\033[0m'

    # Test non-visible characters wrapping
    ANSIBLE_COLOR = True
    assert stringc('This is a test', 'black', True) == '\001\033[30m\002This is a test\001\033[0m\002'

