

# Generated at 2022-06-12 23:59:13.144958
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():

    rc, con = lgetfilecon_raw(b'/var/lib/libvirt/images')
    assert con == 'system_u:object_r:svirt_image_t:s0'
    rc, con = lgetfilecon_raw(b'/etc/selinux/targeted/policy/policy.29')
    assert con == 'system_u:object_r:selinux_policy_t:s0'
    rc, con = lgetfilecon_raw(b'/etc/selinux/targeted/modules/active/policy.kern')
    assert con == 'system_u:object_r:selinux_policy_t:s0'



# Generated at 2022-06-12 23:59:24.497105
# Unit test for function matchpathcon
def test_matchpathcon():
    [rc, con] = matchpathcon('/foo/bar', 0)
    assert rc == 1
    assert con.lower() == 'rootfs:object_r:rootfs:s0'.lower()
    del(rc, con)

    [rc, con] = matchpathcon('/etc/passwd', 0)
    assert rc == 0
    assert con.lower() == 'rootfs:etc_runtime_t:file:s0'.lower()
    del(rc, con)

    [rc, con] = matchpathcon('/etc/foo/passwd', 0)
    assert rc == 0
    assert con.lower() == 'rootfs:etc_runtime_t:file:s0'.lower()
    del(rc, con)

    [rc, con] = matchpathcon('/etc/passwd', 1)

# Generated at 2022-06-12 23:59:30.801870
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    os.chdir('/sys/fs/cgroup/cpu,cpuacct/')
    os.chdir('/sys/fs/cgroup/cpu,cpuacct/')
    for d in os.listdir('.'):
        if os.path.isdir(d):
            print(d)
            [rc, con] = lgetfilecon_raw(d)
            assert rc == 0, 'SELinux context for {0} is {1}'.format(d, con)

# Generated at 2022-06-12 23:59:35.558953
# Unit test for function matchpathcon
def test_matchpathcon():
    rc = matchpathcon('/etc/fstab', 0)
    if rc[0] == 0:
        raise SystemExit("matchpathcon failed with error: %s" % rc[1])
    print("matchpathcon returned: %s, context %s" % (rc[0], rc[1]))

if __name__ == "__main__":
    test_matchpathcon()

# Generated at 2022-06-12 23:59:38.468568
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon('/var/log', 0)
    assert(rc == 0)
    assert(con == "system_u:object_r:var_log_t:s0")

# Generated at 2022-06-12 23:59:43.940656
# Unit test for function matchpathcon
def test_matchpathcon():
    (ret, outbuf) = matchpathcon("/bin/ping", 0)
    if outbuf:
        print("context of /bin/ping is %s"%outbuf)
    else:
        print("failed to get context for /bin/ping")

if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-12 23:59:47.196115
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    try:
        filecon = lgetfilecon_raw('/tmp')
        print(filecon)
    except OSError:
        print('The OS error is raised')


# Generated at 2022-06-12 23:59:53.851022
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    test_path = '/tmp/selinux-test-file'
    test_con = 'system_u:object_r:user_tmp_t:s0'
    test_mode = 0o777

    # Create a test file
    with open(test_path, 'w'):
        pass

    # Set the test file's SELinux context
    lsetfilecon(test_path, test_con)

    # Get the current context
    (_rc, current_con) = lgetfilecon_raw(test_path)

    assert (_rc == 0)
    assert (current_con == test_con)

    # Remove the test file
    os.remove(test_path)

# Generated at 2022-06-12 23:59:59.132124
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    test_path = '/etc/passwd'
    try:
        (rc, con) = lgetfilecon_raw(test_path)
        assert rc >= 0
        assert con is not None
        assert ':'.join(['system_u', 'object_r', 'etc_t', 's0']) in con
    except:
        raise AssertionError


# Generated at 2022-06-13 00:00:02.702412
# Unit test for function matchpathcon
def test_matchpathcon():
    if security_getenforce() == 0:
        assert matchpathcon('/usr/bin/ping', 0) == [0, 'system_u:object_r:ping_exec_t:s0']


if __name__ == "__main__":
    test_matchpathcon()

# Generated at 2022-06-13 00:00:06.944155
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = b'//test'
    rc, con = lgetfilecon_raw(path)
    assert rc >= 0
    assert con is not None


# Generated at 2022-06-13 00:00:16.925067
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Initialize returns
    rc = -1
    context = None

    # Set up path
    path = '/tmp/selinux_getfilecon_raw'

    # Set up context
    context = 'system_u:object_r:tmp_t:s0'

    # Create a file with a context
    with open(path, 'w') as testfile:
        rc = lsetfilecon(path, context)  # 0 if successful

    # Verify file is created with context
    if rc == 0:
        (rc, file_context) = lgetfilecon_raw(path)
        if rc == 0:
            if file_context != context:
                rc = -1

    # Remove file
    os.remove(path)

    return rc



# Generated at 2022-06-13 00:00:18.884791
# Unit test for function matchpathcon
def test_matchpathcon():
    path = '/system/bin/toolbox'
    mode = 0o700
    rc, con = matchpathcon(path, mode)
    print(rc, con)



# Generated at 2022-06-13 00:00:22.973569
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    """Tests for getting file context"""
    (rc, context) = lgetfilecon_raw('/etc/passwd')
    assert rc >= 0
    assert context == 'system_u:object_r:etc_runtime_t:s0'


# Unit tests for function matchpathcon

# Generated at 2022-06-13 00:00:27.671943
# Unit test for function matchpathcon
def test_matchpathcon():
    import os
    import stat
    import tempfile
    from ansible.module_utils.selinux import matchpathcon

    path = tempfile.mktemp()
    os.close(os.open(path, os.O_CREAT))

    mode = os.stat(path).st_mode
    mode &= ~(stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    os.chmod(path, mode)

    (rc, con) = matchpathcon(path, 0)
    print("return code: %d\n" % rc)
    print("context: %s\n" % con)

# Generated at 2022-06-13 00:00:40.198645
# Unit test for function matchpathcon
def test_matchpathcon():
    """This test checks the functionality of matchpathcon"""
    result = matchpathcon('/etc/shadow', 0)
    assert result == [0, 'system_u:object_r:shadow_t:s0']
    result = matchpathcon('/etc/shadow', 2)
    assert result == [0, 'system_u:object_r:shadow_t:s0']
    result = matchpathcon('/etc', 0)
    assert result == [0, 'system_u:object_r:etc_t:s0']
    result = matchpathcon('/etc/shadow', 5)
    assert result == [0, 'system_u:object_r:shadow_t:s0']
    result = matchpathcon('/', 0)

# Generated at 2022-06-13 00:00:42.425141
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon(b'/etc/passwd', 0)
    assert rc == 0
    assert con == 'system_u:object_r:etc_runtime_t:s0'

# Generated at 2022-06-13 00:00:43.956868
# Unit test for function matchpathcon
def test_matchpathcon():
    [rc, con] = matchpathcon(b'/etc', 0)
    if rc == 0:
        print(con)
    else:
        print('unable to match path context')



# Generated at 2022-06-13 00:00:47.487569
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw('/etc/ssh/sshd_config')
    assert rc == 0
    assert con == 'system_u:object_r:etc_t:s0'


# Generated at 2022-06-13 00:00:56.278140
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Test on a file
    (rc, file_context) = lgetfilecon_raw(b'/etc/passwd')
    if rc != 0:
        raise Exception('lgetfilecon_raw(b"/etc/passwd") returned (%d): %s' % (rc, file_context))

    # Test on a directory
    (rc, file_context) = lgetfilecon_raw(b'/etc')
    if rc != 0:
        raise Exception('lgetfilecon_raw(b"/etc") returned (%d): %s' % (rc, file_context))

    # Test on a non-existing file
    (rc, file_context) = lgetfilecon_raw(b'/etc/non_existing_file')

# Generated at 2022-06-13 00:01:00.998036
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw('/usr/bin/pwd')
    assert rc == 0
    assert con == 'root:object_r:etc_runtime_t:s0'

# Generated at 2022-06-13 00:01:11.205288
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    from tempfile import mkstemp
    from ctypes import cdll, c_char_p, c_int, byref, POINTER

    libselinux = cdll.LoadLibrary('libselinux.so.1')
    lgetfilecon_raw = libselinux.lgetfilecon_raw
    lgetfilecon_raw.argtypes = [c_char_p, POINTER(c_char_p)]
    lgetfilecon_raw.restype = c_int
    freecon = libselinux.freecon
    freecon.argtypes = [c_char_p]
    freecon.restype = None
    con = c_char_p()

    (fd, fspath) = mkstemp()

# Generated at 2022-06-13 00:01:13.293767
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, xattr = lgetfilecon_raw(b'/proc')
    assert rc == 0
    assert xattr is not None



# Generated at 2022-06-13 00:01:20.146812
# Unit test for function matchpathcon
def test_matchpathcon():
    # valid context
    path = b'/usr/bin/rcp'
    mode = 0
    rc, con = matchpathcon(path, mode)
    assert rc == 0
    assert con == 'system_u:object_r:bin_t:s0'

    # valid context
    path = b'/bin/ls'
    mode = 0
    rc, con = matchpathcon(path, mode)
    assert rc == 0
    assert con == 'system_u:object_r:bin_t:s0'

    # invalid context
    path = b'/usr/bin/rcp'
    mode = 1
    rc, con = matchpathcon(path, mode)
    assert rc == 0
    assert con == 'system_u:object_r:bin_t:s0'

    # valid context - relabel
    path

# Generated at 2022-06-13 00:01:25.139536
# Unit test for function matchpathcon
def test_matchpathcon():
    result = matchpathcon('/tmp', 0)
    assert result[0] == 0
    assert result[1] == 'system_u:object_r:tmp_t:s0'

    result = matchpathcon('/tmp/', 0)
    assert result[0] == 0
    assert result[1] == 'system_u:object_r:tmp_t:s0'

# Generated at 2022-06-13 00:01:28.755115
# Unit test for function matchpathcon
def test_matchpathcon():
    # If you change the value to a file path without context label, the test will fail
    assert matchpathcon('/usr/bin/true', 0) == [0, 'system_u:object_r:bin_t:s0']



# Generated at 2022-06-13 00:01:32.928255
# Unit test for function matchpathcon
def test_matchpathcon():
    assert matchpathcon('/foo/bar', 0) == [0, u'system_u:object_r:tmp_t:s0']
    assert matchpathcon('/bin/bash', 0) == [0, u'system_u:object_r:bin_t:s0']



# Generated at 2022-06-13 00:01:35.003887
# Unit test for function matchpathcon
def test_matchpathcon():
    # Check that we correctly handle passing a path that doesn't exist
    (rc, value) = matchpathcon('/does/not/exist', 0)
    assert rc == -1

# Generated at 2022-06-13 00:01:37.251608
# Unit test for function matchpathcon
def test_matchpathcon():
    assert matchpathcon('/bin/ls', 0) == [0, 'system_u:object_r:bin_t:s0']
    assert matchpathcon('/doesnotexist', 0) == [-1, '']

# Generated at 2022-06-13 00:01:39.626186
# Unit test for function matchpathcon
def test_matchpathcon():
    path = '/selinux/context'
    mode = 0o777
    rc, con = matchpathcon(path, mode)
    assert con is not None

# Generated at 2022-06-13 00:01:48.846012
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (rc, out) = lgetfilecon_raw(b"/test")
    if rc == -1:
        err = get_errno()
        raise OSError(err, os.strerror(err))
    elif rc == -2:
        raise OSError('lgetfilecon_raw function does not exist')
    elif rc == 0:
        if out == b"system_u:object_r:usr_t:s0":
            return True
    return False


# Generated at 2022-06-13 00:01:52.246263
# Unit test for function matchpathcon
def test_matchpathcon():
    # This function returns a string, but only in the case when the
    # return code is 0. It is assumed that lsetfilecon will always
    # return a non-zero value when it fails.
    # pylint: disable=unsubscriptable-object
    # pylint: disable=invalid-sequence-index
    test_path = '/test/path'
    test_mode = 0
    assert matchpathcon(test_path, test_mode)[0] != 0



# Generated at 2022-06-13 00:01:59.375617
# Unit test for function matchpathcon
def test_matchpathcon():
    assert matchpathcon('/etc/shadow', 0) == [0, 'system_u:object_r:shadow_t']
    assert matchpathcon('/etc/shadow', os.R_OK) == [0, 'system_u:object_r:shadow_t']
    assert matchpathcon('/etc/shadow', os.W_OK) == [0, 'system_u:object_r:shadow_t']



# Generated at 2022-06-13 00:02:01.044901
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = '/tmp'
    rc, _con = lgetfilecon_raw(path)
    assert rc == 0

# Generated at 2022-06-13 00:02:08.454993
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    from tempfile import NamedTemporaryFile
    import os

    with NamedTemporaryFile() as fd:
        fd.write(b"unit test")
        fd.flush()
        os.fsync(fd)
        rc, current_context = lgetfilecon_raw(fd.name)
        assert rc == 0
        assert current_context is not None



# Generated at 2022-06-13 00:02:13.169000
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    test_path = "/dev/null"
    rc, con = lgetfilecon_raw(test_path)
    if rc == 0:
        print("context for %s is %s" % (test_path, con))
    else:
        print("Error getting context for %s" % test_path)



# Generated at 2022-06-13 00:02:15.618689
# Unit test for function matchpathcon
def test_matchpathcon():
    rc = _selinux_lib.matchpathcon("/tmp", 0)
    assert rc == 0
    if rc == 0:
        print("matchpathcon test passed")
    else:
        print("matchpathcon test failed")


# Generated at 2022-06-13 00:02:20.164972
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Test for function lgetfilecon_raw
    path = '/tmp/'
    rc, con = lgetfilecon_raw(path)
    return 'system_u:object_r:tmp_t:s0' in con


# Generated at 2022-06-13 00:02:27.012475
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon(b'/usr/bin/ls', 0)
    assert (rc, con) == (0, '/usr/bin/ls')
    assert isinstance(con, str)

    rc, con = matchpathcon(b'/usr/bin/ls', 1)
    assert (rc, con) == (0, 'system_u:object_r:usr_t:s0')
    assert isinstance(con, str)

# Generated at 2022-06-13 00:02:28.499033
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    return lgetfilecon_raw(b'/etc/passwd')


# Generated at 2022-06-13 00:02:38.689115
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    if (selinux_getenforcemode()[1] != 0):
        print("SELinux is enabled")
        fpath = "/tmp"
        print("Getting context for path %s:" % fpath)
        ret = lgetfilecon_raw(fpath)
        if ret[0] == -1:
            print("failed to get context path %s: %s" % (fpath, os.strerror(ret[0])))
            return ret
        print("context %s : %s" % (fpath, ret[1]))
    else:
        print("SELinux is disabled")
        return 0


# Generated at 2022-06-13 00:02:45.419137
# Unit test for function matchpathcon
def test_matchpathcon():
    import tempfile
    import shutil

    tmp_dir = tempfile.mkdtemp()
    try:
        tmp_file = os.path.join(tmp_dir, 'foo')
        with open(tmp_file, 'w') as f:
            f.write('test')

        assert matchpathcon(tmp_file, 0) == [0, 'test_t:test_t:s0']
        assert matchpathcon(tmp_dir, 0) == [0, 'test_t:test_t:s0']
    finally:
        shutil.rmtree(tmp_dir)



# Generated at 2022-06-13 00:02:49.335764
# Unit test for function matchpathcon
def test_matchpathcon():
    (rc, con) = matchpathcon('/usr/bin/make', 0)
    assert rc == 0, "returns rc 0"
    assert con == 'object_r:shell_exec_t', "returns con %s" % con


# Generated at 2022-06-13 00:02:50.898353
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    [rc, con] = lgetfilecon_raw('/etc/passwd')
    assert (rc == 0)
    assert (con.endswith(':object_r:etc_runtime_t:s0'))



# Generated at 2022-06-13 00:02:57.060986
# Unit test for function matchpathcon
def test_matchpathcon():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_dir, '..', '..')
    (rc, con) = matchpathcon(path, 0)
    if rc == 0 :
        print("Got matchpathcon %s" % (con))
    else:
        print("matchpathcon failed")


# Generated at 2022-06-13 00:03:03.304230
# Unit test for function matchpathcon
def test_matchpathcon():
    import os
    import tempfile

    # Create a file
    fd, f_matchpathcon = tempfile.mkstemp()
    os.close(fd)

    # Run function
    rc, con = matchpathcon(f_matchpathcon, os.R_OK)

    # Cleanup
    os.remove(f_matchpathcon)

    # Check if file was correctly labeled
    assert rc >= 0
    assert con.startswith('unconfined_u:object_r:')

# Generated at 2022-06-13 00:03:07.887805
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # FIXME: the below only works people run the testsuite with selinux enabled
    # we need a better way to test this function
    # currently this function only has one test (exists)
    path = '/var/log/audit/audit.log'
    rc, context = lgetfilecon_raw(path)
    assert rc == 0
    assert type(context) == str

# Generated at 2022-06-13 00:03:12.612478
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    ret = lgetfilecon_raw('/etc')
    assert ret[0] == 0
    assert ret[1] == 'system_u:object_r:etc_t:s0'

    # For Error path, return code should not be less than 0.
    ret = lgetfilecon_raw('/no/such/file')
    assert ret[0] >= 0

# Generated at 2022-06-13 00:03:14.365952
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = '/etc/selinux/targeted/policy/policy.30'
    assert lgetfilecon_raw(path)[1] is not None

# Generated at 2022-06-13 00:03:16.354402
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw('/usr/sbin/sshd') == [0, 'system_u:object_r:ssh_exe_t:s0']


# Generated at 2022-06-13 00:03:20.463582
# Unit test for function matchpathcon
def test_matchpathcon():
    path = "/tmp/test.txt"
    data = matchpathcon(path, 0)
    assert data[1] == "system_u:object_r:tmp_t:s0"

# Generated at 2022-06-13 00:03:24.398888
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    if os.path.exists("/usr/bin/strace"):
        with open("/usr/bin/strace", "r") as f:
            print("%s: %s" % (lgetfilecon_raw("/usr/bin/strace"), f.read()))
    else:
        assert False

# Generated at 2022-06-13 00:03:33.125257
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # check that the os module is working
    try:
        rc = os.getpid()
        if rc < 0:
            errno = get_errno()
            raise OSError(errno, os.strerror(errno))
    except OSError:
        raise ImportError('unable to run os.getpid() test, os module is broken')

    try:
        rc = lgetfilecon_raw('/proc/1/fd/1')
    except OSError:
        raise ImportError('unable to run lgetfilecon_raw(/proc/1/fd/1) test, function is broken')
    # check that the returned value is a list

# Generated at 2022-06-13 00:03:38.731686
# Unit test for function matchpathcon
def test_matchpathcon():
    """
    This function is used to test the matchpathcon function.
    """
    rc, con = matchpathcon(b"/etc/passwd", 0)
    assert rc == 0
    assert con == "system_u:object_r:passwd_file_t:s0"



# Generated at 2022-06-13 00:03:43.249643
# Unit test for function matchpathcon
def test_matchpathcon():
    path = "/etc/hosts"
    mode = 0
    rc, ret = matchpathcon(path, mode)
    assert ret == 'system_u:object_r:etc_runtime_t'

    rc, ret = selinux_getpolicytype()
    assert ret == 'targeted'

    rc, ret = selinux_getenforcemode()
    assert ret == 0

# Generated at 2022-06-13 00:03:45.873240
# Unit test for function matchpathcon
def test_matchpathcon():
    path = "/.ansible"
    mode = os.R_OK
    res = matchpathcon(path, mode)
    assert res, "Function call failed"


if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-13 00:03:47.709636
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert(lgetfilecon_raw("/etc/passwd") == [0, "system_u:object_r:etc_t:s0"])


# Generated at 2022-06-13 00:03:57.175068
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    """
    Unit test for lgetfilecon_raw function.
    """
    # Make sure we're on a system that supports SELinux
    if _selinux_lib.is_selinux_enabled() == 0:
        return

    # Get the full path to the test file
    dirname = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dirname, "unit_test_file")

    # Open the test file for writing
    with open(file_path, "w") as test_file:
        # Write a line to the file
        test_file.writelines("Hello World")

    # Get the SELinux context of the test file
    # The return value from lgetfilecon_raw should be 0 (success)
    # The second

# Generated at 2022-06-13 00:04:00.369305
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    [rc, con] = lgetfilecon_raw('/root/.bashrc')
    assert rc == 0
    assert con == 'unconfined_u:object_r:user_home_t:s0'


# Generated at 2022-06-13 00:04:04.745069
# Unit test for function matchpathcon
def test_matchpathcon():
    # Check that the function returns valid content
    (rc, context) = matchpathcon("/tmp/foo", 1)
    assert(rc == 0)
    assert(context == "staff_u:staff_r:staff_t:s0")



# Generated at 2022-06-13 00:04:11.839299
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = b'/dev/random'
    [rc, con] = lgetfilecon_raw(path)
    assert rc == 0, 'lgetfilecon_raw failed rc={0}'.format(rc)

# Testing lsetfilecon requires sudo privs to create a file in /tmp

# Generated at 2022-06-13 00:04:17.260532
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw('/etc/hosts')[1].endswith(b':object_r:etc_runtime_t')
    assert lgetfilecon_raw('/usr/bin/python3')[1].endswith(b':object_r:bin_t')

# Generated at 2022-06-13 00:04:22.683767
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw('/etc/passwd')[0] == 0
    assert lgetfilecon_raw('/etc/passwd')[1] == "system_u:object_r:passwd_file_t:s0"
    assert lgetfilecon_raw('/etc/hosts')[1] == "system_u:object_r:hosts_file_t:s0"



# Generated at 2022-06-13 00:04:33.229019
# Unit test for function matchpathcon
def test_matchpathcon():
    print(matchpathcon('/tmp/test', 0))
    print(matchpathcon('/tmp/test/', 0))
    print(matchpathcon('/tmp/test/', 0o700))
    print(matchpathcon('/tmp/test', 0o777))
    print(matchpathcon('/tmp/test', 0o711))
    print(matchpathcon('/tmp/test', 0o770))
    print(matchpathcon('/tmp/test', 0o777))
    print(matchpathcon('/tmp/test', 0o750))
    print(matchpathcon('/tmp/test/', 0o777))
    print(matchpathcon('/tmp/test/', 0o750))
    print(matchpathcon('/tmp/test/', 0o700))

# Generated at 2022-06-13 00:04:36.666220
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    files = ['/dev/log', '/etc/passwd', '/etc/shadow', '/etc/sshd_config']
    for f in files:
        rc, con = lgetfilecon_raw(f)
        assert rc >= 0

# Generated at 2022-06-13 00:04:45.588830
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    from tempfile import TemporaryFile
    from os import lstat
    from os.path import join
    from stat import S_ISCHR
    from pwd import getpwuid
    from grp import getgrgid

    RUN_TEST = os.environ.get("TEST_SELINUX", "False")
    if RUN_TEST == "False":
        return
    # Create a temporary file and write some chars to it
    tf = TemporaryFile()
    tf.write("abc".encode('ascii'))
    tf.close()

    # Set file context
    rc, con = lgetfilecon_raw(tf.name)
    assert rc == 0, "Failed to get file context: %s" % con

# Generated at 2022-06-13 00:04:47.516859
# Unit test for function matchpathcon
def test_matchpathcon():
    path = '/etc/selinux/targeted/policy/policy.30'
    mode = 0
    return matchpathcon(path, mode)



# Generated at 2022-06-13 00:04:49.382090
# Unit test for function matchpathcon
def test_matchpathcon():
    x = matchpathcon("/etc/passwd", 0)
    assert x[0] == 0
    assert x[1] != ""
    y = matchpathcon("/invalid/path", 0)
    assert y[0] == -13
    assert y[1] == ""

# Generated at 2022-06-13 00:04:53.487213
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw('/etc/shadow') == [0, 'system_u:object_r:shadow_t:s0']
    assert lgetfilecon_raw('/') == [0, 'system_u:object_r:root_t:s0']


# Generated at 2022-06-13 00:04:58.614102
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon("/etc/hosts", os.R_OK)
    print("rc = %d, con = %s" % (rc, con))
    assert rc == 0
    assert con == "system_u:object_r:etc_t:s0"


# Generated at 2022-06-13 00:05:04.340216
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = '/etc/shadow'
    rc, con = lgetfilecon_raw(path)
    print("con: %s" % con)
    assert isinstance(con, str)


# Generated at 2022-06-13 00:05:11.598875
# Unit test for function matchpathcon
def test_matchpathcon():
    from ansible_collections.community.general.tests.unit.compat.mock import mock_open, patch

    if not os.path.isfile("/selinux/policy"):
        # Run test only if /selinux/policy exists
        print("skipping test")
        return

    with patch('ansible_collections.community.general.plugins.modules.selinux_module.matchpathcon', side_effect=Exception):
        with patch('ansible_collections.community.general.plugins.modules.selinux_module.open', mock_open(read_data='\n')):
            assert matchpathcon('/foo', 0) == [-1, '']


# Generated at 2022-06-13 00:05:20.569153
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = os.path.join(os.sep, "var", "log", "messages")
    if not os.path.exists(path):
        raise Exception("Could not find file {}".format(path))
    rc, con = lgetfilecon_raw(path)    
    if rc != 0:
        raise Exception("Error calling function lgetfilecon_raw : rc={}".format(rc))
    print("Context of file {} is {}".format(path, con))


# Generated at 2022-06-13 00:05:23.822623
# Unit test for function matchpathcon
def test_matchpathcon():
    pkg_info = matchpathcon.__doc__

    if pkg_info is None:
        print('not a wrapper')
    else:
        print(pkg_info)


if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-13 00:05:27.733896
# Unit test for function matchpathcon
def test_matchpathcon():
    try:
        matchpathcon('/etc/passwd', 0)
    except TypeError:
        print('matchpathcon expects two arguments')

# Generated at 2022-06-13 00:05:32.844207
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = b'/etc/shadow'
    [rc, data] = lgetfilecon_raw(path)
    # NOTE: This test will fail on a multilevel system
    assert data == 'system_u:object_r:shadow_t:s0'

# Generated at 2022-06-13 00:05:35.261704
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon('/foo/bar', 0)
    assert rc == 0
    assert con == 'system_u:object_r:usr_t:s0'

# Generated at 2022-06-13 00:05:42.536692
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = b'/tmp'
    rc, ctx = lgetfilecon_raw(path)
    assert rc == 0, 'Test failed with error {0}'.format(rc)
    assert len(ctx) > 1, 'Test failed to return context for {0}'.format(path)
    assert ctx.endswith(b'\x00'), 'Test failed to return null-terminated context for {0}'.format(path)
    return


# Generated at 2022-06-13 00:05:45.669416
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    con = lgetfilecon_raw(b'/usr/bin/id')
    if con[0] == 0:
        print(con[1].decode())
    else:
        print('NO_EXIST')


# Generated at 2022-06-13 00:05:52.713862
# Unit test for function matchpathcon
def test_matchpathcon():

    try:
        fd = os.open('test_path', os.O_CREAT|os.O_RDWR)
        os.close(fd)
        path = os.path.abspath('test_path')
        os.remove(path)
    except Exception as e:
        print("Unable to create test path: %s" % str(e))
        return False

    try:
        rc, con = matchpathcon(path, 0)
    except Exception as e:
        print("Unable to call matchpathcon: %s" % str(e))
        return False

    if rc != 0:
        print("Unable to find context: %s" % str(con))
        return False

    print("Test context: %s" % str(con))

    return True


# Generated at 2022-06-13 00:05:57.295274
# Unit test for function matchpathcon
def test_matchpathcon():
    """Unit test for function matchpathcon"""
    print(matchpathcon('/etc/passwd', 0))



# Generated at 2022-06-13 00:06:07.373635
# Unit test for function matchpathcon
def test_matchpathcon():

    # valid path with default context
    rc, con = matchpathcon('/etc/hosts', os.F_OK)
    assert rc == 0, 'matchpathcon("/etc/hosts", os.F_OK) failed'
    assert con == 'system_u:object_r:etc_t:s0', 'matchpathcon("/etc/hosts", os.F_OK) failed to return system_u:object_r:etc_t:s0'

    # should fail
    rc, con = matchpathcon('/fake/dir', os.F_OK)
    assert rc != 0, 'matchpathcon("/fake/dir", os.F_OK) succeeded'

    # should fail
    rc, con = matchpathcon(1, os.F_OK)

# Generated at 2022-06-13 00:06:09.900807
# Unit test for function matchpathcon
def test_matchpathcon():
    (rc, con) = matchpathcon("/etc/passwd", 0)
    assert rc == 0
    assert con == "system_u:object_r:file_t:s0"



# Generated at 2022-06-13 00:06:12.719943
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (rc, con) = lgetfilecon_raw('/etc/passwd')
    assert rc == 0



# Generated at 2022-06-13 00:06:16.481480
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon('/var/www/html/demo', 0)
    assert rc >= 0, 'matchpathcon failed with {0}:{1}'.format(rc, con)
    print('context for /var/www/html/demo: {0}:{1}'.format(rc, con))


# Generated at 2022-06-13 00:06:20.315255
# Unit test for function matchpathcon
def test_matchpathcon():
    try:
        rc, con = matchpathcon("/tmp", 0)
        assert rc == 0
        assert con == "system_u:object_r:tmp_t:s0"
    except OSError as e:
        if not (e.errno == 22 and e.strerror == 'Invalid argument'):
            raise

# Generated at 2022-06-13 00:06:25.561928
# Unit test for function matchpathcon
def test_matchpathcon():
    import tempfile
    tmpDir = tempfile.mkdtemp()
    tmppath = '%s/test.txt' % tmpDir
    rc, con = matchpathcon(tmppath, 0)
    assert rc == 0
    assert con == 'unlabeled'
    with open(tmppath, 'w') as f:
        f.write('test')
    rc, con = matchpathcon(tmppath, 0)
    assert rc == 0
    assert con == 'user_tmp_t'
    rc, con = lgetfilecon_raw(tmppath)
    assert rc == 0
    assert con == 'user_tmp_t'

# Generated at 2022-06-13 00:06:32.611044
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    print('begin test_lgetfilecon_raw')
    test_path = '/'
    rc, result = lgetfilecon_raw(test_path)
    print('test_path: %s' % test_path)
    print('rc: %s' % rc)
    print('result: %s' % result)
    print('end test_lgetfilecon_raw\n')



# Generated at 2022-06-13 00:06:40.585582
# Unit test for function matchpathcon
def test_matchpathcon():
    """Unit test for function matchpathcon"""
    import tempfile
    import shutil

    tmpdir = tempfile.mkdtemp()
    tmpfile = os.path.join(tmpdir, 'foo')
    with open(tmpfile, 'w') as f:
        f.write('bar')

    try:
        assert _selinux_lib.matchpathcon(tmpdir, 0, None) == 0
        assert _selinux_lib.matchpathcon(tmpfile, 0, None) == 0
    finally:
        shutil.rmtree(tmpdir)

# Generated at 2022-06-13 00:06:49.785914
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    """Exercise lgetfilecon_raw"""
    path = b"/proc/uptime"
    [rc, con] = lgetfilecon_raw(path)
    assert rc < 0
    path = b"/var/log/lastlog"
    [rc, con] = lgetfilecon_raw(path)
    assert rc < 0
    #
    # NB: some paths may be unreadable on your system, such as in a container
    #     not running under root
    #
    path = b"/var/log"
    [rc, con] = lgetfilecon_raw(path)
    assert rc >= 0
    path = b"/var/log/lastlog"
    [rc, con] = lgetfilecon_raw(path)
    assert rc >= 0
    #
    # NB: some paths may

# Generated at 2022-06-13 00:06:54.750155
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw('/etc')
    assert isinstance(con, str)
    assert con.startswith('system_u:object_r')


# Generated at 2022-06-13 00:07:02.251331
# Unit test for function matchpathcon
def test_matchpathcon():
    # Test a directory that we know to have a selinux context
    dir_path = '/'
    mode = os.R_OK
    (rc, con) = selinux_getenforcemode()
    if rc == -1:
        print(con)
    elif con == 1:
        (rc, con) = matchpathcon(dir_path, mode)
        if rc == 0:
            print(con)
        elif rc == -1:
            print("{0} : {1}".format(dir_path, con))
        else:
            print("{0} : {1} - no match".format(dir_path, rc))
    else:
        print("SELinux enforcement is disabled")


if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-13 00:07:08.482500
# Unit test for function matchpathcon
def test_matchpathcon():
    exist_path = b'/etc/passwd'
    non_exist_path = b'/dev/null/non_exist'
    mode = 0

    # True case - path exist
    rc, con = matchpathcon(exist_path, mode)
    assert rc == 0
    assert con == 'system_u:object_r:etc_t:s0'

    # False case - path doesn't exist
    rc, con = matchpathcon(non_exist_path, mode)
    assert rc == -1
    assert con is None



# Generated at 2022-06-13 00:07:11.992657
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon('/etc/hosts', 0)
    assert rc == 0, 'Did not get context for /etc/hosts'
    assert con is not None, 'Did not get context for /etc/hosts'
    assert con != '', 'Context for /etc/hosts is empty'

# Generated at 2022-06-13 00:07:14.175677
# Unit test for function matchpathcon
def test_matchpathcon():
    sys.path.append('/tmp')
    import test_selinux
    test_selinux.selinux.matchpathcon('/some/path')



# Generated at 2022-06-13 00:07:20.167825
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    from ansible.module_utils.selinux import lgetfilecon_raw
    a = lgetfilecon_raw("/tmp/test")
    assert len(a) == 2
    assert a[0] == 0
    assert a[1] == "system_u:object_r:default_t"



# Generated at 2022-06-13 00:07:21.930056
# Unit test for function matchpathcon
def test_matchpathcon():
    # Test for function matchpathcon
    # Test for function matchpathcon
    matchpathcon('/tmp', 0)

# Generated at 2022-06-13 00:07:24.725282
# Unit test for function matchpathcon
def test_matchpathcon():
    import selinux
    rc, con = selinux.matchpathcon('/var/log/audit', selinux.SELINUX_ANDROID_LOG_DIR)
    print(rc, con)

# Generated at 2022-06-13 00:07:28.197576
# Unit test for function matchpathcon
def test_matchpathcon():
    path = "/tmp"
    mode = os.R_OK
    rc, con = matchpathcon(path, mode)
    if rc != 0:
        print("Got no context for matchpathcon")
        return False
    print(con)



# Generated at 2022-06-13 00:07:32.107142
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    try:
        rc, con = lgetfilecon_raw('/etc/passwd')
    except OSError as e:
        print(e.errno)
        print(e.filename)
        print(e.strerror)
        return 1
    print(rc)
    print(con)
    return 0


# Generated at 2022-06-13 00:07:41.463468
# Unit test for function matchpathcon
def test_matchpathcon():
    from tempfile import TemporaryFile

    path = b'/tmp/foo'
    mode = 0

    # open a tempfile and write random bytes to it
    try:
        with TemporaryFile() as f:
            f.write(b'foo')
            f.flush()
            # get its name
            path = f.name.encode('utf-8')
            rc, con = matchpathcon(path, mode)

            if rc < 0:
                raise OSError(to_native(os.strerror(rc)))

            print('tested function: matchpathcon')

    finally:
        # clean up tempfile
        os.unlink(path)



# Generated at 2022-06-13 00:07:43.011668
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    test_path = '/etc/selinux'
    rc, filecon = lgetfilecon_raw(test_path)
    assert rc == 0
    assert filecon



# Generated at 2022-06-13 00:07:48.116508
# Unit test for function matchpathcon
def test_matchpathcon():
    try:
        rc, con = matchpathcon('/var/log/lastlog', 0)
        assert rc == 0
        assert con == 'system_u:object_r:var_log_t:s0'
    except OSError as e:
        print(type(e))
        print(e)
        print('SELinux is not available (or misconfigured), skipping matchpathcon test')

# Generated at 2022-06-13 00:07:50.170759
# Unit test for function matchpathcon
def test_matchpathcon():
    path = "/usr/bin/python"
    [rc, con] = matchpathcon(path, 0)
    assert rc == 0 and con == "bin_t"


# Generated at 2022-06-13 00:07:54.554675
# Unit test for function matchpathcon
def test_matchpathcon():
    # test case 1
    [rc, con] = matchpathcon("/etc/cron.hourly/0yum-hourly.cron", 0)
    assert (rc >= 0 and con) is not None


__all__ = [
    'selinux_getenforcemode',
    'selinux_getpolicytype',
    'lgetfilecon_raw',
    'matchpathcon',
]

# Generated at 2022-06-13 00:07:57.169963
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    result = lgetfilecon_raw(b"/var/log/messages")
    assert result == [0, 'system_u:object_r:var_log_t:s0']
    assert type(result[1]) == str


# Generated at 2022-06-13 00:08:00.985142
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    result = lgetfilecon_raw('../../')
    if result[0] == 0:
        print('lgetfilecon_raw results: ' + result[1])
    else:
        print('lgetfilecon_raw failed, got error: ' + str(result[0]))



# Generated at 2022-06-13 00:08:05.768719
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
  # type: () -> None
  r"""
  This function is used to test the lgetfilecon_raw function in the selinux_state module.
  
  It runs test to check that the function returns the correct file context for a given path.
  
  The following paths are tested:
  /
  /var/run
  /var/lib
  """
  paths = ['/', '/var/run', '/var/lib']
  for path in paths:
    assert lgetfilecon_raw(path)[1] != ''

# Generated at 2022-06-13 00:08:15.638292
# Unit test for function matchpathcon
def test_matchpathcon():
    """
    Determines the context for the path, sysfs_path, under the current policy.
    Returns the valid context for path, sysfs_path, on success and
    an empty string on error.
    """
    context = ""
    mode = 0
    path = "/dev/sda"
    if not os.path.exists(path):
        return

    if not os.access(path, os.R_OK):
        test_matchpathcon.failure = "Could not access path: %s" % path
        return context


# Generated at 2022-06-13 00:08:18.294233
# Unit test for function matchpathcon
def test_matchpathcon():
    path = "/path/to/file"
    mode = 0o777
    rc = matchpathcon(path, mode)[0]

    if rc != 0:
        print("mismatchpathcon: failed to make assertions")
        sys.exit(1)

    print("matchpathcon: passed assertions")
    sys.exit(0)


if __name__ == "__main__":
    test_matchpathcon()

# Generated at 2022-06-13 00:08:28.731009
# Unit test for function matchpathcon
def test_matchpathcon():
    import os
    import tempfile

    # create temp file
    temp_file_handle, temp_file_path = tempfile.mkstemp()

    # get temp file's context
    temp_file_context = matchpathcon(temp_file_path, 0)[1]
    # get current directory's context
    current_dir_context = matchpathcon(os.getcwd(), 0)[1]
    # clean up
    os.remove(temp_file_path)

    # check result
    assert temp_file_context and temp_file_context == current_dir_context, "Matchpathcon returned wrong context"

# Generated at 2022-06-13 00:08:31.595181
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon('/dev/null', 0)
    assert rc == 0
    assert con == 'system_u:object_r:null_device_t:s0'



# Generated at 2022-06-13 00:08:33.945369
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    result = lgetfilecon_raw(b'/etc/passwd')
    if result[0] == 0:
        print(result[1])


# Generated at 2022-06-13 00:08:38.365067
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    """
    Test the lgetfilecon_raw function with a (possibly non existent) file
    """
    test_file = "/tmp/foo"
    (rc, con) = lgetfilecon_raw(test_file)
    if rc != -1:
        print(con)
        assert True
    else:
        print('test_lgetfilecon_raw failed')
        assert False


# Generated at 2022-06-13 00:08:40.826258
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    testpath = b'/etc/passwd'
    rc, context = lgetfilecon_raw(testpath)
    print(rc)
    print(context)
    if rc != 0:
        raise AssertionError('test failed')


# Generated at 2022-06-13 00:08:44.389545
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = 'tests/files/file_contexts'
    rc, con = lgetfilecon_raw(path)
    if rc != 0:
        raise AssertionError('lgetfilecon_raw({}) == {}'.format(path, rc))
    if con != 'system_u:object_r:svirt_sandbox_file_t:s0':
        raise AssertionError('lgetfilecon_raw() == {}'.format(con))


# Generated at 2022-06-13 00:08:48.504972
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = '/foo'
    try:
        con = c_char_p()
        rc = _selinux_lib.lgetfilecon_raw(path, byref(con))
        assert(rc == 0)
        assert(con.value == b'foo_u:foo_r:foo_t:s0')
    finally:
        _selinux_lib.freecon(con)


# Generated at 2022-06-13 00:08:51.078759
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import tempfile
    tempf = tempfile.NamedTemporaryFile()
    context = lgetfilecon_raw(tempf.name)
    assert context[0] == 0


# Generated at 2022-06-13 00:08:57.203530
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    if not is_selinux_enabled():
        return False, "SELinux is not enabled"

    (rc, filecon) = lgetfilecon_raw("/etc/shadow")
    if rc != 0:
        return False, "lgetfilecon_raw failed"
    if filecon != 'system_u:object_r:shadow_t:s0':
        return False, "lgetfilecon_raw did not return the correct SELinux context"

    return True, "lgetfilecon_raw succeeded"


# Generated at 2022-06-13 00:08:59.316998
# Unit test for function matchpathcon
def test_matchpathcon():
    path = '/etc/shadow'
    mode = os.R_OK
    rc, con = matchpathcon(path, mode)
    assert con == 'object_r:shadow_t:s0'

# Generated at 2022-06-13 00:09:09.540878
# Unit test for function matchpathcon
def test_matchpathcon():
    # test selinux_enabled
    assert security_getenforce() == is_selinux_enabled(), "SELinux is not enabled according to is_selinux_enabled()"
    assert security_getenforce() == is_selinux_mls_enabled(), "SELinux is not enabled and/or in mls mode according to is_selinux_mls_enabled()"
    assert len(selinux_getpolicytype()) == 2, "selinux_getpolicytype() return value is not of len 2"
    assert len(selinux_getenforcemode()) == 2, "selinux_getenforcemode() return value is not of len 2"
    assert security_policyvers() == 3, "SELinux policy version is not 3"