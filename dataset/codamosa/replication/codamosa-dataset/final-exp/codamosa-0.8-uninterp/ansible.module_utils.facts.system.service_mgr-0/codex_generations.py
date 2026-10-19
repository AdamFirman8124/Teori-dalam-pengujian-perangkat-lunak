

# Generated at 2022-06-13 03:23:04.062719
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    m = AnsibleModuleMock()
    assert ServiceMgrFactCollector.is_systemd_managed_offline(module=m) == False


# Generated at 2022-06-13 03:23:15.100164
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    # module = None
    # platform.system() = 'Linux'
    # os.path.exists("/run/systemd/system/") = False
    # os.path.exists("/dev/.run/systemd/") = False
    # os.path.exists("/dev/.systemd/") = False
    # return False
    assert ServiceMgrFactCollector.is_systemd_managed(None) == False

    # module = None
    # platform.system() = 'Linux'
    # os.path.exists("/run/systemd/system/") = True
    # os.path.exists("/dev/.run/systemd/") = False
    # os.path.exists("/dev/.systemd/") = False
    # return True
    assert ServiceMgrFactCollector.is_system

# Generated at 2022-06-13 03:23:19.685331
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():

    # Import modules
    from ansible.module_utils.facts.collectors.system import ServiceMgrFactCollector

    # Instance of class ServiceMgrFactCollector
    service_mgr_collector = ServiceMgrFactCollector()

    # Return value of method is_systemd_managed_offline of ServiceMgrFactCollector
    ret_val = service_mgr_collector.is_systemd_managed_offline()
    print(ret_val)

# Generated at 2022-06-13 03:23:27.449606
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    # Create a fake module that is used by ansible.module_utils.facts.collector
    class FakeAnsibleModule(object):
        def get_bin_path(self, *args):
            bin_path = '/bin/systemctl'
            return bin_path

    # When systemctl exists, but /sbin/init is not a symlink to systemd, it's not systemd managed
    fake_ansible_module = FakeAnsibleModule()
    assert ServiceMgrFactCollector.is_systemd_managed_offline(fake_ansible_module) == False

    # When systemctl exists, and /sbin/init is a symlink to systemd
    # override /sbin/init
    class FakeAnsibleModuleWithSystemd(object):
        def get_bin_path(self, *args):
            bin_path

# Generated at 2022-06-13 03:23:33.934892
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    class Module(object):
        def get_bin_path(self, s, opt_dirs=None):
            if s == 'init':
                return '/sbin/init'
            elif s == 'systemctl':
                return '/bin/systemctl'
            else:
                return None

        def run_command(self, s, data=None, check_rc=False, binary_data=False, use_unsafe_shell=False):
            if s == 'systemctl status':
                return 0, '', ''
            else:
                return 0, '', ''

    assert True == ServiceMgrFactCollector.is_systemd_managed(module=Module())


# Generated at 2022-06-13 03:23:39.193455
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    from ansible.module_utils.facts.collector import TestAnsibleModule
    module = TestAnsibleModule()
    module.run_command = lambda *cmd, **kwargs: (0, '', '')
    # no symlink /sbin/init - all systemd canaries are not present
    assert not ServiceMgrFactCollector.is_systemd_managed_offline(module)
    # symlink /sbin/init to non-systemd executable
    module.run_command = lambda *cmd, **kwargs: (0, '/usr/bin/wrong-systemd', '')
    assert not ServiceMgrFactCollector.is_systemd_managed_offline(module)
    # symlink /sbin/init to systemd, but no canaries are present

# Generated at 2022-06-13 03:23:41.559252
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    module = AnsibleModuleMock()
    servicemgr = ServiceMgrFactCollector()

    assert servicemgr.is_systemd_managed_offline(module) == False

# Generated at 2022-06-13 03:23:51.873258
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():

    import ansible.module_utils
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.utils

    class TestModule(object):
        def __init__(self, bin_ansible_call_args):
            self.bin_ansible_call_args = bin_ansible_call_args

        def get_bin_path(self, arg, required=False, opt_dirs=[]):
            if arg=='systemctl':
                return '/bin/true'
            return None

        def run_command(self, cmd):
            output = 'output'
            return 0, output, ''

    class TestCollector( ansible.module_utils.facts.collector.BaseFactCollector ):
        name = 'test_collector'
        _fact_ids = set()
        required

# Generated at 2022-06-13 03:23:53.620165
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    assert ServiceMgrFactCollector.is_systemd_managed_offline(None) == False

# Generated at 2022-06-13 03:24:01.490393
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    from ansible.module_utils import basic
    from ansible.module_utils.facts import collector

    # Tests for method is_systemd_managed_offline
    #
    # Called with module = basic.AnsibleModule('', '')
    #
    # When /sbin/init is a symlink to systemd
    #   Return True
    #
    # When /sbin/init is not a symlink to systemd
    #   Return False

    module_mock = basic.AnsibleModule('', '')
    # mock get_bin_path
    module_mock.get_bin_path = basic.AnsibleModule.get_bin_path
    # mock run_command
    module_mock.run_command = basic.AnsibleModule.run_command

    # mock_os_path_islink

# Generated at 2022-06-13 03:24:24.286257
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    class MockModule(object):
        def __init__(self, **kwargs):
            self.params = kwargs

        def run_command(self, *_, **kwargs):
            if self.params['mocked_command'] == 'ps -p 1 -o comm|tail -n 1':
                return 0, self.params['mocked_command_output'], ''
            return 0, '', ''

    class MockDistribution(object):
        name = 'Linux'

    mocked_platform = {
        'linux_distribution': MockDistribution(),
    }

    def mocked_get_file_content(*args, **kwargs):
        return "COMMAND\n"


# Generated at 2022-06-13 03:24:30.352798
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():

    class ModuleMock(object):
        pass

    class TestServiceMgrFactCollector(ServiceMgrFactCollector):
        # For unit tests we don't need the real logic, just record what was called
        _collected_facts = None
        _module = None

        def _collect(self, module=None, collected_facts=None):
            self._collected_facts = collected_facts
            self._module = module
            return {}

        def is_systemd_managed(self, module):
            self._is_systemd_managed_called = True
            return super(TestServiceMgrFactCollector, self).is_systemd_managed(self._module)

        def is_systemd_managed_offline(self, module):
            self._is_systemd_managed_offline_called = True

# Generated at 2022-06-13 03:24:39.746476
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():

    from ansible.module_utils.basic import AnsibleModule

    # Create a mock module
    module = AnsibleModule()
    module.get_bin_path = lambda executable: '/bin/' + executable if executable in ['systemctl', 'initctl'] else None

    # Create a mock os module
    os_module = AnsibleModule()
    os_module.path.islink = lambda filepath: True
    os_module.readlink = lambda filepath: 'systemd'
    os_module.path.exists = lambda filepath: True
    os_module.stat = lambda filepath: None


# Generated at 2022-06-13 03:24:48.454703
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts.collector import FactsCollector

    # Create some fake classes to be used when creating a FactsCollector object
    # (so we do not have to create fake modules, inventory, ...)
    class FakeModule:
        def get_bin_path(self, name):
            return '/bin/' + name

    class FakeConnection:
        class FakeAnsibleModule:
            def __init__(self):
                self.module = FakeModule()

        def __init__(self):
            self.AnsibleModule = FakeConnection.FakeAnsibleModule

    fake_connection = FakeConnection()

    # We don't want to print anything when calling is_systemd_managed.
    # So we will create a fake stdout for this test.
    import StringIO
    import sys

# Generated at 2022-06-13 03:25:00.523010
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    import ansible.module_utils.facts.collector

    # Create an instance of the ServiceMgrFactCollector class
    service_mgr_fact_collector = ServiceMgrFactCollector()
    # Create an empty module
    module = ansible.module_utils.facts.collector.BaseFactCollector.get_module()

    # output of command 'ls -l /sbin/init' on a systemd-managed box
    command_output = (b'/sbin/init -> /lib/systemd/systemd\n', b'', b'')
    module.run_command = MagicMock(return_value=command_output)

    assert(service_mgr_fact_collector.is_systemd_managed_offline(module))


# Generated at 2022-06-13 03:25:04.638174
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    import ansible.module_utils.facts.collector.service_mgr
    instance = ansible.module_utils.facts.collector.service_mgr.ServiceMgrFactCollector()
    assert instance.collect() == {'service_mgr': 'service'}

# Generated at 2022-06-13 03:25:16.638523
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.collector import FactsCollector

    test_object = FactsCollector()

    platform.mac_ver = lambda: ('10.4.0', ('', '', ''), 'PowerPC')
    platform.system = lambda: 'Darwin'
    platform.machine = lambda: 'Power Macintosh'
    os.path.exists = lambda path: path == '/etc/init/'
    os.path.islink = lambda path: False
    os.readlink = lambda path: None
    os.path.isfile = lambda path: False
    os.path.isdir = lambda path: False
    os.listdir = lambda path: []

# Generated at 2022-06-13 03:25:24.088357
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():

    test_mgr = ServiceMgrFactCollector()

    # Test the case of the link
    test_module = type('module', (object,), {})()
    setattr(test_module, 'get_bin_path', lambda path: '/bin/systemctl')
    os.path.islink = lambda link: True
    os.readlink = lambda link: 'systemd'
    result = test_mgr.is_systemd_managed_offline(test_module)
    assert result

    # Test the case of the islink
    test_module = type('module', (object,), {})()
    setattr(test_module, 'get_bin_path', lambda path: '/bin/systemctl')
    os.path.islink = lambda link: False
    result = test_mgr.is_systemd_managed_

# Generated at 2022-06-13 03:25:35.393498
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts.collector import MockModule
    import tempfile

    test_file_data = ''
    m = MockModule()
    # No file
    assert not ServiceMgrFactCollector.is_systemd_managed(m)

    # No content
    with tempfile.NamedTemporaryFile(delete=False) as test_file:
        test_file.write('')
        m.run_command_mock = lambda x: (0, test_file.name, '')
        assert not ServiceMgrFactCollector.is_systemd_managed(m)

    # First line as canary
    with tempfile.NamedTemporaryFile(delete=False) as test_file:
        test_file.write('first line\n')
        test_file.write('second line\n')


# Generated at 2022-06-13 03:25:46.287949
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    from ansible_collections.misc.not_a_real_collection.tests.unit.compat import unittest
    from ansible_collections.misc.not_a_real_collection.plugins.module_utils.facts.collectors.service_mgr \
        import ServiceMgrFactCollector

    ######################################################################################
    # Initialize test data
    ######################################################################################

    # First, test a system that has no service manager
    class MockModuleWithNoServiceMgr:
        def get_bin_path(self, path):
            return None

    class MockFactsWithoutServiceMgrFacts:
        def __init__(self):
            self.facts = {
                'platform': 'Other',
                'distribution': 'Other',
                'service_mgr': None,
            }


# Generated at 2022-06-13 03:26:09.147212
# Unit test for method collect of class ServiceMgrFactCollector

# Generated at 2022-06-13 03:26:15.615732
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    class MockModule(object):
        def __init__(self, platform, distribution):
            self.platform = platform
            self.distribution = distribution
            self.bin_path = {}
            self.call_count = 0

        def get_bin_path(self, command):
            if command == 'systemctl':
                if self.platform == 'Linux' and self.distribution == 'Ubuntu':
                    return '/bin/systemctl'
                elif self.platform == 'Linux' and self.distribution == 'RedHat':
                    if self.call_count < 1:
                        self.call_count += 1
                        return False
                    if self.call_count == 1:
                        self.call_count += 1
                        return '/bin/systemctl'
                else:
                    return False

# Generated at 2022-06-13 03:26:24.794062
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    from ansible.module_utils.facts import Collector
    import ansible.module_utils.facts

    # Create a mock module
    module = AnsibleModule(name='test')

    # Mock the values returned by is_systemd_managed and is_systemd_managed_offline
    def is_systemd_managed(self):
        return True
    def is_systemd_managed_offline(self):
        return True

    # Mock the value returned by is_systemd_managed
    module.is_systemd_managed = types.MethodType(is_systemd_managed, module)
    module.is_systemd_managed_offline = types.MethodType(is_systemd_managed_offline, module)

    # Mock the value returned by the get_bin_path() method

# Generated at 2022-06-13 03:26:35.415836
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    import collections
    import ansible.module_utils.facts.system.service_mgr

    dummy_module = collections.namedtuple('ansible_module', 'get_bin_path')
    collect_service_mgr = ansible.module_utils.facts.system.service_mgr.ServiceMgrFactCollector()

    # return False if systemctl not found
    dummy_module.get_bin_path = lambda: None
    assert collect_service_mgr.is_systemd_managed(module=dummy_module) is False

    # return True if /run/systemd/ exists
    dummy_module.get_bin_path = lambda: '/bin/systemctl'

# Generated at 2022-06-13 03:26:46.745263
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collectors.service_mgr import ServiceMgrFactCollector
    from ansible.module_utils.facts import ModuleMyself
    from ansible.module_utils.facts.utils import is_executable

    # Create a Collector object
    (module, my_collector) = Collector.create_collector(ModuleMyself, ['service_mgr'], {})

    # Create a ServiceMgrFactCollector object
    my_service_mgr_collector = ServiceMgrFactCollector(module=module)


# Generated at 2022-06-13 03:26:54.643947
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector
    from ansible.utils.path import unfrackpath
    import tempfile
    import os

    class FakeModule:
        def get_bin_path(self, arg1):
            if arg1 == 'systemctl':
                return '/bin/systemctl'
            else:
                return None


    fmodule = FakeModule()
    cwd = os.getcwd()
    workdir = tempfile.mkdtemp()
    os.chdir(workdir)
    os.symlink('/bin/systemd', '/sbin/init')

# Generated at 2022-06-13 03:27:02.363048
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    module = lambda: None
    module.get_bin_path = lambda x: '/bin/systemctl'
    test_collector = ServiceMgrFactCollector()

    try:
        os.symlink('/bin/systemd', '/sbin/init')
        assert test_collector.is_systemd_managed_offline(module)
    finally:
        os.remove('/sbin/init')

    assert not test_collector.is_systemd_managed_offline(module)

# Generated at 2022-06-13 03:27:09.027249
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    """Unit test for method is_systemd_managed"""
    from ansible.module_utils.facts import ModuleStub

    # test with a valid systemd, do not invoke the module
    module = ModuleStub(dict(ansible_system='Linux', ansible_distribution_file_parsed=dict(id='RedHat')))
    test_obj = ServiceMgrFactCollector()
    assert test_obj.is_systemd_managed(module=module)

    # test with a valid systemd, do not invoke the module
    module = ModuleStub(dict(ansible_system='Linux', ansible_distribution='Fedora'))
    test_obj = ServiceMgrFactCollector()
    assert test_obj.is_systemd_managed(module=module)

    # test with an invalid systemd, do not invoke the module
    module

# Generated at 2022-06-13 03:27:13.915159
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    # Create a class
    obj_fact_collector = ServiceMgrFactCollector()
    # Collect facts and check if service mgr is "sysvinit"
    assert(obj_fact_collector.collect()['service_mgr'] == 'sysvinit')


# Generated at 2022-06-13 03:27:25.221453
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    module = AnsibleModule(argument_spec={})
    module.is_systemd_managed = lambda: False
    module.get_bin_path = lambda arg: arg
    service_mgr = ServiceMgrFactCollector()

    # Check if it returns false if /sbin/init does not exist
    os.path.islink = lambda arg: False
    assert service_mgr.is_systemd_managed_offline(module) == False

    # Check if it returns false if /sbin/init is a static binary
    os.path.islink = lambda arg: arg == '/sbin/init'
    os.path.exists = lambda arg: arg == '/sbin/init'
    assert service_mgr.is_systemd_managed_offline(module) == False

    # Check if it returns false if /sbin/

# Generated at 2022-06-13 03:28:04.099216
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    module = mock
    module.get_bin_path.side_effect = lambda x: '/bin/' + x if x in ('systemctl', 'init') else None
    os.path.exists.side_effect = lambda x: True
    os.path.islink.side_effect = lambda x: True
    os.readlink.side_effect = lambda x: x
    collector = ServiceMgrFactCollector()
    assert collector.is_systemd_managed(module=module)
    module.get_bin_path.assert_any_call('systemctl')
    module.get_bin_path.assert_any_call('init')
    os.path.exists.assert_any_call('/run/systemd/system/')

# Generated at 2022-06-13 03:28:06.457326
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():

    class Module:
        def get_bin_path(self, systemctl):
            return "/usr/bin/systemctl"

    module = Module()
    collector = ServiceMgrFactCollector()

    assert collector.is_systemd_managed_offline(module) == False


# Generated at 2022-06-13 03:28:11.468095
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    # Instanciate a minimal module
    class MinimalModule:
        def __init__(self):
            self._bin_paths = {}

        def get_bin_path(self, cmd, required=False, opt_dirs=[]):
            return self._bin_paths.get(cmd, None)

    module = MinimalModule()

    # Test if systemctl is found
    module._bin_paths['systemctl'] = "/usr/bin/systemctl"
    rc = ServiceMgrFactCollector.is_systemd_managed(module=module)
    assert False == rc

    # Test if systemd canaries are there
    module._bin_paths['systemctl'] = "/usr/bin/systemctl"
    rc = ServiceMgrFactCollector.is_systemd_managed(module=module)

# Generated at 2022-06-13 03:28:14.249104
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    """
    Unit test for method ServiceMgrFactCollector.is_systemd_managed
    """
    from ansible.module_utils.basic import AnsibleModule
    obj = ServiceMgrFactCollector()
    obj.collect(module=AnsibleModule(argument_spec={}))

# Generated at 2022-06-13 03:28:24.131460
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    """ check if is_systemd_managed_offline returns expected value """
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector
    from ansible import module_utils

    class MockModule(object):
        """ fake Module class to mock get_bin_path method """
        def get_bin_path(self, cmd, required=False):
            """ fake get_bin_path method """
            if cmd == 'systemctl':
                return "/bin/systemctl"
            return None
    object_under_test = ServiceMgrFactCollector()
    class_under_test = ServiceMgrFactCollector
    mmodule = MockModule()
    # Systemd is not running
    assert class_under_test.is_

# Generated at 2022-06-13 03:28:30.127883
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    from ansible.module_utils.facts import collector

    smf = collector.get_collector('service_mgr')
    assert isinstance(smf, ServiceMgrFactCollector)

    assert not smf.is_systemd_managed_offline({'get_bin_path': lambda x: False})
    assert not smf.is_systemd_managed_offline({'get_bin_path': lambda x: True, 'run_command': lambda x: (0, '', '')})
    assert smf.is_systemd_managed_offline({'get_bin_path': lambda x: True, 'run_command': lambda x: (0, 'init', '')})
    # If /sbin/init is not a symlink as on SLES 12, then is_systemd_managed_offline() will not detect

# Generated at 2022-06-13 03:28:39.548358
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    from ansible.module_utils.facts.collector.service_mgr import ServiceMgrFactCollector
    from ansible.module_utils.facts.collector.base import BaseFactCollector
    from ansible.module_utils.facts.utils import get_file_content
    import platform
    import os

    # Create a mock module
    test_module = type('AnsibleModule', (object,), {
       'get_bin_path': lambda self, executable: None,
       'run_command': lambda self, args, check_rc=True, close_fds=True, executable=None, data=None, binary_data=False, path_prefix=None, cwd=None, use_unsafe_shell=False, prompt=None, answer=None, text=None: (0, '', ''),
    })() 

   

# Generated at 2022-06-13 03:28:48.990100
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    mod = AnsibleModuleMock()
    mod.get_bin_path = lambda x: '/bin/systemctl'
    mod.run_command = lambda x, y: (0, '', '')
    facts_collector = ServiceMgrFactCollector()

    def _os_path_islink(path):
        assert path == '/sbin/init'
        return True

    def _os_readlink(path):
        assert path == '/sbin/init'
        return 'systemd'

    facts_collector.os.path.islink = _os_path_islink
    facts_collector.os.readlink = _os_readlink

    assert facts_collector.is_systemd_managed_offline(module=mod)



# Generated at 2022-06-13 03:28:58.540592
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts.collector import Collector
    import mock
    import os.path

    Collector.collectors = []
    Collector._collectors_names = set()

    module = mock.MagicMock()
    module.get_bin_path.return_value = None

    result = ServiceMgrFactCollector.is_systemd_managed(module)

    assert result == False

    module.get_bin_path.return_value = '/usr/bin/systemctl'
    result = ServiceMgrFactCollector.is_systemd_managed(module)

    assert result == False

    module.get_bin_path.return_value = '/usr/bin/systemctl'
    os.path.exists = mock.MagicMock()

# Generated at 2022-06-13 03:29:00.937388
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    ServiceMgrFactCollector = ServiceMgrFactCollector.__new__(ServiceMgrFactCollector)
    assert ServiceMgrFactCollector.is_systemd_managed_offline(None) == False

# Generated at 2022-06-13 03:30:11.194012
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():

    class MockModule(object):
        _result = {'ansible_distribution': 'RHEL',
                   'ansible_system': 'RedHat'}

        def get_bin_path(self, a):
            return a is 'systemctl' and '/bin/systemctl' or None

        def run_command(self, cmd, use_unsafe_shell=False):
            if cmd == 'ps -p 1 -o comm|tail -n 1':
                return 0, '/bin/systemd', ''
            return 0, '', ''

    m = MockModule()
    collector = ServiceMgrFactCollector()
    res = collector.collect(module=m)
    assert res == {'service_mgr': 'systemd'}

# Generated at 2022-06-13 03:30:19.265989
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts import collector

    # Mock module to return the values that would be normally returned my module_utils
    class MockModule(object):

        def get_bin_path(self, path):
            return True if path == 'systemctl' else None

        def get_bin_path(self, *args):
            return '/usr/bin/systemctl'

    class FakeOs(object):
        def __init__(self):
            self.path = FakePathModule()

    class FakePathModule(object):
        def exists(self, directory):
            if directory == "/run/systemd/system/":
                return True
            return False

        def islink(self, directory):
            if directory == '/sbin/init':
                return True
            return False


# Generated at 2022-06-13 03:30:29.664448
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    module = None

    collector = ServiceMgrFactCollector()

    # Test 1: Run method with no parameters
    result = collector.is_systemd_managed(module)

    assert result == False

    # Test 2: Run method with empty /dev/.run/systemd/ directory
    tmp_dir = "/dev/.run/systemd"
    os.makedirs(tmp_dir)
    result = collector.is_systemd_managed(module)

    assert result == True
    os.removedirs(tmp_dir)

    # Test 3: Run method with file under /dev/.run/systemd/
    tmp_file = tmp_dir + "/testfile.tmp"
    open(tmp_file, 'a').close()
    result = collector.is_systemd_managed(module)

    assert result == True
    os.remove

# Generated at 2022-06-13 03:30:34.183684
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts.collector import collector_subset_fact_classes
    service_mgr_fact_collector = ServiceMgrFactCollector(subset_list=collector_subset_fact_classes)
    class FakeModule(object):
        def get_bin_path(self, path):
            return path
    module = FakeModule()
    assert service_mgr_fact_collector.is_systemd_managed(module=module)


# Generated at 2022-06-13 03:30:39.764397
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    import ansible.module_utils.facts.collectors.service_mgr as service_mgr
    module = ansible.module_utils.basic.AnsibleModule(argument_spec={})

    # Test that the result is False when /sbin/init is not a symlink
    if os.path.islink('/sbin/init'):
        os.unlink('/sbin/init')
    result = service_mgr.ServiceMgrFactCollector.is_systemd_managed_offline(module)
    assert not result

    # Test that the result is False when /sbin/init is not a symlink to systemd
    if not os.path.islink('/sbin/init'):
        os.symlink('/bin/ls', '/sbin/init')

# Generated at 2022-06-13 03:30:49.116834
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    class MockModule():
        def get_bin_path(self, name):
            return name

    class MockFacts():
        def __init__(self):
            self.facts = {
                'ansible_system': 'linux',
                'ansible_distribution': 'SUSE',
                'platform': 'linux',
                'distribution': 'SUSE'
            }

        def get(self, fact):
            '''Returns a fact from facts'''
            return self.facts.get(fact)

    smfc = ServiceMgrFactCollector()
    # expected_result is based on a SLES12 SP3 machine
    expected_result = {
        'service_mgr': 'systemd'
    }
    module = MockModule()
    facts = MockFacts()

# Generated at 2022-06-13 03:30:57.011457
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    from ansible.module_utils.facts.collector import BaseFactCollector
    base_fact_collector_object = BaseFactCollector()
    # Patching method get_bin_path of class BaseFactCollector.
    # As it requires a parameter module and we don't have a module
    # this method is not meaningful to us. So to avoid it, we patch the
    # method get_bin_path to return true.
    def is_systemd_managed_temp(module):
        return True
    base_fact_collector_object.get_bin_path = is_systemd_managed_temp
    service_mgr_fact_collector_object = ServiceMgrFactCollector()
    service_mgr_fact_collector_object.get_bin_path = is_systemd_managed_temp
    assert service_mgr

# Generated at 2022-06-13 03:31:02.004770
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    # when method for class is called with a module, it returns the expected
    # value in the returned dictionary
    from ansible.module_utils.facts.collector import get_collector_facts
    from ansible.module_utils.facts.collectors.service_mgr import ServiceMgrFactCollector

    # assert that we get the expected output
    data = get_collector_facts(module=None, collected_facts=None,
                               source_exts=[ServiceMgrFactCollector])
    assert data == {'service_mgr': 'service'}

# Generated at 2022-06-13 03:31:09.884774
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    import ansible.module_utils.facts.collectors.service_mgr as sm

    class MockModule(object):
        def get_bin_path(self, arg):
            return '/bin/systemctl'

    def mocks_os_path_exists(arg):
        return True

    def mocks_os_path_islink(arg):
        return True

    def mocks_os_readlink(arg):
        return 'systemd'

    class mock_systemctl_tests(object):

        @staticmethod
        def mock_canary_exists(arg):
            return True

    mock_os = mock_systemctl_tests()
    mock_os.path.exists = mocks_os_path_exists
    mock_os.path.islink = mocks_os_path_islink
    mock_

# Generated at 2022-06-13 03:31:15.939827
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():

    # create mocks of the module class
    module = Mock()
    module.get_bin_path.return_value = None

    # create insatnce of class to be tested
    smfc = ServiceMgrFactCollector()

    # test with no tools
    assert not smfc.is_systemd_managed(module)

    # test if systemctl is present and not systemd
    module.get_bin_path.return_value = '/bin/systemctl'
    assert not smfc.is_systemd_managed(module)

    # test if systemctl is present and systemd exists
    module.systemctl.return_value = True
    assert smfc.is_systemd_managed(module)


from ansible.utils.path import unfrackpath
from ansible.module_utils.parsing.convert_bool import boolean