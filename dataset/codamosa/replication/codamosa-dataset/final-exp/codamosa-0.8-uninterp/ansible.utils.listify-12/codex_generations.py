

# Generated at 2022-06-13 16:25:13.108350
# Unit test for function listify_lookup_plugin_terms

# Generated at 2022-06-13 16:25:20.412079
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.utils.plugins import AnsiblePlugin, lookup_loader
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    class TestLookupPlugin(AnsiblePlugin):
        def __init__(self, input_data, loader, templar, **kwargs):
            self.input_data = input_data

    # The following test cases are needed to ensure that all code paths are covered

# Generated at 2022-06-13 16:25:29.103707
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.common._collections_compat import OrderedDict
    from ansible.template import Templar

    templar = Templar(loader=None)

    # The following are the expected values for the tests
    expected_no_fail = [['a', 'b', 'c'], 'a', 'b', 'c', '', 'a\nb\nc', '"a b"', None, []]
    expected_fail = [['a', 'b', 'c'], 'a', 'b', 'c', '', 'a\nb\nc', '"a b"', None, [], {}, {'a': 'b'}]

    # The following are the inputs used for the tests

# Generated at 2022-06-13 16:25:39.167594
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    terms = [u'ansible', u'is', u'awesome']
    templar = Templar(loader=None)
    assert terms == listify_lookup_plugin_terms(terms, templar, loader=None)

    terms = u'ansible is awesome'
    templar = Templar(loader=None)
    assert [u'ansible is awesome'] == listify_lookup_plugin_terms(terms, templar, loader=None)

    terms = [u'ansible', u'is', u'%s' % u'awesome']
    templar = Templar(loader=None)
    assert terms == listify_lookup_plugin_terms(terms, templar, loader=None)

    def bar(self):
        pass

# Generated at 2022-06-13 16:25:51.892839
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    import ansible.template
    from ansible.parsing.yaml.objects import AnsibleUnicode

    def my_loader(name):
        return name

    # Empty term
    terms = None
    templar = ansible.template.Templar(loader=my_loader)
    result = listify_lookup_plugin_terms(terms, templar)
    assert result == [], "check for empty string did not pass"

    # Check for single term
    terms = "foo"
    result = listify_lookup_plugin_terms(terms, templar)
    assert result == ['foo'], "check for single term did not pass"

    # Check for single unicode term
    terms = AnsibleUnicode('foo')
    result = listify_lookup_plugin_terms(terms, templar)

# Generated at 2022-06-13 16:26:01.113574
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    loader = DictDataLoader({})
    templar = Templar(loader=loader)
    ret = listify_lookup_plugin_terms("hello", templar, loader)
    assert ret == ['hello']

    templar = Templar(loader=loader, variables={'n': 1})
    ret = listify_lookup_plugin_terms("hello", templar, loader)
    assert ret == ['hello']

    loader = DictDataLoader({})
    templar = Templar(loader=loader, variables={'n': 1})
    ret = listify_lookup_plugin_terms("hello.{{n}}", templar, loader)
    assert ret == ['hello.1']

    loader = DictDataLoader({'foo': 'bar'})

# Generated at 2022-06-13 16:26:11.899366
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    # NOTE: curt-baker: These tests should be overhauled to be more in line with the
    # current workings of the function. But doing that right now is not feasible.

    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.yaml.objects import AnsibleSequence

    terms = u"{{ lookup('file', 'does-not-exist.txt') }}"
    templar = Templar(loader=None)

    result = listify_lookup_plugin_terms(terms, templar, loader=None, fail_on_undefined=True)

    # TODO: curt-baker: These tests should be overhauled to be more in line with the
    # current workings of the function. But doing that right now is not feasible.

# Generated at 2022-06-13 16:26:20.415375
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.errors import AnsibleError
    from ansible.plugins.loader import lookup_loader

    my_vault_secret = "secret"


# Generated at 2022-06-13 16:26:31.885484
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    # Unit test requires the following items in the loader (mock_loader)
    #
    #      - a vars section with a list
    #      - a vars section with a string
    #      - a template with a list
    #      - a template with a string
    #      - a template with a variable reference to the string
    #      - a template with a variable reference to the list
    #
    # This should cover the scenarios where a lookup is called with either a
    # string or list and both contain variable references and not.

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.template import Templar

    mock_loader = DataLoader()
    mock_loader.set_basedir('/')

    mock_vars = VariableManager()
    mock_v

# Generated at 2022-06-13 16:26:41.741582
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    '''
    Test the listify_lookup_plugin_terms function
    '''

    from ansible.errors import AnsibleError
    from ansible.template import Templar

    class FakeVarManager:
        def get_vars(self, loader, play, host, task):
            return dict()

    class FakeHost:
        def get_name(self):
            return "test_host"

    class FakeV2Task:
        def __init__(self):
            self.name = "test_task"
            self._variable_manager = FakeVarManager()
            self._hosts = [FakeHost()]

    class FakePlayContext:
        def __init__(self):
            self._task = FakeV2Task()

    class FakeVarsModule:
        def __init__(self, data):
            self.data = data

# Generated at 2022-06-13 16:26:44.126655
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    return None

# Generated at 2022-06-13 16:26:50.914426
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    from ansible.template import Templar

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list=[])
    play_context = {}

    # setup context for templar
    variable_manager.set_inventory(inventory)
    variable_manager.extra_vars = {'foo': 'bar'}
    variable_manager.options_vars = {'something': 'nothing'}
    playbook = Play().load({}, variable_manager=variable_manager, loader=loader)

# Generated at 2022-06-13 16:26:51.941463
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    # TODO: target this file via coverage
    pass

# Generated at 2022-06-13 16:27:02.362500
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template.safe_eval import unsafe_eval
    from ansible.template import Templar

    class LookupModule(object):
        def __init__(self, basedir=None, **kwargs):
            pass

        def get_basedir(self, variables):
            return '.'

    loader = 'some_loader'

    def test_data(terms, expected, convert_bare=False, fail_on_undefined=True):
        templar = Templar(loader=loader, variables={'a': 'value_of_a', 'b': 'value_of_b'})
        result = listify_lookup_plugin_terms(terms, templar, loader, fail_on_undefined=fail_on_undefined, convert_bare=convert_bare)
        assert unsafe_eval(repr(result)) == expected

# Generated at 2022-06-13 16:27:09.425739
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    import ansible.template
    templar = ansible.template.Templar()

    assert [ 'h' ] == listify_lookup_plugin_terms('h', templar, None)
    assert [ 'h' ] == listify_lookup_plugin_terms(['h'], templar, None)
    assert [ 'h' ] == listify_lookup_plugin_terms(('h',), templar, None)
    assert [ '1', '2' ] == listify_lookup_plugin_terms("1, 2", templar, None)
    assert [ '1', '2' ] == listify_lookup_plugin_terms(["1", "2"], templar, None)

# Generated at 2022-06-13 16:27:19.100967
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock import patch, Mock

    loader = Mock()
    templar = Mock()

    # No changes if terms is a list
    terms = [1, 2, 3]
    result = listify_lookup_plugin_terms(terms, templar, loader)
    assert result == terms

    # Stringify a string
    templar.template.return_value = "abc"
    result = listify_lookup_plugin_terms("abc", templar, loader)
    assert result == ["abc"]

    # Templar a string
    templar.template.return_value = "abcd"
    result = listify_lookup_plugin_terms("{{abc}}", templar, loader)

# Generated at 2022-06-13 16:27:28.543944
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    import ansible.parsing.yaml.objects

    assert listify_lookup_plugin_terms(
        'a b',
        None, None,
    ) == ['a', 'b']

    assert listify_lookup_plugin_terms(
        'a b',
        None, None,
        fail_on_undefined=False,
    ) == ['a', 'b']

    assert listify_lookup_plugin_terms(
        'a b',
        None, None,
        fail_on_undefined=False,
        convert_bare=True,
    ) == ['a', 'b']


# Generated at 2022-06-13 16:27:40.784960
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play

    dataloader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=dataloader, variable_manager=variable_manager)
    play_context = Play()
    play_context.variable_manager = variable_manager

    templar = Templar(loader=dataloader, variables=variable_manager, play_context=play_context)
    templar._available_variables = dict(name='foo')


# Generated at 2022-06-13 16:27:50.172373
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.vault import VaultLib

    templar = Dictable()
    terms = ['a', 'b', 'c']
    desired_result = ['a', 'b', 'c']

    # Just a simple case
    result = listify_lookup_plugin_terms(terms, templar, None, fail_on_undefined=True, convert_bare=False)
    assert result == desired_result

    # Confirm that it still works as expected when type is string
    result = listify_lookup_plugin_terms('a', templar, None, fail_on_undefined=True, convert_bare=False)
    assert result == ['a']

    # Confirm that it fails if the template is garbage

# Generated at 2022-06-13 16:28:01.709591
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible import errors
    from ansible.vars import VariableManager
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = variable_manager.get_inventory()
    variable_manager.set_inventory(inventory)

    templar = Templar(loader=loader, variables=variable_manager)

    import pytest

    # succeed with single bare var
    result = listify_lookup_plugin_terms('{{ foo }}', templar, loader)
    assert result == ['bar']

    # fail with single bare var

# Generated at 2022-06-13 16:28:16.373923
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.common.collections import is_sequence

    test1_data =  {'simple': 'simple',
                   'list_string': ['a list that is a string'],
                   'list_list': ['a list that is a list'],
                   'list': ['a list'],
                   'complex': 'k=v',
                  }
    test1_result = {'simple': ['simple'],
                    'list_string': ['a list that is a string'],
                    'list_list': ['a list that is a list'],
                    'list': ['a list'],
                    'complex': ['k=v'],
                   }


# Generated at 2022-06-13 16:28:25.167027
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    import os
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    inventory_dir = os.path.join(cur_dir, '../../../test/unit/ansible_collections/ansible/netcommon/tests/unit/inventory')
    inventory = InventoryManager(loader=loader, sources=[os.path.join(inventory_dir, 'test_inventory')])
    inventory.subset('test_group')
    variable_manager = VariableManager(loader=loader, inventory=inventory)


# Generated at 2022-06-13 16:28:32.825295
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    class FakeVars(dict):
        def __init__(self):
            self._data = {
                'var1': 'value1',
                'var2': [ 'value2a', 'value2b' ],
                'var3': 'value3'
            }

    class FakeVarManager():
        def get_vars(self):
            return FakeVars()

    t = Templar(loader=None, variables=FakeVarManager())

    assert listify_lookup_plugin_terms(['var1'], t, None) == ['value1']

    assert listify_lookup_plugin_terms(['var2'], t, None) == ['value2a', 'value2b']


# Generated at 2022-06-13 16:28:42.916388
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    import jinja2

    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    from ansible.errors import AnsibleError

    from ansible.playbook.play_context import PlayContext

    from ansible.module_utils.six import string_types

    from ansible.module_utils.common._collections_compat import Iterable

    def test_data(terms, expected, fail_on_undefined=True, convert_bare=False):

        class TestVarsModule:

            def get_vars(self, loader, play, host):
                return {}

        class TestPlayContext(PlayContext):
            pass


# Generated at 2022-06-13 16:28:49.707783
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.vault import VaultLib
    from ansible.template import Templar
    from ansible.template.safe_eval import safe_eval

    my_vault_secret = VaultLib([])

# Generated at 2022-06-13 16:29:00.766127
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    class VarsModule(object):
        def __init__(self):
            self.hostvars = {}
        def get_vars(self, loader, path, entities, cache=True):
            return self.hostvars

    loader_mock = VarsModule()

    results = listify_lookup_plugin_terms('foo', Templar(loader=loader_mock, shared_loader_obj=loader_mock, variables={}))
    assert results == ['foo']

    results = listify_lookup_plugin_terms(['foo'], Templar(loader=loader_mock, shared_loader_obj=loader_mock, variables={}))
    assert results == ['foo']

if __name__ == '__main__':
    test_listify_lookup_plugin_terms()


# Generated at 2022-06-13 16:29:10.309896
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    templar = Templar(loader=None)

    # test strings
    assert listify_lookup_plugin_terms('foo', templar, None) == ['foo']
    assert listify_lookup_plugin_terms('foo,bar', templar, None) == ['foo', 'bar']
    assert listify_lookup_plugin_terms('foo , bar', templar, None) == ['foo', 'bar']
    assert listify_lookup_plugin_terms('foo, bar', templar, None) == ['foo', 'bar']
    assert listify_lookup_plugin_terms('foo ,bar', templar, None) == ['foo', 'bar']

    # test lists

# Generated at 2022-06-13 16:29:20.409098
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    # pylint: disable=unused-variable
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    loader = None
    variable_manager = VariableManager()
    templar = Templar(loader=loader, variables=variable_manager)

    # Single string input
    single_string = "{{lookup_plugin_test_var1}}"
    list_from_single_string = listify_lookup_plugin_terms(single_string, templar, loader)
    assert isinstance(list_from_single_string, list)
    assert isinstance(list_from_single_string[0], string_types)
    assert list_from_single_string[0] == "lookup_plugin_test_value1"

    # Single list input

# Generated at 2022-06-13 16:29:30.404722
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.template import Templar
    from ansible.template.safe_eval import safe_eval
    from ansible.vars import VariableManager

    variable_manager = VariableManager()
    variable_manager.set_nonpersistent_facts(dict(a='a', b='b', c='c', d='d'))

    loader = variable_manager.get_vars_loader()

    # Test 1: Test escaped terms
    terms = ['1', '2', '3']
    expected = ['1', '2', '3']
    templar = Templar(loader, variable_manager)
    result = listify_lookup_plugin_terms(terms, templar, loader)
    assert type(result) == list
    assert result == expected

   

# Generated at 2022-06-13 16:29:39.492474
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.vault import VaultLib
    from ansible.errors import AnsibleError
    from ansible.utils.vars import combine_vars

    myvars = VariableManager()
    myvars.extra_vars = {'a': 'foobar', 'b': ['foo', 'bar']}
    myloader = DictDataLoader({})
    myvault = VaultLib([])
    mytemplar = Templar(loader=myloader, variables=myvars, vault_secrets=myvault)

    assert listify_lookup_plugin_terms('{{ a }}', mytemplar, myloader) == ['foobar']

# Generated at 2022-06-13 16:29:51.508903
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    templar = Templar(loader=None, variables={})

    # String
    assert listify_lookup_plugin_terms('foo', templar, None) == ['foo']
    # List
    assert listify_lookup_plugin_terms(['foo'], templar, None) == ['foo']
    # List with vars
    assert listify_lookup_plugin_terms(['foo', '{{ foo }}'], templar, None) == ['foo', '{{ foo }}']

# Generated at 2022-06-13 16:30:00.634138
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    t = Templar(loader=DataLoader())

    assert listify_lookup_plugin_terms('a', t, t, fail_on_undefined=False) == ['a']
    assert listify_lookup_plugin_terms('a b c', t, t, fail_on_undefined=False) == ['a b c']
    assert listify_lookup_plugin_terms('a "a b---c"', t, t, fail_on_undefined=False) == ['a "a b---c"']
    assert listify_lookup_plugin_terms('"a b---c"', t, t, fail_on_undefined=False) == ['"a b---c"']
    assert listify_lookup_

# Generated at 2022-06-13 16:30:08.283614
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    class TestVarsModule(object):

        def __init__(self, loader):
            self._loader = loader

        def vars(self, inject=None):
            return dict(a=1, b=2)

    class TestTemplar(Templar):

        def __init__(self, loader, sproxy):
            super(TestTemplar, self).__init__(loader)
            self._sproxy = sproxy

        def _add_toplevel_vars(self, vars):
            vars['s'] = self._sproxy

    class TestLoader(object):

        def __init__(self):
            self._vars_proxy = TestVarsModule(self)

        @property
        def vars(self):
            return self._vars_proxy

   

# Generated at 2022-06-13 16:30:17.682937
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    v = VaultLib(['--vault-password-file', '.vaultpass'])
    variable_manager = VariableManager()
    loader = variable_manager.get_vars_loader()
    variable_manager.set_inventory(InventoryManager(loader=loader, sources=['tests/inventory']))
    variable_manager.extra_vars = load_extra_vars(loader=loader, options=dict(vault_password='secret'))

   

# Generated at 2022-06-13 16:30:29.229764
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch, MagicMock

    class UtilsTestCase(unittest.TestCase):

        def setUp(self):
            pass

        def tearDown(self):
            pass

        @patch('ansible.module_utils.common.listify_lookup_plugin_terms')
        def test_listify_lookup_plugin_terms_string(self, mock_listify_lookup_plugin_terms):
            templar = MagicMock()
            loader = MagicMock()
            fail_on_undefined = True
            convert_bare = True
            terms = "Hello World"

# Generated at 2022-06-13 16:30:40.482229
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    # Test when lookup term is a scalar string
    scalar_string = ['foo']
    assert listify_lookup_plugin_terms('foo', None, None) == scalar_string

    # Test when lookup term is a list of strings
    list_of_strings = ['foo', 'bar']
    assert listify_lookup_plugin_terms(list_of_strings, None, None) == list_of_strings

    # Test when lookup term is a list of unicode and strings
    list_of_unicode_and_strings = ['foo', u'bar']
    assert listify_lookup_plugin_terms(list_of_unicode_and_strings, None, None) == list_of_unicode_and_strings

    # Test when lookup term is a list of non-strings (even though this is likely a bug elsewhere)


# Generated at 2022-06-13 16:30:46.210362
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    templar = Templar(loader=DataLoader())

    assert listify_lookup_plugin_terms('foo', templar, DataLoader()) == ['foo']
    assert listify_lookup_plugin_terms(['foo'], templar, DataLoader()) == ['foo']
    assert listify_lookup_plugin_terms(['foo', 'bar'], templar, DataLoader()) == ['foo', 'bar']
    assert listify_lookup_plugin_terms((x for x in ['foo', 'bar']), templar, DataLoader()) == ['foo', 'bar']
    assert listify_lookup_plugin_terms('{{foo}}', templar, DataLoader(), convert_bare=True) == ['foo']


# Generated at 2022-06-13 16:30:56.133054
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.utils.vault import VaultAES256

    terms = [1, 2, 3]
    templar = Templar(vault_secrets=VaultLib([('password', VaultAES256('password'))]))
    loader = AnsibleVaultEncryptedUnicode()
    # test only type is Iterable
    result = listify_lookup_plugin_terms(terms, templar, loader)
    assert result == terms

    string = 'test'
    templar = Templar(vault_secrets=VaultLib([('password', VaultAES256('password'))]))
    loader = Ansible

# Generated at 2022-06-13 16:31:07.851118
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils._text import to_text

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.template import Templar

    loader = DataLoader()
    variable_manager = VariableManager()

    plugin_options = {u'_data': {u'vars': {u'a': u'1', u'b': u'2', u'c': [3, 4, 5], u'd': 6}}, u'_ansible_version': u'2.1.1.0', u'_ansible_no_log': False, u'_ansible_debug': False, u'_ansible_verbosity': 0}
    variable_manager.extra_vars = plugin_options.get('vars', {})
    variable_manager.options

# Generated at 2022-06-13 16:31:14.547442
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    loader = DictDataLoader({})
    templar = Templar(loader=loader)

    assert [] == listify_lookup_plugin_terms(None, templar, loader)
    assert [] == listify_lookup_plugin_terms([], templar, loader)
    assert ['42'] == listify_lookup_plugin_terms(42, templar, loader)
    assert ['42'] == listify_lookup_plugin_terms('42', templar, loader)
    assert ['42'] == listify_lookup_plugin_terms(['42'], templar, loader)
    assert ['42'] == listify_lookup_plugin_terms(['42', '43'], templar, loader)
    assert ['42', '43'] == listify_lookup_plugin

# Generated at 2022-06-13 16:31:38.243782
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DictDataLoader({})
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources='')
    variable_manager.set_inventory(inventory)

    templar = Templar(loader=loader, variables=variable_manager)

    assert listify_lookup_plugin_terms("some string", templar, loader) == ["some string"]
    assert listify_lookup_plugin_terms(["some string"], templar, loader) == ["some string"]
    assert listify_lookup_plugin_terms(("some string",), templar, loader) == ["some string"]

# Generated at 2022-06-13 16:31:45.698422
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    import ansible.parsing.yaml.loader
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    loader = ansible.parsing.yaml.loader.AnsibleLoader
    play_context = PlayContext()
    templar_args = dict(loader=loader, variables={}, fail_on_undefined=True)
    templar = Templar(**templar_args)

    var_manager = VariableManager()
    var_manager.set_inventory(None)
    templar._add_tqm_variables(var_manager, play_context)

    assert listify_lookup_plugin_terms([1], templar, loader) == [1]
    assert listify_lookup_plugin

# Generated at 2022-06-13 16:31:53.769195
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    templar = Templar(loader=DataLoader(), variables=VariableManager(), shared_loader_obj=None)
    templar.set_available_variables(dict(a=1))

    assert listify_lookup_plugin_terms('{{ a }}', templar, DataLoader()) == [1]
    assert listify_lookup_plugin_terms(['{{ a }}'], templar, DataLoader()) == [1]
    assert listify_lookup_plugin_terms('1', templar, DataLoader()) == ['1']

# Generated at 2022-06-13 16:32:01.755310
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.vars import VariableManager

    vars_manager = VariableManager()
    loader = vars_manager.loader
    templar = Templar(loader=loader, variables=vars_manager, fail_on_undefined=True)

    # Test a string or a list
    assert listify_lookup_plugin_terms('foo', templar, loader) == ['foo']
    assert listify_lookup_plugin_terms(['foo', 'bar'], templar, loader) == ['foo', 'bar']

    # Test Jinja2 templates
    assert listify_lookup_plugin_terms('{{ foo }}', templar, loader) == ['foo']
    assert listify_lookup_plugin_terms('{{ "foo" }}', templar, loader) == ['foo']


# Generated at 2022-06-13 16:32:13.118705
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    class DummyVarsModule(object):
        def __init__(self, loader, items=None):
            if items:
                self.items = items

        def get_vars(self, loader, play, host, task):
            return dict(self.items)
    class DummyVarsManager(object):
        def __init__(self):
            self.loaders = {}
            self.host_vars = {}
            self.group_vars = {}
            self.play = None
            self.playbook = None

        def add_loader(self, loader):
            self.loaders[loader.get_basedir()] = loader


# Generated at 2022-06-13 16:32:22.582537
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible import context
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleUnicode

    class FakeVaultSecret(object):
        def __init__(self, secret):
            self.secret = secret

    class FakeVaultLib(object):
        vault_secrets = [FakeVaultSecret('fake_vault_secret')]

        def decrypt(self, value):
            return self.vault_secrets.pop(0).secret

    class FakeLoader(object):
        pass

    class FakeTemplar(object):
        loader = FakeLoader()

# Generated at 2022-06-13 16:32:32.408459
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    loader = None
    templar = Templar(loader=loader, variables={'ansible_host': '10.1.2.3', 'ansible_distribution': 'RedHat'})

    # Test that a simple string is turned into a list
    terms = "http://{{ ansible_host }}/{{ ansible_distribution }}"
    results = listify_lookup_plugin_terms(terms, templar, loader)
    assert results == ['http://10.1.2.3/RedHat']

    # Test that a list of strings is used as is
    terms = ['http://{{ ansible_host }}/{{ ansible_distribution }}', 'http://{{ ansible_host }}/{{ ansible_distribution }}']

# Generated at 2022-06-13 16:32:40.808920
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.vars import VariableManager

    my_var = dict(a=1)
    variable_manager = VariableManager()
    variable_manager.set_nonpersistent_facts(my_var)
    templar = Templar(loader=None, variables=variable_manager)

    # Test to see if string terms are converted to a list
    string_terms = "{{ a }}"
    list_terms = listify_lookup_plugin_terms(string_terms, templar, loader=None)
    assert len(list_terms) == 1
    assert isinstance(list_terms, list)
    assert list_terms[0] == 1

    # Test to see if complex terms are converted to a list
    complex_terms = [1, '{{ a }}']
    list_terms = listify

# Generated at 2022-06-13 16:32:43.039029
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    '''
    ansible/test/units/modules/utils/test_lookup_plugins.py
    '''
    pass

# Generated at 2022-06-13 16:32:50.948909
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.template import Templar

    class LookupModule:
        def __init__(self, basedir=None, runner=None, inject=None, **kwargs):
            pass

    loader = LookupModule()
    templar = Templar(loader=loader)
    terms = ['foo', 'bar', 'baz', 'bat']

# Generated at 2022-06-13 16:33:25.323306
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    class DummyVarsModule(object):
        def vars(self):
            return dict()

        def get_vars(self, loader, play, host, task):
            return dict()
 
    def _get_templar(vars_loader=None, shared_loader_obj=None, variables=None):
        ''' Return a Templar object populated with fake state'''
        loader = DataLoader()
        if vars_loader is None:
            vars_loader = DummyVarsModule()

        if shared_loader_obj is None:
            shared_loader_obj = []

        if variables is None:
            variables = dict()

        templar = Templar(loader=loader, variables=variables)
       

# Generated at 2022-06-13 16:33:37.307369
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib
    from ansible.vars.manager import VariableManager

    fake_loader = DictDataLoader({
        "var": "infile"
    })
    fake_vault_secrets = dict(
        vault_password="vaultpass"
    )
    vault_secrets_loader = DictDataLoader(fake_vault_secrets)

    # Test string input
    templar = Templar(loader=fake_loader, variable_manager=VariableManager(), vault_secrets=vault_secrets_loader)
    assert listify_lookup_plugin_terms(' {{ var }} ', templar) == ['infile'], "single string term"

# Generated at 2022-06-13 16:33:46.911035
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    import ansible.parsing.yaml.loader

    terms = [1,2,3, {'foo': 'bar'}]
    templar = Templar(loader=ansible.parsing.yaml.loader.AnsibleLoader)
    templar._available_variables = dict(foo='bar')
    templar.available_variables = dict(foo='bar')

    # Check that the function doesn't change the list
    listified = listify_lookup_plugin_terms(terms, templar, None)
    assert terms == listified

    # Now, check that we do expand things properly
    terms = [1,2,3, "{{ foo }}"]
    listified = listify_lookup_plugin_terms(terms, templar, None)

# Generated at 2022-06-13 16:33:59.114697
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    '''
    Test listify_lookup_plugin_terms
    '''
    import ansible.module_utils.common.collections
    from ansible.parsing.yaml.objects import AnsibleUnicode

    assert listify_lookup_plugin_terms(
        ['001', '002'],
        None,
        None,
        fail_on_undefined=True,
        convert_bare=False
    ) == ['001', '002']

    assert listify_lookup_plugin_terms(
        '001',
        None,
        None,
        fail_on_undefined=True,
        convert_bare=False
    ) == ['001']


# Generated at 2022-06-13 16:34:09.079314
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.module_utils.common._collections_compat import assertCountEqual
    from ansible.template import Templar

    terms = "{{ hostvars['localhost'].ansible_ssh_host }}"
    templar = Templar(loader=None, variables={'hostvars': {'localhost': {'ansible_ssh_host': '127.0.0.1'}}})

    result = listify_lookup_plugin_terms(terms, templar, None, fail_on_undefined=True, convert_bare=False)

    assert result == ['127.0.0.1']

    all_the_vars = {'a': 'A', 'b': 'B', 'c': 'C'}
    templar = Templar(loader=None, variables=all_the_vars)


# Generated at 2022-06-13 16:34:16.842439
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.template import Templar
    import ansible.constants as C


# Generated at 2022-06-13 16:34:28.797532
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible import template
    from ansible.template import Templar
    from ansible.parsing.yaml.loader import AnsibleLoader
    import pytest

    loader = AnsibleLoader(None, None)
    templar = Templar(loader=loader, variables={'a': ['b', 'c']})

    term = 'foo'
    result = listify_lookup_plugin_terms(term, templar)
    assert result == ['foo']

    term = ['foo', 'bar']
    result = listify_lookup_plugin_terms(term, templar)
    assert result == ['foo', 'bar']

    term = '{{a}}'
    result = listify_lookup_plugin_terms(term, templar, fail_on_undefined=False)
    assert result == ['b', 'c']

# Generated at 2022-06-13 16:34:38.281788
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    # Basic tests
    assert listify_lookup_plugin_terms(1) == [1]
    assert listify_lookup_plugin_terms([1]) == [1]
    assert listify_lookup_plugin_terms([1,2]) == [1,2]
    assert listify_lookup_plugin_terms({'foo': 'bar'}) == [{'foo': 'bar'}]
    assert listify_lookup_plugin_terms('foo') == ['foo']
    assert listify_lookup_plugin_terms([]) == []

    # Test with template string
    from ansible.template import Templar
    from ansible.parsing.yaml.loader import AnsibleLoader
    l = AnsibleLoader(None)

# Generated at 2022-06-13 16:34:48.224325
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    # Test that passing a string returns a list of one element
    templar = Templar(loader=None)

    assert listify_lookup_plugin_terms('test', templar, None) == ['test']

    # Test that passing a list returns a list with the same elements
    input = ['test1', 'test2', 'test3']
    assert listify_lookup_plugin_terms(input, templar, None) == input

    # Test that passing a list of lists returns a flattened list
    input = [['test1', 'test2'], ['test3'], 'test4', ['test5']]
    assert listify_lookup_plugin_terms(input, templar, None) == ['test1', 'test2', 'test3', 'test4', 'test5']

   

# Generated at 2022-06-13 16:34:57.728883
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    import sys
    import os
    import tempfile
    import shutil
    import json
    import yaml

    if not os.path.exists('/tmp/ansible_test_file'):
        test_file = tempfile.mkstemp()[1]
    else:
        test_file = '/tmp/ansible_test_file'

    # write a test Ansible inventory file to a temporary directory
    test_inventory = open(test_file, 'w')