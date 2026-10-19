

# Generated at 2022-06-12 23:27:46.409380
# Unit test for function get_bin_path
def test_get_bin_path():
    import sys
    import pytest
    from ansible.module_utils.common.file import get_bin_path

    def test_get_bin_path_error(arg, opt_dirs=None, required=None):
        with pytest.raises(Exception):
            get_bin_path(arg, opt_dirs, required)

    if sys.platform == 'win32':
        # Check default paths
        assert get_bin_path('dir') == 'C:\\WINDOWS\\system32\\dir.EXE'

        # Check opt_dirs
        assert get_bin_path('dir', opt_dirs=['C:\\WINDOWS\\system32']) == 'C:\\WINDOWS\\system32\\dir.EXE'

# Generated at 2022-06-12 23:27:54.933791
# Unit test for function get_bin_path
def test_get_bin_path():
    from ansible.module_utils.common.process import get_bin_path

    # Test finding standard executables
    assert get_bin_path('echo')

    # Test finding executable with relative path
    assert get_bin_path('./echo')

    # Test finding executable where one path is None
    assert get_bin_path('echo', opt_dirs=['/usr/bin', None])

    # Test finding executable that doesn't exist
    try:
        get_bin_path('does_not_exist')
    except Exception:
        pass
    else:
        # This statement should not be reached if test is successful
        assert False

    # Test finding executable with optional path
    assert get_bin_path('echo', opt_dirs=['/bin'])

    # Test finding executable with optional path that is None

# Generated at 2022-06-12 23:28:02.059863
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Test to see if get_bin_path will raise an exception when called.
    Also test to see if get_bin_path will find executables in the paths.
    '''
    from ansible.module_utils._text import to_bytes
    PATH = os.environ.get('PATH', None)
    bin_test_paths = ['/bin', '/usr/bin', '/usr/local/bin']

# Generated at 2022-06-12 23:28:11.407334
# Unit test for function get_bin_path
def test_get_bin_path():

    # Test 1: with required
    try:
        get_bin_path('cat')
        print('Test 1 passed')
    except Exception as e:
        print('Test 1 failed: %s' % str(e))

    # Test 2: without required
    try:
        get_bin_path('cat', required=False)
        print('Test 2 passed')
    except Exception as e:
        print('Test 2 failed: %s' % str(e))

    # Test 3: with wrong path
    try:
        get_bin_path('cat', opt_dirs=['/bad'])
        print('Test 3 failed: Could not detect missing binary')
    except Exception as e:
        print('Test 3 passed: %s' % str(e))

# Generated at 2022-06-12 23:28:20.006483
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Check if get_bin_path() finds the executable it is supposed to find.
    '''

    # test for required shell binaries
    for arg in (('/bin/sh', '/bin/sh'), ('ls', 'ls'), ('chmod', 'chmod'), ('cp', 'cp')):
        try:
            get_bin_path(arg[0])
        except ValueError as e:
            print(e)
            print('Failed to find required shell executable "%s" in path: %s' % (arg[0], os.environ.get('PATH')))
        else:
            print('Found shell executable "%s" in path: %s' % (arg, os.environ.get('PATH')))

# Generated at 2022-06-12 23:28:27.249216
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('ls', ['/bin']) == '/bin/ls'
    assert get_bin_path('ls') in ['/bin/ls', '/usr/bin/ls']
    assert get_bin_path('ls', required=False) in ['/bin/ls', '/usr/bin/ls']
    assert get_bin_path('ls', ['/bin', '/usr/local/bin']) == '/bin/ls'

    try:
        get_bin_path('missing_command')
    except ValueError as e:
        assert "Failed to find required executable \"missing_command\" in paths" in str(e)
    try:
        get_bin_path('missing_command', required=False)
    except ValueError as e:
        assert "Failed to find required executable \"missing_command\" in paths" in str

# Generated at 2022-06-12 23:28:36.679007
# Unit test for function get_bin_path
def test_get_bin_path():
    # os.pathsep is ':' on Unix and ';' on Windows, so to cover both we just use both
    os.environ['PATH'] = '/bin' + os.pathsep + '/sbin'
    assert get_bin_path('bash') == '/bin/bash'
    assert get_bin_path('ls') == '/bin/ls'
    assert get_bin_path('ip') == '/sbin/ip'
    try:
        get_bin_path('notthere')
        assert False, "Should have raised an exception"
    except ValueError:
        pass
    # None in dir list returns None
    assert get_bin_path('bash', opt_dirs=[None]) == '/bin/bash'
    # Empty dir list returns None

# Generated at 2022-06-12 23:28:43.684045
# Unit test for function get_bin_path
def test_get_bin_path():

    assert get_bin_path("sleep") == "/bin/sleep"
    assert get_bin_path("sleep", opt_dirs=["/bin"]) == "/bin/sleep"
    assert get_bin_path("sleep", opt_dirs=["/bin", "/bin"]) == "/bin/sleep"

    try:
        get_bin_path("non_existent_file")
        raise Exception("Not found")
    except ValueError:
        pass

    try:
        get_bin_path("non_existent_file", opt_dirs=["/bin"])
        raise Exception("Not found")
    except ValueError:
        pass


# Generated at 2022-06-12 23:28:52.521547
# Unit test for function get_bin_path
def test_get_bin_path():
    import sys

    assert get_bin_path('w') == '/usr/bin/w'
    assert get_bin_path('top') == '/usr/bin/top'
    assert get_bin_path('ls','/bin') == '/bin/ls'
    try:
        get_bin_path('top',['/usr/local/bin'])
        assert 0
    except ValueError as e:
        assert "Failed to find required executable" in str(e)

    assert get_bin_path('ls',['/usr/local/bin','/bin']) == '/bin/ls'
    try:
        get_bin_path('top',['/usr/bin','/usr/local/bin'])
        assert 0
    except ValueError as e:
        assert "Failed to find required executable" in str(e)

# Generated at 2022-06-12 23:29:03.643051
# Unit test for function get_bin_path
def test_get_bin_path():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.six.moves import StringIO
    import sys
    import pytest

    test_data = [
        ('python', True, '/usr/bin/python'),
        ('bash', True, '/bin/bash'),
        ('not a valid exe name', False, 'not a valid exe name'),
        ('non_existent_exec', False, 'non_existent_exec'),
    ]

    # Save stdout so we can restore it and hide pytest's output
    stdout = sys.stdout

    # Suppress all pytest output, as this test is not run in the context of a module
    sys.stdout = StringIO()

    # Execute the get_bin_path function

# Generated at 2022-06-12 23:29:12.728812
# Unit test for function get_bin_path
def test_get_bin_path():
    testpath = os.path.realpath(os.path.dirname(__file__))
    # returns the full path for an executable in PATH
    assert get_bin_path('python')
    # returns the full path for an executable in PATH (bash)
    assert get_bin_path('env')
    # returns the full path for an executable in PATH (zsh)
    assert get_bin_path('zsh')
    # returns the full path for an executable in PATH (/sbin/poweroff)
    assert get_bin_path('poweroff')
    # returns the full path for an executable in PATH (/usr/sbin/chkconfig)
    assert get_bin_path('chkconfig')
    # returns the full path for an executable in PATH (/usr/local/sbin/lsof)

# Generated at 2022-06-12 23:29:17.610888
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('no_such_program', opt_dirs=['/dev/null']) == '/dev/null/no_such_program'
    try:
        get_bin_path('no_such_program')
    except ValueError:
        pass
    else:
        raise Exception("Unit test failed")

    assert get_bin_path('cat') == '/bin/cat'

# Generated at 2022-06-12 23:29:22.038839
# Unit test for function get_bin_path
def test_get_bin_path():
    bin_path = '/usr/bin/ls'
    opt_dirs = ['/bin', '/usr/bin']

    assert get_bin_path('ls', opt_dirs, True) == bin_path
    assert get_bin_path('ls', None, True) == bin_path
    assert get_bin_path('ls', [], True) == bin_path
    assert get_bin_path('ls', opt_dirs) == bin_path

# Generated at 2022-06-12 23:29:31.657713
# Unit test for function get_bin_path
def test_get_bin_path():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils._text import to_native
    from ansible.module_utils.common.file import is_executable
    # Utility function for testing
    def test_get_bin_path_wrapper(mocker, arg, opt_dirs=None,
                                  required=True, expected_path=None,
                                  raises_exception=False):
        '''
        Test get_bin_path using mocker and calling into the module context
        '''
        bin_path = None
        try:
            bin_path = basic.get_bin_path(arg, opt_dirs=opt_dirs)
        except (OSError, ValueError) as e:
            if raises_exception:
                pass

# Generated at 2022-06-12 23:29:41.966581
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test 1: required executable (ping) exists in PATH and should be found
    assert get_bin_path("ping", required=True)

    # Test 2: non-required executable (ping) exists in PATH and should be found
    assert get_bin_path("ping", required=False)

    # Test 3: required executable (invalid) does not exist in PATH and should raise exception
    try:
        get_bin_path("invalid", required=True)
    except ValueError:
        pass
    else:
        assert(False)

    # Test 4: non-required executable (invalid) does not exist in PATH and should be None
    assert get_bin_path("invalid", required=False) is None

# Generated at 2022-06-12 23:29:45.712836
# Unit test for function get_bin_path
def test_get_bin_path():
    # Use the path for the ansible executable as a known good input
    paths = ['/usr/bin', '/bin', '/usr/sbin', '/sbin', '/usr/local/bin', '/usr/local/sbin']
    bin_path = get_bin_path('ansible', paths)
    assert bin_path

# Generated at 2022-06-12 23:29:50.165872
# Unit test for function get_bin_path
def test_get_bin_path():
    # When
    result = get_bin_path('python2')

    # Then
    assert os.path.exists(result)
    assert os.path.isfile(result)
    assert is_executable(result)

    # When
    result = get_bin_path('python3')
    # Then
    assert os.path.exists(result)
    assert os.path.isfile(result)
    assert is_executable(result)

# Generated at 2022-06-12 23:29:58.665605
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path('echo')
    except Exception:
        assert False, 'Executable "echo" should exist in PATH.'

    try:
        get_bin_path('thiscommanddoesnotexist')
        assert False, 'Executable "thiscommanddoesnotexist" should not exist in PATH.'
    except ValueError:
        pass

    try:
        get_bin_path('echo', [os.path.dirname(os.path.abspath(__file__))])
    except ValueError:
        assert False, 'Executable "echo" should exist in PATH.'


# Generated at 2022-06-12 23:30:00.667113
# Unit test for function get_bin_path
def test_get_bin_path():
    bin_path = get_bin_path('which')
    assert bin_path == '/usr/bin/which'

# Generated at 2022-06-12 23:30:11.485379
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil

    def _init_temp_path():
        tmp_dir = tempfile.mkdtemp()
        tmp_file_1 = tempfile.NamedTemporaryFile(dir=tmp_dir, delete=False)
        shutil.copyfile('/bin/pwd', tmp_file_1.name)
        os.chmod(tmp_file_1.name, 0o755)
        tmp_file_2 = tempfile.NamedTemporaryFile(dir=tmp_dir, delete=False)
        shutil.copyfile('/bin/pwd', tmp_file_2.name)
        os.chmod(tmp_file_2.name, 0o750)
        return tmp_dir, tmp_file_1, tmp_file_2


# Generated at 2022-06-12 23:30:20.128239
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('sh') == '/bin/sh'
    assert get_bin_path('sh', opt_dirs=['/usr/bin', '/bin']) == '/bin/sh'
    assert get_bin_path('sh', opt_dirs=['/usr/bin', '/bin']) == '/bin/sh'
    assert get_bin_path('sh', opt_dirs=['/usr/bin', '/bin'], required=True) == '/bin/sh'

# Generated at 2022-06-12 23:30:29.874852
# Unit test for function get_bin_path
def test_get_bin_path():
    import mock
    from ansible.module_utils.common.system import get_bin_path

    def call_get_bin_path(arg, opt_dirs, required=None):
        return get_bin_path(
            arg=arg,
            opt_dirs=opt_dirs,
            required=required
        )

    with mock.patch('ansible.module_utils.common.file.is_executable') as mock_is_executable:
        mock_is_executable.return_value = True

# Generated at 2022-06-12 23:30:40.909452
# Unit test for function get_bin_path
def test_get_bin_path():
    import sys
    import os

    # Test successful finding of executable
    assert get_bin_path('%s' % sys.executable.split(os.path.sep)[-1]) == sys.executable
    assert get_bin_path('%s' % sys.executable.split(os.path.sep)[-1], required=False) == sys.executable

    # Test error conditions for path not found
    got_exception = False
    try:
        get_bin_path('nosuchpath')
    except ValueError as e:
        got_exception = True
        assert 'Failed to find required executable "nosuchpath"' in str(e)
    assert got_exception

    # Test error conditions for path not found with deprecated parameter
    got_exception = False

# Generated at 2022-06-12 23:30:49.127166
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('cat') == '/bin/cat'
    assert get_bin_path('pwd') == '/bin/pwd'
    assert get_bin_path('pwd', ['/usr/bin', '/usr/sbin']) == '/bin/pwd'
    assert get_bin_path('pwd', ['/usr/bin', '/usr/sbin'], ['/bin']) == '/bin/pwd'
    assert get_bin_path('pwd', ['/usr/bin', '/usr/sbin'], ['/usr/bin', '/usr/sbin']) == '/usr/bin/pwd'
    assert get_bin_path('pwd', ['/usr/bin', '/usr/sbin'], ['/usr/sbin', '/usr/bin']) == '/usr/sbin/pwd'

# Generated at 2022-06-12 23:30:59.602086
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Test function get_bin_path
    '''
    path = get_bin_path('/bin/ls', ['/bin'])
    assert path == '/bin/ls'
    path = get_bin_path('ls', ['/bin'])
    assert path == '/bin/ls'
    path = get_bin_path('ls')
    assert path == '/bin/ls'
    try:
        get_bin_path('ls', ['/nonexistent'])
        assert False, 'should raise ValueError'
    except ValueError:
        pass
    try:
        get_bin_path('/bin/ls', ['/nonexistent'])
        assert False, 'should raise ValueError'
    except ValueError:
        pass

# Generated at 2022-06-12 23:31:05.122059
# Unit test for function get_bin_path
def test_get_bin_path():
    opt_dirs = ['/usr/bin', '/bin']
    # whereis(1) is a standard utility on most common platforms.
    assert get_bin_path('whereis', opt_dirs=opt_dirs)
    assert get_bin_path('whereis', required=True, opt_dirs=opt_dirs)

# Generated at 2022-06-12 23:31:06.465723
# Unit test for function get_bin_path
def test_get_bin_path():
    if not os.path.isfile(get_bin_path('sh')):
        raise Exception('get_bin_path failed to find known binary "sh"')

# Generated at 2022-06-12 23:31:14.428677
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path("non_existing_file_foo_bar")
    except ValueError as e:
        if "Failed to find required executable" in str(e):
            assert True
    assert get_bin_path("python", ["/usr/bin"]) == "/usr/bin/python"
    assert get_bin_path("python") == "/usr/bin/python"
    assert get_bin_path("python", ["/root"]) == "/root/python"
    assert get_bin_path("python", ["/root", "/root"]) == "/root/python"

# Generated at 2022-06-12 23:31:23.626565
# Unit test for function get_bin_path
def test_get_bin_path():
    import shutil
    import tempfile
    import unittest
    import ansible.utils.unsafe_proxy

    class TestGetBinPath(unittest.TestCase):
        def setUp(self):
            tmpdir = tempfile.mkdtemp(prefix='ansible-tmp', dir=None)
            self.addCleanup(shutil.rmtree, tmpdir)
            if os.environ.get("PATH", None) is None:
                self.addCleanup(os.environ.pop, "PATH")
            else:
                self.addCleanup(os.environ.update, {"PATH": os.environ["PATH"]})
            os.environ["PATH"] = os.path.pathsep.join([tmpdir, os.environ["PATH"]])


# Generated at 2022-06-12 23:31:33.557683
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('sh') is not None, 'sh missing in PATH'
    assert get_bin_path('zebulon') is None, 'zebulon found in PATH'
    assert get_bin_path('zebulon', opt_dirs=['/dev']) is None, 'zebulon found in /dev'
    try:
        get_bin_path('zebulon')
        raise AssertionError('Failed to raise ValueError for missing zebulon')
    except ValueError:
        pass
    try:
        get_bin_path('zebulon', required=True)
        raise AssertionError('Failed to raise ValueError for missing zebulon')
    except ValueError:
        pass

# Generated at 2022-06-12 23:31:46.095964
# Unit test for function get_bin_path
def test_get_bin_path():
    '''Test function get_bin_path running under python3'''
    arg = 'vi'
    opt_dirs = []
    required = True
    assert get_bin_path(arg, opt_dirs, required) == '/usr/bin/vi'
    arg = 'vi'
    opt_dirs = ['/usr/local/bin']
    required = True
    assert get_bin_path(arg, opt_dirs, required) == '/usr/bin/vi'
    arg = 'vi'
    opt_dirs = ['/usr/local/bin', '/bin']
    required = True
    assert get_bin_path(arg, opt_dirs, required) == '/usr/bin/vi'
    arg = 'vi'

# Generated at 2022-06-12 23:31:56.437786
# Unit test for function get_bin_path
def test_get_bin_path():
    path = os.path.dirname(os.path.abspath(__file__))
    test0_expected_value = 'true'
    if os.path.exists(path + '/test0'):
        test0_expected_value = path + '/test0'
    test_module_commands = [
        ('test0', [path], test0_expected_value),
        ('test0', [path, ''], test0_expected_value),
        ('test0', [path, '/invalid'], test0_expected_value),
        ('test0', [path, '/bin'], test0_expected_value),
    ]
    test_module_commands_fail = [
        ('test0', ['/invalid', '/invalid'], ValueError),
        ('test0', [], ValueError),
    ]

# Generated at 2022-06-12 23:32:05.464155
# Unit test for function get_bin_path
def test_get_bin_path():
    import shutil
    import tempfile

    example_path_name = 'example'
    expected_path_name = os.path.join(tempfile.gettempdir(), example_path_name)

    tmpdir_path = tempfile.mkdtemp()
    try:
        with open(expected_path_name, 'w') as f:
            f.write('content')
        try:
            os.chmod(expected_path_name, 0o755)
            os.environ['PATH'] = tmpdir_path
            assert get_bin_path(example_path_name) == expected_path_name
        finally:
            del os.environ['PATH']
    finally:
        shutil.rmtree(tmpdir_path)
        os.remove(expected_path_name)

# Generated at 2022-06-12 23:32:15.322378
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil
    import signal

    class MockPopen:
        def __init__(self, args, stdout=None, stderr=None):
            self.returncode = 0
            pass

        def communicate(self):
            return "output\n", None

        def poll(self):
            return self.returncode

        def wait(self):
            return self.returncode

    def _mock_check_output(args, opt_dirs=None, required=True, stdin=None, stderr=None, shell=False):
        if args == ['true']:
            return "output\n"
        else:
            raise Exception('failed')

    class MockProcess:
        def __init__(self):
            self.pid = 99999

        def poll(self):
            return None



# Generated at 2022-06-12 23:32:20.709235
# Unit test for function get_bin_path
def test_get_bin_path():
    bin_path = get_bin_path('sh')
    # NOTE:  This is not a path we can rely on.  See
    #        https://github.com/ansible/ansible/issues/50984
    # assert bin_path == '/bin/sh'

# Generated at 2022-06-12 23:32:24.572687
# Unit test for function get_bin_path
def test_get_bin_path():
    import sys
    if sys.platform.startswith('win'):
        return
    try:
        get_bin_path('this_path_must_not_exist_or_the_test_will_fail')
    except ValueError as e:
        if 'this_path_must_not_exist_or_the_test_will_fail' not in str(e):
            raise Exception('Unexpected ValueError: %s' % e)
    else:
        raise Exception('Expected ValueError, but none was raised')

    assert get_bin_path('sh')

# Generated at 2022-06-12 23:32:26.434880
# Unit test for function get_bin_path
def test_get_bin_path():
    bin_path = get_bin_path('ansible-playbook')
    assert(bin_path.endswith('ansible-playbook'))

# Generated at 2022-06-12 23:32:38.816200
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        from shutil import which
    except ImportError:
        from distutils.spawn import find_executable as which
    get_bin_path('bash')
    get_bin_path('bash', ['/bin', '/usr/local/bin'])
    try:
        get_bin_path('wrong_executable')
    except ValueError:
        pass
    else:
        raise AssertionError('Executable found in PATH but should not.')

    try:
        get_bin_path('wrong_executable', ['/wrong/dir'])
    except ValueError:
        pass
    else:
        raise AssertionError('Executable found in PATH but should not.')


# Generated at 2022-06-12 23:32:45.839926
# Unit test for function get_bin_path
def test_get_bin_path():

    def do_assert(fn):
        try:
            get_bin_path(fn)
            assert False
        except ValueError:
            pass

    do_assert('/this/file/does/not/exist')
    do_assert('/bin')
    do_assert('/bin/')

    get_bin_path('/bin/hostname')
    get_bin_path('hostname', ['/bin'])

# Generated at 2022-06-12 23:32:52.045960
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile

    testpath = os.path.join(tempfile.gettempdir(), 'test_get_bin_path')
    os.mkdir(testpath)
    exe_path = os.path.join(testpath, 'exe')
    f = open(exe_path, 'w')
    f.write('#!/bin/bash')
    f.close()

# Generated at 2022-06-12 23:32:56.913239
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        bp = get_bin_path('cat', ['/bin', '/usr/bin'])
    except ValueError:
        raise Exception('Unit test for function get_bin_path failed: function raised ValueError exception')
    assert (bp == '/bin/cat')

# Generated at 2022-06-12 23:32:58.573655
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    This is a unit test
    '''
    bin_path_ping = get_bin_path('ping')
    assert bin_path_ping != None



# Generated at 2022-06-12 23:33:05.320282
# Unit test for function get_bin_path
def test_get_bin_path():

    # test for finding executables in PATH on a unix like operating system
    if 'PATH' in os.environ:
        assert os.path.isabs(get_bin_path('env')) == True
        assert 'PATH' in os.environ
        assert 'env' in get_bin_path('env')

    # test for finding executables in custom path
    custom_paths = ['.', '/bin']
    assert os.path.isabs(get_bin_path('sh', opt_dirs=custom_paths)) == True
    assert 'sh' in get_bin_path('sh', opt_dirs=custom_paths)
    assert '/bin' in get_bin_path('sh', opt_dirs=custom_paths)

    # test for an exception if the executable is not found

# Generated at 2022-06-12 23:33:10.210912
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('ls') == '/bin/ls'
    assert get_bin_path('ls', opt_dirs=['/usr/bin']) == '/usr/bin/ls'
    assert get_bin_path('COPYING', opt_dirs=['/usr/bin']) == '/usr/bin/COPYING'
    assert get_bin_path('curl') == '/usr/bin/curl'
    assert get_bin_path('curl', opt_dirs=['/usr/bin']) == '/usr/bin/curl'
    assert get_bin_path('curl', opt_dirs=['/bin']) == '/bin/curl'
    assert get_bin_path('curl', opt_dirs=['/bin']) == '/bin/curl'
    assert get_

# Generated at 2022-06-12 23:33:19.260291
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('cat') == '/bin/cat'
    assert get_bin_path('/bin/cat') == '/bin/cat'
    assert get_bin_path('/bin/cat', ['/usr/bin']) == '/bin/cat'
    assert get_bin_path('/bin/cat', ['/usr/bin'], True) == '/bin/cat'
    try:
        assert get_bin_path('/bin/cat', ['/usr/bin'], False)
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "/bin/cat" in paths: /usr/bin:/bin:/usr/sbin:/sbin:/usr/local/sbin'

# Generated at 2022-06-12 23:33:30.106672
# Unit test for function get_bin_path
def test_get_bin_path():
    import shutil, tempfile
    tempdir = tempfile.mkdtemp()

# Generated at 2022-06-12 23:33:35.224277
# Unit test for function get_bin_path
def test_get_bin_path():
    from ansible.module_utils import basic

    assert basic.get_bin_path('echo') == '/bin/echo'
    assert basic.get_bin_path('ansible-config') == os.path.normpath(os.environ.get('ANSIBLE_CONFIG', '/etc/ansible/ansible.cfg'))
    assert basic.get_bin_path(os.environ.get('ANSIBLE_CONFIG', '/etc/ansible/ansible.cfg')) == os.environ.get('ANSIBLE_CONFIG', '/etc/ansible/ansible.cfg')


# Generated at 2022-06-12 23:33:41.427288
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        # check if get_bin_path found a command
        find_path = get_bin_path('find')
        assert find_path != None

        # check if get_bin_path raises an exception when the command is not found
        get_bin_path('find_fake_command')
        assert False
    except ValueError:
        assert True
    except:
        assert False

# Generated at 2022-06-12 23:33:48.261471
# Unit test for function get_bin_path
def test_get_bin_path():
    path = []
    assert get_bin_path('python') == get_bin_path('./python', path)
    assert get_bin_path('/bin/bash') == get_bin_path('./bin/bash', path)

    # the test system doesn't always have the command 'true', so use the command 'true' that is part of this script
    path = [os.path.dirname(os.path.realpath(__file__))]
    assert get_bin_path('true', path) == get_bin_path('./true', path)

# Generated at 2022-06-12 23:33:59.316822
# Unit test for function get_bin_path
def test_get_bin_path():

    # if specified program is not available
    try:
        get_bin_path('non-existent-program')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "non-existent-program" in paths: /bin:/usr/bin:/usr/local/bin:/sbin:/usr/sbin:/usr/local/sbin'
    else:
        assert False

    # if specified program is available
    assert get_bin_path('date') == '/bin/date'

    # if specified program is available in additional directories
    assert get_bin_path('date', opt_dirs=['/usr/bin', '/usr/local/bin']) == '/bin/date'

    # if specified program is available in additional directories but not in PATH

# Generated at 2022-06-12 23:34:10.047072
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test 1: Test to find a known system executable
    res = get_bin_path('rm', opt_dirs=['/bin'], required=True)
    assert res == '/bin/rm'
    try:
        get_bin_path('no_such_executable', opt_dirs=['/bin'], required=True)
        assert False
    except ValueError:
        pass

    # Test 2: Test to find a known system executable with an alternate
    # path in opt_dirs
    res = get_bin_path('rm', opt_dirs=['/bin'], required=True)
    assert res == '/bin/rm'
    # Test 3: Test to find a known system executable with an alternate
    # path in opt_dirs but required=False

# Generated at 2022-06-12 23:34:17.935033
# Unit test for function get_bin_path
def test_get_bin_path():
    # Make tmp dir and put some mock executables there
    import tempfile
    td = tempfile.mkdtemp()
    with open(os.path.join(td, 'my-exe'), 'wb', 0o777) as f:
        f.write(b'#!/usr/bin/env python\n')
    with open(os.path.join(td, 'my-exe2'), 'wb', 0o777) as f:
        f.write(b'#!/usr/bin/env python\n')
    os.environ['PATH'] = td

    # Ensure no errors raised
    get_bin_path('my-exe')

    # Ensure errors raised in appropriate cases
    try:
        get_bin_path('not-my-exe')
    except ValueError as e:
        assert 'Failed to find required executable'

# Generated at 2022-06-12 23:34:27.636515
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('ls') is not None

    from ansible.compat.tests import unittest

    try:
        get_bin_path('unknown_executable')
        assert False, "Expected an exception"
    except Exception as e:
        assert e.__class__ == ValueError

    try:
        get_bin_path('unknown_executable', ['/dev/null'])
        assert False, "Expected an exception"
    except Exception as e:
        assert e.__class__ == ValueError

    try:
        get_bin_path('unknown_executable', required=False)
        assert False, "Expected an exception"
    except Exception as e:
        assert e.__class__ == ValueError

# Generated at 2022-06-12 23:34:38.613598
# Unit test for function get_bin_path
def test_get_bin_path():
    import ansible.module_utils.basic
    import mock
    from ansible.module_utils.common.file import is_executable

    fake_paths = ['/usr/bin', '/usr/local/bin', '/usr/sbin']

    bin_path = ansible.module_utils.common.get_bin_path('date', fake_paths)
    is_executable.assert_called_with(bin_path)

    with mock.patch('os.path.exists') as mock_exists:
        mock_exists.return_value = False
        with mock.patch('os.path.isdir') as mock_is_dir:
            mock_is_dir.return_value = False


# Generated at 2022-06-12 23:34:48.875202
# Unit test for function get_bin_path
def test_get_bin_path():
    from ansible.utils.plugin_docs import get_bin_path as gbp

    # Test for an existing executable
    assert gbp('date') is not None
    # Test for an executable that does not exist
    try:
        gbp('invalid_command')
        assert False
    except ValueError:
        pass
    # Test an optional list of directories
    assert gbp("date", opt_dirs=[os.path.dirname(gbp("date"))]) is not None
    # Test that specifying a directory that isn't in the path and doesn't contain the executable fails
    try:
        gbp("date", opt_dirs=['/tmp'])
        assert False
    except ValueError:
        pass
    # Test the deprecated required argument

# Generated at 2022-06-12 23:34:57.173279
# Unit test for function get_bin_path
def test_get_bin_path():
    path1 = get_bin_path("/usr/bin/python")
    assert os.path.exists(path1)
    assert os.access(path1, os.X_OK)

    path2 = get_bin_path("/usr/bin/python", ['/usr/bin', '/usr/local/bin'])
    assert os.path.exists(path2)
    assert os.access(path2, os.X_OK)

    path3 = get_bin_path("/usr/bin/python", ['/usr/bin', '/usr/local/bin'], True)
    assert os.path.exists(path3)
    assert os.access(path3, os.X_OK)


# Generated at 2022-06-12 23:35:06.354931
# Unit test for function get_bin_path
def test_get_bin_path():
    bin_path = get_bin_path('sh')
    print(bin_path)
    assert bin_path == '/bin/sh'

    bin_path = get_bin_path('/bin/sh')
    print(bin_path)
    assert bin_path == '/bin/sh'

    bin_path = get_bin_path('/bin/sh', opt_dirs=['/usr/bin'])
    print(bin_path)
    assert bin_path == '/bin/sh'

    bin_path = get_bin_path('/bin/sh', opt_dirs=['/bin'])
    print(bin_path)
    assert bin_path == '/bin/sh'

    bin_path = get_bin_path('sh', opt_dirs=['/bin'])
    print(bin_path)


# Generated at 2022-06-12 23:35:17.674801
# Unit test for function get_bin_path
def test_get_bin_path():
    def mock_is_executable(path):
        return True

    def mock_isdir(path):
        return False

    def mock_exists(path):
        return True

    def mock_getenv(key, default=None):
        if key == 'PATH':
            return '/sbin:/bin:/usr/sbin:/usr/bin'
        return default

    old_is_executable = is_executable
    old_isdir = os.path.isdir
    old_exists = os.path.exists
    old_getenv = os.environ.get
    is_executable.side_effect = mock_is_executable
    os.path.isdir.side_effect = mock_isdir
    os.path.exists.side_effect = mock_exists

# Generated at 2022-06-12 23:35:24.210345
# Unit test for function get_bin_path
def test_get_bin_path():
    # The results should be the same in all cases
    assert get_bin_path('python', opt_dirs=['/usr/bin', '/bin']) == get_bin_path('python', opt_dirs=[b'/usr/bin', b'/bin'])

    python = get_bin_path('python')
    perl = get_bin_path('perl')

    try:
        get_bin_path('foo')
        assert False
    except ValueError:
        assert True

    # Test search_paths argument
    assert get_bin_path('python', opt_dirs=[]) == python
    assert get_bin_path('python', opt_dirs=['/bin', '/usr/bin']) == python
    assert get_bin_path('perl', opt_dirs=[]) == perl
    assert get_bin_path

# Generated at 2022-06-12 23:35:34.981868
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil
    path = tempfile.mkdtemp()

    # Test paths arg
    assert get_bin_path(os.path.basename(__file__), [os.path.dirname(__file__)]) == __file__
    assert get_bin_path(os.path.basename(__file__), opt_dirs=[path]) == os.path.join(path, os.path.basename(__file__))

    # Test required arg (deprecated)
    with open(os.path.join(path, os.path.basename(__file__)), "w") as f:
        f.write("\n")

# Generated at 2022-06-12 23:35:46.867483
# Unit test for function get_bin_path
def test_get_bin_path():
    path = get_bin_path('/bin/sh')
    assert path == '/bin/sh'

    path = get_bin_path('sh', opt_dirs=['/bin'])
    assert path == '/bin/sh'

    path = get_bin_path('invalid_name', opt_dirs=['/bin'])
    assert path

    try:
        path = get_bin_path('invalid_name')
        assert False
    except ValueError:
        assert True

# Generated at 2022-06-12 23:35:59.422567
# Unit test for function get_bin_path
def test_get_bin_path():
    # NOTE(retr0h): This test is more of a smoke test than a unit test.
    # The function needs to be reworked in order to properly be tested.
    # The function os.path.exists is mocked in the unittest in the test code.
    paths = os.pathsep.join(['/usr/bin', '/bin', '/usr/sbin', '/sbin', '/usr/local/bin'])
    assert get_bin_path("perl", paths.split(os.pathsep)) == '/usr/bin/perl'
    assert get_bin_path("ruby", paths.split(os.pathsep)) == '/usr/bin/ruby'
    assert get_bin_path("python", paths.split(os.pathsep)) == '/usr/bin/python'

# Generated at 2022-06-12 23:36:06.121503
# Unit test for function get_bin_path
def test_get_bin_path():
    import glob
    import tempfile
    import pytest
    tmpdir = tempfile.mkdtemp()

    # Create a dummy command
    test_cmd = 'ansible_test_cmd'
    real_cmd = '/bin/sh'
    file_path = os.path.join(tmpdir, test_cmd)
    with open(file_path, 'w') as f:
        f.write('''#!/bin/sh
echo $@
''')
    perms = os.stat(file_path)
    os.chmod(file_path, 0o700 | perms.st_mode)

    # Find the real command in tmpdir
    cmd_path = get_bin_path(real_cmd, opt_dirs=[tmpdir])

# Generated at 2022-06-12 23:36:14.610985
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test normal usage
    get_bin_path('ls')

    # Test if invalid binary name
    try:
        get_bin_path('asdf')
        assert False
    except ValueError as e:
        assert 'Failed to find required executable' in str(e)

    # Test opt_dirs parameter
    valid_opt_dirs = ['asdf', ['/bin', '/usr/bin'], ('/bin', '/usr/bin')]
    for opt_dirs in valid_opt_dirs:
        get_bin_path('ls', opt_dirs=opt_dirs)

    # Test if file is found in opt_dirs
    assert get_bin_path('ls', opt_dirs=['/bin']) == '/bin/ls'

# Generated at 2022-06-12 23:36:16.579531
# Unit test for function get_bin_path
def test_get_bin_path():
    ''' test get_bin_path() '''
    paths = get_bin_path('/bin/ls')
    assert paths == '/bin/ls'

# Generated at 2022-06-12 23:36:25.373831
# Unit test for function get_bin_path
def test_get_bin_path():

    # Create test directories
    import shutil
    import tempfile
    import filecmp

# Generated at 2022-06-12 23:36:34.012384
# Unit test for function get_bin_path
def test_get_bin_path():
    test_path = '/bin'
    test_arg = 'ls'
    test_notarg = 'ls_not'

    bin_path = get_bin_path(test_arg)
    assert bin_path == '/bin/ls'

    bin_path = get_bin_path(test_arg, opt_dirs=['/sbin'])
    assert bin_path == '/sbin/ls'

    bin_path = get_bin_path(test_arg, opt_dirs=[os.path.join(test_path, '../sbin'), test_path])
    assert bin_path == '/sbin/ls'


# Generated at 2022-06-12 23:36:45.182566
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil

    # Create temporary directory
    tmpdir = tempfile.mkdtemp()

    # Create temporary fake files and directories
    fake_path = os.path.join(tmpdir, 'fake')
    fake_file = os.path.join(tmpdir, 'fake_file')
    fake_symlink = os.path.join(tmpdir, 'fake_symlink')

    open(fake_file, 'a').close()
    os.chmod(fake_file, 0o777)
    os.symlink(fake_file, fake_symlink)

    # Assert ValueError raised if executable not found
    try:
        get_bin_path(fake_path)
    except ValueError:
        pass
    else:
        assert False

    # Assert ValueError raised if executable

# Generated at 2022-06-12 23:36:53.287602
# Unit test for function get_bin_path
def test_get_bin_path():
    import sys
    import pwd
    ansible_user = pwd.getpwuid(os.getuid()).pw_name
    bin_name = 'python'
    if sys.platform == 'win32':
        bin_name = 'python.exe'
    # get_bin_path return full path - executable name
    bin_path = get_bin_path(bin_name)
    assert bin_path is not None
    assert os.path.isfile(bin_path)
    assert bin_name in bin_path
    # get_bin_path raises Exception if executable is not found
    try:
        get_bin_path('not_known_bin_name')
    except Exception:
        assert True
    else:
        assert False

# Generated at 2022-06-12 23:37:05.603726
# Unit test for function get_bin_path
def test_get_bin_path():
    import mock
    import sys

    # Find the current Python executable
    python_interpreter = sys.executable

    # Test that the get_bin_path returns the interpreter
    with mock.patch.dict(os.environ, {'PATH': os.path.dirname(python_interpreter)}):
        assert get_bin_path(os.path.basename(python_interpreter)) == python_interpreter

    # Test that the get_bin_path returns the interpreter
    # when searching in the script directory
    with mock.patch.dict(os.environ, {'PATH': os.path.dirname(python_interpreter)}, clear=True):
        assert get_bin_path(os.path.basename(python_interpreter), opt_dirs=[os.getcwd()]) == python_interpre

# Generated at 2022-06-12 23:37:20.468124
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('python2') == get_bin_path('python2', ['/usr/bin'])
    assert get_bin_path('python2', ['/bin', '/usr/bin']) == '/usr/bin/python2'
    try:
        get_bin_path('python2', ['/bin', '/usr/bin'], required=True)
        assert False, "Wrong bin path not detected"
    except ValueError:
        pass

    bin_path = get_bin_path('python2', ['/bin', '/usr/bin', '/bin/python2'])
    assert bin_path == '/bin/python2'

# Generated at 2022-06-12 23:37:25.232358
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test invalid binary
    try:
        get_bin_path('this-is-not-a-valid-binary')
        assert(False)
    except ValueError:
        assert(True)

    # Test valid binary
    try:
        path = get_bin_path('sh')
        assert('sh' in path)
        assert(path.startswith('/'))
    except (ValueError, AssertionError):
        assert(False)

# Generated at 2022-06-12 23:37:36.868420
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil

    def create_temp_exec(name):
        temp_exec_path = os.path.join(temp_dir, name)
        open(temp_exec_path, 'w').close()
        os.chmod(temp_exec_path, 0o755)
        return temp_exec_path

    temp_dir = tempfile.mkdtemp()