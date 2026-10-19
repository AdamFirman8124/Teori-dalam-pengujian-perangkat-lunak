

# Generated at 2022-06-13 16:25:12.604645
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    '''This function just implements a basic test that should be expanded'''

    # Import modules so Ansible is not required
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    # Import needed functions
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    # Setup function parameters
    terms = '{{ test_var }}'
    templar = Templar(VariableManager(), loader=DataLoader())
    loader = DataLoader()

    # Setup expected results
    expected_results = ['test_value']

    # Call function and check kwargs
    function_results = listify_lookup_plugin_terms(terms, templar, loader)

    # Check results

# Generated at 2022-06-13 16:25:20.059976
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    import ansible.module_utils.common.text.converters as converters
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.template import Templar

    templar = Templar(loader=None, variables={})

    test_result = [templar.template('{{ foo }}', fail_on_undefined=False), templar.template('{{ bar }}', fail_on_undefined=False)]
    assert listify_lookup_plugin_terms(['{{ foo }}', '{{ bar }}'], templar, loader=None, fail_on_undefined=False) == test_result


# Generated at 2022-06-13 16:25:27.421098
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar

    loader = DataLoader()
    templar = Templar(loader=loader)

    terms = [1, 2, 3]
    result = listify_lookup_plugin_terms(terms, templar, loader)
    assert terms == result

    terms = '{{ foo }}'
    result = listify_lookup_plugin_terms(terms, templar, loader)
    assert isinstance(result, list)
    assert isinstance(result[0], string_types)

    terms = [
        '{{ foo }}',
        '{{ bar }}',
        '{{ baz }}'
    ]
    result = listify_lookup_plugin_terms(terms, templar, loader)

# Generated at 2022-06-13 16:25:38.344250
# Unit test for function listify_lookup_plugin_terms

# Generated at 2022-06-13 16:25:50.775725
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.set_inventory(loader.load_inventory("/dev/null"))
    my_vars = dict(
        name1 = "foo",
        var1 = ['a','b','c'],
        var2 = 'bar',
        num = 4
    )
    variable_manager.set_vars(my_vars)
    templar = Templar(loader=loader, variables=variable_manager)

    assert listify_lookup_plugin_terms(templar.template('{{name1}}'), templar, loader) == ['foo']
    assert listify_lookup_plugin

# Generated at 2022-06-13 16:26:00.356990
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    class DummyVarsModule(object):

        def __init__(self):
            self.FILE_ATTRIBUTES = dict(
                follow=True,
                regexp=None,
                age=None,
                size=None,
                get_md5=False,
                access_time=None,
                modify_time=None,
                change_time=None,
                search_regexp=None,
                use_regexp=False
            )

    class DummyModuleManager(object):

        def __init__(self):
            self.vars = DummyVarsModule()

    class Dummy(object):

        def __init__(self):
            self.module_manager = DummyModuleManager()


# Generated at 2022-06-13 16:26:11.697619
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    class FakeVarsModule():
        def __init__(self):
            self.noop = False
            self.failed = False
            self.cur_context = ['joe', 'bob']
        def add_host_var(self, host, varname, value):
            pass
        def add_group_var(self, group, varname, value):
            pass
        def merge_vars(self, vars, prio=None):
            return vars
    class FakePlayContext():
        def __init__(self):
            self.hostvars = {}
            self.vars = {}
            self.prompt = False

    templar = Templar(loader=None, variables=FakeVarsModule(), play_context=FakePlayContext())
    assert listify_lookup_plugin

# Generated at 2022-06-13 16:26:20.229920
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.common.collections import is_sequence

    from ansible.parsing.yaml.objects import AnsibleMapping

    from ansible.template import Templar
    from ansible.playbook.play_context import PlayContext

    from units.mock.loader import DictDataLoader

    from units.compat.mock import patch


# Generated at 2022-06-13 16:26:31.689747
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    templar = Templar(loader=loader, variables=VariableManager())

    # Test a string, will become a list of one string
    terms = 'mystring'
    results = listify_lookup_plugin_terms(terms, templar, loader)
    assert(isinstance(results, list))
    assert(results == ['mystring'])

    # Test a list of strings, should maintain its structure
    terms = ['mystring1', 'mystring2']
    results = listify_lookup_plugin_terms(terms, templar, loader)
    assert(isinstance(results, list))

# Generated at 2022-06-13 16:26:41.418766
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    '''
    This tests that a dict, when passed as a single term and wrapped
    in a list, gets iterated over properly.
    '''
    from ansible.utils import plugin_docs as doc_templar
    from ansible.parsing.dataloader import DataLoader

    loader_kwargs = dict(
        class_name='AnsibleLoader',
        config=dict(
            connection='local',
            module_path='/tmp',
        )
    )

    terms = dict(
        key='value',
        key2='value2'
    )

    templar = doc_templar.LookupModuleDocs()
    loader = DataLoader()

# Generated at 2022-06-13 16:26:43.817411
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    pass

# Generated at 2022-06-13 16:26:50.724867
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    module = None
    templar = DummyTemplar()
    loader = DummyLoader()

    # Test conversion of a string to a list
    terms = 'foo'
    result = listify_lookup_plugin_terms(terms, templar, loader)
    assert result == ['foo']

    # Test conversion of a list to a list
    terms = [True, False]
    result = listify_lookup_plugin_terms(terms, templar, loader)
    assert result == [True, False]

    # Test conversion of a non-string, non-Iterable to a list
    terms = 1
    result = listify_lookup_plugin_terms(terms, templar, loader)
    assert result == [1]

# Dummy classes for unit testing listify_lookup_plugin_terms

# Generated at 2022-06-13 16:27:01.431524
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.module_utils._text import to_native
    from ansible.template import Templar

    templar = Templar(None, loader=None)

    terms = u"{{ my_terms }}"
    terms_data = {u'my_terms': u'single'}
    result = listify_lookup_plugin_terms(terms, templar, loader=None, fail_on_undefined=True,
                                         convert_bare=False)
    assert result == [u'single']
    result = listify_lookup_plugin_terms(terms, templar, loader=None, fail_on_undefined=True,
                                         convert_bare=True, variables=terms_data)
    assert result == [u'single']

    terms = u"{{ my_terms | to_json }}"

# Generated at 2022-06-13 16:27:08.863822
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    fake_loader = DataLoader()
    fake_env_vars = dict()
    fake_inventory = dict()
    fake_variable_manager = VariableManager()

    fake_loader.set_basedir("/test/test")
    fake_loader.set_variable_manager(fake_variable_manager)
    fake_templar = Templar(loader=fake_loader, variables=fake_variable_manager)

    # test strings
    terms = "{{ test }}"
    terms = listify_lookup_plugin_terms(terms, fake_templar, fake_loader)
    assert isinstance(terms, list)
    assert len(terms) == 1

# Generated at 2022-06-13 16:27:18.074182
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    templar = None
    loader = None

    # Empty list
    assert listify_lookup_plugin_terms('', templar, loader) == []

    # Not a list but a string
    assert listify_lookup_plugin_terms('foo', templar, loader) == ['foo']

    # A list
    assert listify_lookup_plugin_terms(['foo', 'bar', 'baz'], templar, loader) == ['foo', 'bar', 'baz']

    # A list with a variable
    assert listify_lookup_plugin_terms(['foo', '{{ bar }}', 'baz'], templar, loader) == ['foo', '{{ bar }}', 'baz']

# Generated at 2022-06-13 16:27:27.856347
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    # Make sure it treats strings as is
    assert listify_lookup_plugin_terms(terms='mystring', templar=None, loader=None, fail_on_undefined=True, convert_bare=False) == 'mystring'

    # Make sure it turns non-strings into strings
    assert listify_lookup_plugin_terms(terms=1, templar=None, loader=None, fail_on_undefined=True, convert_bare=False) == '1'
    assert listify_lookup_plugin_terms(terms='1', templar=None, loader=None, fail_on_undefined=True, convert_bare=False) == '1'

    # Make sure it turns lists into lists of strings

# Generated at 2022-06-13 16:27:40.394170
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    import ansible.module_utils.common.collections
    import ansible.template

    # test 1 string
    templar = ansible.template.Templar(loader=ansible.loader.Loader())
    terms = ['foo']
    assert listify_lookup_plugin_terms(terms, templar, None) == ['foo']

    # test 1 bare string
    templar = ansible.template.Templar(loader=ansible.loader.Loader())
    terms = 'foo'
    assert listify_lookup_plugin_terms(terms, templar, None) == ['foo']

    # test 1 templated string
    templar = ansible.template.Templar(loader=ansible.loader.Loader())
    terms = '{{foo}}'
    assert listify_lookup_plugin_terms

# Generated at 2022-06-13 16:27:41.724742
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.vault import VaultLib
    from ansible.template import Templar
    from ansible.vars import VariableManager

    vault_pass = 'ansible'

# Generated at 2022-06-13 16:27:45.596233
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.parsing.vault import VaultLib

    class TestLoader(object):
        def __init__(self):
            pass

    class TestVaultLib(VaultLib):
        def __init__(self):
            pass

    class TestHost(object):
        def __init__(self):
            pass

    class TestPlay(object):
        def __init__(self):
            self.hosts = [TestHost()]

    vault_password = 'asdf'
    vault = TestVaultLib()
    vault.read_vault_password_file(vault_password)
    loader = TestLoader()
   

# Generated at 2022-06-13 16:27:56.709342
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    # Mock jinja2
    import json
    class MockTemplar:
        '''Mock class for jinja2 templar'''
        def template(self, terms, convert_bare=False, fail_on_undefined=True):
            return terms

    class MockLoader:
        '''Mock class for jinja2 template loader'''
        def get_basedir(self, terms):
            return '.'

    templar = MockTemplar()
    loader = MockLoader()

    # Test with string
    assert listify_lookup_plugin_terms('value', templar, loader) == ['value']

    # Test with list
    assert listify_lookup_plugin_terms(['value'], templar, loader) == ['value']


    # Test with complex data
    # value.y

# Generated at 2022-06-13 16:28:09.531624
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    '''
    returns a list, with a single item, of a unicode string
    '''
    from ansible.module_utils.common._collections_compat import StringIO
    from ansible.module_utils.common._collections_compat import OrderedDict
    from ansible.parsing.vault import VaultLib
    from ansible.template import Templar

    loader = DictDataLoader({})
    list_of_strings = u'foo'
    templar = Templar(loader=loader, shared_loader_obj=loader, vault_secrets=VaultLib(None, None, [], None))
    result = listify_lookup_plugin_terms(list_of_strings, templar, loader, fail_on_undefined=True, convert_bare=False)
    assert result == [u'foo']

# Generated at 2022-06-13 16:28:17.934909
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    # Create test inventory for templar
    class TestInventory:
        def __init__(self):
            self.vars = dict()

        # Return variables for the host
        def get_vars(self, host, new_pb_basedir, runner_basedir):
            return self.vars

        # Get host by name
        def get_host(self, host):
            return host
    # Create templar
    inventory = TestInventory()
    templar = Templar(inventory=inventory, variables={})

    # Test basic functionality
    # When templating string, it is interpreted as jinja2 template
    terms = '{{ foo }}'
    # Set test variable
    inventory.vars = dict()
    inventory.vars['foo'] = 'bar'
    # Template

# Generated at 2022-06-13 16:28:19.364942
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    '''
    dummy function to serve as a unit test
    '''
    assert True

# Generated at 2022-06-13 16:28:22.976253
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    assert listify_lookup_plugin_terms('/tmp/foo.txt',None,None,False) == ['/tmp/foo.txt']
    assert listify_lookup_plugin_terms(['/tmp/foo.txt'], None, None) == ['/tmp/foo.txt']


# Generated at 2022-06-13 16:28:31.103841
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible import constants as C
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import lookup_loader, filter_loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    from ansible.utils.display import Display
    from ansible.utils.vars import load_extra_vars
    import os
    import json

    class Host:
        def __init__(self):
            self.name = "myhost"
            self.vars = dict()

        def get_name(self):
            return self.name


# Generated at 2022-06-13 16:28:39.812790
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar
    from ansible.vars    import VariableManager
    from ansible.parsing.dataloader import DataLoader

    class Options:
        DEFAULT_VAULES = {
            '__file__': None,
            '__line__': None,
            '_terms_': None,
            '_raw_params': None
        }

        def __init__(self, values):
            self.__dict__.update(self.DEFAULT_VAULES)
            self.__dict__.update(values)

    _VALUES = dict(
        _raw_params = dict(),
        __file__ = None,
        __line__ = None,
        _terms_ = None
    )


# Generated at 2022-06-13 16:28:49.720543
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.template import Templar

    v = {'a': 'b'}
    t = Templar(loader=None, variables=v)
    l = listify_lookup_plugin_terms(terms=1, templar=t, loader=None)
    assert isinstance(l, list)
    assert len(l) == 1
    assert l[0] == 1

    l = listify_lookup_plugin_terms(terms='1', templar=t, loader=None)
    assert isinstance(l, list)
    assert len(l) == 1
    assert l[0] == '1'

    l = listify_lookup_plugin_terms(terms='{{a}}', templar=t, loader=None)


# Generated at 2022-06-13 16:29:00.755992
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    import ansible.constants as C
    import os

    terms = "{{ foo }}"
    templar = Templar(loader=DataLoader(), variables={'foo': 'bar'})
    expected = ['bar']
    assert listify_lookup_plugin_terms(terms, templar, loader=None) == expected

    terms = "{{ foo }}"
    templar = Templar(loader=DataLoader(), variables={'foo': 'foobar'})
    expected = ['foobar']
    assert listify_lookup_plugin_terms(terms, templar, loader=None) == expected

    terms = "{{ foo }}"

# Generated at 2022-06-13 16:29:10.282333
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    import ansible.module_utils.jinja2_native as j2

    terms = 'foo'
    templar = j2.Jinja2Native()
    loader = None
    fail_on_undefined = True
    convert_bare = False

    assert listify_lookup_plugin_terms(terms, templar, loader, fail_on_undefined, convert_bare) == ['foo']

    terms = ['foo', 'bar']
    assert listify_lookup_plugin_terms(terms, templar, loader, fail_on_undefined, convert_bare) == ['foo', 'bar']

    terms = 'foo,bar,baz'

# Generated at 2022-06-13 16:29:20.379955
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils._text import to_text
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

    terms = listify_lookup_plugin_terms("{{ '[' + lookup('env', 'HOME') + ']' }}", None, loader)
    assert to_text("{{ '[' + lookup('env', 'HOME') + ']' }}") == terms[0]
    assert isinstance(terms, list)

    terms = listify_lookup_plugin_terms("['{{ lookup('env', 'HOME') }}']", None, loader)
    assert to_text("{{ '[' + lookup('env', 'HOME') + ']' }}") == terms[0]
    assert isinstance(terms, list)


# Generated at 2022-06-13 16:29:35.214695
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    # Test always returns a list.
    assert isinstance(listify_lookup_plugin_terms('string'), list)
    assert isinstance(listify_lookup_plugin_terms(42), list)
    assert isinstance(listify_lookup_plugin_terms(42.0), list)
    # Test doesn't convert existing lists.
    assert isinstance(listify_lookup_plugin_terms([]), list)
    assert isinstance(listify_lookup_plugin_terms(['string']), list)

# Generated at 2022-06-13 16:29:46.757146
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.vars.unsafe_proxy import UnsafeProxy, wrap_var
    from ansible.compat.tests import unittest
    from ansible.template import Templar

    vars = {'a': 'foo', 'b': 'bar', 'c': 'baz'}
    templar = Templar(loader=None, variables=vars)

# Generated at 2022-06-13 16:29:55.321837
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.template import AnsibleVaultNoKeyException
    from ansible.template import AnsibleVaultError
    from ansible.template import AnsibleUndefinedVariable
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    import sys
    import unittest

    # Init templar
    class FakeVars(object):
        _fact_cache = {}
        _hostvars = {}

    templar = Templar(loader=None, variables=FakeVars())

    # Test with a scalar string
    assert listify_lookup_plugin_terms('{{ data }}', templar, loader, fail_on_undefined=True, convert_bare=False) == ['{{ data }}']

# Generated at 2022-06-13 16:30:04.331339
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    terms = '{{ variable }}'
    templar = Templar(None, None, None)
    loaded_vars = dict()
    loaded_vars['variable'] = 'value'
    templar._available_variables = loaded_vars
    assert templar._available_variables['variable'] == loaded_vars['variable']
    assert listify_lookup_plugin_terms(terms, templar, None) == ['value']

    terms = ['{{ variable }}']
    templar = Templar(None, None, None)
    loaded_vars = dict()
    loaded_vars['variable'] = 'value'
    templar._available_variables = loaded_vars
    assert templar._available_variables['variable'] == loaded_vars['variable']
   

# Generated at 2022-06-13 16:30:15.701445
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.module_utils.common._collections_compat import OrderedDict
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import VaultLib
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    import json

    vault_id = None
    vault_secret = 'ansible-vault-test'

    inventory = InventoryManager(loader=None, sources=[])
    variable_manager = VariableManager(loader=None, inventory=inventory)


# Generated at 2022-06-13 16:30:27.805189
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.template import Templar
    from ansible.template.safe_eval import safe_eval
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVarsVars

    vars_manager = VariableManager()
    vars_manager.add_extra_vars(HostVarsVars(vars_manager, "localhost"))
    templar = Templar(loader=None, variables=vars_manager)
    just_bare = AnsibleMapping(dict(var="{{bare}}"))
    var_bared = AnsibleMapping(dict(var="{{ variable_1 }}"))
    var_bared_in

# Generated at 2022-06-13 16:30:36.710102
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    import ansible.parsing.yaml.objects
    from ansible.template import Templar

    class DummyVarsModule(object):
        def __init__(self, tmp, fail_on_undefined=True):
            self._tmp = tmp
            self._fail_on_undefined = fail_on_undefined

        def __getitem__(self, key):
            return self._tmp[key]

        def get_fail_on_undefined(self):
            return self._fail_on_undefined

    class DummyVars(object):
        def __init__(self, tmp):
            self._tmp = tmp

        def get_vars(self):
            return DummyVarsModule(self._tmp)


# Generated at 2022-06-13 16:30:42.142989
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    # Import here, so that the Templar class isn't instantiated twice
    from ansible.playbook.play_context import PlayContext

    terms = 'foo'
    templar = Templar(loader=None, variables={})
    assert listify_lookup_plugin_terms(terms, templar, loader=None, fail_on_undefined=True, convert_bare=False) == ['foo']

    terms = ['foo', 'bar']
    templar = Templar(loader=None, variables={})
    assert listify_lookup_plugin_terms(terms, templar, loader=None, fail_on_undefined=True, convert_bare=False) == ['foo', 'bar']

    terms = '{{ foo }}'

# Generated at 2022-06-13 16:30:53.081532
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    def _assert_terms(terms, original, expected):
        templar = Templar(loader=None, variables={})
        assert listify_lookup_plugin_terms(terms, templar) == expected
        assert listify_lookup_plugin_terms(original, templar) == expected

    _assert_terms('foo', 'foo', ['foo'])
    _assert_terms('foo,bar', 'foo,bar', ['foo', 'bar'])
    _assert_terms('foo\nbar', 'foo\nbar', ['foo', 'bar'])
    _assert_terms(['foo'], ['foo'], ['foo'])
    _assert_terms(['foo', 'bar'], ['foo', 'bar'], ['foo', 'bar'])

# Generated at 2022-06-13 16:31:01.497384
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    class DummyVarsModule:
        def _load_name_to_path(self, name):
            return 'fakedir/fakefile'

    class DummyLoader(DummyVarsModule):
        pass

    templar = Templar(loader=DummyLoader())

    assert listify_lookup_plugin_terms('one', templar, loader, convert_bare=False) == ['one']
    assert listify_lookup_plugin_terms('one two', templar, loader, convert_bare=False) == ['one two']
    assert listify_lookup_plugin_terms(' one two ', templar, loader, convert_bare=False) == ['one two']

# Generated at 2022-06-13 16:31:24.468866
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar


# Generated at 2022-06-13 16:31:36.130870
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    import sys

    variable_manager = VariableManager()
    loader = DataLoader()
    templar = Templar(loader=loader, variable_manager=variable_manager, shared_loader_obj=None)

    variable_manager.set_inventory(Inventory(loader=loader, variable_manager=variable_manager, host_list='localhost'))

    # test a string that is the name of a single file
    res = listify_lookup_plugin_terms('foobar', templar, loader, False)
    assert (len(res) == 1 and res[0] == 'foobar')

    # test a string that is the names of files, separated by

# Generated at 2022-06-13 16:31:43.873835
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    assert listify_lookup_plugin_terms('foo', Templar(loader=None), None) == ['foo']
    assert listify_lookup_plugin_terms(' foo ', Templar(loader=None), None) == ['foo']
    assert listify_lookup_plugin_terms(['foo'], Templar(loader=None), None) == ['foo']
    assert listify_lookup_plugin_terms(('foo',), Templar(loader=None), None) == ['foo']
    assert listify_lookup_plugin_terms('1', Templar(loader=None), None, convert_bare=True) == [1]
    assert listify_lookup_plugin_terms('1', Templar(loader=None), None, convert_bare=False) == ['1']

# Generated at 2022-06-13 16:31:52.629714
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar
    from ansible.vars.unsafe_proxy import UnsafeProxy

    templar = Templar(loader=None)
    templar._available_variables = dict(oval=5, oval2=6, oval3="{{ oval2 }}")

    terms = [1, 2, "{{ oval }}", UnsafeProxy("{{ oval }}")]

    res = listify_lookup_plugin_terms(terms, templar, loader=None, fail_on_undefined=False, convert_bare=False)
    assert res == [1, 2, 5, UnsafeProxy("{{ oval }}")]

    terms  = [1, 2, "{{ oval }}", UnsafeProxy("{{ oval }}")]

# Generated at 2022-06-13 16:32:00.027738
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.plugins.loader import lookup_loader
    from ansible.template import Templar

    data = dict(
        one=dict(
            a=1,
            b=2,
        ),
        two=dict(
            c=3,
            d=4,
        ),
        three=dict(
            e=5,
            f=6,
        ),
    )

    # Test a string and objects that are not Iterable.
    for terms in (True, 1, 1.0):

        terms = listify_lookup_plugin_terms(terms, Templar(loader=lookup_loader, variables=data), lookup_loader)

        assert isinstance(terms, list)
        assert len(terms) == 1
        assert terms[0] == terms

    # Test a list of string and objects.
    terms = listify

# Generated at 2022-06-13 16:32:11.450257
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.loader import lookup_loader
    from ansible import utils

    class TestLookupModule:
        def __init__(self, basedir=None, runner=None, **kwargs):
            pass

        def run(self, terms, **kwargs):
            return templar.template(terms, convert_bare=True, fail_on_undefined=True)

    lookup_loader.add('test_lookup_module', TestLookupModule)
    loader = DataLoader()
    utils.plugins.lookup_loader = lookup_loader
    templar = Templar(loader=loader, variables={'foo': 'universe'})


# Generated at 2022-06-13 16:32:18.735554
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.utils.unsafe_proxy import wrap_var
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.template import Templar
    from ansible.template.vars import AnsibleVariableManager
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.vars.manager import HostVars

    class DummyVars(VariableManager):
        def get_vars(self, loader, path, entities, cache=True):
            if isinstance(entities, list):
                entities = entities[0]

            if isinstance(entities, string_types):
                x = AnsibleUnicode(entities)
                x._unsafe = True

# Generated at 2022-06-13 16:32:26.065779
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible import constants as C
    from ansible.template import Templar
    from ansible.template.vars import AnsibleVars
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.template.safe_eval import safe_eval

    # just in case we're running as root
    templar = Templar(loader=None, variables=AnsibleVars(playbook_basedir='/tmp', additional_variable_paths=[]))

    # test simple string
    terms = "foo"
    terms = listify_lookup_plugin_terms(terms, templar, loader=None)
    assert isinstance(terms, list)
    assert len(terms) == 1
    assert terms[0] == "foo"

    # test a complex expression
    terms = AnsibleUnicode

# Generated at 2022-06-13 16:32:34.587106
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.module_utils.common._collections_compat import UnsafeList
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    terms = '[ "{{ foo }}", "{{ bar }}", ["{{ baz }}", "{{ qux }}"] ]'
    templar = Templar(loader=DataLoader())
    templar._available_variables = dict(
        foo="foo",
        bar=AnsibleUnsafeText("bar"),
        baz="baz",
        qux=AnsibleUnsafeText("qux"),
    )

# Generated at 2022-06-13 16:32:39.708199
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    expected = ['foo', 'bar']
    assert listify_lookup_plugin_terms(expected, Templar(loader=None, variables={})) == expected
    assert listify_lookup_plugin_terms('foo,bar', Templar(loader=None, variables={})) == expected
    assert listify_lookup_plugin_terms('"foo,bar"', Templar(loader=None, variables={})) == expected

# Generated at 2022-06-13 16:33:13.684395
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.template import Templar
    from ansible.vars import VariableManager

    v = VariableManager()
    v.set_variable('_terms', 'string_terms')
    v.set_variable('_terms_list', 'list_terms')
    v.set_variable('_undefined', 'undefined_var')
    v.set_variable('_empty_string', '')
    v.set_variable('_list', ['a', 'b', 'c'])
    v.set_variable('_dict', {'a': 'b', 'c': 'd'})
    v.set_variable('_empty_list', [])
    v.set_variable('_empty_dict', {})

    terms = '{{ _terms }}'
    terms

# Generated at 2022-06-13 16:33:21.561195
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    templar = Templar(loader=None)

    # Single value
    x = listify_lookup_plugin_terms('one', templar, None)
    assert x == ['one']

    # Single value already a list
    x = listify_lookup_plugin_terms(['one'], templar, None)
    assert x == ['one']

    # Single templated value
    x = listify_lookup_plugin_terms('{{ foo }}', templar, None, convert_bare=True)
    assert x == ['{{ foo }}']

    # Single templated value
    x = listify_lookup_plugin_terms('{{ foo }}', templar, None, convert_bare=True)
    assert x == ['{{ foo }}']

    # Single templated value

# Generated at 2022-06-13 16:33:27.936999
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    terms = '{{ a }},{{ b }}'
    templar = Templar(loader=None, variables={'a': 'a', 'b': 'b'})

    expected = ['a', 'b']
    assert listify_lookup_plugin_terms(terms, templar, None) == expected

    terms = {'foo': '{{ a }}', 'bar': '{{ b }}'}

    expected = {'foo': 'a', 'bar': 'b'}
    assert listify_lookup_plugin_terms(terms, templar, None) == expected

    terms = ['foo', 'bar']
    assert listify_lookup_plugin_terms(terms, templar, None) == terms

# Generated at 2022-06-13 16:33:39.890330
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.utils.vars import combine_vars

    play_context = PlayContext()
    templar = Templar(loader=None, variables=combine_vars(loader=None, variables={'item': 'item'}))

    assert listify_lookup_plugin_terms('item', templar, loader=None) == ['item']
    assert listify_lookup_plugin_terms(['item'], templar, loader=None) == ['item']
    assert listify_lookup_plugin_terms('{{item}}', templar, loader=None) == ['item']
    assert listify_lookup_plugin_terms(['{{item}}'], templar, loader=None) == ['item']
   

# Generated at 2022-06-13 16:33:48.653044
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    # Test string
    terms = '{{ lookup_string }}'
    result = listify_lookup_plugin_terms(terms, templar, loader)
    assert isinstance(result, list)
    assert result == [u'lookup_string_value']

    # Test True
    terms = True
    result = listify_lookup_plugin_terms(terms, templar, loader)
    assert isinstance(result, list)
    assert result == [True]

    # Test string with separator
    terms = '{{ lookup_string | join(",") }}'
    result = listify_lookup_plugin_terms(terms, templar, loader)
    assert isinstance(result, list)
    assert result == ['lookup_string_value1,lookup_string_value2,lookup_string_value3']



# Generated at 2022-06-13 16:33:56.407466
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    terms = listify_lookup_plugin_terms(['a', 'b', 'c'], templar=None, loader=None)
    assert len(terms) == 3
    assert terms[0] == 'a'
    assert terms[1] == 'b'
    assert terms[2] == 'c'
    terms = listify_lookup_plugin_terms('a', templar=None, loader=None)
    assert len(terms) == 1
    assert terms[0] == 'a'

# Generated at 2022-06-13 16:34:05.535421
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    """Unit test for listify_lookup_plugin_terms function to make sure it returns a list"""
    from ansible.utils.display import Display
    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib

    display = Display()
    templar = Templar(loader=None, variables={}, vault_password=None)
    templar.set_available_variables(variables=dict())
    vault_secrets = {}
    vault = VaultLib(vault_secrets, 'foo', vault_password_file=None)
    loader = True

    terms = listify_lookup_plugin_terms('{{foo}}', templar, loader)
    assert isinstance(terms, list)
    assert terms == ['{{foo}}']


# Generated at 2022-06-13 16:34:14.136929
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.module_utils._text import to_text
    from ansible.template import Templar

    loader = DictDataLoader()
    templar = Templar(loader=loader)

    result = listify_lookup_plugin_terms(42, templar=templar, loader=loader)
    assert result == [42]

    result = listify_lookup_plugin_terms("42", templar=templar, loader=loader)
    assert result == ["42"]

    result = listify_lookup_plugin_terms("{{ [1, 2, 3] }}", templar=templar, loader=loader)
    assert result == [1, 2, 3]


# Generated at 2022-06-13 16:34:26.421501
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible import constants as C
    from ansible.template import Templar
    from ansible.template.vars import VarsModule
    from ansible.vars import VariableManager

    def test_template(value, fail_on_undefined):
        t = Templar(loader=None, variables=None)
        t._available_variables = {}
        t._add_tokens(value, fail_on_undefined)
        return t.template()

    # Init
    vars_mgr = VariableManager()

    # Setup Vars
    vars_mgr.set_module_vars(VarsModule({}))
    vars_mgr.update_vars({'omit': 'none'})
    vars_mgr.extra_vars = {}

    # Init Templar

# Generated at 2022-06-13 16:34:33.948647
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    loader = None
    templar = None
    fail_on_undefined = True
    convert_bare = False
    terms1 = [1, 2, 3, 4, 5]
    terms2 = '{{ a }}'
    terms3 = ['{{ a }}', '{{ b }}']

    ret = listify_lookup_plugin_terms(terms1, templar, loader, fail_on_undefined, convert_bare)
    assert ret == [1, 2, 3, 4, 5]