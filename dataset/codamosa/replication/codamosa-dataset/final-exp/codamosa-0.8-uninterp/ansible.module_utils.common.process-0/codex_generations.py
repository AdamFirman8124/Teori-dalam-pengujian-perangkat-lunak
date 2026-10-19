

# Generated at 2022-06-12 23:27:41.700084
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        # missing unix executable
        get_bin_path('missing_unix_executable')
        assert False, "Expected ValueError missing_unix_executable"
    except ValueError as e:
        # expected exception
        pass
    try:
        # missing windows executable
        get_bin_path('missing_windows_executable')
        assert False, "Expected ValueError missing_windows_executable"
    except ValueError as e:
        # expected exception
        pass
    try:
        # missing darwin executable
        get_bin_path('missing_darwin_executable')
        assert False, "Expected ValueError missing_darwin_executable"
    except ValueError as e:
        # expected exception
        pass
    # existing unix executable

# Generated at 2022-06-12 23:27:43.431283
# Unit test for function get_bin_path
def test_get_bin_path():
    # None required since 2.10
    assert 'ls' == get_bin_path('ls')
    assert 'vi' == get_bin_path('vi')

# Generated at 2022-06-12 23:27:45.773180
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        # Test failing case
        get_bin_path("__executable_that_does_not_exist__")
    except ValueError as e:
        assert 'Failed to find' in str(e)



# Generated at 2022-06-12 23:27:54.686881
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('bash') == '/bin/bash'
    assert get_bin_path('sudo') in ['/usr/bin/sudo', '/usr/local/bin/sudo']
    assert get_bin_path('which') in ['/bin/which', '/usr/bin/which']
    assert get_bin_path('ls') in ['/bin/ls', '/usr/bin/ls']

    # If the executable is not in the path, it should raise an exception
    try:
        get_bin_path('nonexistent_command', required=True)
    except ValueError:
        pass
    else:
        raise Exception("Did not raise error for nonexistent command")

    # If the executable exists but is not in the path, it should raise an exception

# Generated at 2022-06-12 23:28:01.863879
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test with executable that exists
    result = get_bin_path('ls')
    assert result
    assert os.path.exists(result)
    assert not os.path.isdir(result)
    assert is_executable(result)

    # Test with executable that doesn't exist
    try:
        get_bin_path('this_is_an_invalid_executable')
        assert False
    except ValueError as e:
        assert "Failed to find required executable" in str(e)

    # Test with executable that doesn't exist in the given search path
    bin_path = get_bin_path('ls')

# Generated at 2022-06-12 23:28:11.885637
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil

    test_paths = [
        {'arg': 'nft', 'expected': '/sbin/nft'},
        {'arg': 'true', 'expected': '/bin/true'},
        {'arg': 'false', 'expected': '/bin/false'}
    ]

    # Create a temporary directory
    tmpdir = tempfile.mkdtemp()

    # Create some files for this test
    for t in test_paths:
        bin_path = os.path.join(tmpdir, t.get('arg'))
        open(bin_path, 'a').close()
        t['expected'] = bin_path

    # Add the tmpdir to the PATH

# Generated at 2022-06-12 23:28:15.575171
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    value of bin_path should be equal to location of 'ls' binary
    '''
    cmd = 'ls'
    bin_path = get_bin_path(cmd)
    assert bin_path is not None and len(bin_path) > 0, 'location of %s is blank' % cmd



# Generated at 2022-06-12 23:28:24.582644
# Unit test for function get_bin_path
def test_get_bin_path():
    path = get_bin_path('pip')
    assert path == '/usr/bin/pip'

    path = get_bin_path('pip', opt_dirs=['/usr/local/bin'])
    assert path == '/usr/bin/pip'

    path = get_bin_path('pip3', opt_dirs=['/usr/local/bin'])
    assert path == '/usr/local/bin/pip3'

    # Test ValueError
    args = {'arg': 'foobar', 'opt_dirs': []}
    try:
        get_bin_path(**args)
        assert False
    except ValueError:
        pass

    args = {'arg': 'foobar', 'opt_dirs': ['/invalid_dir']}

# Generated at 2022-06-12 23:28:31.108091
# Unit test for function get_bin_path
def test_get_bin_path():
    # generate a dummy bin_path for testing
    import tempfile
    temp_file = tempfile.NamedTemporaryFile(prefix="test_get_bin_path_")
    temp_file.close()
    bin_path = temp_file.name

    # Assert that get_bin_path returns the pathname of the tempfile when it is
    # given as an argument
    assert(get_bin_path(bin_path) == bin_path)

    # Assert that get_bin_path raises a ValueError exception when it is given
    # and argument that does not exist
    try:
        get_bin_path('/not/a/valid/path')
        assert(False)
    except ValueError:
        assert(True)
    except Exception:
        assert(False)

# Generated at 2022-06-12 23:28:41.310991
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Test function get_bin_path
    '''
    def test_assert(path, arg, opt_dirs=None, required=None):
        if required is None:
            required = True
        bin_path = get_bin_path(arg, opt_dirs=opt_dirs, required=required)
        if not os.path.exists(bin_path):
            raise ValueError('Path does not exist %s' % bin_path)
        elif not is_executable(bin_path):
            raise ValueError('Path is not executable %s' % bin_path)
        elif bin_path != path:
            raise ValueError('Path is not "%s": %s instead' % (path, bin_path))

    test_assert('/bin/echo', 'echo')

# Generated at 2022-06-12 23:28:45.337248
# Unit test for function get_bin_path
def test_get_bin_path():
    repoquery_path = get_bin_path("repoquery")
    assert repoquery_path == "/usr/bin/repoquery"

# Generated at 2022-06-12 23:28:53.372468
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test that get_bin_path raises Exception if none of the paths
    # have the executable
    test_paths = [
        "/bad1",
        "/bad2",
    ]

    try:
        get_bin_path("ls", test_paths)
        assert False, "get_bin_path should raise an Exception"
    except:
        pass
    # Test that get_bin_path returns the executable in the first path that it exists.
    test_paths = [
        os.path.dirname(os.path.realpath(__file__)),
        "/bad2",
    ]

    path = get_bin_path("import_module_utils_common_file.py", test_paths)
    assert os.path.realpath(path) == os.path.realpath(__file__)

# Generated at 2022-06-12 23:29:01.390675
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    This function is not used in any module or
    plugin. It is intended to serve as an example
    of how to use get_bin_path
    '''

    # Test no path
    try:
        path = get_bin_path('foo')
    except ValueError as e:
        assert "Failed to find required executable" in e.message

    # Test with path
    try:
        path = get_bin_path('ls', ['/bin'])
    except ValueError as e:
        assert False, 'unexpected exception'

    assert path == '/bin/ls'

# Generated at 2022-06-12 23:29:10.337821
# Unit test for function get_bin_path
def test_get_bin_path():
    from ansible.module_utils.six import PY3

    # Test file exists in PATH
    assert get_bin_path('dirname') == os.path.join(os.path.dirname(__file__), '..', '..', '..', 'bin', 'dirname')
    assert get_bin_path('./' + os.path.basename(__file__)) == os.path.join(os.path.dirname(__file__), os.path.basename(__file__))

    # Test file exists in PATH/sbin
    assert get_bin_path('ip') == '/sbin/ip'
    assert get_bin_path('ip', ['/usr/bin']) == '/sbin/ip'

# Generated at 2022-06-12 23:29:17.654762
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('cat') == '/bin/cat'
    assert get_bin_path('/bin/cat') == '/bin/cat'
    try:
        get_bin_path('cat', ['/dev/null'])
        raise Exception('get_bin_path accepted an invalid directory')
    except ValueError:
        pass
    #
    # Test that sbin dir is in the path
    #
    assert get_bin_path('udevadm') == '/sbin/udevadm'

# Generated at 2022-06-12 23:29:27.179564
# Unit test for function get_bin_path
def test_get_bin_path():
    t_paths_list = ['/tmp/bin', '/usr/bin', '/bin', '/usr/local/bin']
    t_paths_str = os.pathsep.join(t_paths_list)
    os.environ['PATH'] = t_paths_str
    t_dirs = ['.']
    t_cmd = 'date'
    t_bin = get_bin_path(t_cmd, t_dirs)
    assert t_bin == os.path.join(t_paths_list[1], t_cmd)

# Generated at 2022-06-12 23:29:38.349729
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path("")
        raise AssertionError("get_bin_path(\"\") did not raise ValueError")
    except ValueError:
        pass

    # Assume a unix-like environment
    # Empty PATH
    os.environ['PATH'] = ""
    try:
        get_bin_path("ls")
        raise AssertionError("get_bin_path(\"ls\") in empty PATH did not raise ValueError")
    except ValueError:
        pass

    # PATH with only one dir
    os.environ['PATH'] = "/bin"
    try:
        get_bin_path("ls")
        raise AssertionError("get_bin_path(\"ls\") in PATH=/bin did not raise ValueError")
    except ValueError:
        pass

    # PATH with two

# Generated at 2022-06-12 23:29:48.055700
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Test function for get_bin_path function
    '''

    import sys

    # Save original PATH
    original_path = os.environ.get('PATH', '')


# Generated at 2022-06-12 23:29:54.816142
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil

    test_executable = 'ansible_test_executable'
    test_dir = tempfile.mkdtemp()

    test_executable_path = os.path.join(test_dir, test_executable)
    with open(test_executable_path, 'w'):
        os.chmod(test_executable_path, 0o777)

    assert get_bin_path(test_executable, [test_dir]) == test_executable_path

    shutil.rmtree(test_dir)

# Generated at 2022-06-12 23:29:58.675455
# Unit test for function get_bin_path
def test_get_bin_path():
    cwd = os.getcwd()
    testdir = os.path.join(cwd, 'testdir')
    os.makedirs(testdir)
    with open(os.path.join(testdir, 'foo'), 'w') as f:
        f.write('#!/usr/bin/env python')
    os.chmod(os.path.join(testdir, 'foo'), 0o755)
    try:
        assert get_bin_path('foo', [testdir]) == os.path.join(testdir, 'foo')
    finally:
        os.remove(os.path.join(testdir, 'foo'))
        os.rmdir(testdir)

# Generated at 2022-06-12 23:30:11.250822
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('pwd')
    assert get_bin_path('/usr/bin/python3')
    assert get_bin_path('/usr/bin/python2', required=False)
    assert get_bin_path('/usr/bin/python2', required=False) == \
        get_bin_path('/usr/bin/python2') == '/usr/bin/python2'

# Generated at 2022-06-12 23:30:21.419856
# Unit test for function get_bin_path
def test_get_bin_path():
    # No valid executable should be found here
    paths = [None, '/path/does/not/exist']

    try:
        get_bin_path('non-existent-executable', paths)
        assert False, "function get_bin_path returned a value, expected exception"
    except ValueError as e:
        assert 'Failed to find required executable' in str(e)
    except:
        assert False, "function get_bin_path returned an inappropriate exception"

    # In this case get_bin_path should return /usr/bin/whoami
    paths.append('/usr/bin')
    assert get_bin_path('whoami', paths) == '/usr/bin/whoami'

# Generated at 2022-06-12 23:30:27.981072
# Unit test for function get_bin_path
def test_get_bin_path():

    # Verify that function raises ValueError if executable is not found
    try:
        get_bin_path("NEVER-DEFINED-COMMAND")
        raise AssertionError("Failed to raise ValueError when executable not found")
    except ValueError:
        pass

    # Verify that function returns full path if executable is found
    try:
        assert os.path.isabs(get_bin_path("python"))
    except AssertionError:
        raise AssertionError("Failed to return full path when executable is found")

# Generated at 2022-06-12 23:30:38.892564
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test: /usr/bin/python is an executable file
    bin_path = get_bin_path('python')
    assert(bin_path == '/usr/bin/python')

    # Test: /usr/bin/not_an_existing_path is not an executable
    try:
        get_bin_path('not_an_existing_path')
    except ValueError as e:
        assert(e.args[0] == 'Failed to find required executable "not_an_existing_path" in paths: /bin:/usr/bin')
    else:
        assert(False, "/usr/bin/not_an_existing_path should not be found")

    # Test: /usr/bin/not_an_existing_path is not an executable, but with user specified paths

# Generated at 2022-06-12 23:30:47.039891
# Unit test for function get_bin_path
def test_get_bin_path():

    if os.path.exists('/bin/sh'):
        bin_path = get_bin_path('sh')
        assert bin_path == '/bin/sh'
    else:
        print('Warning: skipping test as /bin/sh does not exist')

    try:
        bin_path = get_bin_path('ansible', opt_dirs=os.path.dirname(__file__))
    except ValueError:
        print('Warning: skipping test as ansible is not in the directory %s' % (os.path.dirname(__file__)))
    else:
        assert bin_path == os.path.join(os.path.dirname(__file__), 'ansible')

# Generated at 2022-06-12 23:30:58.767158
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('sh') == '/bin/sh'
    assert get_bin_path('sh', ['/bar']) == '/bar/sh'
    try:
        get_bin_path('sh', ['/bar', '/baz/'])
        assert False
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "sh" in paths: /bar:/baz/:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'


# Generated at 2022-06-12 23:30:59.684523
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('ls')

# Generated at 2022-06-12 23:31:10.115453
# Unit test for function get_bin_path
def test_get_bin_path():
    if 'PATH' in os.environ:
        del os.environ['PATH']

    # Set custom PATH
    paths = ['/usr/bin', '/usr/sbin']
    os.environ['PATH'] = os.pathsep.join(paths)

    # 'ruby' executable is found using the modified PATH
    assert '/usr/bin/docker' == get_bin_path('docker')
    assert '/usr/libexec/docker/docker-runc-current' == get_bin_path('docker-runc')
    # 'ruby' executable is not found and throws an Exception
    try:
        get_bin_path('not-a-real-executable')
    except ValueError as e:
        assert "Failed to find required executable 'not-a-real-executable' in paths: %s" % os.path

# Generated at 2022-06-12 23:31:14.384550
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path('pippo-mammolo', required=True)
    except ValueError:
        pass
    else:
        raise AssertionError('get_bin_path is not failing.')

    if not get_bin_path('ls', required=True):
        raise AssertionError('ls should be found.')

# Generated at 2022-06-12 23:31:22.124890
# Unit test for function get_bin_path
def test_get_bin_path():
    sbin_path = []
    try:
        get_bin_path('csh')
    except ValueError as e:
        assert e.message == 'Failed to find required executable "csh" in paths: /bin:/usr/bin:/usr/local/bin'
    try:
        get_bin_path('csh', sbin_path)
    except ValueError as e:
        assert e.message == 'Failed to find required executable "csh" in paths: /bin:/usr/bin:/usr/local/bin'
    try:
        get_bin_path('csh', None, True)
    except ValueError as e:
        assert e.message == 'Failed to find required executable "csh" in paths: /bin:/usr/bin:/usr/local/bin'
    sbin_path = ['/sbin']

# Generated at 2022-06-12 23:31:34.379550
# Unit test for function get_bin_path
def test_get_bin_path():
    '''Test that get_bin_path returns the path to the specified command'''
    assert get_bin_path('/bin/ls', opt_dirs=['/bin']) == '/bin/ls'
    assert get_bin_path('/bin/ls', required=True) == '/bin/ls'
    assert get_bin_path('ls') == '/bin/ls'
    assert get_bin_path('ls', opt_dirs=['/bin', '/usr/bin']) == '/bin/ls'
    assert get_bin_path('ls', opt_dirs=['/usr/bin', '/bin']) == '/bin/ls'
    assert get_bin_path('ls', opt_dirs=['/usr/bin', '/bin']) == '/bin/ls'

# Generated at 2022-06-12 23:31:43.642912
# Unit test for function get_bin_path
def test_get_bin_path():
    ''' test_get_bin_path '''

    # Testing
    # 1) get_bin_path() function gets a valid path
    # 2) Get an exception, since the given execuatble file is not present in the paths.

    try:
        system_executable_path = get_bin_path('python')
        assert os.path.exists(system_executable_path)
    except ValueError as VALUE_ERROR:
        assert VALUE_ERROR.message == "Failed to find required executable \"python2\" in paths: " \
                                       "/bin:/usr/bin:/usr/local/bin"

# Generated at 2022-06-12 23:31:51.773531
# Unit test for function get_bin_path
def test_get_bin_path():
    mock_path = ['foo/bar']
    test_bin = 'test.bin'

    # Test that ValueError is raised for missing binary
    try:
        get_bin_path(test_bin, mock_path)
    except ValueError:
        pass
    else:
        raise AssertionError('ValueError not raised for missing binary.')

    # Test that ValueError is raised for missing binary in additional paths
    try:
        get_bin_path(test_bin, ['missing_path'])
    except ValueError:
        pass
    else:
        raise AssertionError('ValueError not raised for missing binary in additional paths')

    # Test that binary search is performed when paths are provided
    with open('test.bin', 'w') as f:
        f.write('test')

# Generated at 2022-06-12 23:32:01.709083
# Unit test for function get_bin_path
def test_get_bin_path():
    import sys
    import tempfile
    exe_file = tempfile.NamedTemporaryFile()
    exe_file.write('''#!/bin/sh
    echo 'Unit test script'
    ''')
    exe_file.flush()
    os.fchmod(exe_file.fileno(), 0o755)
    exe_file_path = exe_file.name

    # get_bin_path should use current PATH
    path = os.environ.get('PATH', '').split(os.pathsep)
    for p in path:
        if p == os.path.dirname(exe_file_path):
            sys.stderr = sys.stdout
            found = get_bin_path(os.path.basename(exe_file_path))
            assert found == exe_

# Generated at 2022-06-12 23:32:10.175780
# Unit test for function get_bin_path
def test_get_bin_path():
    test_path_list = ['/bin', '/usr/bin']
    test_exe = 'test1'
    test_exe_path = '/bin/test1'
    test_exe_false = 'test2'
    assert get_bin_path(test_exe, opt_dirs=test_path_list) == test_exe_path
    try:
        get_bin_path(test_exe_false, opt_dirs=test_path_list)
        raise AssertionError
    except ValueError:
        pass

# Generated at 2022-06-12 23:32:18.386836
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    test function get_bin_path
    '''
    # Test with prepend
    path = get_bin_path('/bin/true', opt_dirs=['/bin'])
    assert path == '/bin/true'

    # Test with missing prepend
    try:
        path = get_bin_path('/bin/true', opt_dirs=['/doesnotexist'])
        assert not path
    except ValueError:
        pass
    else:
        assert False, 'failed to throw exception'

    # Test with missing path
    try:
        path = get_bin_path('/bin/true', opt_dirs=[])
        assert not path
    except ValueError:
        pass
    else:
        assert False, 'failed to throw exception'

    # Test with missing path and command

# Generated at 2022-06-12 23:32:24.162905
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('ls')
    assert get_bin_path('ls', opt_dirs=[])
    assert get_bin_path('ls', opt_dirs=None)
    assert get_bin_path('ls', opt_dirs=['/bin'])
    assert get_bin_path('ls', opt_dirs=['/usr/bin'])
    assert get_bin_path('ls', opt_dirs=['/usr/bin', '/bin'])



# Generated at 2022-06-12 23:32:36.468841
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('sh') == '/bin/sh'
    assert get_bin_path('sh', opt_dirs=['/usr/local/bin']) == '/bin/sh'
    assert get_bin_path('sh', opt_dirs=['/usr/local/bin', '/usr/bin']) == '/bin/sh'
    assert get_bin_path('sh', opt_dirs=['/usr/bin']) == '/bin/sh'
    assert get_bin_path('sh', opt_dirs=['/usr/sbin']) == '/bin/sh'

    # Don't find sbin programs by default

# Generated at 2022-06-12 23:32:42.076341
# Unit test for function get_bin_path
def test_get_bin_path():
    import shutil, tempfile
    tmp = tempfile.mkdtemp()
    tmp_path = [tmp,]
    f1 = os.path.join(tmp, 'f1')
    open(f1, 'w').close()

# Generated at 2022-06-12 23:32:52.659486
# Unit test for function get_bin_path
def test_get_bin_path():

    import shutil
    import tempfile

    class PathEntry(object):
        def __init__(self, path):
            self.path = path

    dir_tmp = tempfile.mkdtemp()

    dir_foo = PathEntry(os.path.join(dir_tmp, 'foo'))
    os.makedirs(dir_foo.path)

    bin_foo = PathEntry(os.path.join(dir_foo.path, 'foo'))
    open(bin_foo.path, "w").close()
    os.chmod(bin_foo.path, 0o700)

    dir_bar = PathEntry(os.path.join(dir_tmp, 'bar'))
    os.makedirs(dir_bar.path)


# Generated at 2022-06-12 23:33:00.420201
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    arg = 'foo'
    bin_path = os.path.join(tempfile.gettempdir(), arg)
    with open(bin_path, 'w') as fw:
        fw.write('#!/usr/bin/env python\n')
        fw.write('print("getting bin path")\n')
    os.chmod(bin_path, 0o755)
    assert get_bin_path(arg, [tempfile.gettempdir()]) == bin_path

# Generated at 2022-06-12 23:33:11.052946
# Unit test for function get_bin_path
def test_get_bin_path():

    import shutil
    import tempfile
    from ansible.module_utils.common.file import is_executable, is_writable

    def _temp_file(mode, dir_path=None, create=True):
        '''
        Create a temporary file.
        '''
        fh, path = tempfile.mkstemp(dir=dir_path)
        os.close(fh)
        if create:
            open(path, mode).close()
        return path

    def _clean_temp_file(path):
        '''
        Clean up temporary file.
        '''
        if os.path.isfile(path):
            os.unlink(path)

    def _temp_dir(prefix):
        '''
        Create a temporary directory.
        '''

# Generated at 2022-06-12 23:33:17.200373
# Unit test for function get_bin_path
def test_get_bin_path():
    paths = ['/usr/bin', '/bin']
    # Test with existing executable
    get_bin_path('ls', paths, True)
    # Test with non-existing executable
    try:
        get_bin_path('notexist', paths, True)
    except ValueError:
        pass
    # Test with non-existing executable and non-existing path
    paths.append('/this/path/does/not/exist')
    try:
        get_bin_path('ls', paths, True)
    except ValueError:
        pass

# Generated at 2022-06-12 23:33:28.331245
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path('no_executable')
    except ValueError as err:
        assert err.args[0] == 'Failed to find required executable "no_executable" in paths: /sbin:/usr/sbin:/usr/local/sbin:/bin:/usr/bin:/usr/local/bin:/opt/bin'

    import os.path
    import tempfile
    import sys
    import shutil

    tmpdir = tempfile.mkdtemp(prefix='ansible_test_get_bin_path')

# Generated at 2022-06-12 23:33:35.296194
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil
    import stat
    import sys

    test_dir = tempfile.mkdtemp()
    test_bin = os.path.join(test_dir, 'test_bin')
    with open(test_bin, 'w') as f:
        f.write('test')
    os.chmod(test_bin, stat.S_IXUSR | stat.S_IRUSR)

    # make a non-executable file
    test_not_bin = os.path.join(test_dir, 'test_not_bin')
    with open(test_not_bin, 'w') as f:
        f.write('test2')
    os.chmod(test_not_bin, stat.S_IRUSR)

    # test both with and without the optional directory
    assert get_

# Generated at 2022-06-12 23:33:39.380793
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('ls')
    try:
        get_bin_path('this-is-not-an-executable')
    except ValueError:
        pass
    else:
        assert False, "Failure, this should have raised an exception"

# Generated at 2022-06-12 23:33:49.442199
# Unit test for function get_bin_path
def test_get_bin_path():
    # Check on a specific path
    assert get_bin_path('/usr/bin/pwd') == '/usr/bin/pwd'
    try:
        get_bin_path('/bogus/bin/pwd')
    except ValueError as e:
        assert "Failed to find required executable" in str(e)

    # Check in PATH
    assert get_bin_path('pwd') == '/bin/pwd'
    try:
        get_bin_path('bogus-pwd')
    except ValueError as e:
        assert "Failed to find required executable" in str(e)

    # Check in optional path
    assert get_bin_path('pwd', ['/bin']) == '/bin/pwd'

# Generated at 2022-06-12 23:33:51.470293
# Unit test for function get_bin_path
def test_get_bin_path():
    # setup

    # test
    get_bin_path('bash')

# Generated at 2022-06-12 23:34:02.847634
# Unit test for function get_bin_path
def test_get_bin_path():
    import shutil
    import tempfile
    import getpass
    import sys
    import traceback
    import functools

    if os.name != 'posix':
        sys.stderr.write("This test should be run on a posix system")
        return False

    if os.geteuid() == 0:
        sys.stderr.write("This test can not be run as root")
        return False

    # Create a temporary directory and copy python3 executable there.
    test_dir = tempfile.mkdtemp()
    python3_bin_path = shutil.copy(sys.executable, test_dir)
    get_bin_path_partial = functools.partial(get_bin_path, opt_dirs=[test_dir])

    # Try to retrieve python3 executable

# Generated at 2022-06-12 23:34:06.055786
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('sh') == '/bin/sh'

    try:
        get_bin_path('missing')
    except ValueError as e:
        assert ('Failed to find required executable "missing" in paths: ' in str(e)) and ('/bin' in str(e))

# Generated at 2022-06-12 23:34:16.501722
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Check that get_bin_path works properly.
    '''
    import tempfile
    import shutil
    import os
    import stat

    def temp_dir_create(dir_name):
        '''
        Create a temporary directory.
        '''
        thisdir = tempfile.mkdtemp(dir=dir_name, prefix='ansible_test_')
        os.chmod(thisdir, stat.S_IRWXU)
        return thisdir

    def temp_dir_create_files(dir_name, files):
        '''
        Create temporary files in a directory.
        '''
        tmpfiles = []
        for f in files:
            tmpfiles.append(tempfile.NamedTemporaryFile(dir=dir_name, prefix=f, delete=False))
        return tmpfiles

   

# Generated at 2022-06-12 23:34:27.301326
# Unit test for function get_bin_path
def test_get_bin_path():
    def test_helper(bin):
        try:
            get_bin_path(bin)
        except ValueError:
            assert False, 'Failed to find required executable "%s"' % bin
        except Exception:
            assert False, 'Unexpected exception in get_bin_path(%s)' % bin

    # Test a few commands and verify they're on the path
    test_helper('awk')
    test_helper('sed')
    test_helper('python')
    test_helper('pip')
    test_helper('git')

    # Test that an exception is raised if a non-existent binary is not on the path

# Generated at 2022-06-12 23:34:28.094065
# Unit test for function get_bin_path
def test_get_bin_path():

    get_bin_path('sh')

# Generated at 2022-06-12 23:34:37.763874
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('/bin/echo') == '/bin/echo'
    assert get_bin_path('/bin/echo', opt_dirs=['/dev']) == '/bin/echo'
    assert get_bin_path('echo') == os.path.join(os.sep, 'bin', 'echo')
    assert get_bin_path('echo', opt_dirs=['/dev']) == os.path.join(os.sep, 'bin', 'echo')
    try:
        get_bin_path('notfound')
    except ValueError:
        pass
    else:
        assert False, 'get_bin_path must raise ValueError if not found'

# Generated at 2022-06-12 23:34:46.032985
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path('no_such_executable')
    except ValueError as e:
        assert 'Failed to find required executable' in str(e)

    assert get_bin_path('/bin/bash') == '/bin/bash'

    assert get_bin_path('bash') == '/bin/bash'

    try:
        get_bin_path('no_such_executable')
    except ValueError as e:
        assert 'Failed to find required executable' in str(e)

    assert get_bin_path('bash', required=False) == '/bin/bash'
    assert get_bin_path('no_such_executable', required=False) is None

# Generated at 2022-06-12 23:34:50.168458
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path("sh", ['/bin']) == '/bin/sh'
    assert get_bin_path("bash", opt_dirs=['/bin']) == '/bin/bash'
    assert get_bin_path("noexist", ['/bin'], required=False) is None
    try:
        get_bin_path("sh", ['/nowhere'])
        assert False, "should have failed"
    except ValueError:
        pass
    assert get_bin_path("sh", ['/nowhere'], required=False) is None
    try:
        get_bin_path("noexist", ['/nowhere'])
        assert False, "should have failed"
    except ValueError:
        pass
    assert get_bin_path("noexist", ['/nowhere'], required=False) is None

# Generated at 2022-06-12 23:34:58.363925
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path('doesnotexist')
        assert("Expected ValueError for non-existent executable")
    except ValueError:
        pass
    try:
        get_bin_path('doesnotexist', [])
        assert("Expected ValueError for non-existent executable")
    except ValueError:
        pass

    try:
        get_bin_path('doesnotexist', required=True)
        assert("Expected ValueError for non-existent executable")
    except ValueError:
        pass

    bin_path = get_bin_path('cat')
    assert(is_executable(bin_path))

    # Test that a directory is not found
    try:
        get_bin_path('/bin')
        assert("Expected ValueError for directory")
    except ValueError:
        pass

    bin_path

# Generated at 2022-06-12 23:35:07.421583
# Unit test for function get_bin_path
def test_get_bin_path():
    import sys
    import tempfile

    # Test for #47150
    if sys.platform != 'win32':
        import stat
        # Set PATH to a temporary dir with only a file lacking execution
        # permissions, and expect the function to raise a ValueError
        tmpdir_path = tempfile.mkdtemp()

# Generated at 2022-06-12 23:35:15.002281
# Unit test for function get_bin_path
def test_get_bin_path():
    test_paths = ['/usr/bin', '/usr/local/bin']
    assert get_bin_path('bash', test_paths) == '/usr/bin/bash'
    try:
        get_bin_path('fakebin', test_paths)
        raise Exception('exception expected but not raised')
    except ValueError:
        pass
    # method will return the first executable that it finds
    # given that fakebin does not exist, it should return sh
    assert get_bin_path('fakebin', test_paths, '/bin') == '/bin/sh'

# Generated at 2022-06-12 23:35:20.839326
# Unit test for function get_bin_path
def test_get_bin_path():
    from shutil import rmtree

    tmp_path = tempfile.mkdtemp(prefix='ansible_test_')

    bin_name = 'my_test_executable'
    # Verify that the executable is not found
    try:
        get_bin_path(bin_name, opt_dirs=[tmp_path])
        assert True== False, 'Failed to raise exception'
    except ValueError as e:
        assert f"Failed to find required executable \"{bin_name}\" in paths: {os.pathsep.join([tmp_path])}" == str(e)
    # Create the executable in the temporary dir
    bin_path = os.path.join(tmp_path, bin_name)
    assert True
    open(bin_path, 'a').close()

# Generated at 2022-06-12 23:35:34.111373
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('ls') == '/bin/ls'
    assert get_bin_path('ls', opt_dirs=['/bin', '/usr/bin']) == '/bin/ls'
    assert get_bin_path('ls', opt_dirs=['/usr/bin']) == '/usr/bin/ls'
    assert get_bin_path('ls', opt_dirs=['/usr/bin']) == '/usr/bin/ls'
    try:
        get_bin_path('asdfasdfasdf')
        assert False, 'expected an exception due to missing executable'
    except Exception:
        assert True

# Generated at 2022-06-12 23:35:44.371727
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    unit test for get_bin_path
    '''
    import tempfile
    import shutil

    tmp_d = tempfile.mkdtemp()
    try:
        tmp_p = os.path.join(tmp_d, 'getbinpathtest')
        with open(tmp_p, 'w') as f:
            f.write('#!/bin/bash\necho 1\nexit 0')
        os.chmod(tmp_p, 0o777)
        assert get_bin_path('getbinpathtest', opt_dirs=[tmp_d]) == tmp_p
    finally:
        shutil.rmtree(tmp_d)

# Generated at 2022-06-12 23:35:49.930834
# Unit test for function get_bin_path
def test_get_bin_path():
    # test for existing valid executable path
    assert get_bin_path('ls') == '/bin/ls'
    # test for non valid executable path
    try:
        get_bin_path('ls', ['/not_exists'])
    except ValueError as e:
        assert "Failed to find required executable" in str(e)
        assert "/not_exists" in str(e)
    # test for valid executable path with optional arguments
    assert get_bin_path('ls', ['/usr/bin']) == '/usr/bin/ls'

# Generated at 2022-06-12 23:35:51.837047
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('sh').endswith('/sh')

# Generated at 2022-06-12 23:36:00.735484
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Test function get_bin_path
    '''

    # test for raise ValueError
    try:
        get_bin_path('/usr/bin/ls')
        assert False
    except ValueError:
        assert True

    # test for return value
    import sys
    path = get_bin_path(os.path.basename(sys.executable), [os.path.dirname(sys.executable)])
    assert path == sys.executable
    assert os.path.exists(path)
    assert not os.path.isdir(path)
    assert is_executable(path)

# Generated at 2022-06-12 23:36:04.839620
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path('/bin/sh')
    except ValueError:
        raise AssertionError('get_bin_path: unable to find /bin/sh')

# Generated at 2022-06-12 23:36:07.176810
# Unit test for function get_bin_path
def test_get_bin_path():
    get_bin_path('pwd', opt_dirs=['/bin'])
    get_bin_path('pwd', opt_dirs=['/bin', '/sbin'])

# Generated at 2022-06-12 23:36:17.354411
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        bin_path = get_bin_path('test_get_bin_path', required=True)
    except ValueError as e:
        pass
    else:
        raise AssertionError("Failed to raise an exception, when test_get_bin_path is missing and required=True")
    test_path = os.path.realpath(__file__)
    test_dir = os.path.dirname(test_path)
    bin_path = get_bin_path('python', opt_dirs=[test_dir], required=True)
    assert test_path == bin_path, ("get_bin_path() failed to find python. Expected: %s, Got: %s" % (test_path, bin_path))
    test_dir = os.path.dirname(test_dir)
    assert get_

# Generated at 2022-06-12 23:36:21.922142
# Unit test for function get_bin_path
def test_get_bin_path():
    assert(get_bin_path('sh') == '/bin/sh')
    assert(get_bin_path('pwd') == '/bin/pwd')
    assert(get_bin_path('python2.7') == '/usr/bin/python2.7')
    assert(get_bin_path('python3') == '/usr/bin/python3')



# Generated at 2022-06-12 23:36:31.006828
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    from tempfile import mkdtemp
    from shutil import rmtree

    # Create temporary directory
    temp_dir = mkdtemp()

    # Create executable test_file in temporary directory
    test_file = tempfile.NamedTemporaryFile(mode="w+", suffix=".py", dir=temp_dir, delete=False)
    test_file.write("import os\nprint(os.getcwd())\n")
    test_file.close()
    os.chmod(test_file.name, 0o755)

    # Create directory with test_file name to test whether function fails if end-result is a directory
    test_dir = tempfile.mkdtemp(dir=temp_dir)

# Generated at 2022-06-12 23:36:42.007873
# Unit test for function get_bin_path
def test_get_bin_path():
    '''Unit test for function get_bin_path'''

    # test executable found in path
    try:
        bin_path = get_bin_path("ls")
        assert(bin_path != "")
        assert(os.path.exists(bin_path))
        assert(os.path.isfile(bin_path))
    except:
        assert(False)

    # test executable not found
    try:
        get_bin_path("this_command_should_never_exists")
    except ValueError:
        pass
    except:
        assert(False)

if __name__ == '__main__':
    test_get_bin_path()

# Generated at 2022-06-12 23:36:51.661177
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil

    test_dir = tempfile.mkdtemp()
    test_bin = os.path.join(test_dir, 'test_bin')
    with open(test_bin, 'w') as f:
        f.write("#!/bin/sh\necho Hello")
    os.chmod(test_bin, 0o755)

    # Test 1: Try to find 'test_bin' from current working directory (which should be the directory
    # where the test file resides)
    found_bin = get_bin_path('test_bin')
    assert os.path.samefile(found_bin, test_bin)

    # Test 2: Try to find 'test_bin' from a directory that is not in the PATH, but explicitly
    # specified.

# Generated at 2022-06-12 23:36:52.356912
# Unit test for function get_bin_path
def test_get_bin_path():
    import ansible.module_utils.basic
    impor

# Generated at 2022-06-12 23:36:53.922553
# Unit test for function get_bin_path
def test_get_bin_path():
    ssh = get_bin_path('ssh')
    assert ssh.endswith('ssh'), 'Failed to find system binary for ssh'

# Generated at 2022-06-12 23:37:04.367247
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Test get_bin_path function
    '''
    # Test get_bin_path with required=true and exception should be raised
    try:
        get_bin_path('junk-cmd')
        assert False, "Test get_bin_path with required=true and exception should be raised. But not raised."
    except ValueError:
        pass

    # Test get_bin_path with required=false and exception should not be raised
    try:
        get_bin_path('junk-cmd', required=False)
    except ValueError:
        assert False, "Test get_bin_path with required=false and exception should not be raised."

# Generated at 2022-06-12 23:37:11.769231
# Unit test for function get_bin_path
def test_get_bin_path():
    '''Test function get_bin_path'''
    # for use as a unit test, this file should exist
    this_file = os.path.abspath(__file__)
    # should not exist, but should not create an error
    this_file_not_found = this_file + '.fake'
    # should not exist, nor create an error, as it is a directory
    this_dir = os.path.dirname(this_file)
    # for use as a unit test, this file should exist
    this_file_in_sbin = '/sbin/ansible'
    # binary to test for, which should exist on most systems
    this_binary = 'chmod'
    # binary to test for, which may not exist on all systems
    this_binary_opt = 'rsync'

    assert get_bin_path

# Generated at 2022-06-12 23:37:21.014101
# Unit test for function get_bin_path
def test_get_bin_path():
    # Existing file
    assert get_bin_path('/bin/ls') == '/bin/ls'

    # Missing file
    try:
        get_bin_path('/bin/nonexistant')
        assert False
    except ValueError:
        assert True

    # Existing files with bash on PATH
    assert get_bin_path('bash') == '/bin/bash'
    assert get_bin_path('/bin/bash') == '/bin/bash'
    assert get_bin_path('bash', opt_dirs=['/bin']) == '/bin/bash'
    assert get_bin_path('bash', opt_dirs=['/bin/']) == '/bin/bash'

# Generated at 2022-06-12 23:37:25.089574
# Unit test for function get_bin_path
def test_get_bin_path():
    ''' test will fail if something is wrong with PATH or /sbin is missing '''
    get_bin_path('ls')
    get_bin_path('df')
    get_bin_path('ping', opt_dirs=['/bin', '/usr/bin'])
    get_bin_path('fake_cmd_should_not_exist', ['/bin', '/usr/bin'])

# Generated at 2022-06-12 23:37:31.344400
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test for executable in PATH
    try:
        get_bin_path('which')
        assert True
    except ValueError:
        # Test failed
        assert False

    # Test for executable not in PATH
    try:
        get_bin_path('foobar')
        # Test failed, ValueError exception was not thrown
        assert False
    except ValueError:
        # Test passed
        assert True