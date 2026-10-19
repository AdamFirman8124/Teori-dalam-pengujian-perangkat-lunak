

# Generated at 2022-06-13 15:38:35.988048
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    # Create a test object with a dictionary of data in its memory
    test_data = {
        "a":"b",
        "c":"d",
        "e":"f"
    }
    test_obj = AnsibleJ2Vars(None, None)

    # Make sure every item in memory is yielded by __iter__
    for i in test_obj:
        assert i in test_data.keys()



# Generated at 2022-06-13 15:38:46.595785
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    ''' return value of __getitem__() method of AnsibleJ2Vars class
    '''
    # define AnsibleJ2Vars object
    templar=None
    globals=None
    locals=None
    jvars=AnsibleJ2Vars(templar, globals, locals)

    # test not existed variable
    try:
        result=jvars.__getitem__('not_exist_var')
    except KeyError as e:
        assert True

    # test existed variable
    templar.available_variables={'varname':'value'}
    val=jvars.__getitem__('varname')
    assert val == 'value'

# Generated at 2022-06-13 15:38:51.878137
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    templar = Templar(loader=None)
    globals = {}

    AnsiJ2Var = AnsibleJ2Vars(templar, globals)

    assert 'test' not in AnsiJ2Var

    AnsiJ2Var._templar.available_variables['test'] = 'test1'
    assert 'test' in AnsiJ2Var

    AnsiJ2Var._templar.available_variables['test'] = 1
    assert 'test' in AnsiJ2Var

    AnsiJ2Var._templar.available_variables['test'] = AnsibleUnsafeText(u'test1')

# Generated at 2022-06-13 15:39:01.699672
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    def Templar(available_variables):
        class Templar:
            available_variables = available_variables
        return Templar()

    # case1 test AnsibleJ2Vars.__getitem__.
    #var_name = 'varname', templar = Templar({'varname':'varname'}), globals = dict(varname='varname')
    templar = Templar({'varname':'varname'})
    globals = dict(varname='varname')
    locals = {}
    ansible_j2vars = AnsibleJ2Vars(templar, globals, locals)
    varname = 'varname'
    assert varname in ansible_j2vars.__dict__['_locals']                                          # check if the var_

# Generated at 2022-06-13 15:39:13.918775
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    templar = Templar(loader=None, variables={'a': 'b'})
    globals = {'a': 'b'}

    case_mapping_dict = {'a': 'b', 'c': 'd'}
    case_iterable_dict = {'a': 'b', 'c': 'd', 'e': 'f'}
    case_string = "abcd"

    # Test dict
    case = AnsibleJ2Vars(templar, globals, locals=case_mapping_dict)
    assert iter(case) == iter(case_mapping_dict)

    # Test dict-like

# Generated at 2022-06-13 15:39:22.798223
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    '''
    ansible.utils.vars.AnsibleJ2Vars unit tests
    '''
    import pytest
    from ansible.utils.vars import AnsibleJ2Vars
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    templar = AnsibleJ2Vars(None, None)
    with pytest.raises(AnsibleUndefinedVariable):
        templar['foo']
    templar._templar.available_variables = {'foo': AnsibleUnsafeText(u'test')}
    templar._globals = {'bar': AnsibleUnsafeText(u'test')}
    templar._locals = {'baz': AnsibleUnsafeText(u'test')}

# Generated at 2022-06-13 15:39:30.113207
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars

    assert Templar().vars == {}
    assert Templar().available_variables == {}

    templar = Templar(loader=None)
    templar.vars = {}
    templar.available_variables = {}

    j2vars = AnsibleJ2Vars(templar, None)
    assert 'foo' not in j2vars

    templar.vars['foo'] = "bar"
    templar.available_variables = {}
    assert 'foo' not in j2vars

    templar.vars = {}
    templar.available_variables = {'foo': "bar"}
    assert 'foo' in j2vars

    templar.vars['foo']

# Generated at 2022-06-13 15:39:41.167486
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from ansible import templar

    class _Templar(templar.Templar):
        '''Class for test'''
        def __init__(self, variables):
            self.available_variables = variables

    variables = {
        "var1": "value1",
        "var2": "value2",
        "var3": "{{ value3 }}"
    }

    local = {
        "var1": "value1_local",
        "var3": "value3_local",
    }

    globals = {
        "var1": "value1_global",
        "var2": "value2_global",
        "var4": "value4_global"
    }

    templar = _Templar(variables)
    ansible_j2_vars = AnsibleJ

# Generated at 2022-06-13 15:39:50.520818
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars

    templar = Templar(loader=None)
    var1 = {'my_var1': 'Hello, World!'}
    var2 = {'my_var2': 'Goodbye, World!'}
    hostvars = HostVars(loader=None, variables=var1)
    v1 = AnsibleJ2Vars(templar, var2, locals=None)
    assert 'my_var1' in v1
    assert 'my_var2' in v1
    assert 'my_var3' not in v1


# Generated at 2022-06-13 15:39:55.694806
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    globals = dict(gbl='global')
    locals = dict(lcl='local')
    templar = dict(tmp='templar')

    proxy = AnsibleJ2Vars(templar, globals, locals)

    assert('gbl' in proxy)
    assert('lcl' in proxy)
    assert('tmp' in proxy)

    assert('xxx' not in proxy)


# Generated at 2022-06-13 15:40:09.226565
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import os
    import json
    import unittest
    import pytest
    from jinja2 import Environment, StrictUndefined
    from ansible.template import Templar

    class AnsibleJ2VarsTest(unittest.TestCase):
        '''
        test_AnsibleJ2Vars___getitem__()
        test AnsibleJ2Vars.__getitem__() method
        '''

        def setUp(self):
            '''
            initializer for each tests.
            '''
            self.templar = Templar(variables={'a': 'hello', 'b': {'c': 'world'}, 'd': '{{ a }}'})
            self.test_data = os.path.join(os.path.dirname(__file__), 'test_hostvars.json')

# Generated at 2022-06-13 15:40:21.447027
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.vars import variable_manager
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import UnsafeVaultLib

    # Mock methods
    class MockTemplar():
        '''
        Mock Templar class
        '''

        def __init__(self, available_variables):
            self.available_variables = available_variables

    class MockVaultLib(VaultLib):
        '''
        Mock VaultLib class
        '''

        def __init__(self, password_file):
            pass

    class MockUnsafeVaultLib(UnsafeVaultLib):
        '''
        Mock UnsafeVaultLib class
        '''

        def __init__(self, password_file):
            pass


# Generated at 2022-06-13 15:40:32.632968
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    vm = VariableManager()
    vm.add_host_vars(Host(name='some_host'), {'var1': 'a'})
    vm.add_host_vars(Host(name='some_other_host'), {'var2': 'a'})
    host_vars = HostVars(vm)
    templar = Templar(loader=None, variables=vm, shared_loader_obj=None)

    vars = AnsibleJ2Vars(templar, {})
    assert len(vars) == 2


# Generated at 2022-06-13 15:40:41.501877
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.parsing import vault
    from ansible.vars import VariableManager, HostVars
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import AnsibleVars
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import create_template_vars
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import UnsafeProxy
    ## Set up
    # Available variables
    available_variables = dict()
    available_variables['foo'] = 'bar'
    # Globals
    globals = dict()
    globals['one'] = 1
    globals['two'] = 2

# Generated at 2022-06-13 15:40:49.807630
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    from ansible.template import Templar
    import jinja2
    from ansible.parsing.dataloader import DataLoader

    dataloader = DataLoader()
    environment = jinja2.Environment(loader=dataloader, undefined=jinja2.StrictUndefined, trim_blocks=True)

    templar = Templar(loader=dataloader, variables={}, environment=environment)

    globals = jinja2.runtime.Context.get_default_globals()
    jinja2_vars = AnsibleJ2Vars(templar, globals);
    pass_test = True
    try:
        iter(jinja2_vars)
    except:
        pass_test = False
    assert pass_test == True

# Generated at 2022-06-13 15:40:58.724023
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    import pytest
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    templar = object()
    globals = {'g1':10.,'g2':"g2",'g3':AnsibleUnsafeText('g3')}
    locals  = {'l1':20.,'l2':"l2",'l3':AnsibleUnsafeText('l3')}
    vars = AnsibleJ2Vars(templar, globals, locals=locals)

    # Test for 'g1'
    assert 'g1' in vars

    # Test for 'g2'
    assert 'g2' in vars

    # Test for 'g3'
    assert 'g3' in vars

    # Test for 'l1'

# Generated at 2022-06-13 15:41:06.949582
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    templar = Templar(loader=None)
    # __getitem__ should return value of key in available_variables
    templar.available_variables = {'test_key': 1}
    j2_vars = AnsibleJ2Vars(templar, None)
    assert j2_vars['test_key'] == 1
    # __getitem__ should return value of key in globals
    j2_vars = AnsibleJ2Vars(templar, {'test_key': 1}, None)
    assert j2_vars['test_key'] == 1
    # __getitem__ should raise exception if key not in available_variables and globals
    templar.available_variables = {}

# Generated at 2022-06-13 15:41:17.660010
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.template.vars import AnsibleJ2Vars

    templar = Templar(loader=None, variables={}, shared_loader_obj=None)
    play_context = PlayContext(variable_manager=None, loader=None)
    play_context.CLIARGS = dict()
    play_context._set_fact_cache = []
    templar.set_available_variables(play_context)
    ansible_vars = AnsibleJ2Vars(templar, {}, {'a': 1, 'b': 'bb', 'c': AnsibleUnsafeText('{{a}}')})

    assert 'a' in ans

# Generated at 2022-06-13 15:41:21.332761
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    sut = AnsibleJ2Vars(templar=None, globals=None)
    varname = 'varname'
    value = 'value'
    sut._locals[varname] = value

    result = sut.__getitem__(varname)

    assert result == value



# Generated at 2022-06-13 15:41:27.757041
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar

    data = {'a': 1, 'b': 2, 'c': 3}
    templar = Templar(loader=None, variables=data)

    assert 'a' in AnsibleJ2Vars(templar, {})
    assert 'a' in AnsibleJ2Vars(templar, {'a': None})
    assert 'a' in AnsibleJ2Vars(templar, {'a': 1})

    assert 'b' in AnsibleJ2Vars(templar, {})
    assert 'b' in AnsibleJ2Vars(templar, {'b': None})
    assert 'b' in AnsibleJ2Vars(templar, {'b': 2})


# Generated at 2022-06-13 15:41:41.692305
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    # Initialize a templar with a set of variables
    templar = Templar(loader=None)
    templar._available_variables = {
        'foo': 'FOO',
    }

    # Initialize a globals dictionary
    globals = {
        'bar': 'BAR',
    }

    # Initialize a locals dictionary
    locals = {
        'baz': 'BAZ',
    }

    vars = AnsibleJ2Vars(templar, globals, locals)

    # Fetch 'foo' variable from templar
    assert vars['foo'] == 'FOO'

    # Fetch 'bar' variable from globals
    assert vars['bar'] == 'BAR'

    # Fetch 'baz' variable from locals

# Generated at 2022-06-13 15:41:48.037776
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.template import Templar

    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    from ansible.inventory.host import Host

    from ansible.vars.hostvars import HostVars

    templar = Templar(loader=None)
    globals = {}
    locals = None

    j2vars = AnsibleJ2Vars(templar, globals, locals=locals)

    # test case: undefined variable
    try:
        # __getitem__ should raise KeyError with the given message
        j2vars['undefined_var']
    except KeyError as e:
        assert e.args[0] == 'undefined variable: undefined_var'

    # test case: available_variables contains

# Generated at 2022-06-13 15:41:59.598531
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    
    #The following imports are required to use Templar class and builtin filters
    import jinja2
    from ansible.template import Templar
    from ansible.template.safe_eval import safe_eval

    #This is just a test code to test the AnsibleJ2Vars class
    def test__getitem__():
        templar = Templar(None, loader=None, variables=None)
        setattr(templar, 'available_variables', dict())
        setattr(templar, 'template', safe_eval)
        j2_vars = AnsibleJ2Vars(templar, globals=dict())
        j2_vars['test'] = 'testVar'
        assert j2_vars['test'] == 'testVar'
        pass


# Generated at 2022-06-13 15:42:09.768815
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():

   from ansible.template import Templar
   from ansible.vars.hostvars import HostVars
   from ansible.playbook.play_context import PlayContext

   dict_templar = dict()
   dict_templar['var1'] = 10
   dict_templar['var2'] = 20
   dict_templar['var3'] = dict()
   dict_templar['var3']['var4'] = 40
   dict_templar['var3']['var5'] = None
   dict_templar['var3']['var6'] = HostVars(dict())
   dict_templar['var3']['var7'] = dict()
   dict_templar['var3']['var7']['var8'] = 80


# Generated at 2022-06-13 15:42:21.105813
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from jinja2 import Template, Undefined
    from ansible import module_utils
    from ansible.module_utils._text import to_native
    from ansible.template import Templar
    from ansible.vars.unsafe_proxy import wrap_var

    templar = Templar(loader=None, variables={})
    my_globals = {'test1': 18, 'test2': 'test_string'}
    my_locals = {'test3': True, 'test4': [1, 5, 8]}
    ansible_vars = AnsibleJ2Vars(templar, my_globals, my_locals)

    # Test if key is in self._templar
    assert 'test1' in ansible_vars
    assert 'test2' not in ansible_vars
    #

# Generated at 2022-06-13 15:42:28.616459
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    # Create a class instance
    templar = []
    globals = dict()
    globals['hostvars'] = dict()
    globals['hostvars']['testhost'] = dict()
    globals['hostvars']['testhost']['testvar'] = 'testvar_testhost_value'
    globals['testglobal'] = 'testglobal_value'

    locals = dict()
    locals['testlocal1'] = 'testlocal1_value'
    locals['testlocal2'] = 'testlocal2_value'

    variables = AnsibleJ2Vars(templar, globals, locals)
    # Test if method __getitem__ of class AnsibleJ2Vars works properly
    assert variables['testglobal'] == 'testglobal_value'

# Generated at 2022-06-13 15:42:29.379889
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    # TODO
    pass


# Generated at 2022-06-13 15:42:39.641019
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    
    templar = Templar(loader=None, variables={'foo': 'bar'})
    globals = {'baz': 'baz'}
    locals = {'locals': 'locals'}
    j2vars = AnsibleJ2Vars(templar, globals, locals)

    if 'foo' not in j2vars:
        raise Exception("Failed to find j2vars variable 'foo'")

    if 'baz' not in j2vars:
        raise Exception("Failed to find j2vars variable 'baz'")

    if 'locals' not in j2vars:
        raise Exception("Failed to find j2vars variable 'locals'")


# Generated at 2022-06-13 15:42:43.238780
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    a = AnsibleJ2Vars(Templar(), VariableManager())
    a.__contains__("a")

# Generated at 2022-06-13 15:42:52.210693
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    from ansible.vars.hostvars import HostVars
    from ansible.template import Templar

    # Create a Templar object
    templar = Templar()

    # Create a dict of locals
    locals = dict()
    locals['l_fruits'] = 'apples'
    locals['l_numbers'] = '12345'

    # Create a dict of variables
    variables = dict()
    variables['fruits'] = 'apples'
    variables['numbers'] = '12345'

    # Create a dict of globals
    globals = dict()
    globals['g_fruits'] = 'apples'
    globals['g_numbers'] = '12345'

    # Create a host variables object
    host_vars = HostVars()

# Generated at 2022-06-13 15:43:06.274799
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    # TODO: how to test this?
    return True


# Generated at 2022-06-13 15:43:10.862649
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    from ansible.template import Templar
    from ansible.vars import hostvars
    templar = Templar()

    j2v = AnsibleJ2Vars(templar, hostvars)
    iter_j2v = j2v.__iter__()
    assert hostvars['inventory_dir'] == next(iter_j2v)
    assert 'inventory_dir' == next(iter_j2v)

# Generated at 2022-06-13 15:43:22.762456
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    import ansible.module_utils.facts
    import ansible.playbook.play
    import ansible.playbook.play_context
    import ansible.template.template
    import ansible.template.vars

    ansible_facts_obj = ansible.module_utils.facts.AnsibleFacts(dict(), '', None)
    facts = ansible_facts_obj.get_facts()

    templar = ansible.template.template.Templar(loader=None, variables={}, shared_loader_obj=None)
    templar._available_variables = ansible.template.vars.VarsModule(loader=None, variables=facts)

    play_context = ansible.playbook.play_context.PlayContext()
    play_context.setup_cache()


# Generated at 2022-06-13 15:43:25.153999
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    AnsibleJ2Vars(object, {'greeting': 'hello'}, locals={'name': 'world'})


# Generated at 2022-06-13 15:43:31.764953
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    templar = Templar(loader=None)
    locals={'name': 12, 'value': ['a', 'b', 'c']}
    available_variables={'name': 78, 'value': ['x','y','z']}
    ansible_vars = AnsibleJ2Vars(templar, {}, locals=locals)
    # Check if AnsibleJ2Vars __getitem__ works
    assert ansible_vars['name'] == locals['name']
    assert ansible_vars['value'] == locals['value']

# Generated at 2022-06-13 15:43:34.551037
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    # Test with all params
    # Test with no params
    # Test with one param
    # Test with several params

    assert(False)


# Generated at 2022-06-13 15:43:45.074460
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.vars.hostvars import HostVars
    glob = {}
    loc = None
    templar = Templar(loader=None)
    ansible_j2_vars = AnsibleJ2Vars(templar=templar, globals=glob, locals=loc)
    ansible_j2_vars.__templar.set_available_variables({})

    # test case with available variables
    mock_var_dict = {'test1': 10, 'test2': 'teststring'}
    ansible_j2_vars.__templar.set_available_variables(mock_var_dict)

# Generated at 2022-06-13 15:43:54.480018
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    import ansible.playbook.templar

    templar = ansible.playbook.templar.Templar(loader=None)
    globals = {}
    locals = {}
    ajv = AnsibleJ2Vars(templar, globals, locals)

    varname = "test_var"
    value = "value_for_test"
    templar.available_variables[varname] = value
    assert ajv[varname] == value

    options = {
        'minimal_jvars': False,
        'use_lookup_extensions': True
    }
    templar.set_available_variables(options)
    templar.available_variables[varname] = value
    assert ajv[varname] == value

    tem

# Generated at 2022-06-13 15:44:04.984343
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    import unittest
    import mock

    class AnsibleJ2VarsTestCase(unittest.TestCase):
        def setUp(self):
            self.ansible_vars = {'a': 'a', 'b': 'b', 'c': 'c'}
            self.globals = {'d': 'd', 'e': 'e', 'f': 'f'}
            self.current_locals = {'g': 'g', 'h': 'h', 'i': 'i'}
            self.mock_templar = mock.MagicMock()
            self.mock_templar.available_variables = self.ansible_vars

# Generated at 2022-06-13 15:44:14.880648
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.hostvars import HostVars
    from ansible.vars import VariableManager
    from ansible.template import Templar
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from jinja2 import DictLoader

    var = AnsibleUnsafeText("{{ pwd }}")
    globals = {'ansible_version': '2.0.0.2'}
    locals = {'pwd': '/home'}

    var_manager = VariableManager()
    var_manager.set_globals(globals)
    var_manager.set_nonpersistent_facts(dict())
    loader = DataLoader()

# Generated at 2022-06-13 15:44:39.678926
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    """
    Test method __contains__ for class AnsibleJ2Vars
    """
    from ansible.template import Templar
    import sys
    import jinja2
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    test_data = dict(
        l_test='local_test',
        g_test='global_test',
        v_test='var_test',
    )

    class MyJ2Vars(AnsibleJ2Vars):
        def __contains__(self, k):
            # if k in self._locals:
            #     return True
            if k in self._templar.available_variables:
                return True
            if k in self._globals:
                return True
            return False

   

# Generated at 2022-06-13 15:44:51.015714
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    pc = PlayContext()
    templar = Templar(loader=pc.variable_manager.loader)

    variables = {'test1': '{{var1}}', 'test2': '{{var2}}', 'test3': '{{var3}}'}
    undefined_variables = {'var1': 'something', 'var2': '{{something_else}}', 'var3': '{{something}}'}
    defined_variables = {'something': 'value', 'something_else': 'value'}
    all_vars = AnsibleJ2Vars(templar, defined_variables, locals=variables)

    # this test checks if the correct error occurs
    # if a variable is not defined
    error_occured = False

# Generated at 2022-06-13 15:44:59.052002
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    '''
    test method AnsibleJ2Vars.__getitem__
    '''

    from ansible.template.safe_eval import safe_eval
    from ansible.template.templar import Templar

    templar = Templar(loader=None, variables={})

    data = safe_eval("vars: {'var1': 'value1', 'var2': 'value2'}")
    # value1
    print(AnsibleJ2Vars(templar, data).__getitem__('var1'))
    # Traceback (most recent call last):
    #   File "/usr/lib/python2.7/site-packages/ansible/template/vars.py", line 73, in __getitem__
    #     raise KeyError("undefined variable: %s" % varname)
    # KeyError

# Generated at 2022-06-13 15:45:06.286775
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    g = dict({'a_g': 'a'})
    l = dict({'a_l': 'a'})
    # Let's add one key-value pair to global dictionary
    # and one key-value pair to local dictionary
    # with the same key 'a'
    #
    # The expected value of dict[a] is 'a' from local dict
    g['a'] = 'a_g'
    l['a'] = 'a_l'

    templar = Templar()
    global_vars = AnsibleJ2Vars(templar, g, l)

    print(global_vars['a'])

    assert global_vars['a'] == 'a_l'



# Generated at 2022-06-13 15:45:17.594161
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    class MyAnsibleJ2Vars(AnsibleJ2Vars):
        def __init__(self, templar, globals, locals=None):
            super(MyAnsibleJ2Vars, self).__init__(templar, globals, locals)
            self._templar.available_variables = {'foo': 'bar'}

    globals = {}
    locals = {}
    templar = None
    vars = MyAnsibleJ2Vars(templar, globals, locals)

    assert 'foo' in vars, 'Test that __contains__ works for foo (in _templar.available_variables)'
    assert 'not_foo' not in vars, 'Test that __contains__ works for not_foo (not in _templar.available_variables)'

# Generated at 2022-06-13 15:45:24.410127
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    # Note: This test serves only as documentation, since the method
    #   is not callable with public parameters from outside.

    # TODO: Add more elaborate test

    import ansible
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.template.safe_eval import safe_eval

    templar = ansible.template.template.Templar(loader=None, variables=None)
    templar.available_variables = ImmutableDict()

    from ansible.playbook.base import Base
    from jinja2 import DictLoader
    from ansible.playbook.handler import Handler
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role.include import RoleInclude

# Generated at 2022-06-13 15:45:35.909411
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    """
    This method tests that when a varname is not found in the locals
    or globals dictionaries, the undefined variable error is raised
    """

    from ansible.module_utils.common._collections_compat import UserDict
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.template.safe_eval import ansible_safe_eval
    from ansible.module_utils.six import StringIO

    templar = Templar(loader=None, variables={}, shared_loader_obj=None)

    locals = UserDict()
    locals.data = {'key': 'value'}
    locals = dict(locals)

    globals = dict()


# Generated at 2022-06-13 15:45:46.193729
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    class Templar(object):
        available_variables = {
            'v1': 'v1 value',
            'v2': 'v2 value',
            'v3': 'v3 value',
        }

    class Globals(object):
        globals_var = 'globals_var value'

    class Locals(object):
        locals_var = 'locals_var value'
        # following should be ignored
        variable        = 'is ignored'
        context         = 'is ignored'
        environment     = 'is ignored'
        template        = 'is ignored'
        l_var1          = 'is ignored'
        l_var2          = 'is ignored'

    templar      = Templar()
    globals      = Globals()
    locals       = Locals()


# Generated at 2022-06-13 15:45:54.314809
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from jinja2._compat import string_types
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.vars.hostvars import HostVars
    from ansible.template import Templar
    templar = Templar()

    mock_templar = MagicMock(spec=templar)
    globals = {'a': 'b'}
    locals = {'c': 'd'}
    a = AnsibleJ2Vars(mock_templar, globals, locals)
    varname = 'd'
    assert varname in a
    assert a[varname] == locals[varname]
    mock_templar.available_variables = {'b': 'c'}
    varname = 'b'
    assert varname

# Generated at 2022-06-13 15:46:03.716973
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    import sys
    sys.path.insert(0,'/src/ansible/lib/ansible/modules/')
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.callback import CallbackBase
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.utils.vars import load_extra_vars
    import yaml
    import json
    import jinja2
    import os
    import datetime
    import shutil
    import sys
    import re
    import difflib



# Generated at 2022-06-13 15:46:32.985718
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    templar = Templar()
    globals = dict(a='b', c=['d', 'e'])
    locals = dict(a='z')
    ajv = AnsibleJ2Vars(templar, globals, locals)
    assert 'a', 'c' in ajv


# Generated at 2022-06-13 15:46:40.772440
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import ansible.template.safe_eval as safe_eval
    from ansible.template.templar import Templar

    templar = Templar(loader=None, variables=dict(a=dict(var1='test1', var2='test2'), b='test3', c='test4'))
    ansible_j2_vars = AnsibleJ2Vars(templar, dict(d='test5', e='test6'))

    # test1
    assert ansible_j2_vars['a']['var1'] == 'test1'

# Generated at 2022-06-13 15:46:51.295583
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import ansible.vars.hostvars
    ansible_vars_hostvars = ansible.vars.hostvars
    # Test with some mock data
    # __getitem__ of Templar is expected to be called with 'foo' or 'bar' or 'vars' or 'hostvars' argument
    # and expects to receive an object of type dict or HostVars or int or str or AnsibleUndefinedVariable or AnsibleError
    expected_data_1 = [
        ('foo', 'foo'),
        ('bar', 42),
        ('vars', {'foo': 'foo', 'bar': 42}),
        ('hostvars', ansible.vars.hostvars.HostVars({'foo': 'foo', 'bar': 42}))
    ]

# Generated at 2022-06-13 15:47:02.274919
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    v = AnsibleJ2Vars()

    assert(v.__contains__("abc") == False)
    assert(v.__contains__("") == False)

    v = AnsibleJ2Vars(dict(), dict(), dict())

    assert(v.__contains__("abc") == False)
    assert(v.__contains__("") == False)

    t = dict()
    t["abc"] = "test"
    v = AnsibleJ2Vars(t, dict(), dict())

    assert(v.__contains__("abc") == True)
    assert(v.__contains__("") == False)

    v = AnsibleJ2Vars(dict(), {"abc":"test"}, dict())

    assert(v.__contains__("abc") == True)

# Generated at 2022-06-13 15:47:05.029949
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    from ansible.template import Templar
    for v in AnsibleJ2Vars(Templar(None), {}, {'hello': 'world'}):
        assert v == 'hello'


# Generated at 2022-06-13 15:47:13.609025
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    from ansible.parsing.vault import VaultLib
    from ansible.template.safe_eval import safe_eval

    from ansible.template.templar import Templar

    templar_cls = Templar(loader=None, variables={'vault_password': 'secret'})
    templar_cls._vault = VaultLib(['secret'])

    global_vars = {"var_a": "a", "var_b": "b"}
    local_vars = {"var_c": "c", "var_d": "d"}

    j2vars = AnsibleJ2Vars(templar_cls, global_vars, locals=local_vars)

    # Verify that the method __iter__ returns the correct elements

# Generated at 2022-06-13 15:47:20.003601
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.vars.hostvars import HostVars
    from ansible.template import Templar

    h = HostVars({})
    h.update({'foo' : 'bar', 'baz' : 'qux'})

    t = Templar({}, {})

    v = AnsibleJ2Vars(t, h)

    assert 'foo' in v
    assert 'baz' in v
    assert 'bar' not in v
    assert 'qux' not in v

# Generated at 2022-06-13 15:47:28.713883
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    available_variables = {'var1': "{{foo}}", 'var2': "{{bar}}"}
    templar_obj = Templar(variables=available_variables)
    global_variables = {'var1': "var1_value", 'bar': "var2_value"}
    local_variables = {'foo': "var3_value"}
    ansible_j2_vars = AnsibleJ2Vars(templar_obj, global_variables, local_variables)
    assert ansible_j2_vars['var1'] == "var1_value"
    assert ansible_j2_vars['var2'] == "var2_value"
    assert ansible_j2_vars['var3'] == "var3_value"

# Generated at 2022-06-13 15:47:33.529847
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    import numpy.testing as npt
    from ansible.template import Templar

    jvars = AnsibleJ2Vars(Templar(), {'a': 1, 'b': 2})
    npt.assert_equal(jvars.__contains__('a'), True)
    npt.assert_equal(jvars.__contains__('b'), True)
    npt.assert_equal(jvars.__contains__('c'), False)


# Generated at 2022-06-13 15:47:41.139039
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.playbook.templar import Templar
    from ansible.parsing.vault import VaultLib
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    vault_password = 'hunter2'