

# Generated at 2022-06-12 23:27:44.518616
# Unit test for function get_bin_path
def test_get_bin_path():
    arg = 'ls'
    p = get_bin_path(arg)
    assert p is not None, 'Return value is not none'
    assert os.path.exists(p), 'Return value is a valid path'
    assert os.path.isfile(p), 'Path is a file'
    assert os.access(p, os.X_OK), 'Path is executable'

# Generated at 2022-06-12 23:27:51.887082
# Unit test for function get_bin_path
def test_get_bin_path():
    # Check for system command
    assert get_bin_path('sh') is not None

    # Check for script in test/utils/module_utils
    assert get_bin_path('test_module_utils_test_module_utils_test.sh', opt_dirs=[os.path.join(os.path.dirname(__file__), 'test', 'utils', 'module_utils')]) is not None

    # Check that ValueError is raised when required is False
    try:
        get_bin_path('command_does_not_exist', required=False)
        assert False, "get_bin_path should have raised ValueError"
    except ValueError:
        pass

# Generated at 2022-06-12 23:27:57.325281
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Unit test for function get_bin_path
    '''

    assert get_bin_path('sh')
    assert get_bin_path('sh', ['/bin', '/usr/bin'])
    assert get_bin_path('sh', ['/bin', '/usr/bin'], False)

    try:
        get_bin_path('no_way_this_exists_so_failure_must_be_raised')
        assert False
    except ValueError as e:
        pass

    assert get_bin_path('sh', ['/bin', '/usr/bin'])

# Generated at 2022-06-12 23:28:00.670625
# Unit test for function get_bin_path
def test_get_bin_path():
    # common in PATH
    get_bin_path('python', ['/usr/bin'])

    # with opt_dirs
    get_bin_path('python', opt_dirs=['/usr/bin'])

    # common not in PATH
    get_bin_path('python', ['/usr/bin'])



# Generated at 2022-06-12 23:28:08.886368
# Unit test for function get_bin_path
def test_get_bin_path():
    # find an executable that we can assume is on all systems (like /bin/ls)
    test_path = get_bin_path('ls')
    assert '/bin/ls' == test_path
    # if we give an invalid command, it should throw
    try:
        test_path = get_bin_path('ls-invalid', required=False)
        assert False, "Should have thrown exception"
    except ValueError as e:
        assert "Could not find the executable ls-invalid" in str(e)
    return True

# Generated at 2022-06-12 23:28:18.556389
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('pwd') == '/bin/pwd'
    assert get_bin_path('/bin/pwd') == '/bin/pwd'
    assert get_bin_path('/bin/pwd', ['/usr/bin']) == '/bin/pwd'
    assert get_bin_path('/bin/pwd', ['/usr/bin'], 'required') == '/bin/pwd'
    assert get_bin_path('pwd', ['/usr/bin'], 'required') == '/usr/bin/pwd'
    assert get_bin_path('/bin/pwd', ['/bin']) == '/bin/pwd'
    assert get_bin_path('pwd', ['/none'], 'required') == False

# Generated at 2022-06-12 23:28:26.830008
# Unit test for function get_bin_path
def test_get_bin_path():

    import tempfile


# Generated at 2022-06-12 23:28:35.311391
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('python') == '/usr/bin/python'
    assert get_bin_path('python', opt_dirs=['/bin', '/usr/bin']) == '/usr/bin/python'
    assert get_bin_path('python', opt_dirs=['/usr/bin']) == '/usr/bin/python'
    assert get_bin_path('python', opt_dirs=['/bin']) == '/bin/python'
    assert get_bin_path('/usr/bin/python') == '/usr/bin/python'
    assert get_bin_path('/bin/python', opt_dirs=['/usr/bin']) == '/bin/python'

# Generated at 2022-06-12 23:28:42.561548
# Unit test for function get_bin_path
def test_get_bin_path():
    ''' Return result of basic functionality '''
    import os
    import tempfile
    from shutil import rmtree

    result = get_bin_path('pwd')
    assert result is not None

    # On AIX and HP-UX, default path doesn't include /sbin.
    # When /sbin is on PATH, it should return the path
    # for the executable with /sbin. This will not work
    # on Linux and other Unix systems because the
    # executable is not on /sbin on those OS's.
    if os.path.isfile('/sbin/pwd'):
        result = get_bin_path('pwd', ['/sbin'])
        assert result == '/sbin/pwd'

    tmpdir = tempfile.mkdtemp()

# Generated at 2022-06-12 23:28:51.731255
# Unit test for function get_bin_path
def test_get_bin_path():
    import os
    import tempfile
    import shutil
    import stat
    tmp_dir = tempfile.mkdtemp()
    os.mkdir(tmp_dir + "/exec")
    os.mkdir(tmp_dir + "/exec2")
    bin_name = "my_bin"
    bin_path = "%s/exec/%s" % (tmp_dir, bin_name)
    bin_path2 = "%s/exec2/%s" % (tmp_dir, bin_name)
    with open(bin_path, "w") as f:
        f.write("#!/bin/bash\n")
    with open(bin_path2, "w") as f:
        f.write("#!/bin/bash\n")
    st = os.stat(bin_path)

# Generated at 2022-06-12 23:29:00.723251
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('ls') == '/bin/ls'

    opt_dirs = ['/bin', '/usr/bin']
    assert get_bin_path('ls', opt_dirs) == '/bin/ls'
    assert get_bin_path('does-not-exist', opt_dirs) == '/usr/bin/does-not-exist'

    opt_dirs = ['/does/not/exist']
    assert get_bin_path('ls', opt_dirs) == '/sbin/ls'

# Generated at 2022-06-12 23:29:09.989085
# Unit test for function get_bin_path
def test_get_bin_path():
    (directory, name) = os.path.split(os.path.realpath(__file__))
    filename = os.path.join(directory, 'test_file')

    # Create a testing file
    test_file = open(filename, 'w')
    test_file.write('test_get_bin_path')
    test_file.close()
    os.chmod(filename, 755)

    # Test for existing file in current directory
    try:
        assert get_bin_path(filename) == filename
    except ValueError:
        assert False

    # Test for existing file in current directory with optional path
    try:
        assert get_bin_path(filename, [directory]) == filename
    except ValueError:
        assert False

    # Test for non-existing file in current directory with optional path

# Generated at 2022-06-12 23:29:20.410914
# Unit test for function get_bin_path

# Generated at 2022-06-12 23:29:24.797562
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path("fake_not_found_program")
    except ValueError:
        pass
    else:
        assert False, "Should raise exception"

    assert get_bin_path("cat")

# Generated at 2022-06-12 23:29:32.298562
# Unit test for function get_bin_path

# Generated at 2022-06-12 23:29:36.029223
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path('invalid-executable')
    except ValueError as e:
        assert 'Failed to find required executable' in str(e)

# Generated at 2022-06-12 23:29:40.151846
# Unit test for function get_bin_path
def test_get_bin_path():

    # Given
    arg = 'python'

    # When
    python_bin_path = get_bin_path(arg)

    # Then
    assert os.path.exists(python_bin_path)
    assert os.path.isfile(python_bin_path)
    assert is_executable(python_bin_path)

# Generated at 2022-06-12 23:29:49.465766
# Unit test for function get_bin_path
def test_get_bin_path():
    path = get_bin_path('cp')
    assert os.path.exists(path) and is_executable(path)

    try:
        # need a command that doesn't exist
        get_bin_path('fhafhakfhakdshjfkhafhdsa')
    except ValueError as e:
        assert 'Failed to find required executable' in str(e)
    else:
        # Should have raised exception
        assert False

    try:
        # need a command that doesn't exist and isn't in PATH
        get_bin_path('fhafhakfhakdshjfkhafhdsa', opt_dirs=['/bin'])
    except ValueError as e:
        assert 'Failed to find required executable' in str(e)

# Generated at 2022-06-12 23:29:58.191124
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        with open('/bin/true', 'w'):
            pass
        old_true = '/bin/true'
    except IOError:
        old_true = None

# Generated at 2022-06-12 23:30:05.511794
# Unit test for function get_bin_path
def test_get_bin_path():
    # Setup
    test_args = [
        "/bin/ls",
        "ls",
        "/usr/bin/ssh",
        "ssh",
    ]
    paths = [
        "/bin",
        "/usr/bin",
        "/usr/local/bin",
    ]

    # Execute
    for arg in test_args:
        bin_path = get_bin_path(arg, paths)

        # Verify
        assert os.path.exists(bin_path)



# Generated at 2022-06-12 23:30:15.168310
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path('/usr/bin/find', required=True)
    except ValueError as e:
        assert False, "Test with absolute path failed"

    try:
        get_bin_path('this_is_an_invalid_executable_name', required=True)
    except ValueError:
        pass
    else:
        assert False, "Test with invalid executable name should have failed"

    try:
        get_bin_path('find', required=True)
    except ValueError:
        assert False, "Test with valid executable name failed"
    else:
        pass

    try:
        get_bin_path('find', ['/usr/bin','/usr/local/bin'], required=True)
    except ValueError:
        assert False, "Test with extra search path failed"

# Generated at 2022-06-12 23:30:19.672705
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Test the get_bin_path function
    '''

    # Test an executable that exists
    path = get_bin_path('cat')
    assert path.endswith('/cat')

    # Test an executable that does not exist in a path
    try:
        get_bin_path('fake')
    except ValueError:
        # We expected an exception from get_bin_path
        pass
    else:
        # We did not get an exception from get_bin_path, and that's bad!
        raise Exception('test_get_bin_path: test failed!')

# Generated at 2022-06-12 23:30:21.689490
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('ls') == '/bin/ls'
    assert get_bin_path('python') == '/usr/bin/python'

# Generated at 2022-06-12 23:30:31.006696
# Unit test for function get_bin_path
def test_get_bin_path():
    """Unit test for function get_bin_path."""
    # Get the path for the find command
    try:
        find_path = get_bin_path('find')
        assert find_path, 'No path found for find command.'
    except ValueError as e:
        assert False, 'Error from get_bin_path: {0}'.format(str(e))
    else:
        assert os.access(find_path, os.X_OK), 'find command is not executable.'

# Generated at 2022-06-12 23:30:34.919685
# Unit test for function get_bin_path
def test_get_bin_path():
    paths = os.environ.get('PATH', '').split(os.pathsep)
    bp = get_bin_path('python', paths)
    assert os.path.isabs(bp)
    assert os.path.isfile(bp)

# Generated at 2022-06-12 23:30:45.151327
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test PATH contains required executable
    assert get_bin_path('python')
    assert get_bin_path('python', required=True)

    # Test executable exists in one of the optional paths
    opt_dirs = ['/opt/ansible/bin', '/opt/ansible/sbin']
    assert get_bin_path('ansible-playbook', opt_dirs=opt_dirs)

    # Test executable exists in both PATH and one of the optional paths
    opt_dirs = ['/usr/bin', '/usr/sbin']
    assert get_bin_path('python', opt_dirs=opt_dirs)

    # Test non-existent executable
    opt_dirs = ['/opt/ansible/bin', '/opt/ansible/sbin']

# Generated at 2022-06-12 23:30:57.148841
# Unit test for function get_bin_path
def test_get_bin_path():
    bin_path = get_bin_path('thebinary')
    assert bin_path == '/bin/thebinary' or os.path.exists(bin_path)

    bin_path = get_bin_path('nonexistentbinary')
    assert bin_path is None

    try:
        get_bin_path('/does/not/exist/thebinary')
        raise AssertionError('Expected exception')
    except ValueError as e:
        assert 'Failed to find required executable' in str(e)

    try:
        get_bin_path('nonexistentbinary', required=False)
        raise AssertionError('Expected exception')
    except ValueError as e:
        assert 'Failed to find required executable' in str(e)


# Generated at 2022-06-12 23:31:04.140956
# Unit test for function get_bin_path
def test_get_bin_path():

    def get_bin_path_with_dir(arg, opt_dirs):
        try:
            return get_bin_path(arg, opt_dirs=opt_dirs)
        except ValueError as e:
            raise AssertionError(e)

    assert get_bin_path('sh') not in ('sh', '/bin/sh')
    assert get_bin_path('sh', opt_dirs=['/bin']) == '/bin/sh'

    assert get_bin_path('sh', required=False) not in ('sh', '/bin/sh')
    assert get_bin_path('sh', opt_dirs=['/bin'], required=False) == '/bin/sh'


# Generated at 2022-06-12 23:31:12.545047
# Unit test for function get_bin_path
def test_get_bin_path():
    # test 1
    try:
        get_bin_path('/bin/cat')
    except ValueError as e:
        assert 'Failed to find required executable "/bin/cat" in paths: ' in str(e)
        assert '/bin:' in str(e)
        assert '/sbin:' in str(e)

    # test 2
    try:
        get_bin_path('/bin/cat', ['/bin'])
    except ValueError:
        assert False, 'Incorrect exception raised.'

    # test 3
    try:
        get_bin_path('/bin/cat', ['/bin', '/sbin'])
    except ValueError:
        assert False, 'Incorrect exception raised.'

    # test 4

# Generated at 2022-06-12 23:31:22.149590
# Unit test for function get_bin_path
def test_get_bin_path():
    # Path to unit test file
    test_file = "/tmp/ansible.test.file"

    # Create test file
    with open(test_file, 'wb') as f:
        f.write(b"")
    os.chmod(test_file, 0o777)

    try:
        # Valid file
        assert get_bin_path(test_file) == test_file
        # Invalid file
        try:
            get_bin_path("/tmp", required=True)
        except ValueError:
            raise ValueError('Failed to find required executable "/tmp" in paths: ')

    finally:
        if os.path.exists(test_file):
            os.unlink(test_file)

# Generated at 2022-06-12 23:31:31.534986
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil

    bin_name = 'test_binary'

    tmp_dir = tempfile.mkdtemp()
    bin_path = os.path.join(tmp_dir, bin_name)
    with open(bin_path, 'w'):
        os.chmod(bin_path, 0o0755)

    assert get_bin_path(bin_name, opt_dirs=[tmp_dir]) == bin_path

    shutil.rmtree(tmp_dir)

# Generated at 2022-06-12 23:31:37.611177
# Unit test for function get_bin_path
def test_get_bin_path():
    import sys
    import tempfile

    temp_dir = tempfile.gettempdir()

    # This will sometimes raise exceptions in the unit test if the
    # executable is not found
    get_bin_path(sys.executable)
    get_bin_path(os.path.basename(sys.executable))
    get_bin_path(os.path.basename(sys.executable), [os.path.dirname(sys.executable)])

    # This should not raise any exceptions, even if paths point to
    # non-existing locations.
    get_bin_path(os.path.basename(sys.executable), [temp_dir])

# Generated at 2022-06-12 23:31:47.535386
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('python') == '/usr/bin/python'
    assert get_bin_path('python', ['/usr/bin']) == '/usr/bin/python'
    assert get_bin_path('python', ['/usr/bin'], True) == '/usr/bin/python'
    assert get_bin_path('python', ['/nonexistent'], False) == '/usr/bin/python'
    assert get_bin_path('nonexistent', required=False) is None

    try:
        get_bin_path('nonexistent')
        raise AssertionError("Expected ValueError because executable is not found")
    except ValueError:
        pass


# Generated at 2022-06-12 23:31:53.533784
# Unit test for function get_bin_path
def test_get_bin_path():
    from ansible.module_utils import basic

    def assert_equals(cmd, options, expected):
        assert get_bin_path(cmd) == expected, \
            'wrong result for get_bin_path("%s"): %s' % (cmd, basic.jsonify(options))

    assert_equals('python', [], '/usr/bin/python')
    assert_equals('ssh', [], '/usr/bin/ssh')
    assert_equals('/usr/bin/python', [], '/usr/bin/python')
    assert_equals('/usr/bin/python', ['/path/not/exist'], '/usr/bin/python')

    # Test for optional options
    assert_equals('/bin/ls', ['/bin'], '/bin/ls')

# Generated at 2022-06-12 23:32:02.323194
# Unit test for function get_bin_path
def test_get_bin_path():
    # This is more of a functional test to assure that get_bin_path
    # will always return the path to the current python interpreter
    # This test should always pass no matter what the current environments PATH value is
    path = get_bin_path('python')
    try:
        assert os.path.exists(path)
    except Exception as e:
        raise AssertionError('get_bin_path returned a path that does not exist (%s) : %s' % (path, e))
    # This test should pass unless the current python interpreter is not executable
    try:
        assert is_executable(path)
    except Exception as e:
        raise AssertionError('get_bin_path returned a path (%s) that is not executable : %s' % (path, e))

# Generated at 2022-06-12 23:32:13.427880
# Unit test for function get_bin_path
def test_get_bin_path():
    ''' Ensure get_bin_path returns correct answers for correct inputs, and errors for incorrect inputs '''
    import unittest
    import shutil
    import tempfile

    class TestGetBinPath(unittest.TestCase):
        # ensure that get_bin_path will find common linux commands
        def test_get_bin_path_commands(self):
            self.assertEqual(get_bin_path('ls'), '/bin/ls')
            self.assertEqual(get_bin_path('cp'), '/bin/cp')
            self.assertEqual(get_bin_path('mv'), '/bin/mv')
            self.assertEqual(get_bin_path('rsync'), '/usr/bin/rsync')

        # ensure that get_bin_path will find common macOS commands

# Generated at 2022-06-12 23:32:24.006573
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Test the module's get_bin_path function
    '''
    import platform

    # Test that running it with an invalid path should raise a ValueError
    try:
        get_bin_path("invalid")
        assert False, "Failed to raise a ValueError for an invalid executable name"
    except ValueError:
        pass

    # Test that running it with an invalid path should raise a ValueError
    try:
        get_bin_path("/invalid")
        assert False, "Failed to raise a ValueError for an invalid executable name"
    except ValueError:
        pass

    # Test that running it with an invalid path should raise a ValueError

# Generated at 2022-06-12 23:32:26.197901
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('/usr/bin/env') == '/usr/bin/env'
    assert get_bin_path('env') == '/usr/bin/env'

# Generated at 2022-06-12 23:32:38.776959
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile

    def write_file(f, line):
        f.write(line)
        f.close()
        os.chmod(f.name, 0o755)


# Generated at 2022-06-12 23:32:46.204001
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('env') == '/usr/bin/env'
    assert get_bin_path('/usr/bin/env') == '/usr/bin/env'
    assert get_bin_path('env', ['/usr/bin']) == '/usr/bin/env'

    import pytest
    with pytest.raises(ValueError):
        get_bin_path('_this_does_not_exists_')

# Generated at 2022-06-12 23:32:54.135869
# Unit test for function get_bin_path
def test_get_bin_path():
    which = get_bin_path('which')
    assert which == '/usr/bin/which'
    # shouldn't work as 'which' is not in the second path
    try:
        which = get_bin_path('which', ['/usr/bin', '/usr/local/bin'])
        print(which)
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError")
    # should work as 'which' is in the second path
    which = get_bin_path('which', ['/usr/local/bin', '/usr/bin'])
    assert which == '/usr/bin/which'

# Generated at 2022-06-12 23:32:59.552731
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        # should not throw an exception in normal circumstances
        get_bin_path('ls')
    except Exception:
        raise Exception("Failed to find required executable 'ls'")

    try:
        # should raise exception when not found
        get_bin_path('nonexistent_executable')
    except Exception:
        pass  # Expected
    else:
        raise Exception("Exception not raised when required executable is not found")

# Generated at 2022-06-12 23:33:08.854327
# Unit test for function get_bin_path
def test_get_bin_path():
    '''Unit test for function get_bin_path'''
    # check for default paths
    assert get_bin_path('touch') == '/bin/touch'
    assert get_bin_path('ls') == '/bin/ls'
    # check for additional directories
    assert get_bin_path('touch', ['/usr/bin']) == '/usr/bin/touch'
    assert get_bin_path('ls', ['/usr/bin']) == '/usr/bin/ls'
    # check for error handling
    try:
        get_bin_path('not_existing_command')
    except ValueError as e:
        assert True
    else:
        assert False



# Generated at 2022-06-12 23:33:17.770257
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil

    bin_path = get_bin_path('python3')

    assert os.path.isfile(bin_path)

    # test with optional dirs
    opt_dirs = ['/usr/bin']
    bin_path = get_bin_path('python3', opt_dirs)
    assert opt_dirs[0] in bin_path

    # ensure PATH is still intact
    new_dir = tempfile.mkdtemp()
    bin_file = os.path.join(new_dir, 'test')
    with open(bin_file, 'w') as f:
        f.write('#!/bin/sh\necho hello world')
    os.chmod(bin_file, 0o755)

# Generated at 2022-06-12 23:33:19.328038
# Unit test for function get_bin_path
def test_get_bin_path():
    path = get_bin_path('echo')
    assert path == '/bin/echo'

    from ansible.module_utils.six.moves import shlex_quote
    escaped_path = shlex_quote(path)
    assert escaped_path == "'/bin/echo'"

# Generated at 2022-06-12 23:33:30.185222
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile

# Generated at 2022-06-12 23:33:32.772040
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('python') == os.path.realpath(sys.executable)
    assert get_bin_path('/bin/python') == '/bin/python'
    assert get_bin_path('/nosuchpath/python') == '/nosuchpath/python'

# Generated at 2022-06-12 23:33:44.322834
# Unit test for function get_bin_path
def test_get_bin_path():
    # Assume the executable "true" is available
    assert get_bin_path('true', ['/bin']) is not None

    # Assume the executable "true" is available in one of the dirs: /bin, /usr/bin
    assert get_bin_path('true', ['/usr/bin']) is not None

    # Assume the executable "true-not-existing" is not available
    try:
        res = get_bin_path('true-not-existing', ['/bin'], True)
    except ValueError:
        assert 1, "ValueError has been raised as expected"
    else:
        assert 0, "ValueError has not been raised"

# vim: expandtab tabstop=4 fencen=utf-8 ff=unix:

# Generated at 2022-06-12 23:33:51.779180
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil
    import sys

    # Create a fake executable in a temporary directory
    tmpdir = tempfile.mkdtemp()
    executable = os.path.join(tmpdir, 'executable')
    with open(executable, 'w') as file_obj:
        file_obj.write('#!/bin/sh\necho it works')

    # Make it executable
    os.chmod(executable, 0o755)

    # Ensure it is found
    assert get_bin_path('executable', opt_dirs=[tmpdir]) == executable

    # Ensure it is not found
    try:
        get_bin_path('executable')
    except ValueError as exc:
        assert 'Failed to find required executable' in str(exc)

# Generated at 2022-06-12 23:34:03.166928
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test normal path search
    bin_path = get_bin_path('ls')
    assert bin_path == '/bin/ls'

    # Test extra search path
    bin_path = get_bin_path('git', opt_dirs=['/usr/local/bin'])
    assert bin_path == '/usr/local/bin/git'

    # Test missing executable
    try:
        get_bin_path('fake-executable')
    except ValueError:
        pass
    else:
        assert False, 'Expected exception failed to raise'

    # Test fake directory
    try:
        get_bin_path('/fake-directory')
    except ValueError:
        pass
    else:
        assert False, 'Expected exception failed to raise'

    # Test fake file

# Generated at 2022-06-12 23:34:14.352110
# Unit test for function get_bin_path
def test_get_bin_path():
    test_paths = [
        '/sbin', '/usr/sbin', '/usr/local/sbin',
        '/bin', '/usr/bin', '/usr/local/bin',
        '/usr/libexec',
    ]

    # Test with no optional search paths defined
    # Ensure path = /bin
    path = get_bin_path('ls')
    assert '/bin/ls' == path

    # Test with optional search paths defined
    # Ensure path = /bin, /usr/bin, /usr/local/bin, /usr/libexec, /sbin, /usr/sbin, /usr/local/sbin
    path = get_bin_path('ls', test_paths)
    assert '/bin/ls' == path

    # Test with optional search paths defined, but with the path missing from the optional paths
    # Ensure path

# Generated at 2022-06-12 23:34:22.959467
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test with no optional directories
    path = get_bin_path('pip')
    assert os.path.exists(path)

    # Test with optional directory
    path = get_bin_path('pip', [os.environ.get('PATH')])
    assert os.path.exists(path)

    # Non-existent command should throw an exception
    try:
        get_bin_path('pip-not-found', [os.environ.get('PATH')])
        raise Exception('Hit this line, but should not have.')
    except ValueError as e:
        assert 'Failed to find required executable' in str(e)

# Generated at 2022-06-12 23:34:31.355676
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Ensure that get_bin_path() finds some executables
    '''


# Generated at 2022-06-12 23:34:35.316585
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('env') == get_bin_path('env', [])
    test_path = '/home/test'
    assert get_bin_path('env', [test_path]) == os.path.join(test_path, 'env')

# Generated at 2022-06-12 23:34:43.454942
# Unit test for function get_bin_path
def test_get_bin_path():
    '''Test function get_bin_path'''
    from shutil import rmtree
    from tempfile import mkdtemp

    # this executable should always exist in the paths that we are testing
    test_exes = ['cat', 'ls', 'sha1']

    # create test directories and executables

# Generated at 2022-06-12 23:34:53.454183
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('/bin/ls') == '/bin/ls'
    assert get_bin_path('ls') == '/bin/ls'
    assert get_bin_path('ls', ['/bin']) == '/bin/ls'
    assert get_bin_path('ls', ['/bin', '/usr/bin']) == '/bin/ls'
    assert get_bin_path('ls', ['/usr/bin', '/bin']) == '/bin/ls'
    assert get_bin_path('ls', ['/bin/fake-bin'], required=False) is None
    assert get_bin_path('/fake-path/ls', required=False) is None
    try:
        get_bin_path('/fake-path/ls')
        assert False
    except ValueError:
        assert True

# Generated at 2022-06-12 23:35:00.709251
# Unit test for function get_bin_path
def test_get_bin_path():
    """ Test function get_bin_path """
    import tempfile

    # Ensure that get_bin_path raises an error when the executable is not found
    # in the given path
    try:
        get_bin_path('nonexistent_command', [tempfile.gettempdir()])
    except ValueError:
        pass
    else:
        raise AssertionError('get_bin_path failed to raise an exception when an executable is not found')

    # Ensure that get_bin_path returns the absolute path of the executable when
    # it is found
    ret = get_bin_path('ls', [tempfile.gettempdir()])
    assert ret == os.path.abspath(os.path.join(tempfile.gettempdir(), 'ls'))

# Generated at 2022-06-12 23:35:09.617620
# Unit test for function get_bin_path
def test_get_bin_path():
    # assert get_bin_path('/bin/ls') == '/bin/ls'
    # assert get_bin_path('ls') == '/bin/ls'
    assert get_bin_path('ls') == os.path.join(os.environ.get('PATH', '').split(os.pathsep)[0], 'ls')
    assert get_bin_path('ls', ['/usr/bin']) == os.path.join('/usr/bin', 'ls')
    assert get_bin_path('ls', ['/usr/bin'], True) == os.path.join('/usr/bin', 'ls')
    # assert get_bin_path('ls', ['/usr/bin'], False) == os.path.join('/usr/bin', 'ls')


# Generated at 2022-06-12 23:35:13.698192
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test to make sure it finds the executable
    get_bin_path('cat')
    # Make sure that it raises an exception if the executable does not exist
    try:
        get_bin_path("xyz")
    except ValueError:
        pass

# Generated at 2022-06-12 23:35:22.365497
# Unit test for function get_bin_path
def test_get_bin_path():
    from ansible.module_utils._text import to_native
    import tempfile
    import shutil


# Generated at 2022-06-12 23:35:31.931826
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('ls') == '/bin/ls'
    assert get_bin_path('ls', opt_dirs=['/bin']) == '/bin/ls'
    try:
        get_bin_path('ls', opt_dirs=['/notadir'])
    except ValueError as e:
        assert 'Failed to find required executable "ls" in paths: /notadir' in str(e)
    else:
        assert False

# Generated at 2022-06-12 23:35:44.014033
# Unit test for function get_bin_path
def test_get_bin_path():
    import unittest
    import tempfile
    import shutil
    import subprocess

    class BaseTestCase(unittest.TestCase):
        '''
        Common code to set up and tear down temporary directories
        '''
        def setUp(self):
            tmp = tempfile.mkdtemp()
            self.addCleanup(self._cleanup, tmp)
            self.exe = os.path.join(tmp, 'bash')
            self.exe_bin = '/bin/bash'
            self.exe_sbin = '/sbin/sysctl'

        def _cleanup(self, tmp):
            shutil.rmtree(tmp)


# Generated at 2022-06-12 23:35:47.332398
# Unit test for function get_bin_path
def test_get_bin_path():
    bin_path = get_bin_path('python')
    assert os.path.exists(bin_path)
    assert is_executable(bin_path)

    bin_path = get_bin_path('ansible-test-does-not-exist')
    assert bin_path is None

# Generated at 2022-06-12 23:35:55.636066
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        test_path = get_bin_path('foo')
    except ValueError:
        pass
    else:
        raise AssertionError('get_bin_path should have failed for non-existent file')

    test_path = get_bin_path('python')

    # Just check that it returns a string
    assert isinstance(test_path, str)

    # Just check that it returns an absolute path
    assert test_path.startswith('/')

# Generated at 2022-06-12 23:36:04.218117
# Unit test for function get_bin_path
def test_get_bin_path():
    # No arg tests
    arg = None
    opt_dirs = None
    found = False
    try:
        get_bin_path(arg,opt_dirs)
    except ValueError:
        found = True
    assert found, 'get_bin_path should throw a ValueError when no arg given'

    # Not found test
    arg = 'nothere'
    found = False
    try:
        get_bin_path(arg)
    except ValueError:
        found = True
    assert found, 'get_bin_path should throw a ValueError when not found'

    # Found in path test
    arg = 'ls'
    opt_dirs = None
    found = False

# Generated at 2022-06-12 23:36:14.366517
# Unit test for function get_bin_path
def test_get_bin_path():
    ret = get_bin_path('sh')
    assert ret == '/bin/sh'
    ret = get_bin_path('sh', ['/foo'])
    assert ret == '/bin/sh'
    try:
        ret = get_bin_path('sh', ['/foo'], True)
    except:
        assert True
    ret = get_bin_path('sh', ['test'])
    assert ret == '/bin/sh'
    ret = get_bin_path('sh', ['/bin'])
    assert ret == '/bin/sh'
    ret = get_bin_path('sh', ['/foo/bar'])
    assert ret == '/bin/sh'
    try:
        ret = get_bin_path('sh', ['/foo/bar'], True)
    except:
        assert True

# Generated at 2022-06-12 23:36:23.419719
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    get_bin_path function test
    '''
    # Normal usage
    expected_result = '/bin/sh'
    assert get_bin_path('sh') == expected_result

    # PATH is empty
    os.environ['PATH'] = ''
    expected_result = '/bin/sh'
    assert get_bin_path('sh') == expected_result

    # Executable does not exist
    expected_result = ValueError
    try:
        get_bin_path('sdlkfj')
    except ValueError as e:
        assert type(e).__name__ == expected_result.__name__
        del e

    # Path is not executable
    expected_result = ValueError
    with open('/tmp/foo', 'w') as f:
        f.write('foo')

# Generated at 2022-06-12 23:36:29.945957
# Unit test for function get_bin_path
def test_get_bin_path():
    assert '/bin/bash' == get_bin_path('bash')
    assert '/bin/bash' == get_bin_path('bash', ['/usr/bin', '/bin', '/usr/sbin'])
    assert '/sbin/ping' == get_bin_path('ping', opt_dirs=['/usr/bin', '/bin', '/usr/sbin', '/bin'])
    assert '/sbin/ping' == get_bin_path('ping', opt_dirs=['/bin', '/sbin', '/usr/sbin'])
    try:
        assert '/sbin/ping' == get_bin_path('ping', ['/usr/bin', '/bin', '/usr/sbin'])
    except ValueError:
        pass
    else:
        assert False, "Should have raised value error"

# Generated at 2022-06-12 23:36:37.092669
# Unit test for function get_bin_path
def test_get_bin_path():
    from tempfile import mkdtemp

    test_paths = ['/bin', '/usr/bin', '/usr/local/bin']
    test_bin = 'test_ansible_module_util_get_bin_path'

    # Test that expected exception is raised if required is None and executable is not found
    with open(test_bin, 'w') as f:
        f.write('#!/usr/bin/env python2\n')
    os.chmod(test_bin, 0o755)
    try:
        get_bin_path(test_bin, test_paths, required=None)
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "%s" in paths: %s' % (test_bin, ':'.join(test_paths))

# Generated at 2022-06-12 23:36:48.194430
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('cat') == '/bin/cat'
    assert get_bin_path('cat', opt_dirs=['/usr/bin']) == '/usr/bin/cat'
    assert get_bin_path('cat', opt_dirs=['/usr/bin', '/bin']) == '/bin/cat'
    assert get_bin_path('cat', opt_dirs=['/usr/sbin']) == '/usr/sbin/cat'
    assert get_bin_path('cat', opt_dirs=['/usr/local/sbin']) == '/usr/local/sbin/cat'
    assert get_bin_path('cat', opt_dirs=['/usr/bin/bogus']) == '/bin/cat'

# Generated at 2022-06-12 23:37:00.980792
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('ls')
    assert get_bin_path('ls', required=True)
    assert get_bin_path('ls', opt_dirs=[os.path.dirname(os.path.realpath(__file__))])

    try:
        get_bin_path('foobar')
    except ValueError as e:
        assert 'foobar' in str(e)
    finally:
        pass
    try:
        get_bin_path('foobar', required=True)
    except ValueError as e:
        assert 'foobar' in str(e)
    finally:
        pass

# Generated at 2022-06-12 23:37:10.704970
# Unit test for function get_bin_path
def test_get_bin_path():

    # Test missing commands in PATH
    missing_commands = ['foo', 'bar', 'baz']
    for mcmd in missing_commands:
        try:
            get_bin_path(mcmd)
        except ValueError:
            pass
        except Exception:
            raise AssertionError('get_bin_path succeeded in finding %s, but should have failed' % mcmd)
        else:
            raise AssertionError('get_bin_path found %s, but it is not installed' % mcmd)

    # Test existing commands in PATH
    existing_commands = ['ls', 'chmod', 'ip']

# Generated at 2022-06-12 23:37:21.238868
# Unit test for function get_bin_path
def test_get_bin_path():

    import os

    # Test 1: successful path lookup
    if os.path.exists('/bin/cat'):
        assert "/bin/cat" == get_bin_path("cat", [], True)

    # Test 2: unsuccessful path lookup without required param
    try:
        get_bin_path("cat", [], False)
        assert False
    except ValueError:
        assert True

    # Test 3: unsuccessful path lookup with required param
    try:
        get_bin_path("cat", [], True)
        assert False
    except ValueError:
        assert True

    # Test 4: unsuccessful path lookup with optional dirs
    try:
        get_bin_path("cat", ["/bin", "/usr/bin"], True)
        assert False
    except ValueError:
        assert True

# Generated at 2022-06-12 23:37:22.964437
# Unit test for function get_bin_path
def test_get_bin_path():
    import pytest

    assert get_bin_path("sh") == '/bin/sh'
    with pytest.raises(ValueError):
        get_bin_path("not_a_real_executable")

# Generated at 2022-06-12 23:37:23.904138
# Unit test for function get_bin_path
def test_get_bin_path():
    path = get_bin_path('lsb_release')

# Generated at 2022-06-12 23:37:28.339255
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test for valid call with path in path
    get_bin_path('python3')

    # Test for valid call with path not in path
    with os.environ.copy():
        os.environ['PATH'] = ''
        get_bin_path('python3', opt_dirs=['/usr/bin'])

# Generated at 2022-06-12 23:37:39.377604
# Unit test for function get_bin_path
def test_get_bin_path():
    '''Test function get_bin_path'''

    # Normal list of test cases