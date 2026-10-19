

# Generated at 2022-06-13 15:38:39.095945
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.template import Templar
    templar = Templar(loader=None)

    # Test case 1
    aj2v = AnsibleJ2Vars(templar, {'hostvars': 'hostvars'})
    assert len(aj2v) == 1

    # Test case 2
    aj2v = AnsibleJ2Vars(templar, {'hostvars': 'hostvars', 'var1': 'var1'})
    aj2v._locals['var2'] = 'var2'
    assert len(aj2v) == 3

    # Test case 3
    aj2v = AnsibleJ2Vars(templar, {'hostvars': 'hostvars', 'var1': 'var1'})
    aj2v._templar.available_variables

# Generated at 2022-06-13 15:38:49.606264
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleMapping
    my_templar = Templar()
    my_ansible_mapping = AnsibleMapping()
    my_ansible_mapping['my_key'] = 'my_val'
    my_ansible_mapping['my_key2'] = 'my_val2'
    my_ansible_mapping['my_key3'] = 'my_val3'
    my_ansible_mapping['my_key4'] = 'my_val4'
    my_ansible_mapping['my_key5'] = 'my_val5'
    my_globals = {'g_key': 'g_val'}

# Generated at 2022-06-13 15:38:57.735698
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    # Here we have to import Templar temporarily
    from ansible.template.safe_eval import Templar

    templar = Templar()
    globals = {}
    locals = {'k1': 'v1'}
    ansible_j2_vars = AnsibleJ2Vars(templar, globals, locals)

    print(ansible_j2_vars.keys())
    print(ansible_j2_vars['k1'])


if __name__ == "__main__":
    test_AnsibleJ2Vars()

# Generated at 2022-06-13 15:39:01.852826
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    templar = get_templar()
    test_vals = "test_val_1"
    test_key = "test_key_1"
    test_vals_dict = {test_key: test_vals}
    j2_vars = AnsibleJ2Vars(templar, test_vals_dict)
    assert test_vals in j2_vars


# Generated at 2022-06-13 15:39:07.215440
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.parsing.vault import VaultLib
    from ansible.template import Templar
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    templar = Templar(None, vault_secrets=[])

    # test with valid hostvars
    globals = dict(hostvars=dict(host1=dict(foo=dict(bar='baz'))))
    assert 'hostvars' in AnsibleJ2Vars(templar, globals, locals={})
    assert 'hostvars.host1' in AnsibleJ2Vars(templar, globals, locals={})
    assert 'hostvars.host1.foo' in AnsibleJ2Vars(templar, globals, locals={})
    assert 'hostvars.host1.foo.bar' in Ansible

# Generated at 2022-06-13 15:39:08.725734
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    pass

# Generated at 2022-06-13 15:39:19.163584
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar

    templar = Templar(loader=None)

    # test normal values
    j2vars = AnsibleJ2Vars(templar, globals={'a': 1, 'b': 2, 'c': 3}, locals=None)
    assert 'a' in j2vars
    assert 'b' in j2vars
    assert 'c' in j2vars
    assert 'd' not in j2vars

    # test values with string keys
    j2vars = AnsibleJ2Vars(templar, globals={'a': 1, 'b': 2, 'c': 3}, locals={'a': 'str', 'd': 4})
    assert 'a' in j2vars
    assert 'b' in j2vars
    assert 'c' in j2

# Generated at 2022-06-13 15:39:20.741193
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    assert isinstance(AnsibleJ2Vars, object)


# Generated at 2022-06-13 15:39:28.388091
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.set_loader(loader)
    templar = Templar(loader=loader, variables=variable_manager)

    variables = AnsibleJ2Vars(templar, None)
    print(variables)
    # print(variables.__getitem__('ansible_version'))
    # print(variables.__getitem__('env'))

if __name__ == '__main__':
    test_AnsibleJ2Vars___getitem__()

# Generated at 2022-06-13 15:39:40.140343
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars

    available_variables = {
        'a': '',
        'b': '',
    }
    templar = Templar(loader=None, variables=available_variables)
    globals = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': [1, 2, 3],
    }

    # Test __getitem__
    ansible_j2_vars = AnsibleJ2Vars(templar, globals)
    assert ansible_j2_vars['a'] == 1
    assert ansible_j2_vars['b'] == 2
    assert ansible_j2_vars['c'] == 3
    assert ans

# Generated at 2022-06-13 15:39:54.696025
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import os

    # set up testing dummy variable to play with
    test_vars = []
    test_vars.append({'variable': {'name': 'my_dummy_var', 'value': 'my_dummy_value'}})

    # initialize the templar class
    from ansible.template import Templar
    templar = Templar(loader=None, variables=test_vars)
    # initialize the globals
    globals_ = globals()
    # initialize the locals
    locals_ = locals()

    # initialize the AnsibleJ2Vars class
    ansible_j2vars = AnsibleJ2Vars(templar, globals_, locals_)

    # test if the method really works as expected

# Generated at 2022-06-13 15:40:00.067678
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    # set the test parameters
    templar = {}
    globals = {'hostvars':{'host':None}}
    locals = {}
    j2_vars = AnsibleJ2Vars(templar, globals, locals)

    # test if AnsibleJ2Vars behaves like a dict
    assert set(['hostvars']) == set(j2_vars)

# Generated at 2022-06-13 15:40:09.441199
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    '''
    This function tests that class AnsibleJ2Vars works as expected. 
    '''

    from ansible.plugins.loader import plugin_loader
    for p in plugin_loader.all():
        print(p)
    from ansible.template import Templar
    from ansible.playbook.play import Play
    from ansible.template.template import Templar
    from ansible.vars.hostvars import HostVars

    # Initialize some variables
    templar = Templar(loader=None)
    globals = dict()
    locals = dict()

    # Test class AnsibleJ2Vars with empty locals, empty globals and empty hostvars
    hostvars = HostVars(HostVars({}))
    templar._available_variables = {'vars': hostvars}
    ansible_

# Generated at 2022-06-13 15:40:21.566715
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar, TemplarException
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.template.safe_eval import ansible_safe_eval

    # Initialized with setting dict, dict of context vars, dict of global vars
    valid_variables = {'a': 'b'}
    aj2v = AnsibleJ2Vars(Templar(loader=None), locals=valid_variables)

    # Dict of valid variables
    valid_variables_dict = dict(a='b')

    # Testing 'a' in valid_variables
    assert 'a' in valid_variables
    assert 'a' in valid_variables_dict
    assert 'a' in a

# Generated at 2022-06-13 15:40:27.091814
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    templar = Templar()
    globals = dict(glob='glob')
    locals = dict(loc='loc')
    proxy = AnsibleJ2Vars(templar, globals, locals=locals)
    assert 'glob' in proxy
    assert 'loc' in proxy
    assert 'vars' in proxy


# Generated at 2022-06-13 15:40:36.798417
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    print('PHASE 1')
    globals={'a':2}
    locals={'b':3}

    templar = Templar({'a':1,'b':2,'c':3},globals=globals,locals=locals)
    j2vars = AnsibleJ2Vars(templar,globals,locals)

    print(j2vars['a'])
    print(j2vars['b'])
    print(j2vars['c'])
    print('PHASE 2')
    try:
        print(j2vars['d'])
    except KeyError as e:
        print('Catched expected exception: {0}'.format(e))



# Generated at 2022-06-13 15:40:45.647205
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    """
    JinjaVars object
    """
    import jinja2
    from ansible.vars import VariableManager
    from ansible.template import Templar

    params = dict(test="test", foo="foo")
    vm = VariableManager()
    vm.extra_vars = dict()
    vm.extra_vars.update(params)
    loader = jinja2.BaseLoader()
    env = jinja2.Environment(loader=loader, undefined=jinja2.StrictUndefined)
    templar = Templar(loader=loader, variables=vm, environment=env)
    globals = dict()
    locals = dict()
    AnsibleJ2Vars(templar, globals, locals)

# Generated at 2022-06-13 15:40:47.780341
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    class FakeTemplar():
        def __init__(self):
            self.available_variables = {}

        def template(self, variable):
            return variable

    var = AnsibleJ2Vars(FakeTemplar(), {}, locals={})
    assert var["vars"] == {}

# Generated at 2022-06-13 15:40:53.787328
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    # Set up variables
    key = 'key'
    value = 'value'

    # Set up mocks
    class mockAnsibleError(AnsibleError):
        pass
    mock_templar = mock.Mock()
    mock_globals = mock.Mock()
    type(mock_globals).__UNSAFE__ = mock.PropertyMock(return_value=False)
    type(mock_globals).__name__ = mock.PropertyMock(return_value=key)
    type(mock_globals).__class__ = mock.PropertyMock(return_value=mock_globals)
    type(mock_globals).copy = mock.Mock(return_value=mock_globals)

# Generated at 2022-06-13 15:40:58.759163
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.playbook.play_context import PlayContext
    from ansible.template.task_template import TaskTemplate
    templar = TaskTemplate(PlayContext())
    vars = AnsibleJ2Vars(templar, dict())
    assert len(vars) == 5


# Generated at 2022-06-13 15:41:15.640087
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    in_locals = {'a': 1}
    in_globals = {'b': 2}
    in_globals_2 = {'b': 2, 'c': 2}
    in_templar = {'a': 1, 'b': 2, 'c': 3}
    test_proxy_1 = AnsibleJ2Vars(in_templar, in_globals, in_locals)
    test_proxy_2 = AnsibleJ2Vars(in_templar, in_globals_2, in_locals)
    assert ('b' in test_proxy_1) == False
    assert ('a' in test_proxy_1) == True
    assert ('c' in test_proxy_2) == True
    assert ('c' in test_proxy_1) == True

# Generated at 2022-06-13 15:41:23.490043
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    try:
        from ansible.template import Templar
    except ImportError:
        raise unittest.SkipTest("jinja2 is not installed")

    vars_obj = AnsibleJ2Vars(
        templar = Templar(loader=None),
        globals = {},
        locals = {}
    )

    vars_obj._templar.available_variables = {
        'good_name' : 'good_value',
    }
    assert vars_obj['good_name'] == 'good_value'

    vars_obj._locals = {
        'good_name' : 'good_value',
    }
    assert vars_obj['good_name'] == 'good_value'


# Generated at 2022-06-13 15:41:34.821933
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.add_group_vars_file(loader, 'test/unit/ansible_module_meta/group_vars/all')
    variable_manager.add_host_vars_file(loader, 'test/unit/ansible_module_meta/group_vars/all')
    templar = Templar(loader=loader, variables=variable_manager)
    globals = {'my_global': 'my_global_value'}
    locals = {'my_local': 'my_local_value'}


# Generated at 2022-06-13 15:41:43.925035
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    class MockTemplar(object):
        def __init__(self):
            self._available_variables = {'v1': 'p1', 'v2': 'p2'}
        def template(self, variable):
            return self._available_variables[variable]
        @property
        def available_variables(self):
            return self._available_variables

    # test base case for available variables
    templar = MockTemplar()
    globals = {'g1': 'p1', 'g2': 'p2'}
    locals = {'l1': 'p1', 'l2': 'p2'}
    vars = AnsibleJ2Vars(templar, globals, locals=locals)
    assert 'v1' in vars

# Generated at 2022-06-13 15:41:55.823008
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    ansible_vars = {
        "vars": {
            "a": 1,
            "b": 2,
            "c":  {
                "d": 3,
                "e": 4
            }
        }
    }
    from ansible.template.safe_eval import ansible_safe_eval
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleUnicode
    templar = Templar(loader=None, variables=ansible_vars, shared_loader_obj=None)
    j2_vars_obj = AnsibleJ2Vars(templar, None, locals=None)

    assert(j2_vars_obj["vars"]["a"] == ansible_vars["vars"]["a"])

# Generated at 2022-06-13 15:42:04.299395
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.vars import VariableManager
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar

    variable_manager = VariableManager()
    vault_pass = None
    loader = DataLoader()
    templar = Templar(loader=loader, variables=variable_manager, vault_secrets=VaultLib(password_files=[vault_pass]))

    # Test1: varname is in _locals
    a = AnsibleJ2Vars(templar, {}, locals={'test_var': 'test_value'})
    assert 'test_var' in a

    # Test2: varname is in _templar.available_vars

# Generated at 2022-06-13 15:42:09.791375
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    # HACK
    # obtain a template which uses the AnsibleJ2Vars.__contains__ method
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    import os
    import tempfile
    loader = DataLoader()
    inv_manager = InventoryManager(loader=loader, sources='localhost,')
    distfact = DistributionFactCollector(loader=loader)
    variables = VariableManager()
    templar = Templar(loader=loader, variables=variables,
                      shared_loader_obj=None, template_class='J2Template')

    variables = VariableManager()

    # FIXME

# Generated at 2022-06-13 15:42:14.577260
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    # Init the templar object
    templar = Templar()

    # Init the globals object
    globals = {}

    # Init the locals object
    locals = {}

    # Init the j2vars object
    j2vars = AnsibleJ2Vars(templar, globals, locals)

    # Test with a known key
    j2vars['inventory_hostname'] = 'test_AnsibleJ2Vars___getitem__'

    # And ensure that the value have been stored in the Templar
    assert(templar.available_variables['inventory_hostname'] == 'test_AnsibleJ2Vars___getitem__')


# Generated at 2022-06-13 15:42:20.950466
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    test_templar = Templar()

    test_globals = {'test_global': 'global', 'test_global2': 'global2'}
    test_locals = {'test_local': 'local', 'test_local2': 'local2'}
    test_vars = {'test_var': 'var', 'test_var2': 'var2'}

    test_obj = AnsibleJ2Vars(test_templar, test_globals, locals=test_locals)
    test_obj._templar.available_variables = test_vars

    assert 'test_global' in test_obj
    assert 'test_global2' in test_obj
    assert 'test_local' in test_obj
    assert 'test_local2' in test

# Generated at 2022-06-13 15:42:28.535143
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    from ansible.module_utils.six import PY2
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars

    templar = Templar(loader=None)
    test_host_vars = HostVars(hostname='test_host', variables=dict(a=1, b=2))
    test_host_vars.set_variable('c', 3)
    templar._available_variables = {
        'hostvars': test_host_vars,
        'vars': test_host_vars,
        'groups': {
            'host_group': [
                'test_host'
            ]
        }
    }
    globals = {
        'a': 1,
    }

    # No locals
    vars = AnsibleJ2

# Generated at 2022-06-13 15:42:45.305387
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    class MockedTemplar(object):
        def __init__(self, available_variables):
            self.available_variables = available_variables

    globals = {'g1': 'gloabal1', 'g2': 'gloabal2'}
    locals = {'l1': 'local1', 'l2': 'local2'}
    templar = MockedTemplar({'v1': 'variable1', 'v2': 'variable2'})
    vars = AnsibleJ2Vars(templar, globals, locals)
    assert set(vars.__contains__('l1')) == True
    assert set(vars.__contains__('l2')) == True
    assert set(vars.__contains__('v1')) == True

# Generated at 2022-06-13 15:42:54.606478
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    def make_ansible_vars(d):
        return { k: AnsibleVars(v, AnsibleTemplar()) for (k, v) in iteritems(d) }
    def make_AnsibleJ2Vars(globals, locals=None):
        return AnsibleJ2Vars(AnsibleTemplar(), globals, locals)
    from ansible.vars.hostvars import HostVars
    hostvars = HostVars({ 'a': 'A' }, None)
    hostvars.__UNSAFE__ = True
    #
    templar = AnsibleJ2Vars(AnsibleTemplar(), {}, {})
    assert templar['template'] == templar._templar
    assert templar['environment'] == templar._templar.environment


# Generated at 2022-06-13 15:43:01.923575
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    # Arrange
    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib
    from ansible.plugins.loader import vars_loader

    templar = Templar(
        vault_password=VaultLib(),
        loader=None,
        variables={}
    )

    vars = AnsibleJ2Vars(templar={}, globals={}, locals={})

    # Act
    keys = set()
    keys.update(vars)

    # Assert
    assert len(keys) == 0


# Generated at 2022-06-13 15:43:08.639051
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    templar = None
    globals = dict()
    locals = dict()
    ajv = AnsibleJ2Vars(templar, globals, locals)
    assert 'any_key' in ajv == False
    globals = {'any_key': 'any_value'}
    locals = dict()
    ajv = AnsibleJ2Vars(templar, globals, locals)
    assert 'any_key' in ajv == True


# Generated at 2022-06-13 15:43:13.013883
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    import jinja2
    templar = Templar(loader=jinja2.DictLoader({}))
    globals = {}
    locals = {}
    j2vars = AnsibleJ2Vars(templar, globals, locals)

    globals['test'] = 'test'
    assert 'test' in globals

    assert 'test' in j2vars

    del globals['test']
    assert 'test' not in globals

    assert 'test' not in j2vars



# Generated at 2022-06-13 15:43:25.820420
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template.safe_eval import safe_eval
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.vars.unsafe_proxy import UnsafeProxy

    def _mock_unsafe_proxy(*args, **kwargs):
        return UnsafeProxy(object())

    import sys
    from ansible.playbook.play_context import PlayContext

    # AnsibleJ2Vars keyError exception handler
    def key_error_handler(exception):
        if exception.message == 'undefined variable: undefined':
            print("AnsibleJ2Vars.__getitem__('undefined'): [PASS]")

# Generated at 2022-06-13 15:43:36.583873
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    import sys
    import types
    import unittest

    sys.modules['ansible'] = types.ModuleType('ansible')
    sys.modules['ansible.errors'] = types.ModuleType('errors')
    sys.modules['ansible.vars'] = types.ModuleType('vars')
    sys.modules['ansible.vars.hostvars'] = types.ModuleType('hostvars')



    from ansible.errors import AnsibleError
    from ansible.module_utils._text import to_native
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.template import Templar


    class AnsibleJ2VarsTestCase(unittest.TestCase):
        def setUp(self):
            self.templar = Templar()
            self.ansible_j

# Generated at 2022-06-13 15:43:41.206384
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    templar = Templar(loader=None, variables={})
    j2vars = AnsibleJ2Vars(templar, {}, locals={})
    assert 'foo' in j2vars
    assert 'bar' not in j2vars


# Generated at 2022-06-13 15:43:49.308454
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import ansible.utils.unsafe_proxy
    from ansible.playbook.template import Templar
    from ansible.vars.hostvars import HostVars
    from ansible.vars.hostvars import HostVarsVarsModule
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    hostvars = HostVars(fake_host)
    hostvars.vars = hostvars_to_inject
    _vars = {
        'environment': 'production',
        'context': 'production',
        'template': 'production',
        'vars': hostvars,
        'inventory_hostname': 'fake_host',
        'inventory_hostname_short': 'fake_host'}
    globals = {}
    locals = {}

# Generated at 2022-06-13 15:43:53.202007
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    templar = None
    globals = {'J2Vars':42}
    localvars = {'foo': 'bar'}

    vars = AnsibleJ2Vars(templar, globals, localvars)
    assert vars.__contains__('J2Vars') == True
    assert vars.__contains__('foo') == True
    assert vars.__contains__('bar') == False

# Generated at 2022-06-13 15:44:09.013976
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    locals = {'a': 1, 'b': 2}
    globals = {'a': 1, 'b': 2, 'c': 3}
    templar = {}
    proxy = AnsibleJ2Vars(templar, globals, locals)
    assert len(proxy) == len(set(locals) | set(globals))


# Generated at 2022-06-13 15:44:16.796715
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    # Make a templar object
    pass
    # Make a dict for globals
    globals = dict([("gvar1", "value1"), ("gvar2", "value2")])
    # Make a dict for locals
    locals = dict([("lvar1", "value1"), ("lvar2", "value2")])
    # Make an AnsibleJ2Vars object with templar, globals, and locals
    vars = AnsibleJ2Vars(templar, globals, locals)
    # Test if __getitem__ gets the value from the locals dict
    assert vars.__getitem__("lvar1") == "value1"
    # Test if __getitem__ gets the value from the globals dict
    assert vars.__getitem__("gvar2") == "value2"
    # Test

# Generated at 2022-06-13 15:44:22.149053
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    templar = Templar(loader=None)
    globals = {'gvar': 1}
    locals = {'lvar': 2}
    vars = AnsibleJ2Vars(templar, globals, locals)
    assert('gvar' in vars)
    assert('lvar' in vars)
    # test undefined variable
    assert('undefined' not in vars)


# Generated at 2022-06-13 15:44:28.795839
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=["../../test/unit/ansible_module_meta/inventory"])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    inventory_vars = variable_manager.get_vars(host="host0")

    test_obj = AnsibleJ2Vars(variable_manager.extra_vars, inventory_vars)
    assert "fake_var" in test_obj
    assert "fake_var2" in test_obj
    assert "fake_dict_var" in test_obj


# Generated at 2022-06-13 15:44:37.253143
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.template import Templar
    templar = Templar(None, loader=None)

    test_j2vars = AnsibleJ2Vars(templar, {
        "var_global": "var_global",
        "var_global2": "var_global2"
    }, {
        "var_local": "var_local",
        "var_local2": "var_local2"
    })

    assert len(test_j2vars) == 4


# Generated at 2022-06-13 15:44:42.662071
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    m_templar = AnsibleJ2Vars(templar=dict(), globals=dict(), locals=dict())
    vars = AnsibleJ2Vars(templar=m_templar, globals=dict(), locals=dict(a=1, b=2))

    assert 'a' in vars
    assert 'b' in vars
    assert 'c' not in vars


# Generated at 2022-06-13 15:44:51.701480
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template.safe_eval import safe_eval

    templar = safe_eval.Streamer()
    globals = SafeDict({
        'var_from_globals': 'I am variable from globals',
    })
    locals = SafeDict({
        'var_from_locals': 'I am variable from locals',
        'l_var_from_locals': 'I am also variable from locals',
    })

    vars = AnsibleJ2Vars(templar, globals, locals)

    assert vars['var_from_locals'] == 'I am variable from locals'
    assert vars['l_var_from_locals'] == 'I am also variable from locals'
    assert vars['var_from_globals'] == 'I am variable from globals'
    assert vars

# Generated at 2022-06-13 15:45:04.098195
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.parsing.ajson import AnsibleJSONEncoder
    import json
    import os
    import jinja2

    env = jinja2.Environment(extensions=['jinja2.ext.do'])
    templar = AnsibleJSONEncoder()

    # inputs
    hostvars = {'foo': 'baz'}
    variable = '{{ foo }}'
    varname = 'variable'
    globals = {
        'hostvars': hostvars,
        'vars': variable,
        'varname': varname,
        'raw_var': variable,
        'var': 'neverseen',
    }

    # expected
    contained = {
        'var': False,
        'vars': True,
    }

    # testing object
    jvars = Ans

# Generated at 2022-06-13 15:45:11.636298
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    sut = AnsibleJ2Vars(Templar(), dict(), dict())
    sut._locals = {'key_locals': 'value_locals'}
    sut._templar.available_variables = {'key_templar': 'value_templar'}
    sut._globals = {'key_globals': 'value_globals'}

    assert 'key_locals' in sut
    assert 'key_templar' in sut
    assert 'key_globals' in sut
    assert 'not_in_any_dict' not in sut

    # 'has_key' is the name used by jinja2 to check if a

# Generated at 2022-06-13 15:45:20.499796
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template.safe_eval import safe_eval, compile_and_eval
    from ansible.template.template import Templar

    def recursive_contains(seq, value):
        # https://stackoverflow.com/a/50484165/194586
        if value in seq:
            return True
        if isinstance(seq, dict):
            wrapped_seq = seq.values()
        else:
            wrapped_seq = seq
        for item in wrapped_seq:
            if recursive_contains(item, value):
                return True
        return False

    def recursive_isinstance(seq, type):
        if isinstance(seq, type):
            return True
        if isinstance(seq, dict):
            wrapped_seq = seq.values()
        else:
            wrapped_seq = seq

# Generated at 2022-06-13 15:45:45.203066
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.errors import AnsibleUndefinedVariable
    from ansible.template import Templar


# Generated at 2022-06-13 15:45:53.659106
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.vars import VariableManager
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    variable_manager.extra_vars = {'dict': {'key': 'value'}}
    loader = DataLoader()
    templar = Templar(loader=loader, variables=variable_manager)

    ansible_j2_vars = AnsibleJ2Vars(templar, {'item': 'value'})
    assert 'dict' in ansible_j2_vars
    assert ansible_j2_vars['dict'] == {'key': 'value'}
    assert ansible_j2_vars['item'] == 'value'
    assert len(ansible_j2_vars) == 2

# Generated at 2022-06-13 15:45:54.556084
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    i = AnsibleJ2Vars(1,2,3)

# Generated at 2022-06-13 15:46:01.716122
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    templar = None
    globals = None
    locals = None

    try:
        obj = AnsibleJ2Vars(templar, globals, locals)
    except Exception as e:
        if e.args[0] != 'templar must be of type: Templar':
            raise
    else:
        raise

    try:
        obj = AnsibleJ2Vars(None, globals, locals)
    except Exception as e:
        if e.args[0] != 'templar must be of type: Templar':
            raise
    else:
        raise

# Generated at 2022-06-13 15:46:13.167395
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    _loader = DataLoader()
    _variable_manager = VariableManager()
    hosts = ['localhost']
    vars_map = {u'foo': u'bar', u'baz': u'qux'}
    _host = HostVars(hostname='localhost', variables=vars_map)  # type: HostVars
    _variable_manager.set_host_variable(host=hosts[0], varname='vars', value=_host)

# Generated at 2022-06-13 15:46:23.011876
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.template import Templar
    templar = Templar()
    globals = dict()
    locals = dict()

    a = AnsibleJ2Vars(templar, globals, locals)
    # __len__() returns 0's when there is no variables
    assert len(a) == 0

    globals['a'] = 1
    a = AnsibleJ2Vars(templar, globals, locals)
    # __len__() returns 1 when there is one variables
    assert len(a) == 1

    globals['b'] = 2
    a = AnsibleJ2Vars(templar, globals, locals)
    # __len__() returns 2 when there are two variables
    assert len(a) == 2

    globals['b'] = 3

# Generated at 2022-06-13 15:46:33.748596
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.vars import VariableManager
    from ansible.template import Templar

    variable_manager = VariableManager()
    variable_manager.set_host_variable('localhost', 'localhost')
    variable_manager._extra_vars = {'host_with_underscores': 'a_host_with_underscores',
                                    'host': 'a_host',
                                    'host_with_vars': {'name': 'a_host_with_vars'},
                                    'hostvars': {'host_nested_in_hostvars': 'a_host_nested_in_hostvars'}}
    templar = Templar(loader=None, variables=variable_manager)

    a = AnsibleJ2Vars(templar, {}, locals={'l_var': 'local_var'})



# Generated at 2022-06-13 15:46:42.509210
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.vars.hostvars import HostVars

    from io import BytesIO
    from jinja2 import Environment, FileSystemLoader
    from ansible.utils.unsafe_proxy import wrap_var

    example_file = b'example file content'

    templar = Templar(loader=FileSystemLoader('.'), variables={}, tqm=None)
    datas = AnsibleJ2Vars(templar, { 'hostvars': {} })

    # Test variable as file and variable as safe str
    data = { 'example_variable_1': 'example variable value 1',
             'example_variable_2': 'example variable value 2',
    }

# Generated at 2022-06-13 15:46:51.747634
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    templar = Templar(loader=None)
    # once again simulate a global variable
    AnsibleJ2Vars.DEFAULT_UNDEFINED_VAR_BEHAVIOR = 'strict'
    # initialize a j2vars object, with globals set and templar object
    j2vars = AnsibleJ2Vars(templar, globals, locals=locals)
    # simulate a host variable, with a safe value
    templar.available_variables = {
        'hostvar': 'foo'
    }
    # test the output of this host variable
    assert j2vars['hostvar'] == 'foo'
    # simulate a host variable, with an unsafe value

# Generated at 2022-06-13 15:47:00.571784
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    templar = Templar(loader=None)
    assert templar
    templar.basedir = '/tmp'
    var_name='my_var'
    my_var='hello world'
    templar.set_available_variables({var_name: my_var})
    ajv = AnsibleJ2Vars(templar, {}, locals({var_name: my_var}))
    assert ajv
    assert ajv[var_name] == my_var

# Make sure all methods are covered by unit tests

# Generated at 2022-06-13 15:47:25.436262
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar

    def _getitem_test_init(self):
        self.available_variables = dict()
        self.available_variables['foo'] = 'bar'

        self.template_data = dict()

    def _getitem_test_template(self, data):
        from ansible.template.safe_eval import safe_eval
        if isinstance(data, dict):
            return data
        elif isinstance(data, basestring) and data.startswith('$eval '):
            return safe_eval(data[6:])
        else:
            return data

    templar = Templar(loader=None)
    templar.loader = None
    templar.available_variables = dict()
    templar.template = _getitem_test_template
    templar

# Generated at 2022-06-13 15:47:33.725079
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    '''
    Tests that AnsibleJ2Vars.__getitem__ returns the expected values and raises
    the expected exceptions.
    '''

    # Test scenarios:
    #
    # Variable exists and is a dictionary
    # Variable exists and is an ansible.vars.hostvars.HostVars instance

    from ansible.vars.hostvars import HostVars
    from ansible.template import Templar

    templar = Templar(loader=None)
    locals = dict()
    hostvars = HostVars({})

    j2vars = AnsibleJ2Vars(templar, globals=dict(), locals=locals)

    # Test variable exists and is a dictionary
    vars = dict()
    vars['ansible_python_interpreter'] = '/usr/bin/python'
    templ

# Generated at 2022-06-13 15:47:37.422361
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    """
    Tests that AnsibleJ2Vars correctly fetches variables and correctly raises
    KeyError on undefined variable.
    """
    t = Templar()
    v = AnsibleJ2Vars(t, {}, locals={'test': 'value'})

    assert 'test' in v
    assert v['test'] == 'value'

    try:
        v['nosuch']
        assert False
    except KeyError:
        pass # expected

# vim: set sts=4 sw=4 et :

# Generated at 2022-06-13 15:47:44.037447
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    import pytest
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext

    loader = DataLoader()
    var_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources='localhost')
    host = inventory.get_host('localhost')
    var_manager.add_host_vars(host, dict(test_var="test"))
    play_context = PlayContext()
    templar = Templar(var_manager, loader)

    # test with a basic setup
    ansible_j2_vars = AnsibleJ2Vars(templar, dict())
    # test we have an iterator

# Generated at 2022-06-13 15:47:48.547211
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    ansible_j2_vars = AnsibleJ2Vars(templar=None, globals={}, locals=None)
    assert iter(ansible_j2_vars) is not None, "Expected iter(ansible_j2_vars) is not None, but got None"


# Generated at 2022-06-13 15:47:57.450558
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    class TestClass:
        def __init__(self):
            self._templar = Templar()
            self._globals = dict()

    def func(a,b):
        return str(a) + str(b)


# Generated at 2022-06-13 15:48:05.507921
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    import ansible.template
    import ansible.vars
    import ansible.inventory

    # Create templar
    templar = ansible.template.Templar(loader=None)

    # Create host
    host = ansible.inventory.Host('localhost')
    host.vars = {}

    # Create variables
    variables = ansible.vars.VariableManager(loader=None, inventory=None)
    variables.set_host_variable(host, 'var1', 'var1')

    # Create globals
    globals = {}

    # Create locals
    locals = {}

    # Create AnsibleJ2Vars instance
    variables_proxy = AnsibleJ2Vars(templar, globals, locals)
    # Test implement of getitem of class AnsibleJ2Vars
    value = variables_proxy.__

# Generated at 2022-06-13 15:48:16.790206
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    from ansible.template import Templar

    templar = Templar(loader=None, variables={'hello': 'world'})
    vars = { 'foo': 'bar' }
    a = AnsibleJ2Vars(templar, vars)
    assert len(a) == 2
    assert a['hello'] == 'world'
    assert a['foo'] == 'bar'
    assert set(a.keys()) == set(['foo', 'hello'])
    assert set(a.values()) == set(['bar', 'world'])
    assert set(a.items()) == set([('foo', 'bar'), ('hello', 'world')])
    assert {'hello': 'world', 'foo': 'bar'} == dict(a)
    assert 'foo' in a
    assert 'hello' in a
    assert 'foobar'

# Generated at 2022-06-13 15:48:27.258356
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template.safe_eval import safe_eval

    from ansible.vars.hostvars import HostVars
    from ansible.vars import VariableManager

    variable_manager = VariableManager()
    variable_manager.extra_vars = {"test_item": "asd"}
    variable_manager.host_vars = HostVars(dict(host1={"host1_item": "host1_value"},
                                              host2={"host2_item": "host2_value"}))

    t = safe_eval.Templar(loader=None,
                         variables=variable_manager.get_vars(play=None, host=None))

    var_proxy = AnsibleJ2Vars(t, t.available_variables)

    assert "test_item" in var_proxy