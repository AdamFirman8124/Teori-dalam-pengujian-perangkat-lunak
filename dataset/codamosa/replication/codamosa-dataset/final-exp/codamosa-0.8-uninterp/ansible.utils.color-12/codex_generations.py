

# Generated at 2022-06-13 15:59:41.229467
# Unit test for function stringc
def test_stringc():
    """ Test the stringc() function using hardcoded output data """

    # Test strings

# Generated at 2022-06-13 15:59:52.119339
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor('black') == u'38;5;0'
    assert parsecolor('white') == u'38;5;15'
    assert parsecolor('0') == u'38;5;0'
    assert parsecolor('15') == u'38;5;15'
    assert parsecolor('rgb123') == u'38;5;33'
    assert parsecolor('rgb111') == u'38;5;231'
    assert parsecolor('rgb555') == u'38;5;231'
    assert parsecolor('gray0') == u'38;5;232'
    assert parsecolor('gray23') == u'38;5;234'
    assert parsecolor('gray24') == u'38;5;235'

# Generated at 2022-06-13 16:00:02.019014
# Unit test for function hostcolor
def test_hostcolor():
    # Tests that hostcolor will print the correct color and length for various
    # possible results
    host = 'testhost'
    stats = {'ok': 0, 'changed': 0, 'unreachable': 0, 'failures': 0}
    assert hostcolor(host, stats, True) == u'%-37s' % stringc(host, C.COLOR_OK)

    stats['changed'] = 1
    assert hostcolor(host, stats, True) == u'%-37s' % stringc(host, C.COLOR_CHANGED)

    stats['unreachable'] = 1
    assert hostcolor(host, stats, True) == u'%-37s' % stringc(host, C.COLOR_ERROR)

    stats['unreachable'] = 0
    stats['failures'] = 1

# Generated at 2022-06-13 16:00:08.014780
# Unit test for function hostcolor
def test_hostcolor():
    s = {}
    s['failures'] = 0
    s['changed'] = 0
    s['unreachable'] = 0
    for color in [True, False]:
        yield (colorize, u'ok', s['ok'], C.COLOR_OK)
        yield (colorize, u'changed', s['changed'], C.COLOR_CHANGED)
        yield (colorize, u'unreachable', s['unreachable'], C.COLOR_UNREACHABLE)
        yield (colorize, u'failed', s['failures'], C.COLOR_ERROR)
        yield (colorize, u'ignored', s['ignored'], C.COLOR_SKIP)
        hostcolor(u'foo', s, color)
    s['failures'] = 1
    for color in [True, False]:
        yield

# Generated at 2022-06-13 16:00:18.128735
# Unit test for function hostcolor
def test_hostcolor():

    print(u"Testing function hostcolor, ANSIBLE_NOCOLOR and ANSIBLE_FORCE_COLOR are %s, %s"
          % (C.ANSIBLE_NOCOLOR, C.ANSIBLE_FORCE_COLOR))

    global ANSIBLE_COLOR

    ANSIBLE_COLOR = True

    print(u"Testing hostcolor with no failures, unreachables, or changes")
    color = hostcolor('testhost.example.com', {'failures': 0,
                                               'unreachable': 0,
                                               'changed': 0})
    assert color == u'%-37s' % stringc('testhost.example.com', C.COLOR_OK)

    print(u"Testing hostcolor with no failures or unreachables but with changed")

# Generated at 2022-06-13 16:00:29.739408
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor('black') == '0'
    assert parsecolor('red') == '1'
    assert parsecolor('green') == '2'
    assert parsecolor('yellow') == '3'
    assert parsecolor('blue') == '4'
    assert parsecolor('magenta') == '5'
    assert parsecolor('cyan') == '6'
    assert parsecolor('white') == '7'
    assert parsecolor('default') == '9'
    assert parsecolor('grey') == '15'
    assert parsecolor('bright_red') == '9'
    assert parsecolor('bright_green') == '10'
    assert parsecolor('bright_yellow') == '11'
    assert parsecolor('bright_blue') == '12'

# Generated at 2022-06-13 16:00:34.657276
# Unit test for function colorize
def test_colorize():
    for color in ['red', 'green', 'yellow', 'blue']:
        for n in range(2):
            lead = '<-' + color[0] + '->'
            print(colorize(lead, n, color))
    print()


# Generated at 2022-06-13 16:00:41.478089
# Unit test for function colorize
def test_colorize():
    assert colorize('ok', 0, C.COLOR_OK) == 'ok=0   '
    assert colorize('changed', 0, C.COLOR_CHANGED) == 'changed=0   '
    assert colorize('unreachable', 0, C.COLOR_UNREACHABLE) == 'unreachable=0   '
    assert colorize('failed', 0, C.COLOR_ERROR) == 'failed=0   '
    assert colorize('skipped', 0, C.COLOR_SKIP) == 'skipped=0   '



# Generated at 2022-06-13 16:00:46.689729
# Unit test for function hostcolor
def test_hostcolor():
    desc = 'hostcolor should return a string with the hostname'
    assert hostcolor('localhost', {}) == '%-26s' % 'localhost', desc

    desc = 'hostcolor should return a colorized string with the hostname'
    color = False
    assert hostcolor('localhost', {}, color) == '%-26s' % 'localhost', desc

    desc = 'hostcolor should return a colorized string with the hostname when ANSIBLE_COLOR'
    color = True
    assert hostcolor('localhost', {}, color) == '%-37s' % stringc('localhost', C.COLOR_OK), desc



# Generated at 2022-06-13 16:00:58.926154
# Unit test for function hostcolor
def test_hostcolor():
    def _test_hostcolor_case(stats, expect):
        result = hostcolor(u"foo", stats, True)
        if result != expect:
            raise AssertionError("hostcolor returned '%s' but expected '%s'!" % (result, expect))
    _test_hostcolor_case({"failures": 0, "unreachable": 0, "changed": 0}, u'foo ')
    _test_hostcolor_case({"failures": 0, "unreachable": 0, "changed": 1}, u'\x1b[0;32mfoo\x1b[0m')
    _test_hostcolor_case({"failures": 0, "unreachable": 1, "changed": 0}, u'\x1b[0;31mfoo\x1b[0m')
    _test_host

# Generated at 2022-06-13 16:01:14.867151
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor("localhost", dict(skipped=0, ok=0, failures=0, unreachable=0, changed=0), True) == u"\033[0m%-37s\033[0m" % "localhost"
    assert hostcolor("localhost", dict(skipped=0, ok=0, failures=1, unreachable=0, changed=0), True) == u"\033[0;31m%-37s\033[0m" % "localhost"
    assert hostcolor("localhost", dict(skipped=0, ok=0, failures=0, unreachable=1, changed=0), True) == u"\033[0;31m%-37s\033[0m" % "localhost"

# Generated at 2022-06-13 16:01:21.571840
# Unit test for function parsecolor
def test_parsecolor():
    assert(parsecolor('blue') == u'34')
    assert(parsecolor('color1') == u'38;5;1')
    assert(parsecolor('rgb555') == u'38;5;8')
    assert(parsecolor('rgb123') == u'38;5;18')
    assert(parsecolor('rgb333') == u'38;5;52')
    assert(parsecolor('rgb444') == u'38;5;58')
    assert(parsecolor('rgb442') == u'38;5;57')
    assert(parsecolor('rgb000') == u'38;5;16')
    assert(parsecolor('rgb555') == u'38;5;8')

# Generated at 2022-06-13 16:01:31.653085
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor('black') == u'30'
    assert parsecolor('red') == u'31'
    assert parsecolor('green') == u'32'
    assert parsecolor('yellow') == u'33'
    assert parsecolor('blue') == u'34'
    assert parsecolor('magenta') == u'35'
    assert parsecolor('cyan') == u'36'
    assert parsecolor('white') == u'37'
    assert parsecolor('color0') == u'38;5;0'
    assert parsecolor('color8') == u'38;5;8'
    assert parsecolor('color15') == u'38;5;15'
    assert parsecolor('rgb000') == u'38;5;16'

# Generated at 2022-06-13 16:01:39.080696
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor(u'blue') == u'34'
    assert parsecolor(u'bold') == u'1'
    assert parsecolor(u'red') == u'31'
    assert parsecolor(u'underline') == u'4'
    assert parsecolor(u'cyan') == u'36'
    assert parsecolor(u'green') == u'32'
    assert parsecolor(u'magenta') == u'35'
    assert parsecolor(u'yellow') == u'33'
    assert parsecolor(u'white') == u'37'
    assert parsecolor(u'black') == u'30'
    assert parsecolor(u'reset') == u'0'
    assert parsecolor(u'on_blue') == u'44'

# Generated at 2022-06-13 16:01:45.897974
# Unit test for function stringc
def test_stringc():
    assert stringc(u'hello', u'green') == u'\033[32mhello\033[0m'
    assert stringc(u'goodbye', u'blink') == u'\033[5mgoodbye\033[0m'
    assert stringc(u'oh no', u'red blink') == u'\033[31;5moh no\033[0m'

# safely end this program - nothing below this line runs
if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 16:01:50.131051
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor('red') == '31'
    assert parsecolor('cyan') == '36'
    assert parsecolor('color1') == '38;5;1'
    assert parsecolor('rgb211') == '38;5;39'
    assert parsecolor('rgb122') == '38;5;28'
    assert parsecolor('rgb202') == '38;5;38'
    assert parsecolor('gray0') == '38;5;232'
    assert parsecolor('gray7') == '38;5;239'



# Generated at 2022-06-13 16:02:00.283980
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor('red') == '31'
    assert parsecolor('color8') == '38;5;8'
    assert parsecolor('rgb25533221') == '38;5;196'
    assert parsecolor('rgb000') == '38;5;16'
    assert parsecolor('rgb255255255') == '38;5;231'
    assert parsecolor('rgb255050') == '38;5;94'
    assert parsecolor('rgb2552552550') == '38;5;231'
    assert parsecolor('gray0') == '38;5;232'
    assert parsecolor('gray23') == '38;5;255'
    assert parsecolor('random') == '38;5;208'

# Generated at 2022-06-13 16:02:08.242678
# Unit test for function parsecolor
def test_parsecolor():
    import pytest

# Generated at 2022-06-13 16:02:17.524675
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor('black') == u'38;5;0'
    assert parsecolor('rgb255255255') == u'38;5;15'
    assert parsecolor('rgb000') == u'38;5;16'
    assert parsecolor('rgb255255000') == u'38;5;226'
    assert parsecolor('rgb000255000') == u'38;5;46'
    assert parsecolor('rgb000255255') == u'38;5;51'
    assert parsecolor('rgb255000255') == u'38;5;201'
    assert parsecolor('rgb255000000') == u'38;5;196'
    assert parsecolor('rgb000000255') == u'38;5;21'

# Generated at 2022-06-13 16:02:26.718835
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor("127.0.0.1", dict(failures=0, unreachable=0, changed=0)) == "127.0.0.1                      "
    assert hostcolor("127.0.0.1", dict(failures=0, unreachable=0, changed=1)) == "127.0.0.1                      "
    assert hostcolor("127.0.0.1", dict(failures=0, unreachable=1, changed=0)) == "127.0.0.1                      "
    assert hostcolor("127.0.0.1", dict(failures=1, unreachable=0, changed=0)) == "127.0.0.1                      "



# Generated at 2022-06-13 16:02:42.159409
# Unit test for function hostcolor
def test_hostcolor():
    testcases = (
        (dict(failures=1, unreachable=0, changed=0), C.COLOR_ERROR),
        (dict(failures=0, unreachable=1, changed=0), C.COLOR_ERROR),
        (dict(failures=0, unreachable=0, changed=1), C.COLOR_CHANGED),
        (dict(failures=0, unreachable=0, changed=0), C.COLOR_OK)
    )
    for stats, color in testcases:
        yield (stats, color)
        host = 'test'
        if ANSIBLE_COLOR:
            assert hostcolor(host, stats, color=True) == u"%-37s" % stringc(host, color)

# Generated at 2022-06-13 16:02:49.982061
# Unit test for function hostcolor
def test_hostcolor():
    for color in (True, False):
        for host in (u"localhost", u"localhost.localdomain", u"127.0.0.1"):
            assert hostcolor(host, dict(changed=0, failures=0, unreachable=0, skipped=0)) == u'%-26s' % host
            assert hostcolor(host, dict(changed=1, failures=0, unreachable=0, skipped=0), color=color) == u'%-37s' % host
    assert hostcolor(u"host.example.net", dict(changed=0, failures=0, unreachable=0, skipped=0)) == u'%-26s' % u'host.example.net'
    assert hostcolor(u"host.example.net", dict(changed=1, failures=0, unreachable=0, skipped=0)) == u

# Generated at 2022-06-13 16:02:56.259097
# Unit test for function hostcolor
def test_hostcolor():
    host = 'testhost'
    stats = {}
    stats['failures'] = 0
    stats['unreachable'] = 0
    stats['changed'] = 0
    print(hostcolor(host, stats))
    stats['failures'] = 1
    print(hostcolor(host, stats))
    stats['failures'] = 0
    stats['unreachable'] = 1
    print(hostcolor(host, stats))
    stats['unreachable'] = 0
    stats['changed'] = 1
    print(hostcolor(host, stats))

# --- end "pretty"



# Generated at 2022-06-13 16:03:04.649600
# Unit test for function colorize
def test_colorize():
    print("colorize('ok', 0, 'C.COLOR_OK'): %s" %
          colorize('ok', 0, C.COLOR_OK))
    print("colorize('changed', 1, 'C.COLOR_CHANGED'): %s" %
          colorize('changed', 1, C.COLOR_CHANGED))
    print("colorize('unreachable', 2, 'C.COLOR_UNREACHABLE'): %s" %
          colorize('unreachable', 2, C.COLOR_UNREACHABLE))
    print("colorize('failed', 3, 'C.COLOR_ERROR'): %s" %
          colorize('failed', 3, C.COLOR_ERROR))



# Generated at 2022-06-13 16:03:15.213500
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('a', {'failures': 1,
                           'changed': 0,
                           'unreachable': 1}) == u"a                        "
    # Toggle ANSIBLE_COLOR on before testing hostcolor
    global ANSIBLE_COLOR
    ANSIBLE_COLOR = True
    assert hostcolor('a', {'failures': 1,
                           'changed': 0,
                           'unreachable': 1}) == u"\u001b[91ma                        \u001b[0m"
    assert hostcolor('a', {'failures': 0,
                           'changed': 1,
                           'unreachable': 0}) == u"\u001b[33ma                        \u001b[0m"

# Generated at 2022-06-13 16:03:23.663870
# Unit test for function colorize
def test_colorize():
    assert colorize(u"foo", 0, u"red") == u"foo=0   "
    assert colorize(u"foo", 0, None) == u"foo=0   "
    assert colorize(u"foo", 1, u"red") == u"foo=1   "
    assert colorize(u"foo", 2, u"red") == u"foo=2   "
    assert colorize(u"foo", 12, u"red") == u"foo=12  "
    assert colorize(u"foo", 123, u"red") == u"foo=123 "
    assert colorize(u"foo", 1234, u"red") == u"foo=1234"
    assert colorize(u"foo", 12345, u"red") == u"foo=12345"



# Generated at 2022-06-13 16:03:28.434433
# Unit test for function hostcolor
def test_hostcolor():
    stats = dict(failures=0, unreachable=0, changed=0)
    assert hostcolor('localhost', stats, True) == u'%-37s' % stringc('localhost', C.COLOR_OK)
    stats = dict(failures=1, unreachable=0, changed=0)
    assert hostcolor('localhost', stats, True) == u'%-37s' % stringc('localhost', C.COLOR_ERROR)
    stats = dict(failures=0, unreachable=1, changed=0)
    assert hostcolor('localhost', stats, True) == u'%-37s' % stringc('localhost', C.COLOR_ERROR)
    stats = dict(failures=0, unreachable=0, changed=1)

# Generated at 2022-06-13 16:03:30.019098
# Unit test for function hostcolor
def test_hostcolor():
    # Make sure it doesn't throw an exception
    hostcolor('localhost', dict(failures=0, unreachable=0, changed=0), True)

# --- end "pretty"



# Generated at 2022-06-13 16:03:41.151572
# Unit test for function hostcolor
def test_hostcolor():
    def test(host, stats, color, ansi):
        if ansi:
            prefix = u'\033['
            suffix = u'\033[0m'
        else:
            prefix = u''
            suffix = u''
        status = hostcolor(host, stats, color)
        if stats['failures'] != 0 or stats['unreachable'] != 0:
            assert status == u"%-37s" % (prefix + C.COLOR_ERROR + suffix + host)
        elif stats['changed'] != 0:
            assert status == u"%-37s" % (prefix + C.COLOR_CHANGED + suffix + host)
        else:
            assert status == u"%-37s" % (prefix + C.COLOR_OK + suffix + host)

    # Test cases

# Generated at 2022-06-13 16:03:49.236564
# Unit test for function stringc
def test_stringc():
    assert stringc('hello world', 'blue') == "\033[34mhello world\033[0m"
    assert stringc('hello world', '33') == "\033[33mhello world\033[0m"
    assert stringc('hello world', 'rgb255255255') == "\033[37mhello world\033[0m"
    assert stringc('hello world', 'rgb000255000') == "\033[32mhello world\033[0m"
    assert stringc('hello world', 'rgb255000255') == "\033[35mhello world\033[0m"

# --- end of pretty.py



# Generated at 2022-06-13 16:03:58.687059
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('foobar', {}) == 'foobar'



# Generated at 2022-06-13 16:04:08.000596
# Unit test for function colorize
def test_colorize():
    for lead in ("", " ", "X"):
        for num in (0, 1):
            for color in (None, 'blue',):
                s = colorize(lead, num, color)
                #print (lead, num, color, ":", s)
                assert type(s) == unicode


# ---- end of pretty.py

from ansible.parsing.utils.addresses import parse_address
from ansible.utils.unsafe_proxy import AnsibleUnsafeText
from ansible.template import Templar

from ansible.utils.unicode import to_unicode

from ansible.plugins.callback import CallbackBase

from collections import defaultdict
from io import StringIO



# Generated at 2022-06-13 16:04:19.467784
# Unit test for function stringc
def test_stringc():
    assert stringc('Hello', 'red') == u"\033[31mHello\033[0m"
    assert stringc('Hello', 'red', wrap_nonvisible_chars=True) == u"\001\033[31m\002Hello\001\033[0m\002"
    assert stringc('Hello\nWorld', 'red') == u"\033[31mHello\033[0m\n\033[31mWorld\033[0m"
    assert stringc('Hello\nWorld', 'red', wrap_nonvisible_chars=True) == u"\001\033[31m\002Hello\001\033[0m\002\n\001\033[31m\002World\001\033[0m\002"

# Generated at 2022-06-13 16:04:30.412029
# Unit test for function hostcolor
def test_hostcolor():
    import ast

# Generated at 2022-06-13 16:04:38.698409
# Unit test for function stringc
def test_stringc():
    assert(stringc('foo', 'blue') == '\033[34mfoo\033[0m')
    assert(stringc('foo', '0') == '\033[38;5;0mfoo\033[0m')
    assert(stringc('foo', 'rgb255000') == '\033[38;5;9mfoo\033[0m')
    assert(stringc('foo', 'rgb000255') == '\033[38;5;33mfoo\033[0m')


# --- end "pretty"
#
# The code below is released into the public domain.
# Originally based on the "ansiterm" plugin by Kirk Strauser <kirk@strauser.com>

# ANSI Escape Sequences
#
#   Trailing characters are not part of the sequence.
#   No sequences are two characters

# Generated at 2022-06-13 16:04:41.328452
# Unit test for function colorize
def test_colorize():
    """
    %s = 'foo'
    """

    # pylint: disable=E0602
    if colorize('%s', 'foo', 'red') != stringc('%s=foo', 'red'):
        raise AssertionError()

# Generated at 2022-06-13 16:04:52.894471
# Unit test for function hostcolor
def test_hostcolor():
    test_host = u"1234"
    test_stats = {'ok':1, 'changed':0, 'failures':0, 'unreachable':0}
    assert hostcolor(test_host, test_stats, True) == u"%-37s" % stringc(test_host, C.COLOR_OK)

    test_stats = {'ok':1, 'changed':1, 'failures':0, 'unreachable':0}
    assert hostcolor(test_host, test_stats, True) == u"%-37s" % stringc(test_host, C.COLOR_CHANGED)

    test_stats = {'ok':1, 'changed':0, 'failures':1, 'unreachable':0}
    assert hostcolor(test_host, test_stats, True) == u"%-37s"

# Generated at 2022-06-13 16:05:04.424516
# Unit test for function colorize
def test_colorize():
    """ Unit test for function colorize """
    from ansible.utils.color import colorize
    import sys
    import termios
    from select import select

    if sys.stdout.isatty():
        # curses isn't available on all platforms
        try:
            import curses
        except ImportError:
            sys.exit(0)

        # Save the terminal settings
        fd = sys.stdin.fileno()
        new = termios.tcgetattr(fd)
        old = termios.tcgetattr(fd)

        # New terminal setting unbuffered
        new[3] = (new[3] & ~termios.ICANON & ~termios.ECHO)
        termios.tcsetattr(fd, termios.TCSANOW, new)

        # Support normal-length and single-character input
        c = None

# Generated at 2022-06-13 16:05:06.397307
# Unit test for function stringc
def test_stringc():
    assert stringc('foo', 'red', False) == u'\033[31mfoo\033[0m'



# Generated at 2022-06-13 16:05:15.575203
# Unit test for function stringc
def test_stringc():
    print("TEST: Testing stringc")
    print(stringc("This is black", "black"))
    print(stringc("This is red", "red"))
    print(stringc("This is green", "green"))
    print(stringc("This is yellow", "yellow"))
    print(stringc("This is blue", "blue"))
    print(stringc("This is magenta", "magenta"))
    print(stringc("This is cyan", "cyan"))
    print(stringc("This is white", "white"))
    print(stringc("This is default", "default"))
    print(stringc("This is bright black", "brightblack"))
    print(stringc("This is bright red", "brightred"))
    print(stringc("This is bright green", "brightgreen"))

# Generated at 2022-06-13 16:05:31.864266
# Unit test for function stringc
def test_stringc():
    """Function stringc() test"""
    print(stringc('Reverse is not black', 'RED'))
    print(stringc('Reverse is not black', 'BLUE'))
    print(stringc('Reverse is not black', 'GREEN'))
    print(stringc('Reverse is not black', 'YELLOW'))
    print(stringc('Reverse is not black', 'MAGENTA'))
    print(stringc('Reverse is not black', 'CYAN'))
    print(stringc('Reverse is not black', 'WHITE'))

    print(stringc('Reverse is not black', 'rgb255000'))
    print(stringc('Reverse is not black', 'rgb255255255'))

# Generated at 2022-06-13 16:05:41.591114
# Unit test for function hostcolor
def test_hostcolor():
    import json
    import color_diff

    host = "localhost"
    stats = {'skipped': 0, 'failures': 3, 'changed': 0, 'ok': 2, 'unreachable': 0}
    fail = u'(\u001b[38;5;9mlocalhost\u001b[0m)'
    assert hostcolor(host, stats) == u"%-37s" % fail
    stats = {'skipped': 0, 'failures': 0, 'changed': 3, 'ok': 2, 'unreachable': 0}
    change = u'(\u001b[38;5;214mlocalhost\u001b[0m)'
    assert hostcolor(host, stats) == u"%-37s" % change

# Generated at 2022-06-13 16:05:48.264885
# Unit test for function parsecolor

# Generated at 2022-06-13 16:05:54.114155
# Unit test for function parsecolor

# Generated at 2022-06-13 16:06:04.019435
# Unit test for function colorize
def test_colorize():
    assert u"a=1" == colorize(u"a", 1, None)
    assert u"a=0" == colorize(u"a", 0, None)
    assert u"a=-1" == colorize(u"a", -1, None)
    # We only care if we operate in ANSIBLE_COLOR mode
    if ANSIBLE_COLOR:
        assert u"\x1b[31ma=1\x1b[0m" == colorize(u"a", 1, C.COLOR_ERROR)
        assert u"\x1b[31ma=0\x1b[0m" == colorize(u"a", 0, C.COLOR_ERROR)

# Generated at 2022-06-13 16:06:12.552947
# Unit test for function colorize
def test_colorize():
    assert colorize('foo', 4, 'black') == 'foo=4   '
    assert colorize('foo', 0, 'black') == 'foo=0   '
    assert colorize('foo', 1234, 'black') == 'foo=1234'
    assert colorize('f' * 50, 4, 'black') == ('f' * 46) + '=4   '
    assert colorize('foo', 4, None) == 'foo=4   '
    assert colorize('foo', 4, 'blue') == 'foo=4   '


# Generated at 2022-06-13 16:06:15.723167
# Unit test for function stringc
def test_stringc():
    assert stringc('text', 'blue') == u"\033[34mtext\033[0m"
    assert stringc('text', 'rgb255') == u"\033[38;5;214mtext\033[0m"



# Generated at 2022-06-13 16:06:18.161076
# Unit test for function colorize
def test_colorize():
    colorize('hello', 3, 'black')


# --- end of "pretty"



# Generated at 2022-06-13 16:06:27.505673
# Unit test for function parsecolor
def test_parsecolor():
    # Test the function parsecolor with real valid and invalid color strings
    assert(parsecolor('black') == u'30')
    assert(parsecolor('black') != u'rgb122')
    assert(parsecolor('color8') == u'38;5;8')
    assert(parsecolor('color8') != u'color18')
    assert(parsecolor('rgb222') == u'38;5;248')
    assert(parsecolor('rgb222') != u'38;5;258')
    assert(parsecolor('gray8') == u'38;5;238')
    assert(parsecolor('gray8') != u'gray18')
    # Test for invalid color strings
    assert(parsecolor('color256') is None)

# Generated at 2022-06-13 16:06:37.208133
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor(u'localhost : ok', dict(
        changed=0, unreachable=0, failures=0)) == u'localhost              \x1b[0;32m\x1b[0m'
    assert hostcolor(u'localhost : changed', dict(
        changed=1, unreachable=0, failures=0)) == u'localhost              \x1b[0;33m\x1b[0m'
    assert hostcolor(u'localhost : unreachable', dict(
        changed=0, unreachable=1, failures=0)) == u'localhost              \x1b[0;31m\x1b[0m'

# Generated at 2022-06-13 16:07:01.907748
# Unit test for function hostcolor
def test_hostcolor():
    class args(object):
        """A simple class to hold the arguments"""
        displays = None

    args.displays = ['verbose']
    stats = {
        'ok': 10,
        'failures': 1,
        'changed': 2,
        'unreachable': 3
    }
    assert hostcolor(u"test", stats) == u"test                             "
    assert hostcolor(u"test", stats, False) == u"test                       "
    stats = {
        'ok': 10,
        'failures': 0,
        'changed': 0,
        'unreachable': 0
    }
    assert hostcolor(u"test", stats) == u"test                             "



# Generated at 2022-06-13 16:07:05.814182
# Unit test for function colorize
def test_colorize():
    """ test_colorize - unit-test for function colorize """
    assert colorize(u"a", 2, C.COLOR_WARN) == u"\033[93ma=2  \033[0m", "colorize failed"



# Generated at 2022-06-13 16:07:15.224792
# Unit test for function stringc
def test_stringc():
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    from ansible.utils.color import stringc

    assert(stringc("hello", "CYAN") == u"\033[96mhello\033[0m")
    assert(stringc([u'foo'], 'CYAN') == u"\033[96mfoo\033[0m")
    assert(stringc(['foo'], 'CYAN') == u"\033[96mfoo\033[0m")
    assert(stringc({'foo': 'bar'}, 'CYAN') == u"\033[96m")
    assert(stringc(u"{{ bar }}", "CYAN") == u"\033[96m{{ bar }}\033[0m")


# Generated at 2022-06-13 16:07:23.444751
# Unit test for function hostcolor
def test_hostcolor():
    stats = dict(changed=0, dark=0, failures=0, unreachable=0, ok=1)
    assert hostcolor('myserver', stats) == 'myserver'
    stats = dict(changed=1, dark=0, failures=0, unreachable=0, ok=0)
    assert hostcolor('myserver', stats) == '\033[0;34mmyserver\033[0m'
    stats = dict(changed=0, dark=0, failures=0, unreachable=1, ok=0)
    assert hostcolor('myserver', stats) == '\033[0;31mmyserver\033[0m'

# --- end of "pretty" code


# Generated at 2022-06-13 16:07:29.702880
# Unit test for function parsecolor

# Generated at 2022-06-13 16:07:39.469672
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('i-1234567', dict(changed=0, failures=0, unreachable=0), True) == u'i-1234567                  '
    assert hostcolor('i-1234567', dict(changed=0, failures=0, unreachable=0), False) == u'i-1234567                '
    assert hostcolor('i-1234567', dict(changed=1, failures=0, unreachable=0), True) == u"\x1b[0;34mi-1234567\x1b[0m      "
    assert hostcolor('i-1234567', dict(changed=0, failures=1, unreachable=0), True) == u"\x1b[0;31mi-1234567\x1b[0m      "

# Generated at 2022-06-13 16:07:45.381954
# Unit test for function stringc
def test_stringc():
    assert stringc(u'hello', 'blue') == u"\033[34mhello\033[0m"
    assert stringc(u'hello', 'deep blue') == u"\033[34mhello\033[0m"
    assert stringc(u'hello', 'cyan') == u"\033[36mhello\033[0m"
    assert stringc(u'hello', 'black') == u"\033[30mhello\033[0m"
    assert stringc(u'hello', 'bLack') == u"\033[30mhello\033[0m"
    assert stringc(u'hello', 'color1') == u"\033[38;5;1mhello\033[0m"

# Generated at 2022-06-13 16:07:55.416546
# Unit test for function colorize
def test_colorize():
    from ansible.utils.color import colorize
    from ansible.utils.color import colorize_ansi

    assert colorize_ansi is colorize

    # let's test some colors
    #

    # good
    assert colorize('p', 12, 'green') == "\033[32mp=12  \033[0m"
    assert colorize('p', 12, '00ff00') == "\033[32mp=12  \033[0m"
    # bad
    assert colorize('p', 12, 'foo') == "\033[32mp=12  \033[0m"
    # (passing None for color is like passing False for color)
    assert colorize('p', 12, None) == "p=12  "
    assert colorize('p', 12, False) == "p=12  "



# Generated at 2022-06-13 16:08:05.726588
# Unit test for function hostcolor
def test_hostcolor():
    good_result = "abcdefghijklmnopqrstuvwxyz       "
    assert good_result == hostcolor("abcdefghijklmnopqrstuvwxyz", {}, color=False)
    assert good_result == hostcolor("abcdefghijklmnopqrstuvwxyz", {}, color=True)

    bad_result = "abcdefghijklmnopqrstuvwxyz       "
    assert bad_result == hostcolor("abcdefghijklmnopqrstuvwxyz", { "failures": 1 }, color=False)
    assert bad_result == hostcolor("abcdefghijklmnopqrstuvwxyz", { "unreachable": 1 }, color=False)


# Generated at 2022-06-13 16:08:15.762890
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('1.1.1.1', {}) == u'1.1.1.1                    '
    assert hostcolor('1.1.1.1', {'failures': 1})[:12] == u'1.1.1.1       '
    assert hostcolor('1.1.1.1', {'failures': 1})[-5:] == u'\x1b[31m\x1b[0m'
    assert hostcolor('1.1.1.1', {'changed': 1})[:12] == u'1.1.1.1       '
    assert hostcolor('1.1.1.1', {'changed': 1})[-12:] == u'\x1b[33m\x1b[0m    '

# Generated at 2022-06-13 16:09:01.281154
# Unit test for function stringc

# Generated at 2022-06-13 16:09:06.645825
# Unit test for function colorize
def test_colorize():
    assert colorize('ok', 0, C.COLOR_OK) == 'ok=0   '
    assert colorize('changed', 0, C.COLOR_CHANGED) == 'changed=0   '
    assert colorize('failed', 0, C.COLOR_ERROR) == 'failed=0   '
    assert colorize('dark', 'dark', 'dark') == 'dark=dark'



# Generated at 2022-06-13 16:09:12.628802
# Unit test for function stringc
def test_stringc():
    import sys
    for color in C.COLOR_CODES:
        print("%s" % stringc("Testing %s color." % color, color))
    print("\n")
    if sys.version_info < (3, 0):
        for color in C.COLOR_CODES:
            print("%s" % stringc(u"Testing %s color." % color, color))



# Generated at 2022-06-13 16:09:21.038950
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor("green") == "32"
    assert parsecolor("red")   == "31"
    assert parsecolor("blue")  == "34"
    assert parsecolor("rgb255") == "38;5;255"
    assert parsecolor("rgb256") == "38;5;256"
    assert parsecolor("rgb000") == "38;5;0"
    assert parsecolor("rgb100") == "38;5;100"
    assert parsecolor("rgb001") == "38;5;6"
    assert parsecolor("rgb010") == "38;5;36"
    assert parsecolor("rgb011") == "38;5;42"
    assert parsecolor("gray0") == "38;5;232"

# Generated at 2022-06-13 16:09:30.367308
# Unit test for function hostcolor
def test_hostcolor():
    stats1 = dict(ok=1, failures=0, unreachable=0, changed=0)
    stats2 = dict(ok=1, failures=1, unreachable=0, changed=0)
    stats3 = dict(ok=0, failures=0, unreachable=1, changed=0)
    stats4 = dict(ok=1, failures=0, unreachable=0, changed=1)
    stats5 = dict(ok=0, failures=1, unreachable=1, changed=1)

    # test all ok
    hostcolor('foobar', stats1, color=True) == u"\033[0;32m%-26s\033[0m" % 'foobar'

    # one failure