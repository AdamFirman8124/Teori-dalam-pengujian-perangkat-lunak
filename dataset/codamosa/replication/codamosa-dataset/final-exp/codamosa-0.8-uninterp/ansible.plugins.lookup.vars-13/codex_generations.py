

# Generated at 2022-06-13 14:45:07.288316
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_dict = {'a': 1, 'b': '2', 'c': {'d': '3', 'e': '4'}, 'f': [5, 6, 7]}
    # Create a test class to test the method run
    l = LookupModule()
    l._templar._available_variables = test_dict
    # test with _terms as string
    test_result = l.run('a')
    assert(test_result[0] == 1)
    # test with _terms as list
    test_result = l.run(['a', 'b', 'c.d'])
    assert(test_result[0] == 1 and test_result[1] == '2' and test_result[2] == '3')
    # test with _terms with invalid string

# Generated at 2022-06-13 14:45:17.918206
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['tests/inventory'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)


# Generated at 2022-06-13 14:45:29.969645
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()

    # Basic test
    terms = ['variablename']
    variables = {'variablename': 'value'}
    expected_results = ['value']
    assert lookup_plugin.run(terms, variables=variables) == expected_results

    # Two variables
    terms = ['variablename', 'variable2']
    variables = {'variablename': 'value', 'variable2': 'value2'}
    expected_results = ['value', 'value2']
    assert lookup_plugin.run(terms, variables=variables) == expected_results

    # Two variables with default value
    terms = ['variablename', 'variable2']
    variables = {'variablename': 'value'}
    expected_results = ['value', '']
    assert lookup_plugin.run

# Generated at 2022-06-13 14:45:41.051744
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    # return term
    template = '{{ lookup("vars", "a", default="a") }}'
    result = lookup._templar.template(template, dict(a='b'))
    assert result == 'b'

    # stringify term
    template = '{{ lookup("vars", 1, default="a") }}'
    result = lookup._templar.template(template)
    assert result == 'a'

    # return default
    template = '{{ lookup("vars", "not_a", default="a") }}'
    result = lookup._templar.template(template)
    assert result == 'a'

    # raise exception
    template = '{{ lookup("vars", "not_a") }}'

# Generated at 2022-06-13 14:45:48.714208
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookuper = LookupModule()
    variables = {"answer": 42,
                 "junk": ["fish", "finger"]}
    lookuper._templar.available_variables = variables
    lookuper._templar._available_variables = variables
    assert lookuper.run(["answer"], variables=variables) == ["42"]
    try:
        assert lookuper.run(["junk"], variables=variables) == ["fish", "finger"]
    except AnsibleError:
        pass
    assert lookuper.run(["answer", "junk"], variables=variables) == ["42", "fish", "finger"]
    try:
        assert lookuper.run(["fish"], variables=variables)
    except AnsibleUndefinedVariable:
        pass

# Generated at 2022-06-13 14:45:57.141630
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    class UnitTestLookupModule(LookupModule):
        def __init__(self):
            pass

        def _templar(var):
            return 1

    utlm = UnitTestLookupModule()
    result = utlm.run(["HAVE_TO_FAIL"], None, default=23)
    assert result == [23]

    result = utlm.run(["HAVE_TO_FAIL"], None)
    assert len(result) == 0

    result = utlm.run([42], None)
    assert len(result) == 0

    result = utlm.run(["HAVE_TO_FAIL"], None, default="23")
    assert result == ["23"]

# Generated at 2022-06-13 14:46:07.411315
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test: vars is a dict
    lookup_instance = LookupModule()
    lookup_instance._templar = MockAnsibleTemplar(variables = {})
    assert lookup_instance.run(['test_var']) == []

    # test: vars is None
    lookup_instance = LookupModule()
    lookup_instance._templar = MockAnsibleTemplar(variables = {
        'test_var': 1,
        'test_var_2': 'test_var_2'
    })
    assert lookup_instance.run(['test_var', 'test_var_2']) == [1, 'test_var_2']

    # test: checking that invalid types of term results into AnsibleError
    lookup_instance = LookupModule()
    lookup_instance._templar = MockAn

# Generated at 2022-06-13 14:46:16.915983
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import json
    from ansible.parsing.dataloader import DataLoader

    # Test template variables
    # This is the inventory file to use for this test
    test_inventory = '''
    {
        "_meta": {
                "hostvars": {
                        "host1" : {
                                "var1": "test variable 1",
                                "var2": "test variable 2"
                        }
                }
        },
        "group1": {
                "hosts": ["host1"]
        }
    }
    '''

    # Play
    # This is the play to use for this test

# Generated at 2022-06-13 14:46:20.941898
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['ansible_play_hosts', 'ansible_play_batch', 'ansible_play_hosts_all']


# Generated at 2022-06-13 14:46:25.717598
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Set up mocks/fakes
    mock_templar = MockTemplar()
    mock_lookup_base = MockLookupBase(templar=mock_templar)
    test_terms = [
        "variable_name",
        "variable_name.sub_var"
    ]
    test_kwargs = {
        "default": "default the value"
    }

# Generated at 2022-06-13 14:46:38.826297
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import os
    from ansible.module_utils.six import PY3, string_types
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.parsing.ajson import AnsibleJSONEncoder
    from ansible.template import Templar
    from ansible.utils.shlex import shlex_split
    from ansible.plugins.loader import lookup_loader

    template_dir = os.path.join(os.path.dirname(__file__), 'test_templates')

# Generated at 2022-06-13 14:46:40.104475
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Add your unit test for method run of class LookupModule
    pass

# Generated at 2022-06-13 14:46:47.613001
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule(loader=None, templar=None, shared_loader_obj=None)
    # test_terms is a tuple of tuples containing test case, expected result
    test_terms = (
        (("a", "b", "c"), [None, None, None]),
        (("a", "b", "c"), [None, None, None]),
        (("a", "b", "c", "d"), [None, None, None, None]),
        (("a", "c", "d"), [None, None, None]),
    )

    result = lookup.run(
        test_terms[0][0],
        variables={
            'a': 1,
            'b': 2,
            'c': 3,
            'd': 4
        }
    )

# Generated at 2022-06-13 14:46:57.779423
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup.vars import LookupModule
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    myvars = {
        'inventory_hostname':'localhost',
        'hostvars': { 'localhost': {'testvar':'testval'} }
    }
    play_context = PlayContext()
    templar = Templar(loader=None, variables=myvars)
    lookup_module = LookupModule()
    lookup_module.set_templar(templar=templar)
    terms = ["testvar"]
    results = lookup_module.run(terms, variables=myvars)
    assert results == ["testval"]

# Generated at 2022-06-13 14:47:03.512770
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Testing return values for function run of class LookupModule.
    """
    terms = ['var1', 'var2', 'var3']
    variables = {'var1': 1, 'var2': 2, 'var3': 3}
    lookup = LookupModule()
    assert len(lookup.run(terms, variables=variables)) == 3
    assert lookup.run(terms, variables=variables) == [1,2,3]

# Generated at 2022-06-13 14:47:10.446274
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    terms = [
        'this_is_a_valid_host_variable_name',
        'this_is_not_a_valid_host_variable_name'
    ]
    variables = {
        'inventory_hostname': 'localhost',
        'this_is_a_valid_host_variable_name': 'Hello',
        'hostvars': {
            'localhost': {'this_is_a_valid_host_variable_name': 'Hello',
                          'not_valid_host_variable_name': 'Host Variable'
                          }
        },
        'this_is_not_a_valid_host_variable_name': 'Default'
    }

    assert module.run(terms, variables) == ['Hello', 'Default']

    # With default

# Generated at 2022-06-13 14:47:21.338798
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible_collections.ansible.community.tests.unit.compat.mock import patch, Mock, MagicMock
    from ansible_collections.ansible.community.plugins.lookup import vars as test_vars

    Term = Mock()
    Term.return_value = "test_term"
    Term.__iter__ = MagicMock(return_value=iter(['test_term']))
    Term.__getitem__ = MagicMock(side_effect=lambda x: "test_term")
    Term.__len__ = Mock(return_value=1)

    Var_Options = MagicMock(return_value=True)
    Set_Options = Mock()
    Vars_None = Mock()


# Generated at 2022-06-13 14:47:31.381895
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    V = {'variablename': 'hello', 'myvar': 'ename'}
    templar = DummyTemplar()

    # Test default case
    l = LookupModule(loader=None)
    l._templar = templar
    templar._available_variables = V

    actual_result = l.run(terms=['variabl' + 'ename'])
    assert [u'hello'] == actual_result
    assert [u'variabl' + u'ename'] == templar.template_near

    # Test default empty case
    l = LookupModule(loader=None)
    l._templar = templar
    templar._available_variables = V


# Generated at 2022-06-13 14:47:38.037784
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test class making
    module = LookupModule()
    # Test method run()
    # Test error output
    terms = [1, 'a']
    assert module.run(terms) == ['ab']
    assert module.run(terms, default='') == ['', 'a']
    assert module.run(terms, default='') == ['', 'a']
    assert module.run(terms, default='', a='') == ['', 'a']

# Generated at 2022-06-13 14:47:43.952125
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    var1 = dict()
    var1['hostvars'] = dict()
    var1['hostvars']['host1'] = dict()
    var1['hostvars']['host1']['var1'] = 'value1'
    var1['var2'] = 'value2'

    var3 = dict()
    var3['var3'] = 'value3'
    var3['hostvars'] = dict()
    var3['hostvars']['host1'] = dict()
    var3['hostvars']['host1']['var4'] = 'value4'

    var5 = dict()
    var5['var5'] = 'value5'
    var5['hostvars'] = dict()

# Generated at 2022-06-13 14:47:57.883393
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test whether run method returns value of the variable found or default
    lookup_plugin = LookupModule()
    fake_variable = 'all'
    fake_terms = ['hostvars', fake_variable]
    fake_hostname = 'host1'
    fake_variables = {'hostvars': {fake_hostname: {'variable1': 'value1'}}, 'inventory_hostname': fake_hostname}
    fake_default = None
    fake_kwargs = {}

    ret = lookup_plugin.run(terms=fake_terms, variables=fake_variable, **fake_kwargs)
    assert ret[0] == 'value1'



# Generated at 2022-06-13 14:48:05.282983
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a class object for LookupModule
    lk = LookupModule()

    # Create a dictionary object for variables
    # and add an entry for ansible_play_hosts
    variables = dict()
    variables['ansible_play_hosts'] = ['1.1.2.2', '1.1.2.3']
    variables['ansible_play_batch'] = ['1.1.2.1', '1.1.2.2']
    variables['ansible_play_hosts_all'] = ['1.1.2.1', '1.1.2.2', '1.1.2.3']

    # Create a list object for terms
    # and add three strings
    terms = list()
    terms.append('ansible_play_hosts')

# Generated at 2022-06-13 14:48:06.579249
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule.run()

# Generated at 2022-06-13 14:48:15.665527
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.plugins.lookup.vars
    print('Testing LookupModule.run()')
    x = ansible.plugins.lookup.vars.LookupModule()
    x._templar = object
    x._templar._available_variables = {'variablename': 'hello', 'myvar': 'ename', 'inventory_hostname': 'localhost'}
    x._templar._available_variables['hostvars'] = {'localhost': {'variablename': 'hello'}}
    print(x.run(['variablename']))

# Generated at 2022-06-13 14:48:26.493809
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lu = LookupModule()

    # test normal fetch
    lu.set_options(var_options={'testvar': 'testvalue', 'testvar2': 'testvalue2'}, direct={})
    assert lu.run(['testvar']) == ['testvalue']

    # test fetch array
    lu.set_options(var_options={'testvar': ['testvalue'], 'testvar2': 'testvalue2'}, direct={})
    assert lu.run(['testvar']) == [['testvalue']]

    # test fetch dict
    lu.set_options(var_options={'testvar': {'sub': 'subvalue'}, 'testvar2': 'testvalue2'}, direct={})

# Generated at 2022-06-13 14:48:38.738100
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Mock class for LookupModule
    class Mock_LookupModule(object):
        # Mock class for self._templar
        class Mock_Templar(object):
            # Mock class for self._templar._available_variables
            class Mock_Available_Variables(object):
                # Mock class for self._templar._available_variables['red']
                class Mock_Red(object):
                    def template(self, value, fail_on_undefined):
                        return value

                red = Mock_Red()

            def __init__(self):
                self._available_variables = self.Mock_Available_Variables()

        _templar = Mock_Templar()

    # Mock class for self.set_options

# Generated at 2022-06-13 14:48:39.254767
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert True

# Generated at 2022-06-13 14:48:47.376485
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    assert module.run(['var']) == [None]
    assert module.run(['var'], {}, default='') == ['']
    assert module.run(['var'], {'var': 'val'}) == ['val']
    assert module.run(['var'], {'var': 'val'}, default='') == ['val']
    assert module.run(['var', 'var2'], {'var': 'val', 'var2': 'val2'}) == ['val', 'val2']
    assert module.run(['var2', 'var'], {'var': 'val', 'var2': 'val2'}) == ['val2', 'val']

# Generated at 2022-06-13 14:48:56.216949
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:49:04.859393
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit test cases for method run of class LookupModule
    """
    from ansible.template import Templar
    from ansible.module_utils._text import to_text
    # For supporting python3
    from ansible.utils.display import Display
    Display().deprecated("Instead of running tests locally, you should use `tox`")
    # Define variables
    templar = Templar(variables={'hello':'world'})
    templar._available_variables = {}
    terms = ['hello']
    # Call method under test
    result = LookupModule().run(terms=terms, variables=None, templar=templar)
    # Assertion method
    assert result == [to_text('world')]

# Generated at 2022-06-13 14:49:23.655125
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # with simple lookups
    kwargs_1 = {'default': 'value'}
    terms_1 = ['test', 'test2']
    variables_1 = {'test': 'value'}

    class MockVars(object):
        def _init_(self, vars):
            self._available_variables = vars

    class MockTemplar():
        def __init__(self, value):
            self.value = value
        def template(self, value, fail_on_undefined=True):
            return self.value

    templar = MockTemplar(variables_1)
    vars = MockVars(variables_1)
    templar._templar = vars

    assert LookupModule(templar).run(terms_1, variables_1, **kwargs_1)

# Generated at 2022-06-13 14:49:33.497846
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # This is a bit of a pain as we need to mock a lot of the class
    # before we can even instantiate it.
    mock_loader_mgr = Mock()
    mock_host = Mock()
    mock_host.name = 'test'
    mock_task = Mock()
    mock_task.loop = None
    mock_task.loop_args = []

    mylookup = LookupModule(loader=mock_loader_mgr, templar=Mock(), variables={})

    # Set the class variable to an AnsibleVariable
    mylookup._templar._available_variables = AnsibleVars(mylookup._templar, loader=mock_loader_mgr, templated=True)

    # Test we raise an error if anything but strings are passed

# Generated at 2022-06-13 14:49:40.024027
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six.moves import StringIO
    from ansible.plugins.lookup import LookupModule
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    from ansible.vars import VariableManager


# Generated at 2022-06-13 14:49:50.995989
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class TestException(Exception):
        pass

    # These are required to find the vars plugin
    lookup_module = sys.modules[__name__]
    lookup_module.__loader__ = None
    lookup_module.__spec__ = None
    lookup_module.__file__ = os.path.join(os.path.dirname(ustr(__file__)), 'lib/ansible/plugins/lookup')

    # LookupModule.run => AnsibleUndefinedVariable
    module = LookupModule()

    terms = [b'foo']
    variables = {}
    kwargs = {'default': u'bar'}


# Generated at 2022-06-13 14:49:59.905936
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    my_lookup = LookupModule()
    myvars = {'hostvars': {'host1': {'first_var': '1', 'second_var': '2'}}, 'a_var': 'Hello World'}
    # Should return the value of a_var
    assert my_lookup.run(["a_var"], variables=myvars) == [myvars['a_var']]
    # Should return the values of second_var and a_var
    assert my_lookup.run(["second_var", "a_var"], variables=myvars) == [myvars['hostvars']['host1']['second_var'], myvars['a_var']]
    # Should return the value of a_var

# Generated at 2022-06-13 14:50:09.439814
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import PY3

    assert(LookupModule._debug is False)

    # Test case 1: success -- no problem
    mylookup = LookupModule()
    try:
        mylookup.set_options(var_options={"variablename": "hello", "myvar": "ename"}, direct={})
        terms = ["variablename"]
        ret = mylookup.run(terms)
    except:
        assert(False)

    # Test case 2: success -- no problem
    mylookup = LookupModule()

# Generated at 2022-06-13 14:50:20.303874
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import StringIO
    from ansible.template import Templar
    from ansible.vars import VariableManager

    variable_manager = VariableManager()
    variable_manager.set_inventory(inventory=None)

    utilsVars = {"foo": "bar", "hello": "world"}
    results = LookupModule(loader=None, templar=Templar(variable_manager=variable_manager, loader=None),
                                  shared_loader_obj=None).run(terms=['foo'], variables=utilsVars)
    assert results == ["bar"]


# Generated at 2022-06-13 14:50:26.887788
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest

    def ansibleUndefinedVariable(msg):
        raise AnsibleUndefinedVariable(msg)

    def template(value, fail_on_undefined=False):
        return value

    def set_option(value):
        return value

    class LookupModuleForTest(LookupModule):

        def __init__(self):
            self._templar = EasyMock()

# Generated at 2022-06-13 14:50:36.006414
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a new instance of this class
    mod = LookupModule()
    mod.set_options(direct = {'default': None})

    # Create a dictionary of variables
    vars = {'var1': 'var1value',
            'var2': 'var2value',
            'var3': 'var3value',
            'inventory_hostname': 'myhost',
            'hostvars': {'myhost': {'var4': 'var4value'}}}

    # Successfully gets the values of var1, var2 and var3
    result = mod.run(['var1', 'var2', 'var3'], vars)
    assert result == ['var1value', 'var2value', 'var3value']

    # Fails to get the value of var5 and since default is None, an error is raised

# Generated at 2022-06-13 14:50:45.275440
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.template.safe_eval import unsafe_eval

    terms = ['variablename.sub_var', 'variablnotename']
    variables = {
        'variablename': AnsibleBaseYAMLObject('{sub_var: 12}'),
        'variablenotename': AnsibleBaseYAMLObject('{sub_var: 12}')
    }

    # Should not raise error
    lookup_obj = LookupModule()
    ret = lookup_obj.run(terms, variables)

    assert ret[0] == '12'
    assert ret[1] is None

    # Should not raise error

# Generated at 2022-06-13 14:51:06.151606
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    class LookupModuleTestStub(LookupModule):
        def __init__(self):
            self.lookup_obj = {'foo': 'bar'}

        def run(self, terms, variables=None, **kwargs):
            return [self.lookup_obj]

    lmt = LookupModuleTestStub()
    assert lmt.run(terms='foo') == [lmt.lookup_obj]

# Generated at 2022-06-13 14:51:14.216865
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible.plugins.lookup import LookupBase
    from ansible.module_utils.six import string_types

    # Unit test for var type other than string_types
    lookup = LookupModule()
    with pytest.raises(AnsibleError):
        lookup.run(terms=[None])

    # Unit test for undefined variable with no default
    lookup = LookupModule()
    try:
        lookup.run(terms=['undefined_variable'])
    except AnsibleUndefinedVariable:
        assert True
    else:
        assert False

    # Unit test for undefined variable with default
    lookup = LookupModule()
    assert 'default' in lookup.run(terms=['undefined_variable'], default='default')[0]

    # Unit test for defined variable without default
    lookup = LookupModule

# Generated at 2022-06-13 14:51:21.112064
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Check if run of LookupModule works."""
    lookup_module = LookupModule()
    result = lookup_module.run(terms=[{'item1': 'value1'}, 'item2'],
                               variables={'item1_var': 'value1_var', 'item2_var': 'value2_var'})
    assert result == ['value1_var', 'value2_var']

    result = lookup_module.run(terms=['item'],
                               variables={'item_var': {'item_var_sub_item': 'item_var_sub_item_value'}})
    assert result == ['item_var_sub_item_value']


# Generated at 2022-06-13 14:51:22.630610
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule().run(["geoip_region_name"]) == ["New Jersey"]

# Generated at 2022-06-13 14:51:33.241913
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    print('Execute test_LookupModule_run.')
    instance = LookupModule()
    #ansible.constants = {"DEFAULT_HASH_BEHAVIOUR": "replace"}

    data = {}

    data["myvar"] = "ename"
    data["variablename"] = "hello"
    data["inventory_hostname"] = "myhost"
    data["hostvars"] = {"myhost": {"variablename": "hello"}}
    data["hostvars"]["myhost"]["variablename"] = "hello"
    data["hostvars"]["myhost"]["variablenotename"] = "foo"

    result = instance.run(["variabl" + data["myvar"]], variables=data)

# Generated at 2022-06-13 14:51:35.378644
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    result = lookup_module.run(['vault_password'])
    assert result == [None]

# Generated at 2022-06-13 14:51:36.712576
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    
    assert LookupModule.run(terms=['hello']) == [None]

# Generated at 2022-06-13 14:51:42.915411
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    This is a test for method run of class LookupModule
    """
    variablename = 'hello'
    myvar = 'ename'
    variablenotename = ''
    mynotename = 'notename'
    sub_var = 12
    mysubvar = 'name'
    ansible_play_hosts = 'asdf'
    ansible_play_batch = 'qwer'
    ansible_play_hosts_all = 'zxcv'

    obj = LookupModule()

# Generated at 2022-06-13 14:51:49.169313
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    mylookup = LookupModule()
    mylookup._templar = {
        "_available_variables": {
            "hostvars": {
                "host": {
                    "host_var_name": "host_var_value"
                }
            },
            "inventory_hostname": "host",
            "variable_name": "value"
        },
        "template": "This is a test for {{ value }}"
    }

    result = mylookup.run(["variable_name", "host_var_name"], variables={"value": "lookup_plugin"})
    assert result == ["lookup_plugin", "host_var_value"]


# Generated at 2022-06-13 14:51:58.204950
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    ###############################
    # testing 'default' parameter #
    ###############################
    terms = ['foo', 'bar']

    variables = {
        'foo': 'foo',
        'hostvars': {
            'host_name': {
                'bar': 'bar'
            }
        },
        'inventory_hostname': 'host_name'
    }

    kwargs = {}

    ansible_module_instance = AnsibleUndefinedVariable('No variable found with this name: baz')

    test_module = LookupModule(None)
    test_module.set_options(var_options=variables, direct=kwargs)
    default = test_module.get_option('default')


# Generated at 2022-06-13 14:52:38.067678
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()

# Generated at 2022-06-13 14:52:46.508000
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # test when no variables are provided
    test_terms = ("hostvars", "inventory_hostname")
    lookup_module_instance = LookupModule()
    assert lookup_module_instance.run(terms=test_terms) == []

    # test when variables are provided
    test_terms = ("hostvars", "inventory_hostname")
    test_variables = dict(hostvars="test variables", inventory_hostname="test hostname")
    lookup_module_instance = LookupModule()
    assert lookup_module_instance.run(terms=test_terms, variables=test_variables) == ["test variables", "test hostname"]

# Generated at 2022-06-13 14:52:51.473696
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:52:57.679441
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Testing against the example code in the docstring of LookupModule
    def mock_lookup_file(self, terms, variables=None, **kwargs):
        '''
        This function is the return value of LookupBase.run.
        It "returns" a value based on the contents of terms,
        which is an array that contains the parameters passed
        to lookup.
        '''
        # Example vars as in source code
        example_vars = {
            u'variablename': {'sub_var':12},
            u'myvar': u'ename',
            u'hostvars': {
                u'inventory_hostname': {
                    u'variablename': u'hello'
                    },
                u'ignore_errors': True,
                },
            }

        # The conditional below is to test the

# Generated at 2022-06-13 14:53:06.322845
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Testing 'ansible_play_hosts' variable
    assert LookupModule({}).run([
        'ansible_play_hosts'
    ], variables={
        'ansible_play_hosts': 'localhost'
    }) == ['localhost']

    # Testing not existing term
    with raises(AnsibleUndefinedVariable) as error:
        LookupModule({}).run([
            'ansible_play_hosts_not'
        ], variables={
            'ansible_play_hosts': 'localhost'
        })
    assert 'No variable found with this name: ansible_play_hosts_not' in str(error.value)

    # Testing not existing term with default option

# Generated at 2022-06-13 14:53:11.657111
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()
    assert lookup_plugin.run(['ansible_play_hosts', 'ansible_play_batch', 'ansible_play_hosts_all'], variables={"ansible_play_hosts": "1","ansible_play_batch": "2","ansible_play_hosts_all": "3"}) == ['1', '2', '3']

# Generated at 2022-06-13 14:53:19.910509
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a FakePlugin to have an instance of the _templar object
    # which will be the same for this test
    class FakePlugin(object):
        def __init__(self):
            self.vars = {'var_one': 'value_one', 'var_two': 'value_two'}
            self.myvars = getattr(self, '_available_variables', {})

        def template(self, value, fail_on_undefined=True):
            return value

    templar = FakePlugin()

    # Create an instance of class LookupModule to test it
    lookup = LookupModule()

    # Create test variables
    for var in ('var_one', 'var_two'):
        if var not in lookup._templar.available_variables:
            lookup._templar.available_vari

# Generated at 2022-06-13 14:53:28.916677
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest

    from ansible.vars.manager import VariableManager

    from ansible.module_utils.six import string_types

    # invalid off
    l = LookupModule()
    l.set_options(direct={'_terms': ['my_variable']})
    l._templar._available_variables = {'my_variable': 'my_value'}
    l._templar.available_variables = {}
    assert l.run() == ['my_value']

    # invalid on
    l = LookupModule()
    l.set_options(direct={'_terms': ['my_variable']})
    l._templar._available_variables = {}
    l._templar.available_variables = {}

# Generated at 2022-06-13 14:53:40.374590
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
	
    def _set_available_variables(variables):
        lookup_module._templar._available_variables = variables

    # 1. simple
    variables = {'variablename': 'hello', 'myvar': 'ename'}
    _set_available_variables(variables)
    assert lookup_module.run(terms=['variabl' + '{{ myvar }}'], variables=variables) == ['hello']

    # 2. default
    variables = {'variablename': 'hello', 'myvar': 'notename'}
    _set_available_variables(variables)
    assert lookup_module.run(terms=['variabl' + '{{ myvar }}'], variables=variables, default='') == ['']

    # 3. int


# Generated at 2022-06-13 14:53:48.408396
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import PY3
    from ansible.module_utils._text import to_bytes
    from ansible.vars import VariableManager
    from ansible.parsing.vault import VaultLib
    from ansible.template import Templar
    from ansible.compat.tests import unittest

    if PY3:
        unicode_type = str
    else:
        unicode_type = unicode

    class AnsibleVariable:

        def __init__(self, value):
            if isinstance(value, unicode_type):
                self.__value = value
            else:
                self.__value = to_bytes(value)

        def __str__(self):
            return self.__value
