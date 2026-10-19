

# Generated at 2022-06-12 23:59:21.858211
# Unit test for function matchpathcon
def test_matchpathcon():
    def runtest(testcase):
        if opts['verbose']:
            print("Testing matchpathcon with mode %s" % testcase['mode'])
        rc, res = matchpathcon(testcase['path'], testcase['mode'])
        if rc != 0:
            print("Failed to match path %s: %s" % (testcase['path'], res))
            return False
        if testcase.get('expect_error', False):
            print("Expected failure for path %s, but did not get an error" % testcase['path'])
            return False
        if not res.startswith(testcase['expected_match']):
            print("Expected %s to start with %s but it does not" % (res, testcase['expected_match']))
            return False

# Generated at 2022-06-12 23:59:28.656730
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    file_list = ['/etc/passwd', '/etc/group', '/etc/shadow', '/etc/gshadow']
    test_file = file_list[1]
    if os.path.exists(test_file):
        [rc, con] = lgetfilecon_raw(test_file)

        if rc == -1:
            print("Error: " + strerror(get_errno()) + ".")
        else:
            print("Context of " + test_file + " is " + con + ".")



# Generated at 2022-06-12 23:59:32.743158
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert os.path.exists('/etc/passwd')
    (rc, value) = lgetfilecon_raw(to_bytes('/etc/passwd', errors='surrogate_or_strict'))
    assert value is not None
    assert rc == 0

# Generated at 2022-06-12 23:59:37.207973
# Unit test for function matchpathcon
def test_matchpathcon():
    import os
    import sys
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils import basic
    results = matchpathcon(basic.SYSTEM_PATH, os.R_OK)
    assert results[0] in (0, -1)
    assert isinstance(results[1], basestring)


# Unit test function selinux_getenforcemode

# Generated at 2022-06-12 23:59:42.480856
# Unit test for function matchpathcon
def test_matchpathcon():
    path = '/etc/mtab'
    (rc, con) = matchpathcon(path, 0)
    if rc == 0:
        print(con)
    else:
        print("{0} {1}".format(rc, con))


if __name__ == "__main__":
    test_matchpathcon()

# Generated at 2022-06-12 23:59:49.306617
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    def_con = "system_u:object_r:usr_t:s0"
    test_file = "/tmp/test_file"
    f = open(test_file, "w")
    f.close()
    # Test non existant file
    assert lgetfilecon_raw("/tmp/blah") == [-1, b'NIL']
    # Test existant file
    assert lgetfilecon_raw(test_file) == [0, def_con.encode()]
    os.remove(test_file)

# Generated at 2022-06-12 23:59:55.377093
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (rc, con) = lgetfilecon_raw("/test_directory")
    if rc == 0:
        print('Executed Successfully lgetfilecon_raw on directory')
    else:
        print('Not able to execute lgetfilecon_raw due to error')
        print('Error is: %s' % con)

    (rc, con) = lgetfilecon_raw("/test_file")
    if rc == 0:
        print('Executed Successfully lgetfilecon_raw on file')
    else:
        print('Not able to execute lgetfilecon_raw due to error')
        print('Error is: %s' % con)



# Generated at 2022-06-13 00:00:05.093809
# Unit test for function matchpathcon
def test_matchpathcon():
    # Using file /usr/bin/id as an example
    (rc, con) = selinux_getenforcemode()
    if rc == -1:
        print('Error invoking selinux_getenforcemode:')
        print('errno: {}'.format(get_errno()))
        print('strerror: {}'.format(os.strerror(get_errno())))
        print('Con: {}'.format(con))
        return False

    if con == 1:
        print('Enforcing is enabled (selinux_getenforcemode returned {})'.format(con))
        (rc, policy) = selinux_getpolicytype()
        if rc == -1:
            print('Error invoking selinux_getpolicytype:')
            print('errno: {}'.format(get_errno()))

# Generated at 2022-06-13 00:00:08.750788
# Unit test for function matchpathcon
def test_matchpathcon():

    testPath = '/tmp/testFile'

    # Create test file
    f = open(testPath, 'w')
    f.close()

    # Remove test file
    os.remove(testPath)


if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-13 00:00:10.968158
# Unit test for function matchpathcon
def test_matchpathcon():
    assert [0, 'system_u:object_r:root_t:s0'] == matchpathcon('/', 0)



# Generated at 2022-06-13 00:00:16.235631
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():

    # Since lgetfilecon_raw is working correctly, the following module should run without error
    result = lgetfilecon_raw("/root")

    if result[0] != 0:
        raise Exception("lgetfilecon_raw() failed")

# Generated at 2022-06-13 00:00:20.606502
# Unit test for function matchpathcon
def test_matchpathcon():
    import tempfile
    tmp_dir_path = tempfile.mkdtemp()
    con = None
    try:
        (_, con) = matchpathcon(tmp_dir_path, os.R_OK)
    finally:
        os.rmdir(tmp_dir_path)
    if not con:
        raise Exception("matchpathcon returned empty context")



# Generated at 2022-06-13 00:00:27.801674
# Unit test for function matchpathcon
def test_matchpathcon():
    expected_results = [
        [0, 'system_u:object_r:initrc_exec_t:s0'],
        [0, 'system_u:object_r:initrc_tmp_t:s0'],
        [0, 'system_u:object_r:rc_tmp_t:s0']]
    for test_path, expected in zip(['/sbin/init', '/etc/init.d/var', '/sbin/reboot'], expected_results):
        results = matchpathcon(test_path, 0)
        assert results == expected

# Generated at 2022-06-13 00:00:33.259439
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = '/root'
    res = lgetfilecon_raw(path)
    assert res[0] == 0
    assert res[1].startswith('unconfined_u:object_r:root_t')

# Generated at 2022-06-13 00:00:37.160753
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = '/etc/passwd'
    rc, con = lgetfilecon_raw(path)
    assert rc == 0
    assert con == "system_u:object_r:etc_runtime_t:s0"



# Generated at 2022-06-13 00:00:39.668211
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon("/home", 0)
    assert rc >= 0
    assert con == "user_home_dir_t"


# Generated at 2022-06-13 00:00:41.721341
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    testpath = '/etc/group'
    rc, con = lgetfilecon_raw(testpath)
    assert rc == 0
    assert con == 'system_u:object_r:group_data_t:s0'



# Generated at 2022-06-13 00:00:43.787578
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon('/var/log', 7)
    assert rc == 0
    assert con == 'system_u:object_r:var_log_t'



# Generated at 2022-06-13 00:00:53.629081
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon('ow_dir_x/file_x', os.R_OK)
    print('{0} {1}'.format(rc, con))
    rc, con = matchpathcon('ow_dir_x', os.R_OK)
    print('{0} {1}'.format(rc, con))
    rc, con = matchpathcon('ow_dir_x/file_x', os.W_OK)
    print('{0} {1}'.format(rc, con))
    rc, con = matchpathcon('ow_dir_x/file_x', os.X_OK)
    print('{0} {1}'.format(rc, con))


# Generated at 2022-06-13 00:01:00.954488
# Unit test for function matchpathcon
def test_matchpathcon():
    if not os.path.exists('/etc/localtime'):
        print("SELinux does not exist, skip this test")
        return
    # test for /etc/localtime
    [rc, con] = matchpathcon('/etc/localtime', 0)
    assert rc == 0
    assert con == 'system_u:object_r:timezone_home_t:s0'

    # test for nonexisting file
    [rc, con] = matchpathcon('/etc/localtime1', 0)
    assert rc != 0
    assert con == ''

if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-13 00:01:07.532613
# Unit test for function matchpathcon
def test_matchpathcon():
    assert _selinux_lib.matchpathcon('/etc/passwd', 1)[0] == 0
    assert _selinux_lib.matchpathcon('/foo/bar/baz', 1)[0] == -1
    assert _selinux_lib.matchpathcon('/etc/passwd', -1)[0] == -1
    assert _selinux_lib.matchpathcon('/etc/passwd', 0)[0] == 0



# Generated at 2022-06-13 00:01:11.377100
# Unit test for function matchpathcon
def test_matchpathcon():
    """
    This unit test verifies the matchpathcon function in module_utils.selinux using the /etc/hosts file.
    The matchpathcon function calls matchpathcon_raw from the libselinux.so library to return the
    SELinux context of the file. If the context is returned OK, the unit test passes.

    :return:
    """
    rc_status, selinux_context = matchpathcon('/etc/hosts', 0)
    assert rc_status == 0
    assert selinux_context == 'system_u:object_r:etc_runtime_t:s0'

# Generated at 2022-06-13 00:01:13.393950
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (rc, con) = lgetfilecon_raw('/')
    assert rc == 0
    assert con != None


# Generated at 2022-06-13 00:01:16.024099
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    ret = lgetfilecon_raw(b'/')
    if ret[0] == -1:
        raise OSError(ret[0], os.strerror(ret[0]))
    print(ret[1])



# Generated at 2022-06-13 00:01:22.001678
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Load mock library
    my_lib = CDLL('test_libselinux.so')
    # Attach function to ctypes
    f = my_lib.lgetfilecon_raw
    f.argtypes = [c_char_p, POINTER(c_char_p)]
    f.restype = c_int

    class mock_selinux_lib:
        class lgetfilecon_raw:
            @staticmethod
            def __get__(*args):
                return f

    _selinux_lib.lgetfilecon_raw = mock_selinux_lib.lgetfilecon_raw

    # Function to test
    rc, con = lgetfilecon_raw('/tmp/test')
    assert con == 'system_u:object_r:tmp_t:s0'
    assert rc == 0

# Generated at 2022-06-13 00:01:33.347283
# Unit test for function matchpathcon
def test_matchpathcon():
    import os
    import os.path
    sys_policy_dir = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', '..', 'policy')
    ret, con = selinux_getpolicytype()
    if ret != 0:
        print('[failed] selinux_getpolicytype')
        sys.exit(1)

    path = os.path.join(sys_policy_dir, con, 'policy')
    if not os.path.exists(path):
        print('[failed] {path} does not exist'.format(**locals()))
        sys.exit(1)

    mode = 0
    ret, con = matchpathcon(path, mode)
    if ret != 0:
        print('[failed] matchpathcon')
        sys.exit

# Generated at 2022-06-13 00:01:37.234521
# Unit test for function matchpathcon
def test_matchpathcon():
    """
    test_matchpathcon:
    """
    if os.geteuid() == 0:
        res = matchpathcon("/var/log/audit/audit.log", os.R_OK)
        if res[0] == 0:
            print("secon={0}".format(res[1]))
        else:
            print("error getting security context: {0}".format(res[0]))
    else:
        print("Need root to run this test")


# Generated at 2022-06-13 00:01:41.953639
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Test to check if the given file path is valid or not
    if os.path.exists('/etc/passwd'):
        if os.path.isfile('/etc/passwd'):
            rc, con = lgetfilecon_raw('/etc/passwd')
            assert(rc == 0)
            assert(con)
        else:
            print('file does not exist')
    else:
        print('file does not exist')



# Generated at 2022-06-13 00:01:46.497672
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    test_path = '/tmp/'
    expected_con = 'system_u:object_r:tmp_t:s0'
    [rc, con] = lgetfilecon_raw(test_path)
    assert rc == 0
    assert con == expected_con

# Generated at 2022-06-13 00:01:49.155784
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = "/tmp"
    rc, result = lgetfilecon_raw(path)
    assert isinstance(result, str) is True
    assert isinstance(rc, int) is True


# Generated at 2022-06-13 00:02:02.815754
# Unit test for function matchpathcon
def test_matchpathcon():
    currentpath = os.getcwd()
    state = selinux_getenforcemode()
    if state[1] != 1:
        rc = matchpathcon(currentpath, 0)[0]
        if selinux_getpolicytype()[1] == 'targeted':
            assert rc == 0
        else:
            assert rc == -1
    else:
        rc = matchpathcon(currentpath, 0)[0]
        if selinux_getpolicytype()[1] == 'targeted':
            assert rc == -1
        else:
            assert rc == 0


# Generated at 2022-06-13 00:02:10.980306
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    """
    Get the SELinux security context from a file, in raw form.
    Returns:
    Type: list
    Sample:
    [0, 'u:object_r:unlabeled_t:s0']
    Description:
    [
        0,
        'u:object_r:unlabeled_t:s0'
    ]
    """
    return lgetfilecon_raw(b'/etc/selinux')

# Generated at 2022-06-13 00:02:17.051264
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Test for normal output
    try:
        [rc, con] = lgetfilecon_raw('selinux_facts.py')
    except Exception as e:
        raise AssertionError(e)
    else:
        if rc > 0 or con == "":
            raise AssertionError("Output is empty or error")

    # Test for file without context
    try:
        [rc, con] = lgetfilecon_raw('does_not_exist')
    except Exception as e:
        raise AssertionError(e)
    else:
        if rc != 0 or con != None:
            raise AssertionError("Output is not empty or error")


# Generated at 2022-06-13 00:02:24.034809
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    lgetfilecon_raw_output = lgetfilecon_raw(path="test_file")
    assert lgetfilecon_raw_output[0] == 0, "The return value was not a success"
    assert lgetfilecon_raw_output[1] == 'system_u:object_r:tmp_t:s0', "The return context was not what was expected"

# Generated at 2022-06-13 00:02:28.876566
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    test_path = "/etc/mtab"
    rc, con = lgetfilecon_raw(test_path)
    print("rc = {0} ; con = {1}".format(rc, con))
    assert rc == 0, "lgetfilecon_raw failed"


# Generated at 2022-06-13 00:02:32.736700
# Unit test for function matchpathcon
def test_matchpathcon():
    path = b'/var/log/syslog'
    mode = os.R_OK
    rc, con = matchpathcon(path, mode)
    assert rc == 0
    assert con == 'system_u:object_r:var_log_t:s0'

# Generated at 2022-06-13 00:02:37.075177
# Unit test for function matchpathcon
def test_matchpathcon():
    import subprocess

    [rc, con] = matchpathcon('/etc/selinux/plans/develop/etc/hosts', 0)
    print('Return code: %d Con: %s' % (rc, con))

if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-13 00:02:45.770607
# Unit test for function matchpathcon
def test_matchpathcon():
    def check_matchpathcon(path, mode, expect_rc, expect_result):
        rc, result = matchpathcon(path, mode)
        assert rc == expect_rc, 'wrong return code.  Expected {0}, got {1}'.format(expect_rc, rc)
        assert result == expect_result, 'Wron result {0}, expected {1}'.format(result, expect_result)

    check_matchpathcon('/etc/bin/foo/bar', 0, -1, '')
    check_matchpathcon('/etc/bin/foo', 0, -1, '')
    check_matchpathcon('/etc/bin', 0, 0, 'system_u:object_r:bin_t:s0')

# Generated at 2022-06-13 00:02:57.649410
# Unit test for function matchpathcon
def test_matchpathcon():
    import json
    import pytest

    path = '/tmp/test'
    test_mode = os.stat(path)[0]

    rc, con = matchpathcon(path, test_mode)

    # rc should be 0, indicating success, and con should be the context
    if rc == 0:
        assert con == 'system_u:object_r:tmp_t:s0'
    else:
        pytest.fail('Failed to retrieve context')

    # test with invalid path
    path = '/inexistent'
    test_mode = os.stat(path)[0]

    rc, con = matchpathcon(path, test_mode)

    # rc should be -1, indicating failure to retrieve context
    if rc == -1:
        assert con == ''
    else:
        pytest.fail('This should have failed')

# Generated at 2022-06-13 00:03:05.345974
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (rc, con) = lgetfilecon_raw('/etc/passwd')
    print('Path: /etc/passwd')
    print('RC: %d, Context: %s' % (rc, con))
    (rc, con) = lgetfilecon_raw('/etc/group')
    print('Path: /etc/group')
    print('RC: %d, Context: %s' % (rc, con))
    (rc, con) = lgetfilecon_raw('/etc/shadow')
    print('Path: /etc/shadow')
    print('RC: %d, Context: %s' % (rc, con))

