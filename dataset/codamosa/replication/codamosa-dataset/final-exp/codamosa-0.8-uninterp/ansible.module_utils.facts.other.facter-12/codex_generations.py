

# Generated at 2022-06-13 01:58:53.092526
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    # test with a empty module
    ffc = FacterFactCollector()
    assert ffc.collect() == {}

    # test with a valid facter
    module = {}
    ffc = FacterFactCollector()
    module.get_bin_path = lambda cmd, opt_dirs: "/usr/bin/{}".format(cmd)
    ffc.run_facter = lambda m, facter_path: (0, '{"system-uptime": {}}', "")

    assert ffc.collect(module) == {"facter_system_uptime": {}}

# Generated at 2022-06-13 01:58:54.028510
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    facterfactcollector = FacterFactCollector()
    assert facterfactcollector.find_facter() is not None

# Generated at 2022-06-13 01:58:54.815012
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    assert FacterFactCollector().find_facter(None) == None

# Generated at 2022-06-13 01:59:06.340649
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    test_cases = [
        {
            # Return None if facter_path is None
            'facter_path': None,
            'expected': None
        },
        {
            # Return None if facter_path is ''
            'facter_path': '',
            'expected': None
        }
    ]
    class Module:
        def get_bin_path(self, cmd, opt_dirs=()):
            return cmd

        def run_command(self, cmd):
            return 0, '12345', ''

    for test_case in test_cases:
        fact_collector = FacterFactCollector()
        result = fact_collector.get_facter_output(test_case['facter_path'])
        assert result == test_case['expected']

# Generated at 2022-06-13 01:59:11.736393
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    FactCollector = FacterFactCollector(None)
    class TestModule():
        def get_bin_path(self, name, required=False, opt_dirs=[]):
            return '/usr/bin/' + name
        def run_command(self, command):
            return 0, '''{
    "operatingsystem": "Ubuntu",
    "kernel": "Linux",
    "kernelmajversion": "4.4"
}''', ''
    facter_output = FactCollector.get_facter_output(TestModule())
    assert facter_output is not None

# Generated at 2022-06-13 01:59:17.595150
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    from ansible_collections.ansible.community.tests.unit.compat.mock import patch
    from ansible_collections.ansible.community.tests.unit.modules.utils import set_module_args
    import ansible_collections.ansible.community.plugins.module_utils.facts.collectors.facter as facter_collector

    with patch.object(facter_collector.FacterFactCollector,
                      'get_facter_output',
                      return_value=json.dumps({'os': 'darwin'})):
        set_module_args({})
        collector = facter_collector.FacterFactCollector()

        assert collector.collect() == {'facter_os': 'darwin'}

# Generated at 2022-06-13 01:59:22.570353
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    ff = FacterFactCollector()
    collected_facts = {}

    # TODO: add more tests for each path
    # mock module where facter --json works
    class ModuleMock(object):
        def __init__(self, bin_path_result, run_command_results):
            self.bin_path_return = bin_path_result
            self.run_command_results = run_command_results
            self.bin_path_count = 0
            self.run_command_count = 0

        def get_bin_path(self, name, opt_dirs=None, required=False):
            self.bin_path_count += 1
            return self.bin_path_return

        def run_command(self, cmd):
            self.run_command_count += 1

# Generated at 2022-06-13 01:59:31.301950
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    collector = FacterFactCollector(None, None)
    # Remove existing facter binaries
    del os.environ['PATH']
    # If Facter is not available, collector.find_facter should return None
    assert collector.find_facter(None) is None
    # But, if Facter is available, collector.find_facter should return its path
    os.environ['PATH'] = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'lib', 'ansible', 'module_utils', 'facts'))
    assert collector.find_facter(None) is not None
    # Add back the original path

# Generated at 2022-06-13 01:59:41.023936
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    import sys
    import os
    import unittest

    class MockModule(object):
        def __init__(self, test_case):
            self.test_case = test_case
            self.params = {}
            self._fail_json = False

        def fail_json(self, **kwargs):
            self._fail_json = True
            self.fail_json_msg = kwargs


# Generated at 2022-06-13 01:59:48.380789
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    class mock_get_bin_path():
        def __call__(self, name, **kwargs):
            if name == 'facter':
                return '/usr/bin/facter'
            elif name == 'cfacter':
                return None
            else:
                raise Exception('unknown argument to mock_get_bin_path: {}'.format(name))

    
    class mock_module():
        def __init__(self):
            self.run_command_calls = 0
            self.run_command_returns = [0, json.dumps({}), ""]
            self.run_command_return_idx = 0
            self.get_bin_path = mock_get_bin_path()


# Generated at 2022-06-13 02:00:00.519547
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():
    """
    Test whether the required shellcode 'facter --json' is executed
    correctly.
    """
    # Use a real module
    from ansible.modules.system.setup import setup

    # Create the class object and define the mock functions and parameters
    module = setup.SetupModule()
    facter_path = '/opt/puppetlabs/bin/facter'

# Generated at 2022-06-13 02:00:10.741213
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():
    """
    This test is a bit naive, basically look for any JSON-ish looking string in the output
    for which I can construct a dictionary.
    """

    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts import collector

    # Creating a FacterFactCollector object and mocking module.run_command
    facter_collector = FacterFactCollector()
    facter_collector.module = collector.ActionModule()
    facter_collector.module.run_command = lambda cmd, warn: (0, '{"testing": "test_passed"}', '')

# Generated at 2022-06-13 02:00:22.810000
# Unit test for method collect of class FacterFactCollector

# Generated at 2022-06-13 02:00:31.030086
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    from ansible.module_utils.common.collections import ImmDict

    class FakeModule:
        def __init__(self, return_value):
            self._return_value = return_value

        def get_bin_path(self, binary, opt_dirs=[]):
            return self._return_value

    # When facter is available
    fake_module = FakeModule(return_value='/usr/bin/facter')
    facter_collector = FacterFactCollector()
    result = facter_collector.find_facter(fake_module)
    assert result == '/usr/bin/facter'

    # When cfacter is available
    fake_module = FakeModule(return_value='/usr/share/cfacter/bin/cfacter')
    facter_collector = FacterFactCollector()


# Generated at 2022-06-13 02:00:37.481688
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    # Create an object of FacterFactCollector
    facter_collector = FacterFactCollector()
    # Retrieve the return value of find_facter method
    facter_path = facter_collector.find_facter(None)
    # Assert the facter_path is not empty
    assert facter_path is not None
    # Assert the facter_path is not an empty string
    assert facter_path != ''



# Generated at 2022-06-13 02:00:40.181637
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    json_output = '{"architecture":"amd64","operatingsystem":"Amazon","kernel":"Linux","country":"USA"}'
    json_output_dict = json.loads(json_output)

# Generated at 2022-06-13 02:00:47.952647
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    # Dummy ansible module
    from ansible.module_utils.facts.tests.test_utils import DummyModule
    dummy_module = DummyModule()
    # Dummy facter command output

# Generated at 2022-06-13 02:00:55.735116
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    from ansible.module_utils.facts.utils import get_collector_instance
    from ansible.module_utils.facts.collector import get_collector_capabilities

    facter_collector = get_collector_instance(FacterFactCollector)
    assert facter_collector.name == 'facter'

    facter_collector_capabilities = get_collector_capabilities(facter_collector)
    assert 'facter' in facter_collector_capabilities['gather_subset']

# Generated at 2022-06-13 02:01:00.278598
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.utils import get_file_content
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    import tempfile

    class MockModule(object):
        def __init__(self):
            self.params = {
                'path': '/usr/bin'
            }

        def get_bin_path(self, binary, opt_dirs=[]):
            return '/' + binary

        def run_command(self, command, check_rc=True):
            msg = "facter command missing: %s" % command

# Generated at 2022-06-13 02:01:08.701904
# Unit test for method collect of class FacterFactCollector

# Generated at 2022-06-13 02:01:22.215616
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    import mock
    collecter = FacterFactCollector()

    with mock.patch.object(collecter, '_find_executable', return_value=None):
        assert collecter.find_facter(mock.MagicMock()) == None

    module_mock = mock.MagicMock()
    module_mock.get_bin_path.return_value = '/opt/puppetlabs/bin/facter'
    assert collecter.find_facter(module_mock) == '/opt/puppetlabs/bin/facter'

    module_mock.get_bin_path.return_value = '/opt/puppetlabs/bin/cfacter'
    assert collecter.find_facter(module_mock) == '/opt/puppetlabs/bin/cfacter'



# Generated at 2022-06-13 02:01:30.938036
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import MockModule

    class MockFacterFactCollector(FacterFactCollector):
        def find_facter(self, module):
            return '/bin/facter'

        def run_facter(self, module, facter_path):
            return 0, '{"facter_uptime": {"seconds": "14406", "hours": "4"}}', ''

    test_module = MockModule().get_module_mock()

    fact_collector = MockFacterFactCollector(collectors=None, namespace=None)
    facter_dict = fact_collector.get_facter_output(test_module)

    assert facter_dict is not None

# Generated at 2022-06-13 02:01:35.515060
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    """ Unit test for method find_facter of class FacterFactCollector """
    class DummyModule(object):
        def get_bin_path(self, command, opt_dirs = None):
            """ mock get_bin_path """
            return None
    module = DummyModule()
    assert FacterFactCollector().find_facter(module) == None


# Generated at 2022-06-13 02:01:43.438577
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    from ansible.module_utils.facts.collector import Collectors
    collection = Collectors()
    assert isinstance(collection, Collectors)

    collection._module = 'AnsibleModule'
    collection._collectors = [FacterFactCollector()]
    for c in collection:
        for key in ['_module', '_collectors', '_excluded_facts']:
            assert hasattr(c, key)
        facts = c.collect(['facter'])
        assert facts
        assert isinstance(facts, dict)
        #assert facts['facter']['is_virtual']



# Generated at 2022-06-13 02:01:51.450848
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    # Arrange
    temp_data_path = '/temp/test_FacterFactCollector_collect'
    temp_fact_subdir_path = temp_data_path+'/facts'
    os.makedirs(temp_fact_subdir_path)
    module_mock = Mock()
    module_mock.get_bin_path.side_effect = [temp_data_path+'/facter']

# Generated at 2022-06-13 02:01:58.893025
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    """
    Checks if collect method of FacterFactCollector class works as expected.
    """
    from ansible.module_utils import basic
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts import roundup_options

    options = {'gather_subset': 'all', 'gather_timeout': 10}
    module = basic.AnsibleModule(
        argument_spec={
            'gather_subset': dict(default=['!all'], type='list')
        },
        supports_check_mode=True
    )
    module.params = roundup_options(module.params, options)

    fact_collector = FacterFactCollector(collectors=default_collectors)
    facts = fact_collector.collect(module=module)

# Generated at 2022-06-13 02:02:09.612467
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():

    m = AnsibleModule(
        argument_spec = dict()
    )
    f = FacterFactCollector()

    # cfacter binary should be found

# Generated at 2022-06-13 02:02:13.514338
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    ffc = FacterFactCollector()
    class Module:
        def get_bin_path(self, cmd, opt_dirs=None):
            return '/bin/%s' % cmd

    module = Module()
    assert ffc.find_facter(module) == '/bin/facter'



# Generated at 2022-06-13 02:02:23.338191
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():
    module_mock = MockModule()
    module_mock.get_bin_path.side_effect = ['path_to_facter', 'path_to_cfacter']
    module_mock.run_command.side_effect = [[0, 'data', 'error']]

    facter_collector = FacterFactCollector()

    # Using facter
    rc, out, err = facter_collector.run_facter(module_mock, 'path_to_facter')

    assert rc == 0
    assert out == 'data'
    assert err == 'error'
    assert module_mock.get_bin_path.call_count == 2
    assert module_mock.run_command.call_count == 1

# Generated at 2022-06-13 02:02:33.168764
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    '''unit test for method find_facter of class FacterFactCollector'''

    class FacterTestModule:
        '''Fake module to test FacterFactCollector class'''

        def __init__(self):
            self.bin_path = self.find_bin_path

        # pylint: disable=no-self-use
        def find_bin_path(self, bin_name, opt_dirs=None):
            '''
            Fake method for find_bin_path method of module_utils.basic.AnsibleModule,
            to test FacterFactCollector class
            '''
            if bin_name == 'facter' and not opt_dirs:
                return '/usr/bin/facter'

# Generated at 2022-06-13 02:02:53.962407
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    """test collect method of class FacterFactCollector
    """
    import re
    import json

    # A sample output of facter --puppet --json

# Generated at 2022-06-13 02:03:04.026924
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    import ansible.module_utils.facts.collector

    module = ansible.module_utils.facts.collector.BaseFactCollector.module
    assert module is not None
    assert isinstance(module, ansible.module_utils.basic.AnsibleModule)

    facter_fact_collector = ansible.module_utils.facts.collector.FacterFactCollector()
    assert facter_fact_collector is not None

    # Test method with a facter_output value
    facter_output = facter_fact_collector.get_facter_output(module)
    assert facter_output is not None

    # Test method without a facter_output value
    facter_path = module.get_bin_path('facter', opt_dirs=['/opt/puppetlabs/bin'])


# Generated at 2022-06-13 02:03:12.570404
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(
        argument_spec=dict()
    )

    fact_collector = FacterFactCollector()
    facter_path = fact_collector.find_facter(module)
    assert facter_path is not None

    module.params['ansible_system'] = None
    module.params['ansible_distribution'] = None
    facter_path = fact_collector.find_facter(module)
    assert facter_path is None

    module.params['ansible_system'] = 'Windows'
    module.params['ansible_distribution'] = 'CumulusLinux'
    facter_path = fact_collector.find_facter(module)
    assert facter_path is None


# Generated at 2022-06-13 02:03:13.901697
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    FacterFactCollector.find_facter()


# Generated at 2022-06-13 02:03:23.879915
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    from ansible.module_utils.facts.collector import BaseFactCollector
    module = BaseFactCollector.ANSIBLE_MODULE
    facter_fact_namespace = FacterFactCollector()

    # test when facter is not installed
    assert facter_fact_namespace.get_facter_output(module) is None

    # test when facter is installed and facter command returns facter data
    class FakeModule:
        def get_bin_path(self, name, opt_dirs=[]):
            return '/usr/bin/facter'

        def run_command(self, cmd):
            return 0, '{"facter_test": ["facter data"]}', ''

    module = FakeModule()
    facter_fact_namespace = FacterFactCollector()

# Generated at 2022-06-13 02:03:24.429554
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    pass

# Generated at 2022-06-13 02:03:31.489748
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    class TestModule:
        def __init__(self, return_values):
            self.return_values = return_values
            self.run_command_count = 0

        def get_bin_path(self, name, opt_dirs=None):
            return self.return_values[self.run_command_count]

    test_module = TestModule(return_values=['/bin/facter', '/bin/cfacter'])
    facter_path = FacterFactCollector(module=test_module).find_facter(module=test_module)

    assert facter_path == '/bin/cfacter'
    test_module.run_command_count += 1

    test_module = TestModule(return_values=['/bin/facter', '/bin/cfacter'])
    facter_path = FacterFactCollect

# Generated at 2022-06-13 02:03:42.917100
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    from ansible.module_utils.facts.utils import override_module_utils

    # Patch ansible.module_utils.facts.utils.is_container()
    # and make it always return False
    MOCK_DEFAULT = {
        'ansible.module_utils.facts.utils.is_container':
        lambda: False,
    }
    with override_module_utils(MOCK_DEFAULT):
        facter_collector = FacterFactCollector()

    # Patch ansible.module_utils.facts.utils.is_container()
    # and make it always return True
    MOCK_CONTAINER = {
        'ansible.module_utils.facts.utils.is_container':
        lambda: True,
    }
    with override_module_utils(MOCK_CONTAINER):
        facter_collector

# Generated at 2022-06-13 02:03:50.320514
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():

    # Mock class for module
    class MockModule(object):

        def __init__(self):
            self.bin_path = '/usr/bin'

        def get_bin_path(self, app, opt_dirs=None, required=False):
            path = self.bin_path + '/' + app
            return path

        # mock function that runs an external process, can be used to
        # return a known response
        def run_command(self, command):
            if command.startswith('/usr/bin/facter'):
                return 0, "{\"osfamily\": \"RedHat\"}", ''

        def _fail_json(self, msg):
            print(msg)

    # create an instance of the MockModule class
    mock_module = MockModule()

    # create an instance of the FacterFactCollector class,

# Generated at 2022-06-13 02:03:58.014976
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    import os
    import ansible.module_utils.facts.collector
    class MockedModule(object):
        def __init__(self):
            self.path = None
            self.args = ['facter', '--json']
            self.run_command_mock = MockedModule.run_command
            self.get_bin_path_mock = MockedModule.get_bin_path

        @staticmethod
        def run_command(path, args):
            if path == MockedModule.path:
                return 0, '', ''
            else:
                return 1, '', ''


# Generated at 2022-06-13 02:04:27.527823
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    module = {
        'get_bin_path': lambda *args, **kwargs: '/usr/bin/facter',
        'run_command': get_command,
    }

    facter_dict = FacterFactCollector().collect(module)

    assert facter_dict['facter_bios_release_date'] == '12/01/2006'
    assert facter_dict['facter_uptime_seconds'] == '175664'
    assert facter_dict['facter_os']['distro']['codename'] == 'trusty'
    assert facter_dict['facter_os']['family'] == 'Debian'
    assert facter_dict['facter_os']['distro']['description'] == 'Ubuntu 14.04 LTS'

# Generated at 2022-06-13 02:04:32.747367
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    from ansible.module_utils import basic
    from ansible.module_utils.facts.collector import FactsCollector
    from ansible.module_utils.facts import namespace

    m = basic.AnsibleModule(
        argument_spec={},
        supports_check_mode=False,
        add_file_common_args=False,
    )
    fact_collector = FactsCollector(module=m,
                                    collectors=[FacterFactCollector])
    collected_facts = fact_collector.collect()

    assert 'facter_os' in collected_facts
    facter_fact = collected_facts['facter_os']
    assert facter_fact['name'] == 'Linux'

# Generated at 2022-06-13 02:04:35.392165
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    from ansible.module_utils.facts.collector import BaseFactCollector

    module = BaseFactCollector()
    facter_path = FacterFactCollector.find_facter(module)
    assert facter_path is not None

# Generated at 2022-06-13 02:04:41.315179
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    # test with facter_path = None
    facter = FacterFactCollector()
    output = facter.get_facter_output({})
    assert output == None

    # test with facter_path = './does/not/exist'
    output = facter.get_facter_output({'get_bin_path': lambda x: './does/not/exist'})
    assert output == None

    # test with facter_path = './ok' and 'ok' command output = 'facter'
    def mock_run_command(*args, **kwargs):
        return 0, 'facter', ''
    output = facter.get_facter_output({'get_bin_path': lambda x: './ok', 'run_command': mock_run_command})
    assert output == 'facter'

   

# Generated at 2022-06-13 02:04:51.917995
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    from ansible.module_utils.facts import ModuleFactsCollector
    from ansible.module_utils.facts import CommandGenericFactCollector
    import ansible.module_utils.facts.namespace
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.system.facter
    import ansible.module_utils.facts.system.command_generic

    class TestModule:
        def __init__(self, bin_paths):
            self.bin_paths = bin_paths

        def get_bin_path(self, *args, **kwargs):
            return self.bin_paths[args[0]]


# Generated at 2022-06-13 02:04:59.381959
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    import ansible.module_utils.facts.collector
    # mock ansible.module_utils.facts.collector.get_bin_path
    import mock
    get_bin_path = mock.MagicMock()
    get_bin_path.return_value = '/opt/puppetlabs/bin/facter'
    ansible.module_utils.facts.collector.get_bin_path = get_bin_path

    facter_collector = FacterFactCollector()

    # mock ansible.module_utils.facts.collector.AnsibleModule
    import mock
    class AnsibleModule:
        pass
    ansible_module = AnsibleModule()
    # mock ansible_module.get_bin_path
    get_bin_path = mock.MagicMock()
    get_bin_path.return_

# Generated at 2022-06-13 02:05:09.603754
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    '''
    test_FacterFactCollector_find_facter checks that the method find_facter of
    class FacterFactCollector returns None when no facter nor cfacter was found
    and returns the path to the right facter or cfacter binary when one of these
    is found.
    '''
    class MockModule:
        def get_bin_path(self, cmd, opt_dirs=None):
            if cmd == 'facter':
                return '/tmp/facter'
            elif cmd == 'cfacter':
                return '/tmp/cfacter'
            else:
                return None

    facter = FacterFactCollector()
    assert facter.find_facter(MockModule()) == '/tmp/cfacter'
    facter = FacterFactCollector()

# Generated at 2022-06-13 02:05:11.286756
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    m = AnsibleModule()
    fc = FacterFactCollector(namespace=None, collectors=None)
    res = fc.collect(module=m)
    assert isinstance(res, dict)

# Generated at 2022-06-13 02:05:17.545130
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    test_object = FacterFactCollector()

    class TestModule(object):
        def run_command(self, cmd):
            return (0, None, None)
        def get_bin_path(self, *args, **kwargs):
            return None

    test_module = TestModule()
    out = test_object.get_facter_output(test_module)

    assert out is None


# Generated at 2022-06-13 02:05:25.368307
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():
    import ansible.module_utils.facts.collector as collector
    import ansible.module_utils.facts.namespace as namespace
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils._text import to_bytes

    facter_collector = FacterFactCollector(namespace=namespace.BasePersistentNamespace())

    class FakeModule:
        def get_bin_path(self, executable, opt_dirs=[]):
            import os
            import os.path
            mydir = os.path.dirname(os.path.abspath(__file__))
            return os.path.join(mydir, '../../../../../../test/unit/module_utils/legacy/facter/facter_mock')


# Generated at 2022-06-13 02:06:18.396750
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    class MockModule:
        def get_bin_path(self, path, opt_dirs=[]):
            return '/bin/test/facter'

        def run_command(self, path):
            return 0, '{"a":"b"}', ''

    class MockFacts:
        pass

    moduleMock = MockModule()
    factNamespace = PrefixFactNamespace(namespace_name='facter',
                                        prefix='facter_')
    facts = MockFacts()
    facts.facter = {}

    assert FacterFactCollector(namespace=factNamespace).collect(module=moduleMock, collected_facts=facts) == {
            'facter_a': 'b'
        }

# Generated at 2022-06-13 02:06:27.474800
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    # Create the object FacterFactCollector and test the method collect
    facter_dict = FacterFactCollector()
    # if find_facter return None, return empty dict
    assert facter_dict.find_facter() == None
    assert facter_dict.collect() == {}
    # if get_facter_output return None, return empty dict
    class Module():
        def __init__(self):
            self.bin_path = None
        def get_bin_path(self, bin_name, opt_dirs):
            return self.bin_path

        def run_command(self, command):
            return None, None, None
    module_object = Module()
    module_object.bin_path = None
    facter_dict = FacterFactCollector()
    assert facter_dict.get_facter

# Generated at 2022-06-13 02:06:32.487177
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    class MockModule(object):
        def get_bin_path(self, facter, opt_dirs=[]):
            return "/usr/bin/facter"

    facter_fact_collector = FacterFactCollector(collectors=[])
    facter_path = facter_fact_collector.find_facter(MockModule())

    assert facter_path == "/usr/bin/facter"

# Generated at 2022-06-13 02:06:41.981132
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    from ansible.module_utils.facts.collector import MockModule
    from ansible.module_utils.facts.collector import MockFile
    from ansible.module_utils.facts import namespaces
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat import unittest
    import sys
    import os

    class MockFacterFactCollector(FacterFactCollector):
        def find_facter(self, module):
            return None


# Generated at 2022-06-13 02:06:51.086703
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    try:
        import ansible.module_utils.facts.facts
    except TypeError:
        import ansible.module_utils.facts.facts as facts

    from ansible.module_utils.facts.collector import NamespacePrefixFactCollector
    from ansible.module_utils.facts import default_collectors

    # Test that the module produces output, and that it has the expected format
    fact_names = set()

    fact_collector = NamespacePrefixFactCollector('facter', fact_names)
    output = fact_collector.collect(default_collectors())

    assert isinstance(output, dict)
    assert isinstance(output['ansible_facts'], dict)
    assert isinstance(output['ansible_facts']['facter'], dict)

# Generated at 2022-06-13 02:06:54.505356
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    collector = FacterFactCollector()
    facter_dict = collector.collect()
    assert facter_dict is not None, "FacterFactCollector.collect returned no data"
    assert isinstance(facter_dict, dict) and len(facter_dict) > 0, "FacterFactCollector.collect returned an empty dict"



# Generated at 2022-06-13 02:06:59.891812
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    module = type('module', (), {})
    module.run_command = lambda cmd: (0, '{"uptime": {"seconds": 123}}', '')
    module.get_bin_path = lambda path, opt_dirs=None: '.'

    collector = FacterFactCollector()
    facts = collector.collect(module)
    assert facts == {'facter_uptime_seconds': 123}


# Generated at 2022-06-13 02:07:07.176145
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():
    from ansible.module_utils import basic
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils.facts.collector.facter import FacterFactCollector

    ansible_mock = basic.AnsibleModule(argument_spec={},
                                       bypass_checks=True)
    ansible_mock.params = {}

    # Mock the facter class
    class FacterMock:
        def __init__(self):
            pass

        @staticmethod
        def list_external_facts():
            return {}

    FacterFactCollector.facter_instance = FacterMock()
    # Mock the facter path
    FacterFactCollector.find_facter = lambda self, module: '/usr/bin/facter --puppet --json'

    facter = Facter

# Generated at 2022-06-13 02:07:17.501007
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():

   from ansible.module_utils.facts.collector import FactsCollector
   from ansible.module_utils.facts.collector import BaseFactCollector
   from ansible.module_utils.facts.collector import FactCache
   from ansible.module_utils.facts.facts import FactManager
   from ansible.module_utils.facts.namespace import PrefixFactNamespace
   from ansible.module_utils.facts.utils import get_file_lines
   from ansible.module_utils._text import to_bytes

   ###########################################################################
   # Mock Module class
   ###########################################################################

   class MockModule:

       # Set global var
       facter_output = None


# Generated at 2022-06-13 02:07:18.802102
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    facter_path = FacterFactCollector().find_facter('/path/to/bin/facter')
    assert facter_path == '/path/to/bin/facter'
