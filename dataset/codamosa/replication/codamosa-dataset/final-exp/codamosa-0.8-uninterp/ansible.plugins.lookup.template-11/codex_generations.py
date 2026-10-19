

# Generated at 2022-06-22 12:01:16.477030
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.display import Display
    from ansible.template import Templar

    # terms = ["./some_template.j2"]
    # template_data = """
    # {{ lookup('template', './some_template.j2') }}
    # """

    terms = ["./some_template.j2", "some_template_with_ansible_template_vars.j2"]

# Generated at 2022-06-22 12:01:29.172722
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # See https://github.com/ansible/ansible/issues/18807
    # Test for bug with backslash in the remote_src path
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.dataloader import DataLoader
    dataloader = DataLoader()
    dataloader.set_basedir("../test/testdata/test_lookup_plugins")
    tm = LookupModule(basedir=dataloader._basedir, runner=None)
    tm.set_loader(dataloader)
    tm.set_environment('',dict(lookup_file_contents_without_templating=dict()))
    f_name = "backslashInRemoteSrc.txt"
    terms = [f_name]

# Generated at 2022-06-22 12:01:40.282435
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    returncode = 0
    failed_msg = ''
    failed = False

    # Testing Exceptions
    l = LookupModule()
    vars = dict(ansible_search_path=['/dev'])
    terms = ['some_template.j2']
    try:
        l.run(terms, variables=vars)
    except AnsibleError as e:
        if to_text(e) != "the template file some_template.j2 could not be found for the lookup":
            failed = True
            failed_msg = 'Expected AnsibleError "the template file some_template.j2 could not be found for the lookup" but got "%s"' % to_text(e)

    # Testing return
    l = LookupModule()
    terms = ['README.md']

# Generated at 2022-06-22 12:01:52.829558
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    terms_template_file = 'test_terms.j2'
    templar = AnsibleEnvironment()
    variables = {'lookup_template_vars': {'some_key': 'some_value', 'key': 'value'}, 'var1': 'value1'}
    test_obj = LookupModule()

    with open(terms_template_file, 'w') as f:
        f.write("""{{ lookup_template_vars.some_key }}, {{ lookup_template_vars.key }}, {{ var1 }}""")

    terms = [terms_template_file]
    result_expected = ['some_value, value, value1']
    result_actual = test_obj.run(terms, variables, templar=templar)

    return result_actual == result_expected

# Generated at 2022-06-22 12:02:04.972970
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # instantiate the lookup module
    lookup_module = LookupModule()
    # set the loader because it's expected to return some things
    # that assume the loader has been set to something
    lookup_module._loader = DictDataLoader({'test': 'foo'})
    # add some items to the templar
    lookup_module._templar._available_variables = {'test': 'foo'}
    lookup_module._templar.environment.loader = lookup_module._loader
    # set the template_dirs
    lookup_module.template_dirs = []
    # Get the result of the run method
    result = lookup_module.run(['./test'], {}, convert_data=True, jinja2_native=False)
    # assert that we got the right result back

# Generated at 2022-06-22 12:02:15.337767
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_options = dict(convert_data=False, jinja2_native=False, template_vars={'test': 'unit_testing'})
    lookup_module = LookupModule()

    # test with filenames
    lookup_module._templar = Templar(loader=DictDataLoader(dict(test='test_template_content')))
    lookup_module._loader = AnsibleFileLoader(None, 'utf-8')
    results = lookup_module.run(['test'], dict(), **lookup_options)
    assert(list(results) == [u'test_template_content'])

    # test with content
    lookup_module._templar = Templar(loader=DictDataLoader(dict(test='{{ test }}')))

# Generated at 2022-06-22 12:02:27.142826
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a dummy ansible.parsing.dataloader.DataLoader object and
    # its required attributes
    from ansible.parsing.dataloader import DataLoader
    dl = DataLoader()
    dl.set_basedir('/path/to/ansible/playbook')

    # Create a dummy ansible.parsing.vault.VaultEditor object and its
    # required attributes
    from ansible.parsing.vault import VaultEditor
    ve = VaultEditor()

    # Create a dummy ansible.inventory.manager.InventoryManager object
    # and its required attributes
    from ansible.inventory.manager import InventoryManager
    im = InventoryManager(loader=dl, sources='localhost,')

    # Create a dummy ansible.vars.manager.VariableManager object and its
    # required attributes


# Generated at 2022-06-22 12:02:38.511320
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.plugins.loader as plugin_loader
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, variable_manager=variable_manager, host_list=None)

# Generated at 2022-06-22 12:02:49.730704
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup1 = LookupModule()

    # test without jinja2_native
    lookup1.set_options(var_options={'ansible_search_path': ['../../test/test_lookup']}, direct={'jinja2_native': False})

    output = lookup1.run(['./test.j2', './test1.j2'], {}, **{})
    assert output == [u'Hello World\n', u'Hello World\n']

    # test with jinja2_native
    lookup2 = LookupModule()
    lookup2.set_options(var_options={'ansible_search_path': ['../../test/test_lookup']}, direct={'jinja2_native': True})


# Generated at 2022-06-22 12:03:02.298174
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    ##################################################
    # Setup:
    ##################################################
    # Create object for testing.
    options = dict()
    options["variable_start_string"] = "{{{"
    options["variable_end_string"] = "}}}"
    options["comment_start_string"] = "{#"
    options["comment_end_string"] = "#}"
    options["convert_data"] = True
    options["template_vars"] = dict()
    options["jinja2_native"] = False
    terms = ["test_template.j2"]
    variables = dict()
    variables["inventory_hostname"] = "test-host"
    file_name = "test_template.j2"
    with open(file_name, 'w') as f:
        f.write("{{ inventory_hostname }}")

    #################################

# Generated at 2022-06-22 12:03:17.786811
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible.errors import AnsibleError
    from ansible.parsing.dataloader import DataLoader
    import ansible.plugins.loader as plugin_loader
    from ansible.plugins.lookup import LookupBase

    mock_data_loader = DataLoader({})
    mock_templar = lambda: None
    mock_vars = {}
    mock_config_data = {}
    mock_shared_loader_obj = plugin_loader.PluginLoader(
        'LookupModule', 'lookup', 'ansible.plugins.lookup.LookupModule', lookup_loader=None, config_data=mock_config_data
    )
    lookup_base = LookupBase()
    lookup_base._loader = mock_data_loader
    lookup_base._templar = mock_templar
   

# Generated at 2022-06-22 12:03:26.019617
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Instanciate class LookupModule
    l = LookupModule()

    # set test data
    options = {'template_vars': {
      'var1': 'value1',
      'var2': 'value2',
      'quote': '"quoted value"',
      'quotes': '"quoted var"'
    }}

    # call run with valid parameters
    result = l.run(['./template1.j2'], options)

    # assert result
    assert len(result) > 0

# Generated at 2022-06-22 12:03:35.864520
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible.plugins.lookup.template import LookupModule
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    import os

    currentdir = os.path.dirname(__file__)
    inventory_path = os.path.join(currentdir, 'TestContent', 'Hosts')
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[inventory_path])
    variable_manager = VariableManager(loader=loader, inventory=inventory)


# Generated at 2022-06-22 12:03:44.544197
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # LookupModule_run_test is the class where I have defined the test case for this method
    # It is the subclass of unittest.TestCase
    # It is the collection of test method for this method
    
    # In this class I have created the instance of LookupModule class
    # and called the method run and checked the output of the method is as expected or not
    # Here I have checked the return type of the method is list or not
    # and also checked the output of the method is as expected or not
    LookupModule_run_test.test_LookupModule_run()

# Generated at 2022-06-22 12:03:56.207603
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''Test run method from class LookupModule'''
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    inventory = InventoryManager(loader, sources=['localhost,'])
    play_context = Play().load(dict(
        name="Ansible Play",
        hosts=['127.0.0.1'],
        gather_facts='no',
        tasks=[dict(action=dict(module='setup', args=''))]
    ), variable_manager=inventory.get_variable_manager(), loader=loader)

    lookup_plugin = LookupModule()

# Generated at 2022-06-22 12:04:06.088335
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.plugins.loader import lookup_loader

    from ansible.utils.vars import combine_vars
    import ansible.constants as C

    import json
    import os

    look = lookup_loader.get("template")

    def _play_context(variable_manager, inventory):
        play_context = Play()
        play_context._variable_manager = variable_manager
        play_context._loader = variable_manager._loader
        play

# Generated at 2022-06-22 12:04:14.442776
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a lookup module object for testing
    test_lookup = LookupModule()

    # Set up an arguments dictionary
    test_dict = dict(
        terms=["test_template.j2"],
        variables=dict(
            var1="test1",
            var2="test2",
            jinja2_native=False
        )
    )

    # Run the lookup method
    result = str(test_lookup.run(**test_dict))

    # Assert expected
    assert result == 'test1test2'

# Generated at 2022-06-22 12:04:21.934346
# Unit test for method run of class LookupModule
def test_LookupModule_run():
  # parameters
  terms = [
    "/etc/ansible/template_1.j2",
    "/etc/ansible/template_2.j2",
  ]
  variables = {}
  kwargs = {}

  # LookupModule.run()
  lu = LookupModule()
  res = lu.run(terms, variables, **kwargs)

  # assert result
  assert "Template file 1" in res
  assert "Template file 2" in res


# Generated at 2022-06-22 12:04:28.313193
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''
    Test for method run of class LookupModule
    '''
    #s = 'firstline\nsecondline'
    #l = s.splitlines()
    #print(l[0])
    #print(l[1])

    #return
    display = Display()

    t = LookupModule()
    t._display = display
    t.run(terms=["test.j2"], variables={"name": "lookup_module_test"})

    return

# Generated at 2022-06-22 12:04:36.527791
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Setup data
    class Options(object):
        variable_start_string = '{{'
        variable_end_string = '}}'
        comment_start_string = '{{#'
        comment_end_string = '#}}'
        convert_data = True
        template_vars = {}

    class FakeVarsModule(object):
        def __init__(self):
            self.ansible_search_path = ['.']

    class FakeLoaderModule(object):
        def _get_file_contents(self, t):
            template_file = os.path.join(os.getcwd(), 'templates', t)
            with open(template_file, 'rb') as a_file:
                b_data = a_file.read()
            return (b_data, 'data')


# Generated at 2022-06-22 12:04:51.430076
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Setup
    import sys
    import os
    import textwrap
    import tempfile
    import pytest
    from ansible.errors import AnsibleFileNotFound
    from ansible.template import AnsibleEnvironment

    # Test
    return_result=[]
    return_result.append('string')
    return_result.append('string')
    dict_ret = {}
    dict_ret['ansible_facts'] = {}
    dict_ret['ansible_facts']['test_fact'] = 'test_fact_value'

    # test jinja2_native
    mock_templar = MagicMock()
    mock_templar.template.return_value = return_result
    mock_templar.set_temporary_context.return_value = dict_ret

# Generated at 2022-06-22 12:04:59.894946
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    mod = LookupModule()

    # Case 0
    ret = mod.run(terms='test', variable_end_string='%}', variable_start_string='{%', convert_data=False)
    assert ret == ['test']

    # Case 1
    ret = mod.run(terms=[], variable_end_string='%}', variable_start_string='{%', convert_data=False)
    assert ret == []

    # Case 2
    ret = mod.run(terms=['test', 'one', 'two'], variable_end_string='%}', variable_start_string='{%', convert_data=False)
    assert ret == ['test', 'one', 'two']

# Generated at 2022-06-22 12:05:09.863852
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.constants as C
    import os
    import utils

    reload(utils)
    class MockLoader(object):
        def __init__(self):
            self.basedir = os.getcwd()
        def _get_file_contents(self, f):
            return (b"xxx {{ lookup('env','HOME') }}", True)

    class MockTemplar(object):
        def __init__(self):
            self.basedir = os.getcwd()
        def copy_with_new_env(self, environment_class):
            return self
        def template(self, template_data, preserve_trailing_newlines=True, convert_data=True, escape_backslashes=True):
            return template_data

# Generated at 2022-06-22 12:05:22.932856
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    import tempfile
    import json
    import shutil
    if sys.version_info[0] >= 3:
        from unittest.mock import Mock

        from io import StringIO
    else:
        from mock import Mock

        from StringIO import StringIO
    from ansible_collections.ansible.community.tests.unit.compat.mock import patch

    from ansible.module_utils._text import to_bytes
    from ansible.template import generate_ansible_template_vars, AnsibleEnvironment
    from ansible.errors import AnsibleError
    from ansible.plugins.lookup import LookupBase


# Generated at 2022-06-22 12:05:34.754555
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    ansible_vars = dict(
        template_hosts='127.0.0.1',
        template_version='1.2.3',
    )
    ansible_searchpath = ['/a/search/path']
    display = Display()
    loader = DictDataLoader({'/a/search/path/template.yaml': b'{{template_hosts}}'})
    templar = Templar(loader=loader, variables=ansible_vars)
    lookup_plugin = LookupModule(loader=loader, templar=templar, display=display)
    terms = ['template.yaml']

# Generated at 2022-06-22 12:05:43.693965
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    fake_loader = DictDataLoader({'t/hello.j2': b"{{ foo }}\n" })
    templar = Templar(loader=fake_loader, variables={'foo': 'bar'})
    templar._available_variables = {'foo': 'bar'}

    # Test for file lookup term that does not have template variables
    results = module.run(['hello.j2'], templar, loader=fake_loader)
    assert results == ['bar\n']

    # Test for file lookup term that has template variables
    results = module.run(['{{ foo }}.j2'], templar, loader=fake_loader)
    assert results == ['bar\n']

    # Test for existing file lookup term

# Generated at 2022-06-22 12:05:54.626962
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import ansible.parsing.dataloader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.callback import CallbackBase
    from ansible.parsing.vault import VaultLib

    import os
    import sys
    from collections import namedtuple

    class ResultCallback(CallbackBase):
        """A sample callback plugin used for performing an action as results come in

        If you want to collect all results into a single object for processing at
        the end of the execution, look into utilizing the ``json`` callback plugin
        or writing your own custom callback plugin
        """

# Generated at 2022-06-22 12:06:02.849356
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l.set_options(variable_start_string='[%',variable_end_string='%]')
    result = l.run(['./test.j2'], {}, convert_data=False, jinja2_native=True,
                   template_vars={'test': None,
                                  'foo': 'bar',
                                  'baz': ['qux', 'quux', 'corge'],
                                  'grault': {'garply': 'waldo',
                                             'fred': 1234,
                                             'plugh': True,
                                             'xyzzy': None}
                   })

# Generated at 2022-06-22 12:06:10.558519
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Build test data
    terms = ["/foo/bar/baz/qux/quux", "corge/grault"]
    variables = {
        "hostname": "host1.example.com",
        "myenv": "prod",
        "mygroup": "mygroup",
        "myuser": "myuser",
        "mycontext": "ansible_search_path"
    }

    # Build mock objects
    lkm = LookupModule()
    lkm.set_options = lambda var_options, direct: None
    lkm.get_option = lambda option: None
    lkm.find_file_in_search_path = lambda variables, dirname, filename: filename

# Generated at 2022-06-22 12:06:21.324882
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import json
    import os
    import StringIO
    import sys
    import tempfile
    from ansible.errors import AnsibleUndefinedVariable

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.template import Templar

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, variable_manager=variable_manager, host_list='/dev/null')
    variable_manager.set_inventory(inventory)

    lookup_module = LookupModule()

    test_path = os.path.join(os.path.dirname(__file__), 'templates')


# Generated at 2022-06-22 12:06:38.909783
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import lookup_loader
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.utils.path import unfrackpath
    import os

    # this test file can be found in the same directory as the lookup plugin
    TEST_FILE = unfrackpath(os.path.dirname(__file__) + '/../templates/test_file.j2')

    # Escape a string so it can be used inside a double-quoted string or in a regexp
    # NOTE: This function is taken from "ansible/utils/vars.py"

# Generated at 2022-06-22 12:06:44.879737
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookupmod = LookupModule()
    lookupmod.set_loader(DictDataLoader({'my_template.j2': '"{{ my_var }}"'}))
    lookupmod.set_environment(Environment())
    assert lookupmod.run(['./my_template.j2'], {'my_var': 1}, variable_start_string='(', variable_end_string=')') == ['"1"']


# Generated at 2022-06-22 12:06:52.895383
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    lookup_module_instance = LookupModule()


# Generated at 2022-06-22 12:07:03.343072
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test to assert that _templar is not shared with lookupBase
    um_mock = LookupModule({})
    um_mock.set_loader(DictDataLoader({}))
    um_mock.set_templar(DictTemplate())
    um_mock._templar.environment.variable_start_string = '{'
    terms = ['./some_template.j2']
    variables = {'ansible_search_path': '.'}
    ret = um_mock.run(terms, variables)
    # should not be using the template environment from lookupBase
    assert ret[0] == './some_template.j2'
    # should not use global ansible_enviroment
    assert ret[0] != terms

# Generated at 2022-06-22 12:07:13.903514
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # create a collection of settings to use in testing
    # settings will be given to the LookupModule.run() method and then checked
    # against the expected settings
    env_vars = dict()
    env_vars['convert_data'] = True
    env_vars['comment_end_string'] = ":)"
    env_vars['comment_start_string'] = ":("
    env_vars['jinja2_native'] = True
    env_vars['template_vars'] = dict()

# Generated at 2022-06-22 12:07:23.283986
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import os
    import json

    from ansible.plugins.loader import lookup_loader
    from ansible.parsing.dataloader import DataLoader

    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    from units.mock.loader import DictDataLoader

    loader = DictDataLoader({
        # files in the 'templates' subdir of the basedir
        "./templates/foo.j2": """{{ lookup('env','HOME') }}""",
        "./templates/bar": "{{ lookup('env','HOME') }}",
    })


# Generated at 2022-06-22 12:07:29.231075
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    test_lookupbase = LookupModule()
    test_lookupbase.set_loader(None)

    terms = [ './some_template.j2' ]
    variables = {}
    test_lookupbase.run(terms, variables)

    # We added more fields for the template variables
    fields_added_by_ansible = [ 'ansible_managed', 'template_host', 'template_uid', 'template_path', 'template_fullpath', 'template_run_date' ]
    for field in fields_added_by_ansible:
        assert field in test_lookupbase._templar.available_variables

# Generated at 2022-06-22 12:07:41.012224
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader.lookup_loader import LookupModuleLoader
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = LookupModuleLoader()
    def return_template_data(*args, **kwargs):
        return '{{lookup_var}}', False
    loader._get_file_contents = return_template_data

    t1 = 'myfile.j2'

    data_loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.extra_vars = {'lookup_var': 'Lookup Value'}
    variable_manager.options_vars = {'lookup_var': 'Lookup Value'}

# Generated at 2022-06-22 12:07:51.628235
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    Lm = LookupModule()
    mock_loader_get_file_contents = MagicMock(return_value="""
{{ myvar }}
{{ myvar2 }}
{{ myvar3 }}
{{ myvar4 }}
""")
    mock_loader = MagicMock()
    mock_loader.get_file_contents = mock_loader_get_file_contents
    Lm._loader = mock_loader
    Lm.find_file_in_search_path = lambda a, b, c: 'some_file'
    Lm._templar = MagicMock()
    Lm._templar.template = MagicMock(return_value='whatever')
    Lm.set_options = MagicMock()
    Lm.get_option = MagicMock(return_value=True)

# Generated at 2022-06-22 12:08:04.240123
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.template import Templar
    from ansible import context
    import os
    import pytest
    import jinja2
    from ansible.utils.display import Display
    import __builtin__ as builtins
    import sys

    my_vault_secret = VaultLib(password='secret')
    my_loader = DataLoader()
    my_vars = VariableManager()
    my_display = Display()
    context.CLIARGS = {'vault_password_file': None, 'ask_vault_pass': False, 'new_vault_password_file': None, 'vault_ids': [], 'output_file': None}

# Generated at 2022-06-22 12:08:22.918044
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test lookup with a non-existent template file.

    lookup_instance = LookupModule()
    assert lookup_instance is not None

    try:
        lookup_instance.run(
            terms=['not-a-template'],
            variables={},
            **{'_terms': ['not-a-template'], 'convert_data': True, 'template_vars': {}, 'jinja2_native': False, 'variable_start_string': '{{', 'variable_end_string': '}}', 'comment_start_string': '{#', 'comment_end_string': '#}'},
        )
    except AnsibleError:
        pass
    except Exception as e:
        raise Exception("Expecting AnsibleError, found: {0}".format(e))

    # Test lookup with a template file that has a variable.

# Generated at 2022-06-22 12:08:34.860631
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    try:
        from __main__ import display
    except ImportError:
        display = Display()

    # Create an instance of LookupModule
    lookup_plugin = LookupModule()
    # Create an environment and populate it with current Ansible variables
    my_env = Environment()
    my_env.loader = DictDataLoader({'my_var': 'my_var_value'})
    my_env.variable_manager = VariableManager()
    my_env.variable_manager.extra_vars = {'ansible_debug': True}
    # Patch LookupModule.run to use my environment
    lookup_plugin.run = run_patch(lookup_plugin.run, my_env)

    # Run the method under test with a variety of test cases

# Generated at 2022-06-22 12:08:44.558675
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit test for method run of class LookupModule
    """
    from ansible.utils.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    # Dummy vars
    variables = VariableManager()
    inventory = InventoryManager(loader=DataLoader())
    templar = Templar(loader=None, variables=variables)

    # Create LookupModule instance
    lookup_plugin = LookupModule()
    lookup_plugin._loader = DataLoader()
    lookup_plugin._templar = templar

    # Run the run() method with dummy data
    result = lookup_plugin.run(['test.j2'], {}) # noqa
    assert result[0] == "foo"

# Generated at 2022-06-22 12:08:51.706828
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    def lookup_module_run(terms, variables, **kwargs):
        return LookupModule().run(terms, variables, **kwargs)

    terms = [
        "lookup_module_test_1.jinja",
        "lookup_module_test_2.jinja",
    ]

    variables = dict()

    assert lookup_module_run(
        terms=terms,
        variables=variables,
        template_vars={"varname": "value"},
    ) == [
        "foo=value\n",
        "bar=value\n",
    ]

    # test whether search path can be overridden via
    # ansible_search_path - test file lookup_module_test_3.jinja
    # should exist in the current working directory but not in
    # the search path's top directory
    search

# Generated at 2022-06-22 12:08:53.287485
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule().run(terms=['tests/test.tpl'], variables={}) == ['Hello World']

# Generated at 2022-06-22 12:08:53.784489
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-22 12:09:02.583504
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    l = LookupModule()
    l.set_loader({'_get_file_contents': lambda x: (b'{ "a": "b", "c": "d" }', None)})

    def tmpl(str, **kwargs):
        return AnsibleEnvironment(variable_start_string=kwargs.get('variable_start_string', None),
                                  variable_end_string=kwargs.get('variable_end_string', None),
                                  comment_start_string=kwargs.get('comment_start_string', None),
                                  comment_end_string=kwargs.get('comment_end_string', None)).from_string(str).render(kwargs)

    assert l._templar.template(tmpl("{{ a }}", a=1)) == "1"

# Generated at 2022-06-22 12:09:13.256167
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit test for method run of class LookupModule
    """
    m = LookupModule()

    def _fake_templar(context=None, convert_bare=True, preserve_trailing_newlines=False, escape_backslashes=False):
        """  Fake templar class for testing """
        self.assertEqual(context['static'], 'static')
        self.assertEqual(context['static_override'], 'static_override')
        self.assertEqual(convert_bare, False)
        self.assertEqual(preserve_trailing_newlines, True)
        self.assertEqual(escape_backslashes, False)
        return 'test_template_result'


# Generated at 2022-06-22 12:09:24.853587
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit test for method run of class LookupModule
    """
    # setup
    from ansible.plugins.loader import lookup_loader
    lookup_loader.add_directory(os.path.join(os.path.dirname(__file__), '..'))
    lookup_loader.set_global_vars({'foo': 'bar'})

    lookup_module = lookup_loader.get('template')

    # the variable setup may change over time, so let's check for a known variable value here
    assert 'bar' == lookup_module._templar.environment.available_variables['foo']

    # run
    result = lookup_module.run([os.path.join(os.path.dirname(__file__), '..', 'files', 'us-states.j2')], {})

    # test results
   

# Generated at 2022-06-22 12:09:29.995334
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lu = LookupModule()
    lu.set_options({})
    assert lu.run([to_bytes('/path/to/template.j2')], {}) == [to_bytes('the contents from the template')]

# Generated at 2022-06-22 12:10:02.032154
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    display = Display()
    display.vvvv = True  # Enable debug output
    lookup_args = {
        '_terms':         ['../../../library/template_tests/template_examples/test.j2'],
        'variable_start_string': '{{',
        'variable_end_string': '}}',
        'jinja2_native': False,
        'template_vars': {
            'port': 8080
        },
        'convert_data': False
    }
    # variables must be valid YAML
    variables = {
        'ansible_search_path': ['../../../']
    }
    # Test the method run of LookupModule
    print('Test function run of class LookupModule')
    print('')

    lookup_instance = LookupModule()
    result = lookup_instance

# Generated at 2022-06-22 12:10:12.775412
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    if USE_JINJA2_NATIVE:
        from ansible.utils.native_jinja import NativeJinjaText

    # Compose a mock templar object
    fake_templar = MockTemplar()

    # Compose a mock ansible_search_path variable
    fake_vars = {'ansible_search_path': None}

    # Compose a list of fake terms
    terms = [u'./some_template1.j2', u'./some_template2.j2']

    # Compose a lookup module object
    lookup_module = LookupModule()

    # Test on the method run of class LookupModule
    result = lookup_module.run(terms, fake_vars, convert_data=False, jinja2_native=False)


# Generated at 2022-06-22 12:10:24.077057
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a lookup module
    lookup = LookupModule()

    # Create a dict that contains the name of a file to use in the test
    # and the expected result of the test
    test_data = {
        'foo': 'results of foo',
        'bar': 'results of bar',
        'bleh': 'results of bleh',
    }

    # Create a dict that contains the name of each file and the contents of
    # that file
    test_files = {}
    for test_file in test_data:
        test_files[os.path.join(os.path.dirname(__file__), test_file)] = test_data[test_file]

    # Create a dict that contains the name of each file that should not pass
    # the test
    test_fail = []

    # Create a dict that contains the variables

# Generated at 2022-06-22 12:10:24.891767
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert False

# Generated at 2022-06-22 12:10:35.103337
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.plugins.loader import lookup_loader
    import yaml


# Generated at 2022-06-22 12:10:42.860594
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Object instantiation
    obj = LookupModule()

    # Object property assignments
    obj._loader
    obj._templar
    obj._display
    obj._options
    obj._terms
    obj._ds

    # Method calls
    obj.run(['index.html.j2'], True)
    obj.set_options()
    obj.get_option('convert_data')
    obj.get_option('template_vars')
    obj.get_option('jinja2_native')
    obj.get_option('variable_start_string')
    obj.get_option('variable_end_string')
    obj.get_option('commen_start_string')
    obj.get_option('commen_end_string')

# Generated at 2022-06-22 12:10:47.565604
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a mock object which will be called later
    class LookupModule_run_terms_mock: pass
    class LookupModule_run_variables_mock: pass
    class LookupModule_run_kwargs_mock: pass
    class LookupModule_run_ret_mock: pass
    class LookupModule_run_res_mock: pass
    def find_file_in_search_path(variables, *arg): pass
    class LookupModule_run_AnsibleEnvironment_mock: pass
    class LookupModule_run_templar_mock:
        def __init__(self, *arg): pass
        def copy_with_new_env(self, *arg): return LookupModule_run_templar_mock()

# Generated at 2022-06-22 12:10:58.724686
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.template import Templar
    from ansible.utils.display import Display

    display = Display()
    display.verbosity = 3

    inventory = InventoryManager(loader=DataLoader(), sources=['localhost,'])
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)

    templar = Templar(loader=DataLoader(), variables=variable_manager)

    testfile = os.path.join(os.path.dirname(__file__), 'test_template.j2')
    element = 'test_template.j2'
    variables = {}

    term = [element]

    lmodule = LookupModule()


# Generated at 2022-06-22 12:11:07.232596
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    yaml_fixture = '''
---
name: test
status: true
children:
    - { name: "child1", status: "active" }
    - { name: "child2", status: "active" }
'''

    jinja2_template = '''
<%
    obj = {
        "name": "default_name",
        "status": false,
        "children": []
    }
%>
{{ obj|combine(lookup("template", "fixture.yaml"))|to_json }}
'''

    env = dict()
    env.update(generate_ansible_template_vars('fixture.j2', 'fixture.j2'))
    data = dict()

    templar = AnsibleEnvironment(loader=None)