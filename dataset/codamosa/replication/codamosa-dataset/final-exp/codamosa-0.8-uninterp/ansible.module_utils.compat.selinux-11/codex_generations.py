

# Generated at 2022-06-12 23:59:09.971868
# Unit test for function matchpathcon
def test_matchpathcon():
    ret, value = matchpathcon('/etc/passwd', 0)
    assert ret == 0, "matchpathcon failed"
    assert value == 'system_u:object_r:etc_runtime_t:s0', "unexpected output"



# Generated at 2022-06-12 23:59:15.231692
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (rc, con) = lgetfilecon_raw('/etc/services')
    if rc < 0:
        raise OSError(get_errno(), os.strerror(get_errno()))
    return con



# Generated at 2022-06-12 23:59:25.384478
# Unit test for function matchpathcon
def test_matchpathcon():

    # test for a file that is present in the policy
    assert matchpathcon('/bin/ls', os.F_OK)[1] == 'system_u:object_r:bin_t'

    # test for a file that is not present in the policy
    assert matchpathcon('/usr/bin/foobar', os.F_OK)[1] == 'system_u:object_r:usr_t'

    # test for a directory that is present in the policy
    assert matchpathcon('/usr', os.F_OK)[1] == 'system_u:object_r:usr_t'

    # test for a directory that is not present in the policy
    assert matchpathcon('/usr/bin', os.F_OK)[1] == 'system_u:object_r:usr_t'

    # test for a non-existent

# Generated at 2022-06-12 23:59:27.665658
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (rc, con) = lgetfilecon_raw('/etc/fstab')
    assert rc == 0
    assert con != ''

# Generated at 2022-06-12 23:59:31.473404
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = '/boot'
    res = lgetfilecon_raw(path)
    valid_answer = ['system_u:object_r:boot_t:s0', 0]
    return [res[1], res[0]] == valid_answer


# Generated at 2022-06-12 23:59:38.484826
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    try:
        # Try to get the lgetfilecon_raw for a file that exists
        test_path = "/etc/selinux/config"
        rc, con = lgetfilecon_raw(test_path)
        assert rc == 0
        assert 'system_u:object_r:selinux_etc_t:s0' in con

        # Try to get the lgetfilecon_raw for a file that doesn't exists
        test_path = "/foo/bar"
        rc, con = lgetfilecon_raw(test_path)
        assert rc == -1
    except:
        print('test_lgetfilecon_raw() failed')


# Generated at 2022-06-12 23:59:42.818488
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    name = b'/var/empty'
    rc, context = lgetfilecon_raw(name)
    assert rc == 0

    assert len(context) > 0, 'failed to lookup context of path %s' % name



# Generated at 2022-06-12 23:59:45.515101
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon('/tmp', 0)
    assert con == 'system_u:object_r:tmp_t:s0'
    assert rc == 0



# Generated at 2022-06-12 23:59:50.998067
# Unit test for function matchpathcon
def test_matchpathcon():
    results = matchpathcon("/etc/hosts", 0)
    if results[0] != 0:
        print("failed: {0}".format(results[0]))
        sys.exit(1)
    if results[1] == None:
        print("failed: {0}".format(results[1]))
        sys.exit(1)
    print("passed")


if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-12 23:59:55.108998
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import os
    (rc, con) = lgetfilecon_raw("/etc/passwd")
    assert rc == 0
    assert con is not None
    assert len(con) > 0



# Generated at 2022-06-13 00:00:01.757127
# Unit test for function matchpathcon
def test_matchpathcon():
    path = '/usr/sbin/sshd'
    mode = os.stat(path).st_mode
    if not mode & stat.S_IFDIR:
        mode = stat.S_IFREG
    (rc, con) = matchpathcon(path, mode)
    print('matchpathcon:', rc, con)



# Generated at 2022-06-13 00:00:07.890091
# Unit test for function matchpathcon
def test_matchpathcon():
    # This test uses a temporary file under the system's tmp directory.
    import tempfile
    with tempfile.NamedTemporaryFile() as f:
        rcd, s = matchpathcon(f.name, 0)
        if rcd < 0:  # if error
            rcd, s = matchpathcon(f.name, 1)  # try again
    return rcd


if __name__ == '__main__':
    rc = test_matchpathcon()
    print(rc)

# Generated at 2022-06-13 00:00:10.968660
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    stat = lgetfilecon_raw('/')
    assert stat[0] == 0
    assert stat[1] == 'system_u:object_r:root_t:s0'



# Generated at 2022-06-13 00:00:12.683544
# Unit test for function matchpathcon
def test_matchpathcon():
    print(matchpathcon('/var', 0))



# Generated at 2022-06-13 00:00:19.316307
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    sys.stdout.write('Test of lgetfilecon_raw\n')
    for path in ['.', '/dev/null']:
        if os.path.exists(path):
            sys.stdout.write('Path: {}\n'.format(path))
            rc, con = lgetfilecon_raw(path)
            sys.stdout.write('Return code: {}\n'.format(rc))
            sys.stdout.write('Context: {}\n'.format(con))
            sys.stdout.write('\n')
        else:
            sys.stdout.write('Path {} does not exist.\n'.format(path))
            sys.stdout.write('\n')

# Generated at 2022-06-13 00:00:23.149207
# Unit test for function matchpathcon
def test_matchpathcon():
    (rc, con) = matchpathcon('/etc/passwd', os.R_OK)
    print(rc)
    print(con)

    (rc, con) = lgetfilecon_raw('/etc/passwd')
    print(rc)
    print(con)

# Generated at 2022-06-13 00:00:26.816324
# Unit test for function matchpathcon
def test_matchpathcon():
    """Test for function matchpathcon."""
    libselinux = sys.modules[__name__]
    rc, value = libselinux.matchpathcon('/tmp/test_matchpathcon', 1)
    assert rc == 0
    assert value == 'user_tmp_t'



# Generated at 2022-06-13 00:00:33.968867
# Unit test for function matchpathcon
def test_matchpathcon():
    test_path = "/usr/bin/htop"
    test_mode = 0
    test_rc, test_con = matchpathcon(test_path, test_mode)
    print("matchpathcon() returned: [{0}, {1}]".format(test_rc, test_con))
    assert test_rc == 0
    assert test_con == "unconfined_u:object_r:usr_t:s0"


# Generated at 2022-06-13 00:00:38.603232
# Unit test for function matchpathcon
def test_matchpathcon():
    path = '/tmp/selinux'
    mode = 0
    rc, con = matchpathcon(path, mode)
    assert rc == 0
    assert con == 'system_u:object_r:tmp_t:s0'
    return 0

# unit test for function lgetfilecon_raw

# Generated at 2022-06-13 00:00:44.368397
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (rc, con) = lgetfilecon_raw('/etc/localtime')
    print('return code: %d' % rc)
    print('context: %s' % con)
    print('')

    (rc, con) = lgetfilecon_raw('/etc/hostname')
    print('return code: %d' % rc)
    print('context: %s' % con)
    print('')

    (rc, con) = lgetfilecon_raw('/etc/passwd')
    print('return code: %d' % rc)
    print('context: %s' % con)
    print('')

    (rc, con) = lgetfilecon_raw('/etc/group')
    print('return code: %d' % rc)

# Generated at 2022-06-13 00:00:51.011954
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw("/etc/issue")
    assert rc == 0
    assert con == "system_u:object_r:etc_runtime_t:s0"

# Generated at 2022-06-13 00:00:53.663046
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw(b'/')
    assert rc == 0
    assert isinstance(con, str)

# Generated at 2022-06-13 00:00:58.705260
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = "/etc/passwd"
    [rc, con] = lgetfilecon_raw(path)
    assert hasattr(rc, "__iter__")
    assert len(rc) == 2
    assert rc[0] == 0
    assert rc[1] == "system_u:object_r:passwd_file_t:s0"
    assert con == rc[1]


# Generated at 2022-06-13 00:01:03.373942
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    if os.geteuid() != 0:
        raise OSError('This test must be run as root')
    # Test a read-only path
    path = '/usr/lib/python2.7/site-packages/ansible/modules/network/vyos/vyos_l2_interface.py'
    rc, con_value = lgetfilecon_raw(path)
    assert rc == -1
    assert os.strerror(os.errno) == 'Operation not permitted'



# Generated at 2022-06-13 00:01:08.651232
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = 'selinux_test.py'
    con = c_char_p()
    res = lgetfilecon_raw(path)
    if res[0] != 0:
        print(res[0])
        res = lgetfilecon_raw(path)
        print(selinux_getpolicytype())
        print(res[1])
    else:
        print(res[1])

# Generated at 2022-06-13 00:01:16.417898
# Unit test for function matchpathcon
def test_matchpathcon():
    from contextlib import contextmanager
    from tempfile import mkdtemp
    from shutil import rmtree

    @contextmanager
    def tmpdir():
        try:
            td = mkdtemp()
            yield td
        finally:
            rmtree(td)

    with tmpdir() as td:
        # Get the default context
        rc, context = matchpathcon(td, 0)
        assert rc == 0

        # Set the context to the default context
        rc = _selinux_lib.lsetfilecon(td, context)
        assert rc == 0

        # Verify that setting the context returned the same context
        rc, context2 = lgetfilecon_raw(td)
        assert rc == 0
        assert context2 == context



# Generated at 2022-06-13 00:01:22.238664
# Unit test for function matchpathcon
def test_matchpathcon():

    matchpathcon(path='/sbin/modprobe', mode=0)
    matchpathcon(path='/sbin/modprobe', mode=1)
    matchpathcon(path='/sbin/modprobe', mode=2)
    matchpathcon(path='/sbin/modprobe', mode=3)
    matchpathcon(path='/sbin/modprobe', mode=-1)
    matchpathcon(path='/sbin/modprobe', mode=-2)

    try:
        matchpathcon(path=2, mode=3)
        assert False, 'Expected exception: TypeError'
    except TypeError:
        raise


# Generated at 2022-06-13 00:01:33.392525
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import tempfile
    import shutil
    import errno

    dir_path = tempfile.mkdtemp()
    file_path = os.path.join(dir_path, "tmp-file")

    # test_file is generated by Selinux enforcement mode 'permissive'
    try:
        test_file = open(file_path, "w")
        test_file.close()
    except EnvironmentError as e:
        if e.errno == errno.EACCES:
            raise ImportError("No permission to write in current directory")

    try:
        # lgetfilecon_raw will fail if selinux is not enabled
        rc, con = lgetfilecon_raw(file_path)
        assert rc == 0
        assert con is not None
    except OSError:
        pass

    shutil.rmt

# Generated at 2022-06-13 00:01:35.507173
# Unit test for function matchpathcon
def test_matchpathcon():
    path = '/usr/bin/passwd'
    mode = 0
    rc, con = matchpathcon(path, mode)
    print('matchpathcon({0}, {1}) == {2}, {3}'.format(path, mode, rc, con))

# Generated at 2022-06-13 00:01:39.753457
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    from ansible.module_utils._text import to_text
    from ansible.module_utils.common.sys_info import SUPPORTS_SELINUX_PYTHON
    if SUPPORTS_SELINUX_PYTHON:
        CON = "user_u:object_r:user_tmp_t:s0"
        result = lgetfilecon_raw(b"/tmp")
        assert result[0] == 0
        assert to_text(result[1]) == CON

# Generated at 2022-06-13 00:01:47.446983
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, retpath = lgetfilecon_raw('/usr/sbin/ip6tables')
    print(rc, retpath)
    assert rc == 0 and 'system_u:object_r:ip6tables_exec_t:s0' in retpath


# Generated at 2022-06-13 00:01:49.575999
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw('/etc/passwd') == [0, 'unconfined_u:object_r:etc_t:s0']



# Generated at 2022-06-13 00:01:50.882912
# Unit test for function matchpathcon
def test_matchpathcon():
    if not os.path.isdir("/tmp"):
        return True
    else:
        return matchpathcon("/tmp", 0)

# Generated at 2022-06-13 00:02:02.932559
# Unit test for function lgetfilecon_raw

# Generated at 2022-06-13 00:02:12.641936
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = os.environ.get('PATH')
    if path is None:
        raise KeyError('must have PATH environment variable set')

    # Normally we wouldn't validate the return code (it's done in the function)
    # but we need to verify that SELinux is actually available on the system
    rc, con = lgetfilecon_raw(path)
    if rc < 0:
        raise OSError(rc, os.strerror(rc))

    if isinstance(con, bytes):
        con = to_native(con)

    assert con



# Generated at 2022-06-13 00:02:15.219317
# Unit test for function matchpathcon
def test_matchpathcon():
    import os
    rc, context = matchpathcon('/usr/', 0)
    if rc < 0:
        raise OSError('Could not retrieve context: {0}'.format(context))
    os.setfilecon('/usr/', context)

# Generated at 2022-06-13 00:02:16.196903
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    return lgetfilecon_raw('/tmp')


# Generated at 2022-06-13 00:02:26.865923
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import tempfile
    tmpdir = tempfile.mkdtemp(prefix="ansible_test_selinux_")
    try:
        path = os.path.join(tmpdir, 'foo')
        with open(path, 'w') as f:
            f.write("test content")
        rc, con = lgetfilecon_raw(path)
        print("SELinux context for %s is %s" % (path, con))
    finally:
        os.unlink(path)
        os.rmdir(tmpdir)

if __name__ == '__main__':
    test_lgetfilecon_raw()

# Generated at 2022-06-13 00:02:29.425055
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = "/var/log/ansible.log"
    actual_rc, actual_con = lgetfilecon_raw(path)
    if actual_rc == 0:
        print("File Context for %s is: %s" % (path, actual_con))
    else:
        print("Error getting context for %s" % path)


# Generated at 2022-06-13 00:02:32.217439
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon("/tmp/this-file-does-not-exist", 0)
    assert rc == -1
    assert con is None



# Generated at 2022-06-13 00:02:45.280318
# Unit test for function matchpathcon
def test_matchpathcon():
    """
    Test if selinux wrapper functions are working properly
    """

    # test on a directory
    results = matchpathcon('/etc', 0)

    if results[0] != 0:
        raise Exception('selinux matchpathcon error: {}'.format(to_native(os.strerror(results[0]))))

    if not results[1].startswith('system_u:object_r:'):
        raise Exception('selinux matchpathcon failed: {}'.format(results[1]))

    # test on a file
    results = matchpathcon('/etc/passwd', 0)
    if results[0] != 0:
        raise Exception('selinux matchpathcon error: {}'.format(to_native(os.strerror(results[0]))))


# Generated at 2022-06-13 00:02:54.627343
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    try:
        import selinux
    except ImportError:
        return

    import tempfile
    import shutil
    tempdir = tempfile.mkdtemp()
    try:
        filepath = "test_file"
        path = os.path.join(tempdir, filepath)
        open(path, "w").close()

        output = lgetfilecon_raw(path)
        assert output[0] == 0
        assert output[1] == "system_u:object_r:unlabeled_t:s0"
    finally:
        shutil.rmtree(tempdir)

# Generated at 2022-06-13 00:02:55.611031
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw('/etc/hosts')

# Generated at 2022-06-13 00:03:05.041182
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = '/tmp/selinux-python-test'

    rc = _selinux_lib.fsetfilecon(path, b'system_u:object_r:user_tmp_t:s0')
    if rc != 0:
        if rc != -1:
            raise OSError(rc, os.strerror(rc))
        else:
            errno = get_errno()
            if errno == 95:
                # fsetfilecon failed because selinux is not enabled
                return False
            if errno == 95:
                raise OSError(errno, os.strerror(errno))
            else:
                # Other error, raise error
                raise OSError(errno, os.strerror(errno))


# Generated at 2022-06-13 00:03:09.528865
# Unit test for function matchpathcon
def test_matchpathcon():
    path = b'/tmp/testfile'
    mode = 1
    try:
        _selinux_lib.matchpathcon(path, mode, None)
        return False
    except OSError as e:
        # In CentOS 7, error code 22 is returned, that corresponds to EINVAL.
        return e.errno == 22

# Generated at 2022-06-13 00:03:12.081594
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon('/etc/foo/bar', 0)
    assert rc == 0
    assert con == 'system_u:object_r:etc_t:s0'



# Generated at 2022-06-13 00:03:20.856436
# Unit test for function matchpathcon
def test_matchpathcon():
    rc = _selinux_lib.matchpathcon("/etc/hosts", 0, None)
    assert rc == -1

    # FIXME: update unit test when the function is wrapped
    # con = c_char_p()
    # try:
    #     rc = _selinux_lib.matchpathcon("/etc/hosts", 0, byref(con))
    #     assert rc == 0
    #     assert to_native(con.value) == "system_u:object_r:etc_hosts_t:s0"
    #     rc = _selinux_lib.matchpathcon("/dev/null", 0, byref(con))
    #     assert rc == 0
    #     assert to_native(con.value) == "system_u:object_r:null_device_t:s

# Generated at 2022-06-13 00:03:26.275441
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon("/home/user1/dir1", 0)
    print("rc: %s" % str(rc))
    print("con: %s" % str(con))


if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-13 00:03:29.225495
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (rc, con) = lgetfilecon_raw('/tmp')
    assert rc == 0
    assert con == 'system_u:object_r:tmp_t:s0'


# Generated at 2022-06-13 00:03:31.064861
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon(b'/tmp', 0)
    assert rc == 0
    assert con == 'system_u:object_r:tmp_t:s0'


# Generated at 2022-06-13 00:03:45.149393
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    class testFile:
        def __init__(self, path):
            self.path = path
            self.mode = 0o644

    file_contexts = '/tmp/test-file_contexts'
    file_contexts_copy = '/tmp/test-file_contexts_copy'

    test_file = '/tmp/test-file'
    test_file_copy = '/tmp/test-file_copy'

    dir_contexts = '/tmp/test-dir_contexts'
    dir_contexts_copy = '/tmp/test-dir_contexts_copy'

    test_dir = '/tmp/test-dir'
    test_dir_copy = '/tmp/test-dir_copy'


# Generated at 2022-06-13 00:03:54.525275
# Unit test for function matchpathcon
def test_matchpathcon():
    # Test with path = "/usr/bin/passwd", mode = 0
    [rc, con] = matchpathcon("/usr/bin/passwd", 0)
    assert rc == -1
    assert con == 'system_u:object_r:bin_t'

    # Test with path = "/usr", mode = 0
    [rc, con] = matchpathcon("/usr", 0)
    assert rc == 0
    assert con == 'system_u:object_r:usr_t:s0'

    # Test with path = "/home/me/test_file.txt", mode = 0
    [rc, con] = matchpathcon("/home/me/test_file.txt", 0)
    assert rc == 0
    assert con == 'unconfined_u:object_r:user_home_t:s0'



# Generated at 2022-06-13 00:03:57.793983
# Unit test for function matchpathcon
def test_matchpathcon():
    _selinux_lib.matchpathcon.restype = c_int
    con = c_char_p()
    if _selinux_lib.matchpathcon(b'/', 0, byref(con)) == 0:
        assert con.value is not None

# Generated at 2022-06-13 00:03:59.843975
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw('/tmp') == [0, 'system_u:object_r:tmp_t']


# Generated at 2022-06-13 00:04:09.024299
# Unit test for function matchpathcon
def test_matchpathcon():
    import os

    path = '/etc/passwd'
    mode = os.R_OK

    try:
        result = 'system_u:object_r:passwd_file_t:s0'
        get_result = matchpathcon(path, mode)

        if get_result[0] < 0:
            raise OSError(get_result[0], os.strerror(get_result[0]))

        if get_result[1] != result:
            raise AssertionError('Failed to get result')

    except OSError as e:
        raise e
    except AssertionError as e:
        raise e



# Generated at 2022-06-13 00:04:13.822658
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    def _lgetfilecon_raw_check(path, label):
        rc, con = lgetfilecon_raw(path)
        assert rc == 0 and con == label, \
            'unexpected result, rc={0}, label={1}'.format(rc, label)

    _lgetfilecon_raw_check('.', 'system_u:object_r:root_t:s0')
    _lgetfilecon_raw_check('/dev/null', 'system_u:object_r:null_device_t:s0')



# Generated at 2022-06-13 00:04:18.767795
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    try:
        _selinux_lib.lgetfilecon_raw.argtypes = [c_char_p, POINTER(c_char_p)]
    except Exception as e:
        raise ImportError('failed to load lgetfilecon_raw - {0}'.format(e))

# Generated at 2022-06-13 00:04:21.638244
# Unit test for function matchpathcon
def test_matchpathcon():
    from tempfile import mkdtemp
    from shutil import rmtree

    tmpdir = mkdtemp()
    assert(matchpathcon(tmpdir, 0))
    rmtree(tmpdir)

# Generated at 2022-06-13 00:04:24.054460
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    result = lgetfilecon_raw(b'')
    assert result[0] == -1
    assert result[1] is None


# Generated at 2022-06-13 00:04:28.562069
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    from os import getcwd

    path = getcwd()
    rc, con = lgetfilecon_raw(path)
    if rc < 0:
        raise OSError(rc, con)
    else:
        return con

# Generated at 2022-06-13 00:04:38.965197
# Unit test for function matchpathcon
def test_matchpathcon():
    import tempfile
    test_file = tempfile.NamedTemporaryFile(delete=False)
    test_file_path = test_file.name
    test_file.close()

    result = matchpathcon(test_file_path, 0)
    assert result[0] == 0
    assert result[1] == 'system_u:object_r:unlabeled_t:s0'


# Generated at 2022-06-13 00:04:44.680417
# Unit test for function matchpathcon
def test_matchpathcon():
    # Check some known values
    assert matchpathcon('/tmp', 0)[1] == 'tmp_t'
    assert matchpathcon('/tmp/test.txt', 0)[1] == 'tmp_t'
    assert matchpathcon('/tmp/test.txt', os.R_OK)[1] == 'tmp_t'
    assert matchpathcon('/tmp/test.txt', os.W_OK)[1] == 'tmp_t'
    assert matchpathcon('/tmp/test.txt', os.R_OK | os.W_OK)[1] == 'tmp_t'

# Generated at 2022-06-13 00:04:47.085873
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = '/path/to/somewhere'
    [rc, value] = lgetfilecon_raw(path)
    assert rc == 0
    assert value == 'system_u:object_r:cyberark_ssh_home_t:s0'

# Generated at 2022-06-13 00:04:56.084997
# Unit test for function matchpathcon
def test_matchpathcon():

    rc, con = matchpathcon(b'/tmp', 0)
    print(rc, con)
    assert rc == 0 and con == 'system_u:object_r:tmp_t'

    rc, con = matchpathcon(b'/bar/baz', 0)
    assert rc == -1

    rc, con = matchpathcon(b'/bin/foo', 0)
    print(rc, con)
    assert rc == 0 and con == 'unconfined_u:object_r:user_tmp_t'


# Unit tests for function lgetfilecon_raw

# Generated at 2022-06-13 00:04:58.942687
# Unit test for function matchpathcon
def test_matchpathcon():
    (rc, con) = matchpathcon('/etc/libuser.conf', 0)
    assert (0, u'system_u:object_r:lib_t') == (rc, con)


# Generated at 2022-06-13 00:05:01.831431
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    result = lgetfilecon_raw(b"/bin/ls")
    assert result[0] >= 0
    assert 'system_u:object_r:bin_t:' in result[1]



# Generated at 2022-06-13 00:05:10.524571
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    lgetfilecon_raw_result = lgetfilecon_raw('/etc/fstab')
    print('/etc/fstab: ', lgetfilecon_raw_result[1])
    lgetfilecon_raw_result = lgetfilecon_raw('/etc/services')
    print('/etc/services: ', lgetfilecon_raw_result[1])
    lgetfilecon_raw_result = lgetfilecon_raw('/bin/ls')
    print('/bin/ls: ', lgetfilecon_raw_result[1])
    lgetfilecon_raw_result = lgetfilecon_raw('/usr/bin/python')
    print('/usr/bin/python: ', lgetfilecon_raw_result[1])

# Generated at 2022-06-13 00:05:12.844718
# Unit test for function matchpathcon
def test_matchpathcon():
    assert matchpathcon(b'/etc/ssh/sshd_config', 0) == [0, b'system_u:object_r:etc_t:s0']



# Generated at 2022-06-13 00:05:19.407686
# Unit test for function matchpathcon
def test_matchpathcon():
    context = 0
    ret = matchpathcon('/.selinux/contexts/files/file_contexts', context)
    print('code: ', ret[0])
    print('content: ', ret[1])


if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-13 00:05:27.129626
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import subprocess
    import re
    import tempfile
    import os
    import stat

    devnull = open(os.devnull, 'wb')
    file_name = tempfile.mktemp()
    file_con = lgetfilecon_raw(file_name)
    touch = subprocess.Popen(['touch', file_name], stdout=devnull, stderr=devnull)
    touch.wait()
    file_con_after_touch = lgetfilecon_raw(file_name)
    assert file_con == file_con_after_touch
    new_file_con = re.sub(r':[^:]*$', ':_test_file_con', file_con[1])
    lsetfilecon_rc = lsetfilecon(file_name, new_file_con)
    file_

# Generated at 2022-06-13 00:05:34.324791
# Unit test for function matchpathcon
def test_matchpathcon():
    path = '/etc/passwd'
    mode = 0o10040
    assert matchpathcon(path, mode) == [0, 'system_u:object_r:etc_runtime_t:s0']

# Generated at 2022-06-13 00:05:35.191374
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw("/etc/passwd")[0] == 0

# Generated at 2022-06-13 00:05:39.402850
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = "/etc/passwd"
    result = lgetfilecon_raw(path)
    assert result[0] == 0
    assert result[1] == "system_u:object_r:shadow_t:s0"



# Generated at 2022-06-13 00:05:42.628654
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw('/etc/passwd')
    assert rc == 0
    assert con == 'system_u:object_r:shadow_t:s0'


# Generated at 2022-06-13 00:05:45.418102
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = b'/'
    rc, con = lgetfilecon_raw(path)
    assert type(rc) is int
    assert rc == 0
    assert type(con) is str


# Generated at 2022-06-13 00:05:49.451010
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    con = c_char_p()
    rc = _selinux_lib.lgetfilecon_raw(b'/etc/passwd', byref(con))
    print('rc: {}'.format(rc))
    print('con: {}'.format(to_native(con.value)))
    _selinux_lib.freecon(con)



# Generated at 2022-06-13 00:05:55.687109
# Unit test for function matchpathcon
def test_matchpathcon():
    result = matchpathcon(b'/etc/passwd', 0)
    assert result[0] == 0
    assert result[1].strip() == 'system_u:object_r:passwd_file_t:s0'

    result = matchpathcon(b'/etc/', 0)
    assert result[0] == 0
    assert result[1].strip() == 'system_u:object_r:etc_t:s0'

    result = matchpathcon(b'/', 0)
    assert result[0] == 0
    assert result[1].strip() == 'root:object_r:root_t:s0'

    result = matchpathcon(b'/var/', 0)
    assert result[0] == 0
    assert result[1].strip() == 'root:object_r:var_t:s0'



# Generated at 2022-06-13 00:05:58.186537
# Unit test for function matchpathcon
def test_matchpathcon():
    from selinux.selinux import matchpathcon
    rc, con = matchpathcon('/etc/localtime', 0)
    print('Matchpathcon: {0}, {1}'.format(rc, con))

if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-13 00:06:01.461197
# Unit test for function matchpathcon
def test_matchpathcon():
    path = '/tmp/test'
    mode = os.R_OK
    print(matchpathcon(path, mode))


# Generated at 2022-06-13 00:06:04.416906
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon('/var/log', 0)
    print("rc={0}, con={1}".format(rc, con))


if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-13 00:06:17.531460
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    """
    Test for function lgetfilecon_raw
    """
    if os.path.exists('/tmp/test1.file'):
        os.remove('/tmp/test1.file')

    with open('/tmp/test1.file', 'w') as f:
        f.write('foo')

    assert lgetfilecon_raw('/tmp/test1.file') == [0, 'system_u:object_r:tmp_t:s0']

    if os.path.exists('/tmp/test1.file'):
        os.remove('/tmp/test1.file')



# Generated at 2022-06-13 00:06:18.669865
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw("/etc/selinux/config")
    assert rc == 0
    assert con == "system_u:object_r:etc_t:s0"

# Generated at 2022-06-13 00:06:25.438002
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    testpath = "/etc/selinux/config"
    try:
        con = c_char_p()
        rc = _selinux_lib.lgetfilecon_raw(testpath, byref(con))
        if rc < 0:
            raise RuntimeError('unexpected error code {0} from lgetfilecon_raw'.format(rc))
        if not con:
            raise RuntimeError('invalid context returned by lgetfilecon_raw')
    finally:
        _selinux_lib.freecon(con)



# Generated at 2022-06-13 00:06:27.263307
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con_string = lgetfilecon_raw('/etc/group')
    print(rc, con_string)



# Generated at 2022-06-13 00:06:32.319698
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    [rc, con] = lgetfilecon_raw(b'/etc/passwd')
    assert rc == 0, 'Unexpected return code'
    assert con != b'', 'No context found'



# Generated at 2022-06-13 00:06:42.707489
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    sys.stderr.write('Running test %s ' % os.path.basename(__file__))

    con = c_char_p()
    # lgetfilecon_raw returns 0 if path exists
    rc = _selinux_lib.lgetfilecon_raw('/etc/passwd', byref(con))
    assert rc == 0
    assert con.value is not None

    # lgetfilecon_raw returns -1 if path does not exist
    rc = _selinux_lib.lgetfilecon_raw('/foo', byref(con))
    assert rc == -1
    assert con.value is None

    # lgetfilecon_raw returns -1 if path is a symbolic link
    rc = _selinux_lib.lgetfilecon_raw('/etc/passwd', byref(con))

# Generated at 2022-06-13 00:06:49.604737
# Unit test for function matchpathcon
def test_matchpathcon():
    from shutil import copyfile
    from tempfile import mkdtemp, mktemp

    # Create temporary directory
    tmppath = mkdtemp()

    # Create temporary file in temporary directory
    tmpfile = mktemp(dir=tmppath)

    # Copy some file to the temporary file
    copyfile('/etc/selinux/config', tmpfile)

    # Check whether the function to test returns the expected result
    assert matchpathcon(tmpfile, 0)[0] == 1



# Generated at 2022-06-13 00:06:53.220527
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = '/etc/passwd'
    rc, rv = lgetfilecon_raw(path)

    if rc == 0:
        print("selinux context: {}".format(rv))
    else:
        print("lgetfilecon_raw Failed to get selinux context")


# Generated at 2022-06-13 00:06:54.930104
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    expected_result = [0, b'default_t']
    result = lgetfilecon_raw(b'/')
    assert result == expected_result

# Generated at 2022-06-13 00:06:58.018507
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = "/etc/passwd"
    rc, con = lgetfilecon_raw(path)
    assert rc >= 0
    assert con is not None
    assert con == "system_u:object_r:etc_runtime_t:s0"



# Generated at 2022-06-13 00:07:07.138669
# Unit test for function matchpathcon
def test_matchpathcon():
    """
    Make sure that matchpathcon returns a valid list.
    """
    rc, result = matchpathcon('/usr/bin', 0)
    assert rc == 0, "Returned non-zero RC: %s" % rc
    assert result, "Did not return a string"



# Generated at 2022-06-13 00:07:09.958705
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (rc, selinux_context) = lgetfilecon_raw("/etc/selinux/config")
    print("selinux context {}".format(selinux_context))
    assert rc == 0



# Generated at 2022-06-13 00:07:19.944245
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    test_file = '/root/test_file'
    mode = 0o600
    with open(test_file, 'w') as open_file:
        open_file.write("This is a test file")
    os.chmod(test_file, mode)
    # This is a sample context to be used
    context = "system_u:object_r:usr_t:s0"
    rc, con = lgetfilecon_raw(test_file)
    if rc >= 0:
        print("The context of the file is %s" % con)
        print("The errno returned is %s" % rc)
    else:
        print("The context of the file is not printed")
    os.remove(test_file)



# Generated at 2022-06-13 00:07:22.069785
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw('/tmp') == [0, 'system_u:object_r:tmp_t:s0']

# Generated at 2022-06-13 00:07:25.585057
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw(b'/etc')[0] == 0
    assert lgetfilecon_raw(b'/etc')[1] is not None
    assert lgetfilecon_raw(b'/does/not/exist')[0] == 256



# Generated at 2022-06-13 00:07:28.327984
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = "/"
    rc, con = lgetfilecon_raw(path)
    print("Return code: {0}".format(rc))
    print("Con: {0}".format(con))



# Generated at 2022-06-13 00:07:33.009370
# Unit test for function matchpathcon
def test_matchpathcon():
    try:
        con = matchpathcon('/etc/named.conf', os.R_OK)
        if con[0] < 0:
            raise IOError('failed to match context')
    except NotImplementedError:
        raise Exception('unit test requires a full selinux implementation')
    assert con[1] == 'system_u:object_r:named_conf_t:s0'



# Generated at 2022-06-13 00:07:39.246974
# Unit test for function matchpathcon
def test_matchpathcon():
    import tempfile

    # Create a dummy file to test con(text) of
    testfile = tempfile.NamedTemporaryFile()
    testfile.close()

    # Test the file's con
    rc, con = matchpathcon(testfile.name, 0)
    assert rc == 0, "matchpathcon failed to return context"
    assert con.startswith('unconfined_u:object_r:'), "matchpathcon returned unexpected context"

    # Clean up
    os.unlink(testfile.name)

# Generated at 2022-06-13 00:07:45.071078
# Unit test for function matchpathcon
def test_matchpathcon():
    from ansible.module_utils._text import to_bytes
    # FIXME: this unit test is dubious as-is since matchpathcon() calls are deprecated
    #        and will be rewritten on selabel_lookup().
    #
    # val[0] = rc
    # val[1] = con
    # val[2] = msg
    # val[3] = errno

    val = matchpathcon('/var/log/httpd/access.log', 0)
    assert val[0] == 0
    assert val[1] == 'system_u:object_r:httpd_log_t:s0'
    assert val[2] == ''
    assert val[3] == 0

    val = matchpathcon('/home/foo/not_found', 0)
    assert val[0] == -1

# Generated at 2022-06-13 00:07:48.456154
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Positive test case
    path = '/etc/hosts'
    assert lgetfilecon_raw(path)[0] == 0
    # Negative test case
    path = '/tmp/nofile'
    assert lgetfilecon_raw(path)[0] == -1



# Generated at 2022-06-13 00:08:05.970566
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    test_file_name = 'test_getfilecon_raw'
    test_file_path = os.path.join('/tmp', test_file_name)
    # write test string to test file
    with open(test_file_path, 'w') as f:
        test_file_content = 'some test string'
        f.write(test_file_content)

    rc, con = lgetfilecon_raw(test_file_path)
    assert rc == 0, 'lgetfilecon_raw failed with rc %s' % rc
    test_file_label = 'system_u:object_r:tmp_t:s0'

    # assert test file has system_u:object_r:tmp_t:s0

# Generated at 2022-06-13 00:08:07.752431
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Ensure we can call lgetfilecon_raw with no error.
    assert(lgetfilecon_raw('/tmp/')[0] >= 0)

# Generated at 2022-06-13 00:08:17.442677
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (rc, con) = lgetfilecon_raw('/')
    assert rc == 0, 'rc = %d, con = %s' % (rc, con)
    assert con == 'system_u:object_r:root_t:s0', 'rc = %d, con = %s' % (rc, con)
    (rc, con) = lgetfilecon_raw('/bin')
    assert rc == 0, 'rc = %d, con = %s' % (rc, con)
    assert con == 'system_u:object_r:bin_t:s0', 'rc = %d, con = %s' % (rc, con)
    (rc, con) = lgetfilecon_raw('/lib')

# Generated at 2022-06-13 00:08:24.898603
# Unit test for function matchpathcon
def test_matchpathcon():
    import tempfile

    # Per issue #77180, we have to test matchpathcon with the '<<none>>' context. This function
    # makes sure that the '<<none>>' context is compatible for that purpose.
    def is_none_compatible():
        rc, con = selinux_getenforcemode()

        if rc:
            raise IOError('unable to retrieve selinux mode.')
        elif con != 1:
            # Per https://docs.fedoraproject.org/en-US/Fedora/15/html/Security-Enhanced_Linux/sect-Security-Enhanced_Linux-SELinux_Contexts-SELinux_Contexts-SELinux_Enforcing_and_Permissive_Modes.html
            # Any mode except '1' (enforcing mode) can return '<<none>>'.
            return

# Generated at 2022-06-13 00:08:30.225592
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    try:
        rst, context = lgetfilecon_raw(b'/etc/passwd')
        print(rst, context)
        assert rst == 0
        assert context is not None and context != ''
    except ImportError:
        print('unable to load libselinux.so, skipping unit test for lgetfilecon_raw')



# Generated at 2022-06-13 00:08:38.769546
# Unit test for function matchpathcon
def test_matchpathcon():
    import os
    import errno
    import tempfile
    import stat

    def check_matchpathcon(path, mode, expected_rc, expected_value=None):
        ret = matchpathcon(path, mode)
        actual_rc = ret[0]
        actual_value = ret[1]
        msg = 'matchpathcon(%s, %s) failed.' % (path, mode)
        assert actual_rc == expected_rc, msg
        if expected_rc == 0:
            assert expected_value == actual_value, msg

    top_level_path = tempfile.mkdtemp()
    top_level_path = os.path.abspath(top_level_path)
    sub_path = os.path.join(top_level_path, "sub_dir")
    os.mkdir(sub_path)

# Generated at 2022-06-13 00:08:44.365051
# Unit test for function matchpathcon
def test_matchpathcon():
    # path must exist
    rc, con = matchpathcon('/tmp', 0)
    assert rc >= 0
    # should be able to free the context
    _selinux_lib.freecon(con)
    rc, con = matchpathcon('/tmp', 0)
    assert rc >= 0
    assert con is not None
    # should be able to construct a new context and then free it
    con = c_char_p(to_bytes(con))
    _selinux_lib.freecon(con)
    assert con.value is None

    # path must not exist
    rc, con = matchpathcon('/does_not_exist', 0)
    assert rc < 0
    assert con is None



# Generated at 2022-06-13 00:08:46.564969
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = '/usr/bin/id'
    rc, con = lgetfilecon_raw(path)
    if rc < 0:
        raise SystemError('lgetfilecon_raw rc: %s' % rc)
    print('lgetfilecon_raw rc: %s' % rc)
    print('lgetfilecon_raw con: %s' % con)


# Generated at 2022-06-13 00:08:55.306371
# Unit test for function matchpathcon
def test_matchpathcon():
    import pytest
    import shutil
    import tempfile
    import subprocess

    testdir = tempfile.mkdtemp()

    # copy /bin/true to the tempdir, preserving the label
    true_path = os.path.join(testdir, "true")
    shutil.copy("/bin/true", true_path)
    subprocess.check_call("chcon -v --reference=/bin/true '{0}'".format(true_path), shell=True)

    # get the context on the path we copied
    rc, context = matchpathcon(true_path, os.stat(true_path).st_mode)
    assert rc == 0
    assert context == "system_u:object_r:bin_t:s0"

    # change the context on the copied path

# Generated at 2022-06-13 00:08:57.662979
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    if is_selinux_enabled() == 1:
        assert lgetfilecon_raw('/')[0] == 0
    else:
        assert lgetfilecon_raw('/')[0] == -1