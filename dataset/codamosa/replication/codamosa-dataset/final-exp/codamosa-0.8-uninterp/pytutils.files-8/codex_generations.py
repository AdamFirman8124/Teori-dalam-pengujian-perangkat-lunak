

# Generated at 2022-06-14 05:59:40.755416
# Unit test for function islurp
def test_islurp():
    filename = "../data/SMSSpamCollection.txt"
    text_data = islurp(filename)
    for line in text_data:
        print (line)


# Generated at 2022-06-14 05:59:51.236133
# Unit test for function islurp
def test_islurp():
    # Slurp in lines
    lines = slurp('test_files/test.txt')
    assert('a\n' in lines)
    assert('c\n' in lines)

    # Slurp in lines with autogenerator
    slurp_lines = (l for l in slurp('test_files/test.txt'))
    assert('a\n' in slurp_lines)
    assert('c\n' in slurp_lines)

    # Slurp in lines from STDIN
    stdin_lines = slurp('-')
    assert('aa\n' in stdin_lines)
    assert('cc\n' in stdin_lines)

# Generated at 2022-06-14 06:00:02.913556
# Unit test for function islurp
def test_islurp():
    import io
    import islurp
    import json

    class TestPair(object):  # but named tuple would be simpler
        def __init__(self, description, filename, mode, iter_by, allow_stdin, expanduser, expandvars, expected):
            self.description = description
            self.filename = filename
            self.mode = mode
            self.iter_by = iter_by
            self.allow_stdin = allow_stdin
            self.expanduser = expanduser
            self.expandvars = expandvars
            self.expected = expected

    def to_test_pair(test):
        # for convenience, replace filename with expected if filename is '-' and allow_stdin is False
        if not (test['filename'] == '-' and not test['allow_stdin']):
            test['expected']

# Generated at 2022-06-14 06:00:12.147599
# Unit test for function islurp
def test_islurp():
  # Unit test for function islurp
  slurp_contents = []
  expected_contents = ['Hello\n', 'My name is\n', 'Arun\n']
  temp_file = '/tmp/temp_file.txt'
  with open(temp_file, 'w') as f:
    for i in range(3):
      f.write(expected_contents[i])
  
  for contents in slurp(temp_file, 'LINEMODE'):
    slurp_contents.append(contents)
  
  assert(slurp_contents == expected_contents)

if __name__ == "__main__":
  test_islurp()

# Generated at 2022-06-14 06:00:17.059384
# Unit test for function islurp
def test_islurp():
    contents = list(islurp('test_data.txt'))
    assert contents == [
        '1\n',
        '2\n',
        '3\n',
        '4\n',
        '5\n'
    ]


# Generated at 2022-06-14 06:00:25.071214
# Unit test for function islurp
def test_islurp():
    test_value = 'Mi sed tamen pli amika kaj bonkora estis laŭ la maniero, kiajn aliaj homoj uzas ilin'
    fh = open('test_file.txt', 'w')
    fh.write(test_value)
    fh.close()

    assert islurp('test_file.txt') == test_value
    os.remove('test_file.txt')


# Generated at 2022-06-14 06:00:28.887578
# Unit test for function islurp
def test_islurp():
    assert list(islurp('-', allow_stdin=False)) == []
    assert list(islurp('-', allow_stdin=True)) == ['foo\n', 'bar\n']



# Generated at 2022-06-14 06:00:30.539131
# Unit test for function islurp
def test_islurp():
    import pprint
    pprint.pprint(list(islurp(__file__)))

# Generated at 2022-06-14 06:00:36.426444
# Unit test for function islurp

# Generated at 2022-06-14 06:00:39.555518
# Unit test for function burp
def test_burp():
    print("Test burp")
    filename = 'files.txt'
    contents = 'test string'
    burp(filename, contents)
    os.remove(filename)



# Generated at 2022-06-14 06:00:48.699805
# Unit test for function burp
def test_burp():
    filename = '/tmp/test_burp.txt'
    contents = 'Test contents'
    burp(filename, contents)
    fh = open(filename)
    assert(fh.read() == 'Test contents')
    fh.close()

if __name__ == "__main__":
    test_burp()

# vim: set ts=4 sts=4 sw=4 et:

# Generated at 2022-06-14 06:00:54.210504
# Unit test for function burp
def test_burp():
    import StringIO
    s = StringIO.StringIO()
    
    # Burp gives a file-like object as output
    assert burp(s, 'contents')
    # Burp gives stdout as output
    assert burp('-', 'contents')
    # Burp expands the filepath correctly
    assert burp('~/foo', 'contents')


# Generated at 2022-06-14 06:00:55.076412
# Unit test for function islurp
def test_islurp():
    assert True


# Generated at 2022-06-14 06:00:57.587931
# Unit test for function burp
def test_burp():
    import tempfile
    filename = tempfile.mkstemp()[1]
    contents = "Hello World\n"
    burp(filename, contents)
    assert open(filename, 'r').read() == contents
    os.remove(filename)


# Generated at 2022-06-14 06:01:01.982243
# Unit test for function islurp
def test_islurp():
    from utils.StringIO import StringIO
    sio = StringIO(u"First line\nSecond line\n")
    assert list(islurp(sio)) == [u"First line\n", u"Second line\n"]
    sio.seek(0)
    sio.truncate()
    sio.write(b"First\nSecond\n")
    assert list(islurp(sio)) == [b"First\n", b"Second\n"]

    sio.seek(0)
    sio.truncate()
    sio.write(b'\x80\x81\x82\x83\x84')
    assert list(islurp(sio, mode='rb')) == [b'\x80\x81\x82\x83\x84']

# Generated at 2022-06-14 06:01:09.415925
# Unit test for function islurp
def test_islurp():
    from tempfile import NamedTemporaryFile
    lines = ['This is line 1\n', 'This is line 2\n', 'This is line 3\n']
    with NamedTemporaryFile('w') as fh:
        fh.writelines(lines)
        fh.flush()
        assert list(islurp(fh.name)) == lines



# Generated at 2022-06-14 06:01:19.156904
# Unit test for function islurp
def test_islurp():
    import tempfile
    d = tempfile.mkdtemp()
    filename = os.path.join(d, 'test')
    lines = [
        'line1\n',
        'line2\n',
        'line3\n',
        'line4\n',
        'line5\n',
        'line6\n',
        'line7\n'
    ]
    with open(filename, 'w') as fh:
        fh.write(''.join(lines))

    # test by line
    actual = [l for l in islurp(filename)]
    assert actual == lines

    # test by chunks
    actual = []
    for x in islurp(filename, bytes(2), allow_stdin=False):
        actual.append(x)


# Generated at 2022-06-14 06:01:21.679009
# Unit test for function islurp

# Generated at 2022-06-14 06:01:24.519879
# Unit test for function islurp
def test_islurp():
    xs = list(islurp(__file__))
    assert xs[0] == '#!/usr/bin/env python\n'


# Generated at 2022-06-14 06:01:29.832817
# Unit test for function burp
def test_burp():
    """
    Test burp
    """
    import tempfile
    filename = tempfile.mktemp()
    burp(filename, """hello""")
    contents = slurp(filename)
    assert """hello""" in contents
    os.unlink(filename)


# Generated at 2022-06-14 06:01:43.361149
# Unit test for function islurp
def test_islurp():
    assert ''.join(islurp('/etc/hosts', iter_by=2)) == open('/etc/hosts', 'rb').read().decode('utf8')
    assert ''.join(islurp('/etc/hosts')) == open('/etc/hosts', 'r').read()
    assert ''.join(islurp('/etc/hosts', iter_by=1)) == open('/etc/hosts', 'r').read()
    assert ''.join(islurp('/etc/hosts', iter_by=2)) == open('/etc/hosts', 'r').read()


"""
Utilities to work with lists.
"""



# Generated at 2022-06-14 06:01:50.296087
# Unit test for function islurp
def test_islurp():
    #tests for slurping from stdin
    sys.stdin = open('temp.txt', 'r')
    assert '\n' == next(islurp('-', 'r', allow_stdin=True))
    sys.stdin = open('temp.txt', 'rb')
    assert b'\n' == next(islurp('-', 'rb', allow_stdin=True))
    sys.stdin.close()


# Generated at 2022-06-14 06:01:55.770452
# Unit test for function burp
def test_burp():
    """
    Test function burp.
    """
    target_file = 'testfile.txt'
    contents = 'Contents of testfile.txt'

    burp(target_file, contents)

    assert contents in islurp(target_file)


# Generated at 2022-06-14 06:01:57.753794
# Unit test for function islurp
def test_islurp():
    assert [x for x in islurp(__file__)]


# Generated at 2022-06-14 06:02:01.714484
# Unit test for function islurp
def test_islurp():
    s = list(islurp('../test/test_islurp.py'))
    assert len(s) == 4

if __name__ == '__main__':
    # Run `python ./futil.py` to run tests
    test_islurp()

# Generated at 2022-06-14 06:02:07.364733
# Unit test for function islurp
def test_islurp():
    # test the "normal" use case, which is to read from a file
    normal = islurp('test')
    assert normal == 'testing'

    # test the use case to read from stdin
    sys.stdin.write('testing stdin')
    sys.stdin.flush()
    stdin = islurp(sys.stdin)
    assert stdin == 'testing stdin'

    # without an exception, our tests have passed!

# Generated at 2022-06-14 06:02:20.325261
# Unit test for function islurp
def test_islurp():
    import tempfile
    import contextlib
    import random

    # Test when we don't give a filename
    with contextlib.suppress(TypeError):
        islurp()

    # Test reading from stdin
    with contextlib.redirect_stdin(sys.stdout):
        with contextlib.suppress(AttributeError):
            output = islurp('-', allow_stdin=True)

    # Test reading from a file
    with tempfile.NamedTemporaryFile() as fh:
        fh.write(b'Testing slurp\n')
        fh.flush()

        output = islurp(fh.name)
        output = list(output)

    assert len(output) == 1
    assert output[0] == b'Testing slurp\n'

    # Test reading from a file

# Generated at 2022-06-14 06:02:25.447937
# Unit test for function islurp
def test_islurp():
    fn = islurp('~/Downloads/dummy.txt', iter_by=1024*4)

# Generated at 2022-06-14 06:02:37.790083
# Unit test for function islurp
def test_islurp():
    import tempfile
    contents = 'hello\nworld'
    filename = tempfile.mktemp()
    with open(filename, 'w') as fh:
        fh.write(contents)

    # slurp line by line, std
    assert list(islurp(filename)) == contents.splitlines(True)

    # slurp line by line, keyword
    assert list(islurp(filename, iter_by=islurp.LINEMODE)) == contents.splitlines(True)

    # slurp chunks, std
    assert list(islurp(filename, iter_by=3)) == ['hel', 'lo\n', 'wor', 'ld']

    # slurp chunks, keyword

# Generated at 2022-06-14 06:02:50.904528
# Unit test for function islurp
def test_islurp():
    assert list(islurp('/etc/group', allow_stdin=False)) == list(islurp('/etc/group', allow_stdin=False))
    assert list(islurp(allow_stdin=False, filename='/etc/group')) == list(islurp(allow_stdin=False, filename='/etc/group'))
    assert list(islurp('/etc/group', allow_stdin=False, iter_by=2)) == list(islurp('/etc/group', allow_stdin=False, iter_by=2))
    assert list(islurp('/etc/group', allow_stdin=False, iter_by=2, mode='rb')) == list(islurp('/etc/group', allow_stdin=False, iter_by=2, mode='rb'))

# Generated at 2022-06-14 06:02:59.876728
# Unit test for function burp
def test_burp():
    """
    Test burp: Writes to a file and reads it back
    """
    content = 'Test test test\n'
    burp('testfile.txt',content)
    f1=open('testfile.txt','r')
    f2 = f1.read()
    assert (f2 == content)


# Generated at 2022-06-14 06:03:03.793817
# Unit test for function islurp
def test_islurp():
    for line in islurp('islurp_test.txt'):
        print(line)


if __name__ == '__main__':
    test_islurp()

# Generated at 2022-06-14 06:03:09.210903
# Unit test for function burp
def test_burp():
    filename = 'file_write.txt'
    contents = 'Hello my name is file_write.txt'
    x = burp(filename, contents)
    assert x == None
    fh = open(filename)
    x = fh.read()

# Generated at 2022-06-14 06:03:18.060532
# Unit test for function islurp
def test_islurp():
    import os
    import tempfile
    import contextlib

    # make an empty file for testing
    @contextlib.contextmanager
    def empty_file(**kwargs):
        _, filename = tempfile.mkstemp(**kwargs)
        try:
            yield filename
        finally:
            os.remove(filename)

    # create an empty file for testing
    with empty_file(prefix='islurp_') as empty:
        # islurp empty file
        with islurp(empty, iter_by=1) as lines:
            assert list(lines) == []

    # create a file with some text
    with empty_file(prefix='islurp_') as text:
        with open(text, 'w') as fh:
            fh.write("foo\nbar\n")

        # using

# Generated at 2022-06-14 06:03:19.880882
# Unit test for function islurp
def test_islurp():
    assert list(islurp(_)) == [_]


# Generated at 2022-06-14 06:03:23.630854
# Unit test for function islurp
def test_islurp():
    filename = "~/Documents/python_scripts/testfile.txt"
    #print os.path.expanduser(filename)

    for x in islurp(filename):
        print(x)


# Generated at 2022-06-14 06:03:29.735265
# Unit test for function burp
def test_burp():
    """
    Test for function burp
    """
    try:
        burp('./foo', 'bar', 'w')
        with open('./foo') as fh:
            assert fh.read() == 'bar'
    finally:
        # Remove foo file
        os.remove("./foo")

# Call function test_burp to unit test function burp
test_burp()

# Generated at 2022-06-14 06:03:42.629191
# Unit test for function islurp
def test_islurp():
    slurped = ''.join(islurp('/dev/zero', iter_by=1024))
    assert len(slurped) == 1024
    assert slurped == (chr(0) * 1024)

    slurped = ''.join(islurp('/dev/urandom', iter_by=10))
    assert len(slurped) == 10

    slurped = ''.join(islurp('/dev/urandom', iter_by=10, allow_stdin=False))
    assert len(slurped) == 10

    try:
        slurped = ''.join(islurp('-', iter_by=10, allow_stdin=True))
    except AttributeError:
        print("ERROR:  islurp('-', iter_by=10, allow_stdin=True) failed.")

#

# Generated at 2022-06-14 06:03:51.973108
# Unit test for function islurp
def test_islurp():
    import tempfile
    from io import BytesIO
    from io import StringIO
    from asserts import assert_equal, assert_in, assert_not_in
    from os.path import exists

    tfile = tempfile.NamedTemporaryFile()
    tfile.write(b'aaa\n')
    tfile.write(b'bbb\n')
    tfile.flush()

    data = [line for line in islurp(tfile.name)]
    assert_equal(data, ['aaa\n', 'bbb\n'])

    data = [line for line in islurp(tfile.name, iter_by=100)]
    assert_equal(data, ['aaa\nbbb\n'])

    tfile.close()
    assert_equal(exists(tfile.name), False)



# Generated at 2022-06-14 06:04:03.200328
# Unit test for function islurp
def test_islurp():
    # the following content is from the file islurp_test.txt
    content = '''I am learning Python
        I am learning Python
        I am learning Python
        I am learning Python'''

    # if the input is from stdout
    count = 0
    for line in islurp(sys.stdin):
        count += 1
        if count > 4:
            break
    assert count == 4

    # if the input is from a file
    for line1, line2 in zip(islurp('./islurp_test.txt'), content.split('\n')):
        assert line1 == line2
        # print(line1)

    # if the iter_by is bytes
    count = 0

# Generated at 2022-06-14 06:04:10.314218
# Unit test for function burp
def test_burp():
    import tempfile
    tmp_fname = tempfile.NamedTemporaryFile(delete=False).name
    burp(tmp_fname, "test")
    os.remove (tmp_fname)


# Generated at 2022-06-14 06:04:19.128079
# Unit test for function islurp
def test_islurp():
    """
    Test islurp()
    """
    lines = islurp(__file__)
    print(len(list(lines)))
    lines = islurp(__file__, iter_by=4096)
    print(len(list(lines)))
    lines = islurp(__file__, mode='rb')
    print(len(list(lines)))
    lines = islurp(__file__, mode='rb', iter_by=4096)
    print(len(list(lines)))

if __name__ == '__main__':
    test_islurp()

# Generated at 2022-06-14 06:04:29.389451
# Unit test for function burp
def test_burp():
    # Test writing to a file
    result = burp("burp.tmp", "This is a good test")
    assert result == None
    assert os.path.isfile("burp.tmp")
    fh = open("burp.tmp", "r")
    assert fh.read() == "This is a good test"
    fh.close()
    os.unlink("burp.tmp")

    # Test writing to stdout
    result = burp("-", "This is a good test", allow_stdout=True)
    assert result == None


# Generated at 2022-06-14 06:04:40.861640
# Unit test for function islurp
def test_islurp():
    assert islurp('/dev/null') == []
    assert islurp('/dev/zero', iter_by=512) == ['\x00'*512]
    assert islurp('/dev/zero', iter_by=513) == ['\x00'*513]
    assert islurp('/dev/zero', iter_by=LINEMODE) == ['']
    assert islurp('/dev/zero', iter_by=0) == ['\x00'*512]
    assert islurp('/dev/zero', iter_by=-1) == ['\x00'*512]
    assert islurp('/dev/zero', iter_by=1024) == ['\x00'*512, '\x00'*512]

# Generated at 2022-06-14 06:04:44.445068
# Unit test for function islurp

# Generated at 2022-06-14 06:04:54.710876
# Unit test for function islurp
def test_islurp():
    import StringIO


# Generated at 2022-06-14 06:04:59.563289
# Unit test for function burp
def test_burp():
    contents = "Testing burp function"
    filename = "foo.txt"
    burp(filename, contents)
    fh = open(filename, "r")
    assert(fh.read() == contents)
    fh.close()
    os.remove(filename)

# Generated at 2022-06-14 06:05:10.127158
# Unit test for function burp
def test_burp():
    """
    Test burp function.
    """
    from random import randint
    from tempfile import gettempdir
    from os.path import join
    from os import remove

    # write to temp file, read back
    test_str = "test"
    file_path = join(gettempdir(), "burp_test_%s_%s" % (test_str, randint(0, 1000000000)))
    burp(file_path, test_str, mode='w')
    assert slurp(file_path, mode='r', iter_by=LINEMODE, allow_stdin=False, expanduser=True, expandvars=True).next() == test_str
    try:
        remove(file_path)
    except OSError:
        pass

    # write to stdout

# Generated at 2022-06-14 06:05:20.038795
# Unit test for function burp
def test_burp():
    # 11-12-2018
    # This is the basic functionality of the function burp.
    # Given a filename, it reads and writes the contents of the file.
    # NOTE: I was unable to test this file, because it was not complete.
    # So, I added some code to the end of the file to make it into a proper unit test.
    # Also, I need to add a line to this code that converts it to a proper unit test.
    # This is the expected result.
    assert(burp('test.txt', 'Hello', 'w') == 'Hello')



# Generated at 2022-06-14 06:05:28.141535
# Unit test for function islurp
def test_islurp():
    filename = "test_file.txt"
    s = "test line one\ntest line two\ntest line three\n"

    with open(filename, "w") as fh:
        fh.write(s)

    lines = list(islurp(filename))
    assert lines[0] == "test line one\n"
    assert lines[1] == "test line two\n"
    assert lines[2] == "test line three\n"

    os.unlink(filename)


# Generated at 2022-06-14 06:05:56.343718
# Unit test for function islurp
def test_islurp():
    """
    Unit test for function islurp
    """
    import os
    import tempfile
    test_str = 'Hello\nWorld\n'
    with tempfile.NamedTemporaryFile(mode='w+') as file_handle:
        file_handle.write('Hello\nWorld\n')
        file_handle.flush()
        result = ''
        for line in islurp(file_handle.name):
            result += line
        assert test_str == result
    test_result = list(islurp(os.devnull, allow_stdin=False))
    assert not test_result
    test_result = list(islurp('-', allow_stdin=False))
    assert not test_result
    test_result = list(islurp('-', allow_stdin=True))
   

# Generated at 2022-06-14 06:06:08.280487
# Unit test for function islurp
def test_islurp():
    from io import StringIO
    from contextlib import contextmanager

    @contextmanager
    def stdin_string(contents):
        orig_stdin = sys.stdin
        sys.stdin = StringIO(contents)
        yield
        sys.stdin = orig_stdin

    with stdin_string("1\n2\n3") as _:
        assert [line for line in islurp('-')] == ["1\n", "2\n", "3"]
    assert list(islurp('/dev/null')) == []
    assert [line for line in islurp(__file__)] and len([line for line in islurp(__file__)]) > 0


# Generated at 2022-06-14 06:06:14.574954
# Unit test for function islurp
def test_islurp():
    test_islurp.__test__ = False
    assert list(islurp(__file__)) == list(slurp(__file__))
    assert list(islurp(__file__, iter_by=65536)) == list(slurp(__file__, iter_by=65536))


# Generated at 2022-06-14 06:06:25.079737
# Unit test for function islurp
def test_islurp():
    """
    Unit test for function islurp
    """
    from io import StringIO
    import sys

    def test_slurp_file(filename, expect_result, mode='r'):
        """
        Unit test for function islurp
        """
        result = list(islurp(filename, mode))
        assert result == expect_result

    # Test cases

# Generated at 2022-06-14 06:06:32.452947
# Unit test for function islurp
def test_islurp():
    # Arrange
    filename = 'test_islurp.txt'
    expected = list(range(100))

    # Act
    with open(filename, 'wt') as fh:
        fh.write('\n'.join([str(i) for i in expected]))

    # Assert
    with open(filename) as fh:
        assert fh.read() == '\n'.join([str(i) for i in expected]) + '\n'

    actual = list(islurp(filename))
    actual = [int(x) for x in actual]

    assert actual == expected


# Generated at 2022-06-14 06:06:41.477095
# Unit test for function islurp
def test_islurp():
    try:
        import pytest
        assert pytest
    except ImportError:
        return

    # Test a file that doesn't exist
    with pytest.raises(OSError):
        islurp("/tmp/doesnotexist")

    # Test with a file that does exist
    for x in islurp("/etc/passwd"):
        assert isinstance(x, str)


if __name__ == '__main__':
    test_islurp()

# Generated at 2022-06-14 06:06:45.846833
# Unit test for function burp
def test_burp():
    burp("test_burp_file", "This is a test of the burp function")
    f = islurp("test_burp_file")
    assert("This is a test of the burp function" == next(f))
    os.remove("test_burp_file")

# Generated at 2022-06-14 06:06:55.966345
# Unit test for function islurp
def test_islurp():
    import sys
    sys.argv.append("file")
    with open("file","w") as fh:
        fh.write("Hello world\nline 2\nline 3")
    assert list(islurp("file")) == ['Hello world\n', 'line 2\n', 'line 3']
    assert list(islurp("file", iter_by=5)) == ['Hello', ' worl', 'd\nlin', 'e 2\nli', 'ne 3']
    assert list(islurp("file", allow_stdin=True)) == ['Hello world\n', 'line 2\n', 'line 3']


# Generated at 2022-06-14 06:06:59.770214
# Unit test for function islurp
def test_islurp():
    assert list(islurp('',)) == ['']
    try:
        list(islurp(''))
        assert False
    except Exception as e:
        assert True


# Generated at 2022-06-14 06:07:07.741440
# Unit test for function islurp
def test_islurp():
    for line in islurp(__file__):
        assert line
    for line in islurp(__file__, allow_stdin=False):
        assert line
    for line in islurp(__file__, expanduser=False):
        assert line
    for line in islurp(__file__, expandvars=False):
        assert line
    for line in islurp(__file__, expanduser=False, expandvars=False):
        assert line
    for line in islurp(__file__, iter_by=1):
        assert line
    for line in islurp(__file__, iter_by=10000):
        assert line

# Generated at 2022-06-14 06:07:19.571860
# Unit test for function islurp
def test_islurp():
    # test filename = ./
    try:
        for l in islurp('./'):
            pass
    except IsADirectoryError:
        pass
    else:
        raise Exception('Failed to detect burp as a directory')



# Generated at 2022-06-14 06:07:28.882011
# Unit test for function burp
def test_burp():
    from os.path import isdir, isfile, realpath
    from tempfile import mkdtemp, mkstemp
    from shutil import rmtree

    tmpdir = mkdtemp()
    dirfile = realpath(tmpdir)
    tmpfile = mkstemp(dir=tmpdir)[1]
    dirfile = mkstemp(dir=tmpdir)[1]


# Generated at 2022-06-14 06:07:35.449358
# Unit test for function islurp
def test_islurp():
    assert list(islurp('utils.py'))[0:3] == ['"""\n', 'Utilities to work with files.\n', '"""\n']
    assert list(islurp('utils.py', iter_by=3)) == ['"""\n', 'Ut', 'ili']

if __name__ == '__main__':
    test_islurp()

# Generated at 2022-06-14 06:07:48.915493
# Unit test for function islurp

# Generated at 2022-06-14 06:07:56.078926
# Unit test for function islurp
def test_islurp():
    assert next(islurp(__file__)) == "# Utilities to work with files.\n"
    assert next(islurp(__file__, 'rb')) == "# Utilities to work with files.\n"
    assert next(islurp(__file__, iter_by=50)) == "# Utilities to work with files.\n"
    assert next(islurp('-', allow_stdin=True)) == '\n'
    assert next(islurp('~/foo')) == '\n'
    assert next(islurp('$HOME/foo')) == '\n'



# Generated at 2022-06-14 06:08:08.824553
# Unit test for function islurp
def test_islurp():
    """
    Tests for islurp function.
    """
    import io
    import unittest

    class TestIslurp(unittest.TestCase):

        def test_islurp_with_default_expanduser(self):
            """
            Test islurp in default expanduser mode.
            """
            expected_list = ['abcd\n', 'efgh\n', 'ijkl\n', 'mnop\n', 'qrst']
            filename = "~/test.txt"
            fh = io.StringIO()
            burp(fh, ''.join(expected_list))
            fh.seek(0)

            actual_list = []
            for line in islurp(filename):
                actual_list.append(line)


# Generated at 2022-06-14 06:08:21.072584
# Unit test for function islurp
def test_islurp():
    # Test with invalid file
    results = []
    g = islurp('INVALID_FILE')
    try:
        while True:
            results.append(g.next())
    except StopIteration:
        pass
    assert results == []

    # Test with valid file
    results = []
    fh_curr_dir = os.path.dirname(__file__)
    test_file = os.path.join(fh_curr_dir, 'test.txt')
    g = islurp(test_file)
    try:
        while True:
            results.append(g.next())
    except StopIteration:
        pass
    assert results == ['abc\n', 'xyz\n', '123\n']

    # Test with windows line endings
    results = []
    test_

# Generated at 2022-06-14 06:08:31.130220
# Unit test for function islurp
def test_islurp():

    # Test with file
    fname = 'test_islurp.txt'
    test_string = 'hello world'

    with open(fname, 'w') as fw:
        fw.write(test_string)

    for line in islurp(fname):
        if not test_string in line:
            raise ValueError('Failed islurp test')
    os.remove(fname)

    # Test with stdin
    test_string = 'apple pie'
    with open(fname, 'w') as fw:
        fw.write(test_string)

    for line in islurp('-', allow_stdin=False):
        if not test_string in line:
            raise ValueError('Failed islurp test')

    # Test with stdin, allow_stdin

# Generated at 2022-06-14 06:08:34.495511
# Unit test for function islurp
def test_islurp():
    fh = islurp.open('.gitignore')
    assert fh is not None
    for line in fh:
        print(line)


# Generated at 2022-06-14 06:08:43.296369
# Unit test for function islurp
def test_islurp():
    """
    Test islurp function.
    """
    test_filename = 'tests/resources/islurp.txt'
    expected_arr = ['line one\x0a', 'line two\x0a', 'line three\x0a', 'line four\x0a', 'line five\x0a', 'line six and half\x0a', 'line seven\x0a', 'line seven pt. two\x0a', 'line eight\x0a', 'line nine\x0a', 'line ten\x0a']
    for index, line in enumerate(islurp(test_filename)):
        assert line == expected_arr[index]

# Generated at 2022-06-14 06:08:58.066905
# Unit test for function islurp
def test_islurp():
    """
    Test function: islurp()
    """
    content = '''\
#!/usr/bin/env python

from __future__ import print_function

if __name__ == '__main__':
    print('hello world')
    '''

    import tempfile
    filename = tempfile.mktemp()
    with open(filename, 'w') as fh:
        fh.write(content)


# Generated at 2022-06-14 06:09:11.728481
# Unit test for function islurp
def test_islurp():
    # create and open a test file
    f = open("test_islurp.txt","w")
    # write data to test file
    f.write("This is the test file for islurp()")
    f.close()
    # test filename = file
    assert('This is the test file for islurp()' == list(islurp("test_islurp.txt"))[0])
    # test filename = stdin and allow_stdin = False
    try:
        list(islurp("-",allow_stdin=False))
    except Exception as e:
        assert(type(e) == FileNotFoundError)
    # test invalid filename

# Generated at 2022-06-14 06:09:21.701226
# Unit test for function islurp
def test_islurp():
    assert list(islurp('../test/data/test_islurp', iter_by=1)) == ['F', 'i', 'r', 's', 't', '\n', 'S', 'e', 'c', 'o', 'n', 'd', '\n', 'T', 'h', 'i', 'r', 'd', '\n']
    assert list(islurp('../test/data/test_islurp', iter_by=2)) == ['Fi', 'rs', 't\n', 'Se', 'co', 'nd', '\n', 'Th', 'ir', 'd\n']

# Generated at 2022-06-14 06:09:31.704792
# Unit test for function islurp
def test_islurp():
    # test with file
    if os.path.exists('test_islurp.txt'):
        os.remove('test_islurp.txt')
    test_file = open('test_islurp.txt', 'w+')
    test_file.write('abcd efg hijk lmn')
    test_file.close()
    assert list(islurp('test_islurp.txt')) == ['abcd efg hijk lmn']
    assert list(islurp('test_islurp.txt', iter_by=1)) == ['a', 'b', 'c', 'd', ' ', 'e', 'f', 'g', ' ', 'h', 'i', 'j', 'k',
                                                         ' ', 'l', 'm', 'n']

    # test without file