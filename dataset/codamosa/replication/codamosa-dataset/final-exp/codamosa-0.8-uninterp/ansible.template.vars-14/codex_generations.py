

# Generated at 2022-06-13 15:38:40.910754
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    from ansible.parsing.dataloader import DataLoader

    templar = Templar(loader=DataLoader())

    vars = AnsibleJ2Vars(templar, globals={})

    try:
        for var in vars:
            assert False
    except StopIteration:
        assert True

# Generated at 2022-06-13 15:38:50.730527
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    # pylint: disable=too-many-locals
    from ansible.template import Templar
    from ansible.vars.unsafe_proxy import wrap_var

    templar = Templar()
    globals = dict(a=wrap_var('abc'))
    locals = dict()
    vars = AnsibleJ2Vars(templar, globals, locals)

    # Test case: Try to get a variable from AnsibleJ2Vars object, which is not in
    # locals, globals or templates, then it should raise an exception.
    try:
        x = vars['xyz']
        assert (False)
    except KeyError as e:
        assert (e.args[0] == 'undefined variable: xyz')

    # Test case: Try to get a variable from AnsibleJ2Vars object,

# Generated at 2022-06-13 15:39:00.989483
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    # test that keyerror on undefined variable
    # the variable 'foo' is defined in the context _templar.available_variables
    # Locals is not defined
    assert ('foo' in _templar.available_variables) == True
    test_j2vars = AnsibleJ2Vars(_templar, _globals)
    try:
        test_j2vars["foo"]
    except:
        assert False
    try:
        test_j2vars["nofoo"]
    except:
        assert True
    # test whether the content of vars is accessible
    try:
        test_j2vars["vars"]
    except:
        assert False
    # test whether the content of vars is accessible

# Generated at 2022-06-13 15:39:07.155997
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import ansible.plugins.loader as plugin_loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.templating import Templar
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()
    group_vars = {}
    group_vars['group1'] = {}
    group_vars['group1']['gv11'] = 'value of gv11'
    group_vars['group1']['gv12'] = 'value of gv12'
    variable_manager.add_group_vars('group1', group_vars['group1'])

# Generated at 2022-06-13 15:39:18.473295
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    # Test: Get item defined in templar.available_variables
    templar = _Templar()
    templar.available_variables = _DictOfVars(var1=1)

    vars = AnsibleJ2Vars(templar, globals={}, locals={})
    assert vars['var1'] == 1

    # Test: Get item defined in locals
    locals = _DictOfVars(l_var1=1)
    vars = AnsibleJ2Vars(templar, globals={}, locals=locals)
    assert vars['var1'] == 1

    # Test: Get item defined in globals
    vars = AnsibleJ2Vars(templar, globals=_DictOfVars(var1=1), locals={})

# Generated at 2022-06-13 15:39:25.237506
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from ansible.template import Templar
    templar = Templar(loader=None)
    globals = dict(globals=1)
    locals = dict(locals=3)
    var_obj = AnsibleJ2Vars(templar, globals, locals)
    assert var_obj['globals'] == 1
    assert var_obj['locals'] == 3
    assert var_obj.add_locals(dict(locals_new=5))['locals_new'] == 5
    return True

# Generated at 2022-06-13 15:39:30.962091
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleMapping

    templar = Templar()
    globals = {"global_var":"global_value"}
    locals = AnsibleMapping()
    locals["local_var"] = "local_value"
    locals["local_var2"] = "local_value2"
    locals["l_local_var3"] = "local_value3"

    d = AnsibleJ2Vars(templar, globals, locals)
    assert set(d.__iter__()) == set(('global_var', 'local_var', 'local_var2', 'local_var3' ))



# Generated at 2022-06-13 15:39:41.795924
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import AnsibleUnsafe
    templar = Templar()
    globals = dict()
    locals = dict()

    vars = AnsibleJ2Vars(templar=templar, globals=globals, locals=locals)
    vars._templar.available_variables['vars'] = dict()
    vars._templar.available_variables['ansible_unsafe'] = AnsibleUnsafe("test")
    vars._templar.available_variables['ansible_hostvars'] = HostVars("test")
    vars._templar.available_variables['ansible_hostvars_key'] = AnsibleUnsafe

# Generated at 2022-06-13 15:39:52.977642
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
  from jinja2 import Template
  import ansible.template.safe_eval as safe_eval
  from ansible.module_utils.common._collections_compat import Mapping
  from ansible.module_utils.common.collections import is_list, is_sequence
  from ansible.template import Templar
  abc = AnsibleJ2Vars(Templar, {}, locals()) # __init__ must be called before anything else, else templar is not defined
  try:
    abc['vars']
    assert False, "should raise KeyError"
  except KeyError:
    pass
  try:
    abc['vars']
  except AnsibleUndefinedVariable as e:
    pass
  except Exception as e:
    assert False, "should raise AnsibleUndefinedVariable"


# Generated at 2022-06-13 15:40:00.616079
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():   # pylint: disable=too-many-locals,too-many-statements,too-many-branches
    import datetime
    from jinja2 import Template
    from ansible.parsing.ajson import AnsibleJSONEncoder
    from ansible.template import Templar, derived_var
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.vars.hostvars import HostVars
    from ansible.inventory.host import Host

    from ansible.vars.manager import VariableManager
    from ansible.inventory import Inventory

    host = Host('localhost')
    hostvars = HostVars(host=host, variables={'foo': 'bar'})
    hostvars_json = AnsibleJSONEncoder().encode(hostvars)

# Generated at 2022-06-13 15:40:08.718502
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    templar = None
    globals = {
        "foo": "bar",
        "baz": "bop"
    }
    locals = {
        "baz": "bip"
    }
    v = AnsibleJ2Vars(templar, globals, locals=locals)
    assert len(list(v.__iter__())) == 3
    assert len(list(v.__iter__())) == 3
    locals['bar'] = "foo"
    assert len(list(v.__iter__())) == 4


# Generated at 2022-06-13 15:40:21.193483
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    host_name = 'test_host'
    templar = Templar(loader=None, variables={host_name: {'a': 'b'}})
    globals = {'a': 'b'}
    locals = {host_name: {'c': 'd'}}
    aj2v = AnsibleJ2Vars(templar=templar, globals=globals, locals=locals)

    # Here we test that the class AnsibleJ2Vars works as a dict.
    # It should work.
    assert 'a' in aj2v

    # Here we test that the class AnsibleJ2Vars works as a dict.
    # It should work.
    assert 'b' in aj2v

    # Here

# Generated at 2022-06-13 15:40:32.279930
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    from ansible.vars.hostvars import HostVars
    from ansible.vars import VariableManager
    from ansible.template import Templar
    import jinja2

    vars_mgr = VariableManager()
    vars_mgr.set_host_variable('foo', 'bar')
    vars_mgr.set_host_variable('baz', 'qux')

    j2vars = AnsibleJ2Vars(Templar(loader=jinja2.DictLoader({}), variables=vars_mgr), {}, {'l_baz': 'loc'})
    vars_mgr.set_nonpersistent_facts(dict(foo='Foo', baz='Baz'))
    vars_mgr.set_facts(dict(baz="Baz"))


# Generated at 2022-06-13 15:40:41.241551
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    '''
    Unit test for method __getitem__ of class AnsibleJ2Vars.
    '''
    import ansible.playbook.play_context
    import ansible.vars.hostvars
    from ansible.template import Templar
    from . import TestModuleUtils
    from . import TestJinja2Utils

    class AnsibleJ2VarsTestCase(TestModuleUtils.AnsibleModuleTestCase):
        '''
        Test cases for method __getitem__ of class AnsibleJ2Vars.
        '''

        def setUp(self):
            super(AnsibleJ2VarsTestCase, self).setUp()

            self.inventory = TestJinja2Utils.mocked_inventory()

# Generated at 2022-06-13 15:40:47.443497
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    from ansible.errors import AnsibleUndefinedVariable
    from ansible.vars.hostvars import HostVars
    from ansible.vars import VariableManager

    globals_ = {'var1': 'val1', 'var2': 'val2'}

    locals_ = {'var3': 'val3', 'var4': 'val4'}

    variable_manager = VariableManager()
    variable_manager.set_globals(globals_)
    variable_manager.set_host_variable(host=None, varname='var5', value='val5')
    variable_manager.set_host_variable(host=None, varname='var6', value='val6')

    templar = Templar(loader=None, variables=variable_manager)
    ansible_v

# Generated at 2022-06-13 15:40:53.552960
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import ansible.template
    import ansible.vars
    import ansible.vars.hostvars
    import jinja2
    import copy

    # prepare data

# Generated at 2022-06-13 15:41:04.394368
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    templar = Templar(loader=None, variables={})

    ansible_j2vars = AnsibleJ2Vars(templar, globals={
        "foo": "bar",
        "baz": {"fizz": "buzz"}
    })

    # Test 1: Check if dict contains key foo
    assert "foo" in ansible_j2vars

    # Test 2: Check if dict contains key baz.fizz
    # This is a bug!!
    # https://github.com/ansible/ansible/issues/10030#issuecomment-84616018
    # assert "baz.fizz" in ansible_j2vars

    # Test 3: Check if dict contains key baz
   

# Generated at 2022-06-13 15:41:15.108449
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import unittest
    import ansible.template
    import ansible.vars.hostvars
    import ansible.vars.unsafe_proxy
    import string

    class TestCase(unittest.TestCase):
        def setUp(self):
            self.variables = dict(
                hostvars=dict(
                    foo=ansible.vars.hostvars.HostVars(
                        ansible.vars.unsafe_proxy.UnsafeProxy(dict(
                            bar='baz',
                            quux='qux',
                        )),
                    ),
                ),
                baz='qux',
                qux=['quux', 'corge'],
                corge='grault',
                garply='waldo',
                waldo=None,
            )

# Generated at 2022-06-13 15:41:19.962509
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    import os
    import tempfile
    from ansible.module_utils.common._collections_compat import Sequence
    from ansible.template import Templar
    from ansible.utils.unsafe_proxy import wrap_var

    # Create a temp file and write some data
    fd, fn = tempfile.mkstemp()
    os.close(fd)

    with open(fn, 'w') as f:
        f.write("test_file_contents")


# Generated at 2022-06-13 15:41:26.731079
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import copy
    import jsonschema
    import os
    import sys

    # Correctly setup testing environment
    os.chdir(os.path.dirname(__file__))
    sys.path.insert(0, os.path.abspath('..'))

    from ansible.module_utils.common.removed import removed
    from ansible.module_utils.common._collections_compat import Mapping, Set, Sequence
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils.six import binary_type, text_type
    from ansible.module_utils.six.moves import StringIO
    from ansible.module_utils.six.moves.urllib_parse import quote as urllib_quote

# Generated at 2022-06-13 15:41:31.902485
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    assert True


# Generated at 2022-06-13 15:41:42.120542
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    from jinja2.sandbox import SandboxedEnvironment
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.yaml.loader import AnsibleLoader

    templates_dir = './tests/templates'
    loader = AnsibleLoader(templates_dir, variable_start_string="{{", variable_end_string="}}")
    env = SandboxedEnvironment(loader=loader, extensions=['jinja2.ext.do'])

    # define test variables
    test_vars_globals = {
        'test_vars_globals_1': 'test_vars_globals_1'
    }

# Generated at 2022-06-13 15:41:45.129353
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    templar = {}
    globals_ = {}
    locals_ = {}

    assert AnsibleJ2Vars(templar, globals_)
    assert AnsibleJ2Vars(templar, globals_, locals_)

# Generated at 2022-06-13 15:41:50.423757
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from ansible.template import Templar

    templar = Templar(loader=None, variables={})
    ansible_vars = AnsibleJ2Vars(templar, globals={}, locals={})
    assert isinstance(ansible_vars, Mapping)

# Generated at 2022-06-13 15:42:01.068958
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    # Creating mock object for Templar
    import mock
    templar = mock.Mock()
    templar.available_variables = {
        'local_file': '/etc/local',
        'local_dir': '/etc/local/',
        'local_dir2': '/etc/local2/',
    }
    templar.template = lambda x : x
    # Creating mock object for globals
    globals = {
        'g_key1': 'g_value1'
    }
    locals = {
        'l_key1': 'l_value1',
        'context': 'context',
        'environment': 'environment',
        'template': 'template',
        'l_key2': 'l_value2',
    }

# Generated at 2022-06-13 15:42:11.342319
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    def test_getitem(self, varname):
        if varname in self._locals:
            return self._locals[varname]
        if varname in self._templar.available_variables:
            variable = self._templar.available_variables[varname]
        elif varname in self._globals:
            return self._globals[varname]
        else:
            raise KeyError("undefined variable: %s" % varname)

        # HostVars is special, return it as-is, as is the special variable
        # 'vars', which contains the vars structure
        from ansible.vars.hostvars import HostVars

# Generated at 2022-06-13 15:42:17.577963
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from ansible.template import Templar
    from ansible.vars import VariableManager

    vars = VariableManager()
    tmplar = Templar(vars=vars)
    var_proxy = AnsibleJ2Vars(tmplar, {})

    assert var_proxy._templar == tmplar
    assert var_proxy._globals == {}
    assert var_proxy._locals == {}

# Generated at 2022-06-13 15:42:26.911360
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    '''
    This test will check the condition of the __contains__ method in the
    AnsibleJ2Vars class
    '''
    def empty_init(self):
        '''
        An empty init that returns a new object
        '''
        return self.__class__()

    # Setup mocks
    templar = lambda: None
    templar.available_variables = {'foo':'bar'}

    globals = {'baz':'foo'}
    globals = AnsibleJ2Vars(templar, globals)

    # Test case 1: locals is None
    j2vars = AnsibleJ2Vars(templar, globals)
    assert j2vars.__contains__('foo') == True

# Generated at 2022-06-13 15:42:34.508123
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.template import Templar
    from ansible.inventory.manager import InventoryManager
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['localhost,',])
    variable_manager.set_inventory(inventory)
    templar = Templar(loader=loader, variables=variable_manager)
    globals = dict()
    locals = dict()
    ansible_j2_vars = AnsibleJ2Vars(templar, globals, locals)
    assert len(ansible_j2_vars) > 5


# Generated at 2022-06-13 15:42:35.595572
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    pass


# Generated at 2022-06-13 15:42:52.168859
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():

    from ansible.template.safe_eval import ansible_safe_eval
    from ansible.template.templar import Templar

    # Initialize class
    j2_vars = AnsibleJ2Vars(
        templar = Templar(loader=None, variables=ansible_safe_eval.build_safe_environment()),
        globals = {},
        locals  = None
    )

    assert set == type( set(j2_vars) )

# Generated at 2022-06-13 15:43:00.522052
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():

    globals = dict()
    locals = dict()
    templar = dict()

    # test when locals is not a dict
    try:
        locals = None
        result = AnsibleJ2Vars(templar, globals, locals=locals)
        for i in result:
            pass
    except TypeError as e:
        print(e)

    # test when locals is a dict
    try:
        locals = dict()
        result = AnsibleJ2Vars(templar, globals, locals=locals)
        for i in result:
            print(i)
    except TypeError as e:
        print(e)


# Generated at 2022-06-13 15:43:10.739469
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    from ansible import templar

    # Instanciate a AnsibleJ2Vars object
    ajv = AnsibleJ2Vars(templar.Templar(), {}, {})

    # Test if a variable is defined in the AnsibleJ2Vars object
    assert(True) == ("vars" in ajv)

    # Test if a variable is not defined in the AnsibleJ2Vars object
    assert(False) == ("my_var_is_not_defined" in ajv)

    # Test if a variable is correctly returned as a dict
    assert(dict) == type(ajv["vars"])

    # Test if an exception is raised when the variable is not defined in the object

# Generated at 2022-06-13 15:43:22.513731
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template.safe_eval import safe_eval
    from ansible.template import Templar
    from ansible.vars import VariableManager

    globals = {}
    locals = {}
    template_ds = {}
    j2vars = AnsibleJ2Vars(Templar(VariableManager(), loader=None, shared_loader_obj=None), globals, locals)

    j2vars._templar._available_variables = {}
    assert j2vars['foo'] == "undefined variable: foo"

    j2vars._templar._available_variables = {'foo' : 'bar'}
    assert j2vars['foo'] == 'bar'

    j2vars._templar._available_variables = {'foo' : 'bar'}
    assert j2vars['foo']

# Generated at 2022-06-13 15:43:31.078854
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template.safe_eval import safe_eval
    from ansible.template.templar import Templar
    from ansible.template.vars import AnsibleVars
    from ansible.playbook.play_context import PlayContext

    play_context = PlayContext()
    templar = Templar(play_context, loader=None, variables=AnsibleVars(loader=None, play_context=play_context))
    ajv = AnsibleJ2Vars(templar, {}, locals={"b":2})
    ajv.__getitem__("b") == 2
    try:
        ajv.__getitem__("a")
    except KeyError:
        pass
    except:
        raise
    else:
        raise Exception("should raise KeyError")

# Generated at 2022-06-13 15:43:38.981593
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    # Create instance of class AnsibleJ2Vars with valid params
    templar = "Templar"  # Fake
    globals = "Globals"  # Fake
    locals  = "Locals"   # Fake
    obj = AnsibleJ2Vars(templar, globals, locals)

    # Test all possible outputs
    assert obj.__contains__("Test1") is False
    assert obj.__contains__("Test2") is False
    assert obj.__contains__("Test3") is False



# Generated at 2022-06-13 15:43:43.181402
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    templar = Templar(loader=loader)
    vars = AnsibleJ2Vars(templar, {'test': 'value'})
    assert vars['test'] == 'value'

# Generated at 2022-06-13 15:43:50.366736
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.template import Templar
    t = Templar()
    vars = AnsibleJ2Vars(t, dict())
    assert len(vars) == 0
    vars._globals['foo'] = 'bar'
    assert len(vars) == 1
    vars._templar.available_variables = {'bar': 'baz'}
    assert len(vars) == 2
    vars._locals['baz'] = 'bye'
    assert len(vars) == 3

# Generated at 2022-06-13 15:43:52.946418
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    templar = Templar(loader=None)
    ansible_j2_vars = AnsibleJ2Vars(templar, dict())

    templar.available_variables = dict(key1=dict(val1='val1'))
    value = ansible_j2_vars['key1.val1']
    assert value == 'val1'

# Generated at 2022-06-13 15:44:04.342629
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    templar = dict()
    vars = dict()

    locals = dict()
    locals['l_a'] = AnsibleUnsafeText('value_a')
    locals['l_b'] = AnsibleUnsafeText('value_b')
    locals['l_c'] = AnsibleUnsafeText('value_c')
    locals['l_d'] = AnsibleUnsafeText('value_d')
    locals['l_e'] = AnsibleUnsafeText('value_e')

    vars['a'] = AnsibleUnsafeText('value_a')
    vars['b'] = AnsibleUnsafeText('value_b')
    vars['c'] = AnsibleUnsafeText

# Generated at 2022-06-13 15:44:18.798472
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    templar = Templar(loader=None)

    plain_variable = {'vars_always_plain': '{{ foo }}',
                      'vars_with_default': '{{ foo | default("bar") }}'}
    unsafe_variable = {'vars_unsafe_variable': '{{ foo }}',
                       '__UNSAFE__': True}
    hostvars = HostVars()
    hostvars.add_host("example.org")
    hostvars.set_variable("example.org", "foo", "bar")

    variables = AnsibleJ2Vars(templar, {'hostvars': hostvars}, locals=plain_variable)
    # variables['vars_with_default'] = '{{

# Generated at 2022-06-13 15:44:26.669629
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    from ansible.template import Templar

    test_templar = Templar(loader=None)
    test_globals = {
        'g_colours': ['red', 'green', 'blue'],
        'g_age': 21,
        'g_greeting': 'Hello dear %s.',
        'g_str': 'The string',
        'g_int': 12,
        'g_list': ['A','B','C','D','E','F','G'],
        'g_dict': {
            'key1': 'value1',
            'key2': 'value2',
        }
    }

# Generated at 2022-06-13 15:44:38.996194
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    try:
        import jinja2
        from ansible.template import Templar
    except Exception as e:
        raise SkipTest(
            "Skipping due to missing jinja2 module: %s" % to_native(e)
        )

    myvars = dict(a=1, b=2, c=3)
    templar = Templar(loader=None)
    templar.set_available_variables(myvars)

    assert "" not in AnsibleJ2Vars(templar, {})
    assert "a" in AnsibleJ2Vars(templar, {})

    assert "d" not in AnsibleJ2Vars(templar, {})
    assert "d" not in AnsibleJ2Vars(templar, {'d': 4})

# Generated at 2022-06-13 15:44:48.461026
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from ansible.template.safe_eval import unsafe_eval
    from ansible.template.template import Templar
    from ansible.vars.hostvars import HostVars
    templar = Templar(loader=None, variables={'varname': 'varvalue', 'varlist': [1,2,3], 'vardict': {'key1': 42, 'key2': 'val2'}, 'varansible': HostVars(vars={'key1': 'val1'})})
    vars = AnsibleJ2Vars(templar, globals={'globalname': 'globalvalue'})

    # test __contains__
    assert 'varname' in vars
    assert 'varlist' in vars
    assert 'vardict' in vars
    assert 'varansible' in vars

# Generated at 2022-06-13 15:44:52.730107
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.template import Templar
    assert len(AnsibleJ2Vars(Templar(), {}, {})) == 0
    assert len(AnsibleJ2Vars(Templar(), {'g': 1}, {})) == 1
    assert len(AnsibleJ2Vars(Templar(), {'g': 1}, {'l': 2})) == 2

# Generated at 2022-06-13 15:44:54.614182
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    result = AnsibleJ2Vars.__len__()
    assert result is not None


# Generated at 2022-06-13 15:45:06.670343
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.vars.hostvars import HostVars

    mock_templar = {}
    mock_templar['available_variables'] = {'test_var': 'ok'}
    mock_templar['template'] = lambda x: x

    mock_globals = {}

    A = AnsibleJ2Vars(mock_templar, mock_globals)

    mock_locals = {}
    mock_locals['test_local'] = 'ok'

    result = A.add_locals(mock_locals)

    assert result['test_var'] == mock_templar['available_variables']['test_var']
    assert result['test_local'] == mock_locals['test_local']

    # HostVars is special, return it as-is, as is

# Generated at 2022-06-13 15:45:17.719055
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    import pytest
    from ansible.vars.hostvars import HostVars
    from units.mock.loader import DictDataLoader

    def test_hostvars():
        templar = DictDataLoader({})
        assert AnsibleJ2Vars(templar, {}, locals={}).__getitem__('hostvars') == {'dummy':42}

    def test_dict():
        templar = DictDataLoader({})
        assert AnsibleJ2Vars(templar, {}, locals={'d':{'value':42}}).__getitem__('d') == {'value':42}

    def test_HostVars():
        templar = DictDataLoader({})

# Generated at 2022-06-13 15:45:19.986836
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    with pytest.raises(KeyError):
        var = {'test': '{{test2}}', 'test2': '{{test3}}', 'test3': '{{test4}}', }
        j2v = AnsibleJ2Vars(Templar(loader=DataLoader()), var)
        print(j2v.__getitem__('test'))

# Generated at 2022-06-13 15:45:29.498965
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.template import Templar
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    var = '{{ name }}'

    vars = AnsibleJ2Vars(
        templar=Templar(loader=None),
        globals={},
        locals={
            'name': AnsibleUnsafeText(var)
        }
    )

    assert isinstance(vars, Mapping) is True
    assert len(vars) == 1


# Generated at 2022-06-13 15:46:00.018148
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    # test __contains__ with empty dictionary
    templar = mock_templar()
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars.__contains__('foo') == False

    # test __contains__ with a variable
    j2vars = AnsibleJ2Vars(templar, {})
    templar.available_variables['foo'] = 'bar'
    assert j2vars.__contains__('foo') == True

    # test __contains__ with a global variable
    j2vars = AnsibleJ2Vars(templar, {'foo': 'bar'})
    assert j2vars.__contains__('foo') == True

    # test __contains__ with a local variable
    j2vars = Ans

# Generated at 2022-06-13 15:46:06.513408
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    from ansible.template import Templar
    (tmplar, res) = Templar._load_vars_file('tests/vars/test_vars.yml')
    # we assume test_vars.yml contains the following contents:
    #---
    #myvar1: TEST1
    #myvar2: TEST2
    #myvar3: TEST3
    testvars = AnsibleJ2Vars(tmplar, {}, {})
    varlist = sorted([k for k in testvars])
    assert(len(varlist) == 3)
    assert(sorted(['myvar1', 'myvar2', 'myvar3']) == varlist)


# Generated at 2022-06-13 15:46:11.433995
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from ansible.templating import Templar

    my_templar = Templar(loader=None, variables={})
    assert isinstance(AnsibleJ2Vars(my_templar, {}), AnsibleJ2Vars)
    assert isinstance(AnsibleJ2Vars(my_templar, {}, locals={}), AnsibleJ2Vars)

# Generated at 2022-06-13 15:46:21.945064
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import json
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    variable_manager = VariableManager()
    loader = DataLoader()

    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager.set_inventory(inventory)

    play_context = PlayContext()

    templar = Templar(loader=loader, variables=variable_manager,
                      all_vars=dict(foo='bar'), follow_parent_dag=False)

    args_locals = dict(foo1='bar1', foo2='bar2', foo3='bar3')


# Generated at 2022-06-13 15:46:33.147516
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.parsing.utils.jinja2_native import AnsibleJinja2NativeEnvironment
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    env = AnsibleJinja2NativeEnvironment(loader=None)
    tmp = Templar(env=env)
    context = PlayContext()
    context.set_options(variable_manager={'defaults': {}, 'vars': {}})
    tmp.set_available_variables(context)

    def test_getitem(expected, key):
        returned = AnsibleJ2Vars(tmp, {}, {})[key]
        assert returned == expected, "expected '%s' for key '%s' got '%s'" % (expected, key, returned)

    from ansible.vars.hostvars import HostV

# Generated at 2022-06-13 15:46:39.365243
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    # test class variable
    templar = "A variable"
    globals = "A variable"
    locals = "A variable"
    ansiblej2vars = AnsibleJ2Vars(templar, globals, locals)
    iter = ansiblej2vars.__iter__()
    assert iter.__next__() == None


# Generated at 2022-06-13 15:46:50.120614
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    from ansible.module_utils.six import PY3
    from ansible.vars.hostvars import HostVars
    try:
        from unittest import mock
    except ImportError:
        import mock
    templar = mock.create_autospec(Templar)
    globals = {'global_dict': 'global_dict_value'}
    locals = {'local_dict': 'local_dict_value'}
    ansible_j2_vars = AnsibleJ2Vars(templar, globals, locals)
    if PY3:
        assert not ansible_j2_vars.__contains__('not_exist')
        assert 'global_dict' in ansible_j2_vars
        assert 'local_dict' in ans

# Generated at 2022-06-13 15:47:00.768168
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from ansible.template import Templar
    from ansible.playbook.play_context import PlayContext

    vars_dict =  {'foo': 'bar',
                  'sub1': {'subsub1': {'subsubsub1': 'subsubsubsub1',
                                       'subsubsub2': 'subsubsubsub2',
                                       'subsubsub3': 'subsubsubsub3'}},
                  'sub2': {'subsub2': {'subsubsub1': 'subsubsubsub1',
                                       'subsubsub2': 'subsubsubsub2',
                                       'subsubsub3': 'subsubsubsub3'}}}

    templar = Templar(loader=None, variables=vars_dict)


# Generated at 2022-06-13 15:47:06.175761
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    loc = {'l_foo': 'bar'}
    templar = 'helloworld'
    glo = {'g_foo': 'bar'}
    ajv = AnsibleJ2Vars(templar, glo, loc)
    assert 'l_foo' in ajv
    assert 'foo' in ajv
    assert 'g_foo' in ajv
    assert 'g__foo' in ajv


# Generated at 2022-06-13 15:47:14.853494
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from ansible.template import Templar
    mytemplar = Templar(loader=None)
    myglobals = {'a': 1}
    mylocals = {'b': 1, 'c': 2}
    vars = AnsibleJ2Vars(mytemplar, myglobals, locals=mylocals)

    assert vars['a'] == 1
    assert vars['b'] == 1
    assert vars['c'] == 2
    assert vars.__contains__('b') is True
    assert len(vars) == 2


#
# (c) 2012, 2013 Michael DeHaan, <michael.dehaan@gmail.com>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of

# Generated at 2022-06-13 15:47:42.380895
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.vars.unsafe_proxy import UnsafeProxy

    VARS = dict(foo=1, bar=2, baz=3, qux=4)
    TEMPLAR = Templar(VariableManager())
    TEMPLAR.available_variables = VARS
    j2v = AnsibleJ2Vars(TEMPLAR, dict())

    assert 'foo' in j2v
    assert 'bar' in j2v
    assert 'baz' in j2v
    assert 'qux' in j2v
    assert 'quux' not in j2v



# Generated at 2022-06-13 15:47:43.339596
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    pass

# Generated at 2022-06-13 15:47:53.635189
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
  templar="""
---
- hosts: localhost
  gather_facts: no
  vars:
    var1:
      key1: value1
      key2: value2
  tasks:
    - debug:
        msg: "{{ var1 }}"
  """

  from ansible.playbook.play_context import PlayContext
  from ansible.template import Templar
  from ansible.vars import VariableManager
  from ansible.inventory.manager import InventoryManager

  from io import StringIO

  loader = DataLoader()
  variable_manager = VariableManager()
  host_list=InventoryManager(loader=loader, sources=['localhost,'])

# Generated at 2022-06-13 15:48:05.392795
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    import copy
    from ansible.template import Templar, AnsibleJ2Vars

    templar = Templar(loader=None, variables=dict())

    vars=AnsibleJ2Vars(templar, dict(x=1, y=2))

    # unit test for the class instantiation
    assert vars._templar == templar
    assert vars._globals == dict(x=1, y=2)
    assert vars._locals == dict()
    assert vars.__contains__('x') == True

    # unit test for method __iter__ of class AnsibleJ2Vars
    assert set(vars.__iter__()) == set(['x', 'y'])

    # unit test for method __len__ of class AnsibleJ2Vars
    assert vars.__len__()

# Generated at 2022-06-13 15:48:09.258442
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    result = True
    print("Test AnsibleJ2Vars.__iter__")
    print("TODO")
    print("Done")
    return result


# Generated at 2022-06-13 15:48:17.206433
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():

    from ansible.template import Templar
    from ansible.template.safe_eval import SafeEval

    j2_vars = AnsibleJ2Vars(
        templar=Templar(loader=None, variables={'a': 'b'}, shared_loader_obj=None, environment=None, fail_on_undefined=True),
        globals={'a': 'b'},
        locals={'c': 'd'})

    iter_result = set()
    for item in j2_vars:
        iter_result.add(item)

    assert iter_result == set(['a'])


# Generated at 2022-06-13 15:48:27.298715
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import os
    import sys
    import unittest
    import ansible.template.safe_eval as safe_eval
    import ansible.template.templar as templar
    from ansible.template.templar import Templar

    class AnsibleJ2VarsTest(unittest.TestCase):
        def setUp(self):
            self.templar = Templar(loader=None, variables={})

        def test__getitem__(self):
            globals = {
            }
            locals = {
            }
            j2vars = AnsibleJ2Vars(self.templar, globals, locals=locals)
            # the original version of __getitem__ just raises KeyError
            self.assertRaises(KeyError, j2vars.__getitem__, 'foo')
            # self.