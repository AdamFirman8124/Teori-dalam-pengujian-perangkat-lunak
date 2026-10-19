

# Generated at 2022-06-12 23:59:13.122410
# Unit test for function matchpathcon
def test_matchpathcon():
    assert matchpathcon('/tmp/foo', 0) == [0, 'system_u:object_r:tmp_t:s0']
    assert matchpathcon(None, 0) == [-1, '']



# Generated at 2022-06-12 23:59:24.494853
# Unit test for function matchpathcon
def test_matchpathcon():
    # template:
    #     rc, con = matchpathcon('/var/lib/libvirt/images', selinux.S_IFREG)

    # These test case definitions match the one in the original implementation
    # https://github.com/ansible/ansible/blob/devel/lib/ansible/module_utils/selinux.py
    rc, con = matchpathcon('/sys/fs/selinux', selinux.S_IFDIR)
    if rc != 0 or con != 'system_u:object_r:selinuxfs:s0':
        raise AssertionError('Can not run test case for function matchpathcon')

    rc, con = matchpathcon('/dev/log', selinux.S_IFCHR)

# Generated at 2022-06-12 23:59:26.730455
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (e, r) = lgetfilecon_raw("/")
    assert e == 0 and r is not None, "Expected to get 0, not None"

# Generated at 2022-06-12 23:59:32.265445
# Unit test for function matchpathcon
def test_matchpathcon():
    # Set up some variables
    path = "/var/tmp/foo"
    mode = 0x800
    import datetime
    import tempfile
    path = tempfile.mkdtemp(prefix='myprefix', dir='/tmp')
    with open(path + '/foo', 'w') as f:
        f.write("Testing...")
        f.close()
    try:
        rc, con = matchpathcon(path + '/foo', mode)
        assert rc == 0
        assert con is not None
    finally:
        import shutil
        shutil.rmtree(path)



# Generated at 2022-06-12 23:59:39.007057
# Unit test for function matchpathcon
def test_matchpathcon():
    import os
    import tempfile

    dfd, dname = tempfile.mkdtemp()
    fd, fname = tempfile.mkstemp(suffix='.txt', dir=dname)
    mode = os.stat(fname).st_mode
    try:
        rc, context = matchpathcon(fname, mode)
        assert rc == 0, 'matchpathcon failed with return code {0}'.format(rc)
        assert context != '', 'matchpathcon failed to return a context'
    finally:
        os.close(fd)
        os.unlink(fname)
        os.rmdir(dname)


# Generated at 2022-06-12 23:59:43.434666
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon('/unittest/path', os.R_OK)
    assert rc == 0
    assert con == 'unconfined_u:object_r:unittest_t:s0'



# Generated at 2022-06-12 23:59:50.131058
# Unit test for function matchpathcon
def test_matchpathcon():
    path = "/tmp"
    mode = os.R_OK
    test_array = [path, mode]
    function_name = "matchpathcon"
    function_params = """
    rc, con = matchpathcon(path, mode)
    """
    expected_results = """[0, to_native(con.value)]"""

    return_value = matchpathcon(path, mode)
    if return_value != [0, '']:
        return_value[0] = 1
        return return_value[0]
    else:
        return 0

# Generated at 2022-06-12 23:59:52.222263
# Unit test for function matchpathcon
def test_matchpathcon():
    assert 'system_u:object_r:usr_t:s0' == matchpathcon('/usr', 0x0)[1]

# Generated at 2022-06-13 00:00:01.528092
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    result = lgetfilecon_raw('/etc/passwd')
    assert result == [0, 'system_u:object_r:etc_runtime_t:s0'], result

    if sys.version_info[0] == 2:
        # NOTE: "Not implemented" is not utf8 in python2
        result = lgetfilecon_raw('/etc/passwd1')
        assert result == [-1, b'Not\x20implemented'], result
    else:
        result = lgetfilecon_raw('/etc/passwd1')
        assert result == [-1, 'Not implemented'], result



# Generated at 2022-06-13 00:00:06.895974
# Unit test for function matchpathcon
def test_matchpathcon():
    """
    test_matchpathcon get the SELinux context for a path

    :kwarg path: path to check
    :kwarg mode: check mode for the path
    :returns: RC, context
    :rtype: tuple
    """
    path_to_check = "/usr/bin/ansible"
    return matchpathcon(path_to_check, os.R_OK)


# Generated at 2022-06-13 00:00:16.925315
# Unit test for function matchpathcon
def test_matchpathcon():
    if not selinux_getenforcemode()[1]:
        return "SELinux is disabled, skipping test"

    cwd = lgetfilecon_raw(b'.')[1]
    rc, con = matchpathcon('file', 0)
    if rc != 0:
        return "matchpathcon for file failed with rc=%d, errno=%d, strerror=%s" % (rc, get_errno(), os.strerror(get_errno()))

    if cwd != con:
        return "test_matchpathcon failed: cwd != con"

    return None

# Generated at 2022-06-13 00:00:22.872931
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw(b'/usr/bin/python') == [0, "unconfined_u:object_r:usr_t:s0"]
    assert lgetfilecon_raw(b'/bin/bash') == [0, "unconfined_u:object_r:shell_exec_t:s0"]
    assert lgetfilecon_raw(b'/dev/null') == [0, "system_u:object_r:chr_file_t:s0"]
    assert lgetfilecon_raw(b'/invalid-path') == [255, None]

# Generated at 2022-06-13 00:00:27.791440
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    from tempfile import TemporaryDirectory
    from shutil import copy
    from selinux import lsetfilecon

    # Creating a temporary folder to test
    with TemporaryDirectory() as tempdir:
        # Copying /etc/passwd to a temporary folder
        # /etc/passwd is readable by everyone, so the test should
        # work even if the user running the test doesn't have
        # read access to it.
        copy('/etc/passwd', tempdir)
        rc, con = lgetfilecon_raw(tempdir + '/passwd')
        assert rc == 0

    # The temporary folder should be deleted by now
    # and /etc/passwd should be back in it's original state

# Generated at 2022-06-13 00:00:31.713297
# Unit test for function matchpathcon
def test_matchpathcon():
    filesystem_context = matchpathcon('/etc/selinux/config', 0)
    print(filesystem_context)



# Generated at 2022-06-13 00:00:41.986990
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = '/'
    [rc, con] = lgetfilecon_raw(path)
    assert rc == 0
    assert con == 'system_u:object_r:root_t:s0'

    path = '/etc/passwd\0' # Invalid path
    [rc, con] = lgetfilecon_raw(path)
    assert rc == -1
    assert con is None

    path = '/etc/init.d/rc'
    [rc, con] = lgetfilecon_raw(path)
    assert rc == 0
    assert con == 'system_u:object_r:etc_runtime_t:s0'

    path = '/bin/ls'
    [rc, con] = lgetfilecon_raw(path)
    assert rc == 0

# Generated at 2022-06-13 00:00:47.446389
# Unit test for function matchpathcon
def test_matchpathcon():
    import textwrap
    import tempfile

    enforcemode, policytype = selinux_getenforcemode()

    if enforcemode == 0 and policytype != b'kernel':

        context = b'system_u:object_r:selinux_test_t:s0'

        fd, path = tempfile.mkstemp()

# Generated at 2022-06-13 00:00:56.254082
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Ensure lgetfilecon_raw is available
    if getattr(sys.modules[__name__], 'lgetfilecon_raw', None) is None:
        raise OSError('lgetfilecon_raw not available')

    # Obtain the SELinux context for /tmp
    try:
        rc, context = lgetfilecon_raw('/tmp')
    except OSError as e:
        print("Error in lgetfilecon_raw:", e, file=sys.stderr)
        rc = e.errno
    else:
        if rc == -1:
            print("Error in lgetfilecon_raw:", context)
        else:
            print("SELinux context for /tmp:", context)

    # This function does not return anything, it only raises exceptions
    return rc




# Generated at 2022-06-13 00:01:02.738966
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # "getcon(1) -s" is the same as python getcon()
    # context is not assigned at the FS level. it is inherited from the process domain
    # FIXME: this test will fail if the user is not running in the unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023 context
    assert lgetfilecon_raw('/etc') == [0, b''.decode()]
    assert lgetfilecon_raw('/etc/shadow') == [0, b'unconfined_u:object_r:shadow_t:s0'.decode()]



# Generated at 2022-06-13 00:01:08.098983
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import os

    if not is_selinux_enabled():
        return

    testfile = os.getcwd() + "/test.txt"

    if os.path.isfile(testfile):
        rc, con = lgetfilecon_raw(testfile)
        assert rc == 0
    else:
        rc, con = lgetfilecon_raw(testfile)
        assert rc == -1

# Generated at 2022-06-13 00:01:12.763556
# Unit test for function matchpathcon
def test_matchpathcon():
    assert matchpathcon('/foo/bar', 0)[1] == 'system_u:object_r:usr_t:s0'
    assert matchpathcon('/foo/bar', os.R_OK)[1] == 'system_u:object_r:usr_t:s0'
    assert matchpathcon('/foo/bar', os.W_OK)[1] == 'system_u:object_r:usr_t:s0'
    assert matchpathcon('/foo/bar', os.X_OK)[1] == 'system_u:object_r:usr_t:s0'
    assert matchpathcon('/foo/bar', os.R_OK | os.W_OK)[1] == 'system_u:object_r:usr_t:s0'

# Generated at 2022-06-13 00:01:21.495388
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    from ansible.module_utils.selinux import lgetfilecon_raw
    rc, con = lgetfilecon_raw('/etc/selinux/config')
    if rc >= 0:
        assert con == 'system_u:object_r:selinux_etc_t:s0'
    else:
        rc, con = lgetfilecon_raw('/blahblah')
        assert rc == -2
        assert con is None


# Generated at 2022-06-13 00:01:23.675141
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon('/test', 0o600)
    assert rc == 0

# Generated at 2022-06-13 00:01:33.957193
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Create two temp files, one with a context and one without.
    # Verify that we can read the context of the file with one and not the other.
    import tempfile
    import shutil
    import os
    import stat

    # tempfile.mkdtemp() returns the path of the temporary directory, so the
    # directory is created when we move into it.
    with tempfile.TemporaryDirectory() as tmpdirname:
        os.chdir(tmpdirname)
        tmp_nocon_filename = tempfile.mktemp()
        os.close(os.open(tmp_nocon_filename, os.O_CREAT, stat.S_IRWXU))

        rc, con = lgetfilecon_raw(tmp_nocon_filename)

# Generated at 2022-06-13 00:01:36.177823
# Unit test for function matchpathcon
def test_matchpathcon():
    ctx = matchpathcon('/etc/a', 0)
    assert ctx[0] == 0
    assert ctx[1] == 'system_u:object_r:etc_t:s0'

# Generated at 2022-06-13 00:01:41.400468
# Unit test for function matchpathcon
def test_matchpathcon():
    import os

    test_dir = 'test_dir'
    test_context = 'system_u:object_r:httpd_sys_content_t:s0'

    try:
        # Create test directory in /tmp
        os.mkdir(test_dir)
        # Set directory context
        _selinux_lib.matchpathcon(test_dir, 0, None)
        # Get saved context
        rc, con = matchpathcon(test_dir, 0)
        # Check that context was saved
        assert rc == 0
        # Check that context is the same as we set
        assert con == test_context
    finally:
        # Delete test directory
        os.rmdir(test_dir)

# Generated at 2022-06-13 00:01:45.139376
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw('/etc/selinux/config')
    assert(rc == 0)
    assert(con == 'system_u:object_r:etc_runtime_t:s0')

# Generated at 2022-06-13 00:01:52.566898
# Unit test for function matchpathcon
def test_matchpathcon():
    # FIXME: unittest
    # NB: this test will fail unless the module is running in an environment the has the file `/usr/bin/man` with the
    #     correct context.  e.g. if `/usr/bin` is not a filesystem mounted with selinux enabled, this will fail.
    # NB: this test has problems with different selinux policies so try to get a default policy as best as possible.

    # this is a hack but seems to be the best solution for a test that is trying to be generic
    if selinux_getpolicytype()[1] != 'targeted':
        # don't even bother
        return

    rc, con = matchpathcon('/usr/bin/man', 0)
    assert rc == 0
    assert con is not None

# Generated at 2022-06-13 00:01:56.000009
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    curdir = os.path.dirname(__file__)
    path = os.path.join(curdir, 'test_lgetfilecon_raw.py')
    rc_tc, con = lgetfilecon_raw(path)
    assert rc_tc == 0, 'lgetfilecon_raw should return 0 if lgetfilecon success'
    assert con == 'system_u:object_r:usr_t:s0', 'test_lgetfilecon_raw.py should be labeled as usr_t'

# Generated at 2022-06-13 00:01:58.067753
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # should return (0, None) for our test module
    assert lgetfilecon_raw(__file__) == (0, None)

# Generated at 2022-06-13 00:02:02.221416
# Unit test for function matchpathcon
def test_matchpathcon():
    print(matchpathcon('/var/lib/whisker/watchman', os.R_OK))
    print(matchpathcon('/var/lib/whisker/watchman', os.R_OK | os.W_OK))


if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-13 00:02:11.661874
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    con = c_char_p()
    try:
        rc = _selinux_lib.lgetfilecon_raw("/usr/bin", byref(con))
        assert rc == 0
        assert con.value is not None
        assert to_native(con.value) is not None
    finally:
        _selinux_lib.freecon(con)


# Generated at 2022-06-13 00:02:16.401378
# Unit test for function matchpathcon
def test_matchpathcon():
    (rc, con) = matchpathcon('/var/tmp/test', os.R_OK)
    assert rc == 0
    assert con == 'system_u:object_r:user_tmp_t:s0'



# Generated at 2022-06-13 00:02:25.392006
# Unit test for function matchpathcon
def test_matchpathcon():
    proposed = "system_u:object_r:user_home_dir_t:s0"
    path = "/home/user"
    print("Proposed for path %s is %s" % (path, proposed))
    rc, con = matchpathcon(path, 0)
    print("Con for path %s is %s" % (path, con))
    assert proposed == con
    return

if __name__ == '__main__':
    rc = test_matchpathcon()
    sys.exit(rc)

# Generated at 2022-06-13 00:02:28.958429
# Unit test for function matchpathcon
def test_matchpathcon():
    (rc, con) = matchpathcon('/tmp', os.R_OK | os.W_OK | os.X_OK)
    assert rc == 0
    assert con.startswith('system_u:object_r:tmp_t')

    (rc, con) = matchpathcon('/tmp/.invalid/file', os.R_OK | os.W_OK | os.X_OK)
    assert rc == -1
    assert rc == get_errno()

    (rc, con) = matchpathcon('/tmp', 255)
    assert rc == 0
    assert con.startswith('system_u:object_r:tmp_t')

# Generated at 2022-06-13 00:02:39.073163
# Unit test for function matchpathcon
def test_matchpathcon():
    match = None
    mode = None
    [rc, match] = matchpathcon("/home/allen", 0)
    if rc:
        print("matchpathcon for /home/allen failed")
    else:
        print("matchpathcon for /home/allen succeeded, context is: ", match)
    [rc, match] = matchpathcon("/home/allen", 32777)
    if rc:
        print("matchpathcon for /home/allen failed")
    else:
        print("matchpathcon for /home/allen succeeded, context is: ", match)
    [rc, match] = matchpathcon("/home/allen", 3)
    if rc:
        print("matchpathcon for /home/allen failed")

# Generated at 2022-06-13 00:02:42.597149
# Unit test for function matchpathcon
def test_matchpathcon():
    if security_policyvers() >= 24:
        rc, con = matchpathcon('/home/user1/tmp', 0)
        assert rc == 0
        assert con == 'tmp_t:object_r:user_home_t:s0'



# Generated at 2022-06-13 00:02:46.739231
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(
        argument_spec=dict(path=dict(type='str'))
    )
    path = module.params.get('path')
    rc, con = lgetfilecon_raw(path)
    module.exit_json(changed=False, ansible_module_results={'rc': rc, 'con': con})



# Generated at 2022-06-13 00:02:49.386959
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = '/tmp'
    result = lgetfilecon_raw(path)
    assert result[0] == 0
    assert result[1] is not None



# Generated at 2022-06-13 00:02:51.393507
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import tempfile
    import os
    import os.path

    (fd, path) = tempfile.mkstemp()
    os.close(fd)
    try:
        rc, out = lgetfilecon_raw(path)
        assert isinstance(out, str)
    finally:
        os.unlink(path)

# Generated at 2022-06-13 00:02:55.701140
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = b'/etc/init.d/ansible-test'
    [rc, con] = lgetfilecon_raw(path)
    print(rc, con)
    assert rc == 0
    assert con == 'system_u:object_r:role_t:s0'

# Generated at 2022-06-13 00:03:02.099130
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = '/etc/hosts'
    rc, con = lgetfilecon_raw(path)
    print("path={0} rc={1} con={2}".format(path, rc, con))
    assert rc == 0
    assert con == "unconfined_u:object_r:etc_t:s0"



# Generated at 2022-06-13 00:03:06.255482
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    file="./foobar.txt"
    with open(file, 'w') as f:
        f.write("hello foobar")
    try:
        result = lgetfilecon_raw(file)
        assert result[0] == 0
    finally:
        os.remove(file)

# Generated at 2022-06-13 00:03:09.402419
# Unit test for function matchpathcon
def test_matchpathcon():
    '''
    Function matchpathcon returns status 0 for success.
    '''
    path = '/etc/passwd'
    mode = 0
    assert matchpathcon(path, mode)[0] == 0

# Generated at 2022-06-13 00:03:12.292954
# Unit test for function matchpathcon
def test_matchpathcon():
    # Check that the wrapper matches the example from the man pages
    (rc, con) = matchpathcon("/etc/passwd", 0)
    assert rc == -1 and con == "system_u:object_r:etc_runtime_t:s0"

# Generated at 2022-06-13 00:03:14.676129
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Check that the return code is negative in case of an invalid path
    invalid_path = "/abc/"
    rc, _ = lgetfilecon_raw(invalid_path)
    assert rc < 0

    # Check that the return code is zero in case of a valid path
    rc, _ = lgetfilecon_raw("/etc/passwd")
    assert rc == 0

if __name__ == "__main__":
    test_lgetfilecon_raw()

# Generated at 2022-06-13 00:03:18.072834
# Unit test for function matchpathcon
def test_matchpathcon():
    path = b'/etc/shadow'
    mode = 0o0400
    [rc, con] = matchpathcon(path, mode)
    assert rc == 0
    assert con == 'shadow:object_r:shadow_t:s0'
    return con


if __name__ == '__main__':
    print(test_matchpathcon())

# Generated at 2022-06-13 00:03:25.480651
# Unit test for function matchpathcon
def test_matchpathcon():
    print("testing matchpathcon")
    import os
    import tempfile
    s = os.stat('/tmp')
    print(s.st_mode)
    mode = s.st_mode
    # Ensure the mode is what we think it is
    assert mode == 16877
    # Try to pass a number to an arg that expects a string
    try:
      rc, con = matchpathcon(12345, mode)
      # We shouldn't get here, because the above line should cause an exception
      raise Exception('Unexpected success')
    except TypeError as e:
      print(e)
      # Make sure the error is what we expect
      assert str(e) == 'must be str, not int'
    # Try to pass a number to an arg that expects a number

# Generated at 2022-06-13 00:03:32.728841
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    def _test(path, con):
        try:
            from selinux.selinux import lgetfilecon
            rc, l_con = lgetfilecon(path)
            assert con == l_con
        except ImportError:
            assert not os.path.exists(path)

    _test('/etc/shadow', 'system_u:object_r:shadow_t:s0')
    _test('/etc/passwd', 'system_u:object_r:etc_t:s0')
    _test('/', 'system_u:object_r:root_t:s0')
    _test('/non-existent-path', '')



# Generated at 2022-06-13 00:03:37.720925
# Unit test for function matchpathcon
def test_matchpathcon():
    path = "path/to/file"
    mode = 1

    rc, con = matchpathcon(path, mode)
    assert rc == 0, "matchpathcon failed"
    assert type(con) == str, "matchpathcon failed"



# Generated at 2022-06-13 00:03:46.398977
# Unit test for function matchpathcon
def test_matchpathcon():
    from ansible.module_utils import basic
    from ansible.module_utils.six.moves.mock import patch
    from ansible.module_utils.six import PY2

    with patch('ansible.module_utils.selinux.matchpathcon') as mock_matchpathcon:
        basic._ANSIBLE_ARGS = None
        with patch.dict(os.environ, {'ANSIBLE_MODULE_ARGS': '{"arg1": "val1"}'}):
            basic._ANSIBLE_ARGS = basic.AnsibleModuleArgumentParser().parse_args()

        module = basic.AnsibleModule(
            argument_spec={'arg1': {'type': 'str', 'required': True}}
        )


# Generated at 2022-06-13 00:03:53.402465
# Unit test for function matchpathcon
def test_matchpathcon():
    import tempfile
    tmpfile = tempfile.NamedTemporaryFile()
    try:
        assert matchpathcon(tmpfile.name, 0)
    finally:
        tmpfile.close()

# Generated at 2022-06-13 00:03:55.549075
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw('/etc') == [0, 'system_u:object_r:etc_t:s0']



# Generated at 2022-06-13 00:04:00.410971
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Test for a common file
    path = "/etc/passwd"
    assert lgetfilecon_raw(path) == [0, 'unconfined_u:object_r:user_home_t:s0']

    # Test for a nonexistant file
    path = "/etc/doesnotexist"
    assert lgetfilecon_raw(path) == [-1, '']



# Generated at 2022-06-13 00:04:08.759465
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    '''Test the function lgetfilecon_raw'''
    # only run the test if libselinux is available
    try:
        _selinux_lib
    except NameError:
        return

    # this test is unit tested in Ansible itself
    if sys.modules['__main__'].__package__ == 'ansible.module_utils.selinux':
        return

    (rc, con) = lgetfilecon_raw('/')
    assert rc == 0

    (rc, con) = lgetfilecon_raw('/nonexistent')
    assert rc != 0


# Generated at 2022-06-13 00:04:10.478216
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw('/') == [0, 'system_u:object_r:root_t:s0']

# Generated at 2022-06-13 00:04:20.267234
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = b'/etc'
    try:
        ret, con = lgetfilecon_raw(b'nothere')
        assert ret == -1
    except:
        pass
    try:
        ret, con = lgetfilecon_raw(path)
        assert ret == 0
        assert con == "_"
    except:
        pass
    path = b"/dev/null"
    try:
        ret, con = lgetfilecon_raw(path)
        assert ret == 0
        assert con == "system_u:object_r:null_device_t:s0"
    except:
        pass

# Generated at 2022-06-13 00:04:23.855226
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    con = c_char_p()
    rc = _selinux_lib.lgetfilecon_raw(to_bytes('/bin/ls'), byref(con))
    print('Return code = {} file context = {}'.format(rc, to_native(con.value)))
    _selinux_lib.freecon(con)


# Generated at 2022-06-13 00:04:30.137542
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    con = c_char_p()
    rc = _selinux_lib.lgetfilecon_raw('/usr/bin/python3', byref(con))
    assert rc == 0, 'lgetfilecon_raw returned failure'
    assert to_native(con.value) == 'python3_exec_t', 'Context did not match'
    _selinux_lib.freecon(con)


# Generated at 2022-06-13 00:04:40.577318
# Unit test for function matchpathcon
def test_matchpathcon():
    def assert_matchpathcon(path, mode, expected_rc, expected_con=None):
        result = matchpathcon(path, mode)
        assert result[0] == expected_rc
        if expected_rc == 0:
            assert result[1] == expected_con

    assert_matchpathcon('/etc/systemd/system', os.R_OK, 0, 'system_u:object_r:etc_t:s0')
    assert_matchpathcon('/sys', os.W_OK, 0, 'root:object_r:fs_type_devtmpfs_t:s0')
    assert_matchpathcon('/root', os.X_OK, 1)  # error


del to_native, to_bytes, CDLL, c_char_p, c_int, byref, POINTER, get_err

# Generated at 2022-06-13 00:04:47.354092
# Unit test for function matchpathcon
def test_matchpathcon():
    import glob
    import time
    import tempfile

    def _create_files(files):
        for fname in files:
            try:
                with open(fname, 'w') as fd:
                    fd.write('hello world')
            except Exception as exc:
                raise Exception('failed to create {0}: {1}'.format(fname, exc))

    def _validate_file_contexts(files):
        for fname in files:
            try:
                rc, context = matchpathcon(fname, 0)
            except Exception as exc:
                raise Exception('failed to get context on {0}: {1}'.format(fname, exc))

            if rc:
                raise Exception('failed to get context on {0}: {1}'.format(fname, rc))


# Generated at 2022-06-13 00:04:59.687842
# Unit test for function matchpathcon
def test_matchpathcon():
    # test with a path that does not exist
    rc, result = matchpathcon('/ansible/does/not/exist/path', 0)
    print(rc, result)
    print('')

    # test with a valid path and mode (octal)
    rc, result = matchpathcon('/bin/bash', 0o755)
    print(rc, result)
    print('')

    # test with a valid path and mode
    rc, result = matchpathcon('/bin/bash', 493)
    print(rc, result)
    print('')



# Generated at 2022-06-13 00:05:02.335318
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw(b'/etc/passwd') == [0, 'system_u:object_r:etc_runtime_t:s0']



# Generated at 2022-06-13 00:05:07.541571
# Unit test for function matchpathcon
def test_matchpathcon():
    """
    Test to see if it can match the path.
    """
    module_failed = False
    path = "/var/log/messages"
    mode = 0
    try:
        rc, context = matchpathcon(path, mode)
    except OSError:
        module_failed = True
    if module_failed:
        print("Unable to match path, error occurred")



# Generated at 2022-06-13 00:05:13.263401
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import os, sys, stat
    import tempfile
    import subprocess
    import ctypes

    def _check_rc(rc):
        if rc < 0:
            errno = get_errno()
            raise OSError(errno, os.strerror(errno))
        return rc

    def _module_setup():

        class _to_char_p:
            @classmethod
            def from_param(cls, strvalue):
                if strvalue is not None and not isinstance(strvalue, binary_char_type):
                    strvalue = to_bytes(strvalue)

                return strvalue

        con = c_char_p()
        rc = _selinux_lib.lgetfilecon_raw("/etc/trace/events/net.txt", byref(con))

# Generated at 2022-06-13 00:05:18.886656
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = b'/etc/resolv.conf'
    (rc, con) = lgetfilecon_raw(path)
    assert rc == 0
    assert con == b'unconfined_u:object_r:etc_t:s0'


# Generated at 2022-06-13 00:05:19.973891
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw(b'/') == [0, 'system_u:object_r:root_t:s0\0']


# Generated at 2022-06-13 00:05:24.510720
# Unit test for function matchpathcon
def test_matchpathcon():
    """
    When selinux is disabled or not present, return an error
    """
    if not is_selinux_enabled():
        rc, con = matchpathcon('/etc/passwd', 0)
        assert rc == -1
        # On some systems (e.g. Fedora 30 armv7l) this is a string, not an int
        assert isinstance(get_errno(), (type(None), int, str))

# Generated at 2022-06-13 00:05:34.826960
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    """
    :return:
    """
    if not isinstance(_selinux_lib, CDLL):
        raise ImportError("lgetfilecon_raw: unable to load libselinux.so")
    con = c_char_p()
    path = b"/tmp/test"
    try:
        rc = _selinux_lib.lgetfilecon_raw(path, byref(con))
        return [rc, to_native(con.value)]
    finally:
        _selinux_lib.freecon(con)

# Generated at 2022-06-13 00:05:40.828499
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw(b'/proc')[1] == b'unlabeled'
    assert lgetfilecon_raw(b'/proc/self/fd')[1] == b'system_u:object_r:proc_fd_t:s0'
    assert lgetfilecon_raw(b'/proc/self/fdinfo')[1] == b'unlabeled'



# Generated at 2022-06-13 00:05:47.090485
# Unit test for function matchpathcon
def test_matchpathcon():

    # the lxcfs pseudo-filesystem has the following base security context
    # type: lxcfs_t, seuser: system_u, level: s0

    path_to_test = "/sys/fs/cgroup/memory/lxc"
    mode = 0

    rc, context = matchpathcon(path_to_test, mode)

    if rc != 0:
        raise Exception('matchpathcon failed with rc %d' % rc)
    else:
        print('matchpathcon returned context: %s' % context)

# Generated at 2022-06-13 00:06:00.848958
# Unit test for function matchpathcon
def test_matchpathcon():
    # Without SELinux support, assertion will fail
    assert matchpathcon("/", 0)[0] == 0

# Generated at 2022-06-13 00:06:03.253459
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    r = lgetfilecon_raw('/etc/passwd')
    assert r == [0, 'system_u:object_r:etc_t:s0']



# Generated at 2022-06-13 00:06:07.636709
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    """Simple test for function lgetfilecon_raw"""
    try:
        # Ensure that / exists and that it has a security context
        rc, con = lgetfilecon_raw('/')
        assert rc == 0
        assert con is not None
    except ImportError:
        pass
    except NotImplementedError:
        pass
    except OSError:
        pass


# Generated at 2022-06-13 00:06:13.054892
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # This test is only for python3
    if sys.version_info.major < 3:
        return
    # non-root user
    try:
        rc, con = lgetfilecon_raw(b'/')
    except Exception as e:
        if 'Operation not permitted' in str(e):
            return
    if rc == 0:
        assert con.startswith('system_u')

# Generated at 2022-06-13 00:06:18.734524
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # We expect that this function raises an OSError for an invalid file path.
    # This is detected when we compare rc with 0.
    # If we do not get an exception or if the rc is not negative and less than 0
    # then the test fails.
    try:
        rc, con = lgetfilecon_raw("/invalidpath")
        if rc < 0:
            return True
        return False
    except OSError:
        return True
    return False


# Generated at 2022-06-13 00:06:25.462768
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import tempfile
    ok_con = 'system_u:object_r:usr_t:s0'

    with tempfile.TemporaryDirectory() as tmpdir:
        # Cannot set file con for tmpdir, so create a subdir to work with
        subdir = os.path.join(tmpdir, 'subdir')
        os.mkdir(subdir)

        try:
            err, con = lgetfilecon_raw(subdir)
            if err == -1:
                raise AssertionError('unable to get file con for {0}'.format(subdir))
            if con != ok_con:
                raise AssertionError('file con for {0} does not match expected value: got "{1}", expected "{2}"'.format(subdir, con, ok_con))
        finally:
            os.rmd

# Generated at 2022-06-13 00:06:38.026202
# Unit test for function matchpathcon
def test_matchpathcon():
    # pylint: disable=unused-variable
    if sys.platform == 'darwin':
        raise AssertionError('Test not supported on this platform')

# Generated at 2022-06-13 00:06:43.825860
# Unit test for function matchpathcon
def test_matchpathcon():
    is_selinux_enabled = selinux_enabled()
    if not is_selinux_enabled:
        return
    is_selinux_mls_enabled = selinux_mls_enabled()
    [rc, con] = matchpathcon('/etc/shadow', 0)
    assert con == 'system_u:object_r:shadow_t:s0' or con == 'system_u:object_r:shadow_t:s0:c0.c1023'

# Generated at 2022-06-13 00:06:53.933809
# Unit test for function matchpathcon
def test_matchpathcon():
    import tempfile
    from os import mkdir
    from os.path import join
    from shutil import rmtree
    from contextlib import contextmanager

    @contextmanager
    def temp_dir(*args, **kwargs):
        try:
            temp_dir = tempfile.mkdtemp(*args, **kwargs)
            yield temp_dir
        finally:
            rmtree(temp_dir)

    def test_context(path, context):
        with temp_dir() as temp_dir:
            path = join(temp_dir, path)
            mkdir(path)
            rc, con = matchpathcon(path, 0)
            assert rc == 0
            assert con == context

    # test cwd
    cwd_context = "system_u:object_r:tmp_t:s0"
    test_context

# Generated at 2022-06-13 00:07:01.608341
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    """Test lgetfilecon_raw() returns the correct values for a directory and a file
    """
    path = "/usr/lib"
    tmp_file = "/etc/sysconfig/network-scripts/ifcfg-eth0"
    dir_result = '/usr/lib(/.*)? system_u:object_r:lib_t:s0'
    file_result = '/etc/sysconfig/network-scripts/ifcfg-eth0 system_u:object_r:etc_runtime_t:s0'
    if sys.version_info[0] == 2:
        dir_result = dir_result.decode('utf-8')
        file_result = file_result.decode('utf-8')
    dir_result = [0, dir_result]
    file_result = [0, file_result]
    assert l

# Generated at 2022-06-13 00:07:26.800852
# Unit test for function matchpathcon
def test_matchpathcon():
    # first check that it creates a file with the correct context
    file = "/tmp/foo"
    os.remove(file)
    f = open(file, 'w')
    f.close()
    (rc, con) = matchpathcon(file, 0o644)
    assert rc == 0
    assert con == "system_u:object_r:user_tmp_t"
    os.remove(file)

# Generated at 2022-06-13 00:07:29.552434
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    result = lgetfilecon_raw(b'/etc/selinux/targeted/policy/policy.29')
    assert result[1] == b'system_u:object_r:etc_t:s0'

# Generated at 2022-06-13 00:07:35.339324
# Unit test for function matchpathcon
def test_matchpathcon():
    path = '/home/joe/foo'

# Generated at 2022-06-13 00:07:37.562408
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = '/etc/issue'
    [rc, con] = lgetfilecon_raw(path)
    assert rc==0
    assert len(con) > 0


# Generated at 2022-06-13 00:07:41.287404
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = b'/etc/shadow'
    if os.path.exists(path):
        enable = is_selinux_enabled()
        if enable:
            rc, con = lgetfilecon_raw(path)
            return con
        else:
            return 'SELinux is disabled.'
    else:
        return 'The path is invalid.'


# Generated at 2022-06-13 00:07:44.271384
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import json
    import pprint
    from ansible.module_utils import basic

    path = b'/tmp/ansible_test_file'
    open(path, 'w').close()
    try:
        pprint.pprint(lgetfilecon_raw(path))
    finally:
        os.unlink(path)


if __name__ == '__main__':
    test_lgetfilecon_raw()

# Generated at 2022-06-13 00:07:47.352282
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = "file.txt"
    con = c_char_p()
    rc = 0
    rc = lgetfilecon_raw(path)
    assert rc[0] == 0
    print(rc[1])


# Generated at 2022-06-13 00:07:49.464449
# Unit test for function matchpathcon
def test_matchpathcon():
    path = 'nevergonnagiveyouup'
    mode = 1
    [rc, con] = matchpathcon(path, mode)
    print(rc, con)



# Generated at 2022-06-13 00:07:53.386980
# Unit test for function matchpathcon
def test_matchpathcon():
    _selinux_lib.matchpathcon.argtypes = [c_char_p, c_int, POINTER(c_char_p)]
    # For this test to succeed, /tmp must be labeled with a valid context
    rc, con = matchpathcon('/tmp', 0)
    assert rc == 0
    assert con == "system_u:object_r:tmpfs:s0"

# Generated at 2022-06-13 00:07:55.653541
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Functionality tests are in test/unit/modules/core/unit/test_selinux.py
    assert isinstance(lgetfilecon_raw('/'), list)

# Generated at 2022-06-13 00:08:43.902056
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w') as f:
        path = f.name
    try:
        rc, res = lgetfilecon_raw(path)
        assert rc == 0
        assert 'system_u' in res
    finally:
        os.remove(path)



# Generated at 2022-06-13 00:08:46.323906
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    filename = '/etc/shadow'
    rc, con = lgetfilecon_raw(filename)
    assert rc >= 0
    print('con: %s' % con)
    assert con[:8] == 'unconfined'


# Generated at 2022-06-13 00:08:51.523694
# Unit test for function matchpathcon
def test_matchpathcon():
    test_file = 'ansible.cfg'
    # Execute the function and save the output
    output = matchpathcon(test_file, 0o400)

    rc = output[0]
    con = output[1]

    # Check to see if rc is 0 (successful)
    assert rc == 0

    # Check to see if output matches a known SELinux mode
    assert con in ('user_home_t', 'user_home_t:s0')

# Generated at 2022-06-13 00:08:54.626573
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    context = lgetfilecon_raw('/etc/passwd')
    assert context[0] == 0
    assert context[1] == 'system_u:object_r:etc_runtime_t:s0'



# Generated at 2022-06-13 00:08:58.109198
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = b'/tmp/testfile'
    if not os.path.exists(path):
        import tempfile
        tempfile.mkstemp(prefix='testfile', dir=b'/tmp')
    rc, con = lgetfilecon_raw(path)
    assert con is not None
    assert rc == 0


# Generated at 2022-06-13 00:09:00.341666
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = '/tmp'
    rc, con = lgetfilecon_raw(path)
    assert rc != -1
    assert con is not None


# Generated at 2022-06-13 00:09:07.846777
# Unit test for function matchpathcon
def test_matchpathcon():
    import tempfile

    testdir = tempfile.mkdtemp(prefix="ansible-test-")
    testfile = testdir + '/matchpathcon_test'
    with open(testfile, "w") as f:
        f.write("")
    [rc, con] = matchpathcon(testfile, os.R_OK)
    assert rc == 0
    assert con == '(system_u:object_r:default_t:s0)'
    with open(testfile, "w") as f:
        f.write("testdata")
    [rc, con_write] = matchpathcon(testfile, os.W_OK)
    assert rc == -1
    assert con_write == ""
    [rc, con_read] = matchpathcon(testfile, os.R_OK)
    assert rc == 0
