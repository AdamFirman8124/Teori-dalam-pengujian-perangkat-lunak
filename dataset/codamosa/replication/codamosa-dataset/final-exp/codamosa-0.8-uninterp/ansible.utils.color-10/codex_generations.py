

# Generated at 2022-06-13 15:59:43.684014
# Unit test for function hostcolor
def test_hostcolor():
    hc = hostcolor("testhost", dict(ok=10, changed=5, unreachable=0, failed=0))
    assert hc == "testhost                       "

    hc = hostcolor("testhost", dict(ok=10, changed=0, unreachable=0, failed=5))
    assert hc == "testhost                       "

    hc = hostcolor("testhost", dict(ok=10, changed=5, unreachable=0, failed=5))
    assert hc == "testhost                       "

    hc = hostcolor("testhost", dict(ok=5, changed=5, unreachable=0, failed=5))
    assert hc == "testhost                       "

    hc = hostcolor("testhost", dict(ok=10, changed=0, unreachable=0, failed=0))

# Generated at 2022-06-13 15:59:53.700423
# Unit test for function stringc
def test_stringc():
    """Unit test for function stringc."""
    print(stringc("Hello World", color="red", wrap_nonvisible_chars=False))
    print(stringc("Hello World", color="blue", wrap_nonvisible_chars=False))
    print(stringc("Hello World", color="yellow", wrap_nonvisible_chars=False))
    print(stringc("Hello World", color="magenta", wrap_nonvisible_chars=False))
    print(stringc("Hello World", color="cyan", wrap_nonvisible_chars=False))
    print(stringc("Hello World", color="white", wrap_nonvisible_chars=False))
    print(stringc("Hello World", color="green", wrap_nonvisible_chars=False))

# Generated at 2022-06-13 15:59:58.953725
# Unit test for function stringc
def test_stringc():
    """Test stringc function."""

    # Iterate over color definitions
    for color in C.COLOR_CODES.keys():
        # Skip 'NOCOLOR'
        if color == "NOCOLOR":
            continue

        # Check, that certain color really prints in corresponding color
        if color in ("BLACK", "WHITE", "GREY", "BOLD"):
            continue
        if color in ("RED", "GREEN", "YELLOW"):
            assert re.match(r"\033\[1;31m.*\033\[0m", stringc(u"test", color)), (
                "failed to print 'test' in color '%s'" % color)

# Generated at 2022-06-13 16:00:01.231029
# Unit test for function stringc
def test_stringc():
    """Pass if colorized strings match the expected format."""
    for color, code in C.COLOR_CODES.items():
        yield check_stringc, color, code



# Generated at 2022-06-13 16:00:08.204711
# Unit test for function parsecolor
def test_parsecolor():

    assert(parsecolor(u"red") == u'31')
    assert(parsecolor(u"blue") == u'34')
    assert(parsecolor(u"yellow") == u'33')
    assert(parsecolor(u"31") == u'31')
    assert(parsecolor(u"34") == u'34')
    assert(parsecolor(u"33") == u'33')
    assert(parsecolor(u"ansible_red") == u'31')
    assert(parsecolor(u"ansible_blue") == u'34')
    assert(parsecolor(u"ansible_yellow") == u'33')
    assert(parsecolor(u"rgb123") == u'38;5;45')

# Generated at 2022-06-13 16:00:15.790658
# Unit test for function hostcolor
def test_hostcolor():
    """Unit test for function hostcolor"""
    p = dict(failed=0, unreachable=0, changed=0, ok=1)
    print(hostcolor("localhost", p))

    p = dict(failed=0, unreachable=0, changed=1, ok=0)
    print(hostcolor("localhost", p))

    p = dict(failed=1, unreachable=0, changed=0, ok=0)
    print(hostcolor("localhost", p))

    p = dict(failed=0, unreachable=1, changed=0, ok=0)
    print(hostcolor("localhost", p))


# Generated at 2022-06-13 16:00:24.703767
# Unit test for function hostcolor
def test_hostcolor():
    # Basic test - only verify the color string is in the output
    for color in ['error', 'changed', 'ok']:
        assert hostcolor('127.0.0.1', {'failures': 0, 'unreachable': 0, 'changed': 0}, color)
        assert hostcolor('127.0.0.1', {'failures': 0, 'unreachable': 0, 'changed': 1}, color)
        assert hostcolor('127.0.0.1', {'failures': 1, 'unreachable': 0, 'changed': 0}, color)
        assert hostcolor('127.0.0.1', {'failures': 1, 'unreachable': 0, 'changed': 1}, color)

    # Verify the no color output

# Generated at 2022-06-13 16:00:29.406156
# Unit test for function stringc
def test_stringc():
    import sys
    import textwrap
    if not ANSIBLE_COLOR:
        print(u"Terminal does not support color, skipping")
        return
    def e(s):
        s = s.expandtabs()
        return "\033[%sm%s\033[0m" % (s.strip().split(u"\n")[0],
                                      u"\n".join(s.strip().split(u"\n")[1:]).rstrip())
    def es(s):
        return "\001\033[%sm\002%s\001\033[0m\002" % (s.strip().split(u"\n")[0],
                                                      u"\n".join(s.strip().split(u"\n")[1:]).rstrip())

# Generated at 2022-06-13 16:00:40.928836
# Unit test for function stringc
def test_stringc():
    assert stringc('foo', 'red', True) == u"\001\033[38;5;1m\002foo\001\033[0m\002"
    assert stringc('foo', 'red') == u"\033[38;5;1mfoo\033[0m"
    assert stringc('foo', 'color16', True) == u"\001\033[38;5;16m\002foo\001\033[0m\002"
    assert stringc('foo', 'rgb3', True) == u"\001\033[38;5;14m\002foo\001\033[0m\002"
    assert stringc('foo', 'rgb123', True) == u"\001\033[38;5;75m\002foo\001\033[0m\002"
    assert stringc

# Generated at 2022-06-13 16:00:47.606148
# Unit test for function stringc
def test_stringc():
    """Test function stringc.

    >>> test_stringc()
    """

    # Make sure all color codes work
    for color in C.COLOR_CODES:
        stringc('color %s' % color, color)

    # Make sure foreground 16-255 works
    for color in range(16, 256):
        stringc('color %d' % color, 'color%d' % color)

    # Make sure rgb works
    for red in range(6):
        for green in range(6):
            for blue in range(6):
                color = 'rgb%d%d%d' % (red, green, blue)
                stringc('color %s' % color, color)

    # Make sure gray works
    for gray in range(23):
        color = 'gray%d' % gray

# Generated at 2022-06-13 16:01:03.302005
# Unit test for function hostcolor
def test_hostcolor():
    """
    Run unit tests for Hostcolor
    Needs to be provided a specific color scheme in order to
    get consistent results
    """

    host = 'host'
    stats = {'changed':0, 'dark':0, 'failures':0, 'ok':0, 'processed':1,
             'skipped':0, 'unreachable':0}

    assert hostcolor(host, stats, color=True) == u'host                 \033[0m'
    stats['ok'] = 1
    assert hostcolor(host, stats, color=True) == u'host                 \033[0;32m'
    stats['changed'] = 1
    assert hostcolor(host, stats, color=True) == u'host                 \033[0;33m'
    stats['unreachable'] = 1

# Generated at 2022-06-13 16:01:14.742318
# Unit test for function stringc
def test_stringc():
    print(stringc("hello", "red", wrap_nonvisible_chars=False))
    print(stringc("hello", "green", wrap_nonvisible_chars=False))
    print(stringc("hello", "blue", wrap_nonvisible_chars=False))
    print(stringc("hello", "rgb255255255", wrap_nonvisible_chars=False))
    print(stringc("hello", "rgb000255000", wrap_nonvisible_chars=False))
    print(stringc("hello", "rgb000000255", wrap_nonvisible_chars=False))
    print(stringc("hello", "gray0", wrap_nonvisible_chars=False))
    print(stringc("hello", "gray15", wrap_nonvisible_chars=False))

# Generated at 2022-06-13 16:01:18.225283
# Unit test for function stringc
def test_stringc():
    # tests for function stringc
    test_color = 'blue'
    sample_string = 'sample string to print'
    test_stringc = stringc(sample_string, test_color)
    assert(test_stringc)
    assert(test_stringc.startswith(u'\033[0;34m'))
    assert(test_stringc.endswith(u'\033[0m'))

# Generated at 2022-06-13 16:01:26.399496
# Unit test for function stringc
def test_stringc():
    """ Tests for stringc() """
    assert stringc("Test String", "green") == u"\033[32mTest String\033[0m"
    assert stringc("Test String", "color15") == u"\033[38;5;15mTest String\033[0m"
    assert stringc("Test String", "rgb542") == u"\033[38;5;2mTest String\033[0m"
    assert stringc("Test String", "gray7") == u"\033[38;5;243mTest String\033[0m"

# Generated at 2022-06-13 16:01:29.372176
# Unit test for function stringc
def test_stringc():
    test_str = "This is a test."
    assert stringc(test_str, 'blue') == "\033[34mThis is a test.\033[0m"


# --- end "pretty"


# --- start of secho code ---


# Generated at 2022-06-13 16:01:34.745720
# Unit test for function stringc
def test_stringc():
    assert stringc("hello", 'blue') == u'\x1b[34mhello\x1b[0m'
    assert stringc("hello", 'badcolor') == u'\x1b[39mhello\x1b[0m'
    assert stringc("hello", 'rgb255000') == u'\x1b[38;5;9mhello\x1b[0m'
    assert stringc("hello", 'rgb255255255') == u'\x1b[38;5;15mhello\x1b[0m'

# Generated at 2022-06-13 16:01:39.506186
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor("localhost : ok=1    changed=1    unreachable=0    failed=0", dict(ok=1, changed=1, unreachable=0, failed=0)) == u"localhost : ok=1    changed=1    unreachable=0    failed=0"


# Generated at 2022-06-13 16:01:48.820769
# Unit test for function stringc
def test_stringc():
    assert stringc('test', 'black') == u"\033[30mtest\033[0m"
    assert stringc('test', 'red') == u"\033[31mtest\033[0m"
    assert stringc('test', 'green') == u"\033[32mtest\033[0m"
    assert stringc('test', 'yellow') == u"\033[33mtest\033[0m"
    assert stringc('test', 'blue') == u"\033[34mtest\033[0m"
    assert stringc('test', 'magenta') == u"\033[35mtest\033[0m"
    assert stringc('test', 'cyan') == u"\033[36mtest\033[0m"

# Generated at 2022-06-13 16:01:55.067895
# Unit test for function parsecolor
def test_parsecolor():
    def ck(code, color_name):
        assert code == parsecolor(color_name), \
            'Color name {0} does not match expected color code {1}'.format(
                color_name, code)
    ck(u'38;5;187', 'red')
    ck(u'38;5;37', 'yellow')
    ck(u'38;5;28', 'green')
    ck(u'38;5;63', 'blue')
    ck(u'38;5;180', 'pink')
    ck(u'38;5;129', 'cyan')
    ck(u'38;5;45', 'white')
    ck(u'38;5;92', 'black')
    ck(u'38;5;15', 'grey')

# Generated at 2022-06-13 16:02:03.691504
# Unit test for function hostcolor
def test_hostcolor():
    # no color
    assert hostcolor('host', {'failures': 0, 'unreachable': 0, 'changed': 0}, False) == u"%-26s" % 'host'
    assert hostcolor('host', {'failures': 0, 'unreachable': 0, 'changed': 1}, False) == u"%-26s" % 'host'
    assert hostcolor('host', {'failures': 0, 'unreachable': 1, 'changed': 0}, False) == u"%-26s" % 'host'
    assert hostcolor('host', {'failures': 1, 'unreachable': 0, 'changed': 0}, False) == u"%-26s" % 'host'

    # color

# Generated at 2022-06-13 16:02:17.534182
# Unit test for function parsecolor
def test_parsecolor():
    if parsecolor("none") != u"38;5;255": sys.exit(1)
    if parsecolor("black") != u"38;5;0": sys.exit(2)
    if parsecolor("red") != u"38;5;1": sys.exit(3)
    if parsecolor("green") != u"38;5;2": sys.exit(4)
    if parsecolor("yellow") != u"38;5;3": sys.exit(5)
    if parsecolor("blue") != u"38;5;4": sys.exit(6)
    if parsecolor("magenta") != u"38;5;5": sys.exit(7)
    if parsecolor("cyan") != u"38;5;6": sys.exit(8)

# Generated at 2022-06-13 16:02:20.493722
# Unit test for function colorize
def test_colorize():
    import unittest
    class TestStringMethods(unittest.TestCase):
        def test_color(self):
            pass
    unittest.main()


# Generated at 2022-06-13 16:02:29.548675
# Unit test for function colorize
def test_colorize():
    """Colorize Test"""

# Generated at 2022-06-13 16:02:41.344865
# Unit test for function parsecolor
def test_parsecolor():
    # Test color numbers
    assert u'38;5;196' == parsecolor(u'color196')
    assert u'38;5;197' == parsecolor(u'color197')
    assert u'38;5;198' == parsecolor(u'color198')
    # Test RGB
    assert u'38;5;196' == parsecolor(u'rgb222')
    assert u'38;5;197' == parsecolor(u'rgb223')
    assert u'38;5;198' == parsecolor(u'rgb224')
    # Test gray
    assert u'38;5;8' == parsecolor(u'gray0')
    assert u'38;5;7' == parsecolor(u'gray1')
    assert u'38;5;245' == par

# Generated at 2022-06-13 16:02:46.731682
# Unit test for function parsecolor

# Generated at 2022-06-13 16:02:56.128208
# Unit test for function hostcolor
def test_hostcolor():
    hstring = "testhost.example.com"
    # Default colors
    assert hostcolor(hstring, {'failures': 0, 'unreachable': 0, 'changed': 0}) == u"%-26s" % hstring
    assert hostcolor(hstring, {'failures': 0, 'unreachable': 0, 'changed': 1}) == u"%-26s" % stringc(hstring, C.COLOR_CHANGED)
    assert hostcolor(hstring, {'failures': 1, 'unreachable': 0, 'changed': 0}) == u"%-26s" % stringc(hstring, C.COLOR_ERROR)

# Generated at 2022-06-13 16:03:01.701254
# Unit test for function hostcolor
def test_hostcolor():
    stats = dict(failures=1, unreachable=0, changed=0)
    assert hostcolor('localhost', stats) == u'localhost                     '

    stats = dict(failures=0, unreachable=0, changed=0)
    assert hostcolor('localhost', stats) == u'localhost                     '

    stats = dict(failures=0, unreachable=0, changed=1)
    assert hostcolor('localhost', stats) == u'localhost                     '

# Generated at 2022-06-13 16:03:04.949339
# Unit test for function stringc
def test_stringc():
    assert stringc('foo', 'RED') == "\033[31mfoo\033[0m"
    assert stringc('foo', 'WHITE', wrap_nonvisible_chars=True) == "\001\033[37m\002foo\001\033[0m\002"


# --- end "pretty"

# Generated at 2022-06-13 16:03:15.540720
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor('blue') == u'34', 'Test #1 failed'
    assert parsecolor('1') == u'31', 'Test #2 failed'
    assert parsecolor('01') == u'38;5;1', 'Test #3 failed'
    assert parsecolor('255') == u'38;5;255', 'Test #4 failed'
    assert parsecolor('rgb222') == u'38;5;18', 'Test #5 failed'
    assert parsecolor('rgb122') == u'38;5;12', 'Test #6 failed'
    assert parsecolor('rgb022') == u'38;5;2', 'Test #7 failed'
    assert parsecolor('rgb211') == u'38;5;17', 'Test #8 failed'

# Generated at 2022-06-13 16:03:25.340868
# Unit test for function hostcolor
def test_hostcolor():
    if 'nocolor' in [C.ANSIBLE_NOCOLOR, 0]:
        return

    stats = dict(changed=1, failures=2, unreachable=0, ok=4)
    assert hostcolor('foobar', stats, False) == u"%-26s" % 'foobar'
    assert hostcolor('foobar', stats, True) == u"%-37s" % stringc('foobar', 'RED')
    stats['failures'] = 0
    stats['unreachable'] = 2
    assert hostcolor('foobar', stats, True) == u"%-37s" % stringc('foobar', 'RED')
    stats['failures'] = 0
    stats['unreachable'] = 0

# Generated at 2022-06-13 16:03:30.889495
# Unit test for function colorize
def test_colorize():
    pass  # TODO: implement this



# Generated at 2022-06-13 16:03:38.455091
# Unit test for function hostcolor
def test_hostcolor():
    from ansible.plugins import callback_loader
    CallbackModule = callback_loader._load_from_file("default", "default", None)
    callback_plugin = CallbackModule(display=None)
    assert callback_plugin.hostcolor("host", {'ok': 1, 'changed': 0, 'unreachable': 0, 'failures': 0}, True) == hostcolor("host", {'ok': 1, 'changed': 0, 'unreachable': 0, 'failures': 0}, True)



# Generated at 2022-06-13 16:03:46.028838
# Unit test for function stringc
def test_stringc():
    assert stringc('foo', 'green') == u'\033[32mfoo\033[0m'
    assert stringc('foo', 'dark green') == u'\033[32mfoo\033[0m'
    assert stringc('foo\nbar', 'yellow') == u'\033[33mfoo\nbar\033[0m'
    assert stringc('foo', 'black', wrap_nonvisible_chars=True) == u'\001\033[30m\002foo\001\033[0m\002'
    assert stringc('foo\nbar', 'yellow', wrap_nonvisible_chars=True) == u'\001\033[33m\002foo\nbar\001\033[0m\002'
    assert stringc('', 'red') == ''

# Generated at 2022-06-13 16:03:51.790769
# Unit test for function hostcolor
def test_hostcolor():
    host = '192.168.1.1'

    stats = {'ok': 0, 'changed': 0, 'unreachable': 0, 'failures': 0}
    color = hostcolor(host, stats, True)
    assert color == stringc(host, C.COLOR_OK)

    stats = {'ok': 0, 'changed': 1, 'unreachable': 0, 'failures': 0}
    color = hostcolor(host, stats, True)
    assert color == stringc(host, C.COLOR_CHANGED)

    stats = {'ok': 0, 'changed': 0, 'unreachable': 0, 'failures': 1}
    color = hostcolor(host, stats, True)
    assert color == stringc(host, C.COLOR_ERROR)

    color = hostcolor(host, stats, False)


# Generated at 2022-06-13 16:04:03.591466
# Unit test for function colorize
def test_colorize():
    # In some terminals, the color is a negative
    # number, so we need to capture that.
    color = parsecolor('blue')
    if color.startswith('-'):
        color = color[1:]
    assert colorize('ok', 0, 'green') == 'ok=0   '
    assert colorize('changed', 0, 'yellow') == 'changed=0   '
    assert colorize('unreachable', 0, 'red') == 'unreachable=0 '
    assert colorize('failed', 0, 'red') == 'failed=0    '
    assert colorize('ok', 1, 'green') == '\x1b[32mok=1   \x1b[0m'

# Generated at 2022-06-13 16:04:11.713661
# Unit test for function hostcolor
def test_hostcolor():
    def colorcheck(term, stats, expect):
        if ANSIBLE_COLOR:
            text = hostcolor(term, stats, True)
            if not text == expect:
                raise AssertionError("hostcolor(%s) produced '%s', not '%s' as expected." % (term, text, expect))
    # Set ANSIBLE_COLOR and verify that ANSIBLE_NOCOLOR overrides it.
    global ANSIBLE_COLOR
    ANSIBLE_COLOR = True
    colorcheck("green", dict(failures=0, unreachable=0, changed=0), u'\x1b[32m%-37s\x1b[0m' % u'green')

# Generated at 2022-06-13 16:04:23.401979
# Unit test for function hostcolor
def test_hostcolor():
    expected_result = u'\033[%sm%-37s\033[0m'
    result = hostcolor(u'testhost', {'failures': 1, 'unreachable': 1, 'changed': 1})
    color_code = parsecolor(C.COLOR_ERROR)
    assert expected_result % color_code == result
    # even if there are no failures we should get color output
    result = hostcolor(u'testhost', {'failures': 0, 'unreachable': 0, 'changed': 1})
    color_code = parsecolor(C.COLOR_CHANGED)
    assert expected_result % color_code == result
    # changed is 0 it should be colored
    result = hostcolor(u'testhost', {'failures': 0, 'unreachable': 0, 'changed': 0})
    color

# Generated at 2022-06-13 16:04:34.572122
# Unit test for function colorize

# Generated at 2022-06-13 16:04:43.228382
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('server1', dict(changed=0, unreachable=0, failures=0), color=True) == \
        u"\u001b[0;32mserver1                 \u001b[0m"
    assert hostcolor('server1', dict(changed=1, unreachable=0, failures=0), color=True) == \
        u"\u001b[0;33mserver1                 \u001b[0m"
    assert hostcolor('server1', dict(changed=0, unreachable=1, failures=0), color=True) == \
        u"\u001b[0;31mserver1                 \u001b[0m"

# Generated at 2022-06-13 16:04:54.767385
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor('black') == u'38;5;16'
    assert parsecolor('red') == u'31'
    assert parsecolor('blue') == u'34'
    assert parsecolor('green') == u'32'
    assert parsecolor('yellow') == u'33'
    assert parsecolor('magenta') == u'35'
    assert parsecolor('cyan') == u'36'
    assert parsecolor('white') == u'37'
    assert parsecolor('bright black') == u'38;5;8'
    assert parsecolor('bright red') == u'91'
    assert parsecolor('bright blue') == u'94'
    assert parsecolor('bright green') == u'92'
    assert parsecolor('bright yellow') == u'93'

# Generated at 2022-06-13 16:05:13.544001
# Unit test for function colorize

# Generated at 2022-06-13 16:05:21.060313
# Unit test for function hostcolor
def test_hostcolor():
    # hostcolor is expected to print the hostname in a color determined by parameters
    # 1. For stats with failures or unreachable, print in red
    # 2. For stats with changed, print in yellow
    # 3. For stats without failures, unreachable, and changed, print in green
    # 4. If ANSIBLE_COLOR is not set, print in black
    # 5. For long hostnames, print the first 26 characters of the hostname
    # 6. Print any other types differently
    stats_failures_changed = {'ok': 0, 'changed': 1, 'unreachable': 0, 'skipped': 0, 'failed': 0}
    stats_failures_unreachable = {'ok': 0, 'changed': 0, 'unreachable': 1, 'skipped': 0, 'failed': 0}
    stats_failures_skipped

# Generated at 2022-06-13 16:05:30.649398
# Unit test for function stringc
def test_stringc():
    assert stringc('foo', 'blue') == u'\033[34mfoo\033[0m'
    assert stringc('bar', 'color1') == u'\033[38;5;1mbar\033[0m'
    assert stringc('baz', 'rgb123') == u'\033[38;5;21mbaz\033[0m'
    assert stringc('qux', 'gray0') == u'\033[38;5;232mqux\033[0m'
    assert stringc('quux', 'white', True) == u'\001\033[38;5;15m\002quux\001\033[0m\002'
    assert stringc('corge', 'white', False) == u'\033[38;5;15mcorge\033[0m'

# Generated at 2022-06-13 16:05:38.209742
# Unit test for function stringc
def test_stringc():
    assert stringc("hello", "blue") == u"\033[34mhello\033[0m"
    assert stringc("hello", "red", wrap_nonvisible_chars=True) == u"\001\033[31m\002hello\001\033[0m\002"
    assert stringc("hello\nworld", "red", wrap_nonvisible_chars=True) == u"\001\033[31m\002hello\nworld\001\033[0m\002"


# End of pretty library
# ----


# Generated at 2022-06-13 16:05:46.014772
# Unit test for function hostcolor
def test_hostcolor():
    stats = dict(failures=0, unreachable=0, changed=0)
    assert hostcolor("localhost", stats) == "localhost               "
    stats['failures'] = 1
    assert hostcolor("localhost", stats) == "localhost\x1b[31m               \x1b[0m"
    stats['failures'] = 0
    stats['changed'] = 1
    assert hostcolor("localhost", stats) == "localhost\x1b[33m               \x1b[0m"
    stats['changed'] = 0
    stats['unreachable'] = 1
    assert hostcolor("localhost", stats) == "localhost\x1b[31m               \x1b[0m"
    stats['unreachable'] = 0
    stats['failures'] = 1

# Generated at 2022-06-13 16:05:50.251194
# Unit test for function stringc
def test_stringc():
    assert stringc('hello', 'green') == '\033[32mhello\033[0m'
    assert stringc('hello', 'red') == '\033[31mhello\033[0m'
    assert stringc('hello', 'blue') == '\033[34mhello\033[0m'
    assert stringc('hello', 'magenta') == '\033[35mhello\033[0m'



# Generated at 2022-06-13 16:06:01.577915
# Unit test for function hostcolor
def test_hostcolor():
    test_host = 'testhost'
    test_stats = { 'changed': 2, 'failures' : 0, 'ok' : 8, 'skipped' : 0, 'unreachable' : 0 }
    assert hostcolor(test_host, test_stats) == 'testhost                 \033[32;1m'
    test_stats = { 'changed': 2, 'failures' : 0, 'ok' : 8, 'skipped' : 1, 'unreachable' : 0 }
    assert hostcolor(test_host, test_stats) == 'testhost                 \033[32;1m'
    test_stats = { 'changed': 0, 'failures' : 0, 'ok' : 8, 'skipped' : 0, 'unreachable' : 0 }

# Generated at 2022-06-13 16:06:06.493448
# Unit test for function colorize
def test_colorize():
    print(colorize("test", 0, "green"))
    print(colorize("test", 1, "green"))
    print(colorize("test", -1, "green"))

# --- end "pretty"



# Generated at 2022-06-13 16:06:14.282048
# Unit test for function colorize
def test_colorize():
    from ansible.utils import colorize
    assert colorize('foo', 0, 'blue') == 'foo=0   '
    assert colorize('foo', 0, 'blue') == 'foo=0   '
    assert colorize('foo', 123, 'blue') == 'foo=123 '
    assert colorize('foo', 1234, 'blue') == 'foo=1234'
    assert colorize('foo', -1234, 'blue') == 'foo=-1234'
    assert colorize('foo', -12, 'blue') == 'foo=-12 '

# Generated at 2022-06-13 16:06:25.536965
# Unit test for function hostcolor
def test_hostcolor():
    stats = dict(
        ok=2,
        skipped=1,
        failed=1,
        unreachable=3,
        changed=4,
        failures=4,
    )

# Generated at 2022-06-13 16:06:51.982872
# Unit test for function stringc
def test_stringc():
    assert stringc("message", "green") == u"\033[32mmessage\033[0m"
    assert stringc("message", "color4") == u"\033[38;5;4mmessage\033[0m"
    assert stringc("message", "rgb222") == u"\033[38;5;16mmessage\033[0m"
    assert stringc("message", "rgb000") == u"\033[38;5;0mmessage\033[0m"
    assert stringc("message", "gray0") == u"\033[38;5;232mmessage\033[0m"
    assert stringc("message", "gray9") == u"\033[38;5;241mmessage\033[0m"


# Generated at 2022-06-13 16:07:01.084743
# Unit test for function stringc

# Generated at 2022-06-13 16:07:07.049755
# Unit test for function hostcolor
def test_hostcolor():
    host = 'testhost'

    stats = dict(failures=0, unreachable=0, changed=0)
    res = hostcolor(host, stats)
    if res != u"%-26s" % host:
        raise Exception("hostcolor failed when all stats were 0")
    stats = dict(failures=1, unreachable=0, changed=0)
    res = hostcolor(host, stats)
    if res != u"%-26s" % stringc(host, C.COLOR_ERROR):
        raise Exception("hostcolor failed when failures=1")
    stats = dict(failures=0, unreachable=1, changed=0)
    res = hostcolor(host, stats)

# Generated at 2022-06-13 16:07:15.746017
# Unit test for function stringc
def test_stringc():
    # Yes, this is an ugly test, but it keeps me from having to figure
    # out how to work both unittest and mock into one file
    # pylint: disable=missing-docstring
    class FakeStdout:

        @staticmethod
        def isatty():
            return True

    sys.stdout = FakeStdout()
    ANSIBLE_COLOR = True

# Generated at 2022-06-13 16:07:21.406643
# Unit test for function hostcolor
def test_hostcolor():
    from ansible.utils.color import hostcolor
    s = dict(ok=1, darkred='\033[31m', lightred='\033[91m', nocolor='\033[0m')
    assert hostcolor('foo', dict(failures=0, unreachable=1), True) == lightred + 'foo' + nocolor
    assert hostcolor('foo', dict(failures=1, unreachable=0), True) == lightred + 'foo' + nocolor
    assert hostcolor('foo', dict(failures=0, unreachable=0), True) == darkred + 'foo' + nocolor
    assert hostcolor('foo', dict(failures=0, unreachable=0), False) == 'foo'


# Generated at 2022-06-13 16:07:28.775114
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('localhost', {'dark': 0, 'skipped': 0, 'changed': 1, 'failures': 0, 'ok': 5, 'unreachable': 0}, True) == u'%-37s' % stringc('localhost', C.COLOR_CHANGED)
    assert hostcolor('localhost', {'dark': 0, 'skipped': 0, 'changed': 0, 'failures': 0, 'ok': 5, 'unreachable': 0}, True) == u'%-37s' % stringc('localhost', C.COLOR_OK)
    assert hostcolor('localhost', {'dark': 0, 'skipped': 0, 'changed': 0, 'failures': 1, 'ok': 5, 'unreachable': 0}, True) == u'%-37s' % stringc('localhost', C.COLOR_ERROR)

# Generated at 2022-06-13 16:07:29.583524
# Unit test for function colorize
def test_colorize():
    pass



# Generated at 2022-06-13 16:07:39.351442
# Unit test for function stringc
def test_stringc():
    assert stringc(u'hello', u'blue') == u'\033[34mhello\033[0m'
    assert stringc(u'hello', u'color3') == u'\033[38;5;11mhello\033[0m'
    assert stringc(u'hello', u'rgb25533') == u'\033[38;5;213mhello\033[0m'
    assert stringc(u'hello', u'gray3') == u'\033[38;5;235mhello\033[0m'
    assert stringc(u'hello\nworld', u'blue') == u'\033[34mhello\033[0m\n\033[34mworld\033[0m'

# Generated at 2022-06-13 16:07:45.310445
# Unit test for function stringc
def test_stringc():

    assert stringc('foo', 'red') == '\033[31mfoo\033[0m'
    assert stringc('bar', 'blue') == '\033[34mbar\033[0m'

    # We need to use a non default value for ANSIBLE_FORCE_COLOR
    # when testing with C.ANSIBLE_NOCOLOR
    C.ANSIBLE_FORCE_COLOR = False
    # Now if ANSIBLE_NOCOLOR is set to something else than "false"
    # the result should not be colorized
    C.ANSIBLE_NOCOLOR = 'true'
    assert stringc('foo', 'red') == 'foo'
    C.ANSIBLE_FORCE_COLOR = True
    assert stringc('foo', 'red') == '\033[31mfoo\033[0m'
   

# Generated at 2022-06-13 16:07:55.416103
# Unit test for function stringc
def test_stringc():
    """Test stringc function."""
    # Ensure default color is used for parameters which don't exists
    assert stringc("text", "notacolor") == "\033[39;49mtext\033[0m"
    # Test all 8-colors
    assert stringc("text", "black") == "\033[30;49mtext\033[0m"
    assert stringc("text", "red") == "\033[31;49mtext\033[0m"
    assert stringc("text", "green") == "\033[32;49mtext\033[0m"
    assert stringc("text", "yellow") == "\033[33;49mtext\033[0m"
    assert stringc("text", "blue") == "\033[34;49mtext\033[0m"

# Generated at 2022-06-13 16:08:33.874589
# Unit test for function hostcolor
def test_hostcolor():
    hostcolor("foobar", dict(failures=0, unreachable=0, changed=0), color=False)
    hostcolor("foobar", dict(failures=1, unreachable=0, changed=0), color=False)
    hostcolor("foobar", dict(failures=0, unreachable=1, changed=0), color=False)
    hostcolor("foobar", dict(failures=0, unreachable=0, changed=1), color=False)

# --- end "pretty"

# Generated at 2022-06-13 16:08:40.697522
# Unit test for function stringc
def test_stringc():
    test_color = sys.stdout.isatty()
    assert test_color == ANSIBLE_COLOR
    if test_color:
        assert stringc('hello', 'red') == u'\033[31mhello\033[0m'
        assert stringc('color1', 'color1') == u'\033[38;5;1mcolor1\033[0m'
        assert stringc('rgb251', 'rgb251') == u'\033[38;5;251mrgb251\033[0m'
        assert stringc('graya7', 'graya7') == u'\033[38;5;247mgraya7\033[0m'

# Generated at 2022-06-13 16:08:51.656509
# Unit test for function hostcolor

# Generated at 2022-06-13 16:09:01.761077
# Unit test for function stringc
def test_stringc():
    print("Testing stringc")

    class ANSI_Colors_Foreground:
        BLACK = '30'
        RED = '31'
        GREEN = '32'
        YELLOW = '33'
        BLUE = '34'
        MAGENTA = '35'
        CYAN = '36'
        WHITE = '37'
        RESET = '0'


# Generated at 2022-06-13 16:09:07.893446
# Unit test for function parsecolor
def test_parsecolor():
    # color
    assert parsecolor(u'color8') == u'38;5;8'
    assert parsecolor(u'color40') == u'38;5;40'
    # rgb
    assert parsecolor(u'rgb000') == u'38;5;16'
    assert parsecolor(u'rgb555') == u'38;5;231'
    assert parsecolor(u'rgb123') == u'38;5;50'
    # gray
    assert parsecolor(u'gray0') == u'38;5;232'
    assert parsecolor(u'gray23') == u'38;5;255'
    # invalid
    assert parsecolor(u'invalid') == u'0'


# Generated at 2022-06-13 16:09:17.178760
# Unit test for function stringc
def test_stringc():
    # Color
    print(u'\033[32;1mtext')
    print(u'\033[32;1mtext\033[0m')
    print(u'\033[32;1mtext\033[0m\033[0m')
    # No color
    print(stringc(u'foo', u'green'))
    # Color with newlines
    print(u'\033[32mtext\n\033[31mtext\033[0m')
    print(stringc(u'foo\nbar', u'red'))
    # Test colors
    for color in C.COLOR_CODES:
        print(u'%-7s: %s' % (color, stringc(u'foo', color)))
# --- end output.py



# Generated at 2022-06-13 16:09:23.772491
# Unit test for function stringc
def test_stringc():
    assert stringc(u'Hello world!', u'blue') == u'\x1b[34mHello world!\x1b[0m'
    assert stringc(u'Hello world!', u'31') == u'\x1b[31mHello world!\x1b[0m'
    assert stringc(u'Hello world!', u'color123') == u'\x1b[38;5;123mHello world!\x1b[0m'
    assert stringc(u'Hello world!', u'rgb255000') == u'\x1b[38;5;196mHello world!\x1b[0m'

# Generated at 2022-06-13 16:09:30.790497
# Unit test for function stringc
def test_stringc():
    s = stringc('this is a test', 'green')
    assert s == u"\033[32mthis is a test\033[0m"

    s = stringc('this is a test', 'rgb254')
    assert s == u"\033[38;5;154mthis is a test\033[0m"

    s = stringc('this is a test', 'nonexistentcolor')
    assert s == u"\033[39mthis is a test\033[0m"


if __name__ == '__main__':
    test_stringc()
    print("OK")