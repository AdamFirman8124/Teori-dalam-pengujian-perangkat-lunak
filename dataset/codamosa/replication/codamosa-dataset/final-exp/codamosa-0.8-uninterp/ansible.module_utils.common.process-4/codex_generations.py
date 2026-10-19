

# Generated at 2022-06-12 23:27:49.699162
# Unit test for function get_bin_path
def test_get_bin_path():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils._text import to_bytes
    from tempfile import mkdtemp
    import shutil

    def get_bin_path_bin(s):
        return get_bin_path(s)

    def get_bin_path_bin_optdirs(s, opt_dirs):
        return get_bin_path(s, opt_dirs=opt_dirs)

    def get_bin_path_bin_optdirs_required(s, opt_dirs, required):
        return get_bin_path(s, opt_dirs=opt_dirs, required=required)

    def write_binary(binary_path, data):
        f = open(binary_path, 'wb')

# Generated at 2022-06-12 23:27:51.807276
# Unit test for function get_bin_path
def test_get_bin_path():
    bin_path = get_bin_path("cat")
    assert os.path.basename(bin_path) == 'cat'

# Generated at 2022-06-12 23:27:59.216038
# Unit test for function get_bin_path
def test_get_bin_path():
    bin_path = get_bin_path('/bin/echo')
    assert bin_path == '/bin/echo'

    try:
        get_bin_path('/nonexistent/echo')
        assert False, 'Absent file path should raise exception'
    except Exception as exc:
        assert 'Failed to find required executable' in str(exc), 'Unexpected error message: %s' % str(exc)

    try:
        get_bin_path('/nonexistent/echo')
    except:
        # Ensure exception has already been raised even if second time
        try:
            get_bin_path('/nonexistent/echo')
            assert False, 'Absent file path should raise exception'
        except Exception as exc:
            assert 'Failed to find required executable' in str(exc), 'Unexpected error message: %s'

# Generated at 2022-06-12 23:28:02.487315
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Test get_bin_path function in ansible.module_utils.six.moves.shutil_get_terminal_size
    '''
    assert get_bin_path('ls') is not None
    try:
        get_bin_path('notexists', required=True)
    except ValueError as e:
        pass
    assert(True)

# Generated at 2022-06-12 23:28:07.423428
# Unit test for function get_bin_path
def test_get_bin_path():
    # Ansible-provided basepath
    bin_path = get_bin_path('cat')

    if os.path.isabs(bin_path):
        assert os.path.exists(bin_path)
        assert not os.path.isdir(bin_path)
        assert is_executable(bin_path)

# Generated at 2022-06-12 23:28:17.929917
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Setup for testing the get_bin_path function
    '''
    
    get_bin_path("/sbin/ip") # => /sbin/ip 
    get_bin_path("/bin/ip") # => /bin/ip
    get_bin_path("/usr/bin/ip") # => /usr/bin/ip
    get_bin_path("/usr/sbin/ip") # => /usr/sbin/ip
    get_bin_path("/usr/local/bin/ip") # => /usr/local/bin/ip
    get_bin_path("/usr/local/sbin/ip") # => /usr/local/sbin/ip
    get_bin_path("/usr/local/bin/nginx") # => /usr/local/bin/nginx
    get_

# Generated at 2022-06-12 23:28:26.444631
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Test to see if the get_bin_path function works as intended
    '''
    # The result should be the absolute path to a given binary
    assert get_bin_path('python') == '/usr/bin/python'

    # The result should be the absolute path to the given binary
    assert get_bin_path('python', required=False) == '/usr/bin/python'

    # We ask for python, but there is no python binary in the path.
    # Should raise an error
    try:
        get_bin_path('notpython')
    except ValueError:
        assert True
    else:
        assert False

    # We ask for python, but there is no python binary in the path.
    # We pass required=False, it should not raise an error but return None

# Generated at 2022-06-12 23:28:32.878083
# Unit test for function get_bin_path
def test_get_bin_path():
    import sys
    import tempfile
    import textwrap

    # create dummy executable
    with tempfile.NamedTemporaryFile() as f:
        script = textwrap.dedent('''#!/usr/bin/env python
if __name__ == '__main__':
    import sys
    sys.exit(0)
''')
        f.write(script)
        f.flush()

# Generated at 2022-06-12 23:28:38.021877
# Unit test for function get_bin_path
def test_get_bin_path():
    '''Test that get_bin_path returns the correct path'''
    test_good = '/bin/ls'
    test_bad = 'bad_executable_name'

    assert get_bin_path('ls') == test_good
    try:
        get_bin_path(test_bad)
    except ValueError as e:
        pass
    else:
        fail('get_bin_path() should raise an error when executable not found')

# Generated at 2022-06-12 23:28:44.766312
# Unit test for function get_bin_path
def test_get_bin_path():
    # check that get_bin_path raises ValueError if binary not found
    try:
        get_bin_path('no-such-binary')
    except ValueError:
        pass
    else:
        raise AssertionError('get_bin_path should have raised ValueError')

    # check that get_bin_path finds a binary using PATH
    assert get_bin_path('sh') == '/bin/sh'

# Generated at 2022-06-12 23:28:52.735221
# Unit test for function get_bin_path
def test_get_bin_path():
    # Set 'PATH' environment value
    os.environ['PATH'] = os.pathsep.join(['/not/in/path', '/bin', '/usr/bin'])

    # Test for expected return values
    try:
        assert get_bin_path('sh') == '/bin/sh'
        assert get_bin_path('find') == '/usr/bin/find'
        assert get_bin_path('/usr/bin/find') == '/usr/bin/find'
    except ValueError:
        assert False
    try:
        get_bin_path('/not/found/arg')
    except ValueError:
        assert True
    else:
        assert False

    # Test with optional argument opt_dirs
    opt_dirs = ['/usr/local/bin', '/usr/local/sbin']

# Generated at 2022-06-12 23:28:56.330888
# Unit test for function get_bin_path
def test_get_bin_path():
    # we have a good chance of finding "ls" executable
    assert(get_bin_path('/bin/ls') == '/bin/ls')
    assert(get_bin_path('/bin/doesnotexist') == None)

# Generated at 2022-06-12 23:29:04.428963
# Unit test for function get_bin_path
def test_get_bin_path():
    bin_path = get_bin_path('python', ['/usr/local/bin'])
    assert '/usr/local/bin/python' == bin_path
    bin_path = get_bin_path('python', ['/usr/local/bin', '/usr/bin/python'])
    assert '/usr/bin/python' == bin_path
    bin_path = get_bin_path('python', ['/usr/local/bin2'])
    assert '/usr/bin/python' == bin_path

    try:
        get_bin_path('python22', [])
        assert False
    except ValueError:
        pass

# Generated at 2022-06-12 23:29:12.538759
# Unit test for function get_bin_path
def test_get_bin_path():
    import mock
    import tempfile

    with mock.patch('os.environ.get') as environ:
        environ.return_value = '/bin:/usr/bin:/usr/local/bin'
        # Testing the case when the path is not in PATH
        with mock.patch('os.path.exists') as exists:
            exists.return_value = False
            with mock.patch('os.path.isdir') as isdir:
                isdir.return_value = True
                # Test the case when the path is a directory
                with mock.patch('ansible.module_utils.common.file.is_executable') as is_executable:
                    import pytest
                    with pytest.raises(ValueError):
                        get_bin_path('foo')
                isdir.return_value = False

# Generated at 2022-06-12 23:29:13.841435
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('tar') == '/bin/tar'

# Generated at 2022-06-12 23:29:22.128313
# Unit test for function get_bin_path
def test_get_bin_path():
    '''Ensure that we find binaries in PATH ignoring case'''
    
    assert get_bin_path('tar') == '/bin/tar'
    assert get_bin_path('Tar') == '/bin/tar'
    assert get_bin_path('TAR') == '/bin/tar'

    try:
        get_bin_path('chmod') == '/bin/chmod'
    except ValueError as e:
        assert False, "Unexpected error: %s" % str(e)

    try:
        get_bin_path('CHMOD')
        assert False, "No ValueError exception on unknown binary"
    except ValueError:
        pass

    # make sure we find the binary in opt_dirs
    assert get_bin_path('tar', opt_dirs=[]) == '/bin/tar'
    assert get_bin_

# Generated at 2022-06-12 23:29:29.084394
# Unit test for function get_bin_path
def test_get_bin_path():
    import pytest
    with pytest.raises(ValueError) as excinfo:
        get_bin_path("this_command_does_not_exist")
    assert "Failed to find required executable" in str(excinfo.value)
    with pytest.raises(ValueError) as excinfo:
        get_bin_path("this_command_does_not_exist", ["/tmp"])
    assert "Failed to find required executable" in str(excinfo.value)

# Generated at 2022-06-12 23:29:40.026695
# Unit test for function get_bin_path
def test_get_bin_path():
    from ansible.module_utils._text import to_bytes

    assert os.path.exists(get_bin_path('sh'))
    assert os.path.exists(get_bin_path('/bin/sh'))
    assert os.path.exists(get_bin_path('/sbin/service', ['/usr/local/sbin']))

    # Test that we are not passing paths through to_bytes
    get_bin_path('/bin/sh')
    assert to_bytes('/bin/sh') == b'/bin/sh'

    try:
        get_bin_path('/no/such/command', required=False)
        assert False
    except ValueError:
        pass
    # From Ansible 2.10, required is always assumed to be True

# Generated at 2022-06-12 23:29:46.940426
# Unit test for function get_bin_path
def test_get_bin_path():
    # On some systems /sbin is not present and /usr/sbin is only in PATH for root, so try to find a program expected to be in /usr/sbin
    try:
        get_bin_path('python')
    except:
        get_bin_path('python', opt_dirs=['/usr/local/sbin'])
    # If a command is not found, it should raise an exception
    try:
        get_bin_path('nonexistentcommand')
        raise Exception("expected exception not raised")
    except Exception:
        pass

# Generated at 2022-06-12 23:29:56.104090
# Unit test for function get_bin_path
def test_get_bin_path():
    # windows path
    assert get_bin_path('abcd') == 'abcd'

    os.environ['PATH'] = '/bin:/usr/bin:/usr/local/bin'
    os.environ['PATHEXT'] = '.EXE'

    assert get_bin_path('ps') == '/bin/ps'
    assert get_bin_path('passwd') == '/usr/bin/passwd'
    assert get_bin_path('ls') == '/bin/ls'
    assert get_bin_path('chown') == '/bin/chown'

    # no longer fails since we have /usr/local/bin in the path
    assert get_bin_path('brew') == '/usr/local/bin/brew'

    os.environ['PATH'] = '/usr/local/bin:/bin:/usr/bin'
    assert get

# Generated at 2022-06-12 23:30:09.974930
# Unit test for function get_bin_path
def test_get_bin_path():
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils import get_bin_path
    from .get_bin_path import unittest_helper_fixture_true_file as fixture
    from .get_bin_path import unittest_helper_fixture_false_file as fixture_inaccessible

    # Test for correct return when file exists.
    assert get_bin_path(fixture('file1')) == fixture('file1')

    # Test for exception when file does not exist.
    with pytest.raises(ValueError):
        get_bin_path(fixture('file_not_exist'))

    # Test for exception when file exists but is inaccessible.

# Generated at 2022-06-12 23:30:21.300143
# Unit test for function get_bin_path
def test_get_bin_path():

    # Create a fake executable in $PWD/fake_bin
    fake_bin = os.path.join(os.environ.get('PWD'), 'fake_bin')
    try:
        os.makedirs(fake_bin)
    except OSError:
        # Directory already exists
        pass
    os.chmod(fake_bin, 0o755)
    bin_name = 'ansible-test-bin'
    with open(os.path.join(fake_bin, bin_name), 'w') as f:
        f.write('#! /bin/sh\n\necho fake bin')
    os.chmod(os.path.join(fake_bin, bin_name), 0o755)


# Generated at 2022-06-12 23:30:30.732480
# Unit test for function get_bin_path
def test_get_bin_path():
    """
    Tests function as called by other modules
    :return:
    """
    # Normal use case
    assert get_bin_path('ping') is not None

    # Not in path
    try:
        get_bin_path('no_such_bin_in_path')
    except ValueError as e:
        assert 'Failed to find required executable "no_such_bin_in_path" in paths:' in str(e)

    # Normal use case with optional directories
    assert get_bin_path('ping', opt_dirs=['/sbin', '/usr/sbin']) is not None

    # Optional directory that does not exist

# Generated at 2022-06-12 23:30:40.243088
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('ls', required=False) == '/bin/ls'
    assert get_bin_path('grep', opt_dirs=['/usr/bin/'], required=False) == '/usr/bin/grep'
    try:
        get_bin_path('missing', opt_dirs=['/usr/bin/'], required=True)
        assert False, 'expected exception ValueError for missing'
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "missing" in paths: /usr/bin/:/bin:/usr/bin'
    assert get_bin_path('ls', required=True) == '/bin/ls'

# Generated at 2022-06-12 23:30:42.425032
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('ls') == '/bin/ls'
    assert get_bin_path('this-executable-should-not-exist') == None

# Generated at 2022-06-12 23:30:54.741127
# Unit test for function get_bin_path
def test_get_bin_path():
    from shutil import rmtree
    from tempfile import mkdtemp
    import sys

    # Verify global path
    if sys.executable is None:
        assert get_bin_path('sh') in os.environ.get('PATH', '').split(os.pathsep)
    else:
        assert get_bin_path(sys.executable) in os.environ.get('PATH', '').split(os.pathsep)

    # Test with additional search paths
    path_dir = mkdtemp(prefix='ansible_path_')
    os.mkdir(os.path.join(path_dir, 'bin'))
    new_path = os.path.join(path_dir, 'bin', 'sh')
    open(new_path, 'w').close()

# Generated at 2022-06-12 23:30:55.709057
# Unit test for function get_bin_path
def test_get_bin_path():
    get_bin_path('/bin/ls')

# Generated at 2022-06-12 23:31:03.022627
# Unit test for function get_bin_path
def test_get_bin_path():
    import types
    from mock import patch

    test_func = types.FunctionType(get_bin_path.__code__, {})
    for i in range(0, 11):
        bin_path = test_func('/bin/ls', ['/sbin', '/usr/sbin'], required=False)
        assert bin_path == '/bin/ls'

    with patch.object(os, 'environ', {}):
        with patch.object(os, 'path', spec=True):
            os.path.exists = lambda name: True
            os.path.isdir = lambda name: False
            with patch.object(os, 'access', lambda name, mode: True):
                bin_path = test_func('/bin/ls', ['/sbin', '/usr/sbin'], required=False)
                assert bin_path

# Generated at 2022-06-12 23:31:05.906493
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('python2.7', required=False) == '/usr/bin/python2.7'

# Generated at 2022-06-12 23:31:09.976224
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('ls')
    assert get_bin_path('ls', '/bin')
    assert get_bin_path('ls', opt_dirs=['/bin'])
    assert get_bin_path('ls', opt_dirs=['/bin', '/usr/bin'])

# Generated at 2022-06-12 23:31:17.672021
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        which_bin = get_bin_path('which')
    except ValueError as e:
        assert False, 'get_bin_path is broken: %s' % to_text(e)
    try:
        get_bin_path('nonexisting_which_bin_should_never_ever_exist_in_the_known_universe')
        assert False, 'get_bin_path failed to raise error when it should'
    except ValueError as e:
        assert True

# Generated at 2022-06-12 23:31:20.710350
# Unit test for function get_bin_path
def test_get_bin_path():
    bin_path = get_bin_path('sh')
    assert bin_path == "/bin/sh"
    try:
        bin_path = get_bin_path('not-an-executable')
    except ValueError as e:
        assert 'Failed to find required executable' in str(e)



# Generated at 2022-06-12 23:31:25.586141
# Unit test for function get_bin_path
def test_get_bin_path():
    bin_name = 'ansible-test-bin'
    # Create a temporary binary file
    tmpbin_path = os.path.join('/tmp', bin_name)
    os.mknod(tmpbin_path, 0o775)

    # Check if it can be found using get_bin_path
    bin_path = get_bin_path(bin_name)
    assert bin_path == tmpbin_path

    # Check if it cannot be found if not in path
    os.unlink(tmpbin_path)
    try:
        get_bin_path(bin_name)
    except ValueError:
        pass

# Generated at 2022-06-12 23:31:35.029050
# Unit test for function get_bin_path
def test_get_bin_path():
    # PATH contains "/usr/bin"
    assert get_bin_path('ls') == '/usr/bin/ls'
    # PATH contains "/usr/bin" and "/usr/sbin"
    assert get_bin_path('ifconfig') == '/usr/sbin/ifconfig'
    # PATH contains "/usr/bin" and opt_dirs contains "/usr/sbin"
    # Verify that the optional dir takes precedence
    assert get_bin_path('ifconfig', opt_dirs=['/usr/sbin']) == '/usr/sbin/ifconfig'
    # PATH contains "/usr/bin" and opt_dirs contains "/usr/local/sbin"
    # Verify that the optional dir takes precedence

# Generated at 2022-06-12 23:31:46.012111
# Unit test for function get_bin_path
def test_get_bin_path():
    executable = os.path.basename(__file__)
    libdir = os.path.dirname(__file__)

    # Executable in local directory, no search path specified
    assert get_bin_path(executable) == __file__
    # Executable in local directory, empty search path specified
    assert get_bin_path(executable, []) == __file__
    # Executable in local directory, local directory in search path specified
    assert get_bin_path(executable, [libdir]) == __file__
    # Executable in PATH, no search path specified.
    assert get_bin_path(os.path.basename(os.path.dirname(__file__))) == os.path.dirname(__file__)
    # Executable not in search path specified.
    import tempfile
    tmpdir = os

# Generated at 2022-06-12 23:31:52.953982
# Unit test for function get_bin_path
def test_get_bin_path():
    # Call get_bin_path multiple times using different arguments, ensure proper handling
    assert get_bin_path('id')
    assert get_bin_path('id', ['/bin'])
    assert get_bin_path('id', ['/bin', '/usr/bin'])
    # Check failure modes
    try:
        get_bin_path('not_exe_bin')
        assert False, 'Failed to raise ValueError for non-existing binary'
    except ValueError:
        pass

    try:
        get_bin_path('test/test_module.py')
        assert False, 'Failed to raise ValueError for non-executable'
    except ValueError:
        pass


# Generated at 2022-06-12 23:31:57.083753
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path(arg='ls') is not None
    try:
        get_bin_path(arg='lsdfdfgdg')
    except:
        pass
    else:
        assert False, "Should throw an exception if the program doesn't exist"

# Generated at 2022-06-12 23:32:02.643452
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test to check if the function raises an exception if the executable is
    # not found
    try:
        test_exec = 'executablenotfound'
        get_bin_path(test_exec)
    except ValueError as e:
        result = 'Failed to find required executable "%s"' % test_exec
        assert result in str(e)

    # Test to check if the function returns a value for a valid executable
    test_exec = 'ls'
    result = get_bin_path(test_exec)
    assert type(result) is str

# Generated at 2022-06-12 23:32:13.517962
# Unit test for function get_bin_path
def test_get_bin_path():
    import sys
    import tempfile
    tmp_path = tempfile.gettempdir()

    # Create a couple of temporary files to test with
    test_files = []
    for x in range(0, 2):
        (fd, fn) = tempfile.mkstemp(dir=tmp_path)
        os.close(fd)
        test_files.append(fn)

    # Replace PATH in environment
    orig_path = os.environ.get('PATH', None)
    os.environ['PATH'] = tmp_path

    # Test that we can find a good file in PATH
    bin_path = get_bin_path(os.path.basename(test_files[0]))
    assert bin_path == test_files[0]

    # Test that we get an exception for a bad file

# Generated at 2022-06-12 23:32:15.173394
# Unit test for function get_bin_path
def test_get_bin_path():
    if get_bin_path('which') is None:
        raise Exception('Failed to find required \'which\' executable in path.')

# Generated at 2022-06-12 23:32:26.939765
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path('nonsense')
        assert False
    except ValueError:
        assert True
    try:
        get_bin_path('nonsense', ['/opt/bin'])
        assert False
    except ValueError:
        assert True
    try:
        get_bin_path('nonsense', ['/opt/bin'], required=True)
        assert False
    except ValueError:
        assert True
    try:
        get_bin_path('ls')
        assert True
    except ValueError:
        assert False
    try:
        get_bin_path('ls', ['/bin'])
        assert True
    except ValueError:
        assert False

# Generated at 2022-06-12 23:32:38.855315
# Unit test for function get_bin_path
def test_get_bin_path():
    import os
    import io
    import sys
    import shutil
    from tempfile import gettempdir
    from functools import wraps

    def make_script(func):
        @wraps(func)
        def script_file():
            fd, fname = tempfile.mkstemp(text=True)
            os.write(fd, '#!/bin/sh\n')
            os.write(fd, 'echo "Running {} with args: $@"\n'.format(func.__name__))
            os.write(fd, '{} $@'.format(func))
            os.close(fd)
            os.chmod(fname, 0o755)
            return fname
        return script_file

    def get_bin_path_test(script_file, *args, **kwargs):
        std

# Generated at 2022-06-12 23:32:48.161609
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path('notexistingfile')
        assert False
    except ValueError as e:
        assert 'Failed to find required executable' in str(e)
    try:
        get_bin_path('notexistingfile', ['/usr/bin'])
        assert False
    except ValueError as e:
        assert 'Failed to find required executable' in str(e)
    assert get_bin_path('sh', ['/usr/bin']) == '/usr/bin/sh'
    assert get_bin_path('sh', ['/usr/bin']) != '/bin/sh'

# Generated at 2022-06-12 23:32:58.244972
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Basic setup to run test
    '''
    import sys
    import os
    import subprocess
    if not os.access("/bin/date", os.X_OK):
        sys.exit("Cannot execute /bin/date")

    date_out = subprocess.Popen(["/bin/date"], stdout=subprocess.PIPE).communicate()[0]
    assert date_out

    date_bin_path = get_bin_path('date')
    assert date_bin_path == "/bin/date"

    date_out = subprocess.Popen([date_bin_path], stdout=subprocess.PIPE).communicate()[0]
    assert date_out

# Generated at 2022-06-12 23:33:03.029058
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('bash') == get_bin_path('/bin/bash')
    assert get_bin_path('bash', ['/bin']) == get_bin_path('/bin/bash')
    assert get_bin_path('bash', ['/usr/bin']) == get_bin_path('/usr/bin/bash')
    assert get_bin_path('bash', ['/usr/bin', '/bin']) == get_bin_path('/usr/bin/bash')
    assert get_bin_path('bash', ['/bin', '/usr/bin']) == get_bin_path('/bin/bash')
    assert get_bin_path('bash', ['/usr/bin', '/bin', '/usr/sbin']) == get_bin_path('/usr/bin/bash')
    assert get_bin_path

# Generated at 2022-06-12 23:33:06.662407
# Unit test for function get_bin_path
def test_get_bin_path():
    import os.path
    assert get_bin_path('ansible') == os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'bin', 'ansible')



# Generated at 2022-06-12 23:33:12.805787
# Unit test for function get_bin_path
def test_get_bin_path():
    # Defining paths for tests
    bin_paths = ['/bin', '/usr/bin', '/usr/local/bin']
    sbin_paths = ['/sbin', '/usr/sbin', '/usr/local/sbin']
    paths = []
    paths += bin_paths
    paths += sbin_paths
    # Testing if get_bin_path can find known locations in path
    for p in paths:
        assert get_bin_path('ls', [p]) == os.path.join(p, 'ls') == os.path.join(p, 'ls')

# Generated at 2022-06-12 23:33:23.721334
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile

    tf1 = tempfile.NamedTemporaryFile(mode='w', delete=False)
    tf1.write('#!/bin/sh\n\necho hello')
    tf1.close()

    tf2 = tempfile.NamedTemporaryFile(mode='w', delete=False)
    tf2.write('#!/bin/bash\n\necho hello')
    tf2.close()

    # bin should be found
    assert get_bin_path(os.path.basename(tf1.name)) == tf1.name
    assert get_bin_path(os.path.basename(tf2.name)) == tf2.name

    # bin should not be found
    try:
        get_bin_path('not_a_bin')
        assert False
    except ValueError:
        assert True

# Generated at 2022-06-12 23:33:32.326670
# Unit test for function get_bin_path
def test_get_bin_path():
    current_dir = os.path.dirname(__file__)
    test_path = os.path.join(current_dir, '../test/utils/test_executables/')


# Generated at 2022-06-12 23:33:44.171560
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test with file in PATH
    try:
        get_bin_path('sh')
    except Exception as e:
        assert False, "Unexpected exception raised: " + str(e)

    # Test with file not in PATH
    try:
        get_bin_path('foo')
    except Exception as e:
        assert type(e) == ValueError, "Exception type not ValueError: " + str(e)

    # Test with optional directories specified
    try:
        get_bin_path('sh', ['/sbin'])
    except Exception as e:
        assert False, "Unexpected exception raised: " + str(e)

    # Test including /sbin/ directories

# Generated at 2022-06-12 23:33:59.665525
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Test get_bin_path
    '''
    # Path to empty dir
    path = '/path/to/empty/dir'
    # Test with empty dir
    test_path = get_bin_path('ls', opt_dirs=[path])
    assert test_path is not None and '/bin/ls' in test_path
    # Test with dir that does not exist
    test_path = get_bin_path('ls', opt_dirs=['/path/to/no/dir'])
    assert test_path is not None and '/bin/ls' in test_path
    # Test with dir that exists with no ls
    test_path = get_bin_path('ls', opt_dirs=[path])
    assert test_path is not None and '/bin/ls' in test_path
    # Test with dir that

# Generated at 2022-06-12 23:34:00.612165
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('which')

# Generated at 2022-06-12 23:34:08.436109
# Unit test for function get_bin_path
def test_get_bin_path():
    bin_path = get_bin_path('cat')
    if os.path.splitext(bin_path)[1] == '.py':
        bin_path = get_bin_path('python')
    assert os.path.isfile(bin_path)
    assert os.access(bin_path, os.X_OK)

    bin_path = get_bin_path('cat', required=True)
    if os.path.splitext(bin_path)[1] == '.py':
        bin_path = get_bin_path('python')
    assert os.path.isfile(bin_path)
    assert os.access(bin_path, os.X_OK)

# Generated at 2022-06-12 23:34:10.437378
# Unit test for function get_bin_path
def test_get_bin_path():
    bin_path = get_bin_path('sh')
    assert os.access(bin_path, os.X_OK)


# Generated at 2022-06-12 23:34:13.617695
# Unit test for function get_bin_path
def test_get_bin_path():
    from nose.plugins.skip import SkipTest

    if not is_executable('/bin/ls'):
        raise SkipTest('skipped, cannot invoke /bin/ls')

    assert get_bin_path('ls') == '/bin/ls'

# Generated at 2022-06-12 23:34:16.332352
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('sh') is not None
    import errno
    try:
        get_bin_path('does_not_exist')
    except ValueError as e:
        # If a value error is raised during unit testing,
        # print a better error message than a stack trace
        print(errno.EINVAL, e.args)
        assert errno.EINVAL in e.args
    else:
        assert False

# Generated at 2022-06-12 23:34:24.176019
# Unit test for function get_bin_path
def test_get_bin_path():
    # Successful run
    assert get_bin_path("date") is not None

    # Failure - command doesn't exist
    try:
        get_bin_path("doesnotexist")
        assert False
    except ValueError:
        assert True

    # Failure - command exists, but is not executable
    try:
        get_bin_path("/dev/null")
        assert False
    except ValueError:
        assert True

    # Successful run - command exists
    assert get_bin_path("/sbin/ifconfig") is not None

# Generated at 2022-06-12 23:34:32.165679
# Unit test for function get_bin_path
def test_get_bin_path():
    import stat
    import tempfile
    import shutil
    import subprocess
    import pytest

    tmpdir = tempfile.mkdtemp()

# Generated at 2022-06-12 23:34:33.543830
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('which') == '/usr/bin/which'

# Generated at 2022-06-12 23:34:37.805237
# Unit test for function get_bin_path
def test_get_bin_path():
    # test executable in /bin dir
    assert get_bin_path('hostname') == '/bin/hostname'
    # test executable in /sbin dir
    assert get_bin_path('pvcreate') == '/sbin/pvcreate'


# Generated at 2022-06-12 23:34:52.401836
# Unit test for function get_bin_path
def test_get_bin_path():
    opt_dirs = ['/opt/bin', '/opt/sbin']

    # (arg, opt_dirs, required)

# Generated at 2022-06-12 23:35:00.464131
# Unit test for function get_bin_path
def test_get_bin_path():
    # test if existing binary is found
    assert get_bin_path('ls')
    assert get_bin_path('ls', None, None)
    assert get_bin_path('ls', ['/bin'], None)

    # test if existing binary is found in supplied path
    assert get_bin_path('ls', ['/bin', '/usr/bin'])

    # test if non-existing binary returns expected error
    try:
        get_bin_path('thisisnotavalidprogram')
        assert False, 'Did not raise ValueError for a missing executable'
    except ValueError as e:
        assert 'Failed to find required executable' in str(e)

    # test if binary path is found in /sbin, /usr/sbin, /usr/local/sbin
    # which are not typically in PATH, but are needed for programs like

# Generated at 2022-06-12 23:35:09.238535
# Unit test for function get_bin_path
def test_get_bin_path():

    import sys
    import shutil
    import tempfile

    test_dir = tempfile.mkdtemp()

    try:
        # Install a simple executable to test with
        fn = os.path.join(test_dir, 'foobar')
        open(fn, 'w').close()
        os.chmod(fn, 0o755)

        pathval = os.environ.get('PATH', '')

        os.environ['PATH'] = test_dir
        assert get_bin_path('foobar') == fn

        os.environ['PATH'] = ''
        get_bin_path('foobar', required=False)
        assert False, "get_bin_path should always raise ValueError when executable not found"
    except ValueError:
        pass
        # cleanup
    os.environ['PATH'] = pathval
   

# Generated at 2022-06-12 23:35:17.719478
# Unit test for function get_bin_path
def test_get_bin_path():
    # test to make sure it finds itself and not something else
    bin_path = get_bin_path('get_bin_path.py', opt_dirs=[os.path.dirname(__file__)])
    assert os.path.realpath(bin_path) == os.path.realpath(__file__)
    # test to make sure it finds the correct script
    bin_path = get_bin_path('setup.py', opt_dirs=[os.path.dirname(__file__)])
    assert os.path.basename(bin_path) == 'setup.py'

# Generated at 2022-06-12 23:35:28.043539
# Unit test for function get_bin_path
def test_get_bin_path():
    import sys
    if sys.version_info[0] >= 3:
        from unittest.mock import patch
    else:
        from mock import patch

    from ansible.module_utils import basic
    import ansible.module_utils.common.file

    class TestAnsibleModule(basic.AnsibleModule):
        def __init__(self, *args, **kwargs):
            super(TestAnsibleModule, self).__init__(*args, **kwargs)

    def fake_is_executable(path):
        if os.path.basename(path) == 'gzip':
            return True
        else:
            return False

    bin_path = None
    # get_bin_path doesn't require PATH to exist

# Generated at 2022-06-12 23:35:30.807329
# Unit test for function get_bin_path
def test_get_bin_path():
    expected_bin_path = '/bin/true'
    assert get_bin_path('true') == expected_bin_path

# Generated at 2022-06-12 23:35:37.731461
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Unit test for function get_bin_path
    '''
    assert get_bin_path('sh') == '/bin/sh'
    assert get_bin_path('ansible-default-roles') != '/usr/bin/ansible-default-roles'
    # test exception thrown
    try:
        get_bin_path('ansible-default-roles')
    except Exception:
        pass
    else:
        assert 0

# Generated at 2022-06-12 23:35:43.612799
# Unit test for function get_bin_path
def test_get_bin_path():
    os.environ['PATH'] = '/usr/sbin:/usr/bin:/sbin:/bin'
    found_bin = get_bin_path('ls')
    assert found_bin == '/bin/ls'
    try:
        get_bin_path('ls', opt_dirs=['/usr/local/bin'])
    except Exception:
        pass
    else:
        assert False, 'Expected exception found!'

# Generated at 2022-06-12 23:35:47.873904
# Unit test for function get_bin_path
def test_get_bin_path():
    path = get_bin_path('python')
    assert path == '/usr/bin/python'

    path = get_bin_path('python', ['/tmp'])
    assert path == '/tmp/python'

    try:
        path = get_bin_path('nonexistantbinary')
        assert False, "Should have raised exception"
    except ValueError:
        pass

# Generated at 2022-06-12 23:36:00.193525
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('cp') == '/bin/cp'
    try:
        get_bin_path('random_file')
        assert False, 'Should have raised an exception'
    except ValueError:
        pass

    # With sbin dirs
    assert get_bin_path('ip') == '/sbin/ip'
    try:
        get_bin_path('random_file')
        assert False, 'Should have raised an exception'
    except ValueError:
        pass

    # With optional dirs
    assert get_bin_path('ip', opt_dirs=['/sbin']) == '/sbin/ip'
    try:
        get_bin_path('ip', opt_dirs=['/sbin'])
        assert False, 'Should have raised an exception'
    except ValueError:
        pass



# Generated at 2022-06-12 23:36:18.529631
# Unit test for function get_bin_path
def test_get_bin_path():
    # Not executable, returns None
    assert get_bin_path('/tmp') is None
    assert get_bin_path('/tmp/foo') is None
    assert get_bin_path('/tmp/foo/bar') is None

    # Exists and executable, returns full path
    bin_path = '/bin/ls'
    assert get_bin_path('/bin/ls') == bin_path
    assert get_bin_path('/bin/ls', opt_dirs=['/bin']) == bin_path

    # The executable is not in PATH, returns None
    assert get_bin_path('ls') is None

    # The executable is available in PATH
    assert get_bin_path('ls', opt_dirs=['/bin']) == bin_path

# Generated at 2022-06-12 23:36:26.850352
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('cat') == '/bin/cat'
    assert get_bin_path('cat', opt_dirs=['/usr/bin']) == '/usr/bin/cat'
    assert get_bin_path('cat', opt_dirs=['/usr/bin', '/bin']) == '/bin/cat'
    try:
        get_bin_path('cat', opt_dirs=['/usr/bin', '/usr/sbin'])
    except ValueError:
        assert True
    else:
        assert False

    try:
        get_bin_path('cat', opt_dirs=['/usr/bin', '/usr/sbin'], required=True)
    except ValueError:
        assert True
    else:
        assert False

    # /sbin dirs should be in path

# Generated at 2022-06-12 23:36:34.867268
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Unit test for get_bin_path
    '''
    # Function get_bin_path can be tested with coreutils shuf program.
    # It exists in Fedora and Ubuntu, so it is a good choice for test.
    # If shuf is not installed, then we skip the test.
    try:
        get_bin_path('shuf')
    except ValueError:
        return
    assert(get_bin_path('shuf') == get_bin_path('shuf'))
    assert(get_bin_path(' shuf') == get_bin_path('shuf ', opt_dirs=[]))

# Generated at 2022-06-12 23:36:45.685122
# Unit test for function get_bin_path
def test_get_bin_path():
    # We can't rely on PATH being set
    if 'PATH' not in os.environ:
        os.environ['PATH'] = "/usr/bin:/usr/sbin:/bin:/sbin"

    assert get_bin_path('ls') == '/bin/ls'
    assert get_bin_path('/bin/ls') == '/bin/ls'
    assert get_bin_path('/usr/bin/ls') == '/usr/bin/ls'
    assert get_bin_path('ls', opt_dirs=['/bin', '/sbin']) == '/bin/ls'
    assert get_bin_path('ls', opt_dirs=['/sbin', '/bin']) == '/sbin/ls'

# Generated at 2022-06-12 23:36:53.626886
# Unit test for function get_bin_path
def test_get_bin_path():
    # Verifies that function raises exception if executable is not found in PATH
    try:
        get_bin_path("foo_executable")
        assert False
    except ValueError:
        assert True

    # Verifies that function looks for executable in /sbin directory and /usr/sbin directories.
    # These directories are added to PATH
    bin_path = get_bin_path("true")
    assert bin_path == "/sbin/true" or bin_path == "/usr/sbin/true" or bin_path == "/usr/bin/true" or bin_path == "/bin/true"
    assert is_executable(bin_path)

    bin_path = get_bin_path("false")

# Generated at 2022-06-12 23:37:06.004341
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil
    import stat

    example_executables = {'foo': 'foo contents', 'bar': 'bar contents', 'baz': 'baz contents'}

    for executable_name in example_executables.keys():
        with tempfile.NamedTemporaryFile(prefix=executable_name) as f:
            os.chmod(f.name, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR)
            f.write(example_executables[executable_name])
            f.flush()
            os.environ['PATH'] = '%s%s%s' % (os.path.dirname(f.name), os.pathsep, os.environ['PATH'])

# Generated at 2022-06-12 23:37:17.805457
# Unit test for function get_bin_path
def test_get_bin_path():
    import nose
    import shutil
    import tempfile
    from ansible.module_utils._text import to_bytes

    tmp = tempfile.gettempdir()
    bin_file = os.path.join(tmp, "ansible_test_bin")


# Generated at 2022-06-12 23:37:22.512324
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path("false", opt_dirs=['/bin'])
    except ValueError:
        pass
    else:
        assert False, "test_get_bin_path did not throw ValueError"

    assert 'true' == get_bin_path("true", opt_dirs=['/bin']), "test_get_bin_path failed to find true"

# Generated at 2022-06-12 23:37:31.637949
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('sh')
    # Check that the optional arguments -- opt_dirs and required -- are used
    assert get_bin_path('sh', opt_dirs=['/bin'])
    try:
        assert get_bin_path('sh', opt_dirs=['/bin'], required=False)
    except:
        raise AssertionError('Failed test')
    try:
        get_bin_path('bogus_command')
        raise AssertionError('Failed test')
    except ValueError:
        pass

if __name__ == '__main__':
    test_get_bin_path()

# Generated at 2022-06-12 23:37:41.095354
# Unit test for function get_bin_path
def test_get_bin_path():
    bin_path = get_bin_path('yes')
    assert bin_path == "/bin/yes"

    # Test for os.sep
    bin_path = get_bin_path('yes', ["/tmp"])
    assert bin_path == "/tmp/yes"

    # Test for os.sep
    bin_path = get_bin_path('yes', ["/tmp/"])
    assert bin_path == "/tmp/yes"

    # Test for os.sep
    bin_path = get_bin_path('yes', ["/tmp/", "/tmp"])
    assert bin_path == "/tmp/yes"

    # Test for Windows backslash