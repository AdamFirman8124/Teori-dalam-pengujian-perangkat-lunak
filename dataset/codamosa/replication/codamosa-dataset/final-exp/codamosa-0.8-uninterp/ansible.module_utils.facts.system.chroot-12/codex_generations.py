

# Generated at 2022-06-13 02:30:16.119989
# Unit test for function is_chroot
def test_is_chroot():
    assert not is_chroot()

# Generated at 2022-06-13 02:30:25.198804
# Unit test for function is_chroot
def test_is_chroot():
    # mocking results for os.stat('/')
    class MockStat:
        def __init__(self, ino, dev):
            self.st_ino = ino
            self.st_dev = dev
    # mocking results for os.stat('/proc/1/root/.')
    class MockProcRoot:
        def __init__(self, ino, dev):
            self.st_ino = ino
            self.st_dev = dev

    # test case 1
    # os.environ['debian_chroot'] is True
    os.environ['debian_chroot'] = 'testing'
    assert is_chroot()

    # test case 2
    # os.stat('/') returns st_ino == 2 and st_dev == 0
    # and os.stat('/proc/1/root/.')

# Generated at 2022-06-13 02:30:31.552640
# Unit test for function is_chroot
def test_is_chroot():
    module = type('', (), {'get_bin_path': lambda x: '/usr/bin/stat'})()
    module.run_command = lambda x: (0, 'ext4\n', None)
    assert is_chroot(module) == False

    module.run_command = lambda x: (0, 'btrfs\n', None)
    assert is_chroot(module) == False

    module.run_command = lambda x: (0, 'xfs\n', None)
    assert is_chroot(module) == False

# Generated at 2022-06-13 02:30:32.740560
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot(None) is False, 'is_chroot should have returned False'

# Generated at 2022-06-13 02:30:33.592580
# Unit test for function is_chroot
def test_is_chroot():
    assert not is_chroot()

# Generated at 2022-06-13 02:30:40.598930
# Unit test for function is_chroot
def test_is_chroot():
    # mock os stat
    old_stat = os.stat
    old_environ = os.environ

    def mock_stat(fname):
        fs = os.stat_result((33188, 2, 1000, 0, 1000, 0, 4096, 1510728303, 1510728303, 1510728303))
        if fname == '.' or fname == '/':
            return fs
        elif fname == '/proc/1/root/.':
            fs.st_ino = 1
            return fs
        else:
            assert False, 'unsupported stat call to %s' % fname

    def mock_environ_set(key, value):
        assert key == 'debian_chroot'
        os.environ['debian_chroot'] = value

    def mock_environ_unset(key):
        assert key

# Generated at 2022-06-13 02:30:43.121708
# Unit test for function is_chroot
def test_is_chroot():
    cwd = os.getcwd()
    os.chdir('/')
    assert is_chroot() == False
    os.chdir(cwd)


# Generated at 2022-06-13 02:30:52.438804
# Unit test for function is_chroot
def test_is_chroot():
    if os.path.exists('/tmp/ansible_fact_collector'):
        os.chdir('/tmp/ansible_fact_collector')
    if not os.path.exists('/tmp/ansible_fact_collector'):
        os.makedirs('/tmp/ansible_fact_collector')
    if not os.path.exists('/tmp/ansible_fact_collector/proc'):
        os.makedirs('/tmp/ansible_fact_collector/proc')
    if not os.path.exists('/tmp/ansible_fact_collector/proc/1'):
        os.makedirs('/tmp/ansible_fact_collector/proc/1')

# Generated at 2022-06-13 02:30:53.362440
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() == False

# Generated at 2022-06-13 02:30:55.316538
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() == False
    assert is_chroot() == True

# Generated at 2022-06-13 02:31:03.406443
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() is False

# Generated at 2022-06-13 02:31:07.824577
# Unit test for function is_chroot
def test_is_chroot():
    # hardcode value because it can not be changed on the fly
    os.environ['debian_chroot'] = False

    # check that hardcoded value is OK
    assert is_chroot() == False

    # check that it can be turned on
    os.environ['debian_chroot'] = True
    assert is_chroot() == True

    # check that it is turned off by default
    del os.environ['debian_chroot']
    assert is_chroot() == False

# Generated at 2022-06-13 02:31:08.780481
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() == False

# Generated at 2022-06-13 02:31:19.509848
# Unit test for function is_chroot
def test_is_chroot():
    class TestModule(object):

        def __init__(self, params):
            self._params = params
            self._bin_path = params.get('bin_path', None)

        def get_bin_path(self, bin_name):
            return self._bin_path

        # pylint: disable=no-self-use
        def run_command(self, cmd):
            return 0, cmd[4], None

    # test normal case
    module = TestModule(params={})
    assert is_chroot(module=module) is False

    # test with environment set
    os.environ['debian_chroot'] = 'I am chroot'
    assert is_chroot(module=module) is True

    # test chroot via /proc/self/root
    del os.environ['debian_chroot']
   

# Generated at 2022-06-13 02:31:28.025170
# Unit test for function is_chroot
def test_is_chroot():
    """
    Verify that ansible_is_chroot is being set correctly
    """
    # This test cannot be run inside a container, and is difficult to run
    # in any virtual system, since the behavior under test depends on the
    # file system
    if os.path.exists('/.dockerenv'):
        return

    import unittest
    import ansible.module_utils.facts.chroot as chroot_facts

    class TestChrootFact(unittest.TestCase):

        @unittest.skipUnless(is_chroot(), 'Test requires running outside of a container and not in a chroot')
        def test_is_chroot(self):
            self.assertTrue(chroot_facts.is_chroot())

    unittest.main()

# Generated at 2022-06-13 02:31:30.814529
# Unit test for function is_chroot
def test_is_chroot():
    try:
        os.stat('/proc/1/root/.')
        in_proc = True
    except Exception:
        in_proc = False

    assert is_chroot() == in_proc

# Generated at 2022-06-13 02:31:40.399457
# Unit test for function is_chroot
def test_is_chroot():
    import mock
    import os

    # regular env
    with mock.patch('os.stat') as mock_stat:
        mock_stat.return_value.st_ino = 2
        mock_stat.return_value.st_dev = 22
        assert is_chroot() is False

    # chroot environment
    with mock.patch('os.stat') as mock_stat:
        mock_stat.return_value.st_ino = 1
        mock_stat.return_value.st_dev = 22
        assert is_chroot() is True

    # chroot environment without proc
    with mock.patch('os.stat'), mock.patch('os.environ'):
        del os.environ['debian_chroot']
        os.stat.return_value.st_ino = 1
        os.stat.s

# Generated at 2022-06-13 02:31:48.214620
# Unit test for function is_chroot
def test_is_chroot():
    import stat
    import tempfile
    import shutil

    # Test 1: test when not in a chroot
    assert not is_chroot()

    # Test 2: Test when in a chroot
    d = tempfile.mkdtemp()

# Generated at 2022-06-13 02:31:52.003637
# Unit test for function is_chroot
def test_is_chroot():
    class LocalModule():
        def get_bin_path(self, module):
            return None

        def run_command(self, module):
            return None
    assert is_chroot(LocalModule()) is False

# Generated at 2022-06-13 02:32:00.120042
# Unit test for function is_chroot
def test_is_chroot():

    # Always allow test_is_chroot be run
    class Module(object):
        def get_bin_path(self, *args, **kw):
            return '/usr/bin/stat'

        def run_command(self, cmd):
            if 'btrfs' in cmd:
                return (0, 'Filesystem', '')
            elif 'xfs' in cmd:
                return (0, 'meta-data=/dev/sda1 isize=512 agcount=4, agsize=655360 blks', '')
            else:
                return (0, '0x102', '')
    module = Module()

    # Chroot

# Generated at 2022-06-13 02:32:15.018011
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot(None) == False

# Generated at 2022-06-13 02:32:17.986895
# Unit test for function is_chroot
def test_is_chroot():
    import os
    assert is_chroot() == (os.stat('/').st_ino == 2)

# Generated at 2022-06-13 02:32:19.537495
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() == False
    assert is_chroot(module=True) == True

# Generated at 2022-06-13 02:32:25.410971
# Unit test for function is_chroot
def test_is_chroot():
    import sys
    # the simplest check, we can't be in a chroot from a test ;-)
    assert not is_chroot()
    # when we run a test in a chroot it will have a debian_chroot set
    os.environ['debian_chroot'] = 'testingansible'
    assert is_chroot()
    del os.environ['debian_chroot']

    try:
        import kmod
    except:
        return # no module to run is_chroot() with

    # in a chroot, this will only work if the test runner is run as root,
    # so we ignore the failure and dlopen error
    try:
        assert is_chroot(kmod)
    except BaseException as e:
        assert e.__class__.__name__ == 'dlopen_error' or e.__

# Generated at 2022-06-13 02:32:26.329032
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() is False

# Generated at 2022-06-13 02:32:36.220281
# Unit test for function is_chroot
def test_is_chroot():
    def fake_module(root_is_chroot, name='ansible.module_utils.facts.chroot.is_chroot'):
        class FakeModule(object):
            def __init__(self):
                self.root_is_chroot = root_is_chroot
                self.stat_path = None

            def get_bin_path(self, name, required=True):
                return self.stat_path

            def run_command(self, cmd):
                if self.stat_path is None or name != 'stat':
                    return 1, None, None

                rc = 0
                out = 'unknown'
                err = ''

                if self.root_is_chroot:
                    out = 'xfs'
                else:
                    out = 'ext4'

                return rc, out, err

        return FakeModule()

# Generated at 2022-06-13 02:32:37.083132
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot(None) == False


# Generated at 2022-06-13 02:32:46.771839
# Unit test for function is_chroot
def test_is_chroot():

    # Dummy module for testing is_chroot
    class Module():
        def get_bin_path(self, name, preferred=False, opt_dirs=None):
            path = None
            if name == 'stat':
                path = '/usr/bin/stat'
            return path

        def run_command(self, cmd, check_rc=True, data=None, binary_data=False, path_prefix=None, cwd=None,
                        use_unsafe_shell=False, prompt_regex=None, environ_update=None, umask=None,
                        encoding=None, errors='surrogate_or_strict', expand_user_and_vars=True):
            return 0, '', ''

    my_module = Module()
    my_chroot = is_chroot(my_module)

# Generated at 2022-06-13 02:32:54.055854
# Unit test for function is_chroot
def test_is_chroot():
    import ansible.module_utils.facts.system.chroot
    # make sure we aren't in a chroot
    if os.environ.get('debian_chroot', False) or is_chroot():
        raise Exception("This test needs to run from the real root directory")

    assert ansible.module_utils.facts.system.chroot.is_chroot() == False

# Generated at 2022-06-13 02:32:55.149199
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() is False

# Generated at 2022-06-13 02:33:09.891147
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chro

# Generated at 2022-06-13 02:33:13.273873
# Unit test for function is_chroot
def test_is_chroot():
    try:
        from ansible.module_utils.facts.collector import BaseFactCollector
        is_chroot = BaseFactCollector.get_collector_class('chroot').is_chroot
    except Exception:
        is_chroot = __import__('ansible.module_utils.facts.chroot').is_chroot

    assert is_chroot() == False

# Generated at 2022-06-13 02:33:15.117941
# Unit test for function is_chroot
def test_is_chroot():
    # pylint: disable=protected-access
    try:
        os.chdir('/')
    except Exception:
        pass
    assert not ChrootFactCollector().collect()

# Generated at 2022-06-13 02:33:15.671762
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() == False

# Generated at 2022-06-13 02:33:19.152944
# Unit test for function is_chroot
def test_is_chroot():
    from ansible.module_utils.facts.collector import BaseFactCollector
    import os
    import shutil

    tmp_dir = '/tmp/ansible_test_is_chroot'
    if os.path.exists(tmp_dir):
        shutil.rmtree(tmp_dir)
    os.mkdir(tmp_dir)

    os.chdir(tmp_dir)
    os.mkdir('proc')
    os.symlink('/proc', 'proc/1')

    # This should be True but can't create /proc in a way that works on Linux & Mac
    assert is_chroot()

# Generated at 2022-06-13 02:33:20.200180
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() is False

# Generated at 2022-06-13 02:33:21.209434
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot()

# Generated at 2022-06-13 02:33:30.682824
# Unit test for function is_chroot
def test_is_chroot():
    the_root = os.stat('/')
    assert not is_chroot()

    def t_run_command(module, cmd, check_rc=True, environ_update=None,
                      data=None, binary_data=False, path_prefix=None, cwd=None,
                      use_unsafe_shell=False):

        assert cmd[0] == 'stat'
        if my_root.st_ino == proc_root.st_ino and my_root.st_dev == proc_root.st_dev:
            cmd[-1] = os.path.basename(cmd[-1])

        if cmd[-1] == '/':
            if 'btrfs' in cmd:
                return 0, 'Btrfs', ''
            elif 'xfs' in cmd:
                return 0, 'Xfs',

# Generated at 2022-06-13 02:33:39.720801
# Unit test for function is_chroot
def test_is_chroot():
    is_chroot = __import__('ansible_collections.ansible.system_basics.plugins.module_utils.facts.system.chroot', globals(), locals(), ['is_chroot'], 0).is_chroot

    class FakeModule:
        def get_bin_path(self, path):
            return None

        def run_command(self, cmd):
            raise Exception("run_command should not be called")

    # Test if a normal environment is not chroot
    assert is_chroot() is False

    # Test if is_chroot recognizes a chroot environment
    os.environ['debian_chroot'] = 'test_chroot'
    assert is_chroot() is True
    del os.environ['debian_chroot']

    # Test that if /proc/ is available it is used to get information
   

# Generated at 2022-06-13 02:33:45.987310
# Unit test for function is_chroot
def test_is_chroot():

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes

    # Mock module object
    module_mock = AnsibleModule(argument_spec={})
    module_mock.run_command = AnsibleModule.run_command
    module_mock.get_bin_path = AnsibleModule.get_bin_path
    module_mock.run_command.return_value = 0, to_bytes(''), to_bytes('')

    # Mock module as root
    module_mock.params['HOME'] = '/root'
    module_mock.params['USER'] = 'root'
    module_mock.params['LOGNAME'] = 'root'
    module_mock.params['SUDO_COMMAND'] = '/bin/mount'
    module

# Generated at 2022-06-13 02:34:19.131636
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() is False
    os.environ['debian_chroot'] = 'something'
    assert is_chroot() is True

# Generated at 2022-06-13 02:34:20.015825
# Unit test for function is_chroot
def test_is_chroot():
    assert not is_chroot()

# Generated at 2022-06-13 02:34:30.551846
# Unit test for function is_chroot
def test_is_chroot():
    from ansible.module_utils.facts.collector import FactsCollector
    from ansible.module_utils._text import to_bytes

    # enumerate possible chroot scenarios
    scenarios = (
        # scenario             chroot result
        ('standard',           False),
        ('my_root_is_chroot',  True),
        ('my_root_is_fakeroot', False),
        ('my_root_is_fakeroot_no_proc', True),
        ('my_root_is_fakeroot_bad_fs', True),
    )

    # create a facts collector
    fc = FactsCollector()

    # add ChrootFactCollector to facts collector
    fc.add_collector(ChrootFactCollector())

    # iterate over scenarios

# Generated at 2022-06-13 02:34:31.636100
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() is False

# Generated at 2022-06-13 02:34:35.422750
# Unit test for function is_chroot
def test_is_chroot():
    import distutils.spawn as spawn

    _ = None  # Ignore warning about _

    # Is chroot not working?
    if not spawn.find_executable('stat'):
        return

    # Test in the jenkins environment
    assert is_chroot()

# Generated at 2022-06-13 02:34:42.061782
# Unit test for function is_chroot
def test_is_chroot():

    import tempfile

    # Create a new chroot environment
    old_cwd = os.getcwd()

    chroot_dir = tempfile.mkdtemp()
    os.chroot(chroot_dir)
    os.chdir('/')
    assert(is_chroot())

    # Delete chroot
    os.chroot('.')
    os.chdir('/')
    assert(not is_chroot())

    # Test without a module
    os.chdir(old_cwd)
    assert(not is_chroot())

    os.rmdir(chroot_dir)

# Generated at 2022-06-13 02:34:42.690197
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() is None

# Generated at 2022-06-13 02:34:43.313381
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() == False

# Generated at 2022-06-13 02:34:44.401668
# Unit test for function is_chroot
def test_is_chroot():

    # Just call is_chroot function as unit test
    is_chroot()

# Generated at 2022-06-13 02:34:46.596884
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() is False
    os.environ['debian_chroot'] = 'something'
    assert is_chroot() is True
    del os.environ['debian_chroot']

# Generated at 2022-06-13 02:36:01.521416
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() == False

# Generated at 2022-06-13 02:36:03.164442
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() is False

# Generated at 2022-06-13 02:36:11.189112
# Unit test for function is_chroot
def test_is_chroot():
    # Create tmp mount point
    import tempfile
    import shutil
    import stat

    tmp_mount = tempfile.mkdtemp()
    tmp_mount_stat = os.stat(tmp_mount)
    # Check if it is a chroot
    assert is_chroot() == False

    # Create tmp mount point and fake its stat
    tmp_mount2 = tempfile.mkdtemp()
    os.chmod(tmp_mount2, 0o555)

    # Create a file in the tmp mount point
    tmp_file = tempfile.mkstemp(dir=tmp_mount2, prefix='fake_chroot')

    # Get the stat of the file
    tmp_file_stat = os.stat(tmp_file[1])

# Generated at 2022-06-13 02:36:11.729801
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot()

# Generated at 2022-06-13 02:36:15.221022
# Unit test for function is_chroot
def test_is_chroot():
    import ansible.module_utils.facts.collector
    import system_info.chroot

    module = ansible.module_utils.facts.collector
    ansible.module_utils.facts.collector.sys = system_info.chroot
    ansible.module_utils.facts.collector.os = system_info.chroot

    is_chroot = module.ChrootFactCollector().collect().get('is_chroot')

    assert isinstance(is_chroot, bool)

# Generated at 2022-06-13 02:36:16.100757
# Unit test for function is_chroot
def test_is_chroot():
    assert isinstance(is_chroot(), bool)

# Generated at 2022-06-13 02:36:18.598957
# Unit test for function is_chroot
def test_is_chroot():
    try:
        # run this test in a chroot
        os.stat('/')
        assert False
    except OSError:
        # we should be in a chroot if we get to this point
        assert is_chroot()



# Generated at 2022-06-13 02:36:21.792344
# Unit test for function is_chroot
def test_is_chroot():
    with open('/chroot.test', 'w') as f:
        f.write('test')
    os.chmod('/chroot.test', 0o755)
    assert is_chroot() == False
    os.chroot('/chroot.test')
    assert is_chroot() == True
    os.rmdir('/chroot.test')

# Generated at 2022-06-13 02:36:23.636913
# Unit test for function is_chroot
def test_is_chroot():
    if os.environ.get('debian_chroot', False):
        assert is_chroot() is True
    else:
        assert is_chroot() is False

# Generated at 2022-06-13 02:36:24.398785
# Unit test for function is_chroot
def test_is_chroot():

    assert not is_chroot()

# Generated at 2022-06-13 02:39:20.486802
# Unit test for function is_chroot
def test_is_chroot():
    # my_root.st_ino != proc_root.st_ino ||  my_root.st_dev != proc_root.st_dev
    # is_chroot = False
    my_root = os.stat('/')
    proc_root = os.stat('/proc/1/root/.')
    assert my_root.st_ino == proc_root.st_ino and my_root.st_dev == proc_root.st_dev
    assert not is_chroot()

    # my_root.st_ino != fs_root_ino
    # is_chroot = True
    my_root = os.stat('/')
    assert my_root.st_ino != 2
    assert is_chroot()

# Generated at 2022-06-13 02:39:25.977285
# Unit test for function is_chroot
def test_is_chroot():
    from ansible.module_utils.facts.collector import FactsCollector
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    # Test with module
    facts = FactsCollector().get_facts(module=object())
    if 'debian' in facts['distribution']:
        # See https://github.com/ansible/ansible/issues/61865
        assert is_chroot()
    else:
        assert is_chroot(module=object())
    # Test without module
    assert is_chroot()

# Generated at 2022-06-13 02:39:30.977328
# Unit test for function is_chroot
def test_is_chroot():
    # Build a mock module
    class AnsibleModule:
        def get_bin_path(self, tool):
            return None

        def run_command(self, arg):
            return (0, b"ext4", b"")

    module_obj = AnsibleModule()
    result = is_chroot(module_obj)
    assert result == False

# Generated at 2022-06-13 02:39:39.056243
# Unit test for function is_chroot
def test_is_chroot():
    import sys

    real_symlink = os.path.islink

    def islink_mock(path):
        if path == '/proc/1/root/.':
            return False
        return real_symlink(path)

    os.path.islink = islink_mock

    class FakeModule(object):
        def __init__(self, run_command=None, get_bin_path=None):
            self.run_command = run_command
            self.get_bin_path = get_bin_path

        def run_command(self, command):
            return 0, '', ''
        def get_bin_path(self):
            return None

    import stat

    # create a temp file
    fh, path = tempfile.mkstemp()
    # get the inode number and device number of

# Generated at 2022-06-13 02:39:40.129110
# Unit test for function is_chroot
def test_is_chroot():
    assert(is_chroot() is False)

# Generated at 2022-06-13 02:39:43.621962
# Unit test for function is_chroot
def test_is_chroot():
    test_cases = ((0, False),
                  (1, False),
                  (2, False),
                  (3, True),
                  (4, True),
                  )
    for case in test_cases:
        os.environ['debian_chroot'] = ''
        os.stat = lambda path: lambda field: case[0]
        assert(is_chroot() == case[1])
        os.environ['debian_chroot'] = 'test'
        assert(is_chroot() == True)
    del os.environ['debian_chroot']

# Generated at 2022-06-13 02:39:45.418823
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() is False

# Generated at 2022-06-13 02:39:46.213576
# Unit test for function is_chroot
def test_is_chroot():
    assert not is_chroot()

# Generated at 2022-06-13 02:39:50.954772
# Unit test for function is_chroot
def test_is_chroot():
    import os.path
    import sys
    import doctest
    #import ansible.module_utils.facts.chroot as chroot

    test = os.path.abspath(__file__)
    test = sys.modules[__name__]
    failures = doctest.testmod(m=test, raise_on_error=True, optionflags=doctest.REPORT_ONLY_FIRST_FAILURE)
    sys.exit(failures)

# Generated at 2022-06-13 02:39:51.682663
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() == True