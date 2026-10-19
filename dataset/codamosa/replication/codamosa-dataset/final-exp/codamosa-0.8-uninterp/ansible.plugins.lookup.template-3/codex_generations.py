

# Generated at 2022-06-22 12:01:16.533684
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Given
    # A lookup module
    lookup_module = LookupModule()

    # Then:
    # The returned result file should be the same as the expected result file
    ret = lookup_module.run(['./tests/files/file_for_lookup_module_run.j2'], {}, _terms=['./tests/files/file_for_lookup_module_run.j2'])
    result_file = ret[0]
    expected_result_file = to_bytes('./tests/files/result_file_for_lookup_module_run.j2')
    assert result_file == expected_result_file


if __name__ == '__main__':
    # Unit test for method run of class LookupModule
    test_LookupModule_run()

# Generated at 2022-06-22 12:01:29.226563
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    print("\n")
    import sys
    import os
    import inspect
    import re

    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    sys.path.insert(0,parentdir)

    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    lookup_module = LookupModule()
    lookup_module._templar = Fake_Templar()


# Generated at 2022-06-22 12:01:40.329099
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import mock

    # This function is called to initialize the plugin
    def setup_loader(loader):
        return loader

    # Define mocks for the lookup module
    terms = ['lookup_test_data.yml']
    variables = {}

    def find_file_in_search_path(variables, dirname, term):
        # Here we just simulate the yml file found in the search path
        return './lookup_test_data.yml'

    _loader = mock.MagicMock()

    # Here we mock that the file content is a string
    _loader.get_file_contents.side_effect = lambda path, show_data: (to_bytes('test'), show_data)

    # Environment class is used to set jinja2 search path
    env_class = mock.MagicMock()
    # Initial

# Generated at 2022-06-22 12:01:41.684469
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    assert False

# Generated at 2022-06-22 12:01:53.409449
# Unit test for method run of class LookupModule

# Generated at 2022-06-22 12:01:58.050052
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Init
    lookup_module = LookupModule()

    # Run
    result = lookup_module.run(terms=["foo"], variables=dict(foo="Hello, World!"), convert_data=False)

    # Assert
    assert len(result) == 1
    assert result[0] == "Hello, World!"

# Generated at 2022-06-22 12:02:05.633463
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Unit test method run of class LookupModule"""

    import warnings

    warnings.filterwarnings("ignore", module='ansible.plugins.lookup')

    from ansible.plugins.loader import lookup_loader

    lookup_loader.get("template").run(terms=['tests/ansible_template_test.j2'], variables={'name': 'Jack'})

if __name__ == '__main__':
    test_LookupModule_run()

# Generated at 2022-06-22 12:02:10.690587
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    terms = ['../../tests/templates/test.j2']
    variables = {'VERSION': '1.2.3', 'env': 'test'}
    result = module.run(terms, variables)
    assert result[0] == "This is a test 1.2.3\n"

# Generated at 2022-06-22 12:02:11.982533
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test class is not callable
    with pytest.raises(TypeError):
        LookupModule()


# Generated at 2022-06-22 12:02:12.530330
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-22 12:02:25.480288
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    terms = ['template_1', 'template_2']
    environment = {'scenario': 'test', 'number': 10}
    variable_start_string = '['
    variable_end_string = ']'
    comment_start_string = '[%'
    comment_end_string = '%]'
    convert_data = True
    lookup_template_vars = {'lookup_var_1': 'lookup_val_1',
                            'lookup_var_2': 'lookup_val_2'}
    jinja2_native = False

    class DummyModule(object):
        def __init__(self):
            self.run_command_environ_update = deepcopy(environment)

    class DummyLoader(object):
        pass


# Generated at 2022-06-22 12:02:33.281738
# Unit test for method run of class LookupModule

# Generated at 2022-06-22 12:02:44.902819
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    _Loader = 'ansible.parsing.dataloader.DataLoader'
    _Templar = 'ansible.parsing.yaml.objects.AnsibleVaultEncryptedUnicode'
    _Plugin = 'ansible.plugins.lookup.template.LookupModule'
    
    # Test the error condition
    # when a template file does not exist
    # and a search path is not provided
    # for the lookup, then an error is raised
    # indicating that the template file
    # could not be found
    _terms = '{{lookup(\'pipe\', "echo test")}}'
    loader = mock.Mock(spec_set=_Loader)
    lm = LookupModule()
    templar = mock.Mock(spec_set=_Templar)
    lm.set_

# Generated at 2022-06-22 12:02:54.280927
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    global templar
    t = LookupModule()
    terms = ['foo.txt']
    t._templar = templar
    variables = {}

    lookupfile = './plugins/lookup/foo.txt'
    with open(lookupfile, 'r') as f:
        text = f.read()
        text = text.encode()
    b_template_data, show_data = t._loader._get_file_contents(lookupfile)

    print(b_template_data)
    if b_template_data == text:
        print("Passed")
    else:
        print("Failed")

# Generated at 2022-06-22 12:02:57.803754
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    terms = ['./some_template.j2']
    variables = {}
    assert(module.run(terms=terms, variables=variables) == [])

# Generated at 2022-06-22 12:03:08.647223
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import pytest

    @pytest.fixture
    def lookup_module():
        """
        create a LookupModule
        """
        return LookupModule()

    # Testing template_vars
    def test_template_vars(lookup_module, mocker):
        """
        testing if the template vars are passed to jinja2
        """

        # mocking in facts, so we can test if lookup_template_vars are passed to jinja2
        facts = {'test_fact': 'test_fact'}
        fake_env = mocker.patch('ansible.template.AnsibleEnvironment')
        fake_env().get_template().render.return_value = ""
        fake_env().get_template().render.assert_called_with(test_fact='test_fact')


# Generated at 2022-06-22 12:03:18.146607
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import lookup_loader, lookup_error_classes

    def _find_file_in_search_path(variables, dirname, filename):
        path = os.path.join(dirname, filename)
        return path

    def _get_file_loader(path):
        return 'test data'

    class TestLookupModule(LookupModule):
        def __init__(self, *args, **kwargs):
            super(TestLookupModule, self).__init__(*args, **kwargs)
            self.set_loader(_get_file_loader)
            self.set_find_file_in_search_path(_find_file_in_search_path)


# Generated at 2022-06-22 12:03:25.601631
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # source: https://github.com/ansible/ansible/blob/v2.1.3.0-1/test/unit/plugins/lookup/test_template.py
    def assertEqual(a, b):
        if a != b:
            raise Exception('%r != %r'%(a, b))

    import sys
    import os
    import json
    import subprocess

    lookup_plugin = LookupModul

# Generated at 2022-06-22 12:03:36.531319
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    class AnsibleModule(object):
        def __init__(self, **kwargs):
            self.params = kwargs
            self.params['template_vars'] = {'key1': 'value1', 'key2': 'value2', 'key3': kwargs['lookup_template_vars']}

    class AnsibleModuleMock(object):
        def __init__(self, **kwargs):
            self.params = kwargs

    class AnsibleModuleMockWithParams(object):
        def __init__(self, **kwargs):
            self.params = kwargs
            self.params['template_vars'] = kwargs['lookup_template_vars']

    class AnsibleModuleMockWithVars(object):
        def __init__(self, **kwargs):
            self

# Generated at 2022-06-22 12:03:48.097264
# Unit test for method run of class LookupModule
def test_LookupModule_run():
  from ansible.compat.tests import unittest
  from ansible.compat.tests.mock import patch
  from ansible.compat.tests.mock import MagicMock
  import ansible.plugins.lookup.template
  import ansible.template
  import json


# Generated at 2022-06-22 12:04:08.089187
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Create LookupModule_run object
    lookup_module = LookupModule()

    # Create an array of variables from the test and control files
    lookup_module.set_options(var_options=dict())

    # Test yaml file path
    test_yaml_file_path = "./tests/lookup/template/test_template_yaml.yaml"

    # Create lookup dictionary
    lookup_dict = {
        "x": "template_lookup_var",
        "y": "{{ x }}",
        "z": "{{ y }}",
        "w": "{{ z }}"
    }

    # Create lookup dictionary yaml

# Generated at 2022-06-22 12:04:20.359258
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible.module_utils.six import PY3
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.template import Templar
    template_data = """
        [{% for i in range(5) %}
        {{ i }}{% endfor %}]
    """

    # setup
    variable_start_string = '{{'
    variable_end_string = '}}'
    lookup_terms = [0]
    lookup_file = 0
    lookup_vars = {}
    kwargs = {'convert_data': True, 'variable_start_string': variable_start_string,
               'variable_end_string': variable_end_string}
    mock_loader = pytest.Mock()
    mock_loader._

# Generated at 2022-06-22 12:04:31.254282
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # NOTE: this is the one case where we don't use the
    # class under test directly, because the test module
    # has to modify some global state in order to make the
    # test go.  This is why the test class is defined outside
    # this function.

    # set up some dummy values
    terms = [ './file1.j2', './file2.j2' ]
    variables = { 'var1': 'foo', 'var2': 'bar' }
    options = { 'convert_data': 'False', 'template_vars': '', 'jinja2_native': 'False' }

    # create a subclass of LookupModule that has the dummy values
    class TestLookupModule(LookupModule):
        def __init__(self):
            super(TestLookupModule, self).__init__()

       

# Generated at 2022-06-22 12:04:42.992383
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play_context import PlayContext
    from ansible.module_utils.six import PY3

    variable_manager = VariableManager()
    variable_manager.set_inventory(Inventory())
    play_context = PlayContext()
    variable_manager.extra_vars = {
        'foo': 'bar',
        'jinja2_native': False,
        'convert_data': False,
        'template_vars': {
            'bar': 'baz',
        },
        'variable_start_string': '<<<',
        'variable_end_string': '>>>',
        'comment_start_string': '{#',
        'comment_end_string': '#}',
    }

    lookup

# Generated at 2022-06-22 12:04:51.849706
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    test_file = 'test.j2'
    test_file_path = os.path.join(os.path.dirname(__file__), test_file)
    fd = open(test_file_path, 'w')
    fd.writelines(['{{ ansible_managed }}', '\n', 'foo'])
    fd.close()

    lookup = LookupModule()

    lookup.set_loader(None)
    lookup.set_inventory(None)
    lookup.set_playbook(None)


# Generated at 2022-06-22 12:05:00.893603
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    mod = LookupModule()
    mod._loader = DictDataLoader({'foo.j2' : '{{ testa }}'})

    assert mod.run([ 'foo.j2' ], {'testa': 'foo'}, convert_data=False) == [ 'foo' ]
    assert mod.run([ 'foo.j2' ], {'testa': 'foo'}, convert_data=True) == [ 'foo' ]
    assert mod.run([ 'foo.j2' ], {'testa': 'foo', 'template_vars': {'foo' : 'bar'}}, convert_data=False) == [ 'foo' ]

# Generated at 2022-06-22 12:05:10.102953
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six.moves import cStringIO as StringIO
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six.moves import builtins
    # define env variables
    os.environ['ANSIBLE_JINJA2_NATIVE'] = 'False'
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    lookup_obj = LookupModule()
    # define parameters for test
    terms = './some_template.j2'
    variables = {'foo': 'bar'}
    terms_type = ['file']
    # run test
    ret = lookup_obj.run(terms, variables, **{'_terms': terms_type})
    sys.stdout = old_stdout

# Generated at 2022-06-22 12:05:23.096064
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    #
    # 1. simple test
    #
    display = Display()
    display.display = lambda msg: None
    lookup = LookupModule(display=display)
    lookup.set_options({'template_vars': {'key1': 'value1', 'key2': 'value2'}})
    template_content = """\
---
data:
- key1: {{ key1 }}
- key2: {{ key2 }}
"""
    #
    # Mock _templar.template() to fake the call to jinja2
    #
    def template(self, template_data, convert_data=False, preserve_trailing_newlines=True, escape_backslashes=False):
        # jinja2_native is true globally
        assert not convert_data
        assert preserve_trailing_newlines

# Generated at 2022-06-22 12:05:34.866001
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    import yaml

    class TestLoader:
        def __init__(self, loader):
            self._loader = loader
        def _get_file_contents(self, path):
            return self._loader(path), False


    pl = None

    for path in sys.path:
        try:
            from ansible.plugins.loader import vars_loader
            pl = vars_loader
        except ImportError:
            continue
        else:
            break
    else:
        raise Exception("vars_loader not found in sys.path")


    def _loader(path):
        if path == './get_url/url_result.yml':
            return "key: some_template.j2"

# Generated at 2022-06-22 12:05:45.544063
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils import basic


# Generated at 2022-06-22 12:06:12.342392
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Arrange
    import sys
    import __builtin__
    if sys.version_info[0] > 2:
        import builtins as __builtin__

    import ansible.plugins.lookup.template
    from ansible.template import ANSIBLE_TEMPLATE_ENGINE
    from ansible.template.safe_environment import SafeEnvironment
    from ansible.template.template import AnsibleEnvironment
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.errors import AnsibleError
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    import ansible.constants as C
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    import os



# Generated at 2022-06-22 12:06:22.788084
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['foo.txt', 'bar.txt']
    variables = dict(
        ansible_search_path=['/tmp']
    )
    kwargs = dict(
        convert_data=True,
        template_vars=dict(),
        jinja2_native=True,
        variable_start_string='[%',
        variable_end_string='%]',
        comment_start_string='[#',
        comment_end_string='#]'
    )
    lookup_module = LookupModule()
    lookup_module.set_loader_utils(
        _loader=MockLoader(),
        _templar=MockTemplar()
    )
    results = lookup_module.run(terms=terms, variables=variables, **kwargs)

# Generated at 2022-06-22 12:06:34.746695
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible.plugins.lookup.template import LookupModule
    from ansible.module_utils._text import to_bytes
    from ansible.template import generate_ansible_template_vars
    from ansible.utils.display import Display

    display = Display()
    display.verbosity = 4

    # Prepare the invocation of the check
    lookup = LookupModule()


# Generated at 2022-06-22 12:06:45.930348
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup = LookupModule()
    lookup.set_loader({})  # dummy loader

    #
    # Test when there are no variables.
    #
    lookup.set_options({'_raw_params': 'foo.txt'})
    lookup.set_environment({'template_host': 'localhost',
                            'template_uid': 1000,
                            'template_path': '/this/is/a/path/to/foo.txt',
                            'template_fullpath': '/this/is/a/path/to/foo.txt',
                            'template_run_date': 'Fri Mar 20 20:46:26 2015',
                            'template_run_date_formatted': 'Fri Mar 20 20:46:26 2015'})
    lookup.run([], {})

    #
    # Test when there are variables and include_v

# Generated at 2022-06-22 12:06:53.013224
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # create instance of class LookupModule
    play_context = dict(lookup_file_escaping=True)
    templar = Templar(loader=None, variables=dict(),
                      fail_on_undefined=True,
                      disable_lookups=False)

    lookup_base = LookupBase()
    lookup_base_inheritance = LookupModule()
    # check that typing the class creates an instance
    assert isinstance(lookup_base_inheritance, LookupBase)
    assert isinstance(lookup_base_inheritance, LookupModule)

    # check that the run method doesn't contain any assert and return a value
    ret = lookup_base_inheritance.run(terms=[], variables={}, **{})
    assert ret is not None

    # check that the method run raise a error when terms is empty


# Generated at 2022-06-22 12:07:03.807939
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import pprint
    from ansible.template import AnsibleEnvironment
    from ansible.playbook.play_context import PlayContext
    import ansible.plugins.loader as plugin_loader

    kwargs = {
        '_terms': ['test_arg.j2'],
        'template_vars': {'test_var': 'value_for_the_test'},
        'convert_data': True,
        'variable_start_string': '[%',
        'variable_end_string': '%]',
        'comment_start_string': '[#',
        'comment_end_string': '#]',
    }

    plugin_loader.add_directory(os.path.join(os.path.dirname(__file__), '..', '..', 'lookup_plugins'))

    lookup_

# Generated at 2022-06-22 12:07:14.230154
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    import os
    import sys

    data_loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(data_loader,'/opt/ansible_test/inventory')
    variable_manager.set_inventory(inventory)
    playbook_path = '/opt/ansible_test/test.yml'

    if not os.path.exists(playbook_path):
        print('[INFO] The playbook does not exist')

# Generated at 2022-06-22 12:07:23.518037
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    # 1)
    # test "string"
    result = lookup_module.run(terms = ['test_lookup_plugin.j2'],
                               variables = {'name' : 'test_lookup_plugin'})
    assert result == ['Hello test_lookup_plugin']
    # 2)
    # test "list"
    result = lookup_module.run(terms=['test_lookup_plugin.j2'],
                               variables={'name': ['test_lookup_plugin', 'test']})
    assert result == ['Hello test_lookup_plugin']
    # 3)
    # test "dict"

# Generated at 2022-06-22 12:07:29.529984
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import lookup_loader

    lookup_plugin = lookup_loader.get('template')
    result = lookup_plugin.run(['{{ ansible_managed }}'], dict(ansible_managed='Ansible managed: Do not change'), variable_start_string='{{', variable_end_string='}}')
    assert result[0] == 'Ansible managed: Do not change'

    assert lookup_plugin.run(['test_template'], dict(), variable_start_string=None, variable_end_string=None, comment_start_string=None, comment_end_string=None) == [u'Hello World\n']

# Generated at 2022-06-22 12:07:38.861264
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # If a file exists, read it and return the content.
    # If the file does not exist, raise AnsibleError.

    # Arrange
    test_templar = DummyTemplar()
    test_loader = DummyLoader()
    test_env = DummyEnvironment()
    test_terms = ['test.j2']
    test_variables = {
        'test': 'test',
        'ansible_search_path': ['test']
    }

    test_lookup_module = LookupModule()
    test_lookup_module._templar = test_templar
    test_lookup_module._loader = test_loader
    test_lookup_module._templar.environment = test_env

# Generated at 2022-06-22 12:08:23.145124
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    if not HAS_PYTEST:
        return
    from ansible.module_utils._text import to_bytes
    from ansible.template import generate_ansible_template_vars
    from ansible.module_utils.six import PY2

    lookup_object = LookupModule()
    searchpath = ["/test"]
    _variable_manager = FakeVariableManager()
    _loader = FakeDataLoader()
    lookup_object._templar = FakeTemplar(loader=_loader, variables=_variable_manager)
    _loader._search_path = searchpath

    # test raw template
    template_data = """
    {{ ansible_managed }}
    {% if test1 %}
    test1
    {% endif %}
    """

# Generated at 2022-06-22 12:08:33.292444
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.utils.display import Display
    from ansible.utils.path import unfrackpath

    display = Display()

    lookup = LookupModule()
    lookup.set_options(variable_start_string='{{', variable_end_string='}}')

    fixture_path = unfrackpath('/test/test_lookup_plugins/fixtures/test.j2')
    testfile = fixture_path

    # result = {'msg': 'Hello World'}
    # result is a list
    result = lookup.run([testfile], {})
    result_msg = ''.join(result)
    assert result_msg == 'Hello World\n'



# Generated at 2022-06-22 12:08:43.742829
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Unit test needs to create a fake environment.
    # Globals need to be set first.
    import ansible.utils.display
    ansible.utils.display.Display = Display
    Display.verbosity = 4

    import ansible.lookup
    from ansible.plugins.loader import lookup_loader

    lookup_module = lookup_loader.get('template', class_only=True)
    terms = ['test_template.j2']
    variables = { 'username': 'admin', 'password': 'topsecret', 'string_var': 'string' }

    ret = lookup_module.run(terms, variables, convert_data=True, variable_start_string='[%', variable_end_string='%]', comment_start_string='[#', comment_end_string='#]')

# Generated at 2022-06-22 12:08:55.669003
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()

# Generated at 2022-06-22 12:09:03.834720
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Setup the class
    lookup = LookupModule()

    # Setup the lookup input
    terms = ['../../../test/integration/data/files/lookup_template.j2']
    variables = {'ansible_search_path': ['/home/fryrear/tmp/ansible/local/lib']}

    # Run the code and get the result
    result = lookup.run(terms, variables)

    # Assert the result
    assert result == ["\ntest1\ntest2\ntest3\n"]

# Generated at 2022-06-22 12:09:14.537775
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    mock_self = MockLookupModule()

    lookup_options = dict(
        template_vars=dict(
            foo="bar",
            baz=5,
        ),
    )

    mock_self.set_options(var_options=dict(), direct=lookup_options)

    # capture options
    convert_data_p = mock_self.get_option('convert_data')
    lookup_template_vars = mock_self.get_option('template_vars')
    jinja2_native = mock_self.get_option('jinja2_native')
    variable_start_string = mock_self.get_option('variable_start_string')
    variable_end_string = mock_self.get_option('variable_end_string')
    comment_start_string = mock_self.get_option

# Generated at 2022-06-22 12:09:26.043442
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test run with a nonexistent file
    test_file = "nonexistent.j2"

    lookup_module = LookupModule()
    terms = [test_file]
    variables = {}
    kwargs = {}

    try:
        lookup_module.run(terms, variables, **kwargs)
    except AnsibleError as e:
        assert test_file in str(e)

    # test run with an existent jinja file
    test_file = "test_jinja2_template.j2"
    test_variable_name = "test_variable_name"
    test_variable_value = "test_value"
    lookup_module = LookupModule()
    terms = [test_file]
    variables = {test_variable_name: test_variable_value}
    kwargs = {}


# Generated at 2022-06-22 12:09:59.170779
# Unit test for method run of class LookupModule

# Generated at 2022-06-22 12:10:01.519626
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    data = 'hello {{ foo }}'
    terms = ['data']
    variables = {'foo': 'world'}

    res = lookup_module.run(terms=terms, variables=variables)
    assertVars = 'hello world'
    assert res == [assertVars]

# Generated at 2022-06-22 12:10:12.277875
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    display = Display()
    display.verbosity = 4
    display._verbosity = 4

    template_string = "{{ [1,2,3] | sum(start=10) }}"
    template_file = "/tmp/ansible_template_plugin.j2"

    temp_file = open(template_file,'w')
    temp_file.write(template_string)
    temp_file.close()
    searchpath = ['/usr/ansible','/tmp']

    lookup_template_vars = {}

    convert_data_p = False

    variable_start_string = '{{'
    variable_end_string = '}}'
    comment_start_string = '{{'
    comment_end_string = '}}'

    jinja2_native = False
