

# Generated at 2022-06-13 03:23:11.237962
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    class MockModule:
        def __init__(self, param):
            self.params = param

        def fail_json(self, *args, **kwargs):
            raise Exception(kwargs['msg'])

        def get_bin_path(self, *args, **kwargs):
            name = args[0]
            if name == 'systemctl':
                return True
            else:
                return False

        def run_command(self, cmd, use_unsafe_shell=True):
            if cmd == "ps -p 1 -o comm|tail -n 1":
                return 0, 'systemd-udevd', 0
            else:
                return 0, None, 0

    class MockFact:
        def __init__(self, param):
            self.dict = param

    params = {}

# Generated at 2022-06-13 03:23:14.123056
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    testobj = ServiceMgrFactCollector()
    assert testobj.is_systemd_managed_offline() == False
# vim: set et ts=4 sw=4 :

# Generated at 2022-06-13 03:23:19.717849
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    """
    In test_ServiceMgrFactCollector_collect(),
    The method collect() of class ServiceMgrFactCollector
    is tested, this methods checks the service manager in system
    and return.
    """
    platform = ['Linux','FreeBSD','SunOS']

    print('Checking ServiceMgrFactCollector_collect() in ansible.module_utils.facts.service_mgr')
    for p in platform:
        print('Testing for platform ' + p)
        fact_collector = ServiceMgrFactCollector()
        print(fact_collector.collect())

# Generated at 2022-06-13 03:23:27.477514
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    """Check that is_systemd_managed_offline returns the expected value."""
    from ansible.module_utils.facts.collectors.system import ServiceMgrFactCollector
    from ansible.module_utils.facts.collectors.system.system import _SystemCollector

    class MockAnsibleModule(object):
        def __init__(self, bin_path):
            self._bin_path = bin_path

        def get_bin_path(self, executable):
            return self._bin_path

    class MockFile(object):
        def __init__(self, content=None):
            self.content = content

        def readlink(self, path):
            """Return a static value when path is /sbin/init."""
            if path == '/sbin/init':
                return 'systemd'

# Generated at 2022-06-13 03:23:36.170007
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    # noinspection PyTypeChecker
    fact_collector = ServiceMgrFactCollector()

    # This method is not tested, because it is based on detection of
    #   file system content, which is not mocked with Ansible tests.
    assert fact_collector.is_systemd_managed(None) == "not tested"

    # This method is not tested, because it is based on detection of
    #   file system content, which is not mocked with Ansible tests.
    assert fact_collector.is_systemd_managed_offline(None) == "not tested"

    assert fact_collector.collect() == {'service_mgr': 'service'}
    assert fact_collector.collect(collected_facts={'ansible_distribution': 'MacOSX'}) == {'service_mgr': 'launchd'}

# Generated at 2022-06-13 03:23:45.946015
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():

    class AnsibleModule():
        def __init__(self):
            self.bin_path_result = 'bin_path_result'

        def get_bin_path(self, name, required=True, opt_dirs=[]):
            if name == 'systemctl':
                return self.bin_path_result
            return None

    class MockOsPath():
        def __init__(self, file_exists_result):
            self.file_exists_result = file_exists_result

        def exists(self, path):
            return self.file_exists_result

    # test that method is_systemd_managed returns True when systemctl is installed and one of the canary files exists
    module = AnsibleModule()
    module.bin_path_result = 'systemctl'

# Generated at 2022-06-13 03:23:54.814488
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    module = mock.MagicMock()
    module.get_bin_path.return_value = '/bin/systemctl'

    instance = ServiceMgrFactCollector()

    # systemd is not running so is_systemd_managed should return False
    with mock.patch.object(os.path, 'exists', return_value=False):
        assert not instance.is_systemd_managed(module)

    # one of the systemctl canaries exists, should return True
    with mock.patch.object(os.path, 'exists', return_value=True):
        assert instance.is_systemd_managed(module)

# Generated at 2022-06-13 03:24:02.224346
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    from ansible.module_utils.facts.collector import BaseFactCollector
    class TestFactCollector(BaseFactCollector):
        name = 'test'
        _fact_ids = set()
        required_facts = set()
        def collect(self, module=None, collected_facts=None):
            self.module = module
            return {
                'facts': {}
            }

    class TestModule:
        def __init__(self):
            self.exit_json = self.fail_json = lambda **kwargs: None
            self.params = {}

        def get_bin_path(self, path, opt_dirs=[]):
            if path == 'systemctl':
                return '/bin/false'
            else:
                return None

    collector = ServiceMgrFactCollector()

# Generated at 2022-06-13 03:24:12.389184
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    from ansible.module_utils.facts.collector import get_collector_facts
    import ansible.module_utils.facts.collectors
    import ansible.module_utils.facts.system.service_mgr
    import ansible.module_utils.common.os.path
    import ansible.module_utils.common.os.linux

    class MockModule(object):

        @staticmethod
        def get_bin_path(binary):
            binaries = {
                'systemctl': '/bin/systemctl',
            }
            return binaries.get(binary)

    # Return true when /sbin/init is a symlink to systemd
    is_systemd_managed_offline = None

# Generated at 2022-06-13 03:24:22.342471
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    from ansible.module_utils import basic
    from ansible.module_utils.facts.utils import get_file_content

    # The following testing function defines a fake AnsibleModule object.
    # This object is then passed to the ServiceMgrFactCollector instantiation.
    #
    # The fake AnsibleModule object is then used to mock _ansible_module_instance.
    #
    # The ServiceMgrFactCollector.collect() method is then executed.
    #
    # Finally, the result is tested.

    # Mock File Not Found Error
    def mock_get_file_content(path):
        if path == "/proc/1/comm":
            return "/sbin/init"
        return None

    # Mock OpenRC

# Generated at 2022-06-13 03:24:43.367451
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    module = MockModule()
    collector = ServiceMgrFactCollector()

    # simulate SUSE with systemd
    module.get_bin_path_mock_retvalue = '/bin/systemctl'
    module.run_command_mock_retcode = 0
    module.run_command_mock_stdout = '/usr/lib/systemd/systemd\n'
    assert collector.is_systemd_managed_offline(module=module)

    # simulate SUSE with init
    module.get_bin_path_mock_retvalue = '/bin/systemctl'
    module.run_command_mock_retcode = 0
    module.run_command_mock_stdout = '/sbin/init\n'
    assert not collector.is_systemd_managed_offline(module=module)

    # simulate

# Generated at 2022-06-13 03:24:50.592170
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    from ansible.module_utils.facts import Facts
    from ansible.module_utils.facts import default_collectors

    ServiceMgrFactCollector.required_facts = set()
    ServiceMgrFactCollector.validate_deps()

    test_collected_facts = {
        'ansible_distribution': 'OpenWrt',
        'ansible_system': 'Linux'
    }

    test_result = {
        'service_mgr': 'openwrt_init'
    }

    # Create Fake empty module
    test_module = type('AnsibleModule', (object,), {'get_bin_path': lambda self, _: None})

    def test_is_systemd_managed(self):
        return False

    def test_is_systemd_managed_offline(self):
        return False

# Generated at 2022-06-13 03:25:03.032218
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.collector import GenericFactCollector
    from ansible.module_utils.facts.collector import PlatformFactCollector
    from ansible.module_utils.facts.collector import DistributionFactCollector
    from ansible.module_utils.common.process import get_bin_path

    # Create a fake module object
    class FakeModule:
        def __init__(self, facts):
            self._facts = facts
            self._platform = facts['ansible_system']
            self._distribution = facts['ansible_distribution']
            self._distribution_version = facts['ansible_distribution_version']


# Generated at 2022-06-13 03:25:10.608070
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    '''
        Unit test function ServiceMgrFactCollector.is_systemd_managed_offline
    '''
    class FakeModule(object):
        def __init__(self):
            self.params = {
                '_ansible_remote_tmp': 'path/to/',
            }

        def get_bin_path(self, executable):
            return '/bin/systemctl'

    smfc = ServiceMgrFactCollector()
    assert not smfc.is_systemd_managed_offline(FakeModule())

    class FakeModule(object):
        def __init__(self):
            self.params = {
                '_ansible_remote_tmp': 'path/to/',
            }

        def get_bin_path(self, executable):
            return None

    smfc = ServiceMgrFactCollector()

# Generated at 2022-06-13 03:25:15.932519
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils import facts

    # All modules should inherit from the base 'FactsBase'
    assert issubclass(ServiceMgrFactCollector, facts.BaseFactsCollector)

    # This class's name attribute should match the file name
    assert ServiceMgrFactCollector.name == os.path.splitext(os.path.basename(__file__))[0]

    service_mgr = ServiceMgrFactCollector()

    # We need to construct a module object.  This is normally takend care of when the module gets executed but since
    # we don't execute the module we need to do it ourselves.
    module_args = dict(
        platform='Linux',
        distribution='Debian')

    module = MockModule(**module_args)

    # Construct a fake ansible_facts object to pass to the

# Generated at 2022-06-13 03:25:24.995772
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    """Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector"""

    class AnsibleModuleMock(object):
        def get_bin_path(self, s):
            return None

    service_mgr_fact_collector = ServiceMgrFactCollector()

    assert not service_mgr_fact_collector.is_systemd_managed_offline(AnsibleModuleMock())

    class AnsibleModuleMock(object):
        def get_bin_path(self, s):
            return True

    service_mgr_fact_collector = ServiceMgrFactCollector()

    assert not service_mgr_fact_collector.is_systemd_managed_offline(AnsibleModuleMock())


# Generated at 2022-06-13 03:25:35.972251
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts.utils import MockModule
    from ansible.module_utils.facts.collector import load_collectors

    collectors_defs = load_collectors()

    def mock_get_bin_path(name):
        if name == "systemctl":
            return "/bin/systemctl"
        return None

    module = MockModule({})
    module.get_bin_path = mock_get_bin_path

    # setup the test case
    os.environ.pop('SYSTEMD_NO_WRAP', None)
    os.environ.pop('INIT_SESSION', None)
    os.environ.pop('XDG_RUNTIME_DIR', None)

    facts = {}
    collector = ServiceMgrFactCollector()

    # test no canary
    os.en

# Generated at 2022-06-13 03:25:44.957063
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts.collector import ModuleStub
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import ServiceMgrFactCollector

    m = ModuleStub()
    b = BaseFactCollector(m)
    s = ServiceMgrFactCollector(b)

    # systemd running
    assert s.is_systemd_managed(m) is True

    # systemd not running
    m.run_command = lambda cmd, **kw: (1, '', '')
    assert s.is_systemd_managed(m) is False


# Generated at 2022-06-13 03:25:52.829587
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    # Make sure that is_systemd_managed returns True when systemd is used
    # as init system

    class _Module:
        def get_bin_path(self, arg):
            return "/bin/systemctl"

    # On Unix system it is hard to mock os.path.exists. Use os.mkdir
    # and os.rmdir for this purpose
    os.mkdir("/run/systemd/system/")
    smfc = ServiceMgrFactCollector()
    assert smfc.is_systemd_managed(_Module())
    os.rmdir("/run/systemd/system/")

    os.mkdir("/dev/.run/systemd/")
    assert smfc.is_systemd_managed(_Module())
    os.rmdir("/dev/.run/systemd/")

    os.mk

# Generated at 2022-06-13 03:26:00.524782
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():

    # Define a mock module
    module = type('module', (object,), {'get_bin_path': staticmethod(lambda *args, **kwargs: 'systemctl')})

    # Return value for is_systemd_managed method
    is_systemd_managed = True

    # Set 'is_systemd_managed' attribute of class ServiceMgrFactCollector to value of variable is_systemd_managed
    ServiceMgrFactCollector.is_systemd_managed = is_systemd_managed

    assert ServiceMgrFactCollector.is_systemd_managed(module=None) == is_systemd_managed


# Generated at 2022-06-13 03:26:35.084649
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    # GIVEN a mock module
    module = MockModule()

    # WHEN we create a new instance of the ServiceMgrFactCollector
    service_mgr_fact_collector = ServiceMgrFactCollector()

    # THEN we assume that the boolean value returned from is_systemd_managed is as expected
    assert(service_mgr_fact_collector.is_systemd_managed(module) == EXPECTED_RESULT)



# Generated at 2022-06-13 03:26:46.583024
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    class ModuleMock(object):
        def __init__(self):
            self.paths = ['*sbin*'] # systemctl binary location

        def get_bin_path(self, cmd):
            return cmd

    import tempfile
    from shutil import rmtree

# Generated at 2022-06-13 03:26:54.536811
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    module = Mock({'get_bin_path': lambda _: True, 'run_command': lambda _: (0, 'sshd', '')})
    collector = ServiceMgrFactCollector()

    # systemctl exists and files in /run/systemd/system/ exist: system is systemd managed
    module.stat.return_value.st_mode = 0o777
    assert collector.is_systemd_managed(module)

    # No files in /run/systemd/system/ exist and files in /dev/.run/systemd/ exist: system is systemd managed
    module.stat.reset_mock()
    module.stat.side_effect = [Mock({'st_mode': 0o0}), Mock({'st_mode': 0o777})]
    assert collector.is_systemd_managed(module)

    # No files in

# Generated at 2022-06-13 03:27:05.171473
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    # Define desired return values for module mocked functions
    path_exists_map = {
        '/proc/1/comm': False,
        '/sbin/init': False,
        '/sbin/openrc': True,
    }
    def path_exists_mock(path):
        return path_exists_map[path]

    get_file_content_map = {
        '/proc/1/comm': None,
    }
    def get_file_content_mock(path):
        return get_file_content_map[path]

    module_map = {
        'get_bin_path': lambda x: '/bin/systemctl' if x == 'systemctl' else None,
        'run_command': lambda x, use_unsafe_shell=False: (0, 'init', ''),
    }


# Generated at 2022-06-13 03:27:07.205945
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    collect_obj = ServiceMgrFactCollector()
    collected_facts = {'ansible_system':'SunOS'}
    collect_obj.collect(collected_facts=collected_facts)

# Generated at 2022-06-13 03:27:18.745366
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    import tempfile
    import os
    import shutil

    from ansible.module_utils.facts import get_module_path

    fake_systemd = "fake_systemd"
    path_to_systemd = os.path.join(os.path.dirname(get_module_path('ansible.module_utils.facts.service_mgr')),"files",fake_systemd)
    tmp_path = tempfile.mkdtemp()
    systemd_bin = os.path.join(tmp_path,fake_systemd)
    shutil.copyfile(path_to_systemd,systemd_bin)
    os.chmod(systemd_bin,0o755)

    class FakeModule(object):
        class FakeModuleError(Exception):
            pass


# Generated at 2022-06-13 03:27:30.101512
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    import pytest
    from ansible.module_utils import basic
    from ansible.module_utils.facts.collector import AnsibleCollector

    class ModuleMock(object):
        def __init__(self, *args, **kwargs):
            self.params = {}

        def fail_json(self, *args, **kwargs):
            self.exit_args = args
            self.exit_kwargs = kwargs
            raise Exception('FAIL')

        def exit_json(self, *args, **kwargs):
            self.exit_args = args
            self.exit_kwargs = kwargs

    module = ModuleMock()

    acol = AnsibleCollector(module=module)
    smcol = ServiceMgrFactCollector(module=module)

# Generated at 2022-06-13 03:27:41.021165
# Unit test for method collect of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_collect():
    import sys
    import inspect

    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.system.service_mgr import ServiceMgrFactCollector

    class MockModule(object):
        def __init__(self, name, get_bin_path_return_value, run_command_return_value_tuple):
            self.name = name
            self.get_bin_path_return_value = get_bin_path_return_value
            self.run_command_return_value_tuple = run_command_return_value_tuple

        def get_bin_path(self, name, opt_dirs=[]):
            self.name = name
            self.opt_dirs = opt_dirs
            return self.get_bin_path_return_value


# Generated at 2022-06-13 03:27:51.031252
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts import collector
    collector._set_collectors([], [])
    ServiceMgrFactCollector(BaseFactCollector)

    # reset mocked facts to default
    BaseFactCollector._COLLECTED_FACTS = {}

    # check for systemd
    BaseFactCollector._COLLECTED_FACTS['ansible_system'] = 'Linux'
    BaseFactCollector._COLLECTED_FACTS['service_mgr'] = 'systemd'
    BaseFactCollector._COLLECTED_FACTS['ansible_distribution'] = 'openSUSE'
    BaseFactCollector._COLLECTED_FACTS['ansible_distribution_release'] = '42.2'
    BaseFactCollector._

# Generated at 2022-06-13 03:28:02.227335
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    def is_systemd_managed_wrapper(module):
        return ServiceMgrFactCollector.is_systemd_managed(module)

    ServiceMgrFactCollector.is_systemd_managed = is_systemd_managed_wrapper

    assert not is_systemd_managed_wrapper(None)

    class MockModule(object):
        def __init__(self, module_name):
            self.module_name = module_name

        def get_bin_path(self, exe):
            return self.module_name

    assert not is_systemd_managed_wrapper(MockModule('/bin/systemctl'))

    class MockOsPath(object):
        def __init__(self):
            self.exists = False

        def exists(self, file_path):
            return self.exists

    mock_os_

# Generated at 2022-06-13 03:29:25.521785
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    class MockModule():
        def get_bin_path(self, cmd):
            return '/bin/systemctl'

    class MockOS():
        @staticmethod
        def path():
            class MockPath():
                @staticmethod
                def islink(path):
                    if path == '/sbin/init':
                        return True
                    else:
                        return False
            return MockPath

        @staticmethod
        def readlink(path):
            if path == '/sbin/init':
                return 'systemd'
            else:
                return '/sbin/init.sysvinit'

    module = MockModule()
    os = MockOS()
    (ServiceMgrFactCollector.is_systemd_managed_offline(module) is True)

# Generated at 2022-06-13 03:29:32.408838
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    import sys
    import datetime
    import json
    import os
    import platform
    import shlex
    import shutil
    import subprocess
    import tempfile
    import time
    import traceback

    import pytest

    from ansible.module_utils.facts import collector

    import ansible.module_utils.facts.collector.systemd
    import ansible.module_utils.facts.collector.service_mgr


    class ModuleMock:

        def __init__(self, systemctl_output=None, systemctl=None, module_utils=None):
            self._systemctl = systemctl_output
            self._systemctl_path = systemctl
            self._module_utils = module_utils


# Generated at 2022-06-13 03:29:42.774268
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.common.process import get_bin_path

    mgr = Collector()
    mgr.add_plugin(ServiceMgrFactCollector())
    facts = {}

    def mgen(path):
        return get_bin_path(path)

    class Module:
        @staticmethod
        def get_bin_path(path):
            return mgen(path)

    m = Module()
    facts['ansible_system'] = 'Linux'
    facts['ansible_lsb']['major_release'] = '7'
    assert ServiceMgrFactCollector.is_systemd_managed(m) == True

    facts['ansible_system'] = 'Linux'
    facts['ansible_lsb']['major_release']

# Generated at 2022-06-13 03:29:52.548242
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector

# Generated at 2022-06-13 03:29:55.753170
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    assert ServiceMgrFactCollector.is_systemd_managed(None) is False


# Generated at 2022-06-13 03:30:05.287898
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    import os
    import unittest
    import mock

    class AnsibleModuleFake(object):
        def __init__(self):
            self.run_command_result = (0, "systemd", None)
            self.get_bin_path_result = "/usr/bin/systemctl"

        def get_bin_path(self, arg):
            return self.get_bin_path_result

        def run_command(self, arg, use_unsafe_shell=False):
            return self.run_command_result

    # Test if method takes False for init is not systemd
    ServiceMgrFactCollector.is_systemd_managed_offline = classmethod(lambda _: False)
    ServiceMgrFactCollector.is_systemd_managed = classmethod(lambda _: False)
    module = AnsibleModuleFake()

# Generated at 2022-06-13 03:30:16.515225
# Unit test for method is_systemd_managed_offline of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed_offline():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.six.moves import mock
    import tempfile

    # create temporary file
    sbin_init = tempfile.NamedTemporaryFile(prefix="sbin_init", suffix="systemd")
    sbin_init_path = sbin_init.name

    # create mocked module
    with mock.patch('ansible.module_utils.facts.collector.Collector.get_file_path', return_value=sbin_init_path):
        collector = Collector()
        mock_module = mock.MagicMock()
        mock_module.run_command.return_value = (0, '', '')
        mock_module.get_bin_path = mock.MagicMock(return_value=sbin_init_path)


# Generated at 2022-06-13 03:30:27.149889
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    from ansible.module_utils.facts.collector import KernelSvcMgrCollector
    from ansible.module_utils.facts.collector import ServiceMgrFactCollector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.utils import get_file_content
    from ansible.module_utils.facts.utils import get_file_lines
    import tempfile

    class ModuleStub(object):
        def __init__(self):
            self._bin_paths = {}
            self.systemctl = None

        def get_bin_path(self, executable):
            return self._bin_paths[executable]


# Generated at 2022-06-13 03:30:32.418921
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    '''
    Test is_systemd_managed method in Class ServiceMgrFactCollector
    Return True if system is managed by systemd, otherwise return False
    '''
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={})
    result = ServiceMgrFactCollector.is_systemd_managed(module)
    if result:
        assert result == True
    else:
        assert result == False

# Generated at 2022-06-13 03:30:35.314408
# Unit test for method is_systemd_managed of class ServiceMgrFactCollector
def test_ServiceMgrFactCollector_is_systemd_managed():
    class Module(object):
        def get_bin_path(self, exe):
            if exe == 'systemctl':
                return '/bin/systemctl'
            return None
    service_mgr = ServiceMgrFactCollector()
    assert True == service_mgr.is_systemd_managed(module=Module())