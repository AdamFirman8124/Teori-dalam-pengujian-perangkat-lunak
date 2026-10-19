

# Generated at 2022-06-13 15:59:41.126723
# Unit test for function hostcolor
def test_hostcolor():
    host = "test_host"
    stats = { 'failures': 0,
              'unreachable': 0,
              'changed': 0 }
    assert hostcolor(host, stats) == "test_host"
    stats = { 'failures': 1,
              'unreachable': 0,
              'changed': 0 }
    assert hostcolor(host, stats) == u"test_host"
    stats = { 'failures': 0,
              'unreachable': 1,
              'changed': 0 }
    assert hostcolor(host, stats) == u"test_host"
    stats = { 'failures': 0,
              'unreachable': 0,
              'changed': 1 }
    assert hostcolor(host, stats) == u"test_host"


# Generated at 2022-06-13 15:59:44.294845
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor("localhost",{'ok':0,'changed':0,'unreachable':0,'skipped':0,'failed':0}) == 'localhost                    '



# Generated at 2022-06-13 15:59:54.001734
# Unit test for function parsecolor
def test_parsecolor():
    assert(parsecolor(u'green') == u'32')
    assert(parsecolor(u'red') == u'31')
    assert(parsecolor(u'blue') == u'34')
    assert(parsecolor(u'0') == u'38;5;0')
    assert(parsecolor(u'1') == u'38;5;1')
    assert(parsecolor(u'2') == u'38;5;2')
    assert(parsecolor(u'3') == u'38;5;3')
    assert(parsecolor(u'4') == u'38;5;4')
    assert(parsecolor(u'5') == u'38;5;5')
    assert(parsecolor(u'6') == u'38;5;6')
   

# Generated at 2022-06-13 16:00:02.903736
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('test_host', dict(failures=0, unreachable=0, changed=0)) == u'%-37s' % stringc('test_host', C.COLOR_OK)
    assert hostcolor('test_host', dict(failures=1, unreachable=0, changed=0)) == u'%-37s' % stringc('test_host', C.COLOR_ERROR)
    assert hostcolor('test_host', dict(failures=0, unreachable=1, changed=0)) == u'%-37s' % stringc('test_host', C.COLOR_ERROR)
    assert hostcolor('test_host', dict(failures=0, unreachable=0, changed=1)) == u'%-37s' % stringc('test_host', C.COLOR_CHANGED)

# --- end of "pretty"

# Generated at 2022-06-13 16:00:09.392919
# Unit test for function parsecolor
def test_parsecolor():
    pcolor = parsecolor
    assert pcolor('black') == '30'
    assert pcolor('red') == '31'
    assert pcolor('green') == '32'
    assert pcolor('yellow') == '33'
    assert pcolor('blue') == '34'
    assert pcolor('magenta') == '35'
    assert pcolor('cyan') == '36'
    assert pcolor('white') == '37'
    assert pcolor('default') == '39'
    assert pcolor('bold') == '1'
    assert pcolor('italic') == '3'
    assert pcolor('underline') == '4'
    assert pcolor('strikethrough') == '9'
    assert pcolor('darkgray') == '90'
    assert pcolor('darkred') == '91'

# Generated at 2022-06-13 16:00:14.601839
# Unit test for function stringc
def test_stringc():
    print('stringc', end=' ')
    assert stringc('hi there', 'blue', True) == '\001\033[34m\002hi there\001\033[0m\002'
    assert stringc('hi there', 'blue') == '\033[34mhi there\033[0m'
    print('ok')

if __name__ == "__main__":
    test_stringc()

# Generated at 2022-06-13 16:00:18.770964
# Unit test for function parsecolor
def test_parsecolor():
    assert parsecolor('33') == u'38;5;33'
    assert parsecolor('33m') == u'38;5;33'
    assert parsecolor('rgb255') == u'38;5;231'
    assert parsecolor('rgb222') == u'38;5;59'
    assert parsecolor('rgb123') == u'38;5;18'
    assert parsecolor('rgb221') == u'38;5;58'
    assert parsecolor('rgb212') == u'38;5;52'
    assert parsecolor('rgb211') == u'38;5;51'
    assert parsecolor('rgb121') == u'38;5;17'
    assert parsecolor('rgb111') == u'38;5;15'

# Generated at 2022-06-13 16:00:29.823203
# Unit test for function stringc
def test_stringc():
    """Test function stringc by generating a chessboard."""
    for fg in u'black red green yellow blue cyan white'.split():
        for bg in u'black', u'gray', u'red', u'green', u'yellow', u'blue', u'cyan', u'white':
            print(u"%-7s %-7s %s" % (fg, bg, stringc(u'\u2588\u2588', fg, bg)))
        print()


if __name__ == '__main__':
    test_stringc()
    print(stringc(u'foo', u'blue'))
# --- end "pretty"

# --- begin terminal table

# Copyright (c) 2013 by Patrick Rainsberry. All rights reserved.
#
# Permission is hereby granted, free of charge, to

# Generated at 2022-06-13 16:00:40.971384
# Unit test for function stringc
def test_stringc():
    tests = ((u'test', u'green', u'\033[32mtest\033[0m'),
             (u'test', u'blue', u'\033[34mtest\033[0m'),
             (u'test', u'color2', u'\033[38;5;2mtest\033[0m'),
             (u'test', u'rgb124', u'\033[38;5;78mtest\033[0m'),
             (u'test', u'gray1', u'\033[38;5;234mtest\033[0m'),
             (u'\ntest', u'green', u'\n\033[32mtest\033[0m'))
    for test in tests:
        res = stringc(test[0], test[1])

# Generated at 2022-06-13 16:00:46.356409
# Unit test for function stringc
def test_stringc():
    assert stringc('foo', 'blue') == '\033[34mfoo\033[0m'
    assert stringc('foo', 'black', True) == '\001\033[30m\002foo\001\033[0m\002'
    assert stringc('foo', 'color8', True) == '\001\033[38;5;8m\002foo\001\033[0m\002'
    assert stringc('foo', 'rgb255000', True) == '\001\033[38;5;9m\002foo\001\033[0m\002'



# Generated at 2022-06-13 16:01:04.761287
# Unit test for function hostcolor
def test_hostcolor():
    stats = {'failures': 0,
             'ok': 0,
             'changed': 1,
             'unreachable': 0}

    assert hostcolor('testhost', stats, False) == '%-26s' % 'testhost'
    assert hostcolor('testhost', stats, True) == u"%-37s" % stringc('testhost', C.COLOR_CHANGED)

    stats = {'failures': 1,
             'ok': 0,
             'changed': 1,
             'unreachable': 0}

    assert hostcolor('testhost', stats, False) == '%-26s' % 'testhost'
    assert hostcolor('testhost', stats, True) == u"%-37s" % stringc('testhost', C.COLOR_ERROR)


# Generated at 2022-06-13 16:01:15.776190
# Unit test for function stringc
def test_stringc():
    """ Use this function to generate stringc test results. """
    print(u"%s" % stringc(u"Hello World", 'blue'))
    print(u"%s" % stringc(u"Hello World", 'bright blue'))
    print(u"%s" % stringc(u"Hello World", 'green'))
    print(u"%s" % stringc(u"Hello World", 'bright green'))
    print(u"%s" % stringc(u"Hello World", 'white'))
    print(u"%s" % stringc(u"Hello World", 'black'))
    print(u"%s" % stringc(u"Hello World", 'red'))
    print(u"%s" % stringc(u"Hello World", 'bright red'))

# Generated at 2022-06-13 16:01:22.146100
# Unit test for function stringc
def test_stringc():
    ''' test function stringc '''
    print()
    print(stringc('Hello World!', 'BLUE'))
    print(stringc('Hello World!', 'RED', wrap_nonvisible_chars=True))
    print(stringc('Hello World!', 'rgb123', wrap_nonvisible_chars=True))
    print(stringc('Hello World!', 'rgb222', wrap_nonvisible_chars=True))
    print(stringc('Hello World!', 'rgb332', wrap_nonvisible_chars=True))
    print(stringc('Hello World!', 'gray99', wrap_nonvisible_chars=True))
    print(stringc('Hello World!', 'gray0', wrap_nonvisible_chars=True))

# Generated at 2022-06-13 16:01:26.834807
# Unit test for function parsecolor
def test_parsecolor():
    for key in C.COLOR_CODES.keys():
        # print(parsecolor(key))
        assert parsecolor(key) == C.COLOR_CODES[key]
    # print(parsecolor('color16'))
    assert parsecolor('color16') == u'38;5;16'
    # print(parsecolor('gray0'))
    assert parsecolor('gray0') == u'38;5;232'
    # print(parsecolor('rgb255255255'))
    assert parsecolor('rgb255255255') == u'38;5;231'
    # print(parsecolor('rgb000'))
    assert parsecolor('rgb000') == u'38;5;16'

# --- end of pretty ---



# Generated at 2022-06-13 16:01:34.911967
# Unit test for function colorize
def test_colorize():
    """Unit test for function colorize"""
    import sys
    if not sys.stdout.isatty():
        sys.stdout.write('Test skipped because stdout is not a TTY\n')
        sys.exit(0)

    def assert_equal(want, got):
        if want != got:
            print('test_colorize: %s != %s' % (repr(want), repr(got)))
            sys.exit(1)

    assert_equal(u'\u001b[38;5;9mfoo=0   \u001b[0m', colorize('foo',0,'red'))
    assert_equal(u'\u001b[38;5;9mfoo=1   \u001b[0m', colorize('foo',1,'red'))

# Generated at 2022-06-13 16:01:41.566719
# Unit test for function hostcolor
def test_hostcolor():
    """ 
    >>> test_hostcolor()
    OK
    """
    # TODO: Create a test that actually asserts what it's supposed to

    stats = {
        'ok': 1,
        'failures': 0,
        'unreachable': 0,
        'skipped': 0,
        'changed': 0
    }

    host = 'testhost'
    print(hostcolor(host, stats))



# Generated at 2022-06-13 16:01:50.210807
# Unit test for function stringc
def test_stringc():
    assert stringc('hello', 'red', False) == u'\033[31mhello\033[0m'
    assert stringc('hello', 'RED', False) == u'\033[31mhello\033[0m'
    assert stringc('hello', 'blue', False) == u'\033[34mhello\033[0m'
    assert stringc('hello', '1', False) == u'\033[31mhello\033[0m'
    assert stringc('hello', '12', False) == u'\033[34mhello\033[0m'
    assert stringc('hello', '123', False) == u'\033[31mhello\033[0m'

# Generated at 2022-06-13 16:02:00.283715
# Unit test for function hostcolor
def test_hostcolor():
    h = 'myhost'
    s = dict(ok=0, changed=0, unreachable=0, failed=0)
    print("Color off")
    print(hostcolor(h, s, color=False))
    print("Color on, no failures")
    print(hostcolor(h, s, color=True))
    print("Color on, unreachable")
    s = dict(ok=0, changed=0, unreachable=1, failed=0)
    print(hostcolor(h, s, color=True))
    print("Color on, failed")
    s = dict(ok=0, changed=0, unreachable=0, failed=1)
    print(hostcolor(h, s, color=True))
    print("Color on, changed")

# Generated at 2022-06-13 16:02:01.804470
# Unit test for function stringc
def test_stringc():
    assert stringc("text", "green") == "\033[32mtext\033[0m"
    assert stringc("text", "blue") == "\033[94mtext\033[0m"



# Generated at 2022-06-13 16:02:07.629960
# Unit test for function hostcolor
def test_hostcolor():
    fake_result = {'dark': {'failures': 1, 'unreachable': 0, 'ok': 0, 'changed': 0,
                            'skipped': 0, 'dark': {}, 'processed': {}}}
    assert hostcolor('dark', fake_result['dark']) == u"%-37s" % stringc('dark', C.COLOR_ERROR)
    fake_result = {'failure': {'failures': 0, 'unreachable': 1, 'ok': 0, 'changed': 0,
                               'skipped': 0, 'dark': {}, 'processed': {}}}
    assert hostcolor('failure', fake_result['failure']) == u"%-37s" % stringc('failure', C.COLOR_ERROR)

# Generated at 2022-06-13 16:02:25.595000
# Unit test for function hostcolor
def test_hostcolor():
    class MyHost():
        def __init__(self, name, failed):
            self.name = name
            self.failed = failed

    h = []

    class MyStats(dict):
         def __getitem__(self, idx):
            return self.get(idx, 0)

    for i in range(4):
        h.append(MyHost('host', i % 2))

    t = MyStats({"failures": 1, "unreachable": 0, "changed": 0})
    assert(hostcolor(h[0].name, t) == u"host                         ")
    t = MyStats({"failures": 0, "unreachable": 1, "changed": 0})
    assert(hostcolor(h[1].name, t) == u"host                         ")

# Generated at 2022-06-13 16:02:29.532681
# Unit test for function stringc
def test_stringc():
    """Unit test for function stringc."""
    if not ANSIBLE_COLOR:
        print("Terminal does not support color. Test skipped")
        return

    for key in C.COLOR_CODES:
        print("%s: %s" % (key, stringc("Hello", key)))
    print("color8: %s" % stringc("Hello", "color8"))
    print("rgb555: %s" % stringc("Hello", "rgb555"))



# Generated at 2022-06-13 16:02:41.391833
# Unit test for function hostcolor
def test_hostcolor():
    stats = dict(
        ok=15,
        skipped=0,
        failed=0,
        unreachable=0,
        changed=10,
        dark=dict(ok=0, skipped=0, failed=0, unreachable=0, changed=0),
        failures=0,
        processed=15
    )
    assert hostcolor("dark.example.com", stats, color=False) == "dark.example.com             "
    assert hostcolor("dark.example.com", stats, color=True) == "dark.example.com             "

# Generated at 2022-06-13 16:02:46.776875
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor(u"test.example.com", {u"failures": 1}, True) == u"\x1b[31;01mtest.example.com\x1b[0m      "
    assert hostcolor(u"test.example.com", {u"changed": 1}, True) == u"\x1b[33;01mtest.example.com\x1b[0m      "
    assert hostcolor(u"test.example.com", {u"ok": 1}, True) == u"\x1b[32;01mtest.example.com\x1b[0m      "
    assert hostcolor(u"test.example.com", {u"failures": 1}, False) == u"test.example.com       "

# Generated at 2022-06-13 16:02:56.166030
# Unit test for function stringc
def test_stringc():
    # print "Testing stringc"
    test_string = u"The quick brown fox jumped over the lazy dog"
    color_tests = (u"black", u"red", u"green", u"yellow", u"blue",
          u"magenta", u"cyan", u"white", u"gray8", u"rgb255255255",
          u"rgb0255255", u"rgb000255")
    for color in color_tests:
        # print "  testing %s" % color
        result = stringc(test_string, color)
        assert isinstance(result, basestring)
        assert len(result) == len(test_string) + len(color) + 6
        assert result.startswith(u"\033[")
        assert result.endswith(u"\033[0m")



# Generated at 2022-06-13 16:03:03.590742
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor('example.org', dict(failures=0, unreachable=0, changed=0, ok=1), True) == u'%-26s' % 'example.org'
    assert hostcolor('example.org', dict(failures=0, unreachable=0, changed=1, ok=0), True) == u"%-37s" % stringc('example.org', C.COLOR_CHANGED)
    assert hostcolor('example.org', dict(failures=0, unreachable=1, changed=0, ok=0), True) == u"%-37s" % stringc('example.org', C.COLOR_ERROR)

# Generated at 2022-06-13 16:03:14.238960
# Unit test for function colorize
def test_colorize():
    """ test colorize """
    assert colorize('foo', 0, 'blue') == "foo=0   "
    assert colorize('foo', 0, None) == "foo=0   "
    assert colorize('foo', 1, 'blue') == "foo=1   "
    assert colorize('foo', 10, 'blue') == "foo=10  "
    assert colorize('foo', 100, 'blue') == "foo=100 "
    assert colorize('foo', 1000, 'blue') == "foo=1000"
    assert colorize('foo', 10000, 'blue') == "foo=10000"

    # test with colors disabled
    global ANSIBLE_COLOR
    ANSIBLE_COLOR = False
    assert colorize('foo', 0, 'blue') == "foo=0   "

# Generated at 2022-06-13 16:03:20.660935
# Unit test for function stringc
def test_stringc():
    assert u'\033[1;37myes\033[0m' == stringc('yes', 'white', False)
    assert u'\001\033[1;37m\002yes\001\033[0m\002' == stringc('yes', 'white', True)


if __name__ == "__main__":
    test_stringc()
# --- end "pretty"


# completion used to result in ANSI escape errors

# Generated at 2022-06-13 16:03:28.553510
# Unit test for function stringc
def test_stringc():
    if ANSIBLE_COLOR:
        assert '\033[31mred\033[0m' == stringc('red', 'red')
        assert '\033[31mred\033[0m' == stringc('red', 'Color1')
        assert '\033[31mred\033[0m' == stringc('red', 'Color9')
        assert '\033[32mgreen\033[0m' == stringc('green', 'green')
        assert '\033[32mgreen\033[0m' == stringc('green', 'Color2')
        assert '\033[34mblue\033[0m' == stringc('blue', 'blue')
        assert '\033[34mblue\033[0m' == stringc('blue', 'Color4')

# Generated at 2022-06-13 16:03:33.341403
# Unit test for function hostcolor
def test_hostcolor():
    # Create test data structure
    stats = {'changed': 0, 'failures': 0, 'ok': 0, 'skipped': 0, 'unreachable': 0}
    host = "example.com"
    color = None
    result = hostcolor(host, stats, color)
    # Make sure the output string contains only (3x26) characters
    assert result.find('\n') == -1
    assert len(result) == 26

    # Add red color to text
    stats['unreachable'] = 1
    result = hostcolor(host, stats, color)
    assert result.find('\033') != -1
    assert result.find('\n') == -1


# Generated at 2022-06-13 16:03:46.473193
# Unit test for function stringc
def test_stringc():
    if not ANSIBLE_COLOR:
        # Ignore the test if the terminal does not support color.
        return
    # Test 1: ANSIBLE_COLOR is True and the output is expected.
    color = 'blue'
    text = 'This is a test'
    expected_string = u"\n".join([u"\033[34m%s\033[0m" % t for t in text.split(u'\n')])
    assert stringc(text, color) == expected_string
    # Test 2: ANSIBLE_COLOR is False, and the output is expected.
    ANSIBLE_COLOR = False
    expected_string = "This is a test"
    assert stringc(text, color) == expected_string
# --- end "pretty".

# Generated at 2022-06-13 16:03:53.996282
# Unit test for function stringc
def test_stringc():
    def col(color):
        return stringc('color test', color)

    assert col('default') == u'\033[39mcolor test\033[0m'
    assert col('black') == u'\033[30mcolor test\033[0m'
    assert col('red') == u'\033[31mcolor test\033[0m'
    assert col('green') == u'\033[32mcolor test\033[0m'
    assert col('yellow') == u'\033[33mcolor test\033[0m'
    assert col('blue') == u'\033[34mcolor test\033[0m'
    assert col('magenta') == u'\033[35mcolor test\033[0m'

# Generated at 2022-06-13 16:04:05.542658
# Unit test for function hostcolor
def test_hostcolor():
    from ansible.inventory.host import Host

    host = "testhost"
    stats = {'failures': 0, 'unreachable': 0, 'changed': 1}
    assert hostcolor(host, stats) == u"%-37s" % stringc(host, C.COLOR_CHANGED)

    host = "testhost"
    stats = {'failures': 1, 'unreachable': 0, 'changed': 1}
    assert hostcolor(host, stats) == u"%-37s" % stringc(host, C.COLOR_ERROR)

    host = "testhost"
    stats = {'failures': 0, 'unreachable': 1, 'changed': 0}
    assert hostcolor(host, stats) == u"%-37s" % stringc(host, C.COLOR_ERROR)


# Generated at 2022-06-13 16:04:17.492867
# Unit test for function hostcolor
def test_hostcolor():
    hostcolor = tools.hostcolor
    hosts = ['hostname']

    # No error, changed, ok
    stats = {'failures': 0, 'changed': 0, 'ok': 1, 'dark': 0, 'skipped': 0, 'unreachable': 0}
    assert hostcolor(hosts[0], stats, False) == '%-26s' % hosts[0]
    assert hostcolor(hosts[0], stats, True) == stringc("%-26s" % hosts[0], C.COLOR_OK)

    # Error
    stats = {'failures': 1, 'changed': 0, 'ok': 0, 'dark': 0, 'skipped': 0, 'unreachable': 0}
    assert hostcolor(hosts[0], stats, False) == '%-26s' % hosts[0]

# Generated at 2022-06-13 16:04:28.104983
# Unit test for function stringc
def test_stringc():
    assert stringc(u"test", u"red") == u"\033[31mtest\033[0m"
    assert stringc(u"test", u"color1") == u"\033[38;5;1mtest\033[0m"
    assert stringc(u"test", u"color99") == u"\033[38;5;99mtest\033[0m"
    assert stringc(u"test", u"color112") == u"\033[38;5;112mtest\033[0m"
    assert stringc(u"test", u"color255") == u"\033[38;5;255mtest\033[0m"
    assert stringc(u"test", u"color256") == u"\033[38;5;256mtest\033[0m"


# Generated at 2022-06-13 16:04:37.493692
# Unit test for function stringc
def test_stringc():
    if ANSIBLE_COLOR:
        print(u"Testing stringc")
        print(stringc(u"This is the color blue for you.", u"blue"))
        print(stringc(u"This is the color red for you.", u"red"))
        print(stringc(u"This is the color green for you.", u"green"))
        print(stringc(u"This is the color yellow for you.", u"yellow"))
        print(stringc(u"This is the color cyan for you.", u"cyan"))
        print(stringc(u"This is the color magenta for you.", u"magenta"))
        print(stringc(u"This is the color white for you.", u"white"))
        print(stringc(u"This is the color white on blue for you.", u"white",
                      u"blue"))
       

# Generated at 2022-06-13 16:04:42.866724
# Unit test for function stringc
def test_stringc():
    print(stringc("foo", "blue"))
    print(stringc("foo", "bold"))
    print(stringc("foo", "underline"))
    print(stringc("foo", "green"))
    print(stringc("foo", "red"))
    print(stringc("foo", "purple"))
    print(stringc("foo", "black"))
    print(stringc("foo", "yellow"))
    print(stringc("foo", "white"))
    print(stringc("foo", "cyan"))
# --- end "pretty"

# Generated at 2022-06-13 16:04:54.441383
# Unit test for function hostcolor
def test_hostcolor():
    host = 'testhost'
    stats = {'ok':1, 'changed':1, 'failures':1, 'skipped':1, 'unreachable':1}
    assert hostcolor(host, stats, color=False) == u"testhost                "
    assert hostcolor(host, stats) == u"\x1b[0;31mtesthost\x1b[0m               "
    stats = {'ok':1, 'changed':1, 'failures':0, 'skipped':1, 'unreachable':0}
    assert hostcolor(host, stats) == u"\x1b[0;33mtesthost\x1b[0m               "
    stats = {'ok':1, 'changed':0, 'failures':0, 'skipped':0, 'unreachable':0}

# Generated at 2022-06-13 16:05:02.158534
# Unit test for function hostcolor
def test_hostcolor():
    assert hostcolor(host="localhost", stats={"failures": 1, "unreachable": 0, "changed": 0}, color=False) == u"localhost               "
    assert hostcolor(host="localhost", stats={"failures": 1, "unreachable": 0, "changed": 0}, color=True) == u"\033[31;01mlocalhost\033[0m               "
    assert hostcolor(host="localhost", stats={"failures": 0, "unreachable": 1, "changed": 0}, color=True) == u"\033[31;01mlocalhost\033[0m               "
    assert hostcolor(host="localhost", stats={"failures": 0, "unreachable": 0, "changed": 1}, color=True) == u"\033[33;01mlocalhost\033[0m               "
    assert host

# Generated at 2022-06-13 16:05:12.267347
# Unit test for function stringc
def test_stringc():
    """Basic test of stringc."""
    assert stringc('foo', 'red') == '\x1b[31mfoo\x1b[0m'
    assert stringc('foo', 'blue') == '\x1b[34mfoo\x1b[0m'
    assert stringc('foo', 'bright red') == '\x1b[91mfoo\x1b[0m'
    assert stringc('foo', 'bright blue') == '\x1b[94mfoo\x1b[0m'
    assert stringc('foo', 'bright white') == '\x1b[97mfoo\x1b[0m'
    assert stringc('foo', 'bright purple') == '\x1b[95mfoo\x1b[0m'
    assert stringc('foo', 'bright green')

# Generated at 2022-06-13 16:05:38.402174
# Unit test for function stringc
def test_stringc():
    from ansible.utils.color import stringc
    assert stringc('test', 'blue') == u'\033[34mtest\033[0m'
    assert stringc('test', 'black') == u'\033[30mtest\033[0m'
    assert stringc('test', 'red') == u'\033[31mtest\033[0m'
    assert stringc('test', 'green') == u'\033[32mtest\033[0m'
    assert stringc('test', 'yellow') == u'\033[33mtest\033[0m'
    assert stringc('test', 'blue') == u'\033[34mtest\033[0m'
    assert stringc('test', 'magenta') == u'\033[35mtest\033[0m'
    assert stringc

# Generated at 2022-06-13 16:05:45.834379
# Unit test for function hostcolor

# Generated at 2022-06-13 16:05:54.774303
# Unit test for function stringc
def test_stringc():
    """ Test the function stringc """
    # Pylint false positives for the assertTrue and assertFalse calls
    # pylint: disable=no-member
    assert stringc('black', 'black') == '\033[30mblack\033[0m'
    assert stringc('red', 'red') == '\033[31mred\033[0m'
    assert stringc('green', 'green') == '\033[32mgreen\033[0m'
    assert stringc('yellow', 'yellow') == '\033[33myellow\033[0m'
    assert stringc('blue', 'blue') == '\033[34mblue\033[0m'
    assert stringc('magenta', 'magenta') == '\033[35mmagenta\033[0m'

# Generated at 2022-06-13 16:06:04.453189
# Unit test for function stringc
def test_stringc():
    assert stringc(u"hello", 'red', True) == u"\001\033[31m\002hello\001\033[0m\002"
    assert stringc(u"hello", 'red') == u"\033[31mhello\033[0m"

    assert stringc(u"hello\nworld", 'red', True) == u"\001\033[31m\002hello\001\033[0m\002\n\001\033[31m\002world\001\033[0m\002"
    assert stringc(u"hello\nworld", 'red') == u"\033[31mhello\033[0m\n\033[31mworld\033[0m"


# Generated at 2022-06-13 16:06:15.648612
# Unit test for function hostcolor
def test_hostcolor():
    # Special function for unittests because we don't want to import
    # test.runner() from __main__ to avoid excess dependencies
    from ansible.playbook.play_context import PlayContext

    # Test colors
    stats = dict(
        ok=1, changed=1, unreachable=2, failures=3,
        skipped=4, rescues=5, ignored=6
    )

    # Test colors
    class MockRunner(object):
        def __init__(self, host):
            self.host = host
            self.stats = stats

    class MockTask(object):
        def __init__(self, runner, color):
            self.hosts = {
                'host1': MockRunner('host1'),
                'host2': MockRunner('host2'),
            }
            self.runner = runner

# Generated at 2022-06-13 16:06:21.492732
# Unit test for function colorize
def test_colorize():
    assert colorize("foo", 1, 'red') == stringc("foo=1   ", 'red')
    assert colorize("foo", 0, 'red') == "foo=0   "
    global ANSIBLE_COLOR
    ANSIBLE_COLOR = False
    assert colorize("foo", 1, 'red') == "foo=1   "
    ANSIBLE_COLOR = True


# Generated at 2022-06-13 16:06:24.936969
# Unit test for function hostcolor
def test_hostcolor():
    host = "test.example.com"
    assert hostcolor(host, dict(failed=0, unreachable=0, ok=1, changed=0)) == u"test.example.com             "



# Generated at 2022-06-13 16:06:35.880151
# Unit test for function hostcolor
def test_hostcolor():
    # This function is called when running "./hacking/test-module" to run
    # the unit test.
    from ansible.utils.color import hostcolor
    if hostcolor('host1', {'failures': 0, 'unreachable': 0, 'changed': 0}) != u"host1                     ":
        return False
    if hostcolor('host2', {'failures': 0, 'unreachable': 1, 'changed': 0}) != u"\x1b[31mhost2            \x1b[0m":
        return False
    if hostcolor('host3', {'failures': 0, 'unreachable': 0, 'changed': 1}) != u"\x1b[33mhost3            \x1b[0m":
        return False
    return True

# --- end of "pretty"




# Generated at 2022-06-13 16:06:44.757524
# Unit test for function hostcolor
def test_hostcolor():
    testhost = dict(hostvars=dict(ansible_host="testhost"))
    testhost2 = dict(hostvars=dict(ansible_host="testhost2"))

    # Print "ok" if the color names are not replaced with ANSI color
    # codes or if the ANSI color codes are not interpreted correctly
    # (whatever that means)
    assert hostcolor('testhost', dict(failures=0, unreachable=0, changed=0)) \
        == u'%-26s' % ('testhost')
    assert hostcolor('testhost', dict(failures=1, unreachable=0, changed=0)) \
        == u'%-26s' % ('testhost')
    assert hostcolor('testhost', dict(failures=0, unreachable=1, changed=0)) \
        == u'%-26s'

# Generated at 2022-06-13 16:06:55.537276
# Unit test for function stringc
def test_stringc():
    from ansible.utils.color import stringc
    from ansible.utils.color import ANSIBLE_COLOR
    from ansible.utils.color import parsecolor
    original_ANSIBLE_COLOR = ANSIBLE_COLOR

# Generated at 2022-06-13 16:07:36.801845
# Unit test for function colorize
def test_colorize():
    from ansible.constants import COLOR_ERROR, COLOR_OK, COLOR_CHANGED

    assert colorize('foo', 0, COLOR_ERROR) == u'foo=0   '
    assert colorize('foo', 0, COLOR_OK) == u'foo=0   '
    assert colorize('foo', 0, COLOR_CHANGED) == u'foo=0   '

    ansible_color_old = ANSIBLE_COLOR
    ANSIBLE_COLOR = True

    assert colorize('foo', 1, COLOR_ERROR) == u'\033[31mfoo=1   \x1b[0m'
    assert colorize('foo', 2, COLOR_OK) == u'\033[0;32mfoo=2   \x1b[0m'

# Generated at 2022-06-13 16:07:41.135773
# Unit test for function stringc
def test_stringc():
    assert stringc('foo', 'green') == u'\033[32mfoo\033[0m'
    assert stringc('foo', 'color4') == u'\033[38;5;4mfoo\033[0m'
    assert stringc('foo', 'rgb541') == u'\033[38;5;34mfoo\033[0m'

# Generated at 2022-06-13 16:07:53.096905
# Unit test for function colorize
def test_colorize():
    assert colorize(u"test", 4, None) == u"test=4   "
    assert colorize(u"test", 4, C.COLOR_ERROR) == u"test=4   "
    assert colorize(u"test", 0, C.COLOR_OK) == u"test=0   "
    assert colorize(u"test", 0, C.COLOR_CHANGED) == u"test=0   "
    assert colorize(u"test", 0, C.COLOR_ERROR) == u"test=0   "
    assert colorize(u"test", 1, C.COLOR_OK) == u"test=1   "
    assert colorize(u"test", 2, C.COLOR_CHANGED) == u"test=2   "

# Generated at 2022-06-13 16:08:04.747956
# Unit test for function hostcolor
def test_hostcolor():
    host = 'testhost'
    stats = {'failures': 0, 'unreachable': 0, 'changed': 0}

    assert hostcolor(host, stats) == '%-26s' % host

    stats = {'failures': 1, 'unreachable': 0, 'changed': 0}
    assert hostcolor(host, stats) == stringc(host, C.COLOR_ERROR)

    stats = {'failures': 0, 'unreachable': 1, 'changed': 0}
    assert hostcolor(host, stats) == stringc(host, C.COLOR_ERROR)

    stats = {'failures': 0, 'unreachable': 0, 'changed': 1}
    assert hostcolor(host, stats) == stringc(host, C.COLOR_CHANGED)

    global ANSIBLE_COLOR
    ANSIBLE_

# Generated at 2022-06-13 16:08:14.821144
# Unit test for function hostcolor
def test_hostcolor():
    test_colors = [
        (dict(changed=0, unreachable=0, failures=0), C.COLOR_OK),
        (dict(changed=1, unreachable=0, failures=0), C.COLOR_CHANGED),
        (dict(changed=0, unreachable=1, failures=1), C.COLOR_ERROR),
    ]


# Generated at 2022-06-13 16:08:23.283199
# Unit test for function stringc
def test_stringc():
    # Test a color
    result = stringc(u"Test", u"red")
    assert(result == "\033[31mTest\033[0m")
    # Test an rgb color
    result = stringc(u"Test", u"rgb054")
    assert(result == "\033[38;5;214mTest\033[0m")
    # Test a gray
    result = stringc(u"Test", u"gray5")
    assert(result == "\033[38;5;240mTest\033[0m")
    # Test color None
    result = stringc(u"Test", None)
    assert(result == "Test")


if __name__ == "__main__":
    test_stringc()

# Generated at 2022-06-13 16:08:32.180041
# Unit test for function stringc
def test_stringc():
    ''' "None" color should reset to default '''
    assert(stringc("None", "None") == "None")
    assert(stringc("None", "None", True) == "\001\033[0m\002None\001\033[0m\002")
    ''' Colors '''
    assert(stringc("test", "Red") == "\033[91mtest\033[0m")
    assert(stringc("test", "Red", True) == "\001\033[91m\002test\001\033[0m\002")
    assert(stringc("test", "BRED") == "\033[1;91mtest\033[0m")
    assert(stringc("test", "BRED", True) == "\001\033[1;91m\002test\001\033[0m\002")
   

# Generated at 2022-06-13 16:08:38.154593
# Unit test for function hostcolor
def test_hostcolor():
    stats = {
        'changed': 0,
        'dark': 0,
        'failures': 0,
        'ok': 0,
        'processed': 0,
        'rescued': 0,
        'skipped': 0,
        'unreachable': 0
    }
    color = True

    # Test if hostcolor works
    assert hostcolor('localhost', stats, color) == u"%-37s" % ('localhost')

    # Test if host color changes
    stats['failures'] = 1
    assert hostcolor('localhost', stats, color) == u"%-37s" % (stringc('localhost', C.COLOR_ERROR))
    stats['failures'] = 0
    stats['changed'] = 1

# Generated at 2022-06-13 16:08:40.698137
# Unit test for function stringc
def test_stringc():
    assert stringc(u"foo", u"green") == u"\033[32mfoo\033[0m"



# Generated at 2022-06-13 16:08:48.708250
# Unit test for function hostcolor
def test_hostcolor():
    class foo:
        def __init__(self):
            self.ok = 0
            self.changed = 0
            self.dark = 0
            self.failed = 0
            self.processed = 0
            self.skipped = 0
    # Basic (no color)
    assert hostcolor('foo.bar', foo()) == '%-26s' % 'foo.bar'
    # Default colors
    # (failures=0, unreachable=0)
    assert hostcolor('foo.bar', foo()) == '%-26s' % 'foo.bar'
    # (failures=0, unreachable=2)
    foo.dark = 2
    assert hostcolor('foo.bar', foo()) == '%-26s' % 'foo.bar'
    # (failures=2, unreachable=0)
    foo.dark = 0


# Generated at 2022-06-13 16:09:30.790508
# Unit test for function colorize
def test_colorize():
    # ANSIBLE_COLOR should be True for the following tests
    ANSIBLE_COLOR = True
    assert colorize(u" ", 0, color=None) == u"=0   "
    assert colorize(u" ", 1, color=C.COLOR_CHANGED) == u"=1   "
    assert colorize(u" ", 42, color=C.COLOR_OK) == u"=42  "
    assert colorize(u" ", 100, color=C.COLOR_ERROR) == u"=100 "
    # Set ANSIBLE_COLOR to False and make sure the function
    # colorize returns the exact same output
    ANSIBLE_COLOR = False
    assert colorize(u" ", 0, color=None) == u"=0   "