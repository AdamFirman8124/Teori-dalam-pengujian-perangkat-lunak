

# Generated at 2022-06-22 12:01:16.533457
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = [
        "{{ lookup('template', './some_template.j2') }}",
        "{{ lookup('template', './some_template.j2', variable_start_string='[%', variable_end_string='%]') }}",
        "{{ lookup('template', './some_template.j2', comment_start_string='[#', comment_end_string='#]') }}"
    ]
    
    ansible_options = {
        'variable_start_string': '[%',
        'variable_end_string': '%]',
        'comment_start_string': '[#',
        'comment_end_string': '#]',
    }
    
    lookup_module = LookupModule()
    results = lookup_module.run(terms, variables=ansible_options)

# Generated at 2022-06-22 12:01:20.886721
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test empty
    lookup = LookupModule()
    assert lookup.run([], dict()) == []

    # Test missing template
    lookup = LookupModule()
    assert lookup.run(['missing_template'], dict()) == ["missing_template"]

# Generated at 2022-06-22 12:01:26.665662
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    # check if argument terms is mandatory
    try:
        terms = None
        lookup_module.run(terms,'')
    except TypeError:
        pass

    # check if argument variables is mandatory
    try:
        variables = None
        lookup_module.run('',variables)
    except TypeError:
        pass

# Generated at 2022-06-22 12:01:38.218584
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Set up variables to use in testing
    lookup = LookupModule()
    terms = './some_template.j2'
    variables = {
        'ansible_search_path': [
            os.path.join('one', 'two', 'three')
        ]
    }
    # The original 'optional' parameter has been removed and is not needed for the test
    # optional = False
    convert_data = True
    with_items = False
    lookup_template_vars = {}
    jinja2_native = True
    variable_start_string = '{{'
    variable_end_string = '}}'
    comment_start_string = '{#'
    comment_end_string = '#}'

# Generated at 2022-06-22 12:01:51.232153
# Unit test for method run of class LookupModule

# Generated at 2022-06-22 12:02:03.292046
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()

    terms = dict(
        terms = [ 'test1.txt.j2', 'test2.txt.j2' ],
        convert_data = False,
        variable_start_string = '{{',
        variable_end_string = '}}',
        comment_start_string = '{#',
        comment_end_string = '#}',
        jinja2_native = False
    )


# Generated at 2022-06-22 12:02:14.381575
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.vault import VaultLib
    from ansible.plugins.lookup import LookupBase
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.vars import VariableManager


# Generated at 2022-06-22 12:02:26.263634
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # pylint: disable=too-many-locals,too-many-statements
    # pylint: disable=too-many-branches,fixme,line-too-long
    import os
    import os.path
    import tempfile
    import unittest
    from ansible.utils.display import Display
    from ansible.utils.vars import combine_vars
    from ansible.plugins.lookup import LookupBase
    from ansible.template import generate_ansible_template_vars
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.parsing.dataloader import DataLoader

    class TestTemplar(object):
        ''' Dummy class for testing purposes '''


# Generated at 2022-06-22 12:02:37.867876
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.test_plugins import AnsibleLookupPluginTestCase
    from ansible.module_utils.test_plugins import AnsibleTestCase, AnsibleExitJson
    from ansible.module_utils._text import to_bytes, to_native
    from ansible.module_utils.six import PY3

    import yaml
    from jinja2 import Environment, PackageLoader

    # example template_vars
    template_vars = {'foo': 'bar', 'baz': 'qux'}

    # example jinja2 template_data

# Generated at 2022-06-22 12:02:49.160630
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six.moves import StringIO

    class Fake_Loader():
        def __init__(self, return_data):
            self.return_data = return_data

        def get_basedir(self, path):
            if path is None:
                return None
            else:
                return os.path.dirname(path)

        def is_file(self, path):
            if path is None:
                return False
            if path.endswith('lookup_fixture.txt'):
                return True
            else:
                return False

        def _get_file_contents(self, path):
            if path.endswith('lookup_fixture.txt'):
                return (self.return_data, False)
            else:
                return ('', False)


# Generated at 2022-06-22 12:03:04.353243
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.template.vars import AnsibleVars

    # Test with simple string
    module = LookupModule()
    assert module.run([ "\"{{ 'Hello' }}\"" ], AnsibleVars({})) == [ "Hello" ]

    # Test with complex string
    module = LookupModule()
    assert module.run([ "\"{{ 'Hello world' }}\"" ], AnsibleVars({})) == [ "Hello world" ]

    # Test with a variable
    module = LookupModule()
    assert module.run([ "\"{{ var }}\"" ], AnsibleVars({ "var": "Hello" })) == [ "Hello" ]

# Generated at 2022-06-22 12:03:16.223616
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.basic import *
    from ansible.module_utils.six import iteritems
    from ansible.module_utils import lookup_loader
    from ansible.module_utils.jinja2.environment import ansible_environment

    lookup = lookup_loader.get('template')

# Generated at 2022-06-22 12:03:21.622773
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    display = get_Display()
    display.display = mock.MagicMock()
    templar = Templar(loader=None, variables={})
    lookup_plugin = LookupModule(loader=None, templar=templar)
    # call run
    # assert
    assert False is lookup_plugin.run()

# Generated at 2022-06-22 12:03:31.018246
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    template_data = '{% if True %}True{% else %}False{% endif %}'

    templar = AnsibleEnvironment(loader=None)
    lookup = LookupModule()
    lookup.set_loader(None)
    lookup.set_templar(templar)

    assert lookup.run(terms=['/path/to'], variables={}) == []
    lookup._loader._templates = {'/path/to': (to_bytes(template_data), 'hash')}
    assert lookup.run(terms=['/path/to'], variables={}) == [template_data]
    assert lookup.run(terms=['/path/to2'], variables={}) == []

# Generated at 2022-06-22 12:03:41.758668
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    args = dict(
        _raw=dict(
            src='my_file.j2',
        ),
        variable_start_string='{%',
        variable_end_string='%}',
        convert_data=False,
        jinja2_native=True,
        template_vars=dict(key='value'),
    )
    mock_templar = MockTemplar()
    mock_loader = MockDataLoader()
    lookup_plugin = LookupModule()
    lookup_plugin.set_loader(mock_loader)
    lookup_plugin.set_templar(mock_templar)
    # We need a valid path because find_file_in_search_path will
    # fail if search_path is an empty array

# Generated at 2022-06-22 12:03:53.376184
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test the following scenarios:
    # - lookup_template_vars none passed, no jinja2_native
    # - lookup_template_vars passed, no jinja2_native
    # - lookup_template_vars passed, jinja2_native
    # Each covers the following cases:
    # - convert_data False
    # - convert_data True
    # - convert_data None
    # In addition, each covers the following cases:
    # - term is a non-existent file name
    # - term is the name of a file that exists
    # - term is the path to a non-existent file
    # - term is the path to a file that exists

    # Mocks
    class TestEnv(AnsibleEnvironment):
        def __init__(self, vars):
            self.vars = vars

# Generated at 2022-06-22 12:04:02.391137
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    # Path to test file
    test_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test.template')

    # Setup template environment
    display.verbosity = 4
    templar = LookupBase._create_templar(None, {})
    terms = [ '/some/file', test_file ]

    # Run LookupModule.run()
    result = lookup_module.run(terms, {}, convert_data=True, template_vars={}, lookup_file=test_file, templar=templar)
    assert result == None

# Generated at 2022-06-22 12:04:11.767683
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Use context manager instead of AnsibleOptions(connection='local') to ensure proper cleanup.
    #
    # Create a dummy class to mock methods of AnsibleOptions.
    class AnsibleOptions(object):
        def __init__(self, connection='local'):
            self.connection = connection

    class AnsibleModule(object):
        def __init__(self, **kwargs):
            self.params = kwargs
            self.check_mode = False

    with AnsibleOptions(connection='local'):
        # Create a dummy class to mock methods of Loader.
        class Loader(object):
            def __init__(self):
                pass


# Generated at 2022-06-22 12:04:20.794613
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # arrange
    TEST_YML_DIR = os.path.dirname(os.path.realpath(__file__)) + "/test_data/"
    TEST_YML = TEST_YML_DIR + "test.yml"
    TEST_TPL_DIR = os.path.dirname(TEST_YML)
    TEST_TPL = TEST_TPL_DIR + "/test.j2"
    TEST_VAR = {'firstname': 'John', 'lastname': 'Doe'}
    lookup_base = LookupBase()
    lookup_module = LookupModule()

    # action
    output = lookup_module.run(terms=[TEST_TPL], variables=TEST_VAR)

    # assert
    assert output[0].find(TEST_VAR['firstname']) >= 0
   

# Generated at 2022-06-22 12:04:21.263934
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-22 12:04:36.021231
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    template_path = 'template.j2'
    lookup_module._loader.set_basedir("../..")

    # Test with terms=['template.j2'], jinja2_native=False and convert_data=True
    variables = dict(a=1, b=2)
    content = "{{ a }} == 1, {{ b }} == 2"
    with open("../templates/template.j2","w") as template_content:
        template_content.write(content)
    assert lookup_module.run([template_path], variables, jinja2_native=False, convert_data=True) == ["1 == 1, 2 == 2"]

    # Test with terms=['template.j2'], jinja2_native=False and convert_data=False

# Generated at 2022-06-22 12:04:46.864972
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create test data
    # test_tmpl_src
    # test_tmpl_src_one
    # test_tmpl_src_two
    test_dir_src = os.path.dirname(os.path.realpath(__file__)) + '/test_lookup_plugin_template_sources'

    test_tmpl_src_one = test_dir_src + '/test_lookup_plugin_template_one.j2'
    with open(test_tmpl_src_one, 'w') as f:
        f.write('hello there {{ user.name }}')

    test_tmpl_src_two = test_dir_src + '/test_lookup_plugin_template_two.j2'
    with open(test_tmpl_src_two, 'w') as f:
        f.write

# Generated at 2022-06-22 12:04:57.002891
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    from ansible.template import Templar

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list=[])
    variable_manager.set_inventory(inventory)
    play_context = Play()

    example_vars = {'foo': 'bar'}
    template_vars = {'foo': 'baz'}


# Generated at 2022-06-22 12:05:08.370710
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l.set_options(var_options={}, direct={})

    lookupfile = 'test/integration/lookup-fixtures/template.j2'
    term = 'template.j2'
    display.debug("File lookup term: %s" % term)

    b_template_data, show_data = l._loader._get_file_contents(lookupfile)
    template_data = to_text(b_template_data, errors='surrogate_or_strict')

    # set jinja2 internal search path for includes
    searchpath = []
    searchpath.insert(0, os.path.dirname(lookupfile))

    # The template will have access to all existing variables,
    # plus some added by ansible (e.g., template_{path,mtime}),

# Generated at 2022-06-22 12:05:17.829071
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import __main__ as main
    main.JINJA2_NATIVE_LOOKUP = True
    lookup = LookupModule()
    lookup._loader = DummyLoader()
    lookup._templar = Templar(loader=lookup._loader)
    lookup._templar.environment.undefined = StrictUndefined
    lookup.set_options({'_ansible_verbosity': 3, '_ansible_no_log': False})
    lookup.run(['./test/test.j2'], {'variable': 'value'})


# Generated at 2022-06-22 12:05:30.850958
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    display = Display()
    lookup_module = LookupModule()

    # test1 - test 'convert_data' option
    # the value of 'convert_data' will be converted to bool type
    # but it will be converted to string type when stored in lookup_options
    # Thus, 'convert_data_p' is used to test.
    lookup_module.set_loader(None)
    lookup_module.set_options({'convert_data': "true", 'template_vars': {'result': 1234}})
    lookup_module.set_templar(None)
    lookup_module.set_basedir(None)
    lookup_module._display = display
    assert lookup_module.get_option("convert_data") == True

# Generated at 2022-06-22 12:05:42.505232
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # load the LookupModule
    from ansible.plugins.lookup.template import LookupModule as template_lookup
    lookup_module = template_lookup()

    # load constants for testing
    from ansible.plugins.lookup.template import display

    print("Testing lookup_module:")
    # print the contents of the lookup_module
    #print(lookup_module)

    #print the contents of the vars
    print(vars(lookup_module))

    # print the contents of the display
    #print(display)
    # print the contents of the vars
    #print(vars(display))

    # print the contents of the os
    #print(os)
    # print the contents of the vars
    #print(vars(os))

    # test the run method
    # Define the arguments

# Generated at 2022-06-22 12:05:53.756389
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Input data
    terms = ['./some_template.j2']
    variables = {'ansible_search_path': ['./']}

    # Expected result
    result = ["""this
is
a
test"""]

    # Actual result
    from ansible.module_utils._text import to_bytes
    mock_loader = type('MockModuleLoader', (object,), {
        ('_get_file_contents',): lambda x, y: (to_bytes("""{# this
is a
comment #}
this
is
a
test"""), None)
    })

# Generated at 2022-06-22 12:06:02.280863
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()

# Generated at 2022-06-22 12:06:05.580020
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    variables = dict()
    variables['ansible_search_path'] = ['foo', 'bar']

    terms = []
    terms.append('foo')

    expected = []
    expected.append(None)

    res = lookup.run(terms, variables)
    assert res == expected



# Generated at 2022-06-22 12:06:37.521607
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins.loader import lookup_loader

    # Load fixture and expected result
    with open('../fixtures/template_term_var.json') as fixture_fd:
        fixture = fixture_fd.read()
    with open('../fixtures/template_term_var.out') as result_fd:
        result = result_fd.read()
    # Parse fixture
    fixture_obj = json.loads(fixture)
    # Get template term
    elements_obj = fixture_obj['elements']


# Generated at 2022-06-22 12:06:47.788466
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test using dict `templar` and str `template_data`
    terms = ['/etc/hosts']
    variables = {
        'ansible_managed': 'Ansible managed: Do NOT edit this file manually!',
    }
    result = LookupModule().run(terms, variables)
    assert(result[0] == '# Ansible managed: Do NOT edit this file manually!\n')

    # Test using dict `templar` and str `template_data`
    terms = ['/etc/hosts']
    variables = {
        'ansible_managed': 'Ansible managed: Do NOT edit this file manually!',
    }
    convert_data_p = False
    result = LookupModule().run(terms, variables, convert_data = convert_data_p)

# Generated at 2022-06-22 12:06:59.525682
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def lookup_method(context, loader, templar, params):
        ret = []
        if len(params) >= 1:
            for term in params:
                if term == 'test_lookup_fail':
                    raise AnsibleError("test_lookup_fail")
                ret.append(term)
        return ret

    lookup_plugin = LookupModule()
    lookup_plugin._loader = object()
    lookup_plugin._templar = object()
    lookup_plugin.run = lookup_method
    lookup_plugin.set_options = lambda **kwargs: None

    assert lookup_plugin.run(['test_lookup_run'], dict()) == ['test_lookup_run']


# Generated at 2022-06-22 12:07:10.474767
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Use a value that can't be confused with the string 'null'
    test_vars = {u'ansible_search_path': [u'null']}
    test_terms = [u'this/is/a/test/template.j2']
    test_use_jinja2_native = [u'False']
    test_options = {u'variable_start_string': u'{{',
                    u'variable_end_string': u'}}',
                    u'comment_start_string': u'{#',
                    u'comment_end_string': u'#}',
                    u'jinja2_native': test_use_jinja2_native,
                    u'template_vars': {u'hello': u'world'}
    }

    test_class = LookupModule()
    test_class

# Generated at 2022-06-22 12:07:20.619529
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    try:
        from unittest import mock
        import jinja2
    except ImportError:
        raise ImportError("jinja2 is too old, >= 2.7 is required")

    from ansible.errors import AnsibleError

    # Setup mocks
    lookup_mock = mock.MagicMock(name='lookup_mock')
    jinja2_mock = mock.MagicMock(name='jinja2_mock')

    # Create mock class for jinja2 environment
    class MockEnv(object):
        def __init__(self):
            self.overlays = []
            self.filters = {}
            self.tests = {}
            self.globals = {}
        def getattr(self, key):
            return getattr(self, key)

# Generated at 2022-06-22 12:07:29.230340
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit test case for method run of class LookupModule
    """

    from ansible.plugins.lookup import LookupModule
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_native
    from ansible.constants import mk_boolean
    from ansible.module_utils.six import text_type

    # Create a class for the unit test
    class Options():
        """
        Options class
        """

# Generated at 2022-06-22 12:07:41.012240
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import sys
    from ansible.parsing.vault import VaultLib
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager

    vault_pass = VaultLib('ansible')
    vars_manager = VariableManager(loader=None, host_vars=HostVars(None, vault_pass), vault_ids=[])
    vault_pass.load_vault_password_file('ansible-vault.txt')

    templar = Templar(loader=None, variables=vars_manager.extra_vars, vault_password=vault_pass)

    lookupModule = LookupModule()
    lookupModule.set_loader(None)
    lookupModule.set_env(None)
    lookupModule._templar = tem

# Generated at 2022-06-22 12:07:43.149969
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_lookup = LookupModule()
    test_result = test_lookup.run()
    assert test_result == None

# Generated at 2022-06-22 12:07:54.519906
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    import yaml
    import ansible.utils.jww as jww
    from jinja2 import TemplateSyntaxError
    import json

    class Templar(object):

        def __init__(self, data):
            self._data = data

        def copy_with_new_env(self, environment_class=None):
            pass


# Generated at 2022-06-22 12:07:56.823678
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule.run(None, None, terms=[], convert_data=True, template_vars={}, jinja2_native=False) == []

# Generated at 2022-06-22 12:08:40.618145
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Get parameters for method run of class LookupModule
    test_lm = LookupModule()
    test_lm.set_loader()
    test_lm.set_environment()


# Generated at 2022-06-22 12:08:50.185028
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.module_utils.six import BytesIO
    from ansible.parsing.vault import VaultLib

    dict_args = dict(convert_data=False, template_vars={'var1':'val1'}, variable_start_string='[%', variable_end_string='%]',
                  jinja2_native=False, comment_start_string='[#', comment_end_string='#]')
    dict_template_data = [{'key': 'value'}]
    dict_template_data_to_string = yaml.safe_dump(dict_template_data)
    dict_vars = dict(ansible_search_path='/path/to/search/for/templates', var1='val1')

    # LookupBase._loader._get_file_contents none
   

# Generated at 2022-06-22 12:09:01.925588
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    _loader = DictDataLoader({
        "./templates/foo.j2": "{{ lookup('env', 'HOME') }}",
        "./templates/bar.j2": "{{ lookup('env', 'ANSIBLE_VAR_HOME') }}",
        "./templates/baz.j2": "{{ lookup('env', 'FOO') }}",
        "./templates/nested/foo.j2": "{{ lookup('env', 'HOME') }}",
        "./templates/nested/bar.j2": "{{ lookup('env', 'BAR') }}",
    })

    _templar = Templar(_loader=_loader, variables={'HOME': '/home/johndoe', 'ANSIBLE_VAR_HOME': '/home/ansible'})
    _lookup_module = LookupModule()
   

# Generated at 2022-06-22 12:09:10.697308
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    my_global_vars = {'question': 'life', 'answer': 42}
    my_loader = DictDataLoader({
        'baddir/badsubdir/badtemplate.j2': 'We want to go to %%{{badpath}}%%',
        'goodpath1/goodtemplate1.j2': 'We are the {{knights}} who say {{question}}!',
        'goodpath2/goodtemplate2.j2': 'We got the {{answer}}.'})
    my_lookup = LookupModule(loader=my_loader, templar=FakeTemplar(), basedir='/test')
    terms = ['goodpath1/goodtemplate1.j2',
             'goodpath2/goodtemplate2.j2',
             'baddir/badsubdir/badtemplate.j2']


# Generated at 2022-06-22 12:09:21.859542
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """ test_LookupModule_run
    :returns: None

    """
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.utils.display import Display
    from ansible.utils.vars import merge_hash

    display = Display()
    loader = DataLoader(display=display)

    def lookup_plugin_retrieve(self, term, variables, **kwargs):
        return lookup_plugin_retrieve.result

    lookup_plugin_retrieve.result = """
      {
        "name": "bar",
        "count": 2,
        "users": [ "toto", "titi" ]
      }
    """


# Generated at 2022-06-22 12:09:59.019042
# Unit test for method run of class LookupModule

# Generated at 2022-06-22 12:10:04.144822
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = 'lookup'
    variables = {'test_var': 'test'}

    # Mock objects
    class MockLoader:
        def _get_file_contents(self, lookupfile):
            return 'test', False
    class MockTemplar:
        def set_temporary_context(self, **kwargs):
            return True
        def template(self, template_data, preserve_trailing_newlines=True,
                     convert_data=True, escape_backslashes=False):
            return template_data
    class MockDisplay:
        def debug(self, debug_string):
            pass

    class MockLookupBase:
        def __init__(self, _loader, _templar, _display):
            self._loader = _loader
            self._templar = _templar
            self.display

# Generated at 2022-06-22 12:10:14.923791
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import os.path
    import tempfile
    import filecmp

    test_dir = os.path.dirname(__file__)

    file_path = os.path.join(test_dir, 'file_lookup_fixtures', 'file_lookup_j2.txt')
    fixture_path = os.path.join(test_dir, 'file_lookup_fixtures', 'file_lookup.txt')

    class Fake_VarsModule():
        def __init__(self):
            self.data = {'ansible_search_path': [os.path.join(test_dir, 'file_lookup_fixtures')]}

    class Fake_Templar():
        def __init__(self):
            self._available_variables = {}


# Generated at 2022-06-22 12:10:26.535086
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # case 1:
    # tests the proper result being returned in case of existing file
    # tests the proper result being returned in case of non-existing file

    # setup
    result1 = ["file content"]

    # mock
    templar = MagicMock()
    templar.set_temporary_context.return_value.__enter__.return_value = templar
    templar.template.return_value = result1
    templar._templar = templar

    loader = MagicMock()
    loader._get_file_contents.side_effect = [("b_file content", False)]

    lookup_module = LookupModule()
    lookup_module.set_loader(loader)
    lookup_module._templar = templar

    # test

# Generated at 2022-06-22 12:10:35.147709
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Unit test for AnsibleLookupModule class"""
    lookup_module = LookupModule()
    ret = lookup_module.run(
        ["/dev/null"],
        {
            "hostvars": {
                "foo": {
                    "bar": {
                        "baz": "foo-bar-baz"
                    }
                },
                "foo2": {
                    "bar2": {
                        "baz2": "foo-bar-baz"
                    }
                }
            }
        },
        variables={"inventory_dir": "foo", "inventory_file": "bar"},
        __file__="foo"
    )
    assert ret == []