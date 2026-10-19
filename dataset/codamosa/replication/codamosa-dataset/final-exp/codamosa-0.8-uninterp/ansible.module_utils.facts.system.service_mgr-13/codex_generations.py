

# Generated at 2022-06-13 03:23:14.021907
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    class TestModule:
        def __init__(self, service_mgr_name, cmd_output=None, rc=None, err=None, path_exists=None, is_dir=None, is_symlink=None):
            self.params = {'gather_subset': ['all']}
            self.service_mgr_name = service_mgr_name
            self.cmd_output = cmd_output
            self.rc = rc
            self.err = err
            self.path_exists = path_exists
            self.is_dir = is_dir
            self.is_symlink = is_symlink

        def get_bin_path(self, cmd):
            return cmd


# Generated at 2022-06-13 03:23:23.066649
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    import os
    import tempfile
    import shutil
    from ansible.module_utils import basic

    symlink_path = '/sbin/init'
    if not os.path.exists(symlink_path):
        os.symlink('systemd', symlink_path)

    # An exception is raised if the executable path is not found.
    # The exception is silenced by passing 'catch_errors=False'
    sample_module = basic.AnsibleModule(argument_spec={}, catch_errors=False)

    if ServiceMgrFactCollector.is_systemd_managed_offline(sample_module):
        result_true = True
    else:
        result_true = False

    os.remove(symlink_path)


# Generated at 2022-06-13 03:23:30.875382
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    facts_dict = {}
    svc_mgr_fact = ServiceMgrFactCollector()

    # test 1, service_mgr = systemd, return facts_dict with service_mgr = systemd,
    # since all the required facts are present and is_systemd_managed() returns True
    facts_dict['platform'] = 'Linux'
    facts_dict['distribution'] = 'Gentoo'
    assert svc_mgr_fact.collect(None, facts_dict) == {'service_mgr': 'systemd'}

    # test 2, service_mgr = openrc, return facts_dict with service_mgr = openrc,
    # since all the required facts are present and is_systemd_managed() returns False
    # and os.path.exists('/sbin/openrc') returns True
    facts_dict

# Generated at 2022-06-13 03:23:43.889247
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    import pytest
    import os
    import pwd
    import stat
    import tempfile

    # prepare a fake system
    test_dir = tempfile.mkdtemp(prefix="ansible_test_")
    test_ansible_dir = tempfile.mkdtemp(prefix="ansible_test_", dir=test_dir)
    test_ansible_tmp_dir = tempfile.mkdtemp(prefix="ansible_tmp_", dir=test_dir)

    test_facts = {}

    # create fake /proc/1/comm
    with open(os.path.join(test_ansible_tmp_dir, "1"), 'w') as fd:
        fd.write("ansible_fake_proc_1\n")


# Generated at 2022-06-13 03:23:44.604820
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():

    ServiceMgrFactCollector().collect()

# Generated at 2022-06-13 03:23:55.799195
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    # Caller of this method is a class method, so we need to mock it
    # rather than inheritance.
    from unittest.mock import MagicMock
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.service_mgr import ServiceMgrFactCollector

    module = MagicMock()
    base_fact_collector = BaseFactCollector()
    base_fact_collector.get_file_content = MagicMock()
    service_mgr_fact_collector = ServiceMgrFactCollector()
    service_mgr_fact_collector.get_file_content = base_fact_collector.get_file_content

    # Test with /sbin/init is not a symlink

# Generated at 2022-06-13 03:24:07.285579
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    module = MockAnsibleModule()

    sm = ServiceMgrFactCollector()
    sm.module = module

    # we mock os.path.islink so we can simulate various conditions around /sbin/init
    def mock_islink(path):
        # init is a symlink
        if path == "/sbin/init":
            return True

        return False

    # we mock os.readlink so we can simulate various conditions around /sbin/init
    def mock_readlink(path):
        # init is a symlink to systemd
        if path == "/sbin/init":
            return "systemd"

        return False

    assert sm.is_systemd_managed_offline(module) == False

    module.os.path.islink = mock_islink
    assert sm.is_systemd_managed_off

# Generated at 2022-06-13 03:24:16.167970
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():

    class FakeModule:

        def __init__(self):
            self.result = dict()
            self.params = dict()

        def fail_json(self, **kwargs):
            pass

        def run_command(self, cmd, use_unsafe_shell):
            if cmd == "ps -p 1 -o comm|tail -n 1":
                self.result['rc'] = 0
                self.result['stdout'] = 'init\n'
                self.result['stderr'] = ''
            return self.result['rc'], self.result['stdout'], self.result['stderr']

        def get_bin_path(self, binary):
            if binary == 'systemctl':
                return '/bin/systemctl'
            if binary == 'initctl':
                return '/sbin/initctl'

# Generated at 2022-06-13 03:24:25.067165
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts.collector import CollectorFactory
    from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector

    # Mock class for the module
    class ModuleMock(object):
        def __init__(self):
            self.params = {}

        def fail_json(self, msg):
            raise Exception(msg)

        def get_bin_path(self, executable):
            # Mock method to return path to executable
            return executable

    module = ModuleMock()

    # Mock class for LinuxDistributionMock
    class LinuxDistributionMock(object):
        def __init__(self):
            self.system = 'Linux'
        def linux_distribution(self):
            return True

    # Mock class for the platform

# Generated at 2022-06-13 03:24:34.329844
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    import ansible.module_utils.facts.collector.service_mgr
    class MockModule(object):
        def get_bin_path(self, name):
            return '/bin/%s' % name
        def path_exists(self, name):
            return name in ['/run/systemd/system/', '/dev/.run/systemd/']
    module = MockModule()
    service_mgr_fact_collector = ansible.module_utils.facts.collector.service_mgr.ServiceMgrFactCollector()
    assert service_mgr_fact_collector.is_systemd_managed(module)


# Generated at 2022-06-13 03:24:52.576761
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    class MockModule(object):
        def run_command(self, cmd, check_rc=True, **kwargs):
            return 1, '', 'not relevant here'
        def get_bin_path(self, cmd, required=False, opt_dirs=[]):
            return '/usr/bin/{0}'.format(cmd)

    module = MockModule()

    # No systemctl; this is not systemd
    assert not ServiceMgrFactCollector.is_systemd_managed(module)


# Generated at 2022-06-13 03:25:04.984929
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collection import FactsCollectionError
    from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector
    module = Mock()
    module.run_command("systemctl")
    module.run_command("ps -p 1 -o comm|tail -n 1", use_unsafe_shell=True)
    module.get_bin_path("systemctl")
    module.get_bin_path("systemd")
    module.get_bin_path("init")
    module.get_bin_path("/usr/bin")
    module.get_bin_path("/sbin/init")
    module.get_bin_path("ls")

# Generated at 2022-06-13 03:25:17.038372
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    def get_bin_path(bin_name):
        return "/tmp/{0}".format(bin_name)

    def run_command(cmd, use_unsafe_shell=False):
        return (0, "", "")

    class TestModule:
        def __init__(self):
            self.run_command = run_command
            self.get_bin_path = get_bin_path

    test_module = TestModule()
    import os
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        os.mkdir(os.path.join(tmp, "sbin"))
        os.mkdir(os.path.join(tmp, "usr"))

# Generated at 2022-06-13 03:25:19.873014
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    """Unit test for method collect of class ServiceMgrFactCollector"""
    # Just instantiate the class and call the method
    fact_collector = ServiceMgrFactCollector()
    result = fact_collector.collect()


if __name__=='__main__':
    test_ServiceMgrFactCollector_collect()

# Generated at 2022-06-13 03:25:25.675728
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    fact_collector = ServiceMgrFactCollector()
    module = FakeModule()

    # Test case 1: when /sbin/init is not a symlink
    os.symlink("/bin/ls", "/sbin/init")
    assert not fact_collector.is_systemd_managed_offline(module)
    os.remove("/sbin/init")

    # Test case 2: when /sbin/init is a symlink to systemctl
    os.symlink("/bin/systemctl", "/sbin/init")
    assert not fact_collector.is_systemd_managed_offline(module)
    os.remove("/sbin/init")

    # Test case 3: when /sbin/init is a symlink to systemd and systemctl is not in PATH
    os.symlink

# Generated at 2022-06-13 03:25:36.477092
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    collector = ServiceMgrFactCollector()

    class MockModule(object):
        def __init__(self, bin_path=None):
            self.bin_path = bin_path
            self.__params = {}

        def get_bin_path(self, command, opt_dirs=[]):
            if self.bin_path:
                return self.bin_path
            return None

    # If the systemd command can be found in the PATH, then is_systemd_managed_offline should return True
    module = MockModule(bin_path='/bin/systemctl')
    service_mgr = collector.is_systemd_managed_offline(module=module)
    assert service_mgr

    # If the systemd command can not be found in the PATH, then is_systemd_managed_offline should return False

# Generated at 2022-06-13 03:25:44.769606
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    class MockModule:
        def __init__(self, params):
            self.params = params
        def fail_json(self, msg):
            self.msg = msg
        def get_bin_path(self, name):
            return 'systemctl' if name == 'systemctl' else None
        def run_command(self, command, use_unsafe_shell):
            return (0, 'init', None)

    mock_module = MockModule({})
    assert ServiceMgrFactCollector.is_systemd_managed(mock_module) == True


# Generated at 2022-06-13 03:25:52.716593
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    from ansible.module_utils.facts.service_mgr import ServiceMgrFactCollector
    from ansible.module_utils.facts.service_mgr import is_systemd_managed_offline
    import os

    class MockModule(object):
        def get_bin_path(self, name, required=False):
            if name == 'systemctl':
                return '/usr/bin/systemctl'
            else:
                raise ValueError('unknown bin name: %s' % name)

    class TestServiceMgrFactCollector(ServiceMgrFactCollector):
        @classmethod
        def is_systemd_managed_offline(cls, module):
            return is_systemd_managed_offline(module)

    mock_module = MockModule()

    # Test with /sbin/init is a symlink to systemd

# Generated at 2022-06-13 03:26:01.761283
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    # import module
    import ansible.module_utils.facts.system.service_mgr as service_mgr

    class MockModule(object):
        def __init__(self, dict_1=None, dict_2=None):
            self.fail_json = dict_1
            self.exit_json = dict_2

        def get_bin_path(self, name, opt_dirs=[]):
            if name == 'systemctl':
                return '/bin/systemctl'

    class DictModule(dict):
        def __getattr__(self, name):
            try:
                return self[name]
            except KeyError:
                pass


# Generated at 2022-06-13 03:26:07.834588
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    mock_module = AnsibleModuleMock(
        dict(ansible_distribution='MacOSX')
    )
    service_mgr_collector = ServiceMgrFactCollector()
    service_mgr_collector.collect(mock_module)
    assert mock_module.exit_json.called
    assert mock_module.exit_json.call_args[0] == \
        (dict(changed=False, ansible_facts={'service_mgr': 'launchd'}),)


# Generated at 2022-06-13 03:26:37.724865
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    collector = ServiceMgrFactCollector({}, None)
    collected_facts = {}
    test_facts = collector.collect(None, collected_facts)
    assert 'service_mgr' in test_facts
    assert test_facts['service_mgr'] is not None

# Generated at 2022-06-13 03:26:48.282257
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    # Mock the "import" of a module
    import module_utils.facts.collectors.service_mgr as service_mgr

    # Mock the "import" of a module
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts.collectors.service_mgr import ServiceMgrFactCollector

    # Define the mock ansible module for the ansible.module_utils.facts.collectors.service_mgr module
    module = AnsibleModule()

    # Mock the version_cmp method of the ansible.module_utils.facts.collectors.service_mgr module
    def version_cmp(module, name, version, version_db="Redhat"):
        return LooseVersion(version) >= LooseVersion('1.5.8-5')

    service_mgr.version

# Generated at 2022-06-13 03:26:55.426661
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    import tempfile
    import shutil
    from ansible.module_utils.facts.collector import BaseFactCollector

    # Create a temp dir with systemd as init, then run is_systemd_managed_offline method.
    # assert that the method can detect whether systemd is the init system or not.
    with tempfile.TemporaryDirectory() as tempdir:
        servicedir = os.path.join(tempdir, 'service')
        systemd = os.path.join(tempdir, 'systemd')
        os.mkdir(servicedir)
        os.mkdir(systemd)
        os.symlink('/usr/lib/systemd/systemd',
                   os.path.join(systemd, 'init'))

# Generated at 2022-06-13 03:27:02.762963
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts import ModuleFacts
    import ansible.module_utils.facts.collector

    # Create an instance of the ServiceMgrFactCollector
    obj = ansible.module_utils.facts.collector.get_collector('ServiceMgrFactCollector')

    # Create an instance of ModuleFacts
    module = ModuleFacts()

    # Run the method to test with the arguments: (module)
    obj.is_systemd_managed(module)

# Generated at 2022-06-13 03:27:07.719563
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    import tempfile
    from ansible.module_utils._text import to_bytes

    collector = ServiceMgrFactCollector()
    module = MockModule()
    module.run_command = run_command
    module.get_bin_path = lambda param: None # no path to systemctl

    temp = tempfile.NamedTemporaryFile()
    os.symlink('systemd', temp.name)
    assert collector.is_systemd_managed_offline(module)


# Mock classes and functions used only in the unit tests

# Generated at 2022-06-13 03:27:18.659611
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    class MockModule:
        def get_bin_path(self, path):
            return '/usr/bin/'+path

    class MockOs:
        @staticmethod
        def islink(path):
            return True

        @staticmethod
        def readlink(path):
            return '/usr/lib/systemd/systemd'

    class MockOsModule:

        @staticmethod
        def path():
            return MockOs()

    module = MockModule()
    os_module = MockOsModule()
    sys_module = None
    my_obj = ServiceMgrFactCollector()

    assert my_obj.is_systemd_managed_offline(module=module)
    assert my_obj.is_systemd_managed_offline(module=None) == False

# Generated at 2022-06-13 03:27:30.034024
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts.collector import FactsCollector
    from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector

    # Test for systemd
    class TestModule(object):
        def __init__(self):
            self.run_command = self.run_command1

        def run_command1(self, _, use_unsafe_shell=False):
            return (0, 'systemd', '')

        def get_bin_path(self, binary):
            return '/usr/bin/' + binary

    test_module = TestModule()
    test_system_servicemgr = ServiceMgrFactCollector(test_module, facts_collector=FactsCollector(test_module))
    assert test_system_servicemgr.is_systemd_managed

# Generated at 2022-06-13 03:27:40.981732
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    class MockModule():
        _result = True
        _command = 'systemctl --version'
        _module_args = {'paths': '/bin'}

        def get_bin_path(self, binary):
            return True

        def run_command(self, command, use_unsafe_shell=False):
            return None, '2.0.0', None

    class MockObject():
        def __init__(self, collected_facts):
            self.ansible_facts = collected_facts

    class MockCollectedFacts():
        def __init__(self):
            self.data = {}

        def add(self, key, val):
            self.data[key] = val

        def add_all(self, data):
            for key, val in data.items():
                self.data[key] = val

       

# Generated at 2022-06-13 03:27:49.183616
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    from ansible.module_utils.facts.collector import BaseFactCollector
    import os

    open('/sbin/init', 'w').close()
    os.symlink('/sbin/init', '/sbin/init.systemd')
    assert 'systemd' == ServiceMgrFactCollector.is_systemd_managed_offline(BaseFactCollector)

    os.remove('/sbin/init.systemd')
    assert not ServiceMgrFactCollector.is_systemd_managed_offline(BaseFactCollector)

    os.remove('/sbin/init')

# Generated at 2022-06-13 03:27:59.673750
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    import unittest

    from ansible.module_utils.facts.collector.service_mgr import ServiceMgrFactCollector

    class ServiceMgrFactCollectorTestCase(unittest.TestCase):
        def setUp(self):
            self.fixture = ServiceMgrFactCollector()

    # Mocking module class
    class ModuleMock:
        def __init__(self, is_systemd_managed=False):
            self.run_command_result = 0
            self.run_command_stdout = None
            self.run_command_stderr = None
            self.is_systemd_managed = is_systemd_managed

        def get_bin_path(self, bin_name):
            if bin_name in ['systemctl', 'initctl']:
                return True
            else:
                return

# Generated at 2022-06-13 03:29:09.212774
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    from ansible.module_utils.facts.collector import TestModule
    from ansible.module_utils.facts.utils import AnsibleNullFactsCollector

    # For testing, we use TestModule object. We need to patch its
    # methods, as they return a dummy value.
    test_module = TestModule(
        {},
        supported_by_current_interpreter=True,
        ansible_facts_collector=AnsibleNullFactsCollector()
    )

    collector = ServiceMgrFactCollector()

    # Check with not existing sbin/init symlink
    test_module.run_command = Mock(return_value=(0, "", ""))
    assert collector.is_systemd_managed_offline(module=test_module) is False

    # Check with sbin/init symlink to systemd

# Generated at 2022-06-13 03:29:11.576978
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    # Just test that it doesn't throw exception(s)
    smfc = ServiceMgrFactCollector()
    smfc.collect(module=None, collected_facts=None)

# Generated at 2022-06-13 03:29:19.841910
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts.collector import DictFactsCollector
    from ansible.module_utils.facts.collectors.system.service_mgr import ServiceMgrFactCollector
    import ansible.module_utils.facts.system.service_mgr
    import ansible.module_utils.facts.system.service_mgr
    import os

    class MockModule(object):
        def __init__(self, **kwargs):
            self.params = kwargs

        def run_command(self, *_, **__):
            rc = 0
            out = ''
            err = ''
            return rc, out, err

        def get_bin_path(self, arg, **_):
            if arg == 'systemctl':
                return '/bin/systemctl'
            else:
                return None



# Generated at 2022-06-13 03:29:28.908109
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    class ModuleMock(object):
        def __init__(self):
            self.called_bin_path = 0
            self.called_os_path_exists = 0
            self.called_os_readlink = 0
            self.called_os_path_islink = 0
            self.called_os_path_basename = 0

        def get_bin_path(self, arg):
            self.called_bin_path += 1
            if arg == 'systemctl':
                return True
            return False

        def os_path_exists(self, arg):
            self.called_os_path_exists += 1
            if arg == '/sbin/init':
                return True
            else:
                return False

        def os_readlink(self, arg):
            self.called_os_readlink += 1


# Generated at 2022-06-13 03:29:40.107308
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils import basic
    from ansible.module_utils.facts import collector

    def get_bin_path(self, arg):
        if arg == 'systemctl':
            return '/bin/true'
        return None

    module = basic.AnsibleModule(
        argument_spec=dict(),
    )
    module.get_bin_path = get_bin_path.__get__(module, basic.AnsibleModule)

    # Mock existence of files
    def isfile(arg):
        return os.path.basename(arg) in test_cases[case]['mock_files']

    def exists(arg):
        return arg in test_cases[case]['mock_files']

    # Mock class names

# Generated at 2022-06-13 03:29:50.156427
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    class ModuleStub:
        def __init__(self, fake_path, fake_canary):
            self.path = fake_path
            self.canary = fake_canary

        def get_bin_path(self, command):
            if command == 'systemctl':
                return self.path

        @staticmethod
        def run_command(cmd, use_unsafe_shell=True, check_rc=False, executable=None, data=None, binary_data=False, path_prefix=None, cwd=None, **kwargs):
            return 0, '', ''

    # if tools are present, check if systemd is the boot init system
    module = ModuleStub("/bin/systemctl", '/run/systemd/system/')
    assert ServiceMgrFactCollector.is_systemd_managed(module)

    module

# Generated at 2022-06-13 03:29:56.617475
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    mock_module_class = type('MockModuleUtil', (object,), {})
    mock_module = mock_module_class()
    mock_module.get_bin_path = lambda self, cmd: cmd

# Generated at 2022-06-13 03:30:05.701420
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    from ansible.module_utils.facts.collector import Collector
    collected_facts = Collector().collect(module=None, collected_facts=None)
    collector = ServiceMgrFactCollector()

    # test success (systemd)
    module = mock.MagicMock()
    module.get_bin_path.return_value = '/bin/systemctl'
    os.path.islink = mock.MagicMock(return_value=True)
    os.readlink = mock.MagicMock(return_value='systemd')
    assert collector.is_systemd_managed(module=module) == True

    # test negative (non-systemd)
    module = mock.MagicMock()
    module.get_bin_path.return_value = '/bin/systemctl'
    os.path.islink = mock.MagicMock

# Generated at 2022-06-13 03:30:16.751328
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    import ansible.module_utils.facts.collector

    # if no tools exist and no canaries, fallback to False
    module_mock = MagicMock()
    module_mock.get_bin_path.return_value = None
    assert ServiceMgrFactCollector.is_systemd_managed(module_mock) is False

    # if tools exist but no canaries, fallback to False
    module_mock = MagicMock()
    module_mock.get_bin_path.return_value = 'systemctl'
    assert ServiceMgrFactCollector.is_systemd_managed(module_mock) is False

    # if tools exist and canaries, it's systemd
    module_mock = MagicMock()
    module_mock.get_bin_path.return_value = 'systemctl'


# Generated at 2022-06-13 03:30:27.194669
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts import BaseFactCollector
    from AnsibleModuleMock import AnsibleModuleMock
    import stat

    # ServiceMgrFactCollector is a subclass of BaseFactCollector
    assert issubclass(ServiceMgrFactCollector, BaseFactCollector)

    # ServiceMgrFactCollector is registered as a fact provider with name 'service_mgr'
    assert 'service_mgr' in Collector.fact_classes

    # service_mgr is registered as a required fact
    assert 'service_mgr' in BaseFactCollector.required_facts

    test_module_path = os.path.join(os.path.dirname(__file__), 'FactsCollectorModule.py')