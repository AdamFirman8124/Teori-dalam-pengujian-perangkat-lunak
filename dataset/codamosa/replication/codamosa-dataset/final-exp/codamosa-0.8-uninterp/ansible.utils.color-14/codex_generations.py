

# Generated at 2022-06-13 15:59:44.208842
# Unit test for function hostcolor
def test_hostcolor():
    h = 'foo.bar.baz'
    stats = dict(changed=0, failures=1, unreachable=0)
    s = hostcolor(h, stats, C.COLOR_ERROR)
    assert s == "\x1b[31;1m%-37s\x1b[0m" % h

    stats = dict(changed=1, failures=0, unreachable=0)
    s = hostcolor(h, stats, C.COLOR_CHANGED)
    assert s == "\x1b[33m%-37s\x1b[0m" % h

    stats = dict(changed=0, failures=0, unreachable=0)
    s = hostcolor(h, stats, C.COLOR_OK)
    assert s == "\x1b[32m%-37s\x1b[0m" % h



# Generated at 2022-06-13 15:59:49.358356
# Unit test for function colorize
def test_colorize():
    assert colorize('foo', 0, 'blue') == 'foo=0   '
    assert colorize('foo', 0, None) == 'foo=0   '
    assert colorize('foo', 123, 'blue') == 'foo=123 '
    assert colorize('foo', 123, None) == 'foo=123 '


# Generated at 2022-06-13 15:59:56.861876
# Unit test for function hostcolor
def test_hostcolor():
    host = 'foo.example.com'
    stats = {'failures': 0, 'unreachable': 0, 'changed': 0}
    # pylint: disable=unused-variable
    changed, ok, error = hostcolor(host, stats, color=True), hostcolor(host, stats, color=False), hostcolor(host,
                                                                                                          stats,
                                                                                                          color=True)
    assert ok == u"%-26s" % host, 'Unexpected output from hostcolor when color is False'
    assert changed == u"%-37s" % stringc(host, C.COLOR_OK), 'Unexpected output from hostcolor when color is True'
    assert error == u"%-37s" % stringc(host, C.COLOR_OK), 'Unexpected output from hostcolor when color is True'

# Generated at 2022-06-13 15:59:58.782603
# Unit test for function parsecolor
def test_parsecolor():
    for color, ansi_codes in C.COLOR_CODES.items():
        assert parsecolor(color) == ansi_codes

# Generated at 2022-06-13 16:00:06.529309
# Unit test for function hostcolor
def test_hostcolor():
    tests = {}
    tests[u'ok'] = {'ok': 1, 'changed': 0, 'unreachable': 0, 'failures': 0}
    tests[u'changed'] = {'ok': 0, 'changed': 1, 'unreachable': 0, 'failures': 0}
    tests[u'failures'] = {'ok': 0, 'changed': 0, 'unreachable': 0, 'failures': 1}
    tests[u'unreachable'] = {'ok': 0, 'changed': 0, 'unreachable': 1, 'failures': 0}

    for test in tests:
        print(hostcolor(test, tests[test]))

# --- end "pretty"
#
# ---
#
# Below used to be part of utils.py, then ansible-playbook, then ansible-

# Generated at 2022-06-13 16:00:16.303051
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor("red") == u'31'
    assert parsecolor("RED") == u'31'
    assert parsecolor("navy") == u'34'
    assert parsecolor("darkgray") == u'1;30'
    assert parsecolor("lightred") == u'1;31'
    assert parsecolor("yellow") == u'1;33'
    assert parsecolor("green") == u'32'
    assert parsecolor("darkgreen") == u'0;32'
    assert parsecolor("cyan") == u'36'
    assert parsecolor("purple") == u'35'
    assert parsecolor("magenta") == u'1;35'
    assert parsecolor("blue") == u'34'

# Generated at 2022-06-13 16:00:25.099131
# Unit test for function colorize
def test_colorize():
    color = None

    # reset to default
    print(u"\033[0mRESET")

    # Print a list of all supported colors
    print(u"All colors:")
    for i in range(8):
        for j in range(30, 38):
            print(u"\033[%d;%dm%d;%d\033[0m" % (i, j, i, j))

    # Print a list of all supported formats
    print(u"\nAll formats:")
    for i in range(1, 9):
        print(u"\033[3%dm%d\033[0m" % (i, i))

    print(u"\nYou should see four colors below:")
    print(colorize(u"x", 0, color))

# Generated at 2022-06-13 16:00:34.901090
# Unit test for function parsecolor
def test_parsecolor():
    result = parsecolor("blue")
    assert result == C.COLOR_CODES["blue"]
    assert result == u'34'
    result = parsecolor("green")
    assert result == C.COLOR_CODES["green"]
    assert result == u'32'
    result = parsecolor("rgb255255255")
    assert result == u'38;5;15'
    result = parsecolor("rgb255000255")
    assert result == u'38;5;5'
    result = parsecolor("rgb255000255")
    assert result == u'38;5;5'
    result = parsecolor("rgb0255255")
    assert result == u'38;5;11'
    result = parsecolor("rgb255255000")

# Generated at 2022-06-13 16:00:40.260685
# Unit test for function stringc
def test_stringc():
    # We use `ansible-config` for this testing because it's always
    # available and leans on `pretty`.
    from ansible.cli.config import AnsibleConfigCLI
    args = {'_out': sys.stdout, '_err': sys.stderr}
    config = AnsibleConfigCLI(args)
    config._output_style = 'default'
    config.run()



# Generated at 2022-06-13 16:00:44.503180
# Unit test for function hostcolor
def test_hostcolor():
    assert ANSIBLE_COLOR
    assert hostcolor('host1', {'failures': 1, 'unreachable': 0, 'changed': 0}, color=False) == u"%-26s" % 'host1'
    assert hostcolor('host1', {'failures': 0, 'unreachable': 0, 'changed': 0}) == u"%-37s" % stringc('host1', 'green')



# Generated at 2022-06-13 16:00:55.664972
# Unit test for function stringc
def test_stringc():
    class args:
        def __init__(self):
            self.force_color = False
    options = args()
    C.ANSIBLE_FORCE_COLOR = options.force_color

    print(stringc("test", "green"))
    print(stringc("test", "red"))
    print(stringc("test", "blue"))
    print(stringc("test", "cyan"))
    print(stringc("test", "magenta"))



# Generated at 2022-06-13 16:01:05.768600
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor('black') == u'38;5;0'
    assert parsecolor('blue') == u'38;5;4'
    assert parsecolor('brightgreen') == u'38;5;2'
    assert parsecolor('brightpurple') == u'38;5;13'
    assert parsecolor('cyan') == u'38;5;6'
    assert parsecolor('darkgreen') == u'38;5;22'
    assert parsecolor('darkgrey') == u'38;5;8'
    assert parsecolor('darkred') == u'38;5;1'
    assert parsecolor('green') == u'38;5;10'
    assert parsecolor('lightblue') == u'38;5;12'

# Generated at 2022-06-13 16:01:11.961059
# Unit test for function colorize
def test_colorize():
    assert colorize('ok', 0, C.COLOR_OK) == u"ok=0   "
    assert colorize('failed', 1, C.COLOR_ERROR) == u"failed=1  "
    assert colorize('changed', 0, C.COLOR_CHANGED) == u"changed=0 "
    assert colorize('unreachable', 0, C.COLOR_UNREACHABLE) == u"unreachable=0 "

# Generated at 2022-06-13 16:01:16.812999
# Unit test for function stringc
def test_stringc():
    """Unit test of function stringc"""
    assert stringc(u'foo', u'green') == u'\033[32mfoo\033[0m'
    assert stringc(u'foo', u'lightgreen') == u'\033[92mfoo\033[0m'
    assert stringc(u'foo', u'color1') == u'\033[38;5;1mfoo\033[0m'
    assert stringc(u'foo', u'rgb000') == u'\033[38;5;16mfoo\033[0m'
    assert stringc(u'foo', u'rgb255') == u'\033[38;5;231mfoo\033[0m'

# Generated at 2022-06-13 16:01:26.852511
# Unit test for function hostcolor
def test_hostcolor():
    # Test for ANSIBLE_COLOR = False
    assert hostcolor('bogus', {'failures': 0, 'unreachable': 0, 'changed': 0}, color=True) == '%-26s' % 'bogus'

    # Test for ANSIBLE_COLOR = True
    ANSIBLE_COLOR = True
    # OK
    assert hostcolor('bogus', {'failures': 0, 'unreachable': 0, 'changed': 0}, color=True) == "%s" % stringc('bogus', 'blue')
    # Changed
    assert hostcolor('bogus', {'failures': 0, 'unreachable': 0, 'changed': 1}, color=True) == "%s" % stringc('bogus', 'yellow')
    # Failed

# Generated at 2022-06-13 16:01:35.836067
# Unit test for function hostcolor
def test_hostcolor():
    fake_stats = dict(
        ok=2,
        changed=0,
        unreachable=0,
        failures=0,
    )
    ok_host = hostcolor('ok.example.com', fake_stats)
    assert ok_host == 'ok.example.com'
    assert isinstance(ok_host, unicode)

    failed_host = hostcolor('failed.example.com', dict(
        ok=0,
        changed=1,
        unreachable=0,
        failures=0,
    ))
    assert failed_host == u"\033[91mfailed.example.com\033[0m"
    assert isinstance(failed_host, unicode)


# Generated at 2022-06-13 16:01:44.732863
# Unit test for function stringc
def test_stringc():
    """ my ansible.utils unit test class """
    red = "red"
    blue = "blue"
    white = "white"
    reset = "reset"
    print(stringc("White text", white))
    print(stringc("Red background", red, True))
    print(stringc("Blue text on red background", blue))
    print(stringc("Reset text", reset))
    print(stringc("Red text", red))
    print(stringc("Blue text", blue))
    print(stringc("Reset text", reset))
    print(stringc("White text", white))

# Generated at 2022-06-13 16:01:54.624559
# Unit test for function hostcolor
def test_hostcolor():
    host = 'test_host'
    stats = {
        'ok': 3928,
        'changed': 1,
        'unreachable': 2,
        'failures': 3,
        'skipped': 160,
    }

    print("%-30s %-30s %-30s" % (
        hostcolor(host, stats, False),
        hostcolor(host, {
                    'ok': 1,
                    'changed': 0,
                    'unreachable': 0,
                    'failures': 0,
                    'skipped': 0}),
        hostcolor(host, {
                    'ok': 0,
                    'changed': 1,
                    'unreachable': 0,
                    'failures': 0,
                    'skipped': 0})
    ))


# Generated at 2022-06-13 16:02:03.401718
# Unit test for function parsecolor
def test_parsecolor():
    assert(parsecolor('red') == '31')
    assert(parsecolor('red') != '32')
    assert(parsecolor('red') == '31')
    assert(parsecolor('green') == '32')
    assert(parsecolor('green') != '31')
    assert(parsecolor('green') == '32')
    assert(parsecolor('yellow') == '33')
    assert(parsecolor('blue') == '34')
    assert(parsecolor('cyan') == '36')
    assert(parsecolor('white') == '37')
    assert(parsecolor('black') == '30')
    assert(parsecolor('default') == '39')
    assert(parsecolor('rgb2551020') == '38;5;196')
# --- end "pretty"

# Generated at 2022-06-13 16:02:06.538050
# Unit test for function stringc
def test_stringc():
    assert stringc('text', 'blue') == u'\033[0;34mtext\033[0m'
    assert stringc('text', 'blue', True) == u'\001\033[0;34m\002text\001\033[0m\002'



# Generated at 2022-06-13 16:02:22.429425
# Unit test for function hostcolor
def test_hostcolor():
    # Assume ANSIBLE_COLOR
    host = u"testhost"
    # No failures or unreachable
    stats = {'changed': 2, 'ok': 2, 'failures': 0, 'unreachable': 0}
    assert hostcolor(host, stats, True) == (u"%-37s" % stringc(host, C.COLOR_CHANGED))

    # failures ignored unreachable
    stats = {'changed': 0, 'ok': 2, 'failures': 2, 'unreachable': 0}
    assert hostcolor(host, stats, True) == (u"%-37s" % stringc(host, C.COLOR_ERROR))

    # failures and unreachable
    stats = {'changed': 0, 'ok': 2, 'failures': 2, 'unreachable': 1}

# Generated at 2022-06-13 16:02:28.896519
# Unit test for function stringc
def test_stringc():
    color = 'red'
    text = 'foo'
    assert stringc(text, color) == u"\033[%sm%s\033[0m" % (parsecolor(color), text)
    assert stringc(text, color, wrap_nonvisible_chars=True) == u"\001\033[%sm\002%s\001\033[0m\002" % (parsecolor(color), text)
    assert stringc(text, 'rgb123') == u"\033[38;5;%dm%s\033[0m" % (16 + 36 * 1 + 6 * 2 + 3, text)
    assert stringc(text, 'gray100') == u"\033[38;5;%dm%s\033[0m" % (232 + 100, text)

# Generated at 2022-06-13 16:02:40.453873
# Unit test for function stringc
def test_stringc():
    """Unit test for function stringc"""
    import sys
    sys.stderr.write(u"Test: stringc() - ")

# Generated at 2022-06-13 16:02:45.784488
# Unit test for function stringc
def test_stringc():
    import sys
    if sys.version_info < (2, 6):
        return

    from ansible.compat.tests import unittest

    class TestStringc(unittest.TestCase):
        def test_stringc_special_char(self):
            color = 'yellow'
            text = u'\u00012.4\u0001test'
            self.assertEqual(stringc(text, color), u'\n'.join([u"\033[33m\u00012.4\u0001test\033[0m"]))

        def test_stringc_non_ascii(self):
            color = 'yellow'
            text = u'\u00e5'

# Generated at 2022-06-13 16:02:55.700203
# Unit test for function hostcolor
def test_hostcolor():
    if not ANSIBLE_COLOR:
        return

    from ansible import constants as C
    from ansible.module_utils.compat.collections import (MutableMapping, Mapping)

    class Stats(MutableMapping):
        def __init__(self, d={}):
            self._store = d

        def __getitem__(self, key):
            return self._store[key]

        def __setitem__(self, key, value):
            self._store[key] = value

        def __delitem__(self, key):
            del self._store[key]

        def __iter__(self):
            return iter(self._store)

        def __len__(self):
            return len(self._store)


# Generated at 2022-06-13 16:03:05.233168
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor('red') == u'31'
    assert parsecolor('green') == u'32'
    assert parsecolor('yellow') == u'33'
    assert parsecolor('blue') == u'34'
    assert parsecolor('magenta') == u'35'
    assert parsecolor('cyan') == u'36'
    assert parsecolor('white') == u'37'
    assert parsecolor('black') == u'30'
    assert parsecolor('color0') == u'38;5;0'
    assert parsecolor('color1') == u'38;5;1'
    assert parsecolor('color2') == u'38;5;2'
    assert parsecolor('color3') == u'38;5;3'
    assert parsecolor('color4')

# Generated at 2022-06-13 16:03:15.386999
# Unit test for function hostcolor
def test_hostcolor():
    # Returned values should be a string followed by 26 - len(host) spaces
    assert re.match(r"^[a-z]+\ +$", hostcolor("host", {}))
    # Returned values should be a string of 37 characters
    assert len(hostcolor("host", {"failures": 1, "changed": 0, "unreachable": 0, "ok": 0})) == 37
    assert len(hostcolor("host", {"failures": 0, "changed": 1, "unreachable": 0, "ok": 0})) == 37
    assert len(hostcolor("host", {"failures": 0, "changed": 0, "unreachable": 1, "ok": 0})) == 37
    assert len(hostcolor("host", {"failures": 0, "changed": 0, "unreachable": 0, "ok": 1}))

# Generated at 2022-06-13 16:03:25.220347
# Unit test for function parsecolor
def test_parsecolor():
        result = parsecolor('blue')
        assert result == '34', result

        result = parsecolor('red')
        assert result == '31', result

        result = parsecolor('green')
        assert result == '32', result

        result = parsecolor('white')
        assert result == '37', result

        result = parsecolor('rgb255')
        assert result == '38;5;231', result

        result = parsecolor('rgb500')
        assert result == '38;5;231', result

        result = parsecolor('rgb220')
        assert result == '38;5;59', result

        result = parsecolor('rgb127')
        assert result == '38;5;59', result

        result = parsecolor('rgb128')

# Generated at 2022-06-13 16:03:26.382444
# Unit test for function hostcolor

# Generated at 2022-06-13 16:03:29.613881
# Unit test for function stringc
def test_stringc():
    print(stringc("Colors\nColors\nColors", 'red'))
    print(stringc("Colors\nColors\nColors", 'red', True))



# Generated at 2022-06-13 16:03:43.899695
# Unit test for function parsecolor
def test_parsecolor():
    def str_color(color):
        return "\\x1b[38;5;%dm" % color

    def test(name, input, expected):
        if parsecolor(input) == str_color(expected):
            print("PASS", name)
        else:
            print("FAIL", name)

    test("color number", "color197", 197)
    test("rgb color short", "rgb313", 40)
    test("gray number", "gray7", 244)

# ---  end "pretty"



# Generated at 2022-06-13 16:03:51.808016
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor(u'blue') == u'34'
    assert parsecolor(u'rgb100') == u'38;5;39'
    assert parsecolor(u'rgb512') == u'38;5;46'
    assert parsecolor(u'rgb255') == u'38;5;231'
    assert parsecolor(u'gray1') == u'38;5;232'
    assert parsecolor(u'color8') == u'38;5;8'
    assert parsecolor(u'color04') == u'38;5;4'
    assert parsecolor(u'color100') == u'38;5;100'


# --- end "pretty" ---



# Generated at 2022-06-13 16:04:03.590692
# Unit test for function stringc

# Generated at 2022-06-13 16:04:08.091469
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('localhost', {'changed': 0, 'failures': 0, 'ok': 1, 'skipped': 0, 'unreachable': 0}) == u'localhost                 \n'
    assert hostcolor('localhost', {'changed': 0, 'failures': 0, 'ok': 1, 'skipped': 0, 'unreachable': 1}) == u'\x1b[31mlocalhost                 \x1b[0m\n'
    assert hostcolor('localhost', {'changed': 1, 'failures': 0, 'ok': 1, 'skipped': 0, 'unreachable': 0}) == u'\x1b[33mlocalhost                 \x1b[0m\n'

# Generated at 2022-06-13 16:04:19.557873
# Unit test for function stringc
def test_stringc():
    for color in ('black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', 'rgb888', 'rgb444', 'rgb000', 'rgb555'):
        print(u"%s: %s" % (color, stringc('test', color)))

# --- end "pretty"



# Generated at 2022-06-13 16:04:28.522334
# Unit test for function colorize
def test_colorize():
    # Tests with ANSIBLE_COLOR=True
    if ANSIBLE_COLOR:
        assert colorize('ok', 15, 'green') == u"ok=15 "
        assert colorize('changed', -1, 'yellow') == u"changed=-1 "
        assert colorize('failed', 0, 'red') == u"failed=0  "
        # Tests with ANSIBLE_COLOR=False
    else:
        assert colorize('ok', 15, 'green') == u"ok=15  "
        assert colorize('changed', -1, 'yellow') == u"changed=-1 "
        assert colorize('failed', 0, 'red') == u"failed=0  "



# Generated at 2022-06-13 16:04:36.556366
# Unit test for function hostcolor

# Generated at 2022-06-13 16:04:44.292062
# Unit test for function hostcolor
def test_hostcolor():
    fake_stats = dict(failures=0, unreachable=0, changed=0)
    assert hostcolor("foo", fake_stats) == "foo                          "

    fake_stats['failures'] = 42
    fake_stats['unreachable'] = 0
    assert hostcolor("foo", fake_stats) == stringc("foo                          ", C.COLOR_ERROR)

    fake_stats['failures'] = 0
    fake_stats['unreachable'] = 42
    assert hostcolor("foo", fake_stats) == stringc("foo                          ", C.COLOR_ERROR)

    fake_stats['failures'] = 0
    fake_stats['unreachable'] = 0
    fake_stats['changed'] = 42
    assert hostcolor("foo", fake_stats) == stringc("foo                          ", C.COLOR_CHANGED)

# Generated at 2022-06-13 16:04:55.239560
# Unit test for function colorize
def test_colorize():
    print(colorize(u'ok', 0, C.COLOR_OK))
    print(colorize(u'changed', 0, C.COLOR_CHANGED))
    print(colorize(u'unreachable', 0, C.COLOR_UNREACHABLE))
    print(colorize(u'failed', 0, C.COLOR_ERROR))

    ANSIBLE_COLOR = True
    print(colorize(u'ok', 0, C.COLOR_OK))
    print(colorize(u'changed', 0, C.COLOR_CHANGED))
    print(colorize(u'unreachable', 0, C.COLOR_UNREACHABLE))
    print(colorize(u'failed', 0, C.COLOR_ERROR))

    print(colorize(u'ok', 123, C.COLOR_OK))

# Generated at 2022-06-13 16:05:02.725716
# Unit test for function hostcolor
def test_hostcolor():
    class FakeOptions(object):
        def __init__(self):
            self.nocolor = False

    class FakeStats(object):
        def __init__(self, failures, unreachable, changed):
            self.failures = failures
            self.unreachable = unreachable
            self.changed = changed

    options = FakeOptions()
    stats = FakeStats(0,0,0)

    assert hostcolor("testhost", stats, True) == u"testhost             "
    assert hostcolor("testhost", stats, False) == u"testhost             "

    stats.failures = 1
    assert hostcolor("testhost", stats, True) == u"testhost             "

    options.nocolor = True
    assert hostcolor("testhost", stats, True) == u"testhost             "



# Generated at 2022-06-13 16:05:19.376002
# Unit test for function colorize
def test_colorize():
    """Ensure that the colorize function returns the proper strings."""
    # set up some color codes and leads
    color_codes = {
        'blue': '34',
        'red': '31',
        'green': '32',
        'yellow': '33',
        'gray': '37',
        'magenta': '35',
        'cyan': '36',
    }
    leads = [u'=>', u'@@', u'**']

    # determine the terminal width and set the color output width
    # to two less than that so that the color codes don't wrap
    terminal_width = int(os.environ.get('COLUMNS', 80))
    color_width = terminal_width - 2

    # loop through each color and lead combination and assert
    # the expected value

# Generated at 2022-06-13 16:05:20.139034
# Unit test for function colorize
def test_colorize():
    return



# Generated at 2022-06-13 16:05:30.433828
# Unit test for function stringc
def test_stringc():
    """Test the stringc function"""
    assert stringc('test', 'blue') == '\033[34mtest\033[0m'
    assert stringc('test', 'rgb255') == '\033[38;5;15mtest\033[0m'
    assert stringc('test', 'rgb333') == '\033[38;5;60mtest\033[0m'
    assert stringc('test', 'rgb000') == '\033[38;5;16mtest\033[0m'
    assert stringc('test', 'gray9') == '\033[38;5;241mtest\033[0m'

# --- end "pretty"


# we'll be using some of the pretty stuff, so let's get the color stuff setup
# see if we are using a type of terminal that supports AN

# Generated at 2022-06-13 16:05:40.777748
# Unit test for function stringc
def test_stringc():
    reset = "\033[0m"

    print(u"TESTING STRINGC() FOR COLOUR OUTPUT - YOU SHOULD SEE 6 LINES BELOW")

    print(u'12345678901234567890')
    print(stringc('black', 'black') + reset)
    print(stringc('red', 'red') + reset)
    print(stringc('green', 'green') + reset)
    print(stringc('yellow', 'yellow') + reset)
    print(stringc('blue', 'blue') + reset)
    print(stringc('magenta', 'magenta') + reset)
    print(stringc('cyan', 'cyan') + reset)
    print(stringc('white', 'white') + reset)
    print(u'12345678901234567890')

# Generated at 2022-06-13 16:05:44.657107
# Unit test for function stringc
def test_stringc():
    assert stringc(u"hello", u"red", wrap_nonvisible_chars=False) == "\033[31mhello\033[0m"
    assert stringc(u"hello", u"red", wrap_nonvisible_chars=True) == "\001\033[31m\002hello\001\033[0m\002"
    print(u"✔")



# Generated at 2022-06-13 16:05:51.831136
# Unit test for function stringc
def test_stringc():
    assert(stringc("hello", "green") == "\033[32mhello\033[0m")
    assert(stringc("hello\nthere", "green") == "\033[32mhello\033[0m\n\033[32mt here\033[0m")
    assert(stringc("hello\nthere", "color1") == "\033[38;5;1mhello\033[0m\n\033[38;5;1mt here\033[0m")
    assert(stringc("hello\nthere", "rgb124") == "\033[38;5;124mhello\033[0m\n\033[38;5;124mt here\033[0m")
    assert(stringc("hello", "rgb000") == "\033[38;5;16mhello\033[0m")
   

# Generated at 2022-06-13 16:06:00.192941
# Unit test for function stringc
def test_stringc():
    """
    >>> test_stringc()
    (u'\x1b[38;5;124mtest string\x1b[0m', u'test string')
    """
    if ANSIBLE_COLOR:
        color_on_string = stringc('test string', 'lightred')
        assert color_on_string == u"\x1b[38;5;124mtest string\x1b[0m"

    color_off_string = stringc('test string', 'lightred', False)
    assert color_off_string == u"test string"



# Generated at 2022-06-13 16:06:10.242173
# Unit test for function stringc
def test_stringc():
    assert stringc('test', 'red', False) == u'\033[31mtest\033[0m'
    assert stringc('test', 'red', True) == u'\001\033[31m\002test\001\033[0m\002'
    assert stringc('test', 'rgb255000', False) == u'\033[38;5;196mtest\033[0m'
    assert stringc('test', 'rgb255000', True) == u'\001\033[38;5;196m\002test\001\033[0m\002'

# --- end "pretty"

# Generated at 2022-06-13 16:06:18.771152
# Unit test for function hostcolor
def test_hostcolor():
    stats_ok = {
        'failures': 0,
        'unreachable': 0,
        'changed': 0
    }
    stats_fail = {
        'failures': 1,
        'unreachable': 0,
        'changed': 0
    }
    stats_unreachable = {
        'failures': 0,
        'unreachable': 2,
        'changed': 0
    }
    stats_changed = {
        'failures': 0,
        'unreachable': 0,
        'changed': 1
    }
    stats_failed_unreachable = {
        'failures': 1,
        'unreachable': 2,
        'changed': 0
    }

# Generated at 2022-06-13 16:06:27.899977
# Unit test for function stringc
def test_stringc():
    class args:
        nocolor = False
    global ANSIBLE_COLOR
    try:
        print(u"\x1b[6n")  # request cursor position
        old_stty = sys.stdin.readline()  # read response
    except:
        old_stty = None
    for ANSIBLE_COLOR in [True, False]:
        for color in C.COLOR_CODES:
            try:
                print(u"%s: %s" % (color, stringc(u"foo", color, wrap_nonvisible_chars=True)))
            except:
                pass

# Generated at 2022-06-13 16:06:44.852159
# Unit test for function stringc
def test_stringc():
    import ansible.constants as C
    colors = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', 'default']
    colors.extend(['color%d' % n for n in range(8)])
    colors.extend(['rgb%d%d%d' % (r, g, b) for r in range(6) for g in range(6) for b in range(6)])
    colors.extend(['gray%d' % n for n in range(23)])
    colors.extend(['darkgray', 'brightblack', 'brightred', 'brightgreen', 'brightyellow', 'brightblue', 'brightmagenta', 'brightcyan', 'brightwhite'])


# Generated at 2022-06-13 16:06:49.759154
# Unit test for function colorize
def test_colorize():
    assert colorize("foo", 0, "blue") == "foo=0   "
    assert colorize("foo", 0, None) == "foo=0   "
    assert colorize("foo", 1234, "blue") == "foo=1234"
    assert colorize("foo", 1234, None) == "foo=1234"

# --- end "pretty"



# Generated at 2022-06-13 16:06:55.838614
# Unit test for function colorize
def test_colorize():
    # Note: unit test function must be named 'test_*'
    lead = 'foo'
    num = 42
    assert colorize(lead, num, 'blue') == 'foo=42  '
    assert colorize(lead, num, 'none') == 'foo=42  '
    assert colorize(lead, num, None) == 'foo=42  '
    assert colorize(lead, num, 'invalid') == 'foo=42  '

# end "pretty"
# ---

# Generated at 2022-06-13 16:06:57.803617
# Unit test for function hostcolor
def test_hostcolor():
    class _:
        def __init__(self):
            pass

    stats = _()
    stats.failures = 0
    

# Generated at 2022-06-13 16:07:09.470416
# Unit test for function stringc

# Generated at 2022-06-13 16:07:12.882268
# Unit test for function colorize
def test_colorize():
    if ANSIBLE_COLOR:
        assert colorize(u"lead", 0, u"red") == u"\033[31mlead=0   \033[0m"
    else:
        assert colorize(u"lead", 0, u"red") == u"lead=0   "



# Generated at 2022-06-13 16:07:23.376602
# Unit test for function hostcolor
def test_hostcolor():
    host = 'testhost'
    stats = {}
    for key in ('changed', 'failures', 'ok', 'skipped', 'unreachable'):
        stats[key] = 0
    print(hostcolor(host, stats))
    stats['changed'] = 1
    print(hostcolor(host, stats))
    stats['failures'] = 1
    print(hostcolor(host, stats))
    stats['unreachable'] = 1
    print(hostcolor(host, stats))

# --- end of pretty code

# current legacy / backwards compatibility code
# this should be deprecated and moved elsewhere
# if possible

if C.ANSIBLE_NOCOLOR:
    ANSIBLE_COLOR = False
elif not hasattr(sys.stdout, 'isatty') or not sys.stdout.isatty():
    AN

# Generated at 2022-06-13 16:07:29.644911
# Unit test for function stringc
def test_stringc():
    """Test function stringc."""
    assert stringc('{0}', 'black') == u'\033[30m{0}\033[0m'
    assert stringc('{0}', 'red') == u'\033[31m{0}\033[0m'
    assert stringc('{0}', 'green') == u'\033[32m{0}\033[0m'
    assert stringc('{0}', 'yellow') == u'\033[33m{0}\033[0m'
    assert stringc('{0}', 'blue') == u'\033[34m{0}\033[0m'
    assert stringc('{0}', 'magenta') == u'\033[35m{0}\033[0m'
    assert stringc('{0}', 'cyan') == u

# Generated at 2022-06-13 16:07:39.402039
# Unit test for function hostcolor
def test_hostcolor():

    host1 = 'localhost'
    host2 = 'somehost'
    stats = {'pending': 0, 'ok': 0, 'changed': 0, 'unreachable': 0, 'failures': 0}

    host1_green = hostcolor(host1, stats, True)
    host2_green = hostcolor(host2, stats, True)

    assert(host1_green == host2_green)

    stats['changed'] = 10
    host1_yellow = hostcolor(host1, stats, True)
    host2_yellow = hostcolor(host2, stats, True)

    assert(host1_yellow == host2_yellow)

    stats['failures'] = 10
    host1_red = hostcolor(host1, stats, True)
    host2_red = hostcolor(host2, stats, True)

   

# Generated at 2022-06-13 16:07:45.332732
# Unit test for function hostcolor
def test_hostcolor():
    stats = {
        'ok': 1,
        'changed': 1,
        'unreachable': 1,
        'failures': 1
    }
    host = 'testhost'

    assert 'testhost' == hostcolor(host, stats, False)

    assert '\n'.join([u'\033[0;32m', host, u'\033[0m']) == hostcolor(host, stats)
    assert '\n'.join([u'\033[1;31m', host, u'\033[0m']) == hostcolor(host, dict(stats, failures=1))
    assert '\n'.join([u'\033[1;33m', host, u'\033[0m']) == hostcolor(host, dict(stats, changed=1))



# Generated at 2022-06-13 16:08:12.121457
# Unit test for function stringc
def test_stringc():
    u"""Test stringc()."""
    assert stringc(u"foo", u"RED") == u'\033[91mfoo\033[0m', \
        u'Incorrect formatting of RED'
    assert stringc(u"foo", u"blue") == u'\033[94mfoo\033[0m', \
        u'Incorrect formatting of blue'
    assert stringc(u"foo", u"BOLD") == u'\033[1mfoo\033[0m', \
        u'Incorrect formatting of BOLD'
    assert stringc(u"foo", u"BLINK") == u'\033[5mfoo\033[0m', \
        u'Incorrect formatting of BLINK'

# Generated at 2022-06-13 16:08:19.599399
# Unit test for function hostcolor
def test_hostcolor():
    stats = dict(failures=0, unreachable=0, changed=0)
    print(hostcolor('testhost1', stats, color=False))
    print(hostcolor('testhost2.example.com', stats, color=True))
    stats['changed'] = 1
    print(hostcolor('testhost3', stats, color=True))
    stats['failed'] = 1
    print(hostcolor('testhost4', stats, color=True))
    stats['unreachable'] = 1
    print(hostcolor('testhost5', stats, color=True))



# Generated at 2022-06-13 16:08:25.417453
# Unit test for function hostcolor
def test_hostcolor():
    stdout_orig = sys.stdout
    sys.stdout = open('/dev/null', 'w')
    stats = {'failures': 0, 'unreachable': 0, 'changed': 0}
    assert u"%-26s" % "foo" == hostcolor("foo", stats, color=False)
    stats['failures'] = 1
    sys.stdout = open('/dev/null')
    assert u"%-26s" % "foo" != hostcolor("foo", stats, color=False)
    sys.stdout = stdout_orig



# Generated at 2022-06-13 16:08:34.255401
# Unit test for function stringc
def test_stringc():
    print(u"Test 1: Default style.")
    print(stringc(u"This is a test.", u"green"))

    print(u"Test 2: Bright style.")
    print(stringc(u"This is a test.", u"green,bold"))

    print(u"Test 3: Underline style.")
    print(stringc(u"This is a test.", u"green,underline"))

    print(u"Test 4: Unix colors.")
    print(stringc(u"This is a test.", u"blue"))
    print(stringc(u"This is a test.", u"blue,bold"))
    print(stringc(u"This is a test.", u"blue,underline"))
    print(stringc(u"This is a test.", u"red"))

# Generated at 2022-06-13 16:08:40.294686
# Unit test for function parsecolor
def test_parsecolor():
    '''Unit test for function parsecolor'''
    test_cases = {
        'cyan': '36',
        'color7': '38;5;7',
        'rgb123': '38;5;24',
        'rgb444': '38;5;116',
        'rgb555': '38;5;127',
        'rgb666': '38;5;138',
        'rgb210': '38;5;111',
        'gray0': '38;5;232',
        'gray9': '38;5;241',
    }
    for test_case in test_cases:
        assert parsecolor(test_case) == test_cases[test_case]

# Generated at 2022-06-13 16:08:50.866807
# Unit test for function hostcolor
def test_hostcolor():
    stats = dict(failures=0, unreachable=0, changed=0)
    case = hostcolor('localhost', stats)
    assert case == '%-37s' % u"\n".join(u"\033[0;32m%s\033[0m" % t for t in u'localhost'.split(u'\n'))
    stats = dict(failures=1, unreachable=0, changed=0)
    case = hostcolor('localhost', stats)
    assert case == '%-37s' % u"\n".join(u"\033[1;31m%s\033[0m" % t for t in u'localhost'.split(u'\n'))
    stats = dict(failures=0, unreachable=1, changed=0)
    case = hostcolor('localhost', stats)

# Generated at 2022-06-13 16:09:01.242212
# Unit test for function stringc
def test_stringc():
    assert stringc("foo", "green") == "\x1b[32mfoo\x1b[0m"
    assert stringc("foo", "lightgreen") == "\x1b[92mfoo\x1b[0m"
    assert stringc("foo", "blue") == "\x1b[34mfoo\x1b[0m"
    assert stringc("foo", "rgb255255255") == "\x1b[97mfoo\x1b[0m"
    assert stringc("foo", "rgb000255000") == "\x1b[92mfoo\x1b[0m"
    assert stringc("foo", "rgb000255255") == "\x1b[96mfoo\x1b[0m"

# Generated at 2022-06-13 16:09:12.429444
# Unit test for function hostcolor
def test_hostcolor():
    # test with a UNREACHABLE host
    stats = {
        'failures': 0,
        'unreachable': 1,
    }
    assert hostcolor('not.localhost', stats) == stringc('not.localhost', C.COLOR_ERROR)
    # test with a FAILED host
    stats = {
        'failures': 1,
        'unreachable': 0,
    }
    assert hostcolor('not.localhost', stats) == stringc('not.localhost', C.COLOR_ERROR)
    # test with a CHANGED host
    stats = {
        'changed': 1,
    }
    assert hostcolor('not.localhost', stats) == stringc('not.localhost', C.COLOR_CHANGED)
    # test with an OK host
    stats = {
        'changed': 0,
    }


# Generated at 2022-06-13 16:09:20.874700
# Unit test for function stringc
def test_stringc():
    assert stringc("'foo'", 'white') == "\033[0m'foo'\033[0m"
    assert stringc("'foo'", 'red') == "\033[31m'foo'\033[0m"
    assert stringc("'foo'", 'green') == "\033[32m'foo'\033[0m"
    assert stringc("'foo'", 'yellow') == "\033[33m'foo'\033[0m"
    assert stringc("'foo'", 'blue') == "\033[34m'foo'\033[0m"
    assert stringc("'foo'", 'magenta') == "\033[35m'foo'\033[0m"
    assert stringc("'foo'", 'cyan') == "\033[36m'foo'\033[0m"
   

# Generated at 2022-06-13 16:09:30.230629
# Unit test for function hostcolor
def test_hostcolor():
    p1 = hostcolor('host1', dict(changed=0, failures=0, unreachable=0), True)
    p2 = hostcolor('host1', dict(changed=0, failures=0, unreachable=0), False)
    p3 = hostcolor('host2', dict(changed=1, failures=0, unreachable=0), True)
    p4 = hostcolor('host2', dict(changed=1, failures=0, unreachable=0), False)
    p5 = hostcolor('host3', dict(changed=0, failures=1, unreachable=0), True)
    p6 = hostcolor('host3', dict(changed=0, failures=1, unreachable=0), False)
    p7 = hostcolor('host4', dict(changed=0, failures=0, unreachable=1), True)
    p8