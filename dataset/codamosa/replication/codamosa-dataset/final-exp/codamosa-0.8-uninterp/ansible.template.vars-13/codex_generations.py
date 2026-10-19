

# Generated at 2022-06-13 15:38:41.883462
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    local_dict = {
        'v1': 'value 1',
        'v2': [ 'value', '2' ],
        'v3': { 'key1': 'value', 'key2': 3 }
    }
    for var in local_dict:
        assert var in AnsibleJ2Vars(None, None, locals=local_dict)
    assert 'unexistant_var' not in AnsibleJ2Vars(None, None, locals=local_dict)


# Generated at 2022-06-13 15:38:51.582029
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():

    import ansible.playbook
    import ansible.playbook.play
    from ansible.template import Templar
    from ansible.utils.vars import combine_vars

    host_obj = ansible.playbook.host.Host(name='fake_host')
    templar = Templar(loader=None, variables=combine_vars(host_obj.get_vars(), vars=dict(foo='bar')))
    assert isinstance(templar, Templar)

    vars = AnsibleJ2Vars(templar, globals=dict(test_global='test_global'))
    assert isinstance(vars, AnsibleJ2Vars)

    assert (vars.__contains__('foo'))
    assert (vars.__contains__('test_global'))

# Generated at 2022-06-13 15:39:01.498126
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    # Setup test environment
    from ansible.template import Templar
    import os, tempfile, shutil
    tmp_dir = tempfile.mkdtemp()
    the_vars = {
            'foo': 'bar',
            'the_nest': {
                'title': 'the_nest',
                'nested_var1': 'one'
                },
            'list_var': ['one', 'two', 'three'],
            'l_local_var': 'l_local_var_value'
            }
    the_globals = {
            'g_global_var': 'g_global_var_value'
            }

    # Create the object
    test_templar = Templar(loader=None, variables=the_vars)

# Generated at 2022-06-13 15:39:06.940759
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.template import Templar
    templar = Templar(loader=None, variables={})
    globals = {}
    locals = {}
    ansible_j2_vars = AnsibleJ2Vars(templar, globals, locals)
    assert len(ansible_j2_vars) == 0
    variables = {'a': 'b'}
    globals = {'b': 'c'}
    locals = {'c': 'd', 'd': 'e'}
    ansible_j2_vars = AnsibleJ2Vars(templar, globals, locals)
    assert len(ansible_j2_vars) == 4


# Generated at 2022-06-13 15:39:14.294944
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    class TemplarMock:
        def __init__(self, available_variables):
            self.available_variables = available_variables

        def template(self, variable):
            return variable

    j2vars = AnsibleJ2Vars(TemplarMock({"var1": "value1"}), {}, {"l_var2": "value2"})
    assert len(j2vars) == 2


# Generated at 2022-06-13 15:39:23.075374
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.templating import Templar
    templar = Templar(loader=None)

    # Missing variable in _templar.available_variables
    with pytest.raises(KeyError) as err:
        assert AnsibleJ2Vars(templar, {}).__getitem__('test')
    assert err.value.args[0] == "undefined variable: test"

    # Missing variable in _templar.available_variables, but in _globals
    assert AnsibleJ2Vars(templar, {'test': 'value'}).__getitem__('test') == 'value'

    # Missing variable in _templar.available_variables, but in _locals
    assert AnsibleJ2Vars(templar, {}, locals={'test': 'value'}).__get

# Generated at 2022-06-13 15:39:29.172078
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    tmp = dict()
    tmp['key1'] = 1
    tmp['key2'] = 2
    tmp['key3'] = 3
    tmp['key4'] = 4
    tmp['key5'] = 5

    tmp2 = dict()
    tmp2['key21'] = 'value21'
    tmp2['key22'] = 'value22'
    tmp2['key23'] = 'value23'
    tmp2['key24'] = 'value24'
    tmp2['key25'] = 'value25'

    vars_test = AnsibleJ2Vars('', tmp2)
    vars_test.add_locals(tmp)

    assert len(vars_test) == 10

# Generated at 2022-06-13 15:39:40.804787
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    # Use fixture to setup testing component
    # Call function under test
    # Use assertion to validate code function
    from  ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    yaml_data = """
    - hosts: all
      tasks:
        - debug:
            msg: 'hello world!'
    """

    loader = DataLoader()
    vars_manager = VariableManager()
    dummy_inventory = dict()
    path = './tests/utils/'

    with open(path + 'hosts', 'r') as f:
        host_list = f.readlines()

# Generated at 2022-06-13 15:39:51.846737
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    templar = Templar(loader=DataLoader(), variables=VariableManager())

    # Test case 1: varname in self._locals
    vars_obj = AnsibleJ2Vars(templar, {"gvar": "global_value"}, locals={"lvar": "local_value"})
    assert vars_obj["lvar"] == "local_value"

    # Test case 2: varname in self._templar.available_variables
    vars_obj = AnsibleJ2Vars(templar, {"gvar": "global_value"}, locals={"lvar": "local_value"})

# Generated at 2022-06-13 15:39:55.949401
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    var_proxy = AnsibleJ2Vars({}, {}, locals={'l_a': 10, 'context': 'context'})
    assert 'a' in var_proxy
    assert var_proxy['a'] == 10
    assert 'context' not in var_proxy
    assert 'b' not in var_proxy

# Generated at 2022-06-13 15:40:09.077817
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.template import Templar
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.vars.hostvars import HostVars

    templar = Templar(loader=None)
    globals = {'g_hostname': 'testhost'}
    locals = {'l_hostname': 'testhost'}
    vars_proxy = AnsibleJ2Vars(templar, globals, locals)

    # check that __contains__ work correctly
    assert 'g_hostname' in vars_proxy
    assert 'l_hostname' in vars_proxy
    assert 'hostname' in vars_proxy

    # check that __contains__ raise an exception


# Generated at 2022-06-13 15:40:21.364402
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.utils.vars import combine_vars

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['/dev/null'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    play_context = PlayContext()
    templar = Templar(loader=loader, variables=variable_manager,
                      shared_loader_obj=inventory, play_context=play_context)

    globals = {'test_name': 'value'}


# Generated at 2022-06-13 15:40:32.549047
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar
    variable_manager = VariableManager()

# Generated at 2022-06-13 15:40:36.558713
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    test_dict = dict()
    test_dict['test_variable'] = 'test_value'
    test_templar = AnsibleJ2Vars('', test_dict)
    assert('test_variable' in test_templar)
    assert('test_variable' not in test_templar)

# Generated at 2022-06-13 15:40:46.454068
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template.safe_eval import unsafe_eval
    from ansible.parsing.metadata import MetadataParser
    from ansible.template import Templar
    from ansible.vars import VariableManager

    from jinja2 import DictLoader
    from jinja2 import Environment

    j2vars = AnsibleJ2Vars(
        Templar(
            Environment(
                loader=DictLoader({}),
                undefined=AnsibleUndefinedVariable
            ),
            variable_manager=VariableManager(),
            loader=None,
            shared_loader_obj=None
        ),
        {}
    )

    # Testing KeyError Exception
    # -------------------------------------------
    try:
        j2vars['unknowkey']
    except KeyError as e:
        assert "undefined variable" in str(e)

# Generated at 2022-06-13 15:40:52.921970
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    import sys
    import os
    import unittest

    sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../lib'))
    from ansible.parsing.vault import VaultLib
    from ansible.template import Templar
    from ansible.plugins.loader import vars_loader

    vault = VaultLib('fakepass')
    templar = Templar(loader=vars_loader)

    # test without _globals
    globals = None
    locals = dict()
    ajv = AnsibleJ2Vars(templar, globals, locals)
    assert 'foo' not in ajv

    # test with _globals but no values
    globals = dict()
    locals = dict()

# Generated at 2022-06-13 15:41:04.067198
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    import sys
    import types

    def testme(result, locals_=None):
        j2vars = AnsibleJ2Vars(templar, globals_, locals_)
        return varname in j2vars

    # vars and globals first, then locals
    vars = dict(a=1)
    globals_ = dict(a=10)
    locals_ = dict(b=100)

    templar = Templar(loader=None, variables=vars)

    varname = 'a'
    assert testme(True)

    varname = 'b'
    assert testme(True)

    varname = 'c'
    assert testme(False)

    # locals shadow globals, then vars

# Generated at 2022-06-13 15:41:08.649412
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    from ansible.template import Templar

    # Creating new template
    template = Templar(loader=None, variables={'some_var': 'test'})

    # Creating new AnsibleJ2Vars
    AnsibleJ2Vars = AnsibleJ2Vars(template, {})

    assert 'some_var' in AnsibleJ2Vars



# Generated at 2022-06-13 15:41:18.558167
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    test_AnsibleJ2Vars__SomeLocal = dict (SomeLocal = "SomeValue")
    test_AnsibleJ2Vars__SomeGlobal = dict (SomeGlobal = "SomeValue")

    test_AnsibleJ2Vars__mapping = AnsibleJ2Vars(
        templar=None,
        globals=test_AnsibleJ2Vars__SomeGlobal,
        locals=test_AnsibleJ2Vars__SomeLocal)

    assert len(test_AnsibleJ2Vars__mapping) == 2
    assert 'SomeLocal' in test_AnsibleJ2Vars__mapping
    assert 'SomeGlobal' in test_AnsibleJ2Vars__mapping


# Generated at 2022-06-13 15:41:24.861423
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    try:
        from ansible.vars import BaseVars
        from ansible.template import Templar
        from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    except ImportError:
        return

    base_vars = BaseVars()
    base_vars.add_host_vars_from_inventory(None)
    templar = Templar(loader=None, variables=base_vars)

    glb = {'ansible_version': AnsibleUnsafeText('2.4.2.0')}

    vars = AnsibleJ2Vars(templar, glb)

    assert 'ansible_version' in vars
    assert 'my_var' not in vars
    assert len(vars) == 1

# Generated at 2022-06-13 15:41:38.654351
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template.safe_eval import safe_eval
    import ansible.template.template as template
    from ansible.vars.hostvars import HostVars
    vars = HostVars(dict(k1=1))
    templar = template.AnsibleTemplar(loader=None, variables=dict(v1=vars))
    AnsibleJ2Vars(templar, dict(g1=''), locals=dict(l1=''))['v1'] == vars
    AnsibleJ2Vars(templar, dict(g1=''), locals=dict(l1=''))['vars'] == dict(k1=1)
    AnsibleJ2Vars(templar, dict(g1=''), locals=dict(l1=''))['g1'] == ''


# Generated at 2022-06-13 15:41:46.436911
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader

    # Setup
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader, variable_manager, '')
    variable_manager.set_inventory(inventory)
    hosts = inventory.get_groups_dict().keys()
    variable_manager.set_host_variable(hosts, 'Groups', inventory.get_groups_dict())
    variable_manager.set_host_variable(hosts, 'Hosts', inventory.get_hosts())
    variable_manager.extra_vars = {'foo': 'bar'}
    templar = Templar(loader, variable_manager, None)
    globals = {}

# Generated at 2022-06-13 15:41:57.769866
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars

    templar = Templar()
    globals = {'logic_boolean': False, 'logic_non_boolean': 1}
    ansible_vars = {'logic_boolean': False, 'logic_non_boolean': 1}
    locals = {"logic_boolean": False, 'logic_non_boolean': 1}
    # len(set(globals) + set(ansible_vars) + set(locals))
    assert len(AnsibleJ2Vars(templar, globals, locals=locals)) == 6



# Generated at 2022-06-13 15:42:05.561743
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    templar = Templar(variables={'hostvars': {'host1': "host1", 'host2': "host2"}})
    globals = {'inventory_hostname': 'host1'}
    locals = {'inventory_hostname': 'host2'}
    vars=AnsibleJ2Vars(templar, globals, locals)

    assert 'inventory_hostname' in vars
    assert 'hostvars' in vars
    assert 'foo' not in vars


# Generated at 2022-06-13 15:42:14.301199
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    import ansible.utils.unsafe_proxy
    import ansible.vars.hostvars

    class Templar(object):
        END_MARKER = object()

        def __init__(self, variables):
            self.available_variables = variables
            self.template_ds = None
            self.environment = None

        def template(self, value):
            return value

    names = ('foo', 'bar', 'baz')
    values = (2, 3, 4)
    variables = dict(zip(names, values))
    hostvars = ansible.vars.hostvars.HostVars(variables, per_host=True)
    variables[ansible.utils.unsafe_proxy.UnsafeProxy] = hostvars

    templar = Templar(variables)


# Generated at 2022-06-13 15:42:20.744739
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars

    hostvars = HostVars(loader=None, variables=dict(), group_vars=dict(), host_specific_var_files=[])
    templar = Templar(loader=None, variables=dict(), shared_loader_obj=None)
    globals = {'a': 1, 'b': 2}
    ansible_vars = AnsibleJ2Vars(templar, globals, locals={'c': 3})

    assert 'a' in ansible_vars
    assert 'b' in ansible_vars
    assert 'c' in ansible_vars
    assert 'd' not in ansible_vars
    assert 'a' not in ansible_vars

    # try with templar
   

# Generated at 2022-06-13 15:42:24.864082
# Unit test for constructor of class AnsibleJ2Vars
def test_AnsibleJ2Vars():
    item = AnsibleJ2Vars("templar", "globals", locals="locals")
    assert item._templar == "templar"
    assert item._globals == "globals"
    assert item._locals == "locals"


# Generated at 2022-06-13 15:42:34.425267
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template.safe_eval import safe_eval, expression
    from ansible.template.templar import Templar

    templar = Templar(loader=None, variables={'ansible_host': 'host1'})
    globals = []
    locals = {'a': 'a'}
    aj2v = AnsibleJ2Vars(templar, globals, locals)
    # test with a variable that exists in aj2v and returns a plain string
    assert aj2v['a'] == 'a'
    # test with a variable that exists in aj2v and returns a python expression
    test_expression = safe_eval(expression(templar, '{{ (ansible_host == "host1") }}'))
    assert aj2v['ansible_host'] == test_expression
    # test

# Generated at 2022-06-13 15:42:45.902870
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.parsing.vault import VaultLib
    from ansible.vars.manager import VariableManager

    vault_password = '$ANSIBLE_VAULT;1.1;AES256\n34393537353261623764633630663665376332613030306335623465326330313831323039653665\n3438653366323231666563393162636531653262333531653132393132326163343133353434373965\n373332626130323065333736653637613065393934\n'
    vault = VaultLib([])
    unvaulted_data = vault.decrypt(vault_password)

# Generated at 2022-06-13 15:42:53.502398
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar

    template_uid = 'fadf7421-79fa-46d6-8658-6565e6ab3e3b'

    templar = Templar(loader=None, variables={}, shared_loader_obj=None,
                      inject=None, fail_on_undefined=True, disable_lookups=False,
                      final_only=False, disable_template=False, fail_on_template=False,
                      template_uid=template_uid, template_path=None)

    assert 'test' not in AnsibleJ2Vars(templar, globals={})

    assert 'test' not in AnsibleJ2Vars(templar, globals={}, locals={})


# Generated at 2022-06-13 15:43:07.155440
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.vars.unsafe_proxy import wrap_var
    import jinja2
    test_data = dict()
    test_data['vars'] = dict()
    test_data['vars']['test_var'] = 'bar'
    test_data['vars']['foo'] = 'baz'
    test_data['vars']['ansible_connection'] = 'baz'
    test_data['vars']['ansible_host'] = 'baz'
    test_data['host_self'] = dict()
    test_data['host_self']['ansible_module_name'] = 'win_ping'
    test_data['host_self']['ansible_winrm_transport'] = 'winrm'

# Generated at 2022-06-13 15:43:14.199423
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    '''
    Test __len__ Mapping method of AnsibleJ2Vars class.
    '''
    import jinja2
    from ansible.template import Templar

    locals_ = { 'foo': 'bar' }
    globals_ = { 'baz': 'qux' }
    variables = { 'foo': 'bar' }
    vars_ = AnsibleJ2Vars(Templar(loader=jinja2.DictLoader()), globals_, locals_)

    # len(vars_) should return len(globals_) + len(variables)
    assert len(vars_) == 3, "Expected 3, got %d" % len(vars_)


# Generated at 2022-06-13 15:43:26.560572
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar
    templar = Templar(None)
    # The item is in self._locals
    assert AnsibleJ2Vars(templar, {}, {'key': 'value'})['key'] == 'value'
    # The item is in self._templar.available_variables
    assert AnsibleJ2Vars(templar, {}, {'key': 'value'})._templar.available_variables['key'] is 'value'
    # The item is in self._globals
    assert AnsibleJ2Vars(templar, {'key': 'value'}, {})['key'] == 'value'
    # Throw AnsibleUndefinedVariable

# Generated at 2022-06-13 15:43:37.800507
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    # create jinja2 variables
    host_vars = HostVars(ansible_host="localhost")
    available_variables = dict(host_vars=host_vars)

    # create templar
    templar = Templar(loader=DictDataLoader(dict(vars=dict(a="a", b="b"))))

    # create locals
    locals = dict(i="1", j="2", k="3", h="h", host_vars="host_vars")

    # create AnsibleJ2Vars instance
    ajv = AnsibleJ2Vars(templar, dict(globals="globals"), locals)

    import pytest
    from ansible.vars.hostvars import HostVars

# Generated at 2022-06-13 15:43:39.466971
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    # TODO
    # Write unit tests to test AnsibleJ2Vars.__getitem__()
    pass

# Generated at 2022-06-13 15:43:46.671150
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    templar = None
    globals = {
        'a': 1,
        'b': 2,
    }
    locals = {
        'l_c': 3,
        'l_d': 4,
    }

    import itertools
    expected_keys = {'a', 'b', 'c', 'd'}

    actual_keys = set(itertools.chain(*[a for a in _AnsibleJ2Vars_test_instances(templar, globals, locals)]))

    assert expected_keys == actual_keys


# Generated at 2022-06-13 15:43:52.167344
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.plugins.loader import variable_manager
    from ansible.template import Templar
    from ansible.vars import hostvars
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import wrap_var

    vars = AnsibleJ2Vars(Templar(loader=None, variables=variable_manager), {})
    hostvars_dict = {'a': 'b', 'c': 'd'}
    hostvars_obj = HostVars(hostvars_dict, vault_password=None)
    wrapped_hostvars_obj = wrap_var(hostvars_obj)
    assert vars['vars'] == {}
    assert vars['hostvars']

# Generated at 2022-06-13 15:44:03.822703
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject

    # Simple interpolation
    templar = Templar(loader=None, variables={'foo': 1}, shared_loader_obj=None)
    j2vars = AnsibleJ2Vars(templar, {})
    assert j2vars['foo'] == 1

    # Simple type
    assert j2vars[None] is None
    assert j2vars[1] == 1
    assert j2vars['1'] == 1
    assert j2vars[1.0] == 1.0
    assert j2vars['1.0'] == 1.0
    assert j2

# Generated at 2022-06-13 15:44:14.492569
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    # create a local dict, to be used as `locals` in AnsibleJ2Vars()
    locals = {'l_key1': 'value1', 'l_key2': 'value2'}
    # create a dict to be used as `globals` in AnsibleJ2Vars()
    globals = {'key3': 'value3', 'key4': 'value4'}
    # create a dict representing a host, to be used as `templar.available_variables` in AnsibleJ2Vars()
    available_variables = {'key5': 'value5', 'key6': 'value6'}
    # create a templar object, to be used in AnsibleJ2Vars()

# Generated at 2022-06-13 15:44:23.846788
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variables = VariableManager()

    host = Host(name='foobar')
    variables.set_host_variable(host, 'foo', value='bar')

    templar = Templar(loader=loader, variables=variables)
    aj2v = AnsibleJ2Vars(templar, {}, {'l_foo': 'bar', 'l_foobar': 'baz'})

    assert 'foo' in aj2v
    assert 'foobar' in aj2v
    assert 'bar' not in aj2v
    assert 'baz' not in aj2v


# Generated at 2022-06-13 15:44:39.885508
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template.safe_eval import safe_eval
    from ansible.template.templar import Templar
    templar = Templar(loader=None, variables=dict())

    def test_AnsibleJ2Vars__valid_flag(flag):
        assert flag in AnsibleJ2Vars(templar, dict()) is True

    def test_AnsibleJ2Vars__invalid_flag(flag):
        assert flag in AnsibleJ2Vars(templar, dict()) is False

    test_AnsibleJ2Vars__valid_flag("ansible_default_ipv4")
    test_AnsibleJ2Vars__valid_flag("ansible_default_ipv4.address")

# Generated at 2022-06-13 15:44:51.245251
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.templating import Templar
    from ansible.template import TemplarContext
    from ansible.vars.hostvars import HostVars

    templar = Templar(variables=dict(a=dict(b='foo')))
    globals = dict(g='bar')

    instance = AnsibleJ2Vars(templar, globals)

    # test case 1: get a value defined in AnsibleJ2Vars
    assert instance['g'] == 'bar'

    # test case 2: get a value defined in Templar.available_variables
    assert instance['a'] == {'b': 'foo'}

    # test case 3: get a value defined in Templar.available_variables
    assert instance['a.b'] == 'foo'

    # test case 4: get a value that is a AnsibleVars.

# Generated at 2022-06-13 15:44:52.878875
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    print('##### test class AnsibleJ2Vars: def __iter__():')

    assert 0 == 9

# Generated at 2022-06-13 15:45:05.281180
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    import pytest
    templar = Templar(loader=None, variables={'a': 'b', 'c': 'd'})

    j2vars_instance = AnsibleJ2Vars(templar, {'ingredients': ['peanut butter', 'jelly', 'bread']}, locals={'l_ingredients': ['peanut butter', 'jelly', 'bread']})
    assert 'ingredients' in j2vars_instance
    assert 'a' in j2vars_instance
    assert 'l_ingredients' in j2vars_instance
    assert 'c' in j2vars_instance
    assert 'toast' not in j2vars_instance
    assert 'butter' not in j2vars_instance
    assert 'sandwich' not in j2vars_

# Generated at 2022-06-13 15:45:17.388276
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    from ansible.template import Templar
    templar = Templar(loader=None)
    globals=dict()
    j2vars = AnsibleJ2Vars(templar, globals)

    # available_variables should be initialized to an empty dictionary
    assert len(j2vars._templar.available_variables) == 0

    # False positive case
    with pytest.raises(KeyError) as excinfo:
        j2vars['key']
    assert "undefined variable" in str(excinfo.value)

    # Setting an existing variable
    j2vars._templar.available_variables['key'] = 'value'
    assert j2vars['key'] == 'value'

    # Setting an existing variable again
    j2vars._templar.available_variables['key']

# Generated at 2022-06-13 15:45:22.934895
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    j2vars = AnsibleJ2Vars('')
    print(hasattr(j2vars.__contains__, '__call__'))
    print(j2vars.__contains__('x'))
    print('x' in j2vars)
    j2vars.set_available_variables({'x': 't'})
    print(j2vars.__contains__('x'))
    print('x' in j2vars)

if __name__ == '__main__':
    test_AnsibleJ2Vars___contains__()

# Generated at 2022-06-13 15:45:34.905275
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template import Templar

    templar = Templar(None, loader=None)
    globals = {'foo': 'bar'}
    locals = {'baz': 'bam'}
    ansible_j2_vars = AnsibleJ2Vars(templar, globals.copy(), locals.copy())
    assert isinstance(ansible_j2_vars, Mapping)

    with pytest.raises(KeyError):
        ansible_j2_vars['qux']

    assert ansible_j2_vars['foo'] == globals['foo']
    assert ansible_j2_vars['baz'] == locals['baz']

    globals = {'foo': 'bar'}
    locals = {'baz': 'bam'}
    ansible_j2

# Generated at 2022-06-13 15:45:44.965370
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    import random
    import string
    import sys

    play_context = PlayContext()

    # Create a random variable name
    random_variable_name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(0, 10))

    # Load the system environment variables
    setup = sys.modules['ansible.module_utils.setup']
    setup.clear_fact_cache()
    system_environment_variables = setup.SystemEnvironment()

    # Create AnsibleJ2Vars object
    ansible_j2_vars = AnsibleJ2Vars(Templar(play_context), random_variable_name, system_environment_variables)

    # Test AnsibleJ2

# Generated at 2022-06-13 15:45:53.495504
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template.template import Templar

    templar = Templar(loader=None)
    globals = {"g_1": 1, "g_2": 2}
    locals = {"l_3": 3, "l_4": 4}
    vars = AnsibleJ2Vars(templar, globals, locals)
    test_vars = {"vars_1": 1, "vars_2": 2}
    templar.set_available_variables(test_vars)

    assert "g_1" in vars, "variable g_1 is not in the j2vars"
    assert "g_2" in vars, "variable g_2 is not in the j2vars"
    assert "l_3" in vars, "variable l_3 is not in the j2vars"

# Generated at 2022-06-13 15:46:03.458279
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.parsing.vault import VaultLib
    from ansible.template import Templar
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    vault_pass = 'secret'
    vault_text = VaultLib([], 1).encrypt(vault_pass, b'SECRET_TEXT')
    text = to_native(vault_text)
    variables = {
        'test_value': AnsibleUnsafeText(text),
        'test_dict': {
            'first_key': 'first_value',
            'second_key': 'second_value',
        }
    }
    templar = Templar(loader=None, variables=variables)
    globals = {}
    locals = {}

# Generated at 2022-06-13 15:46:21.583635
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    '''
    Unit test for method __contains__ of class AnsibleJ2Vars
    '''
    from ansible.playbook.play_context import PlayContext

    vars_list = [
        {'new_var1': 'new_value1', 'new_var2': 'new_value2', 'new_var3': 'new_value3'},
        {'new_var1': 'new_value1', 'new_var2': 'new_value2', 'new_var3': 'new_value3'},
        {'new_var1': 'new_value1', 'new_var2': 'new_value2', 'new_var3': 'new_value3'},
    ]

    templar = PlayContext()
    templar.set_available_variables(vars_list)


# Generated at 2022-06-13 15:46:32.986334
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():

    from ansible.parsing.vault import VaultLib
    from ansible.template import Templar

    vault = VaultLib()

    # simple
    def __check(varname, content, expected):
        templar = Templar(vault, loader=None, shared_loader_obj=None)
        ajv = AnsibleJ2Vars(templar, {}, locals=dict(varname=content))
        assert ajv['varname'] == expected

    # starts with dict
    def __check2(varname, content, expected):
        templar = Templar(vault, loader=None, shared_loader_obj=None)
        ajv = AnsibleJ2Vars(templar, {})
        ajv._templar.available_variables[varname] = content
       

# Generated at 2022-06-13 15:46:39.521496
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    templar = Templar(loader=None)
    globals = {'g_var': 'g_var_val'}
    locals_ = None
    vars = AnsibleJ2Vars(templar, globals, locals_)

    templar.available_variables = {'a_var': 'a_var_val'}
    assert 'g_var' in vars
    assert 'a_var' in vars
    assert 'a_var2' not in vars

    locals_ = {'l_var': 'l_var_val'}
    vars = AnsibleJ2Vars(templar, globals, locals_)

    templar.available_variables = {'a_var': 'a_var_val'}

# Generated at 2022-06-13 15:46:50.241841
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    # Create mock objects
    templar = None
    globals = dict(a=1, b=2, c=3)
    locals = dict(d=4, e=5)
    ansibleJ2Vars = AnsibleJ2Vars(templar, globals, locals)
    # Set up AnsibleUndefinedVariable exception object
    ansibleUndefinedVariable = AnsibleUndefinedVariable('exception object')
    # Set up error object
    error = Exception('Test Exception')
    # Set up expected result
    expectedResult1 = 1
    expectedResult2 = 3
    expectedResult3 = 5
    # Call AnsibleJ2Vars.__getitem__ method and check result
    assert(ansibleJ2Vars.__getitem__('a') == expectedResult1)

# Generated at 2022-06-13 15:46:53.414888
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template.safe_eval import safe_eval
    from ansible.template import Templar
    from ansible.plugins.loader import vars_loader
    templar = Templar(loader=None, variables={})
    # TODO


# Generated at 2022-06-13 15:47:01.082214
# Unit test for method __iter__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___iter__():
    from ansible.template import Templar
    v2 = AnsibleJ2Vars(Templar(), {}, {})

    # vars, hostvars and all in vars are accessible, so it should return all the keys of these three.
    keys_except_all = set(['vars', 'hostvars'])
    # keys of all in vars
    keys_all = set(['a', 'b', 'c'])

    assert v2.__iter__() == keys_except_all | keys_all


# Generated at 2022-06-13 15:47:08.999891
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play_context import PlayContext
    from ansible.template.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager, TaskQueueManagerOptions
    from ansible.plugins.strategy import StrategyBase
    from ansible.inventory.manager import InventoryManager

    # 1. Prepare inventory and variables
    loader = DataLoader()
    inv_source = '''
    [local]
    localhost ansible_connection=local'''
    inventories = InventoryManager(loader=loader, sources=[inv_source])
    variable_manager = VariableManager(loader=loader, inventory=inventories)
    variable_manager.set_inventory(inventories)
    variable_

# Generated at 2022-06-13 15:47:17.711515
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.template.safe_eval import safe_eval
    from ansible.template import Templar

    templar = Templar(loader=None)
    variables = {
        'a': 'b',
        'c': [1, 2, 3],
        'd': [{'e': 'f'}],
        'foo': 'Foo',
        'g': dict(
            h=dict(
                i='J',
            ),
        ),
    }

    ansible_vars = AnsibleJ2Vars(templar, variables)
    assert ansible_vars['a'] == 'b'
    assert ansible_vars['c.0'] == 1
    assert ansible_vars['d.0.e'] == 'f'
    assert ansible_vars['foo'] == 'Foo'


# Generated at 2022-06-13 15:47:26.795817
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.templating import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    var_manager = VariableManager()
    var_manager.extra_vars = {'a':1, 'b':2, 'c':3}
    loader = DataLoader()
    templar = Templar(loader=loader, variables=var_manager)

    assert 'a' in AnsibleJ2Vars(templar, dict())
    assert 'b' in AnsibleJ2Vars(templar, dict())
    assert 'c' in AnsibleJ2Vars(templar, dict())
    assert 'foo' not in AnsibleJ2Vars(templar, dict())

# Generated at 2022-06-13 15:47:34.650751
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.vars.hostvars import HostVars
    from ansible.template import Templar

    templar = Templar(loader=None)

    locals = {'test': 'test', 'test2': 2, 'test3': {} }
    hostVars = HostVars({'test': {}, 'test2': { 'test': None},
        'test3': {'test': 'test'}, 'test4': {'test': {}}})
    mappings = {'test': {}, 'test2': { 'test': None},
        'test3': {'test': 'test'}, 'test4': {'test': {}}}


# Generated at 2022-06-13 15:47:57.427788
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    """AnsibleJ2Vars - __getitem__.

    """
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    templar = Templar(loader=None)

    # initialize object
    ansible_vars = AnsibleJ2Vars(templar, {})

    ########
    # case 1: locals defined
    ########
    locals = {'k1': 'v1'}
    ansible_vars = AnsibleJ2Vars(templar, {}, locals=locals)
    k = 'k1'
    ansible_j2vars = ansible_vars[k]
    assert ansible_j2vars == 'v1'

    ########
    # case 2: locals not defined, available and known variables defined
   

# Generated at 2022-06-13 15:48:03.895558
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.template import Templar

    obj = AnsibleJ2Vars(Templar(None, None), {'k1': 'v1'}, {'k2': 'v2'})

    # test cases
    # return self._locals[varname]
    val = obj.__getitem__('k2')
    assert val == 'v2'

    # return variable
    variable = 'v3'
    val = obj.__getitem__('k3')
    assert val == 'v3'

    # return self._globals[varname]

# Generated at 2022-06-13 15:48:08.708559
# Unit test for method __len__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___len__():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.vars.hostvars import HostVars
    from ansible.vars.reserved import Reserved
    from ansible.templating import Templar
    from ansible.template import Templar as TemplateTemplar
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    import copy


# Generated at 2022-06-13 15:48:18.223066
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleUnicode
    templar = Templar(loader=None)
    locals = {}
    globals = {}
    vars = AnsibleJ2Vars(templar, globals, locals)
    # Test case when variable is in locals
    locals['l_foo'] = 'bar'
    assert 'foo' in vars
    # Test case when variable is in templar
    vars._templar.available_variables['blah'] = AnsibleUnicode('yay')
    assert 'blah' in vars
    # Test case when variable is in globals
    globals['foo'] = 'yay'
    assert 'foo' in vars
    # Test case when variable is neither in locals, templar

# Generated at 2022-06-13 15:48:23.147045
# Unit test for method __contains__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___contains__():
    try:
        from __main__ import display
    except ImportError:
        from ansible.utils.display import Display
        display = Display()

    from ansible.module_utils.jinja2 import Templar

    vars = AnsibleJ2Vars(Templar(None, display), {}, {'l_foo': 'bar', 'other': 'thing'})

    assert 'foo' in vars
    assert 'bar' not in vars
    assert 'baz' not in vars
    assert 'l_foo' not in vars
    assert 'other' in vars



# Generated at 2022-06-13 15:48:32.794731
# Unit test for method __getitem__ of class AnsibleJ2Vars
def test_AnsibleJ2Vars___getitem__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar

    vars = AnsibleJ2Vars(
            Templar(
                loader = DataLoader()
            ),
            globals = dict(),
            locals = dict()
        )

    assert(vars['ansible_all_ipv4_addresses'] == ['10.0.0.1'])
    assert(vars['ansible_architecture'] == 'x86_64')
    assert(vars['ansible_bios_date'] == '01/01/2011')
    assert(vars['ansible_bios_version'] == '1.0.0-1')
    assert(vars['ansible_default_ipv4']['address'] == '172.17.0.2')