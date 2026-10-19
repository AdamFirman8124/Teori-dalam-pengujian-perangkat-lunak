

# Generated at 2022-06-13 02:19:53.618441
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    collector = SystemCapabilitiesFactCollector()

    collected_facts = {}

# Generated at 2022-06-13 02:19:54.144510
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:20:04.573767
# Unit test for method collect of class SystemCapabilitiesFactCollector

# Generated at 2022-06-13 02:20:06.954282
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    mock = MockSystemCapabilitiesFactCollector()
    assert mock.collect() == {
        'system_capabilities_enforced': 'NA',
        'system_capabilities': []
    }

# Generated at 2022-06-13 02:20:13.684854
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import mock
    import os
    import shutil
    import tempfile
    caps_test_path = os.path.join(os.path.dirname(__file__), 'test_SystemCapabilitiesFactCollector_collect')
    capsh_test_path = os.path.join(caps_test_path, 'capsh')

# Generated at 2022-06-13 02:20:18.712184
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    class MockModule:
        def __init__(self, out):
            self.output = out
        def get_bin_path(self, bin):
            return bin
        def run_command(self, cmd, errors):
            return(0, self.output, "")

    test_output = "Current: =ep"
    test_data = MockModule(out=test_output)

    test_collector = SystemCapabilitiesFactCollector()
    test_facts = test_collector.collect(test_data, None)

    assert test_facts['system_capabilities_enforced'] == 'False'
    assert test_facts['system_capabilities'] == []

    test_output = "Current: =ep cap_sys_boot"
    test_data = MockModule(out=test_output)

    test_collector = SystemCap

# Generated at 2022-06-13 02:20:25.611482
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts import BaseFactCollector
    from ansible.module_utils._text import to_bytes


# Generated at 2022-06-13 02:20:36.538406
# Unit test for method collect of class SystemCapabilitiesFactCollector

# Generated at 2022-06-13 02:20:47.857566
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    sut = SystemCapabilitiesFactCollector()

# Generated at 2022-06-13 02:20:58.534755
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import ansible.module_utils.facts.collector
    from ansible.module_utils.facts.collector import BaseFactCollector

    with open('./test/unittest/test_capsh_output', 'r') as capsh_output:
        capsh_output = ''.join(capsh_output.readlines())

    test_module = ansible.module_utils.facts.collector.get_module(None)
    test_module.run_command = lambda command, **kwargs: (0, capsh_output, '')

    test_collector = SystemCapabilitiesFactCollector()
    result = test_collector.collect(test_module)

    assert isinstance(result, dict)
    assert isinstance(result.get('system_capabilities'), list)

# Generated at 2022-06-13 02:21:04.826782
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # return dict - empty when no module
    collector = SystemCapabilitiesFactCollector()
    assert collector.collect() == {}
    assert collector.collect(module=None) == {}

    # return dict - empty when 

# Generated at 2022-06-13 02:21:12.065187
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # stubs
    class MockModule():
        def __init__(self):
            self.run_command_results = [0]
            self.run_command_rc_map = {0: (0, "Current: =ep", ""),
                                       1: ("", "", "")}
            self.run_command_output_map = {0: "Current: =ep",
                                           1: ""}

        def get_bin_path(self, capsh_path, required=False):
            return capsh_path

        def run_command(self, cmd, errors='surrogate_then_replace'):
            return self.run_command_rc_map[self.run_command_results.pop(0)], self.run_command_output_map[self.run_command_results[0]]

    module = Mock

# Generated at 2022-06-13 02:21:17.417569
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # test module
    module = type('FakeModule', (object,), {
                    'run_command': run_command,
                    'get_bin_path': get_bin_path})
    # create object
    caps = SystemCapabilitiesFactCollector()
    # run collect
    result = caps.collect(module)
    # test result
    assert isinstance(result, dict)
    assert result == {
        'system_capabilities_enforced': 'True',
        'system_capabilities': ['cap_sys_admin']
    }


# Generated at 2022-06-13 02:21:24.058000
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """ test_SystemCapabilitiesFactCollector_collect()
    Tests the collect() method of the SystemCapabilitiesFactCollector class
    """
    # a basic 'no capability' capsh output

# Generated at 2022-06-13 02:21:35.985143
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import FakeModule
    from ansible.module_utils.facts.collector import FakeCollector
    module = FakeModule({'capsh': '/bin/capsh'})
    fact_collector = FakeCollector({'system_capabilities': 'cap_chown, cap_dac_override, cap_fowner, cap_fsetid, cap_kill, cap_setgid, cap_setuid, cap_setpcap, cap_net_bind_service, cap_net_raw, cap_sys_chroot, cap_mknod, cap_audit_write, cap_setfcap+ep'})
    class_under_test = SystemCapabilitiesFactCollector(module=module, fact_collector=fact_collector)

# Generated at 2022-06-13 02:21:46.724166
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import mock
    import sys
    if sys.version_info[0] < 3:
        import __builtin__ as builtins
    else:
        import builtins
    import ansible.module_utils.facts.collector
    from ansible.module_utils.facts import default_collectors

    class MockModule(object):
        def __init__(self, arg):
            self.run_command = arg

        def get_bin_path(self, arg):
            return arg


# Generated at 2022-06-13 02:21:53.483493
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    class MockOSFile:
        def __eq__(self,value):
            if value == '/usr/bin/capsh':
                return True
            return False

    class MockModule:
        def get_bin_path(self, value):
            if value == 'capsh':
                return MockOSFile()

        def run_command(self, value, errors):
            if value == ['/usr/bin/capsh', '--print']:
                return 0, 'Current: = cap_net_admin,cap_net_raw+eip', ''

    mock_module = MockModule()
    fact_collector = SystemCapabilitiesFactCollector()
    result = fact_collector.collect(mock_module)
    assert result['system_capabilities_enforced'] == 'True'

# Generated at 2022-06-13 02:21:55.661254
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    m = AnsibleModule()
    c = SystemCapabilitiesFactCollector()
    if c.capsh_path:
        c.collect(m)

# Generated at 2022-06-13 02:22:02.844340
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    from ansible.module_utils import basic
    from ansible.module_utils.facts import collector


# Generated at 2022-06-13 02:22:13.200522
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import sys
    import os
    import platform
    import pytest

    if sys.version_info >= (2, 7):
        import unittest
    else:
        import unittest2 as unittest

    from ansible.module_utils.facts.collector import BaseFactCollector

    class TestSystemCapabilitiesFactCollector(unittest.TestCase):
        def setUp(self):
            self.test_SystemCapabilitiesFactCollector = SystemCapabilitiesFactCollector()
            self.test_SystemCapabilitiesFactCollector.collect()

        def test_instance(self):
            """Ensure SystemCapabilitiesFactCollector is an instance of BaseFactCollector."""
            self.assertIsInstance(self.test_SystemCapabilitiesFactCollector,
                                  BaseFactCollector)


# Generated at 2022-06-13 02:22:22.440057
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    obj = SystemCapabilitiesFactCollector()
    facts_dict = obj.collect()
    key = 'system_capabilities'
    assert key in facts_dict
    assert isinstance(facts_dict[key], list)
    assert len(facts_dict[key]) > 0

    key = 'system_capabilities_enforced'
    assert key in facts_dict
    assert isinstance(facts_dict[key], str)

# Generated at 2022-06-13 02:22:28.387072
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: test requires capsh to be installed on test platform
    import stat
    import subprocess

    def shell(cmd):
        res = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        out, err = res.communicate()
        exitcode = res.returncode
        return exitcode, out, err

    def get_capsh_path():
        # NOTE: assume capsh is in standard path -akl
        capsh_path = '/bin/capsh'
        if not capsh_path:
            return capsh_path
        if not (stat.S_IXUSR & os.stat(capsh_path)[stat.ST_MODE]):
            return None
        return capsh_path


# Generated at 2022-06-13 02:22:33.604079
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    m = mock.Mock()
    m.run_command = mock.Mock(return_value=(0, "", ""))
    m.get_bin_path = mock.Mock(return_value="")
    module = m

    c = SystemCapabilitiesFactCollector()
    out_dict = c.collect(m)
    assert out_dict['system_capabilities_enforced'] == 'NA'
    assert out_dict['system_capabilities'] == []

    m.run_command = mock.Mock(return_value=(0, "Current: =eip\n", ""))
    m.get_bin_path = mock.Mock(return_value="")
    module = m

    c = SystemCapabilitiesFactCollector()
    out_dict = c.collect(m)

# Generated at 2022-06-13 02:22:38.202378
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """
    unit test for method collect of class SystemCapabilitiesFactCollector
    """
    module = object()
    caps_fact_collector = SystemCapabilitiesFactCollector()
    facts_dict = caps_fact_collector.collect(module=module)
    assert facts_dict == {'system_capabilities_enforced': 'NA',
                          'system_capabilities': []}

# Generated at 2022-06-13 02:22:43.562062
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from mock import MagicMock
    from ansible.module_utils.facts import get_collector_instance

    module = MagicMock()
    module.run_command.return_value = 25, 'foo', 'bar'
    module.get_bin_path.return_value = False
    capsh_collector = get_collector_instance('caps')

    assert not capsh_collector.collect(module)['system_capabilities']

# Generated at 2022-06-13 02:22:54.148174
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Arrange
    module = mock.MagicMock()
    modulestr = 'ansible.module_utils.basic.AnsibleModule'
    module.get_bin_path = mock.MagicMock(return_value='/usr/bin/capsh')
    module.run_command = mock.MagicMock(return_value=(0, 'Current: =ep\nBounding set =cap_sys_chroot,cap_net_raw+eip', ''))
    module.__name__ = modulestr
    collected_facts = {}

    # Act
    sys_caps = SystemCapabilitiesFactCollector(module=module)
    actual = sys_caps.collect(module=module, collected_facts=collected_facts)

    # Assert
    assert actual['system_capabilities_enforced'] == 'False'


# Generated at 2022-06-13 02:23:05.474074
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Pass a module that is not really used - only its methods are used.
    module = ModuleStub()
    module.run_command = mock_run_command
    module.get_bin_path = mock_get_bin_path

    cc = SystemCapabilitiesFactCollector(module=module)

    collected_facts = cc.collect()

# Generated at 2022-06-13 02:23:13.323955
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    fact_collector = SystemCapabilitiesFactCollector()

    # NOTE: setup collect_io, mock module and mock the run of 'capsh' command
    # -> mock_out, mock_err, mock_rc

# Generated at 2022-06-13 02:23:23.555684
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.system.capabilities import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils import basic
    facts = BaseFactCollector()
    facts.collectors = [ SystemCapabilitiesFactCollector() ]
    module = basic.AnsibleModule(argument_spec={})
    module.run_command = lambda *args: (0, 'Current: =ep', '')
    f = facts.collect(module=module, collected_facts=None)
    assert 'system_capabilities' in f.keys()
    assert 'system_capabilities_enforced' in f.keys()
    assert f['system_capabilities_enforced'] == 'False'
    assert f['system_capabilities'] == []
    module.run

# Generated at 2022-06-13 02:23:34.228920
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    from ansible.module_utils.facts.collector import CollectorException
    from ansible.module_utils.facts.parsers.capabilities import parse_caps_data

    def get_caps_data(path):
        return """Current: =ep
CapInh:    =
CapPrm:    =
CapEff:    =
CapBnd:    =
CapAmb:    =
""", "", "", 0


# Generated at 2022-06-13 02:23:47.132065
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    fact_collector = SystemCapabilitiesFactCollector()

# Generated at 2022-06-13 02:23:47.627769
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:23:53.597734
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import FactsCollector
    from ansible.module_utils.facts.system.caps import SystemCapabilitiesFactCollector


# Generated at 2022-06-13 02:24:02.133423
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: pre-mock test for now until we can develop
    # a proper mock for this module.  Currently fails
    # because AnsibleModule is not defined.
    return
    from ansible.module_utils.facts import collector
    import os
    import sys
    import tempfile
    temp_fd, temp_path = tempfile.mkstemp()
    os.close(temp_fd)
    # temp_fd, temp_path = tempfile.mkstemp()
    collector.add_collector(SystemCapabilitiesFactCollector())

    os.environ['PATH'] = os.pathsep.join([os.path.dirname(__file__), os.environ.get('PATH', '')])

# Generated at 2022-06-13 02:24:09.343253
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import json

    from ansible.module_utils.facts.collectors.system.caps import SystemCapabilitiesFactCollector

    test_class = SystemCapabilitiesFactCollector('')
    assert test_class

    test_class.module = MockModule()
    test_class.module.run_command.return_value = [0, '', '']

    test_class.collect()
    test_class.module.get_bin_path.assert_called_with('capsh')

    test_class.module.run_command.return_value = [0, 'Current: =ep\nBounding set =', '']
    test_class.collect()

    out = test_class.collect()
    assert out['system_capabilities_enforced'] == 'False'
    assert out['system_capabilities'] == []

    test_class

# Generated at 2022-06-13 02:24:21.062662
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: extend as needed
    class MockModule():
        def get_bin_path(self, _):
            return "/capsh"


# Generated at 2022-06-13 02:24:30.004321
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import FactsCollector
    import sys
    import os

    # create a dummy module and call it with empty parameters
    module = ansible_facts._create_module()

    module.get_bin_path = lambda *args: '{}/../../bin/capsh'.format(os.path.dirname(sys.argv[0]))

    # create a dummy facts_collector with the current one and call it to collect the facts
    facts_collector = FactsCollector()
    facts_collector.collectors = [SystemCapabilitiesFactCollector()]
    facts_collector.collect(module=module)

    # get the collected facts

# Generated at 2022-06-13 02:24:39.540507
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = Mock()
    fact = Mock()
    fact._fact_ids = {'system_capabilities', 'system_capabilities_enforced'}
    module.get_bin_path.return_value = '/bin/capsh'

# Generated at 2022-06-13 02:24:44.079325
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    SystemCapabilitiesFactCollector._platform_fact_class = None
    module = MockModule()

    bin_path_success_mock = Mock(return_value='/bin/capsh')

# Generated at 2022-06-13 02:24:52.845463
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """ Unit test for method collect of class SystemCapabilitiesFactCollector
        (module_utils/facts/system/caps.py)

        Method collect returns the system_capabilities and
        system_capabilities_enforced, when system has a capsh.
    """
    class MockModule():
        def get_bin_path(self, name, *args, **kwargs):
            return '/bin/capsh'
        def run_command(self, cmd, *args, **kwargs):
            return 0, 'Current: =ep', ''
    system_capabilities_fact_collector = SystemCapabilitiesFactCollector()
    system_capabilities = system_capabilities_fact_collector.collect(MockModule())
    assert system_capabilities['system_capabilities'] == []
    assert system_capabilities['system_capabilities_enforced']

# Generated at 2022-06-13 02:25:25.312873
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.system.caps import SystemCapabilitiesFactCollector


# Generated at 2022-06-13 02:25:32.948762
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import os
    import pytest

    class MockModule(object):
        def get_bin_path(self, *args, **kwargs):
            if args[0] == 'capsh':
                return args[0]
            raise Exception(args[0])

        def run_command(self, *args, **kwargs):
            if args[0][1] == '--print':
                return (0, '''Current: =ep
Possible: =ep
Bounding set =ep
Securebits: 00/0x0/1'b0 secure-noroot, secure-no-suid
 secure-no-cap ambient-caps=-ep
CapEff: =ep
CapInh: 
CapPrm: 
CapAmb: 
CapBnd: =ep''', '')
            raise Exception(args[0][1])



# Generated at 2022-06-13 02:25:43.870116
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import sys
    if sys.version_info[0] == 2:
        from mock import Mock
        from StringIO import StringIO
    else:
        from unittest.mock import Mock
        from io import StringIO

    module = Mock()
    module.get_bin_path.return_value = '/bin/capsh'
    module.run_command().rc = 0

# Generated at 2022-06-13 02:25:51.768597
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utitlities._text import to_bytes
    from collections import namedtuple

    class FakeModule(object):
        def __init__(self, rc, out, err):
            self.rc, self.out, self.err = rc, out, err

        def get_bin_path(self, _, **kwargs):
            return None

        def run_command(self, _, **kwargs):
            return self.rc, self.out, self.err

    def run_command(self, _, **kwargs):
        return 0, to_bytes(capsh_out), b''

    fake_module = FakeModule(0, '', '')

# Generated at 2022-06-13 02:26:02.058089
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector.system.capabilities import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts.collector import BaseFactCollector

    # Test collect method
    SystemCapabilitiesFactCollector = SystemCapabilitiesFactCollector()
    BaseFactCollector.collectors.append(SystemCapabilitiesFactCollector)

    # Test collect method
    facts_dict = BaseFactCollector.collect(module=None)
    assert 'system_capabilities_enforced' in facts_dict
    assert 'system_capabilities' in facts_dict

    # Test collect method
    # NOTE: -> get_caps_data()/parse_caps_data() for easier mocking -akl

    # Test collect method
    facts_dict = BaseFactCollector.collect(module=None)

# Generated at 2022-06-13 02:26:09.731554
# Unit test for method collect of class SystemCapabilitiesFactCollector

# Generated at 2022-06-13 02:26:19.557116
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import FactsCollector
    # this import required to fix  pytest imports issues
    from ansible.module_utils.facts.system.caps import SystemCapabilitiesFactCollector
    import mock
    import os

    capsh_path = '/usr/bin/capsh'
    # Mock os.path.exists
    mock_path_exists = mock.Mock()
    mock_path_exists.return_value = True
    # Mock run_command
    mock_run_command = mock.Mock()

# Generated at 2022-06-13 02:26:21.642870
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    fake_module = None
    fake_result = None
    collector = SystemCapabilitiesFactCollector()
    assert collector.collect(fake_module, fake_result) == {}

# Generated at 2022-06-13 02:26:31.096987
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    '''
    Test method collect of class SystemCapabilitiesFactCollector
    '''
    from ansible.module_utils.facts.collector import get_collector_class
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.system.caps import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts import collect as test_collect
    from ansible.module_utils.facts import AnsibleFactCollector
    from ansible.module_utils.facts.system.caps import get_caps_data
    import mock
    import sys

    CollectClass = get_collector_class('caps')

# Generated at 2022-06-13 02:26:32.999505
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    results = SystemCapabilitiesFactCollector().collect()
    assert isinstance(results, dict), results



# Generated at 2022-06-13 02:27:48.819486
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import Module

    module = Module()
    module.get_bin_path = lambda x: '/bin/capsh'
    module.run_command = lambda cmd, errors: (0, 'Current: =ep', '')

    # test with current cap:=ep
    collector = SystemCapabilitiesFactCollector(module=module)
    facts = collector.collect()
    assert facts['system_capabilities_enforced'] == 'False'
    assert facts['system_capabilities'] == []

    # test with current cap:=
    module = Module()
    module.get_bin_path = lambda x: '/bin/capsh'
    module.run_command = lambda cmd, errors: (0, 'Current: = cap_chown,cap_dac_override', '')


# Generated at 2022-06-13 02:27:53.546260
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible_collections.ansible.community.plugins.module_utils.facts.collectors.system.capabilities \
        import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts.collector import BaseFactCollector

    caps_collector = SystemCapabilitiesFactCollector()
    assert isinstance(caps_collector, SystemCapabilitiesFactCollector)
    assert isinstance(caps_collector, BaseFactCollector)
    assert caps_collector._fact_ids == {'system_capabilities', 'system_capabilities_enforced'}
    assert caps_collector.name == 'caps'

# Generated at 2022-06-13 02:28:02.269193
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    '''
    When the return of `capsh --print` is:
      0        = cap_sys_chroot,cap_sys_admin+ep
    Current:    =ep
    Bounding set =cap_sys_chroot,cap_sys_admin
    Securebits: 00/0x0/1'b0
    secure-noroot: no (unlocked)
    secure-no-suid-fixup: no (unlocked)
    secure-keep-caps: no (unlocked)
    uid=0(root)
    gid=0(root)
    groups=0(root)

    the fact system_capabilities_enforced is False
    '''
    from ansible.module_utils.facts.collectors.system.system_capabilities import SystemCapabilitiesFactCollector
    import sys


# Generated at 2022-06-13 02:28:10.845348
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = AnsibleModule(
        argument_spec = dict(
            gather_subset=dict(default=['!all'], type='list')
        )
    )
    results = dict(
        system_capabilities_enforced = True,
        system_capabilities = ['chown', 'dac_override', 'fowner', 'fsetid', 'kill', 'setgid', 'setuid', 'setpcap', 'net_bind_service', 'net_raw', 'sys_chroot', 'mknod', 'audit_write', 'setfcap'],
    )

    capsh_path = module.get_bin_path('capsh')
    expected_ansible_module_results = dict(
        ansible_facts=results,
        changed=False
    )


# Generated at 2022-06-13 02:28:12.142574
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    SystemCapabilitiesFactCollector().collect()

# Generated at 2022-06-13 02:28:22.328581
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # try some condition returns True
    def get_bin_path(name):
        return '/usr/bin/capsh'
    class _module:
        def __init__(self):
            self.run_command = run_command
            self.get_bin_path = get_bin_path
    def run_command(cmd, errors='surrogate_then_replace'):
        return 0, 'Current: =ep', ''
    
    module = _module()
    sut = SystemCapabilitiesFactCollector()
    result = sut.collect(module)
    assert result['system_capabilities_enforced'] == 'False'
    assert result['system_capabilities'] == []

    # try some condition returns False
    def get_bin_path(name):
        return None

# Generated at 2022-06-13 02:28:22.836874
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:28:32.168401
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module_mock = Mock(get_bin_path=Mock(return_value='/bin/capsh'))

# Generated at 2022-06-13 02:28:40.718467
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    '''Unit test to test capsh collection'''
    module = MockModule({'get_bin_path': lambda x: '/usr/bin/capsh'})

# Generated at 2022-06-13 02:28:45.784738
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import collector

    module = AnsibleModuleMock(
        params={}
    )

    capsh_path = module.get_bin_path('capsh') # using binary path to detect platform
    my_collector = collector.get_collector('capabilities')

    if capsh_path: # NOTE: if-else capsh_path
        rc, out, err = module.run_command([capsh_path, "--print"], errors='surrogate_then_replace')
        enforced_caps = []
        enforced = 'NA'
        for line in out.splitlines():
            if len(line) < 1:
                continue
            if line.startswith('Current:'):
                if line.split(':')[1].strip() == '=ep':
                    enforced = 'False'
