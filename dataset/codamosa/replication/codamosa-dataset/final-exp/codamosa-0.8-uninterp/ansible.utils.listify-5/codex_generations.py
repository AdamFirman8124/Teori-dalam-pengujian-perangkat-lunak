

# Generated at 2022-06-13 16:25:06.439730
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    assert listify_lookup_plugin_terms('foo, bar', Templar(), None) == ['foo', 'bar']

# Generated at 2022-06-13 16:25:15.502993
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar
    from ansible.parsing.utils.addresses import parse_address
    from ansible.vars.manager import VariableManager

    loader = DictDataLoader({})
    inventory = Inventory(loader=loader, variable_manager=VariableManager(loader=loader), host_list=[])
    templar = Templar(loader=loader, variables=inventory.get_variables())


# Generated at 2022-06-13 16:25:26.274626
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar

    loader = DataLoader()
    # test a simple string
    assert listify_lookup_plugin_terms('foo', Templar(loader=loader), loader, False) == ['foo']
    # test a simple string with whitespace and convert_bare
    assert listify_lookup_plugin_terms(' foo ', Templar(loader=loader), loader, False, True) == ['foo']
    # test a list with strings

# Generated at 2022-06-13 16:25:38.047163
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from unit.compat import unittest
    from unit.compat.mock import MagicMock, patch
    from ansible.template import Templar

    class TestListifyLookupPluginTerms(unittest.TestCase):

        def setUp(self):
            self.loader = MagicMock()
            self.templar = Templar(loader=self.loader, variables={})

        @patch.object(Templar, 'template')
        def test_listify_lookup_plugin_terms_string(self, template):
            template.return_value = 'str'

            terms = 'str'
            result = listify_lookup_plugin_terms(terms, self.templar, self.loader)

            self.assertEqual(['str'], result)

# Generated at 2022-06-13 16:25:43.021411
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    assert listify_lookup_plugin_terms(None) == []
    assert listify_lookup_plugin_terms(42) == [42]
    assert listify_lookup_plugin_terms('a') == ['a']
    assert listify_lookup_plugin_terms('') == []
    assert listify_lookup_plugin_terms(['a' , 'b']) == ['a', 'b']
    assert listify_lookup_plugin_terms(['a', ['b', 'c']]) == ['a', ['b', 'c']]

# Generated at 2022-06-13 16:25:54.714650
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext

    loader = DummyLoader()
    templar = Templar(loader=loader, variables=VariableManager(loader=loader, inventory=InventoryManager(loader=loader)))

    # Test converting a string to a list:
    assert ["a_string"] == listify_lookup_plugin_terms("a_string", templar, loader)

    # Test converting a term to a list
    assert [1] == listify_lookup_plugin_terms(1, templar, loader)

    # Test converting a list to a list
    assert [1,2,3] == list

# Generated at 2022-06-13 16:26:00.625164
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    # empty value
    assert listify_lookup_plugin_terms(None, None, None) == []

    # non-list value
    assert listify_lookup_plugin_terms('one', None, None) == ['one']

    # list value
    assert listify_lookup_plugin_terms(['one'], None, None) == ['one']

    # list of lists value
    assert listify_lookup_plugin_terms([['one'], ['two']], None, None) == [['one'], ['two']]

# Generated at 2022-06-13 16:26:11.742004
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext

    loader = DataLoader()

    variable_manager = VariableManager()
    variable_manager.extra_vars = {'blah': 'foo'}
    variable_manager.set_inventory(loader.load_from_file('tests/inventory'))

    host = Host(name="foo")
    templar = Templar(loader=loader, variables=variable_manager,
                      shared_loader_obj=loader, host=host)

    play_context = PlayContext()

# Generated at 2022-06-13 16:26:20.269591
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib
    from ansible.utils.vars import combine_vars

    class FakeVaultSecret(object):
        def __init__(self, sec):
            self.sec = sec

        def load(self):
            return self.sec

    class FakeVault(VaultLib):
        def __init__(self, loader):
            super(FakeVault, self).__init__(None, loader)
            self.secrets = {}

        def set_secret(self, path, secret):
            self.secrets[path] = FakeVaultSecret(secret)

        def get_secret(self, path):
            return self.secrets.get(path)

        def is_encrypted(self, data):
            return False


# Generated at 2022-06-13 16:26:28.168536
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    try:
        from ansible.template import Templar
        from ansible.parsing.yaml.loader import AnsibleLoader
        from ansible.utils.unsafe_proxy import AnsibleUnsafeText
        terms = AnsibleUnsafeText(u'{{foo}}')
        templar = Templar(loader=AnsibleLoader())
        result = listify_lookup_plugin_terms(terms, templar, loader=AnsibleLoader())
    except ImportError:
        raise AssertionError()
    assert u'{{foo}}' in result

# Generated at 2022-06-13 16:26:38.499604
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.yaml.loader import AnsibleLoader

    templar = Templar(loader=AnsibleLoader(None, '.'))

    # test string
    assert listify_lookup_plugin_terms('foo', templar, '', fail_on_undefined=True) == ['foo']
    assert listify_lookup_plugin_terms('{{ foo }}', templar, '', fail_on_undefined=True) == ['{{ foo }}']
    assert listify_lookup_plugin_terms('{{ foo }}', templar, '', fail_on_undefined=False) == ['foo']

# Generated at 2022-06-13 16:26:47.046868
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    class FakeVarsModule(object):
        def __init__(self, values):
            self.values = values

        def __getitem__(self, key):
            return self.values[key]


    class FakeLoader(object):
        def get_basedir(self, host):
            return ""

    templar = Templar(loader=FakeLoader(), variables=FakeVarsModule({"a": {'b':'c', 'd':'e'}}))

    assert 'a' == listify_lookup_plugin_terms("{{a}}", templar, FakeLoader())[0]
    assert 'b' == listify_lookup_plugin_terms(['a', 'b', 1], templar, FakeLoader())[1]
    assert 1 == listify_lookup_plugin_

# Generated at 2022-06-13 16:26:52.638901
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.common.collections import AnsibleMapping, AnsibleSequence, AnsibleUnicode

    class Templar(object):
        def __init__(self, loader=False, variables={}):
            self.loader = loader
            self.variables = variables
            # If loader=True, this is the "source" function being used by the templar
            if self.loader:
                def tmpl(data, fail_on_undefined=True, convert_bare=False, preserve_trailing_newlines=True, **kwargs):
                    return data
                self.template = tmpl
            else:
                def tmpl(data, fail_on_undefined=True):
                    if isinstance(data, AnsibleMapping):
                        for k in data:
                            data[k] = self

# Generated at 2022-06-13 16:27:01.980379
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible import module_utils
    loaders = module_utils.module_loader._get_module_loader()
    for terms in [
            'foobar',                                              # str
            [ 'foo', 'bar' ],                                      # list
            [ '{{ foo }}', '{{ bar }}' ],                          # list of str
            [ '{{ foo }}', [ '{{ bar }}', [ 'baz' ] ] ],           # list of mixed levels
            { 'a': 'b', 'c': [ 'd', 'e' ] }                         # dict
    ]:
        assert listify_lookup_plugin_terms(terms, module_utils.template.AnsibleTemplar(loader=loaders))

# Generated at 2022-06-13 16:27:05.777483
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    # 'string' case
    assert listify_lookup_plugin_terms('{{ var }}', {}, {}, False) == ['{{ var }}']

    # Iterable case
    assert listify_lookup_plugin_terms(['a', 'b'], {}, {}, False) == ['a', 'b']

# Generated at 2022-06-13 16:27:16.469804
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.errors import AnsibleUndefinedVariable
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    assert listify_lookup_plugin_terms('file.txt', Templar(VariableManager()), None) == ['file.txt']
    assert listify_lookup_plugin_terms(['file1.txt', 'file2.txt'], Templar(VariableManager()), None) == ['file1.txt', 'file2.txt']

    # New in 2.4
    assert listify_lookup_plugin_terms('file.txt', Templar(VariableManager(loader=None)), None) == ['file.txt']

# Generated at 2022-06-13 16:27:26.569151
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.utils.vars import combine_vars

    from ansible.template import Templar
    from ansible.parsing.yaml.loader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()

    fake_loader = DataLoader()
    inventory = InventoryManager(loader=fake_loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=fake_loader, inventory=inventory)

    vars_dict = dict(a="A", b="B", c="{{a}}{{b}}")
    templar = Templar(loader=loader, variables=vars_dict)
    convert_bare = False



# Generated at 2022-06-13 16:27:29.545330
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    assert listify_lookup_plugin_terms("{{ test }}", None, None) == ["{{ test }}"]
    assert listify_lookup_plugin_terms(['foo'], None, None) == ['foo']
    assert listify_lookup_plugin_terms(['foo','bar'], None, None) == ['foo','bar']

# Generated at 2022-06-13 16:27:40.858026
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    # Test with unicode
    templar = Templar(loader=None, variables={'a': u'my ünicode string'})
    assert listify_lookup_plugin_terms(u'{{a}}', templar, None) == [u'my ünicode string']

    # Test with a tuple (a regular expression object will be a tuple)
    templar = Templar(loader=None, variables={'foo': (1, 2, 3)})
    assert listify_lookup_plugin_terms(u'{{foo}}', templar, None) == [(1, 2, 3)]

    # Test with a list
    templar = Templar(loader=None, variables={'foo': ['a', 'b', 'c']})
    assert listify_lookup_plugin_terms

# Generated at 2022-06-13 16:27:50.586320
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar

    loader = DataLoader()
    variable_manager = VariableManager()
    templar = Templar(loader=loader, variables=variable_manager)

    assert listify_lookup_plugin_terms(None, templar, loader) == [None]
    assert listify_lookup_plugin_terms([None], templar, loader) == [None]
    assert listify_lookup_plugin_terms(['1', '2', '3'], templar, loader) == ['1', '2', '3']
    assert listify_lookup_plugin_terms('1', templar, loader) == ['1']

# Generated at 2022-06-13 16:28:06.196962
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    '''
    For testing, set up a mocked templar
    '''
    # TODO: this doesn't test fail_on_undefined/convert_bare, as that probably needs
    # a slightly better mocked templar

    test_value = 'hello'
    terms = test_value

    class MockTemplar:
        def template(self, terms, fail_on_undefined=True, convert_bare=False):
            return terms

    templar = MockTemplar()

    # default is to return a list
    assert listify_lookup_plugin_terms(terms, templar, None) == [test_value]

    # same for a list of strings
    terms = [test_value, test_value]

# Generated at 2022-06-13 16:28:17.269764
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    
    from ansible.parsing.vault import VaultLib
    from ansible.template import Templar
    from ansible.playbook.play_context import PlayContext
    
    vault_pass = 'secret'
    templar = Templar(play_context=PlayContext, vault_password=VaultLib(vault_pass).decrypt)

    # test lookup term: '{{ lookup_passed_value }}'
    given_terms = '{{ lookup_passed_value }}'
    expected_terms = 'the_value_passed_to_lookup'
    lookup_passed_value = [expected_terms]

    actual_terms = listify_lookup_plugin_terms(given_terms, templar, lookup_passed_value)

    assert actual_terms == [expected_terms]

    # test lookup term: '

# Generated at 2022-06-13 16:28:25.743304
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    import os
    import pytest

    def assert_result(terms, expected):
        loader = DataLoader()
        templar = Templar(loader=loader)

        result = listify_lookup_plugin_terms(terms, templar, loader)

        assert result == expected

    terms = 'one, two, three'
    expected = ['one', 'two', 'three']
    assert_result(terms, expected)

    # test with trailing whitespace
    terms = 'one, two, three '
    expected = ['one', 'two', 'three']
    assert_result(terms, expected)

    # test with leading whitespace
    terms = ' one, two, three'

# Generated at 2022-06-13 16:28:36.656280
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    import pprint
    from ansible import constants as C
    from ansible.parsing.vault import VaultLib
    from ansible.template import Templar
    from ansible.utils.vars import combine_vars

    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager

    from ansible.inventory.manager import InventoryManager

    from ansible.plugins.loader import lookup_loader, lookup_loader

    from ansible.module_utils._text import to_native
    from ansible.module_utils.six import PY2

    if PY2:
        import sys
        reload(sys)
        sys.setdefaultencoding('utf8')

    C.HOST_KEY_CHECKING = False
    C.RETRY_FILES_ENABLED = False

    fake_loader

# Generated at 2022-06-13 16:28:45.922262
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    class TestVarsModule:
        def __init__(self, vars):
            self.vars = vars
        def run(self):
            return self.vars

    terms = "{{ var1 }}"
    templar = Templar(DataLoader(), variable_manager=VariableManager(loader=DataLoader()) )
    templar.set_available_variables( TestVarsModule({u'var1': u'value1'}).run() )

    terms = listify_lookup_plugin_terms( terms, templar, DataLoader() )

    assert terms == [u'value1']

# Generated at 2022-06-13 16:28:53.346311
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    '''
    ansible.utils.listify_lookup_plugin_terms unit tests
    :return:
    '''

    from ansible.template import Templar

    templar = Templar()

    # Test list
    assert listify_lookup_plugin_terms(['a', 'b', 'c'], templar, None) == ['a', 'b', 'c']

    # Test list with templating
    assert listify_lookup_plugin_terms(['a', 'b', '{{var}}'], templar, None, False, False) == ['a', 'b', '{{var}}']
    assert listify_lookup_plugin_terms(['a', 'b', '{{var}}'], templar, None, True, False) == ['a', 'b', '{{var}}']
    assert listify

# Generated at 2022-06-13 16:29:01.206758
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    class FakeTemplar(object):

        def __init__(self):
            pass

        def template(self, x, fail_on_undefined=True, convert_bare=False):
            return x

    class FakeLoader(object):

        def __init__(self):
            pass

        def get_basedir(self, x):
            return x

    f = FakeTemplar()
    fl = FakeLoader()
    assert listify_lookup_plugin_terms('string', f, fl) == ['string']
    assert listify_lookup_plugin_terms(['string'], f, fl) == ['string']

# Generated at 2022-06-13 16:29:10.519905
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.errors import AnsibleUndefinedVariable
    from ansible.template import Templar

    templar = Templar(loader=None, variables=dict(a=1))
    assert listify_lookup_plugin_terms('this', templar, None) == ['this']
    assert listify_lookup_plugin_terms(['this', 'that'], templar, None) == ['this', 'that']
    assert listify_lookup_plugin_terms('{{a}}', templar, None) == ['1']
    assert listify_lookup_plugin_terms('{{a}}', templar, None, convert_bare=True) == ['1']
    assert listify_lookup_plugin_terms('{{a}}', templar, None, convert_bare=False) == ['{{a}}']
    assert listify

# Generated at 2022-06-13 16:29:19.676364
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    test_terms = ['{{ ["1", "2"] | list }}', ['3', '4', '5']]
    final_terms = ['1', '2', '3', '4', '5']

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.template import Templar

    variable_manager = VariableManager()
    loader = DataLoader()

    templar = Templar(loader=loader, variables=variable_manager)
    templar._available_variables = dict()

    processed_terms = listify_lookup_plugin_terms(test_terms, templar, loader)
    assert processed_terms == final_terms

# Generated at 2022-06-13 16:29:30.221564
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    loader = DictDataLoader({})
    templar = Templar(loader=loader)
    assert listify_lookup_plugin_terms('a', templar, loader) == ['a']
    assert listify_lookup_plugin_terms(['a'], templar, loader) == ['a']
    assert listify_lookup_plugin_terms(['a', 'b'], templar, loader) == ['a', 'b']
    assert listify_lookup_plugin_terms('a,b', templar, loader) == ['a', 'b']
    assert listify_lookup_plugin_terms(['a,b'], templar, loader) == ['a', 'b']

# Generated at 2022-06-13 16:29:47.299306
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    class Options(object):
        def __init__(self, variables=None):
            if variables is None:
                self.__dict__['variables'] = dict()
            else:
                self.__dict__['variables'] = variables

        def __getitem__(self, key):
            return self.__dict__['variables'][key]

        def __setitem__(self, key, value):
            self.__dict__['variables'][key] = value

        def __contains__(self, key):
            return key in self.__dict__['variables']

        def __getattr__(self, key):
            try:
                return self.__dict__['variables'][key]
            except KeyError:
                raise AttributeError


# Generated at 2022-06-13 16:29:55.410272
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    templar = Templar(loader=None, variables={})
    assert listify_lookup_plugin_terms(None, templar, None) == [None]
    assert listify_lookup_plugin_terms([1,2,3], templar, None) == [1,2,3]
    assert listify_lookup_plugin_terms(['1','2','3'], templar, None) == ['1','2','3']

    assert listify_lookup_plugin_terms('1', templar, None) == ['1']
    assert listify_lookup_plugin_terms('1,2,3', templar, None) == ['1,2,3']
    assert listify_lookup_plugin_terms('1, 2, 3', templar, None)

# Generated at 2022-06-13 16:30:04.390124
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    # Set no_convert_bare to False to make sure the role lookup plugin can be tested
    t = Templar(loader=None, variables={}, no_convert_bare=False)
    assert listify_lookup_plugin_terms([1, 2], t, None) == [1, 2]
    assert listify_lookup_plugin_terms([1, 2, 3, 4, 5], t, None) == [1, 2, 3, 4, 5]
    assert listify_lookup_plugin_terms(['foo', 'bar'], t, None) == ['foo', 'bar']
    assert listify_lookup_plugin_terms('foo', t, None) == ['foo']

# Generated at 2022-06-13 16:30:15.701362
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    options = dict()
    loader = DataLoader()
    inventory = Host(name="test")
    inventory._variable_manager = VariableManager()
    inventory._variable_manager.set_inventory(inventory)

    templar = Templar(loader=loader, variables=inventory.get_vars())

    # Test string
    terms = listify_lookup_plugin_terms("test", templar, loader, fail_on_undefined=True, convert_bare=False)
    assert(type(terms) == list)
    assert(terms[0] == "test")

    # Test list
    terms = listify_lookup_plugin

# Generated at 2022-06-13 16:30:27.806921
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    pass
#    from ansible.module_utils.common._collections_compat import Sequence, Mapping
#    from ansible.plugins.loader import lookup_loader
#    from ansible.template import Templar
#
#    class FakeVarsModule(object):
#
#        def __init__(self):
#            self.vars = dict(foo='bar')
#
#    class FakeLoader(object):
#
#        def __init__(self):
#            pass
#
#    class FakeTemplar(Templar):
#
#        def __init__(self):
#            self._available_variables = dict()
#
#        def set_available_variables(self, variables):
#            self._available_variables = variables
#
#        def template(self, terms, **kwargs):


# Generated at 2022-06-13 16:30:36.709120
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    # Mock up AnsibleModule and AnsibleFileLookupObject
    from ansible.errors import AnsibleError
    from ansible.template import Templar
    from ansible.parsing.yaml import DataLoader

    class FileLookupObject(object):
        def __init__(self, loader):
            self.loader = loader

        def run(self, terms, inject={}, **kwargs):
            terms = listify_lookup_plugin_terms(terms, templar, self.loader, convert_bare=True)

    class AnsibleModule(object):
        def __init__(self):
            self.fail_json = self.fail_jsonp

        def fail_jsonp(self, msg):
            raise Exception("AnsibleModule failed: %s" % msg)

    # Test string input

# Generated at 2022-06-13 16:30:44.711165
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    class fake_templar:
        def template(self, data, **kwargs):
            if 'string_to_list' in data:
                return data.split(',')
            return data

    assert ['www.example.com', 'www.example.org'] == listify_lookup_plugin_terms('www.example.com,www.example.org', fake_templar())
    assert ['www.example.com', 'www.example.org'] == listify_lookup_plugin_terms(['www.example.com', 'www.example.org'], fake_templar())
    assert ['www.example.com', 'www.example.org'] == listify_lookup_plugin_terms('string_to_list', fake_templar())
    assert 'www.example.com' == listify_lookup_

# Generated at 2022-06-13 16:30:55.447748
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.dataloader import DataLoader

    def vault_secrets(secrets=None, filename=None):
        if secrets is not None:
            if isinstance(secrets, string_types):
                secrets = [secrets]
            secrets = [VaultSecret(s, None, filename) for s in secrets]
        return secrets

    loader = DataLoader()
    secrets = vault_secrets(['secret0'])
    vault = VaultLib([])

# Generated at 2022-06-13 16:31:07.509903
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.module_utils.facts.system.distribution import Distribution
    from ansible.template import Templar
    from ansible.vars import VariableManager


# Generated at 2022-06-13 16:31:10.376483
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    assert listify_lookup_plugin_terms("{{ lookup('pipe','echo foo') }}", templar, loader) == ['foo']

# Generated at 2022-06-13 16:31:30.598557
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.template.safe_eval import safe_eval
    from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleSequence, AnsibleMapping
    from ansible.vars.manager import VariableManager

    templar = Templar(loader=None, variables=VariableManager())

    # test list-ifying of strings
    test_terms = templar.template('"{{foo}}"')
    assert test_terms == ['{{foo}}']

    # test list-ifying of variables
    test_terms = templar.template('"{{foo}}"', variables={'foo': 'hello'})
    assert test_terms == ['hello']

    # test list-ifying of lists

# Generated at 2022-06-13 16:31:36.148061
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject

    terms_list = [ AnsibleBaseYAMLObject('foo'), AnsibleBaseYAMLObject('bar'), AnsibleBaseYAMLObject('baz') ]
    terms_string = AnsibleBaseYAMLObject('foo,bar,baz')
    terms_bareword = AnsibleBaseYAMLObject('foobarbaz')
    variable_manager = VariableManager()
    variable_manager.set_host_variable('foobarbaz', 'foobarbaz')
    templar = Templar(loader=None, variables=variable_manager)


# Generated at 2022-06-13 16:31:44.143398
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    #
    # [] -> []
    #
    assert [] == listify_lookup_plugin_terms([], None, None)
    #
    # "foo" -> ["foo"]
    #
    assert ["foo"] == listify_lookup_plugin_terms("foo", None, None)
    #
    # ["foo"] -> ["foo"]
    #
    assert ["foo"] == listify_lookup_plugin_terms(["foo"], None, None)
    #
    # ["foo", "bar"] -> ["foo", "bar"]
    #
    assert ["foo", "bar"] == listify_lookup_plugin_terms(["foo", "bar"], None, None)
    #
    # {"foo":"bar"} -> ["foo"]
    #

# Generated at 2022-06-13 16:31:52.910584
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    # A single non-iterable string should be turned into a list
    assert listify_lookup_plugin_terms('', None, None) == ['']
    assert listify_lookup_plugin_terms('foo', None, None) == ['foo']
    assert listify_lookup_plugin_terms('"', None, None) == ['"']
    assert listify_lookup_plugin_terms('"foo"', None, None) == ['"foo"']

    # A single iterable should be turned into a list
    assert listify_lookup_plugin_terms([], None, None) == [[]]
    assert listify_lookup_plugin_terms(['foo'], None, None) == [['foo']]
    assert listify_lookup_plugin_terms([''], None, None) == [['']]
    assert listify

# Generated at 2022-06-13 16:32:01.045858
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar
    from ansible.module_utils.common._collections_compat import Mapping, Sequence

    def test(terms, expected, fail_on_undefined, convert_bare):
        templar = Templar()
        result = listify_lookup_plugin_terms( terms, templar, None, fail_on_undefined, convert_bare )
        assert result == expected

    yield test, ['a', 'b', 'c'], ['a', 'b', 'c'], True, False
    yield test, u'a\xac\u1234\u20ac\U00008000', [u'a\xac\u1234\u20ac\U00008000'], True, False

# Generated at 2022-06-13 16:32:12.462234
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.utils.vars import combine_vars
    from ansible.playbook.play_context import PlayContext

    class MockTemplar(object):
        def __init__(self, vars=None):
            self._available_variables = vars

        def template(self, terms, convert_bare=False, fail_on_undefined=True):

            if isinstance(terms, string_types):
                terms = terms.split(',')

            ret = []
            for t in terms:
                varname = t.split('.')[0]
                if varname in self._available_variables:
                    ret.append(self._available_variables[varname])
                else:
                    raise AnsibleUndefinedVariable
            ret = combine_vars(ret)


# Generated at 2022-06-13 16:32:18.812072
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.vars import VariableManager

    v = VariableManager()
    t = Templar(loader=None, variables=v)
    terms = listify_lookup_plugin_terms(['{{foo}}', '{{bar}}', 'quux'], t, loader=None)

    assert(terms == ['{{foo}}','{{bar}}','quux'])

    v.set_variable('foo', 'test')
    v.set_variable('bar', 'test')
    t = Templar(loader=None, variables=v)
    terms = listify_lookup_plugin_terms(['{{foo}}', '{{bar}}', 'quux'], t, loader=None, convert_bare=True)

    assert(terms == ['test','test','quux'])

# Generated at 2022-06-13 16:32:29.915456
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    import ansible.constants as C

    loader = DataLoader()
    templar = Templar(loader=loader)

    # Test that a string is listified
    assert [u"a_string"] == listify_lookup_plugin_terms(u"a_string", templar=templar, loader=loader)

    # Test that a string is templated before being listified
    assert [u"a_string"] == listify_lookup_plugin_terms(u"{{ lookup('env','USER') }}", templar=templar, loader=loader)

    # Test that a simple list is not modified

# Generated at 2022-06-13 16:32:39.708736
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.template import Templar

    # Create templar object
    class DummyVarsModule(object):
        def __init__(self):
            self.ANSIBLE_CONFIG = None
            self.ANSIBLE_CONFIG_FILE = None
            self.ANSIBLE_DATA_DIR = None
            self.ANSIBLE_DEBUG = None
            self.ANSIBLE_HOST_KEY_CHECKING = True
            self.ANSIBLE_INVENTORY = None
            self.ANSIBLE_LIBRARY = None
            self.ANSIBLE_LOOKUP_PLUGINS = None
            self.ANSIBLE_MODULE_UTILS = None
            self.ANSIBLE_MODULE_UTILS_PATH = None
            self.ANSIBLE_NOCOLOR

# Generated at 2022-06-13 16:32:44.340908
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    loader = DictDataLoader({})
    templar = Templar(loader=loader)

    assert listify_lookup_plugin_terms('val1', templar, loader) == ['val1']
    assert listify_lookup_plugin_terms(['val1'], templar, loader) == ['val1']
    assert listify_lookup_plugin_terms('val1,val2', templar, loader) == ['val1', 'val2']
    assert listify_lookup_plugin_terms(['val1', 'val2'], templar, loader) == ['val1', 'val2']
    assert listify_lookup_plugin_terms('{{foo}}', templar, loader) == ['{{foo}}']

# Generated at 2022-06-13 16:33:18.969225
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.utils.unsafe_proxy import AnsibleUnsafeText, wrap_var

    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop
    from units.mock.templar import MockTemplar

    terms = u'{{foo}}'
    templar = MockTemplar(loader=DictDataLoader({u'': {u'foo': u'bar'}}))

    ret = listify_lookup_plugin_terms(terms, templar, loader=DictDataLoader(), fail_on_undefined=False)
    assert ret[0] == 'bar'
    ret = listify_lookup_plugin_terms(terms, templar, loader=DictDataLoader(), fail_on_undefined=True)
    assert ret

# Generated at 2022-06-13 16:33:26.094998
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    import ansible.template.safe_eval
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.parsing.yaml.loader import AnsibleLoader

    a_string = "a string"
    a_unicode = AnsibleUnicode('a unicode')
    a_list = [ 'a list', AnsibleUnicode('a unicode'), 'a list2']
    a_sequence = AnsibleSequence(a_list)

    data = dict(a=10)
    templar = Templar(loader=AnsibleLoader(data))


# Generated at 2022-06-13 16:33:38.279208
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    vm = VariableManager()
    assert listify_lookup_plugin_terms('string', vm, vm) == ['string']
    assert listify_lookup_plugin_terms('string with spaces', vm, vm) == ['string with spaces']
    assert listify_lookup_plugin_terms('string_with_underscores', vm, vm) == ['string_with_underscores']
    assert listify_lookup_plugin_terms('string-with-hyphens', vm, vm) == ['string-with-hyphens']
    assert listify_lookup_plugin_terms(42, vm, vm) == [42]
    assert listify_lookup

# Generated at 2022-06-13 16:33:43.608900
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.template import Templar

    t = Templar(loader=None, variables={'var': 'foo'})
    assert listify_lookup_plugin_terms("{{ var }}", t, None) == ['foo']
    assert listify_lookup_plugin_terms("{{ var }}", t, None, convert_bare=True) == ['foo']
    assert listify_lookup_plugin_terms("{{ var }}", t, None, fail_on_undefined=False) == ['foo']
    assert listify_lookup_plugin_terms("{{ var }}", t, None, convert_bare=True, fail_on_undefined=False) == ['foo']

# Generated at 2022-06-13 16:33:50.881486
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    class Templar:
        def template(self, data, fail_on_undefined=True):
        # After the collapse_jinja_inner() function the terms is a list of template objects.
        # The templar object will convert this to a string.
            return data

    loader = None
    templar = Templar()

    # Testing the return for list of string types as input.
    terms = ['foo', 'bar', 'baz']
    result = listify_lookup_plugin_terms(terms, templar, loader)
    assert isinstance(result, list)
    assert ''.join(result) == terms

    # Testing the return for list of string types as input and convert_bare=True.
    terms = ['foo', 'bar', 'baz']

# Generated at 2022-06-13 16:34:02.008970
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible import constants as C
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.template.safe_eval import safe_eval

    templar = Templar(loader=None, shared_loader_obj=None, variables={})

    # test as a single string
    terms = listify_lookup_plugin_terms("{{ foo }}", templar, None, fail_on_undefined=False)
    assert isinstance(terms, list)
    assert len(terms) == 1
    assert isinstance(terms[0], AnsibleUnicode)

    # test as a single integer
    terms = listify_lookup_plugin_terms("{{ foo | int }}", templar, None, fail_on_undefined=False)
    assert isinstance

# Generated at 2022-06-13 16:34:11.848697
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.vars import VariableManager

    varmgr = VariableManager()
    templar = Templar(loader=None, variables=varmgr)

    listify_lookup_plugin_terms(
        terms='one two three',
        templar=templar,
        loader=None)
    listify_lookup_plugin_terms(
        terms=['one', 'two', 'three'],
        templar=templar,
        loader=None)
    listify_lookup_plugin_terms(
        terms=['one', ['two', 'three']],
        templar=templar,
        loader=None)

# Generated at 2022-06-13 16:34:18.736645
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    # Loading a template to get an environment
    loader = DictDataLoader({"test": "{{x}}"})
    env = Environment(loader=loader)
    templar = Templar(loader=loader, variables=dict(x="1"))

    # Test string with ','
    assert listify_lookup_plugin_terms("{{x}}", templar, loader) == ["1"]

    # Test string with ','
    assert listify_lookup_plugin_terms("{{x}},", templar, loader) == ["1"]

    # Test string without ','
    assert listify_lookup_plugin_terms("{{x}}", templar, loader) == ["1"]

    # Test list

# Generated at 2022-06-13 16:34:29.760770
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    class FakeVarsModule(object):
        def get_vars(self, loader, play, host, task):
            return {}

    class FakeLoader(object):
        def __init__(self, data):
            self._data = data
            self._basedir = '.'

        def get_basedir(self):
            return self._basedir

        def set_data(self, data):
            self._data = data

        def load(self, file):
            return self._data.get(file, {})

    class FakeTemplar(object):
        def __init__(self, vars_module, loader, fail_on_undefined=True, convert_bare=False):
            self._vars_module = vars_module
            self._loader = loader
            self._fail_on_undefined = fail_on_

# Generated at 2022-06-13 16:34:38.941871
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext

    inventory = InventoryManager(loader=None, sources='')
    variable_manager = VariableManager(loader=None, inventory=inventory)
    variable_manager.extra_vars = dict(
        var1=10,
        var2=dict(key1=10),
    )