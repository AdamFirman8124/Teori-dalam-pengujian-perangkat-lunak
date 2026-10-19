

# Generated at 2022-06-22 12:01:15.621195
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import lookup_loader, module_loader

    # Create some fields for Mock classes
    mock_loader_class = type('MockLoaderClass', (object,), {})
    mock_loader_class.basedir = 'fake_loader_basedir'
    mock_loader_class.path_sep = 'fake_loader_path_sep'
    mock_loader_class.get_basedir = lambda self, name: 'fake_get_basedir_path'

    # Create Mock classes

# Generated at 2022-06-22 12:01:28.090215
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from collections import namedtuple

    # Create the object under test
    look = LookupModule()

    # Create basic objects for method run to work
    terms = ['some_template.j2']
    vars = {
        'var1': 'VAR1_VALUE',
        'var2': 'VAR2_VALUE',
        'list_var1': ['list_var1_value1', 'list_var1_value2'],
        'list_var2': ['list_var2_value1', 'list_var2_value2', 'list_var2_value3'],
    }

# Generated at 2022-06-22 12:01:39.451891
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    terms = ['./plugins/lookup/test/data/samples/template_vars.j2']
    variables = {
        'var': 'world',
        'empty': '',
        'n': None,
        'list': ['a', 'b', 'c'],
        'dict': {'a': 'b', 'c': 'd'}
    }
    template_vars = {
        'answer': 42,
        'list': [1, 2, 3, 4],
        'list_str': 'a,b,c,d'
    }

# Generated at 2022-06-22 12:01:52.001126
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # This test requires a test file with contents:
    #   $ echo "{{ name }}" > /tmp/test.txt
    #   $ echo "{{ age }}" >> /tmp/test.txt
    # Define the variables used in the test.
    lookup_terms = ['/tmp/test.txt']
    lookup_variables = {'name': 'Jane Smith', 'age': 24}
    lookup_options = {'convert_data': True, 'template_vars': {}}
    # Instantiate the test class.
    test_class = LookupModule()
    # Run the method under test.
    test_output = test_class.run(
        lookup_terms,
        lookup_variables,
        **lookup_options
    )
    # Check the output.

# Generated at 2022-06-22 12:02:03.187729
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Without lookpath
    lookup = LookupModule()
    assert not lookup.run(['test.j2'], {})

    # With wrong lookpath
    lookup = LookupModule()
    assert not lookup.run(['test.j2'], {"_ansible_lookup_plugin_paths": ["/wrong/path"]})

    # With good lookpath
    lookup = LookupModule()
    lookup._templar.set_available_variables({"ansible_search_path": ["/ansible/lookup/tests"]})
    assert lookup.run(['test.j2'], {"_ansible_lookup_plugin_paths": ["/ansible/lookup/plugins"]})[0] == "test template content\n"

# Generated at 2022-06-22 12:02:14.265922
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # from ansible.module_utils import basic  # module under test
    from ansible.module_utils.six import PY2, PY3
    from ansible.module_utils.common._collections_compat import Mapping
    lookup = LookupModule()

    # test with invalid arguments

# Generated at 2022-06-22 12:02:19.528927
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    terms = ['fake_term.j2']
    variables = {
        'ansible_search_path': ['search_path_fake_1', 'search_path_fake_2']
    }
    assert module.run(terms, variables) == ['fake_content']

# Generated at 2022-06-22 12:02:31.224464
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.template import Templar

    _terms = './some_template.j2'
    _variables = {'foo': 'bar'}
    _kwargs = {'variable_start_string': '[%',
                'variable_end_string': '%]',
                'comment_start_string': '[#',
                'comment_end_string': '#]'}

    l = LookupModule()
    l.set_loader({'_get_file_contents': lambda x,y: ('some_template.j2', True)})
    l.set_templar(Templar({'_get_file_contents': lambda x,y: ('some_template.j2', True)}))

    # Normal call to run method of LookupModule 

# Generated at 2022-06-22 12:02:40.810150
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # create a fake lookup module
    lookup = LookupModule()
    lookup._templar = FakeTemplar()
    lookup._loader = FakeLoader()
    lookup.set_loader(lookup._loader)

    # create a fake inventory, some arbitrary data in it
    inventory = FakeInventory()
    inventory._vars = {u'ansible_search_path': [u'/home/ansible/playbooks']}

    # create a fake play context, add the fake inventory and templar to it
    play_context = FakePlayContext()
    play_context.vars_manager.set_inventory(inventory)

    # load the play context into the lookup module
    lookup.set_play_context(play_context)

    # create a set of lookup parameters
    terms = [u'./some_template.j2']

# Generated at 2022-06-22 12:02:52.575938
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    paramiko does not play well in the unit tests and there is no need for it in a unit test
    This is a basic unit test for the LookupModule class. If a test is not mocked, it runs against a live file.
    """
    import os
    import pytest
    import sys
    import tempfile

    test_data_dir = tempfile.TemporaryDirectory()
    sys.path.append(test_data_dir.name)

    # Create some dummy test data
    lookupfile = os.path.join(test_data_dir.name, 'test.j2')
    with open(lookupfile, 'wt') as f:
        f.write('testing')

    class DummyVars(object):
        def __init__(self, my_var):
            self.my_var = my_var

    #

# Generated at 2022-06-22 12:03:13.853682
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import mock
    from ansible.config.manager import ConfigManager

    cm = ConfigManager()
    from ansible.utils.display import Display

    #
    # def run(self, terms, variables=None, **kwargs):
    #

    mydisplay = Display()
    my_env = mock.MagicMock()
    my_loader = mock.MagicMock()

    my_loader.path_dwim_relative.return_value = None
    my_loader.get_basedir.return_value = '/some-basedir'

    my_loader.path_dwim_relative.return_value = '/some-dir/some-file.txt'

    my_loader._get_file_contents.return_value = ('some-file-content', True)


# Generated at 2022-06-22 12:03:21.032904
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six.moves import cPickle as pickle

    # Load a pickle of the basic ansible variables
    if PY3:
        with open(os.path.join(os.path.dirname(__file__), to_bytes('../../test/unit/ansible_vars.pkl')), 'rb') as f:
            variables = pickle.load(f, encoding='bytes')
    else:
        with open(os.path.join(os.path.dirname(__file__), to_bytes('../../test/unit/ansible_vars.pkl')), 'rb') as f:
            variables = pickle.load(f)

    # Instanciate class LookupModule
    l = LookupModule

# Generated at 2022-06-22 12:03:21.823779
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert True

# Generated at 2022-06-22 12:03:31.944790
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    ret = LookupModule().run(
        terms=['test/test_templates/foo.j2'],
        variables={
            'bar': 'baz',
            'nested': {
                'a': {
                    'b': {
                        'c': 'd'
                    }
                }
            },
            'inventory_hostname': 'localhost',
            'inventory_hostname_short': 'localhost'
        })

    assert ret[0] == """
{{bar}}
{% if bar == "baz" %}
jinja2-foo
{% endif %}
"""
    assert ret[0] == """
{{bar}}
{% if bar == "baz" %}
jinja2-foo
{% endif %}
"""

# Generated at 2022-06-22 12:03:41.460204
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Calls run method on LookupModule class with arguments terms, variables,
    # etc
    run_args = {
    '_load_name': 'lookup',
    'terms': 'test.txt',
    'variables': {
      'name': 'Zenoss'
    },
    'templates': ''
    }

    run_args['_templar'] = TemplateLookup(loader=DataLoader())

    lookup = LookupModule()
    lookup.run(**run_args)

    if lookup is None:
        print('test_LookupModule_run - FAIL')
    else:
        print('test_LookupModule_run - PASS')

if __name__ == '__main__':
    test_LookupModule_run()

# Generated at 2022-06-22 12:03:53.066142
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create an instance of class LookupModule
    lm = LookupModule()
    # Load the inventory plugin into the "shell" loader of Ansible
    lm._loader.load_plugin('shell')

    # Load the template plugin into the "template" loader of Ansible
    lm._loader.load_plugin('template')

    # Create an instance of the class VariableManager, passing it a "shell" loader
    vm = lm._loader.get('shell', class_only=True)()

    # Declare an arbitrary variable
    vm.set_options({'ANSIBLE_VAR1': 'string_value'})

    # An arbitrary term
    term = "{{ ANSIBLE_VAR2 | default('test') }}"
    # An arbitrary template variables
    template_vars = {'test1': 'test1'}
    #

# Generated at 2022-06-22 12:03:55.877697
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """unit test for method run of class LookupModule"""
    lookup_module = LookupModule()
    assert isinstance(lookup_module, LookupModule)

# Generated at 2022-06-22 12:04:05.800856
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    class MockTemplar(object):
        def __init__(self):
            self.call_count = 0
            self.templated_data = ''

        def copy_with_new_env(self, environment_class=None):
            return self

        def template(self, data, preserve_trailing_newlines=True, escape_backslashes=False,
                     convert_data=False, fail_on_undefined=True):
            self.call_count += 1
            self.templated_data = data
            return self.templated_data


# Generated at 2022-06-22 12:04:08.729638
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    terms = ['var.yml']
    variables = {'some_var': 'foo'}
    assert module.run(terms, variables) == ['foo']

# Generated at 2022-06-22 12:04:15.148308
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module.set_options({'template_vars': {'foo': 'bar'}})
    lookup_module.set_loader({'_get_file_contents': lambda x: ('{{ foo.upper() }}', None)})
    assert lookup_module.run(terms=['fake-lookup-file'], variables={}) == ['BAR']

# Generated at 2022-06-22 12:04:34.868802
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test 1
    import os

    terms = ['./some_template.j2']
    lookup_options = dict()

    from ansible.vars.manager import VariableManager
    variable_manager = VariableManager()
    variable_manager.extra_vars = dict()
    variable_manager.options_vars = dict()

    from ansible.parsing.dataloader import DataLoader
    dl = DataLoader()  # , variable_manager=variable_manager

    from ansible.inventory.manager import InventoryManager
    inv_manager = InventoryManager(loader=dl, sources=['c:/opt/ansible_2.8/inventory'])
    variable_manager = VariableManager(loader=dl, inventory=inv_manager)

    # Borrowed from template module
    environment = 'ansible-2.8'
    jin

# Generated at 2022-06-22 12:04:42.898580
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_result = ''
    lookup_module = LookupModule()

    # Test 1: no term
    try:
        lookup_result = lookup_module.run([], {})
    except:
        pass

    assert lookup_result == [], "Expected [] but got % s" % lookup_result

    # Test 2: term but no search_path
    try:
        lookup_result = lookup_module.run(['/tmp/a.j2'], {})
    except:
        pass

    assert lookup_result == [], "Expected [] but got % s" % lookup_result

# Generated at 2022-06-22 12:04:53.959262
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # init class
    l = LookupModule()

    # set params
    jinja2_native = 'True'
    variable_start_string = '{{'
    variable_end_string = '}}'
    comment_start_string = '{#'
    comment_end_string = '#}'

    # set params
    terms = [
        '/path/to/some/file1.j2',
        '/path/to/some/file2.j2',
        '/path/to/some/file3.j2',
    ]

    # run method
    ret = l.run(terms, variable_start_string, variable_end_string, comment_start_string, comment_end_string)

    # assert
    assert isinstance(ret, list)
    assert len(ret) == 3

# Generated at 2022-06-22 12:05:07.333252
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    def setup_loader_mocks(mocker, args, string_data=None, path_exists=True):
        # Helper function to set up all the mocks for the loader
        m = mocker.patch('ansible.plugins.lookup.template.LookupModule._templar')
        m.copy_with_new_env().template.return_value = string_data
        mocker.patch('ansible.plugins.lookup.template.LookupModule.find_file_in_search_path').return_value = path_exists

    def test_convert_data(mocker):
        # Check that convert_data is respected
        args = {'convert_data': True}
        setup_loader_mocks(mocker, args, string_data='{"key": "value"}')
        m = LookupModule()

# Generated at 2022-06-22 12:05:13.853108
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    templateFile = {'path': "src/ansible/plugins/lookup/template.py", 'mode': 0o6000}
    terms = [templateFile]
    variables = {'ansible_search_path': ['./']}
    module.run(terms, variables)

# Generated at 2022-06-22 12:05:26.296125
# Unit test for method run of class LookupModule

# Generated at 2022-06-22 12:05:37.006905
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class MyTemplar:
        def __init__(self):
            self.b_template_data = b"some data"
            self.res = b"res"

        def copy_with_new_env(self, environment_class):
            return MyTemplar()

        def set_temporary_context(self, **kwargs):
            return MyTemplar()

        def template(self, template_data, preserve_trailing_newlines=True, convert_data=False, escape_backslashes=False):
            assert isinstance(template_data, to_text.__func__)
            return self.res

    class MyLoader:
        def __init__(self):
            self.dirname = os.path.dirname("some_dirname")

# Generated at 2022-06-22 12:05:47.697669
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module._templar._available_variables = {}
    templar = lookup_module._templar
    lookup_module._templar = templar

    # Template file contains two variable {{ ansible_managed }} and {{ variable_passed_in }}.
    # Template variables passed in looks like below:
    # {
    #     "ansible_managed": "test template with variable",
    #     "variable_passed_in": "test template with variable passed in"
    # }
    terms = [
        "test_template.j2",
    ]
    variables = {
        "ansible_managed": "test template with variable",
        "variable_passed_in": "test template with variable passed in",
    }

# Generated at 2022-06-22 12:05:58.449318
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.vault import VaultLib
    from ansible.template import Templar
    from ansible.vars import VariableManager

    variable_manager = VariableManager()

    test = 'test'
    terms = [test]

    variables = variable_manager.get_vars(play=dict(name='test', play_hosts=['test']))
    vault_pass = 'test'
    vault_secrets = [('vault_password', vault_pass)]
    with VaultLib(vault_secrets=vault_secrets).lock():
        templar = Templar(loader=None, variables=variables, vault_secrets=vault_secrets)
        lookup = LookupModule()
        result = lookup.run(terms=terms, variables=variables, templar=templar)

        assert result

# Generated at 2022-06-22 12:06:08.917295
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    "Tests the run method of the LookupModule class"

    # Test using standard jinja2 templating

# Generated at 2022-06-22 12:06:31.487226
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    variables = {}

    def find_file_in_search_path(variables, directory, filename):
        return filename

    lookup_module.find_file_in_search_path = find_file_in_search_path
    lookup_module.set_options(var_options=variables)

    lookup_module.run(
        [
            "test_template.j2"
        ],
        variables,
    )

    assert lookup_module.result is not None

# Generated at 2022-06-22 12:06:43.259303
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Initializing the LookupModule class
    lm = LookupModule()

    # Test case 1
    test_dict = {
        "_terms": ["/etc/resolv.conf.j2"],
        "template_vars": {"dnsdomain": "redhat.com"},
        "variable_start_string": "{{",
        "variable_end_string": "}}",
        "comment_start_string": "#",
        "comment_end_string": "#"
    }
    expected_result = ["# Caution: This file is autogenerated by Ansible\nsearch redhat.com\nnameserver 123.456.789.10\n"]
    result = lm.run(**test_dict)
    assert result == expected_result

    # Test case 2

# Generated at 2022-06-22 12:06:51.574038
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.module_utils.common.collections import ImmutableDict

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['/dev/null'])
    variable_manager.set_inventory(inventory)
    play_context = PlayContext()

    lookup = LookupModule()
    lookup.set_loader(loader)
    lookup.set_inventory(inventory)
    lookup.set_variable_manager(variable_manager)
    lookup.set_play_context(play_context)


# Generated at 2022-06-22 12:07:03.494197
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    template_data_simple="""
    {{
    output = []
    for i in range(10):
        output.append(i+5)
    output
    }}
    """.strip()

    template_data_complex="""
    {{
    output = []
    for i in range(10):
        output.append(i+5)
    output
    }}
    {{ 10+20 }}
    """.strip()

    template_data_complex_string="""
    {{
    output = []
    for i in range(10):
        output.append(i+5)
    output
    }}
    {{ '10+20' }}
    """.strip()

    from ansible.parsing.vault import VaultLib

    vault_pass = 'password'

# Generated at 2022-06-22 12:07:13.984572
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    plugin = LookupModule()
    ################################################################################
    # Test 1
    terms = ["../library/template_test_jinja2.j2"]
    variables = {"foo": "bar", "baz": "foobaz"}
    ret = plugin.run(terms, variables)

    assert(ret[0] == "This is a test.\n")

    ################################################################################
    # Test 2
    terms = ["../library/template_test_jinja2_native.j2"]
    variables = {"foo": "bar", "baz": "foobaz"}
    ret = plugin.run(terms, variables)

    assert(ret[0] == "This is a test.\n")

    ################################################################################
    # Test 3

# Generated at 2022-06-22 12:07:21.346866
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule().run([
        './files/foo',
        './files/bar',
        './files/baz',
    ], {
        'some_variable': 'I got some variable',
        'some_other_variable': 'I got some other variable',
    }, convert_data=True, variable_start_string='[%', variable_end_string='%]', template_vars={
        'some_lookup_variable': 'I got some lookup variable',
    }) == [
        'I got some variable',
        'I got some variable\nI got another variable',
        'I got some variable\nI got some other variable\nI got some lookup variable',
    ]

# Generated at 2022-06-22 12:07:25.663470
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['.some_template.j2']
    variables = {}
    ## instantiate
    lookup_plugin = LookupModule()
    ## run with emtpy parameter
    result = lookup_plugin.run(terms, variables)
    assert result == []

if __name__ == '__main__':
    test_LookupModule_run()

# Generated at 2022-06-22 12:07:37.825549
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import PY3
    from ansible.modules.system import path
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    loader = DataLoader()
    vars = VariableManager()
    lookup = LookupModule()

    # Test basic template
    template_var = '{{ foo }}'
    if PY3:
        template_var = bytes(template_var, encoding='utf-8')

    lookup.set_loader(loader)
    lookup.set_vars(vars)
    lookup.set_environment(path(loader))
    lookup.set_options({})
    assert lookup.run(terms=[template_var], variables=dict(foo='bar')) == [u'bar']

    # Test template with jinja2

# Generated at 2022-06-22 12:07:48.005952
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Create a mock inventory to use for testing
    class MockInventory:

        def __init__(self):
            self._vars = {}

        def get_vars(self, host):
            return self._vars

        def set_variable(self, host, varname, value):
            self._vars[varname] = value

    # Create a mock module to use for testing
    class MockModule():

        def __init__(self):
            self.params = dict()
            self.params['terms'] = None
            self.params['variables'] = None

        def fail_json(self, *args, **kwargs):
            self.exit_args = args
            self.exit_kwargs = kwargs
            raise Exception('FAIL')

    # Mock the function which finds files in search path

# Generated at 2022-06-22 12:07:49.460258
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert False, 'No unit tests defined for LookupModule.run'

# Generated at 2022-06-22 12:08:34.917659
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = [
        './some_template.j2',
        './another_template.j2',
    ]
    options = {
        '_templar': None,
        'lookup_loader': None,
        'variable_manager': None,
    }

    lookup_result = LookupModule().run(terms, options)
    assert isinstance(lookup_result, list)

# Generated at 2022-06-22 12:08:37.981275
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule().run(terms=['/bin/ls /nonexistent', 'doesnotexist'], variables=dict()) == []

# Generated at 2022-06-22 12:08:41.861234
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    lookup_file = LookupModule()
    term_file = ["./test_files/test_vars.yml"]
    variables = dict(path = "./test_files")
    lookup_file.run(terms = term_file, variables = variables)
    return

# Generated at 2022-06-22 12:08:53.458050
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    import sys
    import os
    import collections
    import json
    import textwrap
    # import yaml
    from ansible.template import Templar
    from ansible.module_utils.six import PY3

    HAS_SIMPLE_TEMPLATE = True
    try:
        from ansible.template.simple_template import SimpleTemplate as Jinja2Template
    except ImportError:
        HAS_SIMPLE_TEMPLATE = False

    os.environ['ANSIBLE_LOOKUP_TEMPLATE'] = '1'
    os.environ['ANSIBLE_LOOKUP_TEMPLATE_TEMPLATE_DIR'] = os.path.join(os.path.dirname(__file__), '../templates')

    # test_LookupModule_run.py is inside lib/ans

# Generated at 2022-06-22 12:09:05.360496
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit test for method run of class LookupModule.
    """
    import os
    from ansible.plugins.loader import lookup_loader

    if os.path.exists("test/template_tests/test.j2"):
        test_templ = lookup_loader.get("template", loader=lookup_loader, templar=None)
        test_terms = ["test.j2"]
        test_variables = {"bar" : "baz"}
        test_results = test_templ.run(test_terms, test_variables, convert_data=True)
        assert test_results == ['foo\n'], "\"foo\\n\" was expected"
    else:
        sys.stderr.write("template_tests/test.j2 not found. Test skipped.\n")

# Generated at 2022-06-22 12:09:10.844130
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    env = {
        'ansible_search_path': [os.path.dirname(__file__) + '/../lookup_plugins']
    }
    terms = ['template_test.j2']
    results = lookup_module.run(terms, env)
    assert len(results) == 1
    assert results[0] == 'TEST: 1, 2, 3, 4'

# Generated at 2022-06-22 12:09:13.064398
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit test for method run of class LookupModule
    :return:
    """

    lookup_module = LookupModule()

# Generated at 2022-06-22 12:09:20.389670
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ['test.j2']

    # Create an empty environment
    variables = {}

    # Create a template_vars mapping
    template_vars = {'name': 'Bob'}

    # Create an empty options dictionary
    options = {}

    # Call method run of class LookupModule to perform template lookup
    result = lookup.run(terms, variables, **template_vars)

    # Assert that the expected result is returned
    assert result == [u'Hello, Bob!']

# Generated at 2022-06-22 12:09:58.974335
# Unit test for method run of class LookupModule

# Generated at 2022-06-22 12:10:04.692015
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    module = LookupModule()
    terms = ["/some/path/some_template.j2"]
    variables = {"some_var": "some_value"}
    kwargs = {"convert_data": False, "template_vars": {"some_template_var": "some_template_value"}}

    module.run(terms, variables, **kwargs)