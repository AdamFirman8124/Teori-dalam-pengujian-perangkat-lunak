

# Generated at 2022-06-13 15:59:42.364971
# Unit test for function parsecolor
def test_parsecolor():
    """Test suite for function parsecolor."""
    # Test integer colors
    assert parsecolor("color0") == "38;5;0"
    assert parsecolor("color1") == "38;5;1"
    assert parsecolor("color2") == "38;5;2"
    assert parsecolor("color3") == "38;5;3"
    assert parsecolor("color4") == "38;5;4"
    assert parsecolor("color5") == "38;5;5"
    assert parsecolor("color6") == "38;5;6"
    assert parsecolor("color7") == "38;5;7"
    assert parsecolor("color8") == "38;5;8"
    assert parsecolor("color9") == "38;5;9"
   

# Generated at 2022-06-13 15:59:46.492889
# Unit test for function stringc
def test_stringc():
    # Test with all defined colors
    color_codes = sorted(C.COLOR_CODES.items())
    for (name, value) in color_codes:
        for attribute in [0, 1, 4, 7]:
            expected = "[%d;%smtest[0m" % (attribute, value)
            assert expected == stringc("test", "%s%s" % (name, attribute))

    # Test with rgb and gray
    assert u"[38;5;124mtest[0m" == stringc("test", "rgb124")
    assert u"[38;5;124mtest[0m" == stringc("test", "color124")
    assert u"[38;5;16mtest[0m" == stringc("test", "rgb100")

# Generated at 2022-06-13 15:59:50.865070
# Unit test for function stringc
def test_stringc():
    failed = 0
    for color in C.COLOR_CODES.keys():
        if parsecolor(color) != C.COLOR_CODES[color]:
            failed += 1
            print("ERROR: color %s parsed incorrectly" % color)

    for color in range(0, 256):
        if parsecolor("color%d" % color) != "38;5;%d" % color:
            failed += 1
            print("ERROR: color %d parsed incorrectly" % color)

    for r in range(0, 6):
        for g in range(0, 6):
            for b in range(0, 6):
                if parsecolor("rgb%d%d%d" % (r, g, b)) != "38;5;%d" % (16 + 36*r + 6*g + b):
                    failed

# Generated at 2022-06-13 16:00:01.869158
# Unit test for function hostcolor
def test_hostcolor():
    # Tests with color enabled
    stats = dict(failures=1, unreachable=0, changed=0)
    assert hostcolor(u"darkblue", stats, True) == u"darkblue               "
    stats = dict(failures=0, unreachable=1, changed=0)
    assert hostcolor(u"darkblue", stats, True) == u"darkblue               "
    stats = dict(failures=0, unreachable=0, changed=1)
    assert hostcolor(u"darkblue", stats, True) == u"darkblue               "
    # Tests with color disabled
    stats = dict(failures=1, unreachable=0, changed=0)
    assert hostcolor(u"darkblue", stats, False) == u"darkblue     "

# Generated at 2022-06-13 16:00:08.661868
# Unit test for function colorize

# Generated at 2022-06-13 16:00:17.991429
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor('green') == '32'
    assert parsecolor('color2') == '38;5;2'
    assert parsecolor('color10') == '38;5;10'
    assert parsecolor('gray1') == '38;5;233'
    assert parsecolor('gray10') == '38;5;242'
    assert parsecolor('rgb322') == '38;5;49'
    assert parsecolor('rgb333') == '38;5;51'
    assert parsecolor('rgb433') == '38;5;62'
    assert parsecolor('rgb543') == '38;5;73'
    assert parsecolor('rgb000') == '38;5;16'

# Generated at 2022-06-13 16:00:23.014747
# Unit test for function parsecolor
def test_parsecolor():
    # Test the color names
    assert parsecolor(u'black')    == u'38;5;16'
    assert parsecolor(u'red')      == u'38;5;196'
    assert parsecolor(u'green')    == u'38;5;46'
    assert parsecolor(u'yellow')   == u'38;5;226'
    assert parsecolor(u'blue')     == u'38;5;21'
    assert parsecolor(u'magenta')  == u'38;5;201'
    assert parsecolor(u'cyan')     == u'38;5;51'
    assert parsecolor(u'white')    == u'38;5;231'

    # Test the color numbers

# Generated at 2022-06-13 16:00:28.106357
# Unit test for function hostcolor
def test_hostcolor():
    stats = dict(darkgreen=dict(ok=10,
                                changed=0,
                                unreachable=0,
                                failures=0),
                 darkred=dict(ok=1,
                              changed=0,
                              unreachable=1,
                              failures=1),
                 darkyellow=dict(ok=1,
                                 changed=1,
                                 unreachable=0,
                                 failures=0))

    for color, result in stats.items():
        assert hostcolor("localhost", result, color)



# Generated at 2022-06-13 16:00:34.765194
# Unit test for function stringc
def test_stringc():
    """Unit tests for stringc."""
    assert stringc(u"test", "red") == u"\033[31mtest\033[0m"
    assert stringc(u"test", u"color1") == u"\033[38;5;1mtest\033[0m"
    assert stringc(u"test", u"color9") == u"\033[38;5;9mtest\033[0m"
    assert stringc(u"test", u"color10") == u"\033[38;5;10mtest\033[0m"
    assert stringc(u"test", u"color12") == u"\033[38;5;12mtest\033[0m"

# Generated at 2022-06-13 16:00:44.008764
# Unit test for function hostcolor
def test_hostcolor():
    from ansible.utils.color import hostcolor
    host = 'foo.example.org'
    stats = {'alive': True,
             'changed': False,
             'dark': False,
             'failed': False,
             'failures': 0,
             'ok': True,
             'processed': True,
             'rescued': 0,
             'skipped': False,
             'unreachable': 0,
             }
    assert hostcolor(host, stats, True) == stringc(host, C.COLOR_OK)
    assert hostcolor(host, stats, False) == u"%-26s" % host

    stats['changed'] = True
    assert hostcolor(host, stats, True) == stringc(host, C.COLOR_CHANGED)


# Generated at 2022-06-13 16:01:00.045600
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('localhost', dict(failures=0, unreachable=0, ok=1, changed=1, skipped=0)) == 'localhost                         '
    assert hostcolor('localhost', dict(failures=1, unreachable=0, ok=0, changed=1, skipped=0)) == u'\x1b[31mlocalhost                         \x1b[0m'
    assert hostcolor('localhost', dict(failures=0, unreachable=0, ok=0, changed=1, skipped=0)) == u'\x1b[33mlocalhost                         \x1b[0m'
    assert hostcolor('localhost', dict(failures=0, unreachable=0, ok=0, changed=0, skipped=0)) == u'\x1b[32mlocalhost                         \x1b[0m'



# Generated at 2022-06-13 16:01:04.879039
# Unit test for function hostcolor
def test_hostcolor():
    host = 'host.example.invalid'

    stats = dict(
        changed=0,
        failures=0,
        unreachable=0,
    )
    assert hostcolor(host, stats) == u"host.example.invalid          "
    assert hostcolor(host, stats, False) == u"host.example.invalid          "

    stats = dict(
        changed=1,
        failures=0,
        unreachable=0,
    )
    assert hostcolor(host, stats) == u"host.example.invalid          "

    stats = dict(
        changed=0,
        failures=1,
        unreachable=0,
    )
    assert hostcolor(host, stats) == u"host.example.invalid          "


# Generated at 2022-06-13 16:01:12.781328
# Unit test for function stringc
def test_stringc():
    print(stringc(u"text", u"black"))
    print(stringc(u"text", u"red"))
    print(stringc(u"text", u"green"))
    print(stringc(u"text", u"yellow"))
    print(stringc(u"text", u"blue"))
    print(stringc(u"text", u"purple"))
    print(stringc(u"text", u"cyan"))
    print(stringc(u"text", u"white"))



# Generated at 2022-06-13 16:01:20.198108
# Unit test for function hostcolor
def test_hostcolor():
    host = u'localhost'

    # Test success case
    stats = {
        'changed': 0,
        'failures': 0,
        'ok': 10,
        'skipped': 0,
        'unreachable': 0
    }
    colorized_host = hostcolor(host, stats)
    assert isinstance(colorized_host, unicode)
    assert host in colorized_host

    # Test failure case
    stats = {
        'changed': 0,
        'failures': 1,
        'ok': 9,
        'skipped': 0,
        'unreachable': 0
    }
    colorized_host = hostcolor(host, stats)
    assert host in colorized_host

    # Test changed case

# Generated at 2022-06-13 16:01:30.438037
# Unit test for function hostcolor
def test_hostcolor():
    stats = dict(failures=1, unreachable=0, changed=0)
    result = hostcolor('test', stats, color=True)
    assert result == u"%-37s" % stringc('test', C.COLOR_ERROR)

    stats = dict(failures=0, unreachable=1, changed=0)
    result = hostcolor('test', stats, color=True)
    assert result == u"%-37s" % stringc('test', C.COLOR_ERROR)

    stats = dict(failures=0, unreachable=0, changed=1)
    result = hostcolor('test', stats, color=True)
    assert result == u"%-37s" % stringc('test', C.COLOR_CHANGED)

    stats = dict(failures=0, unreachable=0, changed=0)

# Generated at 2022-06-13 16:01:39.349085
# Unit test for function colorize
def test_colorize():
    # Set ANSIBLE_COLOR to True for the duration of this test
    color_setting = ANSIBLE_COLOR
    ANSIBLE_COLOR = True

    # We are only testing two things:
    # 1. The appearance of a colorized string
    # 2. The absence of a colorized string
    #
    # To do this, we test two scenarios:
    # 1. Colorize something, then test for colorization
    # 2. Colorize something, then set ANSIBLE_COLOR to False and test for
    #    the absence of colorization.

    # Test colorization of "skipped"
    colorized_skipped = colorize('skipped', 4, 'yellow')
    assert(re.match('skipped=4\033.*?m$', colorized_skipped))

    # Test lack of colorization of "skipped"


# Generated at 2022-06-13 16:01:48.659837
# Unit test for function colorize
def test_colorize():
    assert colorize('test', 0, 'blue') == 'test=0   '
    assert u'\033[0;34mtest=0   \033[0m' == colorize('test', 0, 'blue')
    assert colorize('test', 10, 'blue') == 'test=10  '
    assert u'\033[0;34mtest=10  \033[0m' == colorize('test', 10, 'blue')
    assert colorize('test', 100, 'blue') == 'test=100 '
    assert u'\033[0;34mtest=100 \033[0m' == colorize('test', 100, 'blue')
    assert colorize('test', 1000, 'blue') == 'test=1000'
    assert u'\033[0;34mtest=1000\033[0m' == colorize

# Generated at 2022-06-13 16:01:54.971679
# Unit test for function stringc

# Generated at 2022-06-13 16:02:03.630928
# Unit test for function colorize
def test_colorize():
    """Unit test for function colorize."""
    if not ANSIBLE_COLOR:
        print("Skipping tests for colorize, because colors are disabled")
        return

    # add some colors to our palette so we can test all colors
    C.COLOR_CODES['test1'] = '131'
    C.COLOR_CODES['test2'] = '129'
    C.COLOR_CODES['test3'] = '251'

    # test colorize with a single string
    try:
        assert colorize('ok', '1', 'test1') == stringc('ok=1', 'test1')
    except AssertionError:
        pass

    # test colorize with a string and a non-string

# Generated at 2022-06-13 16:02:08.285285
# Unit test for function colorize
def test_colorize():
    from ansible.utils import colorize
    s = colorize(u"", 0, None)
    if (s != u"=0   "):
        raise AssertionError
    s = colorize(u"", 0, u"black")
    if (s != u"=0   "):
        raise AssertionError
    s = colorize(u"", 0, u"white")
    if (s != u"=0   "):
        raise AssertionError
    s = colorize(u"", 0, u"blue")
    if (s != u"=0   "):
        raise AssertionError
    s = colorize(u"", 1, u"black")
    if (s != u"=1   "):
        raise AssertionError

# Generated at 2022-06-13 16:02:15.968170
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor(u'localhost', {'failures': 1, 'ok': 2, 'changed': 3, 'unreachable': 0}) == u'\033[0;31mlocalhost               \033[0m'
    assert hostcolor(u'localhost', {'failures': 0, 'ok': 2, 'changed': 0, 'unreachable': 0}) == u'\033[0;32mlocalhost               \033[0m'
    assert hostcolor(u'localhost', {'failures': 0, 'ok': 2, 'changed': 3, 'unreachable': 0}) == u'\033[0;33mlocalhost               \033[0m'

# Generated at 2022-06-13 16:02:24.322541
# Unit test for function stringc
def test_stringc():
    try:
        import curses
        curses.setupterm()
        has_colors = curses.tigetnum('colors') > 0
        if not has_colors:
            raise Exception("no colors")
    except:
        has_colors = False
    if has_colors:
        for color in C.COLOR_CODES:
            # skip colors that aren't supported by curses
            if color in ('purple', 'white', 'yellow'):
                continue
            assert stringc("test", color)
    else:
        for color in C.COLOR_CODES:
            assert stringc("test", color) == "test"



# Generated at 2022-06-13 16:02:30.523264
# Unit test for function hostcolor
def test_hostcolor():
    stats1 = dict(ok=1, failures=0, skipped=0, unreachable=0)
    stats2 = dict(ok=1, failures=1, skipped=0, unreachable=0)
    stats3 = dict(ok=1, failures=0, skipped=0, unreachable=1)
    stats4 = dict(ok=0, failures=0, skipped=1, unreachable=0)
    host = "testhost"
    assert hostcolor(host, stats1, True) == stringc(u"testhost", C.COLOR_OK)
    assert hostcolor(host, stats2, True) == stringc(u"testhost", C.COLOR_ERROR)
    assert hostcolor(host, stats3, True) == stringc(u"testhost", C.COLOR_UNREACHABLE)

# Generated at 2022-06-13 16:02:39.660078
# Unit test for function colorize
def test_colorize():
    def check(lead, num, color):
        return color in colorize(lead, num, color)

    assert check("ok", 0, C.COLOR_OK)
    assert check("changed", 0, C.COLOR_CHANGED)
    assert check("unreachable", 0, C.COLOR_UNREACHABLE)
    assert check("failed", 0, C.COLOR_ERROR)

    assert check("ok", 1, C.COLOR_OK)
    assert check("changed", 1, C.COLOR_CHANGED)
    assert check("unreachable", 1, C.COLOR_UNREACHABLE)
    assert check("failed", 1, C.COLOR_ERROR)

# Generated at 2022-06-13 16:02:43.239062
# Unit test for function hostcolor
def test_hostcolor():
    for color in [True, False]:
        yield check_hostcolor, {'changed':0, 'failures':1, 'ok':0, 'skipped':0, 'unreachable':0, 'dark':0}, 'localhost', 'error', color,
        yield check_hostcolor, {'changed':0, 'failures':0, 'ok':1, 'skipped':0, 'unreachable':0, 'dark':0}, 'localhost', 'ok', color,
        yield check_hostcolor, {'changed':1, 'failures':0, 'ok':0, 'skipped':0, 'unreachable':0, 'dark':0}, 'localhost', 'changed', color


# Generated at 2022-06-13 16:02:54.813613
# Unit test for function stringc
def test_stringc():
    assert stringc("Hello World", "blue") == "\033[34mHello World\033[0m"
    assert stringc("Hello World", "red") == "\033[31mHello World\033[0m"
    assert stringc("Hello World", "green") == "\033[32mHello World\033[0m"
    assert stringc("Hello World", "magenta") == "\033[35mHello World\033[0m"
    assert stringc("Hello World", "cyan") == "\033[36mHello World\033[0m"
    assert stringc("Hello World", "yellow") == "\033[33mHello World\033[0m"
    assert stringc("Hello World", "black") == "\033[30mHello World\033[0m"

# Generated at 2022-06-13 16:03:05.153023
# Unit test for function stringc
def test_stringc():
    assert stringc('TEXT', 'black') == '\033[30mTEXT\033[0m'
    assert stringc('TEXT', 'dark gray') == '\033[90mTEXT\033[0m'
    assert stringc('TEXT', 'red') == '\033[91mTEXT\033[0m'
    assert stringc('TEXT', 'light red') == '\033[91mTEXT\033[0m'
    assert stringc('TEXT', 'green') == '\033[92mTEXT\033[0m'
    assert stringc('TEXT', 'light green') == '\033[92mTEXT\033[0m'
    assert stringc('TEXT', 'yellow') == '\033[93mTEXT\033[0m'

# Generated at 2022-06-13 16:03:10.606990
# Unit test for function stringc

# Generated at 2022-06-13 16:03:21.869575
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('example.com', dict(ok=1, changed=0, unreachable=0, failures=0), True) == u"%-26s" % stringc('example.com', C.COLOR_OK)
    assert hostcolor('example.com', dict(ok=1, changed=1, unreachable=0, failures=0), True) == u"%-26s" % stringc('example.com', C.COLOR_CHANGED)
    assert hostcolor('example.com', dict(ok=1, changed=0, unreachable=0, failures=1), True) == u"%-26s" % stringc('example.com', C.COLOR_ERROR)

# Generated at 2022-06-13 16:03:29.331332
# Unit test for function colorize
def test_colorize():
    # just one case to test each conditional
    assert colorize('ok', 0, 'green') == 'ok=0   '
    assert colorize('changed', 0, 'yellow') == 'changed=0   '
    assert colorize('failed', 3, 'red') == 'failed=3   '
    assert colorize('skipped', 2, 'cyan') == 'skipped=2  '
    # count=0 shouldn't colorize
    assert colorize('ok', 0, None) == 'ok=0   '
    assert colorize('changed', 0, None) == 'changed=0   '
    assert colorize('failed', 0, None) == 'failed=0   '
    assert colorize('skipped', 0, None) == 'skipped=0  '



# Generated at 2022-06-13 16:03:42.894415
# Unit test for function colorize
def test_colorize():
    text = "Running...\nRunning...\nOk:\n\nOk:\nKo:\n\nOk:\n"

    # Return value for colorize function should be a string
    assert(isinstance(colorize("A", 1, "blue"), str))

    # Check unicode conversion
    assert(isinstance(colorize("A", 1, "blue"), unicode))

    # Formatting should not change if ANSIBLE_COLOR is False
    assert(colorize("A", 1, "blue") == "A=1   ")

    # Check that colorization works
    assert(colorize("A", 1, "blue") != "A=1   ")
    assert( colorize("A", 0, "blue") == "A=0   ")

    # Check that colorization works with multiple lines

# Generated at 2022-06-13 16:03:47.312188
# Unit test for function hostcolor
def test_hostcolor():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task

    results = {
        'contacted': {},
        'dark': {},
    }

    # create task with default PlayContext
    task = Task()

    assert hostcolor('test', results['contacted']) == 'test                         '
    assert hostcolor('test', results['contacted'], color=False) == 'test                         '

    results['contacted']['failed'] = '1'
    assert hostcolor('test', results['contacted']).startswith(stringc('test', C.COLOR_ERROR))
    assert hostcolor('test', results['contacted'], color=False) == 'test                         '

    # create task with PlayContext, disable color

# Generated at 2022-06-13 16:03:54.369450
# Unit test for function colorize
def test_colorize():
    print(colorize(u"test",    0, C.COLOR_SKIP))
    print(colorize(u"verbose", 0, C.COLOR_VERBOSE))
    print(colorize(u"changed", 0, C.COLOR_CHANGED))
    print(colorize(u"ok",      0, C.COLOR_OK))
    print(colorize(u"failed",  0, C.COLOR_ERROR))
    print(colorize(u"unreachable", 0, C.COLOR_UNREACHABLE))
    print(colorize(u"test",    99, C.COLOR_SKIP))
    print(colorize(u"verbose", 99, C.COLOR_VERBOSE))
    print(colorize(u"changed", 99, C.COLOR_CHANGED))

# Generated at 2022-06-13 16:04:05.762139
# Unit test for function stringc
def test_stringc():
    """Unit test for function stringc."""
    print(stringc('black', 'black'))
    print(stringc('red', 'red'))
    print(stringc('green', 'green'))
    print(stringc('yellow', 'yellow'))
    print(stringc('blue', 'blue'))
    print(stringc('magenta', 'magenta'))
    print(stringc('cyan', 'cyan'))
    print(stringc('white', 'white'))
    print(stringc('bright black', 'bright black'))
    print(stringc('bright red', 'bright red'))
    print(stringc('bright green', 'bright green'))
    print(stringc('bright yellow', 'bright yellow'))
    print(stringc('bright blue', 'bright blue'))

# Generated at 2022-06-13 16:04:17.492000
# Unit test for function colorize
def test_colorize():

    def check(lead, num, color, result):
        r = colorize(lead, num, color)
        if r != result:
            print("colorize(%s,%s,%s) = %s" % (lead, num, color, r))

    check('foo', 0, None, u"foo=0   ")
    check('foo', 0, 'green', u"foo=0   ")
    check('foo', 1, 'green', u"foo=1   ")
    check('foo', 1, 'red', u"foo=1   ")

    host = 'localhost'
    stats = dict(changed=0, failures=0, unreachable=0)

    if hostcolor(host, stats, color=False) != u"%-26s" % host:
        print("hostcolor returned incorrect value")

   

# Generated at 2022-06-13 16:04:28.119798
# Unit test for function hostcolor
def test_hostcolor():
    host = 'fakehost'
    stats = dict(failures=0, unreachable=0, changed=0)
    assert hostcolor(host=host, stats=stats, color=False) == '%-26s' % host
    assert hostcolor(host=host, stats=stats, color=True) == '%-37s' % stringc(host, C.COLOR_OK)
    stats = dict(failures=1, unreachable=0, changed=0)
    assert hostcolor(host=host, stats=stats, color=True) == '%-37s' % stringc(host, C.COLOR_ERROR)
    stats = dict(failures=0, unreachable=1, changed=0)

# Generated at 2022-06-13 16:04:34.714680
# Unit test for function hostcolor
def test_hostcolor():
    result_error   = hostcolor('host', {'failures' : 1}, color=True)
    result_changed = hostcolor('host', {'changed' : 1}, color=True)
    result_ok      = hostcolor('host', {'ok' : 1}, color=True)
    assert result_error   == u"\033[31mhost                     \033[0m"
    assert result_changed == u"\033[34mhost                     \033[0m"
    assert result_ok      == u"\033[32mhost                     \033[0m"


# Generated at 2022-06-13 16:04:41.104457
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('localhost', dict(failures=1, unreachable=0, changed=0), color=True) == u'%-37s' % (u'\n'.join(u'\033[31m%s\033[0m' % t for t in u'localhost'.split(u'\n')))
    assert hostcolor('localhost', dict(failures=0, unreachable=1, changed=0), color=True) == u'%-37s' % (u'\n'.join(u'\033[31m%s\033[0m' % t for t in u'localhost'.split(u'\n')))

# Generated at 2022-06-13 16:04:43.403815
# Unit test for function colorize
def test_colorize():
    for c in ('red', 'green', 'blue', 'yellow', 'cyan', 'magenta'):
        print(colorize('XX', 42, c))

#
# --- end pretty

# Generated at 2022-06-13 16:04:49.498683
# Unit test for function stringc
def test_stringc():
    # Success tests
    assert stringc(u"test", u"red") == u'\033[31mtest\033[0m'

    # Failure tests
    try:
        stringc(u"test", u"unknown")
    except KeyError:
        pass
    else:
        raise AssertionError("Expected KeyError to be raised")

# Generated at 2022-06-13 16:05:01.282962
# Unit test for function colorize
def test_colorize():
    '''colorize should colorize a string if ANSIBLE_COLOR is True'''
    # Set True so that stringc will return a colorized string
    global ANSIBLE_COLOR
    ANSIBLE_COLOR = True

    # colorize uses stringc when ANSIBLE_COLOR is True
    assert colorize('ok', 0, 'green') == u'\x1b[32mok=0  \x1b[0m'
    assert colorize('changed', 0, 'yellow') == u'\x1b[33mchanged=0  \x1b[0m'
    assert colorize('unreachable', 0, 'red') == u'\x1b[31munreachable=0\x1b[0m'

# Generated at 2022-06-13 16:05:11.510237
# Unit test for function hostcolor
def test_hostcolor():
    host = "testhost"
    stats = {"failures": 0, "unreachable": 0, "changed": 0}
    assert hostcolor(host, stats, color=True) == u"\x1b[0;32m%-37s\x1b[0m" % host
    stats = {"failures": 0, "unreachable": 0, "changed": 1}
    assert hostcolor(host, stats, color=True) == u"\x1b[0;33m%-37s\x1b[0m" % host
    stats = {"failures": 1, "unreachable": 0, "changed": 0}
    assert hostcolor(host, stats, color=True) == u"\x1b[0;31m%-37s\x1b[0m" % host

# Generated at 2022-06-13 16:05:19.611865
# Unit test for function colorize
def test_colorize():
    from ansible import color
    from ansible.constants import COLOR_REPORT_SKIP
    from ansible.constants import COLOR_REPORT_OK
    from ansible.constants import COLOR_REPORT_CHANGED
    from ansible.constants import COLOR_REPORT_ERRORS

    assert color.colorize("skipped", 0, COLOR_REPORT_SKIP) == "skipped=0   "
    assert color.colorize("skipped", 1, COLOR_REPORT_SKIP) == "\x1b[0;37;40mskipped=1   \x1b[0m"
    assert color.colorize("changed", 0, COLOR_REPORT_CHANGED) == "changed=0  "

# Generated at 2022-06-13 16:05:21.381159
# Unit test for function colorize
def test_colorize():
    test_str = u"\033[38;5;160mthis is my string\033[0m"
    assert stringc(u"this is my string", u"color160") == test_str

# Generated at 2022-06-13 16:05:27.776024
# Unit test for function stringc
def test_stringc():
    """
    >>> import ansible.utils.ansible_color as ac
    >>> ac.stringc("test", "green") # doctest: +SKIP
    '\x1b[32mtest\x1b[0m'
    >>> ac.stringc("test", "badcolor")
    Traceback (most recent call last):
        ...
    Exception: invalid color specified
    """

if __name__ == "__main__":
    import doctest
    failed, tests = doctest.testmod()
    sys.exit(failed)

# Generated at 2022-06-13 16:05:38.845466
# Unit test for function stringc
def test_stringc():
    if not ANSIBLE_COLOR:
        print("Color not supported in this terminal.")
        sys.exit(1)

    print(u"\nColor should be green.")
    print(u"%s\n" % stringc(u'Green', 'green'))

    print(u"Color should be red.")
    print(u"%s\n" % stringc(u'Red', 'red'))

    print(u"Color should be blue.")
    print(u"%s\n" % stringc(u'Blue', 'blue'))

    print(u"Color should be magenta.")
    print(u"%s\n" % stringc(u'Magenta', 'magenta'))

    print(u"Color should be cyan.")

# Generated at 2022-06-13 16:05:46.434879
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor(u'localhost', {'failures': 0, 'unreachable': 0, 'ok': 1}) == u'localhost                     '
    assert hostcolor(u'localhost', {'failures': 0, 'unreachable': 1, 'ok': 0}) == u'localhost                     '
    assert hostcolor(u'localhost', {'failures': 1, 'unreachable': 1, 'ok': 0}) == u'localhost                     '
    assert hostcolor(u'localhost', {'failures': 0, 'unreachable': 1, 'ok': 2}) == u'localhost                     '
    assert hostcolor(u'localhost', {'failures': 1, 'unreachable': 0, 'ok': 1}) == u'localhost                     '

# Generated at 2022-06-13 16:05:55.228391
# Unit test for function hostcolor
def test_hostcolor():
    stats1 = dict(ok=1, changed=0, unreachable=0, failures=0)
    stats2 = dict(ok=1, changed=1, unreachable=0, failures=0)
    stats3 = dict(ok=0, changed=0, unreachable=1, failures=0)
    stats4 = dict(ok=0, changed=0, unreachable=0, failures=1)
    stats5 = dict(ok=0, changed=0, unreachable=0, failures=0)

    assert hostcolor('test1', stats1) == u'test1'
    assert hostcolor('test1', stats2) == u'test1'
    assert hostcolor('test1', stats3) == u'test1'
    assert hostcolor('test1', stats4) == u'test1'

# Generated at 2022-06-13 16:05:59.190709
# Unit test for function colorize
def test_colorize():
    assert colorize('le', 0, 'red') == 'le=0   '
    assert colorize('ad', 2, 'blue') == 'ad=2   '
    assert colorize('ad', 2, None) == 'ad=2   '


# Generated at 2022-06-13 16:06:07.192602
# Unit test for function stringc
def test_stringc():
    class SimpleNamespace(object):
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    ns = SimpleNamespace(
        COLOR_CODES={'blue': '1;34',
                     'cyan': '1;36',
                     'green': '1;32',
                     'magenta': '1;35',
                     'red': '1;31',
                     'yellow': '1;33',
                     'white': '1;37'})


# Generated at 2022-06-13 16:06:25.580717
# Unit test for function stringc
def test_stringc():
    """Tests for function stringc.

    If called directly, this function will run a test and then exit.
    """
    def _test(text, color, expected):
        result = stringc(text, color)
        if result != expected:
            raise AssertionError("%r != %r" % (result, expected))

    # ANSI color codes obtained from:
    # <http://www.termsys.demon.co.uk/vtansi.htm>

    # Reset, no color
    _test(u"foo\nbar", None, u"foo\nbar")

    # Basic text color
    _test(u"foo\nbar", C.COLOR_ERROR, u"\033[31mfoo\033[0m\n\033[31mbar\033[0m")

    # Basic text color with newline

# Generated at 2022-06-13 16:06:29.820917
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor(u"hostname", dict(failures=0, unreachable=0, changed=0)) == u"hostname                         "
    assert hostcolor(u"hostname", dict(failures=1, unreachable=1, changed=1)) == u"\033[31mhostname\033[0m                "
    assert hostcolor(u"hostname", dict(failures=0, unreachable=0, changed=1)) == u"\033[34mhostname\033[0m                "



# Generated at 2022-06-13 16:06:40.045858
# Unit test for function stringc
def test_stringc():

    try:
        import curses
    except ImportError:
        # curses library was not found, can't test
        return

    curses.setupterm()
    if curses.tigetnum('colors') < 0:
        # terminal does not support colors, can't test
        return

    def strip_escapes(str):
        return re.sub(r"\x1b\[\d+m", "", str)

    assert strip_escapes(u"\n".join(stringc(u"Start End", "never_a_real_color", wrap_nonvisible_chars=True).split(u'\n'))) == u"Start End"

# Generated at 2022-06-13 16:06:50.810129
# Unit test for function stringc
def test_stringc():
    if not ANSIBLE_COLOR:
        return

    from ansible.compat.tests import unittest
    from ansible.utils.color import stringc
    from ansible.utils.unicode import to_unicode

    class TestColor(unittest.TestCase):
        def test_stringc(self):
            black  = u"\u001b[30m";    end = u"\u001b[0m"
            red    = u"\u001b[31m";    end = u"\u001b[0m"
            green  = u"\u001b[32m";    end = u"\u001b[0m"
            yellow = u"\u001b[33m";    end = u"\u001b[0m"

# Generated at 2022-06-13 16:06:57.453262
# Unit test for function colorize
def test_colorize():
    lead = u"test"
    def my_print(num, color):
        s = colorize(lead, num, color)
        print(s)

    my_print(0, None)
    my_print(10, None)
    print(u"----- Enable color -----")
    my_print(0, u"blue")
    my_print(10, u"blue")
    my_print(0, u"red")
    my_print(10, u"red")

# --- end "pretty"



# Generated at 2022-06-13 16:07:04.811973
# Unit test for function stringc
def test_stringc():
    """ Unit test for function stringc """
    from ansible.compat.tests import unittest
    import ansible.constants as C

    class TestStringc(unittest.TestCase):
        def test_stringc_named_colors(self):

            # Test named colors
            self.assertEqual(stringc("foo", "black"), u"\033[30mfoo\033[0m")
            self.assertEqual(stringc("foo", "red"), u"\033[31mfoo\033[0m")
            self.assertEqual(stringc("foo", "green"), u"\033[32mfoo\033[0m")
            self.assertEqual(stringc("foo", "yellow"), u"\033[33mfoo\033[0m")

# Generated at 2022-06-13 16:07:14.082040
# Unit test for function hostcolor
def test_hostcolor():
    host = "test_host"
    stats = dict(ok=10, failures=1, unreachable=0, changed=0)
    assert hostcolor(host, stats, color=True) == u'test_host                      '

    stats = dict(ok=10, failures=0, unreachable=1, changed=0)
    assert hostcolor(host, stats, color=True) == u'\x1b[31mtest_host\x1b[0m           '

    stats = dict(ok=10, failures=0, unreachable=0, changed=1)
    assert hostcolor(host, stats, color=True) == u'\x1b[33mtest_host\x1b[0m           '

    stats = dict(ok=10, failures=0, unreachable=0, changed=0)
    assert hostcolor

# Generated at 2022-06-13 16:07:18.220463
# Unit test for function stringc
def test_stringc():
    print (stringc('Hello World!', 'red', True))
    print (stringc('Hello World!', 'rgb123', True))
    print (stringc('Hello World!', 'gray7', True))
    print (stringc('Hello World!', 'RED', True))


if __name__ == '__main__':
    test_stringc()
# --- end "pretty"



# Generated at 2022-06-13 16:07:26.275847
# Unit test for function hostcolor
def test_hostcolor():
    """
    This is just a sanity test, not a robust unit test.
    """

    def _eq(a, b):
        assert a == b, '%r != %r' % (a, b)
    stats = {'failures': 0, 'unreachable': 0, 'changed': 0}

    _eq(hostcolor('localhost', stats), 'localhost             ')
    stats['changed'] = 1
    _eq(hostcolor('localhost', stats), stringc('localhost', C.COLOR_CHANGED) + ' ' * 11)
    stats['failures'] = 1
    _eq(hostcolor('localhost', stats), stringc('localhost', C.COLOR_ERROR) + ' ' * 11)
    stats['unreachable'] = 1

# Generated at 2022-06-13 16:07:37.193649
# Unit test for function hostcolor
def test_hostcolor():
    host = "testhost"
    stats = {'ok': 0, 'changed': 0, 'unreachable': 0, 'failures': 1}
    expected = u"testhost".encode('utf-8')
    assert hostcolor(host, stats, True) == u"%-37s" % stringc(expected, C.COLOR_ERROR)
    stats = {'ok': 0, 'changed': 0, 'unreachable': 0, 'failures': 0}
    assert hostcolor(host, stats, True) == u"%-37s" % host
    stats = {'ok': 0, 'changed': 2, 'unreachable': 0, 'failures': 0}
    assert hostcolor(host, stats, True) == u"%-37s" % stringc(expected, C.COLOR_CHANGED)

# Generated at 2022-06-13 16:08:04.748947
# Unit test for function stringc
def test_stringc():
    """ Unit test for function stringc """
    assert stringc("hello", "red", True) == u"\x01\x1b[31m\x02hello\x01\x1b[0m\x02"
    assert stringc("hello", "red", False) == u"\x1b[31mhello\x1b[0m"
    assert stringc("hello", "color1", True) == u"\x01\x1b[38;5;1m\x02hello\x01\x1b[0m\x02"
    assert stringc("hello", "color1", False) == u"\x1b[38;5;1mhello\x1b[0m"

# Generated at 2022-06-13 16:08:14.118859
# Unit test for function stringc
def test_stringc():
    assert stringc("text", "green") == "\033[32mtext\033[0m"
    assert stringc("text", "bad color name") is not None
    assert stringc("text", "color1") == "\033[38;5;1mtext\033[0m"
    assert stringc("text", "rgb255255255") == "\033[38;5;15mtext\033[0m"
    assert stringc("text", "rgb000") == "\033[38;5;0mtext\033[0m"
    assert stringc("text", "gray0") == "\033[38;5;232mtext\033[0m"
    print(stringc("text", "rgb255255255"))

# Generated at 2022-06-13 16:08:23.278731
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor("localhost", {"failures": 1}, color=True) == u"\x1b[31mlocalhost              \x1b[0m"
    assert hostcolor("localhost", {"changed": 1}, color=True) == u"\x1b[33mlocalhost              \x1b[0m"
    assert hostcolor("localhost", {"ok": 1}, color=True) == u"\x1b[32mlocalhost              \x1b[0m"
    assert hostcolor("localhost", {"failures": 1, "changed": 1, "ok": 1}, color=True) == u"\x1b[31mlocalhost              \x1b[0m"



# Generated at 2022-06-13 16:08:31.108924
# Unit test for function hostcolor
def test_hostcolor():
    """Unit test for function hostcolor"""
    testhost = 'testhost'
    stats = {
        'failures': 0,
        'ok': 0,
        'skipped': 0,
        'changed': 0,
        'unreachable': 0
    }

    # Test with all stats set to 0
    assert testhost == hostcolor(testhost, stats)

    # Test with failures set to 1
    stats['failures'] = 1
    assert stringc(testhost, C.COLOR_ERROR) == hostcolor(testhost, stats)

    # Test with unreachable set to 1
    stats['unreachable'] = 1
    assert stringc(testhost, C.COLOR_ERROR) == hostcolor(testhost, stats)

    # Test with changed set to 1
    stats['changed'] = 1

# Generated at 2022-06-13 16:08:36.892347
# Unit test for function colorize
def test_colorize():
    print("colorize test:")
    base = '\033[1m%-15s\033[0m'
    if not colorize("foo", 3, "blue"): return 1
    if colorize("foo", 3, "blue") != base % stringc("foo=3", "blue"):
        return 1
    if not colorize("foo", 0, "yellow"): return 1
    if colorize("foo", 0, "yellow") != base % stringc("foo=0", "yellow"):
        return 1
    print("colorize test: ok")
    return 0



# Generated at 2022-06-13 16:08:45.659117
# Unit test for function stringc
def test_stringc():
    assert stringc('text', 'red', False) == '\033[31mtext\033[0m'
    assert stringc('text', 'red', True) == '\x01\033[31m\x02text\x01\033[0m\x02'
    assert stringc('text', '035', False) == '\033[38;5;35mtext\033[0m'
    assert stringc('text', 'rgb444', False) == '\033[38;5;60mtext\033[0m'
    assert stringc('text', 'rgb332', False) == '\033[38;5;52mtext\033[0m'



# Generated at 2022-06-13 16:08:52.724058
# Unit test for function colorize
def test_colorize():
    class FakeStdout(object):
        def isatty(self):
            return True

    sys.stdout = FakeStdout()
    for color in ('black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'):
        for i in range(0, 10):
            print('%-10s %s' % (color, colorize('VAR', i, color)))

# --- end "pretty"



# Generated at 2022-06-13 16:09:02.593946
# Unit test for function stringc
def test_stringc():
    """Unit test function stringc."""

    # Create dictionary of test data
    # Each item has:
    # - color
    # - input string
    # - expected output string
    # - expected return value (return val == 0 -> success)

# Generated at 2022-06-13 16:09:13.561279
# Unit test for function stringc
def test_stringc():
    def expect(actual, expected, msg=None):
        if actual == expected:
            print("test passed")
        else:
            print("test failed")
        assert actual == expected

    # Basic color tests
    expect(stringc("foo", "green"), u"\033[32mfoo\033[0m")
    expect(stringc("foo", "red"), u"\033[31mfoo\033[0m")
    expect(stringc("foo", "yellow"), u"\033[33mfoo\033[0m")

    # Invalid color test
    expect(stringc("foo", "blue"), u"\033[39mfoo\033[0m")

    # RGB tests
    expect(stringc("foo", "rgb255000"), u"\033[38;5;09mfoo\033[0m")
   

# Generated at 2022-06-13 16:09:21.704628
# Unit test for function hostcolor
def test_hostcolor():
    stats = dict(ok=0, failures=0, unreachable=0, changed=0, skipped=0)
    assert hostcolor("localhost", stats) == "%-26s" % "localhost"
    assert hostcolor("localhost", stats, color=False) == "%-26s" % "localhost"
    stats['changed'] = 1
    assert hostcolor("localhost", stats, color=False) == "%-26s" % "localhost"
    assert hostcolor("localhost", stats, color=True) == "%-37s" % stringc("localhost", C.COLOR_CHANGED)
    stats['failures'] = 5
    assert hostcolor("localhost", stats, color=False) == "%-26s" % "localhost"