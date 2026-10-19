

# Generated at 2022-06-22 12:01:09.904205
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: implement this test and add coverage
    # lookup = LookupModule()
    # assert(False)
    pass

# Generated at 2022-06-22 12:01:17.839008
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    text = '''
{{ var_in_include }}
{% include "include.j2" %}
'''
    text_include = '''
{{ var_in_include }}
'''

    assert LookupModule().run([
        'template.j2'
    ], dict(var_in_include="bar"),
        _loader=DictDataLoader({
            'template.j2': text,
            'include.j2': text_include
        }),
        variable_start_string='{{', variable_end_string='}}',
        jinja2_native=True) == ['bar\nbar\n\n']

    # Test variable_start_string and variable_end_string

# Generated at 2022-06-22 12:01:30.498885
# Unit test for method run of class LookupModule
def test_LookupModule_run():
  class AnsibleModule:
    # We don't need the entire class in this case
    def __init__(self):
      self.params = None
  class AnsibleTemplate:
    class AnsibleUndefined:
      def __eq__(self):
        pass

  dummy_term = 'dummy_term'
  dummy_variables = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}

# Generated at 2022-06-22 12:01:35.022100
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    lookup._templar = dict() # override with mock templar
    lookup._loader = dict() # override with mock loader

    lookup.set_options(var_options=dict(), direct=dict())
    lookup.run(terms=[], variables=dict())



# Generated at 2022-06-22 12:01:41.453009
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    terms = 'test_terms'
    vars = 'test_vars'
    options = {
        'convert_data': True,
        'variable_start_string': '{+',
        'variable_end_string': '+}',
        'comment_start_string': '{#',
        'comment_end_string': '#}',
    }
    assert module.run(terms, vars, **options) is None

# Generated at 2022-06-22 12:01:53.214303
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''Unit test for method run of class LookupModule'''

    lookup_mock = """
- path: /tmp/foo.j2
  content: |
    {%- set var = {'foo': 'bar', 'faa': 'bee'} %}
    {%- set var = var | combine(other_var) %}
    {{ var | to_nice_yaml | indent(8) }}
    foo: {{ var.foo }}
    faa: {{ var.faa }}
"""

    lookup_results = [u"\nfoo: bar\nfaa: bee\n    {foo: bar, faa: bee}\n"]

    other_vars = {'other_var': {'faa': 'baz'}}

    # Because our test will be run by pytest, we want to avoid using pytest fixtures


# Generated at 2022-06-22 12:01:58.264093
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    lookup.set_options(dict(variable_start_string='[%', variable_end_string='%]'))
    result = lookup.run(["./example_template.j2"], dict(foo=42, bar="spam"))
    assert to_bytes(result[0]) == to_bytes("[% foo %]")

# Generated at 2022-06-22 12:02:10.690728
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO fix and activate this test
    return
    # create instance of LookupModule class
    lookup_module  = LookupModule()

    # set attributes
    lookup_module._loader = OkLoader()
    lookup_module._templar = OkTemplar()

    # set options
    options = dict(
        _terms=['test_template.j2'],
        convert_data=True,
        template_vars={'test': 'value'},
        jinja2_native=False,
        variable_start_string='{{',
        variable_end_string='}}',
        comment_start_string='{#',
        comment_end_string='#}',
    )
    lookup_module.set_options(var_options={}, direct=options)

    # run method

# Generated at 2022-06-22 12:02:17.650528
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    This is just a quick unit test for the run method of this class
    It makes more sense to call these methods directly and make assertions
    """
    import ansible.plugins.loader as plugin_loader
    plugin_loader.add_directory(os.path.join(os.path.dirname(__file__), '..', '..', 'lookup_plugins'))
    mod = LookupModule()
    mod.set_loader(plugin_loader)

    terms = [ "../../lookup_plugins/template.py" ]
    for term in terms:
        print(term)
        result = mod.run(terms, {})
        print('result: %s' % result)

# Generated at 2022-06-22 12:02:24.390750
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Imports
    from ansible.plugins.loader import lookup_loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext

    # Setup
    lookup_loader.add_directory(os.path.join(os.path.dirname(__file__), 'lookup_plugins'))
    loader = DataLoader()
    play_context = PlayContext()
    variables = dict()

    # Test
    result = LookupModule().run(["test_lookup_template.j2"], variables, loader=loader, play_context=play_context)
    assert result == ['Hello world']

# Generated at 2022-06-22 12:02:40.047534
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    import six

    lookup_instance = LookupModule()

    lookup_instance.set_options({
        'convert_data': False,
        'template_vars': {
            'app': 'example',
        },
        'variable_start_string': '{{',
        'variable_end_string': '}}',
        'comment_start_string': '{#',
        'comment_end_string': '#}',
    })

    # Mock and patch
    #################

    # mock __init__ to avoid file I/O
    lookup_instance._loader = pytest.Mock()
    lookup_instance._loader.path_dwim.return_value = './%s' % (to_text('test_templates/foo.j2'))
    lookup_instance._loader._get_file

# Generated at 2022-06-22 12:02:44.401977
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup_module = LookupModule()
    terms = ['./some_template.j2','./some_template.j2']
    result = lookup_module.run(terms, None)

    assert len(result) == 2
    assert isinstance(result, list)

# Generated at 2022-06-22 12:02:56.641640
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['./some_template.j2']
    variables = {}
    result = LookupModule().run(terms, variables)

    print(result)
    assert(isinstance(result, list))
    # ['{{ 1 + 1 }}'] (test for some_template.j2)

    # result = LookupModule().run(terms, variables, jinja2_native=True)
    # print(result)
    # assert(isinstance(result, list))
    # [2] (test for some_template.j2)

    # result = LookupModule().run(terms, variables, convert_data=True)
    # print(result)
    # assert(isinstance(result, list))
    # [2] (test for some_template.j2)

    lookup_template_vars = {'test': 123}

# Generated at 2022-06-22 12:03:02.036126
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Creating mocks for testing
    import mock
    loader_mock = mock.Mock()
    lookupfile_mock = mock.Mock()
    searchpath_mock = mock.Mock()
    vars_mock = mock.Mock()
    vars_mock.update = mock.Mock()
    vars_mock.update.return_value = None
    vars_mock['ansible_search_path'] = mock.Mock()
    vars_mock['ansible_search_path'].append = mock.Mock()
    vars_mock['ansible_search_path'].append.return_value = None
    jinja_mock = mock.Mock()
    jinja_mock.concat = mock.Mock()

# Generated at 2022-06-22 12:03:13.684567
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # If the below test failed with?
    #     AssertionError: 'template_find(templates, test_jinja2_env.j2)' != ['abc']
    # run this command and try again.
    #   $ python -c "import pyparsing; pyparsing.ParserElement.enablePackrat(); import ansible.plugins.loader"

    # ----------------------------------------------------------------------------
    # test_jinja2_env.j2:
    #   abc
    #   {{ '{{' }}
    #   {{ '}}' }}
    #   {{ '{{}}' }}
    #   {{ '{{' }}
    #   {{ '}}' }}
    #   {{ '{{}}' }}
    #
    # ----------------------------------------------------------------------------

    lm = LookupModule()
    lm._display = Display()
    lookupfile = l

# Generated at 2022-06-22 12:03:20.960250
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    # Py3 imports
    if sys.version_info[0] > 2:
        from unittest.mock import patch, Mock
    else:
        from mock import patch, Mock

    from ansible.plugins.lookup import LookupModule

    lookup_plugin = LookupModule()

    assert not hasattr(lookup_plugin, 'set_options')

    # patching builtins.__import__
    with patch('ansible.plugins.lookup.__builtin__') as mock_builtin:
        mock_builtin.__import__ = Mock(return_value=Mock)
        lookup_plugin = LookupModule()
        assert hasattr(lookup_plugin, 'set_options')

    # create test data

# Generated at 2022-06-22 12:03:31.989586
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    class MockTemplar(object):
        def __init__(self, path_data):
            self.path_data = path_data
            self.templated_data = {}
            self.path_data = {}
            for path, data in path_data.items():
                self.path_data[path] = to_bytes(data)

        def set_available_variables(self, vars):
            pass

        def set_environment(self, environment):
            pass

        def set_vault_secrets(self, vault_secrets):
            pass


# Generated at 2022-06-22 12:03:41.193055
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # FIXME: This unit test is broken right now.
    # We should be able to instantiate a LookupModule here, but it fails
    # because the _loader attribute is not set (it's None).
    # This is because we need to instantiate a LookupBase,
    # and it is called by AnsibleModule with the argument "basedir=".
    #    module = LookupModule()
    #    # This file is created by the test_template.yaml file.
    #    assert module.run(["test_data.txt"], {"convert_data": True}) == [u'test_data_two\n'], module.run(["test_data.txt"], {"convert_data": True})
    pass

# Generated at 2022-06-22 12:03:52.800355
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    file_system = FileSystem()
    loader_mock = LoaderMock(file_system)
    templar_mock = TemplarMock()
    ansible_vars_mock = AnsibleVarsMock(file_system)
    lookup_module_test = LookupModule()
    lookup_module_test._loader = loader_mock
    lookup_module_test._templar = templar_mock
    lookup_module_test._templar._available_variables = ansible_vars_mock
    # test module run - positive pass
    terms = ['foo.template']
    variables = {}
    kwargs = {'convert_data': False, 'template_vars': {'bar': 'Batman'}}

# Generated at 2022-06-22 12:04:03.686282
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import tempfile
    import textwrap

    test_data = textwrap.dedent("""
        [
        {% for item in ['item1', 'item2'] %}
        {% if loop.first %}
        {
        "var1":"{{ item }}",
        "var2":["{{ item }}", "{{ item }}", "{{ item }}"],
        "var3":"{{ item }}"
        }
        {% else %}
        {
        "var1":"{{ item }}",
        "var2":["{{ item }}", "{{ item }}", "{{ item }}"],
        "var3":"{{ item }}"
        }
        {% endif %}
        {% endfor%}
        ]
        """).lstrip()

    test_file = tempfile.NamedTemporaryFile()

# Generated at 2022-06-22 12:04:22.262008
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test successful case
    try:
        lm = LookupModule()
        lm.run(['some_template.j2'], {'var1': 'abc', 'var2': 'def'})
        assert False
    except AnsibleError:
        pass
    else:
        assert True

    # Test failure case
    try:
        lm = LookupModule()
        lm.run([], {'var1': 'abc', 'var2': 'def'})
        assert False
    except AnsibleError:
        assert True
    else:
        assert False

# Generated at 2022-06-22 12:04:33.114926
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from units.compat import unittest

    from ansible.plugins.lookup.template import LookupModule
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    class TestTemplar(object):
        class TemplarEnvironment(object):
            def __init__(self, variables):
                self.variables = variables

        def copy_with_new_env(self, environment_class=None):
            if environment_class is None:
                environment_class = self.__class__.TemplarEnvironment
            return self.__class__(environment_class(self.variables))

        def __init__(self, variables):
            self.variables = variables


# Generated at 2022-06-22 12:04:35.271046
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO(retr0h): Write a test.
    pass

# Generated at 2022-06-22 12:04:46.217175
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six.moves import builtins
    import ansible.parsing.yaml.objects
    import ansible.plugins.lookup.template
    import os

    test_dir = os.path.dirname(os.path.realpath(__file__))

    stdin_values = """---
        - one
        - two
        - three
    """
    environ_values = {'ANSIBLE_JINJA2_NATIVE': 'false'}
    search_path = [test_dir]
    def mock_get_file_contents(path):
        return b'{{ lookup("stdin") | join("_") }}', True

# Generated at 2022-06-22 12:04:56.237024
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    #Test for correct data handling in case of a defined search_path
    lookup_file = "./abc"
    search_paths = ["./", "./test/test_lookup_plugins/templates"]

    # mocking the variables and template file
    variables = dict(
        ansible_search_path = search_paths,
        template_path = "./test/test_lookup_plugins/templates/abc"
    )

    b_result = b'foo'

    # mocking the _get_file_contents method of the module_utils.basic.AnsibleLoader class
    AnsibleLoader._get_file_contents = lambda self, path, decrypt=False: (b_result, False)

    # call the method
    lookup_module = LookupModule()

# Generated at 2022-06-22 12:05:07.960373
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    class MockTemplar(object):

        def __init__(self):
            self.variable_start_string = "{{ "
            self.variable_end_string = " }}"
            self.comment_start_string = "{{ "
            self.comment_end_string = " }}"
            self.searchpath = []

        def copy_with_new_env(self, environment_class):
            return self

        def set_temporary_context(self, variable_start_string, variable_end_string, comment_start_string, comment_end_string, available_variables, searchpath):
            self.variable_start_string = variable_start_string
            self.variable_end_string = variable_end_string
            self.comment_start_string = comment_start_string
            self.comment_end_string = comment

# Generated at 2022-06-22 12:05:09.326190
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass


# Generated at 2022-06-22 12:05:15.644853
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    results = lookup.run([to_bytes(u'../../../utils/jinja2/tests/test_data/test_dict.j2')],
                         dict(foo='bar'))
    assert isinstance(results[0], str)
    assert "foo: 'bar'" in results

# Generated at 2022-06-22 12:05:19.652617
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # params returns [term, variables, kwargs]
    params = LookupModule.run_params
    assert params['terms'] == './examples/test.j2'
    assert params['variables'] == dict(test_var='test')
    assert params['kwargs'] == dict()

# Generated at 2022-06-22 12:05:30.950632
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit tests for the method run.
    """
    import unittest.mock as mock
    args      = 'terms'
    options   = {'convert_data': True, 'ignore_errors': True}
    terms     = ['foo', 'bar']
    variables = {'foo': 'bar'}
    LookupModule.run = mock.MagicMock(return_value='bar')
    result = LookupModule(loader=None, templar=None, variables=None).run(terms, variables, **options)
    LookupModule.run.assert_called_once_with(args, variables, **options)
    assert result == 'bar'

# Generated at 2022-06-22 12:05:58.000553
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test the lookup using a regular template
    term_list1 = [
        './some_template.j2',
        './some_other_template.j2'
    ]
    lookup_mod1 = LookupModule()
    assert lookup_mod1.run(term_list1, variables=None, ** {}) == 'Test Template'

    # test the lookup using an empty string as template
    term_list2 = [
        ''
    ]
    lookup_mod2 = LookupModule()
    assert lookup_mod2.run(term_list2, variables=None, ** {}) == ''

# Generated at 2022-06-22 12:06:08.448351
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    class FakeLookupModule(LookupBase):
        def __init__(self):
            pass

        def run(self, terms, variables, **kwargs):
            return terms

        def error(self, msg):
            raise AnsibleError(msg)

    class FakeLoader(object):
        def _get_file_contents(self, path):
            if path == './some_template.j2':
                return 'some template text', False
            elif path == './some_template_with_context.j2':
                return 'some template text with {{ my_var }} variable', False
            else:
                raise AnsibleError("the template file %s could not be found for the lookup" % path)

    lookup_module = LookupModule()
    lookup_module_fake = FakeLookupModule()
    loader = FakeLoader()


# Generated at 2022-06-22 12:06:18.996898
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.template import Templar

    # Create a templating object
    templar = Templar(loader=None)

    # Create a lookup object
    lookup_object = LookupModule()

    # Add loader to lookup object
    lookup_object._loader = DictDataLoader({})

    # Add templating object to lookup object
    lookup_object._templar = templar

    # Add search path to lookup object
    lookup_object._searchpath = list()

    # Create variables
    variables = dict()

    # Create some test data
    test_data = '{{ hello }} world'

    # Create term
    term = 'test.j2'

    # Create vars
    vars = {'hello': 'wonderful',
            'ansible_search_path': ['.']}

    # Run method run of lookup object

# Generated at 2022-06-22 12:06:29.921132
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup import LookupModule
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six.moves import builtins
    from ansible.module_utils.six.moves import cStringIO as StringIO
    from ansible.galaxy.api import GalaxyAPI
    import sys

    galaxy_api = GalaxyAPI(url='https://galaxy.ansible.com', validate_certs=False, timeout=5)
    galaxy_api.force_deprecated = True
    galaxy_api.collection_branches = {
        'foo.baz': 'master',
    }


# Generated at 2022-06-22 12:06:41.785545
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible.errors import AnsibleError
    from ansible.template import generate_ansible_template_vars, AnsibleEnvironment
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.utils.display import Display
    from ansible.parsing.vault import VaultLib
    from ansible.template import Templar
    from ansible.utils.native_jinja import NativeJinjaText

    display = Display()


# Generated at 2022-06-22 12:06:47.630924
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup = LookupModule()
    lookup.set_loader({})

    # test invalid name_type
    terms = []
    for i in range(10):
        terms.append({'invalid': 'type'})
    result = lookup.run(terms=terms, variables={})

    # test invalid path types
    terms = []
    for i in range(10):
        terms.append({'path': 123})
    result = lookup.run(terms=terms, variables={})

# Generated at 2022-06-22 12:06:59.347439
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import unittest
    import sys
    import os
    import traceback
    import tempfile
    import shutil
    import json

    import ansible.errors
    import ansible.module_utils.six.moves.configparser as configparser
    import ansible.module_utils.six.moves.xmlrpc_client as xmlrpc_client

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.plugins.callback import CallbackBase


    class TestCallbackModule(CallbackBase):

        CALLBACK_VERSION = 2.0
        CALLBACK_TYPE = 'stdout'
        CALLBACK_NAME = 'junit'


# Generated at 2022-06-22 12:07:11.107488
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # setup dict of test parameters
    test_input = dict()

    # first test
    # this test uses the template "./lookup_plugins/test_templates/testfile1.test1"
    # which does not contain any jinja2 variables
    # so it just returns the same string
    test_input[0] = dict()
    test_input[0]['terms'] = ['./lookup_plugins/test_templates/testfile1.test1']
    test_input[0]['variables'] = {'var1': 'test_var1_string'}
    test_input[0]['expected_ret'] = ["Test string"]

    # second test
    # this test uses the template "./lookup_plugins/test_templates/testfile2.test2"
    # which contains two jinja

# Generated at 2022-06-22 12:07:11.984951
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    assert True == isinstance(lookup_module, LookupBase)

# Generated at 2022-06-22 12:07:20.873422
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit test for method run of class LookupModule
    """
    from ansible.module_utils import basic

    dummy_display = basic.AnsibleModule(
        argument_spec = dict()
    )

    # initialize needed objects
    terms = [
        '../test_lookup_plugins/test_template.j2'
    ]

    variables = {
        'inventory_hostname': 'dummy_hostname',
    }

    lookup_obj = LookupModule(dummy_display)
    # do testing
    result = lookup_obj.run(terms, variables, convert_data=False)
    # verify testing
    expected_result = [
        "Hello, I am dummy_hostname\n"
    ]
    assert result == expected_result

# Generated at 2022-06-22 12:08:11.093697
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

#     lookup_module = LookupModule()
    variable_manager = VariableManager()
    loader = DataLoader()

    # Test case 1: terms is not a list.  This should raise an AnsibleError
    (template_vars,
    variable_start_string,
    variable_end_string,
    comment_start_string,
    comment_end_string,
    convert_data) = ({}, '{{', '}}', '{#', '#}', False)
    search_path = ('/home/abcd/ansible_sample_project/lookup_plugins/',)
    terms = 'samplefile.j2'
    #lookup_module.set_options(var_options=template_v

# Generated at 2022-06-22 12:08:17.409223
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module_obj = \
        LookupModule(loader=None, variable_manager=None, templar=None)
    
    #test case1
    terms = 'test.xml'
    variables = {
        'test.xml': 'name.xml'
    }
    res = lookup_module_obj.run(terms, variables, {})
    assert res[0] == 'name.xml', "Error occured"

# Generated at 2022-06-22 12:08:29.589583
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Initializing variables
    kwargs = {}
    kwargs['variable_start_string'] = 'var_start'
    kwargs['variable_end_string'] = 'var_end'
    kwargs['comment_start_string'] = 'comment_start'
    kwargs['comment_end_string'] = 'comment_end'
    term1 = 'test1'
    term2 = 'test2'
    terms = [term1, term2]
    variables = {}
    variables['ansible_search_path'] = ['path1', 'path2']
    loader_mock = MockLoader()
    templar_mock = MockTemplar()
    # Initializing class
    lookup_module_ins = LookupModule()
    lookup_module_ins._loader = loader_mock
    lookup_module

# Generated at 2022-06-22 12:08:38.896650
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()
    assert lookup_plugin.run(['path/to/file'], {'ansible_search_path':[], 'template_vars':{'foo':'bar'}}) == []
    assert isinstance(lookup_plugin.run(['path/to/file'], {'ansible_search_path':[], 'template_vars':{'foo':'bar'}}), list)
    assert lookup_plugin.run(['path/to/file'], {'ansible_search_path':[], 'template_vars':{'foo':'bar'}}) == []

# Generated at 2022-06-22 12:08:48.825809
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import b
    from ansible.module_utils.six.moves import builtins
    from ansible.template import AnsibleTemplate
    from ansible.utils.unicode import to_bytes

    class Options(object):

        __slots__ = ('__dict__')

        def __init__(self, **entries):
            self.__dict__.update(entries)

    class VarsModule(object):

        def __init__(self):
            self.params = {'var1': 'test1', 'var2': ['test2', 'test3']}

    module = VarsModule()

# Generated at 2022-06-22 12:09:00.523710
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    assert lookup_module.run([], {}) == []
    assert lookup_module.run(["../examples/template.j2", "../examples/template_with_precision.j2"], {}) == \
        [u'hello world\n', u'45.67891\n']
    assert lookup_module.run(["../examples/template.j2", "../examples/template_with_precision.j2"],
                                 {u'data': u'hello world'}) == \
        [u'hello world\n', u'45.67891\n']

# Generated at 2022-06-22 12:09:04.946219
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    import sys
    print(sys.modules.keys())
    if 'test_template' in sys.modules.keys():
        raise Exception("Found it")
    module.run({'test_template': '{{ foo }}'}, {'foo': 'bar'})

# Generated at 2022-06-22 12:09:15.458328
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Mock the class variable _get_file_contents from AnsibleFileModuleMixin
    # to test the method run of class LookupModule
    from ansible.utils.file_module_loader import AnsibleFileModuleLoader
    # noinspection PyUnresolvedReferences
    LookupModule._loader = AnsibleFileModuleLoader()

    # Get the class variable _loader from AnsibleFileModuleMixin
    # to set the mock _get_file_contents
    # noinspection PyUnresolvedReferences
    loader = LookupModule._loader
    loader._get_file_contents = lambda a, b: (b'foo bar', True)

    lm = LookupModule()
    res = lm.run(('/some/path'), {}, convert_data=False)
    assert res == ['foo bar']


# Generated at 2022-06-22 12:09:22.786551
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    test_terms = [
        "test.j2",
        "test2.j2"
    ]
    test_variables = {
        "test": "TEST"
    }
    # Simulate the place where Ansible would normally look for templates - the test directory of the ansible project
    lookup_module._loader._basedir = os.path.join(os.path.dirname(os.path.realpath(__file__)), ".." , "..")

    lookup_module.set_options(var_options=test_variables, direct=None)
    ret = lookup_module.run(terms=test_terms, variables=test_variables)

# Generated at 2022-06-22 12:09:58.970228
# Unit test for method run of class LookupModule