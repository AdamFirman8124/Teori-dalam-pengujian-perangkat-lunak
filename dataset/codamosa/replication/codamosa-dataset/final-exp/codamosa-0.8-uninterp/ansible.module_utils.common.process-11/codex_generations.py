

# Generated at 2022-06-12 23:27:47.215078
# Unit test for function get_bin_path
def test_get_bin_path():
    # Testing command with absolute path
    bin_path = get_bin_path("/bin/ls")
    assert os.path.join("/bin", "ls") == bin_path

    # Testing command with relative path
    bin_path = get_bin_path("ls")
    assert os.path.join(os.environ['PATH'].split(os.pathsep)[0], "ls") == bin_path

    # Testing command that is present in only one of the paths in $PATH
    bin_path = get_bin_path("basename")
    assert os.path.join(os.environ['PATH'].split(os.pathsep)[0], "basename") == bin_path

# Generated at 2022-06-12 23:27:55.212661
# Unit test for function get_bin_path
def test_get_bin_path():
    # NOTE: During testing, this function is installed as ansible.module_utils.common.file.get_bin_path
    # Testing in its own function to avoid shadowing the function name
    # Unit test the basic expected usage of get_bin_path
    assert get_bin_path('sh') == '/bin/sh'

    # Unit test a known path to an executable
    bin_path = get_bin_path('sh', ['/bin'])
    assert bin_path == '/bin/sh'

    # Assert that an error is raised if the executable does not exist in the path
    try:
        get_bin_path('sh', ['/usr/not_a_path'])
    except ValueError as err:
        msg = 'Failed to find required executable "sh" in paths: /usr/not_a_path:'
        assert msg

# Generated at 2022-06-12 23:28:02.254201
# Unit test for function get_bin_path
def test_get_bin_path():
    # test 1: valid executable
    try:
        res = get_bin_path('/bin/ls')
    except ValueError as e:
        assert False, 'Unexpected exception: %s' % str(e)
    assert res == '/bin/ls', 'get_bin_path: expected %s, actual %s' % ('/bin/ls', res)
    # test 2: invalid executable
    try:
        res = get_bin_path('/bin/invalid_exe', required=True)
        assert False, 'Expected exception, but no exception thrown.'
    except ValueError:
        pass
    # test 3: valid executable in a path with spaces

# Generated at 2022-06-12 23:28:11.915246
# Unit test for function get_bin_path
def test_get_bin_path():
    path = get_bin_path('python3')
    assert os.path.exists(path)
    assert is_executable(path)

    # test opt_dirs
    path = get_bin_path('python3', opt_dirs=['/bin', '/usr/bin'])
    assert os.path.exists(path)
    assert is_executable(path)

    path = get_bin_path('python3', opt_dirs=['/thispathdoesnotexist'])
    assert os.path.exists(path)
    assert is_executable(path)

    # test when required is True

# Generated at 2022-06-12 23:28:21.445465
# Unit test for function get_bin_path
def test_get_bin_path():
    import sys
    import platform
    import subprocess
    from ansible.module_utils.six.moves import shlex_quote

    FILE_NAME = 'ansible_test_file'
    LINK_NAME = 'ansible_test_link'
    DIR_NAME = 'ansible_test_dir'

    test_dirs = []


# Generated at 2022-06-12 23:28:24.731528
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('ls') is not None
    assert get_bin_path('no_such_command_hopefully_xyz') is None
    try:
        get_bin_path('no_such_command_hopefully_xyz', required=False)
    except ValueError:
        # should we provide a deprecation ???
        pass

# Generated at 2022-06-12 23:28:27.718322
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('true') == '/bin/true'
    assert get_bin_path('grep') == '/bin/grep'
    try:
        get_bin_path('notexistingbinary')
        raise Exception('Not existing binary was found')
    except ValueError:
        pass



# Generated at 2022-06-12 23:28:36.934308
# Unit test for function get_bin_path
def test_get_bin_path():
    # Searches the default path, /bin:/usr/bin, and finds a valid executable.
    get_bin_path('python')

    # Searches a custom path, finds a valid executable.
    get_bin_path('python', opt_dirs=['/usr/local/bin'])

    # Searches a custom path, finds no valid executable.
    try:
        get_bin_path('python', opt_dirs=['/etc'])
    except ValueError:
        pass
    else:
        raise AssertionError('Expected a ValueError to be raised.')

    # Searches the default path, and finds no valid executable.
    try:
        get_bin_path('__does_not_exist')
    except ValueError:
        pass

# Generated at 2022-06-12 23:28:43.845680
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil
    import random
    import string

    def is_executable(mode):
        return mode & 0o111

    def is_exe(path):
        return os.path.isfile(path) and is_executable(os.stat(path).st_mode)

    rand_str = lambda: ''.join(random.choice(string.ascii_letters) for i in range(32))
    temp_dir = tempfile.mkdtemp(prefix='ansible-tmp-')

# Generated at 2022-06-12 23:28:52.599158
# Unit test for function get_bin_path
def test_get_bin_path():
    from ansible.module_utils.basic import AnsibleModule
    import ansible.module_utils.basic

    def get_bin_name(module):
        return module.get_bin_path('echo', required=False)

    # Test PATH
    new_env = dict(
        PATH="/sbin:/bin",
    )

    if 'PATH' in os.environ:
        old_env = dict(PATH=os.environ['PATH'])
        os.environ.update(new_env)
    else:
        old_env = dict()
        os.environ.update(new_env)
    module = AnsibleModule(argument_spec=dict())
    assert get_bin_name(module) == '/bin/echo'

    # Test PATH and optional dirs

# Generated at 2022-06-12 23:29:05.353986
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test to see if get_bin_path passes with a known executable
    try:
        path = get_bin_path('which')
    except ValueError as e:
        print(e)
        print('test_get_bin_path FAILED')
        exit(1)

    # Test to see if get_bin_path raises a ValueError when the path is not found
    try:
        path = get_bin_path('this_is_not_an_executable')
    except ValueError as e:
        print('Got expected exception: %s' % str(e))
    else:
        print('test_get_bin_path FAILED')
        exit(1)
    print('test_get_bin_path SUCCEED')

if __name__ == '__main__':
    test_get_bin_path

# Generated at 2022-06-12 23:29:11.662088
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path('does_not_exist')
    except ValueError:
        pass
    else:
        raise AssertionError('get_bin_path did not raise expected exception')

    try:
        get_bin_path('ls', opt_dirs=['/bin'])
    except ValueError:
        raise AssertionError('get_bin_path raised unexpected exception')

    try:
        get_bin_path('ls', opt_dirs=['/bin'], required=False)
    except ValueError:
        raise AssertionError('get_bin_path raised unexpected exception')

# Generated at 2022-06-12 23:29:15.204075
# Unit test for function get_bin_path
def test_get_bin_path():
    # tests worked on Linux
    assert get_bin_path('ls') != ""
    try:
        get_bin_path('__random_string_not_in_path')
        assert False
    except ValueError:
        assert True

# Generated at 2022-06-12 23:29:16.454271
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('python') == '/usr/bin/python'

# Generated at 2022-06-12 23:29:27.134177
# Unit test for function get_bin_path
def test_get_bin_path():
    executable = 'ansible-playbook'
    opt_dirs = ['$HOME/bin']
    required = True
    assert get_bin_path(executable, opt_dirs, required) == get_bin_path(executable)
    assert get_bin_path(executable, None, required) == get_bin_path(executable)
    assert get_bin_path(executable, [], required) == get_bin_path(executable)
    assert get_bin_path(executable, None, None) == get_bin_path(executable)
    assert get_bin_path(executable, '', required) == get_bin_path(executable)

# Generated at 2022-06-12 23:29:38.307452
# Unit test for function get_bin_path
def test_get_bin_path():
    """
    Unit tests
    """
    # find executable in PATH
    path = get_bin_path('python')
    assert os.path.exists(path) and is_executable(path)

    # find executable in PATH, or specified path
    optional_dir = os.path.dirname(path)
    path = get_bin_path('python', opt_dirs=[optional_dir])
    assert os.path.exists(path) and is_executable(path)

    # find executable in PATH, or specified path or specified alt path
    alt_dir = os.path.dirname(optional_dir)
    path = get_bin_path('python', opt_dirs=[optional_dir, alt_dir])
    assert os.path.exists(path) and is_executable(path)

    # find any executable in

# Generated at 2022-06-12 23:29:44.226480
# Unit test for function get_bin_path
def test_get_bin_path():
    arg = 'python3'
    try:
        bin_path = get_bin_path(arg)
    except ValueError as e:
        bin_path = None
        assert(str(e) == 'Failed to find required executable "%s" in paths: %s' % (arg, os.pathsep.join(os.environ['PATH'].split(os.pathsep))))

    assert(bin_path is not None)

# Generated at 2022-06-12 23:29:51.652796
# Unit test for function get_bin_path
def test_get_bin_path():
    import sys
    from ansible.module_utils import basic

    class FakeModule(object):
        def __init__(self):
            self.params = {}

        class Basic(basic.AnsibleModule):
            pass

    ansible_module = FakeModule.Basic()

    args = ['/bin/mktemp']
    expected_results = '/bin/mktemp'
    results = get_bin_path(args)
    assert results.find(expected_results) != -1, "Test failed: expect: {} Actual: {}".format(expected_results, results)

    args = ['mktemp']
    expected_results = '/bin/mktemp'
    results = get_bin_path(args)

# Generated at 2022-06-12 23:29:52.511672
# Unit test for function get_bin_path
def test_get_bin_path():
    get_bin_path('ls')

# Generated at 2022-06-12 23:29:57.058995
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path("bash") == get_bin_path("bash", [])
    assert get_bin_path("bash") != get_bin_path("bash", ['/sbin'])
    assert get_bin_path("true") == get_bin_path("true", ['/sbin'])
    try:
        get_bin_path("foo")
    except:
        pass
    else:
        assert "This should have thrown"

# Generated at 2022-06-12 23:30:04.306795
# Unit test for function get_bin_path
def test_get_bin_path():
    path = get_bin_path('sh')
    expected = '/bin/sh'
    assert path == expected

    path = get_bin_path('foobarbaz')
    assert path == None

    path = get_bin_path('sh', ['/usr/bin'])
    expected = '/usr/bin/sh'
    assert path == expected

# Generated at 2022-06-12 23:30:13.654117
# Unit test for function get_bin_path
def test_get_bin_path():
    # Verify that find_executable returns None if command is not found
    assert get_bin_path('nonexistent_command') is None
    # exe is found in /usr/bin
    assert get_bin_path('curl', ['/usr/bin/']) == '/usr/bin/curl'
    # exe is found in /usr/bin, even if opt_dir is /usr/bin/
    assert get_bin_path('curl', ['/usr/bin']) == '/usr/bin/curl'
    # exe is found in /bin
    assert get_bin_path('curl', ['/usr/bin/']) == '/usr/bin/curl'
    # exe is found in /usr/bin, even if opt_dir is /bin/

# Generated at 2022-06-12 23:30:23.486736
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test with no additional directories
    try:
        get_bin_path("ls", opt_dirs=None, required=True)
    except ValueError:
        assert 0, "get_bin_path failed to find ls"
    try:
        get_bin_path("invalid_exe", opt_dirs=None, required=True)
        assert 0, "get_bin_path should have raised exception for invalid_exe"
    except ValueError:
        pass
    # Test with additional directories
    try:
        get_bin_path("ls", opt_dirs=["/bin"], required=True)
    except ValueError:
        assert 0, "get_bin_path failed to find ls"

# Generated at 2022-06-12 23:30:31.990763
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Test function get_bin_path
    '''

    # get_bin_path returns the full path of the command
    assert get_bin_path('bash') == '/bin/bash'
    # get_bin_path raises ValueError if command does not exist
    try:
        get_bin_path('foo')
    except ValueError as err:
        assert str(err) == 'Failed to find required executable "foo" in paths: /usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/usr/local/sbin:/sbin:/usr/sbin'
    # get_bin_path looks for command in opt_dirs
    assert get_bin_path('bash', opt_dirs=['/sbin']) == '/sbin/bash'
    # get_bin_path looks for command

# Generated at 2022-06-12 23:30:34.089389
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    show the current system executable for a known executable
    '''
    from ansible.module_utils.six import PY3
    from distutils.spawn import find_executable
    if not PY3:
        from distutils.spawn import find_executable

    assert get_bin_path('ansible-playbook') == find_executable('ansible-playbook')

# Generated at 2022-06-12 23:30:44.495511
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test that /bin/ is searched first
    assert get_bin_path('ls') == '/bin/ls'
    assert get_bin_path('ls', required=True) == '/bin/ls'

    # Test that a directory in PATH is searched, then an additional directory
    # under opt_dirs
    os.environ['PATH'] = '/bin'
    assert get_bin_path('ls', opt_dirs=['/bin/']) == '/bin/ls'
    assert get_bin_path('ls', opt_dirs=['/bin/'], required=True) == '/bin/ls'

    # Test that an optional directory is found
    assert get_bin_path('bash', opt_dirs=['/bin/']) == '/bin/bash'

# Generated at 2022-06-12 23:30:51.871952
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path('nonexistant_binary')
    except ValueError:
        # Expected error
        pass
    else:
        assert False, 'Expected ValueError, but no error was raised'

    try:
        get_bin_path('false', required=True)
    except ValueError:
        pass
    else:
        assert False, 'Expected ValueError, but no error was raised'

    assert is_executable(get_bin_path('python'))

# Generated at 2022-06-12 23:30:57.385970
# Unit test for function get_bin_path
def test_get_bin_path():
    ''' test get_bin_path'''
    assert get_bin_path('ls') == '/bin/ls'
    assert get_bin_path('ls', opt_dirs=['/bin']) == '/bin/ls'
    try:
        assert get_bin_path('no_such_executable') == ''
    except ValueError:
        assert True

# Generated at 2022-06-12 23:31:01.870350
# Unit test for function get_bin_path
def test_get_bin_path():
    from ansible.module_utils.six import PY3

    if PY3:
        exception = FileNotFoundError
    else:
        exception = OSError

    # raise an exception if the program doesn't exist
    try:
        get_bin_path('thisprogramdoesntexist', required=True)
        assert False
    except ValueError as e:
        pass

    # raise an exception if the program isn't executable
    try:
        with open('/etc/passwd', 'r') as f:
            f.read()
        get_bin_path('/etc/passwd', required=True)
        assert False
    except ValueError as e:
        pass

    # don't raise an exception if the program is in the path even if required=True
    get_bin_path('/bin/sh', required=True)

# Generated at 2022-06-12 23:31:11.561731
# Unit test for function get_bin_path
def test_get_bin_path():
    from tempfile import mkdtemp
    from shutil import copy, rmtree

    def _create_bin(name, content='#!/bin/bash\nexit 0'):
        bin_path = os.path.join(my_path, name)
        with open(bin_path, 'w') as f:
            f.write(content)
        os.chmod(bin_path, 0o755)


# Generated at 2022-06-12 23:31:23.472533
# Unit test for function get_bin_path
def test_get_bin_path():
    # Function is_executable must be mocked in order to test get_bin_path
    import __builtin__ as builtins
    original_is_executable = is_executable

    def is_executable_mock(arg):
        if arg == '/usr/bin/sh':
            return True
        if arg == '/usr/bin/sh2':
            return False
        if arg == '/bin/sh':
            return False
        return original_is_executable(arg)


# Generated at 2022-06-12 23:31:34.080539
# Unit test for function get_bin_path
def test_get_bin_path():
    # Check if get_bin_path() raises ValueError
    # for not existing binary
    try:
        get_bin_path('not_existing_binary')
        assert False, 'Should not get here'
    except ValueError as e:
        assert 'Failed to find required executable "not_existing_binary" in' in str(e)

    # Check if get_bin_path() returns correct path
    # for existing binary
    assert get_bin_path('true') == '/bin/true'

    # Check if get_bin_path() returns correct path
    # for existing binary in the given directories
    assert get_bin_path('sh', opt_dirs=['/bin']) == '/bin/sh'
    assert get_bin_path('sh', opt_dirs=['/bin/sh']) == '/bin/sh'



# Generated at 2022-06-12 23:31:45.927002
# Unit test for function get_bin_path
def test_get_bin_path():
    '''get_bin_path function'''
    import tempfile
    from nose2.tools import params
    class paises:
        '''You can see this as a matrix of params and expected results'''

# Generated at 2022-06-12 23:31:48.756248
# Unit test for function get_bin_path
def test_get_bin_path():
    get_bin_path('ls')
    with pytest.raises(ValueError) as excinfo:
        get_bin_path('nonexistent_executable')
    assert 'Failed to find required executable' in str(excinfo.value)

# Generated at 2022-06-12 23:31:58.366130
# Unit test for function get_bin_path
def test_get_bin_path():
    test_paths = ['/tmp/bin', '/tmp']
    # Run test on git - save result then restore git path.
    # Note: we could run test on a command that we know doesn't
    # exist and thus we can test error conditions, but if the test
    # environment really doesn't have 'git' then we can't run the test
    # at all.
    orig_path = get_bin_path('git')
    try:
        git_path = get_bin_path('git', test_paths)
        assert(git_path == orig_path)
    finally:
        os.environ['PATH'] = orig_path

# Generated at 2022-06-12 23:32:05.290722
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile

    def create_executable_file(path, contents='test'):
        with open(path, 'w') as f:
            f.write(contents)
        os.chmod(path, 0o755)

    with tempfile.TemporaryDirectory() as tmp_dir:
        # test regular case
        test_cc = os.path.join(tmp_dir, 'cc')
        create_executable_file(test_cc)
        assert get_bin_path('cc', opt_dirs=[tmp_dir]) == test_cc

        # test current directory
        assert get_bin_path('cc', opt_dirs=['.']) == './cc'

        # test empty directory
        test_cc = os.path.join(tmp_dir, 'cc')

# Generated at 2022-06-12 23:32:08.040979
# Unit test for function get_bin_path
def test_get_bin_path():
    """
    Check that get_bin_path is able to find an executable
    """
    assert isinstance(get_bin_path('python2.7'), basestring)



# Generated at 2022-06-12 23:32:13.472709
# Unit test for function get_bin_path
def test_get_bin_path():
    # We assume that required executable "uname" is available in the PATH
    assert get_bin_path("uname")
    # We assume that non-existing executable "nonexisting_exec" is not available in the PATH
    try:
        get_bin_path("nonexisting_exec")
    except ValueError:
        # Expected exception
        pass
    else:
        assert False, "Expected an exception"

# Generated at 2022-06-12 23:32:24.044440
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil
    import textwrap
    from subprocess import PIPE
    from ansible.module_utils._text import to_bytes

    assert 'PATH' in os.environ
    env_paths = os.environ['PATH'].split(os.pathsep)

    assert get_bin_path('echo')
    assert get_bin_path('echo', ['foo'])
    assert get_bin_path('echo', [os.curdir])

    test_dir = tempfile.mkdtemp()

    with open(os.path.join(test_dir, 'echo'), 'w') as echo:
        echo.write(textwrap.dedent('''
            #!/bin/sh
            exec /bin/echo -n "$@"
        '''))

# Generated at 2022-06-12 23:32:36.349366
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil
    import sys
    import getpass

    user = getpass.getuser()
    local_bin = '/local/bin'
    non_existing = '/lorem/ipsum'
    assert not os.path.exists(local_bin)
    assert not os.path.exists(non_existing)

    # create a fake executable file
    bin_name = 'fake_ansible_dir_exists_script'
    # when creating a tempfile for testing, which is platform specific,
    # it is important to cleanup before assertion failure to clean up
    # temp resources (try/finally is a good choice)
    bin_file = None

# Generated at 2022-06-12 23:32:51.042397
# Unit test for function get_bin_path
def test_get_bin_path():
    from collections import namedtuple
    from ansible.module_utils.common.file import is_executable, is_directory

    TestCase = namedtuple('TestCase', ['path', 'required', 'expect'])
    valid_path_a = 'test_path_file_a'
    valid_path_b = 'test_path_file_b'

    # Create test cases
    dne = 'does_not_exist'

# Generated at 2022-06-12 23:33:00.726735
# Unit test for function get_bin_path
def test_get_bin_path():
    """ Test get_bin_path function """
    import sys
    import os
    os.environ['PATH'] = '/usr/bin'
    assert get_bin_path('ps') == '/usr/bin/ps'
    assert get_bin_path('/usr/bin/ps') == '/usr/bin/ps'
    # verify that opt_dirs is respected
    assert get_bin_path('python', ['/usr/bin']) == '/usr/bin/python'
    assert get_bin_path('python', ['/usr/local/bin', '/usr/local/sbin']) == '/usr/local/bin/python'
    assert get_bin_path('python', opt_dirs=[sys.exec_prefix]) == sys.executable
    # verify that /sbin is searched
    assert get_bin_path('ip')

# Generated at 2022-06-12 23:33:11.326049
# Unit test for function get_bin_path
def test_get_bin_path():
    import os
    import tempfile
    import shutil
    import sys
    import stat
    import fcntl
    import unittest

    test_script = 'testscript.sh'
    test_paths = ['/tmp', '/bin', '/sbin']
    test_script_content = '#!/bin/bash\n' \
                          'echo Success\nexit 0'

    class _AssertRaisesContext(object):
        """A context manager used to implement TestCase.assertRaises* methods."""

        def __init__(self, expected, test_case, expected_regexp=None):
            self.expected = expected
            self.failureException = test_case.failureException
            self.expected_regexp = expected_regexp

        def __enter__(self):
            pass


# Generated at 2022-06-12 23:33:21.893101
# Unit test for function get_bin_path
def test_get_bin_path():
    # need to run this in the test working directory so that we can
    # create a dummy executable
    os.chdir("tests")

    # dummy executable
    exe = "foo"

    # setup and change to test directory
    test_dir = "test_get_bin_path"
    os.makedirs(test_dir)
    os.chdir(test_dir)

    # test file not found
    try:
        get_bin_path(exe)
        assert False
    except ValueError:
        pass

    # create empty executable
    file = open(exe, "w")
    file.close()
    os.chmod(exe, 0o755)

    # test executable found

# Generated at 2022-06-12 23:33:30.946211
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile

    # Create 2 dummy executables in temp dir and make sure we can find them
    dirpath = tempfile.mkdtemp()
    open(os.path.join(dirpath, 'prog1'), 'a').close()
    open(os.path.join(dirpath, 'prog2'), 'a').close()
    os.chmod(os.path.join(dirpath, 'prog1'), 0o755)
    os.chmod(os.path.join(dirpath, 'prog2'), 0o755)
    assert get_bin_path('prog1', [dirpath]) == os.path.join(dirpath, 'prog1')
    assert get_bin_path('prog2', [dirpath]) == os.path.join(dirpath, 'prog2')
    assert get_

# Generated at 2022-06-12 23:33:41.843666
# Unit test for function get_bin_path
def test_get_bin_path():
    if not is_executable('/bin/ls'):
        raise Exception("ls is not executable")
    bin_path = get_bin_path('ls')
    if bin_path != '/bin/ls':
        raise Exception("Expected /bin/ls, got %s" % bin_path)

    try:
        get_bin_path('no_such_executable')
        raise Exception("Should not get here")
    except ValueError:
        pass

    bin_path = get_bin_path('ls', ['/bin'])
    if bin_path != '/bin/ls':
        raise Exception("Expected /bin/ls, got %s" % bin_path)


# Generated at 2022-06-12 23:33:48.558481
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil
    try:
        bindir = tempfile.mkdtemp()
        bin = os.path.join(bindir, 'test_bin_path')
        with open(bin, 'w') as f:
            f.write('#!/bin/sh\nexit 0\n')
        os.chmod(bin, 0o755)
        assert get_bin_path('test_bin_path', [bindir]) == bin
    finally:
        if os.path.exists(bindir):
            shutil.rmtree(bindir)

# Generated at 2022-06-12 23:33:58.082231
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('sh') == '/bin/sh'
    assert get_bin_path('ls') == '/bin/ls'
    assert get_bin_path('touch') == '/bin/touch'
    assert get_bin_path('echo') == '/bin/echo'
    assert get_bin_path('ping') == '/bin/ping'
    assert get_bin_path('test') == '/bin/test'
    assert get_bin_path('date') == '/bin/date'
    assert get_bin_path('ansible-config') == 'ansible-config'
    assert get_bin_path('ansible-playbook') == 'ansible-playbook'



# Generated at 2022-06-12 23:34:03.508804
# Unit test for function get_bin_path
def test_get_bin_path():
    import shutil
    from tempfile import mkdtemp
    import os

    # get_bin_path(arg, opt_dirs=None, required=None)

    required = "/usr/bin/python"
    # test on missing required executable
    opt_dirs = ["/usr/bin", "/usr/local/bin", "/bin", "/usr/sbin", "/usr/local/sbin", "/sbin"]
    if not os.path.exists(required):
        try:
            get_bin_path("python", opt_dirs=opt_dirs, required=required)
            raise AssertionError("Expected error for missing required executable.")
        except ValueError:
            pass

    # test on valid executable
    executable = "/usr/bin/python"
    if os.path.exists(executable):
        get

# Generated at 2022-06-12 23:34:10.649757
# Unit test for function get_bin_path
def test_get_bin_path():
    import sys
    import shutil
    if sys.platform == 'win32':
        path = get_bin_path('cmd.exe')
        assert 'cmd.exe' in path
    else:
        python_executable = sys.executable
        path = get_bin_path(python_executable)
        assert python_executable in path

    fake_dir = os.path.join(os.path.dirname(__file__), 'fake_dir')
    os.mkdir(fake_dir)
    path = os.path.join(fake_dir, python_executable)
    shutil.copy(python_executable, fake_dir)
    os.chmod(path, 0o500)
    bin_path = get_bin_path(python_executable, [fake_dir])

# Generated at 2022-06-12 23:34:22.280303
# Unit test for function get_bin_path
def test_get_bin_path():
    # Arrange
    arg = 'ls'
    required = True
    opt_dirs = None

    # Act
    bin_path = get_bin_path(arg, opt_dirs, required)

    # Assert
    assert bin_path is not None

# Generated at 2022-06-12 23:34:25.551268
# Unit test for function get_bin_path
def test_get_bin_path():
    path = get_bin_path('sh')
    assert path == '/bin/sh'

    path = get_bin_path('doesnotexist')
    assert path is None

    path = get_bin_path('doesnotexist')
    assert path is None

# Generated at 2022-06-12 23:34:36.253425
# Unit test for function get_bin_path
def test_get_bin_path():
    # The unit test does not require python-mock
    import mock
    import ansible
    from ansible.module_utils import basic
    from ansible.module_utils.common.file import get_bin_path

    mock_module = mock.Mock(params={})
    rc, out, err = basic.run_command('which env')

    # test_env_path makes sure 'env' command is found in PATH when unit test is run
    if rc != 0:
        mock_module.fail_json.assert_called_with(msg='Command is not found in PATH')

    # test_env_path makes sure 'env' command is not in /tmp and
    # get_bin_path should fail to find 'env' in /tmp


# Generated at 2022-06-12 23:34:40.213265
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('sh', ['/bin', '/usr/bin']) == '/bin/sh'
    assert get_bin_path('sh', ['/usr/bin', '/bin']) == '/bin/sh'
    assert get_bin_path('sh', ['/bin', '/usr/bin/']) == '/bin/sh'

# Generated at 2022-06-12 23:34:46.598894
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test for existing executable in default directories
    try:
        get_bin_path('touch')
    except ValueError:
        assert False, 'get_bin_path: Exception was raised for existing executable in default directories'
    # Test for executable in optional directory
    opt_dirs = ['/usr/bin']
    try:
        get_bin_path('touch', opt_dirs)
    except ValueError:
        assert False, 'get_bin_path: Exception was raised for existing executable in optional directory'
    # Test for executable in multiple optional directories
    opt_dirs = ['/usr/bin', '/usr/local/bin']
    try:
        get_bin_path('touch', opt_dirs)
    except ValueError:
        assert False, 'get_bin_path: Exception was raised for existing executable in multiple optional directories'


# Generated at 2022-06-12 23:34:51.605687
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Test function get_bin_path
    '''
    # GIVEN
    bin_path = None

    # WHEN
    try:
        # try to find a binary that doesn't exist
        bin_path = get_bin_path('shouldnotbehere')
    except ValueError as e:
        pass

    # THEN
    assert bin_path is None

# Generated at 2022-06-12 23:34:55.563239
# Unit test for function get_bin_path
def test_get_bin_path():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule({})
    a_bin_path = get_bin_path(module._shell.split()[0], None)
    assert a_bin_path is not None
    b_bin_path = get_bin_path("bin_not_found", None)
    assert b_bin_path is None



# Generated at 2022-06-12 23:35:01.140970
# Unit test for function get_bin_path
def test_get_bin_path():
    import sys
    import shutil

    # Get the directory that this test file is in
    old_path = get_bin_path('sh')
    # Copy the file somewhere else.  This will NOT be in the PATH
    new_dir = os.path.dirname(__file__) + os.sep + 'newdir'
    if os.path.exists(new_dir):
        shutil.rmtree(new_dir)
    os.mkdir(new_dir)
    shutil.copy2(old_path, new_dir)
    new_path = new_dir + os.sep + 'sh'
    # Make sure new_path is NOT in the PATH on platforms that we can control this
    if sys.platform.startswith('win'):
        os.environ['PATH'] = ''

# Generated at 2022-06-12 23:35:09.548153
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    tempdir = tempfile.gettempdir()
    curdir = os.getcwd()

    # Set up test files
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write("Hello")
    tfile.close()
    testfiles = [
        # perm, exists, dir, path
        # File should not be missing
        (0o777, False, False, tfile.name + "_-notfound_-" + curdir),
        # File should not be dir
        (0o777, True, True, tfile.name + "_-isdir_-" + curdir),
        # File should be executable and not a dir
        (0o666, True, False, tfile.name),
    ]

# Generated at 2022-06-12 23:35:20.230984
# Unit test for function get_bin_path
def test_get_bin_path():
    import shutil
    import tempfile
    p = os.environ.get('PATH', '').split(os.pathsep)
    test_path = tempfile.mkdtemp()
    p.insert(0, test_path)
    os.environ['PATH'] = os.pathsep.join(p)
    test_bin = os.path.join(test_path, 'testbin')
    open(test_bin, "w").close()

    assert get_bin_path('testbin') == test_bin
    assert get_bin_path('testbin', ['/usr/bin', '/usr/sbin']) == test_bin

    try:
        get_bin_path('not-a-binary')
    except ValueError:
        pass

# Generated at 2022-06-12 23:35:45.849166
# Unit test for function get_bin_path
def test_get_bin_path():
    from ansible.module_utils._text import to_native

    if os.name == 'nt':
        bin_path = get_bin_path("ipconfig")
        assert bin_path.lower().endswith("ipconfig.exe")

    else:
        try:
            ansible_bin = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../', 'bin/ansible'))
            bin_path = get_bin_path("ansible", [os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))])
            assert ansible_bin == bin_path

        except Exception as e:
            assert False, to_native(e)


# Generated at 2022-06-12 23:35:48.163882
# Unit test for function get_bin_path
def test_get_bin_path():
    # We do not expect this test to fail, so we simplify the test by not using assertRaises
    # and checking that the exception ValueError is not raised.
    try:
        import __main__
        # Test that we correctly detect a system executable
        get_bin_path(os.path.basename(__main__.__file__))
    except ValueError:
        pass
    else:
        raise AssertionError('Expected exception ValueError to be raised')

# Generated at 2022-06-12 23:36:00.353831
# Unit test for function get_bin_path
def test_get_bin_path():

    # Test when executable exists in PATH
    try:
        get_bin_path('ls')
    except Exception as e:
        raise

    # Test when executable does not exist and required is not set
    try:
        get_bin_path('not_existent_executable')
    except ValueError:
        pass

    # Test when executable does not exist and required is True
    try:
        get_bin_path('not_existent_executable', required=True)
    except ValueError:
        pass

    # Test when executable does not exist but the optional dir is provided
    # and the executable exists in the optional dir
    try:
        get_bin_path('ls', opt_dirs=[os.path.dirname(os.path.realpath(__file__))])
    except Exception as e:
        raise
    # Test when executable

# Generated at 2022-06-12 23:36:07.914924
# Unit test for function get_bin_path
def test_get_bin_path():
    old_path = os.environ.get('PATH')
    try:
        os.environ['PATH'] = '/bin:/usr/bin'
        test_path = get_bin_path('sed')
        assert test_path == '/bin/sed'
        test_path = get_bin_path('sed', ['/bin'])
        assert test_path == '/bin/sed'
    except Exception:
        raise
    finally:
        os.environ['PATH'] = old_path

# Generated at 2022-06-12 23:36:09.092248
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('foo') == '/bin/foo'

# Generated at 2022-06-12 23:36:17.065398
# Unit test for function get_bin_path
def test_get_bin_path():

    import __builtin__
    from ansible.module_utils._text import to_bytes

    class dummy:
        pass

    d = dummy()
    if not isinstance(__builtin__, object):
        d.__builtin__ = __builtin__
    else:
        d.__builtin__ = dummy()
        d.__builtin__.open = open
    d.os = os
    d.get_bin_path = get_bin_path

    # sanity check
    bp = d.get_bin_path('python')
    if not d.os.path.exists(bp):
        raise Exception('Not found: %s' % bp)
    # no PATH set
    os.environ['PATH'] = ''
    bp = d.get_bin_path('python')
    # full path to

# Generated at 2022-06-12 23:36:25.730494
# Unit test for function get_bin_path

# Generated at 2022-06-12 23:36:34.367744
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    get_bin_path Unit Test
    '''
    # Make sure we can find a command that exists in one of the standard paths
    assert get_bin_path('cat')
    # Make sure we fail to find a command that does not exist
    from ansible.module_utils.six import PY3

    try:
        get_bin_path('this_command_does_not_exist')
        assert False, 'Should have thrown for missing command'
    except ValueError:
        if PY3:
            assert 'find required executable "this_command_does_not_exist" in paths' in repr(ValueError)
        else:
            assert 'find required executable "this_command_does_not_exist" in paths' in repr(ValueError.message)
    except AssertionError as e:
        raise Assertion

# Generated at 2022-06-12 23:36:35.694437
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path("ls") == "/bin/ls"

# Generated at 2022-06-12 23:36:42.841593
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('true') == '/bin/true'
    assert get_bin_path('/bin/true') == '/bin/true'
    assert get_bin_path('./true', opt_dirs=['/bin']) == '/bin/true'
    assert get_bin_path('true', opt_dirs=['/bin']) == '/bin/true'

    try:
        get_bin_path('this-command-does-not-exist')
        assert False
    except ValueError:
        pass

# Generated at 2022-06-12 23:37:00.885265
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('ls') == '/bin/ls'
    assert get_bin_path('ls', opt_dirs=['/usr/bin']) == '/usr/bin/ls'
    assert get_bin_path('ls', opt_dirs=['/usr/bin', '/bin']) == '/bin/ls'

# Generated at 2022-06-12 23:37:06.380906
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test valid executable
    assert get_bin_path('python')
    # Test non-existent executable
    try:
        get_bin_path('__missing_executable__')
    except ValueError as e:
        assert "Failed to find required executable \"__missing_executable__\"" in str(e)



# Generated at 2022-06-12 23:37:18.017360
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    temp_dir = tempfile.gettempdir()
    test_dir = os.path.join(temp_dir, 'test_get_bin_path')
    os.mkdir(test_dir)
    os.environ['PATH'] = ':'.join((temp_dir, os.environ['PATH']))
    os.environ['TEST_GET_BIN_PATH'] = test_dir


# Generated at 2022-06-12 23:37:22.018844
# Unit test for function get_bin_path
def test_get_bin_path():
    ansible_path = get_bin_path('ansible')
    assert ansible_path is not None and os.path.exists(ansible_path)
    try:
        get_bin_path('does_not_exist')
        assert 0, 'Expected ValueError'
    except ValueError:
        pass

# Generated at 2022-06-12 23:37:27.810616
# Unit test for function get_bin_path
def test_get_bin_path():
    import sys
    import tempfile

# Generated at 2022-06-12 23:37:38.993742
# Unit test for function get_bin_path
def test_get_bin_path():
    get_bin_path('bash')
    get_bin_path('bash', ['/bin', '/usr/bin'])
    try:
        get_bin_path('bash', ['/bin', '/usr/bin'], required=True)
    except ValueError:
        pass
    try:
        get_bin_path('bash', ['/bin', '/usr/bin'], required=False)
    except ValueError:
        pass
    try:
        get_bin_path('bash', ['/bin', '/usr/bin'])
    except ValueError:
        pass
    try:
        get_bin_path('bash')
    except ValueError:
        pass
    try:
        get_bin_path('notthere')
    except ValueError:
        pass