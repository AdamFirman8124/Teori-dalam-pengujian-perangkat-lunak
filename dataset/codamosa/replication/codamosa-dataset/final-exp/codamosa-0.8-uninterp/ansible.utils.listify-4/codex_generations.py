

# Generated at 2022-06-13 16:25:07.530230
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    assert listify_lookup_plugin_terms('1', None, None) == [1]
    assert listify_lookup_plugin_terms(['1', '2'], None, None) == [1, 2]
    assert listify_lookup_plugin_terms([1, 2], None, None) == [1, 2]
    assert listify_lookup_plugin_terms(1, None, None) == [1]
    assert listify_lookup_plugin_terms(None, None, None) == [None]

# Generated at 2022-06-13 16:25:18.668809
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    # Test string
    t = Templar(loader=None, variables={'a': [1, 2, 3], 'b': "c"})
    result = listify_lookup_plugin_terms('{{ a }}', t, None)
    assert result == ['1', '2', '3']

    # Test string with default term
    result = listify_lookup_plugin_terms('{{ a }}', t, None, fail_on_undefined=False)
    assert result == ['1', '2', '3']

    # Test list
    result = listify_lookup_plugin_terms(['{{ a }}', '{{ b }}'], t, None)
    assert result == ['1', '2', '3', 'c']

    # Test list with default term
    result = listify_lookup

# Generated at 2022-06-13 16:25:27.987063
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from units.mock.loader import DictDataLoader

    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar

    # Ensure a list is returned even if a string is passed in
    loader = DataLoader()
    templar = Templar(loader=loader)
    terms = ["{ test_var }"]
    loader.set_basedir("./")
    loader.set_data({'test_var': 'Test String'}, "")
    expected_result = ['Test String']

    result = listify_lookup_plugin_terms(terms, templar, loader)
    assert result == expected_result

    # string is encoded to safe_unicode using to_text() if not a string


# Generated at 2022-06-13 16:25:38.382868
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleUnicode
    assert(listify_lookup_plugin_terms('foo, bar', Templar({}), lambda x: x) == [u'foo', u'bar'])
    assert(listify_lookup_plugin_terms(['foo', 'bar'], Templar({}), lambda x: x) == [u'foo', u'bar'])
    assert(listify_lookup_plugin_terms([u'foo', u'bar'], Templar({}), lambda x: x) == [u'foo', u'bar'])
    assert(listify_lookup_plugin_terms(AnsibleUnicode('foo'), Templar({}), lambda x: x) == [u'foo'])

# Generated at 2022-06-13 16:25:50.873404
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.utils.unsafe_proxy import AnsibleUnsafeText, wrap_var

    from ansible.template import Templar
    from ansible.parsing.yaml.loader import AnsibleLoader

    wrapper = wrap_var

    assert listify_lookup_plugin_terms('foobar', Templar(loader=AnsibleLoader), loader, fail_on_undefined=True, convert_bare=False) == [u'foobar']
    assert listify_lookup_plugin_terms('foobar', Templar(loader=AnsibleLoader), loader, fail_on_undefined=False, convert_bare=False) == [u'foobar']

# Generated at 2022-06-13 16:26:02.002753
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    class FakeTemplar(object):
        def template(self, data, fail_on_undefined=True, convert_bare=False):
            return data

    class FakeLoader(object):
        pass

    templar = FakeTemplar()
    loader = FakeLoader()

    # Test 'my_var' (variable)
    data = 'my_var'
    expected = ['my_var']
    assert listify_lookup_plugin_terms(data, templar, loader) == expected

    # Test ['my_var', 'my_var2'] (list)
    data = ['my_var', 'my_var2']
    expected = ['my_var', 'my_var2']
    assert listify_lookup_plugin_terms(data, templar, loader) == expected

    # Test {'key': '

# Generated at 2022-06-13 16:26:12.735882
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    import yaml
    from ansible.template import Templar
    from ansible.vars import VariableManager

    terms = '{{ item }}'
    items = [1, 2, 'three']
    vars = {
        'item': items[0],
        'hostvars': {
            'host0': {
                'item': items[1],
            },
            'host1': {
                'item': items[2],
            },
        }
    }

    variable_manager = VariableManager()
    variable_manager.set_host_variable('host1', vars['hostvars']['host1'])
    variable_manager.set_host_variable('host0', vars['hostvars']['host0'])
    variable_manager.set_nonpersistent_facts(vars)

    templar

# Generated at 2022-06-13 16:26:21.081343
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    data = 'foo'
    loader = DataLoader()
    templar = Templar(loader=loader)

    assert listify_lookup_plugin_terms(data, templar, loader) == ['foo']

    data = 'foo,bar'
    assert listify_lookup_plugin_terms(data, templar, loader) == ['foo', 'bar']

    data = ['foo,bar']
    assert listify_lookup_plugin_terms(data, templar, loader) == ['foo', 'bar']

    data = ['foo', 'bar']
    assert listify_lookup_plugin_terms(data, templar, loader) == ['foo', 'bar']

    data = 'foo{{a}}'


# Generated at 2022-06-13 16:26:32.464449
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    class UnitTestTemplar(Templar):
        def __init__(self, variables):
            self._available_variables = variables

        def available_variables(self):
            return self._available_variables

    # Create an instance of the templar so tests can use its methods
    templar = Templar(DataLoader(), variables={})

    # Test with a string
    terms = listify_lookup_plugin_terms('{{ foo }}', templar, None, fail_on_undefined=True)
    assert terms == ['{{ foo }}']

    # Test with a variable that is a string

# Generated at 2022-06-13 16:26:42.655365
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.config.manager import ConfigManager
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play

    config_manager = ConfigManager(load_vocab=False)
    templar = Templar(loader=DataLoader(),
                      variables=VariableManager(loader=DataLoader()),
                      inventory=InventoryManager(loader=DataLoader()))
    play = Play().load({}, loader=DataLoader(), variable_manager=VariableManager(loader=DataLoader()), templar=templar)

    terms = 'localhost, host.example.com, remotehost.example.com'

# Generated at 2022-06-13 16:26:50.962883
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    # Fixture loading
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    import pytest

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list=[])
    variable_manager.set_inventory(inventory)

    terms = '{{ item }}'
    templar = Templar(loader=loader, variables=variable_manager)

    # test that listify_lookup_plugin_terms produces a list
    assert isinstance(listify_lookup_plugin_terms(terms, templar, loader, fail_on_undefined=True, convert_bare=False), list)

    # test that the variables

# Generated at 2022-06-13 16:26:58.061862
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.playbook.play_context import PlayContext

    templar = Templar(loader=None, variables={})
    terms = "{{ foo }}:{{ bar }}"
    result = listify_lookup_plugin_terms(terms, templar, loader=None)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] == "{{ foo }}:{{ bar }}"

    terms = [1, 2, 3]
    result = listi

# Generated at 2022-06-13 16:27:06.941564
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible import constants as C
    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib
    from ansible.utils.vars import combine_vars
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.yaml.dumper import AnsibleDumper

    class DummyVars(dict):
        def get_vars(self, loader=None, play=None, host=None, task=None):
            return self

    vars_manager = DummyVars()

    my_string = "{{ 'string1' if a == 2 else 'string2' }}"
    my_string2 = "string3"
    my_list = [my_string, my_string2]


# Generated at 2022-06-13 16:27:17.566126
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    try:
        basestring
    except NameError:
        basestring = string_types
    assert listify_lookup_plugin_terms('a', 'b', 'c', True, False) == 'a'
    assert listify_lookup_plugin_terms(['a', 'b'], 'b', 'c', True, False) == ['a', 'b']
    assert listify_lookup_plugin_terms('{{a}}', 'b', 'c', True, False) == '{{a}}'
    assert listify_lookup_plugin_terms(['{{a}}', '{{b}}'], 'b', 'c', True, False) == ['{{a}}', '{{b}}']

# Generated at 2022-06-13 16:27:26.183753
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    # test string type
    terms = 'abc'
    t = Templar(loader=None, variables={'abc':['a', 'b', 'c']})
    r = listify_lookup_plugin_terms(terms, templar=t, loader=None)
    assert isinstance(r, list)
    assert r == ['a', 'b', 'c']

    # test listify
    terms = ['a', 'b', 'c']
    r = listify_lookup_plugin_terms(terms, templar=t, loader=None)
    assert isinstance(r, list)
    assert r == ['a', 'b', 'c']

# Generated at 2022-06-13 16:27:30.878022
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    templar = Templar(variables={})

    assert listify_lookup_plugin_terms(1, templar, None) == [1]
    assert listify_lookup_plugin_terms([1, 2], templar, None) == [1, 2]
    assert listify_lookup_plugin_terms("1", templar, None) == ["1"]
    assert listify_lookup_plugin_terms(["1", "2"], templar, None) == ["1", "2"]

# Generated at 2022-06-13 16:27:41.707517
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.common._collections_compat import Sequence
    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib

    templar = Templar(loader=None, variables={'bar': 'foo'}, fail_on_undefined=True)
    templar.environment.loader.get_basedir = lambda x: '/'
    templar._available_variables = templar._get_variables(loader=templar.loader, vault_secrets=VaultLib())
    assert isinstance(listify_lookup_plugin_terms(terms='1', templar=templar, loader=None), Sequence)
    assert listify_lookup_plugin_terms(terms='1', templar=templar, loader=None) == ['1']

# Generated at 2022-06-13 16:27:51.449411
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    terms_as_string = '{{ lookup("env", "HOME") }}'
    terms_as_dict = {"string": "{{ lookup('env', 'HOME') }}",
                     "list": ["{{ lookup('env', 'HOME') }}", "{{ lookup('env', 'HOME') }}"],
                     "dict": {"key": "{{ lookup('env', 'HOME') }}"}}
    terms_as_list = ["{{ lookup('env', 'HOME') }}", {"dict": "{{ lookup('env', 'HOME') }}"}]

    templar = Templar(loader=DataLoader())


# Generated at 2022-06-13 16:28:01.840301
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.utils.listify import listify_lookup_plugin_terms

    # Test variable string
    assert listify_lookup_plugin_terms('a string variable') == ['a string variable']
    # Test variable list
    assert listify_lookup_plugin_terms(['a', 'list', 'variable']) == ['a', 'list', 'variable']
    # Test variable dict
    assert listify_lookup_plugin_terms({'a': 'dict', 'variable': 'is a string'}) == [{'a': 'dict', 'variable': 'is a string'}]
    # Test variable empty
    assert listify_lookup_plugin_terms([]) == []
    # Test variable None
    assert listify_lookup_plugin_terms(None) == [None]

# Generated at 2022-06-13 16:28:07.972750
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    terms = ['{{ foo }}', 'bar', '{{ baz }}', '{{ bam }}']
    variables = dict(foo='foo', bar='bar', baz='baz', bam='bam')
    templar = Templar(loader=None, variables=variables)

    result = listify_lookup_plugin_terms(terms, templar)

    assert result == ['foo', 'bar', 'baz', 'bam']

# Generated at 2022-06-13 16:28:19.959108
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins.loader import lookup_loader
    
    loader = AnsibleLoader(None, variable_manager=VariableManager(), inventory_manager=InventoryManager(loader=loader))
    templar = Templar(loader=loader, variables=dict())
    
    class MyLookup:
        def __init__(self, templar, loader, terms, variables=None):
            self.terms = terms
    
    my_lookup = MyLookup(templar, loader, "{{ blah }}")

# Generated at 2022-06-13 16:28:28.993208
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleUnicode

    # create a dummy environment for listify_lookup_plugin_terms to use
    templar = Templar({}, {}, {}, loader=None)

    # test with the following values (first val) and expect the corresponding (second val) results

# Generated at 2022-06-13 16:28:38.568733
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    vault_password = '$1$VT0GmovF$m8qmOWYZhbGlmLAi/Wvu9.'
    vault = VaultLib([vault_password])

    terms = ['{{"{{foo}}"}}', '{{bar}}', 123, ['abc', 'efg'], '{{hij}}']
    templar = Templar(loader=None, variables={u'foo': u'FOO', u'bar': [u'BAR', u'BAZ'], u'hij': AnsibleVaultEncryptedUnicode(u'HIJ', vault)})
    result = listify_lookup

# Generated at 2022-06-13 16:28:47.194732
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from jinja2 import Template
    fake_loader = None
    templar = Template('{{var}}')
    assert listify_lookup_plugin_terms(u'foo', templar, fake_loader) == ['foo']
    assert listify_lookup_plugin_terms(u'foo bar', templar, fake_loader) == ['foo bar']
    assert listify_lookup_plugin_terms(u'"foo bar"', templar, fake_loader) == ['foo bar']
    assert listify_lookup_plugin_terms(u'"foo bar" "foo baz"', templar, fake_loader) == ['foo bar', 'foo baz']
    assert listify_lookup_plugin_terms(['foo', 'bar'], templar, fake_loader) == ['foo', 'bar']

# Generated at 2022-06-13 16:28:52.160709
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    # Basic cases
    t = Templar(loader=None)
    assert listify_lookup_plugin_terms("bar", templar=t, loader=None) == ["bar"]
    assert listify_lookup_plugin_terms(["bar", "baz"], templar=t, loader=None) == ["bar", "baz"]
    assert listify_lookup_plugin_terms(42, templar=t, loader=None) == [42]
    assert listify_lookup_plugin_terms(42.0, templar=t, loader=None) == [42.0]
    assert listify_lookup_

# Generated at 2022-06-13 16:29:01.396945
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    templar = Templar(loader=None)

    # Single string
    assert listify_lookup_plugin_terms('single_string', templar, fail_on_undefined=False) == ['single_string']

    # String inside a list
    assert listify_lookup_plugin_terms(['single_string'], templar, fail_on_undefined=False) == ['single_string']

    # List of strings
    assert listify_lookup_plugin_terms(['first_string', 'second_string'], templar, fail_on_undefined=False) == ['first_string', 'second_string']

    # Empty list
    assert listify_lookup_plugin_terms([], templar, fail_on_undefined=False) == []

# Generated at 2022-06-13 16:29:06.656291
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    assert listify_lookup_plugin_terms('foo', None, None) == ['foo']
    assert listify_lookup_plugin_terms('foo,bar', None, None) == ['foo', 'bar']
    assert listify_lookup_plugin_terms(['foo', 'bar'], None, None) == ['foo', 'bar']

# Generated at 2022-06-13 16:29:18.198841
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from io import StringIO
    # some variables we will use in the tests
    test_value = 'I have a #hashtag'
    test_value_encoded = 'I have a %23hashtag'
    test_list_value = ['one', 'two', 'three']
    test_list_value_encoded = ['one', 'two', 'three']
    test_dict_value = {u'one': u'two', u'three': u'four'}
    test_dict_value_encoded = {u'one': u'two', u'three': u'four'}
    non_encodable = '\U00010301'

# Generated at 2022-06-13 16:29:29.868184
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.template import Templar

    # Single string variable
    templar = Templar()
    single_str = 'Single String Variable'
    assert listify_lookup_plugin_terms(single_str, templar, None, fail_on_undefined=True, convert_bare=False) == [single_str]

    # Single string with ansible.vars.unsafe_proxy.AnsibleUnsafeText
    templar = Templar()
    single_str = AnsibleBaseYAMLObject('Single String Variable')
    assert listify_lookup_plugin_terms(single_str, templar, None, fail_on_undefined=True, convert_bare=False) == [single_str]

    # Single list with a

# Generated at 2022-06-13 16:29:32.155698
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    pass

# Generated at 2022-06-13 16:29:45.657162
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    class FakeVarsModule(object):
        def __init__(self, **kwargs):
            self.data = kwargs

        def __getitem__(self, key):
            return self.data[key]

        def __contains__(self, key):
            return key in self.data

    t = Templar(variables=FakeVarsModule(a="a", b="b", c="c", d="d", e="e", f="f"))
    assert listify_lookup_plugin_terms("{{ a }}", t, None) == [t.template("{{ a }}")]
    assert listify_lookup_plugin_terms(["{{ a }}", "{{ b }}"], t, None) == [t.template("{{ a }}"), t.template("{{ b }}")]
   

# Generated at 2022-06-13 16:29:46.668871
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    # TODO: implement this test
    pass

# Generated at 2022-06-13 16:29:54.975560
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    class MyTemplar(object):
        def __init__(self, loader):
            self.loader = loader
        def template(self, terms, **kwargs):
            return terms

    class MyVars(dict):
        def __init__(self, *args, **kwargs):
            super(MyVars, self).__init__(*args, **kwargs)
        def get(self, key, *args, **kwargs):
            return super(MyVars, self).get(key, *args, **kwargs)

    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()

    templar = MyTemplar(loader)
    vars = MyVars({"a": "b"})
    loader._add_variable_mapping('vars', vars)

   

# Generated at 2022-06-13 16:30:03.784252
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    '''Return value should be a list, no matter what is passed to the function'''
    # Pass a string
    assert isinstance(listify_lookup_plugin_terms("hello world"), list)
    # Pass a list of strings
    assert isinstance(listify_lookup_plugin_terms(["hello","world"]), list)
    # Pass a list of lists
    assert isinstance(listify_lookup_plugin_terms([["hello","world"]]), list)
    # Pass a list
    assert isinstance(listify_lookup_plugin_terms(["hello","world"]), list)
    # PASS an int
    assert isinstance(listify_lookup_plugin_terms(1), list)
    # Pass a dict
    assert isinstance(listify_lookup_plugin_terms({"hello":"world"}), list)
   

# Generated at 2022-06-13 16:30:15.051498
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    # Testing import
    from ansible.template import Templar
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    v = VariableManager()
    l = AnsibleLoader(None, v)

    i = InventoryManager(loader=l, sources=['localhost,'])
    t = Templar(loader=l, variables=v, inventory=i)

    # Testing: listify_lookup_plugin_terms(terms, templar, loader, fail_on_undefined=True)
    terms = ['{{ var1 }}', '{{ var2 }}']
    data = {
        "var1": "foo",
        "var2": "bar"
    }

# Generated at 2022-06-13 16:30:21.510113
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    class FakeModule(object):
        def __init__(self, params):
            self._params=params

        def get_options(self):
            return dict(self._params)

    class FakeTemplar(object):
        def __init__(self):
            self._params={}

        def set_available_variables(self, params):
            self._params = params

        def template(self, terms, fail_on_undefined=True, convert_bare=False):
            for k, v in terms.items():
                if isinstance(v, dict) and 'var' in v.keys():
                   v = self._params[v['var']]
                terms[k] = v
            return terms

    import sys
    class FakeFactsModule(object):
        def __init__(self):
            self._params={}

# Generated at 2022-06-13 16:30:32.269970
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    templar = Templar()

    data = """
          - key: "val"
          foo: "{{ lookup_me }}"
          other: "stuff"
    """
    prep_data = templar.template(data, convert_bare=True)
    assert prep_data['foo'] == '{{ lookup_me }}'

    prep_data['foo'] = 'vars_are_good'
    assert prep_data['foo'] == 'vars_are_good'

    prep_data['_raw_params'] = '{{ not_used }}'
    assert prep_data['_raw_params'] == '{{ not_used }}'

    prep_data['_raw_params'] = templar.template('{{ lookup_me }}', convert_bare=True)

# Generated at 2022-06-13 16:30:42.484278
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    # Check normal case of list
    assert listify_lookup_plugin_terms([1,2,3]) == [1,2,3]

    # Check normal case of string
    assert listify_lookup_plugin_terms('1') == [1]

    # Check normal case of unicode
    assert listify_lookup_plugin_terms(u'1') == [1]

    # Check normal case of forced string to list
    assert listify_lookup_plugin_terms('1', force_list=True) == [1]

    # Check normal case of forced unicode to list
    assert listify_lookup_plugin_terms(u'1', force_list=True) == [1]

    # Check no case of forced int to list

# Generated at 2022-06-13 16:30:53.358121
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    mock_loader = False
    mock_fail_on_undefined = False

    templar = Templar(loader=mock_loader)

    # Test when the terms is not a string or iterable
    mock_terms = 123
    resulting_terms = listify_lookup_plugin_terms(mock_terms, templar, loader=mock_loader, fail_on_undefined=mock_fail_on_undefined)
    assert resulting_terms == [mock_terms]

    # Test when the terms is a string but not a template
    mock_terms = 'foo'
    resulting_terms = listify_lookup_plugin_terms(mock_terms, templar, loader=mock_loader, fail_on_undefined=mock_fail_on_undefined)
   

# Generated at 2022-06-13 16:31:00.327029
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.plugins.loader import lookup_loader

    assert listify_lookup_plugin_terms(1, lookup_loader) == [1]
    assert listify_lookup_plugin_terms([1,2], lookup_loader) == [1,2]
    assert listify_lookup_plugin_terms("1,2", lookup_loader) == ['1,2']
    assert listify_lookup_plugin_terms("1,2", lookup_loader, convert_bare=True) == ['1','2']
    assert listify_lookup_plugin_terms("1,{{ foo }},2", lookup_loader) == ['1,{{ foo }},']

# Generated at 2022-06-13 16:31:12.162597
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    # for testing
    def fail_on_undefined(var):
        raise Exception("it failed")

    templar = Templar(loader=None, variables={})

    # no vars, just return an array
    assert ['A', 'B', 'C'] == listify_lookup_plugin_terms(['A', 'B', 'C'], templar, loader=None)
    assert ['A', 'B', 'C'] == listify_lookup_plugin_terms('A B C', templar, loader=None)
    assert ['A', 'B', 'C'] == listify_lookup_plugin_terms('A,B,C', templar, loader=None)

    # more complex cases, with lowering/vars

# Generated at 2022-06-13 16:31:19.868265
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()
    templar = Templar(loader=loader, variables=variable_manager)

    assert listify_lookup_plugin_terms([1, 2], templar, loader) == [1, 2]
    assert listify_lookup_plugin_terms([1, '2'], templar, loader) == [1, '2']
    assert listify_lookup_plugin_terms('1,2', templar, loader) == ['1', '2']

# Generated at 2022-06-13 16:31:29.259123
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    loader = DataLoader()
    jinja2_env = Environment()
    templar = Templar(loader=loader, variables=variable_manager, env=jinja2_env)

    assert listify_lookup_plugin_terms(["1", "2.3"], templar, loader) == ["1", "2.3"]
    assert listify_lookup_plugin_terms(["1", "{{a}}"], templar, loader) == ["1", "{{a}}"]
    assert listify_lookup_plugin_terms("1", templar, loader) == ["1"]

# Generated at 2022-06-13 16:31:39.307936
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.module_utils.common._collections_compat import Mapping, Sequence
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar

    loader = DataLoader()
    variable_manager = VariableManager()
    templar = Templar(loader=loader, variables=variable_manager)

    # test None
    result = listify_lookup_plugin_terms(None, templar, loader)
    assert result == []

    # test empty string
    result = listify_lookup_plugin_terms("", templar, loader)
    assert result == []

    # test whitespace string
    result = listify_lookup_plugin_terms("   ", templar, loader)
    assert result == []

    # test

# Generated at 2022-06-13 16:31:50.040709
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.utils.nested_dict import nested_dict

    class _MockTemplar(object):

        def __init__(self, name, template_data):
            self.name = name
            self.template_data = template_data

        def template(self, value, convert_bare=False, fail_on_undefined=True, override_vars=None):

            if fail_on_undefined:
                new_value = []
                for item in value:
                    if not isinstance(item, string_types):
                        new_value.append(item)
                        continue

                    if item not in self.template_data:
                        raise ValueError("TemplateUndefinedVariable: unable to look up a name or access an attribute in template string (%s). Error was: %s" % (item, item))

                    new_value.append

# Generated at 2022-06-13 16:31:58.145925
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    templar = Templar(loader=loader)

    ## Simple case of string
    input_string = 'input_string'
    expected_result = ['input_string']
    result = listify_lookup_plugin_terms(input_string, templar, loader, False)
    assert result == expected_result

    ## Simple list
    input_list = ['input_list1', 'input_list2']
    expected_result = ['input_list1', 'input_list2']
    result = listify_lookup_plugin_terms(input_list, templar, loader, False)
    assert result == expected_result

    ## Simple dictionary

# Generated at 2022-06-13 16:32:10.214413
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils._text import to_text

    from ansible.template import Templar

    # make sure single value in a list works
    assert listify_lookup_plugin_terms("test", Templar(None)) == ["test"]
    assert listify_lookup_plugin_terms("{{ test }}", Templar(None)) == ["{{ test }}"]

    # make sure that we fail on undefined by default
    try:
        listify_lookup_plugin_terms("{{ test }}", Templar(None))
        assert False
    except Exception as e:
        assert "is undefined" in to_text(e)

    # make sure that we can disable failure on undefined
    assert listify_lookup_plugin_terms("{{ test }}", Templar(None), fail_on_undefined=False) == [u"{{ test }}"]

    # make

# Generated at 2022-06-13 16:32:10.602945
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    pass

# Generated at 2022-06-13 16:32:17.918358
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    # Create a simple function for Jinja2 to call as a test.
    def test_function():
        return "test string"

    class TestVarsModule:
        "Mock AnsibleModule class to allow Templar to convert var lookups"

        def __init__(self, argument_spec, bypass_checks=False, no_log=False,
                     check_invalid_arguments=None, mutually_exclusive=None, required_together=None,
                     required_one_of=None, add_file_common_args=False):
            self.argument_spec = argument_spec
            self.params = {}

    # Create a simple AnsibleModule-like class for Templar to use.
    class TestAnsibleModule:

        def __init__(self):
            return None


# Generated at 2022-06-13 16:32:29.517906
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib

    # Setup vault
    vault_pass = 'vault-password'
    vault_secrets = dict(vault_password=vault_pass)
    vault = VaultLib(vault_secrets)
    vault_text = vault.encrypt('secret-value')

    # Setup the templar
    templar = Templar(loader=None, variables={}, shared_loader_obj=None, vault_secrets=vault_secrets)

    # Test basic string
    result = listify_lookup_plugin_terms('foo', templar, None)
    assert result == ['foo']

    # Test simple vault
    result = listify_lookup_plugin_terms(vault_text, templar, None)


# Generated at 2022-06-13 16:32:45.561765
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    templar = Templar(loader=loader)

    assert listify_lookup_plugin_terms(None, templar, loader) == [None]
    assert listify_lookup_plugin_terms("{{ foo }}", templar, loader) == [None]
    assert listify_lookup_plugin_terms(["{{ foo }}", "bar", "{{ baz }}"], templar, loader) == [None, 'bar', None]

# Generated at 2022-06-13 16:32:55.683738
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.vault import VaultLib
    from ansible.template import Templar

    vault_pass = 'secret'
    loader = DictDataLoader()
    passwords = {'vault_password_file': vault_pass}
    templar = Templar(loader=loader, variables={}, vault_secrets=passwords)
    terms = '[ foo, bar ]'
    data = listify_lookup_plugin_terms(terms, templar, loader)
    assert data == ['foo', 'bar']

    # test when no vault is needed for templating
    terms = '[ foo, bar ]'
    data = listify_lookup_plugin_terms(terms, templar, loader)
    assert data == ['foo', 'bar']

    # test when vault is needed for templating

# Generated at 2022-06-13 16:32:59.872697
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    # The listify_lookup_plugin_terms function is used by most lookup plugins to ensure that the term passed
    # in via a user's playbook always results in a list.  Some lookup plugins require a single item while
    # others require a list.  This function works with both of these situations.
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.common._collections_compat import Sequence
    from ansible.template import Templar
    from ansible.vars.unsafe_proxy import UnsafeProxy

    # Create a standard lookup plugin class
    from ansible.plugins.lookup import LookupBase
    class MyLookup(LookupBase):

        def __init__(self, loader=None, templar=None, **kwargs):
            pass


# Generated at 2022-06-13 16:33:09.703242
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    templar = Templar(loader=loader)

    # Test conversion of string to list
    string_term = 'foobar'
    list_term = listify_lookup_plugin_terms(string_term, templar, loader)
    assert isinstance(list_term, list)
    assert list_term == ['foobar']

    # Test conversion of term which is already a list
    list_term = ['foo', 'bar']
    list_term_converted = listify_lookup_plugin_terms(list_term, templar, loader)
    assert isinstance(list_term_converted, list)
    assert list_term_converted == ['foo', 'bar']

    #

# Generated at 2022-06-13 16:33:17.366961
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager()
    # Load the test data from the unit-tests/data directory
    loader.set_basedir('test/unit/data')
    templar = Templar(loader=loader, variables=variable_manager)


# Generated at 2022-06-13 16:33:26.343508
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.utils import plugin_docs

    # We can't use Ansible's utils.module_docs.AnsibleModule directly
    # because AnsibleTemplate does not accept a set() for the
    # Jinja2 environment variables. So instead we use our own dummy class.
    from ansible.module_utils.facts import AnsibleModule as AnsibleModuleDummy
    from ansible.template import AnsibleTemplate

    # This is the same as AnsibleModule.from_json()

# Generated at 2022-06-13 16:33:32.719715
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    # Mock classes to test listify_lookup_plugin_terms
    class DummyTemplar:
        def template(self, template, convert_bare=False, fail_on_undefined=True, overrides=None):
            return template

    class DummyLoader:
        pass

    # Init mock classes
    dummy_templar = DummyTemplar()
    dummy_loader = DummyLoader()

    # Test listify_lookup_plugin_terms with string input
    assert listify_lookup_plugin_terms('test', dummy_templar, dummy_loader,
                                       fail_on_undefined=True, convert_bare=False) == ['test']

    # Test listify_lookup_plugin_terms with list input

# Generated at 2022-06-13 16:33:43.233556
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.utils.unsafe_proxy import wrap_var

    class FakeVarsModule(object):
        def get_vars(self, play=None, host=None, task=None, include_hostvars=True):
            return dict(x='x')

    class FakeLoader(object):
        def get_basedir(self, task=None):
            return 'a/b/c'

    templar = Templar(loader=FakeLoader(), variables=dict())
    templar._VARIABLE_MANAGER = FakeVarsModule()

    assert listify_lookup_plugin_terms('foo', templar, FakeLoader()) == ['foo']
    assert listify_lookup_plugin_

# Generated at 2022-06-13 16:33:50.654621
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    context = PlayContext()
    templar = Templar(loader=loader)

    # Test string value
    test_data = 'text'
    expected_data = ['text']
    assert (expected_data == listify_lookup_plugin_terms(test_data, templar, loader))

    # Test template value
    vars = VariableManager()
    vars.set_variable('test_var', 'template')
    test_data = '{{ test_var }}'
    expected_data = ['template']

# Generated at 2022-06-13 16:34:01.883610
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.yaml.objects import AnsibleUnicode

    # vars with subelements will be turned into a list
    assert listify_lookup_plugin_terms([AnsibleUnicode('{{foo.bar}}')], None, None) == [AnsibleUnicode('{{foo.bar}}')]

    # subelements in a string will be turned into lists
    assert listify_lookup_plugin_terms('{{foo.bar}}', None, None) == [AnsibleUnicode('{{foo.bar}}')]

    # list elements are unchanged
    assert listify_lookup_plugin_terms(['foo', 'bar'], None, None) == ['foo', 'bar']

    # dict elements fail

# Generated at 2022-06-13 16:34:27.232102
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    # TODO: Use a mock templar here to reduce the number of test cases
    # necessary.
    assert listify_lookup_plugin_terms('a', None, None) == ['a']
    assert listify_lookup_plugin_terms(['a'], None, None) == ['a']
    assert listify_lookup_plugin_terms('a b c', None, None) == ['a b c']
    assert listify_lookup_plugin_terms(['a', 'b', 'c'], None, None) == ['a', 'b', 'c']
    assert listify_lookup_plugin_terms([['a', 'b'], 'c'], None, None) == [['a', 'b'], 'c']

# Generated at 2022-06-13 16:34:35.201471
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    templar = Templar(loader=loader)

    assert listify_lookup_plugin_terms("foo", templar, loader) == ["foo"]
    assert listify_lookup_plugin_terms(['foo', 'bar'], templar, loader) == ["foo", "bar"]
    assert listify_lookup_plugin_terms(('foo', 'bar'), templar, loader) == ["foo", "bar"]
    assert listify_lookup_plugin_terms("{{ foo }}", templar, loader) == ["{{ foo }}"]

# Generated at 2022-06-13 16:34:45.152945
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    class MyOptions(object):
        def __init__(self, no_log_values=None):
            self.no_log_values = no_log_values

        def __getitem__(self, key):
            return self.__dict__[key]

    class MyVarManager(object):
        def __init__(self, no_log_values=None):
            self.options = MyOptions(no_log_values=no_log_values)

    class MyVars(object):
        def __init__(self, hostvars=None):
            if hostvars is None:
                hostvars = {}
            self.hostvars = hostvars

    class MyHost(object):
        def get_vars(self):
            return MyVars()


# Generated at 2022-06-13 16:34:45.697558
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    pass

# Generated at 2022-06-13 16:34:52.394595
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    class FakeLoader:

        def get_basedir(self, path):
            return '/path/to/files'

    class FakeTemplar:
        def __init__(self, loader):
            self._loader = loader

        def template(self, value, fail_on_undefined=False, convert_bare=True):
            if isinstance(value, string_types):
                return value

    assert listify_lookup_plugin_terms(['foo', 'bar'], FakeTemplar(FakeLoader()), FakeLoader()) == ['foo', 'bar']
    assert listify_lookup_plugin_terms('foo bar', FakeTemplar(FakeLoader()), FakeLoader()) == 'foo bar'

# Generated at 2022-06-13 16:34:55.924129
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    terms = '{{ [ "a", "b" ] }}'
    templar = Templar(loader=None)
    assert listify_lookup_plugin_terms(terms, templar, loader=None) == ['a', 'b']

# Generated at 2022-06-13 16:35:03.481705
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.vars import VariableManager

    t = Templar(VariableManager())
    assert listify_lookup_plugin_terms(['foo', 'bar'], t, None) == ['foo', 'bar']
    assert listify_lookup_plugin_terms("{{ ['foo', 'bar'] }}", t, None) == ['foo', 'bar']
    assert listify_lookup_plugin_terms("{{ ['foo', 'bar'] | list }}", t, None) == ['foo', 'bar']
    assert listify_lookup_plugin_terms("foo", t, None) == ['foo']
    assert listify_lookup_plugin_terms("{{ 'foo' }}", t, None) == ['foo']