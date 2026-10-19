

# Generated at 2022-06-12 23:27:47.417918
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('sh') == '/bin/sh'
    assert get_bin_path('sh', opt_dirs=['/bin']) == '/bin/sh'
    assert get_bin_path('sh', opt_dirs=['/bin'], required=False) == '/bin/sh'
    assert get_bin_path('doesnotexist', opt_dirs=['/bin'], required=False) is None
    assert get_bin_path('doesnotexist', opt_dirs=['/bin']) == '/bin/doesnotexist'

# Generated at 2022-06-12 23:27:52.786424
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('ls') == '/bin/ls'

    # should throw exception if required is true
    from ansible.module_utils.common.process import get_bin_path
    try:
        import ansible.module_utils.common.impexception
        get_bin_path('does-not-exist-in-any-path', required=True)
        assert False, "required=True should have thrown"
    except ansible.module_utils.common.impexception:
        assert True

    # should throw exception if 'required' exists in kwargs
    from ansible.module_utils.common.process import get_bin_path

# Generated at 2022-06-12 23:27:58.482907
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('ls', ['/bin', '/usr/bin']) == '/bin/ls'
    assert get_bin_path('ls', ['/bin']) == '/bin/ls'
    assert get_bin_path('ls', []) == '/bin/ls'
    assert get_bin_path('ls', ['.']) == './ls'
    assert get_bin_path('ls', ['/bin', '/usr/bin', '/lsdir']) == '/bin/ls'
    assert get_bin_path('ls', ['/lsdir', '/bin', '/usr/bin']) == '/bin/ls'

# Generated at 2022-06-12 23:27:59.566305
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('sh') == '/bin/sh'



# Generated at 2022-06-12 23:28:05.012821
# Unit test for function get_bin_path
def test_get_bin_path():
    from ansible.module_utils._text import to_bytes
    import sys

    bin_path = get_bin_path('python2')
    assert isinstance(bin_path, bytes)
    assert not to_bytes(sys.executable).startswith(bin_path)

    bin_path = get_bin_path('python2', opt_dirs=[to_bytes(os.path.dirname(sys.executable))])
    assert isinstance(bin_path, bytes)
    assert to_bytes(sys.executable).startswith(bin_path)

    try:
        get_bin_path('npython2')
    except ValueError:
        pass
    else:
        assert False, "get_bin_path should have thrown an exception"


# Generated at 2022-06-12 23:28:12.520034
# Unit test for function get_bin_path
def test_get_bin_path():
    bin_path = '/bin/ls'
    if os.path.exists(bin_path) and os.path.isfile(bin_path) and is_executable(bin_path):
        assert get_bin_path('ls') == bin_path
        assert get_bin_path('ls', opt_dirs=['/bin']) == bin_path
        assert get_bin_path('ls', opt_dirs=['/usr/bin']) == bin_path
        assert get_bin_path('ls', opt_dirs=['/usr/bin', '/bin']) == bin_path
        assert get_bin_path('ls', opt_dirs=['/bin', '/usr/bin']) == bin_path

# Generated at 2022-06-12 23:28:14.848689
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('sh')
    try:
        get_bin_path('bad-exec')
        assert 0, 'unexpected succeeded'
    except ValueError:
        pass

# Generated at 2022-06-12 23:28:16.126213
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('sh') == '/bin/sh'

# Generated at 2022-06-12 23:28:25.007243
# Unit test for function get_bin_path
def test_get_bin_path():
    #
    # Expected to fail
    #
    # no such executable
    try:
        get_bin_path('no_such_executable', [])
        assert False
    except ValueError:
        pass

    # existing file, but not executable
    with open('not_executable_file', 'w') as tf:
        tf.write('not executable')
    try:
        get_bin_path('not_executable_file', [])
        assert False
    except ValueError:
        pass
    os.unlink('not_executable_file')

    #
    # Expected to success
    #

    # existing executable in PATH
    assert get_bin_path('ls', []) == '/bin/ls'

    # existing executable in PATH, but with a wrong name

# Generated at 2022-06-12 23:28:29.010059
# Unit test for function get_bin_path
def test_get_bin_path():
    if os.path.exists('/usr/bin/python'):
        assert get_bin_path('python') == '/usr/bin/python'
    assert get_bin_path('does-not-exist') == None
    try:
        get_bin_path('does-not-exist', required=True)
        assert False, "expected ValueError"
    except ValueError as e:
        assert 'Failed to find' in str(e)

# Generated at 2022-06-12 23:28:40.376113
# Unit test for function get_bin_path
def test_get_bin_path():
    # success case
    try:
        assert get_bin_path('/bin/ls') == '/bin/ls'
    except:
        raise ValueError('Failed to find required executable "/bin/ls"')

    # Failure case
    try:
        assert get_bin_path('ls_nonexist') == '/bin/ls'
        raise ValueError('Expected ValueError exception not raised')
    except ValueError:
        pass

    # success case with optional arg opt_dirs
    try:
        assert get_bin_path('ls_test2', opt_dirs=['/home/test1/']) == '/home/test1/ls_test2'
    except:
        raise ValueError('Failed to find required executable "ls_test2"')

# Generated at 2022-06-12 23:28:42.775030
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path("ansible-playbook", opt_dirs=["/usr/bin"]) == "/usr/bin/ansible-playbook"

# Generated at 2022-06-12 23:28:51.874235
# Unit test for function get_bin_path
def test_get_bin_path():
    # Case 1: get_bin_path finds executable within the PATH
    args = dict(
        arg='dummy_prog',
        opt_dirs=None,
        required=None,
    )
    bin_path = get_bin_path(**args)
    assert '/tests/utils/dummy_prog' in bin_path

    # Case 2: get_bin_path finds executable within alternate PATH
    args = dict(
        arg='dummy_prog',
        opt_dirs=['/bin', '/usr/bin'],
        required=None,
    )
    bin_path = get_bin_path(**args)
    assert '/tests/utils/dummy_prog' in bin_path

    # Case 3: get_bin_path fails to find executable within the PATH

# Generated at 2022-06-12 23:29:02.963621
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil

    # create temporary directory and file
    dir_path = tempfile.mkdtemp()
    open(os.path.join(dir_path, 'test_file'), 'a').close()

    try:
        # test get_bin_path and raise error for missing file
        try:
            get_bin_path('test_file')
        except ValueError as e:
            assert "Failed to find required executable \"test_file\" in paths:" in str(e)
        else:
            raise Exception('expected ValueError was not raised')

        # test get_bin_path will return path with valid input
        assert get_bin_path('test_file', [dir_path]) == os.path.join(dir_path, 'test_file')

    finally:
        # cleanup
        shutil.r

# Generated at 2022-06-12 23:29:11.564506
# Unit test for function get_bin_path
def test_get_bin_path():
    from random import choice
    from ansible.module_utils.common.text import random_alphanum
    from ansible.module_utils.common.file import atomic__write_file

    # noinspection SpellCheckingInspection
    bin_dirs = [
        '/bin',
        '/usr/bin',
        '/usr/local/bin',
        '/usr/local/bin',
        '/foo'
    ]
    bin_names = [
        'ls',
        'df',
        'sh',
        'bash',
        'python',
        'python2'
    ]
    # Create a corrupt file that looks like a binary by setting executable bit
    name = '%s' % random_alphanum(32)

# Generated at 2022-06-12 23:29:20.739801
# Unit test for function get_bin_path
def test_get_bin_path():
    assert '/bin/cat' == get_bin_path('cat')
    assert '/bin/cat' == get_bin_path('cat', [])
    assert '/bin/cat' == get_bin_path('cat', None)
    assert '/bin/cat' == get_bin_path('cat', ['/bin'])
    assert '/bin/cat' == get_bin_path('cat', ['/bin/'])
    assert '/bin/cat' == get_bin_path('cat', ['/bin', '/usr/bin'])
    assert '/bin/cat' == get_bin_path('cat', ['/bin/', '/usr/bin'])


# Generated at 2022-06-12 23:29:30.902956
# Unit test for function get_bin_path
def test_get_bin_path():
    if os.path.exists('/bin/python') and not os.path.exists('/bin/python2'):
        os.symlink('/bin/python', '/bin/python2')
    assert '/bin/python2' == get_bin_path('python2', opt_dirs=['/bin'])
    if os.path.exists('/bin/python2'):
        os.remove('/bin/python2')
    try:
        get_bin_path('python2', opt_dirs=['/bin'])
        assert False
    except ValueError as e:
        assert 'Failed to find required executable "python2" in paths: /bin' == str(e)
    assert '/sbin/ip' == get_bin_path('ip')

# Generated at 2022-06-12 23:29:42.243723
# Unit test for function get_bin_path
def test_get_bin_path():
    from ansible.module_utils.six import unichr
    from tempfile import mkdtemp

    # Test directories for get_bin_path
    def setup_test_dirs():
        bin_path = '/bin'
        fail_path = '/usr/fail'
        success_path = '/usr/success'
        paths = [bin_path, fail_path, success_path]
        for p in paths:
            if not os.path.exists(p):
                os.makedirs(p)
        return bin_path, fail_path, success_path

    # Test invalid /bin/sh path
    def test_get_bin_path_fail(paths):
        bin_path = get_bin_path('sh', opt_dirs=paths)
        assert bin_path == '/bin/sh'

    #

# Generated at 2022-06-12 23:29:50.481675
# Unit test for function get_bin_path
def test_get_bin_path():
    import pytest

    # test for command in PATH
    assert get_bin_path('python') == '/usr/bin/python'

    # test for command not in PATH
    try:
        get_bin_path('not_there')
    except ValueError as e:
        assert "not found" in str(e)
    else:
        pytest.fail("Expected ValueError")

    # test for command in specified directory
    assert get_bin_path('chmod', opt_dirs=['/bin'], required=False) == '/bin/chmod'

    # test for command with file (not executable) in PATH
    # This should return the file as os.path.exists(path) would be true

# Generated at 2022-06-12 23:29:53.714464
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path('missing-executable')
    except Exception:
        pass
    else:
        raise AssertionError('Expected get_bin_path to raise an exception')



# Generated at 2022-06-12 23:29:59.990329
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        # command succeed
        get_bin_path('sh')
        # command failed
        get_bin_path('no_such_command')
    except ValueError:
        pass
    else:
        assert False  # nosec

# Generated at 2022-06-12 23:30:00.957154
# Unit test for function get_bin_path
def test_get_bin_path():
    get_bin_path('curl')

# Generated at 2022-06-12 23:30:11.674599
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Test function get_bin_path with different inputs.
    '''
    # Test 1: Check if bin_path exists in path
    exported_path = '/bin:/usr/bin:/usr/local/bin'
    bin_path = get_bin_path('ls', required=True)
    assert bin_path == '/bin/ls'
    # Test 2: Check if bin_path exists in path or opt_dirs
    bin_path = get_bin_path('ls', opt_dirs=['/bin', '/usr/bin'])
    assert bin_path == '/bin/ls'
    # Test 3: Check if bin_path exists in opt_dirs
    bin_path = get_bin_path('ls', opt_dirs=['/opt/bin', '/opt/usr/bin'])
    assert bin_path

# Generated at 2022-06-12 23:30:18.583721
# Unit test for function get_bin_path
def test_get_bin_path():
    path = '/bin'
    bin_name = 'ls'
    assert get_bin_path(bin_name, [path]) == os.path.join(path, bin_name)

    bin_name = 'no_such_exec'
    try:
        get_bin_path(bin_name, [path])
    except ValueError:
        pass

# Generated at 2022-06-12 23:30:22.651720
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path('cat', opt_dirs=['/bin', '/sbin'])
    except ValueError as ex:
        assert False, "Unexpected ValueError: %s" % str(ex)

    try:
        get_bin_path('missing_executable')
        assert False, "Expected ValueError"
    except ValueError as ex:
        assert True

# Generated at 2022-06-12 23:30:31.656332
# Unit test for function get_bin_path
def test_get_bin_path():
    # Always use absolute paths for unit tests
    abs_paths = [os.path.join(os.path.dirname(__file__), 'data', 'bin'), os.path.join(os.path.dirname(__file__), '..', 'lib')]
    try:
        path = get_bin_path('test_get_bin_path', abs_paths)
    except ValueError:
        assert False, 'Failed to find test_get_bin_path utility'
    # ensure that it returns a fully qualified path
    assert os.path.isabs(path)

    # test that it fails gracefully

# Generated at 2022-06-12 23:30:42.732268
# Unit test for function get_bin_path
def test_get_bin_path():
    # try /bin/sh
    assert get_bin_path('sh') == '/bin/sh'
    # try a non-existent executable
    try:
        get_bin_path('no-such-executable')
        assert False
    except ValueError as e:
        pass
    # try /sbin/ip
    assert get_bin_path('ip') == '/sbin/ip'
    # try /bin/sh - search ['/sbin', '/bin']
    assert get_bin_path('sh', opt_dirs=['/sbin', '/bin']) == '/bin/sh'
    # try /sbin/ip - search ['/sbin', '/bin']
    assert get_bin_path('ip', opt_dirs=['/sbin', '/bin']) == '/sbin/ip'
    # try /

# Generated at 2022-06-12 23:30:54.782287
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('cat') == '/bin/cat'
    assert get_bin_path('cat', ['/usr/bin']) == '/usr/bin/cat'
    assert get_bin_path('cat', ['/usr/bin', '/bin']) == '/bin/cat'
    assert get_bin_path('cat', ['/usr/bin', '/bin'], None) == '/bin/cat'
    assert get_bin_path('cat', ['/usr/bin', '/bin'], True) == '/bin/cat'
    assert get_bin_path('cat', ['/usr/bin', '/bin'], False) == '/bin/cat'

    assert get_bin_path('nonsense') == '/bin/nonsense'


# Generated at 2022-06-12 23:30:58.057875
# Unit test for function get_bin_path
def test_get_bin_path():
    test_path = "/bin:/usr/bin:/usr/local/bin"
    os.environ['PATH'] = test_path
    assert get_bin_path("bash") == "/bin/bash"
    assert get_bin_path("notthere") == None

# Generated at 2022-06-12 23:31:08.624763
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil
    import sys

    # Create temp dir
    tmp_dir = tempfile.mkdtemp()
    sys.path.append(tmp_dir)

    # Create temp executable file
    temp_ex = tempfile.NamedTemporaryFile(dir=tmp_dir, delete=False)
    temp_ex.write(b'#!/bin/sh\necho "I am test"')
    os.chmod(temp_ex.name, 0o755)
    temp_ex.close()

    # Check that we were able to locate our temp executable
    assert get_bin_path(os.path.basename(temp_ex.name), opt_dirs=[tmp_dir]) == temp_ex.name

    # Check cleanup
    shutil.rmtree(tmp_dir)

# Generated at 2022-06-12 23:31:19.714906
# Unit test for function get_bin_path
def test_get_bin_path():
    import shutil, tempfile


# Generated at 2022-06-12 23:31:26.556024
# Unit test for function get_bin_path
def test_get_bin_path():
    # verify expected behavior
    assert get_bin_path('python2.7')

    # verify the function raises an exception when the executable cannot be found
    try:
        get_bin_path('this-executable-does-not-exist')
    except ValueError:
        pass
    else:
        raise AssertionError('Expected ValueError')

    # verify the function raises an exception when the executable is a directory
    try:
        get_bin_path('/')
    except ValueError:
        pass
    else:
        raise AssertionError('Expected ValueError')

    # verify the function raises an exception when the executable isn't executable
    try:
        get_bin_path('/etc/resolv.conf')
    except ValueError:
        pass

# Generated at 2022-06-12 23:31:33.808932
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('sh') == '/bin/sh'
    assert get_bin_path('cat') == '/bin/cat'
    assert get_bin_path('touch') == '/bin/touch'
    assert get_bin_path('less') == '/usr/bin/less'
    assert get_bin_path('grep') == '/bin/grep'
    assert get_bin_path('egrep') == '/bin/egrep'
    assert get_bin_path('fgrep') == '/bin/fgrep'
    assert get_bin_path('[') == '/bin/['

# Generated at 2022-06-12 23:31:42.710561
# Unit test for function get_bin_path
def test_get_bin_path():
    # Return full path for executable
    assert os.path.join(os.environ['HOME'], 'bin', 'ansible') == get_bin_path('ansible', opt_dirs=[os.environ['HOME']])

    # Raise exception with invalid executable
    try:
        get_bin_path('invalid')
    except Exception as e:
        assert isinstance(e, ValueError)
        assert 'Failed to find required executable' in str(e)
    else:
        assert False, "Did not raise exception"

# Generated at 2022-06-12 23:31:51.184106
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil
    import os
    import os.path
    import stat

    def create_executable(path):
        open(path, "wb").close()
        os.chmod(path, 0o700)

    # Test that function raises ValueError if executable not found
    try:
        get_bin_path('invalid-executable')
    except ValueError:
        pass
    else:
        raise AssertionError('test did not fail as expected')

    # Test that function returns executable path if found in path
    tmpdir = tempfile.mkdtemp()
    try:
        path = get_bin_path('ls', opt_dirs=[tmpdir])
        bin_path = os.path.join(tmpdir, 'ls')
        assert path == bin_path
    finally:
        shutil

# Generated at 2022-06-12 23:31:56.527603
# Unit test for function get_bin_path
def test_get_bin_path():
    # Valid executable
    try:
        path = get_bin_path("ip")
        assert path is not None
        assert os.path.exists(path)
    except ValueError:
        assert False

    # Invalid executable
    try:
        path = get_bin_path("idontexist")
        assert False
    except ValueError:
        pass

# Generated at 2022-06-12 23:32:04.171607
# Unit test for function get_bin_path

# Generated at 2022-06-12 23:32:14.712163
# Unit test for function get_bin_path
def test_get_bin_path():
    import sys
    if sys.version_info[0] < 2 or sys.version_info[1] < 6:
        import unittest2 as unittest
    else:
        import unittest
    import shutil
    import os
    import tempfile
    import subprocess

    class TestSequenceFunctions(unittest.TestCase):

        def setUp(self):
            self.dir = tempfile.mkdtemp()
            self.paths = [os.path.join(self.dir, 'path1'), os.path.join(self.dir, 'path2')]
            for path in self.paths:
                os.makedirs(path)
            self.executables = ['test1', 'test2', 'test3']

# Generated at 2022-06-12 23:32:20.659590
# Unit test for function get_bin_path
def test_get_bin_path():
    paths = ['/bin', '/usr/bin', '/usr/local/bin']
    try:
        bin_path = get_bin_path('ls', paths)
    except ValueError:
        assert False, 'Failed to find executable "ls" in search paths'
    assert bin_path == '/bin/ls', 'Failed to return correct pathname'

# Generated at 2022-06-12 23:32:28.388601
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('cat') == '/bin/cat'
    assert get_bin_path('cat', opt_dirs=['/sbin']) == '/bin/cat'
    assert get_bin_path('cat', opt_dirs=['/sbin', '/usr/sbin']) == '/usr/sbin/cat'
    assert get_bin_path('cat', opt_dirs=['/usr/sbin', '/usr/local/sbin']) == '/usr/sbin/cat'
    assert get_bin_path('cat', opt_dirs=['/usr/sbin/', '/usr/local/sbin']) == '/usr/sbin/cat'

# Generated at 2022-06-12 23:32:41.010975
# Unit test for function get_bin_path
def test_get_bin_path():
    def run_test(required, opt_dirs, arg, expected):
        try:
            result = get_bin_path(arg, opt_dirs, required)
            assert result == expected
        except ValueError as e:
            assert expected is None, 'Unexpected ValueError: %s' % e

    # Successful results
    run_test(required=None, opt_dirs=None, arg='sh', expected='/bin/sh')
    run_test(required=True, opt_dirs=None, arg='sh', expected='/bin/sh')
    run_test(required=False, opt_dirs=None, arg='sh', expected='/bin/sh')
    run_test(required=None, opt_dirs=[], arg='sh', expected='/bin/sh')

# Generated at 2022-06-12 23:32:53.001628
# Unit test for function get_bin_path
def test_get_bin_path():

    #
    # Locating the 'python' executable using the system PATH
    #
    python_bin = get_bin_path('python')
    assert is_executable(python_bin)

    #
    # Locating the 'python' executable using optional arguments
    #
    python_bin = get_bin_path('python', ['/usr/bin'])
    assert is_executable(python_bin)

    try:
        get_bin_path('non-existent-executable', required=True)
        assert False, "get_bin_path() failed to raise a ValueError when it should have"
    except ValueError:
        pass

    #
    # Locating the 'python' executable in the /sbin directories
    #

# Generated at 2022-06-12 23:33:01.889911
# Unit test for function get_bin_path
def test_get_bin_path():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    os.environ["PATH"] = "%s:%s" % (current_dir, os.environ["PATH"])
    assert get_bin_path('file_exists.py') == "%s/file_exists.py" % current_dir
    assert get_bin_path('file_exists.py', ['/']) == "%s/file_exists.py" % current_dir
    try:
        get_bin_path('file_does_not_exist.py')
        assert False # FILE NOT FOUND ERROR NOT RAISED
    except ValueError:
        pass

# Generated at 2022-06-12 23:33:12.020664
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test real paths
    paths = ['/bin', '/usr/bin', '/usr/local/bin']
    for p in paths:
        assert get_bin_path('sh', p) == '/bin/sh'
    # Test non existing directory
    try:
        get_bin_path('sh', '/wrongdir')
    except ValueError:
        pass
    else:
        assert False
    # Test invalid path
    try:
        get_bin_path('/not/a/path')
    except ValueError:
        pass
    else:
        assert False
    # Test optional argument
    assert get_bin_path('sh', ['/bin']) == '/bin/sh'
    assert get_bin_path('sh', opt_dirs=['/bin']) == '/bin/sh'

# Generated at 2022-06-12 23:33:15.505477
# Unit test for function get_bin_path
def test_get_bin_path():
    import random
    import string
    random_string = ''.join(random.choice(string.lowercase) for x in range(12))
    bin_path = get_bin_path(random_string + '-not-there')
    print(bin_path)

# Generated at 2022-06-12 23:33:26.483307
# Unit test for function get_bin_path
def test_get_bin_path():
    import unittest
    import tempfile
    import os
    import shutil

    class TestGetBinPath(unittest.TestCase):

        def setUp(self):
            self.tempdir = tempfile.mkdtemp()
            self.tempfile = os.path.join(self.tempdir, 'foo')
            with open(self.tempfile, 'w') as f:
                f.write(u'#!/bin/sh\n')
            os.chmod(self.tempfile, 0o755)

        def tearDown(self):
            shutil.rmtree(self.tempdir)

        def test_finds_executable_in_path(self):
            # Create a fake executable in the PATH.
            new_path = self.tempdir + ':' + os.environ['PATH']
           

# Generated at 2022-06-12 23:33:34.118444
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('ls') == '/bin/ls'
    assert get_bin_path('/bin/ls') == '/bin/ls'
    assert get_bin_path('/nonexistent/bin/ls') == '/nonexistent/bin/ls'
    assert get_bin_path('/bin/ls', ['/nonexistent']) == '/bin/ls'
    assert get_bin_path('/bin/ls', ['/nonexistent', '/nonexistent2']) == '/bin/ls'
    try:
        get_bin_path('nonexistent')
        assert False, 'exception was not thrown'
    except ValueError as e:
        assert 'Failed to find required executable' in str(e)

# Generated at 2022-06-12 23:33:45.416297
# Unit test for function get_bin_path
def test_get_bin_path():
    import pytest
    from ansible.module_utils.common.file import atomic_replace # noqa (fixture)

    test_data = [
        ('cat', None, None),
    ]
    pytestmark = pytest.mark.parametrize('arg, opt_dirs, required', test_data)

    def test_get_bin_path_check(arg, opt_dirs, required):
        bin_path = get_bin_path(arg, opt_dirs, required)
        assert os.path.isfile(bin_path)

    def test_get_bin_path_notfound_raises(arg, opt_dirs, required):
        with pytest.raises(ValueError):
            get_bin_path('nosuchfile')

# Generated at 2022-06-12 23:33:55.800362
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    tmp_dir = tempfile.gettempdir()
    scripts = {
        'arg': '#!/bin/bash\necho arg',
        'usr1': '#!/bin/bash\necho usr1',
        'usr2': '#!/bin/bash\necho usr2',
    }

# Generated at 2022-06-12 23:34:06.656220
# Unit test for function get_bin_path
def test_get_bin_path():
    # Make sure it finds ls in PATH
    bin_path = get_bin_path('ls', opt_dirs=None, required=True)
    assert bin_path.endswith('ls')

    # Make sure it raises when not found
    try:
        bin_path = get_bin_path('ls_8012u3rq0d', opt_dirs=None, required=True)
        raise AssertionError('Should raise exception')
    except ValueError as e:
        pass

    # Try with opt_dirs
    # Try with empty opt_dirs
    bin_path = get_bin_path('ls', opt_dirs=[], required=True)
    assert bin_path.endswith('ls')

    # Try with invalid opt_dirs

# Generated at 2022-06-12 23:34:17.287314
# Unit test for function get_bin_path
def test_get_bin_path():
    def mock_is_executable(path):
        return True

    def mock_isdir(path):
        return False

    def mock_exists(path):
        return True

    def mock_path_sep_join(paths):
        return ':'.join(paths)

    def mock_environ_get(key, default=None):
        return '/usr/bin:/bin'

    paths = {
        '/sbin': True,
        '/usr/sbin': True,
        '/usr/local/sbin': True,
        '/var/tmp': False,
        '/': False,
        '/etc': False,
        '/etc/': False,
        '/foo/bar': False,
        '/a/b/c/d/e/f/g/h': False,
    }

    mock_os_

# Generated at 2022-06-12 23:34:22.421091
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    generates a bin path.
    '''
    # just check if these work, we will test their value in their own modules
    get_bin_path('ansible')
    get_bin_path('ansible', required=True)
    get_bin_path('ansible', required=False)

# Generated at 2022-06-12 23:34:30.974749
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Unit test for function get_bin_path
    '''
    import errno
    import pytest

    # test with optional dirs
    with pytest.raises(ValueError) as excinfo:
        get_bin_path('/bin/foo', opt_dirs=['/usr/bin', '/usr/local/bin', '/bin'], required=False)
    assert 'Failed to find required executable' in str(excinfo.value)
    assert '/bin/foo' in str(excinfo.value)

    # test with path
    with pytest.raises(ValueError) as excinfo:
        get_bin_path('foo', opt_dirs=['/usr/bin', '/usr/local/bin', '/bin'], required=False)

# Generated at 2022-06-12 23:34:40.745626
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path("python2", ["/usr/local/bin", "/usr/bin"]) == "/usr/bin/python2"
    assert get_bin_path("python", ["/usr/local/bin", "/usr/bin"]) == "/usr/local/bin/python"
    try:
        get_bin_path("doesnotexists", ["/usr/local/bin", "/usr/bin"])
        assert False, "Should crash because the python executable is missing"
    except:
        pass
    assert get_bin_path("sh", ["/dev"]) == "/bin/sh"
    assert get_bin_path("python2", opt_dirs=["/usr/bin"]) == "/usr/bin/python2"

# Generated at 2022-06-12 23:34:41.836553
# Unit test for function get_bin_path
def test_get_bin_path():
    assert '/usr/bin/sh' == get_bin_path('sh')

# Generated at 2022-06-12 23:34:43.561861
# Unit test for function get_bin_path
def test_get_bin_path():
    path = get_bin_path('grep')
    assert path == '/bin/grep'

# Generated at 2022-06-12 23:34:53.572091
# Unit test for function get_bin_path
def test_get_bin_path():
    import shutil
    import tempfile
    import sys

    # Create a temporary directory
    tmpdir = tempfile.mkdtemp(prefix='tmp_get_bin_path_')
    # This is the list of directories should be searched
    paths = [os.path.normpath(os.path.join(tmpdir, x)) for x in ['a', 'b/c']]

    # Create a file, should be found
    open(os.path.join(tmpdir, 'foo'), 'a').close()
    assert get_bin_path('foo', paths) == os.path.normpath(os.path.join(tmpdir, 'foo'))

    # file should not be found, exception should be raised
    shutil.rmtree(os.path.join(tmpdir, 'a'))

# Generated at 2022-06-12 23:34:54.620782
# Unit test for function get_bin_path
def test_get_bin_path():
    bin_path = get_bin_path('foo')
    assert bin_path is None

# Generated at 2022-06-12 23:35:00.326714
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Test function
    '''

    def get_bin_ret(arg):
        '''
        Temp
        '''
        return get_bin_path(arg)

    # No args -> ValueError
    try:
        get_bin_ret()
        assert False
    except ValueError:
        assert True

   # valid directory
    assert os.path.exists(get_bin_ret('pwd'))
    try:
        get_bin_ret('asdf')
        assert False
    except ValueError:
        assert True

# Generated at 2022-06-12 23:35:09.135540
# Unit test for function get_bin_path
def test_get_bin_path():
    def test(arg, expected):
        try:
            result = get_bin_path(arg)
        except ValueError as e:
            result = e.message
        assert result == expected, "get_bin_path('%s') returned %r instead of %r" % (arg, result, expected)

    test('some_executable_that_does_not_exist',
        'Failed to find required executable "some_executable_that_does_not_exist" in paths: %s' % (os.pathsep.join(os.environ.get('PATH', '').split(os.pathsep))))
    test('python', os.path.realpath(os.path.join(os.path.dirname(os.__file__), 'python')))

# Generated at 2022-06-12 23:35:21.544638
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil

    my_bin = '/bin/my_bin'
    my_arg = 'my_arg'
    expect_path = '/bin/my_arg'
    opt_dirs = ['/bin']
    # Normal case
    assert get_bin_path(my_arg, opt_dirs) == expect_path
    # Set different PATH
    saved_PATH = os.environ['PATH']
    os.environ['PATH'] = tempfile.mkdtemp(prefix='test_get_bin_path')

# Generated at 2022-06-12 23:35:29.827266
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path("sh") == "/bin/sh"
    # Bin file exists but is not a executable, so it should fail
    try:
        get_bin_path("/etc/hosts")
        assert False
    except ValueError:
        pass
    # Bin file doesn't exists, so it should fail
    try:
        get_bin_path("/bin/no_such_file")
        assert False
    except ValueError:
        pass

# Generated at 2022-06-12 23:35:37.193811
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil
    # setup a fake PATH and some files
    test_dir = tempfile.mkdtemp()

    # this file exists but is not executable, so should not be found
    open(os.path.join(test_dir, 'foo'), 'a').close()

    # this one we will make executable in a second
    open(os.path.join(test_dir, 'bar'), 'a').close()

    # set PATH so we can find foo and bar
    orig_path = os.environ.get('PATH')
    os.environ['PATH'] = test_dir

    # make bar executable and make sure foo is not
    os.chmod(os.path.join(test_dir, 'bar'), 0o777)

# Generated at 2022-06-12 23:35:47.367627
# Unit test for function get_bin_path
def test_get_bin_path():
    from ansible.module_utils.six.moves import builtins
    from ansible.module_utils.common.file import is_executable

    def mock_get_bin_path(arg, opt_dirs=None, required=None):
        paths = []
        if opt_dirs is not None:
            paths += opt_dirs
        paths += os.environ.get('PATH', '').split(os.pathsep)
        bin_path = None
        for d in paths:
            if not d:
                continue
            path = os.path.join(d, arg)
            if os.path.exists(path) and not os.path.isdir(path) and is_executable(path):
                bin_path = path
                break

# Generated at 2022-06-12 23:35:51.065403
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path('/usr/bin/find')
    except ValueError:
        return False
    return True

# Generated at 2022-06-12 23:36:00.117006
# Unit test for function get_bin_path
def test_get_bin_path():
    import pytest
    paths = ['/usr/bin', '/bin', '/usr/sbin', '/sbin', '/usr/local/bin', '/usr/local/sbin']

    # Verify that get_bin_path() returns the correct path
    for p in paths:
        path = os.path.join(p, 'bash')
        if os.path.exists(path):
            bash = get_bin_path('bash')
            assert bash == path
            break

    # Verify that get_bin_path() handles an invalid executable name
    with pytest.raises(ValueError):
        get_bin_path('invalid-executable')

# Generated at 2022-06-12 23:36:10.905755
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path("python")
    try:
        get_bin_path("non-existent-executable")
        assert False, "no exception raised"
    except ValueError:
        pass

    assert get_bin_path("python", opt_dirs=("/usr/bin",))
    try:
        get_bin_path("non-existent-executable", opt_dirs=("/usr/bin",))
        assert False, "no exception raised"
    except ValueError:
        pass

    # Check that function respects optional directories
    assert get_bin_path("head", opt_dirs=("/usr/bin",)) == "/usr/bin/head"
    assert get_bin_path("head", opt_dirs=("/bin",)) == "/bin/head"

# Generated at 2022-06-12 23:36:15.405788
# Unit test for function get_bin_path
def test_get_bin_path():
    bin_paths = ['/sbin/iptables', 'iptables', '/bin/iptables', None]
    for bin_path in bin_paths:
        assert(bin_path == get_bin_path(bin_path))

# Generated at 2022-06-12 23:36:19.901119
# Unit test for function get_bin_path
def test_get_bin_path():
    import sys
    import pytest

    try:
        # should raise exception
        get_bin_path('notexists')
    except ValueError:
        assert True
    else:
        assert False

    # python should always exists
    path = get_bin_path(sys.executable)
    assert os.path.exists(path)
    assert os.path.isabs(path)

# Generated at 2022-06-12 23:36:25.107553
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path("hostname") == '/bin/hostname'
    assert get_bin_path("hostname", opt_dirs=['/bin']) == '/bin/hostname'
    try:
        assert get_bin_path("nosuchbinary")
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "nosuchbinary" in paths: /bin:/usr/bin:/usr/sbin:/sbin'
        pass

# Generated at 2022-06-12 23:36:31.956492
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('/bin/ls', None, None) == '/bin/ls'
    assert get_bin_path('ls', None, None) == '/bin/ls'
    assert get_bin_path('ls', ['.'], None) == './ls'
    try:
        get_bin_path('ls_not_there', None, None)
    except ValueError as e:
        assert 'Failed to find required' in str(e)

# Generated at 2022-06-12 23:36:42.576217
# Unit test for function get_bin_path
def test_get_bin_path():
    import sys
    if sys.version_info >= (3, 0):
        from io import StringIO
    else:
        from StringIO import StringIO
    import unittest

    # Python 2
    try:
        reload
    except NameError:
        # Python 3
        from imp import reload

    # Test for python 2.6
    if '/usr/bin' not in os.environ.get('PATH', '').split(os.pathsep):
        os.environ['PATH'] = os.environ['PATH'] + os.pathsep + '/usr/bin'

    import ansible.module_utils.basic
    reload(ansible.module_utils.basic)

    # Test when a binary is found
    output = StringIO()
    old_stdout = sys.stdout
    sys.stdout = output
   

# Generated at 2022-06-12 23:36:52.063241
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('/bin/sh') == '/bin/sh'
    assert get_bin_path('sh') == '/bin/sh'
    assert get_bin_path('no_such_program', required=False) is None
    #
    # Prior to Ansible 2.10, get_bin_path would raise an exception
    # when the specified binary could not be found.  This behavior
    # is deprecated and will be removed in Ansible 2.14.
    #
    # pylint: disable=deprecated-method
    #
    with pytest.raises(ValueError) as excinfo:
        get_bin_path('no_such_program', required=True)
    assert 'no_such_program' in str(excinfo.value)

# Generated at 2022-06-12 23:37:03.590542
# Unit test for function get_bin_path
def test_get_bin_path():
    import shutil

    # Make a temporary directory to store an executable file
    tmp_dir = None

# Generated at 2022-06-12 23:37:06.257652
# Unit test for function get_bin_path
def test_get_bin_path():
    bin_path = get_bin_path('python3')
    assert not '/bin/python3' == bin_path
    assert b'/bin/python3' != bin_path

# Generated at 2022-06-12 23:37:16.905247
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path('/bin/env')
        get_bin_path('env', opt_dirs=['/bin'])
    except ValueError as e:
        assert False, 'Get_bin_path raised an unexpected ValueError: %s' % e
    except Exception as e:
        assert False, 'Get_bin_path raised an unexpected exception: %s' % e

    try:
        get_bin_path('does_not_exist')
        assert False, 'Get_bin_path did not raise an expected Exception'
    except ValueError as e:
        pass
    except Exception as e:
        assert False, 'Get_bin_path raised an unexpected exception: %s' % e

# Generated at 2022-06-12 23:37:20.559768
# Unit test for function get_bin_path
def test_get_bin_path():
    import sys
    sys.path.append('../../')
    from ansible.module_utils.basic import get_bin_path

    try:
        get_bin_path('notfound')
        assert False
    except ValueError:
        assert True
    else:
        assert False

# Generated at 2022-06-12 23:37:26.675428
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test non-existent binary
    try:
        get_bin_path('foo')
        assert False, 'Did not raise ValueError for non-existent executable'
    except ValueError:
        pass

    # Test existing binary
    path = get_bin_path('sh')

    # Test directory
    try:
        get_bin_path('.')
        assert False, 'Did not raise ValueError for directory'
    except ValueError:
        pass

# Make sure test_get_bin_path is run if this file is run as a script
if __name__ == "__main__":
    test_get_bin_path()

# Generated at 2022-06-12 23:37:38.239425
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil
    import sys
