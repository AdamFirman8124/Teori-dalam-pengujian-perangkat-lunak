

# Generated at 2022-06-13 15:59:41.713104
# Unit test for function hostcolor
def test_hostcolor():
    host = "verylongmyboxname"
    stats = {
        'changed': 1,
        'failures': 2,
        'ok': 3,
        'skipped': 4,
        'unreachable': 5,
    }
    color = True
    result = hostcolor(host, stats, color)
    assert result == u"\033[31;01mverylongmyboxname      \033[0m"

    stats = {
        'changed': 0,
        'failures': 0,
        'ok': 3,
        'skipped': 0,
        'unreachable': 0,
    }
    result = hostcolor(host, stats, color)
    assert result == u"\033[32;01mverylongmyboxname      \033[0m"


# Generated at 2022-06-13 15:59:50.764828
# Unit test for function stringc
def test_stringc():
    assert stringc(stringc('hello', 'blue'), 'red') \
        == u'\033[31m\033[34mhello\033[0m\033[0m'
    assert stringc(stringc('hello', 'rgb025'), 'rgb050') \
        == u'\033[38;5;11m\033[38;5;40mhello\033[0m\033[0m'
    assert stringc(stringc('hello', 'gray3'), 'blue') \
        == u'\033[34m\033[38;5;235mhello\033[0m\033[0m'


# Generated at 2022-06-13 16:00:01.497123
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor("red") == u'31'
    assert parsecolor("white") == u'97'
    assert parsecolor("color1") == u'38;5;1'
    assert parsecolor("color255") == u'38;5;255'
    assert parsecolor("rgb123") == u'38;5;23'
    assert parsecolor("rgb321") == u'38;5;74'
    assert parsecolor("rgb213") == u'38;5;58'
    assert parsecolor("rgb111") == u'38;5;16'
    assert parsecolor("gray0") == u'38;5;232'
    assert parsecolor("gray8") == u'38;5;240'



# Generated at 2022-06-13 16:00:08.403734
# Unit test for function colorize
def test_colorize():
    # ANSIBLE_COLOR==0, color=None
    assert colorize('ok', 0, None) == 'ok=0   '
    assert colorize('changed', 0, None) == 'changed=0   '
    assert colorize('unreachable', 0, None) == 'unreachable=0   '
    assert colorize('failed', 0, None) == 'failed=0  '

    # ANSIBLE_COLOR==1, color=None
    assert colorize('ok', 0, None) == 'ok=0   '
    assert colorize('changed', 0, None) == 'changed=0   '
    assert colorize('unreachable', 0, None) == 'unreachable=0   '
    assert colorize('failed', 0, None) == 'failed=0  '

    # ANSIBLE_COLOR==0, color

# Generated at 2022-06-13 16:00:15.142196
# Unit test for function stringc
def test_stringc():
    from ansible.utils.py3compat import PY3
    if PY3:
        # no tests possible since the output contains unichr() which breaks in
        # python 3
        return None
    else:
        assert stringc('foo', 'blue') == u'\033[34mfoo\033[0m'
        assert stringc('foo', 'red') == u'\033[31mfoo\033[0m'
        assert stringc('foo', 'green') == u'\033[32mfoo\033[0m'



# Generated at 2022-06-13 16:00:24.254215
# Unit test for function hostcolor
def test_hostcolor():
    host_status = {
        'darkriftx.de': {'failures': 1, 'changed': 0, 'ok': 4, 'skipped': 0, 'unreachable': 0},
        'ix.de': {'failures': 0, 'changed': 1, 'ok': 3, 'skipped': 1, 'unreachable': 0},
        'drache.de': {'failures': 0, 'changed': 0, 'ok': 5, 'skipped': 0, 'unreachable': 1},
    }

    ANSIBLE_COLOR = False
    assert u'%-26s' % 'darkriftx.de' == hostcolor('darkriftx.de', host_status['darkriftx.de'])

# Generated at 2022-06-13 16:00:32.885001
# Unit test for function hostcolor
def test_hostcolor():
    try:
        from nose import tools as nt
    except ImportError:
        print('1..0 # SKIP: nose not installed')
        return

    nt.eq_(hostcolor('example-host', {'failures': 0, 'unreachable': 0}),
            'example-host')
    nt.eq_(hostcolor('example-host', {'failures': 1, 'unreachable': 0}),
            '\033[31;01mexample-host\033[0m')
    nt.eq_(hostcolor('example-host', {'failures': 0, 'unreachable': 1}),
            '\033[31;01mexample-host\033[0m')

# Generated at 2022-06-13 16:00:43.132874
# Unit test for function colorize
def test_colorize():
    """ Unit test for function colorize """

# Generated at 2022-06-13 16:00:48.861013
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor(u"default") == u"39"
    assert parsecolor(u"red") == u"31"
    assert parsecolor(u"blue") == u"34"
    assert parsecolor(u"yellow") == u"33"
    assert parsecolor(u"green") == u"32"
    assert parsecolor(u"cyan") == u"36"
    assert parsecolor(u"magenta") == u"35"
    assert parsecolor(u"black") == u"30"
    assert parsecolor(u"dark gray") == u"90"
    assert parsecolor(u"light gray") == u"37"
    assert parsecolor(u"white") == u"97"

# Generated at 2022-06-13 16:00:59.309198
# Unit test for function hostcolor
def test_hostcolor():
    fake_stats = dict(changed=0, failures=1, unreachable=1)
    assert hostcolor('bad.example.com', fake_stats) == 'bad.example.com               '
    assert hostcolor('bad.example.com', fake_stats, False) == 'bad.example.com               '

    fake_stats = dict(changed=1, failures=0, unreachable=0)
    assert hostcolor('changed.example.com', fake_stats) == 'changed.example.com               '

    fake_stats = dict(changed=0, failures=0, unreachable=0)
    assert hostcolor('good.example.com', fake_stats) == 'good.example.com               '



# Generated at 2022-06-13 16:01:10.812811
# Unit test for function stringc
def test_stringc():
    assert (stringc(u"foo", u"blue") == u"\033[34mfoo\033[0m")
    assert (stringc(u"foo", u"rgb255255255", wrap_nonvisible_chars=True)
            == u"\001\033[97m\002foo\001\033[0m\002")


# --- end "pretty"

# ansible-specific color output wrappers

# Generated at 2022-06-13 16:01:18.420178
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor("example.com", dict(failed=0, changed=0, ok=1, skipped=0, unreachable=0)) == u"example.com               "
    assert hostcolor("example.com", dict(failed=1, changed=0, ok=0, skipped=0, unreachable=0)) == u"example.com               "
    assert hostcolor("example.com", dict(failed=0, changed=1, ok=0, skipped=0, unreachable=0)) == u"example.com               "
    assert hostcolor("example.com", dict(failed=0, changed=0, ok=0, skipped=0, unreachable=1)) == u"example.com               "

# Generated at 2022-06-13 16:01:29.024485
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('localhost', dict(changed=0, failures=0, unreachable=0, ok=1)) == u'%-26s' % 'localhost'
    assert hostcolor('localhost', dict(changed=1, failures=0, unreachable=0, ok=1)) == u'%-37s' % u'\u001b[0;32mlocalhost\u001b[0m'
    assert hostcolor('localhost', dict(changed=0, failures=1, unreachable=0, ok=1)) == u'%-37s' % u'\u001b[0;31mlocalhost\u001b[0m'

# Generated at 2022-06-13 16:01:32.081370
# Unit test for function colorize
def test_colorize():
    assert colorize("foo", 0, None) == "foo=0   "
    assert colorize("foo", 0, C.COLOR_ERROR) == "foo=0   "
    assert colorize("foo", 10, C.COLOR_ERROR) == "foo=10  "


# Generated at 2022-06-13 16:01:35.077168
# Unit test for function stringc
def test_stringc():
    print(stringc("this is the string to test", "red"))
    print(stringc("this is the string to test", "green"))
    print(stringc("this is the string to test", "yellow"))
    print(stringc("this is the string to test", "blue"))
    print(stringc("this is the string to test", "magenta"))



# Generated at 2022-06-13 16:01:40.331351
# Unit test for function hostcolor
def test_hostcolor():
    teststats = {'changed': 0, 'failures': 0, 'skipped': 0, 'ok': 1, 'unreachable': 0}
    assert hostcolor('host1', teststats, False) == 'host1 '
    assert hostcolor('host2', teststats, True) == 'host2               '



# Generated at 2022-06-13 16:01:49.478597
# Unit test for function stringc
def test_stringc():
    # error
    text = stringc("ERROR!", "red", wrap_nonvisible_chars=False)
    assert text == u"\033[41mERROR!\033[0m"

    # success
    text = stringc("SUCCESS!", "green")
    assert text == u"\033[32mSUCCESS!\033[0m"

    # non-ascii
    text = stringc(u"\u039A\u03A9", "green", wrap_nonvisible_chars=True)
    assert text == u"\001\033[32m\002\u039A\u03A9\001\033[0m\002"

    # escape sequences
    text = stringc("\033[41mERROR!\033[0m", "green")

# Generated at 2022-06-13 16:02:00.168774
# Unit test for function hostcolor
def test_hostcolor():
    stats_ok = dict(ok=1)
    stats_fail = dict(failures=1)
    stats_unreachable = dict(unreachable=1)
    stats_changed = dict(changed=1)
    stats_mixed = dict(ok=1, failures=1, unreachable=1, changed=1)
    assert hostcolor(u'fake1', stats_ok) == u'fake1                        '
    assert hostcolor(u'fake2', stats_ok, color=False) == u'fake2                  '
    assert hostcolor(u'fake3', stats_fail) == u'\x1b[31mfake3                    \x1b[0m'

# Generated at 2022-06-13 16:02:05.103306
# Unit test for function colorize
def test_colorize():
    # null cases
    assert colorize('ok', 0, None) == u'ok=0   '
    assert colorize('changed', 0, None) == u'changed=0   '
    assert colorize('unreachable', 0, None) == u'unreachable=0   '
    assert colorize('failed', 0, None) == u'failed=0   '
    # non-null cases
    assert colorize('ok', 1, None) == u'ok=1   '
    assert colorize('changed', 1, None) == u'changed=1   '
    assert colorize('unreachable', 1, None) == u'unreachable=1   '
    assert colorize('failed', 1, None) == u'failed=1   '

# --- end "pretty"



# Generated at 2022-06-13 16:02:09.629548
# Unit test for function colorize
def test_colorize():
    # Call function with various arguments
    # Compare returned value with the expected value
    # If the returned value is the same as the expected value, return True
    if colorize('foo', 10, 'red') == u"foo=10  ":
        return True
    else:
        return False

# Generated at 2022-06-13 16:02:22.946461
# Unit test for function stringc
def test_stringc():
    assert stringc("test", "undefined") == "test"
    assert stringc("test", "blue") == "\033[01;34mtest\033[0m"
    assert stringc("test", "on_blue") == "\033[44mtest\033[0m"
    assert stringc("test", "white", True).endswith("\002")

# Define color mappings
color_map = {
    'debug': 'dark gray',
    'verbose': 'cyan',
    'info': 'green',
    'warn': 'yellow',
    'warning': 'yellow',
    'error': 'red',
    'critical': 'bold red',
}

# --- end "pretty"

# Generated at 2022-06-13 16:02:29.365851
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('SOMEHOST', dict(failures=1, unreachable=1, changed=2)) == '\x1b[91mSOMEHOST              \x1b[0m'
    assert hostcolor('SOMEHOST', dict(failures=2, unreachable=0, changed=0)) == '\x1b[91mSOMEHOST              \x1b[0m'
    assert hostcolor('SOMEHOST', dict(failures=0, unreachable=2, changed=0)) == '\x1b[91mSOMEHOST              \x1b[0m'
    assert hostcolor('SOMEHOST', dict(failures=0, unreachable=0, changed=2)) == '\x1b[93mSOMEHOST              \x1b[0m'
    assert host

# Generated at 2022-06-13 16:02:41.119284
# Unit test for function colorize
def test_colorize():

    print(u'Test colorize() function')
    good = u'good'
    bad = u'bad'

    for t in [0, 1, 2, 3]:
        for c in [u'blue', u'green', u'cyan', u'red', u'black', u'yellow', u'magenta', u'white']:
            msg = u'{0} {1:<4} {2}'.format(colorize(u'ok', good, c), colorize(u'changed', good, c), colorize(u'failed', good, c))
            print(msg)
            msg = u'{0} {1:<4} {2}'.format(colorize(u'ok', bad, c), colorize(u'changed', bad, c), colorize(u'failed', bad, c))
            print

# Generated at 2022-06-13 16:02:46.511980
# Unit test for function hostcolor
def test_hostcolor():
    if ANSIBLE_COLOR:
        # ok
        assert hostcolor('localhost', dict(failures=0, unreachable=0, changed=0)) == u"%-37s" % stringc('localhost', C.COLOR_OK)
        # changed
        assert hostcolor('localhost', dict(failures=0, unreachable=0, changed=1)) == u"%-37s" % stringc('localhost', C.COLOR_CHANGED)
        # error
        assert hostcolor('localhost', dict(failures=1, unreachable=0, changed=0)) == u"%-37s" % stringc('localhost', C.COLOR_ERROR)
        # unreachable
        assert hostcolor('localhost', dict(failures=0, unreachable=1, changed=0)) == u"%-37s" % stringc('localhost', C.COLOR_ERROR)

# Generated at 2022-06-13 16:02:53.927029
# Unit test for function colorize
def test_colorize():
    """
    colorize: lead, num, color
    """
    tests = (('foo', 0, 'green'),
             ('foo', 1, 'green'),
             ('foo', -1, 'green'),
             ('foo', 1, None),
             ('bar', 0, 'red'),
             ('bar', 1, 'magenta'),
             ('bar', 2, 'yellow'),
             ('bar', 3, 'white'))

    for (lead, num, color) in tests:
        yield colorize, lead, num, color



# Generated at 2022-06-13 16:03:04.137839
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor(u'foo', dict(failures=0, unreachable=0, changed=0)) == u'foo                          '
    assert hostcolor(u'foo', dict(failures=1, unreachable=0, changed=0)) == u'\x1b[31mfoo                         \x1b[0m'
    assert hostcolor(u'foo', dict(failures=0, unreachable=1, changed=0)) == u'\x1b[31mfoo                         \x1b[0m'
    assert hostcolor(u'foo', dict(failures=0, unreachable=0, changed=1)) == u'\x1b[33mfoo                         \x1b[0m'
    # Test that colorization is disabled when ANSIBLE_NOCOLOR is True
    C.ANSIBLE_NOC

# Generated at 2022-06-13 16:03:14.353428
# Unit test for function stringc
def test_stringc():
    """ test stringc """

    assert stringc("foo", "green") == u'\033[32mfoo\033[0m'
    assert stringc("foo\nbar", "green") == u'\033[32mfoo\033[0m\n\033[32mbar\033[0m'
    assert stringc("foo%sbar" % u'\n', "green") == u'\033[32mfoo\033[0m\n\033[32mbar\033[0m'
    assert stringc("" + u'\n', "green") == u''
    assert stringc("foo", "color236") == u'\033[38;5;236mfoo\033[0m'

# Generated at 2022-06-13 16:03:24.284787
# Unit test for function hostcolor
def test_hostcolor():
    if not C.DEFAULT_HOST_LIST:
        return

    from ansible.runner import Runner
    from ansible import callbacks
    stats = callbacks.AggregateStats()
    runner = Runner(
        pattern=C.DEFAULT_HOST_LIST,
        module_name='ping',
        module_args='',
        forks=10,
        callbacks=callbacks.PlaybookCallbacks(verbose=utils.VERBOSITY),
        stats=stats,
    )

    results = runner.run()

    for (host, value) in results['contacted'].iteritems():
        print(hostcolor(host, value))
    for (host, value) in results['dark'].iteritems():
        print(hostcolor(host, value))



# Generated at 2022-06-13 16:03:28.964716
# Unit test for function hostcolor

# Generated at 2022-06-13 16:03:40.412278
# Unit test for function stringc
def test_stringc():
    assert stringc('pwnd', 'red') == u'\033[31mpwnd\033[0m'
    assert stringc('pwnd', 'blue') == u'\033[34mpwnd\033[0m'
    assert stringc('pwnd', 'on_red') == u'\033[41mpwnd\033[0m'
    assert stringc('pwnd', 'on_blue') == u'\033[44mpwnd\033[0m'
    assert stringc('pwnd', 'blue', wrap_nonvisible_chars=True) == u'\001\033[34m\002pwnd\001\033[0m\002'

# Generated at 2022-06-13 16:03:54.589616
# Unit test for function colorize
def test_colorize():
    if not ANSIBLE_COLOR:
        return
    # These two lines and the `\001` and `\002` characters in the fmt string
    # in stringc() are used to test if we use the non-visible characters
    # wrapping. If we use them, then we can find them in the output.
    # If not, then we print the prompt normally but the wrapped chars will be
    # visible.
    non_visible_chars_wrap_start = u"\001\033[38;5;204m\002"
    non_visible_chars_wrap_end = u"\001\033[0m\002"
    fmt = u"\033[38;5;%sm%s\033[0m"

    assert colorize("ok", 0, "green") == "ok=0"

# Generated at 2022-06-13 16:04:02.120592
# Unit test for function stringc
def test_stringc():
    """
    >>> stringc("hello", "blue")
    u'\\033[34mhello\\033[0m'
    >>> print(stringc("hello", "blue"))
    hello
    >>> print(stringc("hello", "blue", wrap_nonvisible_chars=True))
    \x01\x1b[34m\x02hello\x01\x1b[0m\x02
    """
    pass

# --- end of "pretty"



# Generated at 2022-06-13 16:04:06.806006
# Unit test for function hostcolor
def test_hostcolor():
    stats = dict(ok=0,changed=0,dark=0,failures=0,skipped=0,unreachable=0)

    assert hostcolor(u"dark", stats) == u'dark                 '
    assert hostcolor(u"dark", stats, False) == u'dark                 '

    stats['failures'] = 1
    assert '\033[' in hostcolor(u"dark", stats)

    stats['failures'] = 0
    stats['changed'] = 1
    assert '\033[' in hostcolor(u"dark", stats)

    stats['changed'] = 0
    assert '\033[' in hostcolor(u"dark", stats)

# end "pretty" ---

if __name__ == '__main__':
    print('ANSIBLE_COLOR: %s' % ANSIBLE_COLOR)

# Generated at 2022-06-13 16:04:18.078942
# Unit test for function stringc
def test_stringc():
    print(u"Testing stringc")

    def _test(input, color, expected_output, wrap_nonvisible=False):
        actual_output = stringc(input, color,
                                wrap_nonvisible_chars=wrap_nonvisible)
        assert actual_output == expected_output

    if ANSIBLE_COLOR:
        _test(u"stringc testing", u"green", u"\033[32mstringc testing\033[0m")
        _test(u"stringc testing\nmultiline", u"blue", u"\033[34mstringc testing\nmultiline\033[0m")
        _test(u"\u001b[32mstringc testing", u"green", u"\033[32m\u001b[32mstringc testing\033[0m")
        _test

# Generated at 2022-06-13 16:04:20.880502
# Unit test for function colorize
def test_colorize():
    for n in range(0, 20):
        print (colorize(u"test:", n, u"blue"))

# --- end "pretty"

# Generated at 2022-06-13 16:04:31.112797
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('host.example.com', dict(failures=0, unreachable=0, changed=0)) == u"host.example.com               "
    assert isinstance(hostcolor('host.example.com', dict(failures=0, unreachable=0, changed=0), color=False), unicode)
    assert hostcolor('host.example.com', dict(failures=0, unreachable=0, changed=1)) == u"host.example.com               "
    assert hostcolor('host.example.com', dict(failures=0, unreachable=1, changed=0)) == u"host.example.com               "
    assert hostcolor('host.example.com', dict(failures=1, unreachable=0, changed=0)) == u"host.example.com               "



# Generated at 2022-06-13 16:04:37.880364
# Unit test for function stringc
def test_stringc():
    assert stringc('test', 'green') == u"\033[32mtest\033[0m"
    assert stringc('test', 'red') == u"\033[31mtest\033[0m"
    assert stringc('test', 'rgb333') == u"\033[38;5;114mtest\033[0m"
    assert stringc('test', 'rgb123') == u"\033[38;5;51mtest\033[0m"
    assert stringc('test', 'rgb222') == u"\033[38;5;60mtest\033[0m"
    assert stringc('test', 'rgb321') == u"\033[38;5;94mtest\033[0m"

# Generated at 2022-06-13 16:04:39.948405
# Unit test for function stringc
def test_stringc():
    assert '\x1b[1;33mfoo\x1b[0m' == stringc('foo', 'YELLOW')



# Generated at 2022-06-13 16:04:42.827051
# Unit test for function hostcolor
def test_hostcolor():
    """
    hostcolor: no color
    """
    assert hostcolor(u"foobar.example.org", dict(failures=1, unreachable=0, changed=0)) == u"foobar.example.org          "



# Generated at 2022-06-13 16:04:53.744842
# Unit test for function hostcolor
def test_hostcolor():
    from ansible.utils.color import hostcolor

    assert hostcolor('web01', {'ok': 1}) == 'web01                           '
    assert hostcolor('web01', {'ok': 1}, False) == 'web01                     '
    assert hostcolor('web01', {'failures': 1}) == u"web01                       \033[91m\033[1m\033[0m"
    assert hostcolor('web01', {'output_lines': 1}) == u"web01                       \033[93m\033[1m\033[0m"
    assert hostcolor('web01', {'skipped': 1}) == u"web01                       \033[0m\033[1m\033[0m"

# --- end "pretty"



# Generated at 2022-06-13 16:05:06.257882
# Unit test for function stringc
def test_stringc():
    # Failing cases
    assert stringc('string', 'not a valid color') == 'string'
    assert stringc('string', 'color256') == 'string'
    assert stringc('string', 'rgb57') == 'string'
    assert stringc('string', 'not a valid color') == 'string'

    # Success cases
    assert stringc('string', 'red') == u'\x1b[31mstring\x1b[0m'
    assert stringc('string', 'color1') == u'\x1b[38;5;1mstring\x1b[0m'
    assert stringc('string', 'rgb100') == u'\x1b[38;5;100mstring\x1b[0m'



# Generated at 2022-06-13 16:05:09.592886
# Unit test for function stringc
def test_stringc():
    """
    >>> stringc("hello", "yellow")
    u'\\x1b[33mhello\\x1b[0m'
    >>> stringc("hello", "white")
    'hello'
    """



# Generated at 2022-06-13 16:05:16.638070
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('localhost', dict(changed=0, unreachable=0, failures=0), False) == "localhost                "
    assert hostcolor('localhost', dict(changed=0, unreachable=0, failures=0), True) == "localhost                "
    assert hostcolor('localhost', dict(changed=0, unreachable=1, failures=0), True) == "\x1b[31m%-37s\x1b[0m" % 'localhost'
    assert hostcolor('localhost', dict(changed=1, unreachable=0, failures=0), True) == "\x1b[33m%-37s\x1b[0m" % 'localhost'



# Generated at 2022-06-13 16:05:23.740011
# Unit test for function stringc
def test_stringc():
    """Sample test for function stringc."""
    for name, code in C.COLOR_CODES.items():
        print(u"%s - %s(%s) = '%s'" % (stringc(u'This is code %s' % name, code), code, name, stringc(code, name)))


# --- end "pretty"

__all__ = ['stringc', 'hostcolor', 'test_stringc', 'ANSIBLE_COLOR']

# Generated at 2022-06-13 16:05:29.346760
# Unit test for function hostcolor
def test_hostcolor():
    print(hostcolor('hostname', {'changed': 0, 'failures': 0, 'ok': 1, 'skipped': 0, 'unreachable': 0}))
    print(hostcolor('hostname', {'changed': 1, 'failures': 0, 'ok': 0, 'skipped': 0, 'unreachable': 0}))
    print(hostcolor('hostname', {'changed': 0, 'failures': 1, 'ok': 0, 'skipped': 0, 'unreachable': 0}))

# Generated at 2022-06-13 16:05:39.909464
# Unit test for function stringc
def test_stringc():
    try:
        import curses
    except ImportError:
        sys.stderr.write("curses library not found")
        return
    if curses.tigetnum('colors') < 0:
        sys.stderr.write("no color available")
        return
    sys.stderr.write("%s\n" % stringc("1 normal, ", "purple", wrap_nonvisible_chars=True))
    sys.stderr.write("%s\n" % stringc("2 bright, ", "bright purple", wrap_nonvisible_chars=True))
    sys.stderr.write("%s\n" % stringc("3 bg_normal, ", "on_yellow", wrap_nonvisible_chars=True))

# Generated at 2022-06-13 16:05:43.299050
# Unit test for function hostcolor
def test_hostcolor():
    host = 'testhost'
    stats = {
        'changed': 0,
        'failures': 0,
        'ok': 5,
        'skipped': 0,
        'unreachable': 0}
    if hostcolor(host, stats) != u"%-26s":
        return 1
    return 0



# Generated at 2022-06-13 16:05:51.977306
# Unit test for function colorize
def test_colorize():
    if not ANSIBLE_COLOR:
        return
    from ansible.utils.unicode import to_bytes
    for i in range(0, 200):
        print(to_bytes(colorize(u'VAR', i, u'blue')), end=u' ')
    print()
    for i in range(0, 200):
        print(to_bytes(colorize(u'VAR', i, u'green')), end=u' ')
    print()
    for i in range(0, 200):
        print(to_bytes(colorize(u'VAR', i, u'red')), end=u' ')
    print()
    for i in range(0, 200):
        print(to_bytes(colorize(u'VAR', i, u'cyan')), end=u' ')

# Generated at 2022-06-13 16:06:03.018984
# Unit test for function colorize

# Generated at 2022-06-13 16:06:14.735985
# Unit test for function colorize
def test_colorize():
    lead = 'test'
    num = 42
    color = 'dummy'
    colored_result = colorize(lead, num, color)
    assert colored_result == 'test=42' or colored_result == 'test=42', 'unexpected colorize() result'

    # Passing no color should make it return the same thing whether or not we
    # have color turned on
    uncolored_result = colorize(lead, num, None)
    assert uncolored_result == 'test=42' or uncolored_result == 'test=42', 'unexpected colorize() result'
    assert uncolored_result == colored_result, 'unexpected colorize() result'

    # We should get the same result if we force color off
    old_color = ANSIBLE_COLOR
    ANSIBLE_COLOR = False
    uncolored_result = colorize

# Generated at 2022-06-13 16:06:32.461105
# Unit test for function stringc
def test_stringc():
    """Test stringc."""
    def check(actual, expected):
        """Assert that the string matches the expected value."""
        assert actual == expected, u"\n(%r != %r)" % (actual, expected)

    check(stringc(u'text', u'blue'), u'\033[34mtext\033[0m')
    check(stringc(u'text', u'unknown'), u'text')
    check(stringc(u'text', u'color3'), u'\033[38;5;11mtext\033[0m')
    check(stringc(u'text', u'rgb333'), u'\033[38;5;59mtext\033[0m')

# Generated at 2022-06-13 16:06:41.952202
# Unit test for function stringc
def test_stringc():
    assert stringc("text", "red", True) == "\001\033[31m\002text\001\033[0m\002"
    assert stringc("text", "red", False) == "\033[31mtext\033[0m"
    assert stringc("text", "color2", False) == "\033[38;5;2mtext\033[0m"
    assert stringc("text", "color2", True) == "\001\033[38;5;2m\002text\001\033[0m\002"
    assert stringc("text", "color2", True) == "\001\033[38;5;2m\002text\001\033[0m\002"

# Generated at 2022-06-13 16:06:53.987306
# Unit test for function hostcolor
def test_hostcolor():

    # Formatting strings
    statstr = u'%s: ok=%d changed=%d unreachable=%d failed=%d'
    hoststr = u'             %s'

    # Color and formatting info for each host
    host_info = []

    # Generate a few host tests
    for i in range(1, 10):
        stats = {}
        ok = i % 3
        changed = i % 4
        unreachable = i % 5
        failed = i % 6
        host = u'test%d' % i

        stats['ok'] = ok
        stats['changed'] = changed
        stats['unreachable'] = unreachable
        stats['failed'] = failed
        stats['color'] = None

        stat = (statstr % (host, ok, changed, unreachable, failed))

# Generated at 2022-06-13 16:07:02.635373
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor(u'foo', dict(ok=0, changed=0, unreachable=0, failed=0), False) == u'foo                           '
    assert hostcolor(u'foo', dict(ok=0, changed=0, unreachable=0, failed=0)) == u'foo                           '
    assert hostcolor(u'foo', dict(ok=0, changed=1, unreachable=0, failed=0)) == u'foo                           '
    assert hostcolor(u'foo', dict(ok=0, changed=0, unreachable=1, failed=0)) == u'foo                           '
    assert hostcolor(u'foo', dict(ok=0, changed=0, unreachable=0, failed=1)) == u'foo                           '

# Generated at 2022-06-13 16:07:04.753163
# Unit test for function colorize
def test_colorize():
    assert colorize('foo', 0, 'blue') == u'foo=0   '


# Generated at 2022-06-13 16:07:09.963355
# Unit test for function stringc
def test_stringc():
    """Sample program to demonstrate the usage of stringc to print with color."""
    for color in ['black', 'red', 'green', 'yellow', 'blue', 'purple', 'cyan', 'white']:
        print(u"This is %s in color." % (stringc(color, color)))


# --- end of "pretty"


# --- begin "display" ---


# Generated at 2022-06-13 16:07:16.487896
# Unit test for function stringc

# Generated at 2022-06-13 16:07:21.213085
# Unit test for function stringc
def test_stringc():
    """
    >>> print(stringc("hello", "blue"))
    hello
    >>> print(stringc("hello", "blue", wrap_nonvisible_chars=True))
    hello
    """
# --- end of "pretty"

if __name__ == '__main__':
    # unit tests
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 16:07:27.750615
# Unit test for function stringc
def test_stringc():
    # Just testing that nothing fails and that enough of the string
    # is painted to make it identifiable
    stringc("the quick brown fox jumped over the lazy dog", "white")
    stringc("the quick brown fox jumped over the lazy dog", "red")
    stringc("the quick brown fox jumped over the lazy dog", "green")
    stringc("the quick brown fox jumped over the lazy dog", "yellow")
    stringc("the quick brown fox jumped over the lazy dog", "blue")
    stringc("the quick brown fox jumped over the lazy dog", "magenta")
    stringc("the quick brown fox jumped over the lazy dog", "cyan")

    stringc("the quick brown fox jumped over the lazy dog", "white", True)
    stringc("the quick brown fox jumped over the lazy dog", "red", True)

# Generated at 2022-06-13 16:07:30.684133
# Unit test for function stringc
def test_stringc():
    print(stringc('Hello, world', 'cyan'))
    print(stringc('Hello, world', 'rgb050'))
    print(stringc('Hello, world', 'color99'))



# Generated at 2022-06-13 16:07:42.285967
# Unit test for function stringc
def test_stringc():
    if ANSIBLE_COLOR:
        stringc(u'foreground color', 'red')
        stringc(u'foreground color', 'rgb255')
        stringc(u'foreground color', 'rgb225')
        stringc(u'foreground color', 'color9')
        stringc(u'foreground color', 'gray4')
    else:
        pass
    pass

# --- end "pretty"


# Generated at 2022-06-13 16:07:53.863319
# Unit test for function stringc
def test_stringc():
    for color in C.COLOR_CODES:
        print(stringc('test', color))
    for color_num in range(0, 256):
        print(stringc('test', str(color_num)))

# Generated at 2022-06-13 16:08:04.636124
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor("localhost", dict(failures=1, unreachable=1, changed=1, ok=0)) == u"localhost                                 "
    assert hostcolor("localhost", dict(failures=0, unreachable=1, changed=1, ok=0)) == u"localhost                                 "
    assert hostcolor("localhost", dict(failures=0, unreachable=0, changed=0, ok=1)) == u"localhost                                 "
    assert hostcolor("localhost", dict(failures=0, unreachable=0, changed=1, ok=1)) == u"localhost                                 "
    assert hostcolor("localhost", dict(failures=0, unreachable=0, changed=0, ok=0)) == u"localhost                                 "


# --- end "pretty"



# Generated at 2022-06-13 16:08:08.087511
# Unit test for function stringc
def test_stringc():
    assert stringc('hello', 'red') == u"\033[31mhello\033[0m"
    assert stringc(u'привет', 'red') == u"\033[31mпривет\033[0m"

# Generated at 2022-06-13 16:08:18.932158
# Unit test for function stringc
def test_stringc():
    from ansible import utils
    from units.mock.loader import DictDataLoader

    loader = DictDataLoader({
        "test_stringc.yml": """
        - hosts: localhost
          tasks:
            - name: run the stringc tests
              action: command echo '{{ stringc("Hello World", "blue") }}'
              register: result
        """,
    })

    inventory = utils.create_inventory(loader=loader)
    playbook = PlaybookInventory(loader.load("test_stringc.yml"), inventory)
    tqm = TaskQueueManager(
        inventory=inventory,
        variable_manager=playbook.get_variable_manager(),
        loader=loader,
    )
    result = tqm.run(playbook)
    # print(result)

# Generated at 2022-06-13 16:08:26.970974
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor("example.org", {"changes": 0, "ok": 0}, True) == u"%-37s" % u'\u001b[32;01mexample.org\u001b[0m'
    assert hostcolor("example.org", {"changes": 0, "ok": 0}, False) == u"%-26s" % 'example.org'
    assert hostcolor("example.org", {"changed": 0, "ok": 0}, True) == u"%-37s" % u'\u001b[32;01mexample.org\u001b[0m'
    assert hostcolor("example.org", {"changed": 0, "ok": 0}, False) == u"%-26s" % 'example.org'

# Generated at 2022-06-13 16:08:35.521132
# Unit test for function hostcolor
def test_hostcolor():
    from ansible.compat.tests.mock import patch

    # Test with ANSIBLE_COLOR=False
    with patch.dict("os.environ", ANSIBLE_COLOR="False"):
        assert hostcolor("127.0.0.1", {}, False) == "%-26s" % "127.0.0.1"

    # Test with changed=True

# Generated at 2022-06-13 16:08:45.893163
# Unit test for function colorize
def test_colorize():
    """This function tests the colorize() function."""
    global ANSIBLE_COLOR

    ANSIBLE_COLOR = True

    assert(colorize("ok", 0, "green") == 'ok=0   ')
    assert(colorize("changed", 0, "yellow") == 'changed=0')
    assert(colorize("failed", 0, "red") == 'failed=0 ')
    assert(colorize("skipped", 0, "cyan") == 'skipped=0')
    assert(colorize("unreachable", 0, "magenta") == 'unreachable=0 ')

    ANSIBLE_COLOR = False

    assert(colorize("ok", 0, "green") == 'ok=0   ')
    assert(colorize("changed", 0, "yellow") == 'changed=0')

# Generated at 2022-06-13 16:08:57.404756
# Unit test for function stringc
def test_stringc():
    assert stringc("foo", "black") == "\033[30mfoo\033[0m"
    assert stringc("foo", "red") == "\033[31mfoo\033[0m"
    assert stringc("foo", "green") == "\033[32mfoo\033[0m"
    assert stringc("foo", "yellow") == "\033[33mfoo\033[0m"
    assert stringc("foo", "blue") == "\033[34mfoo\033[0m"
    assert stringc("foo", "magenta") == "\033[35mfoo\033[0m"
    assert stringc("foo", "cyan") == "\033[36mfoo\033[0m"
    assert stringc("foo", "white") == "\033[37mfoo\033[0m"

# Generated at 2022-06-13 16:09:05.477569
# Unit test for function stringc
def test_stringc():
    assert(parsecolor('blue') == u'34')
    assert(parsecolor('color1') == u'38;5;1')
    assert(parsecolor('color99') == u'38;5;99')
    assert(parsecolor('rgb000') == u'38;5;16')
    assert(parsecolor('rgb200') == u'38;5;50')
    assert(parsecolor('rgb333') == u'38;5;63')
    assert(parsecolor('rgb444') == u'38;5;60')
    assert(parsecolor('rgb555') == u'38;5;58')
    assert(parsecolor('rgb666') == u'38;5;54')

# Generated at 2022-06-13 16:09:31.177861
# Unit test for function colorize
def test_colorize():
    print(u"%-15s %s" % (u"COLOR_ERROR", colorize(u"E", 0, C.COLOR_ERROR)))
    print(u"%-15s %s" % (u"COLOR_ERROR", colorize(u"E", 1, C.COLOR_ERROR)))
    print(u"%-15s %s" % (u"COLOR_CHANGED", colorize(u"C", 0, C.COLOR_CHANGED)))
    print(u"%-15s %s" % (u"COLOR_CHANGED", colorize(u"C", 1, C.COLOR_CHANGED)))
    print(u"%-15s %s" % (u"COLOR_OK", colorize(u"O", 0, C.COLOR_OK)))