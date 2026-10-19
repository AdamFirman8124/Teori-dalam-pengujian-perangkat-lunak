

# Generated at 2022-06-13 15:38:38.615339
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.vars.manager import VariableManager
    from ansible.template.safe_eval import unsafe_eval

    vm = VariableManager()
    vm.extra_vars = {"l_my_list": [1, 2, 3]}
    templar = Templar(loader=None, variables=vm)

    av = AnsibleJ2Vars(templar, {}, {'l_my_list': '{{ my_list }}'})
    assert av['my_list'] == [1, 2, 3]

    av = AnsibleJ2Vars(templar, {}, {'l_my_list': '{{ my_list | string }}'})
    assert av['my_list'] == '[1, 2, 3]'


# Generated at 2022-06-13 15:38:44.138417
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.vars import VariableManager
    from ansible.template import Templar
    from ansible.playbook.play_context import PlayContext

    variable_manager = VariableManager()
    variable_manager.extra_vars = {'first_var': 'first', 'second_var': 'second'}
    templar = Templar(loader=None, variables=variable_manager)
    play_context = PlayContext()
    globals = play_context.get_globals()

    aj2v = AnsibleJ2Vars(templar, globals)

    assert aj2v.__contains__('first_var') == True
    assert aj2v.__contains__('second_var') == True

    # __contains__ doesn't depend on the locals parameter value
    # Checking both when locals is None and when

# Generated at 2022-06-13 15:38:52.684788
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.plugins.loader import vars_loader
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    loader  = vars_loader
    variable_manager = VariableManager(loader=loader)
    templar = Templar(loader=loader, variable_manager=variable_manager)
    # Create an empty globals mapping
    globals = {}

    # Create an empty locals mapping
    locals = {}

    # Create an AnsibleJ2Vars object
    vars = AnsibleJ2Vars(templar, globals, locals=locals)

    # Retrieve a non-existent key
    # This should throw a KeyError
    key_does_not_exist = "key_does_not_exist"

# Generated at 2022-06-13 15:39:00.771941
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    tmpl = Templar(loader=None)
    hostv = HostVars(None, dict(abc='abc', efg='efg'))
    obj = AnsibleJ2Vars(tmpl, {}, {})
    assert obj.__getitem__('abc') == 'abc'
    assert obj.__getitem__('efg') == 'efg'
    print('%s: tests pass' % __file__)

if __name__ == '__main__':
    test_AnsibleJ2Vars___getitem__()

# Generated at 2022-06-13 15:39:12.602517
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    
    templar = Templar(DataLoader())
    ansible_vars = AnsibleJ2Vars(templar, globals=dict(abc='def'), locals=dict(ghi='jkl'))
    assert ansible_vars['abc'] == 'def'
    assert ansible_vars['ghi'] == 'jkl'
    try:
        ansible_vars['xyz']
        assert False, 'unexpected success: xyz'
    except KeyError:
        assert True
    ansible_vars._templar.available_variables = {'abc': 'def'}
    assert ansible_v

# Generated at 2022-06-13 15:39:19.609382
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    templar = Templar(loader=None)
    empty_vars = dict()
    globals = dict()
    vars = AnsibleJ2Vars(templar, globals, locals=empty_vars)
    key = 'item'
    value = 'value'

    globals[key] = value
    assert (key in vars) is True

    empty_vars[key] = value
    assert (key in vars) is True

    templar.available_variables[key] = value
    assert (key in vars) is True


# Generated at 2022-06-13 15:39:28.495778
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    '''
    AnsibleJ2Vars.__contains__ should return True if the variable exists in
    any of the sources - available_variables, globals or locals.
    '''

    # Helper to begin a test by initializing an AnsibleJ2Vars object
    def begin_test(vars, globals, locals):
        from ansible.playbook.templar import Templar
        templar = Templar(loader=None)
        templar._available_variables = vars
        return AnsibleJ2Vars(templar, globals, locals)

    # Tests follow
    ansible_vars = dict(one=1, three=3)
    globals = dict(two=2, four=4)

    # First vars are used if the variable is defined there
    j2vars = begin_

# Generated at 2022-06-13 15:39:40.179221
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.errors import AnsibleError
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.template import Templar

    class DummyVars():

        def __contains__(self, key):
            return True

    vars_manager = VariableManager()
    loader = DataLoader()
    templar = Templar(loader=loader, variables=vars_manager)
    globals = DummyVars()
    # missing locals argument
    try:
        AnsibleJ2Vars(templar, globals)
    except TypeError:
        pass
    else:
        raise AssertionError()
    # non-dict locals

# Generated at 2022-06-13 15:39:50.430163
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    import jinja2
    from ansible.template import Templar

    variables_dict = dict(a=1, b=2, c=3)
    templar = Templar(loader=None, variables=variables_dict)
    ansible_j2_vars = AnsibleJ2Vars(templar, dict())

    # test if a variable starts with '-'
    assert('-' in ansible_j2_vars)

    # test if a variable is contained in self._templar.available_variables
    assert('a' in ansible_j2_vars)

    # test if a variable is contained in self._globals
    assert('range' in ansible_j2_vars)


# Generated at 2022-06-13 15:39:57.214678
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar

    templar = Templar(None, loader=None)
    ansible_j2_vars = AnsibleJ2Vars(templar, {}, locals={})

    # Test that AnsibleJ2Vars.__contains__ return True with a good key
    assert True == ('good_key' in ansible_j2_vars)

    # Test that AnsibleJ2Vars.__contains__ return False with a bad key
    assert False == ('bad_key' in ansible_j2_vars)


# Generated at 2022-06-13 15:40:11.368491
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager

    hv = HostVars({'test': {'foo': 'bar'}})
    hv_test = HostVars({'fizz': 'buzz'})
    hv_test['test'] = HostVars({})
    hv_test_test = HostVars({'too': 'deep'})

    hv_test_test['test'] = HostVars({'foo': 'bar'})

    # Ensure VariableManager handles deeply nested hostvars
    v = VariableManager(loader=None, host_vars=hv, group_vars={})

    # Test __len__ with deeply nested hostvars

# Generated at 2022-06-13 15:40:23.391008
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import unittest

    class TestUndefinedVars(unittest.TestCase):
        def test__getitem__(self):
            import ansible.vars.hostvars
            from ansible.template import Templar
            from ansible.parsing.dataloader import DataLoader
            from ansible.inventory.manager import InventoryManager
            from ansible.vars.manager import VariableManager

            loader = DataLoader()
            inventory = InventoryManager(loader=loader, sources=['/dev/null'])
            variable_manager = VariableManager(loader=loader, inventory=inventory)
            templar = Templar(loader=loader, variables=variable_manager)

            j2vars = AnsibleJ2Vars(templar, dict(foo="bar"), locals=dict(ansible_check_mode=True))

# Generated at 2022-06-13 15:40:30.567597
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar

    templar = Templar(loader=None)
    globals = dict()
    locals = dict()

    mocked_self = dict(
        templar=templar,
        globals=globals,
        locals=locals,
    )

    v = AnsibleJ2Vars(
        templar=templar,
        globals=globals,
        locals=locals,
    )

    assert 'somevalue' in v

    assert 'something' not in v



# Generated at 2022-06-13 15:40:40.268178
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    # Setup
    variable = 'test_var'
    variable_value = 'test_var_value'
    variable_value_templated = 'test_var_value_templated'

    dictionary = {variable: variable_value}
    templar = MagicMock()
    templar.available_variables = copy.deepcopy(dictionary)
    templar.template.return_value = variable_value_templated

    # Test case: variable defined in dictionary
    # `__getitem__` should return the variable value
    expected = variable_value_templated
    actual = AnsibleJ2Vars(templar=templar, globals=dict(), locals=dict())[variable]
    assert actual == expected
    templar.template.assert_called_once_with(variable_value)

   

# Generated at 2022-06-13 15:40:49.191045
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    from ansible.vars import VariableModule
    class AnsibleModule(object):
        def __init__(self, params):
            self.params = params
        def fail_json(*args, **kwargs):
            pass
    class AnsibleVarsModule(VariableModule):
        def __init__(self):
            self.params = {}
    dl = DataLoader()
    t = Templar(dl, variables={'foo': 'bar', 'baz': 'qux'})
    hv = HostVars()
    vm = VariableManager(loader=dl, host_vars=hv)
   

# Generated at 2022-06-13 15:40:58.659946
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    import sys
    import os

    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    templar = Templar(loader=loader, variables={'var1': 1, 'var2': 2})

    variables = AnsibleJ2Vars(templar, globals={'g1': 1, 'g2': 2}, locals={'l1': 1})

    assert 'var1' in variables
    assert 'var2' in variables
    assert 'g1' in variables
    assert 'g2' in variables
    assert 'l1' in variables

    assert 'var3' not in variables
    assert 'g3' not in variables
    assert 'l3' not in variables

    return os.EX_OK



# Generated at 2022-06-13 15:41:07.862154
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    # Checks that the return of __getitem__ is a string
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.playbook.play_context import PlayContext
    from ansible.module_utils.six import integer_types

    v = VariableManager()
    v.extra_vars = dict(
        A1="A1",
        A2=dict(
            B1="B1",
            B2="B2",
        ),
        A3=dict(
            B3=dict(
                C1="C1",
                C2=2,
                C3=True,
                C4=False
            ),
        ),
    )
    templar = Templar(vars=v, loader=None, shared_loader_obj=None)


# Generated at 2022-06-13 15:41:18.516351
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():

    #constructor of AnsibleJ2Vars
    #initializes Ansi

    #def __init__(self, templar, globals, locals=None):

    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    class J2Obj(AnsibleBaseYAMLObject):
        pass
    class Templar():
        pass
    class HostVars():
        pass

    hv = HostVars(dict())
    j2obj = J2Obj(dict())
    templar = Templar()


# Generated at 2022-06-13 15:41:25.306837
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from ansible.parsing.vault import VaultLib
    from ansible.template import Templar
    from ansible import constants as C
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    v1 = VaultLib([])
    t = Templar(loader=None, variables={}, vault_secrets={}, shared_loader_obj=None, vault_password=None,
                template_class=None)
    c = DistributionFactCollector()
    v = AnsibleJ2Vars(t, c.get_facts(), locals=None)
    print(v['ansible_pkg_mgr'])
    print(v['ansible_python_version'])
    print(v['dirname'])
    print(v['real_file_name'])
    print(v['vars'])
   

# Generated at 2022-06-13 15:41:32.183689
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from ansible.template import Templar
    templar = Templar(None, loader=None)
    j2vars = AnsibleJ2Vars(templar, {'a':10})
    assert len(j2vars) == 1
    assert 10 == j2vars['a']
    j2vars._locals['b'] = 'b'
    assert len(j2vars) == 2
    assert 'b' == j2vars['b']

# Generated at 2022-06-13 15:41:43.632663
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import sys
    import os
    import __main__ as main
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from ansible.template import Templar
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory import Inventory, Host, Group
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.callback import CallbackBase

    # create the variable manager, which will be shared throughout
    # the code, ensuring a consistent view of global variables
    variable_manager = VariableManager()

    # create the inventory, which contains groups and the hosts

# Generated at 2022-06-13 15:41:55.362327
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.vars.hostvars import HostVars
    from ansible.vars import VariableManager
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    # ============== Test case 0 ==============
    varname = 'a'
    locals = None
    templar = Templar(
        loader=DataLoader(),
        variables=VariableManager(
            loader=DataLoader(),
            inventory=InventoryManager(loader=DataLoader())
        )
    )
    globals = dict()
    j2_vars = AnsibleJ2Vars(templar, globals, locals)
    # Key Exist and it's a hostvars

# Generated at 2022-06-13 15:42:04.043011
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    # import jinja2 to test the constructor of AnsibleJ2Vars
    from jinja2.environment import Environment
    from jinja2.runtime import Undefined

    # create a minimal jinja2 environment
    j2_env = Environment(
        undefined=Undefined,
        trim_blocks=True,
        lstrip_blocks=True,
    )

    # create a minimal jinja2 runtime
    # we are using a dummy loader to pass the test
    j2_loader = j2_env.loader = object()

    # create our minimal j2_vars with a valid jinja2 env and loader
    j2_vars = AnsibleJ2Vars()

    # now we can test the constructor of AnsibleJ2Vars

# Generated at 2022-06-13 15:42:07.513669
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    templar = Templar(loader=None, shared_loader_obj=None)
    j2vars = AnsibleJ2Vars(templar, globals={"var1":"value1","var2":"value2"})
    assert j2vars.__contains__("var1") is True
    assert j2vars.__contains__("var2") is True
    assert j2vars.__contains__("var3") is False


# Generated at 2022-06-13 15:42:15.705629
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    #create a jinja2 environment which will return a mocked jinja template
    template_data = """
    {% if (myvar in myvars) %}
    foo
    {% endif %}
    """
    # mock jinja2 template method render, so that the template does not have to be rendered
    # this is to prevent errors from occuring due to the lack of a loader
    templar = Templar(None, VariableManager(loader=None, inventory=InventoryManager()), None)
    templar._t = templar._environment.from_string(template_data)

    # create a dictionary of variables
    myvars = {}
    myvars["myvar"]

# Generated at 2022-06-13 15:42:25.836767
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    # Create the object
    from units.mock.loader import DictDataLoader
    from ansible.template.safe_eval import safe_eval
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    loader = DictDataLoader({})
    play_context = PlayContext()
    templar = Templar(loader=loader, variables={}, fail_on_undefined=True)
    a = AnsibleJ2Vars(templar, {}, {'l_test': '1', 'test': '{{test}}'})
    r = a.__getitem__('l_test')
    assert '1' == r, "value should be 1"
    r = a.__getitem__('test')
    # for now, return '{{test}}' as this is what we used to do

# Generated at 2022-06-13 15:42:29.344281
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
   #### Define variables #####################################################
   templar = None
   globals = {}
   locals = None
   ajv = AnsibleJ2Vars(templar, globals, locals)

   #### Execute task ########################################################
   contains = ajv.__contains__(None)

   #### Assertions ##########################################################
   assert_equal(contains, False)


# Generated at 2022-06-13 15:42:37.012824
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    import ansible.template.vars as ansible_vars
    from ansible.template import Templar
    templar = Templar(loader=None)
    globals = {'hostvars': {'host1': {'test': '1'}, 'host2': {'test': '2'}}}
    locals = {'test': {'test': '3'}}
    ansible_vars = AnsibleJ2Vars(templar, globals, locals=locals)

    assert 'test' in ansible_vars
    assert 'test1' not in ansible_vars


# Generated at 2022-06-13 15:42:48.160851
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    from ansible.parsing.yaml.objects import AnsibleMapping
    templar = None
    globals = AnsibleMapping(dict(param1='value1', param2='value2'))
    locals = AnsibleMapping(dict(param1='value11', param2='value22', l_param3='value33'))
    vars1 = AnsibleJ2Vars(templar, globals, locals)

    # test if it raises ValueError when templar is None
    try:
        vars2 = AnsibleJ2Vars(None, globals, locals)
    except ValueError:
        pass

# Generated at 2022-06-13 15:42:55.103133
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    locals = {
        'l_hello': '6',
        'foo': '6'
    }
    available_variables = {
        'world': '6'
    }
    globals = {
        'bar': '6'
    }

    templar = MagicMock()
    templar.available_variables = available_variables

    test_obj = AnsibleJ2Vars(templar, globals, locals=locals)
    assert len(test_obj) == 3


# Generated at 2022-06-13 15:43:22.551811
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar

    templar = Templar()

    # Mocking up a AnsibleJ2Vars object
    j2_vars = AnsibleJ2Vars(templar, dict(var2='value2', var3='value3'), dict(var1='value1'))

    assert ('var1' in j2_vars)
    assert ('var2' in j2_vars)
    assert ('var3' in j2_vars)
    assert not ('var4' in j2_vars)


# Generated at 2022-06-13 15:43:27.197510
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    from ansible.template import Templar
    templar = Templar(loader=None)
    j2_vars = AnsibleJ2Vars(templar, {})
    assert isinstance(j2_vars, Mapping)
    assert len(j2_vars) == 0
    assert list(j2_vars) == []

# Generated at 2022-06-13 15:43:37.386141
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars

    class my_vars(HostVars):
        def __getitem__(self, key):
            if key == 'a':
                return 'b'
            elif key == 'c':
                return 'd'
            else:
                raise KeyError

    vars = AnsibleJ2Vars(Templar(), { 'a': 'b', 'c': my_vars({ 'c': 'd' }) })
    assert vars['a'] == 'b'
    assert vars['c'] == 'd'
    assert raises(KeyError, vars.__getitem__, 'e')

# Generated at 2022-06-13 15:43:49.264168
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    variables = HostVars()
    templar = Templar(loader=DataLoader())
    locals_ = {'l_variable': 'value'}
    globals_ = {}
    ansible_j2_vars = AnsibleJ2Vars(templar, globals_, locals=locals_)
    ansible_j2_vars._templar.available_variables = {'variable': 'value'}
    assert 'variable' in ansible_j2_vars
    assert 'l_variable' in ansible_j2_vars
    assert 'variable2' not in ansible_j2_vars


# Generated at 2022-06-13 15:43:59.538476
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    '''
    AnsibleJ2Vars.__contains__(x)
    '''
    templar = None
    globals = {
        'g_var_a': 1,
        'g_var_b': 2,
    }
    locals = {
        'l_var_a': 1,
        'l_var_b': 2,
    }

    vars = AnsibleJ2Vars(templar, globals, locals)

    # check the contents of vars
    assert isinstance(vars, Mapping)
    assert len(vars) == 0

    assert 'g_var_a' in vars
    assert 'g_var_b' in vars
    assert 'g_var_c' not in vars

    assert 'l_var_a' in vars

# Generated at 2022-06-13 15:44:11.005582
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    '''
    Testing AnsibleJ2Vars.__contains__ method
    '''

    def test_AnsibleJ2Vars___contains__ec2(avaible_variable, locals_value):
        '''
        Testing AnsibleJ2Vars.__contains__ method

        :type avaible_variable: dict
        :type locals_value: dict
        :rtype: none
        '''
        globals_value = {'test_globals':'test_globals'}

        ansiblej2vars = AnsibleJ2Vars(avaible_variable, globals_value, locals_value)

        # should return True if all arguments are isinstance(dict)
        assert isinstance(ansiblej2vars.__contains__('test_globals'), bool)
        assert isinstance

# Generated at 2022-06-13 15:44:21.782750
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():

    from ansible.playbook.play_context import PlayContext
    import ansible.template.template as template

    # Initialize a PlayContext and a Templar
    pc = PlayContext()
    pc.hostvars = dict()
    t = template.Templar(loader=None, variables=pc.hostvars)
    vars = AnsibleJ2Vars(t, dict(), dict())

    # Test method __contains__ with an undefined key
    try:
        dict(vars)['undefined']
        assert False
    except KeyError:
        assert True

    # Add a var to the host variables
    pc.hostvars['host'] = 'host'
    pc.hostvars['play'] = 'play'
    pc.hostvars['inventory'] = 'inventory'

# Generated at 2022-06-13 15:44:28.350168
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    #Pass
    my_contains_object = AnsibleJ2Vars(templar=None, globals='', locals='locals')
    my_contains_object.contains('locals')
    my_contains_object.contains('locals')
    my_contains_object.contains('')
    my_contains_object.contains('locals')
    my_contains_object.contains('')

    #Fail
    my_contains_object = AnsibleJ2Vars(templar=None, globals='', locals='locals')
    my_contains_object.contains('local')
    my_contains_object.contains('locals')
    my_contains_object.contains('locals')

# Generated at 2022-06-13 15:44:35.583632
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    templar = Templar(loader=None)

    # Test case for dict vars
    vars = dict(a=1)
    j2vars = AnsibleJ2Vars(templar, {}, vars)

    assert j2vars.__contains__("a") == True
    assert j2vars.__contains__("b") == False


# Generated at 2022-06-13 15:44:45.713178
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    import jinja2
    from ansible.template.templar import Templar

    g = {'foo': 'global'}
    l = {'bar': 'local'}

    x = AnsibleJ2Vars(Templar(loader=None, variables=None), g, l)
    assert(isinstance(x, dict))
    assert('foo' in x)
    assert('bar' in x)
    assert('baz' not in x)

    # In Ansible 2.4, the Jinja environment moved from being a member variable of the templar
    # to being a classmethod on the templar.  If a class is instantiated using the earlier approach,
    # templar.environment still exists and is a Jinja environment.  If a class is instantiated
    # using the new approach, templar.environment is

# Generated at 2022-06-13 15:45:03.107520
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    # test no error
    templar = Templar(VariableManager(), InventoryManager())
    ansible_vars = AnsibleJ2Vars(templar, dict())

# Generated at 2022-06-13 15:45:06.289265
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    vars = AnsibleJ2Vars(Templar(), {'a': 'b'})
    assert 'a' in vars
    assert 'c' not in vars


# Generated at 2022-06-13 15:45:12.600611
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    assert AnsibleJ2Vars(None, None).__contains__(None) == False
    assert AnsibleJ2Vars(None, {'b': 2}).__contains__('b') == True
    assert AnsibleJ2Vars(None, {'b': 2}).__contains__('a') == False


# Generated at 2022-06-13 15:45:17.479183
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.template.safe_eval import allow_unsafe_args
    templar = allow_unsafe_args(True)
    assert isinstance(templar, object)
    globals = None
    locals = None
    obj = AnsibleJ2Vars(templar, globals, locals)
    assert isinstance(obj, Mapping)
    int_obj = len(obj)
    # TODO: Check if obj is mapped
    # assert isinstance(int_obj, int)
    assert isinstance(int_obj, object)


# Generated at 2022-06-13 15:45:24.357089
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.template.safe_eval import safe_eval
    from ansible.template.vars import AnsibleVars

    locals = dict(a=1, b=2)
    globals = dict(c=3, d=4)
    templar = AnsibleVars(safe_eval)
    vars = AnsibleJ2Vars(templar, globals, locals)
    assert len(vars) == 4
    assert 'a' in vars
    assert 'c' in vars
    try:
        vars['e']
        assert 0, "Should get exception here"
    except KeyError as e:
        pass
    try:
        vars['f']
        assert 0, "Should get exception here"
    except KeyError as e:
        pass

# Generated at 2022-06-13 15:45:28.402134
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    """test_AnsibleJ2Vars___contains__ - test class method __contains__ of class AnsibleJ2Vars"""
    pass # print('test')

# Generated at 2022-06-13 15:45:37.581347
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    # test with HostVars
    hostvars = HostVars(dict())
    templar = Templar(loader=None)
    globals = dict()
    vars = AnsibleJ2Vars(templar, globals)
    vars["test"] = hostvars
    assert vars["test"] == hostvars
    # test with unsafe variable
    vars = AnsibleJ2Vars(templar, globals)
    vars["test"] = AnsibleUnicode('test')
    setattr(vars["test"], "__UNSAFE__", True)
    assert vars["test"] == 'test'


# Generated at 2022-06-13 15:45:38.697386
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
   pass

# Generated at 2022-06-13 15:45:48.622608
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject, AnsibleMapping
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    templar = Templar(loader=None, variables={}, shared_loader_obj=None)
    globals = { 'foo': 'foo' }
    locals = { 'bar': 'bar' }
    vars = AnsibleJ2Vars(templar, globals, locals=locals)

    # Test when 'varname' isn't in the globals or locals, or _templar.available_variables
    # Check raised exception type and message

# Generated at 2022-06-13 15:45:55.878045
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    from ansible.parsing.vault import VaultLib
    from ansible.template import Templar

    vault_password = 'ansible'
    vault = VaultLib(vault_password)


# Generated at 2022-06-13 15:46:18.602033
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext

    loader = DataLoader()
    play_context = PlayContext()
    templar = Templar(loader=loader, variables=play_context.startup_vars, shared_loader_obj=loader)
    host = 'localhost'
    variable_manager = VariableManager(loader=loader, inventory=None, play_context=play_context, host_vars={host: {}})

    objects = AnsibleJ2Vars(templar, variable_manager.get_vars(loader=loader, play=None, host=host))

    i = 0
    for key in objects:
        i += 1

# Generated at 2022-06-13 15:46:30.991174
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    templar = Templar(loader=None, variables={})
    globals = {}
    locals = {'foo': 'bar'}
    j2vars = AnsibleJ2Vars(templar, globals, locals)

    # returns True when variable name is found in locals
    assert 'foo' in j2vars
    # returns True when variable name is found in templar.available_variables
    templar.available_variables = {'foo': 'bar'}
    j2vars = AnsibleJ2Vars(templar, globals, locals)
    assert 'foo' in j2vars
    # returns True when variable name is found in globals
    globals = {'foo': 'bar'}
    j2vars = AnsibleJ2Vars(templar, globals, locals)

# Generated at 2022-06-13 15:46:37.827560
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    """
    Unit test for method __contains__ of class AnsibleJ2Vars
    """
    av = {'foo': 'bar', 'z': 'z'}
    m = {'glob_foo': 'glob_bar', 'glob_z': 'glob_z'}
    locals = {'foo': 'baz', 'z': 'z'}
    templar = None
    ansible_j2_vars = AnsibleJ2Vars(templar, m, locals)
    assert 'foo' in ansible_j2_vars
    assert 'z' in ansible_j2_vars
    assert 'foo' in ansible_j2_vars._locals
    assert 'z' in ansible_j2_vars._locals
    assert 'foo' in ansible_

# Generated at 2022-06-13 15:46:46.683280
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    from ansible.template import Templar

    templar = Templar()
    globals = {
        'g_foo': 1,
        'g_bar': 2,
        'g_baz': 3,
    }
    locals_ = {
        'g_bar': -2,
        'l_bar': 4,
        'l_baz': 5
    }

    ajv = AnsibleJ2Vars(templar, globals, locals_)

    assert sorted(ajv.__iter__()) == ['g_bar', 'g_baz', 'g_foo', 'l_bar', 'l_baz']

# Generated at 2022-06-13 15:46:51.574575
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    templar = Templar(loader=None)
    ajv = AnsibleJ2Vars(templar, {}, None)
    ajv._locals = {}
    ajv._templar.available_variables = {}
    with pytest.raises(KeyError):
        ajv.__getitem__("bogus")


# Generated at 2022-06-13 15:46:58.864557
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import ansible.template
    t = ansible.template.AnsibleTemplate('foo', {}, False)
    av = {}
    g = {'foo': 'bar'}
    l = {'baz': 'faz'}
    obj = ansible.template.AnsibleJ2Vars(t, g, l)
    assert obj.__getitem__('foo') == 'bar'
    assert obj.__getitem__('baz') == 'faz'

# Generated at 2022-06-13 15:47:06.140745
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    templar = object()
    globals = {'g1': object()}
    locals = {'l1': object()}
    ansible_j2_vars = AnsibleJ2Vars(templar, globals, locals)
    assert ansible_j2_vars.__contains__('g1') is True
    assert ansible_j2_vars.__contains__('l1') is True
    assert ansible_j2_vars.__contains__('g2') is False
    assert ansible_j2_vars.__contains__('l2') is False


# Generated at 2022-06-13 15:47:14.196381
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    import ansible.template
    import ansible.vars.hostvars
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    from ansible.parsing.dataloader import DataLoader

    hostvars = ansible.vars.hostvars.HostVars({'localhost': '127.0.0.1'})
    templar = ansible.template.Templar(loader=DataLoader())

    assert templar.available_variables is None
    templar.available_variables = {'vars': {'one': '1', 'two': 2, 'three': hostvars}}

    globals = {'one': 1, 'two': 2}

    # vars

# Generated at 2022-06-13 15:47:24.678814
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    # Test if the method throws an exception when the given name is not in the variables

    class Templar():

        @staticmethod
        def template(value):
            return value

        def __init__(self):
            self.available_variables = dict()

    templar = Templar()

    j2vars = AnsibleJ2Vars(templar, dict())

    try:
        j2vars['unknown_name']
        assert False # exception should be thrown
    except KeyError:
        assert True
    except:
        assert False # wrong type of exception is thrown

    # Test if the method gets the value from the global variables

    global_variables = dict()
    global_variables['global_name1'] = 'global_value1'
    global_variables['global_name2'] = 'global_value2'

   

# Generated at 2022-06-13 15:47:27.876994
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    import ansible.template
    import jinja2.utils
    vars = dict(a=dict(b=dict(c=dict(d=1))))
    templar = ansible.template.AnsibleTemplar(loader=None)

    vars = AnsibleJ2Vars(templar, globals=vars)
    assert len(vars) == 1
    assert len(vars['a']) == 1
    assert len(vars['a']['b']) == 1
    assert len(vars['a']['b']['c']) == 1


# Generated at 2022-06-13 15:47:58.451217
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import unittest
    import mock
    import json

    class AssertRaisesContext(object):
        def __init__(self, expected, expected_regex=None):
            self.expected = expected
            self.expected_regex = expected_regex

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_value, tb):
            if exc_type is None:
                try:
                    exc_name = self.expected.__name__
                except AttributeError:
                    exc_name = str(self.expected)
                raise self.failureException("{0} not raised".format(exc_name))
            if not issubclass(exc_type, self.expected):
                # let unexpected exceptions pass through
                return False
            self.exception = exc_value

# Generated at 2022-06-13 15:48:04.696294
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import UnsafeProxy

    templar = Templar()
    locals = dict()
    globals = dict()
    j2_vars = AnsibleJ2Vars(templar, globals, locals=locals)

    j2_vars['toto'] = 'toto'
    assert j2_vars['toto'] == 'toto'

    hostvars = HostVars(templar)
    hostvars['titi'] = 'titi'
    j2_vars['vars'] = hostvars
    assert j2_vars['vars']['titi'] == 'titi'
    assert j2_vars['vars']

# Generated at 2022-06-13 15:48:16.240423
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars

    templar = Templar(loader=None)

    v = AnsibleJ2Vars(templar, globals(), locals())
    v._templar.available_variables = { 'test': 'test' }
    v._locals = { 'locals': 'locals' }

    assert 'test' in v
    assert 'locals' in v
    assert 'range' in v
    assert 'test2' not in v

    # Make sure to check __contains__ with a variable defined in both locals and
    # available_variables i.e. in both _locals and _templar.available_variables.
    # This test method should return True because the variable is in locals and
    # locals should have priority over

# Generated at 2022-06-13 15:48:22.827801
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    from ansible.utils.vars import merge_hash
    from ansible.vars import VariableManager

    class Options(object):
        def __init__(self, no_log, vvv):
            self.no_log = no_log
            self.verbosity = vvv

    class PluginLoader(object):
        def __init__(self):
            pass

    class PlayContext(object):
        def __init__(self):
            pass

    vm = VariableManager()
    vm.extra_vars = {u'foo': u'bar'}
    vm.host_vars = {u'host1': {u'hostvar': u'hostvalue'}}

# Generated at 2022-06-13 15:48:32.367161
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    '''
    Test the AnsibleJ2Vars.__contains__ method
    '''
    from ansible.template import Templar
    templar = Templar(None, loader=None)
    j2vars = AnsibleJ2Vars(templar, globals=dict())

    j2vars['varname1'] = 'value1'
    assert 'varname1' in j2vars
    del(j2vars['varname1'])

    j2vars._globals['varname2'] = 'value2'
    assert 'varname2' in j2vars
    del(j2vars._globals['varname2'])

    j2vars._locals['varname3'] = 'value3'