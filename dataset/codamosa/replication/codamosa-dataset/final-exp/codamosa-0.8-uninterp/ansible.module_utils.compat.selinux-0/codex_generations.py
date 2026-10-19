

# Generated at 2022-06-12 23:59:11.673653
# Unit test for function matchpathcon
def test_matchpathcon():

    (rc, con) = matchpathcon('/foo', 0)
    assert rc == 0
    assert con == 'u:object_r:foo_t:s0'

    (rc, con) = matchpathcon('/bar', 0)
    assert rc == 0
    assert con == 'u:object_r:bar_t:s0'

    (rc, con) = matchpathcon('/nonexistent', 0)
    assert rc == 0
    assert con == 'u:object_r:default_t:s0'

# Generated at 2022-06-12 23:59:17.704736
# Unit test for function matchpathcon
def test_matchpathcon():
    path = '/var/log/audit.log'
    mode = os.R_OK | os.W_OK
    policy, rc = matchpathcon(path, mode)
    if rc != 0:
        print('Error getting security context: Error: {0}'.format(rc))
    else:
        print('Context: {0}'.format(policy))

# Generated at 2022-06-12 23:59:27.752573
# Unit test for function matchpathcon
def test_matchpathcon():
    from ansible_collections.misc.not_a_real_collection.plugins.module_utils.selinux import matchpathcon
    from ansible_collections.misc.not_a_real_collection.plugins.module_utils.selinux import SELINUX_CONTEXT_SUCCESS, SELINUX_CONTEXT_DEFAULT

    [rc, context] = matchpathcon("/bin/sh", SELINUX_CONTEXT_SUCCESS | SELINUX_CONTEXT_DEFAULT)
    assert rc == 0
    assert context == 'system_u:object_r:shell_exec_t:s0'

    [rc, context] = matchpathcon("/bin/sh", SELINUX_CONTEXT_SUCCESS)
    assert rc == 0

# Generated at 2022-06-12 23:59:30.813855
# Unit test for function matchpathcon
def test_matchpathcon():
    path = '/tmp'
    mode = 0
    rc, con = matchpathcon(path, mode)
    assert rc == 0
    assert con == 'system_u:object_r:tmp_t'



# Generated at 2022-06-12 23:59:32.354310
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    print(lgetfilecon_raw(b"/"))


# Generated at 2022-06-12 23:59:37.207930
# Unit test for function matchpathcon
def test_matchpathcon():
    import os

    [rc, con] = matchpathcon('/usr/bin/id', 0)
    [rc, con2] = matchpathcon('/usr/bin/sudo', 0)
    assert con == 'system_u:object_r:bin_t:s0'
    assert con2 != 'system_u:object_r:bin_t:s0'


if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-12 23:59:45.366514
# Unit test for function matchpathcon
def test_matchpathcon():
    """Incomplete test for selinux_lib.matchpathcon().

    The function basically just tests if the correct return values are present and if they
    are what they seem to be. A real testing would require to check if the value is correct.
    """
    mode = os.path.stat('/tmp').st_mode
    path = '/tmp'
    rc, mode_se = matchpathcon(path, mode)
    assert rc == 0, "matchpathcon returned an error code"
    assert mode_se[:3] == 'u:o', "matchpathcon did not return a SELinux context"

# Generated at 2022-06-12 23:59:53.680875
# Unit test for function matchpathcon
def test_matchpathcon():
    from __main__ import matchpathcon
    from ansible_collections.notstdlib.moveitallout.tests.unit.modules.utils.fixtures.selinux import matchpathcon_stdout

    try:
        foo = matchpathcon("/foo", 0)
        assert foo[0] == 0
    except OSError as e:
        if e.errno == 22 and e.strerror == 'Invalid argument':
            pass
        else:
            raise RuntimeError("test_matchpathcon: Unexpected exception")

    try:
        foo = matchpathcon("/foo", 10)
        assert foo[0] == 0
    except OSError as e:
        if e.errno == 13 and e.strerror == 'Permission denied':
            pass

# Generated at 2022-06-12 23:59:59.392732
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    from tempfile import mkstemp

    (fd, path) = mkstemp()
    os.close(fd)

    try:
        (rc, con) = lgetfilecon_raw(path)
        print('rc = {0}, con = \'{1}\''.format(rc, con))
    finally:
        os.remove(path)


# Unit test function selinux_getenforcemode

# Generated at 2022-06-13 00:00:04.624925
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (rc, value) = lgetfilecon_raw('/etc/selinux')
    if rc == -1:
        errno = get_errno()
        print('call to lgetfilecon_raw failed: {0}'.format(os.strerror(errno)))
    else:
        print('call to lgetfilecon_raw returned {0}: {1}'.format(rc, value))

# Generated at 2022-06-13 00:00:16.236682
# Unit test for function matchpathcon
def test_matchpathcon():
    # this test only works with selinux enabled
    if not is_selinux_enabled():
        return

    # sanity check that we're getting good results
    rc, con = matchpathcon('/', 0)
    if rc < 0:
        raise RuntimeError('failed to get selinux context ({0} {1})'.format(rc, con))

    if con == '<<none>>:<<none>>:<<none>>':
        raise RuntimeError('selinux context is not valid')

    # now try to match a bogus path
    rc, con = matchpathcon('/bogus/path', 0)
    if rc != -2:
        raise RuntimeError('selinux returned unexpected value ({0} {1})'.format(rc, con))

# Generated at 2022-06-13 00:00:18.825941
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon("/etc/nsswitch.conf", os.R_OK)
    assert rc == 0, "failed to retrieve selinux context: {0}".format(rc)
    assert con is not None, "failed to retrieve selinux context"

# Generated at 2022-06-13 00:00:28.079591
# Unit test for function matchpathcon
def test_matchpathcon():
    module = sys.modules[__name__]
    assert module.matchpathcon('/usr/bin/true', 0) == [0, 'system_u:object_r:bin_t:s0']
    assert module.matchpathcon('/usr/bin/true', 1) == [0, 'system_u:object_r:bin_t:s0']
    assert module.matchpathcon('/var/empty', 0) == [0, 'system_u:object_r:empty_t:s0']
    assert module.matchpathcon('/var/empty', 1) == [0, 'system_u:object_r:empty_t:s0']
    assert module.matchpathcon('/var/empty/..', 0) == [0, 'system_u:object_r:var_t:s0']
   

# Generated at 2022-06-13 00:00:29.897928
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    result = lgetfilecon_raw(b"/tmp/existing_file")
    assert result[1].startswith('unconfined_u')


# Generated at 2022-06-13 00:00:34.827424
# Unit test for function matchpathcon
def test_matchpathcon():
    for filename in ['/etc/passwd', '/root', '/tmp/test']:
        print(filename, matchpathcon(filename, os.R_OK))


if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-13 00:00:38.552725
# Unit test for function matchpathcon
def test_matchpathcon():
    path = '/var/log'
    mode = 0o644
    context = matchpathcon(path, mode)
    assert context[0] == 0
    assert context[1] == 'system_u:object_r:log_t:s0'

# Generated at 2022-06-13 00:00:41.429745
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw('/proc')
    if rc < 0:
        errno = get_errno()
        raise OSError(errno, os.strerror(errno))


# Generated at 2022-06-13 00:00:51.570210
# Unit test for function matchpathcon
def test_matchpathcon():
    if os.getuid() != 0:
        raise ImportError('skipping test for non-root user')

    try:
        rc, con = matchpathcon('/etc/passwd', 0)
    except OSError as e:
        if e.errno == errno.EINVAL:
            # if the kernel is not compiled for SELinux this will always err
            # accordingly, so we can just silently skip the test
            pass
        else:
            raise e
    else:
        assert rc == 0
        assert con.startswith('system_u:object_r:')
        assert con.endswith(':s0')

# Generated at 2022-06-13 00:00:57.123889
# Unit test for function matchpathcon
def test_matchpathcon():
    rc = matchpathcon('/etc/passwd', os.R_OK)
    assert rc[0] == 0 and rc[1] == 'system_u:object_r:passwd_file_t:s0'
    rc = matchpathcon('/tmp/doesnotexist', os.W_OK)
    assert rc[0] == -1 and rc[1] == None


# Generated at 2022-06-13 00:01:00.081490
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = '/etc/passwd'
    result = lgetfilecon_raw(path)
    assert result[0] == 0
    assert isinstance(result[1], str)
    assert result[1].endswith(':etc_t')

# Generated at 2022-06-13 00:01:11.958710
# Unit test for function matchpathcon
def test_matchpathcon():
    # In a docker container
    if os.path.exists('/.dockerenv'):
        print('Skipping matchpathcon test in a container')
        return

    # In an SELinux VM
    if lgetfilecon_raw('/etc/passwd')[0] == 0:
        print('Skipping matchpathcon test in an SELinux VM')
        return

    # On a system with SELinux disabled
    if not is_selinux_enabled():
        print('Skipping matchpathcon test on a system with SELinux disabled')
        return

    fname = '/tmp/testfile'
    with open(fname, 'w'):
        pass

    assert matchpathcon(fname, 0)[0] == 0



# Generated at 2022-06-13 00:01:19.415790
# Unit test for function matchpathcon
def test_matchpathcon():
    """
    Test for matchpathcon function
    """
    import tempfile
    from os.path import join
    from os import chmod
    from shutil import rmtree

    # create dir for tests
    temp_dir = tempfile.mkdtemp()
    temp_file = join(temp_dir, 'foo')
    open(temp_file, 'a').close()
    chmod(temp_file, 0o777)

    # test matchpathcon
    rc, mode_con = matchpathcon(temp_file, 1205)
    assert rc == 0
    assert mode_con == 'system_u:object_r:unlabeled_t:s0'

    # test selinux_getpolicytype
    rc, policy_type = selinux_getpolicytype()
    assert rc == 0

# Generated at 2022-06-13 00:01:21.880377
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    def test_helper(self):
        self.assertEqual(lgetfilecon_raw('/etc/passwd'), [0, 'system_u:object_r:etc_runtime_t:s0'])
        self.assertEqual(lgetfilecon_raw('/nonexistent'), [0, None])


# Generated at 2022-06-13 00:01:28.837504
# Unit test for function matchpathcon
def test_matchpathcon():
    path = "/"  # In most cases, this will be a valid file system path
    mode = 0    # This value is not used in matchpathcon, but must be passed
    rc, con = matchpathcon(path, mode)

    print("The return code is: %s" % rc)
    print("The context is: %s" % con)

# Test matchpathcon for the correct context for a root directory on a Fedora 27 machine

# Generated at 2022-06-13 00:01:37.112742
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():

    from ansible.module_utils.selinux_lib import lgetfilecon_raw
    import pytest
    (rc, thecon) = lgetfilecon_raw("/etc/system-release")
    assert rc == 0
    assert thecon == "system_u:object_r:etc_t:s0"
    (rc, thecon) = lgetfilecon_raw("/etc/system-release-asdf")
    assert rc == -1
    (rc, thecon) = lgetfilecon_raw("/etc/system-release-asdf/asdf")
    assert rc == -1
    # (rc, thecon) = lgetfilecon_raw("/etc/system-relase")
    # assert rc == -1



# Generated at 2022-06-13 00:01:38.761092
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw('/etc/passwd')
    assert rc == 0
    assert con == 'system_u:object_r:passwd_file_t:s0'

# Generated at 2022-06-13 00:01:44.974020
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    """Returns the context for given file path."""
    if is_selinux_enabled():
        file_path_name = '/etc/passwd'
        rc, context = lgetfilecon_raw(file_path_name)
        assert rc == 0
        assert context.startswith('unconfined_u:object_r:')
    else:
        file_path_name = '/dev/null'
        rc, context = lgetfilecon_raw(file_path_name)
        assert rc == -1
        assert get_errno() == 95
        assert context is None

# Generated at 2022-06-13 00:01:49.727019
# Unit test for function matchpathcon
def test_matchpathcon():
    '''
    Test path without matchpathcon
    '''
    path = u'path'
    mode = 0
    expected = [0, to_native('system_u:object_r:etc_runtime_t:s0')]
    actual = matchpathcon(path, mode)
    assert actual == expected, 'expected: {0} actual: {1}'.format(expected, actual)



# Generated at 2022-06-13 00:01:53.223855
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import tempfile

    (fd, path) = tempfile.mkstemp()
    os.close(fd)
    os.unlink(path)

    try:
        os.symlink("/etc/foo", path)

        (rc, con) = lgetfilecon_raw(path)
        if rc < 0 and rc == -22:
            raise OSError
        assert con == '<<none>>'
    finally:
        os.unlink(path)



# Generated at 2022-06-13 00:02:03.193018
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = selinux_getenforcemode()
    if rc != 0:
        print("Failed to get the status of the SELinux")
        return False
    if con != 1:
        print("SELinux is not enforced, please set it to enforcing")
        return False
    rc, policytype = selinux_getpolicytype()
    if rc != 0:
        print("Failed to get the type of the SELinux policy")
        return False
    if policytype != 'selinux':
        print("The type of the SELinux policy is not selinux",
              "Please set it to selinux")
        return False
    rc, con = matchpathcon('/etc/hosts', 0)
    # rc should be 1 because SELinux is not a valid context

# Generated at 2022-06-13 00:02:09.935336
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw('/etc/hosts')[1] == 'system_u:object_r:etc_t:s0'


# Generated at 2022-06-13 00:02:12.144379
# Unit test for function matchpathcon
def test_matchpathcon():
    path = '/etc/shadow'
    mode = os.R_OK
    result = matchpathcon(path, mode)
    print(result)

# Generated at 2022-06-13 00:02:16.702728
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Test the function with a file whose security context has already been set
    [rc1, con1] = lgetfilecon_raw('/tmp/c')
    assert rc1 == 0
    assert con1.split(':')[0] == 'system_u'

    # Test the function on a new file
    [rc2, con2] = lgetfilecon_raw('/tmp/d')
    assert rc2 == 0
    assert con2.split(':')[0] == 'system_u'



# Generated at 2022-06-13 00:02:25.861793
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    '''
    Test of lgetfilecon_raw
    '''
    testpath = '/etc/passwd'

    test_con = 'system_u:object_r:etc_t:s0'

    assert lgetfilecon_raw(testpath)[0] == 0, 'lgetfilecon_raw should return 0'
    assert lgetfilecon_raw(testpath)[1] == test_con, 'lgetfilecon_raw should return expected lgetfilecon'



# Generated at 2022-06-13 00:02:35.174712
# Unit test for function matchpathcon
def test_matchpathcon():
    import os
    import sys

    # Need to be able to resolve path separators on different OS
    if sys.platform == 'win32':
        # Make sure to double-escape the backslash, as we are using
        # a raw string
        path = r'C:\\Users\\user\\.ansible'
    else:
        path = u'/etc/ansible'

    mode = 0

    retval = matchpathcon(path, mode)

    print("retval: %s" % repr(retval))
    print("retval[0]: %s" % repr(retval[0]))
    print("retval[1]: %s" % repr(retval[1]))

    assert(retval[0] == -1)


# Generated at 2022-06-13 00:02:44.369831
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # FIXME: use paramiko here?
    host = os.environ.get('ANSIBLE_TEST_HOST', 'localhost')

    host_tmp_file = '/tmp/ansible_test_file'
    # Do not try to connect to the host if it's localhost as this would cause
    # ansible to attempt to write localhost to the file /tmp/ansible_test_file
    if host == 'localhost':
        host_tmp_file = '/tmp/ansible_test_file'
    else:
        for ssh_conf in ['ansible_ssh_common_arg', 'ansible_ssh_extra_args']:
            ssh_conf_val = os.environ.get(ssh_conf)

# Generated at 2022-06-13 00:02:48.535035
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = "/etc/shadow"
    output = lgetfilecon_raw(path)
    assert output[0] >= 0
    assert output[1].startswith("system_u:object_r:shadow_t")


# Generated at 2022-06-13 00:02:54.578390
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    test_file_path = '/tmp/test_selinux.txt'
    with open(test_file_path, 'w') as f:
        f.write('test')

    rc, context = lgetfilecon_raw(test_file_path)
    assert rc == 0
    assert context is not None



# Generated at 2022-06-13 00:03:04.268645
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    from ansible_collections.notstdlib.moveitallout.tests.unit.modules.utils import set_module_args
    from ansible_collections.notstdlib.moveitallout.plugins.modules import selinux as selinux_module
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat import unittest

    set_module_args({
        'file': '/tmp',
        'context': 'unconfined_u:object_r:user_tmp_t:s0',
    })
    selinux_module.selinux.lsetfilecon_raw = lambda p, c: True  # noqa

# Generated at 2022-06-13 00:03:11.630375
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import tempfile
    import os
    if not os.path.isdir("/tmp"):
        os.mkdir("/tmp")

    with tempfile.NamedTemporaryFile("w", dir="/tmp", delete=False) as tmp:
        # Expected value retuned by lgetfilecon_raw
        expected = ["0", "system_u:object_r:tmp_t:s0"]
        # Actual value returned by the function lgetfilecon_raw
        actual = lgetfilecon_raw(tmp.name)

        assert expected == actual
    os.unlink(tmp.name)


# Generated at 2022-06-13 00:03:17.563360
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    d = lgetfilecon_raw("/proc/1")
    if d[0] != 0:
        raise AssertionError("function lgetfilecon_raw returns {0} instead of 0".format(d[0]))

    if not d[1]:
        raise AssertionError("function lgetfilecon_raw returns empty string instead of valid security context")


# Generated at 2022-06-13 00:03:20.034393
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    [rc, con] = lgetfilecon_raw("/etc/selinux")
    assert rc == 0
    assert con == "system_u:object_r:etc_runtime_t:s0"


# Generated at 2022-06-13 00:03:27.317493
# Unit test for function matchpathcon
def test_matchpathcon():
    sys.path.append('../../')
    from lib.wrappers.selinux_wrappers import matchpathcon

    input_path = 'test'
    input_mode = 0

    [rc, con] = matchpathcon(input_path, input_mode)

    assert rc == -1 and con == '/test system_u:object_r:sock_file_t:s0'
    assert True


# Generated at 2022-06-13 00:03:34.596467
# Unit test for function matchpathcon
def test_matchpathcon():

    # Test case 1: valid matchpathcon call.
    # Expected result: 1, "system_u:object_r:default_t:s0"
    path = '/home'
    mode = 0o777
    exp = (1, "system_u:object_r:default_t:s0")

    result = matchpathcon(path, mode)
    assert result == exp

    # Test case 2: invalid matchpathcon call.
    # Expected result: -1, "Error accessing matchpathcon"
    path = 'invalidpath1'
    mode = 0o777
    exp = (-1, "Error accessing matchpathcon")

    result = matchpathcon(path, mode)
    assert result == exp

    # Test case 3: invalid matchpathcon call.
    # Expected result: -1, "Error accessing matchpath

# Generated at 2022-06-13 00:03:43.816899
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    test_path = '/tmp/selinux_test'

    def _cleanup():
        try:
            os.remove('/tmp/selinux_test')
        except OSError:
            pass

    try:
        with open(test_path, 'wb') as f:
            f.write(b'1234')

        rc, rv = lgetfilecon_raw(test_path)
        assert rc == 0

        # rv should be something like 'system_u:object_r:tmp_t:s0'
        assert len(rv.split(':')) == 4

    finally:
        _cleanup()



# Generated at 2022-06-13 00:03:46.252349
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    lgetfilecon_raw('/')
    lgetfilecon_raw('/etc/passwd')
    lgetfilecon_raw('/etc/shadow')

# Generated at 2022-06-13 00:03:49.012973
# Unit test for function matchpathcon
def test_matchpathcon():
    (rc, con) = matchpathcon("/etc/passwd", 0)
    if rc >= 0:
        print("Success")
        print("Context: {0}".format(con))
    else:
        print("Failed")

if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-13 00:03:49.646445
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw('/')[1]

# Generated at 2022-06-13 00:03:56.064362
# Unit test for function matchpathcon
def test_matchpathcon():
    import tempfile
    import shutil
    import os
    import selinux

    d = tempfile.mkdtemp()
    fn = os.path.join(d, 'a')
    with open(fn, 'wb') as f:
        f.write(b'x')

    try:
        print(selinux.matchpathcon(fn, os.stat(fn).st_mode))
    except Exception as e:
        print("Unexpected exception:", e)
    finally:
        shutil.rmtree(d)

# Generated at 2022-06-13 00:04:00.097955
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw(b'/bin/bash') == [0, 'system_u:object_r:unlabeled_t:s0']
    assert lgetfilecon_raw(b'/etc/fstab') == [0, 'root:object_r:etc_runtime_t:s0']



# Generated at 2022-06-13 00:04:11.479554
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    from ansible.module_utils.selinux_policy import PySELinux
    from ansible.module_utils.selinux_policy import SELinuxError

    test_file = '/tmp/selinux-policy-test'

    try:
        os.remove(test_file)
    except:
        pass

    try:
        os.mknod(test_file, 0o600)
    except:
        raise Exception('Can not create test file')

    # test with empty label
    rc, con = lgetfilecon_raw(test_file)
    if rc < 0:
        raise SELinuxError(rc)

    if con is not None:
        raise Exception('file context is not empty: ' + con)

    # test with label
    #
    # NB: libselinux needs to

# Generated at 2022-06-13 00:04:13.918969
# Unit test for function matchpathcon
def test_matchpathcon():
    assert matchpathcon('/etc/test.txt', 0)[0] == 0



# Generated at 2022-06-13 00:04:21.077029
# Unit test for function matchpathcon
def test_matchpathcon():

    path = '/etc'
    mode = 0
    rc = matchpathcon(path, mode)
    assert rc[0] == 0
    assert rc[1] == "system_u:object_r:etc_t:s0"
    path = '/etc/passwd'
    mode = 0
    rc = matchpathcon(path, mode)
    assert rc[0] == 0
    assert rc[1] == "system_u:object_r:etc_t:s0"



# Generated at 2022-06-13 00:04:27.096074
# Unit test for function matchpathcon
def test_matchpathcon():
    import tempfile
    import shutil
    import random


# Generated at 2022-06-13 00:04:33.625724
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import tempfile
    import os

    temp_fd, temp_path = tempfile.mkstemp(prefix="selinux-")

    # There is no reliable way to test this function other than hope for the best
    rc, context = lgetfilecon_raw(temp_path)
    os.close(temp_fd)
    os.unlink(temp_path)

    print("rc: %d" % rc)
    print("context: %s" % context)


# Generated at 2022-06-13 00:04:39.369748
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    test_file = '/var/tmp/test_file'
    with open(test_file, "w") as f: f.write('foo')

    rc, con = lgetfilecon_raw(test_file)
    # error code should be 0
    assert rc == 0
    # con should have a value
    assert con != None
    os.unlink(test_file)

# Generated at 2022-06-13 00:04:43.916457
# Unit test for function matchpathcon
def test_matchpathcon():
    """
    Check that a valid path returns the expected context on a selinux host
    :return:
    """
    from ansible.module_utils.selinux import matchpathcon
    from ansible.module_utils.selinux import selinux_getenforcemode
    from ansible.module_utils.selinux import selinux_getpolicytype
    from ansible.module_utils.selinux import is_selinux_enabled
    from ansible.module_utils.selinux import is_selinux_mls_enabled

    assert is_selinux_enabled()
    assert is_selinux_mls_enabled()
    assert selinux_getenforcemode()[1] == 1
    assert selinux_getpolicytype()[1] == 'targeted'

    # Stat a known file on the system


# Generated at 2022-06-13 00:04:46.978759
# Unit test for function matchpathcon
def test_matchpathcon():
    path = os.path.expanduser("~/.bashrc")
    t = matchpathcon(path, 0)
    assert t[0] == 0, "Failed to return a zero exit code"
    assert t[1] == "user_home_t", "Failed to return the correct context"


# Generated at 2022-06-13 00:04:52.122128
# Unit test for function matchpathcon
def test_matchpathcon():
    import os
    import tempfile

    tmpdir = tempfile.mkdtemp()
    try:
        rc, value = matchpathcon(tmpdir, 0)
        assert rc == 0
        assert value == "system_u:object_r:tmp_t:s0"
    finally:
        os.rmdir(tmpdir)


# Generated at 2022-06-13 00:04:58.784880
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import os
    path = '/tmp'
    if not os.path.isdir(path):
        raise Exception("Unable to find path")

    rc, res = lgetfilecon_raw(path)
    if rc == -1:
        raise Exception("Unable to get file con extid")
    print("res:", res)

if __name__ == '__main__':
    test_lgetfilecon_raw()

# Generated at 2022-06-13 00:05:04.462646
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (rc, context) = lgetfilecon_raw('/etc/group')

    if rc < 0:
        raise OSError(rc, os.strerror(-rc))
    return context

# Generated at 2022-06-13 00:05:06.878507
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    os.environ['LC_ALL'] = 'C'
    print(lgetfilecon_raw('/etc/passwd'))

if __name__ == "__main__":
    test_lgetfilecon_raw()

# Generated at 2022-06-13 00:05:10.006324
# Unit test for function matchpathcon
def test_matchpathcon():
    con = c_char_p()
    rc = _selinux_lib.matchpathcon(b"/etc/hosts", 0, byref(con))
    assert rc == -1
    assert to_native(con.value) is None
    _selinux_lib.freecon(con)

# Generated at 2022-06-13 00:05:11.711055
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = to_bytes('/etc')
    res = lgetfilecon_raw(path)
    assert res[0] == 0



# Generated at 2022-06-13 00:05:20.358418
# Unit test for function matchpathcon
def test_matchpathcon():
    """
    Unit test:
    >>> matchpathcon("/etc", 0)
    [0, 'system_u:object_r:etc_t']
    >>> matchpathcon("/etc/shadow", 0)
    [0, 'system_u:object_r:shadow_t']
    >>> matchpathcon("/file/that/does/not/exist", 0)
    [-13, 'system_u:object_r:default_t']
    """
    pass


# Generated at 2022-06-13 00:05:22.344947
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    rc, con = lgetfilecon_raw('/etc/fstab')
    assert(rc == 0)


# Generated at 2022-06-13 00:05:24.189506
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    con = lgetfilecon_raw('/bin/ping')
    con = lgetfilecon_raw(b'/bin/ping')



# Generated at 2022-06-13 00:05:25.492919
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    (rc, con) = lgetfilecon_raw(b"/root/")
    print(rc, con)

# Generated at 2022-06-13 00:05:28.216391
# Unit test for function matchpathcon
def test_matchpathcon():
    """
    This test will fail if selinux is not installed
    """
    # for some reason, matchpathcon is only available if we pass in a path
    # that is not a symlink.
    (rc, context) = matchpathcon('/usr/bin/python', os.R_OK)
    assert rc >= 0  # noqa
    assert context  # noqa

# Generated at 2022-06-13 00:05:38.524924
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import os
    import os.path

    TEST_PATH = '/etc/selinux/config'
    TEST_MODE = os.R_OK
    errno_EOPNOTSUPP = 95  # 'Operation not supported'

    if not os.path.isfile(TEST_PATH):
        raise NotImplementedError('test file for selinux not found: {0}'.format(TEST_PATH))

    # first check that selinux is in fact enabled
    if not is_selinux_enabled():
        raise ValueError('selinux is not enabled')

    # next check that we can read the file
    if not os.access(TEST_PATH, TEST_MODE):
        error = OSError(errno_EOPNOTSUPP, os.strerror(errno_EOPNOTSUPP))  # os

# Generated at 2022-06-13 00:05:46.230580
# Unit test for function matchpathcon
def test_matchpathcon():
    test_path = '/etc/selinux/config'
    result = matchpathcon(test_path, os.R_OK)
    assert result[0] == 0
    assert result[1] == 'system_u:object_r:selinux_config_t:s0'

# Generated at 2022-06-13 00:05:47.815164
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    assert lgetfilecon_raw('/')[1].startswith('system_u:object_r:root_t')

# Generated at 2022-06-13 00:05:50.810829
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon('/usr/bin/ansible', 0)
    assert con == 'system_u:object_r:usr_t:s0'

# Generated at 2022-06-13 00:05:57.007344
# Unit test for function matchpathcon
def test_matchpathcon():
    try:
        # Try to match an invalid path.
        rc, label = matchpathcon('/invalid/path/is/invalid', os.R_OK)
        assert rc in [0, 2]
        assert label is None
    except OSError as e:
        # The function should not throw an error.
        # The code below is kept as a reference to the error that showed up once on MacOS.
        assert e.errno == 2
        assert e.strerror == 'No such file or directory'
        assert to_native(os.strerror(e.errno)) == e.strerror

# Generated at 2022-06-13 00:06:07.189316
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon('/etc/dummy', 0)
    assert rc == 0
    assert con == 'system_u:object_r:etc_runtime_t:s0'
    rc, con = matchpathcon('/etc/dummy', 1)
    assert rc == 0
    assert con == 'system_u:object_r:etc_runtime_t:s0'
    rc, con = matchpathcon('/etc/dummy', 2)
    assert rc == 0
    assert con == 'system_u:object_r:etc_runtime_t:s0'
    rc, con = matchpathcon('/etc/dummy', 3)
    assert rc == 0
    assert con == 'system_u:object_r:etc_runtime_t:s0'

# Generated at 2022-06-13 00:06:12.906567
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    from ansible.module_utils.selinux import lgetfilecon_raw

    rc, con = lgetfilecon_raw("/")
    if rc != -1:
        print("Success: con={0}".format(con))
        sys.exit(0)

    err = os.strerror(get_errno())
    print("Failed: error={0}".format(err))
    sys.exit(1)

# Generated at 2022-06-13 00:06:15.720708
# Unit test for function matchpathcon
def test_matchpathcon():
    path = '/tmp/file_matchpathcon'
    open(path, 'a').close()
    # TODO: use policy-based mode
    mode = 0
    response = matchpathcon(path, mode)
    assert response[0] == 0

# Generated at 2022-06-13 00:06:21.622077
# Unit test for function matchpathcon
def test_matchpathcon():
    import tempfile

    con = c_char_p()
    try:
        fd, fname = tempfile.mkstemp(text=False)
        rc = _selinux_lib.matchpathcon(fname, os.stat(fname).st_mode, byref(con))
        assert rc == 0
    except OSError as e:
        assert False, "Exception generated: {0}".format(e)
    finally:
        # os.close(fd)
        # os.remove(fname)
        _selinux_lib.freecon(con)

# Generated at 2022-06-13 00:06:24.063399
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import os.path
    result = lgetfilecon_raw(os.path.realpath(__file__))
    assert result[0] == 0
    assert result[1] == 'unconfined_u:object_r:user_home_t:s0'

# Generated at 2022-06-13 00:06:27.507615
# Unit test for function matchpathcon
def test_matchpathcon():
    # FIXME: incomplete
    filename = '/tmp/testfile.txt'
    with open(filename, 'a') as f:
        f.write('testfile')
    rc, con = matchpathcon(filename, 0)
    assert rc == 0
    assert con == 'system_u:object_r:user_tmp_t:s0'

# Generated at 2022-06-13 00:06:43.633524
# Unit test for function matchpathcon
def test_matchpathcon():
    assert matchpathcon('/', 3) == [0, 'system_u:object_r:root_t:s0']
    assert matchpathcon('/', 4) == [0, 'system_u:object_r:root_t:s0']

    try:
        matchpathcon('foo', 3)
        raise AssertionError('matchpathcon does not check for non-existent paths')
    except OSError as e:
        assert e.errno == 2



# Generated at 2022-06-13 00:06:50.980565
# Unit test for function matchpathcon
def test_matchpathcon():
    path = '/test'
    mode = 0o600
    [rc, con] = matchpathcon(path, mode)
    assert rc == 0
    assert con == 'system_u:object_r:file_t:s0'

# import unit test modules
from ansible.module_utils.selinux_policy import *  # noqa
from ansible.module_utils.selinux_filecontext import *  # noqa
from ansible.module_utils.selinux_boolean import *  # noqa

# Generated at 2022-06-13 00:06:55.766707
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    """
    If the file is not present raise OSError
    """
    try:
        lgetfilecon_raw("/non_existent/path")
    except OSError as e:
        assert e.errno == 2
    else:
        assert False, "Expected OSError"

    """
    If the file is present check for non-empty context
    """

    assert lgetfilecon_raw("/")[1] != ""

# Generated at 2022-06-13 00:07:01.260301
# Unit test for function matchpathcon
def test_matchpathcon():
    rc, con = matchpathcon('/', 0)
    con_expected = 'system_u:object_r:admin_home_t:s0'
    print('\nComparing the results from matchpathcon with the expected results.')
    print('Expected matchpathcon result: "system_u:object_r:admin_home_t:s0"')
    print('  Actual matchpathcon result: "' + str(con) + '"')
    assert con_expected == con, 'test_matchpathcon failed'
    print('  matchpathcon test passed.')

# Generated at 2022-06-13 00:07:06.377514
# Unit test for function matchpathcon
def test_matchpathcon():
    from shutil import copyfile
    from tempfile import mkdtemp
    from itertools import combinations

    import os
    import selinux

    test_dir = mkdtemp()
    fsrc = os.path.join(test_dir, 'src')
    fdst = os.path.join(test_dir, 'dst')
    try:
        os.mkfifo(fsrc)
        os.mkfifo(fdst)
        copyfile(fsrc, fdst)

        for mode, target in combinations((fsrc, fdst), 2):
            rv, con = matchpathcon(target, mode)
            assert con.startswith('system_u:object_r:sock_t:s0')

    finally:
        for target in (fsrc, fdst):
            os.un

# Generated at 2022-06-13 00:07:15.066412
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Call the function
    try:
        rc, con = lgetfilecon_raw('.')
        print('test_lgetfilecon_raw: rc=', rc, 'con=', con)
    except TypeError as e:
        print('test_lgetfilecon_raw: TypeError', e)
        return 1

    except ValueError as e:
        print('test_lgetfilecon_raw: ValueError', e)
        return 1

    except OSError as e:
        print('test_lgetfilecon_raw: OSError', e)
        return 1
    # NOTE: The above error conditions are possible if the
    #       SELinux policy is not enabled.
    #       In that case, this module will not function anyway, so
    #       we can consider an exception as a success.

   

# Generated at 2022-06-13 00:07:24.045032
# Unit test for function matchpathcon
def test_matchpathcon():
    dirs = [
        ('/', 'system_u:object_r:unlabeled_t:s0'),
        ('/dev/null', 'system_u:object_r:chr_file:s0'),
        ('/dev/tty', 'system_u:object_r:chr_file:s0'),
    ]
    for dir, expected_context in dirs:
        context = matchpathcon(dir, 0)[1]
        assert context == expected_context, \
            'Wrong context found for {0}! Expected {1}, but found {2}'.format(dir, expected_context, context)

# Generated at 2022-06-13 00:07:27.890737
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    try:
        rc, con = lgetfilecon_raw(b'/tmp')
        print("[%s]: [%s]" % (rc, con))
    except OSError as e:
        print("[%s]: [%s]" % (e.errno, e.strerror))



# Generated at 2022-06-13 00:07:32.444568
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():

    rc, out = lgetfilecon_raw("/selinux/enforce")

    assert rc == 0
    assert out == "system_u:object_r:selinux_enforce_t:s0"
    assert isinstance(out, str)

    rc, out = lgetfilecon_raw("/selinux/xxxxx")

    assert rc == -1
    assert out == None



# Generated at 2022-06-13 00:07:36.304294
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    # Putting a test at the bottom of the file makes it easier to
    # exclude from the unit test
    assert lgetfilecon_raw('/bin/ls') == [0, 'system_u:object_r:bin_t:s0']


# Generated at 2022-06-13 00:08:00.608581
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    import os
    import tempfile
    from ansible.module_utils.common.text.converters import to_native

    [rc, con] = lgetfilecon_raw('/tmp')
    os.mkdir('/tmp/test_lgetfilecon_raw')
    [rc, con] = lgetfilecon_raw('/tmp/test_lgetfilecon_raw')
    assert con is not None, "file context is null"
    [rc, con] = lgetfilecon_raw('/tmp/test_lgetfilecon_raw/file')
    os.remove('/tmp/test_lgetfilecon_raw/file')
    os.rmdir('/tmp/test_lgetfilecon_raw')
    assert rc == -1, "unexpected rc: got: {0}".format(rc)

# Generated at 2022-06-13 00:08:04.488379
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    filename = "/etc/selinux/config"
    assert os.path.isfile(filename)
    assert os.access(filename, os.R_OK)
    # This is the value of filename in Fedora 31
    assert "system_u:object_r:selinux_config_t:s0" in lgetfilecon_raw(filename)[1]


# Generated at 2022-06-13 00:08:10.300920
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = b"/etc/hosts"
    rc, con = lgetfilecon_raw(path)
    if rc >= 0:
        print("Context of {} is {}".format(to_native(path), to_native(con)))
    else:
        print("Unable to get context of {}".format(to_native(path)))
        print(to_native(os.strerror(rc)))


# Generated at 2022-06-13 00:08:15.802662
# Unit test for function matchpathcon
def test_matchpathcon():
    # Test valid path
    _rc, _con = matchpathcon("/var/lib/libvirt", os.R_OK)
    print("rc: {}, con: {}\n".format(_rc, _con))

    # Test invalid path
    _rc, _con = matchpathcon("/dev/null/bogus", os.R_OK)
    print("rc: {}, con: {}\n".format(_rc, _con))



# Generated at 2022-06-13 00:08:18.348551
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = b'/home/user/local'
    result = lgetfilecon_raw(path)
    assert result == [0, b'system_u:object_r:user_home_dir_t:s0']



# Generated at 2022-06-13 00:08:21.471347
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.selinux import lgetfilecon_raw
    rc, con = lgetfilecon_raw('/')
    assert rc == 0
    assert con == 'system_u:object_r:root_t:s0'



# Generated at 2022-06-13 00:08:24.138388
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    test_path = '/etc/passwd'
    rc, con = lgetfilecon_raw(test_path)
    assert rc == 0
    assert con == 'system_u:object_r:etc_runtime_t:s0'

# Generated at 2022-06-13 00:08:29.125134
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    tmpfile = '/tmp/foo'
    f = open(tmpfile, 'w')
    f.close()
    rc, con = lgetfilecon_raw(tmpfile)
    assert(rc == 0)
    rc, con = lgetfilecon_raw(tmpfile + '/bar')
    assert(rc == -1)
    os.unlink(tmpfile)

# Generated at 2022-06-13 00:08:35.686998
# Unit test for function matchpathcon
def test_matchpathcon():
    import os
    import tempfile
    try:
        os.getuid()
        print(matchpathcon(None, os.R_OK))
        fd, test_filepath = tempfile.mkstemp()
        print(matchpathcon(test_filepath, os.R_OK))
    finally:
        pass
        if fd is not None:
            os.close(fd)
        if test_filepath is not None:
            os.unlink(test_filepath)


if __name__ == '__main__':
    test_matchpathcon()

# Generated at 2022-06-13 00:08:39.424198
# Unit test for function lgetfilecon_raw
def test_lgetfilecon_raw():
    path = "/tmp"
    try:
        (rc, con) = lgetfilecon_raw(path)
    except OSError:
        raise OSError("Path doesn't exist")
    assert isinstance(con, str)
    assert isinstance(rc, int)
    assert rc == 0
