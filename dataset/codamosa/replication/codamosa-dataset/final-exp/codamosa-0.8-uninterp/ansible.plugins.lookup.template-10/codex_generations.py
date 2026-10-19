

# Generated at 2022-06-22 12:01:12.185922
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ['test.j2', 'test2.j2']
    variables = {}
    env = {'environment_class': AnsibleEnvironment}
    lookup.set_templar(env)
    lookup.run(terms, variables)

# Generated at 2022-06-22 12:01:18.641495
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test that when the file cannot be found, LookupError is raised
    import ansible.plugins.lookup.template as template
    lookup = template.LookupModule()
    assert(isinstance(lookup.find_file_in_search_path(dict(some_var='some_val')), type(None)))
    assert(isinstance(lookup.find_file_in_search_path(dict(some_var='some_val'), 'some_dir'), type(None)))

    # test that the template is correctly rendered
    import os
    import tempfile
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        temp.write(b'{{some_var}}')
        temp.close()

# Generated at 2022-06-22 12:01:30.343687
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    
    # Create variable for testing
    lookupmodule = LookupModule()
    variables = {'ansible_search_path': ['~/']}
    terms = ['./some_template.j2']
    variables = {'ansible_search_path': ['~/']}
    kwargs = {'convert_data': True, 'template_vars': {}, 'jinja2_native': False, 
              'variable_start_string': '{{', 'variable_end_string': '}}',
              'comment_start_string': None, 'comment_end_string': None}

    # Execute the method run
    try:
        lookupmodule.run(terms, variables, **kwargs)
    except Exception as e:
        print (e)

# Generated at 2022-06-22 12:01:41.180891
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible import constants as C

    from ansible.template import Templar

    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    # Variable manager
    variable_manager = VariableManager()
    variable_manager.extra_vars = {'hostvars': {'localhost': {'ansible_all_ipv4_addresses': ['192.0.2.0']}}}
    variable_manager.set_inventory(InventoryManager(loader=DataLoader(), sources='localhost,'))

    # Templar
    templar = Templar(loader=DataLoader(), variables=variable_manager)

    # LookupModule
    lookup_module = LookupModule()
    lookup_module._loader = DataLoader()
    lookup_module._templ

# Generated at 2022-06-22 12:01:45.737949
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest

    @pytest.fixture
    def LookupModule_run_fixture(mocker):
        lookup_module = LookupModule(loader=None, templar=None, shared_loader_obj=None)
        lookup_module._get_plugin_options_from_vars = mocker.MagicMock()
        lookup_module.set_options = mocker.MagicMock()
        lookup_module.get_option = mocker.MagicMock()
        lookup_module.find_file_in_search_path = mocker.MagicMock()
        lookup_module._loader = mocker.MagicMock()
        lookup_module._templar = mocker.MagicMock()
        return lookup_module



# Generated at 2022-06-22 12:01:51.471996
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    lookup.set_loader({'_get_file_contents': lambda self, file: (to_bytes('{{ "1" + "2" }}', errors='surrogate_escape'), False)})
    lookup.set_environment(AnsibleEnvironment())
    assert lookup.run(terms=['file'], variables={}) == ['12']

# Generated at 2022-06-22 12:02:03.485581
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    assert lookup_module.run([], {}) == [], "Empty list of files to template"

    # We are not mocking files, but we can mock the result of _loader.get_basedir()
    def get_basedir(self):
        return os.getcwd()

    lookup_module._loader.get_basedir = types.MethodType(get_basedir, lookup_module._loader)

    # Create a file in the current directory and template it
    f = tempfile.NamedTemporaryFile(delete=False)
    f.write(b"Hello World")
    f.close()


# Generated at 2022-06-22 12:02:14.539160
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    terms = './some_template.j2'
    variables = {
        'ansible_search_path': ['.'],
        'accelerate_port': '5001',
        'template_host': 'localhost',
    }
    kwargs = {
        'variable_start_string': '{{',
        'variable_end_string': '}}',
        'comment_start_string': '{#',
        'comment_end_string': '#}',
        'jinja2_native': False,
    }

    mock_loader_mgr = MockLoaderManager()
    mock_loader = mock_loader_mgr.loader

    mock_loader.get_real_file = MagicMock(return_value='./some_template.j2')


# Generated at 2022-06-22 12:02:26.366896
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Setup test data
    plugin = LookupModule()

    class Options(object):
        def __init__(self, convert_data=True, variable_start_string='{{', variable_end_string='}}',
                     comment_start_string=None, comment_end_string=None, jinja2_native=False):
            self.convert_data = convert_data
            self.variable_start_string = variable_start_string
            self.variable_end_string = variable_end_string
            self.comment_start_string = comment_start_string
            self.comment_end_string = comment_end_string
            self.jinja2_native = jinja2_native

    class Variables(object):
        def __init__(self, ansible_search_path=None, foo=None):
            self

# Generated at 2022-06-22 12:02:38.014621
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.parsing.vault import VaultLib
    from ansible.utils.vault import VaultAware
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.lookup import LookupBase
    from ansible.plugins.lookup import templar_common_args
    from ansible.template import Templar

    # Create a template, find the file and load it
    my_template = """
    Test template {{ palabra }} processing.
    """
    lookupfile = "Testing"
    b_template_data = "Test template {{ palabra }} processing."

    # Create a variable
    my_vars = {"palabra": "template"}

    # Use custom VaultLib
    vault_secrets = VaultLib(password_file='test/test_vault_lib.txt')

# Generated at 2022-06-22 12:02:54.823910
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test data
    terms = ['templates/foo2.j2']
    variables = dict()

    # TODO: Can this mock be made not to raise AssertionError ?
    mock_options = dict()
    mock_options['comment_start_string'] = '#'
    mock_options['comment_end_string'] = '#'
    mock_options['variable_start_string'] = '{{'
    mock_options['variable_end_string'] = '}}'
    mock_options['convert_data'] = True
    mock_options['jinja2_native'] = True
    mock_options['template_vars'] = dict()
    expected = []

    # Mocking
    from ansible.template import generate_ansible_template_vars

# Generated at 2022-06-22 12:03:06.746524
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Correct behaviour
    correct_input_correct_output_dict = {
                                           'terms_input' :
                                               [
                                                   'test_files/test_jinja2_vars.j2'
                                               ],
                                           'variables_input' :
                                               {
                                                   'template_vars_key' : 'template_vars_value'
                                               },
                                           'stdout_output' :
                                               [
                                                   '\n\n'
                                                   'template_vars_value\n'
                                                   # new lines at the end of the template
                                               ],
                                           'stderr_output' :
                                               ''
                                        }

    test_inputs = [correct_input_correct_output_dict]

   

# Generated at 2022-06-22 12:03:17.609492
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    # empty term list
    assert [] == lookup.run([], {})
    # empty term list in variables with key 'ansible.playbook.templates'
    assert [] == lookup.run([], {'ansible.playbook.templates': []})
    # non-empty term list in variables with key 'ansible.playbook.templates'
    assert [] == lookup.run([], {'ansible.playbook.templates': ['a/b/c']})
    # empty term list in variables with key 'template_path'
    assert [] == lookup.run([], {'template_path': []})
    # non-empty term list in variables with key 'template_path'
    assert [] == lookup.run([], {'template_path': ['a/b/c']})

# Generated at 2022-06-22 12:03:28.229476
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    class TestModule:
        def __init__(self):
            self.params = {}
            self.args = None
            self.result = None

    class TestModule2:
        def __init__(self):
            self.params = {}
            self.args = None
            self.result = None

        class TestPlayBook:
            def __init__(self):
                self.vars = {}
                self.basedir = None

        class TestSet:
            def __init__(self):
                self.vars = {}
                self.basedir = None

            class TestTask:
                def __init__(self):
                    self.basedir = None

    class TestModule3:
        def __init__(self):
            self.params = {}
            self.args = None
            self.result = None


# Generated at 2022-06-22 12:03:37.190054
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''This unit test checks if the method run works correctly'''

    # Creating a LookupModule mechanism
    LookupModule_mechanism = LookupModule()

    # Simulating the input key-value
    terms_input = [ "template_test.j2" ]
    variables_input = { "ansible_search_path" : [ "/root/testing" ] }

    # Running the method run
    result = LookupModule_mechanism.run(terms_input,variables_input)

    # Asserting the result
    assert result == [ "\nTemplate Test\n" ]



# Generated at 2022-06-22 12:03:48.521113
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # pylint: disable=protected-access
    lu = LookupModule()
    lookup_template_vars = {"my_host_ip": "10.0.0.1"}

    lu._lookup_plugin = lu
    lu._loader = DictDataLoader({
        "./playbook1.yml": b"This is simple_playbook_1",
        "./playbook2.yml": b"This is simple_playbook_2",
        "./roles/role1/templates/template1.j2": b"Hello {{ my_host_ip }}.",
    })

    terms = ["template1.j2"]

# Generated at 2022-06-22 12:04:00.374410
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    print('TEST: test_LookupModule_run')

    import json, sys, os
    import jinja2

    if sys.version_info < (3, 4):
        import imp
        import io
        imp.reload(io)

    # Create a dummy environment and variables
    class FakeVarsModule():
        def __init__(self, dict):
            self.__dict__.update(dict)

    class FakePlayContext():
        def __init__(self, dict):
            self.__dict__.update(dict)
        def set_variable(self, dict):
            self.__dict__.update(dict)

    class FakeLoader():
        def __init__(self, dict):
            self._module_name = dict.get('module_name')

# Generated at 2022-06-22 12:04:11.054946
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module_test = LookupModule()

    # test for invalid search terms
    terms = '/some/random/file'
    variables = {'ansible_search_path' : ['/some/place']}
    kwargs = {}
    try:
        ret = module_test.run(terms, variables, **kwargs)
    except AnsibleError:
        pass
    else:
        assert ret is not None

    # test for valid search terms
    terms = 'index.html'
    variables = {'ansible_search_path' : [os.path.dirname(__file__)]}
    kwargs = {}
    ret = module_test.run(terms, variables, **kwargs)
    assert ret is not None

    # test for valid search terms
    terms = '../index.html'

# Generated at 2022-06-22 12:04:19.912048
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    # test template file `terraform_setup.sh.j2`
    template_path = os.path.join(os.path.dirname(__file__), '../templates/terraform_setup.sh.j2')
    # test values for optional arguments
    convert_data = False
    lookup_template_vars = {
        'my_variable': 'my_value'
    }
    jinja2_native = False
    variable_start_string = '{{'
    variable_end_string = '}}'
    comment_start_string = '###'
    comment_end_string = '###'
    # test values for mandatory arguments
    terms = [template_path]
    variables = {}
    # call `run` method with test values as arguments

# Generated at 2022-06-22 12:04:29.890620
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.facts.system.distribution import Distribution
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager()
    templar = Templar(loader=loader, variables=variable_manager)

    d = Distribution()
    l = LookupModule(loader=loader, variables=variable_manager, templar=templar)

    ret = l.run(['changelog.j2'], None)

# Generated at 2022-06-22 12:04:51.010814
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit test of method run in class LookupModule
    """
    # use a templar from a custom module to get at its methods and attributes
    from ansible.template import Templar
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader

    class MyLookupModule(LookupModule):
        def __init__(self):
            self.templar = Templar(loader=DataLoader(), variables={})
            self.host = Host(name="testhost")
            self.loader = DataLoader()
            self._templar = Templar(loader=self.loader, variables={})
        def run(self, terms, variables=None, **kwargs):
            return super(MyLookupModule, self).run(terms, variables, **kwargs)

# Generated at 2022-06-22 12:05:00.558984
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    from ansible.errors import AnsibleLookupError
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    class Options(object):
        def __init__(self, connection, remote_user, private_key_file,
                     module_path, forks, become, become_method, become_user,
                     check, diff):
            self.connection = connection
            self.remote_user = remote_user
            self.private_key_file = private_key_file
            self.module_path = module_path
            self.forks = forks

# Generated at 2022-06-22 12:05:07.735877
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import mock
    import tempfile
    import textwrap
    import yaml
    # Setup test input
    test_file_name = 'test.txt'
    test_file_content = 'test content\ntest\ncontent'
    test_file_path = os.path.join(tempfile.gettempdir(), test_file_name)
    # Make sure to create the file in a way that works with Python 2 and 3
    with open(test_file_path, 'w') as f:
        f.write(test_file_content)

    test_file_name_invalid = 'test_invalid.txt'
    test_file_path_invalid = os.path.join(tempfile.gettempdir(), test_file_name_invalid)

    # Setup helper fixtures
    fixture_module_utils_basic = text

# Generated at 2022-06-22 12:05:21.126834
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    """
    Tests for method run of class LookupModule.

    The following cases are tested:
    1. ansible_search_path is not defined.
    2. ansible_search_path is defined.
    """

    from ansible.module_utils.six import StringIO

    from ansible.plugins.loader import lookup_loader

    from ansible.template import Templar

    from ansible.vars import VariableManager

    class MockLoader(object):

        def __init__(self, data=None):
            self._data = data

        def _get_file_contents(self, path):
            return self._data, True

    class MockVarManager(VariableManager):

        def __init__(self, extra_vars=None, inventory=None):
            self.extra_vars = extra_vars

# Generated at 2022-06-22 12:05:33.333620
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit test for method run of class LookupModule
    """

    import os
    import sys
    import pytest
    import lookups.template as template_lookup
    import collections

    if sys.platform.startswith("win"):
        from ansible.module_utils.winutils.ansiballz import ANSIBALLZ_TEMPLATE
        from ansible.module_utils.winutils.ansiballz import ANSIBALLZ_MOD_ARGS

    FileInfo = collections.namedtuple('FileInfo', ['name', 'type'])
    Answer = collections.namedtuple('Answer', ['data', 'type'])

    test_files_dir = os.path.join(os.path.dirname(__file__), 'files')
    template_lookup_obj = template_lookup.Look

# Generated at 2022-06-22 12:05:34.277102
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert False, "TODO"

# Generated at 2022-06-22 12:05:42.337851
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test with simple string
    result = LookupModule({}, {}, {}, {}, {}).run([to_bytes('{{ lookup(\'template\', \'./some_template.j2\') }}',
                                                            errors='surrogate_or_strict'), ],
                                                  {}, **{'variable_start_string': to_bytes('[%', errors='strict'),
                                                         'variable_end_string': to_bytes('%]', errors='strict'),
                                                         'comment_start_string': to_bytes('[#', errors='strict'),
                                                         'comment_end_string': to_bytes('#]', errors='strict'),
                                                         'template_vars': {}})
    assert result == [[to_bytes('data', errors='surrogate_or_strict'), ], ]



# Generated at 2022-06-22 12:05:52.632522
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class AnsibleModule(object):
        def __init__(self):
            self.params = {
                'variable_start_string': '{{',
                'variable_end_string': '}}',
            }
    class AnsibleOptions(object):
        def __init__(self, params):
            self.connection = 'local'
            self.module_path = None
            self.forks = 1
            self.become = False
            self.become_method = 'sudo'
            self.become_user = None
            self.check = False
            self.diff = False
            self.listhosts = None
            self.listtasks = None
            self.listtags = None
            self.syntax = None
            self.verbosity = 3
            self._j2_env = None
            self._j2

# Generated at 2022-06-22 12:06:01.694317
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import copy
    import pytest

    try:
        from ansible.template import __native_types_loaded__ as result_nt
        if result_nt:
            pytest.skip('Skipping since this test is for non-native-types.yml', allow_module_level=True)
    except ImportError:
        pass

    from ansible.errors import AnsibleError
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.plugins.lookup import LookupBase

# Generated at 2022-06-22 12:06:03.066380
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule().run(['/test.j2'], {}) == ['test.j2 results']

# Generated at 2022-06-22 12:06:33.611682
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # simple test
    terms = ['test_templates_1.j2', 'test_templates_2.j2']

    lookup.run(terms,
               variables={'test_var': 'value'},
               convert_data=False,
               jinja2_native=False,
               variable_start_string='--',
               variable_end_string='--',
               comment_start_string='//',
               comment_end_string='//',
               template_vars={'additional_var': 'to_template'})

    # we can't test the result of the run because it's been mocked out with _loader etc

# Generated at 2022-06-22 12:06:44.970424
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Testing run with AnsibleEnvironment

    #creating dummy env
    class AnsibleEnvironmentMock:
        def __init__(self):
            self._data = {}
            self._engine = None

    class DummyTemplar:
        def __init__(self):
            self._data = {}

        def copy_with_new_env(self, environment_class):
            return self

        def template(self, data, preserve_trailing_newlines=True, convert_data=False, escape_backslashes=False):
            return data

        def set_temporary_context(self, available_variables=None, searchpath=None):
            pass

    # creating dummy loader
    class DummyLoader:
        def __init__(self):
            self._data = {}
            self._file_cache = {}
            self._

# Generated at 2022-06-22 12:06:46.622661
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-22 12:06:58.469109
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    # test for method raise "the template file %s could not be found for the lookup" % term
    lookup_module = LookupModule()
    lookup_module._loader = DictDataLoader({'lookup_fixtures': {}})
    lookup_module._templar = Templar({}, loader=lookup_module._loader)
    lookup_module.set_options()
    with pytest.raises(AnsibleError) as e:
        lookup_module.run(['test_foo_file'], {})
    assert e.value.message == "the template file test_foo_file could not be found for the lookup"
    # test for method run with different args
    lookup_module = LookupModule()

# Generated at 2022-06-22 12:07:04.227477
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    term = 'test/test_lookup.py'
    variables = {}
    l = LookupModule()
    result = l.run(terms=term, variables=variables, variable_start_string='{', variable_end_string='}')
    assert len(result) == 1
    assert result[0] == '#!/usr/bin/python'

# Generated at 2022-06-22 12:07:11.278515
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # create an object of class LookupModule
    lookup_module_ob = LookupModule()
    # create a dictionary to pass as variable parameters
    variables = {}
    # create a list of valid file paths for testing
    terms = ['test.j2']
    # call the method run(self, terms, variables, **kwargs) of class LookupModule
    test_result = lookup_module_ob.run(terms, variables)
    # assert to validate the returned value
    assert test_result == ["Hello, {{ name }}"]

# Generated at 2022-06-22 12:07:11.813367
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    a = LookupModule()
    assert a.run()

# Generated at 2022-06-22 12:07:21.157116
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Testing for LookupModule.run
    # Tests for ran case
    terms = ['../test/data/templates/hosts.j2']

# Generated at 2022-06-22 12:07:29.530089
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # How to use:
    # $ pip install coverage
    # $ coverage run coverage_test_lookup_plugins.py
    # $ coverage report -m

    # Setup variables
    lookup = LookupModule()
    result = []
    output = []
    terms = []
    variables = {}

    # Run lookup.run(terms, variables)
    terms = ['vars.j2']

# Generated at 2022-06-22 12:07:41.163328
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.parsing.dataloader
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play

    variable_manager = VariableManager()
    loader = ansible.parsing.dataloader.DataLoader()
    inventory = InventoryManager(loader=loader, sources=[])
    play_source =  dict(
        name = "Ansible Play",
        hosts = 'all',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='debug', args=dict(msg='{{lookup("template","testfile.j2")}}')))
         ]
    )


# Generated at 2022-06-22 12:08:23.467442
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    # TODO

if __name__ == '__main__':
    test_LookupModule_run()

# Generated at 2022-06-22 12:08:28.085917
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    terms = ['test_me.j2']

    lookup_plugin = LookupModule()
    result = lookup_plugin.run(terms, {}, variable_start_string='{{', variable_end_string='}}')

    assert result == [b'\n    Hello World\n']

# Generated at 2022-06-22 12:08:30.576183
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule(loader=None, templar=None, shared_loader_obj=None).run(terms=[None], variables={}) == []

# Generated at 2022-06-22 12:08:42.106621
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.compat.tests import unittest
    import json

    class TestLookupModule(unittest.TestCase):

        def setUp(self):
            self.lookup_module = LookupModule()

        def tearDown(self):
            pass

        def test_LookupModule_run(self):
            templar_mock = MockTemplar()
            loader_mock = MockDataLoader()
            display_mock = MockDisplay()
            env_mock = MockEnvironment()
            test_vars = {
                'template_path': '/home/user/templates/test.j2',
                'template_mtime': 1570551302,
                'ansible_search_path': ['/home/user/templates'],
                'test_var': 'test_value'
            }

# Generated at 2022-06-22 12:08:53.886456
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # ctx_object is an instance of AnsibleContext
    # terms is of type string or string list
    # self.run(terms, variables, **kwargs) is used to run the play
    # context is an instance of AnsibleContext
    # loader is an instance of DataLoader
    ctx_object = AnsibleContext()
    terms = './some_template.j2'
    ctx_object.set_options(var_options=variables, direct=kwargs)
    ctx_object.find_file_in_search_path(variables, 'templates', term)
    b_template_data, show_data = self._loader._get_file_contents(lookupfile)
    template_data = to_text(b_template_data, errors='surrogate_or_strict')
    vars = deep

# Generated at 2022-06-22 12:09:02.459833
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_class = LookupModule()
    terms = ['./some_template.j2']
    variables = {'template_foo': 'HELLO WORLD'}

    def test_loader_get_file_contents(path):
        return "{{ template_foo }}", False
    test_class._loader._get_file_contents = test_loader_get_file_contents

    def test_loader_path_exists(path):
        return path == "./some_template.j2"
    test_class._loader.path_exists = test_loader_path_exists

    def test_loader_is_file(path):
        return path == "./some_template.j2"
    test_class._loader.is_file = test_loader_is_file


# Generated at 2022-06-22 12:09:05.524933
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    # Run with no options
    result = lookup.run([ 'test.j2' ], {})
    assert result == []



# Generated at 2022-06-22 12:09:15.982367
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a Mocking ModuleLoader object
    class ModuleLoader:
        def get_basedir(self, *args, **kwargs):
            return None

        def _get_file_contents(self, *args, **kwargs):
            return "{{ lookup('env', 'HOME') }}", False
    mock_loader = ModuleLoader()

    # Create a Mocking Environment object
    class Environment:
        def get_basedir(self, *args, **kwargs):
            return None
    mock_environment = Environment()

    # Create a Mocking Templar object
    class Templar:
        def __init__(self, *args, **kwargs):
            pass

        def set_available_variables(self, *args, **kwargs):
            pass

        def set_loader(self, *args, **kwargs):
            pass

       

# Generated at 2022-06-22 12:09:27.444822
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Create a mock class for 'VariableManager'
    class MockVariableManager:
        def __init__(self):
            self.vars = {'ansible_search_path': []}

        def __call__(self, loader, path, entities):
            self.vars['ansible_search_path'] = ['/path/to']
            return self.vars

    # Create a mock class for '_Loader'
    class MockLoader:
        def _get_file_contents(self, path):
            return ('string', True)

    # Create a mock class for 'Environment'
    class MockEnvironment:
        def __init__(self, **kwargs):
            return

    # Create a mock class for 'Templar'

# Generated at 2022-06-22 12:09:34.845098
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    with open("/tmp/data.txt", "w") as f:
        f.write("data1")
    with open("/tmp/data2.txt", "w") as f:
        f.write("data2")

    lookup_mod = LookupModule()
    result = lookup_mod.run(["./data.txt", "./data2.txt"], dict())
    assert len(result) == 2
    assert result[0] == to_text("data1")
    assert result[1] == to_text("data2")

# Generated at 2022-06-22 12:11:06.053893
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    import pytest
    assert sys.version_info[:2] == (2, 7) or sys.version_info[:1] == (3, 6)

    class TestLookupModule(LookupModule):
        def __init__(self, loader=None, templar=None, **kwargs):
            self.loader = loader
            self.templar = templar

        def find_file_in_search_path(self, variables, dirname, filename):
            template_dir = ''
            searchpath = variables.get('ansible_search_path', [])
            for path in searchpath:
                new_path = os.path.join(path, dirname, filename)