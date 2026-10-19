

# Generated at 2022-06-22 12:01:15.433043
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import binary_type
    from ansible.module_utils.six.moves import builtins
    from ansible.utils.hashing import secure_hash

    # Assert basics (not run against real files)
    assert isinstance(LookupModule.run(None, None, terms=['a', 'b']), list)
    assert LookupModule.run(None, None, terms=['a', 'b']) == []

    # Assert importing and loading
    import os.path as osp
    basepath = osp.dirname(osp.abspath(__file__))
    filepath = osp.normpath(osp.join(basepath, '..', '..', '..', '..', 'hacking', 'byte-compile'))
    filepath_ext = osp

# Generated at 2022-06-22 12:01:25.467218
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module._templar.environment.loader.list_templates = lambda path: [path + "/a"]
    lookup_module._templar.environment.get_template = lambda path: path.split("/")[-1]
    lookup_module.find_file_in_search_path = lambda variables, searchpath, term: "/foo/bar/" + term
    lookup_module._loader._get_file_contents = lambda path: ("{{ lookup('env','HOSTNAME') }}", path)

    assert lookup_module.run(["a"], dict(ansible_play_hosts="localhost")) == ["localhost"]

# Generated at 2022-06-22 12:01:35.000530
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    module = LookupModule()

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['.'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    module._templar = variable_manager.get_default_templar()
    module._loader = loader
    module.set_options(var_options=variable_manager._extra_vars)
    module._templar.environment.loader = module._loader

    print(module.run(["{{ansible_hostname}}"], {}))

# Generated at 2022-06-22 12:01:41.097400
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    L = LookupModule()

    # No file matching the given term echo
    assert L.run(['echo'], {}) == []

    # File matching the term test_dir/test_file.j2 exists.
    # This test does not work.
    # assert L.run(['test_dir/test_file.j2'], {'ansible_search_path': ['.']}) == ['This is a test\n']

# Generated at 2022-06-22 12:01:48.335214
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()

    # No files found
    lookup_plugin.set_loader('some_loader')
    lookup_plugin.set_environment({'some': 'env'})
    lookup_plugin.set_templar({'some': 'templar'})
    terms = ['./some_template.j2']
    variables = {'ansible_search_path': ['/tmp/data/']}
    lookup_plugin.run(terms, variables)
    assert True

# Generated at 2022-06-22 12:01:59.836018
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit test for method run of class LookupModule
    Returns: None

    """
    # Create instance of class LookupModule
    lookup_module = LookupModule()

    # Create test directory and file
    import tempfile
    from os import remove
    from os.path import exists
    with tempfile.NamedTemporaryFile() as f:
        with open(f.name, "w") as template_file:
            template_file.write('hello {{ whoami }}')
        template_file.close()
        file_name = f.name
    terms = [file_name]
    variables = dict(whoami='naeba')
    results = lookup_module.run(terms, variables)
    assert len(results) == 1
    assert results[0] == 'hello naeba'
    # Remove temporary file
   

# Generated at 2022-06-22 12:02:12.109310
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import lookup_loader
    from ansible.utils.display import Display
    from ansible.plugins.loader import module_loader

    display = Display()
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory_manager = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager.set_inventory(inventory_manager)

    OptionsModule = module_loader.get('debug', class_only=True)
    options = OptionsModule()



# Generated at 2022-06-22 12:02:13.014972
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO
    pass

# Generated at 2022-06-22 12:02:24.827335
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module_name = 'template'
    lookup_plugin = __import__('ansible.plugins.lookup.%s' % module_name, fromlist=[module_name])
    lm = lookup_plugin.LookupModule()

    data = '{{ foo }} bar {{ baz }}'
    terms = [ './files/foo.j2' ]
    variables = { 'foo': 'FOO', 'baz': 'BAZ' }

    ret = lm.run(terms, variables=variables, convert_data=False, jinja2_native=False)
    assert 'FOO bar BAZ' == ret[0]

    ret = lm.run(terms, variables=variables, convert_data=True, jinja2_native=False)
    assert 'FOO bar BAZ' == ret[0]

    ret

# Generated at 2022-06-22 12:02:36.697878
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import lookup_loader

    # create an empty environment and set some variables
    env = dict()
    env['_terms'] = './tests/test_lookup_template.j2'
    env['convert_data'] = True
    env['jinja2_native'] = False
    env['variable_start_string'] = '{{'
    env['variable_end_string'] = '}}'
    env['comment_start_string'] = '{#'
    env['comment_end_string'] = '#}'
    env['template_vars'] = {}
    env['playbook_dir'] = './'
    env['template_dir'] = './templates'

    # build the lookup module
    lookup_plugin_class = lookup_loader.get('template')

# Generated at 2022-06-22 12:02:49.478701
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = AnsibleModule(
        argument_spec={
            "terms": {"type": "list", "required": True},
            "is_json": {"type": "bool", "required": False},
        }
    )

    class FakeLoader():
        def __init__(self):
            self.path_sep = os.path.sep
            self.paths = None

        def _get_file_contents(self, path):
            return "mock", True

    class FakeVars():
        def __init__(self):
            self.ansible_search_path = []

    from ansible.template import Templar
    from ansible.template import AnsibleEnvironment
    templar = Templar(loader=FakeLoader(), variables=FakeVars())

# Generated at 2022-06-22 12:03:02.041470
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit test for the run method of the LookupModule class
    """
    from ansible.compat.tests.mock import patch, Mock
    from ansible.compat.tests.mock import create_autospec
    from ansible.template import Templar
    from ansible.vars import VariableManager

    # Preparation - Create a mocked templar object and fill it with some default values
    mocked_templar = create_autospec(Templar)
    mocked_templar._available_variables = {'test_variable': 'Test', 'test_variable2': 'Test2'}
    mocked_templar.environment.loader = Mock()

    # Mock the find_file_in_search_path method

# Generated at 2022-06-22 12:03:12.665849
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    env = dict()
    data = '/path/to/file'

    # Test with default values of options.
    ret = module.run([data], env)
    assert ret == [to_bytes('\n')]

    # Test with empty values
    ret = module.run(None, env)
    assert ret == []
    ret = module.run([], env)
    assert ret == []

    # Test with invalid term
    ret = module.run([1, 2, 3], env)
    assert ret == [1, 2, 3]

    # Test with more than one term.
    ret = module.run([data, data], env)
    assert ret == [to_bytes('\n'), to_bytes('\n')]

# Generated at 2022-06-22 12:03:22.401690
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # verify that the method does not raise exception when called with expected parameters
    from ansible.template import AnsibleEnvironment
    from ansible.parsing.vault import VaultLib
    from ansible.plugins.lookup import LookupBase
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.vars.reserved import Reserved

    def get_file_contents(path, vault_password=None, convert_data=False):
        return b"", True

    def set_loader(loader):
        return

    def copy_with_new_env(environment_class=AnsibleEnvironment):
        return

    def getattr(attr):
        if attr == "vars":
            return {}
        elif attr == "templar":
            return {}

# Generated at 2022-06-22 12:03:33.196424
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    display.verbosity = 2
    display.debug = True
    display.deprecated = True

    yaml_data = '''
    foo:
        bar: >
            this is a multiline string
        qux:
            - a
            - b
            - c
    '''
    yaml_template = '''
    {% raw %}
    {{ qux[1] }}
    {% endraw %}
    '''

    # normal behaviour
    test_lookup = LookupModule()
    results = test_lookup._loader.load_from_file('yaml_data', to_bytes(yaml_data))
    yaml_vars = results.get_data()
    results = test_lookup._loader.load_from_file('yaml_template', to_bytes(yaml_template))

# Generated at 2022-06-22 12:03:42.628099
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookupModule = LookupModule()

    # test Yaml:
    terms = """[local_action]\n
- name: get file contents\n
  setup: all\n
  register: myfiles\n
- name: show templating results\n
  debug: var=item\n
with_fileglob:\n
  - /etc/hosts\n
  - /etc/resolv.conf\n\n
"""
    # for len(ret) > 0, the ret should be a list, like this

# Generated at 2022-06-22 12:03:52.026615
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Dummy class that simulates AnsibleOptions class
    class AnsibleOptionsMock(object):
        """
            Fake class that simulates AnsibleOptions
        """

        def __init__(self, ansible_vars):
            """
                Method that init AnsibleOptionsMock class

                Args:
                    ansible_vars (dict): Ansible variables to simulate

                Returns:
                    None
            """
            self.ansible_vars = ansible_vars

    # Class that simulates file module
    class FileModuleMock(object):
        """
            Fake class that simulates file module
        """

        # Public class attributes
        search_path = []
        file_name = ''
        content = ''


# Generated at 2022-06-22 12:04:03.372539
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode, AnsibleVaultEncryptedString
    import yaml
    import os

    default_vars = dict()

    def test_data(x):
        return to_text(yaml.safe_dump(x), errors='surrogate_or_strict')

    # Test with convert_data=False
    terms = ['/home/ansible/template.j2']
    # given /home/ansible/template.j2 contains "{{ test }}"
    test_var = dict(test='test1')
    # dict is converted to string for the lookup
    default_vars['test_var'] = test_

# Generated at 2022-06-22 12:04:12.425391
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    ######################################################################
    # check exception when the file is not found
    ######################################################################
    # set find_file_in_search_path return value
    def find_file_in_search_path(variables, subdirs, file_name):
        return None
    lookup_module.find_file_in_search_path = find_file_in_search_path
    # set _loader._get_file_contents return value
    def _get_file_contents(file_name):
        return None, None
    lookup_module._loader._get_file_contents = _get_file_contents
    lookup_module._templar = None
    lookup_module._loader = None

# Generated at 2022-06-22 12:04:24.169821
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Test of method run of class LookupModule
    """
    test_module = LookupModule()
    test_module.set_options({'convert_data': False, 'template_vars': {'one': 'foo', 'two': 'bar'}, 'jinja2_native': False,
                             'variable_start_string': '[%', 'variable_end_string': '%]',
                             'comment_start_string': '[#', 'comment_end_string': '#]'})
    test_module._templar = AnsibleEnvironment().get_template_class().from_module_vars(ansible_version='2.12')
    test_module._templar._basedir = '/'
    test_module._loader = None
    test_module._display = Display()
    test_module._display.verb

# Generated at 2022-06-22 12:04:45.633761
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''Unit test for method run of class LookupModule'''
    # Create a class object with required arguments
    lookup_obj = LookupModule()
    # Create a variable for Ansible Variable for passing it as an argument
    variable_obj = ansible.vars.AnsibleVariableManager()
    variable_obj.extra_vars = {'i_am_a_variable': 'i_am_a_value'}
    # Create a variable for Ansible Options for passing it as an argument
    options_obj = ansible.options.Options()
    options_obj.connection = 'local'
    options_obj.module_path = None
    options_obj.forks = 1
    options_obj.become = None
    options_obj.become_method = None
    options_obj.become_user = None
    options_

# Generated at 2022-06-22 12:04:56.576835
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class Templar(object):
        def __init__(self, env=None):
            self.env = env

        def set_temporary_context(self, **kwargs):
            self.env = kwargs

        def copy_with_new_env(self, environment_class):
            return Templar(self.env)

    class Environment(object):
        pass

    class DummyTerm(object):
        def __init__(self):
            self.results = None

        def run(self, *args, **kwargs):
            self.results = [
                {'terms': ['a.j2'], 'variables': {'search_path': ['/bogus']}, 'direct': {'lookup_template_vars': {'template_var': 'template val'}}},
            ]
            return self.results

# Generated at 2022-06-22 12:05:04.163345
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ["../tests/test_lookup_plugin_template.j2"]
    variables = {"template_host": "test_host", "ansible_distribution": "test_distribution"}
    result = lookup.run(terms=terms, variables=variables)
    assert isinstance(result, list)
    assert result[0] == 'template_host=test_host Distribution: test_distribution'

# Generated at 2022-06-22 12:05:11.735727
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_dict = {"something": 123,
                 "var_name": "ansible",
                 "other": {"myvar1": "foo", "myvar2": "bar"},
                 "list": [1, 2, 3],
                 "listofdicts": [{"foo": 1}, {"bar": 2}]}

    lookup_plugin = LookupModule()

    # Test the case where template_vars is empty
    elem = lookup_plugin.run(["test_templates/test_lookup_template.j2"], test_dict,
                             variable_start_string='[%', variable_end_string='%]',
                             comment_start_string='[#', comment_end_string='#]')
    assert elem == ["[%  %]\n[% ansible %]\n[% foo %]\n"]

# Generated at 2022-06-22 12:05:20.983875
# Unit test for method run of class LookupModule
def test_LookupModule_run():
  lk = LookupModule()
  lk.set_loader(DictDataLoader({}))
  lk._templar.set_available_variables(dict(ansible_search_path=['templates'],
                                           ansible_managed='Test the template lookup',
                                           self='test'))
  terms = [
    './test/template.j2',
  ]
  res = lk.run(terms=terms, variables={})
  assert len(res) == 1, "Expected only one result"
  assert to_text(res[0]) == to_text("Hello world\n")

# Generated at 2022-06-22 12:05:33.251711
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import sys # required to mock sys.stdout
    import sys
    import os
    import pytest
    import yaml

    # Mock the module_utils._text class
    def to_bytes(a, errors):
        return to_text(a, errors).encode('utf-8')
    def to_text(a, errors):
        return a
    import ansible.module_utils._text as _text
    _text.to_text = to_text
    _text.to_bytes = to_bytes

    # Mock the ansible.utils.display class
    class DisplayClass:

        def __init__(self):

            self.fp = sys.stdout

        def __getattr__(self, attr):

            return getattr(self.fp, attr)


# Generated at 2022-06-22 12:05:41.500990
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Initialise object of class LookupModule
    lookupModule = LookupModule()

    jinja2_template = """
                <html>
                <head>
                  <title>Example Page</title>
                </head>
                <body>
                  <p>This is a sample HTML page.</p>
                </body>
                </html> """
    # Test run method with non-existent template filename
    terms = "non-existent-template-file"

    # Deprecated fixture, left for backwards compatibility
    variables = {}

    options = {'_ansible_vault': None, 'convert_data': None, 'template_vars': None, 'jinja2_native': False}
    with pytest.raises(AnsibleError) as excinfo:
        lookupModule.run(terms, variables, **options)
       

# Generated at 2022-06-22 12:05:52.038649
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # create mock object for the lookbase
    # create mock object for the display
    # create mock object for the loader
    # create mock object for the templar
    # create mock object for the file_find
    # create mock object for the safe_eval
    # create mock object for the utils
    # create mock object for the random
    # create mock object for the templatevars
    # create mock object for the playbook
    # create mock object for the ansible_vars
    # create mock object for the template_data
    # create mock object for the terms
    # create mock object for the variables
    lookupBase = LookupBase()
    display = Display()
    loader = AnsibleLoader()
    templar = AnsibleTemplar()
    fileFind = fileFind()
    safeEval = safeEval()

# Generated at 2022-06-22 12:06:01.602520
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import lookup_loader
    import ansible.constants as C
    import json

    def get_loader(loader):
        return DataLoader(C.DEFAULT_LOADERS_PATH_PREFIX).load_from_file("yaml", 'targets.yml')

    loader = get_loader("loader")
    tqm = TaskQueueManager(loader=loader, stdout_callback=None, run_tree=False)
    play_context = PlayContext()
    play_context.network_os = 'ios'
    play

# Generated at 2022-06-22 12:06:09.126109
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Test the module LookupModule"""

    import pytest

    lookup_module = LookupModule()
    lookup_module.set_loader({'_get_file_contents' : lambda x: (b'some text', None)})

    # test with term as a file path
    lookup_module._templar.set_available_variables(dict(inventory_dir='/some/dir'))
    assert lookup_module.run(['/some/dir/path/to/file.j2'], {}) == ['some text']

    # test with term as a relative path
    lookup_module._templar.set_available_variables(dict(inventory_dir='/some/dir'))
    assert lookup_module.run(['relative/path/to/file.j2'], {}) == ['some text']

# Generated at 2022-06-22 12:06:33.648645
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['test_template.j2']

# Generated at 2022-06-22 12:06:39.351749
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    # Test error cases
    with pytest.raises(AnsibleError) as excinfo:
        lookup_module.run(terms=['test/data/not_exist.j2'], variables=dict())
    assert 'could not be found for the lookup' in str(excinfo.value)

# Generated at 2022-06-22 12:06:47.687587
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Given
    data = {
        'msg': '{{ lookup("template", "./some_template.j2") }}',
        'msg_with_start_end_string': '{{ lookup("template", "./some_template.j2", variable_start_string="[%", variable_end_string="%]") }}',
        'msg_with_comment_start_end_string': '{{ lookup("template", "./some_template.j2", comment_start_string="[#", comment_end_string="#]") }}',
    }

# Generated at 2022-06-22 12:06:59.427002
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.parsing.dataloader import DataLoader
    import os


# Generated at 2022-06-22 12:07:08.271072
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # create empty dict
    options = {}

    # create empty dict
    variables = {}

    # create list
    terms = ["ansible.cfg"]

    # create mock
    old_loader = LookupBase.get_loader(None)

    # create mock
    old_templar = LookupBase.get_templar(None)

    # create lookup module
    lookup_module = LookupModule()

    # call run of lookup module
    lookup_module.run(terms, variables, **options)

    # check result
    assert lookup_module.run(terms, variables, **options)

# Generated at 2022-06-22 12:07:18.396997
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()

    searchpath = [os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, 'library')]
    module_utils = [os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir, 'module_utils')]
    ansible_paths = ':'.join(searchpath + module_utils)
    os.environ['ANSIBLE_LIBRARY'] = ansible_paths

    assert lookup_plugin.run(["lookup_template_test.j2"], dict(ansible_search_path=searchpath)) == [u"1\n2\n3\n"]

# Generated at 2022-06-22 12:07:23.510534
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # a normal case test, pass a ansible repo file path to it
    lookupModule = LookupModule()
    lookupModule.set_options(dict(variable_start_string="${",variable_end_string="}"))
    term = "../../lib/ansible/inventory/group_vars/all"
    lookupModule.run(terms=[term], variables={})

# Generated at 2022-06-22 12:07:34.365176
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup_module = LookupModule()
    lookup_module.set_runner()

    # 1st test
    terms = ["./vars/test_var.yml"]
    variables = {"test_var": "My_Name"}
    result = lookup_module.run(terms, variables)

    assert result == ["My_Name\n"], "should be ['My_Name\n'] but is %s" % result

    # 2nd test
    terms = ["./vars/test_var.yml"]
    variables = {"test_vars": "My_Name"}
    result = lookup_module.run(terms, variables)

    assert result == ["My_Name\n"], "should be ['My_Name\n'] but is %s" % result

# Generated at 2022-06-22 12:07:44.252768
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    import os
    import sys

    if not os.path.exists("./test/lookup_plugins/files/test_template"):
        os.makedirs("./test/lookup_plugins/files/test_template")
    data = u'#jinja2:variable_end_string:\'}}\''
    with open("./test/lookup_plugins/files/test_template/test.j2", 'w') as f:
        f.write(data)


# Generated at 2022-06-22 12:07:47.015396
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test for method run (2/2)
    # This is a stub, used to test AnsibleModule#fail_json
    return {'msg': 'No tests written'}

# Generated at 2022-06-22 12:08:37.981782
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # setup
    class MockTemplar():
        def template(self, template_data, preserve_trailing_newlines=True, convert_data=False, escape_backslashes=False):
            return 'some_return_value'


    class TestLookupModule(LookupModule):
        def __init__(self):
            self._loader = None
            self._templar = MockTemplar()
            self.display = Display()

        def find_file_in_search_path(self, variables, path, term):
            return 'some_file'

        def _get_file_contents(self, file):
            return 'some_data'

    test_obj = TestLookupModule()

    # test

# Generated at 2022-06-22 12:08:45.435412
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    kwargs = {'convert_data': True, 'comment_start_string': '--', 'template_vars': {'var1': {'var11': 11}}, 'comment_end_string': '', 'jinja2_native': False, 'variable_start_string': '{', 'variable_end_string': '}'}
    templater = LookupModule()
    templater.set_loader(None)
    templater.set_environment(None)

    terms = ['test1.j2']
    variables = {'var1': {'var11': 11}, 'var2': 2}

    ret = templater.run(terms, variables, **kwargs)
    assert ret == [u'{ var1.var11}']


# Generated at 2022-06-22 12:08:49.803974
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    try:
        lm.run('terms', 'variables', convert_data = True, jinja2_native = True)
    except Exception as e:
        raise Exception("Unexpected exception raised: " + str(e)) from e
    return True

# Generated at 2022-06-22 12:08:51.884111
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # For now, the unit tests are moved to test/units/plugins/lookup/test_template.py
    pass

# Generated at 2022-06-22 12:09:03.605154
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test valid input
    lookup = LookupModule()
    terms = ['./test_template.j2']
    variables = {'var1': 'value1', 'var2': 'value2'}
    kwargs = {'convert_data': True, 'template_vars': {'var3': 'value3', 'var4': 'value4'}}
    lookup.set_loader(None)
    lookup._templar.set_available_variables(variables)
    ret = lookup.run(terms, variables, **kwargs)
    assert isinstance(ret, list)
    assert len(ret) == 1
    assert isinstance(ret[0], str)

# Generated at 2022-06-22 12:09:14.340690
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import datetime
    import textwrap
    import json
    import sys
    import types

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.utils.display import Display

    display = Display()
    display.verbosity = 6
    loader = DataLoader()
    variables = VariableManager()

    lookup_plugin = LookupModule()

    # Make sure the YAML library supports falt syntax for strings
    yaml_string = "Hello world"
    if yaml_string != json.dumps(yaml_string):
        pyyaml_error = "The installed version of the PyYAML library does not support the flat loader."

# Generated at 2022-06-22 12:09:17.922203
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # pylint: disable=protected-access
    lookup = LookupModule()

    assert lookup.run(terms=['/path/to/template.j2'],
                      variables={}) == \
    [u'Hello World!']

# Generated at 2022-06-22 12:09:28.109019
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['./foo/bar/baz.j2', './foo/bar/foo.j2']
    variables = {'test': 'test', 'test2': 'test2'}
    options = {'convert_data': True, 'template_vars': {'test': 'test', 'test2': 'test2'}, 'jinja2_native': False,
            'variable_start_string': False, 'variable_end_string': True} #, 'comment_start_string': False, 'comment_end_string': True}
    lookup_module = LookupModule()
    results = lookup_module.run(terms, variables, **options)
    assert (results == ["foo", "foo"])

# Generated at 2022-06-22 12:09:38.584941
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create simple template file
    template_file = 'simple_template.j2'
    with open(template_file, 'w') as f:
        f.write('Hello World!\n')

    # Create a temporary AnsibleContext object
    context = AnsibleContext()

    # Create a temporary LookupModule object
    lm = LookupModule()

    # Create fake search path
    search_path = {'paths': [os.getcwd()]}
    search_path['paths'].append(os.path.join(os.getcwd(), 'templates'))
    context.set_context({'ansible_search_path': search_path['paths']})

    # Apply the lookup plugin

# Generated at 2022-06-22 12:09:47.050450
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import pytest

    lookup_module = LookupModule()
    lookup_module.set_loader('/home/user1/ansible/plugins/lookup_plugins/template.py')
    lookup_module._loader.set_basedir('/home/user1/ansible/playbooks')

    # first test
    lookup_parameters = {'convert_data': True, 'template_vars': {'foo': 'bar'}, 'jinja2_native': False, 'variable_start_string': '{{', 'variable_end_string': '}}', 'comment_start_string': None, 'comment_end_string': None}
    lookup_module.set_options(lookup_parameters)
    terms = ['../lookup_plugins/all.py']
    variables = {}

    # expected result of the test
    expected_