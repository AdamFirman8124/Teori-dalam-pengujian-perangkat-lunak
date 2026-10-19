

# Generated at 2022-06-13 03:43:59.307380
# Unit test for function get_file_lines
def test_get_file_lines():
    # test with no file specified
    assert get_file_lines(None) == [], 'get_file_lines returned an unexpected result'
    assert get_file_lines('') == [], 'get_file_lines returned an unexpected result'
    assert get_file_lines('/does/not/exist') == [], 'get_file_lines returned an unexpected result'

    # write a test file
    with open('test', 'w') as test_file:
        test_file.write('one\ntwo\nthree\nfour')
    # test without stripping
    assert get_file_lines('test') == ['one', 'two', 'three', 'four'], 'get_file_lines returned an unexpected result'

# Generated at 2022-06-13 03:44:05.609620
# Unit test for function get_file_content
def test_get_file_content():
    import tempfile
    import os

    content = 'test'
    default_val = 'default'
    content_with_space = 'test space'
    path = tempfile.gettempdir() + '/test.txt'

    # Write content to temporary file
    with open(path, 'w') as f:
        f.write(content)

    # Test that the content of our file was returned
    assert get_file_content(path, None) == content

    # Test that the default value was returned when the file could not be read
    os.chmod(path, 0)  # Set file permission to 0 (No read permission)
    assert get_file_content(path, default_val) == default_val

    # Test that the default value was returned when the file was empty
    os.chmod(path, 644)  # Set file

# Generated at 2022-06-13 03:44:12.105162
# Unit test for function get_file_content
def test_get_file_content():
    test_file = "/tmp/test_file.txt"
    if not os.path.exists(test_file):
        with open(test_file, 'w') as f:
            f.write('This is a test file')

    result = get_file_content(test_file, default='', strip=True)
    os.remove(test_file)
    assert result == 'This is a test file'

# Generated at 2022-06-13 03:44:21.740600
# Unit test for function get_file_lines
def test_get_file_lines():
    expected_lines = ['one', 'two', 'three']

    # Test standard input with trailing newline
    test_string = "\n".join(expected_lines) + "\n"
    actual_lines = get_file_lines(test_string)
    assert expected_lines == actual_lines

    # Test standard input without trailing newline
    test_string = "\n".join(expected_lines)
    actual_lines = get_file_lines(test_string)
    assert expected_lines == actual_lines

    # Test single line input with newline
    test_string = expected_lines[0] + "\n"
    actual_lines = get_file_lines(test_string)
    assert [[expected_lines[0]]] == actual_lines

    # Test single line input with no newline

# Generated at 2022-06-13 03:44:27.846636
# Unit test for function get_file_content
def test_get_file_content():
    test_file_name = 'test_file_content.txt'
    file_contents = 'Hello, World!'

    try:
        # Create test file
        file_handle = open(test_file_name, 'w')
        file_handle.write(file_contents)
        file_handle.close()

        # Read test file
        file_contents_read = get_file_content(test_file_name)
        assert file_contents_read == file_contents

    finally:
        # Cleanup test file
        os.remove(test_file_name)



# Generated at 2022-06-13 03:44:33.901344
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content('tests/test_utils/test_get_file_content') == 'test_content'
    assert get_file_content('tests/test_utils/test_get_file_content', strip=False) == '    test_content    \n'
    assert get_file_content('tests/test_utils/test_get_file_content', default='test_default') == 'test_content'
    assert get_file_content('tests/test_utils/test_file_does_not_exist', default='test_default') == 'test_default'



# Generated at 2022-06-13 03:44:44.617980
# Unit test for function get_file_lines
def test_get_file_lines():
    from tempfile import mkstemp
    from ansible.module_utils.basic import AnsibleModule

    path = mkstemp()[1]
    for separator in u' ', u'\n', u'\t', u'\t\n', u'\n\n', u'\n\t':
        expected = [u'one', u'two', u'three', u'four', u'five']
        expected = u'\n'.join(expected) + separator
        with open(path, 'w') as f:
            f.write(expected)

        actual = get_file_lines(path, line_sep=separator)
        assert actual == [u'one', u'two', u'three', u'four', u'five']
    os.remove(path)

    path = mkstemp

# Generated at 2022-06-13 03:44:45.524002
# Unit test for function get_file_lines
def test_get_file_lines():
    assert get_file_lines('/etc/group')

# Generated at 2022-06-13 03:44:47.761446
# Unit test for function get_file_content
def test_get_file_content():
    content = get_file_content("/etc/resolv.conf", "test")
    assert content in ["test", "nameserver 1.1.1.1\n"]



# Generated at 2022-06-13 03:44:49.652687
# Unit test for function get_file_lines
def test_get_file_lines():
    assert get_file_lines('./utils/test_file_lines') == ['line1', 'line2', 'line3']

# Generated at 2022-06-13 03:44:58.282423
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content('/etc/passwd')
    assert get_file_content('/etc/passwd', strip=False)
    assert get_file_content('/etc/passwd', default='foo')
    assert get_file_content('/etc/passwd', default='foo') == get_file_content('/etc/passwd')
    assert get_file_content('/root/bar') == 'foo'


# Generated at 2022-06-13 03:45:07.574730
# Unit test for function get_file_content
def test_get_file_content():
    test_path = os.path.dirname(os.path.abspath(__file__)) + os.sep + "testfile"
    assert get_file_content(test_path) == "hello world"
    assert get_file_content(test_path, "") == "hello world"
    assert get_file_content(test_path, None, False) == "hello world"
    assert get_file_content(test_path, "") == "hello world"
    assert get_file_content(test_path + ".noexist") == None
    assert get_file_content(test_path + ".noexist", "hello world") == "hello world"


# Generated at 2022-06-13 03:45:18.749433
# Unit test for function get_file_content

# Generated at 2022-06-13 03:45:25.221087
# Unit test for function get_file_content
def test_get_file_content():
    path = './test_content.txt'
    try:
        with open(path, "w") as f:
            f.write("ansible")
        content = get_file_content(path)
        os.remove(path)
        print("Test passed")
    except:
        print("Test failed")
    if content != "ansible":
        raise AssertionError("Error in get_file_content")

##### UNIT TESTS #####
if __name__ == '__main__':
    test_get_file_content()

# Generated at 2022-06-13 03:45:34.183170
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content('/dev/null') is None
    assert get_file_content('/dev/null', default='xyz') == 'xyz'
    assert get_file_content('/this/file/does/not/exist') is None
    assert get_file_content('/this/file/does/not/exist', default='xyz') == 'xyz'
    assert get_file_content('/dev/null', default=False) is False
    assert get_file_content('/dev/null', default=0) == 0
    assert get_file_content('/dev/null', default=[]) == []
    assert get_file_content('/dev/null', default='') == ''

    # Function should return the content of the file, stripped.
    file_with_content = '/tmp/some-file'

# Generated at 2022-06-13 03:45:45.261980
# Unit test for function get_file_content
def test_get_file_content():
    test_file_content = "dummy content"
    test_file_path = "/tmp/get_file_content_test"
    with open(test_file_path, "w") as f:
        f.write(test_file_content)

    file_content = get_file_content(test_file_path)
    assert file_content == test_file_content

    file_content = get_file_content(test_file_path, strip=False)
    assert file_content == "%s\n" % test_file_content

    default_content = "dummy default content"
    file_content = get_file_content("/tmp/get_file_content_test_invalid_path", default=default_content)
    assert file_content == default_content


# Generated at 2022-06-13 03:45:54.404687
# Unit test for function get_file_content
def test_get_file_content():
    import tempfile
    import os
    import stat

    testfile = tempfile.NamedTemporaryFile(delete=False)
    testfile2 = tempfile.NamedTemporaryFile(delete=False)
    testfile3 = tempfile.NamedTemporaryFile(delete=False)
    testfile4 = tempfile.NamedTemporaryFile(delete=False)
    testfile5 = tempfile.NamedTemporaryFile(delete=False)

# Generated at 2022-06-13 03:46:00.099749
# Unit test for function get_file_content
def test_get_file_content():
    import tempfile
    fd, path = tempfile.mkstemp()
    try:
        with os.fdopen(fd, 'w') as f:
            f.write('\n')
        assert get_file_content(path) == ''
    finally:
        os.remove(path)



# Generated at 2022-06-13 03:46:11.459175
# Unit test for function get_file_content
def test_get_file_content():
    # create test files
    with open('test1', 'w') as f:
        f.write(' hello\n\n')
    with open('test2', 'w') as f:
        f.write('\n\n hello')
    with open('test3', 'w') as f:
        f.write(' \t  \n hello \n\n')
    with open('test4', 'w') as f:
        f.write('hello ')
    with open('test5', 'w') as f:
        f.write('')
    with open('test6', 'w') as f:
        f.write('\n')

    # test stripping defaults to True
    assert get_file_content('test1') == 'hello'
    assert get_file_content('test2') == 'hello'

    #

# Generated at 2022-06-13 03:46:13.083401
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content('/etc/environment')
    assert not get_file_content('/bad/path')
    assert get_file_content('/bad/path', 'default') == 'default'

# Generated at 2022-06-13 03:46:25.031126
# Unit test for function get_file_content
def test_get_file_content():
    test_string = "test string"
    temp_file = open("tempfile", "w")
    temp_file.write(test_string)
    temp_file.close()

    assert get_file_content("tempfile") == test_string
    assert get_file_content("tempfile", "not the test string") == test_string

    assert get_file_content("notatempfile", "test string") == "test string"
    assert get_file_content("notatempfile", "test string") != test_string

    assert get_file_content("tempfile", strip=False) != test_string
    assert get_file_content("tempfile", strip=False) != test_string + "\n"
    assert get_file_content("tempfile", strip=False) == test_string + "\n"

    os.remove

# Generated at 2022-06-13 03:46:28.946444
# Unit test for function get_file_content
def test_get_file_content():
    f_path = os.path.realpath(__file__)
    assert get_file_content(f_path, default='') != ''

    assert get_file_content('/tmp/does/not/exist') is None

    assert get_file_content(f_path, strip=False) is not None



# Generated at 2022-06-13 03:46:37.044254
# Unit test for function get_file_content
def test_get_file_content():

    # create a test file
    import tempfile
    f = tempfile.NamedTemporaryFile(mode="w+t", delete=False)
    f.write("some text here")
    f.close()

    # run tests on the file we created above
    assert get_file_content(f.name) == "some text here", \
        "Failed to read file %s" % f.name
    assert get_file_content(f.name, strip=False) == "some text here\n"
    assert get_file_content(f.name, default="hello") == "some text here"
    assert get_file_content(f.name, default="hello", strip=False) == "some text here\n", \
        "Failed to read file %s" % f.name

# Generated at 2022-06-13 03:46:44.704624
# Unit test for function get_file_content
def test_get_file_content():
    file_content = get_file_content('/etc/passwd', default='fail')
    assert file_content is not None
    assert file_content != 'fail'
    file_content = get_file_content('/etc/non-existant-file', default='success')
    assert file_content == 'success'
    file_content = get_file_content('/etc/passwd', default='fail', strip=False)
    assert file_content is not None
    assert file_content != 'fail'
    assert not file_content.endswith('\n')


# Generated at 2022-06-13 03:46:56.454933
# Unit test for function get_file_content
def test_get_file_content():
    # get_file_content
    # Error on non-existing file
    assert get_file_content('/tmp/TESTING-FILE-DOES-NOT-EXIST') is None
    # Make sure we get expected data
    assert get_file_content('/etc/hosts', strip=False) == get_file_content('/etc/hosts', default='', strip=False)
    assert get_file_content('/etc/hosts', default='', strip=False) != get_file_content('/etc/hostname', default='', strip=False)
    assert get_file_content('/etc/hosts') == get_file_content('/etc/hosts', strip=True)
    assert get_file_content('/etc/hosts') != get_file_content('/etc/hosts', strip=False)



# Generated at 2022-06-13 03:47:02.476559
# Unit test for function get_file_content
def test_get_file_content():
    test = get_file_content("/dev/null")
    assert test is None, "Failed to return None on /dev/null"
    test = get_file_content("/dev/null", default="test")
    assert test == "test", "Failed to return correct default"
    test = get_file_content("/bin/ls")
    assert len(test) > 0, "Failed to read any content from /bin/ls"

if __name__ == '__main__':
    test_get_file_content()

# Generated at 2022-06-13 03:47:04.492974
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content(os.path.join(os.path.dirname(__file__), 'unit_tests/get_file_content')) == 'test123'



# Generated at 2022-06-13 03:47:10.108224
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content('/proc/sys/fs/file-max', default=-1, strip=False) != -1
    assert get_file_content('/proc/sys/fs/file-max', default=-1) == get_file_content('/proc/sys/fs/file-max', default=-1, strip=True)
    assert get_file_content('/proc/unknown_file', default='invalid') == 'invalid'


# Generated at 2022-06-13 03:47:13.730624
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content('/proc/sys/kernel/domainname') == '(none)'
    assert get_file_content('/proc/sys/kernel/domainname', default='unknown') == '(none)'
    assert get_file_content('/proc/sys/kernel/domainname', default='unknown', strip=False) == '(none)'


# Generated at 2022-06-13 03:47:20.330305
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content('/bin/sh', default='__NOTFOUND__') == '#!/usr/bin/env python\n'
    assert get_file_content('/bin/truc', default='__NOTFOUND__') == '__NOTFOUND__'
    assert get_file_content('/bin/sh', default='__NOTFOUND__', strip=False) == '#!/usr/bin/env python\n'
    assert get_file_content('/bin/truc', default='__NOTFOUND__', strip=False) == '__NOTFOUND__'

# Generated at 2022-06-13 03:47:28.537302
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content('/etc/passwd') is not None, 'This test will fail if you do not have /etc/passwd'
    assert get_file_content('/bad/path') is None, 'This test will fail unless it can read /bad/path'
    assert get_file_content('./test_module_utils.py', default='hello world') == 'hello world', 'This test will always fail'



# Generated at 2022-06-13 03:47:32.493917
# Unit test for function get_file_content
def test_get_file_content():
    from tempfile import mkstemp

    test_content = 'testing_content'
    (fd, path) = mkstemp()
    try:
        os.write(fd, test_content)
        os.close(fd)
        assert(test_content == get_file_content(path, False))
    finally:
        os.unlink(path)

# Generated at 2022-06-13 03:47:39.003912
# Unit test for function get_file_content
def test_get_file_content():
    import tempfile
    import textwrap

    testfile = tempfile.NamedTemporaryFile(delete=False)

# Generated at 2022-06-13 03:47:40.048826
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content('/etc/hostname') == 'ansible-controller'

# Generated at 2022-06-13 03:47:43.584256
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content('/etc/passwd') == open('/etc/passwd').read()
    assert get_file_content('/doesnotexist', default='foo') == 'foo'
    assert get_file_content('/etc/passwd', strip=False) == open('/etc/passwd').read()
    assert get_file_content('/etc/passwd', strip=True) == open('/etc/passwd').read().strip()

# Generated at 2022-06-13 03:47:48.926704
# Unit test for function get_file_content
def test_get_file_content():
    path = '/etc/hosts'
    data = get_file_content(path)
    if data:
        assert(len(data) > 0)
    else:
        assert(False)

    path = '/nonexistentfile'
    data = get_file_content(path)
    if data is not None:
        assert(False)


# Generated at 2022-06-13 03:47:54.565917
# Unit test for function get_file_content
def test_get_file_content():
    '''
    Read a simple file and return the contents
    '''
    assert get_file_content('/etc/os-release', default='', strip=True)

    # Should get the same result with and without strip
    assert get_file_content('/etc/os-release', default='', strip=True) == get_file_content('/etc/os-release', default='', strip=False)

# Generated at 2022-06-13 03:47:56.683891
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content(path="/etc/passwd", strip=True) == open("/etc/passwd", "r").read().strip()



# Generated at 2022-06-13 03:48:03.683262
# Unit test for function get_file_content
def test_get_file_content():
    '''Test for function get_file_content'''

    assert get_file_content('/proc/version', strip=False) == get_file_content('/proc/version', strip=False)
    assert get_file_content('/proc/__version', default='OS release') == 'OS release'
    assert get_file_content('/proc/version', default='OS release', strip=True) == get_file_content('/proc/version', strip=True)
    assert get_file_content('/proc/__version', default=None) is None

    # Check that the function does not fail due to to a file mode not being readable.
    fd, temp_file = tempfile.mkstemp()
    os.chmod(temp_file, 0000)
    assert get_file_content(temp_file) is None
    os

# Generated at 2022-06-13 03:48:09.895125
# Unit test for function get_file_content
def test_get_file_content():

    # Test for a file that does not exist
    data = get_file_content("/path/to/a/file/that/does/not/exist")

    # Test for a file that does exist
    data = get_file_content("/etc/group")

    # Test for a file that exists but is empty
    data = get_file_content("/etc/fstab")


# Generated at 2022-06-13 03:48:13.762687
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content('/dev/null', default=5) == 5
    assert get_file_content('/dev/null') == None

# Generated at 2022-06-13 03:48:20.665677
# Unit test for function get_file_content
def test_get_file_content():
    path = '/tmp/test1.txt'
    text = 'this is a test\n'
    with open(path, 'w') as f:
        f.write(text)
    data = get_file_content(path)
    assert data == text
    data = get_file_content(path, strip=False)
    assert data == text + '\n'
    data = get_file_content(path, default='no data')
    assert data == text
    data = get_file_content('/tmp/does_not_exist', default='pytest')
    assert data == 'pytest'
    data = get_file_content('/tmp/does_not_exist', default='pytest', strip=False)
    assert data == 'pytest'

# Generated at 2022-06-13 03:48:21.968883
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content('/etc/hosts', default='test') == 'test'

# Generated at 2022-06-13 03:48:31.645231
# Unit test for function get_file_content
def test_get_file_content():
    try:
        os.remove('/tmp/test_get_file_content')
    except OSError:
        pass

    # Test that it returns default if file not found
    result = get_file_content('/tmp/test_get_file_content')
    assert result is None

    # Test that it returns default if file is not readable
    open('/tmp/test_get_file_content', 'w').close()
    result = get_file_content('/tmp/test_get_file_content')
    assert result is None

    # Test that it returns file contents if file is readable
    with open('/tmp/test_get_file_content', 'w') as f:
        f.write('foo')
    result = get_file_content('/tmp/test_get_file_content')

# Generated at 2022-06-13 03:48:40.405924
# Unit test for function get_file_content
def test_get_file_content():
    # Create a file
    try:
        # Enter file name
        file_name = input("Enter file name: ")

        # Enter file content
        print("Enter content. Press ctrl+d when finished.")
        content = ""
        while True:
            data = raw_input()
            content = content + data + "\n"
    except EOFError:
        pass

    # Open file and write content
    try:
        file_handle = open(file_name, 'w')
        file_handle.write(content)
        file_handle.close()
    except IOError:
        print("Error: Could not write to the file. Check the permissions.")
        # Abort
        exit()

    # get_file_content without stripping the newline character
    print("Results for get_file_content without stripping the newline character")


# Generated at 2022-06-13 03:48:45.454844
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content("/etc/issue") == get_file_content("/etc/issue", None, False)

    # Make sure we get the value set for default
    assert get_file_content("/etc/invalid_file_test_1234567890", "test") == "test"
    assert get_file_content("/etc/invalid_file_test_1234567890", "") == ""
    assert get_file_content("/etc/invalid_file_test_1234567890", None) is None

    # Test stripping of whitespace
    assert get_file_content("/etc/issue", None, False) != get_file_content("/etc/issue")
    assert get_file_content("/etc/issue", None, True) == get_file_content("/etc/issue")

# Generated at 2022-06-13 03:48:51.885443
# Unit test for function get_file_content
def test_get_file_content():
    # Test empty file
    assert get_file_content('/tmp/ansible-lint') is None

    # Test empty file
    assert get_file_content('/tmp/ansible-lint', default='test') == 'test'

    # Test not empty file
    with file('/tmp/ansible-lint', 'w') as f:
        f.write('test')

    assert get_file_content('/tmp/ansible-lint') == 'test'



# Generated at 2022-06-13 03:49:01.754583
# Unit test for function get_file_content
def test_get_file_content():
    import tempfile
    tmpdir = tempfile.gettempdir()
    tmpfile = tempfile.NamedTemporaryFile(dir=tmpdir)
    tmpfile.write("This is file content\n")
    tmpfile.seek(0)
    assert get_file_content(tmpfile.name) == 'This is file content'
    assert get_file_content(tmpfile.name, default=True) == True
    assert get_file_content(tmpfile.name, default=None, strip=False) == "This is file content\n"
    assert get_file_content(tmpfile.name, default=None, strip=True) == 'This is file content'
    assert get_file_content(tmpfile.name, default=False) == 'This is file content'
    tmpfile.close()


# Generated at 2022-06-13 03:49:06.113741
# Unit test for function get_file_content
def test_get_file_content():
    data_file = "/etc/passwd"
    default_data = "hi"
    assert get_file_content(data_file)
    assert get_file_content(data_file, default=default_data) != default_data
    assert get_file_content(data_file, strip=False)
    data_file = "/tmp/doesnotexist"
    assert get_file_content(data_file) == default_data


# Generated at 2022-06-13 03:49:09.878482
# Unit test for function get_file_content
def test_get_file_content():
    # With no file existing at the specified path, return None
    assert get_file_content('/dev/null/nothing', default=None) == None
    # With a readable file return the content
    assert get_file_content('/etc/passwd') == get_file_content('/etc/passwd', default='')
    assert get_file_content('/etc/passwd', strip=False) == get_file_content('/etc/passwd', default='', strip=False)



# Generated at 2022-06-13 03:49:24.200633
# Unit test for function get_file_content
def test_get_file_content():
    # Test existing file (./test.txt) with content
    existing_file = "./test.txt"
    existing_file_content = get_file_content(existing_file)
    assert existing_file_content == "First line for test"

    # Test existing file (./test.txt) with content
    existing_file = "./test.txt"
    existing_file_content = get_file_content(existing_file)
    assert existing_file_content == "First line for test"

    # Test not existing file
    not_existing_file = "./not_existing_file"
    not_existing_file_content = get_file_content(not_existing_file)
    assert not_existing_file_content is None

    # Test existing file (./test.txt) with content not accessible
    # (chmod -r)

# Generated at 2022-06-13 03:49:31.934116
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content('/etc/issue', None) == get_file_content('/etc/issue', None)
    assert get_file_content('/etc/issue', 'N/A') == get_file_content('/etc/issue', 'N/A')
    assert get_file_content('/etc/issue', 'default') != get_file_content('/etc/issue', 'N/A')
    assert get_file_content('/etc/issue', 'N/A') != get_file_content('/etc/issue2', 'N/A')
    assert get_file_content('/etc/issue.N/A', 'N/A') != get_file_content('/etc/issue', 'default')
    assert get_file_content('/etc/issue', 'default', False) == get_file_content

# Generated at 2022-06-13 03:49:34.292485
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content("/proc/meminfo") == get_file_content("/proc/meminfo", default=None, strip=True)



# Generated at 2022-06-13 03:49:41.447869
# Unit test for function get_file_content
def test_get_file_content():
    # The function get_file_content will return the content of "__file__" and will be compared with the content of
    # "__file__" read by reading the file
    assert os.path.exists("__file__")
    assert os.access("__file__", os.R_OK)
    curr_file_content = None
    with open("__file__") as f:
        for line in f:
            if curr_file_content == None:
                curr_file_content = ''
            curr_file_content += line
    curr_file_content = curr_file_content.strip()
    assert get_file_content("__file__", strip=True) == curr_file_content
    assert get_file_content("fake_file_name") == None
    assert get_file_content

# Generated at 2022-06-13 03:49:48.323053
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content('/dev/null') == ''
    assert get_file_content('/dev/zero') == ''
    assert get_file_content('/dev/zero', strip=False) == '\0' * 64
    # Test for an invalid file
    assert get_file_content('/nonexistent') == None
    assert get_file_content('/nonexistent', default='default') == 'default'



# Generated at 2022-06-13 03:49:57.006968
# Unit test for function get_file_content
def test_get_file_content():
    '''
    get_file_content unit test
    '''
    test_tmp_file = '/tmp/test_file_content'
    test_tmp_file_not_exist = '/tmp/file_does_not_exist'

    test_tmp_file_content = 'This is some content for unit testing'

    f = open(test_tmp_file, 'w')
    f.write(test_tmp_file_content)
    f.close()

    f = open(test_tmp_file, 'r')
    assert get_file_content(test_tmp_file, default='', strip=False) == test_tmp_file_content
    assert get_file_content(test_tmp_file, default='', strip=False) == f.read()
    assert get_file_content(test_tmp_file) == test

# Generated at 2022-06-13 03:50:06.654943
# Unit test for function get_file_content
def test_get_file_content():
    # the following tests are pure filename tests (ansible calls this module using only abspath and file name with no base dir)
    filemap = {
        '/tmp/test_get_file_content1': 'test_get_file_content1',
        '/tmp/test_get_file_content2': 'test_get_file_content2',
        '/tmp/test_get_file_content3': 'test_get_file_content3',
    }
    for test_file in filemap:
        with open(test_file, 'w') as f:
            f.write(filemap[test_file])
        assert get_file_content(test_file) == filemap[test_file]
        assert get_file_content(test_file, default='bad') == filemap[test_file]

# Generated at 2022-06-13 03:50:13.962477
# Unit test for function get_file_content
def test_get_file_content():
    content = 'Hello World'
    assert get_file_content('/bin/sh', 'no_file') == 'no_file'
    fh = open("/tmp/test_get_file_content", "w")
    fh.write(content)
    fh.close()
    assert get_file_content("/tmp/test_get_file_content") == content
    assert get_file_content("/tmp/test_get_file_content", "no_file") == content



# Generated at 2022-06-13 03:50:18.230278
# Unit test for function get_file_content
def test_get_file_content():
    test = get_file_content('/etc/resolv.conf', '# test')
    assert test.startswith('#')

    test = get_file_content('/etc/invalid_file', '# test')
    assert test.startswith('#')

    test = get_file_content('/etc/passwd', '# test')
    assert not test.startswith('#')



# Generated at 2022-06-13 03:50:21.985783
# Unit test for function get_file_content
def test_get_file_content():
    file_name = 'test_file'
    file_content = 'If the test succeed you should read this line'
    test_file = open(file_name, 'w')
    test_file.write(file_content)
    test_file.close()
    test_result = get_file_content(file_name)
    assert test_result == file_content
    os.remove(file_name)