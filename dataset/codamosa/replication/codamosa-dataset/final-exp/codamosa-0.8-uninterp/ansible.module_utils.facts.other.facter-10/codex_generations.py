

# Generated at 2022-06-13 01:58:54.806033
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts.collectors.facter import FacterFactCollector

    test_module = AnsibleModule()

    facter_collector = FacterFactCollector()

    # Scenario 1: facter not installed
    facter_output = facter_collector.get_facter_output(test_module)
    # Should return None if facter is not installed
    assert facter_output is None

    # Scenario 2: facter installed
    facter_collector._find_facter = lambda x: 'facter'
    facter_collector.run_facter = lambda x, y: (0, '{"test": "success"}', '')

# Generated at 2022-06-13 01:58:59.244403
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    from ansible.module_utils.facts.collector import FactsCollector

    # Two collectors that collect_facts() will create
    # FactCollector and DistributionFactCollector

    facter_collector = FacterFactCollector()
    facter_collector.collect()

# Generated at 2022-06-13 01:59:05.039093
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    from ansible.module_utils.facts.tests.mock_module import MockModule
    module = MockModule()
    collector = FacterFactCollector()
    facter_output = collector.get_facter_output(module)
    if facter_output is not None:
        assert(facter_output.startswith('{'))
    return

# Generated at 2022-06-13 01:59:09.177745
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    # create an empty class
    class EmptyClass(object):
        pass

    # build a module
    module = EmptyClass()
    module.run_command = run_command

    # instance a facter collector
    collector = FacterFactCollector(collectors=None)

    facter_output = collector.get_facter_output(module)
    print(facter_output)



# Generated at 2022-06-13 01:59:18.836753
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    # Create a class instance
    ffc = FacterFactCollector()
    # Method find_facter() should always return None if '/bin/facter' is not executable
    assert ffc.find_facter(None) == None
    # Mock ansible.module_utils.facts.collector.find_executable method
    ffc.find_executable = lambda path: os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../bin/facter'))
    # Method find_facter should return the path to the ansible-test fixture executable
    assert ffc.find_facter(None) == os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../bin/facter'))


# Generated at 2022-06-13 01:59:28.161216
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    # setup
    class Module:
        def get_bin_path(self, *args, **kwargs):
            return '/usr/bin/facter'

    class CollectedFacts(object):
        def __init__(self):
            self.ansible_facts = {}
            self.ansible_facts['ansible_local'] = {}
            self.ansible_facts['ansible_local']['facter_path'] = None

    cf = CollectedFacts()
    ffc = FacterFactCollector()

    # execute
    ffc.update_local_facts(cf, Module())

    # assert
    assert cf.ansible_facts['ansible_local']['facter_path'] == '/usr/bin/facter'


# Generated at 2022-06-13 01:59:38.035263
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    import mock

    facter_bin = '/opt/puppetlabs/bin/facter'
    cfacter_bin = '/opt/puppetlabs/bin/cfacter'

    # cfacter exists, facter does not exist
    mocked_module = mock.MagicMock()
    mocked_module.run_command.return_value = (1, None, None)
    mocked_module.get_bin_path.return_value = cfacter_bin
    facter_finder = FacterFactCollector()
    assert facter_finder.find_facter(mocked_module=mocked_module) == cfacter_bin

    # facter exists, cfacter exists
    mocked_module = mock.MagicMock()
    mocked_module.run_command.return_value = (1, None, None)
    mocked_module.get

# Generated at 2022-06-13 01:59:46.569437
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    class FakeModule(object):
        def __init__(self, paths):
            self.paths = paths
        def get_bin_path(self, path, opt_dirs):
            if path in self.paths:
                return self.paths[path]
            else:
                return None

    m = FakeModule({'facter': '/usr/bin/facter', 'cfacter': '/opt/puppetlabs/bin/cfacter'})
    facter_path = FacterFactCollector().find_facter(m)
    assert facter_path == '/usr/bin/facter'

    m = FakeModule({'cfacter': '/opt/puppetlabs/bin/cfacter', 'facter': '/usr/bin/facter'})
    facter_path = FacterFactCollector().find_facter

# Generated at 2022-06-13 01:59:54.973620
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    from ansible.module_utils.facts.collector import GenericFactCollector

    facter_fact = FacterFactCollector(collectors=(GenericFactCollector,))
    assert facter_fact.find_facter == FacterFactCollector.find_facter
    # TODO: find a way to mock get_bin_path
    #facter_bin = '/usr/bin/facter'
    #module.get_bin_path.return_value = facter_bin
    #assert facter_fact.find_facter(module) == facter_bin
    #module.get_bin_path.assert_called_with('facter', opt_dirs=['/opt/puppetlabs/bin'])




# Generated at 2022-06-13 02:00:02.852411
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    # Create a mock module
    module = AnsibleModule(argument_spec=dict())
    module.run_command = MagicMock()
    get_bin_path_mock = MagicMock()
    get_bin_path_mock.return_value = '/opt/puppetlabs/bin/facter'
    module.get_bin_path = get_bin_path_mock

    # Create a FacterFactCollector
    ffc = FacterFactCollector()

    # Test that we return the correct path for facter
    assert ffc.find_facter(module) == '/opt/puppetlabs/bin/facter'


# Generated at 2022-06-13 02:00:18.924908
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():

    from ansible.module_utils.facts.collector import FactsCollector

    module = FactsCollector()
    assert module

    collector = FacterFactCollector()
    assert collector

    facter_path = collector.find_facter(module)

    assert facter_path is not None

    rc, out, err = collector.run_facter(module, facter_path)

    assert rc == 0
    assert out
    assert err == ''

    facter_dict = collector.get_facter_output(module)
    assert facter_dict

    facter_dict = json.loads(facter_dict)
    assert facter_dict

    facter_dict = collector.collect(module)
    assert facter_dict

# Generated at 2022-06-13 02:00:29.227507
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    from ansible.module_utils.facts import ModuleUtilsFactsCollector
    from ansible.module_utils import basic
    import mock

    # Create a mock module, because we are not running
    mock_module = mock.MagicMock(basic.AnsibleModule)
    mock_module.name = "test"
    mock_module.get_bin_path.return_value = '/opt/puppetlabs/bin/facter'

    uf = ModuleUtilsFactsCollector(module=mock_module)
    ffc = FacterFactCollector(collectors=[uf])

    # Check if the mock_module (mocked AnsibleModule) was called with the right
    # arguments. The first argument is the argv argument, which is a list.
    # The other arguments are the kwargs arguments.
    mock_module

# Generated at 2022-06-13 02:00:39.437362
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    class MockModule(object):
        def __init__(self, paths=None):
            self.paths = paths

        def get_bin_path(self, bin_name, opt_dirs=list(), required=False):
            if self.paths is not None and bin_name in self.paths:
                return self.paths[bin_name]

            return None

    # no facter present
    test_module = MockModule(paths=dict())
    collector = FacterFactCollector()
    assert collector.find_facter(test_module) is None

    # facter present but no cfacter
    test_module = MockModule(paths=dict(facter='/usr/bin/facter'))
    collector = FacterFactCollector()

# Generated at 2022-06-13 02:00:43.515789
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():
    collector = FacterFactCollector()
    module = MockModule()
    facter_path = collector.find_facter(module)
    rc, out, err = collector.run_facter(module, facter_path)
    assert rc == 0
    assert len(out) > 0
    assert len(err) == 0


# Generated at 2022-06-13 02:00:53.571893
# Unit test for method get_facter_output of class FacterFactCollector

# Generated at 2022-06-13 02:00:56.690446
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    _result = FacterFactCollector().find_facter('/opt/puppetlabs/bin/facter')
    assert _result == '/opt/puppetlabs/bin/facter'


# Generated at 2022-06-13 02:01:05.094824
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():

    # Create an instance of FacterFactCollector
    ff = FacterFactCollector()

    # Create a empty mock module
    module = MockModule()

    # Test when facter bin not found
    module.bin_exist['facter'] = False
    module.bin_exist['cfacter'] = False
    facter_output = ff.get_facter_output(module)
    assert facter_output is None

    # Test when facter bin is found
    module.bin_exist['facter'] = True
    module.bin_exist['cfacter'] = False
    facter_output = ff.get_facter_output(module)
    assert facter_output is not None

    # Test when cfacter bin is found
    module.bin_exist['facter'] = True
    module.bin_exist['cfacter'] = True

# Generated at 2022-06-13 02:01:12.222008
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    import module_utils.basic
    mock_module = module_utils.basic.AnsibleModule(
    )
    facter_fc = FacterFactCollector()

    facter_fc.get_facter_output = lambda m: None
    facter_fc.find_facter = lambda m: None

    facter_output = facter_fc.get_facter_output(mock_module)
    assert facter_output is None

    facter_fc.get_facter_output = lambda m: None
    facter_fc.find_facter = lambda m: '/path/to/facter'

    facter_output = facter_fc.get_facter_output(mock_module)
    assert facter_output is None

    cfacter_fc = FacterFactCollector()
    cfacter_

# Generated at 2022-06-13 02:01:14.607814
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    collector = FacterFactCollector()
    facter_output = collector.get_facter_output(None)
    assert facter_output is None


# Generated at 2022-06-13 02:01:23.193621
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    class TestModule:
        def __init__(self):
            self.fail_json = None
            self.params = None
            self.bin_path_list = []

        def get_bin_path(self, bin_name, opt_dirs=None, required=False):
            if bin_name not in self.bin_path_list:
                return None
            return "/usr/bin/%s" % bin_name

        def run_command(self, cmd):
            return 0, '{"test": "value"}', ''

    test_module = TestModule()
    facter_collector = FacterFactCollector()
    test_module.bin_path_list = ['facter']
    assert json.loads(facter_collector.get_facter_output(test_module)) == {'test': 'value'}

# Generated at 2022-06-13 02:01:43.318822
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():
    collector = FacterFactCollector()
    class dummy_module:
        @staticmethod
        def get_bin_path(bin, opt_dirs=[]):
            return bin


# Generated at 2022-06-13 02:01:51.349239
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    module = object()
    facter_path = '/usr/bin/facter'

# Generated at 2022-06-13 02:01:58.821438
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    module = MockAnsibleModule()
    facter_path = '/usr/bin/facter'
    module.get_bin_path.return_value = facter_path

    facter_output = '{"fact1": "value1", "fact2": "value2"}'

    facter_collector = FacterFactCollector()

    facter_collector.run_facter = Mock(return_value=(0, facter_output, ''))
    fact_dict = facter_collector.collect(module=module)

    assert fact_dict == {'facter_fact1': 'value1', 'facter_fact2': 'value2'}
    facter_collector.run_facter.assert_called_with(module, '/usr/bin/facter')



# Generated at 2022-06-13 02:02:09.612644
# Unit test for method collect of class FacterFactCollector

# Generated at 2022-06-13 02:02:12.175843
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    m = AnsibleModule(argument_spec={})
    f = FacterFactCollector()
    r = f.collect(m)
    assert r is not None


# Generated at 2022-06-13 02:02:22.005667
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    from ansible.module_utils._text import to_bytes

    module = AnsibleModule(argument_spec=dict())

    facter_collector = FacterFactCollector()
    facter = facter_collector.find_facter(module)

    assert facter is None

    set_module_args(dict(
        ansible_facter='/usr/bin/facter',
    ))

    facter = facter_collector.find_facter(module)

    assert facter == '/usr/bin/facter'

    set_module_args(dict(
        ansible_facter='/opt/puppetlabs/bin/facter',
    ))

    facter = facter_collector.find_facter(module)

    assert facter == '/opt/puppetlabs/bin/facter'

# Generated at 2022-06-13 02:02:32.180210
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():

    class Module(object):
        def __init__(self):
            self.params = {}
            self.options = {}
            self.facts = {}
            self.ansible_facts = {}
            self.basedir = '/'
            self.tmpdir = '/tmp'

        def get_bin_path(self, name, opt_dirs=[]):
            if name == 'facter':
                return 'facter'
            elif name == 'cfacter':
                return 'cfacter'

        def run_command(self, cmd):
            self.cmd = cmd
            return 0, '{"facter_a": "b", "facter_c": "d"}', ''

    module = Module()
    FacterFactCollector().get_facter_output(module)


# Generated at 2022-06-13 02:02:35.683229
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    cache = {}
    import ansible.module_utils.facts.collector.network as collector

    collector.FacterFactCollector.get_facter_output(cache, {}, {}, {})
    assert 'ansible_facts' in cache
    assert 'facter' in cache['ansible_facts']


# Generated at 2022-06-13 02:02:47.471004
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    import tempfile
    import subprocess
    import sys
    import os

    class TestModule():
        class params():
            datadir = "datadir"

        def get_bin_path(self, executable, opt_dirs=[]):
            if executable == "cfacter":
                if sys.platform == 'win32' and os.path.exists("C:/ProgramData/chocolatey/bin/cfacter.cmd"):
                    return "C:/ProgramData/chocolatey/bin/cfacter.cmd"
                else:
                    return executable

            if executable == "facter":
                if sys.platform == 'win32' and os.path.exists("C:/ProgramData/chocolatey/bin/facter.bat"):
                    return "C:/ProgramData/chocolatey/bin/facter.bat"
               

# Generated at 2022-06-13 02:02:55.540822
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.collector import list_collectors
    from ansible.module_utils.facts.collector import disable_collectors
    from ansible.module_utils.facts.collector import filter_collectors


    class Module(object):
        # Return valid path when asked for the facter binary
        def get_bin_path(self, executable, opt_dirs=[]):
            return '/bin/facter'

        # Return valid JSON when asked to run facter binary
        def run_command(self, executable):
            return (0, '{"some_facter_fact":"some facter value"}', '')

    # make sure fact

# Generated at 2022-06-13 02:03:13.320004
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    import ansible.module_utils.facts.collector as facts_collector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes

    class FakeAnsibleModule(AnsibleModule):
        def run_command(self, command):
            self.run_command_args = command

# Generated at 2022-06-13 02:03:22.854870
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():

    class MockModule:
        def __init__(self):
            self.params = {}

        def get_bin_path(self, executable, opt_dirs=None):

            if executable == 'facter' or executable == 'cfacter':
                return '/opt/puppetlabs/bin/facter'

        def run_command(self, command):
            self.command = command
            return (0, '{"facts": {"ipaddress": "192.168.1.1"}, "environment": "production"}', '')


    m = MockModule()
    f = FacterFactCollector()
    f.collect(module=m)
    assert m.command is not None
    assert f.find_facter(m) is not None


# Generated at 2022-06-13 02:03:30.532327
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    module = MockModule('test_module')

    # Case: no facter_path, empty facter_dict is returned
    facter_path = None
    fact_collector = FacterFactCollector()
    assert fact_collector.get_facter_path(module) is None
    assert fact_collector.collect(module) == {}

    # Case: facter_path found, facter_dict is returned
    facter_path = '/opt/puppetlabs/bin/facter'
    fact_collector = FacterFactCollector()
    assert fact_collector.get_facter_path(module) == facter_path
    assert fact_collector.collect(module) == module.run_command(facter_path + " --puppet --json")

    # Case: facter_path found, facter_

# Generated at 2022-06-13 02:03:41.331578
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    import os
    import tempfile
    import pytest
    import subprocess
    facter_dict = get_test_facter_dict()
    facter_fact_collector = FacterFactCollector()
    with tempfile.NamedTemporaryFile(delete=False) as f:
        os.chmod(f.name, 0o755)
        f.write(f'#!{os.getenv("SHELL")}\n')
        f.write('echo \'{}\''.format(json.dumps(facter_dict)))
        facter_path = f.name
        class MockModule:
            def get_bin_path(self, facter, opt_dirs):
                return facter_path

# Generated at 2022-06-13 02:03:51.270812
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    ffc = FacterFactCollector()
    module = "fake_module"

    # Test with a fake module that raises an exception when
    # get_bin_path() is called.
    def raiser(module, opt_dirs=[]):
        raise Exception("Test exception")
    fake_module = {
        "get_bin_path": raiser,
    }
    assert ffc.collect(module=fake_module) == {}

    # Test with a fake module that returns None when
    # get_bin_path() is called.
    def none_returner(module, opt_dirs=[]):
        return None
    fake_module = {
        "get_bin_path": none_returner,
    }
    assert ffc.collect(module=fake_module) == {}

    # Testing facter_output =

# Generated at 2022-06-13 02:03:59.150135
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    class FakeModule(object):
        def __init__(self, bin_path):
            self.bin_path = bin_path
        def get_bin_path(self, *args, **kwargs):
            return self.bin_path
    # facter not installed
    module = FakeModule(None)
    facter_fact_collector = FacterFactCollector()
    assert facter_fact_collector.find_facter(module) is None
    # facter installed
    module = FakeModule('/usr/local/bin/facter')
    assert facter_fact_collector.find_facter(module) == module.bin_path
    # cfacter installed
    module = FakeModule('/usr/local/bin/cfacter')
    assert facter_fact_collector.find_facter(module) == module

# Generated at 2022-06-13 02:04:06.274931
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    import unittest
    from ansible.module_utils.facts import ansible_collector

    facts = {'ansible_python_version': (3, 6, 0, 'final', 0)}
    facter_dict = {'some': 'fact'}

    module = FakeModule()

    class FakeNamespace(object):
        def populate(self, facter_dict):
            if not facter_dict:
                self.populated = False
                return

            self.populated = True
            self.name = 'facter'
            self.prefix = 'facter'

    class FakeFacterCollector(FacterFactCollector):
        def get_facter_output(self, module):
            return '{"some": "fact"}'

    collector = FakeFacterCollector()
    collector.namespace = FakeNamespace()

# Generated at 2022-06-13 02:04:09.910419
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    facter = FacterFactCollector()
    # Test with 'facter' in PATH
    class MockModule(object):

        def get_bin_path(self, app, opt_dirs=[]):
            return True
    assert facter.find_facter(MockModule()) == True

    # Test without 'facter' in PATH
    class MockModule2(object):

        def get_bin_path(self, app, opt_dirs=[]):
            return None
    assert facter.find_facter(MockModule2()) == None

# Generated at 2022-06-13 02:04:17.664158
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    from ansible.module_utils.facts.test import TestModule
    class MockFacterFactCollector(FacterFactCollector):
        def find_facter(self, module):
            return '/opt/puppetlabs/bin/facter'


# Generated at 2022-06-13 02:04:27.780958
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    # note we need to create a module object to pass to the method,
    # not sure how to do this.
    # meanwhile, mocking a get_bin_path method so we return the path to here
    import os
    class MockModule:
        def __init__(self):
            self.path = os.path.dirname(os.path.abspath(__file__))
            self.args = [self.path]
            self.bin_path = None
        def get_bin_path(self, s):
            if s not in self.args:
                return None
            else:
                return self.path
        def run_command(self,s):
            if self.bin_path:
                return 0, self.bin_path, None
            else:
                return 1, None, None
    # Test 1: should return

# Generated at 2022-06-13 02:04:55.683338
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    from ansible.module_utils import facts
    from ansible.module_utils._text import to_bytes

    test_module = facts.RealModule({'PATH': '/usr/bin'})
    test_module.run_command = lambda x, check_rc=True, close_fds=True, executable=None, data=None: (0, to_bytes('{"test":true}'), None)

    test_collector = FacterFactCollector(namespace=None)
    test_collector.find_facter = lambda x: '/bin/facter'
    test_collector.get_facter_output = lambda x: None

    test_collector._collect(module=test_module)

# Generated at 2022-06-13 02:05:07.593036
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    from ansible.module_utils.facts import Collector
    ffc = FacterFactCollector()

    class TestModule(object):
        def get_bin_path(self, binary, opt_dirs=[]):
            if binary == 'facter':
                return "/opt/puppet/bin/facter"
            elif binary == 'cfacter':
                return "/opt/puppet/bin/cfacter"
            else:
                return None

    t = TestModule()
    assert ffc.find_facter(t) == "/opt/puppet/bin/cfacter"

    class TestModule2(object):
        def get_bin_path(self, binary, opt_dirs=[]):
            if binary == 'facter':
                return "/opt/puppet/bin/facter"
            else:
                return None



# Generated at 2022-06-13 02:05:17.614910
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    import os
    import sys
    import mock

    class MockModule(object):
        def __init__(self):
            self.params = {}
            self.params['use_puppet_paths'] = False

        def get_bin_path(self, name, opt_dirs=None, required=False):
            if name == 'facter':
                return '/bin/facter'
            raise Exception('Trying to get wrong binary path')

    m = MockModule()
    facter = FacterFactCollector()
    path = facter.find_facter(m)
    assert path is not None
    assert path == '/bin/facter'


# Generated at 2022-06-13 02:05:20.908821
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    """
    Verify that the Facter fact is empty when facter is not installed
    """

    dm = DummyModule()
    ffc = FacterFactCollector()
    facter_output = ffc.get_facter_output(dm)
    assert facter_output == None


# Generated at 2022-06-13 02:05:25.878623
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():

    # Setup a FacterFactCollector object and call method get_facter_output
    # of class FacterFactCollector
    facter_fact_collector = FacterFactCollector()
    facter_output = facter_fact_collector.get_facter_output(None)

    # Facter version 2.4.4 does not work with --json and has no cfacter
    # so it is expected that facter_output is None
    assert facter_output is None


# Generated at 2022-06-13 02:05:33.283079
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    from ansible.module_utils.facts import ansible_facts

    fake_module = FakeModule({})
    class FactCollector(FacterFactCollector):
        def run_facter(self, module, facter_path):
            return 0, json.dumps(ansible_facts['ansible_facter']), ''

    my_fact_collector = FactCollector()
    my_fact_collector.get_facter_output(fake_module)
    assert True


# Generated at 2022-06-13 02:05:41.269012
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    class MockModule(object):
        def __init__(self, bin_path):
            self.bin_path = bin_path

        def get_bin_path(self, *args, **kwargs):
            return self.bin_path

    class MockCommand(object):
        def __init__(self, rc, out, err):
            self.rc = rc
            self.out = out
            self.err = err

    class MockRunner(object):
        def __init__(self, cmd):
            self.cmd = cmd

        def run_command(self, *args, **kwargs):
            return self.cmd.rc, self.cmd.out, self.cmd.err

    facter_path = 'facter_path'
    facter_out = 'facter_out'

# Generated at 2022-06-13 02:05:48.366457
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    class FakeModule(object):
        def get_bin_path(self, *args, **kwargs):
            return '/path/to/facter'

        def run_command(self, command):
            # if the command contains --json, return the parsed output
            # otherwise, return a string containing the command
            if '--json' in command:
                return 0, '{"foo": "bar"}', ''
            else:
                return 0, command, ''

    facter_collector = FacterFactCollector()

    fake_module = FakeModule()
    out = facter_collector.get_facter_output(fake_module)
    assert type(out) == str
    # second time should return the parsed output
    out = facter_collector.get_facter_output(fake_module)

# Generated at 2022-06-13 02:05:53.359418
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    import ansible.module_utils.facts.collector
    import mock
    import sys

    if sys.version_info[0] == 2:
        from StringIO import StringIO
    else:
        from io import StringIO

    class TestModule(object):
        def __init__(self, has_facter=True, has_json=True):
            self.has_facter = has_facter
            self.has_json = has_json

        def get_bin_path(self, binary, opt_dirs=None):
            if binary == 'facter' and self.has_facter:
                return binary
            elif binary == 'cfacter' and self.has_facter:
                return binary
            else:
                return None


# Generated at 2022-06-13 02:05:59.508174
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    """ Test for finding facter. Expects facter to be installed """

    module_path = '/usr/bin/false'
    module = type('module', (object, ), {'get_bin_path': lambda self, arg1, kwargs: module_path})
    assert module.get_bin_path('false') == module_path

    facter_path = FacterFactCollector().find_facter(module)

    assert facter_path is not None


# Generated at 2022-06-13 02:06:42.899789
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    # FacterFactCollector.get_facter_output() returns a dictionary
    ffc = FacterFactCollector()
    assert isinstance(ffc.get_facter_output("module"), str)


# Generated at 2022-06-13 02:06:51.953272
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    # A simple, obvious, test.  Just want to make sure it works with a valid
    # facter output, and doesn't throw an exception.
    FACT_MODULE_PATH = '../unit/modules/unit/ansible/test_facts.py'

# Generated at 2022-06-13 02:07:00.759568
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    import os
    import subprocess

    from ansible.module_utils.facts.collector import BaseFactCollector

    class Module:
        def __init__(self):
            self.params = {}
            self.params['use_sudo'] = False

        def get_bin_path(self, cmd, opt_dirs=[]):
            try:
                path = subprocess.check_output(["which", cmd])
                return path.rstrip()
            except (OSError, subprocess.CalledProcessError):
                return None

        def run_command(self, cmd):
            try:
                data = subprocess.check_output(cmd, shell=True)
                return 0, data, None
            except subprocess.CalledProcessError as e:
                return e.returncode, None, e.output

    module = Module()

# Generated at 2022-06-13 02:07:07.936393
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    from ansible.module_utils.facts import ModuleFailException
    from ansible.module_utils.facts import FactCollector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.namespace import Namespace

    module_mock = MockAnsibleModule()
    facter_mock = MockFacter(module_mock)
    fact_collector_mock = MockFactCollector(facter_mock)
    fact_collector = FactCollector(fact_collector_mock)
    fact_collector.collect(module=module_mock)
    assert fact_collector_mock.facts == facter_mock.facts


# Mock classes for unit test

# Generated at 2022-06-13 02:07:17.907493
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    import sys
    import os
    import shutil

    from ansible.module_utils.facts import FactCollector

    # Initialize a dummy module, to use with get_bin_path
    class TestModule():
        def __init__(self):
            pass

        def get_bin_path(self, executable, opt_dirs=[]):
            if executable == 'facter':
                return '/usr/bin/facter'
            elif executable == 'cfacter':
                return '/usr/bin/cfacter'

    # Initialize a fact collector
    factcol = FactCollector(module=TestModule())


# Generated at 2022-06-13 02:07:22.014658
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():

    # Mock classes and methods required to run the test
    import os
    import errno
    import collections

    class MockModule(object):

        def __init__(self, *args, **kwargs):
            self.params = collections.defaultdict(collections.defaultdict)
            self.args = collections.defaultdict(collections.defaultdict)

        def run_command(self, cmd):
            if 'facter' in cmd:
                return (0, '{"somekey": "somevalue"}', '')
            else:
                return (0, '/bin/true', '')

        def get_bin_path(self, *args, **kwargs):
            return '/bin/true'

    class MockOS(object):

        def __init__(self, *args, **kwargs):
            pass


# Generated at 2022-06-13 02:07:30.557075
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    class MockModule(object):
        @staticmethod
        def get_bin_path(program, opt_dirs=None):
            return program

    class FakeCmdResult(object):
        def __init__(self, rc, out, err):
            self.rc = rc
            self.out = out
            self.err = err

    class MockRunCmd(object):
        def __init__(self):
            self.cmds = []
            self.results = []
            self.fake_results = []

        def append_cmd(self, cmd, rc, out, err):
            self.cmds.append(cmd)
            self.fake_results.append(FakeCmdResult(rc, out, err))


# Generated at 2022-06-13 02:07:37.636217
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    MockOS = type('MockOS', (object,), {'run_command':
                                             lambda: [0,
                                                      '{"xen_guest_name":"None","xen_guest_uuid":"00000000-0000-0000-0000-000000000000"}',
                                                      None]
                                       })
    MockModule = type('MockModule', (object,), {'get_bin_path': lambda path, paths=None: '/opt/puppetlabs/bin/facter',
                                                'run_command': MockOS().run_command})

    facter_fact_collector = FacterFactCollector()
    assert facter_fact_collector.find_facter(MockModule) == '/opt/puppetlabs/bin/facter'
    assert facter_fact_collector.get_f

# Generated at 2022-06-13 02:07:45.816435
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    # we are in a test_FacterFactCollector_get_facter_output
    # so we need to export open source ansible facts
    ansible_os_family = 'RedHat'
    ansible_architecture = 'x86_64'

    # we are using a class from the same module,
    # so we need to reload the module
    reload(BaseFactCollector)
    # we need to instantiate an object to test the method
    FacterFactCollector_test_object = FacterFactCollector()

    # testing that method returns a string as expected
    assert isinstance(FacterFactCollector_test_object.get_facter_output(), basestring)


# Generated at 2022-06-13 02:07:47.100897
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    FFC = FacterFactCollector()
    FFC.find_facter()