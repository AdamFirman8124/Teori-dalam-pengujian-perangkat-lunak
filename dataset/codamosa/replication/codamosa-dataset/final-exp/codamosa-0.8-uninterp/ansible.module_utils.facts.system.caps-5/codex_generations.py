

# Generated at 2022-06-13 02:19:55.067973
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Set up
    import mock
    import ansible.module_utils.facts.collector
    mod_mock = mock.Mock(name="ansible.module_utils.facts.collector.Module", spec=ansible.module_utils.facts.collector.Module)

    module_import_mock = mock.Mock(name="module_import")
    mod_mock.get_bin_path = module_import_mock
    module_import_mock.return_value = 'fake_path'

    module_run_mock = mock.Mock(name='module_run')
    mod_mock.run_command = module_run_mock


# Generated at 2022-06-13 02:20:05.730384
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """ Unit test for method collect of class SystemCapabilitiesFactCollector
       The method 'collect' returns capabilities of the module/system when executed.
    """
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils._text import to_bytes

    class FakeModule(object):
        def __init__(self):
            self.params = dict()
            self.params['gather_subset'] = ["all"]
            self.params['gather_timeout'] = 10
            self.params['filter'] = '*'

        def get_bin_path(self, binary):
            return '/usr/bin/capsh'


# Generated at 2022-06-13 02:20:12.999499
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = MockAnsibleModule()
    collected_facts = {'os': {}}
    mocked_capsh_path = '/bin/capsh'

# Generated at 2022-06-13 02:20:20.904399
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = None
    fact_collector = SystemCapabilitiesFactCollector()

    # Default case
    expected = {
                'system_capabilities': [],
                'system_capabilities_enforced': 'NA'
                }
    result = fact_collector.collect(module)
    assert result == expected

    # Test with enforced capabilities
    expected = {
                'system_capabilities': ['cap_chown','cap_dac_override','cap_fowner','cap_fsetid','cap_kill','cap_setgid','cap_setuid'],
                'system_capabilities_enforced': 'True'
                }
    result = fact_collector.collect(module)
    assert result == expected

    # Test without enforced capabilities

# Generated at 2022-06-13 02:20:29.593252
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: Should add tests, but don't know of a way to 'mock' run_command -akl
    # If a method 'get_caps_data()' is added, that could be mocked.
    # Until then, just run collect and make sure no errors -akl

    module = ansible.module_utils.facts.collector.BaseFactCollector()
    collected_facts = None
    collector = SystemCapabilitiesFactCollector()
    collector.collect(module, collected_facts)
    assert Collector.system_capabilities_enforced == 'NA'

# Generated at 2022-06-13 02:20:30.176504
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    assert 1 == 1

# Generated at 2022-06-13 02:20:30.784672
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    assert collect() is None

# Generated at 2022-06-13 02:20:38.890014
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import get_collector_instance

    module = FakeAnsibleModule()

# Generated at 2022-06-13 02:20:40.327866
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: Skip these tests because they require `capsh` being available -akl
    pass

# Generated at 2022-06-13 02:20:49.586049
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = None
    if module is None:
        module = AnsibleModule(argument_spec={})
    capsh_path = module.get_bin_path('capsh')

# Generated at 2022-06-13 02:21:03.649189
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    '''Test the method "collect" of the class SystemCapabilitiesFactCollector'''
    from ansible.module_utils.facts.collector import BaseFactCollector

    class module_mock:
        '''Mocking class for AnsibleModule'''
        def get_bin_path(self, path):
            '''Mocking method get_bin_path of AnsibleModule class'''
            return path

        def run_command(self, command, errors):
            '''Mocking method run_command of AnsibleModule class'''
            out = 'Current:\nCapInh: =ep\nCapPrm: =ep\nCapEff: =ep\nCapBnd: =ep\nCapAmb: =ep\n'
            return (0, out, '')

    module_mock_obj = module_mock()


# Generated at 2022-06-13 02:21:11.517350
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import os
    import tempfile
    import shutil
    import subprocess
    import filecmp

    # Create a temporary directory
    tmpdir = tempfile.mkdtemp()

    capsh_fname = os.path.join(tmpdir, 'capsh')
    with open(capsh_fname, 'w') as fh:
        fh.write('#!/bin/bash\n')
        fh.write('echo "Current: =ep"\n')
        fh.write('echo "CapInh:   ="\n')
        fh.write('echo "CapPrm:   ="\n')
        fh.write('echo "CapEff:   ="\n')
        fh.write('echo "CapBnd:   ="\n')

# Generated at 2022-06-13 02:21:19.026060
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import sys
    import unittest
    from types import ModuleType

    class StubModule(ModuleType):
        def __init__(self, *args):
            pass

    # Verify it ignores failures from itself
    module = StubModule('ansible.module_utils.facts.system.caps')
    module.run_command = create_run_command(code=1)
    module.get_bin_path = create_get_bin_path()
    collector = SystemCapabilitiesFactCollector()

    # Verify it gets capsh path via get_bin_path
    module.run_command = create_run_command()
    module.get_bin_path = create_get_bin_path(code=1)
    collector = SystemCapabilitiesFactCollector()
    assert collector.collect(module) == {}

    # Verify it gets output from capsh

# Generated at 2022-06-13 02:21:19.921745
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    assert 'system_capabilities_enforced' in SystemCapabilitiesFactCollector().collect().keys()

# Generated at 2022-06-13 02:21:25.697719
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    print('test')
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.system.caps import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts.system.caps import parse_caps_data


# Generated at 2022-06-13 02:21:36.824222
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import CapabilityCollector, BaseFactCollector
    from ansible.module_utils.facts.collector.system.capabilities import SystemCapabilitiesFactCollector

    mock_module = CapabilityCollector()
    mock_module.get_bin_path = lambda x: '/usr/bin/capsh'

# Generated at 2022-06-13 02:21:47.484547
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """ Test the collect function of the class SystemCapabilitiesFactCollector """

    # Mock module
    module = Mock()
    module.run_command = MagicMock()
    module.run_command.return_value = (0, 'Current: =ep', '')

    # Create collector
    collector = SystemCapabilitiesFactCollector()
    # Collect fact
    fact = collector.collect(module=module, collected_facts=None)

    assert fact['system_capabilities_enforced'] == 'False'
    assert fact['system_capabilities'] == []


# Generated at 2022-06-13 02:21:53.936251
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import get_collector_instance

    capabilities_fact_collector = get_collector_instance('system_capabilities')


# Generated at 2022-06-13 02:22:01.540070
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    # Portion of real output from capsh --print on CentOS 5
    fake_capsoutput = """
Current: =ep
Bounding set =ep
Securebits: 00/0x0/1'b0
secure-noroot: no (unlocked)
secure-no-suid-fixup: no (unlocked)
secure-keep-caps: no (unlocked)
uid=0(root)
gid=0(root)
groups=0(root),1(bin),2(daemon),3(sys),4(adm),6(disk),10(wheel)
CapInh: 0000000000000000
CapPrm: 0000000000000000
CapEff: 0000000000000000
CapBnd: 0000003fffffffff
CapAmb: 0000000000000000
"""

    # Portion of real output from capsh --print on CentOS 7

# Generated at 2022-06-13 02:22:06.176073
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collectors import get_collector_instance
    from ansible.module_utils.facts.collectors.system import SystemCapabilitiesFactCollector

    test_collector = get_collector_instance(SystemCapabilitiesFactCollector)
    # NOTE: below is needed 'cause module_utils.facts caches collector results
    Collector.set_collectors([])
    test_collector.collect()
    assert 'system_capabilities' in test_collector.fact_ids()
    assert 'system_capabilities_enforced' in test_collector.fact_ids()

# Generated at 2022-06-13 02:22:23.225442
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    '''
    Run method collect of class SystemCapabilitiesFactCollector under various
    scenarios. These are not actually tests, but rather proof-of-concepts of how
    the tests would be structured. Actual tests could be implemented by calling
    this module like so:
      python -m testtools.run module_utils.basic.test_SystemCapabilitiesFactCollector
    '''

    # Use mock import to simulate a lack of 'capsh' binary
    from mock import Mock
    fact_collector = SystemCapabilitiesFactCollector()
    modules = []
    modules.append(Mock(name='module', run_command=Mock(return_value=(1, '', ''))))
    facts = {}
    for mod in modules:
        facts.update(fact_collector.collect(module=mod))
    assert 'system_capabilities' not in facts

# Generated at 2022-06-13 02:22:29.174204
# Unit test for method collect of class SystemCapabilitiesFactCollector

# Generated at 2022-06-13 02:22:30.254809
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # FIXME: need to mock module & module.run_command
    pass

# Generated at 2022-06-13 02:22:37.264731
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import ansible_collector

    def get_bin_path(self, arg):
        return '/bin/capsh'


# Generated at 2022-06-13 02:22:47.588572
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    ''' Unit test to confirm that we get the expected output from calling 'collect'
    '''

    # Generate a mock module to pass to the SystemCapabilitiesFactCollector
    class MockModule:
        def __init__(self):
            self.run_command_called = False
            self.run_command_output = None

# Generated at 2022-06-13 02:22:48.102626
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:22:57.086018
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collectors.system import SystemCapabilitiesFactCollector
    from ansible.module_utils.ansible_release import __version__ as ANSIBLE_VERSION
    from ansible.module_utils.facts.utils import get_file_lines
    import sys
    if sys.version_info[0] >= 3:
        import io
        StringIO = io.StringIO
    else:
        import StringIO
        StringIO = StringIO.StringIO

    class TestModule(object):
        def __init__(self, module_args, module_name='test',
                     no_log=False, connection='local',
                     run_command_environ_update=None):
            self.module_args = module_args
            self.module_name = module_name
            self.no_log = no_

# Generated at 2022-06-13 02:23:06.869767
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import platform
    import random

    try:
        import __builtin__ as builtins
    except ImportError:
        import builtins

    # NOTE: avoid modifying constant object
    L = list(range(10))
    random.shuffle(L)

# Generated at 2022-06-13 02:23:14.181891
# Unit test for method collect of class SystemCapabilitiesFactCollector

# Generated at 2022-06-13 02:23:24.165911
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import os
    from ansible.module_utils.facts.collector import BaseFactCollector

    class DummyModule:
        def __init__(self):
            pass

        def get_bin_path(self, arg):
            if arg == 'capsh':
                return os.path.join(os.path.dirname(os.path.realpath(__file__)),'capsh_test')
            else:
                return None


# Generated at 2022-06-13 02:23:44.179929
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    mock_module = MagicMock(
        get_bin_path=MagicMock(
            return_value='/usr/bin/capsh'
        ),
        run_command=MagicMock(
            return_value=(0, 'Current: =eip', None)
        ),
    )
    subject = SystemCapabilitiesFactCollector()
    assert subject.collect(mock_module) == {
        'system_capabilities': [],
        'system_capabilities_enforced': 'False'
    }

# Generated at 2022-06-13 02:23:51.518074
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Create Mock
    module = AnsibleModuleMock()

    # NOTE: run_command() mocking disabled due to the following issue:
    #       https://github.com/ansible/ansible/issues/54402
    # module.run_command.return_value = 0, "Current: =ep\nBounding set =cap_net_raw+ep\nSecurebits: 00/0x0/1'b0\n secure-noroot: no (unlocked)\n secure-no-suid-fixup: no (unlocked)\n secure-keep-caps: no (unlocked)\n uid=0(root) gid=0(root) groups=0(root)\n", ''

# Generated at 2022-06-13 02:24:00.604800
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts import ansible_collector

    class FakeModule(object):
        def __init__(self, bin_path):
            self.bin_path = bin_path

        def get_bin_path(self, name):
            self.bin_name = name
            return self.bin_path

        def run_command(self, cmd, errors='surrogate_then_replace'):
            self.cmd = cmd
            return self.returncode, self.out, self.err

    module = FakeModule(bin_path='/usr/bin/capsh')

   

# Generated at 2022-06-13 02:24:08.741011
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # mock module
    class ModuleMock:
        def __init__(self):
            self.exit_json = True
            self.run_command = True
            self.params = None
            self.get_bin_path = True

    # mock commands
    from ansible.module_utils.six.moves import builtins
    try:
        builtins.open = True
    except AttributeError:
        # FIXME: traversing down a namespace is bad -akl
        builtins = __import__('__builtin__')
        builtins.open = True


    module = ModuleMock()
    capsh_path = module.get_bin_path('capsh')
    rc = 0
    out = 'Current: =ep\n'
    err = ''
    module.run_command.return_value = rc, out

# Generated at 2022-06-13 02:24:10.783158
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    assert True

# Generated at 2022-06-13 02:24:21.492075
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = MagicMock()
    capsh_path = None
    module.get_bin_path.return_value = capsh_path

    # Test when capsh is not present
    facter_caps = SystemCapabilitiesFactCollector()
    facts = facter_caps.collect(module)
    assert facts['system_capabilities'] == []
    assert facts['system_capabilities_enforced'] == 'NA'

    # Test when capsh is present, but no capsh output
    capsh_path = 'test_bin'
    module.get_bin_path.return_value = capsh_path
    module.run_command.return_value = 0, '', ''

    facter_caps = SystemCapabilitiesFactCollector()
    facts = facter_caps.collect(module)

# Generated at 2022-06-13 02:24:30.440275
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils import basic
    from ansible.module_utils.facts import collector

    import ansible.module_utils.facts.system.caps
    import ansible.module_utils.facts.system.platform
    import ansible.module_utils.facts.system.distribution
    import ansible.module_utils.facts.system.machine
    import ansible.module_utils.facts.system.lsb

    assert ansible.module_utils.facts.system.caps is not None
    assert ansible.module_utils.facts.system.platform is not None
    assert ansible.module_utils.facts.system.distribution is not None
    assert ansible.module_utils.facts.system.machine is not None
    assert ansible.module_utils.facts.system.lsb is not None


# Generated at 2022-06-13 02:24:36.015633
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import collector

    module_mock = Mock()
    module_mock.run_command.return_value = 0, 'Current: =ep', ''
    module_mock.get_bin_path.return_value = '/bin/capsh'
    capabilities_fac = SystemCapabilitiesFactCollector()
    facts = capabilities_fac.collect(module_mock)

    assert 'system_capabilities' in facts
    assert 'system_capabilities_enforced' in facts
    assert facts['system_capabilities_enforced'] == 'False'
    assert facts['system_capabilities'] == []

# Generated at 2022-06-13 02:24:41.381301
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector.system_capabilities import SystemCapabilitiesFactCollector as test_fact_collector
    from ansible.module_utils.facts.collector.system_capabilities import get_caps_data, parse_caps_data
    import os
    import tempfile
    import pytest

# Generated at 2022-06-13 02:24:44.941740
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # We instantiate the class
    system_capabilities = SystemCapabilitiesFactCollector()
    # We test the collect method
    output = system_capabilities.collect()
    assert isinstance(output, dict)
    assert 'system_capabilities' in output
    assert 'system_capabilities_enforced' in output

# Generated at 2022-06-13 02:25:25.317798
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import sys
    if sys.version_info.major == 2:
        import __builtin__ as builtins  # pylint: disable=import-error
    else:
        import builtins

    import ansible.module_utils.facts.collector
    ansible.module_utils.facts.collector.__context__ = {'CAPSH': True}

    sys_caps_module = SystemCapabilitiesFactCollector()
    ansible.module_utils.facts.collector.get_bin_path = lambda x: '/bin/capsh'
    ansible.module_utils.facts.collector.run_command = lambda x: (0, 'Current: =ep cap_setpcap+p cap_setfcap+i', '')


# Generated at 2022-06-13 02:25:32.950162
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import ansible.module_utils.facts.system.caps as _caps
    from ansible.module_utils import basic
    results = {}
    caps = SystemCapabilitiesFactCollector
    facts = caps.collect(module=None)
    results['system_capabilities'] = 'NA'
    results['system_capabilities_enforced'] = 'NA'
    assert facts['system_capabilities'] == results['system_capabilities']
    assert facts['system_capabilities_enforced'] == results['system_capabilities_enforced']

    m = basic.AnsibleModule(
        argument_spec = dict()
    )
    m.get_bin_path = lambda x: 'capsh'
    def run_command(command, errors='surrogate_then_replace'):
        rc = 0

# Generated at 2022-06-13 02:25:43.869850
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    # import module to be tested
    # NOTE: not actually used in this test module
    import ansible.module_utils.facts.system.caps as caps_module

    # import names to be used by the test
    from ansible.module_utils._text import to_bytes

    # import test data
    from ansible.module_utils.facts.system.caps import CAPSH_OUTPUT

    # import mocks
    from ansible.module_utils.facts.system.caps import mock_module

    # create mock module object to be tested
    m = mock_module()

    # create unblock_output class to be used by the test
    unblock = SystemCapabilitiesFactCollector()

    # test collect method with enforced capabilties
    rc = 0
    out = to_bytes(CAPSH_OUTPUT)
    err = b

# Generated at 2022-06-13 02:25:44.392516
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:25:52.184943
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import mock

    import types
    import ast
    import os

    mock_module = mock.Mock()

# Generated at 2022-06-13 02:26:02.470202
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = 'module'

# Generated at 2022-06-13 02:26:03.806897
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: mock & unpatch module, e.g. via python-mock
    pass

# Generated at 2022-06-13 02:26:10.608806
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Given a mocked module
    module = mock.MagicMock()

    # Given a mocked capsh command execution
    mocked_rc = 0

# Generated at 2022-06-13 02:26:20.337345
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    facts_dict = {}
    capsh_path = '/bin/capsh'
    rc = 0
    out = 'Current: = cap_setuid+ep cap_setgid+epCapBnd: = 0000003fffffffff'
    err = ''
    collected_facts = {}

    class mock_module:
        def get_bin_path(self, arg):
            return capsh_path

        def run_command(self, arg, errors):
            return rc, out, err

    module = mock_module()
    sut = SystemCapabilitiesFactCollector()

    actual_result = sut.collect(module, collected_facts)

    expected_result = {'system_capabilities_enforced': 'False',
                       'system_capabilities': ['cap_setuid', 'cap_setgid']}
    assert actual_

# Generated at 2022-06-13 02:26:29.393791
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """ Unit test for method collect of class SystemCapabilitiesFactCollector """

# Generated at 2022-06-13 02:27:51.099052
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """Test fact gathering of system capabilities

    Expected results:
    *  system_capabilities and system_capabilities_enforced facts should be present

    """
    import sys
    import pytest
    from ansible.module_utils.facts import collection

    # Generate a fake module object
    import ansible_module_pcap_facts

    # Set module object
    sys.modules['ansible_module_pcap_facts'] = ansible_module_pcap_facts
    from ansible.module_utils.facts.collectors.capabilities import SystemCapabilitiesFactCollector

    # Get collector instance
    my_fact_collector = SystemCapabilitiesFactCollector()

    # Set module.run_command return values
    my_fact_collector.module = ansible_module_pcap_facts

    # Mocked run_command
   

# Generated at 2022-06-13 02:27:59.410985
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    class Module:
        def run_command(self, args, errors='surrogate_then_replace'):
            return 0, 'Current: =ep', ''
        def get_bin_path(self, path, required=True):
            return '/bin/capsh'

    collector = SystemCapabilitiesFactCollector()
    facts = collector.collect(Module())
    assert 'system_capabilities_enforced' in facts
    assert facts['system_capabilities_enforced'] == 'False'
    assert 'system_capabilities' in facts
    assert facts['system_capabilities'] == []



# Generated at 2022-06-13 02:28:01.244193
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    assert True, 'FIXME: No unit test for SystemCapabilitiesFactCollector.collect.'

# Generated at 2022-06-13 02:28:09.963276
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    collector = SystemCapabilitiesFactCollector()
    mock_module = SystemCapabilitiesMockModule()
    facts_dict = collector.collect(mock_module)

# Generated at 2022-06-13 02:28:20.415861
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = AnsibleModuleMock()
    fake_bin_path = "/fake/bin/path"
    module.get_bin_path.return_value = fake_bin_path
    fake_output = "Current: =ep\nBounding set =eip\nSecurebits: 00/0x0/1'b0 grabbing \n secure-noroot, \n secure-no-setuid-fixup \n\n"
    module.run_command.return_value = [0, fake_output, '']

    system_caps_fact_collector = SystemCapabilitiesFactCollector()
    system_caps_fact_collector.collect(module=module)

    # NOTE: -> get_caps_data()/parse_caps_data() for easier mocking -akl

# Generated at 2022-06-13 02:28:29.850597
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.facts import Facts
    from ansible.module_utils.facts.collectors.system.caps import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts.collectors.system.caps import get_caps_data, parse_caps_data
    from ansible.module_utils.six import PY2
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-13 02:28:35.422534
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    test_dict = {}
    test_dict['system_capabilities'] = ['cap_audit_control', 'cap_syslog', 'cap_net_admin', 'cap_sys_tty_config',
                                        'cap_sys_admin', 'cap_net_raw', 'cap_setfcap']
    test_dict['system_capabilities_enforced'] = 'True'
    test_collector = SystemCapabilitiesFactCollector()
    class MockModule:
        def get_bin_path(self, *args, **kwargs):
            return 'capsh'
        def run_command(*args, **kwargs):
            return 0, 'Current: =ep', ''

    test_module = MockModule()
    assert test_collector.collect(test_module) == test_dict
    # This test is to make sure we get the

# Generated at 2022-06-13 02:28:42.417549
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.collector.system import SystemCapabilitiesFactCollector
    # NOTE: these unit tests require a system with capsh installed
    #       used in capsh_path = module.get_bin_path('capsh')
    capsh_collector = get_collector_instance(SystemCapabilitiesFactCollector)
    collected_facts = {}
    assert SystemCapabilitiesFactCollector.name == 'caps'
    assert len(SystemCapabilitiesFactCollector._fact_ids) == 2
    for fact in SystemCapabilitiesFactCollector._fact_ids:
        assert fact in SystemCapabilitiesFactCollector.collect(collected_facts)

# Generated at 2022-06-13 02:28:50.408091
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.collector import TestModule


# Generated at 2022-06-13 02:28:52.867619
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Arrange
    class Module(object):
        def __init__(self):
            self.facts = {}

        def get_bin_path(self, path):
            return '/usr/bin/capsh'

    mod = Module()
    c = SystemCapabilitiesFactCollector()
    # Act
    result = c.collect(mod)
    # Assert
