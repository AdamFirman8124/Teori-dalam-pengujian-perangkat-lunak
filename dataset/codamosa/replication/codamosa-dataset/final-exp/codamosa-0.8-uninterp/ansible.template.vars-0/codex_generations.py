

# Generated at 2022-06-13 15:38:36.564441
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    AnsibleJ2Vars.__getitem__(None, None)


# Generated at 2022-06-13 15:38:42.657566
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    import ansible.template
    templar = ansible.template.Templar()
    test_obj = AnsibleJ2Vars(templar, globals={'foo': 'bar'})
    assert "foo" in test_obj, "foo not in test_obj"
    assert "bar" not in test_obj, "bar in test_obj"


# Generated at 2022-06-13 15:38:51.999821
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret

    from ansible.template import Templar

    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import UnsafeProxy

    vault_secret = VaultSecret('ansible', u'\u1234', None)
    vault_lib = VaultLib([vault_secret])
    templar = Templar(loader=None, variables={}, vault_secrets=[vault_secret])

    ansible_vars1 = AnsibleJ2Vars(templar, {'vault_password': 'ANSIBLESECRET'})
    # len(ansible_vars1) == 0


# Generated at 2022-06-13 15:38:59.949686
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    from ansible.template import Templar
    from ansible.vars.clean import strip_internal_keys
    from ansible.inventory.host import Host
    from ansible.playbook.play_context import PlayContext

    templar = Templar(loader=None, variables=[])
    globals = {}
    locals = {'_host': Host(name='127.0.0.1'), 'play_context': PlayContext()}
    vars = AnsibleJ2Vars(templar, globals, locals=locals)

    for var in vars:
        assert var in vars


# Generated at 2022-06-13 15:39:06.454850
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars


    #
    # Create a jinja context
    #
    from jinja2 import contextfilter
    from jinja2.environment import Environment as JinjaEnvironment
    from jinja2.loaders import DictLoader
    loader = DictLoader({'hello_world.j2': 'Hello World {{ foo.bar }}'})
    env = JinjaEnvironment(loader=loader, extensions=['jinja2.ext.do'],
                           undefined=jinja2.StrictUndefined,
                           finalize=None)

    #
    # Create a fake templar
    #
    t = Templar(loader=loader, variables={'foo': {'bar': 'BOOM'}})

    #
    # Create a

# Generated at 2022-06-13 15:39:18.098330
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    import jinja2
    from ansible.template import Templar

    templar = Templar(loader=None)
    globals = {}
    locals = {}

    vars_obj = AnsibleJ2Vars(templar, globals, locals)
    assert 'fact_a' in vars_obj
    assert 'fact_b' in vars_obj
    assert 'var_a' in vars_obj
    assert 'var_b' in vars_obj
    assert 'var_c' in vars_obj
    assert 'var_d' in vars_obj
    assert 'var_e' in vars_obj
    assert 'var_f' in vars_obj
    assert 'var_g' in vars_obj
    assert 'var_h' in vars_obj
    assert 'var_i'

# Generated at 2022-06-13 15:39:27.588559
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():

    from ansible.template import Templar
    vars = dict(var1=1, var2=2, var3=3)

    ajv = AnsibleJ2Vars(Templar(loader=None, variables=vars), dict())

    assert "var1" in ajv
    assert "var4" not in ajv

    for var in ['var1', 'var2', 'var3']:
        assert var in ajv
    for var in ['var4', 'var5', 'var6']:
        assert var not in ajv

    ajv_with_locals = AnsibleJ2Vars(Templar(loader=None, variables=vars), dict(), dict(var4=4, var5=5, var6=6))

    assert "var1" in ajv_with_loc

# Generated at 2022-06-13 15:39:39.109877
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    # Set up values
    variables = {
        'var1': 'value1',
        'var2': 'value2',
        'var3': 'value3',
    }
    globals = {
        'global1': 'value1',
        'global2': 'value2',
        'global3': 'value3',
    }
    locals = {
        'local1': 'value1',
        'local2': 'value2',
        'local3': 'value3',
    }

    # Initialze class object
    j2_vars_obj = AnsibleJ2Vars(play_context=PlayContext(variables=variables), globals=globals, locals=locals)

    # Test of __

# Generated at 2022-06-13 15:39:49.920710
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from jinja2 import DictLoader, Environment
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar

    j2_env = Environment(loader=DictLoader({}))
    j2_env.filters.update(dict())

    shared_loader = DataLoader()

    templar = Templar(loader=shared_loader, variables={}, jinja2_env=j2_env)
    ansvars = AnsibleJ2Vars(templar, globals={}, locals=dict())

    # test undefined variable
    try:
        res = ansvars['UNDEFINED_VARIABLE']
        raise AssertionError('AnsibleJ2Vars.__getitem__ should throw KeyError')
    except KeyError: pass

    # test undefined variable but

# Generated at 2022-06-13 15:39:58.766064
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import os
    import tempfile
    import unittest

    from ansible.template import Templar
    from ansible.vars.unsafe_proxy import wrap_var

    class TestCase(unittest.TestCase):
        def setUp(self):
            self.vars = dict(
                one=1,
                two=2,
                three=3,
                dict=dict(a="dict_a", b=dict(c="dict_b_c")),
                list=["a", "b", "c"],
                unsafe=wrap_var("not_safe"),
            )

# Generated at 2022-06-13 15:40:10.131615
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    my_vars = dict(a=10, b=[1, 2, 3, 4, 5], c='ansible', d=dict(d1='v1', d2='v2'))
    loader = DataLoader()
    inventory = VariableManager()
    templar = Templar(loader=loader, variables=inventory)
    inventory.set_variable_manager(inventory)

    vars = AnsibleJ2Vars(templar, {}, locals=my_vars)
    # all variables from locals, templar and globals, total 5
    assert len(vars) == 5

# Generated at 2022-06-13 15:40:22.219951
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template.safe_eval import literal_eval
    from ansible.template import Templar

    context = dict()
    context['l_tmpfile'] = '/srv/tmp/ansible-tmp-1409751158.22-275700569677372/source'
    context['l_enc_pass'] = '$6$oFZlz7EI$vwLz7V8JpNMuD7yKakv1RAbEXV9HypZupRnZCzetp6U.k48Uxg6Eb3qY3SWFJg7C9nO.F/QTB1KkT/w8ah7Cp/'
    context['l_dest'] = '/etc/ansible/facts.d/facts.fact'

# Generated at 2022-06-13 15:40:23.526690
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():

    # FIXME: write unit test for __contains__ method
    pass

# Generated at 2022-06-13 15:40:32.685370
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    from ansible.template.safe_eval import safe_eval
    from ansible import constants as C

    templar = Templar(loader=None, variables={'foo': 'bar'})
    templar.available_variables.update(safe_eval(C.DEFAULT_JINJA2_NATIVE_VARIABLES))
    templar.available_variables.update({'foo': 'bar'})
    a = AnsibleJ2Vars(templar, {})
    assert 'foo' in a
    assert 'ansible_foo' in a
    assert 'missing' not in a



# Generated at 2022-06-13 15:40:41.533284
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    class AnsibleJ2Vars_mock_template_class(object):
        def __init__(self, available_variables):
            self.available_variables = available_variables
        def template(self, variable):
            return self.available_variables[variable]

    globals = dict(a=1, b=2, c=3)
    locals = dict(l_e=10, l_f=20, l_g=30)
    vars = {"x": "vx", "y": "vy", "z": "vz"}
    templar = AnsibleJ2Vars_mock_template_class(vars)
    ansible_j2vars = AnsibleJ2Vars(templar, globals, locals)
    for key in globals.keys():
        assert key in ans

# Generated at 2022-06-13 15:40:50.069333
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    templar = Templar(loader=DictDataLoader({}))
    globals = dict()
    locals = dict()
    aj2vars = AnsibleJ2Vars(templar, globals, locals)
    for key in aj2vars:
        assert key in aj2vars
    assert "key" not in aj2vars
    locals = dict({"key": "value"})
    aj2vars = AnsibleJ2Vars(templar, globals, locals)
    assert "key" in aj2vars
    templar.available_variables = dict({"key": "value"})
    aj2vars = AnsibleJ2Vars(templar, globals, locals)
    assert "key" in aj2vars



# Generated at 2022-06-13 15:40:58.787016
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.module_utils.common._collections_compat import Mapping
    assert issubclass(AnsibleJ2Vars, Mapping)

    # Create mocked "templar"
    class MockTemplar(object):
        def __init__(self, variables):
            self._available_variables = variables
        @property
        def available_variables(self):
            return self._available_variables

    # Create mocked "globals"
    globals = {'foo': 'bar'}

    # Create instance of AnsibleJ2Vars
    ajv = AnsibleJ2Vars(templar=MockTemplar({'baz': 'boo', 'bar': 'boz'}), globals=globals, locals=None)

    # Execute tested method
    result = a

# Generated at 2022-06-13 15:41:00.004231
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    # TODO: Implement test for method __getitem__ of class AnsibleJ2Vars
    pass

# Generated at 2022-06-13 15:41:08.676677
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    mock_vars = dict(foo='bar')
    mock_play_context = PlayContext()
    mock_play_context.variable_manager = PythonVariableManager()
    mock_play_context.variable_manager.add_or_update_vars(host=mock_vars)
    mock_play_context.variable_manager.set_globals(globals=dict(baz='qux'))
    mock_templar = Templar(loader=None, variables=mock_play_context.variable_manager.get_vars())


# Generated at 2022-06-13 15:41:19.217647
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.constants import DEFAULT_TEMPLATE_JINJA2_EXT
    from ansible.module_utils.ansible_madule_hijack import AnsibleModule

    class AnsibleJ2Vars_test(AnsibleJ2Vars):
        def __init__(self):
            from ansible.template.safe_eval import AnsibleUnsafe
            from ansible.template.template import Templar
            from ansible.utils.vars import combine_vars


# Generated at 2022-06-13 15:41:33.771595
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    class HostVars(HostVars):
        pass
    templar = Templar()
    globals_dict = dict()
    locals_dict = dict()
    j2_vars = AnsibleJ2Vars(templar, globals_dict, locals_dict)
    assert j2_vars.__contains__("varname")
    assert not j2_vars.__contains__("varnam")
    assert not j2_vars.__contains__("")
    assert j2_vars.__contains__("varname")
    assert j2_vars.__contains__("varname")

# Generated at 2022-06-13 15:41:43.288157
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    import sys
    import os
    file_path = os.path.dirname(__file__)
    sys.path.append(file_path)

    from AnsibleJ2Vars import AnsibleJ2Vars
    from ansible.template import Templar
    from ansible.module_utils.six import string_types


# Generated at 2022-06-13 15:41:45.395421
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
  template_vars = {}
  templar =  AnsibleJ2Vars(template_vars, locals=None)
  assert templar['test'] == True

# Generated at 2022-06-13 15:41:58.079971
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    fail_msg = 'Method __contains__ of class AnsibleJ2Vars did not return expected result'
    vars = {'v1': 'val1', 'v2': 'val2'}
    globals = {'g1': 'gval1', 'g2': 'gval2'}
    locals = {'l1': 'lval1', 'l2': 'lval2'}

    # create a fake Templar object
    templar = type('Templar', (object,), {'available_variables': vars})
    # create a AnsibleJ2Vars object
    obj = AnsibleJ2Vars(templar, globals, locals=locals)

    # assert contains
    assert 'v1' in obj, fail_msg
    assert 'v2' in obj, fail_msg
   

# Generated at 2022-06-13 15:41:59.514224
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
	pass #TODO

# Generated at 2022-06-13 15:42:05.561483
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    templar = Templar(loader=None, variables={'a': 'a'})
    vars = AnsibleJ2Vars(templar=templar, globals={'b': 'b'}, locals={'c': 'c'})
    assert 'a' in vars
    assert 'b' in vars
    assert 'c' in vars
    assert 'd' not in vars


# Generated at 2022-06-13 15:42:11.444382
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    # Unit test for method __getitem__ of class AnsibleJ2Vars with no exception
    # unit test: (in __getitem__) if varname in self._locals:
    # unit test: (in __getitem__) if varname in self._templar.available_variables:
    # unit test: (in __getitem__) if varname in self._globals:

    class _MockTemplar(object):

        def __init__(self):
            self.available_variables = {'available_variable': 'ok'}

        def template(self, variable):
            return variable

    class _MockMapping(Mapping):

        def __getitem__(self, key):
            if key == 'variable_in_globals':
                return 'ok'


# Generated at 2022-06-13 15:42:17.931794
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    templar = {'_available_variables': {'foo': 'bar', 'fizz': 'buzz'}}
    globals = {'baz': 'bat'}
    locals = {'l_local': 'local'}
    vars_ = AnsibleJ2Vars(templar, globals, locals)
    assert ['foo', 'fizz', 'baz', 'local'] == list(vars_)


# Generated at 2022-06-13 15:42:27.119459
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    variables = {"var": "qux", "foo": {"bar": "qux"}, "foo|bar": "baz", "test": "ok"}

    import jinja2
    env = jinja2.Environment(extensions=['jinja2.ext.do'])
    templar = Templar(loader=None, variables=variables)
    local_variables = {"var": "foobar"}
    globals = {"foo": "bar"}

    vars_obj = AnsibleJ2Vars(templar, globals, local_variables)
    assert vars_obj.__contains__("var") == True
    assert vars_obj.__contains__("foo") == True
    assert vars_obj.__contains__("foo|bar") == True
    assert vars_obj.__contains__

# Generated at 2022-06-13 15:42:32.244988
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    templar = None
    globals = {'vars': {'test': 'globals'}}
    locals = {'test': 'locals'}
    proxy = AnsibleJ2Vars(templar, globals, locals)
    # function __iter__
    keys = set()
    keys.update(proxy)
    assert len(keys) == 1 and key in keys


# Generated at 2022-06-13 15:42:46.544817
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.callback import CallbackBase

    class ResultCallback(CallbackBase):
        """A sample callback plugin used for performing an action as results come in

        If you want to collect all results into a single object for processing at
        the end of the execution, look into utilizing the ``json`` callback plugin
        or writing your own custom callback plugin
        """

# Generated at 2022-06-13 15:42:50.735465
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible import template
    t = template. Templar(loader=None)
    t.set_available_variables(dict(vars=dict(a='a')))
    v = AnsibleJ2Vars(t, dict(b='b'))
    assert 'a' in v
    assert 'b' in v
    assert 'c' not in v


# Generated at 2022-06-13 15:42:55.284874
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    v = VariableManager()
    l = DataLoader()

    # TODO create a template for test
    t = None
    d = None
    j = AnsibleJ2Vars(t, d)

    assert j['name'] == 'ansible'

# Generated at 2022-06-13 15:43:01.495803
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    import json
    import sys
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../../')
    from ansible.template import Templar

    templar = Templar()

    # test data
    globals = {}
    locals = {'l_hostvars': {'hostvars_dict': {'host1': 'host1_dict'}}}

    ansible_j2_vars = AnsibleJ2Vars(templar, globals, locals)
    assert isinstance(ansible_j2_vars, AnsibleJ2Vars), "Object ansible_j2_vars has to be instance of class AnsibleJ2Vars"


# Generated at 2022-06-13 15:43:11.272670
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    class _Templar:
        available_variables = {'k1': 'v1', 'k2': '{{k3}}', 'k3': 'v3'}

        def template(self, variable):
            if variable in self.available_variables:
                return self.available_variables[variable]
            else:
                raise AnsibleUndefinedVariable(variable)

    _globals = {'k4': 'value4'}
    _locals = {'k5': 'value5'}

    _aj2v = AnsibleJ2Vars(_Templar(), _globals, _locals)

    assert _aj2v['k1'] == 'v1'
    assert _aj2v['k2'] == 'v3'
    assert _aj2v['k3'] == 'v3'


# Generated at 2022-06-13 15:43:23.459700
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    from ansible.template import Templar

    class TestTemplar(Templar):

        def __init__(self):
            self.available_variables = {}
            self.template = lambda x: x

    class TestVariable():

        def __init__(self, value):
            self.value = value

        def __UNSAFE__(self):
            return True

    class TestHostVars():

        def __init__(self):
            self.value = {}

    class TestVariable_bad():

        def __init__(self, value):
            self.value = value

    class TestVariable_bad_class():

        def __init__(self, value):
            self.value = value

        def __UNSAFE__(self):
            return True


# Generated at 2022-06-13 15:43:28.777536
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.template import Templar

    templar = Templar(loader=None)

    _globals = {'a':'AA', 'b':'BB'}
    _locals = {'c':'CC', 'd':'DD'}

    ajv = AnsibleJ2Vars(templar, _globals, locals=_locals)

    assert len(ajv) == 4


# Generated at 2022-06-13 15:43:39.779382
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.vars.hostvars import HostVars
    # Test when 'varname' found in _locals
    am = dict(a='5')
    ansiblej2vars = AnsibleJ2Vars(1, am)
    assert ansiblej2vars['a']=='5'

    # Test when 'varname' found in _templar
    am = dict(a=5)
    ansiblej2vars = AnsibleJ2Vars(1, am)
    ansiblej2vars._templar = dict(available_variables={'b': '7'})
    assert ansiblej2vars['b']=='7'

    # Test when 'varname' found in _globals
    am = dict(b=7)
    ansiblej2vars

# Generated at 2022-06-13 15:43:51.906935
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template.safe_eval import unsafe_eval

    j2vars = AnsibleJ2Vars(None, {})

    # Test with a variable that is in the dictionary of variables
    variable = 'var1'
    locals = {'var1': 'value1'}
    result = j2vars.__getitem__(variable)
    assert result == 'value1'

    # Test with a variable that is not in the dictionary of variables
    variable = 'var2'
    l = locals.copy()
    l[variable] = 'value2'
    j2vars = AnsibleJ2Vars(None, {}, locals=l)
    result = j2vars.__getitem__(variable)
    assert result == 'value2'

    # Test with an expression as variable
    expr = 'var1'

# Generated at 2022-06-13 15:43:52.779667
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    assert(False), "No test written yet"

# Generated at 2022-06-13 15:44:02.624705
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    templar = None
    globals = {'g1':1, 'g2':2}
    locals = {'l1':1, 'l2':2}
    ajv = AnsibleJ2Vars(templar, globals, locals)
    a = [i for i in ajv]
    assert set(a) == set(['g1', 'g2', 'l1', 'l2'])

# Generated at 2022-06-13 15:44:13.602497
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar

    templar = Templar(loader=None)
    globals = dict()

    # test with locals is None
    proxy = AnsibleJ2Vars(templar, globals, locals=None)
    assert proxy['vars'] == dict()
    assert proxy['hostvars'] == dict()

    # test with locals
    locals = dict(hostvars=dict(host1=dict(hostvar1='hostvar1-value', hostvar2='hostvar2-value')),
                  vars=dict(test_var1='test_var1'))
    proxy = AnsibleJ2Vars(templar, globals, locals=locals)

    assert proxy['vars'] == dict(test_var1='test_var1')

# Generated at 2022-06-13 15:44:14.750749
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    assert False, "Test not implemented"

# Generated at 2022-06-13 15:44:24.019382
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.vars.manager import VariableManager
    from ansible.parsing.vault import VaultLib
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.template import Templar

    vault_secret = None

    play_context = PlayContext()
    play_context.vault_password = vault_secret
    new_stdin = open(os.devnull, 'r')
    templar = Templar(loader=None, variables={}, vault_secrets=[vault_secret],
                      use_handlers=False, fail_on_undefined=False)


# Generated at 2022-06-13 15:44:24.461444
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    assert True

# Generated at 2022-06-13 15:44:29.546848
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    class Templar:
        def __init__(self):
            self.available_vars = {'test_key': 'test_val'}

    # Test func works with none nested dict
    dict_test = {'test_key2': 'test_val2'}
    class DictWrapper:
        def __init__(self, dic):
            self.dic = dic
        def __getitem__(self, key):
            return self.dic[key]
        def __contains__(self, key):
            return key in self.dic

    proxy = AnsibleJ2Vars(Templar(), DictWrapper(dict_test), locals={})
    assert proxy['test_key'] == 'test_val'
    assert proxy['test_key2'] == 'test_val2'

    # Test

# Generated at 2022-06-13 15:44:41.379525
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template.template import Templar
    from ansible.vars.hostvars import HostVars

    t = Templar(loader=None)
    t._available_variables = dict(a=dict(b=dict(c=10)))
    t._available_variables['testvar'] = 'testval'
    t._available_variables['foo'] = dict(bar='baz')
    t._available_variables['supervar'] = dict(__UNSAFE__=True)

    v = AnsibleJ2Vars(t, dict())

    assert v['testvar'] == 'testval'
    assert v['foo'] == dict(bar='baz')
    assert v['supervar'] == dict(__UNSAFE__=True)

    assert v['a.b.c'] == 10

# Generated at 2022-06-13 15:44:51.699488
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    # test variables
    test_variable = 'TEST_VARIABLE'
    test_variable_value = 'TEST_VARIABLE_VALUE'
    test_variable_value_templated = 'TEST_VARIABLE_VALUE_TEMPLATED'

    # create a templar
    templar = Templar(loader=None)
    # set 'TEST_VARIABLE' in the available variables
    templar._available_variables = {test_variable: test_variable_value}

    # create a globals
    globals = {}

    # create an AnsibleJ2Vars
    j2_vars = AnsibleJ2Vars(templar, globals)

    # test whether the templating by the AnsibleJ2Vars works
    assert test_variable_value_tem

# Generated at 2022-06-13 15:44:52.316570
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    pass

# Generated at 2022-06-13 15:45:04.601933
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    # patch jinja2_environment.get_template
    patch_get_template = lambda *args,**kwargs: 'patch_get_template'
    from jinja2 import Environment
    Environment.get_template = patch_get_template

    # patch jinja2.Environment._parse
    patch_environment__parse = lambda *args,**kwargs: (None, dict())
    patch_environment = {'_parse': patch_environment__parse}
    Environment.__getitem__ = lambda *args,**kwargs: patch_environment
    # patch jinja2.Environment._parse()
    def patch_environment__parse(s, with_environment=False, globals=None):
        return None, dict()
    patch_environment['_parse'] = patch_environment__parse

    # patch jinja2.Environment.globals

# Generated at 2022-06-13 15:45:18.430629
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import action_loader
    from ansible.template import Templar

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    from ansible.utils.vars import combine_vars

    inv_path = os.path.expanduser("~/git/ansible/test/inventory")
    inv_manager = InventoryManager(loader=DataLoader(), sources=[inv_path])

    vars_manager = VariableManager(loader=DataLoader())
    vars_manager.set_inventory(inv_manager)


# Generated at 2022-06-13 15:45:20.863785
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    templar = AnsibleJ2Vars(None, None, None)
    assert 'foo' not in templar

# Generated at 2022-06-13 15:45:24.084611
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    assert len(AnsibleJ2Vars(None, {})) == 0
    assert len(AnsibleJ2Vars(None, dict(ansible_fake_variable='example'))) == 1


# Generated at 2022-06-13 15:45:35.718502
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible import templar
    from collections import Mapping

    def test_helper(test_instance):
        # instance is a mapping
        assert isinstance(test_instance, Mapping)
        # instance is not empty
        assert len(test_instance) > 0
        # len(instance) is the result of len(instance.keys())
        assert len(test_instance) == len(test_instance.keys())

    templar._setup_template_class()
    test_instance = AnsibleJ2Vars(templar, globals=dict())
    test_helper(test_instance)

    test_instance = AnsibleJ2Vars(templar, globals=dict(), locals=dict())
    test_helper(test_instance)


# Generated at 2022-06-13 15:45:45.959054
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    # set up
    from ansible.template import Templar
    templar = Templar(loader=None, variables={})
    globals = {'key': 'globals'}
    locals = {'key': 'locals'}
    j2_vars = AnsibleJ2Vars(templar, globals, locals)

    # test for key in locals
    assert j2_vars['key'] == 'locals'

    # test for key in templar
    templar._available_variables = {'key': 'available_variables'}
    assert j2_vars['key'] == 'available_variables'

    # test for key in globals
    templar._available_variables = {}
    assert j2_vars['key'] == 'globals'

    # test for KeyError

# Generated at 2022-06-13 15:45:54.162406
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    """
    Test of retrieving an item from a jinja variable manager.
    Mainly tests if variable is correctly resolved
    """
    from ansible.template import Templar
    template_data = 'this is the {{ test_var }}'
    variable_manager = 'dummy variable manager'
    loader = 'dummy loader'
    shared_loader_obj = None
    variable_loader = 'dummy variable loader'
    context = dict()
    environment = 'dummy environment'
    templar = Templar(template_data, variable_manager, loader, shared_loader_obj, variable_loader, context, environment)
    globals = dict()
    locals = dict()
    vars = AnsibleJ2Vars(templar, globals, locals)
    resolved_variable = vars['test_var']
    # In current config, it

# Generated at 2022-06-13 15:46:02.075702
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():

    class MyTemplar(object):
        def __init__(self):
            self.available_variables = dict(x=1, y=2)

    class MyGlobals(object):
        def __init__(self):
            self.x = 1
            self.y = 2

    vars = AnsibleJ2Vars(MyTemplar(), MyGlobals())
    assert(len(vars) == 2)

    vars = AnsibleJ2Vars(MyTemplar(), MyGlobals(), locals=dict(x=3))
    assert(len(vars) == 3)


# Generated at 2022-06-13 15:46:08.499663
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar


# Generated at 2022-06-13 15:46:17.382707
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.vars.hostvars import HostVars
    from ansible.template import Templar
    hostvars = HostVars(dict(a=1, b=2, c=3))
    globals_vars = dict(a=4, b=5)
    templar = Templar(loader=None)
    templar._available_variables = dict(c=6)
    a = AnsibleJ2Vars(templar, globals_vars, locals=hostvars)
    assert a['a'] == 1
    assert a['b'] == 2
    assert a['c'] == 3
    assert a['d'] is None

# Generated at 2022-06-13 15:46:25.354451
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.vars import VariableManager
    from ansible.playbook.play import Play
    from ansible.template import Templar

    variable_manager = VariableManager()
    variable_manager.extra_vars = {'foo':'bar'}

    play_context = Play()
    templar = Templar(loader=None, variables=variable_manager, loader=None, shared_loader_obj=None)

    # test getitem
    vars = AnsibleJ2Vars(templar, globals={})

    # test getting an existing variable
    assert vars['foo'] == 'bar'

    # test getting an non-existing variable
    try:
        vars['bogus_var']
    except KeyError as e:
        assert e.message == "undefined variable: bogus_var"

# Generated at 2022-06-13 15:46:40.050443
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    from ansible.vars import dark
    from ansible.parsing.vault import VaultLib
    from ansible.template import Templar
    from ansible.template.vars import AnsibleJ2Vars

    templar = Templar(loader=None, variables=dark)
    variables = AnsibleJ2Vars(templar, dict())

    assert sorted(list(variables.__iter__())) == sorted(list(dark))


# Generated at 2022-06-13 15:46:45.808817
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    from ansible.template import Templar
    templar = Templar(loader=None)
    j2vars = AnsibleJ2Vars(templar, globals={'gval': 'gval'}, locals={'lval': 'lval'})
    assert set(j2vars) == {'gval', 'lval'}


# Generated at 2022-06-13 15:46:49.708497
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():

    # setup
    templar = None # FIXME
    globals = {}
    locals = {}
    j2vars = AnsibleJ2Vars(templar, globals, locals)

    # exercise
    count = len(j2vars)
    # assert
    assert count == 0



# Generated at 2022-06-13 15:46:55.806106
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    from ansible.vars import merge_hash

    host_vars = {'foo': 'bar', 'bla': 'blub'}
    play_vars = {'ham': 'eggs'}
    new_vars = merge_hash(host_vars, play_vars)
    templar = Templar(loader=None, variables=new_vars)

    expected = 'bar'
    vars = AnsibleJ2Vars(templar, globals=dict(), locals=dict())
    actual = vars['foo']
    assert expected == actual

    expected = HostVars(host_vars)
    actual = vars['vars']
    assert expected == actual

    expected = 'eggs'

# Generated at 2022-06-13 15:47:04.350487
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    variable_manager = VariableManager()
    variable_manager.set_globals()
    variable_manager.set_fact("l_foo", "bar")
    variable_manager.set_fact("baz", "qux")
    templar = Templar(loader=None, variables=variable_manager)
    vars = AnsibleJ2Vars(templar, variable_manager.extra_vars)
    assert "foo" in vars
    assert "baz" in vars
    assert "qux" not in vars


# Generated at 2022-06-13 15:47:13.250069
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    ansible_vars = {'var1': '{{var2}}', 'var2': 'value2'}
    ansible_globals = {'gvar1': 'value1', 'gvar2': 'value2'}
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    variable_manager = VariableManager()
    variable_manager.extra_vars = ansible_vars
    variable_manager.options_vars = ansible_vars
    variable_manager.options_vars['vars'] = ansible_vars
    templar = Templar(loader=None,
                      variables=variable_manager,
                      shared_loader_obj=None)


# Generated at 2022-06-13 15:47:23.666033
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from ansible.vars import VariableManager
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    variable_manager = VariableManager()
    variable_manager.extra_vars = dict(
        first_var='1'
    )

    variables = variable_manager.get_vars(loader=None, play=PlayContext(), include_hostvars=True)

    templar = Templar(loader=None, variables=variables)
    globals = dict(second_var='2')
    locals = dict(first_local='3', l_second_local='4')

    c = AnsibleJ2Vars(templar, globals, locals)

    # run assertions on member variables
    assert hasattr(c, '_locals')

# Generated at 2022-06-13 15:47:30.543194
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    """
    AnsibleJ2Vars: Test for method __iter__
    """

    from ansible.template import Templar

    templar = Templar(loader=None)
    ansible_j2_vars = AnsibleJ2Vars(templar, { 'key1': 'value1', 'key2': 'value2'})

    keys = {}
    for key in ansible_j2_vars:
        keys[key] = True

    if len(keys) != 2 or not ('key1' in keys and 'key2' in keys):
        raise AssertionError("Unexpected keys")


# Generated at 2022-06-13 15:47:35.309100
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
  from ansible.template import Templar
  
  globals = {
      'foo_bar_baz_1': 1,
      'foo_bar_baz_2': 2,
      'foo_bar_baz_3': 3,
  }
  
  templar = Templar()
  vars = AnsibleJ2Vars(templar, globals)

  print(len(vars))
  assert(len(vars) == 3)

  # Unit test for method __getitem__ of class AnsibleJ2Vars

# Generated at 2022-06-13 15:47:40.227464
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    from ansible import constants as C
    from ansible.utils.vars import combine_vars
    from ansible.inventory.host import Host
    from ansible.vars.hostvars import HostVars

    templar = Templar()
    host = Host(name='testhost')

    vars_dict = dict(a=1, b=2, c=3)
    host.vars = HostVars(vars=vars_dict, host=host)

    # Prepare the globals dict.
    g = dict()
    g['ansible_version'] = dict(string=C.__version__, full=C.__version__, major=C.__version__.split('.')[0], minor=C.__version__.split('.')[1])

# Generated at 2022-06-13 15:48:05.162814
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variables = VariableManager(loader=loader, inventory=inventory)

    # Test all parameters are passed correctly and break if not
    templar = Templar(loader, variables)
    j2vars = AnsibleJ2Vars(templar, {}, locals={})

    assert len(dict(j2vars)) == 0


# Generated at 2022-06-13 15:48:14.440036
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    locals = {'l_foo': 'foo', 'l_bar': 'bar'}
    available_variables = {'baz': 'baz'}
    globals = {'qux': 'qux'}
    ajv = AnsibleJ2Vars(None, globals, locals)
    ajv._templar.available_variables = available_variables
    assert('foo' in ajv)
    assert('bar' in ajv)
    assert('baz' in ajv)
    assert('qux' in ajv)


# Generated at 2022-06-13 15:48:18.186506
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    templar = None
    globals = {'myglobal': 'myglobalvalue'}
    locals = {'mylocal': 'mylocalvalue'}
    proxy = AnsibleJ2Vars(templar, globals, locals)
    assert 'myglobal' in proxy
    assert 'mylocal' in proxy
    assert 'mynotexisting' not in proxy



# Generated at 2022-06-13 15:48:24.705746
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.vars.manager import create_template_vars
    import jinja2

    templar = create_template_vars(None, None, None)
    var_proxy = AnsibleJ2Vars(templar, {})

    # Test __getitem__ with AnsibleVaultEncryptedUnicode as value