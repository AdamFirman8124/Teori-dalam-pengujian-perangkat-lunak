

# Generated at 2022-06-13 15:59:43.350647
# Unit test for function parsecolor
def test_parsecolor():
    def test_color(color, expected):
        assert parsecolor(color) == expected

    test_color("red", u'38;5;1')
    test_color("green", u'38;5;2')
    test_color("yellow", u'38;5;3')
    test_color("blue", u'38;5;4')
    test_color("magenta", u'38;5;5')
    test_color("cyan", u'38;5;6')
    test_color("white", u'38;5;7')
    test_color("dark gray", u'38;5;8')
    test_color("light red", u'38;5;9')
    test_color("light green", u'38;5;10')

# Generated at 2022-06-13 15:59:53.480550
# Unit test for function colorize
def test_colorize():
    """colorize - Unit test for function colorize"""
    assert colorize(u"foo", 0, u"blue") == u"foo=0   "
    assert colorize(u"foo", 1, u"blue") == u"foo=1   "
    assert colorize(u"fool", 10, u"blue") == u"fool=10 "
    assert colorize(u"f", 10, u"blue") == u"f=10    "
    assert colorize(u"f", 100, u"blue") == u"f=100   "
    assert colorize(u"f", 1000, u"blue") == u"f=1000  "
    assert colorize(u"f", 10000, u"blue") == u"f=10000 "


# --- end of "pretty" ---

# Disable pylint message:

# Generated at 2022-06-13 16:00:02.607810
# Unit test for function hostcolor
def test_hostcolor():
    stats = {'failures': 0, 'changed': 0, 'unreachable': 0}
    assert hostcolor('localhost', stats) == u'%-37s' % stringc('localhost', C.COLOR_OK)
    stats['failures'] = 1
    assert hostcolor('localhost', stats) == u'%-37s' % stringc('localhost', C.COLOR_ERROR)
    stats['unreachable'] = 1
    assert hostcolor('localhost', stats) == u'%-37s' % stringc('localhost', C.COLOR_ERROR)
    stats['unreachable'] = 0
    stats['changed'] = 1
    assert hostcolor('localhost', stats) == u'%-37s' % stringc('localhost', C.COLOR_CHANGED)
    stats['changed'] = 0

# Generated at 2022-06-13 16:00:09.176279
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('red', dict(
        changed=10,
        failures=0,
        ok=10,
        skipped=0,
        unreachable=0,
        res=dict(
            skipped=0,
            failed=0,
            changed=0,
            ok=0,
        ),
    ), True) == '\x1b[31mred               \x1b[0m'

    assert hostcolor('yellow', dict(
        changed=10,
        failures=0,
        ok=10,
        skipped=0,
        unreachable=0,
        res=dict(
            skipped=0,
            failed=0,
            changed=0,
            ok=0,
        ),
    ), True) == '\x1b[33myellow            \x1b[0m'

    assert host

# Generated at 2022-06-13 16:00:18.881459
# Unit test for function stringc
def test_stringc():
    """ Tests for function stringc """
    assert stringc('test', 'blue') == '\033[34mtest\033[0m'
    assert stringc('test', 'color3') == '\033[38;5;55mtest\033[0m'
    assert stringc('test', 'color03') == '\033[38;5;55mtest\033[0m'
    assert stringc('test', 'color003') == '\033[38;5;55mtest\033[0m'
    assert stringc('test', 'color0003') == '\033[34mtest\033[0m'
    assert stringc('test', 'rgb123') == '\033[38;5;75mtest\033[0m'

# Generated at 2022-06-13 16:00:29.825078
# Unit test for function parsecolor
def test_parsecolor():
    # colorN
    print("Testing parsecolor colorN...")
    assert(parsecolor("color1") == '38;5;1')
    assert(parsecolor("color0") == '38;5;0')
    assert(parsecolor("color15") == '38;5;15')
    assert(parsecolor("color16") == '38;5;16')
    assert(parsecolor("color235") == '38;5;235')
    assert(parsecolor("color236") == '38;5;236')
    assert(parsecolor("color255") == '38;5;255')
    print("Passed!")

    # grayN
    print("Testing parsecolor grayN...")
    assert(parsecolor("gray0") == '38;5;232')

# Generated at 2022-06-13 16:00:37.247574
# Unit test for function stringc
def test_stringc():
    if ANSIBLE_COLOR:
        assert stringc("foo", "red") == u"\x1b[31mfoo\x1b[0m"
        assert stringc("foo", "blue") == u"\x1b[34mfoo\x1b[0m"
    else:
        assert stringc("foo", "red") == u"foo"
        assert stringc("foo", "blue") == u"foo"

# --- end "pretty"



# Generated at 2022-06-13 16:00:45.439201
# Unit test for function parsecolor
def test_parsecolor():
    """Test function parsecolor"""

    assert parsecolor("black") == u"30"
    assert parsecolor("red") == u"31"
    assert parsecolor("green") == u"32"
    assert parsecolor("yellow") == u"33"
    assert parsecolor("blue") == u"34"
    assert parsecolor("magenta") == u"35"
    assert parsecolor("cyan") == u"36"
    assert parsecolor("white") == u"37"

    assert parsecolor("brightblack") == u"30;1"
    assert parsecolor("brightred") == u"31;1"
    assert parsecolor("brightgreen") == u"32;1"
    assert parsecolor("brightyellow") == u"33;1"

# Generated at 2022-06-13 16:00:53.101799
# Unit test for function parsecolor
def test_parsecolor():
    if not ANSIBLE_COLOR:
        return
    code = parsecolor('blue')
    if code != u'34':
        raise Exception("SGR parameter for blue should be 34")
    code = parsecolor('bright blue')
    if code != u'94':
        raise Exception("SGR parameter for bright blue should be 94")
    code = parsecolor('color27')
    if code != u'38;5;27':
        raise Exception("SGR parameter for color27 should be 38;5;27")
    code = parsecolor('rgb2553325')
    if code != u'38;5;215':
        raise Exception("SGR parameter for rgb2553325 should be 38;5;215")
    code = parsecolor('gray3')
    if code != u'38;5;235':
        raise Exception

# Generated at 2022-06-13 16:00:58.934692
# Unit test for function colorize
def test_colorize():
    assert ANSIBLE_COLOR
    assert colorize("foo", 0, "black") == u'foo=0   \033[0m'
    assert colorize("foo", 1, "red") == stringc(u'foo=1   ', 'red')
    assert colorize("foo", 2, None) == u'foo=2   '

# End of pretty library
# ---


# Generated at 2022-06-13 16:01:14.866259
# Unit test for function stringc
def test_stringc():
    assert stringc("Hello world", "blue") == "\033[34mHello world\033[0m"
    assert stringc("Hello world", "black") == "\033[30mHello world\033[0m"
    assert stringc("Hello world", "red") == "\033[31mHello world\033[0m"
    assert stringc("Hello world", "pink") == "\033[35mHello world\033[0m"
    assert stringc("Hello world", "green") == "\033[32mHello world\033[0m"
    assert stringc("Hello world", "grey") == "\033[37mHello world\033[0m"
    assert stringc("Hello world", "blue") == "\033[34mHello world\033[0m"

# Generated at 2022-06-13 16:01:21.604162
# Unit test for function hostcolor
def test_hostcolor():
    stats_ok = dict(changed=0, unreachable=0, failures=0)
    stats_fail = dict(changed=0, unreachable=0, failures=1)
    stats_unreachable = dict(changed=0, unreachable=1, failures=0)
    stats_changed = dict(changed=1, unreachable=0, failures=0)
    assert hostcolor("ok", stats_ok, True) == stringc("ok", C.COLOR_OK)
    assert hostcolor("fail", stats_fail, True) == stringc("fail", C.COLOR_ERROR)
    assert hostcolor("unreachable", stats_unreachable, True) == stringc("unreachable", C.COLOR_ERROR)
    assert hostcolor("changed", stats_changed, True) == stringc("changed", C.COLOR_CHANGED)




# Generated at 2022-06-13 16:01:25.513683
# Unit test for function stringc
def test_stringc():
    assert stringc('Hello World', 'blue') == u"\033[34mHello World\033[0m"
    assert stringc('Hello World', 'x') == u'Hello World'



# Generated at 2022-06-13 16:01:33.546078
# Unit test for function stringc

# Generated at 2022-06-13 16:01:44.072975
# Unit test for function hostcolor
def test_hostcolor():
    stats = dict(failures=1, unreachable=0, changed=1)
    assert hostcolor('www', stats, False) == u"%-26s" % 'www'
    assert hostcolor('www', stats, True) == u"%-37s" % stringc('www', C.COLOR_ERROR)
    stats.update(dict(failures=0, unreachable=1, changed=0))
    assert hostcolor('www', stats, False) == u"%-26s" % 'www'
    assert hostcolor('www', stats, True) == u"%-37s" % stringc('www', C.COLOR_ERROR)
    stats.update(dict(failures=0, unreachable=0, changed=1))
    assert hostcolor('www', stats, False) == u"%-26s" % 'www'
    assert hostcolor

# Generated at 2022-06-13 16:01:53.912950
# Unit test for function colorize
def test_colorize():
    assert colorize(u"foo", 0, u"blue") == u"foo=0   "
    assert colorize(u"foo", 1, u"blue") == u"foo=1   "
    assert colorize(u"foo", 2, u"blue") == u"foo=2   "
    assert colorize(u"foo", 3, u"blue") == u"foo=3   "
    assert colorize(u"foo", 4, u"blue") == u"foo=4   "
    assert colorize(u"foo", 5, u"blue") == u"foo=5   "
    assert colorize(u"foo", 6, u"blue") == u"foo=6   "
    assert colorize(u"foo", 7, u"blue") == u"foo=7   "

# Generated at 2022-06-13 16:01:58.905480
# Unit test for function stringc
def test_stringc():
    assert stringc(u"foo", u"red") == u"\033[31mfoo\033[0m"
    assert stringc(u"foo", u"red", wrap_nonvisible_chars=True) == u"\001\033[31m\002foo\001\033[0m\002"
    # Test extended color values
    assert stringc(u"foo", u"color2") == u"\033[38;5;2mfoo\033[0m"
    assert stringc(u"foo", u"color2", wrap_nonvisible_chars=True) == u"\001\033[38;5;2m\002foo\001\033[0m\002"

# Generated at 2022-06-13 16:02:03.126201
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor("blue") == "34"
    assert parsecolor("bold") == "1"
    assert parsecolor("35") == "35"
    assert parsecolor("on_blue") == "44"
    assert parsecolor("on_red") == "41"
    assert parsecolor("underline") == "4"
    assert parsecolor("blink") == "5"



# Generated at 2022-06-13 16:02:10.158448
# Unit test for function hostcolor
def test_hostcolor():
    from ansible.utils.color import hostcolor
    assert hostcolor("host", dict(changed=0, unreachable=0, failures=0, ok=0, skipped=0)) == u"host                 "
    assert hostcolor("host", dict(changed=1, unreachable=0, failures=0, ok=0, skipped=0)) == u"host                 "
    assert hostcolor("host", dict(changed=0, unreachable=1, failures=0, ok=0, skipped=0)) == u"host                 "
    assert hostcolor("host", dict(changed=0, unreachable=0, failures=1, ok=0, skipped=0)) == u"host                 "
    assert hostcolor("host", dict(changed=0, unreachable=0, failures=0, ok=1, skipped=0)) == u"host                 "


# Generated at 2022-06-13 16:02:11.382700
# Unit test for function colorize
def test_colorize():
    from ansible.cli.color import colorize
    pass

# --- end of pretty library

# Generated at 2022-06-13 16:02:22.822512
# Unit test for function stringc
def test_stringc():
    import time
    # palette[0] is black, palette[15] is white
    palette = ['000000', '800000', '008000', '808000', '000080', '800080',
               '008080', 'c0c0c0', '808080', 'ff0000', '00ff00', 'ffff00',
               '0000ff', 'ff00ff', '00ffff', 'ffffff']
    for foreground in range(0, 16):
        for background in range(0, 16):
            testcolor = palette[foreground] + palette[background]
            colored_color = stringc('color%s # foreground = %d, background = %d' % (testcolor, foreground, background),
                                    'color%s' % testcolor)

# Generated at 2022-06-13 16:02:26.148175
# Unit test for function colorize
def test_colorize():
    colors = ('black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white')
    string = 'the quick brown fox jumps over the lazy dog'
    for c in colors:
        print('%-9s' % c, stringc(string, c))


# This is the end of "pretty"
# ---



# Generated at 2022-06-13 16:02:29.316479
# Unit test for function stringc
def test_stringc():
    assert stringc("Test", "blue") == u"\033[0;34mTest\033[0m"
    assert stringc("Test", "1;34") == u"\033[1;34mTest\033[0m"
    assert stringc("Test", "1;34", wrap_nonvisible_chars=True) == u"\001\033[1;34m\002Test\001\033[0m\002"



# Generated at 2022-06-13 16:02:41.022340
# Unit test for function hostcolor
def test_hostcolor():
    """
    >>> hostcolor(u'localhost', dict(failures=0, unreachable=0, changed=0))
    u'localhost                 '
    >>> hostcolor(u'localhost', dict(failures=1, unreachable=0, changed=0))
    u'\x1b[31mlocalhost\x1b[0m              '
    >>> hostcolor(u'localhost', dict(failures=0, unreachable=1, changed=0))
    u'\x1b[31mlocalhost\x1b[0m              '
    >>> hostcolor(u'localhost', dict(failures=0, unreachable=0, changed=1))
    u'\x1b[33mlocalhost\x1b[0m              '
    """
    pass  # for the compiler

# --- end of "pretty"

# Generated at 2022-06-13 16:02:49.259617
# Unit test for function hostcolor
def test_hostcolor():
    s = dict(failures=0, unreachable=0, changed=0)
    assert hostcolor('host', s) == 'host'
    s = dict(failures=1, unreachable=0, changed=0)
    assert hostcolor('host', s) == 'host'
    s = dict(failures=0, unreachable=1, changed=0)
    assert hostcolor('host', s) == 'host'
    s = dict(failures=0, unreachable=0, changed=1)
    assert hostcolor('host', s) == 'host'
    s = dict(failures=1, unreachable=1, changed=0)
    assert hostcolor('host', s) == 'host'
    s = dict(failures=0, unreachable=1, changed=1)
    assert hostcolor('host', s)

# Generated at 2022-06-13 16:02:51.708774
# Unit test for function hostcolor
def test_hostcolor():
    assert '\033[38;5;0m' not in hostcolor("localhost", {})



# Generated at 2022-06-13 16:02:57.089313
# Unit test for function stringc
def test_stringc():
    # No color
    s = stringc("test", "red", False)
    if s != "test":
        raise AssertionError("red != test")
    # With color
    s = stringc("test", "red", True)
    if s != u"\033[31mtest\033[0m":
        raise AssertionError("red != test")

#
# --- end "pretty"
if __name__ == '__main__':
    test_stringc()

# Generated at 2022-06-13 16:03:06.201434
# Unit test for function stringc
def test_stringc():
    """ Tests basic functionality """
    # Basic functionality
    assert stringc("hello", "blue") == u"\033[36mhello\033[0m"
    assert stringc("hello", "green", wrap_nonvisible_chars=True) == u"\001\033[38;5;2m\002hello\001\033[0m\002"
    assert stringc("hello\nworld", "blue") == u"\033[36mhello\033[0m\n\033[36mworld\033[0m"

# Generated at 2022-06-13 16:03:11.245012
# Unit test for function hostcolor
def test_hostcolor():

    if ANSIBLE_COLOR:
        assert hostcolor("host1", {"ok": 1, "changed": 0, "dark": 0, "failures": 0, "skipped": 0, "unreachable": 0}) == \
            u"%-37s" % stringc("host1", C.COLOR_OK)
        assert hostcolor("host2", {"ok": 0, "changed": 1, "dark": 0, "failures": 0, "skipped": 0, "unreachable": 0}) == \
            u"%-37s" % stringc("host2", C.COLOR_CHANGED)

# Generated at 2022-06-13 16:03:22.641462
# Unit test for function stringc
def test_stringc():
    """Unit test for stringc."""
    sample = u"This is a sample string"
    assert stringc(sample, "blue") == u"\033[34mThis is a sample string\033[0m"
    assert stringc(sample, "red") == u"\033[31mThis is a sample string\033[0m"
    assert stringc(sample, "default") == u"\033[39mThis is a sample string\033[0m"
    assert stringc(sample, "30") == u"\033[30mThis is a sample string\033[0m"
    assert stringc(sample, "lightgray") == u"\033[37mThis is a sample string\033[0m"

# Generated at 2022-06-13 16:03:38.848504
# Unit test for function stringc
def test_stringc():
    import unittest

    class TestStringc(unittest.TestCase):
        """Test case for function stringc()."""
        def setUp(self):
            pass

        def test_nocolor(self):
            global ANSIBLE_COLOR
            ANSIBLE_COLOR = False
            self.assertEqual(stringc('test', 'black'), 'test')

        def test_color(self):
            global ANSIBLE_COLOR
            ANSIBLE_COLOR = True
            self.assertEqual(stringc('test', 'red'), '\033[31mtest\033[0m')

        def test_parsecolor(self):
            self.assertEqual(parsecolor('red'), '31')
            self.assertEqual(parsecolor('rgb111'), '38;5;21')

# Generated at 2022-06-13 16:03:40.342046
# Unit test for function stringc
def test_stringc():
    if ANSIBLE_COLOR:
        assert stringc("text", "red") == "\033[31mtext\033[0m"
    else:
        assert stringc("text", "red") == "text"



# Generated at 2022-06-13 16:03:46.848440
# Unit test for function stringc
def test_stringc():
    if not ANSIBLE_COLOR:
        sys.stderr.write('\033[1;31mSkipping color tests, terminal does not support color.\n\033[0m')
        return

    sys.stderr.write(colorize('v', 5, 'blue') + ' ')
    sys.stderr.write(colorize('v', 0, 'blue') + ' ')
    sys.stderr.write(colorize('v', 1, 'blue') + ' ')
    sys.stderr.write(colorize('v', 4, 'blue') + '\n')

    sys.stderr.write(stringc('This is ANSIBLE_COLOR True color', 'blue') + '\n')

# Generated at 2022-06-13 16:03:54.140954
# Unit test for function hostcolor

# Generated at 2022-06-13 16:03:58.792943
# Unit test for function hostcolor
def test_hostcolor():
    s = {"changed": 0, "dark": 0, "failures": 0, "ok": 0,
         "processed": 0, "skipped": 0, "unreachable": 0}
    assert hostcolor("test.example.org", s) == "test.example.org          "

# end "pretty"



# Generated at 2022-06-13 16:04:09.014326
# Unit test for function stringc
def test_stringc():
    """Test stringc()"""
    assert stringc("foo", "red") == "\033[31mfoo\033[0m"
    assert stringc("foo", "green") == "\033[32mfoo\033[0m"
    assert stringc("foo", "blue") == "\033[34mfoo\033[0m"
    assert stringc("foo", "yellow") == "\033[33mfoo\033[0m"
    assert stringc("foo", "purple") == "\033[35mfoo\033[0m"
    assert stringc("foo", "cyan") == "\033[36mfoo\033[0m"
    assert stringc("foo", "grey") == "\033[37mfoo\033[0m"

# Generated at 2022-06-13 16:04:15.948442
# Unit test for function hostcolor
def test_hostcolor():
    for color in [True, False]:
        assert hostcolor("localhost",
                         dict(failures=0, unreachable=0, changed=0),
                         color) == u"%-26s" % "localhost"
        assert hostcolor("localhost",
                         dict(failures=1, unreachable=1, changed=1),
                         color) == u"%-26s" % "localhost"

# --- end of "pretty"



# Generated at 2022-06-13 16:04:27.115524
# Unit test for function hostcolor
def test_hostcolor():
    stats = dict(failures=0, unreachable=0, changed=0)
    def hostcolor_test(host, stats):
        return hostcolor(host, stats, True)
    assert u"%-26s" % stringc(u'localhost', C.COLOR_OK) == hostcolor_test(u'localhost', stats)
    stats = dict(failures=1, unreachable=0, changed=0)
    assert u"%-26s" % stringc(u'localhost', C.COLOR_ERROR) == hostcolor_test(u'localhost', stats)
    stats = dict(failures=0, unreachable=0, changed=1)
    assert u"%-26s" % stringc(u'localhost', C.COLOR_CHANGED) == hostcolor_test(u'localhost', stats)


# Generated at 2022-06-13 16:04:36.798569
# Unit test for function hostcolor
def test_hostcolor():
    def check_color(host, stats, expected):
        if ANSIBLE_COLOR is True:
            assert expected in hostcolor(host, stats)
        else:
            assert expected == hostcolor(host, stats)
    stats = {'changed': 0, 'failures': 0, 'ok': 1, 'skipped': 0, 'unreachable': 0}
    check_color('localhost', stats, 'localhost')
    stats = {'changed': 1, 'failures': 0, 'ok': 0, 'skipped': 0, 'unreachable': 0}
    check_color('localhost', stats, 'localhost')
    stats = {'changed': 0, 'failures': 1, 'ok': 0, 'skipped': 0, 'unreachable': 0}
    check_color('localhost', stats, 'localhost')

# Generated at 2022-06-13 16:04:41.138900
# Unit test for function stringc
def test_stringc():
    pass
    # print stringc(u"Testing...", "green")
    # print stringc(u"Testing...", "color8")
    # print stringc(u"Testing...", "rgb132")
    # print stringc(u"Testing...", "gray1")

# Test the colorizer
if __name__ == "__main__":
    test_stringc()
# --- end "pretty"

# Generated at 2022-06-13 16:04:54.361300
# Unit test for function stringc
def test_stringc():
    for i in range(256):
        print(stringc(str(i), "color%d" % i))
    for i in range(256):
        print(stringc(str(i), "rgb%d%d%d" % (i // 36, (i // 6) % 6, i % 6)))
    for i in range(24):
        print(stringc(str(i), "gray%d" % i))
    print(stringc("foo\nbaz", "red", wrap_nonvisible_chars=True))

if __name__ == '__main__':
    test_stringc()

# Generated at 2022-06-13 16:04:57.505617
# Unit test for function colorize
def test_colorize():
    color = C.COLOR_ERROR
    lead = 'FAILED'
    num = 0
    if colorize(lead, num, color) != "FAILED=0":
        print("colorize FAILED")
        sys.exit(1)


# Generated at 2022-06-13 16:05:09.601815
# Unit test for function hostcolor
def test_hostcolor():
    res = hostcolor('server1', dict(failures=0, unreachable=0, changed=0), color=True)
    assert(res == u'%-37s' % stringc('server1', C.COLOR_OK))
    res = hostcolor('server1', dict(failures=0, unreachable=0, changed=1), color=True)
    assert(res == u'%-37s' % stringc('server1', C.COLOR_CHANGED))
    res = hostcolor('server1', dict(failures=0, unreachable=1, changed=0), color=True)
    assert(res == u'%-37s' % stringc('server1', C.COLOR_ERROR))
    # if ANSIBLE_COLOR is false, no color is added

# Generated at 2022-06-13 16:05:19.568240
# Unit test for function parsecolor
def test_parsecolor():
    # All these parsecolor calls should be equivalent to each other
    assert parsecolor("red") == parsecolor("color1")
    assert parsecolor("white") == parsecolor("color0")
    assert parsecolor("color7") == parsecolor("color7")
    assert parsecolor("color15") == parsecolor("color15")
    assert parsecolor("color231") == parsecolor("color231")
    assert parsecolor("color255") == parsecolor("color255")
    assert parsecolor("rgb255255255") == parsecolor("rgb255255255")
    assert parsecolor("rgb000255255") == parsecolor("rgb000255255")
    assert parsecolor("rgb0130204") == parsecolor("rgb0130204")

# Generated at 2022-06-13 16:05:29.279283
# Unit test for function stringc
def test_stringc():
    assert stringc('foo', 'green') == '\x1b[32mfoo\x1b[0m'
    assert stringc('foo', 'red') == '\x1b[31mfoo\x1b[0m'
    assert stringc('foo', 'yellow') == '\x1b[33mfoo\x1b[0m'


#
# --- end of "pretty" library

# --- begin "cli" library
#
# cli - A library of functions to create command line user interfaces
# Copyright (C) 2004-2006 Red Hat, Inc.
# Copyright (C) 2005-2006 Brent Fox <bfox@redhat.com>
# Copyright (C) 2005-2006 Tim Waugh <twaugh@redhat.com>
#
# This program is free software; you can redistribute it and/or modify


# Generated at 2022-06-13 16:05:32.713597
# Unit test for function stringc
def test_stringc():
    if stringc('foo', 'red') == '\033[31mfoo\033[0m':
        print('%s ok' % stringc('stringc', 'green'))



# Generated at 2022-06-13 16:05:36.923638
# Unit test for function stringc
def test_stringc():
    # Test that the color codes can be used in a regex
    regex = re.compile(u"\033\[.*?m")

    # Test that strin

# Generated at 2022-06-13 16:05:41.153973
# Unit test for function stringc
def test_stringc():
    assert stringc("test", "red") == u"\033[31mtest\033[0m"
    assert stringc("test", "color16") == u"\033[38;5;16mtest\033[0m"
    assert stringc("test", "rgb255000") == u"\033[38;5;196mtest\033[0m"



# Generated at 2022-06-13 16:05:50.100499
# Unit test for function hostcolor
def test_hostcolor():
    from ansible.utils.color import hostcolor
    from copy import deepcopy
    stats = {'changed': 0, 'unreachable': 0,'failures': 0}
    tc = hostcolor('fakehost', deepcopy(stats), True)
    assert tc == u'%-37s' % stringc('fakehost', C.COLOR_OK)

    stats['changed'] = 1
    tc = hostcolor('fakehost', deepcopy(stats), True)
    assert tc == u'%-37s' % stringc('fakehost', C.COLOR_CHANGED)

    stats['failures'] = 1
    stats['unreachable'] = 1
    tc = hostcolor('fakehost', deepcopy(stats), True)
    assert tc == u'%-37s' % stringc('fakehost', C.COLOR_ERROR)

    # test without color


# Generated at 2022-06-13 16:05:58.287147
# Unit test for function colorize
def test_colorize():
    from ansible.utils.color import colorize
    assert colorize('foo', 4, 'black') == stringc('foo=4   ', 'black')
    assert colorize('foo', 40, 'blue') == stringc('foo=40  ', 'blue')
    assert colorize('foo', 400, 'cyan') == stringc('foo=400 ', 'cyan')
    assert colorize('foo', 4000, 'green') == stringc('foo=4000', 'green')
    assert colorize('foo', 40000, 'magenta') == stringc('foo=40000', 'magenta')
    assert colorize('foo', 400000, 'red') == stringc('foo=400000', 'red')
    assert colorize('foo', 4000000, 'white') == stringc('foo=4000000', 'white')

# Generated at 2022-06-13 16:06:17.706028
# Unit test for function stringc
def test_stringc():
    if not ANSIBLE_COLOR:
        return

    class Object(object):
        def __unicode__(self):
            return u'foo'

    assert stringc(u'test', u'white', wrap_nonvisible_chars=True) == u"\001\033[38;5;15m\002test\001\033[0m\002"
    assert stringc(u'test', u'white') == u"\033[38;5;15mtest\033[0m"
    assert stringc(u'test', u'white') == stringc(u'test', u'white')
    assert stringc(u'test', u'white') == u"\033[38;5;15mtest\033[0m"

# Generated at 2022-06-13 16:06:27.156781
# Unit test for function hostcolor

# Generated at 2022-06-13 16:06:37.184443
# Unit test for function hostcolor
def test_hostcolor():
    assert u"%-26s" == hostcolor(u'host.example.com', {u'failures': 0, u'unreachable': 0, u'changed': 0})
    assert stringc(u'host.example.com', C.COLOR_ERROR) == hostcolor(u'host.example.com', {u'failures': 1, u'unreachable': 0, u'changed': 0})
    assert stringc(u'host.example.com', C.COLOR_CHANGED) == hostcolor(u'host.example.com', {u'failures': 0, u'unreachable': 0, u'changed': 1})

# Generated at 2022-06-13 16:06:45.538080
# Unit test for function hostcolor
def test_hostcolor():
    test_stats = dict(
        ok=10,
        failures=0,
        unreachable=0,
        changed=0
    )
    test_host = 'example.org'
    # This should generate "example.org" in green in the first column
    print(hostcolor(test_host, test_stats))
    # This should generate "example.org" without colors, since color=False
    print(hostcolor(test_host, test_stats, color=False))
    # This should generate "example.org" in red in the first column
    test_stats['failures'] = 1
    test_stats['unreachable'] = 1
    print(hostcolor(test_host, test_stats))
    # This should generate "example.org" in yellow in the first column
    test_stats['failures'] = 0
   

# Generated at 2022-06-13 16:06:55.471187
# Unit test for function hostcolor
def test_hostcolor():
    colors = {
        'red': [dict(failures=1, unreachable=0, changed=0),
                dict(failures=0, unreachable=1, changed=0)],
        'yellow': [dict(failures=0, unreachable=0, changed=1)],
        'green': [dict(failures=0, unreachable=0, changed=0)],
    }
    for color, statslist in colors.items():
        for stats in statslist:
            hc = hostcolor('hostname', stats, color=True)
            assert hc.startswith(u"%s%-37s" % (chr(27), chr(27)))
            assert hc.endswith(chr(27))
            assert hc.count(C.COLOR_CODES[color]) == 1

# Generated at 2022-06-13 16:07:03.626071
# Unit test for function stringc
def test_stringc():
    good_str = "text"

# Generated at 2022-06-13 16:07:08.579759
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('test', dict(failures=0, unreachable=0, changed=0)) == u"%-26s" % u"test"
    assert hostcolor('test', dict(failures=0, unreachable=0, changed=1)) == u"%-26s" % u"test"
    assert hostcolor('test', dict(failures=1, unreachable=0, changed=0)) == u"%-26s" % u"test"
    assert hostcolor('test', dict(failures=0, unreachable=1, changed=0)) == u"%-26s" % u"test"
    assert hostcolor('test', dict(failures=0, unreachable=0, changed=0), color=False) == u"%-26s" % u"test"



# Generated at 2022-06-13 16:07:13.426267
# Unit test for function stringc
def test_stringc():
    tests = [
        ('<%= color.error("failed") %>', 'failed', 'error', True),
    ]
    for t in tests:
        tmp_result = stringc(t[1], t[2], t[3])
        if tmp_result != t[0]:
            raise AssertionError(
                u"%s != %s" % (tmp_result, t[0])
            )



# Generated at 2022-06-13 16:07:21.213239
# Unit test for function stringc
def test_stringc():
    print(stringc('Hello, World!', 'red'),
          stringc('Colors, yay!', 'rgb255255255'),
          stringc('I love you!', 'green'),
          stringc('And you!', 'gray9'))

# --- end of "pretty" from https://github.com/thedude/pretty.py ---

# This was taken from the Python 2.7.3 source code, so it is under the PSF
# license as well.  It has been modified slightly to fit in with the rest
# of the code here.

# Generated at 2022-06-13 16:07:28.766913
# Unit test for function hostcolor
def test_hostcolor():
    from ansible.utils.color import hostcolor
    h = hostcolor('hostname', 'stats')
    assert h == 'hostname                      ', 'hostcolor_test: Basic test failed'

# --- end "pretty"
#
# Some of the color-related functions were originally in pretty.py,
# modified to support being used in this library.
#
# The following code is based on the following library:
#
# https://github.com/tartley/colorama/blob/master/colorama/ansi.py
#
# Copyright Jonathan Hartley 2013. BSD 3-Clause license, see LICENSE file.



# Generated at 2022-06-13 16:07:56.444453
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
    assert parsecolor('default') == u'39'

    assert parsecolor('darkgray') == u'38;5;232'
    assert parsecolor('lightgray') == u'38;5;255'
    assert parsecolor('darkred') == u'38;5;1'

# Generated at 2022-06-13 16:08:06.446177
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('myhost', dict(ok=1, changed=0, unreachable=0, failures=0)) == u'%-26s' % 'myhost'
    if ANSIBLE_COLOR:
        assert hostcolor('myhost', dict(ok=1, changed=0, unreachable=0, failures=1)) == u"%-37s" % stringc('myhost', C.COLOR_ERROR)
        assert hostcolor('myhost', dict(ok=1, changed=1, unreachable=0, failures=0)) == u"%-37s" % stringc('myhost', C.COLOR_CHANGED)
        assert hostcolor('myhost', dict(ok=1, changed=0, unreachable=0, failures=0)) == u"%-37s" % stringc('myhost', C.COLOR_OK)

# --- end

# Generated at 2022-06-13 16:08:16.558542
# Unit test for function stringc
def test_stringc():
    try:
        import curses
        curses.setupterm()
        if curses.tigetnum('colors') < 0:
            print("no color terminal")
            ANSIBLE_COLOR = False
    except ImportError:
        print("no color terminal")
        ANSIBLE_COLOR = False
    except curses.error:
        print("no color terminal")
        ANSIBLE_COLOR = False


# Generated at 2022-06-13 16:08:24.606179
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor("test.example.org", dict(
        failures=0, unreachable=0, changed=0), True) == u"test.example.org          "
    assert hostcolor("test.example.org", dict(
        failures=1, unreachable=0, changed=0), True) == u"test.example.org          "
    assert hostcolor("test.example.org", dict(
        failures=0, unreachable=1, changed=0), True) == u"test.example.org          "
    assert hostcolor("test.example.org", dict(
        failures=0, unreachable=0, changed=1), True) == u"test.example.org          "



# Generated at 2022-06-13 16:08:33.476361
# Unit test for function hostcolor
def test_hostcolor():

    host1 = "testhost"
    stats1 = {'changed': 4, 'failures': 0, 'ok': 10, 'skipped': 0, 'unreachable': 0}

    assert hostcolor(host1, stats1, True) == u"\033[0;32m%-37s\033[0m", "testhost: pass"

    host2 = "testhost"
    stats2 = {'changed': 2, 'failures': 0, 'ok': 10, 'skipped': 0, 'unreachable': 2}
    assert hostcolor(host2, stats2, True) == u"\033[0;31m%-37s\033[0m", "testhost: fail"

    host3 = "testhost"

# Generated at 2022-06-13 16:08:42.988442
# Unit test for function hostcolor
def test_hostcolor():
    stats = dict(failures=0, unreachable=0, changed=0)
    assert hostcolor("darkblue.example.com", stats) == u"%-37s" % u'darkblue.example.com'
    assert hostcolor("darkblue.example.com", dict(failures=1), color=False) == u"%-26s" % u'darkblue.example.com'
    assert hostcolor("darkblue.example.com", stats, color=False) == u"%-26s" % u'darkblue.example.com'

# --- end "pretty"

# --- begin "generic utils"



# Generated at 2022-06-13 16:08:50.859361
# Unit test for function colorize
def test_colorize():
    curses.setupterm()
    assert curses.tigetnum("colors") >= 8
    # These values are so we can simulate nocolor, light background, and dark background
    nocolor = (0, 0, 0)
    light_back = (15, 15, 15)
    dark_back = (0, 0, 0)

# Generated at 2022-06-13 16:08:54.002476
# Unit test for function stringc
def test_stringc():
    assert stringc("Some text", "black") == "\033[30mSome text\033[0m"


# --- end

# --- begin "formatters"


# Generated at 2022-06-13 16:09:03.289575
# Unit test for function stringc
def test_stringc():
    print(u"\nBasic test of function stringc")
    strings = [u'This is the message in color', u'This is the colored message on the second line']
    fores = [u'black', u'red', u'green', u'yellow', u'blue', u'magenta', u'cyan', u'white', u'rgb333', u'gray8']
    styles = [u'normal', u'bold', u'faint', u'italic', u'underline', u'blink', u'inverse', u'normal']
    backs = [u'black', u'red', u'green', u'yellow', u'blue', u'magenta', u'cyan', u'white', u'rgb333']

# Generated at 2022-06-13 16:09:14.088896
# Unit test for function hostcolor
def test_hostcolor():
    def _test_hostcolor(host, stats, color=True, expected=None):
        assert expected == hostcolor(host, stats, color=color)

    stats1 = {'unreachable': 0, 'skipped': 0, 'changed': 1, 'failures': 0, 'ok': 1}
    _test_hostcolor('server1', stats1, color=True,
                    expected=u'\033[0;32mserver1               \033[0m')
    _test_hostcolor('server1', stats1, color=False, expected=u'server1               ')

    stats2 = {'unreachable': 1, 'skipped': 0, 'changed': 1, 'failures': 0, 'ok': 1}