

# Generated at 2022-06-13 01:58:49.074832
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():
    lines = ''
    with open('test_facter') as f:
        lines = f.read()
    res = FacterFactCollector().run_facter('', '')
    assert res[1] == lines



# Generated at 2022-06-13 01:58:57.169819
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    import ansible.module_utils.facts.collector as collector
    import ansible.module_utils.facts.namespace as namespace
    import ansible.module_utils.facts.system as system

    facts_dict = {'foo': 'bar'}
    facts_namespace = namespace.PrefixFactNamespace(
        namespace_name='test',
        prefix='test_')

    # mock the fact collector to return a known result
    class MockFactCollector(collector.BaseFactCollector):
        name = 'MockFactCollector'
        _fact_ids = set(['test'])
        def collect(self, module=None, collected_facts=None):
            return facts_dict

    local_fact_collector = MockFactCollector(namespace=facts_namespace)

# Generated at 2022-06-13 01:58:59.735315
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    module = None
    facter_output = FacterFactCollector().get_facter_output(module)
    assert facter_output is None

# Generated at 2022-06-13 01:59:06.713465
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    from ansible.module_utils.facts import ModuleUtilsLegacyFactCollector
    fc = FacterFactCollector(collectors=[ModuleUtilsLegacyFactCollector])

    # TODO: mock module obj? mgmt_server? not sure how to.
    #fact_collector = FacterFactCollector(module=module)
    #facter_output = fact_collector.get_facter_output()
    #assert facter_output is not None



# Generated at 2022-06-13 01:59:17.086122
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():
    from ansible.module_utils.facts.legacy import Facts
    from ansible.module_utils._text import to_text

    class MockedModule:
        def __init__(self):
            pass

        def get_bin_path(self, *args, **kwargs):
            return "/opt/puppetlabs/bin/facter"


# Generated at 2022-06-13 01:59:25.852528
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():
    from ansible.module_utils.facts.collector import FactsCollector

    module = AnsibleModuleMock()
    module.run_command = AnsibleModuleMock.run_command
    facter_path = module.get_bin_path('facter')

    facter_collector = FacterFactCollector()

    rc, out, err = facter_collector.run_facter(module, facter_path)

    assert rc == 0, 'The rc should be 0.'
    assert isinstance(out, str), 'facter_output should be a string.'
    assert isinstance(err, str), 'The err should be a string.'



# Generated at 2022-06-13 01:59:31.814407
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    class Module(object):
        def run_command(self):
            return 0, u'{ "facter_version": "3.7.1", "virtual": "kvm" }', ''
        def get_bin_path(self, **kwargs):
            return '/opt/puppetlabs/bin/facter'

    module = Module()
    collector = FacterFactCollector()

    facter_output = collector.get_facter_output(module)
    assert facter_output is not None
    assert facter_output == '{ "facter_version": "3.7.1", "virtual": "kvm" }'

# Generated at 2022-06-13 01:59:41.593810
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    import unittest
    import os

    class TestFacterFactCollector(unittest.TestCase):
        """
        Test to ensure that the FacterFactCollector.get_facter_output method
        returns the appropriate data.
        """
        def setUp(self):
            self.collector = FacterFactCollector()
            self.module = AnsibleModule(
                argument_spec={},
                supports_check_mode=True
            )

            class ModuleMock(object):
                def __init__(self):
                    self.params = {}

                def get_bin_path(self, tool, opt_dirs=None):
                    self.get_bin_path.called += 1


# Generated at 2022-06-13 01:59:44.285033
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    module = MockModule()
    facter_path = "/usr/bin/facter"
    module.set_bin_path(path=facter_path)
    facter_collector = FacterFactCollector()
    assert facter_collector.find_facter(module) == facter_path

test_results = '{"test": "results"}'



# Generated at 2022-06-13 01:59:53.517604
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    """
    AnsibleModule object has a method run_command that can be mocked in order to validate the
    behaviour of method run_facter as well as method get_facter_output of class FacterFactCollector.
    The run_command method is not mocked for the test_FacterFactCollector_collect unit test in the same
    module because that test is rather checking that the actual facter command is executed, whereas this
    unit test is rather checking the output of method get_facter_output.
    """
    from ansible.module_utils.facts.collector.facter import FacterFactCollector
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six.moves import StringIO


# Generated at 2022-06-13 02:00:04.918684
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    from ansible.module_utils.facts.collector import ModuleStub
    from ansible.module_utils.facts.collector import FactsCollectionStub

    module = ModuleStub()
    collector = FacterFactCollector()

    facts = FactsCollectionStub([], module)
    facter_path = collector.find_facter(module)

    fact_id = 'facter'
    fact_name = 'facter'
    fact_data = facter_path
    fact_source = 'FacterFactCollector'

    facts_dict = {'facter': facter_path}
    facts.append(fact_id, fact_name, fact_data, fact_source)

    # Test facts collection
    assert facter_path == fact_data
    assert facts_dict == facts.facts_dict

# Generated at 2022-06-13 02:00:08.038409
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    collectors = [FacterFactCollector()]
    facts = {}
    for collector in collectors:
        facts.update(collector.collect(module=None, collected_facts=facts))
        print(facts)


# Generated at 2022-06-13 02:00:18.924105
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.utils
    import ansible.module_utils.facts.cache
    class fake_module:
        def get_bin_path(self, name, opt_dirs=[]):
            if name == 'facter':
                return '/some_path/facter'
            elif name == 'cfacter':
                return '/some_other_path/cfacter'
            else:
                return None
    ffc = FacterFactCollector()
    facter_path = ffc.find_facter(fake_module())
    assert facter_path == '/some_other_path/cfacter'


# Generated at 2022-06-13 02:00:29.194106
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule
    import os

    class Mock_get_bin_path(object):
        def __init__(self, return_value):
            self.return_value = return_value

        def __call__(self, arg1, arg2=None):
            return self.return_value

    class Mock_Module(object):
        def __init__(self, *args, **kwargs):
            self.params = {}
            self.args = {}
            self.exit_args = {}
            self.fail_json = {}
            self.run_command_return_value = None
            if 'run_command_return_value' in kwargs.keys():
                self.run_command_return_value = kwargs

# Generated at 2022-06-13 02:00:35.779496
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    # Mock Module class
    module = MockModule()
    module.get_bin_path.return_value = 'facter'
    module.run_command.return_value = (0, '{ "fact1": "value1", "fact2": "value2" }', '')
    fac = FacterFactCollector()
    facter_output = fac.get_facter_output(module)
    assert(facter_output == '{ "fact1": "value1", "fact2": "value2" }')

# Generated at 2022-06-13 02:00:44.957089
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    """Test the find_facter and run_facter methods of the
    FacterFactCollector class, which is used to collect Facter facts.
    """

    try:
        from ansible.module_utils.facts import Collector, namespace_manager
    except ImportError:
        from ansible.module_utils.facts.collector import Collector, namespace_manager

    class FakeModule(object):
        def __init__(self):
            self.params = {'gather_subset': []}

        def get_bin_path(self, binary, opt_dirs=None, required=False):
            if binary == 'facter':
                return '/usr/bin/facter'
            elif binary == 'cfacter':
                return None
            return '/usr/bin/which'


# Generated at 2022-06-13 02:00:50.976023
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    module = Mock()
    module.run_command.return_value = 0, '{ "test": "test" }', ''
    facter_path = 'test/path/'
    f = FacterFactCollector()
    f.find_facter = Mock(return_value=facter_path)
    assert f.get_facter_output(module) == '{ "test": "test" }'


# Generated at 2022-06-13 02:01:00.171052
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    from ansible.module_utils.facts.system.base import BaseFactCollector

    facter_output = """{
        "blockdevice_xvda_model": "",
        "operatingsystem": "Debian",
        "dmi_system_product_name": "Google Compute Engine",
        "role": "",
        "domain": "cs.washington.edu",
        "blockdevice_xvda_vendor": "",
        "dmi_system_manufacturer": "Google"
    }"""

    def find_facter_mock():
        return "/usr/bin/facter"

    def run_facter_mock(facter_path):
        return 0, facter_output, ''

    module = MagicMock()


# Generated at 2022-06-13 02:01:05.945729
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():
    collector = FacterFactCollector()
    class FakeModule:
        def get_bin_path(self, path, opt_dirs):
            return '/usr/bin/facter'
        def run_command(self, command):
            return 0, "{\"somefactname\":\"somefactvalue\"}", ""

    testModule = FakeModule()
    result = collector.run_facter(testModule, "/usr/bin/facter")
    assert(result == (0, "{\"somefactname\":\"somefactvalue\"}", ""))


# Generated at 2022-06-13 02:01:12.652093
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    facter_collector = FacterFactCollector()

    collected_facts = {}

    class FakeModule():
        def __init__(self):
            self._bin_paths = {}
            self._bin_paths_cache = {}

        def get_bin_path(self, name, opt_dirs=None):
            if name in self._bin_paths:
                return self._bin_paths[name]

            return None

        def run_command(self, cmd):
            if cmd.strip() == '/usr/bin/facter --puppet --json':
                return 0, '{"facter": "true"}', None
            else:
                return 1, '', None

    fake_module = FakeModule()

    # sample ansible_facts
    ansible_facts = {}

    # When I run facter collector with

# Generated at 2022-06-13 02:01:25.050033
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.error import FactCollectorUnsupportedError
    from ansible.module_utils._text import to_bytes
    try:
        from ansible.module_utils.facts.collector import BaseFactCollector
        from ansible.module_utils.facts.error import FactCollectorUnsupportedError
        from ansible.module_utils._text import to_bytes
    except ImportError:
        base_fact_collector = None
    else:
        base_fact_collector = BaseFactCollector

    class FakeModule(object):
        def __init__(self):
            self.fail_json = lambda **kwargs: exit(1)


# Generated at 2022-06-13 02:01:32.136743
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    # Test with successful output of facter
    module = FacterFactCollector()
    module.run_command = mock_run_command_output_facter_json

# Generated at 2022-06-13 02:01:42.586396
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    # mock module
    class MockModule:
        def get_bin_path(self, arg1, opt_dirs):
            return "/usr/bin/facter"

        def run_command(self, arg):
            return 0, '{"kernel":"Linux", "kernelrelease":"3.16.0-4-amd64", "sysname":"Linux"}', ''

        class AnsibleModule:
            class params:
                ansible_host = "host.example.com"

    class MockCollectedFacts:
        pass

    mock_module = MockModule()
    mock_collected_facts = MockCollectedFacts()
    # end of mock module

    facter_collector = FacterFactCollector([], namespace='facter')

# Generated at 2022-06-13 02:01:51.350209
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    from ansible.module_utils.facts.collector import FacterFactCollector, BaseFactCollector

    facter = FacterFactCollector()

    class Module:
        def get_bin_path(self, name, opt_dirs=None, required=False):
            if name == 'facter':
                return '/usr/bin/facter'
            if name == 'cfacter':
                return '/opt/puppetlabs/bin/cfacter'
            return None

    module = Module()
    facter_path = facter.find_facter(module)
    assert facter_path == '/opt/puppetlabs/bin/cfacter'


# Generated at 2022-06-13 02:01:57.112366
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    class fake_module(object):
        def get_bin_path(self, candidate, opt_dirs):
            if candidate == 'cfacter':
                return '/opt/puppetlabs/bin/cfacter'
            if candidate == 'facter':
                return '/opt/puppetlabs/bin/facter'
            return None

    m = fake_module()
    f = FacterFactCollector()
    facter_path = f.find_facter(m)
    assert facter_path == '/opt/puppetlabs/bin/cfacter'


# Generated at 2022-06-13 02:02:08.310113
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    class TestModule:
        def __init__(self):
            self.path = '/usr/local/bin:/usr/bin:/bin'
            self.params = {}

        def get_bin_path(self, path, opt_dirs=[]):
            if path == 'facter':
                return '/usr/bin/facter'
            else:
                return None


# Generated at 2022-06-13 02:02:09.748250
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    from ansible.module_utils.facts.collector import get_collector_instance
    get_collector_instance("FacterFactCollector").find_facter()

# Generated at 2022-06-13 02:02:19.701780
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    from ansible.module_utils.facts import collector
    import ansible.module_utils.facts.collector

    # The methods calls get_bin_path on module, which is not fakeable.
    # We use the real module class, but stub out run_command
    module = ansible.module_utils.facts.collector.BaseFactCollector.module
    def run_command_stub(cmd, **args):
        return 0, '', ''
    module.run_command = run_command_stub

    facter_fact_collector = collector.get_collector('facter')
    facter_output = facter_fact_collector.get_facter_output(module)
    assert facter_output is not None
    assert facter_output.startswith('{')
    assert facter_output.endsw

# Generated at 2022-06-13 02:02:24.100135
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    module = MockModule()
    bin_dirs = ['/bin', '/sbin', '/usr/bin', '/usr/sbin', '/usr/local/bin', '/usr/local/sbin', '/opt/puppetlabs/bin']
    if module.which(None, bin_dirs):
        assert True
    else:
        assert False


# Generated at 2022-06-13 02:02:33.834487
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    facter_fact_collector = FacterFactCollector()

    # Tests if a facter executable is found on path
    # noinspection PyUnusedLocal
    def find_facter_mock(*args):
        return 'mock_facter'
    facter_fact_collector.find_facter = find_facter_mock

    # Set up a module which has a facter executable on its path
    # noinspection PyUnusedLocal
    def path_exists_mock(path):
        if path == 'mock_facter':
            return True
        return False
    module = MockModule()
    module.path_exists = path_exists_mock
    module.run_command = run_mock_facter_run_command


# Generated at 2022-06-13 02:02:54.996128
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    import os
    import tempfile
    import pytest
    import json

    with tempfile.NamedTemporaryFile(mode='w', delete=False) as json_mock:
        tmp_json_mock = json_mock.name
        print("""
{
  "kernel": "Linux",
  "kernelmajversion": "4.4"
}
""".format(), end='', file=json_mock)

    # create a module mock
    class FacterModule:
        def get_bin_path(self, executable, opt_dirs=[]):
            if executable == 'facter':
                return tmp_json_mock
            return None


# Generated at 2022-06-13 02:03:03.037295
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    # Initialize a TestModule class object
    m = TestModule()
    # Set the find_facter_outcome to the TestModule object
    m.find_facter_outcome = '/usr/bin/facter'
    # Initialize the FacterFactCollector class object
    f = FacterFactCollector()
    # Call the get_facter_output method of the FacterFactCollector object
    # with the TestModule object as argument
    f.get_facter_output(m)
    # Check the outcome of the method
    assert m.command_executed == "/usr/bin/facter --puppet --json"


# Generated at 2022-06-13 02:03:09.950412
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    '''
    Test to verify the Facter fact collector's find_facter method returns
    puppet's or puppetlabs' facter binary, if installed.
    '''
    module_mock = Mock()
    facter_instance = FacterFactCollector()
    module_mock.get_bin_path.return_value = '/bin/facter'
    facter_path = facter_instance.find_facter(module_mock)
    expected_facter_path = '/bin/facter'

    assert facter_path == expected_facter_path


# Generated at 2022-06-13 02:03:10.841343
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    pass



# Generated at 2022-06-13 02:03:11.363020
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    pass

# Generated at 2022-06-13 02:03:21.873578
# Unit test for method collect of class FacterFactCollector

# Generated at 2022-06-13 02:03:28.440462
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    ffc = FacterFactCollector(module=None)
    assert not ffc.get_facter_output(None)

    class module_mock:
        def __init__(self):
            self.run_command_results = [
                (0, b'{"facterversion":"2.4.6"}', b''),
                (2, b'', "facter: command not found"),
                (1, b'', ""),
            ]

        def get_bin_path(self, _name, _opt_dirs=None, required=False):
            if required:
                return "/bin/facter"
            return "/bin/facter"

        def run_command(self, _command, _check_rc=True):
            return self.run_command_results.pop()

    assert ffc.get_f

# Generated at 2022-06-13 02:03:39.056719
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    test = FacterFactCollector()
    # Test with a module that only knows how to run facter
    # Return value will be a dict of facter facts
    sample_module = object()

    class MockModule(object):
        @staticmethod
        def run_command(command, check_rc=True):
            # Return sample facter facts
            return 0, "{\"puppetversion\":\"3.7.3\",\"facterversion\":\"1.7.5\"}", ""

        @staticmethod
        def get_bin_path(binary_name, opt_dirs=None):
            return True

    sample_module.run_command = MockModule.run_command
    sample_module.get_bin_path = MockModule.get_bin_path


# Generated at 2022-06-13 02:03:45.665131
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():
    class Module:

        def get_bin_path(self, name, opt_dirs):
            return '/bin/' + name

        def run_command(self, cmd):
            return -1, '', ''

    module = Module()
    facter_path = FacterFactCollector().find_facter(module)
    assert facter_path is '/bin/cfacter'
    rc, out, err = FacterFactCollector().run_facter(module, facter_path)
    assert rc is -1

# Generated at 2022-06-13 02:03:51.897302
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    import os
    import tempfile

    try:
        import ansible.module_utils.facts.collector
        import ansible.module_utils.facts.hardware
        import ansible.module_utils.facts
    except ImportError:
        import ansible.module_utils.facts.collector
        import ansible.module_utils.facts.hardware
        import ansible.module_utils.facts
    import ansible.module_utils.facts.collectors.facter

    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collectors.facter import FacterFactCollector
    from ansible.module_utils.facts.hardware import Hardware
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    # Create a temporary directory


# Generated at 2022-06-13 02:04:18.411306
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    from ansible.module_utils.facts import ansible_facts
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils._text import to_text
    import ansible.module_utils.facts.collectors.facter as ans_mod

    ansible_facts.clear()
    get_collector_instance(ans_mod.FacterFactCollector)

    # TODO: figure out how to mock module.run_command
    # TODO: figure out how to mock module.get_bin_path


# Generated at 2022-06-13 02:04:24.832952
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    # Define test variables
    true_path = '/opt/puppetlabs/bin/facter'
    true_path_cfacter = '/opt/puppetlabs/bin/cfacter'
    false_path = ''
    false_path_cfacter = ''

    # Define mock module
    class MockModule(object):
        @staticmethod
        def get_bin_path(app, opt_dirs=None):
            if app == 'facter':
                return true_path
            if app == 'cfacter':
                return true_path_cfacter

    # Attempt to find facter
    facter_path = FacterFactCollector.find_facter(MockModule())
    assert(facter_path == true_path_cfacter)

    # Attempt to find facter
    facter_path = FacterFact

# Generated at 2022-06-13 02:04:32.544305
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    from ansible.module_utils.facts.collector.facter import FacterFactCollector
    from ansible.module_utils.facts.utils import ModuleFinder
    from ansible.module_utils.facts.utils import ModuleLoader
    ffc = FacterFactCollector()
    mf = ModuleFinder()
    ml = ModuleLoader()

    class FakeModule(object):
        def __init__(self, bin_path=None, run_command=None):
            self.__bin_path = bin_path
            self.__run_command = run_command

        # mock ansible.module_utils.facts.utils.ModuleFinder.get_bin_path
        def get_bin_path(self, *args, **kwargs):
            return self.__bin_path

        # mock ansible.module_utils.facts.

# Generated at 2022-06-13 02:04:36.821873
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():
    module = None
    ft = FacterFactCollector(module) 
    module = None
    facter_path = None
    xfacter_path = None
    rc, out, err = ft.run_facter(module, facter_path)
    assert rc == 0
    facter_path = None
    rc, out, err = ft.run_facter(module, facter_path)
    assert rc == 0

# Generated at 2022-06-13 02:04:42.771929
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    import ansible.module_utils.facts.collectors.facter as t_facter

    module_obj = object()
    t_facter.get_bin_path = lambda self, a: 'a'

    t_collector = t_facter.FacterFactCollector(module=module_obj)
    t_path = t_collector.find_facter(module_obj)
    assert t_path == 'a'

# Generated at 2022-06-13 02:04:46.193289
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    module = None
    collected_facts = None
    facter_collector = FacterFactCollector(collectors=None, namespace=None)
    facter_dict = facter_collector.collect(module, collected_facts)
    assert isinstance(facter_dict, dict)

# Generated at 2022-06-13 02:04:48.900966
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    module = MockModule()
    f = FacterFactCollector()
    facter_path = f.find_facter(module)
    assert facter_path is None


# Generated at 2022-06-13 02:04:56.246889
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    # This is the simplest way to mock a module
    class MockModule(object):
        def get_bin_path(self, executable, opt_dirs=None):
            return '/bin/' + executable
        def run_command(self, command):
            return 0, '{"foo":"bar", "uptime_seconds":42}', ''

    facter = FacterFactCollector()
    mock_module = MockModule()
    facter_output = facter.get_facter_output(mock_module)
    assert facter_output == '{"foo":"bar", "uptime_seconds":42}'



# Generated at 2022-06-13 02:05:07.633383
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    class MockModule():
        def __init__(self, rc, out, err):
            self.rc = rc
            self.out = out
            self.err = err

        # FIXME: should we name rc/out/err to something else?
        def run_command(self, cmd):
            return self.rc, self.out, self.err

        def get_bin_path(self, bin, opt_dirs):
            # We have facter 3.6.2 installed in /opt/puppetlabs/bin
            # cfacter is just a symlink to /opt/puppetlabs/bin/facter
            if bin == 'facter':
                return '/opt/puppetlabs/bin/facter'

# Generated at 2022-06-13 02:05:18.703735
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():

    import tempfile
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts import module


# Generated at 2022-06-13 02:06:12.697506
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.utils import get_file_lines
    from ansible.module_utils.facts.utils.files import file_exists

    # Create temporary file
    tmp_fact_file = 'tmp_fact_file'

    # Create temporary facter config file
    with open(tmp_fact_file, 'w+') as fd:
        fd.write('{"ipaddress": "192.168.1.1"}')

    # Create a FacterFactCollector instance
    facter_collector = FacterFactCollector()

    # Check the output of FacterFactCollector._run_facter()

# Generated at 2022-06-13 02:06:22.214336
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    '''
    Test get_facter_output method of class FacterFactCollector
    '''
    def mock_module_run_command(command):
        '''
        Fake the run_command method of module object (used inside the method
        get_facter_output of class FacterFactCollector)
        Return a faked output for the command 'facter --puppet --json'
        '''
        if command == 'facter --puppet --json':
            out = '{"facter": {"a": 1, "b": "2"}}'
            return 0, out, ''
        elif command == 'cfacter --puppet --json':
            out = '{"facter": {"a": 1, "b": "2"}}'
            return 0, out, ''

        return None, None, None


# Generated at 2022-06-13 02:06:32.068990
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    from ansible.module_utils import basic
    import os
    import mock
    import json

    def my_run_command(self, args, check_rc=True):
        return 0, os.path.join(os.path.dirname(__file__),"facter_json.txt"), ""

    m = mock.mock_module.MockModule(basic._ANSIBLE_ARGS)
    m.run_command = my_run_command
    f = FacterFactCollector()
    facter_output = f.get_facter_output(m)
    json_facter_output = json.dumps(json.load(open(os.path.join(os.path.dirname(__file__),"facter_json.txt"))))
    assert facter_output == json_facter_output

# Generated at 2022-06-13 02:06:41.664896
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    # Arrange
    module_mock = MockModule()
    facter_output = '{"facterversion":"2.5.1","os":{"family":"RedHat","hardware":"x86_64","name":"RedHat","release":{"full":"7.3","major":"7","minor":"3"}},"osfamily":"RedHat","path":"/usr/local/bin:/usr/bin:/bin","ruby":{"platform":"x86_64-linux","sitedir":"/usr/local/lib64/site_ruby/devel/puppet","version":"2.0.0"},"selinux":{"config_mode":"enforcing","current_mode":"enforcing","config_policy":"targeted","enforced":true,"policy_version":"28"}}'

    class find_facter_mock:
        def __init__(self):
            self.times_called = 0



# Generated at 2022-06-13 02:06:50.795715
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    collector = FacterFactCollector()

    module = Mock()
    module.get_bin_path.return_value = None
    facter_path = collector.find_facter(module)
    assert facter_path is None

    module.get_bin_path.return_value = '/facter'
    facter_path = collector.find_facter(module)
    assert facter_path == '/facter'

    module.get_bin_path.return_value = None
    module.get_bin_path.side_effect = ['/facter', None]
    facter_path = collector.find_facter(module)
    assert facter_path == '/facter'

    module.get_bin_path.side_effect = ['/facter', '/cfacter']
    facter_path = collector.find_

# Generated at 2022-06-13 02:06:59.892168
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collector import get_collector_instance, get_collector_names

    collect_names = get_collector_names()
    assert 'facter' in collect_names

    # 1) Init Collector instance
    collector = Collector(collectors=reached_collect_names)
    # 2) Init FacterFactCollector instance
    facter_collector = get_collector_instance('facter', collectors=collector)

    # 3) Create test class which contains method get_bin_path
    class MockModule:
        class C:
            def __init__(self, config=None):
                self.DEFAULT_BIN_PATH = config

            def get(self, v):
                return self.DEFAULT_BIN_

# Generated at 2022-06-13 02:07:02.862942
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    from ansible.module_utils.facts.collector import get_collector_instance
    fact_collector = get_collector_instance(FacterFactCollector)
    facter_path = fact_collector.find_facter()
    assert facter_path is not None

# Generated at 2022-06-13 02:07:09.766400
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    from ansible.module_utils.facts import DefaultCollectors
    from ansible.module_utils._text import to_bytes, to_native
    import json
    import sys

    if sys.version_info.major >= 3:
        unicode = str
    else:
        import codecs

    # Create a test object to populate the collected facts
    module_args = dict(
        ansible_facts=dict(
            ansible_facter=dict(
                lsb=dict(
                    id="Debian",
                    release="8.0",
                    codename="jessie",
                    major_release="8",
                    distributor_id="Debian"
                )
            )
        )
    )

    # Create a MockModule that mocks the module argument parsing from CLI

# Generated at 2022-06-13 02:07:18.595486
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    # Create a Mock module
    module = type('MockAnsibleModule', (object,), dict(
        get_bin_path=lambda self, name, opt_dirs: '/opt/puppetlabs/bin/' + name,
        run_command=lambda self, cmd: (0, '{ "lsbdistdescription": "CentOS Linux release 7.2.1511 (Core)", "lsbdistrelease": "7.2", "lsbmajdistrelease": "7", "lsbdistcodename": "Core", "lsbdistid": "CentOS", "operatingsystem": "CentOS", "osfamily": "RedHat" }', ''),
        ))()

    facter_dict = FacterFactCollector().collect(module)

# Generated at 2022-06-13 02:07:25.994134
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    # pylint: disable=protected-access
    module = lambda **kwargs: None
    module.run_command = lambda *args, **kwargs: (0, 'json', '')

    f = FacterFactCollector([])
    f._find_facter = lambda x: 'facter'
    #f._get_facter_output = lambda x: 'json'
    facter = f.collect(module)
    assert facter['facter_somefact'] == 'somevalue'