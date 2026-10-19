

# Generated at 2022-06-13 02:19:52.377275
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """
    Return a 'system_capabilities' and a 'system_capabilities_enforced' fact from the output of capsh.
    """
    collector = SystemCapabilitiesFactCollector()
    assert collector.collect() == {}
    # NOTE: -> mocked get_caps_data() for easier testing -akl
    assert collector.collect('fake module return') == {'system_capabilities': ['test_cap'],
                                                       'system_capabilities_enforced': 'True'}


# Generated at 2022-06-13 02:19:58.691143
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    test_module = type(sys)('test_module')
    test_module.get_bin_path = lambda x: '/bin/capsh'
    test_module.run_command = lambda *args, **kwargs: (0, 'Current: =ep\nAmbient: =\n', '')

    collector = SystemCapabilitiesFactCollector()

    facts = collector.collect(module=test_module)
    assert facts['system_capabilities'] == []
    assert facts['system_capabilities_enforced'] == 'False'


# Generated at 2022-06-13 02:20:08.862573
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    mock_module = Mock()

# Generated at 2022-06-13 02:20:14.839704
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.caps import SystemCapabilitiesFactCollector

    # Create a ModuleStub to use for the test
    test_module_stub = CollectorModuleStub()
    
    # Ensure that the 'capsh' binary exists under the path module_stub.get_bin_path()
    test_module_stub.bin_path_for_bins['capsh'] = '/usr/bin/capsh'

    # Create a facts collecter
    test_collector = Collector(module=test_module_stub)

    # Register the 'capsh' facts collector with the facts collector
    test_collector.register_collector(SystemCapabilitiesFactCollector())

    # Call the collect method to get the facts

# Generated at 2022-06-13 02:20:18.168377
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: write unit test for check of 'system_capabilities' fact
    # NOTE: use mock for module (ansible.module_utils.facts.module_common.AnsibleModule)
    # NOTE: and for subprocess.Popen()
    # NOTE: create test data (capsh command and its output)
    pass

# Generated at 2022-06-13 02:20:25.214602
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import os
    module = AnsibleModule(argument_spec={})
    module.run_command = MagicMock()
    module.run_command.return_value = (0, 'Current: =ep', '')
    module.get_bin_path = MagicMock()
    module.get_bin_path.return_value = os.path.realpath(__file__)
    SCFC = SystemCapabilitiesFactCollector(module)
    assert SCFC.collect() == {'system_capabilities_enforced': 'False', 'system_capabilities': []}

    module.run_command.return_value = (0, 'Current: =ep cap_net_admin,cap_bluetooth_admin,cap_net_raw+eip', '')
    SCFC = SystemCapabilitiesFactCollector(module)

# Generated at 2022-06-13 02:20:34.709203
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    testmod = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode=True
    )
    testmod.run_command = MagicMock(return_value=(0, 'Current: =ep', ''))

    expected_facts = { 'system_capabilities_enforced': 'False',
                        'system_capabilities': [] }
    assert SystemCapabilitiesFactCollector.collect(None, testmod) == expected_facts
    testmod.run_command.assert_called_once_with(['/usr/sbin/capsh', '--print'], errors='surrogate_then_replace')



# Generated at 2022-06-13 02:20:44.566691
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: fact cache is not passed, no caching for now
    fact_collector = SystemCapabilitiesFactCollector(None)
    # NOTE: fact cache is not updated for now, no caching for now
    facts_dict = fact_collector.collect()

    # Only tests that the data collection works
    # Content of system_capabilities_enforced can be None/NA/True/False, check as string
    assert 'system_capabilities_enforced' in facts_dict
    assert isinstance(facts_dict['system_capabilities_enforced'], str)
    assert 'system_capabilities' in facts_dict
    assert isinstance(facts_dict['system_capabilities'], list)

# Generated at 2022-06-13 02:20:54.644921
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils import basic
    from ansible.module_utils.facts import collector

    test_module = basic.AnsibleModule(
        argument_spec = dict()
    )

    test_module.params = None


# Generated at 2022-06-13 02:21:05.927410
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible_collections.ansible.community.tests.unit.module_utils._text import to_bytes
    def test_module(module_name, **kwargs):
        if module_name == 'ansible.module_utils.system_capabilities_available':
            return True
        else:
            return False
    def test_run_command(command, **kwargs):
        return 0,to_bytes(
                    'Current:\n'
                    ' = cap_net_admin,cap_setgid,cap_setuid+ep\n'
                    'Bounding set =cap_sys_admin,cap_sys_chroot,cap_sys_ptrace,cap_dac_override,cap_setgid,cap_setuid'),to_bytes('')

# Generated at 2022-06-13 02:21:18.382860
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    mock_module = Mock()

    # Mock out a valid capsh path, and a valid capsh output
    mock_module.get_bin_path.return_value = "/bin/capsh"

# Generated at 2022-06-13 02:21:24.755721
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import json
    import sys
    import os
    import unittest
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.collector
    from ansible.module_utils.facts.collector import BaseFactCollector

# Generated at 2022-06-13 02:21:36.190243
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils import basic
    module = basic.AnsibleModule(
        argument_spec = dict()
    )
    module.run_command = mock.Mock(return_value=(0,'Current: = cap_chown,cap_dac_override+eip cap_setgid+ep cap_setuid+ep\nBounding set =cap_chown,cap_dac_override+eip cap_setgid+ep cap_setuid+ep\nSecurebits: 00/0x0/1'))
    collector = SystemCapabilitiesFactCollector(module)
    res = collector.collect()
    assert(res['system_capabilities_enforced'] is 'True')

# Generated at 2022-06-13 02:21:39.309305
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    assert SystemCapabilitiesFactCollector.collect() == {
        'system_capabilities': [],
        'system_capabilities_enforced': 'NA'
    }

# Generated at 2022-06-13 02:21:48.976773
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import ModuleStub
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts import get_module_facts
    import tempfile

    m = ModuleStub()
    collected_facts = get_module_facts(m)

    fd = tempfile.NamedTemporaryFile(delete=False)
    fd.close()

    m.run_command = lambda args, **kwargs: (0, to_bytes('Current: =ep'), to_bytes(''))
    fact_collector = SystemCapabilitiesFactCollector(m, collected_facts)
    assert fact_collector.collect()['system_capabilities_enforced'] == 'False'
    assert fact_collect

# Generated at 2022-06-13 02:21:57.030539
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import os
    import re
    import pdb
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts import runner


# Generated at 2022-06-13 02:22:03.789424
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    try:
        import os
        import mock
    except:
        import unittest.mock as mock

    module_mock = mock.Mock()

# Generated at 2022-06-13 02:22:13.311859
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """
    Test for the collect method of class SystemCapabilitiesFactCollector
    """
    # NOTE: capsh does not exist in Docker image
    # mock class attributes
    caps_fact_collector = SystemCapabilitiesFactCollector()
    # mock fetch method of the BaseFactCollector
    caps_fact_collector.fetch_base_facts = MagicMock(name='fetch_base_facts')
    # mock get_bin_path
    caps_fact_collector.fetch_base_facts.module.get_bin_path = MagicMock(name='get_bin_path')
    # if capsh path exists
    caps_fact_collector.fetch_base_facts.module.get_bin_path.return_value = '/usr/bin/capsh'
    # mock run_command
    caps_fact_collect

# Generated at 2022-06-13 02:22:23.287596
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import importlib
    import os
    import sys
    import tempfile
    import copy
    import shutil
    import ansible.module_utils.facts.collector
    module = importlib.import_module('ansible.module_utils.facts.collector')
    cap_path = '/usr/bin/capsh'
    test_subdir = 'test_facts'
    test_dir = os.path.join('/tmp', test_subdir)
    if not os.path.isdir(test_dir):
        os.makedirs(test_dir)
    capsh_test_script = os.path.join(test_dir, 'capsh')

# Generated at 2022-06-13 02:22:27.454991
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = mock.MagicMock()
    module.run_command.return_value = 0, 'Current: =ip', ''
    module.get_bin_path.return_value = 'capsh_path'

    system_capabilities_enforced_facts = {}
    system_capabilities_facts = {}
    module.exit_json.assert_called_with(
        ansible_facts={'system_capabilities': system_capabilities_facts,
                       'system_capabilities_enforced': system_capabilities_enforced_facts})

# Generated at 2022-06-13 02:22:34.271134
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    SystemCapabilitiesFactCollector().collect()

# Generated at 2022-06-13 02:22:39.790118
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    capsh_path = '/usr/bin/capsh'
    module = MagicMock()
    module.get_bin_path.return_value = capsh_path

# Generated at 2022-06-13 02:22:50.182140
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import ansible.module_utils.facts.collectors.system.caps as caps
    import tempfile
    import mock
    import os

    # methods to mock

# Generated at 2022-06-13 02:22:51.080476
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # TODO: implement unit test
    pass

# Generated at 2022-06-13 02:22:52.230466
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    SystemCapabilitiesFactCollector.collect()

# Generated at 2022-06-13 02:22:59.540466
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import json
    import os
    import tempfile
    import textwrap

    # NOTE: unittest doesn't seem to handle patching modules,
    # might need to move to pytest. -akl
    #
    # NOTE: setup a fake capsh executable with some expected
    # output. -akl
    capsh_path = os.path.join(tempfile.mkdtemp(), 'capsh')

# Generated at 2022-06-13 02:23:02.164113
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    test_obj = SystemCapabilitiesFactCollector()
    assert test_obj.collect() == {'system_capabilities': [], 'system_capabilities_enforced': 'NA'}

# Generated at 2022-06-13 02:23:11.015696
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import os
    import tempfile

    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector.system import SystemCapabilitiesFactCollector

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True)

    # prepare some files
    (fd, capsh_path) = tempfile.mkstemp()
    with open(fd, 'wb') as f:
        os.fchmod(fd, 0o755)

# Generated at 2022-06-13 02:23:22.008620
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_text


    ################################################################
    # Dummy Module
    class DummyModule:
        base_dir = '.'
        params = {
            'gather_subset': 'all',
            'gather_timeout': 10
        }
        def __init__(self):
            self.facts = {}
        def get_bin_path(self, app):
            return app
        # NOTE: get_caps_data()/parse_caps_data() for easier mocking -akl
        def run_command(self, cmd, errors='surrogate_then_replace'):
            capsh_path = cmd[0]

# Generated at 2022-06-13 02:23:24.617117
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    test = SystemCapabilitiesFactCollector()
    assert test.collect(collected_facts={'somekey': False}) == {'somekey': False}

# Generated at 2022-06-13 02:23:37.058596
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    mock_module = Mock(params = dict(), run_command = run_command)
    sc = SystemCapabilitiesFactCollector()
    caps = sc.collect(mock_module)
    
    # Check that we got the enforced capabilities right
    assert caps['system_capabilities_enforced'] == 'True'
    
    # Check that we got the capabilities right
    assert caps['system_capabilities'] == enforced_caps

#Unit test for the collect method if capsh is not available

# Generated at 2022-06-13 02:23:42.628488
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import ansible.module_utils.facts.system.caps as caps
    import ansible.module_utils.facts.collectors.system.caps as caps_collector
    import ansible.module_utils.facts.system.caps as caps
    import ansible.module_utils.facts.collectors.system.caps as caps_collector

    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.test import set_module_args, AnsibleExitJson, AnsibleFailJson

    capsh_path = '/bin/capsh'

    def get_caps_data(path=capsh_path, module=None):
        cmd = [path, "--print"]
        rc, out, err = module.run_command(cmd, errors='surrogate_then_replace')

# Generated at 2022-06-13 02:23:43.423773
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:23:49.183945
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """
    Collects the output of the command 'capsh --print'.
    """
    import ansible.module_utils.facts.system.caps as sys_caps

    test_module = sys_caps.AnsibleModuleMock('ansible.module_utils.facts.system.caps')

    collector = sys_caps.SystemCapabilitiesFactCollector()
    result = collector.collect(test_module, None)

    assert result['system_capabilities_enforced'] == 'NA'
    assert result['system_capabilities'] is None

# Generated at 2022-06-13 02:23:59.258170
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import ansible_collector

    # mock facts
    # ansible_facts['ansible_default_ipv4']['address'] = '192.0.2.1'
    ansible_facts = {
        'module_setup': True,
        'system_capabilities_enforced': 'NA',
        'system_capabilities': [],
    }

    # mock module
    from ansible.module_utils.facts import ansible_local
    ansible_module_instance = ansible_local.AnsibleModule(
        argument_spec={})
    ansible_module_instance.get_bin_path = (
        lambda x: '/bin/capsh')  # NOTE: -> get_caps_data()/parse_caps_data()
    ansible_module_instance.run_

# Generated at 2022-06-13 02:24:05.508849
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Patch AnsibleModule to return sensible values
    m = MockAnsibleModule()
    m.get_bin_path.return_value = '/bin/capsh'
    m.run_command.return_value = (0, 'Current: =ep Bounding set =cap_sys_chroot+p cap_sys_admin+eip', '')
    # Create a SystemCapabilitiesCollector object for testing
    collector = SystemCapabilitiesFactCollector(m)
    # Call the collect method
    result = collector.collect()
    # Check the result
    assert result == {'system_capabilities': [], 'system_capabilities_enforced': 'False'}


# Generated at 2022-06-13 02:24:13.104296
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import ansible.module_utils.facts.collector.system.system_capabilities as module
    from types import ModuleType
    from ansible.module_utils.facts import Facts
    from ansible.module_utils.facts.collector.system.system_capabilities import SystemCapabilitiesFactCollector as TestSystemCapabilitiesFactCollector
    from ansible.module_utils.six.moves import builtins
    import sys
    import copy
    import os
    # create instance of mock -akl
    mock = ModuleType("mock")
    mock.run_command = TestSystemCapabilitiesFactCollector
    mock.get_bin_path = TestSystemCapabilitiesFactCollector
    mock.get_caps_data = TestSystemCapabilitiesFactCollector
    mock.parse_caps_data = TestSystemCapabilitiesFactCollector

    # mock out '

# Generated at 2022-06-13 02:24:13.988760
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
  pass

# Generated at 2022-06-13 02:24:21.453128
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import tempfile

    module = Mock()
    module.get_bin_path.return_value = tempfile.gettempdir()
    module.run_command.return_value = 0, 'Current: =ep\nBounding set =cap_setpcap,cap_sys_nice', ''
    facts = SystemCapabilitiesFactCollector.collect(module)
    assert facts['system_capabilities'] == ['cap_setpcap', 'cap_sys_nice']
    assert facts['system_capabilities_enforced'] == 'False'

# Generated at 2022-06-13 02:24:26.531201
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = FakeModule('/usr/lib/systemd/systemd')
    fact_collector = SystemCapabilitiesFactCollector()
    collected_facts = fact_collector.collect(module)

    assert collected_facts["system_capabilities_enforced"] == "True"
    assert collected_facts["system_capabilities"] == ['= cap_net_admin', '= cap_net_raw', '=ep']



# Generated at 2022-06-13 02:24:50.292735
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import get_collector_instance
    
    # Mocked method
    class LinuxAnsibleModule_Mocked:
        def __init__(self, argument_spec=None, bypass_checks=False, no_log=False, check_invalid_arguments=True,
                     mutually_exclusive=None, required_together=None, required_one_of=None,
                     add_file_common_args=False, supports_check_mode=False, required_if=None):
            pass

        def get_bin_path(self, executable, opt_dirs=[]):
            return '/bin/capsh'


# Generated at 2022-06-13 02:24:56.856085
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():#
    import ansible.module_utils.facts.system.caps
    import ansible.module_utils.facts.system.caps as caps_mod
    import ansible.module_utils.facts.system.caps as caps_module
    from ansible.module_utils.facts.system.caps import test_SystemCapabilitiesFactCollector_collect
    import sys
    import os
    ansible.module_utils.facts.collector.BaseFactCollector.collect(self=ansible.module_utils.facts.system.caps.SystemCapabilitiesFactCollector, module=ansible.module_utils.facts.collector.BaseFactCollector, collected_facts=ansible.module_utils.facts.collector.BaseFactCollector)

# Generated at 2022-06-13 02:24:58.142619
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: fake module required to be available to 'run_command'
    pass

# Generated at 2022-06-13 02:25:07.386453
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector.system.capabilities import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts.collector.system import SystemCollector
    from ansible.module_utils.facts.utils import get_file_content

    def mock_run_command(self, args, check_rc=True):
        my_str = get_file_content('system_capabilities_capsh_result.txt')
        my_str = my_str.replace('\n', ' ')
        my_str = my_str.replace('  ', ' ')
        my_list = my_str.split(' ')
        return my_list[0], my_list[1], my_list[2]

    def myeq(thing1, thing2):
        return thing1 == thing2

   

# Generated at 2022-06-13 02:25:07.874702
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:25:09.763345
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    result = SystemCapabilitiesFactCollector.collect()
    assert result
    assert 'system_capabilities_enforced' in result
    assert 'system_capabilities' in result

# Generated at 2022-06-13 02:25:12.521270
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: mock 'module' argument -akl
    fake_module = Mock()
    facts_dict = SystemCapabilitiesFactCollector().collect(module=fake_module)
    assert facts_dict == {}

# Generated at 2022-06-13 02:25:18.238010
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import collector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector.system.capabilities import SystemCapabilitiesFactCollector

    collector.collectors = set()
    cap = SystemCapabilitiesFactCollector()
    BaseFactCollector.collectors.add(cap)

# Generated at 2022-06-13 02:25:27.619904
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.six import iteritems

    class StubModule(object):
        def get_bin_path(self, cmd, opt_dirs=[]):
            return '/bin/capsh'


# Generated at 2022-06-13 02:25:34.149876
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    from ansible.module_utils import basic
    import ansible.module_utils.facts.collector
    from ansible.module_utils._text import to_bytes

    # Create a fake module
    fake_module = basic.AnsibleModule(argument_spec={})
    # Set the module's run_command method, we'll mock the actual
    # method because we don't care about running commands in this
    # unit test.

# Generated at 2022-06-13 02:26:10.093684
# Unit test for method collect of class SystemCapabilitiesFactCollector

# Generated at 2022-06-13 02:26:11.141688
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    SystemCapabilitiesFactCollector.collect()

# Generated at 2022-06-13 02:26:20.679619
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    module = Mock()
    module.get_bin_path.return_value = 'capsh_path'

    # Test case 1: Expected to return all values as list in facts_dict
    module.run_command.return_value = (0, 'Current: =ep Bounding set =eip cap_file_dac_read+p cap_file_dac_write+ep cap_kill+ep cap_dac_read_search+p cap_dac_override+ep cap_sys_admin+ep', '')
    capsh_collector = SystemCapabilitiesFactCollector()
    result = capsh_collector.collect(module)

    assert(result['system_capabilities_enforced'] == 'False')

# Generated at 2022-06-13 02:26:29.768400
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """
    If we can find the capsh binary, the run it with arguments --print,
    and parse the output to determine system_capabilities and
    system_capabilities_enforced
    """
    class MockModule:
        def __init__(self, rc, out, err):
            self.rc = rc
            self.out = out
            self.err = err
            self.run_command_called = 0

        def run_command(self, args, errors):
            assert (args == ['/usr/bin/capsh', '--print'])
            self.run_command_called += 1
            return self.rc, self.out, self.err

        def get_bin_path(self, binary):
            if binary == 'capsh':
                return '/usr/bin/capsh'
            else:
                return None



# Generated at 2022-06-13 02:26:37.380343
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    class MockModule(object):
        def run_command(self, *args, **kwargs):
            # This is mocked away because we just need to test the parsing of
            # the capsh command
            output = (
                0,
                'Current: =ep',
                ''
            )
            return output
        def get_bin_path(self, *args, **kwargs):
            return '/bin/capsh'

    sut = SystemCapabilitiesFactCollector()
    result = sut.collect(module=MockModule())
    assert result['system_capabilities_enforced'] == 'False'
    assert result['system_capabilities'] == []

# Generated at 2022-06-13 02:26:43.411717
# Unit test for method collect of class SystemCapabilitiesFactCollector

# Generated at 2022-06-13 02:26:53.460599
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Create a fake module
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import ModuleDeprecationWarning
    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=ModuleDeprecationWarning)
        module = AnsibleModule(argument_spec={})

    # mock the methods
    from ansible.module_utils.facts.collector import BaseFactCollector
    BaseFactCollector.get_module_path = lambda self: '/module/path/'
    BaseFactCollector.get_file_content = lambda self, fp: 'file content of {}'.format(fp)

    # mock the shared module object
    import os
    import tempfile
    real_os_path = os.path

# Generated at 2022-06-13 02:27:02.310508
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import json
    import os
    from ansible.module_utils.facts.collector.system.sysctl import SystemCapabilitiesFactCollector


# Generated at 2022-06-13 02:27:13.409226
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass
#     # NOTE: refactor to use a MagicMock which uses a configurable
#     #       side_effect method to return the values we want to test -akl
#     # NOTE: based on SystemD fact collector tests -akl
#     # NOTE: this function test really needs to use a Mock module class -akl
#     def run_command_mock(params, *_args, **_kwargs):
#         if params == [capsh_path, 'print']:
#             return 0, out, ''
#         return None
#
#     fake_module = mock.MagicMock(get_bin_path=mock.MagicMock(return_value=capsh_path))
#     fake_module.run_command = run_command_mock
#     false_collector = SystemCapabilitiesFactCollector()


# Generated at 2022-06-13 02:27:23.304766
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import FactsCollector
    from ansible.module_utils.facts.collectors.capabilities import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts.system.capabilities import get_caps_data, parse_caps_data
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.six.moves import mock


# Generated at 2022-06-13 02:28:29.883614
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import FactsCollector
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.collector import list_fact_collectors
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts import _variable_manager

    loader = _variable_manager.get_vars_loader()
    sut = get_collector_instance(SystemCapabilitiesFactCollector)

    with pytest.raises(TypeError):
        # No params = fail
        sut.collect()

    with pytest.raises(TypeError):
        # Wrong param = fail
        sut.collect(module=loader)

    # No capsh_path = return empty dict
   

# Generated at 2022-06-13 02:28:35.439852
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    fact_collector = SystemCapabilitiesFactCollector('')
    fact_collector._module = ''
    assert fact_collector.collect() == {}
    fact_collector.name = 'capsh'
    fact_collector._module.get_bin_path.return_value = True
    fact_collector._module.run_command.return_value = (0, 'Current: =ep', '')
    assert fact_collector.collect() == {'system_capabilities': [], 'system_capabilities_enforced': 'False'}
    fact_collector._module.run_command.return_value = (0, 'Current: ^ep', '')
    assert fact_collector.collect() == {'system_capabilities': ['ep'], 'system_capabilities_enforced': 'True'}
    fact_collect

# Generated at 2022-06-13 02:28:36.184159
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass


# Generated at 2022-06-13 02:28:39.710611
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # arrange
    collector = SystemCapabilitiesFactCollector()
    collector.file_name = 'CapEff'

    # act
    result = collector.collect()

    # assert
    assert result == {'system_capabilities_enforced': 'True', 'system_capabilities': []}

# Generated at 2022-06-13 02:28:45.240490
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible_collections.ansible.community.tests.unit.module_utils.facts.test_SystemCapabilitiesFactCollector import test_module
    fact_collector = SystemCapabilitiesFactCollector(module=test_module())


# Generated at 2022-06-13 02:28:45.769798
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:28:46.510609
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # avoid 'argument must be an int' error due to mock
    return

# Generated at 2022-06-13 02:28:53.515614
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import collections
    import unittest.mock as mock
    # Initialize
    module = mock.Mock()

# Generated at 2022-06-13 02:28:55.807820
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import ansible.module_utils.facts.collector
    res = ansible.module_utils.facts.collector.get_collector_facts(SystemCapabilitiesFactCollector, {})
    assert('system_capabilities_enforced' in res['ansible_facts']['caps'] and len(res['ansible_facts']['caps']) == 2)

# Generated at 2022-06-13 02:28:58.510977
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Unit test: Return an empty dict.
    m = SystemCapabilitiesFactCollector()
    assert type(m.collect()) == dict
    assert m.collect() == {'system_capabilities_enforced': 'NA', 'system_capabilities': []}