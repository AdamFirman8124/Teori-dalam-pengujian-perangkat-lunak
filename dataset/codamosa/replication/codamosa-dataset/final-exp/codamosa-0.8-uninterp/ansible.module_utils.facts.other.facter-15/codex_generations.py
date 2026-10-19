

# Generated at 2022-06-13 01:58:50.744456
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    # Init a FacterFactCollector object
    facter_collector = FacterFactCollector()

    # Create a fake module object and assign facter_path to it
    fake_module = {}
    fake_module.facter_path = '/usr/bin/facter'

    # Call the method under test
    facter_output = facter_collector.get_facter_output(fake_module)

    # Should return the correct facter output
    assert facter_output == b'{ "facterversion": "3.13.1" }\n'

# Generated at 2022-06-13 01:58:57.881705
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    from ansible.module_utils.facts.collector import ModuleUtilsCollector
    import tempfile

    class mock_module(object):
        def __init__(self):
            self.run_command_called = 0
            self.run_command_results = []

        def get_bin_path(self, executable, required=False, opt_dirs=[]):
            if executable == 'facter':
                return '/usr/bin/facter'
            elif executable == 'cfacter':
                return None
            else:
                return None

        def run_command(self, cmd, check_rc=True, close_fds=True, data=None, binary_data=False):
            self.run_command_called += 1
            return self.run_command_results.pop(0)

    # create a module for the module

# Generated at 2022-06-13 01:59:08.647636
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    import ansible.module_utils.facts.collector as facts_collector
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts.namespace import PrefixFactNamespace
    from ansible.module_utils._text import to_text

    class TestModule:
        def __init__(self):
            self.facter_path = '/usr/bin/facter'
            self.exit_args = {}
            self.exit_args['rc'] = 0
            self.exit_args['out'] = '{ "facter1" : "value1", "facter2" : "value2" }'
            self.exit_args['err'] = ''


        def get_bin_path(self, *args, **kwargs):
            return self.facter_

# Generated at 2022-06-13 01:59:18.611675
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():

    # Create a mock of class AnsibleModule.
    # This mock can be used in lieu of AnsibleModule during unit testing
    # of methods in class FacterFactCollector.
    class MockAnsibleModule:

        # Return boolean True when method get_bin_path() is invoked
        def get_bin_path(self, name, opt_dirs=None, required=False):
            return True

        # Return return code 0 and string '{"fact_1": "value_1", "fact_2": "value_2"}'
        # when method run_command() is invoked

# Generated at 2022-06-13 01:59:28.568814
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.namespace

    # ansible.module_utils.facts.collector.FactCollectorCache
    facts = ansible.module_utils.facts.collector.FactCollectorCache()

    # ansible.module_utils.facts.namespace.FactNamespace
    fact_namespace = ansible.module_utils.facts.namespace.FactNamespace(
        namespace_name='namespace',
        prefix='prefix_'
    )

    # Test simple output with only hostname
    _, out, _ = ansible.module_utils.basic.AnsibleModule(
    ).run_command('echo \'{"hostname":"test_hostname"}\'',
                  check_rc=True)
    fact_collector = FacterFactCollector

# Generated at 2022-06-13 01:59:38.265172
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    collectors = []
    namespace = None
    facter_collector = FacterFactCollector(collectors=collectors, namespace=namespace)
    
    # Given "facter" is installed in /usr/bin/ directory
    # When find_facter is called
    # Then it will return /usr/bin/facter path
    assert facter_collector.find_facter() == "/usr/bin/facter"
    
    # Given "facter" is not installed
    # When find_facter is called
    # Then it will return None
    assert facter_collector.find_facter() is None
    
    # Given "cfacter" is installed in /usr/local/bin/ directory
    # When find_facter is called
    # Then it will return /usr/local/bin/cfacter path

# Generated at 2022-06-13 01:59:46.745412
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    try:
        import __main__
        from ansible.module_utils.facts.collector import get_collector_instance
    except:
        import ansible.module_utils.facts.collector
        setattr(__main__, '__file__', '/tmp/ansible')
        ansible.module_utils.facts.collector.MODULE_CACHE = {}
        ansible.module_utils.facts.collector.CollectorRegistry = {}
        ansible.module_utils.facts.collector.CollectorCache = {}
        from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.vars.manager import VariableManager
    from ansible.module_utils.facts import ansible_local
    from ansible.module_utils.facts.namespace import PrefixFactNamespace

# Generated at 2022-06-13 01:59:54.414425
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    from ansible.module_utils.facts.collector import get_collector_instance
    # Create instance of this fact collector
    fact_collector = get_collector_instance(FacterFactCollector)

    # Test that trying to find facter without a module raises an error
    fail = False
    try:
        fact_collector.find_facter(None)
    except Exception:
        fail = True
    assert fail

    # Test that trying to find facter with a module, but facter not found, returns None
    import ansible.module_utils.facts.system.system
    fact_collector.find_facter(ansible.module_utils.facts.system.system)

# Generated at 2022-06-13 01:59:59.324338
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    class FakeModule(object):
        def get_bin_path(self, executable, opt_dirs=[]):
            return '/usr/bin/' + executable

    facter_collector = FacterFactCollector()
    facter_path = facter_collector.find_facter(FakeModule())
    assert facter_path == '/usr/bin/cfacter'


# Generated at 2022-06-13 02:00:04.099943
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():
    facter_path = '/opt/puppetlabs/bin/facter'
    facter = FacterFactCollector()
    facter.run_facter = lambda m, p: (0, "{\"facter_fact1\":\"value1\"}", "")
    module = object()
    facter.collect(module=module)
    assert facter._collector_data['facter_fact1'] == 'value1'


# Generated at 2022-06-13 02:00:11.551349
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():

    facter = FacterFactCollector()
    from ansible.modules.extras.cloud.oracle import ocicli
    dummy_module = ocicli
    facter_path = facter.find_facter(dummy_module)
    assert facter_path == "/usr/bin/facter"

# Generated at 2022-06-13 02:00:22.255740
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.namespace
    import ansible.module_utils.facts

    module = Mock()
    module.get_bin_path = Mock(return_value='/bin/facter')
    collectors = [ansible.module_utils.facts.collector.VirtualFactCollector,
                  ansible.module_utils.facts.collector.FacterFactCollector]
    namespace = ansible.module_utils.facts.namespace.FactNamespace()
    ffactor = FacterFactCollector(collectors=collectors, namespace=namespace)
    ffactor.run_facter(module,'/bin/facter')



# Generated at 2022-06-13 02:00:30.804988
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    import os
    import sys
    class TestModule():
        def run_command(self, command):
            if command == facter_path:
                return 0, out, ""
            elif command == facter_path+" --json":
                return 0, out, ""
            elif command == cfacter_path:
                return 0, out, ""
            elif command == cfacter_path+" --json":
                return 0, out, ""
            else:
                return 1, "", ""
        def get_bin_path(self, name, **kwargs):
            if name == "facter":
                return facter_path
            elif name == "cfacter":
                return cfacter_path
            else:
                return None
        def run_command(self, command):
            return 0, out, ""
    input

# Generated at 2022-06-13 02:00:35.018360
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():
    from ansible.module_utils.facts import FacterFactCollector
    from ansible.module_utils.facts.collector import ModuleStub
    module = ModuleStub()
    facter_path = module.get_bin_path('facter', opt_dirs=['/opt/puppetlabs/bin'])

    if facter_path is None:
        print('not istalled')

    rc, out, err = FacterFactCollector.run_facter(None, facter_path)

    print(rc, out, err)
    json_str = out
    facter_dict = json.loads(json_str)
    print(facter_dict)

if __name__ == "__main__":
    test_FacterFactCollector_run_facter()

# Generated at 2022-06-13 02:00:44.394374
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    from ansible.module_utils.facts import ansible_facts

    # Note that this test mirrors the behavior of the previous facter
    # factorial plugin where 'ansible_facter' key is not present in
    # 'ansible_facts' dict.
    facts = ansible_facts.AnsibleFacts(
        dict(_fact_ids=set(['facter']),
             _module_name='ansible.module_utils.facts.network.facter',
             ansible_module=None)
    )

    # Run collect method of FacterFactCollector
    facts.populate()


# Generated at 2022-06-13 02:00:47.883741
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    from ansible.module_utils.facts.collector.system.posix import POSIXFactCollector
    test_obj = FacterFactCollector(collectors=[POSIXFactCollector])
    test_obj.get_facter_output = lambda: '{}'
    assert test_obj.collect() == {}

# Generated at 2022-06-13 02:00:58.631043
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    import os
    import tempfile
    import shutil

    import ansible.module_utils

    class AnsibleModuleMock():
        # In this mock, we pretend that the 'facter' binary is always found and
        # that it alway returns a valid JSON output
        def get_bin_path(self, binary, opt_dirs):
            return '/the/path/of/the/%s/binary' % binary

        def run_command(self, command):
            assert command == '/the/path/of/the/facter/binary --puppet --json'

            # Return the content of a facter dump in a temporary file
            with tempfile.NamedTemporaryFile(mode='w+', delete=False) as f:
                f.write('{')

# Generated at 2022-06-13 02:01:07.390035
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    from ansible.module_utils import basic

    module = basic.AnsibleModule(
        argument_spec=dict()
    )

    ffc = FacterFactCollector()

    def _find_facter(self, module):
        return '/opt/puppetlabs/bin/facter'


# Generated at 2022-06-13 02:01:17.954900
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    from ansible.module_utils import basic
    from ansible.module_utils.basic import AnsibleModule

    class AnsibleModuleWithFindFacter(AnsibleModule):
        def get_bin_path(self, app, opt_dirs=[]):
            if app == 'cfacter':
                return '/opt/puppetlabs/bin/cfacter'
            elif app == 'facter':
                return '/usr/bin/facter'

    module = AnsibleModuleWithFindFacter(argument_spec={}, supports_check_mode=False)
    result = FacterFactCollector().find_facter(module)

    # cfacter found, should return that
    assert result == '/opt/puppetlabs/bin/cfacter'


# Generated at 2022-06-13 02:01:18.513618
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    pass

# Generated at 2022-06-13 02:01:31.917464
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    class Module:
        def get_bin_path(self, binary, opt_dirs=None, required=False):
            raise Exception('Called get_bin_path()')
        def run_command(self, cmd):
            raise Exception('Called run_command()')
    mod = Module()

    # no facter
    find_facter = lambda mod: None
    facter_fact_collector = FacterFactCollector(module=mod,
                                                find_facter=find_facter)
    facter_output = facter_fact_collector.get_facter_output(mod)
    assert facter_output is None
    # Found facter but failed to run it
    find_facter = lambda mod: '/bin/facter'

# Generated at 2022-06-13 02:01:42.304020
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    from ansible.module_utils.facts.system.facter import FacterFactCollector
    from ansible.module_utils import basic

    test_data = {'ansible_python_version': '3.7.3'}
    module = basic.AnsibleModule(argument_spec={})

    test_obj = FacterFactCollector(collectors=None, namespace=None)
    result = test_obj.run_facter(module, 'facter')

    assert result[0] == 0

    result = test_obj.get_facter_output(module)

    assert result is not None
    try:
        facter_dict = json.loads(result)

        assert facter_dict['ansible_python_version'] == test_data['ansible_python_version']
    except Exception:
        assert False

# Generated at 2022-06-13 02:01:50.035528
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    module = json

# Generated at 2022-06-13 02:01:51.416713
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    ffc = FacterFactCollector()
    ffc.get_facter_output('fake module')
    pass

# Generated at 2022-06-13 02:01:58.870017
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    from ansible.module_utils.facts.collector import BaseFactCollector
    # ansible_module_instance should be a ansible BaseAnsibleModule instance
    ansible_module_instance = None
    collected_facts = None

    FacterFactCollector.collect(ansible_module_instance, collected_facts)

    # Test FacterFactCollector.find_facter function
    facter_bin_path = "/usr/bin/facter"
    dummy_module = object()
    dummy_module.get_bin_path = lambda: facter_bin_path
    fact_collector = FacterFactCollector([])
    assert fact_collector.find_facter(dummy_module) == facter_bin_path

    # Test FacterFactCollector.get_facter_output function

# Generated at 2022-06-13 02:02:09.611894
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    class FakeModule():
        def __init__(self, facter_bin_path, cfacter_bin_path):
            self.facter_bin_path = facter_bin_path
            self.cfacter_bin_path = cfacter_bin_path
        def get_bin_path(self, binary_name, opt_dirs = None):
            if binary_name == 'facter':
                return self.facter_bin_path
            elif binary_name == 'cfacter':
                return self.cfacter_bin_path
            return None
    # Test when facter and cfacter are not present
    module = FakeModule(None, None)
    facter_path = FacterFactCollector().find_facter(module)
    assert facter_path is None
    # Test when only cfacter is present
    module

# Generated at 2022-06-13 02:02:17.358650
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    """
    Unit test for method get_facter_output of class FacterFactCollector
    """

    fake_module = MockAnsibleModule()
    with patch('ansible_collections.puppetlabs.facter.plugins.module_utils.facts.collector.FacterFactCollector.run_facter') as test_obj:
        test_obj.return_value = 0, "{'test': 'value'}", 'test error'
        facter_fact_collector = FacterFactCollector()
        facter_fact_collector.get_facter_output(fake_module)


# Generated at 2022-06-13 02:02:25.946822
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    test_dict = dict()
    test_dict['facter_path'] = '/opt/puppetlabs/puppet/bin/facter'
    test_dict['cfacter_path'] = '/opt/puppetlabs/puppet/bin/cfacter'
    test_dict['bin_path_value'] = '/opt/puppetlabs/puppet/bin/facter'
    test_dict['bin_path_value_2'] = '/opt/puppetlabs/puppet/bin/cfacter'
    test_dict['bin_path_value_3'] = None


# Generated at 2022-06-13 02:02:28.360676
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    collector = FacterFactCollector()
    assert collector.get_facter_output() is not None

# Generated at 2022-06-13 02:02:36.946762
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    from ansible.module_utils.facts import test_module_data

    # test case for existent facter
    facter_data = {'facter': {'a': 1}}
    test_module_data['ansible_module'].run_command.return_value = (0, 'test_results', "")
    test_module_data['ansible_module'].get_bin_path.return_value = '/path/to/facter'
    FacterFactCollector.run_facter = lambda self, module, python_path: (0, json.dumps(facter_data), "")

    facter_collector = FacterFactCollector(collectors=None, namespace='ansible')

# Generated at 2022-06-13 02:02:56.611347
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.namespace import BaseFactNamespace
    from ansible.module_utils.facts.utils import get_file_module
    from ansible.module_utils.facts.utils import set_module_instance

    facter_collector = get_collector_instance('facter')
    dummy_collector_list = []
    facter_collector.collectors = dummy_collector_list
    facter_namespace = BaseFactNamespace()
    facter_collector.namespace = facter_namespace

    tmp = get_file_module('/bin/false')
    set_module_instance(tmp)
    result = facter_collector.find_facter(tmp)

# Generated at 2022-06-13 02:03:07.275852
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    import os
    import tempfile
    from ansible.module_utils.facts.collector import FactsCollector
    from ansible.module_utils.facts.utils import get_file_content

    def get_test_module(arguments):
        import ansible.module_utils.facts.system
        new_instance=ansible.module_utils.facts.system.SystemFacts()
        new_instance.args = arguments
        return new_instance

    def test_path_exists(path):
        path = path.split(',')[0]
        return os.path.exists(path)

    class TestAnsibleModule:
        def __init__(self, facts):
            self.facts = facts

        def run_command(self, command):
            module_args = self.facts
            facter_path = module_

# Generated at 2022-06-13 02:03:14.307628
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():
    import ansible.module_utils.facts.collector
    import ansible.module_utils.facts.cache
    import ansible.module_utils.facts.namespace
    import ansible.module_utils.facts.legacy

    module = ansible.module_utils.facts.collection.get_file_module()
    module.get_bin_path = lambda x, opt_dirs=None: '/bin/' + x

    facter_path = FacterFactCollector().find_facter(module)
    assert facter_path
    assert '/bin/facter' in facter_path or '/bin/cfacter' in facter_path

    rc, out, err = FacterFactCollector().run_facter(module, facter_path)
    assert rc == 0

# Generated at 2022-06-13 02:03:23.344761
# Unit test for method get_facter_output of class FacterFactCollector

# Generated at 2022-06-13 02:03:29.164783
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():
    from ansible.module_utils.facts.collector import get_collector_instance
    from ansible.module_utils.facts.collector import BaseFactCollector
    from ansible.module_utils.facts import namespace 
    from ansible.module_utils.facts import collector

    BaseFactCollector.clear_cache()

    # Initialize test class
    fac = get_collector_instance(FacterFactCollector, namespace.BaseNamespace)

    # Testing None
    out = fac.run_facter(None, None)
    assert out == (None, None, None)

# Generated at 2022-06-13 02:03:31.740231
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    facter_collector = FacterFactCollector()
    assert facter_collector.find_facter


# Generated at 2022-06-13 02:03:41.182770
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    import sys, traceback, StringIO
    class _Module():
        def get_bin_path(self, cmd, opt_dirs):
            if cmd == 'facter':
                return '/bin/facter'
            elif cmd == 'cfacter':
                return '/bin/cfacter'
    
    module = _Module()
    facter_path = FacterFactCollector.find_facter(module)
    if facter_path != '/bin/cfacter':
        traceback.print_stack(file=sys.stdout)
        assert False


if __name__ == '__main__':
    test_FacterFactCollector_find_facter()

# Generated at 2022-06-13 02:03:49.373548
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    from ansible.module_utils.facts import collector

    facter_path = '/opt/puppet/bin/facter'

    # Create an instance of the FacterFactCollector class
    fact_collector = FacterFactCollector()

    # The find_facter method must be mocked before calling the get_facter_output method
    fact_collector.find_facter = mock_find_facter

    # The run_facter method must be mocked before calling the get_facter_output method
    fact_collector.run_facter = mock_run_facter

    # Calling get_facter_output must return valid JSON output
    assert valid_json(fact_collector.get_facter_output(None))

# Mocked "find_facter" method

# Generated at 2022-06-13 02:03:57.182696
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    from ansible.module_utils.facts.collector import DictCollector
    from ansible.module_utils import basic

    # Create a FacterFactCollector instance
    facter_collector = FacterFactCollector(collectors=[DictCollector()])

    # Create a fake AnsibleModule to pass to the collect method
    class FakeModule(basic.AnsibleModule):
        def __init__(self, *args, **kwargs):
            self._ansible_no_log = True
            super(FakeModule, self).__init__(*args, **kwargs)

        @property
        def facter_data(self):
            return json.dumps({'fact_1': 'val_1', 'fact_2': 'val_2'})


# Generated at 2022-06-13 02:03:59.409121
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    collector = FacterFactCollector()
    real_bin_path = collector.find_facter(None)
    assert real_bin_path is not None

# Generated at 2022-06-13 02:04:25.131520
# Unit test for method run_facter of class FacterFactCollector
def test_FacterFactCollector_run_facter():
    from ansible.module_utils.facts.collector import call_legacy_facts_callback
    from ansible.module_utils.facts.collector import get_collector_class
    from ansible.module_utils.facts.collector import get_collector_namespace

    def _fake_run_command(cmd):
        return 0, json.dumps({'hostname': 'testhost', 'test': 'testvalue'}), ''

    _fixture_dict = {
        'ansible_facter': {
            'hostname': 'testhost',
            'test': 'testvalue',
        }
    }


# Generated at 2022-06-13 02:04:31.233685
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    from ansible.module_utils.facts.collector import FactsCollector
    import ansible.module_utils.facts.system
    import ansible.module_utils.facts.virtual
    import ansible.module_utils.facts.network
    import ansible.module_utils.facts.distribution
    import ansible.module_utils.facts.operating_system
    import ansible.module_utils.facts.other
    from ansible.module_utils.facts.utils import get_file_content

    class MockModule:
        def __init__(self):
            self.params = {'gather_subset': ['all']}

        def fail_json(self, *args, **kwargs):
            raise Exception('fail_json called')


# Generated at 2022-06-13 02:04:38.322200
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    #Creates instance of class FacterFactCollector
    facter_collector = FacterFactCollector()
    #Creates instance of class MockModule
    module = MockModule()
    #Creates instance of class MockCommand
    command = MockCommand()
    #Assigns an object of class MockCommand to the variable "run_command" of the class MockModule
    module.run_command = command
    #Assigns an object of class MockModule to the variable "module" of the class FacterFactCollector
    facter_collector.module = module
    #Assigns a string to the variable "path" of the class MockModule
    #This string is the path of facter executable
    module.path = '/usr/bin/facter'
    #Creates a string that contains the expected output of method get_facter_output
    #

# Generated at 2022-06-13 02:04:39.690008
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    # Using eval to create the local scope for this test
    scope = {}

# Generated at 2022-06-13 02:04:45.046792
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    class FakeModule(object):
        def __init__(self):
            self._bin_paths = []

        def get_bin_path(self, *paths, **kwargs):
            if len(paths):
                return self._bin_paths.get(paths[0])
            return None

    class FakeAnsibleModule(FakeModule):
        def __init__(self):
            super(FakeAnsibleModule, self).__init__()
            self._bin_paths = {
                'facter': '/opt/puppetlabs/bin/facter',
            }

    assert FacterFactCollector().find_facter(FakeModule()) is None

    fm = FakeAnsibleModule()

# Generated at 2022-06-13 02:04:54.905816
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    from ansible.module_utils._text import to_unicode
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts.collector import get_collector_instance

    module = AnsibleModule(
        argument_spec=dict()
    )

    module.run_command = Mock(return_value=(0, u'', u''))

    fact_collector = get_collector_instance('facter')
    facter_path = fact_collector.find_facter(module)

    module.run_command.assert_called_with(u'facter --puppet --json')
    assert isinstance(facter_path, to_unicode)
    assert facter_path == u'facter'



# Generated at 2022-06-13 02:05:06.372672
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    class MockModule(object):
        def __init__(self):
            self.params = {}
            self.params['path'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
            self.run_command_called_with = None

        def run_command(self, command):
            self.run_command_called_with = command
            if command.endswith('facter --puppet --json'):
                return 0, '{"facter_key": "facter_value"}', ''
            elif command.endswith('cfacter --puppet --json'):
                return 0, '{"facter_key": "facter_value"}', ''
            else:
                return 1, '', 'command not found'


# Generated at 2022-06-13 02:05:11.711281
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    class FakeModule:
        def get_bin_path(self, name, opt_dirs=None):
            return "/opt/puppetlabs/bin/facter"

        def run_command(self, cmd):
            return 0, '{"test":"test"}', ''

    f = FacterFactCollector()
    f.get_facter_output(FakeModule())

# Generated at 2022-06-13 02:05:21.370769
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    class Module(object):
        def get_bin_path(self, bin, opt_dirs=None):
            return None

        def run_command(self, cmd):
            return 0, '{}', ''

    module = Module()
    facterFactCollector = FacterFactCollector()
    facter_output = facterFactCollector.get_facter_output(module)
    assert facter_output is not None
    assert facter_output == '{}'

    class Module(object):
        def get_bin_path(self, bin, opt_dirs=None):
            return '/bin/facter'

        def run_command(self, cmd):
            return 0, '{}', ''

    module = Module()
    facterFactCollector = FacterFactCollector()

# Generated at 2022-06-13 02:05:26.518161
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    class TestModule:
        def get_bin_path(self, executable, opt_dirs=[]):
            if executable == 'facter':
                return '/bin/facter'
            elif executable == 'cfacter':
                return '/bin/cfacter'
            else:
                return None

    facter_collector = FacterFactCollector(None, None)
    module = TestModule()
    facter_path = facter_collector.find_facter(module)
    assert facter_path == '/bin/cfacter'


# Generated at 2022-06-13 02:06:19.465473
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    class FakeModule(object):
        def get_bin_path(self, name, opt_dirs=[]):
            if name == 'cfacter':
                return "cfacter"
            return None


# Generated at 2022-06-13 02:06:28.412746
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():

    class MockModule:
        class MockCommand:
            def __init__(self, cmd, returncode, out, err):
                self.cmd = cmd
                self.returncode = returncode
                self.out = out
                self.err = err

            def __call__(self, *args, **kwargs):
                return self.returncode, self.out, self.err

        def __init__(self, bin_path, run_command):
            self.bin_path = bin_path
            self.run_command = run_command

        def get_bin_path(self, *args, **kwargs):
            return self.bin_path(*args, **kwargs)

        def run_command(self, *args, **kwargs):
            return self.run_command(*args, **kwargs)

    # Construct a module

# Generated at 2022-06-13 02:06:37.222795
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    import mock
    import os
    import sys

    # use a fake module object, as get_bin_path relies on an ansible module object
    # to define paths to search for the facter and cfacter commands
    class FakeModule:

        # return path of the facter and cfacter commands
        def get_bin_path(self, command, opt_dirs=None):
            if command == 'facter' and sys.platform.startswith('linux'):
                return '/usr/bin/facter'
            if command == 'facter' and sys.platform.startswith('darwin'):
                return '/usr/local/bin/facter'
            if command == 'cfacter' and sys.platform.startswith('linux'):
                return '/opt/puppetlabs/bin/cfacter'

# Generated at 2022-06-13 02:06:46.542103
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    """
    Return an empty dict from collect of FacterFactCollector
    """
    import ansible.module_utils.facts.collector

    ansible.module_utils.facts.collector.FacterFactCollector.find_facter = lambda self, module: None
    fact_collector = ansible.module_utils.facts.collector.FacterFactCollector()
    ansible.module_utils.facts.collector.FacterFactCollector.find_facter = lambda self, module: '/usr/bin/facter'
    fact_collector = ansible.module_utils.facts.collector.FacterFactCollector()
    fact_collector.collect()

# Generated at 2022-06-13 02:06:49.114250
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    from ansible.module_utils.facts.collector import MockModule

    facter_output = '{"test_output": "output"}\n'

    class MockFacterCollector(FacterFactCollector):
        def get_facter_output(self, module):
            return facter_output

    mock_module = MockModule({})
    facts = MockFacterCollector(module=mock_module).collect()

    assert facts == {'facter_test_output': 'output'}



# Generated at 2022-06-13 02:06:55.867100
# Unit test for method collect of class FacterFactCollector
def test_FacterFactCollector_collect():
    import mock
    import json

    module_mock = mock.MagicMock()
    module_mock.get_bin_path.side_effect = ValueError('No binary found')

    facter_fact_collector = FacterFactCollector()
    facter_fact_collector.get_facter_output = mock.MagicMock()
    facter_fact_collector.get_facter_output.return_value = None
    facter_fact_collector.collect(module_mock)

    module_mock = mock.MagicMock()
    module_mock.get_bin_path.return_value = '/usr/local/bin/facter'

# Generated at 2022-06-13 02:07:03.828279
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    from ansible.module_utils.facts.utils import FactsCollector

    # find_facter should return cfacter if both facter and cfacter are installed
    # we can simulate this by stubbing the get_bin_path() method
    def get_bin_path_stub(self, binary, opt_dirs=[]):
        if binary == 'cfacter':
            return '/bin/cfacter'
        else:
            return '/bin/facter'

    # stub out the get_bin_path() method of a FactsCollector
    # object
    FactsCollector.get_bin_path = get_bin_path_stub

    # now create a FacterFactsCollector object
    ff = FacterFactCollector()

    assert ff.find_facter(FactsCollector) is not None


# Generated at 2022-06-13 02:07:06.836247
# Unit test for method find_facter of class FacterFactCollector
def test_FacterFactCollector_find_facter():
    # Nothing to test: module.get_bin_path() is a thin wrapper around
    # module_utils.paths.HAS_BIN_UTILS, module.run_command() is a thin
    # wrapper around module_utils.basic.AnsibleModule.run_command()
    pass


# Generated at 2022-06-13 02:07:11.989320
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    # Create FacterFactCollector instance
    F = FacterFactCollector()

    # Test get_facter_output in condition where facter is not found
    class MockModule(object):
        def get_bin_path(self, name, opt_dirs=None):
            return None

    assert None == F.get_facter_output(MockModule())

    # Test get_facter_output in condition where facter is found but output is not valid json
    class MockModule2(object):
        def get_bin_path(self, name, opt_dirs=None):
            return 'facter'
        def run_command(self, cmd):
            return 0, "random output", ""

    assert None == F.get_facter_output(MockModule2())
 
    # Test get_facter_output in

# Generated at 2022-06-13 02:07:20.145704
# Unit test for method get_facter_output of class FacterFactCollector
def test_FacterFactCollector_get_facter_output():
    class AnsibleModuleMock(object):
        @classmethod
        def get_bin_path(cls, path, opt_dirs=None):
            return "/opt/puppetlabs/bin"

        @classmethod
        def run_command(cls, cmd):
            return 0, '{"foo": "bar", "baz": "qux"}', ''

        @classmethod
        def exit_json(cls, facter_dict):
            pass

        @classmethod
        def fail_json(cls, msg):
            pass

    facter_fact_collector = FacterFactCollector()
    assert facter_fact_collector.get_facter_output(AnsibleModuleMock) is not None
    facter_fact_collector = FacterFactCollector()

