

# Generated at 2022-06-13 16:25:09.829256
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.vault import VaultLib

    # Setup basic mocks for Templar and AnsibleLoader
    class MockVaultLib:
        def decrypt(self, b_data):
            return 'hello world'

    vault_secret = MockVaultLib()

    # Used to decrypt vaulted values, but we don't want
    # to actually encrypt/decrypt in the unit test, so the mock
    # just returns the already decrypted value
    def vault_decrypt(b_data):
        return b_data

    class MockVaultSecret:
        def __init__(self):
            self.decrypt = vault_decrypt


# Generated at 2022-06-13 16:25:20.013285
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    '''
    listify_lookup_plugin_terms:
      - '{{fqdn_list}}'
      - '{{prefix}}-{{item}}.{{suffix}}'
      - item: '{{ansible_hostname}}'
      - item: '{{ansible_domain}}'
    '''
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.vars import VariableManager
    from ansible.utils.vars import combine_vars
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import wrap_var
    from ansible.vars.unsafe_proxy import AnsibleUnsafe

# Generated at 2022-06-13 16:25:27.392047
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    variable_manager = VariableManager()
    variable_manager.extra_vars = dict(foo='bar')
    templar = Templar(loader=None, variables=variable_manager)

    assert listify_lookup_plugin_terms("a", templar) == ["a"]
    assert listify_lookup_plugin_terms("a, b", templar) == ["a, b"]
    assert listify_lookup_plugin_terms(["a", "b"], templar) == ["a", "b"]
    assert listify_lookup_plugin_terms(["a", "{{ foo }}"], templar) == ['a', 'bar']

# Generated at 2022-06-13 16:25:38.342280
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    play_context = PlayContext()
    templar = Templar(loader=None, variables={})

    assert listify_lookup_plugin_terms(None, templar, None, False, False) == [None]
    assert listify_lookup_plugin_terms("string", templar, None, False, False) == ["string"]
    assert listify_lookup_plugin_terms(" string ", templar, None, False, False) == ["string"]
    assert listify_lookup_plugin_terms("{{string}}", templar, None, False, False) == ["{{string}}"]

# Generated at 2022-06-13 16:25:44.780231
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    variable_manager = DummyVars({})
    loader = DataLoader()
    templar = Templar(loader=loader, variable_manager=variable_manager)


# Generated at 2022-06-13 16:25:56.410448
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    templar = Templar(loader=loader)

    # test case 1
    terms = "{{ lookup('pipe', 'echo teststring') }}"
    expected_terms = ["teststring"]
    new_terms = listify_lookup_plugin_terms(terms, templar, loader, fail_on_undefined=True, convert_bare=False)
    assert new_terms == expected_terms

    # test case 2
    terms = "{{ lookup('pipe', 'echo teststring').split()[0] }}"
    expected_terms = ["teststring"]

# Generated at 2022-06-13 16:26:03.422311
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.module_utils.common._collections_compat import Sequence
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    templar = Templar(loader=loader)


# Generated at 2022-06-13 16:26:13.614800
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    terms = ['{{ inventory_hostname }}', '{{ inventory_hostname }}', ['{{ ansible_hostname }}', '{{ inventory_hostname }}']]
    my_vars = dict(inventory_hostname='localhost',
                   ansible_hostname='127.0.0.1')
    my_loader = DataLoader()
    my_templar = Templar(loader=my_loader, variables=my_vars)
    result = listify_lookup_plugin_terms(terms, my_templar, my_loader, fail_on_undefined=True, convert_bare=False)
    assert result == ['localhost', 'localhost', ['127.0.0.1', 'localhost']]

# Generated at 2022-06-13 16:26:21.729665
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar
    from ansible.vars import VariableManager

    t = Templar(loader=None, variables=VariableManager())
    assert listify_lookup_plugin_terms('{{foo}}', t, None, fail_on_undefined=True) == ['{{foo}}']
    assert listify_lookup_plugin_terms(['{{foo}}', '{{bar}}'], t, None, fail_on_undefined=True) == ['{{foo}}', '{{bar}}']
    assert listify_lookup_plugin_terms('foo', t, None, fail_on_undefined=True) == ['foo']
    assert listify_lookup_plugin_terms([1, 2], t, None, fail_on_undefined=True) == [1, 2]

# Generated at 2022-06-13 16:26:25.771771
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    vars_manager = VariableManager()

    # String, String
    input = "{{ foo }}"
    expected = ["{{ foo }}"]
    templar = Templar(loader=loader, variables=vars_manager)
    output = listify_lookup_plugin_terms(input, templar, loader)
    assert output == expected

    # List, String
    input = ["{{ foo }}"]
    expected = ["{{ foo }}"]
    templar = Templar(loader=loader, variables=vars_manager)
    output = listify_lookup_plugin_terms(input, templar, loader)
    assert output == expected

   

# Generated at 2022-06-13 16:26:36.912040
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    class TestYAMLObject(AnsibleBaseYAMLObject):
        @property
        def data(self):
            return self._yaml_data

    from ansible.template import Templar

    loader = None
    templar = Templar(loader=loader)

    assert(listify_lookup_plugin_terms(3, templar, loader) == [3])
    assert(listify_lookup_plugin_terms([3], templar, loader) == [3])
    assert(listify_lookup_plugin_terms(TestYAMLObject([3]), templar, loader) == [3])

    assert(listify_lookup_plugin_terms("3", templar, loader) == ["3"])

# Generated at 2022-06-13 16:26:45.983226
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    def _terms_equal(result, expected):
        assert result == expected, '%s != %s' % (result, expected)
        if isinstance(result, list):
            assert len(result) == len(expected), '%s != %s' % (result, expected)
            for r, e in zip(result, expected):
                assert r == e, '%s != %s' % (result, expected)

    from ansible.template import Templar
    from ansible.inventory.host import Host
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    data_loader = DataLoader()

    variable_manager = VariableManager()

# Generated at 2022-06-13 16:26:57.094359
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils._text import to_bytes

    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar

    loader = DictDataLoader({})
    variable_manager = VariableManager()
    templar = Templar(loader=loader, variables=variable_manager)

    assert listify_lookup_plugin_terms('foo', templar, loader) == ['foo'], "Should return a list of one element"

# Generated at 2022-06-13 16:27:06.456715
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.common._collections_compat import OrderedDict
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.template import Templar
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.utils.vars import combine_vars

    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=["localhost"])
    variable_manager.set_inventory(inventory)
    hostvars = inventory.get_host("localhost").get_vars()
    play_context = PlayContext()
    variable_manager.set_play_context(play_context)


# Generated at 2022-06-13 16:27:17.091333
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    import ansible.template
    import ansible.parsing.yaml.objects
    from ansible.template import Templar

    assert listify_lookup_plugin_terms([1, 2, [3, 4]], None, None) == [1, 2, [3, 4]]

    # test with a string of json
    template_data = """
    {
        "foo": [1, 2, {"bar": [3, 4]}]
    }
    """
    yaml_data = ansible.parsing.yaml.objects.AnsibleBaseYAMLObject(template_data, ansible.template.AnsibleOptions(lookup_loader=None))
    templar = Templar(loader=None)

# Generated at 2022-06-13 16:27:27.030810
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    # Imports
    import ansible.errors as errors
    import ansible.template as template

    # Create a templar and templar-related variables
    templar = template.Templar(loader=None, variables={'a': ['b', 'c'], 'd': 'e', 'f': 1, 'f': None})

    # Test with a basic (non-iterable) usage
    assert listify_lookup_plugin_terms('a', templar, None) == ['b', 'c']

    # Test with a basic (non-iterable) usage that is a string
    assert listify_lookup_plugin_terms('d', templar, None) == ['e']

    # Test with a basic (non-iterable) usage that is a integer

# Generated at 2022-06-13 16:27:35.501463
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleSequence
    from ansible.module_utils._text import to_bytes
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    class test_loader(object):
        def get_basedir(self, x):
            return 'some/path'

    loader = test_loader()
    templar = Templar(loader=loader)

    # Fake the ansible version
    templar.environment.ansible_version_info = (2, 0)

    # Handle string
    string_terms = '{{ term }}'
    string_terms_with_convert_bare = {'_raw_params': 'term', '_ansible_convert_bare': True}
    string_terms

# Generated at 2022-06-13 16:27:46.778680
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.six import StringIO
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.objects import AnsibleUnicode

    class DummyVarsModule:
        def __init__(self, data):
            self.data = data

        def get_vars(self, loader, path, entities, cache=True):
            if isinstance(path, StringIO):
                data = self.data.get("_original_file")
            else:
                data = self.data.get(path.orig_path)

            if data is None:
                data = dict()

            return data

# Generated at 2022-06-13 16:27:57.323514
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    import ansible.template
    from ansible.vars.manager import VariableManager

    class FakeHost(object):
        def __init__(self, *args, **kwargs):
            self.get_vars = lambda: {}

    fake_vars = dict(
        hostvars=dict(fakehost=FakeHost())
    )

    fake_loader = lambda *args, **kwargs: None

    fake_inventory = lambda *args, **kwargs: None
    fake_inventory.get_host = lambda *args, **kwargs: FakeHost()

    fake_variable_manager = VariableManager(loader=fake_loader, inventory=fake_inventory)
    fake_variable_manager.extra_vars = fake_vars

    ## Basic variables

# Generated at 2022-06-13 16:28:08.161389
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    templar = Templar()

    # 1D list
    in_value = ['one', 'two']
    assert listify_lookup_plugin_terms(in_value, templar) == in_value

    # 2D list
    in_value = [['one', 'two'], ['three', 'four']]
    assert listify_lookup_plugin_terms(in_value, templar) == [['one', 'two'], ['three', 'four']]

    # String
    assert listify_lookup_plugin_terms('one', templar) == ['one']

    # Variable
    assert listify_lookup_plugin_terms('{{ var }}', templar, convert_bare=True) == ['{{ var }}']
    templar.available_variables = dict

# Generated at 2022-06-13 16:28:20.313518
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.module_utils._text import to_bytes
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import VaultLib

    vault_secret = 'test'
    vault_password = VaultLib(vault_secret).encrypt(to_bytes(vault_secret))

# Generated at 2022-06-13 16:28:27.425666
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    dataloader = DataLoader()
    templar = Templar(loader=dataloader)

    assert listify_lookup_plugin_terms('foo', templar, dataloader) == ['foo']
    assert listify_lookup_plugin_terms('foo', templar, dataloader, convert_bare=True) == ['foo']
    assert listify_lookup_plugin_terms('foo', templar, dataloader, convert_bare=False) == ['foo']
    assert listify_lookup_plugin_terms(['foo'], templar, dataloader) == ['foo']

# Generated at 2022-06-13 16:28:37.746365
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.vars import VariableManager
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    variable_manager = VariableManager()
    loader = variable_manager.get_vars_loader()
    variable_manager.set_inventory(loader.get_inventory())

    play_context = PlayContext()

    templar = Templar(loader=loader, variables=variable_manager, fail_on_undefined=True)
    terms = ['one', '{{ var1 }}', 'three', 'four']
    expected = ['one', 'two', 'three', 'four']
    variable_manager.extra_vars = {'var1': 'two'}
    templated_terms = listify_lookup_plugin_terms(terms, templar, loader)
    assert templated_terms

# Generated at 2022-06-13 16:28:46.606009
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    '''Test function listify_lookup_plugin_terms'''
    # import module snippets
    from ansible.utils.listify import listify_lookup_plugin_terms
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.template import Templar

    loader = DataLoader()

    # Set up inventory
    inventory = InventoryManager(loader=loader, sources='localhost,')

    # Set up variable_manager and templar
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    variable_manager.set_inventory(inventory)


# Generated at 2022-06-13 16:28:53.733827
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.common._collections_compat import SafeDict
    from ansible import constants as C
    from ansible.template import Templar
    from ansible.parsing.yaml.loader import AnsibleLoader

    C.DEFAULT_HASH_BEHAVIOUR = 'merge'
    templar = Templar(loader=AnsibleLoader(''))
    test_dict = dict(
        dict1 = dict(
          dict2 = dict(
            a = 5,
            b = 6,
            c = '{{ a }}',
          ),
        ),
    )
    test_dict = {k: SafeDict(v) for k, v in test_dict.items()}


# Generated at 2022-06-13 16:28:56.796582
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    # FIXME: Add tests
    pass

# Generated at 2022-06-13 16:29:03.599806
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    templar = Templar(loader=None, variables={})

    assert listify_lookup_plugin_terms('{{foo}}', templar, None, True, True) == ['{{foo}}']
    assert listify_lookup_plugin_terms('foo', templar, None, True, True) == ['foo']
    assert listify_lookup_plugin_terms(['foo', 'bar'], templar, None, True, True) == ['foo', 'bar']

    assert listify_lookup_plugin_terms('{{foo}}', templar, None, False, True) == ['{{foo}}']
    assert listify_lookup_plugin_terms('foo', templar, None, False, True) == ['foo']

# Generated at 2022-06-13 16:29:08.589564
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing import DataLoader

    data = dict(
        a=1,
        b=2,
        c=3
    )

    templar = Templar(loader=DataLoader(), variables=data)

    assert listify_lookup_plugin_terms('a={{ a }}', templar, None)           == ['a=1']
    assert listify_lookup_plugin_terms(['a={{ a }}', 'b={{ b }}'], templar, None) == ['a=1', 'b=2']
    assert listify_lookup_plugin_terms(['a={{ a }}', 'b={{ b }}'], templar, None, convert_bare=True) == ['a=1', 'b=2']
    assert listify_lookup

# Generated at 2022-06-13 16:29:15.480706
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    # For now, just test that it doesn't raise any exceptions
    try:
        listify_lookup_plugin_terms(123, None, None)
        listify_lookup_plugin_terms('{{var}}', None, None)
        listify_lookup_plugin_terms(['{{var}}'], None, None)
    except Exception:
        import traceback
        traceback.print_exc()
        raise

# Generated at 2022-06-13 16:29:22.493128
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleUnicode

    test_data = [
        '{{ lookup("pipe", "echo hello world") }}',
        AnsibleUnicode('{{ lookup("pipe", "echo hello world") }}'),
        [AnsibleUnicode('{{ lookup("pipe", "echo hello world") }}')],
        ['{{ lookup("pipe", "echo hello world") }}'],
        ['{{ lookup("pipe", "echo hello world") }}', '{{ lookup("pipe", "echo foo bar") }}'],
    ]

    templar = Templar(loader=None)

    for terms in test_data:
        result = listify_lookup_plugin_terms(terms, templar, loader=None)
        assert isinstance(result, list)

# Generated at 2022-06-13 16:29:33.492509
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible import constants as C
    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib

    # Test 1: test template function
    templar = Templar(loader=None, variables={'a': '1st', 'b': '2nd', 'dict': {'a': '3rd', 'b': '4th'}, 'list': [5, 6]}, vault_password="password")
    result = listify_lookup_plugin_terms('{{a}},{{b}}', templar, None)
    assert result == ['1st,2nd']

    # Test 2: test template function, order by dict
    templar = Templar(loader=None, variables={'dict': {'a': '3rd', 'b': '4th'}}, vault_password="password")
    result

# Generated at 2022-06-13 16:29:34.080245
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    pass

# Generated at 2022-06-13 16:29:45.655084
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.template import Templar

    loader = DataLoader()
    variable_manager = VariableManager()
    templar = Templar(loader=loader, variables=variable_manager)

    single_string_term = ['a string']
    assert listify_lookup_plugin_terms(single_string_term, templar, loader) == ['a string']

    multiple_string_terms = ['a string', 'another string']
    assert listify_lookup_plugin_terms(multiple_string_terms, templar, loader) == ['a string', 'another string']

    single_j2_term = ['"{{ foo }}"']
    variable_manager.set_nonpersistent_facts(dict(foo='bar'))

# Generated at 2022-06-13 16:29:54.522877
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar
    from ansible.vars import VariableManager

    variable_manager = VariableManager()
    variable_manager.set_host_variable("fqdn", "my_host")
    variable_manager.set_host_variable("group_names", ['my_group'])

    templar = Templar(loader=None, variables=variable_manager)

    terms = "{{fqdn}}"
    terms = listify_lookup_plugin_terms(terms, templar, loader=None)
    assert terms == ['my_host']

    terms = ["{{fqdn}}", "{{group_names}}"]
    terms = listify_lookup_plugin_terms(terms, templar, loader=None)
    assert terms == ['my_host', ['my_group']]


# Generated at 2022-06-13 16:30:03.861871
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    # test strings and lists
    t = Templar(loader=None, variables={})
    assert listify_lookup_plugin_terms(["a", "b"], templar=t, loader=None) == ["a", "b"]
    assert listify_lookup_plugin_terms("a", templar=t, loader=None) == ["a"]
    assert listify_lookup_plugin_terms(u"{{ ['a', 'b'|upper] }}", templar=t, loader=None) == ["A", "B"]
    assert listify_lookup_plugin_terms(["{{ ['a', 'b'|upper] }}"], templar=t, loader=None) == ["A", "B"]

# Generated at 2022-06-13 16:30:11.810589
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    # Test good inputs
    assert listify_lookup_plugin_terms(['foo', 'bar'], None, None) == ['foo', 'bar']
    assert listify_lookup_plugin_terms('foo', None, None) == ['foo']
    assert listify_lookup_plugin_terms(u'foo', None, None) == ['foo']
    assert listify_lookup_plugin_terms(u'foo\nbar\nbaz', None, None) == ['foo', 'bar', 'baz']

# Generated at 2022-06-13 16:30:19.655567
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    import ansible
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar

    class FakeVarsModule(object):
        def get_vars(self, loader, play, host, task):
            return None

    loader = DataLoader()
    templar = Templar(loader=loader, variables={})
    n = FakeVarsModule()
    templar._available_variables = n
    templar.set_available_variables(n)

    assert listify_lookup_plugin_terms('foo, bar', templar, loader) == ['foo', 'bar']
    assert listify_lookup_plugin_terms(['foo, bar'], templar, loader) == ['foo, bar']

# Generated at 2022-06-13 16:30:31.210146
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    # Test string and list with Iterable
    assert ['test'] == listify_lookup_plugin_terms('test', None, None)
    assert ['test'] == listify_lookup_plugin_terms(['test'], None, None)

    # Test string and list without Iterable
    assert ['test'] == listify_lookup_plugin_terms('test', None, None, convert_bare=True)
    assert ['test'] == listify_lookup_plugin_terms(['test'], None, None, convert_bare=True)

    # Test string and list with multiple items
    assert ['test1', 'test2'] == listify_lookup_plugin_terms(['test1', 'test2'], None, None)

# Generated at 2022-06-13 16:30:39.234381
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    """
    Test listify_lookup_plugin_terms
    """
    from ansible.module_utils.common._collections_compat import Sequence
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar

    # example vars data
    vars_data = {
        'var1': 'value1',
        'var2': [1, 2, 3, 4, 5],
        'var3': { 'k1': 'v1', 'k2': 'v2', 'k3': 'v3' },
    }

    loader = DataLoader()
    templar = Templar(loader=loader, variables=vars_data)

    # test a string
    term = 'value{{ var1 }}'

# Generated at 2022-06-13 16:30:45.760228
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar

    loader = DataLoader()
    templar = Templar(loader=loader)

    # answer should be a list of values with items that are a string
    assert listify_lookup_plugin_terms([1,2,3], templar, loader) == [1,2,3]

    assert listify_lookup_plugin_terms([1,2,3], templar, loader) == [1,2,3]

    assert listify_lookup_plugin_terms(["foo", "bar"], templar, loader) == ["foo", "bar"]

    # answer should be a list of values with items that are still variables

# Generated at 2022-06-13 16:30:58.579993
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    loader = DataLoader()

    templar = Templar(loader=loader, variable_manager=variable_manager)

    terms = "{{ ['foo', 'bar'] }}"
    listified_terms = listify_lookup_plugin_terms(terms, templar, loader)
    assert listified_terms == ["foo", "bar"]

    terms = ["123", "456"]
    listified_terms = listify_lookup_plugin_terms(terms, templar, loader)
    assert listified_terms == ["123", "456"]

    terms = "{{ var1 }}"

# Generated at 2022-06-13 16:31:08.859311
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.vars import VariableManager
    from ansible.template import Templar
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext

    loader = AnsibleLoader(None, None)

    inv_data = '''
    [all]
    localhost ansible_connection=local

    [all:vars]
    foo: bar
    '''

    variables = VariableManager()
    inventory = InventoryManager(loader=loader, sources=[inv_data])
    variables.set_inventory(inventory)

    play_context = PlayContext()
    templar = Templar(loader=loader, variables=variables, disable_lookups=False)


# Generated at 2022-06-13 16:31:18.513361
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    # There is no good way to test this function directly so we use a test structure and call
    # the function indirectly.
    from ansible.plugins.lookup import lineinfile
    test_terms = lineinfile.LookupModule(loader=None, templar=None, **{}).listify_lookup_plugin_terms

    templar = Templar(loader=None, variables={})
    assert ['foo'] == test_terms('foo', templar, None)
    assert ['bar'] == test_terms(' bar ', templar, None)
    assert ['baz', 'bam'] == test_terms('baz,bam', templar, None)
    assert ['baz', 'bam'] == test_terms('baz, bam', templar, None)

# Generated at 2022-06-13 16:31:28.447210
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    loader = object()  # dummy arg that is not used
    templar = Templar(loader=loader, variables={'var': 'variable_value'})

    # String term with a variable
    terms = '{{ var }}'
    result = listify_lookup_plugin_terms(terms, templar, loader)
    assert len(result) == 1
    assert isinstance(result[0], string_types)
    assert result[0] == 'variable_value'

    # String term without a variable
    terms = 'string_value'
    result = listify_lookup_plugin_terms(terms, templar, loader)
    assert len(result) == 1

# Generated at 2022-06-13 16:31:38.716709
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible import constants as C
    from ansible.plugins.loader import lookup_loader

    # Returns list when passed a string
    assert listify_lookup_plugin_terms('foo', lookup_loader.get('identity', basedir=C.DEFAULT_LOCAL_TMP), lookup_loader) == ['foo']
    # Returns list when passed a list
    assert listify_lookup_plugin_terms(['foo', 'bar'], lookup_loader.get('identity', basedir=C.DEFAULT_LOCAL_TMP), lookup_loader) == ['foo', 'bar']
    # Returns list when passed a comma separated string

# Generated at 2022-06-13 16:31:49.824623
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    import os
    import sys
    import pytest
    from ansible.module_utils.six import PY3

    # add the current directory to the module path
    sys.path.append(os.path.dirname(__file__))
    from ansible.template import Templar

    test_data = list()

    # Case 1: Simple string
    templar = Templar(loader=None, variables={})
    test_case_data = list()
    test_case_data.append("my_var_value")
    test_case_data.append(templar)
    test_case_data.append(None)
    test_case_data.append(True)
    test_case_data.append(False)
    test_data.append(tuple(test_case_data))

    # Case 2: Simple list


# Generated at 2022-06-13 16:31:58.041144
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    # Make sure we can always handle strings as input
    # NOTE: stringify_values is intentionally skipped because it might be removed in the future
    # and the tests here should fail if that happens
    for term in ['string', AnsibleUnsafeText(u'string'), u'string']:
        assert listify_lookup_plugin_terms(term, None, None) == ['string']

    # Make sure we can always handle lists as input, even if the items in the list are not strings
    # NOTE: stringify_values is intentionally skipped because it might be removed in the future
    # and the tests here should fail if that happens

# Generated at 2022-06-13 16:32:03.086178
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible import constants as C

    class TestVarsModule(object):
        def __init__(self, variables):
            self.RESULTS = variables

    class TestTemplar(Templar):
        def __init__(self, variables):
            self._available_variables = variables

        def available_variables(self):
            return self._available_variables

        def template(self, *args, **kwargs):
            return super(TestTemplar, self).template(*args, variables=self._available_variables, **kwargs)

    def test_hostvars(hostvars):
        return hostvars

    # Basic string
    templar = TestTemplar(TestVarsModule(dict(omg='wtf')))
    assert listify_lookup_plugin

# Generated at 2022-06-13 16:32:14.051915
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    # Create a mock environment to test against
    group_vars = dict(a="a1", b="b1")
    host_vars = dict(a="a2", c="c2")
    templar = Templar(loader=DataLoader(), variables=VariableManager(),
                      shared_loader_obj=None, host=Host("example.org"),
                      exclude_hosts=[], exclude_vars=[])

    # Test a single string

# Generated at 2022-06-13 16:32:22.688226
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.utils.vars import combine_vars
    from ansible.parsing.vault import VaultLib
    from ansible.utils.display import Display
    from ansible.utils.vars import load_extra_vars
    from ansible.utils.vars import load_options_vars
    from ansible.utils.vars import load_group_vars
    from ansible.utils.vars import load_host_vars
    from ansible.utils.vars import merge_hash
    from ansible.errors import AnsibleError
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play

# Generated at 2022-06-13 16:32:48.045981
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.vault import VaultLib

    # Set up templar and loader
    vault_secret = 'mysecret'
    vault_password_file = os.path.join(os.path.dirname(__file__), 'vault_password')
    loader = DataLoader()
    vault = VaultLib([(vault_secret, vault_password_file)], loader=loader)
    templar = Templar(loader=loader, variables={}, vault_secrets=vault.secrets)

    # Test listify_lookup_plugin_terms with a string
    assert listify_lookup_plugin_terms("{{test_var}}", templar, loader) == ['foo']

    # Test listify_lookup_plugin_terms with a list

# Generated at 2022-06-13 16:32:57.361764
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.playbook.templar import Templar
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    var_mgr = VariableManager()
    templar = Templar(loader=loader, variables=self.var_mgr)

    terms = listify_lookup_plugin_terms("{{a}}", templar, loader, fail_on_undefined=False)
    assert terms == [u'{{a}}']

    terms = listify_lookup_plugin_terms("{{a}}", templar, loader, fail_on_undefined=False, convert_bare=True)
    assert terms == [u'{{a}}']


# Generated at 2022-06-13 16:33:07.402420
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.vars.templar import Templar
    from ansible.parsing.yaml.objects import AnsibleUnicode
    assert listify_lookup_plugin_terms([], Templar({}), None) == []

    # test string input
    terms = AnsibleUnicode('one')
    result = listify_lookup_plugin_terms(terms, Templar({}), None)
    assert isinstance(result, list)
    assert result == ['one']

    # test list input
    terms = [AnsibleUnicode('one'), AnsibleUnicode('two')]
    result = listify_lookup_plugin_terms(terms, Templar({}), None)
    assert isinstance(result, list)
    assert result == ['one', 'two']

    # test dict input

# Generated at 2022-06-13 16:33:07.909962
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    pass

# Generated at 2022-06-13 16:33:15.678390
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    class VarsModule:
        def get_vars(self, loader, path, entities):
            return {}

    my_vars = dict(
        foo='bar',
        baz='test'
    )
    loader = DataLoader()
    templar = Templar(loader=loader, variables=my_vars)

    terms = listify_lookup_plugin_terms('{{ foo }}', templar, loader)

    assert isinstance(terms, list)
    assert len(terms) == 1
    assert 'bar' in terms

    terms = listify_lookup_plugin_terms(['{{ foo }}', '{{ baz }}'], templar, loader)

    assert isinstance(terms, list)

# Generated at 2022-06-13 16:33:24.518257
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    # from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

    # variable_manager = VariableManager()
    templar = Templar(loader=loader)

    # Test invalid term
    result = listify_lookup_plugin_terms(1, templar, loader)
    assert result == [1], result

    # Test single term
    result = listify_lookup_plugin_terms('hello', templar, loader)
    assert result == ['hello'], result

    # Test single term in list
    result = listify_lookup_plugin_terms(['hello'], templar, loader)
    assert result == ['hello'], result

    # Test multiple terms in list
    result = listify

# Generated at 2022-06-13 16:33:31.443993
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play = Play().load({}, variable_manager=variable_manager, loader=loader)
    templar = Templar(loader=loader, inventory=inventory, variables=variable_manager)
    single_term = "a.txt"
    terms = [single_term]
    term_list = listify_lookup_plugin_terms(terms, templar, loader)
    assert type(term_list) is list


# Generated at 2022-06-13 16:33:41.617203
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.utils.unsafe_proxy import AnsibleUnsafeBytes

    from ansible.template import Templar
    from ansible.parsing.yaml.loader import AnsibleLoader

    terms_in         = b'{{ foo }},bar,baz,boo'
    terms_in_ac      = AnsibleUnsafeBytes(terms_in)
    terms_in_at      = AnsibleUnsafeText(terms_in)

    terms_expected   = ['foo', 'bar', 'baz', 'boo']

    # Input is bytes
    loader = AnsibleLoader(None, {})
    templar = Templar(loader=loader)

    terms_out = listify_lookup_plugin_terms(terms_in, templar)
   

# Generated at 2022-06-13 16:33:49.645883
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    # Do not remove these imports - used in unittest
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.vars.manager import VariableManager

    my_vars = dict(foo='bar', spam='eggs', number=42)
    my_loader = 'dummy_loader'
    my_variable_manager = VariableManager()
    my_variable_manager.set_nonpersistent_facts(my_loader, my_vars)

    templar = Templar(loader=my_loader, variables=my_variable_manager)


# Generated at 2022-06-13 16:34:00.715435
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    '''
    listify_lookup_plugin_terms: test of proper string or list is returned
    '''
    from ansible import errors
    from ansible.utils.vars import AnsibleVars
    from ansible.template import Templar
    class mock_loader:
        pass
    class mock_plugin:
        def __init__(self):
            self.templar = Templar(loader=mock_loader, variables=AnsibleVars())
        def template(self, value):
            return value
    v = mock_plugin()
    assert 'foo' == listify_lookup_plugin_terms('foo', v)
    assert ['foo', 'bar'] == listify_lookup_plugin_terms(['foo', 'bar'], v)

# Generated at 2022-06-13 16:34:37.204771
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible import errors
    from ansible.template import Templar

    templar = Templar(loader=None, variables={}, fail_on_undefined=True)

    assert listify_lookup_plugin_terms(None, templar, None) == [None]
    assert listify_lookup_plugin_terms('string', templar, None) == ['string']
    assert listify_lookup_plugin_terms(['array', 'of', 'strings'], templar, None) == ['array', 'of', 'strings']

    assert listify_lookup_plugin_terms('"string"', templar, None) == ['string']
    assert listify_lookup_plugin_terms(['"array"', 'of', '"strings"'], templar, None) == ['array', 'of', 'strings']
   

# Generated at 2022-06-13 16:34:46.136519
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.template import Templar

    assert listify_lookup_plugin_terms('foo', Templar(None, loader=None), None) == ['foo']
    assert listify_lookup_plugin_terms(['foo'], Templar(None, loader=None), None) == ['foo']
    assert listify_lookup_plugin_terms(['foo', 'bar'], Templar(None, loader=None), None) == ['foo', 'bar']
    assert listify_lookup_plugin_terms(AnsibleUnsafeText('foo'), Templar(None, loader=None), None) == ['foo']

# Generated at 2022-06-13 16:34:53.770676
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.vars.manager import VariableManager

    templar = Templar(loader=None, variables=VariableManager())

    term = AnsibleMapping()
    term.update({'a': 'b'})

    # Test string type template
    ret = listify_lookup_plugin_terms('my-string', templar, None)
    assert isinstance(ret, list)
    assert ret == ['my-string']

    ret = listify_lookup_plugin_terms([term], templar, None)
    assert isinstance(ret, list)
    assert str(ret) == '[<AnsibleMapping: {u\'a\': u\'b\'}>]'

    ret = listify_look

# Generated at 2022-06-13 16:35:02.085234
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    # First test: no conversion, var is a string
    # -------------
    test_var = "test"
    expected_output = ["test"]
    assert listify_lookup_plugin_terms(test_var, None, None) == expected_output

    # Second test: no conversion, var is a list
    # -------------
    test_var = ["test"]
    expected_output = ["test"]
    assert listify_lookup_plugin_terms(test_var, None, None) == expected_output

    # Third test: conversion, var is a string
    # -------------
    test_var = "{ 'test': 'test'}"
    expected_output = [{'test': 'test'}]
    assert listify_lookup_plugin_terms(test_var, None, None, convert_bare=True) == expected_output