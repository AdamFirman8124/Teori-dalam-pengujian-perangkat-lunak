

# Generated at 2022-06-13 03:23:16.398221
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collectors import ServiceMgrFactCollector

    module = AnsibleModuleTest('service_mgr')
    # Mock module
    module.get_bin_path = lambda x: '/bin/systemctl' if x == 'systemctl' else None
    module.run_command = lambda x, use_unsafe_shell=False: os.system(to_bytes(x)) == 0

    assert ServiceMgrFactCollector.is_systemd_managed(module=module)


# Generated at 2022-06-13 03:23:25.514250
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    import ansible.module_utils.facts.fact_collector

    # Create a fake module, and a fake module_util.
    # While we are at it, create some fake directories as well.
    class FakeModule:
        def __init__(self):
            self.run_command_rc = 0
            self.run_command_stdout = ""
            self.run_command_stderr = ""

        def get_bin_path(self, _):
            return None

        def run_command(self, _, use_unsafe_shell=False):
            return [self.run_command_rc, self.run_command_stdout, self.run_command_stderr]

    class FakeModuleUtil:
        def get_platform(self):
            return 'Linux'


# Generated at 2022-06-13 03:23:31.703886
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts.collector import MockModule
    from ansible.module_utils.facts.collector import MockFile
    from ansible.module_utils.facts.collector import MockCommand
    from ansible.module_utils.facts.service_mgr import ServiceMgrFactCollector

    # Create mock directory structure
    mock_file_dict = {'/run/systemd/system/': MockFile(),
                      '/dev/.run/systemd/': MockFile(),
                      '/dev/.systemd/': MockFile()}

    mock_module = MockModule(file_dict=mock_file_dict, command_dict={})

    assert True == ServiceMgrFactCollector.is_systemd_managed(mock_module)

# Generated at 2022-06-13 03:23:44.416978
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    class ModuleStub:
        def get_bin_path(self, app):
            if app == "systemctl":
                return "/bin/systemctl"
            else:
                return None

    # Stub out os.path
    class FakeOsPath:
        def islink(path):
            if path == "/sbin/init":
                return True
            else:
                return False

        def readlink(path):
            if path == "/sbin/init":
                return "systemd"
            else:
                return None

    os.path = FakeOsPath()

    # Stub out platform
    platform.system = lambda: "Linux"

    # Create a instance of class ServiceMgrFactCollector
    s = ServiceMgrFactCollector()

    # Make a call to the method is_systemd_managed_offline of class ServiceM

# Generated at 2022-06-13 03:23:55.515878
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    from ansible.module_utils.facts.collector.service_mgr import ServiceMgrFactCollector

    class MockModule(object):
        def get_bin_path(self, arg):
            return arg

        def run_command(self, arg):
            return None

    class MockCollectedFacts(object):
        def __init__(self):
            self.ansible_distribution = None
            self.ansible_system = None

    instance = MockModule()
    proc_1_map = {
        'procd': 'openwrt_init',
        'runit-init': 'runit',
        'svscan': 'svc',
        'openrc-init': 'openrc',
    }

    # On Linux, with is_systemd_managed defined and true
    facts = MockCollectedFacts()


# Generated at 2022-06-13 03:23:58.041541
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    assert ServiceMgrFactCollector.is_systemd_managed_offline(None) == False

# Generated at 2022-06-13 03:24:08.411165
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():

    # Mock class for module_utils.facts.utils.get_file_content
    class GetFileContentMock(object):

        # Mock for get_file_content
        #
        # Return value of this mock can be configured using 'result' attribute
        def __call__(self, filename):
            return self.result

    # Mock class for module_utils.facts.collector.BaseFactCollector
    class BaseFactCollectorMock(object):

        # Mock for method get_file_content
        def get_file_content(self, filename):
            return get_file_content_mock(filename)

    # Mock class for module_utils.facts.collector.BaseFactCollector.run_command

# Generated at 2022-06-13 03:24:16.906647
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    module = basic.AnsibleModule(argument_spec={})
    module.run_command = Mock(return_value=(0, 'init', ''))
    module.get_bin_path = Mock(return_value='/bin/systemctl')
    module.exit_json = Mock()
    module.fail_json = Mock()

    with patch.dict('os.path.exists.__dict__', {'/sbin/init': lambda: True}):
        with patch.object(ServiceMgrFactCollector, 'is_systemd_managed') as mock_is_systemd_managed:
            mock_is_systemd_managed.return_value = True

# Generated at 2022-06-13 03:24:20.804598
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts.collector.service_mgr import ServiceMgrFactCollector
    from ansible.module_utils.facts.utils import FactsFiles

    fake_module = FactsFiles({})
    smfc = ServiceMgrFactCollector()
    assert not smfc.is_systemd_managed(fake_module)


# Generated at 2022-06-13 03:24:31.433321
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    class MockModule(object):
        def __init__(self, ret_commands, ret_files):
            self.commands = ret_commands
            self.files = ret_files

        def get_bin_path(self, command):
            assert command in self.commands
            return self.commands[command]

        def run_command(self, command, use_unsafe_shell=False):
            # we don't actually run this command
            assert use_unsafe_shell
            output = 'ps command output'
            assert output in self.commands[command]
            return (0, output, None)

        def exists(self, path):
            return path in self.files

        def islink(self, path):
            return path in self.files


# Generated at 2022-06-13 03:24:52.675753
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    # Initialize a mock module and a mock set of collected facts
    module = AnsibleModuleMock()
    collected_facts = {}

    # Pre-setup mock conditions for supported service managers
    service_mgr_facts = {
        'service_mgr': None
    }

    # Pre-setup mock conditions for service managers that are not supported
    not_supported_facts = {
        'service_mgr': None
    }

    # Initialize a instance of ServiceMgrFactCollector
    service_mgr_collector = ServiceMgrFactCollector()
    service_mgr_collector.required_facts = set(['platform'])

    # Setup mock conditions
    # Mock condition: Service manager is runit
    service_mgr_facts['ansible_system'] = 'Linux'

# Generated at 2022-06-13 03:25:00.856574
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    module = MockModule()
    collector = ServiceMgrFactCollector()

    assert not collector.is_systemd_managed_offline(module)

    module.run_command.return_value = 0, "/sbin/systemd", ""

    assert collector.is_systemd_managed_offline(module)

    module.run_command.return_value = 0, "/sbin/init", ""

    assert not collector.is_systemd_managed_offline(module)


# Generated at 2022-06-13 03:25:09.613157
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    class FakeModule:
        def get_bin_path(self, prog):
            return prog

    #test case with systemctl and /sbin/init not symlinked
    MockedServiceMgrFactCollector = ServiceMgrFactCollector()
    FakeModule.run_command = lambda self, command: (0, '', '')
    assert not MockedServiceMgrFactCollector.is_systemd_managed_offline(FakeModule())

    #test case with systemctl and /sbin/init symlinked
    MockedServiceMgrFactCollector = ServiceMgrFactCollector()
    FakeModule.run_command = lambda self, command: (0, 'systemd', '')
    FakeModule.os_path_exists = lambda self, path: True

# Generated at 2022-06-13 03:25:13.178449
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    """
    Test ServiceMgrFactCollector.collect()
    """
    # ServiceMgrFactCollector.collect() is task-specific and will not be auto-tested.
    pass

# Generated at 2022-06-13 03:25:22.297580
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    import json

    class EmptyModule(object):
        def __init__(self, params):
            self.params = params

    class FakeModule(EmptyModule):
        def fail_json(self, msg, **kwargs):
            raise ValueError(msg)


# Generated at 2022-06-13 03:25:34.192215
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():

    # Mock object to use with patched service_mgr, import of AnsibleModule fails on Python 2.6
    class MockAnsibleModule(object):

        def __init__(self):
            self.params = dict()

        def get_bin_path(self, prog):
            return '/bin/systemctl'

        def run_command(self, cmd, use_unsafe_shell=True):
            raise NotImplementedError()

    service_mgr = ServiceMgrFactCollector()

    for path in ['/sbin/init', '/sbin/init.backup']:
        # Use a symbolic link named init
        os.symlink('/usr/lib/systemd/systemd', path)
        assert(service_mgr.is_systemd_managed_offline(MockAnsibleModule()))
        #

# Generated at 2022-06-13 03:25:42.332339
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    class MockModule(object):
        def get_bin_path(self, command):
            if command == 'systemctl':
                return '/bin/systemctl'

    module = MockModule()
    collector = ServiceMgrFactCollector()

    # Negative test
    collector.is_systemd_managed_offline(module)
    assert not collector.is_systemd_managed_offline(None)

    # Positive test
    os.symlink('systemd', '/sbin/init')
    assert collector.is_systemd_managed_offline(module)
    os.remove('/sbin/init')

# Generated at 2022-06-13 03:25:51.247633
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    '''
    This function tests ServiceMgrFactCollector.collect function
    '''
    from ansible.module_utils.facts.utils import ModuleBase
    import ansible.module_utils.facts.system.service_mgr

    test_result = {
        'ansible_distribution': 'OpenWrt',
        'ansible_distribution_version': 'Barrier Breaker',
        'ansible_distribution_release': 'r39192',
        'ansible_system': 'Linux',
        'ansible_machine': 'mvebu',
        'ansible_architecture': 'armv7l',
        }

    # Setup test module
    module = ModuleBase(argument_spec=dict())
    module.run_command = lambda args, use_unsafe_shell=False: (0, '', '')
   

# Generated at 2022-06-13 03:26:00.999609
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    """Test case to verify the method is_systemd_managed_offline of the class ServiceMgrFactCollector is working as expected."""

    # The mocked module_util_paths should include the bin paths for systemctl and readlink.
    # See https://github.com/ansible/ansible/pull/48297 for more information.

# Generated at 2022-06-13 03:26:09.990781
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts.collector import collector_registry
    from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector

    # Create fake module
    class FakeModule:
        def get_bin_path(self, name):
            return 'systemctl'
    fake_module = FakeModule()

    # Remove the registered collectors
    collector_registry.clear()

    # Check with canaries for systemd
    for canary in ["/run/systemd/system/", "/dev/.run/systemd/", "/dev/.systemd/"]:
        open(canary, 'w').close()
        assert ServiceMgrFactCollector.is_systemd_managed(fake_module)
        os.remove(canary)

    # Check without canaries for systemd

# Generated at 2022-06-13 03:26:50.191213
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    import ansible.module_utils.facts.collector
    module_name = "ansible.module_utils.facts.collector"
    module = __import__(module_name, fromlist=['ansible.module_utils.facts.collector'])
    module.FACTS = {}
    service_mgr_fact_collector = getattr(module, "ServiceMgrFactCollector")
    service_mgr_fact_collector.is_systemd_managed_offline = module.ServiceMgrFactCollector.is_systemd_managed_offline
    module.FACTS = {
        'ansible_system': 'Linux',
        'ansible_service_mgr': '',
    }
    service_mgr_fact_collector.is_systemd_managed_offline = module.ServiceMgrFact

# Generated at 2022-06-13 03:27:00.226489
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.utils import NormalizedFactCache
    from ansible.module_utils.six import PY3
    from ansible.module_utils.common._collections_compat import Mapping

    # Arrange
    if PY3:
        from unittest import mock
        import builtins
        MOCK_MODULE = mock.MagicMock(builtins)
    else:
        import __builtin__ as builtins
        import mock
        MOCK_MODULE = mock.MagicMock(builtins)

    mock_module = mock.MagicMock()

# Generated at 2022-06-13 03:27:07.981309
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector

# Generated at 2022-06-13 03:27:19.179776
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    # Define the files to be read and the content they will *normally*
    # contain.
    files_to_read = {
        '/proc/1/comm': 'systemd\n',
        '/sbin/init': '../lib/systemd/systemd',
    }

    # Define the file contents to use when mocking the contents of
    # the files listed above.
    # An empty file_contents dictionary will cause the
    # mock_open.return_value.__iter__ to raise a StopIteration
    # exception.  In this case the file_utils.read_file_from_filesystem function
    # will return None.
    # A non-empty file_contents dictionary will cause the
    # mock_open.return_value.__iter__ to return the contents of the file
    # indexed by the name of the

# Generated at 2022-06-13 03:27:28.886915
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    # Mock module
    module = MockModule()

    # If a tool has been found, the method will return True
    module.get_bin_path = Mock(return_value='tool_path')

    # If the module's run_command method returns a status code of 0 and
    # a command string (first word) of ssh, the method returns True.
    module.run_command = Mock(return_value=(0, 'systemctl'))

    # Call the method
    result = ServiceMgrFactCollector.is_systemd_managed(module)

    # Check if the result is what is expected
    assert result



# Generated at 2022-06-13 03:27:39.882389
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    class MockModule(object):
        def __init__(self):
            self.run_command_map = {}

        def get_bin_path(self, arg):
            return "/path/to/" + arg

        def run_command(self, arg, use_unsafe_shell=None):
            if self.run_command_map:
                return self.run_command_map[arg]
            return 0, "", ""
    smfc = ServiceMgrFactCollector()
    f = open("systemctl", "w")
    f.close()
    module = MockModule()
    module.run_command_map = {
            'systemctl list-unit-files': (0, "openrc-init.service enabled\n", ""),
    }
    assert smfc.is_systemd_managed(module=module)
   

# Generated at 2022-06-13 03:27:44.053967
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    class Module():
        def get_bin_path(self, binary):
            return '/usr/bin/' + binary
    module = Module()
    sm = ServiceMgrFactCollector()
    assert sm.is_systemd_managed_offline(module) == True

# Generated at 2022-06-13 03:27:49.891148
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    from ansible.module_utils.facts.collector import MockModule
    m = MockModule(
        module_args='',
        ansible_facts={
            'ansible_distribution': 'CentOS',
            'ansible_system': 'Linux',
        },
    )
    svc_mgr_fc = ServiceMgrFactCollector(m)
    facts = svc_mgr_fc.collect(m)
    assert facts['service_mgr'] == 'systemd'

# Generated at 2022-06-13 03:27:56.165786
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts.collectors.service_mgr import ServiceMgrFactCollector
    from ansible.module_utils.six import with_metaclass

    # Need to inherit from object class otherwise the test code of Ansible will not recognize
    # this as a class
    class TestClass(with_metaclass(ServiceMgrFactCollector)):
        """TestClass"""
    # Supply dummy module so that the method can be executed
    module = object()

    # Mock get_bin_path to return None (no systemctl binary is found)
    def mock_get_bin_path(binary):
        if binary == 'systemctl':
            return None
    module.get_bin_path = mock_get_bin_path
    assert not TestClass.is_systemd_managed(module=module)

    # Mock get

# Generated at 2022-06-13 03:28:07.654805
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    module_mock = AnsibleModuleMock()
    service_mgr_fact_collector_instance = ServiceMgrFactCollector()

    # case 1: systemctl is not installed
    module_mock.set_bin_path('systemctl', None)
    assert not service_mgr_fact_collector_instance.is_systemd_managed_offline(module_mock)

    # case 2: systemctl is installed, but /sbin/init is not a symlink
    module_mock.set_bin_path('systemctl', '/usr/bin/systemctl')
    service_mgr_fact_collector_instance.is_systemd_managed_offline(module_mock)
    os.symlink = lambda x, y: None

# Generated at 2022-06-13 03:29:45.844836
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    import sys
    import platform
    py_version = sys.version_info[0]

    # setup module args
    module_args = dict(
        ansible_distribution='Linux',
        ansible_distribution_version='7.2',
        ansible_distribution_release='1511',
        ansible_distribution_file_parsed=False,
        ansible_sysvinit_has_enabled=True,
    )

    class mock_module1(object):
        # Mock class for cyclical import
        def __init__(self, module_params):
            self.params = module_params
            self.run_command_environ_update = {}
            self.run_command_stdout = True
            self.get_bin_path_return_value = '/usr/bin/systemctl'


# Generated at 2022-06-13 03:29:54.164180
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    kw_args = {'use_unsafe_shell': True, 'module': None}

    # Ensure is_systemd_managed_offline returns False if /sbin/init not a symlink
    fake_os_path_islink_true = os.path.islink
    def fake_os_path_islink_false(*args, **kwargs):
        return False

    os.path.islink = fake_os_path_islink_false
    assert ServiceMgrFactCollector.is_systemd_managed_offline(module=None) == False
    os.path.islink = fake_os_path_islink_true

    # Ensure is_systemd_managed_offline returns False if /sbin/init is a symlink (to a file)

# Generated at 2022-06-13 03:29:59.189384
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    sample_systemctl_output = {
        'stdout': [
            'systemctl',
            '--failed'
        ]
    }

    class MockServiceMgrFactCollector:
        @staticmethod
        def is_systemd_managed(module):
            return True

    class MockModule:
        def get_bin_path(self, executable):
            return 'systemctl'

        def run_command(self):
            return sample_systemctl_output

    mockModule = MockModule()
    mockServiceMgrFactCollector = MockServiceMgrFactCollector()

    assert ServiceMgrFactCollector.is_systemd_managed(mockModule)
    assert mockServiceMgrFactCollector.is_systemd_managed(mockModule)


# Generated at 2022-06-13 03:30:06.676139
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    import ansible.module_utils.facts.facts as ansible_facts
    # Mock module and facts submodule
    module_mock = type('module', (object,), {})()
    module_mock.exit_json = lambda x: None
    module_mgr_mock = type('ansible_facts.service_mgr', (), {})()
    setattr(module_mock, '_ansible_facts', {'ansible_facts': {}})

    # Mock BaseFactCollector module and its methods and attributes
    base_fact_collector_mock = type('BaseFactCollector', (object,), {})()
    base_fact_collector_mock.required_facts = set(['platform', 'distribution'])
    base_fact_collector_mock.is_systemd_managed = ServiceM

# Generated at 2022-06-13 03:30:17.240861
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    # Mock AnsibleModule
    from ansible.module_utils.facts import ModuleFacts
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.utils import get_file_content

    mock_ansible_module = ModuleFacts(BaseFactCollector)

    # Mock setup of class ServiceMgrFactCollector
    mock_ServiceMgrFactCollector = ServiceMgrFactCollector()

    # Mock test method of class ServiceMgrFactCollector
    mock_ansible_module.run_command = {'rc': 0, 'ps': 'init', 'err': ''}
    mock_get_file_content = None

    # Method tested: collect
    assert mock_ServiceMgrFactCollector.collect() == {'service_mgr': 'sysvinit'}

# Generated at 2022-06-13 03:30:19.486774
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    # Facts['service_mgr'] == 'service' and Facts['service_mgr'] == 'systemd' should be covered
    # by their respective unit tests in common/test_linux.py and service/test_systemd.py.
    pass

# Generated at 2022-06-13 03:30:28.610643
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    # pylint: disable=import-error
    from ansible.module_utils.facts.collector.service_mgr import ServiceMgrFactCollector

    # Unit test for method is_systemd_managed of class ServiceMgrFactCollector
    def get_bin_path(path):
        return path

    assert False == ServiceMgrFactCollector.is_systemd_managed(module=AnsibleModuleMock(get_bin_path=get_bin_path))

    assert True == ServiceMgrFactCollector.is_systemd_managed(module=AnsibleModuleMock(get_bin_path=get_bin_path, systemd=True))


# Generated at 2022-06-13 03:30:34.572775
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    # In case of absence of systemd-sysvinit package on SUSE,
    # there is no way to know if it is systemd managed or not.
    class TestModule:
        def get_bin_path(self, bin_path):
            pass
    test_module = TestModule()
    service_mgr = ServiceMgrFactCollector()
    assert service_mgr.is_systemd_managed_offline(test_module) is False

# Generated at 2022-06-13 03:30:39.995693
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    c = ServiceMgrFactCollector()
    # create fake module for test
    class Module:
        def __init__(self):
            self.params = {}

        def get_bin_path(self, executable):
            return None

    module = Module()

    # case of systemctl
    def run_command_mock_1(cmd, use_unsafe_shell=False):
        return 0, 'systemd\n', ''
    module.run_command = run_command_mock_1
    result = c.collect(module)
    assert result['service_mgr'] == 'systemd'

    # case of ps
    def run_command_mock_2(cmd, use_unsafe_shell=False):
        return 0, 'runit\n', ''
    module.run_command = run_command_m

# Generated at 2022-06-13 03:30:49.314438
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    import sys
    import tempfile

    class MockModule(object):
        def __init__(self):
            self.run_command = Mock()
            self.fail_json = Mock()
            self.get_bin_path = Mock()
            self.run_command.return_value = (0, '', '')
            self.get_bin_path.return_value = '/bin/systemctl'

    # Test with not existing path to systemctl
    mod = MockModule()
    mod.get_bin_path.return_value = None
    assert ServiceMgrFactCollector.is_systemd_managed(mod) == False

    # Test with existing path to systemctl
    mod = MockModule()
    mod.get_bin_path.return_value = '/bin/systemctl'

    # Test with existing /run/systemd/