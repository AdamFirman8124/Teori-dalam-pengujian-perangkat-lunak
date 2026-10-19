

# Generated at 2022-06-22 12:01:12.798799
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    args = {}
    args['_terms'] = ['foo.j2', 'bar.j2']
    args['_raw_params'] = 'variable_start_string="<%" variable_end_string="%>"'
    
    lookup_module = LookupModule()
    lookup_module.set_loader()
    lookup_module.set_environment()
    lookup_module.set_options(var_options=[], direct=args)
    
    results = lookup_module.run(**args)
    assert results == ['foo', 'bar']

# Generated at 2022-06-22 12:01:24.771660
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # LookupModule: run method tests
    mod_name = 'ansible.plugins.lookup.template'
    mock_module = imp.load_source(mod_name, os.path.join(os.path.dirname(__file__), mod_name + '.py'))
    my_object = mock_module.LookupModule()
    my_object.set_loader(DictDataLoader({}))
    my_object.set_templar( Templar({'test_var': 'value'}))
    def open(path):
        if path == 'test_path':
            return io.StringIO('test_file_content')
        else:
            raise AnsibleFileNotFound()

    with patch.object(mock_module, 'open', create=True, side_effect=open):
        my_object._templ

# Generated at 2022-06-22 12:01:36.518850
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a mock display class to write out test messages
    class MockDisplay:
        def __init__(self):
            self.log_calls = []
            pass

        def debug(self,msg):
            self.log_calls.append(msg)

    global display
    mock_display = MockDisplay()
    display = mock_display

    # Using a simple template with no vars

    class MockLookupBase:
        def __init__(self):
            self.template_data = ''
            self.search_paths = []
            self.lookup_template_vars = {}
            pass

        def find_file_in_search_path(self, vars, subdir, file):
            return "Simple template"

        def _get_file_contents(self, lookupfile):
            return self.template_data

# Generated at 2022-06-22 12:01:43.854324
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Testcase 1: lookup_template_vars is not empty and convert_data is not False
    lookup_template_vars = {
        'test': 'value'
    }
    x = LookupModule()
    x._templar = None
    x._loader = None
    result = x.run(['index.html.j2'], {}, convert_data=True, template_vars=lookup_template_vars)

# Generated at 2022-06-22 12:01:55.825039
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # The mock ansible template
    template = "/home/user/playbooks/templates/test.j2"
    assert os.path.isfile(template)

    # Dump template content
    with open(template, 'r') as f:
        template_content = f.read()

    # The lookup module to test
    lookup = LookupModule()

    # Mock task context
    variables = {'ansible_search_path': ['/home/user/playbooks']}
    kwargs = {
        'variable_start_string': '{%', 'variable_end_string': '%}',
        'comment_start_string': '[#', 'comment_end_string': '#]',
        'convert_data': False, 'jinja2_native': True
    }

    # We just want to test the method

# Generated at 2022-06-22 12:02:07.987325
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import pytest

    # Function loads json file and returns the content
    def load_json(json_file):

        import json

        with open(json_file, 'r') as f:
            mock_data = json.loads(f.read())
        return mock_data

    # Mock of AnsibleEnvironment class
    class MockEnvironment(object):

        def copy_with_new_env(self, environment_class=None):
            return self

        def __init__(self, variable_start_string=None, variable_end_string=None,
                     comment_start_string=None, comment_end_string=None,
                     available_variables=None, searchpath=None):

            self.variable_start_string = variable_start_string
            self.variable_end_string = variable_end_string
            self.comment_start

# Generated at 2022-06-22 12:02:16.989843
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Testing method run of class LookupModule

    # Testing variable convert_data_p with value True
    # Testing variable lookup_template_vars with value None
    # Testing variable jinja2_native with value False
    # Testing variable variable_start_string with value '{{'
    # Testing variable variable_end_string with value '}}'
    # Testing variable comment_start_string with value '{#'
    # Testing variable comment_end_string with value '#}'
    # Testing variable terms with value []
    # Testing variable variables with value {}
    # Testing variable kwargs with value {}


    # Setup mock modules and test directory
    import tempfile
    import shutil
    from ansible import context

    temp_dir = tempfile.mkdtemp()


# Generated at 2022-06-22 12:02:25.043865
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # create an instance of LookupModule
    lm = LookupModule()

    # attempt running with no arguments
    try:
        lm.run([])
    except Exception as e:
        assert isinstance(e, AnsibleError)
        print(e)

    # attempt running with invalid arguments
    try:
        lm.run(["invalid_file.j2"])
    except Exception as e:
        assert isinstance(e, AnsibleError)
        print(e)

    # attempt running with valid arguments
    result = lm.run(["../../../../../../etc/passwd"])
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0].startswith("root:x:0:0:root:")

    # attempt running with valid arguments
    result

# Generated at 2022-06-22 12:02:36.909838
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.display import Display
    from ansible.template import AnsibleEnvironment

    # Create a test template
    template = '''{{ ansible_managed }}
# Test comment with {{ lookup_template_vars['var'] }}
{% for item in lookup_template_vars['list'] %}{{ item }}{% endfor %}
# Test comment with {{ lookup_template_vars['var'] }} after the loop
'''
    template_file = '/tmp/template_test'
    with open(template_file, 'w+') as f:
        f.write(to_bytes(template))

    # Params for the lookup
    terms = [template_file]
    
    # Params for the jinja2 context
    variable_start_string = '{{'
    variable_end_string = '}}'


# Generated at 2022-06-22 12:02:47.906169
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import PY2

    data = (b'foo: bar\nbaz: qux', None)

    module = LookupModule()
    module.set_loader_for_testing('/path/to/loader')
    module._loader._mock_data['/path/to/loader/templates/test.j2'] = data

    terms = ['test.j2']
    variables = {'foo': 'test'}

    ret = module.run(terms, variables, convert_data=True, jinja2_native=False, lookup_template_vars=None)

    if PY2:
        # Note: literals used are implicitly unicode in Python 2
        assert ret == [u'{foo: test, baz: qux}']

# Generated at 2022-06-22 12:03:05.372711
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.unsafe_proxy import UnsafeProxy
    from ansible.module_utils.six.moves import StringIO

    import sys
    import json


# Generated at 2022-06-22 12:03:16.790042
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    display = Display()
    display.verbosity = 4

    import os.path
    search_path = [os.path.join('/', 'home', 'mikhail', 'ansible')]
    term = 'index.j2'
    variable_start_string = '['
    variable_end_string = ']'
    comment_start_string = '['
    comment_end_string = ']'
    convert_data = False
    lookup_template_vars = {
        "first": "abc",
        "second": [1, 2, 3]
    }

    from ansible.vars import VariableManager
    from ansible.plugins.loader import lookup_loader
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    variables = VariableManager()


# Generated at 2022-06-22 12:03:28.252943
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # create instance of LookupModule
    lookup_module = LookupModule()

    # create mock of class display
    lookup_module.display = MockDisplay()

    # create mock of class Ansible
    lookup_module.ansible = MockAnsible()

    # create mock of class AnsibleTemplate
    lookup_module.ansible.template = MockAnsibleTemplate()

    # create mock of class AnsibleFileSystemLoader
    lookup_module.ansible.loader = MockAnsibleFileSystemLoader()

    # create mock of class AnsibleVariableManager
    lookup_module.ansible.vars = MockAnsibleVariableManager()
    lookup_module.ansible.vars.get_vars.return_value = dict()

    # create mock of class AnsibleTemplateVars
    lookup_module.ansible.template_vars = MockAn

# Generated at 2022-06-22 12:03:32.209114
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Init LookupModule
    lookup1 = LookupModule()

    # Assert
    assert lookup1.run([], {}) == []

    # Assert
    assert lookup1.run([], {"template_vars":{"weapon": "katana"}}) == []

# Generated at 2022-06-22 12:03:42.209128
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a LookupModule instance
    l = LookupModule()

    # Get the path of the folder containing this test file
    path = os.path.dirname(os.path.abspath(__file__))

    # Get the path of the test file
    test_template_file_path = os.path.join(path, 'test_template_file.j2')

    # Create a dictionary which will be used as variables by the lookup
    variables = {
        'test_var': True,
        'test_var_false': False,
        'test_var_int': 1,
        'test_var_string': 'test',
        'test_var_dict': {'A': 'B'},
        'test_var_list': [1, 2, 3],
        'test_var_none': None
    }

# Generated at 2022-06-22 12:03:51.451366
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import doctest
    from ansible.module_utils._text import to_bytes

    def my_find_file_in_search_path_native(self, var_name, paths, unsafe=False):
        '''
        This is a copy of the module LookupModule's method find_file_in_search_path
        used to test LookupModule's run method.
        This method must be called for run method to use it.
        '''
        self._templar.set_available_variables(self._templar._available_variables)
        lookupfile = self._templar.template(paths[0])
        lookupfile = to_bytes(lookupfile, errors='surrogate_or_strict')
        paths[0] = lookupfile
        return super(LookupModule, self).find_file_in_

# Generated at 2022-06-22 12:04:00.442719
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Unit test for method run of class LookupModule."""

    ############################################################################
    # Create instances of the needed mocks.
    ############################################################################

    # The mock for class LookupBase.
    mock_lookup_base = mock.create_autospec(LookupBase)

    # The mock for method AnsibleModuleUtilsTemplateVars.generate_ansible_template_vars.
    mock_method_generate_ansible_template_vars = mock.create_autospec(AnsibleModuleUtilsTemplateVars.generate_ansible_template_vars)

    # The mock for method AnsibleModuleUtilsTemplateVars.set_temporary_context.

# Generated at 2022-06-22 12:04:11.121315
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    # test 1: convert_data is unset
    # expect: convert_data is set to True
    lookup_module.set_options(direct={})
    assert(True == lookup_module.get_option('convert_data'))

    # test 2: convert_data is set to False
    # expect: convert_data is set to False
    lookup_module.set_options(direct={"convert_data": False})
    assert(False == lookup_module.get_option('convert_data'))

    # test 3: convert_data is set to True
    # expect: convert_data is set to True
    lookup_module.set_options(direct={"convert_data": True})
    assert(True == lookup_module.get_option('convert_data'))

    #

# Generated at 2022-06-22 12:04:22.900994
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    module = LookupModule()

    terms = ['./some_template.j2']

    variables = {'template_vars': {'my_var': 'my_value'}}

    result = module.run(terms,variables)

    assert len(result) == 1

    expected = 'This is {{my_var}}\n'

    assert result[0] == expected

    terms = ['./some_template.j2', './some_other_template.j2']

    result = module.run(terms, variables)

    expected = 'This is {{my_var}}\n'

    assert len(result) == 2

    assert result[0] == expected

    assert result[1] == expected

    terms = ['./jinja2_native_types.j2']


# Generated at 2022-06-22 12:04:33.539077
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Testing run
    #
    # Args:
    #     terms (list)
    #     variables (dict)

    ########
    # mock
    ########

    from ansible.template import generate_ansible_template_vars, AnsibleEnvironment
    from ansible.utils.display import Display
    from ansible.plugins.loader import LookupModule as loader_LookupModule
    from ansible.plugins.lookup.template import LookupModule
    from ansible.template import generate_ansible_template_vars, USE_JINJA2_NATIVE

    class Mock_loader_LookupModule:

        @staticmethod
        def _get_file_contents(file):
            return to_bytes('''{% set var1 = 'value1' %}
{{ var1 }}''')


# Generated at 2022-06-22 12:04:54.896353
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    display = Display()

    # Test template_vars and convert_data options
    print("Testing template_vars and convert_data lookup option")
    lookup_options = dict(
        variable_start_string='[%', variable_end_string='%]',
        convert_data=True, template_vars={'test_var': 'some_value'},
        lookup_file=True
    )
    lookup = LookupModule()
    lookup.set_loader(DictDataLoader(dict(
        templates={'test_file.j2': "[% test_var %]"}
    )))
    assert lookup.run(
        ['/home/user/test_file.j2'], dict(), **lookup_options
    ) == ['some_value']

    # Test jinja2_native option

# Generated at 2022-06-22 12:05:06.394693
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    mock_self = MockClass()
    lookupModule = LookupModule()
    lookupModule.run(["hex_value.j2"], {}, _templar=mock_self)

from ansible.template import AnsibleTemplate
import jinja2
import os
from unittest.mock import patch
from unittest import TestCase
import collections

from ansible.template import generate_ansible_template_vars, AnsibleEnvironment
from ansible.utils.display import Display

template_dir = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'lib', 'ansible', 'template')


# Generated at 2022-06-22 12:05:19.344771
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    import os
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable

    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))))
    from ansible.plugins.loader import lookup_loader

    mod = lookup_loader.get("template", class_only=True)()
    # No file
    assert isinstance(mod.run(["f"], {"var": "val"}, convert_data=False, template_vars={}), list)
    # File exists and is not a directory
    assert isinstance(mod.run(["README.md"], {"var": "val"}, convert_data=False, template_vars={}), list)

# Generated at 2022-06-22 12:05:32.204179
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['../lookup_plugins/templates/test_template.j2']
    display = Display()
    variables = AnsibleEnvironment()
    # Set a mock for the templar
    templar = AnsibleEnvironment()
    display.debug('Mock jinja2 environment created')
    templar.variable_start_string = '{{'
    templar.variable_end_string = '}}'
    template_data = (u'host_var: {{ hostvars["localhost"]["foo"] }}\n'
                     u'inventory_hostname: {{ inventory_hostname }}\n'
                     u'group_name: {{ group_names[0] }}')
    display.debug('Mock template data: %s' % template_data)
    templar.available_variables = variables
    # Templar

# Generated at 2022-06-22 12:05:43.225145
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    assert lookup.run([], {}) == []

    lookup._templar = mock_templar
    lookup._loader = mock_loader
    mock_loader.path_dwim.return_value = "/test/test.j2"
    mock_loader._get_file_contents.return_value = (to_bytes("data"), False)

    results = lookup.run(["./test.j2"], {})
    mock_loader._get_file_contents.assert_called_once_with("/test/test.j2")
    mock_loader.path_dwim.assert_called_once_with({}, "templates", "./test.j2")

# Generated at 2022-06-22 12:05:53.335813
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module._templar = lambda: None
    lookup_module._templar.environment = lambda: None
    lookup_module._templar.environment.loader = lambda: None
    lookup_module._templar.environment.loader._get_file_contents = lambda a: (b'test', False)
    lookup_module._templar.template = lambda a: a
    lookup_module._templar.copy_with_new_env = lambda *a, **kw: lookup_module._templar
    lookup_module._templar.set_temporary_context = lambda self, **kw: self
    lookup_module._loader = lambda: None
    lookup_module._loader._get_file_contents = lambda a: (b'test', False)

# Generated at 2022-06-22 12:05:56.157820
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    assert lm.run(['test1.txt', 'test2.txt'], dict()) == ['this is a test', 'this is another test']

# Generated at 2022-06-22 12:05:57.903723
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    assert False, "Need to write unit tests for LookupModule.run"

# Generated at 2022-06-22 12:06:06.889048
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module.set_loader({'templates/formats/file.j2' : '', 'templates/formats/file2.j2' : ''})

    result = lookup_module.run(terms=['formats/file.j2', 'formats/file2.j2'], variables=dict(),
                               convert_data=False, jinja2_native=False, template_vars=dict(),
                               variable_start_string='{{', variable_end_string='}}',
                               comment_start_string='{#', comment_end_string='#}')

    assert result == ['', '']

# Generated at 2022-06-22 12:06:07.424478
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-22 12:06:39.235890
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # START test for https://github.com/ansible/ansible/issues/16111
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext

    class MyTemplar(Templar):
        def __init__(self):
            super(MyTemplar, self).__init__(loader=DataLoader(), variables={'var': 'abc'})

    class MyLookupModule(LookupModule):
        _templar = MyTemplar()

    results = MyLookupModule(None, None, 'test_var', None, dict()).run('/tmp/test_template', PlayContext(), None, None)

# Generated at 2022-06-22 12:06:48.736633
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup_module = LookupModule()

    term = './some_template.j2'
    # test values of options
    convert_data_p = True
    lookup_template_vars = {'var1': 'value1', 'var2': {'var2_1': 'value2_1', 'var2_2': 'value2_2'}}
    variable_start_string = '{{'
    variable_end_string = '}}'

    template_data = 'Template with simple variable {{ var }}'
    lookupfile = './some_template.j2'

    # create copy of variables with ansible_search_path and ansible_{path,mtime} added to dictionary
    variables = dict()
    variables['ansible_search_path'] = ['.']

# Generated at 2022-06-22 12:07:00.664547
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    #
    # Test with default config
    #
    lookup = LookupModule()
    #
    # Test absent file
    #
    with pytest.raises(AnsibleError) as excinfo:
        lookup.run(['not_existing.yml'], {}, convert_data=False)
    assert 'could not be found for the lookup' in str(excinfo.value)
    #
    # Test invalid variable_end_string
    #
    with pytest.raises(AnsibleError) as excinfo:
        lookup.run(['not_existing.yml'], {})
    assert 'Invalid chars in variable_end_string option' in str(excinfo.value)
    #
    # Test invalid comment_end_string
    #

# Generated at 2022-06-22 12:07:08.185918
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()
    terms = ['does_not_exist.j2']
    variables = {}
    options = {}

    # test without convert_data
    lookup_module = LookupModule()
    lookup_module.set_loader(loader)
    lookup_module.set_variable_manager(variable_manager)
    lookup_module.run(terms, variables, **options)

# Generated at 2022-06-22 12:07:16.363554
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = [
        './some_template.j2',
    ]
    variables = {
        'variable_start_string': '[%',
        'variable_end_string': '%]',
        'comment_start_string': '[#',
        'comment_end_string': '#]',
    }
    lookup_module = LookupModule()
    results = lookup_module.run(terms, variables, **variables)
    for result in results:
        print(to_text(result))


if __name__ == "__main__":
    test_LookupModule_run()

# Generated at 2022-06-22 12:07:26.323823
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_templ = LookupModule()
    terms_1 = {'test.j2': 'This is a test template!'}
    terms_2 = ['test.j2', 'test.j2']
    templar_1 = {}
    templar_2 = {{'test.j2': 'This is a test template!'}}
    lookup_templ.run(terms_1, templar_1)
    assert terms_1 == templar_2
    lookup_templ.run(terms_2, templar_1)
    import pdb; pdb.set_trace()
    assert terms_2 == templar_2


# Generated at 2022-06-22 12:07:31.529558
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    class Options(object):
        def __init__(self, **entries):
            self.__dict__.update(entries)

    class Vars(object):
        def __init__(self, **entries):
            self.__dict__.update(entries)

    # Test with template_vars
    options = Options(convert_data=False, template_vars={"test_var": "test_value"})
    vars = Vars(ansible_search_path=["/ansible/search/path"])
    lookup = LookupModule(loader=None, templar=None, variables=vars, **options.__dict__)

    terms = ["test_template.j2"]
    results = lookup.run(terms, variables=vars)


# Generated at 2022-06-22 12:07:42.741483
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test run method of class LookupModule
    test_lookup = LookupModule()
    test_lookup.set_loader({'_basedir': '', '_get_file_contents': lambda x: ('{{ test }}', False)})

    test_ret = test_lookup.run(['template.j2'], {'test': 'test'}, {})

    # Check that run method returns a list with one string
    assert isinstance(test_ret, list)
    assert len(test_ret) == 1
    assert isinstance(test_ret[0], str)

    # Check that the string returned by run method is what it should be
    assert test_ret[0] == 'test'

    # Test run method with jinja2_native option
    test_lookup = LookupModule()
    test_lookup

# Generated at 2022-06-22 12:07:54.041989
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play

#    yaml_data = """
#    ---
#    - hosts: localhost
#      gather_facts: False
#
#      tasks:
#        - name: Test
#          debug:
#            msg: "{{lookup('template', 'test.j2', template_vars={'variable': 'value'})}}"
#    """
#
#    # Create data loader and variable manager
#    loader = DataLoader()
#    loader.set_basedir(os.path.dirname(__file__))
#    variable_manager = VariableManager()
#    inventory = Inventory(loader=loader, variable_manager=

# Generated at 2022-06-22 12:08:06.728954
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    mod = LookupModule()
    mod.set_loader(dict(path=[os.path.join(os.path.dirname(__file__), '..', 'test_data/lookup_plugins')]))
    mod.set_environment(dict(path=['/bin', '/usr/bin'],
                             ansible_search_path=[os.path.join(os.path.dirname(__file__), '..', 'test_data/lookup_plugins')]))
    display.verbosity = 3
    assert mod.run(terms=['stringtest.j2'], variables={'myvar': 'myvalue'}) == ['myvalue is a string']

# Generated at 2022-06-22 12:08:47.100349
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert False, "TODO"

# Generated at 2022-06-22 12:08:48.612339
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule().run(["{{foo}}"], {}) == ["{{foo}}"]

# Generated at 2022-06-22 12:09:00.315229
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create empty AnsibleOptions object
    ansible_options = object()
    # Create empty Vars object
    ansible_vars = object()
    # Create empty InventoryManager object
    inventory_manager = object()
    # Create empty Host object
    host = object()
    # Create empty PlayContext object
    play_context = object()
    # Create empty private dictionary for LookupModule object
    private_dic = object()
    # Create LookupModule object with specified options
    lookup_obj = LookupModule(ansible_options=ansible_options,
                              ansible_vars=ansible_vars,
                              loader=inventory_manager,
                              templar=host,
                              shared_loader_obj=play_context,
                              _templar=private_dic)
    # Create empty terms list


# Generated at 2022-06-22 12:09:08.733499
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    # Without convert_data
    result = lookup_module.run(terms=['../../test/templates/test_template_jinja2.j2'], variables=dict())
    assert result == [u'This is a test, OK.\n']
    # With convert_data
    result = lookup_module.run(terms=['../../test/templates/test_template_jinja2.j2'], variables=dict(), convert_data=True)
    assert result == [u'This is a test, OK.\n']


# Generated at 2022-06-22 12:09:15.731107
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    #ret = direct_LookupModule_run([u'my_template.j2'], {'myvar': 'myvalue'}, convert_data=False)
    ret = direct_LookupModule_run([u'my_template.j2'], {}, convert_data=False)
    assert ret == [u'Hello World']


# Generated at 2022-06-22 12:09:27.246321
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.plugins.loader import lookup_loader
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.inventory.host import Host

    env = 'dev'
    loader = lookup_loader
    templar = None
    shared_loader_obj = None
    lookup_plugin = 'template'
    loader.get_all(env, templar, shared_loader_obj, lookup_plugin)

    # create ansible host object
    host = Host(name='localhost')

    # create variables
    variables = {}

    # create ansible object
    ansible = object()

    # create the lookup object

# Generated at 2022-06-22 12:09:34.766898
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    templar = LookupModule()
    result = templar.run(terms=['test-dummy.j2', 'test-dummy-2.j2'],
                         variables={'item_key': 'item_value'},
                         convert_data=True,
                         jinja2_native=False,
                         variable_start_string='{{',
                         variable_end_string='}}')
    expected = [u'item_key=item_value\nitem_key=item_value\n']
    assert result == expected

# Generated at 2022-06-22 12:09:44.634317
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Test function for module lookup/template.py
    Test function run of class LookupModule
    """

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    loader = DataLoader()
    hostvars = {"testhost": {"ansible_connection": "local",
                             "ansible_host": "127.0.0.1",
                             "ansible_inventory": ["testhost"]}}
    inventory = InventoryManager(loader=loader, sources=[])
    inventory.set_host_variable(host=hostvars.keys()[0], variable=hostvars)

# Generated at 2022-06-22 12:09:53.720559
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    This method tests the run method of class LookupModule. It
    checks if the returned list contains the same number of elements
    as the number of elements in the list of templates. For each
    element in the returned list, it checks if the content of the
    template is the same as the content of the element in the
    returned list.
    """

    # Initialise variables
    variable_start_string = '{{'
    variable_end_string = '}}'
    template_vars = {'my_name': 'John'}
    module_path = os.path.dirname(os.path.abspath(__file__))
    test_file = os.path.join(module_path, '..', 'test_data', 'test.j2')

# Generated at 2022-06-22 12:09:57.666101
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    #this test is not ready yet as we have to initalize some plugin infrastructure
    #lookup_mod = LookupModule()
    #lookup_mod.run(['some_template.j2'], {'template_vars': {'bla': 'blub'}})
    pass