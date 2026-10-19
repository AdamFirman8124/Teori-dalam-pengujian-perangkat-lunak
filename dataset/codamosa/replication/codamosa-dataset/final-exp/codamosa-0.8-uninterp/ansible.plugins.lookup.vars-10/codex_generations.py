

# Generated at 2022-06-13 14:45:08.295512
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test object initialization
    obj = LookupModule()

    # Test default values
    obj.set_options({})
    assert (obj.get_option('default') == None)

    # Test set options
    obj.set_options({'default': 2})
    assert (obj.get_option('default') == 2)

    # Test run method
    # Test first if
    obj.run("test", {"test": "test1"})

    # Test second if
    obj.run("test2", {})

    # Test run method except block
    # Test first except
    obj.run("test3", {"test3": "test4"})

    # Test second except block
    obj.run("test4", {"test4": "test4"})

# Generated at 2022-06-13 14:45:18.645154
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class Object(object):
        pass
    terms = ['ansible_facts', 'hostvars']

# Generated at 2022-06-13 14:45:23.926371
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test function to check the output against the expected value
    def test_output(expected_value, *terms, **kwargs):
        kwargs_lookup = {'default': None}
        kwargs_lookup.update(kwargs)

        class GenericContainer(object):
            def __init__(self, *args, **kwargs):
                self.__dict__.update(kwargs)

        # Test lookup function
        lookup = LookupModule()
        lookup.set_options(kwargs_lookup)
        value = lookup.run(terms)

        # Test templar
        templar = lookup._templar
        templar.available_variables = kwargs_lookup.pop('variables', None)

# Generated at 2022-06-13 14:45:29.199589
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Arrange
    self = LookupModule()
    terms = ['VAR1', 'VAR2']
    variables = {'VAR1': 'y', 'VAR2': 'z'}

    # Act
    result = self.run(terms, variables)

    # Assert
    assert result == ['y', 'z']



# Generated at 2022-06-13 14:45:40.581049
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    LM = LookupModule()

    LM._templar._available_variables = {'test_var': 'test_value'}
    assert LM.run(terms=['test_var'], variables={}, default=None) == ['test_value']

    LM._templar._available_variables = {'hostvars': {'host1': {'test_var': 'test_value'}}}
    assert LM.run(terms=['test_var'], variables={'inventory_hostname': 'host1'}, default=None) == ['test_value']

    LM._templar._available_variables = {'hostvars': {'host1': {'test_var': 'test_value'}}}

# Generated at 2022-06-13 14:45:48.433586
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Check default value
    l = LookupModule()
    l._templar = "test"
    myvars = {'test': 'OK'}
    res = l.run(['test'], variables=myvars, **{})
    assert res == ['OK']

    # Check not existing value
    l = LookupModule()
    l._templar = "test"
    myvars = {'test': 'OK'}
    res = l.run(['test2'], variables=myvars, **{})
    assert res == []

    # Check default value
    l = LookupModule()
    l._templar = "test"
    myvars = {'test': 'OK'}

# Generated at 2022-06-13 14:45:56.082012
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Declare test variables
    terms = ['ansible_play_hosts', 'ansible_play_batch', 'ansible_play_hosts_all']
    variables = {'ansible_play_hosts': 'hosts', 'ansible_play_hosts_all': 'hostsall', 'ansible_play_batch': 'batchnum'}
    default = None

    # Create LookupModule object for testing
    lookup_obj = LookupModule()

    # Test LookupModule method run
    ret = lookup_obj.run(terms, variables, default=default)
    assert ret == ['hosts', 'batchnum', 'hostsall']

    # Declare test variables
    terms = ['ansible_play_hosts', 'ansible_play_batch', 'ansible_play_hosts_all']

# Generated at 2022-06-13 14:46:06.218688
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class TestLookupModule(LookupModule):
        def __init__(self):
            self.params = {}
            self.t = {}

        def set_options(self, var_options=dict(), direct=dict()):
            self.params = dict(var_options)
            self.params.update(direct)
            self.t = dict()

        def get_option(self, key):
            return self.params[key]

        def _templar(self, v, **kwargs):
            self.t = dict(kwargs)
            self.t['template'] = v
            return v

    lookup = TestLookupModule()
    terms = ["lol"]
    variables = {"lol": "ahaha"}

    lookup.run(terms=terms, variables=variables)

# Generated at 2022-06-13 14:46:16.478470
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class MyTemplar:
        def __init__(self):
            self.vars = {
                'inventory_hostname': 'my_host',
                'hostvars': {
                    'my_host': {
                        'a': 'A'
                    }
                },
                'b': 'B'
            }

    my_templar = MyTemplar()

    class MockLookupBase:
        def __init__(self):
            self._templar = my_templar

        def set_options(self, var_options=None, direct=None):
            self.direct = direct

        def get_option(self, key):
            return self.direct[key]
    

# Generated at 2022-06-13 14:46:17.212826
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert True

# Generated at 2022-06-13 14:46:21.604171
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 14:46:27.509373
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six.moves import StringIO
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    loader = DataLoader()
    inv_source = StringIO("""
        foo ansible_connection=local ip=1.2.3.4
        bar ansible_connection=local ip=4.3.2.1
        """)
    inv_inventory = InventoryManager(loader=loader, sources=[inv_source])
    variables = {"inventory_hostname": "foo"}
    variable

# Generated at 2022-06-13 14:46:32.003633
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.template import Templar

    templar = Templar(variables={
        'foo': 'bar',
        'baz': 'biz',
        'foo2': 'bar2',
        'baz2': 'biz2',
        'inventory_hostname': 'test_host',
        'hostvars': {
            'test_host': {
                'foo2': 'bar2',
                'baz2': 'biz2',
            }
        }
    })

    # Test with one simple variable
    res = LookupModule(templar).run(terms=['foo'], variables={
        'foo': 'bar',
    })
    assert ['bar'] == res

    # Test with two simple variables

# Generated at 2022-06-13 14:46:42.135045
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test with default
    lm = LookupModule()
    terms = ["term1", "term2"]
    variables = {'term1': "val1", 'term2': "val2"}
    default = "default"
    result = lm.run(terms, variables, default=default)
    assert result == ["val1", "val2"]

    # test without default, should fail
    lm = LookupModule()
    terms = ["term1", "term2", "term3"]
    variables = {'term1': "val1", 'term2': "val2"}
    default = None
    try:
        lm.run(terms, variables, default=default)
    except AnsibleUndefinedVariable:
        pass
    except Exception as e:
        assert False, "Unexpected exception: %s" % e

   

# Generated at 2022-06-13 14:46:53.037111
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    ''' Unit tests for method run of class LookupModule '''
    # Variable declaration
    terms = ['ansible_play_hosts', 'ansible_play_batch', 'ansible_play_hosts_all']
    variables = {'ansible_play_hosts' : 'localhost', 'ansible_play_batch' : 1, 'ansible_play_hosts_all' : ['localhos']}
    kwargs = {}
    myvars = {'ansible_play_hosts' : 'localhost', 'ansible_play_batch' : 1, 'ansible_play_hosts_all' : ['localhos']}

    # Object initialization
    obj = LookupModule()

    # Check if run returns the expected result

# Generated at 2022-06-13 14:47:03.559347
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.plugins.lookup
    from ansible.plugins.lookup import LookupModule
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    lookup_plugin = LookupModule()
    inventory = InventoryManager(loader=None, sources='localhost,')
    variables = VariableManager(loader=None, inventory=inventory)
    templar = Templar(loader=None, variables=variables)
    variables['myvar'] = 'ename'
    variables['variablename'] = 'hello'
    assert lookup_plugin.run(['variablename'], variables=variables) == ['hello']
    assert lookup_plugin.run(['variablename'], variables=templar._available_variables) == ['hello']
    assert lookup

# Generated at 2022-06-13 14:47:10.469439
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """ Unit test for method run of class LookupModule """
    lookup_plugin = LookupModule()

    # Test for empty terms
    try:
        lookup_plugin.run([], variables=None)
        raise AssertionError('Test #1.1 failed - empty terms')
    except AnsibleError as e:
        if str(e) != 'At least one term needs to be supplied to the vars lookup plugin':
            raise AssertionError('Test #1.1 failed - wrong exception message: %s' % str(e))
        pass

    # Test for terms of wrong type

# Generated at 2022-06-13 14:47:19.439340
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Injecting fake values in contexts to test the methods
    lookup_module = LookupModule()
    lookup_module.set_options(var_options={'test_var1': 'test_val1', 'test_var2': 'test_val2', 'ansible_play_hosts': [1,2,3,4]}, direct={'default':'test_default'})
    result = lookup_module.run(['test_var1', 'test_var2', 'ansible_play_hosts'])
    assert result == ['test_val1', 'test_val2', [1,2,3,4]]

# Generated at 2022-06-13 14:47:29.856171
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    # A single argument is returned
    assert lookup_module.run(['ansible_play_hosts'], variables=dict(ansible_play_hosts = 'some_host')) == ['some_host']

    # Multiple arguments are returned
    assert lookup_module.run(
        ['ansible_play_hosts', 'ansible_play_batch', 'ansible_play_hosts_all'],
        variables=dict(ansible_play_hosts = 'some_host', ansible_play_batch = 'some_batch', ansible_play_hosts_all = 'some_hosts_all'))\
        == ['some_host', 'some_batch', 'some_hosts_all']

    # The default value is returned if the variable is not set
    assert lookup_module

# Generated at 2022-06-13 14:47:41.344958
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class MockTemplar:
        _available_variables = {'ansible_play_hosts':'', 'ansible_play_batch':'', 'ansible_play_hosts_all':'', 'inventory_hostname':''}

        def template(self, value, fail_on_undefined=True):
            return value

    class MockVarManager:
        def __init__(self):
            self.variable_manager = MockVariableManager()

        def get_vars(self, loader, play, host=None):
            return self.variable_manager.extra_vars


# Generated at 2022-06-13 14:48:00.178185
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # patch the module
    old_load_module = None
    old_construct_instance = None
    old_module_cache = None

# Generated at 2022-06-13 14:48:06.276375
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit test for method run of class LookupModule
    """
    lookup = LookupModule()

    # Testing with simple variables
    terms = 'hello'
    variables = dict(
        hello='world'
    )
    assert lookup.run([terms], variables=variables) == ['world']

    # Testing with complex variables
    variables = dict(
        hello=dict(
            sub_var=12
        )
    )
    assert lookup.run([terms], variables=variables) == [dict(sub_var=12)]

# Generated at 2022-06-13 14:48:18.193910
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources="localhost,")
    variable_manager = VariableManager(loader=loader, inventory=inventory)

# Generated at 2022-06-13 14:48:33.196752
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    look = LookupModule()
    look._templar = Mock_look_templar()
    terms = ["ansible_play_hosts", "ansible_play_batch", "ansible_play_hosts_all"]
    variables = {'ansible_play_hosts':'localhost', 'ansible_play_batch':'1',
                 'ansible_play_hosts_all':'localhost', 'hostvars': {'localhost': {'ansible_play_hosts':'localhost', 'ansible_play_batch':'1',
                 'ansible_play_hosts_all':'localhost'}}}
    look._templar._available_variables = variables
    assert look.run(terms, variables) == ['localhost', '1', 'localhost']

    # testing a single variable

# Generated at 2022-06-13 14:48:43.087204
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import PY2
    from ansible.module_utils.six.moves import cStringIO
    from ansible.module_utils.six.moves import builtins

    args = [
        'variabl' + myvar,
        'default',
    ]

    variables = dict(
        variablename = 'hello',
        myvar = 'ename',
    )

    arguments = dict(
        terms = args,
        variables = variables,
    )

    c = LookupModule()
    c.set_options(arguments.copy())
    c.run(**arguments)

    variables = dict(
        variablename = 'hello',
        myvar = 'notename',
    )


# Generated at 2022-06-13 14:48:49.457213
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()


    # test with no default
    module._templar._available_variables = { "foo": "bar"}
    result = module.run(["foo"])
    assert result == ["bar"]

    result = module.run(["foo", "bar", "baz"])
    assert result == ["bar", '', '']

    # test with default
    module._templar._available_variables = { "foo": "bar"}
    result = module.run(["foo"], default="hello")
    assert result == ["bar"]

    result = module.run(["foo", "bar", "baz"], default="hello")
    assert result == ["bar", 'hello', 'hello']

# Generated at 2022-06-13 14:48:57.363752
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # initialize
    test_loader_mock = Mock(return_value=None)
    test_display_mock = Mock(return_value=None)
    test_var_options = {}

    test_templar_mock = Mock()
    test_templar_mock.return_value = None
    test_templar_mock.template = Mock(return_value=None)

    test_module = LookupModule()
    test_module.set_loader = test_loader_mock
    test_module.display = test_display_mock

    test_module._templar = Mock()
    test_module._templar._available_variables = {}
    test_module._templar.template = Mock(return_value=None)

    #execution

# Generated at 2022-06-13 14:48:59.287187
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    result = lookup.run('test')
    assert result == []


# Generated at 2022-06-13 14:49:03.804124
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Test the methods of class LookupModule
    """

    assert LookupModule('', '', '', '').run(['var']) == []
    assert LookupModule('', '', '', '').run(['var'], {'var':'val'}) == ['val']
    assert LookupModule('', '', '', '').run([1]) == []

# Generated at 2022-06-13 14:49:14.410294
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    terms = ['a', 'b']
    variables = {
      'a': 'A',
      'b': {
        'x': 'X',
        'y': 1234
      },
      'hostvars': {
        'host': {
          'a': 'A',
          'b': {
            'x': 'X',
            'y': 1234
          }
        }
      },
      'inventory_hostname': 'host'
    }
    kwargs = {
      'default': 'DEFAULT'
    }

    lu = LookupModule()
    result = lu.run(terms, variables=variables, **kwargs)
    assert result[0] is variables['a']
    assert result[1] is variables['b']

    variables['inventory_hostname'] = 'host2'


# Generated at 2022-06-13 14:49:36.446771
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:49:39.095858
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test the method run of class LookupModule
    # Arrange
    terms = ['term_one', 'term_two']
    variables = {'term_one': 'value one'}
    kwargs = {'default': 'default'}
    lu = LookupModule()

    result = lu.run(terms, variables, **kwargs)
    expected = ['value one', 'default']
    assert result == expected

# Generated at 2022-06-13 14:49:42.546018
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()
    assert lookup_plugin.run(['variablename'], 
        variables={},
        defaults={}) == ['hello']

if __name__ == '__main__':
    test_LookupModule_run()

# Generated at 2022-06-13 14:49:50.397586
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Import module to be tested
    from ansible.plugins.lookup import vars

    # Create instance of class to be tested and test function
    module = vars.LookupModule()
    terms = ['variablename', 'variablenotename']
    variables = { "variablename": "hello", "myvar": "ename" }
    kwargs = { "default": "" }
    out_1 = module.run(terms, variables, **kwargs)

    # assert outcomes
    assert(out_1 == ["hello", ""])

# Generated at 2022-06-13 14:49:53.803546
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager


# Generated at 2022-06-13 14:50:05.562837
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import os
    import sys
    import pytest

    curr_dir = os.path.dirname(os.path.realpath(__file__))
    sys.path.insert(0, os.path.join(curr_dir, '../../../'))

    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.module_utils.six import string_types
    from ansible.plugins.lookup import LookupBase
    from ansible.playbook.play_context import PlayContext
    from jinja2.exceptions import UndefinedError

    from units.mock.loader import DictDataLoader
    from units.compat.mock import patch

    loader = DictDataLoader({})
    myvar = LookupModule(play_context=PlayContext(loader=loader))

    # Case

# Generated at 2022-06-13 14:50:15.893582
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    m = LookupModule()
    m._templar = DummyTemplar()
    m.set_options(var_options={}, direct={})
    terms = ['foo', 'bar']
    # Test with all valid terms
    assert(m.run(terms) == ['foo value', 'bar value'])
    # Test with one invalid term
    assert(m.run(terms[:1]) == ['foo value'])
    m.set_options(var_options={}, direct={'default': 'foo'})
    assert(m.run(terms) == ['foo value', 'bar value'])
    m._templar._available_variables['bar'] = None
    m.set_options(var_options={}, direct={'default': 'bar'})

# Generated at 2022-06-13 14:50:24.903160
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.template import Templar

    templar = Templar(loader=None)

    myvariables = {'inventory_hostname': 'localhost', 'inventory_hostname_short': 'localhost',
                   'hostvars': {'localhost': {'ansible_play_hosts': [u'foo'], 'ansible_play_batch': [u'foo']}},
                   'ansible_play_hosts': [u'foo'], 'ansible_play_batch': [u'foo']}

    myvars = {'inventory_hostname': 'localhost', 'inventory_hostname_short': 'localhost'}

    lookup = LookupModule()

    expected = [u'foo']
    result = lookup.run([u'ansible_play_hosts'], variables=myvars, templar=templar)


# Generated at 2022-06-13 14:50:34.746349
# Unit test for method run of class LookupModule
def test_LookupModule_run():
	import pytest
	from ansible.module_utils.six import StringIO
	from ansible.template import Templar
	from ansible.vars.hostvars import HostVars

	hostvars = HostVars(None)
	hostvars.data = {
			"host_name": {
				"v": "host_value"
			},
			"host_name2": {
				"v": "host_value2"
			}
	}
	hostvars.hostnames = ("host_name", "host_name2")


# Generated at 2022-06-13 14:50:44.678855
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['var1', 'var2']
    variables = { 'var1': 'value', 'var2': 'value2' }
    default = 'default'

    test_lookup = LookupModule()
    test_lookup._templar = {}
    test_lookup.set_options(var_options=variables, direct={ 'default': default })
    test_lookup._templar._available_variables = variables

    assert test_lookup.run(terms) == ['value', 'value2']
    assert test_lookup.run(['not_var']) == [default]
    assert test_lookup.run(['not_var'], default='another') == ['another']
    assert test_lookup.run(['not_var'], default=None) == [None]
    assert test_lookup

# Generated at 2022-06-13 14:51:20.243611
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module._templar._available_variables = {
        "variable_bar": "bar",
        "variable_foo": "foo",
        "variable_baz": "baz",
        "variable_baz_qux": "qux"
    }

    terms = [
        "variable_bar",
        "variable_foo",
        "variable_baz",
        "variable_baz_qux"
    ]
    expected_results = [
        "bar",
        "foo",
        "baz",
        "qux"
    ]

    res = lookup_module.run(terms, variables=None, **{})
    assert res == expected_results

# Generated at 2022-06-13 14:51:28.081187
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    """
    Unit test for method run of class LookupModule
    """

    my_lookup = LookupModule()
    my_lookup.set_options({'default': 'default_value'})

    # test with string type input
    ret = my_lookup.run(['term1'], variables={'term1': 'value1', 'other_term': 'other_value'})
    assert ret == ["value1"]

    # test with list type input
    ret = my_lookup.run(['term1', 'other_term'], variables={'term1': 'value1', 'other_term': 'other_value'})
    assert ret == ["value1", "other_value"]

    # test with bad input

# Generated at 2022-06-13 14:51:32.281105
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Testing to see that the lookup module can find a single variable
    variables = {
        "hostvars": {},
        "name1": "value1"
    }

    terms_to_test = [
        "name1",
        "name2"
    ]

    returned_value = LookupModule().run(terms=terms_to_test, variables=variables)
    assert returned_value[0] == "value1"
    assert returned_value[1] == None

# Generated at 2022-06-13 14:51:41.634683
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class MockTemplar(object):
        def __init__(self):
            self._available_variables = {'a': 'a_value',
                'hostvars': {'host1': {'b': 'b_host1_value', 'c': 'c_host1_value'},
                'host2': {'b': 'b_host2_value', 'c': 'c_host2_value'},
                'host3': {'b': 'b_host3_value', 'c': 'c_host3_value'}},
                'inventory_hostname': 'host2'}

        def template(self, value, fail_on_undefined=True):
            return value

    class MockLookupModule(LookupModule):
        def __init__(self):
            self._templar = MockTem

# Generated at 2022-06-13 14:51:49.359829
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit test for method run of class LookupModule
    """
    # First: Test without variable default
    # Test without variable default
    # Test without terms
    my_lookup = LookupModule()
    my_lookup._templar._available_variables = {'var1': 'this is variable 1', 'var2': 'this is variable 2'}
    my_lookup.set_options(var_options={}, direct={})
    assert my_lookup.run([], variables={}) == []
    # Test with one term
    assert my_lookup.run(['var1'], variables={}) == ['this is variable 1']
    # Test with several terms
    assert my_lookup.run(['var1', 'var2'], variables={}) == ['this is variable 1', 'this is variable 2']
   

# Generated at 2022-06-13 14:51:58.345121
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # testcase 1
    terms = ['var_name']
    variables = {'var_name': 'var_value1'}
    kwargs = {'var_name': 'var_value2'}
    lookup = LookupModule()
    result = lookup.run(terms, variables, **kwargs)
    assert result == ['var_value1']

    # testcase 2
    terms = ['var_name1', 'var_name2']
    variables = {'var_name1': 'var_value1', 'var_name2': 'var_value2'}
    kwargs = {'var_name1': 'var_value1', 'var_name2': 'var_value2'}
    lookup = LookupModule()
    result = lookup.run(terms, variables, **kwargs)

# Generated at 2022-06-13 14:52:01.509183
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Random dictionary
    variables = {"random": "dict"}
    # Empty list
    terms = []

    # Named arguments 
    default = {}
    kwargs = {}
    ret = run_LookupModule_run(variables,terms,default,kwargs)
    assert ret == []


# Generated at 2022-06-13 14:52:01.986493
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert True

# Generated at 2022-06-13 14:52:02.758826
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert False, "Test not implemented"

# Generated at 2022-06-13 14:52:09.162316
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup import LookupBase
    from ansible.template import Templar

    fixture_hostvars = {"host1": {"var": "host1var"},
                        "host2": {"var": "host2var"},
                        "host3": {"var": "host3var"}
                        }

    fixture_player = {"var": "playervar",
                      "inventory_hostname": "host1"
                      }

    fixture_player.update({"hostvars": fixture_hostvars})
    templar = Templar(loader=None, variables=fixture_player)
    fixture_terms = ["var", "hostvars", "inventory_hostname"]

    lu = LookupModule()
    lu._templar = templar
    lu._templar._available_variables = fixture_player



# Generated at 2022-06-13 14:53:18.687983
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Given
    # (mocking LookupBase)
    module_kwargs = {
        '_templar': {
            '_available_variables': {
                'hostvars': {
                    'myhostname': {
                        'hostvar_to_get': 'hostvar_value'
                    }
                },
                'top_level_var_to_get': 'top_level_var_value',
            }
        }
    }
    lookup_module = LookupModule(**module_kwargs)

    # When
    # (mocking LookupBase)
    result = lookup_module.run(
        terms=['top_level_var_to_get', 'hostvar_to_get'],
        **module_kwargs
    )

    # Then

# Generated at 2022-06-13 14:53:25.172329
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def set_option(self, var_options=None, direct=None):
        self._templar._available_variables = var_options

    class TestClass(LookupModule):
        _templar = dict()
        _templar._available_variables = dict()
        set_option = set_option

    # test success cases
    test_obj = TestClass()
    assert test_obj.run(terms=['abc'],
                        variables={'abc':'def'}) == ['def']

    assert test_obj.run(terms=['abc'],
                        variables={'hostvars': {'some.host': {'abc':'def'}}}) == ['def']


# Generated at 2022-06-13 14:53:36.957532
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play_context import PlayContext

    loads = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loads, variable_manager=variable_manager, host_list='')
    variable_manager.set_inventory(inventory)

    current_play_context = PlayContext()
    current_play_context.vars = {}

    test_object = LookupModule()
    test_object.set_options(var_options=current_play_context.vars, direct=current_play_context.vars)

# Generated at 2022-06-13 14:53:46.004502
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    result = [
        ['localhost'],
        ['localhost'],
        [['localhost']]
    ]
    terms = [
        'ansible_play_hosts',
        'ansible_play_batch',
        'ansible_play_hosts_all'
    ]
    variables = {
        'ansible_play_hosts': ['localhost'],
        'ansible_play_batch': 'localhost',
        'ansible_play_hosts_all': [['localhost']],
        'inventory_hostname': 'localhost',
        'hostvars': {
            'localhost': {
                'foo': 'bar'
            }
        }
    }

    lu = LookupModule()
    lu.set_options(
        var_options=variables,
        direct={'default': 'default'})

# Generated at 2022-06-13 14:53:55.894104
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.playbook import Playbook
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    fake_loader = DictDataLoader({
        "test": "{{ var }}",
        "test2": "{{ var2 }}",
    })

    templar = Templar(loader=fake_loader)
    play_context = PlayContext()
    play_context.variable_manager = VariableManager()
    # Set some variables
    play_context.variable_manager.extra_vars = load_resource({
        "var": "value",
        "var2": "value2",
    })

    new_stdin = StringIO()
    fake_playbook = Playbook()


# Generated at 2022-06-13 14:54:05.146638
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    test_LookupModule_run: test the run function of class LookupModule
    """
    from ansible.template import Templar
    from ansible.vars import VariableManager

    #  Create a templar object
    templar = Templar(loader=None, variables=VariableManager())

    #  Instantiate LookupModule object
    lookup = LookupModule(loader=None, templar=templar, variables=VariableManager(), **dict(
        inventory=None,
        cache=False,
        fact_path=None,
        loader=None,
        variable_manager=None
    ))
    #  Set the options
    lookup.set_options(var_options="vars", direct=dict(
        cache=False
    ))

    #  Create variables

# Generated at 2022-06-13 14:54:13.974089
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import copy

    variables = {
        "a_random_variable": "some_value",
        "hostvars": {
            "10.10.10.10": {
                "ansible_ssh_host": "10.10.10.10",
                "ansible_connection": "ssh",
                "ansible_user": "root",
                "example_variable": "value_1",
            },
            "10.10.10.11": {
                "ansible_ssh_host": "10.10.10.11",
                "ansible_connection": "ssh",
                "ansible_user": "root",
                "example_variable": "value_2",
            },
        }
    }

    class FakeTemplar:
        def __init__(self, var_dict):
            self.var_

# Generated at 2022-06-13 14:54:16.814288
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Given
    terms = ['foo', 'bar']
    variables = {'foo': 'FOO', 'bar': 'BAR'}

    # When
    res = LookupModule().run(terms, variables)

    # Then
    assert 'FOO' in res
    assert 'BAR' in res

# Generated at 2022-06-13 14:54:24.677144
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    term_list = ['variablename', 'variablenotename', 'variablename', 'ansible_play_hosts', 'ansible_play_batch', 'ansible_play_hosts_all', 'ansible_play_x', 'variablename.sub_var']
    variables = {}
    vars_dict = {'variablename': 'hello', 'myvar': 'ename', 'variablenotename': 'hello'}
    variables.update(vars_dict)
    l = LookupModule()
    l.set_options({u'default': None})

    # Mock getattr method of class LookupModule to return the vars_dict as available_variables
    def _getattr_method(self, variable):
        if variable == '_available_variables':
            return vars_

# Generated at 2022-06-13 14:54:32.554419
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_obj = LookupModule()
    vars = {'hostvars': {'host1': {'v1': 'value1'}}}
    result = test_obj.run(['v1'], variables=vars)
    assert result == ['value1']
    result = test_obj.run(['v2'], variables=vars)
    assert result == []
    result = test_obj.run(['v1'], variables=vars, default='default')
    assert result == ['value1']
    result = test_obj.run(['v2'], variables=vars, default='default')
    assert result == ['default']