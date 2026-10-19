

# Generated at 2022-06-22 12:01:15.584244
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup import LookupModule
    lookup_instance = LookupModule()
    from ansible.compat.tests.mock import patch, Mock
    import ansible.constants
    import os

    with patch.object(ansible.constants, 'DEFAULT_VAULT_ID_MATCH', 'test_vault_id_match'):
        with patch.object(os.path, 'exists', Mock(return_value=True)):
            with patch.object(os, 'access', Mock(return_value=True)):
                with patch('ansible.plugins.loader.get_loader') as mock_loader:
                    import jinja2.exceptions

# Generated at 2022-06-22 12:01:28.090483
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import pytest
    from unittest.mock import patch

    from ansible.module_utils._text import to_bytes, to_native
    from ansible.plugins.lookup import LookupBase

    example_yaml = """
- node:
    name: testing
    hidden: True
    children:
    - name: c1
    - name: c2
    """

    example_yaml_data = [{
        b'node': {
            b'children': [
                {b'name': b'c1'},
                {b'name': b'c2'}],
            b'hidden': True,
            b'name': b'testing'}}]

    example_vars = {
        'nodes': [{'name': 'node1'}]
    }

    example_vars_file

# Generated at 2022-06-22 12:01:37.656105
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    display = Display()
    templar = Templar(variables={})
    lookup = LookupModule()
    lookup.set_options(templar=templar)
    lookup._loader = DictDataLoader({'some_template.j2': b"This is a {{test}}\n"})
    lookup._loader.set_basedir(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'test', 'templates'))

    terms = ['./some_template.j2<%test%>']
    variables = {'test': 'lookup'}

    # case where convert_data is True
    convert_data = True
    lookup.set_options(var_options=variables, direct={'convert_data': convert_data})

# Generated at 2022-06-22 12:01:44.336601
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup_object = LookupModule()

    # Invoke the method
    assert lookup_object.run(["test.j2"], {})

    # Invoke the method
    assert lookup_object.run(["test.j2"], {}, convert_data=True)

    # Invoke the method
    assert lookup_object.run(["test.j2"], {}, variable_start_string='[%')

    # Invoke the method
    assert lookup_object.run(["test.j2"], {}, variable_end_string='%]')

    # Invoke the method
    assert lookup_object.run(["test.j2"], {}, jinja2_native=True)

    # Invoke the method
    assert lookup_object.run(["test.j2"], {}, template_vars={'abc': 'def'})

   

# Generated at 2022-06-22 12:01:56.270324
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Instantiate mock object for display and create an instance of LookupModule
    display = Display()
    lookup_module = LookupModule(loader=None, templar=None, shared_loader_obj=None)

    # Create Mocks for AnsibleModule and create an instance of it
    ansible_module = AnsibleModule(argument_spec=dict())

    # Create a mock of LookupBase class
    lookup_base_mock = lookup_base.LookupBase(loader=None, templar=None)

    # Create a mock of AnsibleEnvironment class
    ansible_environment_mock = ansible_environment.AnsibleEnvironment

    # Create a mock of native_jinja class
    native_jinja_mock = native_jinja.NativeJinjaText

    # Mocking the _get_file_contents method of Ans

# Generated at 2022-06-22 12:02:08.441642
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Prepare mocks
    terms = './some_template.j2'
    variables = dict()
    lookup_template_vars = dict()
    jinja2_native = False
    convert_data_p = True
    variable_start_string = '{'
    variable_end_string = '}'
    comment_start_string = '{#'
    comment_end_string = '#}'
    kwargs = dict()
    kwargs['variable_start_string'] = variable_start_string
    kwargs['variable_end_string'] = variable_end_string
    kwargs['comment_start_string'] = comment_start_string
    kwargs['comment_end_string'] = comment_end_string
    kwargs['template_vars'] = lookup_template_vars


# Generated at 2022-06-22 12:02:17.410275
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    class VarsModule(object):
        def __init__(self):
            # the new style accesses of templar have dot notation instead of []
            # so we need to create an object rather than a dict
            # TODO: revisit this decision
            self.hostvars = {'host1': {'foo': 'bar'}, 'host2': {'ansible_host': '127.0.0.1'}}

    class Templar(object):
        def __init__(self):
            self.SEARCHPATH = []
            self.set_available_variables({'omg': 'zomg'})

        def copy(self):
            return Templar()

        def set_available_variables(self, vars):
            self.available_variables = vars


# Generated at 2022-06-22 12:02:28.879405
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.facts import is_local_vagrant_vm
    from ansible.module_utils.six import string_types
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext

    vault_pass = None
    if os.path.exists('.vault_pass'):
        with open('.vault_pass', 'r') as f:
            vault_pass = f.read()

    password = VaultLib(password=vault_pass)


# Generated at 2022-06-22 12:02:39.847536
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test the run() method with a sample template file.
    # The file to process is provided as first parameter.
    # The second parameter is a dict describing the
    # ansible variables to be used.
    from ansible.utils.vars import combine_vars
    from ansible.compat.six import text_type
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.template import Templar

    with open('./test_data/vault.yml') as f:
        vault_pwd_file = f.read()

    # The dict to pass as second parameter of run()
    # The 'hostvars' key is required to run the test.
    # The 'ansible_vault_password_file' key is required to parse a vault encrypted file.
   

# Generated at 2022-06-22 12:02:51.660985
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module._templar = None
    lookup_module._loader = None
    template_path = "./../../../../../tests/templates"
    template_file = os.path.join(template_path, "all_format_types.j2")
    terms = ["../../../tests/templates/all_format_types.j2"]
    variables = {
        "template_host": "example.com",
        "template_uid": 12345,
        "template_path": template_path,
        "template_mtime": 1500000000,
        "template_mtime_utc": "2017-07-14T07:40:00Z",
        "lookupfile": template_file
    }

# Generated at 2022-06-22 12:03:03.693690
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module.set_loader({})

    # set up some dummy data for this test
    data = dict(
        template_dir = '.',
        template_dirs = ['.'],
        searchpath = ['./test/'],
        files = ['ansible.cfg'],
        _terms = 'ansible.cfg',
        convert_data = False,
        variable_start_string = '{{',
        variable_end_string = '}}',
        comment_start_string = '#',
        comment_end_string = '#'
    )
    lookup_module.set_options(data)

    # run the test
    result = lookup_module.run(data['_terms'], data, './test/')

# Generated at 2022-06-22 12:03:06.269184
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule.run(
        terms=['a'],
        variables={'_terms': ['b']}
    ) == []



# Generated at 2022-06-22 12:03:17.285931
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    templar = AnsibleEnvironment()

    module = LookupModule()
    module._templar = templar
    module._loader = templar._loader

    # Testing basic functionality of lookup.

# Generated at 2022-06-22 12:03:23.987610
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # input
    terms = ['some_template.j2']
    variables = {}

    # instantiate object
    obj = LookupModule()
    obj.set_loader(obj)
    obj._templar = obj

    # run run
    results = obj.run(terms, variables)

    # assert
    for result in results:
        assert result == "hello"

# Generated at 2022-06-22 12:03:34.928480
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    args = {'_raw_params': 'foo', '_terms': ['foo'], 'jinja2_native': False, 'convert_data': False}
    lu = LookupModule()
    result = lu.run([to_bytes('foo')], {}, **args)
    assert result == ['foo']

    args = {'_raw_params': 'foo', '_terms': ['foo'], 'jinja2_native': True, 'convert_data': False}
    lu = LookupModule()
    result = lu.run([to_bytes('foo')], {}, **args)
    assert result == ['foo']

    args = {'_raw_params': 'foo', '_terms': ['foo'], 'jinja2_native': False, 'convert_data': True}
    lu = Lookup

# Generated at 2022-06-22 12:03:43.561418
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play

    lookup_plugin = LookupModule()
    inventory = InventoryManager(loader=DataLoader(), sources='localhost,')
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)
    play_source =  dict(
        name = "Ansible Play",
        hosts = 'localhost',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='debug', args=dict(msg='{{lookup("template", "./test_lookup_plugin/hello_world.j2")}}')))
        ]
    )

# Generated at 2022-06-22 12:03:55.067165
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    env = {
        'basedir': '..'
    }

    import jinja2
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import lookup_loader
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    loader = DataLoader()
    inv_manager = InventoryManager(loader=loader, sources=['hosts'])

# Generated at 2022-06-22 12:04:04.719733
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.vars import VariableManager
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    loader = DataLoader()
    variable_manager.extra_vars = {
        'foo': 'foo_value',
    }
    templar = Templar(loader=loader, variables=variable_manager)
    lookup_obj = LookupModule()
    lookup_obj.set_loader(loader)
    lookup_obj._templar = templar
    lookup_obj.set_environment(variable_manager.extra_vars)
    data = [u'<%= foo %>']
    assert lookup_obj.run(data, dict()) == ['foo_value']


# Generated at 2022-06-22 12:04:16.298496
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import StringIO
    from ansible.template import Templar

    # Create a mock environment with a templar.
    mock_env = {
        'name': 'mock_env',
        '_templar': Templar(),
    }

    # Create a looker that uses this environment.
    looker = LookupModule()
    looker.set_environment(mock_env)

    # Create some mock data to look up.
    terms = ['{{ foo }}', '{{ not_foo_bar }}']
    variables = {'foo': 'bar'}

    # Run the lookup. It should return data containing only the first term.
    data = looker.run(terms, variables)
    assert len(data) == 1
    assert data[0] == 'bar'

    # Run the lookup again

# Generated at 2022-06-22 12:04:27.764624
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Run a single test case of the method run directly
    #
    # Note: This test case is based on a test file and the module name
    #       used in this test file is dummy and not relevant.
    #       The actual file and module names are much more related and
    #       are refelcted in the test case files of each module.
    #
    class LookupModule_run_test():

        def __init__(self):

            # Initialize the test parameters
            #
            # Note: The test file is in the same dir as the unit test file
            #
            self.tmpl_file_name = 'test.tmpl'
            self.tmpl_file_path = os.path.dirname(__file__)
            self.param_dirs = [ '/etc/ansible' ]

            # Initialize the Ans

# Generated at 2022-06-22 12:04:49.063835
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Setup
    # to_text(bytes) is a no-op when built with unicode; to_text(bytes, 'utf-8') is a no-op when built with unicode and u'abc' is just a unicode string;
    # to_bytes(unicode) is a no-op when built with unicode; to_bytes(unicode, 'utf-8') is a no-op when built with unicode and u'abc' is just a unicode string.
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader
    import ansible.constants as C

    # create a dummy inventory

# Generated at 2022-06-22 12:04:59.834311
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def lookuper():
        LookupModule.run(self, terms, variables, variable_start_string='[%', variable_end_string='%]')

    from ansible.template import AnsibleTemplate
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.vars import combine_vars
    from ansible.vars.clean import clean_facts
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager

    # here is sample plugin configuration
    vars_plugins = ['host_extra_vars']
    # we need use VariableManager instance, so we need build class structure not only dict
    hvars = HostVars({"localhost": {'a': 1, 'b': 2}})

# Generated at 2022-06-22 12:05:09.827308
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Unit test for method run of class LookupModule."""

    ###############################################################################
    ### LookupModule.run(self, terms, inject=None, variable_start_string=None, variable_end_string=None,
    #                     convert_bare=True, fail_on_undefined=True, filter_fatal=False, **kwargs):
    ###############################################################################

    # Mock module loader to have
    # - a function set_basedir, which does nothing.
    # - a function get_basedir, which returns the string '_basedir'
    # - a property basedir, which returns the string 'basedir'
    # - a property cache, which returns None
    class _loader:
        def set_basedir(self, _):
            return None

        def get_basedir(self):
            return

# Generated at 2022-06-22 12:05:22.932994
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Unit test for method run of class LookupModule"""

    # Define test variables
    class DummyVars(object):
        """Dummy object for variables"""
        def __init__(self, value):
            self._value = value

        def get(self, key, default):
            if key == "ansible_search_path":
                return self._value

    class DummyVars2(object):
        """Dummy object for variables"""
        def get(self, key, default):
            return default

    class DummyDisplay(object):
        """Dummy object for display"""
        def __init__(self):
            self._last = None

        def debug(self, msg):
            self._last = msg

        def vvvv(self, msg):
            self._last = msg


# Generated at 2022-06-22 12:05:24.747133
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert False, "WIP"

# Generated at 2022-06-22 12:05:35.510102
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six.moves import StringIO
    module_args = dict(
        terms=['../../test/unit/lookup_plugins/test.j2'],
        variables={
            'template_host': '127.0.0.1',
            'ansible_search_path': ['../../test/unit/lookup_plugins']
        },
        convert_data=False,
        jinja2_native=False,
        variable_start_string='{{',
        variable_end_string='}}',
        comment_start_string='{#',
        comment_end_string='#}',
        template_vars={},
        _original_file=None
    )
    lu = LookupModule()

# Generated at 2022-06-22 12:05:44.552921
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Construct an instance of the class
    lookup_module = LookupModule()

    # Save the current env vars
    old_env = {}
    old_env.update(os.environ)

    # Add an environment var

# Generated at 2022-06-22 12:05:55.674322
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import re
    import json
    from ansible.module_utils.common.text_factory import to_text
    from ansible.module_utils.common.text_factory import to_bytes
    from ansible.module_utils.common.text_factory import to_native
    from ansible.template import Templar

    env = {
        'template_dir': './tests/templates'
    }

    lookup = LookupModule()
    ansible_env = [to_native(e, errors='surrogate_or_strict') for e in env.items()]
    lookup._templar = Templar(loader=None, variables=dict(ansible_env))
    ansible_search_path = {
        'ansible_search_path': ['./tests/templates']
    }
    lookup.set_

# Generated at 2022-06-22 12:06:00.993138
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest

    # test will fail if called with native_jinja2=True when jinja2 is not installed
    lookup = LookupModule(loader=None, templar=None, shared_loader_obj=None, **{'jinja2_native': False})
    result = lookup.run([pytest.helpers.data_path('template_lookup_test.j2')], variables={}, **{})

    assert len(result) == 1
    assert result[0] == 'Hello World\n'

# Generated at 2022-06-22 12:06:03.631182
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    LookupModule(loader=None, templar=None, shared_loader_obj=None).run(['./test.j2'],dict())

# Generated at 2022-06-22 12:06:36.510954
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    my_terms = {
        '../test/test6.j2',
        '../test/test1.j2',
        '../test/test2.j2',
        '../test/test3.j2',
        '../test/test4.j2',
        '../test/test5.j2',
        '../test/test7.j2',
        '../test/test8.j2',
        '../test/test9.j2',
    }


# Generated at 2022-06-22 12:06:46.195386
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible.parsing.dataloader import DataLoader

    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager.set_inventory(inventory)

    class VarsModule:
        def run(self, terms):
            return {'key1': 'value1', 'key2': [1, 2, 3]}

    variable_manager.set_vars_mod

# Generated at 2022-06-22 12:06:58.275074
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test with three-part lookup and two successful lookups
    module = LookupModule()
    basedir = '/tmp'
    module._loader.path_basedirs = [basedir]
    terms = [
        '{{ inventory_dir }}/group_vars/{{ inventory_hostname }}/foo.yml',
        '{{ inventory_dir }}/foo.yml',
        '{{ inventory_dir }}/bar.yml',
    ]
    variables = dict(
        inventory_dir='/my/inventory/dir',
        inventory_hostname='testhost',
    )


# Generated at 2022-06-22 12:07:05.847665
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = {
        'var': 'var',
        'path': os.path.abspath('./test/fixtures/test.j2')
    }
    variables = {
        'var': 'hello world',
        'ansible_search_path': [os.path.abspath('./test/fixtures')],
    }
    expected = ["hello world"]
    lookup_module = LookupModule()
    assert lookup_module.run(terms, variables) == expected

# Generated at 2022-06-22 12:07:13.761531
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lu = LookupModule()
    data = lu.run(['string_to_template.j2'], {
        'template_vars': {'vars': 'templated'},
        'variable_start_string': '%%',
        'variable_end_string': '%%',
        'comment_start_string': '%%#',
        'comment_end_string': '#%%'
    })
    assert data[0] == 'This is templated data\n'

# Generated at 2022-06-22 12:07:23.165202
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # FIXME: remove this module_utils import when the test method is moved to the test file
    module_utils = __import__('ansible.module_utils.six', fromlist=['*'])

    # Define mock_args

# Generated at 2022-06-22 12:07:34.902100
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module.set_loader({'_get_file_contents': lambda x,y: ('<<< {{ some_var }} >>>', False)})
    lookup_module._templar = None

    # Testing with jinja2_native = False
    assert lookup_module.run(terms=['some_template.j2'], variables={'some_var': 'some_value'}) == ['<<< some_value >>>']

    # Testing with jinja2_native = True
    lookup_module._templar = None
    lookup_module.set_loader(None)
    lookup_module.set_options(direct={'jinja2_native': True})

# Generated at 2022-06-22 12:07:44.634155
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    #
    # test setup
    #
    import sys
    sys.path.insert(0, '.')
    sys.path.insert(0, 'lib/ansible/modules')
    from ansible.constants import DEFAULT_MODULE_PATH, DEFAULT_VAULT_ID_MATCH
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts.system.distribution import WindowsDistribution
    from ansible.module_utils.facts.system.distribution import DistFact
    from ansible.vars import combine_vars
    from ansible.vars.hostvars import HostVars

    d = DistributionFactCollector()

# Generated at 2022-06-22 12:07:49.015083
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # test required and optional arguments
    module = LookupModule()
    assert 'template: some_template.j2' in module.run(['some_template.j2'], {}, convert_data='true')

    # TODO: Test other options, get_option, find_file_in_search_path

# Generated at 2022-06-22 12:07:57.791805
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import yaml
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play import Play
    from ansible.plugins.loader import lookup_loader

    # Create a class object to handle test data
    class MyTestVars(object):
        def __init__(self, data=None):
            self.data = data

        def get_vars(self, loader, path, entities):
            return self.data


# Generated at 2022-06-22 12:08:48.361348
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Method run of class LookupModule to test template lookup plugin
    # Arguments of method run:
    #   1. terms: The variables to load, given as a list.
    #   2. variables: Variables given from command line.
    #   3. **kwargs: arbitrary keyword arguments.
    # Return value of method run:
    #   A list of template results.
    # Create an instance LookupModule
    lookup_instance = LookupModule()
    # Call method run
    lookup_instance.run(terms = ["./test/fixtures/template.j2"],
                        variables = {},
                        **{'convert_data':False})

# Generated at 2022-06-22 12:08:54.790346
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Define temporary variables
    terms = ['/path/to/a/file.j2']
    variables = {'item': 'value'}
    kwargs = {'variable_end_string': '}}', 'variable_start_string': '{{'}
    # Instantiate object LookupModule
    lookup_module = LookupModule()
    # Call method run
    assert lookup_module.run(terms, variables, **kwargs)

# Generated at 2022-06-22 12:09:06.768740
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import unittest
    class Mock_ModuleDepLoader:
        def _get_file_contents(self, file):
            pass

    class Mock_Templar:
        def __init__(self):
            pass

        def set_temporary_context(self):
            pass

        def template(self):
            pass

    class Mock_SearchPath:
        def __init__(self):
            pass

        def find(self):
            pass

    class Mock_LookupBase:
        def __init__(self):
            pass

        def find_file_in_search_path(self):
            pass

    class Mock_Ansible:
        def __init__(self):
            pass

        def get_config(self):
            pass


# Generated at 2022-06-22 12:09:12.245145
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupBase()
    setattr(lookup, "_loader", MockLoader())
    setattr(lookup, "_templar", MockTemplar())
    assert lookup.run("test.txt", {}, __file__) == "Hello World"


# Generated at 2022-06-22 12:09:23.810160
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader

    lookup_instance = LookupModule()
    lookup_instance.set_loader(DataLoader())
    lookup_instance._templar.environment.filters.update(dict(to_json=lambda x: 'filter_result'))

    def _get_file_contents(path):
        if path.endswith('linux.j2'):
            return b'{{ lookup("pipe", "uname -s") }}', True
        elif path.endswith('aix.j2'):
            return b'{{ lookup("pipe", "uname -s") }}', True
        elif path.endswith('solaris.j2'):
            return b'{{ lookup("pipe", "uname -s") }}', True

# Generated at 2022-06-22 12:09:59.069113
# Unit test for method run of class LookupModule

# Generated at 2022-06-22 12:10:04.184079
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    filename = 'file_name'
    folder = 'folder'
    fullpath = os.path.join(folder, filename)
    # Create a content for the template file
    content = "Hello World"

    # Create a class for the properties
    class Options(object):
       pass

    options = Options()
    options.convert_data = 'True'
    options.variable_start_string = '{{'
    options.variable_end_string = '}}'
    options.template_vars = ['test:test']
    options.comment_start_string = '----'
    options.comment_end_string = '----'
    options.jinja2_native = 'False'
    vars = ['ansible_search_path']

    # Create a class for the self._loader
    class Loader(object):
        pass

# Generated at 2022-06-22 12:10:14.954124
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Unit test for method run of class LookupModule"""

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()

    variable_manager = VariableManager()
    variable_manager.set_inventory(loader.load_inventory(['localhost']))

    module = LookupModule(loader=loader, variable_manager=variable_manager)

    terms = ['./some_template.j2']
    variables = dict()

    # test with empty search path
    module.set_options(var_options=variables, direct=dict())
    result = module.run(terms, variables)
    assert result == ["./some_template.j2"]

    # test with existing search path

# Generated at 2022-06-22 12:10:20.642770
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # This is a hack to setup the class so we can just call run.
    # We would normally call that from the playbook.
    lm = LookupModule()
    lm.set_options(var_options=dict(ansible_search_path=[]))
    data = lm.run(['tests/test_lookup_template.j2'], dict())
    assert data[0] == u'Hello world\n'

# Generated at 2022-06-22 12:10:32.140692
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.template import Templar

    templar = Templar(loader=None, variables=dict())
    args = dict(
        _terms=['foo.j2', 'bar.j2'],
        convert_data=True,
        template_vars={'var0': 'foo', 'var1': 'bar'},
        variable_start_string='{{', variable_end_string='}}',
        comment_start_string='{#', comment_end_string='#}'
        )
    kwargs = dict()
    lookup_module = LookupModule(templar=templar, loader=None)

    # Fake filesystem paths
    foo_path = 'path/to/foo.j2'

    # Expected result of lookup using the fake file system paths