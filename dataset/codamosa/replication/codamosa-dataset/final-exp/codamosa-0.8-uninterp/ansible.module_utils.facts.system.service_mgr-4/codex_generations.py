

# Generated at 2022-06-13 03:23:01.089103
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    ServiceMgrFactCollector().collect()

# Generated at 2022-06-13 03:23:12.716526
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():

    import mock
    from ansible.module_utils import basic
    from ansible.module_utils.facts import collector

    # Create mock module
    mock_module = mock.MagicMock(
        get_bin_path=lambda *args, **kwargs: '/bin/systemctl',
        fail_json=basic.fail_json
    )

    mock_module.run_command.return_value = (0, 'foo\nbar\n', '')


# Generated at 2022-06-13 03:23:20.710654
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    import sys
    import unittest
    import ansible.module_utils.facts.collector

    # Create a mock module for testing
    class MockModule:
        def get_bin_path(self, executable):
            return executable if executable == "systemctl" else None

    # Create a mock thing for open()
    class MockOpen:
        def __init__(self, files, read_content=None):
            self.files = files
            self.read_content = read_content

        def __call__(self, fname, flags):
            self.fname = fname
            self.flags = flags
            return self

        def read(self):
            return self.read_content

        def __exit__(self, type, value, traceback):
            pass

        def __enter__(self):
            return self


# Generated at 2022-06-13 03:23:27.825742
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    class MockModule:
        class MockDistro:
            @staticmethod
            def get_distribution_info():
                return ('Linux', '', '')

        @staticmethod
        def get_bin_path(value):
            return 'mock_bin_path'

        def run_command(self, value, use_unsafe_shell):
            return 0, '', ''

    file_content = 'mock_file_content'
    module = MockModule()

    ServiceMgrFactCollector.is_systemd_managed = lambda module: True
    facts_dict = ServiceMgrFactCollector.collect(module)
    assert facts_dict['service_mgr'] == 'systemd'

    ServiceMgrFactCollector.is_systemd_managed = lambda module: False
    ServiceMgrFactCollector.is_systemd_

# Generated at 2022-06-13 03:23:36.310888
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    in_data = {
        '/run/systemd/system': True,
        '/dev/.run/systemd': True,
        '/dev/.systemd': True,
        '/run/something/other': False
    }
    out_data = {
        '/run/systemd/system': True,
        '/dev/.run/systemd': True,
        '/dev/.systemd': True,
        '/run/something/other': False
    }
    from ansible.module_utils import basic
    m = basic.AnsibleModule(argument_spec={})
    for k, v in in_data.items():
        m.paramiko_conn = None
        def get_bin_path(path):
            if path == 'systemctl' and v: return '/bin/systemctl'
            return None
        m.get_bin_

# Generated at 2022-06-13 03:23:46.006103
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts.collector.service_mgr import ServiceMgrFactCollector

    def mock_get_bin_path(name):
        return '/bin/%s' % name

    class MockModule(object):
        def get_bin_path(self, name):
            return mock_get_bin_path(name)

        def run_command(self, command, use_unsafe_shell=True):
            pass

    def mock_exists(path):
        return path == '/run/systemd/system/'

    module = MockModule()
    srv = ServiceMgrFactCollector()
    srv.is_systemd_managed = mock_systemd_managed

    assert srv.is_systemd_managed(module) is True

    def mock_systemd_managed(module):
        return

# Generated at 2022-06-13 03:23:56.891106
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():

    import ansible.module_utils.facts.collector.service_mgr as mod_servmgr
    import ansible.module_utils.facts.collector as mod_factcollector

    test_g_module_class = MockModule('mock_module')
    test_g_module_class.run_command.return_value = (0, 'mock output 1', 'mock output 2')
    test_g_module_class.get_bin_path.return_value = True

    test_g_base_class = MockBaseFactCollector()

    test_g_distro_class = MockDistributionFactCollector()
    test_g_distro_class.collect.return_value = {'distribution': 'mock distribution', 'platform': 'mock platform'}

    test_g_platform_class = MockPlatformFact

# Generated at 2022-06-13 03:24:03.726799
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    import ansible.module_utils.facts.collectors.service_mgr as service_mgr
    # Function is_systemd_managed returns true when it's able to find in
    # /run/systemd/system, /dev/.run/systemd/ and /dev/.systemd/
    assert service_mgr.ServiceMgrFactCollector.is_systemd_managed({'get_bin_path': lambda path: path, 'run_command': lambda path: [0, '', '']})
    # Function is_systemd_managed returns false when it's unable to find in
    # /run/systemd/system, /dev/.run/systemd/ and /dev/.systemd/

# Generated at 2022-06-13 03:24:07.417732
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():

    import mock

    m = mock.Mock()
    m.get_bin_path.return_value = '/bin/systemctl'

    smfc = ServiceMgrFactCollector()
    assert smfc.is_systemd_managed(m) is True


# Generated at 2022-06-13 03:24:14.263724
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    from ansible.module_utils.facts.collector import MockModule
    from ansible.module_utils.basic import AnsibleModule

    mod = MockModule(argument_spec={})
    mod.run_command = lambda cmd: (1, "/usr/bin/systemd", "")
    collector = ServiceMgrFactCollector()
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )
    module.get_bin_path = mod.get_bin_path
    result = collector.is_systemd_managed_offline(module)
    assert result is True

# Generated at 2022-06-13 03:24:35.520696
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    # Test parameters and expected results.
    test_data = {
        'systemctl_path': False,
        'run_command_result': [0, 'Red Hat', ''],
        'run_command_failure': False,
        'system_canaries_exist': False,
        'is_systemd_managed': False,
    }

    fail_str = "Failure: ServiceMgrFactCollector.is_systemd_managed()"

    # Test the following parameters are acceptable.
    # test_data['systemctl_path'] = True
    # test_data['system_canaries_exist'] = True
    # test_data['run_command_result'] = [0, 'systemd-sysv', '']
    # test_data['run_command_result'] = [0, 'systemd-sysv', '']


# Generated at 2022-06-13 03:24:41.924132
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():

    class MockModule(object):
        def __init__(self):
            self.systemctl = '/bin/systemctl'
            self.run_command = MockModule.run_command
        @staticmethod
        def run_command(command, use_unsafe_shell=True):
            return [0, 'sbin/systemd', '']

    module = MockModule()

    service_mgr = ServiceMgrFactCollector()
    assert service_mgr.is_systemd_managed(module)


# Generated at 2022-06-13 03:24:50.161483
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    # Unit test for not Linux
    import platform
    platform_system = platform.system
    platform.system = lambda: 'FreeBSD'
    assert ServiceMgrFactCollector.collect().get('service_mgr') is None
    platform.system = platform_system

    # Unit test for Linux
    import platform
    import unittest.mock
    from ansible.module_utils.facts.collector import BaseFactCollector
    platform_system = platform.system
    platform.system = lambda: 'Linux'
    service_mgr_collector = ServiceMgrFactCollector()
    with unittest.mock.patch.object(BaseFactCollector, 'collect') as mock_collect:
        mock_collect.return_value = {'ansible_system': 'Linux'}

# Generated at 2022-06-13 03:24:55.403666
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    import sys
    import types
    import os

    class FakeModule:
        def get_bin_path(self, executable):
            return '/bin/systemctl'

    module = FakeModule()

    class FakeSys:
        def __getitem__(self, key):
            if key == 0:
                return os.path.join(os.path.sep, 'sbin', 'init')
            else:
                return None

    sys = FakeSys()

    class FakeSbin:
        def __getitem__(self, key):
            if key == 1:
                return os.path.join(os.path.sep, 'sbin')
            else:
                return None

    os.path.sep = '/'
    os.sep = '/'

    os.path.join = lambda a, b: '/'.join

# Generated at 2022-06-13 03:25:05.988664
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    """
    Test if is_systemd_managed() method of class ServiceMgrFactCollector
    returns expected results
    """
    # Mock a module object
    class AnsibleModuleMock(object):
        def __init__(self):
            self.run_command = None

        def get_bin_path(self, command):
            """
            Returns parameter command if the mock object is not initialized
            Returns the value of self.run_command if the mock object is initialized
            """
            if self.run_command is None:
                return command
            else:
                return self.run_command

    def mock_run_command(command):
        """
        Mocks the output of the command "systemctl is-system-running"
        used by the is_systemd_managed() method
        """

# Generated at 2022-06-13 03:25:18.132574
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    import os
    import shutil
    import tempfile
    import unittest
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.common.process import get_bin_path
    from ansible.module_utils.facts.collector import BaseFactCollector

    class FakeModule:
        def __init__(self):
            FakeModule.bin_path = None
            FakeModule.os = os

        def get_bin_path(self, executable, required=False, opt_dirs=None):
            return FakeModule.bin_path

    class FakeBaseFactCollector(BaseFactCollector):
        def __init__(self):
            super(FakeBaseFactCollector, self).__init__()
           

# Generated at 2022-06-13 03:25:23.467789
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    from ansible.module_utils.facts.collector import ServiceMgrFactCollector
    from ansible.module_utils.facts.module_utils.module import AnsibleModule

    fake_module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode=True
    )
    fake_module.run_command = lambda *args, **kwargs: (0, 'systemd\n', '')

    collector = ServiceMgrFactCollector()

    # check that the method returns the expected boolean value
    assert collector.is_systemd_managed_offline(fake_module)

# Generated at 2022-06-13 03:25:34.954946
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    class MockModule(object):
        def __init__(self, bin_path):
            self.bin_path = bin_path

        def get_bin_path(self, cmd):
            return self.bin_path
    module = MockModule('/usr/bin/systemctl')

    if os.path.islink('/sbin/init'):
        os.unlink('/sbin/init')
    assert not ServiceMgrFactCollector.is_systemd_managed_offline(module=module)

    if not os.path.islink('/sbin/init'):
        os.symlink('/bin/true', '/sbin/init')
    assert not ServiceMgrFactCollector.is_systemd_managed_offline(module=module)

    os.unlink('/sbin/init')
   

# Generated at 2022-06-13 03:25:45.970069
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():

    from ansible.module_utils.facts import ModuleStub, ansible_facts
    from ansible.module_utils.facts.collector.service_mgr import ServiceMgrFactCollector

    in_memory_facts = ansible_facts()

    class CollectFactsModule(object):
        def __init__(self, facts=None, *args, **kwargs):
            self.facts = facts or {}
            self.params = {}

        def run_command(self, command, *args, **kwargs):
            return [0, '/sbin/init', '']

        def get_bin_path(self, command, *args, **kwargs):
            return None

    module = CollectFactsModule(in_memory_facts)

    out_memory_facts = {'ansible_distribution': 'macOS'}
    result

# Generated at 2022-06-13 03:25:50.296962
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    def is_systemd_managed_fake(m):
        return 'systemd_test'
    ServiceMgrFactCollector.is_systemd_managed = is_systemd_managed_fake
    f = ServiceMgrFactCollector()
    assert f.collect().get('service_mgr') == 'systemd_test'
    del ServiceMgrFactCollector.is_systemd_managed


# Generated at 2022-06-13 03:26:21.558845
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    from ansible.module_utils.facts.collector import BaseFactCollector

    from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector
    from ansible.module_utils.facts import ModuleFacts, ModuleFiles, SystemFacts

    module = ModuleFacts(
        os.environ['_ANSIBLE_TEST_MODULE_NAME'],
        '/tmp/ansible_facts',
        ModuleFiles(None),
        SystemFacts(None),
        False
    )

    # Test 1: /sbin/init is not a symlink
    module.paths.add('/sbin/init')
    assert not ServiceMgrFactCollector.is_systemd_managed_offline(module)

    # Test 2: /sbin/init is a symlink but does not point

# Generated at 2022-06-13 03:26:28.579667
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    class ModuleMock(object):
        def __init__(self):
            self.bin_paths = {}

        def get_bin_path(self, executable, required=False, opt_dirs=None):
            return self.bin_paths.get(executable, None)

        def run_command(self, executable, use_unsafe_shell=True):
            return (0, None, None)

    module = ModuleMock()
    smfc = ServiceMgrFactCollector()

    # Should return as True only if systemctl path exists
    module.bin_paths['systemctl'] = None
    for canary in ["/run/systemd/system/", "/dev/.run/systemd/", "/dev/.systemd/"]:
        assert not smfc.is_systemd_managed(module)
        os.maked

# Generated at 2022-06-13 03:26:37.086375
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    module = AnsibleModule(argument_spec=dict())
    service_mgr_collector = ServiceMgrFactCollector()
    assert service_mgr_collector.is_systemd_managed_offline(module) == False

    class MockModule:
        def __init__(self):
            self.params = {}

        def get_bin_path(self, command):
            if command != 'systemctl':
                raise Exception('Unexpected call of get_bin_path with %s' % command)
            return "systemctl"

    module = MockModule()
    service_mgr_collector = ServiceMgrFactCollector()
    assert service_mgr_collector.is_systemd_managed_offline(module) == False

    class MockModule:
        def __init__(self):
            self.params = {}



# Generated at 2022-06-13 03:26:45.801530
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    fake_module = FakeAnsibleModule()
    fact_collector = ServiceMgrFactCollector()

    # test success
    fake_module.readlink_returns = "systemd"
    assert fact_collector.is_systemd_managed_offline(fake_module)

    # test fail
    fake_module.readlink_returns = "not-systemd"
    assert not fact_collector.is_systemd_managed_offline(fake_module)

    fake_module.readlink_returns = None
    assert not fact_collector.is_systemd_managed_offline(fake_module)


# Generated at 2022-06-13 03:26:53.935354
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    import os
    import tempfile
    import shutil

    import ansible.module_utils.facts.collector as service_mgr_collector

    tmp_dir = tempfile.mkdtemp(prefix='ansible_test_service_mgr')
    test_init = os.path.join(tmp_dir, 'init')

    print(tmp_dir)

    _, path = tempfile.mkstemp()
    os.write(1, '#!/bin/sh\nwhile true; do sleep 1; done\n'.encode('utf-8'))
    os.close(1)
    os.chmod(path, 0o700)
    os.rename(path, test_init)

    # Check result with test_init and without

# Generated at 2022-06-13 03:27:04.514821
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    import ansible.module_utils.facts.service_mgr
    import ansible.module_utils.pycompat24
    import ansible.module_utils.urls

    class DummyModule(object):
        def __init__(self):
            self.params = dict()
            self.fail_json = None

        def get_bin_path(self, name):
            if name == 'systemctl':
                return '/bin/systemctl'
            else:
                return None

    module = DummyModule()

    assert not ServiceMgrFactCollector.is_systemd_managed(module)

    def get_file_content_side_effect(path):
        if path == '/proc/1/comm':
            return 'systemd'


# Generated at 2022-06-13 03:27:14.724630
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():

    import ansible.module_utils.facts
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.collectors
    import ansible.module_utils.facts.collectors.service_mgr

    import mock

    mock_module = mock.Mock()
    mock_module.get_bin_path.return_value = '/sbin/init'

    fact_collector = ansible.module_utils.facts.collectors.service_mgr.ServiceMgrFactCollector
    result = fact_collector.is_systemd_managed_offline(module=mock_module)

    assert 'systemd' in result

# Generated at 2022-06-13 03:27:25.221406
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector

    class MockModule:
        def get_bin_path(self, cmd):
            if cmd == "systemctl":
                return "/bin/systemctl"
            return None

    module = MockModule()
    service_mgr_collector = ServiceMgrFactCollector()

    assert not service_mgr_collector.is_systemd_managed_offline(module)

    # Create symlinks
    os.symlink("systemd", "/sbin/init")

    assert service_mgr_collector.is_systemd_managed_offline(module)

    # Cleanup
    os.remove("/sbin/init")


# Generated at 2022-06-13 03:27:32.230868
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    '''Unit test for method collect of class ServiceMgrFactCollector'''
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils._text import to_bytes
    import os

    class MockModule(object):
        def __init__(self):
            self.run_command = lambda x, y: (0, to_bytes(os.readlink('/sbin/init')), '')
            self.get_bin_path = lambda x: '/bin/systemctl'
    class MockFacts(object):
        def __init__(self):
            self.collector = {'ansible_distribution': 'OpenWrt', 'ansible_system': 'Linux'}

    ServiceMgrFactCollector._fact_ids.clear()
    facts = ServiceMgrFactCollector

# Generated at 2022-06-13 03:27:43.186389
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    import mock
    import tempfile
    import shutil

    # Creates a mock module with a specific file system structure
    #
    #    /run/systemd/system/   -> no system directory
    #    /dev/.run/systemd/     -> no system directory
    #    /dev/.systemd/          -> no system directory
    #    /non-existent-directory -> no system directory
    file_system = {
        '/run/systemd/system': False,
        '/dev/.run/systemd': False,
        '/dev/.systemd': False,
        '/non-existent-directory': False
    }

    def mock_walk(path):
        dirs = []
        if file_system.get(path, True):
            dirs.append((path, [], []))
        return dirs


# Generated at 2022-06-13 03:28:11.252663
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    # create instance and test
    ServiceMgrFactCollector()

# Generated at 2022-06-13 03:28:17.422017
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    from ansible.module_utils import basic
    from ansible.module_utils.facts.collector import BaseFactCollector
    import ansible.module_utils.facts.collectors.service_mgr
    import os

    collector = ansible.module_utils.facts.collectors.service_mgr.ServiceMgrFactCollector()

    # Create a fake module class instance which can be used to call the static method.
    module = basic.AnsibleModule(argument_spec={})

    # /sbin/init is a symlink to systemd
    os.symlink('/bin/systemd', '/sbin/init')
    assert collector.is_systemd_managed_offline(module)

    # /sbin/init is not a symlink to systemd

# Generated at 2022-06-13 03:28:22.113864
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    '''
    Test for method is_systemd_managed_offline of class ServiceMgrFactCollector
    '''
    test_module = MockModule(dict())
    fact_collector = ServiceMgrFactCollector()
    expected_result = False
    actual_result = fact_collector.is_systemd_managed_offline(test_module)
    assert actual_result == expected_result



# Generated at 2022-06-13 03:28:28.630253
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    from ansible.module_utils.facts import collector

    # Specify the service manager name
    service_mgr = 'systemd'

    # Replace the existing service manager collector with a new class
    # Use service_mgr as the name
    class TestServiceMgrFactCollector(ServiceMgrFactCollector):
        name = service_mgr
        fact_ids = set()

        # Override the collect method of the class
        @staticmethod
        def collect(module=None, collected_facts=None):
            collected_facts[service_mgr] = 'systemd'

    # Add this new class to the service manager collectors
    collector.add_collector(TestServiceMgrFactCollector)

    # Create a fake module to be used by the is_systemd_managed_offline method
    # Only the get_bin_path is

# Generated at 2022-06-13 03:28:38.618770
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    collector = ServiceMgrFactCollector()
    # The following file is used for testing, add your own OS specific files
    # for testing and add some code to the unit test accordingly

# Generated at 2022-06-13 03:28:43.557455
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    # Import and setup required modules
    module_args = dict()

    import ansible.module_utils.facts.collector.base
    import ansible.module_utils.facts.collector.service_mgr

    import os
    import sys
    import tempfile
    import shutil

    # Setup initial test environment
    tmpdir = tempfile.mkdtemp()
    test_dirs = [
        tmpdir,
        os.path.join(tmpdir, "bin"),
        os.path.join(tmpdir, "run", "systemd"),
        os.path.join(tmpdir, "dev", ".run", "systemd"),
        os.path.join(tmpdir, "dev", ".systemd"),
    ]


# Generated at 2022-06-13 03:28:48.041137
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    # pylint: disable=protected-access
    c = ServiceMgrFactCollector()
    # Test if the methods have the required attributes
    assert c.required_facts == set(['platform', 'distribution'])
    assert c.name == 'service_mgr'
    assert c._fact_ids == set()
    assert c.collect_once is False

# Generated at 2022-06-13 03:28:57.386290
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    import tempfile
    import shutil

    # Prepare a fake system at temporary directory
    tempdir = tempfile.mkdtemp()
    # Create fake symlink /sbin/init to systemd
    systemd_symlink = os.path.join(tempdir, 'systemd')
    os.symlink(systemd_symlink, os.path.join(tempdir, 'sbin', 'init'))

    # Create a mock module
    import ansible.module_utils.basic
    m = ansible.module_utils.basic.AnsibleModule(argument_spec={})
    # Add fake pathes to module
    m.get_bin_path = lambda x : os.path.join(tempdir, x)

    # Perform test
    from ansible.module_utils.facts.system.service_mgr import ServiceM

# Generated at 2022-06-13 03:29:03.513627
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.system.service_mgr

    collector = ansible.module_utils.facts.collector.get_collector(ansible.module_utils.facts.system.service_mgr.ServiceMgrFactCollector.name)
    assert isinstance(collector, ansible.module_utils.facts.system.service_mgr.ServiceMgrFactCollector)
    assert collector.is_systemd_managed_offline(None) == False

# Generated at 2022-06-13 03:29:09.341857
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collectors import network

    class TestModule:
        def __init__(self, path):
            self.path = path

        def get_bin_path(self, cmd):
            """ Return the path to a command, or None if not found """
            return self.path


    # test the case where systemd is managing init
    module = TestModule('/bin/systemctl')
    smfc = ServiceMgrFactCollector()
    assert smfc.is_systemd_managed_offline(module=module)

    # test the case where init is managed by upstart
    module = TestModule('/sbin/upstart-udev-bridge')
    smfc = ServiceMgrFactCollector()
    assert not sm

# Generated at 2022-06-13 03:30:20.728383
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    module = AnsibleModuleMock()
    module.get_bin_path.return_value = '/sbin/systemctl'
    sm = ServiceMgrFactCollector()
    os.symlink('/bin/systemd', '/sbin/init')
    assert sm.is_systemd_managed_offline(module)
    os.unlink('/sbin/init')
    assert sm.is_systemd_managed_offline(module) is False
    module.get_bin_path.return_value = None
    assert sm.is_systemd_managed_offline(module) is False
    os.symlink('/bin/systemd', '/sbin/init')
    assert sm.is_systemd_managed_offline(module) is False



# Generated at 2022-06-13 03:30:31.058116
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    import pytest
    from ansible.module_utils.facts.collector import Collector

    # Test with a runit managed service.
    collector = Collector(None)
    runit = ServiceMgrFactCollector(collector)

    with pytest.helpers.mocked_command('ps', stdout='runit-init\n') as mocked_command:
        runit.collect()
        mocked_command.assert_has_calls([])

    assert 'service_mgr' in collector.collector
    assert collector.collector['service_mgr'] == 'runit'

    # Test with a systemd managed system.
    collector = Collector(None)

    systemd = ServiceMgrFactCollector(collector)


# Generated at 2022-06-13 03:30:37.461583
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    import unittest
    from ansible.module_utils.facts.collector import Monger

    class MockModule(object):
        def __init__(self, bin_path):
            self.bin_path = bin_path

        def get_bin_path(self, executable, required=False, opt_dirs=None):
            if executable == 'systemctl':
                return self.bin_path

    class TestServiceMgrFactCollector(unittest.TestCase):
        def test_is_systemd_managed_not_present(self):
            # Test with systemctl not present
            bin_path = None
            module = MockModule(bin_path)
            smfc = ServiceMgrFactCollector()
            self.assertFalse(smfc.is_systemd_managed(module))


# Generated at 2022-06-13 03:30:43.333924
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    tester = ServiceMgrFactCollector()
    tester.collect()

# The following conditional checks if the current file is being executed as the 'main' python script instead of being
# imported as a module. To execute the following code, you can run `python service_mgr.py`. This conditional prevents
# the code to be executed when the associated facts module is imported.

if __name__ == '__main__':
    test_ServiceMgrFactCollector_collect()

# Generated at 2022-06-13 03:30:52.867288
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    from ansible.module_utils.facts.collector.service_mgr import ServiceMgrFactCollector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.six import b
    import json

    # Make a fake module
    class MockModule(object):
        @staticmethod
        def get_bin_path(name, opts=None, required=False):
            if name == "systemctl" and opts is None:
                return "/bin/" + name
            else:
                return None


# Generated at 2022-06-13 03:31:00.194355
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    import ansible.module_utils.facts.collector
    import ansible.module_utils
    import ansible.module_utils.basic

    def RunModuleExec(module):
        args = dict()
        args['module_name'] = "command"
        args['module_args'] = "ls -l"
        args['return_contents'] = "yes"
        args['warnings'] = [ "default" ]
        args['executable'] = 'python'
        return ansible.module_utils.basic.AnsibleModule(**args).run()

    class AnsibleModuleFake:
        def get_bin_path(self, command):
            if command in ['systemctl', 'init']:
                return 'dummy'


# Generated at 2022-06-13 03:31:01.091033
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    ServiceMgrFactCollector.is_systemd_managed_offline(module=None)

# Generated at 2022-06-13 03:31:07.830711
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    from ansible.module_utils import facts
    import ansible.module_utils.facts.collectors.service_mgr as service_mgr
    import ansible.module_utils.facts.collectors.get_distribution as distribution
    import ansible.module_utils.facts.collectors.get_platform as platform

    dist = distribution.DistributionFactCollector()
    dist.collect()
    plt = platform.PlatformFactCollector()
    plt.collect()

    facts_dict = {
        'get_distribution': dist.collect(),
        'get_platform': plt.collect()
    }

    mgr = service_mgr.ServiceMgrFactCollector()
    result = mgr.collect(None, facts_dict)
    assert result['service_mgr']

# Generated at 2022-06-13 03:31:14.296681
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():

    # mock module
    class MockModule(object):
        def __init__(self, command, exists):
            self.command = command
            self.exists = exists

        def get_bin_path(self, executable):
            if self.command == executable and self.exists:
                return executable
            else:
                return None

    # Assertions
    # when tools are installed and the canary file exists
    testModule = MockModule('systemctl', True)
    assert ServiceMgrFactCollector().is_systemd_managed(module=testModule)

    # when tools are not installed
    testModule = MockModule('systemctl', False)
    assert not ServiceMgrFactCollector().is_systemd_managed(module=testModule)

    # when canary file does not exist

# Generated at 2022-06-13 03:31:22.646804
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.collector import BaseFactCollector
    import tempfile

    class MockModule(object):
        def get_bin_path(self, bin_path, required=False, opt_dirs=[]):
            return 'MOCK_BIN_PATH_FOR:' + bin_path

        @staticmethod
        def run_command(command, use_unsafe_shell=True):
            pass

    # Create a temporary directory
    tmpdir = tempfile.mkdtemp()

    # If is_systemd_managed_offline() is called without systemctl,
    # return False
    service_mgr_collector = ServiceMgrFactCollector()