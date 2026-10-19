

# Generated at 2022-06-13 16:25:12.303199
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    from six import text_type

    # Below is a list of tuples. Each tuple is a set of arguments for the function
    # listify_lookup_plugin_terms. Each tuple has two elements. The first element
    # is a list of arguments that will be passed to the function. The second element
    # is the expected result of the function.

# Generated at 2022-06-13 16:25:21.674979
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    import unittest2 as unittest
    from ansible.errors import AnsibleError
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    class TestJinja2Templar(Templar):
        '''
        Subclass of the Templar class which, for our purposes here,
        simply returns the template string rather than rendering it
        '''
        def template(self, data, preserve_trailing_newlines=True,
                     escape_backslashes=True, fail_on_undefined=True,
                     convert_bare=False, ignore_errors=False,
                     overrides=None, **kwargs):
            return data


# Generated at 2022-06-13 16:25:28.433548
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.set_vault_password('ansible')
    templar = Templar(loader=loader, variable_manager=variable_manager)

    terms = listify_lookup_plugin_terms('{{ foo }}', templar, loader)
    assert terms == ['{{ foo }}']

    terms = listify_lookup_plugin_terms(['{{ foo }}'], templar, loader)
    assert terms == ['{{ foo }}']

    terms = listify_lookup_plugin_terms('{{ foo }}, {{ foo2}}', templar, loader)

# Generated at 2022-06-13 16:25:38.737212
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    dl = DataLoader()
    t  = Templar(dl)

    assert listify_lookup_plugin_terms(["one", "two"], t, dl, fail_on_undefined=True) == ["one", "two"]
    assert listify_lookup_plugin_terms("one two", t, dl, fail_on_undefined=True) == ["one", "two"]
    assert listify_lookup_plugin_terms(["one two"], t, dl, fail_on_undefined=True) == ["one", "two"]
    assert listify_lookup_plugin_terms("one", t, dl, fail_on_undefined=True) == ["one"]
    assert listify_lookup_

# Generated at 2022-06-13 16:25:44.990589
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.six import PY3
    try:
        from ansible.playbook.play_context import PlayContext
        from ansible.template import Templar
        from ansible.vars import VariableManager
        from ansible.parsing.dataloader import DataLoader
    except ImportError:
        from ansible.playbook.play_context import PlayContext
        from ansible.template import Templar
        from ansible.vars import VariableManager
        from ansible.parsing.dataloader import DataLoader

    if not PY3:
        import ansible.module_utils.six.moves.builtins as __builtin__
    else:
        import builtins as __builtin__

    variable_manager = VariableManager()
    loader = DataLoader()

# Generated at 2022-06-13 16:25:56.628427
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    
    class fake_templar:
        def template(self, terms, fail_on_undefined=True):
            return terms

    class fake_loader:
        pass
    
    tf = fake_templar()
    fl = fake_loader()
    foo = "foo"
    bar = ["bar", "baz", "bam", "bap"]
    baz = (1, 2, 3, 4)
    
    # non-iterable string which should return a list
    ret = listify_lookup_plugin_terms(foo, tf, fl)
    assert isinstance(ret, list)
    assert len(ret) == 1
    assert ret[0] == foo
    
    # list which should return a list
    ret = listify_lookup_plugin_terms(bar, tf, fl)

# Generated at 2022-06-13 16:26:03.521356
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    try:
        from jinja2 import Environment
    except ImportError:
        print("SKIP: unable to import jinja2 (required for this test)")
        import sys
        sys.exit(0)
    from ansible.template import Templar

    env = Environment()
    templar = Templar(loader=None, variables={})

    assert listify_lookup_plugin_terms('', templar, loader=None) == ['']
    assert listify_lookup_plugin_terms(['',''], templar, loader=None) == ['', '']
    assert listify_lookup_plugin_terms('foo', templar, loader=None) == ['foo']
    assert listify_lookup_plugin_terms('foo bar', templar, loader=None) == ['foo', 'bar']
    assert list

# Generated at 2022-06-13 16:26:13.480682
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib


# Generated at 2022-06-13 16:26:21.641419
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.extra_vars = {'a_var': 'var_value'}
    variable_manager.set_available_variables(loader.load_from_file('tests/fixtures-templating/test_listify_lookup_plugin_terms.json'))
    variable_manager.update_vars({'hostvars': {'hostname': variable_manager._hostvars}})
    templar = Templar(loader, variable_manager)


# Generated at 2022-06-13 16:26:29.155605
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.yaml.objects import AnsibleUnicode

    assert listify_lookup_plugin_terms(['foo', 2, 3], 'templar', 'loader') == [u'foo', 2, 3]
    assert listify_lookup_plugin_terms('foo', 'templar', 'loader') == [u'foo']
    assert listify_lookup_plugin_terms(AnsibleUnicode('foo'), 'templar', 'loader') == [u'foo']

# Generated at 2022-06-13 16:26:38.693450
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar     # imports here due to ut import order issues
    templar = Templar(loader=None)
    terms = "[u'foo', 'bar']"
    terms = listify_lookup_plugin_terms(terms, templar, None)
    assert isinstance(terms, list)
    assert len(terms) == 2
    assert isinstance(terms[0], string_types)
    assert isinstance(terms[1], string_types)
    terms = u"foo"
    terms = listify_lookup_plugin_terms(terms, templar, None)
    assert isinstance(terms, list)
    assert len(terms) == 1
    assert isinstance(terms[0], string_types)

# Generated at 2022-06-13 16:26:47.177490
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.six import PY3
    from ansible.parsing.vault import VaultLib
    from ansible.template import Templar
    from ansible.playbook.play_context import PlayContext

    test_vars = {
        'val1': 'value1',
        'val2': 'value2',
        'val3': 'value3'
    }
    test_loader = DictDataLoader(test_vars)

    test_passwords = {
        'vault_password1': 'pass1',
    }
    test_vault = VaultLib(passwords=test_passwords)

    class TestInventory(object):
        def __init__(self, *args, **kwargs):
            pass

    test_context = PlayContext()


# Generated at 2022-06-13 16:26:57.862778
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    templar = Templar(loader=None, variables=VariableManager())

    ascii_str = "Hello, world."
    utf8_str = "\xc3\xbcnic\xc3\xb8de."

    ascii_list = ['Hello, world.']
    utf8_list = ["\xc3\xbcnic\xc3\xb8de."]
    utf8_list_str = "['\\xc3\\xbcnic\\xc3\\xb8de.']"

    ascii_list_str = "['Hello, world.']"

    play_context = PlayContext()


# Generated at 2022-06-13 16:27:06.910327
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template.safe_eval import safe_eval
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    terms = u'{{ lookup("file", "listify.txt") }}'
    temp_file = "listify.txt"
    terms_data = "{ 'a': 1, 'b': 2, 'c': 3 }"
    temp_file_path = "/tmp/%s" % temp_file

    # Create tmp file for the test
    open(temp_file_path, "w").write(terms_data)

    loader

# Generated at 2022-06-13 16:27:17.527084
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.module_utils.common.collections import is_sequence

    # We need a real templar object so that the tests will behave correctly
    # when variables are involved.  However, we don't want any of our normal
    # behavior to be executed, so we will override its methods to do nothing
    # except return an appropriate value.
    from ansible.template import Templar
    class EmptyTemplar(Templar):
        def __init__(self):
            self._available_variables = dict()
            self._hostvars = dict()

        def set_available_variables(self, variables):
            self._available_variables = variables

        def set_host_variables(self, variables):
            self._hostvars = variables


# Generated at 2022-06-13 16:27:27.425379
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    try:
        from ansible import context
        from ansible.template import Templar
        from ansible.vars.unsafe_proxy import UnsafeProxy, wrap_var
        from ansible.parsing.dataloader import DataLoader
    except ImportError:
        # Ansible >= 2.4
        from ansible.utils.unsafe_proxy import UnsafeProxy, wrap_var
        from ansible.template import Templar
        from ansible.vars import VariableManager
        from ansible.parsing.vault import VaultLib
        from ansible.parsing.dataloader import DataLoader

    from ansible.errors import AnsibleError

    from ansible.parsing.yaml.objects import AnsibleSequence

    loader = DataLoader()
    templar = Templar(loader=loader)


# Generated at 2022-06-13 16:27:36.519475
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    templar = Templar(loader=None)

    # This is a basic unit test
    # It does not cover all edge cases

    # single term string
    assert listify_lookup_plugin_terms('file1', templar, None) == ['file1']

    # multiple term string
    assert listify_lookup_plugin_terms('file1,file2', templar, None) == ['file1', 'file2']

    # single term list
    assert listify_lookup_plugin_terms(['file1'], templar, None) == ['file1']

    # multiple term list
    assert listify_lookup_plugin_terms(['file1', 'file2'], templar, None) == ['file1', 'file2']

    # test with templating


# Generated at 2022-06-13 16:27:47.143727
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    '''
    Test the listify_lookup_plugin_terms function.
    '''
    from ansible.template import Templar

    class FakeVarsModule(object):
        def get_vars(self, loader, path, entities):
            return {}

    class FakeLoaderModule(object):
        def get_basedir(self, path):
            return '/'

    templar = Templar(loader=FakeLoaderModule(), variables=FakeVarsModule())

    assert listify_lookup_plugin_terms('string', templar, FakeLoaderModule()) == ['string']
    assert listify_lookup_plugin_terms(['string'], templar, FakeLoaderModule()) == ['string']
    assert listify_lookup_plugin_terms(['string', 'string'], templar, FakeLoaderModule()) == ['string', 'string']

# Generated at 2022-06-13 16:27:57.808845
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.templating import Templar

    class FakeVarsModule(object):
        def __init__(self, templar):
            self.templar = templar

        def get_vars(self, loader, play, host, task):
            return dict(name='steve')


# Generated at 2022-06-13 16:28:08.378500
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleUnicode

    fake_loader = dict(
        variable_manager=dict(
            extra_vars=dict(),
        ),
    )
    templar = Templar(fake_loader)

    # Python 2's unicode objects are broken, so we need to use AnsibleUnicode
    # to get a string-like object that Ansible can listify.
    assert listify_lookup_plugin_terms(
        AnsibleUnicode('a'), templar, fake_loader) == ['a']


# Generated at 2022-06-13 16:28:21.851752
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    vault_secrets = VaultLib([])
    variable_manager = VariableManager()
    templar = Templar(loader=loader, variables=variable_manager, vault_secrets=vault_secrets)

    # listify_lookup_plugin_terms takes list as argument
    assert listify_lookup_plugin_terms([u'hi'], templar, loader) == [u'hi']
    assert listify_lookup_plugin_terms([u'hi', u'there'], templar, loader) == [u'hi', u'there']

    # listify_

# Generated at 2022-06-13 16:28:29.164877
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    # test that listify_lookup_plugin_terms is an Iterable
    terms = listify_lookup_plugin_terms('xyz', 'templar', 'loader')
    assert(isinstance(terms, Iterable))
    # test that the listify_lookup_plugin_terms returns a list with 1 element
    terms = listify_lookup_plugin_terms('xyz, ', 'templar', 'loader')
    assert(len(terms) == 1)
    # test that listify_lookup_plugin_terms returns a list with two elements
    terms = listify_lookup_plugin_terms('xyz, 123', 'templar', 'loader')
    assert(len(terms) == 2)

# Generated at 2022-06-13 16:28:38.649363
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    '''
    Validate the listify_lookup_plugin_terms() returns the expected values.
    '''

    class Templar(object):
        '''
        Fake class for templar
        '''

        @staticmethod
        def template(data, fail_on_undefined=False, convert_bare=False):
            '''
            Stub method for templar
            '''
            return data

    assert listify_lookup_plugin_terms(['[1,2,3]'], Templar, None, convert_bare=True) == [1,2,3]
    assert listify_lookup_plugin_terms('[1,2,3]', Templar, None, convert_bare=True) == [1,2,3]

# Generated at 2022-06-13 16:28:47.257262
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.common.collections import is_sequence
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode, AnsibleUnicode
    arr = [AnsibleUnicode('foo'), AnsibleUnicode('bar'), AnsibleUnicode('baz')]
    assert is_sequence(arr)
    templar = Templar(loader=None)
    assert listify_lookup_plugin_terms('{{ arr }}', templar, loader=None) == arr
    assert listify_lookup_plugin_terms(['{{ item }}'], templar, loader=None) == ['foo', 'bar', 'baz']

# Generated at 2022-06-13 16:28:52.198692
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    import ansible.errors as errors

    from ansible.template import Templar

    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleSequence

    class MockVars:

        def get_vars(self, play, host, task, wrap_values=True):
            return dict(single="single", list=["list", "of", "items"], dict=dict(a="a"))

        def get_hostvars(self, host):
            return dict(single="single", list=["list", "of", "items"], dict=dict(a="a"))

        def get_vars_files(self, play):
            return "/dev/null"

    class MockOptions:
        def __init__(self):
            self.tags = None
            self.skip_tags = None

# Generated at 2022-06-13 16:29:01.202464
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    #Test converting a dictionary to a list
    class FakeModule():
        def __init__(self):
            self.params = []
        def fail_json(self, **kwargs):
            pass
    class FakeTemplar():
        def __init__(self, module):
            self.module = module
        def template(self, terms, fail_on_undefined=True, convert_bare=False):
            return ['Hello', 'World']
    class FakeLoader():
        pass
    module = FakeModule()
    templar = FakeTemplar(module)
    loader = FakeLoader()
    listified_terms = listify_lookup_plugin_terms({'Hello': 'World'}, templar, loader)
    assert listified_terms == ['Hello', 'World']

# Generated at 2022-06-13 16:29:05.019568
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    assert listify_lookup_plugin_terms([["a","b","c"],["1","2","3"]],None, None) == [["a","b","c"],["1","2","3"]]

# Generated at 2022-06-13 16:29:12.194532
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    class Template(object):
        def __init__(self, value):
            self.value = value

        def template(self, value, **kwargs):
            return self.value

    class LookupModule(object):
        def __init__(self, **kwargs):
            self.templar = Template('')

    class TestException(Exception):
        pass

    class Term(object):
        pass

    terms = {
      'list': [Term(), Term()],
      'tuple': (Term(), Term()),
      'set': set([Term(), Term()]),
      'dir': {'a': Term(), 'b': Term()},
      'string': 'foo',
      'term': Term(),
      'empty': None
    }


# Generated at 2022-06-13 16:29:17.453418
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    variable_manager = VariableManager()
    loader = DataLoader()

    variable_manager.set_nonpersistent_facts(dict(foo='bar', baz='qux'))
    templar = Templar(loader=loader, variables=variable_manager)

    assert listify_lookup_plugin_terms(2, templar, loader) == ['2']
    assert listify_lookup_plugin_terms([1, 2], templar, loader) == [1, 2]
    assert listify_lookup_plugin_terms([1, '{{foo}}'], templar, loader) == [1, 'bar']

# Generated at 2022-06-13 16:29:29.632222
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.template import AnsibleEnvironment
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext

    variable_manager = VariableManager()
    loader = DataLoader()
    play_context = PlayContext()
    inventory = variable_manager.get_inventory()

    templar = Templar(loader=loader, variables=variable_manager,
                      shared_loader_obj=loader, environment=AnsibleEnvironment(loader))

    assert listify_lookup_plugin_terms('foo', templar, loader, fail_on_undefined=True, convert_bare=False) == ['foo']

# Generated at 2022-06-13 16:29:42.265323
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.dataloader import DataLoader

    dl = DataLoader()
    assert listify_lookup_plugin_terms('foo', dl) == ['foo']
    assert listify_lookup_plugin_terms(['foo'], dl) == ['foo']
    assert listify_lookup_plugin_terms(u'foo', dl) == ['foo']

# Generated at 2022-06-13 16:29:51.858182
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    # Test regular string input
    terms = 'foobar'
    result = listify_lookup_plugin_terms(terms, Templar({}), None, False)
    assert result == ['foobar']

    # Test string input with commas
    terms = 'foo,bar'
    result = listify_lookup_plugin_terms(terms, Templar({}), None, False)
    assert result == ['foo', 'bar']

    # Test string input with commas and spaces
    terms = 'foo, bar'
    result = listify_lookup_plugin_terms(terms, Templar({}), None, False)
    assert result == ['foo', 'bar']

    # Test string input with commas and quotes
    terms = 'foo, "bar"'

# Generated at 2022-06-13 16:30:01.089070
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.plugins.loader import lookup_loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    from ansible.vars import VariableManager

    test_strings = ["{{ foo }}", "{{ foo }}, {{ bar }}", "{{ foo }}, {{ bar }}, {{ bam }}",
                    "{{ foo }},{{ bar }},{{ bam }}", "{{ foo }},{{bar}},{{bam}}"]

    test_dict = {'foo': 'val1',
                 'bar': 'val2',
                 'bam': 'val3'}


# Generated at 2022-06-13 16:30:08.548391
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.errors import AnsibleUndefinedVariable
    from ansible.template.safe_eval import safe_eval

    from ansible.template import Templar

    assert listify_lookup_plugin_terms(None, None, None) == [None]
    assert listify_lookup_plugin_terms([None], None, None) == [None]

    templar = Templar(loader=None)

    # test with bare vars disabled
    assert listify_lookup_plugin_terms('1', templar, None, convert_bare=False) == ['1']
    assert listify_lookup_plugin_terms(['1'], templar, None) == ['1']
    assert listify_lookup_plugin_terms(['1', '2'], templar, None) == ['1', '2']

    # test with

# Generated at 2022-06-13 16:30:15.898836
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    templar = Templar(loader=None)

    try:
        listify_lookup_plugin_terms(None, templar)
    except ValueError:
        pass
    else:
        raise AssertionError('failed to raise ValueError')

    terms = listify_lookup_plugin_terms('string', templar)
    assert terms == ['string']

    terms = listify_lookup_plugin_terms(['string1', 'string2'], templar)
    assert terms == ['string1', 'string2']

# Generated at 2022-06-13 16:30:27.805984
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    loader = DataLoader()
    variable_manager.extra_vars = {'var1': 'foo', 'var2': 'bar'}
    variable_manager.set_nonpersistent_facts({'ansible_version': {'full': '0.9.6dev'}})

    # Initialize Templar
    templar = Templar(loader=loader, variables=variable_manager)

    # Single string argument
    assert listify_lookup_plugin_terms('foo', templar, loader) == ['foo']
    # Single non-string argument
    assert listify_lookup_plugin_terms(['foo'], templar, loader)

# Generated at 2022-06-13 16:30:36.710911
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()
    templar = Templar(loader=loader, variables=variable_manager)

    assert listify_lookup_plugin_terms(["{{ var }}", "{{ other_var }}"], templar, loader, fail_on_undefined=False) == ["", ""]
    assert listify_lookup_plugin_terms(["{{ var }}", "{{ other_var }}"], templar, loader, convert_bare=True, fail_on_undefined=False) == ["{{ var }}", "{{ other_var }}"]

# Generated at 2022-06-13 16:30:47.570285
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.yaml.objects import AnsibleMapping
    t = Templar(loader=None)

    # test case of string with no variables
    var = "item_1"
    assert listify_lookup_plugin_terms(var, t, None) == ["item_1"]

    # test case of dict with no variables
    var = dict(item_1=1, item_2=2)
    assert listify_lookup_plugin_terms(var, t, None) == var

    # test case of list with no variables
    var = ["item_1", "item_2"]
    assert listify_lookup_plugin_terms(var, t, None) == var

    # test case of string with bare

# Generated at 2022-06-13 16:30:56.256687
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    # Make a templar
    loader = None
    variables = dict(
        foo="bar",
        biz=dict(
            baz="bax"
        ),
        x=[1, 2, 3]
    )
    shared_loader_obj = None
    templar = Templar(loader=loader, variables=variables)

    terms = listify_lookup_plugin_terms("{{ foo }}", templar, loader)
    assert terms == ["bar"]

    terms = listify_lookup_plugin_terms(dict(key="{{ foo }}"), templar, loader)
    assert terms == [dict(key="bar")]

    terms = listify_lookup_plugin_terms(["{{ foo }}", "{{ biz.baz }}"], templar, loader)
   

# Generated at 2022-06-13 16:31:07.982091
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    # Setup tests:
    #  - listify_lookup_plugin_terms uses the Templar class (for template)
    #    and VariableManager (to construct Templar)
    #  - For this test, VariableManager and Templar will be "fake"
    #  - We create a "fake" inventory to use in the "fake" VariableManager
    #  - The "fake" inventory has the variable 'var_b' set to ['b1', 'b2']


# Generated at 2022-06-13 16:31:29.784815
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    class FakeTemplar(object):
        def __init__(self, value):
            self.value = value

        def template(self, terms, convert_bare=False, fail_on_undefined=True):
            return self.value

    # this test will raise errors on failure
    t = FakeTemplar("value1")
    assert listify_lookup_plugin_terms("value1", t, None) == ["value1"]
    assert listify_lookup_plugin_terms("value2", t, None) == ["value2"]
    t = FakeTemplar("value1,value2")
    assert listify_lookup_plugin_terms("value1,value2", t, None) == ["value1", "value2"]
    assert listify_lookup_plugin_terms("value2,value2", t, None)

# Generated at 2022-06-13 16:31:35.937036
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.template import Templar

    secret = VaultSecret(identity='dummy', password='dummy', salt='dummy')
    templar = Templar(loader=None, variables=dict(foo='bar'))
    lookup_plugin_terms = '{{ foo }}'
    ret = listify_lookup_plugin_terms(lookup_plugin_terms, templar, loader=None, convert_bare=False)
    assert ret == ['bar']

    lookup_plugin_terms = '{{ foo }}'
    ret = listify_lookup_plugin_terms(lookup_plugin_terms, templar, loader=None, convert_bare=True)
    assert ret == ['bar']

    lookup_plugin

# Generated at 2022-06-13 16:31:42.061062
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    assert listify_lookup_plugin_terms('a', None, None) == ['a']
    assert listify_lookup_plugin_terms('a, b, c', None, None) == ['a', 'b', 'c']
    assert listify_lookup_plugin_terms(['a'], None, None) == ['a']
    assert listify_lookup_plugin_terms(['a', 'b', 'c'], None, None) == ['a', 'b', 'c']
    assert listify_lookup_plugin_terms('a, b, c,', None, None) == ['a', 'b', 'c']
    assert listify_lookup_plugin_terms('a, b, c,d', None, None) == ['a', 'b', 'c']

# Generated at 2022-06-13 16:31:51.273662
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    terms = [1, 2]
    templar = Templar(loader=None, variables={})
    ret = listify_lookup_plugin_terms(terms, templar, loader=None)
    assert ret == [1, 2]

    terms = 1
    templar = Templar(loader=None, variables={})
    ret = listify_lookup_plugin_terms(terms, templar, loader=None)
    assert ret == [1]

    terms = "1"
    templar = Templar(loader=None, variables={})
    ret = listify_lookup_plugin_terms(terms, templar, loader=None)
    assert ret == [1]

    terms = "1 + 2"
    templar = Templar(loader=None, variables={})
    ret

# Generated at 2022-06-13 16:31:59.090202
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.vars import VariableManager
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext

    variable_manager = VariableManager()
    loader = DataLoader()
    templar = Templar(loader=loader, variables=variable_manager)

    play_context = PlayContext()
    templar._available_variables = variable_manager
    templar.set_available_variables(play_context.acquire_lock_on_variable_manager())

    terms = None
    assert listify_lookup_plugin_terms(terms, templar, loader) == [None]

    terms = 'test'
    assert listify_lookup_plugin_terms(terms, templar, loader) == ['test']



# Generated at 2022-06-13 16:32:11.233607
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleUnicode

    vm = VariableManager()
    vm.set_variable('foo', 'bar')
    vm.set_variable('a', {'b': 'c'})

    t = Templar(loader=None, variables=vm)

    assert listify_lookup_plugin_terms(['a', 'b', 'c'], t, None) == ['a', 'b', 'c']

    # string is returned as a single element list
    assert listify_lookup_plugin_terms('foo', t, None) == ['foo']

    # list is returned as it is
    assert listify_lookup_plugin_terms(['foo'], t, None) == ['foo']



# Generated at 2022-06-13 16:32:15.616699
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.six import PY3
    import pytest
    from ansible.module_utils.common._collections_compat import OrderedDict
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.template import Templar
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import lookup_loader

    def _get_loader():
        return DataLoader()

    def _get_passwords(passwords):
        return dict(vault_pass='secret')


# Generated at 2022-06-13 16:32:27.586957
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.common._collections_compat import Sequence
    try:
        from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    except ImportError:
        # Ansible UnsafeText was added in Ansible 2.8
        class AnsibleUnsafeText(str):
            pass

    from ansible.template import Templar

    class FakeVarManager(object):
        def __init__(self):
            self.vars = dict(var1=42, var2='string')

        def get_vars(self, loader, play, hostvars=None):
            return self.vars

    class FakeHost(object):
        def __init__(self, name):
            self.get_name = lambda: name


# Generated at 2022-06-13 16:32:35.537146
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    import ansible.template
    import ansible.parsing.yaml.loader
    import ansible.parsing.yaml.objects

    templar = ansible.template.Templar(loader=ansible.parsing.yaml.loader.AnsibleLoader(''))

    test1 = "{{ 'a' }}"
    test2 = ["{{ 'a' }}"]
    test3 = ["{{ 'a' }}", "b"]
    test4 = ["a", "b", "{{ 'c' }}"]
    test5 = ['{{ test_var }}']

    fail_msg = "test 1 failed"
    assert listify_lookup_plugin_terms(test1, templar, loader) == ['a'], fail_msg



# Generated at 2022-06-13 16:32:48.004217
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    '''
    ansible.module_utils.common.listify_lookup_plugin_terms test
    '''
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list=['localhost'])
    host = inventory.get_host('localhost')
    templar = Templar(loader=loader, variables=variable_manager.get_vars(host=host))

    #####
    # confirm edge cases return a list
    #####

# Generated at 2022-06-13 16:33:24.279152
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    assert listify_lookup_plugin_terms(['a'], {}, {}, True, True) == ['a']
    assert listify_lookup_plugin_terms('a', {}, {}, True, True) == ['a']
    assert listify_lookup_plugin_terms('a,b', {}, {}, True, True) == ['a', 'b']
    assert listify_lookup_plugin_terms('1,2', {}, {}, True, True) == ['1', '2']
    assert listify_lookup_plugin_terms(['a', 'b'], {}, {}, True, True) == ['a', 'b']
    assert listify_lookup_plugin_terms(['a', 'b,c'], {}, {}, True, True) == ['a', 'b,c']

    assert listify_

# Generated at 2022-06-13 16:33:31.273739
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.vault import VaultLib
    from ansible.template import Templar

    loader = DictDataLoader({})
    vault_secrets = DictVaultSecret({})
    templar = Templar(loader=loader, variables={}, vault_secrets=vault_secrets)

    assert listify_lookup_plugin_terms('foo', templar, loader) == ['foo']
    assert listify_lookup_plugin_terms('foo bar', templar, loader) == ['foo bar']
    assert listify_lookup_plugin_terms(['foo', 'bar', 'baz'], templar, loader) == ['foo', 'bar', 'baz']
    assert listify_lookup_plugin_terms('{{ foo }}', templar, loader) == ['{{ foo }}']
    assert list

# Generated at 2022-06-13 16:33:41.499733
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    dummy_loader = DataLoader()
    dummy_templar = Templar(loader=dummy_loader, variables={})
    test_string = '{{ "string" }}'
    test_list_of_strings = '{{ ["list", "of", "strings"] }}'
    test_list_of_strings_and_vars = '{{ ["list", "of", "strings", var1, var2, "etc."] }}'
    test_list_of_strings_and_iterators = '{{ ["list", "of", "strings", "{{ \"{{ \" }}", "{{ \"}} \" }}", "etc."] }}'
    test_list_of

# Generated at 2022-06-13 16:33:49.558630
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    assert listify_lookup_plugin_terms(['a', 'b', 'c'], Templar(loader=None), loader=None) == ['a', 'b', 'c']
    assert listify_lookup_plugin_terms('a b c', Templar(loader=None), loader=None) == ['a b c']
    assert listify_lookup_plugin_terms(['a', ['b', 'c']], Templar(loader=None), loader=None) == ['a', ['b', 'c']]
    assert listify_lookup_plugin_terms(['a', [1, 2, 3], ['b', 'c']], Templar(loader=None), loader=None) == ['a', [1, 2, 3], ['b', 'c']]

# Generated at 2022-06-13 16:34:00.673758
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    # Make a minimal ansible module
    import ansible.module_utils.basic
    import datetime
    import os

    class FakeModule(object):
        def __init__(self, params):
            self.params = params
            self.fail_json = ansible.module_utils.basic.fail_json
            self.exit_json = ansible.module_utils.basic.exit_json
            self._terminal_debug_msg = ansible.module_utils.basic._terminal_debug_msg

    module = FakeModule({'convert_bare': False})

    # Make a minimal ansible templar
    import jinja2

    class FakeTemplar(object):
        def __init__(self, module):
            self.module = module

# Generated at 2022-06-13 16:34:03.625728
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    '''
    listify_lookup_plugin_terms: returns a list of the given args, either as a string or a list,
                                 if they are defined. Otherwise returns an empty list

    '''
    pass

# Generated at 2022-06-13 16:34:12.698638
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.facts import Facts
    from ansible.template import Templar
    from ansible.vars import VariableManager

    # Create the shared objects (for unit tests only)
    variable_manager = VariableManager()
    loader = variable_manager.get_vars_loader()
    facts = Facts(variable_manager=variable_manager, loader=loader)
    variable_manager.set_fact_cache(facts.get_facts())

    templar = Templar(loader=loader, variables=variable_manager)

    # Test with a string containing a list
    terms = '{{ [1, 2] }}'
    terms = listify_lookup_plugin_terms(terms, templar=templar, loader=loader, convert_bare=True)
    assert isinstance(terms, list)
    assert len(terms) == 2

# Generated at 2022-06-13 16:34:24.458668
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    import ansible.template
    import ansible.vars

    # setup dummy objects to pass variables into the function
    class DummyVars:
        def get_vars(self, loader, path, entities=None):
            condition = "{{ couldhavebeendefined }}"
            return condition

    class DummyClass:
        pass

    class DummyTemplar:
        def __init__(self):
            self.template = DummyClass()
            self.vars = DummyVars()

        def template(self, data, fail_on_undefined=False, convert_bare=False):
            return data

    dummy_terms = ['{{ couldhavebeendefined }}']

    # Instantiate the dummy objects to make them available for the function
    dummy_templar = DummyTemplar()

    # make sure we didn't

# Generated at 2022-06-13 16:34:35.566045
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib
    fd, vault_password_file = tempfile.mkstemp()
    os.close(fd)

# Generated at 2022-06-13 16:34:41.134041
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    terms = "1 2 3"
    templar = Templar(loader=DataLoader(), variables=VariableManager())

    result = listify_lookup_plugin_terms(terms, templar, loader=DataLoader())

    assert result == [1, 2, 3]