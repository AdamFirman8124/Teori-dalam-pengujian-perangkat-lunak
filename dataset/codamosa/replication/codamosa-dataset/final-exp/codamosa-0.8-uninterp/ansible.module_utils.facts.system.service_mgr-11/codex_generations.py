

# Generated at 2022-06-13 03:23:12.469160
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    import tempfile
    import shutil
    import os

    # Setting up necessary environnement
    test_dir = tempfile.mkdtemp()
    os.mkdir(os.path.join(test_dir, 'sbin'))
    test_target = os.path.join(test_dir, 'sbin', 'init')
    test_link = os.path.join(test_dir, 'sbin', 'systemd')
    shutil.copyfile(test_target, test_link)

    # Testing a first case
    os.symlink(test_link, test_target)
    assert ServiceMgrFactCollector.is_systemd_managed_offline(None)

    # Testing a second case
    os.remove(test_link)
    assert not ServiceMgrFactCollector.is_systemd_

# Generated at 2022-06-13 03:23:16.436286
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts.collectors import ServiceMgrFactCollector
    from ansible.module_utils.facts.utils import MockModule
    test_module = MockModule()
    results = ServiceMgrFactCollector.is_systemd_managed(test_module)
    assert results is False

# Generated at 2022-06-13 03:23:25.580944
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    import ansible.module_utils.facts.collector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collectors.service_mgr import ServiceMgrFactCollector
    from ansible.module_utils.facts import Collectors
    import ansible.module_utils.facts.utils
    from ansible.module_utils.facts.utils import get_file_content
    from ansible.module_utils._text import to_native
    import platform
    import tempfile
    import os
    import shutil
    from ansible.module_utils.facts.utils import get_file_content
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collectors.service_mgr import ServiceMgrFact

# Generated at 2022-06-13 03:23:33.364590
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    # Systemd managed
    proc_1 = "/usr/lib/systemd/systemd"
    with mock.patch('ansible.module_utils.facts.collector.ServiceMgrFactCollector.is_systemd_managed_offline') as mocked_is_systemd_managed_offline:
        mocked_is_systemd_managed_offline.return_value = ''
        assert(ServiceMgrFactCollector.is_systemd_managed(proc_1)) == True

    # Systemd not managed
    proc_1 = None
    with mock.patch('ansible.module_utils.facts.collector.ServiceMgrFactCollector.is_systemd_managed_offline') as mocked_is_systemd_managed_offline:
        mocked_is_systemd_managed_offline.return_value = ''

# Generated at 2022-06-13 03:23:37.745525
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    smfc = ServiceMgrFactCollector

    assert smfc.is_systemd_managed(None) is True
    assert smfc.is_systemd_managed_offline(None) is True

    assert smfc.is_systemd_managed({}) is False
    assert smfc.is_systemd_managed_offline({}) is False

    assert smfc.is_systemd_managed({'get_bin_path': lambda x: '/bin/systemctl'}) is True
    assert smfc.is_systemd_managed_offline({'get_bin_path': lambda x: '/bin/systemctl'}) is True

    assert smfc.is_systemd_managed({'get_bin_path': lambda x: '/sbin/initscript'}) is False

# Generated at 2022-06-13 03:23:45.346922
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    """Unit test for method collect of class ServiceMgrFactCollector"""
    # Initialize test environment
    ServiceMgrFactCollector.is_systemd_managed_offline = ServiceMgrFactCollector.is_systemd_managed = lambda x: True
    # Initialize test variable
    collected_facts = {}
    module = AnsibleModule()
    expected_dict = {'service_mgr': 'systemd'}

    # Call method under test
    actual_dict = ServiceMgrFactCollector.collect(module=module, collected_facts=collected_facts)
    assert expected_dict == actual_dict

# Generated at 2022-06-13 03:23:56.326557
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    # Fake data for testing. To test the upper layer of the method,
    # we mock the return value of class method get_bin_path. We don't care about
    # the parameter that is passed to get_bin_path, but we do care
    # about the number of times it is called.
    class Fake_module(object):
        def __init__(self):
            self.get_bin_path_called_times = 0

        def get_bin_path(self, x):
            self.get_bin_path_called_times += 1
            return 'some_string'

    # Pass in a module with a fake get_bin_path method that returns a string.
    # Verify that the returned value is False because the condition is not satisfied
    fm = Fake_module()
    ret = ServiceMgrFactCollector.is_systemd

# Generated at 2022-06-13 03:23:59.465244
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    collector = ServiceMgrFactCollector()
    assert collector.is_systemd_managed() is False

# Generated at 2022-06-13 03:24:05.483197
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    # Mock module
    class MockModule(object):
        def get_bin_path(self, name):
            return name

    module = MockModule()

    # Run test
    service_mgr = ServiceMgrFactCollector()
    is_systemd_managed = service_mgr.is_systemd_managed(module)

    # Assertions
    assert type(is_systemd_managed) is bool


# Generated at 2022-06-13 03:24:14.588646
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    """
        Unit test for method collect of class ServiceMgrFactCollector
    """
    import ansible.module_utils.facts.collector
    ServiceMgrFactCollector.is_systemd_managed = lambda x: True
    ServiceMgrFactCollector.is_systemd_managed_offline = lambda x: True
    module_mock = ansible.module_utils.facts.collector.AnsibleModuleMock()
    module_mock.get_bin_path = lambda x: True
    assert ServiceMgrFactCollector.collect(module=module_mock) == {'service_mgr' : 'systemd'}
    ServiceMgrFactCollector.is_systemd_managed = lambda x: False

# Generated at 2022-06-13 03:24:37.924147
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    class Options:
        def __init__(self):
            self.remote_tmp = '/tmp'
    from ansible.module_utils.facts.collectors import which

    class TestModule:
        def __init__(self):
            self.options = Options()
            self.which = which

        def get_bin_path(self, program):
            return self.which(program)

    test_module = TestModule()

    # testing with a systemd-managed system.
    with open('/proc/1/comm', 'w') as f:
        f.write('systemd')
    with open('/proc/1/cmdline', 'w') as f:
        f.write('/lib/systemd/systemd')
    os.symlink('/lib/systemd/systemd', '/bin/systemctl')


# Generated at 2022-06-13 03:24:47.440192
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():

    from ansible.module_utils.facts.collector.system import ServiceMgrFactCollector

    import ansible.module_utils.facts.system.service_mgr

    class ModuleMock(object):
        def __init__(self, params):
            self.params = params
            self.run_command_args = []
            self.run_command_rc = 0
            self.run_command_stdout = ''

        def get_bin_path(self, bin_name, required=False, opt_dirs=[]):
            if bin_name == 'systemctl':
                return '/bin/systemctl'
            elif bin_name == 'initctl':
                return '/bin/initctl'

        def run_command(self, args, use_unsafe_shell=True):
            self.run_command_args.append

# Generated at 2022-06-13 03:24:52.944055
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    import tempfile
    import shutil
    import os

    test_cases = [
        # input, expected
        # absent
        (([], [], []), False),
        # no systemd
        ((['/usr/bin/systemctl'], [], []), False),
        # runit-init as pid1
        ((['/usr/bin/systemctl'], ['/run/systemd/system/'], []), False),
        # systemd
        ((['/usr/bin/systemctl'], [], ['/run/systemd/system/']), True),
    ]

    tempdir = tempfile.mkdtemp()

# Generated at 2022-06-13 03:25:00.568375
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    # create mock for module
    module = MockModule()
    module.get_bin_path = lambda x: os.path.join(os.sep, 'bin', 'systemctl')
    os.readlink = lambda x: 'systemd'

    # create collector
    sms = ServiceMgrFactCollector()

    # test
    assert sms.is_systemd_managed_offline(module=module)


# Generated at 2022-06-13 03:25:02.937642
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    collector = ServiceMgrFactCollector()
    assert collector.is_systemd_managed_offline(None) == False
  

# Generated at 2022-06-13 03:25:10.584167
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    module = AnsibleModuleMock()
    module.get_bin_path = get_bin_path
    collector = ServiceMgrFactCollector(module=module)

    # Paths that will be checked for canaries
    # Return True if canary exists
    def is_file(path):
        if path in ['/run/systemd/system/', '/.run/systemd/']:
            return True
        else:
            return False

    # Mock os.path.exists
    original_os_path_exists = os.path.exists
    os.path.exists = is_file

    # Test the case if systemd is used as the init system
    result = collector.is_systemd_managed(module=module)
    assert result == True

    # UnMock os.path.exists

# Generated at 2022-06-13 03:25:20.926296
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    import os
    import tempfile

    from ansible.module_utils.facts.collector import ServiceMgrFactCollector, BaseFactCollector

    class FakeModule(object):
        def __init__(self):
            self.check_mode = False
            self.debug = True
            self.no_log = False
            self.run_command_environ_update = {}

        def get_bin_path(self, executable, required=False, opt_dirs=[]):
            return '/bin/{0}'.format(executable)

        def run_command(self, cmd, use_unsafe_shell=False):
            return 0, cmd, ''

    basedir = tempfile.mkdtemp()

# Generated at 2022-06-13 03:25:33.745627
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collectors.service_mgr import ServiceMgrFactCollector
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(argument_spec={})


# Generated at 2022-06-13 03:25:44.411706
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    from ansible.module_utils.facts.collector import ServiceMgrFactCollector
    from ansible.module_utils.facts.collector.system import SystemFactCollector
    from ansible.module_utils.facts.collector.base import BaseFactCollector
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule

    mock_module = AnsibleModule()
    mock_module.params.update({})
    mock_module.run_command = lambda args, binary_data=False: (0, to_bytes('systemd'), '')
    mock_module.get_bin_path = lambda args: '/bin/systemctl'

    facts = {'service_mgr': '', 'system': 'Linux'}
    system = SystemFactCollector(mock_module)

# Generated at 2022-06-13 03:25:52.486344
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():

    from ansible.module_utils.facts.collector.service_mgr import ServiceMgrFactCollector
    import pytest

    class MockModule:
        def __init__(self, run_command_func):
            self.run_command_func = run_command_func
        def get_bin_path(self, executable, required=False, opt_dirs=[]):
            if executable in ["systemctl", "launchctl", "systemd-analyze", "systemd-firstboot"]:
                return executable
            return None
        def run_command(self, args, **kwargs):
            return self.run_command_func(args)


# Generated at 2022-06-13 03:26:13.288472
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    # If we cannot import distutils, the method will always return False
    try:
        from distutils import spawn
    except ImportError:
        assert ServiceMgrFactCollector.is_systemd_managed(None) is False
        return

    class FakeModule:

        def get_bin_path(self, command):
            return '/usr/bin/' + command

    module = FakeModule()

    assert ServiceMgrFactCollector.is_systemd_managed(module) is False

    class FakeOs:
        def islink(path):
            return path == '/sbin/init'

        def readlink(path):
            return 'systemd'

        class Error:
            errno = os.errno.ENOENT

        def path(self, *args):
            raise FakeOs.Error

    os.path = FakeOs()



# Generated at 2022-06-13 03:26:15.891666
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    assert ServiceMgrFactCollector.is_systemd_managed_offline(None) == False

# Generated at 2022-06-13 03:26:24.651818
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    from ansible.module_utils.facts import Facts

    test_platform = platform.system()
    test_distribution = platform.dist()[0]
    if test_platform == 'SunOS':
        test_platform = 'Solaris'

    fake_module = Facts(dict(
        ansible_facts=dict(
            ansible_system=test_platform,
            ansible_distribution=test_distribution,
        )
    ))

    collector = ServiceMgrFactCollector()
    expected = collector.is_systemd_managed(module=fake_module)
    actual = collector.is_systemd_managed_offline(module=fake_module)

    assert actual == expected, 'Expected: %s, actual: %s' % (expected, actual)

# Generated at 2022-06-13 03:26:27.172649
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    # initialize a module class to test ServiceMgrFactCollector.is_systemd_managed_offline
    module = AnsibleModule(argument_spec={})
    ServiceMgrFactCollector.is_systemd_managed_offline(module)



# Generated at 2022-06-13 03:26:36.287856
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    ServiceMgrFactCollector_collect_mock = ServiceMgrFactCollector()

    # Mocking real methods and properties of class ServiceMgrFactCollector
    # and its parent class BaseFactCollector
    from ansible.module_utils.facts.collector import BaseFactCollector

    BaseFactCollector_collect_mock = MagicMock(return_value=dict())
    BaseFactCollector_collect_mock.__name__ = 'BaseFactCollector.collect'
    ServiceMgrFactCollector_collect_mock.collect = BaseFactCollector_collect_mock

    ServiceMgrFactCollector_is_systemd_managed_mock = MagicMock(return_value=False)

# Generated at 2022-06-13 03:26:47.033868
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts import ansible_collector
    import ansible.module_utils.facts.system.service_mgr as service_mgr
    import ansible.module_utils.facts.system.service_mgr as serv_mgr
    from ansible.module_utils._text import to_native
    from ansible.module_utils.facts.utils import get_file_content
    from ansible.module_utils.facts.collector import BaseFactCollector
    import ansible.module_utils.facts.collector as col

    # initialize fact_collector with this class
    service_mgr_col = ServiceMgrFactCollector()

    # create temporary folder and file
    proc_1_path = '/proc/1/comm'
    proc

# Generated at 2022-06-13 03:26:53.349350
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts import ModuleFactCollector

    # Case: Systemd detected
    mock_module = MockAnsibleModule(dict(ansible_servicemgr='systemd'))
    assert ServiceMgrFactCollector.is_systemd_managed(module=mock_module)

    # Case: Systemd not detected
    mock_module = MockAnsibleModule(dict())
    assert not ServiceMgrFactCollector.is_systemd_managed(module=mock_module)

    # Case: Systemd detected
    mock_module = MockAnsibleModule(dict(ansible_servicemgr='bsdinit'))
    assert not ServiceMgrFactCollector.is_systemd_managed(module=mock_module)


# Generated at 2022-06-13 03:26:55.682315
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    class ModuleMock(object):
        @staticmethod
        def get_bin_path(path):
            return True

    collector = ServiceMgrFactCollector()

    module_mock = ModuleMock()
    assert collector.is_systemd_managed(module_mock) == False


# Generated at 2022-06-13 03:27:05.879015
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    class Module:
        def get_bin_path(self, path):
            if path == 'systemctl':
                return '/usr/bin/systemctl'

    class CollectedFacts:
        def __init__(self, platform, distribution):
            self.facts = { 'ansible_system': platform,
                           'ansible_distribution': distribution}

    class CollectedFacts_Solaris(CollectedFacts):
        def __init__(self, platform, distribution):
            super(CollectedFacts_Solaris, self).__init__(platform, distribution)
            self.facts['ansible_system'] = 'SunOS'

    # Test: platform: Fedora, distribution: Fedora
    module = Module()
    collected_facts = CollectedFacts('Linux', 'Fedora')

# Generated at 2022-06-13 03:27:18.619375
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():

    class MockModule(object):
        def __init__(self):
            self.run_command_return_value = (1, 'command standard output', 'command standard error')
            self.get_bin_path_return_value = None

        def get_bin_path(self, executable):
            return self.get_bin_path_return_value

        def run_command(self, command, use_unsafe_shell=True):
            return self.run_command_return_value

    class MockFacts(object):
        def __init__(self):
            self._dict = {}

        def get(self, key, default=None):
            return self._dict.get(key, default)

        def setdefault(self, key, value):
            return self._dict.setdefault(key, value)


# Generated at 2022-06-13 03:27:53.479927
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.utils import mock_module
    from ansible.module_utils.facts.collector import Bas

# Generated at 2022-06-13 03:28:04.869038
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():

    # Test: create collector instance
    service_mgr_fact_collector = ServiceMgrFactCollector()
    assert service_mgr_fact_collector is not None

    # Test: create a custom class for module_utils.facts
    class CustomModuleUtilsFacts(object):
        def __init__(self, value):
            self.value = [value]

        def get(self, name, default=None):
            return self.value

        def setdefault(self, name, default=None):
            return self.value

    # Test: verify that method collect() correctly identifies upstart as the service manager
    module_utils_facts = CustomModuleUtilsFacts(None)
    module_utils_facts = service_mgr_fact_collector.collect(module_utils_facts)

# Generated at 2022-06-13 03:28:06.890083
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    import ansible.module_utils.facts.collectors.service_mgr as module_service_mgr
    assert(module_service_mgr.ServiceMgrFactCollector.is_systemd_managed('module') == False)


# Generated at 2022-06-13 03:28:11.814054
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    import sys
    if sys.hexversion < 0x2070000:
        import imp
        import ansible.module_utils.facts.collectors
        ServiceMgrFactCollector = imp.load_source('ServiceMgrFactCollector', 'ansible/module_utils/facts/collectors/service_mgr.py').ServiceMgrFactCollector
    else:
        from ansible.module_utils.facts.collectors import ServiceMgrFactCollector

    class Module(object):
        class RunCommandError(Exception):
            pass

        def __init__(self, use_unsafe_shell=True):
            self.use_unsafe_shell = use_unsafe_shell
            self.exec_path_cache = {}


# Generated at 2022-06-13 03:28:17.771254
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    # Test data
    p = ServiceMgrFactCollector()
    module = type('', (), {'get_bin_path': lambda self, arg: arg})()
    collected_facts = {'ansible_system': ''}
    # Mock
    def run(module, command, use_unsafe_shell=False):
        return (0, '', '')
    module.run_command = run
    def get_file_content(path):
        return 'test'
    module.get_file_content = get_file_content
    def is_systemd_managed(module):
        return True
    module.is_systemd_managed = is_systemd_managed
    # Run method
    ret = p.collect(module=module, collected_facts=collected_facts)
    # Check result

# Generated at 2022-06-13 03:28:24.867597
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    import sys
    import os
    import shutil
    try:
        os.mkdir('/run')
        os.mkdir('/run/systemd')
        os.mkdir('/run/systemd/system')
        os.mkdir('/dev/.run')
        os.mkdir('/dev/.run/systemd')
        os.mkdir('/dev/.systemd')
        if ServiceMgrFactCollector.is_systemd_managed():
            sys.exit(0)
        sys.exit(1)
    finally:
        shutil.rmtree('/run')
        shutil.rmtree('/dev/.run')
        shutil.rmtree('/dev/.systemd')

# Generated at 2022-06-13 03:28:26.312627
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    module = None
    collector = ServiceMgrFactCollector()
    assert collector.is_systemd_managed(module) == False


# Generated at 2022-06-13 03:28:37.156630
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    import ansible.module_utils.facts.collectors.service_mgr as service_mgr_collector
    import ansible.module_utils.facts.collectors.service_mgr as service_mgr_collector
    module = ansible.module_utils.facts.collectors.service_mgr.ServiceMgrFactCollector()

    class TestModule():
        def get_bin_path(self, path):
            if path == 'systemctl':
                return '/bin/systemctl'
            else :
                return None

    class TestModuleWithoutSystemctl():
        def get_bin_path(self, path):
            if path == 'systemctl':
                return ''
            else :
                return None

    assert service_mgr_collector.ServiceMgrFactCollector.is_systemd_managed(TestModule)
   

# Generated at 2022-06-13 03:28:42.764523
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    import sys
    from ansible.module_utils.facts.collector.service_mgr import ServiceMgrFactCollector
    from ansible.module_utils.facts.collector.service_mgr import is_systemd_managed_offline
    from ansible.module_utils.six.moves import mock

    class ModuleMock(object):
        def __init__(self):
            self.path = sys.path

        def get_bin_path(self, path):
            return '/bin/' + path

    module = ModuleMock()

    ServiceMgrFactCollector._is_systemd_managed_offline = is_systemd_managed_offline
    result = ServiceMgrFactCollector._is_systemd_managed_offline(module)


# Generated at 2022-06-13 03:28:51.378169
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    import ansible.module_utils.basic
    import os
    import tempfile
    import shutil

    class TestModule(ansible.module_utils.basic.AnsibleModule):
        pass

    class TestServiceMgrFactCollector():
        @staticmethod
        def get_bin_path(name):
            return None

    test_dir = tempfile.mkdtemp()

# Generated at 2022-06-13 03:30:16.950951
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    collector = ServiceMgrFactCollector()

    module = AnsibleModuleMock()
    module.get_bin_path.return_value = True
    assert collector.is_systemd_managed_offline(module)

    module = AnsibleModuleMock()
    module.get_bin_path.return_value = None
    assert not collector.is_systemd_managed_offline(module)

    # Test that method returns False if os.readlink fails
    module = AnsibleModuleMock()
    module.get_bin_path.return_value = True
    os.readlink = lambda path: None
    assert not collector.is_systemd_managed_offline(module)



# Generated at 2022-06-13 03:30:24.377726
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    from ansible.module_utils import facts

    class MockModule:
        def __init__(self, use_unsafe_shell=False, rc=0, stdout=None):
            self.use_unsafe_shell = use_unsafe_shell
            self.rc = rc
            self.stdout = stdout

        def run_command(self, cmd, use_unsafe_shell=False):
            self.use_unsafe_shell = use_unsafe_shell
            return self.rc, self.stdout, ""

        def get_bin_path(self, prog):
            if prog == "initctl":
                if os.path.exists('/sbin/initctl'):
                    return '/sbin/initctl'

# Generated at 2022-06-13 03:30:28.447187
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():

    from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector

    class FakeModule(object):
        def run_command(self, cmd, use_unsafe_shell=False):
            return (0, '', '')

        def get_bin_path(self, name):
            return "/bin/{0}".format(name)

    assert ServiceMgrFactCollector.is_systemd_managed(FakeModule()) == True


# Generated at 2022-06-13 03:30:31.665304
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():

    tested_fact_collector = ServiceMgrFactCollector()
    # collected_facts = None
    collected_facts = {}

    # result of method collect (this should be a dict)
    result = tested_fact_collector.collect(module=None, collected_facts=collected_facts)

    assert result is not None
    assert len(result) > 0
    assert 'service_mgr' in result



# Generated at 2022-06-13 03:30:34.303426
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():

    class MockModule(object):
        def get_bin_path(self, path):
            # make this always return a path
            return '/bin/' + path

    module = MockModule()

    assert ServiceMgrFactCollector.is_systemd_managed(module) == True

# Generated at 2022-06-13 03:30:36.851883
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts import DefaultCollector
    module = AnsibleModule()
    DefaultCollector.collect(module=module)

    sm = ServiceMgrFactCollector()
    assert sm.is_systemd_managed(module=module) is True

# Generated at 2022-06-13 03:30:40.982764
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    module = MagicMock()

    collector = ServiceMgrFactCollector()
    facts = collector.collect(module=module, collected_facts={'ansible_distribution': 'OpenWrt'})

    assert facts == {'service_mgr': 'openwrt_init'}

# Generated at 2022-06-13 03:30:50.329673
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    # Modules that are being used
    import ansible.module_utils.facts.collector

    # Module import plugin to be tested
    # test_obj = ansible.module_utils.facts.collector.ServiceMgrFactCollector()
    test_obj = ServiceMgrFactCollector()

    # Arguments required for the function that is being tested
    # To be filled with dummy values
    module_argument = None

    # Loop through all return values from the function being tested
    # Move this line out of the function being test to use as global variable
    test_cases_for_function = []

    for curr_retured_value in test_cases_for_function:
        error_thrown = False

# Generated at 2022-06-13 03:30:58.229912
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    # monkeypatch get_bin_path function of module
    def get_bin_path_function_monkeypatch(arg):
        if (arg == "systemctl"):
            return True
        return False

    def os_path_islink_function_monkeypatch(arg):
        if (arg == "/sbin/init"):
            return True
        return False

    def os_readlink_function_monkeypatch(arg):
        if (arg == "/sbin/init"):
            return "systemd"
        return arg

    # monkeypatch module class to return a mock value for get_bin_path function
    ServiceMgrFactCollector.module.get_bin_path = get_bin_path_function_monkeypatch
    ServiceMgrFactCollector.os.path.islink = os_path_islink_function_monkeypatch
   

# Generated at 2022-06-13 03:31:05.623777
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    '''Unit test for method collect of class ServiceMgrFactCollector.'''

    # The mock_module fixture is not included in this module. We will
    # mock the module ourselves.
    import ansible.module_utils.facts.system.service_mgr

    module = ansible.module_utils.facts.system.service_mgr.AnsibleModule(
        argument_spec={},
    )

    module.run_command = lambda x: None

    # Mock the service_mgr method of the ServiceMgrFactCollector class.
    import ansible.module_utils.facts.system.service_mgr

    # Mock some return values, so a check can be performed whether the
    # method collect() uses the mocked return values.