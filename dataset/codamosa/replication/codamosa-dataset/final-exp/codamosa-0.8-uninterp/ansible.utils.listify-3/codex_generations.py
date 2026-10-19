

# Generated at 2022-06-13 16:25:11.300109
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    # Bare variable
    assert listify_lookup_plugin_terms('{{foo}}', None, None, fail_on_undefined=False) == [{{foo}}]
    assert listify_lookup_plugin_terms('{{foo}}', None, None, fail_on_undefined=False, convert_bare=True) == ['foo']
    assert listify_lookup_plugin_terms('foo', None, None, fail_on_undefined=False) == ['foo']
    assert listify_lookup_plugin_terms('foo', None, None, fail_on_undefined=False, convert_bare=True) == ['foo']

    # List with bare variable
    assert listify_lookup_plugin_terms(['{{foo}}'], None, None, fail_on_undefined=False) == ['{{foo}}']
    assert list

# Generated at 2022-06-13 16:25:20.866645
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    # Probably better to test ansible.templar module separately, but started
    # this and it got out of hand...
    templar = Templar(loader=None, variables={})

    assert listify_lookup_plugin_terms(['item1'], templar, loader=None) == ['item1']
    assert listify_lookup_plugin_terms('item1', templar, loader=None) == ['item1']
    assert listify_lookup_plugin_terms(['item1', 'item2'], templar, loader=None) == ['item1', 'item2']
    assert listify_lookup_plugin_terms('item1, item2', templar, loader=None) == ['item1', 'item2']
    assert listify_lookup_plugin_terms

# Generated at 2022-06-13 16:25:27.936779
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    # backport
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    import ansible.parsing.yaml.objects
    import ansible.template.safe_eval
    import ansible.template.template
    import ansible.vars.unsafe_proxy

    doc = """
    - hello
    - 1
    - 2.5
    """

    terms = ansible.parsing.yaml.objects.AnsibleBaseYAMLObject.from_yaml(doc)
    assert isinstance(terms, list)
    assert len(terms) == 3
    assert isinstance(terms[0], ansible.parsing.yaml.objects.AnsibleBaseYAMLObject)

# Generated at 2022-06-13 16:25:38.381774
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    mock_loader = Mock()
    mock_loader.get_basedir.return_value = 'mocked_basedir'

    templar = Templar(loader=mock_loader, variables={})
    assert listify_lookup_plugin_terms('foo', templar, mock_loader) == ['foo']
    assert listify_lookup_plugin_terms(['foo'], templar, mock_loader) == ['foo']
    assert listify_lookup_plugin_terms(dict(foo='foo'), templar, mock_loader) == [dict(foo='foo')]
    assert listify_lookup_plugin_terms(1, templar, mock_loader) == [1]

# Generated at 2022-06-13 16:25:50.873415
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.six import PY3
    if PY3:
        unicode = str
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.template import Templar
    from ansible.utils.vars import merge_hash

    templar = Templar(loader=None, variables={})
    values = [42, dict(a=42), AnsibleUnicode('42'), '{{fortytwo}}', u'foo{{fortytwo}}']

    for value in values:
        assert listify_lookup_plugin_terms(value, templar, None, False) == [42]


# Generated at 2022-06-13 16:26:00.429402
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    import json
    import sys
    from ansible.module_utils.six import PY3

    # need templar and loader before we can proceed
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar

    class FakeSrc:
        def __init__(self):
            self.paths = ["."]

    data = """
    {
        "a": 1,
        "b": [ "c", "d", "e" ],
        "c": {
            "d": {
                "e": "f",
                "g": "h"
            }
        }
    }
    """

    loader = DataLoader()
    variable_manager = VariableManager()

# Generated at 2022-06-13 16:26:11.740952
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    class DummyVars(dict):
        def get_vars(self, loader, play, host=None, task=None):
            return {}

        def get_hostvars(self, tqm, host):
            return {}

    variable_manager = VariableManager(loader=DataLoader(), inventory=None, variable_manager=DummyVars())
    templar = Templar(loader=loader, variables=variable_manager)

    # test string with spaces
    terms = listify_lookup_plugin_terms('http://1.2.3.4/foo/bar.zip', templar, loader)
    assert isinstance(terms, list)

# Generated at 2022-06-13 16:26:20.269340
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.template import Templar
    import os

    terms = '"{{ foo }}", "{{ bar }}"'
    current_path = os.getcwd()
    lookup_loader = os.path.join(current_path, 'ansible/module_utils/facts/')
    templar = Templar(loader=None, variables={'foo': 'one', 'bar': 'two'}, shared_loader_obj=None, vault_secrets=None)
    result = listify_lookup_plugin_terms(terms, templar, lookup_loader)

# Generated at 2022-06-13 16:26:31.736826
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.common._collections_compat import Mapping, Sequence, Set
    from ansible.module_utils.common._collections_compat import Mapping, Sequence, Set
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.plugins.loader import lookup_loader
    from ansible.utils import template

    # TODO: add a clean `templar` mock that does not depend on `DistributionFactCollector` for simple unit tests
    templar = template.Templar(loader=lookup_loader, shared_loader_obj=DistributionFactCollector(), disable_lookups=True)

# Generated at 2022-06-13 16:26:41.501866
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.dataloader import DataLoader

    templar = Templar(VaultLib(),  dict(), loader=DataLoader())
    assert listify_lookup_plugin_terms('foo', templar, DataLoader()) == ['foo']
    assert listify_lookup_plugin_terms(['foo'], templar, DataLoader()) == ['foo']
    assert listify_lookup_plugin_terms(['foo', 'bar'], templar, DataLoader()) == ['foo', 'bar']

    assert listify_lookup_plugin_terms('', templar, DataLoader()) == ['']
    assert listify_lookup_plugin_terms([''], templar, DataLoader()) == ['']

# Generated at 2022-06-13 16:26:50.442308
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    lookup_loader = DataLoader()

    lookup_templar = Templar(None, loader=lookup_loader)

    # Test with an empty string
    assert listify_lookup_plugin_terms("", lookup_templar, lookup_loader) == ['']

    # Test with a list of string
    assert listify_lookup_plugin_terms("hello, world", lookup_templar, lookup_loader) == ['hello', 'world']

    # Test with an empty list
    assert listify_lookup_plugin_terms("[]", lookup_templar, lookup_loader) == ['']

    # Test with a list of int

# Generated at 2022-06-13 16:27:01.189438
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    '''
    dict lookups should be converted to list, not just if they are a string
    '''
    from ansible.module_utils.common.path import unfrackpath
    from ansible.module_utils.six import StringIO
    from ansible.errors import AnsibleUndefinedVariable
    from ansible.template import Templar
    from ansible import constants as C
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext 

    basedir = unfrackpath('/tmp/ansible/test/lookup_plugins')

# Generated at 2022-06-13 16:27:04.553358
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    import ansible.template
    t = ansible.template.AnsibleTemplate()
    assert listify_lookup_plugin_terms('hello', t, None) == ['hello']
    assert listify_lookup_plugin_terms(['hello'], t, None) == ['hello']

# Generated at 2022-06-13 16:27:10.650377
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.module_utils.six import PY3

    # test value as list of strings
    assert [u'test'], listify_lookup_plugin_terms([u'test'], Templar({}))

    # test value as an iterable of strings
    assert [u'test'], listify_lookup_plugin_terms(iter([u'test']), Templar({}))

    # test value as a string
    if PY3:
        # TODO: can't find a way to get a string_types object
        # that PY3 accepts as a string type, not a bytes type
        pass
    else:
        assert [u'test'], listify_lookup_plugin_terms(u'test', Templar({}))

# Generated at 2022-06-13 16:27:19.742903
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible import constants as C
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    loader = DataLoader()
    options = C._get_default_options()

    plugin_terms = '{{ item }}'
    terms = listify_lookup_plugin_terms(plugin_terms, Templar(loader=loader, variables=variable_manager), loader)
    assert terms[0] == plugin_terms

    plugin_terms = [plugin_terms]
    terms = listify_lookup_plugin_terms(plugin_terms, Templar(loader=loader, variables=variable_manager), loader)
    assert terms[0] == plugin_terms

    # Test with a list of different types

# Generated at 2022-06-13 16:27:28.736832
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    templar = Templar(loader=None)


# Generated at 2022-06-13 16:27:40.784412
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play

    variable_manager = VariableManager()
    loader = DataLoader()

    inventory = InventoryManager(loader=loader, variable_manager=variable_manager)
    variable_manager.set_inventory(inventory)

    play_source =  dict(
            name = "neo",
            hosts = 'webservers',
            gather_facts = 'no',
            tasks = [
                dict( action=dict( module='debug', args=dict( msg='{{ my_var }}' ) ) ),
            ]
        )


# Generated at 2022-06-13 16:27:50.173160
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()
    templar = Templar(loader=loader, variable_manager=variable_manager)

    # test variables
    vars = {'var1': 'foo', 'var2': 'bar'}
    variable_manager.set_nonpersistent_facts(vars)

    # test listify_lookup_plugin_terms
    for term in ['{{ var1 }}', '{{ var1 }}, {{ var2 }}', ['{{ var1 }}', '{{ var2 }}']]:
        terms = listify_lookup_plugin_terms(term, templar)
        assert(isinstance(terms, list))

# Generated at 2022-06-13 16:28:01.709793
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.template import Templar

    loader = DataLoader()
    variable_manager = VariableManager()
    templar = Templar(loader=loader, variables=variable_manager)

    # Test if string is returned as a one element list
    assert listify_lookup_plugin_terms('value', templar, loader, convert_bare=False) == ['value']

    # Test if list is returned as is
    assert listify_lookup_plugin_terms(['value1', 'value2'], templar, loader, convert_bare=False) == ['value1', 'value2']

    # Test if list is returned as is

# Generated at 2022-06-13 16:28:11.012366
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    assert listify_lookup_plugin_terms(
        "{{ item }}",
        Templar(loader=None), None, False
    ) == ["{{ item }}"]

    assert listify_lookup_plugin_terms(
        ["{{ item }}"],
        Templar(loader=None), None, False
    ) == ["{{ item }}"]

    assert listify_lookup_plugin_terms(
        "item1",
        Templar(loader=None), None, False
    ) == ["item1"]

    assert listify_lookup_plugin_terms(
        ["item1", "item2"],
        Templar(loader=None), None, False
    ) == ["item1", "item2"]

# Generated at 2022-06-13 16:28:22.493497
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar

    my_vars = dict(a='1', b='2', c='3', d='4')
    loader = DataLoader()
    templar = Templar(loader=loader, variables=my_vars)

    print('TEST 1')
    terms1 = '{{ [a, b, c] }}'
    terms1 = listify_lookup_plugin_terms(terms1, templar, loader)
    assert terms1 == ['1', '2', '3']

    print('TEST 2')
    terms2 = ['{{ a }}', '{{ b }}']
    terms2 = listify_lookup_plugin_terms(terms2, templar, loader)
    assert terms2 == ['1', '2']



# Generated at 2022-06-13 16:28:30.430109
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    import json
    import copy
    import sys
    import os

    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
    import ansible.utils.async_wrapper
    import ansible.template

    template_data = {
        '_raw_params': '{{ items }}',
        'items': ['foo', 'bar'],
    }

    templar = ansible.template.Templar(loader=ansible.parsing.dataloader.DataLoader(), variables=template_data)


# Generated at 2022-06-13 16:28:39.027771
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    fake_loader = None
    strings = [
        "string",
        "string with spaces",
        "string with     spaces",
        "string\nwith\nnewlines",
        "string with an {{ var }}",
        "string with an {{ var | default('unset_var') }}"
    ]
    expected = [
        ["string"],
        ["string with spaces"],
        ["string with     spaces"],
        ["string\nwith\nnewlines"],
        ["string with an {{ var }}"],
        ["string with an {{ var | default('unset_var') }}"]
    ]
    actual = [listify_lookup_plugin_terms(s, Templar(loader=fake_loader), fake_loader) for s in strings]
    assert actual == expected


# Generated at 2022-06-13 16:28:49.435891
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.plugins.lookup import LookupBase

    class TestLookupModule(LookupBase):

        def __init__(self, basedir=None, runner=None, **kwargs):
            pass

        def run(self, terms, variables=None, **kwargs):
            raise Exception("run() was invoked, the test failed")

    test_lookup = TestLookupModule()

    def test_templar(terms, convert_bare=False):

        def test_templar_fail(terms, convert_bare=False):
            return ""

        if terms == "Failed":
            raise test_lookup.AnsibleError("lookup() was invoked, the test failed")
        if terms == "FailOnUndefined":
            return test_templar_fail(terms, convert_bare=convert_bare)


# Generated at 2022-06-13 16:29:00.723587
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleSequence

    variable_manager = VariableManager()
    variable_manager.set_nonpersistent_facts({'first' : '1st', 'second' : '2nd'})

    terms = AnsibleMapping()
    terms['not_a_var'] = 'my_value'
    terms['first'] = '{{first}}'
    terms['second'] = '{{second}}'
    terms['list'] = AnsibleSequence()
    templar = Templar(loader=None, variables=variable_manager)

    terms = listify_lookup_plugin_terms(terms, templar, loader=None)
    assert isinstance(terms, dict)


# Generated at 2022-06-13 16:29:10.282499
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    templar = Templar(loader=None, variables={})

    lookup_plugin_terms = """
        ---
        a: 1
        b: # 2
        c: yes
        d:
          - aaa
          - bbb
          - yes
        e: "{{ a }}"
        """
    expected = [{'a': 1, 'b': '# 2', 'c': 'yes', 'd': ['aaa', 'bbb', 'yes'], 'e': 1}]

    results = listify_lookup_plugin_terms(lookup_plugin_terms, templar, loader=None, convert_bare=False)
    assert results == expected

    lookup_plugin_terms = "{{ a }}"
    expected = [1]

    results = listify_lookup_plugin_terms

# Generated at 2022-06-13 16:29:20.380060
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.module_utils.six import PY2
    from ansible.module_utils.common._collections_compat import MutableMapping, MutableSequence

    class VarManager(object):
        def __init__(self):
            self.vars = {'a': "foo"}

    vars_mgr = VarManager()
    templar = Templar(loader=None, variables=vars_mgr)
    assert listify_lookup_plugin_terms(['foo', ['bar', 'baz'], {1: 'qux'}], templar, loader=None,
                                       fail_on_undefined=True, convert_bare=False) \
                                       == ['foo', ['bar', 'baz'], {1: 'qux'}]

# Generated at 2022-06-13 16:29:29.105140
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.parsing.vault import VaultLib
    from ansible.template import Templar

    terms = "{{ lookup('file', '/etc/ansible/hosts') }}"
    vault_password = 'VaultPasswordHere'
    vault = VaultLib([])
    assert vault.is_encrypted(terms)
    assert vault.is_encrypted(terms)
    terms = vault.decrypt(terms, vault_password).strip()
    # AnsibleModule, loader
    templar = Templar(loader=None, variables={}, vault_secrets=[])
    terms = listify_lookup_plugin_terms(terms, templar, None, False, False)

    assert terms == ['localhost']

# Generated at 2022-06-13 16:29:38.955704
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    my_loader = DictDataLoader({})
    my_env = Environment()
    my_templar = Templar(loader=my_loader, variables={}, fail_on_undefined=True)

    # test string -> list
    assert listify_lookup_plugin_terms("foo", my_templar, my_loader) == ["foo"]

    # test iterable -> list
    assert listify_lookup_plugin_terms(["foo", "bar"], my_templar, my_loader) == ["foo", "bar"]

    # test list -> list
    assert listify_lookup_plugin_terms(["foo"], my_templar, my_loader) == ["foo"]

    # test noniterable -> list

# Generated at 2022-06-13 16:29:48.945690
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager()
    templar = Templar(loader=loader, variable_manager=variable_manager)

    # listify with string and template
    original = '{{ a + "/" + b }}'
    expected = ['foo/bar']
    vars = {'a': 'foo', 'b': 'bar'}
    variable_manager.set_nonpersistent_facts(vars)
    result = listify_lookup_plugin_terms(original, templar, loader, convert_bare=True)
    assert expected == result

    # test with non-string

# Generated at 2022-06-13 16:30:01.905537
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import merge_hash
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    vars_manager = VariableManager()
    templar = Templar(loader=loader, variables=vars_manager)
    vars_manager._extra_vars = merge_hash({'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f'})

    # Test empty string
    assert listify_lookup_plugin_terms('', templar, loader, fail_on_undefined=True, convert_bare=False) == ['']

    # Test string with spaces
    assert listify_

# Generated at 2022-06-13 16:30:10.623952
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar
    templar = Templar(loader=None, shared_loader_obj=None)

    # test with a string
    terms = '{{ foo }}/{{ bar }}'
    terms = listify_lookup_plugin_terms(terms, templar=templar, loader=None, fail_on_undefined=True, convert_bare=False)
    assert isinstance(terms, list), terms

    # test with a list, where there is no templating
    terms = ['foo', 'bar']
    terms = listify_lookup_plugin_terms(terms, templar=templar, loader=None, fail_on_undefined=True, convert_bare=False)
    assert isinstance(terms, list), terms

    # test with a list, where there are templates

# Generated at 2022-06-13 16:30:15.774405
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    vault_secrets = VaultLib([])
    templar = Templar(loader=loader, variables={}, fail_on_undefined=True, vault_secrets=vault_secrets)

    assert listify_lookup_plugin_terms(templar, loader, fail_on_undefined=True, terms='foo') == ['foo']
    assert listify_lookup_plugin_terms(templar, loader, fail_on_undefined=True, terms='foo,') == ['foo']

# Generated at 2022-06-13 16:30:26.196854
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    templar = Templar(loader=loader)

    assert listify_lookup_plugin_terms('foo', templar, loader) == ['foo']
    assert listify_lookup_plugin_terms(['foo'], templar, loader) == ['foo']
    assert listify_lookup_plugin_terms(['foo', 'bar'], templar, loader) == ['foo', 'bar']
    assert listify_lookup_plugin_terms({'a': 'b'}, templar, loader) == [{'a': 'b'}]

# Generated at 2022-06-13 16:30:35.423336
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    loader = DictDataLoader({})
    variable_manager = VariableManager(loader=loader)
    templar = Templar(loader=loader, variables=variable_manager)

    assert listify_lookup_plugin_terms(['foo'], templar, loader) == ['foo']
    assert listify_lookup_plugin_terms(['foo', 'bar'], templar, loader) == ['foo', 'bar']

    assert listify_lookup_plugin_terms('foo', templar, loader, convert_bare=True) == ['foo']
    assert listify_lookup_plugin_terms('foo bar', templar, loader, convert_bare=True) == ['foo', 'bar']
    assert listify_lookup_plugin_

# Generated at 2022-06-13 16:30:43.998447
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    # test invalid input
    assert listify_lookup_plugin_terms(None) == [None]
    assert listify_lookup_plugin_terms(23) == [23]

    # test string input and simple jinja2 templating
    assert listify_lookup_plugin_terms('foo') == ["foo"]
    assert listify_lookup_plugin_terms('foo bar') == ["foo bar"]

    # test lists as input returning a list is input
    assert listify_lookup_plugin_terms(['foo', 'bar']) == ['foo', 'bar']
    assert listify_lookup_plugin_terms(('foo', 'bar')) == ['foo', 'bar']

    from collections import namedtuple
    Point = namedtuple('Point', ['x', 'y'])
    assert listify_lookup_plugin

# Generated at 2022-06-13 16:30:55.059432
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils._text import to_text
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar
    import pytest

    dataloader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.extra_vars = dict(foo="bar")
    templar = Templar(loader=dataloader, variables=variable_manager, fail_on_undefined=True)

    # test string
    result = listify_lookup_plugin_terms('{{foo}}', templar, loader=dataloader)
    assert isinstance(result, list)
    assert result == ['bar']

    # test bare string that needs templating
    result = listify_lookup_plugin_

# Generated at 2022-06-13 16:31:02.586403
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    # some AnsibleModule to simulate real-world usage
    from ansible.module_utils.basic import AnsibleModule

    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    module  = AnsibleModule({'my_var': 'foo'})
    templar = Templar(loader=DataLoader(), variables=module.params)

    assert listify_lookup_plugin_terms('{{ my_var }}', templar, DataLoader()) == ['foo']
    assert listify_lookup_plugin_terms(42, templar, DataLoader()) == ['42']

# Generated at 2022-06-13 16:31:11.412311
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode


# Generated at 2022-06-13 16:31:19.554744
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar
    from ansible.vars import VariableManager

    vars_mgr = VariableManager()

    t = Templar(loader=None, variables=vars_mgr)

    # Check that listify_lookup_plugin_terms converts string input to list
    assert listify_lookup_plugin_terms('my_word', t, None) == ['my_word']

    # Check that it also accepts a list
    assert listify_lookup_plugin_terms(['my_word'], t, None) == ['my_word']

    # Check that it accepts a template
    assert listify_lookup_plugin_terms('{{my_word}}', t, None) == [None]

    # Check that it accepts a list of templates

# Generated at 2022-06-13 16:31:37.297491
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible import constants as C
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.playbook.play_context import PlayContext
    from ansible.utils.vars import combine_vars
    from ansible.module_utils._text import to_bytes

    loader = DataLoader()
    templar = Templar(loader=loader, variables=VariableManager())

    C.HOST_KEY_CHECKING = False
    vault_secret = 'dummypass'
    vault_password_file = '/tmp/ansible_vault.password'

# Generated at 2022-06-13 16:31:45.020576
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    templar = Templar(loader=loader, variables={'a': 'blue', 'b': 'green', 'c': 'red', 'd': ['red', 'green', 'blue']})

    assert listify_lookup_plugin_terms('{{a}}', templar, loader) == ['blue']
    assert listify_lookup_plugin_terms('{{b}}', templar, loader) == ['green']
    assert listify_lookup_plugin_terms('{{a}}:{{b}}:{{c}}', templar, loader) == ['blue:green:red']
    assert listify_lookup_plugin

# Generated at 2022-06-13 16:31:51.188705
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible import templating
    from ansible.template import Templar

    my_vars = dict(a=1, b=2, c=[3,4], d=dict(e=5,f=6))
    my_loader = DictDataLoader({})
    my_templar = Templar(loader=my_loader, variables=my_vars)

    # Test a string is returned as a list with the string
    value = 'test'
    expected_value = [value]
    assert listify_lookup_plugin_terms(value, my_templar, my_loader) == expected_value

    # Test a list is returned as a list
    value = ['test', 'test2', 'test3']
    expected_value = value

# Generated at 2022-06-13 16:31:59.030688
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible import errors
    assert listify_lookup_plugin_terms(' string ') == ['string']
    assert listify_lookup_plugin_terms({'a': 1, 'b': 2}) == [{'a': 1, 'b': 2}]
    assert listify_lookup_plugin_terms([1, 2, 3]) == [1, 2, 3]
    assert listify_lookup_plugin_terms(1) == [1]
    assert listify_lookup_plugin_terms(True) == [True]
    assert listify_lookup_plugin_terms(False) == [False]
    assert listify_lookup_plugin_terms(None) == [None]
    assert listify_lookup_plugin_terms(['a', 'b']) == ['a', 'b']
    assert listify_

# Generated at 2022-06-13 16:32:11.233058
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    play_context = PlayContext()
    templar = Templar(loader=None, variables=dict())

    # test when terms is a string
    terms = 'foo'
    result = listify_lookup_plugin_terms(terms, templar, loader=None)
    assert result == ['foo']

    # test when terms is a list
    terms = ['foo']
    result = listify_lookup_plugin_terms(terms, templar, loader=None)
    assert result == ['foo']

    # test when terms is a list of strings with a var
    terms = ["{{ foo }}"]
    templar._available_variables = play_context.get_variables(loader=None, play=None, host=None)

# Generated at 2022-06-13 16:32:18.628783
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    import pytest

    from ansible.template import Templar

    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.utils.vars import combine_vars
    from ansible.vars.unsafe_proxy import UnsafeProxy, wrap_var

    # This data structure can be used to test all the different
    # types of input that listify_lookup_plugin_terms should accept.

# Generated at 2022-06-13 16:32:29.787609
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    templar = Templar(loader=None, variables={})

    assert listify_lookup_plugin_terms([u'a', u'b'], templar, loader=None) == [u'a', u'b']
    assert listify_lookup_plugin_terms([u'a', u'b', u'{{foo}}'], templar, loader=None, fail_on_undefined=True) == [u'a', u'b', u'{{foo}}']
    assert listify_lookup_plugin_terms([u'a', u'b', u'{{foo}}'], templar, loader=None, fail_on_undefined=False) == [u'a', u'b']

# Generated at 2022-06-13 16:32:39.708767
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager

    terms = '{{ foo | join(",")  }}'
    templar = Templar(loader=DataLoader(), variables=VariableManager(loader=DataLoader(), inventory=InventoryManager()))
    templar._available_variables['foo'] = [1,2,3]

    result = listify_lookup_plugin_terms(terms=terms, templar=templar, loader=DataLoader(), fail_on_undefined=True)
    assert result == ['1','2','3']

# Generated at 2022-06-13 16:32:45.175139
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.common._collections_compat import OrderedDict
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    def t(x, fail_on_undefined=True, convert_bare=False):
        y = templar.template(x, convert_bare=convert_bare, fail_on_undefined=fail_on_undefined)
        assert isinstance(y, (string_types, Iterable))
        return y

    dataloader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.extra_vars = dict(item=['foo', 'bar'])

# Generated at 2022-06-13 16:32:55.602664
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib
    from ansible.utils.vault import VaultSecret
    from ansible.vars import VariableManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager

    v = VaultLib([])
    pw_src = VaultSecret(password='pw')
    v.secrets = [ pw_src ]
    loader = v._loader
    variable_manager = VariableManager()
    variable_manager.set_inventory(InventoryManager(loader=loader, sources=['localhost,']))
    variable_manager.set_vault_secrets([pw_src])

    variable_manager.extra_vars = { 'src' : 'src_value' }

# Generated at 2022-06-13 16:33:17.800509
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    class DummyTemplar(object):
        '''
        This is a dummy class used for unit testing without requiring the full templar module
        '''
        def __init__(self):
            self.available_variables = {u'item': u'first'}

        def template(self, terms, fail_on_undefined=True, convert_bare=True):
            if isinstance(terms, str):
                return self.available_variables.get(terms, terms)
            return terms

    dummy_templar = DummyTemplar()

    # Scenario - passing a string to function with templar result: 'first'
    result = listify_lookup_plugin_terms(u'item', dummy_templar, None)
    assert result == [u'first']

    # Scenario - passing a list of

# Generated at 2022-06-13 16:33:25.643173
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    terms = [u'A', [u'B', u'C'], u'D']
    templar = None
    loader = None
    fail_on_undefined = True
    convert_bare = False

    result = listify_lookup_plugin_terms(terms, templar, loader, fail_on_undefined, convert_bare)

    assert isinstance(result, list)
    assert isinstance(result[0], string_types)
    assert isinstance(result[1], list)
    assert isinstance(result[1][0], string_types)
    assert isinstance(result[1][1], string_types)
    assert isinstance(result[2], string_types)

# Generated at 2022-06-13 16:33:32.229720
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    import os

    class FakeLoader():
        class FakeTemplates():
            def __init__(self, path):
                self.path = path

            def get_basedir(self, path):
                return os.path.dirname(self.path)

            def path_dwim(self, path):
                return path

        def __init__(self, basedir):
            pass

        def get_basedir(self, path):
            return os.path.dirname(path)

        def path_dwim(self, path):
            return path

        def get_source(self, path):
            source = fake_templates.FakeTemplates(path)

# Generated at 2022-06-13 16:33:42.885395
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    # NOTE: this test is not exhaustive, only meant to change when the function changes

    from ansible.utils.listify import listify_lookup_plugin_terms
    from ansible.parsing.yaml.loader import AnsibleLoader


# Generated at 2022-06-13 16:33:50.465441
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    # test_listify_lookup_plugin_terms: invalid terms
    invalid_terms = (
        None,
        1,
        2.0,
        True,
        False,
        {},
        {'a': 1},
        (1, 2),
    )

    # test_listify_lookup_plugin_terms: valid terms
    valid_terms = (
        '',
        '1',
        '1, 2',
        '1,2',
        '"a", "b", "c"',
        'a,b,c',
        [1, 2],
        [],
        ['a', 'b'],
        ['1', '2', '3'],
    )

    templar = Templar(loader=None)


# Generated at 2022-06-13 16:33:58.915471
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    terms = 1
    assert listify_lookup_plugin_terms(terms, None, None) == [1]

    terms = "1 2 3"
    assert listify_lookup_plugin_terms(terms, None, None) == [1, 2, 3]

    terms = ['1', '2', '3']
    assert listify_lookup_plugin_terms(terms, None, None) == [1, 2, 3]

    terms = [1, 2, 3]
    assert listify_lookup_plugin_terms(terms, None, None) == [1, 2, 3]



# Generated at 2022-06-13 16:34:06.912300
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible import constants as C

    templar = Templar(loader=DataLoader(), variables={})
    assert listify_lookup_plugin_terms(["a", "b"], templar, DataLoader(), fail_on_undefined=True, convert_bare=False) == ["a", "b"]
    assert listify_lookup_plugin_terms("a,b", templar, DataLoader(), fail_on_undefined=True, convert_bare=False) == ["a", "b"]
    assert listify_lookup_plugin_terms("{{a}},{{b}}", templar, DataLoader(), fail_on_undefined=True, convert_bare=False) == ["{{a}}", "{{b}}"]


# Generated at 2022-06-13 16:34:15.599390
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.playbook.play_context import PlayContext

    class DataLoader:
        def __init__(self):
            self.data = {}

    class Environment:
        def __init__(self, vars):
            self.vars = vars
            self.loader = DataLoader()

    class VariableManager:
        def __init__(self, vars):
            self.vars = vars
            self.loader = DataLoader()

    class Templar:
        def __init__(self, vars):
            self.vars = vars
            self.loader = DataLoader()


# Generated at 2022-06-13 16:34:24.305097
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    terms = listify_lookup_plugin_terms('foo')
    assert isinstance(terms, list)
    assert terms == ['foo']

    terms = listify_lookup_plugin_terms('foo, bar')
    assert isinstance(terms, list)
    assert terms == ['foo', 'bar']

    terms = listify_lookup_plugin_terms(['foo', 'bar', 'baz'])
    assert isinstance(terms, list)
    assert terms == ['foo', 'bar', 'baz']

# Generated at 2022-06-13 16:34:33.870242
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleUnicode

    templar = Templar(loader=None)

    assert listify_lookup_plugin_terms(AnsibleUnicode('a\n'), templar, None) == ['a']
    assert listify_lookup_plugin_terms(AnsibleUnicode('a'), templar, None) == ['a']
    assert listify_lookup_plugin_terms(['a'], templar, None) == ['a']
    assert listify_lookup_plugin_terms('a', templar, None) == ['a']