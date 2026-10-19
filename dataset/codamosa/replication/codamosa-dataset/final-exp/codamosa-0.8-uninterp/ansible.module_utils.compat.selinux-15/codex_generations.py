

# Generated at 2022-06-12 23:59:14.162645
# Unit test for function matchpathcon
def test_matchpathcon():
    from ansible.module_utils.selinux import lgetfilecon_raw
    from ansible.module_utils.selinux import matchpathcon
    import os
    import stat

    # Create a file and get its context
    file_name = "/tmp/flask_test_file"
    with open(file_name, "w") as f:
        f.write("Test")

    file_context = lgetfilecon_raw(file_name)[1]

    # Create a directory and get its context
    dir_name = "/tmp/flask_test_dir"
    os.mkdir(dir_name)

    dir_context = lgetfilecon_raw(dir_name)[1]

    # Create a link and get its context
    link_name = "/tmp/flask_test_link"
    os.sy

# Generated at 2022-06-12 23:59:17.740658
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import os
    (rc, con) = lgetfilecon_raw(os.path.realpath(__file__))
    assert rc == 0
    assert type(con) == str

# Generated at 2022-06-12 23:59:27.751405
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import os.path
    import ansible.utils.path
    from ansible.module_utils.basic import AnsibleModule

    _test_func_name = 'lgetfilecon_raw'
    _test_func = getattr(ansible.module_utils.selinux_functions, _test_func_name)

    _test_files = []
    _test_files.append(os.path.join(ansible.utils.path.get_bin_dir(), 'ansible-connection'))
    _test_files.append(os.path.join(ansible.utils.path.get_bin_dir(), 'ansible-doc'))
    _test_files.append(os.path.join(ansible.utils.path.get_bin_dir(), 'ansible-galaxy'))
    _test_files.append

# Generated at 2022-06-12 23:59:29.518182
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = b'/tmp'
    out = lgetfilecon_raw(path)
    assert out[0] != -1

# Generated at 2022-06-12 23:59:33.794042
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    con = lgetfilecon_raw(b'/etc/hosts')
    assert con[0] == 0
    assert con[1] == 'system_u:object_r:etc_t:s0'
    assert con == lgetfilecon_raw('/etc/hosts')



# Generated at 2022-06-12 23:59:38.455385
# Unit test for function matchpathcon
def test_matchpathcon():
    test_path = '/tmp/sample.txt'
    if os.path.exists(test_path):
        print('Test file already exists: {0}'.format(test_path))
    else:
        open(test_path, 'a').close()
        result = matchpathcon(test_path, 0)
        if isinstance(result, int):
            print('Success')
        else:
            print('Failed')
        os.remove(test_path)



# Generated at 2022-06-12 23:59:49.389332
# Unit test for function matchpathcon
def test_matchpathcon():
    """
    matchpathcon - path, mode
    Function to test matchpathcon

    Check return code from matchpathcon
    If rc is not zero, then there was an issue when calling the function
    If rc is not equal to expected_rc, then test failed
    If rc is equal to expected_rc and con is equal to expected_con, test passed
    """

    path = '/bin/bash'
    mode = 32768
    expected_rc = 0
    # NB: this is done in a separate function because of the extra freecon code
    func_rc, func_con = matchpathcon(path, mode)
    test_rc = func_rc == expected_rc
    if not test_rc:
        return [test_rc, 'expected_rc', expected_rc, 'func_rc', func_rc]

# Generated at 2022-06-12 23:59:56.515265
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = selinux_getenforcemode()
    assert rc >= 0
    assert con >= 0

    rc, policy_type = selinux_getpolicytype()
    assert rc == 0
    assert policy_type

    rc, file_con = lgetfilecon_raw('/etc/passwd')
    assert rc >= 0
    assert file_con

    rc, con = matchpathcon('/etc/passwd', 0)
    assert rc == 0
    assert con == file_con

# Generated at 2022-06-12 23:59:59.192372
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw(b'/etc/passwd') == [0, 'system_u:object_r:etc_runtime_t']


# Generated at 2022-06-13 00:00:05.740241
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    """
    Test the wrapper function lgetfilecon_raw().
    """
    _, fname = tempfile.mkstemp()
    con = 'unconfined_u:object_r:file_t:s0'

    try:
        _selinux_lib.lsetfilecon(fname, con)
        rc, file_con = lgetfilecon_raw(fname)

        assert rc == 0
        assert con == file_con
    finally:
        _selinux_lib.freecon(con)
        os.remove(fname)


# Generated at 2022-06-13 00:00:19.224633
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    """
    lgetfilecon_raw(3) selinux lib call
    """
    def check_lgetfilecon_raw(path):
        con = c_char_p()
        try:
            rc = _selinux_lib.lgetfilecon_raw(path, byref(con))
            if rc < 0:
                errno = get_errno()
                raise OSError(errno, os.strerror(errno))
            return [rc, to_native(con.value)]
        finally:
            _selinux_lib.freecon(con)

    def test_lgetfilecon_raw_success(path):
        """
        unit function to test lgetfilecon_raw(3) success
        """
        (rc, con) = check_lgetfilecon_raw(path)

# Generated at 2022-06-13 00:00:23.727899
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw('/etc/passwd')
    print('lgetfilecon_raw({0}) => {1}, {2}'.format('/etc/passwd', rc, con))
    assert rc == 0
    assert con == 'system_u:object_r:etc_runtime_t:s0'


# Generated at 2022-06-13 00:00:26.690506
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = '/etc/selinux/config'
    rc, result = lgetfilecon_raw(path)
    assert rc == 0
    assert result == 'system_u:object_r:etc_runtime_t:s0'

# Generated at 2022-06-13 00:00:38.602570
# Unit test for function matchpathcon
def test_matchpathcon():
    # prepare
    assert is_selinux_enabled() == 1

    # test files in /home
    assert matchpathcon('/home/someuser/testfile', 0) == [0, 'user_home_t']
    assert matchpathcon('/home/someuser/somefile', os.R_OK) == [0, 'user_home_t']
    assert matchpathcon('/home/someuser/somefile', os.W_OK) == [0, 'user_home_t']
    assert matchpathcon('/home/someuser/somefile', os.X_OK) == [0, 'system_u:object_r:user_home_t:s0']

    # test files in /home with mode None

# Generated at 2022-06-13 00:00:44.624750
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import os

    # Find a file that exists and has an SELinux context
    home = os.getenv('HOME')
    if home is None:
        home = os.path.expanduser('~')

    path = '{0}/.bashrc'.format(home)
    if not os.path.isfile(path) or not os.path.exists(path):
        raise RuntimeError('unable to find a test file')

    # Run the test
    con = lgetfilecon_raw(path)[1]
    print('SELinux context of {0} is: {1}'.format(path, con))



# Generated at 2022-06-13 00:00:48.030283
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    result, con = lgetfilecon_raw("/etc/passwd")
    if result < 0:
        raise OSError("Failed to get con")
    print("con is: ", con)



# Generated at 2022-06-13 00:00:50.772890
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, path = matchpathcon("/tmp", 0)
    print("rc = {0}, path = {1}".format(rc, path))


# Generated at 2022-06-13 00:00:55.008012
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = b'/tmp/test'
    f = open(path, "w")
    f.close()
    assert lgetfilecon_raw(path)[1] == 'system_u:object_r:tmp_t:s0'

# Generated at 2022-06-13 00:01:00.040590
# Unit test for function matchpathcon
def test_matchpathcon():
    from ansible.module_utils.common._collections_compat import UserDict
    context = UserDict()
    retval, context['matchpathcon_result'] = matchpathcon(b'/tmp', 0)
    assert retval == 0, 'matchpathcon failed with return value {0}'.format(retval)
    assert context['matchpathcon_result'], 'matchpathcon failed to return a value'



# Generated at 2022-06-13 00:01:10.764794
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # pylint: disable=redefined-outer-name
    try:
        import selinux
        def _lgetfilecon(path):
            rc, context = selinux.lgetfilecon(path)
            if rc != 0:
                raise OSError(rc)
            return context

        orig_context = _lgetfilecon('/')
        assert orig_context
        assert lgetfilecon_raw('/') == [0, orig_context]

        _selinux_lib.lsetfilecon('/', orig_context)
        assert lgetfilecon_raw('/') == [0, orig_context]
    except ImportError:
        from nose2.tools import lorem_ipsum_generator

# Generated at 2022-06-13 00:01:18.183969
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw('/etc/passwd')
    assert rc == 0
    assert isinstance(con, str)
    assert con != ''



# Generated at 2022-06-13 00:01:21.168795
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (rc, value) = lgetfilecon_raw('/etc/passwd')
    assert rc == 0
    assert isinstance(value, str)
    assert value.startswith('system_u:object_r:')


# Generated at 2022-06-13 00:01:23.010328
# Unit test for function matchpathcon
def test_matchpathcon():
    assert matchpathcon('/var/log/messages', 0) == [0, 'system_u:object_r:var_log_t:s0']

# Generated at 2022-06-13 00:01:27.393549
# Unit test for function matchpathcon
def test_matchpathcon():
    res = matchpathcon('/sys/kernel/security/apparmor/features', 0)
    assert len(res) == 2
    assert res[0] == 0
    assert res[1] == u'system_u:object_r:apparmor_db_t:s0'

# Generated at 2022-06-13 00:01:32.368276
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, msg = matchpathcon('/tmp/foo.txt', 0)
    if rc != 0:
        return msg
    rc, msg = matchpathcon('/tmp/foo.txt', 1)
    if rc != 0:
        return msg
    return "hw"


if __name__ == '__main__':
    print(test_matchpathcon())

# Generated at 2022-06-13 00:01:39.533872
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw('/usr/bin/python') == [0, 'unconfined_u:object_r:usr_t:s0']
    assert lgetfilecon_raw('/usr') == [0, 'unconfined_u:object_r:usr_t:s0']
    assert lgetfilecon_raw('/') == [0, 'system_u:object_r:root_t:s0']
    assert lgetfilecon_raw('/usr/bin/this/dont/exist') == [-2, 'unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023']
    assert lgetfilecon_raw(None) == [0, 'system_u:object_r:unlabeled_t:s0']



# Generated at 2022-06-13 00:01:48.924960
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    from ansible.module_utils.selinux_policycap import policycaps_to_list
    from ansible.module_utils.selinux import matchpathcon_pattern, lgetfilecon_raw, selinux_getpolicytype, SELINUX_POLICY_VERSIONS, SELINUX_STATE_ENFORCING, SELINUX_STATE_PERMISSIVE, SELINUX_STATE_DISABLED
    from ansible.module_utils.six.moves import map

    if lgetfilecon_raw("/")[0] == -1:
        exit("This test is designed to be run on an selinux enabled system!")

    rc, con = lgetfilecon_raw("/")
    assert not rc, "I was unable to get the context of '/'!"

    rc, policytype = selinux_

# Generated at 2022-06-13 00:01:51.413551
# Unit test for function matchpathcon
def test_matchpathcon():
    # This function returns an empty string if no context is available
    file_context = matchpathcon('/tmp', 0)[1]
    assert file_context == ''

if __name__ == "__main__":
    test_matchpathcon()

# Generated at 2022-06-13 00:01:56.822773
# Unit test for function matchpathcon
def test_matchpathcon():
    '''Unit test for function matchpathcon'''
    assert matchpathcon(b'/sys', 0) == [0, b'system_u:object_r:sysfs_t:s0']
    assert matchpathcon(b'/sys/devices/system/cpu', 0) == [0, b'system_u:object_r:sysfs_t:s0']
    assert matchpathcon(b'/usr/lib', 0) == [0, b'system_u:object_r:usr_t:s0']
    assert matchpathcon(b'/usr/lib/testfile', 0) == [0, b'system_u:object_r:usr_t:s0']

# Generated at 2022-06-13 00:02:01.087918
# Unit test for function matchpathcon
def test_matchpathcon():
    path = b"/etc/passwd"
    mode = c_int(0)
    con = c_char_p()
    rc = _selinux_lib.matchpathcon(path, mode, byref(con))
    assert rc == -1
    assert con.value == b'(null)'


# Generated at 2022-06-13 00:02:12.967351
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # File name
    file_name = "/usr/bin/perl"
    # Call the function
    ret, con = lgetfilecon_raw(file_name)
    # Returned value should be 0
    assert ret == 0
    # Context should be unconfined_u:object_r:bin_t:s0
    assert con == "unconfined_u:object_r:bin_t:s0"


# Generated at 2022-06-13 00:02:19.297730
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    if os.geteuid() == 0:
        import getpass

        rc, con = lgetfilecon_raw('/')
        if rc:
            print('con: %s' % con)
            print('user: %s' % getpass.getuser())

        rc, con = lgetfilecon_raw('/home')
        if rc:
            print('con: %s' % con)
            print('user: %s' % getpass.getuser())



# Generated at 2022-06-13 00:02:26.231581
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():

    path = os.path.join(os.sep, 'selinux')
    rc, con = lgetfilecon_raw(path)

    if rc < 0:
        raise OSError('unable to get selinux context for path {0}'.format(path))

    assert(con == 'selinux_file_t:system_u:object_r:selinuxfs:s0')



# Generated at 2022-06-13 00:02:35.373311
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import os
    import os.path
    import sys
    import tempfile
    import unittest

    class SELinuxTestCase(unittest.TestCase):
        def setUp(self):
            self.tmpdir = tempfile.mkdtemp()
            self.path = os.path.join(self.tmpdir, 'testfile')
            with open(self.path, 'w') as f:
                f.write('Hello')

        def tearDown(self):
            os.unlink(self.path)
            os.rmdir(self.tmpdir)

        def test_lgetfilecon_raw(self):
            mycon = _selinux_lib.lgetfilecon_raw(self.path)

# Generated at 2022-06-13 00:02:44.524992
# Unit test for function matchpathcon
def test_matchpathcon():
    """Tests using file_tests/selinux_test.py"""
    import json
    import shlex
    import subprocess

    TESTDIR = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(TESTDIR, 'file_tests')

    test_file = os.path.join(path, 'selinux_test.py')
    cmd = 'ANSIBLE_LIBRARY={0} ansible localhost -m {1} -e @{2}'.format(path, test_file, os.path.join(path, 'selinux_test_vars.json'))
    p = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Generated at 2022-06-13 00:02:45.580554
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    print(lgetfilecon_raw(b'/tmp'))


# Generated at 2022-06-13 00:02:48.215523
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    context = lgetfilecon_raw('/tmp/')
    assert context[0] == 0
    print('Passed: lgetfilecon_raw')


# Generated at 2022-06-13 00:03:00.071426
# Unit test for function matchpathcon

# Generated at 2022-06-13 00:03:05.582143
# Unit test for function matchpathcon
def test_matchpathcon():
    """
    Test _selinux_lib.matchpathcon.

    When there is no policy loaded, this test will fail with the following
    error:
    _selinux_lib.matchpathcon(b'/tmp', 0, byref(con))
    OSError: [Errno 2] Function not implemented
    """
    rc, con = matchpathcon(b'/tmp', 0)
    print(rc, con)
    assert rc == -1

# Generated at 2022-06-13 00:03:10.426973
# Unit test for function matchpathcon
def test_matchpathcon():
    results = matchpathcon('/var/folders/yj/06yfpjd569z26h_tdf1dzp5r0000gn/T/tmp8e7tby5a', 0)
    print('Return code: {0}'.format(results[0]))
    print('Context: {0}'.format(results[1]))



# Generated at 2022-06-13 00:03:24.030602
# Unit test for function matchpathcon
def test_matchpathcon():
    import tempfile
    import os
    import logging

    logger = logging.getLogger()

    success = False

    with tempfile.TemporaryDirectory() as tmppath:
        testpath = os.path.join(tmppath, 'selinux-matchpathcon.txt')

        with open(testpath, 'w') as f:
            f.write('foo')

        ret, con = matchpathcon(testpath, os.R_OK)

        if ret == 0:
            if con == 'system_u:object_r:usr_t:s0':
                success = True
                logger.info('Test passed')
            else:
                logger.error('matchpathcon for a file should return \'system_u:object_r:usr_t:s0\'. Got: %s', con)

        os.remove

# Generated at 2022-06-13 00:03:26.853139
# Unit test for function matchpathcon
def test_matchpathcon():
    ret = matchpathcon('/selinux/null', 0)
    assert ret == [0, 'system_u:object_r:selinuxfs:s0']

# Generated at 2022-06-13 00:03:34.334507
# Unit test for function matchpathcon
def test_matchpathcon():
    # Check if the selinux library is available
    if _selinux_lib:
        print("matchpathcon: %s" % matchpathcon("/etc/services", 0))
    print("matchpathcon: %s" % matchpathcon("/etc/services", 0o600))
    print("matchpathcon: %s" % matchpathcon("/etc/services", 0o601))
    print("matchpathcon: %s" % matchpathcon("/etc/services", 0o611))
    print("matchpathcon: %s" % matchpathcon("/etc/services", 0o621))
    print("matchpathcon: %s" % matchpathcon("/etc/services", 0o622))
    print("matchpathcon: %s" % matchpathcon("/etc/services", 0o633))
   

# Generated at 2022-06-13 00:03:42.466256
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = b'/tmp/somefile'
    con = c_char_p(b'user_u:object_r:user_tmp_t:s0')
    try:
        rc = _selinux_lib.lsetfilecon(path, con)
        assert rc == 0
        rc, gotten_con = lgetfilecon_raw(path)
        assert gotten_con == 'user_u:object_r:user_tmp_t:s0'
    finally:
        os.remove(path)



# Generated at 2022-06-13 00:03:46.408393
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import tempfile

    fd, path = tempfile.mkstemp()
    os.close(fd)
    try:
        rc, con = lgetfilecon_raw(path)
        assert con == 'unconfined_u:object_r:user_tmp_t:s0'
        assert rc == 0
    finally:
        os.remove(path)

# Generated at 2022-06-13 00:03:48.924400
# Unit test for function matchpathcon
def test_matchpathcon():
    current_dir = os.getcwd()
    [rc, fcontext] = matchpathcon(current_dir, 0)
    assert rc >= 0, 'unable to match current directory context'
    assert fcontext, 'unable to match current directory context'



# Generated at 2022-06-13 00:03:53.020844
# Unit test for function matchpathcon
def test_matchpathcon():
    def _run(path, mode, target_rc, target_con):
        rc, con = matchpathcon(path, mode)
        assert rc == target_rc, 'invalid rc: {0} != {1}'.format(rc, target_rc)
        assert con == target_con, 'invalid context: {0} != {1}'.format(con, target_con)

    _run('/', 0, 0, 'system_u:object_r:usr_t:s0')
    _run('/', 1, 0, 'system_u:object_r:usr_t:s0')

# Generated at 2022-06-13 00:03:56.207921
# Unit test for function matchpathcon
def test_matchpathcon():
    try:
        import selinux
        rc, context = matchpathcon(b'/etc', 0)
        assert rc == 0
        assert context == selinux.matchpathcon(b'/etc', 0)[1]
    except ImportError:
        pass

# Generated at 2022-06-13 00:03:59.508188
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = '/etc/redhat-release'
    rc, con = lgetfilecon_raw(path)
    assert rc == 0 and con is not None
    rc, con = lgetfilecon_raw('somefilethatdoesntexist')
    assert rc == -1



# Generated at 2022-06-13 00:04:08.720555
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # To test the python implementation of lgetfilecon_raw function by replacing original function with test function
    _selinux_lib.lgetfilecon_raw = lgetfilecon_raw
    # Replacing the unit test result according to the file system path
    result = lgetfilecon_raw("/etc/passwd")
    unit_test_result = [0, 'system_u:object_r:etc_runtime_t:s0']
    assert result[0] == unit_test_result[0] and result[1] == unit_test_result[1], \
        "Unit test is not passed for the function lgetfilecon_raw"



# Generated at 2022-06-13 00:04:19.440695
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    con = c_char_p()
    try:
        rc = _selinux_lib.lgetfilecon_raw("/", byref(con))
        print("RC: %s" % rc)
        print("CON: %s" % to_native(con.value))
    finally:
        _selinux_lib.freecon(con)


# Generated at 2022-06-13 00:04:21.734128
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # TODO: test with a file that has an assigned SELinux context
    # TODO: test with a file that does *not* have an assigned SELinux context
    pass



# Generated at 2022-06-13 00:04:25.449358
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Run test to get the correct context
    (rc, context) = lgetfilecon_raw(b'/')
    if rc != -1:
        return context
    else:
        return 'selinux is not available'


# Generated at 2022-06-13 00:04:26.623255
# Unit test for function matchpathcon
def test_matchpathcon():
    assert matchpathcon('/tmp/', 0) == [0, 'system_u:object_r:tmp_t:s0']

# Generated at 2022-06-13 00:04:30.261800
# Unit test for function matchpathcon
def test_matchpathcon():
    matchinfo = matchpathcon('test_file', 0)
    assert matchinfo[0] == 0
    assert matchinfo[1] == 'user_u:user_r:user_t:s0'

# Generated at 2022-06-13 00:04:33.840752
# Unit test for function matchpathcon
def test_matchpathcon():
    import os
    from ansible.module_utils.selinux import matchpathcon

    rc, con = matchpathcon("/", os.stat("/").st_mode)
    assert rc == 0
    assert con == "system_u:object_r:root_t:s0"

# Generated at 2022-06-13 00:04:43.603614
# Unit test for function matchpathcon
def test_matchpathcon():
    from ansible_collections.community.general.plugins.module_utils import selinux
    from ansible_collections.community.general.tests.unit.test_utils.test_text.test_converters import to_bytes, to_native

    args = []
    if sys.version_info[0] < 3:
        # The source is a unicode string in Python 2
        filename = '/tmp/\xe3\x81\x82\xe3\x81\x84\xe3\x81\x86\xe3\x81\x88\xe3\x81\x8a'
        args = [filename.decode('utf-8'), 0]

# Generated at 2022-06-13 00:04:46.608873
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    if os.path.exists('test_file'):
        os.remove('test_file')

    os.system('touch test_file')
    rc, con = lgetfilecon_raw('test_file')
    assert rc == 0

    os.remove('test_file')

# Generated at 2022-06-13 00:04:58.147944
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    from stat import S_IFDIR, S_IFREG
    from os import mkdir, mknod
    from tempfile import mkdtemp

    def _check_filecon(fn, expected):
        rc, con = lgetfilecon_raw(fn)
        if expected is None:
            assert rc == -1
        else:
            assert rc == 0
            assert con == expected

    # create directory structure
    tmpdir = mkdtemp()
    etcdir = os.path.join(tmpdir, 'etc')
    mkdir(etcdir)

    # set file contexts
    _check_filecon(tmpdir, None)
    _check_filecon(etcdir, None)
    lsetfilecon(etcdir, 'system_u:object_r:etc_t:s0')
    _check_file

# Generated at 2022-06-13 00:05:00.622413
# Unit test for function matchpathcon
def test_matchpathcon():
    # Test case should use real path
    result = matchpathcon('/etc/passwd', 0)
    assert result == [0, 'user_home_dir_t']



# Generated at 2022-06-13 00:05:07.240608
# Unit test for function matchpathcon
def test_matchpathcon():
    """Returns True if no error occurs, False otherwise."""
    try:
        matchpathcon('/etc/selinux/config', 0)
    except OSError:
        return False
    return True

# Generated at 2022-06-13 00:05:09.561657
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    selinux_info = lgetfilecon_raw('/etc/passwd')
    print(selinux_info[0])
    print(selinux_info[1])



# Generated at 2022-06-13 00:05:19.801825
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    def _setup():
        base_file = '/etc/selinux/targeted/contexts/files/file_contexts'
        test_file = '/tmp/file_contexts.test'
        os.symlink(base_file, test_file)

        target_con = 'system_u:object_r:usr_t:s0'
        test_con = lgetfilecon_raw(test_file)

        os.unlink(test_file)
        return [test_con, target_con]

    [rc, test_con], [target_con] = _setup()
    assert rc == 0
    assert test_con == target_con



# Generated at 2022-06-13 00:05:22.090239
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    [rc, con] = lgetfilecon_raw('test_lgetfilecon_raw_foo')
    assert rc == -1
    assert con is None


# Generated at 2022-06-13 00:05:24.812159
# Unit test for function matchpathcon
def test_matchpathcon():
    if not _selinux_lib.matchpathcon:
        return
    ctx = matchpathcon('/', 0)
    assert ctx[0] == 0
    assert ctx[1] is not None



# Generated at 2022-06-13 00:05:36.786099
# Unit test for function matchpathcon
def test_matchpathcon():
    path = '/tmp/testfile'
    mode = os.R_OK | os.W_OK | os.X_OK

    try:
        # Create file
        with open(path, 'w') as testfile:
            testfile.write('test')

        # Execute function
        ret = matchpathcon(path, mode)
        assert ret[0] == 0

    finally:
        # Remove file
        os.remove(path)


if __name__ == '__main__':
    # Run tests
    # FIXME: test_matchpathcon requires write-protected /tmp or root access
    # test_matchpathcon()
    print('No unit tests for module {0}.'.format(__file__))
    sys.exit(0)

# Generated at 2022-06-13 00:05:41.848427
# Unit test for function matchpathcon
def test_matchpathcon():
    # Test an invalid path
    path = '/no_such_file'
    mode = os.R_OK
    expected = [0, 'system_u:object_r:unlabeled_t:s0']
    result = matchpathcon(path, mode)
    assert result == expected, "matchpathcon failed for invalid path"



# Generated at 2022-06-13 00:05:44.729859
# Unit test for function matchpathcon
def test_matchpathcon():
    # returns 0 on success
    rc, con = matchpathcon('/tmp/test', 0)
    assert rc == 0, rc
    # returns string on success
    assert isinstance(con, str), con



# Generated at 2022-06-13 00:05:48.001113
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    if os.path.exists('/etc/issue'):
        assert lgetfilecon_raw('/etc/issue') is not None
    else:
        assert lgetfilecon_raw('/etc/issue')[0] == -1


# Generated at 2022-06-13 00:05:49.623994
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # prepare meta data
    rc, context = lgetfilecon_raw('/tmp')
    assert rc == 0
    assert context



# Generated at 2022-06-13 00:06:03.717756
# Unit test for function matchpathcon
def test_matchpathcon():
    path = "/etc/myfile"
    mode = 0
    rc, con = matchpathcon(path, mode)
    print("rc: {}, con: {}".format(rc, con))


# Generated at 2022-06-13 00:06:12.019042
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = '/tmp/test_lgetfilecon_raw'
    with open(path, 'w+') as f:
        f.write('foo')

    # If a file does not have any SELinux context and SELinux is disabled,
    # we return 0 but we do not set context (con.value is NULL)
    if is_selinux_enabled() == 1:
        rc, con = lgetfilecon_raw(path)
        assert (con is not None)
    else:
        rc, con = lgetfilecon_raw(path)
        assert (con is None)


if __name__ == '__main__':
    test_lgetfilecon_raw()

# Generated at 2022-06-13 00:06:20.385635
# Unit test for function matchpathcon
def test_matchpathcon():
    import contextlib
    import tempfile

    def test_path(path):
        mode = os.R_OK
        if os.path.isfile(path):
            mode = os.R_OK + os.W_OK

        rc, con = matchpathcon(path, mode)
        assert rc == 0, "Expect no error, got {0}".format(rc)
        if not con:
            raise Exception("Expect valid context, got {0}".format(con))

        return con

    @contextlib.contextmanager
    def mkdtemp():
        tmpdir = tempfile.mkdtemp()
        try:
            yield tmpdir
        finally:
            os.rmdir(tmpdir)

    # test a directory
    with mkdtemp() as path:
        con = test_path(path)
        print

# Generated at 2022-06-13 00:06:22.017145
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    ''' lgetfilecon_raw unit test'''
    results = lgetfilecon_raw('/etc/passwd')
    # FIXME: What are the expected values, can we assert on them?
    assert results


# Generated at 2022-06-13 00:06:24.763757
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw(b'/etc/passwd')[1] == 'system_u:object_r:etc_runtime_t:s0'
    assert lgetfilecon_raw(b'/tmp/randomfile')[0] == -1, 'Should return -1 if file does not exist'


# Generated at 2022-06-13 00:06:35.478008
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw('/proc/self/')
    assert rc == 0, "unable to get/proc/self/ context, rc: {0}, con: {1}".format(rc, con)
    assert con.startswith('system_u:object_r:proc_t:s0'), "invalid /proc/self/ context, rc: {0}, con: {1}".format(rc, con)

    rc, con = lgetfilecon_raw('/etc/shadow')
    assert rc == -1, "expected error when getting /etc/shadow, rc: {0}, con: {1}".format(rc, con)



# Generated at 2022-06-13 00:06:41.349521
# Unit test for function matchpathcon
def test_matchpathcon():
    path = '/'
    con = c_char_p()
    rc = _selinux_lib.matchpathcon(path, 0, byref(con))
    if rc < 0:
        errno = get_errno()
        raise OSError(errno, os.strerror(errno))
    print(con.value)
    _selinux_lib.freecon(con)


if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-13 00:06:48.925117
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import tempfile
    from os import stat as os_stat
    from os.path import ismount

    fd, temp_file_path = tempfile.mkstemp()
    os.close(fd)
    is_source_mounted = ismount(temp_file_path)
    result = lgetfilecon_raw(temp_file_path)
    os.remove(temp_file_path)
    # Need to test only failed cases, because return values depend on host, file and policy
    assert result[0] == 0 or result[0] == 1, \
        "selinux.lgetfilecon_raw() execution failed with status: %s" % result[0]

# Generated at 2022-06-13 00:06:54.006584
# Unit test for function matchpathcon
def test_matchpathcon():
    rc = matchpathcon('/', 0)
    assert rc[0] == 0, 'matchpathcon is not working for /'

    rc = matchpathcon('/', os.R_OK)
    assert rc[0] == 0, 'matchpathcon is not working for /'

    rc = matchpathcon('foo', 0)
    assert rc[0] != 0, 'matchpathcon is not working for foo'



# Generated at 2022-06-13 00:06:56.533855
# Unit test for function matchpathcon
def test_matchpathcon():
    if matchpathcon('/tmp', 0)[1] == b'unconfined_u:object_r:user_tmp_t:s0':
        return True
    return False


# Generated at 2022-06-13 00:07:19.898659
# Unit test for function matchpathcon
def test_matchpathcon():
    [rc, con] = matchpathcon('/dev/null', 0)
    assert rc == 0
    assert con == 'system_u:object_r:null_device_t:s0'

# Generated at 2022-06-13 00:07:24.631203
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    try:
        rc, con = lgetfilecon_raw('/etc/selinux')
        assert rc == 0, "Error in function lgetfilecon_raw"
        assert con == 'system_u:object_r:etc_t:s0', "Error in function lgetfilecon_raw"
    except ImportError:
        # ignore import errors
        pass



# Generated at 2022-06-13 00:07:31.531247
# Unit test for function matchpathcon
def test_matchpathcon():
    assert matchpathcon("/etc/passwd", 0) == [0, "system_u:object_r:unlabeled_t:s0"]
    assert matchpathcon("/etc", 0) == [0, "system_u:object_r:etc_t:s0"]
    assert matchpathcon("/", 0) == [0, "system_u:object_r:root_t:s0"]
    assert matchpathcon("/var/log/audit", 0) == [0, "system_u:object_r:auditd_log_t:s0"]



# Generated at 2022-06-13 00:07:34.986866
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    str = "/"
    [rc, mode] = lgetfilecon_raw(str)
    assert rc == 0
    assert to_native(mode) == 'system_u:object_r:root_t:s0'



# Generated at 2022-06-13 00:07:42.547258
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import tempfile
    import shutil

# Generated at 2022-06-13 00:07:46.656841
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw('/etc')
    if rc == 0:
        print('/etc context is {0}'.format(con))
    else:
        print('lgetfilecon_raw: {0}'.format(os.strerror(rc)))

# Generated at 2022-06-13 00:07:50.314841
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # create tmp file
    path = "/tmp/test_lgetfilecon_raw"
    open(path, "w").close()
    [rc, con] = lgetfilecon_raw(path)
    assert rc == 0
    assert con == "system_u:object_r:unlabeled_t:s0"
    os.remove(path)

# Generated at 2022-06-13 00:07:57.132920
# Unit test for function matchpathcon
def test_matchpathcon():
    path = b'/etc/passwd'
    mode = os.R_OK
    rc, value = matchpathcon(path, mode)
    assert rc == 0
    assert value == 'system_u:object_r:etc_runtime_t:s0'
    path = b'/usr/bin/foo'
    mode = os.R_OK
    rc, value = matchpathcon(path, mode)
    assert rc == -1
    assert value == ''
    rc, value = selinux_getpolicytype()
    assert rc == 0
    assert value == 'targeted'
    rc, value = selinux_getenforcemode()
    assert rc == 0
    assert value == 0

# Generated at 2022-06-13 00:08:01.633990
# Unit test for function matchpathcon
def test_matchpathcon():
    # Test a path and file type that needs the selinux_binary_policy_path argument
    test_path = '/usr/bin/foo'
    test_file_type = 'file'
    [rc, con] = matchpathcon(test_path, 0)
    assert (rc == 0)
    assert (con == 'system_u:object_r:bin_t:s0')

# Generated at 2022-06-13 00:08:03.641197
# Unit test for function matchpathcon
def test_matchpathcon():
    (rc, con) = matchpathcon('/etc/passwd', 0)
    assert rc == 0
    assert con == 'root:object_r:etc_runtime_t:s0'

# Generated at 2022-06-13 00:08:52.626684
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = b'/home/bob/file.txt'
    rc, con = lgetfilecon_raw(path)
    assert(rc == 0)
    assert(con == 'system_u:object_r:user_home_t:s0')



# Generated at 2022-06-13 00:08:56.796260
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    from tempfile import NamedTemporaryFile
    from os.path import exists

    with NamedTemporaryFile(prefix='ansible_unit_test_') as f:
        path = f.name
        assert exists(path)
        assert lgetfilecon_raw(path)[1] == 'system_u:object_r:unlabeled_t:s0'

# Generated at 2022-06-13 00:08:59.861886
# Unit test for function matchpathcon
def test_matchpathcon():
    x = matchpathcon('/etc/hosts', 1)
    print('/etc/hosts has SELinux type:')
    print(x[1])


__all__ = [
    f
    for f in dir()
    if not f.startswith('_') and f not in sys.modules
]

# Generated at 2022-06-13 00:09:07.509791
# Unit test for function matchpathcon
def test_matchpathcon():
    # Test values come from https://github.com/python-selinux/python-selinux/blob/master/selinux/test/test_selinux_py.py
    assert matchpathcon('/etc/passwd', 0) == [0, 'system_u:object_r:etc_runtime_t:s0']
    assert matchpathcon('/etc/passwd', 1) == [0, 'system_u:object_r:etc_runtime_t:s0']
    assert matchpathcon('/etc/passwd', 2) == [0, 'system_u:object_r:etc_runtime_t:s0']
    assert matchpathcon('/etc/passwd', 3) == [-1, '']
