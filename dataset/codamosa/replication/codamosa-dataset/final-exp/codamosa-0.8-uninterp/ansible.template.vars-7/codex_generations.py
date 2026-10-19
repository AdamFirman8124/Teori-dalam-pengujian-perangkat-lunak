

# Generated at 2022-06-13 15:38:38.610663
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    locals = {'hostname': 'host1', 'var1': 'val1', 'var2': 'val2'}
    vars = {'hostname': 'host2', 'var2': 'val3', 'var3': 'val3'}
    globals = {'hostname': 'host3', 'var3': 'val4', 'var4': 'val4'}

    ajv = AnsibleJ2Vars(None, globals, locals)
    assert set(iteritems(locals)) == set(ajv)

    ajv = AnsibleJ2Vars(None, globals, locals=None)
    assert set(iteritems(globals)) == set(ajv)

    ajv = AnsibleJ2Vars(None, globals, locals)

# Generated at 2022-06-13 15:38:45.428125
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.template.safe_eval import safe_eval
    globals = dict()
    locals = dict()
    templar = safe_eval.Templar(loader=None)
    j2_vars = AnsibleJ2Vars(templar, globals, locals)

    assert len(j2_vars) == 0
    locals['a'] = 1
    assert len(j2_vars) == 1


# Generated at 2022-06-13 15:38:53.462419
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    ## fix error in __getitem__ of class AnsibleJ2Vars
    ## This class is only used in ansible/playbook/included_file.py line 65
    import ansible.playbook.included_file

    dict1 = dict()
    dict1['vars'] = {'item': 'item'}
    test1 = ['item', 'vars']
    for var in test1:
        from ansible.playbook.play_context import PlayContext
        from ansible.template import Templar

        templar = Templar(loader=None, variables=dict1)
        context = PlayContext()
        context._init_vars_cache()
        context.hostvars = dict1
        context.vars = dict1
        context.vars['template'] = ('vars', 'hostvars')
        context.v

# Generated at 2022-06-13 15:38:58.162847
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():

    templar = Templar()
    v = AnsibleJ2Vars(templar, {}, {})

    # Create a fake Ansible module to populate AnsibleJ2Vars
    class FakeModule:
        def __init__(self):
            self.params = {}
        def fail_json(self, **kwargs):
            pass
        def get_bin_path(self, executable):
            return "/usr/bin/%s" % executable
        def run_command(self, command):
            return (0, "mocked %s" % command, "log msg")

    mod = FakeModule()
    wrapped_mod = _AnsibleModuleWrapper(mod)

    templar.set_available_variables(wrapped_mod.get_vars(load_extra_vars=False))


# Generated at 2022-06-13 15:39:05.348924
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar

    ajv = AnsibleJ2Vars(templar=Templar(), globals={}, locals={'a_b':1, 'a_c':2, 'a_d':3, 'a_e':4})
    assert 'a_b' in ajv
    assert 'a_c' in ajv
    assert 'a_d' in ajv
    assert 'a_e' in ajv

    ajv = AnsibleJ2Vars(templar=Templar(), globals={'a_b':1, 'a_c':2, 'a_d':3, 'a_e':4}, locals={})
    assert 'a_b' in ajv
    assert 'a_c' in ajv

# Generated at 2022-06-13 15:39:17.181693
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import UnsafeProxy

    templar = Templar(loader=None, variables=VariableManager())

    # special variable
    vars_dict = {'_': 'foo'}
    vars_dict_with_unsafe = {'_': UnsafeProxy({'x': 'y'})}

    # HostVars is special
    hostvars = HostVars(loader=None, variables=None, hostname='a.b.c')

    # globals contains range
    globals = dict(range=range)

    assert 'x' not in AnsibleJ2Vars(templar, globals)

# Generated at 2022-06-13 15:39:22.049222
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from ansible.template import Templar
    templar = Templar()

    # Initialize AnsibleJ2Vars
    ad = dict()
    ad['ansible_j2vars'] = AnsibleJ2Vars(templar, dict())
    ad['ansible_j2vars'].add_locals(dict(a=10))


if __name__ == '__main__':
    test_AnsibleJ2Vars()

# Generated at 2022-06-13 15:39:29.607440
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    try:
        from ansible.template import Templar
        from ansible.vars.hostvars import HostVars
        import jinja2
    except ImportError:
        return
    templar = Templar(loader=jinja2.DictLoader(dict()), variables={'hostvars': HostVars(None, dict(key='value'))})
    dct = {'l_key': 'localized_value', 'key': 'value'}
    proxy = AnsibleJ2Vars(templar, dct, locals=dct)
    print(proxy.__contains__('key'))
    print(proxy.__contains__('l_key'))
    print(proxy.__contains__('hostvars'))
    print(proxy.__contains__('missing'))


# Generated at 2022-06-13 15:39:35.081829
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    globals = {}
    test_input = {}
    templar = {}
    test_ansiblej2vars_obj = AnsibleJ2Vars(templar, globals, test_input)
    assert test_ansiblej2vars_obj.__contains__(test_input) == 1


# Generated at 2022-06-13 15:39:44.109205
# Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2022-06-13 15:39:52.977622
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    import jinja2
    templar = jinja2.Template('')
    vars = AnsibleJ2Vars(templar, {'gvar': 'global'}, locals={'lvar': 'local'})

    keys = set(vars)
    assert 'gvar' in keys
    assert 'lvar' in keys
    assert 'undefined_var' not in keys


# Generated at 2022-06-13 15:39:58.338116
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    # initialize
    from ansible.template import Templar
    templar = Templar(loader=None, variables={})
    from ansible.vars.hostvars import HostVars
    locals = HostVars(host_name='test', host_vars={})
    globals = {'foo': 'bar'}

    # test
    vars = AnsibleJ2Vars(templar, globals, locals)
    print(vars['hostvars'])

# Generated at 2022-06-13 15:40:07.605456
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    # Available variables
    available_variables = dict()
    available_variables['test_variable'] = 'test value'
    # Template
    templar = dict()
    templar['available_variables'] = available_variables
    # Locals
    locals = dict()
    locals['test_locals'] = 'test value'
    # Globals
    globals = dict()
    globals['test_global'] = 'test value'
    # Create object
    obj = AnsibleJ2Vars(templar, globals, locals)
    # Evaluate object
    assert obj['test_variable'] == 'test value'
    assert obj['test_locals'] == 'test value'
    assert obj['test_global'] == 'test value'


# Generated at 2022-06-13 15:40:19.528435
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    import ansible.template.templar

    # Create a valid Templar object
    templar = ansible.template.templar.Templar(loader=None)

    # Create a dict of variables
    var = dict()
    var['a'] = 'a'
    var['b'] = 'b'

    # Create a dict of locals
    locals = dict()
    locals['c'] = 'c'
    locals['d'] = 'd'

    # Create a dict of globals
    globals = dict()
    globals['e'] = 'e'
    globals['f'] = 'f'

    # Create an object with valid constructor params
    obj = AnsibleJ2Vars(templar, globals, locals)

    # Check if object is not none
    assert obj is not None

    # Check if object

# Generated at 2022-06-13 15:40:29.049910
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():

    from ansible.template import Templar

    templar = Templar(loader=None)
    globals = { 'g1': 'g1', 'g2': 'g2' }
    locals = { 'l_l1': 'l1', 'l_l2': 'l2' }

    vars_obj = AnsibleJ2Vars(templar, globals, locals=locals)

    # Check if value is iterable, then check wether it contains all expected keys
    # TODO: add more checks in the future
    assert(hasattr(vars_obj.__iter__(), '__iter__'))
    assert({ 'g1', 'g2', 'l1', 'l2' }.issubset(vars_obj))

# Generated at 2022-06-13 15:40:34.814594
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.template import Templar
    globals = {'foo' : 1, 'bar' : 2, 'baz' : 3}
    locals = {'l_apple':1, 'l_orange':2}
    templar = Templar(loader=None)
    a = AnsibleJ2Vars(templar, globals, locals)
    assert len(a) == 5



# Generated at 2022-06-13 15:40:40.228627
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    templar = AnsibleJ2Vars(None, None)
    assert list(templar) == []
    templar = AnsibleJ2Vars(None, {'foo':'bar'})
    assert list(templar) == ['foo']
    templar = AnsibleJ2Vars(None, {'foo':'bar'}, locals={'baz':'quux'})
    assert list(templar) == ['foo', 'baz']

# Generated at 2022-06-13 15:40:44.502597
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():

    # Prepare test data
    av = {}
    av['1'] = 2
    gv = {}
    gv['1'] = 3
    lv = {}
    lv['1'] = 4
    ansible_vars = AnsibleJ2Vars(av, gv, lv)

    assert 1 in ansible_vars


# Generated at 2022-06-13 15:40:51.463721
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template.safe_eval import ansible_safe_eval
    from ansible.template.template import Templar

    templar = Templar(variables=dict())
    variables = dict(x=1, y=2, z=3)

    vars_object = AnsibleJ2Vars(templar, variables)

    assert 'x' in vars_object
    assert 'y' in vars_object
    assert 'z' in vars_object
    assert 'a' not in vars_object
    assert 'b' not in vars_object
    assert 'c' not in vars_object


# Generated at 2022-06-13 15:41:02.879396
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    d = {}
    d.update({"1":"a","2":"b","3":"c"})
    d.update({"4":"d","5":"e","6":"f"})
    print("Available variables in d:\n",list(d))
    ansible_j2vars = AnsibleJ2Vars({},d)
    print("Vars are going to be templated")
    for i in range(1,7):
        if str(i) in ansible_j2vars:   # Here is the important test
            print("Variable %s is available" % str(i))
            print("Value = ",ansible_j2vars[str(i)])
            print()
        else:
            print("Variable %s is not available!" % str(i))


# Generated at 2022-06-13 15:41:20.047260
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    templar = Templar(loader=None)

    # Initialize a globals dictionary
    globals = dict()
    globals['g_var1'] = 'g_var1_value'
    globals['g_var2'] = 'g_var2_value'
    globals['g_var3'] = 'g_var3_value'

    # Initialize a locals dictionary
    locals = dict()
    locals['l_var1'] = 'l_var1_value'
    locals['l_var2'] = 'l_var2_value'
    locals['l_var3'] = 'l_var3_value'

    # Initialize an available_variables dictionary
    templar.available_variables = dict()

# Generated at 2022-06-13 15:41:31.520661
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.vars.hostvars import HostVars
    import ansible.vars
    import tempfile
    import json
    tf = tempfile.NamedTemporaryFile(delete=False)
    # create a file with a valid json
    json.dump({'a': 'b'}, tf)
    tf.flush()
    tf.close()
    # create HostVars object
    hostvars = HostVars(hostvars_filename=tf.name)
    # create AnsibleJ2Vars object
    ajv = AnsibleJ2Vars(templar=None, globals=ansible.vars.__dict__, locals=None)
    # test that AnsibleJ2Vars evaluates to the HostVars instance
    assert ajv['vars'] == hostvars
    # test that Host

# Generated at 2022-06-13 15:41:41.770182
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    '''
    This test is trying to simulate the __getitem__ of the AnsibleJ2Vars
    class.
    '''
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    import datetime

    # Initialize the AnsibleJ2Vars object
    t = Templar(loader=None)
    g = {}
    l = {}

    A = AnsibleJ2Vars(t, g, l)

    # The first case 
    l['v0'] = 'test'
    assert A['v0'] == 'test'
    del l['v0']

    # The second case 
    t.set_available_variables({'v1': 'test'})

# Generated at 2022-06-13 15:41:42.927783
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    assert False, "Unit test for method __contains__ of class AnsibleJ2Vars not implemented"


# Generated at 2022-06-13 15:41:48.738820
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    templar = Templar()
    globals = {'test_globals': AnsibleUnicode('test_globals')}
    locals = {'test_locals': AnsibleUnicode('test_locals')}
    fake_host_vars = HostVars(dict())
    j2_vars = AnsibleJ2Vars(templar, globals, locals=locals)
    assert j2_vars['test_locals'] == 'test_locals'
    assert j2_vars['test_globals'] == 'test_globals'
    assert j2_vars['vars']

# Generated at 2022-06-13 15:41:59.931387
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    import jinja2

    # Test empty AnsibleJ2Vars
    assert 'test' not in AnsibleJ2Vars(jinja2.Environment(), {})

    # Test AnsibleJ2Vars that contains 'test' in locals
    assert 'test' in AnsibleJ2Vars(jinja2.Environment(), {}, {'test': 1})

    # Test AnsibleJ2Vars that contains 'test' in available_variables
    assert 'test' in AnsibleJ2Vars(jinja2.Environment(), {}, {'l_test': 1})

    # Test AnsibleJ2Vars that contains 'test' in globals
    assert 'test' in AnsibleJ2Vars(jinja2.Environment(), {'test': 1}, {'ltest': 1})

    # Test AnsibleJ2Vars that does not

# Generated at 2022-06-13 15:42:04.623847
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    # Create Templar with no data
    templar = Templar(loader=None)

    # Create instance of AnsibleJ2Vars
    aj2v = AnsibleJ2Vars(templar, globals={})

    # Call __getitem__
    aj2v['asdasd']

# Generated at 2022-06-13 15:42:13.560398
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import os
    import sys
    import unittest
    import ansible.template
    import ansible.vars
    import ansible.utils

    class Connection:
        def __init__(self):
            self.__host = None
        @property
        def host(self):
            return self.__host
        @host.setter
        def host(self, value):
            self.__host = value

    class PlayContext:
        def __init__(self):
            self.connection = Connection()
            self.remote_addr = None
            self.remote_user = None
            self.port = None
            self.become = False
            self.become_method = None
            self.become_user = None
            self.module_name = None
            self.only_tags = set()
            self.skip

# Generated at 2022-06-13 15:42:20.152987
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader


    # Create a data loader
    data_loader = DataLoader()

    # Create an inventory manager
    inventory_manager = InventoryManager('/etc/ansible/hosts', data_loader)

    # Create a variable manager
    variable_manager = VariableManager(loader=data_loader, inventory=inventory_manager)

    # Create a templar
    templar = Templar(loader=data_loader, variables=variable_manager)

    # Create a class AnsibleJ2Vars
    j2vars = AnsibleJ2Vars(templar, {}, {})

    # Make a iteration over the j2vars

# Generated at 2022-06-13 15:42:31.408277
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    templar = Templar(loader=None, variables={'v': {'foo': 'bar'}})

    def _test(vars_obj, expected_result, reason):
        actual_result = vars_obj.__contains__('v')
        assert actual_result == expected_result, 'Test of __contains__ failed; {}, actual result {}, expected result {}'.format(reason, actual_result, expected_result)

    # Test 1:
    #  vars_obj:
    #    self._locals: {}
    #    self._templar.available_variables: {v: {foo: bar}}
    #    self._globals: {}
    #  expected_result: True
    vars_obj = AnsibleJ2Vars(templar, globals={}, locals={})
    _test

# Generated at 2022-06-13 15:42:48.586954
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar

    mock_templar = Templar(loader=None)

    # test 1: "vars" variable
    mock_templar.available_variables = dict()
    mock_templar.available_variables["vars"] = dict()
    mock_templar.available_variables["vars"]["test"] = "test1"
    aj2v = AnsibleJ2Vars(mock_templar, dict())
    assert aj2v["vars"] == dict(test="test1")

    # test 2: "vars" variable
    mock_templar.available_variables = dict()
    mock_templar.available_variables["vars"] = dict()
    mock_templar.available_variables["vars"]["test"]

# Generated at 2022-06-13 15:42:58.701404
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.plugins.loader import lookup_loader
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    from ansible.parsing.vault import VaultLib
    from ansible.inventory.manager import InventoryManager
    from ansible.template.templar import Templar
    from ansible.template.vars import AnsibleJ2Vars

    hosts_file = './tests/unit/inventory/hosts'
    vault_file = './tests/unit/vault_pass.txt'
    valuted_playbook_file = './tests/unit/playbook.yml'
    inventory = InventoryManager(loader=lookup_loader, sources=[hosts_file])
    variable_manager = VariableManager(loader=lookup_loader, inventory=inventory)
   

# Generated at 2022-06-13 15:43:07.597187
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.template import Templar
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager.set_inventory(inventory)
    templar = Templar(loader=loader, variables=variable_manager)
    globals_ = dict()
    locals_ = dict()
    ansible_vars = AnsibleJ2Vars(templar, globals_, locals_)

    # not found in ansible_vars
    assert ('test_value' in ansible_vars) is False

    # found in ansible_vars

# Generated at 2022-06-13 15:43:10.024535
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    templar = AnsibleJ2Vars(templar=None, globals={'g': 'g'}, locals={'l': 'l'})
    assert 'g' in templar
    assert 'l' in templar
    assert 'z' not in templar

# Generated at 2022-06-13 15:43:12.506737
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    templar = Templar(loader=None)
    Vars = AnsibleJ2Vars(templar, dict())

    assert Vars.__contains__('var') == False
    assert Vars.__contains__('var') is not None



# Generated at 2022-06-13 15:43:25.156028
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    # Execution of "ansible-playbook --version" with ansible 2.3.1.0
    templar = "Templar (version 2.3.1.0)"
    globals = {  }

# Generated at 2022-06-13 15:43:35.210498
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    '''
    For AnsibleJ2Vars.__iter__
    '''
    from jinja2 import DictLoader
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    vault_pass = 'secret'

    # vault_password is set to None to prevent templar from
    # prompting the user for a vault password
    context = dict(
        vault_password=None,
        loader=DataLoader(),
        variables=dict(var1='test1', var2='test2', var3='test3'),
        DEFAULT_VAULT_ID_MATCH='testvault'
    )

    # create a dummy play to use for testing


# Generated at 2022-06-13 15:43:45.809463
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.hostvars import HostVars

    variable = {'v1': '{{ v2 }}', 'v2': '{{ v1 }}'}
    templar = Templar(loader=None, variables=variable)
    play_context = PlayContext()
    inventory = InventoryManager(loader=None, sources='localhost ansible_connection=local')
    globals = {'foo': 'bar'}
    locals = {}
    vars = AnsibleJ2Vars(templar, globals, locals)
    assert vars['v1'] == '{{ v2 }}'
    assert vars['v2'] == '{{ v1 }}'
    assert vars

# Generated at 2022-06-13 15:43:55.041381
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import load_extra_vars, load_options_vars, combine_vars

    variable_manager = VariableManager()
    loader = DataLoader()

    # all_vars contains the facts and variables mainly
    all_vars = variable_manager.get_vars(loader=loader, play=None)
    extra_vars = load_extra_vars(loader=loader, play=None)
    options_vars = load_options_vars(loader=loader, play=None)

    # all_vars is a composite of facts, variables, extra_vars, options_vars

# Generated at 2022-06-13 15:44:03.732858
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible import template

    # Initialize Templar with a valid set of variables
    # For the sake of the test, we'll just add a simple key:value pair
    t = template.AnsibleTemplar(variables={'testing': '123'})

    # Now create an AnsibleJ2Vars instance
    j = AnsibleJ2Vars(t, {})

    # Ensure that the __contains__ method works as expected
    assert 'testing' in j


# Generated at 2022-06-13 15:44:17.276916
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.six import PY3
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    AnsibleJ2Vars_ = AnsibleJ2Vars

    # Create a simple AnsibleJ2Vars_ object
    templar = Templar(loader=None, variables={'var1': u'var1 value'}, shared_loader_obj=None)
    globals = {'glo': u'glo value'}
    locals_ = {'var2': u'var2 value', 'var3': u'var3 value'}
    ansible_j2_vars = AnsibleJ2Vars_(templar, globals, locals_)

    # Assert

# Generated at 2022-06-13 15:44:25.681156
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.vars import VariableManager
    var_manager = VariableManager()

    globals_var = dict()
    locals_var = dict()

    # Test case 1: If a variable of name "varname" is present in both
    # self._locals, self._templar.available_variables and self._globals,
    # return True
    varname = 'templar_variable'
    globals_var[varname] = 'templar_variable'
    locals_var[varname] = 'templar_variable'
    var_manager.set_available_variables({varname: 'templar_variable'})
    ansible_j2_var = AnsibleJ2Vars(var_manager, globals_var, locals_var)
    assert ansible_j2

# Generated at 2022-06-13 15:44:37.772187
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.template import Templar
    templar = Templar(loader=None)
    globals = {}
    locals = {}
    j2_vars = AnsibleJ2Vars(templar, globals, locals)
    # without contents
    assert len(j2_vars) == 0
    # with content
    templar._available_variables = {'a': 1, 'b': 2, 'c': 3}
    globals = {'d': 4, 'e': 5, 'f': 6, 'a': 7}
    locals = {'g': 7, 'h': 8, 'i': 9, 'b': 10}
    j2_vars = AnsibleJ2Vars(templar, globals, locals)
    assert len(j2_vars) == 9

# Generated at 2022-06-13 15:44:47.515488
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    result = dict()
    # check variable 'vars'
    variable = dict()
    variable['vars'] = 'ok'
    variable['v2'] = 'ok'
    variable['var3'] = 'ok'
    templar = "templar"
    globals = dict()
    vars = AnsibleJ2Vars(templar, globals)
    for i in variable:
        result[i]=vars[i]
    assert result == variable
    # check undefined variable
    result.clear()
    variable.clear()
    try:
        result['var4']=vars['var4']
    except KeyError:
        assert True
    # check HostVars
    result.clear()
    variable.clear()
    variable['vars'] = "templar"

# Generated at 2022-06-13 15:44:55.403224
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    # test AnsibleUndefinedVariable exception
    _templar = {}
    _locals = {}
    _globals = {}
    obj = AnsibleJ2Vars(_templar, _globals, _locals)
    try:
        obj.__getitem__("undefined_varname")
    except AnsibleUndefinedVariable as auv:
        assert(auv.message == "undefined_varname")
    except:
        assert(False)
    else:
        assert(False)
    # test exception
    try:
        obj.__getitem__("undefined_varname")
    except Exception:
        assert(True)
    else:
        assert(False)
    # test HostVars
    class HostVars(object):
        pass

# Generated at 2022-06-13 15:45:06.117043
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template.safe_eval import safe_eval
    from ansible.template import Templar
    templar = Templar(loader=None)
    templar.available_variables = {'network_os': 'eos'}
    av = AnsibleJ2Vars(templar, {})
    assert 'network_os' in av
    assert 'not_in_av' not in av
    templar.available_variables = {'network_os': 'eos'}
    av = AnsibleJ2Vars(templar, {'global': 'global'})
    assert 'global' in av
    assert 'network_os' in av
    assert 'not_in_av' not in av


# Generated at 2022-06-13 15:45:17.554302
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    from ansible.vars.unsafe_proxy import wrap_var
    data={
        'a1':'a',
        'b':{
              'b2':{
                  'c': 'c'
                },
              'b3':'b3'
            },
        'l_a':'a',
        'l_b':{
              'l_b2':{
                  'c': 'c'
                },
              'l_b3':'b3'
            }
        }
    t = Templar(variables=data)
    obj = AnsibleJ2Vars(t, data)
    assert obj['a1'] == 'a'
    assert obj['b.b3'] == 'b3'
    assert obj['a'] == 'a'
    assert obj

# Generated at 2022-06-13 15:45:19.031000
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    import jinja2
    assert False, "TODO: Write this test!"


# Generated at 2022-06-13 15:45:31.999075
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.vars.hostvars import HostVars
    from ansible.vars import AnsibleVars
    from ansible.template import Templar

    templar = Templar(loader=None)
    globals = AnsibleVars(loader=None)
    locals = dict()
    proxy = AnsibleJ2Vars(templar, globals, locals)

    assert 'ansible_version' in list(proxy.keys())
    assert 'ansible_version' in proxy
    assert proxy['ansible_version'] is not None
    assert isinstance(proxy['ansible_version'], str)

    assert 'inventory_hostname' in list(proxy.keys())
    assert 'inventory_hostname' in proxy
    assert proxy['inventory_hostname'] is None

    # Test of the HostVars special case

# Generated at 2022-06-13 15:45:39.954214
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    import os
    import jinja2
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar

    variable_manager = VariableManager()
    variable_manager.extra_vars = {
        'server': 'demo.example.com',
        'web_servers': [
            'foo.example.com',
            'bar.example.com',
        ]
    }

    templar = Templar(loader=jinja2.DictLoader({}), variable_manager=variable_manager, shared_loader_search_path=VariableManager._get_loader_search_path(variable_manager))

    variables = AnsibleJ2Vars(templar, {}, {})

    # test variables
    assert 'web_servers' in variables
    assert 'server' in variables

    # test jin

# Generated at 2022-06-13 15:46:06.128198
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from ansible.template import Templar
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.vars.hostvars import HostVars
    # test variables
    templar = Templar(loader=None)
    test_vars = {
        'a': 1,
        'b': 2,
        'c': 'It works!',
        'HostVars': HostVars(),
        'ansible_vars': {
            'd': 'It works!',
            'e': AnsibleUnsafeText('It works!'),
        },
    }
    templar._available_variables = test_vars
    # init proxy
    proxy = AnsibleJ2Vars(templar, globals={'test':test_vars['ansible_vars']})
   

# Generated at 2022-06-13 15:46:10.525248
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    templar = Templar(loader=None, variables={'a': 'a', 'b': '{{a}}'})
    v = AnsibleJ2Vars(templar, globals={})
    assert 'a' in v
    assert v['a'] == 'a'
    assert 'b' in v
    assert v['b'] == 'a'
    assert 'vars' in v
    assert 'template' in v
    assert 'environment' in v
    assert 'context' not in v
    assert 'l_context' in v
    assert 'l_template' in v
    assert 'l_environment' in v

# Generated at 2022-06-13 15:46:21.128475
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import unittest
    import sys
    import os
    import tempfile
    import shutil
    import jinja2
    import ansible.constants as C
    import ansible.playbook.play
    from ansible.module_utils.common._collections_compat import Mapping

    class FakeModule(object):
        
        def __init__(self, hostname='testhost', environment={}, ran_once=False):
            self._hostname = hostname
            self._environment = environment
            self._ran_once = ran_once

        def get_hostname(self):
            return self._hostname
        
        def get_environment(self):
            return self._environment

        def ran_once(self):
            return self._ran_once


# Generated at 2022-06-13 15:46:25.703963
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    templar = Templar()
    j2vars = AnsibleJ2Vars(templar=templar, globals={})
    assert "hostvars" not in j2vars


# Generated at 2022-06-13 15:46:35.328738
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import pytest
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.templating import Templar

    # Define objects and variables for the test
    variable_manager = VariableManager()
    loader = DataLoader()
    variable_manager.set_loader(loader=loader)
    variable_manager.extra_vars = dict(var1='foo', var2='bar')

    # Create a list of variable names and their values.
    variable_names = ['var1', 'var2', 'var3', 'var4', 'var5']
    variable_values = ['foo', 'bar', '{{var1}}', '{{var3}}', '{{var4}}']
    variables = dict(zip(variable_names, variable_values))

    # Create a dict to

# Generated at 2022-06-13 15:46:41.133951
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.playbook.play_context import PlayContext
    from ansible.template.template import Templar
    from ansible.vars.hostvars import HostVars

    play_context = PlayContext()
    templar = Templar(loader=None, variables=play_context.variables)
    j2vars = AnsibleJ2Vars(templar, globals={'test': HostVars(play_context, {})})

    test_str = 'test_str'
    assert j2vars[test_str] == test_str
    assert isinstance(j2vars['test'], HostVars)

    try:
        j2vars['not_present']
    except KeyError as e:
        assert str(e) == 'undefined variable: not_present'
    else:
        assert False

# Generated at 2022-06-13 15:46:45.855773
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    from ansible.template import Templar
    variables = {'a': 1, 'b': 2, 'c': 3}
    proxy = AnsibleJ2Vars(Templar(loader=None), variables, {})
    assert (set(proxy) == set(['a', 'b', 'c']))



# Generated at 2022-06-13 15:46:51.746151
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar # We need the class Templar()
    vars = AnsibleJ2Vars(Templar(), globals=dict(), locals=dict())
    vars['name'] = 'Ansible'
    assert vars['name'] == 'Ansible'

    # Make sure vars['name'] is not a reference to the dictionary entry.
    vars['name'] = 'New Value'
    assert vars['name'] != 'Ansible'
    assert vars['name'] == 'New Value'

# Generated at 2022-06-13 15:46:52.814050
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    pass


# Generated at 2022-06-13 15:47:00.767524
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    # Setup
    templar = Templar(loader=DictDataLoader({}))
    globals = {'from_globals': 'from_globals'}
    locals = {'from_locals': 'from_locals'}

    # When
    ansible_j2_vars = AnsibleJ2Vars(templar, globals, locals)
    actual = ansible_j2_vars['from_locals']

    # Then
    assert 'from_locals' == actual



# Generated at 2022-06-13 15:47:32.569076
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    import jinja2
    from jinja2.utils import missing
    from ansible.playbook.play_context import PlayContext
    from ansible.template.template import Templar
    templar = Templar(play_context=PlayContext())
    globals = {'abc': 123}
    j2vars = AnsibleJ2Vars(templar=templar, globals=globals, locals={})
    keys = ["abc", "environment", "template", "context"]
    for key in keys:
        try:
            assert key in j2vars
        except:
            assert (False), "%s is not in the j2vars" % key


# Generated at 2022-06-13 15:47:35.689104
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from ansible import templar
    templar_obj = templar.Templar(loader=None)
    vars_obj = AnsibleJ2Vars(templar=templar_obj, globals={}, locals=None)
    assert isinstance(vars_obj, Mapping)

# Generated at 2022-06-13 15:47:38.912141
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    import pytest

    templar = '_templar'
    globals = {'_hey': 'ho'}
    locals = None

    ansibleJ2Vars = AnsibleJ2Vars(templar, globals, locals)

    assert (ansibleJ2Vars.__len__() == 1)

# Generated at 2022-06-13 15:47:44.933506
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    hostvars = HostVars(None, None)
    hostvars._data = {"foo": "bar"}
    templar = Templar(loader=None)
    templar.available_variables = {"vars": hostvars}
    globals = {}
    locals = {}

    proxy = AnsibleJ2Vars(templar, globals, locals)
    assert proxy["vars"].get_vars() is hostvars._data
    assert proxy["vars"]["foo"] == "bar"
    assert proxy["vars"]["foo"] == proxy["vars"].get_vars()["foo"]

# Generated at 2022-06-13 15:47:54.953878
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    '''
    Check AnsibleJ2Vars method __contains__
    '''
    # Unit tests do not support importing ansible.utils.template so just mock Templar
    class Templar():
        def __init__(self, available_variables):
            self.available_variables = available_variables

    av = {'var1': 'val1', 'var2': 'val2'}
    t = Templar(av)
    globals = {'var3': 'val3'}
    locals = {'var4': 'val4'}
    av_proxy = AnsibleJ2Vars(t, globals, locals)
    assert 'var1' in av_proxy
    assert 'var2' in av_proxy
    assert 'var3' in av_proxy
    assert 'var4' in av_proxy

# Generated at 2022-06-13 15:47:58.787351
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    import ansible.template.template
    templar = ansible.template.template.Templar()
    globals = {}
    locals = {}
    AnsibleJ2Vars(templar, globals, locals)


# Generated at 2022-06-13 15:48:10.322926
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    from ansible.template.safe_eval import safe_eval
    templar = Templar(loader=None, variables={})
    varname = 'varname'
    value = 'test'
    templar.set_available_variables({varname: value})
    globals = {}
    locals = {}

    ansible_j2vars = AnsibleJ2Vars(templar, globals, locals)
    ansible_j2vars_value = ansible_j2vars[varname]
    assert ansible_j2vars_value == safe_eval(value), 'assert ansible_j2vars[varname] == safe_eval(varname)'


# Generated at 2022-06-13 15:48:17.823275
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    class Templar:
        def __init__(self, available_variables):
            self.available_variables = available_variables

        def template(self):
            print('template')

    class Globals:
        def __init__(self, globals):
            self.globals = globals

    available_variables = {1:2, 3:4}
    t = Templar(available_variables)
    g = Globals({5:6})
    ajv = AnsibleJ2Vars(t, g)

    assert(1 in ajv)
    assert(3 in ajv)
    assert(5 in ajv)
    assert(7 not in ajv)



# Generated at 2022-06-13 15:48:27.430525
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    templar = Templar(None, loader=None)

    def raise_AnsibleUndefinedVariable(k):
        raise AnsibleUndefinedVariable("test")

    def getitem_test_case(test_name, globals, locals, check_name, has_key=True):
        # create an AnsibleJ2Vars instance with the given globals and locals
        vars = AnsibleJ2Vars(templar, globals, locals)
        # test the __contains__ method on the AnsibleJ2Vars instance
        if has_key:
            assert check_name in vars, "%s: %s should be in vars" % (test_name, check_name)