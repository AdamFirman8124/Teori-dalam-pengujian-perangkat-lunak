

# Generated at 2022-06-13 15:59:41.083494
# Unit test for function parsecolor

# Generated at 2022-06-13 15:59:49.929515
# Unit test for function stringc
def test_stringc():
    """Return fail if there are any unicode errors when executing the
    stringc function.

    Test text string surrounded by various ASCII characters.
    """
    # Test data
    test_data = []

    # First character code and last character code to test
    first_code = 0
    last_code = 255

    # Populate test_data
    for i in range(first_code, last_code):
        test_data.append(unichr(i))


# Generated at 2022-06-13 16:00:01.151670
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor('default')   == "39"
    assert parsecolor('black')     == "30"
    assert parsecolor('white')     == "37"
    assert parsecolor('green')     == "32"
    assert parsecolor('lightgreen')== "92"
    assert parsecolor('darkgreen') == "32"
    assert parsecolor('grey')      == "90"
    assert parsecolor('darkgrey')  == "90"
    assert parsecolor('blue')      == "34"
    assert parsecolor('cyan')      == "36"
    assert parsecolor('yellow')    == "33"
    assert parsecolor('lightyellow') == "93"
    assert parsecolor('purple')    == "35"
    assert parsecolor('darkpurple') == "35"

# Generated at 2022-06-13 16:00:04.043313
# Unit test for function hostcolor
def test_hostcolor():
    s = hostcolor('host1', dict(failed=1, unreachable=0, changed=0, ok=0))
    assert s == u"host1                  "

# --- end "pretty"
#
# --- begin JINJA2 filters
#



# Generated at 2022-06-13 16:00:06.066948
# Unit test for function stringc
def test_stringc():
    assert stringc('test', 'green') == '\x1b[32mtest\x1b[0m'



# Generated at 2022-06-13 16:00:15.791143
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor('grey') == '30'
    assert parsecolor('red') == '31'
    assert parsecolor('green') == '32'
    assert parsecolor('yellow') == '33'
    assert parsecolor('blue') == '34'
    assert parsecolor('magenta') == '35'
    assert parsecolor('cyan') == '36'
    assert parsecolor('white') == '37'
    assert parsecolor('black') == '30'
    assert parsecolor('dark gray') == '1;30'
    assert parsecolor('bright gray') == '0;37'
    assert parsecolor('dark red') == '1;31'
    assert parsecolor('bright red') == '1;31'
    assert parsecolor('dark green') == '1;32'


# Generated at 2022-06-13 16:00:19.518786
# Unit test for function colorize
def test_colorize():
    import curses
    curses.setupterm()
    if curses.tigetnum("colors") > 0:
        print(colorize("test", 1, 'green'))
        print(colorize("test", 0, 'red'))
    else:
        print(lead + '=%-4s' % str(num))
# --- end of "pretty"



# Generated at 2022-06-13 16:00:30.026152
# Unit test for function hostcolor
def test_hostcolor():
    # Note: these tests do not look for the colorization in the output since the
    #       curses library doesn't like being imported into the unit test
    assert hostcolor('myhost', {'changed': 0, 'unreachable': 0, 'failures': 0, 'ok': 1}, False) == 'myhost                 '
    assert hostcolor('myhost', {'changed': 0, 'unreachable': 0, 'failures': 0, 'ok': 1}, True) == 'myhost                 '
    assert hostcolor('myhost', {'changed': 0, 'unreachable': 0, 'failures': 1, 'ok': 0}, False) == 'myhost                 '
    assert hostcolor('myhost', {'changed': 0, 'unreachable': 0, 'failures': 1, 'ok': 0}, True) == 'myhost                 '
   

# Generated at 2022-06-13 16:00:41.133343
# Unit test for function colorize
def test_colorize():
    for color in C.COLOR_CODES:
        lead = u"%-15s" % color
        print (u"%s %s" % (lead, stringc(lead, color)))

# --- end "pretty"

# ANSI color definitions

# Generated at 2022-06-13 16:00:47.728485
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('localhost', dict(failures=1, unreachable=0, changed=0)) == u'\x1b[31mlocalhost              \x1b[0m'
    assert hostcolor('localhost', dict(failures=0, unreachable=1, changed=0)) == u'\x1b[31mlocalhost              \x1b[0m'
    assert hostcolor('localhost', dict(failures=0, unreachable=0, changed=1)) == u'\x1b[33mlocalhost              \x1b[0m'
    assert hostcolor('localhost', dict(failures=0, unreachable=0, changed=0)) == u'\x1b[32mlocalhost              \x1b[0m'

# Generated at 2022-06-13 16:01:02.832405
# Unit test for function colorize
def test_colorize():
    good = u"ok      = 1"
    skipped = u"skipped = 2"
    failed = u"failed  = 3"
    unreachable = u"unreachable = 4"
    changed = u"changed = 5"

    assert good == colorize(u"ok", 1, C.COLOR_OK)
    assert skipped == colorize(u"skipped", 2, C.COLOR_SKIP)
    assert failed == colorize(u"failed", 3, C.COLOR_ERROR)
    assert unreachable == colorize(u"unreachable", 4, C.COLOR_UNREACHABLE)
    assert changed == colorize(u"changed", 5, C.COLOR_CHANGED)
    assert good == colorize(u"ok", 1, None)

# --- end "pretty"

# Generated at 2022-06-13 16:01:14.658898
# Unit test for function hostcolor
def test_hostcolor():
    stats = {
        'changed': 0,
        'failures': 0,
        'ok': 1,
        'skipped': 0,
        'unreachable': 0
    }
    assert hostcolor('localhost', stats, color=True) == u"\033[0;32mlocalhost\033[0m%-10s"
    stats['changed'] = 1
    assert hostcolor('localhost', stats, color=True) == u"\033[0;33mlocalhost\033[0m%-10s"
    stats['changed'] = 0
    stats['failures'] = 1
    assert hostcolor('localhost', stats, color=True) == u"\033[0;31mlocalhost\033[0m%-10s"
    stats['failures'] = 0

# Generated at 2022-06-13 16:01:21.434829
# Unit test for function parsecolor
def test_parsecolor():
    assert u'38;5;15' == parsecolor('black')
    assert u'38;5;9' == parsecolor('darkred')
    assert u'38;5;8' == parsecolor('darkgreen')
    assert u'38;5;130' == parsecolor('lightblue')
    assert u'38;5;136' == parsecolor('lightcyan')
    assert u'38;5;7' == parsecolor('white')
    assert u'38;5;52' == parsecolor('yellow')
    assert u'38;5;88' == parsecolor('lightgreen')
    assert u'38;5;130' == parsecolor('color30')
    assert u'38;5;14' == parsecolor('cyan')

# Generated at 2022-06-13 16:01:31.540060
# Unit test for function hostcolor
def test_hostcolor():
    mock_stats = dict(failures=0, unreachable=0, changed=0)
    assert hostcolor("localhost", mock_stats, True) == "%-26s" % stringc("localhost", C.COLOR_OK)
    mock_stats = dict(failures=1, unreachable=0, changed=0)
    assert hostcolor("localhost", mock_stats, True) == "%-26s" % stringc("localhost", C.COLOR_ERROR)
    mock_stats = dict(failures=0, unreachable=1, changed=0)
    assert hostcolor("localhost", mock_stats, True) == "%-26s" % stringc("localhost", C.COLOR_ERROR)
    mock_stats = dict(failures=0, unreachable=0, changed=1)

# Generated at 2022-06-13 16:01:40.016602
# Unit test for function stringc

# Generated at 2022-06-13 16:01:49.252392
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor('red') == '31'
    assert parsecolor('bold') == '1'
    assert parsecolor('color1') == '38;5;1'
    assert parsecolor('color11') == '38;5;11'
    assert parsecolor('color111') == '38;5;111'
    assert parsecolor('rgb123') == '38;5;114'
    assert parsecolor('rgb333') == '38;5;255'
    assert parsecolor('rgb000') == '38;5;16'
    assert parsecolor('rgb555') == '38;5;185'
    assert parsecolor('rgb222') == '38;5;59'
    assert parsecolor('rgb255') == '38;5;231'
    assert parsecolor

# Generated at 2022-06-13 16:01:59.968785
# Unit test for function colorize
def test_colorize():
    """
    >>> colorize("test", 3, "blue")
    'test=3   '

    >>> colorize("test", 0, "blue")
    'test=0   '

    >>> colorize("test", -3, "blue")
    'test=-3  '

    >>> colorize("test", 12, "blue")
    'test=12  '

    >>> colorize("test", 123, "blue")
    'test=123 '

    >>> colorize("test", 1234, "blue")
    'test=1234'

    >>> colorize("test", 12345, "blue")
    'test=12345'
    """
    pass

# --- end of "pretty"

# a simple class to provide a file-like interface to stdout, stderr
# while ensuring everything stays in the proper color



# Generated at 2022-06-13 16:02:07.993776
# Unit test for function parsecolor
def test_parsecolor():
    # check if an invalid color raises an exception
    try:
        parsecolor(u'invalid color name')
    except:
        pass
    else:
        assert True, "exception was not raised for invalid color name"

    # check if valid color names are mapped to expected color codes

# Generated at 2022-06-13 16:02:14.297790
# Unit test for function hostcolor
def test_hostcolor():
    stats = dict(failures=0, unreachable=0, changed=0)
    assert hostcolor("test_host", stats) == "%-37s" % "test_host"
    stats['changed'] = 1
    assert hostcolor("test_host", stats, color=False) == u"%-26s" % "test_host"
    assert hostcolor("test_host", stats, color=True) == stringc("%-37s" % "test_host", C.COLOR_CHANGED)



# Generated at 2022-06-13 16:02:25.146812
# Unit test for function parsecolor
def test_parsecolor():

    # Basic colors
    assert parsecolor('red') == u'31'
    assert parsecolor('green') == u'32'
    assert parsecolor('yellow') == u'33'
    assert parsecolor('blue') == u'34'
    assert parsecolor('magenta') == u'35'
    assert parsecolor('cyan') == u'36'
    assert parsecolor('white') == u'37'

    # 256 colors using X11 colorscheme specification
    assert parsecolor('color1') == u'38;5;1'
    assert parsecolor('color252') == u'38;5;252'

    # 16 base colors
    assert parsecolor('color0') == u'38;5;16'
    assert parsecolor('color15') == u'38;5;231'



# Generated at 2022-06-13 16:02:41.391099
# Unit test for function stringc
def test_stringc():
    test_string = "This is a test string"

    # Test the default and no color override
    assert stringc(test_string, 'blue', False) == "\033[34mThis is a test string\033[0m"
    assert stringc(test_string, 'blue', True) == "\001\033[34m\002This is a test string\001\033[0m\002"
    assert stringc(test_string, None, False) == test_string
    assert stringc(test_string, None, True) == test_string

    # Test all the colors

# Generated at 2022-06-13 16:02:46.955120
# Unit test for function stringc
def test_stringc():
    """Unit test for function stringc."""
    # print all colors
    for color in C.COLOR_CODES:
        print(color)
        print(stringc('stringc', color))
        print(stringc('stringc', color, wrap_nonvisible_chars=True))
    # some gray values
    print(stringc('stringc', 'gray0'))
    print(stringc('stringc', 'gray1'))



# Generated at 2022-06-13 16:02:53.849927
# Unit test for function hostcolor
def test_hostcolor():
    hostcolor_test = {}
    hostcolor_test['name'] = 'test'
    hostcolor_test['changed'] = 0
    hostcolor_test['failures'] = 0
    hostcolor_test['unreachable'] = 0
    host_name = 'ansible-test'
    host_color = hostcolor(host_name, hostcolor_test)
    assert host_color == u"%-26s" % stringc(host_name, C.COLOR_OK), 'The hosts color is not OK'



# Generated at 2022-06-13 16:03:00.614860
# Unit test for function stringc
def test_stringc():
    # Expected value is the same as the actual because C.COLOR_ERROR
    # is a string of ANSI sequences, and so ANSIBLE_COLOR is True
    # and the value remains unchanged
    assert stringc(u"ERROR", C.COLOR_ERROR) == u"\033[1m\033[91mERROR\033[0m"
    assert stringc(u"ERROR", None) == u"ERROR"


__all__ = ['stringc', 'colorize', 'hostcolor']

# Generated at 2022-06-13 16:03:08.289907
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor("000102030405060708090a0b0c0d0e0f") == "38;5;16"
    assert parsecolor("00000000000000000000000000000000") == "38;5;16"
    assert parsecolor("color16") == "38;5;16"
    assert parsecolor("color1") == "38;5;1"
    assert parsecolor("rgb555") == "38;5;232"
    assert parsecolor("rgb444") == "38;5;59"
    assert parsecolor("rgbabc") == "38;5;33"
    assert parsecolor("rgb123") == "38;5;18"
    assert parsecolor("rgb000") == "38;5;16"

# Generated at 2022-06-13 16:03:17.701857
# Unit test for function colorize
def test_colorize():
    import ansible.constants as C

    # Test with ANSIBLE_COLOR disabled
    ANSIBLE_COLOR = False
    colorize(C.HOST_KEY, 1, C.COLOR_ERROR)
    colorize(C.HOST_KEY, 1, C.COLOR_CHANGED)
    colorize(C.HOST_KEY, 1, C.COLOR_OK)
    colorize(C.HOST_KEY, 0, C.COLOR_OK)

    # Test with ANSIBLE_COLOR enabled
    ANSIBLE_COLOR = True
    colorize(C.HOST_KEY, 1, C.COLOR_ERROR)
    colorize(C.HOST_KEY, 1, C.COLOR_CHANGED)
    colorize(C.HOST_KEY, 1, C.COLOR_OK)

# Generated at 2022-06-13 16:03:23.702199
# Unit test for function colorize
def test_colorize():
    class DummyOpts(object):
        color = 'yes'
        nocolor = False

    # Check simple number
    assert colorize('test', 0, 'blue') == stringc('test=0', 'blue')
    assert colorize('test', 1, 'blue') == stringc('test=1', 'blue')

    # Check number with padding
    assert colorize('test', 10, 'blue') == stringc('test=10 ', 'blue')

# Generated at 2022-06-13 16:03:27.550115
# Unit test for function stringc
def test_stringc():
    """
    >>> stringc("test", "red")
    u'\\x1b[31mtest\\x1b[0m'
    >>> stringc("test", "blue")
    u'\\x1b[34mtest\\x1b[0m'
    >>> stringc("test", "not a real color")
    u'test'
    """
    pass


# Generated at 2022-06-13 16:03:39.277218
# Unit test for function parsecolor

# Generated at 2022-06-13 16:03:44.202922
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor(u"black") == u"30"
    assert parsecolor(u"red") == u"31"
    assert parsecolor(u"green") == u"32"
    assert parsecolor(u"yellow") == u"33"
    assert parsecolor(u"blue") == u"34"
    assert parsecolor(u"magenta") == u"35"
    assert parsecolor(u"cyan") == u"36"
    assert parsecolor(u"white") == u"37"
    assert parsecolor(u"color0") == u"38;5;0"
    assert parsecolor(u"color1") == u"38;5;1"
    assert parsecolor(u"color2") == u"38;5;2"

# Generated at 2022-06-13 16:03:51.429864
# Unit test for function stringc
def test_stringc():
    assert stringc("foo", "cyan") == "\033[36mfoo\033[0m"
    assert stringc("foo\nbar", "cyan") == "\033[36mfoo\033[0m\n\033[36mbar\033[0m"



# Generated at 2022-06-13 16:04:03.201283
# Unit test for function hostcolor
def test_hostcolor():
    s = {'ok': 0, 'errors': 0, 'dark': 0,
         'changed': 1, 'skipped': 0, 'failures': 0,
         'unreachable': 0}
    assert hostcolor('localhost', s) == u"localhost                   "
    s = {'ok': 0, 'errors': 0, 'dark': 0,
         'changed': 1, 'skipped': 0, 'failures': 1,
         'unreachable': 0}
    assert hostcolor('localhost', s) == u"localhost                   "
    s = {'ok': 0, 'errors': 0, 'dark': 0,
         'changed': 0, 'skipped': 0, 'failures': 1,
         'unreachable': 0}
    assert hostcolor('localhost', s) == u"localhost                   "

# Generated at 2022-06-13 16:04:03.825609
# Unit test for function hostcolor

# Generated at 2022-06-13 16:04:11.824902
# Unit test for function stringc
def test_stringc():
    assert stringc('text', 'blue') == u'\033[34mtext\033[0m'
    assert stringc('text', color='red') == u'\033[31mtext\033[0m'
    assert stringc(text='text', color='red') == u'\033[31mtext\033[0m'
    assert stringc('text', color='rgb123') == \
        u'\033[38;5;111mtext\033[0m'
    assert stringc('text', color='rgb333') == \
        u'\033[38;5;202mtext\033[0m'
    assert stringc('text', color='rgb555') == \
        u'\033[38;5;231mtext\033[0m'

# Generated at 2022-06-13 16:04:17.723480
# Unit test for function parsecolor
def test_parsecolor():
    # Test a regular color name
    assert parsecolor('blue') == u'38;5;4'

    # Test a gray color
    assert parsecolor('gray2') == u'38;5;242'

    # Test an RGB color
    assert parsecolor('rgb124') == u'38;5;104'

# --- end "pretty"



# Generated at 2022-06-13 16:04:28.313845
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor("blue") == u"34"
    assert parsecolor("color8") == u"38;5;8"
    assert parsecolor("color16") == u"38;5;16"
    assert parsecolor("color255") == u"38;5;255"

    # ANSI color 0-7
    for i in range(8):
        assert parsecolor("color%d" % i) == "38;5;%d" % i

    # ANSI color 16-255
    for i in range(16, 256):
        assert parsecolor("color%d" % i) == "38;5;%d" % i

    # xterm grayscale (only works in 256 color mode)
    for i in range(24):
        c = 232 + i

# Generated at 2022-06-13 16:04:37.633555
# Unit test for function hostcolor
def test_hostcolor():
    stats = {'failures': 0, 'unreachable': 0, 'ok': 1, 'changed': 0,
             'skipped': 0}
    assert hostcolor("localhost", stats) == "localhost"
    assert hostcolor("localhost", stats, color=False) == "localhost"
    stats = {'failures': 1, 'unreachable': 0, 'ok': 0, 'changed': 0,
             'skipped': 0}
    assert hostcolor("localhost", stats) != "localhost"
    assert hostcolor("localhost", stats, color=False) == "localhost"
    stats = {'failures': 0, 'unreachable': 0, 'ok': 0, 'changed': 1,
             'skipped': 0}
    assert hostcolor("localhost", stats) != "localhost"
    assert hostcolor("localhost", stats, color=False)

# Generated at 2022-06-13 16:04:47.839379
# Unit test for function hostcolor
def test_hostcolor():
    import ansible.constants as C
    from ansible.utils.color import hostcolor
    test_hosts = {"127.0.0.1": {"failures": 0, "unreachable": 0, "ok": 5, "changed": 0, "skipped": 0},
                  "127.0.0.2": {"failures": 1, "unreachable": 0, "ok": 4, "changed": 0, "skipped": 0},
                  "127.0.0.3": {"failures": 0, "unreachable": 3, "ok": 2, "changed": 0, "skipped": 0},
                  "127.0.0.4": {"failures": 0, "unreachable": 0, "ok": 5, "changed": 1, "skipped": 0}}
    # Testing without color

# Generated at 2022-06-13 16:04:50.428311
# Unit test for function stringc
def test_stringc():
    """ Verify that function stringc colors strings correctly. """

    # TODO

    pass


# --- end "pretty"

# Generated at 2022-06-13 16:04:59.206419
# Unit test for function hostcolor
def test_hostcolor():
    fake_stats = {'failures': 0, 'unreachable': 0, 'changed': 0}
    assert hostcolor('example.com', fake_stats, color=False) == 'example.com                    '
    assert hostcolor('example.com', fake_stats, color=True) == u'example.com                    '
    fake_stats['changed'] = 1
    assert hostcolor('example.com', fake_stats, color=False) == 'example.com                    '
    assert hostcolor('example.com', fake_stats, color=True) == u'\u001b[32;01mexample.com\u001b[0m'
    fake_stats['unreachable'] = 1
    assert hostcolor('example.com', fake_stats, color=False) == 'example.com                    '

# Generated at 2022-06-13 16:05:13.662469
# Unit test for function stringc
def test_stringc():
    # Test color 0-15
    for i in range(16):
        text = stringc('test: %d' % i, str(i))
        assert text == u'\u001b[38;5;%dmtest: %d\u001b[0m' % (i, i)

    # Test colour 16-231 (RGB)
    for i in range(216):
        text = stringc('test: %d' % i, 'rgb%d%d%d' % ((i//36) % 6, (i//6) % 6, i % 6))
        assert text == u'\u001b[38;5;%dmtest: %d\u001b[0m' % (i + 16, i)

    # Test colour 232-255 (grayscale)

# Generated at 2022-06-13 16:05:21.141532
# Unit test for function stringc
def test_stringc():
    colors = ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white',
              'black')
    bgColors = ('on_red', 'on_green', 'on_yellow', 'on_blue', 'on_magenta',
                'on_cyan', 'on_white', 'on_black')
    attrs = ('bold', 'dark', '', 'underline', 'blink', 'reverse', 'concealed')
    string = 'This is a colorful test!'
    string = string.split()

# Generated at 2022-06-13 16:05:24.705718
# Unit test for function stringc
def test_stringc():
    for color in C.COLOR_CODES:
        print("%s: %s" % (color, stringc("I'm %s!" % color, color)))

# For testing
if __name__ == '__main__':
    test_stringc()

# Generated at 2022-06-13 16:05:35.766890
# Unit test for function hostcolor
def test_hostcolor():
    # test string with ANSI color chars
    ansi_str = u'\x1b[0;35mtest\x1b[0m'
    # expected result without ANSI color chars
    no_color = u'test'
    # test a basic string
    assert hostcolor('test', {}) == u'%-26s' % no_color
    # test a string with color
    assert hostcolor('test', {}, True) == u'%-37s' % ansi_str
    # test a string with color (explicit)
    assert hostcolor('test', {}, color=True) == u'%-37s' % ansi_str
    # test a string with color (explicit False)
    assert hostcolor('test', {}, color=False) == u'%-26s' % no_color
    # test a string with

# Generated at 2022-06-13 16:05:44.333719
# Unit test for function stringc
def test_stringc():
    if not ANSIBLE_COLOR:
        print("Color is disabled")
        return

    # named colors
    print(u"Named colors:")
    for i in C.COLOR_CODES.keys():
        print(stringc(i, i))

    # color using numbers
    print(u"\nColors using numbers:")
    for i in range(1, 10):
        print(stringc(u"color" + str(i), "color" + str(i)))
    for i in range(1, 23):
        print(stringc(u"gray" + str(i), "gray" + str(i)))
    # rgb colors
    print(u"\nColors using rgb:")

# Generated at 2022-06-13 16:05:51.617652
# Unit test for function hostcolor
def test_hostcolor():
    stats1 = dict(skipped=0, ok=0, changed=0, unreachable=0, failures=0)
    stats2 = dict(skipped=1, ok=0, changed=0, unreachable=0, failures=0)
    stats3 = dict(skipped=0, ok=1, changed=0, unreachable=0, failures=0)
    stats4 = dict(skipped=0, ok=0, changed=1, unreachable=0, failures=0)
    stats5 = dict(skipped=0, ok=0, changed=0, unreachable=1, failures=0)
    stats6 = dict(skipped=0, ok=0, changed=0, unreachable=0, failures=1)

# Generated at 2022-06-13 16:06:02.857461
# Unit test for function colorize
def test_colorize():
    assert colorize('foo', 0, 'black') == 'foo=0   '
    assert colorize('foo', 0, None) == 'foo=0   '
    assert colorize('foo', 1, 'black') == stringc('foo=1   ', 'black')
    assert colorize('foo', 2, 'blue') == stringc('foo=2   ', 'blue')
    assert colorize('foo', 3, 'cyan') == stringc('foo=3   ', 'cyan')
    assert colorize('foo', 4, 'green') == stringc('foo=4   ', 'green')
    assert colorize('foo', 5, 'magenta') == stringc('foo=5   ', 'magenta')
    assert colorize('foo', 6, 'red') == stringc('foo=6   ', 'red')

# Generated at 2022-06-13 16:06:14.649890
# Unit test for function stringc
def test_stringc():
    print(stringc('hello', 'white', False))
    print(stringc('hello', 'white', True))
    print(stringc('hello', 'blue', False))
    print(stringc('hello', 'blue', True))
    print(stringc('hello', '0', False))
    print(stringc('hello', '1', False))
    print(stringc('hello', '00', False))
    print(stringc('hello', '01', False))
    print(stringc('hello', '5', False))
    print(stringc('hello', '05', False))
    print(stringc('hello', '255', False))
    print(stringc('hello', '2555', False))
    print(stringc('hello', '25', False))
    print(stringc('hello', '22', False))
    print

# Generated at 2022-06-13 16:06:23.077419
# Unit test for function colorize
def test_colorize():
    """Run unit test for function colorize"""
    if ANSIBLE_COLOR:
        print(colorize('ok', 0, 'green'))
        print(colorize('changed', 0, 'yellow'))
        print(colorize('unreachable', 0, 'red'))
        print(colorize('failed', 0, 'red'))
        print(colorize('ok', 1, 'green'))
        print(colorize('changed', 1, 'yellow'))
        print(colorize('unreachable', 1, 'red'))
        print(colorize('failed', 1, 'red'))



# Generated at 2022-06-13 16:06:34.623169
# Unit test for function stringc
def test_stringc():
    assert stringc(u'foo', u'green', wrap_nonvisible_chars=True) == u'\001\033[32m\002foo\001\033[0m\002'
    assert stringc(u'foo', u'BLUE', wrap_nonvisible_chars=True) == u'\001\033[34m\002foo\001\033[0m\002'
    assert stringc(u'foo\nbar\nbaz', u'yellow', wrap_nonvisible_chars=True) == u'\001\033[33m\002foo\nbar\nbaz\001\033[0m\002'

# Generated at 2022-06-13 16:06:54.189123
# Unit test for function stringc
def test_stringc():
    if ANSIBLE_COLOR:
        # color name
        assert stringc('bar', 'red') == "\033[91mbar\033[0m"

        # color number (not as bright as the name)
        assert stringc('bar', 'color1') == "\033[38;5;9mbar\033[0m"

        # same as above
        assert stringc('bar', 'rgb100') == "\033[38;5;9mbar\033[0m"

        # gray number
        assert stringc('bar', 'gray1') == "\033[38;5;233mbar\033[0m"

        # gray number (not as bright as the name)
        assert stringc('bar', 'gray8') == "\033[38;5;240mbar\033[0m"

        # tester for wrap_

# Generated at 2022-06-13 16:07:02.795861
# Unit test for function stringc
def test_stringc():
    def test_output(value, output):
        if value != output: return 1
        return 0
    assert test_output(stringc('test', 'normal'), 'test') == 0
    assert test_output(stringc('test', 'red'), '\x1b[31mtest\x1b[0m') == 0
    assert test_output(stringc('test', 'rgb300'), '\x1b[38;5;11mtest\x1b[0m') == 0
    assert test_output(stringc('test', 'rgb322', True), '\x01\x1b[38;5;50m\x02test\x01\x1b[0m\x02') == 0

# Generated at 2022-06-13 16:07:12.965842
# Unit test for function stringc
def test_stringc():
    """Test the stringc function."""

    assert stringc("Hello", "red") == '\001\033[31m\002Hello\001\033[0m\002'
    assert stringc("Hello", "CYAN") == '\001\033[36m\002Hello\001\033[0m\002'
    assert stringc("Hello", "Green") == '\001\033[32m\002Hello\001\033[0m\002'
    assert stringc("Hello", "YELLOW") == '\001\033[33m\002Hello\001\033[0m\002'
    assert stringc("Hello", "magenta") == '\001\033[35m\002Hello\001\033[0m\002'


# Generated at 2022-06-13 16:07:14.380647
# Unit test for function colorize
def test_colorize():
    pass

# --- end "pretty"


# Generated at 2022-06-13 16:07:21.622153
# Unit test for function stringc
def test_stringc():
    def color_test(color, expected_color_code, expected_color_string):
        color_code = parsecolor(color)
        assert color_code == expected_color_code
        assert stringc("test", color) == expected_color_string

    # Test truecolor
    color_test("color256", "38;5;256", "\033[38;5;256mtest\033[0m")
    color_test("color15", "38;5;15", "\033[38;5;15mtest\033[0m")
    color_test("color0", "38;5;0", "\033[38;5;0mtest\033[0m")

    # Test rgb

# Generated at 2022-06-13 16:07:28.950850
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('foobar', {'failures': 0, 'unreachable': 0, 'changed': 0}) == u"%-37s" % 'foobar'
    assert hostcolor('foobar', {'failures': 0, 'unreachable': 0, 'changed': 1}) == u'%-37s' % stringc('foobar', C.COLOR_CHANGED)
    assert hostcolor('foobar', {'failures': 0, 'unreachable': 1, 'changed': 0}) == u'%-37s' % stringc('foobar', C.COLOR_ERROR)
    assert hostcolor('foobar', {'failures': 1, 'unreachable': 0, 'changed': 0}) == u'%-37s' % stringc('foobar', C.COLOR_ERROR)

# Generated at 2022-06-13 16:07:34.237052
# Unit test for function stringc
def test_stringc():
    """ Test if stringc() function displays the expected output """


# Generated at 2022-06-13 16:07:39.810139
# Unit test for function stringc
def test_stringc():
    result = stringc("Hello World", "red")
    assert result == u"\033[31mHello World\033[0m"
    assert stringc("Hello World", 'color1') == u"\033[38;5;1mHello World\033[0m"
    assert stringc("Hello World", 'rgb123') == u"\033[38;5;94mHello World\033[0m"
    # print stringc("Hello World", 'rgb123')
    assert stringc("Hello World", 'rgb000', True) == u"\001\033[38;5;16m\002Hello World\001\033[0m\002"

# --- end "pretty"

# Generated at 2022-06-13 16:07:45.736701
# Unit test for function hostcolor
def test_hostcolor():
    from ansible.utils.color import hostcolor
    from ansible.utils.color import stringc
    host = 'some_host'
    stats_changed = dict(failures=0, unreachable=0, changed=1)
    stats_failures = dict(failures=1, unreachable=0, changed=0)
    stats_unreachable = dict(failures=0, unreachable=1, changed=0)
    stats_ok = dict(failures=0, unreachable=0, changed=0)

    # Test ANSIBLE_COLOR=False
    colorized = hostcolor(host, stats_changed)
    if colorized != host:
        raise AssertionError("Unexpected colorized string: %s" % colorized)

    # Test ANSIBLE_COLOR=True, stats=stats_failures
    colorized

# Generated at 2022-06-13 16:07:55.639222
# Unit test for function hostcolor
def test_hostcolor():
    host_unreachable = dict(changed=0, failures=0, ok=5, skipped=0, unreachable=1)
    host_failures = dict(changed=0, failures=1, ok=5, skipped=0, unreachable=0)
    host_changed = dict(changed=1, failures=0, ok=5, skipped=0, unreachable=0)
    host_ok = dict(changed=0, failures=0, ok=5, skipped=0, unreachable=0)
    assert hostcolor('test', host_unreachable, False) == "test               "
    assert hostcolor('test', host_unreachable) == u"test               "
    assert hostcolor('test', host_failures, False) == "test               "
    assert hostcolor('test', host_failures) == u"test               "


# Generated at 2022-06-13 16:08:13.460260
# Unit test for function stringc
def test_stringc():
    """Test ANSIBLE_COLOR."""

# Generated at 2022-06-13 16:08:23.015185
# Unit test for function stringc
def test_stringc():
    """Unit test for function stringc."""
    def fmt(c, t):
        return u"\033[%sm%s\033[0m" % (parsecolor(c), t)

    assert stringc('hello', 'blue') == fmt('blue', 'hello')
    assert stringc('hello', 'blue', wrap_nonvisible_chars=True) == u'\001\033[38;5;4m\002hello\001\033[0m\002'
    assert stringc('hello', 'blue on yellow') == stringc('hello', 'blue', wrap_nonvisible_chars=True)
    assert stringc('hello', 'red') == fmt('red', 'hello')
    assert stringc('hello', 'red on yellow') == fmt('red', 'hello')
    assert stringc('hello', 'green') == fmt

# Generated at 2022-06-13 16:08:29.428542
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor("hi", {'changed': 0, 'failures': 0, 'ok': 1, 'skipped': 0, 'unreachable': 0}) == "hi                           "
    assert hostcolor("hi", {'changed': 1, 'failures': 0, 'ok': 1, 'skipped': 0, 'unreachable': 0}) == u"\033[0;32mhi\033[0m                     "
    assert hostcolor("hi", {'changed': 1, 'failures': 1, 'ok': 1, 'skipped': 0, 'unreachable': 0}) == u"\033[0;31mhi\033[0m                     "

# Generated at 2022-06-13 16:08:36.050567
# Unit test for function colorize
def test_colorize():
    from six import StringIO
    def p(s):
        return s if s else u" "


# Generated at 2022-06-13 16:08:46.148845
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor("localhost", {"failures": 0, "changed": 0, "unreachable": 0}) == "%-37s" % "localhost"
    assert hostcolor("localhost", {"failures": 0, "changed": 1, "unreachable": 0}) == "%-37s" % stringc("localhost", C.COLOR_CHANGED)
    assert hostcolor("localhost", {"failures": 1, "changed": 0, "unreachable": 0}) == "%-37s" % stringc("localhost", C.COLOR_ERROR)
    assert hostcolor("localhost", {"failures": 0, "changed": 0, "unreachable": 1}) == "%-37s" % stringc("localhost", C.COLOR_ERROR)
    # We disable color by default, so force it to be True
    ANSIBLE_COLOR = True

# Generated at 2022-06-13 16:08:57.533762
# Unit test for function hostcolor
def test_hostcolor():
    host = 'www.example.com'
    stats = {'failures': 0, 'unreachable': 0, 'ok': 8, 'changed': 0, 'skipped': 0}
    assert hostcolor(host, stats) == '%-37s' % u"\033[0;32m%s\033[0m" % host
    stats = {'failures': 0, 'unreachable': 0, 'ok': 0, 'changed': 8, 'skipped': 0}
    assert hostcolor(host, stats) == '%-37s' % u"\033[0;33m%s\033[0m" % host
    stats = {'failures': 0, 'unreachable': 0, 'ok': 0, 'changed': 0, 'skipped': 8}

# Generated at 2022-06-13 16:09:05.571973
# Unit test for function colorize
def test_colorize():
    """colorize - A function to turn text red, green, or blue
    Usage: test_colorize()
    """
    good = u"success!"
    bad = u"failure!"
    print(u"\nShould see two green lines and two red ones:")
    print(colorize(good, 0, C.COLOR_OK))
    print(colorize(good, 1, C.COLOR_OK))
    print(colorize(bad, 0, C.COLOR_ERROR))
    print(colorize(bad, 1, C.COLOR_ERROR))

#
# --- end "pretty"
#

# --- begin "minimal"
#
# minimal.py - a minimal ansible module
#
# (c) 2013, Michael DeHaan <michael.dehaan@gmail.com>
#
# This file is part

# Generated at 2022-06-13 16:09:15.917174
# Unit test for function colorize
def test_colorize():
    # pylint: disable=protected-access
    assert parsecolor('red') == u'31'
    assert parsecolor('green') == u'32'
    assert parsecolor('blue') == u'34'
    assert parsecolor('cyan') == u'36'
    assert parsecolor('bright red') == u'91'
    assert parsecolor('bright green') == u'92'
    assert parsecolor('bright blue') == u'94'
    assert parsecolor('bright cyan') == u'96'
    assert parsecolor('color8') == u'38;5;8'
    assert parsecolor('color16') == u'38;5;16'
    assert parsecolor('color255') == u'38;5;255'

# Generated at 2022-06-13 16:09:23.041035
# Unit test for function stringc

# Generated at 2022-06-13 16:09:31.568587
# Unit test for function stringc
def test_stringc():
    for color in ('black', 'red', 'green', 'yellow', 'blue',
                  'magenta', 'cyan', 'white', 'color236', 'rgb123', 'gray17'):
        msg = u"test msg in %s color" % color
        print(u"%-20s: %s" % (u'"%s"' % msg, stringc(msg, color)))


# --- end "pretty"

# pager

# CONTROL_CHARS = set(unichr(x) for x in range(32))
# CONTROL_CHARS.add(u'\x7f')
# CONTROL_CHAR_RE = re.compile(u"[%s]" % re.escape(u''.join(CONTROL_CHARS)))
# RE_COLOR_CODES = re.compile(u"\033\[(