

# Generated at 2022-06-13 14:45:07.239183
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    items = ["ansible_play_hosts", "ansible_play_batch", "ansible_play_hosts_all"]
    terms = [1, "ansible_play_hosts", -1, "ansible_play_batch", "ansible_play_hosts_all", 1234]

    l = LookupModule()
    assert l.run(terms, **{'ansible_play_hosts': "value", 'ansible_play_batch': "value", 'ansible_play_hosts_all': "value"}) == items


# Generated at 2022-06-13 14:45:17.870037
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.module_utils.six import PY3
    from ansible.module_utils.six.moves import builtins
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.template import Templar
    from ansible.module_utils._text import to_text

    # Get a lookup class instance
    lookup = LookupModule()

    # Create fake templar
    templar = Templar(loader=None, variables=ImmutableDict())

    # Set templar to the fake on
    lookup._templar = templar

    # Required vars for the test
    builtins.__ansible_module_name__ = 'test'

# Generated at 2022-06-13 14:45:29.926016
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    myvars = {
        'inventory_hostname': 'testhost',
        'hostvars': {
            'testhost': {
                'term1': 'value1',
                'term2': 'value2'
            }
        }
    }
    lookup_obj = LookupModule()
    assert lookup_obj.run(terms=['term1', 'term2'], variables=myvars) == ['value1', 'value2']
    assert lookup_obj.run(terms=['term1', 'doesnotexist'], variables=myvars) == ['value1', 'DEFAULT']
    # test exception
    try:
        lookup_obj.run(terms=['term1', 'doesnotexist'], variables=myvars, default=None)
        assert False
    except AnsibleUndefinedVariable:
        pass



# Generated at 2022-06-13 14:45:40.588540
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    class MY_VARS(object):
        def __getitem__(self, item):
            return self.__dict__.__getitem__(item)

        def __setitem__(self, key, value):
            return self.__dict__.__setitem__(key, value)
        hostvars = {'testhost': {}}

    myvars = MY_VARS()
    myvars.testvar = 'testval'
    myvars['hostvars']['testhost']['test'] = 'testval2'
    ret = lookup_module.run(terms=['testvar'], variables=myvars.__dict__)
    assert ret == ['testval']

    ret = loo

# Generated at 2022-06-13 14:45:45.218782
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # import somemodule and set its _shared_loader_obj
    module = 'ansible_collections.testns.testcoll.plugins.lookup.vars_test'
    lookup = LookupModule()
    lookup.set_loader('the_loader') # to prevent a warning in AnsibleRunner
    somemodule = __import__(module, globals(), locals(), ['object'], -1)
    somemodule._shared_loader_obj = None

    # create the testcases for LookupModule.run
    testcases = {}

    testcase_name = 'default_behaviour'
    testcases[testcase_name] = {}
    testcases[testcase_name]['terms'] = ['term_1', 'term_2', 'term_3'] 
    testcases[testcase_name]['variables']

# Generated at 2022-06-13 14:45:52.013724
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def build(term, variables = None, **kwargs):
        return LookupModule().run(terms=term, variables=variables, **kwargs)

    assert build([]) == []
    assert build(['ansible_ssh_host']) == ['127.0.0.1']
    assert build(['ansible_ssh_host', 'ansible_play_hosts_all']) == ['127.0.0.1', ['127.0.0.1']]

    def ommit(variables, term):
        return (LookupModule().run(terms=[term], variables = variables))[0]

    assert ommit({}, 'ansible_ssh_host') == '127.0.0.1'

# Generated at 2022-06-13 14:46:00.363887
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    # Test no variables
    getattr(lookup_module._templar, '_available_variables', {}).clear()
    terms = ['var1', 'var2']
    assert lookup_module.run(terms) == []

    # Test empty variables
    getattr(lookup_module._templar, '_available_variables', {}).clear()
    terms = ['var1', 'var2']
    variables = {'var1': None, 'var2': None}
    assert lookup_module.run(terms, variables) == [None, None]

    # Test variables with values
    terms = ['var1', 'var2']
    variables = {'var1': 'value1', 'var2': 'value2'}

# Generated at 2022-06-13 14:46:08.880160
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    t1 = dict(name=dict(key1='value1', key2='value2'))
    lm = LookupModule()
    result = lm.run(['name'], t1)
    assert result[0] == t1['name']
    result = lm.run(['another_var'], t1)
    assert result == []
    result = lm.run(['another_var'], t1, default='some_default')
    assert result == ['some_default']
    result = lm.run([1], t1)
    assert result == []
    result = lm.run(['another_var'], t1, default='some_default')
    assert result == ['some_default']

# Generated at 2022-06-13 14:46:19.217310
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    result = module.run(terms=['param_1'], variables={'param_1' : 'value_1'})
    assert result == ['value_1']
    result = module.run(terms=['param_1'], variables={'param_1' : 'value_1', 'hostvars' : { 'host_1' : { 'hostparam_1' : 'hostvalue_1'}}})
    assert result == ['value_1']
    result = module.run(terms=['param_1'], variables={'param_1' : 'value_1', 'hostvars' : { 'host_1' : { 'param_1' : 'hostvalue_1'}}})
    assert result == ['value_1']

# Generated at 2022-06-13 14:46:26.529512
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # create variables (ansible_play_hosts) used as terms
    terms = ['ansible_play_hosts', 'ansible_play_batch', 'ansible_play_hosts_all']
    assert terms

    my_lookup_module = LookupModule()


    # create variables (ansible_inventory_hostname) used to create ansible_play_batch
    myvars = {'ansible_inventory_hostname': 'ansible_inventory_hostname'}
    assert myvars

    # call method run
    try:
        lookups = my_lookup_module.run(terms, myvars)
        assert lookups
    except AnsibleUndefinedVariable:
        pass

# Generated at 2022-06-13 14:46:41.223823
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test with all terms defined
    my_terms = [u'variablename', u'myvar']
    my_variables = {u'variablename': u'hello', u'myvar': u'ename'}
    expected = [u'hello']  # All terms are defined, no defaults are used
    actual = LookupModule().run(terms=my_terms, variables=my_variables)
    assert expected == actual

    # Test with one term defined (default='')
    my_terms = [u'variablename', u'myvar']
    my_variables = {u'variablename': u'hello', u'myvar': u'notename'}
    expected = [u'hello', u'']

# Generated at 2022-06-13 14:46:48.248666
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.template.template import Templar

    jinja2_env = Templar._init_global_env()

    templar = Templar(loader=None, variables={})
    templar._available_variables = {
        'ansible_play_hosts': ['one', 'two'],
        'ansible_play_batch': 'ansible_play_batch',
        'ansible_play_hosts_all': 'ansible_play_hosts_all',
        'test': {'test1': 'test1'}
    }


# Generated at 2022-06-13 14:46:59.547245
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module._templar._available_variables = {'hostvars': {'localhost': {'ansible_play_hosts': [u'localhost']}},
                                                   'ansible_play_batch': u'localhost',
                                                   'ansible_play_hosts_all': [u'localhost'],
                                                   'my_var': u'hello'}
    lookup_module._templar.template = lambda x, fail_on_undefined=True: x
    lookup_module.get_option = lambda x: None
    lookup_module.set_options = lambda var_options=None, direct=None: None


# Generated at 2022-06-13 14:47:08.228255
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # LookupModule_run_testCase1()
    # Check the lookup method on top level variable.
    # Return: list of values of variables.
    variables = {'variablename': 'hello', 'myvar': 'ename'}
    lookup = LookupModule()
    lookup.set_options(var_options=variables, direct={})
    terms = ['variablename']
    result = lookup.run(terms, variables, {})
    assert result == ['hello']

    # LookupModule_run_testCase2()
    # Check the lookup method on nested variable.
    # Return: list of values of variables.
    variables = {'variablename': {'sub_var': 12}, 'myvar': 'ename'}
    lookup = LookupModule()

# Generated at 2022-06-13 14:47:16.864462
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # In python 3 str and unicode are the same
    try:
        unicode
    except NameError:
        unicode = str

    # Create LookupModule object and call run method
    look = LookupModule()
    ret = look.run(terms=["hostvars", "inventory_hostname"], variables=None, **{})

    # Check the return value is a list
    assert isinstance(ret, list)

    # Check the return value is a list of unicodes
    assert isinstance(ret[0], unicode)
    assert isinstance(ret[1], unicode)

# Generated at 2022-06-13 14:47:24.918783
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    obj = LookupModule()
    terms = ['key1', 'key2']
    variables = {'hostvars':{'hostname':{'key3':'val3'}}}
    assert obj.run(terms, variables) == ['val1', 'val2']
    variables = {'hostvars':{'hostname':{'key1':'val1'}}}
    assert obj.run(terms, variables) == ['val1']
    assert obj.run(terms, variables, default='val3') == ['val1', 'val3']
    assert obj.run(terms, {}) == []
    assert obj.run(terms, {}, default='val3') == ['val3', 'val3']

# Generated at 2022-06-13 14:47:33.694690
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.parsing.dataloader
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.plugins.loader import lookup_loader

    loader = ansible.parsing.dataloader.DataLoader()
    inventory = InventoryManager(loader=loader, sources=['tests/inventory'])

    host_vars = inventory.get_vars('localhost')
    play_context = dict()
    play_context['inventory_hostname'] = 'localhost'
    play_context['port'] = 2222
    play_context['timeout'] = 5

    # create the variable manager
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    variable_manager

# Generated at 2022-06-13 14:47:43.305513
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # We need to mock find_vars and ansible_play_batch
    from ansible import context
    from ansible.plugins.loader import lookup_loader

    # Set globals in context
    context._init_global_context(play_context=None)

    # Declare our YAML file
    yaml_string = '''
    all_hosts:
      hosts:
        all_hosts:
          ansible_host: 1.2.3.4
    '''

    # Load hosts using the YAML file
    loader = lookup_loader.get('include_vars')
    loader.set_options(play_context=None)
    all_hosts = loader.run([yaml_string], variable_manager=None, loader=None)

    # Set hosts in ansible_play_hosts (global variable)

# Generated at 2022-06-13 14:47:51.393415
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Input parameters
    terms = ['ansible_play_hosts','ansible_play_batch','ansible_play_hosts_all']

# Generated at 2022-06-13 14:47:53.234320
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    plugin = LookupModule()
    assert plugin.run([], {}) == []

# Generated at 2022-06-13 14:48:18.194198
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    #inputs
    terms = [u'variablename', u'ansible_play_hosts', u'ansible_play_batch', u'ansible_play_hosts_all', u'ansible_play_hosts_all']

# Generated at 2022-06-13 14:48:20.049260
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    # TODO: see if adding Mock module for the purpose of testing lookup plugins

# Generated at 2022-06-13 14:48:43.007232
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    default = 'default'

    # No variables
    lookup = LookupModule()
    assert lookup.run(terms=['some_var'], variables={}, default=default) == [default]

    # Not defined variable
    lookup = LookupModule()
    assert lookup.run(terms=['some_var'], variables={'some': 'variables'}, default=default) == [default]

    # Defined variable
    lookup = LookupModule()
    assert lookup.run(terms=['some_var'], variables={'some_var': 'variables'}, default=default) == ['variables']

    # Two terms, one defined, one not
    lookup = LookupModule()

# Generated at 2022-06-13 14:48:53.115935
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ("test_term1", "test_term2")
    variables = {"test_term1": "test1", "test_term2": "test2", "test_term3": "test3", "test_term4": "test4"}

    # Run lookup and assert the result with expected result
    assert lookup.run(terms, variables) == ["test1", "test2"]

    # Run lookup with default value and assert the result with expected result
    # When both terms are not defined in variables
    assert lookup.run(("test_term3", "test_term4"), variables, default="") == ["", ""]
    # When only one term is not defined in variables
    assert lookup.run(("test_term1", "test_term3"), variables, default="") == ["test1", ""]
   

# Generated at 2022-06-13 14:48:53.867136
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 14:49:04.258687
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_member = LookupModule()

    args = []
    kwargs = {
        'default': 'something',
        'errors': 'something',
        'variables': {
            'inventory_hostname': 'something',
            'myvar': 'hello',
            'variablename': {
                'sub_var': 12
            },
            'hostvars': {
                'host1': {
                    'variablename': 12
                }
            }
        },
    }
    assert type(test_member.run(args, **kwargs)) is list
    assert test_member.run(args, **kwargs)[0] == 'something'


# Generated at 2022-06-13 14:49:05.018528
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 14:49:15.340751
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    mod = AnsibleModule(argument_spec={'terms': dict(type='list', elements='str', required=True),
                                       'variables': dict(type='dict', required=False),
                                       'default': dict(type='str', required=False),
                                      })

    # Test with undefined variable
    lookup = LookupModule()
    try:
        assert lookup.run(mod.params['terms'], variables=mod.params['variables']) == [None]
    except AnsibleError as e:
        assert str(e) == 'No variable found with this name: variablename'

    # Test with defined variable
    mod.params['terms'].append('variablename')
    lookup = LookupModule()

# Generated at 2022-06-13 14:49:16.500184
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # NOTHING BREAK
    assert True

# Generated at 2022-06-13 14:49:28.315767
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Given:
    # a dictionary for available variables
    # a list of terms
    # a list of variables
    # a dictionary with options
    from ansible.template import Templar
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.extra_vars = {'file_name': 'test.xml'}
    context = PlayContext()
    context._variable_manager = variable_manager
    templar = Templar(loader=loader, variables=variable_manager._available_variables, shared_loader_object=loader, fail_on_undefined=True, disable_lookups=True)

# Generated at 2022-06-13 14:49:53.458702
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Tests for the constructor of class LookupModule
    # Instantiate an object of class LookupModule
    lookup_module = LookupModule()

    # Tests for the run method of class LookupModule
    # Lookup run method with terms of type list
    result = lookup_module.run(terms=['ansible_play_hosts', 'ansible_play_batch', 'ansible_play_hosts_all'])

    # Lookup run method with terms of type string
    result = lookup_module.run(terms='ansible_play_hosts', variables={'ansible_play_hosts': 'localhost',
                                                                      'ansible_play_batch': 'localhost',
                                                                      'ansible_play_hosts_all': 'localhost'})

    # Lookup run method with terms of type list, variable values preset
   

# Generated at 2022-06-13 14:50:05.275141
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Mocks
    class MyTemplar(object):
        def __init__(self):
            self.available_variables = {}
        def template(self, value, fail_on_undefined):
            return value

    # Test
    lm = LookupModule()
    lm._templar = MyTemplar()

    # 1. case: term is a list of strings
    terms = [
        'hostvars',
        'inventory_hostname',
        'ansible_play_hosts',
        'ansible_play_batch',
        'ansible_play_hosts_all'
    ]

# Generated at 2022-06-13 14:50:12.926588
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from .lookup_plugins.vars import LookupModule

    # Simple test case.
    look = LookupModule()
    ret = look.run([''])
    assert ret == [], 'run should return empty list'

    # Test case with terms.
    look = LookupModule()
    ret = look.run(['var1', 'var2'], variables={'var1': 'hello', 'var2': 'world', })
    assert ret == ['hello', 'world'], 'run should return list of world'

    # Test case with terms and default.
    look = LookupModule()
    ret = look.run(['var1', 'var2'], variables={'var1': 'hello', 'var2': 'world', }, default='bar')
    assert ret == ['hello', 'world'], 'run should return list of world'

# Generated at 2022-06-13 14:50:23.239683
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()

    # Testing with variables that should exist
    module._templar = FakeTemplar()
    module._templar._available_variables = { "test_variable": 123, "hostvars": {"host1": {"host_variable": 456}}}

    results = module.run(["test_variable", "host_variable"], variables=None, fail_on_undefined=False, default="nope")
    assert results == [123, 456]

    # Testing with variables that don't exist
    module._templar = FakeTemplar()
    module._templar._available_variables = { "test_variable": None, "hostvars": {"host1": {"host_variable": None}}}


# Generated at 2022-06-13 14:50:26.470347
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    mod = LookupModule()
    mod.set_options({})
    res = mod.run(["one","two"], variables={'one':'1', 'two':'2'})
    assert res == ['1', '2']



# Generated at 2022-06-13 14:50:35.749292
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # setup
    terms = ['ansible_play_hosts', 'ansible_play_batch', 'ansible_play_hosts_all']
    variables = {
        'ansible_play_hosts': ['host1', 'host2'],
        'ansible_play_batch': 'host3',
        'ansible_play_hosts_all': ['host1', 'host2', 'host3']
    }
    # execute
    actual = LookupModule().run(terms, variables)
    # verify
    expected = [
        ['host1', 'host2'],
        'host3',
        ['host1', 'host2', 'host3']
    ]
    assert actual == expected

    # verify

# Generated at 2022-06-13 14:50:45.038530
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    lookup.set_options(var_options=None, direct=dict())
    assert [{'foo': 'bar'}] == lookup.run(terms=['foo'], variables=dict(foo={'foo': 'bar'}))
    assert [{'foo': 'bar'}] == lookup.run(terms=['foo'], variables={'foo': {'foo': 'bar'}})


# Generated at 2022-06-13 14:50:49.427373
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    terms = [ "test_value", "test_value2" ]
    myvars = { "test_value": "test", "test_value2": "test2" }
    results = module.run(terms, variables=myvars)
    assert results == [ "test", "test2" ]

# Test with variables not found, but default value defined

# Generated at 2022-06-13 14:50:56.023667
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    lookup._templar._available_variables = dict(c=1)
    assert lookup.run('a', dict(a='c')) == ['c']
    assert lookup.run(['a'], dict(a='c')) == ['c']
    assert lookup.run(['a', 'b'], dict(a='c')) == ['c']
    assert lookup.run(['a', 'b'], dict(a='c', b=None)) == ['c', 'None']
    assert lookup.run(['a', 'b'], dict(a='c', b=1)) == ['c', '1']



# Generated at 2022-06-13 14:51:00.287884
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l._templar.set_available_variables({'inventory_hostname': 'test'})
    l._templar.set_available_variables({'hostvars': {'test': {'ansible_play_hosts': ['1']}}})
    assert l.run(['ansible_play_hosts'], kwargs={}) == [['1']]

# Generated at 2022-06-13 14:51:31.246010
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    ret = list()
    ret.append("hello")
    assert(len(ret) == 1)
    ret.append("world")
    assert(len(ret) == 2)
    ret.append("ciao")
    assert(len(ret) == 3)

# Generated at 2022-06-13 14:51:37.251145
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['one', 'two', 'three']
    variables = {'one': 1, 'two': 2, 'hostvars': {'host': {'three': 3}}}
    lookup_module = LookupModule()
    lookup_module.set_options(var_options=variables, direct={})
    lookup_module._templar._available_variables = variables
    result = lookup_module.run(terms, variables)
    assert result == [1, 2, 3]

# Generated at 2022-06-13 14:51:44.047042
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create mock objects
    lookup = LookupModule()
    lookup._templar = MagicMock()
    lookup._templar._available_variables = {'hostvars': { 'localhost': {'localhost_var': 1,
                                                                        'localhost_var2': 2,
                                                                        'localhost_var3': 3,
                                                                        'inventory_hostname': 'localhost'}},
                     'localhost_var': 1,
                     'localhost_var2': 2,
                     'localhost_var3': 3,
                     'inventory_hostname': 'localhost'}
    lookup.set_options = MagicMock()
    lookup.get_option = MagicMock(return_value=None)
    lookup.get_option.__getitem__ = MagicMock(return_value=None)

    # Perform test
   

# Generated at 2022-06-13 14:51:44.935023
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    LookupModule().run()

# Generated at 2022-06-13 14:51:48.066729
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    print(LookupModule().run(terms=["test", "test2"], variables={'test': 'test1', 'test2': 'test2'}))
    print(LookupModule().run(terms=["test"], variables=None))

# Generated at 2022-06-13 14:51:57.281018
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # input
    terms = ['ansible_play_hosts', 'ansible_play_batch', 'ansible_play_hosts_all']
    variables = {
        "ansible_play_hosts": [1, 2, 3],
        "ansible_play_batch": [4, 5, 6],
        "ansible_play_hosts_all": [7, 8, 9]
    }
    # expected output
    output = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # test
    test = LookupModule()
    result = test.run(terms, variables=variables)
    assert result == output

    # input
    terms = ['ansible_play_hosts', 'ansible_play_batch', 'ansible_play_hosts_all']
   

# Generated at 2022-06-13 14:52:06.189106
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.parsing.yaml.objects
    import ansible.plugins.lookup.vars
    from ansible.template import Templar

    mylookup = ansible.plugins.lookup.vars.LookupModule()

    mylookup.set_options(direct={})


# Generated at 2022-06-13 14:52:15.086603
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:52:23.930462
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import PY3

    #### Test for a single undefined variable
    # test with unavailable variable
    terms = ['test']
    variables = {'test': []}

    ret = LookupModule._run_terms(terms, variables)
    assert ret == []

    # test with available variable
    terms = ['test']
    variables = {'test': [1]}

    ret = LookupModule._run_terms(terms, variables)
    assert ret == [1]

    #### Test for multiple undefined variables
    # When all variables are available
    terms = ['test', 'test2']
    variables = {'test': [1], 'test2': [2]}

    ret = LookupModule._run_terms(terms, variables)
    assert ret == [1, 2]

    # When not all variables are

# Generated at 2022-06-13 14:52:32.384347
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    my_object = LookupModule()
    my_variables = {
        'first_var': 3,
        'second_var': 2,
        'third_var': 1
    }
    my_terms = ['first_var', 'second_var', 'third_var']
    expected_value = [3, 2, 1]
    result_value = my_object.run(my_terms, my_variables)
    assert result_value == expected_value

    # Method run should return a list even if there is only one element
    my_terms = ['first_var']
    expected_value = [3]
    result_value = my_object.run(my_terms, my_variables)
    assert result_value == expected_value

    # Method run should raise an AnsibleError if the terms are not a string
    my

# Generated at 2022-06-13 14:53:40.374755
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()
    terms = ['hostvars']
    variables = {
            'inventory_hostname': 'server1',
            'hostvars': {
                'server1': {
                    'ansible_os_family': 'RedHat'
                    }
                }
            }
    result = lookup_plugin.run(terms, variables)
    assert result == [variables['hostvars']['server1']]

# Generated at 2022-06-13 14:53:41.092974
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: Create valid unit test
    pass

# Generated at 2022-06-13 14:53:47.105576
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.template import Templar

    mylookup = LookupModule()
    mylookup._templar = Templar()

    # Setup fake variables
    mylookup._templar.available_variables = {'my_var': 'my_value', 'my_var2': 'my_value2'}
    mylookup._templar.set_available_variables({'my_var': 'my_value', 'my_var2': 'my_value2'})

    # Test with a single term
    terms = ['my_var']
    myvars = mylookup._templar.available_variables
    terms = mylookup.run(terms, variables=myvars)
    assert terms == ['my_value']

    # Test with multiple terms

# Generated at 2022-06-13 14:53:57.167680
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Check if undefine variable is raise error
    # Check if undefine variable is raise error
    # Check if undefine variable is raise error
    undefine_variable = 'undefine'
    test_terms = [undefine_variable]
    try:
        look = LookupModule()
        look.run(terms=test_terms)
    except Exception as e:
        assert(isinstance(e, AnsibleError))

    # Check if empty variable is raise error
    # Check if empty variable is raise error
    # Check if empty variable is raise error
    empty_variable = ''
    test_terms = [empty_variable]
    try:
        look = LookupModule()
        look.run(terms=test_terms)
    except Exception as e:
        assert(isinstance(e, AnsibleError))

   

# Generated at 2022-06-13 14:54:06.150357
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import PY3

    class FakeVars:
        ansible_facts = {
            'ansible_play_hosts': [],
            'ansible_play_batch': [],
            'ansible_play_hosts_all': [],
            'ansible_play_batch': [],
            'ansible_play_batch_count': 0,
            'ansible_play_hosts_file': '',
            'ansible_play_name': '',
        }

        def update(self, **kwargs):
            pass

        def template(self, value, fail_on_undefined=False):
            return value

    class FakeTemplar:
        _available_variables = FakeVars()

        def __init__(self, available_variables):
            pass



# Generated at 2022-06-13 14:54:09.959881
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    m = LookupModule()
    assert m.run(terms=['myvar']) == [None]
    assert m.run(terms=['myvar'], variables={'myvar': True}) == [True]
    assert m.run(terms=['myvar'], variables={'myvar': {'sub_var': 12}}) == [{'sub_var': 12}]

# Generated at 2022-06-13 14:54:16.758338
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test simple usecase with existing variable
    test_object = LookupModule()
    test_object._templar = DummyTemplar()
    test_object._templar._available_variables = {'name1': 'value1', 'name2': 'value2', 'hostvars': {'hostname1': {'name3': 'value3', 'name4': 'value4'}, 'hostname2': {'name5': 'value5', 'name6': 'value6'}}}
    result = test_object.run(terms=['name1', 'name2'], variables=None)
    assert result == ['value1', 'value2']

    # Test lookup in hostvars
    result = test_object.run(terms=['name3', 'name4'], variables=None)

# Generated at 2022-06-13 14:54:23.328938
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    LookupModule_class = LookupModule()
    terms = ['user']
    kwargs = {'default': 'ansible'}
    variables = {'user': 'john', 'hostvars': {'localhost': {'user': 'admin'}}}
    assert LookupModule_class.run(terms, variables, **kwargs) == ['john']
    variables = {'hostvars': {'localhost': {'user': 'admin'}}}
    assert LookupModule_class.run(terms, variables, **kwargs) == ['admin']
    assert LookupModule_class.run(terms, **kwargs) == ['ansible']

# Generated at 2022-06-13 14:54:23.968534
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 14:54:32.405719
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_term = "random_variable"

    # Set parameters for test
    params = dict(
        ansible_play_hosts = [ "10.0.0.1", "10.0.0.2" ],
        ansible_play_batch = [ dict(inventory_hostname = "10.0.0.1"), dict(inventory_hostname = "10.0.0.2") ]
    )

    # create new LookupModule object
    lm = LookupModule()

    # call run method of LookupModule class with input parameters
    result = lm.run([ test_term ], params)

    # assert the result
    assert result == [ params[test_term] ]

