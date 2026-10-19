

# Generated at 2022-06-12 23:27:43.112575
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('sh')

# Generated at 2022-06-12 23:27:47.632721
# Unit test for function get_bin_path
def test_get_bin_path():
    """Unit tests for method get_bin_path"""
    # Success
    cmd = 'true'
    ret = get_bin_path(cmd)
    assert ret is not None

    # Failure
    cmd = 'doesnotexist'
    try:
        get_bin_path(cmd, required=True)
    except ValueError as e:
        assert 'Failed to find required executable "%s"' % cmd in str(e)
    else:
        assert False, "Expected exception"

# Generated at 2022-06-12 23:27:55.654295
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Test get_bin_path
    '''

    # define expected results
    expected_results = {
        '/bin/true': ['/bin', '/usr/bin', '/usr/local/bin', '/usr/sbin', '/usr/local/sbin'],
        '/usr/bin/true': ['/bin', '/usr/bin', '/usr/local/bin', '/usr/sbin', '/usr/local/sbin'],
        '/usr/local/bin/true': ['/bin', '/usr/bin', '/usr/local/bin', '/usr/sbin', '/usr/local/sbin'],
        '/bin/false': ['/bin', '/usr/bin', '/usr/local/bin'],
    }

    # loop through the expected results

# Generated at 2022-06-12 23:28:00.694200
# Unit test for function get_bin_path
def test_get_bin_path():
    import sys
    # get_bin_path with 'python' which should always exist
    python_path = get_bin_path('python', ['/bin'])
    assert python_path
    assert python_path == sys.executable
    # get_bin_path with arg 'nosuchbinary' which should always produce an Exception
    nosuch_bin_path = False
    try:
        get_bin_path('nosuchbinary')
    except ValueError as e:
        nosuch_bin_path = True
    assert nosuch_bin_path

# Generated at 2022-06-12 23:28:11.741793
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil

    # Create directories for test
    tdir = tempfile.mkdtemp()
    paths = [os.path.join(tdir, 'bin'), os.path.join(tdir, 'sbin')]

    # Create executables to be found
    os.makedirs(paths[0])
    os.makedirs(paths[1])
    executable = os.path.join(paths[0], 'foo')
    with open(executable, 'w') as f:
        f.write('0')
    executable = os.path.join(paths[1], 'bar')
    with open(executable, 'w') as f:
        f.write('0')
    os.chmod(executable, 0o755)

    # Create links for executables
    os

# Generated at 2022-06-12 23:28:19.225347
# Unit test for function get_bin_path
def test_get_bin_path():
    result = get_bin_path('ls')
    assert result == '/bin/ls'

    result = get_bin_path('ls', ['.'])
    assert result == './ls'

    try:
        result = get_bin_path('x' * 200)
    except ValueError as e:
        assert 'Failed to find required executable' in str(e)
    else:
        assert False

    try:
        result = get_bin_path('ls', ['/_this_path_does_not_exist'])
    except ValueError as e:
        assert 'Failed to find required executable' in str(e)
    else:
        assert False

# Generated at 2022-06-12 23:28:22.927031
# Unit test for function get_bin_path
def test_get_bin_path():
    # function to be tested
    from ansible.module_utils.basic import *

    # test 1 - normal case
    try:
        assert get_bin_path('ls')
    except Exception as e:
        assert False, 'Failed test 1: %s' % e

    # test 2 - not found
    try:
        assert get_bin_path('xxx-non-existent-xxx')
        assert False, 'Failed test 2: Expected ValueError Exception not raised'
    except ValueError:
        pass
    except Exception as e:
        assert False, 'Failed test 2: Unexpected exception raised: %s' % e

if __name__ == '__main__':
    test_get_bin_path()

# Generated at 2022-06-12 23:28:27.717935
# Unit test for function get_bin_path
def test_get_bin_path():
    # Testing with different PATH env variable
    os.environ['PATH'] = '/bin:/usr/bin'

    # Testing with existing and executable /bin/id command
    assert get_bin_path('id') == '/bin/id'

    # Testing with non-existing command
    try:
        get_bin_path('non-existing')
        assert False
    except ValueError:
        assert True
    else:
        assert False

    # Testing with executable (in python script) command
    assert get_bin_path(__file__) == __file__

# Generated at 2022-06-12 23:28:33.791291
# Unit test for function get_bin_path
def test_get_bin_path():
    path = get_bin_path('ls')
    assert '/bin/ls' == path
    path = get_bin_path('ls', required=True)
    assert '/bin/ls' == path
    path = get_bin_path('ls', ['/bin'])
    assert '/bin/ls' == path
    path = get_bin_path('ls', ['/bin', '/usr/bin'])
    assert '/bin/ls' == path
    path = get_bin_path('ls', ['/usr/bin', '/bin'])
    assert '/bin/ls' == path
    path = get_bin_path('ls', ['/usr/bin', '/bin'], True)
    assert '/bin/ls' == path
    path = get_bin_path('ls', ['/usr/bin', '/bin'], False)

# Generated at 2022-06-12 23:28:40.747282
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('ls') == '/bin/ls'
    try:
        get_bin_path('command-that-does-not-exist', ['/usr'])
        assert False, 'This should not have worked'
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "command-that-does-not-exist" in paths: /bin:/usr/bin'

    try:
        get_bin_path('command-that-does-not-exist')
        assert False, 'This should not have worked'
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "command-that-does-not-exist" in paths: '

# Generated at 2022-06-12 23:28:49.368193
# Unit test for function get_bin_path
def test_get_bin_path():
    token_path = get_bin_path('sh', ['/bin', '/usr/bin'])
    assert token_path == '/bin/sh' or token_path == '/usr/bin/sh'

    token_path = get_bin_path('sh', ['/bin', '/usr/bin'], ['/usr/local/bin', '/usr/local/sbin'])
    assert token_path == '/bin/sh' or token_path == '/usr/bin/sh' or token_path == '/usr/local/bin/sh' or token_path == '/usr/local/sbin/sh'

# Generated at 2022-06-12 23:28:56.556277
# Unit test for function get_bin_path
def test_get_bin_path():
    # This function must raise ValueError if executable is not found
    try:
        get_bin_path('nonexistent_executable')
        assert False
    except ValueError:
        pass
    # This function must return a full path, even if executable is in current directory
    assert get_bin_path('/bin/ls') == '/bin/ls'
    assert get_bin_path('ls') == '/bin/ls'

# Generated at 2022-06-12 23:29:00.978162
# Unit test for function get_bin_path
def test_get_bin_path():
    result = get_bin_path('sh')
    assert result == '/bin/sh'
    result = get_bin_path('ls', opt_dirs=['/tmp', '/bin'])
    assert result == '/bin/ls'
    result = get_bin_path('foo')
    assert result == 'foo'

# Generated at 2022-06-12 23:29:05.535945
# Unit test for function get_bin_path
def test_get_bin_path():
    # Assumes that path to ping is /bin/ping
    assert get_bin_path('ping') == '/bin/ping'

    # Assumes that path to ping is not /bin/no_such_binary
    try:
        get_bin_path('no_such_binary')
        assert False
    except ValueError:
        pass

# Generated at 2022-06-12 23:29:11.120468
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('python') == '/usr/bin/python'
    assert get_bin_path('python', ['/usr/local/bin']) == '/usr/local/bin/python'
    try:
        get_bin_path('notaprogram', ['/usr/local/bin'])
    except ValueError as err:
        assert str(err) == 'Failed to find required executable "notaprogram" in paths: /usr/local/bin:/usr/bin:/bin'
    else:
        assert False, 'get_bin_path failed to raise ValueError'

# Generated at 2022-06-12 23:29:13.101618
# Unit test for function get_bin_path
def test_get_bin_path():
    path = get_bin_path("ssh")
    assert path.endswith("ssh")

# Generated at 2022-06-12 23:29:15.479055
# Unit test for function get_bin_path
def test_get_bin_path():
    arg = 'ansible-console'
    expected = '/usr/bin/ansible-console'

    actual = get_bin_path(arg)

    assert expected == actual

# Generated at 2022-06-12 23:29:20.069715
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test a known executable
    assert get_bin_path('awk')

    # Test a known non-executable
    try:
        get_bin_path('/etc/passwd')
        assert False
    except ValueError:
        assert True

    # Test a nonexistent file
    try:
        get_bin_path('/no/such/file')
        assert False
    except ValueError:
        assert True

# Generated at 2022-06-12 23:29:26.078650
# Unit test for function get_bin_path
def test_get_bin_path():
    import sys
    sys.path.insert(0, '..')
    from ansible.module_utils.common.file import get_bin_path
    from ansible.module_utils.common.file import is_executable
    from ansible.module_utils.common.file import is_executable_file
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec = dict(
            arg = dict(type='str', required=True),
            opt_dirs = dict(type='list', required=False),
            required = dict(type='bool', required=False),
        )
    )
    arg = module.params['arg']
    opt_dirs = module.params['opt_dirs']
    required = module.params['required']

# Generated at 2022-06-12 23:29:37.038325
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Test get_bin_path()
    '''
    cmds = ['ls', 'python']  # commands which should be found in any PATH
    if os.geteuid() == 0:  # test commands which are only in /sbin on privileged accounts
        cmds.extend(['iptables', 'ip'])
    for command in cmds:
        path = get_bin_path(command)
        # check if path is an existing file
        assert os.stat(path)
        # check if file is executable
        assert os.access(path, os.X_OK)
        # get basename of path and check if it's the same as command
        assert os.path.basename(path) == command
    # test if command not found raises exception
    found = False

# Generated at 2022-06-12 23:29:42.609928
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('sh') == '/bin/sh'
    try:
        assert get_bin_path('sh', ['/usr/bin', '/usr/sbin']) == '/bin/sh'
    except ValueError:
        pass



# Generated at 2022-06-12 23:29:51.681504
# Unit test for function get_bin_path
def test_get_bin_path():
    # Set PATH to a known value and remove PATH
    # Modules should not rely on the system PATH
    os.environ['PATH'] = '/bin:/usr/bin'
    try:
        del os.environ['PATH']
    except Exception:
        pass

    path = get_bin_path('sh')
    assert path == '/bin/sh'

    path = get_bin_path('sh', opt_dirs=['/usr/bin'])
    assert path == '/usr/bin/sh'

    try:
        get_bin_path('ls', required=True)
    except ValueError:
        pass
    else:
        assert False

    try:
        get_bin_path('ls', required=False)
    except ValueError:
        pass
    else:
        assert False


# Generated at 2022-06-12 23:29:59.240059
# Unit test for function get_bin_path
def test_get_bin_path():
    from tempfile import mkdtemp
    from shutil import rmtree
    import random
    # create a temporary directory and make sure it's in the PATH
    temp_dir = mkdtemp()
    old_path = os.environ.get('PATH')
    os.environ['PATH'] = ':'.join([temp_dir, old_path])

    # create a random executable "foo" in the temp_dir and
    # make sure the function can find it
    file_name = os.path.join(temp_dir, "foo")
    with open(file_name, "wb") as f:
        f.write(str(random.random()))

    # make sure file has execute bit set
    mode = os.stat(file_name).st_mode
    mode |= (mode & 0o444) >> 2    # copy

# Generated at 2022-06-12 23:30:09.975331
# Unit test for function get_bin_path
def test_get_bin_path():
    bin_path = get_bin_path('ls')
    assert bin_path == '/bin/ls'
    bin_path = get_bin_path('ls', opt_dirs=['/usr/bin'])
    assert bin_path == '/bin/ls'
    bin_path = get_bin_path('echo', opt_dirs=[None])
    assert bin_path == '/bin/echo'

    try:
        get_bin_path('i_dont_exist')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "i_dont_exist" in paths: /sbin:/bin:/usr/sbin:/usr/bin:/opt/ansible/ansible/bin'
    else:
        assert False, "ValueError not raised"

# Generated at 2022-06-12 23:30:18.281895
# Unit test for function get_bin_path
def test_get_bin_path():
    bin_path = get_bin_path('sh')
    assert bin_path is not None
    assert os.path.exists(bin_path)
    assert bin_path == '/bin/sh'

    # test it with directory paths given
    bin_path = get_bin_path('sh', ['/usr/bin', '/bin'])
    assert bin_path is not None
    assert os.path.exists(bin_path)
    assert bin_path == '/bin/sh'

# Generated at 2022-06-12 23:30:24.520073
# Unit test for function get_bin_path
def test_get_bin_path():
    good_bins = ('ls', '/bin/ls')
    bad_bins = ('madeupname', '/madeupdir/ls')
    opt_dirs = ['/bin', '/usr/bin']

    for arg in good_bins:
        assert get_bin_path(arg, opt_dirs=opt_dirs)

    for arg in bad_bins:
        try:
            get_bin_path(arg, opt_dirs=opt_dirs)
        except ValueError:
            pass
        else:
            raise AssertionError("get_bin_path('%s') should have raised exception" % arg)

# Generated at 2022-06-12 23:30:31.930419
# Unit test for function get_bin_path
def test_get_bin_path():
    test_path = '/tmp/ansible-test'
    if os.path.exists(test_path):
        os.remove(test_path)
    with open(test_path, 'w') as fd:
        fd.write('')
    os.chmod(test_path, 0o0755)
    assert get_bin_path('ansible-test', opt_dirs=[os.path.dirname(test_path)]) == test_path
    os.remove(test_path)
    try:
        get_bin_path('ansible-test', opt_dirs=[os.path.dirname(test_path)])
        assert False, 'Expected Exception'
    except:
        pass

# Generated at 2022-06-12 23:30:42.238605
# Unit test for function get_bin_path
def test_get_bin_path():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict(
            arg=dict(required=True, type='str'),
            opt_dirs=dict(required=False, type='list', default=None),
        )
    )

    arg = module.params['arg']
    opt_dirs = module.params['opt_dirs']

    result = get_bin_path(arg, opt_dirs)

    if not result:
        module.fail_json(msg='Failed to find required executable "%s" in paths: %s' % (arg, os.pathsep.join(opt_dirs)))
    else:
        module.exit_json(path=result)

# Generated at 2022-06-12 23:30:54.740106
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        # test by providing invalid executable name
        get_bin_path('invalid_exec')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "invalid_exec" in paths: /bin:/usr/bin:/usr/local/bin:/sbin:/usr/sbin:/usr/local/sbin'
    else:
        assert False

    # test by providing invalid directory in optional argument opt_dirs
    dir_path = '/invalid/directory/path'

# Generated at 2022-06-12 23:31:05.451328
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('sh') == '/bin/sh'
    opt_dirs = ['/sbin', '/usr/sbin', '/usr/local/sbin']
    assert get_bin_path('ping', opt_dirs=opt_dirs) == '/bin/ping'
    assert get_bin_path('traceroute', opt_dirs=opt_dirs) == '/usr/sbin/traceroute'
    opt_dirs = ['/sbin', '/usr/sbin', '/usr/local/sbin', '/usr/bin']
    assert get_bin_path('traceroute', opt_dirs=opt_dirs) == '/usr/bin/traceroute'
    opt_dirs = ['/sbin', '/usr/sbin', '/usr/local/sbin']

# Generated at 2022-06-12 23:31:16.112598
# Unit test for function get_bin_path
def test_get_bin_path():
    paths = ['/bin', '/usr/bin', '/usr/local/bin']
    assert get_bin_path('sh', paths) == '/bin/sh'
    path = get_bin_path('sh', [])
    if os.path.exists('/bin/sh'):
        assert path == '/bin/sh'
    else:
        assert path == '/usr/bin/sh'
    try:
        get_bin_path('has_no_path_in_the_known_universe')
        raise Exception('unreachable code')
    except ValueError:
        pass

# Generated at 2022-06-12 23:31:23.429417
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Ensure get_bin_path works
    '''
    from ansible.module_utils import basic

    # Test directory that has subfolders, but no bash
    opt_dirs = ['../module_utils/basic', '../module_utils/shell/basic']
    try:
        get_bin_path('bash', opt_dirs)
        assert False, 'get_bin_path should have raised an exception'
    except AssertionError:
        raise
    except Exception:
        pass
    else:
        assert False, 'get_bin_path should have raised an Exception'

    # Now test a directory that has bash
    opt_dirs = ['/usr/bin', '/usr/sbin', '/bin']
    assert '/usr/bin/bash' == get_bin_path('bash', opt_dirs)

# Generated at 2022-06-12 23:31:34.037039
# Unit test for function get_bin_path
def test_get_bin_path():

    from shutil import which

    # Successful calls
    for cmd in ['python', 'python3', 'pip', 'pip3']:
        assert get_bin_path(cmd) == which(cmd)

    # Failed calls
    for cmd in ['badcmd']:
        try:
            get_bin_path(cmd)
            success = True
        except:
            success = False

        assert not success

    # Successful calls with optional parameters
    for cmd in ['python', 'python3', 'pip', 'pip3']:
        opt_paths = ['/usr/bin', '/usr/local/bin', '/bin', '/usr/sbin', '/usr/local/sbin', '/sbin']
        assert get_bin_path(cmd, opt_dirs=opt_paths) == which(cmd)

    #

# Generated at 2022-06-12 23:31:45.929395
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Test the get_bin_path function.
    '''

    try:
        import __main__
        real_program_name = __main__.__file__
    except Exception:
        real_program_name = 'python'

    # Test cases

# Generated at 2022-06-12 23:31:49.959716
# Unit test for function get_bin_path
def test_get_bin_path():
    # Assert expected behavior when passing a required parameter

    # Assert exception is raised if required is True and executable is not found
    try:
        get_bin_path('invalid_exe')
    except ValueError as e:
        assert 'Not Found' in str(e)


if __name__ == '__main__':
    test_get_bin_path()

# Generated at 2022-06-12 23:32:00.933134
# Unit test for function get_bin_path
def test_get_bin_path():

    # Success Tests
    assert os.path.exists(get_bin_path('ansible-playbook'))
    assert os.path.exists(get_bin_path('python'))
    assert os.path.exists(get_bin_path('/bin/bash'))
    assert os.path.exists(get_bin_path('/usr/bin/bash'))
    assert os.path.exists(get_bin_path('/bin/sh'))
    assert os.path.exists(get_bin_path('/usr/bin/sh'))
    assert os.path.exists(get_bin_path('/usr/bin/python'))
    assert os.path.exists(get_bin_path('/usr/bin/python2'))

# Generated at 2022-06-12 23:32:09.969076
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('cat') == '/bin/cat'
    assert get_bin_path('cat', opt_dirs=['/usr/bin']) == '/usr/bin/cat'
    try:
        get_bin_path('cat', opt_dirs=['/no/such/path/bin'])
    except ValueError as e:
        assert 'Failed to find required executable "cat" in paths: /no/such/path/bin:/bin:/usr/bin:/usr/local/bin' in str(e)

# Generated at 2022-06-12 23:32:18.267209
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('/bin/mkdir') == '/bin/mkdir'
    assert get_bin_path('mkdir') == '/bin/mkdir'
    assert get_bin_path('mkdir', ['/usr/bin', '/bin', '/usr/sbin']) == '/bin/mkdir'
    assert get_bin_path('mkdir', ['/usr/bin', '/usr/sbin']) == '/usr/bin/mkdir'
    assert get_bin_path('mkdir', ['/usr/bin', '/bin']) == '/bin/mkdir'
    assert get_bin_path('mkdir', ['/usr/bin', '/usr/sbin']) == '/usr/bin/mkdir'

# Generated at 2022-06-12 23:32:22.337578
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('true') == '/bin/true'
    assert get_bin_path('/bin/true') == '/bin/true'
    assert get_bin_path('/usr/bin/true') == '/usr/bin/true'
    assert get_bin_path('/tmp/doesnotexist') is None

# Generated at 2022-06-12 23:32:33.940682
# Unit test for function get_bin_path
def test_get_bin_path():
    # test common bin path in PATH
    try:
        get_bin_path('pwd')
    except ValueError:
        raise AssertionError('test_get_bin_path: \'pwd\' not found in PATH')

    # test bin path not in PATH
    # expect ValueError
    try:
        get_bin_path('doesnotexist')
        raise AssertionError('test_get_bin_path: \'doesnotexist\' found in PATH')
    except ValueError:
        pass

    # test bin path in provided opt_dirs
    # expect no ValueError

# Generated at 2022-06-12 23:32:49.626249
# Unit test for function get_bin_path
def test_get_bin_path():
    '/usr/bin/foo' == get_bin_path('foo')
    '/usr/bin/foo' == get_bin_path('/usr/bin/foo')
    '/usr/bin/foo' == get_bin_path('/usr/bin/../bin/foo')
    '/usr/bin/foo' == get_bin_path('/usr/bin/../sbin/../bin/foo')
    '/usr/bin/foo' == get_bin_path('/usr/bin/foo', ['', '/usr/bin'])
    '/usr/bin/foo' == get_bin_path('/usr/bin/foo', ['', '/usr/bin'])
    '/usr/bin/foo' == get_bin_path('/usr/bin/foo', ['/usr/bin/../bin'])

    # Check with optional directories


# Generated at 2022-06-12 23:32:59.839346
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    from ansible.module_utils.common.file import is_executable

    def write_file(path, content):
        with open(path, 'w') as fd:
            fd.write(content)

# Generated at 2022-06-12 23:33:07.277847
# Unit test for function get_bin_path
def test_get_bin_path():
    # test for non-existant executable
    import pytest
    from ansible.module_utils.common.file import is_executable

    with pytest.raises(ValueError):
        get_bin_path("notanexecutablethisshouldneverbeinapath")

    # example return value
    assert get_bin_path("ls") is not None
    assert is_executable(get_bin_path("ls"))
    assert os.path.split(get_bin_path("ls"))[-1] == "ls"

# Generated at 2022-06-12 23:33:11.739939
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test case 1:  PATH and opt_dirs are empty
    assert get_bin_path('python') == '/usr/bin/python'

    # Test case 2:  PATH contains directory '/bin' and opt_dirs is empty
    oldPath = os.environ.get('PATH', '')
    newPath = oldPath + os.pathsep + '/bin'
    os.environ['PATH'] = newPath
    assert get_bin_path('python') == '/usr/bin/python'

    # Test case 3:  PATH is empty and opt_dirs contains directory '/bin'
    os.environ['PATH'] = ''
    assert get_bin_path('python', opt_dirs=['/bin']) == '/bin/python'

    # Test case 4:  PATH does not contain directory '/bin' and opt_dirs

# Generated at 2022-06-12 23:33:22.386120
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil
    import stat

    tempdir = tempfile.mkdtemp()

# Generated at 2022-06-12 23:33:31.325043
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import os
    import shutil
    import stat

    tmp_dir = tempfile.mkdtemp()
    test_bins = ['bash', 'test_bin_path']
    old_path = os.environ.get('PATH')


# Generated at 2022-06-12 23:33:42.452841
# Unit test for function get_bin_path
def test_get_bin_path():
    import os
    import shutil
    import tempfile

    bin_path = '/bin/sh'

    test_dir = tempfile.gettempdir()
    test_binary = os.path.join(test_dir, 'test_binary')
    shutil.copyfile(bin_path, test_binary)
    os.chmod(test_binary, 0o755)
    assert get_bin_path('test_binary', opt_dirs=[test_dir]) == test_binary

    test_dir = tempfile.mkdtemp()
    test_binary = os.path.join(test_dir, 'test_binary')
    shutil.copyfile(bin_path, test_binary)
    os.chmod(test_binary, 0o755)

# Generated at 2022-06-12 23:33:50.814529
# Unit test for function get_bin_path
def test_get_bin_path():
    from ansible.module_utils.six.moves import builtins
    #
    # test when executable is found
    #
    # make open() a no-op
    fake_open = lambda *args, **kwargs: None
    original_open = builtins.open
    builtins.open = fake_open
    # make os.path.exists() always return True
    original_exists = os.path.exists
    os.path.exists = lambda *args: True
    # make is_executable() always return True
    original_is_executable = is_executable
    is_executable = lambda *args: True

# Generated at 2022-06-12 23:33:53.695083
# Unit test for function get_bin_path
def test_get_bin_path():
    path_found = get_bin_path('ls', opt_dirs=['/bin/', '/usr/bin/', '/tmp/'])
    assert path_found == '/bin/ls'


# Generated at 2022-06-12 23:34:04.979336
# Unit test for function get_bin_path
def test_get_bin_path():
    bin_path = get_bin_path('sh')
    assert not is_executable('/')
    assert not is_executable('/nonexistent')
    assert is_executable(bin_path)
    assert os.environ.get('PATH') is not None

    # Test for optional arguments
    assert get_bin_path('sh', required=True)
    assert get_bin_path('sh', ['.'], required=True)
    assert bin_path == get_bin_path('sh', ['/bin'])
    assert bin_path == get_bin_path('sh', ['/bin'], required=True)

    try:
        get_bin_path('nonexistent', required=True)
        raise AssertionError('Expected ValueError')
    except ValueError:
        pass


# Generated at 2022-06-12 23:34:17.600243
# Unit test for function get_bin_path
def test_get_bin_path():
    print(get_bin_path('ansible-playbook'))
    print(get_bin_path('ansible-playbook', opt_dirs=['/opt/ansible/bin']))
    print(get_bin_path('ansible-playbook', opt_dirs=['/nonexisting/path']))


# Generated at 2022-06-12 23:34:28.288804
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('cowsay', required=True) == '/usr/games/cowsay'
    assert get_bin_path('cowsay', required=True, opt_dirs=['/usr/games']) == '/usr/games/cowsay'
    assert get_bin_path('cowsay', required=True, opt_dirs=['/usr']) == '/usr/games/cowsay'
    try:
        get_bin_path('cowsay', required=False)
        assert False
    except ValueError:
        pass
    try:
        get_bin_path('not-a-binary', required=True)
        assert False
    except ValueError:
        pass

# Generated at 2022-06-12 23:34:39.341487
# Unit test for function get_bin_path
def test_get_bin_path():
    from ansible.module_utils.common._collections_compat import UserDict
    bin_path = get_bin_path('sh')
    cmd = "%s -c 'echo $PATH'" % bin_path
    ouf, inp, err = os.popen3(cmd)
    err.readlines()
    path = ouf.readlines()[0]
    opt_dirs = ['/tmp', '/usr/bin']
    assert get_bin_path('sh', opt_dirs) == bin_path
    assert get_bin_path('true', opt_dirs) == '/usr/bin/true'
    assert get_bin_path('false', opt_dirs) == '/usr/bin/false'
    assert get_bin_path('date') is not None
    import tempfile

# Generated at 2022-06-12 23:34:42.518132
# Unit test for function get_bin_path
def test_get_bin_path():
    opt_dirs = ["/usbin"]
    for script in ["py.test", "ansible", "cd", "ls"]:
        assert get_bin_path(script, opt_dirs)
    for script in ["cd", "ls"]:
        assert get_bin_path(script, opt_dirs)

# Generated at 2022-06-12 23:34:52.729170
# Unit test for function get_bin_path
def test_get_bin_path():
    def _test_get_bin_path(paths):
        assert get_bin_path('sh', paths) == os.path.join('/', 'bin', 'sh')
        assert get_bin_path('cat', paths) == os.path.join('/', 'bin', 'cat')
        assert get_bin_path('ls', paths) == os.path.join('/', 'bin', 'ls')

    # Test get_bin_path when path contains only /bin
    _test_get_bin_path(['/bin'])

    # Test get_bin_path when path contains only /usr/bin
    _test_get_bin_path(['/usr/bin'])

    # Test get_bin_path when path contains only /usr/local/bin

# Generated at 2022-06-12 23:35:00.440070
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test with no arguments
    assert get_bin_path('sh') == '/bin/sh'

    # Test with valid optional arguments
    assert get_bin_path('sh', ['.']) == '/bin/sh'

    # Test with invalid optional arguments
    try:
        get_bin_path('sh', ['./foo'])
        assert False, 'Expected exception to be raised'
    except ValueError:
        pass

    # Test with missing required executable
    try:
        get_bin_path('foo')
        assert False, 'Expected exception to be raised'
    except ValueError:
        pass

    # Test with missing required executable and optional arguments

# Generated at 2022-06-12 23:35:09.206392
# Unit test for function get_bin_path
def test_get_bin_path():
    from mock import patch
    import tempfile
    import stat
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils import basic
    import sys

    tmp_dir = tempfile.mkdtemp()
    tmp_file = tempfile.NamedTemporaryFile(mode='wt', dir=tmp_dir, delete=False)
    tmp_file.close()
    fpath = tmp_file.name
    os.chmod(fpath, stat.S_IREAD | stat.S_IEXEC)

    if 'PATH' in os.environ:
        old_path = os.environ['PATH']
        new_path = tmp_dir + ':' + old_path
    else:
        old_path = ':'
        new_path = tmp_dir


# Generated at 2022-06-12 23:35:19.950683
# Unit test for function get_bin_path
def test_get_bin_path():
    from collections import namedtuple
    from ansible.module_utils.common.file import is_executable
    import tempfile
    import os
    import shutil
    import unittest

    def touch_file(path):
        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))
        with open(path, 'a'):
            os.utime(path, None)

    # Set up
    FakePopen = namedtuple('popen', ['returncode'])
    p = FakePopen(0)
    popen_impl = os.popen

    class MockFile(object):
        def __init__(self, path):
            self.path = path


# Generated at 2022-06-12 23:35:32.234892
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    We assume that /bin/ls exists and is executable,
    /bin/ls-does-not-exist does not exist, and
    /bin is not executable.
    '''
    # Test normal behavior, should work
    assert get_bin_path('ls') == '/bin/ls'

    # Test function properly raises exception when file doesn't exist
    try:
        get_bin_path('ls-does-not-exist')
    except ValueError:
        pass
    else:
        raise AssertionError('get_bin_path did not raise exception when file does not exist.')

    # Test function properly raises exception when dir is not executable
    try:
        get_bin_path('ls', opt_dirs=['/bin'])
    except ValueError:
        pass
    else:
        raise AssertionError

# Generated at 2022-06-12 23:35:39.091185
# Unit test for function get_bin_path
def test_get_bin_path():
    """
    Test get_bin_path. It searches for echo executable in the list of directories
    appended with the system path. It expects to find one in /bin.
    """
    test_dir = '/bin'
    try:
        ret = get_bin_path('echo', opt_dirs=[test_dir])
    except:
        ret = None
    assert ret is not None

# Generated at 2022-06-12 23:35:57.975738
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path("python") == "/usr/bin/python"

# Generated at 2022-06-12 23:36:05.388243
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path('foo_bar_baz.sh')
        raise Exception("Failed to raise an exception")
    except ValueError as e:
        print("Expected exception: %s" % e)

    try:
        get_bin_path('an-unreadable-file')
        raise Exception("Failed to raise an exception")
    except ValueError as e:
        print("Expected exception: %s" % e)

    print("/bin exists, and is executable: %s" % get_bin_path('/bin'))
    print("/bin exists, but is not executable: %s" % get_bin_path('/bin', required=False))


# Generated at 2022-06-12 23:36:06.746010
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('sh') == '/bin/sh'

# Generated at 2022-06-12 23:36:15.843935
# Unit test for function get_bin_path
def test_get_bin_path():
    # If we do not have the specified executable in path, raise ValueError
    try:
        get_bin_path('not-executable')
    except ValueError as e:
        assert 'Failed to find required executable' in str(e)
    else:
        assert False, 'Expected ValueError'

    # If we have the specified executable in path, return the path
    try:
        assert get_bin_path('ls') == '/bin/ls'
    except ValueError as e:
        assert False, 'Expected path to ls executable: %s' % str(e)

    # If we have the specified executable in the alternative paths, return the path
    # Note that we need to add a directory that does not exist, or else get_bin_path will
    # return the first match instead of the last match.

# Generated at 2022-06-12 23:36:24.690645
# Unit test for function get_bin_path
def test_get_bin_path():
    import os

    _vim_path = get_bin_path('vim')
    assert _vim_path == '/usr/bin/vim'

    # 'vim' found in PATH
    _vim_path = get_bin_path('vim', ['/bin', '/usr/bin', '/usr/sbin'])
    assert _vim_path == '/usr/bin/vim'

    # 'vim' found in PATH and /usr/sbin
    _vim_path = get_bin_path('vim', opt_dirs=['/bin', '/usr/bin'])
    assert _vim_path == '/usr/bin/vim'

    # 'vim' found in PATH and /usr/sbin. Need to test both because it is OS dependent
    _vim_path = get_bin_path('vim', opt_dirs=['/bin'])


# Generated at 2022-06-12 23:36:33.284088
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('sh') == '/bin/sh'
    assert get_bin_path('/bin/sh') == '/bin/sh'
    assert get_bin_path(os.path.abspath('../test/runner/molecule/scenario/default/playbook.yml')) == os.path.abspath('../test/runner/molecule/scenario/default/playbook.yml')
    import tempfile
    temp_dir = tempfile.mkdtemp()
    with open(os.path.join(temp_dir, 'foo'), 'w') as f:
        f.write('#!/bin/sh\n')
    assert get_bin_path('foo', [temp_dir]) == os.path.join(temp_dir, 'foo')
    import shutil

# Generated at 2022-06-12 23:36:38.213654
# Unit test for function get_bin_path
def test_get_bin_path():
    path = get_bin_path('sh')
    if not path:
        raise AssertionError('Did not find expected executable "sh" in path')

    try:
        get_bin_path('notthere')
    except ValueError:
        pass
    else:
        raise AssertionError('get_bin_path did not raise expected exception')

# Generated at 2022-06-12 23:36:46.359703
# Unit test for function get_bin_path
def test_get_bin_path():
    import sys

    # save current PATH
    old_path = os.environ.get('PATH', '')
    try:
        os.environ['PATH'] = ':'.join([os.path.dirname(sys.executable),
                                       '/usr/bin', '/bin', '/usr/sbin', '/sbin'])

        path = get_bin_path('python3.6')
        assert os.path.basename(path) == 'python3.6'
    finally:
        os.environ['PATH'] = old_path

# Generated at 2022-06-12 23:36:54.046439
# Unit test for function get_bin_path
def test_get_bin_path():
    bin_path = get_bin_path('ls')
    assert bin_path is not None
    assert bin_path == '/bin/ls'
    bin_path = get_bin_path('ls', ['/bin', '/usr/bin'])
    assert bin_path is not None
    assert bin_path == '/bin/ls'
    bin_path = get_bin_path('awk', [])
    assert bin_path is not None
    assert bin_path == '/usr/bin/awk'
    bin_path = get_bin_path('sed', ['/bin', '/usr/bin'])
    assert bin_path is not None
    assert bin_path == '/bin/sed'
    bin_path = get_bin_path('wc', ['/usr/bin', '/bin'])
    assert bin_path is not None
   

# Generated at 2022-06-12 23:36:58.282310
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        # success condition
        get_bin_path('python')
        # failure conditions
        get_bin_path('no_such_file_should_exist')
    except Exception:
        assert True
    else:
        assert False

# Generated at 2022-06-12 23:37:24.367779
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test the case where the binary is found on the path
    try:
        find_bin = get_bin_path('find')
    except ValueError:
        assert False
    assert find_bin == '/usr/bin/find'

    # Test the case where the binary is not found on the path
    try:
        get_bin_path('does_not_exist')
        assert False
    except ValueError:
        assert True

    # Test the case where the binary is found in opt_dirs
    try:
        get_bin_path('pkg-config', opt_dirs=['/usr/bin'])
    except ValueError:
        assert False

    # Test the case where the binary is found in opt_dirs

# Generated at 2022-06-12 23:37:30.324816
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Unit test for function get_bin_path.
    '''
    import sys
    import tempfile

    tmp_path = tempfile.mkdtemp()
    tmp_file = tempfile.NamedTemporaryFile(dir=tmp_path, mode='w', delete=False)
    tmp_file.write('#!/bin/sh')
    tmp_file.close()

    old_path = os.environ['PATH']
    os.environ['PATH'] = os.pathsep.join([os.path.dirname(tmp_file.name), tmp_path])

    if not sys.platform.startswith('win'):
        assert get_bin_path(os.path.basename(tmp_file.name)) == tmp_file.name

# Generated at 2022-06-12 23:37:40.701030
# Unit test for function get_bin_path
def test_get_bin_path():
    # Assume current path is in PATH and it contains a file named "test_file" and it is executable
    os.environ['PATH'] = '.:'
    assert get_bin_path('test_file') == 'test_file'
    assert get_bin_path('./test_file') == './test_file'
    assert get_bin_path('test_file', opt_dirs=['.']) == 'test_file'
    os.environ['PATH'] = ''
    assert get_bin_path('test_file', []) == 'test_file'
    assert get_bin_path('test_file', []) == 'test_file'
    assert get_bin_path('./test_file', ['.']) == './test_file'
    # Remove the test file