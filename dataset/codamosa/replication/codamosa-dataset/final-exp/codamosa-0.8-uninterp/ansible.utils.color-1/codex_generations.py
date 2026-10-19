

# Generated at 2022-06-13 15:59:38.452047
# Unit test for function parsecolor
def test_parsecolor():
    """
    Test SGR code mapping for parsecolor().

    The mapping between color specifier and SGR code is not one-to-one.
    Some have aliases. To test parsecolor(), we need to test the mapping
    for all color specifier, but not for all SGR code.
    """
    sgr_codes = set(C.COLOR_CODES.values())
    for color in C.COLOR_CODES:
        sgr_codes.remove(parsecolor(color))
    assert not sgr_codes

# Generated at 2022-06-13 15:59:42.244079
# Unit test for function stringc
def test_stringc():
    assert stringc("testtext", "red") == u"\u001b[31mtesttext\u001b[0m"


# Generated at 2022-06-13 15:59:47.317300
# Unit test for function colorize
def test_colorize():
    print(stringc("ok", "green"))
    print(stringc("changed", "yellow"))
    print(stringc("unreachable", "red"))
    print(stringc("failed", "red"))
    print(stringc("skipped", "cyan"))
    print(stringc("unreachable", "blue"))

# Generated at 2022-06-13 15:59:55.692970
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor('black') == u'38;5;16'
    assert parsecolor('darkgray') == u'38;5;250'
    assert parsecolor('red') == u'38;5;196'
    assert parsecolor('green') == u'38;5;46'
    assert parsecolor('yellow') == u'38;5;226'
    assert parsecolor('blue') == u'38;5;21'
    assert parsecolor('magenta') == u'38;5;201'
    assert parsecolor('cyan') == u'38;5;51'
    assert parsecolor('lightgray') == u'38;5;250'
    assert parsecolor('white') == u'38;5;231'


# Generated at 2022-06-13 16:00:04.116535
# Unit test for function stringc
def test_stringc():
    """Returns False if the function `stringc` doesn't work as expected, otherwise True."""
    # test all colors
    colors = ['blue', 'cyan', 'green', 'magenta', 'red', 'white', 'yellow',
              'dark gray', 'dark red', 'dark green', 'dark yellow',
              'dark blue', 'dark magenta', 'dark cyan', 'light gray']

    for color in colors:
        # test if color is printed for every color name
        if not stringc('test', color):
            return False

    # test if colorless string is returned if colors are disabled
    if not (stringc('test', colors[0], False) == 'test'):
        return False

    # test if colorless string is returned for unsupported colors
    if not (stringc('test', 'foo') == 'test'):
        return False

# Generated at 2022-06-13 16:00:13.595381
# Unit test for function parsecolor
def test_parsecolor():
    def check(color, code):
        assert parsecolor(color) == code

    check('blue', '38;5;4')
    check('dark gray', '38;5;8')
    check('green', '38;5;2')
    check('light blue', '38;5;12')
    check('light cyan', '38;5;14')
    check('light gray', '38;5;7')
    check('light green', '38;5;10')
    check('light magenta', '38;5;13')
    check('light red', '38;5;9')
    check('magenta', '38;5;5')
    check('red', '38;5;1')
    check('white', '38;5;15')
    check('yellow', '38;5;3')
   

# Generated at 2022-06-13 16:00:21.187599
# Unit test for function stringc
def test_stringc():
    """Test if a test string is colorized."""
    ansible_color = ANSIBLE_COLOR
    global ANSIBLE_COLOR
    ANSIBLE_COLOR = True
    import os
    import sys
    import unittest

    class TestStringc(unittest.TestCase):
        """
        Test if a test string is colorized.
        """
        def setUp(self):
            """
            Create a test string.
            """
            self.s = "test"
            self.colors = u"black, darkgray, red, lightred, green, lightgreen, brown, yellow, blue, lightblue, purple, pink, cyan, lightcyan"
            self.colors += u", lightgray, white"

# Generated at 2022-06-13 16:00:31.193443
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor(u'red') == u'31'
    assert parsecolor(u'green') == u'32'
    assert parsecolor(u'yellow') == u'33'
    assert parsecolor(u'blue') == u'34'
    assert parsecolor(u'magenta') == u'35'
    assert parsecolor(u'cyan') == u'36'
    assert parsecolor(u'white') == u'37'
    assert parsecolor(u'black') == u'30'
    assert parsecolor(u'rgb123') == u'38;5;33'
    assert parsecolor(u'rgb321') == u'38;5;137'
    assert parsecolor(u'rgb213') == u'38;5;70'
    assert par

# Generated at 2022-06-13 16:00:42.233332
# Unit test for function hostcolor
def test_hostcolor():
    if not sys.stdout.isatty():
        return
    print(hostcolor(u"127.0.0.1", {'failures': 0, 'unreachable': 0, 'changed': 0}, True))
    print(hostcolor(u"127.0.0.1", {'failures': 0, 'unreachable': 0, 'changed': 1}, True))
    print(hostcolor(u"127.0.0.1", {'failures': 1, 'unreachable': 0, 'changed': 0}, True))
    print(hostcolor(u"127.0.0.1", {'failures': 0, 'unreachable': 1, 'changed': 0}, True))

# Generated at 2022-06-13 16:00:45.344984
# Unit test for function colorize
def test_colorize():
    assert "foo=1" == (colorize("foo", 1, None))
    assert "foo=0" == (colorize("foo", 0, None))
    assert "foo=-1" == (colorize("foo", -1, None))


# --- end "pretty"
#

# Generated at 2022-06-13 16:01:01.625064
# Unit test for function stringc
def test_stringc():
    """ Tests for function stringc() """
    assert stringc('foo', 'green') == u'\033[32mfoo\033[0m'
    assert stringc('foo', 'red') == u'\033[31mfoo\033[0m'
    assert stringc('foo', 'color254') == u'\033[38;5;254mfoo\033[0m'
    assert stringc('foo', 'rgb123') == u'\033[38;5;111mfoo\033[0m'
    assert stringc('foo', 'gray99') == u'\033[38;5;245mfoo\033[0m'

# Generated at 2022-06-13 16:01:06.462577
# Unit test for function stringc
def test_stringc():
    print(stringc("text", "green", wrap_nonvisible_chars=True))
    print(stringc("text", "blue"))
    print(stringc("text", "red"))
    print(stringc("text", "black"))
    print(stringc("text", "white"))
    print(stringc("text", "green", wrap_nonvisible_chars=True))


#
# --- end of "pretty" code
#####################################################################



# Generated at 2022-06-13 16:01:16.381449
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor('black') == u'38;5;0'
    assert parsecolor('red') == u'38;5;1'
    assert parsecolor('yellow') == u'38;5;3'
    assert parsecolor('blue') == u'38;5;4'
    assert parsecolor('white') == u'38;5;7'
    assert parsecolor('default') == u'39'
    assert parsecolor('green') == u'38;5;2'
    assert parsecolor('cyan') == u'38;5;6'
    assert parsecolor('magenta') == u'38;5;5'
    assert parsecolor('1') == u'38;5;1'
    assert parsecolor('9') == u'38;5;9'
    assert par

# Generated at 2022-06-13 16:01:26.112964
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor("localhost", {'failures': 1,
                      'unreachable': 0, 'changed': 0}) == u"%-37s" % stringc("localhost", C.COLOR_ERROR)
    assert hostcolor("localhost", {'failures': 0,
                      'unreachable': 1, 'changed': 0}) == u"%-37s" % stringc("localhost", C.COLOR_ERROR)
    assert hostcolor("localhost", {'failures': 0,
                      'unreachable': 0, 'changed': 1}) == u"%-37s" % stringc("localhost", C.COLOR_CHANGED)
    assert hostcolor("localhost", {'failures': 0,
                      'unreachable': 0, 'changed': 0}) == u"%-37s" % stringc("localhost", C.COLOR_OK)
    # hostcolor using

# Generated at 2022-06-13 16:01:31.579908
# Unit test for function colorize
def test_colorize():
    for i in (0, 1, 2, 3, 4, 10, 11, 25, 26, 27, 334, 1026):
        s = colorize(u"VAR", i, color=u'blue')
        print(s)
    print(u"%s=%-4s" % (u"HOST", str(0)))
    print(stringc(u"foo\nbar", color=u'green', wrap_nonvisible_chars=True))



# Generated at 2022-06-13 16:01:40.015558
# Unit test for function hostcolor
def test_hostcolor():
    if ANSIBLE_COLOR:
        assert hostcolor('foo', {'failures': 0, 'unreachable': 0, 'changed': 0}, True) == stringc('%-26s' % 'foo', C.COLOR_OK)
        assert hostcolor('foo', {'failures': 0, 'unreachable': 0, 'changed': 0}, False) == '%-26s' % 'foo'
        assert hostcolor('foo', {'failures': 0, 'unreachable': 1, 'changed': 0}, True) == stringc('%-26s' % 'foo', C.COLOR_ERROR)
        assert hostcolor('foo', {'failures': 0, 'unreachable': 1, 'changed': 0}, False) == '%-26s' % 'foo'

# Generated at 2022-06-13 16:01:49.288221
# Unit test for function hostcolor
def test_hostcolor():
    c_ok    = "\033[32m"
    c_failed  = "\033[31m"
    c_skipped = "\033[33m"
    c_unreachable = "\033[35m"
    c_changed = "\033[34m"

    class Options(object):
        def __init__(self, color=False, force_color=False, nocolor=False):
            self.color = color
            self.force_color = force_color
            self.nocolor = nocolor

    # Test cases
    C.ANSIBLE_FORCE_COLOR = False

# Generated at 2022-06-13 16:01:54.137630
# Unit test for function stringc
def test_stringc():
    print(__file__, end=':')
    for color in C.COLOR_CODES.keys():
        print(stringc('test', color), end=',')
    print('done')

if __name__ == '__main__':
    test_stringc()
# --- end "pretty"



# Generated at 2022-06-13 16:02:03.029145
# Unit test for function hostcolor
def test_hostcolor():
    good_host = "192.168.1.1"
    changed_host = "192.168.1.2"
    unreachable_host = "192.168.1.3"
    failed_host = "192.168.1.4"

    good_host_stats = {'ok': 10, 'changed': 0, 'unreachable': 0, 'failures': 0}
    changed_host_stats = {'ok': 20, 'changed': 5, 'unreachable': 0, 'failures': 0}
    unreachable_host_stats = {'ok': 0, 'changed': 0, 'unreachable': 1, 'failures': 0}
    failed_host_stats = {'ok': 0, 'changed': 0, 'unreachable': 0, 'failures': 1}

    # Change global ANSIBLE_COLOR

# Generated at 2022-06-13 16:02:10.112538
# Unit test for function hostcolor
def test_hostcolor():
    stats = {
        'changed': 0,
        'failures': 0,
        'ok': 1,
        'skipped': 0,
        'unreachable': 0
    }
    assert hostcolor('host', stats) == u'host'

    stats = {
        'changed': 1,
        'failures': 0,
        'ok': 0,
        'skipped': 0,
        'unreachable': 0
    }
    assert hostcolor('host', stats) == u'host'

    stats = {
        'changed': 0,
        'failures': 1,
        'ok': 0,
        'skipped': 0,
        'unreachable': 0
    }
    assert hostcolor('host', stats) == u'host'


# Generated at 2022-06-13 16:02:21.544035
# Unit test for function hostcolor
def test_hostcolor():
    h = 'hostname'
    _stats = {'failures': 0, 'unreachable': 0, 'changed': 0}
    print(hostcolor(h, _stats))


# --- end "pretty"



# Generated at 2022-06-13 16:02:26.031808
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor("localhost", dict(changed=1)) == u"localhost                "
    assert hostcolor("localhost", dict(failed=1)) == u"localhost                "
    assert hostcolor("localhost", dict(ok=1)) == u"localhost                "

# --- end "pretty"

# --- begin ansible style



# Generated at 2022-06-13 16:02:30.638955
# Unit test for function hostcolor
def test_hostcolor():
    # No color
    assert hostcolor('dummy', dict(ok=1)) == 'dummy                  '

    # Dictionary or color in recurse directory
    stats = dict(ok=1, changed=2, unreachable=3, failures=4)
    assert hostcolor('dummy', stats, color=False) == 'dummy                  '
    assert hostcolor('dummy', stats, color=True) == u'\u001b[31mdummy\u001b[0m                  '

    # color=None
    assert hostcolor('dummy', stats, color=None) == u'\u001b[31mdummy\u001b[0m                  '

# --- end "pretty"



# Generated at 2022-06-13 16:02:41.750501
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor('cyan') == u'38;5;6'
    assert parsecolor('Color3') == u'38;5;3'
    assert parsecolor('Blue') == u'38;5;4'
    # 8-bit color
    assert parsecolor('color1') == u'38;5;1'
    # 24-bit color
    assert parsecolor('rgb000') == u'38;5;16'
    assert parsecolor('rgb001') == u'38;5;17'
    assert parsecolor('rgb010') == u'38;5;22'
    assert parsecolor('rgb123') == u'38;5;57'
    # 256-color grayscale (colors 233 to 254 inclusive)

# Generated at 2022-06-13 16:02:49.719276
# Unit test for function stringc
def test_stringc():
    # Prints colors to the terminal
    print(stringc("stringc", "blue"))
    print(stringc("stringc", "blue", wrap_nonvisible_chars=True))
    print(stringc("stringc", "green"))
    print(stringc("stringc", "green", wrap_nonvisible_chars=True))
    print(stringc("stringc", "red"))
    print(stringc("stringc", "red", wrap_nonvisible_chars=True))
    print(stringc("stringc", "yellow"))
    print(stringc("stringc", "yellow", wrap_nonvisible_chars=True))
    print(stringc("stringc", "magenta"))
    print(stringc("stringc", "magenta", wrap_nonvisible_chars=True))

# Generated at 2022-06-13 16:02:52.418437
# Unit test for function stringc
def test_stringc():
    assert stringc('foo bar', C.COLOR_CHANGED) == '\033[38;5;214mfoo bar\033[0m'

# Generated at 2022-06-13 16:02:54.966273
# Unit test for function colorize
def test_colorize():
    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

# --- end "pretty"

# ===========================================
# Module execution.
#



# Generated at 2022-06-13 16:03:05.152662
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor('blue') == u'38;5;4'
    assert parsecolor('color8') == u'38;5;8'
    assert parsecolor('rgb123') == u'38;5;18'
    assert parsecolor('gray1') == u'38;5;233'
    assert parsecolor('green') == u'38;5;2'
    assert parsecolor('red') == u'38;5;1'


# end "pretty"

# These have to be global in order to be used by ansible.utils.module_docs
# without further mucking around with the code

# Generated at 2022-06-13 16:03:15.718752
# Unit test for function hostcolor
def test_hostcolor():
    # pylint: disable=unused-variable
    # pylint: disable=redefined-outer-name
    if ANSIBLE_COLOR:
        stats = {'changed': 0, 'failures': 0, 'ok': 0, 'skipped': 0, 'unreachable': 0}
        host = 'host'
        assert hostcolor(host, stats) == u"%-37s" % stringc(host, C.COLOR_OK)
        stats['changed'] = 1
        assert hostcolor(host, stats) == u"%-37s" % stringc(host, C.COLOR_CHANGED)
        stats['changed'] = 0
        stats['failures'] = 1
        assert hostcolor(host, stats) == u"%-37s" % stringc(host, C.COLOR_ERROR)

test_hostcolor()


# Generated at 2022-06-13 16:03:24.192836
# Unit test for function colorize
def test_colorize():
    # Yes, these tests are brittle but they're simple and they do the job
    assert colorize("foo", 4, "blue") == u'foo=4   '
    assert stringc("foo", "blue") == u'\x1b[94mfoo\x1b[0m'
    assert colorize("foo", 0, "blue") == u'foo=0   '
    assert colorize("foo", None, "blue") == u'foo=None'


# --- end pretty
#
# --- begin textwrap
#
# textwrap.py - A library that provides some text wrapping and filling
# functions that are not available in python's standard library.
#
# Copyright (C) 2004 Manish Singh <yosh@gimp.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the

# Generated at 2022-06-13 16:03:42.116714
# Unit test for function stringc
def test_stringc():
    assert stringc("text", "green") == "\033[32mtext\033[0m"
    assert stringc("text", "color8") == "\033[38;5;8mtext\033[0m"
    assert stringc("text", "rgb123") == "\033[38;5;63mtext\033[0m"
    assert stringc("text", "gray12") == "\033[38;5;244mtext\033[0m"
    assert stringc("text", "green", wrap_nonvisible_chars=True) == '\001\033[32m\002text\001\033[0m\002'  # noqa: E501

# --- end "pretty"

# Generated at 2022-06-13 16:03:50.821409
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('localhost', dict(failures=1, unreachable=0, changed=0)) == u'localhost               '
    assert hostcolor('localhost', dict(failures=0, unreachable=1, changed=0)) == u'localhost               '
    assert hostcolor('localhost', dict(failures=0, unreachable=0, changed=1)) == u'localhost               '
    assert hostcolor('localhost', dict(failures=0, unreachable=0, changed=0)) == u'localhost               '

# --- end of "pretty" ---

# =============================================
# ANSIBALLZ SPECIFIC CODE


# FIXME: other places in the code use exceptions for flow control, this
# should do the same

# Generated at 2022-06-13 16:04:02.545039
# Unit test for function stringc
def test_stringc():
    s = b(u"this is my l\u0161ng string")
    assert s == u"this is my l\u0161ng string"
    assert stringc(s, u'ok_green') == u'\033[92mthis is my l\u0161ng string\033[0m'


# --- end pretty
#
# Credit: http://code.activestate.com/recipes/577058/
# Created by Trent Mick.
#
# Run me with:
#   python -m ansible.utils.color ansible-playbook
# to see the results of the ANSIBLE_* env vars compared to the option parser
# defaults.
try:
    from optparse import OptionParser
except:
    from ansible.compat.optparse import OptionParser

atexit_was_registered = False




# Generated at 2022-06-13 16:04:09.947280
# Unit test for function colorize
def test_colorize():
    T = stringc(u'this is red', u'red') + u':'
    assert(colorize(u'foo', 0, u'red') == u"foo=0   ")
    assert(colorize(u'foo', 123, u'red') == T + u'   foo=123')
    assert(colorize(u'foo', 1234, u'red') == T + u'  foo=1234')
    assert(colorize(u'foo', 12345, u'red') == T + u' foo=12345')
    assert(colorize(u'foo', 123456, u'red') == T + u'foo=123456')


# Generated at 2022-06-13 16:04:21.183247
# Unit test for function hostcolor
def test_hostcolor():
    stats = dict(changed=0, failures=0, unreachable=0)
    assert hostcolor(u"host1", stats, True) == u"host1                 "
    stats['failures'] = 1
    assert hostcolor(u"host1", stats, True) == u"host1                 "
    stats['failures'] = 0
    stats['unreachable'] = 1
    assert hostcolor(u"host1", stats, True) == u"host1                 "
    stats['changed'] = 1
    stats['unreachable'] = 0
    assert hostcolor(u"host1", stats, True) == u"host1                 "

# --- end of pretty

# ---- begin error colors


# Generated at 2022-06-13 16:04:25.514825
# Unit test for function colorize
def test_colorize():
    string = colorize(u" ", 3, u"red")
    assert string == u"=3   "
    string = colorize(u" ", 0, u"green")
    assert string == u"=0   "
    string = colorize(u" ", 3, None)
    assert string == u"=3   "

# Generated at 2022-06-13 16:04:32.235062
# Unit test for function stringc
def test_stringc():
    """Unit test for function stringc."""
    assert stringc('hello world', 'blue') == '\033[34mhello world\033[0m'
    assert stringc('hello world', 'rgb255255255') == '\033[97mhello world\033[0m'
    assert stringc('hello world', 'color1') == '\033[38;5;1mhello world\033[0m'



# Generated at 2022-06-13 16:04:41.620079
# Unit test for function stringc
def test_stringc():
    if ANSIBLE_COLOR and sys.stdout.isatty():
        b = "bold"
        u = "underline"
        bl = "black"
        r = "red"
        g = "green"
        y = "yellow"
        bu = "blue"
        m = "magenta"
        c = "cyan"
        w = "white"
        for i in range(16):
            print(parsecolor("color%s" % i))
        for i in range(6):
            for j in range(6):
                for k in range(6):
                    print(parsecolor("rgb%s%s%s" % (i, j, k)))
        for i in range(24):
            print(parsecolor("gray%s" % i))

# Generated at 2022-06-13 16:04:45.896940
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor(u'localhost', dict(failures=1, unreachable=0, changed=0),
                     color=True) == '%-37s' % stringc(u'localhost', C.COLOR_ERROR)
    assert hostcolor(u'localhost', dict(failures=0, unreachable=1, changed=0),
                     color=True) == '%-37s' % stringc(u'localhost', C.COLOR_ERROR)
    assert hostcolor(u'localhost', dict(failures=0, unreachable=0, changed=1),
                     color=True) == '%-37s' % stringc(u'localhost', C.COLOR_CHANGED)

# Generated at 2022-06-13 16:04:56.483334
# Unit test for function stringc
def test_stringc():
    """
    Enable by setting the environment variable: ANSIBLE_KEEP_REMOTE_FILES=1
    """
    if not ANSIBLE_COLOR:
        raise AssertionError('ANSIBLE_COLOR must be True')

    colors = C.COLOR_CODES.keys()
    colors.remove('NORMAL')
    colors.remove('RESET')

    text = 'This is a message'

    for color in colors:
        print('Color: %s, code: %s' % (color, C.COLOR_CODES[color]))
        print(stringc(text, color))
        print(stringc(text, 'NORMAL'))

    print('Color: rgb31, code: %s' % (parsecolor('rgb31')))
    print(stringc(text, 'rgb31'))
   

# Generated at 2022-06-13 16:05:20.636319
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor("host.domain.tld", dict(changed=0, failures=0, unreachable=0, ok=1)) == u"host.domain.tld            \033[0;32m"
    assert hostcolor("host.domain.tld", dict(changed=1, failures=0, unreachable=0, ok=0)) == u"host.domain.tld            \033[0;33m"
    assert hostcolor("host.domain.tld", dict(changed=0, failures=1, unreachable=0, ok=0)) == u"host.domain.tld            \033[0;31m"
    assert hostcolor("host.domain.tld", dict(changed=0, failures=0, unreachable=1, ok=0)) == u"host.domain.tld            \033[0;31m"

# Generated at 2022-06-13 16:05:30.474765
# Unit test for function hostcolor
def test_hostcolor():
    stats = dict(
        ok=2,
        failures=0,
        skipped=0,
        unreachable=0,
        changed=0,
        processed=1
    )

    # Test if color is enabled, function should return a unicode string
    try:
        colorized = hostcolor(u'example.com', stats, color=True)
        assert isinstance(colorized, unicode), "hostcolor() returned non-unicode string"
    except NameError:
        colorized = hostcolor('example.com', stats, color=True)
        assert isinstance(colorized, str), "hostcolor() returned non-string"

    # Test if color is disabled, function should return a unicode string

# Generated at 2022-06-13 16:05:40.817080
# Unit test for function hostcolor
def test_hostcolor():
    stats = dict(failures=0, unreachable=0, changed=0)
    assert hostcolor(u"localhost", stats, False) == u"%-26s" % "localhost"
    assert hostcolor(u"localhost", stats, True) == u"%-37s" % u"\u001b[0;32mlocalhost\u001b[0m"
    stats['failures'] = 1
    assert hostcolor(u"localhost", stats, True) == u"%-37s" % u"\u001b[0;31mlocalhost\u001b[0m"
    stats['failures'] = 0
    stats['changed'] = 2
    assert hostcolor(u"localhost", stats, True) == u"%-37s" % u"\u001b[0;33mlocalhost\u001b[0m"

# Generated at 2022-06-13 16:05:49.776893
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('localhost', dict(changed=1, unreachable=0, failures=0), True) == u'%-37s' % stringc('localhost', C.COLOR_CHANGED)
    assert hostcolor('localhost', dict(changed=0, unreachable=0, failures=0), True) == u'%-37s' % stringc('localhost', C.COLOR_OK)
    assert hostcolor('localhost', dict(changed=0, unreachable=1, failures=0), True) == u'%-37s' % stringc('localhost', C.COLOR_ERROR)
    assert hostcolor('localhost', dict(changed=0, unreachable=0, failures=1), True) == u'%-37s' % stringc('localhost', C.COLOR_ERROR)

# Generated at 2022-06-13 16:05:57.354722
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor("localhost", dict(failures=0, unreachable=0, changed=0)) == "localhost               "
    assert hostcolor("localhost", dict(failures=1, unreachable=0, changed=0)) == "localhost               "
    assert hostcolor("localhost", dict(failures=0, unreachable=1, changed=0)) == "localhost               "
    assert hostcolor("localhost", dict(failures=0, unreachable=0, changed=1)) == "localhost               "
    assert hostcolor("localhost", dict(failures=1, unreachable=1, changed=1)) == "localhost               "
    assert hostcolor("localhost", dict(failures=0, unreachable=1, changed=1)) == "localhost               "

# --- end "pretty"



# Generated at 2022-06-13 16:06:06.074596
# Unit test for function hostcolor
def test_hostcolor():
    USER_COLOR = 'yes'
    USER_NOCOLOR = 'no'
    USER_NOCOLOR_TRUE = 'True'
    USER_NOCOLOR_FALSE = 'False'
    USER_NOCOLOR_0 = '0'
    USER_NOCOLOR_1 = '1'
    USER_NOCOLOR_EMPTY_STRING = ''

    # Set color to True
    class FakeContext():
        def __init__(self, color=''):
            self.color = color
            self.prompt_context = self

    class FakeRunner():
        def __init__(self, color):
            self._elements = []
            self.stats = {}
            self.host_name = 'testhost'
            self.context = FakeContext(color)

# Generated at 2022-06-13 16:06:11.506674
# Unit test for function stringc
def test_stringc():
    """Unit test for stringc"""
    color = 'blue'
    text = 'hello world'
    assert isinstance(
        stringc(text, color),
        unicode
    ), "stringc should return unicode string"

    text, color = u'hello world', u'blue'
    assert isinstance(
        stringc(text, color),
        unicode
    ), "stringc should return unicode string"

    text, color = u'hello world', u'color9'
    text_colorized = u'\033[38;5;9mhello world\033[0m'
    assert stringc(text, color) == text_colorized, "stringc(%s, %s) != %s" % (
        text, color, text_colorized)



# Generated at 2022-06-13 16:06:16.609249
# Unit test for function hostcolor
def test_hostcolor():
    "hostcolor()"
    host = 'host'
    stats = {
        'pending': 0,
        'skipped': 0,
        'success': 3,
        'failures': 0,
        'changed': 2,
        'unreachable': 0,
        'dark': 0
    }
    ok = hostcolor(host, stats, False)
    assert ok == "%s=" % host, "hostcolor() failed"
    test_color = hostcolor(host, stats, True)
    assert test_color == u"%-37s" % stringc(host, C.COLOR_OK)
    host = 'host'

# Generated at 2022-06-13 16:06:25.777034
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('host', {'failures':0,'unreachable':0,'changed':0}) == u"host                          "
    assert hostcolor('host', {'failures':1,'unreachable':0,'changed':0}) == u"host                          "
    assert hostcolor('host', {'failures':1,'unreachable':0,'changed':2}) == u"host               "
    assert hostcolor('host', {'failures':1,'unreachable':2,'changed':2}) == u"host                          "
    assert hostcolor('host', {'failures':1,'unreachable':2,'changed':0}) == u"host                          "

# end of "pretty"
# ---


# Generated at 2022-06-13 16:06:28.400899
# Unit test for function stringc
def test_stringc():
    assert stringc('foo', 'black') == '\033[30mfoo\033[0m'



# Generated at 2022-06-13 16:07:04.099171
# Unit test for function hostcolor
def test_hostcolor():
    def my_stringc(text, color):
        return color
    assert hostcolor(u"localhost", {"failures":0, "unreachable":0, "changed":0}, True) == \
        "%-37s" % C.COLOR_OK
    assert hostcolor(u"localhost", {"failures":1, "unreachable":0, "changed":0}, True) == \
        "%-37s" % C.COLOR_ERROR
    assert hostcolor(u"localhost", {"failures":0, "unreachable":1, "changed":0}, True) == \
        "%-37s" % C.COLOR_ERROR
    assert hostcolor(u"localhost", {"failures":0, "unreachable":0, "changed":1}, True) == \
        "%-37s" % C.COLOR_CHANGED
   

# Generated at 2022-06-13 16:07:13.563988
# Unit test for function hostcolor
def test_hostcolor():
    stats_ok = dict(
            changed=0,
            failures=0,
            skipped=0,
            unreachable=0,
            ok=10,
    )
    stats_changed = dict(
            changed=10,
            failures=0,
            skipped=0,
            unreachable=0,
            ok=0,
    )
    stats_fail = dict(
            changed=0,
            failures=10,
            skipped=0,
            unreachable=0,
            ok=0,
    )
    stats_unreach = dict(
            changed=0,
            failures=0,
            skipped=0,
            unreachable=10,
            ok=0,
    )
    color = hostcolor("testhost", stats_ok)

# Generated at 2022-06-13 16:07:23.547452
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor(u"foobar", {'failures': 1, 'changed': 2, 'ok': 3, 'skipped': 4, 'unreachable': 5}) == u'foobar                           '
    assert hostcolor(u"foobar", {'failures': 1, 'changed': 2, 'ok': 3, 'skipped': 4, 'unreachable': 0}) == u'\n'.join([u'\x1b[31mfoobar\x1b[0m', u''])
    assert hostcolor(u"foobar", {'failures': 0, 'changed': 1, 'ok': 3, 'skipped': 4, 'unreachable': 0}) == u'\n'.join([u'\x1b[34mfoobar\x1b[0m', u''])

# Generated at 2022-06-13 16:07:26.813070
# Unit test for function stringc
def test_stringc():
    print(stringc("foo", "green"))
    print(stringc("bar", "red"))
    print(stringc("baz", "blue"))
    print(stringc("blah", "yellow"))
    print(stringc("wibble", "magenta"))
    print(stringc("wobble", "cyan"))
# --- end "pretty"



# Generated at 2022-06-13 16:07:37.310111
# Unit test for function stringc
def test_stringc():
    """This is only for stdout. Not for actual test."""
    for color in ('blue', 'lightblue', 'lightgreen'):
        print(stringc("blue", color))

    for color in ('red', 'lightred', 'green', 'lightgreen'):
        print(stringc("red", color))

    for color in ('darkgray', 'lightgray', 'white'):
        print(stringc("white", color))

    for color in ('darkgray', 'lightgray', 'white'):
        print(stringc("dark gray", color))

    for color in ('darkgray', 'lightgray', 'white'):
        print(stringc("light gray", color))

    for color in ('black', 'darkgray', 'lightgray'):
        print(stringc("black", color))


# Generated at 2022-06-13 16:07:44.373603
# Unit test for function stringc
def test_stringc():
    ''' assert that a stringc can be properly printed '''
    test1 = 'Stringc: Testing.'
    assert stringc(test1, 'red') == u'\x1b[31m' + test1 + u'\x1b[0m'

# --- end "pretty"

# This dictionary contains colors that we use for specific types of
# events.  It allows the user to override the colors if they so choose.

# Generated at 2022-06-13 16:07:54.996738
# Unit test for function stringc
def test_stringc():
    try:
        from nose.tools import eq_
    except:
        def eq_(a, b):
            assert a == b
    assert u"\x1b[1mbold\x1b[0m" == stringc(u"bold", "bold")
    assert u"\x1b[31mred\x1b[0m" == stringc(u"red", "red")
    assert u"\x1b[41m\x1b[37mbgred-white\x1b[0m" == stringc(u"bgred-white", "bgred", "white")
    assert u"\x1b[31m\x1b[41mbgred-white\x1b[0m" == stringc(u"bgred-white", ("red", "bgred"))

# Generated at 2022-06-13 16:08:03.822632
# Unit test for function hostcolor
def test_hostcolor():
    from ansible.callbacks import AggregateStats
    for c in (False, True):
        yield _run_hostcolor_test, AggregateStats(), c
        yield _run_hostcolor_test, AggregateStats(failures=1), c
        yield _run_hostcolor_test, AggregateStats(changed=1), c
        yield _run_hostcolor_test, AggregateStats(ok=1), c
        yield _run_hostcolor_test, AggregateStats(dark=1), c
        yield _run_hostcolor_test, AggregateStats(failures=2, ok=2, changed=2), c



# Generated at 2022-06-13 16:08:13.545547
# Unit test for function stringc
def test_stringc():
    """ Tests for the stringc function """
    assert stringc("This is a test", "blue") == "\033[34mThis is a test\033[0m"
    assert stringc("This is a test", "red") == "\033[31mThis is a test\033[0m"
    assert stringc("This is a test", "green") == "\033[32mThis is a test\033[0m"
    assert stringc("This is a test", "yellow") == "\033[33mThis is a test\033[0m"
    assert stringc("This is a test", "magenta") == "\033[35mThis is a test\033[0m"
    assert stringc("This is a test", "cyan") == "\033[36mThis is a test\033[0m"

# Generated at 2022-06-13 16:08:24.193821
# Unit test for function hostcolor
def test_hostcolor():
    result = hostcolor('foohost', {'changed': 0, 'failures': 0, 'ok': 2, 'skipped': 0, 'unreachable': 0})
    assert result == u"foohost                 "
    result = hostcolor('foohost', {'changed': 0, 'failures': 1, 'ok': 1, 'skipped': 0, 'unreachable': 0})
    assert result == u"\n".join(["\n".join([u"\001\033[0;31m\002", u"\001\033[0m\002"]), u"foohost\n                "])
    result = hostcolor('foohost', {'changed': 1, 'failures': 0, 'ok': 1, 'skipped': 0, 'unreachable': 0})

# Generated at 2022-06-13 16:09:03.216751
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('localhost', dict(failures=0, unreachable=0, changed=0), color=True) == stringc('localhost', C.COLOR_OK) + ' '
    assert hostcolor('localhost', dict(failures=1, unreachable=0, changed=0), color=True) == stringc('localhost', C.COLOR_ERROR) + ' '
    assert hostcolor('localhost', dict(failures=0, unreachable=1, changed=0), color=True) == stringc('localhost', C.COLOR_ERROR) + ' '
    assert hostcolor('localhost', dict(failures=0, unreachable=0, changed=1), color=True) == stringc('localhost', C.COLOR_CHANGED) + ' '



# Generated at 2022-06-13 16:09:13.973315
# Unit test for function colorize
def test_colorize():
    """ Unit test for function colorize """
    tests = ((u'ok', 0, u'green'),
             (u'changed', 1234, u'yellow'),
             (u'unreachable', 0, u'red'),
             (u'failed', 0, u'red'),
             (u'mixed', 0, None),
             (u'ok', 0, None),
             (u'changed', 1234, None),
             (u'unreachable', 0, None),
             (u'failed', 0, None),
             (u'mixed', 1234, None),
             )
    # This forces ANSIBLE_COLOR to be True
    global ANSIBLE_COLOR
    ANSIBLE_COLOR = True
    for (lead, num, color) in tests:
        yield colorize, lead, num, color



# Generated at 2022-06-13 16:09:16.300435
# Unit test for function stringc
def test_stringc():
    assert stringc(u"hello", u"blue") == u"\033[34mhello\033[0m"



# Generated at 2022-06-13 16:09:23.264294
# Unit test for function stringc
def test_stringc():
    assert stringc("text", "blue", wrap_nonvisible_chars=False) == u'\033[34mtext\033[0m'
    assert stringc("text", "blue", wrap_nonvisible_chars=True) == u'\001\033[34m\002text\001\033[0m\002'
    assert stringc("text", "0") == u'\033[30mtext\033[0m'
    assert stringc("text", "1") == u'\033[31mtext\033[0m'
    assert stringc("text", "2") == u'\033[32mtext\033[0m'
    assert stringc("text", "3") == u'\033[33mtext\033[0m'

# Generated at 2022-06-13 16:09:29.215855
# Unit test for function stringc
def test_stringc():
    print(stringc('hello world', 'green'))
    print(stringc('hello world', 'red'))
    print(stringc('hello world', 'blue'))
    print(stringc('hello world', 'yellow'))
    print(stringc('hello world', 'magenta'))
    print(stringc('hello world', 'cyan'))
    print(stringc('hello world', 'white'))
    print(stringc('hello world', 'black'))

