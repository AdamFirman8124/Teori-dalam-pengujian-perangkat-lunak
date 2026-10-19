

# Generated at 2022-06-13 14:45:09.931280
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Test if a variable is found in the inventory_hostname variable, then in the hostvars variable, then undefined variable error is raised"""
    variable1 = {'var1': 'testvar1', 'var2': 'testvar2'}
    variable2 = {'var3': {'test': 'testvar3'}}
    variable3 = {'inv_host': 'test'}
    variable4 = {'hostvars': {'test': {'var4': 'testvar4'}}}

    terms = ['var1','var3']
    default = None
    attributes = {'_templar': {'_available_variables':{'var1':'testvar1', 'var2':'testvar2', 'var3':{'test':'testvar3'}}}}

# Generated at 2022-06-13 14:45:16.009266
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_lookup_plugin = LookupModule()

    # Test with an undefined variable
    terms = ['uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu']
    res = test_lookup_plugin.run(terms, variables={'foo': 'bar'})
    assert(res == [None])

    # Test with a defined variable
    terms = ['foo']
    res = test_lookup_plugin.run(terms, variables={'foo': 'bar'})
    assert(res == ['bar'])

    # Test with a set default value

# Generated at 2022-06-13 14:45:23.963664
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import PY3
    from ansible.parsing.splitter import parse_kv
    from ansible.plugins.loader import lookup_loader
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    if PY3:
        unicode = str

    test_vars_dict = dict(
        name='testvar',
        default='testdefault',
        test_dict_nested=[
            dict(a=1, b=2),
            dict(c=3, d=4),
        ],
        test_dict={'a': 1, 'b': 2},
        test_list=["test_list_a", "test_list_b"],
    )


# Generated at 2022-06-13 14:45:33.982929
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    #lookup module vars test case
    import unittest
    import copy
    class LookupModuleTest(unittest.TestCase):
        lookup_module = None

        def setUp(self):
            self.lookup_module = LookupModule()

        def test_LookupModule_run(self):
            # load initial vars
            self.lookup_module._templar.available_variables = copy.deepcopy(self._initial_vars)
            # test case
            terms = [
                'ansible_play_hosts',
                'ansible_play_batch',
                'ansible_play_hosts_all',
                'hostvars.host1.host_var1'
            ]
            # expected result

# Generated at 2022-06-13 14:45:37.529700
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['a', 'b']
    variables = {
        'a': 1,
    }
    default = None

    result = LookupModule({}).run(terms, variables, default=default)

    assert result == [1, None]

# Generated at 2022-06-13 14:45:46.724658
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest

    mock_inventory = {'nested_variable': {'sub': '12'}, 'inventory_hostname': 'test_hostname'}

    my_lookup = LookupModule()

    my_lookup._templar.available_variables = mock_inventory

    myvars = getattr(my_lookup._templar, '_available_variables', {})

    my_lookup.set_options(var_options=mock_inventory, direct={})

    default = my_lookup.get_option('default')

    my_lookup._templar.template = lambda x, y=None: x

    # NOTE: Here we can simply test the method run of class LookupModule,
    # but we need to mock the method fail_on_undefined of class Templar
    # which is in the

# Generated at 2022-06-13 14:45:52.880526
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Instantiate test class and test variables
    lookup_module = LookupModule()

    # Test variables
    terms = ['hello', 'world']
    myvars = {'hello': 'Bonjour', 'world': 'le monde'}
    default = 'nothing'
    # Run method, then test
    result = lookup_module.run(terms, variables=myvars, default=default)
    assert result == ['Bonjour', 'le monde']

# Generated at 2022-06-13 14:46:00.905921
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    lookup_dict = {
        'hostvars': {
            'hostname': {
                'ansible_play_hosts': 'a test string',
                'ansible_play_batch': 12
            }
        },
        'ansible_play_hosts_all': 'another test'
    }
    expected_result = [['a test string', 12, 'another test']]
    class Options():
        # Mock the vars and default options to pass in the vars dictionary
        var_options = lookup_dict
        default = None
    module_options = Options()
    lookup_module = LookupModule()
    lookup_module.set_options(var_options=lookup_dict, direct=None, **module_options)
    lookup_module._templar._available_variables = lookup_dict


# Generated at 2022-06-13 14:46:05.475316
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    myLookupModule = LookupModule()
    myLookupModule._templar = {}
    myLookupModule._templar._available_variables = {'ansible_play_hosts': 'localhost'}
    assert myLookupModule.run(['ansible_play_hosts']) == ['localhost']



# Generated at 2022-06-13 14:46:14.964065
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:46:26.384205
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost,', 'otherhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    assert LookupModule(loader=loader, variable_manager=variable_manager).run(['hostname']) == ['localhost']

# Generated at 2022-06-13 14:46:28.564636
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    #pylint: disable=no-self-use
    lookup_module = LookupModule()
    result = lookup_module.run(["var1", "var2"])
    assert result == []


# Generated at 2022-06-13 14:46:38.062347
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['test/unit/ansible/inventory/hosts'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

# Generated at 2022-06-13 14:46:47.516352
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # the first 'module_utils' imports create an empty lookup module
    # the second 'module_utils' import creates a templar with a given set of options
    # (for the example, we set two variables: 'ansible_play_hosts' and 'ansible_play_batch')
    from ansible.plugins.lookup.vars import LookupModule
    from ansible.module_utils.basic import AnsibleModule
    from ansible.template import Templar

    terms = ['ansible_play_hosts', 'ansible_play_batch']
    default = 'default'
    variables = {'ansible_play_hosts': 'host1', 'ansible_play_batch': '1'}
    # TODO: fix to support Ansible 2.6
    mylookup = LookupModule()
    mylookup.set_

# Generated at 2022-06-13 14:46:48.669470
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    raise NotImplementedError("TODO")

# Generated at 2022-06-13 14:47:00.157873
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    terms = ['ansible', 'intvar', 'ansible.intvar']
    myvars = {
        'ansible': 'is_awesome',
        'ansible_play_hosts': 'localhost',
        'ansible_play_batch': 'localhost',
        'ansible_play_hosts_all': 'localhost',
        'inventory_hostname': 'localhost',
        'intvar': 42,
        'ansible.intvar': 42,
        'ansible.subvar': {'subsub': 'value'}
    }
    variable_manager = VariableManager()
    variable_manager._options_vars = ['vars', 'hostvars']
   

# Generated at 2022-06-13 14:47:08.663609
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test1: terms contain two string, variables contain hostvars, inventory_hostname and two variables
    # Expect: return two variable value
    lookup = LookupModule({}, {})

    variables = {}
    variables['hostvars'] = {'host_1': {'var_1': 'value1', 'var_2': 'value2'}, 'host_2': {'var_1': 'value3', 'var_2': 'value4'}}
    variables['inventory_hostname'] = 'host_1'
    variables['var_3'] = 'value5'
    variables['var_4'] = 'value6'

    terms = ['var_1', 'var_3']

    ret = lookup.run(terms, variables)
    assert ret == ['value1', 'value5']

    # Test2: terms contain two string,

# Generated at 2022-06-13 14:47:15.663734
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    value = lookup_module.run(["foo", "bar"], variables={
        "foo": "foo_value",
        "bar": "bar_value",
        "hostvars": {
            "host": {
                "baz": "baz_value"
            }
        },
        "inventory_hostname": "host"
    })
    assert value == ["foo_value", "bar_value"]

# Generated at 2022-06-13 14:47:16.244134
# Unit test for method run of class LookupModule
def test_LookupModule_run():
        assert False

# Generated at 2022-06-13 14:47:25.292859
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    t = LookupModule()
    terms = ['ansible_play_hosts', 'ansible_play_batch', 'ansible_play_hosts_all', 'ansible_play_hosts_count']
    variables = {'ansible_play_hosts': 'hosts', 'ansible_play_batch': 'batch', 'ansible_play_hosts_all': 'hosts_all', 'ansible_play_hosts_count': 'hosts_count'}
    assert t.run(terms, variables) == ['hosts', 'batch', 'hosts_all', 'hosts_count']
    assert t.run(['ansible_play_hosts_count'], variables) == ['hosts_count']
    # assert that default='' will will return an empty string if the variable is undefined

# Generated at 2022-06-13 14:47:42.263247
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Since the method run depends on some methods of LookupBase,
    # test methods of LookupBase class first.
    # Test cases for LookupBase class are defined in:
    # .../test/units/plugins/lookup/TestLookupBase.py
    test_LookupModule_run.__dict__['testcases_LookupBase_set_options'] = \
        test_LookupBase_set_options.__dict__['testcases_LookupBase_set_options']
    test_LookupModule_run.__dict__['testcases_LookupBase_get_option'] = \
        test_LookupBase_get_option.__dict__['testcases_LookupBase_get_option']
    test_LookupModule_run.__dict__['testcases_LookupBase_get_options'] = \
        test

# Generated at 2022-06-13 14:47:48.736621
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    import pytest
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    variables = VariableManager()
    terms = ['a', 'b']
    variables.set_variable('a', '1')
    variables.set_variable('b', '2')

    lookup = LookupModule()
    res = lookup.run(terms, variables, loader=loader)

    assert res == ['1', '2']
    assert res[0] == '1'
    assert res[1] == '2'

# Generated at 2022-06-13 14:47:49.261202
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 14:48:01.258474
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # NOTE: The following test uses mocks (unittest.mock) to replace the ansible.plugins.lookup.LookupBase class
    # and Ansible's templating engine. Testing this class is complicated and needs this approach.

    # Create the class we're testing
    lookup_plugin = LookupModule()

    # Mock the templating engine
    from ansible.plugins.lookup.vars import MyTemplar
    lookup_plugin._templar = MyTemplar()

    # Set some variables and the inventory host, so that we can test the hostvars section in the vars plugin

# Generated at 2022-06-13 14:48:08.238136
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_obj = LookupModule()
    result = lookup_obj.run(['non_existing_var'], {'var1': ['val1', 'val2'], 'var2': 'val3'}, default='value')
    assert result == ['value']

    result = lookup_obj.run(['var1', 'var2'], {'var1': ['val1', 'val2'], 'var2': 'val3'}, default='value')
    assert result == ['val1', 'val2', 'val3']

# Generated at 2022-06-13 14:48:15.194030
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # examples to test
    lookup_examples = {"example1":  
                        {"terms":["ansible_play_hosts","ansible_play_batch","ansible_play_hosts_all"]}
                     }

    # test
    lm = LookupModule()
    #lm.run(terms=lookup_examples["example1"]["terms"])


if __name__ == "__main__":
    test_LookupModule_run()

# Generated at 2022-06-13 14:48:22.535988
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup.vars import LookupModule

    # No value found for myvar, expect AnsibleError
    term = 'myvar'
    variables = {
        'myvar': None
    }
    with pytest.raises(AnsibleError):
        LookupModule().run(terms=[term], variables=variables)

    # Value found for myvar, expect None (because no default is specified)
    term = 'myvar'
    variables = {
        'myvar': None
    }
    assert LookupModule().run(terms=[term], variables=variables, default=None) == [None]

    # Value found for myvar, expect default value
    term = 'myvar'
    variables = {
        'myvar': None
    }

# Generated at 2022-06-13 14:48:41.168034
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l._templar = {'_available_variables': { 'variable_one': 'hello', 'variable_two': 'world'} }
    assert l.run(['variable_one']) == ['hello']
    assert l.run(['variable_two']) == ['world']
    assert l.run(['variable_one', 'variable_two']) == ['hello', 'world']
    assert l.run(['variable_one', 'variable_two'], default='default') == ['hello', 'world']
    assert l.run(['variable_one', 'undefined'], default='default') == ['hello', 'default']

# Generated at 2022-06-13 14:48:42.078009
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: Write unit tests
    pass

# Generated at 2022-06-13 14:48:51.764901
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class LookupModuleMock(LookupBase):
        _templar = dict(
            _available_variables = dict(
                variablename = 'hello',
                hostvars = dict(
                    hostname = dict(
                        variablename = 'hello'
                    )
                )
            )
        )

    lookup_plugin = LookupModuleMock()

    # simple
    results = lookup_plugin.run(terms=['variablename'])
    assert results == ['hello'], 'unable to find simple variable for lookup plugin'

    # default
    results = lookup_plugin.run(terms=['variableunknownname'], default='defaulttest')
    assert results == ['defaulttest'], 'unable to find default variable for lookup plugin'

    # non existent

# Generated at 2022-06-13 14:49:15.194932
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.plugins.loader
    import ansible.plugins.lookup.vars
    defaults = {
        'inventory_hostname': 'localhost',
        'groups': {
            'all': ['localhost'],
            'webservers': ['localhost'],
            'dbservers': ['localhost'],
            'ungrouped': []
            },
        'hostvars': {
            'localhost': {
                'hostvars_data': 'hostvars_value'
                }
            },
        'hostvars_data': 'vars_value',
        'myvar': 'myvarvalue'
        }

    # test with simple inputs

# Generated at 2022-06-13 14:49:27.148257
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Method run of class LookupModule
    """
    test_obj = LookupModule()

    myvars = {'inventory_hostname': 'localhost',
              'hostvars': {'localhost': {'test_var': 'hello world'}}}
    test_obj._templar._available_variables = myvars

    test_obj.set_options(var_options=None, direct=None)
    test_obj.get_option('default')

    test_obj.set_options(var_options=None, direct=None)
    test_obj.get_option('default')


# Generated at 2022-06-13 14:49:37.899208
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    ml = LookupModule()
    terms = ['test1']
    variables = {'test1':'var1'}
    assert ml.run(terms) == ['var1']
    assert ml.run(terms, variables=variables) == ['var1']
    terms = ['test1', 'test2']
    variables = {'test1':'var1', 'test2':'var2'}
    assert ml.run(terms) == ['var1', 'var2']
    assert ml.run(terms, variables=variables) == ['var1', 'var2']

    terms = ['test1', 'test2']
    variables = {'test1':'var1'}
    try:
        assert ml.run(terms) == ['var1', 'var2']
    except AnsibleUndefinedVariable:
        pass

   

# Generated at 2022-06-13 14:49:43.865778
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create an instance of LookupModule
    l = LookupModule()

    # Create a variable of type dict
    mydict = {'ansible_play_hosts': ['192.168.50.41', '192.168.50.42'], 'ansible_play_batch': ['192.168.50.41'], 'ansible_play_hosts_all': ['192.168.50.41', '192.168.50.42']}

    # Call method run of class LookupModule with mydict as variables parameter
    result = l.run(['ansible_play_hosts', 'ansible_play_batch', 'ansible_play_hosts_all'], mydict)

    # Check if the returned value is correct

# Generated at 2022-06-13 14:49:55.330182
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module._templar = MagicMock()
    lookup_module._templar._available_variables = {
        'hostvars': {
            'host1': {'myvar1': 'value1', 'myvar2': 'value2'},
            'host2': {'myvar1': 'value3', 'myvar2': 'value4'},
            'myvar5': 'top_value',
            'myvar6': {'key1': 'value6', 'key2': 'value6'}
        }
    }
    lookup_module._templar.template = MagicMock(side_effect=['value1', 'value5'])

    assert lookup_module.run(['myvar1'], None) == ['value1']
    assert lookup_module

# Generated at 2022-06-13 14:50:06.651594
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    term = 'ansible_play_hosts'

    LookupModule_object = LookupModule()

    # Test with missing term
    term = 'ansible_play_hosts_all'
    expected_result = ['localhost']
    result = LookupModule_object.run([term])
    assert result == expected_result

    # Test with given term
    term = 'ansible_play_hosts'
    expected_result = ['localhost']
    result = LookupModule_object.run([term])
    assert result == expected_result

    # Test with nested term
    term = 'ansible_play_hosts.0'
    expected_result = 'localhost'
    result = LookupModule_object.run([term])
    assert result[0] == expected_result

    # Test with multiple terms

# Generated at 2022-06-13 14:50:17.307467
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a template object i.e. AnsibleTemplate object
    template_obj = ansible.template.AnsibleTemplate(
        dictionary={
            'hostvars': {
                'host1': {
                    'host1variable': 'host1variablevalue'
                }
            }
        },
    )
    # Create an LookupModule object
    lookup_plugin = ansible.plugins.lookup.vars.LookupModule()
    # Create a variable manager object i.e AnsibleVariableManager object
    variable_manager = ansible.vars.manager.VariableManager()
    variable_manager._extra_vars = {
        'host1variable': 'host1variablevalue',
        'host2variable': 'host2variablevalue'
    }

# Generated at 2022-06-13 14:50:25.587247
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ['hello']
    source = '''
    {
        "hello": "world",
        "ansible_play_hosts": [ "master" ],
        "ansible_play_batch": [],
        "ansible_play_hosts_all": "foo"
    }
    '''
    variables = {}
    # use _load_data to process source
    lookup._load_data(source)
    ret = lookup.run(terms, vars=variables)
    assert(ret == ['world'])

    terms = ['ansible_play_hosts', 'ansible_play_batch', 'ansible_play_hosts_all']
    ret = lookup.run(terms, vars=variables)
    assert(ret == [['master'], [], 'foo'])

# Generated at 2022-06-13 14:50:35.190900
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:50:39.833733
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['test1', 'test3', 'test5']
    variables = {'test1': 1, 'test2': 2, 'test3': 3, 'test4': 4, 'test5': 5, 'test6': 6}
    f = LookupModule()
    assert [1, 3, 5] == f.run(terms, variables)

# Generated at 2022-06-13 14:51:14.427191
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # variable = hostvars[inventory_hostname]
    # variable = myvars[term]

    import sys
    import json
    import os
    import tempfile
    import shutil
    import stat

    # we will create two temp dirs
    # our current working dir
    # and a child dir of that
    tmp_cwd = tempfile.mkdtemp()
    tmp_subdir = tempfile.mkdtemp(dir=tmp_cwd)

    os.chdir(tmp_subdir)

    # lets create some files to play with
    test_vars = tempfile.NamedTemporaryFile(mode='w+t', suffix='vars', prefix='test', delete=False)

# Generated at 2022-06-13 14:51:21.263593
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup_plugin = LookupModule()

    # test invalid term
    term = {}
    assert lookup_plugin.run(terms=[term], fail_on_undefined=True) is None

    # test undefined term
    myvars = {
        'inventory_hostname': 'localhost',
        'hostvars': {
            'localhost': {
                'test1': 'test1',
                'test2': [1, 2, 3],
            }
        }
    }
    terms = [
        'test1',
        'test2',
        'test3',
    ]
    assert lookup_plugin.run(terms=terms, variables=myvars, fail_on_undefined=True) == ['test1', [1, 2, 3], None]

    # test defined term

# Generated at 2022-06-13 14:51:28.728569
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # test string variables
    terms = ['ansible_play_hosts', 'ansible_play_batch', 'ansible_play_hosts_all']
    variables = {'ansible_play_hosts': ['host1', 'host2'], 'ansible_play_batch': ['host1', 'host2'],
                 'ansible_play_hosts_all': ['host1', 'host2'], 'inventory_hostname': 'host1'}
    assert LookupModule().run(terms=terms, variables=variables) == [['host1', 'host2'], ['host1', 'host2'], ['host1', 'host2']]

    # test string and dict variables
    terms = ['ansible_play_hosts', 'ansible_play_batch', 'ansible_play_hosts_all']
   

# Generated at 2022-06-13 14:51:34.259382
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import unittest
    class TestLookupModule_run(unittest.TestCase):

        def test_all_except_inventory_error(self):
            lookup_module = LookupModule()
            lookup_module._templar = AnsibleUndefinedVariable()
            lookup_module._templar.available_variables = {}
            lookup_module._templar._available_variables = {}
            lookup_module.set_options(var_options={}, direct={})
            lookup_module.get_option = lambda x: None
            with self.assertRaises(AnsibleUndefinedVariable):
                lookup_module.run(['pouet', 'pouet_pouet'], {'inventory_hostname': 'localhost'})

        def test_inventory_error(self):
            lookup_module = LookupModule()


# Generated at 2022-06-13 14:51:43.237727
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.module_utils
    module_args = {
        'terms': ['foo'],
        'default': 'Default',
    }
    terms = ['foo']
    fake_loader = ansible.module_utils.get_module_loader()
    fake_module = ansible.module_utils.basic.AnsibleModule(argument_spec={}, module_args=module_args, loader=fake_loader)
    module = LookupModule()

    def fake_get_option(self, option):
        return module_args[option]

    def fake_set_options(self, var_options, direct):
        pass

    # Testing when foo is defined
    module._templar = ansible.parsing.dataloader.DataLoader()

# Generated at 2022-06-13 14:51:49.595295
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    # There are two ways to use AnsibleModule, both of which yield the same result
    # module_args = { '_terms' : "ansible_playbook_python" , '_variables' : None }
    # module_args = { '_terms' : "ansible_playbook_python" }

    return_value = LookupModule().run( ["ansible_playbook_python"], { 'hostvars' : {'host_name' : { 'ansible_playbook_python' : "/tmp/python" } }, 'inventory_hostname' : "host_name" } )

    assert return_value[0] == "/tmp/python"

# Generated at 2022-06-13 14:51:58.552662
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:52:06.044039
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible.errors import AnsibleUndefinedVariable
    lu = LookupModule()
    terms = ["ansible_play_hosts", "ansible_play_batch", "ansible_play_hosts_all"]
    variables = {"ansible_play_hosts": "value1", "ansible_play_batch": "value2", "ansible_play_hosts_all": "value3"}
    result = lu.run(terms, variables, direct={})
    assert result == ["value1", "value2", "value3"]
    terms = ["ansible_play_hosts", "ansible_play_batch", "ansible_play_hosts_all", "ansible_play_non_existing"]
    result = lu.run(terms, variables, direct={})

# Generated at 2022-06-13 14:52:15.010630
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from units.mock.loader import DictDataLoader
    from ansible.template import Templar

    # Prepare test environment for test LookupModule.run()
    # To test the method, we have to setup some environment
    # for the lookup modules. So the lookup can work normally.
    #
    # Step 1: Create a dict type ansible variable
    # To make the lookup module can be tested, we need to
    # create a dict type variable, so the lookup module
    # can find variable from this dict.
    test_var_dict = {'a' : '1', 'b' : '2'}

    # Step 2: Setup test environment for _templar.
    # _templar is a member of LookupBase class, this
    # member is used to template a string. For lookup
    # module, we will use _templ

# Generated at 2022-06-13 14:52:18.213256
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_LookupModule = LookupModule()
    # test_LookupModule.run(terms, variables=None, **kwargs)
    pass


# Generated at 2022-06-13 14:53:25.265061
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    my_vars = dict(inventory_hostname='localhost', ansible_play_hosts=['192.168.1.1', '192.168.1.2'],
        ansible_play_batch=['192.168.1.3', '192.168.1.4'], ansible_play_hosts_all=['192.168.1.5', '192.168.1.6'])
    my_terms = ['ansible_play_hosts', 'ansible_play_batch', 'ansible_play_hosts_all']
    lm = LookupModule()
    result = lm.run(my_terms, my_vars)

# Generated at 2022-06-13 14:53:36.322516
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Set up test data
    terms = ['ansible_play_hosts', 'ansible_play_batch', 'ansible_play_hosts_all']
    variables = {'ansible_play_hosts':'foo', 'ansible_play_batch':'bar', 'ansible_play_hosts_all':'zap'}

    # Create the LookupModule
    v = LookupModule()

    # Create the mocked templar
    templar_mock = v._templar = MagicMock()
    templar_mock.available_variables = variables

    # run the code
    ret = v.run(terms, variables=variables)

    # Confirm the results
    assert ret == ['foo', 'bar', 'zap']



# Generated at 2022-06-13 14:53:40.052963
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()

    l._templar = DummyTemplar()
    l._templar._available_variables = {
        "hostvars": {
            "host": {
                "variablename": "1234"
            }
        }
    }
    assert l.run(['variablename']) == ['1234']
    assert l.run(['variablename'], variables={"variablename": "5678"}) == ['5678']

    # 'default' option test
    assert l.run(['variablename1'], variables={"variablename": "5678"}, default='default') == ['default']
    assert l.run(['variablename'], variables={"variablename": "5678"}, default='default') == ['5678']

# Generated at 2022-06-13 14:53:44.634961
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ['ansible_play_hosts', 'ansible_play_batch', 'ansible_play_hosts_all']
    variables = {
        'ansible_play_hosts': 'test_ansible_play_hosts',
        'ansible_play_batch': 'test_ansible_play_batch',
        'ansible_play_hosts_all': 'test_ansible_play_hosts_all'
    }
    test_ret = lookup.run(terms, variables)
    assert terms == test_ret

# Generated at 2022-06-13 14:53:55.642094
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    terms = 'myvar'
    variables = {'myvar': 'hello'}
    res = lookup_module.run(terms, variables)
    assert res == ['hello']

    terms = 'myvar'
    res = lookup_module.run(terms)
    assert res == []

    terms = ['myvar', 'myvar2']
    variables = {'myvar': 'hello'}
    res = lookup_module.run(terms, variables)
    assert res == ['hello']

    terms = ['myvar', 'myvar2']
    variables = {'myvar': ['hello', 'world']}
    res = lookup_module.run(terms, variables)
    assert res == [['hello', 'world']]

    terms = 'myvar'

# Generated at 2022-06-13 14:54:04.900683
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Give all the required parameters to the instance of LookupModule class
    mod = LookupModule()
    mod._templar = dict()
    mod._templar._available_variables = dict(
        a=1,
        b="2",
        c=3,
        d=4,
        inventory_hostname="[aHost]",
        hostvars={
            "[aHost]": dict(
                b="Not2",
                d="Not4",
                e=5,
                f=6
            )
        }
    )

    # Check if the method raises AnsibleError exception if the term is not string
    with pytest.raises(AnsibleError):
        mod.run([4], {})

    # Check default parameter
    assert mod.run(['z'], {}) == []

# Generated at 2022-06-13 14:54:13.716209
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # first block of tests - setting the variablename result and myvar value
    myvars = {
        'variablename': 'hello',
        'other_variable': 'world',
        'hostvars': {'hostname': {'ansible_play_hosts': [], 'ansible_play_batch': 0, 'ansible_play_hosts_all': []}},
    }

    # test with all three parameters
    myterm = 'variablename'
    m = LookupModule()
    m._templar.available_variables = myvars
    m._templar._available_variables = myvars
    result = m.run([myterm], variables=myvars)
    assert result == ['hello']

    # test with two parameters and see no NameError exception is thrown
    my

# Generated at 2022-06-13 14:54:16.044432
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    assert lookup_module.run([]) == []
    assert lookup_module.run(['', '']) == [None, None]

# Generated at 2022-06-13 14:54:24.145603
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Tests for run() method of class LookupModule
    # _templar._available_variables = {'variablename': 'hello'}
    myvars = {'variablename': 'hello'}

    # test 1: if '_templar.available_variables' is None
    l = LookupModule()
    l._templar._available_variables = None
    try:
        l.run(terms=['variablename'], variables=None)
    except AnsibleUndefinedVariable:
        pass
    else:
        assert False
    l.run(terms=['variablename'], variables=myvars)

    # test 2: if terms is a list with one term 'variablename'
    terms = ['variablename']
    l = LookupModule()
   

# Generated at 2022-06-13 14:54:33.658743
# Unit test for method run of class LookupModule