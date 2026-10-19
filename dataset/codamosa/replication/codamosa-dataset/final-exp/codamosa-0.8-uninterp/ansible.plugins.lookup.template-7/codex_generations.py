

# Generated at 2022-06-22 12:01:15.002708
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()

    template_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'units', 'utils', 'fixtures', 'lookup_plugins', 'template.j2'))

    terms = [template_path]
    variables = {
        "variable1": "value1",
        "ansible_search_path": [os.path.dirname(template_path)],
    }

    result = module.run(terms, variables)
    assert result == ['Hello World!\n']

# Generated at 2022-06-22 12:01:27.432893
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six.moves import builtins

    # define return value of method find_file_in_search_path
    # Expected to be called with arguments variables and term
    # This is in order to not throw exception at AnsibleFind(self, variables)
    def find_file_mock(self, variables, directories, term):
        return "lookupfile_mock_return"

    # define return value of method _get_file_contents
    # Expected to be called with arguments lookupfile
    # This is in order to not throw exception at AnsibleLoader(self, basedir, 'lookupfile_mock_return')
    def get_file_contents_mock(self, lookupfile):
        lookupfile = lookupfile.replace('\\', '/')

# Generated at 2022-06-22 12:01:38.865941
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Initialization
    x = {}
    x['one'] = 1
    x['two'] = 2
    x['vars'] = {}

    class Dummy_module():
        def __init__(self):
            self.params = x

    class Dummy_loader():
        def get_basedir(self, *args, **kwargs):
            pass

        def _find_file_in_search_path(self, *args, **kwargs):
            pass

        def _get_file_contents(self, *args, **kwargs):
            return "{{ one }}", True

    class Dummy_template():
        pass

    class Dummy_templar():
        def __init__(self):
            self.environment = Dummy_template()


# Generated at 2022-06-22 12:01:51.519193
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # lookup_templates ['./template.j2', './template2.j2', './template3.txt.j2']
    module = LookupModule()
    terms = ['./template.j2', './template2.j2', './template3.txt.j2']

# Generated at 2022-06-22 12:02:03.537722
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a class object
    LookupModule_obj = LookupModule()

    # Set the paths to template and inventory files
    template_path = os.path.join(os.path.dirname(__file__), 'test_template.j2')
    variables_path = os.path.join(os.path.dirname(__file__), 'test_variable.yaml')

    # Read the YAML file with variables
    with open(variables_path) as stream:
        variables = yaml.safe_load(stream)

    # Set the arguments for method run()
    terms = [template_path]
    success, msg = LookupModule_obj.run(terms, variables)

    # Check if the template was rendered successfully
    assert success == True
    print(msg)

    # Test output validity

# Generated at 2022-06-22 12:02:14.577059
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import pytest
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    # prepare the mocks
    class FakeEnv():

        def __init__(self, new_searchpath):
            self.searchpath = new_searchpath

        def get_temporary_context(self):
            return FakeEnv(self.searchpath)

        def set_available_variables(self, available_variables):
            self.vars = available_variables

        def from_string(self, template_data):
            return FakeTemplar(content=template_data)

    class FakeTemplar():

        def __init__(self, content):
            self.content = content

        def template(self, preserve_trailing_newlines):
            return self.content


# Generated at 2022-06-22 12:02:24.102524
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    def get_option(k):
        return getattr(module, k)
    module._templar = type('Templar', (object,), {'template': lambda s: s, 'copy_with_new_env': lambda x: module._templar})
    module.set_options = lambda x, y: None
    module.find_file_in_search_path = lambda x, y, z: z
    module._loader = type('Loader', (object,), {'_get_file_contents': lambda x: ('some content', True)})

    assert module.run([], {}) == ['some content']

# Generated at 2022-06-22 12:02:35.947880
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['127.0.0.1,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    templar = LookupModule()
    templar.set_options(var_options=variable_manager, direct={})

    res = templar.run(['./some_template.j2'], {})
    assert res == []

    term = './some_template.j2'
    lookupfile = './some_template.j2'
    b_template_data = b"Hello World!"
    show_data = "Hello World!"
   

# Generated at 2022-06-22 12:02:38.661557
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert False, 'No tests defined'

# Generated at 2022-06-22 12:02:49.932920
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = object()
    loader = object()
    variable_manager = object()
    templar = object()
    convert_data = object()
    lookup_template_vars = object()
    lookupfile = object()
    template_data = object()
    vars = object()


# Generated at 2022-06-22 12:03:07.083306
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.utils.template as plugin
    import sys

    lookup_base = plugin.LookupBase()
    real_run = lookup_base.run # Save reference to real method
    terms = ['test1', 'test2']
    check_run = True
    min_version = '0.9'

    def fake_run(self, terms, variables, **kwargs):
        if check_run:
            check_run = False
            assert terms == ['test1', 'test2'], 'Wrong terms was passed'
            assert type(variables) is dict, 'Wrong type of variables'
            assert kwargs == {}, 'Wrong kwargs was passed'
            return ['template_data', 'template_data']
        else:
            return real_run(terms, variables, **kwargs)


# Generated at 2022-06-22 12:03:17.751030
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a test fixture.
    lookup_obj = LookupModule()
    lookup_obj._templar = DummyTemplar()
    lookup_obj._loader = DummyLoader()
    lookup_obj._display = Display()
    lookup_obj._display.verbosity = 4

    # Test successful execution of method.
    # Expected result:
    # - ret is a list of two lists of strings, where the first list contains the string 'Hello, world!'
    #   and the second list contains the string 'Another test'.
    ret = lookup_obj.run(['test1.j2','test2.j2'], {'ansible_search_path': ['test_dir1']})
    assert isinstance(ret, list)
    assert len(ret) == 2
    assert isinstance(ret[0], list)
    assert len

# Generated at 2022-06-22 12:03:29.018611
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play_context import PlayContext

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list='localhost')
    variable_manager.set_inventory(inventory)

    from ansible.utils.vars import combine_vars
    variable_manager._extra_vars = combine_vars(loader=loader, variables={"favcolor": "blue"},
            include_cache=variable_manager.include_cache)
    variable_manager.set_inventory(inventory)

    play_context = PlayContext()

    from ansible.plugins.loader import lookup_loader
    lookup

# Generated at 2022-06-22 12:03:40.140846
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six.moves import builtins
    import sys

    open_name = 'ansible.plugins.lookup.template.open'
    if open_name in sys.modules['ansible.plugins.lookup.template'].__dict__:
        del sys.modules['ansible.plugins.lookup.template'].__dict__[open_name]
    sys.modules['ansible.plugins.lookup.template'].__dict__['open'] = builtins.open

    lookup_plugin = LookupModule()
    assert lookup_plugin
    templar = lookup_plugin._templar
    assert templar

    from ansible.template import template
    template_name = 'ansible.template.template'

# Generated at 2022-06-22 12:03:41.124760
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup = LookupModule()


# Generated at 2022-06-22 12:03:52.748212
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    class AnsibleModule_class_mock:

        class AnsibleFileNotFound_Exception(Exception):
            pass

        def __init__(self):
            self.params = {}

        def fail_json(self, *args, **kwargs):
            raise self.AnsibleFileNotFound_Exception()

    class AnsibleTemplar_class_mock:

        class AnsibleTemplateError_Exception(Exception):
            pass

        def __init__(self):
            self.environment = AnsibleEnvironment_class_mock()
            self.template_vars = None

        def set_available_variables(self, *args, **kwargs):
            pass

        def set_environment(self, *args, **kwargs):
            pass

        def set_options(self, *args, **kwargs):
            pass


# Generated at 2022-06-22 12:03:57.732872
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # This test is disabled because it's hard to test as it instantiates class LookupModule and invokes the run() method.
    # This would require a detailed understanding of what's going on, which is beyond me.
    # But at least this dummy test demonstrates how the test for this class should look like.
    pass

# Generated at 2022-06-22 12:04:03.636716
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # run with options
    terms = ['/tmp/test.j2']
    options = {'comment_start_string': '[#', 'comment_end_string': '#]'}
    variables = {'path': 'foo'}
    results = [u'Hello, foo!']
    assert lookup.run(terms, variables, **options) == results

# Generated at 2022-06-22 12:04:14.951513
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    test_dir = pytest.helpers.make_test_dir()
    os.makedirs(os.path.join(test_dir, 'templates'))

    display = Display()
    display.debug = lambda x: x
    display.vvvv = lambda x: x

    lookup = LookupModule()
    lookup._loader = DictDataLoader({}, basedir=test_dir)

    lookup.set_options(var_options=dict(), direct=dict())

    lookup._templar = Templar(loader=lookup._loader, variables={})

    # Test with single file
    terms = ['foo.j2']
    lookup.run(terms, variables={'foo': 'bar'}, convert_data=True)

    # Test with list of files

# Generated at 2022-06-22 12:04:22.043060
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Unit test for method run of class LookupModule"""
    lookup = LookupModule()
    assert 'my_var' == lookup.run(['my_template'], {'my_var': 'my_var'}, plugin_dir='')[0]
    assert 'my_var' == lookup.run(['my_template'], {'my_var': 'my_var'}, plugin_dir='', jinja2_native=True)[0]

# Generated at 2022-06-22 12:04:43.682660
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # get default options
    options = {
        'convert_data': False,
        'template_vars': {},
        'jinja2_native': False,
        'variable_start_string': u'{{',
        'variable_end_string': u'}}',
        'comment_start_string': u'{#',
        'comment_end_string': u'#}',
    }
    # create lookup module
    lookup_module = LookupModule()
    # run method with default options and return value
    retval = [
        '#!/usr/bin/env python\n',
        '\n',
        '# This file was generated by the Ansible\'s lookup plugin\n',
        '# and contains default values for netbox-ansible\n',
    ]
    res = lookup_module.run

# Generated at 2022-06-22 12:04:54.742661
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    template_data = 'datadatadatadatadatadatadatadatadatadatadatadatadatadatadatadata'
    templar = AnsibleEnvironment(loader=None, variables={})

    term = 'lookup.j2'
    lookupfile = 'lookup.j2'
    vars = deepcopy(variables)


# Generated at 2022-06-22 12:05:07.610496
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.template import Templar
    from ansible.vars.unsafe_proxy import AnsibleUnsafeVars

    terms = './some_template.j2'

# Generated at 2022-06-22 12:05:21.075328
# Unit test for method run of class LookupModule

# Generated at 2022-06-22 12:05:33.293385
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    #1. test for the case of no output file
    # setup the test
    lookupmodule = LookupModule()
    lookupmodule.env=dict()
    lookupmodule.basedir="."
    testterms=["./nooutput.j2"]
    # run the test
    try:
        lookupresult = lookupmodule.run(testterms, lookupmodule.env)
    except AnsibleError:
        #raise
        assert 1==1
    else:
        assert 1==0
    #2. test for other case
    # setup the test
    lookupmodule = LookupModule()
    lookupmodule.env=dict()
    lookupmodule.basedir="."
    testterms=["./templateoutput.j2"]
    # run the test
    lookupresult = lookupmodule.run(testterms, lookupmodule.env)

    # check the result


# Generated at 2022-06-22 12:05:41.529757
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    assert lookup.run(
        terms=None,
        variables=dict(
            ansible_search_path=['/your/home'],
        ),
    ) == []

    from ansible.utils import plugin_docs

    assert 'jinja2_native' in plugin_docs['lookup']['template']
    assert 'convert_data' in plugin_docs['lookup']['template']

    class DummyVars(object):
        def __init__(self, search_path):
            self.search_path = search_path

        def __getitem__(self, item):
            return self.get(item)

        def get(self, item):
            if item is 'ansible_search_path':
                return self.search_path
            else:
                return None

   

# Generated at 2022-06-22 12:05:52.086404
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.plugins.lookup.template as test_template
    from ansible.template import Templar

    module = test_template.LookupModule()
    assert module != None

    # Test with both convert_data and jinja2_native set to True
    # convert_data always takes precedence over jinja2_native
    with open('/tmp/test_jinja2_native', 'w') as f:
        f.write('{{ lookup("pipe","echo 42") }}')

    lookup_template_vars = { 'test_var': 42 }
    jinja2_native = False
    searchpath = ['/tmp']
    b_template_data = '{{ lookup("pipe","echo 42") }}'
    template_data = to_text(b_template_data, errors='surrogate_or_strict')

   

# Generated at 2022-06-22 12:05:57.297240
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_args = ['ansible/test/unit/modules/test_template']
    assert LookupModule().run(terms=test_args, variables={'ansible_search_path': ['./lib']}, variable_start_string='[%', variable_end_string='%]') == ['This is to test the templating lookup']

# Generated at 2022-06-22 12:05:58.254057
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert 1==1


# Generated at 2022-06-22 12:06:08.776478
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    a1 = LookupModule()
    a1.get_option = lambda x: None if x == 'convert_data' else ''
    a1.set_options(var_options=dict(), direct=dict())
    a1._loader = ''
    a1.find_file_in_search_path = lambda x, y, z: z
    a1._templar = ''
    t1 = ['t1.txt']
    ret = a1.run(t1, dict())
    #assert ret == [b'\n']
    assert ret == [u'\n']

    a2 = LookupModule()
    a2.get_option = lambda x: None if x == 'convert_data' else ''
    a2.set_options(var_options=dict(), direct=dict())

# Generated at 2022-06-22 12:06:33.198690
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    #Creating a Mock Environment for testing
    from unittest.mock import patch, Mock
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    # Setting up the Mock Environment
    mock_loader = Mock()
    mock_inventory = Mock(InventoryManager)
    test_vars = Mock(VariableManager)
    test_vars.extra_vars = {"foo": "bar"}
    lookupmodule = LookupModule(loader=mock_loader, environment=None, inventory=mock_inventory, variable_manager=test_vars)

    test_lookup_file = "file1.j2"
    test_lookup_file_path = "/path/to/file1.j2"
    test_look

# Generated at 2022-06-22 12:06:44.636309
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.module_utils._text import to_bytes
    from ansible.parsing.splitter import parse_kv
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    # Prepare environment and args
    terms = [to_bytes('file.j2')]
    jinja2_native = False
    variable_start_string = None
    variable_end_string = None
    comment_start_string = None
    comment_end_string = None
    convert_data_p = False
    lookup_template_vars = {}
    template_data = to_bytes('{% if hubble == 1 %}hubble{% endif %}')
    searchpath = []
    lookupfile = None
    variables = parse_kv(to_bytes('hubble=1'))



# Generated at 2022-06-22 12:06:52.665199
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create the LookupModule instance
    the_ansible_var = {"page": 123, "title": "test page"}
    the_template_var = {"page": 456}
    the_local_var = {"page": 789}
    the_vars = {"ansible_test": the_ansible_var}
    the_local_action = Dict(page=None, content=None)
    the_action = Dict(page=None, content=None)
    the_loader = Dict(path_dwim=lambda self, term: term)
    the_play_context = Dict(variable_manager=Dict(extra_vars=the_template_var))
    the_shared_loader_obj = Dict(searchpath=[])

# Generated at 2022-06-22 12:07:04.567180
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup_module = LookupModule()

    # hardcoding params for unit test, for more information about params
    # check https://github.com/ansible/ansible/blob/devel/lib/ansible/plugins/lookup/template.py#L105
    search_paths = [os.path.dirname(__file__)]
    kwargs = {
        '_templar': None,
        'convert_data': False,
        'template_vars': {},
        'jinja2_native': False,
        'variable_start_string': '{{',
        'variable_end_string': '}}',
        'comment_start_string': None,
        'comment_end_string': None
    }
    # hardcoding params for unit test

    lookup_results = lookup_module.run

# Generated at 2022-06-22 12:07:14.787845
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Patch Display class
    Display.verbosity = 4
    display.verbosity = 4

    # Setup LookupModule object to test
    testobj = LookupModule()
    testobj.set_options(direct={'variable_start_string': '[[', 'variable_end_string': ']]'})

    # Test for term of type string
    test_term_string = './some_template.j2'
    test_term_list = [test_term_string]
    test_term_dict = {'test_key': test_term_string}
    test_variables = {'test_var': 'test_value'}
    test_templar = {}
    test_jinja2_native = False

    # Set return values for relevant mocked methods

# Generated at 2022-06-22 12:07:26.322651
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six.moves.builtins import unicode
    display = Display()

    fake_loader = object()
    fake_templar = object()
    lookup = LookupModule(loader=fake_loader, templar=fake_templar, display=display)

    # test plain strings
    res = lookup.run('dummy', dict(foo='bar'))
    assert [u'dummy'] == res

    # test templating
    terms = [u'{{ foo }}']
    res = lookup.run(terms, dict(foo='bar'))
    assert [u'bar'] == res

    # test jinja2_native
    terms = [u'{{ [1, 2, 3] }}']

# Generated at 2022-06-22 12:07:38.450515
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.executor.task_queue_manager import TaskQueueManager

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader)
    play_source = dict(
      name = "Test Play",
      hosts = 'all',
      gather_facts = 'no',
      tasks = [
        dict(action=dict(module='template',
                         args=dict(src='/tmp/test.j2', dest='/tmp/test_result', convert_data=False)))
      ]
    )
    play

# Generated at 2022-06-22 12:07:48.976279
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import lookup_loader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    lookup = lookup_loader.get(None, 'template')

    terms = ['test-template-jinja2', 'test-template-mustache']

    variable_manager = VariableManager()
    loader = DataLoader()
    variable_manager.set_inventory(InventoryManager(loader=loader, sources=['tests/unit/test_lookup_plugins/inventory']))

    ret = lookup.run(terms=terms,
                     variables=variable_manager.get_vars(),
                     convert_data=True,
                     template_vars={'name': 'Test'})


# Generated at 2022-06-22 12:08:01.130282
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''
    Run unittest for method run of class LookupModule
    '''
    # pylint: disable=unused-argument
    import sys
    import unittest
    import contextlib
    import io
    import os
    import tempfile
    # pylint: disable=import-error
    # pylint: disable=no-name-in-module,import-error
    # pylint: disable=unused-import,wrong-import-position
    from ansible.module_utils._text import to_bytes
    from ansible.template import generate_ansible_template_vars
    # pylint: enable=import-error,wrong-import-position
    from ansible.plugins.lookup import lookup_loader
    # pylint: enable=no-name-in-module,import-error
   

# Generated at 2022-06-22 12:08:12.365209
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.vault import VaultLib
    from ansible.template import Templar
    from ansible.utils.vars import combine_vars
    from ansible.vars import VariableManager
    from ansible.utils.vault import VaultSecret
    from ansible.plugins.lookup import LookupBase
    lookup = LookupModule()

    # this is a very basic test, mostly to check nothing changed
    plaintext = u"""
{{ ansible_managed }}
    """
    this_vars = dict(
        ansible_managed='Ansible managed: Do NOT edit this file manually!',
        foo='bar',
    )
    combine_vars(this_vars, {})

# Generated at 2022-06-22 12:08:53.683050
# Unit test for method run of class LookupModule

# Generated at 2022-06-22 12:09:02.206934
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.path import unfrackpath
    from ansible.vars import VariableManager
    from ansible.playbook.play_context import PlayContext

    # hack to not require ansible-playbook and friends to be installed just to run tests
    from ansible.module_utils._text import to_text
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.errors import AnsibleError

    class TestLookupModule(LookupModule):
        def __init__(self):
            self.basedir = unfrackpath("../../../../")

        def find_file_in_search_path(self, variables, dir_name, file_name):
            paths = variables.get('ansible_search_path', [])

# Generated at 2022-06-22 12:09:12.869333
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # arrange
    LookupModule.set_options = lambda self, var_options, direct: None
    LookupModule.get_option = lambda self, opt: None
    LookupModule.find_file_in_search_path = lambda self, variables, dir_name, term: None
    templar = object()
    LookupModule._templar = templar
    display = object()
    LookupModule.display = display
    loader = object()
    LookupModule._loader = loader
    terms = ['file1']
    variables = {
        'variable1': 'value1',
        'variable2': 'value2',
        'ansible_search_path': ['search_path1', 'search_path2']
    }

# Generated at 2022-06-22 12:09:24.409100
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Given
    lookup_module = LookupModule()
    lookup_module.set_loader({'paths': {'templates': []}})
    lookup_module._loader = {'__name__': 'mock_loader'}
    lookup_module._templar = {'__name__': 'mock_templar'}
    lookup_module._templar.copy_with_new_env = {'__name__': 'mock_templar_copy'}
    lookup_module._templar.set_temporary_context = {'__name__': 'mock_templar_context'}

    # When
    lookup_module.run(['file_to_template'], {}, {})

    # Then
    assert lookup_module.get_option.called
    assert lookup_module.find_

# Generated at 2022-06-22 12:09:35.572393
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Unit test for method run of class LookupModule"""

    # Test set-up
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['tests/inventory'])

    variable_manager.set_inventory(inventory)

    test_play = Play()
    test_play.hosts = ['127.0.0.1']

# Generated at 2022-06-22 12:09:42.217696
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import LookupModule as LookupModule_

    lookup_plugin_instance = LookupModule_()

    test_vars = {'foo': {'bar': 'baz'}}
    test_term = 'foo.j2'
    test_direct = {'template_vars': {'key': 'value'}}
    # FIXME: this test fails because the lookup_template_vars param doesn't work
    assert lookup_plugin_instance.run([test_term], test_vars, **test_direct) == [u'value: baz']

# Generated at 2022-06-22 12:09:51.402345
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    make_fake_module = lambda cls: type('fake_module', (object,), {'_templar': cls,
                                                                   'get_option': lambda self, x: None,
                                                                   'set_options': lambda self, **kwargs: None})

    fake_templar = type('fake_templar', (object,), {'template': lambda self, template_data, preserve_trailing_newlines=True, convert_data=False, escape_backslashes=False: template_data,
                                                    'copy_with_new_env': lambda self, environment_class: self,
                                                    'set_temporary_context': lambda self, **kwargs: self})
    module = make_fake_module(fake_templar)
    module.run = LookupModule.run

# Generated at 2022-06-22 12:10:02.548795
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a mock-AnsibleModule to test lookup
    from ansible.module_utils.six.moves import builtins
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import StringIO
    from ansible.compat.tests import unittest
    import ansible.constants

    class TestLookupModule(LookupModule):
        def __init__(self, basedir=None, *args, **kwargs):
            self.basedir = basedir
            super(TestLookupModule, self).__init__(*args, **kwargs)

        def run(self, terms, variables, **kwargs):
            return super(TestLookupModule, self).run(terms, variables, **kwargs)


# Generated at 2022-06-22 12:10:14.182935
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    global USE_JINJA2_NATIVE
    USE_JINJA2_NATIVE = True
    global __loader__
    from ansible.plugins.loader import lookup_loader
    __loader__ = lookup_loader
    global __file__
    __file__ = "./ansible_collections/ansible_collections/pearson/testing/ansible_collections/pearson/testing/plugins/lookup/template.py"
    display.verbosity = 4

# Generated at 2022-06-22 12:10:19.352046
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module.set_loader(None)

    display.verbosity = 4
    term = 'test_LookupModule_run.j2'
    variables = {}
    lookup_module.run(terms=[term], variables=variables)

    assert False

if __name__ == '__main__':
    test_LookupModule_run()