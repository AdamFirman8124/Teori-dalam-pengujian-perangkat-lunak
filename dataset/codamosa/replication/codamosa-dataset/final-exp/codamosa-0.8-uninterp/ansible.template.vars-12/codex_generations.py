

# Generated at 2022-06-13 15:38:46.549261
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    import os

    context = {'type': 'unsafe', 'role': 'test'}
    templar = Templar(loader=None, variables=VariableManager(), shared_loader_obj=None)
    ansible_vars = AnsibleJ2Vars(templar, {'ansible_version': {'full': '2.1.1.0'}})

    # Test with success case
    assert "ansible_version" in ansible_vars

    ansible_vars = AnsibleJ2Vars(templar, globals={'ansible_version': {'full': '2.1.1.0'}})
    ansible_vars._

# Generated at 2022-06-13 15:38:50.346505
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    j2vars = AnsibleJ2Vars(None, {'a': 1, 'b': 2}, {'c': 3})

    assert('a' in j2vars)
    assert('b' in j2vars)
    assert('c' in j2vars)
    assert('d' not in j2vars)


# Generated at 2022-06-13 15:39:00.760355
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    # The function is tested as part of the test for class AnsibleJ2Vars

    from ansible.parsing.vault import VaultLib
    from ansible.template import Templar

    templar = Templar(None, vault_password='test')
    # Add variables to the variable manager for testing
    templar._available_variables = {
        'a': 'A',
        'aa': 'AA',
        'b': 'B',
        'c': 'C',
    }

    # Test with empty globals, locals
    ansible_j2_vars = AnsibleJ2Vars(templar, {}, {})
    assert ansible_j2_vars.__contains__('a') == True
    assert ansible_j2_vars.__contains__('aa') == True
    assert ans

# Generated at 2022-06-13 15:39:02.207965
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    t = AnsibleJ2Vars("empty")
    assert 'empty' in t


# Generated at 2022-06-13 15:39:06.867717
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.parsing.vault import VaultLib
    templar = Templar(vars={'a': 1}, vault_password='secret')
    ansible_vars = AnsibleJ2Vars(templar, {'b': 2}, locals={'c': 3})
    assert ('a' in ansible_vars) == True
    assert ('b' in ansible_vars) == True
    assert ('c' in ansible_vars) == True
    assert ('d' in ansible_vars) == False

test_AnsibleJ2Vars___contains__()


# Generated at 2022-06-13 15:39:18.303341
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.errors import AnsibleUndefinedVariable
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    import tempfile
    import os

    # data for test
    vars_data = {'name': 'ansible', 'version': '1.9.3'}
    globals_data = {'keys': ['name', 'version']}

    # initialize test vars
    templar = Templar(loader=DataLoader(), variables=vars_data)
    vars = AnsibleJ2Vars(templar, globals=globals_data)

    # test __getitem__ with valid dict key

# Generated at 2022-06-13 15:39:27.710350
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    globals = {
        'g_foo': 'g_foo_value',
        'g_': 'g__value'
    }
    locals = {
        'l_foo': 'l_foo_value',
        'l_': 'l__value'
    }
    templar = {
        't_foo': 't_foo_value',
        't_': 't__value',
    }

    ajv = AnsibleJ2Vars(templar, globals, locals)

    assert 'g_foo' in ajv
    assert 'g_' in ajv
    assert 'l_foo' in ajv
    assert 'l_' in ajv
    assert 't_foo' in ajv
    assert 't_' in ajv

# Generated at 2022-06-13 15:39:39.303732
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    t = Templar(loader=None)
    x = AnsibleJ2Vars(t, {'a': 'a', 'b': 'b'}, {'c': 'c', 'd': 'd'})
    y = x.__iter__()
    assert isinstance(y, type(iter([])))
    assert set(y) == set(['a', 'b', 'c', 'd'])
    assert len(x) == 4
    assert 'a' in x
    assert 'b' in x
    assert 'c' in x
    assert 'd' in x
    assert x['a'] == 'a'
    assert x['b'] == 'b'
    assert x['c'] == 'c'

# Generated at 2022-06-13 15:39:50.157283
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager(loader=loader)
    templar = Templar(loader=loader, variables=variable_manager)
    v = AnsibleJ2Vars(templar, globals={}, locals={})

    assert 'foo' not in v

    assert 'bar' not in v
    templar.available_variables = {'bar': AnsibleUnsafeText(u'foobaz')}
    assert 'bar' in v

    assert 'baz' not in v
   

# Generated at 2022-06-13 15:39:58.920354
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import ansible.template
    import contextlib
    import jinja2
    import os
    import sys

    def mkdtemp():
        return tempfile.mkdtemp(prefix='ansible-j2vars-test-')

    @contextlib.contextmanager
    def chdir(new_dir):
        old_dir = os.getcwd()
        os.chdir(new_dir)
        try:
            yield
        finally:
            os.chdir(old_dir)

    def writetmp(filename, contents):
        with open(filename, 'w') as f:
            f.write(contents)

    def readtmp(filename):
        with open(filename) as f:
            return f.read()


# Generated at 2022-06-13 15:40:06.271713
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar

    templar = Templar(loader=None, variables={'test': 'bar'})

    vars_proxy = AnsibleJ2Vars(templar, {'test': 'foo'})
    assert 'test' in vars_proxy
    assert 'missing' not in vars_proxy


# Generated at 2022-06-13 15:40:10.363936
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    import sys, os, inspect
    # realpath() will make your script run, even if you symlink it :)
    cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
    load_folder = cmd_folder + '/../lib/ansible'
    if load_folder not in sys.path:
        sys.path.insert(1, load_folder)

    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop
    from ansible.template import Templar

    loader = DictDataLoader({})
    templar = Templar(loader=loader, variables={})
    globals = {}


# Generated at 2022-06-13 15:40:10.911137
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    pass

# Generated at 2022-06-13 15:40:21.994291
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    '''
    Ensure variable names are properly resolved.

    :param Templar templar: Templar object for variable resolution.
    :param dict globals: Dict with global variables.
    :param dict locals: Dict with local variables.
    '''

    from ansible.template import Templar
    templar = Templar(loader=None, variables={'a': 'bar'})

    vars = AnsibleJ2Vars(templar, {'a': 'foo', 'b': 'bar'}, locals={'a': 'baz', 'b': 'test'})

    assert vars['a'] == 'baz'
    assert vars['b'] == 'test'
    assert vars['c'] == 'bar'

# Generated at 2022-06-13 15:40:26.570683
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    class _MockTemplar:
        def __init__(self):
            self.available_variables = {'key1':'value1', 'key2':'value2'}
        def template(self, variable):
            return 'templated_' + variable
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    globals = {'key3': 'value3',
               'key4': AnsibleUnsafeText('value4')}
    proxy = AnsibleJ2Vars(_MockTemplar(), globals)

    assert proxy['key1'] == 'templated_value1'
    assert proxy['key2'] == 'templated_value2'
    assert proxy['key3'] == 'value3'
    assert proxy['key4'] == 'value4'

# Generated at 2022-06-13 15:40:34.680231
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    class Templar:
        available_variables = {'test': 'test','test2': 'test2'}
    t = Templar()
    j2vars = AnsibleJ2Vars(t, globals={'test3': 'test3'}, locals={'test4': 'test4'})
    assert('test' in j2vars)
    assert('test2' in j2vars)
    assert('test3' in j2vars)
    assert('test4' in j2vars)
    assert('unknown' not in j2vars)


# Generated at 2022-06-13 15:40:42.771463
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    from ansible.template.safe_eval import safe_eval
    from ansible.template.safe_eval import AnsibleUndefinedError
    from ansible.template.safe_eval import AnsibleAssertionError
    from ansible.template.safe_eval import AnsibleError
    from ansible.template.safe_eval import AnsibleTimeoutError
    from ansible.template.safe_eval import AnsibleEvaluationError
    from ansible.template.safe_eval import AnsibleExpressionError


# Generated at 2022-06-13 15:40:49.397494
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    vars = VariableManager()
    templar = Templar(loader=None, shared_loader_obj=None, variables=vars)
    ansible_j2_vars = AnsibleJ2Vars(templar, {'version': 2})

    assert 'version' in ansible_j2_vars
    assert 'version' not in ansible_j2_vars._globals
    assert 'version' in ansible_j2_vars._templar.available_variables


# Generated at 2022-06-13 15:40:55.439748
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():

    # create test-object
    test_obj = AnsibleJ2Vars(None, None)

    # create empty dict
    test_dict = {}

    # loop over the test-object and check if the dict is filled correctly
    for var in test_obj:
        if var not in test_dict:
            test_dict[var] = True
        else:
            return False

    # return true if the dict is empty
    return len(test_dict) == 0

# Generated at 2022-06-13 15:41:05.465312
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.templating import Templar
    from ansible.template import Templar as Templar_
    from ansible.vars.hostvars import HostVars

    ####################################################################################################################
    # Unit test for line 407 ( when varname in self._locals == True )
    ####################################################################################################################

    # Set-up the test
    templar = Templar(variables={'var1': 'bar1'})
    globals = {'var2': 'bar2'}
    locals = {'l_var3': 'bar3'}
    j2_vars = AnsibleJ2Vars(templar, globals, locals=locals)

    # Test that getitem with a key that exist in locals
    assert j2_vars['l_var3'] == 'bar3'

    #################################################################################################

# Generated at 2022-06-13 15:41:20.879730
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.playbook.play_context import PlayContext
    from ansible.template.safe_eval import safe_eval

    from ansible.template.templar import Templar
    from ansible.template.vars import AnsibleVars

    from ansible.vars.manager import VariableManager

    play_context = PlayContext()
    templar = Templar(loader=None, variables=dict())
    ansible_vars = AnsibleVars(play_context, templar, loader=None)
    variable_manager = VariableManager(loader=None, inventory=None)
    variable_manager._extra_vars = dict()
    templar.set_available_variables(play_context, ansible_vars, variable_manager)

    j2vars = AnsibleJ2Vars(templar, dict())
   

# Generated at 2022-06-13 15:41:27.479126
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import pytest
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.plugins.vars import BaseVarsPlugin
    from ansible.inventory.host import Host
    from ansible.template.template import Templar
    from ansible.vars.manager import VariableManager

    # setup needed objects
    vault_secret = VaultSecret('secret')
    vault_lib = VaultLib(vault_secret)

    vars_plugin = BaseVarsPlugin()
    vars_plugin.get_vars(Host('localhost'), vault_secret)

    variable_manager = VariableManager(vars_plugin, vault_secret)
    variable_manager.set_host_variable(Host('localhost'), 'var', 1)

    # create object to be tested
    templar

# Generated at 2022-06-13 15:41:38.356150
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from ansible.template import Templar
    vars_ = {
        "outer": {
            "inner": 42
        }
    }
    locals_ = {
        "foo": "bar",
    }
    templar = Templar(vars_, loader=None)
    globals_ = {
        "os": {
            "sep": "/"
        }
    }
    aj2v = AnsibleJ2Vars(templar, globals_, locals_)

    assert aj2v['os']['sep'] == '/'
    assert aj2v['outer']['inner'] == 42
    assert aj2v['foo'] == 'bar'
    assert aj2v.add_locals({'x': 42})['x'] == 42

# Generated at 2022-06-13 15:41:42.414124
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    globals = [ 'abc' ]
    locals = { 'def': 'ghi' }

    templar = None
    j2_vars = AnsibleJ2Vars(templar, globals, locals)

    # testing the variant with the StringIO()
    output = StringIO()
    sys.stdout = output
    print(list(j2_vars))
    sys.stdout = sys.__stdout__

    assert(output.getvalue() == "['def', 'abc']\n")


# Generated at 2022-06-13 15:41:46.643511
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    # Create fake Templar() object to pass to AnsibleJ2Vars()
    class FakeTemplar(object):
        def __init__(self, available_variables):
            self.available_variables = available_variables
        def template(self, variable):
            return variable

    # Create available variables
    available_variables = {'vars':{'foo':'bar'}, 'hostvars':{'foo':'bar'}}

    # Create instance of AnsibleJ2Vars()
    ajv = AnsibleJ2Vars(FakeTemplar(available_variables), {})

    # Test cases, expect:
    # 1.1,1.2: "bar"
    # 1.3: KeyError, since variable is not in available variables
    # 2.1,2.2: "bar"
   

# Generated at 2022-06-13 15:41:59.109785
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    from ansible.template import Templar
    templar = Templar(None)
    globals = {'a': 1, 'b': 2, 'c': 3}
    locals = {'z': 26, 'y': 25, 'x': 24}
    # Initialize the AnsibleJ2Vars object
    j2vars = AnsibleJ2Vars(templar, globals, locals=locals)
    # Call method __iter__ of class AnsibleJ2Vars
    iter_j2vars = iter(j2vars)
    # The result of method __iter__ should be a iterator object
    assert isinstance(iter_j2vars, object)
    assert isinstance(iter_j2vars, iter)
    # The result of method __iter__ should be a iterable object
    assert '__next__'

# Generated at 2022-06-13 15:42:09.115501
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    # create a mock
    mock_templar = mock.MagicMock()
    # set return value for the mock
    mock_templar.template.return_value = 'my.host.example.com'
    # define a dict with vars
    var_dict = {'var1': {'a': 10}, 'var2': {'b': 20}}
    # create a dict with global vars
    gvar_dict = {'var1': 'foo', 'var2': 'bar'}
    # create the object with the mock
    ajv_obj = AnsibleJ2Vars(mock_templar, gvar_dict)
    # define a dict with local vars
    locals = {'var2': 'baz', 'var3': 'spam'}
    # create a local AnsibleJ2V

# Generated at 2022-06-13 15:42:14.937899
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.vars.hostvars import HostVars
    from ansible.vars import combine_vars
    from ansible.template import Templar

    inventory = {'host1': {'hostvars': {'foo': 'bar'}}, 'host2': {'hostvars': {'foo': 'baz'}}}
    templar = Templar(loader=None, variables=combine_vars(HostVars(inventory), {'foo': 'bam'}))
    v = AnsibleJ2Vars(templar, {})
    assert 'foo' in v

# Generated at 2022-06-13 15:42:21.226276
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from jinja2 import Environment, DictLoader
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    import pytest
    # initializing containers of variables that define the scope of available variables
    # in the order of increasing scope
    primary_vars = dict()
    facts = {}
    templar = Templar(Environment(loader=DictLoader(dict())), loader=DataLoader())
    vars = VariableManager(loader=DataLoader(), hosts=None, play=None)

    # jinja2-templated value that should be returned as-is

# Generated at 2022-06-13 15:42:32.167254
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from ansible.template.safe_eval import unsafe_eval

    initial_vars = dict(a=1,b="2")
    template_vars = dict(a=3)
    inventory_hostname="host1"

    # Construct a Templar object
    ansible_vars = dict(template_host=inventory_hostname)
    ansible_vars.update(initial_vars)
    templar = unsafe_eval.AnsibleTemplar(extra_vars=ansible_vars)
    templar.set_available_variables(template_vars)

    # The AnsibleJ2Vars object is constructed with a reference to the AnsibleTemplar object
    # and a reference to the template_vars dictionary
    vars = AnsibleJ2Vars(templar, dict())

   

# Generated at 2022-06-13 15:42:56.500511
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    def func(val):
        return val

    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    templar = Templar(loader=DataLoader(), variables={'dict_var': {'key': 'value'}, 'str_var': 'value', 'list_var': [' value1', 'value2 ', ' value3 '], 'int_var': 1, 'bool_var': True, 'func_var': func(True)})
    j2vars = AnsibleJ2Vars(templar, globals={'func_glob': func(True)})

    # dict_var
    assert j2vars['dict_var'] == {'key': 'value'}
    assert j2vars['dict_var']['key'] == 'value'
    assert j2v

# Generated at 2022-06-13 15:43:05.771484
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

# [ begin getitem_test_code ]
    from ansible.parsing.vault import VaultLib
    from ansible.template import Templar
    from ansible.errors import AnsibleUndefinedVariable
    import pytest

    vault_password = 'secret'

    vault_text = VaultLib(vault_password).encrypt(u"my secret")

    my_globals = dict(
        vault=vault_text
    )

    my_locals = dict(
        myhost=u"hostname"
    )

    my_vars = dict(
        host=u"hostname",
        group=u"webservers",
        password=vault_text
    )

    # missing value


# Generated at 2022-06-13 15:43:14.113133
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():

    import ansible.utils.unsafe_proxy

    # with templar=Templar(),
    # some_var='foo',{'name': 'baz'} from module_utils, globals={'bar': 'foo'}
    globals = {'bar' : 'foo', }
    j2vars = AnsibleJ2Vars(None, globals,
                           locals={'some_var': 'foo', 'name': 'baz'})

    # Test positive __contains__ cases
    assert 'some_var' in j2vars
    assert 'name' in j2vars
    assert 'bar' in j2vars

    # Test negative __contains__ cases
    assert 'undefined_var' not in j2vars

    # Test __contains__ with a mocked Templar() object
    j2

# Generated at 2022-06-13 15:43:25.369100
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    # Prepare data for test case
    import ansible.template
    templar = ansible.template.Templar(loader=None)
    globals = dict()
    locals = dict(a=1, b="abc", c=dict(d="def"), e=[1,2,[3,4]])

    # Run test case and verify result
    vars_obj = AnsibleJ2Vars(templar, globals, locals=locals)
    for key, expect_val in locals.items():
        assert vars_obj[key] == expect_val
    try:
        vars_obj["xxx"]
    except KeyError:
        pass
    else:
        assert False, "Should raise KeyError"

# Generated at 2022-06-13 15:43:35.306280
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    templar = Templar(loader=None, variables={})
    globals = {'hostvars': {'foo.example.com': {}}}
    locals = {'item': {'key': 'value'}}
    vars = AnsibleJ2Vars(templar, globals, locals)

    assert vars['item']['key'] == 'value'
    assert vars['hostvars']['foo.example.com'] == {}, "'hostvars' should be {:}"
    assert vars['bar'] == None, "variable 'bar' should be None, but is: " + repr(vars['bar'])
    #assert vars['bar'] == None, "variable 'bar' should be None, but is: " + repr(vars['bar'])

# Generated at 2022-06-13 15:43:45.883714
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    class Dict:
        def __init__(self, list):
            self.list = list

    from units.compat.mock import patch, Mock
    from ansible.vars.hostvars import HostVars
    mock_templar = Mock()
    mock_templar.available_variables = {'variable1'}
    mock_globals = {'global1'}
    mock_locals = {'local1'}
    locals = {
            'l_local1': 'local1.2',
            'l_local2': 'local2.2',
            'context' : 'context',
            'environment': 'environment',
            'template': 'template'
            }

# Generated at 2022-06-13 15:43:55.114069
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    import pytest
    from ansible.vars.hostvars import HostVars
    from ansible.vars.reserved import Reserved

    reserved = Reserved()

# Generated at 2022-06-13 15:44:02.141049
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    _templar = Templar(loader=DataLoader())
    _templar.available_variables = dict(var0='value')

    _obj = AnsibleJ2Vars(_templar, dict(var1='value'))
    assert 'var0' in _obj
    assert 'var1' in _obj


# Generated at 2022-06-13 15:44:13.268425
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    class mock_templar(object):
        def __init__(self):
            self.available_variables = {'available_variables': True}

        def template(self, variable, fail_on_undefined=True):
            return variable

    class mock_vars(object):
        def __init__(self):
            self.early_debug = True

    class mock_hostvars(object):
        def __init__(self):
            self.hostvars = True

    class mock_unsafe(object):
        def __init__(self):
            self.__UNSAFE__ = True

    templar = mock_templar()
    globals = {'globals': True}
    locals = {'locals': True}
    ansible_j2_vars = AnsibleJ2Vars

# Generated at 2022-06-13 15:44:23.016810
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils._text import to_native
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    from collections import Iterable
    from copy import copy

    cls = AnsibleJ2Vars
    Templar = Templar
    # AnsibleJ2Vars.__len__()

    # Test 1
    templar = Templar(loader=None)
    m = cls(templar, dict(var1=1, var2=2), dict(var3=3, var4=4))
    assert len(m) == 4

    # Test 2

# Generated at 2022-06-13 15:44:46.952728
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from io import StringIO

    VM = VariableManager()

    class MyVars(AnsibleJ2Vars):
        pass

    map = dict()
    map['vars'] = { 'a': 'a' }
    map['vars_files'] = [ 'group_vars/all', 'host_vars/1' ]

    VM.extra_vars = map['vars']
    VM.options_vars = map['vars_files']
    VM.host_vars = dict()
    VM.host_vars['1'] = dict()
    VM.host_vars['1']['a'] = 'a'
    VM.set_inventory(VM.loader.load_inventory_from_source('localhost,'))


# Generated at 2022-06-13 15:44:55.007165
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar

    def init_templar(available_variables=None, local_vars=None):
        if available_variables is None:
            available_variables = {}
        if local_vars is None:
            local_vars = {}
        templar = Templar(loader=None, variables=available_variables)
        return templar, locals

    templar, locals = init_templar()
    vars = AnsibleJ2Vars(templar, locals)
    for varname in ('a1', 'a2', 'b1', 'b2', 'c1', 'c2'):
        assert(vars.__contains__(varname))

    templar, locals = init_templar({'a1': 1, 'a2': 2})

# Generated at 2022-06-13 15:44:58.199613
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    # FIXME: unit test for this method, for the moment it doesn't need one.
    pass

# Generated at 2022-06-13 15:45:01.177308
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    globals = {}
    templar = None
    locals = None
    ajv = AnsibleJ2Vars(templar, globals, locals=locals)
    assert 'some_key' not in ajv

# Generated at 2022-06-13 15:45:08.195452
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.template import Templar

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['examples/hosts'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    myvars = variable_manager.get_vars(host=inventory.get_host('foobar'))
    mytemplate = Templar(loader=loader, variables=variable_manager.get_vars(host=inventory.get_host('foobar')), shared_loader_obj=loader)
    locals = dict()
    globals = dict()
    obj = AnsibleJ2Vars(mytemplate, globals, locals)

# Generated at 2022-06-13 15:45:17.388276
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():

    class FakeTemplar(object):
        def __init__(self):
            self.available_variables = {}
        def template(self, data):
            return data

    class FakeGlobals(object):
        def __getitem__(self, k):
            return k

    class FakeLocals(object):
        def __getitem__(self, k):
            return k

    vars = AnsibleJ2Vars(FakeTemplar(), FakeGlobals(), locals=FakeLocals())

    assert('locals' in vars)
    assert('available_variables' in vars)
    assert('globals' in vars)
    assert('not_present' not in vars)


# Generated at 2022-06-13 15:45:22.456065
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    import jinja2
    from ansible.template import Templar
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText


    templar = Templar()
    global_vars = AnsibleUnsafeText("Globals")
    local_vars = AnsibleUnsafeText("Locals")

    ansiblej2vars = AnsibleJ2Vars(templar, global_vars, locals=local_vars)

    assert len(ansiblej2vars) == 2


# Generated at 2022-06-13 15:45:23.509295
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    pass

#

# Generated at 2022-06-13 15:45:24.141087
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    pass

# Generated at 2022-06-13 15:45:35.756190
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar

    templar = Templar(loader=None)

    # Using real vars for these tests
    vars_obj = {}
    vars_obj['v1'] = 42
    vars_obj['v2'] = "{{ x }}"
    vars_obj['v3'] = "{{ v1 }}"
    vars_obj['v4'] = "{{ v1 }}"
    vars_obj['v5'] = "{{ v1 }}"
    vars_obj['v6'] = "{{ v1 }}"
    vars_obj['v7'] = "{{ v6 }}"
    vars_obj['v8'] = "{{ v7 }}"
    vars_obj['v9'] = "{{ v8 }}"

    # Defining global variables for testing
    gvars

# Generated at 2022-06-13 15:46:16.216962
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    import unittest

    class AnsibleJ2Vars_UT(unittest.TestCase):
        """
        Test class for AnsibleJ2Vars.
        """

        def setUp(self):
            """ setup test environment """
            import ansible.config.manager
            import ansible.template.template

            ansible_cfg = ansible.config.manager.ConfigManager()

            self.test_templar = ansible.template.template.Templar(loader=None, variables=None,
                                                                  shared_loader_obj=None,
                                                                  env=ansible_cfg.get_environment())

        def test__behavior_of_AnsibleJ2Vars(self):
            """ test __contains__ method of class AnsibleJ2Vars """

            # create test object

# Generated at 2022-06-13 15:46:24.685877
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.template import Templar
    _loader = DataLoader()
    _variable_manager = VariableManager()
    _templar = Templar(loader=_loader, variables=_variable_manager)
    j2_vars = AnsibleJ2Vars(_templar, {}, {'l_name': 'test', 'l_age': 10})

    assert 'name' in j2_vars
    assert 'age' in j2_vars
    assert 'l_name' in j2_vars
    assert 'l_age' in j2_vars
    assert 'context' not in j2_vars
    assert 'environment' not in j2_vars
    assert 'template' not in j

# Generated at 2022-06-13 15:46:31.487124
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    from ansible.template import Templar
    templar = Templar()
    a = {'a': 1, 'b': 2}
    b = {'c': 3, 'd': 4}
    j = AnsibleJ2Vars(templar, a, b)
    answer = set(['c', 'd', 'a', 'b'])
    assert set(j.__iter__()) == answer
    assert set(j) == answer  # test __iter__ is used by default

# Generated at 2022-06-13 15:46:38.747278
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    import jinja2
    import collections

    assert issubclass(AnsibleJ2Vars, collections.Mapping)


# Generated at 2022-06-13 15:46:49.467437
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    templar = Templar(loader=None, variables={'var': 42})
    var = AnsibleJ2Vars(templar, globals=dict())

    # should use __getitem__
    assert var['var'] == 42 

    # should use __contains__
    assert 'var' in var

    # should use __iter__
    assert list(iter(var)) == ['var']

    # should use __len__
    assert len(var) == 1

    # should raise KeyError for inexistent variable
    expected_message = "undefined variable: inexistent_var"
    raised = False
    try:
        var['inexistent_var']
    except KeyError as err:
        raised = True
        assert str(err) == expected_message
    assert raised

# Generated at 2022-06-13 15:46:55.702551
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import os
    import unittest

    from ansible.errors import AnsibleUndefinedVariable
    from ansible.template import Templar

    from ansible.vars.hostvars import HostVars

    hostvars = HostVars(dict())
    templar = Templar(loader=None)
    templar._available_variables = {
        "vars": hostvars
    }

    globals = {
        "hostvars": hostvars
    }

    locals = {
        "l_special": "SPECIAL"
    }

    J2V = AnsibleJ2Vars(templar, globals, locals)

    # Test that exception is thrown if var is not present in any scope.

# Generated at 2022-06-13 15:47:05.845747
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.template import Templar
    from itertools import chain
    from collections import Mapping
    vars_ = dict(map(reversed, chain(enumerate([str(i) * 10] * 10, 1),
                                     enumerate([str(i) * 20] * 10, 1))))
    templar = Templar(None, None, None)
    for locals_ in (None, dict(), vars_):
        ansible_j2_vars = AnsibleJ2Vars(templar, vars_, locals_)
        assert len(ansible_j2_vars) == len(vars_) + len(locals_)
        if isinstance(locals_, Mapping):
            assert len(locals_) == len(ansible_j2_vars._locals)

# Generated at 2022-06-13 15:47:12.618695
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    templar = Templar(loader=None, variables={})
    globals = {'test_global': 't_g'}
    locals  = {'test_local':  't_l'}
    ansible_j2_vars = AnsibleJ2Vars(templar, globals, locals)

    assert 'test_global' in ansible_j2_vars
    assert 'test_local'  in ansible_j2_vars
    assert 'test_host'   in ansible_j2_vars


# Generated at 2022-06-13 15:47:18.762193
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.vars.hostvars import HostVars
    hostvars=HostVars()
    templar=templar=MockTemplar()
    globals=dict(file="foo.txt", namespace="default")
    proxy=AnsibleJ2Vars(templar, globals, locals=None)
    assert proxy["file"]=="foo.txt"
    assert proxy["vars"]==hostvars


# Generated at 2022-06-13 15:47:23.710883
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    t = Templar(loader=None)
    templar = AnsibleJ2Vars(t, globals=dict())
    assert 'vars' not in templar
    templar._templar.available_variables = dict(vars=dict())
    assert 'vars' in templar

# Generated at 2022-06-13 15:48:30.647962
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.vars.unsafe_variable import UnsafeVariable
    import jinja2
    import os
    import tempfile
    import textwrap
    import yaml

    # test non-templating variable
    ds = '''
        foo:
          baz:
            - 1
            - 2
            - 3
        bar:
            baz:
            - 4
            - 5
    '''
    test_dir = tempfile.mkdtemp()
    test_file = 'test.yml'