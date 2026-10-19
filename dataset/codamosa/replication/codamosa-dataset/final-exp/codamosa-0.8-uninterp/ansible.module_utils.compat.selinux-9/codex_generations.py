

# Generated at 2022-06-12 23:59:14.452667
# Unit test for function matchpathcon
def test_matchpathcon():
    dir_name = 'test_directory'
    file_name = 'test_file'

    # Test file
    if os.path.isdir(dir_name):
        os.rmdir(dir_name)
    os.mkdir(dir_name)
    os.chmod(dir_name, 0o755)
    with open(dir_name + '/' + file_name, 'w'):
        pass

    (rc, _) = matchpathcon(dir_name, 0)
    assert rc == 0

    # Test file
    (rc, con) = matchpathcon(dir_name + '/' + file_name, 0)
    assert rc == 0
    assert 'system_u:object_r:tmp_t' in con


# Generated at 2022-06-12 23:59:18.202715
# Unit test for function matchpathcon
def test_matchpathcon():
    [rc, con] = matchpathcon("/tmp/test.txt", 0)
    assert rc == 0
    return con


if __name__ == "__main__":
    print(test_matchpathcon())

# Generated at 2022-06-12 23:59:24.247390
# Unit test for function matchpathcon
def test_matchpathcon():
    # test file with context
    assert matchpathcon('/etc/hosts', os.R_OK)[0] == 0
    assert matchpathcon('/etc/hosts', os.W_OK)[0] != 0
    # test link with context
    assert matchpathcon('/etc/hosts.allow', os.R_OK)[0] == 0
    assert matchpathcon('/etc/hosts.allow', os.W_OK)[0] == 0



# Generated at 2022-06-12 23:59:30.508901
# Unit test for function matchpathcon
def test_matchpathcon():
    import tempfile
    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, 'foo')
        try:
            os.mkdir(path)
            rc, xcontext = matchpathcon(path, 0)
            assert(rc == 0)
            assert(xcontext is not None)
            assert(xcontext.find('system_u') == 0)
        finally:
            os.rmdir(path)

# Generated at 2022-06-12 23:59:34.997737
# Unit test for function matchpathcon
def test_matchpathcon():
    """
    Unit test for matchpathcon
    """
    for path in ['/etc/hosts', '/foo/bar/hosts', '/proc/sys/kernel/hostname']:
        rc, con = matchpathcon(path, 0)
        assert rc == 0, "{0} -- {1}".format(rc, con)

# Generated at 2022-06-12 23:59:37.390971
# Unit test for function matchpathcon
def test_matchpathcon():
    assert matchpathcon('/var/lib/nfs/sm', 0x06) == [0, 'system_u:object_r:nfs_t']

# Generated at 2022-06-12 23:59:47.242263
# Unit test for function matchpathcon
def test_matchpathcon():
    import os
    workdir = os.path.dirname(__file__)
    testdir = os.path.realpath(os.path.join(workdir, '..', 'lib'))
    (rc, con) = matchpathcon(testdir, os.R_OK)
    print(rc, con)
    assert rc == 0
    (rc, con) = matchpathcon(testdir, os.R_OK | os.W_OK)
    print(rc, con)
    assert rc == 0
    (rc, con) = matchpathcon(testdir, os.R_OK | os.W_OK | os.X_OK)
    print(rc, con)
    assert rc != 0

# Generated at 2022-06-12 23:59:51.652224
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (rc, pathcon) = lgetfilecon_raw('/etc/group')
    assert rc == 0
    (rc, pathcon) = lgetfilecon_raw('/dev/null')
    assert rc == 0
    (rc, pathcon) = lgetfilecon_raw('/etc/group-doesnotexist')
    assert rc == -1

# Generated at 2022-06-12 23:59:59.870140
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    try:
        import selinux
    except ImportError:
        return 0

    if not selinux.is_selinux_enabled():
        return 0

    # create a file named test in /tmp
    path = "/tmp/test"
    f = open(path, "w")
    f.close()

    # get its context
    result = lgetfilecon_raw(path)
    if result[0] in [0, 1]:
        if result[1] is None:
            return 100
    return 0


# Generated at 2022-06-13 00:00:03.064509
# Unit test for function matchpathcon
def test_matchpathcon():
    err, con = matchpathcon('/home/test/testfile', 0)
    assert err == -1
    assert not con
    err, con = matchpathcon('/home/test/testfile', 1)
    assert err == 0
    assert con

# Generated at 2022-06-13 00:00:11.013331
# Unit test for function matchpathcon
def test_matchpathcon():
    import tempfile
    with tempfile.NamedTemporaryFile() as f:
        assert matchpathcon(f.name, PySTAT.S_IFREG) == [0, 'unlabeled_t']


if __name__ == '__main__':
    import pytest
    sys.exit(pytest.main(['-s', __file__]))

# Generated at 2022-06-13 00:00:12.588593
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon('/tmp', 0)
    assert rc == 0
    assert con == 'system_u:object_r:tmp_t:s0'



# Generated at 2022-06-13 00:00:20.142475
# Unit test for function matchpathcon
def test_matchpathcon():
    from tempfile import mkstemp, mkdtemp
    from os import close, unlink, chmod, makedirs, rmdir, path
    from stat import S_IRWXU, S_IRWXO

    # Set up a temp directory with a temp file
    rwdir = mkdtemp()
    rwfile = mkstemp(dir=rwdir)
    close(rwfile[0])
    chmod(rwdir, S_IRWXU | S_IRWXO)
    chmod(rwfile[1], S_IRWXU | S_IRWXO)

    # Get the context for a rwdir/rwfile pair, and set the context for rwdir
    rwdircon = matchpathcon(rwdir, 0)[1]

# Generated at 2022-06-13 00:00:21.752294
# Unit test for function matchpathcon
def test_matchpathcon():
    result = matchpathcon("/home/ansible", 0)
    assert result[0] == 0

# Generated at 2022-06-13 00:00:30.476648
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import tempfile
    tmp = tempfile.NamedTemporaryFile()

    try:
        # Ensure tmp file exists
        rc, con = lgetfilecon_raw(tmp.name)
        assert rc == 0

        # Now change it's context
        rc = lsetfilecon(tmp.name, 'system_u:object_r:tmp_t:s0')

        # Ensure its context has changed
        rc, con = lgetfilecon_raw(tmp.name)
        assert rc == 0

        # Ensure it's context is tmp_t
        assert con == 'system_u:object_r:tmp_t:s0'
    except OSError:
        if is_selinux_enabled()[0] != 1:
            assert True
        else:
            assert False


# Generated at 2022-06-13 00:00:41.716635
# Unit test for function matchpathcon
def test_matchpathcon():
    # Call matchpathcon.
    (rc, retval) = matchpathcon('/tmp', os.R_OK)

    # Check return value and return code.
    print('retval: {0}, rc: {1}'.format(retval, rc))
    assert retval == 'system_u:object_r:tmp_t', 'Return value is wrong'
    assert rc == 0, 'Return code is wrong'

    # Call matchpathcon with bad mode value.
    (rc, retval) = matchpathcon('/tmp', 10)

    # Check return value and return code.
    print('retval: {0}, rc: {1}'.format(retval, rc))
    assert retval is None, 'Return value is wrong'
    assert rc == -1, 'Return code is wrong'

    sys.stdout.flush

# Generated at 2022-06-13 00:00:45.210438
# Unit test for function matchpathcon
def test_matchpathcon():
    p = '/tmp'
    m = 0o600
    result = matchpathcon(p, m)
    print(result)

# Generated at 2022-06-13 00:00:53.663844
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    from tempfile import NamedTemporaryFile

    with NamedTemporaryFile(prefix='ansible-tmp-', suffix='.txt') as file_obj:
        path = file_obj.name

    # test with no SELinux installed
    rc, result = lgetfilecon_raw(path)
    assert result == "<<none>>"
    assert rc == -1

    rc, policy = selinux_getpolicytype()
    assert rc == 0

    if policy.lower() != 'disabled':
        rc, result = lgetfilecon_raw(path)
        assert rc == 0
        assert result

    os.remove(path)

# Generated at 2022-06-13 00:00:55.902758
# Unit test for function matchpathcon
def test_matchpathcon():
    # Test function with invalid path
    assert matchpathcon('/invalid/path', 0)[0] == -1



# Generated at 2022-06-13 00:01:03.573724
# Unit test for function matchpathcon
def test_matchpathcon():
    # NB: this test is only applicable on systems that have SELinux enabled
    if not is_selinux_enabled():
        return

    # dump
    print("Enforcing mode = %d, MLS enabled = %d, policy version = %d, policy type = %s" % (
        security_getenforce(),
        is_selinux_mls_enabled(),
        security_policyvers(),
        selinux_getpolicytype()[1])
    )

    # test pathcon
    path = u"/tmp/testaaa"
    print("path = %s" % path)
    rc, mode = matchpathcon(path, os.R_OK)

# Generated at 2022-06-13 00:01:08.824664
# Unit test for function matchpathcon
def test_matchpathcon():
    path = b'/etc/httpd'
    mode = 0

    matchpathcon(path, mode)



# Generated at 2022-06-13 00:01:10.885134
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    """
    Unit test for function "lgetfilecon_raw"
    """
    (rc, message) = lgetfilecon_raw("/etc/hosts")
    print("rc = %d" % rc)
    print("message = %s" % message)



# Generated at 2022-06-13 00:01:15.439463
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import os
    import tempfile

    temp_file = tempfile.NamedTemporaryFile(buffering=0)
    temp_file.write(b'Hello World\n')
    temp_file.flush()
    context = lgetfilecon_raw(temp_file.name)[1]
    temp_file.close()
    assert context is not None, 'lgetfilecon_raw returned None context'

# Generated at 2022-06-13 00:01:17.834428
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = b'/tmp'
    r = lgetfilecon_raw(path)
    assert r[0] == 0
    assert r[1] == 'system_u:object_r:tmp_t:s0'


# Generated at 2022-06-13 00:01:25.399677
# Unit test for function matchpathcon
def test_matchpathcon():
    assert matchpathcon('/', 0) == [0, 'system_u:object_r:file_t:s0']
    assert matchpathcon('/', 1) == [0, 'system_u:object_r:file_t:s0']
    assert matchpathcon('/', 2) == [0, 'system_u:object_r:file_t:s0']
    assert matchpathcon('/tmp', 0) == [0, 'system_u:object_r:tmp_t:s0']
    assert matchpathcon('/tmp', 1) == [0, 'system_u:object_r:tmp_t:s0']
    assert matchpathcon('/tmp', 2) == [0, 'system_u:object_r:tmp_t:s0']

# Generated at 2022-06-13 00:01:32.494141
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = '/etc/passwd'
    try:
        [rc, con] = lgetfilecon_raw(path)
        if con:
            print('SELinux context for {0} is {1}'.format(path, con))
        else:
            print('No SELinux context for {0}'.format(path))
    except OSError as e:
        print('Cannot retrieve SELinux context for {0}: {1}'.format(path, to_native(e)))


# Generated at 2022-06-13 00:01:39.618054
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # NOTE: To test this, one needs to have at least a dummy filesystem mounted at /mnt
    # and set selinux context on /mnt such that it can be properly fetched.
    #
    # Example:
    #   mount -t tmpfs tmpfs /mnt
    #   touch /mnt/dummyfile
    #   chcon -t dummyfs_t /mnt
    #   chcon -t tmp_t /mnt/dummyfile

    fs_con = 'dummyfs_t:dummyfs_t:s0'
    file_con = 'tmp_t:tmp_t:s0'

    (rc1, con1) = lgetfilecon_raw('/mnt')
    assert rc1 >= 0
    assert con1 == fs_con

    (rc2, con2) = lget

# Generated at 2022-06-13 00:01:42.256433
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    if not lgetfilecon_raw('/etc/shadow')[0]:
        # If no application domains are defined the file context is `unlabeled`
        assert lgetfilecon_raw('/etc/shadow')[1] == 'unlabeled'



# Generated at 2022-06-13 00:01:50.309362
# Unit test for function matchpathcon
def test_matchpathcon():
    def test_pass(rc, con):
        assert rc == 0
        assert con

    def test_fail(rc, con):
        assert rc == -1
        assert not con

    tests = [
        ('/', 0, test_pass),
        ('/bin/ls', 0, test_pass),
        ('/bin/foo', 0, test_fail),
        ('/bin', 0, test_pass),
        ('/var/yum', 0, test_pass)
    ]

    for path, mode, cb in tests:
        rc, con = matchpathcon(path, mode)
        cb(rc, con)



# Generated at 2022-06-13 00:01:56.518846
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon("/etc/", 0)
    con_expected = "system_u:object_r:etc_t:s0"
    assert con == con_expected
    assert rc == 0


# Generated at 2022-06-13 00:02:03.186279
# Unit test for function matchpathcon
def test_matchpathcon():
    test_path = "/etc/hostname"
    e_test_path = to_bytes(test_path)
    mode = os.R_OK
    e_mode = c_int(mode)
    e_con = c_char_p()

    rc = _selinux_lib.matchpathcon(e_test_path, e_mode, byref(e_con))

    assert rc == 0

# Generated at 2022-06-13 00:02:05.815053
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = b'/etc/passwd'
    con = lgetfilecon_raw(path)
    assert con
    print(con)



# Generated at 2022-06-13 00:02:13.682116
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Creating a temporary file
    with open('file_context', 'w') as fp:
        fp.write('Object Class Label')
    con = c_char_p()
    try:
        rc = _selinux_lib.lgetfilecon_raw('file_context', byref(con))
        print (rc, con.value)
        assert rc == 0
    finally:
        _selinux_lib.freecon(con)


# Generated at 2022-06-13 00:02:20.346983
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # test for non directory
    path = "/etc/hosts"
    rc = lgetfilecon_raw(path)
    assert rc[0] == 0
    assert "system_u:object_r:etc_t:s0" in rc[1]
    # test for directory
    path = "/etc"
    rc = lgetfilecon_raw(path)
    assert rc[0] == 0
    assert "system_u:object_r:etc_t:s0" in rc[1]


# Generated at 2022-06-13 00:02:27.123696
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # This test is intended to be run as root
    # This test creates a file called test.txt ...
    try:
        os.system('touch test.txt')
        rc, con = lgetfilecon_raw('test.txt')
        assert 0 == rc and con == 'system_u:object_r:user_tmp_t:s0'
    finally:
        os.system('rm test.txt')


# Generated at 2022-06-13 00:02:30.256806
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = b'/sbin/init'
    result = lgetfilecon_raw(path)
    assert result == [0, b'system_u:system_r:init_t:s0']

# Generated at 2022-06-13 00:02:33.747378
# Unit test for function matchpathcon
def test_matchpathcon():
    assert lgetfilecon_raw(b'/')[0] == 0
    assert matchpathcon(b'/', 0)[0] == 0
    assert selinux_getpolicytype()[0] == 0

# Generated at 2022-06-13 00:02:38.387781
# Unit test for function matchpathcon
def test_matchpathcon():
    import selinux
    rc, con = selinux.matchpathcon("/tmp", selinux.S_IFREG)
    assert rc == 0, "matchpathcon failed"
    assert con is not None
    assert con != "", "matchpathcon returned invalid context"
    print("selinux_getpolicytype returned '%s'" % (con))



# Generated at 2022-06-13 00:02:43.606278
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path_name = "/etc"
    expected_con = "system_u:object_r:etc_t:s0"

    # NOTE: we wrap a call to an external selinux lib, so exercise a bit of caution
    if not is_selinux_enabled():
        return

    [rc, con] = lgetfilecon_raw(b"/etc")
    assert rc == 0
    assert con == expected_con


# Generated at 2022-06-13 00:02:52.333382
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import errno
    from ansible.module_utils.six.moves import builtins

    try:
        with builtins.open('/etc/fstab', 'r') as _:
            pass
    except IOError as e:
        if e.errno != errno.EACCES:
            raise

    print(lgetfilecon_raw('/etc/fstab'))
    print(lgetfilecon_raw('/tmp/doesnotexist'))

# Generated at 2022-06-13 00:03:02.670957
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    result = lgetfilecon_raw(b'/tmp')
    assert result[0] == 0
    assert result[1] == 'system_u:object_r:tmp_t:s0'


# Generated at 2022-06-13 00:03:05.406053
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw('/etc/passwd')[0] == 0
    assert lgetfilecon_raw('/etc/shadow')[0] == 0


# Generated at 2022-06-13 00:03:14.443420
# Unit test for function matchpathcon
def test_matchpathcon():
    res = matchpathcon(b'/path/', 0)
    assert res[0] == 0
    assert res[1]
    res = matchpathcon(b'/path/', 1)
    assert res[0] == 0
    assert res[1]
    res = matchpathcon(b'/path/', 2)
    assert res[0] == 0
    assert res[1]
    res = matchpathcon(b'/file1', 0)
    assert res[0] == 0
    assert res[1]
    res = matchpathcon(b'/file1', 1)
    assert res[0] == 0
    assert res[1]
    res = matchpathcon(b'/file1', 2)
    assert res[0] == 0
    assert res[1]

# Generated at 2022-06-13 00:03:19.051724
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Give file path as argument
    if __name__ == '__main__':
        path = sys.argv[1]
    else:
        path = "/etc/selinux/config"
    result = lgetfilecon_raw(path)
    if result[0] == -1:
        print('Error: %d, %s' % (result[0], os.strerror(result[0])))
    else:
        print(result[1])



# Generated at 2022-06-13 00:03:25.217955
# Unit test for function matchpathcon
def test_matchpathcon():
    """
    Test basic functionality of matchpathcon
    """
    (rc, con) = matchpathcon('/tmp', mode=0)
    if rc != 0:
        raise Exception('matchpathcon failed with rc=%d' % rc)
    if con == '':
        raise Exception('matchpathcon returned an empty string')
    return True


# Generated at 2022-06-13 00:03:32.522688
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import tempfile
    import os

    (fd, path) = tempfile.mkstemp()
    with os.fdopen(fd, 'w') as f:
        f.write('a test file')
    os.chmod(path, 0o644)
    path = path.encode('utf-8')
    rc, con = lgetfilecon_raw(path)
    assert rc == 0
    assert con == 'system_u:object_r:user_home_t:s0'
    rc, con = lsetfilecon(path, 'system_u:object_r:user_home_t:s0')
    assert rc == 0
    os.remove(path)

# Generated at 2022-06-13 00:03:36.851203
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = os.getcwd()
    res_val = lgetfilecon_raw(path)
    if res_val[0] != 0:
        raise Exception("lgetfilecon_raw failed")
    return res_val


# Generated at 2022-06-13 00:03:44.051394
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = '/etc/passwd'
    try:
        if is_selinux_enabled() != 0:
            [rc, con] = lgetfilecon_raw(path)
            if rc != -1:
                assert(con.startswith('system_u:object_r:etc_t:'))
            else:
                raise Exception('An error occurred when calling lgetfilecon_raw()')
        else:
            raise Exception('SELinux is not enabled')
    finally:
        _selinux_lib.freecon(con)


# Generated at 2022-06-13 00:03:48.104228
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Negative test: invalid path
    ret, context = lgetfilecon_raw('/invalid/path')
    assert ret == -1

    # Positive test: valid path
    ret, context = lgetfilecon_raw('/etc/selinux/config')
    assert ret == 0
    assert context



# Generated at 2022-06-13 00:03:54.485283
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import os
    for f in os.listdir('/'):
        (rc, con) = lgetfilecon_raw(os.path.join('/', f))
        if rc < 0:
            print(rc)
        else:
            if con.startswith('system_u:object_r:rootfs'):
                continue
            if con.startswith('unlabeled'):
                print(rc, f, con)
            else:
                print(rc, f, con)


# Generated at 2022-06-13 00:04:15.230966
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert len(lgetfilecon_raw("/srv/test_host")) == 2
    assert isinstance(lgetfilecon_raw("/srv/test_host")[0], int)
    assert isinstance(lgetfilecon_raw("/srv/test_host")[1], str)


# Generated at 2022-06-13 00:04:19.648958
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (rc, con) = lgetfilecon_raw("/etc/shadow")
    assert rc == 0, "lgetfilecon_raw failed"
    assert con == b"unconfined_u:object_r:shadow_t:s0", "Unexpected lgetfilecon_raw result"


# Generated at 2022-06-13 00:04:22.893674
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    """Test lgetfilecon_raw() wrapper function."""
    rc, con = lgetfilecon_raw(b'/')
    # rc = 0, con = None on selinux disabled systems
    assert rc in (0, -1)
    return 0



# Generated at 2022-06-13 00:04:25.820187
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, fcon = lgetfilecon_raw('/etc/selinux/config')
    assert rc == 0
    assert fcon == 'system_u:object_r:etc_t:s0'

# Generated at 2022-06-13 00:04:36.577974
# Unit test for function matchpathcon
def test_matchpathcon():

    import os
    import pytest

    tmpdir = os.path.dirname(os.getcwd())
    stat = os.stat(tmpdir)

    # Do a sanity check for the file we are about to create
    assert tmpdir is not None

    fname = tmpdir + '/ansible_matchpathcon_test_file'
    fd = os.open(fname, os.O_CREAT, 0o666)
    os.close(fd)

    # Test getting the context of a file in the system root
    mode = 0
    matchpathcon_result = matchpathcon(fname, mode)
    assert matchpathcon_result[0] == 0
    assert matchpathcon_result[1] == 'system_u:object_r:usr_t:s0'

    # Test that a bad path fails properly


# Generated at 2022-06-13 00:04:39.588236
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, context = matchpathcon('/etc/shadow', 0)
    assert rc == 0
    assert context == 'shadow_t'

# Generated at 2022-06-13 00:04:41.086480
# Unit test for function matchpathcon
def test_matchpathcon():
    assert matchpathcon('/etc/shadow', 0) == [0, 'shadow:shadow:r--']

# Generated at 2022-06-13 00:04:44.516319
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import tempfile

    test_temp_file = tempfile.NamedTemporaryFile()
    ans = lgetfilecon_raw(test_temp_file.name)
    assert ans[0] == 0
    assert 'system_u:object_r:user_tmp_t:s0' in ans[1]



# Generated at 2022-06-13 00:04:47.846915
# Unit test for function matchpathcon
def test_matchpathcon():
    # This test is expected to fail in selinux permissive
    from ansible.module_utils.selinux import matchpathcon
    rc, con = matchpathcon('/foo', os.R_OK)
    if rc == 0:
        return [False, con]
    else:
        return [True, con]


# Generated at 2022-06-13 00:04:59.402929
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # FIXME: add tests that use real world paths on disk
    #        i.e. in /usr/sbin or /home/foo/bar

    res, con = lgetfilecon_raw('/')
    assert res == 0

    res, con = lgetfilecon_raw('/usr/sbin')
    assert res == 0

    res, con = lgetfilecon_raw('/usr/local/bin')
    assert res == 0

    res, con = lgetfilecon_raw('/etc/passwd')
    assert res == 0

    res, con = lgetfilecon_raw('/dev/null')
    assert res == 0

    res, con = lgetfilecon_raw('/etc/selinux/targeted/contexts/users/system_u')
    assert res == 0

    #
   

# Generated at 2022-06-13 00:05:33.002266
# Unit test for function matchpathcon
def test_matchpathcon():
    """
    Print results of matchpathcon. This can give a good idea if the
    matchpathcon function is working.
    """
    rc, con = matchpathcon('/etc/passwd', 0)
    print('rc: {0}, con: {1}'.format(rc, con))
    rc, con = matchpathcon('/etc/passwd', 1)
    print('rc: {0}, con: {1}'.format(rc, con))



# Generated at 2022-06-13 00:05:34.819660
# Unit test for function matchpathcon
def test_matchpathcon():
    assert matchpathcon('/etc/passwd', 0) == [0, 'system_u:object_r:passwd_file_t:s0']



# Generated at 2022-06-13 00:05:45.543488
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import os
    import tempfile

    from tempfile import NamedTemporaryFile
    from ansible.module_utils.common.file import set_fs_attributes_if_different

    # code cribbed from ansible.module_utils.basic.py:_load_params()
    # which does the same in a more complicated context
    tmpdir = tempfile.gettempdir()
    tmpfile = os.path.join(tmpdir, NamedTemporaryFile().name)

    rc = 0
    old_con = con = None
    try:
        rc, old_con = lgetfilecon_raw(tmpfile)
    finally:
        if con:
            _selinux_lib.freecon(con)

    if rc >= 0 or old_con is not None:
        raise RuntimeError("expected error getting default context")


# Generated at 2022-06-13 00:05:48.121520
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (rc, con) = lgetfilecon_raw('/etc/selinux/config')
    if rc == 0:
        print(con)
    else:
        print('error')


# Generated at 2022-06-13 00:05:50.985447
# Unit test for function matchpathcon
def test_matchpathcon():
    assert matchpathcon('/usr/bin/python', 0)[0] == 0
    assert matchpathcon('/usr/bin/python', 0)[1] == 'system_u:object_r:usr_t:s0'


if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-13 00:05:54.063925
# Unit test for function matchpathcon
def test_matchpathcon():
    path = '/etc/shadow'
    mode = 0o100

    rc, con = matchpathcon(path, mode)
    assert rc == 0
    assert con == 'system_u:object_r:shadow_t:s0'



# Generated at 2022-06-13 00:05:56.930470
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = "/etc/hosts"
    rc, con = lgetfilecon_raw(path)
    assert rc == 0, "lgetfilecon_raw for %s failed" % path
    print("SELinux context for %s is %s" % (path, con))



# Generated at 2022-06-13 00:06:07.116447
# Unit test for function matchpathcon
def test_matchpathcon():
    """
        Test the function matchpathcon
    """
    # Check return value
    ret, con = matchpathcon("/home/foo/bar", 0)
    assert ret == 0
    assert con == "user_home_dir_t"

    # Check return value for path not exist
    ret, con = matchpathcon("/home/foo/bar2", 0)
    assert ret == 2
    assert con == "system_u:object_r:file_t:s0"

    # Check return value when path is a dir
    ret, con = matchpathcon("/home/foo/", 0)
    assert ret == 0
    assert con == "user_home_dir_t"

    # Check return value when path is a link
    ret, con = matchpathcon("/home/foo/bar/bar", 0)

# Generated at 2022-06-13 00:06:12.530130
# Unit test for function matchpathcon
def test_matchpathcon():
    # This tests for a matchpathcon failure on a file that does not exist
    [rc, context] = matchpathcon("/tmp/foo/bar", os.R_OK)
    assert rc == -1, 'Expected matchpathcon return value -1, got {0}'.format(rc)
    assert context == '', 'Expected matchpathcon context value empty string, got {0}'.format(context)

# Generated at 2022-06-13 00:06:17.974794
# Unit test for function matchpathcon
def test_matchpathcon():
    # Test if testpath exists and is a symbolic link
    testpath = '/etc/systemd/system/multi-user.target.wants/systemd-networkd.service'
    if os.path.islink(testpath):
        assert matchpathcon(testpath, 0) == [0, 'system_u:system_r:networkd_t:s0-s0:c0.c1023']
    else:
        print('No symbolic link found to test matchpathcon')

# Generated at 2022-06-13 00:07:33.347095
# Unit test for function matchpathcon
def test_matchpathcon():
    """Unit test of matchpathcon function"""
    import tempfile
    tf = tempfile.NamedTemporaryFile()
    rc, context = matchpathcon(tf.name, os.R_OK)
    assert rc == 0
    assert context == 'unconfined_u:object_r:user_tmp_t:s0'


# Generated at 2022-06-13 00:07:36.184175
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon('/etc/httpd/conf.d/', 0)
    assert rc == 0
    assert con == 'httpd_sys_content_t'

# Generated at 2022-06-13 00:07:43.322672
# Unit test for function matchpathcon
def test_matchpathcon():
    assert matchpathcon(b'/tmp/foo', 0) == [0, 'system_u:object_r:tmp_t']
    assert matchpathcon(b'/tmp/foo', 1) == [0, 'system_u:object_r:tmp_t:s0']
    assert matchpathcon(b'/etc/foo', 0) == [0, 'system_u:object_r:etc_runtime_t']
    assert matchpathcon(b'/etc/foo', 1) == [0, 'system_u:object_r:etc_runtime_t:s0']
    assert matchpathcon(b'/etc/bar', 0) == [0, 'system_u:object_r:etc_t']

# Generated at 2022-06-13 00:07:48.627616
# Unit test for function matchpathcon
def test_matchpathcon():
    try:
        import selinux
        rc, con = matchpathcon(b'/', 0)
        assert rc == 0, 'matchpathcon failed'
        assert con
        print('matchpathcon returned: {0}'.format(con))

    except ImportError as e:
        print('skipping import error: {0}'.format(repr(e)))


if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-13 00:07:51.550120
# Unit test for function matchpathcon
def test_matchpathcon():
    path = '/etc/test'
    mode = 0

    rct = matchpathcon(path, mode)
    print("Path: %s\nMode: %s\nRCT: %s\n" % (path, mode, rct))



# Generated at 2022-06-13 00:07:58.520916
# Unit test for function matchpathcon
def test_matchpathcon():
    # cf. https://github.com/ansible/ansible/issues/91213

    path = "/etc/fstab"
    rc, con = matchpathcon(path, 0)
    if rc < 0:
        # On Fedora Core, the SELinux policy currently (2004-03-05)
        # only defines ownership mappings for files in / and /usr.
        # Therefore, matchpathcon will fail for /etc/fstab with
        # errno ENOENT.  We expect to get this error, so we simply
        # ignore it.
        import errno
        if rc != -errno.ENOENT:
            raise OSError(rc, "error in matchpathcon")
    else:
        print(con)



# Generated at 2022-06-13 00:08:06.247280
# Unit test for function matchpathcon
def test_matchpathcon():
    # Create a temp file, get it's context and write it to a file
    (rc, con) = matchpathcon("/tmp/test.txt", os.R_OK)
    assert rc == 0
    assert con == u"system_u:object_r:user_tmp_t:s0"
    (rc, con) = matchpathcon("/tmp/test.txt", os.R_OK | os.W_OK)
    assert rc == 0
    assert con == u"system_u:object_r:user_tmp_t:s0"
    (rc, con) = matchpathcon("/tmp/test.txt", os.R_OK | os.W_OK | os.X_OK)
    assert rc == 0

# Generated at 2022-06-13 00:08:09.836429
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw(b'/var/log')

    print('lgetfilecon_raw: rc={0} con={1}'.format(rc, con))



# Generated at 2022-06-13 00:08:12.630834
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (rc, con) = lgetfilecon_raw("/bin/ls")

    assert rc == 0
    assert "system_u:object_r:bin_t:s0" in con


# Generated at 2022-06-13 00:08:15.701545
# Unit test for function matchpathcon
def test_matchpathcon():
    """
    test_selinux.py
    ~~~~~~~~~~~~~~~

    :copyright: (c) 2017 by the Ansible Project.
    :license: GPLv3, see LICENSE for more details.
    """
    path = "/etc/shadow"
    mode = 0

    result = matchpathcon(path, mode)

    expected_result = [0, 'system_u:object_r:shadow_t:s0']
    assert result == expected_result, \
        "matchpathcon failed: {}".format(result)