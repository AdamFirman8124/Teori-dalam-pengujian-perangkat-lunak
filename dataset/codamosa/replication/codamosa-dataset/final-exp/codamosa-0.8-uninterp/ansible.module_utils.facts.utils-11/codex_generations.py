

# Generated at 2022-06-13 03:43:54.053676
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content('/etc/aliases') == get_file_content('/etc/aliases')
    assert not get_file_content('/etc/doesnotexist', default="NONE")
    assert get_file_content('/etc/aliases', strip=False) != get_file_content('/etc/aliases')

# Generated at 2022-06-13 03:44:01.987712
# Unit test for function get_file_lines
def test_get_file_lines():
    lines = ['abc', 'def', 'ghi', 'jkl', '']

    with open('test_get_file_lines', 'w') as fd:
        fd.write('\n'.join(lines) + '\n')

    for sep in [None, '\r', '\n', '\r\n']:
        assert lines == get_file_lines('test_get_file_lines', line_sep=sep)

    assert [lines[0]] == get_file_lines('test_get_file_lines', line_sep=sep, strip=False)

    try:
        os.remove('test_get_file_lines')
    except OSError:
        pass

# Generated at 2022-06-13 03:44:10.692076
# Unit test for function get_file_content
def test_get_file_content():
    assert '' == get_file_content('/does/not/exist')
    assert 'default' == get_file_content('/does/not/exist', 'default')
    assert '\n' == get_file_content('/does/not/exist', '\n')
    assert '  \n' == get_file_content('/does/not/exist', '  \n')
    assert '' == get_file_content('/does/not/exist', '  \n', strip=False)

    # does exist, is readable
    assert '' == get_file_content('/etc/passwd')
    assert 'default' == get_file_content('/etc/passwd', 'default')

    assert '\n' == get_file_content('/etc/passwd', '\n')

# Generated at 2022-06-13 03:44:20.482924
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content("/etc/hosts", default="") == ""
    assert get_file_content("/etc/hosts") == ""
    assert get_file_content("/etc/hosts", default="some_val") == "some_val"
    assert get_file_content("/etc/hosts", strip=False) == ""
    assert get_file_content("/etc/hosts", strip=False, default="some_val") == "some_val"

    with open("/tmp/test_content", "w") as f:
        f.write("Test content\n")

    assert get_file_content("/tmp/test_content", default="") == "Test content"
    assert get_file_content("/tmp/test_content", default="", strip=False) == "Test content\n"


# Generated at 2022-06-13 03:44:28.274741
# Unit test for function get_file_content
def test_get_file_content():
    ''' Check that get_file_content works as documented '''
    # Invalid path, return default
    assert get_file_content('/invalid/path', "foo") == "foo"
    # no such file, return default
    assert get_file_content('/etc/passwd0', "foo") == "foo"
    # file exists, no default
    assert get_file_content('/etc/passwd') == get_file_content('/etc/passwd')
    # exist & default, return default
    assert get_file_content('/etc/passwd', "foo") == "foo"
    # exist and strip
    assert get_file_content('/etc/passwd', strip=True).startswith("root:")

# Generated at 2022-06-13 03:44:35.563393
# Unit test for function get_file_lines
def test_get_file_lines():
    '''get_file_lines should return a list of lines from a file'''
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    myfile = 'myfile.txt'

    # Line separator string
    line_sep = '\n'

    # Create a file, add some lines to it, and close it
    with open(myfile, 'w') as f:
        f.write(to_bytes('Line1\nLine2\nLine3\n'))

    # Read in the file
    lines = get_file_lines(myfile)

    if lines[0] != 'Line1':
        module.fail_json(msg='Test 01 Failed:  Expected Line 1')
        return

# Generated at 2022-06-13 03:44:40.754372
# Unit test for function get_file_lines
def test_get_file_lines():
    filenames = [
        ('/etc/passwd', '/etc/passwd'),
    ]
    for fn in filenames:
        ret = get_file_lines(fn, strip=False)
        assert ret
        for line in ret:
            assert isinstance(line, str)
        if ret:
            assert ret[-1] == ''



# Generated at 2022-06-13 03:44:48.050318
# Unit test for function get_file_lines
def test_get_file_lines():
    assert get_file_lines('/etc/passwd') == [
        'root:x:0:0:root:/root:/bin/bash',
        'daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin',
        'bin:x:2:2:bin:/bin:/usr/sbin/nologin',
        'sys:x:3:3:sys:/dev:/usr/sbin/nologin',
        'sync:x:4:65534:sync:/bin:/bin/sync',
        'games:x:5:60:games:/usr/games:/usr/sbin/nologin'
    ]

# Generated at 2022-06-13 03:44:55.981499
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content('/no/file/here', default='bad') == 'bad'
    assert get_file_content('/etc/passwd', default='bad') != 'bad'
    assert get_file_content('/etc/passwd', default='bad', strip=False) != 'bad'
    assert get_file_content('/no/file/here', default='bad', strip=False) == 'bad'
    assert get_file_content('/etc/fstab', strip=False)



# Generated at 2022-06-13 03:45:06.392992
# Unit test for function get_file_lines
def test_get_file_lines():
    ''' Test for get_file_lines '''
    assert get_file_lines('/etc/resolv.conf') == get_file_lines('/etc/resolv.conf', line_sep='\n')
    assert get_file_lines('/etc/resolv.conf', line_sep='\n') == ['nameserver ::1', 'nameserver 127.0.0.1', 'search vagrantup.com']
    assert get_file_lines('/etc/resolv.conf', line_sep=' ') == ['nameserver', '::1', 'nameserver', '127.0.0.1', 'search', 'vagrantup.com']



# Generated at 2022-06-13 03:45:20.726162
# Unit test for function get_file_content
def test_get_file_content():
    # assume no file exists
    assert get_file_content('/no/file') is None

    # assume that exists and is readable
    assert get_file_content('/etc/hosts') == get_file_content('/etc/hosts', default=None, strip=False)

    # assume that exists and is readable
    assert get_file_content('/etc/hosts', default="empty file") == get_file_content('/etc/hosts', default=None, strip=False)

    # assume file exists but is not readable
    assert get_file_content('/etc/hosts') == get_file_content('/etc/hosts', default=None, strip=False)

    # assume file exists but is not readable
    assert get_file_content('/etc/hosts', default="empty file") == get_file_content

# Generated at 2022-06-13 03:45:28.336569
# Unit test for function get_file_lines
def test_get_file_lines():
    import tempfile
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write('a\nb\nc\n')
    assert set(get_file_lines(f.name)) == set(['a', 'b', 'c'])
    os.remove(f.name)
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write('a,b,c\n')
    assert set(get_file_lines(f.name, line_sep=',')) == set(['a', 'b', 'c'])
    os.remove(f.name)
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write('a,b,c\n')

# Generated at 2022-06-13 03:45:36.350308
# Unit test for function get_file_lines
def test_get_file_lines():
    # Setup a testing file
    filename = "/tmp/test.txt"
    with open(filename, 'w') as f:
        f.write("Test\nTest\n")

    # Test with empty separator
    result = get_file_lines(filename, line_sep='')
    assert result == ['TestTest'], "Expected ['TestTest'], found %s" % result

    # Test with line separator
    result = get_file_lines(filename, line_sep="\n")
    assert result == ['Test', 'Test'], "Expected ['Test', 'Test'], found %s" % result

    # Test with multiline separator
    result = get_file_lines(filename, line_sep="\n\n")

# Generated at 2022-06-13 03:45:44.634807
# Unit test for function get_file_content
def test_get_file_content():
    testfile = './testfile'
    # Create test file
    test_string = 'Test String'
    with open(testfile, 'w') as f:
        f.write(test_string)
    # Test file created check that content is correctly returned
    assert get_file_content(testfile) == test_string
    # Cleanup
    os.unlink(testfile)
    # Check default is returned if file not found
    assert get_file_content(testfile, default="default") == "default"


# Generated at 2022-06-13 03:45:47.686857
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content('/etc/passwd', default='/etc/passwd') == '/etc/passwd'
    assert get_file_content('/etc/hostname') == 'debian8-64'

# Generated at 2022-06-13 03:45:55.891402
# Unit test for function get_file_content
def test_get_file_content():
    text_path1 = '/etc/mtab'
    text_path2 = '/etc/baddata'
    text_path3 = '/etc/non_existent_file'
    text_path4 = '/etc/non_existent_file'
    text_path5 = '/etc/non_existent_file'

    # Verify that text_path1 file is readable
    assert os.path.exists(text_path1) == True
    assert os.access(text_path1, os.R_OK) == True

    # Verify that text_path2 file is readable
    assert os.path.exists(text_path2) == True
    assert os.access(text_path2, os.R_OK) == True

    # Verify that text_path3 file is not readable

# Generated at 2022-06-13 03:46:06.158676
# Unit test for function get_file_content
def test_get_file_content():
    class Args(object):
        def __init__(self, path, default=None, strip=True):
            self.path = path
            self.default = default
            self.strip = strip
    assert get_file_content(Args('/proc/sys/fs/file-max')) == '1048576'
    assert get_file_content(Args('/proc/sys/fs/file-max'), default='foo') == '1048576'
    assert get_file_content(Args('/proc/sys/fs/file-max'), default='foo', strip=False) == '1048576\n'
    assert get_file_content(Args('/proc/foobar'), default='foo') == 'foo'

# Generated at 2022-06-13 03:46:17.018839
# Unit test for function get_file_lines
def test_get_file_lines():
    assert get_file_lines('../../lib/ansible/module_utils/basic.py', line_sep='\n')[0] == ""
    assert get_file_lines('../../lib/ansible/module_utils/basic.py', strip=False, line_sep='\n')[0] == " #"
    assert get_file_lines('../../lib/ansible/module_utils/basic.py', line_sep='\n')[1] == " # (c) 2012, Michael DeHaan <michael.dehaan@gmail.com>"

# Generated at 2022-06-13 03:46:26.509295
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content('sysctl.py', default='')

    # file contains 'test\n'
    assert get_file_content('./tests/unittests/test_file.txt', default='', strip=True) == 'test'
    # file contains 'test\n'
    assert get_file_content('./tests/unittests/test_file.txt', default='', strip=False) == 'test\n'
    # exists but not readable
    assert get_file_content('./tests/unittests/test_file_no_read.txt', default='') == ''
    # does not exists
    assert get_file_content('./tests/unittests/test_file_no_exists.txt', default='') == ''
    # does not exists and default=None
   

# Generated at 2022-06-13 03:46:31.239793
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content('./test_files/file_ansible_facts_module', default=None) == 'module_setup'
    assert get_file_content('./test_files/no_such_file', default='default_value') == 'default_value'
    assert get_file_content('./test_files/file_ansible_facts_module', default='default_value') == 'module_setup'

# Generated at 2022-06-13 03:46:43.080012
# Unit test for function get_file_lines
def test_get_file_lines():
    assert get_file_lines('/dev/null') == []
    tf = '/tmp/salt-test-file-lines'
    with open(tf, 'w') as f:
        f.write('a\nb\nc\n')
    assert get_file_lines(tf) == ['a', 'b', 'c']
    assert get_file_lines(tf, line_sep='a') == ['', '\nb\nc\n']
    with open(tf, 'w') as f:
        f.write('a\nb\nc\n\n')
    assert get_file_lines(tf) == ['a', 'b', 'c', '']

# Generated at 2022-06-13 03:46:50.539589
# Unit test for function get_file_lines
def test_get_file_lines():
    # Make sure it handles different line endings
    assert get_file_lines("tests/test_utils/test_data/filelines/file1.txt") == ['a', 'b', 'c']
    assert get_file_lines("tests/test_utils/test_data/filelines/file2.txt") == ['a', 'b', 'c']
    assert get_file_lines("tests/test_utils/test_data/filelines/file3.txt") == ['a', 'b', 'c']

    # Check the strip argument
    assert get_file_lines("tests/test_utils/test_data/filelines/file1.txt", strip=False) == ['a ', 'b ', 'c ']

    # Check the line_sep argument

# Generated at 2022-06-13 03:46:59.970418
# Unit test for function get_file_content
def test_get_file_content():
    try:
        import pytest
    except:
        print("pytest is required for unit tests")
        exit(0)


# Generated at 2022-06-13 03:47:06.338964
# Unit test for function get_file_lines
def test_get_file_lines():
    print("get_file_lines function")

    # test simple file with \n new lines
    path = "/tmp/ansible_test_file_lines"
    data = "this is a test\nit has two lines\nin it\n"
    with open(path, "w") as f:
        f.write(data)

    ret = get_file_lines(path)
    print(ret)
    assert len(ret) == 4
    assert ret == data.splitlines()

    with open(path, "w") as f:
        f.write(data.replace('\n', '\r'))

    ret = get_file_lines(path, line_sep='\r')
    print(ret)
    assert len(ret) == 4
    assert ret == data.splitlines()



# Generated at 2022-06-13 03:47:14.610262
# Unit test for function get_file_content
def test_get_file_content():

    assert get_file_content('/etc/hosts', default='0.0.0.0') == '0.0.0.0'
    assert get_file_content('./test-data/null.txt') == ''
    assert get_file_content('./test-data/null.txt', default='0.0.0.0') == '0.0.0.0'
    assert get_file_content('./test-data/fake.txt') == 'spam\nham\neggs'
    assert get_file_content('./test-data/fake.txt', strip=False) == 'spam\nham\neggs\n'
    assert get_file_content('./test-data/fake.txt', strip=True) == 'spam\nham\neggs'
   

# Generated at 2022-06-13 03:47:22.730451
# Unit test for function get_file_lines
def test_get_file_lines():
    if os.path.exists('/tmp/ansible_test'):
        os.unlink('/tmp/ansible_test')

    # Create test file
    with open('/tmp/ansible_test', 'w') as testfile:
        testfile.write('1\n2\n3\n4\n5\n')

    # Test 1: Get list of lines
    assert get_file_lines('/tmp/ansible_test') == ['1', '2', '3', '4', '5']

    # Test 2: Get list of lines, stripping whitespace
    assert get_file_lines('/tmp/ansible_test', True) == ['1', '2', '3', '4', '5']

    # Test 3: Get list of lines, stripping whitespace and specifying custom line separator
    assert get_

# Generated at 2022-06-13 03:47:32.680047
# Unit test for function get_file_lines
def test_get_file_lines():
    try:
        os.makedirs("/tmp/ansible_test")
    except Exception:
        pass

    assert get_file_lines("/tmp/ansible_test") == []
    assert get_file_lines("/tmp/ansible_test", line_sep="\n") == []

    assert get_file_lines("/tmp/ansible_test", strip=False) == ['']
    assert get_file_lines("/tmp/ansible_test", strip=False, line_sep="\n") == ['']

    with open("/tmp/ansible_test/file1", "w") as outfile:
        outfile.write("a")
        outfile.write("b")
        outfile.write("c")


# Generated at 2022-06-13 03:47:38.250351
# Unit test for function get_file_lines
def test_get_file_lines():
    '''test function get_file_lines'''

    lines = '''
    line 1
    line 2
    line 3
    '''

    file_name = os.path.join(os.path.dirname(__file__), '_test_file_lines')

    # Test without line separator
    with open(file_name, 'w') as f:
        f.write(lines)

    assert get_file_lines(file_name) == ['line 1', 'line 2', 'line 3']

    # Test with different line separators
    line_seps = ('\n', '\r', '\r\n', '  ', '  \n')

# Generated at 2022-06-13 03:47:44.532693
# Unit test for function get_file_lines
def test_get_file_lines():
    assert get_file_lines('/proc/self/cmdline') == [b'/usr/bin/python3']
    assert get_file_lines('/proc/self/cmdline', strip=False) == [b'/usr/bin/python3\x00']

    assert get_file_lines('/proc/self/cmdline', line_sep='\0') == [b'/usr/bin/python3']
    assert get_file_lines('/proc/self/cmdline', strip=False, line_sep='\0') == [b'/usr/bin/python3']

    assert get_file_lines('/proc/self/cmdline', line_sep=b'\0') == [b'/usr/bin/python3']

# Generated at 2022-06-13 03:47:55.420757
# Unit test for function get_file_content
def test_get_file_content():
    """Test function get_file_content()"""
    import os

    file_name = 'test_file.txt'
    test_file_path = os.getcwd() + '/' + file_name
    test_file_pointer = open(file_name, 'w')
    test_file_pointer.write('Test content of file')
    test_file_pointer.close()

    assert get_file_content(test_file_path) == 'Test content of file'
    assert get_file_content(test_file_path, strip=False) == 'Test content of file\n'
    assert get_file_content(test_file_path, default='Alternate content') == 'Test content of file'
    assert get_file_content('dummy_file.txt', default='Alternate content') == 'Alternate content'

   

# Generated at 2022-06-13 03:47:58.297915
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content(__file__, '') != ''

# Generated at 2022-06-13 03:48:01.938799
# Unit test for function get_file_content
def test_get_file_content():
    file = 'test_file'
    test_str = 'test'
    f = open(file, 'w')
    f.write(test_str)
    f.close()

    assert get_file_content(file) == test_str
    assert get_file_content(file, strip=False) == test_str + '\n'

    os.remove(file)

# Generated at 2022-06-13 03:48:13.395899
# Unit test for function get_file_content
def test_get_file_content():
    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch

    class TestSource(unittest.TestCase):
        def setUp(self):
            self.fake_path = '/test/file/path'
            self.fake_data = 'Hello World'
            self.fake_default = 'default'

            self.mock_open = patch('ansible.module_utils.common.os.open')
            self.mock_open_obj = self.mock_open.start()

            self.mock_access = patch('os.access')
            self.mock_access_obj = self.mock_access.start()

            self.mock_file = patch('__builtin__.open')
            self.mock_file_obj = self.mock

# Generated at 2022-06-13 03:48:16.133875
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content("/etc/hosts") == get_file_content("/etc/hosts", strip=False)
    assert get_file_content("/etc/shadow") == None
    assert get_file_content("/etc/shadow", default="") == ""
    assert get_file_content("/etc/passwd")
    assert get_file_content("/etc/shadow", strip=False) == None
    assert get_file_content("/etc/shadow", default="", strip=False) == ""



# Generated at 2022-06-13 03:48:22.922821
# Unit test for function get_file_content
def test_get_file_content():
    '''Asserts get_file_content works as expected'''
    import tempfile

    tmp_dir = tempfile.mkdtemp()
    tmp_file_1 = tmp_dir + '/tmp_file_1'
    tmp_file_2 = tmp_dir + '/tmp_file_2'

    # Create the two test files
    with open(tmp_file_1, 'w') as f:
        f.write('test_get_file_content')

    with open(tmp_file_2, 'w') as f:
        f.write('test_get_file_content_empty')

    # Delete the last newline
    with open(tmp_file_2, 'a') as f:
        f.seek(-1, os.SEEK_END)
        f.truncate()

    # Test reading file1

# Generated at 2022-06-13 03:48:32.764472
# Unit test for function get_file_content
def test_get_file_content():
    import tempfile
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts import Facts

    module = AnsibleModule(
        argument_spec=dict()
    )

    facts = Facts(module).populate()

    with tempfile.NamedTemporaryFile(mode='w+') as tmpfile:
        tmpfile.write('test\n')
        tmpfile.flush()

        # Test normal case
        module.assertEqual(get_file_content(tmpfile.name), 'test')

        # Test try to read an inaccessible file
        os.chmod(tmpfile.name, 0)
        module.assertEqual(get_file_content(tmpfile.name), None)
        os.chmod(tmpfile.name, 0o700)

        # Test default value
        tmp

# Generated at 2022-06-13 03:48:34.919007
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content('/nonexistent/file/path') == None


# Generated at 2022-06-13 03:48:41.902097
# Unit test for function get_file_content
def test_get_file_content():
    path = os.path.expanduser("~/.vimrc")

    content = get_file_content(path)
    assert content is not None and len(content) > 0

    content = get_file_content("/tmp/test.txt")
    assert content is None

    content = get_file_content("/tmp/test.txt", default="default")
    assert content == "default"

    path = '/proc/meminfo'
    content = get_file_content(path)
    assert content is not None and len(content) > 0 and content.startswith("MemTotal")

    path = '/proc/meminfo'
    content = get_file_content(path, strip=False)
    assert content is not None and len(content) > 0 and content.endswith("\n")

# Generated at 2022-06-13 03:48:46.482878
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content(os.path.join(os.path.dirname(__file__), 'test_file/test_file1'), default=None, strip=False) == '  this is a test  \nhere is another line\n'
    assert get_file_content(os.path.join(os.path.dirname(__file__), 'test_file/test_file1'), default=None) == 'this is a test\nhere is another line'
    assert get_file_content(os.path.join(os.path.dirname(__file__), 'test_file/test_file2'), default=None, strip=False) == '  this is a test  \nhere is another line'

# Generated at 2022-06-13 03:48:51.874830
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content('/dev/null', '') == ''
    assert get_file_content('/dev/null', default='foo') == 'foo'
    assert get_file_content('/dev/null', default='foo', strip=False) == 'foo'
    assert get_file_content('/dev/null', default='foo', strip=True) == 'foo'


# Generated at 2022-06-13 03:48:59.665022
# Unit test for function get_file_content
def test_get_file_content():
    # test valid file
    assert get_file_content('/proc/version')
    # test invalid file
    assert get_file_content('/proc/invalidfilepath', default="default") == "default"

    # test invalid path
    assert get_file_content('/invalidpath', default="default") == "default"

    # test file exist but can not access
    assert get_file_content('/etc/shadow', default="default") == "default"

# Generated at 2022-06-13 03:49:07.355928
# Unit test for function get_file_content
def test_get_file_content():
    # Create test file
    test_file_path = '/tmp/ansible_test_file.txt'
    test_file = open(test_file_path, 'w')
    test_file.write("MyTestString")
    test_file.close()

    # Read test file
    content_string = get_file_content(test_file_path)
    assert content_string == 'MyTestString'

    # Remove test file
    os.remove(test_file_path)

    # test default value when file does not exist
    assert get_file_content('/tmp/does_not_exist.txt', 'default_value') == 'default_value'

    # test default value is returned when file is empty
    test_file = open(test_file_path, 'w')
    test_file.close()
    assert get

# Generated at 2022-06-13 03:49:11.387962
# Unit test for function get_file_content
def test_get_file_content():
    import tempfile

    def __test_get_file_content(path, default=None, strip=True):
        temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
        temp_file.write(path)
        temp_file.close()
        ret = get_file_content(temp_file.name, default, strip)
        os.unlink(temp_file.name)
        return ret

    assert __test_get_file_content('foo', 'bar', False) == 'foo'
    assert __test_get_file_content('foo', 'bar', True) == 'foo'
    assert __test_get_file_content('foo\n', 'bar', False) == 'foo\n'

# Generated at 2022-06-13 03:49:15.035984
# Unit test for function get_file_content
def test_get_file_content():
    test_file = '/tmp/get_file_content.txt'
    test_value = 'simple_test_value'
    with open(test_file, 'w') as f:
        f.write(test_value)
    assert get_file_content(test_file) == test_value



# Generated at 2022-06-13 03:49:25.175738
# Unit test for function get_file_content
def test_get_file_content():

    # get_file_content() should return the contents of '/etc/hosts'
    hosts = get_file_content('/etc/hosts')
    assert(hosts.endswith('localdomain'))

    # get_file_content() should return None if the file does not exist
    hosts_again = get_file_content('/no_such_file')
    assert(hosts_again is None)

    # get_file_content() should return the contents of '/etc/hosts'
    hosts_again = get_file_content('/etc/hosts', 'default')
    assert(hosts_again.endswith('localdomain'))

    # get_file_content('/no_such_file', 'default') should return 'default'

# Generated at 2022-06-13 03:49:27.027348
# Unit test for function get_file_content
def test_get_file_content():
    result = get_file_content("/dev/zero", default="default", strip=False)
    assert result == "default"


# Generated at 2022-06-13 03:49:33.929031
# Unit test for function get_file_content
def test_get_file_content():
    ''' get_file_content unit test'''
    # create a temp file
    tempfile = "/tmp/ansible_test_file"
    testline = "this is a test\n"

    f = open(tempfile, 'w')
    f.write(testline)
    f.close()

    # test file exists and read, should return data
    data = get_file_content(tempfile)
    if data != testline:
        print("FAILED: could not read test file, expected: %s got: %s" % (testline, data))
        exit(1)

    # delete the file, test should fail
    os.unlink(tempfile)
    data = get_file_content(tempfile, "nofile")

# Generated at 2022-06-13 03:49:34.903741
# Unit test for function get_file_content
def test_get_file_content():
    content = get_file_content('/etc/hostname')
    assert content



# Generated at 2022-06-13 03:49:41.971476
# Unit test for function get_file_content

# Generated at 2022-06-13 03:49:48.065308
# Unit test for function get_file_content
def test_get_file_content():
    test_file_path = '/tmp/test_file'
    test_file_content = 'test_content'
    fd = open(test_file_path, 'w')
    fd.write(test_file_content)
    fd.close()
    result = get_file_content(test_file_path)
    assert result == test_file_content
    os.remove(test_file_path)