

# Generated at 2022-06-13 02:19:55.296807
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils import basic
    from ansible.module_utils.facts import collector
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils._text import to_text

    module_mock = basic.AnsibleModule(argument_spec={}, supports_check_mode=False)
    module_mock.get_bin_path = lambda x: "/usr/bin/capsh"

# Generated at 2022-06-13 02:20:06.014667
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Testing the collection of system capabilities with enforced limits
    module = FakeModule(capsh_path='/bin/capsh')
    caps_fc = SystemCapabilitiesFactCollector(module=module)
    collected_facts = caps_fc.collect()

# Generated at 2022-06-13 02:20:13.181771
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import FactsCollector
    from ansible.module_utils.facts.system.caps import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts.system.caps import get_caps_data
    from ansible.module_utils.facts.system.caps import parse_caps_data
    from ansible.module_utils.facts.system.caps import PATH_CAPSH
   
    #Collector information
    coll = SystemCapabilitiesFactCollector()
    coll.name = 'caps'
    coll.module = None
    coll._fact_ids = set(['system_capabilities', 'system_capabilities_enforced'])
    facts_dict = {}
    facts_dict['system_capabilities_enforced'] = 'True'

# Generated at 2022-06-13 02:20:14.600968
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
        """ SystemCapabilitiesFactCollector: test 'collect' method """

        # NOTE: need to mock the module -akl

# Generated at 2022-06-13 02:20:19.540198
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts import get_module
    import ansible.module_utils.facts.collectors.system.system_capabilities as test_system_capabilities

    # mock module
    module = get_module()

# Generated at 2022-06-13 02:20:20.844883
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.system.caps import SystemCapabilitiesFactCollector

    SystemCapabilitiesFactCollector.collect()

# Generated at 2022-06-13 02:20:24.805161
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect(): 
    module = object()
    collected_facts = object()
    collector = SystemCapabilitiesFactCollector()  
    assert collector.collect(module, collected_facts) == {'system_capabilities': ['ep'], 'system_capabilities_enforced': 'False'}

# Generated at 2022-06-13 02:20:35.939162
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.collector.system import SystemCollector

    # mock module
    class AnsibleModuleFake:
        def __init__(self):
            self.params = {}
            self.facts = {}
            self._name = 'ansible fake module'

        def get_bin_path(self, s):
            return 'capsh'

        def run_command(self, cmd, **kwargs):
            if cmd[0] == 'capsh' and '--print' in cmd:
                return 0, capsh_test_output, ''
            else:
                return 0, '', ''

    # mock ansible_collector

# Generated at 2022-06-13 02:20:40.897088
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = MockModule()
    module.run_command = Mock(return_value=(0,'Current: =ep\n','NA'))
    instance = SystemCapabilitiesFactCollector()
    assert instance.collect(module) == {'system_capabilities_enforced': 'False', 'system_capabilities': []}

# Generated at 2022-06-13 02:20:49.892804
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = "{'get_bin_path': lambda x: '/bin/capsh'}"
    capsh_output = """Capabilities for `/bin/capsh': 
  Current: =ep
  Bounding set =ep
  Securebits: 00/0x0/1'b0
  secure-noroot: no (unlocked)
  secure-no-suid-fixup: no (unlocked)
  secure-keep-caps: no (unlocked)
  uid=0(root) gid=0(root)
  groups=0(root),1(bin),2(daemon),3(sys),4(adm),6(disk),10(wheel)"""


# Generated at 2022-06-13 02:20:54.319898
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: get_caps_data()/parse_caps_data() for easier mocking -akl
    pass

# Generated at 2022-06-13 02:21:05.595674
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """
    Method collect of class SystemCapabilitiesFactCollector
    """
    def get_bin_path(self, executable):
        return "/bin"

# Generated at 2022-06-13 02:21:11.670271
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import mock

    import ansible.module_utils.facts.collector

    mock_module = mock.MagicMock()
    mock_module.run_command.return_value = (0, 'Current: =ep', '')
    mock_module.get_bin_path.return_value = '/bin/capsh'

    ansible.module_utils.facts.collector.SystemCapabilitiesFactCollector._instance = None

    collector = ansible.module_utils.facts.collector.SystemCapabilitiesFactCollector()

    result =  collector.collect(mock_module, {})
    assert {'system_capabilities': [], 'system_capabilities_enforced': 'False'} == result

# Generated at 2022-06-13 02:21:19.332379
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collectors.base import BaseFactCollector
    import ansible.module_utils.facts.collectors.capsh as capsh

    # checking if _collect_capsh_facts() is defined in dictionary
    assert '_collect_capsh_facts' in dir(BaseFactCollector)
    assert 'collect' in dir(SystemCapabilitiesFactCollector)

    # mock ansible module instance
    class MockAnsibleModule(object):

        def get_bin_path(self, arg):
            # if 'arg' == 'capsh':
            #     return "capsh_path"
            return "capsh_path"

        def run_command(self, arg1, arg2):
            # capsh_path, "--print"
            # return stdout, stderr, rc
            return

# Generated at 2022-06-13 02:21:25.361104
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """
    Test to collect facts related to systems capabilities via capsh
    """
    module = AnsibleModuleMock({'path': {'default': "/bin/capsh"}})
    out = 'Current: = cap_net_raw+ep cap_sys_ptrace+ep cap_dac_read_search+ep\
        cap_sys_admin+ep cap_sys_pacct+ep cap_sys_rawio+ep cap_sys_nice+ep\
        cap_sys_tty_config+ep cap_setgid+ep cap_setuid+ep cap_chown+ep\
        cap_sys_chroot+ep cap_sys_resource+ep cap_sys_boot+ep\
        cap_audit_write+ep cap_audit_control+ep cap_setfcap+ep'
    module.run_command

# Generated at 2022-06-13 02:21:36.544250
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import mock
    import sys

    # For unit testing, we have to alter sys.modules to import
    # our own module class directly into ansible.module_utils.facts.system.distribution instead of importing ansible.module_utils.facts.system.distribution.linux and thereby calling sys.modules['ansible.module_utils.facts.system.distribution'].LinuxDistribution, which would circumvent our monkeypatching of the class.
    from ansible.module_utils.facts import system
    sys.modules['ansible.module_utils.facts.system'] = system
    from ansible.module_utils.facts.system import distribution
    sys.modules['ansible.module_utils.facts.system.distribution'] = distribution


# Generated at 2022-06-13 02:21:39.355953
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # test_SystemCapabilitiesFactCollector_collect():
    # Check if the function returns empty Dictionary
    assert SystemCapabilitiesFactCollector().collect() == {}

# Generated at 2022-06-13 02:21:49.013713
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import FactCollector
    import ansible_collections.ansible.community.plugins.module_utils.facts.system.caps
    import ansible.module_utils.basic

    # create test module instance
    mod = ansible_collections.ansible.community.plugins.module_utils.facts.system.caps.__AnsibleModuleMock__()

    # create test collector instance
    caps_col = ansible_collections.ansible.community.plugins.module_utils.facts.system.caps.SystemCapabilitiesFactCollector(module=mod)

    # test method collect
    caps_val = caps_col.collect()

    # verify results
    assert caps_col.name == 'caps'

# Generated at 2022-06-13 02:21:49.477120
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:21:57.586001
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    fact_collector = SystemCapabilitiesFactCollector()

# Generated at 2022-06-13 02:22:13.200165
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    # NOTE: not much to test here, we just ensure we execute the 'capsh'
    # command with the correct params, leave it to 'capsh' to test its own
    # functionality. -akl
    class MockModule(object):
        def __init__(self):
            self.check_mode = False
            self.run_command_returns = [
                    (0, 'Current: =ep\nBounding set =chroot,cap_set_file+ep\nSecurebits: 00/0x0/1\n secure-noroot,\n secure-no-suid-fixup,\n secure-keep-caps\n', ''),
                    (1, '', 'usage')
            ]
            self.run_command_index = 0
            self.run_command_calls = []


# Generated at 2022-06-13 02:22:23.241773
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import collector
    from mock import MagicMock
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.system.caps import SystemCapabilitiesFactCollector

    mock_module = MagicMock(path=['/usr/bin'])
    mock_module.run_command = MagicMock()
    # This is an example of how to use the run_command() mock:
    #mock_module.run_command.side_effect = [
    #    (0, '/usr/bin/capsh --print', ''),
    #    (0, 'Capability Ambient set', ''),
    #    (0, 'Current: =ep', ''),
    #]


# Generated at 2022-06-13 02:22:31.271797
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import CapabilityCollector
    capsh_path = "/bin/capsh"
    module = CapabilityCollector()
    module.run_command = lambda x,y,*args,**kwargs: (0, "Current: =ep\n", "")
    module.get_bin_path = lambda x: capsh_path
    cap_collector = SystemCapabilitiesFactCollector()
    assert cap_collector.collect(module) == {'system_capabilities': [], 'system_capabilities_enforced': 'False'}
    assert cap_collector.collect(None) == {}

# Generated at 2022-06-13 02:22:35.978953
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    # NOTE: this really needs a mock module object -akl
    caps_mod = None
    facts_mod = None

# Generated at 2022-06-13 02:22:46.040223
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    fact_collector = SystemCapabilitiesFactCollector()

# Generated at 2022-06-13 02:22:55.389794
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import sys
    import io
    import os

    # Setup FakeModule object
    if sys.version_info[0] >= 3:
        import unittest.mock as mock
    else:
        import mock

    class FakeModule(object):
        def __init__(self, *args, **kwargs):
            self.params = {}

        def get_bin_path(self, *args, **kwargs):
            return 'capsh'


# Generated at 2022-06-13 02:23:06.060126
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.system.collectors.capabilities import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts.system import DistributionFactory


# Generated at 2022-06-13 02:23:13.723976
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    mock_module = Mock()

# Generated at 2022-06-13 02:23:23.592390
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: having a 'module' param is an unusual pattern,
    #       but we need it for mocking -akl
    fact_collector = SystemCapabilitiesFactCollector()
    capsh_path = '/usr/bin/capsh'
    # NOTE: -> get_caps_data() for easier mocking -akl
    # test with caps enforced

# Generated at 2022-06-13 02:23:34.218779
# Unit test for method collect of class SystemCapabilitiesFactCollector

# Generated at 2022-06-13 02:23:50.589882
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = AnsibleModule(argument_spec={},supports_check_mode=True)
    module.run_command = MagicMock(return_value=[0, "Current: =ep", ""])
    capsh_path = module.get_bin_path('capsh')
    collector = SystemCapabilitiesFactCollector()
    result = collector.collect(module)
    assert result['system_capabilities'] == []
    assert result['system_capabilities_enforced'] == 'False'

# Generated at 2022-06-13 02:23:52.642201
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """
    Test method collect of class SystemCapabilitiesFactCollector
    """
    pass



# Generated at 2022-06-13 02:24:01.397713
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import ansible_collected_facts
    from ansible.module_utils._text import to_text
    from ansible.module_utils.facts.collector.system import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts.system.caps import get_caps_data, parse_caps_data
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six.moves import mock
    from ansible.module_utils.common._collections_compat import Sequence
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils.parsing.convert_bool import BOOLEANS_TRUE
    import builtins


# Generated at 2022-06-13 02:24:09.040826
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collectors import BaseFileFactCollector
    from ansible.module_utils.facts.collectors.capabilities import SystemCapabilitiesFactCollector
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils.facts import gather_subset
    from ansible.module_utils.parsing.convert_bool import boolean
    import ansible.module_utils.facts.collectors.capabilities

    # NOTE: mock get_bin_path that capsh is available
    import unittest.mock
    capsh_path = unittest.mock.Mock(return_value='/mock/capsh')

    import sys
    import io
    stdout = io.StringIO()
    # NOTE: mock stdout

# Generated at 2022-06-13 02:24:09.531134
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:24:15.580338
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import cache
    from ansible.module_utils.facts import ansible_collector

    ansible_collector.get_module = lambda: None
    ansible_collector.get_bin_path = lambda x: '/bin/capsh' if x == 'capsh' else None

    # NOTE: passed CollectorTestModule instead of core's FakeModule to make
    # sure no unneeded function calls are made -akl
    module = cache.CollectorTestModule()

    module.run_command = lambda x, y: (0, 'Current: =pe\nBounding set =cap_chown,cap_dac_override,cap_fowner,cap_fsetid,cap_kill,cap_setgid,cap_setuid', None)
    c = SystemCapabilitiesFactCollector()
   

# Generated at 2022-06-13 02:24:19.728911
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Init
    mock_module = Mock()
    mock_module.run_command.return_value = (
        0,
        """
        Current: =ep
        Bounding set =ep
        Securebits: 00/0x0/1'b0
        secure-noroot: no (unlocked)
        secure-no-suid-fixup: no (unlocked)
        secure-keep-caps: no (unlocked)
        uid=0(root)
        gid=0(root)
        groups=0(root)
        """,
        ''
    )
    facts_dict = {}
    system_capabilities_enforced = 'NA'
    system_capabilities = []

    # Call
    cap = SystemCapabilitiesFactCollector()

# Generated at 2022-06-13 02:24:20.199007
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    assert True

# Generated at 2022-06-13 02:24:26.269211
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts import FactCollector
    import os
    import mock

    class Test(object):

        def __init__(self):
            self.facts = {}
            self.params = {}

        def set_fact(self, key, val):
            self.facts[key] = val

        def get_bin_path(self, key, path, opts=None):
            if key == 'capsh':
                return '/usr/bin/capsh'
            else:
                return None


# Generated at 2022-06-13 02:24:31.544774
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Setup
    module = Mock()
    module.run_command.return_value = (0, 'Current: =ep', '')
    # Expected result
    result = {
        'system_capabilities_enforced': 'False',
        'system_capabilities': []
    }
    # Actual result
    fact_collector = SystemCapabilitiesFactCollector()
    collected_facts = fact_collector.collect(module)
    # Test assertions
    assert result == collected_facts

# Generated at 2022-06-13 02:25:01.384082
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:25:10.012481
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts import get_module_obj
    import tempfile
    import os

    # setup fake fact module
    fact_module = get_module_obj('fake_fact_module')
    tmpdir = tempfile.mkdtemp()
    capsh_path = os.path.join(tmpdir, 'capsh')
    with open(capsh_path, 'wb') as capsh_binary:
        capsh_binary.write(to_bytes('#!/bin/sh\n'))
        capsh_binary.write(to_bytes('echo "Current: =ep"\n'))
        capsh_binary.close()
        os.chmod(caps_path, 0o755)

    # setup collector
    collector = SystemCapabilitiesFact

# Generated at 2022-06-13 02:25:20.407587
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import collector

    def mock_get_bin_path(bin, opts=None):
        if bin == 'capsh':
            return '/usr/bin/capsh'


# Generated at 2022-06-13 02:25:29.573988
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """
    SystemCapabilitiesFactCollector - method collect
    """
    module = AnsibleModuleMock()
    module.run_command=run_command_mock
    module.get_bin_path=get_bin_path_mock

    facter=SystemCapabilitiesFactCollector(module=module)

    # test all caps
    module.run_command.return_value = (0, out_caps_all, '')
    facter.collect()
    assert facter.collect()['system_capabilities'] == out_caps_all.split("=",1)[1].strip().split(",")

    # test no caps (not enforced)
    module.run_command.return_value = (0, out_caps_none, '')
    facter.collect()
    assert facter.collect()['system_capabilities']

# Generated at 2022-06-13 02:25:33.939811
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """Unit testing for method collect of class SystemCapabilitiesFactCollector"""
    module = None # place holder for testing.
    fact_collector = SystemCapabilitiesFactCollector()
    collected_facts = None
    facts_dict = fact_collector.collect(module,collected_facts)
    # This test does not have a plugin_collection as it does not need to stub the system
    # so we will assert that we got an empty dict.
    assert(isinstance(facts_dict, dict)),'Facts dict was not an instance of dict'

# Generated at 2022-06-13 02:25:39.192142
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    collector = SystemCapabilitiesFactCollector()
    assert not collector.collect()
    assert not collector.collect(collected_facts={'system_capabilities': True})
    assert not collector.collect(collected_facts={'system_capabilities_enforced': True})

    pytest.skip("start here -akl")
    # mock module
    # mock module.command
    # run method and validate results

# Generated at 2022-06-13 02:25:48.550307
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Compose mock module object
    class MockModule:
        def __init__(self, capsh_path):
            self.capsh_path = capsh_path

        def get_bin_path(self, path):
            return self.capsh_path


# Generated at 2022-06-13 02:25:55.144356
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    class TestModule(object):
        def __init__(self, rc=0, out='', err=''):
            self.rc = rc
            self.out = out
            self.err = err

        def get_bin_path(self, arg1):
            return arg1

        def run_command(self, args, errors):
            return self.rc, self.out, self.err


# Generated at 2022-06-13 02:26:05.521798
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """ Verify get_caps_data()/parse_caps_data() """
    mock_module = MagicMock()
    mock_collector = SystemCapabilitiesFactCollector()

    # No capsh binary
    mock_module.get_bin_path.return_value = None
    mock_facts = mock_collector._get_facts(mock_module)

    assert not mock_facts
    assert not mock_module.run_command.called

    # capsh binary
    mock_module.get_bin_path.return_value = '/bin/capsh'

    # capsh unexpeced output
    mock_module.run_command.return_value = (0, 'Current: =ep', '')
    mock_facts = mock_collector._get_facts(mock_module)


# Generated at 2022-06-13 02:26:11.496021
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """SystemCapabilitiesFactCollector.collect()
    with correct output
    """
    import os
    _cur_path = os.getcwd()
    test_file = os.path.join(_cur_path, 'SystemCapabilitiesFactCollector_collect_test_out.txt')

    import ansible_collections.ansible.community.plugins.module_utils.facts.system.caps as caps_module

    x = caps_module.SystemCapabilitiesFactCollector()
    collected_facts = {}
    collected_facts['system_capabilities'] = []

    from ansible.module_utils.facts.collector import BaseFactCollector
    y = BaseFactCollector()
    test_module = y.get_module(test_file)
    caps_caps_dict = x.collect(test_module, collected_facts)

# Generated at 2022-06-13 02:27:24.889531
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Execute the SystemCapabilitiesFactCollector's method collect
    # and test if it is as expected
    module = None
    system_capabilities_fact_collector = SystemCapabilitiesFactCollector()
    facts = system_capabilities_fact_collector.collect(module)

# Generated at 2022-06-13 02:27:30.347445
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    '''Test cases for SystemCapabilitiesFactCollector class'''
    from ansible.module_utils.facts.collectors.system import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts import FactManager
    from ansible.module_utils.facts.system.caps import get_caps_data
    from ansible.module_utils.facts.system.caps import parse_caps_data
    from ansible.module_utils.facts.system.caps import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts.system.caps import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts.system.caps import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts.system.caps import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts.system.caps import System

# Generated at 2022-06-13 02:27:32.298420
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: load or mock module(/bin/capsh) and/or method(/sbin/capsh) -akl
    pass


# Generated at 2022-06-13 02:27:41.890226
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Mimic module object
    class TestModule:
        def get_bin_path(self, path, args=[]):
            # NOTE: Test with no executable return values first, then path with executable
            # NOTE: Testcase for:
            # ansible.module_utils.facts.system.caps.SystemCapabilitiesFactCollector.collect
            if path == "capsh":
                return "/usr/bin/capsh"
            else:
                return None


# Generated at 2022-06-13 02:27:50.601321
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    # Given
    module = {'get_bin_path': lambda *args, **kwargs: '/sbin/capsh'}

# Generated at 2022-06-13 02:28:00.840683
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import tempfile
    import shutil
    import subprocess
    from ansible.module_utils.facts.collector.system import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts import ModuleFacts

    class module(object):
        def get_bin_path(self, exe, required=False):
            return exe

# Generated at 2022-06-13 02:28:01.836456
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # TODO
    pass

# Generated at 2022-06-13 02:28:10.446970
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
  from ansible.module_utils.facts import ModuleFacts
  from ansible.module_utils.facts.collector import BaseFactCollector
  from ansible.module_utils.facts.collectors.capabilities.system_capabilities import SystemCapabilitiesFactCollector
  from ansible.module_utils.six import string_types

  # Create a system capabilities collector object.
  collector = SystemCapabilitiesFactCollector()

  # Create a mock module.
  module = ModuleFacts(name='test',
                       argument_spec={},
                       supports_check_mode=True
                       )

  # Create a mock module.

# Generated at 2022-06-13 02:28:18.008065
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = object()
    module.get_bin_path = lambda x: '/usr/bin/capsh'
    module.run_command = lambda x, b: (0, "Current: =ep", "")
    capfact = SystemCapabilitiesFactCollector()
    result_dict = capfact.collect(module=module, collected_facts={})
    assert 'system_capabilities' in result_dict.keys()
    assert 'system_capabilities_enforced' in result_dict.keys()

# Generated at 2022-06-13 02:28:27.399207
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    # Mocking module input argument and facts
    module = Mock(return_value=None)
    collected_facts = {'system_capabilities': ['NONE']}
    capsh_path = 'capsh'

    # Mocking class to be instantiated without calling __init__
    class SystemCapabilitiesFactCollector:
        def __init__(self, module, collected_facts):
            pass

        def capsh_path(capsh_path):
            pass

        def get_caps_data(self, capsh_path):
            return 0, "Current:\t=ep\n", ""

        def parse_caps_data(self, caps_data):
            return {'system_capabilities_enforced': 'False', 'system_capabilities': ['NONE']}

    # Mocking __init__ and module.run_command methods
   