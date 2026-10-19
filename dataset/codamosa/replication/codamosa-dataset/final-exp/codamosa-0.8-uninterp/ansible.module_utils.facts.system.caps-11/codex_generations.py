

# Generated at 2022-06-13 02:19:55.037434
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = AnsibleModuleMock()

# Generated at 2022-06-13 02:20:05.685983
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    capsh_path = '/usr/bin/capsh'


# Generated at 2022-06-13 02:20:12.999121
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE:
    # _collect() should not be called outside the 'collect()' method.
    # Therefore there is no need to test 'collect()' anymore and
    # no need to test '_fact_ids'.
    # Please test method collect only.
    # many thanks -akl
    class MockModule:
        def run_command(self, cmd, errors='surrogate_then_replace'):
            out = "Current: =ep"
            rc = 0
            err = ''
            return rc, out, err

        def get_bin_path(self, cmd):
            return '/path/to/capsh'

    class MockFactCollector:
        pass

    m  = MockModule()
    fc = MockFactCollector()
    scfc = SystemCapabilitiesFactCollector()

    # test unset "capsh"

# Generated at 2022-06-13 02:20:20.940890
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.basic import AnsibleModule
    import collections
    import unittest
    import tempfile
    import shutil

    class AnsibleModuleStub(object):
        def __init__(self, run_command_result=0, run_command_stdout='', run_command_stderr=''):
            self.run_command_result = run_command_result
            self.run_command_stdout = run_command_stdout
            self.run_command_stderr = run_command_stderr

        def run_command(self, command, errors='surrogate_then_replace'):
            return self.run_command_result, self.run_command_stdout, self.run_command_stderr


# Generated at 2022-06-13 02:20:24.951129
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    m = AnsibleModule(
            argument_spec = dict(),
            supports_check_mode = True
    )

    bc = SysctlFactCollector()
    bc.collect(m)
    m.exit_json(changed=False, ansible_facts=dict())

# Generated at 2022-06-13 02:20:36.096024
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    # sample facts file
    caps_sample = '''
Current: =ep
Bounding set =b
Securebits: 00/0x0/1'b0
 secure-noroot: no (unlocked)
 secure-no-suid-fixup: no (unlocked)
 secure-keep-caps: no (unlocked)
uid=3(syslog)
 gid=3(syslog)
 groups=3(syslog),27(sudo),28(puppet)
CapInh: =
CapPrm: =ep
CapEff: =ep
CapBnd: =ep
CapAmb: 
'''
    facts_dict = SystemCapabilitiesFactCollector().collect(None, {})
    assert facts_dict == {}

    # NOTE: import here to avoid circular imports -akl

# Generated at 2022-06-13 02:20:47.442478
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.system.capabilities.system_capabilities \
        import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts.system.capabilities.system_capabilities \
        import parse_caps_data


# Generated at 2022-06-13 02:20:57.696369
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: values of some items like 'system_capabilities' may change
    # based on the system where this unit test is ran.
    #
    # The values are taken from a Redhat Linux 6.9 system
    system_capabilities_collector = SystemCapabilitiesFactCollector()

# Generated at 2022-06-13 02:21:08.733247
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import ExitCollectorFacts, PathNotFoundError
    from ansible.module_utils.facts.utils import get_file_lines

    module = MockAnsibleModule()

    # Mock case: capsh_path is not available
    capsh_path = module.get_bin_path('capsh')
    m = Mock(side_effect=PathNotFoundError(capsh_path))
    with patch.object(module, 'run_command', m):
        collector = SystemCapabilitiesFactCollector()
        result = collector.collect(module)
        assert result['system_capabilities_enforced'] == 'NA'
        assert result['system_capabilities'] == []

    # Mock case: capsh_path is available
    m = Mock(side_effect=get_file_lines)


# Generated at 2022-06-13 02:21:09.344440
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:21:20.192911
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import pdb
    pdb.set_trace()
    facts_dict = {}

    capsh_path = '/bin/capsh' #  module.get_bin_path('capsh')


# Generated at 2022-06-13 02:21:31.635382
# Unit test for method collect of class SystemCapabilitiesFactCollector

# Generated at 2022-06-13 02:21:39.871052
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import sys

    # Python 2 and 3
    if sys.version_info[0] < 3:
        from mock import Mock
        from io import BytesIO as StringIO
    else:
        from unittest.mock import Mock
        from io import StringIO

    import ansible.module_utils.facts.collector

    test_collector = ansible.module_utils.facts.collector.SystemCapabilitiesFactCollector()


# Generated at 2022-06-13 02:21:49.381075
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.collector.system import SystemCollector

    sc = SystemCollector()
    facts_dict = sc.collect()
    sys_cap_fact_collector = get_collector_instance(SystemCapabilitiesFactCollector)

    # NOTE: maybe this could be improved. May be it can only be tested on an
    # actual system and not on a system where module code is running -akl
    sys_caps = sys_cap_fact_collector.collect(facts_dict)
    assert isinstance(sys_caps, dict)
    assert 'system_capabilities' in sys_caps
    assert 'system_capabilities_enforced' in sys_caps

# Generated at 2022-06-13 02:21:54.871385
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.facts.collectors.capabilities import SystemCapabilitiesFactCollector

    scfc = SystemCapabilitiesFactCollector()
    scfc.collect = lambda x: ['system_capabilities', 'system_capabilities_enforced']
    result = scfc.collect()
    assert type(result) == dict
    assert result == {'system_capabilities': 'system_capabilities', 'system_capabilities_enforced': 'system_capabilities_enforced'}

# Generated at 2022-06-13 02:21:55.414209
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:21:56.591100
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    my_SystemCapabilitiesFactCollector = SystemCapabilitiesFactCollector()

# Generated at 2022-06-13 02:22:03.491014
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """
    Unit tests for the collect method of the SystemCapabilitiesFactCollector
    class.
    """

    # NOTE: if this test fails, one likely cause is that the output
    # of the command 'capsh --print' has changed.  This is not
    # unusual since this command is intended to reflect the
    # capabilities of your system.  Update the test to reflect
    # a new output if possible. -akl

    # NOTE: Using multiple test cases might be useful in
    # determining the cause of a test failure. -akl

    # NOTE: mock_module is not used yet -akl
    mock_module = mock.Mock()

# Generated at 2022-06-13 02:22:13.274672
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = MockModule()

    capsh_path = '/usr/bin/capsh'
    module.run_command = Mock(
        return_value=(
            0,
            'Current: =ep',
            ''
        )
    )

    class Collector(SystemCapabilitiesFactCollector):
        def __init__(self, *args, **kwargs):
            self.module = module
            self.module.get_bin_path = Mock(return_value=capsh_path)

    collector = Collector()
    collected_facts = {}
    facts = collector.collect(module=module,
                              collected_facts=collected_facts)

    expected_facts = {'system_capabilities': [],
                      'system_capabilities_enforced': 'False'}

    assert facts == expected_facts


# Generated at 2022-06-13 02:22:23.288667
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import ansible.module_utils.facts.system.system_capabilities
    import ansible.module_utils.facts.collector
    class MockModule(object):
        def __init__(self):
            self.run_command_calls = []

        def get_bin_path(self, executable, required=False, opt_dirs=None):
            return capsh_path

        def run_command(self, cmd, errors='surrogate_then_replace'):
            self.run_command_calls.append(cmd)

# Generated at 2022-06-13 02:22:34.083724
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = MockModule()

# Generated at 2022-06-13 02:22:43.423353
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module_mock = Mock(return_value=(0, 'Current: =ep', ''))

    def fake_run_command(args, errors):
        return module_mock(args, errors)

    module = Mock()
    module.run_command = fake_run_command
    module.get_bin_path.return_value = '/usr/bin/capsh'
    collected_facts = Kollector()
    fact_collector = SystemCapabilitiesFactCollector()
    facts_dict = fact_collector.collect(module=module,
                                        collected_facts=collected_facts)

    assert facts_dict == {"system_capabilities_enforced": 'False',
                          "system_capabilities": []}


# Generated at 2022-06-13 02:22:46.188652
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    collector = SystemCapabilitiesFactCollector()
    assert collector.collect() == {}
    assert collector.collect() == {}

# Generated at 2022-06-13 02:22:55.521792
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import ansible.module_utils.facts.collectors.system.system_capabilities
    import ansible.module_utils.facts.collectors.system.system_capabilities
    import ansible.module_utils.facts.collectors.system.system_capabilities
    import ansible.module_utils.facts.collectors.system.system_capabilities
    import ansible.module_utils.facts.collectors.system.system_capabilities
    import ansible.module_utils.facts.collectors.system.system_capabilities
    import ansible.module_utils.facts.collectors.system.system_capabilities
    import ansible.module_utils.facts.collectors.system.system_capabilities
    import ansible.module_utils.facts.collectors.system.system_capabilities
    import ansible.module_utils.facts

# Generated at 2022-06-13 02:23:06.050164
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import tempfile


# Generated at 2022-06-13 02:23:13.722931
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import os
    import tempfile
    import unittest
    import AnsibleModuleFake
    import ansible.module_utils.facts.collector

    class FakeAnsibleModule(AnsibleModuleFake.AnsibleModuleFake):
        def get_bin_path(self, name):
            if name == 'capsh':
                return os.path.realpath(__file__)
            else:
                return None

    capsh_out_path = os.path.join(tempfile.mkdtemp(), 'capsh_out')
    capsh_out_path_link = os.path.join(tempfile.mkdtemp(), 'capsh_out_link')

# Generated at 2022-06-13 02:23:23.591863
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import sys
    import json

    # Get the stubbed module & fact_collector from the import
    from ansible.module_utils import basic
    from ansible.module_utils.facts import collector

    # Stub out the 'ansible' module
    sys.modules['ansible'] = basic
    sys.modules['ansible.module_utils.facts'] = collector

    # We don't care about the actual file, just the code loaded by pytest
    class MockModule(object):
        def get_bin_path(self, name, opt_dirs=[]):
            if name == 'capsh':
                return "/usr/bin/capsh"


# Generated at 2022-06-13 02:23:34.216044
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import sys
    import os
    import datetime
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts import cache
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils.facts.collector import set_unsafe_env_vars
    from ansible.module_utils.facts.collector import monotonic_time

    # Initialize the collector class and mock required functions
    # Time the collector class
    start_time = monotonic_time()
    capsh_collector = SystemCapabilitiesFactCollector()

    # Collect the facts
    collector_data = {}
    capsh_collector.collect()
    # Compute the elapsed time
   

# Generated at 2022-06-13 02:23:35.086674
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    assert SystemCapabilitiesFactCollector.collect()

# Generated at 2022-06-13 02:23:41.076884
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    m = _get_module_mock()
    c = SystemCapabilitiesFactCollector()

    # test case: capsh is not on machine
    m.params['ansible_capabilities'] = None
    assert c.collect(module=m) == {}

    # test case: capsh is on machine
    m.params['ansible_capabilities'] = {'system_capabilities': ['cap_chown', 'cap_dac_override'],
                                        'system_capabilities_enforced': 'True'}
    assert c.collect(module=m) == {'system_capabilities': ['cap_chown', 'cap_dac_override'],
                                   'system_capabilities_enforced': 'True'}


# Generated at 2022-06-13 02:24:02.132974
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: system module object is created and passed to the collector -akl
    system_instance = SystemCapabilitiesFactCollector()
    # NOTE: system module's get_bin_path() is called, with capsh as the argument
    #       and the return value is stored in capsh_path.
    capsh_path = system_instance.module.get_bin_path('capsh')
    if capsh_path:
        rc, out, err = system_instance.module.run_command([capsh_path, "--print"])

    # Return value of the collect method
    return_value = {'system_capabilities_enforced': 'NA',
                    'system_capabilities': []}
    for line in out.splitlines():
        if len(line) < 1:
            continue

# Generated at 2022-06-13 02:24:09.342931
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    from ansible.module_utils.facts.collector import get_collector_instance

    # Mock the module and it's basic facts
    module_mock = ImmutableMock()
    module_mock.get_bin_path.return_value = '/test/bin/capsh'

# Generated at 2022-06-13 02:24:21.062660
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Test 'system_capabilities_enforced' fact is set
    module = ansible_mock.AnsibleModule

# Generated at 2022-06-13 02:24:29.707600
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import ModuleFacts
    import re

    temp_module = ModuleFacts()
    temp_module.run_command = lambda command, errors: ['Current:  = cap_setpcap,'
            'cap_setfcap+eip cap_net_bind_service', '']
    temp_module.get_bin_path = lambda command: '/bin/capsh'

    fact_collector = SystemCapabilitiesFactCollector(temp_module)
    facts_dict = fact_collector.collect(temp_module)

    assert facts_dict['system_capabilities_enforced'] == 'True'
    assert facts_dict['system_capabilities'] == ['cap_setpcap', 'cap_setfcap', 'cap_net_bind_service']

# Generated at 2022-06-13 02:24:36.922849
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    class SystemCapabilitiesFactCollectorMockedModule:
        def __init__(self):
            self.params = {}
            self.params['shell'] = ''
            self.params['_uses_shell'] = False
            self.params['_raw_params'] = ''
            self.params['_binary_suffix'] = False
            self.run_command = lambda args, **kwargs: ''

        def get_bin_path(self, name, opt_dirs=[]):
            return name

    class SystemCapabilitiesFactCollectorMockedFacts:
        def __init__(self):
            pass

    mp = SystemCapabilitiesFactCollectorMockedModule()
    mf = SystemCapabilitiesFactCollectorMockedFacts()
    sc = SystemCapabilitiesFactCollector()

# Generated at 2022-06-13 02:24:47.664490
# Unit test for method collect of class SystemCapabilitiesFactCollector

# Generated at 2022-06-13 02:24:49.125706
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # FIXME: Need to write test for SystemCapabilitiesFactCollector.collect()
    #        https://github.com/ansible/ansible-modules-core/issues/3372 -akl
    pass

# Generated at 2022-06-13 02:24:53.185159
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils import basic
    from ansible.module_utils.facts import collector

    module = basic.AnsibleModule(
        argument_spec = dict()
    )

    mock_module = collector.get_module_mock()
    mock_module.get_bin_path.return_value = '/usr/bin/capsh'
    mock_module.run_command.return_value = (0, 'Current: =ep', '')

    result = SystemCapabilitiesFactCollector().collect(module=mock_module, collected_facts=dict())
    assert result == {'system_capabilities': [], 'system_capabilities_enforced': 'False'}

# Generated at 2022-06-13 02:25:03.866665
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = MockModule()

# Generated at 2022-06-13 02:25:11.295953
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import sys
    import os
    import pwd

    # collect() needs a module() as arg, so fake one
    class FakeModule:
        def __init__(self, args=None):
            self.argv = sys.argv
            self.user = pwd.getpwuid(os.geteuid()).pw_name
            self.env = os.environ.copy()
            self.run_command = run_command_mock

    # collect() needs a CmdRunner() as arg, so fake one
    class FakeCmdRunner:
        def get_bin_path(self,cmd, required=False):
            if cmd == "capsh":
                return "/bin/capsh"
            elif cmd == "crash":
                return None

    testobj = SystemCapabilitiesFactCollector()

# Generated at 2022-06-13 02:25:46.592519
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import mock
    import os

    # NOTE: 'module.run_command' mocked below
    with mock.patch.dict(os.environ, {'PATH': '/sbin'}):
        # NOTE: mock a module object and the run_command method
        module = mock.MagicMock()
        module.get_bin_path.return_value = '/sbin/capsh'
        module.run_command.return_value = 0, 'Current: =ep', ''

        # NOTE: define two "facts" that we're testing
        fact_ids = set(['system_capabilities', 'system_capabilities_enforced'])

        # NOTE: instantiate a SystemCapabilitiesFactCollector object, and call the collect method
        sys_caps_collector = SystemCapabilitiesFactCollector()
        facts = sys_caps_collector.collect

# Generated at 2022-06-13 02:25:53.768518
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = AnsibleModule(argument_spec={'test_unit': {'type': 'bool', 'default': False}})
    mock_capsh_path = '/bin/capsh'

# Generated at 2022-06-13 02:25:59.133482
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.capabilities import SystemCapabilitiesFactCollector
    fact_collector = SystemCapabilitiesFactCollector()
    facts_dict = fact_collector.collect()
    assert 'system_capabilities_enforced' in facts_dict
    assert 'system_capabilities' in facts_dict

# Generated at 2022-06-13 02:26:02.056671
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """SystemCapabilitiesFactCollector - unit test for collect method."""

    # NOTE: use of mock module instead to run a specific code path
    # https://docs.python.org/3/library/unittest.mock.html#quick-guide

# Generated at 2022-06-13 02:26:09.732575
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils import basic
    from ansible.module_utils.facts.collector import Collector

    # Used for testing purposes only

# Generated at 2022-06-13 02:26:19.598769
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import ansible.module_utils.facts.collector
    from ansible.module_utils.facts.collector import SystemCapabilitiesFactCollector
    import subprocess
    import ansible.module_utils.basic
    import ansible.module_utils.facts.cache
    import ansible.module_utils.facts

    class MockModule(object):
      def __init__(self):
        self.exit_json = ansible.module_utils.basic.AnsibleModule.exit_json
        self.fail_json = ansible.module_utils.basic.AnsibleModule.fail_json


# Generated at 2022-06-13 02:26:28.451509
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.system.caps
    import ansible.module_utils.facts.system
    import ansible.module_utils.facts
    import ansible.module_utils.facts.utils
    import tempfile
    import os

    test_obj = ansible.module_utils.facts.collector.BaseFactCollector()
    test_system_caps = ansible.module_utils.facts.system.caps.SystemCapabilitiesFactCollector()
    test_system_summary = ansible.module_utils.facts.system.summary.SystemSummaryFactCollector()
    test_system_distribution = ansible.module_utils.facts.system.distribution.SystemDistributionFactCollector()
    test_system_selinux = ansible.module_utils.facts

# Generated at 2022-06-13 02:26:37.877637
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.collector.capsh import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils import basic
    from ansible.module_utils.six import iteritems

    module = basic.AnsibleModule(argument_spec={})
    module.run_command = basic.AnsibleModule.run_command
    facts_dict = {
        'system_capabilities': [],
        'system_capabilities_enforced': 'True',
        'system_capabilities_bak': None,
        'system_capabilities_enforced_bak': None
    }

    BaseFactCollector.pop

# Generated at 2022-06-13 02:26:43.707391
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: Define a module mock so that we can test the method without the
    #       need to patch all the things the method depends on and without
    #       the need to have a working capsh binary installed.
    class ModuleMock(object):
        def __init__(self, state):
            self.state = state

        def get_bin_path(self, name, required=False, opt_dirs=[]):
            # No need to call get_bin_path() anyway, since we will mock
            # run_command() anyways.
            return None


# Generated at 2022-06-13 02:26:53.613902
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.system.capabilities import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts.system.capabilities import get_caps_data
    from ansible.module_utils.facts.system.capabilities import parse_caps_data
    from ansible.module_utils.six import PY3
    import mock

    capsh_path = '/bin/capsh'

    # Test: capsh returns data and raises no errors

# Generated at 2022-06-13 02:27:56.886757
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # TODO: unit test for method collect of class SystemCapabilitiesFactCollector
    pass

# Generated at 2022-06-13 02:28:03.539899
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    fake_module = None

# Generated at 2022-06-13 02:28:04.036639
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:28:09.081018
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import cutils
    m = cutils.get_ansible_module()
    c = SystemCapabilitiesFactCollector()
    f = c.collect(module=m)
    assert f.get('system_capabilities') is not None
    assert f.get('system_capabilities_enforced') is not None
    assert f.get('system_capabilities') != []

# Generated at 2022-06-13 02:28:19.519670
# Unit test for method collect of class SystemCapabilitiesFactCollector

# Generated at 2022-06-13 02:28:20.033355
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:28:21.660351
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import CapshFactCollec

# Generated at 2022-06-13 02:28:22.836174
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: for now - just return empty dict to satisfy flake8 unused args rule
    pass

# Generated at 2022-06-13 02:28:32.199472
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import subprocess
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.collector.system.caps import SystemCapabilitiesFactCollector

    # Mock class 'BaseFactCollector'
    BaseFactCollector_mock = BaseFactCollector
    BaseFactCollector_mock.get_file_content = lambda self, filename: '''Current: =ep
        CapInh: 00000000a80425fb
        CapPrm: 00000000a80425fb
        CapEff: 00000000a80425fb
        CapBnd: 00000000a80425fb
        CapAmb: 0000000000000000'''.splitlines()

    # Mock class 'collector'
    collector_mock = collector

# Generated at 2022-06-13 02:28:40.750962
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """ system_capability_collector: collect() unit test """
    import json
    import shlex
    import mock

    test_fact_ids = ['system_capabilities', 'system_capabilities_enforced']

    module = mock.Mock()