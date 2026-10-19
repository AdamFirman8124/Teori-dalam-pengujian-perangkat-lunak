

# Generated at 2022-06-13 14:45:10.474739
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.vars import VariableManager

    variable_manager = VariableManager()
    variable_manager._extra_vars = {"first": "first variable"}
    variable_manager._options = {"extra_vars": {"second": "second variable"}}
    variable_manager._available_variables = {"inventory_hostname": "localhost"}

    look = LookupModule()
    look._templar = variable_manager.get_vars(loader=None, play=None, host=None)

    ret = look.run([
        "first",
        "second",
        "third",
    ], variables={
        "first": "v1",
        "second": "v2",
        "third": "v3",
    })

    assert ret == ["v1", "v2", "v3"]


# Generated at 2022-06-13 14:45:16.323987
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    class FakeAnsibleModule:

        def __init__(self):
            self.params = dict()

        def get_option(self, option):
            return self.params.get(option)

    class FakeTemplar():
        def __init__(self):
            self._available_variables = dict()

        def template(self, value, fail_on_undefined):
            return value

    fake_module = FakeAnsibleModule()
    fake_module.params = dict()
    fake_templar = FakeTemplar()
    fake_templar._available_variables = {'term_with_value':'term_value'}

    lookup = LookupModule(fake_module, templar=fake_templar)


# Generated at 2022-06-13 14:45:24.135931
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Setup
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['127.0.0.1,', 'localhost,'])
    variable_manager.set_inventory(inventory)

# Generated at 2022-06-13 14:45:32.465270
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # A class for testing lookup module
    # The tests are run by test_lookup.py
    class Class1(LookupModule):
        def run(self, terms, variables=None, **kwargs):
            return [1]

    class Class2(LookupModule):
        def run(self, terms, variables=None, **kwargs):
            return [2]

    class Class3(LookupModule):
        def run(self, terms, variables=None, **kwargs):
            return [3]

    # Method run is tested by test_lookup.py
    result = Class1().run([1,2,3])
    assert result == [1]

# Generated at 2022-06-13 14:45:42.949822
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    """
    Test for the LookupModule.run method.
    """

    lookup_module = LookupModule()

    terms = ['var1', 'var2', 'var3']
    variables = {'var1': 1, 'var2': 2, 'var3': 3, 'var4': 4}
    kwargs = {'generic': 1}

    assert lookup_module.run(terms, variables=variables, **kwargs) == [1, 2, 3]

    terms = ['var1', 'var2', 'var3', 'var4', 'var5']
    kwargs = {'default': 0}

    assert lookup_module.run(terms, variables=variables, **kwargs) == [1, 2, 3, 4, 0]

    # Error: Invalid setting identifier
    lookup_module = LookupModule()



# Generated at 2022-06-13 14:45:53.839377
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils._text import to_bytes
    

# Generated at 2022-06-13 14:46:04.298968
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.compat.six import BytesIO

    my_run = LookupModule().run
    # Inject a fake file into the module._templar.loader so that we do not have to
    # load a real file
    LookupModule()._templar.loader.set_basedir(None)
    LookupModule()._templar.loader.add_directory(u'test', BytesIO())

    # [0] Successful
    result = my_run([u'var'], {u'var': u'{{foo}}'}, foo=u'bar')
    assert result == [u'bar']

    # [1] Successful with multiple variables

# Generated at 2022-06-13 14:46:04.947842
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert True

# Generated at 2022-06-13 14:46:14.481255
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import PY3

    mod = LookupModule()
    mod.set_options(direct={'_original_file': '', '_terms': 'ansible_play_hosts', '_lineage': []})
    mod._templar._available_variables = {'ansible_play_hosts': ['test_term_item']}

    assert mod.run(terms=['ansible_play_hosts']) == [['test_term_item']]

    # Test with a list of terms
    mod.set_options(direct={'_original_file': '', '_terms': ['ansible_play_hosts', 'ansible_play_batch', 'ansible_play_hosts_all'], '_lineage': []})
    mod._templar._available_variables

# Generated at 2022-06-13 14:46:23.124691
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup.vars import LookupModule
    from ansible.template import Templar
    from ansible.vars import VariableManager

    var_manager = VariableManager()
    var_manager.set_inventory(inventory=dict(hostvars=dict(hostname=dict(var_name='value'))))
    templar = Templar(loader=None, variables=var_manager)

    lookup_module = LookupModule()
    lookup_module._templar = templar
    lookup_module._templar._available_variables = dict(inventory_hostname='hostname', var_name='var_value')

    # Test success
    assert lookup_module.run([u'var_name'], dict(inventory_hostname='hostname')) == ['var_value']

    # Test error

# Generated at 2022-06-13 14:46:30.293459
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    assert lookup_module.run([u'foo'], {u'foo': u'bar'}) == [u'bar']
    assert lookup_module.run([u'foo'], {u'foo': u'bar', u'bar': u'foo'}) == [u'bar']
    assert lookup_module.run([u'foo', u'bar'], {u'foo': u'bar', u'bar': u'foo'}) == [u'bar', u'foo']

# Generated at 2022-06-13 14:46:40.014768
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Arrange
    args = ['ansible_play_hosts', 'ansible_play_batch', 'ansible_play_hosts_all']
    variables = {
        "ansible_play_hosts": ["192.168.1.10", "192.168.1.20"],
        "ansible_play_hosts_all": ["192.168.1.10", "192.168.1.20"],
        "ansible_play_batch": 0
    }

    # Act
    lookup_module = LookupModule()
    returned_value = lookup_module.run(terms=args, variables=variables)

    # Assert

# Generated at 2022-06-13 14:46:43.986342
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), u'..', u'..',))
    look = LookupModule()
    values = look.run(['some_variable'])
    assert len(values) == 1
    assert values[0] == 'victory'

# Generated at 2022-06-13 14:46:50.208659
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test return variable if variable is exist
    test_lookup = LookupModule()
    test_lookup._templar._available_variables = {'a':'1', 'b':'2', 'c':'3'}
    assert test_lookup.run(['a', 'b'], {'a':'1', 'b':'2', 'c':'3'}) == ['1', '2']


# Generated at 2022-06-13 14:47:01.978184
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.vars import combine_vars, load_extra_vars, combine_facts
    # Create a templar object
    from ansible.parsing.vault import VaultLib
    vault_secret = VaultLib()
    templar = Templar(loader=None, variables={'inventory_hostname': 'localhost'}, vault_secrets=[vault_secret])

    # Create a lookup module object
    lookup = LookupModule()

    # Create a fake module
    module_name = 'fake'
    module_args = {'myvar1': 'value1', 'myvar2': 'value2'}
    module_kwargs = {'myvar3': 'value3'}

# Generated at 2022-06-13 14:47:09.640408
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup.vars import LookupModule
    from ansible.module_utils._text import to_bytes
    from ansible.template import Templar
    from ansible import context

    test_templar = Templar(loader=None, variables=dict(test_var='test_value'))
    lookup_module = LookupModule()

    variables = None
    test_terms = ['test_var']
    test_kwargs = {}

    result = lookup_module.run(test_terms, variables, **test_kwargs)
    assert isinstance(result, list)
    assert len(result) == 1
    assert isinstance(result[0], to_bytes)
    assert result[0] == 'test_value'

    test_terms = []

# Generated at 2022-06-13 14:47:10.248126
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 14:47:21.188332
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    lm.set_loader(DictDataLoader({}))
    lm._templar.set_available_variables({
        'ansible_play_hosts': [],
        'ansible_play_batch': [],
        'ansible_play_hosts_all': [],
        'hostvars': {
            'localhost': {
                'ansible_play_hosts': [],
                'ansible_play_batch': [],
                'ansible_play_hosts_all': []
            }
        }
    })
    assert lm.run(["ansible_play_hosts", "ansible_play_batch", "ansible_play_hosts_all"]) == [[], [], []]


# Test for method set_options of class Lookup

# Generated at 2022-06-13 14:47:31.268113
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test with a variable that exists
    variable_name = "variable"
    variable_value = "value"
    variable_dict = { variable_name: variable_value }

    # Test without a default value
    lookup_module = LookupModule()
    result = lookup_module.run([variable_name], variable_dict)
    assert result == [variable_value]

    # Test with a default value
    default_value = "default"
    result = lookup_module.run([variable_name], variable_dict, default=default_value)
    assert result == [variable_value]

    # Test with an undefined variable
    variable_name = "undefined"
    result = lookup_module.run([variable_name], variable_dict)
    assert result == []

    # Test with an undefined variable and a default value
    result = lookup_module

# Generated at 2022-06-13 14:47:42.108005
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Mock AnsibleModule class from Ansible
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.facts import ansible_facts
    import os

    my_vars_dict = {
        'apt_repo': 'http://repo.example.com/x/x/x/x/x/x/x',
        'is_correct_apt_repo': True,
        'is_incorrect_apt_repo': False
    }

    # Create an instance of AnsibleModule class to test the LookupModule class

# Generated at 2022-06-13 14:47:52.473026
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    assert isinstance(lookup, LookupModule)

# Generated at 2022-06-13 14:48:03.549450
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    assertion = "hello"
    assertion1 = "world"
    assertion2 = "12"

    # Test 1
    test_variables = {
        "variablename": "hello"
    }
    test_variables.update({"myvar": "ename"})
    test_variables.update({"_terms": ["variabl" + test_variables['myvar']]})

    assert lookup.run([test_variables['_terms'][0]], variables=test_variables) == [assertion]

    # Test 2
    test_variables = {
        "variablename": "hello"
    }
    test_variables.update({"myvar": "notename"})

# Generated at 2022-06-13 14:48:15.713394
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible.vars.manager import VariableManager

    class VarsModule:
        def __init__(self):
            self.lookup_plugin = LookupModule()
            self.variable_manager = VariableManager()
            self.variable_manager.set_inventory(pytest.inventory)

            self.variable_manager.set_host_variable(
                host='target2',
                varname='key_var',
                value='key'
            )

            self.variable_manager.set_host_variable(
                host='target1',
                varname='var_one',
                value='val_one'
            )
            self.variable_manager.set_host_variable(
                host='target2',
                varname='var_one',
                value='val_one_target2'
            )


# Generated at 2022-06-13 14:48:17.452873
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule(None, {}).run(terms=terms, variables=variables, **kwargs) == result

# Generated at 2022-06-13 14:48:28.565581
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test with all valid input data
    lookup_module = LookupModule()
    in_data = ['ansible_play_hosts', 'ansible_play_batch', 'ansible_play_hosts_all']
    out_data = lookup_module.run(in_data)
    assert out_data == [u'127.0.0.1', [0], u'127.0.0.1']
    # Test with default option
    in_data = ['variabnotename']
    out_data = lookup_module.run(in_data, default='default')
    assert out_data == ['default']
    # Test with error
    in_data = ['variabnotename']
    out_data = lookup_module.run(in_data, fail_on_undefined=False)

# Generated at 2022-06-13 14:48:35.284150
# Unit test for method run of class LookupModule
def test_LookupModule_run():
        a = LookupModule()
        b = {'my_var' : 'my_value', 'inventory_hostname':'localhost', 'hostvars':{'localhost':{'localhost_var' : 'localhost_value'}}}
        c = ['my_var', 'localhost_var']
        a.run(terms=c, variables=b)
        assert a._templar._available_variables == b
        assert a.run(terms=c, variables=b) == ['my_value', 'localhost_value']

# Generated at 2022-06-13 14:48:44.650767
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["hello", "play_hosts_all", "inventory_hostname"]

    vars = {
        'hello': 'world',
        'hostvars': {
            'test.example.com': {
                'inventory_hostname': 'test.example.com',
                'super_secret_var': 'hidden'
            }
        },
        'inventory_hostname': 'test.example.com',
        'play_hosts_all': 'test.example.com',
    }

    assert LookupModule().run(terms,vars,None) == ['world', 'test.example.com', 'test.example.com']
    assert LookupModule().run([],vars,default='') == ['']

# Generated at 2022-06-13 14:48:54.465575
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    # Test with invalid type of param 'terms'
    try:
        lookup_module.run(terms=123)
        assert False
    except AnsibleError as e:
        assert "is not a string" in str(e)

    # Test with non-existed variables
    lookup_module._templar._available_variables = {}
    assert lookup_module.run(terms=['not_existed_var']) == []

    # Test with existed variables
    lookup_module._templar._available_variables = {'existed_var': 123}
    assert lookup_module.run(terms=['existed_var']) == [123]

# Generated at 2022-06-13 14:49:04.470152
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ('inventory_hostname', 'play_hosts')

# Generated at 2022-06-13 14:49:15.005668
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    terms = ['ansible_play_hosts', 'ansible_play_batch', 'ansible_play_hosts_all']
    variables = {
        'ansible_play_hosts': 'foo',
        'ansible_play_batch': 41,
        'ansible_play_hosts_all': [12, 'asd', 12.45],
        'hostvars': {'host': {
            'ansible_play_hosts': 'host',
            'ansible_play_batch': 'host',
            'ansible_play_hosts_all': 'host'
        }}
    }
    kwargs = {'_variables': variables, 'inventory_hostname': 'host'}

# Generated at 2022-06-13 14:49:33.460162
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test with list of variables
    lookup_instance = LookupModule()
    lookup_instance._templar = DummyTemplar()
    terms = ['ansible_play_hosts', 'ansible_play_batch', 'ansible_play_hosts_all']
    results = lookup_instance.run(terms)
    assert(isinstance(results, list))
    assert(len(results) == 3)
    assert(results == ['ansible_play_hosts', 'ansible_play_batch', 'ansible_play_hosts_all'])

    # Test with single variable
    lookup_instance = LookupModule()
    lookup_instance._templar = DummyTemplar()
    terms = ['ansible_play_hosts']
    results = lookup_instance.run(terms)

# Generated at 2022-06-13 14:49:44.042154
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''Test the functions'''
    print("\nTesting LookupModule_run")
    myvars = LookupModule()

    terms = ['var', 'var2']

    # SETTINGS
    print("\n\tSettings, get_option")
    # Should be: None
    assert myvars.get_option('default') == None

    # Should be: 'default_value'
    myvars.set_options(var_options=None, direct={'default': 'default_value'})
    assert myvars.get_option('default') == 'default_value'

    # Should be: 'default_value'
    myvars.set_options(var_options=None, direct={'default': 'new_default_value'})

# Generated at 2022-06-13 14:49:53.756363
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    # Test with a list of items.
    lookup_module.set_options(direct={'default': ''})
    ret = lookup_module.run(['default', 'myvar'], variables={'myvar': 'myvalue'})
    assert ret == ['', 'myvalue']

    # Test with a dict.
    lookup_module.set_options(direct={'default': ''})
    ret = lookup_module.run(['default', 'myvar'], variables={'myvar': {'nestedvar': 'myvalue'}})
    assert ret == ['', {'nestedvar': 'myvalue'}]

# Generated at 2022-06-13 14:50:05.514542
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Set initializing variables
    lookup_module = LookupModule()
    lookup_module._templar._available_variables = {'variablename': 'hello', 'myvar': 'ename'}
    lookup_module.set_options(var_options={'inventory_hostname': 'localhost', 'hostvars': {'localhost': {'variablename': 'hello', 'myvar': 'ename'}}}, direct={})

    # Test variable names given are strings
    assert isinstance(lookup_module.run(['variablename'])[0], str)

    # Test variable names given are not strings
    try:
        lookup_module.run([1])
    except AnsibleError:
        pass

    # Test lookup doesn't throw exceptions because of undefined variables
    lookup_module = LookupModule()
    lookup_module

# Generated at 2022-06-13 14:50:11.068669
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create an instance of class LookupModule
    lookup_module = LookupModule()

    # Create a dict used as value in the method
    variables = {}

    # Create the variables used as argument in the method
    terms = ["toto", "tata"]
    kwargs = {}

    # Return the result of the method run of class LookupModule
    return lookup_module.run(terms, variables, **kwargs)


# Generated at 2022-06-13 14:50:17.759561
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create object of class LookupModule
    lookup = LookupModule()
    # Call run method of class LookupModule and provide terms, variables,
    # and kwargs as input
    lookup.run(terms = ['ansible_play_hosts', 'ansible_play_batch', 'ansible_play_hosts_all'], variables = None, **{'_original_file': 'chained_lookup_plugin.py', '_original_line': '37'})

# Generated at 2022-06-13 14:50:25.795126
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    def test_run_normal(terms, variables, default, expected):
        lookup_module = LookupModule()
        result = lookup_module.run(terms, variables=variables, default=default)
        assert result == expected

    tests = dict()

    terms = ['foo', 'bar', 'ansible_play_hosts']
    variables = dict()
    variables['foo'] = 'foo_value'
    variables['hostvars'] = dict()
    variables['hostvars']['test_host'] = dict()
    variables['hostvars']['test_host']['bar'] = 'bar_value'
    variables['inventory_hostname'] = 'test_host'
    variables['ansible_play_hosts'] = 'ansible_play_hosts_value'
    default = 'default_value'
    expected

# Generated at 2022-06-13 14:50:27.571927
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test invalid return value
    x = LookupModule()
    x.run([1, 2, 3], {})

# Generated at 2022-06-13 14:50:32.799548
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module._templar._available_variables = {'test1': 'test1', 'test2': 'test2', 'test3': 'test3', 'test4': 'test4'}
    lookup_module._templar._available_variables['hostvars'] = {'hostname': {'test1': 'test1_hostvars', 'test2': 'test2_hostvars'}}
    result = lookup_module.run(['test1', 'test2', 'test3', 'test4'], {'test1': 'test1', 'test2': 'test2', 'test3': 'test3', 'test4': 'test4'})
    assert result == ['test1', 'test2', 'test3', 'test4']

# Generated at 2022-06-13 14:50:43.216402
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    LM = LookupModule()

    # When
    ret = LM.run(terms=["var3", "var2", "var1"], variables={'var1': 1, 'var2': 2, 'var3': 3})

    # Then
    assert ret == [3, 2, 1]

    # When
    try:
        ret = LM.run(terms=["var1", "var2"], variables={'var2': 2, 'var3': 3})
    except AnsibleUndefinedVariable:
        # Then
        assert True

    # When
    ret = LM.run(terms=["var1", "var2"], variables={'var2': 2, 'var3': 3}, default=4)

    # Then
    assert ret == [4, 2]

# Generated at 2022-06-13 14:51:20.123350
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    assert lookup.run(['var_1'], {'var_1': 'value_1'}) == ['value_1']

    assert lookup.run(['var_1'], {'var_2': 'value_2'}) == []

    assert lookup.run(['var_1', 'var_2'], {'var_1': 'value_1'}) == ['value_1']

    assert lookup.run(['var_1', 'var_2'], {}) == []

    assert lookup.run(['v1', 'v2'], {'v1': 'value_1'}) == ['value_1']


# Generated at 2022-06-13 14:51:30.023341
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play

    # Create mock objects
    loader = DictDataLoader({
        "inventory": "{'_meta': {'hostvars': {'host-1': {'x': 1}}}}",
    })
    inventory = InventoryManager(loader=loader, sources=['inventory'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play = Play().load({}, loader=loader, variable_manager=variable_manager, loader_class=DictDataLoader)



# Generated at 2022-06-13 14:51:36.804445
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup.vars import LookupModule
    from ansible.template import Templar

    terms = 'my_variables'
    variables = {'my_variables': 'lookup_value'}
    kwargs = {}
    obj = LookupModule()
    obj._templar = Templar(loader=None, variables=variables)
    obj.set_options(var_options=variables, direct=kwargs)

    assert obj.run(terms, variables, **kwargs) == ['lookup_value']

# Generated at 2022-06-13 14:51:45.188073
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:51:54.775699
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    class MyLookupModule(LookupModule):
        def _init_(self, basedir=None, runner=None, inject=None, **kwargs):
            self.runner = runner
            self.basedir = basedir
            self.inject = inject
            self.set_options(kwargs)

        def set_options(self, *args, **kwargs):
            self.options = kwargs
        def get_option(self, *args, **kwargs):
            if 'default' in self.options:
                return self.options['default']


        def run(self, *args, **kwargs):
            return LookupModule.run(self, *args, **kwargs)

        def template(self, *args, **kwargs):
            return args[0]

    mylookup = MyLookupModule()

   

# Generated at 2022-06-13 14:52:04.532519
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Unit test for method run of class LookupModule"""
    import pytest
    import ansible.plugins.loader as plugin_loader
    from ansible.template import Templar

    lm = LookupModule()
    lm._templar = Templar(loader=None)

    lm._templar.available_variables = {
        "inventory_hostname": "12",
        "ansible_play_hosts": ["a", "b"],
        "ansible_play_batch": ["a"],
        "ansible_play_hosts_all": ["b", "a"], }

    # First test case
    terms = ["inventory_hostname"]

# Generated at 2022-06-13 14:52:11.866268
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # --------------------------------------------------------------------------------
    # Test with two terms and a default value
    # --------------------------------------------------------------------------------
    # Create the object.
    lm = LookupModule()
    # Create two terms to pass.
    terms = ['ansible_play_hosts', 'ansible_play_batch', 'ansible_play_hosts_all']
    # Create a variable to give.
    myvar = {'ansible_play_hosts': ['localhost'], 'ansible_play_batch': ['localhost1'], 'ansible_play_hosts_all': ['localhost2']}
    # Create the default variable.
    default = 'This is a default value.'
    # Create the return_value.
    return_value = ['localhost', 'localhost1', 'localhost2']
    # Call method run.

# Generated at 2022-06-13 14:52:16.468038
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup import LookupModule
    from ansible.module_utils._text import to_bytes
    lookup = LookupModule()

    def run(p, terms, variables=None, **kwargs):
        lookup.set_loader(p._loader)
        return lookup.run(terms, variables=variables, **kwargs)

    # Generate a fake play context
    fake_play_source = dict(
        name="Ansible Play",
        hosts=['fake_host'],
        roles=[],
        tasks=[
            dict(action=dict(module='ping', args=dict()), register='fake_result'),
        ],
    )

    class FakeVarsModule():
        def get_vars(self, loader, play, host, task):
            return dict()


# Generated at 2022-06-13 14:52:23.124160
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup import LookupBase
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.template import Templar

    def get_basedir(self, vars):
        return "/home/ansible/lookup_plugins"
    LookupBase.get_basedir = get_basedir

    import __main__
    setattr(__main__,'__file__','/tmp/ansible_lookup_plugin.py')
    loader = DataLoader()
    variable_manager = VariableManager()

# Generated at 2022-06-13 14:52:31.803116
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    mod = LookupModule()
    mod._templar = MockTemplar()

    assert mod.run([u'some_var'], variables={u'some_var': u"some_value"}) == [u"some_value"]

    # Test undefined variable
    with pytest.raises(AnsibleUndefinedVariable):
        mod.run([u'some_var'], variables={})

    # Test with default value
    assert mod.run([u'some_var'], variables={}, default="some_default") == [u"some_default"]

    # Test nested variables
    assert mod.run([u'some_nested_var.sub_var'], variables={u'some_nested_var': {'sub_var': 'some_value'}}) == [u"some_value"]

# Generated at 2022-06-13 14:53:45.518500
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import shutil
    import tempfile

    from ansible.plugins.loader import lookup_loader

    def get_loader():
        lookup_loader.set_collection_playbook_paths('')
        return lookup_loader._create_loader(playbook_basedir=None)

    def purge_loader():
        lookup_loader._clear_caches()


# Generated at 2022-06-13 14:53:55.727572
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    myVar_a = {
        'hostvars': {
            'host1': {
                'host1_var': 'host1'
            },
            'host2': {
                'host2_var': 'host2'
            }
        },
        'inventory_hostname': 'host1',
        'inv_var': 'inv_var_value'
    }

    # myVar_a returns expected value
    # test1: term 'inv_var' is defined
    myTerm_a = ['inv_var']
    result_a = LookupModule().run(terms=myTerm_a, variables=myVar_a)
    assert result_a == ['inv_var_value']

    # test2: term 'host1_var' is defined
    myTerm_b = ['host1_var']
    result_

# Generated at 2022-06-13 14:54:03.043162
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule().run(['ansible_play_hosts', 'ansible_play_batch'], dict(ansible_play_hosts=['host1', 'host2'], ansible_play_batch=1)) == [['host1', 'host2'], 1]
    assert LookupModule().run(['ansible_play_hosts', 'ansible_play_batch'], dict(ansible_play_hosts=['host1', 'host2'], ansible_play_batch=1), default=None) == [['host1', 'host2'], 1, None]


# Generated at 2022-06-13 14:54:11.917469
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Build a LookupModule object with ansible_play_hosts, ansible_play_batch and ansible_play_hosts_all as available variables
    # Example: 'ansible_play_hosts': ['10.36.34.62', '10.36.34.61', '10.36.34.60']
    my_vars = {'ansible_play_hosts': ['10.36.34.62', '10.36.34.61', '10.36.34.60'], 'ansible_play_batch': 0, 'ansible_play_hosts_all': ['10.36.34.62', '10.36.34.61', '10.36.34.60']}
    my_module = LookupModule()

# Generated at 2022-06-13 14:54:12.919067
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    assert isinstance(lm, LookupModule)

# Generated at 2022-06-13 14:54:18.790246
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Arrange
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    inventory = InventoryManager(loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    # Act
    # set up test variables

# Generated at 2022-06-13 14:54:25.923238
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_obj = LookupModule()
    # define the variables to be used

# Generated at 2022-06-13 14:54:35.625626
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Unit test for method run of class LookupModule."""
    lm = LookupModule()
    assert(lm.run(['var1', 'var2']) == [None, None])
    assert(lm.run(['var1', 'var2'], variables={'var1': 'value1', 'var2': 'value2'}) == ['value1', 'value2'])
    assert(lm.run(['var2', 'var1'], variables={'var1': 'value1', 'var2': 'value2'}) == ['value2', 'value1'])
    assert(lm.run(['var3', 'var4'], variables={'var1': 'value1', 'var2': 'value2'}) == [None, None])

# Generated at 2022-06-13 14:54:37.754629
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    mylookup = LookupModule()
    assert mylookup.run(['ansible_play_hosts', 'ansible_play_batch', 'ansible_play_hosts_all']) == [
        'localhost', '1', ['localhost']]

# Generated at 2022-06-13 14:54:42.199736
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    module = os.path.join(os.path.dirname(__file__), '../lookup_plugins/vars.py')
    m = None
    exec(compile(open(module, "rb").read(), module, 'exec'), globals(), locals())
    m = locals()['LookupModule']()
    m.run(terms=["ansible_play_batch"])
    assert m.run(terms=["ansible_play_batch"]) == ["10"]
    assert m.run(terms=["ansible_play_hosts"]) == ['["testhost"]']