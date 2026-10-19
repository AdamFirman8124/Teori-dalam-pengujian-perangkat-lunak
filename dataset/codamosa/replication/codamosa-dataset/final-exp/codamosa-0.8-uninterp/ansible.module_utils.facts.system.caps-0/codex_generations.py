

# Generated at 2022-06-13 02:19:55.349858
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils._text import _text
    from ansible.module_utils.facts.collector import get_collector_instance


# Generated at 2022-06-13 02:20:06.105285
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = mock.Mock()
    module.get_bin_path.return_value = '/capsh'

    rc = 0

# Generated at 2022-06-13 02:20:13.229942
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import json
    import os
    import sys
    try:
        from ansible.module_utils.facts.collector import BaseFactCollector
    except Exception as e:
        if os.path.exists('/tmp/ansible_collections/ansible/community/general/plugins/module_utils/facts/collector.py'):
            sys.path.insert(0, '/tmp/ansible_collections/ansible/community/general/plugins/module_utils/facts')
            from ansible.module_utils.facts.collector import BaseFactCollector
        else:
            sys.path.insert(0, '../../../plugins/module_utils/facts')
            from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.system.capability import SystemCapabilities

# Generated at 2022-06-13 02:20:15.538487
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # TODO:
    # Mock current system to have a non-empty output of capsh --print
    # Check output vs expected value
    # Check AssertionError on empty result
    assert False, "Not implemented"

# Generated at 2022-06-13 02:20:23.210337
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Since run_command() is mocked, we expect to get an empty dictionary
    # returned by SystemCapabilitiesFactCollector.collect()
    mod_mock = AnsibleMock()
    facts_dict = SystemCapabilitiesFactCollector().collect(module=mod_mock)
    assert isinstance(facts_dict, dict)
    assert facts_dict == {}

    # We now expect the Dict Facts containing the capabilties in the
    # default CentOS/RedHat 7 system.
    mod_mock = AnsibleMock()
    mod_mock.get_bin_path = MagicMock(return_value="/usr/libexec/platform-python")

# Generated at 2022-06-13 02:20:28.580727
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import sys
    import unittest

    def get_bin_path(name):
        return name

    class AnsibleModule:
        def get_bin_path(self, name):
            return name


# Generated at 2022-06-13 02:20:37.901770
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.system.caps import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts.system.caps import BaseFactCollector as BaseCollector
    from ansible.module_utils.facts.utils import get_file_content
    from ansible.module_utils.basic import AnsibleModule
    from ansible.utils.path import which

    saved_rc, saved_stdout, saved_stderr = 0, '', ''
    expected_facts = {
     'system_capabilities': ['cap_chown', 'cap_dac_override', 'cap_fowner', 'cap_kill', 'cap_setgid', 'cap_setuid'],
     'system_capabilities_enforced': 'True'
    }

# Generated at 2022-06-13 02:20:48.572881
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    mock_module = type('', (), dict())
    mock_module.get_bin_path = lambda name, required=True: 'capsh'
    mock_module.run_command = lambda command, errors='surrogate_then_replace', **kwargs: (0, 'Current: =ep\nBounding set =cap_chown,cap_dac_override,cap_dac_read_search\n', '')
    facts = SystemCapabilitiesFactCollector().collect(mock_module)
    assert facts['system_capabilities'] == []
    assert facts['system_capabilities_enforced'] == 'False'


# Generated at 2022-06-13 02:20:59.046684
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """Test SystemCapabilitiesFactCollector::collect()"""
    import ansible.module_utils.facts.system.caps
    import ansible.module_utils.facts.system
    import ansible.module_utils.facts

    import os
    import sys
    import stat
    import tempfile
    import shutil
    import textwrap
    import platform

    # Create a fake capsh binary
    def make_fake_capsh(tmp_dir):
        capsh_path = os.path.join(tmp_dir, 'capsh')

# Generated at 2022-06-13 02:21:09.604413
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """systemcapabilities should return the output of `capsh --print` properly parsed"""

    class MockModule(object):
        @staticmethod
        def get_bin_path(*_, **__):
            # NOTE: assuming capsh is in PATH for testing
            return 'capsh'
        @staticmethod
        def run_command(*_, **__):
            return 0, STDOUT_CAPSH, STDERR_CAPSH
    class MockFacts(dict):
        pass

    MockTarget = type('MockTarget', (object,), {})

    target = MockTarget()
    module = MockModule()
    facts = MockFacts()

    collector = SystemCapabilitiesFactCollector(target, module, facts)

    result = collector.collect()
    assert result == RESULT_CAPSH



# Generated at 2022-06-13 02:21:19.662700
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    test_module_mock = Mock()
    test_module_mock.run_command.return_value = [0, 'Current: =ep', None]
    test_module_mock.get_bin_path.return_value = '/bin/capsh'

    capsFactCollector_object = SystemCapabilitiesFactCollector()

    # Test with no capabilities enforced
    result = capsFactCollector_object.collect(test_module_mock, None)
    assert result == {'system_capabilities_enforced': 'False',
                      'system_capabilities': []}

    # Test with capabilities enforced
    test_module_mock.run_command.return_value = [0, 'Current: =ep cap_net_bind_service,cap_chown', None]

# Generated at 2022-06-13 02:21:20.871279
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:21:26.219808
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import ansible.module_utils.facts.collector
    mod = ansible.module_utils.facts.collector.BaseFactCollector()
    import os
    mod.get_bin_path = lambda executable: '/bin/' + executable if executable in os.listdir('/bin/') else None
    import json
    capsh_path = mod.get_bin_path('capsh')
    if capsh_path:
        mod.run_command = lambda a, b: (0, 'Current: =ep', '')
        out = SystemCapabilitiesFactCollector(mod).collect()
        assert out == {'system_capabilities_enforced': 'False', 'system_capabilities': []}

# Generated at 2022-06-13 02:21:31.105402
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    '''
    Unit test for method collect of class SystemCapabilitiesFactCollector
    '''
    # NOTE: no unit tests here, see 'System capabilities' tests in other
    #       modules via module_utils/facts.py:test_module_utils_facts()
    pass

# Generated at 2022-06-13 02:21:38.664041
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Initialize a SystemCapabilitiesFactCollector object
    c = SystemCapabilitiesFactCollector()

    # mock module:
    module = MagicMock()

    # Set the return values of the mocked methods of module
    module.get_bin_path.return_value = '/bin/capsh'
    module.run_command.return_value = (0, 'Current: =ep', '')

    # Invoke the collect method of SystemCapabilitiesFactCollector
    res = c.collect(module)

    assert len(res) == 2
    assert res['system_capabilities_enforced'] == 'False'
    assert res['system_capabilities'] == []


# Generated at 2022-06-13 02:21:48.409092
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: mock import with importlib
    import ansible.module_utils.facts.collector
    ansible.module_utils.facts.collector.BaseFactCollector = BaseFactCollector

    # NOTE: patch modules you use.
    # TODO: mock module -akl
    import ansible.module_utils.facts.collector.system.SystemCapabilitiesFactCollector
    m1 = mock.mock_open(read_data='caps')
    with mock.patch('ansible.module_utils.facts.collector.system.SystemCapabilitiesFactCollector.open', m1, create=True):
        a = ansible.module_utils.facts.collector.system.SystemCapabilitiesFactCollector()
        # NOTE: setup needed fixtures
        a.__init__()
        # NOTE: execute code to be tested

# Generated at 2022-06-13 02:21:56.390944
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # setup mock return values
    module = Mock()
    # check_caps = 'True'
    module.get_bin_path = Mock(return_value='/usr/bin/capsh')
    rc = 0
    out = 'Current: =ep'
    err = ''
    module.run_command = Mock(return_value=(rc, out, err))

    # setup the test subject
    fact_collector = SystemCapabilitiesFactCollector()

    # call the method
    fact_collector.collect(module=module, collected_facts={})

    # assert the results
    assert module.get_bin_path.called
    assert module.run_command.called
    assert fact_collector._fact_ids == set(['system_capabilities', 'system_capabilities_enforced'])



# Generated at 2022-06-13 02:22:03.359228
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """Unit test for method collect of class SystemCapabilitiesFactCollector."""
    import os
    import mock

    # This is the class we are going to use in this test
    cs = SystemCapabilitiesFactCollector()

    # Things we expect to get out at the end
    cs_facts = {
        'system_capabilities': [],
        'system_capabilities_enforced': 'NA'
    }

    # Things we expect to be called with
    run_command_data = {
        'rc': 0,
        'stdout': 'foo\nbar\nbaz',
        'stderr': 'foo\nbar\nbaz'
    }

    run_command_return_value = (run_command_data['rc'], run_command_data['stdout'], run_command_data['stderr'])



# Generated at 2022-06-13 02:22:13.274933
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import os
    import tempfile
    from ansible.module_utils.facts.collector import BaseFactCollector


# Generated at 2022-06-13 02:22:23.287813
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Arrange
    import sys
    if sys.version_info[0] >= 3:
        from unittest.mock import Mock
    else:
        from mock import Mock
    module_mock = Mock()
    collected_facts_mock = Mock()
    capsh_path = '/path/to/capsh'

# Generated at 2022-06-13 02:22:30.554931
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    collector = SystemCapabilitiesFactCollector()
    assert collector.collect() == {'system_capabilities': [],
                                   'system_capabilities_enforced': 'NA'}

# Generated at 2022-06-13 02:22:38.694766
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.collector.system_capabilities import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts.collector.system_capabilities import get_caps_data
    from ansible.module_utils.facts.collector.system_capabilities import parse_caps_data

# Generated at 2022-06-13 02:22:40.762994
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Note: SystemCapabilitiesFactCollector calls module.run_command which we cannot mock
    #       so we simply skip the test.
    pass

# Generated at 2022-06-13 02:22:51.207122
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    m = Mock_module()
    c = SystemCapabilitiesFactCollector(module=m)

    (i1, o1, e1) = m.run_command.call_args_list.pop(0)[0]
    assert i1 == ['/bin/capsh', '--print']

# Generated at 2022-06-13 02:22:59.015403
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: class import done in module scope for easy mocking -akl
    from ansible.module_utils.facts import collector


# Generated at 2022-06-13 02:23:08.508830
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import collector
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.system.caps import SystemCapabilitiesFactCollector

    class MockModule(object):
        def __init__(self, capsh_path, *args):
            self.caps_path = capsh_path
            self.args = args

        def run_command(self, path, errors):
            if not self.caps_path:
                return (1, '', 'capsh not found')

            if self.args == (1, False):
                return (1, '', 'capsh failed')

            if self.args == (1, True):
                return (0, '', 'capsh failed')

# Generated at 2022-06-13 02:23:18.706258
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = FakeModule(bin_path={'capsh': '/usr/bin/capsh'},
                        run_command=run_command)
    capsh_collector = SystemCapabilitiesFactCollector()
    facts_dict = capsh_collector.collect(module=module)
    assert set(facts_dict) == set(['system_capabilities',
                                 'system_capabilities_enforced'])
    assert facts_dict['system_capabilities'] == ['cap_sys_chroot',
                                                 'cap_sys_nice',
                                                 'cap_setuid',
                                                 'cap_setgid']
    assert facts_dict['system_capabilities_enforced'] == 'True'


# Generated at 2022-06-13 02:23:28.917752
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.utils import get_file_content
    mock_module_with_results = get_file_content('/tmp/capsh_out')
    mock_module = Mock()
    mock_module.run_command.return_value = (0, mock_module_with_results, '')
    facts_dict = SystemCapabilitiesFactCollector().collect(mock_module)
    assert len(facts_dict['system_capabilities_enforced']) == 4
    assert len(facts_dict['system_capabilities']) == 3
    assert facts_dict['system_capabilities'][0] == 'chown'
    assert facts_dict['system_capabilities'][1] == 'dac_override'
    assert facts_dict['system_capabilities'][2] == 'kill'

# Generated at 2022-06-13 02:23:38.038735
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    class TestModule(object):
        def __init__(self):
            self.params = dict()
            self.fail = False
            self.run_command_result = (0, '', '')

# Generated at 2022-06-13 02:23:43.273837
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import fact_collector
    from ansible.module_utils._text import to_text

    module = MockModule()
    module.run_command.return_value = (0, 'Current: =ep', '')
    collected_facts = {}
    SystemCapabilitiesFactCollector._test = True
    SystemCapabilitiesFactCollector.collect(module=module, collected_facts=collected_facts)
    expected_collected_facts = {'system_capabilities': [], 'system_capabilities_enforced': 'False'}
    assert collected_facts == expected_collected_facts

    module.run_command.return_value = (0, 'Current: =ep cap_net_raw,cap_net_admin,cap_net_bind_service', '')
    collected_facts = {}
    System

# Generated at 2022-06-13 02:23:55.249918
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # The method does not return anything
    assert SystemCapabilitiesFactCollector().collect() is None

# Generated at 2022-06-13 02:23:58.098692
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = None
    collected_facts = None
    test_SystemCapabilitiesFactCollector = SystemCapabilitiesFactCollector()
    results = test_SystemCapabilitiesFactCollector.collect(module, collected_facts)
    assert results

# Generated at 2022-06-13 02:24:07.612485
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    from ansible_collections.ansible.community.tests.unit.compat.mock import Mock, patch

    module = Mock()
    capsh_path = '/usr/bin/capsh'
    module.get_bin_path.return_value = capsh_path

# Generated at 2022-06-13 02:24:14.373659
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """
    This method is used to test if the fact collector, SystemCapabilitiesFactCollector,
    returns facts in the expected format.
    """
    def mock_get_bin_path(path, opt_dirs=[]):
        mock_bin_path = '/bin/'
        return mock_bin_path + path

    def mock_run_command(command, **kwargs):
        rc = 0
        out = 'Current: =ep\n'
        err = ''
        return rc, out, err


    test_module = type('module', (object,), dict(get_bin_path=mock_get_bin_path,
                                                 run_command=mock_run_command))()
    # NOTE: validate return data not simply 'is not None' -akl

# Generated at 2022-06-13 02:24:14.959975
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:24:23.294895
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    class Module(object):
        def get_bin_path(self, name):
            return 'capsh_path'

        def run_command(self, args, **kwargs):
            return 0, 'Current: =ep', ''

    class AnsibleModule(object):
        def __init__(self):
            self.params = {'data': {'system_capabilities': [], 'system_capabilities_enforced': False}}

        def fail_json(self, *args, **kw):
            raise AssertionError(args)

    m = Module()
    c = SystemCapabilitiesFactCollector()
    f = c.collect(m)

# Generated at 2022-06-13 02:24:27.421403
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """
    Unit test for method collect of class SystemCapabilitiesFactCollector
    """
    collector = SystemCapabilitiesFactCollector()
    assert collector.collect() == {'system_capabilities': [], 'system_capabilities_enforced': 'NA'}


# Generated at 2022-06-13 02:24:28.729770
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    assert False, "This is not implemented yet"


# Generated at 2022-06-13 02:24:36.081394
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import ModuleUtils

    capsh_path = "test/exec/path/for/capsh"
    capsh_command = [capsh_path, "--print"]
    capsh_module_mock_out = "\n\nCurrent: =ep\nCapInh:  =\nCapPrm:  =\nCapEff:  =\nCapBnd:  =\nCapAmb:  =\n"

    assert SystemCapabilitiesFactCollector._fact_ids == set(['system_capabilities',
                                                             'system_capabilities_enforced'])
    assert SystemCapabilitiesFactCollector.name == 'caps'

    def run_command(self, args, errors='surrogate_then_replace'):
        assert args == capsh_command
        assert errors

# Generated at 2022-06-13 02:24:37.496519
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    SystemCapabilitiesFactCollector = SystemCapabilitiesFactCollector()
    assert not SystemCapabilitiesFactCollector.collect()

# Generated at 2022-06-13 02:25:11.770207
# Unit test for method collect of class SystemCapabilitiesFactCollector

# Generated at 2022-06-13 02:25:12.659818
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    assert True

# Generated at 2022-06-13 02:25:23.263097
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    COLLECTOR = SystemCapabilitiesFactCollector()

    class MockModule(object):
        def run_command(self, cmd, errors):
            if cmd == ['/usr/bin/capsh', '--print']:
                return (0, 'Current: =ep', '')
            elif cmd == ['/usr/bin/capsh', '--print']:
                return (0, '', 'capsh: --print: No such file or directory\n')
            elif cmd == ['/usr/bin/capsh', '--print']:
                return (0, 'Current: =cap_setuid+ep', '')
            elif cmd == ['nocapsh', '--print']:
                return (1, '', 'capsh: --print: No such file or directory\n')

# Generated at 2022-06-13 02:25:31.373010
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.collector.capabilities import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts.collector.base import BaseFactCollector
    from ansible.module_utils.facts.collector.system import SystemCollector
    from ansible.module_utils.facts.utils import get_file_lines
    #from ansible.module_utils.facts.collector.capabilities import get_caps_data
    #from ansible.module_utils.facts.collector.capabilities import parse_caps_data

    def get_caps_data(module=None):
        return get_file_lines('capsh_file_data.txt')

    def parse_caps_data(data=None):
        return {}

    collector.fact_classes

# Generated at 2022-06-13 02:25:40.854912
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    import ansible.module_utils.facts.system.capabilities as cap

    def mock_run_command(self, args, errors='surrogate_then_replace'):
        return 0, 'Current: =ep', None

    from ansible.module_utils.facts.system.capabilities import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts.utils import AnsibleFactsCollector
    import ansible.module_utils.facts.system.capabilities as cap

    # Mock a module
    class MockModule:

        def get_bin_path(self, name):
            return '/bin/capsh'

        def run_command(self, args, errors='surrogate_then_replace'):
            if args[0] == '/bin/capsh':
                return 0, 'Current: =ep', None
            return

# Generated at 2022-06-13 02:25:48.487562
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Mock the inputs (module, facts)
    module = {
        "run_command": [
            0,
            "Current: =ep\r\n",
            ""
        ],
        "get_bin_path": "capsh"
    }

    # Init the SystemCapabilitiesFactCollector
    s = SystemCapabilitiesFactCollector(module=module)

    # Declare output variable
    out = {}

    # Call the collect method
    out = s.collect(module=module)

    # Assert if the outputs are correct
    assert out == {"system_capabilities": [], "system_capabilities_enforced": "False"}

# Generated at 2022-06-13 02:25:55.104089
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: why not mock these things up? -akl
    capsh_path="/bin/capsh"
    # NOTE: return_value is never assigned -akl
    capsh_mock = MagicMock()
    capsh_mock.get_bin_path.return_value = capsh_path
    capsh_result_mock = MagicMock()
    capsh_result_mock.returncode = 0

# Generated at 2022-06-13 02:26:03.238418
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # create object of class
    fact_collector = SystemCapabilitiesFactCollector()

    # create sample module object
    module = AnsibleModule(argument_spec={})
    module.run_command = lambda args, **kwargs: (0, '0x00000080,cap_kill=ep', '')

    # get system capabilities
    facts_dict = fact_collector.collect(module)

    # compare assert statments
    assert facts_dict['system_capabilities_enforced'] == 'False'
    assert facts_dict['system_capabilities'] == ['cap_kill']

# Generated at 2022-06-13 02:26:07.268426
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    m = MockModule()
    module = m.get_module()
    collector = SystemCapabilitiesFactCollector()
    result = collector.collect(module=module, collected_facts=None)
    assert result['system_capabilities'] == ['cap_sys_ptrace', 'cap_sys_admin']
    assert result['system_capabilities_enforced'] == 'True'

# Generated at 2022-06-13 02:26:12.298160
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import mock

    # Create object to test method
    from ansible.module_utils.facts import collector
    facts_dict = {}
    test_obj = collector.get_collector('SystemCapabilitiesFactCollector')

    # Setup mocked objects
    capsh_path = 'capsh'
    rc = 0

# Generated at 2022-06-13 02:27:17.409571
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """
    unit test method collect of class SystemCapabilitiesFactCollector
    """
    import os
    import tempfile
    from shutil import copy
    from ansible.module_utils.facts import collector

    cwd = os.path.dirname(os.path.abspath(__file__))
    capsh_path = os.path.join(cwd, 'fake_capsh')
    test_tmp_dir = tempfile.mkdtemp()
    copy(capsh_path, test_tmp_dir)
    new_capsh_path = os.path.join(test_tmp_dir, 'fake_capsh')
    os.chmod(new_capsh_path, 0o755)


# Generated at 2022-06-13 02:27:20.821976
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    collector = SystemCapabilitiesFactCollector()
    result = collector.collect()
    assert 'system_capabilities' in result
    assert 'system_capabilities_enforced' in result



# Generated at 2022-06-13 02:27:27.231591
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import sys
    import os

    module = os.path.realpath(os.path.join(sys.path[0], '..', '..', '..'))
    module = module + os.sep + 'lib' + os.sep + 'ansible' + os.sep + 'modules' + os.sep + 'system' + os.sep + 'capabilities.py'
    module = os.path.dirname(module)
    module = os.path.dirname(module)
    module = os.path.dirname(module)
    module = os.path.dirname(module)

    test_module = __import__('ansible.module_utils.facts.collector.system', globals(), locals(), [], -1)

# Generated at 2022-06-13 02:27:37.433122
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    import ansible.module_utils.facts.collector

    class MockModule(object):
        def __init__(self):
            self.run_command_results = []

        def run_command(self, args, errors='strict'):
            return self.run_command_results.pop(0)

        @staticmethod
        def get_bin_path(tool):
            return '/bin/' + tool

    # Mock module.run_command().
    module = MockModule()
    module.run_command_results.append((0, 'Current: =ep', ''))

    # Collect system capabilities facts.
    collector = SystemCapabilitiesFactCollector()
    facts = collector.collect(module)

    assert len(facts) == 2
    assert facts['system_capabilities_enforced'] == 'False'

# Generated at 2022-06-13 02:27:46.861437
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    SystemCapabilitiesFactCollector = SystemCapabilitiesFactCollector()
    # TODO: mock module.run_command
    # capsh_path = module.get_bin_path('capsh')
    # TODO: mock out
    # rc, out, err = module.run_command([capsh_path, "--print"], errors='surrogate_then_replace')
    # TODO: mock enforcement
    # if line.split(':')[1].strip() == '=ep':
    #     enforced = 'False'
    # else:
    #     enforced = 'True'
    #     enforced_caps = [i.strip() for i in line.split('=')[1].split(',')]
    # facts_dict['system_capabilities_enforced'] = enforced
    # facts_dict['system_capabilities'] =

# Generated at 2022-06-13 02:27:53.481768
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    '''
    test for method collect of class SystemCapabilitiesFactCollector
    '''
    fact = SystemCapabilitiesFactCollector()
    collected_facts = {}
    module = FakeModule()

    result = fact.collect(module, collected_facts)
    assert result.get('system_capabilities_enforced')  == 'True'

# Generated at 2022-06-13 02:28:02.269746
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: this method is passed directly to the module, so it must return a dict, not use a param module
    # NOTE: instead, mock the module object and pass it to the method here
    # NOTE: use a mock class for module, then patch/mock as needed
    from ansible.module_utils.facts import gather_subset_from_gather_by_facts_module
    from ansible.module_utils.facts.collectors.system.caps import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts.collectors.base import BaseFactCollector
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.six import iteritems
    import mock
    import os

    module = BaseFactCollector()



# Generated at 2022-06-13 02:28:10.843422
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    test_collector = SystemCapabilitiesFactCollector()
    from ansible.module_utils._text import to_bytes
    test_module = FakeModule()


# Generated at 2022-06-13 02:28:21.553053
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    mock_module = Mock()

# Generated at 2022-06-13 02:28:30.899865
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    print("TEST: test_SystemCapabilitiesFactCollector_collect")
    import ansible.module_utils.facts.collector
    system_cap_collector_obj = ansible.module_utils.facts.collector.SystemCapabilitiesFactCollector()
    # run collect with fake module

    print("TEST: test_SystemCapabilitiesFactCollector_collect - run collect with fake module")
    from ansible.module_utils.basic import AnsibleModule
    module_obj = AnsibleModule(argument_spec={})
    module_obj.get_bin_path = lambda x: "/bin/capsh"
    module_obj.run_command = lambda *a, **kw: (0, "Current: = cap_chown,cap_fowner+eip", "")
    collected_facts = {}
    system_cap_collector_