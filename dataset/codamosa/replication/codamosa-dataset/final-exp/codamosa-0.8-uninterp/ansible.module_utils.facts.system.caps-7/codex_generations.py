

# Generated at 2022-06-13 02:19:55.255787
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    import os

    import ansible.utils.display
    from ansible.module_utils.facts.collector import Collector

    module = MockModule()
    module.run_command = Mock(return_value=(0, 'Current: =ep', ''))
    collect = Collector.fetch_collector(SystemCapabilitiesFactCollector.name, module)
    assert collect is not None
    fact_dict = collect.collect(module=module)
    assert fact_dict
    assert fact_dict['system_capabilities_enforced'] == 'False'
    assert fact_dict['system_capabilities'] == []

    module.run_command = Mock(return_value=(0, 'Current: =ep cap_chown,cap_dac_override+eip', ''))
    fact_dict = collect.collect(module=module)
    assert fact

# Generated at 2022-06-13 02:19:55.774426
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:20:06.447961
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import FactsCollector

    #Attempt to use an instance of FactsCollector
    collector = FactsCollector(None)
    #Prior to assigning values, check if the value of a fact is None
    assert collector.get_fact(SystemCapabilitiesFactCollector.name) is None

    #See if we can assign a value to a fact
    collector._facts[SystemCapabilitiesFactCollector.name] = True
    #Check if the value of the fact is the one we expect
    assert collector.get_fact(SystemCapabilitiesFactCollector.name) is True

    #Create an instance of SystemCapabilitiesFactCollector

# Generated at 2022-06-13 02:20:07.351930
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: will unit test this when module_utils/system/capsh.py is converted -akl
    assert True

# Generated at 2022-06-13 02:20:14.162639
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Note: 'module_utils.facts.collector.BaseFactCollector' is the one to be mocked
    #       and not 'ansible.module_utils.facts.collector.SystemCapabilitiesFactCollector'
    #       itself ('capsh' binary is mocked by 'ansible_collections.ansible.community.plugins.module_utils.facts.capsh.capsh'
    #       where 'ansible_collections.ansible.community.plugins.module_utils.facts.capsh.capsh.CAPSH_BINARY'
    #       is setup with the output of 'capsh --print')
    pass

# Generated at 2022-06-13 02:20:15.217607
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass
# vim: set et ts=4 sts=4 sw=4:

# Generated at 2022-06-13 02:20:21.548247
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = AnsibleModuleMock()
    module.run_command = run_command
    module.get_bin_path = get_bin_path

    obj = SystemCapabilitiesFactCollector()
    result = obj.collect(module)

    assert result['system_capabilities_enforced'] == 'True'
    assert result['system_capabilities'] == ['chown', 'dac_override', 'fowner', 'fsetid', 'kill', 'setgid', 'setuid', 'setpcap', 'net_bind_service', 'net_raw', 'sys_chroot', 'mknod', 'audit_write', 'setfcap']



# Generated at 2022-06-13 02:20:26.614060
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import mock
    module = mock.Mock()
    module.run_command.return_value = 0, '', ''

    fact_collector = SystemCapabilitiesFactCollector()
    facts_dict = fact_collector.collect(module=module)

    assert facts_dict['system_capabilities'] == []
    assert facts_dict['system_capabilities_enforced'] == 'NA'



# Generated at 2022-06-13 02:20:37.193294
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    m = MockModule()
    c = SystemCapabilitiesFactCollector(m)

# Generated at 2022-06-13 02:20:38.371934
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    assert 1 == 1

# Generated at 2022-06-13 02:20:50.045962
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    mock_module = Mock()

    mock_capsh_path = 'path'
    mock_out = '''Current: = cap_setuid,cap_sys_chroot+eip
Bounding set =cap_chown,cap_dac_override,cap_dac_read_search,cap_fowner,cap_fsetid,cap_kill,cap_setgid,cap_setuid,cap_setpcap,cap_net_bind_service,cap_net_raw,cap_sys_chroot,cap_mknod,cap_audit_write,cap_setfcap+eip
Securebits: 00/0x0/1'''
    mock_rc = 0
    mock_err = []

    mock_command = ['capsh', '--print']
    mock_module.run_command.return_value

# Generated at 2022-06-13 02:20:56.269792
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = FakeAnsibleModule()
    SystemCapabilitiesFactCollector(module=module, collected_facts=None).collect()
    assert module.facts['system_capabilities'] == ['chown', 'dac_override', 'fowner', 'fsetid', 'kill', 'setgid', 'setuid', 'setpcap', 'net_bind_service', 'net_raw', 'sys_chroot', 'mknod', 'audit_write', 'setfcap']


# Generated at 2022-06-13 02:21:07.570067
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import os
    import sys

    import mock
    import unittest

    class SystemCapabilitiesFactCollectorTestCase(unittest.TestCase):
        def setUp(self):
            self.fake_capsh_path = os.path.join('/', 'path', 'to', 'capsh')

# Generated at 2022-06-13 02:21:08.826447
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # FIXXME: 'mock' object needed
    return None

# Generated at 2022-06-13 02:21:18.244457
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = get_module()
    capsh_path = module.get_bin_path('capsh')

    # NOTE: move to test_utils.py and use call_with_mocked_command() -akl

# Generated at 2022-06-13 02:21:23.356718
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    mock_ansible_module = MockAnsibleModule()
    mock_ansible_module.get_bin_path = Mock(return_value=True)
    mock_ansible_module.run_command = Mock(return_value=(0, 'Current: =ep',
                                                         'Current: =ep'))
    mock_collector = SystemCapabilitiesFactCollector()
    assert mock_collector.collect(module=mock_ansible_module) == {
            'system_capabilities': [],
            'system_capabilities_enforced': 'False'
    }



# Generated at 2022-06-13 02:21:27.724707
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import sys
    sys.path.append('/usr/local/lib/python2.7/dist-packages/ansible')
    import ansible.module_utils
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.system.caps
    import types
    import unittest

    class AnsibleModule:
        def __init__(self):
            self.run_command_rc = 0
            self.run_command_out = 'Current: =   Current:=ip cap_setpcap,cap_setfcap+eip capsh --print'
            self.run_command_err = ''

        def get_bin_path(self):
            return '/usr/bin/capsh'


# Generated at 2022-06-13 02:21:28.692744
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:21:30.030580
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    fc = SystemCapabilitiesFactCollector()
    fc.collect(None, None)

# Generated at 2022-06-13 02:21:36.391539
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts import BaseFactModule
    from ansible.module_utils._text import to_bytes

    module = BaseFactModule()
    result = ansible_collector.get_collector("SystemCapabilitiesFactCollector").collect(module)

    assert isinstance(result, dict)
    # assert 'system_capabilities_enforced' in result
    # assert 'system_capabilities' in result

# Generated at 2022-06-13 02:21:42.379986
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:21:50.808278
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    mock_module = MockModule()
    mock_module.run_command = Mock(return_value=(0, 'Current: =ep', ''))
    facts_collector = SystemCapabilitiesFactCollector()
    facts_collector.collect(module=mock_module)
    assert mock_module.run_command.call_count == 1
    assert mock_module.run_command.call_args == call([mock_module.get_bin_path('capsh'), "--print"])
    assert facts_collector.collect(module=mock_module) == {'system_capabilities': [], 'system_capabilities_enforced': 'False'}

    mock_module.run_command.return_value = (0, 'Current: = cap_net_admin,cap_net_raw+eip', '')
    assert facts_

# Generated at 2022-06-13 02:21:58.967017
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import ansible.module_utils.facts.system.caps

    class MockModule(ansible.module_utils.facts.system.caps.BaseFile):
        def __init__(self, *args, **kwargs):
            super(MockModule, self).__init__(*args, **kwargs)
            self.run_command_rc = 0

# Generated at 2022-06-13 02:22:05.090013
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # unit test common objects, modules and methods
    m_ansible_module = Mock()
    m_ansible_module.run_command.return_value = (0, "Current: =ep\nSecurebits: 00/0x0/1'b0", '')
    m_ansible_module.get_bin_path.return_value = 'capsh_path'
    m_ansible_module.exit_json = lambda x: None

    # unit test object
    system_capabilities_fact_collector = SystemCapabilitiesFactCollector()

    # unit test execution
    system_capabilities_fact_collector.collect(m_ansible_module, {})

    # unit test assertions
    m_ansible_module.get_bin_path.assert_called_once_with('capsh')
    m_ansible_

# Generated at 2022-06-13 02:22:06.516272
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    
    sys_class = SystemCapabilitiesFactCollector()
    
    assert sys_class.collect() == {}

# Generated at 2022-06-13 02:22:11.976793
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import ModuleDataCollector
    from ansible.module_utils.facts.collector import TestModule
    
    module_data_collector = ModuleDataCollector()
    module_data_collector.collect()
    ansible_module = module_data_collector.ansible_module
    
    SystemCapabilitiesFactCollector.collect(ansible_module)

# Generated at 2022-06-13 02:22:21.008003
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    module = basic.AnsibleModule(
        argument_spec={},
        supports_check_mode=True,
    )

    def mock_get_bin_path(name, opts=None, required=False):
        return '/bin/capsh'

    def mock_run_command(cmd, check_rc=True, close_fds=True, executable=None, data=None, binary_data=False, path_prefix=None, cwd=None,
                         use_unsafe_shell=False, env_variables=None, errors='surrogate_then_replace',
                         encoding='utf-8', values_sep='\n', expand_user_and_vars=False):
        return 0, to_bytes

# Generated at 2022-06-13 02:22:30.518995
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import tempfile

    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts import collector
    import ansible.module_utils.facts.collectors.system.caps as caps

    class TestModule(object):
        def __init__(self, exit_json, run_command, is_capable):
            self.exit_json = exit_json
            self.run_command = run_command
            self.is_capable = is_capable

        def fail_json(self, *args, **kwargs):
            self.exit_json(msg='ERROR: {0}'.format(args), failed=True)


# Generated at 2022-06-13 02:22:31.309769
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: implement this unit test -akl
    pass

# Generated at 2022-06-13 02:22:31.648908
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    return

# Generated at 2022-06-13 02:22:47.311634
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # use a local import to avoid polluting the real __import__() cache
    from ansible.module_utils.facts.collector import get_collector_instance
    assert isinstance(get_collector_instance('system_capabilities'), SystemCapabilitiesFactCollector)

# Generated at 2022-06-13 02:22:54.949554
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import FactsCollector

    mock_module = Mock()
    mock_module.run_command.return_value = (0, 'Current: =ep', '')

    # Get a SystemCapabilitiesFactCollector instance
    system_cap_fc = FactsCollector.get_collector('caps', mock_module)

    # Call method collect on this instance
    facts_dict = system_cap_fc.collect()

    # Run asserts
    assert facts_dict['system_capabilities_enforced'] == 'False'
    assert facts_dict['system_capabilities'] == []



# Generated at 2022-06-13 02:22:57.838634
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    my_caps = SystemCapabilitiesFactCollector()
    assert my_caps.collect() == {}

# Generated at 2022-06-13 02:23:07.594228
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import ansible_module
    from ansible.module_utils.facts.collector import AnsibleFactsCollector
    from ansible.module_utils.facts.collector.system import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts.collector.system.caps import get_caps_data, parse_caps_data
    import os
    import mock

    module_name = 'ansible_test_module'


    module_mock = ansible_module.AnsibleModule(
        argument_spec={},
        supports_check_mode=True,
    )


    def get_bin_path_mock(path):
        return '/usr/bin/'+path


# Generated at 2022-06-13 02:23:17.876707
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import sys
    import signal
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    sys.stdin = open(__file__, 'rb')
    collected_facts = {}
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts import get_collector_object
    from ansible.module_utils.facts import get_all_collector_objects
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.system.caps import SystemCapabilitiesFactCollector
    import ansible.module_utils.facts.collector
    ansible.module_utils.facts.collector.COLLECTORS['system'] = ['caps']
    collector_obj = get_collector_

# Generated at 2022-06-13 02:23:25.357457
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    m = MockModule()
    c = SystemCapabilitiesFactCollector()
    f = c.collect(m)

    # Ensure that the correct facts are returned
    assert f['system_capabilities_enforced'] == 'True'
    assert f['system_capabilities'] == ['chown', 'dac_override', 'fowner', 'fsetid', 'kill', 'setgid', 'setuid', 'setpcap', 'net_bind_service', 'net_raw', 'sys_chroot', 'mknod', 'audit_write', 'setfcap']


# Generated at 2022-06-13 02:23:35.252170
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import FakeModule
    from ansible.module_utils.facts.collector import run_command
    from copy import copy
    import json
    import platform

    SystemCapabilitiesFactCollector.run_command = run_command
    FakeModule.run_command = run_command

    testable_facts = {}
    testable_facts['system'] = platform.system().lower()

    testable_facts_json = json.dumps(testable_facts)

    module = FakeModule(
        json.loads(testable_facts_json),
        './tests/testdata/SystemCapabilitiesFactCollector_test_data.txt'
    )

    collector = SystemCapabilitiesFactCollector(module=module, collected_facts=None)

    fact_data_dict = {}
    fact_data

# Generated at 2022-06-13 02:23:40.784084
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: this test requires executable 'capsh' installed
    try:
        from ansible.module_utils.basic import _load_params
        from ansible.module_utils.facts.collector import get_collector_instance

        facts_collector = get_collector_instance(SystemCapabilitiesFactCollector)
        params = dict(
            ANSIBLE_MODULE_ARGS=dict(
                gather_subset=[facts_collector.name],
            ),
        )
        module = _load_params(params)
        facts_collector.collect(module=module)
    except Exception:
        pass

# Unit test SystemCapabilitiesFactCollector module

# Generated at 2022-06-13 02:23:49.600329
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collectors.system.caps import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts.utils import get_file_lines
    # creating singleton instance
    Collector.init_singleton()
    capsh_path = '/tmp/capshpath'

    class FakeModule(object):
        def get_bin_path(self, path):
            return capsh_path

        def run_command(self, cmd, **kwargs):
            if cmd[0] == capsh_path:
                return 0, ' '.join(['Current: =ep', 'Bounding set =eip', 'Securebits: 00/0x0/1', 'Kernel output',
                                     'Kernel mode setting']), 'error'


# Generated at 2022-06-13 02:23:59.406295
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import get_collector_instance

    # simple test for method collect of class SystemCapabilitiesFactCollector
    class AnsibleModuleMock(object):
        def get_bin_path(self, arg):
            return capsh_path

        def run_command(self, arg1, arg2):
            return '0', capsh_output, ''

    capsh_path = '/fake/path/capsh'
    capsh_output = 'Current: =ep\nSupported: =ep cap_net_admin,cap_net_raw+p'
    capsh_cmd = (capsh_path, "--print")
    capsh_enforced = 'False'
    capsh_caps = ['cap_net_admin', 'cap_net_raw+p']

# Generated at 2022-06-13 02:24:32.462596
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """
    Method collect should return a dict with system_capabilities and
    system_capabilities_enforced.
    """
    import os
    import sys
    assert sys.version_info >= (2, 7)
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import DictFactsPatch
    from ansible.module_utils.facts.collector import BaseFileReadBasedLegacyCollector
    import ansible.module_utils.facts.collectors.capabilities as cap_collector
    from ansible.module_utils.command import Command
    import ansible.module_utils.facts.system.capabilities_collector as cap_collector_fact_module
    import ansible.module_

# Generated at 2022-06-13 02:24:38.948805
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    vars = {}
    capsh_path = '/usr/bin/capsh'

# Generated at 2022-06-13 02:24:48.910912
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import tempfile

    module = None  # noqa: F821
    facts = {}

    fd, path = tempfile.mkstemp(prefix="ansible_facts_", suffix="_capsh")
    os.close(fd)

    test_file = path + "-system_capabilities_enforced"
    open(test_file, 'w').write("Current: =ep\n")
    test_collector = SystemCapabilitiesFactCollector()
    test_collector.collect(module, facts)
    assert facts['system_capabilities_enforced'] == 'False'

    test_file = path + "-system_capabilities_sys"
    open(test_file, 'w').write("Current: =ep\n")
    test_collector = SystemCapabilitiesFactCollector()

# Generated at 2022-06-13 02:24:55.924464
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    capsh_paths = ['/sbin/capsh','/usr/sbim/capsh','']

# Generated at 2022-06-13 02:25:06.205608
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Setup
    module = Mock(run_command=Mock(return_value=(0, 'Current: =ss cap_sys_admin,cap_net_admin=pe', '')),
                  get_bin_path=Mock(return_value='/bin/capsh'))
    collected_facts = {}
    collector = SystemCapabilitiesFactCollector(module)
    expected_collected_facts = {
        'system_capabilities_enforced': 'False',
        'system_capabilities': ['cap_sys_admin', 'cap_net_admin']
    }

    # Act
    actual_collected_facts = collector.collect(module, collected_facts)

    # Assert
    assert module.run_command.called
    assert expected_collected_facts == actual_collected_facts


# Generated at 2022-06-13 02:25:12.587466
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import get_collector_instance
    import ansible.module_utils.facts.system.caps as caps_mod
    # NOTE: can't mock ansible.module_utils.facts.system.caps.capsh_path, but we can't really mock this anyway
    # because it uses os.path.exists(capsh_path) in a while loop and I don't see a way to mock this.
    # if we want to mock it, we can mock ansible.module_utils.facts.system.caps.get_bin_path to return a path
    # that we can provide
    # we can mock the module.run_command to always return the same values
    # NOTE: added run_command() to caps_mod so we can mock it.

# Generated at 2022-06-13 02:25:23.184075
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import sys
    import os
    import tempfile
    import shutil
    import subprocess
    import mock


# Generated at 2022-06-13 02:25:23.982876
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    assert False, 'Not implemented yet'



# Generated at 2022-06-13 02:25:31.993495
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    collector = SystemCapabilitiesFactCollector()

# Generated at 2022-06-13 02:25:32.433780
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    assert True

# Generated at 2022-06-13 02:26:37.721020
# Unit test for method collect of class SystemCapabilitiesFactCollector

# Generated at 2022-06-13 02:26:38.215890
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:26:43.909939
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Build mock module and output
    module = 'module'
    out = """
Current: =ep
Bounding set =eip
Securebits: 00/0x0/1'b0
 secure-noroot: no (unlocked)
 secure-no-suid-fixup: no (unlocked)
 secure-keep-caps: no (unlocked)
uid=1002(ansible)
"""
    err = ''
    rc = 0

    class ModuleMock:
        def __init__(self, mod, opts):
            pass

        def get_bin_path(self, command, opt_dirs=[]):
            return 'capsh'

        def run_command(self, cmd, errors='surrogate_then_replace'):
            return rc, out, err

    # setup patches

# Generated at 2022-06-13 02:26:47.073375
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    with mock.patch("ansible.module_utils.facts.collector.BaseFactCollector.collect") as collect:
        SystemCapabilitiesFactCollector().collect()
        assert collect.called


# Generated at 2022-06-13 02:26:56.410534
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    # Test 1
    import tempfile
    import os
    import re
    import shutil
    from ansible.module_utils._text import to_bytes

    # create a test bin dir
    TEST_DIR = tempfile.mkdtemp()
    bin_dir = os.path.join(TEST_DIR, "bin")
    os.mkdir(bin_dir)
    os.mkdir(os.path.join(bin_dir, "x86_64-linux-gnu"))

    # create a test bin dir
    TEST_DIR = tempfile.mkdtemp()
    test_bin_dir = os.path.join(TEST_DIR, "test_bin")
    os.mkdir(test_bin_dir)

# Generated at 2022-06-13 02:27:01.740319
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    def _exec(module):
        return True, "Current: =ep", ""
    class MockModule:
        def __init__(self):
            self.run_command = _exec
            self.get_bin_path = lambda x: '/usr/bin/'

    collector = SystemCapabilitiesFactCollector()
    assert collector.collect(module=MockModule()) == {'system_capabilities': [], 'system_capabilities_enforced': 'False'}

# Generated at 2022-06-13 02:27:12.550998
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module_mock = MagicMock()
    module_mock.get_bin_path.return_value = 'capsh'

# Generated at 2022-06-13 02:27:17.570431
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.facts.system.capabilities import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts.utils import get_file_content

    module = AnsibleModule(
        argument_spec = dict(
            gather_subset=dict(type='list', elements='str'),
            filter=dict(type='str')
        )
    )

    test_files = ['/proc/sys/kernel/cap_last_cap']
    test_files_content = map(
      lambda x: get_file_content(x),
      test_files)

    capsh_path = module.get_bin_path('capsh')

# Generated at 2022-06-13 02:27:20.256568
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Arrange
    system_caps_facts = SystemCapabilitiesFactCollector()

    # Act
    system_caps_facts.collect()

    # Assert

# Generated at 2022-06-13 02:27:26.903082
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: 'import mock' will be in ansible 2.1/2.2 -akl
    import sys
    if sys.version_info[:2] < (2, 7):
        import unittest2 as unittest
    else:
        import unittest
    import mock

    class TestSystemCapabilitiesFactCollector(unittest.TestCase):
        # Mock class for module_utils.basic.AnsibleModule

        class AnsibleModule:
            class RunCommand:
                def __init__(self, module, bin_path, opts):
                    pass


# Generated at 2022-06-13 02:29:37.129314
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import os
    import tempfile

    cmd = 'capsh --print'
    capsh_out = '''
Capability LSM:
Current: =ep
Bounding set =ep
Securebits: 00/0x0/1'b0 secure-noroot,no-setuid-fixup
 secure-noroot,no-setuid-fixup
Secure mode:  rtnl_lock
'''
    tfile = tempfile.mkstemp()

# Generated at 2022-06-13 02:29:41.510520
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import sys
    import os
    if sys.version_info[0] < 3:
        from ansible.module_utils.facts import ansible_facts