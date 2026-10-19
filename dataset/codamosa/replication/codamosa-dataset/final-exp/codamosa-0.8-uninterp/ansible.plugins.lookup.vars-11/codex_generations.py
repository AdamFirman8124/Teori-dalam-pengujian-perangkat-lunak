

# Generated at 2022-06-13 14:45:09.883798
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test with one variable
    terms = ['test_var']
    variables = {
        'test_var': '12'
    }

    a = LookupModule()
    assert a.run(terms, variables) == ['12']

    # Test with a variable that does not exist
    terms = ['test_var2']
    variables = {
        'test_var': '12'
    }

    try:
        a = LookupModule()
        assert a.run(terms, variables)
    except Exception as e:
        assert str(e) == 'AnsibleUndefinedVariable: No variable found with this name: test_var2'

    # Test with a variable that does not exist and default
    terms = ['test_var2']
    variables = {
        'test_var': '12'
    }

    a = Look

# Generated at 2022-06-13 14:45:15.955744
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Setup
    class OptionsModule(object):
        def __init__(self):
            self._options = {
                'default': None,
                'run_once': False,
                'no_log': False,
                '_original_file': None,
                'task_vars': {},
                '_variable_manager': None,
                '_task': None
            }

        def get_option(self, option_key):
            return self._options.get( option_key, None)

        def update_option(self, option_key, value):
            self._options[option_key] = value

    class VariableModule(object):
        def __init__(self, item):
            self._item = item


# Generated at 2022-06-13 14:45:18.103974
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup import LookupModule
    from ansible.template import Templar
    from ansible.vars import VariableMa

# Generated at 2022-06-13 14:45:30.186558
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module.set_options(var_options={}, direct={'default': None })

    vars = {'name': 'value',
            'name2': 'value2'}
    lookup_module._templar = DummyTemplar()
    lookup_module._templar._available_variables = vars
    res = lookup_module.run(['name', 'name2'])
    assert res == ['value', 'value2']
    assert lookup_module._templar._template_called == 2

    lookup_module.set_options(var_options={}, direct={'default': 'default'})
    res = lookup_module.run(['name', 'name3'])
    assert res == ['value', 'default']


# Generated at 2022-06-13 14:45:41.359749
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test method with variables (not mandatory)
    module = LookupModule()

    # Test method with wrong type for terms string_types
    for term in ["hello", ["hello"], ("hello"), ("hello", "world")]:
        try:
            module.run(terms=term)
            assert False
        except AnsibleError:
            pass

    # Test method with variables not in dict
    for term in ["hello", "world"]:
        try:
            module.run(terms=term, variables=None)
            assert False
        except AnsibleUndefinedVariable:
            pass

    # Test method with term in variables
    terms = "hello"
    variables = {"hello": "world"}
    assert module.run(terms=terms, variables=variables) == ["world"]

    # Test method with term in variables but wrong value type

# Generated at 2022-06-13 14:45:44.220655
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule().run(["some_variable"], variables={"some_variable": "some_value"}) == ["some_value"]
    assert LookupModule().run(["some_undefined_variable"], variables={"some_variable": "some_value"}) == [""]
    assert LookupModule().run(["some_undefined_variable"], dict(variables={"some_variable": "some_value"}, default="")) == [""]

# Generated at 2022-06-13 14:45:51.023072
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = 'test_lookup_vars_class.py'
    is_error, has_changed, result = LookupModule.run_ansible_module(module, [])

    assert not is_error
    assert not has_changed
    assert result == {'_ansible_parsed': True, '_ansible_no_log': False, '_ansible_item_result': True, '_value': ['12'], '_ansible_ignore_errors': True}

# Generated at 2022-06-13 14:45:59.742160
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test __init__ and set_options
    lookup_module = LookupModule()
    assert type(lookup_module) is LookupModule

    # ensure only string accepted for terms
    failed = False
    try:
        lookup_module.run([{"this": "is", "solubility": "great"}])
    except AnsibleError as e:
        failed = True
        assert e.message == 'Invalid setting identifier, "{\'this\': \'is\', \'solubility\': \'great\'}" is not a string, its a <class \'dict\'>'
    assert failed == True

    # test run method
    lookup_module = LookupModule()
    lookup_module._templar = object()

# Generated at 2022-06-13 14:46:09.266448
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:46:19.376815
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.plugins.loader import lookup_loader
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from copy import deepcopy
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.hostvars import HostVars
    import pytest
    module_args = {
        '_terms': ['variablename', 'myvar'],
        '_templar': Templar(loader=None),
        '_available_variables': {'variablename': 'hello', 'myvar': 'ename', 'inventory_hostname': 'test_inven_hostname'}
    }

# Generated at 2022-06-13 14:46:29.569934
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test with variablname = 'hello' and myvar = 'ename'
    myvars = {'variablename': 'hello', 'myvar': 'ename'}

    from ansible.module_utils.six import PY2
    from ansible.module_utils.common._collections_compat import Mapping
    if PY2:
        myvars = Mapping(myvars)

    test1 = LookupModule().run(terms=[u'variabl' + myvars['myvar']], variables=myvars)
    assert test1 == ['hello']

    # test with variablname = 'hello' and myvar = 'notename'
    myvars['myvar'] = 'notename'

# Generated at 2022-06-13 14:46:38.753592
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()

    # Set hostvars with 2 hosts and two variables each
    module._templar._available_variables['hostvars'] = {}
    module._templar._available_variables['hostvars']['host1'] = {}
    module._templar._available_variables['hostvars']['host1']['hostvar1'] = 'a'
    module._templar._available_variables['hostvars']['host1']['hostvar2'] = 'b'
    module._templar._available_variables['hostvars']['host2'] = {}
    module._templar._available_variables['hostvars']['host2']['hostvar1'] = 'c'

# Generated at 2022-06-13 14:46:48.518255
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    assert lookup.run(['a'], {'a': 1}) == [1]

    with pytest.raises(AnsibleError):
        lookup.run([('a')], {'a': 1})

    with pytest.raises(AnsibleError):
        lookup.run(['a'])

    assert lookup.run(['a'], {'a': 1}, default=2) == [1]
    assert lookup.run(['a'], {}) == []

    assert lookup.run(['a'], {}, default=2) == [2]
    assert lookup.run(['a', 'b'], {'a': 1}, default=2) == [1, 2]

# Generated at 2022-06-13 14:46:59.930191
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    def _mock_get_option(option, default):
        if option == 'default':
            return default
        else:
            return None

    lookup_module._templar._available_variables = {'msg': 'Hello World'}

    def _mock_template(template, fail_on_undefined=True):
        return template

    lookup_module._templar.template = _mock_template
    lookup_module.get_option = _mock_get_option

    terms = ['msg']

    actual = lookup_module.run(terms, variables={}, var_templar=lookup_module._templar, default=None)
    assert actual == ['Hello World']


# Generated at 2022-06-13 14:47:08.500205
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    # Set attributes needed in method run of class LookupModule
    lookup._templar = {'_available_variables': {'hostname': 'host1'}}
    result = lookup.run(terms=['hostname'])
    assert result == ['host1']

    # Set attributes needed in method run of class LookupModule
    lookup._templar = {'_available_variables': {'hostvars': {'host1': {'nested_var': '12'}}}}
    result = lookup.run(terms=['nested_var'])
    assert result == ['12']

    # Set attributes needed in method run of class LookupModule
    lookup._templar = {'_available_variables': {}}

# Generated at 2022-06-13 14:47:20.078272
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    This test compares the LookupModule.run method against a reference list.
    The first list being the arguments for the run method of class LookupModule.
    The second list being the expected output of the run method.

    I have added a third list because I needed to create myself a reference result.
    I have added this third list to make the test independant from my reference output.
    """
    # First list is the reference input for the run method

# Generated at 2022-06-13 14:47:30.531865
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Outputs
    output_run_1 = [u'hello']
    output_run_1_str = str(output_run_1)
    output_run_2 = [u'']
    output_run_2_str = str(output_run_2)
    output_run_3 = [u'hello']
    output_run_3_str = str(output_run_3)

# Generated at 2022-06-13 14:47:38.964005
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l._templar = DummyJinja2()
    l._templar._available_variables = {'var':'hello','var2':'foo', 'inventory_hostname':'localhost',
                                       'hostvars':{'localhost': {'var3': 'bar'}} }
    assert l.run(['var','var2']) == ['hello', 'foo']
    assert l.run(['var','var3']) == ['hello', 'bar']


# Mock object of jinja2.Environment

# Generated at 2022-06-13 14:47:42.962455
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['inventory_hostname']
    variables = {'inventory_hostname': 'test_hostname'}
    default = 'default'
    myvars = {'inventory_hostname': 'test_hostname'}
    templar = Templar(variables=variables)
    templar._available_variables = variables
    looker = Looker(templar=templar)
    assert looker.run(terms, myvars) == variables.values()
    looker.set_options(var_options=variables, direct={'default': default})
    assert looker.get_option('default') == default
    templar.available_variables = myvars
    myvars.pop('inventory_hostname')
    assert looker.run(terms) == [default]

# Generated at 2022-06-13 14:47:51.200861
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    my_vars = {'a': 1, 'b': 2, 'c': 3}
    lookup_module.run([], variables=my_vars)
    result = lookup_module.run(['a'], variables=my_vars)
    assert result == [1]
    result = lookup_module.run(['b'], variables=my_vars)
    assert result == [2]
    result = lookup_module.run(['c'], variables=my_vars)
    assert result == [3]
    result = lookup_module.run(['c', 'b'], variables=my_vars)
    assert result == [3, 2]
    result = lookup_module.run(['c', 'a'], variables=my_vars)

# Generated at 2022-06-13 14:48:02.053159
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()
    # Test variables
    test_terms = []
    test_kwargs = {}
    # Expected output
    expected = []
    # Test
    actual = lookup_plugin.run(test_terms, variables=None, **test_kwargs)
    assert actual == expected, "ERROR[1]: Expected: "+str(expected) + " != Actual: "+str(actual)

    # Test variables
    test_terms = ["var1", "var2"]
    test_kwargs = {}

    # Expected output
    expected = []
    myvars = {
        "var1": "value1",
        "var2": "value2",
    }
    # Test
    actual = lookup_plugin.run(test_terms, variables=myvars, **test_kwargs)

# Generated at 2022-06-13 14:48:04.053095
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''
    Unit test for method run of class LookupModule

    '''

    assert callable(LookupModule().run)

# Generated at 2022-06-13 14:48:11.019568
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Initialize the class
    my_lookup_module = LookupModule()
    # Test with default parameters (No variables term)
    # This should return an empty list

# Generated at 2022-06-13 14:48:17.135012
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lu = LookupModule()
    terms = ['val1','val2','val3']
    variables={
        'val1': 'val11',
        'val2': 'val22',
        'val3': 'val33'
    }
    assert(lu.run(terms, variables) == ['val11', 'val22', 'val33'])
    assert(lu.run([],variables) == [])

# Generated at 2022-06-13 14:48:39.997279
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # pylint: disable=too-many-arguments,too-many-locals
    from ansible.plugins.lookup.vars import LookupModule
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.template import Templar

    mylookup = LookupModule()

    mylookup.set_options(direct={'default': 'A default', 'play_hosts': 'p_h'})

    # init needed objects
    loader = DataLoader()
    variable_manager = VariableManager()

    # set needed objects on lookup
    mylookup._loader = loader
    mylookup._templar = Templar(loader=loader, variables=variable_manager)

# Generated at 2022-06-13 14:48:42.576936
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Test case for the method run of class LookupModule
    """
    LookupModule()
    print("Test success for method run of class LookupModule")

# Generated at 2022-06-13 14:48:49.788989
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:48:57.528593
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test_LookupModule_run() method
    #
    # A test case for the LookupModule.run() method.
    #
    # Here, we test to see if the LookupModule.run() method will
    # return the value of the variable as specified in
    # the parameter terms.

    # create instance LookupModule
    lookup_mod = LookupModule()

    # create sample group variables and or host variables
    # within the scope of the LookupModule class
    lookup_mod._templar = {
        '_available_variables':
            {'var1': 'val1',
             'var2': 'val2',
             'var3': 'val3'
             }
    }

    # test to see if the LookupModule class will return
    # the value of the variable as specified in
    # the parameter

# Generated at 2022-06-13 14:49:02.027178
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module.get_option = lambda x: ''
    lookup_module.set_options = lambda y, z: ''
    lookup_module.run(terms = ["variablename", 'variablenotename'], variables = { "variablename" : "hi" } )
    return

# Generated at 2022-06-13 14:49:12.341075
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l.set_loader(None)
    result = l.run(terms=['test_variable'], variables={'test_variable': 'hello_world'})
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] == 'hello_world'

    default_value = 'default_value'
    result = l.run(terms=['test_variable'], variables={}, default=default_value)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] == default_value


# Generated at 2022-06-13 14:49:35.208262
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Generate random variable name
    from string import ascii_letters
    from random import choice
    var_name = ''.join(choice(ascii_letters) for _ in range(15))

    # Generate random value
    from uuid import uuid4
    var_value = str(uuid4())

    # Initialize LookupModule
    from ansible.plugins.lookup import LookupModule
    lookup_module = LookupModule()

    # Execute method run
    terms = [var_name]
    variables = dict()
    variables[var_name] = var_value
    variables['inventory_hostname'] = 'dummy_name'
    variables['hostvars'] = dict()
    variables['hostvars']['dummy_name'] = dict()

# Generated at 2022-06-13 14:49:40.099566
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    first_var = 'ansible_ssh_user'
    second_var = 'ansible_user'
    third_var = 'ansible_play_hosts'
    terms = [first_var, second_var, third_var]
    assert module.run(terms=terms) == ['root', 'root', None]

# Generated at 2022-06-13 14:49:48.424923
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Arrange
    import sys

    sys.path.append('../')
    import test_utils
    test_utils.run_module(['-c', './unit_tests/vars_ansible.cfg'])

    from ansible.template import Templar
    templar = Templar(loader=None)
    lookup_mod = LookupModule()
    lookup_mod._templar = templar

    # Act
    result = lookup_mod.run(terms=['variable', 'hostname'])

    # Assert
    assert result[0] == 'hi'
    assert result[1] == 'localhost'

# Generated at 2022-06-13 14:49:58.203426
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    if sys.version_info[0] >= 3:
        long = int
    import json
    import yaml
    # Pass the template through the vars lookup.
    # This will allow the use of a template
    # to generate the input to the lookup
    def _vars_lookup_templated_variable(value, variables, fail_on_undefined):
        from ansible.template import Templar
        templar = Templar(loader=None, variables=variables)
        return templar.template(value, fail_on_undefined=fail_on_undefined, convert_bare=True)


# Generated at 2022-06-13 14:50:08.412558
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    assert lookup.run(["invalid"]) == []
    assert lookup.run(["invalid"], default="ok") == ["ok"]
    assert lookup.run(["invalid"], default=["ok"]) == ["ok"]
    assert lookup.run(["invalid"], default=["ok", "ok2"]) == ["ok", "ok2"]
    assert lookup.run(["invalid"], default="ok", ignore_undefined=True) == ["ok"]
    assert lookup.run(["invalid"], default=["ok"], ignore_undefined=True) == ["ok"]
    assert lookup.run(["invalid"], default=["ok", "ok2"], ignore_undefined=True) == ["ok", "ok2"]

# Generated at 2022-06-13 14:50:15.071268
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class LookupModule_obj(LookupModule):

        def __init__(self):
            pass

        def get_option(self, option):
            return 'test'

    class Templar():

        def __init__(self):
            self.diff = {}

        def template(self, term, fail_on_undefined=True):
            return term

    class Variables():

        def __init__(self):
            self.diff = {}

        def __getitem__(self, name):
            return self.diff[name]

        def __setitem__(self, name, value):
            self.diff[name] = value

    templar = Templar()
    variables = Variables()

    # test vars is defined
    variables['variables'] = 'variables'
    lookup_module_obj = LookupModule_

# Generated at 2022-06-13 14:50:24.567442
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    lookup._templar._available_variables = {'variablename': 'hello', 'myvar': 'ename', 'hostvars': {'host': {'var_host': 'value_host'}}}

    lookup._templar.available_variables = {}
    assert lookup.run([], variables={'variablename': 'hello', 'myvar': 'ename', 'hostvars': {'host': {'var_host': 'value_host'}}}) == []

    assert lookup.run(['variablename'], variables={'variablename': 'hello', 'myvar': 'ename', 'hostvars': {'host': {'var_host': 'value_host'}}}) == ['hello']

# Generated at 2022-06-13 14:50:34.480350
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    _templar = Dummy({'inventory_hostname': 'testhost'})

    lm = LookupModule()
    lm._templar = _templar
    lm.set_options = Mock()

    # test variables and values that should be added to _templar._available_variables
    variables = {'var1': 'value1', 'var2': 'value2', 'var3': 'value3'}
    # test variables and values that should be passed as kwargs
    kwargs = {'kwarg1': 'kwarg1', 'kwarg2': 'kwarg2', 'kwarg3': 'kwarg3'}

    # set the variables that should be returned
    terms = ['var1', 'var2', 'var4']

    # add the test values to _templar._available_vari

# Generated at 2022-06-13 14:50:44.639789
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a fake context to be used for tests
    class FakeContext:
        def __init__(self):
            self.hostvars = {}
            self.hostvars['hostname1'] = {}
            self.hostvars['hostname1']['var_a'] = 'value_a'
            self.hostvars['hostname1']['var_b'] = 'value_b'
            self.hostvars['hostname2'] = {}
            self.hostvars['hostname2']['var_a'] = 'value_a'
            self.hostvars['hostname2']['var_b'] = 'value_b'
        # Fake method which will be called from the templar
        def template(self, value, fail_on_undefined=True):
            return value

    # Create

# Generated at 2022-06-13 14:50:48.588494
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Arrange
    terms = ['key', 'other_key']
    variables = {'key': 'value', 'other_key': 'other_value'}
    lookup = LookupModule()

    # Act
    result = lookup.run(terms, variables)

    # Assert
    assert type(result) is list
    assert 'value' in result
    assert 'other_value' in result

# Generated at 2022-06-13 14:51:22.809710
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    parameters = [ 'ansible_play_hosts', 'ansible_play_batch', 'ansible_play_hosts_all' ]
    variables = {'ansible_play_hosts': ['192.168.33.10']}
    actual = lookup_module.run(parameters, variables)
    expected = ["['192.168.33.10']", None, None]
    assert actual == expected, 'LookupModule.run() failed with Invalid output'

# Generated at 2022-06-13 14:51:33.566548
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()

    # test method run with a term which is not string type
    lm.set_options(var_options={}, direct={})
    terms = [123]
    variables = None
    try:
        lm.run(terms, variables)
    except Exception as e:
        assert str(e) == 'Invalid setting identifier, "123" is not a string, its a %s' % type(123)

    # test method run with term with no default value and no matching variable
    lm.set_options(var_options={}, direct={})
    terms = ['term_not_matched']
    variables = {}

# Generated at 2022-06-13 14:51:42.667913
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['a']
    variables = {'hostvars': {'host1': {'a': 'b'}}}
    kwargs = {'play_hosts': ['host1']}
    lookup = LookupModule()
    assert lookup.run(terms, variables, **kwargs) == ['b']

    terms = ['a']
    variables = {'hostvars': {'host1': {'a': 'b'}}}
    kwargs = {'play_hosts': ['host2']}
    lookup = LookupModule()
    assert lookup.run(terms, variables, **kwargs) == ['b']

    terms = ['b', 'c']
    variables = {'hostvars': {'host1': {'a': 'b'}}, 'a': 'b', 'c': 'b'}
    k

# Generated at 2022-06-13 14:51:49.834235
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import sys

    #
    # Remove path to lookup_plugins/cache from sys.path
    #
    lookup_plugins_cache_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'lookup_plugins', 'cache')
    if sys.path[-1] == lookup_plugins_cache_path:
        sys.path.pop()

    os.chdir('../../')
    lookupModule = LookupModule()
    os.chdir('.tox/py27/lib/python2.7/site-packages/lib/ansible/plugins/lookup/') # path of file which invoke test

    #
    # Test with correct params
    #
    print('Test1')

# Generated at 2022-06-13 14:51:58.690440
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Create instance of class LookupModule
    lookup_module = LookupModule()

    # Create variable terms with a list of tuples
    terms = ['ansible_play_hosts', 'ansible_play_batch', 'ansible_play_hosts_all']

    # Create variable myvars
    myvars = {
        'ansible_play_hosts': ['localhost'],
        'ansible_play_batch': ['localhost'],
        'ansible_play_hosts_all': ['localhost'],
        'inventory_hostname': 'localhost',
        'hostvars': {'localhost': {}}
    }

    # Retrieve the value of an Ansible variable
    # Note: Only returns top level variable names.

# Generated at 2022-06-13 14:52:06.172934
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    host_name = 'hostvars_host_name'
    sub_var = 'subvar_host_name'
    test_lookup_plugin = LookupModule()
    test_lookup_plugin._templar._available_variables['inventory_hostname'] = host_name
    test_lookup_plugin._templar._available_variables['hostvars'] = {}
    my_var = {}
    my_var[sub_var] = 'aaa'
    test_lookup_plugin._templar._available_variables['hostvars'][host_name] = my_var
    test_lookup_plugin._templar._available_variables[sub_var] = 'bbb'

# Generated at 2022-06-13 14:52:15.088809
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import ansible.plugins.lookup
    import ansible.plugins.loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    # Load Plugins
    loader = ansible.plugins.loader.LookupModuleLoader(None, None)
    lookup_loader = ansible.plugins.loader.LookupModuleLoader(None, None)
    lookup_loader._package_paths = []
    lookup_loader.set_directory(["ansible/plugins/lookup"])
    lookup_loader.find_plugin("vars")

    # Load Inventory
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=["ansible/tests/inventory"])

    # Create Variables

# Generated at 2022-06-13 14:52:19.973644
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # given
    lm = LookupModule()

    # when
    try:
        lm.run([123], {'foo':'bar'})
    except AnsibleError as e:
        assert str(e) == 'Invalid setting identifier, "123" is not a string, its a <class \'int\'>'

# Generated at 2022-06-13 14:52:29.341336
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import PY3
    import sys

    if PY3:
        from io import StringIO
    else:
        from StringIO import StringIO

    out = StringIO()
    err = StringIO()

    l = LookupModule()
    l.set_options(direct={})

    l._templar.set_available_variables({'a': 'Hi'})

    sys.stdout = out
    sys.stderr = err

    try:
        l.run(['a'])
    except Exception as e:
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

        assert False, e.message

    assert out.getvalue() == 'Hi\n', out.getvalue()
    assert err.getvalue

# Generated at 2022-06-13 14:52:29.825049
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 14:53:39.867358
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['ansible_play_hosts', 'ansible_play_batch', 'ansible_play_hosts_all']
    variables = {'play': {'hosts': [1], 'batch': 2, 'hosts_all': [1, 2, 3]}}
    expected_result = [
        [1],
        2,
        [1, 2, 3],
    ]
    result = LookupModule().run(terms, variables)
    assert result == expected_result

# Generated at 2022-06-13 14:53:45.987750
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    lookup._loader = DummyLoader({})

    # _templar is not set, _available_variables is not set
    lookup._templar = None
    assert lookup.run([]) == [], 'should be empty'

    # _templar is not set, _available_variables is not set
    lookup._templar = None
    assert lookup.run(['non_exist_var']) == [], 'should be empty'

    # _templar is not set, _available_variables is not set, default is set
    lookup._templar = None
    assert lookup.run(['non_exist_var'], default='abc') == ['abc'], 'should be empty'

    # _templar._available_variables is set, _available_variables is not set
   

# Generated at 2022-06-13 14:53:55.893455
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch, MagicMock

    with patch('ansible.plugins.lookup.vars.LookupBase.run') as lookup_base_run:
        lookup_base_run.return_value = 'some_result'
        lookup_obj = LookupModule()
        result = lookup_obj.run(['varname'], 'variables')
        assert result == 'some_result'
        lookup_base_run.assert_called_once_with(['varname'], variables='variables', **{})

    class TestException(Exception):
        pass

    with patch('ansible.plugins.lookup.vars.AnsibleUndefinedVariable') as ansible_undefined_variable:
        ansible_undefined_

# Generated at 2022-06-13 14:54:05.134590
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # A dict of ansible variables
    variables = {'var':'var val', 'hostvars':{'hostname':{'hostvar':'hostvar val'}}}

    # Create an instance of LookupModule
    lm = LookupModule()

    # Create an instance of the templar class and attach it as an attribute of LookupModule
    class FakeTemplar():
        def __init__(self):
            self.available_variables = variables
        def template(self, data, fail_on_undefined=None):
            return data

    lm._templar = FakeTemplar()

    # Test with a variable defined in 'variables' dict
    terms = ['var']
    result = lm.run(terms, variables=variables)
    assert result == ['var val']

    # Test with a variable inside

# Generated at 2022-06-13 14:54:12.083917
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test case where variable is defined
    mm = LookupModule()
    mm._templar._available_variables = {'test_variable': 'test_value'}
    terms = ['test_variable']
    result = mm.run(terms)
    assert result == ['test_value']
    # Test case where variable is undefined
    terms = ['not_defined']
    mm._templar._available_variables = {'test_variable': 'test_value'}
    mm._templar.environment = 'test'
    result = mm.run(terms)
    assert result == []

# Generated at 2022-06-13 14:54:12.818751
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass


# Generated at 2022-06-13 14:54:18.721662
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test = LookupModule()
    terms = ["myvar"]
    variables = {
        "myvar": "hello",
        "myvar2": "world",
        "inventory_hostname": "localhost",
        "hostvars": {
            "localhost": {
                "myvar3": "local_var"
            }
        }
    }
    returned_value = test.run(terms=terms, variables=variables)
    assert returned_value == ["hello"]

    terms = ["myvar", "myvar2"]
    variables = {
        "myvar": "hello",
        "myvar2": "world",
        "inventory_hostname": "localhost",
        "hostvars": {
            "localhost": {
                "myvar3": "local_var"
            }
        }
    }
   

# Generated at 2022-06-13 14:54:25.883614
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms_with_1_value = ["ansible_play_hosts"]
    terms_with_2_values = ["ansible_play_batch", "ansible_play_hosts_all"]
    terms_with_3_values = ["ansible_play_hosts", "ansible_play_batch", "ansible_play_hosts_all"]

    terms_with_no_value = ["ansible_play_hosts_not_exists"]
    terms_with_1_undefined_variable = ["ansible_play_hosts", "ansible_play_hosts_not_exists"]
    terms_with_2_undefined_variables = ["ansible_play_hosts_not_exists_1", "ansible_play_hosts_not_exists_2"]
    terms_with_1_

# Generated at 2022-06-13 14:54:31.465298
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lu = LookupModule()
    lu._templar.available_variables = {'inventory_hostname': 'foo', 'hostvars': {'foo': {'bar': 'foo_bar'}}}
    terms = ['inventory_hostname', 'hostvars']
    res = lu.run(terms)
    assert res[0] == 'foo'
    assert res[1] == {'foo': {'bar': 'foo_bar'}}

# Generated at 2022-06-13 14:54:40.333932
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup import LookupModule
    from ansible.module_utils.six import string_types
    from ansible.module_utils._text import to_bytes, to_native
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor

    # initializing LookupModule class 
    test_lookup = LookupModule()
    loader = DataLoader()
    inv_manager = InventoryManager(loader=loader, sources='')
    inv_manager.set_inventory(inv_manager.inventory)