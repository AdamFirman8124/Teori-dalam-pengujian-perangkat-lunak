

# Generated at 2022-06-12 23:27:43.222530
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path('does-not-exist')
    except ValueError as e:
        assert "Failed to find required executable" in str(e)
    else:
        raise AssertionError("Failed to raise ValueError on failure")
    try:
        get_bin_path('python', ['/anywhere'])
    except ValueError as e:
        assert "Failed to find required executable" in str(e)
    else:
        raise AssertionError("Failed to raise ValueError on failure")
    assert type(get_bin_path('python', required=True)) is str

# Generated at 2022-06-12 23:27:47.849689
# Unit test for function get_bin_path
def test_get_bin_path():
    opt_dirs = ['/bin','/sbin','/usr/bin','/usr/sbin']
    assert get_bin_path('ls') == '/bin/ls'
    assert get_bin_path('ls',opt_dirs) == '/bin/ls'
    assert get_bin_path('ls',opt_dirs,True) == '/bin/ls'
    assert get_bin_path('ls',opt_dirs,False) == '/bin/ls'

# Generated at 2022-06-12 23:27:48.987394
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('sh') == '/bin/sh'

# Generated at 2022-06-12 23:27:56.936635
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test with a bad path
    try:
        bin_path = get_bin_path('/__junk/something_fake', '/__junk')
    except ValueError:
        pass
    else:
        raise AssertionError('Expected get_bin_path to raise ValueError with bad path')

    # Test with a good path
    os.environ["PATH"] = "/usr/bin:/bin:/usr/local/bin"
    bin_path = get_bin_path('ls')
    assert bin_path == '/bin/ls', 'Expected /bin/ls, got %s' % bin_path

    # Test with a good path in an optional dir
    tmpdir = 'test_get_bin_path_dir'
    os.environ["PATH"] = "/usr/bin:/bin:/usr/local/bin"
   

# Generated at 2022-06-12 23:28:03.447307
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('python')
    assert get_bin_path('python', ['/usr/bin', '/usr/local/bin'])
    assert get_bin_path('python', ['/usr/bin/python3'])

    try:
        get_bin_path('asdfghjkl')
    except ValueError as e:
        assert e.message.startswith('Failed to find required executable')
        assert e.message.endswith('in paths: %s' % (os.pathsep.join(os.environ.get('PATH', '').split(os.pathsep))))
        assert e.message.find('asdfghjkl') > -1


# Generated at 2022-06-12 23:28:07.566219
# Unit test for function get_bin_path
def test_get_bin_path():
    # test that it finds the current executable
    cur_exe = sys.argv[0]
    if getattr(sys, 'frozen', False):
        assert get_bin_path('ansible-test-unit') == cur_exe
    else:
        assert get_bin_path('python') == cur_exe



# Generated at 2022-06-12 23:28:18.010171
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    from ansible_collections.misc.not_a_real_collection.plugins.module_utils import basic

    pat = os.path.join(tempfile.gettempdir(), "binpath_test")
    open(pat, "w").close()
    with basic.environment_append({"PATH": tempfile.gettempdir()}):
        assert get_bin_path("binpath_test") == pat

    # check /sbin dirs
    check_paths = [
        ('/usr/sbin/nologin', '/usr/sbin/nologin'),
        ('/sbin/nologin', '/sbin/nologin'),
    ]
    for path in check_paths:
        assert get_bin_path(path[0]) == path[1]

    import shutil
    shut

# Generated at 2022-06-12 23:28:21.337303
# Unit test for function get_bin_path
def test_get_bin_path():
    from distutils.spawn import find_executable
    
    assert(get_bin_path('ls') == find_executable('ls'))
    assert(get_bin_path('foo') == None)

# Generated at 2022-06-12 23:28:27.248576
# Unit test for function get_bin_path
def test_get_bin_path():
    import os

    arg = 'ls'
    opt_dirs = None
    required = True
    assert os.path.exists(get_bin_path(arg, opt_dirs, required))

    arg = 'ls'
    opt_dirs = '/bin'
    required = True
    assert os.path.exists(get_bin_path(arg, opt_dirs, required))

    arg = 'lsssssssssssssssssssss'
    opt_dirs = '/bin'
    required = True
    try:
        get_bin_path(arg, opt_dirs, required)
    except ValueError:
        assert True
        return
    assert False

# Generated at 2022-06-12 23:28:36.678988
# Unit test for function get_bin_path
def test_get_bin_path():
    # TODO: better unit testing here, test all return paths
    import sys

    if sys.platform == 'win32':
        raise AssertionError('win32 not supported for these tests')

    # non-existent executable on OSX
    try:
        get_bin_path('/Library/Application Support/foo.bar/blah.sbin/exec', required=True)
        raise AssertionError('did not raise exception on failed find')
    except ValueError:
        pass

    # valid executable on OSX /path/to/del_svc.sh
    assert get_bin_path('del_svc.sh', opt_dirs=[os.path.join('/Library', 'Application Support')]) == 'del_svc.sh'
    # valid executable on OSX /Library/Application Support/foo.bar/blah.s

# Generated at 2022-06-12 23:28:40.886406
# Unit test for function get_bin_path
def test_get_bin_path():
    # test for non-existing binary
    assert get_bin_path('non-existing-binary', opt_dirs=[])


# Generated at 2022-06-12 23:28:47.081921
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path('/bin/sh')
        get_bin_path('/bin/sh', opt_dirs=['/bin'])
        assert False
    except ValueError as e:
        assert 'Failed to find required executable' in str(e)

    assert get_bin_path('sh') == '/bin/sh'
    assert get_bin_path('sh', opt_dirs=['/bin']) == '/bin/sh'

# Generated at 2022-06-12 23:28:52.705990
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil


# Generated at 2022-06-12 23:29:03.828945
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Test case:
    - test executable does not exist in $PATH
    - test executable does not exist in /usr/sbin
    - test executable does not exist in /usr/local/sbin
    - test executable exists in /bin
    - test executable exists in $PATH
    '''
    import tempfile
    import shutil
    
    # Create test directory
    temp_dir = tempfile.mkdtemp(prefix='ansible_test_get_bin_path')

    # Create test executable
    bin_path = os.path.join(temp_dir, 'ansible_test_bin')
    with open(bin_path, 'w') as f:
        f.write('#!/usr/bin/python\n')
        f.write('print("Hello World")\n')

# Generated at 2022-06-12 23:29:11.283231
# Unit test for function get_bin_path
def test_get_bin_path():
    # get_bin_path raises ValueError if executable is not found
    try:
        get_bin_path('doesNotExist')
        assert False
    except ValueError:
        pass

    try:
        get_bin_path('doesNotExist', required=True)
        assert False
    except ValueError:
        pass

    # search /sbin, /usr/sbin, or /usr/local/sbin
    assert get_bin_path('ip') == '/bin/ip'
    assert get_bin_path('ifconfig') == '/sbin/ifconfig'
    assert get_bin_path('route') == '/sbin/route'

    # executable can be in current working directory
    cwd = os.getcwd()
    os.chdir('/tmp')

# Generated at 2022-06-12 23:29:16.046113
# Unit test for function get_bin_path
def test_get_bin_path():

    assert get_bin_path('sh') == '/bin/sh'
    assert get_bin_path('bash') == '/bin/bash'

    #if the file doesn't exist, raise the ValueError
    try:
        get_bin_path('gibberish')
    except ValueError:
        assert True
    else:
        assert False

# Generated at 2022-06-12 23:29:22.613945
# Unit test for function get_bin_path
def test_get_bin_path():
    # get a fake path
    oldpath = os.environ.get('PATH')
    testpath = '/tmp/testpath' + os.pathsep + oldpath
    # make it non-existent
    os.environ['PATH'] = testpath
    # invoking get_bin_path with required=False should not fail
    get_bin_path('some_executable', required=False)
    # invoking get_bin_path with required=True should fail
    try:
        get_bin_path('some_executable', required=True)
        assert False
    except ValueError as e:
        assert True
    # clean up
    os.environ['PATH'] = oldpath

# Generated at 2022-06-12 23:29:31.789204
# Unit test for function get_bin_path
def test_get_bin_path():
    get_bin_path('sh')  # should not raise any errors and should return a valid executable in PATH
    try:
        get_bin_path('random_command')  # should raise ValueError
    except ValueError:
        pass
    else:
        raise AssertionError('get_bin_path should raise a ValueError if the executable is not found in paths')
    try:
        get_bin_path('random_command', opt_dirs=['/junk'])  # should raise ValueError
    except ValueError:
        pass
    else:
        raise AssertionError('get_bin_path should raise a ValueError if the executable is not found in paths')
    get_bin_path('sh', opt_dirs=['/bin'])  # should not raise any errors and should return a valid executable in /bin

# Generated at 2022-06-12 23:29:43.090298
# Unit test for function get_bin_path
def test_get_bin_path():
    # create temp dirs
    import tempfile
    import shutil
    tmpdir = tempfile.mkdtemp(prefix='ansible-tmp')
    tmpdir2 = tempfile.mkdtemp(prefix='ansible-tmp')

    # create temp files
    fd, exec_file = tempfile.mkstemp(dir=tmpdir)
    os.chmod(exec_file, 0o777)
    exec_file2 = exec_file + '2'
    shutil.copy(exec_file, exec_file2)
    noexec_file = tempfile.mkstemp(dir=tmpdir)[1]


# Generated at 2022-06-12 23:29:51.033878
# Unit test for function get_bin_path
def test_get_bin_path():
    # no exception should be thrown here
    get_bin_path('sh')
    get_bin_path('bash')
    get_bin_path('python')

    # bin is not in $PATH and thus should raise exception
    try:
        get_bin_path('foobarinvalid')
    except ValueError:
        pass
    else:
        raise AssertionError('Invalid executable was found in $PATH or exception was not raised')

    # bin from /sbin is not in $PATH by default and thus should raise exception
    try:
        get_bin_path('poweroff')
    except ValueError:
        pass
    else:
        raise AssertionError('Invalid executable was found in $PATH or exception was not raised')

    # bin from /sbin should be in $PATH and thus should not raise exception

# Generated at 2022-06-12 23:29:54.107791
# Unit test for function get_bin_path
def test_get_bin_path():
    import sys
    assert get_bin_path(sys.executable) == sys.executable

# Generated at 2022-06-12 23:30:00.736928
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil
    import os
    full_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'get_bin_path')
    # Create a temporary directory
    tmpdir = tempfile.mkdtemp()
    if os.path.exists(full_path):
        # Move get_bin_path script to temporary directory
        shutil.move(full_path, tmpdir)
    # Create local dir in temp directory
    local_dir = os.path.join(tmpdir, 'local')
    os.mkdir(local_dir)
    os.environ['PATH'] = tmpdir + os.pathsep + os.environ['PATH']
    # Place the script in search path

# Generated at 2022-06-12 23:30:11.526138
# Unit test for function get_bin_path
def test_get_bin_path():
    # set PATH to a known value
    path = '/usr/bin:/bin'
    os.environ['PATH'] = path

    # test normal case where a valid binary is found
    try:
        get_bin_path('ls')
    except:
        raise AssertionError('get_bin_path should not throw an Exception')

    # test case where binary is not found in path and required=False
    try:
        get_bin_path('not_ls')
    except ValueError:
        pass
    except:
        raise AssertionError('get_bin_path should throw a ValueError')

    # test case where binary is not found in path and required=True
    try:
        get_bin_path('not_ls', required=True)
    except ValueError:
        pass
    except:
        raise AssertionError

# Generated at 2022-06-12 23:30:14.880611
# Unit test for function get_bin_path
def test_get_bin_path():
    path = get_bin_path('ls')
    assert is_executable(path)

# Generated at 2022-06-12 23:30:19.884522
# Unit test for function get_bin_path
def test_get_bin_path():
    # Setup environ PATH
    test_path = '/bin:/usr/bin:/sbin:/usr/sbin'

    os.environ['PATH'] = test_path

    # Call get_bin_path
    bin_path = get_bin_path('sh')

    # Check results
    assert bin_path == '/bin/sh'


# Utility function for unit testing only

# Generated at 2022-06-12 23:30:29.595516
# Unit test for function get_bin_path
def test_get_bin_path():
    import sys
    import nose

    if not os.path.isdir('/usr/bin'):
        raise nose.SkipTest('/usr/bin does not exist')

    # test find bash in PATH
    ret = get_bin_path('bash')
    assert ret == '/bin/bash'

    # test fail to find invalid executable
    try:
        get_bin_path('invalid_exec')
    except ValueError:
        pass
    else:
        assert False, "Function get_bin_path: Invalid executable 'invalid_exec' not found in PATH."

    # test find bash using optional list of directories
    ret = get_bin_path('bash', ['/bin'])
    assert ret == '/bin/bash'

    # test find bash in optional list of directories

# Generated at 2022-06-12 23:30:38.951132
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('/bin/ls') == '/bin/ls'
    assert get_bin_path('ls') == '/bin/ls'
    assert get_bin_path('ls', opt_dirs=['/tmp']) == '/bin/ls'
    try:
        get_bin_path('/doesnotexist')
        assert False
    except ValueError:
        assert True
    try:
        get_bin_path('/doesnotexist', required=True)
        assert False
    except ValueError:
        assert True
    try:
        get_bin_path('doesnotexist', required=True)
        assert False
    except ValueError:
        assert True

# Generated at 2022-06-12 23:30:47.935469
# Unit test for function get_bin_path
def test_get_bin_path():
    if 'TEST_GET_BIN_PATH' in os.environ and os.environ['TEST_GET_BIN_PATH'] == '1':
        # Function get_bin_path is being tested with a subprocess. Make sure that the current
        # process has no PATH set.
        if os.environ.get('PATH', False):
            os.environ.pop('PATH')

        (rc, out, err) = module.run_command('echo $PATH')
        if rc != 0:
            module.fail_json(msg=err)
        if out:
            module.fail_json(msg='PATH should not be set but is set to "%s"' % out)

        # PATH is empty. This should raise an Exception since the required executable does not exist.

# Generated at 2022-06-12 23:30:53.041118
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test with missing executable
    try:
        get_bin_path('nonexisting-executable', required=True)
        assert False, "get_bin_path('nonexisting-executable') should fail but succeeded"
    except ValueError:
        pass
    try:
        get_bin_path('nonexisting-executable')
        assert False, "get_bin_path('nonexisting-executable') should fail but succeeded"
    except ValueError:
        pass
    # Test with existing executable
    assert get_bin_path('/bin/sh') == '/bin/sh'
    assert get_bin_path('sh') == '/bin/sh'
    assert get_bin_path('sh', opt_dirs=['/bin']) == '/bin/sh'



# Generated at 2022-06-12 23:31:02.134888
# Unit test for function get_bin_path
def test_get_bin_path():

    try:
        get_bin_path('sh')
    except ValueError:
        assert False, 'No sh found'
    try:
        get_bin_path('my_special_shell', ['/bin'])
    except ValueError:
        pass
    else:
        assert False, 'This should fail'
    try:
        get_bin_path('my_special_shell', ['/bin'], required=True)
    except ValueError:
        pass
    else:
        assert False, 'This should fail'
    try:
        get_bin_path('my_special_shell', required=True)
    except ValueError:
        pass
    else:
        assert False, 'This should fail'

# Generated at 2022-06-12 23:31:11.227293
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path("wrong_file")
    except:
        sys.exc_info()[0]
    try:
        get_bin_path("false")
    except:
        sys.exc_info()[0]
    try:
        get_bin_path("/usr/bin/python3")
    except:
        sys.exc_info()[0]

# Generated at 2022-06-12 23:31:14.928470
# Unit test for function get_bin_path
def test_get_bin_path():
    test_arg = 'python3'
    test_opt_dir = '/usr/bin'
    assert get_bin_path(test_arg, [test_opt_dir]) == '/usr/bin/python3'
    assert get_bin_path(test_arg) == '/usr/bin/python3'

# Generated at 2022-06-12 23:31:18.282558
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('ls') == '/bin/ls'
    assert get_bin_path('ls', ['/usr/bin']) == '/usr/bin/ls'
    try:
        get_bin_path('grep')
        assert False
    except ValueError:
        pass

# Generated at 2022-06-12 23:31:26.995227
# Unit test for function get_bin_path
def test_get_bin_path():
    test_paths = None
    executable = 'ansible'
    # Find in default path
    try:
        get_bin_path(executable)
    except ValueError:
        raise ValueError("Executable %s not found in path" % executable)

    # Find in non-default path
    try:
        get_bin_path(executable, opt_dirs=['/usr/bin'])
    except ValueError:
        raise ValueError("Executable %s not found in path" % executable)

    # Assert check for executable
    try:
        get_bin_path('/etc/passwd')
        raise ValueError("Executable is a directory")
    except ValueError:
        pass


# Generated at 2022-06-12 23:31:32.900748
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path("python") != None
    try:
        get_bin_path("python2.7", required=True)
        assert False, "python2.7 should not be in path on this system"
    except ValueError:
        pass
    assert get_bin_path("python2.7", opt_dirs=["/usr/bin/"])
    assert get_bin_path("python2.7", ["/usr/bin/"])

# Generated at 2022-06-12 23:31:39.455363
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path('invalid_file', required=True)
        assert False
    except ValueError:
        assert True
    try:
        get_bin_path('invalid_file')
        assert False
    except ValueError:
        assert True
    try:
        get_bin_path('invalid_file', opt_dirs=['/usr/bin'], required=True)
        assert False
    except ValueError:
        assert True
    try:
        get_bin_path('invalid_file', opt_dirs=['/usr/bin'])
        assert False
    except ValueError:
        assert True

# Generated at 2022-06-12 23:31:48.942085
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Unit test for function get_bin_path
    '''
    import os
    import tempfile
    import sys

    # Create some temporary files with various permissions
    # get_bin_path will return the first one which is executable
    (fd, fn) = tempfile.mkstemp(prefix='ansible-test-file')
    os.chmod(fn, 0o777)
    (fd, fn1) = tempfile.mkstemp(prefix='ansible-test-file')
    os.chmod(fn1, 0o000)
    (fd, fn2) = tempfile.mkstemp(prefix='ansible-test-file')
    os.chmod(fn2, 0o555)
    (fd, fn3) = tempfile.mkstemp(prefix='ansible-test-file')
   

# Generated at 2022-06-12 23:32:00.101399
# Unit test for function get_bin_path
def test_get_bin_path():
    from ansible.module_utils.common._text import to_bytes

    paths = os.pathsep.join([os.path.join(x, "bin") for x in ("/usr", "/usr/local")])
    os.environ['PATH'] = paths
    os.environ['PATH'] = os.environ.get('PATH', '') + os.pathsep + os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                                                              '../../..'))
    assert get_bin_path('ansible-playbook')
    assert get_bin_path('ansible-playbook', [])
    assert get_bin_path('bash', required=False)
    assert get_bin_path('/bin/bash')

# Generated at 2022-06-12 23:32:12.098080
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import random
    import shutil
    import string
    import stat

    # Create a temp directory
    tmpdir = tempfile.mkdtemp()

    # Create a dummy executable file
    (fd, path) = tempfile.mkstemp(dir=tmpdir)
    f = os.fdopen(fd, "w")
    f.write("#!/bin/bash\n")
    f.close()
    os.chmod(path, 0o755)
    bin_name = os.path.basename(path)

    # Try to find the executable in its parent directory
    assert get_bin_path(bin_name, opt_dirs=[tmpdir]) == path

    # Try to find the executable in the system PATH
    old_path = os.getenv("PATH")
    os.environ["PATH"]

# Generated at 2022-06-12 23:32:19.517240
# Unit test for function get_bin_path
def test_get_bin_path():
    import sys
    import tempfile
    import shutil
    sys.path.insert(0, os.getcwd())

    # test against valid executable
    tempdir = tempfile.mkdtemp()
    valid_executable = os.path.join(tempdir, 'test_executable')
    with open(valid_executable, 'wt') as f:
        f.write('#!/bin/sh\n')
        f.write('echo hello')
    os.chmod(valid_executable, 0o755)

    # search in folder containing executable
    assert get_bin_path('test_executable', opt_dirs=tempdir) == valid_executable
    # search in folder not containing executable

# Generated at 2022-06-12 23:32:36.287922
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test 1: find a system executable
    assert get_bin_path('bash') == '/bin/bash'

    # Test 2: find a system executable in opt_dirs
    assert get_bin_path('bash', opt_dirs=['/bin']) == '/bin/bash'

    # Test 3: find a system executable in /sbin paths
    assert get_bin_path('fdisk') == '/sbin/fdisk'

    # Test 4: executable found in opt_dirs paths
    assert get_bin_path('bash', opt_dirs=['/bin', '/sbin']) == '/bin/bash'

    # Test 5: executable found in opt_dirs paths, before system /sbin paths

# Generated at 2022-06-12 23:32:43.382421
# Unit test for function get_bin_path
def test_get_bin_path():
    from ansible.module_utils._text import to_bytes

    def check(arg, expected):
        try:
            result = get_bin_path(arg)
        except ValueError as e:
            raise ValueError('%s, %s' % (e, arg))
        assert result == expected

    check('sh', to_bytes(os.path.abspath('/bin/sh')))
    check('bash', to_bytes(os.path.abspath('/bin/bash')))
    check('non_existing_file', None)
    check('non_existing_file', None, ['./bin'])
    # An empty path element in PATH is expanded to current directory,
    # and is used to find 'sh' in this unit test.

# Generated at 2022-06-12 23:32:53.031033
# Unit test for function get_bin_path
def test_get_bin_path():
    from ansible.module_utils._text import to_bytes

    def test_executable(path, arg):
        if os.path.exists(path) and not os.path.isdir(path) and is_executable(path):
            return path
        raise ValueError('Failed to find required executable "%s" in paths: %s' % (arg, os.pathsep.join([path])))

    path = '/tmp/foo'
    arg = 'zzzzz'
    try:
        res = get_bin_path(arg)
    except ValueError:
        pass
    else:
        assert False, "Should raise ValueError for %s" % arg
    with open(path, 'w+') as f:
        pass

# Generated at 2022-06-12 23:32:57.435676
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path('this-tool-does-not-exist')
    except ValueError as e:
        assert str(e) == 'Failed to find required executable "this-tool-does-not-exist" in paths: /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'

# Generated at 2022-06-12 23:33:04.660653
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile

    tmpdir = tempfile.gettempdir()

    # Temporary copy of some test file
    fh_dest, fh_dest_name = tempfile.mkstemp(dir=tmpdir)
    with os.fdopen(fh_dest, 'wb') as fh_dest:
        fh_src = open(__file__, 'rb')
        fh_dest.write(fh_src.read())
        fh_src.close()

    # Make sure file is executable
    oldmode = os.stat(fh_dest_name).st_mode
    newmode = (oldmode | 0o111) & 0o7777
    os.chmod(fh_dest_name, newmode)

    # Test file exists
    test_file = os.path.basename(__file__)

# Generated at 2022-06-12 23:33:10.056778
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test that get_bin_path raises an exception if the executable is not found
    got_exception = False
    try:
        _ = get_bin_path('non-existent.sh')
    except ValueError:
        got_exception = True
    assert got_exception

    # Test that get_bin_path returns the full path if the executable is found
    assert get_bin_path('true') == '/bin/true'

# Generated at 2022-06-12 23:33:13.042708
# Unit test for function get_bin_path
def test_get_bin_path():
    mypath = get_bin_path("sh")
    assert os.access(mypath, os.X_OK)

    mypath = get_bin_path("NOSUCHBINARY", opt_dirs=['/bin', '/usr/bin'])

# Generated at 2022-06-12 23:33:23.988708
# Unit test for function get_bin_path
def test_get_bin_path():
    bin_path = get_bin_path('sh')
    assert isinstance(bin_path, str)
    assert os.path.sep in bin_path
    assert is_executable(bin_path) == True

    opt_dirs = ['/bin','/usr/local/bin']
    bin_path = get_bin_path('sh', opt_dirs=opt_dirs)
    assert isinstance(bin_path, str)
    assert os.path.sep in bin_path
    assert is_executable(bin_path) == True

    opt_dirs = ['/bin/sh','/usr/bin']
    bin_path = get_bin_path('sh', opt_dirs=opt_dirs)
    assert isinstance(bin_path, str)
    assert os.path.sep in bin_

# Generated at 2022-06-12 23:33:32.538453
# Unit test for function get_bin_path
def test_get_bin_path():
    # set PATH to temp dir
    import tempfile
    tmpdir = tempfile.mkdtemp()
    os.environ['PATH'] = tmpdir

    # test command not found
    try:
        get_bin_path("nonexistent")
    except ValueError:
        pass
    else:
        raise Exception("failed to raise exception for non-existent command")

    # test command found
    try:
        fname = os.path.join(tmpdir, "foo")
        f = open(fname, "w")
        f.write("#!/bin/sh\nexit 0")
        f.close()
        os.chmod(fname, 0o755)
        result = get_bin_path("foo")
    except ValueError:
        raise Exception("failed to find foo command")

    # compare result to expected


# Generated at 2022-06-12 23:33:44.471163
# Unit test for function get_bin_path
def test_get_bin_path():
    # Try to get some executable, while dealing with broken PATH
    # (Usually /usr/bin is not in PATH)
    from ansible.module_utils._text import to_bytes

    # save original PATH for later restore
    old_path = os.environ.get("PATH")

    # clear PATH and check if get_bin_path raise the ValueError
    os.environ["PATH"] = ""
    try:
        get_bin_path("ls")
        assert(False)
    except ValueError:
        assert(True)

    # mangle PATH so that /usr/bin is not included
    os.environ["PATH"] = "/bin"
    result = get_bin_path("ls")
    assert(result == "/bin/ls")

    # Restore PATH
    os.environ["PATH"] = old_path

# Generated at 2022-06-12 23:33:58.080543
# Unit test for function get_bin_path
def test_get_bin_path():

    assert get_bin_path('ls') is not None
    assert get_bin_path(['ls']) is not None

    try:
        get_bin_path('notfound')
    except ValueError as e:
        assert "Failed to find required executable" in str(e)

# Generated at 2022-06-12 23:34:03.410809
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test binary is found in PATH
    assert get_bin_path('ls') == '/bin/ls'
    assert get_bin_path('ls', opt_dirs=['/opt/bin']) == '/bin/ls'
    assert get_bin_path('ls', opt_dirs=[]) == '/bin/ls'
    assert get_bin_path('ls', opt_dirs=None) == '/bin/ls'

    # Specifying opt_dirs overrides PATH
    assert get_bin_path('ls', opt_dirs=['/bin']) == '/bin/ls'
    assert get_bin_path('ls', opt_dirs=['/bin', '/opt/bin']) == '/bin/ls'

    # We don't find anything in PATH so we look in opt_dirs

# Generated at 2022-06-12 23:34:08.786147
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('echo') == '/bin/echo'
    assert get_bin_path('which') == '/usr/bin/which'

    # Test with bin as path
    test_bin = '/usr/bin/foo'
    with open(test_bin, 'w') as f:
        f.write('')
    assert get_bin_path('foo', opt_dirs=['/usr/bin']) == test_bin
    os.remove(test_bin)

    # Test with bin in PATH
    os.environ['PATH'] = '/usr/bin:/usr/sbin'
    test_bin = '/usr/sbin/foo'
    with open(test_bin, 'w') as f:
        f.write('')
    assert get_bin_path('foo') == test_bin
    os

# Generated at 2022-06-12 23:34:17.132002
# Unit test for function get_bin_path
def test_get_bin_path():
    # Executables on the PATH
    assert(get_bin_path('awk') == '/usr/bin/awk')
    assert(get_bin_path('curl') == '/usr/bin/curl')
    assert(get_bin_path('grep') == '/usr/bin/grep')
    assert(get_bin_path('ping') == '/bin/ping')
    assert(get_bin_path('python') == '/usr/bin/python')
    assert(get_bin_path('rsync') == '/usr/bin/rsync')
    assert(get_bin_path('scp') == '/usr/bin/scp')
    assert(get_bin_path('ssh') == '/usr/bin/ssh')
    assert(get_bin_path('sudo') == '/usr/bin/sudo')

# Generated at 2022-06-12 23:34:20.849614
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('sh') == '/bin/sh'
    assert get_bin_path('true') == '/bin/true'
    assert get_bin_path('false') == '/bin/false'

# Generated at 2022-06-12 23:34:30.039915
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil
    import stat

    # make a temp dir that is in the path
    bin_dir = tempfile.mkdtemp()
    bin_path = os.path.join(bin_dir, 'bin')
    fd = open(bin_path, 'w')
    fd.close()
    os.chmod(bin_path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR )
    os.environ['PATH'] = "%s:%s" % (os.environ['PATH'], bin_dir)

    # try to find the file
    found_path = get_bin_path('bin')
    assert found_path == bin_path

    # try to find a file that isn't there

# Generated at 2022-06-12 23:34:39.936461
# Unit test for function get_bin_path
def test_get_bin_path():
    '''
    Test get_bin_path function
    '''
    # find system executable
    bin_path = get_bin_path('cat')
    assert os.path.exists(bin_path)
    assert not os.path.isdir(bin_path)
    assert is_executable(bin_path)
    # Should raise an error (file does not exist)
    try:
        bin_path = get_bin_path('bogus', required=True)
        raise AssertionError('get_bin_path did not error when searching for a non-existent executable')
    except ValueError as e:
        assert 'Failed to find required executable' in str(e)
    # Shorten the PATH
    old_env = os.environ.get('PATH')
    os.environ['PATH'] = '/bin'


# Generated at 2022-06-12 23:34:46.455296
# Unit test for function get_bin_path
def test_get_bin_path():
    ''' Check the get_bin_path function. '''

    import shutil
    import tempfile

    # Create a temp directory and a fake executable.
    tmpdir = tempfile.mkdtemp()
    fake_executable = os.path.join(tmpdir, 'fake_executable')
    open(fake_executable, 'w').write('')
    os.chmod(fake_executable, 0o755)

    # Try the fake executable within the temporary directory with full path.
    # Should be found.
    try:
        assert get_bin_path(fake_executable, []) == fake_executable
    except Exception:
        assert False, 'Failed to find %s by full path.' % fake_executable

    # Try the fake executable within the temporary directory without full path.
    # Should be found.
   

# Generated at 2022-06-12 23:34:55.527478
# Unit test for function get_bin_path
def test_get_bin_path():
    from tempfile import mkdtemp
    from shutil import rmtree
    from os import mkdir
    from os.path import join, exists
    from sys import executable

    # Create a tmp dir with a known executable to find, and another file
    tmpdir = mkdtemp()
    mkdir(join(tmpdir, 'sbin'))
    mkdir(join(tmpdir, 'other'))
    open(join(tmpdir, 'sbin', 'exectest'), 'w').close()
    open(join(tmpdir, 'other', 'filetest'), 'w').close()
    mkdir(join(tmpdir, 'empty'))
    old_path = os.environ['PATH']
    os.environ['PATH'] = tmpdir + os.pathsep + join(tmpdir, 'sbin') + os.pathse

# Generated at 2022-06-12 23:35:04.394929
# Unit test for function get_bin_path
def test_get_bin_path():
    """
    Test the get_bin_path function.

    This test should pass if get_bin_path returns the path
    to /bin/pwd, and should raise an exception if it is unable
    to find an executable.
    """
    import sys
    import inspect
    import platform
    from ansible.module_utils.common.file import get_bin_path

    def path_to_pwd():
        """
        Return the path to pwd.

        Under different platform, pwd can be in different places.
        Under Windows, there either is no pwd, or it is in C:\Windows\System32.
        """
        if sys.platform.startswith('win'):
            pwd = 'C:\\Windows\\System32\\pwd'
        elif sys.platform.startswith('darwin'):
            p

# Generated at 2022-06-12 23:35:33.927086
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('python') == '/usr/bin/python'
    assert get_bin_path('python', opt_dirs=['/usr/local/bin']) == '/usr/local/bin/python'
    assert get_bin_path('python', opt_dirs=['/usr/local/bin', '/usr']) == '/usr/bin/python'
    try:
        get_bin_path('python', opt_dirs=['/usr/local/bin', '/usr/local'])
        assert False, 'Expected exception'
    except ValueError:
        pass
    try:
        get_bin_path('non_existing_executable')
        assert False, 'Expected exception'
    except ValueError:
        pass

if __name__ == '__main__':
    test_get_bin_

# Generated at 2022-06-12 23:35:45.857667
# Unit test for function get_bin_path
def test_get_bin_path():
    d = os.path.dirname(os.path.abspath(__file__))

    # test_path has no executable files
    test_path = os.path.join(d, "bin")
    try:
        get_bin_path('ansible-test-executable', opt_dirs=[test_path])
    except ValueError:
        pass
    else:
        raise AssertionError("get_bin_path() did not fail with non-executable file ansible-test-executable")

    # test_path has executable file: ansible-test-executable
    test_path = os.path.join(d, "bin", "executable")
    r = get_bin_path('ansible-test-executable', opt_dirs=[test_path])

# Generated at 2022-06-12 23:35:51.174491
# Unit test for function get_bin_path
def test_get_bin_path():
    # Returns executable if it is in the PATH
    assert get_bin_path('/bin/echo') == '/bin/echo'
    # Throws exception if executable is not in the PATH
    try:
        get_bin_path('cant_find_this', required=True)
        assert False
    except ValueError:
        pass

    # Returns executable if it is in the additional directories
    assert get_bin_path('touch', opt_dirs=['/bin', '/usr/bin']) == '/bin/touch'
    # Returns executable if it is in the PATH and additional directories
    assert get_bin_path('echo', opt_dirs=['/bin', '/usr/bin']) == '/bin/echo'
    # Throws exception if executable is not in the PATH and additional directories

# Generated at 2022-06-12 23:35:54.128351
# Unit test for function get_bin_path
def test_get_bin_path():
    # Tests are run in the top level directory of the project, therefore PATH
    # includes 'bin'
    bin_path = get_bin_path('ansible')
    assert is_executable(bin_path)

# Generated at 2022-06-12 23:35:57.197886
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('echo') == '/bin/echo'
    assert get_bin_path('echo', ['/tmp']) == '/bin/echo'
    assert get_bin_path('echo', ['/bin/echo']) == '/bin/echo'
    assert get_bin_path('echo', ['/bin/echo', '/tmp']) == '/bin/echo'
    assert get_bin_path('foo') is None

# Generated at 2022-06-12 23:35:59.567545
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('ls') is not None
    assert get_bin_path('blarg') is None

# Unit tests for deprecated argument required

# Generated at 2022-06-12 23:36:06.308348
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil
    import subprocess
    import sys
    import stat

    # Create test dir and file
    bin_dir = tempfile.mkdtemp()
    bin_file = os.path.join(bin_dir, 'ansible')
    with open(bin_file, 'w') as f:
        f.write('''#!/bin/sh
echo "test"
''')
    os.chmod(bin_file, stat.S_IXUSR)

    # Set PATH
    os.environ['PATH'] = bin_dir

    # Test if command found
    res = get_bin_path('ansible')
    assert os.path.exists(res) and os.path.isfile(res)

    # Test if command with path found

# Generated at 2022-06-12 23:36:07.293241
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('git') == '/usr/bin/git'

# Generated at 2022-06-12 23:36:17.483119
# Unit test for function get_bin_path
def test_get_bin_path():
    paths = []
    path = get_bin_path('ls')
    assert path
    assert os.path.exists(path)
    assert is_executable(path)
    assert path.endswith('ls')
    assert path == get_bin_path('ls')
    paths = ['/bin', '/usr/bin']
    path = get_bin_path('ls', paths)
    assert path
    assert os.path.exists(path)
    assert is_executable(path)
    assert path.endswith('ls')
    assert path == get_bin_path('ls', paths)

    try:
        get_bin_path('moo')
    except ValueError:
        pass
    else:
        assert False, "This should raise a ValueError"


# Generated at 2022-06-12 23:36:20.252302
# Unit test for function get_bin_path
def test_get_bin_path():
    # is_executable must work properly in order for this test to work
    assert get_bin_path("touch") is not None
    assert get_bin_path("/bin/touch") is not None

# Generated at 2022-06-12 23:36:48.815866
# Unit test for function get_bin_path
def test_get_bin_path():
    import tempfile
    import shutil

    tmp = tempfile.mkdtemp()
    assert get_bin_path('ls') == '/bin/ls'
    assert get_bin_path('ls', [tmp]) == '/bin/ls'

    f = open(os.path.join(tmp, 'ls'), 'w')
    f.write('foo')
    f.close()
    assert get_bin_path('ls', [tmp]) == '/bin/ls'

    f = open(os.path.join(tmp, 'ls'), 'w')
    f.write('foo')
    f.close()

# Generated at 2022-06-12 23:36:54.645695
# Unit test for function get_bin_path
def test_get_bin_path():
    import pytest

    # Test that correct path is returned
    assert get_bin_path('python') == '/usr/bin/python'

    # Test that required results in ValueError
    with pytest.raises(ValueError, match='Failed to find required executable "python3" in paths: .*'):
        get_bin_path('python3')

    # Test that optional path is included in search
    assert get_bin_path('python3', opt_dirs=['/bin']) == '/bin/python3'

    # Test that opt_dirs overrides path
    assert get_bin_path('python3', opt_dirs=['/bin']) == '/bin/python3'

# Generated at 2022-06-12 23:37:06.976931
# Unit test for function get_bin_path
def test_get_bin_path():

    # Test for invalid argument
    try:
        expected_output = get_bin_path('khsjkfstrrcs')
        assert False, "Invalid executable should fail: %s" % expected_output
    except ValueError:
        assert True

    # Test if executable exists in the PATH
    expected_output = get_bin_path('echo')
    assert expected_output is not None

    # Test if executable exists in custom PATH
    expected_output = get_bin_path('ls', opt_dirs=['/bin'])
    assert expected_output is not None

    # Test if executable exists in custom PATH
    expected_output = get_bin_path('ifconfig', opt_dirs=['/sbin'])
    assert expected_output is not None

    # Test for invalid executable in custom PATH

# Generated at 2022-06-12 23:37:18.073734
# Unit test for function get_bin_path
def test_get_bin_path():
    exclude_paths = ['/usr/bin/python2.6', '/usr/bin/python2.7', '/usr/bin/python']
    for p in exclude_paths:
        try:
            test_paths = ['/usr/bin']
            if os.path.exists(p):
                test_paths.append(p)
            assert get_bin_path('python', test_paths) == '/usr/bin/python'
        except ValueError as ex:
            assert 'Failed to find required executable "python"' in str(ex)
    assert get_bin_path('python', ['/usr/bin/python2.7']) == '/usr/bin/python2.7'

# Generated at 2022-06-12 23:37:24.026127
# Unit test for function get_bin_path
def test_get_bin_path():
    # Test with missing exec
    try:
        path1 = get_bin_path('MISSING_FILE')
        assert(False)
    except ValueError:
        pass

    # Test with existing, executable file
    path2 = get_bin_path('/bin/pwd')
    assert(path2 == '/bin/pwd')

    # Test with additional directories
    path3 = get_bin_path('bash', ['/bin', '/usr/bin'])
    assert(path3 == '/bin/bash')

# Generated at 2022-06-12 23:37:30.092441
# Unit test for function get_bin_path
def test_get_bin_path():
    assert get_bin_path('/bin/ls') == '/bin/ls'
    assert get_bin_path('ls') == '/bin/ls'
    assert get_bin_path('ls', opt_dirs=['/bin']) == '/bin/ls'
    try:
        get_bin_path('ls', opt_dirs=['/usr/bin'])
        assert False, 'Did not get expected exception'
    except ValueError:
        pass
    try:
        get_bin_path('/bin/ls', opt_dirs=['/usr/bin'])
        assert False, 'Did not get expected exception'
    except ValueError:
        pass

# Generated at 2022-06-12 23:37:36.961057
# Unit test for function get_bin_path
def test_get_bin_path():
    try:
        get_bin_path('/usr/bin/netstat')
        assert True
    except ValueError:
        assert False

    try:
        get_bin_path('bogus_prog')
        assert False
    except ValueError:
        assert True

    try:
        get_bin_path('bogus_prog', required=True)
        assert False
    except ValueError:
        assert True