

# Generated at 2022-06-13 16:25:13.108290
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    import ansible.template
    loader = None  # not used
    env = ansible.template.environment.Environment()
    templar = ansible.template.Template(loader=loader, environment=env)
    assert listify_lookup_plugin_terms('foo', templar, loader) == ['foo']
    assert listify_lookup_plugin_terms('foo,bar', templar, loader) == ['foo', 'bar']
    assert listify_lookup_plugin_terms([1, 2, 3], templar, loader) == [1, 2, 3]
    assert listify_lookup_plugin_terms(['foo', 'bar'], templar, loader) == ['foo', 'bar']
    # with templating

# Generated at 2022-06-13 16:25:20.409992
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.vault import VaultLib

    v = VaultLib(password_file=None)
    m = VariableManager()
    t = Templar(m, vault_secrets=v)

    # test single scalar
    assert listify_lookup_plugin_terms('foo', t) == ['foo']
    assert listify_lookup_plugin_terms(u'foo', t) == ['foo']
    assert listify_lookup_plugin_terms(5, t) == [5]
    assert listify_lookup_plugin_terms(True, t) == [True]
    assert listify_lookup_plugin_terms(False, t) == [False]

    # test single iterable (list, set, tuple)
   

# Generated at 2022-06-13 16:25:29.104165
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    in_vars = dict(foo='bar', biz='baz')
    in_inventory = {}
    in_loader = DataLoader()
    in_variable_manager = VariableManager(loader=in_loader, inventory=in_inventory)

    in_variable_manager.set_nonpersistent_facts(in_vars)
    in_templar = Templar(loader=in_loader, variables=in_variable_manager)

    # Should return a list
    assert listify_lookup_plugin_terms('{{ foo }}', in_templar, loader=in_loader) == ['bar']

# Generated at 2022-06-13 16:25:39.169786
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    ''' listify_lookup_plugin_terms() takes a list of values and returns a list, no matter what '''

    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    from ansible.template import Templar

    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.parsing.yaml.objects import AnsibleSequence

    # some objects that pretend to be strings, mappings, and sequences
    class FakeString(AnsibleBaseYAMLObject):
        def __init__(self, data):
            self.data = data

        def __str__(self):
            return str(self.data)


# Generated at 2022-06-13 16:25:51.893019
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.common import template_replacer
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.dumper import AnsibleDumper

    from ansible.template import Templar

    loader = AnsibleLoader(template_replacer, None, AnsibleDumper)
    tmplar = Templar(loader=loader)

    assert listify_lookup_plugin_terms(terms=None, templar=tmplar, loader=loader) == ["None"]
    assert listify_lookup_plugin_terms(terms=['b','c','d', '{{a}}'], templar=tmplar, loader=loader, fail_on_undefined=False) == ['b', 'c', 'd', '{{a}}']

    assert listify_look

# Generated at 2022-06-13 16:26:01.113634
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    # Set up mock AnsibleModule
    from ansible.compat.tests import unittest
    from ansible.module_utils.facts import default_collectors
    from ansible.module_utils._text import to_native
    from ansible.parsing.vault import VaultLib
    from ansible.template import Templar

    class MockModule(object):
        def __init__(self, params):
            self.params = params

    class MockVault(object):
        def __init__(self, password):
            self.password = password

        def decrypt(self, value):
            return value

    class MockLoaderObj(object):
        def __init__(self):
            self._vault = MockVault(password='password')

    class MockVarsModule(object):
        def __init__(self):
            self._

# Generated at 2022-06-13 16:26:11.898340
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible import constants as C
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleUnicode

    import os
    import tempfile

    from ansible.module_utils.common._collections_compat import Mapping

    class TestVarsModule:
        def __init__(self, basedir):
            self.basedir = basedir

        def get_vars(self, loader, path, entities, cache=True):
            ''' Just return a single value, based on the task '''
            return dict(ansible_local=dict(basedir=self.basedir))

    class TestTemplar(Templar):
        ''' A test class to load a specific vars module '''
        def set_loader(self, loader):
            self._loader = loader

       

# Generated at 2022-06-13 16:26:20.414782
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    facts = dict(foo="some_string")
    templar = Templar(loader=None, variables=facts)
    assert [u'some_string'] == listify_lookup_plugin_terms(u"{{ foo }}", templar, None)
    assert [u'some_string'] == listify_lookup_plugin_terms(u"{{ foo }}", templar, None, convert_bare=True)
    assert [u'{{ foo }}'] == listify_lookup_plugin_terms(u"{{ foo }}", templar, None, convert_bare=False)
    assert [u"{{ foo }}"] == listify_lookup_plugin_terms(u"{{ foo }}", templar, None, fail_on_undefined=False)
    assert [u"{{ foo }}"]

# Generated at 2022-06-13 16:26:31.886012
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    import ansible.errors

    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    from units.mock.loader import DictDataLoader

    # TODO: There is no mock for a playbook
    from ansible.playbook import Playbook

    templar = Templar(loader=DataLoader(), variables={})
    terms = ["a","b"]
    result = listify_lookup_plugin_terms(terms, templar, None)
    assert result == ["a","b"]

    templar = Templar(loader=DataLoader(), variables={'a':"c"})
    terms = "{{a}}"
    result = listify_lookup_plugin_terms(terms, templar, None)
    assert result == ["c"]


# Generated at 2022-06-13 16:26:41.741578
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    import sys
    import os
    import json
    import tempfile
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    class Options(object):
        def __init__(self, connection=None, module_path=None, forks=None, become=None, become_method=None, become_user=None, check=None, diff=None, listhosts=None, listtasks=None, listtags=None, syntax=None):
            self.connection = connection
            self.module_path = module_path
            self.forks = forks
            self.become = become
            self.become_method = become_method
            self.become_user = become_user
            self.check = check

# Generated at 2022-06-13 16:26:50.547957
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    import ansible.constants as C
    import ansible.parsing.yaml.objects as yObjects
    import ansible.template as template

    # Set up template/ansible objects
    _loader = C.DEFAULT_LOADER
    _loader.set_basedir('/tmp')
    _loader.path_backup = _loader.path
    _templar = template.AnsibleTemplar(loader=_loader, variables={'foo': 'bar'})

    # test 1: string
    string = '"{{ foo }}"'
    assert listify_lookup_plugin_terms(string, _templar, _loader) == ['bar']

    # test 2: yaml list
    string = '["{{ foo }}", "bar"]'

# Generated at 2022-06-13 16:26:58.061081
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing import DataLoader
    from ansible.template import Templar
    from ansible.vars import VariableManager

    loader = DataLoader()
    v = VariableManager()
    templar = Templar(loader=loader, variables=v)

    terms = "foo"
    assert listify_lookup_plugin_terms(terms, templar, loader) == ["foo"]

    terms = ["foo", "bar", "baz"]
    assert listify_lookup_plugin_terms(terms, templar, loader) == ["foo", "bar", "baz"]

# Generated at 2022-06-13 16:27:06.943846
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.template import Templar

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.set_inventory(loader.inventory)
    templar = Templar(loader=loader, variables=variable_manager)
    terms = 'foo, bar, bam'
    expected = ['foo', 'bar', 'bam']
    result = listify_lookup_plugin_terms(terms, templar, loader)
    assert result == expected, 'Terms not converted to a list'
    terms = 'foo and bar'
    expected = ['foo and bar']
    result = listify_lookup_plugin_terms(terms, templar, loader)

# Generated at 2022-06-13 16:27:17.566568
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    from ansible.utils.vars import Combiner
    from ansible.template import Templar

    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost'])
    variable_manager.set_inventory(inventory)
    variable_manager.extra_vars = {'foo': 'bar'}


# Generated at 2022-06-13 16:27:27.457413
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib

    templar = Templar(None, vault_secrets=[VaultLib()], loader=None)
    assert listify_lookup_plugin_terms('foo', templar, None) == ['foo'], 'failed to listify a string'

    assert listify_lookup_plugin_terms([None], templar, None) == [None], 'failed to listify a list that contains None'

    assert listify_lookup_plugin_terms(AnsibleUnsafeText(u'foo'), templar, None) == ['foo']
    assert listify_lookup_plugin_terms(42, templar, None) == [42]
    assert listify

# Generated at 2022-06-13 16:27:39.948831
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    class DummyVarsModule:
        def __init__(self, value):
            self.value = value
        def __getitem__(self, name):
            return self.value

    class DummyTemplate:
        def __init__(self, value):
            self.value = value
        def template(self, term, **kwargs):
            return self.value

    class DummyLoader:
        pass

    assert listify_lookup_plugin_terms(
        ['foo', 'bar'],
        DummyTemplate(['foo', 'bar']),
        DummyLoader(),
        fail_on_undefined=True,
        convert_bare=False) == ['foo', 'bar']


# Generated at 2022-06-13 16:27:49.413614
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    class DummyVarsModule(object):
        def vars(self):
            return {'foo': 'bar'}

    class DummyInventoryModule(object):
        def host_vars(self, name):
            return {'foo': 'notbar'}

    class DummyPlayContext(object):
        def __init__(self):
            self.inventory = DummyInventoryModule()

    class DummyLoader(object):
        def get_basedir(self, play=None):
            return "/dev/null"

    class DummyVarManager(object):
        def __init__(self):
            self._fact_cache = None
            self._vars_cache = {}


# Generated at 2022-06-13 16:27:55.670504
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleUnicode
    class C(object):
        pass
    templar = Templar(loader=C())
    failed = False
    try:
        listify_lookup_plugin_terms(AnsibleUnicode('localhost'), templar, C())
    except:
        failed = True
    assert not failed


# Generated at 2022-06-13 16:28:07.105011
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.common._collections_compat import Mapping

    terms = "{{ foo }}"
    templar = FakeTemplar({'foo': 'bar'})
    assert ['bar'] == listify_lookup_plugin_terms(terms, templar, None)

    terms = "{{ foo }}"
    templar = FakeTemplar({'foo': ['bar', 'baz']})
    assert ['bar', 'baz'] == listify_lookup_plugin_terms(terms, templar, None)

    terms = "{{ foo }}"
    templar = FakeTemplar({'foo': {'bar': 'baz'}})
    assert [{'bar': 'baz'}] == listify_lookup_plugin_terms(terms, templar, None)

   

# Generated at 2022-06-13 16:28:18.013140
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    # Import here to stub in the test
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins import plugin_loader

    templar = Templar(loader=None, variables={}, fail_on_undefined=True)
    templar._available_variables = {
        'foo': '123',
        'bar': 456,
        'list': [
            'a',
            'b',
            'c',
        ],
    }


# Generated at 2022-06-13 16:28:29.393743
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    '''
    Verify behavior of listify_lookup_plugin_terms
    '''

    # Verify that if a string is provided, it is returned in a list
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    t = Templar(DataLoader())
    terms = "test string"
    assert listify_lookup_plugin_terms(terms, t, DataLoader()) == [terms]

    # Verify that if a dict is provided, it is returned in a list
    terms = {"test": "dict"}
    assert listify_lookup_plugin_terms(terms, t, DataLoader()) == [terms]

    # Verify that items in list are processed by template

# Generated at 2022-06-13 16:28:38.777595
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    #from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    templar = Templar(loader=DataLoader())

    def get_failed_items(terms):
        return [t for t in templar.template(terms) if templar.template(t, fail_on_undefined=True) == 'FAILED']

    # test passing a string
    assert listify_lookup_plugin_terms('foo', templar, loader) == ['foo']
    assert listify_lookup_plugin_terms('', templar, loader) == ['']
    assert listify_lookup_plugin_terms('{{foo}}', templar, loader) == ['FAILED']
    assert listify_

# Generated at 2022-06-13 16:28:49.212281
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.template import Templar

    loader = DataLoader()
    variable_manager = VariableManager()
    my_vars = {"snake_oil": "over the rainbow"}
    variable_manager.set_host_variable(host=None, varname='hostvars', value=my_vars)
    templar = Templar(loader=loader, variables=variable_manager)

    my_input = '{{snake_oil}}'
    my_output = listify_lookup_plugin_terms(my_input, templar, loader, False)
    assert my_output == ['over the rainbow']

    my_input = 'foo {{snake_oil}}'
    my_output = listify_lookup_

# Generated at 2022-06-13 16:29:00.618317
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar

    loader = DataLoader()
    variable_manager = VariableManager()

    templar = Templar(loader=loader, variables=variable_manager)


# Generated at 2022-06-13 16:29:10.223149
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.six import BytesIO
    from ansible.plugins import lookup_loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.template import Templar
    from ansible.vars import VariableManager

    dataloader = DataLoader()
    variable_manager = VariableManager()

    class MockedLookupPlugin:

        def run(self, terms, **kwargs):
            return terms

    lookup_loader.add(MockedLookupPlugin, 'mock')
    lookup = lookup_loader.get('mock', {})


# Generated at 2022-06-13 16:29:20.346738
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.plugins.loader import lookup_loader, module_loader
    from ansible.template.template import Templar

    def _create_templar(variables):
        loader = module_loader._create_loader()
        variable_manager = loader.get('variable_manager')
        variable_manager.extra_vars = variables
        return Templar(loader=loader, variables=variable_manager)

    templar = _create_templar({})
    assert listify_lookup_plugin_terms([1, 2, 3], templar, templar.loader) == [1, 2, 3]
    assert listify_lookup_plugin_terms(1, templar, templar.loader) == [1]

# Generated at 2022-06-13 16:29:30.368734
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    class randomclass:
        pass

    class myvars(dict):
        def get(self, key, defval=None):
            if key == 'omg':
                return 1
            return defval

    class myloader:
        def get_basedir(self, path):
            return '/'

    def test_fail_on_undefined(variable):
        raise Exception("Should not be called")

    templar = Templar(loader=myloader(), variables=myvars())
    templar.environment.globals['randomclass'] = randomclass

    # simple string tests
    assert listify_lookup_plugin_terms('t1', templar, myloader()) == ['t1']

# Generated at 2022-06-13 16:29:35.619673
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    import ansible.parsing.dataloader
    from ansible.template import Templar
    loader = ansible.parsing.dataloader.DataLoader()
    templar = Templar(loader=loader)

    assert listify_lookup_plugin_terms('foo', templar, loader) == ['foo']
    assert listify_lookup_plugin_terms(['foo'], templar, loader) == ['foo']
    assert listify_lookup_plugin_terms(['{{ foo }}', 'bar'], templar, loader, convert_bare=True) == ['foo', 'bar']
    assert listify_lookup_plugin_terms('[1, 2, 3]', templar, loader) == ['1', '2', '3']

# Generated at 2022-06-13 16:29:46.987826
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    class FakeVarManager():
        def __init__(self, *args, **kwargs):
            pass

        def get_vars(self, *args, **kwargs):
            return dict()

        def add_host_vars(self, *args, **kwargs):
            return dict()

        def add_group_vars(self, *args, **kwargs):
            return dict()

        def add_task_vars(self, *args, **kwargs):
            return dict()

        def set_host_variable(self, *args, **kwargs):
            return dict()

        def set_task_variable(self, *args, **kwargs):
            return dict()

        def set_host_facts(self, *args, **kwargs):
            return dict()

       

# Generated at 2022-06-13 16:29:55.181269
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    fake_loader = "fake_loader"
    fake_shared_loader = "fake_shared_loader"

    templar = Templar(loader=fake_loader, shared_loader=fake_shared_loader)


# Generated at 2022-06-13 16:30:08.626896
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.set_inventory(loader.load_inventory('localhost'))
    templar = Templar(loader=loader, variables=variable_manager)


# Generated at 2022-06-13 16:30:17.915719
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    # First, we construct a mock templar.
    mock = MockTemplar()

    # string type
    input = "{{ item1 }}{{ item2 }}"
    expected = ['item1item2']
    actual = listify_lookup_plugin_terms(input, mock, None)
    assert expected == actual

    # list type
    input = ["{{ item1 }}{{ item2 }}"]
    expected = ['item1item2']
    actual = listify_lookup_plugin_terms(input, mock, None)
    assert expected == actual

    # tuple type
    input = ("{{ item1 }}{{ item2 }}", 'notemplate')
    expected = ['item1item2', 'notemplate']
    actual = listify_lookup_plugin_terms(input, mock, None)
    assert expected == actual

# Generated at 2022-06-13 16:30:29.419488
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    import os
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    terms = u'{{ lookup("pipe", "cat /tmp/test_pipe_lookup_plugin_args") }}'

    with open("/tmp/test_pipe_lookup_plugin_args", "w") as testfh:
        testfh.write("""
---
- "one"
- "two"
- "three"
- "four"
- "five"
- "six"
- "seven"
- "eight"
- "nine"
- "ten"
""")

    assert terms == '{{ lookup("pipe", "cat /tmp/test_pipe_lookup_plugin_args") }}'


# Generated at 2022-06-13 16:30:40.967750
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    templar = Templar(loader=None, variables={})

    # test basic string
    assert listify_lookup_plugin_terms('test', templar, None) == ['test']

    # test basic list
    assert listify_lookup_plugin_terms(['a', 'b'], templar, None) == ['a', 'b']

    # test template
    assert listify_lookup_plugin_terms('{{ test }}', templar, None) == ['{{ test }}']

    # test simple jinja2

# Generated at 2022-06-13 16:30:52.578096
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    terms = "{{ 'a, b, c' }}"
    templar = Templar(loader=None)
    assert listify_lookup_plugin_terms(terms, templar, loader=None, fail_on_undefined=True, convert_bare=False) == ['a, b, c']

    terms = "{{ ['a', 'b', 'c'] }}"
    assert listify_lookup_plugin_terms(terms, templar, loader=None, fail_on_undefined=True, convert_bare=False) == ['a', 'b', 'c']

    terms = "{{ ['a', 'b', 'c'] | to_json }}"

# Generated at 2022-06-13 16:31:00.907530
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    # Testing a single string
    assert listify_lookup_plugin_terms('foo', None, None) == ['foo']
    assert listify_lookup_plugin_terms('[bar, baz]', None, None) == ['[bar, baz]']

    assert listify_lookup_plugin_terms(['foo'], None, None) == ['foo']
    assert listify_lookup_plugin_terms(['foo', 'bar'], None, None) == ['foo', 'bar']
    assert listify_lookup_plugin_terms('foo, bar', None, None) == ['foo', 'bar']
    assert listify_lookup_plugin_terms(['foo', ['bar', 'baz']], None, None) == ['foo', ['bar', 'baz']]

# Generated at 2022-06-13 16:31:10.423143
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import get_file_vault_secret
    from ansible.template import Templar
    import os, yaml
    yaml.warnings({'YAMLLoadWarning': False})

    lookup_loader_mock = None
    templar_mock = Templar(loader=lookup_loader_mock, vault_secrets=[], vault_password='')

    # test string
    terms = 'string'
    expected_result = ['string']
    assert listify_lookup_plugin_terms(terms, templar_mock, lookup_loader_mock) == expected_result

    # test string, templated
    terms = '{{ string }}'
    expected_result = ['string']
    assert listify_look

# Generated at 2022-06-13 16:31:19.223071
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    try:
        import unittest2 as unittest
    except ImportError:
        import unittest

    from ansible.template import Templar

    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.vault import VaultLib

    class TestListifyLookupPluginTerms(unittest.TestCase):

        def setUp(self):

            loader = AnsibleLoader(None, vault_password_file=None)
            vault = VaultLib(None, None)

            self.templar = Templar(loader, vault)

        def test_single(self):
            term = '{{ test_var }}'
            vars = dict(
                test_var='foo',
            )

# Generated at 2022-06-13 16:31:26.651935
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    loader = DictDataLoader({})
    templar = Templar(loader=loader)

    strings = ['this is a string', 'this is also a string', 'so is this']
    assert listify_lookup_plugin_terms(strings[0], templar, loader) == [strings[0]]
    assert listify_lookup_plugin_terms(strings, templar, loader) == strings
    assert listify_lookup_plugin_terms(strings, templar, loader, convert_bare=True) == strings

# Generated at 2022-06-13 16:31:37.421494
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    terms = "a,b,c"
    templar = Templar(loader=None, variables=VariableManager(), shared_loader_obj=None)
    assert listify_lookup_plugin_terms(terms, templar, None) == ['a', 'b', 'c']

    terms = [ "a", "b", "c" ]
    templar = Templar(loader=None, variables=VariableManager(), shared_loader_obj=None)
    assert listify_lookup_plugin_terms(terms, templar, None) == ['a', 'b', 'c']

    terms = ['{{ foo }}', '{{ bar }}', 'baz']
    templar = Templar

# Generated at 2022-06-13 16:31:54.790535
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template.safe_eval import safe_eval
    from ansible.template import Templar
    terms = 'foo_'
    templar = Templar(loader=None, variables={'foo': 'bar'})
    terms = listify_lookup_plugin_terms(terms, templar=templar, loader=None, fail_on_undefined=True, convert_bare=False)
    assert terms == ['bar_']

# Generated at 2022-06-13 16:32:01.640653
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    """
    >>> from ansible.module_utils import basic
    >>> from ansible.module_utils.template import Templar
    >>> from ansible.parsing.mod_args import ModuleArgsParser
    >>> from ansible.template import Templar

    >>> terms = [u'foo', '{{var}}', [u'alpha', u'beta', '{{var2}}']]

    >>> mock_args = dict(var='bar', var2='gamma')
    >>> t = Templar(loader=None, variables=mock_args)

    >>> listify_lookup_plugin_terms(terms, t, None)
    [u'foo', 'bar', [u'alpha', u'beta', 'gamma']]
    """

# Generated at 2022-06-13 16:32:13.044802
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.yaml.loader import AnsibleLoader

    loader = AnsibleLoader(None, dict())
    templar = Templar(loader=loader)

    class FakeVarsModule1(object):
        def vars(self):
            return dict(foo='bar', baz=dict(bing='bong'))
    fake_vars_module1 = FakeVarsModule1()

    class FakeVarsModule2(object):
        def get_vars(self, loader, play, host, task):
            return dict(foo='baz', baz=dict(bing='baz'))
    fake_vars_module2 = FakeVarsModule2()


# Generated at 2022-06-13 16:32:22.582938
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    import json
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    class VarsModule:
        def get_vars(self, loader, path, entities, cache=True):
            return {}

    inv = InventoryManager(loader=DataLoader())
    vars_mgr = VariableManager(loader=DataLoader(), inventory=inv)
    templar = Templar(loader=DataLoader(), variables=vars_mgr)


# Generated at 2022-06-13 16:32:28.599251
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    ''' unit test for listify_lookup_plugin_terms '''

    from ansible.template import Templar
    from ansible import constants as C

    class FakeVarsModule(object):
        def get_vars(self, loader, path, entities, cache=True):
            return {}
    vars_mock = FakeVarsModule()

    class FakeLoaderModule(object):
        _basedir = 'testdir'

        def __init__(self):
            pass

        def path_dwim_relative(self, basedir, given, source=True):
            return given

        def get_basedir(self):
            return self._basedir


    class FakeVarManager():
        def __init__(self, loader=None, inventory=None):
            pass

        def set_inventory(self, inventory):
            pass



# Generated at 2022-06-13 16:32:39.180376
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible import errors

    templar = Templar(loader=None)
    # the following is from a real ansible-playbook run
    assert listify_lookup_plugin_terms('{{ var1 }}', templar, None) == ['{{ var1 }}']
    assert listify_lookup_plugin_terms('{{ var2 }}', templar, None) == ['{{ var2 }}']
    assert listify_lookup_plugin_terms(['{{ var3 }}'], templar, None) == ['{{ var3 }}']
    # the following are unit test cases
    assert listify_lookup_plugin_terms(['1'], templar, None) == ['1']
    assert listify_lookup_plugin_terms(['1', '2'], templar, None)

# Generated at 2022-06-13 16:32:49.318325
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    ctx = PlayContext()
    ctx._loader = True
    templar = Templar(loader=True, variables={'x': 'X', 'y': ['Y1', 'Y2'], 'z': 'Z'})

    assert listify_lookup_plugin_terms(['a', ['b', 'c'], '{{x}}', '{{y}}'], templar, True) == ['a', 'b', 'c', 'X', 'Y1', 'Y2']
    assert listify_lookup_plugin_terms('a', templar, True) == ['a']
    assert listify_lookup_plugin_terms(['a', 'b'], templar, True) == ['a', 'b']
   

# Generated at 2022-06-13 16:32:58.137144
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.common._collections_compat import namedtuple
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    def wrapped_lookup_error(*args, **kwargs):
        raise AnsibleAssertionError()

    mock_loader = namedtuple('mock_loader', ['loaders'])

    templar = Templar(loader=mock_loader, variables = VariableManager())
    templar._fail_on_lookup_errors = True
    templar._fail_on_undefined_errors = True
    templar._original_file = '<test_terms>'
    templar._templar = templar
    templar._available_vari

# Generated at 2022-06-13 16:33:03.893090
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    assert listify_lookup_plugin_terms("foo", None, None) == ["foo"]
    assert listify_lookup_plugin_terms(["foo"], None, None) == ["foo"]
    assert listify_lookup_plugin_terms("  foo bar  ", None, None) == ["foo bar"]
    assert listify_lookup_plugin_terms("  foo 'bar  ' ", None, None) == ["foo bar"]

# Generated at 2022-06-13 16:33:10.330457
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    args = {'terms': '{{ foo }}', 'templar': None, 'loader': None, 'fail_on_undefined': True}
    assert listify_lookup_plugin_terms(**args) == ['{{ foo }}']

    args['terms'] = 42
    assert listify_lookup_plugin_terms(**args) == [42]

    # FIXME: requires better mocking
    #args['terms'] = '{{ foo }} {{ bar }}'
    #assert listify_lookup_plugin_terms(**args) == ['{{ foo }}', '{{ bar }}']

# Generated at 2022-06-13 16:33:44.933759
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    import ansible.parsing.yaml
    terms = '{{foo}}'
    templar = Templar(loader, variables=dict(foo=['bar', 'baz']))
    assert listify_lookup_plugin_terms(terms, templar) == ['bar', 'baz']
    terms = ['{{foo}}']
    templar = Templar(loader, variables=dict(foo=['bar', 'baz']))
    assert listify_lookup_plugin_terms(terms, templar) == ['bar', 'baz']
    terms = ['{{foo}}', '{{bar}}']
    templar = Templar(loader, variables=dict(foo=['bar', 'baz'], bar='qux'))

# Generated at 2022-06-13 16:33:57.056125
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.common._collections_compat import Sequence
    from ansible.template import Templar

    mock_loader = None
    mock_templar = Templar(loader=mock_loader)

    # Test case insensitivity
    assert isinstance(listify_lookup_plugin_terms(["foo", "bar"], templar=mock_templar, loader=mock_loader, fail_on_undefined=False, convert_bare=True), Sequence)
    assert isinstance(listify_lookup_plugin_terms(["foo", "bar"], templar=mock_templar, loader=mock_loader, fail_on_undefined=False, convert_bare=False), Sequence)

    # Test with string

# Generated at 2022-06-13 16:34:06.689103
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.common._collections_compat import Mapping

    # Importing here so we don't need to worry about it during test-time
    from ansible.module_utils.six import PY3

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.set_vault_secrets(loader.set_vault_secrets(['default']))
    variable_manager.extra_vars = {'foo': 'abc', 'five': '5', 'dictionary': {'complex': 'object'}}
    play_context = PlayContext()
    play_context

# Generated at 2022-06-13 16:34:15.563696
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    class TestTemplar(object):
        def template(self, data, convert_bare=False, fail_on_undefined=True):
            if fail_on_undefined:
                return data
            else:
                return ''

    class TestLoader(object):
        pass

    templar = TestTemplar()
    loader = TestLoader()

    data = [1, 2, 3]
    assert listify_lookup_plugin_terms(data, templar, loader) == data

    data = '{{ lookup("env", "HOME") }}'
    assert listify_lookup_plugin_terms(data, templar, loader) == [data]

    data = '{{ lookup("env", "HOME") }}'

# Generated at 2022-06-13 16:34:28.106087
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib

    templar = Templar(loader=None, variables={})

    assert listify_lookup_plugin_terms(["a", "b"], templar, None) == ["a", "b"]
    assert listify_lookup_plugin_terms("a b", templar, None) == ["a", "b"]
    assert listify_lookup_plugin_terms("a,b", templar, None) == ["a", "b"]
    assert listify_lookup_plugin_terms("{{a}}", templar, None) == ["{{a}}"]

# Generated at 2022-06-13 16:34:35.018804
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    # Verify that strings are converted to a one-element list
    assert listify_lookup_plugin_terms('string', None, None) == ['string']

    # Verify that lists are not altered
    assert listify_lookup_plugin_terms(['list', 'of', 'strings'], None, None) == ['list', 'of', 'strings']

    # Verify that a tuple is converted to a list
    assert listify_lookup_plugin_terms(('tuple', 'of', 'strings'), None, None) == ['tuple', 'of', 'strings']

# Generated at 2022-06-13 16:34:45.051606
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    import jinja2
    import ansible.vars
    import ansible.template

    env = ansible.template.AnsibleEnvironment(loader=jinja2.DictLoader({}))
    t = ansible.template.AnsibleTemplate(u"{{'a,b,c'}}", env)
    results = listify_lookup_plugin_terms(t.template, t, t._loader)
    assert results == ['a,b,c']

    t = ansible.template.AnsibleTemplate(u"[ 'a', 'b', 'c' ]", env)
    results = listify_lookup_plugin_terms(t.template, t, t._loader)
    assert results == ['a', 'b', 'c']


# Generated at 2022-06-13 16:34:52.922831
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    # Test a string
    terms = '{{ item }}'
    templar = MockTemplar(terms)
    assert listify_lookup_plugin_terms(terms, templar, None) == [['{{', 'item', '}}']]

    # Test a string with convert_bare=True
    terms = '{{ item }}'
    templar = MockTemplar(terms)
    assert listify_lookup_plugin_terms(terms, templar, None, convert_bare=True) == ['{{ item }}']

    # Test an empty list
    terms = []
    templar = MockTemplar(terms)
    assert listify_lookup_plugin_terms(terms, templar, None) == [[]]

    # Test a list
    terms = ['{{ item }}', '{{ other_item }}']


# Generated at 2022-06-13 16:35:01.503944
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    templar = DummyTemplar()
    loader = DummyLoader()
    assert listify_lookup_plugin_terms('value1', templar, loader) == ['value1']
    assert listify_lookup_plugin_terms(['value1'], templar, loader) == ['value1']

    # with templating
    assert listify_lookup_plugin_terms('{{value1}}', templar, loader) == ['value1']
    assert listify_lookup_plugin_terms(['{{value1}}'], templar, loader) == ['value1']
    assert listify_lookup_plugin_terms(['{{value1}}', 'value2'], templar, loader) == ['value1', 'value2']

    # with templating and failures
    templar.fail_on