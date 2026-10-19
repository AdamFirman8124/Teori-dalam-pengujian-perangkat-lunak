

# Generated at 2022-06-14 05:59:45.823574
# Unit test for function islurp
def test_islurp():
    print('Testing islurp')
    # Test simple file
    test_file = "/tmp/test_file"
    test_content = "This is some test text"
    try:
        with open(test_file, "w") as file:
            file.write(test_content)
        slurped_text = ""
        for text in islurp(test_file):
            slurped_text += text
        assert test_content == slurped_text
    finally:
        if os.path.isfile(test_file):
            os.remove(test_file)
    print("Passed islurp test")


# Generated at 2022-06-14 05:59:56.948423
# Unit test for function islurp
def test_islurp():
    text = "a,1\nb,2\nc,3\nd,4\n"
    # test no file
    assert list(islurp('no_file_here', allow_stdin=False)) == []
    # test small file by line
    assert list(islurp('_files/test.csv', allow_stdin=False)) == [x + '\n' for x in text.split('\n')]
    # test small file by chunk
    assert list(islurp('_files/test.csv', iter_by=2, allow_stdin=False)) == [x.encode('utf-8') for x in text]
    # test stdin
    import io
    import sys
    sys.stdin = io.StringIO(text)

# Generated at 2022-06-14 06:00:08.202886
# Unit test for function burp
def test_burp():

    # Test string
    test_string = "123456789"

    # Test burp, create file
    fname = 'test_burp_filename'
    burp(fname, test_string)
    assert os.path.isfile(fname)

    # Test burp, write to file
    burp(fname, test_string)
    assert os.path.isfile(fname)
    f = open(fname, 'r')
    assert f.read() == test_string + test_string

    # Test burp, write to stdout
    import sys
    from contextlib import contextmanager
    from StringIO import StringIO
    @contextmanager
    def captured_output():
        new_out, new_err = StringIO(), StringIO()
        old_out, old_err = sys.stdout,

# Generated at 2022-06-14 06:00:20.282596
# Unit test for function islurp
def test_islurp():
    files = ["test_islurp.txt", "temp.txt"]
    for file in files:
        with open(file, "w") as fh:
            fh.write("testing123")
    try:
        assert next(islurp("-", allow_stdin=False)) == "testing123"
        assert next(islurp("test_islurp.txt")) == "testing123"
        assert next(islurp("test_islurp.txt", expandvars=False)) == "testing123"
        assert next(islurp("test_islurp.txt", expandvars=False, expanduser=False)) == "testing123"
    except Exception:
        raise Exception("test_islurp() failed")
    finally:
        for file in files:
            os.remove(file)


# Generated at 2022-06-14 06:00:29.252736
# Unit test for function islurp
def test_islurp():
    from os import path
    import tempfile
    with tempfile.TemporaryDirectory() as dirname:
        tempfile.mkstemp(dir=dirname)
        filename = path.join(dirname, 'foo.txt')
        with open(filename, 'w') as f:
            f.write("This is line1\nThis is line2\nThis is line3")
        assert islurp(filename).__next__() == "This is line1\n"
        assert "line3" in list(islurp(filename))

# Generated at 2022-06-14 06:00:37.925421
# Unit test for function burp
def test_burp():
    import tempfile
    import os
    filename = tempfile.mktemp()
    burp(filename, "test content")
    with open(filename, 'r') as fh:
        assert fh.read() == "test content"
    os.remove(filename)

if __name__ == '__main__':
    contents = '\n'.join(islurp(sys.argv[1], 'rb', allow_stdin=False))
    sys.stdout.write(contents)

# Generated at 2022-06-14 06:00:40.594857
# Unit test for function burp
def test_burp():
    burp('test.txt', 'Hello World!')
    assert(islurp('test.txt') == ['Hello World!'])
    os.remove('test.txt')


# Generated at 2022-06-14 06:00:47.874619
# Unit test for function islurp
def test_islurp():
    file1 = 'sample.txt'
    with open(file1, 'w') as fh:
        fh.write("""This is
a sample
text file.""")

    result = [x for x in islurp(file1)]
    exp = ["This is\n",
           "a sample\n",
           "text file."]
    assert result == exp


# Generated at 2022-06-14 06:00:50.075720
# Unit test for function burp
def test_burp():
    burp('burp.txt', 'Testing burp...', mode='w')



# Generated at 2022-06-14 06:00:56.809539
# Unit test for function islurp
def test_islurp():
    for c in islurp(__file__):
        assert isinstance(c, str)
    for c in islurp(__file__, 'rb'):
        assert isinstance(c, bytes)
    for c in islurp(__file__, iter_by=16):
        assert isinstance(c, str)
        assert len(c) == 16



# Generated at 2022-06-14 06:01:04.727702
# Unit test for function burp
def test_burp():
    from StringIO import StringIO
    stdout = sys.stdout
    sys.stdout = StringIO()
    burp("-", "hello")
    assert sys.stdout.getvalue() == "hello"
    sys.stdout.close()
    sys.stdout = stdout


# Generated at 2022-06-14 06:01:12.242478
# Unit test for function burp
def test_burp():
    filename = '/tmp/burp.txt'
    contents = "Burp\n"
    burp(filename, contents)
    with open(filename) as f:
        text = f.read()
    assert contents == text
    os.remove(filename)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 06:01:16.321140
# Unit test for function burp
def test_burp():
    import tempfile

    tmpdir = tempfile.mkdtemp()
    tmpfile = os.path.join(tmpdir, 'burp_test.txt')
    burp(tmpfile, 'hello')
    assert open(tmpfile).read() == 'hello'
    os.remove(tmpfile)
    os.rmdir(tmpdir)



# Generated at 2022-06-14 06:01:21.047122
# Unit test for function burp
def test_burp():
    burp('/tmp/burp.txt', 'howdy doody')
    slurped = slurp('/tmp/burp.txt')
    assert list(slurped)[0] == 'howdy doody'


# Generated at 2022-06-14 06:01:28.405762
# Unit test for function burp
def test_burp():

    filename = 'burp_test.txt'
    contents = 'This is the text that is written to the file.'

    # Write to file
    burp(filename, contents)

    # Read file and compare to contents
    with open(filename, 'r') as fh:
        contents_from_file = fh.read()
    assert contents == contents_from_file

    # Clean up
    os.remove(filename)

test_burp()



# Generated at 2022-06-14 06:01:34.664824
# Unit test for function burp
def test_burp():
    import tempfile
    with tempfile.NamedTemporaryFile(delete=False,mode='a+') as f:
        name=f.name
        #print('temp file name: '+name)
    contents='hello'
    burp(name, contents)
    with open(name, mode='r') as f:
        assert f.readline()==contents
    os.remove(name)



# Generated at 2022-06-14 06:01:36.341489
# Unit test for function islurp
def test_islurp():
    for item in islurp("/tmp/test_islurp.txt"):
        print(item)


# Generated at 2022-06-14 06:01:41.662360
# Unit test for function burp
def test_burp():
    assert burp('./test_burp_file.txt', 'burp') == None
    with open('./test_burp_file.txt') as f:
        assert f.readlines()[0] == 'burp'
    os.remove('./test_burp_file.txt')



# Generated at 2022-06-14 06:01:52.692820
# Unit test for function burp
def test_burp():
    import StringIO
    import tempfile
    import os

    fh = StringIO.StringIO()
    # test for stdout
    burp('-', 'hello, world!', mode='w', allow_stdout=True, expanduser=False, expandvars=False, fh=fh)

    # test for file
    fh = StringIO.StringIO()
    output_file = tempfile.NamedTemporaryFile(delete=False)
    output_file.close()
    burp(output_file.name, 'hello, world!', mode='w', allow_stdout=False, expanduser=False, expandvars=False, fh=fh)

    # clean up
    os.unlink(output_file.name)



# Generated at 2022-06-14 06:01:59.474705
# Unit test for function islurp
def test_islurp():
    t_file = "/tmp/test_islurp.txt"
    t_data = b"This is a test file\n"

    with open(t_file, "wb") as tf:
        tf.write(t_data)

    for tline in islurp(t_file):
        assert tline == t_data.decode("utf-8")
    os.unlink(t_file)


if __name__ == "__main__":
    test_islurp()

# Generated at 2022-06-14 06:02:11.343297
# Unit test for function islurp
def test_islurp():
    assert [x for x in islurp('/dev/null')] == []
    assert islurp('/dev/null', iter_by=1) == []
    assert list(islurp('/dev/null', iter_by=1)) == []
    assert islurp('/dev/null', iter_by='LINEMODE') == []
    assert list(islurp('/dev/null', iter_by='LINEMODE')) == []
    assert list(islurp('/dev/null')) == []
    assert list(islurp('/dev/null', iter_by=128)) == []

    buf = ''.join(islurp(__file__))
    assert buf



# Generated at 2022-06-14 06:02:18.209674
# Unit test for function islurp
def test_islurp():
    import tempfile
    import shutil

    tmpdir = tempfile.mkdtemp()

    with open(os.path.join(tmpdir, 'foo'), 'w') as fh:
        fh.write('This is a test.\n')

    for line in slurp(os.path.join(tmpdir, 'foo')):
        print(line)

    shutil.rmtree(tmpdir)

# Generated at 2022-06-14 06:02:21.405782
# Unit test for function burp
def test_burp():
    import tempfile
    fname = tempfile.mktemp()
    contents = "test\n"
    burp(fname, contents)
    s = slurp(fname).next()
    assert s==contents

# Generated at 2022-06-14 06:02:34.183216
# Unit test for function islurp
def test_islurp():
    file = open('/tmp/test', 'w')
    file.write('line1\nline2')
    file.close()
    result = islurp('/tmp/test')
    assert list(result) == ['line1\n', 'line2']
    file = open('/tmp/test', 'w')
    file.write('line1\nline2')
    file.close()
    result = islurp('/tmp/test', 'rb')
    assert list(result) == ['line1\n', 'line2']
    file = open('/tmp/test', 'w')
    file.write('line1\nline2')
    file.close()
    result = islurp('/tmp/test', iter_by=2)

# Generated at 2022-06-14 06:02:39.911339
# Unit test for function burp
def test_burp():
    burp("test.txt", "This is a test to see if burp worked")
    f = open("test.txt", "r")
    assert f.read() == "This is a test to see if burp worked"
    f.close()
    os.remove("test.txt")


# Generated at 2022-06-14 06:02:52.991002
# Unit test for function burp
def test_burp():
    import tempfile
    import filecmp
    import io

    tmpdir = tempfile.TemporaryDirectory()
    tmpdir_name = tmpdir.name
    tmpdir_file = os.path.join(tmpdir_name, 'file_write.txt')
    tmpdir_file_gold = os.path.join(tmpdir_name, 'file_write_gold.txt')
    tmpdir_file_gold_data = 'file_write_gold'

    with open(tmpdir_file_gold, 'w') as fw:
        fw.write(tmpdir_file_gold_data)

    with io.StringIO() as sio:
        sio.write(tmpdir_file_gold_data)
        sio.seek(0)
        burp(tmpdir_file, sio.read())

    assert file

# Generated at 2022-06-14 06:03:01.822429
# Unit test for function islurp
def test_islurp():
    class StdinMock:
        def __init__(self, lines):
            self._lines = lines

        def readline(self):
            if len(self._lines) == 0:
                return ""
            else:
                return self._lines.pop(0)

    class StdoutMock:
        def __init__(self):
            self._lines = []

        def write(self, content):
            self._lines.append(content)

        def getlines(self):
            return self._lines

    def test_islurp_file(filename, lines):
        fh = open(filename, 'w')
        for line in lines:
            fh.write(line)
        fh.close()

        read_lines = []

# Generated at 2022-06-14 06:03:04.892075
# Unit test for function islurp
def test_islurp():
    assert list(islurp('/usr/share/dict/words', iter_by=10)) == list(islurp('/usr/share/dict/words', iter_by=10, allow_stdin=False))

# Generated at 2022-06-14 06:03:13.675389
# Unit test for function islurp
def test_islurp():
    """
    Unit test for function islurp
    """
    import time
    import random
    contents = ''.join([str(time.time()) + ': ' + str(random.randint(0, 1000)) + '\n' for x in range(1000)])

    # test simple write/read
    testfile = 'tmp.txt'
    burp(testfile, contents)
    for line in islurp(testfile):
        assert line in contents

    # test read from stdin
    for line in islurp('-', allow_stdout=True):
        assert line in contents

    # clean up
    os.remove(testfile)



# Generated at 2022-06-14 06:03:19.630115
# Unit test for function burp
def test_burp():
    burp(filename='./test_burp.txt', contents='I am burping!')
    assert open('./test_burp.txt','r').read() == 'I am burping!'
    os.remove('./test_burp.txt')
    return True

# Generated at 2022-06-14 06:04:11.160953
# Unit test for function islurp
def test_islurp():
    # Test for file that does not exist
    with open('fakefile1') as fh:
        filename = fh.read()
    # Test for file that does exist
    with open('fakefile2') as fh:
        filename = fh.read()
    # Test for file that exists and has permission to read
    with open('fakefile3') as fh:
        filename = fh.read()
    # Test for files that are unreadable
    with open('fakefile4') as fh:
        filename = fh.read()
    # Test for files with permission denied
    with open('fakefile5') as fh:
        filename = fh.read()
    # Test for files with permission denied
    with open('fakefile6') as fh:
        filename = fh.read()
    # Test for files that does

# Generated at 2022-06-14 06:04:20.095084
# Unit test for function islurp
def test_islurp():
    assert list(islurp('tests/test.txt', iter_by=1)) == ['H','e','l','l','o','\n','W','o','r','l','d','!','\n']
    assert list(islurp('tests/test.txt', iter_by=5)) == ['Hello\n', 'World!\n']
    assert list(islurp('tests/test.txt', iter_by=LINEMODE)) == ['Hello\n', 'World!\n']
    assert slurp('tests/test.txt') == list(islurp('tests/test.txt', iter_by=LINEMODE))


# Generated at 2022-06-14 06:04:25.921865
# Unit test for function burp
def test_burp():
    burp('test.txt', 'line1\nline2\nline3\n')
    assert(slurp('test.txt') == ['line1\n', 'line2\n', 'line3\n'])
    os.remove('test.txt')

# Generated at 2022-06-14 06:04:33.634383
# Unit test for function islurp
def test_islurp():
    import os

    expected = [
        'This is a test file.\n',
        'Another line of text.\n',
    ]

    test_file = '~/tmp/file_utils_test.txt'
    test_file = os.path.expanduser(test_file)
    burp(test_file, ''.join(expected))

    i = 0
    for line in islurp(test_file):
        assert line == expected[i]
        i += 1

    os.remove(test_file)

# Generated at 2022-06-14 06:04:39.850524
# Unit test for function islurp
def test_islurp():
    sample_file = 'tests/sample_file.txt'
    expected_contents = [
        'foo\n',
        'bar\n',
        'baz\n',
        'boo\n'
    ]
    for line, expected in zip(islurp(sample_file), expected_contents):
        assert line == expected


# Generated at 2022-06-14 06:04:45.810279
# Unit test for function burp
def test_burp():
    import tempfile

    filename = tempfile.mktemp()
    contents = 'hello world'
    burp(filename, contents)
    slurp_contents = slurp(filename).next()
    assert slurp_contents == contents

    try:
        os.remove(filename)
    except:
        pass

# Generated at 2022-06-14 06:04:54.398796
# Unit test for function islurp
def test_islurp():
    expected = ['#!/usr/bin/python', '', 'import sys', '']
    actual = [x for x in islurp('../bin/isort_helpers/slugify.py')]
    assert expected == actual
    expected = ['\x89PNG\r\n']
    actual = [x for x in islurp('isort.png', iter_by=8)]
    assert expected == actual
    assert [x for x in islurp('isort.png')] == [None]
    assert [x for x in islurp('non-existant.file')] == [None]
    expected = ['Hello\n', 'World\n']
    actual = [x for x in islurp('-', allow_stdin=True, iter_by=5)]
    assert expected == actual

# Generated at 2022-06-14 06:05:00.710959
# Unit test for function burp
def test_burp():
    import tempfile
    import os

    fd, fname = tempfile.mkstemp()
    os.close(fd)
    try:
        burp(fname, 'hello world')
        assert slurp(fname) == 'hello world'
    finally:
        os.remove(fname)
# vim: sw=4:expandtab:ts=4

# Generated at 2022-06-14 06:05:11.099179
# Unit test for function islurp
def test_islurp():
    from tempfile import NamedTemporaryFile
    from subprocess import check_call
    from nose.tools import with_setup

    fh = None
    def setup_islurp():
        nonlocal fh
        with NamedTemporaryFile(suffix='.dat', delete=False) as tf:
            fh = tf
            tf.write(b"line 1\nline 2\n")
            tf.flush()
        return fh.name

    def test_islurp_lines(fn=None):
        nonlocal fh
        lines = [line.rstrip(b'\n') for line in islurp(fn)]
        assert lines == [b"line 1", b"line 2"]

    def test_islurp_binary(fn=None):
        nonlocal fh

# Generated at 2022-06-14 06:05:24.015209
# Unit test for function islurp
def test_islurp():
    assert list(islurp('/dev/null')) == []
    assert list(islurp('/dev/null', mode='rb')) == []
    assert list(islurp('/dev/zero')) == []
    assert list(islurp('/dev/zero', mode='rb', iter_by=32)) == [b"\x00" * 32] * 3
    assert list(islurp('/dev/zero', mode='rb', iter_by=63)) == [b"\x00" * 63] * 2
    assert list(islurp('/dev/zero', mode='rb', iter_by=64)) == [b"\x00" * 64] * 2

# Generated at 2022-06-14 06:06:42.301168
# Unit test for function islurp
def test_islurp():
    """
    Test islurp
    """
    import utils

# Generated at 2022-06-14 06:06:50.013324
# Unit test for function islurp
def test_islurp():
    import tempfile

    with tempfile.NamedTemporaryFile(mode='w') as fh:
        path = fh.name

        # write a line
        fh.write('line 1\n')
        fh.seek(0)
        lines = list(islurp(path))
        assert lines == ['line 1\n']

        # overwrite with a longer line
        fh.seek(0)
        fh.write('line 2\n')
        fh.seek(0)
        lines = list(islurp(path))
        assert lines == ['line 2\n']

        # add another line
        fh.seek(0)
        fh.write('line 3\n')
        fh.seek(0)
        lines = list(islurp(path))

# Generated at 2022-06-14 06:07:03.234046
# Unit test for function islurp
def test_islurp():
    assert list(islurp("/etc/passwd")) == ["root:x:0:0:root:/root:/bin/bash\n", "daemon:x:1:1:daemon:/usr/sbin:/bin/sh\n", "bin:x:2:2:bin:/bin:/bin/sh\n", "sys:x:3:3:sys:/dev:/bin/sh\n", "sync:x:4:65534:sync:/bin:/bin/sync\n", "games:x:5:60:games:/usr/games:/bin/sh\n", "man:x:6:12:man:/var/cache/man:/bin/sh\n"]
    assert list(islurp("/")) == [""]

# Generated at 2022-06-14 06:07:19.575259
# Unit test for function islurp
def test_islurp():
    import sys
    from pprint import pprint
    from dez.io import islurp
    from dez.io import burp as io_burp
    from dez.io import slurp as io_slurp
    # TODO: make this depend on pytest vs nose vs ...
    # TODO: dont forget to add a python package version check, eg
    #       if sys.version_info.major < 3:
    #           ...
    if not os.path.exists('tests'):
        os.mkdir('tests')
    if not os.path.exists('tests/fixtures'):
        os.mkdir('tests/fixtures')
    if not os.path.exists('tests/fixtures/islurp'):
        os.mkdir('tests/fixtures/islurp')
    #

# Generated at 2022-06-14 06:07:28.922765
# Unit test for function islurp
def test_islurp():
    # Check with the default value for iter_by
    for i, line in enumerate(islurp('test_slurp.py', mode='r', iter_by=LINEMODE)):
        if i == 5:
            assert line == "slurp = islurp\n"

        if i == len(list(islurp('test_slurp.py', mode='r', iter_by=LINEMODE)))-1:
            assert line == "'''\n"

    # Check with the default value for iter_by
    fd = islurp('test_slurp.py', mode='r')
    if sys.version_info[0] == 3:
        assert next(fd) == "#!/usr/bin/env python\n"

# Generated at 2022-06-14 06:07:37.630868
# Unit test for function islurp
def test_islurp():
    # Test with file
    assert '\n'.join(islurp('/bin/ls')) == '\n'.join(open('/bin/ls').readlines())
    assert list(islurp('/bin/ls')) == list(open('/bin/ls').readlines())

    # Test with -
    import sys
    sys.stdin = open('/bin/ls')
    assert '\n'.join(islurp('-')) == '\n'.join(open('/bin/ls').readlines())
    sys.stdin.close()


# Generated at 2022-06-14 06:07:43.671667
# Unit test for function burp
def test_burp():
    original = 'hello, world'
    burp('test_burp.txt', original)
    with open('test_burp.txt') as f:
        result = f.readline()
        assert result == original

# alias
spit = burp

# Generated at 2022-06-14 06:07:47.701551
# Unit test for function islurp
def test_islurp():
    result = list(islurp.islurp(os.path.join(os.path.dirname(__file__), 'test_bytes.txt')))
    assert result == ['Python3\n', 'JavaScript\n', 'Go']

# Generated at 2022-06-14 06:07:53.999829
# Unit test for function burp
def test_burp():
    filename = os.path.join(os.getcwd(), 'burp.txt')
    burp(filename, 'This is test')
    lines = islurp(filename, 'r')
    assert lines[0].strip() == 'This is test'
    try:
        os.remove(filename)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))

test_burp()

# Generated at 2022-06-14 06:08:02.687081
# Unit test for function islurp
def test_islurp():
    """Test islurp function."""
    import tempfile
    import os

    with tempfile.NamedTemporaryFile() as fh:
        filename = fh.name
        fh.write('hello\nworld\n')
        fh.flush()

        for line in islurp(filename):
            print('line: %s' % line)


if __name__ == '__main__':
    test_islurp()

# Generated at 2022-06-14 06:08:13.436101
# Unit test for function islurp
def test_islurp():
    assert list(islurp(__file__)) == list(islurp(__file__, iter_by=islurp.LINEMODE))
    assert list(islurp(__file__, iter_by=islurp.LINEMODE)) == open(__file__).readlines()
    assert list(islurp(__file__, iter_by=2048)) == open(__file__).read().split('\n')


# Generated at 2022-06-14 06:08:26.403857
# Unit test for function islurp
def test_islurp():

    # unit tests
    assert islurp.__doc__ is not None

    text = 'one\ntwo\nthree\nfour\nfive\nsix\nseven\neight\nnine\nten'
    data = ''.join([chr(x) for x in range(ord('a'), ord('z') + 1)])

    # slurp lines from text
    assert list(islurp(text.split('\n'))) == text.split('\n')
    assert list(islurp([text])) == text.split('\n')
    assert list(islurp((text,))) == text.split('\n')

    # slurp lines from data
    result = list(islurp(data))
    assert result == [i for i in data]

    # read lines

# Generated at 2022-06-14 06:08:32.612452
# Unit test for function islurp
def test_islurp():

    # Unit test for the LINEMODE
    # :param islurp: the filename, mode and iter_by
    # :return: True if the contents of the file is larger than 0 otherwise it returns false
    assert islurp("/usr/share/dict/words", 'r', LINEMODE), True


# Generated at 2022-06-14 06:08:38.055217
# Unit test for function burp
def test_burp():
    import tempfile

    textname = tempfile.mktemp()
    text = 'text to write'
    burp(textname, text)

    with open(textname, 'r') as fh:
        assert text == fh.read()
    os.remove(textname)



# Generated at 2022-06-14 06:08:41.852263
# Unit test for function burp
def test_burp():
    burp('test.txt', "hello world")
    assert slurp('test.txt', 'r')[0] == "hello world"
    os.remove('test.txt')

# Generated at 2022-06-14 06:08:43.964052
# Unit test for function islurp
def test_islurp():
	for i, line in enumerate(islurp(__file__)):
		assert line.startswith('#')


# Generated at 2022-06-14 06:08:54.611185
# Unit test for function burp
def test_burp():
    # file mode w
    burp('test.txt', 'Hello World!')
    assert(open('test.txt', 'r').read() == 'Hello World!')

    # file mode a
    burp('test.txt', 'Hello World!', mode='a')
    assert(open('test.txt', 'r').read() == 'Hello World!Hello World!')

    # delete file
    os.remove('test.txt')

    # stdout mode
    burp('-', 'Hello World!', allow_stdout=True)
    assert(sys.stdout.getvalue() == 'Hello World!')

test_burp()


# Generated at 2022-06-14 06:08:59.070462
# Unit test for function islurp
def test_islurp():
    import tempfile
    import shutil

    tmpdir = tempfile.mkdtemp()
    try:
        testfile = os.path.join(tmpdir, 'work.txt')
        burp(testfile, 'hello')
        burp(testfile, 'world')

        for line in slurp(testfile):
            assert line in ['h', 'el', 'l', 'o', '\n', 'w', 'or', 'ld', '\n']

    finally:
        shutil.rmtree(tmpdir)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

# Generated at 2022-06-14 06:09:05.737971
# Unit test for function burp
def test_burp():
    fname = "test_burp.txt"
    contents = "abcdefgh"
    burp(fname, contents)
    assert os.path.isfile(fname)
    lcont = slurp(fname)
    burp(fname, "")
    os.remove(fname)
    assert lcont.next() == contents


# Generated at 2022-06-14 06:09:16.715101
# Unit test for function burp
def test_burp():
    # Create a test file
    filename = 'test.txt'
    contents = 'abcdefg'
    expected = contents
    burp(filename, contents)
    try:
        # Check if the file exists
        assert os.path.exists(filename), "File " + filename + " doesn't exist!"
        # Check if the content is correct
        assert ''.join(islurp(filename)) == expected, "File content doesn't match, expected: " + expected + ", actual: " + ''.join(islurp(filename))
    finally:
        # Remove the test file
        os.remove(filename)


# Generated at 2022-06-14 06:09:30.582323
# Unit test for function burp
def test_burp():
    import tempfile
    f = tempfile.NamedTemporaryFile(delete=False)
    f.close()

    burp(f.name, "Hello World!")

    with open(f.name) as f:
        assert f.read() == "Hello World!"

    os.remove(f.name)
