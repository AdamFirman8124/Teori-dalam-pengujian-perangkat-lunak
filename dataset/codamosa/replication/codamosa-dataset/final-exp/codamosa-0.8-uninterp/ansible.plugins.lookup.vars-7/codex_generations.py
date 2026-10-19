

# Generated at 2022-06-13 14:45:07.797927
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test if lookup_type 'vars' and terms together with variables return expected value
    test_terms = ['ansible_play_hosts', 'ansible_play_batch', 'ansible_play_hosts_all']
    test_variables = { "ansible_play_hosts": ["a", "b", "c"],
                       "ansible_play_batch": ["d", "e", "f"],
                       "ansible_play_hosts_all": ["g", "h", "i"]}
    term_lookup = LookupModule().run(terms = test_terms, variables = test_variables)
    assert term_lookup == [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
    # test if lookup_type 'vars' and

# Generated at 2022-06-13 14:45:18.361242
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.collections import is_sequence

    # setup for testing
    # test with good & bad term
    # can only return raw datatype
    test_terms = (
        dict(
            value='test_value',
            term='test_term',
            ref_result=[b'test_value'],
            # TODO: Test with sub_vars
        ),
    )


# Generated at 2022-06-13 14:45:24.246727
# Unit test for method run of class LookupModule
def test_LookupModule_run():
  # Use case #1
  terms = ["variable_name"]
  variables = {"variable_name": "This is variable"}

  # Create object of class LookupModule
  lookup_module = LookupModule()

  # Call method run
  result = lookup_module.run(terms, variables)

  # Check the result
  assert result == ["This is variable"]

# Generated at 2022-06-13 14:45:34.154733
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    my_vars = {'hostvars': {'HOST_A': {'var_a': 1, 'var_b': 2}, 'HOST_B': {'var_a': 10, 'var_b': 20, 'var_c': 30}}}
    my_terms = ['var_a', 'var_b', 'var_c']
    my_options = {'default': 0}
    lookup_module = LookupModule(loader=None, templar=None, shared_loader_obj=None)
    my_return = lookup_module.run(terms=my_terms, variables=my_vars, **my_options)
    assert my_return == [1, 2, 0]
    my_return = lookup_module.run(terms=my_terms, variables=my_vars)

# Generated at 2022-06-13 14:45:44.439398
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.module_utils.six import string_types
    from ansible.plugins.lookup import LookupModule

    class LookupModuleTest(LookupModule):
        def __init__(self, kwargs):
            from ansible.template import Templar
            from ansible.parsing.vault import VaultLib
            from ansible.vars.manager import VariableManager

            vault_secrets_file = None
            self._templar = Templar(loader=None, variables=VariableManager(), vault_secrets=VaultLib(vault_secrets_file))
            self.set_options(kwargs)


# Generated at 2022-06-13 14:45:51.296958
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest

    mock_loader = 'foo'
    mock_templar = 'bar'
    mock_params = 'foobar'

    class MockAnsibleTemplar(object):

        def __init__(self, loader, variables=None, **kwargs):
            self.loader = loader
            self.variables = variables
            self.kwargs = kwargs
            self._available_variables = {}

        def template(self, *args, **kwargs):
            return args[0]

    class MockAnsibleLookupModule(LookupModule):

        def __init__(self):
            self._loader = mock_loader
            self._templar = MockAnsibleTemplar(self._loader, **mock_params)

    mock_module = MockAnsibleLookupModule()

    # Verify

# Generated at 2022-06-13 14:46:00.393670
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    assert lookup.run([], variables={}) == []
    assert lookup.run(['foo'], variables={}) == []
    assert lookup.run(['foo'], variables={'foo':'bar'}) == ['bar']
    assert lookup.run(['hostvars'], variables={'hostvars':{'local':{'foo':'bar'}}}) == [{'local':{'foo':'bar'}}]
    assert lookup.run(['hostvars'], variables={'inventory_hostname':'local','hostvars':{'local':{'foo':'bar'}}}) == [{'local':{'foo':'bar'}}]

# Generated at 2022-06-13 14:46:09.228660
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    hostvars = {'192.168.0.1': {'ansible_hostname': 'test1', 'ansible_ssh_user': 'test_user1', 'ansible_ssh_port': 22},
                '192.168.0.2': {'ansible_hostname': 'test2', 'ansible_ssh_user': 'test_user2', 'ansible_ssh_port': 22}}
    variables = {'hostvars': hostvars, 'inventory_hostname': '192.168.0.1'}
    terms = ['ansible_hostname']
    result = [{'_value': ['test1']}]
    assert module.run(terms, variables) == result


# Generated at 2022-06-13 14:46:19.377235
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import unittest
    from ansible.module_utils.six import PY2

    class TestLookupModule(unittest.TestCase):

        class FakeTemplate:

            def __init__(self):
                self._available_variables = {'inventory_hostname': 'fakehost'}

            def template(self, value, fail_on_undefined=False):
                return value

        class FakeLookupModule(LookupModule):

            def __init__(self, variable_manager=None, loader=None, templar=None, **kwargs):
                super(FakeLookupModule, self).__init__(variable_manager=variable_manager, loader=loader, templar=templar, **kwargs)
                self._templar = templar


# Generated at 2022-06-13 14:46:26.349851
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()

    # Test with default option set
    l.set_options(direct={'default': 'DEFAULT'})
    terms=[('foo', None), ('bar', None)]
    variables={}
    variables['foo'] = 'foo'
    variables['bar'] = 'bar'
    variables['baz'] = 'baz'
    variables['hostvars'] = {'host1': {'host1_foo': 'host1_foo'}}

    assert l.run(terms=terms, variables=variables) == ['foo', 'bar']
    terms=[('baz', None)]
    assert l.run(terms=terms, variables=variables) == 'DEFAULT'

    # Test with default option set to None
    l.set_options(direct={'default': None})

# Generated at 2022-06-13 14:46:39.757426
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    import pytest
    from ansible.errors import AnsibleError

    terms = []
    variables = {'test': 1}
    # Initialize test object
    test_obj = LookupModule()

    # Test normal execution of the run method
    test_obj.run(terms=terms, variables=variables)
    # Test run method with exception
    with pytest.raises(AnsibleError) as ex:
        test_obj.run(terms=terms, variables=None)
    assert 'Invalid setting identifier, "" is not a string, its a <class \'set\'>' in str(ex.value)
    # Test run method with exception
    with pytest.raises(AnsibleError) as ex:
        test_obj.run(terms=['test'], variables=variables)

# Generated at 2022-06-13 14:46:47.437866
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test case 1
    # When user provides a dictionary, return list of values from dictionary
    # with one element
    lookup = LookupModule()
    terms = ['variablename']
    variables = {
        "variablename": 'hello',
        "myvar": 'ename'
    }
    lookup.set_loader()
    result = lookup.run(terms=terms, variables=variables)
    assert result == ['hello']

    # Test case 2
    # When user provides a dictionary, return list of values from dictionary
    # with two elements
    lookup = LookupModule()
    terms = ['variablename', "myvar"]
    variables = {
        "variablename": 'hello',
        "myvar": 'ename'
    }
    lookup.set_loader()

# Generated at 2022-06-13 14:46:57.654821
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    loader = AnsibleLoader(None, {}, None, None)
    # Test for basic template
    variables1 = loader.load('''
        initial_var: initial
    ''')
    templar = Templar(None, None, None, None, None, loader=loader)
    vars_manager1 = VariableManager(loader=loader, use_cache=False)
    vars_manager1.set_fact_cache(variables1)

    test_term1 = ['initial_var']

    lookup_obj1 = LookupModule()

# Generated at 2022-06-13 14:47:06.900155
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def tested_function(terms, variables=None, **kwargs):
        lookup_module = LookupModule()
        return lookup_module.run(terms, variables=variables, **kwargs)

    my_vars = {
        'nested': {
            'string': 'hello',
            'number': 11,
            'list': [1,2,3,4],
            'dict': {'a':1, 'b':2}
        }
    }
    # test if all elements of dict are returned as one string
    def test_vars_elements(terms, variables=None, **kwargs):
        ret = tested_function(terms, variables=variables, **kwargs)
        for term in terms:
            assert term in ret, 'expected "%s", got "%s"' % (term, ret)

    test_

# Generated at 2022-06-13 14:47:18.812200
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()

    default = "default_value"
    # No var is defined so it should return default value
    terms = ["host_var_not_defined"]
    results = module.run(terms, default=default)
    assert results == [default]

    def_vars = {'var_one': 'var_value_one', 'var_two': 'var_value_two', "hostvars": {'host_one': {'host_var_one': 'host_var_value_one', 'host_var_two': 'host_var_value_two'}, 'host_two': {'host_var_one': 'host_var_value_one'}}}

    # Run with one host var Defined
    terms = ["var_three"]

# Generated at 2022-06-13 14:47:24.794120
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    default = None

    assert LookupModule().run([], {}) == []
    assert LookupModule().run(['foo'], {'foo': 'bar'}) == ['bar']
    assert LookupModule().run(['foo'], {'foo': 'bar'}, default=default) == ['bar']
    assert LookupModule().run(['foo'], {}, default=default) == []
    assert LookupModule().run(['foo'], {}) == []

# Generated at 2022-06-13 14:47:33.632129
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    l = LookupModule()
    l._templar = FakeTemplarClass()

# Generated at 2022-06-13 14:47:43.282313
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six.moves import reload_module
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.utils.display import Display
    from ansible.plugins import lookup_loader
    from ansible.executor.playbook_executor import PlaybookExecutor
    import os

    import pytest

    fixture_path = os.path.join(os.path.dirname(__file__), 'fixtures')

    vars_file = os.path.join(fixture_path, 'vars_test.yml')
    hosts_file = os.path.join(fixture_path, 'hosts')

# Generated at 2022-06-13 14:47:51.393138
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    assert lookup_module.run(terms=None)[0] == '', 'test_LookupModule_run() assertion error'
    myvars = {'first':'first_value', 'second': 'second_value'}
    assert lookup_module.run(terms=myvars.keys(), variables=myvars)[0] == 'first_value', 'test_LookupModule_run() assertion error'
    assert lookup_module.run(terms=myvars.keys(), variables=myvars)[1] == 'second_value', 'test_LookupModule_run() assertion error'
    assert lookup_module.run(terms=['first', 'second'], variables=myvars) == ['first_value', 'second_value'], 'test_LookupModule_run() assertion error'

# Generated at 2022-06-13 14:47:56.060396
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    print("""Test 1 expected output: AnsibleUndefinedVariable""")
    module = LookupModule()
    module.run(terms=['my_var'])

if __name__ == "__main__":
    test_LookupModule_run()

# Generated at 2022-06-13 14:48:15.716502
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a mock variabled
    class mock_variables():
        def __init__(self):
            self.variables = {'variable_1': 1, 'variable_2': 2}
    variables = mock_variables()

    # Create a mock templar
    class mock_templar():
        def __init__(self):
            self.available_variables = variables.variables
    templar = mock_templar()

    # Create a mock templar
    class mock_LookupBase():
        def __init__(self):
            self._templar = templar
    lookup_base = mock_LookupBase()

    # Create a mock set option
    class mock_set_options():
        def __init__(self):
            self.var_options = variables

# Generated at 2022-06-13 14:48:21.867702
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module.set_options(var_options={}, direct={})
    lookup_module._templar._available_variables = {'inventory_hostname': 'localhost'}
    lookup_module._templar.available_variables = {'inventory_hostname': 'localhost'}
    result = lookup_module.run(terms=['inventory_hostname'])
    assert result == ['localhost']


# Generated at 2022-06-13 14:48:38.429661
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    terms = []
    variables = { 'inventory_hostname': 'web',
                  'hostvars': { 'web': { 'user': 'alice',
                                         'password': 'secret' }
                              }
                }
    assert lm.run(terms, variables=variables) == []

    terms = ['user']
    assert lm.run(terms, variables=variables) == ['alice']

    terms = ['inventory_hostname']
    assert lm.run(terms, variables=variables) == ['web']

    terms = ['user', 'password']
    assert lm.run(terms, variables=variables) == ['alice', 'secret']

    terms = [1, 'user', 'password']

# Generated at 2022-06-13 14:48:47.094561
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.common._collections_compat import MutableSequence
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.module_utils._text import to_native

    from ansible.parsing.yaml.loader import AnsibleLoader

    ####
    # Test cases for when default is not set
    ####
    # Test case 1
    # _terms is empty, inventory_hostname is not set.
    # Expected output: AnsibleError
    with pytest.raises(AnsibleError) as e:
        mylookup = LookupModule()
        mylookup.run([], dict())

    assert to_native(e.value) == 'No variable found with this name: '
    # Test case 2
    # _terms has one

# Generated at 2022-06-13 14:48:56.021826
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()

    # Setup mocks
    module._templar = Mock()
    module._templar.template = Mock()
    module._templar.template.side_effect = [
        'Variable 1',
        'Variable 2',
    ]

    # Execute
    var_options = {
        'Variable 1': 'Value 1',
        'Variable 2': 'Value 2',
        'Variable 3': 'Value 3',
    }
    terms = [
        'Variable 1',
        'Variable 2',
    ]
    result = module.run(terms, var_options)

    # Verify
    assert result == [
        'Variable 1',
        'Variable 2',
    ]

# Generated at 2022-06-13 14:49:05.203016
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''
    making use of the test infrastructure
    via the method "test_LookupModule_run"
    '''
    from ansible.plugins.lookup import LookupModule
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    from ansible.vars import VariableManager

    # test values variables
    # =====================
    # ansible_play_hosts     ['localhost']
    # ansible_play_batch     []
    # ansible_play_hosts_all ['localhost']
    terms = ['ansible_play_hosts', 'ansible_play_batch', 'ansible_play_hosts_all']
    default = ''
    expected_failed_term = 'ansible_play_badterm'

# Generated at 2022-06-13 14:49:13.867976
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Prepare
    lookup_module = LookupModule()
    lookup_module.set_loader({'_load_from_file': lambda path, internal=False: [{'hostvars': {'test-host': {'test_var': 'value'}}}]})
    lookup_module._templar._available_variables = {'inventory_hostname': 'test-host'}
    lookup_module.set_options(var_options={'inventory_hostname': 'test-host'}, direct={})

    # Test
    value = lookup_module.run(['test_var'])

    # Assert
    assert value == ['value']

# Generated at 2022-06-13 14:49:17.754877
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    myvars = {
        'top_var': 'rendered_val',
        'hostvars': {
            'my_fqdn': {
                'subvar': 'subvar_val'
            }
        }
    }

    class Plugin:
        def __init__(self):
            self.options = {}

    p = Plugin()
    l = LookupModule(plugin=p)



# Generated at 2022-06-13 14:49:29.632737
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils._text import to_text
    import ansible.utils.unsafe_proxy as unsafe_proxy
    lookup_module = LookupModule()

    # Testing terms with subvars

    terms = ['variabl' + 'ename' ]
    variables = unsafe_proxy.AnsibleUnsafeText('{"variablename": {"sub_var": 12}}')
    assert lookup_module.run(terms, variables=variables) == [unsafe_proxy.AnsibleUnsafeText('{"sub_var": 12}')]

    terms = ['variabl' + 'ename' + '.sub_var']
    variables = unsafe_proxy.AnsibleUnsafeText('{"variablename": {"sub_var": 12}}')

# Generated at 2022-06-13 14:49:41.285869
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Setup
    import inspect
    import os
    import sys

    # Testing the method
    def fake_get_option(self, key):
        return 'default_var'
    LookupBase.get_option = fake_get_option

    module = sys.modules['ansible.plugins.lookup.vars']
    module.AnsibleError = Exception

    class FakeTemplar(object):
        def template(self, value, fail_on_undefined=False):
            return 'templated_value_for_' + value

    # Testing the method
    def fake__get_vars(self):
        return {
            'inventory_hostname': 'host',
            'hostvars': {
                'host': {
                    'my_var': 'my_value'
                }
            }
        }

   

# Generated at 2022-06-13 14:50:06.478629
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    class unitTest_Templar:
        def __init__(self):
            self._available_variables = {}

        def template(self, value, fail_on_undefined=False):
            return value

    class unitTest_LookupModule(LookupModule):
        def __init__(self):
            self.set_options(var_options=None, direct=None)

        def get_option(self, var):
            return None

    # SETUP
    # instantiate unitTest_Templar()
    unitTest_templar = unitTest_Templar()
    unitTest_templar._available_variables = {'hostvars': {'localhost': {'hostvar_default': 0, 'hostvar_2': 3, 'hostvar_1': 2}}}
    # instantiate unitTest_LookupModule

# Generated at 2022-06-13 14:50:13.730482
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class MyLookupModule(LookupModule):
        def run(self, terms, variables, **kwargs):
            return super(MyLookupModule, self).run(terms, variables, **kwargs)

    def test_empty_dict():
        # default parameter is None
        result = MyLookupModule().run(['test_variable'], {}, {})
        assert result == []

    def test_dict_no_value():
        # default parameter is None
        result = MyLookupModule().run(['test_variable'], {'item': 'test_item'}, {})
        assert result == []

    def test_dict():
        # default parameter is None
        result = MyLookupModule().run(['test_variable'], {'test_variable': 'test_value'}, {})
        assert result == ['test_value']

# Generated at 2022-06-13 14:50:16.599727
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    assert lm.run(terms=["foo"]) == ["foo"]



# Generated at 2022-06-13 14:50:19.013592
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    _terms = ("variablename", "myvarnotename")
    myvariables = {'variablename': 'hello', 'myvar': 'ename'}

    my_module = LookupModule()
    my_module.run(_terms, myvariables)

    # assert that the module returned the proper value
    assert my_module.run(_terms, myvariables) == ['hello', '']

# Generated at 2022-06-13 14:50:19.447344
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert True

# Generated at 2022-06-13 14:50:22.907538
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def setUp(self):
        self.run = LookupModule.run(self, terms, variables=None, **kwargs)
        self.run = LookupModule(self, terms, variables=None, **kwargs)


# Generated at 2022-06-13 14:50:32.741788
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # =======================================
    # Test with a valid term but missing var
    # =======================================
    terms = ['no_var']
    variables = {}
    lu = LookupModule()
    with pytest.raises(AnsibleUndefinedVariable) as exc:
        lu.run(terms, variables)
    assert "No variable found with this name: no_var" in str(exc.value)

    # =======================================
    # Test with a valid term and valid var
    # =======================================
    terms = ['var']
    variables = { 'var' : 'hello world'}
    lu = LookupModule()
    ret = lu.run(terms, variables)
    assert ret == ['hello world']

    # =======================================
    # Test with a valid term and valid var
    # =======================================
    terms = ['var']
    variables

# Generated at 2022-06-13 14:50:43.810161
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a TestTemplate as _templar
    from ansible.template import Templar
    from jinja2.environment import Environment
    from jinja2.loaders import DictLoader
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    loader = DataLoader()
    variable_manager = VariableManager()

    env = Environment(loader=loader)
    variable_manager.extra_vars = {'hostvars': {'host1': {'test1': 'test2'}}}
    variable_manager.set_inventory(loader.load({}))
    templar = Templar(loader=loader, variables=variable_manager)

    # Create a LookupModule and call method run
    lookupModule = LookupModule()
    lookupModule._templar = templar



# Generated at 2022-06-13 14:50:51.548281
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    results = 0

    # normal usage
    terms = ['ansible_play_hosts_all']
    variables = {'hostvars': {'ansible_play_hosts_all': []}}
    terms2 = ['ansible_play_hosts_all']
    lookup_module = LookupModule()
    results = lookup_module.run(terms, variables=variables)
    assert results == terms2, 'method run of class LookupModule with normal usage failed'

    variables = {'ansible_play_hosts_all': ['test1', 'test2']}
    terms2 = [['test1', 'test2']]
    lookup_module = LookupModule()
    results = lookup_module.run(terms, variables=variables)

# Generated at 2022-06-13 14:51:00.016060
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # check multi variable
    variables = {'a':1,'b':2,'hostvars':{'host1':{'c':3,'d':4}},'inventory_hostname':'host1'}
    terms = ['a','c']
    module = LookupModule()
    result = module.run(terms=terms,variables=variables)
    assert len(result) == 2
    assert result == [1,3]

    # check undefined varibale
    variables = {'a':1,'b':2,'hostvars':{'host1':{'c':3,'d':4}},'inventory_hostname':'host1'}
    terms = ['a','c','e']
    module = LookupModule()

# Generated at 2022-06-13 14:51:36.031138
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest

    # Test 2 variables
    test_terms = ['term1', 'term2']
    test_variables = {'term1': 'value1', 'term2': 'value2'}
    test_default = None

    lu = LookupModule()
    result = lu.run(test_terms, test_variables, default=test_default)
    assert result == ['value1', 'value2']

    # Test that raises exception
    test_terms = ['term1', 'term2']
    test_variables = {'term1': 'value1'}
    test_default = None


# Generated at 2022-06-13 14:51:41.263338
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['ansible_facts_path', 'inventory_filename']
    expected_result = ['/etc/ansible/facts.d', 'example.yml']
    variables = {'ansible_facts_path': '/etc/ansible/facts.d', 'inventory_filename': 'example.yml'}

    module = LookupModule()
    result = module.run(terms=terms, variables=variables)
    assert result == expected_result

# Generated at 2022-06-13 14:51:41.998998
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule({}).run([]) == []

# Generated at 2022-06-13 14:51:50.701626
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_obj = LookupModule()
    myvars = {'ansible_play_hosts_all': [],
              'ansible_play_batch': [],
              'ansible_play_hosts': [],
              'ansible_play_hosts_count': 0,
              'ansible_play_hosts_num': 0}

    expected = []
    result = test_obj.run(terms=['ansible_play_hosts_all'], variables=myvars)
    assert result == expected

    expected = []
    result = test_obj.run(terms=['ansible_play_batch'], variables=myvars)
    assert result == expected

    expected = []
    result = test_obj.run(terms=['ansible_play_hosts'], variables=myvars)

# Generated at 2022-06-13 14:52:00.706561
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    #args = ['ansible_play_hosts', 'ansible_play_batch', 'ansible_play_hosts_all']
    args = ['ansible_play_hosts', 'ansible_play_batch', 'ansible_play_hosts_all']
    lm = LookupModule()
    vars = {}
    myvars = {}
    vars['hostvars'] = {}
    vars['hostvars'][vars['inventory_hostname']] = {}
    vars['hostvars'][vars['inventory_hostname']]['ansible_play_hosts'] = 'hosts'
    vars['hostvars'][vars['inventory_hostname']]['ansible_play_batch'] = 'batch'

# Generated at 2022-06-13 14:52:09.388830
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Set values of parameters
    terms = [u'host1', u'host2', u'host3']
    variables = None
    kwargs = {u'something': 123}

    # Set values of instance variables needed by the module
    _terms = terms

# Generated at 2022-06-13 14:52:20.682110
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Create a fake object class LookupBase
    class LookupBase_class():
        # Create a fake object class LookupBase
        class LookupBase():
            def __init__(self):
                self._templar = _templar_class()


    # Create a fake object class _templar_class
    class _templar_class():
        def __init__(self):
            self.available_variables = {}

        def template(self, value, fail_on_undefined=True):
            return value

    # Create a fake object class LookupModule
    class LookupModule_class():
        def __init__(self):
            self._templar = _templar_class()

        # Fake implementation of method _templar.template

# Generated at 2022-06-13 14:52:21.335735
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert(False)

# Generated at 2022-06-13 14:52:26.505832
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.compat.tests.mock import patch, MagicMock
    from ansible.module_utils import basic

    lm = LookupModule()
    with patch.object(basic.AnsibleModule, 'run_command') as mock_run_command:
        mock_run_command.return_value = (0,'')
        lm = LookupModule()
        lm.run([], dict())



# Generated at 2022-06-13 14:52:34.005046
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import unittest

    class AnsibleUndefinedVariableMock(AnsibleUndefinedVariable):
        def __init__(self, original_exception, *args, **kwargs):
            super(AnsibleUndefinedVariableMock, self).__init__(*args, **kwargs)

    class AnsibleErrorMock(AnsibleError):
        def __init__(self, original_exception, *args, **kwargs):
            super(AnsibleErrorMock, self).__init__(*args, **kwargs)

    class LookupModuleTest(unittest.TestCase):
        def setUp(self):
            self.lookup_module = LookupModule()
            self.lookup_module.set_options(var_options=None, direct=None)

# Generated at 2022-06-13 14:53:46.681710
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create an instance of look module
    lu = LookupModule()

    # Create an object for template class
    class DummyVars:
        pass
    v = DummyVars()

    # Set dummy values for following 3 templates
    v.path = '/home/dummy_ansible/temp_templates'
    v.new_path = '/home/dummy_ansible/temp_templates'
    v.ansible_play_hosts = ['host1', 'host2', 'host3']

    # vars and terms are the actual arguments passed to the method run of class LookupModule

# Generated at 2022-06-13 14:53:51.089848
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module=LookupModule()
    terms=['redhat']
    variables={'redhat': 'siddhesh', 'ubuntu':'manoj'}
    try:
        value = lookup_module.run(terms,variables)
        assert value == ['siddhesh']
    except Exception as e:
        raise e

# Generated at 2022-06-13 14:54:01.164783
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert_raises(AnsibleError, LookupModule().run, [ {'a': 1} ], {})
    assert_raises(
        AnsibleError,
        LookupModule().run,
        ['hostvars.example.com.ansible_ssh_host'],
        {
            'hostvars': {
                'example.com': {
                    'ansible_ssh_host': 'example.com'
                }
            }
        }
    )

# Generated at 2022-06-13 14:54:09.288452
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # No arguments passed
    lookup_module = LookupModule()
    result = lookup_module.run(terms=[])
    # Should handle error for two arguments passed
    lookup_module = LookupModule()
    result = lookup_module.run(terms=[],
                               variables={'inventory_hostname': 'localhost',
                                          'hostvars': {'localhost': {}}})
    assert isinstance(result, list)
    # Should handle error for three arguments passed
    lookup_module = LookupModule()
    result = lookup_module.run(terms=[], default="",
                               variables={'inventory_hostname': 'localhost',
                                          'hostvars': {'localhost': {}}})
    assert isinstance(result, list)
    # Should handle error for three arguments passed
    lookup_module = LookupModule()
   

# Generated at 2022-06-13 14:54:15.632522
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["ansible_play_hosts", "ansible_play_batch", "ansible_play_hosts_all"]
    host = {'ansible_play_hosts': ['hostname'], 'ansible_play_batch': ['192.168.1.1', '192.168.1.2'],
            'ansible_play_hosts_all': ['192.168.1.1', '192.168.1.2']}
    host_vars = {'inventory_hostname': 'hostname', 'hostvars': {'hostname': host}}
    mylookup = LookupModule()
    mylookup._templar = {}
    mylookup._templar._available_variables = host_vars

# Generated at 2022-06-13 14:54:22.861500
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    h_ansible_undefined_var = """\
---
msg: 'Hello, World!'
"""
    # AnsibleUndefinedVariable
    pytest.raises(AnsibleUndefinedVariable, LookupModule().run, [ "toto" ])
    # with default set
    assert LookupModule().run(["toto"], default="default") == ["default"]

    # variables is not None
    # with template
    assert LookupModule().run(["msg"], variables={"msg": "Hello, %(user)s"}, user="World") == ['Hello, World']
    # without template
    assert LookupModule().run(["msg"], variables={"msg": "Hello, World"}, user="World") == ['Hello, World']

    # hostvars
    # with template

# Generated at 2022-06-13 14:54:32.556136
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:54:41.580566
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Test for method run of class LookupModule."""

    test_instance = LookupModule()
    test_instance._templar = "test_instance Templar"
    test_instance._templar._available_variables = {'hostvars':{'host1':{'test_variable':'test_value'}}}
    terms = ['test_variable']
    result = test_instance.run(terms)
    expected_result = ['test_value']
    assert result == expected_result

    test_instance = LookupModule()
    test_instance._templar = "test_instance Templar"
    test_instance._templar._available_variables = {'test_variable':'test_value'}
    terms = ['test_variable']
    result = test_instance.run(terms)

# Generated at 2022-06-13 14:54:50.734816
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['ansible_play_hosts', 'ansible_play_batch', 'ansible_play_hosts_all', 'ansible_play_hosts_all_strings', 'ansible_play_hosts_all_blahblah']
    variables = {
        'ansible_play_hosts': [],
        'ansible_play_batch': [],
        'ansible_play_hosts_all': {},
        'inventory_hostname': 'localhost'
    }

    # first test with required variable name only
    lookup_obj = LookupModule()
    results = lookup_obj.run(terms, variables=variables)

    assert len(results) == 5
    assert results[0] == []
    assert results[1] == []
    assert results[2] == {}
    
    # second test

# Generated at 2022-06-13 14:54:59.838904
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    mylookup = LookupModule()

    # Test if raises exception when terms is not a string
    terms = (1, 2, 3)
    try:
        mylookup.run(terms)
        assert False
    except AnsibleError:
        assert True

    # Test if raises exception when terms is not a string
    terms = ["1", None, "3"]
    try:
        mylookup.run(terms)
        assert False
    except AnsibleError:
        assert True

    # Test if lookup value for a random variable
    variables = {
        'variablename': 'hello',
        'myvar': 'ename',
        'variablenotename': 'nothello'
    }
    assert mylookup.run(['variablenotename'], variables) == ['nothello']

    # Test if default value