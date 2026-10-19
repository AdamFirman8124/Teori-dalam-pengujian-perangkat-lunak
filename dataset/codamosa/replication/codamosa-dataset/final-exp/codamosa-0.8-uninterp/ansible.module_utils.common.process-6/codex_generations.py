

# Generated at 2022-06-12 23:27:45.492973
# Unit test for function get_bin_path
def test_get_bin_path():
    def reset_environ():
        # reset PATH and sbin_paths to original state
        os.environ['PATH'] = old_path
        for p in old_sbin_paths:
            if p not in paths and os.path.exists(p):
                paths.append(p)
        for p in paths:
            if p not in sbin_paths and os.path.exists(p):
                sbin_paths.remove(p)

    def populate_paths():
        # set up some fake values to use for testing
        paths = []
        paths.append('/foo')
        paths.append('/bar')
        paths.append('/baz')
        paths.append('/sbin')
        paths.append('/usr/sbin')

# Generated at 2022-06-12 23:27:50.794851
# Unit test for function get_bin_path
def test_get_bin_path():
    # check for required executable in PATH
    get_bin_path('bash', [])

    # check for required executable in custom paths
    get_bin_path('bash', ['/bin', '/usr/bin'])

    try:
        # check for non-existing executable in custom paths
        get_bin_path('does_not_exist', ['/bin', '/usr/bin'])
    except ValueError:
        pass
    else:
        assert(False)

# Generated at 2022-06-12 23:27:58.519588
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil

    # Test caching of binary path
    assert get_bin_path('sh') == get_bin_path('sh')

    try:
        # Test with a directory
        path = os.path.join(tempfile.mkdtemp(), 'sh')
        get_bin_path(path)
    except ValueError:
        pass
    else:
        assert False, 'Expected ValueError when running get_bin_path with a directory'

    # Test with a file and directory
    path = os.path.join(tempfile.mkdtemp(), 'sh')
    with open(path, 'w+') as f:
        f.write('test file')
    bin_path = '/bin/sh'

    del os.environ['PATH']

# Generated at 2022-06-12 23:28:01.713261
# Unit test for function get_bin_path
def test_get_bin_path():
    for executable, required in [('cat', True), ('not_exists', False)]:
        try:
            get_bin_path(executable, required=required, opt_dirs=[])
        except ValueError:
            if required:
                pass
            else:
                raise
        else:
            if required:
                raise

# Generated at 2022-06-12 23:28:11.857551
# Unit test for function get_bin_path
def test_get_bin_path():
    # Directories to test.
    real_dirs = ['/usr/bin', '/usr/sbin', '/bin', '/sbin', '/usr/local/bin', '/usr/local/sbin', '/foo']
    # Directories that can not be found.
    fake_dirs = ['/bin1', '/sbin1', '/usr/bin1', '/usr/sbin1', '/usr/local/bin1', '/usr/local/sbin1']
    # Search for a real executable 'ls' in real_dirs directories.
    for d in real_dirs:
        if d is not None and os.path.exists(d):
            test_dirs = [d] + fake_dirs
            bin_path = get_bin_path('ls', opt_dirs=test_dirs)
            assert bin_path

# Generated at 2022-06-12 23:28:21.339783
# Unit test for function get_bin_path
def test_get_bin_path():
    class MyError(Exception):
        pass

    old_environ_path = os.environ.get('PATH')
    os.environ['PATH'] = '/bin:/usr/bin:/usr/local/bin'

# Generated at 2022-06-12 23:28:25.484679
# Unit test for function get_bin_path
def test_get_bin_path():
    test_path = '/tmp/foo'
    try:
        # test non-existant file
        get_bin_path('foobar')
    except ValueError:
        pass
    else:
        assert False

    # test existing file
    with open(test_path, 'w') as f:
        f.write('#!/bin/sh\n')

# Generated at 2022-06-12 23:28:32.111306
# Unit test for function get_bin_path
def test_get_bin_path():
    import ansible.module_utils.common.file as file_utils

    assert file_utils.get_bin_path('ls') == '/bin/ls'
    assert file_utils.get_bin_path('ls', opt_dirs=['/tmp']) == '/bin/ls'
    assert file_utils.get_bin_path('wc', opt_dirs=['/tmp']) == '/usr/bin/wc'
    assert file_utils.get_bin_path('wc', opt_dirs=['/bin', '/usr/local/bin']) == '/usr/bin/wc'
    assert file_utils.get_bin_path('ls', opt_dirs=['/sbin', '/usr/sbin', '/usr/local/sbin']) == '/usr/bin/ls'

# Generated at 2022-06-12 23:28:37.721807
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('true') == '/bin/true'
    assert get_bin_path('ip') == '/sbin/ip'
    assert get_bin_path('ls') == '/bin/ls'
    assert get_bin_path('false') == '/bin/false'
    try:
        get_bin_path('invalid')
    except ValueError:
        pass
    else:
        assert False, 'Did not raise error with invalid input'

# Generated at 2022-06-12 23:28:39.084640
# Unit test for function get_bin_path
def test_get_bin_path():
    bin_path = get_bin_path("which")
    assert is_executable(bin_path)

# Generated at 2022-06-12 23:28:50.754610
# Unit test for function get_bin_path
def test_get_bin_path():
    """
    Unit test for function get_bin_path
    """
    import tempfile
    import shutil
    import sys

    # Set up a temp directory
    test_path = tempfile.mkdtemp()
    test_dir = os.path.join(test_path, "bin")
    os.mkdir(test_dir)
    # Add a test executable
    fh, test_exec = tempfile.mkstemp(dir=test_dir)
    os.close(fh)
    os.chmod(test_exec, 0o755)
    # Set up a second temp directory
    test2_path = tempfile.mkdtemp()
    test2_dir = os.path.join(test2_path, "bin")
    os.mkdir(test2_dir)
    # Add another test executable
   

# Generated at 2022-06-12 23:29:02.156004
# Unit test for function get_bin_path
def test_get_bin_path():
    # get_bin_path should return None
    assert get_bin_path('/bin/false') == '/bin/false'
    assert get_bin_path('false') == '/usr/bin/false'
    assert get_bin_path('false', opt_dirs=['/usr/local/bin']) == '/usr/local/bin/false'

    try:
        assert get_bin_path('fals') == None
        assert False, 'get_bin_path did not raise ValueError'
    except ValueError:
        pass

    try:
        assert get_bin_path('false', opt_dirs=['/usr/local/bin'], required=False) == None
        assert False, 'get_bin_path did not raise ValueError'
    except ValueError:
        pass

# Generated at 2022-06-12 23:29:11.055134
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('sh') == '/bin/sh'
    assert get_bin_path('/bin/sh') == '/bin/sh'
    assert get_bin_path('cat') == '/bin/cat'
    assert get_bin_path('ls', opt_dirs=['/bin']) == '/bin/ls'
    assert get_bin_path('ls', opt_dirs=['/usr/bin']) == '/usr/bin/ls'

# Generated at 2022-06-12 23:29:12.750196
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('vim')

# Generated at 2022-06-12 23:29:21.374133
# Unit test for function get_bin_path
def test_get_bin_path():
    # The test script prepends a bin directory to the PATH in the subprocess.
    # If the test fails, either os.environ['PATH'] has changed or get_bin_path()
    # is broken.
    my_env = os.environ.copy()
    test_script = os.path.join(os.path.dirname(__file__), "test_get_bin_path.sh")
    cmd = [test_script, 'some_nonexistent_binary']
    status, stdout, stderr = module.run_command(cmd, environ_update=my_env)

    if status == 0:
        msg = "get_bin_path() should return an exception, but it returned '%s'" % stdout
        module.fail_json(msg=msg)

# Generated at 2022-06-12 23:29:30.837824
# Unit test for function get_bin_path
def test_get_bin_path():
    if os.path.exists('/usr/bin/python'):
        path = get_bin_path('python')
        assert path and type(path) is str, 'Failed to find python'
    with pytest.raises(ValueError):
        get_bin_path('T0T4LLYS3CUR3F1L3N4M3')
    assert get_bin_path('python', ['/usr/bin']) == '/usr/bin/python', 'Searching in list of extra paths failed'
    if os.path.exists('/usr/bin/python'):
        path = get_bin_path('python', required=False)
        assert path and type(path) is str, 'Failed to find python with required=False'

# Generated at 2022-06-12 23:29:42.202658
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import stat
    import shutil
    import os

    old_path = os.environ['PATH']
    old_cwd = os.getcwd()
    bin_name = 'foo'
    bin_dir = tempfile.mkdtemp()
    os.chdir(bin_dir)
    with open(bin_name, 'w') as f:
        f.write('#!/bin/bash\necho hello world\n')
    os.chmod(bin_name, stat.S_IRWXU)
    os.environ['PATH'] = bin_dir
    try:
        assert 'hello world' in get_bin_path(bin_name)
    finally:
        shutil.rmtree(bin_dir)
        os.chdir(old_cwd)
        os.en

# Generated at 2022-06-12 23:29:48.817539
# Unit test for function get_bin_path
def test_get_bin_path():
    # test with no OPT_DIRS and required=True
    assert get_bin_path("true") == '/bin/true'
    # test with no OPT_DIRS and required=False
    assert get_bin_path("true") == '/bin/true'
    # test with OPT_DIRS and required=True
    assert get_bin_path("true", ['/','/usr/bin']) == '/bin/true'
    # test with OPT_DIRS and required=False
    assert get_bin_path("true", ['/','/usr/bin']) == '/bin/true'


# Generated at 2022-06-12 23:29:54.028950
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('cat') is not None
    try:
        get_bin_path('foobar')
        fail('No exception raised trying to find nonexistant binary')
    except ValueError:
        pass
    assert get_bin_path('cat', required=False) is not None
    assert get_bin_path('cat', opt_dirs=['/bin', '/usr/bin']) is not None

# Generated at 2022-06-12 23:30:00.672813
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil

    ansible_test_dir = tempfile.mkdtemp()
    real_path = shutil.which('env')
    try:
        # test found bin path
        assert real_path == get_bin_path('env')
        # test not found bin path
        try:
            get_bin_path('nosuchfile')
        except ValueError:
            # expect exception
            pass
        else:
            assert False, "Expected exception"

        # test opt_dirs
        env_file = os.path.join(ansible_test_dir, 'env')
        os.symlink(real_path, env_file)
        assert env_file == get_bin_path('env', opt_dirs=[ansible_test_dir])
    finally:
        shutil.r

# Generated at 2022-06-12 23:30:03.275628
# Unit test for function get_bin_path
def test_get_bin_path():
    path = get_bin_path("python2.7")


# Generated at 2022-06-12 23:30:12.805763
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test that get_bin_path returns the correct path for a command found
    # in the PATH
    assert get_bin_path('ansible') == get_bin_path('ansible', [])

    # Test that get_bin_path returns the correct path for a command found
    # in the opt_dirs
    assert get_bin_path('ansible', opt_dirs=[os.path.dirname(get_bin_path('ansible'))]) == get_bin_path('ansible', [])
    assert get_bin_path('ansible', opt_dirs=['/tmp']) != get_bin_path('ansible', [])

    # Test that get_bin_path raises a ValueError when the command is not found
    import pytest
    with pytest.raises(ValueError):
        get_bin_path

# Generated at 2022-06-12 23:30:20.720625
# Unit test for function get_bin_path
def test_get_bin_path():
    bin_path_dirs = ['.']
    bin_path_dirs = [os.path.dirname(__file__)] + bin_path_dirs
    # The following exists because people do not read the doc.
    bin_path_dirs.append('/usr/bin')
    bin_path_dirs.append('/usr/local/bin')
    assert get_bin_path('ansible-test', bin_path_dirs) == os.path.join(os.path.dirname(__file__), 'ansible-test')

# Generated at 2022-06-12 23:30:30.297885
# Unit test for function get_bin_path
def test_get_bin_path():
    # Existing path
    assert get_bin_path('cat')

    # Non-existing path
    try:
        get_bin_path('xxxxx')
        assert False
    except ValueError:
        assert True

    # Relative path
    # FIXME: This test fails on Python 3.  Figure out how to do this in a way
    # that works with both Python 2 and 3.
    # assert get_bin_path('cat', opt_dirs=['.']) == os.path.join(os.getcwd(), 'cat')

    # Existing path in relative directory
    assert get_bin_path('cat', opt_dirs=['/bin']) == '/bin/cat'

    # Non-existing path in relative directory

# Generated at 2022-06-12 23:30:36.558777
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('sh') == '/bin/sh'
    opt_dirs = set(['/opt/bin', '/local/bin'])
    assert get_bin_path('sh', opt_dirs) == '/bin/sh'
    opt_dirs = set(['/opt/bin', '/local/bin', '/bin'])
    assert get_bin_path('sh', opt_dirs) == '/bin/sh'

# Generated at 2022-06-12 23:30:37.584326
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('ls')

# Generated at 2022-06-12 23:30:45.936543
# Unit test for function get_bin_path
def test_get_bin_path():
    from ansible.modules.system import get_bin_path

    import os
    import sys

    # Test for executable in standard PATH
    bin_path = get_bin_path(sys.executable)
    assert bin_path == sys.executable

    # Test for non existent executable
    try:
        get_bin_path('does-not-exist')
        assert False, 'Error should have been raised for an executable that does not exist'
    except ValueError:
        pass

    # Test for executable in optional path
    bin_path = get_bin_path('tar', opt_dirs=[os.path.dirname(bin_path)])
    assert bin_path

# Generated at 2022-06-12 23:30:57.664950
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('python', ['/python/bin']) == '/python/bin/python'
    assert get_bin_path('python', ['/python/bin', '/xyz']) == '/python/bin/python'
    assert get_bin_path('python', ['/xyz', '/python/bin']) == '/python/bin/python'
    assert get_bin_path('python', ['/xyz', '/usr/bin', '/python/bin']) == '/usr/bin/python'
    assert get_bin_path('python', ['/xyz', '/usr/bin']) == '/usr/bin/python'
    assert get_bin_path('python', ['/xyz']) == '/usr/bin/python'
    assert get_bin_path('python', []) == '/usr/bin/python'

# Generated at 2022-06-12 23:31:01.593156
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('sh') == '/bin/sh'
    assert get_bin_path('/bin/sh') == '/bin/sh'
    assert get_bin_path('/usr/bin/env') == '/usr/bin/env'
    assert get_bin_path('/usr/bin/env', opt_dirs=['/usr/bin']) == '/usr/bin/env'

# Generated at 2022-06-12 23:31:04.002250
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test for system executable
    bin_path = get_bin_path('grep')
    if bin_path is None:
        raise ValueError('Unable to find system executable "grep"')


if __name__ == '__main__':
    test_get_bin_path()

# Generated at 2022-06-12 23:31:15.721308
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        assert get_bin_path('/bin/bash', required=False)
    except ValueError:
        assert False, 'get_bin_path("/bin/bash") failed'

    try:
        assert not get_bin_path('/bin/xyz', required=False)
    except ValueError:
        assert False, 'get_bin_path("/bin/xyz") failed'

    try:
        assert get_bin_path('bash', required=False)
    except ValueError:
        assert False, 'get_bin_path("bash") failed'

    try:
        assert not get_bin_path('xyz', required=False)
    except ValueError:
        assert False, 'get_bin_path("xyz") failed'


# Generated at 2022-06-12 23:31:21.086321
# Unit test for function get_bin_path
def test_get_bin_path():
    ''' test get_bin_path function '''
    # Test for the case the executable binary file is found in '/usr/bin'.
    import sys
    if sys.platform.startswith('darwin'):
        if sys.version_info[0] < 3:
            bin_path = get_bin_path('python')
        else:
            bin_path = get_bin_path('python3')
    else:
        bin_path = get_bin_path('python')
    assert bin_path == '/usr/bin/python'

# Generated at 2022-06-12 23:31:25.496674
# Unit test for function get_bin_path
def test_get_bin_path():
    for fn in ['get_bin_path', 'ansible.module_utils.common.file.get_bin_path']:
        assert get_bin_path(fn) == get_bin_path(fn)
        try:
            get_bin_path(fn + '-does-not-exist')
            raise Exception('Failed to raise exception in get_bin_path(fn + "-does-not-exist")')
        except ValueError as e:
            # verify exception is as expected
            assert 'Failed to find required executable' in str(e)

# Generated at 2022-06-12 23:31:32.399046
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('ls') == '/bin/ls'
    assert get_bin_path('ls', opt_dirs=['/usr/bin']) == '/bin/ls'
    assert get_bin_path('ls', ['/usr/bin', '/usr/sbin']) == '/bin/ls'
    assert get_bin_path('ls', opt_dirs=['/usr/sbin']) == '/usr/bin/ls'
    assert get_bin_path('ls', ['/usr/sbin']) == '/usr/bin/ls'

# Generated at 2022-06-12 23:31:37.670240
# Unit test for function get_bin_path
def test_get_bin_path():
    import sys
    import tempfile
    import shutil
    from distutils.spawn import find_executable
    from ansible.module_utils.six import PY3

    path = tempfile.mkdtemp()
    name = 'test_cmd'
    cmd = find_executable(name, path=path) or sys.executable
    f = tempfile.NamedTemporaryFile(suffix='.py', delete=False)
    if PY3:
        f.write(b'#!/usr/bin/env python3\n')
    else:
        f.write(b'#!/usr/bin/env python\n')
    f.write(b'print("Hello World")\n')
    f.close()
    subpath = tempfile.mkdtemp(dir=path)

# Generated at 2022-06-12 23:31:47.576485
# Unit test for function get_bin_path
def test_get_bin_path():
    ''' Test function get_bin_path '''

    # Valid test: FreeBSD
    if os.path.isfile('/etc/freebsd-update.conf'):
        assert get_bin_path('freebsd-version') == '/usr/bin/freebsd-version'

    # Valid test: Linux
    if os.path.isfile('/etc/lsb-release'):
        assert get_bin_path('lsb_release') == '/usr/bin/lsb_release'

    # Invalid test: no args
    try:
        get_bin_path()
    except TypeError:
        pass
    else:
        assert False

    # Invalid test: bad value

# Generated at 2022-06-12 23:31:50.089137
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('cat') == '/bin/cat'
    assert get_bin_path('cat', ['/usr/local/bin', '/usr/bin']) == '/usr/bin/cat'

# Generated at 2022-06-12 23:31:56.667984
# Unit test for function get_bin_path
def test_get_bin_path():
    path_dir = '/usr/local/bin'
    paths = os.environ.get("PATH") + os.pathsep + path_dir
    os.environ["PATH"] = paths
    bin_path = get_bin_path("sh")
    assert os.path.isfile(bin_path) == True
    assert bin_path.endswith("sh") == True

# Generated at 2022-06-12 23:31:58.225604
# Unit test for function get_bin_path
def test_get_bin_path():
    test_path = get_bin_path('python')
    assert os.path.isfile(test_path), 'get_bin_path did not return a valid path'

# Generated at 2022-06-12 23:31:59.000556
# Unit test for function get_bin_path
def test_get_bin_path():
    # very basic test with the existence of /bin/ls
    assert get_bin_path('ls') is not None

# Generated at 2022-06-12 23:32:13.201486
# Unit test for function get_bin_path
def test_get_bin_path():

    test_path = './test/units/module_utils/common/executable_exists_in_path/bin_path'
    test_path_no_file = './test/units/module_utils/common/executable_exists_in_path/bin_path_no'
    test_path_no_dir = './test/units/module_utils/common/executable_exists_in_path/bin_path_no.dir'
    test_dir_no_file = './test/units/module_utils/common/executable_exists_in_path/bin_dir_no'
    test_dir = './test/units/module_utils/common/executable_exists_in_path/bin_dir'

    # Test case: Executable in path
    bin_path = get_bin_

# Generated at 2022-06-12 23:32:18.827390
# Unit test for function get_bin_path
def test_get_bin_path():
    from ansible.module_utils._text import to_bytes
    try:
        get_bin_path('this_file_does_not_exist')
        assert False
    except ValueError:
        pass
    assert get_bin_path('sh') == to_bytes(os.path.normpath(os.path.normcase(os.path.realpath('/bin/sh'))))

# Generated at 2022-06-12 23:32:24.160372
# Unit test for function get_bin_path
def test_get_bin_path():
    bin_path = get_bin_path('python')
    assert bin_path == '/usr/bin/python'
    try:
        get_bin_path('nonexistent_exe', required=True)
        assert False, 'Expected ValueError!'
    except ValueError:
        pass
    try:
        get_bin_path('nonexistent_exe')
        assert False, 'Expected ValueError!'
    except ValueError:
        pass

# Generated at 2022-06-12 23:32:32.579441
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('python2') == '/usr/bin/python2'
    assert get_bin_path('python3') == '/usr/bin/python3'
    assert get_bin_path('python3', ['/usr/sbin', '/usr/bin']) == '/usr/bin/python3'
    try:
        get_bin_path('no_such_python')
    except (Exception) as e:
        assert isinstance(e, ValueError)
    else:
        assert False

# Generated at 2022-06-12 23:32:35.955736
# Unit test for function get_bin_path
def test_get_bin_path():
    import os
    import shutil
    import tempfile

    # build a fake path
    test_path = tempfile.mkdtemp()
    # build a fake executable in the path
    test_exec = os.path.join(test_path, 'test_exec')
    with open(test_exec, 'w') as f:
        f.write('#!%s\nexit 0\n' % os.path.join(test_path, 'bash'))
        os.chmod(test_exec, 0o755)
    # build a duplicate executable in a subdirectory
    test_exec_dupe = os.path.join(test_path, 'subdir', 'test_exec')
    os.makedirs(os.path.dirname(test_exec_dupe))

# Generated at 2022-06-12 23:32:43.220164
# Unit test for function get_bin_path
def test_get_bin_path():
    import sys
    import tempfile

    res = get_bin_path(sys.executable)
    assert res == sys.executable

    try:
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write('#!/bin/sh\nexit 0'.encode())
            executable = tmp_file.name
    except Exception as e:
        print('Failed to create executable file %s : %s' % (tmp_file.name, str(e)))
        exit(1)
    res = get_bin_path(executable)
    assert res == executable
    os.remove(executable)


# Generated at 2022-06-12 23:32:51.996233
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('ansible', ['/usr/local/bin']) == '/usr/local/bin/ansible'
    assert get_bin_path('ansible', ['/usr/local/bin'], required=True) == '/usr/local/bin/ansible'
    assert get_bin_path('ansible', None, required=True) == '/usr/bin/ansible'
    assert get_bin_path('ansible', None) == '/usr/bin/ansible'
    try:
        get_bin_path('this_should_not_exist_ever')
        raise Exception('Should have raised ValueError')
    except ValueError:
        pass

# Generated at 2022-06-12 23:33:01.338175
# Unit test for function get_bin_path
def test_get_bin_path():
    import sys
    import unittest

    from tempfile import NamedTemporaryFile

    class TestGetBinPath(unittest.TestCase):

        @classmethod
        def setUpClass(self):
            self.sys_path = os.environ.get('PATH', '').split(os.pathsep)
            self.cwd = os.getcwd()

        def test_get_bin_path(self):
            with NamedTemporaryFile() as f:
                bin_path = get_bin_path(f.name)
                self.assertEqual(bin_path, f.name)

        def test_get_bin_path_notfound(self):
            with self.assertRaises(ValueError):
                get_bin_path('/does/not/exist')


# Generated at 2022-06-12 23:33:08.685668
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    make sure the get_bin_path function returns the correct path to the passed in file
    '''
    match_list = {
        'sh': '/bin/sh',
        'no_file': None,
    }
    for test in match_list:
        f = get_bin_path(test)
        if test in ('sh', 'echo'):
            assert f == match_list.get(test)
        else:
            assert f is None

# Generated at 2022-06-12 23:33:15.135297
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('ls')
    assert get_bin_path('ls', ['/bin', '/usr/bin'])
    assert get_bin_path('ls', required=True)

    try:
        get_bin_path('ls_xyz')
        raise Exception("'ls_xyz' should not have been found")
    except ValueError:
        pass

    try:
        get_bin_path('ls_xyz', required=True)
        raise Exception("'ls_xyz' should not have been found")
    except:
        pass

# Generated at 2022-06-12 23:33:28.193944
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Test with PATH set to /bin and /usr/bin
    Test with PATH undefined
    Test with additional dirs supplied in opt_dirs
    Test with /sbin dirs included
    '''
    def test_get_bin_path(exe, p, opt_dirs, expected, display_paths):
        # exe: executable name
        # p:   PATH environ var
        # opt_dirs: optional list of dirs to search
        # expected:  root of full path that get_bin_path should return
        # display_paths:  True if want verbose output for debugging

        os.environ['PATH'] = p
        o = opt_dirs if opt_dirs else ''

# Generated at 2022-06-12 23:33:33.990478
# Unit test for function get_bin_path
def test_get_bin_path():

    # Test for finding binary in PATH
    assert get_bin_path('lsb_release') == '/usr/bin/lsb_release'

    # Test for finding binary in opt_dirs
    assert get_bin_path('lsb_release', ['/usr/bin']) == '/usr/bin/lsb_release'

    # Test for finding binary in PATH with additional opt_dirs
    assert get_bin_path('lsb_release', ['/tmp']) == '/usr/bin/lsb_release'

    # Test for finding binary with opt_dirs only
    assert get_bin_path('lsb_release', ['/tmp', '/usr/bin']) == '/usr/bin/lsb_release'

    # Test for finding binary with None opt_dirs
    assert get_bin_path('lsb_release', None)

# Generated at 2022-06-12 23:33:43.864404
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path('iwillneverbeinpath')
    except ValueError as e:
        assert 'Failed to find required executable "iwillneverbeinpath"' in str(e)
    else:
        assert False, 'Failed to raise exception'

    try:
        get_bin_path('iwillneverbeinpath', ['/bin'])
    except ValueError as e:
        assert 'Failed to find required executable "iwillneverbeinpath"' in str(e)
    else:
        assert False, 'Failed to raise exception'

    assert get_bin_path('ls', ['/bin']) == '/bin/ls'

# Generated at 2022-06-12 23:33:45.899161
# Unit test for function get_bin_path
def test_get_bin_path():
    ret = get_bin_path('this_exe_doesnt_exist_IPswa7VuXm1n')
    assert ret is None



# Generated at 2022-06-12 23:33:56.731869
# Unit test for function get_bin_path
def test_get_bin_path():

    import os
    import tempfile
    import shutil

    # save PATH and other env vars
    save_env = dict(os.environ)


# Generated at 2022-06-12 23:34:06.884195
# Unit test for function get_bin_path
def test_get_bin_path():

    test_bin_paths = (
        ('/bin/ls', ['/usr/sbin'], '/bin/ls'),
        ('ls', ['/usr/sbin'], '/bin/ls'),
        ('ls', ['/usr/sbin'], '/bin/ls'),
        ('ls', ['/usr/sbin', '/usr/bin', '/bin', '/usr/local/bin'], '/bin/ls'),
        ('ls', ['/tmp'], '/tmp/ls'),
        ('ls', ['/tmp', '/usr/bin'], '/tmp/ls'),
        ('/usr/local/bin/ls', None, '/usr/local/bin/ls'),
        ('ls', None, None),
    )

    def mkbin(path, content):
        dirname = os.path.dirname(path)

# Generated at 2022-06-12 23:34:11.308973
# Unit test for function get_bin_path
def test_get_bin_path():
    # test when there is no opt_dirs
    try:
        get_bin_path('/foo/bar')
    except ValueError as e:
        assert 'foo' in str(e) and 'bar' in str(e)

    # test when the opt_dirs is not a list
    try:
        get_bin_path('/foo/bar', '/foo')
    except Exception:
        pass

    # test when the opt_dirs is a list
    try:
        get_bin_path('/foo/bar', ['/foo'])
    except Exception:
        pass

# Generated at 2022-06-12 23:34:22.658991
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('sh') == '/bin/sh'
    assert get_bin_path('sh', ['/usr/bin', '/bin', '/usr/sbin', '/sbin']) == '/bin/sh'
    try:
        get_bin_path('some-unlikely-executable-name')
        assert False
    except ValueError as e:
        assert 'Failed to find required executable' in str(e)
    try:
        get_bin_path('ls', ['/usr/bin', '/bin', '/usr/sbin', '/sbin'])
        assert False
    except ValueError as e:
        assert 'Failed to find required executable' in str(e)


# Run test if module is called directly
if __name__ == '__main__':
    test_get_bin_path()

# Generated at 2022-06-12 23:34:31.202976
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    temp_dir = tempfile.gettempdir()
    assert temp_dir is not None

    # Test successful discovery
    # NOTE: This test will fail on platforms that don't have cp (wsl, I'm looking at you!)
    executable_path = get_bin_path('cp')

    # Test that we fail if the executable is missing
    try:
        get_bin_path('missing_executable_iwfsdhfiuerhg')
        assert False
    except ValueError:
        pass
    # Test that we fail if directory is not executable
    try:
        get_bin_path('/etc/fstab')
        assert False
    except ValueError:
        pass
    # Test that we succeed if the executable is given in an optional path
    get_bin_path('chmod', ['/bin'])
   

# Generated at 2022-06-12 23:34:33.228603
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        import nose2
        nose2.main()
    except ImportError:
        print("Please install nose2 to run unit tests")

# Generated at 2022-06-12 23:34:42.672351
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('cat') == '/bin/cat'
    assert get_bin_path('cat', opt_dirs=['/usr/bin']) == '/bin/cat'
    assert get_bin_path('cat', opt_dirs=['/usr/bin', '/bin']) == '/bin/cat'
    assert get_bin_path('cat', opt_dirs=['/usr/bin', '/bin'], required=True) == '/bin/cat'

    try:
        get_bin_path('no_such_file_is_hoped_for')
        assert False, "Failed to raise exception for missing executable"
    except ValueError:
        pass

# Generated at 2022-06-12 23:34:47.556439
# Unit test for function get_bin_path
def test_get_bin_path():
    assert os.path.exists(get_bin_path('sh'))
    assert os.path.exists(get_bin_path('sh', ['/bin']))
    try:
        get_bin_path('asdfasdf')
        assert False, 'Expected ValueError due to missing executable'
    except ValueError:
        pass

# Generated at 2022-06-12 23:34:53.687206
# Unit test for function get_bin_path
def test_get_bin_path():
    paths = ['/sbin', '/usr/sbin', '/usr/local/sbin']
    for arg in ['ip','ls','systemctl']:
        path = get_bin_path(arg)
        assert path == os.path.join(paths[0],arg), "Test failed: get_bin_path returned unexpected path"
    # Test return value when bin file is not found
    try:
        path = get_bin_path('non-existent-file')
    except ValueError:
        pass


# Generated at 2022-06-12 23:35:01.468045
# Unit test for function get_bin_path
def test_get_bin_path():
    import sys
    import tempfile
    from ansible.module_utils.common.file import TemporaryDirectory

    required = False
    path_dirs = []

    # Create test files
    tmpdir = tempfile.gettempdir()
    with TemporaryDirectory() as tmpdir:
        f1 = open(tmpdir + '/test1', 'w+')
        f1.close()
        f2 = open(tmpdir + '/test2', 'w+')
        f2.close()

        # No directory specified
        # Standard executable
        if sys.platform.startswith('win'):
            test1 = 'test1.exe'
        else:
            test1 = 'test1'
        path = get_bin_path(test1)
        assert path == os.path.abspath(test1)

        # Directory specified


# Generated at 2022-06-12 23:35:02.739175
# Unit test for function get_bin_path
def test_get_bin_path():
    bin_path = get_bin_path('ls')
    assert bin_path

# Generated at 2022-06-12 23:35:10.590270
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil

    def exec_file(name):
        f = open(name, 'w')
        f.write("#!/bin/sh\n")
        f.write("echo 0")
        f.close()
        os.chmod(name, 0o755)

    def make_exec(name):
        exec_file(name)
        return name

    temp_dir = tempfile.mkdtemp()

# Generated at 2022-06-12 23:35:21.046445
# Unit test for function get_bin_path
def test_get_bin_path():
    # get_bin_path(arg, opt_dirs=None, required=True):

    # Executable found in PATH
    assert get_bin_path('ls') == '/bin/ls'
    assert get_bin_path('ls', ['/usr/bin']) == '/bin/ls'
    assert get_bin_path('ls', None, False) == '/bin/ls'
    assert get_bin_path('ls', ['/usr/bin'], False) == '/bin/ls'

    # Executable found in opt_dirs.
    assert get_bin_path('ls', ['/bin']) == '/bin/ls'
    assert get_bin_path('ls', ['/bin', '/usr/bin']) == '/bin/ls'

    # Executable not found.

# Generated at 2022-06-12 23:35:25.020127
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('yes')
    assert get_bin_path('yes', opt_dirs=['.'])
    assert is_executable(get_bin_path('python3'))

# Generated at 2022-06-12 23:35:29.357740
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path('nonsense_executable')
        assert False, 'nonsense_executable unexpectedly found'

    except ValueError:
        assert True, 'correctly raised ValueError for nonsense_executable'

# Generated at 2022-06-12 23:35:37.000085
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    If a required executable is not in path, raises an Exception.
    '''
    import shutil
    import tempfile

    # Case 1: Executable not found
    #=======================================================================
    try:
        get_bin_path('not_in_path', required=True)
    except Exception:
        pass
    else:
        assert False, 'Expected an Exception'

    # Case 2: Executable found in optional dir
    #=======================================================================
    # Create temporary dir and put an executable in it
    tmpdir = tempfile.mkdtemp()
    with open(os.path.join(tmpdir, 'mybin'), 'wb') as f:
        f.write(b'#!/bin/sh')
    os.chmod(os.path.join(tmpdir, 'mybin'), 0o755)
   

# Generated at 2022-06-12 23:35:43.772838
# Unit test for function get_bin_path
def test_get_bin_path():
    # get_bin_path should error when not installed
    try:
        get_bin_path('asdf')
        assert False, "get_bin_path('asdf') should error"
    except ValueError:
        pass

    # get_bin_path('python') should not error
    get_bin_path('python')

# Generated at 2022-06-12 23:35:47.405342
# Unit test for function get_bin_path
def test_get_bin_path():
    if os.path.isdir('/usr/bin'):
        bin_path = get_bin_path('echo')
        assert os.path.isdir(bin_path) is False
        assert os.path.isfile(bin_path)
        assert is_executable(bin_path)



# Generated at 2022-06-12 23:35:59.944651
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    bin_path = tempfile.mkstemp()[1]
    os.chmod(bin_path, 0o755)

    def mock_is_executable(path):
        if path == bin_path:
            return True
        return os.access(path, os.X_OK)

    # pylint: disable=protected-access
    # call to get_bin_path with a valid path
    real_is_executable = is_executable
    is_executable = mock_is_executable

# Generated at 2022-06-12 23:36:11.176230
# Unit test for function get_bin_path
def test_get_bin_path():
    # Ensure that get_bin_path raises an error if the executable is not found
    if 'SHELL' in os.environ:
        _SHELL = os.environ['SHELL']
        os.environ['SHELL'] = '/bin/not-found-sh'
        try:
            get_bin_path('ansible-playbook')
        except Exception as ex:
            if 'required executable' not in str(ex):
                raise
        os.environ['SHELL'] = _SHELL
    # Ensure that get_bin_path raises an error if the executable is not found
    # when SHELL is not set.
    else:
        _SHELL = None

# Generated at 2022-06-12 23:36:19.214116
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Test case functions must start with the word test
    '''
    try:
        get_bin_path('non-existant-cmd')
        assert False, 'Expected ValueError not raised'
    except ValueError as e:
        assert 'Failed to find required executable "non-existant-cmd"' in str(e) and 'PATH' in str(e)

    assert get_bin_path('sh')
    assert get_bin_path('sh', ['/bin', '/sbin'])
    assert get_bin_path('sh', ['/non-existant-dir'])

# Generated at 2022-06-12 23:36:27.320841
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test a valid path
    valid_binary_path = get_bin_path('echo')
    assert valid_binary_path == '/bin/echo'
    # Test a valid path with optional directories
    valid_binary_path = get_bin_path('echo', ['/usr/bin', '/bin'])
    assert valid_binary_path == '/bin/echo'
    # Test an invalid path
    with pytest.raises(ValueError):
        bad_binary_path = get_bin_path('not_there')
    # Test a valid path with an invalid path
    valid_binary_path = get_bin_path('echo', ['/usr/bin', '/bin', '/no/such/place'])
    assert valid_binary_path == '/bin/echo'
    # Test an invalid path

# Generated at 2022-06-12 23:36:35.164759
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path("foo") == '/usr/bin/foo'
    assert get_bin_path("foo", opt_dirs=['/usr/bin/']) == '/usr/bin/foo'
    assert get_bin_path("foo", opt_dirs=['/usr/bin', '/usr/bin/']) == '/usr/bin/foo'
    assert get_bin_path("foo", opt_dirs=['/usr/bin/'], required=False) == '/usr/bin/foo'
    assert get_bin_path("foo", opt_dirs=[], required=False) is None
    assert get_bin_path("foo", opt_dirs=['']) is None
    assert get_bin_path("foo", required=False) is None

# Generated at 2022-06-12 23:36:41.221586
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('ansible-doc', required=False) is not None
    assert get_bin_path('ansible-doc', opt_dirs=['/'], required=False) is not None
    try:
        get_bin_path('ansible-doc', opt_dirs=['/tmp'], required=True)
    except ValueError:
        pass
    else:
        assert False, "Exception not raised"

# Generated at 2022-06-12 23:36:50.970815
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Test function get_bin_path
    '''

    try:
        nonexistent_path = get_bin_path('nonexistent-executable')
    except ValueError as e:
        assert 'Failed to find required executable "nonexistent-executable"' in str(e)
    except Exception as e:  # Unexpected error
        assert False

    try:
        opt_dirs = ['/opt/bin']
        nonexistent_path = get_bin_path('nonexistent-executable', opt_dirs=opt_dirs)
    except ValueError as e:
        assert 'Failed to find required executable "nonexistent-executable"' in str(e)
    except Exception as e:  # Unexpected error
        assert False


if __name__ == '__main__':
    test_get_bin_

# Generated at 2022-06-12 23:36:51.972733
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('python')

# Generated at 2022-06-12 23:36:59.226479
# Unit test for function get_bin_path
def test_get_bin_path():
    for i in range(5):
        path = get_bin_path('/bin/ls', required=True)
        assert os.path.exists(path) and os.path.isfile(path) and os.path.isabs(path) and os.access(path, os.X_OK)

# Generated at 2022-06-12 23:37:09.655813
# Unit test for function get_bin_path
def test_get_bin_path():
    import os
    test_path = os.path.abspath(os.path.dirname(__file__))
    test_fail_file = os.path.join(test_path, 'test-fail-file')
    test_file = os.path.join(test_path, 'test-file')
    test_dir = os.path.join(test_path, 'test-dir')

    assert get_bin_path('cat') == '/bin/cat'
    assert get_bin_path('cat', ['/foo']) == '/bin/cat'
    assert get_bin_path('cat', ['/bin']) == '/bin/cat'


# Generated at 2022-06-12 23:37:16.295053
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('ls') == '/bin/ls'
    assert get_bin_path('chroot') == '/usr/sbin/chroot'
    assert get_bin_path('crontab', ['/usr/local/bin']) == '/usr/local/bin/crontab'
    import pytest
    with pytest.raises(ValueError, match='Failed to find'):
        get_bin_path('unknown_command')

# Generated at 2022-06-12 23:37:21.243711
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil
    import sys

    if sys.platform.startswith('win'):
        # This test only applies when running on Windows
        return

    test_prog_file_name = 'test_prog'

    dirs = [tempfile.mkdtemp(suffix='_test_dir'), tempfile.mkdtemp(suffix='_test_dir')]

# Generated at 2022-06-12 23:37:27.080887
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile

    def touch(path):
        with open(path, 'a'):
            os.utime(path, None)

    # Create a temporary directory
    tmpdir = tempfile.mkdtemp()

    # Create a file in the temporary directory
    touch(os.path.join(tmpdir, "bin_path_test"))

    # Test 1: File exists and is executable
    assert get_bin_path('bin_path_test', [tmpdir]) == os.path.join(tmpdir, 'bin_path_test')

    # Test 2: File exists and is not executable
    os.chmod(os.path.join(tmpdir, "bin_path_test"), 0o0600)

# Generated at 2022-06-12 23:37:33.227424
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path('this_executable_does_not_exist')
    except ValueError as e:
        assert 'Failed to find required executable' in e.args[0]
        assert 'this_executable_does_not_exist' in e.args[0]
    else:
        assert False, "ValueError should have been raised"