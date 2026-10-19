

# Generated at 2022-06-12 23:27:45.098036
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path("python") is not None
    assert get_bin_path("/usr/bin/python") is not None

    try:
        get_bin_path("python_no_exist")
    except ValueError as e:
        assert "Failed to find required executable" in str(e)
    else:
        assert False, "Should have thrown an exception"

# Generated at 2022-06-12 23:27:47.482573
# Unit test for function get_bin_path
def test_get_bin_path():
    if 'PATH' in os.environ and not os.environ['PATH']:
        os.environ['PATH'] = '/bin:/usr/bin'
    for arg in ['ls', 'bash', 'minimum_path_test']:
        get_bin_path(arg)



# Generated at 2022-06-12 23:27:48.656851
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('echo') == get_bin_path('echo')

# Generated at 2022-06-12 23:27:56.582915
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil
    import stat


# Generated at 2022-06-12 23:28:01.024253
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Unit test for function get_bin_path
    '''

    # get_bin_path should return the full path to an executable
    path_ls = get_bin_path('ls')
    assert 'ls' in path_ls

    # if the executable is not found in PATH, an exception should be raised
    import pytest
    with pytest.raises(ValueError):
        get_bin_path('some_executable_that_does_not_exist')


# Generated at 2022-06-12 23:28:09.188339
# Unit test for function get_bin_path
def test_get_bin_path():
    import sys

    try:
        get_bin_path('foo')
        assert False, 'Expected ValueError'
    except ValueError:
        pass
    try:
        get_bin_path('foo', sys.executable)
        assert False, 'Expected ValueError'
    except ValueError:
        pass
    bin_path = get_bin_path(sys.executable, [sys.prefix])
    assert bin_path == sys.executable, 'Expected %s, got %s' % (sys.executable, bin_path)

# Generated at 2022-06-12 23:28:16.870791
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    This function verifies the function get_bin_path() found in module_utils/basic.py
    '''
    tests = (
        ("/bin/sh", True),
        ("/bin/bash", True),
        ("/bin/zsh", False),
        ("/bin/zsh", False),
        ("/sbin/route", True),
        ("/sbin/iproute2/ip", True),
    )

    for arg, expected_result in tests:
        try:
            result = get_bin_path(arg)
            assert expected_result is True
        except ValueError:
            assert expected_result is False

# Generated at 2022-06-12 23:28:19.881217
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('sh') is not None
    try:
        get_bin_path('non_existent')
    except ValueError:
        pass
    else:
        assert False

# Generated at 2022-06-12 23:28:27.177721
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test if we're able to run uname(1)
    assert get_bin_path('uname')

    # Test if we're able to run uname(1) in /bin directory
    assert get_bin_path('uname', ['/bin'])

    # Test if we're able to run uname(1) in /bin directory and /sbin directory
    assert get_bin_path('uname', ['/bin', '/sbin'])

    # Test if we're able to run uname(1) in /bin directory and /sbin directory but /sbin
    # is not in the PATH variable. In that case get_bin_path inserts /sbin directory in the
    # PATH variable.
    assert get_bin_path('uname', ['/bin', '/sbin'])

    # Test if we're able to run uname

# Generated at 2022-06-12 23:28:36.318729
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path("ls") == "/bin/ls"
    assert get_bin_path("ls", ["/usr/bin"]) == "/usr/bin/ls"
    assert get_bin_path("ls", ["/bin"]) == "/bin/ls"
    assert get_bin_path("ls", ["/usr/bin", "/bin"]) == "/bin/ls"
    assert get_bin_path("ls", ["/bin", "/usr/bin"]) == "/bin/ls"
    assert get_bin_path("ls", required=True) == "/bin/ls"
    try:
        get_bin_path("notthere", required=True)
    except ValueError:
        pass
    else:
        assert False, "get_bin_path did not raise an exception"

# Generated at 2022-06-12 23:28:49.837544
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile

    expected_paths = '/bin:/usr/bin:/usr/local/bin:/sbin:/usr/sbin:/usr/local/sbin'
    expect = os.environ.get('PATH', '')
    assert expect == expected_paths, "get_bin_path assumed to work with default test path of %s" % expected_paths

    binfile = 'test_get_bin_path.bin'
    realdir = os.path.dirname(__file__)
    to_find = os.path.join(realdir, binfile)
    assert os.path.exists(to_find) and is_executable(to_find)

    # test with executable
    found = get_bin_path(binfile, [realdir])

# Generated at 2022-06-12 23:29:02.454812
# Unit test for function get_bin_path
def test_get_bin_path():

    # save and restore PATH since we modify it
    old_environ_path = os.environ.get('PATH', '')
    os.environ['PATH'] = '/usr/local/bin:/bin'

    # dir1 and dir2 don't exist
    dir1 = '/this/path/does/not/exist'
    dir2 = '/this/path/either'

    # /bin/sh does exist (and is executable) on all systems
    required_bin = 'sh'

    # /sbin/nologin does not exist on all systems
    nonrequired_bin = 'nologin'

    # PATH
    assert get_bin_path('sh') == '/bin/sh'

    # PATH + list of extra dirs to search

# Generated at 2022-06-12 23:29:11.239957
# Unit test for function get_bin_path
def test_get_bin_path():
    bin_path = get_bin_path('sh', ['/bin', '/usr/bin'], required=False)
    assert bin_path == '/bin/sh'
    bin_path = get_bin_path('sh', ['/bin', '/usr/bin'], required=True)
    assert bin_path == '/bin/sh'
    bin_path = get_bin_path('sh', ['/usr/bin'], required=True)
    assert bin_path == '/usr/bin/sh'
    bin_path = get_bin_path('sh', required=True)
    assert bin_path == '/bin/sh'
    # Testing exception.
    try:
        bin_path = get_bin_path('nonsense', required=True)
        assert False
    except ValueError:
        assert True

# Generated at 2022-06-12 23:29:19.763189
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path('invalid_executable')
    except ValueError as e:
        assert e.args[0] == 'Failed to find required executable "invalid_executable" in paths: %s' % str(os.environ['PATH'])
    else:
        raise Exception('Unexpected success.')

    try:
        get_bin_path('true', required=True)
    except ValueError as e:
        raise Exception('Unexpected exception "%s"' % str(e))

    assert get_bin_path('true') == '/bin/true'

    assert get_bin_path('true', opt_dirs=['/bin', '/invalid/path']) == '/bin/true'

# Generated at 2022-06-12 23:29:30.236432
# Unit test for function get_bin_path
def test_get_bin_path():
    import pytest
    from ansible.module_utils.common._text import to_bytes

    def _call_func(args):
        from ansible.module_utils.common.file import get_bin_path
        return to_bytes(get_bin_path(*args))

    # Test with no optional arguments
    system_paths = [
        '/bin/', '/usr/bin/', '/usr/local/bin/', '/sbin/', '/usr/sbin/', '/usr/local/sbin/',
        '/bin', '/usr/bin', '/usr/local/bin', '/sbin', '/usr/sbin', '/usr/local/sbin',
    ]
    os_path = os.environ.get('PATH')

# Generated at 2022-06-12 23:29:39.096714
# Unit test for function get_bin_path
def test_get_bin_path():
    if os.name == 'nt':
        assert get_bin_path('cmd.exe') == 'cmd.exe'
        assert get_bin_path('nul') == 'nul'
    else:
        assert get_bin_path('/bin/sh') == '/bin/sh'
        assert get_bin_path('/usr/bin/sh') == '/usr/bin/sh'
        assert get_bin_path('/usr/local/bin/sh') == '/usr/local/bin/sh'
        assert get_bin_path('/usr/local/sbin/sh') == '/usr/local/sbin/sh'

# Generated at 2022-06-12 23:29:48.628402
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path(arg='doesnotexists')
    except ValueError as e:
        assert 'Failed to find required executable "doesnotexists"' in '%s' % e
    else:
        assert False

    try:
        get_bin_path(arg='doesnotexists', opt_dirs=['/usr/bin'])
    except ValueError as e:
        assert 'Failed to find required executable "doesnotexists" in paths: /usr/bin' in '%s' % e
    else:
        assert False

    try:
        get_bin_path(arg='bash', opt_dirs=['/usr/bin'])
    except ValueError as e:
        assert False, '%s' % e


# Generated at 2022-06-12 23:29:54.776170
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test case 1: 'sh' command should always be found
    bin_path = get_bin_path('sh')
    assert bin_path
    assert bin_path == '/bin/sh' or bin_path == '/usr/bin/sh'
    # Test case 2: 'nonsense' command should always throw an exception
    try:
        get_bin_path('nonsense')
        assert False
    except ValueError as e:
        assert 'Failed to find required executable' in str(e)



# Generated at 2022-06-12 23:29:57.656714
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('id') is not None
    try:
        get_bin_path('thisfiledoesntexist')
    except:
        pass
    else:
        raise AssertionError('get_bin_path for non-existent file failed to raise an exception')

# Generated at 2022-06-12 23:30:09.106833
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile

    # check get_bin_path error format
    try:
        get_bin_path("nothis_is_not_a_cmd")
        assert False
    except ValueError as e:
        assert "Failed to find required executable \"nothis_is_not_a_cmd\" in paths" in str(e)

    # check get_bin_path success
    bin_path = get_bin_path("ls")
    assert os.path.exists(bin_path)
    assert is_executable(bin_path)

    # check get_bin_path in /sbin
    bin_path = get_bin_path("ip")
    assert os.path.exists(bin_path)
    assert is_executable(bin_path)

    # check get_bin_path with optional dir
   

# Generated at 2022-06-12 23:30:23.358735
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Verify function get_bin_path:
    '''
    def test_path_existence(executable, paths, existing_paths):
        '''
        Verifies if executable is in all paths that are supplied
        '''
        for path in existing_paths:
            if path not in paths:
                paths.append(path)
        if existing_paths:
            bin_path = get_bin_path(executable, paths, required=True)
            assert bin_path
        else:
            caught = None
            try:
                get_bin_path(executable, paths, required=True)
            except ValueError as e:
                caught = e
            assert caught

    # Test with existing and non-existing executables

# Generated at 2022-06-12 23:30:28.023343
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test path values
    import tempfile
    tmp_dir = tempfile.mkdtemp()
    try:
        assert get_bin_path('sh') == '/bin/sh'
        path1 = [tmp_dir]
        assert get_bin_path('sh', path1) == '/bin/sh'
    finally:
        os.rmdir(tmp_dir)

# Generated at 2022-06-12 23:30:33.232260
# Unit test for function get_bin_path
def test_get_bin_path():
    path = get_bin_path('ls')
    assert path == '/bin/ls'
    # non-existing binary
    try:
        get_bin_path('nonexisting')
    except ValueError:
        pass

    # make sure /usr/sbin is searched for
    path = get_bin_path('iptables')
    assert 'usr/sbin' in path

# Generated at 2022-06-12 23:30:43.849672
# Unit test for function get_bin_path
def test_get_bin_path():
    from ansible.module_utils._text import to_bytes

    path_list = []
    # Add paths to this list to test get_bin_path
    # Symbolic link to /bin/ls
    path_list.append(('/bin/ls', '/bin'))
    # Python2
    path_list.append(('/usr/bin/python', '/usr/bin'))
    # Python3
    path_list.append(('/usr/bin/python3', '/usr/bin'))

    for arg, arg_dir in path_list:
        arg_dir_bytes = to_bytes(arg_dir, errors='strict')
        exe_path = get_bin_path(arg, opt_dirs=[arg_dir], required=True)

# Generated at 2022-06-12 23:30:51.058329
# Unit test for function get_bin_path
def test_get_bin_path():
    from ansible.module_utils.six import PY3

    if PY3:
        assert get_bin_path('python3') == get_bin_path('python3', opt_dirs=['/usr/bin', '/usr/sbin', '/bin'])
    else:
        assert get_bin_path('python') == get_bin_path('python', opt_dirs=['/usr/bin', '/usr/sbin', '/bin'])

# Generated at 2022-06-12 23:30:53.162082
# Unit test for function get_bin_path
def test_get_bin_path():
    bin_path = get_bin_path('ls')
    assert bin_path
    assert bin_path.endswith('/ls')

# Generated at 2022-06-12 23:31:04.172235
# Unit test for function get_bin_path
def test_get_bin_path():
    # sanity, should return a path
    bin_path = get_bin_path("python")
    assert os.path.exists(bin_path)
    assert is_executable(bin_path)

    # path prefix, should return full path
    bin_path = get_bin_path("/bin/python")
    assert os.path.exists(bin_path)
    assert is_executable(bin_path)

    # no path prefix, should return full path
    bin_path = get_bin_path("python", ['/bin'])
    assert os.path.exists(bin_path)
    assert is_executable(bin_path)

    # with prefix, should return full path
    bin_path = get_bin_path("/bin/python", ['/bin'])

# Generated at 2022-06-12 23:31:12.572456
# Unit test for function get_bin_path
def test_get_bin_path():
    def _test_path(expected, path, args, opt_dirs):
        assert expected == get_bin_path(args, opt_dirs)

    # Debian jessie
    _test_path('/bin/ls', '/bin/ls', 'ls', None)
    _test_path('/bin/ls', '/bin/ls', 'ls', ['/bin'])
    _test_path('/bin/ls', '/bin/ls', 'ls', ['/bin', '/usr/bin'])
    _test_path('/sbin/init', '/sbin/init', 'init', None)
    _test_path('/sbin/init', '/sbin/init', 'init', ['/sbin', '/usr/sbin'])

    # z/OS

# Generated at 2022-06-12 23:31:22.201775
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('sh') == '/bin/sh'
    try:
        get_bin_path('this-command-does-not-exist')
        assert False, 'This command should not exist'
    except ValueError:
        pass
    assert get_bin_path('sh', ['/bin', '/usr/bin']) == '/bin/sh'
    assert get_bin_path('sh', ['/usr/bin']) == '/usr/bin/sh'
    try:
        get_bin_path('sh', ['/sbin', '/usr/sbin', '/usr/local/sbin'])
        assert False, 'This command should not exist in the provided path list'
    except ValueError:
        pass

# Generated at 2022-06-12 23:31:32.775706
# Unit test for function get_bin_path
def test_get_bin_path():
    from ansible.module_utils import basic

    test_bin = 'test_bin'

    test_dirs = ['/sbin', '/usr/sbin', '/usr/local/sbin', '/usr', '/usr/local/bin']
    for dir in test_dirs:
        if os.path.exists(dir):
            break
    else:
        # didn't find any of the dirs, not a good test
        assert False, "no test dir found"

    test_path = os.path.join(dir, test_bin)
    open(test_path, 'w').close()
    os.chmod(test_path, 0o755)

    assert get_bin_path(test_bin) == test_path, "Failed to find executable in PATH"

    # it is in the list, but not in PATH

# Generated at 2022-06-12 23:31:45.607838
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Test for function get_bin_path
    '''
    assert get_bin_path('cat') == '/bin/cat'
    assert get_bin_path('cat', ['/bin']) == '/bin/cat'
    assert get_bin_path('cat', ['/bin', '/usr/bin']) == '/bin/cat'
    try:
        get_bin_path('cat', ['foo'], required=True)
    except ValueError:
        pass
    except:
        assert False, 'Unexpected exception raised'

if __name__ == "__main__":
    test_get_bin_path()

# Generated at 2022-06-12 23:31:52.758029
# Unit test for function get_bin_path
def test_get_bin_path():
    paths = [
        '/bin',
        '/usr/bin',
        '/usr/local/bin',
        '/usr/bin/core_perl',
        '/usr/local/bin/core_perl'
    ]
    paths.extend(os.environ.get('PATH', '').split(os.pathsep))
    for d in paths:
        try:
            get_bin_path('ls', opt_dirs=[d])
        except Exception as e:
            raise Exception('Failed to find required executable "ls" in path: %s' % d)
    # negative tests
    try:
        get_bin_path('/nonexistent_dir/foo')
    except ValueError as e:
        assert "Failed to find required executable" in str(e)

# Generated at 2022-06-12 23:32:02.094497
# Unit test for function get_bin_path
def test_get_bin_path():
    test_bin_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test_get_bin_path')
    assert get_bin_path(test_bin_path) == test_bin_path

    test_bin_name = 'test_get_bin_path'
    test_bin_path = get_bin_path(test_bin_name)
    assert os.path.basename(test_bin_path) == test_bin_name

    test_bin_name = 'test_get_bin_path'
    import shutil
    test_bin_path_bin = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'bin')

# Generated at 2022-06-12 23:32:13.384681
# Unit test for function get_bin_path
def test_get_bin_path():
    import shutil
    import tempfile
    fd, bin_path = tempfile.mkstemp(suffix='.bin')
    os.close(fd)
    shutil.copyfile('/bin/sh', bin_path)
    os.chmod(bin_path, 0o755)
    os.environ['ANSIBLE_TEST_GET_BIN_PATH'] = bin_path


# Generated at 2022-06-12 23:32:20.808025
# Unit test for function get_bin_path
def test_get_bin_path():
    path_list = ['/usr/local/bin', '/usr/bin', '/bin']
    try:
        get_bin_path('__nonexistent_binary__', opt_dirs=path_list, required=True)
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "__nonexistent_binary__" in paths: ' + os.pathsep.join(path_list)
    else:
        assert False, 'ValueError not raised'



# Generated at 2022-06-12 23:32:25.980524
# Unit test for function get_bin_path
def test_get_bin_path():

    assert get_bin_path("ls") == "/bin/ls"
    assert get_bin_path("ls", opt_dirs=["/tmp"]) == "/bin/ls"
    assert get_bin_path("ls", opt_dirs=["/nodir"]) == "/bin/ls"

    try:
        get_bin_path("ls", opt_dirs=["/nodir"], required=False)
    except ValueError:
        assert False

# Generated at 2022-06-12 23:32:31.645742
# Unit test for function get_bin_path
def test_get_bin_path():
    import os
    import sys
    import tempfile
    from ansible.module_utils.common.file import is_executable

    path = os.environ.get('PATH')
    test_bin = tempfile.NamedTemporaryFile(mode='w+t', suffix='.py', delete=False)
    test_bin.write('#!/usr/bin/python2\n'
                   'import sys\n'
                   'str = "Hello World!\n"\n'
                   'sys.stdout.write(str)\n'
                   'sys.exit(0)\n')
    test_bin_name = os.path.basename(test_bin.name)
    test_bin_dir = os.path.dirname(test_bin.name)
    os.chmod(test_bin.name, 0o755)

# Generated at 2022-06-12 23:32:36.210671
# Unit test for function get_bin_path
def test_get_bin_path():
    import shutil
    import tempfile


# Generated at 2022-06-12 23:32:41.234156
# Unit test for function get_bin_path
def test_get_bin_path():
    bin_path = get_bin_path('ls')
    if bin_path is None:
        raise Exception('Failed to find "ls" in paths: %s' % os.pathsep.join(paths))
    if not os.path.exists(bin_path):
        raise Exception('File "%s" does not exist' % bin_path)
    if not is_executable(bin_path):
        raise Exception('File "%s" is not executable' % bin_path)

# Generated at 2022-06-12 23:32:52.497612
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil

    # Create simple test script
    (fd, fn) = tempfile.mkstemp(dir='/tmp', prefix='ansible_test_get_bin_path')
    f = os.fdopen(fd, 'w')
    f.write('#!/bin/sh\nexit 0')
    f.close()
    os.chmod(fn, 0o755)

    # Test 1: bin_path in PATH
    os.environ['PATH'] = os.pathsep.join(['/tmp', '/bin', '/usr/bin'])
    assert get_bin_path(os.path.basename(fn)) == fn

    # Test 2: bin_path not in PATH

# Generated at 2022-06-12 23:32:59.727116
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('ansible-playbook') == os.path.realpath('../../bin/ansible-playbook')
    assert get_bin_path('test-get_bin_path.py') == os.path.realpath(__file__)
    assert get_bin_path('doesnotexist.py') == os.path.realpath(__file__)

# Generated at 2022-06-12 23:33:09.727053
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile

    def touch(fname, times=None):
        with open(fname, 'a'):
            os.utime(fname, times)

    with tempfile.TemporaryDirectory() as tmp_dir:
        touch(os.path.join(tmp_dir, 'foo'))
        os.environ['PATH'] = tmp_dir
        assert get_bin_path('foo') == os.path.join(tmp_dir, 'foo')
        # should not raise exception
        get_bin_path('bar', required=False)
        # raises exception
        try:
            get_bin_path('bar')
        except ValueError:
            pass
        else:
            raise AssertionError('Unexpectedly succeeded to find executable')

# Generated at 2022-06-12 23:33:15.256752
# Unit test for function get_bin_path
def test_get_bin_path():
    import pytest

    with pytest.raises(ValueError):  # normally you should use unittest.TestCase.assertRaises for this
        get_bin_path('/bin/false')
        get_bin_path('/dev/this_does_not_exist')
    get_bin_path('/bin/false', ['/bin', '/sbin'])
    get_bin_path('true', ['/bin', '/sbin'])
    get_bin_path('/bin/true', ['/bin', '/sbin'])
    get_bin_path('/sbin/e2fsck', ['/bin', '/sbin'])

# Generated at 2022-06-12 23:33:26.221380
# Unit test for function get_bin_path
def test_get_bin_path():
    import sys

    try:
        # Should raise an exception because executable /bin/not-exists is missing
        bin_path = get_bin_path('/bin/not-exists')
        print('Failed to detect missing executable /bin/not-exists')
    except ValueError:
        print('Correctly failed to find missing executable /bin/not-exists')

    try:
        # Since arg is an absolute path, PATH is not used and os.path.exists is called on arg
        bin_path = get_bin_path('/bin/sh')
        print('Found executable %s' % bin_path)
    except:
        print('Failed to find executable /bin/sh')


# Generated at 2022-06-12 23:33:29.755521
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Test get_bin_path using /bin/ls as the example
    '''

    from ansible.module_utils.common.file import is_executable

    assert get_bin_path('ls') == '/bin/ls'
    assert is_executable(get_bin_path('ls'))

# Generated at 2022-06-12 23:33:36.016185
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test that ValueError is raised when an executable is not found in path
    try:
        get_bin_path("this_is_not_on_the_path")
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError when executable is not found"

    # Test that ValueError is raised when an optional dir is also not found
    try:
        get_bin_path("this_is_not_on_the_path", ["/this/is/not/a/valid/path"])
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError when optional dir is also not found"

    # Test that ValueError is raised when an executable is not found in path
    # and optional dir is also not found, but required is False

# Generated at 2022-06-12 23:33:41.791390
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('bash') == '/usr/bin/bash'
    assert get_bin_path('bash', opt_dirs=['/bin']) == '/bin/bash'
    assert get_bin_path('bash', opt_dirs=['/nonexist']) == '/usr/bin/bash'



# Generated at 2022-06-12 23:33:50.416307
# Unit test for function get_bin_path
def test_get_bin_path():
    # Since we are using a fake os module, we can't do any checking on the
    # environ PATH, so we can only test passing of opt_dirs.
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.file import get_bin_path
    module = AnsibleModule(argument_spec=dict(
        arg=dict(type='str', default='sh'),
        required=dict(type='bool', default=False),
        opt_dirs=dict(type='list', default=None),
    ))
    arg = module.params['arg']
    required = module.params['required']
    opt_dirs = module.params['opt_dirs']

    got_exception = False

# Generated at 2022-06-12 23:34:02.262740
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path('notfound')
    except Exception as e:
        assert 'Failed to find required executable' in str(e)
    assert get_bin_path('/bin/ls') == '/bin/ls'
    assert get_bin_path('ls', ['/bin']) == '/bin/ls'
    assert get_bin_path('ls') == '/bin/ls'
    try:
        get_bin_path('ls', ['notadir'])
    except Exception as e:
        assert str(e) == '/bin/ls'
    try:
        get_bin_path('ls', [])
    except Exception as e:
        assert str(e) == '/bin/ls'
    assert get_bin_path('/sbin/ip') == '/sbin/ip'
    assert get_

# Generated at 2022-06-12 23:34:10.021989
# Unit test for function get_bin_path
def test_get_bin_path():
    from functools import partial
    from ansible.module_utils.six import PY3
    from ansible.module_utils._text import to_text
    import tempfile

    # Use method #1 to invoke get_bin_path
    # Use case: required=True
    # Pre-condition: PATH contains a non-executable file
    # Post-condition: ValueError exception is raised
    non_executable = os.path.normpath(u'test/fixtures/scripts/no_execute')
    assert not is_executable(non_executable)
    path = os.environ['PATH']
    test_path = os.path.dirname(non_executable)
    os.environ['PATH'] = test_path

# Generated at 2022-06-12 23:34:27.762253
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Test function get_bin_path
    '''
    fake_path = os.path.join(os.path.dirname(__file__), 'fakesbin')
    bin_path = get_bin_path('thereisnotsuchfile')
    assert False, "Failed to find required executable 'thereisnotsuchfile' in paths: %s" % bin_path
    bin_path = get_bin_path('true', [fake_path])
    assert bin_path == os.path.join(fake_path, 'true'), "Expecting fake_path/true, got %s" % bin_path


if __name__ == '__main__':
    test_get_bin_path()

# Generated at 2022-06-12 23:34:37.375731
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Test function get_bin_path
    '''
    try:
        _ = get_bin_path('this_is_not_a_valid_executable_name')
        assert False
    except ValueError:
        assert True
    try:
        _ = get_bin_path(['this', 'is', 'not a valid executable name'])
        assert False
    except ValueError:
        assert True
    # Test with optional arguments
    assert get_bin_path('ls', required=True)
    assert get_bin_path('ls', opt_dirs=['/usr'])
    assert get_bin_path('ls', ['usr', 'etc'], True)

# Generated at 2022-06-12 23:34:46.737148
# Unit test for function get_bin_path
def test_get_bin_path():

    # Test case 1
    try:
        get_bin_path('/usr/bin/python')
    except ValueError:
        assert False, "Test case 1 failed"

    # Test case 2
    try:
        get_bin_path('/usr/binx/python')
    except ValueError:
        assert False, "Test case 2 failed"

    # Test case 3
    try:
        get_bin_path('python')
    except ValueError:
        assert False, "Test case 3 failed"

    # Test case 4
    my_dict = {'PATH': '/usr/bin/'}
    for d in my_dict.get('PATH', '').split(':'):
        path = os.path.join(d, 'python')

# Generated at 2022-06-12 23:34:55.757112
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test positive cases
    assert get_bin_path('ls') == '/bin/ls'
    assert get_bin_path('ls', opt_dirs=['/bin']) == '/bin/ls'
    assert get_bin_path('ls', opt_dirs=['/usr/bin']) == '/usr/bin/ls'
    assert get_bin_path('ls', opt_dirs=['/usr/bin', '/bin']) == '/usr/bin/ls'

    # Test negative cases
    try:
        get_bin_path('nosuchcmd')
    except ValueError as exc:
        assert 'Failed to find required executable "nosuchcmd"' in str(exc)


# Generated at 2022-06-12 23:34:59.948102
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('/bin/echo') == '/bin/echo'
    assert get_bin_path('echo') == '/bin/echo'
    assert get_bin_path('echo', opt_dirs=['/bin']) == '/bin/echo'
    assert get_bin_path('echo', opt_dirs=['/bin'], required=True) == '/bin/echo'
    try:
        get_bin_path('foo')
        assert False, "get_bin_path('foo') - expected ValueError Exception"
    except ValueError:
        pass

# Generated at 2022-06-12 23:35:08.807677
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('pwd') == '/bin/pwd'
    assert get_bin_path('/bin/pwd') == '/bin/pwd'
    assert get_bin_path('/bin/pwd', ['/bin']) == '/bin/pwd'
    assert get_bin_path('pwd', ['/bin']) == '/bin/pwd'
    assert get_bin_path('/bin/pwd', ['/tmp']) == '/bin/pwd'
    assert get_bin_path('pwd', ['/tmp']) == '/bin/pwd'
    assert get_bin_path('pwd', ['/tmp']) == '/bin/pwd'
    assert get_bin_path('pwd', opt_dirs=None) == '/bin/pwd'
    assert get_bin_

# Generated at 2022-06-12 23:35:19.575676
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile

    test_dir = tempfile.mkdtemp()
    script_dir_1 = os.path.join(test_dir, 'scriptdir1')
    script_dir_2 = os.path.join(test_dir, 'scriptdir2')

    os.mkdir(script_dir_1)
    os.mkdir(script_dir_2)

    os.chmod(script_dir_1, 0o0111)
    os.chmod(script_dir_2, 0o0111)

    # Setup bash scripts in both directories, but only the one
    # in script_dir_1 will be executable

# Generated at 2022-06-12 23:35:25.180432
# Unit test for function get_bin_path
def test_get_bin_path():

    # Test full path to executable
    bin_path = '/usr/bin/test_bin_path'
    bin_path_test = get_bin_path(bin_path)
    assert bin_path_test == bin_path

    # Test relative path to executable
    relative_bin_path = os.path.join(os.path.dirname(__file__), 'test_bin_path')
    relative_bin_opt_dirs = [os.path.dirname(__file__)]
    assert os.path.exists(relative_bin_path)
    relative_bin_test = get_bin_path('test_bin_path', opt_dirs=relative_bin_opt_dirs)
    assert relative_bin_test == relative_bin_path

    # Test invalid relative path to executable
    invalid_relative_bin_path

# Generated at 2022-06-12 23:35:31.216096
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        import __builtin__
        get_bin_path('__no_such_executable_file__', required=True, opt_dirs=[])
    except Exception:
        pass
    else:
        print("ansible.module_utils.common.process.get_bin_path() Unit test Failed.")
        # AssertionError

# Generated at 2022-06-12 23:35:43.011915
# Unit test for function get_bin_path
def test_get_bin_path():
    required = None
    opt_dirs = None

    # Verify get_bin_path throws ValueError with non-existent binary
    try:
        get_bin_path('no_such_binary_should_exist', required=required, opt_dirs=opt_dirs)
        assert False, 'get_bin_path did not raise ValueError for non-existent binary'
    except ValueError:
        pass

    # Verify get_bin_path throws ValueError with non-executable binary
    try:
        get_bin_path('/etc/passwd', required=required, opt_dirs=opt_dirs)
        assert False, 'get_bin_path did not raise ValueError for non-executable binary'
    except ValueError:
        pass

    # Verify get_bin_path returns expected path for an executable binary in a standard location


# Generated at 2022-06-12 23:36:11.214911
# Unit test for function get_bin_path
def test_get_bin_path():
    import sys
    from six.moves import reload_module
    from ansible.module_utils.common.file import is_executable

    # We are going to add a function is_executable to our test_module, and make sure it gets used.
    # To do that, we will mock the function is_executable, in the common.file module, and make sure
    # that get_bin_path uses the mocked function by calling get_bin_path from within our mocked
    # is_executable method.
    def is_executable():
        import ansible.module_utils.common.file as mod_file
        reload_module(mod_file)
        return mod_file.is_executable(mod_file.get_bin_path('python'))

    # Reload module to ensure the mocked function is in place.

# Generated at 2022-06-12 23:36:21.838027
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil
    import os

    # create temporary directory
    tdir = tempfile.mkdtemp()
    # create a file in path
    fname = 'foo'
    tmpfile = os.path.join(tdir, fname)
    f = open(tmpfile, 'w')
    f.write('')
    f.close()

    # remove tmpfile after test
    def remove_tmpfile():
        if os.path.exists(tmpfile):
            os.remove(tmpfile)
        shutil.rmtree(tdir)

    # test positive result
    assert get_bin_path(fname, opt_dirs=[tdir]) == tmpfile
    # test negative result

# Generated at 2022-06-12 23:36:29.028635
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Testing get_bin_path
    '''

    # No required parameter
    assert get_bin_path('ls') == '/bin/ls'
    assert get_bin_path('ls', opt_dirs='/usr/bin') == '/usr/bin/ls'

    # No required parameter
    assert get_bin_path('ls', required=True) == '/bin/ls'

    # Required parameter
    assert get_bin_path('foobar', required=True) == 'foobar'

    # Required parameter
    assert get_bin_path('/bin/ls', required=True) == '/bin/ls'

    # No file found

# Generated at 2022-06-12 23:36:35.064302
# Unit test for function get_bin_path
def test_get_bin_path():
    if os.path.exists('/usr/bin/python'):
        assert get_bin_path('python') == '/usr/bin/python'

    try:
        get_bin_path('this_program_does_not_exist')
    except ValueError as e:
        assert e.args[0] == 'Failed to find required executable "this_program_does_not_exist" in paths: %s' % os.pathsep.join(os.environ.get('PATH', '').split(os.pathsep))
    else:
        assert False, 'An exception should have been raised'

# Generated at 2022-06-12 23:36:45.913701
# Unit test for function get_bin_path
def test_get_bin_path():
    # test normal path
    search_paths = ['/bin']
    result = get_bin_path('ls', search_paths)
    assert result == '/bin/ls'

    # test overridden path
    search_paths = ['/usr/bin']
    result = get_bin_path('pwd', search_paths)
    assert result == '/usr/bin/pwd'

    # test not found path
    search_paths = ['/etc']
    try:
        get_bin_path('ls', search_paths)
    except ValueError as exc:
        assert "Failed to find required executable 'ls' in paths: /etc" == str(exc)

    # test path with sbin
    search_paths = ['/usr/bin']

# Generated at 2022-06-12 23:36:53.779104
# Unit test for function get_bin_path
def test_get_bin_path():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    import tempfile

    # save PATH
    save_path = os.environ['PATH']

    # try to find an executable that exists in the system
    tempdir = tempfile.mkdtemp()

# Generated at 2022-06-12 23:37:06.176341
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import subprocess

    # create a test executable
    testexec = tempfile.NamedTemporaryFile(mode='w', prefix='ansible_test_', suffix='.py', delete=False, dir='/tmp')
    testexec.write("#!/usr/bin/python\nprint 'Hello, world!'\n")
    testexec.close()
    os.chmod(testexec.name, 0o755)

    # add testexec folder to PATH
    mypath = os.getenv('PATH')
    os.environ['PATH'] = os.path.dirname(testexec.name) + ":" + mypath

    assert get_bin_path(testexec.name) == testexec.name

    os.remove(testexec.name)

    # test nonexistent executable

# Generated at 2022-06-12 23:37:13.998106
# Unit test for function get_bin_path
def test_get_bin_path():
    import sys
    if sys.version_info[0] < 3 and sys.version_info[1] < 3:
        import mock
        with mock.patch('ansible.module_utils.facts.system.is_executable', return_value=True):
            assert get_bin_path('/bin/ls') == '/bin/ls'
            assert get_bin_path('ls', opt_dirs=['/usr/bin', '/bin']) == '/bin/ls'



# Generated at 2022-06-12 23:37:19.095188
# Unit test for function get_bin_path
def test_get_bin_path():
    assert '/foo/bar/get_bin_path' == get_bin_path('get_bin_path', opt_dirs=['/foo/bar'])
    assert '/usr/bin/get_bin_path' == get_bin_path('get_bin_path', opt_dirs=['/usr/bin'])
    try:
        get_bin_path('get_bin_path', opt_dirs=['/bar'])
        raise Exception("Should have thrown an exception")
    except ValueError as e:
        assert 'Failed to find required executable "get_bin_path"' in str(e)

# Generated at 2022-06-12 23:37:27.151879
# Unit test for function get_bin_path
def test_get_bin_path():
    import sysconfig
    import shutil
    import tempfile
    import uuid
    test_file = tempfile.NamedTemporaryFile(delete=True)
    test_file.write(b'#! /usr/bin/env sh')
    test_file.flush()
    os.chmod(test_file.name, 0o755)
    path = tempfile.mkdtemp()