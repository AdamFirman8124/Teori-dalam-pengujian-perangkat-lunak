

# Generated at 2022-06-13 15:59:42.357184
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor("localhost", {'failures': 0, 'changed': 0, 'unreachable': 0}) == u"%-26s" % 'localhost'
    assert hostcolor("localhost", {'failures': 1, 'changed': 0, 'unreachable': 0}) == u"%-26s" % stringc('localhost', C.COLOR_ERROR)
    assert hostcolor("localhost", {'failures': 0, 'changed': 1, 'unreachable': 0}) == u"%-26s" % stringc('localhost', C.COLOR_CHANGED)
    assert hostcolor("localhost", {'failures': 0, 'changed': 0, 'unreachable': 1}) == u"%-26s" % stringc('localhost', C.COLOR_ERROR)

# Generated at 2022-06-13 15:59:47.685425
# Unit test for function stringc
def test_stringc():
    assert parsecolor("black") == u'30'
    assert parsecolor("red") == u'31'
    assert parsecolor("green") == u'32'
    assert parsecolor("yellow") == u'33'
    assert parsecolor("blue") == u'34'
    assert parsecolor("magenta") == u'35'
    assert parsecolor("cyan") == u'36'
    assert parsecolor("white") == u'37'
    assert parsecolor("bblack") == u'1;30'
    assert parsecolor("bred") == u'1;31'
    assert parsecolor("bgreen") == u'1;32'
    assert parsecolor("byellow") == u'1;33'
    assert parsecolor("bblue") == u'1;34'
   

# Generated at 2022-06-13 15:59:52.671007
# Unit test for function hostcolor
def test_hostcolor():
    """
    >>> test_hostcolor()
    \x1b[32m- hostname                 \x1b[0m\n
    """
    host = u"hostname"
    stats = {'changed': 0, 'skipped': 0, 'failures': 0, 'ok': 1, 'unreachable': 0}
    sys.stdout.write(hostcolor(host, stats))



# Generated at 2022-06-13 16:00:02.302203
# Unit test for function colorize
def test_colorize():
    def _color(lead, num, color):
        return colorize(lead, num, color)

    assert _color("ok", 0, "green") == "ok=0   "
    assert _color("changed", 0, "yellow") == "changed=0"
    assert _color("unreachable", 0, "red") == "unreachable=0"
    assert _color("failed", 0, "red") == "failed=0 "
    assert _color("ok", 2, "green") == "ok=2   "
    assert _color("changed", 1, "yellow") == "changed=1 "
    assert _color("unreachable", 10, "red") == "unreachable=10"
    assert _color("failed", 100, "red") == "failed=100"


# --- end "pretty"

# Using the same

# Generated at 2022-06-13 16:00:08.973539
# Unit test for function parsecolor

# Generated at 2022-06-13 16:00:19.030193
# Unit test for function hostcolor
def test_hostcolor():
    # Test for changed
    stats = {'changed': 1, 'failures': 0, 'skipped': 0, 'ok': 2, 'unreachable': 0}
    assert hostcolor('localhost', stats, color=True).endswith(u"\033[0;32mlocalhost\033[0m")
    assert hostcolor('localhost', stats, color=False).endswith(u"localhost")

    # Test for failures
    stats = {'changed': 0, 'failures': 1, 'skipped': 0, 'ok': 2, 'unreachable': 0}
    assert hostcolor('localhost', stats, color=True).endswith(u"\033[0;31mlocalhost\033[0m")
    assert hostcolor('localhost', stats, color=False).endswith(u"localhost")

    # Test for unre

# Generated at 2022-06-13 16:00:29.906353
# Unit test for function stringc
def test_stringc():
    """Example of using stringc function."""
    if ANSIBLE_COLOR:
        print(stringc(u"This text is bold", u"bold"))
        print(stringc(u"This text is red", u"red"))
        print(stringc(u"This text is blue", u"blue"))
        print(stringc(u"This text is cyan", u"cyan"))
        print(stringc(u"This text is green", u"green"))
        print(stringc(u"This text is white", u"white"))
        print(stringc(u"This text is color244", u"color244"))
        print(stringc(u"This text is bold cyan", u"bold cyan"))
        print(stringc(u"This text is bold on cyan", u"bold cyan"))

# Generated at 2022-06-13 16:00:39.236221
# Unit test for function parsecolor
def test_parsecolor():
    from units.compat import unittest

    class Parsecolor(unittest.TestCase):
        def test_color(self):
            self.assertEqual(u'38;5;12', parsecolor(u'color12'))

        def test_rgb(self):
            self.assertEqual(u'38;5;12', parsecolor(u'rgb120'))

        def test_gray(self):
            self.assertEqual(u'38;5;234', parsecolor(u'gray8'))
    return unittest.TestLoader().loadTestsFromTestCase(Parsecolor)



# Generated at 2022-06-13 16:00:41.792589
# Unit test for function colorize
def test_colorize():
    for i in range(-1, 2):
        for color in [None, 'red', 'green', 'blue', 'white', 'yellow']:
            print(colorize(u"test", i, color))



# Generated at 2022-06-13 16:00:48.087449
# Unit test for function parsecolor
def test_parsecolor():
    assert(parsecolor('black') == u'30')
    assert(parsecolor('color0') == u'38;5;0')
    assert(parsecolor('color8') == u'38;5;8')
    assert(parsecolor('color16') == u'38;5;16')
    assert(parsecolor('color255') == u'38;5;255')
    assert(parsecolor('rgb000') == u'38;5;16')
    assert(parsecolor('rgb255') == u'38;5;231')
    assert(parsecolor('rgb555') == u'38;5;59')
    assert(parsecolor('rgb123') == u'38;5;95')
    assert(parsecolor('rgb333') == u'38;5;119')

# Generated at 2022-06-13 16:01:03.251892
# Unit test for function stringc
def test_stringc():
    res = stringc("This is a test", "red", wrap_nonvisible_chars=False)
    assert res == '\033[31mThis is a test\033[0m'

    res = stringc("This is a test", "red", wrap_nonvisible_chars=True)
    assert res == '\001\033[31m\002This is a test\001\033[0m\002'

    res = stringc("This is a test", "rgb255255255", wrap_nonvisible_chars=False)
    assert res == '\033[38;5;15mThis is a test\033[0m'

    res = stringc("This is a test", "rgb255255255", wrap_nonvisible_chars=True)

# Generated at 2022-06-13 16:01:06.011771
# Unit test for function stringc
def test_stringc():
    assert stringc("foo", "green") == u"\033[32mfoo\033[0m"



# Generated at 2022-06-13 16:01:16.083207
# Unit test for function stringc

# Generated at 2022-06-13 16:01:21.628559
# Unit test for function hostcolor
def test_hostcolor():
    """ Unit test for function hostcolor """

    stats = dict(
        failures=0,
        changed=0,
        unreachable=0,
    )
    assert hostcolor('test_host', stats) == u'%-26s' % 'test_host'
    stats['changed'] = 1
    assert hostcolor('test_host', stats) == u'%-37s' % stringc('test_host', C.COLOR_CHANGED)
    stats['unreachable'] = 1
    assert hostcolor('test_host', stats) == u'%-37s' % stringc('test_host', C.COLOR_ERROR)

# End of functions from the "pretty" library



# Generated at 2022-06-13 16:01:31.650262
# Unit test for function stringc
def test_stringc():
    ANSIBLE_COLOR = False
    assert stringc('test', 'black') == 'test'
    ANSIBLE_COLOR = True
    assert stringc('test', 'black') == '\x1b[30mtest\x1b[0m'

# --- end of "pretty"

# ===========================================
# YAML filter plugin
#
# Simple filter to represent colors in strings
# in a YAML serialization.
#
# This filter will use ANSIBLE_COLOR, so it can be
# used in tests as well.
#
# Example usage:
#
# 1)
# msg: "Some {{ 'colored' | colorize('red') }} text"
#
# 2)
# msg: "Some {{ 'colored' | colorize('red_bold') }} text"
#
# 3)
# msg:

# Generated at 2022-06-13 16:01:40.016573
# Unit test for function stringc
def test_stringc():
    print(u"Testing stringc")
    assert stringc(u"Stringc", u"blue") == u"\033[34mStringc\033[0m"
    assert stringc(u"Stringc", u"green") == u"\033[32mStringc\033[0m"
    assert stringc(u"Stringc", u"red") == u"\033[31mStringc\033[0m"
    assert stringc(u"Stringc", u"purple") == u"\033[35mStringc\033[0m"
    assert stringc(u"Stringc", u"cyan") == u"\033[36mStringc\033[0m"
    assert stringc(u"Stringc", u"white") == u"\033[37mStringc\033[0m"
   

# Generated at 2022-06-13 16:01:46.533224
# Unit test for function hostcolor
def test_hostcolor():
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import get_all_plugin_loaders
    for plugin_loader in get_all_plugin_loaders():
        for plugin in plugin_loader.get_all_plugins():
            if not isinstance(plugin, PlayContext):
                continue
            if plugin.COLOR is None:
                continue
            assert C.HOST_COLOR == plugin.COLOR
            return
    else:
        assert False


# --- end of "pretty"



# Generated at 2022-06-13 16:01:57.067105
# Unit test for function stringc
def test_stringc():
    import re
    color_code_re = re.compile("\033\[\d+m")
    stringc("test", "red")
    assert color_code_re.search("\033[31mtest\033[0m")
    stringc("test", "rgb123")
    assert color_code_re.search("\033[38;5;191mtest\033[0m")
    stringc("test", "gray99")
    assert color_code_re.search("\033[38;5;255mtest\033[0m")
    stringc("test", "blue", wrap_nonvisible_chars=True)
    assert color_code_re.search("\001\033[34m\002test\001\033[0m\002")
    # --- end "pretty"

# Generated at 2022-06-13 16:02:04.701838
# Unit test for function stringc
def test_stringc():
    class P(object):
        def __init__(self, color=None, nocolor=None):
            self.color = color
            self.nocolor = nocolor

    results = []
    results.append(test_stringc_helper(u"test", P(color=u"green")))
    results.append(test_stringc_helper(u"test", P(color=u"blue")))
    results.append(test_stringc_helper(u"test", P(color=None)))

    results.append(test_stringc_helper(u"test", P(color=u"red"), True))
    results.append(test_stringc_helper(u"test", P(color=u"blue"), True))

# Generated at 2022-06-13 16:02:14.699330
# Unit test for function stringc
def test_stringc():
    import filecmp
    import shutil
    import tempfile
    import unittest
    import os

    test_color = None
    env_color = os.getenv('ANSIBLE_FORCE_COLOR', '')

    def set_test_color(value):
        global test_color
        test_color = value

    def set_env_color(value):
        if value is True:
            value = 'True'
        elif value is False:
            value = ''
        os.putenv('ANSIBLE_FORCE_COLOR', value)

    def is_colorized(line):
        return line[:4] == '\033[3' or line[-5:] == '\033[0m'

    def is_not_colorized(line):
        return not is_colorized(line)


# Generated at 2022-06-13 16:02:28.552346
# Unit test for function hostcolor
def test_hostcolor():
    # No color
    assert hostcolor('dummy', dict(changed=2, failures=0, unreachable=0), False) == 'dummy'
    assert hostcolor('dummy', dict(changed=0, failures=2, unreachable=0), False) == 'dummy'
    assert hostcolor('dummy', dict(changed=0, failures=0, unreachable=2), False) == 'dummy'
    assert hostcolor('dummy', dict(changed=0, failures=0, unreachable=0), False) == 'dummy'
    # With color
    assert hostcolor('dummy', dict(changed=2, failures=0, unreachable=0), True) == '\x1b[1;32mdummy\x1b[0m'

# Generated at 2022-06-13 16:02:37.448570
# Unit test for function hostcolor
def test_hostcolor():
    host = 'test_host'
    stats = {'failures': 0, 'changed': 0, 'unreachable': 0}
    assert host == hostcolor(host, stats, False).strip()
    assert stringc(host, C.COLOR_ERROR) == hostcolor(host, {'failures': 1}, True).strip()
    assert stringc(host, C.COLOR_CHANGED) == hostcolor(host, {'changed': 1}, True).strip()
    assert stringc(host, C.COLOR_OK) == hostcolor(host, stats, True).strip()

# --- end "pretty"



# Generated at 2022-06-13 16:02:46.860391
# Unit test for function hostcolor
def test_hostcolor():
    stats = dict(ok=1, failures=0, unreachable=0, changed=0)
    if hostcolor(u"green-unicorn", stats) != u"%-37s" % stringc(u"green-unicorn", C.COLOR_OK):
        raise AssertionError("Green Unicorn is not green")

    stats = dict(ok=1, failures=1, unreachable=0, changed=0)
    if hostcolor(u"red-unicorn", stats) != u"%-37s" % stringc(u"red-unicorn", C.COLOR_ERROR):
        raise AssertionError("Red Unicorn is not red")

    stats = dict(ok=1, failures=0, unreachable=2, changed=0)

# Generated at 2022-06-13 16:02:56.195160
# Unit test for function hostcolor
def test_hostcolor():
    h = {}
    h['darkred'] = dict(failures=10, unreachable=0, changed=0)
    h['lightred'] = dict(failures=0, unreachable=1, changed=0)
    h['darkgreen'] = dict(failures=0, unreachable=0, changed=10)
    h['lightgreen'] = dict(failures=0, unreachable=0, changed=0)
    h['brown'] = dict(failures=1, unreachable=0, changed=10)

    for (host, stats) in h.items():
        assert hostcolor(host, stats, color=False) == "%-26s" % host
        # If we run out of terminal colors just tests the length
        if ANSIBLE_COLOR:
            assert len(hostcolor(host, stats, color=True)) == 37

# Generated at 2022-06-13 16:03:05.573001
# Unit test for function hostcolor
def test_hostcolor():
    stats = {'changed': 0, 'dark': 0, 'failures': 0, 'ok': 0, 'processed': 0, 'skipped': 0, 'unreachable': 0}

    # Test default
    if hostcolor(u'foo', stats) != u"%-26s":
        raise AssertionError('hostcolor test 1 failed!')

    # Test ok
    if hostcolor(u'foo', stats, True) != u"%-37s":
        raise AssertionError('hostcolor test 2 failed!')

    # Test changed
    stats['changed'] = 1
    if hostcolor(u'foo', stats, True) != u"%-37s":
        raise AssertionError('hostcolor test 3 failed!')

    # Test unreachable
    stats['unreachable'] = 1

# Generated at 2022-06-13 16:03:13.817374
# Unit test for function hostcolor
def test_hostcolor():
    stats = dict(failures=0, unreachable=0, changed=0)
    assert u"%-37s" % u'localhost' == hostcolor(u'localhost', stats, True)
    stats = dict(failures=1, unreachable=0, changed=0)
    assert u"%-37s" % stringc(u'localhost', C.COLOR_ERROR) == \
        hostcolor(u'localhost', stats, True)
    stats = dict(failures=1, unreachable=0, changed=0)
    assert u"%-37s" % u'localhost' == hostcolor(u'localhost', stats, False)

# Generated at 2022-06-13 16:03:19.127343
# Unit test for function colorize
def test_colorize():
    if not ANSIBLE_COLOR:
        return
    print(colorize(u"foo", 42, C.COLOR_OK))
    print(colorize(u"bar", -1, C.COLOR_ERROR))
    print(colorize(u"baz", 0, C.COLOR_CHANGED))

# end of pretty library code



# Generated at 2022-06-13 16:03:27.645755
# Unit test for function parsecolor
def test_parsecolor():

    # Test named colors
    for color in C.COLOR_CODES.keys():
        assert parsecolor(color) == C.COLOR_CODES[color]

    # Test color numbers
    for num in range(0, 7):
        assert parsecolor('color' + str(num)) == '38;5;%d' % (num + 30)

    # Test gray scale numbers
    for num in range(0, 23):
        assert parsecolor('gray' + str(num)) == '38;5;%d' % (num + 232)

    # Test rgb values
    for r in range(0, 6):
        for g in range(0, 6):
            for b in range(0, 6):
                color = 'rgb' + str(r) + str(g) + str(b)
                assert par

# Generated at 2022-06-13 16:03:33.422669
# Unit test for function hostcolor
def test_hostcolor():
    import io
    import sys
    import textwrap


# Generated at 2022-06-13 16:03:42.954266
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor("localhost", dict(changed=0, failures=0, ok=3, skipped=0, unreachable=0)) == u"%-26s" % u"localhost"
    # Test no color
    assert hostcolor("localhost", dict(changed=0, failures=0, ok=3, skipped=0, unreachable=0), color=False) == u"%-26s" % u"localhost"
    # Test changed
    assert hostcolor("localhost", dict(changed=1, failures=0, ok=3, skipped=0, unreachable=0)) == u"%-37s" % u"\n".join([u"\033[33m%s\033[0m" % t for t in u"localhost".split(u'\n')])
    # Test unreachable

# Generated at 2022-06-13 16:03:52.465614
# Unit test for function hostcolor
def test_hostcolor():
    from ansible.utils.unicode import to_unicode
    from ansible.utils.color import hostcolor
    stats = {
        'skipped': 0,
        'ok': 10,
        'failed': 0,
        'processed': 10,
        'dark': 0,
        'changed': 9,
        'failures': 0,
        'unreachable': 0,
    }
    assert hostcolor('test', stats, color=True) == u'%-37s' % to_unicode(stringc('test', C.COLOR_CHANGED))

# Generated at 2022-06-13 16:03:55.735410
# Unit test for function colorize
def test_colorize():
    for color in C.COLOR_CODES.keys():
        print(u"This is the color '%s' %s" % (color, colorize('>', 'OK', color)))


# Generated at 2022-06-13 16:04:04.340710
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor("test", dict(ok=1, changed=0, unreachable=0, failures=0)) == u"test                   "
    assert hostcolor("test", dict(ok=0, changed=1, unreachable=0, failures=0)) == u"test                   "
    assert hostcolor("test", dict(ok=0, changed=0, unreachable=1, failures=0)) == u"test                   "
    assert hostcolor("test", dict(ok=0, changed=0, unreachable=0, failures=1)) == u"test                   "

# --- end "pretty"



# Generated at 2022-06-13 16:04:14.975605
# Unit test for function hostcolor
def test_hostcolor():
    from ansible import constants as C
    stats = {
        'changed': 0,
        'failures': 0,
        'skipped': 0,
        'ok': 4,
        'unreachable': 0,
    }
    # No failures, unreachable, or changes.
    assert hostcolor("test.example.com", stats) == u"%-37s" % stringc("test.example.com", C.COLOR_OK)
    # No failures or unreachable, but there are changes.
    stats['changed'] = 1
    assert hostcolor("test.example.com", stats) == u"%-37s" % stringc("test.example.com", C.COLOR_CHANGED)
    # No unreachable, but there are failures.
    stats['changed'] = 0
    stats['failures'] = 1
    assert hostcolor

# Generated at 2022-06-13 16:04:26.173393
# Unit test for function stringc

# Generated at 2022-06-13 16:04:35.994572
# Unit test for function hostcolor
def test_hostcolor():
    host = 'example.com'
    stats = dict(failures=0, unreachable=0, changed=0)
    assert hostcolor(host, stats, True) == stringc(
        "%-37s" % host, C.COLOR_OK)
    stats['changed'] = 1
    assert hostcolor(host, stats, True) == stringc(
        "%-37s" % host, C.COLOR_CHANGED)
    stats['changed'] = 0
    stats['unreachable'] = 1
    assert hostcolor(host, stats, True) == stringc(
        "%-37s" % host, C.COLOR_ERROR)
    stats['unreachable'] = 0
    stats['failures'] = 1

# Generated at 2022-06-13 16:04:43.856132
# Unit test for function hostcolor
def test_hostcolor():
    # Successful run
    stats_ok = dict(failures=0, unreachable=0, changed=0)
    assert hostcolor("localhost", stats_ok, True) == u'%-37s' % stringc("localhost", C.COLOR_OK)
    # Failed run
    stats_err = dict(failures=1, unreachable=0, changed=0)
    assert hostcolor("localhost", stats_err, True) == u'%-37s' % stringc("localhost", C.COLOR_ERROR)
    # Changes detected
    stats_change = dict(failures=0, unreachable=0, changed=1)
    assert hostcolor("localhost", stats_change, True) == u'%-37s' % stringc("localhost", C.COLOR_CHANGED)
    # No color

# Generated at 2022-06-13 16:04:47.233822
# Unit test for function colorize
def test_colorize():
    result = colorize('FAILED', 34, 'red')
    assert result == u'\033[31mFAILED=34  \033[0m'
#
# --- end "pretty"



# Generated at 2022-06-13 16:04:50.683074
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('host1', dict(ok=1, changed=1, unreachable=1, failures=1), True) == u"host1                 "



# Generated at 2022-06-13 16:04:59.385791
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('host0', {'ok': 1, 'changed': 0, 'unreachable': 0,
                               'failures': 0}) == u'host0                    '
    assert hostcolor('host1', {'ok': 0, 'changed': 1, 'unreachable': 0,
                               'failures': 0}) == (
        u'\x1b[33;01mhost1\x1b[0m  '
    )
    assert hostcolor('host2', {'ok': 0, 'changed': 0, 'unreachable': 1,
                               'failures': 0}) == (
        u'\x1b[31;01mhost2\x1b[0m '
    )

# Generated at 2022-06-13 16:05:13.622880
# Unit test for function hostcolor
def test_hostcolor():
    "hostcolor"
    global ANSIBLE_COLOR
    ANSIBLE_COLOR=True
    h = 'darkblue.example.org'
    stats = dict(
        ok=1,
        failures=0,
        unreachable=0,
        changed=0,
        skipped=0,
    )
    assert hostcolor(h, stats, color=True) == u"\x1b[0;34mdarkblue.example.org\x1b[0m "
    stats = dict(
        ok=0,
        failures=1,
        unreachable=0,
        changed=0,
        skipped=0,
    )
    assert hostcolor(h, stats, color=True) == u"\x1b[0;31mdarkblue.example.org\x1b[0m "
    stats = dict

# Generated at 2022-06-13 16:05:15.656036
# Unit test for function stringc
def test_stringc():
    """Unit test for function stringc."""
    assert stringc("foo", "green") == "\033[32mfoo\033[0m"



# Generated at 2022-06-13 16:05:21.032766
# Unit test for function hostcolor
def test_hostcolor():
    stats = dict(changed=0, failures=0, unreachable=0)
    assert hostcolor('host1', stats) == 'host1                      '

    stats = dict(changed=1, failures=0, unreachable=0)
    assert hostcolor('host1', stats) == 'host1                      '

    stats = dict(changed=0, failures=1, unreachable=0)
    assert hostcolor('host1', stats) == 'host1                      '

    stats = dict(changed=0, failures=0, unreachable=1)
    assert hostcolor('host1', stats) == 'host1                      '



# Generated at 2022-06-13 16:05:30.649749
# Unit test for function colorize
def test_colorize():
    # basic test
    assert colorize("foo", 0, "black") == "foo=0   "
    assert colorize("foo", 1, "black") == "foo=1   "
    assert colorize("foo", 10, "black") == "foo=10  "
    assert colorize("foo", 100, "black") == "foo=100 "

    # test with color
    if ANSIBLE_COLOR:
        assert colorize("foo", 0, "red") == "\x1b[31mfoo=0   \x1b[0m"
        assert colorize("foo", 1, "red") == "\x1b[31mfoo=1   \x1b[0m"
        assert colorize("foo", 10, "red") == "\x1b[31mfoo=10  \x1b[0m"
       

# Generated at 2022-06-13 16:05:40.932114
# Unit test for function stringc
def test_stringc():
    """
    Test case for function stringc.
    """
    # test color codes
    assert stringc('color', 'white') == u'\033[37mcolor\033[0m'
    assert stringc('color', 'black') == u'\033[30mcolor\033[0m'
    assert stringc('color', 'blue') == u'\033[34mcolor\033[0m'
    assert stringc('color', 'cyan') == u'\033[36mcolor\033[0m'
    assert stringc('color', 'green') == u'\033[32mcolor\033[0m'
    assert stringc('color', 'magenta') == u'\033[35mcolor\033[0m'

# Generated at 2022-06-13 16:05:49.932759
# Unit test for function hostcolor
def test_hostcolor():
    host = 'localhost'
    stats = {'ok': 1, 'changed': 1, 'unreachable': 1, 'failures': 1}
    print(hostcolor(host, stats, color=True))
    stats = {'ok': 1, 'changed': 0, 'unreachable': 0, 'failures': 0}
    print(hostcolor(host, stats, color=True))
    stats = {'ok': 1, 'changed': 1, 'unreachable': 0, 'failures': 0}
    print(hostcolor(host, stats, color=True))
    stats = {'ok': 0, 'changed': 0, 'unreachable': 1, 'failures': 1}
    print(hostcolor(host, stats, color=True))

if __name__ == '__main__':
    test_hostcolor()

# Generated at 2022-06-13 16:05:58.244446
# Unit test for function stringc
def test_stringc():
    assert stringc("%s" % (1), 'blue') == u"\u001b[34m1\u001b[0m"
    assert stringc("%s" % (1), 'rgb255255255') == u"\u001b[38;5;15m1\u001b[0m"
    assert stringc("%s" % (1), 'rgb000255000') == u"\u001b[38;5;40m1\u001b[0m"
    assert stringc("%s" % (1), 'rgb000000255') == u"\u001b[38;5;20m1\u001b[0m"

# Generated at 2022-06-13 16:06:02.521226
# Unit test for function stringc
def test_stringc():
    """Unit test"""
    assert stringc("Text", "blue") == u"\033[34mText\033[0m"
    assert stringc("Text", "blue", True) == u"\001\033[34m\002Text\001\033[0m\002"



# Generated at 2022-06-13 16:06:14.605298
# Unit test for function hostcolor
def test_hostcolor():
    host = 'testhost'
    color = True
    stats1 = {u'started': 1, u'ok': 1, u'changed': 2, u'failures': 0, u'unreachable': 0}
    stats2 = {u'started': 1, u'ok': 1, u'changed': 0, u'failures': 0, u'unreachable': 0}
    stats3 = {u'started': 1, u'ok': 1, u'changed': 2, u'failures': 3, u'unreachable': 0}
    stats4 = {u'started': 1, u'ok': 1, u'changed': 2, u'failures': 0, u'unreachable': 4}


# Generated at 2022-06-13 16:06:25.578610
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('debian', dict(ok=1, changed=1, unreachable=0, failed=0)) == u'\u001b[0;32mdebian                     \u001b[0m'
    assert hostcolor('debian', dict(ok=1, changed=0, unreachable=0, failed=0)) == u'\u001b[0;32mdebian                     \u001b[0m'
    assert hostcolor('debian', dict(ok=0, changed=0, unreachable=1, failed=0)) == u'\u001b[0;31mdebian                     \u001b[0m'
    assert hostcolor('debian', dict(ok=0, changed=0, unreachable=0, failed=1)) == u'\u001b[0;31mdebian                     \u001b[0m'

# Generated at 2022-06-13 16:06:39.867636
# Unit test for function stringc
def test_stringc():
    """Unit test for function stringc."""
    print(stringc("stringc", "blue", True))
    print(stringc("stringc", "normal"))
    print(stringc("stringc", "red", True))
    print(stringc("stringc", "green", True))
    print(stringc("stringc", "yellow", True))
    print(stringc("stringc", "magenta", True))
    print(stringc("stringc", "cyan", True))
    print(stringc("stringc", "white", True))
    print(stringc("stringc", "blue"))
    print(stringc("stringc", "normal"))
    print(stringc("stringc", "red"))
    print(stringc("stringc", "green"))
    print(stringc("stringc", "yellow"))

# Generated at 2022-06-13 16:06:50.738348
# Unit test for function stringc
def test_stringc():
    """ Unit test for function stringc """
    print(stringc("Test", "green"))
    print(stringc("Test", "color33"))
    print(stringc("Test", "rgb123"))
    print(stringc("Test", "gray9"))
    print(stringc("Test", "blue", wrap_nonvisible_chars=True))
    print(stringc("\nTest\n", "blue"))
    print(stringc("\nTest\n", "blue", wrap_nonvisible_chars=True))
    print(stringc("\nTest\n", "rgb123"))
    print(stringc("\nTest\n", "rgb123", wrap_nonvisible_chars=True))
    print(stringc("\nTest\n", "gray9"))

# Generated at 2022-06-13 16:07:00.090662
# Unit test for function stringc
def test_stringc():
    assert stringc("foo", "green") == "\033[32mfoo\033[0m"
    assert stringc("hello", "red") == "\033[31mhello\033[0m"
    assert stringc("world", "yellow") == "\033[33mworld\033[0m"
    assert stringc("this is a test", "blue") == "\033[34mthis is a test\033[0m"
    assert stringc("example", "magenta") == "\033[35mexample\033[0m"
    assert stringc("text", "cyan") == "\033[36mtext\033[0m"
    assert stringc("that is bold", "bold") == "\033[37mthat is bold\033[0m"

# Generated at 2022-06-13 16:07:11.348467
# Unit test for function hostcolor
def test_hostcolor():
    host = "www.example.com"
    stats = {u'changed': 0, u'failures': 0, u'ok': 6, u'skipped': 0, u'unreachable': 0}

    # if ANSIBLE_COLOR and color
    result = hostcolor(host, stats, True)
    assert result == u"%-26s" % stringc(host, C.COLOR_OK)

    # if not ANSIBLE_COLOR and color
    result = hostcolor(host, stats, False)
    assert result == u"%-26s" % host

    # if ANSIBLE_COLOR and not color
    result = hostcolor(host, stats, False)
    assert result == u"%-26s" % host

    # if not ANSIBLE_COLOR and not color
    result = hostcolor(host, stats, False)


# Generated at 2022-06-13 16:07:17.081252
# Unit test for function colorize
def test_colorize():
    """Make sure that this string is the only thing printed"""
    assert colorize(u'ok', 0, C.COLOR_OK) == u'ok=0   '
    assert colorize(u'changed', 0, C.COLOR_CHANGED) == u'changed=0   '
    assert colorize(u'unreachable', 0, C.COLOR_UNREACHABLE) == u'unreachable=0   '
    assert colorize(u'failed', 0, C.COLOR_ERROR) == u'failed=0   '
    assert colorize(u'ok', 1, C.COLOR_OK) == u'\033[0;32mok=1   \033[0m'

# Generated at 2022-06-13 16:07:25.703983
# Unit test for function stringc
def test_stringc():
    if not ANSIBLE_COLOR:
        raise AssertionError("Abort testing function `stringc`"
                             " when color is disabled")
    for color in C.COLOR_CODES:
        c = parsecolor(color)
        s = stringc("string in color %s" % color, color)
        fmt = "\033[%smstring in color %s\033[0m" % (c, color)
        if s != fmt:
            raise AssertionError("Wrong color format: %s\n"
                                 "                  expected: %s" % (s, fmt))

# Generated at 2022-06-13 16:07:36.686755
# Unit test for function hostcolor

# Generated at 2022-06-13 16:07:39.317122
# Unit test for function colorize
def test_colorize():
    print(u"Testing colorize")
    assert colorize(u"changed", 3, u"green") == stringc(u"changed=3", u"green")
    print(u"OK")

# --- end "pretty"



# Generated at 2022-06-13 16:07:45.018323
# Unit test for function hostcolor
def test_hostcolor():
    h = 'darkblue.example.org'
    stats = {'failures': 1, 'unreachable': 0, 'changed': 1}
    # check output when color is True
    assert hostcolor(h, stats, True) == u'%-37s' % stringc(h, C.COLOR_ERROR)
    stats = {'failures': 0, 'unreachable': 0, 'changed': 1}
    assert hostcolor(h, stats, True) == u'%-37s' % stringc(h, C.COLOR_CHANGED)
    stats = {'failures': 0, 'unreachable': 0, 'changed': 0}
    assert hostcolor(h, stats, True) == u'%-37s' % stringc(h, C.COLOR_OK)
    # check output when color is False

# Generated at 2022-06-13 16:07:55.219012
# Unit test for function stringc
def test_stringc():
    """Test function stringc."""
    # Check stringc with color names that should be supported by all terminals.
    assert stringc('test', 'black') == '\x1b[30mtest\x1b[0m'
    assert stringc('test', 'red') == '\x1b[31mtest\x1b[0m'
    assert stringc('test', 'green') == '\x1b[32mtest\x1b[0m'
    assert stringc('test', 'yellow') == '\x1b[33mtest\x1b[0m'
    assert stringc('test', 'blue') == '\x1b[34mtest\x1b[0m'

# Generated at 2022-06-13 16:08:11.400444
# Unit test for function colorize
def test_colorize():
    if ANSIBLE_COLOR:
        assert colorize("a", 0, 'green') == "\033[32ma=0   \033[0m"
        assert colorize("a", 1, 'red') == "\033[31ma=1   \033[0m"
        assert colorize("a", 2, 'blue') == "\033[34ma=2   \033[0m"
        assert colorize("a", 3, 'reset') == "a=3   "
        assert colorize("a", 4, 'random') == "a=4   "
    else:
        assert colorize("a", 1, 'red') == "a=1   "
        assert colorize("a", 2, 'blue') == "a=2   "

# Generated at 2022-06-13 16:08:21.349458
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor("localhost", {"failures": 0, "unreachable": 0, "changed": 0}, color=True) == u"%-37s" % stringc("localhost", C.COLOR_OK)
    assert hostcolor("localhost", {"failures": 0, "unreachable": 0, "changed": 1}, color=True) == u"%-37s" % stringc("localhost", C.COLOR_CHANGED)
    assert hostcolor("localhost", {"failures": 1, "unreachable": 0, "changed": 1}, color=True) == u"%-37s" % stringc("localhost", C.COLOR_ERROR)
    assert hostcolor("localhost", {"failures": 0, "unreachable": 1, "changed": 1}, color=True) == u"%-37s" % stringc("localhost", C.COLOR_ERROR)




# Generated at 2022-06-13 16:08:28.476352
# Unit test for function hostcolor
def test_hostcolor():
    from ansible.compat.tests import unittest
    from ansible.utils.color import hostcolor
    try:
        from unittest.mock import MagicMock
    except ImportError:
        from mock import MagicMock
    if ANSIBLE_COLOR:
        mock_call = MagicMock(return_value=u"\033[31mtest.example.org\033[0m")
    else:
        mock_call = MagicMock(return_value=u"test.example.org")
    with MagicMock(side_effect=mock_call):
        assert hostcolor(u"test.example.org", {u"failures": 1, u"changed": 0, u"unreachable": 0}, color=True) == u"\033[31mtest.example.org\033[0m "


# Generated at 2022-06-13 16:08:34.064720
# Unit test for function colorize
def test_colorize():
    for i in range(3):
        for j in range(3):
            for k in range(3):
                s = colorize("ok", i, C.COLOR_OK) + \
                    colorize("changed", j, C.COLOR_CHANGED) + \
                    colorize("unreachable", k, C.COLOR_UNREACHABLE) + \
                    colorize("failed", i, C.COLOR_ERROR)
                print(s)

#
# --- end "pretty"

# For backwards compatibility



# Generated at 2022-06-13 16:08:40.791400
# Unit test for function colorize
def test_colorize():
    """ Return a string that is colorized according to the values passed into this function """
    results = dict(changed=12, skipped=0, unreachable=0, failed=0)
    lead = "ok"
    color = True
    num = results[lead]
    assert colorize(lead, num, color) == stringc(u"%s=%-4s" % (lead, str(num)), C.COLOR_OK)

    results = dict(changed=0, skipped=0, unreachable=0, failed=0)
    lead = "changed"
    color = True
    num = results[lead]
    assert colorize(lead, num, color) == stringc(u"%s=%-4s" % (lead, str(num)), C.COLOR_CHANGED)


# Generated at 2022-06-13 16:08:43.922885
# Unit test for function colorize
def test_colorize():
    pass
    # print "%-15s" % stringc("Hello World", 'yellow'),
    # print colorize(" ", 42, 'blue')

# --- end "pretty"


# ansible-specific colors


# Generated at 2022-06-13 16:08:56.012841
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('foo.example.com', dict(changed=0, failures=0, unreachable=1), color=True) == stringc('foo.example.com', C.COLOR_ERROR)
    assert hostcolor('foo.example.com', dict(changed=0, failures=1, unreachable=0), color=True) == stringc('foo.example.com', C.COLOR_ERROR)
    assert hostcolor('foo.example.com', dict(changed=1, failures=0, unreachable=0), color=True) == stringc('foo.example.com', C.COLOR_CHANGED)
    assert hostcolor('foo.example.com', dict(changed=0, failures=0, unreachable=0), color=True) == stringc('foo.example.com', C.COLOR_OK)

# Generated at 2022-06-13 16:09:05.911159
# Unit test for function colorize
def test_colorize():
    assert colorize(u"foo", 0, None) == u"foo=0   "
    assert colorize(u"foo", 1, None) == u"foo=1   "
    assert colorize(u"foo", 2, None) == u"foo=2   "
    assert colorize(u"foo", 3, None) == u"foo=3   "
    assert colorize(u"foo", -1, None) == u"foo=-1  "
    assert colorize(u"foo", -2, None) == u"foo=-2  "
    assert colorize(u"foo", -3, None) == u"foo=-3  "
    assert colorize(u"foo", 0.2, None) == u"foo=0.2 "
    assert colorize(u"foo", 0.02, None) == u

# Generated at 2022-06-13 16:09:16.143345
# Unit test for function stringc
def test_stringc():
    for color in ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', 'lightred', 'lightgreen', 'lightyellow', 'lightblue', 'lightmagenta', 'lightcyan', 'lightgray', 'darkgray', 'color1', 'color2', 'color3', 'color4', 'color5', 'color6', 'color7', 'color8', 'color9', 'color10'):
        sys.stdout.write(stringc(color, color))
        sys.stdout.write(stringc(color, "black"))
    sys.stdout.write(stringc('foreground', 'rgb123'))
    sys.stdout.write(stringc('foreground', 'rgb321'))
    sys.stdout.write(stringc('foreground', 'rgb213'))


# Generated at 2022-06-13 16:09:21.410545
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor("host123", dict(failures=0, unreachable=1)) == u"host123                 "
    assert hostcolor("host123", dict(failures=1, unreachable=0)) == u"host123                 "
    assert hostcolor("host123", dict(changed=1), color=False) == u"host123                 "
    # For the following test to work, ANSIBLE_COLOR must be True and
    # ANSIBLE_NOCOLOR must be False
    print(hostcolor("host123", dict(changed=1)))

