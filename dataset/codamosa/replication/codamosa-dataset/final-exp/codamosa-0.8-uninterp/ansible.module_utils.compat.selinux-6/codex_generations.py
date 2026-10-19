

# Generated at 2022-06-12 23:59:10.633222
# Unit test for function matchpathcon
def test_matchpathcon():
    test_path = b"/"
    test_mode = 0o600
    if matchpathcon(test_path, test_mode) == (0, 'system_u:object_r:file_t:s0'):
        print("Module matchpathcon successful")
    else:
        print("Module matchpathcon failed")



# Generated at 2022-06-12 23:59:15.651394
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    mode, con = lgetfilecon_raw('/etc/mtab')
    assert mode == 0
    assert con.startswith('system_u:object_r:fstab_t:s0')


# Generated at 2022-06-12 23:59:20.781759
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    r = lgetfilecon_raw('/etc/selinux/config')
    assert r[0] == 0
    assert r[1] == 'system_u:object_r:etc_runtime_t:s0'
    r = lgetfilecon_raw('/etc/selinux/config1234')
    assert r[0] == -1


# Generated at 2022-06-12 23:59:25.147794
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = b'/etc/passwd'

    # Return value of the wrapper
    rc, con = lgetfilecon_raw(path)
    if rc != 0:
        print('lgetfilecon_raw: ' + str(rc))
        sys.exit(1)
    print('File context of', path, 'is: ', con)



# Generated at 2022-06-12 23:59:27.835252
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon('/usr/sbin', 0)
    assert rc == 0
    assert con == 'system_u:object_r:usr_t'

# Generated at 2022-06-12 23:59:31.800190
# Unit test for function matchpathcon
def test_matchpathcon():
    print(matchpathcon(b"/var/spool/rsyslog", os.R_OK))
    print(matchpathcon(b"/usr/bin/ping", os.R_OK))

if __name__ == "__main__":
    test_matchpathcon()

# Generated at 2022-06-12 23:59:34.928428
# Unit test for function matchpathcon
def test_matchpathcon():
    path = b'/proc/uptime'
    mode = os.R_OK
    # We are not verifying the context, just that we can call matchpathcon
    [rc, con] = matchpathcon(path, mode)
    assert rc == 0

# Generated at 2022-06-12 23:59:46.131742
# Unit test for function matchpathcon
def test_matchpathcon():
    import tempfile
    tmp_filename = tempfile.mktemp(prefix='test_selinux-')
    (rc, con) = matchpathcon('/sys', 0x6)
    assert rc == 0, "Selinux error: {0}".format(con)
    assert 'system_u:object_r:sysfs_t:s0' == con, "Unexpected selinux context: {0}".format(con)
    # Test that the file is created
    with open(tmp_filename, 'w') as f:
        pass
    (rc, con) = lgetfilecon_raw(tmp_filename)
    assert rc == 0, "Selinux error: {0}".format(con)
    with open(tmp_filename, 'w') as f:
        pass
    (rc, con) = matchpathcon

# Generated at 2022-06-12 23:59:51.423638
# Unit test for function matchpathcon
def test_matchpathcon():
    f_type = 0
    path = "/tmp/testfile22"
    try:
        file = open(path, "w")
        file.write("test")
        file.close()
        rc = matchpathcon(path, f_type)
        assert rc[0] == 0
        os.remove(path)
    except OSError:
        pass


if __name__ == "__main__":
    # Unit test for function matchpathcon
    test_matchpathcon()

# Generated at 2022-06-12 23:59:56.413125
# Unit test for function matchpathcon
def test_matchpathcon():
    file = '/tmp'
    mode = os.R_OK
    rc, con = matchpathcon(file, mode)
    print('matchpathcon("{0}", {1}) -> ({2}, "{3}")'.format(file, mode, rc, con))



# Generated at 2022-06-13 00:00:07.179239
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import os
    # This function works for both single-user and multiuser
    # selinux modes
    # Check the file /etc/selinux/config

    # Check for multiuser selinux mode
    # Create a test file in /tmp
    fd = os.open("/tmp/test-file", os.O_CREAT)
    os.close(fd)
    # Get the context of /tmp/test-file
    [rc, context] = lgetfilecon_raw("/tmp/test-file")
    # Cleanup - remove the test file
    os.unlink("/tmp/test-file")

# Generated at 2022-06-13 00:00:11.398994
# Unit test for function matchpathcon
def test_matchpathcon():
    filepath_t = "/tmp/test.txt"
    mode =0
    rc, con = matchpathcon(filepath_t, mode)
    assert rc == 0
    assert isinstance(con, str)


if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-13 00:00:13.110060
# Unit test for function lgetfilecon_raw

# Generated at 2022-06-13 00:00:21.848604
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import tempfile
    import shutil

    try:
        tmpdir = tempfile.mkdtemp()
        tmpfile = os.path.join(tmpdir, 'testfile')

        with open(tmpfile, 'w') as f:
            f.write('This is a test')

        rc, c = lgetfilecon_raw(tmpfile)
        assert rc == 0, "rc = {0}".format(rc)
        assert c.startswith('system_u:object_r:usr_t:'), "con = {0}".format(c)

    finally:
        if os.path.exists(tmpdir):
            shutil.rmtree(tmpdir)

if __name__ == '__main__':
    test_lgetfilecon_raw()

# Generated at 2022-06-13 00:00:25.967610
# Unit test for function matchpathcon
def test_matchpathcon():
    path = b'/etc/passwd'
    mode = os.R_OK
    rc, con = matchpathcon(path, mode)
    assert rc == 0
    assert con == 'system_u:object_r:etc_runtime_t:s0'



# Generated at 2022-06-13 00:00:29.040874
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import tempfile
    with tempfile.NamedTemporaryFile() as f:
        result = lgetfilecon_raw(f.name)
        assert(result[0] == 0)
        assert(len(result[1]) > 0)



# Generated at 2022-06-13 00:00:34.122481
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = "/etc/shadow"
    [rc, con] = lgetfilecon_raw(path)
    assert rc == 0
    assert con == 'system_u:object_r:shadow_t:s0'

# Generated at 2022-06-13 00:00:39.496434
# Unit test for function matchpathcon
def test_matchpathcon():
    # Check for error conditions
    if not matchpathcon("/etc/", 1)[0]:
        if matchpathcon("/etc/", 1)[1]:
            print("FAILED")
        else:
            print("PASSED")
    else:
        print("FAILED")


if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-13 00:00:43.212749
# Unit test for function matchpathcon
def test_matchpathcon():
    '''
    Unit test for matchpathcon
    '''
    # Normal invocation
    rc, con = matchpathcon('/tmp', 0)
    assert rc == 0
    assert con == 'tmp_t'
    rc, con = matchpathcon('/tmp/', 0)
    assert rc == 0
    assert con == 'tmp_t'
    rc, con = matchpathcon('/tmp', 0)
    assert rc == 0
    assert con == 'tmp_t'

# Generated at 2022-06-13 00:00:47.634181
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw(b'/etc/passwd').count(b':') == 4
    assert lgetfilecon_raw(b'/etc/passwd')[1] == b'unconfined_u:object_r:usr_t:s0'

# Generated at 2022-06-13 00:00:53.812683
# Unit test for function matchpathcon
def test_matchpathcon():
    ret = matchpathcon('/etc/resolv.conf', 0)
    assert ret[0] == 0
    assert ret[1] == 'system_u:object_r:net_conf_t:s0'

# Generated at 2022-06-13 00:00:57.783804
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (rc, con) = lgetfilecon_raw("/etc")
    if rc != 0:
        raise AssertionError("lgetfilecon_raw() failed")
    if con == "":
        raise AssertionError("lgetfilecon_raw() returned an empty string")
    return True


# Generated at 2022-06-13 00:01:01.248358
# Unit test for function matchpathcon
def test_matchpathcon():
    path = "/tmp"
    mode = 0o755
    rc, con = matchpathcon(path, mode)
    if rc == 0:
        print("Success: security context found: {0}".format(con))
    else:
        print("Error: selinux policy lookup failed: {0}".format(con))

# Generated at 2022-06-13 00:01:04.130518
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw("/")[1] == "system_u:object_r:root_t:s0"


# Generated at 2022-06-13 00:01:10.296923
# Unit test for function matchpathcon
def test_matchpathcon():
    # matchpathcon takes in a path as string and a mode as int
    # a return value of 0 indicates success
    # a nonzero return value indicates an error
    # a nonzero value in the case of an error indicates the error code
    # a value of -1 indicates that selinux is disabled
    assert matchpathcon('/', 0)[0] == -1
    assert matchpathcon('/', 0)[1] == 'system_u:object_r:var_t:s0'



# Generated at 2022-06-13 00:01:16.904249
# Unit test for function matchpathcon
def test_matchpathcon():
    # This function has been deprecated and replaced by selinux_lgetfilecon.
    # This function only exists for backward compatibility.
    assert matchpathcon('/', -1) == [0, '(unlabeled_t:unlabeled_t:s0)']
    assert matchpathcon('/', 0) == [0, '(unlabeled_t:unlabeled_t:s0)']
    assert matchpathcon('/', 1) == [0, '(unlabeled_t:unlabeled_t:s0)']
    assert matchpathcon('/', 2) == [0, '(unlabeled_t:unlabeled_t:s0)']

# Generated at 2022-06-13 00:01:25.489269
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (rc, con) = lgetfilecon_raw(b"/")
    assert rc == 0
    assert con == 'system_u:object_r:root_t:s0'
    (rc, con) = lgetfilecon_raw(b"/usr/bin/python")
    assert rc == 0
    # FIXME: don't hard code the context
    assert con == 'system_u:object_r:usr_t:s0'
    (rc, con) = lgetfilecon_raw(b"/usr/bin/python3")
    assert rc == 0
    # FIXME: don't hard code the context
    assert con == 'system_u:object_r:usr_t:s0'

# Generated at 2022-06-13 00:01:32.576513
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = '/tmp/test1'
    errno = 0
    try:
        os.remove(path)
    except OSError as ex:
        if ex.errno != errno.ENOENT:
            raise
    fd = os.open(path, os.O_CREAT)
    rc, con = lgetfilecon_raw(path)
    os.close(fd)
    os.remove(path)
    assert (rc == 0 and con == 'system_u:object_r:tmp_t:s0\0')

# Generated at 2022-06-13 00:01:35.002114
# Unit test for function matchpathcon
def test_matchpathcon():
    path = '/var/tmp'
    mode = 0o644
    rc, con = matchpathcon(path, mode)
    assert rc == 0
    assert con.startswith('system_u')



# Generated at 2022-06-13 00:01:38.185187
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    """Test case for lgetfilecon_raw function.
    """
    test_file = '/tmp/ansible_selinux_test_file'
    rc, con = lgetfilecon_raw(test_file)
    os.remove(test_file)
    return rc == -1 and con == ''



# Generated at 2022-06-13 00:01:50.019733
# Unit test for function matchpathcon
def test_matchpathcon():
    """
    This test assumes that the default policy supports the sshd_config file.

    Some policies may not support sshd_config and the test will fail.
    """
    # states = 0, 1, 2 mean permissive, enforcing, disabled
    for state in [0, 1, 2]:
        rc, con = matchpathcon('/etc/ssh/sshd_config', state)
        if rc < 0:
            raise Exception('selinux_lib.matchpathcon({0}, {1}) returned {2} ({3})'.format('/etc/ssh/sshd_config', state, rc, to_native(con)))



# Generated at 2022-06-13 00:01:51.509949
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw('/etc/resolv.conf')[1].startswith('system_u:object_r:net_conf')


# Generated at 2022-06-13 00:02:02.416546
# Unit test for function matchpathcon
def test_matchpathcon():
    from ansible.module_utils import basic
    from ansible.module_utils.common._collections_compat import Mapping

    from ansible.module_utils.selinux import matchpathcon, security_getenforce

    spec = dict(
        path=dict(required=True, type='path'),
        filetype=dict(required=True, type='int'),
        mode=dict(default=security_getenforce(), type='int'),
        _ansible_check_mode=dict(default=False, type='bool'),
    )

    res = basic.AnsibleModule(argument_spec=spec).run()

    if isinstance(res, Mapping):
        res = res['failed']

    sys.exit(res)



# Generated at 2022-06-13 00:02:09.275007
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon("/etc/hostname", 0)
    assert rc == 0, "unittest failed: Matchpathcon rc:" + rc
    assert con == "system_u:object_r:etc_runtime_t:s0", "unittest failed: Matchpathcon could not find context"



# Generated at 2022-06-13 00:02:11.566001
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = './test'
    result = lgetfilecon_raw(path)
    assert result[0] == 0



# Generated at 2022-06-13 00:02:14.720985
# Unit test for function matchpathcon
def test_matchpathcon():
    _path = '/etc/hosts'

# Generated at 2022-06-13 00:02:17.986324
# Unit test for function matchpathcon
def test_matchpathcon():
    try:
        rc, con = matchpathcon('/', 0)
        if rc != 0:
            raise Exception('matchpathcon returned error code')
    except OSError:
        raise Exception('matchpathcon failed')


# Generated at 2022-06-13 00:02:22.932840
# Unit test for function matchpathcon
def test_matchpathcon():
    [rc, con] = matchpathcon('/usr/bin/', 0)
    assert rc == 0
    assert con == 'system_u:object_r:usr_t:s0'


# Generated at 2022-06-13 00:02:32.452203
# Unit test for function matchpathcon
def test_matchpathcon():
    # sanity test to ensure wrapping was correct, this implicitly exercises the wrapper functions
    success, mode = selinux_getenforcemode()
    assert success == 0 and mode == 1
    success, policytype = selinux_getpolicytype()
    assert success == 0 and policytype == b'strict'

    # verify the function works as expected
    path = '/'
    mode = 1
    success, context = matchpathcon(path, mode)
    assert success == 0 and context is not None

    # verify it errors when given a bad path
    path = '/no/such/path'
    mode = 1
    success, context = matchpathcon(path, mode)
    assert success != 0 and context is None



# Generated at 2022-06-13 00:02:38.570037
# Unit test for function matchpathcon
def test_matchpathcon():
    import tempfile
    import os
    # TODO: should we use a different template?
    test_file = tempfile.NamedTemporaryFile(prefix='selinux-test_', dir='/tmp', delete=False)
    con = matchpathcon(test_file.name, 0)[1]
    os.unlink(test_file.name)
    return con


if __name__ == '__main__':
    print(test_matchpathcon())

# Generated at 2022-06-13 00:02:48.684519
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    test_input_path = "./testdata/example.conf"
    test_output_con = "system_u:object_r:test_file_t"
    [rc, con] = lgetfilecon_raw(test_input_path)
    assert rc == 0

# Generated at 2022-06-13 00:02:54.324838
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Check if file exists
    if os.path.isfile("/etc/passwd"):
        rc, stdout = lgetfilecon_raw("/etc/passwd")
        print("stdout: %s" % stdout)
        assert stdout != None
    else:
        assert True



# Generated at 2022-06-13 00:03:04.073940
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Test case 1: Check the return value of lgetfilecon_raw function
    file_name = sys.modules[__name__].__file__
    assert _selinux_lib.lgetfilecon_raw(file_name, byref(c_char_p())) == 0

    # Test case 2: Check if lgetfilecon_raw raises OSError when passed with
    #              file name which does not exist
    # Note: The function raises OSError with errno = ENOENT.
    #       ENOENT = 2 (https://www.kernel.org/doc/html/v4.18/core-api/errno.html)

# Generated at 2022-06-13 00:03:13.361393
# Unit test for function lgetfilecon_raw

# Generated at 2022-06-13 00:03:18.970502
# Unit test for function matchpathcon
def test_matchpathcon():
    # check that when passed a valid path, the matchpathcon function will return the expected results
    assert matchpathcon(b'/sys', 0) == [0, 'system_u:object_r:selinuxfs:s0']

    # check that when passed an invalid path, the matchpathcon function will throw an os error
    try:
        matchpathcon(b'/doesnt_exist', 0)
    except OSError:
        return True
    raise AssertionError('matchpathcon did not throw an OSError when passed an invalid path')



# Generated at 2022-06-13 00:03:21.351476
# Unit test for function matchpathcon
def test_matchpathcon():
    path = b"/sys/fs/selinux/enforce"
    rc, con = matchpathcon(b"/sys/fs/selinux/enforce", 0)
    assert rc == 0

# Generated at 2022-06-13 00:03:32.220392
# Unit test for function matchpathcon
def test_matchpathcon():
    if not is_selinux_enabled():
        raise SystemExit('SELinux not enabled, skipping test')

    path = os.path.expanduser('~/.ansible.cfg')
    mode = os.R_OK
    try:
        con = lgetfilecon_raw(path)[1]
        mcon = matchpathcon(path, mode)[1]
    except OSError as e:
        raise SystemExit('SELinux failed: {0}'.format(to_native(e)))

    print('SELinux con for {0}: {1}'.format(path, con))
    print('SELinux matchpathcon for {0}: {1}'.format(path, mcon))


if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-13 00:03:43.165574
# Unit test for function matchpathcon
def test_matchpathcon():
    """ Tests the matchpathcon function
        Returns a string to be printed that is either
        status message or error message
    """
    try:
        (rc, con) = matchpathcon('/test', 0)
        status = 'matchpathcon function is working properly'
        err_msg = ''
    except ImportError as error:
        status = ''
        err_msg = 'Error: matchpathcon function is not working properly'
    except OSError as error:
        status = ''
        err_msg = 'Error: OSError: {0}'.format(error)
    except NotImplementedError as error:
        status = ''
        err_msg = 'Error: NotImplementedError: {0}'.format(error)
    except:
        status = ''
        err_msg = 'Error: Unexpected error'

# Generated at 2022-06-13 00:03:48.244880
# Unit test for function matchpathcon
def test_matchpathcon():
    from stat import S_ISLNK
    from pyaux.ansible.module_utils.selinux import lstat_raw, matchpathcon

    path = '/etc/machine-id'
    rc, ftype = lstat_raw(path)
    if S_ISLNK(ftype):
        path = os.readlink(path)
    rc, con = matchpathcon(path, 0)
    assert rc == 0
    assert con == 'system_u:object_r:container_file_t:s0'



# Generated at 2022-06-13 00:03:52.481390
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    out = lgetfilecon_raw('/etc/passwd')
    assert out[0] == 0
    assert out[1] == "system_u:object_r:passwd_file_t:s0\n"

if __name__ == '__main__':
    test_lgetfilecon_raw()

# Generated at 2022-06-13 00:04:07.589088
# Unit test for function matchpathcon
def test_matchpathcon():
    path = os.path.abspath(__file__)

    def _ret(retcode, stdout=None, stderr=None):
        return dict(rc=retcode, path=path, stdout=stdout, stderr=stderr)

    if not os.path.isfile(path):
        raise AssertionError('{0} is not a file'.format(path))

    def _call(mode):
        rc, con = matchpathcon(path, mode)
        sys.stderr.write('matchpathcon: rc={0}, path={1}, mode={2}, con={3}\n'.format(rc, path, mode, con))
        return _ret(rc, stdout=con)

    # http://man7.org/linux/man-pages/man3/matchpathcon.3.html

# Generated at 2022-06-13 00:04:09.648435
# Unit test for function matchpathcon
def test_matchpathcon():
    matchpathcon(u'/etc/selinux/targeted/contexts/files/file_contexts', 0)



# Generated at 2022-06-13 00:04:14.725396
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    """
    Return context of a file
    """
    expected = [0, 'system_u:object_r:unlabeled_t:s0']
    rc, con = lgetfilecon_raw(b"SELinux-python-test")
    assert [rc,con] == expected


# Generated at 2022-06-13 00:04:18.062602
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw('/etc/')
    assert rc == 0
    # If a type computes to '<<none>>', it means that a path is not labeled
    assert '<<none>>' not in con

# Generated at 2022-06-13 00:04:20.533860
# Unit test for function matchpathcon
def test_matchpathcon():
    err, rc = matchpathcon("/home/foo/bar", 1)
    assert rc == 'system_u:object_r:user_home_dir_t:s0'
    assert err == 0

# Generated at 2022-06-13 00:04:31.179143
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    from ansible_collections.misc.selinux_test.tests.unit.compat import unittest

    class Lgetfilecon_rawTestCase(unittest.TestCase):
        def test_lgetfilecon_raw_does_not_raise(self):
            """Test that lgetfilecon_raw does not raise an exception when valid path is given.
            The path can be a directory or a file.
            """
            valid_path = os.path.realpath(os.path.curdir)
            try:
                rc, con = lgetfilecon_raw(valid_path)
            except OSError as e:
                self.fail("Raised OSError: {} {}".format(e.errno, e.strerror))
            self.assertEqual(rc, 0)

# Generated at 2022-06-13 00:04:38.448767
# Unit test for function matchpathcon
def test_matchpathcon():
    if is_selinux_enabled():
        rc, ctx = matchpathcon('/etc/passwd', os.R_OK)
        assert rc == 0, 'matchpathcon failed: {0}'.format(rc)
        assert type(ctx) == str, 'context not a str type: {0}'.format(type(ctx))
        assert len(ctx) > 0, 'context is empty'
    else:
        assert matchpathcon('/etc/passwd', os.R_OK) == [-1, '']

# Generated at 2022-06-13 00:04:43.212001
# Unit test for function matchpathcon
def test_matchpathcon():
    testdir = '/tmp/'
    tc = matchpathcon(testdir, 0)
    if tc[1] == 'system_u:object_r:tmp_t:s0':
        print("matchpathcon function is working")
    else:
        print("matchpathcon function has FAILED !!!")

    toc = lgetfilecon_raw(testdir)
    print("lgetfilecon_raw = ", toc)


# Generated at 2022-06-13 00:04:53.146276
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    from contextlib import contextmanager
    from io import StringIO

    @contextmanager
    def capture_output():
        new_out = StringIO()
        old_out = sys.stdout
        try:
            sys.stdout = new_out
            yield sys.stdout
        finally:
            sys.stdout = old_out

    # Set up a test file
    import tempfile
    testfile = tempfile.NamedTemporaryFile()

    with capture_output() as out:
        rc, con = lgetfilecon_raw(testfile.name)
    assert rc == 0, "lgetfilecon_raw returned non-zero exit code"
    # Con should be of the form "context1:context2:context3:context4"
    pairs = con.split(":")

# Generated at 2022-06-13 00:05:01.404197
# Unit test for function matchpathcon
def test_matchpathcon():
    ret = matchpathcon('/var/tmp', 0)
    if ret[0] != 0 or ret[1] != 'system_u:object_r:tmp_t:s0':
        sys.exit(1)
    ret = matchpathcon('/var/log/audit', 0)
    if ret[0] != 0 or ret[1] != 'system_u:system_r:auditd_t:s0':
        sys.exit(1)
    sys.exit(0)


if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-13 00:05:08.286415
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    ret, filecon = lgetfilecon_raw('/etc/passwd')
    assert ret == 0
    assert filecon == 'unconfined_u:object_r:user_home_t:s0'

# Generated at 2022-06-13 00:05:13.060276
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = b'/tmp/test_filecon'

    test_file = open(path, 'w')
    test_file.close()

    try:
        rc, con = lgetfilecon_raw(path)
        assert rc == 0
        rc, con_getenforcemode = selinux_getenforcemode()
        if rc == 0 and con_getenforcemode > 0:
            assert con != 'unlabeled'
    finally:
        os.remove(path)

    try:
        rc, con = lgetfilecon_raw(b'/tmp/unexistentfile')
        assert rc != 0
        assert con == ''
    except Exception:
        pass



# Generated at 2022-06-13 00:05:24.510965
# Unit test for function matchpathcon
def test_matchpathcon():
    # Test 1
    path = '/var/empty'
    mode = 0o777
    rc, con_datum = matchpathcon(path, mode)  # noqa: F841
    assert rc == 0, "matchpathcon failed with '{0}'".format(con_datum)
    # Test 2
    path = '/etc/shadow'
    mode = 0o777
    rc, con_datum = matchpathcon(path, mode)  # noqa: F841
    assert rc == 0, "matchpathcon failed with '{0}'".format(con_datum)
    # Test 3
    path = '/etc/shadow'
    mode = 0o660
    rc, con_datum = matchpathcon(path, mode)  # noqa: F841

# Generated at 2022-06-13 00:05:32.612962
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import os

    if os.environ.get('TRAVIS_OS_NAME', '') == 'osx':
        return

    con = ''
    ret = lgetfilecon_raw('/bin/ls')
    print(ret)
    if ret[0] == 0:
        con = ret[1]
    print(con)

# Generated at 2022-06-13 00:05:38.062256
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    test_path = '/tmp'
    rc, con = lgetfilecon_raw(test_path)
    if rc < 0:
        errno = get_errno()
        print('error: errno: {0}, strerror: {1}'.format(errno, os.strerror(errno)))
    else:
        print('path: {0}, context: {1}'.format(test_path, con))


# Generated at 2022-06-13 00:05:41.112842
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    [rc, con] = lgetfilecon_raw('/etc/')
    assert rc == 0
    assert con == 'system_u:object_r:etc_t:s0'


# Generated at 2022-06-13 00:05:46.967171
# Unit test for function matchpathcon
def test_matchpathcon():
    import os
    path = os.path.expanduser('~')
    rc, con = matchpathcon(path, 0)
    assert rc == 0
    assert con == 'unconfined_u:object_r:user_home_t:s0'

    rc, con = lgetfilecon_raw(path)
    assert rc == 0
    assert con == 'unconfined_u:object_r:user_home_t:s0'



# Generated at 2022-06-13 00:05:47.808400
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    print(lgetfilecon_raw('testfile'))

# Generated at 2022-06-13 00:05:50.984536
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw('/etc/passwd') == [0, 'system_u:object_r:etc_t:s0']
    assert lgetfilecon_raw('/foo/bar/baz') == [0, 'system_u:object_r:user_home_dir_t:s0']



# Generated at 2022-06-13 00:05:54.905302
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # If SELinux is not enabled, it will return a unexpected result.
    assert lgetfilecon_raw('/')[0] != -1

    # If file does not exist, it should return -1 with errno as ENOENT
    assert lgetfilecon_raw('/path/to/non/existing/file') == [-1, 2]

# Generated at 2022-06-13 00:06:08.691517
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict(path=dict(type='str', required=True))
    )

    if not module.check_mode:
        try:
            path = module.params['path']
            rc, con = lgetfilecon_raw(path)

            if rc == 0:
                module.exit_json(changed=False, msg='File has context {0}'.format(con))
            else:
                module.fail_json(msg='Unable to read context of file {0}'.format(path))
        except OSError as e:
            module.fail_json(msg='Error while reading context {0}'.format(e))



# Generated at 2022-06-13 00:06:14.703924
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    from tempfile import mkstemp

    fd, path = mkstemp()
    with os.fdopen(fd, 'wb') as fobj:
        fobj.write(b'foo')

    # check that a file without a security context returns an error
    rc, _val = lgetfilecon_raw(path)
    assert rc == -1

    os.unlink(path)

    rc, _val = lgetfilecon_raw(path)
    assert rc == -1

# Generated at 2022-06-13 00:06:17.375534
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw(b'/tmp')
    assert rc == 0
    assert to_native(con) == 'system_u:object_r:tmp_t:s0'

# Generated at 2022-06-13 00:06:19.892369
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    print(lgetfilecon_raw('/foo'))
    print(lgetfilecon_raw('/bin/ls'))
    print(lgetfilecon_raw('/dev/null'))


# Generated at 2022-06-13 00:06:22.847456
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    file_name = '/etc/selinux/config'
    out, rc = lgetfilecon_raw(file_name)
    assert rc == 0
    assert isinstance(out, str)
    assert out == "system_u:object_r:etc_t:s0"



# Generated at 2022-06-13 00:06:24.244257
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw(b'/')[1].startswith(b'unconfined_u:object_r:rootfs')

# Generated at 2022-06-13 00:06:30.621094
# Unit test for function matchpathcon
def test_matchpathcon():
    test_path = '/etc/passwd'
    fd = os.open(test_path, 0)
    enable_selinux, mode = selinux_getenforcemode()
    if enable_selinux == 1:
        rc, con = matchpathcon(test_path, 0)
        print(rc, con)
        rc = lsetfilecon(test_path, con)
        print(rc)

# Generated at 2022-06-13 00:06:35.184492
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    con = c_char_p()
    try:
        rc = _selinux_lib.lgetfilecon_raw(b"/", byref(con))
        assert rc == 0
    finally:
        _selinux_lib.freecon(con)

# Generated at 2022-06-13 00:06:42.833262
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw(None) == [-22, None]
    assert lgetfilecon_raw('/')[0] >= 0
    assert lgetfilecon_raw('/')[1].startswith('system_u:object_r:root_t:s0')
    assert lgetfilecon_raw('/etc/passwd')[0] >= 0
    assert lgetfilecon_raw('/etc/passwd')[1].startswith('system_u:object_r:etc_t:s0')
    assert lgetfilecon_raw('/etc/passwd2') == [-2, None]



# Generated at 2022-06-13 00:06:47.961642
# Unit test for function matchpathcon
def test_matchpathcon():
    (rc, con) = matchpathcon('/tmp', 0)
    assert rc == 0
    assert con == 'system_u:object_r:tmp_t:s0'
    (rc, con) = matchpathcon('/bad/path', 0)
    assert rc == 1
    assert con == '<<none>>:<<none>>:<<none>>:s0'

# Generated at 2022-06-13 00:06:55.882337
# Unit test for function matchpathcon
def test_matchpathcon():
    mode = 0
    rc, con = matchpathcon('/var/tmp/test_file_for_conf', mode)
    assert rc == 0 and con == 'system_u:object_r:user_tmp_t:s0'

# Generated at 2022-06-13 00:07:02.949352
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    [rc, con] = lgetfilecon_raw("/tmp/test1")
    assert(rc == 0)
    assert(con == "system_u:object_r:tmp_t:s0")

    [rc, con] = lgetfilecon_raw("/etc/passwd")
    assert(rc == 0)
    assert(con == "system_u:object_r:etc_runtime_t:s0")

    try:
        [rc, con] = lgetfilecon_raw("/not/existing/file")
        assert(rc == -1)
    except OSError:
        pass

    try:
        [rc, con] = lgetfilecon_raw(None)
        assert(rc == -1)
    except OSError:
        pass



# Generated at 2022-06-13 00:07:06.384095
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import selinux
    if selinux.is_selinux_enabled():
        assert lgetfilecon_raw('/bin/bash')[0] == 0
        assert lgetfilecon_raw('/does/not/exists')[0] != 0

# Generated at 2022-06-13 00:07:09.915937
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = '/tmp'
    rc, con = lgetfilecon_raw(path)
    print("{0}:{1}:{2}".format(con, rc, type(con)))

if __name__ == '__main__':
    test_lgetfilecon_raw()

# Generated at 2022-06-13 00:07:12.820156
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = '/etc/passwd'
    result, con = lgetfilecon_raw(path)
    assert result == 0
    assert con == 'system_u:object_r:etc_runtime_t:s0'



# Generated at 2022-06-13 00:07:17.753281
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert os.path.exists('/usr/bin/python3')
    [rc, con] = lgetfilecon_raw('/usr/bin/python3')
    assert rc == 1
    assert con == "system_u:object_r:usr_t:s0"

# Generated at 2022-06-13 00:07:19.190140
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert isinstance(lgetfilecon_raw('/'), list)


# Generated at 2022-06-13 00:07:28.667934
# Unit test for function matchpathcon
def test_matchpathcon():
    import os
    import stat

    test_root = 'selinux_test_root'
    test_file = 'selinux_test_file'
    test_path = os.path.join(test_root, test_file)

    if not os.path.isdir(test_root):
        os.mkdir(test_root, stat.S_IRWXU)
    with open(test_path, 'w') as f:
        f.write('test\n')

    rc, con = matchpathcon(test_path, os.R_OK)
    assert(rc == 0)

    # The context of the test file will be something like `unconfined_u:object_r:default_t:s0`.
    # The following line will check that `test` is in the context

# Generated at 2022-06-13 00:07:31.668213
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = '/home/user1/file1.txt'
    assert lgetfilecon_raw(path)[1] == 'system_u:object_r:user_home_t:s0'

# Generated at 2022-06-13 00:07:35.111539
# Unit test for function matchpathcon
def test_matchpathcon():
   path = "/tmp"
   mode = 0
   rc, con = matchpathcon(path, mode)
   assert(rc == 0)
   assert(con == "system_u:object_r:tmp_t:s0")



# Generated at 2022-06-13 00:07:44.302466
# Unit test for function matchpathcon
def test_matchpathcon():
    result = matchpathcon('/etc/passwd', 0)
    print(result)


# Generated at 2022-06-13 00:07:46.733636
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw(path="/var/log/audit")
    assert rc == 0
    assert con is not None



# Generated at 2022-06-13 00:07:50.097594
# Unit test for function matchpathcon
def test_matchpathcon():
    # This function is deprecated. See selinux_getenforcemode
    test_mode = 0
    test_path = "/tmp/secretfile"
    rc, con = matchpathcon(test_path, test_mode)
    assert rc != -1
    assert con is not None


# Generated at 2022-06-13 00:07:52.799711
# Unit test for function matchpathcon
def test_matchpathcon():
    result = matchpathcon('/boot/grub2/grub.cfg', 0)
    assert (result[0] == 0)
    assert (result[1] == 'system_u:object_r:boot_t:s0')

# Generated at 2022-06-13 00:07:54.689024
# Unit test for function matchpathcon
def test_matchpathcon():
    assert [0, 'system_u:object_r:usr_t:s0'] == matchpathcon('/usr', os.R_OK)

# Generated at 2022-06-13 00:07:57.487439
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon('/sys/fs/selinux/booleans/deny_dac_read_search', 0)
    assert(rc == 0)
    assert(con == 'system_u:object_r:devpts_t:s0')

# Generated at 2022-06-13 00:08:02.673136
# Unit test for function matchpathcon
def test_matchpathcon():
    if not is_selinux_enabled():
        return

    # get a path with a defined context
    rc, path = _get_path_with_context()
    if rc < 0 or not path:
        return

    # check matchpathcon
    rc, context = matchpathcon(path, 0)
    assert rc >= 0, "Return code is negative"
    assert context is not None, "Context string is None"



# Generated at 2022-06-13 00:08:05.175549
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw('/etc/passwd') == [0, 'system_u:object_r:etc_t:s0']


# Generated at 2022-06-13 00:08:07.281209
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    r = lgetfilecon_raw('./')
    assert r[0] == 0 and r[1] is not None, 'failed to get context of current directory'



# Generated at 2022-06-13 00:08:10.300945
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw('/etc/passwd')
    assert type(con) == str



# Generated at 2022-06-13 00:08:19.276103
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = os.path.expanduser("~")
    mode, con = lgetfilecon_raw(path)
    assert mode == 0
    assert con is not None

    path = "/etc/hosts"
    mode, con = lgetfilecon_raw(path)
    assert mode == 0
    assert con is not None



# Generated at 2022-06-13 00:08:21.739331
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = os.path.dirname(os.path.realpath(__file__))
    rc, con = lgetfilecon_raw(path)
    assert rc == 0
    assert con == 'system_u:object_r:texinfo_t:s0'

# Generated at 2022-06-13 00:08:30.782171
# Unit test for function matchpathcon
def test_matchpathcon():
    # test hardcoded strings
    testpaths = [
        '/',
        '/a',
        '/a/b',
        '/a/b/c',
        '/a/b/c/d',
        '/tmp',
        '/tmp/a',
        '/tmp/a/b',
        '/tmp/a/b/c',
        '/tmp/a/b/c/d',
    ]

    for path in testpaths:
        con = matchpathcon(path, 0)
        assert con[0] == 0, 'unexpected return code {0} for {1}'.format(con[0], path)
        assert con[1] is not None, 'unexpected return value {0} for {1}'.format(con[1], path)



# Generated at 2022-06-13 00:08:35.378626
# Unit test for function matchpathcon
def test_matchpathcon():
    import tempfile
    fd, path = tempfile.mkstemp()
    os.close(fd)
    rc, con = matchpathcon(path, os.R_OK)
    if rc < 0:
        errno = get_errno()
        raise OSError(errno, os.strerror(errno))
    print(con)
    os.remove(path)

# Generated at 2022-06-13 00:08:41.601563
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    from os import path
    from tempfile import mkstemp

    (fd, filepath) = mkstemp()
    os.close(fd)
    assert path.exists(filepath) is True, 'error creating temp file for test'

    (rc, current_scontext) = lgetfilecon_raw(filepath)
    assert rc == 0, 'error getting security context'

    assert current_scontext is not None, 'security context is None'
    assert current_scontext != '', 'security context is empty'

    os.remove(filepath)
    assert path.exists(filepath) is False, 'error deleting temp file for test'

# Generated at 2022-06-13 00:08:43.996880
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    test_file_path = '/etc/passwd'
    result = lgetfilecon_raw(test_file_path)
    assert result[1] == 'system_u:object_r:passwd_file_t:s0-s0:c0.c1023', result



# Generated at 2022-06-13 00:08:50.677989
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    d = {}
    d['stdout'], d['stdout_lines'] = lgetfilecon_raw('/etc/pam.d/sshd')
    assert d['stdout'] == 0
    assert d['stdout_lines'] == 'system_u:object_r:etc_runtime_t:s0'

    # Test forcing to return failure code and error message
    d['stdout'], d['stdout_lines'] = lgetfilecon_raw('/foo/bar')
    assert d['stdout'] == -1
    assert 'No such file or directory' in d['stdout_lines']
    assert 'No such file or directory' in str(d['stdout_lines'])



# Generated at 2022-06-13 00:08:58.224268
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import socket
    try:
        _selinux_lib.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
    except:
        raise ImportError('could not load libselinux.so')

    # lgetfilecon_raw returns a list with the first value as the return code and the second as the context
    # assert that the list length is equal to 2
    assert len(lgetfilecon_raw('/')) == 2
    # assert that the context of the root directory is system_u:object_r:root_t:s0
    assert lgetfilecon_raw('/') == [0, 'system_u:object_r:root_t:s0']

# Generated at 2022-06-13 00:09:05.253230
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Do not run if we are not on a selinux enabled system or selinux
    # is not running in enforcing mode
    if selinux_getenforcemode()[1] == "Disabled" or not is_selinux_enabled():
        return (0, "")

    # Check if the current context is "system_u:system_r:unconfined_t:s0:c0,c0,c0"
    ret, con = lgetfilecon_raw("/")
    if ret == 0 and con == "system_u:object_r:unconfined_t:s0:c0,c0,c0":
        return (ret, con)
    else:
        return (ret, "")