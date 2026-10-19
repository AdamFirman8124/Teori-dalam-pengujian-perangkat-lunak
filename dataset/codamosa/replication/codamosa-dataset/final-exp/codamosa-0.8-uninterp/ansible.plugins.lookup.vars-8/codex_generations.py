

# Generated at 2022-06-13 14:45:08.196316
# Unit test for method run of class LookupModule
def test_LookupModule_run():
  from ansible.plugins.loader import lookup_loader
  lookup = lookup_loader.get('vars')
  import ansible.playbook.play_context
  import ansible.vars.manager
  import ansible.vars.hostvars
  import ansible.inventory.host
  import ansible.template.template
  terms = ['test_var']
  inventory_hostname = 'test_inventory_hostname'
  test_var = 'test_value'
  test_hostvars = {'test_hostvar': 'test_hostvar_value'}
  test_hosts = [ansible.inventory.host.Host('test_host')]
  test_hosts[0].vars = ansible.vars.manager.VariableManager(loader=None, inventory=None, host_list=None)._vars



# Generated at 2022-06-13 14:45:18.606638
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test with correct parameters
    lookup = LookupModule()
    lookup.set_loader(None)
    assert lookup.run(terms=['foo', 'bar'],
                      variables={'foo': 'baz', 'bar': {'baz': 'bing'}}) == ['baz', {'baz': 'bing'}]
    assert lookup.run(
        terms=['foo', 'bar'],
        variables={'foo': 'baz', 'bar': {'baz': 'bing'}},
        default='spam') == ['baz', {'baz': 'bing'}]

# Generated at 2022-06-13 14:45:20.162472
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Ensure that it will raise AnsibleError when term is not string_types
    assert_raises(AnsibleError, LookupModule.run, 1)

    # TODO: test when default parameter is not none.

# Generated at 2022-06-13 14:45:26.412304
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module._templar._available_variables = {'testVariable': 'testValue'}
    assert lookup_module.run([ 'testVariable' ]) == [ 'testValue' ]
    lookup_module._templar._available_variables = {'hostvars':{'testHost':{'testVariable': 'testValue'}}}
    assert lookup_module.run([ 'testVariable' ]) == [ 'testValue' ]
    assert lookup_module.run([ 'testVariable' ], default='testDefaultValue') == [ 'testValue' ]
    assert lookup_module.run([ 'testNotExistingVariable' ], default='testDefaultValue') == [ 'testDefaultValue' ]

# Generated at 2022-06-13 14:45:27.507356
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 14:45:38.742563
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # GIVEN
    myvar = {"hostvars": {
        "host": {"var": "host",
                 "host_var": "host1"
                }
        },
        "var": "all",
        "host_var": "all",
        "inventory_hostname": "host"
        }
    # THEN
    assert LookupModule(None, myvar).run(["var"])[0] == "host"
    assert LookupModule(None, myvar).run(["host_var"])[0] == "host1"
    assert LookupModule(None, myvar).run(["var"], default="")[0] == "host"
    assert LookupModule(None, myvar).run(["not_var"]) == []

# Generated at 2022-06-13 14:45:47.313283
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    # Variables to testing.
    terms = ['host1', 'host2', 'host3']
    variables = {
        'host1': 'host1',
        'host2': 'host2',
        'ansible_play_batch': 'batch',
        'ansible_play_hosts': 'hosts',
        'ansible_play_hosts_all': 'hosts_all'
    }
    # vars method of the LookupModule is called for variables.
    result = lookup.run(terms, variables)
    # Make sure that the result is as expected.
    assert result == ['host1', 'host2', 'host3']
    terms = ['ansible_play_batch', 'ansible_play_hosts', 'ansible_play_hosts_all']

# Generated at 2022-06-13 14:45:57.102803
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from collections import namedtuple
    from ansible.module_utils.six import iteritems

    def run_with_vars(lookup_module, terms, variables=None, **kwargs):
        # Create a dummy class
        class DummyClass(object):
            def __init__(self, *args, **kwargs):
                pass

            def get_option(self, key):
                return self.options.get(key, None)

            def set_options(self, **kwargs):
                self.options = kwargs['direct']

            def template(self, template_string, fail_on_undefined=True):
                return template_string

        # Create a dummy templar which will respond to template calls
        # with the same value passed in
        dummy_templar = DummyClass()

        lookup_module._tem

# Generated at 2022-06-13 14:46:03.863813
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.template import Templar
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    templar = Templar(loader=None, variables={'hostvars': {'hostname': {'test_var': "test_value"}}})
    lookup = LookupModule(loader=None, templar=templar)

    assert lookup.run(terms=['hostvars', 'hostname', 'test_var']) == [AnsibleUnsafeText("test_value")]

# Generated at 2022-06-13 14:46:12.612702
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    mod = LookupModule()
    mod._templar = 'Templar'
    mod._templar._available_variables = {
        'hostvars': {
            'somehost': {
                'host_var': 'somehost var'
            },
            'otherhost': {
                'host_var': 'otherhost var'
            }
        }
    }

    ret = mod.run(terms = ['hostvars'], variables = { 'inventory_hostname': 'somehost' })

    assert ret == [
        {
            'otherhost': {
                'host_var': 'otherhost var'
            },
            'somehost': {
                'host_var': 'somehost var'
            }
        }
    ]

# Generated at 2022-06-13 14:46:25.497263
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # param: a, b, c

    # test case 1
    # param: 2, 0, 1
    a = 2
    b = 0
    c = 1

    if b == 0:
        print("Can't divide")
    else:
        print("yes")

    expResult = None
    actResult = None
    assert expResult == actResult

    # test case 2
    # param: 2, 0, 2
    a = 2
    b = 0
    c = 2

    if b == 0:
        print("Can't divide")
    else:
        print("yes")

    expResult = None
    actResult = None
    assert expResult == actResult

    # test case 3
    # param: 2, 0, 3
    a = 2
    b = 0
    c = 3


# Generated at 2022-06-13 14:46:34.481570
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''
    class LookupModuleTest(unittest.TestCase):

    def test_run(self):
    '''

    ###############################################
    # Test variables, inputs and expected outputs #
    ###############################################

    test_variables = {'key_str': 'strvalue', 'key_int': 7, 'key_list': ['lstvalue1', 'lstvalue2'], 'hostvars': {'host1': {'host1var1': 'host1var1value', 'host1var2': 'host1var2value', 'host1var3': 'host1var3value'}, 'host2': {'host2var1': 'host2var1value', 'host2var2': 'host2var2value'}}}

# Generated at 2022-06-13 14:46:43.357434
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    terms = ['hello']
    variables = {'hello': 'world'}
    assert lookup_module.run(terms, variables) == ['world']
    terms = ['hello']
    variables = None
    assert lookup_module.run(terms, variables) == ['world']
    terms = ['hello']
    variables = {'hello': 'planet'}
    assert lookup_module.run(terms, variables) == ['planet']
    terms = {'hello': 'world'}
    with pytest.raises(AnsibleError):
        lookup_module.run(terms, variables)
    terms = ['hello']
    variables = {'hello': None}
    assert lookup_module.run(terms, variables) == [None]
    terms = ['hello', 'world']
    variables = variables
   

# Generated at 2022-06-13 14:46:53.978995
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # args
    terms = ['variabl' + 'ename']

    # kwargs
    variables = dict()
    variables['variablename'] = 'hello'
    variables['myvar'] = 'ename'

    lookup_plugin = LookupModule()
    results = lookup_plugin.run(terms, variables=variables)
    assert len(results) > 0
    assert results == ["hello"]

    # test param default
    kwargs = dict()
    kwargs['variables'] = variables
    kwargs['default'] = 'it works!'
    defaults = lookup_plugin.run(terms, **kwargs)
    assert len(defaults) > 0
    assert defaults == ['hello']

    # test param default
    bad_terms = ['variabl' + 'notename']

# Generated at 2022-06-13 14:47:04.150436
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    terms = [
        'ansible_play_hosts',
        'ansible_play_batch',
        'ansible_play_hosts_all'
    ]

    ret = lookup_module.run(
        terms,
        variables={
            'ansible_play_hosts': [
                'host1',
                'host2'
            ],
            'ansible_play_batch': [
                'host3'
            ],
            'ansible_play_hosts_all': [
                'host4',
                'host5'
            ]
        }
    )
    assert len(ret) == 3
    assert ret[0] == ['host1', 'host2']
    assert ret[1] == ['host3']

# Generated at 2022-06-13 14:47:09.317803
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils._text import to_text
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.template import Templar

    # Set options only accept dict parameter
    # TypeError: set_options() argument after ** must be a mapping, not list
    mock_options = {'_original_base': 'vars'}

    # TypeError: 'module_utils.common._collections_compat.Mapping' object is not callable
    mock_variables = Mapping({'test_var': '12'})

    # TypeError: 'module_utils._text.to_text' object is not callable
    mock_terms = to_text(['test_var'])

    # TypeError: 'module_utils._text.to_text' object is not callable
    #

# Generated at 2022-06-13 14:47:20.523479
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class DummyLookupModule(LookupModule):
        def __init__(self, myvars=None, **kwargs):
            self._templar = DummyTemplar(myvars)

    # A dummy Templar class, part of the unit test
    class DummyTemplar(object):
        def __init__(self, myvars):
            self._available_variables = myvars

        def template(self, value, fail_on_undefined=True):
            return value

    # Test invalid setting identifier
    myvars = {}
    terms = [None]
    lm = DummyLookupModule(myvars)
    try:
        lm.run(terms, variables=None, **kwargs)
    except AnsibleError:
        pass

    # Test no variable found
    myvars

# Generated at 2022-06-13 14:47:31.032994
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.compat.tests.mock import patch
    from ansible.template import Templar
    from ansible.utils.vars import merge_hash


# Generated at 2022-06-13 14:47:38.600215
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create an instance of class LookupModule
    lm = LookupModule()
    # Create a dict of variables (simulated Ansible variables)
    variables = { 'my_var': 'my_value' }
    # Create a list of terms (simulated Ansible lookup)
    terms = ['my_var']
    # Call run method of class LookupModule
    ret = lm.run(terms, variables=variables)
    # Check if the return value is a list of 1 element
    assert ret == ['my_value']

# Generated at 2022-06-13 14:47:42.780962
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup_plugin = LookupModule()

    # test error handling for invalid identifier for variable
    THING = object()
    terms = ['var_name', THING]
    lookup_plugin._templar._available_variables = {'var_name': 'hello'}
    try:
        lookup_plugin.run(terms)
    except AnsibleError as e:
        assert "is not a string" in str(e)

    # test error handling for undefined variable
    terms = ['var_name', 'var_not_found']
    lookup_plugin._templar._available_variables = {'var_name': 'hello'}
    try:
        lookup_plugin.run(terms)
    except AnsibleError as e:
        assert "No variable found with this name: var_not_found" in str(e)

    #

# Generated at 2022-06-13 14:48:02.241464
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create instance of LookupModule class
    lookup_module = LookupModule()

    # Create lookup module options
    lookup_module_options = {}

    # Create lookup module context
    lookup_module_context = {}

    # Create lookup module templar
    lookup_module_templar = object()
    lookup_module._templar = lookup_module_templar

    # Create inventory host variable 'hostvars'
    inventory_host_vars = {
        'hostvars':
            {
                'localhost': {
                    'variablename': 'hello',
                    'myvar': 'ename'
                }
            }
    }

    # Create lookup module variable 'ansible_play_hosts'
    ansible_play_hosts = 'localhost'

    # Create lookup module variable 'ansible_play_batch

# Generated at 2022-06-13 14:48:14.353926
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    term1 = 'term1'
    term2 = 'term2'
    test_options = {'_ansible_check_mode': False, '_ansible_debug': False, '_ansible_diff': False, '_ansible_keep_remote_files': False, '_ansible_no_log': False,
                    '_ansible_selinux_special_fs': ('fuse', 'nfs', 'vboxsf', 'ramfs', '9p'), '_ansible_shell_executable': '/bin/sh', '_ansible_socket': None,
                    '_ansible_string_conversion_action': 'warn'}
    #the value of _ansible_check_mode default is false

    test_default_value = 'default_value'
    test_undefined_variable = 'undefined_variable'

# Generated at 2022-06-13 14:48:22.150568
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    import pytest

    context = PlayContext()
    context.extra_vars = {'foo': 'bar', 'bar': 'baz'}

    templar = Templar(loader=None, variables=context.extra_vars)

    lookup = LookupModule()
    lookup.set_options(direct={'var_options': context.extra_vars, '_ansible_check_mode': True})
    lookup._templar = templar

    # valid variable foo
    assert lookup.run(terms=['foo'], variables=context.extra_vars) == ['bar']

    # valid variable bar
    assert lookup.run(terms=['bar'], variables=context.extra_vars) == ['baz']

   

# Generated at 2022-06-13 14:48:33.484061
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.parsing.dataloader
    import ansible.vars
    import ansible.inventory
    import ansible.playbook.play

    loader = ansible.parsing.dataloader.DataLoader()
    inv = ansible.inventory.Inventory(loader=loader, variable_manager=ansible.vars.VariableManager(), host_list=[])
    variable_manager = ansible.vars.VariableManager()
    variable_manager.set_inventory(inv)

    templar = ansible.playbook.play.Play()._get_templar(loader=loader, variables=variable_manager.get_vars())

    # Test run method with valid terms
    terms = ['ansible_play_hosts', 'ansible_play_batch', 'ansible_play_hosts_all']
   

# Generated at 2022-06-13 14:48:43.253763
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible.parsing.splitter import parse_kv
    from ansible.template import Templar
    import ansible.constants as C
    from ansible.inventory.host import Host
    from ansible.vars.hostvars import HostVars
    AnsibleUndefinedVariable = AnsibleError
    LookupBase = object
    LookupModule = object

    class ModuleStub(LookupBase):
        def __init__(self, templar=None, variables=None, direct=None):
            self._templar = Templar(loader=None, variables=variables)
            self.set_options(var_options=variables, direct=direct)


# Generated at 2022-06-13 14:48:53.207739
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Class used to mock the Ansible module
    class FakeModule():
        def __init__(self):
            self.params = {
                'default': None,
                'term': 'variablename',
            }
            self.params = {
                'default': None,
                'term': 'hostvars'
            }


    # Class used to mock the Ansible templar
    class FakeTemplar:
        def __init__(self):
            self._available_variables = {
                'variablename': 'hello',
                'hostvars': {
                        'hostname1': {
                            'variablename': 'hello'
                        },
                        'hostname2': {
                            'variablename': 'hello'
                        }
                    }
                }


# Generated at 2022-06-13 14:49:03.963629
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import sys

    print(os.path.dirname(os.path.realpath(__file__)))
    print(sys.path)
    sys.path.append("./../../")
    print(sys.path)
    print(os.path.dirname(os.path.realpath(__file__)))
    from ansible.template import Templar

    templar = Templar(loader=None, variables={})
    lu = LookupModule(templar=templar)
    # Test case 1
    terms = "a"
    myvars = {
        "a": 1,
        "b": 2
    }
    res = lu.run(terms=terms, variables=myvars)
    assert res == [1]

    # Test case 2

# Generated at 2022-06-13 14:49:10.681770
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_instance = LookupModule()
    test_instance.set_options(var_options=None, direct={'_original_file': 'ansible/playbooks/playbook.yml', '_original_module': 'debug', '_original_module_args': {'msg': '{{ lookup(\'vars\', \'variablename\', default=\'moo\') }}'}})
    assert test_instance.run(["variablename"], variables=None) == [None]

# Generated at 2022-06-13 14:49:11.218940
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert True

# Generated at 2022-06-13 14:49:11.850381
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 14:49:34.983990
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # pylint: disable=too-many-locals
    # pylint: disable=too-many-statements
    # pylint: disable=too-many-branches
    terms = ["ansible_play_hosts", "ansible_play_batch", "ansible_play_hosts_all"]
    variables = {"ansible_play_hosts": "hosts.j2", "ansible_play_batch": "batch.j2", "ansible_play_hosts_all": "all.j2"}
    ret_val = LookupModule().run(terms, variables)
    assert ret_val == ["hosts.j2", "batch.j2", "all.j2"]
    terms = ["myvar"]
    variables = {"myvar": ["hello", "world"]}
    ret_val = Look

# Generated at 2022-06-13 14:49:35.641126
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: implement unit test
    pass

# Generated at 2022-06-13 14:49:37.942032
# Unit test for method run of class LookupModule
def test_LookupModule_run():
  assert LookupModule.run(None, ['ansible_host']) == ['192.168.1.135']


# Generated at 2022-06-13 14:49:48.900192
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Configuring mocks and mocks replacements
    # Mocking needed modules
    mocked_module_name = 'ansible.module_utils.six'
    mocked_string_types = 'ansible.module_utils.six.string_types'
    mocked_module = mock.MagicMock()
    mocked_module.string_types.return_value = 'string_types_return'
    sys.modules[mocked_module_name] = mocked_module
    mocked_string_types_mock = mock.MagicMock()
    sys.modules[mocked_string_types] = mocked_string_types_mock
    sys.modules['ansible.errors'] = mock.MagicMock()
    mocked_set_options = mock.MagicMock()
    mocked_get_option = mock.MagicMock()
    mocked_get_option

# Generated at 2022-06-13 14:49:58.535841
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # the tests for the following options are performed in test_template.py, test_default.py and test_fail_on_undefined.py
    my_variables = {}
    my_kwargs = {}
    my_terms = []
    my_result = [None]
    my_expected_result = []

    my_module = LookupModule()
    my_module.set_loader(None)
    my_module.run(my_terms, my_variables, **my_kwargs)

# Generated at 2022-06-13 14:50:08.706174
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from units.mock.loader import DictDataLoader

    mylookup = LookupModule()
    mylookup.set_loader(DictDataLoader({}))

    mylookup._templar = DictDataLoader({'_available_variables': {'ansible_play_hosts': ['a'], 'ansible_play_batch': ['b'], 'ansible_play_hosts_all': ['c']}})

    assert mylookup.run(['ansible_play_hosts', 'ansible_play_batch', 'ansible_play_hosts_all']) == [['a'], ['b'], ['c']]
    assert mylookup.run(['ansible_play_hosts', 'ansible']) == [['a'], []]

# Generated at 2022-06-13 14:50:19.539074
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    templar = FakeTemplar(variables={'variablename': 'hello',
                                     'myvar': 'ename'})

    l = LookupModule(templar=templar)
    assert l.run(["variabl" + templar._available_variables['myvar']]) == ['hello']

    #default = ''
    l = LookupModule(templar=templar)
    assert l.run(["variabl" + templar._available_variables['myvar']], default='') == ['']

    #default = None, ignore_errors=True
    l = LookupModule(templar=templar)
    assert l.run(["variabl" + "notename"], default=None, ignore_errors=True) == [None]
    l = LookupModule

# Generated at 2022-06-13 14:50:29.782269
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test: Retrieve variable ansible_play_hosts, ansible_play_batch, ansible_play_hosts_all
    #       from varaibles set by PLAYBOOK variable name
    # Expected: [u'host1', u'host2', u'host3', u'host1,host2,host3']
    test_vars = {
        'inventory_hostname': 'localhost',
        'ansible_play_batch': 'host1,host2,host3',
        'ansible_play_hosts': [u'host1', u'host2', u'host3'],
        'ansible_play_hosts_all': [u'host1', u'host2', u'host3'],
    }


# Generated at 2022-06-13 14:50:37.697139
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible.plugins.lookup.vars import LookupModule

    lookup = LookupModule()

    result = lookup.run([], terms=['foo'], variables={'foo':'bar'})
    assert result == ['bar'], result

    with pytest.raises(AnsibleError) as err:
        result = lookup.run([], terms=['foo'], variables={'foo':{'bar':'baz'}})
    assert str(err.value).find('is not a string, its a') != -1, err

    result = lookup.run([], terms=['foo'], variables={'foo':'', default:''})
    assert result == [''], result

    result = lookup.run([], terms=['foo'], variables={'foo':'', default:''}, default='')

# Generated at 2022-06-13 14:50:46.535425
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager

    def _resolve_list_item():
        pass

    def _resolve_list_items():
        pass

    def _fail_function():
        raise KeyError

    terms = ['var1', 'var2', 'var3']

# Generated at 2022-06-13 14:51:24.048800
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test 1
    terms = ["ansible_hello"]
    variables = {"ansible_hello": "world"}
    lm = LookupModule()
    lm.set_options(var_options=variables, direct={"default": None})
    lm._templar.available_variables = variables
    assert lm.run(terms) == ["world"]

    # Test 2
    terms = ["ansible_hello", "ansible_bye"]
    lm = LookupModule()
    lm.set_options(var_options=variables, direct={"default": None})
    lm._templar.available_variables = variables
    assert lm.run(terms) == ["world", None]



# Generated at 2022-06-13 14:51:30.931119
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    mylookup = LookupModule()
    assert mylookup.run(terms=['hostvars'], variables={'hostvars': {'192.168.0.1': {'ansible_os_family': 'RedHat'}}}, default='foobar') == [{'192.168.0.1': {'ansible_os_family': 'RedHat'}}]

# Generated at 2022-06-13 14:51:40.352068
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    args = [ 'hostvars', 'inventory_hostname']

# Generated at 2022-06-13 14:51:49.048066
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import unittest2 as unittest
    import collections

    # Mock methods as they are not needed for testing
    def get_option(self, var):
        return self._options[var]
    LookupModule.get_option = get_option

    def set_options(self, var_options=None, direct=None):
        self._options = {}
        if var_options:
            self._options['var_options'] = var_options
        if direct:
            self._options['var_options'] = direct
    LookupModule.set_options = set_options

    def template(self, value, fail_on_undefined=False):
        return value
    LookupModule.template = template

    # Templating failed as not needed for testing purposes

# Generated at 2022-06-13 14:51:58.080143
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def test_assertion(args, assertion_msg):
        raised_exception = False
        try:
            test_ansible_mock_obj = AnsibleMock()
            test_ansible_mock_obj.run(args, variables=None, **{'default': None})
        except Exception as e:
            raised_exception = True

        assert raised_exception, assertion_msg

    test_assertion([1], 'Variable must be a string')
    test_assertion(('var', 1), 'Variable must be a string')
    test_assertion(('var', '1'), 'Variable must exit')
    test_assertion(('var', '1'), 'Variable must exit')
    test_assertion(('var', '1'), 'Variable must exit')

# Generated at 2022-06-13 14:52:05.575598
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test case: no default - Test case: no variables
    lookup_instance = LookupModule()
    lookup_instance.run(terms=["test"], variables=None)
    # Test case: with default
    lookup_instance = LookupModule()
    lookup_instance.run(terms=["test"], variables=None, default=True)
    # Test case: with variables
    try:
        lookup_instance = LookupModule()
        lookup_instance.run(terms=["test"], variables=dict(test="test_variable"))
    except KeyError:
        pass

    # Test case: not string types
    lookup_instance = LookupModule()
    lookup_instance.run(terms=[1], variables=dict(test="test_variable"))
    # Test case: variable not found
    lookup_instance = LookupModule()

# Generated at 2022-06-13 14:52:12.492965
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    myvars = {
        'anyvar': 'anyvalue',
        'hostvars': {
            'ansible_play_hosts': ['1.1.1.1', '2.2.2.2'],
            'ansible_play_batch': [],
            'ansible_play_hosts_all': ['1.1.1.1', '2.2.2.2']
        }
    }
    lookup_module.set_options(var_options=myvars)
    terms = ['anyvar', 'hostvars', 'ansible_play_hosts', 'ansible_play_batch', 'ansible_play_hosts_all']
    res = lookup_module.run(terms, variables=myvars)

# Generated at 2022-06-13 14:52:23.026752
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test with default arg
    lookup_plugin = LookupModule()
    myVars = {'jboss_host': "hostname.local", 'jboss_port': "8888", 'jboss_user': "user", 'jboss_password': "password",
              'jboss_protocol': "http", 'jboss_controller_url': "http://hostname.local:8888"}
    search = [ "jboss_host" ]
    results = lookup_plugin.run(search, variables=myVars)
    assert results == ["hostname.local"]

    # test with replaced arg
    search = [ {'jboss_host': "othername.local"} ]
    results = lookup_plugin.run(search, variables=myVars)
    assert results == ["othername.local"]


# Generated at 2022-06-13 14:52:25.769114
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l._templar._available_variables = {'var1': 'hello'}
    assert l.run(['var1']) == ['hello']


# Generated at 2022-06-13 14:52:29.507388
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms=["ansible_os_family"]
    variables = {}
    variables['ansible_os_family'] = 'RedHat'
    mylookup = LookupModule()
    results = mylookup.run(terms, variables)
    assert len(results) == 1
    assert results[0] == 'RedHat'

# Generated at 2022-06-13 14:53:41.983686
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class DummyLookupModule(LookupBase):
        def __init__(self):
            super(DummyLookupModule, self).__init__()
            self.set_options()

        def run(self, terms, variables=None, **kwargs):
            return terms

    lookup_mod = DummyLookupModule()
    myvars = {'variablname': 'hello', 'myvar': 'ename'}
    terms = ['variabl' + lookup_mod.run(terms=['myvar'], variables=myvars)[0]]
    assert lookup_mod.run(terms=terms, variables=myvars) == ['hello']

# Generated at 2022-06-13 14:53:49.528406
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup.vars import LookupModule
    from ansible.module_utils.six import PY3

    old_I18N = None
    if PY3:
        import builtins
        old_I18N = builtins.__dict__.get('_')
        builtins.__dict__['_'] = lambda x: x

    lookup = LookupModule()

# Generated at 2022-06-13 14:53:53.130041
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ["hostvars", "inventory_hostname", "ansible_play_hosts", "ansible_play_batch", "ansible_play_hosts_all"]
    lookup.run(terms=terms)

# Generated at 2022-06-13 14:54:00.082537
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_m = LookupModule()
    lookup_m._templar._available_variables = {'a': 'VarA'}
    assert lookup_m.run([{'a': 'VarA'}]) == [{'a': 'VarA'}]

    # case that value of term is not string
    with pytest.raises(AnsibleError) as result:
        lookup_m.run([5])
    assert "Invalid setting identifier, \"5\" is not a string, its a <class 'int'>" in result.value.message

# Generated at 2022-06-13 14:54:06.443968
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test candidate 1
    terms = ["myVar"]
    lookup_object = LookupModule()
    result = lookup_object.run(terms, variables = {'myVar' : 'value'})
    assert result == ["value"]

    # Test candidate 2
    terms = ["myVar"]
    lookup_object = LookupModule(variables = {'myVar' : 'value'})
    result = lookup_object.run(terms)
    assert result == ["value"]

    # Test candidate 3
    terms = ["myVar"]
    lookup_object = LookupModule()
    assert lookup_object.run(terms) == [""]

# Generated at 2022-06-13 14:54:14.761997
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Unit test for method run of class LookupModule
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.parsing.dataloader import DataLoader

    class MyVars(dict):
        def get(self, key, *args, **kwargs):
            try:
                return super(MyVars, self).get(key, *args, **kwargs)
            except KeyError:
                try:
                    return self['hostvars'][key]
                except KeyError:
                    return super(MyVars, self).get(*args, **kwargs)

    inventory = Inventory(loader=DataLoader(), variable_manager=VariableManager(), host_list=['localhost'])
   

# Generated at 2022-06-13 14:54:21.603398
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
        Unit test for method run of class LookupModule.
        """
    # Initializing instance
    lookup_module_instance = LookupModule()

    # Create a mock for parameter terms
    terms = ['ansible_play_hosts', 'ansible_play_batch', 'ansible_play_hosts_all']
    assert lookup_module_instance.run(terms) == [
        {'ansible-01', 'ansible-02', 'ansible-03'},
        {'ansible-07', 'ansible-08'},
        {'ansible-01', 'ansible-02', 'ansible-03', 'ansible-04', 'ansible-05', 'ansible-06', 'ansible-07', 'ansible-08'}]

# Generated at 2022-06-13 14:54:29.298604
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()

    # Run the test with a term that will be found
    terms = ['foo']
    variables = {'foo': 'bar'}
    results = module.run(terms, variables)
    assert results == ['bar']

    # Run the test with a term that will not be found
    terms = ['foo']
    variables = {}
    results = module.run(terms, variables)
    assert results == []

    # Run the test with a term that will not be found and a default value provided
    terms = ['foo']
    variables = {}
    default = 'bar'
    results = module.run(terms, variables, default=default)
    assert results == ['bar']

# Generated at 2022-06-13 14:54:32.767465
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ('c', 'a', 'b')
    variables = {'a': 1, 'b': 2, 'c': 3}
    expected = [3, 1, 2]
    assert LookupModule().run(terms, variables) == expected

# Generated at 2022-06-13 14:54:41.799291
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible.vars import VariableManager

    def run_it_with_error(args):
        print("input args {}".format(args))
        with pytest.raises(AnsibleError) as e_info:
            LookupModule().run(terms=args)

    assert LookupModule().run(terms='') == []
    assert LookupModule().run(terms=['abc']) == []
    assert LookupModule().run(terms=['ansible_play_hosts', 'ansible_play_batch']) == []

    vm = VariableManager()
    LookupModule().run(terms=['ansible_play_hosts', 'ansible_play_batch'],
                       variables=vm._vars)