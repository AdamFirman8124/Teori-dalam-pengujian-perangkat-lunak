

# Generated at 2022-06-13 03:23:15.359123
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():

    import ansible.module_utils.basic

    class MockModule(object):
        params = {
            'use_unsafe_shell': False,
        }
        def __new__(cls, *args, **kwargs):
            with open('/proc/1/comm','w') as f:
                f.write('systemd')
            return super(MockModule, cls).__new__(cls, *args, **kwargs)

        def get_bin_path(self, *args, **kwargs):
            return '/bin/systemctl'

        def run_command(self, *args, **kwargs):
            return 0, '', ''

    mock_module = MockModule()
    obj = ServiceMgrFactCollector()
    ret = obj.is_systemd_managed(module=mock_module)


# Generated at 2022-06-13 03:23:24.476827
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    ServiceMgrFactCollector_instance = ServiceMgrFactCollector()

    # create a mock module to pass to is_systemd_managed_offline
    class MockModule:
        @staticmethod
        def get_bin_path(arg1):
            # return the value for systemctl
            if arg1 == 'systemctl':
                return "/bin/systemctl"
            # return the value for systemctl
            if arg1 == 'systemd':
                return "/bin/systemd"
            return None


# Generated at 2022-06-13 03:23:30.341033
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    import mock
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector

    # mock facts
    facts = {'ansible_system': 'Linux', 'ansible_distribution': 'SUSE'}
    base_fact_collector_obj = BaseFactCollector(module=None)
    for key in facts:
        base_fact_collector_obj.collect(key, module=None, collected_facts=facts)

    # If neither "/sbin/init" nor systemctl exists, the function should return False
    with mock.patch.object(ServiceMgrFactCollector, 'get_file_content', return_value=None):
        facts_collector_obj = ServiceMgrFactCollector()

# Generated at 2022-06-13 03:23:36.714517
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():

    class MockModule:
        def __init__(self):
            self.run_command_calls = 0
            self.run_command_results = [
                (0, 'init', ''),
            ]

        def get_bin_path(self, _):
            return None

        def run_command(self, _, **kwargs):
            self.run_command_calls += 1
            return self.run_command_results[self.run_command_calls - 1]

    module = MockModule()

    facts_dict = {
        'platform': 'Linux',
        'distribution': 'CentOS'
    }

    service_mgr_fact_collector = ServiceMgrFactCollector(module)

# Generated at 2022-06-13 03:23:46.233033
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    '''Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector.'''

    # Setup
    from ansible.module_utils.facts.collector import BaseFactCollector
    mock_module = BaseFactCollector()
    mock_module.get_bin_path = lambda x: True
    test_smfc = ServiceMgrFactCollector()

    # Test
    try:
        os.symlink('/bin/true', '/sbin/init')
        result = test_smfc.is_systemd_managed_offline(mock_module)
        assert not result
    finally:
        os.unlink('/sbin/init')


# Generated at 2022-06-13 03:23:57.063914
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    class ModuleStub(object):
        def __init__(self):
            self.params = None
            self.binary_paths = {'systemctl': '/bin/systemctl'}
        def get_bin_path(self, binary):
            return self.binary_paths.get(binary)
    def os_path_islink_stub(path):
        return path == '/sbin/init'
    def os_readlink_stub(path):
        return '/sbin/systemd'
    module = ModuleStub()
    service_mgr_obj = ServiceMgrFactCollector()

    # Mocking os.path.islink and os.readlink
    original_os_path_islink = os.path.islink
    os.path.islink = os_path_islink_stub
    original

# Generated at 2022-06-13 03:24:03.857125
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    from ansible.module_utils.facts.collector import ServiceMgrFactCollector
    from ansible.module_utils.facts.collection import BaseFactCollector
    from ansible.module_utils.facts.utils import get_file_content

    class Module(object):

        @staticmethod
        def get_bin_path(cmd):
            if cmd == 'systemctl':
                return '/bin/systemctl'
            return None

        @staticmethod
        def run_command(cmd, use_unsafe_shell=False):
            return 1, ['systemd'], 'systemd'

    obj = ServiceMgrFactCollector()
    obj.distribution = 'OpenSuse'
    obj.module = Module()
    obj.platform = 'Linux'

    assert obj.is_systemd_managed_offline() == True

# Generated at 2022-06-13 03:24:07.193450
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    class FakeModule(object):
        def get_bin_path(self, cmd, required=False):
            return False

    result = ServiceMgrFactCollector.is_systemd_managed_offline(module=FakeModule())
    assert result == False

# Generated at 2022-06-13 03:24:16.099904
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils import facts
    import os
    import stat
    import tempfile
    import shutil
    import sys


# Generated at 2022-06-13 03:24:24.996884
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():

    import ansible.module_utils.facts as facts_module_utils
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector

    facts_module_utils.CACHE = {}

    class ModuleMock(object):
        def __init__(self):
            self._bin_path = {}
            self.params = {}
            self.env = {}
            self.run_command_environ_update = {}

        def get_bin_path(self, arg):
            if arg in self._bin_path:
                return self._bin_path[arg]
            return None

        def run_command(self, arg, use_unsafe_shell=True):
            return (0, '', '')

   

# Generated at 2022-06-13 03:24:49.305848
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    import ansible.module_utils.facts.collector
    import tempfile
    import shutil
    import os

    ## create test case for /sbin/init is a symlink to system

    # create a temporary directory
    temp_dir = tempfile.mkdtemp()

    # the symlink file name
    symlink_file_name = "init"
    symlink_file_path = os.path.join(temp_dir, symlink_file_name)

    # Create symlink file
    os.symlink(os.path.join(temp_dir, "system"), symlink_file_path)

    # create the object
    obj = ServiceMgrFactCollector()

    # create fake module object
    class FakeModule(object):
        def __init__(self, name):
            self

# Generated at 2022-06-13 03:25:01.307530
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():

    def fake_module_run_command(command, **kwargs):
        if command == "ps -p 1 -o comm|tail -n 1":
            return (0, 'init\n', '')
        else:
            return (1, '', '')
    # create fake module object
    module = type('FakeModule', (object,), {})
    setattr(module, 'run_command', fake_module_run_command)

    def fake_get_bin_path(command):
        if command == 'systemctl':
            return 'systemctl'
        return None
    setattr(module, 'get_bin_path', fake_get_bin_path)

    # create fake collected_facts
    collected_facts = {
        'ansible_distribution': None,
        'ansible_system': 'Linux',
    }

# Generated at 2022-06-13 03:25:09.868150
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts.collector import FakeModule
    from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector

    fake_module = FakeModule()
    collector = ServiceMgrFactCollector(fake_module)

    def get_bin_path(exe):
        if exe == 'systemctl':
            return '/usr/bin/systemctl'
        else:
            return None

    fake_module.get_bin_path = get_bin_path

    should_be_true = [
        '/run/systemd/system/',
        '/dev/.run/systemd/',
        '/dev/.systemd/'
    ]
    should_be_false = ['/.systemd/', '/run/.systemd', '/dev/.systemd']

# Generated at 2022-06-13 03:25:20.702929
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    set_module_args({'service_mgr': 'service'})
    service = ServiceMgrFactCollector()
    collected_facts = dict()
    collected_facts['service_mgr'] = {'service_mgr': 'service'}
    collected_facts['ansible_system'] = 'AIX'
    collected_facts['ansible_distribution'] = 'OpenWrt'
    collected_facts['platform'] = 'AIX'
    collected_facts['distribution'] = 'OpenWrt'

# Generated at 2022-06-13 03:25:33.611306
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    import datetime
    import pytest
    from ansible.module_utils.facts import Facts
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector
    from ansible.module_utils.facts.utils import get_file_content, get_file_lines

    class MockModule():
        def __init__(self):
            self.params = { 'gather_subset': ['all'] }

        def get_bin_path(self, name):
            return '/usr/bin/'+name


    # set the facts to known values
    facts = Facts({}, {}, {})
    # setup minimal fact structure
    facts['ansible_facts'] = {}
    facts['server_facts'] = {}
   

# Generated at 2022-06-13 03:25:44.280552
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    from ansible.module_utils.facts import Collector

    CollectedFacts = Collector().collect()

    # Create simple test for method collect of class ServiceMgrFactCollector
    smfc = ServiceMgrFactCollector()

    collected_facts = smfc.collect(module=None, collected_facts=CollectedFacts)

    assert collected_facts['service_mgr'] == 'service'

    # Create test for detection of 'service_mgr' for platform 'Linux' with distribution 'Ubuntu'
    CollectedFacts['ansible_distribution'] = 'Ubuntu'
    CollectedFacts['ansible_system'] = 'Linux'

    # Create test for detection of 'service_mgr' with 'systemd'
    CollectedFacts['ansible_system'] = 'Linux'
    CollectedFacts['ansible_distribution']

# Generated at 2022-06-13 03:25:52.425758
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts.collector import DummyModule
    module = DummyModule()

    def mx(x):
        return os.path.exists(x)

    sm = ServiceMgrFactCollector()

    # test sub conditions
    assert mx('/proc/1/comm') and os.readlink('/sbin/init') == 'systemd'

    # test systemd
    module.run_command = lambda x: (0, '', '')

    os.stat = lambda x: True
    os.path.exists = mx
    os.path.islink = lambda x: True

    assert sm.is_systemd_managed(module=module) is True

    os.stat = lambda x: False
    del os.readlink
    os.path.islink = lambda x: False

   

# Generated at 2022-06-13 03:25:59.418387
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    from ansible.module_utils.facts.collector import FactsCollector
    from ansible.module_utils.facts.collectors.linux.service_mgr import ServiceMgrFactCollector

    fc = FactsCollector()
    fc.add_collector(ServiceMgrFactCollector())
    result = fc.collect(module=None, collected_facts={})
    assert result['service_mgr'] == 'service'

if __name__ == '__main__':
    test_ServiceMgrFactCollector_collect()

# Generated at 2022-06-13 03:26:06.061367
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    import os
    import sys
    import tempfile

    # Create temporary directories
    temp_dirs = []

    for i in range(0, 4):
        temp_dir = tempfile.mkdtemp()
        temp_dirs.append(temp_dir)

    # Create links inside base directory
    os.symlink('/bin/systemd', os.path.join(temp_dirs[0], 'init'))
    os.symlink('/bin/systemd', os.path.join(temp_dirs[1], 'init'))
    os.symlink('/bin/systemd', os.path.join(temp_dirs[2], 'init'))
    os.symlink('/bin/systemd', os.path.join(temp_dirs[3], 'init'))

    # create

# Generated at 2022-06-13 03:26:11.016222
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    from ansible.module_utils.facts.collector import MockModule
    # mock up the module
    module = MockModule(
        params=dict(
            filter=['ansible_service_mgr'],
            gather_subset=['all']
        )
    )
    # initialize the fact collector
    fact_collector = ServiceMgrFactCollector(module=module)
    # run the actual collect method
    results = fact_collector.collect(module=module)
    # we do not need to test the actual values, the logic is tested in
    # the methods is_systemd_managed and is_systemd_managed_offline
    assert 'ansible_service_mgr' in results

# Generated at 2022-06-13 03:26:53.413614
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    # create instance of class for testing
    service_mgr_fact_collector = ServiceMgrFactCollector()

    # test for return value of True
    for canary in ["/run/systemd/system/", "/dev/.run/systemd/", "/dev/.systemd/"]:
        service_mgr_fact_collector.module.run_command = lambda cmd, use_unsafe_shell: (0, '', '')
        service_mgr_fact_collector.module.get_bin_path = lambda cmd: os.path.exists("/usr/bin/systemctl")
        assert service_mgr_fact_collector.is_systemd_managed(service_mgr_fact_collector.module) == True

    # test for return value of False
    service_mgr_fact_collector.module.run

# Generated at 2022-06-13 03:27:03.970849
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    fake_module_mock = type('module', (object,), {})()
    setattr(fake_module_mock, 'get_bin_path', lambda self, executable: None)
    assert ServiceMgrFactCollector.is_systemd_managed_offline(fake_module_mock) is False

    import tempfile
    tmpdir = tempfile.mkdtemp()

# Generated at 2022-06-13 03:27:06.651240
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
  from ansible.module_utils.facts.collector import get_collector_facts
  from ansible.module_utils.facts.collector import get_module

  module = get_module()
  collector = get_collector_facts(module=module,
                                  collector=ServiceMgrFactCollector)

  assert collector.is_systemd_managed(module) is False

# Generated at 2022-06-13 03:27:18.702735
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    import ansible.module_utils.facts.system.service_mgr
    from ansible.module_utils.facts.system import service_mgr

    # create dummy module with get_bin_path set to return path to systemctl binary
    class Module(object):
        def __init__(self):
            self.params = dict()
            self.fail_json = None
            self.run_command = None
        def get_bin_path(self, binary, opt_dirs=[]):
            if binary == 'systemctl':
                return '/usr/bin/systemctl'

    module = Module()
    service_mgr_obj = ansible.module_utils.facts.system.service_mgr.ServiceMgrFactCollector()

    # create symlink from /sbin/init to /lib/systemd/systemd
   

# Generated at 2022-06-13 03:27:30.062415
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts.collector import MockModule

    facts_dict = {}
    collected_facts = MockModule().get_facts(facts_dict)
    is_systemd_managed = ServiceMgrFactCollector.is_systemd_managed(module=MockModule())

    assert is_systemd_managed is True or is_systemd_managed is False

    def test_ServiceMgrFactCollector_is_systemd_managed_offline():
        from ansible.module_utils.facts.collector import MockModuleOffline

        facts_dict = {}
        collected_facts = MockModuleOffline().get_facts(facts_dict)
        is_systemd_managed_offline = ServiceMgrFactCollector.is_systemd_managed_offline(module=MockModuleOffline())

        assert is_systemd_managed

# Generated at 2022-06-13 03:27:38.364221
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    class MockModule:
        def get_bin_path(self, command):
            return '/usr/bin/env'

    import tempfile
    import os

    temp_dir = tempfile.mkdtemp()

    os.symlink('systemd', os.path.join(temp_dir, 'sbin/init'))
    os.symlink('systemd', os.path.join(temp_dir, 'bin/init'))

    svc = ServiceMgrFactCollector()
    assert svc.is_systemd_managed_offline(MockModule())

# Generated at 2022-06-13 03:27:48.940161
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    mock_module = type('module', (object,), {
        'run_command': lambda self, *args, **kwargs: (0, '\nCOMMAND\n', ''),
        'get_bin_path': lambda self, path: None,
    })

    # Test without module
    facts_dict = ServiceMgrFactCollector.collect()
    assert facts_dict == {}

    # Test with module
    module = mock_module()

    # Test with proc/1/comm not readable
    facts_dict = ServiceMgrFactCollector.collect(module)
    assert facts_dict == {'service_mgr': 'service'}

    # Test with /proc/1/comm not readable and ps command fails
    module.run_command = lambda self, *args, **kwargs: (1, '', 'process error')


# Generated at 2022-06-13 03:27:54.750596
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    collected_facts = dict(ansible_distribution = "OpenWrt",
                           ansible_distribution_major_version = "15.05",
                           ansible_distribution_version = "15.05",
                           ansible_system = "Linux",
                           ansible_lsb = dict(id = "OpenWrt",
                                              major_release = "15.05",
                                              release = "15.05"),
                           ansible_pkg_mgr = "ipkg")

    ServiceMgrFactCollector().collect(module=None, collected_facts=collected_facts)
    assert collected_facts['service_mgr'] == 'openwrt_init'

# Generated at 2022-06-13 03:28:00.049836
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    import tempfile
    import shutil
    import os

    # Make a temporary directory
    tmpdir = tempfile.mkdtemp()

    # Create a subdirectory 'sbin'
    os.mkdir(os.path.join(tmpdir, 'sbin'))

    # Create a symlink named 'init' pointing to 'systemd' in the 'sbin' subdirectory
    os.symlink('systemd', os.path.join(tmpdir, 'sbin', 'init'))

    # Prepare module argument
    from ansible.module_utils.facts import ModuleTest
    from ansible.module_utils.facts import AnsibleModule
    module_args = {}
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)
    module.params['_ansible_tmpdir'] = tmp

# Generated at 2022-06-13 03:28:08.351875
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    import ansible.module_utils.basic
    from ansible.module_utils.facts import Collector
    collector = Collector()
    module_mock = ansible.module_utils.basic.AnsibleModule(argument_spec={})
    collector.populate()
    smfc = ServiceMgrFactCollector(module=module_mock)
    assert smfc.is_systemd_managed(module_mock) is False
    assert smfc.is_systemd_managed_offline(module_mock) is False


if __name__ == "__main__":
    test_ServiceMgrFactCollector_is_systemd_managed()

# Generated at 2022-06-13 03:29:49.708100
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    import ansible.module_utils.facts.collector
    tmp = ansible.module_utils.facts.collector.BaseFactCollector.get_bin_path
    ansible.module_utils.facts.collector.BaseFactCollector.get_bin_path = lambda x,y: y
    from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector
    saved_readlink = os.readlink
    from ansible.test.unit import skipIf, AnsibleExitJson
    from ansible.test.unit.module_utils import basic
    from ansible.module_utils import basic
    import os
    import tempfile
    import shutil

    tmp_path = tempfile.mkdtemp()
    os.mkdir(tmp_path + '/sbin')
    os.symlink

# Generated at 2022-06-13 03:29:56.386611
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts import ModuleFacts
    from ansible.module_utils.facts.utils import get_file_content, get_bin_path
    import tempfile

    class TestModuleFactsHelper(ModuleFacts):
        def get_bin_path(self, arg):
            return get_bin_path(arg)

        def get_file_content(self, path):
            return get_file_content(path)

    mf = TestModuleFactsHelper()

    # setup fake run_command
    mf.run_command = lambda x: (0, '', '')

    # setup fake file paths
    os.path.exists = lambda x: True
    temp_dir = tempfile.TemporaryDirectory(prefix='ansible_test_')


# Generated at 2022-06-13 03:30:05.605404
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    from ansible.module_utils.facts.collector import ServiceMgrFactCollector
    # make sure the test is only run on Linux
    assert platform.system() == 'Linux'
    # This test is using a patched module_utils.systemd.py to make sure systemctl is not called.
    # The patched version of module_utils.systemd.py is located in test/unit/utils/systemd_patch.py
    # The test will only succeed if the patched version of module_utils.systemd.py is loaded before the systemd.py.
    # In the test environment, Ansible is installed in a virtual environment. Ansible's module_utils is located
    # in the virtual environment. So we need to add the parent directory of the virtual environment to the search path
    # so that the patched version of module_utils.systemd.py can be loaded.


# Generated at 2022-06-13 03:30:14.252184
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    class StubModule(object):
        def get_bin_path(self, program):
            # any executable path
            return "/bin/echo"

        def run_command(self, command, use_unsafe_shell=False):
            return 0, 'systemd', ''

    class StubFacts(object):
        pass

    smfc = ServiceMgrFactCollector()
    smfc.required_facts = set()
    smfc.name = 'service_mgr'
    assert(smfc.is_systemd_managed(module=StubModule()))

# Generated at 2022-06-13 03:30:25.165828
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    class MockModule(object):
        class run_command(object):
            def __init__(self):
                self.rc = 0
                self.stdout = ''
                self.stderr = ''

            def run_command(self, *args, **kwargs):
                return self.rc, self.stdout, self.stderr

        def get_bin_path(self, binary, required=False, opt_dirs=None):
            return binary

    def mock_os_path_exists(fname):
        exists = False
        if fname == '/proc/1/comm':
            exists = True
        if fname == '/dev/.run/systemd':
            exists = True
        if fname == '/etc/init.d/':
            exists = True

# Generated at 2022-06-13 03:30:31.486671
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    import tempfile
    import os
    import shutil
    tmp_dir = tempfile.mkdtemp()
    # Create a fake systemd in a temporary directory
    os.symlink(os.path.join(tmp_dir, 'systemd'),
              os.path.join(tmp_dir, 'init'))
    os.makedirs(os.path.join(tmp_dir, 'systemd'))
    os.makedirs(os.path.join(tmp_dir, 'run'))

    def catch_warning(module, warning):
        '''
        ModuleMock.warnings is an object, we need to catch the warning that is an
        exception
        '''
        try:
            module.fail_json(msg=warning)
        except Exception as e:
            return to_native(e)

    # M

# Generated at 2022-06-13 03:30:37.816935
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    import ansible.module_utils.facts.collector.service_mgr as service_mgr
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector.service_mgr import ServiceMgrFactCollector

    # Create a mock module
    class MockModule(ansible_facts.AnsibleFacts):
        def __init__(self):
            self.systemctl = None
            self.run_command = None
            self.get_bin_path = None

        def get_bin_path(self, cmd):
            if cmd == 'systemctl':
                if self.systemctl:
                    return True
            return None

    # Create mocked facts

# Generated at 2022-06-13 03:30:46.954697
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts.collector import Namespace
    from ansible.module_utils.facts.collector import get_collector_class
    from ansible.module_utils.facts.collector import get_collector_for

    service_collector = get_collector_class('service_mgr')
    
    is_systemd_managed = lambda: service_collector.is_systemd_managed(mock_module)
    mock_module = Namespace()

    def mock_get_bin_path(command):
        return command == 'systemctl'
    mock_module.get_bin_path = mock_get_bin_path


# Generated at 2022-06-13 03:30:55.866237
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    class MockModule(object):
        def __init__(self):
            self.params = {}
            self.run_command = lambda self, cmd, use_unsafe_shell=True: None

        def get_bin_path(self):
            return None

        def fail_json(self, **args):
            raise Exception("")

    class MockCollector(object):
        def __init__(self):
            self.ansible_facts = {'service_mgr': 'systemd', 
                                  'platform': 'Linux'}

    collector = ServiceMgrFactCollector()
    module = MockModule()
    collected_facts = MockCollector()
    result = collector.collect(module=module, collected_facts=collected_facts)
    assert result['service_mgr'] == 'systemd'

# Generated at 2022-06-13 03:30:59.879404
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts.collector.service_mgr import ServiceMgrFactCollector

    assert not ServiceMgrFactCollector.is_systemd_managed(None)

    class TestModule(object):
        def get_bin_path(self, tool):
            return '/bin/true'

    assert ServiceMgrFactCollector.is_systemd_managed(TestModule())

