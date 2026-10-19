

# Generated at 2022-06-22 12:01:16.131510
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # NOTE: the LookupModule class is effectively an abstract base class,
    #       it cannot be instantiated directly, thus the class cannot be
    #       properly unit tested.  This test method was a proof-of-concept
    #       to ensure that individual methods of the class could be tested.
    #       That being said, this method is being left in the codebase as a
    #       reference in case more direct testing of the class is ever needed.

    # Create an instance of the class so we can access the run method.
    import ansible.plugins.loader
    lm = ansible.plugins.loader.lookup_loader.get('template', class_only=True)()

    # Define the terms and variables that would be passed as args to the method.
    terms = "{{ lookup('template', './some_template.j2') }}"
   

# Generated at 2022-06-22 12:01:28.698274
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import sys
    import tempfile

    # prepare a source file for a test
    test_dir = tempfile.mkdtemp()
    test_file_path = os.path.join(test_dir, "test.j2")
    test_file_content = u"Test string: {{ test_var }}"
    with open(test_file_path, "wb") as f:
        f.write(test_file_content.encode('utf-8'))

    # prepare a test environment
    module_utils_path = os.path.dirname(sys.modules['ansible'].__file__)
    module_utils_path = os.path.join(module_utils_path, 'module_utils')
    sys.path.insert(0, module_utils_path)

# Generated at 2022-06-22 12:01:38.019137
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    # We don't have plugins/lookup/template.py, so the plugin cannot work
    # and will return an error

    # Test with empty options
    with pytest.raises(AnsibleError):
        lookup_module.run(
            terms=['template/test.j2'],
            variables={}
        )

    # Test with no default options
    with pytest.raises(AnsibleError):
        lookup_module.run(
            terms=['template/test.j2'],
            variables={},
            _templar=False,
            _loader=False,
        )

# Generated at 2022-06-22 12:01:44.523983
# Unit test for method run of class LookupModule

# Generated at 2022-06-22 12:01:56.418661
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Case: These conditions are expected to be true.
    # Case: get_option method successfully.
    # Case: find_file_in_search_path method successfully.
    # Case: _get_file_contents method successfully.
    lookup_module = LookupModule()
    lookup_module.set_loader(FakeLoader())
    result = lookup_module.run(['./some_template.j2'], {'variable': 'value', 'ansible_search_path': ['/etc/ansible']})
    assert type(result) is list
    assert len(result) == 1
    assert result[0] == 'successful'

# Generated at 2022-06-22 12:02:06.041993
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Tests the method run of class LookupModule
    # Unit test for method run of class LookupModule
    lookup_mock = LookupModule()

    # test missing template
    with pytest.raises(AnsibleError, match='template file test could not be found'):
        lookup_mock.run([], {}, 'templates', 'test')

    # test templates directory in search path
    lookup_mock.run([], {}, 'templates', 'templates_dir')

    # test templates directory in search path
    lookup_mock.run([], {}, 'templates', 'relative')

# Generated at 2022-06-22 12:02:15.917045
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # These arguments are named to match the parameters
    # of the plugin for the sake of clarity
    # It is the responsibility of the test to ensure that
    # the plugin is using them properly
    terms = [
        "./some_template.j2"
    ]
    variables = {
        'template_path': 'templates/',
        'foo': 'bar',
        'var': {
            'a': 'b'
        }
    }

# Generated at 2022-06-22 12:02:27.592670
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test with parameter comment_end_string
    module = LookupModule()
    # comment_start_string default is '{#'
    assert module.run(terms=['./some_template.j2'], variables={}, comment_end_string='#}') == ['{{ test }}\n']

    # Test with parameters convert_data and jinja2_native
    module = LookupModule()
    # convert_data = False
    # jinja2_native = False
    assert module.run(terms=['./some_template.j2'], variables={}, convert_data=False, jinja2_native=False) == ['{{ test }}\n']
    module = LookupModule()
    # convert_data = False
    # jinja2_native = True

# Generated at 2022-06-22 12:02:38.922410
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_mock_class = LookupBase()
    lookup_mock_class.set_loader({'paths': ['/etc/ansible/playbooks']})
    lookup_mock_class._templar = AnsibleEnvironment()
    lookup = LookupModule(loader=None, templar=None, shared_loader_obj=lookup_mock_class)
    lookup._templar = lookup_mock_class._templar
    lookup._loader = lookup_mock_class._loader
    lookup.set_options({'variable_start_string': '[%', 'variable_end_string': '%]'})

    results = lookup.run(['ansible'], {'inventory_hostname': 'host1', 'inventory_hostname_short': 'host1'})

# Generated at 2022-06-22 12:02:50.438323
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    lookup.set_loader(module_loader)
    lookup._templar = templar

    # Empty terms should raise an error
    terms = []
    variables = dict()
    try:
        ret = lookup.run(terms, variables)
    except AnsibleError as e:
        assert e.message == 'with_template: template file argument is required'
    else:
        raise AssertionError("AnsibleError not raised")

    # Invalid paths should raise an error
    terms = [
        "/foo/bar/baz.j2",
        "baz.j2",
    ]
    variables = dict()

# Generated at 2022-06-22 12:03:10.676889
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    import pytest

    loader = DataLoader()
    variables = VariableManager(loader=loader)

    basedir = 'tests/lookup_plugins/'

    def _lookup_file_in_search_path(self, variables, dirname, filename):
        return basedir + filename

    ############################################################
    ### run method first test
    ############################################################
    templar = PlayContext()
    templar._loader = DataLoader()
    templar._loader.set_basedir(basedir)

# Generated at 2022-06-22 12:03:21.419995
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a mock environment
    mock_loader = 'foo'
    mock_templar = 'bar'
    mock_env = {'template_hostvars': {}, 'template_uid': 1000, 'template_path': '/bar/foo', 'template_mtime': 0}
    mock_basedir = '/foo'
    mock_vars = {'inventory_dir': '/foo', 'inventory_file': '/foo/bar'}

    test = LookupModule(loader=mock_loader, basedir=mock_basedir, env=mock_env, templar=mock_templar)
    test.set_options(direct={'variable_start_string': '{{', 'variable_end_string': '}}'})
    terms = ['./some_template.j2']

# Generated at 2022-06-22 12:03:32.805414
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing import DataLoader
    from ansible.playbook.play_context import PlayContext

    lookup = LookupModule()

    assert(lookup.run([], dict()) == [])
    assert(lookup.run(['test.j2'], dict()) == [])

    loader = DataLoader()
    loader.set_basedir('/tmp')
    context = PlayContext()
    lookup._loader = loader
    lookup._templar = context.templar

    with open('/tmp/test.j2', 'w') as f:
        f.write('data')
    assert(lookup.run(['test.j2'], dict()) == ['data'])
    os.remove('/tmp/test.j2')

    # we don't test the jinja2 templating by now

# Generated at 2022-06-22 12:03:42.429056
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    This is a unit test for the method LookupModule._run()
    """
    lookup_module = LookupModule()
    lookup_module._templar = Templar()
    lookup_module._loader = DictDataLoader({
        "hello.j2": "hello {{ name }}!",
        "bye.j2": "bye {{name}}",
        "backslash.j2": "\\"
    })
    lookup_module._display = Display()
    lookup_module.set_options({'variable_start_string': '[%',
                               'variable_end_string': '%]',
                               'comment_start_string': '',
                               'comment_end_string': ''})

# Generated at 2022-06-22 12:03:51.099458
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Set up class instance to test
    lookup_base = LookupBase()
    lookup_module = LookupModule()
    lookup_base.set_loader(None)
    lookup_base.set_templar(None)
    lookup_module._templar = None
    lookup_module._loader = None
    # Set up lookup_module with required mock attributes
    lookup_module._templar = MockTemplar()
    lookup_module._loader = MockLoader()

    # Generate return from method being tested
    ret = []
    terms = None
    variables = None
    kwargs = None
    ret = lookup_module.run(terms, variables, **kwargs)

    # Assert
    assert ret == [u'Test template']


# Generated at 2022-06-22 12:04:00.188480
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test data
    #
    # content of file/templates/test.j2
    template_content_1_0=to_bytes("""
    {% for i in range(0, 6) %}
    The current num is {{ i }}
    {% endfor %}
    """, encoding='utf-8')
    # expected output
    expected_1_0=to_bytes("""
    
    The current num is 0
    
    The current num is 1
    
    The current num is 2
    
    The current num is 3
    
    The current num is 4
    
    The current num is 5
    
    """, encoding='utf-8')
    #
    # content of file/templates/test2.j2

# Generated at 2022-06-22 12:04:10.447740
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.vault import VaultEditor

    secret_vault_password = "foo"
    vault_password_file = "/tmp/vault_password_file.txt"
    secrets_file = "/tmp/secrets.yml"
    template_file = "/tmp/template.j2"
    output_file = "/tmp/template.out"

    with open(vault_password_file, "w") as f:
        f.write(secret_vault_password)


# Generated at 2022-06-22 12:04:16.567024
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    assert module.run([], {}, convert_data="yes") == []
    assert module.run([], {}, convert_data="no") == []
    assert module.run([], {}, convert_data="True") == []
    assert module.run([], {}, convert_data="False") == []
    assert module.run([], {}, convert_data=1) == []


# Generated at 2022-06-22 12:04:27.903976
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import tempfile

    class Options(object):
        convert_data = False
        template_vars = {}
        jinja2_native = False
        variable_start_string = '{{'
        variable_end_string = '}}'
        comment_start_string = '{#'
        comment_end_string = '#}'

    opts = Options()

    # Create a temporary directory
    tmpdir = tempfile.mkdtemp()

    # Create a temporary file in the temporary directory
    tmplookupfile = tempfile.NamedTemporaryFile(dir=tmpdir, mode='w', delete=False)
    tmplookupfile.write("{{ lookup_file_content }}")
    tmplookupfile.close()

    # Create a temporary file in the temporary directory
    tmpfile

# Generated at 2022-06-22 12:04:34.530243
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import random
    terms = ['single_file.txt', 'single_file2.txt']
    variables = {'ansible_search_path': [['/foo/bar']]}
    plugin = LookupModule()
    plugin.set_loader(random.randint(0, 255))
    ret = plugin.run(terms, variables)
    assert(isinstance(ret, list))
    assert(ret[0] == 'this is a single file\n')
    assert(ret[1] == 'this is another single file\n')

# Generated at 2022-06-22 12:04:52.697699
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert USE_JINJA2_NATIVE

    lookup = LookupModule()
    lookup.set_loader(None)
    templar = None
    def get_loader(name):
        class Dummy:
            class _get_file_contents:
                @staticmethod
                def __call__(*args, **kwargs):
                    return to_bytes('foo', encoding='utf-8'), True
        return Dummy
    lookup._loader = get_loader('')
    def get_templar(environment_class=None):
        nonlocal templar
        class Dummy:
            class Searchpath:
                def __init__(self, searchpath):
                    self.searchpath = searchpath

# Generated at 2022-06-22 12:05:01.232702
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Instantiate modules.lookup
    import ansible.plugins.loader as plugins_loader
    _lookup_lookup = plugins_loader.lookup_loader._lookup_plugins['template']['obj']
    lookup_inst = _lookup_lookup()

    # Instantiate testing vars
    test_terms = ['ansible_template_test_terms.j2']
    test_variables = {'test': 'variable', 'test2': 'var2'}

    # Call the method run
    result = lookup_inst.run(test_terms, test_variables)

    # Assert result is not empty
    assert result

    # Assert result list contains just one element
    assert len(result) == 1

    # Assert result list contains the string

# Generated at 2022-06-22 12:05:01.920480
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert False

# Generated at 2022-06-22 12:05:10.561204
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # This tests a few things:
    """
    1. The lookup finds the file in the search path even when it is not the first path in the search path
    2. The lookup uses the variables in the templating correctly
    3. The lookup uses the options variable_start_string and variable_end_string in the templating correctly
    4. The lookup uses the options comment_start_string and comment_end_string in the templating correctly
    5. The lookup uses the options convert_data and jinja2_native in the templating correctly
    """

    # This is a lookup module for a lookup plugin, so it would seem that we could
    # just create a LookupBase object and call 'run'.  However, this doesn't work
    # because _templar is not an attribute.  There is no public interface to create
    # a lookup

# Generated at 2022-06-22 12:05:17.778003
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lu = LookupModule()
    lu.set_options({})
    assert lu._templar
    lu.set_loader({'_get_file_contents': lambda a, b: ('{\'a\':\'b\'}', True)})
    assert lu._loader
    assert lu.run(['test'], {'ansible_lookup_plugin': 'test'})

# Generated at 2022-06-22 12:05:30.753739
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    This test case checks the real behaviour of the module run method of
    LookupModule class.
    """
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    # create inventory, variable and play context
    variable_manager = VariableManager()
    loader = variable_manager.get_vars_loader()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager.set_inventory(inventory)
    play_context = PlayContext()
    variable_manager.set_play_context(play_context)

    template_data_source = '''
{% for item in items %}
{{ item }}
{% endfor %}
'''

    # create a new instance of LookupModule


# Generated at 2022-06-22 12:05:42.504350
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    # setup the context
    engine = DummyEngine(None)
    engine.get_context = Mock(return_value=Mock(**{
        'get_template_vars.return_value': {},
        'environment_class.return_value': AnsibleEnvironment,
        'environment.return_value': {},
        'variable_start_string.return_value': '{{',
        'variable_end_string.return_value': '}}',
        'comment_start_string.return_value': '{#',
        'comment_end_string.return_value': '#}',
    }))
    lookup_module._templar = engine
    lookup_module._loader = DummyLoader(None)

    # setup the test
    term = 'test_file_name'


# Generated at 2022-06-22 12:05:53.755593
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    variable_manager = VariableManager()

    loader = DataLoader()
    variable_manager.set_inventory(InventoryManager(loader=loader, sources=["tests/inventory"]))

    # Create test terms
    terms = [
        "unittest-terms-template.j2",
        "unittest-terms-template-with-lookup.j2",
    ]

    # Create test variables
    variables = {
        "test_variable": "a"
    }

    # Create test template variables

# Generated at 2022-06-22 12:06:02.282182
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    terms = [
        "./some_template.j2",
        "./other_template.j2"
    ]

    variables = {
        "template_vars": { "answer": 42 },
        "variable_start_string": "[%",
        "variable_end_string": "%]"
    }


# Generated at 2022-06-22 12:06:11.680271
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Init vars
    terms = ['some_template.j2']
    variables = {}
    kwargs = {'variable_start_string': "{{", 'variable_end_string': "}}", 'template_vars': {"key1": "value1"}}
    kwargs_empty = {}
    kwargs_wrong = {'invalid1': "invalid", 'invalid2': "invalid2"}
    kwargs_strange = {'variable_start_string': "{{", 'variable_start_string': "{{", 'template_vars': ""}

    # Init class
    lookup_plugin = LookupModule()

    # Check for empty kwargs
    result = lookup_plugin.run(terms, variables, **kwargs_empty)
    for item in result:
        assert item == "value1"

# Generated at 2022-06-22 12:06:33.765017
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    display = Display()
    display.verbosity = 4
    test_file_path = "/path/with/trailing/slash/"

    result = LookupModule.run(None, [test_file_path], None, **{
        "_loader": MockLoader({
            "path/with/trailing/slash/testfile": "test"
        }),
        "_templar": MockTemplar(),
        "_context": MockContext(),
        "convert_data": False,
        "template_vars": {},
        "jinja2_native": False,
        "variable_start_string": "{{",
        "variable_end_string": "}}",
        "comment_start_string": "{#",
        "comment_end_string": "#}",
    })

    assert(result == ["test"])



# Generated at 2022-06-22 12:06:45.112184
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    
    # Setup
    terms = ['/some/path/to/file.j2']
    variables = dict(
        ansible_search_path = ["/some/path", "/another/path"]
    )

    # Mock blueprint
    class Mock(LookupModule):
        def _initialize(self, *args, **kwargs):
            pass

        def find_file_in_search_path(self, *args, **kwargs):
            return '/some/path/to/file.j2'

        def _templar_convert_data(self, *args):
            return args
        
        def _templar_template(self, *args):
            return '/some/path/to/file.j2'

    # Mock class that returns a mocked loader

# Generated at 2022-06-22 12:06:52.921542
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.module_utils.module_replacer
    import ansible.module_utils.six
    from ansible.module_utils.six.moves import builtins
    from ansible.module_utils.six import BytesIO
    from ansible.module_utils import basic

    class Display(object):
        def __init__(self):
            pass

        def display(self, msg, color=None, stderr=False, screen_only=False, log_only=False):
            print(msg)

    display = Display()

    module_replacer = ansible.module_utils.module_replacer
    builtins.__dict__['display'] = display

# Generated at 2022-06-22 12:07:03.670932
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ['common.j2']
    variables = {
        'test_var': 'value_of_test_var',
        'test_dict': {'test_key': 'value_of_test_key'},
        'ansible_search_path': ['/data/ansible/playbooks']
    }

    # test_var
    result = lookup.run(terms, variables)
    assert isinstance(result, list), 'Value is not a list'
    assert len(result) == 1, 'Value is not a list with one item'
    assert result[0] == 'value_of_test_var', 'Value is not what we expected'

    # test_dict
    result = lookup.run(terms, variables, jinja2_native=True)

# Generated at 2022-06-22 12:07:15.468321
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    # Create objects required by the lookup module

    # Create ansible variable manager
    variable_manager = VariableManager()

    # Create ansible data loader
    loader = DataLoader()

    # Create ansible inventory manager
    inventory = InventoryManager(loader=loader)

    # Create ansible play

# Generated at 2022-06-22 12:07:27.077674
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    name = 'test_LookupModule_run'

    # Setup
    # FIXME:
    # - Replace `ANSIBLE_LIBRARY_LOOKUPS` with `ANSIBLE_LIBRARY_LOOKUPS` and
    #   remove the `mkstemp` call once Ansible 2.4 support is dropped.
    # - Use `fixture_loader` once we have one. Also update the test to use it.
    from ansible.constants import ANSIBLE_LIBRARY_LOOKUPS
    from tempfile import mkstemp
    os_fd, lookup_file = mkstemp(prefix='ansible_test_lookup_plugin_%s_' % name)
    with os.fdopen(os_fd, 'w') as f:
        f.write('{{ foo }}\n')
    template_file

# Generated at 2022-06-22 12:07:31.245594
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """ Unit test for method run of class LookupModule """
    lookup_module = LookupModule()
    assert hasattr(lookup_module, 'run')
    assert callable(getattr(lookup_module, 'run'))

# Generated at 2022-06-22 12:07:38.508850
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import sys

    module_path = os.path.dirname(os.path.abspath(sys.modules[LookupModule.__module__].__file__))
    data_dir = os.path.join(module_path, '..', '..', 'data')

    variabes = dict(
        languages_path=data_dir,
        languages_count=3)

    terms = ['files_with_variable.yml']

    lookup_plugin = LookupModule()
    res = lookup_plugin.run(terms, variabes)

    assert res == [u'foo\nbar\nbaz\n']

# Generated at 2022-06-22 12:07:42.587580
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module._loader.set_basedir("/root")
    lookup_module._templar.set_available_variables(dict(a=10, b=20))
    assert lookup_module.run(["test_template.j2"], dict()) == [u"1020"]

# Generated at 2022-06-22 12:07:53.837762
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def _get_terms():
        return (
            to_bytes('test.j2'),
        )
    def _get_variables():
        return {
            'convert_data': True,
            'template_vars': {
                'some_var': 'some_var_value'
            },
            'jinja2_native': False,
            'variable_start_string': '{{',
            'variable_end_string': '}}',
            'comment_start_string': '{#',
            'comment_end_string': '#}',
        }

# Generated at 2022-06-22 12:08:22.582875
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os

    os.environ['DAMIAA_INVENTORY_DIR'] = '/tests/inventory'

    import ansible.plugins.lookup.template as lookup
    lookup_obj = lookup.LookupModule()
    terms = ['/tests/templates/template.j2']
    variables = {}
    direct = {}
    lookup_obj.set_options(var_options=variables, direct=direct)
    res = lookup_obj.run(terms, variables)
    res = res[0]
    assert(res == '# Ansible managed\n\nhosts:\n')

# Generated at 2022-06-22 12:08:34.473529
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest

    # Arrange
    terms = ['./some_template.j2']
    variables = {'foo': 'bar',
                 'ansible_current_user': {'name': 'some_user'},
                 'ansible_search_path': ['/etc/ansible'],
                 'ansible_user_id': 'some_user_id'}
    kwargs = {'convert_data': True,
              'variable_start_string': '{{',
              'variable_end_string': '}}',
              'comment_start_string': '{#',
              'comment_end_string': '#}',
              'jinja2_native': True,
              'template_vars': {'some_key': 'some_value'}}

    expected = ['bar']

    # Act
   

# Generated at 2022-06-22 12:08:44.379362
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import PY2
    from ansible.module_utils.six.moves import StringIO

    if PY2:
        lookup_file_contents = u"value: {{ test_var }}"
    else:
        lookup_file_contents = "value: {{ test_var }}"

    # Create a test environment
    backup_env = dict(os.environ)
    os.environ = dict(ANSIBLE_TEMPLATE_INTERPRETER_JINJA2_OVERRIDE="True",
                      ANSIBLE_TEMPLATE_INTERPRETER_NATIVE_JINJA2="False")

    # Create a fake inventory

# Generated at 2022-06-22 12:08:56.312557
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    display = Display()
    display.verbosity = 4
    
    # from ansible.vars import VariableManager
    # from ansible.inventory.manager import InventoryManager
    # from ansible.parsing.dataloader import DataLoader

    # loader = DataLoader()
    # inventory = InventoryManager(loader=loader, sources=['tests/lib/ansible/inventory/test_inventory.inventory'])
    # variable_manager = VariableManager(loader=loader, inventory=inventory)

    # Variable('ansible_search_path', ['jinjatestdir'], loader=loader, variables=variable_manager)
    # Variable('jinjatestdir', 'tests/lib/ansible/plugins/lookup', loader=loader, variables=variable_manager)
    # Variable('a_var', '1', loader=loader, variables=variable_

# Generated at 2022-06-22 12:09:08.028990
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Prepare data
    terms = ['some_template.j2']

# Generated at 2022-06-22 12:09:18.390299
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # check if LookupModule.run raises error in case of wrong template_vars type
    module = LookupModule()
    assert module.run(terms=['missing_file'], variables={}, **{'template_vars': "string", 'convert_data': False, 'variable_start_string': '{', 'variable_end_string': '}'}) == []
    assert module.run(terms=['missing_file'], variables={}, **{'template_vars': "string", 'convert_data': False, 'variable_start_string': '{', 'variable_end_string': '}', 'jinja2_native': True}) == []

# Generated at 2022-06-22 12:09:58.919787
# Unit test for method run of class LookupModule

# Generated at 2022-06-22 12:10:10.716814
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

    lm = LookupModule(loader=loader)

    # create a dummy vars
    class DummyVars(object):
        def __init__(self):
            self.foo = "bar"
            self.bar = "foo"

        def get(self, arg, default=None):
            return self.foo

    # test native_jinja off and jinja2_native off
    res = lm.run(terms=["test.j2"], variables=DummyVars(), convert_data=False,
                 jinja2_native=False, variable_start_string='[%', variable_end_string='%]',
                 comment_start_string='[#', comment_end_string='#]')
    assert res

# Generated at 2022-06-22 12:10:18.976581
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_template_vars = {}
    term = ''
    terms = [term]
    kwargs = {}
    variables = {}
    lookup = LookupModule()
    lookup.set_options(var_options=variables, direct=kwargs)

    # capture options
    convert_data_p = False
    jinja2_native = False
    variable_start_string = '{{'
    variable_end_string = '}}'
    comment_start_string = '{#'
    comment_end_string = '#}'

    def _templar_copy_with_new_env(environment_class=AnsibleEnvironment):
        return templar


# Generated at 2022-06-22 12:10:30.546111
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    result = lookup.run(['./tests/data/templates/ha.j2', './tests/data/templates/galera.cnf.j2'], {})
    result[0] = result[0].replace("\t", '')