

# Generated at 2022-06-22 12:01:16.721340
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test for success.
    args = {"_terms": ["./tests/lookup/template_test.j2"],
            "comment_end_string": None,
            "comment_start_string": None,
            "variable_end_string": None,
            "variable_start_string": None,
            "convert_data": True,
            "jinja2_native": False,
            "template_vars": {"var1": "This is a test!", "var2": "There are many tests like this."}}

    # This is the only supported instance of the LookupModule class.
    lookup_module = LookupModule()

    # This is Ansible's cache of variables from inventory, fact gathering, etc.
    variables = {"var1": "This is a test!", "var2": "There are many tests like this."}

   

# Generated at 2022-06-22 12:01:29.441152
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import tempfile
    from ansible.module_utils._text import to_text
    from ansible.plugins.loader import lookup_loader
    from ansible.parsing.dataloader import DataLoader
    test_lookup_plugin = lookup_loader.get('template')
    test_loader = DataLoader()

    # create temporary test file
    fd, temppath = tempfile.mkstemp()
    os.write(fd, to_text("""{{ ansible_env.USER }}""").encode('utf-8'))
    os.close(fd)


# Generated at 2022-06-22 12:01:40.512127
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Set up mock class
    class MockLookupBase(LookupBase):
        def __init__(self, *args, **kwargs):
            pass

        def run(self, *args, **kwargs):
            return True
    l = LookupModule(loader=MockLookupBase())

    # Create a MockRun() object
    class MockRun():
        def __init__(self):
            self.result = True
    m = MockRun()

    # Create a MockClass() object
    class MockClass():
        def __init__(self):
            d = {
                'result': True,
                'msg_template': "The template file '%s' could not be found for the lookup"
            }
            self.result = d

    # Set up the patch

# Generated at 2022-06-22 12:01:52.874953
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['/path/to/file']
    variables = {'a': 1}
    kwargs = {'variable_start_string': '[',
              'variable_end_string': ']'}

    class AnsibleModuleMock(object):
        def __init__(self, variables):
            self.params = {}
            self.params['_ansible_search_path'] = ['/path/to/dir']
            self.params['variable_start_string'] = '{{'
            self.params['variable_end_string'] = '}}'
            self.params['comment_start_string'] = '{#'
            self.params['comment_end_string'] = '#}'
            self.params['env'] = {}
            self.params['tmpdir'] = '/path/to/tmpdir'

# Generated at 2022-06-22 12:02:05.025123
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_obj = LookupModule()


    # Unit test for method run when assert_type is None
    def run_assert_type_is_none(param):
        template_vars_dic = {}
        lookup_obj.run(param["terms"], param["variables"], template_vars=template_vars_dic)

    # Unit test for method run when assert_type is not None
    def run_assert_type_is_not_none(param):
        template_vars_dic = {}
        lookup_obj.run(param["terms"], param["variables"], template_vars=template_vars_dic)


# Generated at 2022-06-22 12:02:08.125954
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """ Unit test for run method of class LookupModule """
    options = {}
    return_data = [
        {
            'msg': 'Hello world',
        }
    ]
    lookup_plugin = LookupModule()
    lookup_plugin.set_options(var_options=options, direct=options)
    terms = ['test1.j2']
    variables = {
        'testvar': 'testvalue',
    }
    display_content = {'msg': 'Hello world\n'}
    test_lookup_plugin_run(lookup_plugin, terms, variables, return_data, display_content)


# Generated at 2022-06-22 12:02:17.129927
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    lookup._loader = DictDataLoader({"dir/foo.j2": "{{ bar }}"})
    lookup._templar = Templar(variables=dict())
    lookup.set_loader(lookup._loader)

    ret = lookup.run(["foo.j2"], dict(bar="baz"))
    assert ret == ["baz"]

    # jinja2_native is True globally and on for the lookup
    lookup._templar = Templar(variables=dict(), jinja2_native=True)
    lookup.set_loader(lookup._loader)
    ret = lookup.run(["foo.j2"], dict(bar="baz", jinja2_native=True))
    assert ret == ["baz"]

    # jinja2_native is True globally and off for the

# Generated at 2022-06-22 12:02:25.093168
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Unit test for template lookup, with native jinja2 and converting data
    f = open("/tmp/test.j2", "w")
    f.write("{{ansible_env['HOME']}}")
    f.close()
    lu = LookupModule()
    terms = ["/tmp/test.j2"]
    display.verbosity = 4
    import os
    variables = {"ansible_env": os.environ}
    result = lu.run(terms, variables, convert_data=True, jinja2_native=True)
    assert result == [os.environ["HOME"]]

    # Unit test for template lookup, with native jinja2 but not converting data
    f = open("/tmp/test.j2", "w")
    f.write("{{ansible_env['HOME']}}")

# Generated at 2022-06-22 12:02:36.959464
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.template import Templar

    def _templar_copy_with_new_env(self, environment_class=None):
        return self

    def _templar_copy(self):
        return self

    def _templar_set_available_variables(self, variables):
        self._available_variables = variables

    def _templar_set_temporary_context(self, *args, **kwargs):
        if not hasattr(self, '_available_variables'):
            self._templar_set_available_variables(kwargs['available_variables'])

        return self


# Generated at 2022-06-22 12:02:47.906168
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Create an instance of LookupModule
    lookup_mod = LookupModule()

    # Simulate a 'find_file_in_search_path' method (normally is part of the 'PluginLoader')
    # This method is used in the 'run' method
    def find_file_in_search_path(variables, dirname, filename):
        return(filename)

    # Simulate a '_get_file_contents' method (normally is part of the 'PluginLoader')
    # This method is used in the 'run' method
    def get_file_contents(filename):
        contents = "This is the contents of the template file %s" % filename
        # Using base64.b64encode just to simulate a non-text (binary) file
        show_data = b64encode(contents)

# Generated at 2022-06-22 12:03:05.280232
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

# Generated at 2022-06-22 12:03:16.671039
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # The variabes are gathered from the ansible-playbook run
    # The test does not get the variables from the playbook run
    # The variables are mocked in the test
    from ansible.module_utils.parsing.convert_bool import BOOLEANS_TRUE, BOOLEAN_FALSE, BOOLEAN_TRUE
    from ansible.template import Templar
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    import mock
    import os
    import sys
    import yaml

    mock_loader = mock.MagicMock()
    mock_loader._get_file_contents = mock.MagicMock(return_value=[
        b'Test Template File\n', ''
    ])

# Generated at 2022-06-22 12:03:28.254573
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Init unit test environment
    import os.path
    import shutil
    import sys
    import tempfile
    import yaml

    currentDirectory = os.path.dirname(os.path.realpath(__file__))
    tempTemplateFolder = tempfile.mkdtemp()

    # Write test template files
    testTemplateFileList = (
        (os.path.join(tempTemplateFolder, 'testTemplate.txt'), {"a": 1, "b": 2, "c": "{{ c }}"}),
        (os.path.join(tempTemplateFolder, 'testTemplate2.txt'), {"a": "{{ lookup('template', 'testTemplate.txt') }}", "c": 3}),
    )

# Generated at 2022-06-22 12:03:36.706134
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins import lookup_loader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    import ansible.constants as C

    class LookupModule_run(LookupModule):

        def __init__(self, loader=None, templar=None, **kwargs):
            self._loader = loader or DataLoader()
            self._templar = templar
            self.set_options(kwargs)

        def find_file_in_search_path(self, variables, dirs, file):
            return './templates/' + file

        def get_option(self, key):
            return self.options[key]


# Generated at 2022-06-22 12:03:48.291328
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.vault import VaultLib
    from ansible.plugins.lookup import LookupBase
    from ansible.template import Templar
    from ansible import context
    import os
    import sys

    cwd = os.path.join(os.path.dirname(sys.argv[0]), os.pardir, os.pardir, os.pardir)
    lookup = LookupModule()
    templar = Templar(loader=None, variables=None, vault_secrets=VaultLib())
    lookup._loader = context.CLIARGS['loader']

    #########################################################################################
    # Run test 1: test a "template file does not exist" case
    #########################################################################################
    params = ['some_template_file.j2']

# Generated at 2022-06-22 12:04:00.169975
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    terms = ['./file1']
    variables = {}
    ret = module.run(terms, variables)
    assert ret == [u'Hello, World!']

    module = LookupModule()
    terms = ['./file2']
    variables = {'var1': 'foo', 'var2': 'bar'}
    ret = module.run(terms, variables)
    assert ret == [u"Hello, foo bar!"]

    module = LookupModule()
    terms = ['./file3']
    variables = {'my_list': ['val1', 'val2'], 'my_dict': {'key1': 'val1', 'key2': 'val2'}}
    ret = module.run(terms, variables)

# Generated at 2022-06-22 12:04:10.451420
# Unit test for method run of class LookupModule

# Generated at 2022-06-22 12:04:16.704040
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test with a variable_start_string and variable_end_string
    module = LookupModule()
    terms = './some_template.j2'
    variables = {'greeting': 'hello'}
    kwargs = {'variable_start_string': '--', 'variable_end_string': '--'}
    result = module.run(terms=terms, variables=variables, **kwargs)
    assert result[0] == 'hello'

# Generated at 2022-06-22 12:04:27.996951
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.six import string_types

    # Construct an object of the LookupModule class
    test_obj = LookupModule()

    # Test if function run raises an Exception if the
    # lookupfile path is not existing
    terms = ['hello_world.j2']
    variables = {}
    with pytest.raises(AnsibleError):
        test_obj.run(terms, variables)

    # Test if function run returns a list of strings when
    # results are returned from templating
    test_path = './test/integration/lookup_plugins/'
    test_file = os.path.join(test_path, 'hello_world.j2')

# Generated at 2022-06-22 12:04:36.384776
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Mocking the object
    class object(object):
        def __init__(self):
            self.var_options = {'hostvars': None}
            self.direct = {'lang': 'python'}
            # This class attribute is necessary for Ansible 2.6.0
            self.fallback = None
            self.ansible_basedir = os.getcwd()
        def set_options(self, var_options, direct):
            self.var_options = var_options
            self.direct = direct
        def find_file_in_search_path(self, variables, directory, term):
            return self._loader._get_file_contents(term)[1]
        def _templar(self):
            return object(self)
            # TODO: Templating not working
            # return object()
       

# Generated at 2022-06-22 12:04:50.921760
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Executes the module code with a valid input
    result = LookupModule().run(terms=['/etc/passwd'], variables={})
    assert result == ['/etc/passwd']

    # Executes the module code with a valid input
    result = LookupModule().run(terms=['/etc/passwd'], variables=dict(file='/etc/passwd'))
    assert result == ['/etc/passwd']

# Generated at 2022-06-22 12:05:00.510022
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import types
    #import mock
    from ansible.parsing import vault

    #class mock_loader(object):
    #    pass
    #class mock_templar(object):
    #    pass
    #class mock_unfrackpath(object):
    #    pass
    #class mock_find_file_in_search_path(object):
    #    pass
    #class mock_AnsibleEnvironment(object):
    #    pass

    lookup_plugin = LookupModule()
    #lookup_plugin._loader = mock_loader()
    #lookup_plugin._loader._loader = mock_loader()
    #lookup_plugin._loader._loader.get_basedir = mock.MagicMock(return_value='/my_basedir/')
    #lookup_plugin._templar = mock_tem

# Generated at 2022-06-22 12:05:10.077719
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Test the method run of the module ansible.plugins.lookup.template"""
    env = {
        'template_path': ['.'],
        'ansible_search_path': ['.'],
        'ansible_managed': 'Ansible managed',
        'ansible_facts': {
            'distribution': 'debian'
        }
    }

    env_templar = DummyTemplar(env)
    loader1 = DummyLoader(None)
    loader1.set_basedir('tests/templates')
    templar = Templar(loader=loader1, variables=env_templar)
    # test with some jinja2 options
    templar2 = templar.copy_with_new_env(environment_class=DummyEnv)
    templar2.environment.variable_start

# Generated at 2022-06-22 12:05:23.026317
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    return_str = '{ "test": "test" }'

    class VarsModule:
        def __init__(self):
            self._templar = "test"

        def get_option(self, option):
            if option == 'jinja2_native':
                return False
            elif option == 'template_vars':
                return {}
            elif option == 'variable_start_string':
                return '{{'
            elif option == 'variable_end_string':
                return '}}'
            elif option == 'comment_start_string':
                return '{#'
            elif option == 'comment_end_string':
                return '#}'
            else:
                return None

        def set_options(self, var_options, direct):
            pass


# Generated at 2022-06-22 12:05:34.829971
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.template import Templar
    from ansible.utils.display import Display
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    import os
    import pytest

    lookup_term = "lookup_term"
    lookup_template_vars = dict()
    lookup_terms = [lookup_term]
    lookup_variables = dict(
        ansible_search_path=['/path/to/first/search/path', '/path/to/second/search/path'],
        vault_password=[AnsibleVaultEncryptedUnicode(u'vault_password')],
    )
    display = Display()

# Generated at 2022-06-22 12:05:43.771119
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import copy
    import sys
    import tempfile
    import warnings

    try:
        from ansible.module_utils.common._collections_compat import MutableMapping
    except ImportError:
        from collections import MutableMapping
    from ansible.parsing.yaml.objects import AnsibleSequence, AnsibleMapping
    from ansible.template import Templar
    from ansible.vars import combine_vars

    class FakeVarsModule(MutableMapping):

        def __init__(self, name, data=None):
            self.name = name
            self.data = data or {}

        def __setitem__(self, key, value):
            self.data[key] = value

        def __getitem__(self, key):
            return self.data[key]


# Generated at 2022-06-22 12:05:50.614434
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: better unit test
    #       -> more tests
    #       -> make more isolated (e.g. with mocks)
    lookup_module = LookupModule()
    lookup_module.set_loader({'_get_file_contents': lambda x: (to_bytes('{{var1}}'), False)})
    lookup_module._templar = AnsibleEnvironment(loader=lookup_module._loader)
    lookup_module.run(['./test_template'], {'var1': 'this is var1'})

# Generated at 2022-06-22 12:06:00.661981
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test data
    lookup_file_name = "./test.j2"
    variable_start_string = '{{'
    variable_end_string = '}}'
    variable_value = "I am a variable"
    variable_name = "var"

    test_data = '%s %s %s' % (variable_start_string, variable_name, variable_end_string)
    j2_types = True

    # create a file for test
    with open(lookup_file_name, 'w+') as lookup_file:
        lookup_file.write(test_data)

    # create instance of LookupModule
    lookup_module = LookupModule()
    template_vars = {variable_name : variable_value}

    # run test with j2_types enabled

# Generated at 2022-06-22 12:06:10.826072
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # When convert_data is True
    ret = LookupModule().run(
        terms=["../test/test.j2"],
        variables={
            "testvar": "testval",
            "testvar2": "testval2",
        },
        convert_data=True,
    )

    assert ret == [["testval", "testval2"]]

    try:
        ret = LookupModule().run(
            terms=["../test/test.j2"],
            variables={
                "testvar": "testval",
                "testvar2": ["testval2"],
            },
            convert_data=True,
        )
    except ValueError:
        pass
    else:
        assert False

    # When convert_data is False

# Generated at 2022-06-22 12:06:21.597642
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    def mock_find_file_in_search_path(*args, **kwargs):
        return 'str'

    import pytest
    from ansible.errors import AnsibleError
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.template import generate_ansible_template_vars


# Generated at 2022-06-22 12:06:49.474559
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''
    Used to test if the method run of class LookupModule
    returns the correct results
    '''
    import re

    path = '/usr/share/ansible/lookup_plugins/template'

    terms = ['./some_template.j2']

# Generated at 2022-06-22 12:07:01.667951
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup import LookupModule
    from ansible.module_utils._text import to_text
    from ansible.template import AnsibleEnvironment

    if USE_JINJA2_NATIVE:
        templar = AnsibleEnvironment()
    else:
        templar = {}

    lookup = LookupModule()
    lookup.set_loader({})
    lookup._templar = templar
    lookup.set_options({})
    lookup.set_options({'_ansible_check_mode': False})
    terms = ['lookup_test_test1.j2']
    variables = {}
    result = lookup.run(terms=terms, variables=variables, convert_data=True)
    assert result == [to_text("Lookup test with ansible_hostname Hello test1\n")]

# Generated at 2022-06-22 12:07:12.891468
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.errors import AnsibleError
    from ansible.module_utils._text import to_bytes


# Generated at 2022-06-22 12:07:18.958260
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # First, create an instance of LookupModule class
    lookup_module_instance = LookupModule()
    # Next, create a dictionary to pass as arg variables,
    # as this arg is required by run()
    terms = "./some_template.j2"
    # The variables arg below is used in the test for find_file_in_search_path()
    variables = {"ansible_search_path": ['.']}
    # Pass all the args to run()
    lookup_module_instance.run(terms, variables)

# Generated at 2022-06-22 12:07:28.931919
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    jinja2_native = True
    lookup_template_vars = {}
    convert_data_p = False
    variable_start_string = '{{'
    variable_end_string = '}}'
    comment_start_string = '{#'
    comment_end_string = '#}'

    if USE_JINJA2_NATIVE and not jinja2_native:
        templar = None
    else:
        templar = None


    # test for jinja2_native is true globally but off for the lookup, we need this text
    # not to be processed by literal_eval anywhere in Ansible
    res = NativeJinjaText(res)

    assert res == "message: 'Hello world!'"

# Generated at 2022-06-22 12:07:32.645254
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    assert(module.run(["test_jinja2.j2"], {'option_not_to_be_used': 'foo'}) == ['Hello Ansible!'])


# Generated at 2022-06-22 12:07:42.541508
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Check default behavior when jinja2_native=False
    module = LookupModule()
    module.set_options({})  # reset the options to default
    assert module.run(['./some_template.j2'], {'a': 'b'}) == [u'{{ a }}']

    # Check default behavior when jinja2_native=True
    module.set_options({'jinja2_native': 'yes'})
    assert module.run(['./some_template.j2'], {'a': 'b'}) == [u'{{ a }}']

    # Check that the lookup_type and lookup_plugin values are available
    # to templates as variables.

# Generated at 2022-06-22 12:07:53.643409
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.vars.manager import VariableManager

    def test_options(self, *args, **kwargs):
        def get_option(option):
            option_lookup = {'convert_data': True, 'template_vars': {}, 'jinja2_native': False,
                             'variable_start_string': '{{', 'variable_end_string': '}}',
                             'comment_start_string': None, 'comment_end_string': None}
            return option_lookup[option]
        self.get_option = get_option

    if USE_JINJA2_NATIVE:
        from ansible.template import ANSIBLE_NATIVE_JINJA_TEMPLATE_INTERFACE as environment_class
    else:
        from ansible.template import ANSIBLE_JINJA2_

# Generated at 2022-06-22 12:08:06.303281
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # arguments used for instantiating LookupModule object
    terms = ['test_template_file.txt']
    variables = {'test_var': 'test_var_value'}

    # arguments used for calling method run
    test_kwargs = {'variable_start_string': '{{',
                   'variable_end_string': '}}',
                   'comment_start_string': '{#',
                   'comment_end_string': '#}',
                   'convert_data': False,
                   'jinja2_native': False}

    # test successful case
    lookup_module_object = LookupModule()

# Generated at 2022-06-22 12:08:15.610138
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # init LookupModule class
    from ansible.plugins.lookup import file
    lookup = LookupModule()
    lookup._templar = file.Templar(loader=None, variables={
        'template_path': './templates',
        'ansible_facts': {
            'system': "Red Hat Linux"
        }
    })
    # test run method
    result = lookup.run(
        [
            './test_template.j2'
        ],
        variables={
            'template_path': './templates',
            'ansible_facts': {
                'system': "Red Hat Linux"
            }
        }
    )

# Generated at 2022-06-22 12:09:02.426038
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Unit test for method run of class LookupModule"""
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.plugins.lookup.template import LookupModule as TemplateLookupModule
    from ansible.template import Templar

    test_lookup_module = TemplateLookupModule()
    # setup context:
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

# Generated at 2022-06-22 12:09:13.115147
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager.set_inventory(inventory)

    fh = open(os.path.join(os.environ['HOME'], 'sample_inventory.yml'))
    inventory_file = fh.read()
    fh.close()


# Generated at 2022-06-22 12:09:13.735119
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-22 12:09:25.402043
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Without any keyword arguments
    lookup_module = LookupModule()
    lookup_module.set_loader(DictDataLoader({
        'test.jinja2': b'<html>{{ name }}</html>',
        'test.json': b'{"name": "paul"}'
    }))
    lookup_module._templar = Templar()
    lookup_module._templar.environment.loader = lookup_module._loader

    ret = lookup_module.run(
        [
            'test.jinja2',
            'test.json'
        ],
        {},
        convert_data=True,
        jinja2_native=False,
        template_vars={'name': 'paul'}
    )


# Generated at 2022-06-22 12:09:36.326065
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import tempfile
    import ansible.utils.plugin_docs as plugin_docs
    class Options(object):
        def __init__(self, variable_start_string, variable_end_string,
                     convert_data=False, jinja2_native=True, **kwargs):
            self.variable_start_string = variable_start_string
            self.variable_end_string = variable_end_string
            self.convert_data = convert_data
            self.jinja2_native = jinja2_native
            for k, v in kwargs.items():
                setattr(self, k, v)

    class DummyVarsModule(object):
        def __init__(self, vars):
            self.vars = vars

        def dump(self):
            return self.vars

    #

# Generated at 2022-06-22 12:09:45.864019
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import io
    import os
    import pytest
    lookup = LookupModule()
    # test unsuccesful lookup with no file
    term = '/unexisting/file.j2'
    variables = {}
    lookup.set_options(var_options=variables, direct={})
    pytest.raises(AnsibleError, lookup.run, terms=term, variables=variables)
    # test succesful lookup with file
    term = ['test_template.j2']
    variables['template_path'] = os.path.realpath(os.path.join(os.path.dirname(__file__), 'data'))
    lookup.set_options(var_options=variables, direct={})
    res = lookup.run(terms=term, variables=variables)
    assert res == [u'hello world']

# Generated at 2022-06-22 12:09:56.011830
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    module = LookupModule(loader=None, spi=None, templar=None)

    def dummy_find_file_in_search_path(*args, **kwargs):
        return '/some/path'

    module.find_file_in_search_path = dummy_find_file_in_search_path

    class DummyLoader(object):
        def _get_file_contents(*args, **kwargs):
            return (b"Hello\n", True)

    class DummyTemplar(object):
        class DummyEnv(object):
            def __init__(self):
                self.variable_start_string = '{{'
                self.variable_end_string = '}}'
                self.comment_start_string = '{#'
                self.comment_end_string = '#}'


# Generated at 2022-06-22 12:10:06.722432
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    # DummyVars is used to simulate a variable containing a json string
    class DummyVars(dict):
        # This method is used by AnsibleEnvironment to convert variables containing json into json objects
        def __getitem__(self, key):
            class DummyJson(object):
                def __init__(self, json_value):
                    self.json_value = json_value
                def __str__(self):
                    return self.json_value
            return DummyJson(super(DummyVars, self).__getitem__(key))

    # DummyCliOptions is used to simulate a cli options.
    # These options will be used

# Generated at 2022-06-22 12:10:16.392761
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import os
    import tempfile

    # create a temporary directory
    tmp_dir = tempfile.mkdtemp()
    # create a temporary file
    temp_file = tempfile.mkstemp(dir=tmp_dir)
    os.close(temp_file[0])
    temp_file_name = temp_file[1]
    # create a temporary file
    temp_file = tempfile.mkstemp(dir=tmp_dir)
    os.close(temp_file[0])
    temp_file_name2 = temp_file[1]
    # write content to the temporary file
    fp = open(temp_file_name, 'w')
    fp.write('{{ test }}')
    fp.close()
    # write content to the temporary file

# Generated at 2022-06-22 12:10:27.957642
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    class Options:
        convert_data = False
        jinja2_native = False
        variable_start_string = '{{'
        variable_end_string = '}}'
        comment_start_string = '{#'
        comment_end_string = '#}'
        template_vars = { 'foo': 'bar' }
    lookup.set_options(var_options=Options(), direct=Options())
    class Display:
        verbosity = 1
    lookup.display = Display()
    class Loader:
        class _vault:
            def is_encrypted(self, a):
                return False
        _vault = _vault()