

# Generated at 2022-06-22 12:01:17.183056
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    display = Display()

    ####################################################################
    # Test with default settings with jinja2_native=False to check an
    # empty file won't raise an exception
    ####################################################################
    class TestLookupModule(LookupModule):
        def __init__(self):
            pass
        def _get_file_contents(self, path):
            class A():
                def __init__(self):
                    pass
                def __repr__(self):
                    return '<A>'
            return [A(), True]
        def _templar(self):
            class B():
                def __init__(self, a, b):
                    pass
                def template(self, content, preserve_trailing_newlines, convert_data, escape_backslashes):
                    return '<{}>'.format(content)

# Generated at 2022-06-22 12:01:29.860059
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Setup an empty envars
    envars = {}

    # Setup a simple templar
    templar = DummyTemplar(envars)

    # Setup a simple display
    display = DummyDisplay()

    # Setup a simple loader
    loader = DummyLoader()

    # Setup a simple terms
    terms = "test"

    # Setup a simple variables
    variables = {}

    # Setup a simple kwargs
    kwargs = {"convert_data": False, "comment_end_string": ']]', "comment_start_string": '[[', "template_vars": {}}

    # Create a LookupModule object
    look = LookupModule(loader=loader, templar=templar, display=display)

    # Test a simple lookup
    look._options = kwargs
    assert look.run

# Generated at 2022-06-22 12:01:30.505350
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-22 12:01:38.812391
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    def mock_find_file_in_search_path():
        pass
    
    def mock_get_file_contents(filename):
        with open(filename) as file_:
            template_data = file_.read()
            return (template_data, True)

    # Bare LookupModule
    lookup_module = LookupModule()

    # LookupModule with mocks for needed methods
    lookup_module._loader.get_file_contents = mock_get_file_contents
    lookup_module.find_file_in_search_path = mock_find_file_in_search_path

    # variables sent to run
    variables = {
        'ansible_search_path': ['/dummy/'],
    }

    # terms sent to run
    terms = ['dummy.j2']

    # Get result of

# Generated at 2022-06-22 12:01:51.472791
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit test for module ansible.plugins.lookup.template.LookupModule.run()
    """
    from collections import namedtuple

    from ansible.errors import AnsibleError
    from ansible.module_utils._text import to_bytes
    from ansible.template import generate_ansible_template_vars, AnsibleEnvironment, USE_JINJA2_NATIVE
    from ansible.utils.display import Display
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    if USE_JINJA2_NATIVE:
        from ansible.utils.native_jinja import NativeJinjaText

    # Mock class
    class MockTemplar:

        def __init__(self, templar_env, templar_ctx):
            self.templar_env = templar

# Generated at 2022-06-22 12:02:03.485087
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    # Parameterized unit tests
    # Each element of the following list is a set of arguments for the
    # test method, and the relative expected output.
    # The arguments for the call to the _run_lookup method are:
    # args = (terms, variables=None, **kwargs)
    # In this test method, we assume that terms is a list of strings;
    # variables is a dictionary; kwargs is a dictionary

# Generated at 2022-06-22 12:02:14.539413
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import StringIO
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext

    display_out = StringIO()
    display_err = StringIO()
    display.verbosity = 3
    display.stdout = display_out
    display.stderr = display_err

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = None
    play_context = PlayContext(variable_manager=variable_manager, loader=loader, inventory=inventory)

    term = ['./tests/templates/jinja2_template.j2']
    lookup_plugin = LookupModule()

    # create a temporary directory to put the test files into
    import temp

# Generated at 2022-06-22 12:02:26.417442
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Testcase initially taken from ansible/test/units/plugins/lookup/test_template.py
    # This tests the variable_start_string and variable_end_string options of lookup_plugin

    from ansible.module_utils.six import StringIO
    from ansible.template import Templar

    # Test with variable_start_string and variable_end_string provided for the lookup_plugin
    test_template = StringIO(u'[% ansible_hostname %]')
    templar = Templar(loader=None, variables={})
    lookup_plugin = LookupModule()



# Generated at 2022-06-22 12:02:38.004726
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()

    ret = module.run(['some_template_file.j2'], dict(), _connection='local', convert_data=True, variable_start_string='{{', variable_end_string='}}', jinja2_native=True, template_vars={'color': 'green'}, comment_start_string='[%', comment_end_string='%]')
    assert ret == ['some_template_file.j2\n']
    ret = module.run(['some_template_file.j2'], dict(), _connection='local', convert_data=True, variable_start_string='[%', variable_end_string='%]', jinja2_native=True, template_vars={'color': 'green'}, comment_start_string='{{', comment_end_string='}}')

# Generated at 2022-06-22 12:02:46.032072
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import tempfile

    temp_file_content="Hello World"

    lookup = LookupModule()

    # create a temporary file
    tf = tempfile.NamedTemporaryFile(delete=False)
    with tf as fd:
        fd.write(to_bytes(temp_file_content + "\n"))

    terms = [tf.name]
    variables = {}

    res = lookup.run(terms, variables)
    assert res[0].rstrip() == temp_file_content
    assert res[0] == to_text(to_bytes(temp_file_content + "\n"))

# Generated at 2022-06-22 12:03:03.788880
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Unit tests use this class to mock the _loader of real LookupModule
    class MockLoader:

        def _get_file_contents(self, path):
            if path == "./a.txt":
                return to_bytes("this is a test"), False
            raise AnsibleError("the template file %s could not be found for the lookup" % path)

    class MockTemplar:

        def __init__(self):
            self.new_vars = {}
            self.all_vars = {}
            self.template_data = ""

        def set_available_variables(self, variables):
            self.all_vars = variables

        def template(self, template_data, preserve_trailing_newlines=False,
                     convert_data=False, escape_backslashes=False):
            self.template_data

# Generated at 2022-06-22 12:03:15.471872
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create an instance of LookupModule
    lookup_plugin = LookupModule()

    # Make the templar available
    lookup_plugin._templar = DummyTemplar()

    # Make the loader available
    lookup_plugin._loader = DummyLoader()

    # Make the display available
    lookup_plugin._display = display

    # Create the search path for the expected file to be found
    searchpath = [os.path.join(os.path.dirname(__file__), "files")]

    # Define the variables available for the template
    variables = dict(nested1=dict(nested2=False))

    # Set of global options used by the lookup/templar
    lookup_plugin.set_options(
        var_options=variables,
        direct={'jinja2_native': False}
    )

# Generated at 2022-06-22 12:03:21.759506
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import copy
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.vars.manager import VariableManager

    from ansible.template import ANSIBLE_VAULT_IDENTITY
    from . import lookup_dir, lookup_config_dir
    lu = LookupModule()


# Generated at 2022-06-22 12:03:29.250582
# Unit test for method run of class LookupModule

# Generated at 2022-06-22 12:03:40.550020
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # testing the LOOKUP_OPTIONS (e.g. convert_data)
    lookup = LookupModule()
    assert lookup.run(terms=['sample-template.j2'], variables={'ansible_search_path': ['/some/path/on/disk']}, convert_data=False)[0] == '- name: from templated file\n  debug: msg={{ a_variable_with_dashes }}\n\n- name: from second templated file\n  debug: msg={{ a_variable_with_dashes }}\n'

# Generated at 2022-06-22 12:03:51.746386
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.template import Templar
    from ansible.vars.unsafe_proxy import UnsafeProxy
    import sys
    import jinja2
    import jinja2.exceptions

    # mock _templar class
    fake_env_class = object()
    fake_unsafe = UnsafeProxy({"a": {"b": 900}})

    class FakeTemplar(object):
        # set class variable values
        environment_class = fake_env_class
        template_class = jinja2.Template
        native_JinjaText = USE_JINJA2_NATIVE

        def set_common_environment(self, env):
            self.env = env
            assert self.env.environment_class == fake_env_class

        def set_available_variables(self, vars):
            self.v

# Generated at 2022-06-22 12:04:03.166057
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Creating a mock object of class LookupBase
    lu_object = LookupModule()
    # lu_object.set_options is a method of LookupBase, setting this method to a mock object
    lu_object.set_options = Mock(return_value=None)
    # Creating a mock object of class AnsibleEnvironment
    ansible_environment = Mock()
    # Creating a mock object of class NativeJinjaText
    nativeJinjaText = Mock()
    # Overwriting get_option method of LookupBase class
    lu_object.get_option = Mock(side_effect=[False, ansible_environment])

    # Creating mock objects of datatype dictionary

# Generated at 2022-06-22 12:04:12.263381
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a class object
    y = LookupModule()

    # Create a dict object
    dict_object = {'a': '1', 'b': '2', 'c': '3', 'd': '4'}

    # The test terms list
    terms = ['./test.j2']

    # The test variables dictionary
    variables = {'a': '{{a}}', 'b': '{{b}}', 'c': '{{c}}', 'd': '{{d}}'}

    # Run the actual test
    ret = y.run(terms, variables)

    # Check if result is as expected
    assert ret == [u'a=1 b=2 c=3 d=4']

    # Create a dict object

# Generated at 2022-06-22 12:04:21.226422
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Test run method"""

    # initialize the class and it's member vars
    import ansible.plugins.loader as plug_loader
    lookup_plugin = plug_loader.get('lookup', 'template')
    import ansible.parsing.dataloader as data_loader
    import ansible.vars as var
    import ansible.utils.display as display

    # init member vars
    lookup_plugin._loader = data_loader.DataLoader()
    lookup_plugin._templar = var.VariableManager()
    lookup_plugin._templar.set_available_variables({
        "ansible_search_path": [
            "/root/test/templates",
            "/root/test/playbooks",
        ]
    })

    # test run method

# Generated at 2022-06-22 12:04:31.973451
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    opts = {'convert_data': False, 'template_vars': {}}
    lookup_module._templar = AnsibleEnvironment()
    lookup_module._templar.loader = DummyLoader()
    lookup_module._templar.loader.basedir = './'

    result = lookup_module.run('../../lookup_plugins/template/test.j2', {}, **opts)
    assert result == to_bytes('test')

    opts["template_vars"] = {"testvar": "testvar"}
    result = lookup_module.run('../../lookup_plugins/template/test_vars.j2', {}, **opts)
    assert result == to_bytes('testvar')


# Generated at 2022-06-22 12:04:53.099895
# Unit test for method run of class LookupModule

# Generated at 2022-06-22 12:05:01.387906
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    terms = ['test1.j2', 'test2.j2']
    variables = {
        'somevar': 'somevalue',
    }

    lookup_module = LookupModule()
    lookup_module._templar = Templar(loader=loader, variables=variable_manager)
    lookup_module.set_options(var_options=variables)
    results = lookup_module.run(terms, variables)
    assert len(results) == 2

# Generated at 2022-06-22 12:05:02.454989
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert True


# Generated at 2022-06-22 12:05:04.871616
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # It is not possible to test LookupModule.run method because it uses Ansible's
    # PluginLoader which uses the global config object.
    pass

# Generated at 2022-06-22 12:05:05.516039
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-22 12:05:12.283081
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Unit test for method run of class LookupModule"""
    # pylint: disable=import-error
    from ansible.module_utils.six import StringIO
    # pylint: enable=import-error
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    PARAMS = {
        'variable_start_string': u'{{',
        'variable_end_string': u'}}',
        'comment_start_string': u'#',
        'comment_end_string': u'',
        'convert_data': False,
        'jinja2_native': True,
    }

    PARSED_TEMPLATE = u"This is a test: {{ var1 }}\n"

# Generated at 2022-06-22 12:05:15.983383
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    args = (
        ('lookup_plugin.py',),
        {
            'convert_data': False,
            'template_vars': {},
            'jinja2_native': False,
            'variable_start_string': '{{',
            'variable_end_string': '}}',
            'comment_start_string': '',
            'comment_end_string': '',
        },
    )
    kwargs = {'_terms': ['lookup_plugin.py'], 'variables': {'__ansible_lookup_plugin__': 'template'}}
    lookup_mod = LookupModule()
    result = lookup_mod.run(*args, **kwargs)
    assert result == [b"#!/usr/bin/python\n"]

# Unit tests for global variable USE_JINJA2

# Generated at 2022-06-22 12:05:28.540519
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test case 1
    lookup_module = LookupModule()
    lookup_module._loader = 'fake_loader'
    lookup_module._templar = 'fake_templar'
    ret = lookup_module.run(['./some_template.j2'], {'variable_start_string': '{{',
                                                     'variable_end_string': '}}'})
    assert ret == ['{{lookup(\'template\', \'./some_template.j2\')}}']
    # test case 2
    ret = lookup_module.run(['./some_template.j2'], {'variable_start_string': '[%',
                                                     'variable_end_string': '%]'})
    assert ret == ['[% lookup(\'template\', \'./some_template.j2\') %]']

# Generated at 2022-06-22 12:05:38.260159
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible import __file__ as anslib_file
    from ansible.constants import DEFAULT_VAULT_PASSWORD_FILE
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

# Generated at 2022-06-22 12:05:47.438048
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    # Test run method using a lookup_template_vars dictionary with two entries
    terms = [b'data/test_template.yaml']
    lookup_template_vars = {
        'test1': 'testvalue',
        'test2': {'test3': 'testvalue3', 'test4': 'testvalue4'}
    }
    lookup_file = lookup_module.run(terms, variables={}, template_vars=lookup_template_vars)
    assert len(lookup_file) == 1
    assert lookup_file[0] == "testvalue\ntestvalue4\n"

    # Test run method when a term exists in the lookup_template_vars dictionary
    terms = [b'data/test_template_with_dictionary.yaml']
    lookup_

# Generated at 2022-06-22 12:06:16.788974
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    display = Display()
    display.verbosity = 4
    test_template_dir = './test/templates'
    test_template_path = './test/templates/hello_world.j2'
    test_template_str = '{{ ansible_ssh_host }}'
    test_template_vars = {'ansible_ssh_host': '127.0.0.1'}

    l = LookupModule()

    result = l.run([test_template_path], variables=test_template_vars)
    assert result[0] == '127.0.0.1'

    # Test that extra variables are passed to the templating engine, making an
    # extra variable available in the template

# Generated at 2022-06-22 12:06:24.727106
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.errors import AnsibleError
    from ansible.plugins.loader import get_loader
    from ansible.template import Templar
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.vars.hostvars import HostVars

    terms = [
        './some_template.j2'
    ]

    loader = get_loader('load_plugins')

    templar = Templar(loader=loader, variables=dict())

    lookupModule = LookupModule(templar, loader=loader)

    # Unit test for method run with success
    ret = lookupModule.run(terms, dict(), convert_data=True, variable_start_string='{{', variable_end_string='}}')
    assert ret == [to_text(terms[0])]

    # Unit test for method run

# Generated at 2022-06-22 12:06:30.497954
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    lookup._load_plugins = lambda *args: None
    lookup._templar = object()
    lookup._loader = object()
    lookup.set_options({})
    lookup_options = {}
    def find_file_in_search_path(variables, directory, file):
      del variables, directory, file  # Unused
      return None
    lookup.find_file_in_search_path = find_file_in_search_path

    # Test default args
    assert lookup.run(['./sometemplate.j2'], lookup_options)
    # Test jinja2_native=True
    assert lookup.run(['./sometemplate.j2'], lookup_options, jinja2_native=True)
    # Test convert_data=True
    assert lookup.run

# Generated at 2022-06-22 12:06:42.320127
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.template import Templar

    # Create the arguments for the call to the run method
    # test
    # _terms = [u'mytemplate.j2']
    # convert_data = True
    # variable_start_string = '{{'
    # variable_end_string = '}}'
    # jinja2_native = False
    # lookup_template_vars = {'test':'test'}
    # output_encoding = 'utf-8'
    # comment_start_string = '{#'
    # comment_end_string = '#}'

    # Declare the variables used in the test
    content = "# test"
    _terms = [u'mytemplate.j2']
    convert_data = True
   

# Generated at 2022-06-22 12:06:48.685003
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    input_variables = {
        'test_variable_1': 'A',
        'test_variable_2': 'B',
        'test_variable_3': 'C',
    }
    input_terms = [
        'test.j2',
        'test2.j2'
    ]
    input_kwargs = {
        'variable_start_string': '<<',
        'variable_end_string': '>>',
        'comment_start_string': '#',
        'comment_end_string': '#',
        'template_vars': {
            'input_var_1': 'A',
            'input_var_2': 'B',
            'input_var_3': 'C',
        },
    }

# Generated at 2022-06-22 12:06:56.578339
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Arrange
    args = ['templatename']
    variables = {'foo': 'bar'}
    kwargs = {'variable_start_string': '{{', 'variable_end_string': '}}'}
    
    lookup_module = LookupModule()
    lookup_module.set_loader(None)
    lookup_module.set_templar(None)

    # Act
    lookup_module.run(args, variables, **kwargs)

    # Assert


# Generated at 2022-06-22 12:07:07.758023
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Creating mock_loader
    import pytest
    loader_mock = pytest.Mock()
    loader_mock.get_basedir.return_value = "/home/test"
    loader_mock.path_dwim.return_value = "/home/test/test.yml"
    loader_mock.path_dwim_relative.return_value = "relative/path/to/file.txt"

    # Creating mock_display
    display_mock = pytest.Mock()

    # Creating mock_env
    env_mock = pytest.Mock()
    env_mock.get_options.return_value = {'connection': 'local'}

    # Creating mock_variable_manager
    vars_mock = pytest.Mock()
    vars_mock.get_v

# Generated at 2022-06-22 12:07:18.243421
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # create an instance of LookupModule to be able to run method run
    templ = LookupModule()

    # Use of method run
    # set of variables
    variables_list = [ 'var1', 'var2' ]
    variables = { "var1": "var1", "var2": "var2" }
    # set of terms
    terms = [ '/path/to/file' ]
    # set of options
    options = { "convert_data": None, "template_vars": variables,
                "jinja2_native": False, "variable_start_string": None,
                "variable_end_string": None, "comment_start_string": None,
                "comment_end_string": None }

    # call method run with the set of terms, variables and options

# Generated at 2022-06-22 12:07:19.197003
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()

# Generated at 2022-06-22 12:07:23.598128
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    lookup.set_loader({'_get_file_contents': lambda x,y: ('This is a template', 'blah')})
    assert lookup.run(terms=['tmpl.j2'], variables={}, convert_data=True) == ['This is a template']

# Generated at 2022-06-22 12:08:12.872092
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Check the result when convert_data is True and jinja2_native is False
    # which is the default behavior.
    # This is a test for the case where the template contains YAML.
    lookup_mod = LookupModule()
    lookup_mod.set_loader({'_load_file': lambda x, y: (to_bytes('{"foo": [123, 456]}'), False)})
    ret = lookup_mod.run(['data.yml'], {}, convert_data=True, jinja2_native=False)
    assert ret == [{'foo': [123, 456]}] # datatype

    # Check the result when convert_data is True and jinja2_native is True
    # which is the case where the template contains YAML.
    # This is a test for the case where the

# Generated at 2022-06-22 12:08:24.142225
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.display import Display
    from ansible.template import generate_ansible_template_vars

    display = Display()
    display.verbosity = 4
    display.deprecated("check", "true", version="2.4")
    display.deprecated("check", "true", version="2.4")
    display.deprecated("check", "false", version="2.4", removed=False)

    class obj:
        pass

    x = obj()
    x.templar = obj()
    x.set_options = obj()
    x.get_option = obj()
    x.find_file_in_search_path = obj()
    x.find_file_in_search_path.return_value = "/var/lib/awx/projects/default/project.yaml"
    x._loader

# Generated at 2022-06-22 12:08:36.466561
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Tests LookupModule.run to make sure that jinja2_native is respected.
    """
    import jinja2
    # Use a template that would fail without jinja2 native
    template_data = "{% set testarray = [1,2,3] %}{{ testarray|to_json }}"
    terms = [template_data]
    variables = {}
    # The lookup should fail if jinja2 native is not used
    test_lookup = LookupModule()
    output = test_lookup.run(terms, variables, convert_data=False, jinja2_native=False)
    assert len(output) == 0
    # The lookup should succeed if jinja2 native is used
    test_lookup = LookupModule()

# Generated at 2022-06-22 12:08:43.169972
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Setup some dummy variables
    class Namespace:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)
    terms = ['foo.j2']
    variables = Namespace(template_data='foo: {{ a }}')
    # Call the function and check the result
    res = LookupModule(None, None).run(terms=terms, variables=variables, convert_data=False)[0]
    # Check that the result is correct
    assert res == 'foo: {{ a }}'

# Generated at 2022-06-22 12:08:55.137331
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.errors import AnsibleError, AnsibleFileNotFound
    from ansible.template import generate_ansible_template_vars
    from ansible.parsing.plugin_docs.module_docs import (
        _load_docstrings,
        _get_action_docs,
        _get_module_metadata,
    )
    from ansible.module_utils._text import to_bytes, to_text
    import six

    display = Display()

    lookup_module = LookupModule()
    lookup_module.set_loader({})
    lookup_module.set_basedir(six.u('/home/ansible/playbooks'))

    def _get_file_contents(self, path, enable_mako=False):
        if enable_mako:
            return b'{{ ansible_system }}', True

# Generated at 2022-06-22 12:09:07.098279
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # check if the lookup module is working
    lookup_module = LookupModule()
    lookup_module._templar = None
    lookup_module._loader = None
    lookup_module.set_options(var_options=None, direct=None)
    lookup_module.run(terms=["template_data.j2"], variables=dict())
    # check if the lookup module is working when USE_JINJA2_NATIVE is set to true and option jinja2_native is set to True
    lookup_module.set_options(var_options=None, direct={"jinja2_native": True})
    lookup_module.run(terms=["template_data.j2"], variables=dict())
    # check if the lookup module is working when USE_JINJA2_NATIVE is set to true and option jinja2_native is

# Generated at 2022-06-22 12:09:18.365414
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.vars import combine_vars

    module = LookupModule()
    # use v2_playbook_item for top level vars.
    # modules do not have access to the inventory so ansible_vars are not available

# Generated at 2022-06-22 12:09:26.404729
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    templ = LookupModule()

    # Check the case when one of the template files is missing
    with pytest.raises(AnsibleError):
        templ.run(['absent_file.j2'], dict())

    # Check the case when both of the template files are present
    ret = templ.run(['present_file_1.j2', 'present_file_2.j2'], dict())
    assert len(ret) == 2
    assert all([ret[0] == ret[1]])



# Generated at 2022-06-22 12:09:36.850926
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch, MagicMock

    test_loader = "ansible.plugins.lookup.template.LookupBase._loader"
    test_find_file_in_search_path = "ansible.plugins.lookup.template.LookupBase.find_file_in_search_path"

    test_term = "test_template.j2"
    test_lookup_file = "/tmp/test_template.j2"

    test_template_data = "TestTemplate"

    class OptionsModule():
        class __ansible__():
            convert_data = False
            template_vars = {}
            jinja2_native = False

    class Foo:
        def __init__(self, **kwargs):
            self

# Generated at 2022-06-22 12:09:39.959278
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Run the method
    actual = LookupModule.run({"terms": "", "variables": "", "kwargs": ""})
    expected = ""
    assert actual == expected



# Generated at 2022-06-22 12:11:01.359898
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass


# Generated at 2022-06-22 12:11:08.054648
# Unit test for method run of class LookupModule
def test_LookupModule_run():
  print("Testing method run of class LookupModule")

  import types
  import inspect
  import os
  import pytest
  from jinja2.environment import Environment

  from ansible.module_utils._text import to_bytes, to_text

  from ansible.template import generate_ansible_template_vars, USE_JINJA2_NATIVE
  if USE_JINJA2_NATIVE:
    from ansible.utils.native_jinja import NativeJinjaText

  from ansible.module_utils.six import PY3
  from ansible.parsing.vault import VaultAwareParameterLoader

  # FIXME: these tests should not rely on the filesystem
  basedir = os.path.join(os.path.dirname(__file__), '..', '..')
  # FIXME: make