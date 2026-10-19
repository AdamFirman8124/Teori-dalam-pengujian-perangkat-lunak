

# Generated at 2022-06-13 15:38:39.201841
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    from ansible.template import Templar
    templar = Templar()

    j2vars = AnsibleJ2Vars(templar, {}, locals={'l_a':1})
    assert {'a'} == set(j2vars)
    assert {1} == set(j2vars.values())

    j2vars = AnsibleJ2Vars(templar, {'g_b':1}, locals={'l_a':1})
    assert {'a', 'b'} == set(j2vars)
    assert {1, 1} == set(j2vars.values())

# test for method __contains__ of class AnsibleJ2Vars

# Generated at 2022-06-13 15:38:49.681990
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    module = 'ping'
    args = dict()
    args['inventory'] = 'inventory/hosts'
    args['module_name'] = module
    args['module_args'] = ''
    args['module_path'] = 'library'
    args['module_vars'] = dict()
    args['module_vars']['ansible_python_interpreter'] = '/usr/bin/python3'
    args['module_vars']['ansible_connection'] = 'local'

    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import connection_loader, module_loader
    from ansible.template import Templar
    from ansible.vars import VariableManager

    conn = connection_loader.get('local', basedir=os.getcwd(), **args)
    # create the

# Generated at 2022-06-13 15:39:00.565675
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    VM = VariableManager()

    group = Group('test_group')
    group.set_variable('test_group_var', 'test_group_var_value')

    host = Host('test_getitem')
    host.set_variable('test_host_var', 'test_host_var_value')

    VM.add_group(group)
    VM.add_host(host)

    j2_vars = AnsibleJ2Vars(Templar(VM), {}, {})

    assert j2_vars['test_group_var'] == 'test_group_var_value'

# Generated at 2022-06-13 15:39:06.941212
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from ansible.template.safe_eval import ansible_safe_eval
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.template import Templar
    from ansible import constants as C

    # create a vault encrypted variable

# Generated at 2022-06-13 15:39:18.323958
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.vars import HostVars
    from ansible.template import Templar
    from ansible.playbook.play_context import PlayContext

    hostvars = HostVars(dict(), dict())

    class TestVarsModule(object):
        def run(self, tmp=None, task_vars=None):
            if task_vars is None:
                task_vars = dict()
            new_result = dict({'ansible_facts': {'test_key': 'test_value'}, 'changed': False})
            new_result.update(task_vars)
            return new_result


# Generated at 2022-06-13 15:39:26.588532
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    '''
    This function performs a test for the method __getitem__ of class AnsibleJ2Vars
    '''

    from ansible.template import Templar

    from ansible.vars.manager import VariableManager

    from ansible.utils.vars import combine_vars

    from ansible.parsing.vault import VaultLib

    from ansible.vars.hostvars import HostVars

    from ansible.vars.unsafe_proxy import UnsafeProxy

    templar = Templar(variables=combine_vars(loader=None, variables=dict(vars={'hostvars': {'host': 1}})))

    globals = VariableManager().get_vars(play=dict(vars=dict()), include_hostvars=False, include_delegate_to=False)


# Generated at 2022-06-13 15:39:32.565885
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    def _test_AnsibleJ2Vars___contains__(test_case):
        from ansible.template import Templar
        templar = Templar(loader=None)
        globals = dict(
            g=dict(
                g_x=True,
            ),
            g_x=True,
        )
        locals = dict(
            l=dict(
                l_x=True,
            ),
            l_x=True,
        )
        HOST_VARS = dict(
            hostvars=dict(
                x=True,
            ),
            x=True,
        )
        VARS = dict(
            vars=HOST_VARS,
            x=True,
        )
        templar.set_available_variables(VARS)
        variable_manager = AnsibleJ

# Generated at 2022-06-13 15:39:42.756197
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2022-06-13 15:39:54.181776
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    t = Templar(loader=None)
    test_locals = {
        'foo': 'bar',
        'test_accessible': True,
        'test_inaccessible': False,
        'test_available': False,
        'test_undefined': False,
        'test_hostvars': False,
    }

# Generated at 2022-06-13 15:40:04.674138
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars

    locals = dict(foo='foo', bar='bar', foobar='foobar')
    templar = Templar(loader=None)
    globals = dict(foo='foo', baz='baz')
    vars = AnsibleJ2Vars(templar, globals, locals)
    assert vars['foo'] == 'foo'
    assert vars['bar'] == 'bar'
    assert vars['foobar'] == 'foobar'
    assert vars['baz'] == 'baz'
    try:
        print(vars['fizz'])
        assert False
    except KeyError:
        pass

# Generated at 2022-06-13 15:40:20.375436
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    templar = Templar(loader=None)
    templar._available_variables = {'vars': {'k': 'v'}}
    # variable already in local scope
    assert AnsibleJ2Vars(templar, {'k': 'v'}, locals={'k': 'v'})['k'] == 'v'
    # variable in current local scope but not in the top local scope
    assert AnsibleJ2Vars(templar, {'k': 'v'}, locals={'k': 'v'})['k'] == 'v'

    # variable not in local scope
    assert AnsibleJ2Vars(templar, {'k': 'v'}, locals={'k': 'v'})['k'] == 'v'

    # variable not in local scope but in

# Generated at 2022-06-13 15:40:31.285536
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():

    from ansible.vars.manager import VariableManager
    from ansible.template import Templar

    from ansible.plugins.loader import dynamic_plugin_source, vars_loader
    from ansible.plugins.filter.core import wrap_var, combine

    dynamic_plugin_source.add_directory(vars_loader, './plugins/vars')
    dynamic_plugin_source.add_directory(wrap_var, './plugins/filter/core')
    dynamic_plugin_source.add_directory(combine, './plugins/filter/core')

    test_vars = dict(
        a="a",
        b="b",
        c="{{a}}{{b}}",
    )

    # FIXME the proper way to test the Iterator is not to call the method
    #       but to call next() on the Iterator and check the

# Generated at 2022-06-13 15:40:40.602280
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():

    class AnsibleJ2VarsTest(AnsibleJ2Vars):
        def __init__(self, templar, globals, locals=None):
            # self._templar = templar
            self._templar = None
            self._globals = {'g1': 1, 'g2': 2}
            self._locals = {'l1': 1, 'l2': 2}

    # tests
    ansible_j2_vars_test1 = AnsibleJ2VarsTest(None, None)
    assert 'g1' in ansible_j2_vars_test1
    assert 'g2' in ansible_j2_vars_test1
    assert 'l1' in ansible_j2_vars_test1
    assert 'l2' in ansible_j

# Generated at 2022-06-13 15:40:49.432984
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    from ansible.vars import VariableManager

    variable_manager = VariableManager()
    variable_manager.set_nonpersistent_facts(dict(a=1, b=2))
    variable_manager.set_host_variable('g', 'global')
    variable_manager.set_host_variable('h', 'host')
    variable_manager.set_host_variable('c', 'command')
    variable_manager.set_host_variable('s', 'setup')
    variable_manager.set_host_variable('f', 'fact')
    variable_manager.set_host_variable('o', 'ohai')

    templar = Templar(loader=None, variables=variable_manager)

# Generated at 2022-06-13 15:40:55.764527
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    '''
    This unit test checks the method __contains__ of the class AnsibleJ2Vars
    '''
    ansiblej2vars = AnsibleJ2Vars(templar=None, globals={'g1': 'gvalue1'}, locals={'l1': 'lvalue1'})

    assert 'g1' in ansiblej2vars
    assert 'l1' in ansiblej2vars
    assert not ('x' in ansiblej2vars)


# Generated at 2022-06-13 15:41:05.541741
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    templar = Templar(loader=None)
    globals = {'gvar': 'global', 'gdict': {'subgvar': 'subglobal'}}
    vars = {'var': 'variable', 'dict': {'subvar': 'subvariable'}}
    locals = {'lvar': 'local', 'ldict': {'sublvar': 'sublocal'}}
    j2vars = AnsibleJ2Vars(templar, globals, locals)

    # Test variable variable
    templar._available_variables = vars
    assert j2vars['var'] == 'variable'

    # Test variable variable in an AnsibleVaultEncryptedUnicode object


# Generated at 2022-06-13 15:41:16.328865
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template.safe_eval import ansible_safe_eval
    from ansible.template import Templar

    templar = Templar(None)
    globals = {}
    locals = {'l_var1': 1, 'var2': 2}

    jvars = AnsibleJ2Vars(templar, globals, locals)

    # Test if key 'var1' is in the jvars
    assert 'var1' in jvars

    # Test if key 'var2' is in the jvars
    assert 'var2' in jvars

    # Test if key 'var3' is in the jvars
    assert 'var3' in jvars

    # Test if key 'var4' is in the jvars
    assert 'var4' in jvars

    # Test if key 'var

# Generated at 2022-06-13 15:41:23.857474
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    templar = Templar()

    # contains_test_simple is a simple test case with a small set of variables
    contains_test_simple_globals = {
        u"ansible_os_family": u"Debian",
        }
    contains_test_simple_locals = {
        u"ansible_local": u"local",
        u"ansible_local_var": u"local var"
        }

# Generated at 2022-06-13 15:41:35.102825
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    locals = {'l_foo': 'bar'}
    templar = Templar(loader=None)
    templar._available_variables = {'foo': 'bar', 'baz': 'baz'}
    globals = {'global_foo': 'global_bar'}

    ansible_vars = AnsibleJ2Vars(templar, globals, locals)
    assert 'foo' in ansible_vars
    assert 'baz' in ansible_vars
    assert 'global_foo' in ansible_vars
    assert 'l_foo' in ansible_vars
    assert 'missing_foo' not in ansible_vars
    # Override locals with available variables
    templar._available_variables = {'l_foo': 'baz'}

# Generated at 2022-06-13 15:41:40.165399
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    class Templar(object):
        def __init__(self):
            self.available_variables = {}
    globals = {}
    locals = None
    with pytest.raises(AnsibleUndefinedVariable):
        AnsibleJ2Vars(Templar(), globals, locals).__contains__('test')


# Generated at 2022-06-13 15:41:55.465424
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    import jinja2
    import ansible.parsing.yaml.objects
    import ansible.template.safe_eval

    globals = {'a': 3}
    locals = {'b': 4}
    v = AnsibleJ2Vars(jinja2.Environment(), globals, locals)
    assert v['a'] == globals['a']
    assert v['b'] == locals['b']
    assert isinstance(v['a'], ansible.parsing.yaml.objects.AnsibleUnicode)
    assert isinstance(v['b'], ansible.parsing.yaml.objects.AnsibleUnicode)
    try:
        v['c']
    except KeyError:
        pass

# Generated at 2022-06-13 15:42:04.104503
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    from ansible.template.safe_eval import safe_eval

    templar = Templar(loader=None, variables={}, fail_on_undefined=True)
    ansiblej2vars = AnsibleJ2Vars(templar, globals={}, locals={})

    assert 'a' not in ansiblej2vars

    ansiblej2vars._templar.available_variables['a'] = safe_eval('1+1')
    assert 'a' in ansiblej2vars

    ansiblej2vars._globals['a'] = 2
    assert 'a' in ansiblej2vars

    ansiblej2vars._locals['a'] = 3
    assert 'a' in ansiblej2vars


# Generated at 2022-06-13 15:42:09.522693
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    from ansible.plugins.loader import variable_loader
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars

    templar = Templar(loader=None)
    globals = {}

    locals = {
        'test_dict': {
            'test_key': '{{ test_var }}'
        },
        'test_dict_complex': {
            'test_key2': {
                'test_key3': '{{ test_var }}'
            }
        },
        'test_key': 'test_val',
        'test_var': 'test_val2',
        'hostvars': HostVars(dict())
    }

    vars = AnsibleJ2Vars(templar, globals, locals)

# Generated at 2022-06-13 15:42:15.134498
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    from ansible.plugins import filter_loader
    import jinja2

    # Create a jinja2 enviroment
    jenv = jinja2.Environment(undefined=jinja2.StrictUndefined)
    jenv.filters.update(filter_loader.filters())
    templar = Templar(loader=None, variables={}, filters=jenv.filters)
    aj2v = AnsibleJ2Vars(templar, globals={})
    assert aj2v.__contains__('not_exist_variable') is False
    aj2v = AnsibleJ2Vars(templar, globals={'test': 'value'})
    assert aj2v.__contains__('test') is True
    aj2v = Ans

# Generated at 2022-06-13 15:42:25.570391
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from jinja2.environment import Environment
    from ansible.template import Templar

    environment_vars = {
        'foo': 'bar'
    }
    j2_environment = Environment(loader=None)
    j2_environment.globals.update(environment_vars)

    templar = Templar(loader=None, variables={'dummy': 'variable'}, shared_loader_obj=j2_environment)

    # Test that shared_loader_obj globals are in AnsibleJ2Vars
    j2_vars = AnsibleJ2Vars(templar, {}, {'foo': 'baz'})
    assert 'foo' in j2_vars

    # Test that Templar variables are in AnsibleJ2Vars
    assert 'dummy' in j2_vars

    # Test that locals are

# Generated at 2022-06-13 15:42:34.021131
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    templar = Templar(loader=None)
    templar.set_available_variables({'foo': {'bar': {'baz': 'qux'}}})
    j2vars = AnsibleJ2Vars(templar, {}, {})

    assert 'foo' in j2vars
    assert 'foo.bar' in j2vars
    assert 'foo.bar.baz' in j2vars
    assert 'foo.bar.nope' not in j2vars
    assert 'foo.nope.nope' not in j2vars
    assert 'nope' not in j2vars
    assert 'True' not in j2vars

# Generated at 2022-06-13 15:42:35.105577
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    #TODO
    pass


# Generated at 2022-06-13 15:42:42.160086
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.template import Templar
    import pytest

    class Dummy(object):
        pass

    templar = Templar(
        loader=None,
        variables={
            'foo': 'bar',
            'bar': 'foo'
        }
    )

    j2_vars = AnsibleJ2Vars(templar, { 'baz': 'foo' }, { 'egg': 'spam'})

    assert( len(j2_vars) == 4 )


# Generated at 2022-06-13 15:42:51.696507
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    from ansible.template import Templar

    # Test with unknown varname
    my_templar  = Templar()
    my_globals  = {"testkey": "testval"}
    with pytest.raises(KeyError):
        res = AnsibleJ2Vars(my_templar, my_globals)["unknown"]

    # Test with existing hostvars
    my_hostvars = {"host1": {"var1": "val1", "var2": "val2"}, "host2": {"var1": "val3", "var2": "val4"}}
    my_templar  = Templar(loader=None, variables=my_hostvars)
    my_globals  = {"testkey": "testval"}

# Generated at 2022-06-13 15:43:00.383259
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    templar = Templar()

    locals1 = {'a': 1, 'b': 2, 'c': 3}
    globals1 = {'x': 'abc', 'y': 'def', 'z': 'ghi'}
    available_variables1 = {'foo': 'bar', 'baz': 'bing'}
    val1 = AnsibleJ2Vars(templar, globals1, locals1)
    templar.available_variables = available_variables1
    assert('a' in val1)
    assert('foo' in val1)
    assert('x' in val1)
    assert('y' not in val1)

# Generated at 2022-06-13 15:43:12.882135
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    from ansible.template import Templar

    templar = Templar(loader=None)

    globals = dict()
    locals = dict()
    aj2vars = AnsibleJ2Vars(templar, globals, locals)

    def get_var(varname):
        return aj2vars[varname]

    # varname in self._locals
    locals['v1'] = 'v1'
    assert get_var('v1') == 'v1'

    # varname in self._templar.available_variables
    templar.available_variables['v2'] = 'v2'
    assert get_var('v2') == 'v2'

    # varname in self._globals
    globals['v3'] = 'v3'

# Generated at 2022-06-13 15:43:25.674715
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible import constants as C
    from ansible.template import Templar

    j2v = AnsibleJ2Vars(Templar({'name': 'test'}), {})
    assert 'name' in j2v
    assert j2v['name'] == 'test'
    assert 'vars' in j2v
    assert j2v['vars'] == {}
    try:
        j2v['unknown_name']
    except KeyError:
        pass
    else:
        assert False  # Should not reach this line

    j2v = AnsibleJ2Vars(Templar({'name': 'test', 'vars': {'name': 'test2'}}), {})
    assert 'name' in j2v
    assert j2v['name'] == 'test'
    assert 'vars' in j

# Generated at 2022-06-13 15:43:36.331548
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.module_utils._text import to_text
    from ansible.template import Templar

    # Test for: if varname in self._locals
    templar = Templar(loader=None, variables={})
    locals = {'var1': 'local_value1'}
    globals = {}
    ansible_j2_vars = AnsibleJ2Vars(templar, globals, locals)
    assert ansible_j2_vars['var1'] == 'local_value1'

    # Test for: if varname in self._templar.available_variables
    locals = {}
    globals = {}
    ansible_j2_vars = AnsibleJ2Vars(templar, globals, locals)

# Generated at 2022-06-13 15:43:46.533843
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    templar = Templar(loader=None, variables={}, fail_on_undefined=False)
    a = AnsibleJ2Vars(templar, {}, {})
    try:
        a['b']
        assert(False)
    except KeyError:
        assert(True)
    try:
        a['base']
        assert(False)
    except KeyError:
        assert(True)
    templar.available_variables = {'base': 'base', 'b': 'b'}
    try:
        x = a['base']
        assert(x=='base')
        assert(True)
    except KeyError:
        assert(False)

# Generated at 2022-06-13 15:43:54.709012
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    templar = Templar(loader=DataLoader(), variables=dict(foo='bar'))
    assert 'foo' in AnsibleJ2Vars(templar, dict(baz='buzz'))
    assert 'bar' == AnsibleJ2Vars(templar, dict(baz='buzz'))['foo']
    assert 'buzz' == AnsibleJ2Vars(templar, dict(baz='buzz'))['baz']
    assert 'buzz' != AnsibleJ2Vars(templar, dict(baz='buzz'))['foo']

# Generated at 2022-06-13 15:44:05.097357
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    import collections
    from ansible.playbook.play_context import PlayContext
    glob = dict(a = 1, b = 2, c = 3)
    loc = dict(d = 4, e = 5, f = 6)
    t = 'string'
    vars = dict(t = t)
    pc = PlayContext()
    templar = pc.get_templar()
    for k, v in iteritems(vars):
        templar._available_variables[k] = v
    ans = AnsibleJ2Vars(templar, glob, loc)
    res = set()
    for x in ans:
        res.add(x)
    exp = set()
    exp.update(glob, loc, vars)
    assert exp == res


# Generated at 2022-06-13 15:44:14.942424
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template.safe_eval import safe_eval
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    from ansible.parsing.vault import VaultLib
    from ansible.plugins.loader import vars_loader
    from ansible.plugins.dynamic_inventories import InventoryDirectory

    import os
    import sys

    def _create_templar():
        return Templar(loader=None, variables=dict(), vault_secrets=protected_vars_file, shared_loader_obj=None)

    def _fail(func, *args, **kwargs):
        "Wraps the given function in a try/except block and returns False if the function raises an exception."

# Generated at 2022-06-13 15:44:21.699966
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    '''
    test the method __contains__ of class AnsibleJ2Vars
    '''
    templar = dict()
    globals = dict()
    locals = dict()
    obj = AnsibleJ2Vars(templar, globals, locals)
    varname = 'varname'
    actual = obj.__contains__(varname)
    expected = False
    failmsg='expect %s,actual %s' % (expected, actual)
    assert actual == expected, failmsg



# Generated at 2022-06-13 15:44:28.308420
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template.safe_eval import ansible_safe_eval
    from ansible.template import Templar
    from ansible.templating import templar

    obj_AnsibleJ2Vars = AnsibleJ2Vars(templar, {}, locals={})
    assert not (obj_AnsibleJ2Vars.__contains__('vars_1'))
    assert not (obj_AnsibleJ2Vars.__contains__('vars_2'))

    #
    #  Adding some test variables to the templar object
    #    - vars_1 : variable present
    #    - vars_2 : variable missing
    templar._available_variables = ansible_safe_eval({'vars_1':'value_1'})

    assert obj_AnsibleJ

# Generated at 2022-06-13 15:44:40.511190
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from jinja2.runtime import Undefined
    import sys

    class NotMapping:
        '''
        class used to test 'variable' argument of method __getitem__ of class AnsibleJ2Vars
        '''
        pass

    class Templar:
        '''
        class used to by pass __init__ method of class AnsibleJ2Vars
        '''
        def __init__(self):
            self.available_variables = {'foo': 'bar'}

        def template(self, variable):
            return variable

    # check that __getitem__ returns the value of a key of self._locals dictionary
    templar = Templar()
    ajv = AnsibleJ2Vars(templar, globals={'bar': 'baz'}, locals={'foo': 'bar'})
    assert aj

# Generated at 2022-06-13 15:45:07.495079
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    import pytest
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar
    from ansible.inventory.manager import InventoryManager

    # Test with simple dict variables
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    variable_manager.extra_vars = dict(
        hostvars=dict(foo='bar'),
        playvars=dict(bar='foo'),
    )
    templar = Templar(loader=loader, variables=variable_manager)

    # variable_manager.extra_vars should not exist in the AnsibleJ2Vars instance

# Generated at 2022-06-13 15:45:17.803973
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    # test-1
    templar = object()
    globals = {}
    locals = {}
    var_container = AnsibleJ2Vars(templar, globals, locals)
    var_name = 'fake_var'
    assert (var_name not in var_container)

    # test-2
    templar = object()
    globals = {}
    locals = {'fake_var': None}
    var_container = AnsibleJ2Vars(templar, globals, locals)
    var_name = 'fake_var'
    assert (var_name in var_container)

    # test-3
    templar = object()
    globals = {'fake_var': None}
    locals = {}

# Generated at 2022-06-13 15:45:20.558186
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    # There is no dict.__contains__
    assert not dict.__contains__({}, 'a')

    ansible_j2_vars = AnsibleJ2Vars(templar=None, globals={'a': 1}, locals={'b': 2})
    assert 'a' in ansible_j2_vars
    assert 'b' in ansible_j2_vars
    assert 'c' not in ansible_j2_vars


# Generated at 2022-06-13 15:45:32.758542
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    # Create a stub for class Templar and set it as the attribute _templar of the object AnsibleJ2Vars
    from ansible.parsing.template import Templar
    templar_object = Templar(loader=None)
    AnsibleJ2Vars._templar = templar_object

    # Create a stub for class HostVars and set it as the attribute HostVars of the object AnsibleJ2Vars
    from ansible.vars.hostvars import HostVars
    ansible_j2_vars_object = AnsibleJ2Vars(templar=templar_object, globals={}, locals={})
    AnsibleJ2Vars.HostVars = HostVars

    # Create a stub for class AnsibleUndefinedVariable and set it as the attribute AnsibleUndefinedVariable of the object Ansible

# Generated at 2022-06-13 15:45:43.079007
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template.safe_eval import SafeEval

    # setup test object to test
    templar = SafeEval()
    test_globals = { "foo": "bar" }
    test_locals = { "foo": "baz" }
    test_ansiblej2vars = AnsibleJ2Vars(templar, test_globals, test_locals)

    # test existing local variables
    # is string
    assert(test_ansiblej2vars["foo"] == "baz")
    # is list
    assert(test_ansiblej2vars["l_play_hosts"] == [])
    # is dict
    assert(test_ansiblej2vars["l_hostvars"] == {})

    # test not existing local variables

# Generated at 2022-06-13 15:45:52.211976
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.module_utils.six import add_metaclass
    import ansible.module_utils.common.jsoncompat

    class Templar(object):
        available_variables = dict(var1='var1', var2='var2')

        def template(self, value):
            return value

    @add_metaclass(MutableMapping.__metaclass__)
    class VarsModule(object):
        def __init__(self, vars_dict):
            self.vars_dict = vars_dict

        def __getitem__(self, varname):
            return self.vars_dict[varname]



# Generated at 2022-06-13 15:46:03.191729
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import os
    import sys
    import unittest

    # FIXME: Don't use the fact that we have modules in the current directory
    sys.path.append(os.getcwd())

    from ansible.parsing.vault import VaultLib
    from ansible.templating import Templar
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    class TestAnsibleJ2Vars(unittest.TestCase):

        def setUp(self):
            self.unvault_secret = 'foo'
            self.vault_secret = VaultLib().encrypt(self.unvault_secret)
            self.templar = Templar()
            self.templar.set_available_variables({'vault_secret': self.vault_secret})
            self.ansible_j

# Generated at 2022-06-13 15:46:14.747567
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()
    aj2v = AnsibleJ2Vars(variable_manager.get_vars, {}, {'l_foo': 1, 'l_bar': 2})
    assert aj2v['foo'] == 1
    assert aj2v['bar'] == 2
    variable_manager.set_host_variable('host1', 'hostvars_var', 10)
    assert aj2v['hostvars_var'] == 10
    variable_manager.set_host_variable('host2', 'hostvars_var', 15)
    assert aj2v['hostvars_var'] == 10
    variable_manager.set_host_

# Generated at 2022-06-13 15:46:23.894161
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    '''
    This method tests __getitem__ method of `AnsibleJ2Vars` class.
    '''
    # Importing module here to avoid external dependencies
    import ansible.template
    # Set up the variables
    available_variables = {'item1': 'value1', 'item2': 'value2', 'item3': '{{ var }}'}
    locals_ = {'our_var': 'value3'}
    globals_ = {'global_var': 'value4'}
    templar = ansible.template.Templar(loader=None, variables=available_variables)
    ansible_vars = AnsibleJ2Vars(templar, globals_, locals_)
    # Testing our setup
    assert 'item1' in ansible_vars
    assert 'item2'

# Generated at 2022-06-13 15:46:28.113475
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.template import Templar
    templar = Templar()
    vars = AnsibleJ2Vars(templar, {})
    actual = vars.__len__()
    assert 0 == actual
    

# Generated at 2022-06-13 15:46:50.745020
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    # arrrange
    globals = {
        'test': 'ok'
    }

    from ansible.parsing.vault import VaultLib
    from ansible.plugins.loader import vars_loader
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    templar = Templar(vars_loader=vars_loader(), vault_secrets=VaultLib())
    variables = {
        'test': 'ko'
    }
    templar.set_available_variables(variables)
    variables['vars'] = variables

    locals = {
        'test2': 'ko'
    }

    j2vars = AnsibleJ2Vars(templar, globals, locals)

    #act
    result = j2vars['test']



# Generated at 2022-06-13 15:46:55.594721
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from ansible.template.safe_eval import safe_eval

    a = safe_eval("dict(A=1, B=2 , C=3)")
    b = safe_eval("dict(D=4, B=3 , E=6)")

    ansible_vars = AnsibleJ2Vars(None, b, a)
    assert(ansible_vars['A'] ==  1)
    assert(ansible_vars['D'] ==  4)
    assert(ansible_vars['B'] ==  2)
    assert(ansible_vars['C'] ==  3)
    assert(ansible_vars['E'] ==  6)

# Generated at 2022-06-13 15:47:05.732355
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    class Templar:
        def __init__(self, available_variables):
            self.available_variables = available_variables

    class Global:
        pass

    templar = Templar({'x': 'y'})
    globals = {'a': 'b'}

    # Testing with no locals
    vars = AnsibleJ2Vars(templar, globals)

    assert len(vars) == 3, 'Expected 3 but returned %d' % (len(vars))

    # Testing with locals
    locals = {'c': 'd', 'e': 'f'}
    vars = AnsibleJ2Vars(templar, globals, locals)

    assert len(vars) == 5, 'Expected 5 but returned %d' % (len(vars))


# Generated at 2022-06-13 15:47:14.009036
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
  from ansible.playbook.play_context import PlayContext
  from ansible.template import Templar
  from ansible.vars.hostvars import HostVars

  play_context = PlayContext()
  templar = Templar(loader=None, variables=play_context)
  template = AnsibleJ2Vars(templar, {
    'my_new_variable': 'value',
    'my_new_variable2': 'value2',
    'my_new_variable3': 'value3'
  })
  print('Template result: ')
  print(template._templar)
  print('Template globals: ')
  print(template._globals)
  print('Template locals: ')
  print(template._locals)

# Generated at 2022-06-13 15:47:21.937203
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    try:
        from ansible.playbook.play_context import PlayContext
        context = PlayContext()
        templar = Templar(loader=None, variables={}, shared_loader_obj=None)
        vars_ = AnsibleJ2Vars(templar, {'a':1}, {})
        assert 'a' in vars_
        assert 'b' not in vars_
        assert 'a' in AnsibleJ2Vars(templar, {'a':1}, {'a':2})
    except ImportError:
        pass


# Generated at 2022-06-13 15:47:24.670922
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    # Create the instance
    ajv = AnsibleJ2Vars(None, None)
    iter_obj = ajv.__iter__()
    assert isinstance(iter_obj, iter)


# Generated at 2022-06-13 15:47:33.129409
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():

    import copy

    import jinja2
    from ansible.parsing.vault import get_vault_secret
    from ansible.template import Templar
    from ansible.vars._merge import merge_hash
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.basic import AnsibleModule

    playbook_vars = dict(
        ansible_connection='local',
        ansible_python_interpreter='/usr/bin/python',
        ansible_managed='Ansible managed: Do NOT edit this file manually!',
        ansible_inventory_sources=[],
    )

# Generated at 2022-06-13 15:47:40.738169
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import copy

    from ansible.playbook.role import Role
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.included_file import IncludedFile
    from ansible.vars import VariableManager
    from ansible.template import Templar

    from ansible.plugins.loader import get_all_plugin_loaders

    plugin_classes = get_all_plugin_loaders()

    playbook = Play()
    host = "127.0.0.1"

    variable_manager = VariableManager()
    variable_manager.set_nonpersistent_facts({host: {'foo': 'test', 'bar': 42, 'baz': ['test1', 'test2', 'test3']}})

    templar

# Generated at 2022-06-13 15:47:51.558422
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template.safe_eval import safe_eval

    raw_variables = {
        'k1': 'v1',
        'k2': 'v2',
        'k3': 'v3',
        'k4': '{{ "v4" }}',
        'k5': '{{ k1 }}',
        'k6': '{{ k3 }}',
    }

    def _get_templar(variables):
        return safe_eval.AnsibleJ2Template(variables, loader=None)

    # Case 1: 'k4' is a not a valid Jinja2 expression
    test_cases = (
        ('k4', "v4"),
    )

    for test_case in test_cases:
        with pytest.raises(AnsibleError):
            _test_case_An

# Generated at 2022-06-13 15:47:59.373326
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import sys
    import os

    # ansible path
    ansible_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

    sys.path.append(ansible_path)

    from ansible.module_utils.six import StringIO
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.mod_args import ModuleArgsParser

    data = '---\n' \
           'foo: "{{ missing }}"\n'

    module_vars = ModuleArgsParser.parse(task_ds=data, variable_manager=None)

    from ansible.playbook.play import Play


# Generated at 2022-06-13 15:48:32.034523
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    from ansible.template.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.utils.vars import combine_vars

    all_vars = VariableManager()
    templar = Templar(loader=None, shared_loader_obj=None, variables=all_vars)
    templar._available_variables = {
        'var_1': 1,
        'var_2': 2,
        'var_3': 3,
        'var_4': 4,
        'var_5': 5,
    }

    # Test where locals and globals are empty
    ansible_j2_vars = AnsibleJ2Vars(templar, {})
    keys_0 = set()