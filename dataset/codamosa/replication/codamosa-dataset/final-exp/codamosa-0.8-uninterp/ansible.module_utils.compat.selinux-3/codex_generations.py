

# Generated at 2022-06-12 23:59:11.379756
# Unit test for function matchpathcon
def test_matchpathcon():
    assert isinstance(matchpathcon('/tmp/foo', 0), list), \
        'return value from matchpathcon was not a list'
    assert isinstance(matchpathcon('/tmp/foo', 0)[0], int), \
        'return value from matchpathcon was not an integer'
    assert isinstance(matchpathcon('/tmp/foo', 0)[1], str), \
        'return value from matchpathcon was not a string'

# Generated at 2022-06-12 23:59:23.062301
# Unit test for function matchpathcon
def test_matchpathcon():
    path = "/tmp/test_matchpathcon_file"

# Generated at 2022-06-12 23:59:33.276077
# Unit test for function matchpathcon
def test_matchpathcon():
    # Test case identifier
    test_id = 1

    # Path, Mode and expected result

# Generated at 2022-06-12 23:59:34.887542
# Unit test for function matchpathcon
def test_matchpathcon():
    res, con = matchpathcon('/tmp', 0)
    print(res)
    print(con)

# Generated at 2022-06-12 23:59:46.066411
# Unit test for function matchpathcon
def test_matchpathcon():
    con = c_char_p()

# Generated at 2022-06-12 23:59:48.127670
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon('/home/sugand/test', 0)
    print(rc)
    print(con)



# Generated at 2022-06-12 23:59:50.508747
# Unit test for function matchpathcon
def test_matchpathcon():
    assert matchpathcon('/var/log/messages', 0) == [0, 'system_u:object_r:etc_runtime_t']


# Generated at 2022-06-12 23:59:56.157923
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (rc, con) = lgetfilecon_raw('/etc/hosts')
    print('lgetfilecon_raw returns: {} {}'.format(rc, con))
    if int(rc) != 0:
        print('Error lgetfilecon_raw: {}'.format(con))
        exit(-1)


# Generated at 2022-06-12 23:59:58.017462
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    home = os.environ['HOME']
    assert lgetfilecon_raw(home) == 0


# Generated at 2022-06-13 00:00:01.248984
# Unit test for function matchpathcon
def test_matchpathcon():
    results = None

    try:
        results = matchpathcon('/', os.R_OK)
    except OSError:
        print('Unable to load matchpathcon.')

    if results is not None:
        rc, con = results

        assert rc == -2
        assert con == 'system_u:object_r:rootfs:s0'


if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-13 00:00:05.561688
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon('/foo/bar', 0)
    assert rc == 0
    assert con == 'unlabeled_t'


# Generated at 2022-06-13 00:00:09.642168
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    context = lgetfilecon_raw("/etc/shadow")
    if context[0] == 0:
        print("Context: " + context[1])
    else:
        print("lgetfilecon_raw failed: " + os.strerror(-context[0]))



# Generated at 2022-06-13 00:00:16.875615
# Unit test for function matchpathcon
def test_matchpathcon():
    path = '/'
    mode = 0
    expected_result = [0, u'user_u:object_r:root_t:s0-s0:c0.c1023']
    actual_result = matchpathcon(path, mode)
    if actual_result != expected_result:
        raise Exception("actual: %s, expected: %s" % (actual_result, expected_result))
    print("actual: %s, expected: %s, matched" % (actual_result, expected_result))


# Generated at 2022-06-13 00:00:24.603717
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    """
    This function ensures that lgetfilecon_raw is working as expected.
    We check that the output is what we expect, and we also check that
    an error is returned for a file that does not exist.
    """
    from ansible.module_utils._text import to_text

    result = lgetfilecon_raw(__file__)
    assert result[0] == 0
    assert result[1] == 'system_u:object_r:etc_runtime_t:s0'

    result = lgetfilecon_raw("/nonexistent/file")
    assert result[0] == -1
    assert result[1] is None
    python_version = sys.version_info

# Generated at 2022-06-13 00:00:26.345537
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = '/var/log/ansible.log'
    rc, con = lgetfilecon_raw(path)

    assert rc == 0
    assert con.startswith('system_u:object_r:')


# Generated at 2022-06-13 00:00:28.795131
# Unit test for function matchpathcon
def test_matchpathcon():
    (rc, con) = matchpathcon('/tmp/foo.txt', 0)
    assert rc == 0
    assert con == 'tmp:object_r:default_t:s0'



# Generated at 2022-06-13 00:00:33.664373
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon(b'/sbin/modprobe', 1)
    assert rc == 0
    assert con == 'system_u:object_r:kernel_modprobe_t'



# Generated at 2022-06-13 00:00:39.801696
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    try:
        if not os.path.exists('/selinux/booleans/'):
            raise OSError('/selinux/booleans/ does not exist')
        rc, con = lgetfilecon_raw('/selinux/booleans/')
        print(rc)
        print(con)
    except OSError as e:
        print(to_native(e))



# Generated at 2022-06-13 00:00:45.888288
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import subprocess
    import tempfile
    import os

    (tmpfile, pathname) = tempfile.mkstemp()
    os.close(tmpfile)

    try:
        cmd = ['touch', pathname]
        subprocess.Popen(cmd).wait()
        cmd = ['chcon', '-u', 'system_u:object_r:system_dbusd_tmp_t:s0', pathname]
        subprocess.Popen(cmd).wait()
        rc, con = lgetfilecon_raw(pathname)
        assert rc == 0
        assert con == 'system_u:object_r:system_dbusd_tmp_t:s0'
    finally:
        os.remove(pathname)

# Generated at 2022-06-13 00:00:51.527932
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    testpath = '/etc/passwd'
    [rc, con] = lgetfilecon_raw(testpath)
    if rc != 0:
        raise ValueError('bad lgetfilecon_raw return value {0}'.format(rc))
    if '/usr/sbin/crond' in con:
        raise ValueError('bad lgetfilecon_raw return: {0}'.format(con))


# Generated at 2022-06-13 00:00:58.307938
# Unit test for function matchpathcon
def test_matchpathcon():
    result = matchpathcon('/usr/bin/passwd', 0)
    assert result[0] == 0
    assert result[1] == 'system_u:object_r:passwd_exec_t:s0'

# Generated at 2022-06-13 00:01:02.375418
# Unit test for function matchpathcon
def test_matchpathcon():
    # Return rc, con if matches, else No match
    rc, con = matchpathcon("/etc", 0)
    if rc == 0:
        print(to_native(con))
    else:
        print("No match")


if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-13 00:01:09.705151
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import unittest
    libselinux_py = __import__(__name__)

    class Lgetfilecon_rawTest(unittest.TestCase):
        def setUp(self):
            self.path = '/'

        def tearDown(self):
            self.path = None

        def test_lgetfilecon_raw(self):
            self.assertEqual(libselinux_py.lgetfilecon_raw(self.path), [0, 'system_u:object_r:root_t:s0'])

    unittest.main()

# Generated at 2022-06-13 00:01:17.801844
# Unit test for function matchpathcon
def test_matchpathcon():
    """
    Unit test to check the matchpathcon function
    """
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.selinux import matchpathcon

    selinux_module = AnsibleModule(
        argument_spec=dict(
            path=dict(type='str', required=True),
            mode=dict(type='int', required=True),
        ),
    )

    path = selinux_module.params['path']
    mode = selinux_module.params['mode']

    rc, con = matchpathcon(path, mode)
    if rc < 0:
        selinux_module.fail_json(msg='unable to find the path con %s: %s' % (path, os.strerror(rc * -1)))

    selinux_module.exit_json

# Generated at 2022-06-13 00:01:23.155238
# Unit test for function matchpathcon
def test_matchpathcon():
    from ansible_collections.misc.not_a_real_collection.plugins.module_utils.selinux.test import Test

    test = Test(module=None)

    test.assertEqual(matchpathcon("/", 0), [0, 'system_u:object_r:root_t:s0'])
    test.assertEqual(matchpathcon("/var/log", 0), [0, 'system_u:object_r:var_log_t:s0'])
    test.assertEqual(matchpathcon("/var/log/yum.log", 0), [0, 'system_u:object_r:var_log_t:s0'])

# Generated at 2022-06-13 00:01:29.608453
# Unit test for function matchpathcon
def test_matchpathcon():
    # Test 1
    rc, con = matchpathcon('/var/log/test.log', 0)
    assert rc == 0
    assert con == 'system_u:object_r:var_log_t:s0'
    # Test 2
    rc, con = matchpathcon('/var/log/test.log', 1)
    assert rc == 0
    assert con == 'root:object_r:var_log_t:s0'

# Generated at 2022-06-13 00:01:37.842468
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import tempfile
    import shutil
    import os
    import pwd
    import grp

    [rc, c0] = is_selinux_enabled()
    if rc < 0:
        print('selinux_enabled() call failed')
        sys.exit(1)

    if c0 != 1:
        print('selinux not enabled')
        sys.exit(0)

    tmpdir = tempfile.mkdtemp()

    if os.geteuid() == 0:
        (uid, gid) = pwd.getpwnam('nobody')
    else:
        uid = gid = -1

    rc = os.chown(tmpdir, uid, gid)

# Generated at 2022-06-13 00:01:42.112957
# Unit test for function matchpathcon
def test_matchpathcon():
    # Check that matchpathcon works
    rc, con = matchpathcon('/etc/passwd', 0)
    assert rc == 0
    assert con in ['system_u:object_r:etc_runtime_t:s0', 'unlabeled_t:unlabeled_t']

    # Check that matchpathcon does not crash if path does not exist
    rc, con = matchpathcon('/path/that/does/not/exist', 0)
    assert rc == -1

# Generated at 2022-06-13 00:01:46.623360
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = b"/etc/passwd"
    [rc, con] = lgetfilecon_raw(path)
    assert rc == 0
    assert con == "system_u:object_r:passwd_file_t:s0"


# Generated at 2022-06-13 00:01:51.321776
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import re
    import os

    pattern = re.compile(r'.+:.+:.+')
    assert len(pattern.findall(os.getcwd())) > 0
    assert len(pattern.findall(os.environ['HOME'])) > 0

    assert lgetfilecon_raw(os.getcwd())[0] == 0
    assert lgetfilecon_raw(os.environ['HOME'])[0] == 0

# Generated at 2022-06-13 00:01:59.607991
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw('/etc/passwd')
    print('Return code: %s' % rc)
    if rc == 0:
        print('Context: %s' % con)
    else:
        print('Error in retrieving context: %s' % con)


# Generated at 2022-06-13 00:02:03.192465
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    def check_result(result):
        assert result[0] == 0
        assert result[1] == b':object_r:var_t:s0'

    check_result(lgetfilecon_raw(b'/var/log'))
    check_result(lgetfilecon_raw('/var/log'))

# Generated at 2022-06-13 00:02:14.966777
# Unit test for function matchpathcon
def test_matchpathcon():
    """Unit tests for matchpathcon()."""
    from ansible_collections.ansible.posix.plugins.modules.selinux import selinux_utils

    if not selinux_utils.is_selinux_enabled():
        raise AssertionError("selinux_utils isn't enabled. Test skipped")

    file_path = 'matchpathcon.file'
    dir_path = 'matchpathcon.dir'

    _file = open(file_path, 'w')
    _file.close()
    os.mkdir(dir_path)
    error = False


# Generated at 2022-06-13 00:02:18.260206
# Unit test for function matchpathcon
def test_matchpathcon():
    path = b'/etc/yum/pluginconf.d'
    print('matchpathcon(%s) -> %s' % (path, repr(matchpathcon(path, 0))))


if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-13 00:02:31.113443
# Unit test for function matchpathcon
def test_matchpathcon():
    import os
    import tempfile
    import shutil
    import stat

    file_path = tempfile.mkdtemp()
    (fd, tmp_file) = tempfile.mkstemp(dir=file_path)
    os.close(fd)
    os.remove(tmp_file)
    os.mkdir(tmp_file, stat.S_IRWXU)

    (rc, file_context) = selinux_getenforcemode()
    assert rc == 0
    assert file_context == 1

    (rc, policy_type) = selinux_getpolicytype()
    assert rc == 0
    assert isinstance(policy_type, str)

    (rc, matching_path) = matchpathcon(tmp_file, os.R_OK | os.W_OK | os.X_OK)

# Generated at 2022-06-13 00:02:34.050580
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (rc, con) = lgetfilecon_raw('/tmp')
    assert rc == 0
    assert con == 'system_u:object_r:tmp_t:s0'

# Generated at 2022-06-13 00:02:37.283237
# Unit test for function matchpathcon
def test_matchpathcon():
    mpcon = matchpathcon("/var/log/messages", 0)
    print("Result of matchpathcon() is ", mpcon)
    assert mpcon[0] == 0, "Something went wrong with matchpathcon()"



# Generated at 2022-06-13 00:02:40.053906
# Unit test for function matchpathcon
def test_matchpathcon():
    (rc, con) = matchpathcon('/', 0)
    if rc != 0:
        raise ValueError('matchpathcon returned {0}'.format(rc))
    if con not in ('system_u:object_r:root_t:s0', 'system_u:object_r:unlabeled_t:s0'):
        raise ValueError('matchpathcon returned {0}'.format(con))



# Generated at 2022-06-13 00:02:43.031986
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    [rc, con] = _selinux_lib.lgetfilecon_raw('/', None)
    assert rc == 0
    assert con == b"system_u:object_r:root_t:s0"



# Generated at 2022-06-13 00:02:52.282889
# Unit test for function matchpathcon
def test_matchpathcon():
    path = b"/home/foo"
    mode = 1
    f = matchpathcon(path, mode)
    if f[1] == "unlabeled":
        print("Labeling not enabled")
    elif f[1] == "<<none>>":
        print("File or directory not found")
    elif f[1] == "<<error>>":
        print("Error reading context")
    else:
        print(f[1])


# Generated at 2022-06-13 00:03:00.573271
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = '/etc/security/selinux/src/policy/policy.conf'
    rc, out = lgetfilecon_raw(path)
    print('return code {0}'.format(rc))
    print('context {0}'.format(out))



# Generated at 2022-06-13 00:03:10.325842
# Unit test for function matchpathcon
def test_matchpathcon():
    _funcmap = dict(
        matchpathcon=[{'path': '/this/is/a/test', 'mode': 0}, [0, 'unconfined_u:object_r:user_tmp_t:s0'], {'path': '/this/is/a/test', 'mode': -1}, [0, 'unconfined_u:object_r:user_tmp_t:s0']],
        security_getenforce=[{}, [0], {}],
        security_policyvers=[{}, [3], {}],
        is_selinux_mls_enabled=[{}, [1], {}],
        is_selinux_enabled=[{}, [1], {}])

    # Enforce with mode 0

# Generated at 2022-06-13 00:03:14.943855
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, selinux_context = matchpathcon(b'/tmp', 0)
    assert rc == 0
    assert selinux_context == 'system_u:object_r:tmp_t:s0'
    rc, selinux_context = matchpathcon(b'/usr/sbin/sshd', 0)
    assert rc == 0
    assert selinux_context == 'system_u:system_r:sshd_t:s0'


# Generated at 2022-06-13 00:03:18.398559
# Unit test for function matchpathcon
def test_matchpathcon():
    """Unit test for matchpathcon"""
    result = matchpathcon("/etc/shadow", 0)
    assert result[1] == "system_u:object_r:shadow_t:s0"

# Generated at 2022-06-13 00:03:22.990018
# Unit test for function matchpathcon
def test_matchpathcon():
    path = os.path.abspath(__file__)
    mode = os.stat(path).st_mode
    rc, ocon = matchpathcon(path, mode)
    assert rc == 0
    assert ocon == "system_u:object_r:etc_runtime_t:s0"



# Generated at 2022-06-13 00:03:28.677431
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    from ansible.module_utils.selinux import lgetfilecon_raw

    r_list = lgetfilecon_raw('/etc/ssh/sshd_config')
    assert r_list[0] == 0
    assert r_list[1] == 'unconfined_u:object_r:ssh_etc_t:s0-s0:c0.c1023'

# Generated at 2022-06-13 00:03:29.526407
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert isinstance(lgetfilecon_raw('/'), tuple)



# Generated at 2022-06-13 00:03:31.823249
# Unit test for function matchpathcon
def test_matchpathcon():
    rc = matchpathcon('/etc/zshrc', 0)
    assert rc[0] == 0
    assert rc[1] == 'system_u:object_r:usr_t:s0'



# Generated at 2022-06-13 00:03:35.100809
# Unit test for function matchpathcon
def test_matchpathcon():
    try:
        _selinux_lib.matchpathcon
    except AttributeError:
        from nose import SkipTest
        raise SkipTest('matchpathcon is unavailable on this platform')

    path = '/usr/bin/python3'
    mode = os.R_OK | os.W_OK | os.X_OK
    rc, con = matchpathcon(path, mode)
    assert rc == 0
    assert con == 'unconfined_u:object_r:usr_t:s0'



# Generated at 2022-06-13 00:03:45.077290
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    def generate_test(test_case):
        context = test_case[0]
        filename = test_case[1]
        mode = test_case[2]
        result = test_case[3]

        with open(filename, 'wb') as f:
            f.write('')


# Generated at 2022-06-13 00:03:58.628737
# Unit test for function matchpathcon
def test_matchpathcon():
    if not is_selinux_enabled():
        print("SELinux is not enabled, skipping MatchPathConunit test")
        return

    # Get the label of /usr/bin/python2.7
    tbase = '/usr/bin/python'
    tver = sys.version_info
    tpath = tbase + str(tver.major) + '.' + str(tver.minor)
    rc, result = matchpathcon(tpath, os.R_OK)

    if rc != 0:
        raise OSError("Error: MatchPathCon function returned non-zero return code")

    if result == None or result.strip() == '':
        raise OSError("Error: MatchPathCon function returned an empty security label")

if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-13 00:04:04.381282
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    try:
        con = _selinux_lib.lgetfilecon_raw(b'/usr/bin/ping', 'a')
        con = con[0]
        rc = int(con[0])
        return rc
    except OSError as e:
        print('Caught OSError: {0}'.format(e))
        return -1


# Generated at 2022-06-13 00:04:08.251300
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw(b'/home/')
    if rc != 0:
        print('Test for lgetfilecon_raw: FAILED')
    else:
        print('Test for lgetfilecon_raw: PASSED')


# Generated at 2022-06-13 00:04:14.734314
# Unit test for function matchpathcon
def test_matchpathcon():

    res = matchpathcon('/tmp/test.txt', 1)
    assert res == [0, 'system_u:object_r:user_tmp_t:s0']

    # Test when file doesn't exist
    res = matchpathcon('/tmp/fake/fake.txt', 1)
    assert res == [0, 'system_u:object_r:user_tmp_t:s0']

    # Test when given a directory
    res = matchpathcon('/tmp/', 1)
    assert res == [0, 'system_u:object_r:user_tmp_t:s0']

    # Test when given a symbolic link
    os.symlink('/tmp', '/tmp/mylink')
    res = matchpathcon('/tmp/mylink', 1)

# Generated at 2022-06-13 00:04:21.595808
# Unit test for function matchpathcon
def test_matchpathcon():
    # Set error conditions
    rc, con = matchpathcon('/etc/', 0)
    assert rc == -1
    assert con is None

    rc, con = matchpathcon('/etc/', -1)
    assert rc == -1
    assert con is None

    rc, con = matchpathcon('/etc/', 100)
    assert rc == -1
    assert con is None

    # Valid condition
    rc, con = matchpathcon('/etc/', 0)
    assert rc == 0
    assert con is not None



# Generated at 2022-06-13 00:04:27.404454
# Unit test for function matchpathcon
def test_matchpathcon():
    import os
    import tempfile
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat import unittest
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock import patch

    class TestMatchpathcon(unittest.TestCase):
        tmpdir = None

        @patch('selinux.matchpathcon')
        def setUp(self, mock_matchpathcon):
            self.tmpdir = tempfile.mkdtemp()
            self.assertTrue(os.path.isdir(self.tmpdir))

            def _mock_matchpathcon(path, mode):
                return [0, 'user_u:role_r:type_t:s0']

            mock_matchpathcon.side_effect = _mock_

# Generated at 2022-06-13 00:04:38.602939
# Unit test for function matchpathcon
def test_matchpathcon():
    from ansible.module_utils.selinux import matchpathcon

    # FIXME: need to find a good test path that doesn't require either of these
    # errors = {
    #     13: "Permission Denied"
    #     39: "Function Not Implemented"
    # }
    # for i in range(0, 50):
    #     try:
    #         matchpathcon("/var/lib/file.txt", i)
    #     except OSError as err:
    #         print(errors.get(err.errno, err))
    #
    #     print("\n")
    #
    # print("If you found some errors, please report them to Ansible GitHub Issues")

    rc, con = matchpathcon("/var/lib/file.txt", 0)  # NOQA



# Generated at 2022-06-13 00:04:41.331053
# Unit test for function matchpathcon
def test_matchpathcon():
    result = matchpathcon('/tmp/myfile', 0)
    assert result[0] == 0, 'RC is not zero'

    # NB: won't work for people that have a custom policy in use
    #     but since we're just testing that the right functions are
    #     called and we get back a string it can be whatever
    assert result[1] == 'var_tmp_t', 'Pathcon is not var_tmp_t'



# Generated at 2022-06-13 00:04:42.162702
# Unit test for function matchpathcon
def test_matchpathcon():
    assert matchpathcon(b'/', mode=0) == [0, 'system_u:object_r:file_t']

# Generated at 2022-06-13 00:04:48.322852
# Unit test for function matchpathcon
def test_matchpathcon():
    # check if SELinux is enabled
    if not is_selinux_enabled():
        print("SELinux is not enabled. Skipping selinux tests.")
        return

    con = c_char_p()

    if security_getenforce() == 1:
        enforce = "enforcing"
    else:
        enforce = "permissive"

    print("SELinux is enabled in %s. Continuing with selinux tests." % enforce)

    print("Checking the context of /." )
    rc, con = matchpathcon('/', 0)
    if rc == -1:
        print("matchpathcon for / returned -1")
        return -1
    print("The context of / is %s" % con.value)

    print("Checking the context of /dev/sdz1" )
    rc, con

# Generated at 2022-06-13 00:05:04.884125
# Unit test for function matchpathcon
def test_matchpathcon():
    (rc, con) = matchpathcon("/tmp/testdir/testfile", 0o755)
    if rc != 0:
        raise Exception("test_matchpathcon failed: Unable to match context for /tmp/testdir/testfile")

    (rc, con2) = lgetfilecon_raw("/tmp/testdir/testfile")
    if rc != 0:
        raise Exception("test_matchpathcon failed: Unable to get context for /tmp/testdir/testfile")

    if con != con2:
        raise Exception("test_matchpathcon failed: matchpathcon returned unexpected context: {0}".format(con))



# Generated at 2022-06-13 00:05:11.083790
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    from ctypes import c_char_p
    from errno import ENOENT

    fp = open("/tmp/ansible-test", "w+")
    fp.close()

    _test_path = "/tmp/ansible-test"
    try:
        rc, con = lgetfilecon_raw(_test_path)
        assert rc == 0
        assert type(con) == type(str())

        rc, con = lgetfilecon_raw("/tmp/ansible-test-noent")
        assert rc == -1
        assert get_errno() == ENOENT

    finally:
        os.remove("/tmp/ansible-test")



# Generated at 2022-06-13 00:05:14.286479
# Unit test for function matchpathcon
def test_matchpathcon():
    if is_selinux_enabled():
        check_result(matchpathcon('/var/log', 0), 0, 'system_u:object_r:var_log_t')

# Generated at 2022-06-13 00:05:19.406609
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import tempfile
    fd, path = tempfile.mkstemp()
    os.close(fd)
    os.unlink(path)
    assert lgetfilecon_raw(path) == [1, '(null)']

# Generated at 2022-06-13 00:05:24.405690
# Unit test for function matchpathcon
def test_matchpathcon():
    if is_selinux_enabled() and is_selinux_mls_enabled():
        (rc, ret) = matchpathcon('/tmp', 0)
        if rc == 0:
            assert ret == 'user_tmp_t', 'Failed to retrieve context for path'


if __name__ == '__main__':
    result = test_matchpathcon()
    if result:
        print(result)

    sys.exit(result)

# Generated at 2022-06-13 00:05:33.728833
# Unit test for function matchpathcon
def test_matchpathcon():
    import tempfile
    fd, fname = tempfile.mkstemp()
    try:
        rc, con = matchpathcon(fname, 0o0770)
        print("rc: %d" % rc)
        print("con: %s" % con)
    finally:
        os.close(fd)
        os.unlink(fname)


if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-13 00:05:41.678519
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # use /etc/ in the test with selinux enabled because it will always be set
    if not is_selinux_mls_enabled():
        raise RuntimeError('selinux not enabled for this system')
    if selinux_getenforcemode()[1] == 0:
        raise RuntimeError('selinux is disabled for this system')
    con = lgetfilecon_raw('/etc')
    assert con[0] == 0
    assert isinstance(con[1], str)
    assert len(con[1]) > 0
    assert isinstance(con[1][0], str)



# Generated at 2022-06-13 00:05:43.800295
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw('selinux_test.py')
    assert rc == 0



# Generated at 2022-06-13 00:05:51.305356
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Verify we can load the library and get a result
    (rc, con) = lgetfilecon_raw("/usr/bin/id")
    assert rc == 0
    assert con is not None
    assert con != ''

    # Verify that access to an invalid file returns an error
    (rc, con) = lgetfilecon_raw("/usr/bin/id/")
    assert rc != 0
    assert con is None

    # Verify that access to an invalid file returns an error
    (rc, con) = lgetfilecon_raw(None)
    assert rc != 0
    assert con is None



# Generated at 2022-06-13 00:05:53.988655
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, filecon = lgetfilecon_raw(b'/proc/meminfo')
    if rc < 0:
        raise Exception('{0}:{1}'.format(rc, filecon))



# Generated at 2022-06-13 00:06:20.280161
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import os

    # get current executable file context
    (rc, con) = lgetfilecon_raw(os.path.realpath(sys.argv[0]))

    assert isinstance(rc, int)
    assert isinstance(con, str)
    assert rc == 0



# Generated at 2022-06-13 00:06:24.152469
# Unit test for function matchpathcon
def test_matchpathcon():
    import tempfile
    path = tempfile.mktemp(prefix='test_selinux_')
    try:
        rc, mode = matchpathcon(path, 0)
        assert rc == 0
        assert not mode
        rc, mode = matchpathcon(path, 1)
        assert rc == 0
        assert mode
    finally:
        os.unlink(path)


if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-13 00:06:25.895093
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Use lgetfilecon_raw to get the SELinux context of the python executable
    file_context = lgetfilecon_raw(sys.executable)[1]
    assert file_context



# Generated at 2022-06-13 00:06:27.789364
# Unit test for function matchpathcon
def test_matchpathcon():
    print(matchpathcon('/etc/shadow', 0))
    print(matchpathcon('/etc/shadow', 1))
    print(matchpathcon('/etc/shadow', 2))
    print(matchpathcon('/etc/shadow', 3))



# Generated at 2022-06-13 00:06:34.887716
# Unit test for function matchpathcon
def test_matchpathcon():
    path = '/etc/resolv.conf'
    mode = 0
    [rc, con] = matchpathcon(path, mode)
    assert rc == 0, 'function returned bad rc'
    assert con == 'system_u:object_r:net_conf_t:s0', 'function returned bad con'



# Generated at 2022-06-13 00:06:44.168401
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = b'/tmp/testfile'

# Generated at 2022-06-13 00:06:47.019410
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    file_name = __file__
    _, context = lgetfilecon_raw(file_name)
    assert context, 'File path %s does not have a SELinux context' % ( file_name )

# Generated at 2022-06-13 00:06:52.692689
# Unit test for function matchpathcon
def test_matchpathcon():
    mode = os.path.stat('tmp').st_mode
    # we are checking if matchpathcon function is returning proper exit code - '0'
    # and proper context when executed with valid arguments
    assert matchpathcon('tmp', mode)[0] == 0
    assert 'user_u:object_r:tmp_t:s0' in matchpathcon('tmp', mode)[1]



# Generated at 2022-06-13 00:06:58.917727
# Unit test for function matchpathcon
def test_matchpathcon():
    path = 'my_path'
    mode = 2
    con = c_char_p(to_bytes('system_u:object_r:user_home_dir_t:s0'))
    try:
        _selinux_lib.matchpathcon.argtypes = [_to_char_p, c_int, POINTER(c_char_p)]
        rc = _selinux_lib.matchpathcon(path, mode, byref(con))
        print([rc, to_native(con.value)])
    finally:
        _selinux_lib.freecon(con)

# Generated at 2022-06-13 00:07:02.313255
# Unit test for function matchpathcon
def test_matchpathcon():
    # sanity test
    path = '/bin/sh'
    rc, con = matchpathcon(path, 0)
    assert rc == 0, 'unexpected rc: {0}: {1}'.format(rc, con)
    assert con == 'system_u:object_r:shell_exec_t:s0', 'unexpected context: {0}'.format(con)

# Generated at 2022-06-13 00:07:50.955767
# Unit test for function matchpathcon
def test_matchpathcon():
    import ansible.module_utils.basic  # noqa
    from ansible_collections.community.general.tests.unit.modules.utils import set_module_args
    from ansible_collections.community.general.tests.unit.modules.utils import AnsibleExitJson, AnsibleFailJson, ModuleTestCase
    from ansible_collections.community.general.plugins.modules.files import selinux

    set_module_args(dict(
        path='/var/tmp',
        context='unconfined_u:object_r:tmp_t:s0',
        state='present',
        debug=False
    ))

    with ModuleTestCase(selinux, pass_args=True, exit_json=True, fail_json=True) as case:
        case.runTest()

# Generated at 2022-06-13 00:07:53.386546
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw('/etc/passwd')
    assert rc == 0
    assert con == 'system_u:object_r:etc_t:s0'


# Generated at 2022-06-13 00:07:56.260176
# Unit test for function matchpathcon
def test_matchpathcon():
    try:
        is_selinux_enabled()
    except PermissionError:
        # Don't fail module if selinux is not enabled on this host
        pass

if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-13 00:08:00.331626
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw('/etc/selinux/config')
    if rc != 0:
        raise Exception('unable to retrieve context for /etc/selinux/config: {0}'.format(con))
    print('context for /etc/selinux/config: {0}'.format(con))



# Generated at 2022-06-13 00:08:07.020453
# Unit test for function matchpathcon
def test_matchpathcon():
    testpath = '/tmp/testpath'
    testfilename = '/tmp/testfilename'
    testfilecontent = 'hello world!'
    con = 'user_u:object_r:tmp_t:s0'

    with open(testpath, 'w') as testfile:
        rc, result = matchpathcon(testpath, 0)
        assert result == con

    with open(testfilename, 'w') as testfile:
        rc, result = matchpathcon(testfilename, 0)
        assert result == con

    with open(testfilename, 'w') as testfile:
        testfile.write(testfilecontent)
    rc, result = matchpathcon(testfilename, 0)
    assert result == con

    # cleanup
    os.remove(testpath)
    os.remove(testfilename)

# Generated at 2022-06-13 00:08:14.037017
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # simple test to get the selinux context of a file or directory
    path = '/tmp/test'
    rc, con = lgetfilecon_raw(path)
    if rc != 0:
        raise Exception('error getting context: {0}'.format(rc))

    if isinstance(con, list):
        con = con[0]

    print('{0}: context = {1}'.format(path, con))


if __name__ == '__main__':
    test_lgetfilecon_raw()

# Generated at 2022-06-13 00:08:18.134138
# Unit test for function matchpathcon
def test_matchpathcon():
    # Positive test case
    path = 'labeledpath'
    mode = os.R_OK
    rc, con = matchpathcon(path, mode)
    print(rc, con)

    # Negative test case. Call the function with invalid inputs
    path = ''
    mode = os.R_OK
    rc, con = matchpathcon(path, mode)
    print(rc, con)



# Generated at 2022-06-13 00:08:26.777521
# Unit test for function matchpathcon
def test_matchpathcon():
    import tempfile
    import selinux
    import os
    import os.path
    import re

    # Need to check if selinux is enabled
    if not selinux.is_selinux_enabled():
        print("selinux is disabled")
        return

    # /tmp is labeled tmpfs_t
    # Need to create a file, get the context and then delete it
    # This is because matchpathcon is deprecated and should be replaced with selabel_lookup
    def test_matchpathcon_file(path):
        f = tempfile.NamedTemporaryFile(dir=path, delete=False)
        os.close(f.fileno())
        context = selinux.matchpathcon(f.name, 0)[1]
        os.unlink(f.name)
        return context

    # Get the context of /tmp


# Generated at 2022-06-13 00:08:35.572768
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import tempfile
    with tempfile.TemporaryDirectory() as tmpdir:
        path = tmpdir + '/test_file'
        with open(path, 'w') as out:
            out.write('data')
        (rc, context) = lgetfilecon_raw(path)
        assert rc == 0
        assert context
        values = context.split(':')
        assert len(values) == 6
        assert values[0] == 'system_u'
        assert values[1] == 'object_r'
        assert values[2] == 'tmp_t'
        assert values[3] == 's0'
        assert values[4] == '' # expected context range
        assert values[5] == 'unconfined_u:object_r:tmp_t:s0' # default type

# Generated at 2022-06-13 00:08:42.924380
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = '/etc/selinux/config'
    # Test for the function lgetfilecon_raw
    try:
        # Test if the function lgetfilecon_raw exists
        assert hasattr(selinux_utils, 'lgetfilecon_raw')
        assert callable(getattr(selinux_utils, 'lgetfilecon_raw'))

        # Test if the function lgetfilecon_raw has the right number of arguments
        assert len(getfullargspec(getattr(selinux_utils, 'lgetfilecon_raw'))) == 2
    except:
        print("Unit test for function lgetfilecon_raw failed")
        raise

    # Test for the argument path
    try:
        # Test if string path has the right type
        assert isinstance(path, str)
    except:
        print