

# Generated at 2022-06-12 23:27:43.875051
# Unit test for function get_bin_path
def test_get_bin_path():
    assert os.path.exists(get_bin_path('python'))
    assert os.path.exists(get_bin_path('python', ['/usr/bin']))
    try:
        get_bin_path('ossssssss')
    except ValueError as e:
        assert 'ossssssss' in str(e)
        pass
    assert os.path.exists(get_bin_path('python', required=False))

# Generated at 2022-06-12 23:27:50.021226
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path("/tmp/doesnotexist")
    except ValueError as ve:
        assert ("Failed to find required executable" in str(ve))
    assert (get_bin_path("/bin/sh") == "/bin/sh")
    assert (get_bin_path("/bin/sh", ['/sbin', '/usr/sbin']) == "/bin/sh")
    assert (get_bin_path("/bin/sh", ['/nosuchdir', '/usr/sbin']) == "/bin/sh")
    assert (get_bin_path("sh") == "/bin/sh")
    assert (get_bin_path("sh", ['/sbin', '/usr/sbin']) == "/bin/sh")

# Generated at 2022-06-12 23:27:53.636259
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('sed') == '/bin/sed'
    assert get_bin_path('echo') == '/bin/echo'
    assert get_bin_path('/usr/bin/echo') == '/usr/bin/echo'
    assert get_bin_path('no_such_binary') == '/bin/sed'

# Generated at 2022-06-12 23:28:00.992735
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Function get_bin_path: given a program name, return full path of executable if found in PATH, otherwise raise ValueError.
    '''
    # Found in PATH
    assert get_bin_path('ls') == '/bin/ls'
    # Not found in PATH
    try:
        get_bin_path('this_command_does_not_exists')
        assert False
    except ValueError:
        pass
    # Found in opt_dirs
    assert get_bin_path('ls', ['/bin']) == '/bin/ls'
    # Found in opt_dirs - first match wins
    assert get_bin_path('ls', ['/bin', '/usr/bin']) == '/bin/ls'
    # Not found in opt_dirs

# Generated at 2022-06-12 23:28:04.906358
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('sh') == '/bin/sh'

# Generated at 2022-06-12 23:28:12.284643
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path(os.path.basename(__file__)) == __file__

    test_dir = os.path.dirname(os.path.abspath(__file__))

    try:
        get_bin_path('i_dont_exist')
        assert False, 'expected error'
    except ValueError:
        pass

    try:
        get_bin_path(os.path.basename(__file__), [test_dir])
    except ValueError:
        assert False, 'unexpected error'

    try:
        get_bin_path(os.path.basename(__file__), ['/no_way_this_path_exists'])
        assert False, 'expected error'
    except ValueError:
        pass

# Generated at 2022-06-12 23:28:21.751906
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Test get_bin_path() function.
    '''
    import sys
    import tempfile
    import shutil
    import os
    import stat

    # Create temporary directory to work in
    here = os.path.abspath(os.path.dirname(__file__))
    tmp_dir = tempfile.mkdtemp(prefix='ansible-test-get_bin_path-')

    # Inputs for tests

# Generated at 2022-06-12 23:28:24.365238
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path("cat") == "/bin/cat"
    assert get_bin_path("bash") == "/bin/bash"
    try:
        get_bin_path("nonexisting_unittest")
        assert False
    except ValueError:
        pass

# Generated at 2022-06-12 23:28:31.169784
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile

    # Test Test Test
    assert get_bin_path('python') == '/usr/bin/python'
    assert get_bin_path('python', ['/some/path']) == '/usr/bin/python'

    # Setup a fake /sbin and add to PATH
    sbin_dir = tempfile.mkdtemp()
    os.environ['PATH'] = sbin_dir + ':' + os.environ['PATH']
    assert get_bin_path('python') == '/usr/bin/python'

    # Add a fake python executable to /sbin and make sure it is found
    python_bin_path = os.path.join(sbin_dir, 'python')
    with open(python_bin_path, 'w') as f:
        f.write('#!fake\n')

# Generated at 2022-06-12 23:28:35.310468
# Unit test for function get_bin_path
def test_get_bin_path():
    # get_bin_path() raises ValueError if executable is not found in the path
    try:
        get_bin_path('nonexisting12345')
    except ValueError as e:
        assert 'Failed to find required executable' in e.args[0]
    else:
        assert False, 'ValueError was not raised'


# Generated at 2022-06-12 23:28:43.532188
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('ls') == '/bin/ls'
    assert get_bin_path('ls', opt_dirs=['/bin']) == '/bin/ls'
    assert get_bin_path('ls', opt_dirs=['/bin', '/usr/bin']) == '/bin/ls'
    assert get_bin_path('ls', opt_dirs=['/usr/bin']) == '/usr/bin/ls'
    assert get_bin_path('fsck', opt_dirs=['/bin', '/usr/bin']) == '/sbin/fsck'  # should find in /sbin

# vim: filetype=python expandtab tabstop=4 softtabstop=4 shiftwidth=4

# Generated at 2022-06-12 23:28:52.425868
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil

    # Find system executable in PATH
    try:
        assert get_bin_path('/usr/bin/env') == '/usr/bin/env'
    except ValueError:
        assert False, 'Failed to find system executable'

    try:
        get_bin_path('/usr/bin/nonexistent')
        assert False, 'Expected ValueError'
    except ValueError:
        assert True

    # find executable using optional dir
    try:
        assert get_bin_path('/usr/bin/env', ['/usr/bin']) == '/usr/bin/env'
    except ValueError:
        assert False, 'Failed to find system executable'

    # find executable using optional dirs
    tmp_dir = tempfile.mkdtemp()

# Generated at 2022-06-12 23:29:03.546728
# Unit test for function get_bin_path
def test_get_bin_path():
    current_path = os.path.dirname(os.path.realpath(__file__))

    assert get_bin_path('/bin/bash') == '/bin/bash'
    assert get_bin_path('bash') == '/bin/bash'

    assert get_bin_path('bash', opt_dirs=[current_path]) == '/bin/bash'
    assert get_bin_path('sh', opt_dirs=[current_path]) == '/bin/sh'

    assert get_bin_path('cat', opt_dirs=[current_path]) == get_bin_path('cat', opt_dirs=['/bin/sh'])

    try:
        get_bin_path('foo')
        assert False, "Expected exception for no such binary"
    except ValueError:
        pass


# Generated at 2022-06-12 23:29:09.297241
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('ls') == '/bin/ls'
    assert get_bin_path('ls', ['/bin']) == '/bin/ls'
    assert get_bin_path('ls', ['/bin', '/sbin']) == '/bin/ls'
    assert get_bin_path('ping6') == '/sbin/ping6'
    try:
        get_bin_path('please_do_not_have_this_binary')
        assert False
    except ValueError:
        pass

# Generated at 2022-06-12 23:29:19.687042
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('true') == '/bin/true'
    assert get_bin_path('ls') == '/bin/ls'
    assert get_bin_path('ls', opt_dirs=['/usr/bin']) == '/usr/bin/ls'
    assert get_bin_path('fake_app') == '/bin/fake_app'
    assert get_bin_path('fake_app', opt_dirs=['/usr/bin']) == '/usr/bin/fake_app'
    assert get_bin_path('fake_app', opt_dirs=['/usr/bin', '/bin']) == '/bin/fake_app'
    assert get_bin_path('fake_app', opt_dirs=['/usr/bin', '/usr/sbin/']) == '/usr/sbin/fake_app'

# Generated at 2022-06-12 23:29:25.784002
# Unit test for function get_bin_path
def test_get_bin_path():
    import sys
    import shutil
    import tempfile
    from ansible.module_utils.common.file import is_executable

    # Temporary dir for testing, ensure to use independent path from other test code.
    temp_dir = tempfile.mkdtemp('-test-ansible-module-utils-basic')
    temp_file = os.path.join(temp_dir, 'test_module_utils_basic')
    temp_file_abs = os.path.abspath(temp_file)

    assert len(sys.argv) == 0

    # Test exception for executable not exist.
    try:
        get_bin_path('invalid-path')
        assert False, 'should have raised exception'
    except ValueError:
        assert sys.exc_info()[0] is ValueError

# Generated at 2022-06-12 23:29:36.625314
# Unit test for function get_bin_path
def test_get_bin_path():
    # if these are the only two entries in PATH, find is expected to be found
    test_path = ['', '/bin']
    test_bin = 'find'
    find_bin_path = get_bin_path(test_bin, test_path)
    assert True, isinstance(find_bin_path, str)
    assert True, os.path.exists(find_bin_path)
    assert True, os.path.isfile(find_bin_path)
    assert True, is_executable(find_bin_path)

    # if these are the only two entries in PATH, the following is expected to raise ValueError
    test_bin = 'this_does_not_exist'
    result = None
    try:
        result = get_bin_path(test_bin, test_path)
    except:
        assert True

# Generated at 2022-06-12 23:29:42.602166
# Unit test for function get_bin_path
def test_get_bin_path():
    from ansible.module_utils import basic
    from ansible_collections.ansible.netcommon.tests.unit.compat import unittest

    class TestGetBinPath(unittest.TestCase):

        def setUp(self):
            self.mock_path = os.path.join(basic.HOST_VAR_FILES, 'ansible_net_netconf_path_mock')

        def test_get_bin_path_found(self):
            '''Test that we find the mock executable'''
            bin_path = get_bin_path('mock_netconf_ssh.sh', opt_dirs=[self.mock_path])
            self.assertEqual(bin_path, os.path.join(self.mock_path, 'mock_netconf_ssh.sh'))



# Generated at 2022-06-12 23:29:44.475496
# Unit test for function get_bin_path
def test_get_bin_path():
    import sys
    if sys.version_info[0] > 2:
        assert get_bin_path('python') == sys.executable

# Generated at 2022-06-12 23:29:49.039987
# Unit test for function get_bin_path
def test_get_bin_path():
    """
    Unit test to validate get_bin_path. It tests if get_bin_path function
    raises ValueError if executable is not found.

    :return: no return
    """
    # For an executable that is not present in PATH
    try:
        get_bin_path("nonexistent_exec")
    except ValueError:
        return True
    assert False, "ValueError for nonexistent executable not raised."

# Generated at 2022-06-12 23:29:55.987095
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('sh') == '/bin/sh'
    assert get_bin_path('/bin/sh') == '/bin/sh'
    assert get_bin_path('cat') == '/bin/cat'

    try:
        get_bin_path('this_program_wont_be_found')
        assert False
    except ValueError as e:
        assert 'this_program_wont_be_found' in str(e)

# Generated at 2022-06-12 23:30:02.884229
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    As we can't easily determine if the 'sh' exists or not in the PATH
    I will use '/bin/ls', which is present in any UNIX system
    '''
    try:
        result = get_bin_path('ls')
        assert result == '/bin/ls'
    except (Exception) as exc:
        assert False, 'Failed to find ls in any of the known paths'

# Generated at 2022-06-12 23:30:11.210961
# Unit test for function get_bin_path
def test_get_bin_path():
    test_system_executable = 'ls'
    # Verify that the function will throw an exception for a bad executable
    bad_test_system_executable = 'bogus'
    try:
        get_bin_path(bad_test_system_executable)
    except ValueError as err:
        # the exception should contain the executable name
        assert bad_test_system_executable in str(err)
    else:
        assert False, "%s not found" % (bad_test_system_executable)
    # Verify that the function returns the full path to a good executable
    assert get_bin_path(test_system_executable) == '/bin/ls'

# Generated at 2022-06-12 23:30:22.578261
# Unit test for function get_bin_path
def test_get_bin_path():
    import mock
    import copy
    import pwd
    import tempfile

    # Create a temporary directory to use when testing
    tmpdir = tempfile.mkdtemp()

    def teardown_module():
        import shutil
        shutil.rmtree(tmpdir)

    # First set the home directory to the temporary directory we created

# Generated at 2022-06-12 23:30:25.827225
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        result = get_bin_path('sh')
        assert(result != None)
    except ValueError as e:
        raise AssertionError("Unexpected ValueError: %s" % e)

# Generated at 2022-06-12 23:30:36.712737
# Unit test for function get_bin_path
def test_get_bin_path():

    import tempfile

    tmpdir = tempfile.mkdtemp()
    fd, my_file = tempfile.mkstemp(dir=tmpdir)
    os.close(fd)


# Generated at 2022-06-12 23:30:46.514442
# Unit test for function get_bin_path
def test_get_bin_path():
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six.moves import shlex_quote
    import os
    import tempfile

    # create a small python script to run
    with tempfile.NamedTemporaryFile(prefix='ansible_test_get_bin_path', suffix='.py', delete=False) as f:
        f.write(b'import sys\nprint(sys.version)\n')
        py_script = f.name

    # create a temp directory and move the script there
    tmp_path = tempfile.mkdtemp()

# Generated at 2022-06-12 23:30:58.576159
# Unit test for function get_bin_path
def test_get_bin_path():

    from ansible.module_utils.six import PY3

    path_saved = os.environ['PATH']


# Generated at 2022-06-12 23:31:05.122508
# Unit test for function get_bin_path
def test_get_bin_path():
    cur_path = os.environ.get('PATH', '')
    try:
        os.environ['PATH'] = '/usr/sbin:/sbin:/usr/local/sbin'
        assert get_bin_path('ping') == '/usr/sbin/ping'
    finally:
        os.environ['PATH'] = cur_path

    with pytest.raises(ValueError):
        get_bin_path('fake_executable')

# Generated at 2022-06-12 23:31:10.391936
# Unit test for function get_bin_path
def test_get_bin_path():
    import sys
    import os
    import shutil
    import tempfile

    # Test get_bin_path for some system executables.
    # Test will fail if any of those executables does not exist.
    # If test fails, it is a good indication that something is really wrong with the system.

# Generated at 2022-06-12 23:31:23.503847
# Unit test for function get_bin_path

# Generated at 2022-06-12 23:31:30.344119
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('ls') == '/bin/ls'
    assert get_bin_path('ls', ['/bin'], True) == '/bin/ls'
    try:
        get_bin_path('not_here')
    except ValueError:
        pass
    else:
        assert False
    try:
        get_bin_path('/bin/ls')
    except ValueError:
        pass
    else:
        assert False

# Generated at 2022-06-12 23:31:35.137409
# Unit test for function get_bin_path
def test_get_bin_path():
    bin_path = get_bin_path("touch")
    assert os.path.basename(bin_path) == "touch"

    # path to executable that does not exist
    try:
        get_bin_path("/usr/bin/does-not-exist.bin")
    except ValueError as e:
        assert "does-not-exist" in str(e)
    else:
        assert False, "should have gotten 'ValueError' exception"

# Generated at 2022-06-12 23:31:46.096962
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil

    path_dirs = []
    for path in os.environ.get('PATH', '').split(os.path.pathsep):
        if os.path.exists(path):
            path_dirs.append(path)

    # test if we find existing executables
    if os.path.exists('/bin/ls'):
        if os.path.exists('/bin/bash'):
            assert get_bin_path('ls') == '/bin/ls'
            assert get_bin_path('bash') == '/bin/bash'
        else:
            assert get_bin_path('ls') == '/bin/ls'
            assert get_bin_path('bash', opt_dirs=path_dirs)

# Generated at 2022-06-12 23:31:56.436589
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test executable that is not in the user's PATH
    # Raises exception since required is specified (not None)
    # Prior to 2.10, it raises an exception when executable is not found and required is True.
    # In 2.10 and later, an Exception is always raised. The "required" parameter will be removed in 2.14.
    test_bin = 'ansible-test-bin'
    paths = ['/bin', '/sbin']
    try:
        get_bin_path(test_bin, opt_dirs=paths, required=True)
    except Exception as e:
        assert 'Failed to find required executable' in str(e)

    # Test executable that is in the user's PATH.
    # Does not raise exception since executable is found.
    assert get_bin_path('ansible')

# Generated at 2022-06-12 23:31:58.106025
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('sh', opt_dirs='/bin') == '/bin/sh'

# Generated at 2022-06-12 23:32:05.128786
# Unit test for function get_bin_path
def test_get_bin_path():
    paths = []
    # create temp dirs for the test
    tmpdir = os.path.realpath(os.path.join('/tmp', 'get_bin_path-' + os.urandom(16).encode('hex')))
    bin1 = os.path.join(tmpdir, 'bin1')
    bin2 = os.path.join(tmpdir, 'bin2')
    os.makedirs(bin1)
    os.makedirs(bin2)
    # create empty files in temp dirs
    exec1 = os.path.join(bin1, 'exec1')
    exec2 = os.path.join(bin2, 'exec2')
    open(exec1, 'a').close()
    open(exec2, 'a').close()
    # change permissions on files

# Generated at 2022-06-12 23:32:15.142417
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    tmp = tempfile.mkdtemp()

    dirs = [os.path.join(tmp, 'j'), os.path.join(tmp, 'k')]

    fn = os.path.join(tmp, 'test')
    open(fn, 'w').close()
    os.chmod(fn, 0o500)
    assert get_bin_path(fn, opt_dirs=[]) == fn
    assert get_bin_path(fn, opt_dirs=dirs) == fn
    os.chmod(fn, 0o000)
    try:
        get_bin_path(fn, opt_dirs=[])
    except ValueError:
        assert os.path.exists(tmp)
        os.chmod(fn, 0o500)
        assert os.path.exists(fn)

# Generated at 2022-06-12 23:32:23.636508
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path('cat', required=True)
    except ValueError:
        raise AssertionError('Unable to find required executable "cat" in path')

    try:
        get_bin_path('/bin/cat', required=True)
        raise AssertionError('Run on absolute path, expected ValueError')
    except ValueError:
        pass

    try:
        get_bin_path('false', required=True)
        raise AssertionError('Run on a not executable file, expected ValueError')
    except ValueError:
        pass

# Generated at 2022-06-12 23:32:35.657397
# Unit test for function get_bin_path
def test_get_bin_path():
    import platform
    import shutil
    import tempfile
    import unittest

    class TestGetBinPath(unittest.TestCase):

        def setUp(self):
            self.base_dir = tempfile.tempdir
            self.tmp_dir = tempfile.mkdtemp()
            self.cwd = os.getcwd()

        def tearDown(self):
            os.chdir(self.cwd)
            shutil.rmtree(self.tmp_dir)

        def is_executable_helper(self, path):
            return os.access(path, os.X_OK)

        def test_find_system_executable_in_path(self):
            os.chdir(self.tmp_dir)
            # Create a fake executable at a temporary location

# Generated at 2022-06-12 23:32:53.018540
# Unit test for function get_bin_path
def test_get_bin_path():

    # Test 1:
    # Test on any non existent binary in path
    try:
        get_bin_path("qwerty")
    except ValueError:
        pass
    except:
        assert 0, "Unexpected error while testing get_bin_path():"

    # Test 2:
    # Test on any binary that exists in path
    get_bin_path("python")

# Generated at 2022-06-12 23:33:01.921742
# Unit test for function get_bin_path
def test_get_bin_path():
    # Find the path to 'ls'
    test_arg = 'ls'

# Generated at 2022-06-12 23:33:12.019813
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile

    def touch(path):
        with open(path, 'a'):
            os.utime(path, None)

    tmpdir = tempfile.mkdtemp()
    try:
        touch(os.path.join(tmpdir, 'bin'))
        os.symlink('bin', os.path.join(tmpdir, 'link'))
        for d in tmpdir, os.path.join(tmpdir, 'link'):
            assert get_bin_path('bin', opt_dirs=[d]) == os.path.join(d, 'bin')

        assert get_bin_path('link', opt_dirs=[tmpdir]) == os.path.join(tmpdir, 'link')
    finally:
        os.rmdir(tmpdir)

# Generated at 2022-06-12 23:33:22.770638
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test when executable is in PATH
    path = get_bin_path('python')
    assert isinstance(path, type(''))
    assert path.endswith('python')

    # Test when directory of executable is in PATH
    assert get_bin_path('python', opt_dirs=['/usr/bin']) == '/usr/bin/python'

    # Test when executable is in PATH and opt_dirs is not a list
    assert get_bin_path('python', opt_dirs='/usr/bin') == '/usr/bin/python'

    # Test when executable not in PATH
    try:
        get_bin_path('not_there')
    except ValueError as e:
        msg = 'Failed to find required executable "not_there" in paths'
        assert msg in str(e)

    # Test when executable

# Generated at 2022-06-12 23:33:31.578132
# Unit test for function get_bin_path
def test_get_bin_path():
    # get_bin_path should return the expected location for the ls program
    assert get_bin_path('ls') == '/bin/ls'

    # get_bin_path should return a path if run from a directory on PATH
    current_directory = os.getcwd()
    paths = os.environ.get('PATH', '').split(os.pathsep)
    paths.append(current_directory)
    os.environ['PATH'] = os.pathsep.join(paths)
    with open('touch', 'a'):
        os.utime('touch', None)
    assert get_bin_path('touch') == current_directory + '/touch'
    os.remove('touch')

    # get_bin_path should return a path if run from a directory not on PATH and opt_dirs is not set
    current_

# Generated at 2022-06-12 23:33:38.142052
# Unit test for function get_bin_path
def test_get_bin_path():
    assert '/bin/echo' == get_bin_path('echo')
    assert '/sbin/dhclient' == get_bin_path('dhclient', opt_dirs=['/sbin'])
    assert '/sbin/dhclient' == get_bin_path('dhclient', opt_dirs=['/bin', '/sbin'])
    try:
        get_bin_path('bogus_executable')
        assert False, 'Expected an error'
    except ValueError:
        pass

# Generated at 2022-06-12 23:33:48.740077
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Test that get_bin_path returns correct path
    '''
    import subprocess
    import platform

    system = platform.system()

    # It's simplest to check the get_bin_path function using the subprocess module's check_output function.
    # check_output uses get_bin_path to locate and execute system executables.
    # The following test simply checks that check_output does not raise an exception when called with a common system executable.
    # If check_output does raise an exception, that indicates get_bin_path does not return a valid path.

# Generated at 2022-06-12 23:33:52.813493
# Unit test for function get_bin_path
def test_get_bin_path():

    assert get_bin_path('cat') == '/bin/cat'
    assert get_bin_path('ip') == '/bin/ip'
    assert get_bin_path('ip', opt_dirs=['/usr/bin']) == '/usr/bin/ip'

# Generated at 2022-06-12 23:34:04.245098
# Unit test for function get_bin_path
def test_get_bin_path():
    for path in ('/bin', '/usr/bin', '/usr/local/bin', '/sbin', '/usr/sbin', '/usr/local/sbin'):
        assert os.path.exists(path)
        assert os.path.isdir(path)
        assert is_executable(path, follow=False), '%s is not executable' % (path)

    import tempfile
    tempdir = tempfile.gettempdir()
    path = get_bin_path(tempfile.gettempprefix(), opt_dirs=[tempdir])
    assert path == os.path.join(tempdir, tempfile.gettempprefix()), '%s != %s' % (path, os.path.join(tempdir, tempfile.gettempprefix()))


# Generated at 2022-06-12 23:34:10.908397
# Unit test for function get_bin_path
def test_get_bin_path():
    path = get_bin_path('touch')
    assert path == '/bin/touch' or path == '/usr/bin/touch'

    # Test opt_dirs
    path = get_bin_path('touch', opt_dirs=['/bin'])
    assert path == '/bin/touch'

    # Test not found
    try:
        get_bin_path('noexecutable')
        assert False
    except ValueError:
        pass

    path = get_bin_path('touch', opt_dirs=[''])
    assert path == '/bin/touch' or path == '/usr/bin/touch'

# Generated at 2022-06-12 23:34:38.242085
# Unit test for function get_bin_path
def test_get_bin_path():
    test_paths = ['/usr/sbin/', '/usr/local/bin/']

    # Make sure we can find a command in the default path
    test_command = 'ls'
    assert get_bin_path(test_command) is not None

    # Make sure we can find a command in provided paths
    test_command = 'touch'
    assert get_bin_path(test_command, test_paths) is not None

    # Make sure we can find a command in provided paths
    test_command = 'should_not_exist'
    try:
        get_bin_path(test_command, test_paths)
    except ValueError:
        assert True
    else:
        assert False

# Generated at 2022-06-12 23:34:47.908950
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil
    import os

    bin_name = 'for_testing_get_bin_path'
    try:
        tmpdir = tempfile.mkdtemp()
        bin_path = os.path.join(tmpdir, bin_name)
        with open(bin_path, 'w') as f:
            f.write("#!/bin/sh\nexit 0")
        os.chmod(bin_path, 0o755)
        bin_path = get_bin_path(bin_name, opt_dirs=[tmpdir])
        assert bin_path
        assert os.path.exists(bin_path)
        assert os.path.isdir(bin_path) is False
    finally:
        shutil.rmtree(tmpdir)

# Generated at 2022-06-12 23:34:51.313966
# Unit test for function get_bin_path
def test_get_bin_path():
    import ansible.module_utils.basic
    try:
        ansible.module_utils.basic.get_bin_path('no-such-file')
        module.fail_json(msg="Should have thrown an exception")
    except ValueError:
        pass

# Generated at 2022-06-12 23:34:56.448642
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('sh') == '/bin/sh'
    assert get_bin_path('foo') == '/bin/foo'
    assert get_bin_path('foo', opt_dirs=["/bin"]) == '/bin/foo'
    assert get_bin_path('foo', opt_dirs=["/usr/bin"]) == '/usr/bin/foo'
    assert get_bin_path('foo', opt_dirs=["/bin", "/usr/bin"]) == '/bin/foo'

# Generated at 2022-06-12 23:35:04.160006
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('ls')
    assert get_bin_path('ls', ['.'])
    try:
        get_bin_path('doesntexist')
        assert False, "Exception not thrown"
    except ValueError:
        # Exception expected, test passed
        pass
    try:
        get_bin_path('doesntexist', [])
        assert False, "Exception not thrown"
    except ValueError:
        # Exception expected, test passed
        pass
    try:
        get_bin_path('doesntexist', ['/bin'])
        assert False, "Exception not thrown"
    except ValueError:
        # Exception expected, test passed
        pass

# Generated at 2022-06-12 23:35:14.767818
# Unit test for function get_bin_path
def test_get_bin_path():
    #print('Test 1: %s' % get_bin_path('ls'))
    assert get_bin_path('ls') == '/bin/ls'
    #print('Test 2: %s' % get_bin_path('invalid-no-such-command'))
    try:
        get_bin_path('invalid-no-such-command')
    except ValueError:
        pass
    #print('Test 3: %s' % get_bin_path('ls', ['/bin','/usr/bin','/usr/local/bin']))
    assert get_bin_path('ls', ['/bin','/usr/bin','/usr/local/bin']) == '/bin/ls'
    #print('Test 4: %s' % get_bin_path('invalid-no-such-command', ['/bin','/usr

# Generated at 2022-06-12 23:35:17.374061
# Unit test for function get_bin_path
def test_get_bin_path():
    assert os.path.realpath(get_bin_path('python')) == os.path.realpath(os.path.join(os.sep, 'usr', 'bin', 'python'))

    raises_valueerror = False
    try:
        get_bin_path('missing-executable')
    except ValueError:
        raises_valueerror = True
    assert raises_valueerror == True

# Generated at 2022-06-12 23:35:26.197756
# Unit test for function get_bin_path
def test_get_bin_path():
    # if get_bin_path raises ValueError it is the only error we expect
    # ValueError should be thrown if file is not found or is not executable
    for path in ['/path/to/file', '/non/existing/file', '/file/not/executable']:
        try:
            get_bin_path(path)
            assert False, 'ValueError not thrown for path: %s' % path
        except ValueError:
            pass

    # test passing a required parameter
    for path in ['/path/to/file', '/non/existing/file', '/file/not/executable']:
        try:
            get_bin_path(path, required=True)
            assert False, 'ValueError not thrown for path: %s' % path
        except ValueError:
            pass

# Generated at 2022-06-12 23:35:28.885738
# Unit test for function get_bin_path
def test_get_bin_path():
    bin_path = get_bin_path('bash')
    assert bin_path != None

# Generated at 2022-06-12 23:35:36.792898
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Validate get_bin_path function
    '''
    opt_dirs = ['/opt']
    assert get_bin_path('cp', opt_dirs) == '/opt/cp'
    assert get_bin_path('/opt/cp', opt_dirs) == '/opt/cp'
    assert get_bin_path('/usr/bin/cp') == '/usr/bin/cp'
    assert get_bin_path('/usr/bin/cp', ['/usr/local/bin']) == '/usr/bin/cp'
    # Now test that it raises an exception
    try:
        get_bin_path('__FOO__')
    except ValueError as e:
        assert 'Failed to find required executable' in str(e)

# Generated at 2022-06-12 23:35:59.543614
# Unit test for function get_bin_path
def test_get_bin_path():
    test_path = '/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin'
    os.environ['PATH'] = test_path
    assert get_bin_path('bash') == '/bin/bash'


# Generated at 2022-06-12 23:36:06.307947
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test call with required only
    try:
        bin_path = get_bin_path('grep')
    except ValueError as e:
        if e.message != 'Failed to find required executable "grep" in paths: /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin':
            raise AssertionError()
    else:
        raise AssertionError()
    # Test valid call
    bin_path = get_bin_path('grep', opt_dirs=None, required=False)
    if not os.path.exists(bin_path):
        raise AssertionError()
    # Test valid call with opt_dirs

# Generated at 2022-06-12 23:36:16.415023
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Function get_bin_path returns the full path to an executable.
    It finds executable along the path even if its name is a sub-string of
    other executables in the path (example: it will find /usr/bin/cut even
    if /usr/bin/cutadapt is also in the path).

    It raises an OSError if a directory is specified.
    It raises a ValueError if the executable is not found.
    '''
    from ansible.module_utils.common.process import get_bin_path

    # Expected success
    assert get_bin_path('cut') == '/usr/bin/cut'
    assert get_bin_path('openssl') == '/usr/bin/openssl'

    import pytest
    with pytest.raises(OSError):
        get_bin_path('')

# Generated at 2022-06-12 23:36:18.093727
# Unit test for function get_bin_path
def test_get_bin_path():
    if get_bin_path("ruby") is not None:
        assert True
    else:
        assert False

# Generated at 2022-06-12 23:36:26.526451
# Unit test for function get_bin_path
def test_get_bin_path():

    import tempfile


# Generated at 2022-06-12 23:36:29.597025
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path('/bin/echo')
    except ValueError:
        pass
    else:
        print('Expected exception for missing path')

    get_bin_path('/bin/echo', required=True)

# Generated at 2022-06-12 23:36:34.488367
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path('missing_binary')
    except ValueError:
        pass
    else:
        assert False, "Didn't catch expected missing binary exception"

    try:
        get_bin_path('ls', opt_dirs=['/bin'])
    except ValueError:
        assert False, "Didn't find ls"
    else:
        pass

if __name__ == '__main__':
    test_get_bin_path()

# Generated at 2022-06-12 23:36:37.028696
# Unit test for function get_bin_path
def test_get_bin_path():
    arg = 'id'
    bin_path = get_bin_path(arg)
    print(bin_path)


if __name__ == '__main__':
    test_get_bin_path()

# Generated at 2022-06-12 23:36:41.792979
# Unit test for function get_bin_path
def test_get_bin_path():

    # Test with empty optional directories
    new_path = get_bin_path('ls', ['/bin', '/usr/bin'])
    assert new_path == '/bin/ls'

    # Test with optional directories
    new_path = get_bin_path('ls')
    assert new_path == '/bin/ls'

# Generated at 2022-06-12 23:36:51.160322
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('sh') == '/bin/sh'
    assert get_bin_path('/bin/sh') == '/bin/sh'
    assert get_bin_path('doesnotexist') == '/bin/doesnotexist'
    assert get_bin_path('/bin/doesnotexist') == '/bin/doesnotexist'
    assert get_bin_path('/bin/doesnotexist', opt_dirs=['/root']) == '/bin/doesnotexist'
    try:
        get_bin_path('doesnotexist', required=True)
        assert False
    except ValueError as e:
        print(e)
    assert get_bin_path('sh', opt_dirs=['/root'], required=True) == '/bin/sh'

# Generated at 2022-06-12 23:37:18.875844
# Unit test for function get_bin_path
def test_get_bin_path():
    test_cmds = ['hello_world', '/bin/bash']
    assert get_bin_path(test_cmds[0]) == '/usr/bin/hello_world'
    assert get_bin_path(test_cmds[1]) == '/bin/bash'
    assert get_bin_path(test_cmds[0], opt_dirs=['/bin']) == '/usr/bin/hello_world'
    assert get_bin_path(test_cmds[1], opt_dirs=['/bin']) == '/bin/bash'
    assert get_bin_path(test_cmds[0], opt_dirs=['/data/bin']) == '/usr/bin/hello_world'

# Generated at 2022-06-12 23:37:27.122995
# Unit test for function get_bin_path
def test_get_bin_path():
    test_path = 'This is not a directory'
    def fake_exists(path):
        return True if path == test_path else False

    def fake_is_executable(path):
        return True if path == test_path else False

    fake_os = {
        '__file__': os.__file__,
        'path': os.path,
        'environ': {'PATH': '/fake/bin:/fake/sbin'},
        'sep': os.sep,
        'EX_CONFIG': os.EX_CONFIG
    }

    fake_path = {
        '__file__': os.path.__file__,
        'exists': fake_exists,
        'isdir': os.path.isdir,
        'join': os.path.join
    }

    fake_

# Generated at 2022-06-12 23:37:38.560990
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Runs a series of basic test cases for the get_bin_path function
    '''

    from units.compat.mock import patch

    # Test get_bin_path with a standard executable in PATH
    with patch('os.path.exists') as exists_mock, patch('os.path.isdir') as isdir_mock, patch('os.environ.get') as get_mock, \
            patch('os.environ.__getitem__') as getitem_mock:

        getitem_mock.return_value = '/usr/local/bin:/usr/bin:/bin'

        exists_mock.return_value = True
        isdir_mock.return_value = False

        result = get_bin_path('ls')
        assert result == ('/bin/ls')

        # Check