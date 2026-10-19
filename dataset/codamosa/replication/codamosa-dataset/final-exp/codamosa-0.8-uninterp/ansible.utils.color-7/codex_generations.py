

# Generated at 2022-06-13 15:59:42.916326
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor("blue") == "34"
    assert parsecolor("Blue") == "34"
    assert parsecolor("bright blue") == "94"
    assert parsecolor("bright Blue") == "94"
    assert parsecolor("BLUE") == "94"
    assert parsecolor("red") == "31"
    assert parsecolor("on red") == "41"
    assert parsecolor("red on white") == "41;37"
    assert parsecolor("red on_white") == "41;37"
    assert parsecolor("red on_bright white") == "101;37"
    assert parsecolor("red on bright white") == "101;37"
    assert parsecolor("red on bright_white") == "101;37"

# Generated at 2022-06-13 15:59:53.185564
# Unit test for function stringc
def test_stringc():
    class TC:
        """Test Cases"""
        def __init__(self, inp, outp):
            self.inp = inp
            self.outp = outp

    tc = []
    tc.append(TC(('hello', 'red'), u'\033[31mhello\033[0m'))
    tc.append(TC(('hello', 'blue'), u'\033[34mhello\033[0m'))
    tc.append(TC(('hello', 'color1'), u'\033[38;5;1mhello\033[0m'))
    tc.append(TC(('hello', 'rgb255255255'), u'\033[38;5;15mhello\033[0m'))

# Generated at 2022-06-13 15:59:56.709503
# Unit test for function colorize
def test_colorize():
    print("Testing colorize()")
    colors = ('black', 'dark gray', 'blue', 'light blue', 'green',
              'light green', 'cyan', 'light cyan', 'red', 'light red',
              'purple', 'light purple', 'brown', 'yellow', 'light gray',
              'white')
    for color in colors:
        print("  %s %s %s" % (colorize("text", 0, color),
                              colorize("text", 0, color),
                              colorize("text", 0, color)))


# Generated at 2022-06-13 16:00:04.900819
# Unit test for function stringc
def test_stringc():
    expected_results = {'black': u'\033[30;1mfoo\033[0m',
                        'white': u'\033[37;1mfoo\033[0m',
                        'red': u'\033[31;1mfoo\033[0m',
                        'green': u'\033[32;1mfoo\033[0m',
                        'yellow': u'\033[33;1mfoo\033[0m',
                        'blue': u'\033[34;1mfoo\033[0m',
                        'magenta': u'\033[35;1mfoo\033[0m',
                        'cyan': u'\033[36;1mfoo\033[0m'}
    for color in expected_results:
        result = stringc('foo', color)

# Generated at 2022-06-13 16:00:05.935678
# Unit test for function stringc
def test_stringc():
    # TODO: Implement this.
    pass


# Generated at 2022-06-13 16:00:15.656537
# Unit test for function parsecolor
def test_parsecolor():
    import subprocess

    def show(color):
        matches = re.match(r"color(?P<color>[0-9]+)"
                           r"|(?P<rgb>rgb(?P<red>[0-5])(?P<green>[0-5])(?P<blue>[0-5]))"
                           r"|gray(?P<gray>[0-9]+)", color)
        if not matches:
            return subprocess.check_output(['echo', '-n', '\x1b[%sm%s\x1b[0m' % (C.COLOR_CODES[color], color)]).decode('utf-8')

# Generated at 2022-06-13 16:00:24.593675
# Unit test for function hostcolor
def test_hostcolor():
    from ansible.compat.six import StringIO
    f = StringIO()
    sys.stdout = f
    hostname = 'foohost'
    stats = {'failures': 0,
             'unreachable': 0,
             'changed': 0,
             'ok': 1,
             'dark': 0}

    hostcolor(hostname, stats, True)
    output = f.getvalue()
    assert u'\u001b[0m%-37s' % hostname in output

    stats = {'failures': 1,
             'unreachable': 0,
             'changed': 0,
             'ok': 0,
             'dark': 0}

    hostcolor(hostname, stats, True)
    output = f.getvalue()

# Generated at 2022-06-13 16:00:32.976607
# Unit test for function hostcolor
def test_hostcolor():
    from ansible.playbook.play_context import PlayContext
    import ansible.constants as C

    pc = PlayContext()
    # no color tests
    pc.remote_addr = None
    pc.remote_user = 'user'

    pc.hostvars = {'hostname':{}}
    pc.hostvars['hostname']['user'] = 'user'
    pc.hostvars['hostname']['inventory_hostname'] = 'hostname'
    pc.hostvars['hostname']['inventory_hostname_short'] = 'hostname'

    stats = dict(changed=0, failures=0, ok=0, skipped=0, unreachable=0)
    assert hostcolor('hostname', stats, False) == 'hostname            '


# Generated at 2022-06-13 16:00:43.207958
# Unit test for function hostcolor
def test_hostcolor():
    stats = {'failures' : 1, 'unreachable' : 0, 'changed' : 0}
    assert hostcolor('test', stats, True) == u'%s%-37s'%('\x1b[31m', u'test')

    stats = {'failures' : 0, 'unreachable' : 1, 'changed' : 0}
    assert hostcolor('test', stats, True) == u'%s%-37s'%('\x1b[31m', u'test')

    stats = {'failures' : 0, 'unreachable' : 0, 'changed' : 1}
    assert hostcolor('test', stats, True) == u'%s%-37s'%('\x1b[34m', u'test')


# Generated at 2022-06-13 16:00:53.958683
# Unit test for function hostcolor
def test_hostcolor():
    def runtest(input, output):
        rc = (hostcolor(input[0], input[1], color=True) == output)
        if not rc:
            print('hostcolor(%s, %s, color=True) expected %s, returned %s' % (input[0], input[1], output, hostcolor(input[0], input[1], color=True)))
        return rc


# Generated at 2022-06-13 16:01:06.933734
# Unit test for function hostcolor
def test_hostcolor():
    class Dummy: pass
    stats = Dummy()
    stats.failures = 0
    stats.unreachable = 0
    stats.changed = 0
    assert hostcolor("dummy_host", stats) == u"dummy_host                "
    stats.failures = 1
    assert hostcolor("dummy_host", stats) == u"dummy_host                "
    stats.unreachable = 1
    assert hostcolor("dummy_host", stats) == u"dummy_host                "
    stats.changed = 1
    assert hostcolor("dummy_host", stats) == u"dummy_host                "
    stats.changed = 0
    assert hostcolor("dummy_host", stats, color=False) == u"dummy_host                "
    stats.failures = 0
    stats.unreachable = 0

# Generated at 2022-06-13 16:01:16.678487
# Unit test for function parsecolor
def test_parsecolor():
    for color in (u'blue', u'bright cyan', u'yellow', u'bright white',
                  u'green', u'bright red'):
        assert(C.COLOR_CODES[color] == parsecolor(color))

    assert(u'38;5;129' == parsecolor(u'1'))
    assert(u'38;5;130' == parsecolor(u'2'))
    assert(u'38;5;131' == parsecolor(u'3'))
    assert(u'38;5;132' == parsecolor(u'4'))
    assert(u'38;5;133' == parsecolor(u'5'))
    assert(u'38;5;134' == parsecolor(u'6'))

# Generated at 2022-06-13 16:01:26.626068
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor('color0') == '38;5;0'
    assert parsecolor('color1') == '38;5;1'
    assert parsecolor('color9') == '38;5;9'
    assert parsecolor('color10') == '38;5;10'
    assert parsecolor('color232') == '38;5;232'
    assert parsecolor('color255') == '38;5;255'

    assert parsecolor('rgb000') == '38;5;0'
    assert parsecolor('rgb001') == '38;5;1'
    assert parsecolor('rgb009') == '38;5;9'
    assert parsecolor('rgb555') == '38;5;15'


# Generated at 2022-06-13 16:01:32.128614
# Unit test for function stringc
def test_stringc():
    """Tests for `stringc()`."""
    # We only test the RGB and gray syntaxes, which can't be tested
    # using the `colors` module.
    assert stringc('42', 'rgb255255255', False) == u'\033[1;38;5;231m42\033[0m'
    assert stringc('42', 'gray0', False) == u'\033[1;38;5;232m42\033[0m'



# Generated at 2022-06-13 16:01:40.066515
# Unit test for function stringc
def test_stringc():
    # Check all named colors
    for color in C.COLOR_CODES:
        out = stringc("This is %s" % color, color)
        print("%s color output: %s" % (color, out))
    # Check gray colors
    out = stringc("This is gray0", 'gray0')
    print("%s color output: %s" % (out, out))
    out = stringc("This is gray23", 'gray23')
    print("%s color output: %s" % (out, out))
    # Check rgb colors
    out = stringc("This is rgb123", 'rgb123')
    print("%s color output: %s" % (out, out))
    # Check color aliases
    out = stringc("This is bright purple", 'bright purple')

# Generated at 2022-06-13 16:01:49.287598
# Unit test for function hostcolor
def test_hostcolor():
    _inventory = {
        'all': {
            'hosts': [
                'localhost',
                'remotehost',
                'anotherhost',
                'darkhost',
            ]
        },
        'dark': {
            'hosts': [
                'darkhost',
            ]
        }
    }

# Generated at 2022-06-13 16:01:51.731709
# Unit test for function colorize
def test_colorize():
    assert colorize("foo", 0, None) == "foo=0   "

# end "pretty"
# ---

# Generated at 2022-06-13 16:02:01.313021
# Unit test for function hostcolor
def test_hostcolor():
    stats_array = [
        {'changed': 0, 'failures': 0, 'ok': 10, 'skipped': 0, 'unreachable': 0},
        {'changed': 10, 'failures': 0, 'ok': 0, 'skipped': 0, 'unreachable': 0},
        {'changed': 0, 'failures': 10, 'ok': 0, 'skipped': 0, 'unreachable': 0},
        {'changed': 0, 'failures': 0, 'ok': 0, 'skipped': 10, 'unreachable': 0},
        {'changed': 0, 'failures': 0, 'ok': 0, 'skipped': 0, 'unreachable': 10}
    ]

# Generated at 2022-06-13 16:02:06.325673
# Unit test for function colorize
def test_colorize():
    for c in ('blue', 'lightblue', 'yellow', 'lightyellow', 'green',
              'lightgreen', 'red', 'lightred'):
        lead = 'XX'
        num = 1
        test = '%s=%s' % (lead, str(num))
        s = colorize(lead, num, c)
        if not s.startswith(test):
            print(u"%s != %s" % (s, test))



# Generated at 2022-06-13 16:02:15.381836
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor(u'1') == u'38;5;1'
    assert parsecolor(u'15') == u'38;5;15'
    assert parsecolor(u'16') == u'38;5;16'
    assert parsecolor(u'17') == u'38;5;17'
    assert parsecolor(u'19') == u'38;5;19'
    assert parsecolor(u'27') == u'38;5;27'
    assert parsecolor(u'default') == u'39'
    assert parsecolor(u'31') == u'31'
    assert parsecolor(u'0') == u'38;5;0'

    assert parsecolor(u'color1') == u'38;5;1'
    assert parsecolor

# Generated at 2022-06-13 16:02:25.344957
# Unit test for function hostcolor
def test_hostcolor():
    # u' should be used instead of ' for any string that contains non-ASCII
    # characters.
    assert hostcolor(u'localhost', dict(failures=0, unreachable=1, ok=1, changed=0)) == u"%-37s" % u"\033[31mlocalhost\033[0m"
    assert hostcolor(u'localhost', dict(failures=0, unreachable=0, ok=1, changed=1)) == u"%-37s" % u"\033[33mlocalhost\033[0m"
    assert hostcolor(u'localhost', dict(failures=0, unreachable=0, ok=1, changed=0)) == u"%-37s" % u"\033[32mlocalhost\033[0m"

# Generated at 2022-06-13 16:02:31.395460
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor('black') == u'30'
    assert parsecolor('red') == u'31'
    assert parsecolor('blue') == u'34'
    assert parsecolor('yellow') == u'33'
    assert parsecolor('white') == u'37'
    assert parsecolor('darkgray') == u'90'
    assert parsecolor('rgb100100100') == u'38;5;234'
    assert parsecolor('rgb255255255') == u'38;5;255'
    assert parsecolor('rgb255025502550') == u'38;5;255'
    assert parsecolor('rgb000') == u'38;5;16'
    assert parsecolor('rgb111') == u'38;5;59'
    assert parsecolor

# Generated at 2022-06-13 16:02:42.385919
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('localhost', dict(failures=0, unreachable=0, changed=0, ok=1)) == u"%-37s" % stringc('localhost', C.COLOR_OK)
    assert hostcolor('localhost', dict(failures=1, unreachable=0, changed=0, ok=0)) == u"%-37s" % stringc('localhost', C.COLOR_ERROR)
    assert hostcolor('localhost', dict(failures=2, unreachable=0, changed=0, ok=1)) == u"%-37s" % stringc('localhost', C.COLOR_ERROR)
    assert hostcolor('localhost', dict(failures=2, unreachable=1, changed=0, ok=1)) == u"%-37s" % stringc('localhost', C.COLOR_ERROR)

# Generated at 2022-06-13 16:02:54.140369
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor("green") == "32"
    assert parsecolor("red") == "31"
    assert parsecolor("blue") == "34"
    assert parsecolor("rgb255255255") == "38;5;15"
    assert parsecolor("rgb255255255") == "38;5;15"
    assert parsecolor("rgb25525511") == "38;5;226"
    assert parsecolor("color1") == "38;5;1"
    assert parsecolor("color250") == "38;5;250"
    assert parsecolor("color0") == C.COLOR_CODES['default']
    assert parsecolor("default") == C.COLOR_CODES['default']
    assert parsecolor("gray0") == "38;5;232"

# Generated at 2022-06-13 16:03:04.395893
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor("testhost", dict(failures=0, unreachable=0, changed=0)) == u"testhost                       "
    assert hostcolor("testhost", dict(failures=1, unreachable=0, changed=0)) == u"testhost                       "
    assert hostcolor("testhost", dict(failures=0, unreachable=1, changed=0)) == u"testhost                       "
    assert hostcolor("testhost", dict(failures=0, unreachable=0, changed=1)) == u"testhost                       "
    assert hostcolor("testhost", dict(failures=0, unreachable=0, changed=0), color=False) == u"testhost            "

# --- end "pretty"

# utility functions
from ansible.utils.unicode import to_unicode


# Generated at 2022-06-13 16:03:14.607183
# Unit test for function colorize
def test_colorize():
    assert colorize('foo', 0, None) == "foo=0   "
    assert colorize('foo', 0, 'black') == "foo=0   "
    assert colorize('foo', 0, 'blue') == "foo=0   "
    assert colorize('foo', 0, 'cyan') == "foo=0   "
    assert colorize('foo', 0, 'green') == "foo=0   "
    assert colorize('foo', 0, 'magenta') == "foo=0   "
    assert colorize('foo', 0, 'red') == "foo=0   "
    assert colorize('foo', 0, 'white') == "foo=0   "
    assert colorize('foo', 0, 'yellow') == "foo=0   "

# Generated at 2022-06-13 16:03:19.815325
# Unit test for function hostcolor
def test_hostcolor():
    stats1 = {
        'changed': 0,
        'failures': 0,
        'ok': 10,
        'skipped': 0,
        'unreachable': 0
    }
    print(hostcolor('localhost', stats1))

# --- end of "pretty"


if __name__ == '__main__':
    test_hostcolor()

# Generated at 2022-06-13 16:03:25.959148
# Unit test for function stringc
def test_stringc():
    """
    >>> print(stringc("foo", "green"))
    \x1b[32mfoo\x1b[0m
    >>> print(stringc("bar", "red"))
    \x1b[31mbar\x1b[0m
    >>> print(stringc("baz", "blue"))
    \x1b[34mbaz\x1b[0m
    """

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# --- end of "pretty"



# Generated at 2022-06-13 16:03:37.721440
# Unit test for function hostcolor
def test_hostcolor():
    from collections import namedtuple

# Generated at 2022-06-13 16:03:45.632628
# Unit test for function hostcolor

# Generated at 2022-06-13 16:03:57.994980
# Unit test for function hostcolor
def test_hostcolor():
    from ansible import utils
    from ansible.callbacks import AggregateStats, PlaybookCallbacks
    stats = AggregateStats()
    stats.process_raw_stats(utils.parse_json(playbook_output))
    stats.summarize(PlaybookCallbacks(), "/path/to/play/file")
    assert hostcolor("localhost", stats.dark, True) == u"\x1b[38;5;34m%-37s\x1b[0m" \
        % stringc("localhost", C.COLOR_OK)


# Generated at 2022-06-13 16:04:08.439582
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor('black') == C.COLOR_CODES['black']
    assert parsecolor('red') == C.COLOR_CODES['red']
    assert parsecolor('green') == C.COLOR_CODES['green']
    assert parsecolor('yellow') == C.COLOR_CODES['yellow']
    assert parsecolor('blue') == C.COLOR_CODES['blue']
    assert parsecolor('magenta') == C.COLOR_CODES['magenta']
    assert parsecolor('cyan') == C.COLOR_CODES['cyan']
    assert parsecolor('white') == C.COLOR_CODES['white']
    assert parsecolor('darkgray') == C.COLOR_CODES['darkgray']
    assert parsecolor('lightgray') == C.COLOR

# Generated at 2022-06-13 16:04:20.420055
# Unit test for function colorize
def test_colorize():
    """Unit test for function colorize"""

    # Functions tested: colorize
    #
    # Test 1
    #
    # colorize(lead, num, color)
    # The color constants are set in the most recent
    # versions of the library. Create them here if missing
    #
    # Test 2
    #
    # Test function with color=True
    # Test function with color=False
    # Test function with color=True and ANSIBLE_COLOR=False
    # Test function with color=True and ANSIBLE_COLOR=True
    #
    # Test 3
    #
    # Test lead and num parameters.
    # Test one lead and num combination
    # Test several lead and num combinations
    # Test empty string as lead
    # Test empty string as num
    # Test lead and num as empty strings
    #
    # Test

# Generated at 2022-06-13 16:04:24.925429
# Unit test for function colorize
def test_colorize():
    print(repr(colorize('foo', 0, None)))
    print(repr(colorize('foo', 1, None)))
    print(repr(colorize('foo', 0, 'black')))
    print(repr(colorize('foo', 1, 'red')))



# Generated at 2022-06-13 16:04:29.014653
# Unit test for function colorize
def test_colorize():
    print(colorize('foo', 42, 'green'))
    print(colorize('foo', 0, 'blue'))
    print(colorize('foo', 42, None))



# Generated at 2022-06-13 16:04:38.057575
# Unit test for function stringc
def test_stringc():
    try:
        import curses
    except ImportError:
        return
    try:
        curses.setupterm()
    except curses.error:
        # curses returns an error (e.g. could not find terminal)
        return
    colors = ['black', 'red', 'green', 'yellow', 'blue',
              'magenta', 'cyan', 'white']
    attrs = ['bold', 'dark', 'underline', 'blink', 'reverse',
             'concealed']
    for color in colors:
        print("%15s" % color, end=' ')
        sys.stdout.write(stringc("test", color))
        print("\n")
    for attr in attrs:
        print("%15s" % attr, end=' ')

# Generated at 2022-06-13 16:04:45.271227
# Unit test for function hostcolor
def test_hostcolor():
    def chk(host, stats, color, ans):
        return hostcolor(host, stats, color) == ans
    assert chk("testhost.example.com", {'failures': 0, 'unreachable': 0,
        'changed': 0}, True, u"testhost.example.com                ")
    assert chk("testhost.example.com", {'failures': 1, 'unreachable': 0,
        'changed': 0}, True, u"testhost.example.com                ")
    assert chk("testhost.example.com", {'failures': 0, 'unreachable': 1,
        'changed': 0}, True, u"testhost.example.com                ")

# Generated at 2022-06-13 16:04:52.895175
# Unit test for function colorize
def test_colorize():
    print(u"test_colorize():")
    leads = ['ok', 'changed', 'unreachable', 'failed']
    nums = [0, 1, 99]
    colors = [C.COLOR_OK, C.COLOR_HIGHLIGHT, C.COLOR_ERROR]
    for l in leads:
        for n in nums:
            for c in colors:
                print(u"%s" % colorize(l, n, c))
    print(u" ")



# Generated at 2022-06-13 16:05:02.516515
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor("foo", {"unreachable": 0, "failures": 0, "changed": 0}) == "foo                     "
    assert hostcolor("foo", {"unreachable": 1, "failures": 0, "changed": 0}) == "foo                     "
    assert hostcolor("foo", {"unreachable": 0, "failures": 1, "changed": 0}) == "foo                     "
    assert hostcolor("foo", {"unreachable": 0, "failures": 0, "changed": 1}) == "foo                     "
    assert hostcolor("foo", {"unreachable": 0, "failures": 0, "changed": 0}, color=False) == "foo                     "

# Generated at 2022-06-13 16:05:12.894618
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor("white") == "38;5;15"
    assert parsecolor("blue") == "38;5;12"
    assert parsecolor("red") == "38;5;9"
    assert parsecolor("color8") == "38;5;8"
    assert parsecolor("color1") == "38;5;1"
    assert parsecolor("color16") == "38;5;16"
    assert parsecolor("rgb300") == "38;5;22"
    assert parsecolor("rgb321") == "38;5;52"
    assert parsecolor("rgb123") == "38;5;18"
    assert parsecolor("rgb100") == "38;5;234"
    assert parsecolor("rgb122") == "38;5;24"

# Generated at 2022-06-13 16:05:30.433430
# Unit test for function stringc
def test_stringc():
    assert stringc('hello', 'blue') == u'\033[34mhello\033[0m'
    assert stringc('hello', 'color12') == u'\033[38;5;12mhello\033[0m'
    assert stringc('hello', 'rgb255000255') == u'\033[38;5;201mhello\033[0m'
    assert stringc('hello', 'rgb25500000') == u'\033[38;5;196mhello\033[0m'
    assert stringc('hello', 'rgb000255255') == u'\033[38;5;51mhello\033[0m'
    assert stringc('hello', 'rgb000000255') == u'\033[38;5;21mhello\033[0m'

# Generated at 2022-06-13 16:05:35.385590
# Unit test for function colorize
def test_colorize():
    assert colorize('test', 3, 'blue') == u'test=3   '
    assert colorize('test >', 3, 'blue') == u'test >=3 '
    assert colorize('test >', 300, 'blue') == u'test =>300'
    assert colorize('test >', 3000, 'blue') == u'test =3000'



# Generated at 2022-06-13 16:05:44.156666
# Unit test for function hostcolor
def test_hostcolor():
    stats = dict(
        ok=0,
        skipped=0,
        changed=0,
        unreachable=0,
        failures=0,
    )

    s = u"ok               "
    assert hostcolor('ok', stats, color=False) == s
    assert hostcolor('ok', stats, color=True) == stringc(s, C.COLOR_OK)

    stats['changed'] = 1
    s = u"changed          "
    assert hostcolor('changed', stats, color=False) == s
    assert hostcolor('changed', stats, color=True) == stringc(s, C.COLOR_CHANGED)

    stats['unreachable'] = 1
    s = u"unreachable      "
    assert hostcolor('unreachable', stats, color=False) == s

# Generated at 2022-06-13 16:05:51.505943
# Unit test for function hostcolor
def test_hostcolor():
    stats = {}
    stats['failures'] = 0
    stats['unreachable'] = 0
    stats['changed'] = 0
    assert hostcolor('localhost', stats) == '%-37s' % stringc('localhost', C.COLOR_OK)
    stats['changed'] = 1
    assert hostcolor('localhost', stats) == '%-37s' % stringc('localhost', C.COLOR_CHANGED)
    stats['failures'] = 1
    stats['unreachable'] = 1
    assert hostcolor('localhost', stats) == '%-37s' % stringc('localhost', C.COLOR_ERROR)
    # ANSIBLE_COLOR = False
    global ANSIBLE_COLOR
    ANSIBLE_COLOR = False
    assert hostcolor('localhost', stats) == '%-26s' % 'localhost'

# Generated at 2022-06-13 16:06:02.857368
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor('red') == u'31'
    assert parsecolor('black') == u'30'
    assert parsecolor('white') == u'37'
    assert parsecolor('blue') == u'34'
    assert parsecolor('cyan') == u'36'
    assert parsecolor('green') == u'32'
    assert parsecolor('magenta') == u'35'
    assert parsecolor('yellow') == u'33'
    assert parsecolor('darkgray') == u'90'
    assert parsecolor('darkred') == u'91'
    assert parsecolor('darkgreen') == u'92'
    assert parsecolor('darkyellow') == u'93'
    assert parsecolor('darkblue') == u'94'
    assert parsecolor('darkmagenta')

# Generated at 2022-06-13 16:06:14.650103
# Unit test for function hostcolor
def test_hostcolor():
    stats = dict(failures=0, unreachable=0, changed=0)
    for c in (True, False):
        assert hostcolor("localhost", stats, c) == "localhost                "
        assert hostcolor("localhost.localdomain", stats, c) == "localhost.localdomain  "
        stats['failures'] = stats['unreachable'] = 1
        assert hostcolor("localhost", stats, c) == "localhost                "
        assert hostcolor("localhost.localdomain", stats, c) == "localhost.localdomain  "
        stats['failures'] = 0
        assert hostcolor("localhost", stats, c) == "localhost                "
        assert hostcolor("localhost.localdomain", stats, c) == "localhost.localdomain  "
        stats['changed'] = 1
        assert hostcolor

# Generated at 2022-06-13 16:06:25.580515
# Unit test for function colorize
def test_colorize():
    failed_colorized = colorize('Fail', 0, C.COLOR_ERROR)
    succeeded_colorized = colorize('Ok', 0, C.COLOR_OK)
    skipped_colorized = colorize('Skip', 0, C.COLOR_SKIP)
    unreachable_colorized = colorize('Unreachable', 0, C.COLOR_UNREACHABLE)
    changed_colorized = colorize('Changed', 0, C.COLOR_CHANGED)
    ok_colorized = colorize('Ok', 10, C.COLOR_OK)
    unreachable_colorized_2 = colorize('Unreachable', 2, C.COLOR_UNREACHABLE)

# Generated at 2022-06-13 16:06:36.347671
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor("localhost", {'failures': 0, 'changed': 0, 'unreachable': 0, 'skipped': 0}) == u"%-26s" % "localhost"
    assert hostcolor("localhost", {'failures': 1, 'changed': 0, 'unreachable': 0, 'skipped': 0}) == u"%-37s" % stringc("localhost", C.COLOR_ERROR)
    assert hostcolor("localhost", {'failures': 0, 'changed': 1, 'unreachable': 0, 'skipped': 0}) == u"%-37s" % stringc("localhost", C.COLOR_CHANGED)

# Generated at 2022-06-13 16:06:45.005513
# Unit test for function colorize
def test_colorize():
    # The following are all equal
    assert colorize(u"foo", 0, None) == u"foo=0   "
    assert colorize(u"foo", 0, C.COLOR_SKIP) ==  u"foo=0   "
    assert colorize(u"foo", u"0", C.COLOR_SKIP) ==  u"foo=0   "

    # Print numbers with leading zeroes

# Generated at 2022-06-13 16:06:52.979938
# Unit test for function stringc
def test_stringc():
    """test function stringc()"""
    # ANSIBLE_COLOR=False
    # result = stringc("test text", "blue")
    # assert result == "test text"

    # ANSIBLE_COLOR=False
    # result = stringc("test text", "blue")
    # assert result == "test text"

    # ANSIBLE_COLOR=True
    # result = stringc("test text", "blue")
    # assert result == "`test text`"

    # ANSIBLE_COLOR=True
    # result = stringc("test text", "blue", True)
    # assert result == "\001`test text`\002"

# Generated at 2022-06-13 16:07:16.206497
# Unit test for function colorize
def test_colorize():
    fail_sep = u'='
    print(u'Colorize Tests')
    print(u'\tcolorize(u"ok", 1, None)', colorize(u"ok", 1, None))
    print(u'\tcolorize(u"changed", 1, None)', colorize(u"changed", 1, None))
    print(u'\tcolorize(u"darkgreen", 1, u"darkgreen")', colorize(u"darkgreen", 1, u"darkgreen"))
    print(u'\tcolorize(u"ok", 1, u"green")', colorize(u"ok", 1, u"green"))
    print(u'\tcolorize(u"changed", 1, u"yellow")', colorize(u"changed", 1, u"yellow"))

# Generated at 2022-06-13 16:07:23.229842
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor("success-green", {'failures': 0, 'changed': 0}) == u"%-37s" % stringc("success-green", C.COLOR_OK)
    assert hostcolor("failure-red", {'failures': 1, 'changed': 0}) == u"%-37s" % stringc("failure-red", C.COLOR_ERROR)
    assert hostcolor("changed-yellow", {'failures': 0, 'changed': 1}) == u"%-37s" % stringc("changed-yellow", C.COLOR_CHANGED)



# Generated at 2022-06-13 16:07:29.532492
# Unit test for function stringc
def test_stringc():
    try:
        curses.setupterm()
        if curses.tigetnum("colors") > 0:
            ANSIBLE_UNIT_TESTS_COLOR = True
        else:
            ANSIBLE_UNIT_TESTS_COLOR = False
    except Exception:
        ANSIBLE_UNIT_TESTS_COLOR = False


# Generated at 2022-06-13 16:07:39.318662
# Unit test for function stringc
def test_stringc():
    """Unit test for function stringc."""

    def _test(text, color):
        """Test with the specified color name."""
        return stringc(text, color)

    # ANSI color codes
    for color in ('black', 'red', 'green', 'yellow', 'blue', 'magenta',
                  'cyan', 'white'):
        assert _test('foo', color).startswith(u'\033[9'), \
            "%s: leading ESC[9 is missing" % color
        assert _test('foo', color).endswith(u'm\033[0m'), \
            "%s: trailing mESC[0m is missing" % color

    # 256 color codes
    for color in ('color%d' % i for i in xrange(0, 256)):
        assert _test('foo', color).startsw

# Generated at 2022-06-13 16:07:42.227304
# Unit test for function hostcolor
def test_hostcolor():
    test_host = 'testhost'
    test_stats = dict(failures=1, unreachable=0, skipped=0, changed=0, ok=1)
    print(hostcolor(test_host, test_stats, color=True))
    return True


# Generated at 2022-06-13 16:07:53.823524
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor("red") == u'31'
    assert parsecolor("rgb255255255") == u'38;5;15'
    assert parsecolor("color1") == u'38;5;1'
    assert parsecolor("black") == u'30'
    assert parsecolor("gray0") == u'38;5;232'
    assert parsecolor("blue") == u'34'
    assert parsecolor("green") == u'32'
    assert parsecolor("yellow") == u'33'
    assert parsecolor("magenta") == u'35'
    assert parsecolor("cyan") == u'36'
    assert parsecolor("gray8") == u'38;5;245'

# Generated at 2022-06-13 16:08:04.882973
# Unit test for function stringc
def test_stringc():
    assert stringc("blah", 'green') == "\033[32mblah\033[0m"
    assert stringc("blah", 'blue') == "\033[34mblah\033[0m"
    assert stringc("blah", 'red') == "\033[31mblah\033[0m"

    # test with wrap_nonvisible_chars set to True
    assert stringc("blah", 'green', wrap_nonvisible_chars=True) == "\001\033[32m\002blah\001\033[0m\002"
    assert stringc("blah", 'blue', wrap_nonvisible_chars=True) == "\001\033[34m\002blah\001\033[0m\002"
    assert stringc("blah", 'red', wrap_nonvisible_chars=True)

# Generated at 2022-06-13 16:08:14.993320
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor('red') == u'31'
    assert parsecolor('white') == u'37'
    assert parsecolor('COLOR232') == u'38;5;232'
    assert parsecolor('COLOR255') == u'38;5;255'
    assert parsecolor('COLOR0') == u'38;5;0'
    assert parsecolor('gray0') == u'38;5;232'
    assert parsecolor('gray7') == u'38;5;239'
    assert parsecolor('gray8') == u'38;5;240'
    assert parsecolor('gray15') == u'38;5;247'
    assert parsecolor('gray16') == u'38;5;248'
    assert parsecolor('gray23') == u'38;5;255'


# Generated at 2022-06-13 16:08:18.133600
# Unit test for function parsecolor
def test_parsecolor():
    test_color = 'cyan'
    ansible_parsecolor = parsecolor(test_color)
    test_parsecolor = '36'
    assert ansible_parsecolor == test_parsecolor


# Generated at 2022-06-13 16:08:19.682298
# Unit test for function hostcolor
def test_hostcolor():
    # Simple test that it doesn't crash
    hostcolor('test1', {})



# Generated at 2022-06-13 16:08:43.805605
# Unit test for function stringc
def test_stringc():
    assert stringc('foo', 'blue') == "\033[34mfoo\033[0m"
    assert stringc('foo bar', 'blue') == "\033[34mfoo bar\033[0m"
    assert stringc('foo\nbar', 'blue') == "\033[34mfoo\n\033[0mbar"



# Generated at 2022-06-13 16:08:55.971302
# Unit test for function hostcolor
def test_hostcolor():
    # hostcolor without color
    host = 'testhost.com'
    stats = {'failures': 0, 'unreachable': 0, 'changed': 0}
    color = False
    assert hostcolor(host, stats, color) == '%-26s' % host

    # hostcolor without color, but 'changed' happened
    host = 'testhost.com'
    stats = {'failures': 0, 'unreachable': 0, 'changed': 1}
    color = False
    assert hostcolor(host, stats, color) == '%-26s' % host

    # hostcolor with color, but 'changed' happened
    host = 'testhost.com'
    stats = {'failures': 0, 'unreachable': 0, 'changed': 1}
    color = True

# Generated at 2022-06-13 16:09:04.662208
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('hostname', {'changed': 0, 'failures': 1, 'ok': 20, 'skipped': 1, 'unreachable': 1}) == u'hostname                          '
    assert hostcolor('hostname', {'changed': 0, 'failures': 0, 'ok': 20, 'skipped': 1, 'unreachable': 1}) == u'hostname                          '
    assert hostcolor('hostname', {'changed': 0, 'failures': 0, 'ok': 20, 'skipped': 0, 'unreachable': 0}) == u'hostname                          '
    assert hostcolor('hostname', {'changed': 1, 'failures': 0, 'ok': 20, 'skipped': 0, 'unreachable': 0}) == u'hostname                          '

# Generated at 2022-06-13 16:09:14.710909
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor('rgb255255255') == u'38;5;15'
    assert parsecolor('rgb000255000') == u'38;5;2'
    assert parsecolor('rgb255000255') == u'38;5;13'
    assert parsecolor('rgb000000000') == u'38;5;0'
    assert parsecolor('rgb255255255') == parsecolor('color15')
    assert parsecolor('rgb000255000') == parsecolor('color2')
    assert parsecolor('rgb255000255') == parsecolor('color13')
    assert parsecolor('rgb000000000') == parsecolor('color0')
    assert parsecolor('rgb255255255') == parsecolor('gray15')

# Generated at 2022-06-13 16:09:22.652357
# Unit test for function colorize
def test_colorize():
    print(colorize(u'foo', 0, u'blue'))
    print(colorize(u'foo', 1, u'blue'))
    print(colorize(u'foo', 2, u'blue'))
    print(colorize(u'foo', -2, u'blue'))
    print(colorize(u'foo', -1, u'blue'))
    print(colorize(u'OK:   ', 0, u'green'))
    print(colorize(u'CHANGED:   ', 1, u'yellow'))
    print(colorize(u'FAILED:   ', -3, u'red'))
    print(colorize(u'UNREACHABLE: ', -2, u'red'))
    print(colorize(u'foo', False, u'blue'))
   

# Generated at 2022-06-13 16:09:25.387323
# Unit test for function stringc
def test_stringc():
    assert stringc(u"cool", u"green", True) == u"\x01\033[38;5;2m\x02cool\x01\033[0m\x02"



# Generated at 2022-06-13 16:09:30.819479
# Unit test for function colorize
def test_colorize():
    assert colorize('ok', 0, 'green') == u'ok=0   '
    assert colorize('changed', 0, 'yellow') == u'changed=0   '
    assert colorize('unreachable', 0, 'red') == u'unreachable=0   '
    assert colorize('failed', 0, 'red') == u'failed=0   '
    assert colorize('skipped', 0, 'cyan') == u'skipped=0   '

