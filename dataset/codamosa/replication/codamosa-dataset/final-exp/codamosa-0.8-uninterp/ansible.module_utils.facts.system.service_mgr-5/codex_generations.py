

# Generated at 2022-06-13 03:23:12.222607
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    from ansible.module_utils.facts import FactCollector, fallback_facts
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector
    from ansible.module_utils.facts.utils import get_file_content

    # set service_mgr fallback empty
    fallback_facts['service_mgr'] = None

    # initialize fact collector
    fact_collector = FactCollector(collected_facts=fallback_facts,
                                   raise_on_error=False,
                                   resource_facts_module=dict(),
                                   collectors=[ServiceMgrFactCollector])

    # collect facts
    facts = fact_collector.collect(module=None)
    assert 'service_mgr' in facts

# Generated at 2022-06-13 03:23:18.270810
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    '''Unit test for method collect of class ServiceMgrFactCollector.'''
    from ansible.module_utils.facts.collector import Collector

    # Create an instance of class Collector
    collector = Collector()

    # Create an instance of class ServiceMgrFactCollector
    service_mgr_collector = ServiceMgrFactCollector()

    # Check method collect of class ServiceMgrFactCollector
    assert service_mgr_collector.collect(collector)

# Execute the unit test
# test_ServiceMgrFactCollector_collect()

# Generated at 2022-06-13 03:23:26.588614
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts.collector.service_mgr import ServiceMgrFactCollector
    import os
    import shutil
    import tempfile
    import pytest


    def makedirs(name):
        try:
            os.makedirs(name)
        except OSError:
            pass

    results = {}
    results['ansible_facts'] = {}
    temp_dir = tempfile.mkdtemp(prefix='ansible_test_service_mgr')
    current_dir = os.getcwd()
    os.chdir(temp_dir)

    makedirs('/run/systemd/system/')
    makedirs('/dev/.run/systemd/')

# Generated at 2022-06-13 03:23:31.650791
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    from ansible.module_utils.facts.collector import MockModule
    Platform = 'AIX'
    Distribution = 'AIX'
    class MockAnsibleModule:
        def __init__(self):
            self.params = {}
            self.facts = {'ansible_system': Platform, 'ansible_distribution': Distribution}
        def get_bin_path(self, command):
            return command
    module = MockAnsibleModule()
    if (Platform == 'AIX'):
        smg = ServiceMgrFactCollector.collect(MockAnsibleModule())
        service_mgr = smg['service_mgr']
        assert service_mgr == 'src'

# Generated at 2022-06-13 03:23:40.563829
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    """
    Test method is_systemd_managed of class service_mgr.ServiceMgrFactCollector.
    """
    from ansible.module_utils.facts.collector import BaseFactCollector

    class MockModule(object):
        @staticmethod
        def get_bin_path(arg):
            return '/bin/systemctl'

    assert ServiceMgrFactCollector.is_systemd_managed(MockModule) is True



# Generated at 2022-06-13 03:23:48.463619
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    mock_module = Mock()
    mock_module.get_bin_path.return_value = None

    collector = ServiceMgrFactCollector()
    facts_dict = collector.collect(module=mock_module)
    assert facts_dict['service_mgr'] == 'service'

    mock_module.get_bin_path.return_value = 'systemctl'

    facts_dict = collector.collect(
        module=mock_module,
        collected_facts=dict(ansible_system='AIX', ansible_distribution='MacOSX')
    )
    assert facts_dict['service_mgr'] == 'src'

    facts_dict = collector.collect(
        module=mock_module,
        collected_facts=dict(ansible_system='Linux', ansible_distribution='MacOSX')
    )

# Generated at 2022-06-13 03:23:57.922973
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts.collector import FactsCollector
    facts = FactsCollector()
    facts_dict = facts.collect(module=None, collected_facts=None)
    facts_dict['ansible_system'] = 'Linux'

    # Mock module with fake commands/files
    module = type('Module', (object,), {
        'get_bin_path': lambda self, command: 'systemctl',
        'run_command': lambda self, command, **kwargs: ('systemd', '', ''),
        'run_command_expect_success': lambda self, command, **kwargs: ('systemd', '', ''),
        '_fail_json': lambda self, **kwargs: None
    })()

    assert ServiceMgrFactCollector.is_systemd_managed(module)



# Generated at 2022-06-13 03:24:04.464020
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    """
    Test the method ServiceMgrFactCollector.is_systemd_managed_offline.
        - The method is_systemd_managed_offline should return True if /sbin/init is a symlink to systemd.
    """
    try:
        from ansible.module_utils.facts.collector import ServiceMgrFactCollector
    except ImportError:
        raise AssertionError('Could not import ServiceMgrFactCollector.')
    if platform.system() != 'Linux':
        return
    # Create a temporary symlink at /sbin/init
    try:
        os.symlink('systemd', '/sbin/init')
    except OSError as e:
        raise AssertionError(str(e))
    # Test the method

# Generated at 2022-06-13 03:24:13.784575
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    class MockModule:
        def __init__(self):
            self.params = {}

        def get_bin_path(self, binary, required=False):
            return binary

        def run_command(self, cmd, use_unsafe_shell=False):
            return (0, '', '')

    class MockCollectedFacts:
        def __init__(self):
            self.ansible_facts = {
                'ansible_system': 'AIX',
                'ansible_distribution': 'OpenWrt',
                'ansible_distribution_version': '18.06.1',
            }

    # On OpenWrt
    module_obj = MockModule()
    collected_facts = MockCollectedFacts()
    service_mgr_collector = ServiceMgrFactCollector()

    assert service_mgr

# Generated at 2022-06-13 03:24:23.201673
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    smfc = ServiceMgrFactCollector()

    def mocked_is_systemd_managed(module):
        return smfc.is_systemd_managed(module)

    def mocked_is_systemd_managed_offline(module):
        return smfc.is_systemd_managed_offline(module)

    module = import_module('ansible.module_utils.facts.system.service_mgr')
    old_is_systemd_managed = getattr(module, 'is_systemd_managed')
    old_is_systemd_managed_offline = getattr(module, 'is_systemd_managed_offline')
    setattr(module, 'is_systemd_managed', mocked_is_systemd_managed)

# Generated at 2022-06-13 03:24:43.734560
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts.collector import Collector

    collector = Collector.from_fact_class(ServiceMgrFactCollector)
    assert collector.is_systemd_managed(None), 'should detect systemd in /run/systemd/system'
    assert collector.is_systemd_managed(None), 'should detect systemd in /dev/.run/systemd'
    assert collector.is_systemd_managed(None), 'should detect systemd in /dev/.systemd'
    assert not collector.is_systemd_managed(None), 'should not detect systemd in /run/systemd/not_systemd_system'

# Generated at 2022-06-13 03:24:50.729595
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():

    # The 'platform' module is a stub module for the unit test
    class platform_stub(object):
        @staticmethod
        def system():
            return 'Linux'

    import ansible.module_utils.facts.collectors.service_mgr as service_mgr

    class UtilStub(object):
        class module(object):
            class run_command(object):
                def __init__(self, cmd, use_unsafe_shell=True):
                    self.cmd = cmd
                    self.use_unsafe_shell = use_unsafe_shell

                def __call__(self, *args, **kwargs):
                    if self.cmd == ' which systemctl':
                        return 0, '/usr/bin/systemctl', ''

# Generated at 2022-06-13 03:25:03.233432
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    # Make sure to monkeypatch the module_utils at the beginning of the module before any code executes
    from ansible.module_utils.facts.collector import ModuleUtilsCollector
    ModuleUtilsCollector._platform = platform

    # Mock the module class
    from ansible.module_utils.facts import ModuleBase
    class FakeModule(ModuleBase):
        def __init__(self):
            self.run_command = self.mock_run_command

        # This is an actual command used in method collect of class ServiceMgrFactCollector
        # It is useful to see how the mocked functions are used
        def mock_run_command(self, cmd, use_unsafe_shell=False):
            if cmd == "ps -p 1 -o comm|tail -n 1":
                return 0, "/usr/bin/python2\n", ""


# Generated at 2022-06-13 03:25:10.712999
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    class MockModule(object):

        def get_bin_path(self, arg):
            if arg == 'systemctl':
                if os.path.exists('/etc/alpine-release'):
                    return '/bin/busybox'
                else:
                    return '/bin/systemctl'
        def run_command(self, arg, use_unsafe_shell=None):
            if arg == 'ps -p 1 -o comm|tail -n 1':
                if os.path.exists('/etc/alpine-release'):
                    return 0, '{sysv}', ''
                if os.path.exists('/etc/openrc/softlevel'):
                    return 0, '{openrc}', ''

# Generated at 2022-06-13 03:25:12.726443
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    os.symlink("systemd", "/sbin/init")
    assert ServiceMgrFactCollector.is_systemd_managed_offline(None) == True
    os.remove("/sbin/init")
    assert ServiceMgrFactCollector.is_systemd_managed_offline(None) == False

# Generated at 2022-06-13 03:25:22.045141
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    class _Host(object):
        def __init__(self):
            self.get_bin_path_return_value=None
            self.run_command_return_value=None
            self.run_command_return_value_rc=0

        def get_bin_path(self, value):
            return self.get_bin_path_return_value

    class _Module(object):
        def __init__(self):
            self.params=dict()
            self.check_mode=False

        def get_bin_path(self, value):
            return "/sbin/initctl"

        def run_command(self, value):
            return self.run_command_return_value_rc, self.run_command_return_value, None


# Generated at 2022-06-13 03:25:34.059704
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    sys_booted_paths = [
        "/run/systemd/system/",
        "/dev/.run/systemd/",
        "/dev/.systemd/"
    ]
    for i in range(len(sys_booted_paths)):
        os.environ['PATH'] = os.environ['PATH'] + ":" + sys_booted_paths[i]

        os.environ['PATH'] = os.environ['PATH'] + ":./bin/systemctl"
        result = ServiceMgrFactCollector.is_systemd_managed(None)
        assert result == True

    os.environ['PATH'] = os.environ['PATH'] + ":/usr/bin"
    result = ServiceMgrFactCollector.is_systemd_managed(None)
    assert result == False


# Generated at 2022-06-13 03:25:36.334481
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    current_systemd_managed = ServiceMgrFactCollector.is_systemd_managed(module=None)
    assert current_systemd_managed in (True, False)


# Generated at 2022-06-13 03:25:42.601665
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    class TestModule:
        def get_bin_path(self, path):
            if path == 'systemctl':
                return '/bin/systemctl'

    fact = ServiceMgrFactCollector()
    module = TestModule()
    platform = 'Linux'
    res = fact.collect(module, platform)
    assert 'service_mgr' in res
    assert res['service_mgr'] == 'systemd'



# Generated at 2022-06-13 03:25:51.351776
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    # create a mock ansible module for test
    # TODO: create test for multiple service manager
    # TODO: better test with mockup file /proc/1/comm
    from ansible.module_utils import basic
    from ansible.module_utils.facts import ansible_facts

    class AnsibleModule:

        def __init__(self, argument_spec, bypass_checks=False, check_invalid_arguments=True, mutually_exclusive=None,
                     supports_check_mode=False, required_together=None, required_one_of=None,
                     add_file_common_args=False, supports_diff=True):
            self.argument_spec = argument_spec
            self.bypass_checks = bypass_checks
            self.check_invalid_arguments = check_invalid_arguments
            self.mutually

# Generated at 2022-06-13 03:26:13.141380
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    from ansible.module_utils.facts import ModuleFacts
    from ansible.module_utils.facts import FactCollector

    script_dir = os.path.dirname(os.path.realpath(__file__))
    module_path = os.path.join(script_dir, '..', '..', '..', 'hacking', 'test-module')

    # Set up our modules and facts to test with

# Generated at 2022-06-13 03:26:23.447231
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    mock_module = create_mock_module()

    mock_module.SYSCTL_BIN = "/bin/false"
    mock_module.get_bin_path.side_effect = lambda path: path
    mock_module.mkdtemp.return_value = "/tmp/fake_root.1"

    collector = ServiceMgrFactCollector()

    def reset_mocks():
        mock_module.run_command.reset_mock()
        mock_module.os_path.reset_mock()

    mock_module.os_path.exists.side_effect = lambda path: True

    # /sbin/init is a symlink to systemd
    # ps command runs
    # init is systemd-sysvinit package
    output = collector.is_systemd_managed_offline(mock_module)
   

# Generated at 2022-06-13 03:26:27.688168
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    assert ServiceMgrFactCollector.is_systemd_managed_offline(None) is False
    assert ServiceMgrFactCollector.is_systemd_managed_offline(AnsibleModule(None)) is False

    class AnsibleModuleMock:
        def __init__(self, *args, **kwargs):
            self.bin_path_results = []

        def get_bin_path(self, app):
            return self.bin_path_results[0]

        def run_command(self, args, use_unsafe_shell=False):
            return (0, 'systemd', '')

    systemctl_exists_am = AnsibleModuleMock()
    systemctl_exists_am.bin_path_results = ['/usr/bin/systemctl']
    assert ServiceMgrFactCollector.is_

# Generated at 2022-06-13 03:26:31.780997
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    module = AnsibleModuleMock()
    service_mgr_fact_collector = ServiceMgrFactCollector()
    assert(service_mgr_fact_collector.is_systemd_managed(module) == False)


# Generated at 2022-06-13 03:26:43.371195
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    # import subprocess
    # subprocess.Popen(['/usr/bin/env', 'python', '-m', 'unittest', 'discover', '-v'])

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.collector import get_collector_instance

    class MockModule(object):
        def __init__(self):
            self.params = {}

        def run_command(self, cmd, use_unsafe_shell=False):
            return (1, '', '')

        def get_bin_path(self, cmd):
            return None


# Generated at 2022-06-13 03:26:52.308206
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector
    from ansible.module_utils._text import to_bytes

    class FakeModule(object):
        def __init__(self):
            self.run_command = self._fake_run_command
            self.get_bin_path = self._fake_get_bin_path

        def _fake_get_bin_path(self, *args, **kwargs):
            return to_bytes('/bin/systemctl')

        def _fake_run_command(self, *args, **kwargs):
            return 0, to_bytes('/lib/systemd/systemd'), ''

    module = FakeModule()
    assert ServiceMgrFactCollector.is_systemd_managed_offline(module)


# Generated at 2022-06-13 03:27:00.215335
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    collector = ServiceMgrFactCollector()

    # tempdir used to simulate a system with systemd running
    import tempfile
    import shutil
    tempdir = tempfile.mkdtemp()
    os.makedirs(tempdir + "/run/systemd/system/")
    assert collector.is_systemd_managed(tempdir)
    shutil.rmtree(tempdir)

    # tempdir used to simulate a system with systemd stopped
    tempdir = tempfile.mkdtemp()
    assert not collector.is_systemd_managed(tempdir)
    shutil.rmtree(tempdir)

# Generated at 2022-06-13 03:27:05.219790
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    module = MockAnsibleModule()
    module.get_bin_path.return_value = None
    assert ServiceMgrFactCollector.is_systemd_managed_offline(module) == False
    module.get_bin_path.return_value = "/usr/bin/systemctl"
    assert ServiceMgrFactCollector.is_systemd_managed_offline(module) == False
    module.get_bin_path.return_value = "/usr/bin/systemctl"
    setattr(os.path, 'islink', lambda self, value: False)
    assert ServiceMgrFactCollector.is_systemd_managed_offline(module) == False
    setattr(os.path, 'islink', lambda self, value: True)

# Generated at 2022-06-13 03:27:10.581431
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock import MagicMock, patch

    # set up the mock for methods or functions called by the method to be tested
    mock_module = MagicMock()
    mock_module.get_bin_path.return_value = "/usr/bin/systemctl"

    with patch('os.path.exists') as mock_path_exists:
        mock_path_exists.return_value = False

        # test if systemd is not managed
        assert False == ServiceMgrFactCollector.is_systemd_managed(mock_module)

        # test if systemd is managed
        mock_path_exists.return_value = True
        assert True == ServiceMgrFactCollector.is_systemd_managed(mock_module)



# Generated at 2022-06-13 03:27:21.090293
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    """
    ServiceMgrFactCollector.collect() Test
    """
    # Create mocks
    mock_module = MagicMock()
    mock_collected_facts = {
        'ansible_distribution': None,
        'ansible_system': None
    }

    # Test when proc_1_map.get(proc_1, proc_1) returns proc_1
    mock_proc_1 = "test"
    # Patch needed functions of ServiceMgrFactCollector
    with patch.object(ServiceMgrFactCollector, 'is_systemd_managed', return_value=False):
        with patch.object(ServiceMgrFactCollector, 'is_systemd_managed_offline', return_value=False):
            result = ServiceMgrFactCollector.collect(mock_module, mock_collected_facts)

# Generated at 2022-06-13 03:27:53.186231
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    facts_dict = {}
    service_mgr_fact_collector = ServiceMgrFactCollector()
    class MockModule(object):
        def __init__(self):
            self.params = {}
            self.exit_json = lambda x: (x)
            self.fail_json = lambda x: (x)
        def get_bin_path(self, *args, **kwargs):
            return None
        def run_command(self, *args, **kwargs):
            return (1, "", "")
    service_mgr_fact_collector.collect(MockModule(), facts_dict)
    assert facts_dict['service_mgr'] == 'service'

# Generated at 2022-06-13 03:27:54.482860
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    assert ServiceMgrFactCollector.is_systemd_managed("") == False


# Generated at 2022-06-13 03:27:56.412591
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():

    sl = ServiceMgrFactCollector()
    assert sl.is_systemd_managed_offline(module) == True, "Unexpected result for systemd init"

# Generated at 2022-06-13 03:28:07.836678
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    # Mocking module and env
    class MockedModule:
        def get_bin_path(self, path):
            if path == 'systemctl':
                return '/usr/bin/systemctl'

    class MockedEnv:
        def __init__(self):
            self.tmpdir = '/tmp'

    module = MockedModule()
    env = MockedEnv()

    # Mocking is_system_managed
    import os
    import tempfile
    original_os_path_exists = os.path.exists
    original_os_readlink = os.readlink
    def mock_os_path_exists(path):
        if path == '/tmp/systemd_unit_file.service':
            return True
        return original_os_path_exists(path)

# Generated at 2022-06-13 03:28:14.999452
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    import ansible.module_utils.facts.system.service_mgr

    temp1 = ansible.module_utils.facts.system.service_mgr.is_systemd_managed_offline
    ansible.module_utils.facts.system.service_mgr.is_systemd_managed_offline = lambda x: True
    assert ServiceMgrFactCollector.is_systemd_managed_offline(None) == True
    ansible.module_utils.facts.system.service_mgr.is_systemd_managed_offline = lambda x: False
    assert ServiceMgrFactCollector.is_systemd_managed_offline(None) == False
    ansible.module_utils.facts.system.service_mgr.is_systemd_managed_offline = temp1

# Generated at 2022-06-13 03:28:24.265037
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    # fake module class to store state
    class FakeModule():
        def __init__(self):
            self.get_bin_path_called = False
            self.run_command_called = False
            self.exists_called = False

        def get_bin_path(self, name):
            self.get_bin_path_called = True
            return name

        def run_command(self, name):
            self.run_command_called = True
            return 0, "", ""

        def exists(self, name):
            self.exists_called = True
            return True

    class FakeCollector():
        def __init__(self):
            self.distribution = ''
            self.platform = ''
            self.system = ''


# Generated at 2022-06-13 03:28:30.246591
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    # Assert correct return value when it is systemd managed
    m = type('module', (object,), {})
    m.get_bin_path = lambda name, default=None: '/bin/systemctl'
    os.path.exists = lambda path: False
    os.path.islink = lambda path: True
    os.readlink = lambda path: 'systemd'
    assert ServiceMgrFactCollector.is_systemd_managed(module=m) == True

    # Assert correct return value when it is not systemd managed
    m = type('module', (object,), {})
    m.get_bin_path = lambda name, default=None: None
    os.path.exists = lambda path: False
    os.path.islink = lambda path: True
    os.readlink = lambda path: 'systemd'


# Generated at 2022-06-13 03:28:39.003996
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    class FakeModule:
        def get_bin_path(self, cmd):
            return True

    class FakeFile:
        def read(self):
            return "systemd"

    if platform.system() != 'SunOS':
        import sys
        if sys.version_info[0] > 2:
            import builtins
            builtins.open = open
        else:
             import __builtin__
             __builtin__.open = open

        fake_file = FakeFile()
        fake_module = FakeModule()
        fake_service_manager = ServiceMgrFactCollector()

        open.return_value = fake_file
        assert fake_service_manager.is_systemd_managed_offline(fake_module)

# Generated at 2022-06-13 03:28:49.548998
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    from ansible.module_utils.facts import FactCollector, get_collector_instance
    import ansible.utils.plugin_docs as plugin_docs
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    import json
    import os

    dummy_module = plugin_docs.get_dummy_module()
    os.environ['ANSIBLE_PROCESS_ISOLATION'] = '0'

    # Initialize the fact collector
    fact_collector = get_collector_instance(FactCollector)

    # Run the collect method of ServiceMgrFactCollector
    collected_facts = fact_collector.collect(dummy_module)
    assert collected_facts['service_mgr'] == 'systemd'
    assert isinstance(collected_facts['service_mgr'], AnsibleUnsafeText)

# Generated at 2022-06-13 03:28:57.472394
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    import ansible.module_utils.facts.system.service_mgr

    class MockModule(object):
        def __init__(self):
            self._path = '/usr/bin:/bin:/usr/sbin:/sbin'

        def get_bin_path(self, cmd):
            if cmd == 'systemctl':
                return '/bin/systemctl'
            else:
                return None

    module = MockModule()

    is_systemd_managed = ansible.module_utils.facts.system.service_mgr.ServiceMgrFactCollector.is_systemd_managed(module)

    assert is_systemd_managed == False

# Generated at 2022-06-13 03:30:06.485049
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    """
    Test if is_systemd_managed_offline() method detects whether the system is under control of systemd.
    """
    os.environ['PATH'] = '/usr/bin:/bin'
    sut = ServiceMgrFactCollector()
    class MockModule:
        def get_bin_path(self, executable):
            return executable
    mock_module = MockModule()

    from ansible.module_utils.basic import AnsibleModule
    # Create mock system with symlink to systemd init
    with tempfile.TemporaryDirectory() as temp_dir:
        os.mkdir(os.path.join(temp_dir, 'sbin'))
        os.symlink('/lib/systemd/systemd', os.path.join(temp_dir, 'sbin/init'))
        sut.is_systemd

# Generated at 2022-06-13 03:30:17.208858
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    class F:
        def get_bin_path(self, p):
            if p == 'systemctl':
                return '/bin/systemctl'
            return None
    f = F()
    f.exists = os.path.exists
    f.is_systemd_managed = ServiceMgrFactCollector.is_systemd_managed
    assert f.is_systemd_managed(f) is False
    os.path.exists = lambda p: False
    assert f.is_systemd_managed(f) is False
    os.path.exists = lambda p: (p == "/run/systemd/system/")
    assert f.is_systemd_managed(f) is True
    os.path.exists = lambda p: (p == "/dev/.run/systemd/")
    assert f.is_system

# Generated at 2022-06-13 03:30:27.239049
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    from ansible.module_utils.facts.compat.version import LooseVersion
    from ansible.module_utils.facts import Module
    from ansible.module_utils.facts.utils import get_file_content

    class MockModule():
        def __init__(self, params={}):
            self.module = Module(argument_spec=params)

        @staticmethod
        def get_bin_path(name, required=True):
            return {
                'systemctl': '/usr/bin/systemctl',
                'initctl': '/usr/sbin/initctl',
            }.get(name)

        @staticmethod
        def run_command(cmd, check_rc=True, use_unsafe_shell=False):
            """
            Return 'ls -1 /' for ps command
            """

# Generated at 2022-06-13 03:30:29.975975
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    class Test():
        def __init__(self):
            self.run_command = lambda x: [0, '', '']
            self.get_bin_path = lambda x: '/bin/systemctl'
    module = Test()

    assert ServiceMgrFactCollector.is_systemd_managed(module) == True

# Generated at 2022-06-13 03:30:32.812672
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    try:
        import ansible.module_utils.facts.system.service_mgr
    except ImportError:
        print('ImportError: ansible.module_utils.facts.system.service_mgr cannot be imported')
    else:
        obj = ansible.module_utils.facts.system.service_mgr.ServiceMgrFactCollector()
        obj.collect()



# Generated at 2022-06-13 03:30:38.828757
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    from ansible.module_utils import basic
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collectors import ServiceMgrFactCollector
    from ansible.module_utils.facts.utils import get_file_content
    from ansible.module_utils.facts.utils import get_module_path
    from ansible.module_utils._text import to_native

    import os

    # Test to return fact 'service_mgr' as systemd
    def mock_collect_is_systemd_managed(module):
        return True

    # Test to return fact 'service_mgr' as sysvinit
    def mock_collect_is_systemd_managed_false(module):
        return False

    # Test to return fact 'service_mgr' as systemd

# Generated at 2022-06-13 03:30:48.290949
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    from ansible.module_utils.facts import serializer

    # Test inputs and expected results

# Generated at 2022-06-13 03:30:50.266958
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    service_mgr_fact_collector = ServiceMgrFactCollector()
    assert service_mgr_fact_collector.is_systemd_managed_offline({}) == False

# Generated at 2022-06-13 03:30:58.161616
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    import os
    import tempfile
    import shutil
    import platform
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.service_mgr import ServiceMgrFactCollector

    class DummyModule(object):
        class Result(object):
            def __init__(self, rc=1, stdout='', err=''):
                self.rc = rc
                self.stdout = to_bytes(stdout)
                self.stderr = to_bytes(err)

            def __bool__(self):
                return self.rc == 0

        def __init__(self):
            self.params = {'gather_subset': 'all'}
            self.result = {}

       

# Generated at 2022-06-13 03:31:05.561849
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    class MockModule:
        @staticmethod
        def get_bin_path(cmd):
            return cmd

    module = MockModule()

    class MockServiceMgrFactCollector(ServiceMgrFactCollector):
        @staticmethod
        def _is_systemd_file_candidate(candidate):
            return os.path.exists(candidate)

    msmfc = MockServiceMgrFactCollector()

    msmfc._is_systemd_file_candidate = lambda candidate: candidate == '/run/systemd/system/'
    assert msmfc.is_systemd_managed(module) is True

    msmfc._is_systemd_file_candidate = lambda candidate: candidate == '/dev/.run/systemd/'
    assert msmfc.is_systemd_managed(module) is True

    msm