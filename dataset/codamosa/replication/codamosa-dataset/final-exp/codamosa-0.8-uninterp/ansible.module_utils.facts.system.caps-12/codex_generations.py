

# Generated at 2022-06-13 02:19:43.303827
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    k = SystemCapabilitiesFactCollector()
    k.collect()


# Generated at 2022-06-13 02:19:51.751048
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    '''unit test for method collect of class SystemCapabilitiesFactCollector'''
    obj = SystemCapabilitiesFactCollector()
    out = obj.collect()
    if 'system_capabilities' in out:
        assert(type(out['system_capabilities_enforced']) is str)
        if 'False' in out['system_capabilities_enforced']:
            assert(type(out['system_capabilities']) is list)
    else:
        assert(out == {})

# Generated at 2022-06-13 02:19:52.500150
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:19:58.528878
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module_mock = Mock()
    module_mock.run_command.return_value = (0, CAPSH_OUT, '')
    module_mock.get_bin_path.return_value = '/usr/bin/capsh'

    facts_dict = SystemCapabilitiesFactCollector().collect(module_mock)
    assert facts_dict == {'system_capabilities' : ['cap_setuid', 'cap_setgid'], 'system_capabilities_enforced' : 'True'}


# Generated at 2022-06-13 02:20:08.713081
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    import ansible.module_utils.facts.collectors.system.caps as caps
    from ansible.module_utils.facts.collectors.system.caps import (
        SystemCapabilitiesFactCollector
    )
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock import MagicMock

    mock_module_obj = MagicMock()

    # Set up the mock bin path
    # The mock bin path will return the actual capsh binary path
    # on the test system
    mock_module_obj.get_bin_path.side_effect = \
        lambda x, required=False: x if x != 'capsh' else caps._find_capsh()


    # Set up the mock run_command
    # The mock run_command will return the output of capsh --print
    #

# Generated at 2022-06-13 02:20:11.141393
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    
    collector = SystemCapabilitiesFactCollector()
    assert collector.name == 'caps'
    assert collector._fact_ids == set(['system_capabilities',
                     'system_capabilities_enforced'])
    assert collector.collect() == {}

# Generated at 2022-06-13 02:20:19.766972
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import tempfile
    import os

    with tempfile.TemporaryDirectory() as tempdir:
        capsh_path = os.path.join(tempdir, "capsh")
        capsh_script = os.path.join(tempdir, "capsh_script")
        with open(capsh_script, 'w') as f:
            f.write("#!/bin/sh\n")
            f.write("echo 'Current: =ep'\n")
        os.chmod(capsh_script, 0o755)
        os.symlink(capsh_script, capsh_path)

        orig_module = None
        orig_run_command = None

# Generated at 2022-06-13 02:20:20.501215
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    assert 'get_bin_path' in dir(BaseFactCollector)

# Generated at 2022-06-13 02:20:31.127491
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    class MockModule(object):
        def __init__(self):
            self.params = {}
            self.run_command_capsh_output = ""

        def get_bin_path(self, cmd, opts=None, required=False):
            return cmd

        def run_command(self, cmd, errors='strict'):
            if self.run_command_capsh_output is not None:
                if isinstance(self.run_command_capsh_output, dict):
                    return self.run_command_capsh_output['exit_code'], self.run_command_capsh_output['stdout'], self.run_command_capsh_output['stderr']
                else:
                    return 0, self.run_command_capsh_output, ""

    module = MockModule()
    collector = SystemCap

# Generated at 2022-06-13 02:20:39.070388
# Unit test for method collect of class SystemCapabilitiesFactCollector

# Generated at 2022-06-13 02:20:50.322987
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Setup variables
    raw_env = {
        'PATH': '/usr/local/bin:/usr/bin:/bin',
        'HOME': '/root',
        'SHELL': '/bin/sh',
        'TERM': 'xterm'
    }

    # Setup module args
    raw_args = {
        'ANSIBLE_MODULE_ARGS': {
            'follow': 'no',
            'path': '/tmp',
            'password': '',
            'size': 0,
            'other': None,
            'something': 'nothing',
        }
    }

    # Create a new instance of the AnsibleModule mock class
    AnsibleModule = MockAnsibleModule(raw_env, raw_args)

    # Create a new instance of AnsibleModuleUtils for testing

# Generated at 2022-06-13 02:21:01.217519
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    result1 = { 'system_capabilities': [],
                'system_capabilities_enforced': 'False'}

# Generated at 2022-06-13 02:21:01.944226
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:21:08.593578
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: imports/add imports here, so as to test private method
    #     collect() and so avoid errors such as:
    #
    #     ImportError: Cannot import name 'SystemCapabilitiesFactCollector'
    #
    from ansible.module_utils.facts import collectors
    collectors.system_capabilities = SystemCapabilitiesFactCollector()
    module = object()
    x = SystemCapabilitiesFactCollector._collect(module)
    assert x == {'system_capabilities': None, 'system_capabilities_enforced': 'NA'  }

# Generated at 2022-06-13 02:21:18.032353
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.collector import get_all_collectors_to_execute
    from ansible.module_utils.facts.collector import get_all_facts

    class ModuleExit(Exception): pass

    class Module:
        def __init__(self):
            self._ansible_mock_found_bin_paths = {
                'capsh': '/usr/bin/capsh'
            }

        def get_bin_path(self, name, **kwargs):
            return self._ansible_mock_found_bin_paths[name]


# Generated at 2022-06-13 02:21:18.498482
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:21:24.828896
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # mock capabilities class and create instance
    # of SystemCapabilitiesFactCollector
    mock_class = 'ansible.module_utils.facts.system.capabilities.SystemCapabilitiesFactCollector'
    m_collector = mock_import_module(mock_class)
    mock_class_instance = m_collector()
    mock_method = 'ansible.module_utils.facts.collectors.capabilities.SystemCapabilitiesFactCollector.collect'

    def mock_run_command(binary, errors=None):
        if binary[0] == '/usr/bin/capsh':
            return 0, 'Current: =ep\n', ''
        else:
            return 1, '', ''

    # mock module to be returned by import_module
    m_module = mock_import_module('ansible.module_utils.basic')


# Generated at 2022-06-13 02:21:36.190389
# Unit test for method collect of class SystemCapabilitiesFactCollector

# Generated at 2022-06-13 02:21:46.882977
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """
    Unit test for method collect of class SystemCapabilitiesFactCollector.
    :return: None.
    """
    import mock
    import os
    import pytest
    import re
    mock_module = mock.Mock()
    mock_module.run_command.return_value = (0, "Current: = cap_setpcap,cap_setfcap+eip\n", '')
    mock_module.get_bin_path.return_value = "/usr/bin/capsh"
    mock_module.get_bin_path.return_value = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'capsh')
    fact_collector = SystemCapabilitiesFactCollector(mock_module)
    returned_facts = fact_collector.collect()

# Generated at 2022-06-13 02:21:53.584004
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import FactCollector
    # Create a fake ansible.module_utils.facts.module
    class FakeModule(object):
        def __init__(self):
            self.mock_module = {'rc': 0, 'out': 'Current: =ep', 'err': ''}

        def run_command(self, cmd, errors='surrogate_then_replace'):
            return (self.mock_module['rc'], self.mock_module['out'], self.mock_module['err'])

        def get_bin_path(self, cmd, required=False):
            return cmd

    fact_collector = FactCollector(None, None)
    # create a fake ansible.module_utils.facts.Module object
    fake_module = FakeModule()
    # set the

# Generated at 2022-06-13 02:22:05.346631
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    class TestModule:
        def get_bin_path(self, executable):
            if executable == 'capsh':
                return executable
        def run_command(self, cmd, errors='surrogate_then_replace'):
            assert cmd == ['capsh', '--print']
            return (0, 'Current: =ep', '')

    module = TestModule()
    sut = SystemCapabilitiesFactCollector()
    result = sut.collect(module)
    assert result == {'system_capabilities': [],
                      'system_capabilities_enforced': 'False'}

# Generated at 2022-06-13 02:22:06.039957
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    cpfc = SystemCapabilitiesFactCollector()
    assert cpfc.collect() == {}

# Generated at 2022-06-13 02:22:16.101103
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    output1 = """
Current: =ep
Bounding set =ep
Securebits: 00/0x0/1'b0
 secure-noroot: no (unlocked)
 secure-no-suid-fixup: no (unlocked)
 secure-keep-caps: no (unlocked)
uid=0(root)
gid=0(root)
groups=0(root),1(bin),2(daemon),3(sys),4(adm),6(disk),10(wheel)
"""

# Generated at 2022-06-13 02:22:17.968546
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    assert SystemCapabilitiesFactCollector().collect()
    assert SystemCapabilitiesFactCollector().collect()

# Generated at 2022-06-13 02:22:24.689233
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import did_collect_fact
    import collections
    import os
    import unittest
    from ansible.module_utils._text import to_text
    import time

    class AnsibleModuleFake(object):

        def __init__(self, *args, **kwargs):
            self.params = collections.defaultdict(str)
            self.run_command = self.get_bin_path = self.exit_json = self.fail_json = self.run_command = self.run_command
            self.VERSION = '2.9.9'

        def get_bin_path(self, name, **kwargs):
            return 'capsh'


# Generated at 2022-06-13 02:22:30.539436
# Unit test for method collect of class SystemCapabilitiesFactCollector

# Generated at 2022-06-13 02:22:37.461429
# Unit test for method collect of class SystemCapabilitiesFactCollector

# Generated at 2022-06-13 02:22:47.746285
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.collector import get_file_lines
    from ansible.module_utils.facts.collector import get_parser
    from ansible.module_utils.facts.collector import run_command
    import os

    class TestModule(object):

        @staticmethod
        def get_file_lines(*args, **kwargs):
            return get_file_lines(*args, **kwargs)  # module.run_command is a staticmethod

        @staticmethod
        def get_bin_path(*args, **kwargs):
            return '/bin/capsh'

        @staticmethod
        def run_command(*args, **kwargs):
            return run_command(*args, **kwargs)  # module.run

# Generated at 2022-06-13 02:22:56.804979
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import subprocess
    class MockModule():
        def __init__(self, params):
            self.params = params
        def get_bin_path(self, path):
            return 'capsh'
        def run_command(self, opts, errors=None):
            return 0, """"""
        def fail_json(self, *args, **kwargs):
            self.exit_args = args
            self.exit_kwargs = kwargs
            raise Exception('fail_json')
        def exit_json(self, **kwargs):
            self.exit_args = kwargs.get("changed")
            self.exit_kwargs = kwargs
            return True
        def add_path(self, *args, **kwargs):
            pass

# Generated at 2022-06-13 02:22:58.302542
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    ''' Test class facts_module.facts.SystemCapabilitiesFactCollector '''
    pass

# Generated at 2022-06-13 02:23:07.322360
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import collector

    m = MagicMock()
    m.run_command.return_value = 0, '', ''
    m.get_bin_path.return_value = 'capsh_path'

    sut = collector.get_collector('caps')
    res = sut.collect(m)

    assert 'system_capabilities_enforced' in res
    assert 'system_capabilities' in res


# Generated at 2022-06-13 02:23:14.402657
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import LeakyFactCollector
    from ansible.module_utils.facts.utils.capsh import CapshCollector
    from ansible.module_utils.facts.utils.capsh import Capsh
    from ansible.module_utils.facts.utils.capsh import CapshError
    from ansible.modules.system.capsh import main
    from ansible.module_utils.six import PY3


# Generated at 2022-06-13 02:23:15.015310
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:23:25.143957
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import _get_module_mock
    from ansible.module_utils.facts import Collector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils._text import to_bytes

    class FakeModule:
        def __init__(self):
            self.fail_json = lambda *args, **kwargs: None
        def get_bin_path(self, bin_path, **kwargs):
            if bin_path == 'capsh':
                return bin_path
            return None

# Generated at 2022-06-13 02:23:28.118821
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    data = SystemCapabilitiesFactCollector.collect()
    assert 'system_capabilities' in data
    assert isinstance(data['system_capabilities'], list)
    assert 'system_capabilities_enforced' in data

# Generated at 2022-06-13 02:23:37.391066
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Args:
    #  module: a MagicMock() object to mock the module
    # Returns:
    #  a dictionary containing the keys: system_capabilities,
    #                                     system_capabilities_enforced
    from ansible_collections.misc.not_a_real_collection.tests.unit.compat.mock import patch
    mock_module = patch.object(
        SystemCapabilitiesFactCollector,
        'get_module',
        return_value=None,
        autospec=True,
    )
    with mock_module as mock_module:
        collector = SystemCapabilitiesFactCollector(mock_module, None)
        assert collector.collect(mock_module, None) == {'system_capabilities': [],
                                                        'system_capabilities_enforced': False}
        mock_

# Generated at 2022-06-13 02:23:47.069421
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    # Create a test fixture for the SystemCapabilitiesFactCollector class
    class TestSystemCapabilitiesFactCollector(SystemCapabilitiesFactCollector):

        # Make method get_bin_path available for testing
        def get_bin_path(self, exe):
            if exe == 'capsh':
                return exe

        # Make method run_command available for testing
        def run_command(self, module_args, errors='surrogate_then_replace'):
            if 'print' in module_args:
                rc = 0
                out = 'Current: = ep'
                err = None

            return rc, out, err

    # Create a test instance of the TestSystemCapabilitiesFactCollector class
    test_instance = TestSystemCapabilitiesFactCollector()

    # Create a test ansible module
    # NOTE: module_args is optional

# Generated at 2022-06-13 02:23:53.329978
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import collector

    from ansible.module_utils.facts import ansible_collection
    from ansible.module_utils.facts.ansible_collection.plugins.module_utils.facts.collector import BaseFactCollector
    import types

    # Create a mock context
    context = {}

    # Create a ModuleMock module
    module = types.ModuleType('_ansible_module_mock')

    # Create a CapshMock module
    submodule = types.ModuleType('capsh')
    submodule.path = '/bin/capsh'
    submodule.output = "Current: =ep\n"
    submodule.stderr = "capsh: 0.1.42\n"
    submodule.rc = 0
    module.run_command = submodule


# Generated at 2022-06-13 02:24:00.605532
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    capsh_path = '/usr/bin/capsh'
    module = {}
    module['get_bin_path'] = lambda path: capsh_path
    module['run_command'] = lambda command, errors: (0, "Current: =ep\n", "")

    fact_collector = SystemCapabilitiesFactCollector()
    collected_facts = fact_collector.collect(module)

    assert 'system_capabilities' in collected_facts
    assert 'system_capabilities_enforced' in collected_facts

    assert collected_facts['system_capabilities'] == []
    assert collected_facts['system_capabilities_enforced'] == 'False'

# Generated at 2022-06-13 02:24:03.537214
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    test_instance = SystemCapabilitiesFactCollector()
    assert test_instance.collect() == dict(system_capabilities=None, system_capabilities_enforced=None)

# Generated at 2022-06-13 02:24:17.270854
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """ Unit test for SystemCapabilitiesFactCollector.collect """
    pass

# Generated at 2022-06-13 02:24:25.334261
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    module = MockModule({})
    collector = SystemCapabilitiesFactCollector()

    # Collect facts without enforced capabilities.

# Generated at 2022-06-13 02:24:33.928747
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import FactCollector

    module = Mock()
    module.get_bin_path.return_value = '/bin/capsh'
    module.run_command.return_value = 0, 'Current: =ep', ''

    fact_collector = FactCollector()
    fact_collector.collect_fact = Mock()

    collector = SystemCapabilitiesFactCollector(fact_collector)
    collector.collect(module, collected_facts=None)

    assert fact_collector.collect_fact.call_count == 2
    fact = fact_collector.collect_fact.call_args_list[0][0][1]
    assert fact.fact_name == 'system_capabilities'
    assert fact.fact_data is None
    assert fact.group == 'system'
    fact = fact_collect

# Generated at 2022-06-13 02:24:44.094384
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Collect facts about system capabilities.
    # Expected:
    #   - system_capabilities_enforced is set to False/True based on capsh
    #     output
    #   - system_capabilities is set to a list of capabilities, empty or
    #     based on capsh output

    from ansible.module_utils.facts.collectors.capabilities import SystemCapabilitiesFactCollector

    module = FakeModule()
    module.run_command = fake_run_command
    module.get_bin_path = fake_get_bin_path

    fact_collector = SystemCapabilitiesFactCollector(module)
    fact_collector.collect()

    assert module.terminal_facts['system_capabilities_enforced'] == 'False'

# Generated at 2022-06-13 02:24:52.813827
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """Unit test for method collect of class SystemCapabilitiesFactCollector"""
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.collector.system import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts.utils import AnsibleFactCollector
    from ansible.module_utils import basic

    # Test with a set of data that contains capsh output with capabilities enforced

# Generated at 2022-06-13 02:24:58.221845
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # given
    collector = SystemCapabilitiesFactCollector()
    module = create_ansible_module_mock()

# Generated at 2022-06-13 02:25:07.464025
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """ Unit test for method collect of class SystemCapabilitiesFactCollector """

# Generated at 2022-06-13 02:25:07.825555
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:25:12.035103
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: add patching to mock_module/mock_run_command -akl
    mock_module = {}

# Generated at 2022-06-13 02:25:17.880268
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import ansible.module_utils.facts.collector
    try:
        module = ansible.module_utils.facts.collector.BaseFactCollector.get_module()
        scf = SystemCapabilitiesFactCollector()
        assert scf.collect(module)['system_capabilities'] == []
    except AssertionError:
        print("assertion error")


# Generated at 2022-06-13 02:25:46.063039
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    fact_collector = SystemCapabilitiesFactCollector()
    assert fact_collector != None
    assert fact_collector.name == 'caps'
    assert fact_collector.collect != None
    assert fact_collector.collect_cap_shell != None

if __name__ == "__main__":
    test_SystemCapabilitiesFactCollector_collect()

# Generated at 2022-06-13 02:25:53.400435
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import mock
    import sys
    sys.modules['ansible.module_utils.facts.collector.ansible_local'] = mock.MagicMock()
    from ansible.module_utils.facts.collector.system_capabilities import SystemCapabilitiesFactCollector
    import ansible.module_utils.facts.collector.ansible_local
    module = ansible.module_utils.facts.collector.ansible_local
    capsh_path = '/bin/caps'
    module.get_bin_path.return_value = capsh_path

# Generated at 2022-06-13 02:26:04.064107
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collector import TestModule
    from ansible.module_utils.facts import Facts
    import sys

    facts = Facts(module_name='ansible.module_utils.facts',
                  collected_facts=dict(system='Linux'),
                  module_args=None,
                  )

    collector = Collector(collected_facts=dict(system='Linux'),
                          module_args=None,
                          facts=facts,
                          )

# Generated at 2022-06-13 02:26:10.766225
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = object()
    fact_collector = SystemCapabilitiesFactCollector()

    # command output to test all the 3 scenarios 
    data_sets = [
        ('Current: =ep', False, []),
        ('Current: = cap_chown,cap_dac_override+eip', True, ["cap_chown", "cap_dac_override"]),
        ('Error: Some error from capsh command', False, [])
    ] 

    for data in data_sets:
        fact_collector.execute_module = lambda *args, **kwargs: (0, data[0], '')
        fact_dict = fact_collector.collect(module=module)

# Generated at 2022-06-13 02:26:20.419603
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    class MockAnsibleModule(object):
        def get_bin_path(self, command, required=False):
            return 'capsh'


# Generated at 2022-06-13 02:26:24.991962
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import tempfile
    tmp_dir = tempfile.gettempdir()
    tmp_file = tmp_dir + '/tmp_ansible_caps'

    # System capabilities enforced with no capabilities
    with open(tmp_file, 'w') as f_p:
        f_p.write('Current: =ep')
    capsh_path = tmp_dir + '/capsh'
    with open(capsh_path, 'w') as f_p:
        f_p.write('#!/bin/bash\n' + 'cat ' + tmp_file)
    module = FakeAnsibleModule(capsh_path = capsh_path)
    collector = SystemCapabilitiesFactCollector(module=module)
    results = collector.collect()
    assert results['system_capabilities'] == []

# Generated at 2022-06-13 02:26:35.364020
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector

# Generated at 2022-06-13 02:26:42.174654
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import os
    import sys
    import unittest

    class SystemCapabilitiesFactCollectorTestCase(unittest.TestCase):
        module_name = 'ansible.module_utils.basic'

        module = None


# Generated at 2022-06-13 02:26:45.344765
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    # NOTE: Replace with mock and assert calls to collect()
    # NOTE: (see test_systemd.test_SystemdFactCollector_collect())
    # NOTE: -akl

    return True

# Generated at 2022-06-13 02:26:46.467049
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:28:00.118305
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.collector import get_collector_names
    from ansible.compat.tests.mock import patch

    module = patch("ansible.module_utils.facts.collector.AnsibleModule").__enter__()

    os.environ['PATH'] = '/bin/:/usr/bin/'
    os.environ['___CAP_EVIDENCE___'] = 'cap-evidence'

    module.run_command.return_value = (0, 'Current: = cap_setpcap+ep\n', '')

    collector = get_collector_instance

# Generated at 2022-06-13 02:28:05.532594
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import ansible.module_utils.facts.collector

    mock_module = ansible.module_utils.facts.collector.BaseFactCollector()
    mock_module.run_command = { 'rc': -1, 'out':'you are in active mode', 'err':'' }
    test_class = SystemCapabilitiesFactCollector()

    # call the method and compare results
    result = test_class.collect(mock_module)

    assert result is not None

# Generated at 2022-06-13 02:28:12.558227
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import ModuleFaked

    system_capabilities_fact_collector = SystemCapabilitiesFactCollector()
    capsh_path = '/usr/bin/capsh'

# Generated at 2022-06-13 02:28:22.800545
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible_collections.ansible.community.plugins.module_utils.facts import collector


# Generated at 2022-06-13 02:28:23.273353
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:28:32.496001
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import Facts
    from ansible.module_utils.facts.collectors.system import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts.collectors.system.capabilities import get_caps_data

    non_priv_caps_data = {'system_capabilities_enforced': 'True', 'system_capabilities': ['cap_dac_override', 'cap_net_raw']}
    priv_caps_data = {'system_capabilities_enforced': 'True', 'system_capabilities': ['cap_dac_read_search', 'cap_ipc_lock', 'cap_net_bind_service', 'cap_sys_chroot', 'cap_sys_ptrace', 'cap_sys_tty_config']}


# Generated at 2022-06-13 02:28:33.136877
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:28:41.275407
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule
    import ansible.module_utils.facts.system.caps as caps

    module = AnsibleModule()

    BaseFactCollector._module = module  # pylint: disable=protected-access
    SystemCapabilitiesFactCollector._module = module  # pylint: disable=protected-access


# Generated at 2022-06-13 02:28:44.456885
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    class MockModule(object):
        def __init__(self):
            self.run_command = lambda command, err_to_info: (0, command[1], '')
            self.get_bin_path = lambda command: command
    obj = SystemCapabilitiesFactCollector()
    obj.collect(MockModule())
    assert obj.collect(MockModule()).keys().sort() == [
        'system_capabilities',
        'system_capabilities_enforced'
    ]

# Generated at 2022-06-13 02:28:48.853083
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import (
        BaseFactCollector
    )

    print(
"""
---------------------------------------------------------------------------
Running unit test for method 'SystemCapabilitiesFactCollector.collect'
---------------------------------------------------------------------------
""")

    from ansible_collections.notstdlib.moveitallout.tests.unit.compat import unittest
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock import MagicMock, patch

    class TestSystemCapabilitiesFactCollector(unittest.TestCase):

        def setUp(self):
            self.mock_module = MagicMock()
            self.mock_basefactclass = MagicMock(spec=BaseFactCollector)