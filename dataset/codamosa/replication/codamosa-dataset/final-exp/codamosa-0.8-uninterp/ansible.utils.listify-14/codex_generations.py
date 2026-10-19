

# Generated at 2022-06-13 16:25:13.752394
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.module_utils.basic import AnsibleModule, AnsibleModuleDeprecationWarning
    import sys

    try:
        from ansible.parsing.dataloader import DataLoader
        from ansible.vars import VariableManager
        from ansible.inventory.manager import InventoryManager
        from ansible.template import Templar
        from ansible.playbook.play import Play

        HAS_ANSIBLE_MODULES = True

    except ImportError:
        HAS_ANSIBLE_MODULES = False

    if not HAS_ANSIBLE_MODULES:
        sys.exit()


# Generated at 2022-06-13 16:25:20.658636
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.yaml import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory

    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list=[])
    variable_manager.set_inventory(inventory)

    templar = Templar(loader=loader, variable_manager=variable_manager)

    my_terms = u"{{ ['a', 'b', 'c'] }}"
    listified_terms = listify_lookup_plugin_terms(my_terms, templar, loader)
    assert listified_terms == [u'a', u'b', u'c']


# Generated at 2022-06-13 16:25:27.809705
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variables = VariableManager(loader=loader, inventory=inventory)

    template_data = '["foo", "bar"]'
    template_data_1 = 'foo'
    test_data = [
        {
            'terms': template_data,
            'expected': ['foo', 'bar']
        },
        {
            'terms': template_data_1,
            'expected': ['foo']
        }

    ]

# Generated at 2022-06-13 16:25:38.386058
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    '''
    Test the listify_lookup_plugin_terms function
    '''
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.template import Templar

    secret1 = '$ANSIBLE_VAULT;1.2;AES256;foo\nbar\n'
    secret2 = '$ANSIBLE_VAULT;1.2;AES256;foo\nfoobar\n'

    loader = DictDataLoader({
        'secret1': secret1,
        'secret2': secret2,
    })

    secrets = {'vault_password_file': 'secrets'}
    vault = VaultLib([])
    vault.read_vault_secrets

# Generated at 2022-06-13 16:25:41.822545
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    terms = listify_lookup_plugin_terms([1, '{{foo}}', '{{bar}}'], Templar({}, {}, {}, None), None, fail_on_undefined=False)

    assert sorted(terms) == [1, '{{bar}}', '{{foo}}']



# Generated at 2022-06-13 16:25:49.434561
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    # Did not test this with a real templar, loader and env because it was too
    # complex.  Just tested we got back a list of items.
    terms = listify_lookup_plugin_terms(terms=['[1,2,3]', '{{a}}'], templar=None, loader=None)

    assert(isinstance(terms, list))
    assert(isinstance(terms[0], list))
    assert(isinstance(terms[1], string_types))

# Generated at 2022-06-13 16:25:59.968543
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    import sys

    class T(object):
        pass

    templar = Templar(loader=DataLoader(), variables=VariableManager(), shared_loader_obj=T())

    test_string = """
    foo
    bar
    baz
    """

    expected_result = ['foo\n', 'bar\n', 'baz\n']

    assert listify_lookup_plugin_terms(test_string, templar, None, False, False) == expected_result

    assert listify_lookup_plugin_terms(test_string.splitlines(), templar, None, False, False) == expected_result


# Generated at 2022-06-13 16:26:11.068854
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.template import Templar
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.dataloader import DataLoader
    # Set up dataloader and templar
    dl = DataLoader()
    t = Templar(dl)

    # Test single-item inputs
    for i in [u'item1', b'item1', [u'item1'], [b'item1'], 'item1']:
        assert listify_lookup_plugin_terms(i, t, dl) == [u'item1']

    # Test two-item inputs

# Generated at 2022-06-13 16:26:19.754553
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils._text import to_text
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import lookup_loader

    class VarsModule:
        def __init__(self, ids):
            self.ids = ids
        def run(self, terms, variables=None, **kwargs):
            return [terms] if isinstance(terms, string_types) else terms

    class VarsManager(VariableManager):
        def __init__(self):
            pass

# Generated at 2022-06-13 16:26:31.340185
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    # Stub out the templar and loader.
    class StubTemplar(object):
        def __init__(self):
            super(StubTemplar, self).__init__()

        def template(self, terms, convert_bare=False, fail_on_undefined=False):
            return terms

    class StubLoader(object):
        def __init__(self):
            super(StubLoader, self).__init__()

        def get_basedir(self, hostname):
            return "/a/b/c"

    templar = StubTemplar()
    loader = StubLoader()

    # We should be able to handle a string.
    assert listify_lookup_plugin_terms(terms="foo", templar=templar, loader=loader) == ["foo"]

    # We should be able to

# Generated at 2022-06-13 16:26:43.077393
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.vars.manager import VariableManager

    from ansible.template import Templar

    mgr = VariableManager()
    templar = Templar(loader=None, variables=mgr)
    vault = VaultLib()
    items = ['{{ vault_string }}', 'stuff', '{{ other }}', 1, 2, 3]

# Generated at 2022-06-13 16:26:50.305538
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    def _get_loader():
        return DataLoader()


# Generated at 2022-06-13 16:27:01.110137
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    class FakeVarsModule(object):
        def __init__(self):
            self.fact_cache = dict()

    variables = FakeVarsModule()

    templar = Templar(loader=None, variables=variables)

    terms = '{{ foo }}'
    retterms = listify_lookup_plugin_terms(terms=terms, templar=templar)
    assert not retterms

    terms = '{{ foo }}'
    variables.fact_cache = dict()
    variables.fact_cache['foo'] = [1, 2]
    retterms = listify_lookup_plugin_terms(terms=terms, templar=templar)
    assert retterms == [1, 2]

    terms = ['{{ foo }}']
    variables.fact_cache = dict()
   

# Generated at 2022-06-13 16:27:08.743970
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    terms = """
    {{ [ 'foo', 'bar', 'bat' ] }}
    {{ 'bam' }}
    {{ ( [ 'gronk', 'grunk' ] + [ 'funky' ] ) }}
    {{ 'borp' }}
    """
    templar = Templar(loader=loader)
    templar._available_variables = dict()

    new_list = listify_lookup_plugin_terms(terms, templar, loader)

    from ansible.compat.tests.mock import patch
    m = patch('ansible.module_utils.common.listify_lookup_plugin_terms.templar')
    m.start()

# Generated at 2022-06-13 16:27:18.836844
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    import ansible.template.template
    import ansible.template.safe_eval
    jenv = ansible.template.safe_eval.Math()
    templar = ansible.template.template.Templar(loader=None, variables={}, shared_loader_obj=None,
                                                searchpath=['.'], jinja2_env=jenv, environment=None)
    class VarsModule(object):
        def __init__(self):
            self.foo = "bar"

    loader = ansible.parsing.dataloader.DataLoader()
    loader.set_vars(VarsModule())

    # test string input
    terms = '{{ foo }}'
    terms = listify_lookup_plugin_terms(terms, templar, loader, False)
    assert terms == ['bar']

   

# Generated at 2022-06-13 16:27:28.371592
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.utils import plugin_docs

    class AnsibleOptions(object):
        connection = 'smart'
        module_path = None
        forks = 5
        become = None
        become_method = None
        become_user = None
        check = False
        diff = False

    class AnsibleRunner:
        def __init__(self):
            self.options = AnsibleOptions()
            self.loader = plugin_docs.get_loader()
            self.variable_manager = plugin_docs.get_variable_manager()

    test_runner_instance = AnsibleRunner()

    from ansible.template import Templar
    templar = Templar(loader=test_runner_instance.loader, variables=test_runner_instance.variable_manager)

    # Test: single string term

# Generated at 2022-06-13 16:27:40.752139
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    terms = """{
        "one": "1",
        "two": "2",
        "three": "3"
    }"""

    # Test setting a variable containing the stringified json
    assert listify_lookup_plugin_terms(terms, templar=None, loader=None) == [terms]

    # Test setting a variable to the output of a template
    assert listify_lookup_plugin_terms('{{ terms | to_json }}', templar=None, loader=None) == [terms]

    # Test setting a variable to a list containing the json as a string
    assert listify_lookup_plugin_terms(['{{ terms | to_json }}'], templar=None, loader=None) == [terms]

    # Test setting a variable to a list containing the json as a dictionary
    assert listify_lookup

# Generated at 2022-06-13 16:27:50.135476
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar

    loader = DataLoader()
    templar = Templar(loader=loader)

    def assert_iterable_equal(l1, l2):
        assert len(l1) == len(l2)
        for i in range(len(l1)):
            assert l1[i] == l2[i]

    assert_iterable_equal(["single"],
        listify_lookup_plugin_terms("single", templar, loader))
    assert_iterable_equal(["single"],
        listify_lookup_plugin_terms(["single"], templar, loader))

# Generated at 2022-06-13 16:28:01.709340
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.yaml.loader import AnsibleLoader

    lookup_loader = AnsibleLoader(None, variable_manager={}, loader=None)
    lookup_templar = Templar(loader=lookup_loader, variables={})

    # Test 1: Check for proper conversion when term is a string
    term = "{{ myvar }}"
    expected_result = 'myvar content'
    conversion_result = listify_lookup_plugin_terms(term, lookup_templar, lookup_loader, False, False)
    assert conversion_result == expected_result.split(':')

    # Test 2: Check for proper conversion when term is a dict
    term = dict(var1="{{ myvar1 }}", var2=2, var3="{{ myvar2 }}")
    expected_result

# Generated at 2022-06-13 16:28:12.308937
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    ''' test listify_lookup_plugin_terms() '''
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    inv_manager = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inv_manager)
    templar = Templar(loader=loader, inventory=inv_manager, variables=variable_manager)

    # test with string
    test_listify_lookup_plugin_terms_value1 = listify_lookup_plugin_terms("{{ foo }}", templar, loader)

# Generated at 2022-06-13 16:28:24.366104
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar
    from ansible.vars.unsafe_proxy import UnsafeProxy

    # Test list of dicts
    to_list = [{"common": "1", "unique": "a"}, {"common": "2", "unique": "b"}, {"common": "3", "unique": "c"}]
    templar = Templar(None, loader=None)
    assert listify_lookup_plugin_terms(to_list, templar=templar, loader=None) == [to_list]

    # Test list of strings
    to_list = ["1", "2", "3"]
    templar = Templar(None, loader=None)

# Generated at 2022-06-13 16:28:32.096642
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar
    from ansible import context
    import pytest
    from ansible.utils.vars import combine_vars

    # verify that it is idempotent
    assert listify_lookup_plugin_terms(['foo', 'bar'], Templar(variables={}), context.CLIARGS.get('vars_plugins', []), fail_on_undefined=True) == ['foo', 'bar']
    # and when undefined values are allowed
    assert listify_lookup_plugin_terms(['foo', 'bar'], Templar(variables={}), context.CLIARGS.get('vars_plugins', []), fail_on_undefined=False) == ['foo', 'bar']

# Generated at 2022-06-13 16:28:41.301932
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    import ansible.parsing.yaml.objects

    # Make sure we get a list back
    assert listify_lookup_plugin_terms('foo', None, None) == ['foo']

    # Make sure we can pass in a list and we get the same list back
    assert listify_lookup_plugin_terms(['foo'], None, None) == ['foo']

    # Make sure unicode strings are converted to regular strings
    assert listify_lookup_plugin_terms(u'foo', None, None) == ['foo']

    # Make sure any AnsibleUnicode is converted to regular strings
    u = ansible.parsing.yaml.objects.AnsibleUnicode()
    u.ansible_internals = dict(unicode_value='foo')

# Generated at 2022-06-13 16:28:48.771082
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    class FakeVarsModule(object):
        def __init__(self, name):
            self.name = name

        def __getattr__(self, name):
            return FakeVarsModule(name)

    class FakeVars:
        def __init__(self):
            self.ansible_env = FakeVarsModule('ansible_env')
            self.ansible_env.HOME = '/home/test_user'
            self.ansible_env.USER = 'test_user'

    templar = Templar(loader=DataLoader(), variables=FakeVars())

    assert(listify_lookup_plugin_terms('{{ ansible_env.USER }}', templar, None) == ['test_user'])

# Generated at 2022-06-13 16:29:00.436895
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.vars import VariableManager

    assert listify_lookup_plugin_terms("{{ foo }}, {{ bar }}", templar=Templar(VariableManager()), loader=None, fail_on_undefined=False) == ['{{ foo }}', '{{ bar }}']

    # travis.yml uses this feature
    assert listify_lookup_plugin_terms("[ '{{ foo }}', '{{ bar }}' ]", templar=Templar(VariableManager()), loader=None, fail_on_undefined=False) == ['{{ foo }}', '{{ bar }}']

    # test with converting bare variables

# Generated at 2022-06-13 16:29:10.157003
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    import os
    import sys
    import tempfile

    sys.path.append(os.environ["HOME"] + "/.ansible/plugins/lookup")

    from lookup_plugins.file import LookupModule
    from ansible.playbook.play_context import PlayContext

    def _get_tmp_path(content):
        ''' return temporary file path, which contains specified content '''
        fd, path = tempfile.mkstemp()
        os.write(fd, content)
        os.close(fd)
        return path


# Generated at 2022-06-13 16:29:20.314574
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    my_vars = dict(a='b')
    my_loader = None

    templar = Templar(loader=my_loader, variables=my_vars)

    assert listify_lookup_plugin_terms(terms='c', templar=templar, loader=my_loader) == ['c']
    assert listify_lookup_plugin_terms(terms=['c'], templar=templar, loader=my_loader) == ['c']
    assert listify_lookup_plugin_terms(terms=u'c', templar=templar, loader=my_loader) == ['c']
    assert listify_lookup_plugin_terms(terms=u'{{a}}', templar=templar, loader=my_loader) == ['b']
   

# Generated at 2022-06-13 16:29:30.332156
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar

    loader = DataLoader()
    templar = Templar(loader=loader)

    def _deunicode(x):
        '''Recursively convert unicode in lists and dicts to strings in python2'''
        if isinstance(x, unicode):
            return x.encode('utf-8')
        elif isinstance(x, list):
            return [_deunicode(y) for y in x]
        elif isinstance(x, dict):
            return {_deunicode(key):_deunicode(val) for key,val in x.items()}
        else:
            return x

    from ansible.module_utils import six

    # These strings are unicode in py2, str in py

# Generated at 2022-06-13 16:29:35.749167
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.playbook.play import Play
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    play_context = dict(
        basedir='/path/to/ansible/playbooks',
    )

# Generated at 2022-06-13 16:29:46.990563
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    dumper = AnsibleDumper(width=9999, default_flow_style=False)

    templar = Templar(loader=None, variables={}, fail_on_undefined=False)
    assert listify_lookup_plugin_terms(['{{ foo }}', '{{ bar }}'], templar, loader=None) == ['{{ foo }}', '{{ bar }}']

    templar = Templar(loader=None, variables={}, fail_on_undefined=True)

# Generated at 2022-06-13 16:30:02.144987
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    # Check with a string argument
    term = "{{ var }}"
    assert listify_lookup_plugin_terms(term, None, None) == [term]
    term = "{{ var }}"
    assert listify_lookup_plugin_terms(term, object(), object()) == [term]

    # Check with a list argument
    term = ["{{ var }}", "{{ var2 }}", "{{ var3 }}"]
    assert listify_lookup_plugin_terms(term, None, None) == term
    term = ["{{ var }}", "{{ var2 }}", "{{ var3 }}"]
    assert listify_lookup_plugin_terms(term, object(), object()) == term

    # Check with a None argument
    term = None
    assert listify_lookup_plugin_terms(term, None, None) == [term]

# Generated at 2022-06-13 16:30:10.623664
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible import constants as C
    import ansible.parsing.dataloader
    from ansible.template import Templar

    parser = ansible.parsing.dataloader.DataLoader()
    t = Templar(parser=parser, variables={}, loader=parser)

    # test convert_bare
    terms = '{{ foo }}'
    result = listify_lookup_plugin_terms(terms, t, parser, convert_bare=True)
    assert result == ['foo'], result

    # test trimming
    terms = '   foo   '
    result = listify_lookup_plugin_terms(terms, t, parser, convert_bare=True)
    assert result == ['foo'], result

    # test string to list
    terms = 'foo'

# Generated at 2022-06-13 16:30:18.985130
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    """
    This function is easier to test than it looks.  The conversion of types
    is performed by the Templar so we simply need to make sure the correct
    code path is chosen.
    """
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.yaml.loader import AnsibleLoader

    templar = DummyTemplar()

    loader = AnsibleLoader(None, None, None)

    #
    # Test a string and ensure it is considered a single term
    #
    fake_string = 'we are now at least 2 terms'
    ret = listify_lookup_plugin_terms(fake_string, templar, loader, True, False)
    assert ret == [fake_string]

    #
    # Test a list of strings, no changes should be made

# Generated at 2022-06-13 16:30:30.452528
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    variable_manager = VariableManager()
    variable_manager.extra_vars = {'test_var': 'foo'}
    loader = variable_manager.get_vars_loader()
    templar = Templar(loader=loader, variables=variable_manager.get_vars())

    assert listify_lookup_plugin_terms('{{test_var}}', templar, loader) == ['foo']
    assert listify_lookup_plugin_terms('{{test_var}}', templar, loader) == templar.template('{{test_var}}', convert_bare=False, fail_on_undefined=True)
    assert listify_

# Generated at 2022-06-13 16:30:41.714957
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager()
    templar = Templar(loader=loader, variables=variable_manager)

    data = [
        {"a": 1, "b": 2},
        {"a": 3, "b": 4, "c": 5},
    ]
    terms_string = "{{ lookup('someplugin', args='foobar') }}"
    terms_dict = {"a": "{{ lookup('someplugin', args='foobar') }}", "b": "BAZ"}

# Generated at 2022-06-13 16:30:52.688350
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    import copy

    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.template import Templar

    class TestVarsModule: pass
    vars_mock = TestVarsModule()
    vars_mock.host_vars = {}
    vars_mock.group_vars = {}

    templar = Templar(loader=None, variables=vars_mock)


# Generated at 2022-06-13 16:30:58.713370
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    dataloader = DataLoader()
    variable_manager = VariableManager()
    inventory = Host(name="foobar")
    variable_manager.set_inventory(inventory)
    host = Host(name='inventory_hostname')
    host.vars = dict(
        foo=1,
        bar=2,
    )
    variable_manager.set_host_variable(host=host, varname='inventory_hostname', value=host.name)
    group = Group('all')
    group.add_host(host)
    variable_manager.set_inventory(inventory)
   

# Generated at 2022-06-13 16:31:08.941728
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing import DataLoader

    loader = DataLoader()
    templar = Templar(loader=loader)

    # test strings
    assert listify_lookup_plugin_terms('foo', templar, loader) == ['foo']
    assert listify_lookup_plugin_terms('bing', templar, loader) == ['bing']
    assert listify_lookup_plugin_terms('foo bar', templar, loader) == ['foo bar']
    assert listify_lookup_plugin_terms('foo bar bing', templar, loader) == ['foo bar bing']

    # test lists
    assert listify_lookup_plugin_terms(['foo', 'bar'], templar, loader) == ['foo', 'bar']
    assert listify_lookup_

# Generated at 2022-06-13 16:31:18.511423
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible import constants as C
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.lookup import LookupBase
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    C.DEFAULT_HASH_BEHAVIOUR = "merge"

    templar = Templar(loader=None, variables=VariableManager())
    lookup1 = LookupBase()

    #############################
    # Test string terms
    #############################
    terms = "List of strings"
    result = listify_lookup_plugin_terms(terms, templar, None)
    assert result == ['List of strings']

    #############################
    # Test string terms
    #############################
    terms = "String with {{ b }} style vars"

# Generated at 2022-06-13 16:31:28.442697
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import merge_hash

    yaml_data = """a: 1
b:
    - 2
    - 3
    - "4"
c:
    - {key: 5}
d:
    - 6
    - 7
    -
        - 8
    - "9"
e:
    - 10
    - 11
    -
        - 12
        - 13"""
    variable_manager = VariableManager()
    variable_manager.extra_vars = {}
    variable_manager.options_vars = {}
    vault_secrets = {}
    loader = DataLoader()

# Generated at 2022-06-13 16:31:50.355332
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.six import string_types

    def test_assert_type(terms, expected_type):
        assert isinstance(terms, expected_type)

    # Init dicts for test data

# Generated at 2022-06-13 16:31:58.450669
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    class MyLoader(object):
        def get_basedir(self, x):
            return 'loaderdir'

    templar = Templar(loader=MyLoader())

    # Invalid
    assert listify_lookup_plugin_terms(None, templar, templar.loader, convert_bare=False) == []
    assert listify_lookup_plugin_terms('', templar, templar.loader, convert_bare=False) == []

    # Bare vars
    assert listify_lookup_plugin_terms('1', templar, templar.loader, convert_bare=False) == ['1']
    assert listify_lookup_plugin_terms('{{1}}', templar, templar.loader, convert_bare=False) == ['{{1}}']
   

# Generated at 2022-06-13 16:32:10.614974
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.template import Templar

    loader = DictDataLoader({})
    templar = Templar(loader=loader)

    # first verify the AnsibleBaseYAMLObject gets converted
    data = AnsibleBaseYAMLObject('a')
    result = listify_lookup_plugin_terms(terms=data, templar=templar, loader=loader)
    assert isinstance(result, list)
    assert result == ['a']

    data = [AnsibleBaseYAMLObject('a')]
    result = listify_lookup_plugin_terms(terms=data, templar=templar, loader=loader)
    assert isinstance(result, list)
    assert result == ['a']

    # then verify

# Generated at 2022-06-13 16:32:13.625921
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    assert(listify_lookup_plugin_terms(1,[2])   == [1])
    assert(listify_lookup_plugin_terms([1],[2]) == [1])
    assert(listify_lookup_plugin_terms('1',[2]) == ['1'])
    assert(listify_lookup_plugin_terms('[1]',[2]) == [[1]])

# Generated at 2022-06-13 16:32:22.636092
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    loader = DictDataLoader({
        "template_name.j2": "{{ a }}",
        u"template_name_u.j2": "{{ b }}",
        "template_list.j2": "{% for x in list %}{{ x }},{% endfor %}",
        "template_var.j2": "{{ foo }}"
    })

    myvars = {
        'a': 1,
        'b': 2,
        'list': [2, 3, 4],
        'foo': 'bar'
    }

    templar = Templar(loader=loader, variables=myvars)


# Generated at 2022-06-13 16:32:28.633365
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    import ansible.errors
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    terms = "{{ foo }}"
    templar = Templar(loader=DataLoader(), variables=dict(foo=1))
    assert listify_lookup_plugin_terms(terms, templar, templar.loader) == [1]

    terms = "{{ foo | to_json }}"
    templar = Templar(loader=DataLoader(), variables=dict(foo=[1,2,3]))
    assert listify_lookup_plugin_terms(terms, templar, templar.loader) == [[1,2,3]]

    terms = "{{ foo }}"
    templar = Templar(loader=DataLoader(), variables=dict(foo=[1,2,3]))


# Generated at 2022-06-13 16:32:39.215814
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.vars import VariableManager

    v = VariableManager()
    t = Templar(loader=None, variables=v)
    assert listify_lookup_plugin_terms('hello', t, None) == ['hello']
    assert listify_lookup_plugin_terms('hello,world', t, None) == ['hello', 'world']
    assert listify_lookup_plugin_terms(['hello,world'], t, None) == ['hello,world']
    assert listify_lookup_plugin_terms('127.0.0.1, {{foo}}', t, None) == ['127.0.0.1', '{{foo}}']

    v.set_variable('foo', 'bar')

# Generated at 2022-06-13 16:32:46.100028
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    terms = listify_lookup_plugin_terms(['a', 'b', 'c'], Templar({}), None)
    assert type(terms) == list

    terms = listify_lookup_plugin_terms('a, b, c', Templar({}), None)
    assert type(terms) == list

    terms = listify_lookup_plugin_terms('a', Templar({}), None)
    assert type(terms) == list

# Generated at 2022-06-13 16:32:55.843859
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    '''
    Test listify_lookup_plugin_terms
    '''
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook import Playbook

    variable_manager = VariableManager()
    loader = DataLoader()

# Generated at 2022-06-13 16:33:05.032786
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager()

    templar = Templar(loader=loader, variable_manager=variable_manager)

    # Test to ensure that 'asdf' is returned as ['asdf']
    terms = 'asdf'
    result = listify_lookup_plugin_terms(terms, templar, loader, fail_on_undefined=True, convert_bare=False)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] == 'asdf'

    # Test to ensure that 'asdf' is returned as ['asdf'] with convert_bare
    terms = 'asdf'
    result

# Generated at 2022-06-13 16:33:40.940658
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleSequence
    from ansible.template import Templar
    from ansible.utils.vars import combine_vars
    from ansible.vars.manager import VariableManager

    templar = Templar(loader=None, variables=combine_vars(loader=None, variables=dict()))
    templar._available_variables = VariableManager()

    assert listify_lookup_plugin_terms('foo', templar, None) == ['foo']
    assert listify_lookup_plugin_terms(' foo ', templar, None) == ['foo']

    assert listify_lookup_plugin_terms(['foo', ' bar '], templar, None) == ['foo', ' bar ']
    assert listify_lookup_plugin_terms

# Generated at 2022-06-13 16:33:49.176358
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleUnicode

    my_loader = DataLoader()
    my_inventory = InventoryManager(loader=my_loader, sources='localhost,')
    my_variable_manager = VariableManager(loader=my_loader, inventory=my_inventory)
    my_templar = Templar(loader=my_loader, variables=my_variable_manager)

    assert(listify_lookup_plugin_terms('hello', my_templar, my_loader) == ['hello'])

# Generated at 2022-06-13 16:33:59.258377
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    # Test listify_lookup_plugin_terms with string types
    assert listify_lookup_plugin_terms('a', fail_on_undefined=True, convert_bare=False) == ['a']
    assert listify_lookup_plugin_terms('a', fail_on_undefined=True, convert_bare=True) == [u'a']

    # Test listify_lookup_plugin_terms with a non-string, non-iterable type
    assert listify_lookup_plugin_terms(1, fail_on_undefined=True, convert_bare=False) == [1]

    # Test listify_lookup_plugin_terms with a list, string and integer
    assert listify_lookup_plugin_terms([1, 2, 'a'], fail_on_undefined=True, convert_bare=False)

# Generated at 2022-06-13 16:34:02.535535
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleMapping, AnsibleSequence
    from ansible.vars.manager import VariableManager

    my_vars = dict(
        a_string="foo",
        a_list=['a', 'b', 'c'],
    )

    variable_manager = VariableManager()
    variable_manager.set_host_variable("127.0.0.1", my_vars)
    loader = None

    # listify_lookup_plugin_terms should return a list with one AnsibleUnicode when given an AnsibleUnicode
    test_value = AnsibleUnicode("{{ a_string }}")

# Generated at 2022-06-13 16:34:12.186075
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    templar = Templar(loader=DataLoader())

    assert listify_lookup_plugin_terms('some string', templar, DataLoader()) == ['some string']
    assert listify_lookup_plugin_terms(['some', 'string'], templar, DataLoader()) == [['some', 'string']]
    assert listify_lookup_plugin_terms(['some', '{{foo}}'], templar, DataLoader(), fail_on_undefined=False) == ['some', '{{foo}}']
    assert listify_lookup_plugin_terms(['some', '{{foo}}'], templar, DataLoader(), convert_bare=True) == ['some', '{{foo}}']
    assert listify_

# Generated at 2022-06-13 16:34:17.701518
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from units.mock.loader import DictDataLoader

    loader = DictDataLoader({})
    templar = Templar(loader=loader)
    result = listify_lookup_plugin_terms('test', templar, loader, convert_bare=True)
    assert(result == ['test'])

    result = listify_lookup_plugin_terms('test1,test2', templar, loader, convert_bare=True)
    assert(result == ['test1', 'test2'])

    result = listify_lookup_plugin_terms(['test1', 'test2'], templar, loader, convert_bare=True)
    assert(result == ['test1', 'test2'])


# Generated at 2022-06-13 16:34:29.408299
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    # Test 1: Test with list
    # Test 2: Test with comma separated string
    # Test 3: Test with single string
    contents = '''
    a: 1
    b: 2
    c:
      - 3
      - 4
      - 5
    d: 6
    '''

    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import merge_hash
    from ansible.vars.manager import VariableManager

    def dummy_get_basedir(*args, **kwargs):
        return '/'

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager._fact_cache = dict()
    variable_manager.extra_vars = dict()
    variable_manager.options_vars = dict()



# Generated at 2022-06-13 16:34:38.770009
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    import ansible.template.safe_eval

    # test safe_eval
    assert(ansible.template.safe_eval.safe_eval("foo", locals=locals()) == "foo")
    assert(ansible.template.safe_eval.safe_eval("a+b", locals=locals()) == 3)
    assert(ansible.template.safe_eval.safe_eval("a+b+c", locals=locals()) == 9)

    # test listify_lookup_plugin_terms
    test_templar = DummyTemplar()
    test_loader = DummyLoader()

# Generated at 2022-06-13 16:34:48.877755
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleUnicode

    # Plugins may return a string or list of strings
    terms = ['hello', 'world']
    results = listify_lookup_plugin_terms(terms, Templar({}), None)
    assert results == ['hello', 'world']

    # The templates plugin may return a string or list of strings
    terms = '{{ hello }} world'
    results = listify_lookup_plugin_terms(terms, Templar({'hello': 'hello'}), None)
    assert results == ['hello world']

    # The file lookup plugin may return a string or list of strings
    terms = '{{ test_dir }}/myhosts'

# Generated at 2022-06-13 16:34:55.610754
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    my_vars = dict(
        test_var="foo.bar"
    )
    loader = DataLoader()
    templar = Templar(loader=loader, variables=my_vars)

    # test string types
    res = listify_lookup_plugin_terms("{{ test_var }}", templar, loader, fail_on_undefined=True, convert_bare=False)
    assert res == ['foo.bar']

    # test non string types
    res = listify_lookup_plugin_terms(["{{ test_var }}"], templar, loader, fail_on_undefined=True, convert_bare=False)
    assert res == ['foo.bar']

    # test list with list inside
   