

# Generated at 2022-06-13 15:38:46.597116
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
  from ansible.module_utils.common._collections_compat import Mapping
  from ansible.module_utils.six import PY2

  # initialize
  ans_j2vars = AnsibleJ2Vars(None, globals(), locals())
  assert isinstance(ans_j2vars, Mapping), "type(ans_j2vars) is '%s', expected '%s'" % (type(ans_j2vars), Mapping)

  # check globals
  assert 'sys' in ans_j2vars, "sys in ans_j2vars is False"
  assert 'ansible_check_mode' in ans_j2vars, "ansible_check_mode in ans_j2vars is False"

  # check locals
  assert 'ans_j2vars' in ans_j

# Generated at 2022-06-13 15:38:51.889002
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    from ansible.utils.vars import combine_vars

    templar = Templar(loader=None)
    templar._available_variables = dict(var1="value1", var2="value2")
    locals = dict(l_var1="value1", l_var2="value2")

    # Test for existence of known variables
    variables = AnsibleJ2Vars(templar, dict(), locals=locals)
    for varname in ('var1', 'var2', 'l_var1', 'l_var2'):
        print("Checking for existence of variable %s" % varname)
        assert varname in variables

    # Test for existence of unknown variables
    with pytest.raises(KeyError):
        assert 'non_existent_var' in variables



# Generated at 2022-06-13 15:39:01.730209
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.vars.hostvars import HostVars
    from ansible.vars.hostvars import DEFAULT_HASH_BEHAVIOUR
    from ansible.template import Templar
    from ansible.utils.vars import combine_vars
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    vars = {'test_key1': 'test_value1', 'test_key2': 'test_value2'}

# Generated at 2022-06-13 15:39:13.918774
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.parsing.vault import VaultLib
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars

    vault_password = '123'
    vault = VaultLib(password=vault_password)
    templar = Templar(loader=None, shared_loader_obj=None, variables={}, vault_secrets=[vault])
    test = AnsibleJ2Vars(templar, globals={}, locals={'l_some_key': 123})
    result = test.__contains__('some_key')
    assert result == True, 'should be true'
    result = test.__contains__('NOT_THERE')
    assert result == False, 'should be false'
    result = test.__contains__('NOT_THERE')

# Generated at 2022-06-13 15:39:18.212495
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    templar = Templar(loader=loader, variables=variable_manager)

    varsObj = AnsibleJ2Vars(templar, None)

    assert False == ("test_var" in varsObj)
    assert True  == ("test_var" in varsObj)
    assert False == ("test_var" in varsObj)



# Generated at 2022-06-13 15:39:24.171780
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    templar = Templar()
    globals = dict({'foo': 'bar'})
    locals = dict({'ansible_foo': 'bar'})
    var = AnsibleJ2Vars(templar, globals, locals)
    assert 'foo' in var
    assert 'ansible_foo' in var
    assert var['foo'] == 'bar'
    assert var['ansible_foo'] == 'bar'

# Generated at 2022-06-13 15:39:30.869081
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    # Assert that the method __getitem__ raises KeyError
    # if the given variable has not been found in the
    # dictionaries
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    vars_ = {'vars_test': 'test'}
    var_proxy = AnsibleJ2Vars(Templar(), vars_)
    try:
        var_proxy['variable_does_not_exist']
    except KeyError:
        pass
    else:
        assert False

    # Assert that the method __getitem__ raises KeyError
    # if the given variable has not been found in the
    # available variables dictionary
    vars_ = {'variable_does_not_exist': 'test'}

# Generated at 2022-06-13 15:39:38.814406
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    print("\nTESTING AnsibleJ2Vars::__getitem__\n{}".format("-" * 80))
    import ansible.template.safe_eval
    import ansible.template.templar
    import jinja2.utils
    print("\nTesting for variable 'vars'")
    d = {'vars': 'myvalue'}
    globals = dict()
    j2vars = AnsibleJ2Vars(ansible.template.templar.Templar(loader=None), globals, locals=d)
    assert 'vars' in j2vars
    assert j2vars['vars'] == d['vars']
    print("\nTesting for variable 'missing'")

# Generated at 2022-06-13 15:39:45.589868
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import ansible.template
    templar = ansible.template.AnsibleLegacyJ2Vars()
    vars = AnsibleJ2Vars(templar, globals, locals)
    vars.__getitem__('dict')
    vars.__getitem__('dict_sub')
    vars.__getitem__('dict_sub2')
    vars.__getitem__('int')
    vars.__getitem__('string')
    vars.__getitem__('string_int')
    vars.__getitem__('string_int_sub')
    vars.__getitem__('string_sub')
    vars.__getitem__('string_sub2')

# Generated at 2022-06-13 15:39:54.525912
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.template import Templar
    globals = {'var1': 1, 'var2': 2, 'var3': 3}
    locals = {'var1': 10, 'var2': 20, 'var3': 30}
    templar = Templar()
    assert(isinstance(templar, Templar))

    ansible_j2_vars = AnsibleJ2Vars(templar, globals, locals)
    assert(isinstance(ansible_j2_vars, Mapping))


# Generated at 2022-06-13 15:40:07.074274
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    '''
    Testing the __contains__ method of AnsibleJ2Vars class
    '''
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    templar = Templar()
    # Variable foo (without starting underscore) is available in jinja2
    templar.available_variables['foo'] = AnsibleUnsafeText('foo_value')
    # Variable _bar (with starting underscore) is available in jinja2
    templar.available_variables['_bar'] = AnsibleUnsafeText('_bar_value')
    # Variable l_baz (prefixed with l_) is available in jinja2
    templar.available_variables['l_baz']

# Generated at 2022-06-13 15:40:09.995680
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.template import Templar

    j2vars = AnsibleJ2Vars(Templar(), {'var_foo': 'var_foo', 'var_bar': 'var_bar'})
    assert len(j2vars) == 2


# Generated at 2022-06-13 15:40:22.073447
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.parsing.vault import VaultLib
    from ansible.template import Templar
    my_vault_secret = 'my_vault_secret'
    vault_password_file = './test_vault.txt'
    vault = VaultLib(password_file=vault_password_file, template_dir=None, loader=None)
    my_vars = {'my_var': 'my_value'}
    j2_vars = AnsibleJ2Vars(Templar(vault=vault, variables=my_vars), {}, locals=my_vars)
    nb_vars = len(my_vars) * 2 + 1
    assert nb_vars == len(j2_vars)
    assert my_vars == dict(j2_vars)
   

# Generated at 2022-06-13 15:40:29.254423
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    try:
        env = Environment()
    except Exception as e:
        #print "env error", e
        pass

    templar = Templar(loader=DictLoader({
        'tags_include.j2': '{% for item in [0, 1, 2, 3, 4] %}'
                           '{% if item|int > 2 %}'
                           '{{ item }} '
                           '{% endif %}'
                           '{% endfor %}'
    }), variables={'item': 'ABC', 'not_a_var': 'Bar'})

    globals = {'item': 'ABC', 'not_a_var': 'Bar'}
    locals = {'item': 'ABC', 'not_a_var': 'Bar'}

# Generated at 2022-06-13 15:40:37.180073
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    from ansible.template.template import Templar
    templar = Templar()
    globals = dict(g1='global1', g2='global2')
    locals = dict(l1=1, l2=2)
    vars = AnsibleJ2Vars(templar, globals, locals)

    assert len(vars) == 4
    keys = set(vars)
    assert isinstance(keys, set)
    assert len(keys) == 4
    assert 'l1' in keys
    assert 'l2' in keys
    assert 'g1' in keys
    assert 'g2' in keys

# Generated at 2022-06-13 15:40:47.090119
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inv_manager = InventoryManager(loader=loader, sources=['localhost,',])
    variable_manager = VariableManager(loader=loader, inventory=inv_manager)

    cur_dir = os.path.dirname(os.path.abspath(__file__))
    variable_manager.set_inventory(inv_manager)


    variable_manager.extra_vars = {'hehe': 'haha', 'ansible_nodename': 'ha'}

    templar = Templar(loader=loader, variable_manager=variable_manager,
                        fail_on_undefined=True)

   

# Generated at 2022-06-13 15:40:53.274024
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    try:
        import json
    except ImportError:
        try:
            import simplejson as json
        except ImportError:
            print("Unable to import json or simplejson.  Skipping test.")
            return

    templar = Templar(loader=DictDataLoader({}), variables={}, shared_loader_obj=None)
    globals = {}
    v = AnsibleJ2Vars(templar, globals)
    v._templar.set_available_variables({'var1': 'var1value'})
    v._templar.set_available_variables({'var2': 'var2value'})
    v._templar.set_available_variables({'var3': 'var3value'})
    assert v['var1'] == 'var1value'

# Generated at 2022-06-13 15:41:03.080961
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    '''
    Test the __getitem__ function of the AnsibleJ2Vars class
    '''
    from ansible.template import Templar
    templar = Templar()
    o = AnsibleJ2Vars(templar, {'test_var': 'global'})
    assert o['test_var'] == 'global'
    o = AnsibleJ2Vars(templar, {}, locals={'test_var': 'local'})
    assert o['test_var'] == 'local'
    o = AnsibleJ2Vars(templar, {'test_var': 'global'}, locals={'test_var': 'local'})
    assert o['test_var'] == 'local'

# Generated at 2022-06-13 15:41:10.704175
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    # Create an empty container for variables.
    # It is not possible to create an empty dict because __contains__
    # requires the 'vars' member.  The 'vars' member must be a dict
    # containing a valid entry.  The 'foo' entry is used to create
    # a valid dict.  The 'foo' entry will be deleted such that the dict
    # appears to be empty.
    vars_dict = dict();
    vars_dict['foo'] = 42

    # Create a Templar() object
    templar = Templar(loader=None, variables=vars_dict, shared_loader_obj=None)

    # Create a dict containing "globals"
    globals_dict = dict()
    globals_dict['bar'] = 'baz'

    # Create a dict containing "locals"
    locals_

# Generated at 2022-06-13 15:41:14.999225
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    # Equal test
    templar = Templar(loader=None)
    globals = dict()
    locals = dict()
    result = AnsibleJ2Vars(templar, globals, locals).__contains__('ansible_check_mode')
    assert result == False

# Generated at 2022-06-13 15:41:27.499582
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.set_inventory(loader.load_inventory(host_list=[], group_list=[]))
    templar = Templar(loader=loader, variables=variable_manager)

    # Test if the exception is caught correctly
    test_variables = dict(a=1, b="{{c}}", d=[1,2], e=dict(f="{{g}}", h=[1,2]))
    test_globals = dict(c=2, g=3)
    test_locals = dict()

# Generated at 2022-06-13 15:41:38.354185
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.templating.jinja2.environment import Environment, get_template_class
    from jinja2.exceptions import UndefinedError

    ansible_vars = AnsibleJ2Vars(Environment().from_string(template="", globals=dict()), dict())

    assert ansible_vars["missing_key"] == KeyError

    ansible_vars._locals = dict(a=1)
    assert ansible_vars["a"] == 1
    assert ansible_vars["missing_key"] == KeyError


# Generated at 2022-06-13 15:41:46.870376
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.vars.hostvars import HostVars
    from ansible.template import Templar
    templar = Templar(loader=None)
    globals = {'foo': 'bar'}
    locals = {'baz': 'qux'}
    variables = AnsibleJ2Vars(templar, globals, locals)
    assert len(variables) == 3
    assert len(variables) == 3
    templar.available_variables = {'boolean': True}
    variables = AnsibleJ2Vars(templar, globals, locals)
    assert len(variables) == 4
    assert len(variables) == 4
    templar.available_variables = {'array': [1]}
    variables = AnsibleJ2Vars(templar, globals, locals)

# Generated at 2022-06-13 15:41:49.101603
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    pass


# Generated at 2022-06-13 15:41:54.009006
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    '''
    Test method AnsibleJ2Vars.__iter__
    '''
    from ansible.template import Templar
    aj2v = AnsibleJ2Vars(Templar(), dict())
    assert isinstance(aj2v.__iter__(), iter)


# Generated at 2022-06-13 15:42:01.258435
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    from ansible.playbook.play_context import PlayContext
    templar = Templar(loader=None, variables={'VAR': 'value'})
    global_vars = {}
    ans_j2_vars = AnsibleJ2Vars(templar, global_vars)

    assert "VAR" in ans_j2_vars
    assert "var" not in ans_j2_vars  # var should not exist, it should fail to match
    assert "A" not in ans_j2_vars

# Generated at 2022-06-13 15:42:11.496157
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    from ansible.vars import VariableManager

    templar = Templar(loader=None, variables=VariableManager())

    J2Vars = AnsibleJ2Vars(templar, { "globalvar": "globalvar_value" })

    J2Vars.add_locals({ "localvar": "localvar_value" })
    assert J2Vars["localvar"] == "localvar_value"

    J2Vars.add_locals({ "globalvar": "localglobalvar_value" })
    assert J2Vars["globalvar"] == "localglobalvar_value"

    hostvars = HostVars(loader=None, variables=VariableManager())

# Generated at 2022-06-13 15:42:22.845960
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    templar = Templar(
        loader=DataLoader(),
        variables=VariableManager(loader=DataLoader(), inventory=InventoryManager())
    )
    test_instance = AnsibleJ2Vars(templar, globals=dict())

    # test with undefined variable

# Generated at 2022-06-13 15:42:33.161074
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    templar = Templar(loader=None)
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    from ansible.vars.special import SpecialVars

    # Sample variables for testing
    vars = dict(
        a="val a",
        b=dict(
            c="val c",
            d=dict(
                e="val e",
                f="{{ x }}"
            ),
        ),
    )

    # Sample variables dict

# Generated at 2022-06-13 15:42:45.159161
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    templar = Templar()
    # Test variable in locals
    locals = {"l_var1": "value1"}
    globals = {"g_var1": "value2"}
    aj2v = AnsibleJ2Vars(templar, globals, locals)
    assert aj2v["var1"] == "value1"
    # Test variable in available variables
    available_variables = {"var2": "value2"}
    templar.available_variables = available_variables
    assert aj2v["var2"] == "value2"
    # Test variable in globals
    assert aj2v["var3"] == "value2"
    # Test undefined variable

# Generated at 2022-06-13 15:42:58.102946
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    # ansible 2.5 use _text instead of to_text
    try:
        from ansible.module_utils._text import to_text
    except:
        from ansible.module_utils.six import text_type as to_text

    from ansible.template import Templar
    from ansible_collections.ansible.community.tests.unit.compat.mock import MagicMock
    from ansible_collections.ansible.community.tests.unit.compat.mock import patch

    from ansible_collections.ansible.community.plugins.module_utils.gcp import gcp_connect
    from ansible_collections.ansible.community.tests.unit.compat.mock import Mock

    # FIXME: fix this for use with jinja2 > 2.9.0


# Generated at 2022-06-13 15:43:03.022797
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    templar = object()
    globals = {'gg': 'gg'}
    locals = {'ll': 'll'}
    vars = AnsibleJ2Vars(templar, globals, locals=locals)

    assert 'll' in vars
    assert 'gg' in vars
    assert 'uu' not in vars

# Generated at 2022-06-13 15:43:12.048391
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.vars.hostvars import HostVars
    from ansible.template import Templar
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from copy import copy

    def _get_templar(available_variables):
        play_context = PlayContext()
        play_context.prompt = dict()
        play_context.prompt.prompt = (lambda x, y, z, a: 'test_AnsibleJ2Vars___getitem__')
        play_context.update_vars(dict(a=1, b=2))

# Generated at 2022-06-13 15:43:21.878526
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    locals = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    globals = {'a': 1, 'b': 2, 'z': 26, 'w': 23}
    templar = Templar()
    proxy = AnsibleJ2Vars(templar, globals, locals)

    assert 'a' in proxy
    assert 'z' in proxy
    assert 'zz' not in proxy
    assert {'a', 'b', 'c', 'd', 'z', 'w'} == set(proxy)


# Generated at 2022-06-13 15:43:30.812735
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    class _AnsibleJ2Vars_templar:
        def __init__(self, available_variables, template):
            self.available_variables = available_variables
            self.template = template

        def __contains__(self, key):
            return self.available_variables.__contains__(key)

        def __getitem__(self, item):
            return self.available_variables[item]

    def _AnsibleJ2Vars_template(self, data):
        return data

    import unittest

    class AnsibleJ2Vars_test(unittest.TestCase):
        def setUp(self):
            self.globals = {"globals_key": "globals"}
            self.locals = {"locals_key": "locals"}
            self

# Generated at 2022-06-13 15:43:42.102101
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.vars.hostvars import HostVars
    assert AnsibleJ2Vars('templar', {'a': 1}, locals={'b': 2}).__contains__('a') is True
    assert AnsibleJ2Vars('templar', {'a': 1}, locals={'b': 2}).__contains__('b') is True
    assert AnsibleJ2Vars('templar', {'a': 1}, locals={'b': 2}).__contains__('c') is False
    assert AnsibleJ2Vars('templar', {'a': 1}, locals={'b': 2, 'c': HostVars()}).__contains__('c') is True

    # test for bug #27602

# Generated at 2022-06-13 15:43:44.683981
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    templar = Templar(loader, variables=dict())
    vars = AnsibleJ2Vars(templar, dict())
    assert vars['vars'] is not None

# Generated at 2022-06-13 15:43:54.361529
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.callback import CallbackBase

    # create the callback
    class ResultsCollector(CallbackBase):
        def v2_runner_on_ok(self, result):
            pass

    # create play with tasks to run

# Generated at 2022-06-13 15:44:04.765418
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    templar = Templar(loader=None, variables={})
    assert 'test' not in AnsibleJ2Vars(templar, globals={})
    assert 'test' not in AnsibleJ2Vars(templar, globals={}, locals={'test': 'foo'})
    assert 'test' in AnsibleJ2Vars(templar, globals={'test': 'foo'})
    assert 'test' not in AnsibleJ2Vars(templar, globals={'test': 'foo'}, locals={'test': 'bar'})
    assert 'test' in AnsibleJ2Vars(templar, globals={'test': 'foo'}, locals={'l_test': 'bar'})


# Generated at 2022-06-13 15:44:12.667232
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from jinja2 import Environment, StrictUndefined, Undefined
    from jinja2.environment import TemplateModule
    from jinja2.sandbox import SandboxedEnvironment
    from jinja2.runtime import Context, LazyObject, UndefinedContext
    import unittest
    import mock

    class AnsibleJ2VarsTest(unittest.TestCase):
    
        def setUp(self):
            self.mock_templar = mock.MagicMock()
            self.mock_globals = mock.MagicMock()
            self.mock_locals = mock.MagicMock()
            self.mock_undefined = mock.MagicMock()
            self.mock_context = mock.MagicMock()
            self.mock_hostvars = mock.MagicMock()


# Generated at 2022-06-13 15:44:25.549838
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    templar = None
    globals = { 'g_foo': 'global foo', 'g_bar': 'global bar' }
    locals = { 'l_foo': 'local foo', 'l_bar': 'local bar' }
    j2vars = AnsibleJ2Vars(templar, globals, locals=locals)

    # Check the number of items
    count = -1
    for _ in j2vars:
        count += 1
    assert count == len(j2vars)


# Generated at 2022-06-13 15:44:32.929715
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    templar = jinja2.Environment()
    j2v = AnsibleJ2Vars(templar, globals = {})
    j2v_obj = AnsibleJ2Vars(templar, globals = {"hostvars": {}}, locals = {"hostvars": {}})
    assert j2v_obj.__contains__('hostvars') == True
    assert j2v.__contains__('hostvars') == False


# Generated at 2022-06-13 15:44:42.156805
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    # __contains__() should return True if the provided varname can be found in the class
    # The tested class has two dictionaries: _templar and _locals
    # This test queries the _templar dictionary

    # Create a fake available_variables dict
    templar = {}
    templar['available_variables'] = {}
    templar['available_variables']['test_var'] = 'test_value'

    # Test arguments:
    # locals = {}
    # globals = {}
    test_obj = AnsibleJ2Vars(templar, {}, {})

    assert('test_var' in test_obj)


# Generated at 2022-06-13 15:44:51.336681
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar

    import json
    def test_data(key, value):
        _templar = Templar(loader=None)
        _templar.available_variables = {key: value}
        ajvars = AnsibleJ2Vars(_templar, globals={}, locals=None)
        return ajvars[key]

    assert test_data('str_var', 'string') == 'string'
    assert test_data('int_var', 1) == 1
    assert test_data('float_var', 1.11) == 1.11
    assert test_data('bool_var', True) == True
    assert test_data('bool_var', False) == False

    # all list, tuple, and dict should be returned as list

# Generated at 2022-06-13 15:44:59.373286
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    class AnsibleJ2VarsTest:

        def __init__(self, templar, globals, locals=None):
            self._templar = templar
            self._globals = globals
            self._locals = locals

        def __contains__(self, k):
            return True if k in self._locals or k in globals or k in self._templar.available_variables else False

    templar = None
    locals = {'a':1}
    globals = {'b':2}
    ansible_j2_vars = AnsibleJ2VarsTest(templar, globals, locals)
    assert 'a' in ansible_j2_vars
    assert 'c' in ansible_j2_vars


# Generated at 2022-06-13 15:45:00.856865
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    # TODO: test for multiple conditions for each variable
    assert False

# Generated at 2022-06-13 15:45:05.281048
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from ansible.template.template import Templar
    mock_templar = Templar(loader=None)
    mock_globals = {}
    mock_locals = {}
    test_object = AnsibleJ2Vars(mock_templar, mock_globals, mock_locals)
    assert test_object.__len__() == 0

# Generated at 2022-06-13 15:45:17.388653
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    #Act
    from ansible.vars.hostvars import HostVars
    from ansible.vars import VariableManager
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    import ansible.constants as C
    import os

    variable_manager = VariableManager()
    loader = C.DEFAULT_LOADER
    variable_manager.extra_vars = {"my_var": "my_value"}
    inventory = HostVars(loader=loader, variable_manager=variable_manager)
    play_context = PlayContext()

    templar = Templar(loader=loader, variables=variable_manager,
                      shared_loader_obj=loader, inventory=inventory,
                      play_context=play_context)

# Generated at 2022-06-13 15:45:21.754069
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template.safe_eval import safe_eval
    from ansible.template.templar import Templar
    from ansible.vars.hostvars import HostVars

    templar = Templar(loader=None)
    globals = {'from_globals': 123}
    locals = {'from_locals': 456}
    vars = {'from_vars': 789}

    # Test that locals and globals have the expected values
    obj = AnsibleJ2Vars(templar, globals, locals)
    assert(obj['from_globals'] == 123)
    assert(obj['from_locals'] == 456)

    # Test that we can access variables via templar
    templar.available_variables = vars

# Generated at 2022-06-13 15:45:33.729139
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    fake_vars = HostVars()

    def set_available_variables(self, variables):
        self.available_variables = variables

    Templar.set_available_variables = set_available_variables

    templar = Templar()
    templar.set_available_variables({"banana":1, "apple":fake_vars})
    globals = {"sugar":2}

    j2var = AnsibleJ2Vars(templar, globals)

    assert "banana" in j2var
    assert "apple" in j2var
    assert "sugar" in j2var
    assert "carrot" not in j2var



# Generated at 2022-06-13 15:45:51.662608
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import sys
    import unittest
    import jinja2

    class foobar(object):
        pass

    class TestClass(unittest.TestCase):
        def setUp(self):
            from ansible.template import Templar

            self.mock_templar = Templar(loader=None)
            self.mock_templar.available_variables = dict()

            self.mock_globals = dict()
            self.mock_locals = dict()

            self.ansible_j2_vars = AnsibleJ2Vars(self.mock_templar, self.mock_globals, locals=self.mock_locals)

        def test_returns_dict_if_variable_is_dict_and_name_is_vars(self):
            mock_v

# Generated at 2022-06-13 15:45:59.516796
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    templar = object()
    globals = { 'a': '1', 'c': 'A', 'd': 'B'}
    locals = { 'b': '2', 'c': 'B', 'e': 'C'}
    aj2v = AnsibleJ2Vars(templar, globals, locals)
    keys = list(aj2v.__iter__())
    assert(keys == ['a', 'b', 'c', 'd', 'e'])

# Generated at 2022-06-13 15:46:06.893233
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    from ansible.vars import VariableManager

    v = VariableManager()
    v.extra_vars = {"test_dict": {"test_key": "test_value"}}
    v.host_vars = {"my_var": "my_value"}
    templar = Templar(loader=None, variables=v)

    j2globals = {"globals_var": "globals_value"}
    j2locals = {"locals_var": "locals_value"}

    variables = AnsibleJ2Vars(templar, j2globals, locals=j2locals)
    assert "my_var" in variables
    assert "globals_var" in variables
    assert "locals_var" in variables
    assert "test_dict" in variables


# Generated at 2022-06-13 15:46:14.545139
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    globals = {'g_a': 'g_a_value'}
    locals = {'l_a': 'l_a_value'}
    vars = {'available_variables': {'v_a': 'v_a_value'}}
    ansible_j2_vars = AnsibleJ2Vars(vars, globals, locals)

    # len should return the total number of variables,
    # both global, local and available ones.
    assert len(ansible_j2_vars) == 3

# Generated at 2022-06-13 15:46:23.158012
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.template import Templar
    import os

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    template_dir = os.path.join(os.path.dirname(__file__), '../templates')
    j2_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))

    assert AnsibleJ2Vars(Templar(loader, j2_env, variable_manager), {})['my_var'] is None

# Generated at 2022-06-13 15:46:33.863971
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    # create a simple AnsibleJ2Vars object:
    #    - a templar object
    #    - a globals dict
    #    - a locals dict
    # the dicts are empty so that the test is simple
    templar = 'my templar mock'
    globals_dict = dict()
    locals_dict = dict()
    ansibleJ2Vars = AnsibleJ2Vars(templar, globals_dict, locals_dict)

    # try to get a key that is in the 'locals' dict
    key = 'my_locals_key'
    locals_dict[key] = 'my locals value'
    contains = ansibleJ2Vars.__contains__(key)
    assert contains

    # try to get a key that is in the 'available_variables' dict
   

# Generated at 2022-06-13 15:46:38.380183
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import ansible
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    # init a DataLoader obj
    loader = DataLoader()
    # init a Templar obj
    templar = Templar(loader=loader, variables={
        'hostvars':{'host-1':{'ip':'10.0.0.1','port':80}},
        'inventory_hostname':'host-1',
        'inventory_hostname_short':'host-1',
        'group_names' : ['group-a','group-b'],
        'groups' : {'group-a': {'hosts': ['host-1']}, 'group-b': {'hosts': ['host-1']}}
    })

    # init a mapping var like as AnsibleJ2V

# Generated at 2022-06-13 15:46:43.544189
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.template import Templar

    v = AnsibleJ2Vars(Templar(loader=None, variables=dict(a=1, b=2, c=3)), globals=dict(d=4, e=5))
    assert(len(v) == 5)


# Generated at 2022-06-13 15:46:45.283343
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import AnsibleJ2Vars
    run_AnsibleJ2Vars__getitem___unit_test()


# Generated at 2022-06-13 15:46:51.657866
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import UnsafeProxy

    templar = Templar(loader=None)
    templar.available_variables.update({'foo': 'bar'})

    value = 'bar'
    variable = UnsafeProxy(value)
    templar.available_variables.update({'unsafe_proxy': variable})

    hostvars = HostVars(hostname='foo')
    templar.available_variables.update({'hostvars': hostvars})

    j2vars = AnsibleJ2Vars(templar, {})

    assert j2vars['foo'] == 'bar'
    assert j2vars['unsafe_proxy'] == 'bar'

# Generated at 2022-06-13 15:47:08.420999
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():

    templar = ""
    globals = {'g1': 1}
    locals = {'l1': 1, 'l2': 2, 'a': 1, 'g2': 2}

    vars = AnsibleJ2Vars(templar, globals, locals)
    for v in locals:
        assert v in vars
        try:
            assert locals[v] == vars[v]
        except KeyError:
            raise
    for v in globals:
        assert v in vars
        try:
            assert globals[v] == vars[v]
        except KeyError:
            raise
    for v in ('l1', 'l2', 'g1', 'g2'):
        assert v in vars
    for v in ('l3', 'g3'):
        assert v not in v

# Generated at 2022-06-13 15:47:14.221339
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    from ansible.template import Templar
    j2 = Templar(loader=None)
    globals = {'a': 1, 'b': 2}
    locals = {'c': 3, 'd': 4}
    ansible_j2_vars = AnsibleJ2Vars(j2, globals, locals=locals)
    result = set()
    for x in ansible_j2_vars:
        result.add(x)
    assert set(result) == set(['a', 'b', 'c', 'd']), "all expected keys should have been visited"


# Generated at 2022-06-13 15:47:24.677412
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.compat.tests.mock import patch
    from ansible.template import Templar

    templar = Templar(loader=None)
    templar._available_variables = {'foo': 'bar'}

    with patch.dict(templar._available_variables, {'foo': 'bar'}, clear=True):
        proxy = AnsibleJ2Vars(templar, {'baz': 'qux'})
        assert 'foo' in proxy
        assert 'bar' not in proxy
        assert 'baz' in proxy

    with patch.dict(templar._available_variables, {'foo': 'bar'}, clear=True):
        proxy = AnsibleJ2Vars(templar, {'baz': 'qux'}, {'dummy': 'dummy'})

# Generated at 2022-06-13 15:47:29.749240
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    """
    AnsibleJ2Vars: Testing method __getitem__
    """
    import jinja2
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    ##########
    # case 1 #
    ##########
    # input
    # declare args for a constructor of AnsibleJ2Vars
    templar = jinja2.Environment()
    globals = {}
    locals = {}
    locals['l_test1'] = AnsibleUnsafeText(u'test1')
    locals['l_test2'] = AnsibleUnsafeText(u'test2')
    locals['l_test3'] = AnsibleUnsafeText(u'test3')
    # declare a variable for __getitem__
    varname = 'l_test2'
    # expected
    expected = u

# Generated at 2022-06-13 15:47:36.555574
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar

    variable_manager = VariableManager()
    variable_manager.set_globals({'foo': 'global foo', 'fiz': 'global fiz'})
    variable_manager.set_host_variable(host='127.0.0.1', varname='foo', value='host foo')
    variable_manager.set_host_variable(host='127.0.0.1', varname='bar', value='host bar')

    templar = Templar(loader=None, variables=variable_manager)
    global_vars = templar.available_variables

    proxy = AnsibleJ2Vars(templar, global_vars, locals={'baz': 'local baz'})

    assert 'foo' in proxy

# Generated at 2022-06-13 15:47:43.516792
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar

    class MockedTemplar():
        def __init__(self, available_variables):
            self.available_variables = available_variables
        def template(self, variable):
            return "test_templar.template"

    globals_ = {"var1": "var1_value", "var2": "var2_value"}
    locals_ = {"var3": "var3_value", "var4": "var4_value"}
    available_variables = {"var5": "var5_value"}

    mocked_templar = MockedTemplar(available_variables)
    instance = AnsibleJ2Vars(mocked_templar, globals_, locals_)

    # test get from locals
    assert instance["var3"] == "var3_value"

# Generated at 2022-06-13 15:47:53.812653
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    # set up
    templar = None
    globals = dict()
    locals = dict()
    testObj = AnsibleJ2Vars(templar, globals, locals=locals)
    testObj._templar.available_variables = dict()
    testObj._templar.available_variables['varname1'] = 'value1'
    testObj._templar.available_variables['varname2'] = 'value2'
    testObj._templar.available_variables['varname3'] = 'value3'
    testObj._globals['globals1'] = 'value1'
    testObj._globals['globals2'] = 'value2'
    testObj._globals['globals3'] = 'value3'
    testObj._loc

# Generated at 2022-06-13 15:48:03.207981
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    templar = object()
    globals = {'key1': 'val1'}
    locals = {'key2': 'val2'}
    j2_vars = AnsibleJ2Vars(templar, globals, locals)
    assert templar == j2_vars._templar
    assert globals == j2_vars._globals
    assert locals == j2_vars._locals
    assert 'key1' in j2_vars
    assert 'key2' in j2_vars
    assert j2_vars['key1'] == 'val1'
    assert j2_vars['key2'] == 'val2'

# Generated at 2022-06-13 15:48:15.379485
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.template import Templar

    # Create required objects
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list=[])
    templar = Templar(loader=loader, variables=variable_manager.get_vars(play=None, include_hostvars=True))

    # initialize vars
    locals = dict()
    globals_ = dict()

    # test with empty vars
    j2vars = AnsibleJ2Vars(templar, globals_, locals)
    assert len(j2vars) == 0
    assert list(j2vars)

# Generated at 2022-06-13 15:48:16.609395
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    # TODO: test me!
    pass
