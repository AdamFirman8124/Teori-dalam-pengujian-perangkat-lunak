

# Generated at 2022-06-13 15:38:39.522246
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    data = {}
    data['foo'] = 'bar'
    data['baz'] = {'foo': 'bar'}
    obj = AnsibleJ2Vars()
    assert(obj['foo'] == 'bar')
    assert(obj['baz']['foo'] == 'bar')

# Generated at 2022-06-13 15:38:49.906691
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    class MockTemplar:
        available_variables = dict(var1='mock', var2='mock')

    class MockTemplar2:
        available_variables = dict(var2='mock', var3='mock')

    # Test existing variable
    vars_obj = AnsibleJ2Vars(MockTemplar(), dict(), dict(var1='mock'))
    assert 'var1' in vars_obj

    # Test non-existing variable
    vars_obj = AnsibleJ2Vars(MockTemplar(), dict(), dict())
    assert 'var1' not in vars_obj

    # Test that variable from parent Templar is found
    vars_obj = AnsibleJ2Vars(MockTemplar(), dict(), dict())
    assert 'var2' in vars_

# Generated at 2022-06-13 15:39:00.606022
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import jinja2

    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars

    # Create a simple jinja2 env
    j2_env = jinja2.Environment(undefined=jinja2.StrictUndefined)

    hostvars = HostVars(host_name='localhost')
    hostvars.update({'v': 'foo'})

    globals={
        'v': 'ok',
        'hostvars': hostvars,
        'missing_var': missing,
    }
    
    # Create a templar with a jinja2 env
    templar = Templar(loader=None, variables=None, jinja2_env=j2_env)

    # Test variables
    variables = dict()

# Generated at 2022-06-13 15:39:06.996196
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    var = AnsibleJ2Vars(None, None, None)
    
    assert 'test' not in var
    assert 'test' not in var._locals
    assert 'test' not in var._templar.available_variables

    var._locals['test'] = 'test'
    assert 'test' in var
    assert 'test' in var._locals
    assert 'test' not in var._templar.available_variables

    var._templar.available_variables['test'] = 'test'
    assert 'test' in var
    assert 'test' in var._locals
    assert 'test' in var._templar.available_variables

    var._globals['test'] = 'test'
    assert 'test' in var
    assert 'test' in var._locals

# Generated at 2022-06-13 15:39:18.361221
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    globals = {'g_arg1': 123}

    locals = {'l_arg1': 123, 'l_arg2': "abc", 'arg2': "efg"}

    templar = Templar(loader=None)

    t = AnsibleJ2Vars(templar, globals, locals)
    len(t)
    gen = t.__iter__()
    assert next(gen) == 'l_arg1'
    assert next(gen) == 'l_arg2'
    assert next(gen) == 'arg2'
    assert next(gen) == 'g_arg1'
    #assert next(gen) == 'arg1'
    try:
        next(gen)
    except StopIteration as e:
        pass
    else:
        assert 1 == 2


# Generated at 2022-06-13 15:39:26.673466
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.vars.hostvars import HostVars
    from ansible.template import Templar
    from ansible.utils.unsafe_proxy import wrap_var

    globals = { 'foo': 'bar', 'baz': wrap_var('baz') }
    locals = { 'l_foo': 'bar' }
    vars = { 'bar': 'baz' }
    hostvars = HostVars(vars, False, False)

    # Templar is not initalized, no variables should be allowed
    proxy = AnsibleJ2Vars(Templar(loader=None), globals, locals)
    assert 'foo' not in proxy
    assert 'l_foo' not in proxy
    assert 'bar' not in proxy
    assert 'baz' not in proxy

    # Templar is initalized, variables should be

# Generated at 2022-06-13 15:39:33.111267
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    templar = ""
    globals = dict()
    locals = None
    ajv = AnsibleJ2Vars(templar, globals, locals)

    if(ajv.__contains__ ("foo")):
        print("Test AnsibleJ2Vars.__contains__(): Pass")
    else:
        print("Test AnsibleJ2Vars.__contains__(): Fail")
        assert False


# Generated at 2022-06-13 15:39:43.025479
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    import sys
    import pytest
    from ansible.errors import AnsibleError
    from ansible.vars.hostvars import HostVars
    templar = Templar()
    globals = {'foo':'bar'}
    locals = {'hi':'bye'}
    ajv = AnsibleJ2Vars(templar, globals, locals)
    assert ajv['foo'] == globals['foo']
    assert ajv['hi'] == locals['hi']
    assert ajv['foo'] == 'bar'
    assert ajv['hi'] == 'bye'
    assert ajv['vars'] == templar.available_variables
    # if variable not in locals, globals and available_variables, KeyError should be raised

# Generated at 2022-06-13 15:39:48.468391
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import json
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.template import Templar

    # Note: in ansible.template.__init__ , Templar.available_variables is a dict
    templar = Templar(loader=None)

    # Note: in ansible.template.__init__ , Templar._available_variables is a dict
    templar._available_variables = dict(
        var_unicode_from_yaml=AnsibleUnicode(value='/path/from/yaml/file'),
        var_from_yaml=dict(sub_var_from_yaml='sub_value')
    )

    globals = dict(
        json=json,
        var_from_module='var_from_module'
    )


# Generated at 2022-06-13 15:39:53.450350
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from ansible.template import Templar
    globals = {'a': 1, 'b': 2}

    vars = AnsibleJ2Vars(Templar(None, None), globals)
    assert (vars.get('a') == 1)
    assert (vars.get('b') == 2)
    assert (vars.get('c') is None)

# Generated at 2022-06-13 15:40:06.444359
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    templar = Templar(loader=None)
    ansible_j2_vars = AnsibleJ2Vars(templar, globals={2:3})
    assert 2 in ansible_j2_vars
    assert ansible_j2_vars[2] == 3
    ansible_j2_vars = AnsibleJ2Vars(templar, globals={'a':2})
    assert 'a' in ansible_j2_vars
    assert ansible_j2_vars['a'] == 2
    ansible_j2_vars = AnsibleJ2Vars(templar, globals={'a':2}, locals={'b':{'c':4}})
   

# Generated at 2022-06-13 15:40:17.079964
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.hostvars import HostVars
    import os
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.utils.vars import combine_vars

    test_dir = os.path.dirname(os.path.realpath(__file__))
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader, variable_manager, host_list=test_dir + "/../../inventory/hosts")
    variable_manager.set_inventory(inventory)

# Generated at 2022-06-13 15:40:24.497988
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    templar = Templar(loader=None, variables={'a': 'A'})
    vars = AnsibleJ2Vars(templar, globals={'b': 'B'}, locals={'l_c': 'C'})
    assert vars['a'] == 'A'
    assert vars['b'] == 'B'
    assert vars['c'] == 'C'
    assert 'd' not in vars
    try:
        vars['d']
    except KeyError:
        pass
    else:
        raise Exception('KeyError expected')

# Generated at 2022-06-13 15:40:30.658821
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import wrap_var
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.vars.unsafe_proxy import AnsibleUnsafeBytes
    from ansible.vars import HostVars
    import datetime

    t = Templar(None, loader=None)

# Generated at 2022-06-13 15:40:32.283892
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    ansiblej2vars = AnsibleJ2Vars(None, {}, {})
    try:
        assert '123' in ansiblej2vars
        assert ansiblej2vars['123'] is None
    except KeyError as e:
        assert e is not None


# Generated at 2022-06-13 15:40:38.886426
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.playbook.play import Play
    from ansible.template import Templar
    templar = Templar(loader=None, variables={})
    p = Play().load({}, loader=None, variable_manager=templar._available_variables)
    n = AnsibleJ2Vars(templar, p.get_vars(), p.get_vars())
    assert 'omg' in n


# Generated at 2022-06-13 15:40:48.376794
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    from ansible.module_utils.facts import ModuleFacts
    from ansible.utils.collection_loader import AnsibleCollectionLoader
    from ansible.module_utils.connection import ConnectionBase
    from ansible.parsing.dataloader import DataLoader

    templar = Templar(loader=DataLoader(), variables = {'hostvars': ModuleFacts(ConnectionBase()),'groups': {}})
    globals = {'foo': 'global_foo'}
    locals = {'foo': 'local_foo'}
    vars = {'foo': 'foo'}
    args = {'vars': vars}
    ansible_vars = AnsibleJ2Vars(templar, globals, locals)

# Generated at 2022-06-13 15:40:58.474615
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.vars.hostvars import HostVars

    l_vars = {"l_var1": "l_var1_value", "l_var2": "l_var2_value"}
    g_vars = {"g_var1": "g_var1_value", "g_var2": "g_var2_value"}

    templar = Templar(loader=None, variables=dict())
    templar._available_variables = {"t_var1": "t_var1_value", "t_var2": "t_var2_value"}

# Generated at 2022-06-13 15:41:07.721446
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.vars.hostvars import HostVars
    from ansible.vars import VariableManager
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar

    hostvars_var = HostVars()

    variable_manager = VariableManager()
    variable_manager.set_host_variable(host='example.org', varname='hostname', value=hostvars_var)
    variable_manager.set_host_variable(host='example.org', varname='ansible_fact', value=dict())
    variable_manager.set_host_variable(host='example.org', varname='a', value=42)

# Generated at 2022-06-13 15:41:18.391446
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    from ansible.template.safe_eval import AnsibleJ2TemplateModuleDefaults
    from ansible.template import Templar
    aj2v = AnsibleJ2Vars(Templar(module_defaults=AnsibleJ2TemplateModuleDefaults()), {}, {})
    assert len(list(aj2v.__iter__())) == 0

    aj2v = AnsibleJ2Vars(Templar(module_defaults=AnsibleJ2TemplateModuleDefaults()), {}, {'a': 1, 'b': 2})
    assert len(list(aj2v.__iter__())) == 2

    aj2v = AnsibleJ2Vars(Templar(module_defaults=AnsibleJ2TemplateModuleDefaults()), {'c': 3})

# Generated at 2022-06-13 15:41:33.455916
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template.template import Templar
    templar = Templar(loader=None, variables={'url': 'https://example.com/'})
    ansible_j2_vars = AnsibleJ2Vars(templar, globals={})

    try:
        ansible_j2_vars['test_access_unexisted_varname']
    except KeyError as e:
        assert str(e) == "undefined variable: test_access_unexisted_varname"

    ansible_j2_vars._locals['test_access_added_locals'] = 'test added locals'

    assert ansible_j2_vars['test_access_added_locals'] == 'test added locals'


# Generated at 2022-06-13 15:41:41.652563
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    locals = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
    vars = {'key4': 'value4', 'key5': 'value5', 'key6': 'value6'}
    globals = {'key7': 'value7', 'key8': 'value8', 'key9': 'value9'}
    ajv = AnsibleJ2Vars(locals, vars, globals)

    assert len(list(ajv.__iter__())) == len(locals) + len(vars) + len(globals)



# Generated at 2022-06-13 15:41:48.152476
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.vars.hostvars import HostVars

    templar = Templar(loader=None, variables={'key': 'value'})
    # Test for global variables (taken from AnsibleJ2Vars._globals)
    ajv = AnsibleJ2Vars(templar, {'test_key': 'test_value'})
    assert ajv['test_key'] == 'test_value'
    # Test for local variables (taken from AnsibleJ2Vars._locals)
    # variable not available in AnsibleJ2Vars._locals
    ajv = AnsibleJ2Vars(templar, {'test_key': 'test_value'})


# Generated at 2022-06-13 15:41:59.642998
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.vars import VariableManagerOptions
    variable_manager = VariableManager()
    variable_manager_options = VariableManagerOptions()
    variable_manager.set_options(variable_manager_options)
    play_context = PlayContext()
    templar = Templar(loader=None, variables=variable_manager, shared_loader_obj=None)
    # __len__ calls iter, which also calls __contains__
    assert len(AnsibleJ2Vars(templar, {})) == 0
    assert len(AnsibleJ2Vars(templar, dict(a=1))) == 1
    # FIXME
    # assert len(AnsibleJ2V

# Generated at 2022-06-13 15:42:04.270610
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    templar = Templar()
    templar.template = lambda x: x
    templar.available_variables = {
    "a": "1"
    }
    vars = AnsibleJ2Vars(templar, {}, {})
    assert vars["a"] == "1"


# Generated at 2022-06-13 15:42:13.267439
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    """
    method __getitem__ of class AnsibleJ2Vars is a
    replacement of dictionary getitem
    """

    from ansible.parsing.dataloader import DataLoader
    from ansible.parsing.mod_args import ModuleArgsParser
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars

    base_dir = "/path/to/"
    inventory_dir = base_dir + "inventory"
    group_vars_dir = inventory_dir + "/group_vars/"
    host_vars_dir = inventory_dir + "/host_vars/"

    loader = DataLoader()
    variable_manager = VariableManager()

# Generated at 2022-06-13 15:42:18.716752
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    templar = dict()
    globals = dict()
    locals = dict()

    ans_j2_vars = AnsibleJ2Vars(templar, globals, locals)

    assert ('name' in ans_j2_vars) == False
    globals['name'] = 'John'
    assert ('name' in ans_j2_vars) == True
    locals['name'] = 'Doe'
    assert ('name' in ans_j2_vars) == True
    templar['name'] = 'Jimmy'
    assert ('name' in ans_j2_vars) == True


# Generated at 2022-06-13 15:42:30.845753
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    globals = {}
    locals = {'hostvars': {'host1':{'v1':'v1'}, 'host2':{'v2':'v2' }, 'ansible_ssh_host': '{{v1}}' }}
    j2vars = AnsibleJ2Vars(globals, locals)
    print(j2vars)

    import ansible.inventory
    inventory = ansible.inventory.Inventory("/etc/ansible/hosts")
    inventory.parse_inventory(inventory.host_list)

    print(inventory)
    print (inventory.hosts)
    print (inventory.get_host(inventory.host_list[0]).get_vars())
    print ("inventory.get_host.get_vars().__dict__ ")

# Generated at 2022-06-13 15:42:36.667992
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import UNSAFE_PROXY
    from ansible.template.safe_eval import safe_eval
    
    assert AnsibleJ2Vars(Templar(), {})
    my_hostvars = HostVars({"machinetype": "Unknown"}, {})
    my_hostvars1 = HostVars({"machinetype": "Unknown"}, {})
    my_hostvars2 = HostVars({"machinetype": "Unknown"}, {})
    my_unsafe_proxy = UNSAFE_PROXY(my_hostvars, "machinetype")

# Generated at 2022-06-13 15:42:37.247780
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    assert 1==1

# Generated at 2022-06-13 15:42:50.590080
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    class Templar():
        available_variables = {
            "variable_one": 1,
            "variable_two": 2,
        }
        def template(self, var):
            return var

    class Local():
        def __init__(self):
            self["local_one"] = 1

    class Global():
        def __init__(self):
            self["global_one"] = 1

    local = Local()
    globalj2 = Global()
    ansiblej2vars = AnsibleJ2Vars(Templar(), globalj2, locals=local)
    assert "local_one" in ansiblej2vars
    assert "variable_one" in ansiblej2vars
    assert "variable_two" in ansiblej2vars
    assert "global_one" in ansiblej2vars

# Generated at 2022-06-13 15:42:54.880560
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template.template import Templar
    templar_obj = Templar(loader=None, variables={'test': 'foo'})
    ansible_vars = AnsibleJ2Vars(templar_obj, globals={}, locals={'test': 'bar'})
    assert 'test' in ansible_vars


# Generated at 2022-06-13 15:43:04.605347
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.module_utils.common.removed import removed
    from ansible.module_utils.common.collections import ImmutableDict

    known_vars = {
        'foo': 'bar',
        'boo': 'far',
    }

    known_locals = {
        'l_qux': 'baz'
    }

    known_globals = {
        'g_qux': 'baz'
    }

    templar = removed.RemovedModule()

    # Simple case, read a known variable
    assert AnsibleJ2Vars(templar, known_globals, locals=known_locals)['g_qux'] == 'baz'

# Generated at 2022-06-13 15:43:13.378844
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    from jinja2 import DictLoader

    # Make variables to psuedo-template
    var1 = {'var1': '{{foo}}'}
    var2 = {'var2': '{{foo}}'}
    var3 = {'var3': '{{foo}}'}

    # Create templar and an AnsibleJ2Vars object to test with
    templar = Templar(loader=DictLoader({}))
    templar.set_available_variables(var1)
    j2vars = AnsibleJ2Vars(templar, var2)

    # Test __contains__ with a variable that should be found in locals
    assert 'foo' in j2vars

    # Test __contains__ with a variable that should be found in the Templar

# Generated at 2022-06-13 15:43:20.436677
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    templar = Templar(None)
    globals = {'hostvars': {'a': {'b': 1}}}
    ansible_vars = AnsibleJ2Vars(templar, globals)
    assert ansible_vars['hostvars'] == {'a': {'b': 1}}


# Generated at 2022-06-13 15:43:30.046351
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars

    variable_manager = VariableManager()
    loader = DataLoader()
    variable_manager.extra_vars = {'hostvars': u'world'}
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager.set_inventory(inventory)
    play_context = PlayContext()
    templar = Templar(loader=loader, variables=variable_manager,
                      shared_loader_obj=loader)

    my_AnsibleJ2Vars = Ansible

# Generated at 2022-06-13 15:43:41.256112
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    # Create a AnsibleJ2Vars object
    j2vars = AnsibleJ2Vars(None, None, None)

    # Create a variable key/value pair
    varname = "test_var"
    value = "test_value"

    # Add the key/value pair to the AnsibleJ2Vars locals
    j2vars._templar.available_variables[varname] = value
    j2vars._locals[varname] = value

    # Assert that the key is present in the object keys
    assert varname in j2vars

    # Assert that the key is present in the object locals
    assert varname in j2vars._locals

    # Assert that the key is present in the object available variables
    assert varname in j2vars._templar.available_

# Generated at 2022-06-13 15:43:49.335541
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    # This variable is publicly visible and should be detected by AnsibleJ2Vars
    variable_globally_visible = 'test_value'

    # This variable is privately visible and should be detected by AnsibleJ2Vars
    _variable_privately_visible = 'test_value_2'

    # This variable does not exist and should not be detected by AnsibleJ2Vars
    variable_nonexistant = 'non_existent'

    # This dictionary is a private dictionary of variables
    locals = {
        'variable_in_locals': 'test_value_3'
    }

    # This is a mock object which simulates the Templar class

# Generated at 2022-06-13 15:43:59.655273
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    from unittest import TestCase
    import ansible.vars.hostvars
    import ansible.playbook.templar
    import ansible.template.safe_eval
    import ansible.template.template

    class MockHostVars(ansible.vars.hostvars.HostVars):
        def __init__(self, param=None):
            super(ansible.vars.hostvars.HostVars, self).__init__()

    # Unit tests

# Generated at 2022-06-13 15:44:09.221712
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    from ansible.template.safe_eval import safe_eval
    from ansible.template import Templar

    templar = Templar(None, loader=None, variables=None)
    jvars = AnsibleJ2Vars(templar, safe_eval({'JINJA2_GLOBALS': {'range': range}}))
    jvars['JINJA2_LOCALS'] = {'test1': 'test_value'}

    for var in jvars:
        assert var == 'test1' or var == 'range'
        assert jvars[var] == 'test_value' or jvars[var] == range

# Generated at 2022-06-13 15:44:22.307557
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():

    from ansible.template import Templar

    j2vars_obj = AnsibleJ2Vars(templar=Templar(), globals=dict())
    assert(not j2vars_obj.__contains__('foo'))

    assert(j2vars_obj.__contains__('hostvars') == True)
    assert(j2vars_obj.__contains__('group_names') == True)
    assert(j2vars_obj.__contains__('inventory_hostname') == True)
    assert(j2vars_obj.__contains__('play_hosts') == True)
    assert(j2vars_obj.__contains__('groups') == True)
    assert(j2vars_obj.__contains__('group_names') == True)

# Generated at 2022-06-13 15:44:28.246120
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    templar = Templar()
    globals = {}
    j2vars = AnsibleJ2Vars(templar, globals, locals=None)
    ['foo', 'bar', 'baz', 'quux']
    j2vars._templar.available_variables = {}
    assert 'foo' not in j2vars
    assert 'bar' not in j2vars
    assert 'baz' not in j2vars
    assert 'quux' not in j2vars
    j2vars._templar.available_variables = {'foo': None}
    assert 'foo' in j2vars
    j2vars._templar.available_variables = {'foo': None, 'bar': None}
    assert 'foo' in j2

# Generated at 2022-06-13 15:44:28.873135
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    pass

# Generated at 2022-06-13 15:44:41.020835
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
   from ansible.parsing import DataLoader
   from ansible.template import Templar
   from ansible.vars import VariableManager

   dataloader = DataLoader()
   vm = VariableManager()
   myvars = dict(a='a', b='b', test_var='test_val')
   vm.set_vars(myvars)
   vm.set_inventory(dataloader.load_inventory('ansible/tests/unit/inventory.yml'))
   #myvars = vm.get_vars()

   templar = Templar(loader=dataloader, variables=vm)


# Generated at 2022-06-13 15:44:51.245473
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():

    from ansible.template import Templar

    templar = Templar(loader=None)

    globals_ = dict(a=1, b=2, c=3)
    locals = dict(d=4, e=5, f=6)

    obj = AnsibleJ2Vars(templar, globals_, locals)

    for i in globals_:
        assert i in obj

    for i in locals:
        assert i in obj

    assert 'd' in obj
    assert 'e' in obj
    assert 'f' in obj

    assert 'a' in obj
    assert 'b' in obj
    assert 'c' in obj

    assert 'g' not in obj
    assert 'h' not in obj
    assert 'i' not in obj



# Generated at 2022-06-13 15:44:59.295466
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.parsing.vault import VaultAES256
    from ansible.template.vars import AnsibleJ2Vars, Templar

    templar = Templar(vault_password=VaultAES256('NOT A REAL PASSWORD'))
    j2vars = AnsibleJ2Vars(templar, globals={})
    assert j2vars['missing'] == None
    assert j2vars['vars'] == {}

    templar = Templar(vault_password=None, available_variables={'missing': None})
    j2vars = AnsibleJ2Vars(templar, globals={})
    assert j2vars['missing'] == None


# Generated at 2022-06-13 15:45:08.569434
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import jinja2
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars

    # Case 1.
    # Test that AnsibleJ2Vars.__contains__ really associates local variables to their name
    # and not to their variables.
    ansible_var_name = "local_var"
    local_var = "local_var_value"
    locals = {ansible_var_name: local_var}
    j2vars = AnsibleJ2Vars(Templar, {}, locals)
    assert j2vars.__contains__(ansible_var_name)

    # Case 2.
    # Test that AnsibleJ2Vars.__getitem__ work with Jinja2 built-in variables.
    ansible_var_name = "loop"


# Generated at 2022-06-13 15:45:14.716887
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar

    dummy_val = 'dummy_val'
    dummy_varname = 'dummy_varname'

    templar = Templar()
    globals = {}
    locals = {dummy_varname: dummy_val}
    j2_vars = AnsibleJ2Vars(templar, globals, locals)

    assert j2_vars[dummy_varname] == dummy_val

# Generated at 2022-06-13 15:45:22.608668
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import os
    import tempfile
    import filecmp

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.template import Templar

    # generate test data
    #   1. testdata1: a dictionary of variables
    #   2. testdata2: a dictionary containing the dictionary of variables
    testdata = dict()
    testdata["testvars"] = dict()
    testdata["testvars"]["testvar1"] = "testvalue1"
    testdata["testvars"]["testvar2"] = "testvalue2"
    testdata["testdict"] = dict()
    testdata["testdict"]["testdict1"] = dict

# Generated at 2022-06-13 15:45:34.563091
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    # test __getitem__(self, varname)
    # func type: builtin_function_or_method (builtin), with inheritance
    # Test adding locals which existing keys in templar.
    from ansible.template import Templar
    templar = Templar(loader=None)
    templar._available_variables = {'a': 1}
    j2vars = AnsibleJ2Vars(templar, {'b': 2})
    assert j2vars['a'] == 1
    assert j2vars['b'] == 2
    j2vars.add_locals({'a': 3, 'b': 4})
    assert j2vars['a'] == 3
    assert j2vars['b'] == 4
    # Test choose available_variables when only key in locals and available_variables.

# Generated at 2022-06-13 15:45:49.529712
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template.safe_eval import safe_eval
    import os
    import tempfile

    j2_vars = AnsibleJ2Vars(safe_eval, {}, locals={'l_foo': 'foo', 'l_bar': 'bar'},)

    # check with defined variable
    assert j2_vars['l_foo'] == 'foo'

    # check with undefined variable
    try:
        j2_vars['undefined']
        assert False
    except KeyError:
        pass

    # check variable contains unsafe values
    dummy_file, test_file = tempfile.mkstemp(dir=os.getcwd(), prefix='test')
    os.close(dummy_file)
    os.unlink(test_file)

# Generated at 2022-06-13 15:46:00.943241
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['tests/ansible/inventory/test_inventory.yml'])
    variable_manager.set_inventory(inventory)

    templar = Templar(loader=loader, variables=variable_manager)
    vars = AnsibleJ2Vars(templar, globals=dict(), locals=dict())

    var1 = vars['groups']

# Generated at 2022-06-13 15:46:06.027290
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    tmpl_obj = 'invalid'
    globals_obj = 'invalid'
    test_obj = AnsibleJ2Vars(tmpl_obj, globals_obj)

    with pytest.raises(KeyError):
        test_obj.__getitem__('invalid')

# Generated at 2022-06-13 15:46:11.134456
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    templar = Dummy_Templar()
    globals = {'g_foo':'bar'}
    locals_1 = {'l_foo':'bar'}
    locals_2 = {'foo':'bar'}
    vars_1 = AnsibleJ2Vars(templar, globals, locals=locals_1)
    assert ( vars_1['l_foo'] == 'bar' )
    assert ( vars_1['foo'] == 'bar' )
    assert ( vars_1['g_foo'] == 'bar' )
    vars_2 = AnsibleJ2Vars(templar, globals, locals=locals_2)
    assert ( vars_2['l_foo'] == 'bar' )
    assert ( vars_2['foo'] == 'bar' )

# Generated at 2022-06-13 15:46:14.807025
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():

    # This test is no longer possible as AnsibleJ2Vars is now a Mapping.

    # # Create a Templar() object
    # templar = Templar(loader=None)

    # # Create a dummy set of globals
    # globals_hash = dict()

    # # Create an instance of AnsibleJ2Vars
    # ajv = AnsibleJ2Vars(templar, globals_hash)

    # # Check that it contains a nonexistent key
    # assert 'nonexistent_key' not in ajv

    return

# Generated at 2022-06-13 15:46:23.926981
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    from ansible.parsing.splitter import parse_kv
    from ansible.utils.vars import combine_vars

    # Test empty class object
    templar = Templar(loader=None, variables={})
    globals = {}
    locals = {}
    ansible_j2_vars = AnsibleJ2Vars(templar, globals, locals)
    assert 'DEBUG' not in ansible_j2_vars
    assert 'FAILED' not in ansible_j2_vars
    assert 'ansible_foo_bar' not in ansible_j2_vars

    # Test single class object
    templar = Templar(loader=None, variables={'ansible_foo_bar': 'baz'})
    globals = {}

# Generated at 2022-06-13 15:46:25.274442
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    pass


# Generated at 2022-06-13 15:46:35.132509
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.vars import VariableManager
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.inventory.host import Host

    vm = VariableManager()
    vm.add_host_vars(Host(name='localhost'), {'foo': AnsibleUnicode('1')})

    ans_j2_vars = AnsibleJ2Vars(templar=VariableManager(), globals={'foo2': '2'}, locals={'foo3': '3'})

    print(ans_j2_vars['foo'])
    print(ans_j2_vars['foo2'])
    print(ans_j2_vars['foo3'])


if __name__ == '__main__':
    test_AnsibleJ2Vars___getitem__()

# Generated at 2022-06-13 15:46:36.616097
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    assert False, "No implemented"


# Generated at 2022-06-13 15:46:46.816054
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar

    my_dict = dict()
    my_templar = Templar(loader=None)
    my_globals = dict()

    my_J2Vars = AnsibleJ2Vars(my_templar, my_globals, locals=my_dict)

    #Variable not in locals, globals, or available_variables:
    assert 'foo' not in my_J2Vars
    #Variable in locals:
    my_dict['foo'] = 'bar'
    assert 'foo' in my_J2Vars
    #Variable in globals:
    my_globals['foo'] = 'bar'
    assert 'foo' in my_J2Vars
    #Variable in available_variables:

# Generated at 2022-06-13 15:47:00.670840
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
  try:
    from ansible.template import Templar
  except Exception as e:
    raise AssertionError("Failed to import ansible.template.Templar: %s" % str(e.message))
  templar = Templar(loader={}, variables={'name': 'world'})
  variable = templar.template('Hello {{name}}!')
  assert variable == 'Hello world!', 'variable == %s' % variable
  wrapped_templar = AnsibleJ2Vars(templar, dict())
  name = 'world'
  variable = wrapped_templar['name']
  assert variable == 'world', 'variable == %s' % variable

# Generated at 2022-06-13 15:47:08.511528
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    locals = {'s1': 1, 's2': 2, 's3': 3}
    variables = {'v1': 'V1', 'v2': 2, 'v3': 3.0, 'v4': None }
    globals = {'g1': 'G1', 'g2': 2, 'g3': 3.0, 'g4': None }
    templar = None

    j2 = AnsibleJ2Vars(templar, globals, locals)

    assert('s1' in j2)
    assert('s4' not in j2)
    assert('v1' in j2)
    assert('v4' in j2)
    assert('g1' in j2)
    assert('g4' in j2)


# Generated at 2022-06-13 15:47:14.378838
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    loader = DataLoader()
    context = PlayContext()
    templar = Templar(loader=loader, variables=dict(foo='bar'))
    vars = AnsibleJ2Vars(templar, dict(), dict(baz='boo'))

    assert 'foo' in vars
    assert 'baz' in vars
    assert 'not_defined' not in vars

# Generated at 2022-06-13 15:47:21.987130
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    vars_manager = VariableManager()
    templar = Templar(loader=None, variables=vars_manager)
    vars = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
    ansible_j2_vars = AnsibleJ2Vars(templar, vars)
    assert sorted(ansible_j2_vars.keys()) == ['k1', 'k2', 'k3']

# Generated at 2022-06-13 15:47:30.853410
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    templar = Templar()
    variables = dict()
    from ansible.template import generate_ansible_template_vars
    globals = generate_ansible_template_vars(variables)
    ansible_j2vars = AnsibleJ2Vars(templar, globals)
    # case 1
    key = "ansible_ssh_user"
    value = ansible_j2vars[key]
    assert value == "root"

    # case 2
    key = "var"
    value = ansible_j2vars[key]
    assert value == "test-var"

    # case 3
    key = "blah"
    try:
        value = ansible_j2vars[key]
    except KeyError as e:
        assert e

# Generated at 2022-06-13 15:47:41.765353
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    '''
    Test AnsibleJ2Vars constructor
    '''

    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar

    hostvars = HostVars({"_ansible_no_log": True, "foo": "bar"})
    variable_manager = VariableManager(loader=None)
    variable_manager.set_host_variable(host=None, variable=hostvars)
    variable_manager.set_nonpersistent_facts(dict())
    variable_manager.set_fact_cache(dict())

    templar = Templar(loader=None, variables=variable_manager)

    global_vars = {"foo2": "bar2"}

    # With all parameters

# Generated at 2022-06-13 15:47:43.201524
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    j2vars = AnsibleJ2Vars()

# Generated at 2022-06-13 15:47:48.846442
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    templar = Templar(_available_variables={'hello': 'world'},
                      _context=PlayContext(variables={'hello': 'world'}))

    vars_obj = AnsibleJ2Vars(templar, globals={}, locals={})
    assert 'hello' in vars_obj

# Generated at 2022-06-13 15:47:55.296659
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    v = AnsibleJ2Vars(None, None, None)
    # AnsibleJ2Vars with locals
    v = AnsibleJ2Vars(None, {'a': 1}, {'b': 2})
    assert 'a' in v
    assert v['a'] == 1
    assert 'b' in v
    assert v['b'] == 2
    # AnsibleJ2Vars without locals
    v = AnsibleJ2Vars(None, {'a': 1})
    assert 'a' in v
    assert v['a'] == 1

# Generated at 2022-06-13 15:48:06.560662
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    class Templar:
        available_variables = dict(
            a_dict=dict(a_field1='foo'),
            a_list=[dict(a_field1='foo', a_field2='bar'), dict(a_field1='foo', a_field2='bar')],
            a_complex=dict(
                dict1=dict(field1='foo'),
                dict2=dict(field2='bar')
            )
        )

    templar = Templar()
    jvars = AnsibleJ2Vars(templar, dict(a_global='foo', a_global_dict=dict(a_global_dict_field='foo')))

    assert jvars['a_global'] == 'foo'
    assert jvars['a_global_dict']['a_global_dict_field'] == 'foo'

# Generated at 2022-06-13 15:48:26.991953
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    # Make a Templar() object
    templar = Templar()

    # Make a AnsibleJ2Vars() object
    globals = {}
    platform = 'win32'
    j2_vars = AnsibleJ2Vars(templar, globals, platform)

    varname = 'vars_to_templated_string'
    variable = '{{vars_to_templated_string}}'
    templar.available_variables = {varname: variable}

    # Add the key
    var_key = '{{vars_to_templated_string}}'
    templar.set_available_variables({var_key: 'foo'})

    # Get the item
    assert j2_vars[varname] == 'foo'

# Generated at 2022-06-13 15:48:36.084305
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.template import Templar
    from ansible.template.safe_eval import safe_eval

    template_data = AnsibleUnicode('"{{ http_port | int + 1 }}"')
    t = Templar(loader=None, variables={'http_port': '5000'})
    ajv = AnsibleJ2Vars(t, {})
    result = ajv['http_port']
    expected = safe_eval(template_data, variables=ajv)
    assert(result == expected)
