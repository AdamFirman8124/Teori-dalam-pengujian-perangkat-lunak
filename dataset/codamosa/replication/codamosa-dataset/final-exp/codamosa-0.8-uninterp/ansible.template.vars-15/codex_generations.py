

# Generated at 2022-06-13 15:38:39.114300
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    assert False, "Test is not implemented"


# Generated at 2022-06-13 15:38:43.584664
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    templar = None
    globals = {}
    locals = {'key':'value'}
    test_var = AnsibleJ2Vars(templar, globals, locals=locals)
    
    assert('key' in test_var)


# Generated at 2022-06-13 15:38:45.537567
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    from ansible.template import Templar
    templar = Templar(loader=None)

    test_obj = AnsibleJ2Vars(templar, {}, {})
    assert test_obj.__iter__() is not None



# Generated at 2022-06-13 15:38:51.627765
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from jinja2.utils import missing
    from ansible.template import Templar
    from ansible.vars import Version
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import combine_vars
    from ansible.utils import context_objects as co

    templar = Templar(co.GlobalCLIArgs())

    globals = dict()
    locals = dict()

    ansible_vars = dict()
    ansible_vars["ansible_version"] = Version()
    ansible_vars["ansible_version"]._data = {
        'full': "3.0.0",
        'major': "3",
        'minor': "0",
        'revision': "0",
        'string': "3.0.0"
    }

    vars

# Generated at 2022-06-13 15:39:01.522662
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.templating import Templar
    from ansible.template import TemplarEnvironment, AnsibleEnvironment
    from ansible.vars.hostvars import HostVars
    templar = Templar(TemplarEnvironment([], None, None, None))

    globals = {'a': 1}
    locals = templar.available_variables

    proxy = AnsibleJ2Vars(templar, globals, locals)
    got = proxy['a']
    assert got == 1

    globals = {}
    locals = templar.available_variables

    proxy = AnsibleJ2Vars(templar, globals, locals)
    got = proxy['a']
    assert got == 1

    globals = {}
    locals = templar.available_variables

    locals['f'] = 2

# Generated at 2022-06-13 15:39:04.795382
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
  from ansible.template import Templar
  j2vars = AnsibleJ2Vars(Templar(loader=None), globals={}, locals=None)
  assert j2vars.__getitem__('hoge') is None

# Generated at 2022-06-13 15:39:16.916485
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from ansible.playbook.play_context import PlayContext

    # Test setup
    context = PlayContext()
    context.vars = dict(fruit='apple', number=1)
    context.globals = dict(glob_fruit='glob_apple', glob_number=2)
    context.update_vars()

    # Test class constructor
    vars_proxy = AnsibleJ2Vars(context.templar, context.globals, locals=context.vars)

    # Test membership
    assert 'fruit' in vars_proxy
    assert 'number' in vars_proxy
    assert 'glob_fruit' in vars_proxy
    assert 'glob_number' in vars_proxy

    # Test getitem
    assert vars_proxy['fruit'] == 'apple'
    assert vars_proxy

# Generated at 2022-06-13 15:39:26.730013
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    vm = VariableManager()
    vm.set_globals({'foo': 'bar'})

    class Dummy(object):
        def __init__(self, variable_manager):
            self.variable_manager = variable_manager

    templar = Templar(loader=None, variables=vm, shared_loader_obj=None, environment=Dummy(vm))
    vars = AnsibleJ2Vars(templar, {'foo': 'bar'})
    assert vars.__contains__('hostvars') == True
    # assert vars.__contains__('myvar') == False
    # assert vars.__contains__('myglob') == False

# Generated at 2022-06-13 15:39:38.169148
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import ansible.template
    templar = ansible.template.AnsibleTemplar(loader=None)

    vars = {'a': 'b'}
    globals = {}
    locals = None

    # 1. getitem when `vars` is in templar.available_variables
    j2vars = AnsibleJ2Vars(templar, globals, locals)
    templar.available_variables = {'a': 'b', 'vars': vars}

    # 1.1 getitem when `vars` is in templar.available_variables, key `vars`
    vars = j2vars.__getitem__('vars')
    assert vars == {'a': 'b', 'vars': vars}

    # 1.2 getitem when `

# Generated at 2022-06-13 15:39:40.841696
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    ansible_vars = {'varname': 'value'}
    globals = {}
    locals = {}
    j2vars = AnsibleJ2Vars(ansible_vars, globals, locals)

    assert j2vars['varname'] == 'value'


# Generated at 2022-06-13 15:39:56.037553
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    # Create a Templar() object
    class Executor():
        def get_host_vars(self, host):
            return {'foo': 'bar'}
    class Play():
        def __init__(self):
            self.hostvars = {'127.0.0.1': {'foo': 'bar'}}
            self.name = 'play_name'
            self.vars = {'foo': 'bar'}
            self.vars_prompt = {}
            self.vars_files = []
    class Runner():
        def __init__(self, results_callback=None):
            self.host_vars = {'127.0.0.1': {'foo': 'bar'}}
            self.inventory = []
            self.results_callback = results_callback
            self.options = {}
           

# Generated at 2022-06-13 15:40:02.349016
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.template import Templar
    class Template:
        def __init__(self, name):
            self.name = name
    templar = Templar(loader=None, variables={'var1': Template('var1')})
    ansible_j2_vars = AnsibleJ2Vars(templar, {'global1': Template('global1')})
    assert len(ansible_j2_vars) == 4
    ansible_j2_vars._locals['local1'] = Template('local1')
    assert len(ansible_j2_vars) == 5
    ansible_j2_vars._templar.available_variables['var2'] = Template('var2')
    assert len(ansible_j2_vars) == 6
    ansible_j2_vars._

# Generated at 2022-06-13 15:40:10.795434
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils._text import to_native
    from ansible.template import Templar

    class TestAnsibleJ2Vars(AnsibleJ2Vars, Mapping):
        ''' This class is to get access to the private methods of the AnsibleJ2Vars class
        '''
        def __init__(self, vars):
            self.templar = Templar(variables=vars)
            self.templar._available_variables = vars
            AnsibleJ2Vars.__init__(self, self.templar, {})


# Generated at 2022-06-13 15:40:22.993371
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.playbook.included_file import IncludedFile
    from ansible.template import Templar

    config = {}
    parameters = {}
    variables = {}

    included_file = IncludedFile(config, parameters, variables)
    templar = Templar(loader=None, variables=variables, include_vars=included_file)

    j2_vars = AnsibleJ2Vars(templar, {})

    try:
        # should raise an exception because 'foo' doesn't exist
        _ = j2_vars['foo']
    except KeyError:
        pass
    else:
        assert False, "AnsibleJ2Vars.__getitem__ didn't fail on missing item."

    # no exception should be raised as 'foo' is now defined
    j2_vars._templar.available_

# Generated at 2022-06-13 15:40:33.762532
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import os
    import sys
    import json
    import ansible
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.template import Templar
    from ansible.module_utils.six import iteritems
    from ansible.utils.vars import load_extra_vars
    from ansible.plugins.loader import add_all_plugin_dirs

    class MyVarsModule:
        def get_vars(self, loader, path, entities, cache=True):
            return dict()

    test_dir = os.path.dirname(os.path.realpath(__file__))
    sys.path.insert(0, test_dir + "/../plugins/modules")  # Load plugins from this

# Generated at 2022-06-13 15:40:40.623479
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    class Templar(object):
        available_variables = {'a': 1, 'b': 2, 'c': 3}

    globals = {'var1': 'var1', 'var2': 'var2'}
    locals = {'local1': 'local1', 'local2': 'local2'}
    ansible_j2vars = AnsibleJ2Vars(Templar(), globals, locals)
    assert len(ansible_j2vars) == 7

# Generated at 2022-06-13 15:40:49.461852
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    # Arrange
    import ansible.template.safe_eval
    import ansible.template.templar

    class _templar(ansible.template.templar.Templar):

        def __init__(self):
            ansible.template.templar.Templar.__init__(self, loader=None, variables={})

        def available_variables(self):
            return {'v': 1}

        def template(self, val):
            return val

    globals = {
        'g': 1
    }
    locals = {
        'l': 2,
        'l_v': 3,
        'context': 4,
        'environment': 5,
        'template': 6
    }

    ansible_vars = AnsibleJ2Vars(_templar(), globals, locals)

# Generated at 2022-06-13 15:40:58.692187
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.vars.hostvars import HostVars
    hostvars = HostVars({"key1": "val1"})
    templar = "templar"
    globals = {"vars": {"key2": "val2"}}
    locals = {"key3": "val3"}
    vars = AnsibleJ2Vars(templar, globals, locals)
    # test key available in locals
    assert vars["key1"] == locals["key1"]
    # test key available in templar
    assert vars["key2"] == globals["vars"]["key2"]
    # test key available in globals
    assert vars["key3"] == locals["key3"]

    # test key not available in locals, templar and globals
    import pytest

# Generated at 2022-06-13 15:41:06.903248
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from ansible.template import Templar

    # Create the Templar object
    templar = Templar(loader=None, variables={'foo': 'bar', 'baz': {'quux': 'qux'}})

    # Create the AnsibleJ2Vars object
    vars = AnsibleJ2Vars(templar, {'debug': True, 'version': '2.2'})

    # Check the length
    assert len(vars) == 5

    # Check the __getitem__ method
    assert vars['debug'] == True
    assert vars['version'] == '2.2'
    assert vars['foo'] == 'bar'
    assert vars['baz']['quux'] == 'qux'

    # Check the __contains__ (in) operator method
    assert 'debug' in vars
   

# Generated at 2022-06-13 15:41:10.282402
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    t = Templar(None)
    t._available_variables = {"a": "b"}
    v = AnsibleJ2Vars(t, {})
    assert v["a"] == "b"


# Generated at 2022-06-13 15:41:20.502199
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    a = AnsibleJ2Vars(None, {'a':1, 'b':2})

    assert len(a) == 2

    a['x'] = 3
    a['y'] = 4

    assert len(a) == 4


# Generated at 2022-06-13 15:41:22.571228
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    # TODO: For now this is just a placeholder, in the future it would be nice to add some real tests
    #       (also, note that most of the features of this class are currently untested).
    return

# Generated at 2022-06-13 15:41:27.569624
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    from ansible.vars.hostvars import HostVars
    from ansible.vars import VariableManager
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext


# Generated at 2022-06-13 15:41:38.440780
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar

    test_data = {
        'ansible_datadirs': [ '/var/tmp/ansible-test' ],
        'ansible_facts': {
            'config': {
                'gid': '0'
            }
        },
        'ansible_pkg_mgr': 'homebrew',
        'ansible_python_interpreter': '/usr/bin/python',
        'foo': 'bar'
    }
    templar = Templar(loader=None, variables=test_data)

    aj2v = AnsibleJ2Vars(templar, globals={})

    assert 'ansible_facts' in aj2v
    assert 'foo' in aj2v

    assert aj2v['ansible_pkg_mgr'] == 'homebrew'


# Generated at 2022-06-13 15:41:46.870097
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar, TemplarError
    # create an instance of class AnsibleJ2Vars
    templar = Templar(loader=None)
    vars_mapping = AnsibleJ2Vars(templar, dict())
    # check if an Exception is raised when key is not present in dict
    try:
        _ = vars_mapping['key_not_present_in_dict']
        assert False
    except KeyError as e:
        assert str(e) == 'undefined variable: key_not_present_in_dict'
    # check if an Exception is raised when variable is undefined
    from ansible.parsing.yaml.objects import AnsibleUnicode
    value = AnsibleUnicode('{{ key_not_defined }}')

# Generated at 2022-06-13 15:41:59.534669
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():

    '''
    This function is used to test the AnsibleJ2Vars class.
    '''

    # Import the needed modules.
    from ansible.parsing import vault

    # Create the needed objects.
    templar = AnsibleJ2Vars()
    globals = AnsibleJ2Vars()
    locals = AnsibleJ2Vars()

    # Create the AnsibleJ2Vars object.
    aj2vars = AnsibleJ2Vars(templar, globals, locals)

    assert aj2vars.__contains__('vault') == False

    vault_passwords = vault.get_vault_password('vault')
    aj2vars.vault_password = vault_passwords

    assert aj2vars.__contains__('vault') == True


# Generated at 2022-06-13 15:42:09.724524
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    import tempfile

    templar = get_templar()
    vars = dict()

    j2vars = AnsibleJ2Vars(templar, vars)
    expected_len = 0
    actual_len = len(j2vars)
    assert actual_len == expected_len

    j2vars = AnsibleJ2Vars(templar, vars)
    expected_len = 1
    j2vars._locals['test'] = 1
    actual_len = len(j2vars)
    assert actual_len == expected_len

    j2vars = AnsibleJ2Vars(templar, vars)
    expected_len = 1
    j2vars._globals['test'] = 1
    actual_len = len(j2vars)
    assert actual

# Generated at 2022-06-13 15:42:15.290068
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.parsing import DataLoader
    from ansible.vars.hostvars import HostVars
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.template.template import AnsibleTemplate

    fixture = dict(
        hostvars = HostVars(
            host = Host("localhost", "127.0.0.2"),
            variables = dict(a="b")
        ),
        templar = AnsibleTemplate(
            loader = DataLoader(),
            variables = VariableManager()
        )
    )

    # Test template on a dictionary
    fixture['templar'].available_variables = {'vars': fixture['hostvars']}

# Generated at 2022-06-13 15:42:25.604130
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import jinja2
    from ansible.template import Templar

    loc = { 'f': 'foo'}
    tem = Templar(loader=None, variables={})
    jv = AnsibleJ2Vars(tem, {}, locals=loc)

    # If the key exists in 'self._locals', we should be returning
    # a value.
    assert jv['f'] == loc['f']

    # If the key exists in 'self._templar.available_variables',
    # we should return a value.
    tem = Templar(loader=None, variables={'g': 'goo'})
    jv = AnsibleJ2Vars(tem, {}, locals={})
    assert jv['g'] == tem.available_variables['g']


# Generated at 2022-06-13 15:42:34.697522
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.vars.hostvars import HostVars
    from ansible.template import Templar
    template_class = dict(
        one=1,
        two='{{ one }}'
    )
    globals_ = dict(
        three='foo'
    )
    locals_ = dict(
        three='foo'
    )
    templar = Templar(loader=None, variables=template_class)
    jvars = AnsibleJ2Vars(templar, globals_, locals_)

    assert 'one' in jvars
    assert 'three' in jvars
    assert 'two' not in jvars
    assert 'four' not in jvars
    assert 'five' not in jvars
    assert 'vars' in jvars

    # Also need to ensure that HostVars

# Generated at 2022-06-13 15:42:54.602517
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib
    j2_vars = AnsibleJ2Vars(Templar(vault_secrets=VaultLib()), globals=dict())
    variables = dict(var='test')

    assert j2_vars['var'] == 'test'


# Generated at 2022-06-13 15:43:04.356432
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop as mock_unfrackpath
    from ansible.vars.manager import VariableManager

    templar = Templar(loader=DictDataLoader(), variables={})
    variable_manager = VariableManager()
    variable_manager.set_host_variable("host1", dict(var1="defined"))
    variable_manager.set_host_variable("host2", dict(var2="defined"))
    variable_manager.set_host_variable("host3", dict(var3="defined"))
    variable_manager.set_host_variable("host4", dict(var4="defined"))
    variable_manager.set_

# Generated at 2022-06-13 15:43:11.028418
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    context = PlayContext()
    templar = Templar(loader=None, variables=context._replacement_vars)
    globals = dict()
    locals = dict()
    ansiblej2vars = AnsibleJ2Vars(templar, globals, locals)
    ansiblej2vars['Foo'] = 'BadTemplate'
    with pytest.raises(AnsibleError):
        ansiblej2vars.__getitem__('Foo')

# Generated at 2022-06-13 15:43:23.180110
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template.safe_eval import ansible_safe_eval

    class Templar(object):
        '''
        Class to fake ansible.vars.Templar
        '''
        def __init__(self, available_variables):
            self.available_variables = available_variables

    x = {'a': 1}
    # emulate ansible variable 'inventory_hostname'
    globals = {'inventory_hostname': 'localhost'}
    # emulate ansible variable 'inventory_hostname_short'
    locals = {'l_inventory_hostname_short': 'localhost'}

    templar = Templar(ansible_safe_eval(x))
    vars_obj = AnsibleJ2Vars(templar, globals, locals)

    assert 'a' in vars_obj



# Generated at 2022-06-13 15:43:30.077272
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    templar = None
    globals = dict(t1='g1', t2='g2')
    locals = dict(t3='l3', t4='l4')

    v = AnsibleJ2Vars(templar, globals, locals)

    assert 't1' in v
    assert 't2' in v
    assert 't3' in v
    assert 't4' in v
    assert 't5' not in v
    assert 't6' not in v

    for i in v:
        assert i in ['t1','t2','t3','t4']


# Generated at 2022-06-13 15:43:41.257563
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    import ansible.template

    # Test valid parameters
    test_templar = ansible.template.Templar(loader=None)
    ansible_j2_vars = AnsibleJ2Vars(templar=test_templar, globals=dict())
    assert len(ansible_j2_vars) == 0

    # Test spurious parameters
    with pytest.raises(AssertionError):
        len(AnsibleJ2Vars(templar=test_templar, globals=None))
    with pytest.raises(AssertionError):
        len(AnsibleJ2Vars(templar=None, globals=dict()))

# Generated at 2022-06-13 15:43:49.363789
# Unit test for method __contains__ of class AnsibleJ2Vars

# Generated at 2022-06-13 15:43:59.731404
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    # Test for method __getitem__ of class AnsibleJ2Vars
    #
    # If varname in self._locals
    #
    # Returns:
    #
    # Return the local variable
    #
    # Raises:
    #
    # If varname in self._templar.available_variables
    #
    # Returns:
    #
    # Return the variable by templating it.
    #
    # Can raise:
    #
    # AnsibleUndefinedVariable if variable is missing
    # AnsibleError if templating fails
    #
    # If varname in self._globals
    #
    # Returns:
    #
    # The variable in globals
    #
    # Raises:
    #
    # KeyError if variable is missing
    pass

# Generated at 2022-06-13 15:44:03.827902
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    class MockTemplar(object):
        def __init__(self):
            self.available_variables = dict()
        def template(self, variable):
            return variable

    v = AnsibleJ2Vars(MockTemplar(), dict())
    assert v['a.b'] == 'a.b'

# Generated at 2022-06-13 15:44:08.237488
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    v = dict(a=1, b=2, c=3)
    x = AnsibleJ2Vars(None, v)
    assert len(x) == len(v)


# Generated at 2022-06-13 15:44:48.574874
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template.safe_eval import unsafe_eval
    from ansible.template import Templar
    templar = Templar(loader=None, variables={'a': 10})
    t = AnsibleJ2Vars(templar, globals={'b':20})
    assert 'a' in t
    assert 'b' not in t # 'b' exists, but in global scope, not in t
    assert 'c' not in t

    # test handling of context/environment/template
    locals = dict(context='context', environment='environment', template='template')
    t = AnsibleJ2Vars(templar, globals=dict(), locals=locals)
    assert 'context' in t
    assert 'environment' in t
    assert 'template' in t

    # test availability of built-in functions
    assert 'min'

# Generated at 2022-06-13 15:44:55.958418
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():

    # Test the initial state of AnsibleJ2Vars
    ansible_j2_vars = AnsibleJ2Vars(None, globals=None, locals=None)
    assert 'foo' not in ansible_j2_vars
    assert 'foo' not in ansible_j2_vars
    assert 'foo' not in ansible_j2_vars

    # Test the state of AnsibleJ2Vars after calling __init__
    ansible_j2_vars = AnsibleJ2Vars(None, globals={'foo': 'bar'}, locals=None)
    assert 'foo' in ansible_j2_vars
    assert 'foo' in ansible_j2_vars

# Generated at 2022-06-13 15:44:57.600307
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    assert True


# Generated at 2022-06-13 15:45:07.786194
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    import sys
    import os
    import unittest
    sys.path.append(os.path.dirname(__file__) + '/../')
    import jinja2
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret

    class Test_AnsibleJ2Vars(unittest.TestCase):

        def setUp(self):
            from ansible.template import Templar
            from ansible.vars.vars_loader import DataLoader

            vault_secret = VaultSecret('vault_password')
            self.vault_passwords = [vault_secret.load()]

            self.loader = DataLoader()
            self.loader.set_vault_secrets(self.vault_passwords)
            self.templar = Templar

# Generated at 2022-06-13 15:45:18.057873
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    import sys
    import nose.tools

    import ansible.template
    import ansible.variables.hostvars

    t = ansible.template.template.AnsibleJ2Vars(
        ansible.template.Templar(loader=ansible.parsing.dataloader.DataLoader()),
        globals=dict(foo=[1, 2, 3]),
        locals=dict(bar=dict(a=1, b=2))
    )

    if sys.version_info[0] >= 3:
        expected_keys = frozenset(['foo', 'bar'])
    else:
        expected_keys = set(['foo', 'bar'])
    i = iter(expected_keys)
    for k in t:
        nose.tools.eq_(k, next(i))

# Generated at 2022-06-13 15:45:22.879357
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    from ansible.parsing.yaml.loader import AnsibleLoader

    vars_dict = AnsibleLoader(None, variable_start_string="%{", variable_end_string="}%").load("""
        test_int: 100
        test_str: "%{test_var}%"
        test_var: "test variable"
        test_undefined_var: "%{undefined_var}%"
        """)['data']
    templar = Templar(loader=None)
    test_vars = AnsibleJ2Vars(templar, {}, locals=vars_dict)

    # Test that you can get valid variables
    assert test_vars['test_int'] == 100
    assert test_vars['test_str'] == 'test variable'

    # Test that

# Generated at 2022-06-13 15:45:34.820247
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play = Play().load({}, variable_manager=variable_manager, loader=loader)
    templar = Templar(loader=loader, variables=variable_manager.get_vars())

    var_dict = {'somevar':'somevalue'}
    vars = AnsibleJ2Vars(templar, globals=var_dict)
    # expected number of variables is

# Generated at 2022-06-13 15:45:44.888256
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.errors import AnsibleError
    from ansible.plugins.loader import lookup_loader
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    templar = Templar(loader=None)
    globals = {
        'range' : range,
        'lookup': lookup_loader.get('debug'),
    }
    vars = AnsibleJ2Vars(templar, globals)

    # test AnsibleUnsafeText class
    assert(vars[AnsibleUnsafeText('range')] is range)

# Generated at 2022-06-13 15:45:49.827702
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    templar = Templar(None, loader=None)
    var = AnsibleJ2Vars(templar, globals={}, locals={'foo': 'bar'})
    assert var['foo'] == 'bar'
    assert var.__getitem__('foo') == 'bar'


# Generated at 2022-06-13 15:46:00.611842
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    class Templar():
        available_variables = dict()
        def template(self, the_str):
            return the_str

    aj2v = AnsibleJ2Vars(Templar(), dict())

    assert 'key' not in aj2v
    aj2v._locals['key'] = 'local_val'
    assert 'key' in aj2v
    assert aj2v['key'] == 'local_val'

    Templar.available_variables = dict(key='global_val')
    assert aj2v['key'] == 'global_val'

    aj2v._globals['key'] = 'global_val'
    assert aj2v['key'] == 'global_val'

# Generated at 2022-06-13 15:47:24.069124
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    # Test the first branch: if varname in self._locals:
    #     return self._locals[varname]
    # 1. varname is in self._locals
    # 1.1 local is dict
    proxy = AnsibleJ2Vars(None, None, locals={"a": 1})
    assert(proxy.__getitem__("a") == 1)
    # 1.2 local is not dict
    class test():
        def __init__(self,a):
            self.a = a
    proxy = AnsibleJ2Vars(None, None, locals={"b": test(2)})
    assert(proxy.__getitem__("b").a == 2)

    # Test the second branch:
    # if varname in self._templar.available_variables:
    #     variable = self._

# Generated at 2022-06-13 15:47:29.110861
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template.safe_eval import safe_eval
    from ansible.template.template import Templar
    from ansible.template.vars import AnsibleJ2Vars

    # __getitem__(self, varname):

    # if varname in self._locals:
    #     return self._locals[varname]
    locals = {}
    templar = Templar(loader=None, variables=None)
    globals = {}
    proxy = AnsibleJ2Vars(templar, globals, locals)
    varname = 'key'
    locals[varname] = 'value'
    assert proxy[varname] == 'value'

    # if varname in self._templar.available_variables:
    #     variable = self._templar.available_variables[varname

# Generated at 2022-06-13 15:47:31.401715
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    # TODO
    raise NotImplementedError()

# Generated at 2022-06-13 15:47:39.029002
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    # Arrange
    templar = None
    g = {"g1": "g1"}
    l = {"l1": "l1"}
    a = AnsibleJ2Vars(templar, g, l)

    # Act
    r1 = "l1" in a
    r2 = "g1" in a
    r3 = "x" in a

    # Assert
    assert r1 == True
    assert r2 == True
    assert r3 == False

# Generated at 2022-06-13 15:47:40.159450
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    # Need to write unit test for this method
    assert(False)


# Generated at 2022-06-13 15:47:44.087852
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.template import Templar

    j2vars = AnsibleJ2Vars(Templar(), dict())
    # Call the method
    length = len(j2vars)
    # Check that the result is the expected one
    assert length == 0, "Unexpected result."

# Generated at 2022-06-13 15:47:54.334222
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    '''
    AnsibleJ2Vars.__contains__ unit test
    '''
    class TestTemplar:
        '''
        fakes a Templar object
        '''
        def __init__(self, available_vars):
            self.available_variables = available_vars

    aj2v = AnsibleJ2Vars(TestTemplar({'key1': 'val1'}), {'key2': 'val2'}, {'l_key3': 'val3'})
    assert 'key1' in aj2v
    assert 'key2' in aj2v
    assert 'key3' in aj2v
    assert 'l_key1' not in aj2v
    assert 'l_key2' not in aj2v

# Generated at 2022-06-13 15:48:05.900350
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.inventory import Host
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject, AnsibleSequence

    inv_host = Host('hostname')


# Generated at 2022-06-13 15:48:13.663538
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    templar = Templar(loader=None)
    ansible_j2_vars = AnsibleJ2Vars(templar, dict())
    if dict() not in ansible_j2_vars:
        assert False
    if ansible_j2_vars[dict()] is not None:
        assert False
    if 'test' not in ansible_j2_vars:
        assert False



# Generated at 2022-06-13 15:48:20.914117
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    test_vars = {'a': 'A', 'b': 'B'}
    test_globals = {'g': 'G'}
    test_locals = {'l': 'L'}

    class TestTemplar():
        def __init__(self):
            self.available_variables = test_vars
            self._available_variables_cache = dict()

    templar = TestTemplar()
    vars_obj = AnsibleJ2Vars(templar, test_globals, locals=test_locals)

    ansible_keys = set()
    ansible_keys.update(test_vars, test_locals, test_globals)

    assert len(ansible_keys) == 4

    iter_keys = set()