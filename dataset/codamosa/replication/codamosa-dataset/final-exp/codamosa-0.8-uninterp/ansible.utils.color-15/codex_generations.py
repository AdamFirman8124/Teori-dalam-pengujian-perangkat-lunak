

# Generated at 2022-06-13 15:59:39.436513
# Unit test for function stringc
def test_stringc():
    """Test stringc function."""
    bgcolors = [u'black', u'red', u'green', u'yellow', u'blue',
                u'magenta', u'cyan', u'white']

# Generated at 2022-06-13 15:59:47.571776
# Unit test for function colorize
def test_colorize():
    assert colorize('   ok', '0', C.COLOR_OK) == '   ok=0    '
    assert colorize('  fail', '2', C.COLOR_ERROR) == '  fail=2  '
    assert colorize('  skip', '1', C.COLOR_SKIP) == '  skip=1  '
    assert colorize('unreach', '3', C.COLOR_UNREACHABLE) == 'unreach=3'


# Generated at 2022-06-13 15:59:55.849664
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor('red') == u'31'
    assert parsecolor('on_red') == u'41'
    assert parsecolor('blue') == u'34'
    assert parsecolor('on_blue') == u'44'
    assert parsecolor('black') == u'30'
    assert parsecolor('on_black') == u'40'
    assert parsecolor('green') == u'32'
    assert parsecolor('on_green') == u'42'
    assert parsecolor('yellow') == u'33'
    assert parsecolor('on_yellow') == u'43'
    assert parsecolor('cyan') == u'36'
    assert parsecolor('on_cyan') == u'46'
    assert parsecolor('magenta') == u'35'

# Generated at 2022-06-13 16:00:04.268649
# Unit test for function hostcolor
def test_hostcolor():
    colorized_host = hostcolor(u'testa', dict(changed=0, failures=0, ok=2, skipped=0, unreachable=0))
    assert colorized_host == u'%-37stesta' % stringc(u'', C.COLOR_OK)

    colorized_host = hostcolor(u'testb', dict(changed=2, failures=0, ok=0, skipped=0, unreachable=0))
    assert colorized_host == u'%-37stestb' % stringc(u'', C.COLOR_CHANGED)

    colorized_host = hostcolor(u'testc', dict(changed=0, failures=2, ok=0, skipped=0, unreachable=0))

# Generated at 2022-06-13 16:00:09.888064
# Unit test for function stringc
def test_stringc():
    c = stringc('text', 'red')
    assert c == '\x1b[31mtext\x1b[0m'
    c = stringc('text', 'rgb25515')
    assert c == '\x1b[38;5;12mtext\x1b[0m'
    c = stringc('text', 'rgb25500')
    assert c == '\x1b[38;5;9mtext\x1b[0m'
    c = stringc('text', 'rgb25500', wrap_nonvisible_chars=True)
    assert c == '\x01\x1b[38;5;9m\x02text\x01\x1b[0m\x02'



# Generated at 2022-06-13 16:00:16.826102
# Unit test for function colorize
def test_colorize():
    """ basic functionality test for colorize """

    color_list = C.COLOR_OK, C.COLOR_CHANGED, C.COLOR_SKIP, C.COLOR_UNREACHABLE, C.COLOR_ERROR
    for color in color_list:
        # Each color should be different
        assert len(set([colorize('', 'X', color) for color in color_list])) == len(color_list)
        # Normal color should be different from colorized
        assert colorize('', 'X', None) != colorize('', 'X', color)



# Generated at 2022-06-13 16:00:25.386756
# Unit test for function stringc
def test_stringc():
    """
    Some basic unit tests for stringc
    """
    assert parsecolor('red') == C.COLOR_CODES['red'], "should match 'RED'"
    assert parsecolor('green') == C.COLOR_CODES['green'], "should match 'GREEN'"
    assert parsecolor('white') == C.COLOR_CODES['white'], "should match 'WHITE'"
    assert parsecolor('blue') == C.COLOR_CODES['blue'], "should match 'BLUE'"
    assert parsecolor('cyan') == C.COLOR_CODES['cyan'], "should match 'CYAN'"
    assert parsecolor('yellow') == C.COLOR_CODES['yellow'], "should match 'YELLOW'"
    assert parsecolor('dark gray') == C.COLOR_

# Generated at 2022-06-13 16:00:32.078481
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor('blue') == u'38;5;4'
    assert parsecolor('red') == u'38;5;1'
    assert parsecolor('black') == u'38;5;16'
    assert parsecolor('white') == u'38;5;15'
    assert parsecolor('rgb255255255') == u'38;5;231'
    assert parsecolor('rgb000255000') == u'38;5;2'
    assert parsecolor('rgb255000255') == u'38;5;5'
    assert parsecolor('rgb01234567') == u'38;5;196'
    assert parsecolor('gray255') == u'38;5;231'
    assert parsecolor('gray0') == u'38;5;232'


# Generated at 2022-06-13 16:00:42.506472
# Unit test for function stringc
def test_stringc():
    """
    >>> c = lambda x: stringc(x, 'red', wrap_nonvisible_chars=True)
    >>> print("" + c("abcd"))
    \001\033[38;5;9m\002abcd\001\033[0m\002
    >>> print(c("abcd") == "\\001\\033[38;5;9m\\002abcd\\001\\033[0m\\002")
    True
    >>> c = lambda x: stringc(x, 'red')
    >>> print("" + c("abcd"))
    \033[38;5;9mabcd\033[0m
    >>> print(c("abcd") == "\\033[38;5;9mabcd\\033[0m")
    True
    """
    import doctest
    doctest.testmod

# Generated at 2022-06-13 16:00:49.583097
# Unit test for function parsecolor

# Generated at 2022-06-13 16:01:04.585270
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor('black') == '38;5;0'
    assert parsecolor('color0') == '38;5;0'
    assert parsecolor('color16') == '38;5;16'
    assert parsecolor('color1') == '38;5;1'
    assert parsecolor('color16') == '38;5;16'
    assert parsecolor('color255') == '38;5;255'

    assert parsecolor('rgb000') == '38;5;0'
    assert parsecolor('rgb255') == '38;5;255'
    assert parsecolor('rgb222') == '38;5;59'
    assert parsecolor('rgb123') == '38;5;123'

# Generated at 2022-06-13 16:01:14.699026
# Unit test for function hostcolor
def test_hostcolor():
    print(u"%s %s" % (hostcolor(u"testhost1", dict(changed=0, failures=0, unreachable=0)), u"OK"))
    print(u"%s %s" % (hostcolor(u"testhost2", dict(changed=0, failures=1, unreachable=1)), u"FAILED"))
    print(u"%s %s" % (hostcolor(u"testhost3", dict(changed=1, failures=0, unreachable=0)), u"CHANGED"))
    print(u"%s %s" % (hostcolor(u"testhost4", dict(changed=0, failures=0, unreachable=0), False), u"OK"))



# Generated at 2022-06-13 16:01:21.526913
# Unit test for function hostcolor
def test_hostcolor():
    # Default colors
    colors = dict(C.DEFAULT_PASSWORD_COLORS)

    # No color
    assert hostcolor(u'fakehost', dict(failures=0, unreachable=0,
                                       changed=0), False) == u'fakehost               '

    # Default colors
    assert hostcolor(u'fakehost', dict(failures=0, unreachable=0,
                                       changed=0)) == u'%s%-37s\033[0m' % (colors['ok'], u'fakehost')
    assert hostcolor(u'fakehost', dict(failures=1, unreachable=0,
                                       changed=0)) == u'%s%-37s\033[0m' % (colors['error'], u'fakehost')

# Generated at 2022-06-13 16:01:29.707530
# Unit test for function stringc
def test_stringc():
    assert stringc(u"hello", u"ok") == u"\033[32mhello\033[0m"
    assert stringc(u"hello", u"changed") == u"\033[94mhello\033[0m"
    assert stringc(u"hello", u"error") == u"\033[31mhello\033[0m"
    assert stringc(u"hello", u"emphasized") == u"\033[1mhello\033[0m"
    assert stringc(u"hello", u"header") == u"\033[95mhello\033[0m"



# Generated at 2022-06-13 16:01:38.812928
# Unit test for function parsecolor

# Generated at 2022-06-13 16:01:48.260439
# Unit test for function hostcolor
def test_hostcolor():
    # Set up a dictionary of stats for various hosts
    s = {}
    # change, fail, unreach, ok
    s['alpha'] = {'changed': 0, 'failures': 0, 'unreachable': 0, 'ok': 2}
    s['beta'] = {'changed': 1, 'failures': 0, 'unreachable': 0, 'ok': 1}
    s['gamma'] = {'changed': 0, 'failures': 1, 'unreachable': 0, 'ok': 1}
    s['delta'] = {'changed': 0, 'failures': 0, 'unreachable': 1, 'ok': 1}
    s['epsilon'] = {'changed': 0, 'failures': 1, 'unreachable': 1, 'ok': 0}
    # Expected results
    e = {}
   

# Generated at 2022-06-13 16:01:59.265882
# Unit test for function hostcolor
def test_hostcolor():
    # First we test with color disabled
    example_stats1 = dict(skipped=0, ok=3, failures=2, unreachable=1, changed=0)
    example_host1 = 'localhost'

    assert hostcolor(example_host1, example_stats1, color=False) == u"%-26s" % example_host1
    assert hostcolor(example_host1, example_stats1, color=True) == u'%-37s' % stringc(example_host1, C.COLOR_ERROR)

    # Then we test with color enabled with the stats dict having failures
    example_stats1 = dict(skipped=0, ok=3, failures=2, unreachable=1, changed=0)
    example_host1 = 'localhost'

    assert hostcolor(example_host1, example_stats1, color=False)

# Generated at 2022-06-13 16:02:07.395591
# Unit test for function stringc
def test_stringc():
    """ Ensure the stringc() function is working correctly """
    # Valid colors
    assert stringc(u"black", u"black") == u"\033[30mblack\033[0m"
    assert stringc(u"red", u"red") == u"\033[31mred\033[0m"
    assert stringc(u"green", u"green") == u"\033[32mgreen\033[0m"
    assert stringc(u"yellow", u"yellow") == u"\033[33myellow\033[0m"
    assert stringc(u"blue", u"blue") == u"\033[34mblue\033[0m"
    assert stringc(u"magenta", u"magenta") == u"\033[35mmagenta\033[0m"

# Generated at 2022-06-13 16:02:16.701384
# Unit test for function hostcolor
def test_hostcolor():
    # This code is executed when the module is imported.
    # Test colors for failures, unreacheables, and changes
    fail_stats = dict(failures=1, unreachable=0, changed=0)
    unreach_stats = dict(failures=0, unreachable=1, changed=0)
    change_stats = dict(failures=0, unreachable=0, changed=1)
    print(hostcolor('test1', fail_stats, color=False), hostcolor('test1', fail_stats, color=True))
    print(hostcolor('test2', unreach_stats, color=False), hostcolor('test2', unreach_stats, color=True))
    print(hostcolor('test3', change_stats, color=False), hostcolor('test3', change_stats, color=True))
    # Test colors when host is

# Generated at 2022-06-13 16:02:26.536448
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor('red') == u'31'
    assert parsecolor('dark red') == u'31'
    assert parsecolor('bold red') == u'31;1'

    assert parsecolor('color1') == u'38;5;1'
    assert parsecolor('rgb123') == u'38;5;18'
    assert parsecolor('rgb222') == u'38;5;118'
    assert parsecolor('rgb200') == u'38;5;226'

    assert parsecolor('gray1') == u'38;5;232'
    assert parsecolor('gray8') == u'38;5;239'


# Generated at 2022-06-13 16:02:34.608195
# Unit test for function hostcolor
def test_hostcolor():
    hostcolor('dark', dict(failures=1, unreachable=0, changed=0, ok=3))
    hostcolor('bright', dict(failures=0, unreachable=1, changed=0, ok=3))



# Generated at 2022-06-13 16:02:44.790385
# Unit test for function hostcolor
def test_hostcolor():
    test_host = "testhost1"
    stats = {
        "ok": 4,
        "changed": 0,
        "unreachable": 0,
        "skipped": 0,
        "failed": 0
    }
    result = hostcolor(test_host, stats)
    assert(result == u"%-37s" % stringc(test_host, C.COLOR_OK))

    stats["changed"] = 1
    result = hostcolor(test_host, stats)
    assert(result == u"%-37s" % stringc(test_host, C.COLOR_CHANGED))

    stats["unreachable"] = 1
    result = hostcolor(test_host, stats)
    assert(result == u"%-37s" % stringc(test_host, C.COLOR_ERROR))

    # Disabling color should

# Generated at 2022-06-13 16:02:55.539418
# Unit test for function stringc
def test_stringc():
    test_cases = (
        (u'foo', u'black'),
        (u'bar', u'blue'),
        (u'baz', u'cyan'),
        (u'foobar', u'green'),
        (u'barfoo', u'magenta'),
        (u'foobaz', u'red'),
        (u'bazfoo', u'white'),
        (u'barbaz', u'yellow'),
        (u'foobarbaz', u'color9'),
        (u'barfoobaz', u'rgb0321'),
        (u'foobarfoobaz', u'gray9'),
    )
    global ANSIBLE_COLOR

# Generated at 2022-06-13 16:03:03.117312
# Unit test for function hostcolor
def test_hostcolor():
    hostcolor(u"127.0.0.1", dict(failures=1), color=True)
    hostcolor(u"127.0.0.1", dict(failures=1), color=False)
    hostcolor(u"127.0.0.1", dict(unreachable=1), color=True)
    hostcolor(u"127.0.0.1", dict(unreachable=1), color=False)
    hostcolor(u"127.0.0.1", dict(changed=1), color=True)
    hostcolor(u"127.0.0.1", dict(changed=1), color=False)
    hostcolor(u"127.0.0.1", dict(), color=True)
    hostcolor(u"127.0.0.1", dict(), color=False)



# Generated at 2022-06-13 16:03:13.974027
# Unit test for function stringc
def test_stringc():
    assert stringc("this is red", "RED") == u'\033[31mthis is red\033[0m'
    assert stringc("this is red", "RED", wrap_nonvisible_chars=True) == u'\001\033[31m\002this is red\001\033[0m\002'
    assert stringc("this is green", "GREEN") == u'\033[32mthis is green\033[0m'
    assert stringc("this is blue", "blue") == u'\033[34mthis is blue\033[0m'
    assert stringc("this is red", "rgb255000") == u'\033[31mthis is red\033[0m'

# Generated at 2022-06-13 16:03:20.803357
# Unit test for function stringc
def test_stringc():
    print(stringc("Hello world", "black"))
    print(stringc("Hello world", "red"))
    print(stringc("Hello world", "green"))
    print(stringc("Hello world", "yellow"))
    print(stringc("Hello world", "blue"))
    print(stringc("Hello world", "magenta"))
    print(stringc("Hello world", "cyan"))
    print(stringc("Hello world", "white"))

# --- end of "pretty"



# Generated at 2022-06-13 16:03:28.553714
# Unit test for function parsecolor
def test_parsecolor():
    # test ansible colors
    for name, code in list(C.COLOR_CODES.items()):
        assert parsecolor(name) == code

    # test 256 colors
    for i in range(256):
        assert parsecolor('color%d' % i) == '38;5;%d' % i

    for i in range(0, 6):
        for j in range(0, 6):
            for k in range(0, 6):
                assert parsecolor(u'rgb%d%d%d' % (i, j, k)) ==\
                    u'38;5;%d' % (16 + 36 * i + 6 * j + k)


# Generated at 2022-06-13 16:03:31.636778
# Unit test for function stringc
def test_stringc():
    assert u"\033[1;31mfoo\033[0m" == stringc("foo", "RED", wrap_nonvisible_chars=True)



# Generated at 2022-06-13 16:03:42.116778
# Unit test for function stringc
def test_stringc():
    """Tests for function stringc."""

    from ansible.compat.tests import unittest

    class MyTest(unittest.TestCase):
        def test_stringc(self):
            global ANSIBLE_COLOR
            prev_color = ANSIBLE_COLOR
            try:
                ANSIBLE_COLOR = True
                self.assertEqual(stringc("hello", "blue"), u"\033[34mhello\033[0m")
                self.assertEqual(stringc("couleur", "rgb255200100"), u"\033[38;5;202mcouleur\033[0m")
                ANSIBLE_COLOR = False
                self.assertEqual(stringc("hello", "blue"), "hello")
            finally:
                ANSIBLE_COLOR = prev_color

    unitt

# Generated at 2022-06-13 16:03:51.673639
# Unit test for function stringc
def test_stringc():
    assert stringc('These are some words.', 'black') == (
        '\033[30mThese are some words.\033[0m')
    assert stringc('These are some words.', 'red') == (
        '\033[31mThese are some words.\033[0m')
    assert stringc('These are some words.', 'green') == (
        '\033[32mThese are some words.\033[0m')
    assert stringc('These are some words.', 'yellow') == (
        '\033[33mThese are some words.\033[0m')
    assert stringc('These are some words.', 'blue') == (
        '\033[34mThese are some words.\033[0m')

# Generated at 2022-06-13 16:04:01.326152
# Unit test for function colorize
def test_colorize():
    if ANSIBLE_COLOR and color is not None:
        for c in C.COLOR_CODES.keys():
            print("colorize('TEST', 42, '" + c + "') = " + colorize("TEST", 42, c))
    else:
        print("No colors supported on this terminal")

# end "pretty"

# Generated at 2022-06-13 16:04:10.427467
# Unit test for function stringc
def test_stringc():
    print()
    print(stringc("This is black", "black"))
    print(stringc("This is red", "red"))
    print(stringc("This is green", "green"))
    print(stringc("This is yellow", "yellow"))
    print(stringc("This is blue", "blue"))
    print(stringc("This is magenta", "magenta"))
    print(stringc("This is cyan", "cyan"))
    print(stringc("This is white", "white"))
    print(stringc("This is BRIGHTBLACK", "BRIGHTBLACK"))
    print(stringc("This is BRIGHTRED", "BRIGHTRED"))
    print(stringc("This is BRIGHTGREEN", "BRIGHTGREEN"))
    print(stringc("This is BRIGHTYELLOW", "BRIGHTYELLOW"))


# Generated at 2022-06-13 16:04:18.078391
# Unit test for function colorize
def test_colorize():
    for c in ('blue', 'lightblue', 'cyan',
              'green', 'lightgreen',
              'magenta', 'lightmagenta', 'purple',
              'red', 'lightred',
              'yellow', 'lightyellow',
              'dark gray', 'light gray'):
        print(colorize('>', 5, c))
    print(colorize('>', 0, 'blue'))

if __name__ == '__main__':
    test_colorize()

# Generated at 2022-06-13 16:04:25.027351
# Unit test for function colorize
def test_colorize():
    assert colorize('foo', 0, 'green') == u'foo=0   '
    assert colorize('foo', 0, None) == u'foo=0   '
    assert colorize('foo', 123, 'green') == u'foo=123 '
    assert colorize('foo', 123, None) == u'foo=123 '
    assert stringc('foo', 'green') == u'\033[32mfoo\033[0m'
#
# --- end "pretty"

# Generated at 2022-06-13 16:04:31.817167
# Unit test for function hostcolor
def test_hostcolor():
    check = dict(failed=0, ok=0, changed=0, unreachable=0, skipped=0)

# Generated at 2022-06-13 16:04:38.087606
# Unit test for function stringc
def test_stringc():
    assert stringc('foo', 'blue') == u'\033[34mfoo\033[0m'
    assert stringc('foo', 'color123') == u'\033[38;5;123mfoo\033[0m'
    assert stringc('foo', 'rgb25515115') == u'\033[38;5;214mfoo\033[0m'
    assert stringc('foo', 'gray8') == u'\033[38;5;242mfoo\033[0m'
    assert stringc('foo', 'bad name') == u'\033[31mfoo\033[0m'

# Generated at 2022-06-13 16:04:44.104732
# Unit test for function colorize
def test_colorize():
    test_lead = 'test'
    test_num = 0
    test_color = 'cyan'
    test_val = colorize(test_lead, test_num, test_color)
    # If ANSIBLE_NOCOLOR is set, the colored string is returned as a non-colorized string
    assert test_val == "%s=%-4s" % (test_lead, str(test_num))
    assert test_num != 0


# Generated at 2022-06-13 16:04:55.086951
# Unit test for function stringc
def test_stringc():
    class TTY:
        def isatty(self):
            return True
    sys.stdout = TTY()
    # Simple tests
    assert stringc("Test", "blue") == u"\033[34mTest\033[0m"
    assert stringc("Test\nTest2", "blue") == u"\033[34mTest\nTest2\033[0m"

    # Test perserving invisible characters
    prompt_prefix = u"\n\033[0m\033[4m\033[1;32m$ \033[0m\033[1;32m\033[0m"

# Generated at 2022-06-13 16:05:06.879433
# Unit test for function colorize
def test_colorize():
    # Tests with ANSIBLE_COLORS=1
    try:
        import __builtin__ as builtins
    except ImportError:
        import builtins
    global C
    setattr(builtins, '_', lambda x: x)
    setattr(C, 'ANSIBLE_NOCOLOR', 0)
    setattr(C, 'COLOR_CHANGED', 'blue')
    setattr(C, 'COLOR_ERROR', 'red')
    setattr(C, 'COLOR_OK', 'green')
    setattr(C, 'COLOR_SKIPPED', 'cyan')
    setattr(C, 'COLOR_UNREACHABLE', 'red')
    setattr(C, 'COLOR_WARN', 'yellow')

# Generated at 2022-06-13 16:05:13.714095
# Unit test for function stringc
def test_stringc():
    if ANSIBLE_COLOR:
        assert stringc(u"A", u"red", True) == u"\x01\x1b[31m\x02A\x01\x1b[0m\x02"
        assert stringc(u"B", u"blue") == u"\x1b[34mB\x1b[0m"
    else:
        assert stringc(u"C", u"green") == u"C"



# Generated at 2022-06-13 16:05:23.802393
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor("myhost", {'failures': 0, 'changed': 0, 'ok': 1, 'dark': 0, 'skipped': 0, 'unreachable': 0, 'rescued': 0}, False) == "%-26s" % "myhost"


# Generated at 2022-06-13 16:05:29.627106
# Unit test for function hostcolor
def test_hostcolor():
    if ANSIBLE_COLOR:
        stats = dict(changed=1, failures=0, unreachable=0)
        assert hostcolor('host.example.com', stats).endswith(u"host.example.com\033[0m")
        stats = dict(changed=0, failures=0, unreachable=0)
        assert hostcolor('host.example.com', stats).endswith(u"host.example.com\033[0m")
        stats = dict(changed=1, failures=0, unreachable=1)
        assert hostcolor('host.example.com', stats).endswith(u"host.example.com\033[0m")
        stats = dict(changed=0, failures=1, unreachable=0)

# Generated at 2022-06-13 16:05:38.400125
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('test', dict(failures=0, unreachable=0, changed=0)) == 'test                            '
    assert hostcolor('test', dict(failures=1, unreachable=0, changed=0)) == 'test                            '
    assert hostcolor('test', dict(failures=0, unreachable=1, changed=0)) == 'test                            '
    assert hostcolor('test', dict(failures=0, unreachable=0, changed=1)) == 'test                            '
    assert hostcolor('test', dict(failures=1, unreachable=1, changed=1)) == 'test                            '



# Generated at 2022-06-13 16:05:45.342554
# Unit test for function stringc
def test_stringc():
    for color in ('black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'):
        for background in (False, True):
            if background:
                c = 'on_' + color
            else:
                c = color
            print(stringc('abc', c))

    # Test with wrap_nonvisible_chars=True
    res = stringc('abc', 'red', wrap_nonvisible_chars=True)
    assert res == u'\001\033[31m\002abc\001\033[0m\002'
    assert len(res) == 7

if __name__ == '__main__':
    test_stringc()
# --- end "pretty"

# Generated at 2022-06-13 16:05:50.995974
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('localhost', dict(changed=1)) == u'\x1b[0;32mlocalhost          \x1b[0m'
    assert hostcolor('localhost', dict(failures=1)) == u'\x1b[1;31mlocalhost          \x1b[0m'
    assert hostcolor('localhost', dict(unreachable=1)) == u'\x1b[1;31mlocalhost          \x1b[0m'
    assert hostcolor('localhost', dict()) == u'\x1b[0;32mlocalhost          \x1b[0m'



# Generated at 2022-06-13 16:05:56.017020
# Unit test for function stringc
def test_stringc():
    assert(stringc("foo", "black", True) == u"\001\033[30m\002foo\001\033[0m\002")
    assert(stringc("bar", "red", True) == u"\001\033[31m\002bar\001\033[0m\002")
    assert(stringc("baz", "green", True) == u"\001\033[32m\002baz\001\033[0m\002")
    assert(stringc("bax", "yellow", True) == u"\001\033[33m\002bax\001\033[0m\002")
    assert(stringc("bay", "blue", True) == u"\001\033[34m\002bay\001\033[0m\002")

# Generated at 2022-06-13 16:06:05.244194
# Unit test for function stringc

# Generated at 2022-06-13 16:06:11.168503
# Unit test for function hostcolor

# Generated at 2022-06-13 16:06:14.337900
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor("localhost", {}) == "%-26s" % "localhost"
    assert hostcolor("localhost", {'failures':99}) == "%-37s" % stringc("localhost", C.COLOR_ERROR)
    assert hostcolor("localhost", {'changed':99}) == "%-37s" % stringc("localhost", C.COLOR_CHANGED)
    assert hostcolor("localhost", {'ok':99}) == "%-37s" % stringc("localhost", C.COLOR_OK)

# Generated at 2022-06-13 16:06:25.537365
# Unit test for function hostcolor
def test_hostcolor():
    host, stats, color = "192.168.1.1", dict(failures=0, unreachable=0, changed=1), True
    assert hostcolor(host, stats, color) == u"192.168.1.1                   ", "test 1 failed"
    host, stats, color = "192.168.1.2", dict(failures=1, unreachable=0, changed=0), True
    assert hostcolor(host, stats, color) == u"192.168.1.2                   ", "test 2 failed"
    host, stats, color = "192.168.1.3", dict(failures=0, unreachable=0, changed=0), True
    assert hostcolor(host, stats, color) == u"192.168.1.3                   ", "test 3 failed"

# Generated at 2022-06-13 16:06:44.998238
# Unit test for function stringc
def test_stringc():
    """Unit tests for function stringc."""

    assert stringc('foo', 'pink') == '\033[95mfoo\033[0m'



# Generated at 2022-06-13 16:06:55.691067
# Unit test for function stringc
def test_stringc():
    """ Provide example function use from the command line. """
    print(stringc("this is a test", "black", True))
    print(stringc("this is a test", "blue", True))
    print(stringc("this is a test", "green", True))
    print(stringc("this is a test", "cyan", True))
    print(stringc("this is a test", "red", True))
    print(stringc("this is a test", "purple", True))
    print(stringc("this is a test", "orange", True))
    print(stringc("this is a test", "lightgray", True))
    print(stringc("this is a test", "darkgray", True))
    print(stringc("this is a test", "lightblue", True))

# Generated at 2022-06-13 16:07:03.741075
# Unit test for function stringc

# Generated at 2022-06-13 16:07:13.338830
# Unit test for function parsecolor
def test_parsecolor():
    def assertColor(color, ansi_color_code):
        assert (parsecolor(color) == ansi_color_code)
    assertColor('red', '31')
    assertColor('boldred', '31;1')
    assertColor('blue', '34')
    assertColor('boldyellow', '33;1')
    assertColor('on_grey', '1;30')
    assertColor('on_red', '1;41')
    assertColor('on_green', '1;42')
    assertColor('on_yellow', '1;43')
    assertColor('on_cyan', '1;46')
    assertColor('black', '30')
    assertColor('white', '37')
    assertColor('boldblack', '30;1')
    assertColor('boldwhite', '37;1')
    assertColor

# Generated at 2022-06-13 16:07:20.131580
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('foo', dict(ok=1), C.COLOR_OK) == u"foo"
    assert hostcolor('foo', dict(ok=1, changed=1), C.COLOR_CHANGED) == u"foo"
    assert hostcolor('foo', dict(failed=1, unreachable=1), C.COLOR_ERROR) == u"foo"
    assert u"\001\033[35m\002foo\001\033[0m\002" == hostcolor('foo', dict(ok=1), C.COLOR_OK, wrap_nonvisible_chars=True)

# --- end "pretty"

__all__ = ['stringc', 'hostcolor', 'colorize']

# Generated at 2022-06-13 16:07:27.699816
# Unit test for function stringc
def test_stringc():
    assert stringc('foo', 'blue') == '\x1b[34mfoo\x1b[0m'
    assert stringc('foo', 'white') == '\x1b[0mfoo\x1b[0m'
    assert stringc('foo', 'gray10') == '\x1b[38;5;12mfoo\x1b[0m'
    assert stringc('foo', 'color1') == '\x1b[38;5;1mfoo\x1b[0m'
    assert stringc('foo', 'color2') == '\x1b[38;5;2mfoo\x1b[0m'
    assert stringc('foo', 'color3') == '\x1b[38;5;3mfoo\x1b[0m'

# Generated at 2022-06-13 16:07:35.142924
# Unit test for function stringc
def test_stringc():
    test_passed = True

# Generated at 2022-06-13 16:07:39.137425
# Unit test for function stringc
def test_stringc():
    for color in C.COLOR_CODES.keys():
        text = 'text in %s!!!' % color
        ct = stringc(text, color)
        print('Testing color: %s' % color)
        print('text: %s' % text)
        print('colored test: %s' % ct)
        print('')

# Generated at 2022-06-13 16:07:41.899220
# Unit test for function colorize
def test_colorize():
    print(colorize('foo', 42, 'blue'))
    print(colorize('foo', 0, 'blue'))
    print(colorize('foo', 42, None))
    print(colorize('foo', 0, None))

if __name__ == '__main__':
    test_colorize()



# Generated at 2022-06-13 16:07:50.127710
# Unit test for function hostcolor
def test_hostcolor():
    hosts = [
        'a', 'b', 'c',
    ]
    stats = [
        dict(failures=0, unreachable=0, changed=0),
        dict(failures=0, unreachable=1, changed=0),
        dict(failures=1, unreachable=0, changed=0),
    ]

    i = 0
    for h in hosts:
        print(hostcolor(h, stats[i]))
        i += 1



# Generated at 2022-06-13 16:08:09.616206
# Unit test for function hostcolor
def test_hostcolor():
    host_name = "test_host"
    stats = {'failures': 0, 'unreachable': 0, 'changed': 0}
    print(hostcolor(host_name, stats))

#Unit test for function stringc

# Generated at 2022-06-13 16:08:19.854039
# Unit test for function hostcolor
def test_hostcolor():
    print(u"Test hostcolor:")
    print(u"Test C.COLOR_OK %s" % hostcolor('test_host_ok', {'ok': 1, 'failures': 0, 'unreachable': 0, 'changed': 0}))
    print(u"Test C.COLOR_ERROR %s" % hostcolor('test_host_error', {'ok': 0, 'failures': 1, 'unreachable': 0, 'changed': 0}))
    print(u"Test C.COLOR_ERROR %s" % hostcolor('test_host_error2', {'ok': 0, 'failures': 0, 'unreachable': 1, 'changed': 0}))

# Generated at 2022-06-13 16:08:29.375033
# Unit test for function stringc
def test_stringc():
    # Exact match
    assert stringc('foo', 'black') == u"\033[30mfoo\033[0m"
    # Case-insensitive match
    assert stringc('foo', 'bLaCk') == u"\033[30mfoo\033[0m"
    # Matching substring
    assert stringc('foo', 'lac') == u"\033[30mfoo\033[0m"
    # Boolean values
    assert stringc('foo', True) == u"\033[30mfoo\033[0m"
    assert stringc('foo', False) == u"foo"
    assert stringc('foo', 'x') == u"foo"
    # Color name -> RGB

# Generated at 2022-06-13 16:08:31.344301
# Unit test for function hostcolor
def test_hostcolor():
    hc = hostcolor('hostname', dict(failures=0, unreachable=0, changed=0))
    assert len(hc) == 37



# Generated at 2022-06-13 16:08:37.494680
# Unit test for function stringc
def test_stringc():
    """Test customized stringc function above."""
    if not ANSIBLE_COLOR:
        return

    def col(n):
        """Color n."""
        return stringc(str(n), n)

    def col16(n):
        """Color 16 + n."""
        return stringc(str(n), 'color%d' % (16 + n))

    def colrgb(r, g, b):
        """rgb."""
        return stringc('rgb', 'rgb%s%s%s' % (r, g, b))

    def colgray(n):
        """gray."""
        return stringc(str(n), 'gray%d' % n)

    print(u"".join([col(n) for n in range(8)]))

# Generated at 2022-06-13 16:08:40.895936
# Unit test for function stringc
def test_stringc():
    ''' basic test for stringc
    '''
    assert stringc("text", "black") == "\033[30mtext\033[0m"



# Generated at 2022-06-13 16:08:48.843459
# Unit test for function hostcolor
def test_hostcolor():
    """ Method to test if the color formatting of hostcolor works correctly """
    assert hostcolor(u"test.example.com", {u'skipped': 1, u'pending': 0, u'ok': 1, u'failures': 0, u'changed': 0, u'unreachable': 0}, True) == u'test.example.com            '
    assert hostcolor(u"test.example.com", {u'skipped': 0, u'pending': 0, u'ok': 0, u'failures': 0, u'changed': 1, u'unreachable': 0}, True) == u'\x1b[0;34mtest.example.com\x1b[0m '

# Generated at 2022-06-13 16:08:59.566606
# Unit test for function stringc

# Generated at 2022-06-13 16:09:06.766451
# Unit test for function stringc
def test_stringc():
    assert stringc("foo_bar", 'red') == u"\033[31mfoo_bar\033[0m"
    assert stringc("foo_bar", 'black') == u"\033[30mfoo_bar\033[0m"
    assert stringc("foo_bar", 'white') == u"\033[37mfoo_bar\033[0m"
    assert stringc("foo_bar", 'green') == u"\033[32mfoo_bar\033[0m"
    assert stringc("foo_bar", 'yellow') == u"\033[33mfoo_bar\033[0m"
    assert stringc("foo_bar", 'magenta') == u"\033[35mfoo_bar\033[0m"

# Generated at 2022-06-13 16:09:16.688293
# Unit test for function stringc
def test_stringc():
    assert parsecolor('red') == '31'
    assert parsecolor('0;31') == '31'
    assert stringc('abc', 'red') == '\033[31mabc\033[0m'
    assert stringc('abc', '0;31') == '\033[31mabc\033[0m'
    assert stringc('abc', 'rgb255') == '\033[38;5;9mabc\033[0m'
    assert stringc('abc', 'rgb000') == '\033[38;5;16mabc\033[0m'
    assert stringc('abc', 'rgb255255255') == '\033[38;5;15mabc\033[0m'