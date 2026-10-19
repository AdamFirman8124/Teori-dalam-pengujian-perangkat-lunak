

# Generated at 2022-06-22 12:01:15.939819
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    #
    # test the default case
    #
    module = AnsibleModule(
        argument_spec=dict(
            _raw_params=dict(type='list', required=True),
            _terms=dict(type='list', required=True),
        ),
        supports_check_mode=True,
    )

    lookup_module = LookupModule()

    # pylint: disable=protected-access
    lookup_module._templar = Templar(loader=DictDataLoader(dict(templates={})))
    lookup_module._loader = DictDataLoader(dict(templates={}))
    # pylint: enable=protected-access

    assert lookup_module._get_file_contents('/tmp/s') == (b'', False)

# Generated at 2022-06-22 12:01:28.477986
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    import os
    import pytest

    # Create a dict object to store the ansible variables
    v = dict()
    v['ansible_verbosity'] = 1

    # Create a LookupModule object and initialize it using the ansible variable
    l = LookupModule()
    l.set_options(var_options=v, direct=None)

    # Perform the run operation
    result = l.run(terms=['/home/ubuntu/GIT/ansible'], variables=v, convert_data=False, jinja2_native=False, variable_start_string='{{', variable_end_string='}}', comment_start_string='{#', comment_end_string='#}', template_vars=None)
    assert len(result) == 1

# Generated at 2022-06-22 12:01:39.784157
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    PythonVersionTestPair = collections.namedtuple('PythonVersionTestPair', ['python_version', 'case'])
    with pytest.raises(AnsibleError) as excinfo:
        assert LookupModule().run([],{},{})
    assert 'the template file' in str(excinfo.value)

    # Test if the templates are rendered correct (using only default values)
    assert LookupModule().run(['tests/ansible/roles/role_for_testing_lookups/templates/os_template.j2'],[],{}) == ['Linux']
    assert LookupModule().run(['tests/ansible/roles/role_for_testing_lookups/templates/user_template.j2'],[],{}) == ['ChefLamp']

# Generated at 2022-06-22 12:01:43.039457
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['./some_template.j2']
    variables = {}
    ret = LookupModule.run(terms, variables)
    assert ret == []

# Generated at 2022-06-22 12:01:54.800868
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def _get_loader_mock():
        class MockLoader(object):
            def __init__(self):
                self.basedir = "/some/path"
                self.mock_file_contents = {
                    'some/path/myfile.j2': 'Hello {{ my_name }}',
                    'some/path/myotherfile.j2': 'Hello {{ my_name }}'
                }

            def get_basedir(self):
                return self.basedir

            def _get_file_contents(self, path):
                return self.mock_file_contents[path], True
        return MockLoader()

    def _get_templar_mock():
        class MockTemplar(object):
            def __init__(self):
                self.available_variables = {}


# Generated at 2022-06-22 12:01:59.835670
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit test for method run of class LookupModule
    :return:
    """
    module = LookupModule()
    terms = ['./test/test_lookup.py']
    result = module.run(terms, {}, **{})
    print(result)
    assert result[0].find('import os') > 0

# Generated at 2022-06-22 12:02:07.725269
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    terms = [b"{{ foo }}"]

    # ansible_os_family isn't actually a lookupable template in practice but we can use
    # it to provide an example of a variable that might be set on a host
    variables = dict(
        ansible_os_family='RedHat',
        foo='bar'
    )

    result = lm.run(terms, variables)
    assert result == [to_bytes('bar')]

# Generated at 2022-06-22 12:02:16.885219
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # try to run the LookupModule.run method against some simple template
    my_env = os.environ.copy()

    my_env["ANSIBLE_CONFIG"] = ''
    my_env["ANSIBLE_DEBUG"] = 'True'
    my_env["ANSIBLE_ERROR_ON_MISSING_HANDLER"] = 'True'
    my_env["ANSIBLE_FORCE_COLOR"] = 'True'
    my_env["ANSIBLE_HOST_KEY_CHECKING"] = 'False'
    my_env["ANSIBLE_PIPELINING"] = 'False'
    my_env["ANSIBLE_ROLES_PATH"] = 'doc/playbooks/test/roles'
    my_env["ANSIBLE_SSH_PIPELINING"] = 'False'

# Generated at 2022-06-22 12:02:23.660436
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''
    Testing the run method for LookupModule.
    '''
    # Create a sample lookup module
    lu = LookupModule()

    # Create a sample variable to process
    variables = dict(a=1, b=2, c=3, d=4)

    # Create a sample file to read from
    terms = ['/tmp/test.j2']

    # Use the run function to check the result
    result = lu.run(terms=terms, variables=variables, **{})
    print(result)

    # Assert that the output matches the sample
    # assert result

# Generated at 2022-06-22 12:02:35.563355
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create LookupModule object
    lookup_module = LookupModule()

    # Create terms
    terms = ["/ansible/data/j2templates/test.j2"]

    # Create variables
    variables = {
        'ansible_search_path': [
            "/ansible/tests/integration/inventory"
        ],
        'template_mtime': 1515138870.143176,
        'template_path': '/ansible/data/j2templates/test.j2',
        'template_uid': 1000
    }

    # Create kwargs

# Generated at 2022-06-22 12:02:41.378419
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-22 12:02:53.209625
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # mock the Loader class and its methods
    # mock the templar class and its methods - to use jinja2 and not use jinja2 native types
    #   NativeJinjaText is used to make sure we return the same result as jinja2_native=False
    terms = ['./some_template.j2']
    lookup_template_vars = {'key_for_template': 'value_for_template'}
    variable_start_string = '[%'
    variable_end_string = '%]'
    searchpath = './'
    lookupfile = './some_template.j2'

    class MockLoader(object):
        def __init__(self):
            pass


# Generated at 2022-06-22 12:03:05.322422
# Unit test for method run of class LookupModule

# Generated at 2022-06-22 12:03:16.709877
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import tempfile

    test_module = LookupModule()
    test_module._loader._get_basedir = lambda: os.getcwd()

    # Create a new temporary directory. The prefix ends with a trailing slash,
    # which is important to make the temporary directory appear as a file
    # system root.
    with tempfile.TemporaryDirectory(prefix='lookup_template_') as temp_dir:

        # We do not want to modify test data, so we copy the relevant test files
        # to the temporary directory.
        for f in ['bar.j2', 'foo.j2', 'foo.yaml']:
            src_path = os.path.join(os.getcwd(), '../lookup_plugins/', f)
            dst_path = os.path.join(temp_dir, f)
           

# Generated at 2022-06-22 12:03:23.941017
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # unit test for template lookup
    lu = LookupModule()
    ret = lu.run(['nested1.j2', 'nested2.j2'], {u'nested1_var': u'toto'}, basedir='../../lookup_plugins/test/files/')
    assert ret == [u'This is nested1 file toto\n', u'This is nested2 file toto\n']

# Generated at 2022-06-22 12:03:31.338734
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    lookup._loader = DictDataLoader({'a/a.j2': '{{ a }}'})
    template_data = lookup._loader.load('a/a.j2')
    lookup._templar = Templar(variables={u'a': u'A'})
    assert lookup.run([u'a.j2'], dict(a=u'A')) == to_text(template_data).split(u'\n')
    assert lookup.run([u'a.j2'], dict(a=u'B')) == [u'B']



# Generated at 2022-06-22 12:03:41.828169
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    def _assert_run(lookup, terms, variables, expected, **kwargs):
        assert isinstance(expected, list)
        got = lookup(terms=terms, variables=variables, **kwargs)
        assert expected == got

    f = LookupModule([])

    _assert_run(f.run,
                [], None,
                [])

    _assert_run(f.run,
                ['file_ok_1.j2'], dict(my_var='my_value'),
                [u'Hello my_value'],
                convert_data=False)

    _assert_run(f.run,
                ['file_ok_1.j2'], dict(my_var='my_value'),
                [{'my_list': ['an', 'example']}])


# Generated at 2022-06-22 12:03:51.021191
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a temporary file
    import tempfile
    fd, path = tempfile.mkstemp()
    f = os.fdopen(fd, "w")
    f.write("Hello, {{ test }}\n")
    f.close()

    # Hack to make unit test work without going through the full Ansible stack
    import ansible.plugins.loader as plugin_loader
    import ansible.plugins.lookup as lookup_plugins
    plugin_loader._package_paths = [os.path.dirname(os.path.realpath(__file__))]
    lookup_plugins._lookup_plugins = dict()

    # Create argument for method run and execute it
    LookupModule.run(LookupModule(), terms=[path], variables=dict(test="world"))

    # Clean up temporary file
    os.remove(path)

# Generated at 2022-06-22 12:03:51.921378
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()

# Generated at 2022-06-22 12:04:03.331543
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Instantiate a LookupModule object
    lookup_module_obj = LookupModule()
    # Test values for parameters
    # Testing scenario where no file is found
    # Test cases
    # using variables with name
    lookup_module_obj.set_loader(None)
    lookup_module_dict = {
        "convert_data": False,
        "template_vars": {},
        "jinja2_native": False,
        "variable_start_string": "{{",
        "variable_end_string": "}}",
        "comment_start_string": "",
        "comment_end_string": ""
    }
    lookup_module_obj.set_options(var_options=None, direct=lookup_module_dict)
    lookup_module_obj.set_environment(None)
    lookup_module_

# Generated at 2022-06-22 12:04:21.889322
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookupModule = LookupModule()
    terms = ['../lookup_plugins/test_template.j2']
    variables = dict(
        template_host='localhost',
        template_uid=1000,
        template_path='./lookup_plugins/test_template.j2',
        template_mtime=1598772956.13,
        ansible_search_path=[]
        )
    display = Display()
    lookupModule.set_display(display)
    kwargs = {}
    res = lookupModule.run(terms, variables, **kwargs)
    expected = ['template_host=localhost template_uid=1000 template_path=./lookup_plugins/test_template.j2 template_mtime=1598772956.13\n']

# Generated at 2022-06-22 12:04:31.518684
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.template import Templar

    templar = Templar(loader=None, variables={})
    lookup_class = LookupModule(loader=None, basedir=None, templar=templar)

    terms = []
    terms.append('example_template.j2')

    lookup_result = lookup_class.run(terms, {}, convert_data=False, jinja2_native=False)
    assert lookup_result[0] == 'Hello World!'

    lookup_result = lookup_class.run(terms, {}, convert_data=False, jinja2_native=True)
    assert lookup_result[0] == 'Hello World!'

    terms.append('example_template_with_variable.j2')

# Generated at 2022-06-22 12:04:43.339209
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class MockEnvironment:
        def template(self, template_data, preserve_trailing_newlines=False, convert_data=True, escape_backslashes=True):
            return 'Hello world'
    class MockTemplar:
        def __init__(self, *args, **kwargs):
            self._environment = MockEnvironment()
        def set_temporary_context(self, *args, **kwargs):
            return self

    class MockLoader:
        def _get_file_contents(self, lookupfile):
            return to_bytes('''Welcome to {{ hostname }}.
I am {{ myname }}.
My daily limit is {{ day_limit }}
'''), True

    class MockDisplay:
        def __init__(self, *args, **kwargs):
            pass

# Generated at 2022-06-22 12:04:54.432223
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    print("test_LookupModule_run: module:", module)
    
    # test_LookupModule_run: module: <ansible.plugins.lookup.template.LookupModule object at 0x7f8a88e5c5c0>
    
    terms = ['./some_template.j2']

# Generated at 2022-06-22 12:04:59.907615
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    L = LookupModule()
    result = L.run(['my_file.j2'],{
        'playbook_dir': '/home/ansible/playbooks',
        'apb_var': 'value'
    })
    print(result)

# Generated at 2022-06-22 12:05:09.859264
# Unit test for method run of class LookupModule

# Generated at 2022-06-22 12:05:22.931807
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleSequence

    import os
    import sys
    import __main__ as main

    # Hack so that the tests will be found
    main.GLOBAL_HELPER_SETTINGS = {'ROLE_PATH': '/dev/null/roles'}
    sys.modules['ansible.constants'] = type('DummyModule', (object,), {'DEFAULT_MODULE_PATH': '/dev/null/library'})

    # Hack so that the right lookup plugin path is detected
    sys.modules['ansible.plugins'] = type('DummyModule', (object,), {'__file__': '/dev/null/plugins/modules'})

# Generated at 2022-06-22 12:05:34.755182
# Unit test for method run of class LookupModule

# Generated at 2022-06-22 12:05:43.693194
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # mock display
    def display_mock(self, msg, *args, **kwargs):
        for arg in args:
            msg = msg % arg
        for kwarg in kwargs.values():
            msg = msg % kwarg

        # capture debug messages
        if debug_value == True:
            print(msg, file=sys.stderr)

    def find_file_mock(self, variables, loader, path, names):
        return ["ansible/plugins/lookup/template.py"]

    def get_file_contents_mock(self, path):
        return "test1, {{test2}}", True

    term = "test_template.j2"
    variables = {"test2": "test2_variable"}
    debug_value = True

# Generated at 2022-06-22 12:05:54.579202
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    ansible_env = os.path.expanduser('~') + '/.ansible/test_AnsibleEnvironment'
    if os.name != 'nt':
        os.environ['ANSIBLE_CONFIG'] = ansible_env + '/ansible.cfg'
    else:
        os.environ['ANSIBLE_CONFIG'] = ansible_env + '\\ansible.cfg'
    if os.path.exists(ansible_env):
        shutil.rmtree(ansible_env)
    os.makedirs(ansible_env)
    # Create a test ansible.cfg
    with open(os.path.expanduser('~') + '/.ansible/test_AnsibleEnvironment/ansible.cfg', 'w') as f:
        f.write('[defaults]\n')


# Generated at 2022-06-22 12:06:23.551738
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import tempfile
    import yaml

    # create temporary test directory
    temp_dir = tempfile.mkdtemp()

    # create temporary test vars
    test_vars = dict()
    test_vars['var1'] = 'foo'
    test_vars['var2'] = 'bar'

    # create temporary test templates
    template_path = os.path.join(temp_dir, '1.j2')
    with open(template_path, 'w') as file:
        file.write("{{ var1 }}\n{{ var2 }}\n")

    # create LookupModule instance
    module = LookupModule()
    module._templar = None

    # call method run for template_path with test_vars

# Generated at 2022-06-22 12:06:35.587953
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # create a template with a {{ ansible_managed }} tag
    # should be rendered by the lookup
    lookup_plugin = LookupModule()
    lookup_plugin.set_options(direct={})
    lookup_term = lookup_plugin.run(["template.j2"], dict(ansible_managed='Ansible managed'), convert_data=True)
    assert isinstance(lookup_term, list)
    assert lookup_term[0] == 'Ansible managed\n'

    # create a template with a [% ansible_managed %] tag
    # should be rendered by the lookup
    lookup_term = lookup_plugin.run(["template.j2"], dict(ansible_managed='Ansible managed'),
                                    variable_start_string='[%', variable_end_string='%]')

# Generated at 2022-06-22 12:06:46.426326
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # the jinja2_native option is tested in this test case.
    # the jinja2_native option is available only in Ansible 2.11 and later.
    # Therefore, the test case is only run if Ansible version is 2.11 or later.
    from ansible.module_utils.version import __version__
    from packaging.version import Version
    if Version(__version__) < Version("2.11"):
        return

    from ansible.module_utils.jinja2._compat import PY3

    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    class Options():
        """ dummy class to mimic options passed to AnsibleModule """
        def __init__(self):
            self.lookup_plugin = 'template'
            self.convert_data

# Generated at 2022-06-22 12:06:58.469282
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    # The options for jinja2_native can only be tested if the plugin has been compiled against
    # the native Jinja2 library
    if USE_JINJA2_NATIVE:
        g_native_jinja = True
    else:
        g_native_jinja = False

    # Test the default operation
    vari = dict()
    vari['environment'] = dict()
    vari['environment']['convert_data'] = True
    templar = dict()
    templar['_available_variables'] = dict()
    templar['available_variables'] = dict()
    templar['_available_variables']['test_available_variables'] = True

# Generated at 2022-06-22 12:07:09.296241
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Unit test for method run of class LookupModule"""
    # Creation of a lookup plugin
    lookup_plugin = LookupModule()
    # Creation of a dict
    lookup_terms = dict()
    # Creation of a dict
    variables = dict()
    # Creation of a dict
    lookup_vars = dict()
    lookup_vars['name'] = 'myTest'
    # Creation of a dict
    kwargs = dict()
    kwargs['convert_data'] = False
    kwargs['template_vars'] = lookup_vars
    kwargs['comment_start_string'] = "#"
    kwargs['comment_end_string'] = ""
    kwargs['variable_start_string'] = "{{"
    kwargs['variable_end_string'] = "}}"
    # Assign to

# Generated at 2022-06-22 12:07:16.933049
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module._templar = {"template": lambda x, vars: x}
    lookup_module.set_options(var_options={"a": "b"}, direct={"template_vars": {"foo": "bar"}})
    res = lookup_module.run(["msg: '{{a}}'", "msg: '{{foo}}'"], {"a": "c"})
    assert res == ["msg: 'b'", "msg: 'bar'"]

# Generated at 2022-06-22 12:07:28.181293
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """This method is used to run unit tests for class LookupModule."""
    from ansible.__main__ import cli
    from ansible.constants import DEFAULT_MODULE_PATH
    from ansible.utils.display import Display
    from ansible.plugins.loader import lookup_loader

    display = Display()
    cli.parser(["", "--tree", ".", "--list-hosts"])
    cli.options.module_path.append(DEFAULT_MODULE_PATH)
    host_list = cli.inventory.list_hosts()

    var_manager = cli.variable_manager
    loader = cli.loader
    var_manager.extra_vars = {}
    var_manager.options_vars = {}

    lookups = lookup_loader.all(class_only=True)

# Generated at 2022-06-22 12:07:39.685693
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.plugins.loader
    # Create the module instance
    lookup_module_class = ansible.plugins.loader.lookup_loader.get('template')
    lookup_module_instance = lookup_module_class()
    # Call the method run
    result = lookup_module_instance._lookup_plugin.run(terms=['./some_template.j2'], variables={'lookup_file': 'lookup_file.ext'},
                                                       convert_data=True, template_vars={'foo': 'bar'}, jinja2_native=True,
                                                       variable_start_string='[%', variable_end_string='%]',
                                                       comment_start_string='[#', comment_end_string='#]')
    assert result == []

# Generated at 2022-06-22 12:07:50.821044
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create an instance of the LookupModule class
    l = LookupModule()

    # Create a term to use for the tests
    term = 'filetest.test'

    # Create a dictionary containing a variable
    variables = {
        "ipsum": "ipsum"
    }

    # Create variable_start_string
    variable_s_s = '{{'

    # Create variable_end_string
    variable_e_s = '}}'

    # Create a dictionary containing a variable
    lookup_template_vars = {
        "loreum": "loreum"
    }

    # Create jinja2_native
    jinja2_n = False

    # Create a dictionary containing options used by the function run of AnsibleLookupModule class

# Generated at 2022-06-22 12:08:03.373395
# Unit test for method run of class LookupModule
def test_LookupModule_run():  # noqa
    test_object = LookupModule()

    # Check with a valid template
    terms = ['./testLookup/test.j2']
    variables = {'lang': 'en', 'key': ['foo', 'bar']}
    result = test_object.run(terms, variables)
    assert result == ["en,foo,bar"]

    # Check with a valid template, with extended types
    terms = ['./testLookup/test2.j2']
    variables = {'lang': 'en', 'key': {'foo': 42, 'bar': 43}}
    result = test_object.run(terms, variables)
    assert result == ["en,42,43"]

    # Check with invalid template
    terms = ['./testLookup/nothere.j2']

# Generated at 2022-06-22 12:08:54.153335
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Disabling pylint because of the classes used in the test
    # pylint: disable=no-member
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.template import Templar
    from ansible.utils.display import Display
    _ = Display()

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['tests/inventory'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    variable_manager.extra_vars = {
        'vars': {
            'template_var': 'template_var_value',
        },
    }

# Generated at 2022-06-22 12:09:06.085459
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import sys
    import pytest
    from ansible.module_utils.six.moves import StringIO
    from ansible.module_utils.six import PY2

    # used to test if warning is correctly thrown when convert_data is set
    lookup_file_data = '''{
        "foo": "{{ bar }}",
        "ref": "{{ ref_var }}",
        "list": [ "{{ item }}" ]
    }'''

    # used to test if yaml data is correctly returned when convert_data is not set
    lookup_yaml_data = '''{
        "foo": {{ bar }},
        "ref": {{ ref_var }},
        "list": [ {{ item }} ]
    }'''

    # used to test whether jinja2 native types and convert_data option are mutually exclusive

# Generated at 2022-06-22 12:09:16.493858
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit test for method run of class LookupModule
    """
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.lookup_plugins.template import LookupModule
    from ansible.template import template_from_string
    display = Display()
    fake_loader = DictDataLoader({u'test_template.j2': u'foo'})
    fake_templar = Templar(loader=fake_loader, variables={u'lookup_file': u'/etc/foo.conf'})
    display.display(u"Using templar: %s" % fake_templar)
    lookup = LookupModule()
    lookup.set_loader(fake_loader)
    lookup.set_templar(fake_templar)


# Generated at 2022-06-22 12:09:27.956940
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # The fixtures required by this method are not provided originaly, so we need to do it here
    import pytest
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText # The function we are testing retunrs objects of this type
    from ansible.parsing.yaml.objects import AnsibleMapping # The function we are testing accepts an object of this type
    from ansible.template import AnsibleEnvironment # The function we are testing calls this class
    from ansible.vars.manager import VariableManager # The function we are testing calls this class
    from ansible.parsing.dataloader import DataLoader # The function we are testing calls this class
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText # The function we are testing calls this class
    from ansible.inventory.manager import InventoryManager # The function

# Generated at 2022-06-22 12:09:38.543077
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest

    module_args = dict(
        lookup_file='tests/test.j2',
        template_vars=dict(
            hostname="localhost",
            port=22
        )
    )
    module_args_multiple = dict(
        lookup_file='tests/test.j2,tests/test2.j2',
        template_vars=dict(
            hostname="localhost",
            port=22
        )
    )
    module_args_multiple_oneline = dict(
        lookup_file='tests/test.j2,tests/test2.j2',
        template_vars=dict(
            hostname="localhost",
            port=22
        ),
        convert_data=False
    )

# Generated at 2022-06-22 12:09:47.020514
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import tempfile

    lookup = LookupModule()
    lookup._loader = DictDataLoader()
    lookup._templar = Templar(loader=lookup._loader)
    lookup._loader.set_basedir(os.getcwd())

    lookupfile = os.path.join(os.getcwd(), "tests", "templatetest.j2")
    assert lookupfile == lookup.find_file_in_search_path(
        dict(), "templates", "templatetest.j2"
    )

    lookup._loader.set_basedir(tempfile.mkdtemp())
    lookupfile = os.path.join(tempfile.mkdtemp(), "templatetest.j2")

# Generated at 2022-06-22 12:09:57.404345
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # The initial setup is borrowed from test_TemplateLookupPlugin.
    from ansible.plugins.loader import lookup_loader
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    loader = DataLoader()
    paths = ':'.join(['.', './lookup_plugins'])
    inventory = InventoryManager(loader=loader, sources=paths)
    variable_manager.set_inventory(inventory)

    # Initialize a LookupModule instance.
    lookup_plugin = lookup_loader.get('template', variables=variable_manager)

    # Initialize a Templar instance.

# Generated at 2022-06-22 12:10:00.210269
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookupModule = LookupModule()
    assert lookupModule.run(["tests/template_test.j2"], {"myvar": "my_content"}) == ["my_content"]

# Generated at 2022-06-22 12:10:11.542228
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class FakeLoader:
        def get_basedir(self, _):
            return 'fake_ansible_dir'

        def _get_file_contents(self, path):
            return 'fake templated content', False

    class FakeVars:
        def get(self, key, default=''):
            return default

    class FakeEnv:
        def set_temporary_context(self, *args, **kwargs):
            return self

        def template(self, *args, **kwargs):
            return 'fake rendered content'

    loader = FakeLoader()
    templar = FakeEnv()
    lookup = LookupModule(loader=loader, templar=templar)
    terms = ['fake_template.j2']
    variables = FakeVars()
    kwargs = {}
    result = lookup

# Generated at 2022-06-22 12:10:22.113884
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import tempfile
    import textwrap
    import os
    import json
    import yaml
    import pytest

    # Create temporary file
    template_file = tempfile.NamedTemporaryFile(prefix='ansible-template-lookup-test-', dir='.')
    template_file.write(to_bytes(textwrap.dedent("""
        # This is a test
        {{ foo }}
        {{ bar }}
        {% for x in y %}
        [{{ x }}]
        {% endfor %}
        """), errors='surrogate_escape'))

    # Close temporary file
    template_file.close()

    # Create lookup module
    lookup_module = LookupModule()

    # Create context
    context = {}
    context['foo'] = "hello"
    context['bar'] = "world"