

# Generated at 2022-06-12 23:59:11.099371
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import selinux
    path = '/var/tmp/socket'
    if selinux.is_selinux_enabled():
        rc, con = selinux.lgetfilecon_raw(path)
        if rc == 0:
            print(con)

# Generated at 2022-06-12 23:59:16.354030
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = "/tmp/"
    rc, con = lgetfilecon_raw(path)
    print("lgetfilecon_raw({0}): rc={1}, con={2}".format(path, rc, con))



# Generated at 2022-06-12 23:59:20.602233
# Unit test for function matchpathcon
def test_matchpathcon():
    path = '/home/ddelisle/test_file'
    sys.argv.append(path)
    mode = 4
    rc, con = matchpathcon(path, mode)
    assert con == 'system_u:object_r:user_home_t:s0'
    assert rc == 0

# Generated at 2022-06-12 23:59:23.526280
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    test_file = '/etc/passwd'
    assert lgetfilecon_raw(test_file) == [0, 'system_u:object_r:etc_runtime_t:s0']

# Generated at 2022-06-12 23:59:26.936737
# Unit test for function matchpathcon
def test_matchpathcon():
    (rc, con) = matchpathcon('/etc/hosts', os.R_OK)
    assert rc == 0
    assert isinstance(con, str)
    # print('con = %s' % con)


# Generated at 2022-06-12 23:59:29.763323
# Unit test for function matchpathcon
def test_matchpathcon():
    result = matchpathcon('/var/lib/libvirt/images/vm01.qcow2', 0)
    assert result == [0, 'system_u:object_r:virt_image_t:s0']

# Generated at 2022-06-12 23:59:32.606208
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import tempfile
    (fd, filename) = tempfile.mkstemp()
    lgetfilecon_raw(filename)
    os.close(fd)
    os.remove(filename)

# Generated at 2022-06-12 23:59:35.953706
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw('/etc/hosts')
    if rc < 0:
        raise SystemError('error getting context for file {0!r}: {1}'.format(file_name, rc))

    print(con)


# Generated at 2022-06-12 23:59:40.174968
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    possible_enforce_values = [0, 1, 2]
    ret = _selinux_lib.lgetfilecon_raw('/etc/hosts', byref(con))
    if ret != 0:
        raise OSError(get_errno(), os.strerror(get_errno()))



# Generated at 2022-06-12 23:59:46.923254
# Unit test for function matchpathcon
def test_matchpathcon():
    import os
    path = os.path.join("/etc/selinux", "policy.xml")
    mode = 0
    rc, con = matchpathcon(path, mode)
    if rc == 0:
        print("Context of file " + path + " is " + con)
    else:
        print("matchpathcon failed: " + str(rc))


if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-12 23:59:56.929953
# Unit test for function matchpathcon
def test_matchpathcon():
    # test file mode with SELinux context
    mode = 0o644
    path = '/etc'
    rc, selinux_context = matchpathcon(path, mode)
    if rc != 0:
        raise AssertionError('matchpathcon failed. rc is {0}'.format(rc))
    if selinux_context != 'system_u:object_r:etc_t:s0':
        raise AssertionError('matchpathcon failed. selinux_context is {0}'.format(selinux_context))



# Generated at 2022-06-13 00:00:06.193848
# Unit test for function matchpathcon
def test_matchpathcon():
    import os
    import shutil
    import tempfile
    import stat
    import selinux

    rc, mode = selinux.selinux_getenforcemode()
    assert rc == 0
    assert mode in [0, 1, 2]

    assert selinux.is_selinux_enabled(), "SELinux is not enabled"
    assert selinux.is_selinux_mls_enabled(), "SELinux is not mls enabled"

    tempdir_path = tempfile.mkdtemp()
    con = None

# Generated at 2022-06-13 00:00:12.528864
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    """
    Test lgetfilecon_raw by checking for the security context for '/tmp'
    """
    try:
        (rc,label) = lgetfilecon_raw('/tmp')
    except OSError as e:
        raise AssertionError('Error: ' + str(e))
    assert rc == 0, to_native(label)
    assert to_native(label) == 'system_u:object_r:tmp_t:s0'


# Generated at 2022-06-13 00:00:18.206108
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import os
    import sys
    # Change to Ansible root directory
    sys.path.insert(0, os.environ['ANSIBLE_LIBRARY'])
    # Change to ansible-utils project root directory
    os.chdir(os.environ['ANSIBLE_PROJECT_DIR'])
    # Execute the function lgetfilecon_raw
    lgetfilecon_raw(b'/selinux/enforce')

# Generated at 2022-06-13 00:00:20.031188
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (rc, con) = lgetfilecon_raw("/")
    assert con == "system_u:object_r:unlabeled_t:s0"
    assert rc == 0

# Generated at 2022-06-13 00:00:29.292355
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    """test lgetfilecon_raw"""
    if os.environ.get('TRAVIS') == 'true':
        raise unittest.SkipTest('Testing on Travis is not supported')

    # If the context is not loaded, the function returns None
    if not selinux_getpolicytype()[1]:
        return

    # In case that selinux is disabled, it returns None
    if not is_selinux_enabled() or not selinux_getenforcemode()[1]:
        return

    # If the context is loaded, the function should return a list of 2 items
    # where the first item is 0 (success) and the second item is the context
    # of the file /etc/shadow

# Generated at 2022-06-13 00:00:32.731635
# Unit test for function matchpathcon
def test_matchpathcon():
    assert matchpathcon('/etc/passwd', 0) == [0, 'system_u:object_r:etc_runtime_t:s0']

# Generated at 2022-06-13 00:00:36.459746
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (rc, con) = lgetfilecon_raw('/etc/localtime')
    assert rc == 0
    assert con == 'system_u:object_r:etc_runtime_t:s0'



# Generated at 2022-06-13 00:00:41.072947
# Unit test for function matchpathcon
def test_matchpathcon():
    [rc, con] = matchpathcon('/etc', 0)

    if rc != 0:
        raise Exception('matchpathcon failed: {0}'.format(con))

    [rc, con] = matchpathcon('/etc1', 0)

    if rc != 0:
        raise Exception('matchpathcon failed: {0}'.format(con))


# Generated at 2022-06-13 00:00:42.778364
# Unit test for function matchpathcon
def test_matchpathcon():
    '''
    unit test for matchpathcon()
    '''
    path = '/tmp'
    mode = 0
    (rc, con) = matchpathcon(path, mode)
    print(rc, con)
    return rc == 0



# Generated at 2022-06-13 00:00:54.353270
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    test_path = "/tmp/test"

    # create test file
    with open(test_path, "w") as f:
        f.write("test")

    # get file context
    try:
        [rc, context] = lgetfilecon_raw(test_path)
    except OSError as e:
        if e.errno == 95:
            raise OSError(
                "Selinux is not enabled in system, "
                "please disable testcase or enable selinux"
            )
        raise
    assert rc == 0
    print('context: {0}'.format(context))

    # delete test file
    os.unlink(test_path)



# Generated at 2022-06-13 00:00:57.557580
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import tempfile
    path = tempfile.mktemp()
    open(path, 'w').close()

    data = lgetfilecon_raw(path)
    assert data[0] == 0

    os.remove(path)

# Generated at 2022-06-13 00:01:02.177119
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    print(lgetfilecon_raw('/etc/shadow'))
    print(lgetfilecon_raw('/tmp'))
    print(lgetfilecon_raw(b'/tmp'))
    print(lgetfilecon_raw('/tmp/testfile'))
    print(lgetfilecon_raw('/tmp/testfile2'))
    print(lgetfilecon_raw(b'/tmp/testfile2'))


# Generated at 2022-06-13 00:01:11.321183
# Unit test for function matchpathcon
def test_matchpathcon():
    class TestCase:
        def __init__(self, path, label):
            self.path = path
            self.label = label

    test_cases = [
        TestCase('/bin/ls', 'system_u:object_r:bin_t:s0'),
        TestCase('/tmp', 'system_u:object_r:tmp_t:s0'),
        TestCase('/dev/null', 'system_u:object_r:chr_file:s0')]

    for test_case in test_cases:
        res, rc = matchpathcon(test_case.path, 0)
        assert rc == 0, 'matchpathcon failed'
        assert res == test_case.label, 'matchpathcon failed'

# Generated at 2022-06-13 00:01:20.540841
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = 'test_path'
    con = 'test_con'
    # set lgetfilecon_raw function to dummy function
    _selinux_lib.lgetfilecon_raw = lambda path, con: 0
    # set con to global variable
    global _con
    _con = con
    # define dummy function
    def dummy_function(path, p_con):
        # set con value
        p_con.value = _con
        global _path
        _path = path
        return 0

    # set lgetfilecon_raw function to dummy function
    _selinux_lib.lgetfilecon_raw = dummy_function

    result = lgetfilecon_raw(path)
    # check if lgetfilecon_raw function is called
    assert result[0] == 0
    # check if path variable is

# Generated at 2022-06-13 00:01:22.704177
# Unit test for function matchpathcon
def test_matchpathcon():
    assert matchpathcon('/etc/passwd', 0) == [0, 'system_u:object_r:etc_runtime_t:s0']



# Generated at 2022-06-13 00:01:27.250899
# Unit test for function matchpathcon
def test_matchpathcon():
    path = "/tmp/foo"
    mode = 0
    (rc, context) = matchpathcon(path, mode)
    assert(rc == 0)
    assert(context == "system_u:object_r:tmp_t:s0")



# Generated at 2022-06-13 00:01:30.298746
# Unit test for function matchpathcon
def test_matchpathcon():
    path = b"/tmp"
    mode = 0
    result = matchpathcon(path, mode)
    assert result == [0, 'system_u:object_r:tmp_t:s0']



# Generated at 2022-06-13 00:01:32.779205
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw('/')
    print("rc: %s, context: %s" % (rc, con))



# Generated at 2022-06-13 00:01:35.152912
# Unit test for function matchpathcon
def test_matchpathcon():
    path = '/tmp/'
    mode = os.st_mode(path)
    con = matchpathcon(path, mode)[1]
    assert con.startswith('system_u:object_r')

# Generated at 2022-06-13 00:01:41.426596
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    from ansible.module_utils.six.moves import StringIO

    test_file = StringIO(u"test")

    # this should return the '/' context
    assert lgetfilecon_raw('/')[1] == '/'

    # this should return the '/' context
    assert lgetfilecon_raw(test_file)[1] == '/'



# Generated at 2022-06-13 00:01:47.486915
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = '/tmp/testfile'
    if not os.path.isfile(path):
        with open(path, 'w') as f:
            print('testfile', file=f)

    [rc, context] = lgetfilecon_raw(path)
    assert rc == 0
    assert context == 'system_u:object_r:tmp_t:s0'
    os.remove(path)

# Generated at 2022-06-13 00:01:49.002129
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw('/')
    assert rc == 0
    assert con != ''

# Generated at 2022-06-13 00:01:52.365786
# Unit test for function matchpathcon
def test_matchpathcon():
    test = {}
    test['path'] = '/etc/shadow'
    test['mode'] = os.R_OK
    test['result'] = matchpathcon(test['path'], test['mode'])
    print("matchpathcon: rc: %s" % test['result'][0])
    print("matchpathcon: con: %s" % test['result'][1])


if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-13 00:01:58.260417
# Unit test for function matchpathcon
def test_matchpathcon():
    if selinux_getenforcemode()[1] == 0:
        if os.path.exists('/var/www/html'):
            return matchpathcon('/var/www/html', 0)[1]
        elif os.path.exists('/var/www'):
            return matchpathcon('/var/www', 0)[1]

# Generated at 2022-06-13 00:02:04.333919
# Unit test for function matchpathcon
def test_matchpathcon():
    # Get path for directory by using __file__
    # __file__ return file name
    path = os.path.dirname(os.path.abspath(__file__)) + '/file_to_relabel'

    # mode is a file type
    mode = os.stat(path).st_mode
    rc, con = matchpathcon(path, mode)
    if rc >= 0:
        print('\tsecurity context of the path: %s' % con)
    else:
        print('\tmatchpathcon error: %s' % rc)



# Generated at 2022-06-13 00:02:08.454759
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon('/', 0)
    assert con == "system_u:object_r:admin_home_t:s0"

# Generated at 2022-06-13 00:02:11.328675
# Unit test for function matchpathcon
def test_matchpathcon():
    (rc, final_context) = matchpathcon(b'/', 0)
    assert rc == 0 and final_context is not None, 'matchpathcon(b"/", 0) failed for root'


# Generated at 2022-06-13 00:02:13.368360
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    [rc, con] = lgetfilecon_raw(b'/tmp/sample1.txt')
    assert rc == 0


# Generated at 2022-06-13 00:02:19.351481
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc = 0
    con = ''
    path = '/etc/resolv.conf'
    test_result = lgetfilecon_raw(path)
    if test_result[0] >= 0:
        con = test_result[1]
    elif test_result[0] == -1 and test_result[1] == 22:
        con = test_result[1]
    else:
        rc = 1
    print(rc)
    print(con)


# Generated at 2022-06-13 00:02:22.747937
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon('/etc/hosts', 0)
    assert rc == 0
    assert con == 'system_u:object_r:net_conf_t:s0'

# Generated at 2022-06-13 00:02:26.865580
# Unit test for function matchpathcon
def test_matchpathcon():
    result = []
    result = matchpathcon('/opt/test','0')
    assert result[0] == 0
    assert result[1]=='user_home_dir_t:dir:s0'


# Generated at 2022-06-13 00:02:30.757038
# Unit test for function matchpathcon
def test_matchpathcon():
    path = '/etc/shadow'
    # set the mode to path exists
    mode = 0
    result = matchpathcon(path, mode)
    assert result[0] == 0 and result[1] == 'system_u:object_r:shadow_t'



# Generated at 2022-06-13 00:02:31.888402
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw('/tmp')[0] == 0

# Generated at 2022-06-13 00:02:35.604044
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw('/usr/lib/python3.6/site-packages/ansible/module_utils/selinux/_selinux.py') == [0, b'system_u:object_r:usr_t:s0']

# Generated at 2022-06-13 00:02:44.828452
# Unit test for function matchpathcon
def test_matchpathcon():
    from ansible.module_utils.common._collections_compat import OrderedDict

    # Some examples from the library documentation
    # http://linux.die.net/man/3/matchpathcon

# Generated at 2022-06-13 00:02:53.612906
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # /dev/null is always label sys_devpts:chr_file, but is available on any system
    path = '/dev/null'
    expected = [0, 'system_u:object_r:sys_devpts:s0']
    actual = lgetfilecon_raw(path)
    if actual != expected:
        raise AssertionError('Failed to get actual filecon ' + actual + ' expected ' + expected)

if __name__ == '__main__':
    test_lgetfilecon_raw()

# Generated at 2022-06-13 00:02:57.111018
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = b"/etc/selinux/config"
    rc, con = lgetfilecon_raw(path)
    assert rc == 0
    assert con == "system_u:object_r:etc_runtime_t:s0"

# Generated at 2022-06-13 00:03:00.573524
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = '/selinux/test'
    rc, con = lgetfilecon_raw(path)
    assert not rc
    assert con == 'system_u:object_r:test_t:s0'


# Generated at 2022-06-13 00:03:10.327026
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    testcases = (
        {'name': '/etc/fstab', 'out': b'system_u:object_r:etc_t:s0'},
        {'name': '/tmp/ansible', 'out': b'system_u:object_r:tmp_t:s0'},
        {'name': '/home/ansible', 'out': b'system_u:object_r:home_root_t:s0'},
        {'name': 'not/a/path', 'out': b'bad selinux context'},
    )

    for test_case in testcases:
        result = lgetfilecon_raw(test_case['name'])[1].decode()
        assert result == test_case['out'], "Unexpected output, got: {}".format(result)

# Generated at 2022-06-13 00:03:15.431010
# Unit test for function matchpathcon
def test_matchpathcon():

    (rc, con) = matchpathcon('/sys', 0)
    print('rc: {0}, con: {1}'.format(rc, con))
    assert rc == 0
    assert con == 'system_u:system_r:sysfs_t:s0'


# Generated at 2022-06-13 00:03:24.553601
# Unit test for function matchpathcon
def test_matchpathcon():
    """Test to check if it returns the proper SELinux context for a given path"""

    try:
        from unittest.mock import patch
    except ImportError:
        from mock import patch

    with patch.object(os, 'stat', return_value=None):
        assert matchpathcon('/var/log/messages', 0) == [0, 'user_log_t']

        assert matchpathcon('/var/log/messages', 0o100) == [0, 'user_log_t']

        assert matchpathcon('/var/log/messages', 0o200) == [0, 'user_log_t']

        assert matchpathcon('/var/log/messages', 0o400) == [0, 'user_log_t']


# Generated at 2022-06-13 00:03:26.852785
# Unit test for function matchpathcon
def test_matchpathcon():
    assert matchpathcon('/etc/passwd', 0) == [0, 'system_u:object_r:etc_runtime_t:s0']

# Generated at 2022-06-13 00:03:28.990721
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw(b'/')[1] == 'system_u:object_r:root_t:s0'



# Generated at 2022-06-13 00:03:31.272307
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    if is_selinux_enabled() == 1:
        path = '/etc'
        rc, con = lgetfilecon_raw(path)
        assert rc == 0
        assert con
    else:
        print("selinux is not enabled")



# Generated at 2022-06-13 00:03:34.102067
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Tested against the command line 'semanage fcontext --list'
    test_data = '/dev/mapper(/.*)?  <<none>>:rawdevice_t:s0:s0:s0:s0:s0'
    expected = [0, test_data]
    assert expected == lgetfilecon_raw(b'/dev/mapper'), 'output does not match expected value'

# Generated at 2022-06-13 00:03:45.004304
# Unit test for function matchpathcon
def test_matchpathcon():
    # This test was used once upon a time to verify that the matchpathcon
    # function could be used to set the file context of a new file. It
    # is kept here in case the future need to verify something else
    # related to selinux python bindings.
    def hexstring(bytes):
        return ' '.join(['%0.2X' % ord(b) for b in bytes])

    def test_matchpathcon():
        # Create a new file for the purposes of testing matchpathcon
        (fd, filename) = tempfile.mkstemp()
        os.close(fd)
        st = os.stat(filename)

        # Get file context for new file
        (rc, new_context) = matchpathcon(filename, st.st_mode)

# Generated at 2022-06-13 00:03:48.924077
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = '/tmp/selinux_test_path'
    f = open(path, 'w+')
    f.close()
    ret = lgetfilecon_raw(path)
    print('The SELinux context for file ' + path + ' is:')
    print(ret[1])
    os.remove(path)


if __name__ == '__main__':
    test_lgetfilecon_raw()

# Generated at 2022-06-13 00:03:57.134745
# Unit test for function matchpathcon
def test_matchpathcon():
    # Test for the absence of "selinux_python_test" directory
    assert matchpathcon("/tmp/selinux_python_test", os.R_OK)[0] == -1
    assert matchpathcon("/tmp/selinux_python_test", os.R_OK)[1] == ''
    # Test for the existence of "/tmp/selinux_python_test" directory
    os.makedirs("/tmp/selinux_python_test")
    assert matchpathcon("/tmp/selinux_python_test", os.R_OK)[0] == 0
    os.rmdir("/tmp/selinux_python_test")

# Generated at 2022-06-13 00:03:59.793278
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon('/dev/null', os.R_OK)
    assert rc == 0
    assert con == 'system_u:object_r:null_device_t:s0'

# Generated at 2022-06-13 00:04:11.738718
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = '/etc/localtime'
    check_lgetfilecon_raw = lgetfilecon_raw(path)
    print(check_lgetfilecon_raw)
    assert isinstance(check_lgetfilecon_raw, list)
    assert len(check_lgetfilecon_raw) == 2
    assert isinstance(check_lgetfilecon_raw[0], int)
    assert check_lgetfilecon_raw[0] == 0
    assert isinstance(check_lgetfilecon_raw[1], str)
    assert check_lgetfilecon_raw[1].startswith("system_u")



# Generated at 2022-06-13 00:04:13.311667
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw('/etc/shadow')
    assert rc == 0
    assert con == 'system_u:object_r:shadow_t:s0'

# Generated at 2022-06-13 00:04:19.802983
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    env = os.environ.copy()

    # disable SELinux
    env['SELINUX'] = 'disabled'
    rc, con = lgetfilecon_raw('/')
    assert rc == -2, 'Failed to get context of /'
    assert con == 'system_u:object_r:root_t:s0', 'Failed to get context of /'



# Generated at 2022-06-13 00:04:26.389159
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    test_path = '/etc/passwd'
    try:
        with open(test_path, 'r') as f:
            f.read()
    except OSError as e:
        assert isinstance(e, OSError)
        assert e.errno == 2
        assert e.strerror == 'No such file or directory'

    assert is_selinux_enabled()
    assert lgetfilecon_raw(test_path)[0] == 0
    assert isinstance(lgetfilecon_raw(test_path)[1], str)

# Generated at 2022-06-13 00:04:31.919994
# Unit test for function matchpathcon
def test_matchpathcon():
    con = c_char_p()
    rc = _selinux_lib.matchpathcon("/etc/shadow", 1, byref(con))
    assert rc == 0
    assert to_native(con.value) == "system_u:object_r:shadow_t:s0"
    _selinux_lib.freecon(con)


# Generated at 2022-06-13 00:04:34.090732
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    sys.stderr.write('SELinux is not enabled on this system, skipping test_lgetfilecon_raw...\n')


# Generated at 2022-06-13 00:04:36.962511
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (ret, out) = lgetfilecon_raw('/etc/passwd')
    assert ret in (0, 1)

if __name__ == '__main__':
    test_lgetfilecon_raw()

# Generated at 2022-06-13 00:04:45.736116
# Unit test for function matchpathcon
def test_matchpathcon():
    ret = matchpathcon('/etc/hosts', 0)
    assert(ret == [0, ''])
    ret = matchpathcon('/etc/hosts', 1)
    assert(ret == [0, 'system_u:object_r:etc_runtime_t:s0'])
    ret = matchpathcon('/etc/semanage.d', 1)
    assert(ret == [0, 'system_u:object_r:etc_runtime_t:s0'])
    ret = matchpathcon('/etc/selinux/policy/policy.kern', 1)
    assert(ret == [0, 'system_u:object_r:etc_runtime_t:s0'])
    ret = matchpathcon('/etc/semanage.conf', 1)

# Generated at 2022-06-13 00:04:47.704970
# Unit test for function matchpathcon
def test_matchpathcon():
    if not matchpathcon('/etc/passwd', 0)[0] == 0:
        raise Exception("Failed to match path /etc/passwd")



# Generated at 2022-06-13 00:04:50.923768
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw('/') == [0, 'system_u:object_r:root_t:s0']

# Generated at 2022-06-13 00:05:02.286580
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc = lgetfilecon_raw('/etc/passwd')
    assert rc[0] == 0
    assert type(rc[1]) == str


# Generated at 2022-06-13 00:05:08.396493
# Unit test for function matchpathcon
def test_matchpathcon():
    from ansible.module_utils._text import to_text

    rc, con = matchpathcon(b'/tmp', 0)
    assert rc == 0, 'Expected status code of 0, actual status code is %s' % rc
    assert to_text(con) == 'system_u:object_r:tmp_t:s0', 'Expected context of "system_u:object_r:tmp_t:s0", actual context was %s' % to_text(con)



# Generated at 2022-06-13 00:05:09.813118
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    result = lgetfilecon_raw(b'/tmp')
    assert result[0] == 0
    assert result[1] == 'system_u:object_r:tmp_t:s0'



# Generated at 2022-06-13 00:05:19.408884
# Unit test for function matchpathcon
def test_matchpathcon():
    test_path = b'test'
    # NB: the official selinux module uses this code to test for valid paths
    if not os.path.exists(test_path):
        os.mknod(test_path, 0o644)
    rc, con = matchpathcon(test_path, 0)
    assert rc == 0
    # UNKNOWN is probably okay here as we are testing for a valid label
    assert con == 'UNKNOWN'
    os.remove(test_path)
    rc, con = matchpathcon('', 0)
    assert rc == -1
    assert con is None  # pragma: no cover

# Generated at 2022-06-13 00:05:28.738247
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():

    # Create a new directory with umask 022
    test_dir_con = 'u:object_r:usr_t:s0'
    test_file_con = 'u:object_r:usr_t:s0'


# Generated at 2022-06-13 00:05:35.044534
# Unit test for function matchpathcon
def test_matchpathcon():
    from tempfile import mkdtemp
    from shutil import rmtree
    tmpdir = mkdtemp(prefix='ansible_test_selinux')
    try:
        rc, con = matchpathcon(tmpdir, os.R_OK)
        assert rc == 0
        assert con == 'user_tmp_t'
    finally:
        rmtree(tmpdir)

# Generated at 2022-06-13 00:05:45.882207
# Unit test for function matchpathcon
def test_matchpathcon():
    # NOTE: following selabel_lookup() return values:
    # -1 = error
    # 0 = success
    # 1 = partial match
    # 2 = no match
    assert matchpathcon('/etc/resolv.conf', 0) == [0, 'system_u:object_r:resolv_conf_t:s0']
    assert matchpathcon('/etc/no/such/file', 0)[0] in [1, -1]
    assert matchpathcon('/etc/resolv.conf', SELINUX_COMPUTE_EXCESS) == [0, 'system_u:object_r:resolv_conf_t:s0']

    assert matchpathcon('/tmp/x', 0) == [0, 'system_u:object_r:tmp_t:s0']

   

# Generated at 2022-06-13 00:05:51.075356
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import tempfile

    # create a tempfile and set the context
    with tempfile.NamedTemporaryFile() as tmpfile:
        context = lgetfilecon_raw(tmpfile.name)
        assert context[0] == 0
        # some systems may be in enforcing mode
        assert context[1] in ['system_u:object_r:tmp_t:s0', 'system_u:object_r:tmp_t:s0:c0.c1023']
        assert context[1] == lgetfilecon_raw('/tmp')[1]

# Generated at 2022-06-13 00:05:56.093166
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import os

    from ansible.module_utils.selinux import is_selinux_enabled, lgetfilecon_raw

    con = lgetfilecon_raw(__file__)[1]

    if is_selinux_enabled():
        assert con in ['system_u:object_r:unlabeled_t:s0', 'system_u:object_r:ansible_lib_module_t:s0']
    else:
        assert con is None


# Generated at 2022-06-13 00:05:59.207797
# Unit test for function matchpathcon
def test_matchpathcon():
    [rc, con] = matchpathcon(b'/home/debian', 0)
    print("rc:", rc, ", con:", con)


# Generated at 2022-06-13 00:06:22.415890
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw('/tmp/foo')
    assert rc == 1
    assert con == 'unlabeled_t'



# Generated at 2022-06-13 00:06:24.244348
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw('/etc/passwd')[1] == 'system_u:object_r:etc_runtime_t:s0'


# Generated at 2022-06-13 00:06:26.142458
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (rc, con) = lgetfilecon_raw('/etc/hosts')
    print('/etc/hosts: %s' % con)



# Generated at 2022-06-13 00:06:38.069624
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import subprocess
    major_ver, minor_ver = os.uname()[2].split('.')[:2]
    if int(major_ver) > 2 or (int(major_ver) == 2 and int(minor_ver) >= 6):
        proc = subprocess.Popen(['mount', '-t', 'selinuxfs', 'selinux', '/sys/fs/selinux'], stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        out, err = proc.communicate()
        if proc.returncode == 0:
            res = lgetfilecon_raw(b'/')
            if res[0] == 0:
                print(res[1])



# Generated at 2022-06-13 00:06:41.212242
# Unit test for function matchpathcon
def test_matchpathcon():
    """
    Unit test for function matchpathcon
    """
    rc, con = matchpathcon("/etc", 0)
    assert rc == 0
    assert con == b"system_u:object_r:etc_t:s0"

# Generated at 2022-06-13 00:06:45.235899
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    """
    Get the SELinux context of a file using libselinux Python interface.
    """
    expected = "system_u:object_r:usr_t:s0"
    rc, context = lgetfilecon_raw("/usr")
    assert rc == 0 and context == expected

if __name__ == '__main__':
    test_lgetfilecon_raw()

# Generated at 2022-06-13 00:06:48.377278
# Unit test for function matchpathcon
def test_matchpathcon():
    rc = matchpathcon('/etc/passwd', 0)
    assert rc[0] == 0
    assert rc[1] == 'system_u:object_r:etc_runtime_t:s0'


# Generated at 2022-06-13 00:06:51.355574
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    test_path = '/bin/ls'
    assert lgetfilecon_raw(test_path) == [0, 'system_u:object_r:bin_t:s0']

# Generated at 2022-06-13 00:06:59.564694
# Unit test for function matchpathcon
def test_matchpathcon():
    """
    Test the return value of the wrapper function matchpathcon

    This is testing that matchpathcon returns a list element
    when passed a path and a mode. This unit test is being used
    to test the security module. The test is testing a function
    that is used to get the context of a path. This test is
    also testing a function that is used to match the context
    of a path with a mode. It is also testing that the function
    is returning a list containing the return code and context of
    the path.
    """
    import os
    import stat

    # creating a temporary directory for testing
    new_dir = os.mkdir("/tmp/mytemp")
    # changing to the new directory
    os.chdir("/tmp/mytemp")
    # creating a temporary file in the new directory

# Generated at 2022-06-13 00:07:01.491444
# Unit test for function matchpathcon
def test_matchpathcon():
    """
    Validate matchpathcon function
    """
    from ansible.module_utils.selinux import matchpathcon
    rc, result = matchpathcon('/tmp/foo', 0)
    if rc == 0:
        assert result == 'system_u:object_r:tmp_t:s0'

# Generated at 2022-06-13 00:07:45.489797
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw('/etc/passwd')
    assert rc == 0
    assert con.startswith('system_u:object_r:etc_runtime_t:s0')



# Generated at 2022-06-13 00:07:48.503085
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = '/'
    result = lgetfilecon_raw(path)
    assert(result[0] == 0)
    assert(result[1] == 'system_u:object_r:root_t:s0')


# Generated at 2022-06-13 00:07:53.668023
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    if is_selinux_enabled() != 1:
        print("SELinux is disabled on system")
        return

    path = b'/var/tmp'
    [rc, con] = lgetfilecon_raw(path)
    if rc != 0:
        print("Error: {}".format(os.strerror(rc)))
    else:
        print("con={}".format(con))


if __name__ == '__main__':
    test_lgetfilecon_raw()

# Generated at 2022-06-13 00:07:58.826722
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = "/tmp/foo"
    try:
        f = open(path, "w")
    except IOError:
        raise ValueError('Could not create the file %s' % path)
    else:
        f.close()
    try:
        rc, con = lgetfilecon_raw(path)
    except ValueError as e:
        raise ValueError('Could not get the security context of the file %s: %s' % (path, e))
    else:
        print('Security Context: %s' % con)
    finally:
        os.remove(path)
        pass

# Generated at 2022-06-13 00:08:01.908031
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw('/etc')
    assert rc == 0, 'Error code: ' + str(rc)
    assert con is not None and con != '', 'RC: ' + str(rc)


# Generated at 2022-06-13 00:08:06.152625
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = "/var/log/audit/auditd/current"
    con = c_char_p()
    try:
        rc = _selinux_lib.lgetfilecon_raw(path, byref(con))
        assert rc == 0
        assert con.value == b"system_u:object_r:auditd_log_t:s0"
    finally:
        _selinux_lib.freecon(con)



# Generated at 2022-06-13 00:08:11.695014
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    from ansible.module_utils._text import to_bytes
    test_path = '/etc/localtime'
    test_rc = lgetfilecon_raw(test_path)

    if test_rc[0] != 0:
        raise Exception(test_rc)

    if test_rc[1] is None:
        raise Exception(test_rc)



# Generated at 2022-06-13 00:08:15.292144
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    """
    Check that lgetfilecon_raw is able to process a path, even if it does not exist.
    """
    rc, con = lgetfilecon_raw('/tmp/does_not_exist')

    assert rc == 0
    assert con == '?\x00'



# Generated at 2022-06-13 00:08:18.098897
# Unit test for function matchpathcon
def test_matchpathcon():
    path = '/etc/foo'
    path_mode = 0
    out = matchpathcon(path, path_mode)
    assert out[0] == 0
    assert out[1].startswith("system_u:object_r:"), "policy type: %s" % out[1]

# Generated at 2022-06-13 00:08:23.761196
# Unit test for function matchpathcon
def test_matchpathcon():
    tst = "/etc/passwd"
    mode = os.R_OK
    [rc, con] = matchpathcon(tst, mode)

    if rc == -1:
        rc = get_errno()
        print("matchpathcon failed: " + os.strerror(rc))
        return 1

    if rc == 0:
        if con == "system_u:object_r:user_home_t:s0":
            print("matchpathcon test for " + tst + " successful")
            return 0
        else:
            print("matchpathcon: Context returned from matchpathcon not as expected")
            return 1


if __name__ == '__main__':
    sys.exit(test_matchpathcon())