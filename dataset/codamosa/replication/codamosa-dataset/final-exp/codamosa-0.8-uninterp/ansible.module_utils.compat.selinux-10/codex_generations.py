

# Generated at 2022-06-12 23:59:11.618202
# Unit test for function matchpathcon
def test_matchpathcon():
    path="/bin/ls"
    mode=1
    rc, final_con = matchpathcon(path, mode)
    print("rc=",rc)
    print("final_con=",final_con)


# Generated at 2022-06-12 23:59:13.947930
# Unit test for function matchpathcon
def test_matchpathcon():
    assert matchpathcon('/etc/fstab', 0) == [0, 'system_u:object_r:fstab_t:s0']

# Generated at 2022-06-12 23:59:22.397109
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    '''
    Test the lgetfilecon_raw function
    '''
    rc, con = lgetfilecon_raw('/usr/sbin/ping')
    assert rc == 0
    assert con == 'system_u:object_r:ping_exec_t:s0'
    rc, con = lgetfilecon_raw('/foo/bar')
    assert rc == -1
    if rc == -1:
        rc, con = lgetfilecon_raw('/foo/bar')
        assert rc == -1
        assert con == '<<none>>'


# Generated at 2022-06-12 23:59:27.407436
# Unit test for function matchpathcon
def test_matchpathcon():
    (rc, con) = matchpathcon('/etc/passwd', 0)

    if rc != 0:
        return False

    if not con in ['system_u:object_r:shadow_passwd_t:s0',
                   'system_u:object_r:passwd_file_t:s0']:
        return False

    return True


# Generated at 2022-06-12 23:59:30.801771
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = b'/etc/group'
    (rc, con) = lgetfilecon_raw(path)
    assert rc == 0
    assert con == b'system_u:object_r:etc_runtime_t:s0'



# Generated at 2022-06-12 23:59:36.446889
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon(b'/usr/bin/python2.7', 0)
    assert rc == 0
    assert con == 'system_u:object_r:usr_t:s0'

    # Do not work in Docker, WHY?
    rc, con = matchpathcon(b'/usr/lib/systemd/systemd', 0)
    assert rc == 0
    assert con == 'system_u:object_r:bin_t:s0'

# Generated at 2022-06-12 23:59:42.769294
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    """Example of calling lgetfilecon_raw"""
    # Suppress warnings about insecure privilege operations
    # (the test will succeed if it can read the context)
    from ansible.module_utils.selinux import supress_sec_failure_warning
    supress_sec_failure_warning()

    rc, con = lgetfilecon_raw(b'/')
    print('%s: %s' % (rc, con))



# Generated at 2022-06-12 23:59:47.454642
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert os.path.exists('/etc/selinux')
    assert lgetfilecon_raw('/etc/selinux')[0] == 0
    assert os.path.exists('/etc/selinux/config')
    assert lgetfilecon_raw('/etc/selinux/config')[0] == 0

# Generated at 2022-06-12 23:59:49.910535
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert to_native(lgetfilecon_raw('/etc/passwd')[1]) == 'system_u:object_r:etc_runtime_t:s0'



# Generated at 2022-06-12 23:59:52.255426
# Unit test for function matchpathcon
def test_matchpathcon():
    try:
        assert matchpathcon('/bin/bash', 0o700) == [0, 'system_u:object_r:bin_t:s0']
    except:
        assert False


# Generated at 2022-06-12 23:59:56.583601
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = '/etc/passwd'
    res = lgetfilecon_raw(path)
    assert res[0] == 0
    assert res[1] == 'system_u:object_r:etc_runtime_t:s0'


# Generated at 2022-06-13 00:00:04.681102
# Unit test for function matchpathcon
def test_matchpathcon():
    import os
    import sys
    sys.stderr.write("You have to run this as root\n")
    path = "/"
    newcon = "unlabeled_t"
    [rc, con] = matchpathcon(path, 0)
    sys.stderr.write("Your original context is " + con + "\n")
    sys.stderr.write("Your new context will be " + newcon + "\n")
    [rc, con] = lsetfilecon(path, newcon)
    [rc, con] = matchpathcon(path, 0)
    sys.stderr.write("Your new context is " + con + "\n")

# Generated at 2022-06-13 00:00:08.647618
# Unit test for function matchpathcon
def test_matchpathcon():
    assert matchpathcon('/home/somedir', 0) == [0, 'system_u:object_r:user_home_dir_t']
    assert matchpathcon('/home/somedir', 1) == [0, 'system_u:object_r:user_home_dir_t']

# Generated at 2022-06-13 00:00:11.186496
# Unit test for function matchpathcon
def test_matchpathcon():
    # FIXME: this will only work if SELinux is disabled or in permissive mode
    assert matchpathcon(__file__, 0)[1] == 'unlabeled_t'

# Generated at 2022-06-13 00:00:14.229308
# Unit test for function matchpathcon
def test_matchpathcon():
    path = "/dev/null"
    (rc, con) = matchpathcon(path, 0)
    assert rc == 0
    assert con == "system_u:object_r:nul_device_t:s0"


# Generated at 2022-06-13 00:00:17.935323
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    if not is_selinux_enabled():
        pytest.skip("selinux is not enabled")
        return
    rc, con = lgetfilecon_raw("/")
    assert rc == 0
    assert con == "system_u:object_r:root_t:s0"

# Generated at 2022-06-13 00:00:25.223212
# Unit test for function matchpathcon
def test_matchpathcon():
    if not os.getenv('PYTHON_SELINUX_UNIT_TEST', False):
        sys.stderr.write('PYTHON_SELINUX_UNIT_TEST not set, skipping unit tests\n')
        return

    rc, con = matchpathcon('/home', 0)
    print(rc, con)

    rc, con = matchpathcon('/home/myuser', 0)
    print(rc, con)

    rc, con = matchpathcon('/home/myuser/a/b/c', 0)
    print(rc, con)

    rc, con = matchpathcon('/tmp', 0)
    print(rc, con)

    rc, con = matchpathcon('/dev', 0)
    print(rc, con)

    rc, con = matchpathcon

# Generated at 2022-06-13 00:00:28.079530
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = '/tmp/'
    info = lgetfilecon_raw(path)
    assert isinstance(info[0], int)
    assert isinstance(info[1], str)
    assert info[0] == 0


# Generated at 2022-06-13 00:00:40.519688
# Unit test for function matchpathcon
def test_matchpathcon():
    import os
    import sys

    # TODO: Fix this test_matchpathcon test.
    # Something is wrong here with the parameters in matchpathcon.
    # NEED TO TAKE OUT 'context' which is in the 3rd position.
    # This is causing a `TypeError: an integer is required`.
    # Also, 'context' was a pointer to char_p, which is a very weird type to be using.
    # Need to figure out what this 3rd parameter is for.
    if len(sys.argv) < 2:
        print("usage: " + sys.argv[0] + " <PATH>")
        sys.exit(1)
    # This is an extremely odd use of matchpathcon, the 0 should never be used.
    # No documentation on the interwebz seems to indicate correct usage.
    # The answer may be

# Generated at 2022-06-13 00:00:44.515233
# Unit test for function matchpathcon
def test_matchpathcon():
    # Test for Selinux disabled
    selinux.is_selinux_enabled = lambda: False
    assert matchpathcon('', 2) == [0, '']

    # Test for Selinux enabled
    selinux.is_selinux_enabled = lambda: True
    with pytest.raises(OSError, match='unable to load selinux policy file'):
        assert matchpathcon('', 2) == [0, '']


# Generated at 2022-06-13 00:00:55.607961
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Unit test for function lgetfilecon_raw
    test_path = "/etc/shadow"
    test_context = "system_u:object_r:shadow_t:s0"

    test_con = lgetfilecon_raw(test_path)
    if test_con[0] != 0:
        print("Problem getting context of path")
        sys.exit()
    if not test_context == test_con[1]:
        print("Context of path does not match expected context")
        sys.exit()
    print("Test passed for function lgetfilecon_raw")


# Generated at 2022-06-13 00:00:59.619663
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    from ansible.module_utils.selinux import lgetfilecon_raw
    from tempfile import NamedTemporaryFile

    with NamedTemporaryFile() as f:
        rc, con = lgetfilecon_raw(f.name)
        assert rc == 0
        assert con.startswith('system_u:object_r:')


# Generated at 2022-06-13 00:01:09.539019
# Unit test for function matchpathcon
def test_matchpathcon():
    rc = matchpathcon('/usr/bin/ls', 0)
    assert rc == [0, 'system_u:object_r:bin_t']

    rc = matchpathcon('/usr/bin/ls', os.S_IFDIR)
    assert rc == [0, 'system_u:object_r:bin_t']

    rc = matchpathcon('/usr/bin/ls', os.S_IFREG)
    assert rc == [0, 'system_u:object_r:bin_t']

    rc = matchpathcon('/usr/bin/ls', os.S_IFLNK)
    assert rc == [0, 'system_u:object_r:bin_t']



# Generated at 2022-06-13 00:01:12.030758
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    ret, msg = lgetfilecon_raw('/etc/shadow')
    print('Return code: {}'.format(ret))
    print('  Message: {}'.format(msg))



# Generated at 2022-06-13 00:01:20.794019
# Unit test for function matchpathcon
def test_matchpathcon():
    import subprocess
    import sys

    # make sure SElinux enabled
    rc = selinux_getenforcemode()[1]
    if rc == 0:
        print("Please enable SElinux")
        sys.exit()

    try:
        # Make sure /usr/bin/curl exists
        rc = subprocess.check_output(['ls', '/usr/bin/curl'])
    except:
        print("/usr/bin/curl does not exist. Please install curl")
        sys.exit()
    # print out domain and type of /usr/bin/curl
    print("/usr/bin/curl domain:type ", matchpathcon('/usr/bin/curl', 0)[1])
    sys.exit()

if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-13 00:01:22.878782
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import ansible_collections.ansible.community.plugins.module_utils.selinux as selinux

    assert selinux.lgetfilecon_raw('/etc/shadow')[0] == 0
    assert selinux.lgetfilecon_raw('/nosuchpath')[0] == -1



# Generated at 2022-06-13 00:01:33.531036
# Unit test for function matchpathcon
def test_matchpathcon():
    file_path = "/tmp/foo"
    try:
        os.mkdir(file_path)
    except OSError:
        pass

    try:
        f = open(file_path + "/bar", "w")
        f.close()
    except IOError:
        pass

    result = matchpathcon(file_path + "/bar", 0)
    assert result[0] == 0
    result = lgetfilecon_raw(file_path + "/bar")
    assert result[0] == 0
    result = security_getenforce()
    assert result == 0 or result == 1
    result = selinux_getenforcemode()
    assert result[0] == 0 and (result[1] == 0 or result[1] == 1)
    result = is_selinux_enabled()
    assert result == 1

# Generated at 2022-06-13 00:01:37.711459
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = '/etc/passwd'
    result = lgetfilecon_raw(path)
    # If no errors are detected, the return code is 0 and result[0] is 0
    assert result[0] == 0
    label_example = 'system_u:object_r:etc_t:s0'
    # If the security context is set, it prints the context in result[1]
    assert result[1] == label_example



# Generated at 2022-06-13 00:01:39.560773
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon('/selinux/foo', 0)
    assert rc == 0
    assert con == 'system_u:object_r:selinux_var_t:s0'

# Generated at 2022-06-13 00:01:48.963277
# Unit test for function matchpathcon
def test_matchpathcon():
    import subprocess
    result = matchpathcon('/etc/passwd', os.O_RDONLY)
    assert result[0] == 0
    assert result[1] == b'user_u:object_r:passwd_file_t:s0'
    result = matchpathcon('/etc/passwd', os.O_RDWR)
    assert result[0] == 0
    assert result[1] == b'user_u:object_r:passwd_file_t:s0'
    result = matchpathcon('/etc/passwd', os.O_RDONLY | os.O_WRONLY)
    assert result[0] == 0
    assert result[1] == b'user_u:object_r:passwd_file_t:s0'

# Generated at 2022-06-13 00:01:56.104937
# Unit test for function matchpathcon
def test_matchpathcon():
    assert matchpathcon('/foo', -1) == [0, 'system_u:object_r:usr_t:s0']

# Generated at 2022-06-13 00:02:04.627137
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    """
    Test the lgetfilecon_raw() function
    """
    # verify someones home directory
    home_dir = os.path.expanduser('~')
    returned = lgetfilecon_raw(home_dir)
    if returned[0] != -1:
        raise AssertionError("Failed to retrieve security context for {0}.  Returned {1}".format(home_dir, returned[1]))
    # check for error return
    returned = lgetfilecon_raw('/path/does/not/exist')
    if returned[0] != -1:
        raise AssertionError("Failed lgetfilecon_raw test for non-existent file Should have returned -1.  Returned {0}.".format(returned[0]))
    # check for failure on wrong type of input

# Generated at 2022-06-13 00:02:09.836099
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (rc, con) = lgetfilecon_raw('/etc/selinux/config')
    print(rc, con)

if __name__ == '__main__':
    test_lgetfilecon_raw()

# Generated at 2022-06-13 00:02:16.177350
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    if not is_selinux_enabled():
        print('selinux is not enabled')
        return

    import tempfile
    import os

    tmpdir = tempfile.mkdtemp()
    tmpfile = tempfile.NamedTemporaryFile(prefix=tmpdir)
    print(tmpfile.name, tmpfile.read())
    tmpfile.close()
    print(lgetfilecon_raw(tmpfile.name)[1])
    os.unlink(tmpfile.name)
    os.rmdir(tmpdir)


if __name__ == "__main__":
    test_lgetfilecon_raw()

# Generated at 2022-06-13 00:02:29.052772
# Unit test for function matchpathcon
def test_matchpathcon():
    # Argument must be a string
    test_str = "ThisIsNotAString"
    try:
        matchpathcon(test_str, 0)
    except TypeError:
        pass
    else:
        assert False, "TypeError not raised for matchpathcon"
    # Argument must be an absolute path
    test_str = "./relative/path"
    try:
        matchpathcon(test_str, 0)
    except OSError:
        pass
    else:
        assert False, "OSError not raised for matchpathcon"
    # Argument must exist
    test_str = "/no/such/file"
    try:
        matchpathcon(test_str, 0)
    except OSError:
        pass
    else:
        assert False, "OSError not raised for matchpathcon"
    #

# Generated at 2022-06-13 00:02:37.073325
# Unit test for function matchpathcon
def test_matchpathcon():
    # Based on selinux-python test
    # python2.7/selinux/test_selinux.py

    def dummy_calloc(nmemb, size):
        return "a" * size * nmemb

    def dummy_snprintf(str, size, format, arg):
        str = "dummycon"
        pass

    _selinux_lib.calloc = dummy_calloc
    _selinux_lib.snprintf = dummy_snprintf
    result = matchpathcon("/", 0)
    assert result[1] == "dummycon"

    # Based on selinux-python test
    # python2.7/selinux/test_selinux.py

    def dummy_calloc(nmemb, size):
        return "a" * size * nmemb


# Generated at 2022-06-13 00:02:43.032831
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import tempfile
    import selinux
    import grp

    # create tmp file to get SELinux context of
    tmpfile = tempfile.NamedTemporaryFile()
    file_path = tmpfile.name

    # verify path returned by function is what we expect
    [rc, con] = selinux.lgetfilecon_raw(file_path)
    assert rc == 0
    assert con == "/usr/bin/python3.6 user_u:object_r:user_tmp_t:s0"

# Generated at 2022-06-13 00:02:45.674282
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = "/tmp"
    rc, con = lgetfilecon_raw(path)
    print('{0}'.format(rc))
    print(con)


if __name__ == '__main__':
    test_lgetfilecon_raw()

# Generated at 2022-06-13 00:02:48.730732
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw('/tmp')
    assert rc == 0
    assert con.startswith('system_u:object_r:tmp_t:s0')


# Generated at 2022-06-13 00:02:54.374819
# Unit test for function matchpathcon
def test_matchpathcon():
    """Test if matchpathcon wrapper works correctly"""
    test_path = "/etc"
    context = matchpathcon(test_path, 0)
    assert context[0] == 0
    assert context[1] == "system_u:object_r:etc_t:s0"


# Generated at 2022-06-13 00:03:02.145253
# Unit test for function matchpathcon
def test_matchpathcon():
    res = matchpathcon("/tmp", 0)
    assert res[0] == 0
    assert res[1] == "system_u:object_r:tmp_t:s0"


if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-13 00:03:06.426599
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    test_path = os.path.join('/tmp', 'Testfile1')
    try:
        fd = os.open(test_path, os.O_CREAT, 0o775)
        os.close(fd)
        rc, out = lgetfilecon_raw(test_path)
        assert isinstance(out, unicode)
        assert rc == 0
    finally:
        os.remove(test_path)


# Generated at 2022-06-13 00:03:09.241674
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon("/usr/bin/ping", 0)
    assert rc == 0
    assert con == "system_u:object_r:bin_t:s0"

# Generated at 2022-06-13 00:03:18.434832
# Unit test for function matchpathcon
def test_matchpathcon():
    # Let's assume we are already running under selinux
    # This test is meant to run on a system with SELinux enabled
    if not is_selinux_enabled():
        raise Exception("SELinux is not turned on in this test machine")
    # Create two paths
    # One that should exist on all machines
    # One that will not exist
    good_path = "/proc"
    bad_path = "/doesnotexist"
    (rc, con) = matchpathcon(good_path, os.R_OK)
    if rc < 0:
        raise Exception("Could not get SELinux context for %s" % good_path)
    if len(con) == 0:
        raise Exception("Context string is empty")
    (rc, con) = matchpathcon(bad_path, os.R_OK)
   

# Generated at 2022-06-13 00:03:21.124017
# Unit test for function matchpathcon
def test_matchpathcon():
    (rc, con) = matchpathcon('/tmp/test.foo', 0)
    print('rc=', rc)
    print('con=', con)


if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-13 00:03:32.009443
# Unit test for function matchpathcon
def test_matchpathcon():
    import os
    import sys
    import tempfile

    if not os.path.exists('/usr/bin/matchpathcon'):
        print('SKIPPING: matchpathcon test: no matchpathcon binary')
        return


# Generated at 2022-06-13 00:03:41.394169
# Unit test for function matchpathcon
def test_matchpathcon():
    expected_rc = 0
    con = "/bin/bash u:r:shell_exec:s0"
    expected_con = con
    rc, result_con = matchpathcon("/bin/bash", 0)
    if rc != expected_rc:
        print(
            "error: unexpected return code %i, expected to be %i\n" % (
                rc, expected_rc
            )
        )
    if result_con != con:
        print(
            "error: unexpected result_con %s, expected to be %s\n" % (
                result_con, expected_con
            )
        )


# Generated at 2022-06-13 00:03:45.440753
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    """
    Python unit tests for function lgetfilecon_raw
    """
    rc, con = lgetfilecon_raw("/etc")

    if rc == -1:
        raise Exception("lgetfilecon_raw failed")

    print("con = %s\n" % con)

if __name__ == "__main__":
    test_lgetfilecon_raw()

# Generated at 2022-06-13 00:03:49.513484
# Unit test for function matchpathcon
def test_matchpathcon():
    import selinux
    con = c_char_p()
    path = '/path/to/dir'

    # selinux.matchpathcon returns [rc, con]
    rc = selinux.matchpathcon(path, 0)[0]
    # rc = 0 means the context is found
    assert rc == 0, 'matchpathcon is not working'
    assert con.value != None, 'context is None'
    print('Context is: %s' % con.value);


# Generated at 2022-06-13 00:03:57.712538
# Unit test for function matchpathcon
def test_matchpathcon():

    # Happy path tests
    path = "/foo/bar"
    mode = os.stat(path).st_mode
    rc, ctx = matchpathcon(path, mode)
    print(ctx)

    # Error path tests

    # Bad path
    path = "/missing/file"
    try:
        matchpathcon(path, mode)
    except OSError as ex:
        print("OSError: " + ex.strerror)

    # Unsupported mode
    path = "/foo/bar"
    mode = -1
    try:
        matchpathcon(path, mode)
    except OSError as ex:
        print("OSError: " + ex.strerror)


# Generated at 2022-06-13 00:04:10.170475
# Unit test for function matchpathcon
def test_matchpathcon():
    try:
        rc, result = matchpathcon('/usr', 0)
        assert result == 'system_u:object_r:usr_t'
    except ImportError:
        # selinux not available
        pass

# Generated at 2022-06-13 00:04:12.740818
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():

    raw_str = lgetfilecon_raw('/usr/bin/systemctl')[1]

    assert raw_str is not None

# Generated at 2022-06-13 00:04:14.772119
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw('/etc/passwd')[0] == 0

# Generated at 2022-06-13 00:04:19.426533
# Unit test for function matchpathcon
def test_matchpathcon():
    rc = matchpathcon('/etc/passwd', 0)[0]
    if rc < 0:
        msg = "selinux_lib.matchpathcon() failed with return code: %d" % rc
        raise AssertionError(msg)

if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-13 00:04:21.155078
# Unit test for function matchpathcon
def test_matchpathcon():
    # Test matchpathcon(path, mode)
    # FIXME: write unit test
    pass

# Generated at 2022-06-13 00:04:23.261003
# Unit test for function matchpathcon
def test_matchpathcon():
    if not is_selinux_enabled():
        return

    rc, con = matchpathcon('/etc/', 0)

# Generated at 2022-06-13 00:04:25.163182
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    context = lgetfilecon_raw(__file__)[1]
    assert context

# Generated at 2022-06-13 00:04:35.115705
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Test normal case
    # TODO: test this function with different path

    # Test abnormal case: if the path is not exist
    if not os.path.exists('/foo/bar'):
        out = lgetfilecon_raw('/foo/bar')
        rc = out[0]
        assert rc == -1

    # Test abnormal case: if the path is a directory
    assert os.path.isdir('/home')
    out = lgetfilecon_raw('/home')
    rc = out[0]
    assert rc == -1

    # Test abnormal case: if the path is None
    out = lgetfilecon_raw(None)
    rc = out[0]
    assert rc == -1



# Generated at 2022-06-13 00:04:39.238714
# Unit test for function matchpathcon
def test_matchpathcon():
    (rc, con) = matchpathcon('/usr/sbin/semodule', 0)
    print("semodule context is:")
    print(con)
    print("rc = {0}".format(rc))



# Generated at 2022-06-13 00:04:41.734451
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    f_name = '/etc/hosts'
    f_con = lgetfilecon_raw(f_name)
    assert len(f_con) == 2
    assert f_con[1]

# Generated at 2022-06-13 00:05:00.810208
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    try:
        f = open('/tmp/ansible_selinux_testfile', 'w')
    except:
        print("Unable to open file for writing")
        sys.exit(1)
    try:
        f.write("This is a test file")
    finally:
        f.close()
    rc, context = lgetfilecon_raw('/tmp/ansible_selinux_testfile')
    if rc != 0:
        print("Error in lgetfilecon_raw: %d" % rc)
        sys.exit(1)

# Generated at 2022-06-13 00:05:05.585330
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Create a file and test with it
    path = os.path.join('/tmp', str(os.getpid()))
    os.system("touch %s" % path)
    assert lgetfilecon_raw(path)[0] == 0
    os.system("rm -f %s" % path)



# Generated at 2022-06-13 00:05:07.351430
# Unit test for function matchpathcon
def test_matchpathcon():
    assert matchpathcon('/etc', 0) == [0, u'system_u:object_r:etc_t:s0']

# Generated at 2022-06-13 00:05:10.806863
# Unit test for function matchpathcon
def test_matchpathcon():
    path = '/tmp/foo'
    mode = os.R_OK
    try:
        rc, con = matchpathcon(path, mode)
        assert rc == 0
        assert con is not None
    except OSError as e:
        if e.errno == 13:
            print("Permission denied on %s, skipping test" % path)
        else:
            assert False

# Generated at 2022-06-13 00:05:11.537694
# Unit test for function matchpathcon
def test_matchpathcon():
    return matchpathcon("/etc/hosts", 0)

# Generated at 2022-06-13 00:05:14.935151
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw('/etc/passwd')
    assert rc == 0
    assert con.startswith('unconfined_u')

# Generated at 2022-06-13 00:05:21.419147
# Unit test for function matchpathcon
def test_matchpathcon():
    path = "/var/lib/libvirt/images/test.img"
    mode = os.R_OK | os.W_OK
    [rc, con] = matchpathcon(path, mode)
    assert isinstance(con, str)
    assert con.startswith("system_u:object_r:")
    assert rc == 0


# Generated at 2022-06-13 00:05:28.219532
# Unit test for function matchpathcon
def test_matchpathcon():
    import pytest
    from os.path import join

    from ansible.module_utils.common.text.converters import to_bytes

    # test data
    path = join(b"/path", b"to", b"file")
    no_se_label = b"<<none>>"
    system_u_object_r_file_system_t = b"system_u:object_r:file_system_t"

    # selinux_enabled  ->  selinux_mls_enabled
    # -------          ->  ---------------
    #       0          ->  0               --> <<none>>
    #       0          ->  1               --> <<none>>
    #       1          ->  0               --> system_u:object_r:file_system_t
    #       1          ->  1               --> system_u:object_r

# Generated at 2022-06-13 00:05:38.523436
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict(
            path=dict(type='path'),
        )
    )

    path = module.params.get('path')
    if not path:
        module.fail_json(msg='Missing required argument: path')

    try:
        rc, context = lgetfilecon_raw(path)
    except Exception as e:
        module.fail_json(msg=to_native(e))

    if rc < 0:
        module.fail_json(msg='unable to get selinux context for: {0}: {1}'.format(path, context))

    module.exit_json(changed=False, context=context)


if __name__ == '__main__':
    test_lgetfilecon_raw

# Generated at 2022-06-13 00:05:48.195879
# Unit test for function matchpathcon
def test_matchpathcon():
    import tempfile
    sys.stdout = open(os.devnull, 'wb')

    # check files
    if os.getuid() != 0:
        return 0

    # create a temp file
    tmp_fh, tmp_filepath = tempfile.mkstemp()
    filename = os.path.split(tmp_filepath)[1]
    pathname = tmp_filepath.replace(filename, '')

    rc, mode = matchpathcon(pathname, 0)
    rc, con = matchpathcon(pathname, 0)

    if rc != 0:
        # throw exception on failure
        raise OSError(rc, 'matchpathcon call failed')

    # cleanup temp file
    os.close(tmp_fh)
    os.unlink(tmp_filepath)



# Generated at 2022-06-13 00:06:18.962819
# Unit test for function matchpathcon
def test_matchpathcon():
    if not os.path.isfile('/usr/sbin/selinuxenabled'):
        return

    if not is_selinux_enabled()[1]:
        return

    enforcemode = selinux_getenforcemode()[1]

    # If SELinux is not in enforcing mode, don't run.
    if enforcemode == 0:
        return

    policy_type = selinux_getpolicytype()[1]

    path = '/etc/passwd'

    # If matchpathcon does not match the policy type, don't run.
    if policy_type.lower() != 'targeted':
        return

    # If lgetfilecon_raw fails, don't run
    if lgetfilecon_raw(path)[0] != 0:
        return

    # If matchpathcon fails, don't run

# Generated at 2022-06-13 00:06:21.276884
# Unit test for function matchpathcon
def test_matchpathcon():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict(
            path=dict(type='str'),
            mode=dict(type='int', required=True),
        )
    )

    rc, con = matchpathcon(module.params['path'], module.params['mode'])

    if rc == 0:
        module.exit_json(rc=rc, con=con)
    else:
        module.fail_json(msg=rc)

# Generated at 2022-06-13 00:06:22.470804
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw('/') == [0, 'root:object_r:root_t:s0\n']


# Generated at 2022-06-13 00:06:24.059182
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw('/etc') == [0, 'system_u:object_r:etc_t:s0']

# Generated at 2022-06-13 00:06:30.305089
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # test_path is the absolute path of the file
    test_path = "/var/log/test.log"
    test_result = lgetfilecon_raw(test_path)
    if test_result[0] == 0:
        print(test_result[1])
    else:
        print("Error {0}: {1}".format(test_result[0], test_result[1]))



# Generated at 2022-06-13 00:06:32.561877
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import os.path
    path = os.path.abspath(__file__)
    lgetfilecon_raw(path)

# Generated at 2022-06-13 00:06:39.454061
# Unit test for function matchpathcon
def test_matchpathcon():
    # initialize vars
    path = b"/etc/shadow"
    mode = 0

    # run program/function
    # FIXME: will want to check rc in non-debugging mode
    rc, con = matchpathcon(path, mode)
    print(
        "matchpathcon(\"%s\", %i) -> %s"
        % (to_native(path), mode, rc))
    # TODO: check rc

    # finalize program/function


# Generated at 2022-06-13 00:06:45.557920
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert isinstance(lgetfilecon_raw('/etc/hosts'), tuple)
    assert isinstance(lgetfilecon_raw('/etc/hosts')[0], int)
    assert isinstance(lgetfilecon_raw('/etc/hosts')[1], str)
    assert isinstance(lgetfilecon_raw('/etc/hosts')[1].split(':')[2], str)
    assert isinstance(lgetfilecon_raw('/etc/hosts')[1].split(':')[3], str)



# Generated at 2022-06-13 00:06:48.377508
# Unit test for function matchpathcon
def test_matchpathcon():
    path = "/tmp/file"
    (rc, context) = matchpathcon(path)
    assert rc == 0
    assert context == "system_u:object_r:tmp_t:s0"

# Generated at 2022-06-13 00:06:53.070592
# Unit test for function matchpathcon
def test_matchpathcon():
    if not is_selinux_enabled():
        print("SELinux is disabled. Unable to validate results. Skipping assertions")
        return
    (rc, con) = matchpathcon("/etc/passwd", 0)
    assert rc == 0
    assert con == "system_u:object_r:etc_runtime_t:s0"

# Generated at 2022-06-13 00:07:32.567429
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw(b'/etc/passwd')[0] == 0

# Generated at 2022-06-13 00:07:33.721738
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = "/tmp"
    assert lgetfilecon_raw(path)[0] == 0

# Generated at 2022-06-13 00:07:39.902779
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import json
    try:
        with open('/bin/cat', 'r') as f:
            # Unused, but required to validate path arg exists
            f.close()
    except IOError:
        print('SKIP: unable to find /bin/cat to test lgetfilecon_raw')
        return

    result = lgetfilecon_raw('/bin/cat')
    print(json.dumps({'lgetfilecon_raw': result}, sort_keys=True))



# Generated at 2022-06-13 00:07:43.352573
# Unit test for function matchpathcon
def test_matchpathcon():
    matchpathcon('/etc/shadow', 0)

# Generated at 2022-06-13 00:07:48.666270
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = os.path.expanduser('~/')
    context_list = lgetfilecon_raw(path)
    rc = context_list[0]
    context = context_list[1]
    if rc == -1:
        raise OSError(os.strerror(get_errno()))
    assert not os.environ.get('SELINUX_IGNORE_NEVERALLOWS')



# Generated at 2022-06-13 00:07:53.800817
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert os.path.isdir('/usr/lib/x86_64-linux-gnu/')
    assert lgetfilecon_raw('/usr/lib/x86_64-linux-gnu/')[1] == 'system_u:object_r:usr_t:s0'
    assert lgetfilecon_raw('/usr/lib/x86_64-linux-gnu/libselinux.so.1')[1] == 'system_u:object_r:usr_t:s0'
    assert lgetfilecon_raw('/usr/lib/x86_64-linux-gnu/libselinux.so.1.0.0')[1] == 'system_u:object_r:usr_t:s0'

# Generated at 2022-06-13 00:07:56.333887
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw('/etc/fstab')
    assert rc == 0
    assert con == 'system_u:object_r:etc_t:s0'



# Generated at 2022-06-13 00:08:02.869516
# Unit test for function matchpathcon
def test_matchpathcon():
    # test case where the file exists
    def test1():
        rc, con = matchpathcon('/tmp', 0o666)
        # On success rc returns 0, not the length of the string returned
        assert rc == 0
        # The string returned should be a valid SELinux context
        assert len(con.split(":")) == 4

    # test case where the file does not exists
    def test2():
        rc, con = matchpathcon('/nonexistant-dir/nonexisting-file', 0o666)
        assert rc == 2 and con == ''

    test1()
    test2()

# Generated at 2022-06-13 00:08:06.808032
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    test_file = '/etc/selinux/config'
    retval = lgetfilecon_raw(test_file)
    assert retval[0] == 0
    assert type(retval[1]) is str
    assert retval[1].startswith('system_u:object_r:etc_t')


# Generated at 2022-06-13 00:08:16.607281
# Unit test for function matchpathcon
def test_matchpathcon():
    '''
    Validate that expected return values are returned.
    '''
    # While it is a bit silly for these tests to excercise the selinux library
    # to determine the runpath, there is little to no chance that this path will
    # ever be found on any CI system.
    # TODO: consider using os.getlogin() to return the username, and use that for
    # the path variable, that would enable the test to be run as root, and thus
    # have a more realistic test set.
    testdirs = [
        '/usr/sbin/selinux-python-tests',
        '/home/selinux-python-tests',
        '/var/lib/selinux-python-tests',
    ]

    for path in testdirs:
        actual = matchpathcon(path, 0)
        assert actual