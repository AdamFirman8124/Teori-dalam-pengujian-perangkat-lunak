

# Generated at 2022-06-13 02:19:45.524602
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # TODO: create the mock module object, invoke the collect method, check the returned fact
    # object, and write an assertion.
    pass

# Generated at 2022-06-13 02:19:55.869936
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import os
    import sys
    import platform

    # TODO: Mock run_command() and File module for unit testing -akl
    #from mock import MagicMock
    #from ansible.module_utils.facts import File

    run_command = os.system('/usr/sbin/capsh --print 2>/dev/null')
    run_command = '%s: %s' % (os.WEXITSTATUS(run_command), os.WTERMSIG(run_command))
    if run_command == '0: None':
        print("System Capabilities Fact Collector - Unit Test")
        print("===============================================")
        print("")
        print("  System: %s %s, Python %s" % (platform.system(), platform.release(), sys.version))

# Generated at 2022-06-13 02:20:06.436129
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Test with /usr/bin/capsh present
    class Module:
        def get_bin_path(self, bin):
            if bin == "capsh":
                return "/usr/bin/capsh"
            return None

# Generated at 2022-06-13 02:20:07.158453
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: write unit test with mocks -akl
    pass

# Generated at 2022-06-13 02:20:15.573696
# Unit test for method collect of class SystemCapabilitiesFactCollector

# Generated at 2022-06-13 02:20:23.242642
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: as test_capsh_output.py is currently the gold standard,
    # use that as the source of test data, this is useful as capsh
    # output can vary slightly depending on the distro, kernel,
    # kernel-specific capabilities and versions.
    # -akl
    import json
    import os
    from ansible.module_utils.facts.system.capabilities import (
        get_caps_data, parse_caps_data
    )

    TEST_DIR = os.path.dirname(os.path.realpath(__file__))
    # testfiles/capsh_output-{os_name}-{architecture}.json

# Generated at 2022-06-13 02:20:24.078913
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    SystemCapabilitiesFactCollector().collect()

# Generated at 2022-06-13 02:20:29.204027
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    class MockModule():
        def get_bin_path(self, path):
            return '/bin/capsh'

# Generated at 2022-06-13 02:20:33.466043
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    class TestModule(object):
        def __init__(self, enforce, capabilities):
            self.enforce = enforce
            self.capabilities = capabilities

        def get_bin_path(self, binary):
            return binary

        def run_command(self, cmd, errors):
            if cmd[0] == 'capsh':
                if self.enforce:
                    return (0, "Current: =ep\n" +
                                "Bounding set =" + self.capabilities + '\n',
                            '')
                else:
                    return (0, "Current: =eip\n" +
                                "Bounding set =" + self.capabilities + '\n',
                            '')

    class TestCollectedFacts(object):
        def __init__(self, item):
            self.item = item



# Generated at 2022-06-13 02:20:35.137664
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """ Unit test for method collect of class SystemCapabilitiesFactCollector """
    pass

# Generated at 2022-06-13 02:20:48.540284
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    m = AnsibleModuleStub()
    s = SystemCapabilitiesFactCollector(m)

    m.get_bin_path = lambda x: '/usr/bin/capsh'
    m.run_command = lambda x, errors='surrogate_then_replace': (0, 'Current: =ep', '')
    assert s.collect() == {}

# Generated at 2022-06-13 02:20:59.046756
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible_collections.ansible.community.tests.unit.module_utils.facts.collector.system_capabilities import FakeModule
    module = FakeModule()

# Generated at 2022-06-13 02:21:08.521794
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import sys
    import mock
    from ansible.module_utils.facts.collector import BaseFactCollector

    class MockModule(object):
        pass

    module = MockModule()
    module.get_bin_path = mock.Mock(return_value = '/usr/bin/capsh')
    module.run_command = mock.Mock(return_value = (None, 'Current: =ep', None))

    # Create and run the target mock
    target = SystemCapabilitiesFactCollector()
    result = target.collect(module=module)

    # Check the results
    assert result['system_capabilities_enforced'] == 'False'
    assert result['system_capabilities'] == []

# Generated at 2022-06-13 02:21:17.996532
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # START TESTS #

    import sys
    if sys.version_info[0] > 2:
        # Python 3 imports
        from io import StringIO
    else:
        # Python 2 imports
        from StringIO import StringIO

    # Test the collection and parsing of capability data via the mock module.

# Generated at 2022-06-13 02:21:24.480280
# Unit test for method collect of class SystemCapabilitiesFactCollector

# Generated at 2022-06-13 02:21:26.494048
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    sys_caps = SystemCapabilitiesFactCollector()
    assert sys_caps.collect() == {}

# Generated at 2022-06-13 02:21:33.031826
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    '''
    Returns the correct data structure
    '''
    # NOTE: setup/mock capsh_path here
    collector = SystemCapabilitiesFactCollector()
    assert collector.collect() == {}
    # NOTE: assert non-empty facts_dict/enforced == 'NA'/enforced_caps == [] on non-Linux distro (e.g. macOS) -akl

# Generated at 2022-06-13 02:21:40.245541
# Unit test for method collect of class SystemCapabilitiesFactCollector

# Generated at 2022-06-13 02:21:49.669739
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """SystemCapabilitiesFactCollector - unit test 1"""
    import os
    from ansible.module_utils.facts.collector import FactsCollector
    from ansible.module_utils import basic
    import ansible.module_utils.facts.collector.system as system
    module_path = os.path.dirname(system.__file__)
    for f in os.listdir(module_path):
        if f[-3:] == '.py' and f != '__init__.py':
            m = str('ansible.module_utils.facts.collector.system.' + f[:-3])
            c = str('ansible.module_utils.facts.collector.system.' + f[:-3] + '.FactCollector')
            temp = __import__(m, fromlist=[c])
            cls = getattr

# Generated at 2022-06-13 02:21:57.815464
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import re
    import tempfile
    import ansible.module_utils.facts.collector

    capsh_path = '/path/to/capsh'

# Generated at 2022-06-13 02:22:05.493877
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: -> get_caps_data()/parse_caps_data() for easier mocking -akl
    pass

# Generated at 2022-06-13 02:22:05.990422
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:22:10.188749
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = FakeModule()
    module.run_command = FakeRunCommand()
    module.get_bin_path = FakeGetBinPath()
    module.get_bin_path.paths = {'capsh': '/usr/bin/capsh'}
    module.run_command.results = [(0, 'Current:\nsecure-bits:KEEP CAP_SETPCAP Droping: =ep', '')]
    fact_collector = SystemCapabilitiesFactCollector(module)
    facts_dict = fact_collector.collect()
    assert facts_dict == {'system_capabilities_enforced': 'False', 'system_capabilities': []}
    assert module.run_command.executed == [['/usr/bin/capsh', '--print']]


# Generated at 2022-06-13 02:22:18.619236
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.system.system_capabilities import SystemCapabilitiesFactCollector

    class FakeModule(object):
        def __init__(self):
            self.rc = 0
            self.failed = False


# Generated at 2022-06-13 02:22:22.869222
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # TODO: parameterize (mock) module, collected_facts -akl
    facts_dict = SystemCapabilitiesFactCollector().collect()
    assert set(facts_dict) == set(['system_capabilities', 'system_capabilities_enforced'])
    assert facts_dict['system_capabilities_enforced'] == 'False'
    assert type(facts_dict['system_capabilities']) == list
    assert len(facts_dict['system_capabilities']) > 0

# Generated at 2022-06-13 02:22:27.270948
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = AnsibleModuleMock()
    module.run_command = mock.Mock(return_value=(0, 'Current: = ep', ''))
    module.get_bin_path = mock.Mock(return_value='/bin/capsh')
    module.get_bin_path.side_effect = lambda arg: arg

    fact_collector = SystemCapabilitiesFactCollector()
    result = fact_collector.collect(module=module)

    assert result['system_capabilities'] == []
    assert result['system_capabilities_enforced'] == 'False'


# Generated at 2022-06-13 02:22:32.681598
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():

    import ansible.module_utils.facts.collector.system.system_capabilities as system_capabilities
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes


# Generated at 2022-06-13 02:22:37.071220
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    print("Testing method collect of class SystemCapabilitiesFactCollector")
    # Create an instance of class SystemCapabilitiesFactCollector
    # NOTE: replace SystemCapabilitiesFactCollector with name of class in
    #       fact module -akl
    obj = SystemCapabilitiesFactCollector()

    # Implement code to test method collect of class SystemCapabilitiesFactCollector
    # NOTE: replace SystemCapabilitiesFactCollector with name of class in
    #       fact module -akl
    pass

#

# Generated at 2022-06-13 02:22:47.353609
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import FactsCollector
    from ansible.module_utils.facts.collectors.system.caps import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts.collectors.base import FactCollectorCache
    from ansible.module_utils.facts.cache import FactsCache
    from ansible.module_utils.facts.system.caps import CapabilitiesFacts
    from ansible.module_utils.facts.system.caps import Capsh
    from ansible.module_utils.six import b
    from ansible.module_utils.six.moves import builtins

    # Mock collect method of class Capsh

# Generated at 2022-06-13 02:22:47.866723
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:23:06.827042
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts import ModuleStore
    from ansible.module_utils.facts import fact_collector
    from ansible.module_utils.facts.collector.system import SystemCapabilitiesFactCollector

    # Needed for normalization and for (possible) future automatic type derivation
    system = SystemCapabilitiesFactCollector
    module = ModuleStore.get_module()
    facts = fact_collector.collect(module)

    assert type(system.collect(module, facts)) == dict
    assert type(system.collect(module, facts)['system_capabilities']) == list
    assert type(system.collect(module, facts)['system_capabilities_enforced']) == str

# Generated at 2022-06-13 02:23:14.157859
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import pytest
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.system.caps import SystemCapabilitiesFactCollector
    # TODO: mock
    pytest.skip("Mocking needed to run this test")
    cc = Collector(['posix'], 'posix', None)
    capsh_path = '/usr/bin/capsh'

# Generated at 2022-06-13 02:23:23.752499
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Setup
    import platform
    import distro
    distro_id = distro.id()
    distro_version = distro.version() or 'unknown'
    distro_release = distro.release() or 'unknown'
    distro_codename = distro.codename() or 'unknown'
    sys_platform = platform.system() or 'unknown'

    # Test
    class fake_module(object):
        def __init__(self):
            self.params = {}
            self.READ_CACHE = {'distro_id': distro_id}
            self.distribution = distro_id
            self.distribution_release = distro_version
            self.distribution_major_version = distro_version
            self.distribution_version = distro_version
            self.distribution_release

# Generated at 2022-06-13 02:23:34.256573
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.collector import get_file_content
    import re

    # Declare a minimal test fixture
    minimal_collector_instance = get_collector_instance(SystemCapabilitiesFactCollector)

    # Declare a string with the content of capsh
    capsh_file_content = get_file_content('/usr/bin/capsh')

    # Mock the response of capsh with a regexp matching 'Current:'
    minimal_collector_instance.module.run_command.return_value = (0, capsh_file_content)

    # Call the collect method
    result = minimal_collector_instance.collect()

    # Assert there will be a call to 'capsh' with the correct parameters
   

# Generated at 2022-06-13 02:23:42.501658
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """
    Unit test of SystemCapabilitiesFactCollector().collect()
    """
    # patch
    class MockPayload():
        """
        Class to mock module.run_command()'s 'return_payload'
        """
        def __init__(self):
            self._rc = 0

# Generated at 2022-06-13 02:23:47.139269
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    sys_caps_mod = object()
    sys_caps_collected_facts = object()
    sys_caps_collector = SystemCapabilitiesFactCollector()
    sys_caps_facts_dict = sys_caps_collector.collect(sys_caps_mod, sys_caps_collected_facts)
    assert sys_caps_facts_dict == {}

# Generated at 2022-06-13 02:23:52.893154
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # Init
    test_module = MagicMock()
    test_module.run_command =  MagicMock(return_value=(0, 'Current:\t=ep', ''))
    test_module.get_bin_path = MagicMock(return_value='capsh')

    # Test
    obj = SystemCapabilitiesFactCollector()
    out = obj.collect(module=test_module)

    # Assertions
    assert 'system_capabilities_enforced' in out
    assert 'system_capabilities' in out
    assert out['system_capabilities'] is not None
    assert out['system_capabilities_enforced'] == 'False'
    assert out['system_capabilities'] == []

# Generated at 2022-06-13 02:24:01.593882
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    mock_module = type('module_type', (object,), {'run_command': lambda *args: (0, 'Current: =ep', '')})
    mock_caps_module = SystemCapabilitiesFactCollector()
    assert mock_caps_module.collect(module=mock_module)["system_capabilities_enforced"] == 'False'
    assert mock_caps_module.collect(module=mock_module)["system_capabilities"] == []

    mock_module = type('module_type', (object,), {'run_command': lambda *args: (0, 'Current: =ep cap_chown,cap_dac_override+eip', '')})
    mock_caps_module = SystemCapabilitiesFactCollector()

# Generated at 2022-06-13 02:24:09.130141
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.system.caps import SystemCapabilitiesFactCollector
    from ansible.module_utils.facts import ModuleFacts
    module_facts = ModuleFacts(module_runner=None,
                               loader=None,
                               console_connection=None,
                               ansible_version=None,
                               redact_sensitive_facts=False,
                               active_user='root',
                               ansible_managed=None)
    # In case we need to debug unit tests:
    #import pudb; pu.db
    with open("for_caps_fact_collector_collect.txt", "r") as f:
        capsh_out = f.read().strip()
    module_mock = Mock()

# Generated at 2022-06-13 02:24:21.018231
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    def _module_function(function_name):
        def function(*args, **kwargs):
            if args[0] == 'capsh':
                return self.__get_bin_path(function_name, *args, **kwargs)
            else:
                pass #print(function_name, args[0], kwargs)
        return function

    def _module_method(method_name):
        def method(*args, **kwargs):
            if args[0] == [self.__get_bin_path('capsh'), '--print']:
                return self.__run_command(method_name, *args, **kwargs)
            else:
                pass #print(method_name, args[0], kwargs)
        return method


# Generated at 2022-06-13 02:24:52.910508
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    ''' Unit test for method collect of class SystemCapabilitiesFactCollector '''
    class MockModule(object):
        ''' Mock Module '''
        def __init__(self, capsh_path):
            self.caps_path = capsh_path

        def get_bin_path(self, path, required=False):
            ''' mocked method get_bin_path '''
            return self.caps_path

        def run_command(self, cmd, errors='surrogate_then_replace'):
            ''' mocked method run_command '''

# Generated at 2022-06-13 02:24:58.275549
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """
    Unit test for method collect of class SystemCapabilitiesFactCollector.
    """

    c = SystemCapabilitiesFactCollector()
    from ansible.module_utils.facts import ModuleFacts

    m = ModuleFacts(
        module_name='facts',
        module_args=[],
        ansible_version='2.5.5',
        seed_dir=None,
    )

    m.run_command = lambda x, errors='surrogate_then_replace': ('', 'Current: =ep', '')
    assert c.collect(module=m) == {
                                    'system_capabilities_enforced': 'False',
                                    'system_capabilities': [],
                                   }


# Generated at 2022-06-13 02:25:07.499832
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module_mock = Mock()

    # early exit where capsh_path is unset
    module_mock.get_bin_path.return_value = None

    result = SystemCapabilitiesFactCollector().collect(module_mock)
    assert result == {}

    module_mock.get_bin_path.assert_called_with('capsh')

    # no early exit, i.e. capsh_path is set
    # NOTE: this is not a great test, as we're relying on the underlying run_command() call.
    module_mock.get_bin_path.return_value = 'capsh'

# Generated at 2022-06-13 02:25:11.256646
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils import basic

    from ansible_collections.misc.not_a_real_collection.plugins.module_utils.facts.collectors.system import SystemCapabilitiesFactCollector

    module = basic.AnsibleModule(
        argument_spec={},
        supports_check_mode=True)

    expected_result = {'system_capabilities': ['cap_sys_admin', 'cap_dac_read_search'], 'system_capabilities_enforced': 'True'}

    result = SystemCapabilitiesFactCollector.collect(module=module)

    assert result == expected_result

# Test if the module is idempotent

# Generated at 2022-06-13 02:25:22.704260
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = {}
    collected_facts = {}
    fact_collector = SystemCapabilitiesFactCollector(module, collected_facts)

    capsh_path = '/usr/bin/capsh'
    module['get_bin_path'] = lambda x, opt_dirs=[] : capsh_path

# Generated at 2022-06-13 02:25:23.226177
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:25:23.719402
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    pass

# Generated at 2022-06-13 02:25:31.803087
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts import ansible_module
    from ansible.module_utils.facts.utils import FactsParseError
    from ansible.module_utils._text import to_bytes
    import os

    f = get_collector_instance('SystemCapabilitiesFactCollector')

    def _get_capsh_path():
        capsh_path = None
        if os.path.exists('/usr/sbin/capsh'):
            capsh_path = '/usr/sbin/capsh'
        elif os.path.exists('/usr/bin/capsh'):
            capsh_path = '/usr/bin/capsh'
        return capsh_path

    capsh_path = _get_cap

# Generated at 2022-06-13 02:25:41.928377
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # This is a minimal example of a module, just of use
    # to mock subprocess.Popen as module.run_command
    class Module(object):
        def __init__(self):
            self.run_command_return = (0, '', '')

        def get_bin_path(self, executable=None):
            return '/bin/capsh'

        def run_command(self, args=None, errors='surrogate_then_replace'):
            return self.run_command_return

    # unit test
    # mocking object, to test method collect() of class SystemCapabilitiesFactCollector
    # also testing parse_caps_data()

# Generated at 2022-06-13 02:25:50.507291
# Unit test for method collect of class SystemCapabilitiesFactCollector

# Generated at 2022-06-13 02:26:48.449346
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    test_collector = SystemCapabilitiesFactCollector()
    result = test_collector.collect()
    for fact in result:
        assert isinstance(result[fact], (list, str))

# Generated at 2022-06-13 02:26:57.637507
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import platform
    import re
    import json
    import pytest
    import tempfile
    import subprocess

    class MockOs(object):
        """Mock class for os module"""
        @staticmethod
        def stat(path):
            class MockStatResult(object):
                """Mock class for os.stat result"""
                def __init__(self):
                    self.st_mode = 448  # 448 == 0o700
            return MockStatResult()

    class MockPsutil(object):
        """Mock class for psutil module"""
        @staticmethod
        def process_iter():
            return []

    class MockSubprocess(object):
        """Mock class for subprocess module"""

# Generated at 2022-06-13 02:27:04.768124
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    #
    # module object 'mock' used for unittest
    #
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )

    #
    # set up return values for module.run_command()
    #

# Generated at 2022-06-13 02:27:13.731885
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    module = get_module_mock()
    module.get_bin_path.return_value = '/bin/capsh'
    module.run_command.return_value = (0, 'Current: =ep', '')

    sys_caps = SystemCapabilitiesFactCollector()

    # Get test facts
    facts = sys_caps.collect(module=module)

    # Check for test facts
    assert 'system_capabilities' in facts
    assert isinstance(facts['system_capabilities'], list)
    assert not facts['system_capabilities']
    assert 'system_capabilities_enforced' in facts
    assert isinstance(facts['system_capabilities_enforced'], str)
    assert facts['system_capabilities_enforced'] == 'False'


# Generated at 2022-06-13 02:27:23.334984
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: use mock to replace the module, prevent actual call to 'capsh'
    import mock
    import ansible.module_utils.facts.system.capabilities as cap
    import ansible.module_utils.facts.system.capabilities as utils

    module = mock.MagicMock()
    # NOTE: capsh_path = module.get_bin_path('capsh')
    module.get_bin_path.return_value = '/usr/bin/capsh'

    # NOTE: use mock to replace method run_command
    with mock.patch.object(utils, 'run_command') as mock_run_command:
        # NOTE: rc,out,err = module.run_command([capsh_path,"--print"], errors='surrogate_then_replace')
        rc = 0
        out = 'Current: =ep'

# Generated at 2022-06-13 02:27:30.618304
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    cmd = '/bin/capsh --print'
    capsh_out = b'Current: = cap_setuid+ep cap_setgid+ep cap_setpcap+ep'
    (rc, out, err) = (0, capsh_out, '')

    # Note: 'module' is a mock and get_bin_path() is stubbed to return cmd.
    #       Capabilities() is stubbed to return 'enforced_caps'
    module = mock.MagicMock()
    module.get_bin_path.return_value = cmd
    # Capabilities().parse_caps_data() is stubbed to return 'enforced_caps'
    Capabilities.parse_caps_data.return_value = 'enforced_caps'
    # Capabilities().get_caps_data() is stubbed to return (rc, capsh_

# Generated at 2022-06-13 02:27:35.533058
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    from ansible.module_utils.facts.system.capabilities import SystemCapabilitiesFactCollector

    collector = SystemCapabilitiesFactCollector()

    assert 'system_capabilities' in collector._fact_ids
    assert 'system_capabilities_enforced' in collector._fact_ids

# Generated at 2022-06-13 02:27:42.981305
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    """Test ability to parse capsh capabilities"""
    module = FakeModule('/bin/capsh')

# Generated at 2022-06-13 02:27:51.425855
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    import imp
    import os
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import get_collector_class
    from ansible.module_utils.facts.collector import list_collectors
    from ansible.module_utils.facts import timeout

    # given:
    timeout.SLEEP_TIME = 0.0
    module = imp.new_module('module')
    module.run_command = lambda command, errors: (0, '', '')
    module.get_bin_path = lambda file: '/bin/%s' % file

    # when:
    collected_facts = {}
    collector = get_collector_class(to_bytes("SystemCapabilitiesFactCollector"))

# Generated at 2022-06-13 02:28:01.385843
# Unit test for method collect of class SystemCapabilitiesFactCollector
def test_SystemCapabilitiesFactCollector_collect():
    # NOTE: I'd prefer to be able to refactor this into a helper function
    #       which can be called from other tests, but I don't think that's
    #       possible with the current unit test infrastructure.
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
