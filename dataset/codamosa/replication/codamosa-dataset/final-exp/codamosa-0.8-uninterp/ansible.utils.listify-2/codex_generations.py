

# Generated at 2022-06-13 16:25:09.987343
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.vars import VariableManager

    vars = VariableManager()
    vm = VariableManager()

    templar = Templar(loader=None, variables=vm)
    assert listify_lookup_plugin_terms('foo', templar=templar, loader=None) == ['foo']
    assert listify_lookup_plugin_terms('foo,bar', templar=templar, loader=None) == ['foo', 'bar']
    assert listify_lookup_plugin_terms(['foo', 'bar'], templar=templar, loader=None) == ['foo', 'bar']
    assert listify_lookup_plugin_terms('{{ foo }}', templar=templar, loader=None) == ['{{ foo }}']
    assert listify_lookup

# Generated at 2022-06-13 16:25:20.170698
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    templar = Templar(None, None)

    assert listify_lookup_plugin_terms(1, templar) == [1]
    assert listify_lookup_plugin_terms('my string', templar) == ['my string']
    assert listify_lookup_plugin_terms('my string', templar, convert_bare=True) == ['my string']
    assert listify_lookup_plugin_terms('my "{{string}}"', templar, convert_bare=True) == ['my "string"']
    assert listify_lookup_plugin_terms(['my string'], templar) == ['my string']
    assert listify_lookup_plugin_terms({'a': 'my string'}, templar) == ['my string']

# Generated at 2022-06-13 16:25:27.478652
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    # setup
    loader = DictDataLoader({})
    inventory = InventoryManager(loader=loader, sources='')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    templar = Templar(loader=loader, variables=variable_manager)

    # make sure we get back a list for all terms

# Generated at 2022-06-13 16:25:36.247592
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    global _error, _plugin_name  # pylint: disable=global-statement

    # pylint: disable=unused-variable
    from ansible.plugins.loader import lookup_loader

    # pylint: disable=unused-variable
    from ansible.parsing.vault import VaultLib

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.template import Templar
    from ansible.errors import AnsibleError

    # The global error class for this plugin
    _error = AnsibleError
    _plugin_name = 'test_plugin'

    def _construct_loader(loader=None):
        """Helper method to load a loader from the dataloader"""
        # pylint: disable=arguments-differ

# Generated at 2022-06-13 16:25:43.978814
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    templar = Templar(loader=None, variables=dict())

    assert listify_lookup_plugin_terms('1', templar, None, fail_on_undefined=False) == ['1']
    assert listify_lookup_plugin_terms('1', templar, None, fail_on_undefined=False, convert_bare=True) == ['1']
    assert listify_lookup_plugin_terms(['1'], templar, None, fail_on_undefined=False) == ['1']
    assert listify_lookup_plugin_terms(['1'], templar, None, fail_on_undefined=False, convert_bare=True) == ['1']

# Generated at 2022-06-13 16:25:55.472613
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.common._collections_compat import Sequence
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    ds = dict(
        a = dict(
            b = dict(
                c = "first",
                d = "second"
            )
        )
    )
    vars = VariableManager()
    vars.update(ds)
    loader = DataLoader()
    templar = Templar(loader=loader, variables=vars)


# Generated at 2022-06-13 16:26:05.884163
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.yaml.loader import AnsibleLoader

    class DummyVarsModule(object):
        def __init__(self, name):
            self.name = name

    templar = Templar(loader=AnsibleLoader(DummyVarsModule('test')))

    # test with string
    assert ["foobar"] == listify_lookup_plugin_terms("{{ 'foobar' }}", templar, loader=AnsibleLoader(DummyVarsModule('test')))

    # test with list
    assert ["foo", "bar"] == listify_lookup_plugin_terms(["foo", "bar"], templar, loader=AnsibleLoader(DummyVarsModule('test')))

    # test with tuple
    assert ("foo", "bar") == list

# Generated at 2022-06-13 16:26:15.835603
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.utils.template import Templar

    module_args = dict(
        foo=["bar", "baz"],
    )
    templar = Templar(loader=None, variables=module_args)

    assert listify_lookup_plugin_terms(["{{ foo }}"], templar, None) == [
        ['bar', 'baz']
    ]

    assert listify_lookup_plugin_terms(["{{ foo[0] }}"], templar, None) == [
        'bar'
    ]

    assert listify_lookup_plugin_terms('{{ foo }}', templar, None) == [
        'bar', 'baz'
    ]


# Generated at 2022-06-13 16:26:22.059149
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from io import StringIO
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret

    templar = Templar(loader=None, variables={'a': 'a'})

    # accept raw strings
    result = listify_lookup_plugin_terms('string', templar, loader=None)
    assert result == ['string']

    # no templates, so strings are passed through
    result = listify_lookup_plugin_terms(u'string', templar, loader=None)
    assert result == [u'string']

    # accept lists

# Generated at 2022-06-13 16:26:32.971148
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    try:
        import json
        import jinja2
        from ansible.parsing.dataloader import DataLoader
        from ansible.template import Templar
    except ImportError:
        print("SKIP: not enough dependencies installed to test listify_lookup_plugin_terms")
        return

    dataloader = DataLoader()
    templar = Templar(loader=dataloader)

    # Test with a string
    result = listify_lookup_plugin_terms('foobar', templar, dataloader, convert_bare=True)
    assert result == ['foobar']

    # Test with a list of strings
    result = listify_lookup_plugin_terms(['foo', 'bar'], templar, dataloader)
    assert result == ['foo', 'bar']

    # Test

# Generated at 2022-06-13 16:26:44.831233
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    # empty list
    assert listify_lookup_plugin_terms(None, None) == []
    assert listify_lookup_plugin_terms([], None, None) == []
    assert listify_lookup_plugin_terms({}, None, None) == []

    # non-iterable non-string
    assert listify_lookup_plugin_terms(1, None, None) == [1]

    # string
    assert listify_lookup_plugin_terms("test", None, None) == ["test"]

    # list
    assert listify_lookup_plugin_terms([1, 2, 3], None, None) == [1, 2, 3]

    # single-entry list
    assert listify_lookup_plugin_terms([1], None, None) == [1]

    # tuple
    assert listify_look

# Generated at 2022-06-13 16:26:56.547834
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    #if '__name__' in globals() and globals()['__name__'] == "__main__":
    try:
        from ansible.template import Templar
    except ImportError:
        print("failed=True msg='ansible.template required for this test'")
        return

    from ansible.parsing.vault import VaultLib
    from ansible.template.vars import VarsModule

    templar = Templar(loader=None, vault_secrets=VaultLib(), variables=VarsModule())
    # Test string
    assert listify_lookup_plugin_terms("1 2 3", templar) == ["1", "2", "3"]
    assert listify_lookup_plugin_terms("1, 2, 3", templar) == ["1", "2", "3"]
    assert listify_

# Generated at 2022-06-13 16:27:05.966706
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.parsing.dataloader import DataLoader
    from ansible.templating import Templar

    class FakeVarsModule:
        def __init__(self):
            return

    loader = DataLoader()
    templar = Templar(loader=loader, variables=FakeVarsModule())
    assert [u'/path/to/file'] == listify_lookup_plugin_terms([u'/path/to/file'], templar, loader)
    assert [u'/path/to/file'] == listify_lookup_plugin_terms(u'/path/to/file', templar, loader)
    assert [u'hello'] == listify_lookup_plugin_terms(u'hello', templar, loader)
    assert [u'{{lookup_var}}'] == listify_lookup_plugin_

# Generated at 2022-06-13 16:27:16.642634
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.template import Templar

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='')
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    templar = Templar(loader=loader, variables=variable_manager)
    items = listify_lookup_plugin_terms('item1 item2 item3', templar, loader)
    assert items == ['item1', 'item2', 'item3']

    items = listify_lookup_plugin_terms(('item1', 'item2', 'item3'), templar, loader)

# Generated at 2022-06-13 16:27:26.722483
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.module_utils._text import to_text

    terms = [1, 2, 3, 4]
    templar = Templar(loader=None, variables=terms)
    results1 = listify_lookup_plugin_terms(terms, templar, None, fail_on_undefined=False)
    results2 = listify_lookup_plugin_terms(terms, templar, None, fail_on_undefined=True)
    assert results1 == results2 == [to_text(terms[0]), to_text(terms[1]), to_text(terms[2]), to_text(terms[3])]

    terms = '{{ item }}'
    templar = Templar(loader=None, variables={'item': terms})
    results1 = listify_lookup_plugin

# Generated at 2022-06-13 16:27:29.557886
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    '''
    Test listify_lookup_plugin_terms
    '''
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    # passing dataloader and variable mananger to template
    templar = Templar(loader=DataLoader(), variable_manager=VariableManager())

    test = listify_lookup_plugin_terms(terms="string", templar=templar)

    assert isinstance(test, list)

# Generated at 2022-06-13 16:27:40.896475
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.vault import VaultLib
    from ansible.template import Templar
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager

    # Load vault secrets into the variable manager
    variable_manager = VariableManager()
    variable_manager.extra_vars = {'comma_var': 'one,two,three'}

    # Convert a bare string
    templar = Templar(loader=None, variables=variable_manager, vault_secrets=VaultLib())
    terms = listify_lookup_plugin_terms('{{comma_var}}', templar, loader=None)
    assert terms == ['one,two,three']

    # Convert a list of bare strings

# Generated at 2022-06-13 16:27:50.735413
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    # Import Ansible module_utils
    from ansible.module_utils._text import to_text

    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar

    from ansible.inventory.host import Host

    from ansible.vars.manager import VariableManager

    # Set up loader, templar
    loader = DataLoader()

    # Set up variables for templar
    host = Host(name="localhost")
    variable_manager = VariableManager()
    variable_manager.set_host_variable(host, 'foo', 'bar')
    variable_manager.set_host_variable(host, 'list1', [1, 2, 3])
    variable_manager.set_host_variable(host, 'list2', ['1', '2', '3'])
    variable_manager.set

# Generated at 2022-06-13 16:28:01.790049
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    '''
    listify_lookup_plugin_terms is used in many lookup plugins and is
    currently written in such a way that it depends on the templating engine
    to split a string on commas.  To isolate unit test dependencies this
    function can be called to provide consistent split behavior.
    '''
    from ansible.template import Templar

    templar = Templar(loader=None)
    assert listify_lookup_plugin_terms('a,b,c', templar, None) == ['a', 'b', 'c']
    assert listify_lookup_plugin_terms(['a,b,c'], templar, None) == ['a,b,c']

# Generated at 2022-06-13 16:28:11.865222
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    class DummyVars(object):
        def __init__(self, data):
            self._data = data
        def get(self, key, default=None, boolean=False, templar=None):
            return self._data[key]

    class DummyPlayContext(object):
        def __init__(self, vars):
            self._vars = vars

        def get_variables(self):
            return self._vars

    vars = DummyVars({'a': 'A', 'b': 'B'})
    pc = DummyPlayContext(vars)
    templar = Templar(loader=None, variables=vars, play_context=pc)

    # All of these should convert to a list of length 1

# Generated at 2022-06-13 16:28:18.807013
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleUnicode

    assert listify_lookup_plugin_terms([1,2,3], Templar({}), None) == [1,2,3]
    assert listify_lookup_plugin_terms('foo', Templar({}), None) == ['foo']
    assert listify_lookup_plugin_terms([AnsibleUnicode('foo')], Templar({}), None) == ['foo']

# Generated at 2022-06-13 16:28:28.506685
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    '''
    listify_lookup_plugin_terms unit test
    '''
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    yaml_input_dict = {
        'input': {
            'term': ['foo', 'bar']
        }
    }

    yaml_input_list = [
        'foo',
        ['bar', 'baz', 1, 2]
    ]
    yaml_input_list_vault = [
        'foo',
        ['bar', 'baz', 1, 2],
        AnsibleVaultEncryptedUnicode('test_vault')
    ]

    yaml_input_str = "foobar"
    yaml_

# Generated at 2022-06-13 16:28:38.337015
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    class FakeTemplar(object):
        def template(self, terms, convert_bare=False, fail_on_undefined=True):
            if isinstance(terms, string_types):
                return terms
            else:
                return [a for a in terms]

    fake_loader = None
    fake_templar = FakeTemplar()

    class TestPassFail(object):
        def __init__(self, terms, expected_terms):
            self.terms = terms
            self.expected_terms = expected_terms


# Generated at 2022-06-13 16:28:44.705279
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    assert listify_lookup_plugin_terms("") == ['']
    assert listify_lookup_plugin_terms("hello world from ansible") == ['hello world from ansible']
    assert listify_lookup_plugin_terms("hello world from ansible") == ['hello world from ansible']
    assert listify_lookup_plugin_terms(["hello world from ansible"]) == ['hello world from ansible']
    assert listify_lookup_plugin_terms(["hello world", "from ansible"]) == ['hello world', 'from ansible']

# Generated at 2022-06-13 16:28:50.835559
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    templar = Templar()

    # Test list with only one element
    test_list = listify_lookup_plugin_terms('test', templar)
    assert len(test_list) == 1
    assert test_list[0] == 'test'

    # Test list with only two elements
    test_list = listify_lookup_plugin_terms(['test1', 'test2'], templar)
    assert len(test_list) == 2
    assert test_list[0] == 'test1'
    assert test_list[1] == 'test2'

    # Test list with only one element as a template
    test_list = listify_lookup_plugin_terms('{{ test }}', templar, dict(test=['test1', 'test2']))
   

# Generated at 2022-06-13 16:28:59.750162
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list=[])
    variable_manager.set_inventory(inventory)
    templar = Templar(loader=loader, variables=variable_manager)

    terms = "{{ [1,2,3] }}"
    result = listify_lookup_plugin_terms(terms, templar, loader)
    assert result == [1, 2, 3]

# Generated at 2022-06-13 16:29:10.054680
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.plugins.loader import lookup_loader
    from ansible.errors import AnsibleError

    def _load_lookup(modname):
        return lookup_loader.get(modname, class_only=True)

    template_data = """
    var1:
      - "{{ var2 }}"
    var2: 1
    """
    testdata = dict()

# Generated at 2022-06-13 16:29:20.215803
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.six import PY2
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.yaml.objects import AnsibleUnicode

    variable_manager = VariableManager()
    variable_manager.__setitem__('item1', 'value1')
    variable_manager.__setitem__('item2', 'value2')
    variable_manager.__setitem__('nested', {'item1': 'value1', 'item2': 'value2'})
    variable_manager.__setitem__('quoted1', "'value1'")

    templar = Templar(loader=None, variables=variable_manager)

    # test with single quoted string

# Generated at 2022-06-13 16:29:30.332516
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing import DataLoader
    from ansible.template import Templar

    # Dummy vars for templating
    variables = dict(
        one='1',
        two='2',
        three='3',
        four='4',
        five='5',
        six='6',
        seven='7',
        eight='8',
        nine='9',
        ten='10',
        eleven='11',
        twelve='12',
        dict_var = dict(
            one='1',
            two='2',
            three='3',
            four='4',
            five='5',
            six='6',
            seven='7',
            eight='8',
            nine='9',
            ten='10',
            eleven='11',
            twelve='12',
        )
    )
    test_

# Generated at 2022-06-13 16:29:39.308381
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    templar = Templar(loader=loader)

    # Test listify_lookup_plugin_terms when the input is a string
    input_string = "{{ item }}"
    expected_output = ["test-item"]

    terms = listify_lookup_plugin_terms(input_string, templar, loader, fail_on_undefined=False)

    assert terms == expected_output

    # Test listify_lookup_plugin_terms when the input is not a string and is a list
    input_list = ["test-item"]
    expected_output = ["test-item"]


# Generated at 2022-06-13 16:29:51.891433
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    templar = Templar(loader=None, variables={})

    result = listify_lookup_plugin_terms('1', templar, None)
    assert result == ['1']
    result = listify_lookup_plugin_terms(['1', '2'], templar, None)
    assert result == ['1', '2']
    result = listify_lookup_plugin_terms('1, 2', templar, None)
    assert result == ['1', '2']
    result = listify_lookup_plugin_terms(['1', '2, 3'], templar, None)
    assert result == ['1', '2', '3']

# Generated at 2022-06-13 16:30:01.132237
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    my_host = Host("localhost")
    my_host.set_variable("var_a", "a_value")
    my_host.set_variable("var_b", "b_value")

    my_group = Group("group_1")
    my_group.add_host(my_host)
    my_group.set_variable("var_c", "c_value")
    my_group.set_variable("var_d", "d_value")

    inventory = InventoryManager(loader=DataLoader())
    inventory

# Generated at 2022-06-13 16:30:10.487108
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.module_utils._text import to_text
    from ansible.template import Templar

    assert listify_lookup_plugin_terms(
        "{{ ['one'] | to_json }}", Templar(loader=None, shared_loader_obj=None), None
    ) == ["one"]

    assert listify_lookup_plugin_terms(
        u"{{ ['one'] | to_json }}", Templar(loader=None, shared_loader_obj=None), None,
    ) == [u"one"]

    # this verifies that we convert into unicode strings
    assert listify_lookup_plugin_terms(
        "{{ ['one'] | to_json }}", Templar(loader=None, shared_loader_obj=None), None,
    ) == [u"one"]

    assert listify_lookup_plugin_terms

# Generated at 2022-06-13 16:30:15.692137
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    assert listify_lookup_plugin_terms(
        terms='{{ foo }}',
        templar=Templar(),
        loader=None,
        fail_on_undefined=True,
        convert_bare=False
    ) == ['{{ foo }}']

    assert listify_lookup_plugin_terms(
        terms=['{{ foo }}'],
        templar=Templar(),
        loader=None,
        fail_on_undefined=True,
        convert_bare=False
    ) == ['{{ foo }}']


# Generated at 2022-06-13 16:30:25.715070
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    assert [] == listify_lookup_plugin_terms([], {})
    assert ['foo'] == listify_lookup_plugin_terms('foo', {})
    assert ['1', '2'] == listify_lookup_plugin_terms('1 2', {})
    assert ['1', '2'] == listify_lookup_plugin_terms(['1', '2'], {})
    assert ['1', '2'] == listify_lookup_plugin_terms(['1', ['2']], {})
    assert ['1', '2'] == listify_lookup_plugin_terms("['1', ['2']]", {})

# Generated at 2022-06-13 16:30:35.725169
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.utils.yaml import from_yaml
    from ansible.utils.collection_loader import AnsibleCollectionLoader
    from ansible.module_utils.facts.system import OpenBSDFactCollector
    from ansible.module_utils.facts.virtual.openbsd import OpenBSDVirtual
    from ansible.module_utils.facts.processor.openbsd import OpenBSDProcessor
    OpenBSDModuleFactsCollector = OpenBSDFactCollector.load_collectors(['OpenBSDVirtual', 'OpenBSDProcessor'])

    env_vars = {
        'ANSIBLE_LOOKUP_PLUGINS': '.',
    }

    loader = AnsibleCollectionLoader()

    mock_args = None

# Generated at 2022-06-13 16:30:43.728952
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib

    class TestTemplar(Templar):
        def __init__(self):
            self.vars = {}
            self.loader = None

    t = TestTemplar()

    assert listify_lookup_plugin_terms('foo', t, None) == ['foo']
    assert listify_lookup_plugin_terms(['foo', 'bar'], t, None) == ['foo', 'bar']
    assert listify_lookup_plugin_terms('foo, bar', t, None) == ['foo, bar']

# Generated at 2022-06-13 16:30:54.745130
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.template import Templar

    m = MockVarsModule()
    m.params = MutableMapping()
    m.params['a'] = 'foo'
    l = MockLoader()
    t = Templar(loader=l, variables=m.params)
    assert listify_lookup_plugin_terms('{{a}}', t, l) == ['foo']

    m.params['a'] = AnsibleUnicode('foo')
    assert listify_lookup_plugin_terms('{{a}}', t, l) == ['foo']


# Generated at 2022-06-13 16:31:02.455597
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.common._collections_compat import OrderedDict
    from ansible.parsing.yaml.loader import AnsibleLoader

    def test(terms, expected):
        assert listify_lookup_plugin_terms(terms, templar, loader, False) == expected
        assert listify_lookup_plugin_terms(terms, templar, loader, True) == expected

    # setup jinja2 environment
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    loader = AnsibleLoader(None, variable_manager=VariableManager(), all_vars=OrderedDict())
    templar = Templar(loader=loader, variables=loader.all_vars)

    # test with a string
    test("foo", ['foo'])

    # test with

# Generated at 2022-06-13 16:31:11.353937
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    ansible_vars = {
        'string_var': 'yes',
        'list_var': [1, 2, 3],
        'dict_in_list': [{'k': 'v'}, {'k': 'v'}],
        'undef_var': '{{ not_defined }}',
    }

    ansible_module = FakeAnsibleModule()

    # Test string, should return list with string as first item
    result = listify_lookup_plugin_terms("string literal", ansible_module, None)
    assert len(result) == 1
    assert result[0] == "string literal"

    # Test list, should return identical list
    result = listify_lookup_plugin_terms([1, 2, 3], ansible_module, None)
    assert len(result) == 3
    assert result

# Generated at 2022-06-13 16:31:28.130860
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar

    loader = DataLoader()
    variable_manager = VariableManager()
    templar = Templar(loader=loader, variables=variable_manager)

    # verify that string path is auto-listified
    single_path = 'my-file.txt'
    expected_list = ['my-file.txt']
    actual_list = listify_lookup_plugin_terms(single_path, templar, loader)
    assert expected_list == actual_list

    # verify that list path is not modified
    list_path = ['first.txt', 'second.txt']
    actual_list = listify_lookup_plugin_terms(list_path, templar, loader)


# Generated at 2022-06-13 16:31:38.473664
# Unit test for function listify_lookup_plugin_terms

# Generated at 2022-06-13 16:31:45.834222
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.utils.template import Templar

    class FakeVarsModule(object):
        def __init__(self):
            self._templar = Templar(loader=None)

        def get_vars(self, loader=None, play=None, task=None, host=None):
            return {}

    fake_vars_module = FakeVarsModule()

    class OptionsModule(object):
        def __init__(self):
            self.fail_on_undefined_vars = True

    options_module = OptionsModule()

    results = listify_lookup_plugin_terms('{{ foo }}', fake_vars_module._templar, None, options_module.fail_on_undefined_vars)
    assert results == ['foo'], results


# Generated at 2022-06-13 16:31:53.834850
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleUnicode

    result = listify_lookup_plugin_terms("val1 val2", Templar({}), None)
    assert isinstance(result, list)
    assert result == ['val1', 'val2']

    result = listify_lookup_plugin_terms(["val1 val2", AnsibleUnicode("val3   val4")], Templar({}), None, convert_bare=True)
    assert isinstance(result, list)
    assert result == ['val1', 'val2', 'val3   val4']

    result = listify_lookup_plugin_terms("val1", Templar({}), None)
    assert isinstance(result, list)
    assert result == ['val1']

    result = listify

# Generated at 2022-06-13 16:32:01.808981
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext

    loader = DataLoader()
    vault_secrets_file = {}

    inventory = InventoryManager(loader=loader, sources='')
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    context = PlayContext()
    context._vault = VaultLib([], loader, vault_secrets_file)

    templar = Templar(loader=loader, variables=variable_manager,
                      vault_secrets=context._vault.secrets)

    # Test when the param is not a

# Generated at 2022-06-13 16:32:13.173810
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleUnicode

    templar = Templar(loader=None)

    assert listify_lookup_plugin_terms("{{ test1 }},{{ test2 }}", templar, None, False, False) == ["{{ test1 }},{{ test2 }}"]
    assert listify_lookup_plugin_terms(["{{ test1 }}"], templar, None, False) == ["{{ test1 }}"]
    assert listify_lookup_plugin_terms("test", templar, None, False, False) == ["test"]
    assert listify_lookup_plugin_terms(["test"], templar, None, False) == ["test"]

# Generated at 2022-06-13 16:32:19.314431
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.dataloader import DataLoader

    from ansible.vars.manager import VariableManager
    from ansible.template import Templar

    loader = DataLoader()
    variable_manager = VariableManager()
    templar = Templar(loader=loader, variables=variable_manager)

    # given a bare var, we want back a list
    terms = 'foo'
    terms_out = listify_lookup_plugin_terms(terms, templar, loader, convert_bare=True)
    assert terms_out == ['foo']

    # given a list, we want back a list
    terms = ['foo', 'bar']
    terms_out = listify_lookup_plugin_terms(terms, templar, loader, convert_bare=True)
    assert terms_out == ['foo', 'bar']
   

# Generated at 2022-06-13 16:32:30.327336
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.module_utils.six import PY3
    from ansible.parsing.yaml.objects import AnsibleUnicode
    import ansible.module_utils.common.collections as collections_compat

    templar = FakeTemplar()
    loader = FakeLoader()
    terms = '{{ foo }}'
    result = listify_lookup_plugin_terms(terms, templar, loader)
    assert result == [u'bar']

    if PY3:
        terms = u'{{ foo }}'
    else:
        terms = AnsibleUnicode('{{ foo }}')
    result = listify_lookup_plugin_terms(terms, templar, loader)
    assert result == [u'bar']

    terms = ['{{ foo }}', u'{{ foo }}']
    result = list

# Generated at 2022-06-13 16:32:39.903223
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    import os

    terms = '{{ lookup_var("hostvars." + "localhost" + "." + "ansible_mounts") }}'

    variable_manager = VariableManager()
    loader = DataLoader()

    inventory = InventoryManager(loader=loader, sources=['localhost'])
    variable_manager.set_inventory(inventory)

    mock_tqm = None
    play_context = PlayContext()
    templar = Templar(loader=loader, variable_manager=variable_manager, play_context=play_context)

    results = listify_look

# Generated at 2022-06-13 16:32:49.415321
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    templar = Templar(loader=loader)

    def assert_equal(a, b, *args, **kwargs):
        if type(a) != type(b):
            raise Exception("got: %s(%s) != %s(%s)" % (type(a), a, type(b), b))
        assert a == b

    assert_equal(listify_lookup_plugin_terms('test.txt', templar), ['test.txt'])
    assert_equal(listify_lookup_plugin_terms(['a.txt', 'b.txt'], templar), ['a.txt', 'b.txt'])

# Generated at 2022-06-13 16:33:11.585838
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    templar = Templar(loader=None)
    terms = listify_lookup_plugin_terms(["{{ foo }}", "{{ bar }}"], templar, loader, fail_on_undefined=True)
    assert terms == ["{{ foo }}", "{{ bar }}"]
    terms = listify_lookup_plugin_terms(["{{ foo }}", "{{ bar }}"], templar, loader, fail_on_undefined=False)
    assert terms == ["", ""]
    terms = listify_lookup_plugin_terms("{{ foo }}", templar, loader, fail_on_undefined=True)
    assert terms == ["{{ foo }}"]
    terms = listify_lookup_plugin_terms("{{ foo }}", templar, loader, fail_on_undefined=False)


# Generated at 2022-06-13 16:33:18.963366
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.vault import VaultLib
    from ansible.template import Templar

    # Test value will be a single term (string)
    # Templating a string should return a list with one string element
    test_value = "test"
    expected_result = ['test']
    result = listify_lookup_plugin_terms(test_value, Templar(VaultLib()), None)
    assert result == expected_result

    # Test value will be a single term (string with non-string content)
    # Templating a string should return a list with one string element
    test_value = "{{ test_var }}"
    expected_result = ['{{ test_var }}']
    result = listify_lookup_plugin_terms(test_value, Templar(VaultLib()), None)
    assert result == expected_result



# Generated at 2022-06-13 16:33:26.063891
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    v = VariableManager()
    t = Templar(loader=DataLoader(), variables=v)

    assert listify_lookup_plugin_terms('1', t, t) == ['1']
    assert listify_lookup_plugin_terms(['1'], t, t) == ['1']
    assert listify_lookup_plugin_terms(['1', '2'], t, t) == ['1', '2']
    assert listify_lookup_plugin_terms(1, t, t) == [1]

# Generated at 2022-06-13 16:33:32.545413
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    '''
    Unit test for function listify_lookup_plugin_terms
    '''
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    templar = Templar(loader=loader, variables={})

    play_context = PlayContext()
    templar._init_vars(play_context)

    result = listify_lookup_plugin_terms("{{ var1 }}", templar, loader, fail_on_undefined=True, convert_bare=False)
    assert result == ['{{ var1 }}']

    # template returns a list/tuple
    templar._available_variables = dict(var1=[1, 2, 3])
    result = listify_

# Generated at 2022-06-13 16:33:39.677825
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    assert listify_lookup_plugin_terms('hello', templar=None, loader=None) == ['hello']
    assert listify_lookup_plugin_terms(['hello', 'world'], templar=None, loader=None) == ['hello', 'world']
    assert listify_lookup_plugin_terms(u"hello", templar=None, loader=None) == [u'hello']
    assert listify_lookup_plugin_terms(5, templar=None, loader=None) == [5]

# Generated at 2022-06-13 16:33:48.653674
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    import jinja2.exceptions

    from ansible.module_utils._text import to_text
    from ansible.template import Templar

    loader = DictDataLoader({
        "some_file": (u"""
        [foo]
        bar=baz
        """),
        "some_host": (u"""
        ---
        foo: baz
        """),
    })

    templar = Templar(loader=loader)

    res = listify_lookup_plugin_terms(
        terms=['something_completely_unrelated'],
        templar=templar,
        loader=loader,
        fail_on_undefined=True,
        convert_bare=False,
    )
    assert res == ['something_completely_unrelated']

    # fileglob should be converted to a list

# Generated at 2022-06-13 16:34:00.115706
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar, loader_loader
    from ansible.parsing.yaml.loader import AnsibleLoader

    class DummyVarsModule(dict):
        def __init__(self):
            self['foo'] = 'one'
            self['bar'] = 'two'
            self['baz'] = 'three'
            self['undefined'] = None
            self['user_id'] = 123

    loader = AnsibleLoader(None, variable_manager=DummyVarsModule())

    templar = Templar(loader=loader)

    assert listify_lookup_plugin_terms(None, templar, loader) == [None]

    assert listify_lookup_plugin_terms('one', templar, loader) == ['one']

# Generated at 2022-06-13 16:34:05.904722
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    assert listify_lookup_plugin_terms('', None, None) == []
    assert listify_lookup_plugin_terms(['a', 'b'], None, None) == ['a', 'b']
    assert listify_lookup_plugin_terms('a', None, None) == ['a']
    assert listify_lookup_plugin_terms('a, b', None, None) == ['a, b']

# Generated at 2022-06-13 16:34:14.341193
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject

    class VarsModule:
        def get_vars(self, loader, path, entities, cache=True):
            return dict(lookup_plugin_terms_test='worked')

    class DummyVaultSecret:
        def __init__(self, value=''):
            self.vault = ''
            self.value = value
            self.vault_id = ''

    class DummyLoader:
        def get_basedir(self, path):
            return '/'

        def get_vars(self):
            return dict()

        def path_dwim(self, given):
            return given


# Generated at 2022-06-13 16:34:26.793276
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.utils.template import Templar
    from ansible.template.safe_eval import safe_eval
    templar = Templar(loader=None, variables={u'key1': 3})

    # single string
    assert listify_lookup_plugin_terms(u'key1', templar, loader=None) == [u'key1']
    assert listify_lookup_plugin_terms(u'{{ key1 }}', templar, loader=None) == [3]
    assert listify_lookup_plugin_terms(u'{{ key1 }}', templar, loader=None, fail_on_undefined=False) == [u'{{ key1 }}']
    assert listify_lookup_plugin_terms(u'{{ key2 }}', templar, loader=None) == [u'{{ key2 }}']

# Generated at 2022-06-13 16:34:49.460928
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    templar = Templar(loader=None)

    assert listify_lookup_plugin_terms('string1', templar, None) == ['string1']
    assert listify_lookup_plugin_terms(['list1'], templar, None) == ['list1']
    assert listify_lookup_plugin_terms(('tuple1',), templar, None) == ['tuple1']

    assert listify_lookup_plugin_terms(['list1', 'list2'], templar, None) == ['list1', 'list2']

    assert listify_lookup_plugin_terms([('list1',), ('list2',)], templar, None) == ['list1', 'list2']


# Generated at 2022-06-13 16:34:59.835582
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.vars.manager import VariableManager

    loader = AnsibleLoader(None, variable_manager=VariableManager())
    my_vars = dict(a='foo', b='bar')
    templar = Templar(loader=loader, variables=my_vars)
    assert listify_lookup_plugin_terms('{{a}}', templar, loader) == ['foo']
    assert listify_lookup_plugin_terms('{{a}} {{b}}', templar, loader) == ['foo', 'bar']
    assert listify_lookup_plugin_terms(['{{a}}', '{{b}}'], templar, loader) == ['foo', 'bar']
    assert listify_lookup_plugin