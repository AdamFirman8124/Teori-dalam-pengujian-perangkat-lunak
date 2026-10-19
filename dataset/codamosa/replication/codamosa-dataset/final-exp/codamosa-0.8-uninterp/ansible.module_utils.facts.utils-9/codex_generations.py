

# Generated at 2022-06-13 03:43:56.994602
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content(path='/dev/null') is None
    assert get_file_content(path='/dev/null', strip=False) is None
    assert get_file_content(path='/dev/null', strip=False, default='ok') == 'ok'
    assert get_file_content(path='/dev/null', strip=True, default='ok') == 'ok'

    with open('/tmp/test_get_file_content.txt', 'w') as fd:
        fd.write('abc')
    assert get_file_content(path='/tmp/test_get_file_content.txt') == 'abc'
    assert get_file_content(path='/tmp/test_get_file_content.txt', strip=False) == 'abc'



# Generated at 2022-06-13 03:44:06.150392
# Unit test for function get_file_content
def test_get_file_content():
    '''
    Test get_file_content()

    :returns: True on success, False on failure
    '''
    # Create a file with content
    file_path = '/tmp/test_file'
    file_content = 'test file content'
    f = open(file_path, 'w+')
    f.write(file_content)
    f.close()

    # Test: File exists and content should be returned
    result = get_file_content(file_path)
    if result != file_content:
        os.remove(file_path)
        return False

    # Test: File exists and content should be returned, but no stripping
    result = get_file_content(file_path, strip=False)
    if result != ' ' + file_content + ' ':
        os.remove(file_path)

# Generated at 2022-06-13 03:44:13.372279
# Unit test for function get_file_lines
def test_get_file_lines():
    '''
    Test for the function which returns file lines
    '''
    path = "/tmp/test_file"
    content = "This is the first line\nThis is the second line\nThis is the third line"

    with open(path, "w") as file:
        file.write(content)

    lines = get_file_lines(path)

    os.remove(path)

    assert lines == ['This is the first line', 'This is the second line', 'This is the third line']

# Generated at 2022-06-13 03:44:22.732486
# Unit test for function get_file_lines
def test_get_file_lines():
    s = """line1
line2
line3"""
    fd, path = tempfile.mkstemp()
    try:
        with os.fdopen(fd, 'w') as fh:
            fh.write(s)
        assert get_file_lines(path) == ['line1', 'line2', 'line3']
        assert get_file_lines(path, strip=False) == ['line1\n', 'line2\n', 'line3']
        assert get_file_lines(path, line_sep='\n') == ['line1', 'line2', 'line3']
        assert get_file_lines(path, line_sep='\n\n') == ['line1\nline2\nline3']
    finally:
        os.unlink(path)

# Generated at 2022-06-13 03:44:31.087566
# Unit test for function get_file_lines
def test_get_file_lines():
    import tempfile
    content = '''
  1  foo
  5  bar
  9  baz
'''
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file_name = temp_file.name
    temp_file.write(content)
    temp_file.close()

    test_line_sep = '  '
    test_lines = get_file_lines(temp_file_name, line_sep=test_line_sep)
    assert test_lines == ['1 foo', '5 bar', '9 baz']



# Generated at 2022-06-13 03:44:41.729790
# Unit test for function get_file_lines
def test_get_file_lines():
    assert get_file_lines('/nonexistent') == []
    assert get_file_lines('/etc/mtab') == get_file_lines('/etc/mtab', strip=False).strip().split('\n')
    assert get_file_lines('/etc/mtab', line_sep='::') == get_file_lines('/etc/mtab', strip=False).strip().split('::')
    assert get_file_lines('/etc/mtab', line_sep=None) == get_file_lines('/etc/mtab', line_sep='\n')
    assert get_file_lines('/etc/mtab', line_sep='\n\n') == get_file_lines('/etc/mtab', line_sep='\n')

# Generated at 2022-06-13 03:44:46.809138
# Unit test for function get_file_lines
def test_get_file_lines():
    input_file = """this is 
    a multiline
    file
    """
    ret = get_file_lines(input_file)
    expected_lines = ['this is', 'a multiline', 'file']
    assert ret == expected_lines
    input_file = "   this is a single line file    "
    ret = get_file_lines(input_file)
    assert ret == ["this is a single line file"]

# Generated at 2022-06-13 03:44:57.913953
# Unit test for function get_file_lines
def test_get_file_lines():
    data = '''
    first_line
    second_line


    '''

    # No strip
    lines = get_file_lines('')
    assert [] == lines

    # strip
    lines = get_file_lines('', strip=False)
    assert [] == lines

    # line_sep
    lines = get_file_lines('', line_sep='_', strip=False)
    assert [] == lines
    lines = get_file_lines('', line_sep='first', strip=False)
    assert [] == lines
    lines = get_file_lines('', line_sep='_')
    assert [] == lines
    lines = get_file_lines('', line_sep='first')
    assert [] == lines

    # strip, lines

# Generated at 2022-06-13 03:45:08.871069
# Unit test for function get_file_lines
def test_get_file_lines():
    assert get_file_lines('/proc/version', strip=False) == ['Linux version 2.6.32-279.22.1.el6.x86_64 (mockbuild@c6b8.bsys.dev.centos.org) (gcc version 4.4.6 20120305 (Red Hat 4.4.6-4) (GCC) ) #1 SMP Tue Jun 18 14:21:43 UTC 2013']

# Generated at 2022-06-13 03:45:20.179086
# Unit test for function get_file_content
def test_get_file_content():
    retval = get_file_content('/etc/shadow', default='foo')
    assert retval != 'foo'

    retval = get_file_content('/etc/shadow', default='foo', strip=False)
    assert retval != 'foo'

    retval = get_file_content('/etc/shadow', default='foo', strip=True)
    assert retval != 'foo'

    retval = get_file_content('/tmp/doesnotexists', default='foo')
    assert retval == 'foo'

    retval = get_file_content('/tmp/doesnotexists', default='foo', strip=False)
    assert retval == 'foo'

    retval = get_file_content('/tmp/doesnotexists', default='foo', strip=True)
    assert retval == 'foo'

# Generated at 2022-06-13 03:45:25.781298
# Unit test for function get_file_content
def test_get_file_content():
    my_file = open('/tmp/my_file', 'w')
    my_file.write('this is a test')
    my_file.close()

    result = get_file_content('/tmp/my_file')
    assert result == 'this is a test'

# Generated at 2022-06-13 03:45:27.901732
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content('/etc/passwd', default='This is a test') == 'This is a test'

# Generated at 2022-06-13 03:45:30.644637
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content('/etc/group', default='default') != 'default'
    assert get_file_content('/etc/invalid_file', default='default') == 'default'



# Generated at 2022-06-13 03:45:37.777800
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content("/etc/passwd", default=None) is not None
    assert get_file_content("/etc/passwd", default=True) is not True
    assert get_file_content("/etc/passwd", default="foo") != "foo"
    assert get_file_content("/etc/passwd", strip=False) is not None
    assert get_file_content("/does/not/exist", default=None) is None
    assert get_file_content("/etc/passwd", default=None) == get_file_content("/etc/passwd", default="foo")
    assert get_file_content("/etc/passwd", default=None) != get_file_content("/etc/passwd", strip=False, default="foo")

# Generated at 2022-06-13 03:45:43.545535
# Unit test for function get_file_content
def test_get_file_content():
    import tempfile
    import tempfile
    (fd, path) = tempfile.mkstemp()
    test_data = "Test data"
    os.write(fd, test_data)
    os.close(fd)
    assert test_data == get_file_content(path)
    os.unlink(path)
    assert None == get_file_content(path)

# Generated at 2022-06-13 03:45:51.981838
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content(os.path.join(os.path.dirname(__file__), 'file1.txt')) == 'Hello world!\n'
    assert get_file_content(os.path.join(os.path.dirname(__file__), 'file1.txt'), default='Empty') == 'Hello world!\n'
    assert get_file_content(os.path.join(os.path.dirname(__file__), 'file1.txt'), default='Empty', strip=False) == 'Hello world!\n'
    assert get_file_content(os.path.join(os.path.dirname(__file__), 'file2.txt'), default='Empty') == 'Empty'

# Generated at 2022-06-13 03:45:55.412044
# Unit test for function get_file_content
def test_get_file_content():
    # get_file_content() should return a string
    assert isinstance(get_file_content("/etc/location"), str)
    # get_file_content() with default return the default value
    assert get_file_content("/etc/path/does/not/exist", default="hello") == "hello"


# Generated at 2022-06-13 03:45:57.190170
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content('/etc/ansible/hosts')



# Generated at 2022-06-13 03:46:06.612218
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content('test.txt', default='') == ''
    if os.path.exists('test.txt'):
        os.remove('test.txt')
    assert get_file_content('test.txt', default='default') == 'default'
    with open('test.txt', 'w') as f:
        f.write('123\n')
    assert get_file_content('test.txt', default='') == '123\n'
    assert get_file_content('test.txt', strip=True, default='') == '123'
    if os.path.exists('test.txt'):
        os.remove('test.txt')

# Generated at 2022-06-13 03:46:08.860122
# Unit test for function get_file_content
def test_get_file_content():
    path = '/proc/cpuinfo'
    assert get_file_content(path) == get_file_lines(path)


# Generated at 2022-06-13 03:46:21.251579
# Unit test for function get_file_content
def test_get_file_content():
    import tempfile
    ## positive testing
    (fd, tmp_file_path) = tempfile.mkstemp()
    with os.fdopen(fd, 'w') as tmp_file:
        tmp_file.write('foobar')

    assert get_file_content(tmp_file_path) == 'foobar'
    assert get_file_content(tmp_file_path, 'default') == 'foobar'
    assert get_file_content(tmp_file_path, 'default', False) == 'foobar'
    assert get_file_content(tmp_file_path, 'default', True) == 'foobar'
    assert get_file_content(tmp_file_path, strip=True) == 'foobar'

    ## negative testing
    assert get_file_content('/does/not/exist') == None
   

# Generated at 2022-06-13 03:46:25.898623
# Unit test for function get_file_content
def test_get_file_content():
    path = '/tmp/test.txt'
    content = 'Test File Content'

    get_file_content(path, True)

    with open(path, 'w') as f:
        f.write(content)

    assert get_file_content(path, False) == content

    # Test default
    assert get_file_content('not a real file', 'A default value') == 'A default value'

# Generated at 2022-06-13 03:46:27.363613
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content(os.devnull, default='default_value') == 'default_value'

# Generated at 2022-06-13 03:46:34.729476
# Unit test for function get_file_content
def test_get_file_content():
    # Test with a file that doesn't exist
    result = get_file_content('/tmp/blah', default=False)
    assert result is False, 'Result should be False'

    # Create a file with some content
    import tempfile
    with tempfile.NamedTemporaryFile('w') as test_file:
        test_file.write('this is some data')
        test_file.flush()

        # Test with a file that exists and is readable
        result = get_file_content(test_file.name)
        assert result == 'this is some data', 't1'

        # Test a file that exists, but is not readable
        os.chmod(test_file.name, 0)
        result = get_file_content(test_file.name, default=False)
        assert result is False, 't2'

# Generated at 2022-06-13 03:46:44.251691
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content(__file__, default='', strip=False) == open(__file__).read()
    assert get_file_content(__file__, default='', strip=True) == open(__file__).read().strip()
    assert get_file_content('/tmp/does_not_exist', default='', strip=False) == ''
    assert get_file_content('/tmp/does_not_exist', default='', strip=True) == ''
    assert get_file_content('/tmp/does_not_exist', default='test', strip=False) == 'test'
    assert get_file_content('/tmp/does_not_exist', default='test', strip=True) == 'test'

# Generated at 2022-06-13 03:46:48.827171
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content('/etc/resolv.conf', strip=True)
    assert not get_file_content('/etc/doesnt_exist')



# Generated at 2022-06-13 03:46:55.849366
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content('/dev/null', default=123) == 123
    assert get_file_content('/dev/null') == ''
    assert get_file_content('/dev/null', strip=False) == ''
    # check we get the default as a string, not int/bool
    assert not get_file_content('/not/a/file', default=0) == 0
    # check we get the default as a string, not a list
    assert not get_file_content('/not/a/file', default=[]) == []

# Generated at 2022-06-13 03:47:04.177155
# Unit test for function get_file_content
def test_get_file_content():
    print("Testing get_file_content")
    # Create a test file with the following content:
    #
    #   One
    #   Two
    #   Three
    #
    with open("/tmp/ansible_test_file", "w") as test_file:
        test_file.write("One\n")
        test_file.write("Two\n")
        test_file.write("Three\n")

    # Test 1 : Test that we can read the file, and that we get the same
    #          content we put in the file.
    #
    valid_data = "One\nTwo\nThree\n"
    data = get_file_content("/tmp/ansible_test_file")
    assert(data == valid_data)

    # Test 2 : Test that we can read the file without the trailing

# Generated at 2022-06-13 03:47:12.963396
# Unit test for function get_file_content
def test_get_file_content():
    test_file = 'tests/files/get_file_content_test'
    test_strip = [True, False]
    test_default = [None, 'test_default']
    for strip in test_strip:
        for default in test_default:
            test_result = get_file_content(test_file, default=default, strip=strip)
            if strip and test_result != '' and default != test_result:
                assert False, "get_file_content failed to strip whitespace"
            if (not strip) and (test_result == '' and (not default)):
                assert False, "get_file_content failed to not strip whitespace"
            if test_result == '' and default:
                if test_result != default:
                    assert False, "get_file_content failed to return default"

# Generated at 2022-06-13 03:47:21.915907
# Unit test for function get_file_content
def test_get_file_content():
    test_file_path = "./test_file"
    test_file_path2 = "./test_file2"
    test_file_path3 = "./test_file3"
    test_file_path4 = "./test_file4"

# Generated at 2022-06-13 03:47:33.329422
# Unit test for function get_file_content
def test_get_file_content():
    test_file_path = "/tmp/test_mountinfo"

# Generated at 2022-06-13 03:47:41.109735
# Unit test for function get_file_content
def test_get_file_content():
    os.environ['test_target'] = 'test_content'
    result = get_file_content(os.environ['test_target'], default=None)
    assert result == 'test_content', \
           'Test get_file_content() with file containing string'
    result = get_file_content(os.environ['test_target'], default=None, strip=False)
    assert result == 'test_content\n', \
           'Test get_file_content() with file containing string and strip=False'
    result = get_file_content(os.environ['test_target'], default='default')
    assert result == 'test_content', \
           'Test get_file_content() with file containing string and default'

# Generated at 2022-06-13 03:47:46.238406
# Unit test for function get_file_content
def test_get_file_content():
    '''
        Unit test for function get_file_content
    '''
    import tempfile
    import shutil
    tmpdir = tempfile.mkdtemp()
    tmpfile = tempfile.mkstemp(dir=tmpdir)
    content = 'This is a temporary file'
    os.write(tmpfile[0], content)
    os.close(tmpfile[0])
    try:
        assert get_file_content(tmpfile[1]) == content
        assert get_file_content(tmpfile[1], default='default') == content
        assert get_file_content(os.path.join(tmpdir, 'temp_file'), default='default') == 'default'
        assert get_file_content(os.path.join(tmpdir, 'temp_file')) == None
    finally:
        shutil.r

# Generated at 2022-06-13 03:47:52.188171
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content('/etc/hosts', default='foo') != 'foo'
    assert get_file_content('/etc/foo', default='foo') == 'foo'
    assert get_file_content('/etc/hosts', default='foo', strip=False) != 'foo'
    assert get_file_content('/etc/foo', default='foo', strip=False) == 'foo'


# Generated at 2022-06-13 03:47:55.643905
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content('/etc/shadow', 'does_not_exist') == 'does_not_exist'
    assert get_file_content('/etc/passwd', None, False) is not None
    assert get_file_content('/etc/passwd', None, True) is not None


# Generated at 2022-06-13 03:48:03.020514
# Unit test for function get_file_content
def test_get_file_content():
    fd = open('/tmp/test_file', 'w')
    fd.write('# Hello\nA B C D\n')
    fd.close()

    assert get_file_content('/tmp/test_file', strip=True, default='') == 'A B C D'

    fd = open('/tmp/test_file', 'w')
    fd.write('\n')
    fd.close()
    assert get_file_content('/tmp/test_file', strip=True, default='') == ''

    fd = open('/tmp/test_file', 'w')
    fd.write('# Hello\n\n')
    fd.close()
    assert get_file_content('/tmp/test_file', strip=True, default='') == ''

    f

# Generated at 2022-06-13 03:48:08.729630
# Unit test for function get_file_content
def test_get_file_content():
    # Testing reading file with data
    assert get_file_content('/etc/hostname', default='test') == 'test'
    # Testing reading file with data and stripping whitespace
    assert get_file_content('/etc/hostname') == 'test'
    # Testing reading file without data
    assert get_file_content('/etc/hostname', default=None) == None

# Generated at 2022-06-13 03:48:10.538357
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content("/bin/sh") == "/bin/sh\n"

# Generated at 2022-06-13 03:48:12.205077
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content('/var/log/messages') is None
    assert get_file_content('/var/log/messages', default="File not found") == "File not found"
    assert get_file_content(__file__, strip=False) is not None


# Generated at 2022-06-13 03:48:20.059800
# Unit test for function get_file_content
def test_get_file_content():
    path='test_file'
    default='dummy'
    strip=True


# Generated at 2022-06-13 03:48:26.123297
# Unit test for function get_file_content
def test_get_file_content():
    '''
    This function unit test the get_file_content function
    '''
    import tempfile
    tmp = tempfile.NamedTemporaryFile()
    tmp.write("This is a test")

    data = get_file_content(tmp.name)
    assert data == "This is a test"
    data = get_file_content(tmp.name, default="Default")
    assert data == "This is a test"

    # Test strip
    tmp.write("\ntest\n")
    data = get_file_content(tmp.name, default="Default", strip=False)
    assert data == "\ntest\n"
    data = get_file_content(tmp.name, default="Default")
    assert data == "test"

    # Test default
    tmp.close()
    data = get_file_content

# Generated at 2022-06-13 03:48:30.960704
# Unit test for function get_file_content
def test_get_file_content():
    f = os.tempnam()
    with open(f, 'w') as fp:
        fp.write('hello world\n')
    assert get_file_content(f) == 'hello world'
    os.remove(f)

    # test default
    assert get_file_content('/path/to/nowhere', default='default') == 'default'

# Generated at 2022-06-13 03:48:38.044773
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content('/etc/resolv.conf') == get_file_content('/etc/resolv.conf', default='could not read!')
    assert get_file_content('/etc/resolv.conf', strip=False) == get_file_content('/etc/resolv.conf', strip=False)
    assert get_file_content('/etc/resolv.conf', strip=False, default='could not read!') == 'could not read!'
    assert get_file_content('/does/not/exist', strip=False, default='could not read!') == 'could not read!'

# Generated at 2022-06-13 03:48:43.954802
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content("/proc/1/cmdline", strip=False) == b"systemd\0-switched-root\0-quiet\0"
    assert get_file_content("/proc/1/cmdline", strip=True) == "systemd-switched-root-quiet"
    assert get_file_content("/proc/1/cmdline", strip=True, default='') == "systemd-switched-root-quiet"
    assert get_file_content("/proc/1/cmdline", strip=False, default='') == b"systemd\0-switched-root\0-quiet\0"
    assert get_file_content("/proc/1/cmdline", default="ok") == "systemd-switched-root-quiet"

# Generated at 2022-06-13 03:48:46.222609
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content('/etc/passwd', 'default_value') == 'default_value'



# Generated at 2022-06-13 03:48:53.468800
# Unit test for function get_file_content
def test_get_file_content():
    ''' test for file_content_exists '''
    assert get_file_content('/bin/ls') is not None
    assert get_file_content('/bin/ls', default="None") == "None"
    assert get_file_content('/bin/ls', default="None", strip=False) is not None
    assert get_file_content('/bin/ls', default="None", strip=False) == "None" if get_file_content('/bin/ls', default="None", strip=False) != None else True


# Generated at 2022-06-13 03:49:02.773799
# Unit test for function get_file_content
def test_get_file_content():

    return_values = {
        'SuccessFile': 'success',
        'NoFile': None,
        'NonReadableFile': None
    }

    def _no_file_side_effect(path, default=None, strip=True):
        if path == '/tmp/UnitTestNoFile':
            return return_values['NoFile']
        else:
            return return_values[path.split('/')[-1]]

    def _non_readable_file_side_effect(path, default=None, strip=True):
        if path == '/tmp/UnitTestNonReadableFile':
            return return_values['NonReadableFile']
        else:
            return return_values[path.split('/')[-1]]

    # test a file that should be read successfully

# Generated at 2022-06-13 03:49:06.427569
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content('/dev/null') == ''
    assert get_file_content('/dev/null', strip=False) == ''
    assert get_file_content('/dev/null', ['foo', 'bar']) == []
    assert get_file_content('/dev/null', default=False) is False
    assert get_file_content('/dev/null', default=None) is None



# Generated at 2022-06-13 03:49:08.556456
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content('/dev/null') == ''
    assert get_file_content('/dev/null', strip=False) == ''
    assert get_file_content('/dev/null', default=False) is False


# Generated at 2022-06-13 03:49:10.109404
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content('/etc/ssh/sshd_config') == ""

# Generated at 2022-06-13 03:49:13.612379
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content(__file__, default='default') != 'default'

# Generated at 2022-06-13 03:49:22.209197
# Unit test for function get_file_content
def test_get_file_content():
    '''
        test function get_file_content
    '''
    assert get_file_content('/sys/kernel/mm/transparent_hugepage/enabled') == 'always madvise [never]'
    assert get_file_content('/sys/kernel/mm/transparent_hugepage/enabled', default='defaulted') == 'always madvise [never]'
    assert get_file_content('/sys/kernel/mm/transparent_hugepage/enabled', default='null', strip=False) == 'always madvise [never]\n'
    assert get_file_content('/no/such/file', default='null') is None

# Generated at 2022-06-13 03:49:30.337119
# Unit test for function get_file_content
def test_get_file_content():
    def mock_open(path, *args):
        try:
            if path.startswith('test_file'):
                return open(os.path.join(os.path.dirname(__file__), 'test_data', path), *args)
            else:
                # default to normal `open` behaviour
                return __builtin__.open(path, *args)
        except IOError as e:
            raise IOError('[Errno {}] '.format(e.errno) + e.message)

    # Monkeypatch `open`
    global __builtin__
    try:
        __builtin__ = __builtins__
    except NameError:  # pragma: no cover
        pass  # py3
    __builtin__.open = mock_open

    # Test with nonexistent file
    nonexistent_file = get

# Generated at 2022-06-13 03:49:35.527486
# Unit test for function get_file_content
def test_get_file_content():

    actual = get_file_content(os.path.join(os.path.dirname(__file__), 'test_file'), default='default')
    print('Actual: ' + actual)
    assert actual == 'test'

    actual = get_file_content(os.path.join(os.path.dirname(__file__), 'test_file'), default='default', strip=False)
    print('Actual: ' + actual)
    assert actual == 'test\n'

    actual = get_file_content(os.path.join(os.path.dirname(__file__), 'test_file_noperms'), default='default')
    print('Actual: ' + actual)
    assert actual == 'default'

# Generated at 2022-06-13 03:49:42.384119
# Unit test for function get_file_content
def test_get_file_content():
    # test with file full of spaces
    test_file_path = '/tmp/test_file'
    test_spaces_in_file = 100
    with open(test_file_path, "w") as test_file:
        test_file.write(" " * test_spaces_in_file)
    assert len(get_file_content(test_file_path)) == test_spaces_in_file
    os.remove(test_file_path)

    # test with file full of new lines
    test_file_path = '/tmp/test_file'
    test_lines_in_file = 100
    with open(test_file_path, "w") as test_file:
        test_file.write("\n" * test_lines_in_file)

# Generated at 2022-06-13 03:49:45.807745
# Unit test for function get_file_content
def test_get_file_content():
    file_contents = get_file_content("/etc/passwd", "")

    assert len(file_contents) > 10000
    assert file_contents.startswith('root')
    assert os.path.exists("/etc/passwd")



# Generated at 2022-06-13 03:49:55.614520
# Unit test for function get_file_content
def test_get_file_content():
    class UnitTestException(Exception):
        pass

    path = "/proc/cpuinfo"
    assert get_file_content(path=path, strip=False, default="") != ""
    assert get_file_content(path=path, strip=False, default="") != None
    assert get_file_content(path=path, strip=True, default="") != ""
    assert get_file_content(path=path, strip=True, default="") != None
    assert get_file_content(path="/nonsense/nonsense", strip=True, default="") == ""
    assert get_file_content(path="/nonsense/nonsense", strip=True, default="") != None
    assert get_file_content(path="/nonsense/nonsense", strip=True) == None

# Generated at 2022-06-13 03:50:02.599199
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content('/etc/passwd', default='') != ''
    assert get_file_content('/etc/passwd', default='') == get_file_content('/etc/passwd', default='')
    assert get_file_content('/etc/passwd', default='') == get_file_content('/etc/passwd', default='')
    assert get_file_content('/test/test/test/test', default='testdddd') == 'testdddd'
    assert get_file_content('/test/test/test/test', default='testdddd', strip=False) == 'testdddd'
    assert get_file_content('/test/test/test/test', default='testdddd') == 'testdddd'

# Generated at 2022-06-13 03:50:05.267579
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content('/dev/null') == ''
    assert get_file_content('/tmp/doesnotexist') == None
    assert get_file_content('/tmp/doesnotexist', 'foo') == 'foo'

# Generated at 2022-06-13 03:50:12.368342
# Unit test for function get_file_content
def test_get_file_content():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec=dict(
        path=dict(required=True, type='str'),
        strip=dict(default=True, type='bool')
    ))
    path = module.params['path']
    strip = module.params['strip']

    content = get_file_content(path, strip=strip)
    module.exit_json(changed=False, content=content)



# Generated at 2022-06-13 03:50:18.497532
# Unit test for function get_file_content
def test_get_file_content():
    test_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'unit', 'files', 'test_file.txt')
    assert get_file_content(test_file) == 'this is a test file\nthis is another line'
    assert get_file_content('/i/do/not/exist/file', 'default') == 'default'

# Generated at 2022-06-13 03:50:21.693953
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content('/etc/fstab', default='some non-defined value', strip=True) is not 'some non-defined value'
    assert get_file_content('/etc/nonexistentfile', default='some non-defined value', strip=True) is 'some non-defined value'
    assert get_file_content('/etc/hosts', strip=False).endswith('\n')
    assert get_file_content('/etc/hosts', strip=True) == get_file_content('/etc/hosts', strip=False).strip()



# Generated at 2022-06-13 03:50:31.252259
# Unit test for function get_file_content
def test_get_file_content():
    from tempfile import mkstemp
    from shutil import rmtree

    tmp_dir = '/tmp/ansible_test_get_file_content'
    os.makedirs(tmp_dir)

    fn = os.path.join(tmp_dir, 'test_file_dne')
    assert get_file_content(fn) is None

    fn = os.path.join(tmp_dir, 'test_file_empty')
    with open(fn, 'w') as tf:
        os.utime(fn, None)
    assert get_file_content(fn) is None

    fn = os.path.join(tmp_dir, 'test_file_1line')
    with open(fn, 'w') as tf:
        tf.write('test_1')
        os.utime(fn, None)


# Generated at 2022-06-13 03:50:33.480742
# Unit test for function get_file_content
def test_get_file_content():

    assert get_file_content("/dev/null", "No data") == "No data"
    assert get_file_content("/dev/zero",) == ""

# Generated at 2022-06-13 03:50:41.135247
# Unit test for function get_file_content
def test_get_file_content():
    test_content = 'new content\n'
    with open('/tmp/test_file_content', 'w') as tmp_file:
        tmp_file.write('new content\n')

    assert get_file_content('/tmp/test_file_content') == test_content
    assert get_file_content('/tmp/test_file_content', strip=True) == test_content.strip()
    assert get_file_content('/tmp/test_file_content', strip=False) == test_content
    assert get_file_content('/tmp/test_file_content', default='default') == test_content
    assert get_file_content('/tmp/test_file_content', default='default', strip=False) == test_content

# Generated at 2022-06-13 03:50:45.975088
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content('/etc/profile', default='No such file or directory') == 'No such file or directory'
    assert get_file_content('/etc/profile', default='No such file or directory', strip=False) == 'No such file or directory'
    assert get_file_content('/etc/profile', default='No such file or directory') != '  No such file or directory'
    assert get_file_content('/etc/profile', default='No such file or directory', strip=False) == '  No such file or directory'



# Generated at 2022-06-13 03:50:53.043552
# Unit test for function get_file_content
def test_get_file_content():
    def test_get_file_content():
        result = get_file_content('/tmp/__no_such_file', default='foo')
        assert result == 'foo'

        result = get_file_content('/tmp/__no_such_file', default='foo', strip=False)
        assert result == 'foo'

        with open('/tmp/test1', 'w') as f:
            f.write('   test   ')

        result = get_file_content('/tmp/test1', default='foo', strip=False)
        assert result == '   test   '

        result = get_file_content('/tmp/test1', default='foo')
        assert result == 'test'

        with open('/tmp/test2', 'w') as f:
            f.write('')

        result = get_

# Generated at 2022-06-13 03:51:03.298853
# Unit test for function get_file_content
def test_get_file_content():
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock import patch, mock_open
    import ansible_collections.notstdlib.moveitallout.plugins.module_utils.system.linux as linux

    fake_file1 = b"hello world this is a test"
    fake_file2 = ""
    fake_file3 = "hello world this is a test\n"

    test_mock = mock_open(read_data=fake_file1)
    test_mock.return_value.read.return_value = fake_file1


# Generated at 2022-06-13 03:51:10.579740
# Unit test for function get_file_content
def test_get_file_content():
    import shutil
    import tempfile
    # Case with file exist
    tmpdir = tempfile.mkdtemp()
    try:
        path_to_file = os.path.join(tmpdir, "test_file")
        with open(path_to_file, "w") as fp:
            fp.write("ABCD")
        assert get_file_content(path_to_file) == "ABCD"
    finally:
        shutil.rmtree(tmpdir)
    # Case with file does not exists
    tmpdir = tempfile.mkdtemp()
    try:
        path_to_file = os.path.join(tmpdir, "test_file")
        assert get_file_content(path_to_file) is None
    finally:
        shutil.rmtree(tmpdir)


# Generated at 2022-06-13 03:51:14.929030
# Unit test for function get_file_content
def test_get_file_content():
    '''test for get_file_content'''
    # basic test
    assert get_file_content(path='/etc/hosts') is not None

    # test with a non-existing path
    assert get_file_content(path='/etc/hosts-not-existing', default='default') == 'default'


# Generated at 2022-06-13 03:51:30.168944
# Unit test for function get_file_content
def test_get_file_content():
    # set up a temp file
    from tempfile import mkstemp
    from os import close, unlink
    fd, path = mkstemp()
    close(fd)
    unlink(path)

    # test file does not exist
    assert get_file_content(path) == None
    assert get_file_content(path, default='foo') == 'foo'
    assert get_file_content(path, strip=False) == None
    assert get_file_content(path, default='foo', strip=False) == 'foo'

    # test with empty file
    open(path, 'a').close()
    assert get_file_content(path) == ''
    assert get_file_content(path, default='foo') == ''
    assert get_file_content(path, strip=False) == ''
    assert get_

# Generated at 2022-06-13 03:51:32.685505
# Unit test for function get_file_content
def test_get_file_content():
    '''Test get_file_content'''
    assert get_file_content('/tmp/foo', default='bar') == 'bar'