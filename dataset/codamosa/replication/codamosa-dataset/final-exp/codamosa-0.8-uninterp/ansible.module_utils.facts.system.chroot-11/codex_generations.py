

# Generated at 2022-06-13 02:30:19.120780
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() is False

# Generated at 2022-06-13 02:30:25.080426
# Unit test for function is_chroot
def test_is_chroot():

    # needs to be a class with a run_command method
    module = type('test_is_chroot', (object,), {'run_command': None})()

    # printing results to stderr should be enough
    def run_command(cmd, cwd=None, data=None, binary_data=False):
        return (0, cmd[-1], '')
    module.run_command = run_command

    assert is_chroot(module) is False



# Generated at 2022-06-13 02:30:29.287949
# Unit test for function is_chroot
def test_is_chroot():
    # testing under a chroot
    current_path = os.getcwd()
    os.environ['debian_chroot'] = current_path
    assert is_chroot()

    # testing under a non-chroot
    del os.environ['debian_chroot']
    assert not is_chroot()

# Generated at 2022-06-13 02:30:32.936135
# Unit test for function is_chroot
def test_is_chroot():
    try:
        import ansible.module_utils.basic
    except ImportError:
        # If ansible is not in PYTHONPATH,
        # skip the test because the module_utils import fails.
        return
    mod = ansible.module_utils.basic.AnsibleModule(argument_spec={})
    assert not is_chroot(mod)

# Generated at 2022-06-13 02:30:39.433139
# Unit test for function is_chroot
def test_is_chroot():
    # True
    os.environ['debian_chroot'] = 'fake_env'
    assert is_chroot() is True
    # True
    assert is_chroot(module=module_mock) is True
    # True
    assert is_chroot(module=module_mock_no_proc) is True
    # True
    assert is_chroot(module=module_mock_no_proc_no_root) is True
    # False
    assert is_chroot(module=module_mock_no_stat) is False
    # False
    assert is_chroot(module=module_mock_no_root) is False

# Create mock objects for unit test

# Generated at 2022-06-13 02:30:41.034674
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() is False

# Generated at 2022-06-13 02:30:41.935517
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() is False

# Generated at 2022-06-13 02:30:48.783624
# Unit test for function is_chroot
def test_is_chroot():
    root_dev = "/"

    if os.path.ismount(root_dev) and os.environ.get('debian_chroot', False):
        assert is_chroot() is True
    elif os.path.ismount(root_dev) and os.environ.get('debian_chroot', False) is False:
        assert is_chroot() is False
    else:
        assert is_chroot() is True

# Generated at 2022-06-13 02:30:50.572020
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() == False

# Generated at 2022-06-13 02:30:51.515564
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() == False

# Generated at 2022-06-13 02:31:01.159944
# Unit test for function is_chroot
def test_is_chroot():
    import mock
    import stat

    def mock_stat(path):
        class FakeStat:
            st_ino = 2
            st_dev = 0
        return FakeStat()

    fake_root_stat = mock.MagicMock(spec=stat)
    fake_root_stat.st_ino = 2
    fake_root_stat.st_dev = 0

    # with chroot
    with mock.patch.object(os, 'stat', side_effect=mock_stat):
        assert is_chroot() == True

    with mock.patch.object(os, 'stat', return_value=fake_root_stat):
        assert is_chroot() == False

# Generated at 2022-06-13 02:31:08.466736
# Unit test for function is_chroot
def test_is_chroot():
    import mock
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils import basic
    import ansible.module_utils.facts

    m_module = mock.MagicMock()
    m_module.ansible_facts = ansible_facts.AnsibleFacts(m_module)
    m_module.get_bin_path.return_value = False

    assert not is_chroot(m_module)

    m_module.return_value = True

    assert not is_chroot(m_module)

    m_module.get_bin_path.return_value = True
    m_module.run_command.return_value = (0, 'ext4', '')
    assert not is_chroot(m_module)
    m_module.run_command.return_value

# Generated at 2022-06-13 02:31:19.176443
# Unit test for function is_chroot
def test_is_chroot():
    # python module
    import ansible.module_utils.facts.system.chroot
    # python test class
    class MockModule(object):
        def __init__(self):
            self.run_command_result = None

        def get_bin_path(self, binary):
            return None

        def run_command(self, cmd):
            return self.run_command_result

    # unit tests
    module = MockModule()
    module.run_command_result = (0, 'xfs', '')
    # run the code
    is_chroot = ansible.module_utils.facts.system.chroot.is_chroot(module)
    # check the results
    assert is_chroot
    # unit tests
    module = MockModule()

# Generated at 2022-06-13 02:31:28.027182
# Unit test for function is_chroot
def test_is_chroot():
    import unittest2 as unittest
    # monkeypatch os.stat so that we can test results
    os.stat = lambda x: os.stat('/')

    class FakeModule():
        def get_bin_path(self, arg):
            return '/bin/stat'
        def run_command(self, cmd):
            return 0, 'xfs\n', ''

    class FakeModule2():
        def get_bin_path(self, arg):
            return None
        def run_command(self, cmd):
            return 0, 'xfs\n', ''

    class FakeModule3():
        def get_bin_path(self, arg):
            return '/bin/stat'
        def run_command(self, cmd):
            return 0, 'ext4\n', ''


# Generated at 2022-06-13 02:31:36.337282
# Unit test for function is_chroot
def test_is_chroot():
    test_cases = [
        {
            'environ': {},
            'expected': False
        },
        {
            'environ': {'debian_chroot': True},
            'expected': True
        },
        {
            'environ': {'debian_chroot': False},
            'expected': False
        },
        {
            'environ': {'debian_chroot': 'foo-bar'},
            'expected': True
        },
    ]
    for test_case in test_cases:
        assert is_chroot(test_case['_ansible_module']) == test_case['expected']

# Generated at 2022-06-13 02:31:43.504252
# Unit test for function is_chroot
def test_is_chroot():
    # Test 1:
    # remove debian_chroot and assume there is /proc/1/root/.
    os.environ.pop('debian_chroot', None)
    # We assume that we are not in a chroot
    assert is_chroot() == False

    # Test2:
    # Set debian_chroot. This environment variable is set to the host name if we are in a chroot (
    # see chroot(8))
    os.environ['debian_chroot'] = 'myHost'
    assert is_chroot() == True

    # Test3:
    # Unset debian_chroot and assume that /proc/1/root/. does not exist
    os.environ.pop('debian_chroot', None)
    assert is_chroot() == True

# Generated at 2022-06-13 02:31:53.969861
# Unit test for function is_chroot
def test_is_chroot():

    fake_module = {}

    class RunCommand(object):
        def __init__(self, out, rc):
            self.out = out
            self.rc = rc

        def run_command(self, cmd, check_rc=True):
            return self.rc, self.out

    fake_module.get_bin_path = lambda x: None
    fake_module.run_command = RunCommand('ext4', 0).run_command
    assert not is_chroot(fake_module)

    fake_module.get_bin_path = lambda x: None
    fake_module.run_command = RunCommand('ext4', 1).run_command
    assert not is_chroot(fake_module)

    fake_module.get_bin_path = lambda x: None

# Generated at 2022-06-13 02:31:58.107261
# Unit test for function is_chroot
def test_is_chroot():
    test_pass = True
    if is_chroot():
        test_pass = False
        print("is_chroot function test failed when it should have passed")

    os.environ['debian_chroot'] = 'foo'
    if not is_chroot():
        test_pass = False
        print("is_chroot function test failed when it should have passed")

    return test_pass

# Generated at 2022-06-13 02:31:59.196053
# Unit test for function is_chroot
def test_is_chroot():
    assert isinstance(is_chroot(), bool), "The returned value must be a boolean"

# Generated at 2022-06-13 02:31:59.849078
# Unit test for function is_chroot
def test_is_chroot():
    assert isinstance(is_chroot(), bool)

# Generated at 2022-06-13 02:32:04.097281
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() == True

# Generated at 2022-06-13 02:32:04.911156
# Unit test for function is_chroot
def test_is_chroot():
    assert(is_chroot() is True)

# Generated at 2022-06-13 02:32:06.567831
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot()

# Generated at 2022-06-13 02:32:15.174612
# Unit test for function is_chroot
def test_is_chroot():
    def test_is_chroot_helper(data):
        assert data['is_chroot'] == is_chroot(data['module'])
        assert data['is_chroot'] == (not data['is_chroot_expected'])


# Generated at 2022-06-13 02:32:17.769078
# Unit test for function is_chroot
def test_is_chroot():
    assert not is_chroot()
    assert is_chroot('/')

# Generated at 2022-06-13 02:32:19.347417
# Unit test for function is_chroot
def test_is_chroot():
    # assert is_chroot() is False
    # assert is_chroot() is False
    pass

# Generated at 2022-06-13 02:32:25.320438
# Unit test for function is_chroot
def test_is_chroot():
    def mock_os_stat(path):
        class stat_result(object):
            def __init__(self, ino, dev):
                self.st_ino = ino
                self.st_dev = dev
        return {'/': stat_result(2, 1024),
                '/proc/1/root/.': stat_result(2, 1025)}[path]

    def mock_os_environ(env_name):
        return {'debian_chroot': False}.get(env_name, None)

    old_os_stat = os.stat
    old_environ = os.environ

    os.stat = mock_os_stat
    os.environ = mock_os_environ

    assert is_chroot()
    assert not is_chroot(mock_os_environ)

    os.stat

# Generated at 2022-06-13 02:32:26.248293
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() == False

# Generated at 2022-06-13 02:32:27.093633
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() is False

# Generated at 2022-06-13 02:32:27.926036
# Unit test for function is_chroot
def test_is_chroot():
    import pytest
    assert is_chroot() == True

# Generated at 2022-06-13 02:32:40.600217
# Unit test for function is_chroot
def test_is_chroot():
    import contextlib
    import tempfile
    import shutil

    @contextlib.contextmanager
    def test_chroot(chroot_dir, proc_info=None):
        """
        Make a test root and return its path.
        proc_info is a list of two lists of "files". Each "file" is itself a list of
        lines that represent the output of a command to be piped into a file in
        /proc/<pid>/.
        """
        os.makedirs(chroot_dir)
        os.chroot(chroot_dir)

# Generated at 2022-06-13 02:32:43.472335
# Unit test for function is_chroot
def test_is_chroot():
  # non chroot
  assert not is_chroot()
  # chroot
  os.environ["debian_chroot"] = "true"
  assert is_chroot()
  # cleanup
  os.environ["debian_chroot"] = ""

# Generated at 2022-06-13 02:32:44.346158
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() is False

# Generated at 2022-06-13 02:32:45.502190
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot is not None
    assert is_chroot() is False

# Generated at 2022-06-13 02:32:53.082035
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() is False

    # Simulate chroot
    class MockModule():
        def __init__(self):
            self.run_command = lambda: None
            self.get_bin_path = lambda: None

    os.environ['debian_chroot'] = 'foo'
    assert is_chroot(MockModule())

    del os.environ['debian_chroot']
    assert is_chroot(MockModule())

# Generated at 2022-06-13 02:32:59.942057
# Unit test for function is_chroot
def test_is_chroot():

    class Module:

        class ExitJson:
            pass

        class FailJson:
            pass

        def __init__(self):
            self.run_command_called = False

        def get_bin_path(self, command):
            if command == "stat":
                return "/bin/stat"

        def run_command(self, cmd):
            self.run_command_called = True
            if cmd == ['/bin/stat', '-f', '--format=%T', '/']:
                return (0, "FileSystem Type", "")
            elif cmd == ['/bin/stat', '-f', '--format=%T', '/proc/1/root']:
                return (0, "FileSystem Type", "")

# Generated at 2022-06-13 02:33:00.430325
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() == False

# Generated at 2022-06-13 02:33:06.576472
# Unit test for function is_chroot

# Generated at 2022-06-13 02:33:13.919728
# Unit test for function is_chroot
def test_is_chroot():

    # This is a modifed version of the AnsibleModule class.
    # It is just a container to store the parameter we need.
    class AnsibleModuleMock(object):
        def __init__(self):
            self.params = dict()

        def get_bin_path(self, cmd, required=False):
            if cmd == 'stat':
                return '/usr/bin/stat'

        def run_command(self, cmd):
            if cmd == ['/usr/bin/stat', '-f', '--format=%T', '/']:
                return 0, 'btrfs', ''
            elif cmd == ['/usr/bin/stat', '-f', '--format=%T', '/opt']:
                return 0, 'xfs', ''
            else:
                return 1, '', ''

    # Test in

# Generated at 2022-06-13 02:33:15.762987
# Unit test for function is_chroot
def test_is_chroot():
    if os.path.exists('/proc'):
        assert is_chroot() == (os.geteuid() != 0)
    else:
        assert is_chroot() is None

# Generated at 2022-06-13 02:33:28.368902
# Unit test for function is_chroot
def test_is_chroot():
    if os.path.exists('/proc/1/root/.'):
        my_root = os.stat('/')
        proc_root = os.stat('/proc/1/root/.')
        is_chroot = my_root.st_ino != proc_root.st_ino or my_root.st_dev != proc_root.st_dev
    else:
        # I'm not root or no proc, fallback to checking it is inode #2
        is_chroot = (os.stat('/').st_ino != 2)

    assert is_chroot == is_chroot()

# Generated at 2022-06-13 02:33:35.961725
# Unit test for function is_chroot
def test_is_chroot():
    for root_i, root_d, root_f in os.walk('/'):
        # Because we can't rely on os.environ['debian_chroot'] we need to
        # check for some specific files to ensure we aren't running in a
        # chroot.
        if root_i.endswith('/usr'):
            break
    else:
        assert is_chroot()

    # Now lets make sure the function works when not run as the root user.
    assert not is_chroot()

if __name__ == '__main__':
    import pytest
    pytest.main(__file__)

# Generated at 2022-06-13 02:33:36.795819
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() is False

# Generated at 2022-06-13 02:33:38.802548
# Unit test for function is_chroot
def test_is_chroot():
    """Test if is_chroot is recognized correctly
    """
    import ansible.module_utils.facts.chroot as T

    assert T.is_chroot() is True

# Generated at 2022-06-13 02:33:39.683437
# Unit test for function is_chroot
def test_is_chroot():

    assert is_chroot() == False

# Generated at 2022-06-13 02:33:45.937212
# Unit test for function is_chroot
def test_is_chroot():
    # Test if we are not in a chroot environment
    module = None
    assert is_chroot(module) == False

    # Test if we are in a chroot environment
    module = True

    old_cwd = os.getcwd()
    os.makedirs('/tmp/test_is_chroot')

    # Test if we are not in a chroot environment
    os.chroot(old_cwd)
    os.chdir(old_cwd)
    assert is_chroot(module) == False

    # Test if we are in a chroot environment
    os.makedirs('/tmp/test_is_chroot')
    os.chroot('/tmp/test_is_chroot')
    os.chdir('/tmp/test_is_chroot')

# Generated at 2022-06-13 02:33:50.878411
# Unit test for function is_chroot
def test_is_chroot():

    try:
        from unittest.mock import MagicMock
    except ImportError:
        from mock import Mock as MagicMock

    is_chroot_mock = MagicMock(return_value=True)
    module = MagicMock()
    module.get_bin_path.return_value = '/usr/bin/stat'
    module.run_command.return_value = 0, '', ''
    assert is_chroot(module)

# Generated at 2022-06-13 02:33:54.514565
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() is False

# Make sure we can use the class ChrootFactCollector in unit test
test_is_chroot.collector = ChrootFactCollector

# Generated at 2022-06-13 02:33:56.101016
# Unit test for function is_chroot
def test_is_chroot():
    # If we are not in chroot, should return false
    # If we are in chroot, should return true
    pass

# Generated at 2022-06-13 02:34:02.400146
# Unit test for function is_chroot
def test_is_chroot():
    os.environ['debian_chroot'] = '1'
    assert is_chroot() == True
    del os.environ['debian_chroot']
    os.stat('/').st_ino = 2
    os.stat('/').st_dev = 3
    os.stat('/proc/1').st_ino = 4
    os.stat('/proc/1').st_dev = 5
    os.stat('/proc/1/root').st_ino = 6
    os.stat('/proc/1/root').st_dev = 7
    assert is_chroot() == False

# Generated at 2022-06-13 02:34:29.344581
# Unit test for function is_chroot
def test_is_chroot():
    root_mount = os.stat('/')
    my_root = os.stat('/')
    try:
        # check if my file system is the root one
        proc_root = os.stat('/proc/1/root/.')
        is_chroot = my_root.st_ino != proc_root.st_ino or my_root.st_dev != proc_root.st_dev
    except Exception:
        # I'm not root or no proc, fallback to checking it is inode #2
        fs_root_ino = 2

        stat_path = '/usr/bin/stat'
        cmd = [stat_path, '-f', '--format=%T', '/']
        rc, out, err = module.run_command(cmd)
        if 'btrfs' in out:
            fs_root_

# Generated at 2022-06-13 02:34:34.364680
# Unit test for function is_chroot
def test_is_chroot():
    import os
    os.type = lambda: 'Linux'
    os.path.ismount = lambda path: True
    os.stat.side_effect = lambda path: {'/': [1, 2, 3, 4, 5, 6, 7],
                                        '/proc/1/root/.': [1, 2, 3, 4, 5, 6, 8]}.get(path, [0])
    assert is_chroot() == True
    os.stat.side_effect = lambda path: {'/': [1, 2, 3, 4, 5, 6, 7],
                                        '/proc/1/root/.': [1, 2, 3, 4, 5, 6, 7]}.get(path, [0])
    assert is_chroot() == False

# Generated at 2022-06-13 02:34:38.969371
# Unit test for function is_chroot
def test_is_chroot():
    my_root = os.stat('/')
    proc_root = os.stat('/proc/1/root/.')
    is_chroot = my_root.st_ino != proc_root.st_ino or my_root.st_dev != proc_root.st_dev
    assert(is_chroot == is_chroot())

# Generated at 2022-06-13 02:34:40.336375
# Unit test for function is_chroot
def test_is_chroot():
    import ansible.module_utils.facts.system.chroot as chroot_facts

    # test on rea

# Generated at 2022-06-13 02:34:41.034877
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() is False

# Generated at 2022-06-13 02:34:46.423670
# Unit test for function is_chroot
def test_is_chroot():

    os.environ.clear()

    assert is_chroot() is False

    os.environ['debian_chroot'] = 'fakesys'
    assert is_chroot() is True

    os.environ['debian_chroot'] = 'fakesys'
    os.mkdir('/proc')
    assert is_chroot() is False

    os.environ['debian_chroot'] = 'fakesys'
    os.mkdir('/proc/1')
    os.mkdir('/proc/1/root')
    assert is_chroot() is True

    os.environ['debian_chroot'] = 'fakesys'
    os.mkdir('/proc/1')
    os.mkdir('/proc/1/root')
    os.mkdir('/fake_root')
    os.ut

# Generated at 2022-06-13 02:34:50.710774
# Unit test for function is_chroot
def test_is_chroot():

    class AnsibleModule(object):
        def __init__(self, fail_json):
            self.fail_json = fail_json

        def get_bin_path(self, exe):
            return None

        def run_command(self, args):
            return 0, "", ""

    def fail_json(msg):
        raise Exception(msg)

    module = AnsibleModule(fail_json)

    try:
        assert not is_chroot(module)
    except Exception as e:
        print("Failed to detect whether we are in chroot - exception: %s" % e)

# Generated at 2022-06-13 02:34:56.574232
# Unit test for function is_chroot
def test_is_chroot():
    real_root = os.stat('/')
    container = os.environ.get('container', 'lxc')
    os.environ['container'] = 'lxc'
    is_chroot = is_chroot()
    os.environ['container'] = container
    if is_chroot != real_root.st_ino != 2:
        raise AssertionError('is_chroot() result is incorrect.')
    del os.environ['container']

# Generated at 2022-06-13 02:34:58.531005
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() is False

# Generated at 2022-06-13 02:35:07.558679
# Unit test for function is_chroot
def test_is_chroot():

    # We need a fake module for testing
    class FakeModule(object):
        def get_bin_path(self, arg):
            return None

        def run_command(self, arg):
            return (0, None, None)

    # Test a basic chroot
    assert is_chroot(FakeModule()) is True

    # Test an environment variable that indicates a chroot
    os.environ['debian_chroot'] = True
    assert is_chroot(FakeModule()) is True

    # Test a fake module that returns a stat executable
    class FakeModule2(object):
        def get_bin_path(self, arg):
            return '/bin/stat'

        def run_command(self, arg):
            return (0, 'xfs', None)

    assert is_chroot(FakeModule2()) is True

    # Test a

# Generated at 2022-06-13 02:35:44.501490
# Unit test for function is_chroot
def test_is_chroot():
    facts = ChrootFactCollector().collect()
    assert facts == {'is_chroot': is_chroot()}

# Generated at 2022-06-13 02:35:47.122789
# Unit test for function is_chroot
def test_is_chroot():
    from ansible.module_utils.facts.collector import collect_file_facts
    facts = collect_file_facts(None)
    assert 'is_chroot' in facts

# Generated at 2022-06-13 02:35:47.878167
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot()

# Generated at 2022-06-13 02:35:48.618793
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() is False

# Generated at 2022-06-13 02:35:53.535025
# Unit test for function is_chroot
def test_is_chroot():
    if os.path.exists('/proc/1/root/.'):
        my_root = os.stat('/')
        if my_root.st_ino == os.stat('/proc/1/root/.').st_ino:
            return
        elif my_root.st_dev == os.stat('/proc/1/root/.').st_dev:
            return
    return True

# Generated at 2022-06-13 02:35:55.206572
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() is False

# Generated at 2022-06-13 02:35:55.991420
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() is True

# Generated at 2022-06-13 02:36:01.454727
# Unit test for function is_chroot
def test_is_chroot():
    # Pre-conditions
    assert 'debian_chroot' not in os.environ
    assert 'is_chroot' not in list(collector['chroot'].collect().keys())

    # Run unit tests
    os.environ['debian_chroot'] = 'Test'
    assert collector['chroot'].collect()['is_chroot'] == True

    del os.environ['debian_chroot']
    assert is_chroot() == False
    assert is_chroot() == True

    # Post-conditions
    assert 'debian_chroot' not in os.environ
    assert 'is_chroot' not in list(collector['chroot'].collect().keys())

# Generated at 2022-06-13 02:36:10.530717
# Unit test for function is_chroot
def test_is_chroot():
    import mock

    assert is_chroot(module=None) == False

    with mock.patch.dict(os.environ, {'debian_chroot': 'foo'}):
        assert is_chroot(module=None) == True

    with mock.patch.object(os, 'stat', lambda x: mock.MagicMock(st_ino=1, st_dev=1)):
        with mock.patch.object(os, 'stat', lambda x: mock.MagicMock(st_ino=2, st_dev=2)):
            assert is_chroot(module=None) == False

    # mock a procfs root

# Generated at 2022-06-13 02:36:11.040418
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() == False

# Generated at 2022-06-13 02:37:29.275789
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() == False

# Generated at 2022-06-13 02:37:29.992547
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot()

# Generated at 2022-06-13 02:37:32.725530
# Unit test for function is_chroot
def test_is_chroot():
    # normal call, no module
    test_is_chroot = is_chroot()

    # check we get a boolean
    assert isinstance(test_is_chroot, bool)

    # check the value is False
    assert test_is_chroot is False

# Generated at 2022-06-13 02:37:33.639927
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() is False

# Generated at 2022-06-13 02:37:34.419399
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() is False

# Generated at 2022-06-13 02:37:36.746699
# Unit test for function is_chroot
def test_is_chroot():
    """is_chroot is used by the ChrootFactCollector but can also be called directly."""
    assert is_chroot()

# Generated at 2022-06-13 02:37:37.479865
# Unit test for function is_chroot
def test_is_chroot():
    assert isinstance(is_chroot(), bool)

# Generated at 2022-06-13 02:37:39.015111
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() is None

# Generated at 2022-06-13 02:37:40.121007
# Unit test for function is_chroot
def test_is_chroot():
    is_chroot = is_chroot()
    assert is_chroot == False

# Generated at 2022-06-13 02:37:48.182259
# Unit test for function is_chroot
def test_is_chroot():
    # Make sure we always run this with an unmodified environment
    module = None
    from ansible.module_utils import basic

    module = basic.AnsibleModule(
        argument_spec=dict(),
    )

    if not is_chroot(module):
        raise Exception("is_chroot should returns True when run in chroot")

    # Check that somes exception are caught