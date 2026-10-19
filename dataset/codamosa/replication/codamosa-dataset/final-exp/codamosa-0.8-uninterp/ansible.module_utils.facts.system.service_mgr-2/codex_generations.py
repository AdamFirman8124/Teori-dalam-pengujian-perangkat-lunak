

# Generated at 2022-06-13 03:23:01.542012
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    module = MockModule()
    facts = {}
    fact_collector = ServiceMgrFactCollector()
    service_mgr = fact_collector.collect(module=module, collected_facts=facts)
    assert service_mgr.get('service_mgr') == 'systemd'

# Generated at 2022-06-13 03:23:13.012390
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    import tempfile
    import shutil
    import stat
    import os

    temp_dir = tempfile.mkdtemp()


# Generated at 2022-06-13 03:23:20.888019
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():

    # Set up a module and its parameters:
    module = AnsibleModule(argument_spec={})

    # Set up a mock return value for method run_command of class AnsibleModule:
    command_results = {}
    command_results['rc'] = 0
    command_results['stdout'] = "systemd"
    command_results['stderr'] = ""
    module.run_command = Mock(return_value=command_results)

    # Set up a mock return value for method get_bin_path of class AnsibleModule:
    module.get_bin_path = Mock(return_value="/bin/systemctl")

    # Run the method collect of class ServiceMgrFactCollector:
    results = ServiceMgrFactCollector.collect(module)

    # Verify the test results:

# Generated at 2022-06-13 03:23:27.985150
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    from ansible.module_utils.facts.collector import ServiceMgrFactCollector

    # Check for actual systemctl executable
    class MockModule(object):
        def __init__(self, executable, basename):
            self.executable = executable
            self.basename = basename

        def get_bin_path(self, executable):
            if executable == self.executable:
                return '/foo/' + self.executable

    module = MockModule('systemctl', 'systemctl')
    assert(ServiceMgrFactCollector.is_systemd_managed_offline(module) is False)

    # Check for broken links
    module.executable = 'foo'
    assert(ServiceMgrFactCollector.is_systemd_managed_offline(module) is False)

    # Check for links that are not broken
    module

# Generated at 2022-06-13 03:23:33.345048
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():

    mock_module = MockModule()

    # The value of /proc/1/comm is busybox.
    mock_comm = MockFile('busybox')

    # The value of the output of the ps command is init.
    mock_ps = MockFile('')

    # The process IDs of the zombie processes is(are) 0.
    mock_ps_zombie = MockFile('0')

    # The value of the output of the df command is init.
    mock_df = MockFile('')

    # The value of /proc/1/comm is init.
    mock_comm_init = MockFile('init')

    # The process IDs of the zombie processes is(are) 0.
    mock_ps_zombie_init = MockFile('0')

    # The value of the output of the ps command is init.
    mock_ps

# Generated at 2022-06-13 03:23:39.807483
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    module = AnsibleModuleMock()
    collector = ServiceMgrFactCollector()
    os.symlink('/usr/lib/systemd/systemd', '/sbin/init')
    assert collector.is_systemd_managed_offline(module)
    os.unlink('/sbin/init')


# Generated at 2022-06-13 03:23:47.362991
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    import sys

    # setup
    platform_fact = {'value': 'Linux'}
    distribution_fact = {'value': 'OpenWrt'}

    # add class to module
    sys.modules['ansible.module_utils.facts.system.service_mgr'] = __import__(
        'ansible.module_utils.facts.system.service_mgr')
    import ansible.module_utils.facts.system.service_mgr

    # setup test values
    module = MockModule()
    collected_facts = {'platform': platform_fact['value'], 'distribution': distribution_fact['value']}

    # create test instance
    service_mgr_fact_collector = ansible.module_utils.facts.system.service_mgr.ServiceMgrFactCollector()

    # test
    service_m

# Generated at 2022-06-13 03:23:53.292165
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collectors.service_mgr import ServiceMgrFactCollector
    # Fake the 'systemctl' command for the test.
    os.environ['PATH'] = '/abc:/usr/bin'

    class FakeModule(object):
        def get_bin_path(self, cmd):
            return '/usr/bin/%s' % cmd
    module = FakeModule()
    sm = ServiceMgrFactCollector()

    os.environ['PATH'] = '/abc:/usr/bin'
    os.makedirs('/run/systemd/system/')
    assert sm.is_systemd_managed(module=module)

    os.makedirs('/dev/.run/systemd/')

# Generated at 2022-06-13 03:24:00.170484
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    import mock

    sha = ServiceMgrFactCollector()

    module = mock.Mock()
    module.get_bin_path.return_value = True

    # systemd is the boot init system
    module.run_command.return_value = (0, '', '')

    assert sha.is_systemd_managed(module)

    # systemd is not the boot init system
    module.run_command.return_value = (1, '', '')

    assert not sha.is_systemd_managed(module)

    module.get_bin_path.return_value = None

    assert not sha.is_systemd_managed(module)


# Generated at 2022-06-13 03:24:05.789121
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():

    def mock_get_bin_path(program):
        if program == "systemctl":
            return program

    def mock_os_path_exists(path):
        if path == "/run/systemd/system/":
            return True
        return False

    from ansible.module_utils import basic
    from ansible.module_utils.facts import collector

    # Test with systemctl available, /run/systemd/system/ exists and /dev/.run/systemd/ does not exist
    mock_module = basic.AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )
    mock_module.get_bin_path = mock_get_bin_path
    mock_module.run_command = lambda x, **kwargs: [0, '', '']
    mock_module.os_path

# Generated at 2022-06-13 03:24:24.319896
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    # Test with systemd being the init
    module = MockModule(
        params=dict(),
        binary_path='/bin/systemctl',
        islink_return_values=[False, False, False],
        exists_return_values=[True, True, True]
    )
    assert ServiceMgrFactCollector.is_systemd_managed(module)

    # Test with systemd not being the init
    module = MockModule(
        params=dict(),
        binary_path='/bin/systemctl',
        exists_return_values=[False, False, False]
    )
    assert not ServiceMgrFactCollector.is_systemd_managed(module)

    # Test without systemctl
    module = MockModule(
        params=dict(),
        binary_path=None
    )
    assert not ServiceMgrFactCollector.is_

# Generated at 2022-06-13 03:24:30.375844
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    """
    Test the method ServiceMgrFactCollector.is_systemd_managed_offline
    """
    from ansible.module_utils.facts.collector import ServiceMgrFactCollector
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.fetch import get_file_content

    test_module = AnsibleModule(
        argument_spec=dict(),
    )

    # Prepare data for tests
    data = dict()
    data['is_systemd_managed_offline_systemd_init_sbin'] = \
        dict(
            test_data_value=(
                "lrwxrwxrwx 1 root root 7 Dec 10 10:48 /sbin/init -> systemd",
                "/sbin/init"
            ),
            expected_return=True
        )
   

# Generated at 2022-06-13 03:24:39.746834
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    import platform
    import ansible.module_utils.facts.system.service_mgr
    service_mgr_facts_collector = ansible.module_utils.facts.system.service_mgr.ServiceMgrFactCollector()

    # When binary is not present and init is not a symlink to systemd, the method should return False.
    mockmodule = MockModule(False)
    service_mgr_facts_collector.is_systemd_managed_offline(mockmodule)
    assert not mockmodule.cmd_executed, "The method should not execute systemctl if it is not present."

    # When binary is present and init is not a symlink to systemd, the method should return False.
    mockmodule = MockModule(True)

# Generated at 2022-06-13 03:24:48.653020
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    test_dir = os.path.dirname(os.path.abspath(__file__))
    sys_utils_dir = os.path.join(test_dir, os.pardir, '../../lib/ansible/module_utils')
    sys_utils_path = os.path.abspath(sys_utils_dir)
    if sys_utils_path not in sys.path:
        sys.path.append(sys_utils_path)
    from ansible.module_utils.basic import AnsibleModule

    def get_bin_path(cmd):
        fake_path = ['/systemd/systemd', '/usr/bin/systemctl']
        for dir in fake_path:
            if cmd in dir:
                return dir


# Generated at 2022-06-13 03:25:00.945842
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collectors.service_mgr import ServiceMgrFactCollector
    import os
    import tempfile
    import shutil
    module_path = None
    try:
        module_path = os.path.join(tempfile.mkdtemp(), 'module')
        os.mkdir(module_path)
        os.symlink('systemd', os.path.join(module_path, 'init'))
        module = BaseFactCollector(module_path=module_path)
        assert ServiceMgrFactCollector.is_systemd_managed_offline(module)
    finally:
        if module_path:
            shutil.rmtree(module_path)


# Generated at 2022-06-13 03:25:06.065249
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    module = mock.MagicMock()
    module.get_bin_path.return_value = True
    os.path.islink.return_value = True
    os.readlink.return_value = "systemd"
    service_mgr_fact = ServiceMgrFactCollector()

    assert service_mgr_fact.is_systemd_managed_offline(module)

# Generated at 2022-06-13 03:25:18.238758
# Unit test for method collect of class ServiceMgrFactCollector

# Generated at 2022-06-13 03:25:24.359219
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():

    # Create a test module object
    from ansible.module_utils.basic import AnsibleModule
    test_module = AnsibleModule
    test_module.get_bin_path = lambda x: '/usr/bin/{0}'.format(x)
    test_module.run_command = lambda x: (0, 'runit', '')

    # Check on systemd
    assert ServiceMgrFactCollector.is_systemd_managed_offline(module=test_module)

    # Check on non-systemd
    test_module.run_command = lambda x: (0, 'openrc-init', '')
    assert not ServiceMgrFactCollector.is_systemd_managed_offline(module=test_module)

# Generated at 2022-06-13 03:25:28.890682
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    class MockedModule:
        def get_bin_path(self, _):
            return "/bin/systemctl"

    mocked_module = MockedModule()
    ServiceMgrFactCollector.is_systemd_managed(mocked_module)


# Generated at 2022-06-13 03:25:31.400918
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    import pytest
    plugin = ServiceMgrFactCollector()

    assert plugin.is_systemd_managed(MockModule()) == True


# Generated at 2022-06-13 03:25:50.029446
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.facts import Facts
    from ansible.module_utils.facts.collectors.service_mgr import ServiceMgrFactCollector
    class MockModule(object):
        def __init__(self):
            self.params = dict()
            self.params['gather_subset'] = []
            self.params['filter'] = None
            self.params['gather_timeout'] = 10
            self.params['_ansible_check_mode'] = False
            self.params['_ansible_no_log'] = False
            self.params['_ansible_debug'] = False
            self.params['_ansible_delegated_vars'] = dict()
            self.params['_ansible_version']

# Generated at 2022-06-13 03:25:55.967589
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():

    class CollectedFacts():
        ansible_system = 'Linux'
        ansible_distribution = 'Linux'

    class module():
        returncode = 0
        err = ''
        args = ''

        def get_bin_path(self, arg):
            if arg == 'initctl':
                return '/sbin/initctl'
            elif arg == 'systemctl':
                return '/bin/systemctl'

        def run_command(self, args, use_unsafe_shell=False):
            command = args.split()[0]
            if command == 'ps':
                if args == 'ps -p 1 -o comm|tail -n 1':
                    self.returncode = 0
                    return self.returncode, 'systemd\n', self.err + '\n'

# Generated at 2022-06-13 03:26:01.847113
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    import mock
    import ansible.module_utils.facts.collector

    module = mock.MagicMock()
    module.get_bin_path = mock.MagicMock(return_value='/bin/systemctl')

    # Mock os.path.exists return values for 'canaries' in for loop
    with mock.patch('os.path.exists',
            side_effect=[False, False, True]) as patch:
        result = ServiceMgrFactCollector.is_systemd_managed(module)

        assert(result == True)


# Generated at 2022-06-13 03:26:07.445169
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    """
    If is_systemd_managed method return True
    service manager must be systemd
    """
    module_mock = MockAnsibleModule(is_systemd_managed=True)
    service_mgr_collector = ServiceMgrFactCollector()

    service_mgr_name = service_mgr_collector.collect(module_mock)['service_mgr']

    assert service_mgr_name == 'systemd'


# Mocked class for test.

# Generated at 2022-06-13 03:26:15.739843
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    import mock
    import json
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts import CoreFactCollector
    from ansible.module_utils.facts.collector.system.service_mgr import ServiceMgrFactCollector

    data = json.load(open(os.path.join(os.path.dirname(__file__), 'fixtures', 'service_mgr.json')))

    # init Collector with all subclasses of BaseFactCollector
    collector = Collector(subclasses=[ServiceMgrFactCollector], callback_facts_cache={})

    def LoadModuleShim(name, *args, **kwargs):
        if name == '_text':
            return mock.Mock(to_native=lambda x: x)

# Generated at 2022-06-13 03:26:24.830828
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():

    from ansible.module_utils.facts.collector import DummyModule

    module = DummyModule()
    collector = ServiceMgrFactCollector()

    # Testing for platform
    module._platform = 'linux'
    assert(collector.is_systemd_managed(module))

    # Testing for platform
    module._platform = 'bsd'
    assert(not collector.is_systemd_managed(module))

    # Testing for platform
    module._platform = 'aix'
    assert(not collector.is_systemd_managed(module))

    # Testing for platform
    module._platform = 'sunos'
    assert(not collector.is_systemd_managed(module))

    # Testing for platform
    module._platform = 'macosx'
    assert(not collector.is_systemd_managed(module))

    #

# Generated at 2022-06-13 03:26:35.414470
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    # Ensure that is_systemd_managed_offline returns False if /sbin/init is not a symlink
    module = FakeModule()
    collector = ServiceMgrFactCollector(module)
    collector.is_systemd_offline = True
    assert collector.is_systemd_managed_offline(module) == False

    # Ensure that is_systemd_managed_offline returns True if /sbin/init is a symlink to systemd
    module = FakeModule()
    collector = ServiceMgrFactCollector(module)
    collector.is_systemd_offline = True
    collector.os_path_islink = MagicMock(return_value=True)
    collector.os_readlink = '/sbin/init'
    assert collector.is_systemd_managed_offline(module) == True

    #

# Generated at 2022-06-13 03:26:46.745756
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts.collector import BaseFactCollector
    import sys

    class BaseFactCollector_dummy(BaseFactCollector):
        def collect(self, module=None, collected_facts=None):
            return {}

    # class ServiceMgrFactCollector_dummy(ServiceMgrFactCollector):
    #     def collect(self, module=None, collected_facts=None):
    #         return {}

    class module_dummy(object):
        def get_bin_path(self, cmd):
            return cmd
        def run_command(self, cmd, use_unsafe_shell=True):
            cmd = cmd.replace('\\', '\\\\')
            cmd = 'import sys; sys.stdout.write(r"{}")'.format(cmd)

# Generated at 2022-06-13 03:26:52.023351
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    # Create a new instance of ServiceMgrFactCollector
    module = AnsibleModuleMock()
    smfc = ServiceMgrFactCollector(module=module)

    # Create a new ansible module instance
    ansible_module_instance = AnsibleModuleMock()

    # Get the facts from ServiceMgrFactCollector
    collected_facts = smfc.collect(module=ansible_module_instance)

    assert collected_facts['service_mgr'] == 'service'


# Generated at 2022-06-13 03:27:02.285700
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    import subprocess
    import tempfile
    import shutil
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collectors.service_mgr import ServiceMgrFactCollector
    base_fact_collector = BaseFactCollector()
    service_mgr_fact_collector = ServiceMgrFactCollector()
    test_dir = tempfile.mkdtemp()
    # create a /sbin/init symlink
    subprocess.check_call(['ln', '-s', 'systemd', os.path.join(test_dir, 'sbin', 'init')])
    # with the given arguments, is_systemd_managed_offline should return False
    assert not service_mgr_fact_collector.is_systemd_managed_offline

# Generated at 2022-06-13 03:27:23.143989
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    def get_bin_path(name, *ignore_args, **ignore_kwargs):
        if name == 'systemctl':
            return True

        return None

    # Test is systemd managed offline if /sbin/init is a symlink to systemd
    def is_systemd_managed_offline(module):
        module.get_bin_path = Mock(side_effect=get_bin_path)
        smfc = ServiceMgrFactCollector()
        return smfc.is_systemd_managed_offline(module=module)

    module = Mock()
    module.get_bin_path = Mock(side_effect=get_bin_path)
    os.path.islink = Mock(return_value=True)
    os.readlink = Mock(return_value='systemd')
    smfc = ServiceMgrFactCollect

# Generated at 2022-06-13 03:27:29.509729
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collectors.service_mgr import ServiceMgrFactCollector

    test_object = Collector()
    test_object.get_bin_path = lambda name: "/bin/{0}".format(name)

    assert(ServiceMgrFactCollector.is_systemd_managed(test_object) == True)


# Generated at 2022-06-13 03:27:40.612645
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    import ansible.module_utils.facts.collector.service_mgr
    import ansible.module_utils.facts.systemd
    import ansible.module_utils.facts.systemd.aureport
    import ansible.module_utils.facts.systemd.audit2why
    import ansible.module_utils.facts.systemd.coredumpctl
    import ansible.module_utils.facts.systemd.dmesg
    import ansible.module_utils.facts.systemd.hwclock
    import ansible.module_utils.facts.systemd.ipcmk
    import ansible.module_utils.facts.systemd.journalctl
    import ansible.module_utils.facts.systemd.ldconfig
    import ansible.module_utils.facts.systemd.localectl

# Generated at 2022-06-13 03:27:50.702517
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    class ModuleMock(object):
        def __init__(self, command_result=(0, '', ''), binary_paths=None):
            self.command_result = command_result
            self.binary_paths = binary_paths or {}

        def get_bin_path(self, key, opt_dirs=[]):
            return self.binary_paths.get(key)

        def run_command(self, cmd, use_unsafe_shell=False):
            return self.command_result

    # Mock facts for system
    platform_facts = {
        'ansible_system': 'Linux',
        'ansible_distribution': 'MacOSX'
    }

    # Happy path test using dummy service_mgr name from OS.

# Generated at 2022-06-13 03:28:01.696615
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    import sys
    import json
    import socket
    import unittest.mock as mock

    class MockModule(object):
        def __init__(self):
            self.params = {}

        def get_bin_path(self, arg):
            if arg == 'systemctl':
                return '/bin/systemctl'
            else:
                return None

        def run_command(self, arg, use_unsafe_shell=False):
            if 'ps -p 1 -o comm|tail -n 1' in arg:
                return (0, '1\n', '')
            elif 'ps -p 1 -o comm' in arg:
                return (0, '1\n', '')
            else:
                return (1, '', '')


# Generated at 2022-06-13 03:28:07.437973
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    ## Test the is_systemd_managed method
    # test positive
    collection = ServiceMgrFactCollector()
    assert 'systemd' == collection.is_systemd_managed(None)
    # test negative
    assert not collection.is_systemd_managed_offline(None)

    # test the collect method
    module = AnsibleModuleMock()
    # return proc_1 as init
    collection = ServiceMgrFactCollector()
    assert 'init' == collection.collect(module)['service_mgr']

    # return proc_1 as openwrt_init
    collection = ServiceMgrFactCollector()
    assert 'openwrt_init' == collection.collect(module, {'ansible_distribution':'OpenWrt'})['service_mgr']

    # return proc_1 as openrc
    collection

# Generated at 2022-06-13 03:28:14.906737
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    import tempfile
    import shutil
    import os
    import sys
    import stat
    import types

    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common._collections_compat import MutableMapping

    # import ansible module utils
    from ansible.module_utils.facts import ModuleUtilsLegacyFactCollector

    # import test specific stuff
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from test_utils import FailingModule

    # copy the module file to be tested
    src =  os.path.join(os.path.dirname(__file__), '..', '..', 'ansible', 'module_utils', 'facts', 'service_mgr.py')

# Generated at 2022-06-13 03:28:24.228065
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    class ModuleMock:
        def get_bin_path(self, executable):
            return None

        def run_command(self, cmd, use_unsafe_shell=True):
            return (0, None, None)

    module = ModuleMock()

    # Return None for not supported platforms
    assert ServiceMgrFactCollector.collect(module=module) is None

    # Return service manager for supported platforms with different tools
    module = ModuleMock()
    module.get_bin_path = lambda _: '/bin/systemctl'
    module.run_command = lambda _, __: (0, "init\n", None)
    assert ServiceMgrFactCollector.collect(module=module)['service_mgr'] == 'systemd'

    module = ModuleMock()

# Generated at 2022-06-13 03:28:24.929818
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    ServiceMgrFactCollector()

# Generated at 2022-06-13 03:28:26.549270
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    collector = ServiceMgrFactCollector(None)
    assert not collector.is_systemd_managed(None)

# Generated at 2022-06-13 03:29:17.619315
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock import MagicMock, patch
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils import basic

    # Construct module_mock
    module_mock = MagicMock()
    module_mock.get_bin_path.return_value = None

    # Construct collected_facts_mock
    collected_facts_mock = dict(ansible_distribution='OpenWrt', ansible_system='Linux')

    # Construct mock to return a specific value
    get_file_content_mock = MagicMock(return_value='openwrt_init')

    # Construct patch to mock function get_file_content

# Generated at 2022-06-13 03:29:24.234187
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():

    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.utils import get_file_content

    # Let's create a fake module mock of the AnsibleModule class.
    fake_module = type('AnsibleModule', (object,), {
        'get_bin_path': classmethod(lambda cls, _: '/usr/bin/systemctl'),
        'fail_json': classmethod(lambda *args, **kwargs: None),
        'run_command': classmethod(lambda *args, **kwargs: (0, '', '')),
        'params': {
            'gather_subset': ['!all', 'service_mgr'],
            'gather_timeout': 10
        },
    })

    # Patch 'os.path.exists', so

# Generated at 2022-06-13 03:29:31.589532
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    service_mgr = ServiceMgrFactCollector()
    class ModuleMock:
        def get_bin_path(self, path):
            if path == "systemctl":
                return "/bin/systemctl"
            return None
    module = ModuleMock()

    # test existing directory
    os.makedirs("/run/systemd/system")
    assert service_mgr.is_systemd_managed(module) == True
    os.removedirs("/run/systemd/system")

    # test symlink
    os.makedirs("/run/systemd")
    os.symlink("/run/systemd", "/run/systemd/system")
    assert service_mgr.is_systemd_managed(module) == True
    os.remove("/run/systemd/system")
    os

# Generated at 2022-06-13 03:29:37.844477
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    class ModuleFake:

        @staticmethod
        def get_bin_path(command):
            path = {
                'systemctl': '/bin/systemctl',
            }
            return path[command] if command in path else None

    module = ModuleFake()
    service_mgr_fact_collector = ServiceMgrFactCollector()
    assert service_mgr_fact_collector.is_systemd_managed_offline(module) == True

# Generated at 2022-06-13 03:29:48.599008
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():

    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.fake_module import FakeModule
    from ansible.module_utils.facts.fake_module_args import FakeModuleArgs

    module = FakeModule(FakeModuleArgs())
    cm = get_collector_instance(ServiceMgrFactCollector.name)
    assert cm.is_systemd_managed_offline(module) is False

    # Create the link /sbin/init -> systemd
    os.symlink('/bin/systemctl', '/sbin/init')
    module = FakeModule(FakeModuleArgs())
    assert cm.is_systemd_managed_offline(module) is True

    # Delete the link
    os.unlink('/sbin/init')

# Generated at 2022-06-13 03:29:55.762198
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    import os
    import platform
    import re

    from ansible.module_utils.facts.collector import ServiceMgrFactCollector

    success = True

    tmpdirname = 'tmpdirname'

    # Generate a temp directory
    if 'TMPDIR' in os.environ:
        tmpdir = os.environ['TMPDIR']
    else:
        tmpdir = '/tmp'

    tmpdir = os.path.join(tmpdir, tmpdirname)
    os.mkdir(tmpdir)

    if platform.system() == 'SunOS':
        path_to_systemd = '/usr/lib/systemd/systemd'
    else:
        path_to_systemd = '/usr/bin/systemctl'

    # Create a symlink from /sbin/init to /usr/bin/systemctl

# Generated at 2022-06-13 03:30:00.786314
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts
    import ansible.module_utils
    class FakeModule:
        def run_command(self, command, use_unsafe_shell=False):
            return 0, "something", "something"
        def get_bin_path(self, command):
            return "/bin/command"
        def get_bin_path(self, command, required=True):
            return "command"
        def load_file_common_arguments(self, params):
            pass
    FakeModule.params = {}
    for name, obj in inspect.getmembers(ansible.module_utils.facts.collector):
        if inspect.isclass(obj):
            module = ansible.module_utils.facts.collector.ModuleFactsCollector()
   

# Generated at 2022-06-13 03:30:03.762347
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():

    collection_order = [
        'service_mgr'
    ]

    collect_order = ServiceMgrFactCollector.collect_order()
    assert set(collection_order) == set(collect_order)

# Generated at 2022-06-13 03:30:16.181338
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    import mock
    mock_module = mock.MagicMock()

    # Test is_systemd_managed with systemd canary files
    mock_module.get_bin_path.return_value = '/bin/systemctl'
    for canary in ["/run/systemd/system/", "/dev/.run/systemd/", "/dev/.systemd/"]:
        os.path.exists = mock.MagicMock(return_value=True)
        ServiceMgrFactCollector.is_systemd_managed(module=mock_module)
        os.path.exists.assert_called_with(canary)

    # Test is_systemd_managed without systemd canary files
    os.path.exists = mock.MagicMock(return_value=False)

# Generated at 2022-06-13 03:30:26.921727
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    testcases = [
        {'systemd_canary': False, 'systemd_path': '/usr/bin/systemd', 'expected': False},
        {'systemd_canary': False, 'systemd_path': '/usr/bin/systemd', 'expected': False},
        {'systemd_canary': False, 'systemd_path': None, 'expected': False},
        {'systemd_canary': True, 'systemd_path': '/usr/bin/systemd', 'expected': True},
    ]

    for testcase in testcases:
        class module:
            def get_bin_path(self, arg):
                if arg == 'systemctl':
                    return testcase['systemd_path']

# Generated at 2022-06-13 03:32:02.807890
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    import sys

    class MockModule(object):
        RUN_COMMAND_RESULT = (0, 'sysvinit', '')

        def __init__(self, **kwargs):
            self.params = kwargs
            self.params['gather_subset'] = 'all'
            return None

        def get_bin_path(self, name, opts=None, required=False):
            return None

        def run_command(self, cmd, use_unsafe_shell):
            return self.RUN_COMMAND_RESULT

    class MockCollector(ServiceMgrFactCollector):
        def __init__(self, module):
            self.module = module
            self.facts_dict = None

        # This method is being mocked

# Generated at 2022-06-13 03:32:05.787703
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    from ansible.module_utils.facts.collector import Collector
    mod_cls = Collector.load_collector_classes(['service_mgr'])[0]
    mod_obj = mod_cls()
    assert not mod_obj.is_systemd_managed_offline(None)


# Generated at 2022-06-13 03:32:12.768192
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():

    # Create a mock AnsibleModule
    class MockAnsibleModule(object):

        def __init__(self):
            # Create two mocks
            self.mock_get_bin_path = unittest.mock.MagicMock(return_value=None)
            self.mock_run_command = unittest.mock.MagicMock(side_effect=['init', '/proc/1/comm', '', '/proc/1/comm', None, None])

        # Let the mock object act as the module
        def __getattr__(self, name):
            return getattr(self.mock_get_bin_path, name)
        def __getattr__(self, name):
            return getattr(self.mock_run_command, name)

    # Create a mock AnsibleModule to handle all the Ans

# Generated at 2022-06-13 03:32:17.820483
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    # Arrange
    class ModuleStub:
        def get_bin_path(self, command):
            if command == 'systemctl':
                return '/sbin/systemctl'
            else:
                return None

    obj = ServiceMgrFactCollector()
    module = ModuleStub()

    # Act
    result = obj.is_systemd_managed_offline(module)

    # Assert
    assert result == True



# Generated at 2022-06-13 03:32:24.919407
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector
    from ansible.module_utils.facts.system.service_mgr import is_systemd_managed_offline

    #  If the test is executed on a system where init is systemd, the function
    #  is_systemd_managed_offline should return true.
    if os.path.islink('/sbin/init') and os.path.basename(os.readlink('/sbin/init')) == 'systemd':
       assert ServiceMgrFactCollector.is_systemd_managed_offline(None) == True

# Generated at 2022-06-13 03:32:30.906061
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts import Facts
    from ansible.module_utils.facts.collector import init_module_collection_facts
    try:
        # init_module_collection_facts should be called when this module is executed
        # as the collection
        init_module_collection_facts(module=None, collected_facts=None)
        facts = Facts(module=None)

        # used to validate the service_mgr facts in the main module
        smfc = ServiceMgrFactCollector()
        is_systemd_managed_facts = smfc.is_systemd_managed(facts.module)

        assert is_systemd_managed_facts == False or is_systemd_managed_facts == True
    finally:
        facts.module.exit_json(ansible_facts=facts.get_facts())


# Unit test

# Generated at 2022-06-13 03:32:40.338361
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts.utils import get_file_content

    class MockModule(object):
        @staticmethod
        def get_bin_path(exe=None):
            return '/usr/bin/' + exe

    class MockOs(object):
        @staticmethod
        def path():
            class MockPath(object):
                @staticmethod
                def exists(path):
                    # if the path ends with the canary
                    if path.endswith("canary"):
                        return True
                    else:
                        return False
            return MockPath

    # Mock os.path
    module = MockModule()
    os = MockOs()
    collector = ServiceMgrFactCollector()
    result = collector.is_systemd_managed(module=module)
    assert result == True

# Generated at 2022-06-13 03:32:49.066641
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    class ModuleStub(object):
        def __init__(self, run_command_results, get_bin_path_results, is_systemd_managed_results):
            self.run_command_results = run_command_results
            self.get_bin_path_results = get_bin_path_results
            self.is_systemd_managed_results = is_systemd_managed_results

        def run_command(self, cmd, use_unsafe_shell=False):
            return self.run_command_results.pop(0)

        def get_bin_path(self, cmd):
            return self.get_bin_path_results.pop(0)

        def is_systemd_managed(self):
            return self.is_systemd_managed_results.pop(0)
