

# Generated at 2022-06-22 12:01:06.168833
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO
    pass

# Generated at 2022-06-22 12:01:07.146256
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: implement this unit test
    pass

# Generated at 2022-06-22 12:01:11.248420
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    global LOOKUP, LOOKUP_PLUGIN_KWARGS, LOOKUP_PLUGIN_TERMS
    result = LOOKUP.run(LOOKUP_PLUGIN_TERMS, LOOKUP_PLUGIN_KWARGS)
    print(result)

# Generated at 2022-06-22 12:01:13.843845
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    result = LookupModule().run(terms=['{{ foo }}', '{{ bar }}'], variables={'foo': 'Foo', 'bar': 'Bar'})

    assert result == ['Foo', 'Bar']


# Generated at 2022-06-22 12:01:18.857782
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    """
    ins = LookupModule('.', {'a': 'A', 'b': 'B'})
    ins.set_options({'a': 'A', 'b': 'B'})

    print(ins.run(['./a.j2', './b.j2']))
    """

    pass

# Generated at 2022-06-22 12:01:31.375556
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Unit test for method run of class LookupModule"""

    lookup_module = LookupModule()

    # Generate input parameters

    #########################################################################
    # Case 1: No lookup_template_vars option set.
    #########################################################################

    # Expected Result:

    #########################################################################
    # Case 2: Variable_start_string option set.
    #########################################################################

    # Expected Result:

    #########################################################################
    # Case 3: Variable_end_string option set.
    #########################################################################

    # Expected Result:

    #########################################################################
    # Case 4: Convert_data option set.
    #########################################################################

    # Expected Result:

    #########################################################################
    # Case 5: Comment_start_string option set.
    #########################################################################

    # Expected Result:

    #################################

# Generated at 2022-06-22 12:01:41.782538
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os

    lookup_plugin = LookupModule()
    lookup_plugin.set_options(variable_start_string='{', variable_end_string='}')

    # original Ansible file lookup
    lookup_plugin.set_loader(None)
    lookup_plugin._templar = None

    result = lookup_plugin.run(['./tests/fixtures/template_example.j2'], {}, convert_data=False)[0]
    assert result == 'name: {{ ansible_hostname }}\n'

    # test with convert_data
    lookup_plugin.set_loader(None)
    lookup_plugin._templar = None

    result = lookup_plugin.run(['./tests/fixtures/template_example.j2'], {}, convert_data=True)[0]

# Generated at 2022-06-22 12:01:50.521262
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['../../../test/files/test_templates/good.j2']
    variables = {'ansible_search_path': ['/home/ansible', '/etc/ansible/hosts']}
    lookup_module = LookupModule()
    lookup_module._loader = FakeLoader()
    lookup_module._templar = FakeTemplar()

    result = lookup_module.run(terms, variables)
    assert 'test variable string' in result[0]

# Fake class to simulate _load_file from ansible.parsing.dataloader.BaseDataLoader

# Generated at 2022-06-22 12:02:02.836035
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()

    result = module.run([], {})
    assert result == []

    term = './some_template.j2'
    lookupfile = ''
    variables = {}
    kwargs = {}
    result = module.run([term], variables, **kwargs)
    assert result == []

    term = './some_template.j2'
    lookupfile = './some_template.j2'
    variables = {}
    kwargs = {}
    kwargs['_original_file'] = './some_template.j2'
    kwargs['_loader'] = DummyLoader()
    result = module.run([term], variables, **kwargs)
    assert result == ['some template']

    term = './some_template.j2'

# Generated at 2022-06-22 12:02:05.735632
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    # test
    assert len(module.run(terms=[], variables=None, **{})) == 0

# Generated at 2022-06-22 12:02:19.182685
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Try to pre-process "some_template.j2"
    terms = ['./some_template.j2']
    variables = {}
    kwargs = {}
    LookupModule(loader=None, templar=None, shared_loader_obj=None).run(terms, variables, **kwargs)

    # Try to pre-process "some_template.j2" with different variable start and end string
    variable_start_string = '[%'
    variable_end_string = '%]'
    terms = ['./some_template.j2']
    variables = {}
    kwargs = {}

# Generated at 2022-06-22 12:02:30.864451
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # pylint: disable=line-too-long
    # Patch lookupbase methods which are called by LookupModule.run method but we don't care about for this test
    from ansible.plugins.lookup import LookupBase  # noqa
    LookupBase.set_options = lambda self, **kwargs: None
    LookupBase.find_file_in_search_path = lambda self, variables, subdir, file: file
    # pylint: enable=line-too-long
    # Patch get_option
    LookupModule.get_option = lambda self, option: None if option == 'jinja2_native' else {}

    # Test with one template to template
    ret = [u"one\nthree\n"]
    terms = ['lookup_plugin.j2']
    lookup = LookupModule()
    # Add

# Generated at 2022-06-22 12:02:40.682067
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import tempfile
    import pytest

    test_content = 'hello'
    fd, path = tempfile.mkstemp()
    f = os.fdopen(fd, 'w')
    try:
        f.write(test_content)
    finally:
        f.close()

    def test_run(jinja2_native, convert_data, expected_content):
        lookup_plugin = LookupModule()
        assert lookup_plugin.run([path], {}, **{'jinja2_native': jinja2_native,
                                               'convert_data': convert_data})[0] == expected_content

    test_run(jinja2_native=True, convert_data=True, expected_content=test_content)

# Generated at 2022-06-22 12:02:52.418215
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.utils import context_objects as co
    from ansible.playbook.play_context import PlayContext

    lookup_module = LookupModule()
    test_directory = os.path.dirname(os.path.realpath(__file__))
    fixture_file = os.path.join(test_directory, '..', '..', 'test', 'sanity', 'lookup_plugins', 'template', 'template_test.j2')
    assert os.path.exists(fixture_file)
    display.vvvv = True
    display.verbosity = 4
   

# Generated at 2022-06-22 12:02:56.786411
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """return a list of pathnames matching a pathname pattern"""
    module_ = LookupModule()
    assert module_.run(['debug.j2'], dict(this=['that'], other=dict(lala='lele'))) == []

# Generated at 2022-06-22 12:03:07.877951
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # start with an empty variable hash
    variable_hash = {}
    # define mock objects for AnsibleFileLoader and AnsibleOptions
    mock_AnsibleFileLoader = MockAnsibleFileLoader()
    mock_AnsibleOptions = MockAnsibleOptions()
    mock_AnsibleOptions.tags = None
    mock_AnsibleOptions.skip_tags = None
    mock_AnsibleOptions.force_handlers = None
    mock_AnsibleOptions.step = None
    mock_AnsibleOptions.start_at_task = None
    mock_AnsibleOptions.verbosity = None
    mock_AnsibleOptions.forks = None
    mock_AnsibleOptions.module_path = None
    mock_AnsibleOptions.private_key_file = None
    mock_AnsibleOptions.remote_user

# Generated at 2022-06-22 12:03:17.817243
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # setup test environment
    import os
    import yaml
    test_dir = os.path.dirname(__file__)
    data_dir = os.path.join(test_dir, 'lookup_data')

    # reference AnsibleConfig class
    class AnsibleConfig(object):
        pass

    # initialize test class, then reference its class methods
    class TestClass(object):
        def __init__(self):
            self.test_obj = LookupModule()
            self.test_obj.set_loader = self.test_obj._loader.set_basedir
            self.test_obj.set_templar = self.test_obj._templar.set_available_variables

    # initialize AnsibleConfig object and test object
    ac = AnsibleConfig()
    tc = TestClass()
    ac.based

# Generated at 2022-06-22 12:03:26.418562
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Test lookup module for the template plugin for the reserved keyword 'case'."""
    luc = LookupModule()
    options = {'disable_lookups': True, 'jinja2_native': False}
    terms = ['./test_files/test_case.j2']
    nvariables = {}
    luc.set_options(var_options=nvariables, direct=options)
    ret = to_text(luc.run(terms, nvariables, **options)[0]).strip()
    assert ret == "Test string."

# Generated at 2022-06-22 12:03:36.065084
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Unit test variables
    lookup_module = LookupModule()
    lookup_module._templar.environment.loader = DictLoader
    lookup_module._loader.get_basedir = lambda x: os.path.join(os.path.dirname(__file__), "lookup_fixtures")
    ansible_vars = dict(
        test_var1 = "test_var1",
        test_var2 = "test_var2"
    )
    ansible_search_path = []
    os_path_dirname_method_mock = MagicMock(return_value = os.path.join(os.path.dirname(__file__), "lookup_fixtures"))
    lookup_module._loader.get_basedir = MagicMock(return_value = os.path.dirname(__file__))

# Generated at 2022-06-22 12:03:47.606920
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader

    def return_term(term):
        return term

    lookup = LookupModule()
    lookup.set_options({'convert_data': True, 'template_vars': {'name': 'Batman'}})
    lookup._templar = mock.MagicMock()
    lookup._loader = DataLoader()
    lookup.find_file_in_search_path = return_term
    test_file = './test/fixtures/files/test_template.j2'
    result = lookup.run(terms=[test_file], variables={'type': 'rich'})
    assert result[0] == 'The name is Batman and the type is rich.\nAnd he is Batman.\n'


if __name__ == '__main__':
    import doctest

# Generated at 2022-06-22 12:04:07.970520
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.errors import AnsibleError
    from ansible.plugins.lookup import LookupBase
    from ansible.module_utils._text import to_text, to_bytes
    from ansible.template import generate_ansible_template_vars
    from ansible.module_utils.six import PY3
    from ansible.utils.hashing import checksum_s
    from ansible.utils.path import unfrackpath

    lookup = LookupModule()
    lookup._loader = DummyLoader(path_relative='templates', path='/a/b/c/templates')
    lookup._templar = MockTemplar()
    lookup._templar.available_variables = {'foo': 'bar'}
    lookup.set_options({})


# Generated at 2022-06-22 12:04:20.249898
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import combine_vars
    class DummyVars(dict):
        def get(self, key, *args, **kwargs):
            return self.get(key)

    loader = DataLoader()
    variables = VariableManager()
    inv_data = dict()
    inv_data['hostvars'] = dict()
    inv_data['hostvars']['myhost'] = dict()
    inv_data['hostvars']['myhost']['arg1'] = "bar"
    inv_data['vars'] = dict()
    inv_data['group_names'] = dict()
    inv_data['group_names']['mygroup'] = dict()

# Generated at 2022-06-22 12:04:22.315998
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule.run(LookupModule, ['./some_template.j2'], {}) is None

# Generated at 2022-06-22 12:04:25.381559
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # If a class does not have any unit tests, then this method is not implemented.
    # Hence the method below just raises the exception NotImplementedError.
    raise NotImplementedError("Not implemented yet")



# Generated at 2022-06-22 12:04:34.926456
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class TestEnvironment:
        def __init__(self):
            self.lookup_loader = None
            self.lookup_basedir = None
            self.templar = None
            self.searchpath = None

    class TestLoader:
        def __init__(self):
            self.test_data = {}

        def set_data(self, data):
            self.test_data = data

        def _get_file_contents(self, path):
            # If path exists, return contents
            if path in self.test_data:
                return self.test_data[path], True

            # Return empty string if path does not exist.
            # get_file_contents() does not return the 'show_data' argument for
            # a path that does not exist, so it is unclear what the proper value
            # for this

# Generated at 2022-06-22 12:04:45.928185
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Define template file and expected result
    test_file = "test/test_template.txt"
    test_file_expected_result = "TEST VARIABLE VALUE FROM TEMPLATE MODULE: test_value\n"

    # Define test variables and template vars to be passed to lookup plugin
    test_vars = {}
    test_vars['test_variable'] = 'test_value'
    test_vars['ansible_search_path'] = ["test/"]
    test_vars['template_path'] = "test_template.txt"
    test_template_vars = {'test_variable': 'test_value'}

    # Create LookupModule instance
    lookup_module = LookupModule()

    # Fake the loader object

# Generated at 2022-06-22 12:04:51.909685
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    display = Display()

    terms = [ './some_template.j2' ]
    lookup_module = LookupModule()
    lookup_module.set_loader(DictDataLoader({ 'templates/some_template.j2': 'Hello {{ foo }}!' }))
    lookup_module.set_basedir('/home/jdoe')
    lookup_module.set_vars({ 'foo': 'World' })

    results = lookup_module.run(terms, variables=None, convert_data=True)
    assert results[0] == 'Hello World!'



# Generated at 2022-06-22 12:05:00.915998
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # If we cannot import jinja2 we cannot test template lookup
    try:
        import jinja2
    except ImportError:
        return

    lookup_templ = LookupModule()

    # Simulate the first argument of method run
    test_terms = [
        'test_term1',
        'test_term2'
    ]

    # Simulate the second argument of method run
    test_variables = {
        'test_variable1': 'test_value1',
        'test_variable2': 'test_value2'
    }

    test_additional_variables = {
        'test_variable3': 'test_value3',
        'test_variable4': 'test_value4'
    }

    test_variable_start_string = '{{'

# Generated at 2022-06-22 12:05:08.920225
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Creating objects to make a mock method of 'to_bytes' in 'AnsibleModule' class.
    test_AnsibleModule_to_bytes = AnsibleModule(argument_spec={})
    test_AnsibleModule_to_bytes.params = {}
    test_AnsibleModule_to_bytes.params['convert_data'] = False
    test_AnsibleModule_to_bytes.params['template_vars'] = {}

    # Creating mocks for class 'AnsibleModule'
    class test_AnsibleModule_class:
        def __init__(self, argument_spec):
            self.argument_spec = argument_spec

    test_AnsibleModule = test_AnsibleModule_class(argument_spec={})
    test_AnsibleModule.to_bytes = test_AnsibleModule_

# Generated at 2022-06-22 12:05:21.677293
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    terms = ['./../../../examples/files/foo.j2']
    result = module.run(terms, {})
    assert result[0] == '# This playbook is configured to run on hosts\n# for which the variable \'ansible_ssh_user\',\'ansible_winrm_user\' is defined\n#\n#   ansible_ssh_user=<username> ansible_winrm_user=<username>\n\n# Specify the hosts to execute on.\n# inventory: can be group name or hostname\n#   ansible_ssh_host=<ip or dns name> ansible_winrm_host=<ip or dns name>\n\n[inventory]\nlocalhost\n'

# Generated at 2022-06-22 12:05:51.436341
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    # Test normal operation
    # NOTE: options must be set before running run
    lookup_module.set_options(direct={'convert_data': True,
                                      'template_vars': {'from': 'templating', 'msg': 'Hello'}})
    lookup_module.set_options(var_options={})
    term = {0: './some_template.j2'}
    terms = [term[0]]
    variables = {}
    res = lookup_module.run(terms, variables, **{})
    assert res == ['Hello from templating!']

    # Test error case
    lookup_module = LookupModule()

# Generated at 2022-06-22 12:06:01.388558
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_obj = LookupModule()
    lookup_obj.set_loader(None)
    lookup_obj._templar = None
    lookup_obj._loader = None
    lookup_obj.set_options({'convert_data': True,
                            'template_vars': {},
                            'variable_start_string': '{{',
                            'variable_end_string': '}}',
                            'comment_start_string': '{#',
                            'comment_end_string': '#}'})
    from ansible.template import Templar

# Generated at 2022-06-22 12:06:11.193961
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookupModule = LookupModule()
    lookupModule.set_loader({
        '_get_file_contents': lambda x: ('', False)
    })
    lookupModule.set_basedir('')

    # Just testing the 'normal' case. The other cases are covered by tests for the templar
    # lookupModule.run(['tests/templating_tests/jinja_test_simple.j2'], variables)
    # lookupModule.run(['tests/templating_tests/jinja_test_complex.j2'], variables)
    variables = {
        'name': 'Test'
    }
    searchpath = ['/']


# Generated at 2022-06-22 12:06:21.992724
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    #
    # Tests the templating of a file in the lookup module
    #
    lookup_module = LookupModule()

    template_file = "./tests/files/test_template.j2"
    f = open(template_file, "rb")
    template_content = f.read()
    f.close()
    template_content = to_unicode(template_content, errors='surrogate_or_strict')
    t2 = Template(template_content)
    template_result = t2.render(foo="bar")
    terms = [template_file]
    variables = {}
    file_search_paths = ["./tests/files"]
    var_options = {"file_search_paths": file_search_paths}
    # TODO: How to get a valid self.loader?
    lookup

# Generated at 2022-06-22 12:06:26.123958
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Implementing tests for LookupModule
    # is a work in progress.
    # Please do not remove this line, it is absolutely needed to make
    # tests pass.
    raise NotImplementedError

# Generated at 2022-06-22 12:06:37.683948
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # We need a context for the templar
    from ansible.template import Templar
    templar = Templar(variables={})

    # Create the LookupModule object to be tested
    from ansible.plugins.lookup.template import LookupModule
    l = LookupModule(templar=templar._available_variables, loader=None, templar=templar)

    # We need the 'test_file' fixture
    import pytest

# Generated at 2022-06-22 12:06:44.822136
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    class Options:
        def __init__(self):
            self.convert_data = False
            self.jinja2_native = False
            self.template_vars = {}
    class Variables:
        def __init__(self):
            self.ansible_search_path = ['templates']
    variables = Variables()
    module.set_options(var_options=variables, direct=Options.__dict__)
    terms = ['example.j2']
    result = module.run(terms, variables, **Options.__dict__)
    print(result)

# Generated at 2022-06-22 12:06:52.812212
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import tempfile

    tmp_dir = tempfile.mkdtemp()

    # create test files
    f1 = open(os.path.join(tmp_dir, "test.txt"), "w")
    f1.write("""{{ lookup('env', 'ansible_user') }}""")
    f1.close()
    f2 = open(os.path.join(tmp_dir, "test2.j2"), "w")
    f2.write("""{{ ansible_user }}""")
    f2.close()

    # create test env variable
    os.environ["ANSIBLE_USER"] = "jdoe"


# Generated at 2022-06-22 12:07:04.681065
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    x = 'hello'
    y = 'world'
    lookup_file = 'test.j2'
    lookup_path = lookup_module.find_file_in_search_path(variables={'x': x, 'y': y}, subdir='templates', file_name=lookup_file)
    display.vvvv("File lookup using %s as file" % lookup_path)

    assert lookup_path == 'test.j2'

    # Force ansible to use the local lookup module
    lookup_module._loader = DictDataLoader({'lookup_plugins': {'template': lookup_module}})
    lookup_module._templar = Templar(loader=lookup_module._loader, variables={'x': x, 'y': y})

    # The template will have access to all

# Generated at 2022-06-22 12:07:16.772976
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test setting of lookup vars
    from ansible.utils.display import Display
    display = Display()
    display.verbosity = 3

    # Test with search path set
    from ansible.context import context
    context.CLIARGS = {'roles_path': ['/home/user/ansible/roles'],
                       'module_path': ['/home/user/ansible/modules']}
    import ansible.plugins.loader
    # Sample templates
    template_dir = os.path.join(os.path.dirname(ansible.plugins.loader.__file__), 'lookup_plugins', 'template/templates')
    test_template_file = os.path.join(template_dir, 'test_template.j2')

# Generated at 2022-06-22 12:08:08.084821
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = AnsibleModule(argument_spec=dict(
        terms=dict(type='list'),
        convert_data=dict(type='bool'),
        variable_start_string=dict(type='str'),
        variable_end_string=dict(type='str'),
        jinja2_native=dict(type='bool'),
        template_vars=dict(type='dict'),
        comment_start_string=dict(type='str'),
        comment_end_string=dict(type='str'),
    ))
    lookup_plugin = LookupModule()

    terms = ['./some_template.j2']

# Generated at 2022-06-22 12:08:17.410007
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = AnsibleModule(argument_spec={'_terms':dict(type='list', required=True), 'variable_start_string':dict(type='str', required=False, default='{{'), 'variable_end_string':dict(type='str', required=False, default='}}'), 'comment_start_string':dict(type='str', required=False, default='{#'), 'comment_end_string':dict(type='str', required=False, default='#}'), 'convert_data':dict(type='bool', required=False, default=False), 'template_vars':dict(type='dict', required=False, default={}), 'jinja2_native':dict(type='bool', required=False, default=False)},
        supports_check_mode=False)

    lookup = LookupModule()
    # Expected return of method

# Generated at 2022-06-22 12:08:23.601622
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup.template import LookupModule
    import sys
    import __builtin__ as builtins

    if sys.version_info < (2, 7):
        import unittest2 as unittest
    else:
        import unittest

    class TestLookupModule(unittest.TestCase):

        def setUp(self):
            self._loader, self._lookup = self._load_plugins()

        def tearDown(self):
            self._loader, self._lookup = None, None

        def _load_plugins(self):
            # make sure any lookups are loaded
            self._loader = LookupModule()

            # create a fake environment so we can call our lookup plugin
            templar = Dictable()
            templar._templar = Dictable()
            templar

# Generated at 2022-06-22 12:08:29.782307
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    templar = DummyTemplar()
    module = LookupModule(templar=templar)

    variables = dict(
        ansible_search_path=[
            'roles/example/vars',
            'roles/example/tasks',
            'roles/example/defaults',
            'roles/example/meta',
            'roles/example/handlers',
            'roles/example/files',
            'roles/example/templates',
            'roles/example/library',
            'roles/example/lookup_plugins',
            'roles/example/filter_plugins',
            'roles/example/tests',
        ])
    terms = ['index.html.j2']

# Generated at 2022-06-22 12:08:35.220123
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # pylint: disable=unused-variable
    global LOOKUP_REGISTRY  # pylint: disable=global-statement

    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    # AnsibleEnvironment no longer exists, see https://github.com/ansible/ansible/issues/60067
    class AnsibleEnvironment(object):
        pass

    class LookupLoader(object):
        def __init__(self):
            self.path_mapper = {'templates': '/path/to/template/directory'}
            self.path_searched = {}
            self.file_contents = {}


# Generated at 2022-06-22 12:08:38.150135
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ('/etc/passwd',)
    lookup = LookupModule()
    res = lookup.run(terms)
    assert len(res) == 1

# Generated at 2022-06-22 12:08:45.658050
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Imports
    import ansible.playbook.play_context
    import ansible.vars.manager

    # Setup
    text_data = 'text_data'
    b_data = to_bytes(text_data, encoding='utf-8')

    lookupfile = 'lookupfile'
    vars = dict()
    searchpath = ['/data/sandbox/ansible/lib/ansible/modules/extras',
                  '/data/sandbox/ansible/lib/ansible/modules/core',
                  '/data/sandbox/ansible/lib/ansible/modules']
    variable_start_string = '{{'
    variable_end_string = '}}'
    comment_start_string = '{#'
    comment_end_string = '#}'
    lookup_template_vars = dict()


# Generated at 2022-06-22 12:08:57.345014
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a mock Ansible variable
    mock_variable = {
        'ansible_search_path': [
            '/base/path'
        ],
        'template_path': '/base/path/templates/test.yml.j2'
    }

    # Create a mock templar
    mock_templar = object()

    # Create an LookupModule object
    lookup_plugin = LookupModule()

    # Initialize the lookup_plugin to use the mock templar
    lookup_plugin._templar = mock_templar

    # Initialize the lookup_plugin with the mock variable
    lookup_plugin.set_options(var_options=mock_variable)

    # Create a mock loader
    class MockLoader:
        def __init__(self):
            pass

    mock_loader = MockLoader()

   

# Generated at 2022-06-22 12:09:02.238475
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    assert lookup_module is not None
    terms = ['./some_template.j2']
    variables = {
      'keyName': 'valueName',
      'anotherKeyName': 'anotherValueName'
    }
    assert lookup_module.run(terms, variables) is not None

# Generated at 2022-06-22 12:09:06.650467
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lh = LookupModule()
    ret = lh.run([], dict(convert_yaml=True))
    assert ret == [], ret
    ret = lh.run([], dict(convert_yaml=False))
    assert ret == [], ret

# Generated at 2022-06-22 12:10:34.154953
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def _test_template_run(variable_start_string, variable_end_string, comment_start_string, comment_end_string):
        def _test_template(template):
            templar = Templar(variables=dict(x='x'), loader=DictDataLoader())
            module = LookupModule()
            module.set_loader(templar._loader)
            module._templar = templar
            module.set_options(var_options=dict(template_vars=dict(y='y'),
                                                variable_start_string=variable_start_string,
                                                variable_end_string=variable_end_string,
                                                comment_start_string=comment_start_string,
                                                comment_end_string=comment_end_string))

# Generated at 2022-06-22 12:10:42.424405
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_base = LookupBase()
    lookup_base.set_loader('/usr/libexec/ansible/module_utils/ansible_lookup')
    lookup_base.set_vault_secret('secret')

    lookup_module = LookupModule()
    lookup_module.set_loader('/usr/libexec/ansible/module_utils/ansible_lookup')
    lookup_module.set_vault_secret('secret')


# Generated at 2022-06-22 12:10:54.060570
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """ unit test for method run of class LookupModule """
    
    # TEST_CASE_BEGIN
    # run
    lookup_module = LookupModule()
    lookup_module._templar = None
    lookup_module._loader = None
    lookup_module.set_options = lambda var_options, direct: None
    lookup_module.get_option = lambda option: None
    lookup_module.find_file_in_search_path = lambda variables, directory, filename: './templates/test_template.j2'
    lookup_module._loader._get_file_contents = lambda lookupfile: ("{{ 'Hello' }}", False)
    templar = lookup_module._templar
    
    # mock methods for get_option

# Generated at 2022-06-22 12:11:05.906138
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    #Test with missing file
    lookup_module = LookupModule()
    lookup_module.set_loader(object)
    lookup_module._templar = object
    lookup_module._loader.path_dwim = lambda b: b
    lookup_module._loader.get_basedir = lambda b: b
    lookup_module._loader.path_exists = lambda b: False
    with pytest.raises(AnsibleError) as dummy:
        result = lookup_module.run(terms = ["non-existant-file"],
                                   variables = {"template_vars": {}},
                                   variable_start_string = "{",
                                   variable_end_string = "}",
                                   jinja2_native = False,
                                   convert_data_p = False)