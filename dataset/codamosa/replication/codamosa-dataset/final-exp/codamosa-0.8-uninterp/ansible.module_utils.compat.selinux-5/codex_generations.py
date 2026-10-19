

# Generated at 2022-06-12 23:59:11.423086
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (rc, value) = lgetfilecon_raw(b'/usr/bin/env')
    assert rc == 0
    assert value == 'unconfined_u:object_r:usr_t:s0'


# Generated at 2022-06-12 23:59:20.472366
# Unit test for function matchpathcon
def test_matchpathcon():
    if not is_selinux_enabled():
        return

    # If a file exists, the outcome of matchpathcon should be 0
    if os.path.isfile('/etc/passwd'):
        rc, _ = matchpathcon('/etc/passwd', 0)
        _assert_rc(rc)

    # If a file does not exist, the outcome of matchpathcon should be -1
    if not os.path.isfile('/etc/passwd'):
        rc, _ = matchpathcon('/etc/passw', 0)
        assert rc == -1



# Generated at 2022-06-12 23:59:24.453877
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    test_path = '/var/run/nscd/socket'
    result = lgetfilecon_raw(test_path)
    assert result[0] == 0
    assert result[1] == "system_u:object_r:nscd_var_run_t:s0"


# Generated at 2022-06-12 23:59:25.826894
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    __module__.lgetfilecon_raw(__file__)



# Generated at 2022-06-12 23:59:28.450192
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw('/etc/fstab')
    assert rc == 0
    print(con)
    return rc, con



# Generated at 2022-06-12 23:59:30.852432
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw('/etc')[1] == 'system_u:object_r:etc_t:s0'


# Generated at 2022-06-12 23:59:36.906482
# Unit test for function matchpathcon
def test_matchpathcon():

    # verify the function returns a tuple of two values, the first being an
    # integer value representing an error (0 => no error) and the second
    # being a string representing the security context of the file path
    (err, context) = matchpathcon('/usr/bin/passwd', 0)
    assert err == 0 and context == 'system_u:object_r:usr_t:s0'

    # now verify that the security context is not returned when an invalid path
    # is specified
    (err, context) = matchpathcon('/tmp/doesnotexist', 0)
    assert err == -1 and context == ''



# Generated at 2022-06-12 23:59:38.758913
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw("/etc") == [0, b"system_u:object_r:etc_t:s0"]



# Generated at 2022-06-12 23:59:44.656522
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # In the test we will check the library call with non-existing file
    # if it return an error
    path = b'/test/linux/test_file.txt'
    rc, con = lgetfilecon_raw(path)
    if rc > -1:
        raise OSError
    elif rc < 0:
        # We expect an error so nothing to do.
        pass

# Generated at 2022-06-12 23:59:53.382348
# Unit test for function matchpathcon
def test_matchpathcon():
    assert matchpathcon('/etc/protocols', 0) == [2, 'system_u:object_r:etc_t:s0']
    assert matchpathcon('/etc/protocols', S_IFDIR) == [2, 'system_u:object_r:etc_t:s0']
    assert matchpathcon('/etc/protocols', S_IFREG) == [0, 'system_u:object_r:etc_t:s0']
    assert matchpathcon('/etc/protocols', S_IFLNK) == [3, 'system_u:object_r:etc_t:s0']
    assert matchpathcon('/etc/protocols', S_IFSOCK) == [0, 'system_u:object_r:etc_t:s0']
    assert matchpathcon

# Generated at 2022-06-12 23:59:58.926369
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = b"/sys/firmware/efi/efivars/dump-type-information-*"
    (rc, con) = lgetfilecon_raw(path)
    assert rc == 0


# Generated at 2022-06-13 00:00:03.353574
# Unit test for function matchpathcon
def test_matchpathcon():
    """Test matchpathcon function
    """
    (rc, con) = matchpathcon('/etc/passwd', 0)
    assert rc == 0
    assert con is not None
    (rc, con) = matchpathcon('/etc/passwd', 0o0400)
    assert rc == 0
    assert con is not None
    (rc, con) = matchpathcon('/etc/passwd', 0o0600)
    assert rc == 0
    assert con is not None
    (rc, con) = matchpathcon('/etc/passwd', 0o0000)
    assert rc == -1
    assert con is None
    (rc, con) = matchpathcon('/etc/passwd', 0o0200)
    assert rc == -1
    assert con is None

# Generated at 2022-06-13 00:00:05.917232
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = b"/usr/bin/id"
    rc, con = lgetfilecon_raw(path)
    assert con == "system_u:object_r:shell_exec_t:s0"

# Generated at 2022-06-13 00:00:07.933383
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    test_path = sys.argv[0]
    return lgetfilecon_raw(test_path)



# Generated at 2022-06-13 00:00:16.037532
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    """
    Used in unit test module selinux_tools
    """
    if is_selinux_enabled() == 0:
        raise AssertionError('Selinux is disabled')

    # Print stat for a file when selinux is enabled
    [rc, con] = lgetfilecon_raw('/bin/ls')

    print(rc)
    print(con)
    if rc != 0:
        raise AssertionError('Could not get the context of /bin/ls')
    if con is None:
        raise AssertionError('Context of /bin/ls is null')
    print('Success')



# Generated at 2022-06-13 00:00:20.494345
# Unit test for function matchpathcon
def test_matchpathcon():
    path = '/home/user/file.txt'
    mode = os.R_OK
    rc, con = matchpathcon(path, mode)
    print('{0} for path "{1}" has rc "{2}" and con "{3}"'.format(os.strerror(rc), path, rc, con))


if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-13 00:00:26.799119
# Unit test for function matchpathcon

# Generated at 2022-06-13 00:00:32.812825
# Unit test for function matchpathcon
def test_matchpathcon():

    import os
    from ansible.module_utils.common.text.converters import to_bytes
    import tempfile

    path = "/tmp/test_matchpathcon"
    path_bytes = to_bytes(path)

    try:
        os.mkdir(path)
    except OSError:
        pass

    mode = 0
    rc, con = matchpathcon(path_bytes, mode)
    print('path: {0}'.format(path_bytes))
    print('mode: {0}'.format(mode))
    print('rc: {0}'.format(rc))
    print('con: {0}'.format(con))
    assert rc == 0

    mode = 1
    rc, con = matchpathcon(path_bytes, mode)

# Generated at 2022-06-13 00:00:42.671147
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import stat
    from ansible_collections.ansible.selinux.plugins.module_utils.selinux import selinux_getenforcemode
    from ansible_collections.ansible.selinux.plugins.module_utils.selinux import lgetfilecon_raw
    if selinux_getenforcemode()[0] == 1:
        file = "selinux.py"
        path = ("/usr/lib/python3.6/site-packages/ansible_collections/ansible/selinux/plugins/"
                "module_utils/")
        mode = 0o777
        mode_type = stat.S_IFREG
        mode_perm = mode | mode_type
        (rc, out) = lgetfilecon_raw(path + file)

# Generated at 2022-06-13 00:00:44.831472
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Test on file or directory
    rc, value = lgetfilecon_raw(b'/etc/passwd')
    assert rc == 0 and value == b'unconfined_u:object_r:default_t:s0'


# Generated at 2022-06-13 00:00:52.084313
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    result = lgetfilecon_raw('/tmp')
    assert isinstance(result, list)
    assert len(result) == 2
    assert isinstance(result[0], int)
    assert isinstance(result[1], str)
    assert result[0] == 0
    assert result[1] == 'system_u:object_r:tmp_t:s0'



# Generated at 2022-06-13 00:00:58.103682
# Unit test for function matchpathcon
def test_matchpathcon():
    import tempfile
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.selinux import matchpathcon

    path = tempfile.mktemp()
    with open(path, 'w') as f:
        f.write('hello world')

    argspec = dict(
        path=dict(required=True, type='str', default=None),
        level=dict(required=False, type='int', default=0),
    )

    module = AnsibleModule(argument_spec=argspec, supports_check_mode=True)

    rc, con = matchpathcon(path, 1)
    os.unlink(path)
    if rc == 0 and con is not None:
        module.exit_json(changed=False, msg=con)
    else:
        module.fail_json

# Generated at 2022-06-13 00:01:01.211136
# Unit test for function matchpathcon
def test_matchpathcon():
    try:
        _selinux_lib.matchpathcon('/abc', 0, 0)
    except OSError as e:
        if e.errno == 22:
            pass
        else:
            raise
    except:
        raise
    return 'success'

# Generated at 2022-06-13 00:01:05.498612
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (rc, con) = lgetfilecon_raw(b'/etc/passwd')
    assert rc == 0
    assert con == 'system_u:object_r:passwd_file_t:s0'



# Generated at 2022-06-13 00:01:10.649137
# Unit test for function matchpathcon
def test_matchpathcon():
    import stat
    import os
    import tempfile

    # FIXME: this is probably not the right way to test this
    # Note that this fails on SELinux disabled testbuilds
    # Note that this only works on systems with a fully functional selinux
    # Note that this only works on proper filesystems
    # On a system with *no* selinux this returns rc>=0 and an empty string
    # On a system with selinux but no policy loaded this returns rc=0 and an empty string

    # try to find a context from the root of a filesystem
    context = None
    for root, dirs, files in os.walk('/'):
        for filename in files:
            fullpath = os.path.join(root, filename)
            st = os.lstat(fullpath)

# Generated at 2022-06-13 00:01:13.053686
# Unit test for function matchpathcon
def test_matchpathcon():
    test_path = '/tmp/test'
    mode = 0
    rc, con = matchpathcon(test_path, mode)
    assert rc == -1
    assert con is None

# Generated at 2022-06-13 00:01:14.253774
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    from ansible.module_utils.selinux import lgetfilecon_raw
    rc, con = lgetfilecon_raw(b'/')
    assert rc == 0, "Unable to determine /'s context"

# Generated at 2022-06-13 00:01:18.851308
# Unit test for function matchpathcon
def test_matchpathcon():
    # Make sure this exists for testing
    assert os.path.isdir('/usr/bin')
    expected_rc = 0
    expected_con = 'system_u:object_r:bin_t:s0'
    matchpathcon_result = matchpathcon('/usr/bin', 0)
    assert matchpathcon_result[0] == expected_rc
    assert matchpathcon_result[1] == expected_con

if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-13 00:01:26.310475
# Unit test for function matchpathcon
def test_matchpathcon():
    print("Testing matchpathcon")

    # Test with file that exists
    ret = matchpathcon("/etc/hosts", os.R_OK)
    assert ret == [0, "system_u:object_r:etc_t:s0"], "Testing with file that exists"

    # Test with file that doesn't exist
    ret = matchpathcon("/var/hosts", os.R_OK)
    assert ret == [0, "system_u:object_r:var_t:s0"], "Testing with file that doesn't exist"

    # Test with bad path
    ret = matchpathcon("/etc/hostssssssssssssssssssssssssssssssss", os.R_OK)
    assert ret[0] == -1, "Testing with bad path"


# Generated at 2022-06-13 00:01:30.667557
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    err, con = lgetfilecon_raw("/etc/hosts")
    print("Error: {0}".format(err))
    print("Con: {0}".format(con))


if __name__ == "__main__":
    test_lgetfilecon_raw()

# Generated at 2022-06-13 00:01:39.828895
# Unit test for function matchpathcon
def test_matchpathcon():
    # Test support for glob-like patterns in pathnames
    [rc, con] = matchpathcon('/var/lib', 0)
    assert rc == 0
    [rc, con] = matchpathcon('/var/lib?', 0)
    assert rc == 0
    [rc, con] = matchpathcon('/var/lib??', 0)
    assert rc == 0
    [rc, con] = matchpathcon('/var/lib???', 0)
    assert rc == 0
    [rc, con] = matchpathcon('/var/lib????', 0)
    assert rc == 0
    [rc, con] = matchpathcon('/var/lib[', 0)
    assert rc < 0
    [rc, con] = matchpathcon('/var/lib]', 0)
    assert rc < 0

# Generated at 2022-06-13 00:01:41.562913
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw('/etc/passwd') == [0, 'system_u:object_r:etc_runtime_t:s0']


# Generated at 2022-06-13 00:01:51.278836
# Unit test for function matchpathcon

# Generated at 2022-06-13 00:01:57.427136
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    ret, file_context = lgetfilecon_raw(b'/usr/bin/python')
    assert ret == 0
    assert isinstance(file_context, str)
    assert file_context.split(':')[0] == 'system_u'


# Generated at 2022-06-13 00:02:02.932609
# Unit test for function matchpathcon
def test_matchpathcon():
    # Test correct label
    path = 'foo'
    mode = os.R_OK
    rc, con = matchpathcon(path, mode)
    assert rc < 0, 'matchpathcon failed with valid parameters'
    assert con is None, 'matchpathcon is not returning None'

    # Test invalid argument
    rc, con = matchpathcon('', mode)
    assert rc >= 0, 'matchpathcon failed with invalid parameters'
    assert con is None, 'matchpathcon is not returning None'

# Generated at 2022-06-13 00:02:06.363948
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import tempfile

    tf = tempfile.NamedTemporaryFile()
    rc, con = lgetfilecon_raw(tf.name)
    assert rc == 0 and con.startswith("unconfined_u")

# Generated at 2022-06-13 00:02:12.454066
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw('/etc/resolv.conf')
    if rc != 0:
        raise OSError(rc, os.strerror(rc))
    print(con)


if __name__ == "__main__":
    test_lgetfilecon_raw()

# Generated at 2022-06-13 00:02:16.069662
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    sys.stderr.write('Testing the function selinux.lgetfilecon_raw(path):\n')

    rc, con = lgetfilecon_raw('/bin/ls')
    sys.stderr.write('Return Code: %d\n' % rc)
    sys.stderr.write('Con: %s\n' % con)



# Generated at 2022-06-13 00:02:22.437509
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = b'/tmp'
    rc, con = lgetfilecon_raw(path)
    print('Function lgetfilecon_raw')
    print('\tPath: {}'.format(path))
    print('\trc: {}'.format(rc))
    print('\tcon: {}'.format(con))



# Generated at 2022-06-13 00:02:29.598218
# Unit test for function matchpathcon
def test_matchpathcon():
    # Test with valid input
    r = matchpathcon('/var/log/secure', 0)
    if r[0] != 0:
        raise ValueError('matchpathcon failed with error: {0}'.format(r[0]))

    # Test with invalid input
    r = matchpathcon('/var/log/secure/', 0)
    if r[0] == 0:
        raise ValueError('matchpathcon succeeded with invalid input')



# Generated at 2022-06-13 00:02:34.790606
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    print('Running test for function lgetfilecon_raw')
    assert isinstance(lgetfilecon_raw('/etc/shadow'), list)


# Generated at 2022-06-13 00:02:37.633186
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    myFile = "/etc/passwd"
    rc, con = lgetfilecon_raw(myFile)
    assert rc == 0
    assert isinstance(con, str)



# Generated at 2022-06-13 00:02:44.826803
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    from ansible.module_utils import basic
    import os
    options = basic.AnsibleModule(
        argument_spec=dict(),
    ).params

    if options['_ansible_check_mode']:
        # don't let noop mode make it impossible to test this module
        del os.environ['_ANSIBLE_CHECK_MODE']
    path = "/tmp"
    rc, con = lgetfilecon_raw(path)
    # NB: this test is not very testy. It just outputs the results
    # But it'll at least show when the function is broken
    print("rc={} con={}".format(rc, con))

# Generated at 2022-06-13 00:02:48.580915
# Unit test for function matchpathcon
def test_matchpathcon():
    try:
        # The only test I can do is to see if it returns a list or not with
        # some random path.
        assert(isinstance(matchpathcon("/usr/bin/python", 0), list))
    except ImportError:
        pass

# Generated at 2022-06-13 00:02:52.232509
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon('/etc/shadow', os.R_OK)
    assert con == 'system_u:object_r:shadow_t:s0'



# Generated at 2022-06-13 00:02:57.749486
# Unit test for function matchpathcon
def test_matchpathcon():
    print('[testing] matchpathcon...')

    path = '/etc/httpd/conf.modules.d/00-mpm.conf'
    (rc, con) = matchpathcon(path, 0)
    if rc != 0:
        print('[FAIL] matchpathcon failed with %d' % rc)
        return rc

    print('[OK] matchpathcon')

# Generated at 2022-06-13 00:03:02.145752
# Unit test for function matchpathcon
def test_matchpathcon():
    result = matchpathcon('/', 0)
    if result[0] == 0:
        print('Matchpathcon:  %s' % result[1])
    else:
        print('Error from matchpathcon:  %s' % result[0])


if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-13 00:03:04.734679
# Unit test for function matchpathcon
def test_matchpathcon():
    expected_result = [0, b'system_u:object_r:tmp_t']
    result = matchpathcon('/tmp', 0)
    assert result == expected_result

# Generated at 2022-06-13 00:03:07.887690
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    """ Unit test for function lgetfilecon_raw """
    (rc, con) = lgetfilecon_raw("/etc/passwd")
    if con is not None:
        return True
    else:
        return False


# Generated at 2022-06-13 00:03:17.659868
# Unit test for function matchpathcon
def test_matchpathcon():
    # Pythonize matchpathcon's argtypes to int
    _selinux_lib.matchpathcon.argtypes = [_to_char_p, c_int, POINTER(c_char_p)]

    p = matchpathcon('/etc/passwd', 0)
    assert len(p) == 2
    assert p[0] == 0
    assert p[1] == 'system_u:object_r:passwd_file_t'

    p = matchpathcon('/etc/ssh/sshd_config', 0)
    assert len(p) == 2
    assert p[0] == 0
    assert p[1] == 'system_u:object_r:sshd_config_t'

    # selinux_raw_to_trans_context works with matchpathcon
    # TODO: doesn't seem to be available

# Generated at 2022-06-13 00:03:30.900783
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    """
    This function tests the selinux ansible module for the lgetfilecon_raw function.
    """
    fr_utils = sys.modules['ansible.module_utils.selinux']
    rc = 0
    con = None
    try:
        rc, con = fr_utils.lgetfilecon_raw('/etc/selinux/config')
    except OSError as err:
        sys.stderr.write('File read failed: {0}'.format(err))
    except ValueError as err:
        sys.stderr.write('Invalid arguments passed: {0}'.format(err))
    except NotImplementedError as err:
        sys.stderr.write('Missing selinux function: {0}'.format(err))

# Generated at 2022-06-13 00:03:32.922365
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    try:
        rc, con = lgetfilecon_raw(b"/etc/shadow")
        return [rc, con]
    except OSError as e:
        return [e.errno, os.strerror(e.errno)]

# Generated at 2022-06-13 00:03:34.037000
# Unit test for function matchpathcon
def test_matchpathcon():
    assert not matchpathcon("/foo", 0)


# Generated at 2022-06-13 00:03:42.960673
# Unit test for function matchpathcon
def test_matchpathcon():
    module = sys.modules[__name__]
    status, con = module.matchpathcon('test_file', 0)  # noqa
    assert status == 0
    assert con == 'test_file:test_file_t'
    status, con = module.matchpathcon('test_file', 1)  # noqa
    assert status == 0
    assert con == 'test_file:test_file_t'
    status, con = module.matchpathcon('test_file', 2)  # noqa
    assert status == 0
    assert con == 'test_file:test_file_t'

# Generated at 2022-06-13 00:03:49.041912
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import tempfile

    try:
        with tempfile.NamedTemporaryFile(mode='wb', bufsize=0) as fd:
            fname = to_native(fd.name)

            def _run():
                try:
                    return lgetfilecon_raw(fname)
                finally:
                    _selinux_lib.freecon(con)

            rc, con = _run()
            assert rc >= 0
            assert con

            rc, con = _run()
            assert rc >= 0
            assert con
            assert con == "system_u:object_r:tmp_t:s0"
    finally:
        con = 0



# Generated at 2022-06-13 00:03:52.786645
# Unit test for function matchpathcon
def test_matchpathcon():
    context = matchpathcon(b'test', 0)[1]
    assert isinstance(context, str)
    context = matchpathcon(b'test', 0o0777)[1]
    assert isinstance(context, str)



# Generated at 2022-06-13 00:03:54.441867
# Unit test for function matchpathcon
def test_matchpathcon():
    rcs, con = matchpathcon('/tmp/file.txt', 0)
    assert rcs == 0

# Generated at 2022-06-13 00:03:56.374263
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw('/etc/passwd')
    assert rc == 0
    assert con is not None



# Generated at 2022-06-13 00:03:58.908494
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Expect the following to return as code 0 and a context string as the 2nd value
    print('[{0}]'.format(lgetfilecon_raw('/etc/ansible')))



# Generated at 2022-06-13 00:04:03.832334
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    [rc, con] = lgetfilecon_raw('/etc/passwd')
    if rc != 0:
        raise Exception(
            'failed to fetch selinux context for /etc/passwd. rc = {0}, error = {1}'.format(
                rc, con))



# Generated at 2022-06-13 00:04:15.094995
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # If running from source directory, use source instead of installed module
    from os.path import dirname, abspath
    import sys
    sys.path.insert(0, dirname(dirname(abspath(__file__))))
    import selinux_common

    expected_con = 'system_u:object_r:crond_exec_t:s0'
    rc, con = selinux_common.lgetfilecon_raw('/usr/sbin/crond')

    assert rc == 0
    assert con == expected_con

# Generated at 2022-06-13 00:04:18.982583
# Unit test for function matchpathcon
def test_matchpathcon():
    """
    Test matchpathcon wrapper
    """

    import pytest

    rc, security_context = matchpathcon("/", 0)
    assert rc == 0
    assert security_context == "system_u:object_r:initrc_exec_t:s0"


# Generated at 2022-06-13 00:04:22.137341
# Unit test for function matchpathcon
def test_matchpathcon():
    mode = 0
    path = '/usr/bin/passwd'
    ret, result = matchpathcon(path, mode)

    print('ret: {0}'.format(ret))
    print('result: {0}'.format(result))


# Generated at 2022-06-13 00:04:30.273746
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    from os.path import dirname, join
    from os import environ
    cwd = dirname(__file__)
    filename = join(cwd, 'test_file')
    file = open(filename, 'w+')
    file.write("test")
    file.close()
    assert lgetfilecon_raw(filename) == [0, 'system_u:object_r:etc_t:s0']
    os.remove(filename)


if __name__ == '__main__':
    # Unit test for the functions above
    test_lgetfilecon_raw()

# Generated at 2022-06-13 00:04:40.741628
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Test case #1
    path = '/sample_directory'
    try:
        os.makedirs(path)
        [rc, con] = lgetfilecon_raw(path)
        assert(rc == 0)
    finally:
        os.rmdir(path)
    # Test case #2
    path = '/sample_file'
    try:
        with open(path, 'w') as fout:
            fout.write('')
        [rc, con] = lgetfilecon_raw(path)
        assert(rc == 0)
    finally:
        os.remove(path)
    # Test case #3
    path = '/sample_file'
    [rc, con] = lgetfilecon_raw(path)
    assert(rc == -1)


# Generated at 2022-06-13 00:04:43.949464
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon("/etc/passwd", 0)
    assert rc == 0, "matchpathcon returned an error: %s" % rc
    assert con == "system_u:object_r:etc_runtime_t:s0", "matchpathcon returned an unexpected security context: %s" % con

# Generated at 2022-06-13 00:04:49.503492
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    test_con = lgetfilecon_raw(b'/usr')
    assert test_con[0] == 0
    if os.path.exists('/etc/selinux/config'):
        assert test_con[1] == 'system_u:object_r:root_t:s0'
    else:
        assert test_con[1] == 'unlabeled_t'
    assert isinstance(test_con, list)


# Generated at 2022-06-13 00:05:00.351003
# Unit test for function matchpathcon
def test_matchpathcon():
    # Create a temporary file in /tmp
    import tempfile
    import os
    import selinux
    from ctypes import create_string_buffer
    fp = tempfile.NamedTemporaryFile(dir='/tmp', delete=False)

    # Get a context for the temporary file
    (rc, context) = matchpathcon(fp.name, os.st.S_IFREG)
    assert rc >= 0, "matchpathcon returned an error"

    # Get the context for the system
    (rc, syscontext) = selinux.getcon()
    assert rc >= 0, "getcon returned an error"

    # Check the system context is a subset of the file context
    assert syscontext[:syscontext.find(":")] == context[:context.find(":")], "System context is not a subset of file context"

    # Set

# Generated at 2022-06-13 00:05:02.919811
# Unit test for function matchpathcon
def test_matchpathcon():
    from os.path import exists

    if not exists('/'):
        raise ImportError('/ does not exist')

    assert matchpathcon('/', 0) == [0, 'rootfs']

# Generated at 2022-06-13 00:05:08.792369
# Unit test for function matchpathcon
def test_matchpathcon():
    # We are just testing argument processing and return value, not correctness

    # Path not set yet
    if matchpathcon('/test', 1)[1] is not None:
        print("Test failed, path not set yet")
        sys.exit(1)

    # Path is set
    if matchpathcon('/test', 1)[1] == None:
        print("Test failed, path is set")
        sys.exit(1)


if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-13 00:05:20.945698
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():

    rc, con = lgetfilecon_raw('/')
    if rc < 0:
        raise OSError(get_errno(), os.strerror(get_errno()))
    if rc == 0 and con is None:
        print('\nPreconditions for lgetfilecon_raw failed')
    else:
        print("\nOutput of lgetfilecon_raw for path '/' is: " + con)


# Generated at 2022-06-13 00:05:24.976666
# Unit test for function matchpathcon
def test_matchpathcon():
    if not os.path.isdir("/etc/selinux"):
        # FIXME: Should also test enforcing/permissive modes
        return

    (rc, con) = matchpathcon("/etc/selinux/config", 0)
    assert rc == 0
    assert con == "system_u:object_r:etc_runtime_t:s0"

# Generated at 2022-06-13 00:05:32.296967
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    try:
        # Should not throw an error on valid inputs
        rc, retval = lgetfilecon_raw('/')
        assert rc == 0
    except OSError as e:
        assert False, "Exception in lgetfilecon_raw: " + to_native(e.strerror)



# Generated at 2022-06-13 00:05:38.816401
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Expected values from file
    expected = [0, 'system_u:object_r:admin_home_t:s0']
    expected_invalid = [1, None]
    found = []
    found_invalid = []
    for attr, exp in zip(lgetfilecon_raw('/home/admin'), expected):
        found.append(attr)
    for attr, exp in zip(lgetfilecon_raw('/home/admin/invalid_file'), expected_invalid):
        found_invalid.append(attr)
    assert found == expected
    assert found_invalid == expected_invalid


# Generated at 2022-06-13 00:05:46.844530
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path_list = ['/', '/etc/passwd']
    path_err = 'fake_file'
    for path in path_list:
        rc, con = lgetfilecon_raw(path)
        if rc == 0:
            print('Context of {0} is: {1}'.format(path, con))
        else:
            print('Failed to get context of {0}'.format(path))
    rc, con = lgetfilecon_raw(path_err)
    if rc < 0:
        print('Failed to get context of a non-existent file: {0}'.format(path_err))


# Generated at 2022-06-13 00:05:53.368963
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon(b'/bin/bash', os.R_OK)
    if rc != 0:
        print('No SELinux %s context found for binary /bin/bash: %s' % (b'R_OK', to_native(con)))
    else:
        print('Success: SELinux context %s found for binary /bin/bash with mode %d' % (to_native(con), os.R_OK))

# Generated at 2022-06-13 00:05:56.241934
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (rc, con) = lgetfilecon_raw("/etc/passwd")
    rc_expected = 0
    con_expected = "system_u:object_r:etc_runtime_t:s0"
    assert rc == rc_expected
    assert con == con_expected
    return 0



# Generated at 2022-06-13 00:06:03.550322
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Test use on a local directory
    path = b'/etc/'
    label_data = lgetfilecon_raw(path)

    # Check that the call succeeded
    if label_data[0] != -1:
        print("Successfully retrieved label for path {0} with label {1}".format(path, label_data[1]))
    else:
        print("Unable to retrieve label information for path {0}".format(path))


# Generated at 2022-06-13 00:06:06.693022
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    retval, con_val = lgetfilecon_raw("/etc/shadow")
    print("Retval: {0} Context: {1}".format(retval, con_val))

if __name__ == "__main__":
    test_lgetfilecon_raw()

# Generated at 2022-06-13 00:06:08.607813
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import os
    file = os.path.dirname(__file__) + '/setfilecon.py'
    if os.path.exists(file):
        con = lgetfilecon_raw(file)[1]
        assert con == "unconfined_u:object_r:ansible_module_t:s0"

if __name__ == '__main__':
    test_lgetfilecon_raw()

# Generated at 2022-06-13 00:06:16.852876
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw('/usr/bin/python')
    assert rc == 0
    assert con == "system_u:object_r:bin_t:s0"


# Generated at 2022-06-13 00:06:22.532275
# Unit test for function matchpathcon
def test_matchpathcon():
    current_folder = os.getcwd()
    con = c_char_p()
    path = current_folder + '/selinux.py'

    try:
        rc = _selinux_lib.matchpathcon(path, 0, byref(con))
    except OSError as err:
        print('OSError: {}'.format(to_native(err)))
        return [rc, to_native(con.value)]
    finally:
        _selinux_lib.freecon(con)
    return [rc, to_native(con.value)]

# Generated at 2022-06-13 00:06:25.183052
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (rc, con) = lgetfilecon_raw(b'/')
    assert rc == 0
    assert con == 'system_u:object_r:root_t:s0'


if __name__ == '__main__':
    test_lgetfilecon_raw()

# Generated at 2022-06-13 00:06:27.955156
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = b'.'
    (rc, con) = lgetfilecon_raw(path)
    assert rc == 0
    assert con is not None
    assert len(con) > 1


# Generated at 2022-06-13 00:06:33.357534
# Unit test for function matchpathcon
def test_matchpathcon():
    test_file = '/tmp/test_selinux.txt'
    f = open(test_file, 'w+')
    f.close()
    print(matchpathcon(test_file, os.R_OK))
    os.remove(test_file)

# Generated at 2022-06-13 00:06:38.759591
# Unit test for function matchpathcon
def test_matchpathcon():
    print("matchpathcon('/tmp/foo.txt', 0) = " + str(matchpathcon('/tmp/foo.txt', 0)))
    print("matchpathcon('/tmp/foo.txt', S_IFDIR) = " + str(matchpathcon('/tmp/foo.txt', 0o40000)))



# Generated at 2022-06-13 00:06:41.448155
# Unit test for function matchpathcon
def test_matchpathcon():
    # Test input
    path = "/etc"
    mode = 0
    result = matchpathcon(path, mode)

    if result[0] != 0:
        print("matchpathcon function failed with error {}".format(result[0]))
    else:
        print("matchpathcon function output: ", result[1])

# Test for lgetfilecon_raw function

# Generated at 2022-06-13 00:06:51.464810
# Unit test for function matchpathcon
def test_matchpathcon():
    # First create a file
    f = open('file.txt', 'w')
    f.write('File to test matchpathcon\n')
    f.close()

    # Now we need to clear the context from the file
    _selinux_lib.lsetfilecon(b'file.txt', b'')

    # Now we need to relabel the file
    rc, newcon = _selinux_lib.matchpathcon(b'file.txt', 0)
    if rc == -13 or rc == -14:
        raise OSError(rc, os.strerror(rc))
    elif rc < 0:
        raise OSError(rc, os.strerror(rc))

    # Now we need to set the new context from matchpathcon on the file

# Generated at 2022-06-13 00:06:56.601513
# Unit test for function matchpathcon
def test_matchpathcon():
    from os import mkdir, rmdir
    from tempfile import mkdtemp
    from shutil import rmtree
    tmpdir = mkdtemp()
    testdir = os.path.join(tmpdir, 'test')
    mkdir(testdir)
    try:
        print('selinux.matchpathcon({}, 0) => {}'.format(testdir, matchpathcon(testdir, 0)))
    finally:
        rmtree(tmpdir)



# Generated at 2022-06-13 00:07:03.457675
# Unit test for function matchpathcon
def test_matchpathcon():
    from ansible.module_utils._text import to_text
    # Mock the output of selinux.matchpathcon
    def mock_matchpathcon(p, m):
        return [0, 'system_u:object_r:httpd_user_content_t:s0']

    mock_module = dict(
        matchpathcon=mock_matchpathcon
    )

    with mock.patch.dict('sys.modules', {'selinux': mock_module}):
        from ansible.module_utils import selinux
        test_path = b'/var/www/html/user/content'
        result = selinux.matchpathcon(test_path, 0)
        assert result[1] == to_text('system_u:object_r:httpd_user_content_t:s0')
        result = selinux

# Generated at 2022-06-13 00:07:10.634255
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw('/etc/localtime') == [0, 'system_u:object_r:localtime_t:s0']

# Generated at 2022-06-13 00:07:20.049745
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    new_file_name = 'test_file'
    if os.path.exists(new_file_name):
        os.remove(new_file_name)
    with open(new_file_name, 'w'):
        pass
    (rc, result) = lgetfilecon_raw(new_file_name)
    os.remove(new_file_name)
    if rc != 0:
        raise AssertionError("lgetfilecon_raw failed with non-zero return code rc=%d result=%s" % (rc, result))
    print("lgetfilecon_raw succeeded with rc=%d result=%s" % (rc, result))
    return True

# Generated at 2022-06-13 00:07:24.405336
# Unit test for function matchpathcon
def test_matchpathcon():
    if not is_selinux_enabled():
        return

    (rc, con) = matchpathcon('/etc/selinux/config', 0)
    try:
        assert rc == 0
        assert con == 'etc_t'
    finally:
        _selinux_lib.freecon(con)


# Generated at 2022-06-13 00:07:31.651072
# Unit test for function matchpathcon
def test_matchpathcon():
    import os
    import pwd
    import stat
    import shutil
    import tempfile

    test_dir = tempfile.mkdtemp(prefix='libselinux')
    fd, tmpfname = tempfile.mkstemp(prefix='libselinux', dir=test_dir)

    os.close(fd)

    try:
        rc, context = matchpathcon(tmpfname, stat.S_IFREG)
        assert rc == 0
        assert context is not None
    finally:
        shutil.rmtree(test_dir)


if __name__ == "__main__":
    test_matchpathcon()

# Generated at 2022-06-13 00:07:32.820957
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert type(lgetfilecon_raw(b'/')[1]) == str

# Generated at 2022-06-13 00:07:41.494509
# Unit test for function matchpathcon
def test_matchpathcon():
    (rc, con) = matchpathcon("/etc/passwd", 0)
    if rc < 0:
        raise OSError()
    if con != b'u:object_r:etc_runtime_t:s0':
        raise ValueError("Wrong context returned: %s" % con)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("file", default="/etc/passwd", nargs="?")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--get", action="store_true")
    group.add_argument("--set", action="store_true")
    args = parser.parse_args()
    if args.set:
        (rc, con) = lget

# Generated at 2022-06-13 00:07:43.880304
# Unit test for function matchpathcon
def test_matchpathcon():
    test_path = "/bin/mount"
    test_mode = 0

    matched = matchpathcon(test_path, test_mode)
    assert matched[0] == 0
    assert matched[1] == "system_u:object_r:mount_exec_t:s0"

# Generated at 2022-06-13 00:07:48.321128
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import tempfile

    tf = tempfile.NamedTemporaryFile()
    result = lgetfilecon_raw(tf.name)

    for val in result:
        if val is None:
            print("FAILED")
            return 1
    print("PASSED")
    return 0

if __name__ == "__main__":
    test_lgetfilecon_raw()

# Generated at 2022-06-13 00:07:52.255400
# Unit test for function matchpathcon
def test_matchpathcon():
    # Fake selinux fs context
    path = '/var/lib/libvirt/images/X.qcow2'
    context = 'system_u:object_r:virt_content_t:s0:c0'

    # Match contexts to a file
    rc, new_context = matchpathcon(path, 0)

    # test the matching
    assert rc == 0 and new_context == context

# Generated at 2022-06-13 00:07:57.165747
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    from ansible_collections.community.general.plugins.modules.selinux import lgetfilecon_raw
    print("Unit test for function lgetfilecon_raw")
    INPUT_FILE_PATH = '/etc/default/grub'
    rc, con = lgetfilecon_raw(INPUT_FILE_PATH)
    print("lgetfilecon_raw returned: rc=%s con=%s" % (rc, con))
    assert rc == 0


# Generated at 2022-06-13 00:08:12.781480
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():

    from copy import deepcopy
    from tempfile import mkstemp
    import stat

    def selinux_call(fn, *args, **kwargs):
        rc, retval = fn(*args, **kwargs)
        if rc == -1:
            raise OSError(rc, 'SElinux call failed')
        return retval


# Generated at 2022-06-13 00:08:13.752564
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert sys.modules[__name__] is not None

# Generated at 2022-06-13 00:08:17.655270
# Unit test for function matchpathcon
def test_matchpathcon():
    import tempfile
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        _selinux_lib.matchpathcon(temp_file.name, 0, None)
        _selinux_lib.matchpathcon(temp_file.name, 1, None)

if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-13 00:08:22.865904
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # This test will fail if the test file is not in the same directory as the module file
    module_directory = os.path.dirname(os.path.abspath(__file__))
    test_file = os.path.join(module_directory, "test_file")
    with open(test_file, "w") as f:
        f.write("This is a test file.")
    con = lgetfilecon_raw(test_file)
    os.remove(test_file)
    assert con[0] == 0

# Generated at 2022-06-13 00:08:26.364394
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    for path in ['/dev/null', '/usr']:
        rc, con = lgetfilecon_raw(path)
        assert rc == 0
        assert isinstance(con, str)


if __name__ == '__main__':
    test_lgetfilecon_raw()

# Generated at 2022-06-13 00:08:29.830898
# Unit test for function matchpathcon
def test_matchpathcon():
    """
    Test context is set correctly on file /etc/hosts
    """

    rc, con = matchpathcon("/etc/hosts", 0)
    assert rc == 0
    assert con == "system_u:object_r:net_conf_t:s0"

# Generated at 2022-06-13 00:08:31.879769
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    test_path = '/'
    rc, con = lgetfilecon_raw(test_path)
    assert(rc >= 0)

# Generated at 2022-06-13 00:08:35.176886
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = 'ansible_module_template'
    rc, con = lgetfilecon_raw(path)
    assert rc == 0
    assert con == 'system_u:object_r:ansible_managed_conf_t:s0'


# Generated at 2022-06-13 00:08:42.653509
# Unit test for function matchpathcon
def test_matchpathcon():
    # For each testcase, the expected output from matchpathcon() is stored in a string
    # So, if the output matches the string ( == 0 ), then the testcase passes

    # Testcase 1
    path = 'selinux_getpolicytype_test'
    mode = os.R_OK
    file_context_string = 'system_u:object_r:tmp_t:s0'
    rc, con = matchpathcon(path, mode)
    assert rc == 0
    assert con == file_context_string

    # Testcase 2
    path = 'selinux_getenforcemode_test'
    mode = os.R_OK
    file_context_string = 'system_u:object_r:tmp_t:s0'
    rc, con = matchpathcon(path, mode)
    assert rc == 0

# Generated at 2022-06-13 00:08:44.684396
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    r, con = lgetfilecon_raw('/')
    assert r == 0
    r, con = lgetfilecon_raw('/missing')
    assert r == -1
    assert con is None


# Generated at 2022-06-13 00:08:54.164515
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = "selinux.py"
    con, rc = lgetfilecon_raw(path)
    assert isinstance(con, str)
    assert isinstance(rc, int)


if __name__ == '__main__':
    test_lgetfilecon_raw()

# Generated at 2022-06-13 00:09:02.331909
# Unit test for function matchpathcon
def test_matchpathcon():
    print("")
    print("========== Match Path Con Unit Test ==========")
    print("1. Test for file")
    path = '/etc/passwd'
    mode = 0o644
    print("file path: " + str(path) + " mode: " + str(oct(mode)))
    [rc, con] = matchpathcon(path, mode)
    print("con: " + str(con) + " rc: " + str(rc))
    assert rc == 0

    print("2. Test for directory")
    path = '/etc'
    mode = 0o755
    print("file path: " + str(path) + " mode: " + str(oct(mode)))
    [rc, con] = matchpathcon(path, mode)

# Generated at 2022-06-13 00:09:05.662484
# Unit test for function matchpathcon
def test_matchpathcon():
    test_file = "/etc/ssh/sshd_config"
    test_mode = os.R_OK
    results = matchpathcon(test_file, test_mode)
    assert(results[0] == 0)
    assert(results[1] == "system_u:object_r:sshd_config_t:s0")



# Generated at 2022-06-13 00:09:11.164828
# Unit test for function matchpathcon
def test_matchpathcon():
    # Test1
    # Test on process context file which is used to store the process context
    # This file does not exist if SELinux is disabled
    path = "/proc/self/attr/current"
    mode = os.R_OK
    # expected rc = 0, con = 'unconfined_u:unconfined_r:unconfined_t:s0'
    # selinux_getpolicytype = 'targeted'
    rc, con = matchpathcon(path, mode)
    print(rc)
    print(con)
    assert rc == 0
    assert con == 'unconfined_u:unconfined_r:unconfined_t:s0'

