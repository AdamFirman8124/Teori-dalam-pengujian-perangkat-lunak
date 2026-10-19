

# Generated at 2022-06-14 05:59:48.209233
# Unit test for function islurp
def test_islurp():

    # Passing in sys.stdin reads from stdin
    from io import StringIO
    old_stdin = sys.stdin
    sys.stdin = StringIO("hello world")
    assert list(islurp('-')) == ["hello world"]
    sys.stdin = old_stdin

    # Expanding user of file path works properly
    old_home = os.environ.get("HOME", "/home")
    os.environ["HOME"] = "/home/test"
    assert list(islurp("~/test")) == []
    os.environ["HOME"] = old_home

    # Behavior of islurp on non-existent file
    assert list(islurp("/file/does/not/exist")) == []

    # Reading an empty file gives an empty string

# Generated at 2022-06-14 06:00:01.193253
# Unit test for function burp
def test_burp():
    # Test if it can write to a file
    burp('test_file.txt', "Test string")
    with open('test_file.txt') as f:
        lines = f.readlines()
    assert lines[0] == "Test string", "burp can't write to a file!"
    os.remove('test_file.txt')

    # Test if it can write to stdout
    import sys
    saved_stdout = sys.stdout
    sys.stdout = open('test_file.txt', 'w')
    burp('-', "Test string")
    sys.stdout = saved_stdout
    with open('test_file.txt') as f:
        lines = f.readlines()
    assert lines[0] == "Test string", "burp can't write to stdout!"

# Generated at 2022-06-14 06:00:11.279626
# Unit test for function islurp
def test_islurp():
    import tempfile
    import shutil

    dirpath = tempfile.mkdtemp()

    filepath = os.path.join(dirpath, 'test1.txt')
    with open(filepath, 'w') as fh:
        fh.write('one line\nanother line\n')

    assert list(islurp(filepath)) == ['one line\n', 'another line\n']
    assert list(islurp(filepath, iter_by=3)) == ['one', ' ', 'lin', 'e\n', 'ano', 'the', 'r ', 'lin', 'e\n']

    shutil.rmtree(dirpath)

if __name__ == '__main__':
    test_islurp()

# Generated at 2022-06-14 06:00:23.181253
# Unit test for function islurp
def test_islurp():
    fp = "test.txt"
    # Create a test file:
    with open(fp, "w") as fh:
        fh.write("Line 1 Line 2\nLine 3 Line 4")
    # read the file
    ans = list(islurp(fp))
    assert ans == ["Line 1 Line 2\n", "Line 3 Line 4"]
    # read the file again, this time by chunks
    ans = list(islurp(fp, iter_by=3))
    assert ans == ["Lin", "e 1", " Li", "ne ", "2\n", "Lin", "e 3", " Li", "ne ", "4"]
    # Remove the test file:
    os.unlink(fp)



# Generated at 2022-06-14 06:00:36.968242
# Unit test for function islurp
def test_islurp():
    """
    test_islurp
    """
    import io

    assert list(islurp(io.StringIO("Hello"))) == ["Hello"]
    assert list(islurp(io.StringIO("Hello"), iter_by=3)) == ["Hel", "lo"]
    assert list(islurp(io.StringIO("Hello\nWorld"))) == ["Hello\n", "World"]

    fd, fname = tempfile.mkstemp(text=True)

# Generated at 2022-06-14 06:00:41.555238
# Unit test for function burp
def test_burp():
    filename = "sample.txt"
    contents = "The cat and the hat"
    burp(filename, contents)
    with open(filename, 'r') as fh:
        output = fh.read()
        assert output == contents, 'Wrong data in sample.txt'
        os.remove(filename)


# Generated at 2022-06-14 06:00:53.813259
# Unit test for function islurp
def test_islurp():
    # no file at path
    try:
        list(islurp('/tmp/does-not-exist'))
    except OSError as e:
        assert isinstance(e, OSError)
        assert e.errno == 2
        assert e.strerror == 'No such file or directory'

    # file exists and is readable
    assert 'line1' in (''.join(islurp('/tmp/testfile.txt'))).split('\n')
    assert 'line1' in (''.join(islurp('/tmp/testfile.txt', iter_by=1024))).split('\n')
    assert 'line1' in (''.join(islurp('/tmp/testfile.txt', iter_by='LINEMODE'))).split('\n')

    # test iter_by
   

# Generated at 2022-06-14 06:00:57.174444
# Unit test for function islurp
def test_islurp():
    data = list(islurp('test_file.txt'))
    assert len(data) == 3
    assert data[0] == 'This is test line 1.\n'
    assert data[1] == 'This is test line 2.\n'
    assert data[2] == 'This is test line 3.\n'


# Generated at 2022-06-14 06:01:02.559981
# Unit test for function islurp
def test_islurp():
    assert slurp('/etc/passwd', iter_by=LINEMODE) == islurp('/etc/passwd', iter_by=LINEMODE)

    assert slurp('/etc/passwd', iter_by=10000) == islurp('/etc/passwd', iter_by=10000)


# Generated at 2022-06-14 06:01:15.483151
# Unit test for function islurp
def test_islurp():
    """
    Unit test for function islurp
    """
    def read_expected(filename, mode='r', iter_by=LINEMODE, allow_stdin=True):
        """
        Read [expanded] `filename` and return the result.

        :param str filename: File path
        :param str mode: Use this mode to open `filename`, ala `r` for text (default), `rb` for binary, etc.
        :param int iter_by: Iterate by this many bytes at a time. Default is by line.
        :param bool allow_stdin: If Truthy and filename is `-`, read from `sys.stdin`.
        """
        expected = ''
        if filename == '-' and allow_stdin:
            expected = sys.stdin.read()

# Generated at 2022-06-14 06:01:25.185748
# Unit test for function islurp
def test_islurp():
    expected = ['a\n', 'b\n', 'c\n']
    result = [l for l in islurp('test_islurp.txt')]
    assert result == expected

    expected = ['a\n', 'b\n', 'c\n', '']
    result = [l for l in islurp('test_islurp.txt', iter_by=1)]
    assert result == expected

# Generated at 2022-06-14 06:01:32.773524
# Unit test for function islurp
def test_islurp():
    """
    Test function islurp.
    """
    # TODO: replace this with dict
    #  - or kwargs
    file_data = [
        '/etc/hosts',
        '/etc/passwd',
        '~/foobar',
        '-',
    ]
    for filename in file_data:
        for entry in islurp(filename):
            print(entry)

if __name__ == '__main__':
    test_islurp()

# Generated at 2022-06-14 06:01:35.239411
# Unit test for function islurp
def test_islurp():
    for line in islurp(__file__):
        assert 'def islurp' in line


# Generated at 2022-06-14 06:01:48.400582
# Unit test for function islurp
def test_islurp():
    input_filename = 'test/test_files.txt'
    output_filename = 'test/test_files_out.txt'
    lines = [
        'line 1',
        'line 2',
        'line 3'
    ]

    with open(input_filename, 'w') as fh:
        for line in lines:
            fh.write(line + '\n')

    # Test islurp with mode=TEXT (default)
    for idx, buf in enumerate(islurp(input_filename)):
        assert buf == lines[idx]

    # Test islurp with mode=TEXT, iter_by=LINEMODE (default)
    buf = ''

# Generated at 2022-06-14 06:01:54.915829
# Unit test for function burp
def test_burp():
    """
    Test function burp
    """
    filename = "test.txt"
    try:
        burp(filename, "Test text file")
        with open("test.txt", "r") as fh:
            assert fh.read() == "Test text file"
    finally:
        os.remove(filename)


# Generated at 2022-06-14 06:02:00.225473
# Unit test for function burp
def test_burp():
    filename = "test_burp.txt"
    contents = "contents to be written"
    burp(filename, contents)
    fileslurp = list(islurp(filename))
    assert fileslurp[0] == contents
    

# Generated at 2022-06-14 06:02:05.172354
# Unit test for function burp
def test_burp():
    contents = 'Hello World!'
    output = 'test_burp.txt'
    try:
        burp(output, contents)
        with open(output) as fh:
            s = fh.read()
        assert s == contents
    finally:
        os.remove(output)

# Generated at 2022-06-14 06:02:13.662419
# Unit test for function islurp
def test_islurp():
    cwd = os.getcwd()
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    with open('dummy.txt','w') as f:
        f.write('Foo\nBar')

    sl = list(islurp('dummy.txt'))
    assert sl == ['Foo\n', 'Bar']

    os.remove('dummy.txt')
    os.chdir(cwd)


# Generated at 2022-06-14 06:02:25.599603
# Unit test for function islurp
def test_islurp():
    from difflib import ndiff
    import tempfile

    tmp_file1 = tempfile.NamedTemporaryFile(delete=False)
    tmp_file1.write(b"line1\rline2\r\nline3\nline4\n\n")
    tmp_file1.close()
    assert [s.encode('ascii') for s in islurp(tmp_file1.name)] == \
                [b"line1\r\n", b"line2\r\n", b"line3\n", b"line4\n", b"\r\n", b"\r\n"]

# Generated at 2022-06-14 06:02:31.411152
# Unit test for function islurp
def test_islurp():

    for line in islurp('/etc/hosts', iter_by='LINEMODE'):
        if line.startswith('#'):
            continue

        try:
            host, ip = line.split()
        except ValueError:
            continue

        print(host, '::', ip)


# Generated at 2022-06-14 06:02:39.414517
# Unit test for function islurp
def test_islurp():
    assert list(islurp('test_islurp.py', 'rb')) == open('test_islurp.py', 'rb').read()
    assert list(islurp('/dev/zero', 'rb', 32)) == open('/dev/zero', 'rb').read(32)


# Generated at 2022-06-14 06:02:52.493133
# Unit test for function islurp
def test_islurp():
    assert list(islurp.islurp('/dev/urandom', 'rb', allow_stdin=False, expanduser=False, expandvars=False, iter_by=5)) == list(islurp.islurp('/dev/urandom', 'rb', allow_stdin=False, expanduser=False, expandvars=False, iter_by=5))
    assert list(islurp.islurp('/dev/urandom', 'rb', allow_stdin=False, expanduser=False, expandvars=False, iter_by=5)) != list(islurp.islurp('/dev/urandom', 'rb', allow_stdin=False, expanduser=False, expandvars=False, iter_by=6))

# Generated at 2022-06-14 06:02:58.796112
# Unit test for function islurp
def test_islurp():
    test_filename = 'test/slurp/islurp'
    test_content = "Testing islurp\n"

    burp(test_filename, test_content)
    slurp_content = ''

    for line in islurp(test_filename):
        slurp_content += line

    assert slurp_content == test_content

    os.remove(test_filename)


# Generated at 2022-06-14 06:03:07.413801
# Unit test for function islurp
def test_islurp():
    test_file = 'test.txt'
    test_string = 'This is a test\n'
    with open(test_file, 'w') as fd:
        fd.write(test_string)
    for line in islurp(test_file):
        assert line.rstrip('\n') == 'This is a test'
    os.remove(test_file)

if __name__ == '__main__':
    test_islurp()

# Generated at 2022-06-14 06:03:13.340795
# Unit test for function burp
def test_burp():
    import tempfile
    assert burp('-', 'test_burp', allow_stdout=False) == None
    temp = tempfile.NamedTemporaryFile(delete=False)
    name = temp.name
    temp.close()
    burp(name, 'burp')
    assert open(name).read() == 'burp'
    os.unlink(name)

# Unit tests for function islurp

# Generated at 2022-06-14 06:03:22.925347
# Unit test for function islurp
def test_islurp():
    with open('test_islurp', 'w') as f_out:
        f_out.write('123\n456\n')

    with open('test_islurp', 'r') as f_in:
        for line in f_in:
            print(line)

    for line in islurp('test_islurp'):
        print(line)

    os.remove('test_islurp')


if __name__ == '__main__':
    test_islurp()

# Generated at 2022-06-14 06:03:31.321542
# Unit test for function islurp
def test_islurp():
    assert list(islurp('-', allow_stdin=False)) == []

# Generated at 2022-06-14 06:03:43.496903
# Unit test for function islurp
def test_islurp():
    """
    Test function `islurp`
    """
    assert list(islurp(__file__))[0].startswith('# Unit test for function islurp')

    # Test with `allow_stdin=False`
    assert list(islurp('-', allow_stdin=False)) == []

    # Test reading file into memory using iter_by
    # FIXME What's the point of this block?
    buf = 'a' * 512

# Generated at 2022-06-14 06:03:57.324809
# Unit test for function islurp
def test_islurp():
    my_file = 'tests/test_file.txt'
    assert(list(islurp(my_file)) == ['this\n', 'is\n', 'a\n', 'test\n', 'file\n'])
    assert(list(islurp(my_file, iter_by='LINEMODE')) == ['this\n', 'is\n', 'a\n', 'test\n', 'file\n'])
    assert(list(islurp(my_file, iter_by=4)) == ['this', '\nis\n', 'a\n', 'test', '\nfil', 'e\n'])

# Generated at 2022-06-14 06:04:05.718224
# Unit test for function islurp
def test_islurp():
    # Check reading from stdin
    if os.name == 'posix':
        from .pexpect_utils import pexpect_run
        from .pexpect_utils import DEVNULL
        from .pexpect_utils import PEXPECT_TIMEOUT_1
        from .pexpect_utils import PEXPECT_TIMEOUT_5
        from .pexpect_utils import PEXPECT_TIMEOUT_60

        child = pexpect_run('echo this_is_stdin_text', stdout=DEVNULL, stderr=DEVNULL)
        child.expect(r'this_is_stdin_text\s+', timeout=PEXPECT_TIMEOUT_1)
        child.close()


# Generated at 2022-06-14 06:04:45.845639
# Unit test for function islurp
def test_islurp():
    print('=== test_islurp ===')
    import tempfile
    import random
    contents = '\n'.join('line', '# ', '# ', 'line line' * 100)
    with tempfile.NamedTemporaryFile('w', delete=False) as fh_tmp:
        fh_tmp.write(contents)

    assert list(islurp(filename=fh_tmp.name, expanduser=False, expandvars=False)) == contents.splitlines(True)
    assert list(islurp(fh_tmp.name, iter_by=4)) == contents[4:4].splitlines(True)
    assert list(islurp(fh_tmp.name, iter_by=1)) == list(islurp(fh_tmp.name))


# Generated at 2022-06-14 06:04:54.455126
# Unit test for function islurp
def test_islurp():
    import os
    from io import StringIO
    from tempfile import NamedTemporaryFile
    from tpk.util import islurp

    def _count(iterable):
        n = 0
        for _ in iterable:
            n += 1
        return n

    # Test empty file
    f = NamedTemporaryFile(delete=False)
    expected = 0
    assert _count(islurp(f.name)) == expected
    os.remove(f.name)

    # Test small file
    f = NamedTemporaryFile(mode='w', encoding='utf-8', delete=False)
    expected = 3
    f.write('\n'.join(['1', '2', '3']))
    f.close()
    assert _count(islurp(f.name)) == expected

# Generated at 2022-06-14 06:05:01.966680
# Unit test for function burp
def test_burp():
    test_file_path = os.path.dirname(os.path.realpath(__file__)) + "/test_file1.txt"
    burp(test_file_path, "This is a test file with contents to test burp function\n")
    assert(slurp(test_file_path).next() == "This is a test file with contents to test burp function\n")
    os.remove(test_file_path)

# Generated at 2022-06-14 06:05:04.482754
# Unit test for function islurp
def test_islurp():
    for line in islurp(__file__):
        print(line)


# Generated at 2022-06-14 06:05:07.998461
# Unit test for function burp
def test_burp():
    fname="__test_burp.txt"
    contents="burp"
    burp(fname,contents)
    with open(fname,"r") as f:
        assert f.read() == contents
    os.remove(fname)

# Generated at 2022-06-14 06:05:21.800019
# Unit test for function islurp
def test_islurp():
    filename = 'test_file.txt'

    # Test line by line read
    fp = open(filename, 'w')
    fp.write('Test 1\nTest 2\nTest 3')
    fp.close()
    test_lines = [line for line in islurp(filename)]
    assert test_lines == ['Test 1\n', 'Test 2\n', 'Test 3']

    # Test reading in chunks of 5 bytes
    fp = open(filename, 'w')
    fp.write('Test 1\nTest 2\nTest 3')
    fp.close()
    test_lines = [line for line in islurp(filename, iter_by=5)]
    assert test_lines == ['Test ', '1\nTe', 'st 2\n', 'Test ', '3']

    # Test

# Generated at 2022-06-14 06:05:29.937587
# Unit test for function islurp
def test_islurp():
    from ..test_util import captured_output

    with captured_output() as (out, err):
        print('test_islurp:')

        lines = list(islurp('LICENSE'))
        print('num lines', len(lines))
        print('lines:', lines[:5])  # first 5 lines

        chunks = list(islurp('LICENSE', iter_by=512))
        print('num chunks', len(chunks))
        print('chunks:', chunks[:5])

    return True



# Generated at 2022-06-14 06:05:41.257653
# Unit test for function islurp
def test_islurp():
    from StringIO import StringIO
    from tempfile import NamedTemporaryFile

    with open('/etc/hosts') as fh:
        contents = fh.read()

    # read from stdin
    with NamedTemporaryFile() as tmp:
        tmp.write(contents)
        tmp.flush()
        sys.stdin = open(tmp.name)

        for line in islurp(sys.stdin):
            assert line

        for line in islurp('-'):
            assert line

    # read from real file
    with NamedTemporaryFile() as tmp:
        tmp.write(contents)
        tmp.flush()

        for line in islurp(tmp.name):
            assert line

    # read from file-like object

# Generated at 2022-06-14 06:05:45.623759
# Unit test for function islurp
def test_islurp():
    result = []
    for line in islurp('files.py'):
        result.append(line)
    assert len(result) > 0


# Generated at 2022-06-14 06:05:49.023058
# Unit test for function burp
def test_burp():
    os.mkdir('tmp')
    burp('tmp/test.txt', 'hello world')
    assert os.path.exists('tmp/test.txt')



# Generated at 2022-06-14 06:06:55.854103
# Unit test for function islurp
def test_islurp():
    from pathlib import Path
    from io import BytesIO
    import tempfile

    assert 'hi' == slurp(BytesIO(b'hi')).__next__()
    with tempfile.NamedTemporaryFile() as tf:
        tf.write(b'h\ni')
        tf.flush()

        assert 'h\ni' == slurp(tf.name).__next__()
        assert 'hi' == slurp(tf.name, iter_by=2).__next__()
        assert 'hi' == slurp(tf.name, iter_by=2).__next__() + slurp(tf.name, iter_by=2).__next__()
        assert 'h' == slurp(tf.name, iter_by=1).__next__()

# Generated at 2022-06-14 06:07:02.583416
# Unit test for function islurp
def test_islurp():
    txt = ''
    try:
        for seq in islurp('tests/resources/testfile1.txt'):
            txt += seq
        assert txt == 'This is a test file\nThis is the second line\nAnd the third\n'
        print(txt)
    except Exception as e:
        raise e


if __name__ == '__main__':
    test_islurp()

# Generated at 2022-06-14 06:07:07.748906
# Unit test for function islurp
def test_islurp():
    print("Test islurp()")
    for ln in islurp("file_utils.py", iter_by=islurp.LINEMODE, allow_stdin=True):
        if ln.startswith("def test"):
            print("line is: ", ln)

# Generated at 2022-06-14 06:07:20.925180
# Unit test for function islurp
def test_islurp():
    import io
    import StringIO
    import tempfile
    from contextlib import contextmanager

    # Test stdin support
    @contextmanager
    def stdin(contents):
        old_stdin = sys.stdin
        sys.stdin = StringIO.StringIO(contents)
        yield
        sys.stdin = old_stdin

    # Test binary mode
    @contextmanager
    def binary_fd(contents):
        fd = tempfile.mkstemp()
        os.write(fd[0], contents)
        os.close(fd[0])

        yield fd[1]

        os.unlink(fd[1])

    # Test other modes
    @contextmanager
    def text_fd(contents):
        fd = tempfile.mkstemp()

# Generated at 2022-06-14 06:07:27.916964
# Unit test for function burp
def test_burp():
    # Test a simple write
    filename = 'test.txt'

    burp(filename, 'test')
    with open(filename, 'r') as fh:
        assert fh.read().strip() == 'test'
    os.remove(filename)

    # Test a write to stdout
    burp('-', 'test', allow_stdout=True)

    # Test appending
    burp(filename, 'test', mode='a')
    with open(filename, 'r') as fh:
        assert fh.read().strip() == 'test'
    os.remove(filename)


# Generated at 2022-06-14 06:07:34.385181
# Unit test for function burp
def test_burp():
    fname = 'files-test.txt'
    test = 'Hello World!\n'
    burp(fname, test)
    result = slurp(fname, 'r')
    os.remove(fname)

    assert result.__next__() == test

burp.test = test_burp



# Generated at 2022-06-14 06:07:38.225834
# Unit test for function islurp
def test_islurp():
    result = islurp('tests/test.txt', mode='r', iter_by=LINEMODE, allow_stdin=True, expanduser=True, expandvars=True)
    assert type(result) is type(islurp)
    assert list(result)[-1] == '9\n'

# Generated at 2022-06-14 06:07:52.182252
# Unit test for function islurp
def test_islurp():
    """
    Test islurp()
    """
    # Test default mode
    contents = ''.join(islurp('samples/test_islurp'))
    assert contents == 'line1\nline2\n'

    # Test read modes
    contents = ''.join(islurp('samples/test_islurp_binary', mode='rb'))
    assert contents == '\x19\x80\x98'

    # Test stdin
    contents = ''.join(islurp('-', allow_stdin=True))
    assert contents == 'line1\nline2\n'

    # Test line mode
    contents = [line for line in islurp('samples/test_islurp')]
    assert contents == ['line1\n', 'line2\n']

    # Test

# Generated at 2022-06-14 06:08:01.333102
# Unit test for function islurp
def test_islurp():
    if __name__ == '__main__':
        expected = "This is a test\n"
        test_file = "test.txt"
        with open(test_file, "w") as f:
            f.write(expected)
        actual = [line for line in islurp(test_file)]
        # Remove the test file
        os.remove(test_file)
        assert actual == [expected]


# Generated at 2022-06-14 06:08:11.138835
# Unit test for function islurp