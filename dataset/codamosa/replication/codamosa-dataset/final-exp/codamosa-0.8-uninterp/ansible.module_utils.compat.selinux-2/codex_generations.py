

# Generated at 2022-06-12 23:59:07.807757
# Unit test for function matchpathcon
def test_matchpathcon():
    test_path = to_bytes('/tmp/a')
    print(matchpathcon(test_path, 0))

# Generated at 2022-06-12 23:59:11.501811
# Unit test for function matchpathcon
def test_matchpathcon():
    '''Test that matchpathcon works as expected'''
    import os

    path = '/etc/ansible'
    if os.path.exists(path):
        rc, con = matchpathcon(path, os.R_OK)
        print('rc: {0}, con: {1}'.format(rc, con))



# Generated at 2022-06-12 23:59:17.210968
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    [rc, con] = selinux.lgetfilecon_raw('/tmp/foo')
    assert rc == 0
    assert con == 'tmp_t'
    [rc, con] = selinux.lgetfilecon_raw('/tmp/foo/bar')
    assert rc == 0
    assert con is None

# Generated at 2022-06-12 23:59:24.413677
# Unit test for function matchpathcon
def test_matchpathcon():

    # Test normal case
    res, con = matchpathcon(b'/etc/passwd', 0)
    assert(res == 0)

    # Test path goes outside the root of the filesystem
    res, con = matchpathcon(b'/..passwd', 0)
    assert(res == -1)

    # Test invalid mode
    res, con = matchpathcon(b'/etc/passwd', 5)
    assert(res == -1)

    # Test invalid path
    res, con = matchpathcon(b'/wrong/passwd', 0)
    assert(res == -1)

# Generated at 2022-06-12 23:59:27.878604
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = '/etc/resolv.conf'
    rc, con = tuple(lgetfilecon_raw(path))
    assert (rc == 0 and con == 'system_u:object_r:net_conf_t:s0')


# Generated at 2022-06-12 23:59:33.406729
# Unit test for function matchpathcon
def test_matchpathcon():
    (rc, con) = matchpathcon("/etc/passwd", 0)
    assert rc == 0
    assert con == "system_u:object_r:etc_t:s0"

    (rc, con) = matchpathcon("/etc/passwd", 1)
    assert rc == 0
    assert con == "system_u:object_r:etc_runtime_t:s0"


# Generated at 2022-06-12 23:59:35.719038
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (rc, con) = lgetfilecon_raw("/etc")
    assert rc == 0
    assert con == "system_u:object_r:etc_t:s0"

# Generated at 2022-06-12 23:59:46.761762
# Unit test for function matchpathcon
def test_matchpathcon():
    # Test for case where a file's context is properly set via matchpathcon
    results, con = matchpathcon('/var/log/testfile',
                                os.O_CREAT)
    assert results == 0, "matchpathcon failed to find a context for /var/log/testfile"
    assert isinstance(con, str), "matchpathcon did not return a string"
    assert con != "", "matchpathcon returned an empty string"

    # Test for case where a file's context is not properly set via matchpathcon
    results, con = matchpathcon('/var/log/shouldnotexist',
                                os.O_CREAT)
    assert results != 0, "matchpathcon did not fail to find a context for /var/log/shouldnotexist"

# Generated at 2022-06-12 23:59:50.360746
# Unit test for function matchpathcon
def test_matchpathcon():
    # get the context of current process
    rc, context_str = matchpathcon(None, 0)
    assert rc == 0
    assert context_str == "system_u:system_r:ansible_t:s0"


if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-12 23:59:52.071577
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    res = lgetfilecon_raw("/etc/passwd")
    return res[1]


# Generated at 2022-06-12 23:59:58.580674
# Unit test for function matchpathcon
def test_matchpathcon():
    test_path = "/usr/bin/ping"
    test_mode = 0
    (rc, con) = matchpathcon(test_path, test_mode)
    print("matchpathcon with path \"%s\" returns rc: %s, con %s" % (test_path, rc, con))



# Generated at 2022-06-13 00:00:01.125554
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, context = lgetfilecon_raw(b'/test')
    if rc != 0:
        return [rc, context]
    else:
        return [rc, context.split()[1].decode('UTF-8')]

if __name__ == '__main__':
    print(test_lgetfilecon_raw())

# Generated at 2022-06-13 00:00:05.110775
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    con_raw = lgetfilecon_raw('/sys/kernel/config/target/iscsi/stockholm')
    assert con_raw == [0, "system_u:object_r:iscsi_target_device_t:s0:c121,c281"]

# Generated at 2022-06-13 00:00:12.994766
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon('/etc/ssh/', 0)
    assert os.path.exists('/etc/ssh/sshd_config')
    assert rc == 0
    assert con == 'root:system_r:ssh_config_t:s0'
    rc, con = matchpathcon('/etc/ssh/sshd_config', 0)
    assert rc == 0
    assert con == 'root:object_r:ssh_config_t:s0'
    rc, con = matchpathcon('/nosuchfile', 0)
    assert rc == -1
    assert con == ''

# Generated at 2022-06-13 00:00:15.669043
# Unit test for function matchpathcon
def test_matchpathcon():
    if _selinux_lib.matchpathcon('/path/to/target', 0, None) != 0:
        raise AssertionError('_selinux_lib.matchpathcon: error in calling function')

# Generated at 2022-06-13 00:00:23.896694
# Unit test for function matchpathcon
def test_matchpathcon():

    # Test1: test matchpathcon for a valid path
    path = '/etc/foo.bar'
    mode = os.R_OK
    rc, con = matchpathcon(path, mode)
    assert con == 'system_u:object_r:etc_t:s0'

    # Test2: Test matchpathcon for invalid path
    path = '/foo.bar'
    rc, con = matchpathcon(path, mode)
    assert con == ''

    # Test3: Test matchpathcon with invalid mode
    path = '/etc/foo.bar'
    mode = 1234
    rc, con = matchpathcon(path, mode)
    assert con == ''

    # Test4: Test matchpathcon with empty path
    path = ''
    mode = os.R_OK

# Generated at 2022-06-13 00:00:27.801673
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    test_lgetfilecon_raw_output = lgetfilecon_raw('/tmp')
    assert test_lgetfilecon_raw_output[0] != -1
    assert test_lgetfilecon_raw_output[1] == 'system_u:object_r:tmp_t:s0'


# Generated at 2022-06-13 00:00:40.351423
# Unit test for function matchpathcon
def test_matchpathcon():
    import os
    import pwd
    import grp

    path = '/sys/fs/cgroup/'

    # Get path uid and gid
    uid = pwd.getpwnam(os.getenv("USER")).pw_uid
    gid = grp.getgrnam("root").gr_gid

    # Set the path uid and gid
    os.chown(path, uid, gid)

    # Get path mode
    mode = os.stat(path).st_mode

    # Get path selinux context
    rc, con = matchpathcon(path, mode)
    assert rc == 0, "SELinux is not enabled: {0}".format(rc)
    assert con, "SELinux context not found: {0}".format(con)



# Generated at 2022-06-13 00:00:45.919387
# Unit test for function matchpathcon
def test_matchpathcon():
    r = matchpathcon('/simplefile', 0)
    assert r[0] == 0
    assert r[1] == 'system_u:object_r:user_home_t:s0'
    r = matchpathcon('/sys/kernel/modprobe', 0)
    assert r[0] == 0
    assert r[1] == 'system_u:object_r:modprobe_exec_t:s0'
    r = matchpathcon('/simplefile', 1)
    assert r[0] == 0
    assert r[1] == 'system_u:object_r:user_home_t:s0'
    r = matchpathcon('/sys/kernel/modprobe', 1)
    assert r[0] == 0

# Generated at 2022-06-13 00:00:47.483417
# Unit test for function matchpathcon
def test_matchpathcon():
    print(matchpathcon(b'/', 0)[1])



# Generated at 2022-06-13 00:00:55.395008
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon('/tmp/foo/bar/baz', mode=1)
    assert rc == 0
    assert con == 'system_u:object_r:tmp_t:s0'



# Generated at 2022-06-13 00:00:58.396614
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    ret_obj = {
        "rc": 0,
        "con": "system_u:object_r:devpts_t:s0\n"
    }
    assert lgetfilecon_raw(b'/dev/pts') == ret_obj

# Generated at 2022-06-13 00:01:03.297692
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Test file
    path = '/etc/passwd'

    # Should return code 0, and a context string (for example 'unconfined_u:object_r:user_home_t:s0')
    print(lgetfilecon_raw(path))


if __name__ == '__main__':
    test_lgetfilecon_raw()

# Generated at 2022-06-13 00:01:06.887029
# Unit test for function matchpathcon
def test_matchpathcon():
    path = "/foo"
    print("check pathcon for %s" % path)
    rc, con = matchpathcon(path, 0)
    print("check pathcon rc=%s con=%s" % (rc, con))


# Generated at 2022-06-13 00:01:11.843871
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    _, con = lgetfilecon_raw('/')
    assert isinstance(con, str), "context is not str: %r" % (con,)
    assert len(con) > 0, "empty context"

    _, con = lgetfilecon_raw('/etc/passwd')
    assert con is not None, "could not read context - selinux disabled?"
    assert len(con) > 0, "empty context"



# Generated at 2022-06-13 00:01:14.214958
# Unit test for function matchpathcon
def test_matchpathcon():
    _rc, con = matchpathcon('/var/log/', 0)
    print('/var/log/ context is: {0}'.format(con))


# Generated at 2022-06-13 00:01:16.768363
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import tempfile

    path = tempfile.mktemp()
    rc, con = lgetfilecon_raw(path)

    assert rc == 0
    assert con == "system_u:object_r:tmp_t:s0"

# Generated at 2022-06-13 00:01:19.443275
# Unit test for function matchpathcon
def test_matchpathcon():
    tpath = '/var/tmp/some/file'
    test_mode = os.R_OK
    test_con = 'system_u:object_r:tmp_t:s0'

    assert matchpathcon(tpath, test_mode) == [0, test_con]



# Generated at 2022-06-13 00:01:26.613424
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():

    def _selinux_lgetfilecon_raw(path):
        """
        Do a lgetfilecon_raw call and return any error code or context string.
        """
        try:
            rc, con = lgetfilecon_raw(path)
        except OSError as e:
            return [e.errno, None]

        return [rc, con]

    path = '/tmp/foo'
    rc, con = _selinux_lgetfilecon_raw(path)
    if rc != -1:  # if lgetfilecon_raw returns -1, continue and run the second test
        raise AssertionError('expected an error, got {0}'.format(rc))


# Generated at 2022-06-13 00:01:35.865866
# Unit test for function matchpathcon
def test_matchpathcon():
    import os
    import sys

    TEST_PATH = '/tmp/test_matchpathcon'
    TEST_FILE = os.path.join(TEST_PATH, 'test_file')

    os.makedirs(TEST_PATH)
    open(TEST_FILE, 'a').close()

    # Test for valid path
    rc, con = matchpathcon(TEST_FILE, os.R_OK)
    if rc == -1:
        if con == 'security_getenforce':
            print ('Sorry, SELinux is not enabled.')
            sys.exit(0)
        else:
            print ('Error getting context for {0}: {1}'.format(TEST_FILE, con))
            sys.exit(1)

# Generated at 2022-06-13 00:01:46.788699
# Unit test for function matchpathcon
def test_matchpathcon():
    ret = matchpathcon('/sys/firmware/efi', 0)
    assert ret[0] == 0
    assert ret[1] == 'system_u:object_r:firmware_t:s0'


# Generated at 2022-06-13 00:01:50.866599
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, pathcon = matchpathcon('/foo/bar/baz', 1)
    if rc != 0:
        raise Exception('test_matchpathcon was unable to determine file context')
    if pathcon != b'u:object_r:foo_t:s0':
        raise Exception('test_matchpathcon was unable to determine file context')



# Generated at 2022-06-13 00:01:56.896876
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, context = matchpathcon(b'README', 0)
    if rc == 0:
        print('context is {0}'.format(context))
    else:
        print('matchpathcon call failed')


# Generated at 2022-06-13 00:02:05.068670
# Unit test for function matchpathcon
def test_matchpathcon():
    from ansible.module_utils.selinux import matchpathcon
    from ansible.module_utils.basic import AnsibleModule

    args = dict(
        path='/foo/bar',
    )

    module = AnsibleModule(
        argument_spec=dict(
            path=dict(type='path', required=True),
        ),
        supports_check_mode=True,
    )

    rc, con = matchpathcon(module.params['path'], 0)

    # FIXME: low-quality match

# Generated at 2022-06-13 00:02:08.884007
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw('/tmp')
    assert rc == 0


# Generated at 2022-06-13 00:02:14.026756
# Unit test for function matchpathcon
def test_matchpathcon():
    """
    If possible call matchpathcon(3)

    If the selinux libs are installed this should return a non-error rc
    """
    rc, msg = matchpathcon('/etc/passwd', 0)
    if rc != -1:
        rc2, msg2 = matchpathcon('/var/empty', 0)
        return [rc2, msg2]
    return [rc, msg]


# Generated at 2022-06-13 00:02:17.302141
# Unit test for function matchpathcon
def test_matchpathcon():

    (rc, con) = matchpathcon('/etc/dummy', 0)
    print("Return value = {0}, Context = {1}".format(rc, con))


# Generated at 2022-06-13 00:02:21.262231
# Unit test for function matchpathcon
def test_matchpathcon():
    status = matchpathcon('/tmp/test/file', 0)
    assert isinstance(status, list)
    assert status[0] == 0

# Generated at 2022-06-13 00:02:24.281326
# Unit test for function matchpathcon
def test_matchpathcon():
    (rc, con) = matchpathcon(b'/foo', 0)
    assert rc == 0
    assert con == 'system_u:object_r:etc_runtime_t:s0'

# Generated at 2022-06-13 00:02:29.501292
# Unit test for function matchpathcon
def test_matchpathcon():
    def _test(mode_val):
        rc, con = matchpathcon('/usr', mode_val)
        assert rc == 0
        assert 'system_u:object_r:usr_t:s0' in con

    _test(0)
    _test(1)
    _test(sys.maxsize)



# Generated at 2022-06-13 00:02:42.927049
# Unit test for function matchpathcon
def test_matchpathcon():
    import tempfile
    _, fname = tempfile.mkstemp()
    mode = 0o755

    try:
        assert lsetfilecon(fname, 'u:object_r:user_tmp_t:s0') == 0
        assert matchpathcon(fname, mode)[1] == 'u:object_r:user_tmp_t:s0'
    finally:
        os.unlink(fname)



# Generated at 2022-06-13 00:02:45.828357
# Unit test for function matchpathcon
def test_matchpathcon():
    path = "/etc/hosts"
    mode = 0
    rc, con = matchpathcon(path, mode)
    assert (rc == 0)
    assert (con == "system_u:object_r:etc_t:s0")


# Generated at 2022-06-13 00:02:48.932924
# Unit test for function matchpathcon
def test_matchpathcon():
    """ Unit test for function matchpathcon """
    assert matchpathcon('/root/file1', 0) == [0, 'system_u:object_r:admin_home_t:s0']


# Generated at 2022-06-13 00:02:54.579233
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    """test lgetfilecon_raw function"""
    rc, con = lgetfilecon_raw("/")
    assert not rc
    assert con == "system_u:object_r:root_t:s0"

if __name__ == '__main__':
    test_lgetfilecon_raw()

# Generated at 2022-06-13 00:02:57.698704
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (rc, con) = lgetfilecon_raw('/tmp/')
    if rc < 0:
        print('system does not have selinux support or selinux is disabled')


# Generated at 2022-06-13 00:03:02.411677
# Unit test for function matchpathcon
def test_matchpathcon():
    path = '/tmp/test'
    mode = os.R_OK | os.W_OK
    con = matchpathcon(path, mode)
    if con[0] == 0:
        print('Context is: {}'.format(con[1]))
    else:
        err = con[1]
        print('Error: {}'.format(err))



# Generated at 2022-06-13 00:03:12.170461
# Unit test for function matchpathcon
def test_matchpathcon():
    retval, rc = matchpathcon('/var', 0)
    print('[{0}] matchpathcon(/var, 0) -> {1}'.format(retval, rc))
    retval, rc = matchpathcon('/usr/sbin', 1)
    print('[{0}] matchpathcon(/usr/sbin, 1) -> {1}'.format(retval, rc))
    retval, rc = matchpathcon('/var/www/html/xyz', 5)
    print('[{0}] matchpathcon(/var/www/html/xyz, 5) -> {1}'.format(retval, rc))
    print('security_getenforce() -> {0}'.format(security_getenforce()))

# Generated at 2022-06-13 00:03:13.317229
# Unit test for function matchpathcon
def test_matchpathcon():
    ret = matchpathcon('/etc/init.d', 0)
    assert ret[0] == 0
    assert ret[1] == 'etc_t'

# Generated at 2022-06-13 00:03:15.745231
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    lcon = lgetfilecon_raw('/home/vagrant/test_file_with_selinux_context')
    assert lcon[1] == 'system_u:object_r:bin_t:s0'

# Generated at 2022-06-13 00:03:17.137495
# Unit test for function matchpathcon
def test_matchpathcon():
    r = matchpathcon('/var/lib', 0)
    assert len(r) == 2


# Generated at 2022-06-13 00:03:43.933975
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import os
    import os.path
    import sys
    from ctypes import byref, CDLL

    def lgetfilecon_raw(path):
        con = c_char_p()
        try:
            rc = _selinux_lib.lgetfilecon_raw(path, byref(con))
            return [rc, to_native(con.value)]
        finally:
            _selinux_lib.freecon(con)

    # Unit test for function lgetfilecon_raw
    def test_lgetfilecon_raw():
        import os
        import os.path
        import sys
        from ctypes import byref, CDLL

        def lgetfilecon_raw(path):
            con = c_char_p()

# Generated at 2022-06-13 00:03:49.074344
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Unit test for function lgetfilecon_raw
    # This function runs in with the SELinux disabled, so the context should be "unlabeled"
    result = lgetfilecon_raw('/etc/hosts')
    # No SELinux, so the rc should be set to -1
    assert result[0] == -1
    # The context should be unlabeled
    assert result[1] == 'unlabeled'

# Generated at 2022-06-13 00:03:51.819461
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw(b'/') == [0, 'system_u:object_r:root_t:s0']



# Generated at 2022-06-13 00:03:53.213472
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw('/etc/fstab')
    assert rc == 0 and con == 'system_u:object_r:fstab_t:s0'

# Generated at 2022-06-13 00:03:55.656048
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    file_name = "/etc/hosts"
    rc, con_str = lgetfilecon_raw(file_name)
    assert rc == 0
    assert con_str is not None

# Generated at 2022-06-13 00:04:06.373124
# Unit test for function matchpathcon
def test_matchpathcon():
    def _test_matchpathcon(path, mode):
        rc, con = matchpathcon(path, mode)
        print(to_native(con), rc)

    _test_matchpathcon(b'/var/tmp/testfile', 0)
    _test_matchpathcon(b'/var/tmp', 0)
    _test_matchpathcon(b'/var', 0)
    _test_matchpathcon(b'/', 0)

    _test_matchpathcon(b'/var/tmp/testfile', os.O_RDWR | os.O_CREAT | os.O_EXCL | os.O_NOCTTY)
    _test_matchpathcon(b'/var/tmp/testfile', os.O_RDWR | os.O_CREAT | os.O_EXCL | os.O_TRUNC)

# Generated at 2022-06-13 00:04:09.548025
# Unit test for function matchpathcon
def test_matchpathcon():
    assert matchpathcon('/tmp', 0) == [0, 'system_u:object_r:tmp_t:s0']

# Generated at 2022-06-13 00:04:19.324826
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    try:
        import tempfile
        tmpfile = tempfile.NamedTemporaryFile()
        file_path = tmpfile.name
        tmpfile.close()
        # selinux_getpolicytype() returns a list
        rc, policy_type = selinux_getpolicytype()
        rc, con = lgetfilecon_raw(file_path)

        if policy_type == 'targeted':
            assert 'system_u:object_r:unlabeled_t:s0' in con
        else:
            assert 'system_u:object_r:default_t:s0' in con
    except:
        raise

# Generated at 2022-06-13 00:04:22.100539
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, output = matchpathcon("/var/lib/foo", 0)
    assert rc == 0
    assert output == "system_u:object_r:var_lib_t:s0"

# Generated at 2022-06-13 00:04:32.796174
# Unit test for function lgetfilecon_raw

# Generated at 2022-06-13 00:04:52.682670
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Describe expected output
    expected_output = ['0', 'system_u:object_r:admin_home_t:s0']

    # Perform function call
    returned_output = lgetfilecon_raw('/root')

    assert expected_output == returned_output

# Generated at 2022-06-13 00:05:04.250953
# Unit test for function matchpathcon
def test_matchpathcon():
    from ansible.module_utils.selinux.libselinux import matchpathcon
    from ansible.module_utils.selinux.libselinux import SECURITY_GET_BOOL_ENFORCE
    from ansible.module_utils.selinux.libselinux import SECURITY_GET_BOOL_DISABLE

    # Test code 1 : Perform with the enforcing mode of selinux
    security_mode_enforcing = SECURITY_GET_BOOL_ENFORCE
    path = '/etc/selinux/config'
    rc, out = matchpathcon(path, security_mode_enforcing)
    if rc == 0:
        print('return code : %s and con_val : %s' % (rc, out))
    else:
        print('Error code : %s' % rc)

   

# Generated at 2022-06-13 00:05:11.572432
# Unit test for function matchpathcon
def test_matchpathcon():
    import getpass
    import tempfile

    tmp_dir = tempfile.TemporaryDirectory()


# Generated at 2022-06-13 00:05:18.885712
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path='/etc'
    con = c_char_p()
    rc=0
    try:
        rc = _selinux_lib.lgetfilecon_raw(path, byref(con))
    finally:
        _selinux_lib.freecon(con)
    return [rc, to_native(con.value)]



# Generated at 2022-06-13 00:05:26.325705
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = '/etc/passwd'
    rc, con = lgetfilecon_raw(path)
    con = to_native(con)

    if rc < 0:
        errno = get_errno()
        raise OSError(errno, os.strerror(errno))
    # Should be none if not running in SELinux
    elif rc > 0:
        print("SELinux is not enabled, skipping unit test for lgetfilecon_raw")
        return

    print("Test rc={0} for path={1} context={2}".format(rc, path, con))
    assert con == 'system_u:object_r:etc_t:s0'



# Generated at 2022-06-13 00:05:31.868271
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = None
    rc_expected = -13
    con_expected = None
    assert lgetfilecon_raw(path) == [rc_expected, con_expected], 'Got {}'.format(lgetfilecon_raw(path))



# Generated at 2022-06-13 00:05:33.990532
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # lgetfilecon_raw returns ['0', 'unlabeled_t'] when the path is none
    assert lgetfilecon_raw(None) == ['0', 'unlabeled_t']

# Generated at 2022-06-13 00:05:34.648952
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw(b'/tmp')

# Generated at 2022-06-13 00:05:40.481010
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Create a test file
    with open('/tmp/ctypes_test', 'w'):
        pass
    # Verify context is correct
    assert lgetfilecon_raw('/tmp/ctypes_test')[1] == 'system_u:object_r:default_t:s0'
    # Cleanup file
    os.unlink('/tmp/ctypes_test')



# Generated at 2022-06-13 00:05:46.138560
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():

    con = c_char_p()
    try:
        rc = _selinux_lib.lgetfilecon_raw("/home/centos/test_file", byref(con))
        print("rc:", rc, " context:", con.value)
        return [rc, to_native(con.value)]
    finally:
        _selinux_lib.freecon(con)

test_lgetfilecon_raw()

# Generated at 2022-06-13 00:06:36.580674
# Unit test for function matchpathcon
def test_matchpathcon():
    """
    Test matchpathcon API.
    """
    from os import path

    if not _selinux_lib.is_selinux_enabled():
        testdir = '/tmp'
    else:
        testdir = '/'

    # Test mode zero
    matchpathcon(testdir, 0)

    # Test mode one
    matchpathcon(testdir, 1)


if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-13 00:06:41.641106
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    f_h = open('/etc/group', 'r')
    testfile = f_h.name
    f_h.close()
    rc, con = lgetfilecon_raw(testfile)
    assert not rc
    assert con != 'system_u:object_r:admin_home_t:s0'
    rc, con = lgetfilecon_raw('THIS IS FAKE')
    assert rc

# Generated at 2022-06-13 00:06:46.997255
# Unit test for function matchpathcon
def test_matchpathcon():
    '''
    Check if a syscall calls returns the expected value

    On Fedora the call returns 0
    On RedHat the call fails with a ENOENT error
    '''
    try:
        rc, context = matchpathcon("/etc/passwd", 0)
        assert rc == 0
    except OSError as e:
        assert False, "Unexpected OSError: {:d} {:s}" .format(e.errno, e.strerror)


if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-13 00:06:53.257799
# Unit test for function matchpathcon
def test_matchpathcon():
    assert matchpathcon('/selinux/testcon', 0) == [0, 'system_u:object_r:etc_t:s0']
    assert matchpathcon('/selinux/testcon', 1) == [0, 'system_u:object_r:etc_t:s0']
    assert matchpathcon('/selinux/testcon', 2) == [0, 'system_u:object_r:etc_t:s0']



# Generated at 2022-06-13 00:06:55.721949
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (rc, val) = lgetfilecon_raw("/bin/osh")
    assert rc == 0
    assert val == "system_u:object_r:bin_t:s0"


# Generated at 2022-06-13 00:06:56.874714
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw('/')
    assert rc == 0

# Generated at 2022-06-13 00:06:58.513578
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Test /etc/passwd
    [rc, con] = lgetfilecon_raw('/etc/passwd')
    assert rc == 0
    assert con == 'unconfined_u:object_r:etc_runtime_t:s0'

# Generated at 2022-06-13 00:07:00.417973
# Unit test for function matchpathcon
def test_matchpathcon():
    (rc, con) = matchpathcon('/data', 0)
    assert(rc == 0)
    assert(con == 'system_u:object_r:var_t:s0')

# Generated at 2022-06-13 00:07:04.538368
# Unit test for function matchpathcon
def test_matchpathcon():
    """Unit test for function matchpathcon"""
    import doctest
    from ansible.module_utils.selinux import matchpathcon

    print('running matchpathcon unit tests')
    fail_count, _ = doctest.testmod(matchpathcon)

    if fail_count:
        raise Exception('matchpathcon unit tests failed: {0}'.format(fail_count))

# Generated at 2022-06-13 00:07:13.033540
# Unit test for function matchpathcon
def test_matchpathcon():
    # Test that expected errors occur on non-existent path
    if os.path.exists("/this/is/a/made/up/file/path"):
        print("A file named /this/is/a/made/up/file/path already exists. "
              "This test will not complete as expected. Delete that file and run the test again.")
        sys.exit()


# Generated at 2022-06-13 00:08:35.572541
# Unit test for function matchpathcon
def test_matchpathcon():
    if is_selinux_enabled():
        assert matchpathcon('/home/user/Message.txt', 0) == [0, 'user_home_t']
    else:
        assert matchpathcon('/home/user/Message.txt', 0) == [-1, None]



# Generated at 2022-06-13 00:08:42.896945
# Unit test for function matchpathcon
def test_matchpathcon():
    try:
        matchpathcon_result = matchpathcon('/etc/shadow', 1)
    except OSError as e:
        matchpathcon_result = [e.errno, os.strerror(e.errno)]

    print('matchpathcon(/etc/shadow, 1) = %s' % to_native(matchpathcon_result))
    if matchpathcon_result[0]:
        raise RuntimeError('matchpathcon: %s' % to_native(matchpathcon_result[1]))

    # test label == null
    matchpathcon_result = matchpathcon('/etc/shadow', 1, None)
    print('matchpathcon(/etc/shadow, 1, NULL) = %s' % to_native(matchpathcon_result))
    if matchpathcon_result[0]:
        raise

# Generated at 2022-06-13 00:08:50.517053
# Unit test for function matchpathcon
def test_matchpathcon():
    # the selinux module uses matchpathcon to map file contexts for files to try and
    # determine the selinux type of the file, it's possible that matchpathcon will
    # not be able to resolve a pattern if the file does not exist in the file system
    # (this is the case with the selinux module), in which case matchpathcon will return
    # an error code of -1 and errno will be set to ENOENT.  Since the matchpathcon function
    # has to return a tuple with two values, a string and an error code, the selinux module
    # returns the errno string as the MNTPNT when the error code is -1
    context = matchpathcon('/tmp/doesnt_exist', 0)
    assert context[0] == -1
    assert context[1] == 'ENOENT'

    # But if the file

# Generated at 2022-06-13 00:08:53.287152
# Unit test for function matchpathcon
def test_matchpathcon():
    (rc, con) = matchpathcon(b'/etc/localtime', 0)
    assert rc == 0
    assert con == 'system_u:object_r:localtime_etc_t:s0'

# Generated at 2022-06-13 00:08:55.496933
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw('/sys') == [0, 'system_u:object_r:sysfs_t:s0']

# Generated at 2022-06-13 00:08:58.050407
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    output = lgetfilecon_raw('/etc/passwd')
    assert isinstance(output[0], int)
    assert isinstance(output[1], str) or output[1] is None
    assert len(output) == 2



# Generated at 2022-06-13 00:08:59.461712
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon(b'/tmp/testfile', 0)
    assert rc == 0, con

# Generated at 2022-06-13 00:09:04.074558
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = '/etc/passwd'
    rc, con = lgetfilecon_raw(path)
    if rc == -1:
        raise Exception('Failed retrieve the context of {0}'.format(path))
    # stdout.write('The context of {0} is {1}\n'.format(path, con))
    # The context of /etc/passwd is system_u:object_r:passwd_file_t:s0

