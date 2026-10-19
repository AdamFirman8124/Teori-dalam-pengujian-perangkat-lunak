

# Generated at 2022-06-14 11:08:39.440928
# Unit test for function get_key
def test_get_key():
    assert const.KEY_MAPPING[get_key()] == const.KEY_MAPPING['\n']
    assert const.KEY_MAPPING[get_key()] == const.KEY_MAPPING['\n']

    # arrow up
    assert get_key() == const.KEY_UP

    # arrow left
    assert get_key() == const.KEY_LEFT

    # arrow right
    assert get_key() == const.KEY_RIGHT

    # letter h
    assert get_key() == 'h'

    # enter
    assert get_key() == const.KEY_ENTER

    # shift+f
    assert get_key() == 'F'

    # ctrl+d
    assert get_key() == const.KEY_EXIT

    # delete
    assert get_key() == const.KEY_

# Generated at 2022-06-14 11:08:52.096281
# Unit test for function get_key
def test_get_key():
    print("Start to test function get_key")
    for i in range(5):
        key = out.get_key()
        if key == 'KEY_UP':
            print("Your input is " + key)
        elif key == 'KEY_DOWN':
            print("Your input is " + key)
        elif key == ' ':
            print("Your input is " + key)
        elif key == 'KEY_RIGHT':
            print("Your input is " + key)
        elif key == 'KEY_LEFT':
            print("Your input is " + key)
        elif key == '\x03':
            print("Your input is " + key)
        elif key == '\x04':
            print("Your input is " + key)

# Generated at 2022-06-14 11:08:53.775975
# Unit test for function getch
def test_getch():
    import tempfile

    with tempfile.TemporaryFile() as f:
        f.write('q'.encode("ascii"))
        f.seek(0)
        sys.stdin = f
        assert getch() == 'q'

# Generated at 2022-06-14 11:08:59.384951
# Unit test for function get_key
def test_get_key():
    test_str = "\x1b[A"
    key = get_key()
    assert key == const.KEY_UP
    test_str = "q"
    key = get_key()
    assert key == const.KEY_QUIT
    test_str = "Q"
    key = get_key()
    assert key == "Q"

# Generated at 2022-06-14 11:09:05.270977
# Unit test for function get_key
def test_get_key():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)

# Generated at 2022-06-14 11:09:09.896313
# Unit test for function getch
def test_getch():
    for _ in range(10):
        ch = getch()
        if ch == '\x1b':
            ch = getch()
            if ch == '[':
                ch = getch()

# Generated at 2022-06-14 11:09:11.021359
# Unit test for function get_key
def test_get_key():
    print(get_key())

# Generated at 2022-06-14 11:09:14.507528
# Unit test for function get_key
def test_get_key():
    # TODO: It is better to test this function by mock.
    print('Press any key to test get_key')
    press = get_key()
    print(press)

# Generated at 2022-06-14 11:09:15.565369
# Unit test for function get_key
def test_get_key():
    assert get_key() == 'q'

# Generated at 2022-06-14 11:09:26.207031
# Unit test for function get_key
def test_get_key():
    import sys
    import io

# Generated at 2022-06-14 11:09:34.303009
# Unit test for function getch
def test_getch():
    input_ch = 'a'
    output_ch = getch()
    assert input_ch == output_ch

# Generated at 2022-06-14 11:09:35.214562
# Unit test for function open_command
def test_open_command():
    assert isinstance(open_command(''), str)



# Generated at 2022-06-14 11:09:37.965293
# Unit test for function get_key
def test_get_key():
    print('Please type ' + const.KEY_UP + ' or ' + const.KEY_DOWN)
    key = get_key()
    print('key: ' + key)


# Generated at 2022-06-14 11:09:40.513876
# Unit test for function open_command
def test_open_command():
    assert open_command('test') == 'xdg-open test' or open_command('test') == 'open test'

# Generated at 2022-06-14 11:09:42.351964
# Unit test for function getch
def test_getch():
    assert getch() == chr(27)
    assert getch() == chr(91)
    assert getch() == chr(65)

# Generated at 2022-06-14 11:09:44.329355
# Unit test for function get_key
def test_get_key():
    assert get_key() == 'j'

# Generated at 2022-06-14 11:09:47.621162
# Unit test for function open_command
def test_open_command():
    assert open_command('/hello/world') == 'xdg-open /hello/world' or 'open /hello/world'



# Generated at 2022-06-14 11:09:53.073356
# Unit test for function get_key

# Generated at 2022-06-14 11:09:55.498511
# Unit test for function getch
def test_getch():
    assert getch() == 'a'


# Generated at 2022-06-14 11:09:57.803451
# Unit test for function open_command
def test_open_command():
    assert open_command("") == os.environ["BROWSER"] + " "



# Generated at 2022-06-14 11:10:03.407779
# Unit test for function get_key
def test_get_key():
    pass


if __name__ == '__main__':
    test_get_key()

# Generated at 2022-06-14 11:10:04.734526
# Unit test for function getch
def test_getch():
    assert getch()

test_getch()

# Generated at 2022-06-14 11:10:07.074501
# Unit test for function open_command
def test_open_command():
    assert open_command('www.google.com') == 'xdg-open www.google.com'



# Generated at 2022-06-14 11:10:13.854713
# Unit test for function get_key
def test_get_key():

    assert get_key() == '\x1b'  # Get ESC key
    assert get_key() == '\x1b'  # Get ESC key again
    assert get_key() == '\x1b'  # Get ESC key again
    assert get_key() == 'a'     # Get a
    assert get_key() == '\x1b'
    assert get_key() == '['
    assert get_key() == 'B'

test_get_key()

# Generated at 2022-06-14 11:10:22.994731
# Unit test for function get_key
def test_get_key():
    if sys.version_info > (2, 6):
        import unittest
        import io

        class TestMethods(unittest.TestCase):
            def test_get_key(self):
                self.assertEqual(get_key(), None)
                sys.stdin = io.BytesIO(b'\xc3\xbc')
                self.assertEqual(get_key(), '\xc3\xbc')
                self.assertTrue(sys.stdin.closed)
        unittest.main()

# Generated at 2022-06-14 11:10:31.181874
# Unit test for function get_key
def test_get_key():
    # Testing for key arrow up
    ch = getch()
    assert get_key() == '\x1b'

    next_ch = getch()
    assert get_key() == '['

    last_ch = getch()
    assert get_key() == 'A'

    # Testing for key left
    ch = getch()
    assert get_key() == '\x1b'

    next_ch = getch()
    assert get_key() == '['

    last_ch = getch()
    assert get_key() == 'D'

    # Testing for key right
    ch = getch()
    assert get_key() == '\x1b'

    next_ch = getch()
    assert get_key() == '['

    last_ch = getch()

# Generated at 2022-06-14 11:10:33.162153
# Unit test for function open_command
def test_open_command():
    assert open_command('~') == os.path.expanduser('~')



# Generated at 2022-06-14 11:10:44.702057
# Unit test for function getch
def test_getch():
    # TODO: refactor test
    import sys
    import tty
    import termios

    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        # input = sys.stdin.read(1)
        input = getch()
        print("got key: " + input)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)

# Generated at 2022-06-14 11:10:49.573600
# Unit test for function open_command
def test_open_command():
    assert open_command('test_string') == 'xdg-open test_string'

# Generated at 2022-06-14 11:10:58.752291
# Unit test for function get_key
def test_get_key():
    # Test get_key by pushing all key mapping one by one
    for key in const.KEY_MAPPING.values():
        print("Press key: " + str(key))
        assert key == get_key()

    # Test get_key for KEY_DOWN
    print("Press key: " + str(const.KEY_DOWN))
    assert get_key() == const.KEY_DOWN

    # Test get_key for KEY_UP
    print("Press key: " + str(const.KEY_UP))
    assert get_key() == const.KEY_UP

# Generated at 2022-06-14 11:11:12.096164
# Unit test for function open_command
def test_open_command():
    if find_executable('xdg-open'):
        assert open_command('abc.txt') == 'xdg-open abc.txt'
    else:
        assert open_command('abc.txt') == 'open abc.txt'



# Generated at 2022-06-14 11:11:13.633607
# Unit test for function open_command
def test_open_command():
    assert open_command('http://example.com') == 'open http://example.com'

# Generated at 2022-06-14 11:11:16.857209
# Unit test for function getch
def test_getch():
    import unittest

    class GetchTest(unittest.TestCase):
        def test_enter(self):
            self.assertEqual(getch(), '\n')

    unittest.main()

# Generated at 2022-06-14 11:11:18.147374
# Unit test for function open_command
def test_open_command():
    assert open_command('www.baidu.com') == 'xdg-open www.baidu.com'

# Generated at 2022-06-14 11:11:20.443948
# Unit test for function open_command
def test_open_command():
    assert open_command('test') == 'xdg-open test'

# Generated at 2022-06-14 11:11:21.718474
# Unit test for function get_key
def test_get_key():
    assert get_key() == 'q'


# Generated at 2022-06-14 11:11:24.342902
# Unit test for function open_command
def test_open_command():
    assert open_command('http://google.com') in ('xdg-open http://google.com', 'open http://google.com')

# Generated at 2022-06-14 11:11:33.490159
# Unit test for function getch

# Generated at 2022-06-14 11:11:36.413892
# Unit test for function getch
def test_getch():

    print('Press UP key')
    if getch() == const.KEY_UP:
        print('OK')
    else:
        print('Failed')

# Generated at 2022-06-14 11:11:37.526985
# Unit test for function getch
def test_getch():
    assert getch() != None

# Generated at 2022-06-14 11:11:50.297729
# Unit test for function get_key
def test_get_key():
    for key, i in const.KEY_MAPPING.items():
        print(get_key())
        assert get_key() == i

# Generated at 2022-06-14 11:11:57.219149
# Unit test for function get_key

# Generated at 2022-06-14 11:12:02.559272
# Unit test for function open_command
def test_open_command():
    if os.name == 'posix':
        assert open_command('file') == 'xdg-open file'
    elif os.name == 'nt':
        assert open_command('file') == 'open file'
    else:
        pass


# Generated at 2022-06-14 11:12:11.786965
# Unit test for function get_key
def test_get_key():
    init_output()
    Key_presses = ['A', 'a', '\x1b', '[', 'A', 'B', '[', 'B', '\x1b', '[']
    Key_press = []
    for key in Key_presses:
        if key == '\x1b':
            Key_press.append('\x1b')
        if key == '[':
            Key_press.append('[')
    print(Key_press)
    Key_press = ''.join(Key_press)
    assert Key_press == '\x1b[', "Key_press return value don't match"
    print(Key_press)

    Key_presses = ['A', 'a', '\x1b', '[', 'A', 'B', '[', 'B']
    Key_press = []
   

# Generated at 2022-06-14 11:12:17.370685
# Unit test for function open_command
def test_open_command():
    assert open_command('http://www.google.com') == 'open http://www.google.com'
    assert open_command('http://www.google.com') == 'xdg-open http://www.google.com'

# Generated at 2022-06-14 11:12:18.562666
# Unit test for function get_key
def test_get_key():
    assert get_key() == ''


# Generated at 2022-06-14 11:12:28.682109
# Unit test for function get_key
def test_get_key():
    import os
    cmd = "cd " + os.path.dirname(os.path.realpath(__file__))
    os.system(cmd)
    os.system("echo 'This are test for function get_key'")
    os.system("echo 'Press a'")
    os.system("echo 'Expect: a'")
    os.system("python3 python/test_input.py")
    os.system("echo 'Press b'")
    os.system("echo 'Expect: b'")
    os.system("python3 python/test_input.py")
    os.system("echo 'Press c'")
    os.system("echo 'Expect: c'")
    os.system("python3 python/test_input.py")
    os.system("echo 'Press Enter'")

# Generated at 2022-06-14 11:12:33.763923
# Unit test for function get_key
def test_get_key():
    assert get_key() == '\x1b'
    assert get_key() == '\x1b'
    assert get_key() == '['
    assert get_key() == 'A'

# Generated at 2022-06-14 11:12:38.248874
# Unit test for function get_key
def test_get_key():
    # Test for tuple
    assert get_key() == ''

    # Test for single char
    assert get_key() == ''

    # Test for ESC
    assert get_key() == ''

    # Test for Arrow key



# Generated at 2022-06-14 11:12:43.990694
# Unit test for function get_key
def test_get_key():
    print(const.KEY_DOWN)
    print(get_key())
    print(get_key())
    print(get_key())
    print(get_key())
    print(get_key())
    print(get_key())
    print(get_key())
    print(get_key())
    print(get_key())
    print(get_key())

# Generated at 2022-06-14 11:13:06.599521
# Unit test for function get_key
def test_get_key():
    pass


if __name__ == '__main__':
    test_get_key()

# Generated at 2022-06-14 11:13:13.262936
# Unit test for function get_key
def test_get_key():
    # Test for almost all key
    keys_in = const.SPECIAL_KEYS_AND_MAPPING
    keys_out = []
    for key_in in keys_in:
        print(key_in[1])
        key_out = get_key()
        keys_out.append(key_out)
    print(keys_out)


if __name__ == '__main__':
    test_get_key()

# Generated at 2022-06-14 11:13:14.376115
# Unit test for function get_key
def test_get_key():
    assert get_key() == 'h'

# Generated at 2022-06-14 11:13:23.294526
# Unit test for function getch
def test_getch():
    import sys
    import tty
    import termios
    import time

    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
        print("The pressed key is: ", ch)
        # time.sleep(3)
        return ch
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)


# Generated at 2022-06-14 11:13:27.756481
# Unit test for function get_key
def test_get_key():
    assert get_key() == const.KEY_DOWN
    assert get_key() == const.KEY_UP
    assert get_key() == 'k'

if __name__ == '__main__':
    # test_get_key()
    print(Path('~'))
    print(Path('~').expanduser())

# Generated at 2022-06-14 11:13:28.642584
# Unit test for function get_key
def test_get_key():
    pass

# Generated at 2022-06-14 11:13:31.040256
# Unit test for function open_command
def test_open_command():
    assert open_command('test') in ['xdg-open test', 'open test']
    assert open_command('/home/test') in [
        'xdg-open /home/test', 'open /home/test']

# Generated at 2022-06-14 11:13:43.218912
# Unit test for function get_key
def test_get_key():
    # Clear buffer
    while sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        line = sys.stdin.readline().strip()
        
    # Test arrow key mapping
    print("Press arrow key up")
    assert const.KEY_UP == get_key()
    print("Press arrow key down")
    assert const.KEY_DOWN == get_key()

    # Test escape sequence
    print("Press a")
    assert 'a' == get_key()
    print("Press b")
    assert 'b' == get_key()
    print("Press c")
    assert 'c' == get_key()

    # Test 'Enter' key
    print("Press enter")
    assert const.ENTER_KEY == get_key()
    


# Generated at 2022-06-14 11:13:44.426885
# Unit test for function get_key
def test_get_key():
    assert get_key() in [const.KEY_UP, const.KEY_DOWN]

# Generated at 2022-06-14 11:13:49.769478
# Unit test for function get_key
def test_get_key():
    print ("Testing one")
    val = get_key()
    if val != const.KEY_UP:
        raise Exception("Wrong key pressed. Pressed " + val + " instead of key up")
    print ("Testing two")
    val = get_key()
    if val != const.KEY_DOWN:
        raise Exception("Wrong key pressed. Pressed " + val + " instead of key down")
    print ("Testing three")
    val = get_key()
    if val != const.KEY_EXIT:
        raise Exception("Wrong key pressed. Pressed " + val + " instead of key exit")
    print ("Testing four")
    val = get_key()
    if val != const.KEY_PLAY:
        raise Exception("Wrong key pressed. Pressed " + val + " instead of key play")
    print ("Testing five")

# Generated at 2022-06-14 11:14:14.755596
# Unit test for function open_command
def test_open_command():
    assert open_command('https://www.google.com') == 'xdg-open https://www.google.com'
    assert open_command('https://www.google.com') == 'xdg-open https://www.google.com'

# Generated at 2022-06-14 11:14:16.283953
# Unit test for function getch
def test_getch():
    assert b'q' == getch()

# Generated at 2022-06-14 11:14:23.444647
# Unit test for function getch
def test_getch():
    from .. import controller
    from .. import logger

    logger.init()
    controller._init()

    print('Please press Enter to pass unit test for function getch')
    print('Please press Esc key to exit unit test')
    while True:
        key = get_key()
        if key == const.KEY_ENTER:
            print('Test passed')
        elif key == '\x1b':
            print('Test exited')
            break
        else:
            print('Wrong key pressed: {}'.format(key))

# Generated at 2022-06-14 11:14:27.902953
# Unit test for function get_key
def test_get_key():
    s = ''
    for i in range(0, 127):
        s = s + chr(i)
    sys.stdin = io.StringIO(s)
    for i in range(0, 127):
        key = get_key()
        if i in const.KEY_MAPPING:
            if const.KEY_MAPPING[chr(i)] != key:
                print("error: " + chr(i) + ": " + const.KEY_MAPPING[chr(i)] + " expected, " + key + " found")
        else:
            if chr(i) != key:
                print("error: " + chr(i) + " expected, " + key + " found")

if __name__ == "__main__":  # pragma: no cover
    test_get_key()

# Generated at 2022-06-14 11:14:30.854409
# Unit test for function open_command
def test_open_command():
    assert open_command('google.com') == 'google-chrome google.com'
    assert open_command('google.com') == 'google-chrome google.com'



# Generated at 2022-06-14 11:14:33.524080
# Unit test for function get_key
def test_get_key():
    assert get_key() == 'a'
    assert get_key() == 'b'
    assert get_key() == 'c'

# Generated at 2022-06-14 11:14:34.075444
# Unit test for function get_key
def test_get_key():
    pass

# Generated at 2022-06-14 11:14:45.391295
# Unit test for function get_key
def test_get_key():
    from . import testutils

    def k(key):
        return get_key()

    testutils.assert_equal(k(const.KEY_CTRL_C), '\x03')
    testutils.assert_equal(k(const.KEY_CTRL_D), '\x04')
    testutils.assert_equal(k(const.KEY_CTRL_M), '\r')
    testutils.assert_equal(k(const.KEY_ESCAPE), '\x1b')
    testutils.assert_equal(k(const.KEY_BACKSPACE), '\x7f')
    testutils.assert_equal(k(const.KEY_TAB), '\t')
    testutils.assert_equal(k(const.KEY_ENTER), '\r')

# Generated at 2022-06-14 11:14:47.864671
# Unit test for function get_key
def test_get_key():
    import pytest
    os.environ['TERM'] = 'xterm'
    assert get_key() == const.KEY_UP
    assert get_key() == const.KEY_DOWN

# Generated at 2022-06-14 11:14:48.533386
# Unit test for function open_command
def test_open_command():
    pass

# Generated at 2022-06-14 11:15:31.586910
# Unit test for function get_key
def test_get_key():
    result = 1
    print('input q to exit')
    while True:
        key = get_key()
        if key == 'q':
            sys.exit(0)
        else:
            print(key)
            result += 1



# Generated at 2022-06-14 11:15:37.289746
# Unit test for function get_key
def test_get_key():
    assert get_key() == 'a'
    os.system('echo -ne "\\x1b[D" > /dev/tty')
    assert get_key() == '\x1b'
    assert get_key() == '['
    assert get_key() == 'D'
    os.system('echo -ne "\\x1bOA" > /dev/tty')
    assert get_key() == '\x1b'
    assert get_key() == 'O'
    assert get_key() == 'A'

# Generated at 2022-06-14 11:15:38.823172
# Unit test for function getch
def test_getch():
    assert getch() == 's'
    assert getch() == 'd'

# Generated at 2022-06-14 11:15:50.545459
# Unit test for function get_key
def test_get_key():
    # UP
    sys.stdin.write('\x1b')
    sys.stdin.write('[')
    sys.stdin.write('A')
    sys.stdin.seek(0)
    if get_key() != 'UP':
        raise AssertionError

    # DOWN
    sys.stdin.seek(0)
    sys.stdin.write('\x1b')
    sys.stdin.write('[')
    sys.stdin.write('B')
    sys.stdin.seek(0)
    if get_key() != 'DOWN':
        raise AssertionError

    # SPACE
    sys.stdin.seek(0)
    sys.stdin.write(' ')
    sys.stdin.seek(0)

# Generated at 2022-06-14 11:15:58.820204
# Unit test for function get_key
def test_get_key():
    if unittest:
        stdscr = curses.initscr()

    try:
        # Test arrow keys
        assert get_key() == const.KEY_DOWN
        assert get_key() == const.KEY_UP
        # Test character input
        assert get_key() == 'a'
        assert get_key() == 'b'
        assert get_key() == 'c'
        # Test escape key
        assert get_key() == const.KEY_ESCAPE
    finally:
        if unittest:
            curses.endwin()

# Generated at 2022-06-14 11:16:02.782040
# Unit test for function open_command
def test_open_command():
    assert open_command("https://www.google.com") in ['open https://www.google.com', 'xdg-open https://www.google.com']
    assert type(open_command("https://www.google.com")) == str



# Generated at 2022-06-14 11:16:03.833896
# Unit test for function getch
def test_getch():
    assert getch() == '\x03'

# Generated at 2022-06-14 11:16:04.536523
# Unit test for function getch
def test_getch():
    pass

# Generated at 2022-06-14 11:16:06.607962
# Unit test for function open_command
def test_open_command():
    assert open_command('https://www.google.com/') == 'xdg-open https://www.google.com/'


# Generated at 2022-06-14 11:16:10.632185
# Unit test for function get_key
def test_get_key():
    for k_ch in const.KEY_MAPPING.keys():
        assert get_key() == const.KEY_MAPPING[k_ch]
    assert get_key() == 'A'

if __name__ == '__main__':
    test_get_key()

# Generated at 2022-06-14 11:17:04.066040
# Unit test for function getch
def test_getch():
    termios._tcsetattr = os.tcsetattr
    sys.stdin.fileno = lambda: 3
    fd = sys.stdin.fileno()

    def tcsetattr(fd, arg, arg2):
        assert arg2 == termios.TCSAFLUSH
        return termios.tcsetattr(fd, arg2, arg)

    termios.tcsetattr = lambda fd, arg, arg2=None: tcsetattr(
        fd, arg, arg2)

    def getch():
        return getch()

    os.environ['TERM'] = 'linux'

    sys.stdin.read = lambda: "\x1b[A\x1b[B"

    assert getch() == const.KEY_UP
    assert getch() == const.KEY_DOWN

    sys.stdout.write

# Generated at 2022-06-14 11:17:06.031949
# Unit test for function get_key
def test_get_key():
    assert get_key() is 'a', 'get_key() should read single char from stdin'

# Generated at 2022-06-14 11:17:12.843821
# Unit test for function get_key
def test_get_key():
    assert get_key() == 'q'
    assert get_key() == 'x'
    assert get_key() == 'u'
    assert get_key() == 'd'
    assert get_key() == 'c'
    assert get_key() == 'l'
    assert get_key() == 'k'
    assert get_key() == 'j'
    assert get_key() == 'h'


# Generated at 2022-06-14 11:17:26.003154
# Unit test for function getch
def test_getch():
    init_output()

    print('This is a unit test for function getch')
    print('Please press the following keys on your keyboard:')
    print('[a] for get the letter "a"')
    print('[A] for get the letter "A"')
    print('[esc] for get the key const.KEY_ESC')
    print('[up arrow] for get the key const.KEY_UP')
    print('[down arrow] for get the key const.KEY_DOWN')
    input('Press Enter to start:')

    print('Please press the letter "a":')
    assert getch() == 'a'

    print('Please press the letter "A":')
    assert getch() == 'A'

    print('Please press the key [esc]:')
    assert getch() == const.KEY_ESC

    print

# Generated at 2022-06-14 11:17:27.626968
# Unit test for function open_command
def test_open_command():
    assert 'xdg-open' in open_command('test')
    assert 'open' in open_command('test')

# Generated at 2022-06-14 11:17:40.144815
# Unit test for function getch
def test_getch():
    colorama.init()
    s = "What is your favorite color?\n" + \
        "a) Red\n" + \
        "b) Blue\n" + \
        "c) Green\n"
    sys.stdout.write(s)
    sys.stdout.flush()

    k = None
    validResponse = False
    while not validResponse:
        k = getch()
        sys.stdout.write(colorama.Fore.CYAN + k + colorama.Style.RESET_ALL + '\n')

        if k == 'a':
            sys.stdout.write("You chose Red.\n")
            validResponse = True
        elif k == 'b':
            sys.stdout.write("You chose Blue.\n")
            validResponse = True

# Generated at 2022-06-14 11:17:48.340429
# Unit test for function get_key
def test_get_key():
    global init_output
    def mock_init(autoreset=True, convert=True, strip=False, wrap=False):
        pass

    init_output = mock_init

    global getch
    getch_res = ""
    def mock_getch():
        return getch_res

    getch = mock_getch

    getch_res = 'a'
    assert get_key() == 'a'
    getch_res = '\t'
    assert get_key() == '\t'
    getch_res = '\n'
    assert get_key() == '\n'
    getch_res = '\x1b'
    assert get_key() == '\x1b'

    getch_res = '\x1b'

# Generated at 2022-06-14 11:17:51.559057
# Unit test for function getch
def test_getch():
    a = getch()
    assert a == a


if __name__ == '__main__':
    print('Test for function getch:')
    test_getch()

# Generated at 2022-06-14 11:17:56.911140
# Unit test for function get_key
def test_get_key():
    print('Testing function get_key')
    print('Please input the following keys:')
    print('j')
    print('k')
    print('Enter')
    print('<C-c> to exit')

    while True:
        print(get_key())


if __name__ == '__main__':
    test_get_key()

# Generated at 2022-06-14 11:18:03.928856
# Unit test for function get_key
def test_get_key():
    # Test for every combination for two key press
    for first in ['\x1b', 'a', 'b']:
        for second in ['[', 'a', 'b']:
            for third in ['A', 'B', 'C']:
                key = first + second + third
                sys.stdin = open('/dev/tty')
                sys.stdin.write(key)
                sys.stdin.flush()
                assert get_key() == const.KEY_MAPPING[first + second + third]
        key = first
        sys.stdin = open('/dev/tty')
        sys.stdin.write(key)
        sys.stdin.flush()
        assert get_key() == const.KEY_MAPPING[first]

