

# Generated at 2022-06-13 01:58:54.230282
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    _module = AnsibleModule_Command()
    _module.run_command = AnsibleModule_Command.run_command_factory(rc=0, stdout='{ "facts": { "name": "value" } }')
    facter_output = FacterFactCollector().get_facter_output(_module)
    assert facter_output == '{ "facts": { "name": "value" } }'

    # Test that 'cfacter' program is preferred over 'facter'
    _module = AnsibleModule_Command()
    _module.run_command = AnsibleModule_Command.run_command_factory(rc=0, stdout='{ "facts": { "name": "value" } }')
    facter_path = FacterFactCollector().find_facter(_module)

# Generated at 2022-06-13 01:59:03.511103
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.collectors import which

    import ansible.module_utils.facts.system
    my_collector = Collector()
    my_fact = FacterFactCollector(collectors=[ansible.module_utils.facts.system.collector])
    my_fact._which = which

    result = my_fact.collect(my_collector, collected_facts={})
    assert result
    assert 'facter_architecture' in result
    assert 'facter_kernel' in result

# Generated at 2022-06-13 01:59:11.579301
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    class FakeModule():
        def get_bin_path(self, s, opt_dirs):
            return "/usr/bin/ruby"

        def run_command(self, s):
            if s == "facter --json":
                return 0, '{"a": "1", "b": "2"}', ""
            if s == "cfacter --json":
                return 0, '{"a": "1", "b": "2", "pe_version": "1.0.0", "puppet_vardir": "/fake_vardir"}', ""
            if s == "cfacter --puppet --json":
                return 0, '{"a": "1", "b": "2", "pe_version": "1.0.0", "puppet_vardir": "/fake_vardir"}', ""
            return 1, '', ''



# Generated at 2022-06-13 01:59:18.238042
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    import tempfile
    import os

    with tempfile.NamedTemporaryFile() as f:
        f.write('{"test":"test_value"}')
        f.flush()

# Generated at 2022-06-13 01:59:26.857622
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    '''
    test_FacterFactCollector_collect is the unit test for method
    collect of class FacterFactCollector.

    '''
    class InputModule:
        # dummy module
        pass

    class InputModule:
        # dummy module
        pass

    input_module = InputModule()
    input_module.get_bin_path = lambda: '/usr/bin/facter'
    input_module.run_command = lambda *args, **kwargs: (0, '{"test": "test"}', '')
    fact_collector = FacterFactCollector()
    fact_collector.collect(module=input_module)

# Generated at 2022-06-13 01:59:29.223618
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    module = None
    facter_dict = FacterFactCollector.collect(module)
    assert type(facter_dict) == type({})
    assert facter_dict == {}


# Generated at 2022-06-13 01:59:38.421132
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    class MockModule(object):
        def get_bin_path(self, bin_name, opt_dirs=[]):
            return bin_name

    mock_module = MockModule()

    # Test when cfacter binary is present
    facter_collector = FacterFactCollector()
    assert facter_collector.find_facter(mock_module) == 'cfacter'

    # Test when cfacter binary is not present
    class MockModule2(object):
        def get_bin_path(self, bin_name, opt_dirs=[]):
            if bin_name == 'cfacter':
                return None
            else:
                return bin_name

    mock_module2 = MockModule2()
    facter_collector = FacterFactCollector()

# Generated at 2022-06-13 01:59:45.126016
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    """ Unit test for collect method of class FacterFactCollector.
    """
    from ansible.module_utils.facts.collector import BaseFactCollector

    # Fake FacterCollector class
    class FakeFacterFactCollector(BaseFactCollector):
        name = "fake_facter"
        _fact_ids = set(['facter'])

    # Initialize a FacterFactCollector object
    facter = FakeFacterFactCollector()

    # Assert that facter is instance of FacterFactCollector class
    assert isinstance(facter, FakeFacterFactCollector)

    facter.collect()

# Generated at 2022-06-13 01:59:47.716021
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    # Create an instance of FacterFactCollector class
    instance = FacterFactCollector()
    # Test the collect method and the return type
    assert isinstance(instance.collect(), dict)

# Test for method get_facter_output of class FacterFactCollector

# Generated at 2022-06-13 01:59:51.027829
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    module = MockModule()
    collector = FacterFactCollector()
    out = collector.collect(module)
    expected = {
        'facter_fact1': 'value1',
        'facter_fact2': 'value2',
    }
    assert out == expected


# Generated at 2022-06-13 02:00:02.969815
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector
    from ansible.module_utils.facts.processor import get_processor
    from ansible.module_utils.facts.facts import FactNamespace
    from ansible.module_utils.facts.__init__ import get_collection_module

    module = get_collection_module(module_name='test', namespace=FactNamespace)

    fact_collector = FacterFactCollector(namespace='test')

    facts = fact_collector.collect(module)

    assert 'facter_operatingsystem' in facts
    assert facts['facter_operatingsystem'] is not None

    assert 'facter_uptime_days' in facts
    assert facts['facter_uptime_days'] == 0

    assert 'facter_uptime_seconds' in facts

# Generated at 2022-06-13 02:00:15.107782
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    import sys
    import os
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import Collector
    import ansible.module_utils.facts.collectors.facter as facter

    fc = facter.FacterFactCollector()
    class DummyModule(object):
        def __init__(self):
            self.fail_json = lambda **kwargs: sys.exit(1)
        def get_bin_path(self, executable, opt_dirs=[]):
            return "/usr/bin/{0}".format(executable)
    module = D

# Generated at 2022-06-13 02:00:27.064903
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():

    # Setup
    class MockModule:
        def get_bin_path(self, x, opt_dirs):
            return '/opt/puppetlabs/bin/facter'

# Generated at 2022-06-13 02:00:37.526483
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    ''' Test case for get_facter_output method of class FacterFactCollector '''
    module = MockAnsibleModule('')

    facter_path = '/usr/bin/facter'
    facter_output = '''{
        "test_fact1": "test_value1",
        "test_fact2": "test_value2"
    }'''

    facter_collector = FacterFactCollector()
    rc, out, err = facter_collector.run_facter(module, facter_path)
    assert rc == 0
    assert out == facter_output
    assert err == ''

    facter_path = '/usr/bin/cfacter'

# Generated at 2022-06-13 02:00:45.433555
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    """Unit test for method find_facter of class FacterFactCollector."""
    from ansible.module_utils.facts import collector

    mf = FacterFactCollector(collectors=None, namespace=None)
    class ModuleMock:
        def get_bin_path(self, fn, opt_dirs=None):
            if fn == 'facter':
                return '/usr/bin/facter'
            elif fn == 'cfacter':
                return None
            else:
                return '/bin/' + fn

    mm = ModuleMock()
    facter_path = mf.find_facter(mm)
    assert facter_path == '/usr/bin/facter'

# Generated at 2022-06-13 02:00:56.341111
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    from ansible.module_utils.facts.collector import get_collector_function
    module = None
    mocker = None
    facter_output = '{"ansible_processor_cores": 8, "os": {"release": {"major": "7"}}}'
    #
    # unit test for default behavior when facter is installed
    #
    mocker.patch('ansible.module_utils.facts.collector.get_file_lines', return_value=facter_output)
    mocker.patch('ansible.module_utils.facts.collector.which', return_value='/usr/bin/facter')
    collector = get_collector_function('facter')(module=module, collected_facts=None)
    facter_dict = collector.collect()

# Generated at 2022-06-13 02:01:03.339637
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    # Test that if multiple executables exist on the path, the one with
    # lexicographical precedence is found.
    ansible_path = os.environ['PATH']
    os.environ['PATH'] = os.path.abspath(os.path.join(__file__, '../../../../../test/units/module_utils/facts/facter/'))
    if platform.system() != 'Windows':
        assert FacterFactCollector().find_facter(None) == b'/tmp/facter'
    else:
        assert FacterFactCollector().find_facter(None) == r'C:\ansible\test\units\module_utils\facts\facter\echo.bat'
    os.environ['PATH'] = ansible_path

# Load fact subclasses

# Generated at 2022-06-13 02:01:11.209036
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    from ansible.module_utils.facts import Collector
    from ansible.module_utils.facts.tools import MockModule

    fact_collector = FacterFactCollector()
    assert(fact_collector.find_facter() is None)

    module = MockModule()
    module.run_command.return_value = (0, '', '')

    # Attempt to find facter binary
    fact_collector = FacterFactCollector()
    assert fact_collector.find_facter(module) is None

    # Attempt to find facter binary in /bin
    module.get_bin_path.return_value = '/bin/facter'
    assert fact_collector.find_facter(module) == '/bin/facter'

    # Attempt to find facter binary in /usr/bin
    module.get_bin_

# Generated at 2022-06-13 02:01:21.024054
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    import os
    import subprocess

    def get_facter_path():
        facter_path = None
        facter_path = subprocess.check_output(['which', 'facter']).strip().decode()
        if facter_path is None:
            facter_path = subprocess.check_output(['which', 'cfacter']).strip().decode()
        return facter_path

    def run_facter(facter_path, facts=None):
        base_cmd = [facter_path]
        if facts is not None:
            base_cmd.extend(['--json', '--puppet'])
        facter_cmd = subprocess.Popen(base_cmd, stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE)
        return facter

# Generated at 2022-06-13 02:01:28.897020
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    module = MagicMock()
    facter_path = '/usr/bin/facter'
    module.get_bin_path.return_value = facter_path
    facter_output = '{"facter":{"system_uptime":{"days":2,"hours":8,"seconds":166634,"uptime":"2 days"},"virtual":{"system":"kvm"}}}'

    facter_facts_collector = FacterFactCollector()
    rc, out, err = facter_facts_collector.run_facter(module, facter_path)

    assert rc == 0
    assert out == facter_output
    assert err == ''

# Generated at 2022-06-13 02:01:44.201208
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    class TestFacterFactCollector(FacterFactCollector):
        def find_facter(self, module):
            return '/usr/bin/facter'


# Generated at 2022-06-13 02:01:54.177245
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    import sys
    import tempfile
    import shutil
    import subprocess
    import json

    # FIXME: we should mock this out!
    from ansible.module_utils.facts.collector import BaseFactCollector

    def make_fact_file(collector, fact_json):
        # FIXME: would be nice if we didn't need to go throw this
        #        tempfile dance for each test.  But we cant just write
        #        to collector.fact_file because the next test will
        #        clobber the last one.
        fd, filename = tempfile.mkstemp(prefix='ansible_facts')
        with open(filename, 'wb') as fact_file:
            fact_file.write(json.dumps(fact_json))

        collector.fact_file = filename
        return filename

    fact

# Generated at 2022-06-13 02:01:57.453453
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    # Setup
    module = None
    facter_path = None
    facter_output = None
    facter_dict = {}

    # Test
    facter_output = get_facter_output(module, facter_path)

    # Assert
    assert facter_output is None

# Generated at 2022-06-13 02:02:08.805881
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    class FakeModule:
        def __init__(self):
            self.params = {'facter': dict()}
            self.path = '/bin:/usr/bin:/usr/local/bin:/opt/puppetlabs/bin'
            self.bin_path = '/bin:/usr/bin:/usr/local/bin'

        def get_bin_path(self, binary, opt_dirs=None, required=False):
            return None

        def run_command(self, command):
            return 0, 'test output', 'test error'

    fake_module = FakeModule()

    facter_fact_collector = FacterFactCollector(None, None)
    facter_output = facter_fact_collector.get_facter_output(fake_module)
    assert facter_output == 'test output'

#

# Generated at 2022-06-13 02:02:16.856559
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    # When facter is not installed, get_facter_output should return None
    facter_facts = FacterFactCollector()
    out = facter_facts.get_facter_output(facter_facts)
    assert out is None

    # When facter is installed, get_facter_output should retrun a dict
    facter_facts.find_facter = lambda x: "/usr/bin/facter"
    facter_facts.run_facter = lambda x, y: (0, "", "")

    out = facter_facts.get_facter_output(facter_facts)
    assert type(out) is str

# Generated at 2022-06-13 02:02:25.545384
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    # We need to do this for now, as we do not simulate the actual ansible module,
    # and thus do not have access to the class module which would be created in
    # AnsibleModule.__init__() and thus which could be used to create a new instance
    # of FacterFactCollector.
    class FakeClassModule(object):
        def get_bin_path(self, name, opt_dirs=[]):
            if name == 'facter':
                return 'facter_path'
            if name == 'cfacter':
                return 'cfacter_path'
            return None

    class FakeModule(object):
        def __init__(self):
            self.class_module = FakeClassModule()

        def run_command(self, command):
            if command == 'facter_path --puppet --json':
                return

# Generated at 2022-06-13 02:02:34.815232
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    import os
    os.system("mkdir -p /opt/puppetlabs/bin/")
    os.system("touch /opt/puppetlabs/bin/facter")
    os.system("chmod +x /opt/puppetlabs/bin/facter")
    os.system("echo -n '{\"osfamily\": \"Darwin\"}' > /opt/puppetlabs/bin/facter")

    module = ansible.module_utils.facts.module_util.ModuleUtilsFacts()
    fact_collector = FacterFactCollector()

    assert fact_collector.collect(module) == {'facter_osfamily': 'Darwin'}

    os.system("rm -rf /opt/puppetlabs/bin/facter")

# Generated at 2022-06-13 02:02:39.206602
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    """
    unit test for the find_facter method of the FacterFactCollector class.
    """

    class ModuleMock(object):
        def get_bin_path(self, cmd, opt_dirs=()):
            if cmd == 'cfacter':
                return '/opt/puppetlabs/bin/cfacter'
            return '/usr/bin/facter'

    class FC(FacterFactCollector):
        def run_facter(self, module, facter_path):
            pass

    facter_path = FC().find_facter(ModuleMock())
    assert facter_path == '/opt/puppetlabs/bin/cfacter'



# Generated at 2022-06-13 02:02:51.307404
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils.facts.collector import BaseFactCollector

    class TestModule(object):
        def __init__(self):
            self.params = {}

        @staticmethod
        def get_bin_path(binary, opt_dirs=None):
            if binary == 'facter':
                return "/bin/facter"
            if binary == 'cfacter':
                return "/bin/cfacter"
            return None

        def run_command(self, cmd):
            if "--puppet --json" in cmd:
                return (0, '{"kernel":"Darwin","facterversion":"2.0.2", "domain": "foo.bar"}', None)
            return (1, None, None)


# Generated at 2022-06-13 02:02:58.782919
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.facts import Collector

    class TestCollector(Collector):
        def __init__(self):
            super(TestCollector, self).__init__()

        def get_bin_path(self, name, opt_dirs=None):
            return '/usr/bin/facter'

        def run_command(self, cmd):
            # just return the command, ie:
            # facter --puppet --json
            return 0, cmd, None

    test_collector = TestCollector()

    facter_collector = FacterFactCollector([], namespace=None)
    assert facter_collector.get_facter_output(test_collector) == to_bytes('facter --puppet --json')

# Unit test

# Generated at 2022-06-13 02:03:08.784163
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    find_facter()

# Generated at 2022-06-13 02:03:12.308356
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    class_ = FacterFactCollector
    class_.find_facter = lambda self, module: '/usr/bin/facter'
    facter_path = class_.find_facter(class_, None)
    assert facter_path == '/usr/bin/facter'


# Generated at 2022-06-13 02:03:20.629675
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    from ansible.module_utils.facts.collector import FactsCollector
    from ansible.module_utils.facts.collector import BaseFactCollector
    
    test_module = AnsibleModuleMock()
    fake_collectors = [TestClass1(), TestClass2()]
    fact_collector = FactsCollector(module=test_module,
                                    collectors=fake_collectors)
    # test method find_facter of class FacterFactCollector
    result = FacterFactCollector().find_facter(test_module)
    assert result == '/bin/facter'


# Generated at 2022-06-13 02:03:30.136067
# Unit test for method get_facter_output of class FacterFactCollector

# Generated at 2022-06-13 02:03:41.221928
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    from ansible.module_utils.facts import ansible_collector
    from ansible.module_utils.facts.ansible_collector import AnsibleCollector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    fact_collector = FacterFactCollector()
    fact_collector.module.run_command = lambda cmd: (1, cmd.split()[-1], '')
    fact_collector.module.get_bin_path = lambda cmd, opt_dirs: cmd
    assert fact_collector.find_facter(fact_collector.module) == 'facter'

    fact_collector.module.run_command = lambda cmd: (1, cmd.split()[-1] + '_cmd', '')

# Generated at 2022-06-13 02:03:49.637081
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    from ansible.module_utils import facts
    from ansible.module_utils.facts import collector

    mock_module = facts.get_module()

    # Empty facter output
    mock_run_command = {
        'retcode': 0,
        'stdout': '',
        'stderr': ''
    }
    mock_run_command_retval = [
        mock_run_command['retcode'],
        mock_run_command['stdout'],
        mock_run_command['stderr']
    ]
    mock_module.run_command = lambda *args, **kwargs: mock_run_command_retval

    mock_get_bin_path = '/usr/bin/facter'

    mock_module.get_bin_path = lambda *args, **kwargs: mock_get_bin_

# Generated at 2022-06-13 02:03:57.388497
# Unit test for method find_facter of class FacterFactCollector

# Generated at 2022-06-13 02:04:02.762119
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    import sys
    if sys.version_info[0] >= 3:
        from unittest.mock import Mock, patch
    else:
        from mock import Mock, patch
    import logging

    m = Mock()
    m.find_facter.return_value = 'facter_path'

    module_mock = Mock()
    facter_path = FacterFactCollector(collectors=m).find_facter(module_mock)
    assert facter_path == 'facter_path'


# Generated at 2022-06-13 02:04:10.327272
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    class FakeModule(object):
        def __init__(self):
            self.params = {}
            self.bin_path = None
            self.run_command_rc = 0
            self.run_command_out = "{}"
            self.run_command_err = ""

        def get_bin_path(self, exe, opt_dirs=None, required=False):
            return self.bin_path

        def run_command(self, cmd, check_rc=True):
            return self.run_command_rc, self.run_command_out, self.run_command_err

    my_module = FakeModule()

    # Test case 1 - /usr/bin/facter exists
    my_module.bin_path = '/usr/bin/facter'
    facter = FacterFactCollector()

# Generated at 2022-06-13 02:04:18.075935
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    q = FacterFactCollector()

    # Test with module that has facter installed
    class TestModule:
        @staticmethod
        def get_bin_path(path, opt_dirs=None):
            return '/bin/facter' if path == 'facter' else None


# Generated at 2022-06-13 02:04:47.641685
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():

    class TestModule(object):
        def __init__(self):
            self.bin_path = ''
        def get_bin_path(self, name, opt_dirs=None):
            return self.bin_path

        def run_command(self, command):
            return rc, stdout, stderr

    class TestFacterFactCollector(FacterFactCollector):
        def __init__(self, collectors=None, namespace=None):
            super(TestFacterFactCollector, self).__init__(collectors=collectors, namespace=namespace)

    def test(command, expected_rc, expected_output, expected_err):
        print('Testing command: ' + command)
        module = TestModule()
        # Set bin_path to simulate facter installed or not

# Generated at 2022-06-13 02:04:50.063778
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    facter_path = FacterFactCollector().find_facter(module)
    assert facter_path is not None


# Generated at 2022-06-13 02:04:58.511859
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    # this is a bit wonky because i am mocking the module, but it is
    # a good start.
    # TODO: mock the shell command, and test failures
    # FIXME: what if facter is installed, but no ruby-json ...

    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.namespace

    # set up a test dict
    collected_facts = dict()

    # create a facter fact collector
    facter_fact_collector = ansible.module_utils.facts.collector.FacterFactCollector()

    # mock the module
    class MockModule:
        def __init__(self):
            self._bin_path = dict()


# Generated at 2022-06-13 02:05:09.003149
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    import ansible.module_utils.facts.collector

    class ModuleFake:
        def __init__(self, out, err, rc):
            self.out = out
            self.err = err
            self.rc = rc

        def get_bin_path(self, *args, **kwargs):
            return '/opt/puppetlabs/bin/facter'

        def run_command(self, facter_path):
            return self.rc, self.out, self.err

    # test with facter not found
    module = ModuleFake(None, None, None)
    facter = FacterFactCollector()
    assert facter.get_facter_output(module) is None

    # test with facter found but no json option
    module = ModuleFake(None, None, None)
    facter = Facter

# Generated at 2022-06-13 02:05:19.256923
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():

    # Create a mock module object
    class MockModule(object):
        def __init__(self):
            self.params = {}
            self.path = []
            self.run_command_result = 0, '', ''

        def fail_json(self, *args, **kwargs):
            raise Exception()

        def get_bin_path(self, binary, opt_dirs=[]):
            if binary == 'facter':
                return '/path/to/facter'
            elif binary == 'cfacter':
                return '/path/to/cfacter'

        def run_command(self, command):
            return self.run_command_result

    # Create a mock module
    module = MockModule()

    # Create a FacterFactCollector instance
    facter_collector = FacterFactCollector()

    # Do

# Generated at 2022-06-13 02:05:26.813654
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    ff = FacterFactCollector()
    assert ff.find_facter({
        "PATH": "/usr/bin:/bin"
    }) is None

    assert ff.find_facter({
        "PATH": "/usr/bin:/bin",
        "facter_bin": "/usr/local/bin/facter"
    }) == "/usr/local/bin/facter"

    assert ff.find_facter({
        "PATH": "/usr/bin:/bin",
        "cfacter_bin": "/usr/local/bin/cfacter"
    }) == "/usr/local/bin/cfacter"


# Generated at 2022-06-13 02:05:32.258204
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():
    class MockFactCollector:
        def __init__(self, collectors=None, namespace=None):
            self._collectors = collectors
            self._namespace = namespace

    class MockModule:
        def __init__(self):
            pass

        def get_bin_path(self, bin_name, opt_dirs=[]):
            return '/bin/cfacter'


# Generated at 2022-06-13 02:05:37.070339
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.collector import FactCollectorCache

    facter_dict = {}

    with_facter_path = "test/files/demo_module/with_facter"
    no_facter_path = "test/files/demo_module/no_facter"

    # Test with facter installed
    facter_dict['ansible_facts'] = {'facter': {}}
    fact_cache = FactCollectorCache(collectors=[])
    fact_cache.populate(module_path=with_facter_path)

    facter = FacterFactCollector()

# Generated at 2022-06-13 02:05:43.507640
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    from ansible.module_utils.facts.collector import Collector

    module = MockModule()

    fact_collector = Collector()
    fact_collector.populate()
    fact_collector.facter = FacterFactCollector(fact_collector)

    fact_collector.facter.get_facter_output(module)

    assert module.bin_path.call_count == 2
    assert module.bin_path.call_args_list[0] == call('facter', opt_dirs=['/opt/puppetlabs/bin'])
    assert module.bin_path.call_args_list[1] == call('cfacter', opt_dirs=['/opt/puppetlabs/bin'])

    # if facter is installed cfacter is not installed
    # test for facter
    assert module

# Generated at 2022-06-13 02:05:49.687658
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    # Using a custom class for testing to avoid needing to use a real and working
    # module from Ansible during tests.  This does make the test less realisitc
    # but does allow for the test to be easily isolated for the purpose of testing
    # the collection logic.
    class TestModule:
        def __init__(self):
            self.init_success = False
            self.facts = {}

        def get_bin_path(self, *args, **kwargs):
            # Simulate not having facter installed.
            return None

        def run_command(self, args):
            # Simulate an error return code because we don't have facter installed.
            return 1, '', None

        def exit_json(self, **kwargs):
            self.facts = kwargs.get('ansible_facts', {})
            self

# Generated at 2022-06-13 02:06:36.966479
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    # The result will vary on different operating system, so just test exist
    ff = FacterFactCollector()
    # Should return None if module is None
    assert ff.get_facter_output(None) is None
    # Should return dict if module is not None
    assert isinstance(ff.get_facter_output(MockModule(0)), dict)


# Generated at 2022-06-13 02:06:47.486063
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():

    class TestModule:
        def get_bin_path(self, name, opt_dirs):
            return '/opt/puppetlabs/bin/name'

        def run_command(self, cmd):
            return 0, '{"ansible_processor_count": 2, "ansible_processor_cores": 2, "ansible_processor_threads_per_core": 1, "ansible_processor_vcpus": 2, "ansible_processor": "x86_64", "ansible_architecture": "x86_64", "ansible_system": "Linux", "ansible_machine": "x86_64", "ansible_kernel": "Linux", "ansible_kernel_version": "2.6.32-754.22.1.el6.x86_64"}', ''

    module = TestModule()

   

# Generated at 2022-06-13 02:06:54.884821
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():

    from ansible.module_utils.facts.collector import TestModule
    import sys

    class TestFacterFactCollector(FacterFactCollector):
        def find_facter(self, module):
            return 'facter.bin'

        def run_facter(self, module, facter_path):
            if not hasattr(self, 'results'):
                self.results = ''
            self.results += self.fixture

            return 0, self.results, ''


    collector = TestFacterFactCollector()

    module = TestModule()
    module.fail_json = lambda *args, **kwargs: sys.exit(1)
    module.exit_json = lambda *args, **kwargs: sys.exit(0)

    # Happy path

# Generated at 2022-06-13 02:07:00.863019
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    collector = FacterFactCollector()
    class MockModule:
        def get_bin_path(self, name, opt_dirs=None):
            return '/opt/puppetlabs/bin/facter'
        def run_command(self, name):
            return 0, '{"id":"foo"}', ''

    facter_output = collector.get_facter_output(MockModule())
    assert json.loads(facter_output) == {"id": "foo"}


# Generated at 2022-06-13 02:07:08.152205
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    from ansible.module_utils.facts.collector import FactsCollector

    # First, try some fake modules and see that we don't find facter
    for mod in [object, dict, list]:
        collector = FactsCollector(collectors=[FacterFactCollector()])
        result = collector.collect_from(mod, {}).facter.find_facter(mod)
        assert result is None, "find_facter should have returned None with a fake module"

    # Now, use a real ansible module, but mask its methods to not find facter
    mod = FakeModule()
    mod.run_command = lambda a, b, c=None, d=None, e=None: (0, '', '')

# Generated at 2022-06-13 02:07:18.053049
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    from collections import Mapping
    from ansible.module_utils.facts.utils import get_module_object

    class MockModule(object):
        def __init__(self):
            self.params = dict()

        def get_bin_path(self, bin_path, opt_dirs=None, required=False):
            return None

    # Test case with no arguments
    ffc = FacterFactCollector()
    mm = MockModule()
    mm.params['ansible_facts'] = {'facter': {}}
    mm.params['ansible_facts']['facter'] = ffc.collect(module=mm)
    assert isinstance(mm.params['ansible_facts']['facter'], Mapping)

    # Test case with correct arguments
    ffc = FacterFactCollector()
    mm = Mock

# Generated at 2022-06-13 02:07:23.928312
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    import ansible.module_utils.facts.collector

    fact_collector = FacterFactCollector()
    module = ansible.module_utils.facts.collector.FactsCollector()
    facter_path = fact_collector.find_facter(module)
    assert (facter_path != None)


# Generated at 2022-06-13 02:07:31.863074
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    import ansible.module_utils.facts.collector as tmp_module
    from ansible.module_utils.facts import ModuleArgsParser

    class TestAnsibleModule:

        def __init__(self):
            self.params = {}
            self.args = None

        def set_params(self, params):
            self.params = params

        def fail_json(self, **kwargs):
            self.__fail = kwargs

        def get_bin_path(self, app, opt_dirs=[]):
            if app == 'cfacter':
                return ''
            return '/bin/facter'


# Generated at 2022-06-13 02:07:38.427848
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():
    '''
    class MyModule:
        def get_bin_path(self, name, opt_dirs=[]):
            return 'facter'

    def run_command(self, command, check_rc=True):
        return 0, '{\"example\" : \"dummy data in json\"}', ''

    module = MyModule()
    facter_fact_collector = FacterFactCollector()
    rc, out, err = facter_fact_collector.run_facter(module, 'facter')

    assert rc == 0
    assert out == '{\"example\" : \"dummy data in json\"}'
    assert err == ''
    '''
    pass

# Generated at 2022-06-13 02:07:46.985884
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    from ansible.module_utils.facts import FactsJsonDecoder
    from ansible.module_utils.facts import FactsModule
    from ansible.module_utils.facts import FactCollectorRegistry
    class CustomFactsModule(FactsModule):
        def __init__(self):
            FactsModule.__init__(self)
            self.facts_module = None
            self.params = {}