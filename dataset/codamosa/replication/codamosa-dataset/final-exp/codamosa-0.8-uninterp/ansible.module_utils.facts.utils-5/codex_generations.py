

# Generated at 2022-06-13 03:43:56.661108
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content('/dev/null', 'default') == 'default'
    assert get_file_content('/dev/null', default='default') == 'default'
    assert get_file_content('/dev/zero') == ''
    assert get_file_content('/dev/zero', strip=False) == '\0'



# Generated at 2022-06-13 03:44:00.350652
# Unit test for function get_file_content
def test_get_file_content():
    # Test reading file, assert correct content and correct type
    assert get_file_content(os.path.join(os.path.dirname(__file__), '__init__.py')) == "from system_utils import *"


if __name__ == '__main__':
    test_get_file_content()

# Generated at 2022-06-13 03:44:09.098455
# Unit test for function get_file_lines
def test_get_file_lines():
    test_data = '''
hello world\n
foo bar
\n  \n
    fooooooo\n
        END
    '''
    assert get_file_lines('./invalid_file', strip=False) == []
    assert get_file_lines('./invalid_file', strip=True) == []

    assert get_file_lines('./invalid_file', strip=False, line_sep='\n') == []
    assert get_file_lines('./invalid_file', strip=True, line_sep='\n') == []

    # the file content is more than one line, but line_sep is only one character,
    # so the function will treat it as a separator rather than a line ending

# Generated at 2022-06-13 03:44:10.901772
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content("/etc/fstab")



# Generated at 2022-06-13 03:44:20.041715
# Unit test for function get_file_content
def test_get_file_content():
    from tempfile import NamedTemporaryFile

    test_file = NamedTemporaryFile()

    def get_content():
        with open(test_file.name, 'r') as f:
            return f.read()

    # check default value
    assert get_file_content(test_file.name, 'default') == 'default'

    # check contents
    content = 'hello world'
    with open(test_file.name, 'w') as f:
        f.write(content)
    assert get_file_content(test_file.name) == content

    # check empty content
    open(test_file.name, 'w').close()
    assert get_file_content(test_file.name) == ''

    test_file.close()

# Generated at 2022-06-13 03:44:26.471800
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content('/proc/mounts')
    assert not get_file_content('/proc/mounts', default='')
    assert get_file_content('/proc/meminfo')
    assert get_file_content('/proc/meminfo', strip=False)
    assert not get_file_content('/proc/meminfo', default='', strip=False)
    assert get_file_content('/etc/mtab')
    assert get_file_content('/etc/mtab', strip=False)
    assert not get_file_content('/etc/mtab', default='', strip=False)

# Generated at 2022-06-13 03:44:34.825962
# Unit test for function get_file_content
def test_get_file_content():
    assert get_file_content(path="tests/unit/module_utils/test_file.txt", default=None) == "test_file"
    assert get_file_content(path="tests/unit/module_utils/test_file.txt", default=None, strip=False) == "test_file\n"
    assert get_file_content(path="tests/unit/module_utils/test_file.txt", default="should_be_default") == "test_file"
    assert get_file_content(path="tests/unit/module_utils/test_file.txt", default="should_be_default", strip=False) == "test_file\n"

# Generated at 2022-06-13 03:44:45.324975
# Unit test for function get_file_lines
def test_get_file_lines():
    '''unit tests for get_file_lines'''
    f1 = '/tmp/f1'
    f2 = '/tmp/f2'
    f3 = '/tmp/f3'
    f4 = '/tmp/f4'

# Generated at 2022-06-13 03:44:56.986958
# Unit test for function get_file_lines
def test_get_file_lines():
    test_path = '/tmp/test_ansible_file_path.txt'
    test_data = 'first\nsecond\nthird\n'

# Generated at 2022-06-13 03:45:08.468559
# Unit test for function get_file_content
def test_get_file_content():
    ''' test that it returns the contents of a file '''
    # 'default' value will be returned
    assert get_file_content('/no/file/here') == None

    # file with default values (will be stripped)
    assert get_file_content('/etc/hosts') == '127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4'
    assert get_file_content('/etc/hosts', default='localhost') == 'localhost'

    # test that we can return the data with no stripping