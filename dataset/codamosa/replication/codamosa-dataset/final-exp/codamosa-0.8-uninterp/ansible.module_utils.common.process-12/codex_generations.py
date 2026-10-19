

# Generated at 2022-06-12 23:27:47.778749
# Unit test for function get_bin_path
def test_get_bin_path():
    import os
    import sys
    import tempfile
    import shutil
    import subprocess

    parent_dir = tempfile.mkdtemp()
    # Create executable file in temporary directory
    script_path = parent_dir + '/executable'
    with open(script_path, 'w') as f:
        f.write('#!/bin/sh\n')
        f.write('printf "%%s" "Test"' + os.linesep)

    os.chmod(script_path, 0o775)

# Generated at 2022-06-12 23:27:52.611932
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path("sh") == "/bin/sh"
    assert get_bin_path("sh", opt_dirs=["/bin", "/usr/bin"]) == "/bin/sh"

    try:
        get_bin_path("invalid_bin_path", opt_dirs=["/bin", "/usr/bin"])
        assert False, "invalid_bin_path should not be found"
    except ValueError:
        pass

# Generated at 2022-06-12 23:27:55.442657
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path("sh") == '/bin/sh'
    assert get_bin_path("sh", ["/tmp", "/dev"]) == '/bin/sh'
    assert get_bin_path("sh", ["/tmp", "/dev"], True) == '/bin/sh'

# Generated at 2022-06-12 23:27:56.829753
# Unit test for function get_bin_path
def test_get_bin_path():
    path = get_bin_path('sh')
    assert(path == '/bin/sh')


# Generated at 2022-06-12 23:28:03.376343
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test 1: Try to find the executable "sh", this should be successful
    bin_path = get_bin_path("sh")
    # Test 2: Try to find an non existing executable "foo".
    #         An exception should be raised
    try:
        bin_path = get_bin_path("foo")
    except ValueError:
        pass
    else:
        assert False, "get_bin_path should have raised an exception"
    # Test 3: Try to find the executable "sh" in the directory /bin
    bin_path = get_bin_path("sh", opt_dirs=["/bin"])
    # Test 4: Try to find the executable "sh" in the directory /bin and /usr/bin

# Generated at 2022-06-12 23:28:10.807746
# Unit test for function get_bin_path
def test_get_bin_path():
    paths = ['/bin', '/usr/bin', '/usr/local/bin']
    assert get_bin_path('sh', paths, True) == '/bin/sh'
    paths = ['/bin', '/usr/bin', '/usr/local/bin']
    assert get_bin_path('sh', paths) == '/bin/sh'
    paths = ['/bin', '/usr/bin', '/usr/local/bin']
    assert get_bin_path('sh', '/bin') == '/bin/sh'
    paths = ['/bin', '/usr/bin', '/usr/local/bin']
    assert get_bin_path('sh') == '/bin/sh'

# Generated at 2022-06-12 23:28:14.892010
# Unit test for function get_bin_path
def test_get_bin_path():
    supported_bin_names = ['ansible', 'ansible-playbook', 'ansible-vault']
    for bin_name in supported_bin_names:
        bin_path = get_bin_path(bin_name)
        assert os.path.exists(bin_path), "Could not find %s" % bin_path

# Generated at 2022-06-12 23:28:24.003288
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil

    paths = []

# Generated at 2022-06-12 23:28:30.864178
# Unit test for function get_bin_path
def test_get_bin_path():
    import sys
    import tempfile


# Generated at 2022-06-12 23:28:36.034246
# Unit test for function get_bin_path
def test_get_bin_path():
    # Point to existing commands
    assert get_bin_path('/bin/true') == '/bin/true'
    assert get_bin_path('which') == '/usr/bin/which'

    # Point to non-existing commands
    try:
        get_bin_path('/bin/notexists')
    except ValueError:
        pass

    try:
        get_bin_path('notexists')
    except ValueError:
        pass

# Generated at 2022-06-12 23:28:41.404993
# Unit test for function get_bin_path
def test_get_bin_path():

    path = get_bin_path('python')
    assert path is not None

# Generated at 2022-06-12 23:28:49.324945
# Unit test for function get_bin_path
def test_get_bin_path():
    path = get_bin_path('ls')
    assert is_executable(path)
    try:
        get_bin_path('nonexistent_command')
        assert False, 'Expect ValueError if required executable is not found'
    except ValueError:
        pass
    opt_dirs = ['/usr/bin']
    path = get_bin_path('ls', opt_dirs)
    assert is_executable(path)
    try:
        get_bin_path('nonexistent_command', opt_dirs)
        assert False, 'Expect ValueError if required executable is not found'
    except ValueError:
        pass



# Generated at 2022-06-12 23:28:55.134538
# Unit test for function get_bin_path
def test_get_bin_path():
    from ansible_module_utils.common.file import md5
    test_path = os.path.realpath(os.path.join(os.getcwd(), "./test/support/ansible-test"))
    assert test_path == get_bin_path("ansible-test", opt_dirs=['test/support'])
    assert test_path == get_bin_path("/test/support/ansible-test")
    assert md5(test_path) == md5(get_bin_path("ansible-test", opt_dirs=['/test/support']))
    # test that PATH is searched and works regardless of whether /sbin is included in original PATH or not
    if "/sbin" not in os.environ['PATH']:
        os.environ['PATH'] += ':/sbin'
    assert md

# Generated at 2022-06-12 23:29:05.811413
# Unit test for function get_bin_path
def test_get_bin_path():
    import sys

    if sys.platform.startswith('freebsd'):
        BIN = "ping"
    else:
        BIN = "ping6"

    # Test 1 - if binary is on path, return full path
    assert get_bin_path(BIN)

    # Test 2 - if binary is not on path, return None
    try:
        get_bin_path("foo")
    except ValueError:
        assert 1
    else:
        assert 0

    # Test 3 - if binary is on optional path given, return full path
    if sys.platform.startswith('freebsd'):
        assert get_bin_path(BIN, opt_dirs=['/usr/bin'], required=True) == '/usr/bin/ping'

# Generated at 2022-06-12 23:29:13.360623
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Sometimes we cannot predict the output of get_bin_path
    because that depends on where the test is running.
    '''
    assert any([os.path.exists(get_bin_path('echo'))])
    assert any([os.path.exists(get_bin_path('echo', opt_dirs=['/bin', '/usr/bin']))])
    assert any([os.path.exists(get_bin_path('grep', ['/bin', '/usr/bin']))])
    assert any([os.path.exists(get_bin_path('wc', opt_dirs=['/bin', '/usr/bin']))])


# --- Ansible module utils.py tests below ---
import ansible.module_utils.basic
import ansible.module_utils.facts



# Generated at 2022-06-12 23:29:21.791452
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Test function get_bin_path
    '''
    assert get_bin_path('sh') == '/bin/sh'
    assert get_bin_path('sh', ['/bin']) == '/bin/sh'
    assert get_bin_path('sh', ['/usr/bin']) == '/usr/bin/sh'
    assert get_bin_path('sh', ['/bin', '/usr/bin', '/sbin']) == '/bin/sh'
    assert get_bin_path('sh', ['/usr/bin', '/bin', '/sbin']) == '/bin/sh'
    assert get_bin_path('sh', ['/sbin', '/bin', '/usr/bin']) == '/bin/sh'
    assert get_bin_path('sh', ['/sbin', '/usr/bin', '/bin'])

# Generated at 2022-06-12 23:29:25.877116
# Unit test for function get_bin_path
def test_get_bin_path():
    arg = 'ansible-playbook'
    bin_path = get_bin_path(arg)
    assert(bin_path == '/usr/bin/ansible-playbook')

# Generated at 2022-06-12 23:29:31.696495
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('ansible-console')
    assert get_bin_path('ansible-console', opt_dirs=[os.getcwd()])
    assert get_bin_path('ansible-console', opt_dirs=[os.getcwd(), '/usr/bin', '/usr/sbin'])
    try:
        get_bin_path('ansible-consolexxx')
    except ValueError:
        assert True
    else:
        assert False

# Generated at 2022-06-12 23:29:35.815297
# Unit test for function get_bin_path
def test_get_bin_path():
    bp = get_bin_path('sh')
    assert bp is not None

    try:
        get_bin_path('this_should_not_exist')
        assert False
    except ValueError:
        assert True

# Generated at 2022-06-12 23:29:45.714134
# Unit test for function get_bin_path
def test_get_bin_path():
    # define a list of dirs with non-existing dir and executable
    non_existing_dir = "/xyz"
    non_existing_file = "/xyz/abc"
    existing_exec = "/bin/sh"
    # define alternate PATH
    alternate_path = "/tmp/abc:/tmp/xyz"
    # Create a list of lists of directories
    # each element of the list will be a list of directories, separated by a ":"
    # the first element in the list will be default PATH
    # the second element will be PATH with a non-exisiting directory
    # the third element will be alternate PATH
    dir_list = []
    dir_list.append(os.environ.get('PATH', '').split(os.pathsep))
    tmp = os.environ.get('PATH', '') + os.pathsep

# Generated at 2022-06-12 23:29:56.810191
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil

    def makeTempBinDir():
        tmp = tempfile.mkdtemp()
        bin_dir = os.path.join(tmp, 'bin')
        os.mkdir(bin_dir)
        return bin_dir


# Generated at 2022-06-12 23:30:08.132080
# Unit test for function get_bin_path
def test_get_bin_path():
    a_path = get_bin_path('ansible-doc')
    assert a_path.startswith('/')  # path starts with a /
    assert a_path.endswith('ansible-doc')  # path should end with ansible-doc
    assert os.path.isfile(a_path)  # path should refer to an existing file
    assert os.access(a_path, os.X_OK)  # file should be executable

    # find ansible-doc in a specific directory
    a_path = get_bin_path('ansible-doc', opt_dirs=['/usr/bin'])
    assert a_path.startswith('/usr/bin')  # path starts with /usr/bin
    assert a_path.endswith('ansible-doc')  # path should end with ansible-

# Generated at 2022-06-12 23:30:10.856194
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('cat') == '/bin/cat'
    import pytest
    with pytest.raises(ValueError):
        get_bin_path('this_binary_does_not_exist')

# Generated at 2022-06-12 23:30:22.211768
# Unit test for function get_bin_path
def test_get_bin_path():
    found = get_bin_path('pwd', opt_dirs=['/bin'])
    assert found == '/bin/pwd'
    try:
        get_bin_path('nonexistent_executable')
    except Exception as e:
        assert str(e) == 'Failed to find required executable "nonexistent_executable" in paths: /bin:/usr/bin:/usr/local/bin:/usr/sbin:/usr/local/sbin:/sbin'
    try:
        get_bin_path('nonexistent_executable', opt_dirs=['/usr/bin'])
    except Exception as e:
        assert str(e) == 'Failed to find required executable "nonexistent_executable" in paths: /usr/bin:/bin:/usr/sbin:/usr/local/sbin:/sbin'

# Generated at 2022-06-12 23:30:23.504771
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path("env")



# Generated at 2022-06-12 23:30:29.834059
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Function to test get_bin_path with
    command 'file' on linux and 'file.exe'
    on Windows platform
    '''
    import platform
    import sys

    if platform.system().lower() == 'windows':
        bin_ = 'file.exe'
    else:
        bin_ = 'file'

    try:
        get_bin_path(bin_)
    except ValueError as e:
        sys.exit(1)


if __name__ == '__main__':
    test_get_bin_path()

# Generated at 2022-06-12 23:30:40.909486
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        from nose.tools import assert_equals
    except:
        print('Please install "nose" to run unit tests')

    # Testing with a non-existing executable
    #  get_bin_path
    try:
        get_bin_path('invalid_executable_that_does_not_exist')
        assert False, 'Expected an exception to be thrown'
    except ValueError:
        pass

    # Testing with a valid executable
    #  get_bin_path
    assert_equals(get_bin_path('ls'), '/bin/ls')

    # Testing with a valid executable in an alternate path
    #  get_bin_path
    assert_equals(get_bin_path('ls', opt_dirs=['/usr/bin', '/bin']), '/bin/ls')


# Generated at 2022-06-12 23:30:49.170918
# Unit test for function get_bin_path
def test_get_bin_path():

    get_bin_path('/bin/sh')  # absolute path
    get_bin_path('sh')  # path relative to /bin
    get_bin_path('sh', opt_dirs=['/'])  # path relative to root
    get_bin_path('sh', opt_dirs=['/tmp'])  # path relative to /tmp
    get_bin_path('sh', opt_dirs=['/bin', '/usr/bin'])  # path is relative to either /bin or /usr/bin
    get_bin_path('sh', opt_dirs=['/bin', '/usr/bin'])  # path relative to /bin, with /bin in PATH
    get_bin_path('sh', opt_dirs=['/tmp/noexists'])  # path relative to non-existant dir raises ValueError

# Generated at 2022-06-12 23:30:50.440464
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        path = get_bin_path('ls')
        assert(path != None)
    except ValueError:
        assert(False)

# Generated at 2022-06-12 23:30:57.463024
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Test get_bin_path function
    '''

    # Test exception thrown if command is not found
    try:
        arg = 'foo'
        get_bin_path(arg)
        assert 0, 'Failed to test get_bin_path'
    except ValueError:
        pass

    # Test base case
    arg = 'ls'
    bin_path = get_bin_path(arg)
    assert bin_path == '/bin/ls', 'Failed to test get_bin_path'

# Generated at 2022-06-12 23:31:10.112954
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test for correct return value
    # Select a command which should be found in a PATH
    bin_path = get_bin_path('ls')

    # Check that the return value is a string, and that the command
    # given as argument is in the return path.
    assert(isinstance(bin_path, str))
    assert('ls' in bin_path)

    # Test for command not found in PATH
    # Select a command which should not be found in a PATH
    result = False
    try:
        get_bin_path('ls_not_found')
    except ValueError:
        result = True
    assert(result)

    # Test for command found through an optional directory
    # Select a command which should not be found in PATH, but which
    # exists in an optional directory
    result = False

# Generated at 2022-06-12 23:31:19.137524
# Unit test for function get_bin_path
def test_get_bin_path():
    # Create a temporary directory/file for testing
    import tempfile
    tmp_dir_path = tempfile.mkdtemp()
    tmp_file_path = os.path.join(tmp_dir_path, 'bin')
    tmp_file = open(tmp_file_path, 'w')
    tmp_file.close()

    # Test the function
    import os
    file_name = 'date'
    path_list = ['/usr/bin', '/bin']
    os.environ['PATH'] = os.pathsep.join(path_list)
    assert os.path.join(path_list[0], file_name) == get_bin_path(file_name)
    path_list.insert(0, tmp_dir_path)

# Generated at 2022-06-12 23:31:26.301521
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path('/bin/ls')
        assert False, "Expected an exception"
    except ValueError:
        pass
    assert get_bin_path('ls') == '/bin/ls'
    assert get_bin_path('ls', opt_dirs = ['/bin', '/usr/bin']) == '/bin/ls'
    assert get_bin_path('ls', opt_dirs = ['/usr/bin', '/bin']) == '/bin/ls'
    assert get_bin_path('ls', opt_dirs = ['/bin', '/bin']) == '/bin/ls'
    assert get_bin_path('ls', opt_dirs = ['/sbin']) == '/sbin/ls'

# Generated at 2022-06-12 23:31:29.270094
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('ip') == get_bin_path('ip')
    assert get_bin_path('ip') != get_bin_path('ping')



# Generated at 2022-06-12 23:31:37.322801
# Unit test for function get_bin_path
def test_get_bin_path():
    import errno
    import shutil
    try:
        tmp_path = '/tmp/test_get_bin_path'
        os.mkdir(tmp_path)
        test_file = os.path.join(tmp_path, 'test_file')
        with open(test_file, 'w') as f:
            f.write('Test')
        os.chmod(test_file, 0o755)
        assert get_bin_path('test_file', opt_dirs=[tmp_path]) == test_file
        shutil.rmtree(tmp_path)
    except OSError as e:
        if e.errno != errno.ENOENT:
            raise
    # test failure

# Generated at 2022-06-12 23:31:47.327499
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Test case for function get_bin_path.
    '''
    import tempfile
    import shutil
    import stat
    import sys
    # create a temporary directory
    tmp_dir = tempfile.mkdtemp()
    # create a simple script that returns the current environment variables
    script_name = 'test_env'
    script_path = os.path.join(tmp_dir, script_name)
    with open(script_path, 'w') as script:
        script.write('#!/bin/sh\n/usr/bin/env\n')
    # make it executable
    os.chmod(script_path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR)
    # get the path
    os.environ['PATH'] = tmp_dir

# Generated at 2022-06-12 23:31:57.177475
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('sh') == get_bin_path('sh')
    assert get_bin_path('sh', ['/usr/bin']) == get_bin_path('sh', ['/usr/bin'])
    assert get_bin_path('sh', ['/usr/bin']) != get_bin_path('sh', ['/bin'])
    assert get_bin_path('sh', ['/bin']) != get_bin_path('sh', ['/usr/bin'])
    assert get_bin_path('sh', ['/bin']) == get_bin_path('sh', ['/bin'])
    assert get_bin_path('sh', ['/bin']) == get_bin_path('sh')

# Generated at 2022-06-12 23:32:07.178133
# Unit test for function get_bin_path
def test_get_bin_path():
    test_dir = '/tmp/ansible_test_dir'
    test_file = 'test_get_bin_path'
    file_path = os.path.join(test_dir, test_file)
    with open(file_path, 'w') as f:
        f.write('#!/bin/bash')
    # chmod the test file so it is executable
    os.chmod(file_path, 0o777)
    assert os.path.exists(file_path)
    assert os.path.isdir(file_path) is False
    assert is_executable(file_path) is True
    # Test that the test file exists in the supplied directory
    bin_path = get_bin_path(test_file, opt_dirs=[test_dir], required=True)
    assert bin_path == file_

# Generated at 2022-06-12 23:32:15.656808
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path('nonexistent')
        assert False
    except ValueError:
        pass
    try:
        get_bin_path('nonexistent', required=True)
        assert False
    except ValueError:
        pass
    try:
        get_bin_path('nonexistent', required=False)
        assert False
    except ValueError:
        pass
    try:
        get_bin_path('nonexistent', opt_dirs=['/bin'])
        assert False
    except ValueError:
        pass
    assert get_bin_path('cd') == '/bin/cd'
    assert get_bin_path('cd', opt_dirs=['/']) == '/cd'

# Generated at 2022-06-12 23:32:22.079445
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path('doesnotexist')
        assert False, 'get_bin_path expected to raise ValueError exception'
    except ValueError:
        pass

    try:
        get_bin_path('python2.7', required=False)
        assert False, 'get_bin_path expected to raise ValueError exception'
    except ValueError:
        pass

# Generated at 2022-06-12 23:32:28.030069
# Unit test for function get_bin_path
def test_get_bin_path():
    """
    Test to see if we can find a binary in one of the system paths.
    The test will fail if the default for bin_path is None
    """
    assert get_bin_path('python') is not None



# Generated at 2022-06-12 23:32:39.512144
# Unit test for function get_bin_path
def test_get_bin_path():
    get_bin_path('ls', ['/bin', '/usr/bin'])
    get_bin_path('ls', opt_dirs=None)
    get_bin_path('ls', '/bin')

    try:
        get_bin_path('bad_executable')
        assert False, 'Should fail with ValueError'
    except ValueError as e:
        assert 'Failed to find required executable' in str(e)

    try:
        get_bin_path('bad_executable', required=True)
        assert False, 'Should fail with ValueError'
    except ValueError as e:
        assert 'Failed to find required executable' in str(e)


# Generated at 2022-06-12 23:32:50.886162
# Unit test for function get_bin_path
def test_get_bin_path():
    # Normal case: get_bin_path('cat') should return a valid path
    assert get_bin_path('cat')
    # Normal case: get_bin_path('which') should return a valid path
    assert get_bin_path('which')
    # Normal case: get_bin_path('cat', opt_dirs=['/usr/local']) should return the existing path
    assert get_bin_path('cat', opt_dirs=['/usr/local']) == '/usr/local/bin/cat'
    # Exception case: get_bin_path('invalid_bin') should raise a ValueError
    try:
        get_bin_path('invalid_bin')
    except ValueError:
        assert True
    # Exception case: get_bin_path('cat', opt_dirs=['/usr/local']) should

# Generated at 2022-06-12 23:33:00.616047
# Unit test for function get_bin_path
def test_get_bin_path():
    from ansible import errors

    try:
        get_bin_path('non_existent_executable', required=False)
    except errors.AnsibleError as e:
        assert "Failed to find required executable 'non_existent_executable'" in str(e)
    else:
        assert False, "Failed to raise exception"

    try:
        get_bin_path('non_existent_executable', required=True)
    except errors.AnsibleError as e:
        assert "Failed to find required executable 'non_existent_executable'" in str(e)
    else:
        assert False, "Failed to raise exception"


# Generated at 2022-06-12 23:33:05.561971
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('ls') == '/bin/ls'
    assert get_bin_path('ls', ['/tmp']) == '/bin/ls'
    assert get_bin_path('ls', ['/tmp'], ['/bin', '/usr/bin']) == '/bin/ls'

# Generated at 2022-06-12 23:33:10.005026
# Unit test for function get_bin_path
def test_get_bin_path():
    from ansible.module_utils.basic import AnsibleModule

    assert get_bin_path('/bin/true') == '/bin/true'
    assert get_bin_path('/bin/true', opt_dirs=['/bin']) == '/bin/true'
    assert get_bin_path('/bin/true', opt_dirs=['/var/bin']) == '/bin/true'

    try:
        get_bin_path('/bin/doesnotexist')
        assert False
    except ValueError:
        assert True

    assert get_bin_path('/usr/bin/python') == '/usr/bin/python'
    assert get_bin_path('python') == '/usr/bin/python'

    # Check that '/sbin', '/usr/sbin is in PATH if it exists
    module = AnsibleModule

# Generated at 2022-06-12 23:33:19.076393
# Unit test for function get_bin_path
def test_get_bin_path():
    # Verify get_bin_path() and search order
    assert get_bin_path('/bin/cp') == '/bin/cp'
    assert get_bin_path('cp') == get_bin_path('cp', opt_dirs=['/bin'])
    assert get_bin_path('cp') == get_bin_path('cp', opt_dirs=['/bin/'])
    assert get_bin_path('cp') == get_bin_path('cp', opt_dirs=['/bin', '/usr/bin'])
    assert get_bin_path('cp') == get_bin_path('cp', opt_dirs=['/bin/', '/usr/bin'])

# Generated at 2022-06-12 23:33:29.989187
# Unit test for function get_bin_path
def test_get_bin_path():
    import random
    import tempfile
    import shutil
    tmpdir = tempfile.mkdtemp()
    bin_path = os.path.join(tmpdir, 'bin')
    os.mkdir(bin_path)
    script = os.path.join(bin_path, 'script')
    with open(script, 'w') as f:
        f.write("#!/usr/bin/env python\nimport sys\nprint sys.argv[2]\n")
    os.chmod(script, 0o755)
    test_args = [str(random.randint(0, 1000)) for _ in range(3)]

# Generated at 2022-06-12 23:33:39.708709
# Unit test for function get_bin_path
def test_get_bin_path():
    # python 2.6 does not have assertRaisesRegexp
    if not hasattr(__builtins__, 'assertRaisesRegexp'):
        import re
        def assertRaisesRegexp(exception, regexp, callable, *args, **kwargs):
            try:
                callable(*args, **kwargs)
            except exception:
                if re.search(regexp, str(exception)):
                    pass
                else:
                    raise AssertionError("%r !~ %r" % (str(exception), regexp))
            else:
                raise AssertionError("%r was not raised" % exception.__name__)
        __builtins__.assertRaisesRegexp = assertRaisesRegexp

    assert get_bin_path('ls') == '/bin/ls'
   

# Generated at 2022-06-12 23:33:44.916660
# Unit test for function get_bin_path
def test_get_bin_path():
    path = get_bin_path('ls')
    assert path.endswith('ls')
    try:
        path = get_bin_path('python')
        assert path.endswith('python')
    except ValueError as e:
        assert 'requires Python 2.7' in str(e)

# Generated at 2022-06-12 23:33:53.279215
# Unit test for function get_bin_path
def test_get_bin_path():

    get_bin_path('/usr/bin/python')
    get_bin_path('python')
    get_bin_path('python2')
    get_bin_path('python2.7')
    get_bin_path('python3')

    # this should fail
    try:
        get_bin_path('python_not_found')
    except ValueError as e:
        pass
    else:
        raise Exception('get_bin_path failed to raise an exception')

# Generated at 2022-06-12 23:34:03.314365
# Unit test for function get_bin_path
def test_get_bin_path():
    ''' This is a unit test for ansible.module_utils.basic.get_bin_path()'''
    try:
        # Using 'python' should succeed on all platforms
        if is_executable(get_bin_path('python')):
            print("TEST PASSED")
            return 0
        else:
            print("TEST FAILED: 'python' is not executable")
    except ValueError as e:
        print("TEST FAILED: get_bin_path() threw ValueError: %s " % e)
    return 1

if __name__ == '__main__':
    import sys
    sys.exit(test_get_bin_path())

# Generated at 2022-06-12 23:34:10.556228
# Unit test for function get_bin_path
def test_get_bin_path():
    import sys
    import tempfile

    if sys.version_info >= (3, 0):
        from unittest.mock import patch
    else:
        from mock import patch

    with patch('ansible.module_utils.basic.file.is_executable', return_value=True):
        assert get_bin_path('python') == os.path.realpath('/usr/bin/python')

    with patch('ansible.module_utils.basic.file.is_executable', return_value=False):
        try:
            get_bin_path('python')
            raise AssertionError('Expected a ValueError to be raised.')
        except ValueError:
            pass


# Generated at 2022-06-12 23:34:17.799345
# Unit test for function get_bin_path
def test_get_bin_path():
    exe_path = get_bin_path('python')
    assert os.path.exists(exe_path)
    assert not os.path.isdir(exe_path)
    assert is_executable(exe_path)
    assert exe_path.endswith('python')

    # test opt_dirs
    opt_dirs = [os.path.dirname(exe_path)]
    assert get_bin_path('echo', opt_dirs=opt_dirs).endswith('echo')

    # test exception
    try:
        get_bin_path('doesnotexists')
        assert False
    except ValueError as e:
        assert str(e).startswith('Failed to find required executable "doesnotexists"')

# Generated at 2022-06-12 23:34:23.196699
# Unit test for function get_bin_path
def test_get_bin_path():
    arg = 'ls'
    binary = get_bin_path(arg, ['/bin', '/usr/bin'])
    assert binary == '/bin/ls'

    arg = 'chmod'
    binary = get_bin_path(arg, ['/bin', '/usr/bin'])
    assert binary == '/bin/chmod'

# Generated at 2022-06-12 23:34:31.543552
# Unit test for function get_bin_path
def test_get_bin_path():
    def exec_mock(path):
        return path in ['path1/exec1', 'path2/exec2', 'exec3']

    # Using __builtin__ function as module_utils.common.file.is_executable is a mocker object
    original = __builtin__.is_executable
    __builtin__.is_executable = exec_mock

    # Using os.environ.get as os.environ is a mocker object
    original_env = os.environ.get
    os.environ.get = lambda x: 'path1:path2'

    # Using os.path.exists as os.path is a mocker object
    original_path_exists = os.path.exists

# Generated at 2022-06-12 23:34:36.251873
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('python') == '/usr/bin/python'
    assert get_bin_path('python', ['/usr/bin']) == '/usr/bin/python'
    assert get_bin_path('python', ['/usr/bin'], True) == '/usr/bin/python'

# Generated at 2022-06-12 23:34:41.118877
# Unit test for function get_bin_path
def test_get_bin_path():
    # Required = None
    get_bin_path("echo")
    try:
        get_bin_path("invalid_command")
        assert False
    except ValueError:
        assert True

    # Required = False
    get_bin_path("invalid_command", required=False)

    # Required = True
    try:
        get_bin_path("invalid_command", required=True)
        assert False
    except ValueError:
        assert True

# Generated at 2022-06-12 23:34:46.428516
# Unit test for function get_bin_path
def test_get_bin_path():
    os.environ['PATH'] = '/usr/bin:/usr/sbin:/bin:/sbin'
    assert get_bin_path('sh') == '/bin/sh'
    assert get_bin_path('/bin/sh') == '/bin/sh'
    assert get_bin_path('/usr/bin/sh') == '/usr/bin/sh'
    assert get_bin_path('/usr/sbin/useradd') == '/usr/sbin/useradd'
    try:
        get_bin_path('dummy')
    except ValueError:
        pass
    else:
        raise Exception('get_bin_path failed to raise exception when not finding the binary')



# Generated at 2022-06-12 23:34:55.531026
# Unit test for function get_bin_path
def test_get_bin_path():
    ''' Test get_bin_path() '''
    # Setup mocks
    import __builtin__
    import os
    import tempfile
    from ansible.module_utils.six import PY3
    from shutil import which

    os_environ_orig = os.environ
    __builtin__.open = lambda path: open(path, 'w')
    tempdir = tempfile.mkdtemp()
    os.environ["PATH"] = ':'.join([os.path.dirname(which('ls')), tempdir])

    # Test get_bin_path()
    if PY3:
        import io

# Generated at 2022-06-12 23:35:04.303176
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path('does_not_exist')
    except ValueError:
        pass
    else:
        assert False, 'get_bin_path: function did not raise ValueError'

    try:
        get_bin_path('python')
    except ValueError:
        assert False, 'get_bin_path: function raised ValueError'

# Generated at 2022-06-12 23:35:11.482921
# Unit test for function get_bin_path
def test_get_bin_path():
    import shutil
    import tempfile
    from ansible.module_utils._text import to_bytes

    test_dir = tempfile.mkdtemp()
    null_path = to_bytes(os.devnull)

    # Placeholder files in test_dir, with mode 755
    open(os.path.join(test_dir, 'test_file'), 'w').close()

# Generated at 2022-06-12 23:35:18.486052
# Unit test for function get_bin_path
def test_get_bin_path():
    test_path = '/usr/bin/'
    test_path1 = '/usr/bin'
    test_path2 = '/usr/sbin'
    test_paths = [test_path, test_path1, test_path2]
    test_arg = "ls"
    path = get_bin_path(test_arg, test_paths)
    assert path == os.path.join(test_path, test_arg)

# Generated at 2022-06-12 23:35:29.982425
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil
    temp_dir = tempfile.mkdtemp()
    test_file = 'test_file'
    test_path = os.path.join(temp_dir, test_file)
    open(test_path, 'w').close()
    os.chmod(test_path, 0o755)

    shutil.rmtree(temp_dir)
    assert get_bin_path('dummy_file_1234', [temp_dir]) == test_path
    assert get_bin_path('dummy_file_1234', [temp_dir], None) == test_path

    # test it raises ValueError

# Generated at 2022-06-12 23:35:37.641058
# Unit test for function get_bin_path
def test_get_bin_path():

    # Test for valid path
    expected_bin_path = '/usr/bin/python2'
    actual_bin_path = get_bin_path('python2')
    assert expected_bin_path == actual_bin_path

    # Test for invalid path
    expected_bin_path = None
    try:
        actual_bin_path = get_bin_path('python3')
    except ValueError:
        actual_bin_path = None
    assert expected_bin_path == actual_bin_path

# Generated at 2022-06-12 23:35:47.697709
# Unit test for function get_bin_path
def test_get_bin_path():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict(
            cmd=dict(type='path', required=True),
            path=dict(type='path', required=True),
        ),
    )

    try:
        get_bin_path('not-a-real-executable')
        assert False
    except ValueError as e:
        assert 'Failed to find required executable "not-a-real-executable"' in str(e)

    # Test that the module fails appropriately when invoked with an invalid path
    module.params['cmd'] = 'not-a-real-executable'
    result = module.run_command(module.params['cmd'], check_rc=False)
    assert result[0] != 0

    # Test that the module passes with a valid

# Generated at 2022-06-12 23:36:00.112245
# Unit test for function get_bin_path
def test_get_bin_path():
    """
    Test locating python3 and python3.5 under various conditions
    """
    import shutil
    import tempfile

    class FakePATH(object):
        paths = []
        fake_path_str = None

        def set_paths(self, paths):
            self.paths = paths
            self.fake_path_str = os.path.pathsep.join(paths)

        def __getitem__(self, item):
            return self.fake_path_str

        def __setitem__(self, key, value):
            self.fake_path_str = value

    def tempdir():
        d = tempfile.mkdtemp()
        FakePATH.paths.append(d)
        return d

    def tempfilepath(name, d):
        path = os.path.join(d, name)

# Generated at 2022-06-12 23:36:11.215188
# Unit test for function get_bin_path
def test_get_bin_path():
    paths = ['/bin', '/usr/bin', '/usr/local/bin']
    sbin_paths = ['/sbin', '/usr/sbin', '/usr/local/sbin']
    os.environ['PATH'] = ':'.join(paths)

    bin_path = get_bin_path('ls', opt_dirs=sbin_paths.copy())
    assert bin_path == '/bin/ls'

    # add sbin dirs to PATH
    sbin_paths.extend(paths)
    os.environ['PATH'] = ':'.join(sbin_paths)
    bin_path = get_bin_path('ls')
    assert bin_path == '/bin/ls'


# Generated at 2022-06-12 23:36:17.440673
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path('doesnotexist')
        assert False, 'expected ValueError'
    except ValueError:
        pass

    # PATH is not modified
    oldpath = os.environ.get('PATH')
    try:
        get_bin_path('ls')
        get_bin_path('ls')
    finally:
        if oldpath:
            os.environ['PATH'] = oldpath

# Generated at 2022-06-12 23:36:26.044665
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Test get_bin_path. Note that whether a file is found or not depends on
    the environment and whether it is mocked out.
    '''
    current_dir = os.path.dirname(os.path.abspath(__file__))
    mock_dir = os.path.join(current_dir, 'mock_dir')

    # PATH=/bin:/usr/bin
    mock_env = {'PATH': '/bin:/usr/bin'}
    # Check for /bin/sh
    bin_path = get_bin_path('sh', required=False, env=mock_env)
    assert bin_path == '/bin/sh'
    # Check for non-existing /usr/bin/sh

# Generated at 2022-06-12 23:36:45.503615
# Unit test for function get_bin_path
def test_get_bin_path():

    try:
        get_bin_path('foobar')
        assert False
    except ValueError:
        assert True

    try:
        get_bin_path('foobar', [])
        assert False
    except ValueError:
        assert True

    try:
        get_bin_path('foobar', ['foo'])
        assert False
    except ValueError:
        assert True

    os.environ['PATH'] = 'foo'
    try:
        get_bin_path('foobar')
        assert False
    except ValueError:
        assert True

    os.environ['PATH'] = os.pathsep.join(['foo', '/sbin', 'bin'])
    assert get_bin_path('ping') == '/bin/ping'

# Generated at 2022-06-12 23:36:51.730708
# Unit test for function get_bin_path
def test_get_bin_path():
    # Check with and without optional binary directory in PATH
    test_binary = get_bin_path('dircolors')
    opt_dirs = ['/bin', '/usr/bin']
    test_binary = get_bin_path('dircolors', opt_dirs)
    # Test for an executable that should not be found
    try:
        test_binary = get_bin_path('notanexecutable')
        print('Test failed')
    except ValueError as ex:
        print('Test passed, ValueError raised: "{0}"'.format(ex))
        pass

# Generated at 2022-06-12 23:36:58.974039
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('false')
    try:
        get_bin_path('not_there')
    except ValueError:
        pass
    else:
        assert False, "should have raised ValueError"
    assert get_bin_path('false', ['/usr/bin', '/usr/sbin/'])
    try:
        get_bin_path('false', ['/usr/bin'])
    except ValueError:
        pass
    else:
        assert False, "should have raised ValueError"
    assert get_bin_path('false', required=True)

# Generated at 2022-06-12 23:37:09.479907
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil
    import sys

    d1 = tempfile.mkdtemp()

    path_contents = [
        (os.path.join(d1, 'a'), 'a'),
        (os.path.join(d1, 'b'), 'b'),
        (os.path.join(d1, 'c'), 'c'),
        (os.path.join(d1, 'exec'), 'exec'),
        (os.path.join(d1, 'exec2'), 'exec2'),
    ]

    # create files as they would be created on the filesystem
    for path, content in path_contents:
        with open(path, 'w') as f:
            f.write(content)
        # set execute permissions

# Generated at 2022-06-12 23:37:20.332647
# Unit test for function get_bin_path
def test_get_bin_path():
    import pytest
    from ansible.module_utils.common.sys_info import get_platform_subclass
    from ansible.module_utils.common.os.path import which

    def mock_platform_subclass(platform):
        class MockPlatform(object):
            def __init__(self):
                self.platform = platform

        return MockPlatform()

    def mock_which(command, path=None, opt_dirs=None):
        return command

    PYTEST_PATH = os.path.join(os.path.dirname(pytest.__file__), '__main__.py')

    def verify_error(msg, bin_path, opt_dirs=None):
        with pytest.raises(ValueError) as exc:
            get_bin_path(bin_path, opt_dirs)

       

# Generated at 2022-06-12 23:37:27.661584
# Unit test for function get_bin_path
def test_get_bin_path():
    '''Function to unit test get_bin_path'''

    bin_path_python = get_bin_path('python')
    assert os.path.exists(bin_path_python)
    assert os.path.isfile(bin_path_python)
    bin_path = get_bin_path('python', opt_dirs=['/not/a/dir'])
    assert bin_path == bin_path_python
    path = os.path.dirname(bin_path_python)
    bin_path = get_bin_path('python', opt_dirs=[path])
    assert bin_path == bin_path_python
    try:
        get_bin_path('not_a_command')
    except ValueError:
        assert True
    else:
        assert False

# Generated at 2022-06-12 23:37:37.874676
# Unit test for function get_bin_path
def test_get_bin_path():
    # First test is expected to pass, second should raise an exception
    bin_path = get_bin_path('python', ['/home/test/foo'])
    if not (bin_path == '/home/test/foo/python' or bin_path == 'python.exe'):
        raise AssertionError("test_get_bin_path_1 failed: bin_path %s is not expected value" % bin_path)
    try:
        bin_path = get_bin_path('python', ['/home/test/foo'])
    except ValueError:
        pass
    else:
        raise AssertionError("test_get_bin_path_2 failed: ValueError not raised for missing executable")