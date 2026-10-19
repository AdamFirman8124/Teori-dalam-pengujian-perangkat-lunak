

# Generated at 2022-06-13 02:19:55.564543
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.system import SystemCapabilitiesFactCollector


# Generated at 2022-06-13 02:20:06.350242
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    class mock_module:
        def __init__(self, name):
            self.name = name
        def get_bin_path(self):
            if self.name == 'capsh':
                return '/usr/bin/capsh'
            return None

    mock_module_instance = mock_module('capsh')
    mock_module_instance.run_command = lambda x: [0, 'Current: = cap_chown,cap_dac_override,cap_fowner=ep', '']

    fact_collector = SystemCapabilitiesFactCollector()
    output = fact_collector.collect(mock_module_instance)

    assert output['system_capabilities_enforced'] == 'False'

# Generated at 2022-06-13 02:20:14.200541
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import collector
    #mocking capabilities
    class mock_module:
        def get_bin_path(self, cmd):
            return '/usr/bin/capsh'

# Generated at 2022-06-13 02:20:19.227933
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import sys
    import io
    import re
    import os
    import tempfile
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collectors.system.caps import SystemCapabilitiesFactCollector

    def mock(capsh_path, fail_on_missing=False):
        if fail_on_missing:
            raise IOError('No such file or directory')

# Generated at 2022-06-13 02:20:25.937881
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    class MockModule:
        @staticmethod
        def get_bin_path(path):
            return 'capsh'

        @staticmethod
        def run_command(*args):
            arg_str = ' '.join(args[0])
            assert args[0][0] == 'capsh'
            assert '--print' in arg_str
            assert '' not in arg_str
            assert '\r' not in arg_str
            assert '\n' not in arg_str
            return (0, 'Current: =eip', '')

    def ansible_module_run_command(a1, *a2):
        assert False, 'ansible_module_run_command should not be called'

    facts = SystemCapabilitiesFactCollector(MockModule())
    facts.get_bin_path = MockModule.get_bin_

# Generated at 2022-06-13 02:20:36.779696
# Unit test for method collect of class SystemCapabilitiesFactCollector

# Generated at 2022-06-13 02:20:48.031290
# Unit test for method collect of class SystemCapabilitiesFactCollector

# Generated at 2022-06-13 02:20:57.867152
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Verify provided path exists before constructing 
    import os.path
    import pytest
    if not os.path.exists(CAPSH_PATH):
        pytest.skip("System capabilities not found at {0}".format(CAPSH_PATH))

    # Construct instance of SystemCapabilitiesFactCollector and use to create
    # facts dictionary
    collector = SystemCapabilitiesFactCollector()
    collected_facts = {}
    facts = collector.collect(module=None, collected_facts=collected_facts)

    # Verify 'facts' dictionary has expected contents
    expected_facts = {'system_capabilities': ['cap_setpcap', 'cap_sys_admin'],
                      'system_capabilities_enforced': True}
    assert facts == expected_facts

# Generated at 2022-06-13 02:21:02.740848
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector.system import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts.collector import BaseFactCollector

# Generated at 2022-06-13 02:21:10.997538
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import os
    import sys
    import tempfile
    import unittest

    class SystemCapabilitiesTest(unittest.TestCase):
        def __init__(self, *args, **kwargs):
            super(SystemCapabilitiesTest, self).__init__(*args, **kwargs)
            self.connection = {}
            self.ansible_module = AnsibleFakeModule()

        def test_SystemCapabilitiesFactCollector_collect_success(self):
            """
            Test that SystemCapabilitiesFactCollector_collect returns the expected capability data
            """
            results = SystemCapabilitiesFactCollector.collect(self.ansible_module)
            # TODO: Use assertEqual (after using dict sort) once dict is no longer nested
            # self.assertEqual(results['system_capabilities'], expected['system_capabilities'])

# Generated at 2022-06-13 02:21:21.404768
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = MockAnsibleModule()
    module.run_command.return_value = (0, 'Current: =ep', None)
    facts = SystemCapabilitiesFactCollector().collect(module)
    assert facts['system_capabilities_enforced'] == 'False'
    assert facts['system_capabilities'] == []
    module.run_command.assert_called_once_with(['/bin/capsh', '--print'],
                                               errors='surrogate_then_replace')
    module = MockAnsibleModule()
    module.run_command.return_value = (0, 'Current: = cap_net_raw,cap_net_admin', None)
    facts = SystemCapabilitiesFactCollector().collect(module)
    assert facts['system_capabilities_enforced'] == 'True'

# Generated at 2022-06-13 02:21:26.495479
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    fake_module = object()
    fake_module.get_bin_path = lambda x: '/fake/path'
    fake_module.run_command = lambda x: ('0', 'fake out', 'fake err')
    fake_module.fail_json = lambda x: 'fake fail_json'

    SystemCapabilitiesFactCollector.collect(fake_module)

# Generated at 2022-06-13 02:21:28.688962
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
   pass


# Generated at 2022-06-13 02:21:30.534444
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # We cannot test this as it is not possible to change the
    # capabilities of a process in a meaningful way.
    pass

# Generated at 2022-06-13 02:21:38.752946
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = None
    collected_facts = None
    # test case for 
    # SystemCapabilitiesFactCollector.collect()    
    module = {}
    collected_facts = {}
    # module.run_command.return_value = None, some_string, None
    # monkey patching
    # SystemCapabilitiesFactCollector._get_caps_data()
    SystemCapabilitiesFactCollector._get_caps_data = lambda self, module: some_string
    # initializing SystemCapabilitiesFactCollector.collect()
    # assert to compare
    # assert some_string == expected_return_value
    assert SystemCapabilitiesFactCollector().collect(module, collected_facts) =={'system_capabilities_enforced': 'NA', 'system_capabilities': []}

# Generated at 2022-06-13 02:21:48.485541
# Unit test for method collect of class SystemCapabilitiesFactCollector

# Generated at 2022-06-13 02:21:49.226798
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # TODO: build unit test -akl
    pass

# Generated at 2022-06-13 02:21:57.308413
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import os
    import sys
    import mock
    import unittest

    PY3 = sys.version_info[0] == 3
    if not PY3:
        import __builtin__ as builtins
        BUILTINS_NAME = '__builtin__'
    else:
        import builtins
        BUILTINS_NAME = 'builtins'

    class MockModule(object):
        def __init__(self):
            self.params = {}

        def get_bin_path(self, name, *args, **kwargs):
            if name == "capsh":
                return "/usr/bin/capsh"
            else:
                return None

        def exit_json(self, fact, **kwargs):
            pass

        def fail_json(self, fact, **kwargs):
            pass


# Generated at 2022-06-13 02:22:02.234855
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    with patch('ansible.module_utils.facts.system.system_capabilities.BaseFactCollector.collect'):
        mc = MagicMock(name='mock_module_util')
        mc.get_bin_path = MagicMock(name='get_bin_path')
        mc.run_command = MagicMock(name='run_command')
        mc.run_command.return_value = (0, 'Current: =ep', '')
        SystemCapabilitiesFactCollector.collect(mc)
        assert mc.run_command.call_count == 1
        mc.run_command.assert_called_with([mc.get_bin_path.return_value, '--print'], errors='surrogate_then_replace')

# Generated at 2022-06-13 02:22:03.966120
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = None
    collected_facts = None
    output = SystemCapabilitiesFactCollector().collect(module, collected_facts)
    assert output['system_capabilities_enforced'] != 'NA'

# Generated at 2022-06-13 02:22:10.812000
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: test_SystemCapabilitiesFactCollector_collect() is a stub
    pass

# Generated at 2022-06-13 02:22:11.978196
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    ''' Unit test for method collect of class SystemCapabilitiesFactCollector '''
    pass

# Generated at 2022-06-13 02:22:21.006919
# Unit test for method collect of class SystemCapabilitiesFactCollector

# Generated at 2022-06-13 02:22:27.789120
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    def _run_command(self, args, check_rc=False):
        return ([0, 'Current: =ep\n', ''])
        pass

    SystemCapabilitiesFactCollector._run_command = _run_command
    SystemCapabilitiesFactCollector._load_platform_subclass = lambda a, b: None
    SystemCapabilitiesFactCollector._get_platform_fact = lambda x: ''
    c = SystemCapabilitiesFactCollector()
    res = c.collect()
    assert res['system_capabilities'] == []
    assert res['system_capabilities_enforced'] == 'False'

# Generated at 2022-06-13 02:22:35.756715
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import mock
    import os
    import sys

    class module_mock(object):
        def get_bin_path(self, arg):
            return capsh_path

        def run_command(self, arg, errors=None):
            if arg[0] == capsh_path:
                if arg[1] == "--print":
                    return (0, "Current:\n= ep cap_setpcap,cap_sys_admin+eip\nBounding set =cap_chown,cap_dac_override,cap_fowner,cap_fsetid,cap_kill,cap_setgid,cap_setuid,cap_sys_chroot,cap_mknod,cap_audit_write,cap_setfcap+eip", "")

# Generated at 2022-06-13 02:22:45.743749
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    capsh_path = '/path/to/capsh'
    capsh_rc = 0

# Generated at 2022-06-13 02:22:55.153836
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector.system import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts import AnsibleFactCollector

    fact_collector = SystemCapabilitiesFactCollector()
    collected_facts = AnsibleFactCollector()

    #mock module
    class FakeModule(object):
        def run_command(self, *args, **kwargs):
            return args[0], 'Current: =ep', ''
        def get_bin_path(self, *args, **kwargs):
            return 'capsh'
    module = FakeModule()

    #collect facts
    fact_collector.collect(module=module, collected_facts=collected_facts)

    #assert
    assert "system_capabilities_enforced" in collected_facts

# Generated at 2022-06-13 02:23:02.207780
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module_mock = Mock()
    module_mock.run_command.return_value = (0, 'Current: =ep', 'error')
    collector = SystemCapabilitiesFactCollector(module_mock)
    ret_dict = collector.collect()
    assert ret_dict['system_capabilities_enforced'] == 'False'
    assert ret_dict['system_capabilities'] == []
    assert ret_dict['system_capabilities_enforced'] == 'False'

# Generated at 2022-06-13 02:23:11.134227
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import ansible_capabilities
    from ansible.module_utils.facts.utils_module import AnsibleModule

    module = AnsibleModule()
    capsh_path = module.get_bin_path('capsh')

    res = {'system_capabilities': [], 'system_capabilities_enforced': 'NA'}
    if capsh_path:
        rc, out, err = module.run_command([capsh_path, "--print"], errors='surrogate_then_replace')
        enforced = 'NA'
        enforced_caps = []
        for line in out.splitlines():
            if len(line) < 1:
                continue
            if line.startswith('Current:'):
                if line.split(':')[1].strip() == '=ep':
                    enforced

# Generated at 2022-06-13 02:23:22.052796
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import ansible.module_utils.facts.collectors.system.system_capabilities as system_capabilities
    class FakeModule:
        def __init__(self):
            self.run_command_results = [[0,'Current: =ep','NA'],
                                        [0,'Current: = cap_sys_admin,cap_dac_override+ep','NA']]
            self.run_command_index = 0

        def get_bin_path(self, program):
            return '/usr/bin/' + program

        def run_command(self,args,**kwargs):
            result = self.run_command_results[self.run_command_index]
            self.run_command_index += 1
            return result

    module = FakeModule()
    fact_collector = system_capabilities.SystemCapabilitiesFactCollector

# Generated at 2022-06-13 02:23:34.663050
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    assert SystemCapabilitiesFactCollector().collect()

# Generated at 2022-06-13 02:23:40.971191
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = FakeAnsibleModule()

    capsh_output = "Current: =ep\nBounding set =eip\nSecurebits: 00/0x0/1'b0\n secure-noroot: no (unlocked)\n secure-no-suid-fixup: no (unlocked)\n secure-keep-caps: no (unlocked)\nuid=0(root) gid=0(root)"
    module.run_command = MagicMock(return_value=(0, capsh_output, ""))
    collector = SystemCapabilitiesFactCollector()
    expected = {
        'system_capabilities': [],
        'system_capabilities_enforced': 'False',
    }
    assert collector.collect(module=module, collected_facts=None) == expected


# Generated at 2022-06-13 02:23:46.411948
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """
    Return empty list if `capsh` is not installed
    """
    class TestModule(object):
        def __init__(self):
            self.params = {}

        def get_bin_path(self, cmd, required=False):
            if cmd == 'capsh':
                return None

    m = TestModule()
    fc = SystemCapabilitiesFactCollector()
    assert fc.collect(module=m) == {}



# Generated at 2022-06-13 02:23:52.980526
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import collector
    #init SystemCapabilitiesFactCollector and get an instance of it
    collector.add_collector(SystemCapabilitiesFactCollector)
    #create a mock module object
    module = MagicMock(name='module')
    #create a mock run_command object
    run_command = MagicMock(name='run_command')
    module.run_command = run_command
    #create a mock environ object
    environ = MagicMock(name='environ')
    environ_dict = {'PATH': '/usr/bin'}
    environ.copy.return_value = environ_dict
    module.environ = environ
    #set ok of run_command to True
    run_command.return_value = 0, 'some response', 'some error'
    #

# Generated at 2022-06-13 02:24:01.689171
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    M = TestModule()

    # Ensure capsh is not present
    M.get_bin_path.return_value = None
    c = SystemCapabilitiesFactCollector(M)
    assert c.collect() == {}

    # Ensure capsh is present and returning
    M.get_bin_path.return_value = '/path/to/capsh'
    # NOTE: -> get_caps_data()/parse_caps_data() for easier mocking -akl
    M.run_command.return_value = (0, 'Current: =ep', None)

    expected_caps = {
        'system_capabilities': [],
        'system_capabilities_enforced': 'False'
    }

    assert c.collect() == expected_caps


# Generated at 2022-06-13 02:24:09.175497
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Setup
    fact_collector = SystemCapabilitiesFactCollector()
    module = Mock()
    module.get_bin_path = Mock(return_value='/usr/bin/capsh')
    module.run_command = Mock(return_value=(0, "Current: =ep\nSecurebits: 00/0x0/1'b0\nsecure-noroot: no (unlocked)\nsecure-no-suid-fixup: no (unlocked)\nsecure-keep-caps: no (unlocked)\nuid=1000(test_user) gid=1000(test_user)\neuid=0(root) egid=0(root)", ""))

    # Test
    result = fact_collector.collect(module=module, collected_facts={})

    # Assert
    assert result['system_capabilities_enforced']

# Generated at 2022-06-13 02:24:21.018015
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import os
    import subprocess

# Generated at 2022-06-13 02:24:29.968950
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: mock module & pass in module to (effectively) test 'if not module'
    #       path, as well as 'if not crash_path' path -akl
    from ansible.module_utils.facts.collector.system import SystemCapabilitiesFactCollector
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    tested_instance = SystemCapabilitiesFactCollector()
    assert tested_instance.collect() == {}
    # Mock module
    class MockModule:
        def get_bin_path(self, _):
            return "test_bin_feed"

# Generated at 2022-06-13 02:24:30.478853
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
  pass

# Generated at 2022-06-13 02:24:37.542259
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.system.caps import SystemCapabilitiesFactCollector

    test_module = DummyModule(
        params={}
    )
    # Test calling method collect
    tmp_collector = get_collector_instance(test_module)
    tmp_collector.collect()
    assert [SystemCapabilitiesFactCollector.name,
            ] == tmp_collector.collected_facts.keys()
    #
    # Test calling method collect
    test_module.params['capsh'] = '/bin/true'
    tmp_collector = get_collector_instance(test_module)
    tmp_collector.collect()

# Generated at 2022-06-13 02:25:10.572319
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    mod = AnsibleModule({}, {})
    mod.run_command = MagicMock(return_value=(0, 'Current: =ep', ''))

    fc = SystemCapabilitiesFactCollector(module=mod)
    facts = fc.collect(module=mod)
    assert facts['system_capabilities_enforced'] == 'False'
    assert facts['system_capabilities'] == []


# Generated at 2022-06-13 02:25:21.439931
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import get_collector_instance


# Generated at 2022-06-13 02:25:26.462572
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    collector = SystemCapabilitiesFactCollector()

    # Test with capsh_path defined
    # Test with enforcing sys caps
    class TestModule(object):
        def __init__(self):
            self.params = {
                    'capsh_path': '/bin/capsh'
                    }

        def get_bin_path(self, command):
            return '/bin/capsh'


# Generated at 2022-06-13 02:25:33.490293
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    m =  {
        'get_bin_path': lambda x: '/usr/bin/capsh',
        'run_command': lambda cmd: (0, 'Current: =ep', ''),
    }
    c = SystemCapabilitiesFactCollector()
    facts = c.collect(module=m)
    assert facts.get('system_capabilities_enforced') == 'False'
    assert facts.get('system_capabilities') == []

    m =  {
        'get_bin_path': lambda x: '/usr/bin/capsh',
        'run_command': lambda cmd: (0, 'Current: =ep cap_sys_admin,cap_net_admin,cap_dac_override,cap_setgid,cap_setuid,cap_fowner,cap_mknod', ''),
    }
    c

# Generated at 2022-06-13 02:25:43.996067
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible_collections.community.general.plugins.modules.system.caps import get_bin_path
    from ansible_collections.community.general.plugins.module_utils.common.process import get_bin_path
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.utils import get_file_lines

    module = get_bin_path()
    BaseFactCollector = BaseFactCollector()

    get_file_lines = get_file_lines
    module = get_bin_path()
    BaseFactCollector = BaseFactCollector()

    if capsh_path:
        rc, out, err = module.run_command([capsh_path, "--print"], errors='surrogate_then_replace')
        enforced_caps = []
        enforced

# Generated at 2022-06-13 02:25:51.867776
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.collector import BaseFactCollector



# Generated at 2022-06-13 02:25:58.883804
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import cache
    from ansible.module_utils.facts.collectors.capabilities import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts import ansible_collector

    SystemCapabilitiesFactCollector.collect(cache, ansible_collector)
    assert (cache['system_capabilities'] == ['cap_net_bind_service', 'cap_net_raw'])
    assert (cache['system_capabilities_enforced'] == 'False')

# Generated at 2022-06-13 02:26:07.377378
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """Unit test for method 'collect' of class SystemCapabilitiesFactCollector."""
    import os
    import sys
    import subprocess
    # NOTE: may fail when run under 'coverage' -akl
    if 'COVERAGE_PROCESS_START' in os.environ:
        return None
    fc = SystemCapabilitiesFactCollector()
    # NOTE: mock AnsibleModule/AnsibleModule.run_command/AnsibleModule.get_bin_path/'capsh' -akl
    class MockAnsibleModule:
        def __init__(self):
            self.run_command_rc = 0

# Generated at 2022-06-13 02:26:10.219530
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import Collector
    # NOTE: Testing the 'system_capabilities' and
    # 'system_capabilities_enforced' facts.
    # The result is negative, when method 'get_bin_path' is implemented
    # in Collector.
    c = SystemCapabilitiesFactCollector()
    assert c.collect() == {}

# Generated at 2022-06-13 02:26:14.113659
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: this is not a 'real' test it only checks that the method is callable
    #       and that it does not raise any exception -akl
    assert SystemCapabilitiesFactCollector().collect() == {'system_capabilities_enforced': 'NA',
                                                           'system_capabilities': []}

# Generated at 2022-06-13 02:27:21.302300
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    assert(False)



# Generated at 2022-06-13 02:27:27.624465
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    capsh_path = '/sbin/capsh'


    def run_cmd_side_effect(*args, **kwargs):
        # Mock method for module.run_command()
        if args[0][0] == capsh_path:
            return 0, 'Current: =ep', ''
        else:
            return 0, '', ''

    class dummy_module():
        # Dummy module for testing
        def __init__(self):
            self.run_command = lambda *args, **kwargs: run_cmd_side_effect(*args, **kwargs)

        def get_bin_path(self, bin_path):
            # Dummy method for module.get_bin_path()
            if bin_path == 'capsh':
                return capsh_path
            else:
                return None

    module = dummy_module

# Generated at 2022-06-13 02:27:31.955662
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import mock
    from ansible.module_utils import basic
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.system.caps import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts.collector import BaseFactCollector

    module = basic.AnsibleModule(
        argument_spec=dict()
    )

    module.run_command = mock.MagicMock()
    module.run_command.return_value = (0, "Current: = cap_net_raw,cap_ipc_lock+eip\nVersion: 3.27\n", None)

    # NOTE: skipped fact_ids are not passed to constructor -akl
    # skipped_list = [ 'skipped_fact' ]
    # skipped_list.extend(BaseFactCollector._fact_

# Generated at 2022-06-13 02:27:37.391230
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # just test that it does not raise an exception
    # for detailed tests refer to test_system_capabilities.py
    import ansible.module_utils.facts.collector
    x = ansible.module_utils.facts.collector.get_collector_facts('SystemCapabilitiesFactCollector', {})
    x.collect()

# Generated at 2022-06-13 02:27:41.541499
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: below is a very basic test to at least verify a dict is returned
    mod = MockModule()
    mod.get_bin_path.return_value = '/bin/capsh'
    c = SystemCapabilitiesFactCollector()
    resp = c.collect(module=mod)
    assert resp == {'system_capabilities_enforced': 'NA', 'system_capabilities': []}


# Generated at 2022-06-13 02:27:50.441982
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import ansible.module_utils.facts.collector
    ## Importing of SystemCapabilitiesFactCollector depends on this import.
    import ansible.module_utils.facts.system.system_capabilities_fact

    print("")
    print("##### Testing SystemCapabilitiesFactCollector.")
    print("##### Verify that it's an instance of FactCollector.")
    c = ansible.module_utils.facts.collector.FactCollector()
    assert isinstance(c, ansible.module_utils.facts.collector.FactCollector)

    print("##### Verify that it's an instance of SystemCapabilitiesFactCollector.")
    c = ansible.module_utils.facts.collector.SystemCapabilitiesFactCollector()

# Generated at 2022-06-13 02:28:00.751134
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """ Test a valid case:
    capsh - output sample in ansible/test/unit/module_utils/basic.py
    """
    module = AnsibleModule(
        argument_spec = dict()
    )
    module.get_bin_path = MagicMock(return_value='/bin/capsh')
    module.run_command = MagicMock(return_value=(0, 'Current: =eip', ''))
    system_fact_collector = SystemCapabilitiesFactCollector()
    test_fact_dict = system_fact_collector.collect(module, {})
    assert 'system_capabilities_enforced' in test_fact_dict
    assert 'system_capabilities' in test_fact_dict
    assert len(test_fact_dict['system_capabilities']) == 3
    assert test_fact_dict

# Generated at 2022-06-13 02:28:09.613497
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    class MockModule(object):
        def __init__(self):
            self.run_command = MockRunCommand()
            self.get_bin_path = MockGetBinPath()

    class MockRunCommand(object):
        def __init__(self):
            self.call_count = 0

        def __call__(self, args, check_rc=True, close_fds=True, executable=None, data=None, binary_data=False, path_prefix=None, cwd=None,
                     use_unsafe_shell=False, env_string=None, environ_update=None, umask=None, encoding=None, errors='surrogate_then_replace',
                     log_errors=True):
            self.call_count += 1
            rc = 0
            if self.call_count == 0:
                out

# Generated at 2022-06-13 02:28:19.987112
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """
    Test that SystemCapabilitiesFactCollector.collect() returns correct data
    """
    from ansible_collections.ansible.community.tests.unit.module_utils.facts.utils.special_dims import DummyModule
    from ansible_collections.ansible.community.plugins.module_utils.facts.system import SystemCapabilitiesFactCollector

    module = DummyModule()
    module.run_command_environ_update = {'LANG': 'C', 'LC_ALL': 'C', 'LC_MESSAGES': 'C', 'LC_CTYPE': 'C'}
    module.run_command = lambda *_, **kwargs: (0, 'Current: =ep', '')
    sut = SystemCapabilitiesFactCollector()

# Generated at 2022-06-13 02:28:29.461879
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    class MockModule:
        # Get bin path
        def get_bin_path(self, capsh_path):
            return capsh_path

        # Run commands