

# Generated at 2022-06-13 01:58:55.236744
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    import os
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common._json_compat import json


# Generated at 2022-06-13 01:59:06.927511
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    class MockModule(object):
        def __init__(self):
            self.params = {
                'path': ['/usr/bin']
            }

        def get_bin_path(self, bin_name, opt_dirs=[]):
            if bin_name in self.params:
                return self.params[bin_name]

        def run_command(self, facter_path):
            # Mock a runs on RHEL system with facter output
            if facter_path == "facter --puppet --json":
                return 0, '{"os":{"family":"RedHat","hardware":"x86_64","name":"Fedora"}}', None

        def __getattr__(self, name):
            return None

    # Test for RHEL OS with facter
    module = MockModule()
    collected_facts = {}
   

# Generated at 2022-06-13 01:59:17.160316
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    class MI(object):
        def get_bin_path(self, _, opt_dirs=None):
            return ('facter')

        def run_command(self, cmd):
            return 0, ('{"ansible_facter": {} }'), ''

    facter_obj = FacterFactCollector()
    facter_dict = facter_obj.get_facter_output(MI())
    assert facter_dict

    class MI(object):
        def get_bin_path(self, _, opt_dirs=None):
            raise Exception('Failed')

        def run_command(self, cmd):
            raise Exception('Failed')

    facter_obj = FacterFactCollector()
    facter_dict = facter_obj.get_facter_output(MI())
    assert not facter_dict

# Generated at 2022-06-13 01:59:27.038614
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    module = AnsibleModuleMock('shell', '', '')
    base_collector = BaseFactCollector(module)
    facter_collector = FacterFactCollector(module, base_collector.namespace)
    assert facter_collector.collect() == {}
    module = AnsibleModuleMock('shell', '', '{"network": {"interfaces": {"eth0" : { "ip": "192.168.0.10"}}}}')
    facter_collector = FacterFactCollector(module, base_collector.namespace)
    assert facter_collector.collect() == {"facter_network": {"interfaces": {"eth0" : { "ip": "192.168.0.10"}}}}

# Generated at 2022-06-13 01:59:32.722281
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():
    from ansible.module_utils.facts.collector import BaseFactCollector
    import ansible.module_utils
    import ansible.module_utils.basic

    fc = FacterFactCollector()
    module = ansible.module_utils.basic.AnsibleModule(argument_spec={})
    # The command executed by run_facter is facter_path + " --puppet --json"
    # So the return value is a list [facter_path, "--puppet", "--json"]
    facter_path = fc.find_facter(module)
    assert type(fc.run_facter(module, facter_path)) == tuple


# Generated at 2022-06-13 01:59:42.587232
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    """
    Testcase for method FacterFactCollector.get_facter_output(module)
    """
    class MockModule(object):
        """
        A mock object to fake the AnsibleModule class
        """
        def get_bin_path(self, app, opt_dirs=None):
            """
            Fakes the AnsibleModule.get_bin_path() method
            """
            if app == 'facter':
                return '/opt/puppetlabs/bin/facter'
            if app == 'cfacter':
                return '/opt/puppetlabs/bin/cfacter'

        def run_command(self, cmd):
            """
            Fakes the AnsibleModule.run_command(cmd) method
            """
            json_output = '{"_id": ""}'

# Generated at 2022-06-13 01:59:47.722047
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    from ansible.module_utils import basic
    from ansible.module_utils.facts.utils import get_collector_namespaces
    import ansible.module_utils.facts.collectors
    ansible.module_utils.facts.collectors.FacterFactCollector = FacterFactCollector

    module = basic.AnsibleModule(argument_spec=dict())
    namespaces = get_collector_namespaces(module)

    facter_facts = namespaces.get('facter')

    assert facter_facts['facter_ipaddress'] == '127.0.0.1'
    assert facter_facts['facter_uptime_seconds'] > 100
    assert facter_facts['facter_uptime']
    assert facter_facts['facter_uptime_days'] > 0


# Generated at 2022-06-13 01:59:48.874092
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    assert FacterFactCollector.get_facter_output(module) == out

# Generated at 2022-06-13 01:59:55.893851
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():
    from ansible.module_utils.facts.system.facter import FacterFactCollector
    facter_fact_collector = FacterFactCollector()
    from ansible.module_utils.facts.system.facter import MockModule
    module = MockModule()
    facter_path = '/usr/bin/facter'

    rc, out, err = facter_fact_collector.run_facter(module, facter_path)

    # returned value should be 0, out should be not empty, err should be empty
    assert(rc == 0 and out != '' and err == '')

# Generated at 2022-06-13 01:59:59.845337
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    class Module(object):
        def get_bin_path(self, *args, **kwargs):
            return '/tmp/facter_bin'


# Generated at 2022-06-13 02:00:08.940090
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():
    # Facter should be found
    from ansible.module_utils.common.process import get_bin_path
    from ansible.module_utils.facts.collector import get_collector_subclass
    from ansible.module_utils.facts import get_module_argument_spec

    facter_path = get_bin_path('facter', opt_dirs=['/opt/puppetlabs/bin'])

    module_args = get_module_argument_spec(supports_check_mode=False)
    facter_collector = get_collector_subclass('facter')(module=module_args)

    rc, out, err = facter_collector.run_facter(module_args, facter_path)

    # The return code should be 0
    assert(rc == 0)
    # The std

# Generated at 2022-06-13 02:00:20.801401
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    import os
    import tempfile

    class FakeModule:
        def __init__(self):
            self._tmp_paths = []

        def run_command(self, cmd):
            if not cmd.startswith(self._tmp_paths[0]):
                return (1, '', 'Unexpected tmp facter command path')

            (prefix, suffix) = cmd.split(' ', 1)
            if suffix == '--puppet --json':
                return (0, json.dumps({'key': 'value'}), '')
            else:
                return (1, '', 'Unexpected tmp facter command')

        def get_bin_path(self, binary, opt_dirs=[]):
            fd, path = tempfile.mkstemp(prefix='ansible-fake-facter', suffix=binary)
           

# Generated at 2022-06-13 02:00:28.983204
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    # First we have to simulate the import of a class to a module
    import sys
    module = sys.modules[__name__]

    # Now we create an instance and call the get_facter_output method
    facter_fact_collector = FacterFactCollector()
    facter_fact_collector.get_facter_output(module)

    # Check the returned object by get_facter_output
    assert facter_fact_collector.get_facter_output(module) is not None, \
           "Facter is not installed, run 'sudo apt-get install facter' to install it"


# Generated at 2022-06-13 02:00:39.191014
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    from ansible.module_utils.facts import ansible_collections
    from ansible.module_utils.facts.system import DarwinSystem

    facter_path = "/usr/local/bin/facter"

    # Mock module
    module = ansible_collections.ansible.builtin.system.Darwin('/dev/null')
    module.run_command = lambda x, y=None: (0, facter_path, '')

    # Mock system
    system = DarwinSystem()
    system.distribution = lambda: 'Darwin'

    # Init the collector
    fact_collector = FacterFactCollector(collectors=[system])
    fact_collector.module = module

    # Execute the collector
    output = fact_collector.get_facter_output(module)

    assert output is not None

# Generated at 2022-06-13 02:00:47.327906
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    import ansible.module_utils.facts.collector
    # load the test file
    fixture = ansible.module_utils.facts.collector.get_pytest_fixture('FacterFactCollector',
                                                                      'test/unit/module_utils/facts/collector/fixtures/facter.json')

    # instantiate the class to be tested
    instance = FacterFactCollector()

    # call the method collect
    result = instance.collect(fixture)

    assert isinstance(result, dict)
    assert 'operatingsystemmajrelease' in result
    assert 'uptime_hours' in result
    assert 'virtual' in result
    assert 'ipaddress' in result
    assert 'id' in result
    assert 'hardwareisa' in result
    assert 'processorcount' in result

# Generated at 2022-06-13 02:00:54.346440
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    class FakeModule(object):
        def fail_json(self, msg):
            raise Exception(msg)

        def get_bin_path(self, app, opt_dirs=[]):
            return "/bin/%s" % (app,)

    facter_fact_collector = FacterFactCollector()
    facter_path = facter_fact_collector.find_facter(FakeModule())
    assert facter_path == "/bin/facter"

# Generated at 2022-06-13 02:00:58.258510
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    # Unit test with the real module
    ffc = FacterFactCollector()
    # TODO: it's not possible to initialize a FacterFactCollector without a module,
    # so lets not test this case.
    try:
        print(ffc.collect(None))
    except:
        pass

# Generated at 2022-06-13 02:01:06.778479
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    FCT = FacterFactCollector()
    
    class MockModule(object):
        @staticmethod
        def get_bin_path(name, opt_dirs):
            if name == 'cfacter':
                return '/usr/local/sbin/cfacter'
            elif name == 'facter':
                return '/usr/local/sbin/facter'
            else:
                return None

        @staticmethod
        def run_command(command):
            return 0, "{\"osfamily\": \"RedHat\", \"processor0\": \"Intel(R) Core(TM) i5-7200U CPU @ 2.50GHz\"}", ""
    
    facter_dict = FCT.get_facter_output(MockModule())
    

# Generated at 2022-06-13 02:01:17.486176
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():

    class ModuleTest(object):
        def get_bin_path(self, arg1, **kwargs):
            if arg1 == 'facter':
                return '/usr/bin/facter'
            else:
                return None

        def run_command(self, arg1):
            facter_output = {'path': '/foo'}
            if arg1 == '/usr/bin/facter --puppet --json':
                return 0, json.dumps(facter_output), None
            else:
                return 1, '', 'command not found'

    module = ModuleTest()
    facter_collector = FacterFactCollector()
    has_facter = facter_collector.get_facter_output(module)
    assert has_facter is not None

# Generated at 2022-06-13 02:01:24.839028
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    sample_directories = ['/opt/puppet/bin', '/usr/bin/']

    # TODO: implement more tests that explicitely test the collected facts.
    # For now we just check that the method doesn't fail.
    def test_facter(self, cmd):
        # Simulate Puppet Enterprise installation
        pe_install = "/opt/puppetlabs/puppet/bin/facter"
        if cmd == pe_install + " --puppet --json":
            return 0, '{"facter": "facter"}', ""
        # Simulate agent installation
        agent_install = "/opt/puppet/bin/facter"
        if cmd == agent_install + " --puppet --json":
            return 0, '{"facter": "facter"}', ""
        # Simulate facter not available

# Generated at 2022-06-13 02:01:40.574143
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():
    test_module = AnsibleModule(argument_spec=dict())

# Generated at 2022-06-13 02:01:48.577862
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    class MockModule(object):
        def __init__(self, rc, out, err):
            self.rc = rc
            self.out = out
            self.err = err

        def run_command(self, cmd, opt_dirs=[]):
            return self.rc, self.out, self.err

        def get_bin_path(self, exe, opt_dirs=[]):
            if exe == "facter":
                return "/opt/puppetlabs/bin/facter"
            if exe == "cfacter":
                return None

    class FacterFactCollectorMock(FacterFactCollector):
        _facter_fact_collector_test = True


# Generated at 2022-06-13 02:01:57.076989
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    facter = FacterFactCollector()
    class DummyModule():
        def get_bin_path(self, name, opt_dirs=None):
            if name == "cfacter" and opt_dirs == ['/opt/puppetlabs/bin']:
                return "/bin/cfacter"
            else:
                return None
    module = DummyModule()
    assert facter.find_facter(module) == "/bin/cfacter"

    class DummyCfacterModule():
        def get_bin_path(self, name, opt_dirs=None):
            if name == "cfacter" and opt_dirs == ['/opt/puppetlabs/bin']:
                return None
            elif name == "facter" and opt_dirs is None:
                return "/bin/facter"
           

# Generated at 2022-06-13 02:02:08.310228
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils._text import to_bytes

    collector = get_collector_instance(FacterFactCollector)
    fact = None
    module = None
    facter_path = collector.find_facter(module)
    assert facter_path.endswith(to_bytes('facter'))

    fact = {}
    facter_path = collector.find_facter(module)
    assert facter_path.endswith(to_bytes('facter'))

    fact = { 'PATH': '/usr/bin:/bin' }
    facter_path = collector.find_facter(module)
    assert facter_path.endswith(to_bytes('facter'))


# Generated at 2022-06-13 02:02:18.120955
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    from ansible.module_utils.facts import get_collector_class
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    module = MockModule()
    FactCollector = get_collector_class('facter')

    facter_instance = FactCollector()
    facter_instance.find_facter = MagicMock(return_value=True)
    facter_instance.find_facter.return_value = '/bin/facter'

    facter_instance.run_facter = MagicMock(return_value=True)
    facter_instance.run_facter.return_value = 0, 'facter result', ''


# Generated at 2022-06-13 02:02:19.080315
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    pass


# Generated at 2022-06-13 02:02:26.983082
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    class MockModule(object):
        def get_bin_path(self, command, opt_dirs=None):
            _get_bin_path_call_count = 0

            # Test that cfacter will fail
            if _get_bin_path_call_count == 0:
                _get_bin_path_call_count += 1
                raise Exception

            # Test that facter will fail
            if _get_bin_path_call_count == 1:
                _get_bin_path_call_count += 1
                raise Exception

            # Test that facter will pass
            if _get_bin_path_call_count == 2:
                _get_bin_path_call_count += 1
                return "/usr/bin/facter"

            # Test that cfacter will pass

# Generated at 2022-06-13 02:02:31.711777
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    facter_collector = FacterFactCollector()
    class MockModule(object):
        def get_bin_path(self, name, opt_dirs=None):
            return "facter"

    mock_module = MockModule()
    facter_collector.find_facter(mock_module)


# Generated at 2022-06-13 02:02:39.236704
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    # In order to test the method get_facter_output of class FacterFactCollector,
    # we need to provide mocks for the following object:
    # class AnsibleModule:
    #    def get_bin_path(self, arg1, opt_dirs=None):
    #    def run_command(self, arg1):
    #
    # We can use the mock library for this.
    # In order not to modify the library code, we use the imp module.
    from imp import reload
    from mock import MagicMock

    # make the original method available via a new name
    FacterFactCollector.original_get_facter_output = FacterFactCollector.get_facter_output

    # define the mock

# Generated at 2022-06-13 02:02:51.307115
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    import os
    import sys

    # Import and initialize the testing framework
    import unit
    test = unit.init()

    # Prep test vars
    script_dir = os.path.dirname(__file__)
    data_dir = os.path.join(script_dir, 'data')

    sys.path.append(data_dir)

    from test_module_utils import TestAnsibleModule

    # Test
    facter_collector = FacterFactCollector()

    ansible_module_args = dict()

    # Test that facter_path equals path to cfacter if present,
    # and the path to facter otherwise
    os.chdir(os.path.join(data_dir, 'facter_in_both'))

# Generated at 2022-06-13 02:03:11.232225
# Unit test for method run_facter of class FacterFactCollector

# Generated at 2022-06-13 02:03:21.743991
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    import ansible.module_utils.facts.system.facter

    find_facter = ansible.module_utils.facts.system.facter.FacterFactCollector.find_facter

    class FakeModule(object):
        def get_bin_path(self, binary, opt_dirs=[]):
            try:
                assert binary == 'facter'
                return self.binaries[binary]
            except (AttributeError, AssertionError):
                raise

    m = FakeModule()

    m.binaries = dict(facter=None, cfacter=None)
    assert find_facter(m) is None

    m.binaries = dict(facter='/opt/puppetlabs/bin/facter', cfacter=None)

# Generated at 2022-06-13 02:03:30.228622
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():

    # Mock a module
    module = AnsibleModule(argument_spec={})

    # Mock values for module.get_bin_path

# Generated at 2022-06-13 02:03:41.261141
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    import mock
    from ansible.module_utils.facts.collector.facter import FacterFactCollector
    # Finds facter
    mock_module = mock.MagicMock(return_value='/opt/puppetlabs/bin/facter')
    mock_module.get_bin_path.return_value = '/opt/puppetlabs/bin/facter'
    facter_collector = FacterFactCollector()
    assert facter_collector.find_facter(mock_module) == '/opt/puppetlabs/bin/facter'
    # Facter not installed
    mock_module.get_bin_path.return_value = None
    facter_collector = FacterFactCollector()
    assert facter_collector.find_facter(mock_module) is None



# Generated at 2022-06-13 02:03:51.143848
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    import os

    class ModuleMock:
        def get_bin_path(self, name):
            if name == 'cfacter':
                return None
            elif name == 'facter':
                return '/usr/local/bin/facter'
            else:
                self.fail('Unexpected call to get_bin_path(): %s' % name)

        def run_command(self, cmd):
            if cmd != '/usr/local/bin/facter --puppet --json':
                self.fail('Unexpected call to run_command(): %s' % cmd)
            return 0, '{"architecture": "x86_64", ... }', ''

        def fail(self, msg):
            raise Exception(msg)

    module = ModuleMock()
    module.ENV = os.environ.copy()
    facter

# Generated at 2022-06-13 02:03:57.034828
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    test_module=type('',(),{})
    test_module.PATH = '/opt/puppetlabs/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
    test_module.get_bin_path = lambda self,*args,**kwargs: '/opt/puppetlabs/bin/facter' if args[0]=='facter' else None
    fact_collector = FacterFactCollector()
    assert fact_collector.find_facter(test_module) == '/opt/puppetlabs/bin/facter'


# Generated at 2022-06-13 02:04:05.104061
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():
    def setup_module(self, module):
        pass


# Generated at 2022-06-13 02:04:09.983118
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    '''Unit test for method collect of class FacterFactCollector'''

    # import the module
    from ansible.module_utils.facts.collectors import FacterFactCollector

    # Create a instance of class FacterFactCollector
    facter_collector = FacterFactCollector()

    # Test facter is not installed
    facter_collector.find_facter = lambda module: None
    assert facter_collector.collect() == {}

    # Test facter is installed but not cfacter
    # Test run facter command failed
    def find_facter_1(module):
        return '/usr/bin/facter'

    def run_facter_1(module, facter_path):
        return 1, '', ''

    facter_collector.find_facter = find_facter_1
   

# Generated at 2022-06-13 02:04:16.258053
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    class FakeModule(object):
        def get_bin_path(self, path, opt_dirs):
            return '/bin/' + path

    class FakeAnsibleModule(object):
        def get_bin_path(self, path, opt_dirs):
            return '/bin/' + path

        def run_command(self, cmd):
            return 0, '{"factname": "factvalue"}', ''

    facter_collector = FacterFactCollector(collectors=[])

    result = facter_collector.collect(FakeAnsibleModule(), {})
    assert result['facter'] == {'factname': 'factvalue'}

# Generated at 2022-06-13 02:04:21.739725
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    class FacterFactCollectorStub(FacterFactCollector):
        def __init__(self):
            class ModuleStub:
                def get_bin_path(self, name, **kwargs):
                    return name

            self.module = ModuleStub()

        def find_facter(self, module=None):
            return super(FacterFactCollectorStub, self).find_facter(module=module)

    ffcs = FacterFactCollectorStub()
    facter_path = ffcs.find_facter()
    assert facter_path == 'facter'



# Generated at 2022-06-13 02:04:47.351474
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    try:
        import ansible.module_utils.facts.collector.facter
        o = ansible.module_utils.facts.collector.facter.FacterFactCollector()
        o.find_facter(None)
    except (NameError, Exception) as e:
        print(e)

# Generated at 2022-06-13 02:04:56.893328
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    import os
    import sys
    import tempfile

    # Create a temporary module object
    tmpdir = tempfile.mkdtemp()
    sys.path.append(tmpdir)
    with open(os.path.join(tmpdir, 'ansible_module_test.py'), 'w') as f:
        f.write('#!/usr/bin/python -tt\n')
        f.write('import ansible.module_utils.facts.collector')
        f.write('from ansible.module_utils.facts.collector.facter import FacterFactCollector')
        f.write('import ansible.module_utils.basic')
        f.write('import ansible.module_utils.facts.namespace')
        f.write('from ansible.module_utils.facts.namespace import PrefixFactNamespace')


# Generated at 2022-06-13 02:05:07.308500
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    from ansible.module_utils.facts.collector import FactsCollector

    # Our module object
    module = AnsibleModule(
        argument_spec = dict()
    )

    # Create a dictionary of values to patch into module_utils.basic.AnsibleModule
    mod_globals = {
        "facter_path": None
    }

    # Replace some attributes of the module object with our mocked values
    monkeypatch_module(module, mod_globals)

    # Create our facter collector object
    facter_collector = FacterFactCollector()

    # Call the find_facter function of the facter collector object
    facter_path = facter_collector.find_facter(module)
    assert None == facter_path


# Generated at 2022-06-13 02:05:18.476990
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    from ansible.module_utils.facts.utils import ModuleTempDirHelper
    from ansible.module_utils.facts.collector import get_file_content

    from ansible.module_utils.facts import ModuleDummyModule
    module = ModuleDummyModule()

    facter_path = '/usr/bin/facter'
    facter_content = b'{"test":"test_value"}\n'

    with ModuleTempDirHelper() as temp_dir_helper:
        temp_dir_helper.create_path(facter_path)

        temp_dir_helper.set_content(facter_path, facter_content)

        facter_fact_collector = FacterFactCollector()
        facter_output = facter_fact_collector.get_facter_output(module)

        assert get_file

# Generated at 2022-06-13 02:05:26.178204
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

    # Create mocked module
    class module(object):
        def get_bin_path(self, program, opt_dirs=[]):
            if program == 'cfacter':
                return '/opt/puppetlabs/bin/cfacter'
            elif program == 'facter':
                return '/opt/puppetlabs/bin/facter'
        def run_command(self, cmd):
            if cmd == '/opt/puppetlabs/bin/cfacter --puppet --json':
                return 0, '{"cfacter_output":"cfacter output"}', ''

# Generated at 2022-06-13 02:05:33.963359
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    from ansible.module_utils.facts.collector import _get_collectors_from_namespace
    class Module:
        def get_bin_path(self, cmd, opt_dirs=[]):
            return None
        def run_command(self, cmd):
            return 0, '', ''
    mod = Module()
    facter = FacterFactCollector(namespace=None)
    facter.collect(module=mod)
    facts = facter.get_facts()
    assert 'facter_uptime_days' not in facts

# Generated at 2022-06-13 02:05:41.856622
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    from ansible.module_utils.facts.base_facts import module_facts

    def dummy_get_bin_path(name, opt_dirs=[]):
        # mock get_bin_path
        # TODO: Test more than the mock to cover a neg case
        return '/opt/puppetlabs/bin/facter'

    def dummy_run_command(cmd):
        # TODO: Test more than the mock to cover a neg case
        assert '/opt/puppetlabs/bin/facter --puppet --json' == cmd
        return 0, '{"kernel":"Linux"}', ''

    setattr(module_facts, 'get_bin_path', dummy_get_bin_path)
    setattr(module_facts, 'run_command', dummy_run_command)

    # Test with a dummy module using mocked-out get

# Generated at 2022-06-13 02:05:46.130205
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    from ansible.module_utils.facts import default_collectors

    f = FacterFactCollector(collectors=default_collectors)

    class MockModule(object):
        def get_bin_path(self, name, opt_dirs=None):
            return "/usr/local/bin/" + name

    m = MockModule()
    assert f.find_facter(m) == "/usr/local/bin/cfacter"



# Generated at 2022-06-13 02:05:52.024611
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    # create a module object to pass to the collect method
    class MockModule:

        def __init__(self, values):
            self.values = values

        # set up ansible.module_utils.facts.collector.get_file_content
        def get_file_content(self, filepath):
            if filepath == '/etc/ansible/facts.d/facter.fact':
                return self.values

            return None

        # set up ansible.module_utils.facts.collector.get_bin_path
        def get_bin_path(self, bin_name, opt_dirs=[]):
            # If bin_name is cfacter, return path to cfacter_bin
            # Else return path to facter_bin
            if bin_name == 'cfacter':
                return self.values['cfacter_bin']

# Generated at 2022-06-13 02:06:01.753116
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    # Test successful run when both facter and cfacter are found
    module = MagicMock()
    module.get_bin_path.return_value = '/opt/puppetlabs/bin/cfacter'
    facterFactCollector = FacterFactCollector()
    assert facterFactCollector.find_facter(module) == '/opt/puppetlabs/bin/cfacter'
    assert facterFactCollector.find_facter(module) == '/opt/puppetlabs/bin/cfacter'

    # Test successful run when only facter is found
    module.get_bin_path.return_value = '/opt/puppetlabs/bin/facter'
    facterFactCollector = FacterFactCollector()

# Generated at 2022-06-13 02:06:54.640021
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():

    from ansible.module_utils.facts import ModuleFacts
    from ansible.module_utils.facts.collector import FactsCollector

    class TestModule(object):
        def get_bin_path(self, name, opt_dirs=None):
            return '/usr/bin/{}'.format(name)


# Generated at 2022-06-13 02:06:59.338910
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    module_params = {'platform': 'openbsd'}
    module = AnsibleModule(argument_spec=module_params)
    facter_factcollector = FacterFactCollector()
    assert facter_factcollector.find_facter(module) is None
    assert facter_factcollector.get_facter_output(module) is None

# Generated at 2022-06-13 02:07:00.541196
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    module = AnsibleModule()
    assert FacterFactCollector().collect(module) == {}

# Generated at 2022-06-13 02:07:07.742086
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    from ansible.module_utils.facts import ModuleTestCase
    from ansible.module_utils.facts.collector import BaseFactCollector

    class TestFactCollector(BaseFactCollector):
        name = 'test'

    module = ModuleTestCase.create_test_module(
        module_name='facter',
        module_args={}
    )

    fact_collector = TestFactCollector()

    fact_facter_collector = FacterFactCollector(collectors=[fact_collector])
    fact_facter_collector.find_facter(module)
    module.set_bin_path('cfacter', '/opt/puppetlabs/bin/cfacter')
    fact_facter_collector.find_facter(module)

# Generated at 2022-06-13 02:07:12.558398
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    from ansible.module_utils.facts.utils import get_collector_instance

    fact_collector = get_collector_instance(FacterFactCollector)
    facts = fact_collector.collect()

    assert isinstance(facts, dict)
    assert 'facter_architecture' in facts

# Generated at 2022-06-13 02:07:20.552282
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    from ansible.module_utils.facts.collector.system import SystemFactCollector
    from ansible.module_utils.facts.collector.augeas import AugeasFactCollector
    from ansible.module_utils.facts.collector.distribution import DistributionFactCollector
    module = MockModule()
    facter_path = "/opt/puppetlabs/bin/cfacter"

    # Should exit with no error, out is empty and err contains:
    # msg 1
    module.run_command_exit_vals = [0, '', 'msg 1\n']
    facter_output = FacterFactCollector().get_facter_output(module)
    assert facter_output == ''

    # Should exit with error, out contains:
    # { "facter": { "fact1": "value1", "fact

# Generated at 2022-06-13 02:07:25.844884
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    class TestModule(object):
        @staticmethod
        def run_command(*args, **kwargs):
            return 0, "", ""

        @staticmethod
        def get_bin_path(*args, **kwargs):
            return '/usr/bin/facter'
    facter_obj = FacterFactCollector()
    facter_obj.get_facter_output(TestModule())

# Generated at 2022-06-13 02:07:33.505806
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    from ansible.module_utils.facts.collector import Collector

    # Mocks to use
    class MockFacterFactCollector(FacterFactCollector):
        def get_facter_output(self, module):
            return '{"fact_a":"value_a","fact_b":"value_b"}'

    # Make sure that if facter is not installed, and things
    # pass through, we get an empty dict back
    mock_module = None
    mock_collector = Collector()
    mock_FacterFactCollector = MockFacterFactCollector(collectors=[mock_collector])

    result = mock_FacterFactCollector.collect(module=mock_module)
    assert result == {}

    import tempfile
    import shutil
    import os

    # Make sure that if facter is installed, but fails,

# Generated at 2022-06-13 02:07:36.768291
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    collector = FacterFactCollector()

    mocked_module = type('MockedModule', (object,), {
        '_find_needle.return_value': '/usr/bin/facter',
    })

    module = mocked_module()

    assert collector.find_facter(module) == '/usr/bin/facter'


# Generated at 2022-06-13 02:07:39.381960
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    ''' Unit test for method find_facter of class FacterFactCollector '''
    module = None
    facter_collector = FacterFactCollector(module=module)
    # Execute find_facter
    module_retval = facter_collector.find_facter(module)
    # Assert result
    assert module_retval is None
