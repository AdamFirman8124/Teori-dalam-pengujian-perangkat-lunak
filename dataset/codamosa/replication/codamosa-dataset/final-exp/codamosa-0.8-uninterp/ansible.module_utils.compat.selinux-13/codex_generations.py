

# Generated at 2022-06-12 23:59:20.319361
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = b"/bin/sh"
    try:
        assert(lgetfilecon_raw(path)[1] == "unconfined_u:object_r:shell_exec_t:s0")
    except OSError as e:
        print(e)
        assert(False)
    path = b"/tmp/"
    try:
        assert(lgetfilecon_raw(path)[1] == "system_u:object_r:tmp_t:s0")
    except OSError as e:
        print(e)
        assert(False)
    path = b"/home/ansible"

# Generated at 2022-06-12 23:59:25.826897
# Unit test for function matchpathcon
def test_matchpathcon():
    [rc, con] = matchpathcon('/foo/bar/baz', 0)
    if rc < 0:
        print('matchpathcon failed:', rc, con)
        sys.exit(1)
    print('matchpathcon succeeded:', rc, con)
    sys.exit(0)


if __name__ == '__main__':
    test_matchpathcon()
    test_selinux_getenforcemode()

# Generated at 2022-06-12 23:59:33.752139
# Unit test for function matchpathcon
def test_matchpathcon():
    path = to_bytes('/var/log/test_file')

    try:
        os.mkdir('/var/log/')
    except OSError:
        pass

    try:
        open(path, 'w').close()
    except OSError:
        pass

    rc, con = matchpathcon(path, 0)
    rc_expected = 0
    assert rc == rc_expected, 'Got unexpected rc: %d' % rc
    assert con == 'system_u:object_r:var_log_t:s0', con

    os.unlink(path)

# Generated at 2022-06-12 23:59:40.261105
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    test_path = '/tmp/test_file'
    test_con = 'system_u:object_r:user_tmp_t:s0'
    test_con2 = 'system_u:object_r:default_t:s0'

    lsetfilecon(test_path, test_con)
    [rc, con] = lgetfilecon_raw(test_path)
    assert rc == 0, 'unexpected error code: {0}'.format(rc)
    assert con == test_con, 'unexpected context value: {0}'.format(con)

    [rc, con] = lsetfilecon(test_path, test_con2)
    assert rc == 0, 'unexpected error code: {0}'.format(rc)

# Generated at 2022-06-12 23:59:43.199153
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw('/etc/passwd') == [0, 'system_u:object_r:etc_runtime_t:s0']

# Generated at 2022-06-12 23:59:44.560733
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    val = lgetfilecon_raw("/")
    assert val[0] == 0

# Generated at 2022-06-12 23:59:53.395785
# Unit test for function matchpathcon
def test_matchpathcon():
    import os, errno
    if not os.path.exists('/dir1/dir2/file1'):
        print('/dir1/dir2/file1 should exist')
        return False
    if os.path.exists('/dir1/dir2/file2'):
        print('/dir1/dir2/file2 should not exist')
        return False

    rc, con = matchpathcon('/dir1/dir2/file1', 0)
    if rc != 0:
        print('matchpathcon returned: ' + str(rc))
        return False
    if con != 'system_u:object_r:bin_t:s0':
        print('matchpathcon returned incorrect context: ' + con)
        return False

# Generated at 2022-06-13 00:00:00.681987
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    from ansible.module_utils.selinux import lgetfilecon_raw
    from os.path import dirname, realpath
    path = dirname(realpath(__file__))
    [rc, con] = lgetfilecon_raw(path)
    if rc < 0:
        raise OSError(os.strerror(abs(rc)))
    print("path: {0} context: {1}".format(path, con))


if __name__ == "__main__":
    test_lgetfilecon_raw()

# Generated at 2022-06-13 00:00:08.250809
# Unit test for function matchpathcon
def test_matchpathcon():
    # Test path is found
    (rc, con) = matchpathcon(b'/var/tmp', 0)
    assert rc == 0, "Return code was not as expected."
    assert con == "system_u:object_r:tmp_t:s0", "Context was not as expected."

    # Test path is not found
    (rc, con) = matchpathcon(b'/var/tmp/noxpath', 0)
    assert rc == 2, "Return code was not as expected."
    assert con is None, "Context was not as expected."

    # Test path is not valid
    (rc, con) = matchpathcon(b'/not/a/valid/path', 0)
    assert rc == -1, "Return code was not as expected."
    assert con is None, "Context was not as expected."


# Generated at 2022-06-13 00:00:10.534124
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw('/tmp')
    assert rc >= 0, "Failed to retrieve SELinux label for /tmp"

# Generated at 2022-06-13 00:00:15.611799
# Unit test for function matchpathcon
def test_matchpathcon():
    status, context = matchpathcon('/usr/bin/', os.F_OK)
    assert status == 0
    assert context == 'system_u:object_r:usr_t:s0'



# Generated at 2022-06-13 00:00:17.796356
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    lgetfilecon_raw("/tmp")


if __name__ == '__main__':
    test_lgetfilecon_raw()

# Generated at 2022-06-13 00:00:25.294675
# Unit test for function matchpathcon
def test_matchpathcon():
    try:
        import selinux
    except ImportError:
        raise Exception("This test requires the python selinux module")

    desired_mode = 0
    desired_context = b"system_u\0object_r\0object_t\0"

    # Note: this will only work if the module is installed on the system
    rc, con = selinux.matchpathcon(b"/usr/lib/systemd/system", desired_mode)
    assert rc == 0, "Expected a 0 return code for matchpathcon, got {}".format(rc)
    assert con == desired_context, "Expected a {} context, got {}".format(desired_context, con)

# Generated at 2022-06-13 00:00:36.169809
# Unit test for function matchpathcon
def test_matchpathcon():
    try:
        print("matchpathcon(\"/bin/bash\", 0) = {0}".format(matchpathcon("/bin/bash", 0)))
    except OSError as e:
        print(e)
    try:
        print("matchpathcon(\"/dev/null\", 0) = {0}".format(matchpathcon("/dev/null", 0)))
    except OSError as e:
        print(e)
    try:
        print("matchpathcon(\"/\", 0) = {0}".format(matchpathcon("/", 0)))
    except OSError as e:
        print(e)

# Generated at 2022-06-13 00:00:41.468912
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import selinux
    test_file = os.path.join(os.getcwd(), "test.txt")
    if not os.path.isfile(test_file):
        open(test_file, 'w').close()
    rc, context = selinux.lgetfilecon_raw(test_file)
    assert rc == 0
    assert context == "system_u:object_r:user_home_t:s0"

# Generated at 2022-06-13 00:00:44.300856
# Unit test for function matchpathcon
def test_matchpathcon():
    print(matchpathcon('/etc/shadow', 0))



# Generated at 2022-06-13 00:00:51.059821
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    '''
    Test for lgetfilecon_raw
    :return:
    '''
    try:
        # FIXME: we should have some user_home set up that is temp-ish
        fname = '/tmp/ansible-test'
        res = lgetfilecon_raw(fname)
        assert res[0] == -1
        assert res[1] == ''  # no context, just error code
    except ImportError:
        # can't test
        pass

# Generated at 2022-06-13 00:00:56.119905
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = "./ansible/test/runner_data/module_utils/test.data"
    con = c_char_p()
    rc = _selinux_lib.lgetfilecon_raw(path, byref(con))
    if rc < 0:
        raise OSError('lgetfilecon_raw failed')
    return rc

# Generated at 2022-06-13 00:01:00.122418
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = b'/etc/passwd'
    rc, con = lgetfilecon_raw(path)

    assert rc == 0, 'failed to call lgetfilecon_raw()'
    assert con is not None, 'lgetfilecon_raw() returned null context'
    assert con != b'', 'lgetfilecon_raw() returned empty context'

# Generated at 2022-06-13 00:01:10.764901
# Unit test for function matchpathcon
def test_matchpathcon():
    import os
    from random import randint, shuffle
    from tempfile import mkdtemp
    from ansible.module_utils.common._collections_compat import Mapping, Sequence


# Generated at 2022-06-13 00:01:19.857060
# Unit test for function matchpathcon
def test_matchpathcon():
    from tempfile import mkdtemp
    from shutil import rmtree


# Generated at 2022-06-13 00:01:27.053638
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
  # First, check for file
  try:
    path = "/etc/hosts"
    (rc, con) = lgetfilecon_raw(path)
    assert rc == 0
    assert con is not None
  except:
    assert False
  # Now check for directory
  try:
    path = "/etc"
    (rc, con) = lgetfilecon_raw(path)
    assert rc == 0
    assert con == "system_u:object_r:admin_home_t:s0"
  except:
    assert False


# Generated at 2022-06-13 00:01:36.108124
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():

    # selinux_lib.lgetfilecon_raw shouldn't exist in the module if the corresponding c-function is not present in libselinux
    if not hasattr(_selinux_lib, "lgetfilecon_raw"):
        return

    # Set the function values based on the value of the selinux policy file path
    selinux_policy_file = "/etc/selinux/targeted/contexts/files/file_contexts.local"
    if os.path.exists(selinux_policy_file):
        function_param_value = "system_u:object_r:etc_t:s0"
        function_return_value = 0
    else:
        function_param_value = "system_u:object_r:etc_t:s0"
        function_return_value = -1

    #

# Generated at 2022-06-13 00:01:41.868951
# Unit test for function matchpathcon
def test_matchpathcon():
    import subprocess
    rc, selinux_label = selinux_getenforcemode()
    if rc != 0:
        print("Error in get enforce mode")
        return False

    if selinux_label != 0:
        print("SELinux is not in permissive mode")
        return False

    rc, policy_type = selinux_getpolicytype()
    if rc != 0:
        print("Error in get policy type")
        return False

    if policy_type != 'targeted':
        print("Policy type is not targeted. Test cannot be run")
        return False

    # Create a new temporary file

# Generated at 2022-06-13 00:01:44.619230
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    con = lgetfilecon_raw('/')
    print(con)


# Generated at 2022-06-13 00:01:47.837536
# Unit test for function matchpathcon
def test_matchpathcon():
    mod = sys.modules[__name__]
    func = getattr(mod, "matchpathcon")
    (rc, con) = func("/tmp", 1)
    assert(rc == 0), "matchpathcon failed"


# Generated at 2022-06-13 00:01:50.380113
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    try:
        assert len(lgetfilecon_raw('/tmp')) == 2
    except OSError as exc:
        if exc.errno != errno.ENOENT:
            raise


# Generated at 2022-06-13 00:02:02.656527
# Unit test for function matchpathcon
def test_matchpathcon():
    try:
        selinux_getpolicytype()
    except OSError:
        return

    (rc0, context) = lgetfilecon_raw('/usr/bin/python')
    (rc1, context_nn) = matchpathcon('/usr/bin/python', 0)
    context_nn = context_nn.rstrip('\0')

    assert rc0 == 0
    assert rc1 == 0
    assert context == context_nn

    (rc2, context_nn) = matchpathcon('/usr/bin/python', 1)
    context_nn = context_nn.rstrip('\0')

    assert rc2 == 0
    assert context == context_nn

    (rc2, context_nn) = matchpathcon('/usr/bin/python', 255)
    context_nn = context_nn.rstrip

# Generated at 2022-06-13 00:02:14.581172
# Unit test for function matchpathcon
def test_matchpathcon():
    if not is_selinux_enabled():
        raise RuntimeError('SELinux not enabled, skipping')

    rc = matchpathcon('/etc/passwd', 0)
    assert rc[0] == 0
    assert rc[1].startswith('system_u:object_r:passwd_file_t:s0')

    rc = matchpathcon('/etc/passwd', 0o0400)
    assert rc[0] == 0
    assert rc[1].startswith('system_u:object_r:passwd_file_t:s0')

    rc = matchpathcon('/etc/passwd', 0o0401)
    assert rc[0] == 0
    assert rc[1].startswith('system_u:object_r:passwd_file_t:s0')

    rc = match

# Generated at 2022-06-13 00:02:17.736525
# Unit test for function matchpathcon
def test_matchpathcon():
    path = "/dev/null"
    mode = 0
    ret = matchpathcon(path, mode)

    rc = ret[0]
    con = ret[1]
    assert rc == 0

# Generated at 2022-06-13 00:02:29.792141
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    from os.path import dirname, realpath, join
    lpath = join(dirname(realpath(__file__)), 'unused')
    [rc, con] = lgetfilecon_raw(lpath)
    assert rc == 0
    assert con == 'unconfined_u:unconfined_r:unlabeled_t:s0'
    [rc, con] = lgetfilecon_raw('/')
    assert rc == 0
    assert con == 'system_u:object_r:rootfs_t:s0'

# Generated at 2022-06-13 00:02:36.377246
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = b'/tmp/test1'
    mode = oct(os.stat(path).st_mode)[-3:]
    expected = 3
    rc, con = lgetfilecon_raw(path)
    assert rc == expected, 'Invalid return-code for lgetfilecon_raw(%s)' % path
    assert con.split(b':')[2] == mode, 'Unexpected file context for %s' % path


# Generated at 2022-06-13 00:02:45.244563
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # create temporary file
    import tempfile
    (_, test_file) = tempfile.mkstemp(prefix='selinux_wrapper_test', text=True)

    # result of lgetfilecon_raw before checking the constraint
    tmp_con, tmp_rc = lgetfilecon_raw(test_file)
    assert tmp_rc < 0

    # set the file constraint
    tmp_rc_setfilecon = os.system("chcon -t user_home_t  " + test_file)
    assert tmp_rc_setfilecon == 0

    # result of lgetfilecon_raw after checking the constraint
    tmp_con_after, tmp_rc_after = lgetfilecon_raw(test_file)
    assert tmp_rc_after >= 0

    # check that the constraint got set
    assert tmp_con_

# Generated at 2022-06-13 00:02:50.298123
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import pytest

    try:
        mode, selinfo = lgetfilecon_raw("/etc/hosts")
        assert mode <= 0
        assert selinfo == "unconfined_u:object_r:etc_t:s0"
    except OSError as e:
        pytest.skip("SELinux not available. skipping")

# Generated at 2022-06-13 00:02:56.907548
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    test_path = '/etc/group'
    test_con = lgetfilecon_raw(test_path)
    assert test_con[0] == 0, "lgetfilecon_raw return value is not zero"
    assert test_con[1] == 'system_u:object_r:etc_runtime_t:s0', "lgetfilecon_raw function seems not work, please check!"


# Generated at 2022-06-13 00:03:05.951053
# Unit test for function matchpathcon
def test_matchpathcon():
    curr_mode = selinux_getenforcemode()[1]
    curr_type = selinux_getpolicytype()[1]
    assert curr_mode >= 0
    assert curr_type != ''
    assert matchpathcon('/etc', 0) == [0, 'system_u:object_r:etc_t:s0']
    assert matchpathcon('/etc/hosts', 0) == [0, 'system_u:object_r:etc_t:s0']
    assert matchpathcon('/tmp', 0) == [0, 'system_u:object_r:tmp_t:s0']
    assert matchpathcon('/foo', 0) == [-1, 'system_u:object_r:etc_t:s0']

# Generated at 2022-06-13 00:03:12.122313
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = b'/etc/ssh/sshd_config'
    rc, con = lgetfilecon_raw(path)
    assert rc == 0, 'unable to retrieve context from path: {0}. Error code: {1}'.format(to_native(path), rc)
    assert con == 'system_u:object_r:ssh_etc_t:s0', 'context != system_u:object_r:ssh_etc_t:s0. context = {0}'.format(con)


# Generated at 2022-06-13 00:03:13.910197
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon('/etc/selinux/config', 0)
    if rc == 0:
        print(con)

# Generated at 2022-06-13 00:03:18.209179
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import os, sys

    try:
        # Sample data
        path = "/var/log/messages"

        # Call function
        result = lgetfilecon_raw(path)

        print(result)

    except Exception as err:
        print(err)
        sys.exit(1)


# Generated at 2022-06-13 00:03:21.989480
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon(b'unittest_file', 1)
    assert rc == 0
    assert con == 'unconfined_u:object_r:user_home_t:s0'

    rc, con = lgetfilecon_raw(b'unittest_file')
    assert rc == 0
    assert con == 'unconfined_u:object_r:user_home_t:s0'

# Generated at 2022-06-13 00:03:33.009289
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = os.path.abspath(__file__)
    rc, con = lgetfilecon_raw(path)
    assert rc == 0
    assert con
    assert con.startswith("system_u:object_r:ansible_file_t:s0:c")


# Generated at 2022-06-13 00:03:43.856189
# Unit test for function matchpathcon
def test_matchpathcon():
    # tests for files under /etc/selinux
    [rc, con] = matchpathcon("/etc/selinux/config", 0)
    assert rc == 0
    assert con == "system_u:object_r:etc_t:s0"
    [rc, con] = matchpathcon("/etc/selinux/config", 1)
    assert rc == 0
    assert con == "system_u:object_r:etc_t:s0"
    [rc, con] = matchpathcon("/etc/selinux/config", 2)
    assert rc == 0
    assert con == "system_u:object_r:etc_t:s0"
    # tests for files under /etc/selinux/targeted/etc/security/opasswd

# Generated at 2022-06-13 00:03:46.485505
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Test for the two return values, success and failure
    assert lgetfilecon_raw('/')[0] == 0
    assert lgetfilecon_raw('/nonexistingfile')[0] == -1

# Generated at 2022-06-13 00:03:52.060953
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Test file with selinux_context
    rc, con = lgetfilecon_raw('/etc/selinux/config')
    assert rc == 0
    assert con == 'unconfined_u:object_r:etc_t:s0'

    # Test file without selinux_context
    rc, con = lgetfilecon_raw('/etc/passwd')
    assert rc == -1
    assert con is None

# Generated at 2022-06-13 00:04:01.944096
# Unit test for function matchpathcon
def test_matchpathcon():
    import os

    # setup
    os.environ['SELINUX_ROOT'] = "/tmp"
    os.environ['SELINUX_CONFIG'] = "/tmp/selinux/config"
    os.environ['SELINUX_POLICY_ROOT'] = "/tmp/selinux/policy"
    os.environ['SELINUX_LOG_ROOT'] = "/tmp/selinux/log"
    os.environ['SELINUX_SEMANAGE_CONFIG_PATH'] = "/tmp/selinux"
    os.environ['SELINUX_SEMANAGE_PATH'] = "/tmp/selinux"
    os.environ['SELINUX_PATH'] = "/tmp/selinux"

# Generated at 2022-06-13 00:04:04.462181
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon('/tmp/foo', 0)
    if rc != 0:
        raise OSError(rc, '%s: %s' % (rc, con))

# Generated at 2022-06-13 00:04:07.706609
# Unit test for function matchpathcon
def test_matchpathcon():
    print('Attempting to match the context for path, the context should be system_u:object_r:etc_t:s0')
    print(matchpathcon('/etc', 0)[1])


# Generated at 2022-06-13 00:04:11.477430
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    """
    Test that lgetfilecon_raw handles a path
    """

    try:
        con = lgetfilecon_raw('/')
        assert len(con) == 2
        assert con[0] == 0
        assert 'security' in con[1]
    except OSError:
        assert False
    except AssertionError:
        assert False

# Generated at 2022-06-13 00:04:16.488565
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    test_dirname = u'/etc'
    result = lgetfilecon_raw(test_dirname)
    assert result[0] == 0, result[1]
    assert result[1] == u'system_u:object_r:etc_t:s0', result[1]

# Generated at 2022-06-13 00:04:17.928579
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():

    path = '/etc/selinux'

    rc, con = lgetfilecon_raw(path)

    assert rc == 0
    assert con == 'system_u:object_r:etc_t:s0'



# Generated at 2022-06-13 00:04:41.735702
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    from ansible.module_utils.selinux import lgetfilecon_raw
    rc, con = lgetfilecon_raw("/usr/bin/python")
    assert rc == 0
    assert con == "system_u:object_r:bin_t:s0"
    rc, con = lgetfilecon_raw("/usr/bin/doesnotexist")
    assert rc == -1
    rc, con = lgetfilecon_raw("/usr/bin/")
    assert rc == -1
    rc, con = lgetfilecon_raw("")
    assert rc == -1


# Generated at 2022-06-13 00:04:48.692366
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # /proc/cpuinfo is always readable
    assert lgetfilecon_raw('/proc/cpuinfo') == [0, 'unconfined_u:object_r:proc_cpuinfo_t:s0']

    # /proc/invalid is not allowed to be read
    assert lgetfilecon_raw('/proc/invalid') == [-1, 'Permission denied']

    # /tmp/does_not_exist should have an error
    assert lgetfilecon_raw('/tmp/does_not_exist') == [-1, 'No such file or directory']



# Generated at 2022-06-13 00:04:51.918250
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw(b'/etc/fstab')
    assert rc == 0
    assert con == 'system_u:object_r:etc_t:s0\n'



# Generated at 2022-06-13 00:04:56.246583
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    test_path = '/etc/shadow'

    rc, val = lgetfilecon_raw(test_path)
    assert rc == 0
    assert val.startswith("system_u:object_r:shadow_t:s0")

# Generated at 2022-06-13 00:05:01.441918
# Unit test for function matchpathcon
def test_matchpathcon():
    path = b'/test/'
    mode = 3
    rc, con = matchpathcon(path, mode)
    if rc != 0:
        print("Error: matchpathcon failed! rc={}, con={}".format(rc, con))
        assert False
    else:
        print("Success: matchpathcon succeeded! rc={}, con={}".format(rc, con))
        assert True


# Generated at 2022-06-13 00:05:10.260449
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, ctx = matchpathcon('/etc/passwd', 0)
    assert rc == 0
    assert ctx == 'system_u:object_r:passwd_file_t'

    rc, ctx = matchpathcon('/etc/passwd', os.R_OK)
    assert rc == 0
    assert ctx == 'system_u:object_r:passwd_file_t'

    rc, ctx = matchpathcon('/etc/passwd', os.W_OK)
    assert rc == 0
    assert ctx == 'system_u:object_r:passwd_file_t:s0'

    rc, ctx = matchpathcon('/etc/passwd', os.X_OK)
    assert rc == 0

# Generated at 2022-06-13 00:05:14.885718
# Unit test for function matchpathcon
def test_matchpathcon():
    test_path = b'/var/www/html'
    mode = os.F_OK
    expected_result = 0

    result = matchpathcon(test_path, mode)
    # Check that the returned result is the expected value
    assert result[0] == expected_result


# Generated at 2022-06-13 00:05:18.985529
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = b'/etc/hosts'
    rc, con = lgetfilecon_raw(path)
    assert rc == 0
    assert con.startswith(b':')



# Generated at 2022-06-13 00:05:26.297921
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Get the context of /etc
    [rc, con] = lgetfilecon_raw('/etc')

    assert rc == 0
    assert con.startswith('system_u:object_r')
    assert con.endswith(':s0')

    # Verify /etc/passwd has type user_home_t
    [rc, con] = lgetfilecon_raw('/etc/passwd')
    assert rc == 0
    assert con.startswith('system_u:object_r')
    assert con.endswith(':s0')

    # Verify /etc/passwd has type user_home_t
    [rc, con] = lgetfilecon_raw('/nosuchfile')
    assert rc != 0


# Generated at 2022-06-13 00:05:37.579832
# Unit test for function matchpathcon
def test_matchpathcon():
    __file__ = sys._getframe().f_code.co_filename
    dir_name, filename = os.path.split(os.path.realpath(__file__))
    assert(filename == 'ansible.utils.selinux.py')
    test_path = os.path.join(dir_name, "test_file")
    test_file = open(test_path, "w")
    test_file.write("test")
    test_file.close()
    con = c_char_p()
    rc = _selinux_lib.matchpathcon(test_path, 0, byref(con))
    assert(rc == 0)
    assert(con.value == b"system_u:object_r:default_t")
    # test with a non-existent file
    rc = _selinux_

# Generated at 2022-06-13 00:06:21.961354
# Unit test for function matchpathcon
def test_matchpathcon():
    """
    Invoke matchpathcon on a file which exists in the context
    of the current policy.  If this fails, it should be
    because the file does not exist.
    """
    try:
        from ansible.module_utils.selinux import matchpathcon_fatal
        rc, curcon = matchpathcon_fatal('/etc/selinux/config')
        assert rc == 0
    except:
        # If an exception is raised, we should be running
        # without selinux
        assert matchpathcon('/etc/selinux/config', 0) == (0, 'unlabeled')

# Generated at 2022-06-13 00:06:23.529342
# Unit test for function matchpathcon
def test_matchpathcon():
    # this function needs ctypes to be enabled, so just ensure the function runs without error
    res, _ = matchpathcon('/etc/passwd', 0)
    assert res == 0

# Generated at 2022-06-13 00:06:31.825889
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import os
    import tempfile

    t_file = None
    t_name = None
    try:
        fd, t_name = tempfile.mkstemp()
        t_file = os.fdopen(fd)
        rc, con = lgetfilecon_raw(t_name)
        assert rc == 0
        assert con == 'system_u:object_r:tmp_t:s0'
    finally:
        if t_file:
            t_file.close()

        if t_name:
            os.unlink(t_name)

# Generated at 2022-06-13 00:06:33.219822
# Unit test for function matchpathcon
def test_matchpathcon():
    return matchpathcon('/etc/passwd', 0)


# Generated at 2022-06-13 00:06:38.988341
# Unit test for function matchpathcon
def test_matchpathcon():
    if is_selinux_enabled():
        type = matchpathcon('/usr/bin/python', os.R_OK)
        if type[0] >= 0:
            print("The SELinux type of file /usr/bin/python is: {0}".format(type[1]))


if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-13 00:06:41.725731
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (rc, con) = lgetfilecon_raw('/etc/hosts')
    if rc == 0:
        print(con)
    else:
        print(r"Can't get context")


# Generated at 2022-06-13 00:06:49.213127
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import tempfile
    # lgetfilecon_raw is not available for python3
    if sys.version_info[0] > 2:
        raise ImportError('lgetfilecon_raw is not available for python3')
    if not os.path.exists('/sbin/init'):
        raise ImportError('SELinux is not active')
    with tempfile.NamedTemporaryFile() as f:
        path = f.name
        try:
            rc, con = lgetfilecon_raw(path)
        except OSError as e:
            print('Function lgetfilecon_raw failed with return code %d: %s' % (e.errno, e.strerror))
            raise e
        assert rc == 0, 'Functionlgetfilecon_raw failed'

# Generated at 2022-06-13 00:06:57.676906
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    """Test function lgetfilecon_raw"""
    policy_version = security_policyvers()
    enforcemode, enforcemode_v = selinux_getenforcemode()
    policytype, policytype_v = selinux_getpolicytype()

    if policy_version > 1:
        # Ensure compatibility with security_context_t
        assert policytype_v == 'mcs'
    if enforcemode_v == 0:
        # If SELinux is in Permissive mode, we assume correct
        # If SELinux is in Enforcing mode, we assume correct
        assert enforcemode == 0
    else:
        # If SELinux is in Enforcing mode, we assume correct
        assert enforcemode == 0
        # If SELinux is in Enforcing mode, we assume correct
        assert enforcemode_v == 1

# Generated at 2022-06-13 00:07:04.133262
# Unit test for function matchpathcon
def test_matchpathcon():
    from ansible.module_utils.selinux import matchpathcon
    from ansible.module_utils._text import to_bytes
    import tempfile

    # selinux context for temporary file
    filename = to_bytes(tempfile.mkstemp()[1])
    stat_mode = 0o644
    path = to_bytes("/etc/selinux/test/test")
    expected_context = "system_u:object_r:etc_t:s0"
    selinux_config_dir = to_bytes("/etc/selinux/test")

    # creating a temporary directory

# Generated at 2022-06-13 00:07:09.916992
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import tempfile
    import unittest
    pathname = tempfile.mktemp()
    fd = os.open(pathname, os.O_RDONLY | os.O_CREAT, 0o600)
    os.close(fd)
    lgetfilecon_raw(pathname)
    class TestMiscellaneous(unittest.TestCase):
        # This is a dummy testcase.
        def test_lgetfilecon_raw(self):
            self.assertTrue(True)
    unittest.main()

# Generated at 2022-06-13 00:08:28.524559
# Unit test for function matchpathcon
def test_matchpathcon():
    (rc, con) = matchpathcon(b'/etc/passwd', 1)
    assert rc == 0
    assert isinstance(con, type(''))


# Generated at 2022-06-13 00:08:32.082900
# Unit test for function matchpathcon
def test_matchpathcon():
    # Create a temporary file (a dir)
    import tempfile
    dir_file = tempfile.mkdtemp()
    # Get the context and mode of the file
    con, mode = matchpathcon(dir_file, 0)
    os.rmdir(dir_file)

# Generated at 2022-06-13 00:08:34.437417
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw('/bin/ls') == [0, 'system_u:object_r:bin_t:s0']


# Generated at 2022-06-13 00:08:35.878665
# Unit test for function matchpathcon
def test_matchpathcon():
    assert matchpathcon('/sys/fs/cgroup', os.R_OK)[0] == 0

# Generated at 2022-06-13 00:08:43.101091
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw(b'/tmp')
    assert rc == 0, 'Failed to get context of /tmp'
    assert con != '', 'Context of /tmp is empty'
    os.close(os.open('/tmp/foo', os.O_CREAT))
    rc, con = lgetfilecon_raw(b'/tmp/foo')
    assert rc == 0, 'Failed to get context of /tmp/foo'
    assert con != '', 'Context of /tmp/foo is empty'
    os.remove('/tmp/foo')
    os.mkdir('/tmp/bar')
    rc, con = lgetfilecon_raw(b'/tmp/bar')
    assert rc == 0, 'Failed to get context of /tmp/bar'

# Generated at 2022-06-13 00:08:45.668201
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = "/etc/passwd"
    ret = lgetfilecon_raw(path)
    assert ret[1] == "system_u:object_r:etc_t:s0"
    assert ret[0] == 0

# Generated at 2022-06-13 00:08:50.451955
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # pylint: disable=protected-access
    func = _selinux_lib.lgetfilecon_raw
    func.restype = c_int
    func.argtypes = [c_char_p, POINTER(c_char_p)]
    assert func('/tmp', lambda x: 0) == 0


__all__ = ['selinux_getenforcemode', 'selinux_getpolicytype', 'test_lgetfilecon_raw']

# Generated at 2022-06-13 00:08:59.056247
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    try:
        from ansible.module_utils._text import to_text
    except ImportError:
        from ansible_collections.misc.not_a_real_collection.plugins.module_utils._text import to_text

    # Test if the path is None
    rc, con = lgetfilecon_raw(None)
    assert rc == -1
    assert to_text(con) == ''

    # Test if the path is a string
    rc, con = lgetfilecon_raw('abc')
    assert rc == -1
    assert to_text(con) == ''

    # Test if the path is a bytes string
    rc, con = lgetfilecon_raw(b'abc')
    assert rc == -1
    assert to_text(con) == ''

    # Test if the path is valid
    rc, con

# Generated at 2022-06-13 00:09:06.830483
# Unit test for function matchpathcon
def test_matchpathcon():
    path = '/etc/ansible'
    result = matchpathcon(path, 0)
    assert isinstance(result, list)
    assert len(result) == 2
    assert isinstance(result[0], int)
    if result[0] == 0:
        assert isinstance(result[1], str)
        assert result[1] != ''
    else:
        # This test is designed to be run in an environment where `matchpathcon` is basically always
        # going to succeed, so if it didn't then that's probably a problem that deserves to break
        # the test run.  If anyone wants to make this test more robust in the future, that's fine
        # but please don't make it less robust than it is now.
        assert False, 'matchpathcon returned error code %s' % result[0]