

# Generated at 2022-06-13 02:19:55.932934
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    def module_mock(path):
        return ['capsh']
    module_mock.run_command = run_command_mock
    sut = SystemCapabilitiesFactCollector()
    sut.get_bin_path = module_mock
    rc, out, err = run_command_mock(None, None)

    actual = sut.collect()


# Generated at 2022-06-13 02:19:57.958875
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # tested method
    collector = SystemCapabilitiesFactCollector()
    collected_facts = collector.collect()
    #assert collected_facts == test_facts

# Generated at 2022-06-13 02:20:01.856570
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    test_module = DummyAnsibleModule()
    # NOTE: needs binaries on PATH -akl
    test_collector = SystemCapabilitiesFactCollector(test_module)

    assert 'system_capabilities_enforced' in test_collector.collect()



# Generated at 2022-06-13 02:20:10.944061
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import tempfile
    import os
    test_cmd = ['capsh', '--print']
    print(test_cmd)

# Generated at 2022-06-13 02:20:13.278568
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    assert callable(SystemCapabilitiesFactCollector)
    assert SystemCapabilitiesFactCollector().collect() == {}

# Generated at 2022-06-13 02:20:18.283516
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = ModuleStub()
    fact_collector = SystemCapabilitiesFactCollector()
    collected_facts = {}
    system_caps = fact_collector.collect(module, collected_facts)
    assert len(system_caps) == 2
    assert system_caps['system_capabilities_enforced'] == 'True'

# Generated at 2022-06-13 02:20:25.325905
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Create a module object
    module = AnsibleModule(argument_spec={}, supports_check_mode=False)

    # Create a subclass of SystemCapabilitiesFactcollector
    MySystemCapabilitiesFactCollector = type(
        'MySystemCapabilitiesFactCollector', (SystemCapabilitiesFactCollector, object), {'_capsh_path': '/path/to/capsh'})

    # Create a subpocess class mock 'module.run_command'
    class MockProcess(object):
        def __init__(self):
            self.stdout = 'Current: =ep'
            self.stderr = ''
            self.rc = 0
    module.run_command = Mock(return_value=MockProcess())

    # Create a subclass of AnsibleModule for mocking

# Generated at 2022-06-13 02:20:36.337262
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import sys

    if sys.version_info[0] < 3:
        from mock import MagicMock
    else:
        from unittest.mock import MagicMock
    from ansible_collections.ansible.community.plugins.module_utils.facts import collector
    import ansible_collections.ansible.community.plugins.module_utils.facts.system.caps

    caps_mock = ansible_collections.ansible.community.plugins.module_utils.facts.system.caps.capsh_path = MagicMock(return_value='/bin/capsh')
    caps_mock = ansible_collections.ansible.community.plugins.module_utils.facts.system.caps.run_command = MagicMock(return_value=(0, 'Current: =ep\nBounding set =ep', ''))


# Generated at 2022-06-13 02:20:47.675705
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module_mock = Mock()
    module_mock.run_command.return_value = (0, """\
Current: =ep
Bounding set =eip
Securebits: 00/0x0/1'b0 secure-noroot, nosuid, noexec, noadduser, nokilled
          Capability Bounding set =eip
           Capabilities:

Inheritable:
Securebits: 00/0x0/1'b0 secure-noroot, nosuid, noexec, noadduser, nokilled
          Capability Bounding set =eip
           Capabilities: =eip
""", "")

    capsh_path = None
    module_mock.get_bin_path.return_value = capsh_path
    obj = SystemCapabilitiesFactCollector()

# Generated at 2022-06-13 02:20:49.812194
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # TODO: proper test case needs to be written, mocking os.access related stuff was not easy... -akl
    pass

# Generated at 2022-06-13 02:21:03.608198
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module_mock = Mock(name="module")
    module_mock.run_command.return_value = (1, "Current: =ep\n    Bounding set =cap_kill,cap_setpcap\n    Securebits: 00/0x0/1'b0\n    secure-noroot: no (unlocked)\n    secure-no-suid-fixup: no (unlocked)\n    secure-keep-caps: no (unlocked)\n    uid=0(root) gid=0(root) egid=0(root)", "")
    capsh_fact = SystemCapabilitiesFactCollector(module_mock)
    caps = capsh_fact.collect()
    expected_caps = dict(system_capabilities = [], system_capabilities_enforced = 'False')
    assert caps == expected_caps

# Generated at 2022-06-13 02:21:11.489552
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule

    # NOTE: pylint: disable=protected-access
    # NOTE: This is a generic mock class for any class that inherits from BaseFactCollector
    class CollectMock(BaseFactCollector):
        _fact_ids = set(['fact1'])
        def __init__(self, module):
            self.module = module

        def collect(self, module=None, collected_facts=None):
            return {}

    mock_module = AnsibleModule({})

    # NOTE: Mock out the BaseFactCollector._get_bin_path() method. It is not necessary to mock the
    # whole BaseFactCollector class, as

# Generated at 2022-06-13 02:21:19.204650
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector.system import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts import callback_facts

    # setup
    enforced = 'True'

# Generated at 2022-06-13 02:21:22.892823
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    sys_cap_fact_collector = SystemCapabilitiesFactCollector()
    sys_cap_fact_collector.module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True,
    )

# Generated at 2022-06-13 02:21:34.584220
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Prepare test
    #from ansible.module_utils.facts.system.system_capabilities import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts.system.system_capabilities import SystemCapabilitiesFactCollector
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.system.system_capabilities import test_SystemCapabilitiesFactCollector_collect_inputs
    SystemCapabilitiesFactCollector.collect()
    capsh_path = "/usr/bin/capsh"
    run_command_mock = Mock()
    run_command_mock.return_value = test_SystemCapabilitiesFactCollector_collect_inputs.run_command_result
    get_bin_path_mock = Mock()
    get_

# Generated at 2022-06-13 02:21:36.544429
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: method should return a dict, not a string...
    assert(type(SystemCapabilitiesFactCollector().collect()) is dict)

# Generated at 2022-06-13 02:21:44.051735
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    # NOTE: These are not real tests but rather 'stubs' for now.   As such,
    # they are not being included in the test scaffolding.
    #         TODO:  Convert these to actual tests.
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector.system import SystemCapabilitiesFactCollector

    fact_collector = SystemCapabilitiesFactCollector()
    fact_collector.collect()

    return True

# Generated at 2022-06-13 02:21:51.854164
# Unit test for method collect of class SystemCapabilitiesFactCollector

# Generated at 2022-06-13 02:21:59.924300
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    # Setup module
    module = Mock()
    module.get_bin_path.return_value = 'test_bin_path'
    module.run_command.return_value = (0, 'test_out', 'test_err')

    # Create a fact collector object
    fact_collector = SystemCapabilitiesFactCollector()

    # Call the method collect
    collected_facts = {'network_resources': []}
    result = fact_collector.collect(module, collected_facts)

    # Verify the result
    assert result['system_capabilities'] == []
    assert result['system_capabilities_enforced'] == 'NA'
    module.get_bin_path.assert_called_with('capsh')

# Generated at 2022-06-13 02:22:05.699339
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Preconditions:
    from ansible.module_utils.facts.collector import AnsibleCollector
    import os
    import sys
    import yaml


    class TestModule(object):
        def __init__(self):
            self.run_command = os.system
            self.get_bin_path = lambda x: x

    if sys.version_info[0] < 3:
        import __builtin__ as builtins
    else:
        import builtins

    saved_open = builtins.open

    def _mock_open(name, mode='r'):
        class _MockFile(object):
            def read(self, size=None):
                return '{"system_capabilities_enforced": false}'


# Generated at 2022-06-13 02:22:20.585235
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.collector import get_collector_instance

    # Create a mock module with 'GetBinPath' method that returns '/usr/bin/capsh'
    class MockModule:
        def get_bin_path(self, bin_name, required=True):
            return '/usr/bin/capsh'


# Generated at 2022-06-13 02:22:30.102568
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import AnsibleModule
    from sys import platform
    from ansible.module_utils.basic import AnsibleModuleMockBuilder, AnsibleModuleTestCase
    def mock_collect(self, module=None, collected_facts=None):
        facts_dict = {}
        if not module:
            return facts_dict
        capsh_path = module.get_bin_path('capsh')
        if capsh_path:
            rc, out, err = module.run_command([capsh_path, "--print"], errors='surrogate_then_replace')
            enforced_caps = []
            enforced = 'NA'
            for line in out.splitlines():
                if len(line) < 1:
                    continue

# Generated at 2022-06-13 02:22:32.715814
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """
    Test method collect of class SystemCapabilitiesFactCollector

    """
    collector = SystemCapabilitiesFactCollector()
    assert collector.collect() == {'system_capabilities': [], 'system_capabilities_enforced': 'NA'}

# Generated at 2022-06-13 02:22:41.326592
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import AnsibleModule

    module = AnsibleModule(
        argument_spec={}
    )
    capsh_path = module.get_bin_path('capsh')
    if not capsh_path:
        raise Exception("capsh binary not found in PATH")

    capscollector = SystemCapabilitiesFactCollector()
    data = capscollector.collect(module=module)
    assert set(data.keys()) == set(['system_capabilities_enforced', 'system_capabilities'])
    assert isinstance(data['system_capabilities_enforced'], str)
    assert data['system_capabilities_enforced'] in ['NA', 'True', 'False']
    assert isinstance(data['system_capabilities'], list)

# Generated at 2022-06-13 02:22:52.060340
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector.system.system_capabilities import SystemCapabilitiesFactCollector
    import pytest

    # Mock class base_module()
    class mock_base_module():
        def __init__(self):
            self.params = { 'gather_subset': ['all']}
            self.facts = {}
            self.changed = False

        def get_bin_path(self, binary, required=False, opt_dirs=[]):
            return "/usr/bin/capsh"


# Generated at 2022-06-13 02:22:59.439920
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts.facts import Facts
    import json
    import os

    # setup for unit tests:
    # make a dict for test of SystemCapabilitiesFactCollector.collect
    # and add information from platform, os.uname and os.environ
    collected_facts = dict()
    collected_facts.update(Facts().populate())

# Generated at 2022-06-13 02:23:00.575419
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass


# Generated at 2022-06-13 02:23:09.713387
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    #test case #1
    from ansible.module_utils.facts import settings
    _module = settings.FakeModule()
    _module.run_command = lambda x, **kw: (0, 'Current: = cap_net_admin,cap_export,cap_chown', '')
    col = SystemCapabilitiesFactCollector()
    assert col.collect(_module) == {'system_capabilities_enforced': 'True', 'system_capabilities': ['cap_net_admin', 'cap_export', 'cap_chown']}

    #test case #2
    _module.run_command = lambda x, **kw: (0, 'Current: =ep ', '')
    col = SystemCapabilitiesFactCollector()

# Generated at 2022-06-13 02:23:19.892694
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # create a SystemCapabilitiesFactCollector object
    from ansible.module_utils.facts.collectors import SystemCapabilitiesFactCollector
    foo = SystemCapabilitiesFactCollector()
    # create a mocker for the package ansible.module_utils.basic
    from ansible.module_utils.basic import AnsibleModule
    mocker = Mocker()
    basic = mocker.patch(AnsibleModule)
    # call the collect function on the object
    foo.collect()
    # assert that the function run_commnad was called with the correct parameter
    basic.run_commnad.assert_called_with([capsh_path, "--print"], errors='surrogate_then_replace')
    # assert that the system_capabilities dictionary was created with the correct values

# Generated at 2022-06-13 02:23:30.191943
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # -akl
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collector import get_collector

    class fake_module:
        def get_bin_path(self):
            pass
        def run_command(self):
            pass

    fake_module = fake_module()

    fake_base_fact_collector = BaseFactCollector(fake_module)
    fake_collector = Collector(fake_base_fact_collector)
    fake_get_collector = get_collector(fake_collector)

    # -akl

    test_case = SystemCapabilitiesFactCollector(fake_get_collector)
    # NOTE: More cases needed to be added. -ak

# Generated at 2022-06-13 02:23:50.494396
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import AnsibleModuleStub
    from ansible.module_utils.facts.collector.system.caps import SystemCapabilitiesFactCollector
    import os

    # Create AnsibleModuleStub
    module = AnsibleModuleStub()
    # NOTE: add 'capsh.py' script to $PATH for testing
    capsh_path = os.path.realpath(os.path.join(os.path.dirname(__file__), 'capsh.py'))
    module.PATH = [os.path.dirname(capsh_path), ] + module.PATH
    # Set 'capsh' to return exitcode 0 and mocked/fake output data

# Generated at 2022-06-13 02:23:53.117740
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    sys_caps = SystemCapabilitiesFactCollector()
    assert sys_caps.collect() == {'system_capabilities': [], 'system_capabilities_enforced': 'NA'}

# Generated at 2022-06-13 02:23:54.891797
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    # Init class
    system_capabilities = SystemCapabilitiesFactCollector()
    system_capabilities.collect()

# Generated at 2022-06-13 02:24:02.952756
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = [None]
    collected_facts = [None]
    system_capabilities_collector = SystemCapabilitiesFactCollector()
    data_capsh_path = ['/usr/bin/capsh']
    data_rc_out_err_case1 = [0, 'Current: =ep\n', '']
    data_rc_out_err_case2 = [0, 'Current: =ep\n', '']
    data_rc_out_err_case3 = [0, 'Current: =eip cap_net_raw\n', '']
    data_rc_out_err_case4 = [0, 'Current: =eip cap_net_raw\n', '']
    data_rc_out_err_case5 = [0, 'Current: =eip cap_net_raw\n', '']


# Generated at 2022-06-13 02:24:05.848316
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    SystemCapabilitiesFactCollector.collect(module_mock)
    data = module_mock.run_command.call_args[0][0]
    assert data[0] == '/usr/bin/capsh'
    assert data[1] == "--print"



# Generated at 2022-06-13 02:24:13.159238
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    mock_module = Mock()
    mock_module.get_bin_path.return_value = '/bin/capsh'

# Generated at 2022-06-13 02:24:23.614341
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import ansible.module_utils.facts.system.caps
    import ansible.module_utils.facts.system.distribution
    # create fact collector
    fact_collector = ansible.module_utils.facts.system.caps.SystemCapabilitiesFactCollector()
    # create module obj
    class mock_module():
        def __init__(self, module_name):
            self.module_name = module_name
        def get_bin_path(self, command):
            if command == 'capsh':
                return '/usr/bin/capsh'
            else:
                return False
        def run_command(self, command, errors='surrogate_then_replace'):
            return (0, 'Current: = cap_setgid,cap_setuid+ep', '')

# Generated at 2022-06-13 02:24:32.463588
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    mock_module = MockModule()
    mock_module.run_command.return_value = (0, 'Current: =ep', '')
    # test collect() when 'capsh' is installed
    caps_fact_collector = SystemCapabilitiesFactCollector()
    facts_dict = caps_fact_collector.collect(mock_module, None)
    assert 'system_capabilities_enforced' in facts_dict
    assert 'system_capabilities' in facts_dict
    assert facts_dict['system_capabilities_enforced'] == 'False'
    assert facts_dict['system_capabilities'] == []
    # test collect() when 'capsh' is not installed
    caps_fact_collector._capsh_path = None
    facts_dict = caps_fact_collector.collect(mock_module, None)
   

# Generated at 2022-06-13 02:24:38.974684
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """
    Test if method SystemCapabilitiesFactCollector.collect returns expected 
    data when given a `ansible.module_utils.basic.Module` with 
    `ansible.module_utils.facts.collector.BaseFactCollector.get_bin_path`
    stubbed, and `ansible.module_utils.basic.Module.run_command()` stubbed
    to return values for capsh(1) command
    """
    from ansible.module_utils.facts import c_system_capabilities
    from ansible.module_utils.basic import Module
    from ansible.module_utils.facts.collector import BaseFactCollector
    import os

    capsh_path = os.path.join(os.sep, 'usr', 'bin', 'capsh')

# Generated at 2022-06-13 02:24:47.987068
# Unit test for method collect of class SystemCapabilitiesFactCollector

# Generated at 2022-06-13 02:25:24.866666
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    m = mock.mock_module_helper()
    pc = SystemCapabilitiesFactCollector()

# Generated at 2022-06-13 02:25:32.671743
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import ansible_collector


# Generated at 2022-06-13 02:25:43.551593
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    # Setup
    # Use mocked version of module, so we can mock subprocess calls
    from ansible.module_utils.facts import module
    from ansible.module_utils.facts import ansible_module
    MockedModule = ansible_module.AnsibleModule
    am = MockedModule()

    cfc = SystemCapabilitiesFactCollector(module=am)

# Generated at 2022-06-13 02:25:51.566393
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = AnsibleModuleStub()
    module.run_command = AnsibleModuleMock.run_command
    fact_collector = SystemCapabilitiesFactCollector()
    actual = fact_collector.collect(module)

# Generated at 2022-06-13 02:26:01.638179
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """
    SystemCapabilitiesFactCollector.collect() returns ansible_facts
    """
    # Setup
    module_args = {}
    module_mock = MagicMock()

# Generated at 2022-06-13 02:26:09.435985
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import json
    import os
    import unittest

    class SystemCapabilitiesFactCollector_test(unittest.TestCase):
        def setUp(self):
            class module(object):
                def get_bin_path(self, pathname, opt_dirs=[]):
                    print("find %s" % pathname)
                    return pathname

                def run_command(self, cmd, errors='surrogate_then_replace'):
                    print("run: %s" % cmd)
                    out = None
                    err = None

# Generated at 2022-06-13 02:26:15.181217
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = MagicMock()
    module.get_bin_path.return_value = '/usr/bin/capsh'
    module.run_command.return_value = 0, 'Current: =ep', ''
    cap_collector = SystemCapabilitiesFactCollector()
    fact_data = cap_collector.collect(module)
    assert fact_data['system_capabilities_enforced'] == 'False'
    assert fact_data['system_capabilities'] == []


# Generated at 2022-06-13 02:26:24.165975
# Unit test for method collect of class SystemCapabilitiesFactCollector

# Generated at 2022-06-13 02:26:25.888944
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    Collector1 = SystemCapabilitiesFactCollector()
    test_dict = Collector1.collect('module')
    assert test_dict is not None

# Generated at 2022-06-13 02:26:36.230453
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import ansible.module_utils.facts.collector

    # Test with a faked module, mocked capsh output
    class FakeModule:
        def get_bin_path(self, binpath):
            return '/bin/capsh'
        def run_command(self, cmd, errors='surrogate_then_replace'):
            return (0, 'Current: =ep\nAmbient: =\nBounding set =ep', '')

    # Collect what module_utils.facts.collector.collect_from_collectors returns
    result = ansible.module_utils.facts.collector.collect_from_collectors([SystemCapabilitiesFactCollector()])
    # Test if the fact was collected
    assert "system_capabilities" in result
    assert result['system_capabilities'] == []

# Generated at 2022-06-13 02:27:49.053116
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """
    Unit test for method collect of class SystemCapabilitiesFactCollector
    """

    import sys
    import os
    import unittest
    import mock
    import sys

    if sys.version_info[0] < 3:
        from io import BytesIO
    else:
        from io import StringIO as BytesIO

    from ansible.module_utils import basic
    from ansible.module_utils.facts import collector

    def get_bin_path(self, arg, opt_dirs=[]):
        return 'capsh'


# Generated at 2022-06-13 02:28:00.114929
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    class TestModule(object):
        def __init__(self, out, rc=0, err=''):
            self.out = out
            self.rc = rc
            self.err = err

        def get_bin_path(self, _):
            pass

        def run_command(self, cmd, _):
            out = self.out
            rc = self.rc
            err = self.err
            return rc, out, err

    obj = SystemCapabilitiesFactCollector()
    # NOTE: we should use 'caps' as the param here I think, not capsh?  -akl

# Generated at 2022-06-13 02:28:02.070553
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: not a whole lot to test here -akl
    SystemCapabilitiesFactCollector().collect(collected_facts=dict())

# Generated at 2022-06-13 02:28:10.653634
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    import tempfile

# Generated at 2022-06-13 02:28:21.517259
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    module_return_values = [
        (0, 'Current:\n	 = ep', ''),
        (0, 'Current:\n	 = cap_net_admin+eip', ''),
        (3, '', ''),
    ]
    module_return_values_int = itertools.cycle(module_return_values)
    module.run_command = lambda command, check_rc=True, errors='surrogate_then_replace': next(module_return_values_int)
    capsh_path = module.get_bin_path('capsh')
    SystemCapabilitiesFactCollector_collect_result = SystemCapabilitiesFactCollector().collect(module)

# Generated at 2022-06-13 02:28:30.859674
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Set up a module object for mocked functions
    module = AnsibleModule(argument_spec={})
    # Set up a class object for the facts collector under test
    sut = SystemCapabilitiesFactCollector()

    assert (sut.collect(module)['system_capabilities_enforced'] is 'NA')

    # set up some mock values
    rc = 0

# Generated at 2022-06-13 02:28:34.131631
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    collector = SystemCapabilitiesFactCollector()
    assert collector.collect() == {'system_capabilities': [], 'system_capabilities_enforced': 'NA'}

# Generated at 2022-06-13 02:28:40.811440
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import ansible.module_utils.facts.system.caps

    module = ansible.module_utils.facts.system.caps
    module.run_command = run_command
    module.get_bin_path = get_bin_path

    fact_collector = SystemCapabilitiesFactCollector()
    collected_facts = fact_collector.collect(
        collected_facts=None,
        module=module
    )
    assert collected_facts == {
        'system_capabilities_enforced': 'False',
        'system_capabilities': []
    }

# Mock to simulate method 'run_command' of class 'Common'

# Generated at 2022-06-13 02:28:44.752162
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = mock.MagicMock()
    module.get_bin_path.side_effect = ['/usr/bin/capsh']
    module.run_command.side_effect = [(0, 'Current: =ep', '')]

    collector = SystemCapabilitiesFactCollector()
    assert collector.collect() == {'system_capabilities': [], 'system_capabilities_enforced': 'False'}


# Generated at 2022-06-13 02:28:52.618902
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.utils.capsh import get_caps_data
    from ansible.module_utils.facts.collectors import gather_subset
    from ansible.module_utils.facts.utils.capsh import parse_caps_data
    from ansible.psuedo_set import PSuedoSet
    from ansible.module_utils.facts.collectors.system.capabilities import SystemCapabilitiesFactCollector

    caps_data = get_caps_data()
    augmented_subset = PSuedoSet(gather_subset(subset='facts.system.capabilities'))
    facts_result = parse_caps_data(module=None, facts_data=caps_data, fact_subset=augmented_subset)
    system_capabilities_fact_collector = SystemCapabilitiesFactCollector