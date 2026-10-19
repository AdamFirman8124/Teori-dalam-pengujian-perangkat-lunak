

# Generated at 2022-06-13 16:25:12.442371
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    # Setup a fake ansible
    class FakeAnsibleModule():
        def __init__(self):
            self.params = {}
    fake_ansible_module = FakeAnsibleModule()

    from ansible.template import Templar
    templar = Templar(loader=None, variables={})

    # Test no template needed
    test_string = 'test string'
    result = listify_lookup_plugin_terms(test_string, templar, loader=None)
    assert test_string in result
    assert isinstance(result, list)
    assert len(result) == 1

    # Test one level of templating is applied
    test_string = '{{teststring}}'
    result = listify_lookup_plugin_terms(test_string, templar, loader=None)
    assert test_string in result

# Generated at 2022-06-13 16:25:19.910341
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    vm = VariableManager()

    templar = Templar(loader=loader, variables=vm)
    assert listify_lookup_plugin_terms('foobar', templar) == ['foobar']
    assert listify_lookup_plugin_terms(['foobar'], templar) == ['foobar']
    assert listify_lookup_plugin_terms('{{foobar}}', templar) == ['{{foobar}}']
    assert listify_lookup_plugin_terms('{{foobar|default("no")}}', templar) == ['no']
    assert listify_lookup_plugin_terms('{{foobar}}', templar, convert_bare=True)

# Generated at 2022-06-13 16:25:27.298830
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible import constants as C

    templar = Templar(loader=None, variables={C.DEFAULT_JINJA2_NATIVE_TYPES: True})


# Generated at 2022-06-13 16:25:38.302100
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    class TestObject(object):
        def __init__(self, msg):
            self.msg = msg

    # Templar class mock
    class TestTemplar(object):
        def __init__(self, data, extra_data, convert_bare=False, fail_on_undefined=True, kwargs=dict()):
            self.data = data
            self.extra_data = extra_data
            self.convert_bare = convert_bare
            self.fail_on_undefined = fail_on_undefined
            self.kwargs = kwargs

        # Return a string if the 'data' attribute of the instance is a string,
        # otherwise return 'data' itself.

# Generated at 2022-06-13 16:25:44.756766
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    texplar = DummyTemplar()
    tloader = DummyLoader()

    def get_test_entry(input, output):
        return (input, output)


# Generated at 2022-06-13 16:25:56.354853
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.template.safe_eval import safe_eval
    assert listify_lookup_plugin_terms("{{ [1, 2, 3] }}", Templar(loader=None), None,
                                       fail_on_undefined=True, convert_bare=False) == [1, 2, 3]
    assert listify_lookup_plugin_terms("{{ 'foobar' }}", Templar(loader=None), None,
                                       fail_on_undefined=True, convert_bare=False) == ['foobar']
    # safe_eval() takes a string, so we can't test these two cases.
    #assert listify_lookup_plugin_terms([1, 2, 3], Templar(loader=None), None,
    #                                   fail_on_undefined=True, convert_bare=False)

# Generated at 2022-06-13 16:26:04.890445
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    variable_manager = VariableManager()
    loader = variable_manager.loader
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager.set_inventory(inventory)

    class MyTemplar(Templar):
        def __init__(self, loader, variables=None):
            super(MyTemplar, self).__init__(loader=loader, variables=variables)
            self._available_variables = variables

    templar = MyTemplar(loader=loader, variables=dict())

    # test that a string is returned as a list
    terms = 'a'

# Generated at 2022-06-13 16:26:12.486748
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    ''' Test for function listify_lookup_plugin_terms '''
    from ansible.template import Templar
    terms = '{{ foo | string(4) }} {{bar}}'
    templar = Templar(loader=None, variables={'foo': 'a', 'bar': 'b'})
    transformed_terms = listify_lookup_plugin_terms(terms, templar, loader=None, fail_on_undefined=True)
    assert transformed_terms == ['a', 'b'], "listify_lookup_plugin_terms() did not correctly template terms"

# Generated at 2022-06-13 16:26:20.888012
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.compat.tests import unittest
    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib
    from ansible.utils.vars import combine_vars
    from ansible.utils.listify import listify_lookup_plugin_terms
    from ansible.vars.manager import VariableManager

    class TestTemplar(Templar):
        def __init__(self, variables, loader, shared_loader_obj=None):
            self._datastore = variables
            self._loader = loader
        def template(self, value, convert_bare=True, fail_on_undefined=True, override_vars=None):
            return value
        def set_available_variables(self, variables):
            self._datastore = variables

    TEST_HOST_

# Generated at 2022-06-13 16:26:32.292153
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    # Import all plugins to make sure nothing breaks
    import ansible.plugins # lib/ansible/plugins/__init__.py
    #from ansible.plugins.lookup import * # LookupModule
    #from ansible.plugins.strategy import * # StrategyModule

    from ansible.template import Templar # playbook/template.py
    from ansible.parsing.dataloader import DataLoader # lib/ansible/parsing/dataloader.py

    #from ansible.playbook.play_context import PlayContext # playbook/play_context.py
    from ansible.vars import VariableManager # lib/ansible/vars.py
    from ansible.inventory import Inventory # lib/ansible/inventory/__init__.py
    #from ansible.executor import task_queue_manager # lib/ansible/

# Generated at 2022-06-13 16:26:44.242179
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    # Initialize an empty inventory
    inventory = InventoryManager()
    # Initialize a variable manager
    variable_manager = VariableManager()
    # Set the default host information
    variable_manager.set_inventory(inventory)
    # Initialize a fake play context
    play_context = PlayContext()
    # Initialize the templar
    templar = Templar(loader=None, variables=variable_manager, all_vars=variable_manager)

    # Here are the tests
    # input: a string
    val = "{{ string_var }}"
    # output: a list with the content of the variable string_var

# Generated at 2022-06-13 16:26:56.504148
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.module_utils.common._collections_compat import Sequence

    from ansible.template import Templar

    loader = None

    # Basic pass through test
    terms = listify_lookup_plugin_terms([1,2,3], Templar(loader=loader), loader)
    assert len(terms) == 3

    # Templating test
    terms = listify_lookup_plugin_terms([u"{{foo}}", "2", 3], Templar(loader=loader), loader, convert_bare=True, fail_on_undefined=False)
    assert isinstance(terms, Sequence)
    assert len(terms) == 3
    assert terms[0] == u"{{foo}}"


# Generated at 2022-06-13 16:27:05.928964
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.vars import VariableManager

    v = VariableManager()
    v.extra_vars = {'a': 'A'}
    t = Templar(loader=None, variables=v)

    assert listify_lookup_plugin_terms('1', t, None) == ['1']
    assert listify_lookup_plugin_terms(['1'], t, None) == ['1']
    assert listify_lookup_plugin_terms(['1', '2'], t, None) == ['1', '2']

    # {{ ansible_managed }} uses the "convert_bare" param
    assert listify_lookup_plugin_terms('{{ ansible_managed }}', t, None) == ['{{ ansible_managed }}']
    assert listify_lookup_plugin_terms

# Generated at 2022-06-13 16:27:16.600348
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    templar = Templar(loader=None, variables={})
    assert listify_lookup_plugin_terms('foo', templar) == ['foo']
    assert listify_lookup_plugin_terms('foo bar', templar) == ['foo bar']
    assert listify_lookup_plugin_terms('foo, bar', templar) == ['foo, bar']
    for arg in [ ['foo'], ['foo', 'bar'] ]:
        assert listify_lookup_plugin_terms(arg, templar) == arg
    assert listify_lookup_plugin_terms('{{foo}}', templar, fail_on_undefined=False) == [None]

# Generated at 2022-06-13 16:27:26.683358
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.plugins.lookup import LookupBase
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader)
    variable_manager.set_inventory(inventory)
    play_context = PlayContext()

    templar = Templar(loader=loader, variables=variable_manager,
        shared_loader_obj=loader)

    # 1. test empty term

# Generated at 2022-06-13 16:27:32.248570
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.six import PY3
    from ansible import constants as C
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.parsing.vault import VaultLib

    # We need to mock the class, because it's not serializable, and thus not
    # easy to just put into a yaml file
    class MockVaultLib(object):

        def get_decrypted(self, value):
            return "vaulted:" + value

    def mock_template(value, fail_on_undefined=False, convert_bare=True):
        if not isinstance(value, MutableMapping):
            value = str(value)

# Generated at 2022-06-13 16:27:42.393847
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.utils.listify import listify_lookup_plugin_terms
    from ansible.template import Templar
    from ansible.errors import AnsibleError
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    variable_manager = VariableManager()
    variable_manager.set_inventory(InventoryManager(loader=None, sources=['localhost,']))
    list_of_hosts = ['hostname1', 'hostname2']
    variable_manager.set_host_variable(host=variable_manager.get_inventory().get_host('localhost'), varname='hostvars', value=dict(inventory_hostname=list_of_hosts))


# Generated at 2022-06-13 16:27:51.903589
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from units.compat import unittest
    from units.compat.mock import patch
    from ansible.utils.template import Templar
    from ansible.parsing.dataloader import DataLoader

    class TestListifyLookupPluginTerms(unittest.TestCase):

        def setUp(self):
            self._loader = DataLoader()
            self._templar = Templar(loader=self._loader)

        def tearDown(self):
            pass

        @patch('ansible.module_utils.common.listify_lookup_plugin_terms')
        def test_listify_lookup_plugin_terms_string(self, mock_llpt):

            mock_llpt.return_value = [1, 2, 3]

# Generated at 2022-06-13 16:28:02.649999
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.common._collections_compat import MutableSequence

    def test_templar(obj, fail_on_undefined=True):
        return 'foo'


# Generated at 2022-06-13 16:28:12.598743
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils._text import to_text
    from ansible.template import Templar

    templar = Templar(loader=None, shared_loader_obj=None)

    # test string
    assert listify_lookup_plugin_terms("1 2 3", templar, None) == ["1 2 3"]
    assert listify_lookup_plugin_terms("1\n2\n3", templar, None) == ["1\n2\n3"]

    # test list
    assert listify_lookup_plugin_terms(["1", "2", "3"], templar, None) == ["1", "2", "3"]

    # test dict

# Generated at 2022-06-13 16:28:27.541036
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar

    loader = DataLoader()
    templar = Templar(loader=loader)

    # Test with list to start.
    list_to_start = [1, 2, 3]
    result = listify_lookup_plugin_terms(list_to_start, templar, loader)
    assert result == list_to_start, 'listify_lookup_plugin_terms failed, expected %s, got %s' % (list_to_start, result)

    # Test with string to start.
    string_to_start = '1, 2, 3'
    result = listify_lookup_plugin_terms(string_to_start, templar, loader)

# Generated at 2022-06-13 16:28:37.851543
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    """
    This is not a complete set of tests, but the basics are covered
    """
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar

    terms = [
        "1",
        ["2"],
        [3],
        "{{ lookup('password', 'crypted-password') }}",
        "{{ lookup('env', 'HOME') }}",
        "{{ lookup('pipe', 'date') }}",
    ]

    loader = DataLoader()
    templar = Templar(loader=loader, variables = dict(foo = 'bar', baz = 'xyzzy'))

    assert listify_lookup_plugin_terms(terms, templar, loader, fail_on_undefined=True) == ['1', '2', 3, 'bar', 'xyzzy', 'cyborg']


# Generated at 2022-06-13 16:28:46.708702
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template.safe_eval import safe_eval
    from ansible.template import Templar

    templar = Templar(loader=None)


# Generated at 2022-06-13 16:28:51.867707
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.utils.vars import combine_vars
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    # Create a vault secret
    vault_pass = 'ansible'
    va = VaultLib([])
    vault_secret = va.encrypt('some-secret')

    # Create a templar
    variable_manager = VariableManager()
    loader = None
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager.set_inventory(inventory)

# Generated at 2022-06-13 16:29:01.289730
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    # Testing this function requires a lot of mocking and it is not clear
    # where to start and what needs to be mocked.  For now just do one test
    # to make sure the function signature has not changed and that it returns a list
    assert listify_lookup_plugin_terms('', None, None) == ['']

    # Create a templar mock class
    class TemplarMock(object):
        def __init__(self):
            self._converted_data = None

        def template(self, x, **kwargs):
            return self._converted_data

    # String should convert to a list
    templar = TemplarMock()
    templar._converted_data = 'foo'
    assert listify_look

# Generated at 2022-06-13 16:29:10.782802
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    assert listify_lookup_plugin_terms('a', None, None, True, False) == ['a']
    assert listify_lookup_plugin_terms(['a'], None, None, True, False) == ['a']
    assert listify_lookup_plugin_terms(('a',), None, None, True, False) == ['a']
    assert listify_lookup_plugin_terms(('a'), None, None, True, False) == ['a']
    assert listify_lookup_plugin_terms(['a'], None, None, True, True) == ['a']
    assert listify_lookup_plugin_terms(('a',), None, None, True, True) == ['a']
    assert listify_lookup_plugin_terms(('a'), None, None, True, True) == ['a']


# Generated at 2022-06-13 16:29:20.580956
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib

    # load up needed objects
    templar = Templar(loader=None, variables={})
    vault = VaultLib(password_files=[], passwords=[])

    # test strings
    test = "{{ 'foo' }}"
    assert listify_lookup_plugin_terms(test, templar, None, fail_on_undefined=True, convert_bare=False) == ["foo"]
    test = "{{ 'foo' }},{{ 'bar' }}"
    assert listify_lookup_plugin_terms(test, templar, None, fail_on_undefined=True, convert_bare=False) == ["foo", "bar"]

# Generated at 2022-06-13 16:29:27.586830
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    class TestTemplar(object):
        def __init__(self):
            pass

        def template(self, template, fail_on_undefined=False, bare=False, convert_bare=False):
            return template

    class TestLoader(object):
        pass

    assert listify_lookup_plugin_terms('foo', TestTemplar(), TestLoader()) == ['foo']
    assert listify_lookup_plugin_terms('foo,bar', TestTemplar(), TestLoader()) == ['foo', 'bar']

# Generated at 2022-06-13 16:29:38.076728
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    '''Unit test for function listify_lookup_plugin_terms'''
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory

    test_vars = VariableManager()
    test_vars.extra_vars = {'list_var': ['some', 'list', 'of', 'values']}
    test_hosts = Inventory()
    test_hosts.add_host("localhost")
    test_hosts.set_variable("localhost", 'list_var', ['another', 'list', 'of', 'values'])

    from ansible.parsing.dataloader import DataLoader
    test_loader = DataLoader()

    from ansible.template import Templar
    test_templar = Templar(loader=test_loader, variables=test_vars)

    # Test string lookup term
   

# Generated at 2022-06-13 16:29:48.132028
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils._text import to_text

    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    templar = Templar(loader=None, variables={'secret': AnsibleVaultEncryptedUnicode('somethingsecret')})

    for item in ['foo', 'bar', 'baz']:
        assert listify_lookup_plugin_terms(item, templar, loader=None) == [item]
    test_list = ['foo', 'bar', 'baz']
    assert listify_lookup_plugin_terms(test_list, templar, loader=None) == test_list

    test_unicode = u'foo'

# Generated at 2022-06-13 16:30:03.793356
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    # We can't import ansible.module_utils.six and ansible.parsing.dataloader at the same time
    import ansible.module_utils.six as six
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    args = {
        '_raw_params': '{{ lookup_plugin_terms }}',
        'lookup_plugin_terms': 'a b',
    }
    loader = DataLoader()
    variable_manager = VariableManager()
    templar = Templar(loader=loader, variable_manager=variable_manager)

    terms = listify_lookup_plugin_terms(args, templar, loader)
    assert isinstance(terms, six.string_types)


# Generated at 2022-06-13 16:30:15.063176
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    import ansible.module_utils.common.collections

    # Fixtures
    class TestTemplar(object):
        _templar = True

        def template(self, value, fail_on_undefined=False, convert_bare=False):
            if value == 'var_is_undefined':
                raise ansible.module_utils.common.collections.AnsibleUndefinedVariable('var_is_undefined')
            if value == 'var_convert_bare':
                convert_bare = True
                return convert_bare
            return value


# Generated at 2022-06-13 16:30:27.466788
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleUnicode

    class DummyLoader(object):
        def get_basedir(self):
            return 'testdir'
    class DummyVars(object):
        pass

    class DummyVar(object):
        def __init__(self, val):
            self.val = val
        def __getitem__(self, item):
            return self.val[item]

    def test_term_1(terms):
        assert listify_lookup_plugin_terms(terms, templar, loader) == terms

    def test_term_2(terms, expected):
        assert listify_lookup_plugin_terms(terms, templar, loader) == expected


# Generated at 2022-06-13 16:30:33.851078
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    context = {}
    templar = Templar(loader=None, variables=context)

    assert listify_lookup_plugin_terms('foo', templar, None) == ['foo']
    assert listify_lookup_plugin_terms('foo bar', templar, None) == ['foo bar']
    assert listify_lookup_plugin_terms(['foo'], templar, None) == ['foo']
    assert listify_lookup_plugin_terms(['foo', 'bar'], templar, None) == ['foo', 'bar']

# Generated at 2022-06-13 16:30:43.000301
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.template import Templar

    loader = DataLoader()
    variable_manager = VariableManager()
    templar = Templar(loader=loader, variables=variable_manager)
    lookup_plugin_terms = ['/var/lib/{{ item }}', 'nginx']

    result = listify_lookup_plugin_terms(lookup_plugin_terms, templar, loader)
    assert result == [u'/var/lib/{{ item }}', u'nginx']

    result = listify_lookup_plugin_terms(lookup_plugin_terms, templar, loader, convert_bare=True)
    assert result == [u'/var/lib/{{ item }}', u'nginx']

    result = list

# Generated at 2022-06-13 16:30:54.010229
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar, loader
    templar = Templar(loader=loader)

    def check(terms, expected):
        terms = listify_lookup_plugin_terms(terms=terms, fail_on_undefined=False, templar=templar, loader=loader)
        assert type(terms) == list, "Expected a list, got a %s" % type(terms)
        assert terms == expected, "Expected a %s, got a %s" % (expected, terms)


# Generated at 2022-06-13 16:31:02.002114
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play

    variable_manager = VariableManager()
    loader = AnsibleLoader(None, variable_manager=variable_manager)

    variable_manager.extra_vars = {'foo': 'World', 'bar': ['X', 'Y', 'Z']}

    vault_pass = 'secret'

    vault = VaultLib(vault_pass)

    # create template
    template_data = """
#stdout_lines {{ foo }}
#stdout_lines {{ bar }}
    """

    # create play
    play_

# Generated at 2022-06-13 16:31:09.223916
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    assert listify_lookup_plugin_terms(['foo', 'bar'], None, None) == ['foo', 'bar']
    assert listify_lookup_plugin_terms(('foo', 'bar'), None, None) == ['foo', 'bar']
    assert listify_lookup_plugin_terms('FOO', None, None) == ['FOO']
    assert listify_lookup_plugin_terms('FOO,bar', None, None) == ['FOO', 'bar']
    assert listify_lookup_plugin_terms('foo, BAR', None, None) == ['foo', 'BAR']

# Generated at 2022-06-13 16:31:15.342652
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    import ansible.parsing.dataloader
    import ansible.vars
    import ansible.inventory
    loader = ansible.parsing.dataloader.DataLoader()
    inv = ansible.inventory.Inventory(loader=loader, variable_manager=ansible.vars.VariableManager())
    templar = Templar(loader=loader, variables=inv.get_vars())

    # test string
    assert listify_lookup_plugin_terms('foo', templar, loader) == ['foo']
    assert listify_lookup_plugin_terms(' foo ', templar, loader) == ['foo']

    # test list
    assert listify_lookup_plugin_terms(['foo'], templar, loader) == ['foo']

    # test dict


# Generated at 2022-06-13 16:31:26.032368
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible import constants as C
    from ansible.playbook.play_context import PlayContext

    from ansible.template import Templar

    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=C.DEFAULT_HOST_LIST)
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext()

    templar = Templar(loader=loader, variables=variable_manager,
                      shared_loader_obj=variable_manager, fail_on_undefined=C.DEFAULT_UNDEFINED_VAR_BEHAVIOR)


# Generated at 2022-06-13 16:31:50.040827
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    t = Templar(loader=None, variables={})

    res = listify_lookup_plugin_terms('t1', t, None, convert_bare=True)
    assert res == ['t1'], res

    res = listify_lookup_plugin_terms(['t1', 't2'], t, None, convert_bare=True)
    assert res == ['t1', 't2'], res

    res = listify_lookup_plugin_terms('{{var1}}', t, None, convert_bare=True)
    assert res == [u'{{var1}}'], res

    res = listify_lookup_plugin_terms(['{{ var1 }}', '{{ var2 }}'], t, None, convert_bare=True)

# Generated at 2022-06-13 16:31:58.145520
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.parsing.vault import VaultLib
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar

    loader = DataLoader()
    vault_secrets = VaultLib([])
    variable_manager = VariableManager()
    variable_manager.set_vault_secrets(vault_secrets)
    templar = Templar(loader=loader, variables=variable_manager)


# Generated at 2022-06-13 16:32:10.214900
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    fake_loader = DataLoader()
    fake_host = Host(name="fakehost")
    fake_group = Group(name="fakegroup")
    fake_allgroup = Group(name="all")
    fake_allgroup.add_host(fake_host)
    fake_inventory = [fake_host, fake_group, fake_allgroup]

    fake_vars = VariableManager()
    fake_vars.add_group(fake_group)
    fake_vars.add_host(fake_host)


# Generated at 2022-06-13 16:32:13.216726
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    # Success case
    try:
        from ansible.template import Templar
        from ansible.parsing.dataloader import DataLoader
        templar = Templar(loader=DataLoader())
        assert listify_lookup_plugin_terms("{{ foo }}", templar, templar._loader, False) == ['{{ foo }}']
    except ImportError:
        pass

# Generated at 2022-06-13 16:32:22.090014
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    templar = Templar(loader=None, variables={})

    assert listify_lookup_plugin_terms("foo", templar, None) == ["foo"]
    assert listify_lookup_plugin_terms("foo,bar", templar, None) == ["foo", "bar"]
    assert listify_lookup_plugin_terms(["foo", "bar,baz"], templar, None) == ["foo", "bar,baz"]
    assert listify_lookup_plugin_terms(["foo,bar", "baz"], templar, None) == ["foo,bar", "baz"]


if __name__ == '__main__':
    test_listify_lookup_plugin_terms()

# Generated at 2022-06-13 16:32:32.117029
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    templar = Templar(loader=None, variables={})

    assert listify_lookup_plugin_terms(1, templar, None) == ['1']
    assert listify_lookup_plugin_terms(1.0, templar, None) == ['1.0']
    assert listify_lookup_plugin_terms('1', templar, None) == ['1']
    assert listify_lookup_plugin_terms('1.0', templar, None) == ['1.0']
    assert listify_lookup_plugin_terms([1], templar, None) == [1]
    assert listify_lookup_plugin_terms([1, 2, 3], templar, None) == [1, 2, 3]
    assert listify_lookup_plugin

# Generated at 2022-06-13 16:32:40.629917
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    import pprint
    import sys
    import lib.ansible.modules.system.ping

    p = lib.ansible.modules.system.ping.Ping()
    p.params = {}
    p.params['data'] = sys.modules[__name__]
    p.params['fail_on_undefined'] = False
    p.params['convert_bare'] = False

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['/dev/null'])

# Generated at 2022-06-13 16:32:45.898620
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    # Note that we are only testing the "convert_bare" option here,
    # as other parts of the templating system are tested elsewhere

    # pylint: disable=import-error,no-name-in-module,unused-import
    from ansible.module_utils.common._collections_compat import Mapping

    # pylint: disable=too-many-locals
    from ansible.template import Templar

    from ansible.vars import VariableManager
    from ansible.parsing.vault import VaultLib

    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext

    from ansible.plugins.vars import BaseVarsPlugin

    # Load up

# Generated at 2022-06-13 16:32:55.736260
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    '''
    Listify_lookup_plugin_terms: Tests if the required list format can be obtained
    '''
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.vars.manager import VariableManager

    variable_manager = VariableManager()
    variable_manager.set_inventory(Inventory('localhost'))
    templar = Templar(loader=None, variables=variable_manager)

    # list of strings in unencrypted, encrypted and mixed formats

# Generated at 2022-06-13 16:33:02.484245
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    # Imports of Ansible modules only work inside a module
    from ansible.parsing.plugin_docs import read_docstring
    from ansible.template import Templar

    # Dummy templar object
    templar = Templar(loader=None)

    # Test strings
    terms = "{{ var }}"
    templar.set_available_variables(dict(var="hello"))
    res = listify_lookup_plugin_terms(terms, templar, loader=None)
    assert res == ["hello"]

    # Test lists
    terms = ["{{ var1 }}", "{{ var2 }}"]
    templar.set_available_variables(dict(var1="hello", var2="world"))
    res = listify_lookup_plugin_terms(terms, templar, loader=None)

# Generated at 2022-06-13 16:33:40.724749
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.template import Templar
    from ansible.inventory.manager import InventoryManager

    terms = []
    terms.append('{{["foo", "foo"]}}')
    terms.append('{{[foo, 1 + 1]}}')
    terms.append('a {{item}} b')
    terms.append('{{ item }}')
    terms.append('{{ foo }}')
    terms.append('{{ "bar" }}')
    terms.append('{{ "bar" + "baz" }}')
    terms.append('{{ foo.bar }}')
    terms.append('{{ foo.bar.baz }}')
    terms.append('{{ foo["bar"] }}')

# Generated at 2022-06-13 16:33:48.961002
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib
    vault = VaultLib("")
    templar = Templar(loader=None, variables={}, vault_secrets=vault)

    # test string
    terms = "{{ test_value }}"
    assert listify_lookup_plugin_terms(terms, templar, loader=None) == ['{{ test_value }}']

    # test int
    terms = 5
    assert listify_lookup_plugin_terms(terms, templar, loader=None) == ["5"]

    # test True
    terms = True
    assert listify_lookup_plugin_terms(terms, templar, loader=None) == ["True"]

    # test True
    terms = False

# Generated at 2022-06-13 16:34:00.381555
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    assert listify_lookup_plugin_terms(['a', 'b'], templar=None, loader=None, fail_on_undefined=True,
                                       convert_bare=False) == ['a', 'b']
    assert listify_lookup_plugin_terms('a', templar=None, loader=None, fail_on_undefined=True,
                                       convert_bare=False) == ['a']
    assert listify_lookup_plugin_terms(' a ', templar=None, loader=None, fail_on_undefined=True,
                                       convert_bare=False) == ['a']
    assert listify_lookup_plugin_terms('a,b', templar=None, loader=None, fail_on_undefined=True,
                                       convert_bare=False) == ['a,b']

# Generated at 2022-06-13 16:34:03.085490
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    '''
    - debug:
        msg: "{{ lookup('pipe', 'echo {{item}}') }}"
      with_fileglob:
        - /etc/passwd
    '''



# Generated at 2022-06-13 16:34:12.630730
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    from ansible.template import Templar

    from ansible.inventory.host import Host

    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    class MyHost(Host):
        def __init__(self, name):
            super(MyHost, self).__init__(name)
            self.get_vars = lambda: dict(a=1, b=2, c=dict(d=3, e=4))
            self.get_hostname_variables = lambda: dict(a=1, b=2, c=dict(d=3, e=4))


# Generated at 2022-06-13 16:34:19.176931
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.common._collections_compat import StringIO
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.vault import VaultLib

    variable_manager = VariableManager()
    loader = variable_manager.get_vars_loader()

    variable_manager.set_inventory(loader.load_inventory(loader.inventory_basedirs[0]))
    variable_manager._extra_vars = loader.load_from_file('/dev/null')

    vault_secrets = VaultLib(None, variable_manager=variable_manager)
    variable_manager.set_vault_secrets(vault_secrets)

    templar = Templar(loader=loader, variable_manager=variable_manager)


# Generated at 2022-06-13 16:34:30.101226
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.mod_args import ModuleArgsParser

    mock_loader = None
    args_parser = ModuleArgsParser(templar=Templar(loader=mock_loader))

    # Test the following types of terms
    terms_list = [
        [{'key': 'value'}],
        [{'key': 'value'}, 'second_entry'],
        [{'key': 'value'}, 'second_entry', {'key': 'value'}, 'fourth_entry'],
        {'key': 'value'},
        {'key': 'value', 'another-key': 'another-value'},
        'only-entry',
        '',
        '   '  # String with just whitespace
    ]


# Generated at 2022-06-13 16:34:40.085129
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    import ansible.parsing.yaml.objects

    class FakeTemplar(object):
        def template(self, terms, convert_bare=False, fail_on_undefined=False):
            if isinstance(terms, ansible.parsing.yaml.objects.AnsibleUnicode):
                return terms
            elif isinstance(terms, dict):
                return dict([(terms['key'],terms['value'])])
            elif isinstance(terms, str):
                return terms
            else:
                return terms

    fake_templar = FakeTemplar()


# Generated at 2022-06-13 16:34:48.105361
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    # TODO: need better tests for templating and a way to mock the templar
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import get_file_vault_secret
    import os
    import tempfile

    old_secret = os.environ.get("ANSIBLE_VAULT_PASSWORD_FILE")
    old_vault_key = os.environ.get("ANSIBLE_VAULT_KEY_FILE")
    old_vault_password = os.environ.get("ANSIBLE_VAULT_PASSWORD")
    vault_key_file = None
    vault_password_file = None

    class FakeVault:
        def decrypt(self, b):
            return b


# Generated at 2022-06-13 16:34:57.633134
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.parsing.yaml.objects import AnsibleUnicode

    from ansible.template import Templar

    from ansible.vars.clean import module_response_deepcopy

    the_list = [u'one', u'two', u'three']
    data = {
        'one': '1',
        'two': '2',
        'three': '3',
    }

    class MockTemplar(Templar):

        def __init__(self, loader, variables):
            super(MockTemplar, self).__init__(loader=loader, variables=variables)

        def template(self, data, **kwargs):
            if isinstance(data, string_types):
                data = AnsibleUnicode(module_response_deepcopy(data))