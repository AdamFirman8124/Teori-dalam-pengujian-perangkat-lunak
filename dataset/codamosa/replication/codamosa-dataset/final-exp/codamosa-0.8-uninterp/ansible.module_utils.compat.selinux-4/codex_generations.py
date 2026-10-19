

# Generated at 2022-06-12 23:59:09.548118
# Unit test for function matchpathcon
def test_matchpathcon():
    print(matchpathcon('/usr/bin/passwd', 0))


if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-12 23:59:21.762262
# Unit test for function matchpathcon
def test_matchpathcon():
    import os
    import tempfile

    # create directory with context
    tempdir = tempfile.mkdtemp()
    rc, con = _selinux_lib.lgetfilecon(tempdir)
    if rc < 0:
        # if getfilecon fails, we can't continue with the unittest
        print('Command lgetfilecon failed')
        exit(0)

    # create file in tempdir
    test_file = tempfile.NamedTemporaryFile(dir=tempdir)

    # since we are here, we can delete the temporary directory
    os.rmdir(tempdir)

    # try to get the context of the file
    rc, con = _selinux_lib.lgetfilecon(test_file.name)

# Generated at 2022-06-12 23:59:25.431465
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (rc, con) = lgetfilecon_raw("/etc/passwd")
    if rc >= 0:
        print("con={}".format(con))
    else:
        print("rc={}, errno={}".format(rc, get_errno()))



# Generated at 2022-06-12 23:59:35.488468
# Unit test for function matchpathcon

# Generated at 2022-06-12 23:59:45.467877
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import stat
    import tempfile
    testfile = tempfile.NamedTemporaryFile()
    testfile_path = testfile.name
    testfile.close()
    testfile_stat = os.stat(testfile_path)
    context = lgetfilecon_raw(testfile_path)
    assert type(context[0]) == int
    assert type(context[1]) == str
    assert context[0] == 0
    # Assert the context string is in the form: type:role:level
    assert context[1].count(':') == 2
    os.chmod(testfile_path, stat.S_IWRITE)
    os.remove(testfile_path)


# Generated at 2022-06-12 23:59:53.737614
# Unit test for function matchpathcon
def test_matchpathcon():
    assert matchpathcon('/tmp', 0) == [0, 'system_u:object_r:tmp_t:s0']
    assert matchpathcon('/dev/shm', 0) == [0, 'system_u:object_r:tmpfs_t:s0']
    assert matchpathcon('/dev/sda1', 0) == [0, 'system_u:object_r:blk_file_t:s0']
    assert matchpathcon('/dev/disk/by-label/BOOT', 0) == [0, 'system_u:object_r:blk_file_t:s0']

# Generated at 2022-06-12 23:59:57.400867
# Unit test for function matchpathcon
def test_matchpathcon():
    path = b'/tmp'
    mode = 0
    rc, result = matchpathcon(path, mode)
    assert rc == 0
    assert result == 'system_u:object_r:tmp_t:s0'


# Generated at 2022-06-13 00:00:00.397490
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = '/'

    rc, con = lgetfilecon_raw(path)
    assert rc == 0
    assert 'system_u:object_r:root_t:s0' in con



# Generated at 2022-06-13 00:00:02.330717
# Unit test for function matchpathcon
def test_matchpathcon():
    assert matchpathcon(b'/etc/shadow', 0) == [0, b'system_u:object_r:shadow_t:s0']

# Generated at 2022-06-13 00:00:11.455285
# Unit test for function matchpathcon
def test_matchpathcon():
    # selinux disabled
    def disabled():
        # returns -1 and errno set to ENOENT
        rc, con = matchpathcon('/toys/doesnotexist', 0)
        assert rc == -1
        assert len(con) == 0

    # selinux enabled
    def enabled():
        # returns 0
        rc, con = matchpathcon('/toys/doesnotexist', 0)
        assert rc == 0
        assert con == 'unlabeled'

    old = security_getenforce()
    try:
        security_setenforce(0)
        disabled()
        security_setenforce(1)
        enabled()
    finally:
        security_setenforce(old)



# Generated at 2022-06-13 00:00:22.367730
# Unit test for function matchpathcon
def test_matchpathcon():
    # path = os.path.abspath(__file__)
    # [rc1, con1] = matchpathcon(path, 0)
    # assert rc1 == 0
    path = '/usr/sbin/ntpd'
    [rc2, con2] = matchpathcon(path, 0)
    assert rc2 == 0
    path = '/usr/sbin/ntpd_test'
    [rc3, con3] = matchpathcon(path, 1)
    assert rc3 == 0
    path = os.path.join(os.path.expanduser('~'), "test_matchpathcon.txt")
    [rc4, con4] = matchpathcon(path, 1)
    assert rc4 == 0
    # with open(path, 'wb') as f:
    #     f.write(b'

# Generated at 2022-06-13 00:00:25.669850
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    testpath = '/etc/passwd'
    rc, context = lgetfilecon_raw(testpath)
    assert rc == 0
    assert context == 'system_u:object_r:etc_runtime_t:s0'



# Generated at 2022-06-13 00:00:27.229368
# Unit test for function matchpathcon
def test_matchpathcon():
    context = matchpathcon('/var/log/messages', 0)[1]
    print(context)

# Generated at 2022-06-13 00:00:32.201271
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import json
    import os

    # Make sure the file exists before we run tests
    fname = "test_file"
    open(fname, "a").close()

    test_con = ("system_u:object_r:usr_t:"
                "s0")
    try:
        lsetfilecon(fname, test_con)
        result = lgetfilecon_raw(fname)
        assert type(result) == list
        assert len(result) == 2
        assert result[0] == 0
        assert result[1] == test_con
    finally:
        os.remove(fname)


# Generated at 2022-06-13 00:00:41.986785
# Unit test for function matchpathcon
def test_matchpathcon():
    # The directory and file paths must be absolute
    home_path = os.getenv('HOME')
    test_dir = os.path.join(home_path, 'test_dir')
    test_file = os.path.join(test_dir, 'test_file')

    # Attempt to get context on the file, should fail
    assert matchpathcon(test_file, 0)[0] == -1

    # Create the path
    os.makedirs(test_dir)

    # Should fail again, since path does not exist
    assert matchpathcon(test_file, 0)[0] == -1

    # Create the file
    open(test_file, 'a').close()

    # Should succeed
    assert matchpathcon(test_file, 0)[0] == 0



# Generated at 2022-06-13 00:00:44.038559
# Unit test for function matchpathcon
def test_matchpathcon():
    path = b"/etc/shadow"
    mode = 0
    rc, con = matchpathcon(path, mode)
    assert rc == 0
    assert con == b"system_u:object_r:shadow_t"

# Generated at 2022-06-13 00:00:45.606638
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = b"/etc/passwd"
    assert lgetfilecon_raw(path)[1] == "unconfined_u:object_r:user_home_t:s0"


# Generated at 2022-06-13 00:00:54.515769
# Unit test for function matchpathcon
def test_matchpathcon():
    import tempfile

    dirpath = tempfile.mkdtemp()
    try:
        with open(os.path.join(dirpath, 'testfile'), 'w') as f:
            f.write('test data')

        rc, con = matchpathcon(dirpath, 0)
        assert rc == 0, 'rc={}'.format(rc)
        rc, con = matchpathcon(os.path.join(dirpath, 'testfile'), 0)
        assert rc == 0, 'rc={}'.format(rc)
    finally:
        import shutil
        shutil.rmtree(dirpath)

if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-13 00:01:02.885082
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    from tempfile import mkstemp
    from shutil import rmtree
    from os import close, remove, stat, mkdir, chdir, getcwd
    from os.path import basename
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.selinux import lgetfilecon_raw

    fd, tmpfile = mkstemp()
    close(fd)


# Generated at 2022-06-13 00:01:06.837399
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    testpath = "/etc/passwd"
    testcon = 'system_u:object_r:passwd_file_t:s0'

    [rc, con] = lgetfilecon_raw(testpath)
    assert con == testcon


# Generated at 2022-06-13 00:01:16.559808
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    from ansible.module_utils.selinux import _selinux_lib
    _selinux_lib.is_selinux_enabled.restype = c_int
    rc, enabled = _selinux_lib.is_selinux_enabled()
    assert rc == 0, "unexpected return value"
    if not enabled:
        return
    rc, con = lgetfilecon_raw("/etc")
    assert rc == 0, "unexpected return value"
    assert con, "unexpected return value"
    assert con.startswith("system_u:"), "unexpected return value"
    assert con.endswith(":object_r:etc_t"), "unexpected return value"
    return



# Generated at 2022-06-13 00:01:21.740212
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import sys

    if sys.platform != 'linux':
        raise RuntimeError('selinux module not supported on platform: {0}'.format(sys.platform))

    rc, con = lgetfilecon_raw('/etc/passwd')
    assert rc == 0
    assert con
    assert con.startswith('system_u:object_r:etc_t:s0')

# Generated at 2022-06-13 00:01:27.773014
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    from os import path
    from random import choice

    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.selinux import lgetfilecon_raw, is_selinux_enabled

    if not is_selinux_enabled():
        raise Exception('Function lgetfilecon_raw unit test not possible when SELinux is disabled')

    # if /tmp is mounted on tmpfs, then it will not have a SELinux label
    temp_file = path.join(choice(('/tmp', '/var/tmp')), 'ansible_test_file_%012d' % choice(range(0, 0xFFFFFF)))

    with open(temp_file, 'w+') as f:
        f.write('Test for function lgetfilecon_raw')


# Generated at 2022-06-13 00:01:33.398933
# Unit test for function matchpathcon
def test_matchpathcon():
    from ansible.module_utils.selinux_common import test_selinux_policies
    _thismod = sys.modules[__name__]
    for test in test_selinux_policies:
        if test.get('test_matchpathcon', False):
            rc, con = _thismod.matchpathcon(test['path'], 1)
            assert rc == test['result']
            assert con == test['context']

# Generated at 2022-06-13 00:01:36.247007
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    test_file = "/etc/selinux/config"
    [rc, con_value] = lgetfilecon_raw(test_file)
    assert rc == 0
    assert con_value == "system_u:object_r:etc_t:s0"


# Generated at 2022-06-13 00:01:36.677423
# Unit test for function matchpathcon
def test_matchpathcon():
    pass

# Generated at 2022-06-13 00:01:42.077215
# Unit test for function matchpathcon
def test_matchpathcon():
    filename = '/tmp/testfile'
    p1 = matchpathcon(filename, 0)
    print(filename, p1)
    p2 = matchpathcon(filename, os.R_OK)
    print(filename, p2)
    p3 = matchpathcon(filename, os.R_OK | os.W_OK)
    print(filename, p3)
    p3 = matchpathcon(filename, os.R_OK | os.W_OK | os.X_OK)
    print(filename, p3)

# Generated at 2022-06-13 00:01:49.690040
# Unit test for function matchpathcon
def test_matchpathcon():

    # Test positive matchpathcon call
    path = os.path.join(os.sep, "tmp")
    mode = 0o777
    rc, out = matchpathcon(path, mode)
    assert rc == 0 and out == "user_tmp_t"

    # Test negative matchpathcon call
    path = os.path.join(os.sep, "tmp", "missing")
    rc, out = matchpathcon(path, mode)
    assert rc == -1

if __name__ == '__main__':
    sys.exit(test_matchpathcon())

# Generated at 2022-06-13 00:01:52.598696
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    [rc, con] = lgetfilecon_raw("/proc/1/task/1/attr/current")
    if rc == 0:
        assert con == "system_u:system_r:init_t:SystemLow-SystemHigh"
    if rc < 0:
        raise OSError


# Generated at 2022-06-13 00:01:56.871147
# Unit test for function matchpathcon
def test_matchpathcon():
    """
    Unit test for selinux python module function matchpathcon
    """

    # This returns a context of "system_u:object_r:init_exec_t:s0" on CentOS 7.
    conn_tuple = matchpathcon('/init', 0)
    assert conn_tuple[0] == 0, conn_tuple[1]
    assert conn_tuple[1] == "system_u:object_r:init_exec_t:s0"

    # This should fail cleanly because SELinux is disabled.
    conn_tuple = matchpathcon('/nonexistant', 0)
    assert conn_tuple[0] == -1
    assert conn_tuple[1] == "Not running in enabled SELinux context"

    # This should also fail since the file doesn't exist.
    conn

# Generated at 2022-06-13 00:02:02.289318
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    s = lgetfilecon_raw(b'/')
    assert len(s) == 2
    assert s[0] == 0, "Return value should be 0"
    assert s[1].startswith('system_u:object_r:root_t')


# Generated at 2022-06-13 00:02:05.006382
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw('/')
    assert rc == 0
    assert con == 'system_u:object_r:root_t:s0'


# Generated at 2022-06-13 00:02:11.079320
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (rc1, con1) = lgetfilecon_raw("/usr/bin/python\0")
    if rc1 == -1:
        print("Error: %s" % con1)
    else:
        print("con: %s" % con1)



# Generated at 2022-06-13 00:02:14.650900
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import os

    testpath = os.path.abspath(__file__)

    [rc, con] = lgetfilecon_raw(testpath)
    assert rc == 0, 'Failed to retrieve context'
    assert len(con) > 5, 'Returned invalid context'


# Generated at 2022-06-13 00:02:21.458596
# Unit test for function matchpathcon
def test_matchpathcon():
    if sys.version_info >= (3, 6):
        # ensure that a tmpdir with a leading \\ is correctly escaped
        import tempfile

        with tempfile.TemporaryDirectory(prefix='\\') as d:
            path = d + '/some/deep/path'
            try:
                os.makedirs(path)
            except OSError as e:
                if e.errno != 17:  # 17 == directory exists
                    raise e
            assert matchpathcon(path, 0)[-1] == '?\t?\t?\t'

# Generated at 2022-06-13 00:02:27.749257
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert len(lgetfilecon_raw(b'/bin/bash')) == 2
    assert isinstance(lgetfilecon_raw(b'/bin/bash')[1], str)
    assert len(lgetfilecon_raw(b'/sbin/udevadm')) == 2
    assert isinstance(lgetfilecon_raw(b'/sbin/udevadm')[1], str)


# Generated at 2022-06-13 00:02:36.310804
# Unit test for function matchpathcon
def test_matchpathcon():
    import os

    # Test with a directory
    # [1:2:3:4:5:6:7:8:9::] is a directory context
    context = 'system_u:object_r:bin_t:s0:c1,c2,c3,c4,c5,c6,c7,c8,c9,c0'
    (rc, con) = matchpathcon('/bin', 0)
    assert rc == 0
    assert con == context

    # Test with a file
    # [1:2:3:4:5:6:7:8:9::] is a directory context

# Generated at 2022-06-13 00:02:38.255414
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():

    assert lgetfilecon_raw('/etc/passwd')[1] == 'system_u:object_r:passwd_file_t:s0'

# Generated at 2022-06-13 00:02:44.173497
# Unit test for function matchpathcon
def test_matchpathcon():
    to_native = AnsibleModule._ansible_module.to_native
    if matchpathcon("/etc/passwd",0)[0] == 0:
        assert to_native(matchpathcon("/etc/passwd",0)[1]) == "system_u:object_r:etc_t:s0"
    else:
        assert to_native(matchpathcon("/etc/passwd",0)[1]) == "unconfined_u:object_r:unlabeled_t:s0"

# Generated at 2022-06-13 00:02:48.525898
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    TEST_FILE = 'test_file'
    rc, con = lgetfilecon_raw(TEST_FILE)
    assert rc == 0
    assert con == 'system_u:object_r:unlabeled_t:s0'

# Generated at 2022-06-13 00:02:54.628232
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    c = lgetfilecon_raw("/bin/ls")
    assert c[0] == 0

# Generated at 2022-06-13 00:03:02.589234
# Unit test for function matchpathcon
def test_matchpathcon():
    # Note: the default context for file '/etc/passwd' is 'system_u:object_r:passwd_file_t:s0'
    try:
        [rc, con] = matchpathcon('/etc/passwd', 0)
    except OSError as e:
        # When file '/etc/passwd' is not found
        if e.errno == 2:
            return False
        raise e
    except:
        raise
    if con != 'system_u:object_r:passwd_file_t:s0':
        raise AssertionError('The default context for file /etc/passwd is not correct')
    return True


# Generated at 2022-06-13 00:03:06.028561
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    result = lgetfilecon_raw('/etc/hosts')
    assert isinstance(result, list)
    assert result[0] == 0
    assert result[1] == 'system_u:object_r:etc_t:s0'

# Generated at 2022-06-13 00:03:10.884375
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Run if the function is available
    if 'lgetfilecon_raw' in globals():
        assert lgetfilecon_raw('/etc/') == [0, 'system_u:object_r:etc_t:s0']
    # Fail if the function isn't available
    else:
        raise ImportError('module must define a lgetfilecon_raw function')

# Generated at 2022-06-13 00:03:12.305138
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (rc, con) = lgetfilecon_raw("/proc")
    assert rc == 0
    assert con != "<<none>>"
    assert con == "system_u:object_r:proc_t:s0"


# Generated at 2022-06-13 00:03:21.062060
# Unit test for function matchpathcon
def test_matchpathcon():
    """
    Python code to test all the functions
    matchpathcon, selinux_getpolicytype, selinux_getenforcemode,
    security_policyvers, is_selinux_enabled, is_selinux_mls_enabled
    Returns:
        None
    """

    rc, con = matchpathcon(b"/etc", 0)
    print("matchpathcon rc, con value: {0}, {1}".format(rc, con))
    rc, policy_type = selinux_getpolicytype()
    print("selinux_getpolicytype rc, policy_type value: {0}, {1}".format(rc, policy_type))
    rc, enforcemode = selinux_getenforcemode()

# Generated at 2022-06-13 00:03:29.265160
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    """
    Enables SELinux checking for Django and sets the context for project directory
    :return:
    """

    from ansible.module_utils.selinux import lgetfilecon_raw

    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
    import django
    django.setup()

    assert lgetfilecon_raw('/home/devops/django_app/')[1] == 'system_u:object_r:user_home_t:s0'

# Generated at 2022-06-13 00:03:32.948753
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (rc, con) = lgetfilecon_raw('/dev/null')
    assert rc >= 0
    assert isinstance(con, str)
    (rc, con) = lgetfilecon_raw('/selinux_test')
    assert rc == -1
    assert isinstance(con, str)
    (rc, con) = lgetfilecon_raw('/tmp/doesnotexist')
    assert rc == -1
    assert isinstance(con, str)


# Generated at 2022-06-13 00:03:40.778260
# Unit test for function matchpathcon
def test_matchpathcon():
    from ansible.module_utils.selinux import matchpathcon, SELINUX_DEFAULT

    path = '/tmp'
    mode = SELINUX_DEFAULT

    if os.access(path, os.R_OK):
        rc, con = matchpathcon(path, mode)
        print('matchpathcon({0}, {1}) -> {2:d}, {3}'.format(path, mode, rc, con))
    else:
        print('{0} inaccessible'.format(path))



# Generated at 2022-06-13 00:03:43.649471
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    file_path = "/etc/selinux/selinux.conf"
    assert lgetfilecon_raw(file_path) == [0, 'system_u:object_r:etc_t:s0']


# Generated at 2022-06-13 00:03:54.996933
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = "/etc/selinux/config"
    rc, con = _selinux_lib.lgetfilecon_raw(path, None)
    assert con == b"system_u:object_r:selinux_config_t:SystemLow"


# Generated at 2022-06-13 00:04:00.097727
# Unit test for function matchpathcon
def test_matchpathcon():
    _selinux_lib.matchpathcon.restype = c_int
    path = "var/lib/rpm/Packages"
    mode = 0o644
    con = c_char_p()
    rc = _selinux_lib.matchpathcon(path, mode, byref(con))
    print(rc)
    if con:
        print(con.value)
        _selinux_lib.freecon(con)

# Generated at 2022-06-13 00:04:07.545987
# Unit test for function matchpathcon
def test_matchpathcon():
    test_con = to_bytes('system_u:object_r:user_cron_spool_t:s0')
    test_path = to_bytes('/etc/cron.d/root')
    rc, con = matchpathcon(test_path, 0)
    assert rc == 0, 'expected return code 0, got {0}'.format(rc)
    assert con == test_con, 'expected con {0}, got {1}'.format(test_con, con)



# Generated at 2022-06-13 00:04:12.371100
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Create a temporary test file
    with open('testfile', 'w') as f:
        f.write('this is a test file')

    # Check that it was created
    assert os.path.isfile('testfile')

    # Get the context of the test file
    con = lgetfilecon_raw('testfile')

    # Check that the test file has a context
    assert con[0] == 0
    assert con[1] is not None

    # Clean up the test file
    os.remove('testfile')

# Generated at 2022-06-13 00:04:14.873053
# Unit test for function matchpathcon
def test_matchpathcon():
    mode = os.stat('/').st_mode
    error_len, con = matchpathcon('/', mode)
    print("Matchpathcon: {}".format(con))
    error_len, con = matchpathcon('/home/vagrant', mode)
    print("Matchpathcon: {}".format(con))



# Generated at 2022-06-13 00:04:17.493618
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw(_thismod.__file__) == [0, "unconfined_u:object_r:etc_t:s0"]


# Generated at 2022-06-13 00:04:21.949897
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    ctx = lgetfilecon_raw(b'/proc/cpuinfo')
    if ctx[0] == 0: # success
        print('+ file context for /proc/cpuinfo : {0}'.format(ctx[1]))
    else:
        print('- failed with errno {0}'.format(ctx[0]))


# Generated at 2022-06-13 00:04:30.221324
# Unit test for function matchpathcon
def test_matchpathcon():
    if not is_selinux_enabled():
        # If SELinux is disabled this function is useless
        # and will always return -1 / ENOTSUP
        return

    path = '/etc/shadow'
    mode = os.stat(path).st_mode
    (rc, con) = matchpathcon(path, mode)
    if rc == -1:
        errno = get_errno()
        raise OSError(errno, os.strerror(errno))

    print('Context for {0} is {1}'.format(path, con))


# Generated at 2022-06-13 00:04:35.855588
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = 't.txt'
    returned_rc, returned_con = lgetfilecon_raw(path)
    assert returned_rc == 0, 'lgetfilecon_raw failed, returned code: {}'.format(returned_rc)
    assert returned_con == 'system_u:object_r:tmp_t:s0', 'lgetfilecon_raw failed, returned con {}'.format(returned_con)


# Generated at 2022-06-13 00:04:39.586974
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw("/")
    print("selinux_context: %s" % con)
    assert 'selinux_context' in con


# Generated at 2022-06-13 00:04:58.451662
# Unit test for function matchpathcon
def test_matchpathcon():
    (rc, con) = matchpathcon("/usr/bin/id", 0)
    print("rc is %s" % rc)
    print("con is %s" % con)



# Generated at 2022-06-13 00:05:02.777667
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon("/etc/shadow", 0)
    assert rc == 0, "Expected rc 0, got %d" % (rc,)
    assert con == "system_u:object_r:shadow_t", "Expected 'system_u:object_r:shadow_t', got %s" % (con,)



# Generated at 2022-06-13 00:05:06.615456
# Unit test for function matchpathcon
def test_matchpathcon():
    p = b"context"
    rc = _selinux_lib.matchpathcon(b'/var/log/audit', 1, byref(c_char_p(p)))
    if rc != -1:
        print("ok")


# Generated at 2022-06-13 00:05:09.228908
# Unit test for function matchpathcon
def test_matchpathcon():
    assert matchpathcon('/etc/securetty', 0)[1] == 'system_u:object_r:tty_device_t:s0'

del CDLL, c_char_p, c_int, byref, POINTER, get_errno

# Generated at 2022-06-13 00:05:15.880507
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    if not is_selinux_enabled():
        sys.exit("SELinux is not enabled.")
    (rc, con) = lgetfilecon_raw("/etc/selinux/config")
    if rc != 0:
        sys.exit("lgetfilecon_raw failed for file /etc/selinux/config with error {0}".format(rc))
    print("lgetfilecon_raw for file /etc/selinux/config returns context {0}".format(con))


# Generated at 2022-06-13 00:05:23.545525
# Unit test for function matchpathcon
def test_matchpathcon():
    """Borrowed from: https://github.com/python-selinux/selinux/blob/master/selinux/tests/test_context.py#L29
    """
    os.environ["SELINUX_INIT"] = "YES"
    assert matchpathcon("test.log", os.R_OK)[1] == "system_u:object_r:log_file_t:s0"
    os.environ["SELINUX_INIT"] = "NO"

# Generated at 2022-06-13 00:05:33.451513
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():

  if selinux_getenforcemode()[1] != 1:
      raise AssertionError('SELinux should be enabled for this test to run')

  con = lgetfilecon_raw('/tmp')
  if con[0] != 0:
      raise AssertionError('lgetfilecon_raw failed to execute')
  if con[1] != 'system_u:object_r:tmp_t:s0':
      raise AssertionError('Received unexpected SELinux context')

# Generated at 2022-06-13 00:05:42.714804
# Unit test for function matchpathcon
def test_matchpathcon():
    # initialize return code variable
    rc = 0

    # test missing path
    try:
        rc, con = matchpathcon(None, 0)
    except OSError:
        assert False, 'matchpathcon() raised OSError for missing path'

    # test missing mode
    try:
        rc, con = matchpathcon(None, None)
    except OSError:
        assert False, 'matchpathcon() raised OSError for missing mode'

    # test invalid path
    try:
        rc, con = matchpathcon('/invalidpath', 0)
    except OSError:
        assert False, 'matchpathcon() raised OSError for invalid path'

# Generated at 2022-06-13 00:05:47.573435
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import pytest

    # Test where file exists
    [rc, con] = lgetfilecon_raw('/usr/bin/python3')
    assert rc == 0 and con is not None

    # Test where file does *not* exist
    [rc, con] = lgetfilecon_raw('/usr/bin/python3_')
    assert rc == -1 and con is None


# Generated at 2022-06-13 00:05:49.695740
# Unit test for function matchpathcon
def test_matchpathcon():
    rc = matchpathcon('/etc/passwd', 0)
    print(rc)



# Generated at 2022-06-13 00:06:41.429596
# Unit test for function matchpathcon
def test_matchpathcon():
    from ansible.module_utils.common.text.converters import to_bytes
    assert _selinux_lib.matchpathcon(b"/tmp", 0, None) == 0
    assert _selinux_lib.matchpathcon(b"/tmp", 0, None) == 0
    assert _selinux_lib.matchpathcon(b"/etc/shadow", 0, None) == 0
    con = c_char_p()
    assert _selinux_lib.matchpathcon(b"/tmp", 0, byref(con)) == 0
    assert con.value == b"system_u:object_r:tmp_t:s0"
    con.value = None
    assert _selinux_lib.matchpathcon(b"/etc/shadow", 0, byref(con)) == 0

# Generated at 2022-06-13 00:06:48.002715
# Unit test for function matchpathcon
def test_matchpathcon():
    import tempfile

    # create a tmp dir to test with
    tmpdir = tempfile.mkdtemp(prefix='ansible-selinux-test')

    try:
        # matchpathcon() returns (rc, con) and
        # rc == 0 iff con is valid, otherwise rc is errno
        rc, con = matchpathcon(tmpdir, os.R_OK)
        assert rc == 0
        assert con == 'system_u:object_r:usr_t:s0'
    finally:
        os.rmdir(tmpdir)

# Generated at 2022-06-13 00:06:51.644399
# Unit test for function matchpathcon
def test_matchpathcon():
    path = os.path.abspath(__file__)
    mode = os.stat(path).st_mode

    (rc, con) = matchpathcon(path, mode)
    assert rc == 0
    assert con
    print(con)

# Generated at 2022-06-13 00:06:58.655190
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    try:
        path = '/'
        result = lgetfilecon_raw(path)
        status = result[0]
        context = result[1].split(':')
        if 'unconfined' in context:
            print("PASS: lgetfilecon_raw succeeded on {}".format(path))
        else:
            print("FAIL: lgetfilecon_raw on {}".format(path))
    except OSError as err:
        if err.errno == 95:
            print("SKIP: SELinux or SELinux libraries not available on this system")
        else:
            print("FAIL: lgetfilecon_raw:", err)


# Generated at 2022-06-13 00:07:00.341389
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    if __name__ == '__main__':
        rc, con = lgetfilecon_raw('/etc/passwd')
        print('/etc/passwd: con=%s, rc=%d' % (con, rc))

# Generated at 2022-06-13 00:07:02.414085
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (rc, con) = lgetfilecon_raw('/tmp')
    assert rc == 0
    assert con == 'system_u:object_r:tmp_t:s0'



# Generated at 2022-06-13 00:07:09.720312
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Create a file, check the context
    with open('/tmp/test.file', 'w') as outfile:
        outfile.write('text')
        outfile.close()
        rc, con = lgetfilecon_raw('/tmp/test.file')
        os.remove('/tmp/test.file')
    # If you remove the last argument of the command you will receive:
    # OSError: [Errno 2] No such file or directory
    if rc < 0:
        print('')
    else:
        print(con)


if __name__ == '__main__':
    test_lgetfilecon_raw()

# Generated at 2022-06-13 00:07:20.392092
# Unit test for function matchpathcon
def test_matchpathcon():
    from tempfile import TemporaryFile, NamedTemporaryFile
    import unittest
    import tempfile

    class TestPathMatch(unittest.TestCase):
        def test_file(self):
            with NamedTemporaryFile(prefix='ansible_test', dir='/tmp') as tf:
                rc, con = matchpathcon(tf.name, 0)
                self.assertIsInstance(con, str)

        def test_dir(self):
            with tempfile.TemporaryDirectory(dir='/tmp') as tmpdir:
                rc, con = matchpathcon(tmpdir, 0)
                self.assertIsInstance(con, str)


# Generated at 2022-06-13 00:07:29.423980
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw('/dev/null')[1] == 'system_u:object_r:null_device_t:s0'
    assert lgetfilecon_raw('/tmp')[1] == 'system_u:object_r:tmp_t:s0'
    assert lgetfilecon_raw('/etc/hosts')[1] == 'system_u:object_r:net_conf_t:s0'
    assert lgetfilecon_raw('/etc/shadow')[1] == 'system_u:object_r:shadow_t:s0'
    assert lgetfilecon_raw('/etc/resolv.conf')[1] == 'system_u:object_r:net_conf_t:s0'

# Generated at 2022-06-13 00:07:38.069712
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # test from somewhere in the system
    (rc, con) = lgetfilecon_raw('/home/vagrant/.ssh')
    assert rc == 0
    assert con.startswith('system_u:object_r:user_home_t:s0')
    # test from a file in /dev (i.e. one that is pre-labeled rather than being auto-labeled)
    (rc, con) = lgetfilecon_raw('/dev/zero')
    assert rc == 0
    assert con.startswith('system_u:object_r:device_t:s0')
    # test from a file that doesn't exist
    (rc, con) = lgetfilecon_raw('/does/not/exist')
    assert rc == -1
    assert con == None

# Generated at 2022-06-13 00:09:02.934670
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    res = lgetfilecon_raw('/etc/passwd')
    assert res[0] == 0
    assert res[1] == 'unconfined_u:object_r:etc_runtime_t:s0'


if __name__ == '__main__':
    test_lgetfilecon_raw()

# Generated at 2022-06-13 00:09:06.596604
# Unit test for function matchpathcon
def test_matchpathcon():
    path = '/tmp/test_file_selinux'
    mode = 0o666
    fd = os.open(path, os.O_CREAT)
    try:
        rc, con = matchpathcon(path, mode)
        assert rc == 0, con
    finally:
        os.close(fd)
        os.remove(path)

