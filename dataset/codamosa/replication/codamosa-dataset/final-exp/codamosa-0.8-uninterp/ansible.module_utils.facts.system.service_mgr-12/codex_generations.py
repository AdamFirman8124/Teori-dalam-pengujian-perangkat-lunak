

# Generated at 2022-06-13 03:23:09.604040
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collectors.service_mgr import ServiceMgrFactCollector

    class TestModule:
        def __init__(self):
            self.paths = ['1', '2', '3', '4']
            self.return_value = '/1\n/2\n/3\n/4\n'

        def get_bin_path(self, command):
            if 'systemctl' in command:
                return '/bin/systemctl'
            else:
                return None


        def run_command(self, command, use_unsafe_shell=True):
            return 0, self.return_value, None

    test_module = TestModule()
    service_mgr_fact_collector = ServiceM

# Generated at 2022-06-13 03:23:18.811484
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    from ansible.module_utils import basic
    from ansible.module_utils.facts import collector

    ansible_module = basic.AnsibleModule(argument_spec=dict())
    ansible_module.run_command = lambda args, check_rc=True: (0, 'init', '')
    ansible_module.get_bin_path = lambda arg: '/bin/' + arg
    ansible_module.get_file_content = lambda arg: None

    service_mgr_fact_collector = ServiceMgrFactCollector(ansible_module)
    collected_facts = collector.get_fact_dict(ansible_module)
    collected_facts['ansible_system'] = 'Linux'
    collected_facts['ansible_distribution'] = None
    collected_facts['platform'] = 'Linux'
    collected_facts

# Generated at 2022-06-13 03:23:26.866561
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    """ Unit test for method is_systemd_managed of class ServiceMgrFactCollector
    """
    import ansible.module_utils.facts.system.service_mgr

    # test with a directory that is not a systemd canary
    assert ServiceMgrFactCollector.is_systemd_managed_offline(None) is False
    assert ServiceMgrFactCollector.is_systemd_managed(None) is False

    # test with a directory that is an invalid systemctl
    module = MockModule(systemctl_path=None)
    assert ServiceMgrFactCollector.is_systemd_managed_offline(module) is False
    assert ServiceMgrFactCollector.is_systemd_managed(module) is False

    # test with a directory that is a valid systemctl and an invalid systemd canary

# Generated at 2022-06-13 03:23:34.469557
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    class MockModule:
        def get_bin_path(self, executable):
            if executable == 'systemctl':
                return '/bin/systemctl'
            elif executable == 'initctl':
                return '/bin/initctl'
            else:
                return None
    facts = {}
    module = MockModule()
    service_mgr_fact_collector = ServiceMgrFactCollector(module=module)

    # check that we have the correct systemd version
    facts['ansible_system'] = 'Linux'
    facts['distribution_major_version'] = '6'
    facts['ansible_distribution'] = 'RedHat'
    assert service_mgr_fact_collector.is_systemd_managed(module)

    facts['ansible_system'] = 'Linux'

# Generated at 2022-06-13 03:23:44.969700
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    from ansible import module_utils
    from ansible.module_utils.facts.collector import ServiceMgrFactCollector

    class MockModule(object):
        def __init__(self):
            self.run_command_os_stat_exists = False


# Generated at 2022-06-13 03:23:56.126338
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector

    def mock_get_bin_path(arg):
        if arg == 'systemctl':
            return '/bin/systemctl'

    def mock_path_exists(arg):
        if arg == '/run/systemd/system/':
            return True

    class MockModule(object):
        pass

    class MockOs(object):
        def __init__(self):
            self.path = MockOsPath()

    class MockOsPath(object):
        def __init__(self):
            self.exists = mock_path_exists

        def islink(self, arg):
            if arg == '/sbin/init':
                return True


# Generated at 2022-06-13 03:24:07.825981
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    import os
    import tempfile

    from ansible.module_utils.facts.collector import BaseFactCollector

    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.collector import get_collector_facts

    class MockModule:
        def get_bin_path(self, path):
            return None

    class MockCollector(BaseFactCollector):

        def __init__(self, *args, **kwargs):
            self._collect_subset = kwaws.get('subset', None)
            super(BaseFactCollector, self).__init__(*args, **kwargs)

        def collect(self, module=None, collected_facts=None):
            return { 'systemd': True }


# Generated at 2022-06-13 03:24:12.096526
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    from ansible.module_utils.facts.collector import get_collector_instance
    service_mgr_collector = get_collector_instance('ansible.module_utils.facts.system.service_mgr.ServiceMgrFactCollector')
    assert not service_mgr_collector.is_systemd_managed_offline(None)

# Generated at 2022-06-13 03:24:22.300033
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    from .test_utils.mock_module import MockModule
    import sys
    import os

    this_file = os.path.realpath(__file__)
    this_dir = os.path.dirname(this_file)
    lib_dir = os.path.join(this_dir, '..', '..', 'lib', 'ansible')
    if lib_dir not in sys.path:
        sys.path.append(lib_dir)

    import ansible.module_utils.facts.collectors.system

    # Create a mock module
    module = MockModule()


# Generated at 2022-06-13 03:24:26.045292
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    assert ServiceMgrFactCollector.is_systemd_managed_offline == ServiceMgrFactCollector.is_systemd_managed_offline
    assert ServiceMgrFactCollector.is_systemd_managed_offline == ServiceMgrFactCollector.is_systemd_managed_offline

# Generated at 2022-06-13 03:24:47.661868
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    from ansible.module_utils.facts.collector import ServiceMgrFactCollector

    class FakeModule:
        def get_bin_path(self, _):
            return True

    module = FakeModule()
    smfc = ServiceMgrFactCollector()

    assert not smfc.is_systemd_managed_offline(module=module)
    os.symlink('systemd', '/sbin/init')
    assert smfc.is_systemd_managed_offline(module=module)
    os.remove('/sbin/init')
    assert not smfc.is_systemd_managed_offline(module=module)

# Generated at 2022-06-13 03:24:59.946735
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    """Test the method ServiceMgrFactCollector.collect."""
    platform_system = platform.system()
    collector_instance = ServiceMgrFactCollector()

    printed_facts = {}
    if platform_system == 'Linux':
        printed_facts['ansible_distribution'] = 'MacOSX'
        assert collector_instance.collect(collected_facts=printed_facts) == {'service_mgr': 'launchd'}

        printed_facts['ansible_distribution'] = 'OpenWrt'
        assert collector_instance.collect(collected_facts=printed_facts) == {'service_mgr': 'openwrt_init'}

        printed_facts['ansible_distribution'] = 'Fedora'

# Generated at 2022-06-13 03:25:09.023339
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts.collector import Collector

    # Setup a fake class to allow testing
    class FakeModule():
        def get_bin_path(self, arg):
            # Return 'systemctl' for all arg values
            return '/usr/bin/systemctl'

    class_instance = ServiceMgrFactCollector()
    method_to_test = class_instance.is_systemd_managed

    # Setup temporary path
    import tempfile
    temp_path = tempfile.mkdtemp()

    # Mapping of name of canary to expected return value

# Generated at 2022-06-13 03:25:18.922678
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    class ModuleStub(object):
        def __init__(self):
            self.params = {}
        def get_bin_path(self, binary):
            if binary == 'systemctl':
                return '/usr/bin/systemctl'
            else:
                return None

    moduleStub = ModuleStub()
    if os.path.islink('/sbin/init') and os.path.basename(os.readlink('/sbin/init')) == 'systemd':
        service_mgr_name = True
    else:
        service_mgr_name = False

    assert(ServiceMgrFactCollector.is_systemd_managed_offline(moduleStub) == service_mgr_name)

# Generated at 2022-06-13 03:25:20.536678
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    assert not ServiceMgrFactCollector.is_systemd_managed(None)


# Generated at 2022-06-13 03:25:27.141259
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    from ansible.module_utils.facts import ModuleFacts
    from ansible.module_utils.facts.collector import collector_module

    fact_collector = collector_module['service']
    module_fact = ModuleFacts(module='')
    result = fact_collector.collect(module_fact)

    assert result['service_mgr']

# Generated at 2022-06-13 03:25:37.479570
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    class FakeModule:
        def __init__(self):
            self.run_command = None

        def get_bin_path(self, command):
            if command == 'systemctl':
                return 'true'
            return None

    # test case #1: No run_command
    module = FakeModule()
    module.run_command = None
    res = ServiceMgrFactCollector.is_systemd_managed(module)
    assert not res

    # test case #2: systemd init detected
    module = FakeModule()
    module.run_command = lambda x: [0, 'systemd', '']
    res = ServiceMgrFactCollector.is_systemd_managed(module)
    assert res

    # test case #3: other init detected
    module = FakeModule()

# Generated at 2022-06-13 03:25:42.747426
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    module = AnsibleModuleMock()
    ServiceMgrFactCollector.is_systemd_managed_offline(module)
    if module.get_bin_path.assert_called_once_with('systemctl') != 1:
        raise AssertionError('unexpected module.get_bin_path() call count')

# Generated at 2022-06-13 03:25:51.447926
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():

    # Create an instance of the ServiceMgrFactCollector class
    service_mgr_fact_collector = ServiceMgrFactCollector()

    class MockModule:
        def get_bin_path(self, name):
            return None

        def run_command(self, command, use_unsafe_shell=False):
            return (1, '', '')

    # Create a mock module
    module = MockModule()

    # Create a dictionary that could be a result of calling
    # ServiceMgrFactCollector.collect()
    collected_facts = {
        'ansible_distribution': 'MacOSX',
    }

    # run collect()
    result = service_mgr_fact_collector.collect(module=module, collected_facts=collected_facts)

    # assert that collected fact has the expected value
    assert result

# Generated at 2022-06-13 03:26:01.000532
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    import mock

    class MockModule(object):
        def __init__(self):
            self.params = dict()
            self.exit_json = dict()
            self.exit_json['ansible_facts'] = dict()

        def run_command(self, cmd, check_rc=True, close_fds=True, executable=None, data=None, binary_data=False, path_prefix=None, cwd=None, use_unsafe_shell=False):
            return (0, 'systemd\n', '')

        def get_bin_path(self, command, opt_dirs=[]):
            return '/usr/bin/systemctl'

    module = MockModule()
    ServiceMgrFactCollector.is_systemd_managed = mock.Mock(return_value=True)
    ServiceMgrFactCollector

# Generated at 2022-06-13 03:26:37.756832
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():

    # To create a MockModule, we need to import it first
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import service_mgr
    import os
    
    # create a MockModule object
    module_obj = AnsibleModule(argument_spec={})
    module_obj.get_bin_path = lambda *args, **kwargs: '/bin/true'

    # test_cases is a list of dict with the following keys:
    #  - desc: description of the test case
    #  - input_args: args to be passed to the test method
    #  - input_kwargs: kwargs to be passed to the test method
    #  - expected_result: expected result of the

# Generated at 2022-06-13 03:26:48.323372
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    import unittest
    import tempfile

    class TestServiceMgrFactCollector(unittest.TestCase):
        def setUp(self):
            from ansible.module_utils.facts.collector.service_mgr import ServiceMgrFactCollector
            self.x = ServiceMgrFactCollector()

        def tearDown(self):
            pass

        def test_ServiceMgrFactCollector_is_systemd_managed(self):
            tmpdir = tempfile.mkdtemp()
            import ansible.module_utils.basic
            m = ansible.module_utils.basic.AnsibleModule(
                argument_spec=dict(),
                supports_check_mode=True
            )
            m.get_bin_path = lambda x: x

# Generated at 2022-06-13 03:26:55.448772
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    import sys
    import tempfile
    # Creation of a temporary directory using the tempfile module
    temporary_directory = tempfile.TemporaryDirectory()
    # Retrieving the name of the temp directory to emulate the installation of systemd
    temporary_directory_name = temporary_directory.name
    sys.path.insert(0, temporary_directory_name)
    # Creation of a fake /sbin/init file
    temporary_init_file = os.path.join(temporary_directory_name, "sbin", "init")

    # Creation of a fake systemctl file
    temporary_systemctl_file = os.path.join(temporary_directory_name, "systemctl")
    with open(temporary_systemctl_file, "w") as f:
        f.write("")

    # Creation of a fake proc_1_init file
    temporary

# Generated at 2022-06-13 03:27:05.878006
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    import ansible.module_utils.facts.collectors.service_mgr
    import ansible.module_utils.facts.collector

    class MockModule(object):

        def __init__(self, bin_path):
            self.bin_path = bin_path

        def get_bin_path(self, command):
            return self.bin_path

    # No 'systemctl' binary, should return False
    module = MockModule(None)
    assert not ansible.module_utils.facts.collectors.service_mgr.ServiceMgrFactCollector.is_systemd_managed_offline(module)

    # 'systemctl' binary, but init not a symlink to systemd, should return False
    module = MockModule('/usr/bin/systemctl')
    assert not ansible.module_utils.facts.collectors

# Generated at 2022-06-13 03:27:10.920187
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    """Test the method is_systemd_managed of class ServiceMgrFactCollector."""

    from ansible.module_utils.basic import AnsibleModule

    class TestModule:
        def __init__(self, path=None):
            self.name = 'Test'
            self.path = path

        def get_bin_path(self, name=None, opt_dirs=None):
            return self.path

    # Test A: systemctl is installed, /run/systemd/system/ exists
    module = TestModule(path='/usr/bin/systemctl')
    collector = ServiceMgrFactCollector()
    assert collector.is_systemd_managed(module=module)

    # Test B: systemctl is installed, /run/systemd/system/ doesn't exist

# Generated at 2022-06-13 03:27:12.733682
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    assert ServiceMgrFactCollector.is_systemd_managed_offline(module) == True

# Generated at 2022-06-13 03:27:23.725563
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    def get_bin_path_side_effect(prog):
        if prog == 'systemctl':
            return True
        return False
    m = Mock(spec_set=AnsibleModule)
    m.get_bin_path = Mock(side_effect=get_bin_path_side_effect)
    s = ServiceMgrFactCollector()
    assert s.is_systemd_managed(m) == True

    def get_bin_path_side_effect(prog):
        return False
    m = Mock(spec_set=AnsibleModule)
    m.get_bin_path = Mock(side_effect=get_bin_path_side_effect)
    s = ServiceMgrFactCollector()
    assert s.is_systemd_managed(m) == False


# Generated at 2022-06-13 03:27:31.842149
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts import ModuleUtilsLegacyFactCollector

    module = ModuleUtilsLegacyFactCollector()
    instance = ServiceMgrFactCollector()

    # Negativ test: method returns False if systemd commandline tools are not available
    assert not instance.is_systemd_managed(module)

    # Positiv test: method returns True if systemd commandline tools are available
    module.run_command = lambda command, **_: (0, '', '')
    assert instance.is_systemd_managed(module)

    # Negativ test: method returns False if any of the canaries doesn't exists
    module.run_command = lambda command, **_: (0, '', '')

# Generated at 2022-06-13 03:27:43.142543
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    class FakeModule(object):
        def get_bin_path(self, name):
            if name == 'systemctl':
                return '/bin/systemctl'
            return None

    SMFC = ServiceMgrFactCollector()

    module = FakeModule()
    SMFC.collector['platform']['system'] = 'SunOS'
    assert not SMFC.is_systemd_managed(module=module)

    SMFC.collector['platform']['system'] = 'Linux'
    SMFC.collector['platform']['distribution'] = 'RedHat'
    assert not SMFC.is_systemd_managed(module=module)

    SMFC.collector['platform']['system'] = 'Linux'
    SMFC.collector['platform']['distribution'] = 'FreeBSD'

# Generated at 2022-06-13 03:27:48.183220
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts.utils import FactsModuleMock
    from ansible.module_utils.facts.collector.service_mgr import ServiceMgrFactCollector

    # Setup and run the test
    module = FactsModuleMock()
    results = ServiceMgrFactCollector.is_systemd_managed(module)

    assert results


# Generated at 2022-06-13 03:29:14.483839
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    module = FakeModule({})

    # check if method is_systemd_managed returns true when given existent file as parameter
    def is_systemd_managed_true(module):
        return True

    # check if method is_systemd_managed returns false when given existent file as parameter
    def is_systemd_managed_false(module):
        return False

    # check if method is_systemd_managed_offline returns true when given existent file as parameter
    def is_systemd_managed_offline_true(module):
        return True

    # check if method is_systemd_managed_offline returns false when given existent file as parameter
    def is_systemd_managed_offline_false(module):
        return False

    # check if method get_bin_path of module returns None when given not installed executable as parameter
   

# Generated at 2022-06-13 03:29:21.818580
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    import ansible.module_utils.facts.collectors.service_mgr

    # Method is_systemd_managed_offline should return False
    # when /sbin/init is not a symlink and it doesn't contain systemd in its name
    os.symlink('init', '/tmp/init')
    assert not ansible.module_utils.facts.collectors.service_mgr.ServiceMgrFactCollector.is_systemd_managed_offline(None)
    os.remove('/tmp/init')

    # Method is_systemd_managed_offline should return False
    # when /sbin/init is not a symlink and it doesn't contain systemd in its name
    os.symlink('init', '/tmp/systemd')
    assert not ansible.module_utils.facts.collectors.service_m

# Generated at 2022-06-13 03:29:25.625273
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    # Unit test for a specific method
    # The name of the method is generated automatically by prepending `test_` prefix to the original method name
    assert ServiceMgrFactCollector.is_systemd_managed_offline(None) is False

# Generated at 2022-06-13 03:29:32.447144
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    # Create a Mock module for use with testing
    class MockModule(object):
        def __init__(self):
            self.params = {'systemctl':None}
        def get_bin_path(self, binary):
            return self.params[binary]

    # Create a Mock module for use with testing
    module = MockModule()

    # Test proper systemctl file
    module.params['systemctl'] = '/usr/bin/systemctl'
    for canary in ["/run/systemd/system/", "/dev/.run/systemd/", "/dev/.systemd/"]:
        assert ServiceMgrFactCollector.is_systemd_managed(module)
    module.params['systemctl'] = '/usr/bin/systemctl.FALSE'

    # Test non-systemd system

# Generated at 2022-06-13 03:29:42.773747
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    import sys
    from ansible.module_utils._text import to_bytes
    if sys.version_info[0] > 2:
        from io import StringIO
    else:
        from StringIO import StringIO
    from ansible.module_utils.facts.collectors import which
    from ansible.module_utils.facts.collectors.system.service_mgr import ServiceMgrFactCollector

    TEST_SHORTNAME = 'test'
    TEST_EXECUTABLE = '/temp/bin/{0}'.format(TEST_SHORTNAME)
    TEST_SYMLINK = '/sbin/init'
    TEST_TARGET = 'systemd'
    TEST_SYSTEMD_PATH = '/tmp/systemd'

# Generated at 2022-06-13 03:29:52.548696
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    class Mock(object):
        def __init__(self, module=None, collected_facts=None):
            self.module = module
            self.collected_facts = collected_facts
        def get_bin_path(self, name):
            if name == 'systemctl' or name == 'initctl':
                return name
            else:
                return None
        def run_command(self, name, use_unsafe_shell=True):
            if name == 'ps -p 1 -o comm|tail -n 1':
                return 0, name, None

    service_mgr_fact_collector = ServiceMgrFactCollector()

    def is_systemd_managed(module):
        return True
    service_mgr_fact_collector.is_systemd_managed = is_systemd_managed


# Generated at 2022-06-13 03:29:55.752946
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():

    test = ServiceMgrFactCollector()
    assert test.is_systemd_managed_offline() == False

# Generated at 2022-06-13 03:30:05.290202
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    import tempfile
    import shutil

    import pytest

    from ansible.module_utils.facts.control.service_mgr_fact import ServiceMgrFactCollector

    temp_dir = tempfile.mkdtemp()
    systemd_path = os.path.join(temp_dir, 'systemd')
    systemctl_path = os.path.join(temp_dir, 'systemctl')


# Generated at 2022-06-13 03:30:15.338191
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    class Module(object):
        @staticmethod
        def get_bin_path(command):
            if command == 'systemctl':
                return '/bin/systemctl'
            else:
                return None

    assert not ServiceMgrFactCollector.is_systemd_managed_offline(Module())

    class Module(object):
        @staticmethod
        def get_bin_path(command):
            if command == 'systemctl':
                return '/bin/systemctl'
            else:
                return None

    os.symlink('/usr/bin/systemd', '/sbin/init')
    assert ServiceMgrFactCollector.is_systemd_managed_offline(Module())

# Generated at 2022-06-13 03:30:21.958619
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    """Test method is_systemd_managed_offline of class ServiceMgrFactCollector.
    """
    # Both systemctl and init are systemd
    class FakeModule:
        def __init__(self):
            self.find_executable_mock_return_value = "/usr/bin/systemctl"
            self.check_output_mock_return_value = "systemd"
        def get_bin_path(self, executable):
            return self.find_executable_mock_return_value
        def run_command(self, command, use_unsafe_shell=True):
            return (0, self.check_output_mock_return_value)
    module = FakeModule()
    assert ServiceMgrFactCollector.is_systemd_managed_offline(module) is True

    # systemctl is systemd