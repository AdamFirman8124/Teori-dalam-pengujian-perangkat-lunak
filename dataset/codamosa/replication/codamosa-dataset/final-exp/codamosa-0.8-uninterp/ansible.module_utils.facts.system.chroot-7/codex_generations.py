

# Generated at 2022-06-13 02:30:20.088774
# Unit test for function is_chroot
def test_is_chroot():
    is_chroot_real = is_chroot()
    assert is_chroot_real is False

# Generated at 2022-06-13 02:30:25.355216
# Unit test for function is_chroot
def test_is_chroot():
    is_chroot = __import__('ansible.module_utils.facts.chroot.is_chroot')

    # test chroot
    os.environ['debian_chroot'] = 'chroot'
    assert is_chroot.is_chroot()

    del os.environ['debian_chroot']
    # test not chroot
    assert not is_chroot.is_chroot()

# Generated at 2022-06-13 02:30:26.289867
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() is False

# Generated at 2022-06-13 02:30:27.596136
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() is True

# Generated at 2022-06-13 02:30:30.451324
# Unit test for function is_chroot
def test_is_chroot():

    class Module:

        def get_bin_path(self, bin_name):
            return bin_name

        def run_command(self, cmd):
            return 0, '', ''

    module = Module()

    assert is_chroot(module) is False

# Generated at 2022-06-13 02:30:33.468167
# Unit test for function is_chroot
def test_is_chroot():

    class test_module:
        def get_bin_path(self, what):
            return None

        def run_command(self, cmd):
            return None, None, None

    test_m = test_module()
    assert is_chroot(test_m) == False

# Generated at 2022-06-13 02:30:34.910700
# Unit test for function is_chroot
def test_is_chroot():
    # is_chroot should always return either True or False
    assert is_chroot() is not None

# Generated at 2022-06-13 02:30:35.677152
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() == False

# Generated at 2022-06-13 02:30:46.627874
# Unit test for function is_chroot
def test_is_chroot():
    # . . . . . . . . . . . . . .
    # Some functions of the BaseFactCollector are tested like this:
    #
    #     bc = BaseFactCollector()
    #
    #     # test name
    #     assert bc.name == ''
    #
    #     # test get_fact_id
    #     assert bc.get_fact_id('id') == 'id'
    #
    #     # test filter_facts
    #     assert bc.filter_facts(['id']) == set(['id'])

    # . . . . . . . . . . . . . .
    cfc = ChrootFactCollector()

    # test get_fact_id
    assert cfc.get_fact_id('is_chroot') == 'is_chroot'

    # . .

# Generated at 2022-06-13 02:30:47.696377
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() == False

# Generated at 2022-06-13 02:30:55.993568
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() is None

# Generated at 2022-06-13 02:31:04.205263
# Unit test for function is_chroot
def test_is_chroot():
    def fake_stat(path):
        stat_t = {
            '/proc/1/root/.': {'st_ino': 1, 'st_dev': 1},
            '/': {'st_ino': 2, 'st_dev': 1},
        }
        return stat_t.get(path, {})

    os_stat_orig = os.stat
    os.stat = fake_stat

    try:
        assert is_chroot()
        os.environ['debian_chroot'] = 'foo'
        assert is_chroot()
        os.environ['debian_chroot'] = False
        assert is_chroot()
    finally:
        os.environ.pop('debian_chroot', None)
        os.stat = os_stat_orig

# Generated at 2022-06-13 02:31:06.444252
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() == False
    assert is_chroot() == False

# Generated at 2022-06-13 02:31:08.883537
# Unit test for function is_chroot
def test_is_chroot():
    # Should return one of the two following dicts when run in a chroot
    success_results = [
        {'is_chroot': True},
        {'is_chroot': False}
    ]

    assert is_chroot() in success_results, "is_chroot() did not return True or False"

# Generated at 2022-06-13 02:31:10.641670
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot()

# Generated at 2022-06-13 02:31:14.715588
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() == False
    if os.path.exists('/bin/false'):
        assert is_chroot(module=None) == is_chroot(module=os)
    else:
        assert is_chroot(module=None) == is_chroot(module=os)

# Generated at 2022-06-13 02:31:24.485794
# Unit test for function is_chroot
def test_is_chroot():
    import ansible.module_utils.facts.system.chroot
    from ansible.module_utils.facts.system.chroot import is_chroot
    import pytest
    import os

    fake_chroot = os.path.sep + os.path.join('fake', 'chroot')

    # test that inside chroot, it is recognized as such
    with open(os.path.sep + os.path.join('fake', 'chroot', 'etc', 'debian_chroot'), 'w') as f:
        f.write('fake_chroot')
        f.close()

    os.mkdir(os.path.sep + os.path.join('fake', 'chroot', 'proc'))


# Generated at 2022-06-13 02:31:26.596687
# Unit test for function is_chroot
def test_is_chroot():

    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict(),
    )

    assert is_chroot(module)

# Generated at 2022-06-13 02:31:33.196958
# Unit test for function is_chroot

# Generated at 2022-06-13 02:31:37.484289
# Unit test for function is_chroot
def test_is_chroot():

    try:
        # Test non-chroot
        os.unsetenv('debian_chroot')
        assert is_chroot() is False
    except Exception:
        pass

    try:
        # Test chroot
        os.environ['debian_chroot'] = 'test'
        assert is_chroot() is True
    except Exception:
        pass

# Generated at 2022-06-13 02:31:54.589687
# Unit test for function is_chroot
def test_is_chroot():
    from ansible.module_utils.basic import AnsibleModule
    assert is_chroot() == is_chroot(module=AnsibleModule(argument_spec={}))

# Generated at 2022-06-13 02:32:01.499459
# Unit test for function is_chroot
def test_is_chroot():

    # check with no module
    assert is_chroot() is None

    # check good case
    m = MockModule()
    assert is_chroot(module=m) is False

    # check good case with proc
    m = MockModule(fs='ext4')
    assert is_chroot(module=m) is True

    # check good case with proc
    m = MockModule(fs='ext4', root_test=True)
    assert is_chroot(module=m) is False

    # check good case with proc
    m = MockModule(fs='ext4', root_test=True, root_stat_test=True)
    assert is_chroot(module=m) is False


# Generated at 2022-06-13 02:32:09.508925
# Unit test for function is_chroot
def test_is_chroot():
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.system.chroot
    import ansible.module_utils.facts.system.platform
    import ansible.module_utils.facts.system.distribution

    class DummyModule:
        def __init__(self):
            self.run_command_environ_update = {}
            self.run_command_common_paths = []

        def run_command(self, args, check_rc=True):
            return (0, '', '')

    dummy_module = DummyModule()

    class DummyFacts:
        def __init__(self):
            self.data = {}

        # noinspection PyUnusedLocal

# Generated at 2022-06-13 02:32:20.978327
# Unit test for function is_chroot
def test_is_chroot():
    import os
    from ansible.module_utils import basic

    from ansible.module_utils.facts.collector.chroot import is_chroot

    # This test is not using nosetests because it must be run from a chroot
    # environment directly into the source code tree.
    if os.path.basename(os.getcwd()) != 'ansible':
        print('ERROR: This test must be run from the ansible root directory.')
        print('For exemple:')
        print('ansible$ sudo chroot .')
        print('/# python -m lib.ansible.module_utils.facts.collector.chroot')
        return

    # Ensure that the function return false when not in a chroot environment
    print('Using function is_chroot')
    print('is_chroot:', is_chroot())

# Generated at 2022-06-13 02:32:23.618721
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot()

# Generated at 2022-06-13 02:32:27.335101
# Unit test for function is_chroot
def test_is_chroot():

    # Test can not be run from within a chroot, so just skip it if that's the case
    if is_chroot():
        return

    # Test with /proc
    assert is_chroot() is False

    # Test without /proc
    assert is_chroot(None) is False

# Generated at 2022-06-13 02:32:28.307486
# Unit test for function is_chroot
def test_is_chroot():
    assert isinstance(is_chroot(), bool)

# Generated at 2022-06-13 02:32:31.462263
# Unit test for function is_chroot
def test_is_chroot():
    # We are not in a chroot, let's check
    if is_chroot():
        raise Exception
    # We are in a chroot, let's check
    os.environ['debian_chroot'] = 'test'
    if not is_chroot():
        raise Exception

# Generated at 2022-06-13 02:32:32.044193
# Unit test for function is_chroot
def test_is_chroot():
    module = None
    assert is_chroot(module) == False

# Generated at 2022-06-13 02:32:33.949830
# Unit test for function is_chroot
def test_is_chroot():
    assert(is_chroot() is False)

# Generated at 2022-06-13 02:32:51.410776
# Unit test for function is_chroot
def test_is_chroot():
    try:
        assert is_chroot()
    except AssertionError:
        assert not is_chroot()

# Generated at 2022-06-13 02:32:55.317181
# Unit test for function is_chroot
def test_is_chroot():
    # Set UID to 0 and try to get the chroot.
    os.seteuid(0)
    assert is_chroot(is_chroot) is True
    os.seteuid(1000)

# Generated at 2022-06-13 02:32:59.096288
# Unit test for function is_chroot
def test_is_chroot():
    for test_data in (('/', False),
                      ('/proc', False),
                      ('/sys/fs/cgroup', True)):
        assert is_chroot(test_data[0]) == test_data[1]


# vim: set et ts=4 sw=4 :

# Generated at 2022-06-13 02:33:09.512585
# Unit test for function is_chroot
def test_is_chroot():

    class ModuleStub(object):
        def __init__(self, rc, out, err):
            self.rc = rc
            self.stdout = out
            self.stderr = err

        def run_command(self, args, check_rc=True):
            return self.rc, self.stdout, self.stderr

    class RcModule(object):
        def __init__(self, rc):
            self.rc = rc

        def get_bin_path(self, exe, required=True):
            if exe == 'stat':
                return '/usr/bin/stat'
            else:
                return None

        def run_command(self, args, check_rc=True):
            return self.rc, None, None

    # Test chroot environment

# Generated at 2022-06-13 02:33:10.300831
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() == False

# Generated at 2022-06-13 02:33:16.277883
# Unit test for function is_chroot
def test_is_chroot():

    class Module(object):

        def get_bin_path(self, prog):
            return '/usr/bin/%s' % prog

        def run_command(self, cmd):
            if cmd[0] == '/usr/bin/stat' and cmd[3] == '/':
                if cmd[1] == '-f' and cmd[2] == '--format=%T':
                    if os.path.isdir('/proc/1/root/mnt'):
                        return (0, 'btrfs', None)
                    else:
                        return (0, 'xfs', None)
                else:
                    os.statvfs('/')
                    return (0, '0', None)

        def fail_json(self, **kwargs):
            return None

    test_module = Module()

# Generated at 2022-06-13 02:33:16.909992
# Unit test for function is_chroot
def test_is_chroot():

    assert isinstance(is_chroot(), bool)

# Generated at 2022-06-13 02:33:17.448039
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() == False

# Generated at 2022-06-13 02:33:18.616289
# Unit test for function is_chroot
def test_is_chroot():
    # We should be inside the ansible-test chroot
    assert is_chroot()

# Generated at 2022-06-13 02:33:28.106438
# Unit test for function is_chroot
def test_is_chroot():
    # when we are in a chroot, / and /proc/1/root/ have the same dev but different ino
    class FakeModule(object):
        def get_bin_path(self, a):
            return None

        def run_command(self, a):
            return 1, 'xfs', ''

    class FakeStat(object):
        st_ino = 128
        st_dev = 1

    fake_module = FakeModule()

    result = is_chroot(fake_module)
    assert result is False

    os.stat = lambda x: FakeStat()

    result = is_chroot(fake_module)
    assert result is True

    os.stat = lambda x: FakeStat()
    os.stat.st_ino = 2

    result = is_chroot(fake_module)
    assert result is False

# Generated at 2022-06-13 02:33:44.347207
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot()

# Generated at 2022-06-13 02:33:45.155581
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() == True

# Generated at 2022-06-13 02:33:52.862415
# Unit test for function is_chroot
def test_is_chroot():

    # Prepare a mock module
    class MockModule:
        def get_bin_path(self, bin_path):
            if bin_path == 'stat':
                return self.stat_path

        def run_command(self, cmd):
            if cmd[0] == self.stat_path:
                return self.stat_rc, self.stat_out, self.stat_err

    # Test all branches of the function using btrfs and xfs as extra filesystems

# Generated at 2022-06-13 02:34:02.099410
# Unit test for function is_chroot
def test_is_chroot():
    from ansible.module_utils import basic
    import ansible_collections.ansible.misc.tests.unit.compat.mock as mock

    # FIXME: remove this after other facts are fixed
    # Probably need to move this test to test_low_level.py
    fake_module = basic.AnsibleModule(argument_spec={}, supports_check_mode=True)
    fake_module_without_bin = basic.AnsibleModule(argument_spec={}, supports_check_mode=True)

    # mock is_suse, which is a prerequisite for is_chroot
    fake_module_without_bin.run_command = mock.Mock(return_value=(0, '', ''))
    fake_module_without_bin.get_bin_path = mock.Mock(return_value=None)

    fake_

# Generated at 2022-06-13 02:34:03.819364
# Unit test for function is_chroot
def test_is_chroot():
    module = None
    collected_facts = None
    fact_collector = ChrootFactCollector()
    assert fact_collector.collect(module, collected_facts) == {'is_chroot': False}

# Generated at 2022-06-13 02:34:04.419634
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() is False

# Generated at 2022-06-13 02:34:05.042340
# Unit test for function is_chroot
def test_is_chroot():
    assert not is_chroot()

# Generated at 2022-06-13 02:34:06.747022
# Unit test for function is_chroot
def test_is_chroot():
    os.environ['debian_chroot'] = False
    assert is_chroot() is None
    os.environ['debian_chroot'] = True
    assert is_chroot() is True
    del os.environ['debian_chroot']

# Generated at 2022-06-13 02:34:07.469347
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() is False, "Detect chroot incorrectly"

# Generated at 2022-06-13 02:34:12.381789
# Unit test for function is_chroot
def test_is_chroot():
    for path in ('/', '/no/such/file'):
        __builtins__['open'] = lambda x, y: os.open(x, y)
        __builtins__['os'] = os
        assert is_chroot() == os.stat('/').st_ino != os.stat('/proc/1/root/.').st_ino

# Generated at 2022-06-13 02:34:48.921411
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() == False

# Generated at 2022-06-13 02:34:52.884303
# Unit test for function is_chroot
def test_is_chroot():

    class MockModule(object):
        def run_command(self, cmd):
            if cmd[0] == '/usr/bin/stat' and cmd[1:] == ['-f', '--format=%T', '/']:
                return 0, 'xfs', ''
            else:
                raise Exception("Unexpected run_command: %s" % (cmd,))

        def get_bin_path(self, cmd):
            if cmd == 'stat':
                return '/usr/bin/stat'
            else:
                raise Exception("Unexpected get_bin_path: %s" % (cmd,))

    assert is_chroot(MockModule()) is True

# Generated at 2022-06-13 02:34:54.978371
# Unit test for function is_chroot
def test_is_chroot():

    import os
    import tempfile

    # I should be the chroot
    assert is_chroot()

    # create a temporary directory
    tmpdir = tempfile.mkdtemp()
    os.chdir(tmpdir)

    # I should not be in a chroot
    assert not is_chroot()

    # cleanup
    os.chdir('/')
    os.rmdir(tmpdir)

# Generated at 2022-06-13 02:35:00.058611
# Unit test for function is_chroot
def test_is_chroot():
    try:
        # In a chroot this will fail, since the filesystem will not be mounted at /proc/1/root
        os.stat('/proc/1/root/.')
        assert not is_chroot()

    except (OSError, IOError):
        assert is_chroot()

# Generated at 2022-06-13 02:35:06.980809
# Unit test for function is_chroot
def test_is_chroot():
    import os
    import shutil
    import tempfile

    # In a chroot
    tmpdir = tempfile.mkdtemp()

    # changing the root when we are not root does not work
    os.chroot(tmpdir)
    os.chdir('/')
    # we are not chrooted
    assert not is_chroot()

    os.chroot(tmpdir)
    os.chdir('/')
    # we are chrooted
    assert is_chroot()

    shutil.rmtree(tmpdir)

    # Not in a chroot
    assert not is_chroot()

# Generated at 2022-06-13 02:35:12.668434
# Unit test for function is_chroot
def test_is_chroot():

    class FakeModule(object):
        pass

    assert is_chroot() is True

    module = FakeModule()
    module.run_command = lambda *_: (0, 'xfs', '')
    assert is_chroot(module) is True

    module.run_command = lambda *_: (0, 'ext3', '')
    assert is_chroot(module) is True

    module.run_command = lambda *_: (0, 'ext2', '')
    assert is_chroot(module) is True

    module.run_command = lambda *_: (0, 'btrfs', '')
    assert is_chroot(module) is True

# Generated at 2022-06-13 02:35:21.928353
# Unit test for function is_chroot
def test_is_chroot():
    """ Test whether the is_chroot function returns the correct value
    """
    try:
        import mock
    except ImportError:
        from ansible.module_utils.six.moves.mock import mock
    import sys
    import shutil
    import tempfile
    import os

    tmp_dir = tempfile.mkdtemp()
    os.mkdir(os.path.join(tmp_dir, 'proc'))
    os.mkdir(os.path.join(tmp_dir, 'proc', '1'))
    os.mkdir(os.path.join(tmp_dir, 'proc', '1', 'root'))

    # create a link to '../..' so that we can see that it is a chroot

# Generated at 2022-06-13 02:35:25.308275
# Unit test for function is_chroot
def test_is_chroot():
    import ansible.module_utils.facts.chroot as chroot
    # Run the method to test without module being passed
    is_chroot = chroot.is_chroot()
    # We should get True for ansible run in a chroot, False otherwise
    if os.environ.get('debian_chroot', False):
        assert is_chroot
    else:
        assert not is_chroot

# Generated at 2022-06-13 02:35:28.221472
# Unit test for function is_chroot
def test_is_chroot():

    assert is_chroot() is False
    os.environ['debian_chroot'] = 'Test_chroot'
    assert is_chroot() is True

# Generated at 2022-06-13 02:35:29.137579
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot()

# Generated at 2022-06-13 02:36:55.123278
# Unit test for function is_chroot
def test_is_chroot():
    assert isinstance(is_chroot(), bool)

# Generated at 2022-06-13 02:36:56.444032
# Unit test for function is_chroot
def test_is_chroot():
    is_chroot()

# Generated at 2022-06-13 02:36:57.466883
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() is False

# Generated at 2022-06-13 02:36:58.139098
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() is False, "Should not be a chroot by default"

# Generated at 2022-06-13 02:37:03.457168
# Unit test for function is_chroot
def test_is_chroot():
    # a fake module object
    class FakeModule(object):

        def get_bin_path(self, cmd):
            if cmd == 'stat':
                return cmd

        def run_command(self, cmd):
            import subprocess
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
            out, err = p.communicate()
            return 0, out, ''

    fs_root_ino = 2
    fake_module = FakeModule()

    my_root = os.stat('/')

# Generated at 2022-06-13 02:37:04.506841
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot(module=None) != False, 'invalid chroot check'

# Generated at 2022-06-13 02:37:09.029139
# Unit test for function is_chroot
def test_is_chroot():
    import os
    import tempfile

    with tempfile.TemporaryDirectory() as td:
        chroot_dir = os.path.join(td, 'chroot')
        os.mkdir(chroot_dir)
        os.chroot(chroot_dir)
        assert is_chroot()

# Generated at 2022-06-13 02:37:18.526532
# Unit test for function is_chroot
def test_is_chroot():

    class FakeModule(object):
        def get_bin_path(self, cmd, default=None):
            return None

        def run_command(self, cmd):
            return 0, '', ''

    my_fake_module = FakeModule()
    assert(is_chroot() and is_chroot(my_fake_module))

    class FakeModuleBtrfs(object):
        def get_bin_path(self, cmd, default=None):
            return '/usr/bin/stat'
        def run_command(self, cmd):
            return 0, 'Btrfs', ''

    my_fake_module_btrfs = FakeModuleBtrfs()
    assert(not is_chroot(my_fake_module_btrfs))


# Generated at 2022-06-13 02:37:20.073810
# Unit test for function is_chroot
def test_is_chroot():
    from ansible.module_utils.facts.system.chroot import is_chroot
    assert isinstance(is_chroot(), bool)

# Generated at 2022-06-13 02:37:22.713928
# Unit test for function is_chroot
def test_is_chroot():
    assert is_chroot() == False