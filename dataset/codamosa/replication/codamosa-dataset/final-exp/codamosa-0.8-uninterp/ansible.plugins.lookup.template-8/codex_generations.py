

# Generated at 2022-06-22 12:01:15.837049
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # create a class object
    look_obj = LookupModule()

    # declare empty variable
    variable1 = {}
    variable2 = {}

    variable1['lookup_template_vars'] = {}
    variable2['lookup_template_vars'] = {}
    variable1['convert_data'] = False
    variable2['convert_data'] = False
    variable1['jinja2_native'] = False
    variable2['jinja2_native'] = False
    variable1['variable_start_string'] = '{{'
    variable2['variable_start_string'] = '{{'
    variable1['variable_end_string'] = '}}'
    variable2['variable_end_string'] = '}}'
    variable1['comment_start_string'] = ''

# Generated at 2022-06-22 12:01:28.367426
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.vars import VariableManager
    from ansible.utils.path import unfrackpath
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inv_obj = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inv_obj)

    lookup = LookupModule()

    #############################################
    # test with missing file
    #############################################
    # test with default AnsibleEnvironment
    no_file = [unfrackpath('/no_file_here')]

# Generated at 2022-06-22 12:01:39.690966
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible.module_utils.six.moves import builtins
    from ansible.module_utils.six import BytesIO

    terms = ['templates/test_template.j2']
    with pytest.raises(AnsibleError):
        LookupModule().run(terms, dict())

    # global env

# Generated at 2022-06-22 12:01:52.096533
# Unit test for method run of class LookupModule

# Generated at 2022-06-22 12:02:04.354857
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test with looking up a template file where the template file exists.
    lookup_module = LookupModule()

    # Set some fake values in vars.

# Generated at 2022-06-22 12:02:05.031747
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-22 12:02:08.985998
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    This test asserts the run method of the LookupModule class without
    testing the Ansible call to the LookupModule class.
    """
    try:
        from unittest.mock import patch, Mock
    except ImportError:
        from mock import patch, Mock

    test_dict = {'vars': {'test_var': 'test_value'}}
    lookup_file = "test_file"
    lookup_file_content = "test_file {{ lookup('vars', 'test_var') }}"
    lookup_file_content_jinja2_native = "test_file {{ test_var }}"
    item = Mock()
    item.get_path.return_value = lookup_file
    b_lookup_file_content = to_bytes(lookup_file_content)
    b_lookup_file

# Generated at 2022-06-22 12:02:17.752617
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch, MagicMock

    m_templar = MagicMock()
    m_templar.template.return_value = 'result'
    m_templar.copy_with_new_env.return_value = m_templar

    class TestLookupModule(LookupModule):
        def __init__(self, loader=None, templar=m_templar, **kwargs):
            super(TestLookupModule, self).__init__(loader, templar, **kwargs)

    terms = ['test_template.j2']
    variables = {'search_path': ['/lookup/path'],
                 'template_vars': {'var': 'value'}}

    mock

# Generated at 2022-06-22 12:02:22.309504
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    LookupModule_obj = LookupModule()
    with pytest.raises(AnsibleError) as exception:
        LookupModule_obj.run(terms=['/'], variables={})
    assert 'the template file / could not be found for the lookup' in to_text(exception.value)

# Generated at 2022-06-22 12:02:34.183771
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # TODO: find a way to get rid of dependency on os.path.join
    import os.path

    import ansible.template
    from ansible.template import AnsibleEnvironment, USE_JINJA2_NATIVE

    directory_terms = './tests/templates'
    directory_terms_list = './tests/templates,./tests/templates2'
    file_terms = './tests/templates/example.j2'

    file_terms_not_exist = './not_exist.j2'
    file_terms_not_exist2 = './not_exist2.j2'


# Generated at 2022-06-22 12:02:48.465082
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # Stub of the private _templar.template method
    templar = MockTemplarVars()
    lookup._templar = templar

    # Stub of the private _loader._get_file_contents method
    # It must return a bytestring
    loader = MockLoader()
    lookup._loader = loader

    terms = [
        MockTerm(template_data="Name is {{ user }}",
                 lookupfile=MockFile(dirname="/root/ansible/playbooks/roles/common/",
                                     basename="templates/authorized_key.j2"))
    ]
    variables = {"user": "Mary", "ansible_search_path": ["/root/ansible/playbooks", "/root/ansible/library"]}

# Generated at 2022-06-22 12:03:00.983024
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # Test 1.
    # Check that method run returns the templated contents of specified files
    # Test 1.1.
    # Test with non-existent files, no |default() filter
    # Test 1.1.1.
    # Test with non-existent file and no vars
    # Test 1.1.1.1.
    # Test with non-existent file and empty vars
    terms = ['non-existent-file']
    variables = { }
    assert lookup.run(terms, variables) == [], \
        "Test 1.1.1.1.  Test with non-existent file and empty vars failed"

    # Test 1.1.1.2.
    # Test with non-existent file and non-empty vars

# Generated at 2022-06-22 12:03:01.402959
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    assert False

# Generated at 2022-06-22 12:03:02.871834
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # GIVEN
    assert True
    # WHEN
    # THEN
    assert True

# Generated at 2022-06-22 12:03:10.617810
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from .test.test_data import get_test_cases
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.template import Templar

    for test_case in get_test_cases(__file__):
        setattr(test_case, 'maxDiff', None)

        # Test with deprecated convert_data option

# Generated at 2022-06-22 12:03:13.914190
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    assert lookup.run(["test_run.j2"], {}) == ['Test of method run.']


# Generated at 2022-06-22 12:03:21.080519
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import jinja2
    from ansible.module_utils._text import to_bytes
    from six import StringIO

    # Setup
    templar = DummyTemplar()
    loader = DummyLoader()
    display = DummyDisplay()
    lookup = LookupModule()
    lookup.set_loader(loader)
    lookup._templar = templar

    # run with empty template
    template_data = ''
    lookupfile = '/path/to/template'
    variables = {'ansible_search_path': ['/some/playbook/dir', '/some/playbook/dir/roles/some_role/files']}
    terms = [lookupfile]

# Generated at 2022-06-22 12:03:32.127197
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # needed when testing lookup modules independently
    import sys
    sys.path.append('../')
    # needed when testing lookup modules independently
    sys.path.append('../../lib/')
    # needed when testing lookup modules independently
    sys.path.append('/usr/lib/python2.7/dist-packages')
    from ansible.module_utils.six import PY3

    terms = ['../test/test_template.j2']
    variables = {
        'role_path': '../test/'
    }

    results = LookupModule().run(terms, variables)

    assert len(results) == 1

    assert results.pop(0) == "bar"

    terms = ['../test/test_template.j2', '../test/test_template_2.j2']


# Generated at 2022-06-22 12:03:42.173359
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Without a real ansible context, calls to "self.get_option" will actually return
    # the **kwarg itself, instead of a dict lookup as they do in a real context.
    # So we must supply the dict explicitly.
    lookup_options = dict(comment_end_string='#}', comment_start_string='{#', convert_data=False,
                          jinja2_native=False, template_vars={}, variable_end_string='}}',
                          variable_start_string='{{')
    jinja_env = AnsibleEnvironment(loader=None)
    templar = jinja_env.get_templar()
    lm = LookupModule(loader=None, templar=templar)

    # Test with a valid template

# Generated at 2022-06-22 12:03:51.413361
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test basic operation
    lookup = LookupModule()
    lookup.set_options({})

    class args:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    class play_context:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    for jinja2_native in (True, False):
        # The following tests use the old style search path, which is not
        # maintained in newer versions of Ansible.
        # When this test is modified to use a newer Ansible, the search path
        # will look like the following:
        #   searchpath = [search_path[0], os.path.join(search_path[0], 'templates'), search_path[1]]
        search_path = None


# Generated at 2022-06-22 12:04:11.586282
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # Test 1:
    # The test_data_dir of ansible/test contains a set of test directories (files, tasks and templates)
    # The templates directory contains a test_template.j2
    # The test_template.j2 contains Hello world!
    # The test_template.j2 uses the ansible variable test_variable and sets it to value test_value
    # The test_template.j2 uses the ansible variable test_default_value and sets its default to value test_default
    # The jinja2_native option is false.
    # The convert_data option is false.
    # The variable_start_string is {{.
    # The variable_end_string is }}.
    # The comment_start_string is {#.
    # The comment_end_string is #}.
   

# Generated at 2022-06-22 12:04:20.274597
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test for checking existence of file returned by lookup
    def test_exist():
        config = {}
        config['convert_data'] = False
        config['template_vars'] = {}
        config['jinja2_native'] = False

        # Create mock object for LookupBase class
        lookup_base_object = LookupBase()

        # pylint: disable=W0212
        lookup_base_object._loader = None
        lookup_base_object._templar = None
        lookup_base_object._SEARCHPATH = None
        lookup_base_object.set_options(var_options=[], direct=config)
        lookup_base_object.find_file_in_search_path = lambda x, y, z: 'test_template.j2'

        # Create mock object for LookupModule class
        lookup_module

# Generated at 2022-06-22 12:04:31.254534
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import StringIO
    from ansible.template import template_from_string
    from ansible.module_utils.six.moves import builtins
    from ansible.module_utils.python import PyModule
    import sys
    import types
    import os

    # Create a mock class for the loader that just returns the template
    # string as if it was the content of an existing file
    class LookupModule_fake_loader():

        def __init__(self):
            pass

        def _get_file_contents(self, path):
            return path

    # Create a mock class for the LookupBase object __init__ takes
    class LookupModule_fake_templar():

        def __init__(self):
            pass


# Generated at 2022-06-22 12:04:31.764494
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-22 12:04:43.588093
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import PY2
    from ansible.module_utils.six.moves import builtins

    if PY2:
        builtin_open = '__builtin__.open'
    else:
        builtin_open = 'builtins.open'

    try:
        import __builtin__ as builtins
    except ImportError:
        import builtins

    o_open = getattr(builtins, 'open')

    class TestLookupModule(LookupModule):
        def __init__(self, *a, **kw):
            self._loader = FakeLoader()
            self._templar = FakeTemplar() # will be copied with new env in real module
            self._display = FakeDisplay()
            super(TestLookupModule, self).__init__(*a, **kw)



# Generated at 2022-06-22 12:04:50.727159
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    lookup._loader = DictDataLoader({
        'test1': '{{ value1 }}',
        'test2': '{{ value2 }}',
    })
    lookup._templar = Templar(loader=lookup._loader)

    ret = lookup.run([
        'test1',
        'test2'
    ], {
        'value1': 'one',
        'value2': 'two'
    }, {})

    assert ret == ['one', 'two']

# Generated at 2022-06-22 12:05:00.410246
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Testing for the template lookup for templates specified as list
    lookup_obj = LookupModule()
    terms = ["ntp.conf.j2"]
    variables = {'template_host': 'testhost', 'ansible_search_path': []}
    ret = lookup_obj.run(terms, variables)
    assert ret == [u'# This file is managed by Ansible\n\nrestrict {{ template_host }}\n']

    # Testing for the template lookup for templates specified as string
    lookup_obj = LookupModule()
    terms = "ntp.conf.j2"
    variables = {'template_host': 'testhost', 'ansible_search_path': []}
    ret = lookup_obj.run(terms, variables)

# Generated at 2022-06-22 12:05:06.623938
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    lookup_options = {
        "convert_data": False,
        "variable_start_string": "{ {",
        "variable_end_string": "} }",
        "jinja2_native": False,
        "template_vars": {},
        "comment_start_string": "{#",
        "comment_end_string": "#}",
    }

# Generated at 2022-06-22 12:05:19.199379
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    def do_test(expected_results, parameters):
        result = LookupModule().run(
            terms=parameters.get('terms', []),
            variables=parameters.get('variables', {}),
            **parameters.get('extra_args', {}))

        assert result == expected_results

    # Test 1
    do_test(
        expected_results=['some result'],
        parameters={
            'terms': ['some_term'],
            'extra_args': {},
            'variables': {}
        }
    )

    # Test 2
    do_test(
        expected_results=['some result'],
        parameters={
            'terms': ['some_term'],
            'extra_args': {},
            'variables': {}
        }
    )

# Generated at 2022-06-22 12:05:32.033497
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.template import Templar
    from ansible.vars.unsafe_proxy import UnsafeProxy

    import pytest
    from collections import Mapping

    # Note: This is not a complete test, just enough to get coverage.
    # In order to successfully test the method run, it would probably
    # be necessary to mock the ansible.vars.unsafe_proxy,
    # ansible.utils.display and the ansible.template.Templar objects.

    variables = dict()
    templar = Templar(loader=None, variables=variables)

    terms = ['samplefile']

# Generated at 2022-06-22 12:06:01.565466
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()

    assert l.run(["./test1.j2"], variables={}, basedir="test/templates") == [u'I am test 0']
    assert l.run(["./test2.j2"], variables={}, basedir="test/templates") == ['This\n', 'will be\n', 'three lines long\n', 'unquoted\n']
    assert l.run(["./test3.j2"], variables={}, basedir="test/templates") == ['This\n', 'will be\n', 'three lines long\n', 'unquoted\n']
    assert l.run(["./test4.j2"], variables={"var":"apples"}, basedir="test/templates") == [u'I like apples']

# Generated at 2022-06-22 12:06:08.916370
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create mocks
    test_templar = MockTemplar

    # Call method
    lm = LookupModule(loader=None, templar=test_templar)
    lookup = lambda v: lm.run(v, variables={'ansible_path': 'foo', 'bar': 'baz'})

    # Check results
    assert lookup(['test.j2']) == ['test template result']
    assert lookup(['test.j2', 'test2.j2']) == ['test template result', 'test2 template result']



# Generated at 2022-06-22 12:06:19.554684
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.yaml.loader import AnsibleLoader

    # this approach using the loader class is used by test.modules.template
    display_options = {'verbosity': 3}

    # test fixture
    terms = ['test/test_template.j2']
    variables = AnsibleLoader('').load('''
        {
            "greeting": "Hello",
            "addressee": "world",
            "punctuation": "!"
        }
    ''')['data']

    # test the return type
    ret = LookupModule(display=display_options).run(terms, variables)
    assert isinstance(ret, list)
    assert len(ret) == 1
    assert ret[0] == terms[0]

    # test the return value

# Generated at 2022-06-22 12:06:30.765389
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.six.moves import StringIO
    import yaml
    import pytest
    from ansible.template import Templar

    my_env = dict(
        template_host='example.org',
        template_uid=10001,
        template_path='/etc/ansible/templates',
        ansible_search_path=['/etc/ansible/playbooks', '/usr/share/ansible/playbooks'],
        ANSIBLE_LOADER='ansible.parsing.dataloader.DataLoader',
        ANSIBLE_TEMPLATE_INTERPRETER='ansible.template.safe_tempate'
    )

    def mock_get_file_contents(path):
        path = os

# Generated at 2022-06-22 12:06:35.066547
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule().run(["/tmp/"], {"basedir": "./"})[0] == "[u'/tmp/']"
    assert LookupModule().run(["list of strings"], {"basedir": "./"})[0] == "[u'list of strings']"

# Generated at 2022-06-22 12:06:46.193308
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Initialize module
    global display
    display = Display()
    lookup_plugin = LookupModule()

    # Create option variables
    global options
    options = {
        'convert_data': False,
        'template_vars': {},
        'jinja2_native': False,
        'variable_start_string': '{{',
        'variable_end_string': '}}',
        'comment_start_string': '{#',
        'comment_end_string': '#}',
    }

    # Test file lookup
    test_file = './test_data/test_template.txt'
    files = lookup_plugin.run([test_file], options, inject=dict(variable='value'), verbosity=0)
    assert files[0] == 'Test 1\n'

    # Test file lookup with new

# Generated at 2022-06-22 12:06:58.275763
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module._loader = DictDataLoader({'test/test.j2': 'test_content'})

    lookuper = LookupModule()
    lookuper._loader = DictDataLoader({'test/test.j2': 'test_content'})
    lookuper._templar = Templar(loader=None, variables={'name': 'value'})

    config = {}
    config['module_name'] = 'template'
    config['module_args'] = './test2.j2'
    config['_raw_params'] = './test2.j2'
    config['_terms'] = './test2.j2'

    kwargs = {}
    kwargs['variables'] = deepcopy(config)

# Generated at 2022-06-22 12:07:10.129358
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = ansible.plugins.lookup.template.LookupModule()
    # Preparing the environment.
    # The method run is based on the following environment variables:
    #   - ansible_search_path
    #   - ansible_inventory
    # The method find_file_in_search_path is based on ansible_search_path.
    # The method _get_file_contents is based on inventory plugin.
    # The method template is based on:
    #   - inventory plugin
    #   - template_vars
    #   - ansible_play_hosts
    #   - ansible_play_batch
    #   - lookup_template_vars
    #   - ansible_playbook
    #   - ansible_play_name
    #   - ansible_play_uid
    #   - ans

# Generated at 2022-06-22 12:07:13.866746
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # tests
    module = LookupModule()
    terms = ['file.j2']
    variables = {}

    result = module.run(terms, variables)
    assert result == []

# Generated at 2022-06-22 12:07:22.486752
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    return_value = LookupModule().run(['./some_template.j2'],
                                      {'template_vars': {'a': 'ANSIBLE1', 'b': 'ANSIBLE2'},
                                       'variable_start_string': '<%',
                                       'variable_end_string': '%>'},
                                      convert_data=False,
                                      jinja2_native=False)
    assert return_value[0] == "==> some_template.j2 <==\n" \
        "<%a%> and <%b%> are ANSIBLE1 and ANSIBLE2 when using NativeJinjaText."

if __name__ == '__main__':
    test_LookupModule_run()

# Generated at 2022-06-22 12:08:04.955143
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookupModule = LookupModule()
    lookupModule.set_loader(construct_fake_loader({
        'role/templates/template.j2': b'{{ ansible_managed }}',
    }))
    lookupModule._templar = FakeTemplar()
    terms = [u'role/templates/template.j2']
    variables = {}
    result = lookupModule.run(terms, variables)
    assert result == [u'demo', u'# test']


# Generated at 2022-06-22 12:08:14.752573
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    terms = ["dburi.j2"]
    ext_vars = dict()
    loader = DataLoader()
    variable_manager = VariableManager(loader=loader)
    inventory = HostVars(loader=loader, variable_manager=variable_manager)
    variable_manager.set_inventory(inventory)
    templar = Templar(loader=loader, variables=variable_manager)

    lookup_module = LookupModule()
    lookup_module._templar = templar
    lookup_module._loader = loader
    result = to_text

# Generated at 2022-06-22 12:08:26.443110
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    os.environ['ANSIBLE_CONFIG']='test/ansible.cfg'
    os.environ['ANSIBLE_SEARCH_PATHS']='/path/to/my/files'

    # Create a fake ansible.cfg
    with open('test/ansible.cfg', 'w') as f:
        f.write('[defaults]\nroles_path=%s\n' % os.environ['ANSIBLE_SEARCH_PATHS'])

    # Create a fake template file
    with open('test/templates/hosts.j2', 'w') as f:
        f.write('{% for host in hosts %}\n{{host}}\n{% endfor %}')

    # Create a fake inventory file

# Generated at 2022-06-22 12:08:31.249819
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.vault import VaultLib

    vault_password = 'dummy'
    vault = VaultLib(vault_password)

    test_cases = list()

    # A simple test case
    test_case = dict()
    test_case['terms'] = ['./tests/vault/test.yml']
    test_case['variables'] = dict()
    test_case['options'] = dict()
    test_case['expect_http_status'] = 200
    test_case['expect_response'] = ['foo: bar\n']
    test_cases.append(test_case)

    # A simple test case
    test_case = dict()
    test_case['terms'] = ['./tests/vault/test-vault.yml']
    test_case['variables']

# Generated at 2022-06-22 12:08:42.540181
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    import sys
    module = sys.modules[__name__]
    module.__file__ = '<ansible_module_template>'

    print('---')


# Generated at 2022-06-22 12:08:54.529561
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup.template import LookupModule
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager)
    variable_manager.set_inventory(inventory)

    lookup_obj = LookupModule()
    lookup_obj.set_loader(loader)
    lookup_obj.set_variable_manager(variable_manager, loader=loader)

    # lookup_file is a temporary file in the directory of this script containing
    # a Jinja2 template which prints out two variables.

# Generated at 2022-06-22 12:08:56.312561
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: create unit test for this lookup module
    return

# Generated at 2022-06-22 12:09:06.307612
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    template_data = """
        # {{ lookup("template", "./some_template.j2", comment_start_string="[#", comment_end_string="#]") }}
        {# {{ lookup("template", "./some_template.j2", comment_start_string="{#", comment_end_string="#}") }} #}
        # {{ lookup("template", "./some_template.j2") }}
        """

    results = lm.run([template_data], dict(temp_var='test'), comment_start_string=None, comment_end_string=None)
    assert results[0] == template_data


# Generated at 2022-06-22 12:09:17.439761
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    v = {'searchpath': ['/home/username/.ansible/tmp/ansible-tmp-1528015363.24-96442944444444/ansible'], '_ansible_tmp_dir': '/home/username/.ansible/tmp/ansible-tmp-1528015363.24-96442944444444/', '__ansible_module_name': 'template', 'ansible_facts': {}, 'template_host': 'localhost', 'template_path': '/home/username/.ansible/tmp/ansible-tmp-1528015363.24-96442944444444/ansible/test_jinja2.j2', 'template_uid': '1000', 'template_encoding': 'UTF-8'}

# Generated at 2022-06-22 12:09:28.912649
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    variable_start_string = '{{'
    variable_end_string = '}}'
    comment_start_string = '#'
    comment_end_string = None
    variables = {'variable_start_string': variable_start_string, 'variable_end_string': variable_end_string, 'comment_start_string': comment_start_string, 'comment_end_string': comment_end_string}
    # When all files exist and ok
    terms = ['./doc/examples/ansible.cfg_example']
    res = lookup_module.run(terms, variables)

# Generated at 2022-06-22 12:11:01.444558
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.template import template
    from ansible.module_utils.six import PY3
    from ansible.module_utils._text import to_bytes, to_native
    from ansible.parsing.ajson import AnsibleJSONEncoder
    from ansible.module_utils.common.collections import is_sequence
    from ansible.template.safe_eval import unsafe_eval
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    import json

    if PY3:
        # In Python 3, repr changes along with the repr of str
        # Here is an example:
        # Python 2.7: "u'foo'"
        # Python 3.5: "'foo'"
        # We have to take this into account for these tests to pass
        unicode_repr = "'u'foo''"