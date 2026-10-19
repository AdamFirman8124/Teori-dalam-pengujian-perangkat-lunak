

# Generated at 2022-06-13 03:23:08.180697
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    class MockModule:
        def get_bin_path(self, *args):
            return '/bin/ls'
        def run_command(self, *args, **kwargs):
            raise Exception("run_command not implemented")

    from ansible.module_utils.facts import collector
    import os

    for canary in ["/run/systemd/system/", "/dev/.run/systemd/", "/dev/.systemd/"]:
        os.makedirs(canary)
        result = collector.ServiceMgrFactCollector.is_systemd_managed(MockModule())
        if not result:
            raise Exception("is_systemd_managed returns False while {} is present".format(canary))
        os.rmdir(canary)

# Generated at 2022-06-13 03:23:17.891931
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    import tempfile
    import shutil
    import sys
    import os
    import platform
    from ansible.module_utils.facts import ModuleFacts

    class MockAnsibleModule:

        def __init__(self, exit_json, fail_json):
            self.exit_json = exit_json
            self.fail_json = fail_json

        def get_bin_path(self, command):
            return '/usr/bin/systemctl'

        def run_command(self, command, use_unsafe_shell=False):
            return (1, '', '')

    # create a temporary directory
    temp_dir = tempfile.mkdtemp()


# Generated at 2022-06-13 03:23:24.700599
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    # Mock up a module
    class FakeAnsibleModule:

        def get_bin_path(self, command):
            return 'systemctl' if command == 'systemctl' else None

        def run_command(self, command, use_unsafe_shell=False):
            return (0, "", "")

    class FakeSystemdFactCollector(ServiceMgrFactCollector):
        def collect(self, module=None, collected_facts=None):
            return {'service_mgr': 'systemd'}

    class FakeNonSystemdFactCollector(ServiceMgrFactCollector):
        def collect(self, module=None, collected_facts=None):
            return {'service_mgr': 'not_systemd'}

    systemd_fact_collector = FakeSystemdFactCollector()
    non_systemd_fact

# Generated at 2022-06-13 03:23:29.442101
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    """
    Test:
        - Whether the method ServiceMgrFactCollector.is_systemd_managed_offline returns True, if an init is a symlink to systemd.
    """
    class _MockModule(object):
        def get_bin_path(self, executable):
            return executable
    mock_module = _MockModule()
    service_mgr_fact_collector = ServiceMgrFactCollector()
    assert service_mgr_fact_collector.is_systemd_managed_offline(mock_module) == True

# Generated at 2022-06-13 03:23:31.767234
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    m = MockModule()
    f = ServiceMgrFactCollector()
    fact_list = f.collect(m, {})
    assert sorted(fact_list) == ['service_mgr']

# Generated at 2022-06-13 03:23:39.576162
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts.collectors.system.service_mgr import ServiceMgrFactCollector
    class MockModule:
        def get_bin_path(self, executable):
            return '/path/to/file'
    module = MockModule()
    ServiceMgrFactCollector.is_systemd_managed(module)

# Generated at 2022-06-13 03:23:47.245914
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    '''Test is_systemd_managed method of class ServiceMgrFactCollector'''

    # Test the method is_systemd_managed with systemctl present and
    # /run/systemd mounted
    class TestModule():
        def get_bin_path(self, program):
            return program

    module = TestModule()
    os.environ['PATH'] = '/bin:/usr/bin'
    os.environ['MOCK_SYSTEMD_PATH'] = '/run/systemd/'
    smfc = ServiceMgrFactCollector()
    result = smfc.is_systemd_managed(module=module)
    os.unsetenv('MOCK_SYSTEMD_PATH')
    assert result == True

    # Test the method is_systemd_managed with systemctl present and
    # no systemd marker found

# Generated at 2022-06-13 03:23:53.186060
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector

    class Test(BaseFactCollector):
        platform = 'Linux'
        distribution = None
        def get_bin_path(self, name): return name

    class MockModule(object):
        def __init__(self):
            self.collector = Test()

        def get_bin_path(self, name): return name

    module = MockModule()

    assert ServiceMgrFactCollector.is_systemd_managed(module) == False

    module.collector.distribution = 'Fedora'
    module.collector.platform_version = '21'
    assert ServiceMgrFactCollector.is_systemd_managed(module) == True



# Generated at 2022-06-13 03:23:55.028813
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    assert ServiceMgrFactCollector.is_systemd_managed_offline(module=None) == False


# Generated at 2022-06-13 03:24:02.376421
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():

    def run_command(command, use_unsafe_shell=False):
        """Fake implentation of run_command method."""
        if command == "which systemctl":
            return 0, "/usr/bin/systemctl", ""
        if command == "uname -s":
            return 0, "Linux", ""
        return 0, "", ""


# Generated at 2022-06-13 03:24:14.571692
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    assert ServiceMgrFactCollector.is_systemd_managed_offline(None) == False

# Generated at 2022-06-13 03:24:15.387055
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    pass

# Generated at 2022-06-13 03:24:20.897089
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.collector import BaseFileModuleCollector

    class _Module(object):
        def __init__(self, path):
            self._path = path

        def get_bin_path(self, path):
            return path

    class _TestCollector(BaseFileModuleCollector):
        _fact_ids = ['service_mgr']
        _platform = 'Linux'
        _required_files = []

        def __init__(self, module):
            self._module = module

    class _TestModule(object):
        def __init__(self, path):
            self.path = path
            self.collector = _TestCollector(self)


# Generated at 2022-06-13 03:24:31.554563
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():

    # Dummy module and run command method
    module = type('DummyModule', (object,), {})()
    def run_cmd(command, use_unsafe_shell=False): return 123, "something", "something else"
    module.run_command = run_cmd

    if platform.system() == 'SunOS':
        # Dummy get_bin_path method for system executable
        def get_bin_path(executable, required=False):
            return '/bin/' + executable
        module.get_bin_path = get_bin_path

    # Replace ansible_distribution with distribution name
    facts = {'ansible_distribution': 'CentOS'}

    # Create collector
    collector = ServiceMgrFactCollector()

    # Test collection of service manager

# Generated at 2022-06-13 03:24:40.468720
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    class TestModule(object):

        def get_bin_path(self, name):
            return name

    test_obj = ServiceMgrFactCollector()

    module = TestModule()

    # Test 1 - If 'systemctl' is not present in system,
    #          is_systemd_managed should return False
    test_obj.get_bin_path = lambda systemd: None
    assert False == test_obj.is_systemd_managed(module)

    # Test 2 - If 'systemctl' is present in system and
    #          '/run/systemd/system/' exists,
    #          is_systemd_managed should return True
    test_obj.get_bin_path = lambda systemd: systemd
    test_obj.os.path.exists = lambda canary: True
    assert True == test_obj.is_systemd

# Generated at 2022-06-13 03:24:49.274200
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    fact_collector = ServiceMgrFactCollector()
    facts = fact_collector.collect(None, {
        'ansible_distribution': 'OpenWrt',
        'ansible_system': 'Linux',
    })
    assert facts['service_mgr'] == 'openwrt_init'

    fact_collector = ServiceMgrFactCollector()
    facts = fact_collector.collect(None, {
        'ansible_distribution': 'MacOSX',
        'ansible_system': 'Darwin',
    })
    assert facts['service_mgr'] == 'launchd'

    fact_collector = ServiceMgrFactCollector()

# Generated at 2022-06-13 03:25:01.306673
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    def mock_get_bin_path_False(arg):
        return False
    def mock_get_bin_path_True(arg):
        return True
    def mock_os_path_exists_False(arg):
        return False
    def mock_os_path_exists_True(arg):
        return True
    def mock_os_path_islink_True(arg):
        return True
    def mock_os_readlink_systemd(arg):
        return 'systemd'
    def mock_os_readlink_non_systemd(arg):
        return 'init'

    # These tests are designed for a Linux environment.
    # They should be run in other OS environments as well.
    # In the case of this method, we would have to first find out whether the
    # system is managed by systemd.

    #

# Generated at 2022-06-13 03:25:05.532348
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    class MockModule(object):
        def __init__(self):
            self.fail_json = lambda *args, **kwargs: self.fail_json_arguments.append(dict(args=args, kwargs=kwargs))
            self.fail_json_arguments = []
        def get_bin_path(self, name):
            self.get_bin_path_arguments.append(name)
            return True

    class MockOs(object):
        def __init__(self):
            self.path = MockOsPath()
        class MockOsPath(object):
            def __init__(self):
                self.islink_arguments = []
                self.readlink_arguments = []
            def islink(self, path):
                self.islink_arguments.append(path)
                return True
           

# Generated at 2022-06-13 03:25:15.652888
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    import platform
    import os

    class ModuleMock(object):
        def get_bin_path(self, arg):
            return os.path.join(os.path.dirname(__file__), 'systemctl')

    # System state: systemd detected (correct)
    os.system('mkdir -p /run/systemd/system')
    assert ServiceMgrFactCollector.is_systemd_managed(ModuleMock())

    # System state: systemd not detected
    os.system('rm -rf /run/systemd/system')
    assert not ServiceMgrFactCollector.is_systemd_managed(ModuleMock())


# Generated at 2022-06-13 03:25:23.609964
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    from ansible.module_utils.facts.collector.service.service_mgr import ServiceMgrFactCollector
    class FakeModule(object):
        def __init__(self, executable_exists, readlink_returns, islink_returns, exists_returns, path_exists):
            self.executable_exists = executable_exists
            self.readlink_returns = readlink_returns
            self.islink_returns = islink_returns
            self.exists_returns = exists_returns
            self.path_exists = path_exists

        def get_bin_path(self, binary):
            return binary if self.executable_exists else None

        def run_command(self, cmd, use_unsafe_shell=False):
            return 1, None, None

       

# Generated at 2022-06-13 03:25:43.617370
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    # We don't use real module here, so any errors will just be ignored
    class FakeModule:
        def get_bin_path(self, cmd):
            return None
        @staticmethod
        def fail_json(msg):
            raise Exception(msg)
    # Test condition when /sbin/init is not a symlink
    if os.path.islink('/sbin/init'):
        os.unlink('/sbin/init')
    assert not ServiceMgrFactCollector.is_systemd_managed_offline(FakeModule())
    # Test condition when /sbin/init is not pointing to systemd
    if os.path.islink('/sbin/init'):
        os.unlink('/sbin/init')

# Generated at 2022-06-13 03:25:47.837967
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
  tester = ServiceMgrFactCollector()
  class FakeModule():
    def get_bin_path(self, command):
      if command == 'systemctl':
         return '/bin/systemctl'
      else:
         return None
  module = FakeModule()
  assert tester.is_systemd_managed_offline(module) == True

# Generated at 2022-06-13 03:25:54.606276
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts import ModuleFail
    from ansible.module_utils.facts import FallbackModuleFail

    class FakeModule(object):
        def __init__(self):
            self.fail_json = Exception

    class MyClass(BaseFactCollector):
        name = 'test_service_mgr'

        def collect(self, module=None, collected_facts=None):
            return ServiceMgrFactCollector.is_systemd_managed(module)

    test_classes = [
        MyClass(),
    ]

    # test passing a FakeModule

# Generated at 2022-06-13 03:25:58.437638
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    from ansible.module_utils.facts.collector import mock_module
    import platform

    module = mock_module(platform.system())
    collector = ServiceMgrFactCollector(module)
    assert collector.is_systemd_managed_offline(module) is False

# Generated at 2022-06-13 03:26:05.396366
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    """
    Test the is_systemd_managed method of class ServiceMgrFactCollector.
    """
    from ansible.module_utils.facts.collector import DummyModule

    module = DummyModule()
    collector = ServiceMgrFactCollector()

    # Non-systemd system
    module.get_bin_path.return_value = None
    assert not collector.is_systemd_managed(module)

    for canary_test in ["/run/systemd/system/", "/dev/.run/systemd/", "/dev/.systemd/"]:
        module.run_command.return_value = 0, None, None
        assert not collector.is_systemd_managed(module)
        module.run_command.return_value = 0, canary_test, None

# Generated at 2022-06-13 03:26:13.433958
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    import platform

    # Use object of class PlatformLinux to create mock object of factory class
    fake_module = platform.linux_distribution()

    # Mock system version
    fake_module.system = 'Linux'

    # Mock platform release
    fake_module.release = '4.4.0-116-generic'

    # Mock platform
    fake_module.platform = 'Linux-4.4.0-116-generic-x86_64-with-Ubuntu-16.04-xenial'

    # Mock platform mac_ver
    fake_module.mac_ver = ('10.12.6', ('', '', ''), 'x86_64')

    # Mock platform mac_ver
    fake_module.machine = 'x86_64'

    # Mock platform mac_ver
    fake_module.processor = 'x86_64'

# Generated at 2022-06-13 03:26:21.433658
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    # Get the ServiceMgrFactCollector instance
    service_mgr_fact = ServiceMgrFactCollector()
    # Get the AnsibleModule for ServiceMgrFactCollector
    service_mgr_module = None

    service_mgr_module_instance1 = service_mgr_fact.is_systemd_managed(service_mgr_module)
    service_mgr_module_instance2 = service_mgr_fact.is_systemd_managed(service_mgr_module)
    assert service_mgr_module_instance1 == service_mgr_module_instance2

# Generated at 2022-06-13 03:26:28.465553
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    class DummyModule(object):
        def get_bin_path(self, arg):
            return str(arg)

    # create the dummy object to test the method
    test_class = ServiceMgrFactCollector()

    # create a dummy module object
    test_module = DummyModule()

    # create a dummy dict. This dict will be used to pass info to the method
    collected_facts = {}
    collected_facts['ansible_system'] = 'Linux'
    collected_facts['ansible_distribution'] = 'Fedora'

    # check if the system is already in systemd mode
    is_systemd_managed = test_class.is_systemd_managed(module=test_module)

    # the system is not yet in systemd mode. Force it to be in systemd mode by creating the needed symlink

# Generated at 2022-06-13 03:26:35.343148
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():

    class ModuleMock():

        @staticmethod
        def get_bin_path(name):
            return '/bin/' + name

        @staticmethod
        def exists(path):
            if path == '/bin/systemctl':
                return True

            return False

    # testing systemd based detection
    smfc = ServiceMgrFactCollector()
    smfc.is_systemd_managed_offline(ModuleMock())

    ServiceMgrFactCollector.is_systemd_managed_offline(ModuleMock())


# Generated at 2022-06-13 03:26:43.837721
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    class ModuleStub(object):
        def get_bin_path(self, path):
            return path
    # Successful case
    collector = ServiceMgrFactCollector()
    collector._is_systemd_managed = staticmethod(collector.is_systemd_managed)
    assert collector.is_systemd_managed(ModuleStub())
    # Unsuccessful case
    collector._is_systemd_managed = staticmethod(lambda _: False)
    assert not collector.is_systemd_managed(ModuleStub())


# Generated at 2022-06-13 03:27:05.959616
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    
    # Instantiating an object of class ServiceMgrFactCollector
    test_obj = ServiceMgrFactCollector()

    # Testing if the conditions are True
    if test_obj.is_systemd_managed_offline('/sbin/init'):
        print("Test cases are True.")
    else:
        print("Test case are False.")

if __name__ == '__main__':
    test_ServiceMgrFactCollector_is_systemd_managed_offline()

# Generated at 2022-06-13 03:27:13.915503
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    class MockedModule:
        def get_bin_path(self, software):
            return software

    mock_module = MockedModule()

    assert ServiceMgrFactCollector.is_systemd_managed(mock_module) == True
    os.remove("/run/systemd/system")

    assert ServiceMgrFactCollector.is_systemd_managed(mock_module) == False

# Generated at 2022-06-13 03:27:18.048235
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    class TestModule(object):
        def __init__(self, facts_dict=None):
            self.exit_json = lambda x: None
            self.fail_json = lambda x: None
            self.run_command = lambda cmd, use_unsafe_shell=False: ('', '', '')
            self.get_bin_path = lambda cmd: None

        def get_bin_path(self, cmd):
            if cmd == 'systemd-detect-virt':
                return '/bin/systemd-detect-virt'
            elif cmd == 'systemctl':
                return '/bin/systemctl'
            return None

        def run_command(self, cmd, use_unsafe_shell=False):
            return ('', '/bin/systemd-detect-virt', '')


# Generated at 2022-06-13 03:27:29.664229
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():

    class Mock:
        def get_bin_path(self, path):
            return True

        def run_command(self, command):
            return 0, '\n', ''

    sm = ServiceMgrFactCollector()

    assert sm.is_systemd_managed_offline(Mock())

    def mock_get_bin_path(path):
        if path == 'systemctl':
            return None
        else:
            return True

    assert not sm.is_systemd_managed_offline(Mock())

    if os.path.exists('/sbin/init'):
        os.remove('/sbin/init')

    assert not sm.is_systemd_managed_offline(Mock())


# Generated at 2022-06-13 03:27:40.820841
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    # The distutils module is not shipped with SUNWPython on Solaris.
    # It's in the SUNWPython-devel package which also contains development files
    # that don't belong on production boxes.  Since our Solaris code doesn't
    # depend on LooseVersion, do not import it on Solaris.
    if platform.system() != 'SunOS':
        from ansible.module_utils.compat.version import LooseVersion
        from ansible.module_utils.facts import collector

        # Init module_utils.facts.collector.BaseFactCollector
        BaseFactCollector = collector.BaseFactCollector
        BaseFactCollector.__init__()

        # Init module_utils.facts.collector.ServiceMgrFactCollector
        ServiceMgrFactCollector = collector.ServiceMgrFactCollector
        ServiceMgrFactCollect

# Generated at 2022-06-13 03:27:50.888150
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    # Init
    test_platform = platform.system()
    test_distribution = platform.dist()[0]

    # Mock ansible module class
    class MockAnsibleModule:
        def __init__(self):
            self.params = {}

        def get_bin_path(self, command):
            if command == 'systemctl':
                return True
            else:
                return False

    # Create a mock Module object
    test_module_obj = MockAnsibleModule()

    # Create a mock Collected_facts object
    test_collected_facts_obj = {
        'platform': test_platform,
        'distribution': test_distribution
    }

    # Collect facts
    fact_collector_obj = ServiceMgrFactCollector()

# Generated at 2022-06-13 03:28:00.009625
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    """
    Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
    """
    class ModuleStub(object):
        @staticmethod
        def get_bin_path(path, *args, **kwargs):
            if path == 'systemctl':
                return '/usr/bin/systemctl'
            else:
                return None

    smfc = ServiceMgrFactCollector()
    assert smfc.is_systemd_managed_offline(ModuleStub()) is False

if __name__ == '__main__':
    test_ServiceMgrFactCollector_is_systemd_managed_offline()

# Generated at 2022-06-13 03:28:09.788884
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts.collector import get_collector_instance
    service_mgr_fact_collector = get_collector_instance(ServiceMgrFactCollector)
    class FakeModule:
        def get_bin_path(self, program):
            if program == "systemctl":
                return True
            else:
                return False
    class FakeOs:
        def path(self, path):
            if path == "/run/systemd/system/":
                return True
            elif path == "/dev/.run/systemd/":
                return True
            elif path == "/dev/.systemd/":
                return True
            else:
                return False
    class FakeOsL():
        def readlink(self, path):
            if path == "/sbin/init":
                return "systemd"


# Generated at 2022-06-13 03:28:16.565069
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    from ansible.module_utils.facts.collector import MockModule

    # Mocking the module
    module = MockModule({'sysctl': {}})

    mock_facts_dict = {
        "ansible_distribution": "OpenWrt",
        "ansible_system": "Linux"
    }

    # Mocking the class behavior for
    # - is_systemd_managed
    # - is_systemd_managed_offline
    ServiceMgrFactCollector.is_systemd_managed = Mock(return_value=False)
    ServiceMgrFactCollector.is_systemd_managed_offline = Mock(return_value=False)

    # Assertions
    # - get facts related to system service manager and init

# Generated at 2022-06-13 03:28:20.917607
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    import ansible.module_utils.facts.collector.service_mgr as service_mgr
    from ansible.module_utils.facts import ModuleFactCollector
    mgr = service_mgr.ServiceMgrFactCollector()
    assert not mgr.is_systemd_managed(ModuleFactCollector())


# Generated at 2022-06-13 03:29:20.363088
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    """Test method for collect in class ServiceMgrFactCollector"""
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils import basic

    class MockModule(object):
        def __init__(self, params=None, failed=False, changed=False, msg=None, result=None):
            self.params = params
            self.failed = failed
            self.changed = changed
            self.msg = msg
            self.result = result
            self.argument_spec = basic.AnsibleModule.argument_spec

    class MockAnsibleModule(object):
        def __init__(self, module_args, params=None, failed=False, changed=False, msg=None, result=None):
            self.params = params
            self.failed = failed
            self.changed = changed
           

# Generated at 2022-06-13 03:29:29.555415
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    import copy

    try:
        from ansible.module_utils import basic
    except ImportError:
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'module_utils'))
        from ansible.module_utils import basic

    test_module = basic.AnsibleModule({'_ansible_keep_remote_files': True}, '', {})

    mock_os_module = copy.copy(os)
    # mock islink function and use as an example a normal boot
    mock_os_module.islink = lambda path: True
    mock_os_module.readlink = lambda path: 'systemd'
    test_module.os = mock_os_module

    result = ServiceMgrFactCollector.is_systemd

# Generated at 2022-06-13 03:29:40.760670
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    path_to_mock = os.path.join(os.path.dirname(__file__), os.pardir, 'module_utils', 'facts', 'platform', 'test')
    from ansible.module_utils import facts
    facts.SUPPORTED_SUBFACTS = {'service_mgr': set()}
    facts.CACHE = {}
    import module_utils.facts.platform
    module_utils.facts.platform.ServiceMgrFactCollector.is_systemd_managed = lambda module: 'systemd'
    module_utils.facts.platform.ServiceMgrFactCollector.is_systemd_managed_offline = lambda module: 'systemd'
    module_utils.facts.platform.ServiceMgrFactCollector._fact_ids = set()

    service_mgr_fact_collector = module

# Generated at 2022-06-13 03:29:50.822166
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    # test case 1.1
    from mock import Mock, patch
    import sys
    import os


# Generated at 2022-06-13 03:30:04.151623
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():

    # Test case 1:
    #
    # Given:
    # If /sbin/init is not a symlink, then no further checks are made. 
    #
    # When:
    # /sbin/init is not a symlink
    #
    # Then:
    # systemd is not detected and method returns False

    class MockModule(object):
        def __init__(self):
            self.path = '/bin/'

        def get_bin_path(self, command):
            return "/bin/" + command

    m = MockModule()

    s = ServiceMgrFactCollector()
    result = s.is_systemd_managed_offline(m)

    assert result == False


    # Test case 2:
    #
    # Given:
    # If /sbin/init is a symlink

# Generated at 2022-06-13 03:30:06.925401
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    ServiceMgrFactCollectorObject = ServiceMgrFactCollector()
    ServiceMgrFactCollectorObject.collect()

# Generated at 2022-06-13 03:30:11.436380
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    fakeModule = AnsibleModule()
    fakeModule.get_bin_path = lambda x: '/sbin/systemctl'
    fakeModule.run_command = lambda x, use_unsafe_shell=True: (0, '', '')
    facts = ServiceMgrFactCollector.is_systemd_managed_offline(fakeModule)
    assert facts == True

from ansible.module_utils.facts.collector import BaseFactCollector
from ansible.module_utils.facts import AnsibleModule
from ansible.module_utils._text import to_native

from ansible.module_utils.facts.utils import get_file_content

from ansible.module_utils.facts.collector import BaseFactCollector
from ansible.module_utils.facts import AnsibleModule
from ansible.module_utils._text import to_

# Generated at 2022-06-13 03:30:19.380705
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    import os
    import platform
    import sys

    # Ensure platform is Linux
    if platform.system() != 'Linux':
        sys.exit(0)

    # Ensure we are root user, otherwise we can't run privileged commands
    if os.geteuid() != 0:
        sys.exit(0)

    module = AnsibleModuleMock()
    smfc = None
    systemd = False

    # Mock out the SystemV init system
    os.system("rm -f /etc/init.d/sshd")
    os.system("rm -f /sbin/init")
    os.system("ln -s /lib/systemd/systemd /sbin/init")
    os.system("systemctl mask sshd")

    # Create the ServiceMgrFactCollector object
    smfc = ServiceMgrFactCollector()

    #

# Generated at 2022-06-13 03:30:30.042316
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    import tempfile
    import shutil
    import os

    def is_systemd_managed(paths):
        self = ServiceMgrFactCollector()
        module = AnsibleModuleDummy(paths=paths)
        return self.is_systemd_managed(module)

    def is_systemd_managed_offline(paths):
        self = ServiceMgrFactCollector()
        module = AnsibleModuleDummy(paths=paths)
        return self.is_systemd_managed_offline(module)

    # test if it returns True when the system is systemd managed
    base_paths = {'/proc/1/comm': None, '/sbin/init': '/usr/lib/systemd/systemd', '/run/systemd/system/': None}

# Generated at 2022-06-13 03:30:39.858586
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():

    # Arrange
    from ansible.module_utils.facts.utils import get_file_content
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts import collector

    class FakeModule(object):

        def __init__(self):
            self.run_command_results = {}
            self.params = {}
            self.file_content_results = {}
            self.file_exists_results = {}
            self.file_islink_results = {}

        def get_bin_path(self, path):
            if path == 'systemctl':
                return '/usr/bin/systemctl'
            elif path == 'initctl':
                return '/sbin/initctl'
            elif path == 'sv':
                return '/sbin/sv'
            return

# Generated at 2022-06-13 03:32:41.681953
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    import tempfile
    import shutil

    # Test #1: init is a link to systemd
    with tempfile.TemporaryDirectory() as tmpdirname:
        os.mkdir(os.path.join(tmpdirname, 'sbin'))
        os.symlink(os.path.join(tmpdirname, 'bin/systemd'), os.path.join(tmpdirname, 'sbin/init'))
        assert ServiceMgrFactCollector.is_systemd_managed_offline(module=AnsibleModuleMock(bin_path=os.path.join(tmpdirname, 'bin')))

    # Test #2: init is not a link to systemd
    with tempfile.TemporaryDirectory() as tmpdirname:
        os.mkdir(os.path.join(tmpdirname, 'sbin'))


# Generated at 2022-06-13 03:32:44.447308
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    # FIXME: mock and call is_systemd_managed_offline
    ServiceMgrFactCollector.is_systemd_managed_offline([])
