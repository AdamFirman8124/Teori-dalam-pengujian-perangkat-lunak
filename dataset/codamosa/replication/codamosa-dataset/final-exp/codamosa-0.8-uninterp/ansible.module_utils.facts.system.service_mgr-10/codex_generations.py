

# Generated at 2022-06-13 03:23:10.159118
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    mtargs = dict(module_name=__name__, module_args='', module_kwargs={})
    mbasic = AnsibleModule(**mtargs)
    assert ServiceMgrFactCollector.is_systemd_managed(mbasic) == False

    mtargs = dict(module_name=__name__, module_args='', module_kwargs={})
    mbasic = AnsibleModule(**mtargs)
    assert ServiceMgrFactCollector.is_systemd_managed(mbasic) == False


# Generated at 2022-06-13 03:23:12.334581
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():

    class TestModule(object):
        def get_bin_path(self, cmd):
            return '/usr/bin/systemctl'

    ServiceMgrFactCollector.is_systemd_managed_offline(TestModule())

# Generated at 2022-06-13 03:23:20.443440
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    from ansible.module_utils.facts import ModuleDataCollector
    from ansible.module_utils.facts.facts import Facts
    from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector
    from ansible.module_utils.facts.utils import get_file_content

    collected_facts = Facts({
        'distribution': 'RedHat',
        'distribution_release': '7.0',
        'distribution_version': '7.0',
        'product_name': 'Red Hat Enterprise Linux Server',
        'product_version': '7.0',
        'service_mgr': 'systemd',
        'system': 'Linux',
    })

    test_module = ModuleDataCollector()
    test_module.get_bin_path = lambda x: None  # mock function



# Generated at 2022-06-13 03:23:24.266986
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    # load the default class
    if ServiceMgrFactCollector.name not in __loader__.modules:
        cls = ServiceMgrFactCollector(__loader__)
    else:
        # reload the class
        cls = reload(__loader__.modules[ServiceMgrFactCollector.name])

    # create object
    obj = cls()

    # call collect method
    obj.collect(None)


# Generated at 2022-06-13 03:23:26.661981
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    ServiceMgrFactCollector._fact_ids = set()
    ServiceMgrFactCollector.required_facts = set(['platform', 'distribution'])
    assert ServiceMgrFactCollector().collect() == {}

# Generated at 2022-06-13 03:23:34.289008
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    def get_bin_path(cmd):
        if cmd == 'systemctl':
            return cmd
        return None

    def exists(cmd):
        if cmd == '/run/systemd/system/':
            return True
        return False

    module = Mock(spec=['run_command', 'get_bin_path'])
    module.get_bin_path.side_effect = get_bin_path
    module.run_command.return_value = (0, '', '')

    os.path.exists = Mock(side_effect=exists)

    assert ServiceMgrFactCollector.is_systemd_managed(module)

    module.get_bin_path.return_value = None
    module.run_command.return_value = (1, '', '')

# Generated at 2022-06-13 03:23:44.862988
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    import tempfile
    import os

    def test_case(in_systemd_managed, path, readlink_dest):
        # Copies of module parameters
        tmpdir = tempfile.mkdtemp()
        module = dict()
        module['get_bin_path'] = lambda path: path
        module['run_command'] = lambda cmd, use_unsafe_shell=True: (1, "", "")

        # Create symlink to systemd if needed
        if path and readlink_dest:
            os.symlink(readlink_dest, path)

        # Create the ServiceMgrFactCollector object and call tested method
        fact_collector = ServiceMgrFactCollector()
        assert fact_collector.is_systemd_managed_offline(module=module) == in_systemd_managed

        # Clean up


# Generated at 2022-06-13 03:23:51.044061
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    # use dummy module
    module = DummyAnsibleModule()

    # create instance of ServiceMgrFactCollector
    smfc = ServiceMgrFactCollector()

    # run collect method
    collected_facts = smfc.collect(module=module, collected_facts={})
    assert 'service_mgr' in collected_facts

# class to provide a mock of AnsibleModule

# Generated at 2022-06-13 03:23:53.861840
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():

    # Create instance of class ServiceMgrFactCollector
    test_instance = ServiceMgrFactCollector()

    assert test_instance.collect() == {'service_mgr': 'service'}


# Generated at 2022-06-13 03:23:59.771272
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collectors.service_mgr.systemd import ServiceMgrFactCollector
    from ansible.module_utils.facts.collectors.service_mgr.systemd import MockSystemd
    import pytest

    c = Collector()
    c.collectors = [ServiceMgrFactCollector()]
    c.collectors[0].module = MockSystemd()
    facts = c.collect()

    assert facts['service_mgr'] == 'systemd'

# Generated at 2022-06-13 03:24:20.209084
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    from ansible.module_utils.facts.collector import MockModule

    module = MockModule({'platform.dist': ('', ''), 'platform.system': ('Linux', '')})
    # /bin/systemctl -> initctl
    module.get_bin_path = lambda x: 'systemctl'
    module.run_command = lambda x, *args: (0, 'systemd\n', '')
    module.is_executable = lambda x: True
    collector = ServiceMgrFactCollector()
    result = collector.collect(module)
    assert len(result) == 1
    assert result['service_mgr'] == 'systemd'

# Generated at 2022-06-13 03:24:24.960643
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    # The is_systemd_managed_offline is static method.
    # So we need to instanciate a ServiceMgrFactCollector to call it.
    collector = ServiceMgrFactCollector()
    module = None
    # We don't have a test data as it depends on the system.
    # We simply test the code coverage.
    collector.is_systemd_managed_offline(module=module)

# Generated at 2022-06-13 03:24:36.075252
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.collector.system import SystemFactCollector
    from ansible.module_utils.facts.collector.pkg_mgr import PkgMgrFactCollector
    from ansible.module_utils.facts.collector import collect_facts
    from ansible.module_utils.facts.utils import get_file_content
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts.system.platform import PlatformFactCollector

    test_module = get_module(mock=True, get_ansible_module=False)

    test_module.run_command = run_command_mock
    test_module.get_bin_path = get_bin_path_m

# Generated at 2022-06-13 03:24:45.251818
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    from ansible.module_utils.facts.collector import Collector

    # Set up the collector
    collector = Collector()

    # Create a service_mgr_collector
    service_mgr_collector = ServiceMgrFactCollector()

    # Set up the mock module
    class Module(object):
        def get_bin_path(self, name):
            if name == 'systemctl':
                return '/bin/systemctl'
            return None

    # Create a mock module
    module = Module()

    # Return the mocked value for method is_systemd_managed_offline
    if os.path.exists('/sbin/init'):
        return os.readlink('/sbin/init') == 'systemd'

    # Return the mocked value for method is_systemd_managed_offline
    return False


#

# Generated at 2022-06-13 03:24:51.376991
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():

    import os, tempfile

    class FakeModule(object):

        def __init__(self):
            self.tmp_dir = tempfile.mkdtemp()
            self.path = self.tmp_dir

        def get_bin_path(self, prog):
            return os.path.join(self.path, prog)

        def run_command(self, cmd, **kwargs):
            return 0, '', ''

    class FakeAnsibleModule(object):

        def __init__(self):
            self.tmp_dir = tempfile.mkdtemp()
            self.path = self.tmp_dir

        def get_bin_path(self, prog):
            return os.path.join(self.path, prog)

    smg = ServiceMgrFactCollector()

    # systemctl not present
    mod = FakeAn

# Generated at 2022-06-13 03:25:03.560309
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    from ansible.module_utils.facts.collector import ServiceMgrFactCollector
    from ansible.module_utils.facts import Collector
    from ansible.module_utils._text import to_bytes

    module = MockModule()
    Collector.module_cache['ansible_system'] = to_bytes('Linux')
    Collector.module_cache['ansible_service_mgr'] = to_bytes('sysvinit')

    # check case when /sbin/init is not a symlink
    if os.path.islink('/sbin/init'):
        os.unlink('/sbin/init')
    assert not ServiceMgrFactCollector.is_systemd_managed_offline(module=module)

    # check case when /sbin/init is a symlink but it does not point to systemd

# Generated at 2022-06-13 03:25:10.835577
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    import ansible.module_utils.facts.collector
    from ansible.utils.color import stringc
    from ansible.module_utils.facts import ModuleDepFactsCollector

    print("Testing ServiceMgrFactCollector.collect()")
    test_data = [
        {
            'service_mgr': 'service_mgr_test'
        }
    ]
    # Mock classes
    class MockFactsCollector:
        def __init__(self):
            self.all_facts = {
                'service_mgr': 'service_mgr_test',
                'systemd': 'service_mgr_test'
            }

    class MockAnsibleModule:
        def __init__(self):
            self.params = {
                'service_mgr': 'service_mgr_test'
            }

# Generated at 2022-06-13 03:25:16.210574
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    """is_systemd_managed_offline should return True if /sbin/init is a symlink to systemd"""
    class FakeModule(object):
        def get_bin_path(self, command):
            path = '/bin/%s' % command
            if os.path.exists(path):
                return path
        def run_command(self, cmd, use_unsafe_shell=True):
            pass

    fake_module = FakeModule()
    if os.path.exists('/sbin/init'):
        os.rename('/sbin/init', '/sbin/init.old')
    open('/sbin/init', 'w').close()

    assert not ServiceMgrFactCollector.is_systemd_managed_offline(fake_module)


# Generated at 2022-06-13 03:25:19.249041
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    class MockModule:
        def __init__(self, path):
            self.path = path

        def get_bin_path(self, program):
            return self.path

    assert ServiceMgrFactCollector.is_systemd_managed(MockModule('/usr/bin/systemctl'))

    assert not ServiceMgrFactCollector.is_systemd_managed(MockModule(None))



# Generated at 2022-06-13 03:25:28.297844
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    # test for detected systemd
    os.path.exists = lambda filename: False
    os.path.exists.__name__ = 'exists'
    os.path.islink = lambda filename: False
    os.path.islink.__name__ = 'islink'
    os.readlink = lambda filename: True
    os.readlink.__name__ = 'readlink'
    assert ServiceMgrFactCollector.is_systemd_managed({'get_bin_path': lambda executable: True}), "Testing for detected systemd failed"


# Generated at 2022-06-13 03:25:41.841663
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    expected = True
    actual = ServiceMgrFactCollector.is_systemd_managed(None)
    assert expected == actual

# Generated at 2022-06-13 03:25:51.005447
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    from ansible.module_utils import basic
    from ansible.module_utils.facts import Collector
    from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector
    import tempfile
    import shutil
    import os

    # create temporary directory to serve as root filesystem
    root = tempfile.mkdtemp()
    # create /sbin/init symlink - test should recognize it as systemd managed
    os.symlink('/bin/ls', os.path.join(root, 'sbin', 'init'))

    setattr(basic.AnsibleModule, "run_command", lambda self, command, use_unsafe_shell=True: ('', '', 0))
    setattr(basic.AnsibleModule, "get_bin_path", lambda self, command: 'systemctl')



# Generated at 2022-06-13 03:25:53.838773
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    collector = ServiceMgrFactCollector()
    results = collector.is_systemd_managed(None)
    assert results == True

# Generated at 2022-06-13 03:25:59.418241
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    class ModuleFake(object):
        def __init__(self, path):
            self.path = path

        def get_bin_path(self, path, opt_dirs=[]):
            if path == "systemctl":
                return "/usr/bin/systemctl"
            else:
                return None

    module = ModuleFake({})
    # It should return True
    assert ServiceMgrFactCollector.is_systemd_managed(module)

# Generated at 2022-06-13 03:26:06.062879
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    import mock
    import os
    from ansible.module_utils.facts import collector

    # install mock into class namespace
    service_mgr_collector = None
    for key, obj in collector.__dict__.items():
        if key == 'ServiceMgrFactCollector':
            service_mgr_collector = obj
            break

    # mock module input
    failsafe_os = os.path
    os.path = mock.Mock()
    os.path.exists.side_effect = [False, False, True]

    if service_mgr_collector:
        module = mock.Mock()
        module.get_bin_path.return_value = '/bin/systemctl'

        # systemctl exists and canary run/systemd/system exists => systemd detected

# Generated at 2022-06-13 03:26:13.885664
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    '''The is_systemd_managed_offline method returns True if systemd manages the init system'''
    class TestModule(object):
        def __init__(self, bin_path, linkname):
            self.bin_path = bin_path
            self.linkname = linkname

        def get_bin_path(self, name):
            if name == 'systemctl':
                return self.bin_path
            return None

    # systemd-sysvinit is installed, but systemd is not the boot init system
    testmodule = TestModule('/usr/bin/systemctl', '/sbin/init')
    collector = ServiceMgrFactCollector()
    assert collector.is_systemd_managed_offline(module=testmodule) == False

    # systemd is the boot init system

# Generated at 2022-06-13 03:26:23.809882
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    from ansible.utils.path import unfrackpath
    from ansible.module_utils.facts import ModuleFacts
    # Create a fake module. Since this is a unit test and not an integration test, we do not want
    # to do a full fake with "ansible.module_utils.basic". Instead mock everything in basic that
    # we need.
    # This is a little ugly, but it is the best way to do it as of Ansible 2.3.
    class FakeModule:
       def __init__(self):
           self.get_bin_path = lambda path: path
           self.run_command = lambda path: ("", "", 0)
    def fake_ansible_module():
        return FakeModule()
    # Mock the module loader.
    import ansible.module_utils
    ansible.module_utils.basic = fake

# Generated at 2022-06-13 03:26:32.468097
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    test_facts = {
        'ansible_distribution': 'MacOSX',
        'ansible_system': 'Apple',
        'platform': 'Darwin',
        'distribution': ''
    }
    fact_collector = ServiceMgrFactCollector()
    facts = fact_collector.collect(collected_facts=test_facts)
    assert facts is not None
    assert facts['service_mgr'] == 'launchd'
    assert 'ansible_service_mgr' not in facts

# Generated at 2022-06-13 03:26:36.932287
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.collector import BaseFactCollector
    class ClassDynamicMock(BaseFactCollector):
        name = 'test_ServiceMgrFactCollector_collect'
        _fact_ids = set()
        required_facts = set(['platform', 'distribution'])

        def collect(self, module=None, collected_facts=None):
            return {'test_ServiceMgrFactCollector_collect': collected_facts['distribution']}

    class_mock = ClassDynamicMock()
    Collector = get_collector_instance('service_mgr', class_mock)

    class_mock = ClassDynamicMock()

# Generated at 2022-06-13 03:26:40.880748
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():

    class Object(object):
        def get_bin_path(self, arg):
            return 'systemctl'

    s = Object()
    f = ServiceMgrFactCollector()
    assert f.is_systemd_managed_offline(s) is True


# Generated at 2022-06-13 03:27:03.645457
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():

    class ModuleStub:
        def __init__(self):
            self._facts = {'platform': 'Linux', 'ansible_distribution': 'Debian', 'ansible_distribution_release': '9.9.9', 'ansible_distribution_version': '9.9.9', 'ansible_system': 'Linux'}

        @property
        def facts(self):
            return self._facts

        def get_bin_path(self, item):
            if item == 'systemctl':
                return '/usr/bin/systemctl'
            elif item == 'initctl':
                return '/usr/bin/initctl'
            else:
                return None

        def run_command(self, command, **kwargs):
            return (0, '', '')


# Generated at 2022-06-13 03:27:08.558129
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():

    # Unit test case 1:
    # Test module initialization with empty configuration parameters.

    mock_module = MagicMock(params=dict())

    service_mgr_collector = ServiceMgrFactCollector()

    service_mgr_collector.collect(module=mock_module)

    # Unit test case 2:
    # Test module initialization with non empty configuration parameters.

    mock_module = MagicMock(params=dict(
        ansible_distribution="MacOSX",
        ansible_system='SunOS',
    ))

    service_mgr_collector = ServiceMgrFactCollector()

    service_mgr_collector.collect(module=mock_module)

    # Unit test case 3:
    # Test module initialization with non empty configuration parameters.


# Generated at 2022-06-13 03:27:19.673940
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    from ansible.module_utils.facts.collector import BaseFactCollector
    import os
    import platform

    # Pretend we are running Linux
    plat = platform.system
    platform.system = lambda: 'Linux'

    # Create Object of ServiceMgrFactCollector class
    service_mgr = ServiceMgrFactCollector()
    facts_dict = {}
    collected_facts = {'ansible_distribution': 'SUSE'}

    # Create mock module object, since we don't have access to a real AnsibleModule object
    class AnsibleModule():
        name = 'test'
        args = {}

        def get_bin_path(self, path, opt_dirs=[]):
            return path


# Generated at 2022-06-13 03:27:21.496719
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    ServiceMgrFactCollector.is_systemd_managed(module=None)

# Generated at 2022-06-13 03:27:27.865526
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts.collector import ServiceMgrFactCollector

    class MockModule():
        def get_bin_path(self, cmd):
            if cmd == 'systemctl':
                return 'systemctl'

    assert ServiceMgrFactCollector.is_systemd_managed(MockModule()) == False


# Generated at 2022-06-13 03:27:35.969665
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    import ansible.module_utils.facts.collector.service_mgr
    collected_facts = {
        'ansible_distribution': 'Debian',
        'ansible_distribution_version': '10',
        'ansible_system': 'Linux',
    }
    collector = ansible.module_utils.facts.collector.service_mgr.ServiceMgrFactCollector()
    sut = collector.is_systemd_managed
    assert not sut(module=None)
    assert not sut(module=MockModule(get_bin_path='/bin/systemctl'))



# Generated at 2022-06-13 03:27:40.372167
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    # Arrange
    collector = ServiceMgrFactCollector()
    facts_dict = {}
    # Act
    actual_facts_dict = collector.collect(facts_dict)
    # Assert
    assert 'service_mgr' in actual_facts_dict.keys()
    assert isinstance(actual_facts_dict['service_mgr'], str)

# Generated at 2022-06-13 03:27:50.471608
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    # create a fake module
    module = AnsibleModuleMock()

    # create an instance of the service manager fact collector
    service_mgr_fc = ServiceMgrFactCollector()

    # we should be able to get the unit test to identify our fake module with systemd
    assert service_mgr_fc.is_systemd_managed(module) == True

    # create a fake module which has the 'systemctl' executable but is not a systemd environment
    module = AnsibleModuleMock(systemctl_exe=True)

    # we should be able to get the unit test to identify our fake module without systemd
    assert service_mgr_fc.is_systemd_managed(module) == False

    # create a fake module which does not have the 'systemctl' executable
    module = AnsibleModuleMock()

    # we should be able to get the

# Generated at 2022-06-13 03:27:59.799234
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    # given
    class Module:
        def get_bin_path(self, arg):
            if arg == 'systemctl':
                return '/bin/systemctl'
            return None

        def run_command(self, arg):
            # do not look at the arguments, just return a valid result
            return (0, '', '')

    class ModuleMock:
        # FIXME: move to tests/module_utils/module.py
        def __init__(self):
            self.module = Module()

    module = ModuleMock()

    # when
    facts = ServiceMgrFactCollector()

    # then
    assert facts.is_systemd_managed_offline(module) is False

# Generated at 2022-06-13 03:28:08.983541
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    from ansible.module_utils.facts.collector import ServiceMgrFactCollector
    from ansible.module_utils.facts import collector
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.compat import mock

    test_files = {
        '/sbin/init': to_bytes('/lib/systemd/systemd'),
        '/bin/bash': to_bytes('/bin/bash'),
    }

    with mock.patch.dict(os.path, test_files, clear=True):
        assert ServiceMgrFactCollector.is_systemd_managed_offline(mock.MagicMock(get_bin_path=collector.get_bin_path)) == True


# Generated at 2022-06-13 03:28:36.581537
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    class MockModule(object):
        def __init__(self, is_systemd_managed, is_systemd_managed_offline):
            self.is_systemd_managed_result = is_systemd_managed
            self.is_systemd_managed_offline_result = is_systemd_managed_offline

        def get_bin_path(self, binary):
            return binary == 'systemctl'

    # Test case 1: Systemd
    service_mgr_collector = ServiceMgrFactCollector()
    mock_module = MockModule(True, False)

    collected_facts = {
        'ansible_distribution': 'Linux',
        'ansible_system': 'Linux',
    }

    facts_dict = service_mgr_collector.collect(mock_module, collected_facts)

# Generated at 2022-06-13 03:28:41.211257
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    from ansible.module_utils.facts.collector import DummyModule

    class DummyModule(object):
        def __init__(self, *args, **kwargs):
            self.params = {}
            self.exit_json = lambda *args: None
            self.fail_json = lambda *args: None

        def get_bin_path(self, arg, *args, **kwargs):
            return arg

    obj = ServiceMgrFactCollector()
    obj._module = DummyModule()
    obj.collect(module=None, collected_facts=None)

# Generated at 2022-06-13 03:28:50.110195
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    from ansible.module_utils.facts.collector import collector_registry
    from ansible.module_utils.facts.collector import BaseFactCollector

    # Create an instance of BaseFactCollector
    fact_collector = BaseFactCollector()

    # Create an instance of ServiceMgrFactCollector
    service_mgr = ServiceMgrFactCollector()

    # test /sbin/init is systemd
    setattr(fact_collector, 'module', Mock())
    fact_collector.module.get_bin_path.return_value = '/usr/bin/systemctl'
    assert service_mgr.is_systemd_managed_offline(module=fact_collector.module) == True

    # test /sbin/init is not systemd
    setattr(fact_collector, 'module', Mock())
    fact

# Generated at 2022-06-13 03:28:59.918437
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    import copy
    import os

    from ansible_collections.ansible.community.tests.unit.modules.utils import set_module_args
    import ansible_collections.ansible.community.plugins.module_utils.basic
    import ansible_collections.ansible.community.plugins.module_utils.facts.collectors

    service_mgr_fact_collector = ansible_collections.ansible.community.plugins.module_utils.facts.collectors.service_mgr.ServiceMgrFactCollector
    module = ansible_collections.ansible.community.plugins.module_utils.basic.AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )
    set_module_args({})

# Generated at 2022-06-13 03:29:07.371813
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    test_collector = ServiceMgrFactCollector()

    class Module:
        def __init__(self):
            self.run_command = lambda: ('rc', 'comm', 'stderr')

    module = Module()
    assert test_collector.collect({}, collected_facts={}, module=module) == {'service_mgr': 'service'}

    class Module:
        def __init__(self):
            self.run_command = lambda: ('rc', 'svscan', 'stderr')
        def get_bin_path(self, command):
            return 'path'

    module = Module()
    assert test_collector.collect({}, collected_facts={}, module=module) == {'service_mgr': 'svc'}

    class Module:
        def __init__(self):
            self.run

# Generated at 2022-06-13 03:29:16.736862
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    smfc = ServiceMgrFactCollector()
    module = FakeModule()
    systemd_check = smfc.is_systemd_managed(module)

    assert systemd_check == False

    # Overwrite the type of module to return a non-false value when run_command is called
    class FakeModule2(FakeModule):
        def run_command(self, command, use_unsafe_shell=False):
            return 0, "hello world", ""

    module = FakeModule2()
    systemd_check = smfc.is_systemd_managed(module)
    assert systemd_check == False

    # Overwrite the type of module to return a non-false value when get_bin_path is called
    class FakeModule3(FakeModule):
        def get_bin_path(self, command):
            return "/bin/systemctl"

    module

# Generated at 2022-06-13 03:29:23.572291
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    context=dict()
    context['ansible_facts'] = dict()
    context['ansible_facts']['ansible_system'] = "SunOS"
    context['ansible_facts']['ansible_distribution'] = 'Solaris'
    context['ansible_facts']['ansible_distribution_version'] = '11.2'
    context['ansible_facts']['ansible_distribution_release'] = '11.2'

    service_mgr = ServiceMgrFactCollector()
    module = AnsibleModule(argument_spec=dict())

    # test with a symlink does not exist at /sbin/init
    rc, output, err = module.run_command("rm -f /sbin/init", use_unsafe_shell=True)

# Generated at 2022-06-13 03:29:31.272264
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():

    tmp_path = tempfile.mkdtemp()
    os_path_exists_saved = os.path.exists

# Generated at 2022-06-13 03:29:41.990228
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    """ ServiceMgrFactCollector: test method is_systemd_managed """
    import ansible.module_utils.facts.system.service_mgr
    import ansible.module_utils.facts.system.base
    import ansible.module_utils.facts.system.distribution
    import ansible.module_utils.facts.system.platform
    import ansible.module_utils.facts.system.pkg_mgr
    import ansible.module_utils.facts.system.user

    MODULE = ansible.module_utils.facts.system.service_mgr.ServiceMgrFactCollector
    BASE = ansible.module_utils.facts.system.base.BaseFactCollector
    DISTRIBUTION = ansible.module_utils.facts.system.distribution.DistributionFactCollector
    PLATFORM = ansible.module_utils

# Generated at 2022-06-13 03:29:49.288737
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    # FIXME: not sure if this will work under unit tests
    fact_collector = ServiceMgrFactCollector()
    mock_module = MockModule(None)
    assert ServiceMgrFactCollector.is_systemd_managed(mock_module) is False

    mock_module.params = {'systemctl': 'any'}
    mock_module.run_command = lambda x, y: (0, '', '')
    assert ServiceMgrFactCollector.is_systemd_managed(mock_module) is True



# Generated at 2022-06-13 03:30:26.935538
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    from ansible.module_utils.facts.collector import ServiceMgrFactCollector
    from ansible.module_utils.facts.utils import get_file_content

    # Test case: systemd is the boot init system
    # /sbin/init is symlink to systemd
    os.symlink("/bin/systemd", "/sbin/init")
    assert ServiceMgrFactCollector.is_systemd_managed_offline(None),\
        'Systemd is not detected as the boot init system.'

    # Test case: systemd is not the boot init system
    # /sbin/init is symlink to some other executable
    os.symlink("/bin/bash", "/sbin/init")

# Generated at 2022-06-13 03:30:35.222510
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts.collector import ServiceMgrFactCollector

    # 1. Check if systemd is running
    # Monkey patch ansible.module_utils.facts.collector.ServiceMgrFactCollector.is_systemd_managed() in order to always return true
    old_is_systemd_managed = ServiceMgrFactCollector.is_systemd_managed

    def is_systemd_managed(module):
        return True

    ServiceMgrFactCollector.is_systemd_managed = is_systemd_managed

    service_mgr = ServiceMgrFactCollector().collect()['service_mgr']
    assert service_mgr == 'systemd'

    # 2. Check if systemd is not running
    # Monkey patch ansible.module_utils.facts.collector.ServiceMgrFactCollector.is

# Generated at 2022-06-13 03:30:35.867945
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    pass


# Generated at 2022-06-13 03:30:40.869422
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    class MockModule(object):
        def __init__(self, path):
            self.path = path
        def get_bin_path(self, bin_name):
            if bin_name == 'systemctl':
                return self.path

    module = MockModule(None)
    assert ServiceMgrFactCollector.is_systemd_managed_offline(module) == False

    module = MockModule('/bin/systemctl')
    assert ServiceMgrFactCollector.is_systemd_managed_offline(module) == False

    module = MockModule('/bin/systemctl')
    os.symlink('/bin/systemctl', '/sbin/init')
    assert ServiceMgrFactCollector.is_systemd_managed_offline(module) == False
    os.remove('/sbin/init')

    module

# Generated at 2022-06-13 03:30:50.223414
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    import ansible.module_utils.facts.system.service_mgr as svc_mgr

    # test case 1: systemctl is not installed and /run/systemd/system/ does not exists
    fake_module = FakeModule()
    assert svc_mgr.ServiceMgrFactCollector.is_systemd_managed(fake_module) == False

    # test case 2: systemctl is installed and /run/systemd/system/ does not exists
    fake_module.systemctl_installed = True
    assert svc_mgr.ServiceMgrFactCollector.is_systemd_managed(fake_module) == False

    # test case 3: systemctl is installed and /run/systemd/system/ exists
    fake_module.systemd_system_exists = True
    assert svc_mgr.ServiceMgrFactCollect

# Generated at 2022-06-13 03:30:51.755405
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    assert ServiceMgrFactCollector.is_systemd_managed_offline(None) == False

# Generated at 2022-06-13 03:30:53.570624
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    collector = ServiceMgrFactCollector()
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    assert collector.is_systemd_managed_offline(module) == False
    assert collector.is_systemd_managed_offline(module) == False

# Generated at 2022-06-13 03:31:00.886508
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    import mock
    from ansible.module_utils.facts import Collector

    service_mgr = mock.Mock(
        name='service_mgr',
        is_systemd_managed=mock.Mock(return_value=False),
        is_systemd_managed_offline=mock.Mock(return_value=False)
    )

    mock_module = mock.Mock(
        get_bin_path=mock.Mock(return_value=False),
        run_command=mock.Mock(return_value=(0, 'init', '')),
    )
    mock_facts = dict()

    service_mgr.collect(module=mock_module, collected_facts=mock_facts)
    assert mock_module.run_command.called
    assert 'service_mgr' in mock_

# Generated at 2022-06-13 03:31:07.855570
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    # TestCase 1: when /sbin/init is linked to systemd
    class TestModule:
        def get_bin_path(self, binary):
            return binary

    import tempfile
    import shutil
    import os

    temp_dir = tempfile.mkdtemp()
    systemd_symlink = os.path.join(temp_dir, 'sbin', 'init')
    os.makedirs(os.path.dirname(systemd_symlink))

    open(systemd_symlink, 'a').close()
    os.symlink(systemd_symlink, os.path.join(temp_dir, '/sbin/init'))

    service_mgr_fact_collector = ServiceMgrFactCollector()
    assert service_mgr_fact_collector.is_systemd_managed

# Generated at 2022-06-13 03:31:13.410556
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():

    from ansible.module_utils.facts.collector import AnsibleModuleStub

    mock_module = AnsibleModuleStub()
    mock_module.command = ["/bin/systemctl"]
    mock_module.get_bin_path = lambda x: x
    mock_module.path_dwim = lambda x: x
    mock_module.check_mode = False

    smfc = ServiceMgrFactCollector()

    assert smfc.is_systemd_managed(module=mock_module) == True

    mock_module.command = ["/bin/foo"]

    assert smfc.is_systemd_managed(module=mock_module) == False
