

# Generated at 2022-06-13 01:58:52.270856
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    

# Generated at 2022-06-13 01:58:57.089107
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    import mock
    import tempfile
    import os

    # Mock AnsibleModule (returning only the module argument parsing)
    mock_module = mock.Mock()
    mock_module.params = {'collector_namespace': 'facter'}
    mock_module.run_command.return_value = (0, '', '')
    fake_facter_path = tempfile.mkstemp()[1]
    fake_cfacter_path = tempfile.mkstemp()[1]
    mock_module.get_bin_path.side_effect = lambda x: {
        # Make sure we return the fake paths when asked for them
        'facter': fake_facter_path,
        'cfacter': fake_cfacter_path
    }.get(x, None)

    # Create a new facter collector
   

# Generated at 2022-06-13 01:59:08.167527
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():

    import sys
    if sys.version_info[:2] <= (2, 6):
        try:
            import unittest2 as unittest
        except ImportError:
            print("You need to install unittest2 to run facter unit tests on python 2.6 or lower")
            raise
    else:
        import unittest

    from ansible.module_utils.facts import get_collector_instance


# Generated at 2022-06-13 01:59:11.713195
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    facter_path = FacterFactCollector().find_facter(None)
    assert facter_path is None


# Generated at 2022-06-13 01:59:19.529816
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    class Module(object):
        # Return empty value for calls to module.run_command()
        def run_command(self, path):
            return 0, '{}', 'stderr'

    class CollectedFacts(dict):
        def __init__(self):
            self.keys = []
            super(CollectedFacts, self).__init__()

        def __setitem__(self, key, value):
            self.keys.append(key)
            super(CollectedFacts, self).__setitem__(key, value)

    module = Module()
    facter_path = '/bin/facter'

    # Invalid path
    facter_collector = FacterFactCollector()
    facter_collector.find_facter = lambda x: None
    facter_collector.get_facter_

# Generated at 2022-06-13 01:59:29.322866
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    import ansible.module_utils.facts.collector
    from ansible.module_utils.facts.utils import get_file_content
    from ansible.module_utils._text import to_bytes

    module = ansible.module_utils.facts.collector.BaseFactCollector.module

    class MockModule(object):
        def __init__(self, module_path, bin_path, bin_path_c):
            self.module_path = module_path
            self.bin_path = bin_path
            self.bin_path_c = bin_path_c

        def get_bin_path(self, cmd, opt_dirs=None):
            if cmd == 'cfacter':
                return self.bin_path_c
            else:
                return self.bin_path


# Generated at 2022-06-13 01:59:38.545113
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():

    # mock module and get_bin_path
    # Note: Way of mocking of module is not perfect, but works for now
    #       This is only needed to mock the get_bin_path method of module
    class MockModule(object):
        def __init__(self, facter_path, facter_output):
            self.facter_path = facter_path
            self.facter_output = facter_output

        def get_bin_path(self, name, opt_dirs=[]):
            if name == 'facter' or name == 'cfacter':
                return self.facter_path

        def run_command(self, cmd):
            if self.facter_output:
                return 0, json.dumps(self.facter_output), ''

# Generated at 2022-06-13 01:59:46.988496
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    """
    Unit tests for the 'collect' method of class FacterFactCollector.
    """
    facter_fact_collector = FacterFactCollector()

    # Build test data

# Generated at 2022-06-13 01:59:52.495144
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    facter_path = '/opt/puppetlabs/bin/facter'
    module_mock = mock(get_bin_path=lambda binary, path=None, opt_dirs=None: facter_path if binary == 'facter' else None)
    collector = FacterFactCollector()
    facter_path_found = collector.find_facter(module_mock)
    assert facter_path_found == facter_path


# Generated at 2022-06-13 02:00:01.991689
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    import sys

    if sys.version_info[:2] == (2, 6):
        # unittest2 is needed because we are using skipIf/skipUnless
        import unittest2 as unittest
    else:
        import unittest

    class NullModule():

        def get_bin_path(self, cmd, opt_dirs=None):
            return '/bin/' + cmd

        def run_command(self, cmd):
            if cmd.endswith('facter --puppet --json'):
                return 0, '{"my_key": "my_value"}', None
            else:
                return 1, None, None


    class TestFacterCollector(unittest.TestCase):

        def test_collect(self):
            # If a module is not passed, an empty dict is returned
            ffc

# Generated at 2022-06-13 02:00:06.845443
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    facter_path = FacterFactCollector.find_facter(None)
    assert facter_path is not None


# Generated at 2022-06-13 02:00:11.412939
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    from ansible.module_utils.facts.utils import FactsCollector
    facts_collector = FactsCollector()
    facter_collector = facts_collector._get_fact_collector('facter')
    assert facter_collector.find_facter({}) is None

# Generated at 2022-06-13 02:00:23.551639
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    class Module:
        class ExitError:
            pass

        @staticmethod
        def get_bin_path(name, opt_dirs=None):
            if name in ['facter', 'cfacter']:
                return '/opt/puppetlabs/bin/' + name

    # Testing if cfacter is existent
    assert FacterFactCollector().find_facter(Module()) == "/opt/puppetlabs/bin/cfacter"

    # Testing if cfacter is non-existent, but facter is
    class Module_facter:
        class ExitError:
            pass

        @staticmethod
        def get_bin_path(name, opt_dirs=None):
            if name == 'facter':
                return '/opt/puppetlabs/bin/' + name

    assert FacterFactCollector().find_f

# Generated at 2022-06-13 02:00:30.955835
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    from ansible.module_utils.facts import ModuleFacts
    from collections import namedtuple

    module_facts = ModuleFacts()
    module_facts.get_bin_path = lambda *args, **kwargs: '/usr/bin/facter' # mock facter path
    module_facts.run_command = lambda cmd: namedtuple('obj', ['rc', 'stdout', 'stderr'])(0, '{"facter_1":"value_1"}', '') # mock call to facter
    facter_collector = FacterFactCollector()
    facter_output = facter_collector.get_facter_output(module_facts)

    assert facter_output == '{"facter_1":"value_1"}'


# Generated at 2022-06-13 02:00:41.394323
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    from ansible.module_utils.facts.collector.facter import FacterFactCollector
    facter_collector = FacterFactCollector()

    class fake_module(object):
        def get_bin_path(self, exe, opt_dirs=None, required=False):
            if exe == 'facter':
                if opt_dirs == ['/opt/puppetlabs/bin']:
                    return '/opt/puppetlabs/bin/facter'
                else:
                    return '/usr/bin/facter'
            if exe == 'cfacter':
                return '/opt/puppetlabs/bin/cfacter'
            return None

    # No facter nor cfacter installed
    fake_module_obj = fake_module()
    facter_path = facter_collector.find_f

# Generated at 2022-06-13 02:00:48.652205
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    # Test for class FacterFactCollector
    import _fixture
    from ansible.module_utils.facts.collector import Collector

    # Test with missing module argument
    ffc = FacterFactCollector()
    truth = dict()
    assert isinstance(ffc, Collector)
    assert ffc.collect() == truth

    # Test with module argument
    facter_path = _fixture.facter_output
    module_name = 'ansible.module_utils.facts.collector.BaseFactCollector.run_command'
    _fixture.facter_output = '{"facter1": "test1", "facter2": "test2"}'
    module_mock = _fixture.create_mock_module(module_name)

# Generated at 2022-06-13 02:00:58.851654
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    import ansible.module_utils.facts.collector
    class FakeModule:
        def __init__(self):
            self.name = 'foo'
            self.path = '/usr/bin:/usr/local/bin:/bin'
        def run_command(self, path):
            return (0, '{"hostname": "foo"}')
        def get_bin_path(self, app, opt_dirs=[]):
            return "facter"

    f = FacterFactCollector()

    module = FakeModule()
    facter_output = f.get_facter_output(module)

    # TODO: if we fail, should we add a empty facter key or nothing?
    if facter_output is None:
        assert False, "Expected get_facter_output() to return something!"


# Generated at 2022-06-13 02:01:03.186621
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    # Create mock Ansible module
    module = MagicMock(spec=dict)
    module.run_command.return_value = (0, '{"facter": true}', '')
    module.get_bin_path.return_value = '/bin/facter'

    ff = FacterFactCollector()
    fact_dict = ff.collect(module=module)
    assert fact_dict == {"facter": True}

# Generated at 2022-06-13 02:01:05.898582
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    """test function for find_facter method of class FacterFactCollector """
    assert FacterFactCollector().find_facter() == "/opt/puppetlabs/bin/facter"



# Generated at 2022-06-13 02:01:12.632550
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():
    # unit testing imports
    import pytest
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.utils

    # test class imports
    import ansible.module_utils.facts.collectors.facter

    def get_bin_path(self, arg, opt_dirs=[]):
        return '/usr/bin/facter'

    FacterFactCollector._get_bin_path = get_bin_path

    # testing for success

# Generated at 2022-06-13 02:01:21.020540
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    import sys
    from ansible.module_utils.facts import ansible_collector

    m = ansible_collector.get_module_mock()
    m.run_command = lambda *args, **kwargs: (0, '{"a": "fake"}', '')

    f = FacterFactCollector(collectors=[test_FacterFactCollector_collect])
    f.collect(module=m)

    assert 'facter_a' in m.ansible_facts
    assert m.ansible_facts['facter_a'] == 'fake'


# Generated at 2022-06-13 02:01:22.951539
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    assert FacterFactCollector().get_facter_output(None) is None


# Generated at 2022-06-13 02:01:31.500400
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    import ansible.module_utils
    import ansible.module_utils.facts

    objFacterFactCollector = ansible.module_utils.facts.collectors.facter.FacterFactCollector()

    # Test case #1 - facter_path should not be found. Expect to return None.
    facter_path = objFacterFactCollector.find_facter(None)
    assert facter_path is None

    # Test case #2 - facter_path should be found. Expect to return a dictionary.
    facter_dict = objFacterFactCollector.get_facter_output(None)
    assert isinstance(facter_dict, dict)
    assert len(facter_dict) > 0

    # Test case #3 - facter_path should be found. Expect to return a dictionary.
    testobj = ans

# Generated at 2022-06-13 02:01:41.685905
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    import os
    import sys
    import tempfile
    import shutil
    import ansible.module_utils.facts.collector as fact_collector
    import ansible.module_utils.facts.namespace as fact_namespace
    import ansible.module_utils.facts as facts_module


# Generated at 2022-06-13 02:01:45.857714
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    # noinspection PyMethodMayBeStatic
    class TestHost(object):
        def run_command(self, cmd, module):
            return 0, None, None

        def get_bin_path(self, bin_path, opt_dirs=None):
            if bin_path == 'facter':
                return '/usr/bin/facter'
            elif bin_path == 'cfacter':
                return '/usr/bin/cfacter'
            else:
                return None

    import os
    import tempfile
    import json

    test_host = TestHost()

    class CollectedFacts(object):
        def __init__(self):
            self.facts = {}

    test_collected_facts = CollectedFacts()


# Generated at 2022-06-13 02:01:47.144191
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    ffc = FacterFactCollector()
    ffc.collect()

# Generated at 2022-06-13 02:01:56.215597
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    from ansible.module_utils.facts.system.facter import FacterFactCollector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.namespace import BaseFactNamespace

    # Create object FacterFactCollector
    facter_fact_collector = FacterFactCollector()

    # Create module without facter path
    class FakeModule:
        def get_bin_path(self, executable, opt_dirs=[]):
            return None

        def run_command(self, cmd):
            return 0, "", ""

    # Check facter_output when facter not installed
    assert facter_fact_collector.get_facter_output(FakeModule()) is None

    # Create module with facter path

# Generated at 2022-06-13 02:02:07.263762
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    import platform
    import json

    class TestModule():
        def get_bin_path(self, binary, opt_dirs=None, required=False):
            bin_path = None

            if binary == 'facter':
                bin_path = "/usr/bin/facter"

            return bin_path

        def run_command(self, command):
            stdout_mapping = {
                "/usr/bin/facter --puppet --json": json.dumps({ "ansible_os_family" : "RedHat" }),
            }

            stderr_mapping = {
                "/usr/bin/facter --puppet --json": "",
            }

            rc_mapping = {
                "/usr/bin/facter --puppet --json": 0,
            }

            stdout = None
            stder

# Generated at 2022-06-13 02:02:16.095569
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    module = object()
    facter_path = "/usr/bin/facter"
    expected_path = facter_path

    # If facter path is found in /usr/bin and no cfacter path is found a /usr/bin
    # return expected path
    def module_get_bin_path(binary, opt_dirs=[]):
        if binary == "facter" and not opt_dirs:
            return expected_path
        return None

    module.get_bin_path = module_get_bin_path
    facter = FacterFactCollector()
    actual_path = facter.find_facter(module)

    assert actual_path == expected_path


# Generated at 2022-06-13 02:02:24.947759
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    facter_output = None
    facter_dict = {}

    class MockModule(object):
        def __init__(self):
            self.ansible_facts = {}

        def get_bin_path(self, path, opt_dirs=[]):
            return "/usr/bin/facter"

        def run_command(self, cmd):
            return 0, facter_output, ""

    def mock_run_facter(self, module, facter_path):
        return 0, facter_output, ""

    def mock_get_facter_output(self, module):
        return facter_output

    module = MockModule()
    facter_collector = FacterFactCollector()

    # Simulate find_facter() output
    FacterFactCollector.find_facter = mock_find_facter

# Generated at 2022-06-13 02:02:38.294752
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.collector import BaseFactCollector

    h = BaseFactCollector({}, [])

    collectors = []
    namespace = PrefixFactNamespace('facter', 'facter_')
    facter_collector = FacterFactCollector(collectors, namespace)

    facter_path = facter_collector.find_facter(h)

    assert facter_path



# Generated at 2022-06-13 02:02:50.017640
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    import mock
    module = mock.Mock()
    module.get_bin_path.return_value = None
    facter_collector = FacterFactCollector()
    facter_path_none = facter_collector.find_facter(module)
    assert facter_path_none is None

    module.get_bin_path.return_value = "/bin/facter"
    facter_path = facter_collector.find_facter(module)
    assert facter_path == "/bin/facter"

    # Check that find_facter returns cfacter if available.
    module.get_bin_path.return_value = "/bin/cfacter"
    facter_path_cfacter = facter_collector.find_facter(module)

# Generated at 2022-06-13 02:02:58.356753
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    """
    Unit test will be used with py.test.
    """
    testfactercollector = FacterFactCollector()

    class TestModule:
        def get_bin_path(self, path, opt_dirs=['/opt/puppetlabs/bin']):
            return path

        def run_command(self, command):
            return 0, json.dumps({'test_facter': 'test_value'}), None

    class TestCollectedFacts:
        def __init__(self):
            self = dict()
            self['ansible'] = dict()

    testfactscollected = TestCollectedFacts()
    testmodule = TestModule()

    testfactercollector.collect(module=testmodule,
                                collected_facts=testfactscollected)

# Generated at 2022-06-13 02:03:08.746504
# Unit test for method get_facter_output of class FacterFactCollector

# Generated at 2022-06-13 02:03:18.780127
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.utils import get_file_lines

    module = get_collector_instance("FacterFactCollector")
    # Class method get_facter_output of FacterFactCollector is calling class method find_facter
    # We mock method find_facter to make the test independant on the fact that
    # facter is installed on the system where the test is running.
    # We also mock method get_bin_path to make method find_facter return the path
    # to the script used to fake facter
    module.find_facter = lambda x: 'facter'
    module.get_bin_path = lambda x, y: 'facter'

    facter_output = module.get_facter_

# Generated at 2022-06-13 02:03:26.578657
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    from ansible.module_utils.facts.collector import Cache
    cache = Cache()

    collector = FacterFactCollector()

    class TestModule(object):
        def get_bin_path(self, binary, opt_dirs):
            return "./facter"

        def run_command(self, binary):
            return 0, """{
                "os": {
                    "family": "RedHat",
                    "architecture": "x86_64",
                    "hardware": "x86_64",
                    "name": "Fedora",
                    "release": {
                        "full": "31",
                        "major": "31",
                        "minor": "0"
                    }
                },
                "kernel": "Linux"
            }""", None

    module = TestModule()


# Generated at 2022-06-13 02:03:29.935568
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    import ansible.module_utils.facts.collector

    ff = FacterFactCollector(collectors=None, namespace=None)

    class M:
        def get_bin_path(mself, bin, opt_dirs=None):
            return '/path/to/facter'

        def run_command(mself, cmd):
            return 0, '{"facter": "output"}', ''

    assert ff.get_facter_output(M()) == '{"facter": "output"}'

# Generated at 2022-06-13 02:03:34.433817
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    import os, sys
    # Alter system path to include the mock_module helper along with this module,
    # so Ansible will import the helper instead of the real module.
    sys.path.append(os.path.join(os.path.dirname(__file__), '../../../test/ansible_module_utils/'))
    from mock_module import MockModule

    # Create a module mock with an os.getcwd() method that will return
    # the expected directory path.
    my_os_module = MockModule()
    my_os_module.getcwd.return_value = '/usr/bin/'

    # Create a MockModule object with a fake get_bin_path() method.
    my_module = MockModule()

# Generated at 2022-06-13 02:03:35.536600
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():
    pass

# Generated at 2022-06-13 02:03:44.304254
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    class TestModule(object):
        def get_bin_path(self, name, opt_dirs=None):
            if name == 'facter':
                return '/usr/bin/facter'
            else:
                return None

        def run_command(self, command):
            # We expect the command to be:
            # /usr/bin/facter --puppet --json
            assert command == '/usr/bin/facter --puppet --json'
            return 0, '', ''
    ffc = FacterFactCollector()
    module = TestModule()
    assert ffc.get_facter_output(module) is not None


# Generated at 2022-06-13 02:04:07.606010
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    fake_module = FakeModule()
    fake_module.bin_path_files = {'facter': '/usr/bin/facter', 'cfacter': '/usr/bin/cfacter'}

    facter_fact_collector = FacterFactCollector()
    facter_path = facter_fact_collector.find_facter(fake_module)
    assert facter_path == '/usr/bin/cfacter'


# Generated at 2022-06-13 02:04:11.825193
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    # create class FacterFactCollector object
    ffc = FacterFactCollector()

    # create class FakeModule object
    fm = FakeModule()

    # create dict values for Facter and cfacter
    fm.bin_dir = {'facter': 'facter/facter', 'cfacter': 'cfacter/cfacter'}

    # we expect return value as cfacter if it exists
    assert ffc.find_facter(fm) == 'cfacter/cfacter'


# Generated at 2022-06-13 02:04:19.869149
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():

    import mock
    import os
    import sys

    if sys.version_info < (2, 7):
        import unittest2 as unittest
    else:
        import unittest

    class TestFacterFactCollector(unittest.TestCase):

        def setUp(self):
            self.facter_fact = FacterFactCollector()

        @mock.patch.dict(os.environ, {'ANSIBLE_FACTER_PATH': '/usr/bin/facter'})
        @mock.patch('os.access')
        def test_find_facter_with_envvar(self, mock_access):
            mock_access.return_value = True

            facter_path = self.facter_fact.find_facter(None)

# Generated at 2022-06-13 02:04:29.037515
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    def _run_mock_module(c, args):
        if c == 'facter --version':
            return (0, 'facter-2.0.1', '')
        elif c == 'cfacter --version':
            return (0, 'facter-2.0.1', '')
        elif c == 'facter --json':
            return (0, '{"foo": "bar"}', '')
        elif c == 'cfacter --json':
            return (0, '{"foo": "bar"}', '')
        else:
            raise Exception('Not expected')

    mock_module = type('module', (object,), {
        'run_command': _run_mock_module,
        'get_bin_path': lambda self, path, opt_dirs=[] : None
    })()

   

# Generated at 2022-06-13 02:04:34.653144
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    obj = FacterFactCollector()
    class MockModule(object):
        def get_bin_path(self, program, opt_dirs=None):
            if program == 'cfacter':
                return '/opt/puppetlabs/bin/cfacter'
            return None

    module = MockModule()
    facter_path = obj.find_facter(module)
    assert facter_path == '/opt/puppetlabs/bin/cfacter'

    class MockModule(object):
        def get_bin_path(self, program, opt_dirs=None):
            if program == 'facter':
                return '/opt/puppetlabs/bin/facter'
            return None

    module = MockModule()
    facter_path = obj.find_facter(module)

# Generated at 2022-06-13 02:04:43.277004
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    import sys
    import os
    import tempfile
    # This is needed because we are calling this from another file
    # where the module import is not seen
    sys.path.append(os.path.dirname(__file__))
    from test_utils import AnsibleExitJson, AnsibleFailJson, ModuleTestCase, set_module_args

    class MyModule(object):
        def __init__(self, argument_spec=None, bypass_checks=False, no_log=True,
                     check_invalid_arguments=None, mutually_exclusive=None, required_together=None,
                     required_one_of=None, add_file_common_args=None, supports_check_mode=False,
                     required_if=None, required_by=None, bypass_warnings=False):
            pass


# Generated at 2022-06-13 02:04:48.279792
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():
    module = MockModule()
    facter_path = FacterFactCollector().find_facter(module)
    rc, out, err = FacterFactCollector().run_facter(module, facter_path)
    assert rc == 0
    assert out is not None
    assert err is None


# Mock for ansible.module_utils.basic.AnsibleModule

# Generated at 2022-06-13 02:04:56.392471
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():
    import tempfile
    import os

    o = FacterFactCollector()
    fd, facter_path = tempfile.mkstemp()
    os.write(fd, b"#! /bin/sh\necho '{\"a\": 1, \"b\": 2}'\n")
    os.close(fd)
    os.chmod(facter_path, 0o777)
    rc, out, err = o.run_facter(None, facter_path)
    assert rc == 0
    assert out == "{\"a\": 1, \"b\": 2}"
    assert err == ""
    os.remove(facter_path)


# Generated at 2022-06-13 02:05:07.632194
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    module = type(str("FakeModule"), (object,), {})

# Generated at 2022-06-13 02:05:10.478453
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    facts = FacterFactCollector().collect()
    assert type(facts['kernelmajversion']) == int


# Generated at 2022-06-13 02:05:59.427478
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    # Testing with facter_output as an empty string
    obj = FacterFactCollector()
    facter_dict = obj.collect()
    assert facter_dict == {}

    # Testing with invalid facter_output
    obj = FacterFactCollector()
    facter_dict = obj.collect(module=MockModule({}))
    assert facter_dict == {}

    # Testing with valid facter_output
    obj = FacterFactCollector()

# Generated at 2022-06-13 02:06:09.667166
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():

    class FakeModule(object):
        def __init__(self):
            self.run_command_called = False
            self.run_command_args = None

        def run_command(self, args, check_rc=False, environ_update=None, data=None, binary_data=False,
                        path_prefix=None, cwd=None, use_unsafe_shell=False):
            self.run_command_called = True
            self.run_command_args = args
            return (0, '{"osfamily":"test"}', '')

        def get_bin_path(self, name, opt_dirs=None, required=False):
            return '/bin/facter'

    fake_module = FakeModule()

    facter_path = FacterFactCollector().find_facter(fake_module)

# Generated at 2022-06-13 02:06:16.137637
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.utils

    facter_facts = ansible.module_utils.facts.collector.FacterFactCollector()
    facter_data = facter_facts.get_facter_output(ansible.module_utils.facts.utils.get_module())

    # Verify the returned data is in json format
    json.loads(facter_data)


# Generated at 2022-06-13 02:06:19.175828
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    module = object()
    facter_path = FacterFactCollector().find_facter(module)
    if isinstance(facter_path, str):
        assert True
    else:
        assert False

# Generated at 2022-06-13 02:06:28.169113
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    import os
    from ansible.module_utils.facts.namespace import BaseFactNamespace

    # test with 'facter' on PATH
    class TestModule(object):
        def __init__(self):
            self.PATH = '/usr/bin/'

        def get_bin_path(self, exe, opt_dirs=None):
            if exe == 'facter':
                return os.path.abspath(os.path.join(self.PATH, exe))
            elif exe == 'cfacter':
                return None

    class TestFactNamespace(BaseFactNamespace):
        def __init__(self):
            pass

    module = TestModule()
    facter_path = FacterFactCollector(namespace=TestFactNamespace()).find_facter(module)
    assert facter_

# Generated at 2022-06-13 02:06:30.828490
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    from ansible.module_utils.facts.collector import get_collector_instance


# Generated at 2022-06-13 02:06:39.314102
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():
    import os

    # Test the module with out a facter package installed
    module = MockAnsibleModule()
    facter_fc = FacterFactCollector()
    expected_rc = 0
    expected_out = '''{
  "json => 'true'": "true",
  "path": "/usr/local/bin:/usr/bin:/bin",
  "json => 'false'": "false"
}
'''
    expected_err = ''

    rc, out, err = facter_fc.run_facter(module, "/usr/bin/facter")

    assert rc == expected_rc
    assert out == expected_out
    assert err == expected_err

    # Test the module with a facter package installed
    facter_fc = MockFacterCollector()
    expected_rc = 0

# Generated at 2022-06-13 02:06:49.525173
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    import os
    import sys

    class MockModule(object):
        def __init__(self):
            self.path = os.getcwd()
            for p in sys.path:
                if p.endswith('lib/ansible/module_utils'):
                    self.path = p
                    break

        def get_bin_path(self, name, opt_dirs=[]):
            if name == 'cfacter':
                return os.path.join(self.path, 'facter_mock')
            else:
                return os.path.join(self.path, 'facter_mock_bad')

        def run_command(self, cmd, **kwargs):
            return 0, '{"system_uptime":{"seconds":436}}', ''

    facter = FacterFactCollector()

    # With cfacter

# Generated at 2022-06-13 02:06:59.783381
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    from ansible.module_utils.facts import ModuleFactCollector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.facter import FacterFactCollector
    facter_collector = FacterFactCollector(namespace=PrefixFactNamespace(namespace_name='facter',
                                                                         prefix='facter_'))
    #1. test with empty path
    module = BaseFactCollector()
    module.get_bin_path = lambda x: None
    assert facter_collector.find_facter(module) is None
    #2. test with facter in path
    module.get_bin_path = lambda x: '/usr/bin/facter'

# Generated at 2022-06-13 02:07:05.679507
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    # Create test module
    class FakeModule():

        def get_bin_path(self, *args, **kwds):
            return '/bin/facter'

        def run_command(self, *args, **kwds):
            return (0, '{"ansible_facter":"facter"}', '')

    fake_module = FakeModule()

    # Create object to test
    facter_fc = FacterFactCollector()
    facter_dict = facter_fc.get_facter_output(fake_module)

    assert facter_dict == '{"ansible_facter":"facter"}'