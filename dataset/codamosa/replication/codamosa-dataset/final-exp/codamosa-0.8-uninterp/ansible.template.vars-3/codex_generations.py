

# Generated at 2022-06-13 15:38:39.796575
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    assert AnsibleJ2Vars(templar=None,
                         globals={
                             'a': 12,
                             'b': 12,
                         },
                         locals={
                             'c': 13,
                             'd': 14,
                         }).__contains__('a')
    assert AnsibleJ2Vars(templar=None,
                         globals={
                             'a': 12,
                             'b': 13,
                         },
                         locals={
                             'c': 14,
                             'd': 15,
                         }).__contains__('b')

# Generated at 2022-06-13 15:38:43.262636
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    templar = Templar(loader=None, variables={})

    globals = {
        "test": "a",
        "test2": "b"
    }

    j2vars = AnsibleJ2Vars(templar, globals)

    assert("test2" in j2vars)
    assert("test" in j2vars)
    assert("c" not in j2vars)



# Generated at 2022-06-13 15:38:48.408649
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    from ansible.template import Templar
    from ansible.errors import AnsibleUndefinedVariable

    templar = Templar(loader=None)
    test_vars = {
        'var_correct': 'value_correct',
        'var_undefined': '{{ var_undefined }}',
        'var_incorrect': '{{ var_incorrect }}'
    }
    test_globals = {
        'var_global': 'value_global'
    }

    def test_item(item_name, expected):
        proxy = AnsibleJ2Vars(templar, test_globals, test_vars)
        for i in range(10):
            result = proxy[item_name]
            if result != expected:
                raise AssertionError('%r != %r' % (result, expected))

   

# Generated at 2022-06-13 15:38:59.872226
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():

    import json
    import jinja2

    from ansible.parsing.vault import VaultSecret

    templar = jinja2.Environment(extensions=['ansible.v2.extensions.VaultSecret'])
    templar.loader = jinja2.BaseLoader()

    vault_password = 'secret'

    # prepare range for globals
    range_min = 0
    range_max = 3
    range_step = 1

    # prepare dict for locals
    dict_key = 'locals_dict_key'
    dict_value = 'locals_dict_value'

    # prepare hosts for available_variables
    host_name = 'some_host_name'
    host_value = 'some_host_value'

    # prepare vault string for available_variables

# Generated at 2022-06-13 15:39:06.377778
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    t = Templar(loader=None, variables={'var1': 'value1'}, shared_loader_obj=None)


    # case 1: lookup works as expected
    a = AnsibleJ2Vars(templar=t, globals={'var2': 'value2'})
    assert a['var1'] == 'value1'
    assert a['var2'] == 'value2'

    # case 2: vars accessed via lookup
    a = AnsibleJ2Vars(templar=t, globals={'var2': 'value2'})
    assert a['vars']['var1'] == 'value1'

    # case 3: locals work

# Generated at 2022-06-13 15:39:08.491344
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    pass # TODO


# Generated at 2022-06-13 15:39:18.818146
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars

    templar = Templar(loader=None)
    globals = {'foo': 3, 'bar': 4}
    locals = {'bar': 5, 'baz': 6}
    proxy = AnsibleJ2Vars(templar, globals, locals)
    assert proxy['foo'] == 3
    assert proxy['bar'] == 5
    assert proxy['baz'] == 6

    # 'vars' should not be templated
    templar.set_available_variables({'vars': {'foo': 7}})
    assert proxy['foo'] == 7

    # AnsibleVars should not be templated

# Generated at 2022-06-13 15:39:24.336252
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():

    from ansible.template import Templar
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    templar = Templar()
    globals = {'g_var': AnsibleUnsafeText('g_var_value')}

    # test __contains__
    av = AnsibleJ2Vars(templar, globals)
    assert 'g_var' in av

# Generated at 2022-06-13 15:39:30.972946
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    '''
    Test __iter__ of AnsibleJ2Vars
    '''
    import sys
    import json
    import os

    sys.path.append("../../")
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()

    vault_secrets_path = os.path.join(os.path.dirname(__file__), 'vault.key')
    vault = VaultLib([vault_secrets_path])
    vaultpassword = 'secret'


# Generated at 2022-06-13 15:39:41.794334
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    var = PlayContext()
    templar = Templar(loader=None, variables=var)
    proxy = AnsibleJ2Vars(templar, dict())
    
    print("AnsibleJ2Vars:", proxy)

    print("proxy[inventory_hostname]:", proxy["inventory_hostname"])

    try:
        print("proxy[hostvar]:", proxy["hostvar"])
    except KeyError as err:
        print("proxy[hostvar]:", err)

    try:
        print("proxy[foobar]:", proxy["foobar"])
    except KeyError as err:
        print("proxy[foobar]:", err)


# Generated at 2022-06-13 15:39:56.412350
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.vars.hostvars import HostVars
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.template import Templar
    from ansible.vars import AnsibleVars
    from ansible.inventory.host import Host
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role.definition import RoleDefinition

    class RoleArgumentSpec:
        def __init__(self):
            self.options = {'role_path': '/data1/vars_test/'}

    class Options:
        def __init__(self):
            self.role_path = '/data1/vars_test/'

    class Play:
        def __init__(self):
            self.ROLE_CACHE = True
            self

# Generated at 2022-06-13 15:40:03.161532
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    p = PlayContext()
    t = Templar(loader=None, variables={})
    assert AnsibleJ2Vars(t, p.get_tmp_vars()).__contains__("foo") is False
    p.set_tmp_vars({"foo": "bar"})
    assert AnsibleJ2Vars(t, p.get_tmp_vars()).__contains__("foo") is True


# Generated at 2022-06-13 15:40:11.231413
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from ansible.template import Templar

    vars_dict = dict(a=1, b=2, c=3)
    j2vars = AnsibleJ2Vars(None, dict())

    assert j2vars['a'] == 1
    assert j2vars['b'] == 2
    assert j2vars['c'] == 3
    assert 'a' in j2vars
    assert 'b' in j2vars
    assert 'c' in j2vars
    assert 'd' not in j2vars
    assert len(j2vars) == 3

    # Add a templar to j2vars
    j2vars._templar = Templar(loader=None, variables=vars_dict)
    assert j2vars['a'] == 1
    assert j2vars['b']

# Generated at 2022-06-13 15:40:21.917598
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    def mock_template(data):
        return data

    templar = type("mock", (object,), {"template": mock_template})()

    locals = dict(x="y")
    globals = dict(a="z")

    j2vars = AnsibleJ2Vars(templar, globals, locals=locals)

    assert j2vars["x"] == "y"
    assert j2vars["a"] == "z"
    assert j2vars["y"] == "y"

    try:
        j2vars["z"]
    except KeyError as e:
        assert "z" in e.args[0]
    else:
        assert False

# Generated at 2022-06-13 15:40:33.019333
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    '''
    Test AnsibleJ2Vars.__contains__
    '''
    import ansible.vars.hostvars
    import ansible.parsing.vault

    class TestAnsibleJ2Vars(AnsibleJ2Vars):
        ''' Test class for AnsibleJ2Vars '''
        def __init__(self, templar, globals, locals=None):
            self._templar = templar
            self._globals = globals
            self._locals = {}
            if locals:
                for key, val in locals.items():
                    self._locals[key] = val

        def __getitem__(self, varname):
            if varname in self._locals:
                return self._locals[varname]

# Generated at 2022-06-13 15:40:41.661980
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template.safe_eval import compile_expression

    compile_expression("A", global_vars={}, module_vars={})
    compile_expression("B", global_vars={'B':1}, module_vars={})
    compile_expression("C", global_vars={}, module_vars={'C':1})
    compile_expression("D", global_vars={}, module_vars={}, local_vars={'D':1})

    class DummyTemplar():
        def __init__(self):
            self.available_variables = {'C': 1}

    j2_vars = AnsibleJ2Vars(DummyTemplar(), {'A':1}, locals={'D':1})

    assert 'A' in j2_vars

# Generated at 2022-06-13 15:40:50.150699
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.template import Templar
    from ansible.utils.vars import combine_vars

    loader = DataLoader()

    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    templar = Templar(loader=loader, variables=variable_manager)

    # Tests of edge cases
    # test item exists as a local variable (i.e., as a member of _locals)
    vars_obj = AnsibleJ2Vars(templar, dict(), locals=dict(item1='local variable'))

# Generated at 2022-06-13 15:40:55.500994
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    from ansible.parsing.vault import VaultLib
    from ansible.template import Templar
    from ansible.utils.vars import combine_vars

    fake_vars        = dict(somevar=42, templatedvar='{{ansible_hostname}}', combinedvar='{{somevar}} is {{templatedvar}}')
    fake_globalvars  = dict(globalvar=43)
    fake_hostvars    = HostVars(dict())

    vault_secrets = dict()

    vars_manager = VariableManager()
    vars_manager.add_vars(fake_globalvars)

# Generated at 2022-06-13 15:41:03.001051
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    j2vars = AnsibleJ2Vars(None, None, None)
    assert 'foo' not in j2vars
    j2vars._templar.available_variables['foo'] = None
    assert 'foo' in j2vars
    assert 'bar' not in j2vars
    j2vars._locals['bar'] = None
    assert 'bar' in j2vars
    assert 'baz' not in j2vars
    j2vars._globals['baz'] = None
    assert 'baz' in j2vars

# Generated at 2022-06-13 15:41:08.002741
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar

    templar = Templar(loader=None, variables={'a': 'A', 'b': '{{ a }}'})
    ansible_j2vars = AnsibleJ2Vars(templar, {}, locals={'a': 'B'})

    assert ansible_j2vars['a'] == 'B'
    assert ansible_j2vars['b'] == 'B'


# Generated at 2022-06-13 15:41:22.359455
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.errors import AnsibleUndefinedVariable

    # Init a Templar object
    mgr = VariableManager()
    loader = AnsibleLoader(None, True)
    templar = Templar(loader=loader, variables=mgr)

    # Test ansible j2 vars with no var given
    j2_vars = AnsibleJ2Vars(templar, globals={}, locals={})
    assert not hasattr(j2_vars, '_locals')
    assert len(j2_vars) == 0

    # Test ansible j2 vars with local var given

# Generated at 2022-06-13 15:41:33.817075
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    # TODO: test __contains__
    # assert False
    from jinja2.environment import Environment
    from jinja2 import StrictUndefined
    from ansible.template.safe_eval import safe_eval

    env = Environment(undefined=StrictUndefined)
    templar = Templar(loader=None, variables={})

    j2vars = AnsibleJ2Vars(templar, globals_=safe_eval("dict(foo='var_foo', bar='var_bar')"), locals=None)
    assert 'foo' in j2vars
    assert 'bar' in j2vars
    assert 'baz' not in j2vars
    assert 'var_foo' not in j2vars
    assert 'var_bar' not in j2vars


# Generated at 2022-06-13 15:41:38.388919
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    templar = Templar(loader=None)

    vars = {'foo': 'bar'}

    # default values
    ajv = AnsibleJ2Vars(templar, vars)
    assert ajv['foo'] == 'bar'

    # no locals given => should return bar
    ajv = AnsibleJ2Vars(templar, vars, locals={'foo': 'foo'})
    assert ajv['foo'] == 'foo'

    # locals given and var in locals => should return foo
    ajv = AnsibleJ2Vars(templar, vars, locals={'foo': 'foo'})
    ajv.add_locals({'foo': 'baz'})
    assert ajv['foo'] == 'baz'



# Generated at 2022-06-13 15:41:46.847459
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import Mock, patch

    from ansible.module_utils.six import iteritems
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar

    TEST_DATA = {'test_vars': {'a': 'b'}, 'test_vars_param': {'c': 'd'}}

    class AnsibleJ2VarsProxyTestCase(unittest.TestCase):

        def setUp(self):
            self._templar = Templar(loader=DataLoader())
            self._globals = {'test_globals': 'globals'}

# Generated at 2022-06-13 15:41:54.994386
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.vars import VariableManager
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    loader = DataLoader()
    templar = Templar(loader=loader, variables=variable_manager)
    aj2_vars = AnsibleJ2Vars(templar, {'foo':'bar'})
    assert aj2_vars['foo'] == 'bar'

# Generated at 2022-06-13 15:42:03.828580
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

# Generated at 2022-06-13 15:42:06.668395
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    templar = None
    globals = None
    locals = None

    proxy = AnsibleJ2Vars(templar, globals, locals)

    assert False == ("foo" in proxy)



# Generated at 2022-06-13 15:42:15.073265
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    '''
    Test the __contains__ method of the AnsibleJ2Vars class
    '''

    templar = Templar()
    globals = {}
    locals = {}

    assert 'a' not in AnsibleJ2Vars(templar, globals, locals=locals), "a should not be in AnsibleJ2Vars without it being set"

    templar.available_variables = { 'a': 1 }
    assert 'a' in AnsibleJ2Vars(templar, globals, locals=locals), "a should be in AnsibleJ2Vars after it has been set"

    templar.available_variables = { 'b': 2 }
    locals['a'] = 1

# Generated at 2022-06-13 15:42:21.192965
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    # Create an AnsibleJ2Vars object
    if True:
        vars()
        templar = AnsibleJ2Vars
        globals = AnsibleJ2Vars
        locals = AnsibleJ2Vars
    obj = AnsibleJ2Vars(templar, globals, locals)

    # Test the method __len__
    obj.__len__()

# Generated at 2022-06-13 15:42:26.786346
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.playbook.play_context import PlayContext

    play_context = PlayContext()
    templar = Templar(loader=None, variables={}, disable_lookups=True, play_context=play_context)

    j2vars = AnsibleJ2Vars(templar, {}, {})

    assert 'foo' in j2vars

# Generated at 2022-06-13 15:42:48.332097
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar

    tmp = Templar(loader=None)
    tmp.available_variables = dict(a=7, b=8)
    vars = AnsibleJ2Vars(tmp, {'c': 9}, locals={'d': 10})
    assert vars['a'] == 7
    assert vars['b'] == 8
    assert vars['c'] == 9
    assert vars['d'] == 10
    assert not vars.__contains__('e')
    try:
        v=vars['e']
        assert False, 'KeyError was not raised'
    except KeyError:
        pass

# Generated at 2022-06-13 15:42:55.783859
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.template import Templar
    import ansible.constants as C
    import os
    import sys

    templar = Templar(loader=None, variables={})
    # initialize ansible-specific jinja2 globals
    templar._add_ansible_facts_to_scope()
    jinja2_globals = templar._get_jinja2_globals()

    variables = {
        u'name': u'foo',
        'name2': u'bar'
    }

    # when locals is None
    var_proxy = AnsibleJ2Vars(templar, jinja2_globals)
    assert len(jinja2_globals) + len(variables) == len(var_proxy)

    # when locals is not None

# Generated at 2022-06-13 15:43:05.244368
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    import ansible.template
    templar = ansible.template.AnsibleTemplar(loader=None, variables={})

    test_j2_vars = AnsibleJ2Vars(templar, {})

    # test the class constructor
    if not isinstance(test_j2_vars, Mapping):
        raise Exception("AnsibleJ2Vars is not a Mapping")

    if set(test_j2_vars.keys()) != set():
        raise Exception("AnsibleJ2Vars keys are not correct")

    for k in test_j2_vars.keys():
        test_j2_vars[k]

    # test part of __getitem__
    with pytest.raises(KeyError):
        test_j2_vars.__getitem__('test')

# Generated at 2022-06-13 15:43:10.320206
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    templar = None
    globals = {'a': 'A', 'b': 'B'}
    locals = {'c': 'C', 'A': 'D'}

    var = AnsibleJ2Vars(templar, globals, locals)
    assert var['a'] == 'A'
    assert var['b'] == 'B'
    assert var['c'] == 'D'

# Generated at 2022-06-13 15:43:16.709214
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.template.safe_eval import safe_eval
    from ansible.template import Templar

    # Create AnsibleJ2Vars
    templar = Templar(loader=None, variables={})
    ansiblej2vars = AnsibleJ2Vars(templar, {}, locals={'a': 1})

    # Test AnsibleJ2Vars.__contains__
    assert 'a' in ansiblej2vars
    assert 'b' not in ansiblej2vars
    assert 'b' not in ansiblej2vars
    assert 'c' not in ansiblej2vars

    # Create AnsibleJ2Vars
    templar = Templar(loader=None, variables={})

# Generated at 2022-06-13 15:43:28.062234
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    templar = Templar(loader=None)
    templar.available_variables = dict()
    templar.available_variables['a'] = 1
    templar.available_variables['b'] = 2
    globals = dict()
    globals['c'] = 3
    globals['d'] = 4
    locals = dict()
    locals['l_e'] = 5
    locals['l_f'] = 6
    j2v = AnsibleJ2Vars(templar, globals, locals)
    assert j2v['a'] == 1
    assert j2v['b'] == 2
    assert j2v['c'] == 3
    assert j2v['d'] == 4
    assert j2v['e'] == 5

# Generated at 2022-06-13 15:43:39.282089
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    '''
    Run tests against AnsibleJ2Vars.__iter__()
    '''

    vars = {'a': 'A', 'b': 'B', 'c': 'C'}
    globals = {'g': 'G', 'h': 'H'}
    locals = {'l_x': 'X', 'l_y': 'Y', 'l_z': 'Z'}
    class DummyTemplar(object):
        def __init__(self):
            self.available_variables = vars
    templar = DummyTemplar()

    ajv = AnsibleJ2Vars(templar, globals, locals)
    assert set(ajv.__iter__()) == set(vars.keys()) | set(globals.keys()) | set(locals.keys())

# Generated at 2022-06-13 15:43:49.800893
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    import pytest

    templar = object()
    globals = {}
    locals = {}

    ansiblej2vars = AnsibleJ2Vars(templar, globals, locals=locals)

    new_globals = { 'key1': 'value1' }
    ansiblej2vars = ansiblej2vars.add_locals(new_globals)

    assert ansiblej2vars.__contains__('key1')

    with pytest.raises(KeyError):
        ansiblej2vars.__getitem__('key1')

    assert ansiblej2vars.__contains__('key1')

# Generated at 2022-06-13 15:43:57.027386
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar

    templar = Templar(loader=DataLoader(), variables={})

    ansible_j2_vars = AnsibleJ2Vars(templar, {}, {})

    ansible_j2_vars.add_locals({'foo':'bar', 'baz':'b'})

    assert 'foo' in ansible_j2_vars
    assert 'baz' in ansible_j2_vars

    assert ansible_j2_vars['foo'] == 'bar'
    assert ansible_j2_vars['baz'] == 'b'

# Generated at 2022-06-13 15:44:00.503865
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    templar = None
    globals = None
    locals = None
    AnsiJ2Var = AnsibleJ2Vars(templar, globals, locals)
    ret = AnsiJ2Var.__contains__('vars')
    assert ret == True

# Generated at 2022-06-13 15:44:27.239662
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import ansible.template.template as j2_env
    from ansible.vars.hostvars import HostVars
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.module_utils.six import string_types

    x = {
            "vars": HostVars({ 'a': 'b'}),
            "a": AnsibleUnicode("{{a}}"),
            "b": AnsibleUnicode("{{b}}"),
            "c": {"{{c}}": "{{c}}", "{{d}}": "{{d}}"}
         }

    # Test with an unset variable
    templar = j2_env.AnsibleEnvironment(loader=None).get_template(None, None)._templar
    templar.available_variables = x


# Generated at 2022-06-13 15:44:39.467722
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from binascii import hexlify
    from ansible.vars import VariableManager
    from ansible.template.safe_eval import safe_eval
    from ansible.parsing.vault import VaultLib


# Generated at 2022-06-13 15:44:43.600556
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from ansible.template.safe_eval import safe_eval

    assert isinstance(safe_eval(AnsibleJ2Vars("", "")), dict)
    assert isinstance(AnsibleJ2Vars("", ""), dict)
    assert isinstance(AnsibleJ2Vars("", ""), object)

# Generated at 2022-06-13 15:44:49.296303
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    # We use a mock Templar, because we don't need the real one
    from ansible.template.safe_eval import StrictUndefined
    class Templar():
        def __init__(self):
            self.available_variables = {'foo': StrictUndefined('foo'), 'bar': StrictUndefined('bar')}
    templar = Templar()

    globals = {'baz': 1}

    vars = AnsibleJ2Vars(templar, globals)
    assert len(vars) == 3

# Generated at 2022-06-13 15:44:56.186856
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.playbook import Task
    from ansible.template import Templar

    task = Task()
    templar = Templar(play=None, variables=None, loader=None, shared_loader_obj=None)
    variable_manager = dict()

    ansible_j2_vars = AnsibleJ2Vars(templar, variable_manager, locals=None)
    assert isinstance(ansible_j2_vars, Mapping)
    assert not isinstance(ansible_j2_vars, MutableMapping)

    assert ansible_j2_vars["task_name"] == "unknown"
    assert ansible_j2

# Generated at 2022-06-13 15:45:01.323301
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    # test setUp
    templar = None
    globals = None
    locals = None
    var = AnsibleJ2Vars(templar, globals, locals)

    # test1
    assert False == ("key1" in var)


# Generated at 2022-06-13 15:45:08.269838
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    # set up

    templar = None

    globs = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
    }

    locs = {
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'ten': 10,
    }

    vars = AnsibleJ2Vars(templar, globs, locs)

    # test

    ## keys

    assert ('one' in vars) == True
    assert ('two' in vars) == True
    assert ('three' in vars) == True
    assert ('four' in vars) == True
    assert ('five' in vars) == True

    assert ('six' in vars)

# Generated at 2022-06-13 15:45:18.465134
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.compat.tests import mock
    from ansible.module_utils.six import PY3
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars

    if PY3:
        BUILTIN_MODULE_NAME = 'builtins'
    else:
        BUILTIN_MODULE_NAME = '__builtin__'
    with mock.patch(BUILTIN_MODULE_NAME + '.range') as mock_range:
        templar = Templar(loader=None)
        globals_ = {'test_1': 't1', 'test_2': 't2'}
        locals_ = {'test_1': 'b1'}
        vars_ = AnsibleJ2Vars(templar, globals_, locals_)

# Generated at 2022-06-13 15:45:22.685325
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    from ansible.template import Templar
    templar = Templar(loader=None)
    vars = AnsibleJ2Vars(templar, dict())
    assert 'dict_keys' in str(type(vars.__iter__()))

# Generated at 2022-06-13 15:45:34.649471
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from jinja2.exceptions import UndefinedError
    from ansible.template import Templar

    env = {
        'a_global1': 'a_global1',
        'a_global2': 'a_global2'
    }
    templar = Templar(loader=None, variables=env)
    vars = AnsibleJ2Vars(templar, env)
    assert env['a_global2'] == vars['a_global2']

    locals = {
        'a_local1': 'a_local1',
        'a_local2': 'a_local2'
    }
    vars = AnsibleJ2Vars(templar, env, locals)
    assert locals['a_local2'] == vars['a_local2']



# Generated at 2022-06-13 15:46:23.298832
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    # Copied from ansible/playbook/templar.py
    # TODO: Needed to make this function work, could probably init a Templar() object with something better
    class Templar(object):
        def __init__(self):
            self.available_variables = {'pew':'pew'}

    templar = Templar()
    globals = {'pew':'pew'}
    locals = dict(l_pew='pew')
    vars = AnsibleJ2Vars(templar, globals, locals)

    assert 'pew' in vars
    assert vars['pew'] == 'pew'
    assert vars['l_pew'] == 'pew'


# Generated at 2022-06-13 15:46:33.937659
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    from ansible.module_utils.basic import AnsibleModule
    from ansible.template import Templar

    # Test for Special variables vars and HostVars
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    templar = Templar(module)
    labels = ['creates', 'become', 'become_user']
    vars = AnsibleJ2Vars(templar, {}, {'l_%s' % x: templar.template('{{ %s }}' % x, convert_bare=True) for x in labels})
    assert(vars['l_creates'] == 'None')
    assert(vars['l_become'] == 'None')
    assert(vars['l_become_user'] == 'root')

# Generated at 2022-06-13 15:46:37.994966
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.template.template import Templar
    from ansible.vars import VariableManager
    from ansible.playbook.play_context import PlayContext

    varmgr = VariableManager()

    myvars = {'omero': 'omero', 'omero1': 'omero1', 'omero3': 'omero3'}
    vars = VariableManager()
    vars.extra_vars = myvars

    context = PlayContext()
    templar = Templar(loader=None, variables=vars)

    jvars = AnsibleJ2Vars(templar, locals=varmgr.get_vars(context))
    len(jvars)



# Generated at 2022-06-13 15:46:48.864502
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():

    from ansible.template import Templar

    from ansible.parsing.vault import VaultSecret

    class MyVaultSecret(VaultSecret):

        def __init__(self, vault_secret):
            super(MyVaultSecret, self).__init__(vault_secret)

        def __len__(self):
            return len(self.vault_secret)

    test_template = Templar(loader=None)

    test_globals = {
        'myglobal1': "global1",
        'myglobal2': "global2",
    }

    test_locals = {
        'mylocal1': "local1",
        'mylocal2': "local2",
    }


# Generated at 2022-06-13 15:46:55.395182
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    import jinja2
    from ansible.module_utils.six import PY3

    def j2_filter(a):
        return len(a)

    globals = {
        'len': len,
        'j2_filter': j2_filter,
    }

    # values used in both test cases
    vars = {
        'foo': {
            'a': 'b',
            'c': [1, 2, 3],
            'd': {'aa': 'bb', 'cc': 'dd'},
        },
    }

    # values used in test case k=1
    locals_1 = {
        'list_1': [1, 2, 3],
        'list_2': [4, 5, 6],
    }

    # values used in test case k=2

# Generated at 2022-06-13 15:47:04.268612
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    templar = Templar()
    globals = { 'f': 'g' }
    locals = { 'l_a': 'b', 'c': 'd' }

    ansible_j2vars = AnsibleJ2Vars(templar, globals, locals)

    assert 'e' not in ansible_j2vars

    ansible_unsafe_text = AnsibleUnsafeText(text="Hello world!")

    templar._available_variables = { 'e': ansible_unsafe_text }

    assert 'e' in ansible_j2vars


# Generated at 2022-06-13 15:47:07.948009
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    # load the module
    mod = AnsibleModule(argument_spec={}, supports_check_mode=True)

    # create the module
    a = AnsibleJ2Vars(mod, {'a':'b'})

    # test if item exists
    assert 'a' in a

    # test if item does not exist
    assert 'c' not in a



# Generated at 2022-06-13 15:47:15.145999
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    templar = Templar()

    # Tests for 'undefined variable' exception
    globals = {}
    locals = {}
    var_proxy = AnsibleJ2Vars(templar, globals, locals)
    try:
        var_proxy['undefined_variable']
    except KeyError as e:
        assert 'undefined variable: undefined_variable' == to_native(e)
    else:
        assert False

    # Tests for AnsibleUndefinedVariable exception
    globals = {}
    locals = {}
    var_proxy = AnsibleJ2Vars(templar, globals, locals)

# Generated at 2022-06-13 15:47:25.476106
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import copy
    import pytest

    def test_j2vars_getitem(ansible_vars, templar, j2vars):
        ansible_vars = copy.deepcopy(ansible_vars)
        for v in ansible_vars:
            templar.set_available_variables(ansible_vars)
            templar.set_available_variables({"vars": ansible_vars})

            assert j2vars[v] == templar.template(vars[v])
            assert j2vars[v] == templar.template(ansible_vars[v])


# Generated at 2022-06-13 15:47:33.754899
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import ansible.utils.unsafe_proxy
    import ansible.template
    import os
    import tempfile
    import yaml
    import copy
    import json

    # create variable files
    (fd, vars_file) = tempfile.mkstemp()
    os.close(fd)

    (fd, vars_file2) = tempfile.mkstemp()
    os.close(fd)

    (fd, j2_file) = tempfile.mkstemp()
    os.close(fd)

    # create a variable file with reference to another variable file
    with open(vars_file, 'w+') as vars1:
        vars1.write('foo: value1\n')
        vars1.write('@' + vars_file2 + '\n')

    # create a variable

# Generated at 2022-06-13 15:48:16.075731
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    '''
    Unit test for method __contains__ of class AnsibleJ2Vars
    '''
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader

    hosts = [
        Host(name="localhost"),
        Host(name="otherhost")
    ]
    inventory = Inventory(loader=DataLoader(), hosts=hosts, sources=['localhost', 'otherhost'])
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)
    templar = Templar(loader=DataLoader(), variables=variable_manager.get_vars(host=hosts[0]))

# Generated at 2022-06-13 15:48:22.264933
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():

    # Create a mock Templar object
    class MockTemplar(object):
        """docstring for Templar"""
        def __init__(self):
            self.available_variables = {'var1': '23', 'var3': '42'}

    mock = MockTemplar()

    # Create an instance of AnsibleJ2Vars using the mock
    proxy = AnsibleJ2Vars(mock, globals={'var2': 23, 'var4': 42})

    # Test for existing variables
    assert var1 in proxy
    assert var4 in proxy
    assert var2 in proxy
    assert var3 in proxy

    # Test for nonexistent variables
    assert 'var0' not in proxy
    assert var0 not in proxy



# Generated at 2022-06-13 15:48:29.727827
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.templating.template import Templar
    from ansible.vars import VariableManager
    from jinja2 import StrictUndefined

    def test_contains(name, available_variables, globals, expected):
        templar = Templar(loader=None, variables=VariableManager(loader=None, variable_manager=None), templar_imports=[], undefined=StrictUndefined)
        templar.available_variables = available_variables
        ajv = AnsibleJ2Vars(templar, globals)

        assert (name in ajv) == expected

    test_contains('name', {'name': 'hoge'}, {}, True)
    test_contains('name', {}, {'name': 'hoge'}, True)