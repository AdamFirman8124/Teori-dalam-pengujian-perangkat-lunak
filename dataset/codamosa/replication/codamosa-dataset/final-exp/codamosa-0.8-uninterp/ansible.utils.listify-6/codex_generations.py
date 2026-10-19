

# Generated at 2022-06-13 16:25:09.906375
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.utils.listify import listify_lookup_plugin_terms

    truth_map = [
        ('foo', "{{ 'foo' }}", ['foo']),
        (['foo'], ["{{ 'foo' }}"], ['foo']),
        ('foo', 'foo', ['foo']),
        ('foo', ['foo'], ['foo']),
        ('foo,bar', ['foo'], ['foo', 'bar']),
        ('foo,bar', ['foo', 'bar'], ['foo', 'bar']),
    ]

    for (before, after, result) in truth_map:
        assert listify_lookup_plugin_terms(before) == result
        assert listify_lookup_plugin_terms(after) == result

# Generated at 2022-06-13 16:25:20.095892
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.vault import VaultLib
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible import context
    from ansible.module_utils.facts.system.distribution import Distribution

    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude

    # Set up context for testing
    context.CLIARGS = context.CLIARGS._replace(tags=[])
    current_play_context = PlayContext()
    current_task = Task()
    current_task._role = None
    current_play_context._play = None
    current_play_context._task = current_task
    current_play_context._task.loop = []
    current

# Generated at 2022-06-13 16:25:27.450131
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.vars.manager import VariableManager


# Generated at 2022-06-13 16:25:38.341589
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    import jinja2
    loader = DataLoader()
    loader.set_basedir('/')
    templar = Templar(loader=loader)

    terms = ['foo', 'bar', 'baz']
    r1 = listify_lookup_plugin_terms(terms, templar, loader, convert_bare=True)
    assert(terms == r1)

    terms = ['foo', 'bar', 'baz', '{{foo}}']
    r1 = listify_lookup_plugin_terms(terms, templar, loader, convert_bare=True)
    assert(['foo', 'bar', 'baz', 'foo'] == r1)

    terms = '{{foo}}'
    r1 = listify

# Generated at 2022-06-13 16:25:50.823440
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    def assert_eq(x, y):
        assert x == y, '%r != %r' % (x, y)

    t = Templar(loader=None, variables={'foo': 'bar', 'emptystr': '', 'emptylist': []})
    assert_eq(listify_lookup_plugin_terms('foo', t, None), ['bar'])
    assert_eq(listify_lookup_plugin_terms(['bar'], t, None), ['bar'])
    assert_eq(listify_lookup_plugin_terms(['{{foo}}'], t, None), ['{{foo}}'])
    assert_eq(listify_lookup_plugin_terms('{{foo}}', t, None, convert_bare=True), ['bar'])

# Generated at 2022-06-13 16:26:00.391277
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    # check that a single-element list is returned (for the "list" lookup plugin)
    terms = listify_lookup_plugin_terms('var', None, None)
    assert isinstance(terms, list)
    assert len(terms) == 1
    assert terms == ['var']

    # check that a multi-element list is returned
    terms = listify_lookup_plugin_terms('var1,var2', None, None)
    assert isinstance(terms, list)
    assert len(terms) == 2
    assert terms == ['var1', 'var2']

    # check that a multi-element list with a separator is returned
    terms = listify_lookup_plugin_terms('var1;var2', None, None, convert_bare=True)

# Generated at 2022-06-13 16:26:11.740173
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    import ansible.template
    templar = ansible.template.Templar(loader=None)
    assert listify_lookup_plugin_terms(terms="1", templar=templar) == ["1"]
    assert listify_lookup_plugin_terms(terms=["1"], templar=templar) == ["1"]
    assert listify_lookup_plugin_terms(terms="1 2", templar=templar) == ["1 2"]
    assert listify_lookup_plugin_terms(terms=["1", "2"], templar=templar) == ["1", "2"]

    assert listify_lookup_plugin_terms(terms="1 2", templar=templar, convert_bare=True) == ["1", "2"]
    assert listify_lookup_

# Generated at 2022-06-13 16:26:20.269018
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    import ansible.parsing.yaml.objects

    # Simple strings
    assert listify_lookup_plugin_terms('one', None, None) == ['one']
    assert listify_lookup_plugin_terms('one,two', None, None) == ['one', 'two']
    assert listify_lookup_plugin_terms(['one', 'two'], None, None) == ['one', 'two']
    assert listify_lookup_plugin_terms(['one', 'two'], None, None) == ['one', 'two']

    # String with newlines
    assert listify_lookup_plugin_terms('one\ntwo', None, None) == ['one\ntwo']
    assert listify_lookup_plugin_terms(['one\ntwo'], None, None) == ['one\ntwo']



# Generated at 2022-06-13 16:26:31.736856
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    class PseudoTemplar(object):
        def template(self, stuff):
            return stuff

    templar = PseudoTemplar()

    assert(listify_lookup_plugin_terms('foo', templar)  == ['foo'])
    assert(listify_lookup_plugin_terms(['foo', 'bar'], templar)  == ['foo', 'bar'])
    assert(listify_lookup_plugin_terms('foo,bar', templar)  == ['foo', 'bar'])
    assert(listify_lookup_plugin_terms([['foo', 'bar'], ['baz', 'boo']], templar)  == [['foo', 'bar'], ['baz', 'boo']])

# Generated at 2022-06-13 16:26:41.500974
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    '''
    Listify the terms of the lookup_plugin, this involves templating and
    then converting the results to a list of strings.
    '''
    from units.mock.loader import DictDataLoader
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    loader = DictDataLoader({
        "test_template.j2": "{{ a }} {% if b %} {{ b }} {% endif %} {{ c }}",
    })

    t = Templar(loader=loader, variables=VariableManager())

    # test simple terms
    terms = [u'test1', u'test2', u'test3']

# Generated at 2022-06-13 16:26:54.623409
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    import ansible.playbook.play_context
    from ansible.inventory.manager import InventoryManager
    loader = DataLoader()
    variable_manager = VariableManager()
    playbook_context = ansible.playbook.play_context.PlayContext()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager.set_inventory(inventory)
    templar = Templar(loader=loader, variable_manager=variable_manager,
                      shared_loader_obj=variable_manager,
                      options={'fail_on_undefined': True})

    # Test string
    str_terms = 'str'

# Generated at 2022-06-13 16:27:02.258156
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleUnicode

    loader = DictDataLoader({})
    inventory = Inventory(loader=loader, variable_manager=VariableManager(loader=loader))
    variable_manager = inventory.get_variable_manager()
    templar = Templar(loader=loader, variables=variable_manager.get_vars())

    terms = [AnsibleUnicode('{{ foo }}'), AnsibleUnicode('{{ bar }}')]
    variable_manager.set_nonpersistent_facts({"foo": "test1", "bar": "test2"})
    assert listify_lookup_plugin_terms(terms=terms, templar=templar, loader=loader) == ['test1', 'test2']

    terms = AnsibleUnicode

# Generated at 2022-06-13 16:27:08.785436
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.utils.vars import combine_vars

    terms = '{{ foo }}'
    templar = Templar(loader=None, variables=combine_vars(loader=None, variables=dict(foo='bar')))
    assert listify_lookup_plugin_terms(terms, templar, None) == ['bar']

    terms = ['foo', 'bar', 'baz']
    templar = Templar(loader=None, variables=combine_vars(loader=None, variables=dict(foo='bar')))
    assert listify_lookup_plugin_terms(terms, templar, None) == ['foo', 'bar', 'baz']

# Generated at 2022-06-13 16:27:18.837403
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.template import jinja2
    from ansible.parsing.dataloader import DataLoader

    templar = Templar(loader=DataLoader(), variables={'foo': 'baz'})
    # Check that strings are parsed correctly
    assert listify_lookup_plugin_terms('{{ foo }}', templar, None) == ['baz']
    # Check that iterables are parsed correctly
    assert listify_lookup_plugin_terms(['foo', 'bar'], templar, None) == ['foo', 'bar']

    # Check that the function returns a list
    assert isinstance(listify_lookup_plugin_terms("foo", templar, None), list)

    # Check that the function does not parse strings in lookup plugin result lists
    assert listify_look

# Generated at 2022-06-13 16:27:28.371426
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.errors import AnsibleError
    from ansible.template import Templar
    from ansible.utils.vars import combine_vars

    class VarsModule():
        def get_vars(inner_self, loader, path, entities):
            return combine_vars(loader, path, entities)

    class TestLookupPlugin():
        def __init__(self, basedir, runner, executor, loader, templar):
            self.basedir = basedir
            self.runner = runner
            self.executor = executor
            self.loader = loader
            self.templar = templar

        def get_basedir(self, terms):
            return self.basedir

        def run(self, terms, inject=None, **kwargs):
            return terms


# Generated at 2022-06-13 16:27:40.747136
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    class FakeVarsModule:
        pass

    fake_loader = FakeVarsModule()
    templar = Templar(loader=fake_loader)

    # test with a string
    result = listify_lookup_plugin_terms('foo', templar, fake_loader, fail_on_undefined=False, convert_bare=False)
    assert result == "foo"

    # test with a list that only has a string in it
    result = listify_lookup_plugin_terms(['foo'], templar, fake_loader, fail_on_undefined=False, convert_bare=False)
    assert result == ["foo"]

    # test with a list with two strings in it

# Generated at 2022-06-13 16:27:50.134216
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    """
    Function listify_lookup_plugin_terms unit test
    """
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleUnicode

    templar = Templar(loader=None)
    assert listify_lookup_plugin_terms('foo', templar, loader=None, fail_on_undefined=False, convert_bare=False) == ['foo']
    assert listify_lookup_plugin_terms(['foo'], templar, loader=None, fail_on_undefined=False, convert_bare=False) == ['foo']
    assert listify_lookup_plugin_terms(['{{ foo }}'], templar, loader=None, fail_on_undefined=False, convert_bare=False) == ['{{ foo }}']
    assert listify

# Generated at 2022-06-13 16:28:01.250963
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils._text import to_text
    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib

    templar = Templar(loader={}, variables={})
    terms = "{{ var1 }},{{ var2 }}"
    results_terms = templar.template(terms, convert_bare=True, convert_data=True)
    assert results_terms == [u'foo', u'bar']


# Generated at 2022-06-13 16:28:07.604735
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    skip_test = False

    try:
        from jinja2 import DictLoader, Environment
        loader = DictLoader({})
        environment = Environment(loader=loader)
    except ImportError as e:
        skip_test = True

    # Skip test if modules are not available
    if skip_test is True:
        return 0

    test_list = []

    # test string
    test_list.append(listify_lookup_plugin_terms('foo', environment, loader))
    assert test_list[-1] == ['foo']

    # test integer
    test_list.append(listify_lookup_plugin_terms(42, environment, loader))
    assert test_list[-1] == [42]

    # test dict

# Generated at 2022-06-13 16:28:18.124556
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    terms1 = '{{ foo }}'
    terms2 = '{{ undefined }}'
    terms3 = '{{ foo }}{{ undefined }}'
    terms4 = '   {{ foo }}   '
    terms5 = ['{{ foo }}', '{{ foo }}']
    terms6 = '{{ foo }} {{ bar }}'
    terms7 = '{{ foo }} {{ bar }} {{ bam }}'
    terms8 = [ '{{ foo }}', '{{ bar }}', '{{ bam }}' ]
    terms9 = [ 'foo', 'bar', 'bam' ]
    terms10 = ['foo', 'bar', '{{ foo }}']
    terms11 = ['foo', 'bar', 'bam']
    terms12 = ['foo', 'bar', 'bam']



# Generated at 2022-06-13 16:28:29.688546
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.template import TemplateError

    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    class DummyVars:
        def get_vars(self, **kwargs):
            return dict(foo='bar', bing='bong')

    variable_manager = VariableManager()
    variable_manager.extra_vars = dict(foo='bar', bing='bong')
    variable_manager.get_vars = DummyVars()
    variable_manager.get_host_vars = DummyVars()
    variable_manager.get_all_vars = DummyVars()

    play_context = PlayContext()


# Generated at 2022-06-13 16:28:38.921997
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.vault import VaultLib
    class FakeVaultSecret(VaultLib):
        def decrypt(self, b_data, b_vault_password):
            return b_data

    class FakeVarsPlugin:
        def __init__(self):
            self.VaultSecret = FakeVaultSecret()

    t = Templar(loader=None, variables={'foo': 'bar'}, shared_loader_obj=None, vars_plugins=FakeVarsPlugin())

    assert listify_lookup_plugin_terms('{{foo}}', t, None, convert_bare=True) == ['bar']
    assert listify_lookup_plugin_terms('{{foo}}', t, None, convert_bare=True)

# Generated at 2022-06-13 16:28:49.398338
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template.safe_eval import safe_eval

    terms = '{{ foo }}'
    result = listify_lookup_plugin_terms(terms, safe_eval, None)
    assert result == '{{ foo }}'

    terms = '{{ cow + " and " + dog }}'
    result = listify_lookup_plugin_terms(terms, safe_eval, None)
    assert result == '{{ cow + " and " + dog }}'

    terms = '{{ cow + " and " }} a dog'
    result = listify_lookup_plugin_terms(terms, safe_eval, None)
    assert result == ['{{ cow + " and " }} a dog']

    terms = ['{{ cow + " and " }} a dog']
    result = listify_lookup_plugin_terms(terms, safe_eval, None)


# Generated at 2022-06-13 16:29:00.723285
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar
    from ansible.utils.vars import combine_vars

    class TestVarsModule(object):
        def __init__(self):
            self.STRING = 'STRING'
            self.UNICODE = u'UNICODE'
            self.INTEGER = 42
            self.LIST = ['one', 'two']
            self.DICT = {'key': 'value'}

        def get_vars(self):
            return combine_vars(self.get_vars_precedence())

        def get_vars_precedence(self):
            return [self]

    m = TestVarsModule()
    t = Templar(loader=None, variables=m.get_vars())

# Generated at 2022-06-13 16:29:10.297571
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    # Setup
    my_vars = dict(one=1, two=2, three=3, four=4, five=5)

    my_loader = DummyLoader(paths=[])

    my_templar = Templar(loader=my_loader, variables=my_vars)

    # Test 1
    # case = '1 2 3 4 5'
    case = '{{ one }} {{ two }} {{ three }} {{ four }} {{ five }}'
    terms = listify_lookup_plugin_terms(terms=case, templar=my_templar, loader=my_loader)

    assert len(terms) == 5
    assert terms == ['1', '2', '3', '4', '5']

    # Test 2
    # case = ['1', '2', '3', '

# Generated at 2022-06-13 16:29:20.409154
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.six import PY3
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.errors import AnsibleUndefinedVariable
    from ansible.vars import VariableManager

    from io import StringIO
    import sys

    # The module argument parsing requires a connection to parse into a bytes
    # object, so create a fake connection object

    # We'll create a fake connection object as an instance of object
    class FakeConn(object):

        def __init__(self, *args, **kwargs):
            pass

    # and create a fake connection plugin instance
    class FakeConnection(object):

        def __init__(self, *args, **kwargs):
            pass


# Generated at 2022-06-13 16:29:30.405007
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    vars_mgr = VariableManager()
    loader = DataLoader()
    templar = Templar(loader=loader, variables=vars_mgr)

    # Test String
    assert listify_lookup_plugin_terms('String', templar, loader) == ['String']
    assert listify_lookup_plugin_terms('', templar, loader) == ['']
    assert listify_lookup_plugin_terms(None, templar, loader) == [None]

    # Test List
    assert listify_lookup_plugin_terms(['First Item', 'Second Item'], templar, loader) == ['First Item', 'Second Item']

    # Test

# Generated at 2022-06-13 16:29:34.589782
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    templar = Templar(loader=None, variables={'name': 'ansible'})

    assert listify_lookup_plugin_terms('{{name}}', templar, loader=None) == ['ansible']
    assert listify_lookup_plugin_terms(['{{name}}'], templar, loader=None) == ['ansible']
    assert listify_lookup_plugin_terms(['foo', '{{name}}'], templar, loader=None) == ['foo', 'ansible']

# Generated at 2022-06-13 16:29:46.468242
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    import ansible.utils.unsafe_proxy
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()

    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    dummy_options = {'_ansible_verbosity': 0, '_ansible_no_log': False}

    templar = Templar(loader=loader, variables=variable_manager, options=dummy_options)

    # test with variables
    term = ansible.utils.unsafe_proxy.UnsafeProxy('{{ foo }}')

# Generated at 2022-06-13 16:29:54.829142
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.six import BytesIO
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.template import Templar

    vault = VaultLib([])

    test_string = u'''
- foo
- bar
- {{ baz }}
- {{ 'fizz' | upper }}
'''.strip()

    terms = [u'foo', u'bar', [u'fizz'], u'buzz']

    data = AnsibleLoader(BytesIO(test_string), vault.secrets).get_single_data()

    templar = Templar(loader=AnsibleLoader(data, vault.secrets))

   

# Generated at 2022-06-13 16:30:08.677154
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    try:
        from ansible.utils.vars import AnsibleVars
        from jinja2 import Template
        from ansible.template import Templar
        from ansible.parsing.yaml.loader import AnsibleLoader
        import pytest
    except ImportError:
        raise ImportError

    def mock_vars_obj():
        my_dict = {
            'name': 'Bob',
            'age': '20',
            'fruits': [ {'name': 'apple', 'color': 'red'},
                        {'name': 'banana', 'color': 'yellow'},
                        {'name': 'orange', 'color': 'orange'}],
            'empty_list': [],
            'empty_dict': {},
        }

        vars_obj = AnsibleVars(my_dict)
        return v

# Generated at 2022-06-13 16:30:17.946429
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.template import Templar
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.vars.manager import VariableManager

    terms = 'foo'
    templar = Templar(loader=AnsibleLoader(variable_manager=VariableManager()))
    assert listify_lookup_plugin_terms(terms, templar=templar, loader=AnsibleLoader) == ['foo']

    terms = AnsibleUnsafeText('foo')
    templar = Templar(loader=AnsibleLoader(variable_manager=VariableManager()))
    assert listify_lookup_plugin_terms(terms, templar=templar, loader=AnsibleLoader) == ['foo']


# Generated at 2022-06-13 16:30:29.468702
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    import ansible.parsing.yaml.objects
    from ansible.playbook.play_context import PlayContext

    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager

    # A class implementing mock template methods needed by lookup plugins
    # Make sure to update test if you add methods to ojbect
    class TemplarMock():

        def __init__(self, loader, inventory, play_context):
            pass

        def set_available_variables(self, variables):
            pass


# Generated at 2022-06-13 16:30:40.966538
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    class DummyVarsModule(object):
        def __init__(self, loader, play_context):
            self._loader = loader
            self._play_context = play_context
            self._data = {}
        def set_data(self, data):
            self._data = data
        def get_vars(self):
            return self._data

    loader = DataLoader()
    play_context = PlayContext()
    templar = Templar(loader=loader, variables=DummyVarsModule(loader=loader, play_context=play_context))


# Generated at 2022-06-13 16:30:52.578328
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    import ansible.constants as C

    loader = DataLoader()
    variable_manager = VariableManager()

    my_vars = {'hostvars': {'host1': {'foo': 'bar'}}}
    variable_manager.set_host_variable(host='host1', varname='foo', value='bar')
    templar = Templar(loader=loader, variables=variable_manager, fail_on_undefined=C.DEFAULT_UNDEFINED_VAR_BEHAVIOR)

    terms = None
    test_terms = listify_lookup_plugin_terms(terms, templar, loader)
    assert test_terms == [None]

    terms

# Generated at 2022-06-13 16:31:01.216739
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.template import Templar

    loader = DataLoader()
    variable_manager = VariableManager()
    templar = Templar(loader=loader, variable_manager=variable_manager)

    # Test to ensure listify_lookup_plugin_terms properly handles a unicode
    # string as input
    original = u"my_var"
    result = listify_lookup_plugin_terms(original, templar, loader)
    assert isinstance(result, list)
    assert len(result) == 1
    assert is_unicode_string(result[0])
    assert result[0] == u"my_var"

    # Test to ensure listify_lookup_plugin_terms properly handles a unicode
   

# Generated at 2022-06-13 16:31:10.586879
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    TEST_TERM = {
        'definitions': [
            AnsibleUnsafeText('a'),
            AnsibleUnsafeText('b'),
            AnsibleUnsafeText('c')
        ]
    }

    TEST_TERM_VARS = {"m": 'ansible', "n": 'lookup'}

    # test passing a list
    terms = listify_lookup_plugin_terms(TEST_TERM['definitions'], None, None)
    assert(terms == TEST_TERM['definitions'])

    # test passing a string
    a_terms = listify_lookup_plugin_terms(TEST_TERM['definitions'][0], None, None)

# Generated at 2022-06-13 16:31:19.303043
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.module_utils.six import PY3


# Generated at 2022-06-13 16:31:29.038866
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.errors import AnsibleError

    loader = DataLoader()
    templar = Templar(loader=loader)

    # test string
    assert listify_lookup_plugin_terms('foo', templar, loader) == ['foo']

    # test list
    assert listify_lookup_plugin_terms('["foo", "bar"]', templar, loader) == ['foo', 'bar']

    # test dict
    assert listify_lookup_plugin_terms('{"foo": "bar"}', templar, loader) == [{'foo': 'bar'}]

    # test undef with fail_on_undefined

# Generated at 2022-06-13 16:31:30.366347
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    listify_lookup_plugin_terms(None, Templar(loader=None, variables={}), loader=None)

# Generated at 2022-06-13 16:31:52.510934
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ..module_utils.common import AnsibleModule

    import ansible.plugins.lookup as lookup_plugins
    import jinja2
    import sys

    if sys.version_info >= (3, 0):
        from io import StringIO
        from io import BytesIO
    else:
        from StringIO import StringIO
        from cStringIO import StringIO as BytesIO

    mock_loader = lookup_plugins.LookupLoader()

    class TestTemplar(object):
        def __init__(self, basedir, variables=None):
            if not variables:
                variables = dict()

            lookups = lookup_plugins.LookupBase.get_lookup_plugins(loader=mock_loader)

# Generated at 2022-06-13 16:31:59.944887
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    # Loader requires a basedir to avoid looking for templates in cwd
    loader=DataLoader()

    # Templar needs a variables dictionary
    templar = Templar(loader=loader, variables={'var1':[u'val1']})

    assert listify_lookup_plugin_terms(['a', 'b', 'c'], templar, loader)==[u'a', u'b', u'c']
    assert listify_lookup_plugin_terms('a', templar, loader) == [u'a']
    assert listify_lookup_plugin_terms('a, b, c', templar, loader) == [u'a, b, c']
    assert listify_lookup_plugin_terms

# Generated at 2022-06-13 16:32:03.678228
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    assert listify_lookup_plugin_terms('foo', None, None) == ['foo']
    assert listify_lookup_plugin_terms(['foo'], None, None) == ['foo']

# Generated at 2022-06-13 16:32:14.399334
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.utils.listify import listify_lookup_plugin_terms
    from ansible.template import Templar
    from ansible import context
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import merge_hash

    base_vars = VariableManager()

# Generated at 2022-06-13 16:32:22.758684
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible import constants as C

    terms1 = "{{ foo }} {{ bar }}"
    terms2 = "{{ foo.bar }}"
    terms3 = "{{ foo }} bar"
    terms4 = "foo{{ bar }}"
    terms5 = ["foo", "{{ bar }}"]
    terms6 = "foo bar"
    terms7 = {"a":"{{ b }}"}

    tmpvar = dict(foo="fiddlediddle", bar="dumdum", b="baz")

    templar = Templar(loader=None, variables=tmpvar)

    assert listify_lookup_plugin_terms(terms1, templar, loader=None) == ["fiddlediddle", "dumdum"]

# Generated at 2022-06-13 16:32:31.582050
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.yaml.loader import AnsibleLoader

    terms = '{{ foo }}'
    templar = Templar(loader=AnsibleLoader(None), variables={'foo': [1, 2]})
    result = listify_lookup_plugin_terms(terms, templar, loader=None)
    assert result == [1, 2]
    terms = ['{{ foo }}']
    templar = Templar(loader=AnsibleLoader(None), variables={'foo': [3, 4]})
    result = listify_lookup_plugin_terms(terms, templar, loader=None)
    assert result == [[3, 4]]

# Generated at 2022-06-13 16:32:40.266486
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils._text import to_text
    from ansible.template import Templar
    from ansible import context
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.module_utils._collections_compat import Sequence

    templar = Templar(loader=None, variables=dict(hostvars=dict(host1=dict(var1='value1', var2='value2'))))

    # test simple string variable
    assert listify_lookup_plugin_terms('{{var1}}', templar, None) == ['value1']

    # test simple string with dict lookup
    assert listify_lookup_plugin_terms('{{hostvars.host1.var2}}', templar, None) == ['value2']

    # test simple string template
    assert listify_look

# Generated at 2022-06-13 16:32:49.681565
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible import constants as C
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar
    from ansible.inventory.manager import InventoryManager

    template = Templar(variables=VariableManager(loader=DataLoader()), loader=DataLoader())

    assert listify_lookup_plugin_terms('foo', template) == ['foo']

    assert listify_lookup_plugin_terms(['foo', 'bar', 'baz'], template) == ['foo', 'bar', 'baz']

    assert listify_lookup_plugin_terms(None, template) == ['None']

    assert listify_lookup_plugin_terms(['{{foo}}'], template, fail_on_undefined=True) == ['{{foo}}']

   

# Generated at 2022-06-13 16:32:58.398358
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.vars import VariableManager
    import pytest
    from copy import copy

    # We need to mock out several things here to make this work
    t_vars = AnsibleMapping()
    t_vars['item'] = 'elem1'

    loader = None
    variable_manager = VariableManager()
    variable_manager._extra_vars = t_vars

    templar = Templar(loader=loader, variables=variable_manager)

    # Simple test
    result = listify_lookup_plugin_terms('item', templar, loader)
    assert result[0] == 'elem1'

    # Test a list

# Generated at 2022-06-13 16:33:05.828406
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    terms = listify_lookup_plugin_terms(['a', {'b': ['c']}])
    assert terms == ['a', {'b': ['c']}], 'listify_lookup_plugin_terms returned incorrect data'

    terms = listify_lookup_plugin_terms('a,b')
    assert terms == ['a', 'b'], 'listify_lookup_plugin_terms returned incorrect data'

    terms = listify_lookup_plugin_terms('a, b')
    assert terms == ['a', 'b'], 'listify_lookup_plugin_terms returned incorrect data'

# Generated at 2022-06-13 16:33:43.643400
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    '''
    Unit test for function listify_lookup_plugin_terms
    '''
    from ansible.template import Templar
    from ansible.parsing.yaml.loader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory

    variable_manager = VariableManager()
    loader = DataLoader()

    # Create mock inventory
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list=[])
    variable_manager.set_inventory(inventory)

    templar = Templar(loader=loader, variables=variable_manager)

    fail_on_undefined = True
    convert_bare = False

    # Test with a string that doesn't contain a variable
    terms = 'foo, bar, baz'

# Generated at 2022-06-13 16:33:50.905964
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    module = MockModule()
    templar = Templar(loader=None, variables={})
    assert listify_lookup_plugin_terms("hello world", templar, None) == ["hello world"]
    assert listify_lookup_plugin_terms("{{ prefix }}{{ list }}", templar, None, convert_bare=True, fail_on_undefined=True) == [""]
    assert listify_lookup_plugin_terms("prefix{{ list }}", templar, None, convert_bare=True, fail_on_undefined=True) == ["prefix"]
    assert listify_lookup_plugin_terms("prefix{{ list }}", templar, None, convert_bare=True, fail_on_undefined=False) == ["prefix{{ list }}"]


# Generated at 2022-06-13 16:33:55.614576
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib

    loader = DictDataLoader({
        "vars.yml": """
            foo: bar
            baz: qux
        """
    })
    # Create a fake inventory, so the loader works
    class FakeInventory():
        pass

    loader.set_basedir("/")
    fake_loader = DictDataLoader({})
    fake_loader.set_basedir("/")
    fake_vault_secrets = ['secret0']

    templar = Templar(loader=loader, variables={}, vault_secrets=fake_vault_secrets)

# Generated at 2022-06-13 16:34:05.061505
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.dataloader import DataLoader

    def _get_vault_secret(vault_password, vault_id):
        # TODO: load real vault to test
        return 'mysec'

    class FakeTemplar(object):
        def __init__(self):
            pass

        def template(self, term, fail_on_undefined=True, convert_bare=False):
            return term['a']

    class FakeLoader(object):
        def __init__(self):
            pass

    loader = FakeLoader()
    templar = FakeTemplar()
    templar.set_available_variables(dict())


# Generated at 2022-06-13 16:34:13.373288
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    '''
    Test listify_lookup_plugin_terms function with different input type.
    '''
    import sys
    import os
    import pytest
    from ansible.errors import AnsibleUndefinedVariable
    from ansible.template import Templar
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext

    # Load fake inventory
    inventory_path = os.path.dirname(os.path.realpath(__file__))
    inventory_path += "/../../../tests/utils/test-inventory"
    loader = DataLoader()

# Generated at 2022-06-13 16:34:25.327325
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.common._collections_compat import Mapping, Sequence
    from ansible import constants as C
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar

    src_ds = DataLoader()
    tgt_ds = DataLoader()
    var_mgr = VariableManager()
    var_mgr.set_inventory(tgt_ds.inventory)
    var_mgr.extra_vars = {'answer': 42}
    var_mgr.options_vars = {'target_foo': "I'll be in the vars"}
    templar = Templar(loader=src_ds, variables=var_mgr)

    # Test case where terms is a scalar of the correct type
   

# Generated at 2022-06-13 16:34:36.103469
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleSequence

    from ansible.template import Templar

    assert listify_lookup_plugin_terms(AnsibleUnsafeText('foo'), Templar({})) == ['foo']
    assert listify_lookup_plugin_terms(AnsibleUnsafeText('foo'), Templar({}), convert_bare=True) == [b'foo']
    assert listify_lookup_plugin_terms('foo', Templar({})) == ['foo']
    assert listify_lookup_plugin_terms(AnsibleSequence(['foo']), Templar({})) == ['foo']

# Generated at 2022-06-13 16:34:45.738104
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    my_vars = dict(
        foo='hello world',
        bar=['cow', 'pig', 'chicken'],
    )

    t = Templar(variables=my_vars)

    assert listify_lookup_plugin_terms(['{{ [ "hello world" ] }}'], t, None) == ['hello world']

    assert listify_lookup_plugin_terms(['{{ foo }}'], t, None) == [u'hello world']

    assert listify_lookup_plugin_terms(['{{ bar }}'], t, None) == [u'cow', u'pig', u'chicken']


# Generated at 2022-06-13 16:34:51.613689
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    import ansible.template.template

    t = ansible.template.template.Template(None, None)
    assert listify_lookup_plugin_terms('stringy', t, None) == ['stringy']
    assert listify_lookup_plugin_terms(['str', 'ingy'], t, None) == ['str', 'ingy']
    t.fail_on_undefined = True
    try:
        assert listify_lookup_plugin_terms(t.template('{{test}}'), t, None) == []
        assert False
    except:
        assert True

# Generated at 2022-06-13 16:35:00.729136
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    # Test string
    test_listify_lookup_plugin_terms_string_templar = Templar(loader=None, variables={})
    test_listify_lookup_plugin_terms_string = test_listify_lookup_plugin_terms_string_templar.template(
        "this is a string", convert_bare=True, fail_on_undefined=True)

    assert isinstance(test_listify_lookup_plugin_terms_string, list)
    assert test_listify_lookup_plugin_terms_string == ["this is a string"]

    # Test list
    test_listify_lookup_plugin_terms_list_templar = Templar(loader=None, variables={})
    test_listify_lookup_plugin_terms_list = test_list