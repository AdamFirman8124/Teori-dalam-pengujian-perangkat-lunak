

# Generated at 2022-06-12 23:27:48.094047
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    get_bin_path unit test
    '''
    import sys

    # Fail if not passing any arguments.
    try:
        get_bin_path()
    except TypeError:
        pass
    else:
        assert False, "get_bin_path should require arguments"

    # Fail if passing extra arguments.
    try:
        get_bin_path('test', 'extra')
    except TypeError:
        pass
    else:
        assert False, "get_bin_path should not take extra arguments"

    # Check that an exception is raised if the executable does not exist.
    try:
        assert False, get_bin_path('this_is_not_a_valid_executable')
    except ValueError:
        pass

# Generated at 2022-06-12 23:27:56.081773
# Unit test for function get_bin_path
def test_get_bin_path():
    ''' unit test for function get_bin_path '''
    import tempfile
    import shutil

    class AnsibleModuleFailException(Exception):
        pass

    class AnsibleModuleExitException(Exception):
        pass

    class AnsibleModule():
        '''
            Fake AnsibleModule, it replaces AnsibleModule for unit test
        '''
        def __init__(self):
            self.params = {}

        def exit_json(self, **kwargs):
            '''
                fake exit_json, it raise an Exception and return result
            '''
            raise AnsibleModuleExitException(kwargs)

        def fail_json(self, msg):
            '''
                fake fail_json, it raise an Exception
            '''
            raise AnsibleModuleFailException(msg)

    # create test directory
    tmp_dir = temp

# Generated at 2022-06-12 23:28:02.890131
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil

    good_cmd = 'good_prog'
    bad_cmd = 'bad_prog'
    good_prog = """#!/bin/sh
      echo "Hello"
      """
    # Create temp dir for testing purposes
    tmp_dir = tempfile.mkdtemp()
    good_prog_abs = os.path.join(tmp_dir, good_cmd)
    with open(good_prog_abs, 'w') as f:
        f.write(good_prog)
    os.chmod(good_prog_abs, 0o755)
    os.environ['PATH'] += os.pathsep + tmp_dir
    assert get_bin_path(good_cmd) == good_prog_abs

# Generated at 2022-06-12 23:28:11.964868
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile

    def _create_temp_bin(name='test_get_bin_path', contents='#!/bin/bash'):
        try:
            fd, path = tempfile.mkstemp(dir='/tmp', prefix='ansible_test_%s_' % name, suffix='', text=False)
            os.close(fd)
            fp = open(path, 'wb')
            fp.write(contents.encode('utf-8'))
            fp.close()
            os.chmod(path, 0o755)
        except Exception:
            os.unlink(path)
            raise
        return path

    tmp_path_a = tempfile.mkdtemp(prefix='ansible_test_get_bin_path_')
    tmp_path_b = tempfile.mkdtemp

# Generated at 2022-06-12 23:28:18.772729
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        bp = get_bin_path('not_a_real_cmd')
        assert False, 'Should not have found a bin path for a non-existent command'
    except ValueError as e:
        assert 'Failed to find required executable "not_a_real_cmd"' in str(e)

    try:
        bp = get_bin_path('ansible')
        assert bp.endswith('ansible'), 'bin path for "ansible" should end with "ansible"'
    except ValueError:
        assert False, 'Should have found a bin path for "ansible"'

# Generated at 2022-06-12 23:28:26.910570
# Unit test for function get_bin_path
def test_get_bin_path():
    from ansible.module_utils.common._collections_compat import Mapping
    import unittest
    import tempfile
    import shutil
    import os
    import stat

    supported_shells = ['/bin/bash', '/bin/sh', '/bin/ksh', '/bin/zsh', '/bin/csh', '/bin/tcsh', '/bin/ash']

    class TestGetBinPath(unittest.TestCase):

        def setUp(self):
            self.tempdir = tempfile.mkdtemp()

        def tearDown(self):
            shutil.rmtree(self.tempdir)


# Generated at 2022-06-12 23:28:30.357012
# Unit test for function get_bin_path
def test_get_bin_path():
    #Finds the location of the python executable.
    #Unit test for the function get_bin_path.
    bin_path = get_bin_path('python')
    assert bin_path == '/usr/bin/python'

# Generated at 2022-06-12 23:28:35.774698
# Unit test for function get_bin_path
def test_get_bin_path():
    if os.name == 'nt':
        import win32api
        # check that ValueError is raised if executable is not found
        with pytest.raises(ValueError):
            get_bin_path('nonexistent_executable')
        # check that get_bin_path returns a full path to the executable if it is found
        assert os.path.normcase(get_bin_path('notepad.exe')) == os.path.normcase(win32api.FindExecutable('notepad.exe'))[1]
    else:
        # check that ValueError is raised if executable is not found
        with pytest.raises(ValueError):
            get_bin_path('nonexistent_executable')
        # check that get_bin_path raises ValueError if file is not executable
        # (regardless of whether it is found in

# Generated at 2022-06-12 23:28:37.454851
# Unit test for function get_bin_path
def test_get_bin_path():
    ''' if get_bin_path() fails it raises ValueError, so here we just call it'''
    get_bin_path('awk')

# Generated at 2022-06-12 23:28:48.666987
# Unit test for function get_bin_path
def test_get_bin_path():
    # Tests for get_bin_path function
    # Note: This will fail if /bin/sh does not exist or is not executable
    # Note: This will fail if /bin/bad_command does exist

    # Test 1: find a command that /should/ be on the path
    assert get_bin_path('sh', required=False) == '/bin/sh'

    # Test 2: try to find a command that /should not/ be on the path
    try:
        get_bin_path('bad_command', required=False)
        assert False, "Expected get_bin_path() to raise ValueError when command is missing"
    except ValueError as e:
        # Expected exception
        assert "Failed to find required executable \"bad_command\"" in str(e)

    # Test 3: try to find a command with opt_dir


# Generated at 2022-06-12 23:29:02.642525
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil
    from ansible.utils.path import unfrackpath

    # Create directory and add to PATH
    path = tempfile.mkdtemp()
    os.environ['PATH'] = '%s:%s' % (os.environ['PATH'], path)

    # Create script
    script_name = 'foo'
    script_path = os.path.join(path, script_name)
    with open(script_path, 'w') as fp:
        fp.write('#!/bin/bash\necho Hello World\n')
    os.chmod(script_path, 0o755)

    # Make sure that get_bin_path finds foo
    bin_path = get_bin_path(script_name)
    assert os.path.exists(bin_path)
   

# Generated at 2022-06-12 23:29:05.262433
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path('invalid_binary_name')
    except ValueError:
        pass
    else:
        assert False, 'Expected ValueError'

# Generated at 2022-06-12 23:29:09.176091
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test non-existing binary
    try:
        get_bin_path("boo")
    except ValueError as e:
        assert "Failed to find required executable" in str(e)
    else:
        assert False

    # Test existing binary
    try:
        get_bin_path("true")
    except Exception:
        assert False

# Generated at 2022-06-12 23:29:14.763062
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path('some_file_that_cant_exist')
        assert False, 'get_bin_path() did not fail when expected'
    except ValueError as e:
        # Passed, exception expected
        pass
    get_bin_path('sh')

# vim: expandtab tabstop=4 shiftwidth=4

# Generated at 2022-06-12 23:29:22.695982
# Unit test for function get_bin_path
def test_get_bin_path():
    # test_basic runs with PATH_SIZE = 0, so we need to set the path back to
    # something our test can use
    os.environ['PATH'] = '/usr/bin:/usr/sbin:/bin:/sbin'

    # test basic function sanity
    assert get_bin_path('ls') == '/bin/ls'
    assert get_bin_path('uptime') == '/usr/bin/uptime'

    # test optional paths
    assert get_bin_path('ls', ['/sbin']) == '/sbin/ls'
    assert get_bin_path('ls', ['/bin', '/sbin']) == '/bin/ls'
    assert get_bin_path('uptime', ['/bin']) == '/bin/uptime'
    assert get_bin_path('uptime', ['/usr/bin'])

# Generated at 2022-06-12 23:29:26.999723
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        import ansible.module_utils.basic
        get_bin_path(arg='ls')
        get_bin_path(arg='pwd')
        assert True
    except ValueError:
        assert False



# Generated at 2022-06-12 23:29:35.627044
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Function get_bin_path basic unit test
    '''
    arg = 'ansible-config'
    try:
        bin_path = get_bin_path(arg)
    except ValueError as e:
        raise AssertionError('Failed to get_bin_path for "%s": %s' % (arg, e))
    assert bin_path is not None
    assert os.path.isfile(bin_path)
    assert is_executable(bin_path)
    assert os.access(bin_path, os.X_OK)

# Generated at 2022-06-12 23:29:45.587390
# Unit test for function get_bin_path
def test_get_bin_path():

    # Pass in a directory of executables and have get_bin_path look for one of them
    executables_dir = '/usr/bin'
    executable = 'python3'
    open(os.path.join(executables_dir, executable), 'w')
    os.chmod(os.path.join(executables_dir, executable), 0o755)
    assert(get_bin_path(executable, opt_dirs=[executables_dir]) == os.path.join(executables_dir, executable))
    os.remove(os.path.join(executables_dir, executable))

    # Test when a directory is passed in but cannot find the executable
    executables_dir = '/usr/bin'
    executable = 'python3'

# Generated at 2022-06-12 23:29:48.665348
# Unit test for function get_bin_path
def test_get_bin_path():
    # verify we can return in a dir passed in
    assert get_bin_path('false', opt_dirs=['/bin']) == '/bin/false'

    # verify we can find it in PATH
    assert get_bin_path('false') == '/bin/false'

# Generated at 2022-06-12 23:29:52.839191
# Unit test for function get_bin_path
def test_get_bin_path():
    paths = ['/bin', '/usr/bin', '/usr/local/bin']
    expected = '/bin/ls'
    actual = get_bin_path('ls', paths)
    assert actual == expected, \
        "get_bin_path returned %s. Expected: %s" % (actual, expected)



# Generated at 2022-06-12 23:29:59.444952
# Unit test for function get_bin_path
def test_get_bin_path():
    # unittest.mock is not used because it requires python >= 3.3
    class MockOpen:
        # Mock open method
        def __init__(self):
            self.paths = [] # list of paths passed to open
        def __call__(self, path):
            self.paths.append(path) # remember path
            raise IOError()

    open = MockOpen()
    is_executable = lambda path: path.endswith(os.path.sep + 'bin' + os.path.sep + 'git')
    paths = ['one', 'two', '/bin', '/sbin', '/usr/sbin']
    get_path = lambda arg, opt_dirs=None, required=None: get_bin_path(arg, opt_dirs, required, open, is_executable)
    assert get

# Generated at 2022-06-12 23:30:10.458635
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Ensure that get_bin_path returns proper path
    '''

    result = get_bin_path('python')
    assert result == '/usr/bin/python'

    result = get_bin_path('python', opt_dirs = ['/usr/lib/locale'])
    assert result == '/usr/bin/python'

    try:
        result = get_bin_path('python', opt_dirs = ['/usr/lib/locale'], required = True)
    except Exception as e:
        assert 'Failed to find required executable' in str(e)

    try:
        result = get_bin_path('madeup')
    except Exception as e:
        assert 'Failed to find required executable' in str(e)


# Generated at 2022-06-12 23:30:17.310735
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    executable = 'does_not_exist'

    # create tempfile and cleanup
    tempdir = tempfile.mkdtemp()

# Generated at 2022-06-12 23:30:19.496427
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('ansible') is not None
    assert get_bin_path('foo') is None
    assert get_bin_path('bar', [os.environ.get('PATH')]) is None

# Generated at 2022-06-12 23:30:29.151223
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test for system command with required=True
    try:
        get_bin_path("ls", required=True)
    except ValueError:
        assert False, "Test for system command with required=True failed"
    # Test for system command with required=False
    try:
        get_bin_path("ls", required=False)
    except ValueError:
        assert False, "Test for system command with required=False failed"
    # Test for system command with required=None
    try:
        get_bin_path("ls", required=None)
    except ValueError:
        assert False, "Test for system command with required=None failed"
    # Test for non existent command with required=False

# Generated at 2022-06-12 23:30:40.136895
# Unit test for function get_bin_path
def test_get_bin_path():
    import platform

    system = platform.system()

    # get_bin_path in ansible/module_utils/common/file.py will raise an Exception if the executable is not found
    # For example if running the unit test in a container where busybox is not installed, this will raise an Exception.
    # TODO: find a way to isolate the unit tests so that busybox is not required for this test
    try:
        get_bin_path('ls')
    except Exception as e:
        if system == 'Linux':
            # On Linux this may raise a ValueError
            assert isinstance(e, ValueError)
        elif system == 'FreeBSD':
            # On FreeBSD this may raise an IOError
            assert isinstance(e, IOError)

# Generated at 2022-06-12 23:30:48.659323
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Validate get_bin_path function.
    '''

    # None or empty string not accepted.
    failed = False
    try:
        get_bin_path('')
    except ValueError:
        failed = True
    assert failed

    # On Linux, find ls, which is required.
    ls_bin = get_bin_path('ls')
    assert os.path.isabs(ls_bin)
    assert os.path.isfile(ls_bin)

    # On Linux, find BSD-style date, which is not required.
    date_bin = get_bin_path('date', required=False)
    assert os.path.isabs(date_bin)
    assert os.path.isfile(date_bin)

    # On Linux, do not find BSD-style test, which is not

# Generated at 2022-06-12 23:30:56.584196
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        assert get_bin_path('ls')
    except ValueError:
        assert False

    try:
        assert get_bin_path('ls', opt_dirs=['/bin', '/sbin'])
    except ValueError:
        assert False

    try:
        assert get_bin_path('ls', opt_dirs=['/doesnotexist'])
    except ValueError:
        assert True

    try:
        assert get_bin_path('doesnotexist')
    except ValueError:
        assert True

# Generated at 2022-06-12 23:30:59.994729
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Test if get_bin_path returns correct path or raises ValueError
    '''
    assert get_bin_path('sh') == '/bin/sh'
    # There is no 'xxxxx' executable
    try:
        get_bin_path('xxxxx')
    except ValueError:
        pass
    else:
        assert False

# Generated at 2022-06-12 23:31:10.364261
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    is_executable is mocked in test_utils.py to always return true.
    '''
    sbin_paths = ['/sbin', '/usr/sbin', '/usr/local/sbin']

    # present in opt_dirs
    path = get_bin_path('cat', ['/bin'])
    assert path == '/bin/cat'

    # present in sbin_paths
    path = get_bin_path('mount')
    assert path in sbin_paths

    # present in env PATH
    path = get_bin_path('grep')
    # test assumes /bin is in PATH
    assert path == '/bin/grep'

    # present in sbin_paths and env PATH
    path = get_bin_path('awk')
    # test assumes /bin is in PATH
   

# Generated at 2022-06-12 23:31:23.222521
# Unit test for function get_bin_path
def test_get_bin_path():
    assert (get_bin_path('sh') == '/bin/sh')
    assert (get_bin_path('/bin/sh') == '/bin/sh')
    assert (get_bin_path('/bin/sh', opt_dirs=[]) == '/bin/sh')
    assert (get_bin_path('bash', opt_dirs=[]) == '/bin/bash')

    raised = False
    try:
        get_bin_path('/bin/nosh', opt_dirs=[])
    except ValueError:
        raised = True
    assert raised

    assert (get_bin_path('bash', opt_dirs=['/bin']) == '/bin/bash')
    assert (get_bin_path('sh', opt_dirs=['/bin']) == '/bin/sh')

# Generated at 2022-06-12 23:31:31.275399
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile

    d = tempfile.mkdtemp()
    try:
        with open(os.path.join(d, 'bingo'), 'w') as f:
            f.write('#!/usr/bin/env python\n')

        os.chmod(os.path.join(d, 'bingo'), 0o755)
        get_bin_path('bingo', opt_dirs=[d])
    finally:
        os.remove(os.path.join(d, 'bingo'))
        os.rmdir(d)

# Generated at 2022-06-12 23:31:34.191133
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('ls') == '/bin/ls'
    assert get_bin_path('ansible') == '/usr/bin/ansible'
    assert get_bin_path('git') == '/usr/bin/git'

# Generated at 2022-06-12 23:31:44.048750
# Unit test for function get_bin_path
def test_get_bin_path():
    bin_path = get_bin_path('sh')
    assert bin_path is not None
    assert os.path.exists(bin_path)

    try:
        get_bin_path('foobar')
    except Exception as e:
        # Correct exception
        assert isinstance(e, ValueError)

    bin_path = get_bin_path('sh', ['/bin', '/usr/bin'])
    assert bin_path is not None
    assert os.path.exists(bin_path)

if __name__ == "__main__":
    import sys
    import pytest
    pytest.main(list(sys.argv))

# Generated at 2022-06-12 23:31:51.944251
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile

    # Test 1: get_bin_path raises ValueError if required=None, required=True, required=False
    required = None
    try:
        get_bin_path('this_executable_should_not_exist', required=required)
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "this_executable_should_not_exist" in paths: /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
    else:
        assert False, 'test 1 should fail'

    required = False
    assert get_bin_path('this_executable_should_not_exist', required=required) is None

    required = True

# Generated at 2022-06-12 23:32:01.817021
# Unit test for function get_bin_path
def test_get_bin_path():
    args = ['locate', 'sh', 'doesnotexist']
    expected = []
    basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'test'))
    for arg in args:
        if arg == 'doesnotexist':
            expected.append(None)
        else:
            expected.append(os.path.abspath(os.path.join(basedir, 'fixtures', 'module_utils', arg)))

    exist_dir = os.path.abspath(os.path.join(basedir, 'fixtures', 'module_utils'))
    non_exist_dir = os.path.abspath(os.path.join(basedir, 'fixtures', 'module_utils', 'doesnotexist'))


# Generated at 2022-06-12 23:32:09.759689
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('bash') == '/bin/bash'
    assert get_bin_path('hello_world', opt_dirs=['/home/martin']) == '/home/martin/hello_world'
    try:
        get_bin_path('hello_world', opt_dirs=['/home/martin'], required=True)
    except ValueError:
        assert True
    try:
        get_bin_path('hello_world', required=True)
    except ValueError:
        assert True

# Generated at 2022-06-12 23:32:14.828451
# Unit test for function get_bin_path
def test_get_bin_path():
    assert '/bin/cat' == get_bin_path("cat")
    assert '/bin/cat' == get_bin_path("cat", ['/bin'])
    assert '/bin/cat' == get_bin_path("cat", ["/tmp", "/bin", "/usr/bin/"])
    assert '/usr/bin/cat' == get_bin_path("cat", ['/usr/bin'])

# Generated at 2022-06-12 23:32:22.597586
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path('this-file-does-not-exist')
        assert False, "get_bin_path should fail if executable doesn't exist"
    except ValueError as e:
        if 'Failed to find required executable' not in str(e):
            assert False, 'Should have given ValueError but instead gave: %s' % str(e)

    assert get_bin_path('true') is not None, "get_bin_path should find 'true' binary if it exists"

# Generated at 2022-06-12 23:32:29.530567
# Unit test for function get_bin_path
def test_get_bin_path():
    # PATH normally contains /usr/bin, /bin and /usr/sbin on most linux and unix systems
    # get_bin_path returns the full path to the executable or raises a ValueError if not found
    assert get_bin_path('ls') == '/bin/ls'
    assert get_bin_path('awk') == '/usr/bin/awk'
    # files that are not in PATH but are in the common directory /usr/sbin will be found
    assert get_bin_path('ip') == '/sbin/ip'
    try:
        assert get_bin_path('imaginary_file') == '/imaginary/imaginary_file'
    except ValueError:
        # Cannot find imaginary_file, which is expected
        pass
    # get_bin_path optionally takes a list of optional directories to search in addition to PATH
    assert get

# Generated at 2022-06-12 23:32:40.651519
# Unit test for function get_bin_path
def test_get_bin_path():
    test_value = 'test_value'
    required = None

    assert get_bin_path(test_value) == os.path.join(os.path.sep, 'usr', 'bin', test_value)
    assert get_bin_path(test_value, opt_dirs=['/opt/bin']) == os.path.join('/opt/bin', test_value)
    assert get_bin_path(test_value, opt_dirs=['/opt/bin'], required=required) == os.path.join('/opt/bin', test_value)
    assert get_bin_path(test_value, opt_dirs=['/opt/bin', '/usr/sbin'], required=required) == os.path.join('/opt/bin', test_value)


# Generated at 2022-06-12 23:32:51.388453
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path("fgrep") == "/bin/fgrep"
    assert get_bin_path("fgrep", opt_dirs=["/usr/bin"]) == "/bin/fgrep"
    assert get_bin_path("some_non_existent_program") == "/bin/some_non_existent_program"
    try:
        get_bin_path("some_non_existent_program", required=True)
        assert False
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "some_non_existent_program" in paths: /sbin:/usr/sbin:/usr/local/sbin:/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games'

# Generated at 2022-06-12 23:33:00.982731
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    from ansible.module_utils._text import to_bytes

    test_string = to_bytes(b"import os\nprint(os.getpid())")
    test_files_dir = tempfile.mkdtemp()

    test_file_path1 = os.path.join(test_files_dir, 'test_file1.py')
    with open(test_file_path1, "wb") as f:
        f.write(test_string)
    os.chmod(test_file_path1, 0o700)

    # File not in search paths

# Generated at 2022-06-12 23:33:11.583114
# Unit test for function get_bin_path
def test_get_bin_path():

    def _mock_exists(arg):
        '''mock function for os.path.exists'''
        return arg in (
            '/bin/ls',
            '/tmp/ls',
            '/bin',
            '/tmp',
            '/sbin',
            '/usr/sbin',
            '/usr/local/sbin',
        )

    orig_exists = os.path.exists
    os.path.exists = _mock_exists

    assert get_bin_path('ls') == '/bin/ls'

    env = dict(PATH='/bin:/tmp')
    orig_environ = os.environ
    os.environ = env
    assert get_bin_path('ls') == '/bin/ls'

    opt_dirs = ['/tmp']

# Generated at 2022-06-12 23:33:13.767490
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path('sh')
    except ValueError:
        assert False
    assert get_bin_path('ash') != '/bin/ash'

# Generated at 2022-06-12 23:33:24.615714
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import sys
    import shutil

    # Create a temporary directory
    tmpdir = tempfile.mkdtemp()

    # create a temp directory with fake bins
    fake_bin = os.path.join(tmpdir, 'fake_bin')
    fake_sbin = os.path.join(tmpdir, 'fake_sbin')
    os.mkdir(fake_bin)
    os.mkdir(fake_sbin)

    # Create an exectuable file
    touch = "touch %s"
    for d in [tmpdir, fake_bin, fake_sbin]:
        for f in ['fake', 'python', 'python2', 'python3']:
            os.system(touch % os.path.join(d, f))

    # create a subdir with a fake python

# Generated at 2022-06-12 23:33:28.236377
# Unit test for function get_bin_path
def test_get_bin_path():
    if os.path.exists('/usr/bin/python'):
        assert get_bin_path('python') == '/usr/bin/python'
    assert get_bin_path('unit_testing_path_should_not_exist') == \
        '/usr/bin/python'

# Generated at 2022-06-12 23:33:30.121607
# Unit test for function get_bin_path
def test_get_bin_path():
    bin_path = get_bin_path('ls')
    assert '/bin/ls' in bin_path
    bin_path = get_bin_path('i_do_not_exist')
    assert bin_path == None

# Generated at 2022-06-12 23:33:37.908811
# Unit test for function get_bin_path
def test_get_bin_path():
    test_dir = os.path.dirname(os.path.abspath(__file__))
    assert isinstance(get_bin_path('python'), basestring)
    assert get_bin_path('python') == os.path.join(os.path.sep, 'usr', 'bin', 'python')
    assert get_bin_path('ansible-systemd-service', opt_dirs=[os.path.join(test_dir, '..', '..', '..', 'hacking', 'systemd')]) == os.path.join(test_dir, '..', '..', '..', 'hacking', 'systemd', 'ansible-systemd-service')

# Generated at 2022-06-12 23:33:48.558913
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Basic unit test for get_bin_path function
    '''
    caplog.setLevel(logging.DEBUG)
    tmpdir = tempfile.mkdtemp(prefix='ansible_test_tmp')

# Generated at 2022-06-12 23:33:59.983147
# Unit test for function get_bin_path
def test_get_bin_path():
    test_path_dirs = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
    test_path = os.path.join(test_path_dirs, 'test/sanity/tests/unit/module_utils/basic.py')
    try:
        get_bin_path(test_path)
    except Exception:
        assert True
    else:
        assert False

# Generated at 2022-06-12 23:34:06.806344
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('sh') == "/bin/sh"
    assert get_bin_path('sh', ['/bin']) == "/bin/sh"
    assert get_bin_path('sh', ['/nosuchdir']) == "/bin/sh"
    try:
        get_bin_path('sh', ['/nosuchdir'], 1)
        assert 0
    except ValueError as e:
        assert 1
    try:
        get_bin_path('nosuchcommand')
        assert 0
    except ValueError as e:
        assert 1

# Generated at 2022-06-12 23:34:12.430006
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test if get_bin_path finds commands in
    # 1. directory from PATH environment variable
    # 2. optional directories passed by value
    # 3. directories not in PATH, but which are searched by Ansible

    # Test directory from PATH variable
    assert get_bin_path('sh') == '/bin/sh'

    # Test directory from optional directories
    assert get_bin_path('sh', ['/usr/bin', '/usr/local/bin']) == '/usr/bin/sh'

    # Test directory not in PATH
    assert get_bin_path('sh', ['/usr/bin', '/usr/local/bin', '/usr/local/sbin']) == '/usr/local/sbin/sh'

    # Test exception

# Generated at 2022-06-12 23:34:23.010407
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test various combinations of command name, PATH, and opt_dirs

    # Test that it raises an exception when the command is not found
    try:
        get_bin_path('test_command_notfound')
        assert False, 'Should raise an exception'
    except:
        # This is expected.
        pass

    # Test that it finds an executable when it's in the PATH and opt_dirs is None
    # Save and clear the PATH environment variable
    old_path = os.environ.get('PATH', '')
    os.environ['PATH'] = ''
    # Add to the PATH the directory where we'll put the test executable

# Generated at 2022-06-12 23:34:31.419661
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        test = get_bin_path('date')
        assert(test == '/bin/date' or test == '/usr/bin/date')
    except ValueError as e:
        assert(False)
    try:
        test = get_bin_path('date', opt_dirs=['/bin'])
        assert(test == '/bin/date' or test == '/usr/bin/date')
    except ValueError as e:
        assert(False)
    try:
        test = get_bin_path('date', opt_dirs=['/usr/bin'])
        assert(test == '/bin/date' or test == '/usr/bin/date')
    except ValueError as e:
        assert(False)

# Generated at 2022-06-12 23:34:36.111621
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('ls', opt_dirs=['/bin']) == '/bin/ls'
    assert get_bin_path('bash') == '/bin/bash'
    assert get_bin_path('bash', opt_dirs=['/usr/local/bin']) == '/usr/local/bin/bash'

# Generated at 2022-06-12 23:34:38.776942
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Test that get_bin_path returns the given path when it's an absolute path that exists.
    '''
    assert get_bin_path('/bin/ls') == '/bin/ls'



# Generated at 2022-06-12 23:34:45.730416
# Unit test for function get_bin_path
def test_get_bin_path():
    from tempfile import mkdtemp
    from shutil import rmtree, copy
    import errno

    tempdir = mkdtemp()

    # copy some files to temporary directory
    copy('/bin/date', tempdir)
    copy('/bin/cat', tempdir)
    copy('/bin/echo', tempdir)

    # create test files in temporary directory
    with open(os.path.join(tempdir, 'file_not_executable'), 'w') as f:
        f.write('this is not executable')

    with open(os.path.join(tempdir, 'file_executable'), 'w') as f:
        f.write('#!/bin/sh\necho this is executable')
    os.chmod(os.path.join(tempdir, 'file_executable'), 0o777)

    #

# Generated at 2022-06-12 23:34:49.450218
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    verify that we can run git and ssh via this function
    '''
    if os.name == 'posix':
        assert get_bin_path('git') == '/usr/bin/git'
        assert get_bin_path('ssh') == '/usr/bin/ssh'

# Generated at 2022-06-12 23:34:50.745486
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('sh') == '/bin/sh'

# Generated at 2022-06-12 23:35:00.860589
# Unit test for function get_bin_path
def test_get_bin_path():
    # pylint: disable=redefined-outer-name
    path = get_bin_path('touch')
    assert os.path.basename(path) == 'touch'
    assert os.path.exists(path) and os.path.isfile(path) and is_executable(path)
    path = get_bin_path('touch', opt_dirs=[os.path.split(path)[0]])
    assert os.path.basename(path) == 'touch'
    assert os.path.exists(path) and os.path.isfile(path) and is_executable(path)

# Generated at 2022-06-12 23:35:08.410826
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path("this_is_not_a_valid_path")
    except ValueError:
        pass
    else:
        assert False, "Failed to raise an expected ValueError"
    assert get_bin_path("sh") == "/bin/sh", "Failed to find the sh executable"
    test_paths = [os.path.join(os.path.sep, "tmp")]
    assert get_bin_path("not_a_real_file", test_paths) == os.path.join(os.path.sep, "tmp", "not_a_real_file"), \
        "Failed to find a file in a provided path"

# Generated at 2022-06-12 23:35:16.064151
# Unit test for function get_bin_path
def test_get_bin_path():
    # get path to script
    bin_path = get_bin_path('python')
    assert os.path.exists(bin_path) and os.path.isfile(bin_path) and is_executable(bin_path)

    # get path to script with additional search path
    if not os.path.exists('/bin/sh'):
        try:
            # expect failure as /bin/sh is not in optional search path
            get_bin_path('sh', opt_dirs=['/bin'])
            assert False
        except ValueError:
            assert True

# Generated at 2022-06-12 23:35:18.729004
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('sh') == u'/bin/sh'
    assert get_bin_path('/bin/sh') == u'/bin/sh'

# Generated at 2022-06-12 23:35:30.526040
# Unit test for function get_bin_path
def test_get_bin_path():
    import pytest
    from tempfile import mkdtemp
    from shutil import rmtree

    # Create a temporary test folder
    tmpdir = mkdtemp()
    # Create a test executable
    with open(os.path.join(tmpdir, 'get_bin_path_unit_test'), 'w') as f:
        f.write('#! /bin/bash\n')
    os.chmod(os.path.join(tmpdir, 'get_bin_path_unit_test'), 0o777)

    # Check for success with just tmpdir in opt_dirs
    assert get_bin_path('get_bin_path_unit_test', opt_dirs=[tmpdir])

    # Check for success with tmpdir before system PATH

# Generated at 2022-06-12 23:35:42.273753
# Unit test for function get_bin_path
def test_get_bin_path():
    bin = '/bin/cat'
    assert get_bin_path('cat') == bin
    assert get_bin_path('cat', ['/bin']) == bin
    assert get_bin_path('cat', ['/sbin']) == bin

    try:
        get_bin_path('does_not_exist', ['/bin'])
        assert False, 'Did not fail to find missing binary'
    except ValueError:
        pass

    try:
        get_bin_path('cat', ['/does_not_exist'])
        assert False, 'Did not fail to find binary in missing directory'
    except ValueError:
        pass

    assert get_bin_path('/bin/cat') == bin

# Generated at 2022-06-12 23:35:50.694680
# Unit test for function get_bin_path
def test_get_bin_path():
    import sys
    import tempfile

    # make sure that this is not executable
    (fd, fname) = tempfile.mkstemp()
    test_path = os.path.join(os.path.dirname(fname), '_test_path')
    os.mkdir(test_path)
    test_exec = os.path.join(test_path, 'test_exec')
    os.close(fd)
    os.remove(fname)
    open(test_exec, 'wb').close()

    old_path = os.environ.get('PATH', '')
    os.environ['PATH'] = test_path

# Generated at 2022-06-12 23:36:01.396885
# Unit test for function get_bin_path
def test_get_bin_path():
    paths = ['/bin', '/usr/bin', '/usr/local/bin']
    try:
        get_bin_path('false', paths)
    except ValueError:
        assert False, 'Test 1: Unexpected exception'

    try:
        get_bin_path('/bin/false', paths)
    except ValueError:
        assert False, 'Test 2: Unexpected exception'

    paths = ['/bin', '/usr/bin', '/usr/local/bin']
    try:
        get_bin_path('/bin/false', paths)
    except ValueError:
        assert False, 'Test 3: Unexpected exception'

    paths = ['/bin', '/usr/bin', '/usr/local/bin']

# Generated at 2022-06-12 23:36:05.399411
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('tar') is not None

    try:
        get_bin_path('nonexisting_bin_path')
        assert False, "Expected exception"
    except ValueError:
        pass

    assert (get_bin_path('tar', opt_dirs=['/bin', '/usr/bin']) == '/bin/tar')
    assert get_bin_path('tar', opt_dirs=['/usr/bin']) == '/usr/bin/tar'

# Generated at 2022-06-12 23:36:15.663759
# Unit test for function get_bin_path
def test_get_bin_path():
    # pylint: disable=unused-variable
    from ansible.module_utils.basic import AnsibleModule

    def run_module():
        # in AnsibleModule 'exit_json' and 'fail_json' is mocked
        # pylint: disable=no-member
        module = AnsibleModule(argument_spec={
            'param1': {'required': True, 'type': 'str'},
            'param2': {'required': False, 'type': 'str'}
        }, supports_check_mode=True)
        # pylint: enable=no-member
        # create params
        params = {'param1': 'foo'}
        if module.params['param2'] is not None:
            params['param2'] = module.params['param2']
        # execute get_bin_path

# Generated at 2022-06-12 23:36:25.297398
# Unit test for function get_bin_path
def test_get_bin_path():
    path = get_bin_path('ansible-playbook', opt_dirs=["/usr/bin"])
    assert path == '/usr/bin/ansible-playbook'

# Generated at 2022-06-12 23:36:31.054181
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('ansible', opt_dirs=['/usr/local/bin/']) == '/usr/local/bin/ansible'
    assert get_bin_path('ansible', opt_dirs=['/usr/bin/', '/usr/local/bin/']) == '/usr/bin/ansible'
    assert get_bin_path('ansible', opt_dirs=['/usr/local/bin/', '/usr/bin/']) == '/usr/local/bin/ansible'
    assert get_bin_path('ansible', opt_dirs=['/usr/bin/', '/usr/local/bin/', '/opt/ansible/bin/']) == '/usr/bin/ansible'

# Generated at 2022-06-12 23:36:37.154141
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path('missing_exec')
    except ValueError as e:
        assert 'Failed to find required executable "missing_exec"' in str(e)
    else:
        raise ValueError('ValueError not raised')
    try:
        get_bin_path('ls', required=True)
    except ValueError as e:
        assert 'Failed to find required executable "ls"' in str(e)
    else:
        raise ValueError('ValueError not raised')
    assert get_bin_path('ls')

# Generated at 2022-06-12 23:36:40.842013
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        result = get_bin_path('sh')
        assert result == '/bin/sh'
    except Exception as e:
        assert False, 'Exception thrown from get_bin_path(): %s' % e

# Generated at 2022-06-12 23:36:48.785883
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path('cat', ['/bin'])
        assert False, 'Did not catch missing executable "cat" in an empty PATH'
    except ValueError:
        pass
    try:
        get_bin_path('cat', ['/bin', '/usr/bin'])
    except ValueError:
        assert False, 'Caught missing executable "cat" in a non-empty PATH'

    try:
        get_bin_path('noexec', ['/bin'])
        assert False, 'Did not catch non-executable "noexec" in PATH'
    except ValueError:
        pass

# Generated at 2022-06-12 23:36:55.406906
# Unit test for function get_bin_path
def test_get_bin_path():

    # Test get_bin_path when user specifies required=False
    # This should not trigger an exception
    try:
       get_bin_path('find', required=False)
       get_bin_path('find', required=False, opt_dirs=['/bin'])
    except:
       raise AssertionError('Failed test with required=False')

    # Test get_bin_path with just arg
    # Should always raise exception
    try:
       get_bin_path('nonexistingcommand')
       raise AssertionError('Failed test with nonexistingcommand')
    except ValueError:
       pass

    # Test get_bin_path with arg and opt_dirs
    # Should always raise exception

# Generated at 2022-06-12 23:36:59.431144
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path('foobar')
    except ValueError as e:
        assert ('Failed to find required executable "foobar"' in str(e))

    assert get_bin_path('python') == '/usr/bin/python'

# Generated at 2022-06-12 23:37:09.789418
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil
    import sys


# Generated at 2022-06-12 23:37:17.175994
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Ensure get_bin_path works
    '''
    import stat
    from ansible.module_utils.common.file import is_executable

    (fd, tmppath) = tempfile.mkstemp()
    os.close(fd)
    assert is_executable(tmppath) == False
    os.chmod(tmppath, stat.S_IXUSR)
    assert is_executable(tmppath) == True
    os.remove(tmppath)

# Generated at 2022-06-12 23:37:24.178489
# Unit test for function get_bin_path
def test_get_bin_path():
    # Make sure path is found with empty opt_dirs
    assert get_bin_path('ls') == '/bin/ls'

    # Check that opt_dirs work
    assert get_bin_path('ls', opt_dirs=['/usr/bin', '/usr/local/bin']) == '/usr/bin/ls'

    # Test search within sbin paths, using find as example
    assert get_bin_path('find') == '/usr/bin/find'

    # Test search within sbin paths, using nc as example
    assert get_bin_path('nc') == '/bin/nc'

# Generated at 2022-06-12 23:37:39.451346
# Unit test for function get_bin_path
def test_get_bin_path():
    # No executable
    path = get_bin_path('xxxxxx')
    assert path == None
    # Existent executable
    path = get_bin_path('gzip')
    assert path != None
    # Optional paths
    paths = [ '/bin', '/usr/bin' ]
    path = get_bin_path('rm', paths)
    for p in paths:
        if path.startswith(p):
            break
    else:
        assert True == False
    # Nonexistent optional path
    paths = [ '/bin', '/usr/bin', '/nosuch' ]
    path = get_bin_path('rm', paths)
    for p in paths:
        if path.startswith(p):
            assert True == False
    assert True == True
    # Test with required = True (deprecated)