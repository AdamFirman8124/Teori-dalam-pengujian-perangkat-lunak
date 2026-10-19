

# Generated at 2022-06-12 23:59:14.118129
# Unit test for function matchpathcon
def test_matchpathcon():
    # Runtest for matchpathcon
    from_con = 'system_u:object_r:rpm_etc_t:s0'
    # Test the case of valid path, etc.
    assert matchpathcon('/etc/pki/rpm-gpg', os.R_OK)
    # Test the case of invalid path
    assert matchpathcon('/xyz/pki/rpm-gpg', os.R_OK)[0] != 0
    # Test the case of valid path, but invalid mode.
    assert matchpathcon('/etc/pki/rpm-gpg', os.W_OK)[0] != 0
    # Test the case of valid path, mode & context
    assert from_con == matchpathcon('/etc/pki/rpm-gpg', os.R_OK)[1]

# Generated at 2022-06-12 23:59:20.922520
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    if not os.path.exists('/root'):
        raise Exception('unit test requires /root to exist')
    rc, con = lgetfilecon_raw('/root')
    if con != "system_u:object_r:root_t:s0":
        raise Exception('unit test failed: {0} != {1}'.format(con, "system_u:object_r:root_t:s0"))


# Generated at 2022-06-12 23:59:25.654525
# Unit test for function matchpathcon
def test_matchpathcon():
    cwd = os.getcwd()
    # return value is a tuple (rc, con)
    # con = context to be set
    # rc = 0 (good) -1 (bad)
    ret = matchpathcon(cwd, os.R_OK)
    assert ret[0] == 0
    assert ret[1] != '<<none>>'
    print(ret)

# Generated at 2022-06-12 23:59:28.656644
# Unit test for function matchpathcon
def test_matchpathcon():
    path = "/etc/passwd"
    mode = 0o40
    assert matchpathcon(path, mode) == [0, "system_u:object_r:etc_runtime_t:s0"]

# Generated at 2022-06-12 23:59:33.141687
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw("/usr/bin/true") == [0, "system_u:object_r:bin_t:s0"]
    assert lgetfilecon_raw("/etc/passwd") == [0, "system_u:object_r:etc_runtime_t:s0"]

# Generated at 2022-06-12 23:59:36.959838
# Unit test for function matchpathcon
def test_matchpathcon():
    testpath = '/var/www'
    testmode = os.R_OK
    [rc, con] = matchpathcon(testpath, testmode)
    if rc != 0:
        print("rc = %d" % rc)
    else:
        print("%s: %s" % (testpath, con))



# Generated at 2022-06-12 23:59:47.820952
# Unit test for function matchpathcon
def test_matchpathcon():
    # Run once with enforcing policy and once with permissive policy
    # Permissive policy should succeed while enforcing should fail
    # The file is not expected to exist, but the match should succeed
    results = []
    selinux_enforcemode = selinux_getenforcemode()[1]

    for mode in [0, 1]:
        for con in (None, '', 'system_u:object_r:bin_t'):
            rc, con = matchpathcon('/foo', mode)
            if not mode and rc == -1:
                # error only occurs if not in permissive mode
                if errno.errorcode[rc] in ('EINVAL', 'ENOENT'):
                    # if we're in a permissive mode and get an error
                    # it is not considered an error
                    continue


# Generated at 2022-06-12 23:59:55.276506
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import os
    from ansible.module_utils.common.text.converters import to_bytes
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict(
            path=dict(type='path'),
        ),
        supports_check_mode=False
    )

    errno = 0
    rc = -1
    con = ''
    path = module.params['path']
    if not os.path.exists(path):
        errno = 2
        rc = -1
        module.fail_json(msg="File/path expected but not found", path=path, rc=rc, errno=errno, con=con)


# Generated at 2022-06-13 00:00:05.013856
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    from ansible.module_utils.selinux import lgetfilecon_raw
    from os import path
    from pwd import getpwnam
    from grp import getgrnam

    test_path = 'tests/resources/selinux_testfile'
    test_user = 'nobody'
    test_group = 'nobody'

    if not path.exists(test_path):
        raise RuntimeError('the test file {0!r} does not exist'.format(test_path))

    user = getpwnam(test_user)
    group = getgrnam(test_group)

    # set the permission context
    from os import chown
    from os import chmod
    from ansible.module_utils.six.moves import range
    chmod(test_path, 0o777)

# Generated at 2022-06-13 00:00:08.647280
# Unit test for function matchpathcon
def test_matchpathcon():
    path = '/tmp/test'
    if not os.path.exists(path):
        os.mkdir(path)
    mode = os.stat(path).st_mode
    con = matchpathcon(path, mode)
    assert con
    os.rmdir(path)

# Generated at 2022-06-13 00:00:13.510904
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw('/etc/passwd') == [0, 'system_u:object_r:etc_runtime_t:s0']



# Generated at 2022-06-13 00:00:15.327515
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    [rc, con] = lgetfilecon_raw(__file__)
    assert rc == 0



# Generated at 2022-06-13 00:00:23.411227
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (rc, con) = lgetfilecon_raw('/etc/selinux/config')
    assert rc == 0
    assert con == 'system_u:object_r:etc_runtime_t:s0'
    (rc, con) = lgetfilecon_raw('/nonexistent')
    assert rc == -1
    assert con == ''
    (rc, con) = lgetfilecon_raw('/selinux')
    assert rc == 0
    assert con == 'system_u:object_r:selinuxfs:s0'
    (rc, con) = lgetfilecon_raw('/selinux/config')
    assert rc == 0
    assert con == 'system_u:object_r:selinux_config_t:s0'

# Generated at 2022-06-13 00:00:26.378627
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon('/etc/mysql', os.R_OK)
    if rc != 0:
        print('matchpathcon: {}'.format(con))
    else:
        print('matchpathcon: {}'.format(con))

# Generated at 2022-06-13 00:00:38.300180
# Unit test for function matchpathcon

# Generated at 2022-06-13 00:00:45.469552
# Unit test for function matchpathcon
def test_matchpathcon():
    assert matchpathcon('/etc/test.txt', 0) == [0, 'system_u:object_r:file_t:s0']
    assert matchpathcon('/etc/test.txt', 1) == [0, 'user_u:object_r:file_t:s0']
    assert matchpathcon('/etc/test.txt', 2) == [0, 'user_u:object_r:file_t:s0']
    assert matchpathcon('/etc/test.txt', 3) == [0, 'user_u:object_r:file_t:s0']
    assert matchpathcon('/etc/test.txt', 4) == [0, 'user_u:object_r:file_t:s0']

# Generated at 2022-06-13 00:00:52.045561
# Unit test for function matchpathcon
def test_matchpathcon():
    # Test path existing in the system.
    # The correct selinux context should be: system_u:object_r:etc_t:s0
    print('***matchpathcon test')
    (rc, selinux_context) = matchpathcon('/etc', 0)
    assert rc == 0
    assert selinux_context == 'system_u:object_r:etc_t:s0'


if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-13 00:00:56.714317
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (rc, con) = lgetfilecon_raw('/etc/passwd')
    if rc < 0:
        errno = get_errno()
        raise OSError(errno, os.strerror(errno))
    if con == 'system_u:object_r:etc_t:s0':
        return True
    else:
        raise AssertionError(con)

if __name__ == "__main__":
    print(test_lgetfilecon_raw())

# Generated at 2022-06-13 00:01:03.997176
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    test_path = '/boot/vmlinuz-3.10.0-1062.9.1.el7.x86_64'
    test_con = 'system_u:object_r:boot_t:s0'
    test_con_raw = 'system_u:object_r:boot_t:s0:c123,c456'
    rc, con = lgetfilecon_raw(test_path)
    assert rc == 0
    # NOTE: the inode context is not guaranteed to be the same across
    # systems and so the raw context string will contain arbitrary values
    # depending on the system the test is run on
    # assert con == test_con
    assert con.startswith(test_con_raw)


if __name__ == '__main__':
    test_lgetfilecon_raw()

# Generated at 2022-06-13 00:01:10.563098
# Unit test for function matchpathcon
def test_matchpathcon():
    if not is_selinux_enabled():
        return False

    if __name__ == '__main__':
        # Try to retrieve the context of /etc/hosts
        # and compare it to the expected context
        expected_context = 'system_u:object_r:etc_t:s0'
        [rc, con] = matchpathcon('/etc/hosts', 0)

        return [rc, con] == [0, expected_context]

if __name__ == '__main__':
    print(test_matchpathcon())

# Generated at 2022-06-13 00:01:18.513525
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = 'tests/files/default/self'
    [rc, con] = lgetfilecon_raw(path)
    assert rc == 0
    assert con == "system_u:object_r:default_t:s0"



# Generated at 2022-06-13 00:01:26.075409
# Unit test for function matchpathcon
def test_matchpathcon():
    # This test will fail if the context is set to anything other than "system_u:object_r:unlabeled_t:s0",
    # if the SELinux policy doesn't allow the creation of this file
    # or if the SELinux policy doesn't allow the transition to "system_u:object_r:user_tmp_t:s0" context.

    # Create temp file
    import tempfile, os

    fd, path = tempfile.mkstemp()
    os.close(fd)

    rc, context = matchpathcon(path, 0)
    assert rc != -1
    rc, context_new = matchpathcon(path, 0)
    assert rc != -1
    rc, context_dir = matchpathcon(os.path.dirname(path), 0)
    assert rc != -1

   

# Generated at 2022-06-13 00:01:27.972650
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    test_val = lgetfilecon_raw('/proc')
    print(test_val[1])


# Generated at 2022-06-13 00:01:33.570492
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    test_path = os.path.dirname(os.path.realpath(__file__))
    test_file = os.path.join(test_path, 'test_selinux.py')
    rc, con = lgetfilecon_raw(test_file)
    assert rc == 0
    assert con.startswith('system_u:object_r:')
    assert con.endswith(':s0')



# Generated at 2022-06-13 00:01:36.751448
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import os.path
    file_path = os.path.dirname(os.path.realpath(__file__))
    rc, file_context = lgetfilecon_raw(file_path)
    assert rc == 0
    assert file_context == '/usr/share/pyshared/selinux' or file_context == 'system_u:object_r:usr_t:s0'



# Generated at 2022-06-13 00:01:41.691475
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import os
    if 'ANSIBLE_LGETFILECON_RAW_PATH' in os.environ:
        path = os.environ['ANSIBLE_LGETFILECON_RAW_PATH']
        con = c_char_p()
        try:
            rc = _selinux_lib.lgetfilecon_raw(path, byref(con))
            return [rc, con.value]
        finally:
            _selinux_lib.freecon(con)

# Generated at 2022-06-13 00:01:45.506402
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw("/var")
    assert rc == 0  # The file exists
    assert con == "var_t"  # The context is correct



# Generated at 2022-06-13 00:01:50.200034
# Unit test for function matchpathcon
def test_matchpathcon():
    # Test with correct path
    path = '/opt/test/a'
    mode = 0o755
    rc, con_val = matchpathcon(path, mode)
    if rc != 0:
        print('Path does not exist')
        return rc
    # If Path exists
    print('The context for the path {0} is {1}'.format(path, con_val))
    return rc



# Generated at 2022-06-13 00:02:02.536462
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Test to see if file exists
    i = os.path.exists('/etc/selinux/targeted/contexts/files/file_contexts')
    assert i

    # Test to see if permissions on file is correct
    mode = os.stat('/etc/selinux/targeted/contexts/files/file_contexts')
    assert mode.st_mode == 8192

    # Test to see if lgetfilecon_raw returns a non-empty string
    con = lgetfilecon_raw('/etc/selinux/targeted/contexts/files/file_contexts')[1]
    assert con != ''

    # Test to see if the security context is returned by lgetfilecon_raw
    assert con == 'system_u:object_r:etc_runtime_t:s0'

# Generated at 2022-06-13 00:02:06.363193
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (rc, con) = lgetfilecon_raw('/etc/passwd')
    assert(rc == 0)
    assert(con == 'system_u:object_r:etc_runtime_t:s0')



# Generated at 2022-06-13 00:02:16.123068
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    try:
        [rc, con] = lgetfilecon_raw('/')
    except OSError as e:
        if e.errno == -2:  # No such file or directory
            rc = 0
            con = None
        else:
            raise
    assert rc == 0
    assert con


# Generated at 2022-06-13 00:02:20.137325
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw("/etc/passwd")
    assert rc == 0
    assert con == 'system_u:object_r:etc_t'

# Generated at 2022-06-13 00:02:22.598899
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (rc, context) = lgetfilecon_raw("/etc")
    assert rc == 0
    assert context
    print(context)


# Generated at 2022-06-13 00:02:31.853125
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # [rc, context] = lgetfilecon_raw('/var/log/messages')
    # [rc, context] = matchpathcon('/var/log/messages', 0)
    if is_selinux_enabled():
        [rc, context] = lgetfilecon_raw('/var/log/messages')
        assert rc == 0
        assert context.startswith('system_u:object_r:var_log_t:s0')
    else:
        [rc, context] = lgetfilecon_raw('/var/log/messages')
        assert rc == -1
        assert rc == -1
        assert context == ''

# Generated at 2022-06-13 00:02:36.460985
# Unit test for function matchpathcon
def test_matchpathcon():
    test_path = '/foo/bar'
    test_mode = 0
    rc, con = matchpathcon(test_path, test_mode)
    if rc == 0:
        print(con)
    else:
        print('Failed to get file context for {0}'.format(test_path))


# Generated at 2022-06-13 00:02:45.313777
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import tempfile
    from ctypes import create_string_buffer

    f = tempfile.TemporaryFile()
    status, data = lgetfilecon_raw(f.fileno())
    assert status > -1

    # NB: access() if the file still exists
    assert os.access(f.fileno(), os.F_OK)

    # NB: Test selinux_file_context_match() with a file context that won't match
    #     unless we're in the right policy.
    #     e.g. it will always match if we're in permissive mode.
    #
    #     So, select a file context that won't match anything in my policy, like:
    #
    #     # cat /etc/selinux/targeted/contexts/files/file_contexts.local
    #     # This file is being

# Generated at 2022-06-13 00:02:52.730091
# Unit test for function matchpathcon
def test_matchpathcon():
    """Unit test for python selinux module's matchpathcon function."""

    [[rc, con]] = matchpathcon('/etc/hosts', 0)
    assert rc == 0, 'matchpathcon failed to get the context for /etc/hosts. rc={}'.format(to_native(rc))
    assert con == 'system_u:object_r:net_conf_t:s0', 'matchpathcon returned the wrong context for /etc/hosts'



# Generated at 2022-06-13 00:02:55.749958
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw("/usr/bin/python") == [0, 'unconfined_u:object_r:usr_t:s0']  # nosec

# Generated at 2022-06-13 00:03:01.145779
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Check that the function succeeds with a valid path, and fails with an invalid path
    # A valid path is '.' and an invalid path does not exist
    rc, context_1 = lgetfilecon_raw('.')
    if rc == 0:
        return context_1
    else:
        rc, context_2 = lgetfilecon_raw('invalid_path')
        return rc



# Generated at 2022-06-13 00:03:03.353109
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon(b'/dev/null', 0)
    assert rc == 0
    assert con == b'c1:c0'

# Generated at 2022-06-13 00:03:12.290061
# Unit test for function matchpathcon
def test_matchpathcon():
    path = '/var/lib/libvirt/filesystems/virtfilesystems-0.xml'
    path = path.encode('utf-8')
    mode = os.stat(path)[stat.ST_MODE]
    rc, con = matchpathcon(path, mode)
    print('rc: ', rc)
    print('con:', con)


# Generated at 2022-06-13 00:03:19.453467
# Unit test for function matchpathcon
def test_matchpathcon():
    assert matchpathcon('/missingfile', 0) == [0, '?']
    def do_test(path, mode, expect):
        assert matchpathcon(path, mode) == [0, expect]
    do_test('/etc/selinux/config', 0, 'system_u:object_r:etc_t:s0')
    do_test('/etc/selinux/config', 32768, 'system_u:object_r:etc_t:s0')
    do_test('/etc/selinux/config', 131072, 'system_u:object_r:etc_t:s0')
    do_test('/etc/selinux/config', 327680, 'system_u:object_r:etc_t:s0')

# Generated at 2022-06-13 00:03:23.965686
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon("/selinux/booleans/boolean_test", 0)
    assert rc == 0
    assert con == "system_u:object_r:boolean_test_t:s0"

# Generated at 2022-06-13 00:03:25.601919
# Unit test for function matchpathcon
def test_matchpathcon():
    return matchpathcon('/usr/bin/vim', 0)


# Generated at 2022-06-13 00:03:28.072314
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw('/etc/passwd')[1].startswith('system_u:object_r:etc_runtime_t')

# Generated at 2022-06-13 00:03:29.526637
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon('/tmp', 0)
    assert rc == 0
    assert con == "system_u:object_r:tmp_t:s0"


# Generated at 2022-06-13 00:03:33.143598
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    fun = "lgetfilecon_raw"
    rc, con = lgetfilecon_raw("/etc/passwd")
    if rc == -1:
        raise Exception("{0} function failed to get context of /etc/passwd".format(fun))
    else:
        print("{0} function successfully returned context for /etc/passwd: {1}".format(fun, con))


if __name__ == '__main__':
    test_lgetfilecon_raw()

# Generated at 2022-06-13 00:03:44.012120
# Unit test for function matchpathcon
def test_matchpathcon():
    def _test_matchpathcon(path, mode):
        try:
            rc, con = matchpathcon(path, mode)
            print('matchpathcon({0}, {1}) -> {2}, {3}'.format(repr(path), mode, rc, repr(con)))
        except OSError as e:
            print('matchpathcon({0}, {1}) -> {2}, {3}'.format(repr(path), mode, e.errno, repr(to_native(os.strerror(e.errno)))))

    _test_matchpathcon('/tmp/foo', 0)
    _test_matchpathcon('/tmp/foo', os.constants.S_IRWXU)

# Generated at 2022-06-13 00:03:48.601467
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = to_bytes(__file__)
    con = c_char_p()
    try:
        rc = _selinux_lib.lgetfilecon_raw(path, byref(con))
        return [rc, to_native(con.value)]
    finally:
        _selinux_lib.freecon(con)



# Generated at 2022-06-13 00:03:54.791168
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import sys
    import os
    rc, con = lgetfilecon_raw(sys.argv[0])
    if rc < 0:
        print("lgetfilecon_raw failed: %s" % os.strerror(-rc))
    if rc == 0:
        print("lgetfilecon_raw succeeded: %s" % con)
    if rc == 1:
        print("lgetfilecon_raw succeeded: %s" % con)


# Generated at 2022-06-13 00:04:12.157141
# Unit test for function matchpathcon
def test_matchpathcon():
    # Test result of matchpathcon with regular file
    (rc, result) = matchpathcon('/etc/passwd', 0)
    if rc == 0:
        assert result == 'system_u:object_r:etc_t:s0'
    else:
        raise Exception('test_matchpathcon: rc = %d, expected 0' % rc)

    # Test result of matchpathcon with directory
    (rc, result) = matchpathcon('/etc', 0)
    if rc == 0:
        assert result == 'system_u:object_r:etc_t:s0'
    else:
        raise Exception('test_matchpathcon: rc = %d, expected 0' % rc)

    # Test result of matchpathcon with nonexistent file
    (rc, result) = matchpathcon('/etc/foo', 0)


# Generated at 2022-06-13 00:04:15.668386
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    [rc, con] = lgetfilecon_raw('/initrd.img')
    assert rc == 0
    assert con == 'system_u:object_r:boot_t:s0'



# Generated at 2022-06-13 00:04:24.450337
# Unit test for function matchpathcon
def test_matchpathcon():
    # test a common path
    path = '/etc/selinux/config'
    mode = os.stat(path).st_mode
    rc, con = matchpathcon(path, mode)
    assert rc == 0 and con == 'system_u:object_r:etc_t:s0'

    # this should fail
    path = '/bin/sh'
    mode = os.stat(path).st_mode
    rc, con = matchpathcon(path, mode)
    assert rc == -1 and con == ''

    # this should fail
    path = '/test/selinux/failed/path'
    mode = os.stat(path).st_mode
    rc, con = matchpathcon(path, mode)
    assert rc == -1 and con == ''



# Generated at 2022-06-13 00:04:28.563400
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = '/'
    rc, con = lgetfilecon_raw(path)
    assert rc == 0
    assert con == 'system_u:object_r:file_t:s0'


# Generated at 2022-06-13 00:04:39.109726
# Unit test for function matchpathcon
def test_matchpathcon():
    import os
    import os.path as path

    from tempfile import TemporaryDirectory

    from ansible.module_utils.common.text.converters import to_bytes, to_native

    here = os.path.abspath(os.path.dirname(__file__))

    # NB: cannot create temp file in /tmp due to the presence of a type_transition rule
    with TemporaryDirectory() as tmpdir:
        path = to_bytes(os.path.join(tmpdir, "testfile"))
        mode = 0
        con = c_char_p()
        rc = _selinux_lib.matchpathcon(path, mode, byref(con))
        assert rc == 0
        assert to_native(con.value) == "system_u:object_r:tmp_t:s0"
        _selin

# Generated at 2022-06-13 00:04:42.251870
# Unit test for function matchpathcon
def test_matchpathcon():
    assert matchpathcon('/', 1) == [0, 'system_u:object_r:admin_home_t:s0']
    assert matchpathcon('/etc', 2) == [0, 'system_u:object_r:etc_t:s0']



# Generated at 2022-06-13 00:04:46.182829
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = os.path.abspath(__file__)
    rc, con = lgetfilecon_raw(path)
    assert rc == 0, "lgetfilecon_raw returned a non-zero error code: %s" % rc
    assert con is not None, "lgetfilecon_raw returned None"
    assert type(con) == str, "lgetfilecon_raw returned %s, expected str." % type(con)

# Generated at 2022-06-13 00:04:50.604407
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Re-execute this function in ansible-test to get a complete output:
    # ansible-test selinux_test --collect --requirements --allow-disabled --python 3.6
    from ansible.module_utils.selinux import lgetfilecon_raw

    try:
        rc, con = lgetfilecon_raw('/')
        assert rc == 0, 'Function lgetfilecon_raw failed to retrieve context of /'
    except OSError as e:
        if e.errno == 95:
            print('WARN: selinux not installed, this is expected on some systems')
            return
        else:
            raise


if __name__ == "__main__":
    test_lgetfilecon_raw()

# Generated at 2022-06-13 00:04:53.189041
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Check directory where selinux is disabled
    # [0, ''] is returned in this case
    # rc = 0 and con value = ''
    assert lgetfilecon_raw('/tmp') == [0, '']

# Generated at 2022-06-13 00:04:56.467635
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw("/etc") == [0, 'system_u:object_r:etc_t:s0']



# Generated at 2022-06-13 00:05:12.117651
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw('/etc/gshadow')[1] == 'system_u:object_r:shadow_t:s0'
    assert lgetfilecon_raw('/etc/group')[1] == 'system_u:object_r:etc_runtime_t:s0'
    assert lgetfilecon_raw('/etc/shadow')[1] == 'system_u:object_r:shadow_t:s0'
    assert lgetfilecon_raw('/etc/passwd')[1] == 'system_u:object_r:etc_runtime_t:s0'
    assert lgetfilecon_raw('/etc/hosts')[1] == 'system_u:object_r:hosts_t:s0'

# Generated at 2022-06-13 00:05:15.978952
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    """
    Test intent of lgetfilecon_raw
    """
    [rc, context] = lgetfilecon_raw(b'/etc/hosts')
    assert rc == 0
    assert isinstance(context, str)

# Generated at 2022-06-13 00:05:19.506062
# Unit test for function matchpathcon
def test_matchpathcon():
    print("selinux.matchpathcon:", matchpathcon("/dev/shm/myfile", 0))

# Generated at 2022-06-13 00:05:26.552818
# Unit test for function matchpathcon
def test_matchpathcon():
    import os
    import pwd
    path = os.path.expanduser('~')
    mode = os.stat(path).st_mode
    rc, ctx = matchpathcon(path, mode)
    assert rc == 0
    user = pwd.getpwuid(os.getuid())[0]
    assert ctx == 'unconfined_u:{0}_r:unconfined_t:s0'.format(user)


if __name__ == '__main__':
    import ansible.module_utils.basic

    ansible.module_utils.basic.run_ansible_module(
        module_args=dict(
            path='~',
            mode=None,
        ),
    )

# Generated at 2022-06-13 00:05:32.009758
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw("/etc/passwd")
    assert rc == 0
    assert con.startswith("unconfined_u:object_r:user_home_t:s0")


# Generated at 2022-06-13 00:05:35.860775
# Unit test for function matchpathcon
def test_matchpathcon():
    (rc, con) = matchpathcon('/etc/hosts', os.R_OK)
    assert(rc == 0)
    assert(con == "unconfined_u:object_r:etc_t:s0")


if __name__ == "__main__":
    test_matchpathcon()

# Generated at 2022-06-13 00:05:41.211820
# Unit test for function matchpathcon
def test_matchpathcon():

    rc, con = matchpathcon(b'/etc/mtab', 0)
    if rc != 0:
        sys.exit(1)

    if con == b'':
        sys.exit(1)

    if not con.startswith(b'system_u:object_r:'):
        sys.exit(1)

# Generated at 2022-06-13 00:05:43.800014
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = b'/proc/version'
    rc = lgetfilecon_raw(path)
    assert isinstance(rc, list)
    assert len(rc) == 2


# Generated at 2022-06-13 00:05:45.795461
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, actual = lgetfilecon_raw(__file__)
    assert rc == 0
    assert actual is not None


# Generated at 2022-06-13 00:05:48.039571
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Positive test case
    rc, con = lgetfilecon_raw("/etc/shadow-")
    assert rc == -1
    assert con is None



# Generated at 2022-06-13 00:06:02.153651
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw('/') == [0, 'system_u:object_r:root_t:s0']

# Generated at 2022-06-13 00:06:06.395475
# Unit test for function matchpathcon
def test_matchpathcon():
    try:
        ret = matchpathcon(__file__, 0)
    except AttributeError:
        assert os.path.isfile(__file__) is False, "matchpathcon isn't implemented on your system."
    else:
        assert ret[0] >= 0, "matchpathcon test failed, ret[0]={0}".format(ret)

# Generated at 2022-06-13 00:06:08.113123
# Unit test for function matchpathcon
def test_matchpathcon():
    assert matchpathcon(b'/etc/hosts', 0)[1] == 'system_u:object_r:etc_t:s0'

# Generated at 2022-06-13 00:06:17.533782
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import os
    import tempfile

    # Create a temporary file and a file context to set
    fd, filename = tempfile.mkstemp()
    context = 'unconfined_u:object_r:user_tmp_t:s0'
    os.close(fd)

    # Set the file context

# Generated at 2022-06-13 00:06:21.140121
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    curpath = os.path.dirname(os.path.abspath(__file__))
    if not os.path.exists(curpath):
        raise ValueError('Invalid path: {0}'.format(curpath))
    resp = lgetfilecon_raw(curpath)
    print(''.join(resp))



# Generated at 2022-06-13 00:06:22.984929
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw(b'.')
    assert rc >= 0
    assert isinstance(con, str)
    print('File context for . : {0}'.format(con))


# Unit tests for function matchpathcon

# Generated at 2022-06-13 00:06:24.122859
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    raise ImportError('unable to load libselinux.so')



# Generated at 2022-06-13 00:06:25.651277
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw('/usr') == [0, 'system_u:object_r:usr_t:s0']



# Generated at 2022-06-13 00:06:38.253491
# Unit test for function matchpathcon
def test_matchpathcon():
    assert matchpathcon('/var/log', 0) == [0, b'var_log_t']
    assert matchpathcon('/var/log', os.O_RDONLY) == [0, b'var_log_t']
    assert matchpathcon('/var/log', os.O_WRONLY) == [0, b'var_log_t']
    assert matchpathcon('/var/log', os.O_RDWR) == [0, b'var_log_t']



# Generated at 2022-06-13 00:06:41.034175
# Unit test for function matchpathcon
def test_matchpathcon():
    result = matchpathcon('/tmp/test_file1', os.O_RDWR|os.O_CREAT)
    assert result[1] == "system_u:object_r:tmp_t:s0"

# Generated at 2022-06-13 00:06:59.251214
# Unit test for function matchpathcon
def test_matchpathcon():
    print("Running {0}".format('matchpathcon'))
    # Set execcon for /usr/local/bin/ansible-playbook
    # NB: selinux_getenforcemode()[1] == 1 means "enforce"
    if (selinux_getenforcemode()[1] == 1):  # Permissive Mode
        print("Enforcing mode is off")
        # Set file context
        # NB: selinux_getpolicytype()[1] == "targeted" means "targeted"
        if (selinux_getpolicytype()[1] == "targeted"):  # Targeted Mode
            print("Targeted policy is on")

# Generated at 2022-06-13 00:07:01.551870
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # this test runs with assumptions about the system
    # its running on and should not be ran as part of
    # the unit tests
    rc, con = lgetfilecon_raw('/etc/shadow')
    assert rc == 0
    assert con == "system_u:object_r:shadow_t:s0"



# Generated at 2022-06-13 00:07:07.264533
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = b'/usr/bin/id'
    rc, con = lgetfilecon_raw(path)
    assert rc == 0
    assert con == b'unconfined_u:object_r:user_home_t:s0'
    path = b'/foo/bar/baz'
    rc, con = lgetfilecon_raw(path)
    assert rc == -1
    # NB: that's errno on the library, not the actual module
    assert con == b'Operation not permitted\n'

# Generated at 2022-06-13 00:07:09.440218
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon(u'home', 0)
    assert rc == 1
    assert con == 'system_u:object_r:user_home_t:s0'

# Generated at 2022-06-13 00:07:20.078772
# Unit test for function matchpathcon
def test_matchpathcon():
    path = b'/etc'
    mode = 0
    expected = (0, b'system_u:object_r:etc_t:s0')
    actual = matchpathcon(path, mode)
    assert actual == expected

    path = b'/etc/'
    mode = 0
    expected = (0, b'system_u:object_r:etc_t:s0')
    actual = matchpathcon(path, mode)
    assert actual == expected

    path = b'/etc'
    mode = os.R_OK
    expected = (0, b'system_u:object_r:etc_t:s0')
    actual = matchpathcon(path, mode)
    assert actual == expected

    path = b'/etc/localtime'
    mode = 0

# Generated at 2022-06-13 00:07:25.539938
# Unit test for function matchpathcon
def test_matchpathcon():
    assert matchpathcon('/etc/hosts', 0) == [0, 'system_u:object_r:etc_t:s0']
    assert matchpathcon('/etc/hosts', 1) == [0, 'system_u:object_r:etc_t:s0']
    assert matchpathcon('/etc/hosts', 2) == [0, 'system_u:object_r:etc_t:s0']


# Generated at 2022-06-13 00:07:33.914813
# Unit test for function matchpathcon
def test_matchpathcon():
    dirn = os.getcwd()
    rc, con = matchpathcon(dirn, 0)
    assert rc == 0
    assert con == 'system_u:object_r:admin_home_t:s0'

    rc, con = matchpathcon(dirn, 255)
    assert rc == 0
    assert con == 'system_u:object_r:admin_home_t:s0'

    rc, con = matchpathcon('/', 0)
    assert rc == 0
    assert con == 'system_u:object_r:root_t:s0'

    rc, con = matchpathcon('/dev/tty', 0)
    assert rc == 0
    assert con == 'system_u:object_r:chr_file_t:s0'



# Generated at 2022-06-13 00:07:42.175153
# Unit test for function matchpathcon
def test_matchpathcon():
    import tempfile

    path = tempfile.mkstemp()[1]
    permissions = '0644'
    os.chmod(path, int(permissions, 8))

    # check that matchpathcon can return the correct type and mode in the context
    r = matchpathcon(path, 0)
    assert r[0] == 0, 'got failure from matchpathcon'
    assert r[1].startswith('system_u:object_r:usr_t:{0}'.format(permissions)), \
        'matchpathcon failed to return the correct type and mode: %s' % r[1]

    # check that matchpathcon can return the correct type given a file with no mode set
    # (i.e. default mode for mode=0644)
    os.chmod(path, 0)
    r = matchpathcon

# Generated at 2022-06-13 00:07:44.171584
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # create a test file
    filename = "/tmp/ansible_test_file"
    fd = os.open(filename, os.O_RDWR | os.O_CREAT, 0o600)
    rc, con = lgetfilecon_raw(filename)
    os.close(fd)
    os.unlink(filename)
    assert con is not None

# Generated at 2022-06-13 00:07:50.097327
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    result = lgetfilecon_raw('/etc/group')
    assert result[0] == 0, "lgetfilecon_raw('/etc/group') failed with return code {0}".format(result[0])
    assert len(result[1]) != 0, 'lgetfilecon_raw("/etc/group") return empty string'
    assert result[1] == 'system_u:object_r:etc_runtime_t:s0', 'unexpected result: {0}'.format(result[1])


# Generated at 2022-06-13 00:08:05.646691
# Unit test for function matchpathcon
def test_matchpathcon():
    # https://docs.python.org/3/library/ctypes.html#module-level
    # ctypes.set_errno(0)
    (rc, con) = matchpathcon(b'/tmp/xattr', 0)
    if rc < 0:
        raise Exception("could not matchpathcon(): rc={} error={} con={}", format(rc, os.strerror(rc), con))
    print("rc={}, con={}".format(rc, con))

if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-13 00:08:15.563890
# Unit test for function matchpathcon
def test_matchpathcon():
    import os
    import stat

    (rc, con) = matchpathcon('/etc/shadow', 0)
    if rc < 0:
        raise OSError(rc, os.strerror(rc))

    print('con:', con)

    (rc, con) = matchpathcon('/etc', stat.S_ISDIR)
    if rc < 0:
        raise OSError(rc, os.strerror(rc))

    print('con:', con)

    (rc, con) = matchpathcon('/etc/shadow', stat.S_ISDIR)
    if rc != -1:
        raise ValueError('unexpected success')

    print('errno:', rc)
    print('errstr:', os.strerror(rc))


# Generated at 2022-06-13 00:08:20.134089
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw('/etc/passwd')
    assert rc == 0
    assert con == 'system_u:object_r:shadow_t:s0'
    # File doesn't exist
    rc, con = lgetfilecon_raw('/etc/doesntexist')
    assert rc == -1
    # lstat fails
    rc, con = lgetfilecon_raw('/dev/null')
    assert rc == -1


# Generated at 2022-06-13 00:08:29.206655
# Unit test for function matchpathcon
def test_matchpathcon():
    """
    Test matchpathcon using a unit test

    This function was originally written to test the matchpathcon function
    in the selinux module.  matchpathcon has now been deprecated and replaced
    with selabel_lookup.  I am leaving this comment so that it can serve as a
    reminder of the original purpose of this function.
    """
    # NOTE: this test should only be invoked when we can do a chdir.
    # It is intended to exercise the logic of matchpathcon with a long path.
    # This is to ensure that our long path version of the function
    # is being used and not the short path version.
    (rc,con) = matchpathcon('/var/lib/myapp/writable/log', os.O_CREAT)

    # The context on the test machine should be
    #  system_u:object_

# Generated at 2022-06-13 00:08:33.636433
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, mode = selinux_getenforcemode()
    assert rc == 0
    rc, context = matchpathcon('/etc/resolv.conf', mode)
    assert rc == 0
    print('/etc/resolv.conf selinux context is: {}'.format(context))

if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-13 00:08:35.840497
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, ret = lgetfilecon_raw(b'/etc/passwd')
    assert rc == 0
    assert type(ret) == str


# Generated at 2022-06-13 00:08:40.384946
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    file_path = '/tmp/test_selinux.py'
    os.system('touch {0}'.format(file_path))
    [rc, con] = lgetfilecon_raw(file_path)
    print(con)
    assert con == 'system_u:object_r:user_tmp_t:s0'
    os.system('rm {0}'.format(file_path))



# Generated at 2022-06-13 00:08:42.580371
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import json

    [rc, con] = lgetfilecon_raw("/etc/passwd")
    assert rc == 0
    assert con == "system_u:object_r:etc_runtime_t:s0"

# Generated at 2022-06-13 00:08:47.153223
# Unit test for function matchpathcon
def test_matchpathcon():
    # Test with path that does not need conversion
    if not os.path.exists('/etc'):
        raise ImportError('missing path: /etc')

    rc, con = _selinux_lib.matchpathcon('/etc', 0)
    assert rc == 0
    assert con.startswith(b'user_home_dir_t:')

    # Test with path that needs conversion
    rc, con = _selinux_lib.matchpathcon(b'/etc', 0)
    assert rc == 0
    assert con.startswith(b'user_home_dir_t:')

    # Test with invalid path
    rc, con = _selinux_lib.matchpathcon('/dev/invalid_file1', 0)
    assert rc < 0
    assert b'/dev/invalid_file1' in con

# Generated at 2022-06-13 00:08:47.922397
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # FIXME: add some tests
    pass

# Generated at 2022-06-13 00:09:03.252285
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw('/etc/passwd') == [0, 'system_u:object_r:passwd_file_t']
    assert lgetfilecon_raw('/tmp/doesnotexist') == [errno.ENOENT, None]


# Generated at 2022-06-13 00:09:07.961748
# Unit test for function matchpathcon
def test_matchpathcon():
    os.environ['SELINUX_ROLE_REQUESTED'] = 'object_r'
    os.environ['SELINUX_LEVEL_REQUESTED'] = 's1:c0.c255'

    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'matchpathcon.py')
    print(matchpathcon(path, os.R_OK))
    print(matchpathcon(path, os.W_OK))