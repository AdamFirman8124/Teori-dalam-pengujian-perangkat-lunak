

# Generated at 2022-06-13 15:38:47.826157
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from units.mock.loader import DictDataLoader
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.template import Templar

    # Creating fake data to represent an hosts file with just one host
    inventory = InventoryManager(loader=DictDataLoader({
        'all': {
            'hosts': {
                'host1': {},
            }
        },
    }))

    # Creating a fake variables manager with just one variable
    variables = VariableManager()
    variables.set_host_variable(host=inventory.get_host('host1'), varname='varname', value='value')

# Generated at 2022-06-13 15:38:59.707463
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template.safe_eval import unsafe_eval
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars

    class FakeHostVars(HostVars):
        def __init__(self, data=None):
            super(FakeHostVars, self).__init__(data)


    # test playground
    templar = Templar(loader=None, variables={'nested': {'item': 'nested'}})
    globals = {}

    # test locals
    locals = {'a': 'local'}
    vars = AnsibleJ2Vars(templar, globals, locals)
    assert vars[u'a'] == u'local'

    # test nested vars
    locals = {'nested': {'item': 'local'}}


# Generated at 2022-06-13 15:39:05.874631
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import ansible.playbook.play_context
    locals = {}
    pc = ansible.playbook.play_context.PlayContext()
    globals = {'foo': 'bar'}
    t = ansible.parsing.dataloader.DataLoader()
    # check if item is in locals
    my_ansible_j2_vars = AnsibleJ2Vars(t, globals=globals, locals={'foo': 'bar'})
    result = my_ansible_j2_vars.__getitem__('foo')
    assert result == 'bar'
    # check if item is in templar.available_variables
    my_ansible_j2_vars.__setitem__('foo', 'bar')
    # check if item is in globals
    result = my_ansible

# Generated at 2022-06-13 15:39:17.673160
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    # capture the output of invoking this method
    def expect_msg_1(msg):
        print("\nError was a <class 'ansible.errors.AnsibleError'>, " + msg + ".\n")
    def expect_msg_2(msg):
        print("\nError was a <class 'ansible.errors.AnsibleUndefinedVariable'>, " + msg + ".\n")
    def expect_msg_3(msg):
        print("\nError was a <class 'ansible.errors.AnsibleUndefinedVariable'>, " + msg + ": Undefined variable: 'undefined'.\n")

    # set up templar
    from ansible.template import Templar
    templar = Templar(loader=None, variables={})

    # set up available_variables

# Generated at 2022-06-13 15:39:27.392784
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    import os

    try:
        import ansible.template
        import ansible.vars.hostvars
    except ImportError:
        import lib.ansible.template as ansible_template
        import lib.ansible.vars.hostvars as ansible_vars_hostvars
        ansible_template.Template = ansible_template.Template
        ansible_vars_hostvars.HostVars = ansible_vars_hostvars.HostVars

    from ansible.template import Templar

    templar = Templar(loader=None)

    globals_ = dict()
    globals_['ansible_version'] = 'v2.0'
    globals_['ansible_check_mode'] = False
    globals_['ansible_version_info'] = [2, 0, 0.0]

# Generated at 2022-06-13 15:39:38.579222
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import sys
    import os

    #
    # Class Templar
    #
    class Templar:
        def __init__(self, available_variables):
            self.available_variables = available_variables

        def template(self, var):
            try:
                return self.available_variables[var]
            except:
                raise AnsibleUndefinedVariable(u"VARIABLE IS NOT DEFINED!")

    #
    # Vars
    #
    vars = dict(a="a", b=dict(c="c"))

    #
    # AnsibleJ2Vars
    #
    templar = Templar(vars)
    j2vars = AnsibleJ2Vars(templar, dict(), dict())

    #
    # Tests
    #
    assert j2vars["a"]

# Generated at 2022-06-13 15:39:45.414992
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar

    # Basic call to AnsibleJ2Vars.__getitem__()
    #
    # Implementation note: AnsibleJ2Vars.__getitem__() does a complex series of lookups
    # of variables, so to test it we need to create a reasonably well-populated
    # AnsibleJ2Vars instance, and then test its ability to retrieve each of the
    # variables it knows about.
    #
    # The logic below is designed to create a fully-populated AnsibleJ2Vars
    # instance, and then test it.

    # Create a config object
    from ansible.config.manager import ConfigManager
    config_manager = ConfigManager()

    # Create a data loader
    loader = config_manager.get_

# Generated at 2022-06-13 15:39:56.531310
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.vars.hostvars import HostVars
    # Case: HostVars is special, return it as-is, as is the special variable
    # 'vars', which contains the vars structure
    templar = None
    globals = {}
    locals = {}
    aj2vars = AnsibleJ2Vars(templar, globals, locals)
    assert 'vars' in aj2vars
    assert aj2vars['vars'] == {}
    assert isinstance(aj2vars['vars'], HostVars)
    assert 'template' not in aj2vars
    assert aj2vars['template'] == 'default.conf.j2'
    assert 'environment' not in aj2vars
    assert aj2vars['environment'] == 'production'

# Generated at 2022-06-13 15:40:06.141395
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.module_utils.six import string_types

    templar = Templar(loader=None, variables=None)
    # FIXME: isn't this more properly a dict?
    globals = dict()
    # FIXME: isn't this more properly a dict?
    locals = dict()

    j2vars = AnsibleJ2Vars(templar, globals, locals)

    # Test vars contains 1 key
    templar.available_variables = dict()
    templar.available_variables['var1'] = 'value1'

    assert j2vars.__contains__('var1')

# Generated at 2022-06-13 15:40:11.032512
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    import ansible.template
    # verifies that the key is found in the dict
    assert 'foo' in AnsibleJ2Vars(None, None, locals={'foo': 1})
    # verifies that the key is not found in the dict
    assert 'bar' not in AnsibleJ2Vars(None, None, locals={'foo': 1})

    # verifies that the key is found in the templar
    assert 'foo' in AnsibleJ2Vars(ansible.template.Templar(variables={'foo': 1}), None)
    # verifies that the key is not found in the templar
    assert 'bar' not in AnsibleJ2Vars(ansible.template.Templar(variables={'foo': 1}), None)

    # verifies that the key is found in the globals


# Generated at 2022-06-13 15:40:30.024863
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.plugins.loader import module_loader
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    def mock__getitem__(self, varname):
        if varname == 'vars':
            return '{"vars_key": "vars_value"}'
        elif varname == 'environment':
            return '{"environment_key": "environment_value"}'
        elif varname == 'context':
            return '{"context_key": "context_value"}'
        elif varname == 'hostvars':
            return HostVars(hostvars='{"hostvars_key": "hostvars_value"}')
        elif varname == 'unsafe':
            return

# Generated at 2022-06-13 15:40:39.877843
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template.safe_eval import compile_expression
    from ansible.utils.unsafe_proxy import AnsiibleUnsafeText
    from ansible.template import Templar

    globals = {'foo': ['bar', 'baz'], 'use_jinja': True}
    locals = {'lol': 'ok'}
    templar = Templar(loader=None, variables=globals)
    j2vars = AnsibleJ2Vars(templar, globals, locals)

    assert j2vars['lol'] == 'ok'
    assert j2vars['foo'] == ['bar', 'baz']

    globals = {'vars': {'a': 'b'}, 'use_jinja': True}
    templar = Templar(loader=None, variables=globals)
    j

# Generated at 2022-06-13 15:40:47.451733
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    """
    This unit test mock three types of variable:
    (1) HostVars
    (2) dict with key vars
    (3) dict with key value which contains the structure of vars

    """

    from ansible.vars.hostvars import HostVars
    h = HostVars(vars={'key': 'value'})
    assert isinstance(h, dict)
    assert isinstance(h, HostVars)

    # dict with key vars
    d = {'vars': {'key': 'value'}}
    assert isinstance(d, dict)

    # dict with key value which contains the structure of vars
    d = {'key': {'key': 'value'}}
    assert isinstance(d, dict)

    # dict with key value which contains the structure of vars

# Generated at 2022-06-13 15:40:48.012206
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    # TODO
    assert True



# Generated at 2022-06-13 15:40:58.102063
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader


    j2 = Templar(loader=DataLoader(), variables=VariableManager())
    j2._available_variables = {'a': {'b': '1'}, 'HostVars': HostVars(get_host_vars=lambda x,y: {'b': '2'}), 'environment': {}, 'context': {}, 'template':{}, 'inventory_hostname_short': 'host', 'hostvars': {}}
    j2._add_host_vars_from_inventory(InventoryManager(loader=DataLoader(), sources=''))



# Generated at 2022-06-13 15:41:05.690245
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    globals = {'foo2': 'bar2', 'baz': 'blah'}
    locals = {'foo1': 'bar1', 'bar2': 'baz2', 'blah': 'blihblih'}
    templar = None
    from collections import Mapping
    from ansible.module_utils.six import PY3
    if PY3:
        from collections.abc import Mapping
    assert isinstance(AnsibleJ2Vars(templar, globals, locals), Mapping)
    assert len(AnsibleJ2Vars(templar, globals, locals)) == 5



# Generated at 2022-06-13 15:41:16.474327
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.inventory.host import Host
    from ansible.playbook.play_context import PlayContext
    from ansible.template.template import Templar

    h = Host("myhostname")
    context = PlayContext()
    context._hostvars = {'myhostname': {'var': 'myhost'}}
    templar = Templar(loader=None, variables=dict())
    templar._host = h
    templar._play_context = context
    v = AnsibleJ2Vars(templar, globals={'foo': 'bar'})
    assert v['var'] == 'myhost'
    assert 'var' in v
    assert len(v) == 1
    assert 'foo' in v
    assert len(v) == 2
    assert 'bar' == v['foo']

# Generated at 2022-06-13 15:41:23.939069
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
  templar = "mock_templar"
  vars1 = {"varname" : "mock_variable"}
  vars2 = {"varname2" : "mock_variable2"}
  vars_all = dict(list(vars1.items()) + list(vars2.items()))
  globals = {"var_globals" : "globals"}
  locals = {"varname" : "mock_variable3"}
  a = AnsibleJ2Vars(templar, globals, locals)

  # test with existing varname in class
  a._templar.available_variables = vars1
  a._locals = locals
  assert a["varname"] == "mock_variable3"

  # test with existing varname in templar
  a

# Generated at 2022-06-13 15:41:35.197470
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    # ansible j2 vars
    from ansible.template.safe_eval import unsafe_eval
    from ansible.template.templar import Templar
    templar = Templar(loader=None, variables={'test': 'value'})
    print(templar)

    globals = unsafe_eval("{'foo': 'bar', 'bar': 'baz'}")
    print(globals)
    print(type(globals))

    locals = unsafe_eval("{'bar': 'baz', 'baz': 'foo'}")
    print(locals)
    print(type(locals))

    ansible_j2_vars = AnsibleJ2Vars(templar=templar, globals=globals, locals=locals)

# Generated at 2022-06-13 15:41:44.186004
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    templar = Templar(loader=None)

    # case 1: varname == 'vars'
    ajv = AnsibleJ2Vars(templar, dict(), dict())
    ajv._templar.available_variables = dict(vars=dict(foo='bar'))

    ret = ajv.__getitem__('vars')
    assert ret == dict(foo='bar')

    # case 2: varname == 'hostvars'
    from ansible.vars.hostvars import HostVars
    hostvars = HostVars(loader=None, variables=dict(foo='bar'))
    ajv = AnsibleJ2Vars(templar, dict(), dict())

# Generated at 2022-06-13 15:41:52.871905
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    templar = object()
    globals = dict()
    locals = dict()

    obj = AnsibleJ2Vars(templar, globals, locals)

    obj.__getitem__(varname='hostvars')

# Generated at 2022-06-13 15:42:02.544182
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import os
    import sys
    import unittest
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    # prep for the mock templar
    simple_vars = dict(hostvars=dict(foo='bar'))
    env = dict(path=os.environ['PATH'])
    templar = DummyTemplar(simple_vars)

    # prep for the mock J2Vars
    globals = dict(template='template.j2', environment=env)
    locals = dict(l_var1='value1', l_var2='value2')

    # create the J2Vars object

# Generated at 2022-06-13 15:42:12.114620
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.parsing.vault import VaultLib
    from ansible.templating import Templar
    from ansible.vars import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    vault_secrets = {"pass": "secret", "another_secrets": {"pass2": "secret2"}}
    vault_secrets_file = "../tests/vault_files/expect_success.yml"
    vault_secrets_file_pwd = "../tests/vault_files/expect_success.txt"

# Generated at 2022-06-13 15:42:16.002201
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    v = AnsibleJ2Vars(VariableManager(loader=DataLoader()).get_vars(loader=DataLoader()), {})
    assert len(v) == 0

# Generated at 2022-06-13 15:42:26.186988
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    import json
    import os
    import yaml

    v = AnsibleJ2Vars()

    # todo: add modules/utility scripts to test_templates folder
    yml_file = './test_templates/test.yml'
    j2_file = './test_templates/test.j2'
    tmpl_file = './test_templates/test.tmpl'

    with open(yml_file) as f:
        yml_config = yaml.safe_load(f)

    with open(j2_file) as f:
        j2_template = f.read()

    import ansible.template as template
    t = template.Templar(loader=None)
    t.environment = t.environment.overlay()

# Generated at 2022-06-13 15:42:33.874555
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.template import Templar

    # dict with one element
    data = {'a':5}
    templar = Templar(None)
    templar.available_variables = data
    j2vars = AnsibleJ2Vars(templar, None)
    assert len(j2vars) == len(data)

    # dict with two element
    data = {'a':5, 'b':6}
    templar = Templar(None)
    templar.available_variables = data
    j2vars = AnsibleJ2Vars(templar, None)
    assert len(j2vars) == len(data)

# Generated at 2022-06-13 15:42:41.790334
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    play_context = PlayContext()
    templar = Templar(loader=None, variables={}, fail_on_undefined=True)
    env = AnsibleJ2Vars(templar, {'foo': 'bar'})

    env.add_locals({})
    env.add_locals({'foo': 'baz'})

    assert env['foo'] == 'baz'

    with pytest.raises(KeyError):
        env['bar']


# Generated at 2022-06-13 15:42:49.684140
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.parsing.yaml.objects import AnsibleUnicode

    templar = AnsibleJ2Vars(None, globals=dict(), locals=dict())

    variables = dict()
    variables['list'] = [1, 2, 3]
    variables['list_var'] = AnsibleUnicode('{{ test_list }}')
    templar.available_variables = variables

    # both 'list' and 'list_var' should be resolved correctly
    assert templar['list'] == [1, 2, 3]
    assert templar['list_var'] == [1, 2, 3]

# Generated at 2022-06-13 15:42:52.833109
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import Ansi

# Generated at 2022-06-13 15:43:02.630233
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    from ansible.vars.unsafe_proxy import UnsafeProxy
    templar = Templar(loader=None)
    globals = {'foo': UnsafeProxy({'a': 1}), 'bar': 2}

    vars = AnsibleJ2Vars(templar, globals)

    # Check if var present
    assert 'bar' in vars
    assert 'foo' in vars
    assert 'foo_a' in vars
    assert 'foo_a_1' not in vars

    # Check if the value of var is returned
    assert vars['bar'] == 2
    assert vars['foo'] == {'a': 1}
    assert vars['foo_a'] == 1

# Generated at 2022-06-13 15:43:13.548662
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    from ansible.template import Templar

    t = Templar(loader=None)
    globals = dict()
    aj2v = AnsibleJ2Vars(templar=t, globals=globals, locals=None)

    assert iter(aj2v)



# Generated at 2022-06-13 15:43:25.818903
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    templar = Templar(None, None)
    temporary_hostvars = {'hostvars': {'localhost': {'ansible_hostname': 'localhost'}}}
    globals = {'l_hostvars': {'localhost': {'ansible_hostname': 'localhost'}}}
    locals = {'l_hostvars': {'localhost': {'ansible_hostname': 'localhost'}}}
    vars = AnsibleJ2Vars(templar, globals, locals)
    assert 'hostvars' not in vars
    assert 'localhost' not in vars
    assert 'ansible_hostname' not in vars


# Generated at 2022-06-13 15:43:33.386101
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    globals = {'hostvars': {}, 'group_names': [], 'groups': {}}
    locals = {'l_foo': 'bar'}
    vars = {'foo': 'bar', 'baz': 'qux'}
    templar = Templar(loader=None, variables=vars)
    j2vars = AnsibleJ2Vars(templar, globals, locals)
    assert 'foo' in j2vars
    assert 'bar' not in j2vars


# Generated at 2022-06-13 15:43:44.408203
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.vars import Templar
    from ansible.template import Templar as TemplarOld
    from ansible import constants
    from ansible.parsing.vault import VaultLib
    from ansible.template.safe_eval import safe_eval

    my_env = dict()
    my_vars = dict()
    my_globals = dict()
    my_templar = Templar(my_env, my_vars, constants=constants)
    my_templar_old = TemplarOld(my_env, my_vars, my_globals,
                                vault_password=None,
                                templar=my_templar,
                                shared_loader_obj=None, no_winrm=False,
                                vault_ids=[], disable_lookup=False,
                                loader=None)

# Generated at 2022-06-13 15:43:54.327497
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    '''
    This method is testing the __getitem__ method of AnsibleJ2Vars class.
    The only way to test this method is to call the __getitem__ method using
    an existing variable. For this, let's use the variable "inventory_hostname".

    First, we need to create an instance of AnsibleJ2Vars, so let's call the
    constructor using an existing inventory hostname.
    '''
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    host = inventory.get_host("localhost")

    templar

# Generated at 2022-06-13 15:44:04.765256
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    host_vars = HostVars(dict(a=1, b=2, c=3), name="test_host")
    templar = Templar(loader=None)
    templar.set_available_variables(dict(a=11, c=33))
    globals = dict(b=22, d=44)
    locals = dict(l_c=333)
    vars = AnsibleJ2Vars(templar, globals, locals)
    assert 'a' in vars
    assert 'b' in vars
    assert 'c' in vars
    assert 'd' in vars
    assert 'x' not in vars


# Generated at 2022-06-13 15:44:12.657485
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():

    from ansible.template import Templar

    templar = Templar(loader=None)
    globals = dict()
    locals = dict()
    aj2v = AnsibleJ2Vars(templar, globals, locals)

    assert [] == list(aj2v.__iter__())

    # add globals
    globals["key1"] = "value1"
    globals["key2"] = "value2"
    globals["key3"] = "value3"

    assert ["key1", "key2", "key3"] == list(aj2v.__iter__())

    # add local
    locals["key4"] = "value4"
    locals["key5"] = "value5"


# Generated at 2022-06-13 15:44:21.146771
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    import ansible.vars

    # Create a valid Templar() object
    templar = ansible.vars.UnsafeVariableManager()

    # Create an empty dictionary to add a global variable
    global_var = {}
    global_var.update(a=1)

    # Create an empty dictionary to add a local variable
    local_var = {}
    local_var.update(b=1)

    # Initialize a AnsibleJ2Vars object
    j2vars = AnsibleJ2Vars(templar, global_var, local_var)

    assert 'a' in j2vars
    assert 'b' in j2vars



# Generated at 2022-06-13 15:44:28.120367
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2022-06-13 15:44:33.674277
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    module = AnsibleModule(argument_spec = dict(
        name = dict(required=True),
    ))
    templar = Templetor(loader=None)
    vars = AnsibleJ2Vars(templar, module.params, locals=locals())
    assert 'name' in vars

# Generated at 2022-06-13 15:44:55.020161
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    ansible_j2_vars = AnsibleJ2Vars(Templar(), {}, {})
    assert 'context' not in ansible_j2_vars
    try:
        ansible_j2_vars['context']
    except KeyError:
        pass
    else:
        assert False


# Generated at 2022-06-13 15:45:06.710893
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    ''' Unit test for method __getitem__ of class AnsibleJ2Vars

    This method is called by the jinja2 templating engine in order to get values of jinja2 variables.
    '''

    from ansible.vars.hostvars import HostVars
    from ansible.template import Templar

    if not hasattr(AnsibleJ2Vars, '_getitem_called'):
        AnsibleJ2Vars._getitem_called = 0

    AnsibleJ2Vars._getitem_called += 1  # for first test case

    templar = Templar(loader=None, variables={})

    # case 1
    # just to test that the __getitem__ is called the right number of times
    # the interesting test case are coming next

# Generated at 2022-06-13 15:45:13.071962
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    from collections import OrderedDict
    class Templar:
        available_variables = OrderedDict(a=1,b=2,c=3,d=4)
        def template(self, x):
            return x

    vars = AnsibleJ2Vars(Templar(), {})
    assert list(iter(vars)) == list("abcd")


# Generated at 2022-06-13 15:45:19.530095
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    import ansible.template
    templar = ansible.template.AnsibleTemplar(loader=None).templar

    # Test __init__(self, templar, globals)
    print("Test __init__(self, templar, globals)")
    vars = AnsibleJ2Vars(templar, globals={'foo1': 'bar1'})
    assert vars['foo1'] == 'bar1'

    # Test __init__(self, templar, globals, locals)
    print("Test __init__(self, templar, globals, locals)")
    vars = AnsibleJ2Vars(templar, globals={'foo1': 'bar1'}, locals={'foo2': 'bar2'})

# Generated at 2022-06-13 15:45:32.432015
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.parsing.vault import VaultLib
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager

    vault = VaultLib()
    templar = Templar(
        vault_secrets=vault,
        loader=None,
        variables=VariableManager()
    )

    j2vars = AnsibleJ2Vars(templar, {})
    assert len(j2vars) == 0

    templar.set_available_variables({
        'key': 'value'
    })
    assert len(j2vars) == 1

    j2vars = AnsibleJ2Vars(templar, {'key': 'value'})
    assert len(j2vars) == 1

# Generated at 2022-06-13 15:45:40.163789
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    """
    AnsibleJ2Vars: __getitem__ method Unit Test
    """

    hostvars = {'hostvars': {'hosta': {'var': 'value'}}}
    templar = 'templar'
    globals = {'globals': 'global'}
    locals = {'locals': 'local'}

    # instantiate the object
    obj = AnsibleJ2Vars(templar, globals, locals)

    # varname in _locals
    varname = 'locals'
    result = obj.__getitem__(varname)
    assert result == locals[varname]

    # varname in _templar.available_variables
    varname = 'hostvars'
    obj._templar.available_variables = hostvars
   

# Generated at 2022-06-13 15:45:49.963477
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    # Templar is needed by class AnsibleJ2Vars
    class Templar(object):
        def __init__(self, variables=None):
            self.available_variables = variables

    # Create a new instance of AnsibleJ2Vars
    obj = AnsibleJ2Vars(Templar({'test1_item': 'test1_value'}), {'test2_item': 'test2_value'}, {'l_test3_item': 'test3_value'})

    # Check 'test1_item'
    assert 'test1_item' in obj

    # Check 'test2_item'
    assert 'test2_item' in obj

    # Check 'test3_item'
    assert 'test3_item' in obj

    # Check 'undefined_item'
    assert 'undefined_item'

# Generated at 2022-06-13 15:46:01.432841
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar

    templar = Templar()

    # noinspection PyUnresolvedReferences
    data = {
        'a': 1,
        'b': {'c': 2, 'd': 3}
    }

    # noinspection PyUnresolvedReferences
    data_vars = {
        'a': 'VA',
        'b': 'VB',
        'c': 'VC'
    }

    data_vars_only = {
        'a': 'VA',
        'b': 'VB',
        'c': 'VC'
    }

    data_context = {
        'context': {
            'a': 1,
            'b': {'c': 2, 'd': 3}
        }
    }


# Generated at 2022-06-13 15:46:02.900669
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    assert False, "The test needs an implementation"


# Generated at 2022-06-13 15:46:14.747789
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template.template import Templar
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import UnsafeProxy
    import collections

    templar = Templar(loader=None)
    aj2vars = AnsibleJ2Vars(templar, globals={'globals': 1})
    try:
        aj2vars['globals']
    except KeyError:
        assert False, 'AnsibleJ2Vars can not access "globals"'
    aj2vars['vars'] = {'vars': 2}
    try:
        aj2vars['vars']
    except KeyError:
        assert False, 'AnsibleJ2Vars can not access "vars"'

# Generated at 2022-06-13 15:46:39.698761
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    t = Templar(loader=None)
    v = AnsibleJ2Vars(t, globals={'g': 'g'})
    assert 'g' in v
    assert 'h' not in v
    assert v.get('h') is None
    assert v.get('h', 'h') == 'h'
    # FIXME: need to test for locals, current available vars, and the vars
    # structure, but this will require pulling a lot of stuff in.
    # assert 'vars' in v
    # assert 'include_vars' in v

    v = AnsibleJ2Vars(t, globals={'g': 'g'}, locals={'l': 'l'}) # locals are ignored before jinja2 2.9
    assert 'g' in v

# Generated at 2022-06-13 15:46:50.364777
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2022-06-13 15:47:01.127439
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    class test_templar(object):
        def __init__(self):
            pass
        def template(self, val):
            return val

    class test_globals(object):
        def __init__(self):
            self.a = 1
            self.b = "string"

    class test_test_AnsibleJ2Vars(AnsibleJ2Vars):
        def __init__(self):
            self._templar = test_templar()
            self._globals = test_globals()
            self._locals = {"id":10}

    a_test = test_test_AnsibleJ2Vars()


# Generated at 2022-06-13 15:47:02.645838
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    locals={"a":"b"}
    globals={}
    globals['foo'] = 'bar'
    templar = object
    obj = AnsibleJ2Vars(templar, globals, locals)
    assert len(obj) == 1

# Generated at 2022-06-13 15:47:09.882605
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.vars.hostvars import HostVars
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    from ansible.playbook.play_context import PlayContext
    from ansible.utils.display import Display
    import os
    import tempfile
    _config_data = {}
    _config_data['DEFAULT_MODULE_NAME'] = 'command'
    _config_data['DEFAULT_MODULE_PATH'] = None
    _config_data['DEFAULT_PLAYBOOK_PATH'] = None
    _config_data['DEFAULT_REMOTE_TMP'] = None
    _config_data['DEFAULT_REMOTE_USER'] = None
    _config_data['DEFAULT_SUDO_USER']

# Generated at 2022-06-13 15:47:16.854967
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    from ansible.template import Templar

    print ('UNIT TEST FOR CLASS AnsibleJ2Vars : METHOD __getitem__()')

    m = AnsibleJ2Vars(Templar(loader=None), dict(), dict())

    with pytest.raises(KeyError) as excinfo:
        m['undefined']
    assert 'undefined variable' in str(excinfo.value)

    assert m['vars'] == dict()

    m._templar.available_variables = {'name': 'hassan', 'age': 25, 'married': False}
    assert m['name'] == 'hassan'

    assert m['age'] == 25
    assert m['married'] == False

    m = AnsibleJ2Vars(Templar(loader=None), {'pi': 3.14}, dict())
   

# Generated at 2022-06-13 15:47:25.919296
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():

    from ansible.template.vars import AnsibleJ2Vars

    class Templar:

        def __init__(self):

            self.available_variables = dict(name=dict(key='value'))
            self.template = None

    class AnsibleJ2Globals:

        def __init__(self):

            self.my_global = str()


    globals = AnsibleJ2Globals()
    locals = dict(var1=None, another_var=None)

    vars = AnsibleJ2Vars(Templar(), globals, locals=locals)

    assert (locals.keys() == vars.keys())

    assert ('name' in vars)
    locals['name'] = 'value'
    assert ('name' in vars)

    assert ('my_global' in vars)

# Generated at 2022-06-13 15:47:31.241267
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from jinja2.utils import missing
    from ansible.template import Templar

    templar = Templar()
    item = {'localhost': None}
    globals = {'version': '1.9.4', 'inventory_hostname': 'localhost'}
    vars = AnsibleJ2Vars(templar, globals, locals=item)
    assert vars['inventory_hostname'] == 'localhost'
    assert vars['unexisting_variable'] == missing

# Generated at 2022-06-13 15:47:41.883690
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import ansible.playbook.templar
    # Create a Templar
    templar = ansible.playbook.templar.Templar()
    # Create two variables var1 and var2
    # Templating var2 to "value" because otherwise it won't be used
    templar.set_available_variables({'var1': 'value1', 'var2': 'value'})
    # Create a globals variable globvar with value "globvalue"
    globals = {'globvar': 'globvalue'}
    # Create an instance of AnsibleJ2Vars
    vars = AnsibleJ2Vars(templar, globals)
    # Check that getitem works as intended

# Generated at 2022-06-13 15:47:52.372905
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    var_manager = VariableManager()
    var_manager.extra_vars = {'a':'A', 'b':'B', 'c':'C'}
    templar = Templar(var_manager)

    ajv = AnsibleJ2Vars(templar, var_manager.extra_vars)

    assert ajv['a'] == 'A'
    assert ajv['b'] == 'B'
    assert ajv['c'] == 'C'

    # Make sure that KeyError is raised when variable is not defined
    try:
        assert ajv['d']
    except KeyError as ex:
        assert str(ex) == "undefined variable: d"

# Generated at 2022-06-13 15:48:31.924831
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import pytest
    from units.mock.loader import DictDataLoader

    t = DictDataLoader({'a': '{{b}}', 'b': '{{c}}', 'c': 42, 'no_loop': '{{no_loop}}'})
    v = AnsibleJ2Vars(t, {'no_loop': 42})

    assert isinstance(v, AnsibleJ2Vars)
    assert v['a'] == 42
    assert v['b'] == 42
    assert v['c'] == 42
    assert v['no_loop'] == 42
    with pytest.raises(KeyError) as wrapped_e:
        assert v['d'] == 42
    assert wrapped_e.type == KeyError
    assert wrapped_e.value.args == ('undefined variable: d',)