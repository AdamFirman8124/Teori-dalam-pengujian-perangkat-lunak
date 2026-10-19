

# Generated at 2022-06-13 16:25:11.189787
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.template.template import AnsibleTemplate

    loader = None

    play_context = PlayContext()
    templar = Templar(loader=loader, variables=play_context.variables)

    # Test string type
    test_str = '{{ foo }}'
    assert listify_lookup_plugin_terms(test_str, templar, loader) == [None]
    test_str = '{{ foo }}:{{ bar }}'
    assert listify_lookup_plugin_terms(test_str, templar, loader) == [None]
    test_str = '{{ foo }}:{{ bar }}'
    assert listify_lookup_plugin_terms(test_str, templar, loader) == [None]

# Generated at 2022-06-13 16:25:20.785577
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar # needed for jinja2 env
    import ansible.vars.manager

    # Setup jinja2 environment
    templar = Templar(variables={'var1':'whatsit', 'var2':'whatsit2'})

    # Check with a list
    terms = ['{{ var1 }}', '{{ var2 }}']
    newterms = listify_lookup_plugin_terms(terms, templar, None, convert_bare=False)
    assert newterms == ['whatsit', 'whatsit2']

    # Check with a string
    terms = '{{ var1 }}, {{ var2 }}'
    newterms = listify_lookup_plugin_terms(terms, templar, None, convert_bare=False)

# Generated at 2022-06-13 16:25:29.497778
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.utils import template as template_m
    from ansible.playbook.play_context import PlayContext

    fake_loader = None
    fake_templar = template_m.AnsibleTemplar(loader=fake_loader, variables={'var1': 'foo', 'var2': 'bar'})

    # should return list when given string
    ret = listify_lookup_plugin_terms('var1', fake_templar, fake_loader)
    assert ret == ['foo']

    # should return list when given list
    ret = listify_lookup_plugin_terms(['var1', 'var2'], fake_templar, fake_loader)
    assert ret == ['foo', 'bar']

    # should handle complex vars

# Generated at 2022-06-13 16:25:39.383758
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.utils import template as template_module
    from ansible.template import Templar
    templar = Templar(loader=None)

    class DummyVarManager:
        def __init__(self):
            self.vars = {}

        def __setitem__(self, name, value):
            self.vars[name] = value

        def __getitem__(self, name):
            return self.vars[name]

        def get(self, *args, **kwargs):
            return self.__getitem__(*args, **kwargs)

    class DummyVarsGlobals:
        def __init__(self):
            self.hostvars = {}

        def __setitem__(self, name, value):
            self.hostvars[name] = value


# Generated at 2022-06-13 16:25:51.941071
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    templar = Templar(loader=loader)

    # Test 1
    terms = 'foo'
    result = listify_lookup_plugin_terms(terms, templar, loader)
    assert result == ['foo']

    # Test 2
    terms = ['foo', 'bar']
    result = listify_lookup_plugin_terms(terms, templar, loader)
    assert result == ['foo', 'bar']

    # Test 3
    terms = ['foo', '{{ bar }}']
    result = listify_lookup_plugin_terms(terms, templar, loader)
    assert result == ['foo', '{{ bar }}']

    # Test 4
    bar = 'bar'


# Generated at 2022-06-13 16:26:01.145264
# Unit test for function listify_lookup_plugin_terms

# Generated at 2022-06-13 16:26:11.938449
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.utils.listify_lookup_plugin import listify_lookup_plugin_terms
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    import os
    import pytest

    class Dummy:
        class Dummy1:
            class Dummy2:
                pass

    class FakeVarsModule:
        pass

    class FakeTemplar(Templar):

        def __init__(self, variables=None, loader=None, fail_on_undefined=True, convert_bare=False):
            if variables is None:
                variables = VariableManager()
            self._available_variables = variables
            self._loader = loader
            self.fail

# Generated at 2022-06-13 16:26:20.450545
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.common.collections import listify_lookup_plugin_terms
    from ansible.template import Templar
    from ansible.parsing.yaml.loader import AnsibleLoader

    vars = dict(
        string='foo',
        list=['foo', 'bar'],
        dict={'foo':'bar'}
    )

    terms = [
        {'string': '{{string}}'},
        {'list': ['{{item}}' for item in vars['list']]},
        {'dict': '{{dict[item]}}'}
    ]

    templar = Templar(loader=AnsibleLoader(vars))
    results = listify_lookup_plugin_terms(terms, templar, loader)


# Generated at 2022-06-13 16:26:31.936045
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.template import Templar
    from ansible.template import Jinja2TemplateModule
    from ansible.template import AnsibleJ2Vars
    from ansible.plugins.loader import lookup_loader, action_loader

    templar = Templar(loader=None, variables={})
    # Jinja2TemplateModule.__init__() requires lookup plugins to be registered
    lookup_loader.add_directory("./lib/ansible/plugins/lookup")
    action_loader.add_directory("./lib/ansible/plugins/action")

# Generated at 2022-06-13 16:26:32.819627
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    # TODO: add unit tests for function listify_lookup_plugin_terms
    pass

# Generated at 2022-06-13 16:26:44.677858
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    '''
    Test listify_lookup_plugin_terms()
    '''
    from ansible.module_utils.common.collections import listify_lookup_plugin_terms
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play_context import PlayContext
    import ansible.constants as C
    import jinja2
    import os

    fake_loader = DataLoader()
    fake_inventory = VariableManager()
    fake_context = PlayContext()
    fake_context._the_templar = jinja2.Environment(loader=fake_loader, undefined=jinja2.StrictUndefined)

# Generated at 2022-06-13 16:26:56.546712
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    '''
    if options['_terms']:
        # expand with variables applied to lookups for each term
        vars = templar.available_variables
        terms = listify_lookup_plugin_terms(options['_terms'], templar, loader)
        for x in terms:
            results.append(run_one(x, parameters, loader, variables, vars))
    '''

    # TODO: Need to fix this test.  It's broken when it runs in the test suite
    #       but passes when I remove the 'fail_on_undefined' kwarg and run
    #       the test individually.

    # This test case works:
    # return listify_lookup_plugin_terms(["{{ bar }}"], templar, loader, fail_on_undefined=True, convert_bare=False)



# Generated at 2022-06-13 16:27:05.966840
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    class FakeTemplar(object):
        def __init__(self, value_to_return):
            self.value_to_return = value_to_return

        def template(self, a, b=None, c=None, d=None):
            return self.value_to_return

    # Test 1
    arg1 = '{{ a }}'
    arg2 = 'b'
    arg3 = 'c'
    arg4 = 'd'
    arg4a = True

    # Test 2
    arg5 = ['e']
    arg6 = 'f'
    arg7 = 'g'
    arg8 = 'h'
    arg8a = True

    ans1 = ['x']
    ans2 = ['y']
    ans3 = ['z']
    ans4 = ['w']

    x = FakeTempl

# Generated at 2022-06-13 16:27:16.643651
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    test_terms = "{{ 'a, b, c' | split(',') }}"
    (terms, templar, loader) = (test_terms, "", "")
    assert listify_lookup_plugin_terms(terms, templar, loader) == ['a', ' b', ' c']
    test_terms = "{{ ['d', 'e', 'f'] }}"
    (terms, templar, loader) = (test_terms, "", "")
    assert listify_lookup_plugin_terms(terms, templar, loader) == ['[', 'd', ']']
    test_terms = "{{ 'g' if g else 'h' }}"
    (terms, templar, loader) = (test_terms, "", "")

# Generated at 2022-06-13 16:27:26.723320
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

    terms = [ 'a', 'b', 'c' ]
    assert listify_lookup_plugin_terms(terms, templar=None, loader=loader) == ['a', 'b', 'c']

    terms = 'a,b,c'
    assert listify_lookup_plugin_terms(terms, templar=None, loader=loader) == ['a', 'b', 'c']

    terms = 'a,b,'
    assert listify_lookup_plugin_terms(terms, templar=None, loader=loader) == ['a', 'b', '']

    terms = 'a,b,""'

# Generated at 2022-06-13 16:27:35.182820
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.yaml.loader import AnsibleLoader
    import ansible.constants as C

    templar = Templar(loader=AnsibleLoader(None), variables={'a': 94})

    # Note: empty string never fails, but empty list or dict will fail
    assert listify_lookup_plugin_terms('', templar, None) == ['']
    assert listify_lookup_plugin_terms('a', templar, None) == ['a']
    assert listify_lookup_plugin_terms('"a"', templar, None) == ['a']
    assert listify_lookup_plugin_terms('\'a\'', templar, None) == ['a']

# Generated at 2022-06-13 16:27:46.456839
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    # Imports needed for this test
    from ansible.template import Templar

    # Create the templar
    templar = Templar(loader=None, variables={})

    # Test a string
    terms = listify_lookup_plugin_terms('{{ test1 }}', templar, None)
    assert isinstance(terms, list)
    assert len(terms) == 1
    assert terms[0] == '{{ test1 }}'

    # Test a list of strings with the default setting of fail_on_undefined
    terms = listify_lookup_plugin_terms(['{{ test1 }}', '{{ test2 }}'], templar, None)
    assert isinstance(terms, list)
    assert len(terms) == 2
    assert terms[0] == '{{ test1 }}'

# Generated at 2022-06-13 16:27:57.097133
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.parsing import DataLoader
    from ansible.templating import Templar
    from ansible.vars import VariableManager
    from ansible.playbook.play_context import PlayContext


# Generated at 2022-06-13 16:28:07.972960
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    # The test cases

# Generated at 2022-06-13 16:28:18.318899
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    class TestVarsModule(object):
        def __init__(self, params):
            self.params = params
        def vars(self):
            return self.params

    class TestTask(object):
        def __init__(self, temp_vars, loader, fail_on_undefined):
            self.templar = Templar(loader=loader, variables=temp_vars, fail_on_undefined=fail_on_undefined)

    class TestPlayContext(object):
        def __init__(self, convert_bare=False):
            self.convert_bare = convert_bare

    # test lists
    loader = None
    temp_vars = TestVarsModule({'a': 'a'})

# Generated at 2022-06-13 16:28:29.600389
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.template import Templar

    results = listify_lookup_plugin_terms('string', Templar(loader=None), None) \
        == ['string']
    assert results

    results = listify_lookup_plugin_terms([1, 2, 3], Templar(loader=None), None) \
        == [1, 2, 3]
    assert results

    results = listify_lookup_plugin_terms('{{ lookup("pipe", "ls /tmp") }}', Templar(loader=None), None, convert_bare=True) \
        == ['sh: ls: command not found']

# Generated at 2022-06-13 16:28:38.898664
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.parsing.vault import VaultLib
    from ansible.template import Templar
    from ansible.template import AnsibleVaultEncryptedUnicode

    # Encrypted text
    vault = VaultLib([])
    text = "!vault |\n          $ANSIBLE_VAULT;1.1;AES256\n          31663035383032316337333935633964313965393166623236383362643536666432656566\n          6535343033396438393562663062333962333035\n          31396636356136633736383861306438306339616232386165613663633962333161336161\n          37633736"

    terms = "{{ foo }}"
    args = {'foo': text}

# Generated at 2022-06-13 16:28:47.407334
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    play_context = PlayContext()
    templar = Templar(play_context=play_context)
    terms = listify_lookup_plugin_terms('{{ [] }}', templar, loader=None, fail_on_undefined=True, convert_bare=False)
    assert terms == []

    terms = listify_lookup_plugin_terms('{{ [1, 2, 3] }}', templar, loader=None, fail_on_undefined=True, convert_bare=False)
    assert terms == [1, 2, 3]


# Generated at 2022-06-13 16:28:59.248284
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    import ansible.template
    # empty term list
    t = ansible.template.Template(None)
    assert listify_lookup_plugin_terms([], t, None) == []

    # term list with a single element
    assert listify_lookup_plugin_terms(['foo'], t, None) == ['foo']

    # term list with multiple elements
    assert listify_lookup_plugin_terms(['foo', 'bar', 123], t, None) == ['foo', 'bar', 123]

    # term list with a single templated element
    assert listify_lookup_plugin_terms(['{{ foo }}'], t, None) == ['{{ foo }}']

    # term list with multiple templated elements

# Generated at 2022-06-13 16:29:09.773771
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar
    import ansible.utils.unsafe_proxy

    class DummyVarsModule:
        def __init__(self):
            self.a = {'b': 'c'}

        def get_vars(self, loader, play, host, task):
            return {'a': 'd'}

    d = DummyVarsModule()

    # test strings
    x = listify_lookup_plugin_terms('hello', Templar(loader=None, variables=d), loader=None)
    assert x == ['hello']

    # test lists
    x = listify_lookup_plugin_terms(['hello', 'world'], Templar(loader=None, variables=d), loader=None)
    assert x == ['hello', 'world']

    # test dicts
    x = listify_look

# Generated at 2022-06-13 16:29:20.149642
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    def _test_listify_lookup_plugin_terms(terms, expected):
        templar = Templar(loader=None, variables={})
        actual = listify_lookup_plugin_terms(terms, templar, loader=None, fail_on_undefined=True, convert_bare=False)
        return actual == expected

    assert _test_listify_lookup_plugin_terms(["foo", "bar"], ["foo", "bar"])
    assert _test_listify_lookup_plugin_terms("foo", ["foo"])
    assert _test_listify_lookup_plugin_terms("foo,bar", ["foo,bar"])

# Generated at 2022-06-13 16:29:30.332679
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.vars.unsafe_proxy import wrap_var

    # Set up Templar
    vault_secret = VaultLib('mysecret')
    templar = Templar(loader=None, variables={'password':wrap_var(UnsafeProxy(vault_secret, 'password'))})

    # Test function
    result = listify_lookup_plugin_terms(['{{password}}', 'test', '{{password}}'], templar, None, fail_on_undefined=True, convert_bare=False)
    assert result == ['mysecret', 'test', 'mysecret']

    # Test function

# Generated at 2022-06-13 16:29:31.726655
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    # unit tests need to be in a standalone python file
    # ansible.module_utils.common.listify_lookup_plugin_terms is a hard coded import
    # so, we place these unit tests in a separate file
    raise NotImplementedError

# Generated at 2022-06-13 16:29:39.468851
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    # should handle string
    templar = Templar(loader=None)
    assert listify_lookup_plugin_terms("{{ '-a -b' }}", templar, None) == ["-a -b"]

    # should handle list of strings
    templar = Templar(loader=None)
    assert listify_lookup_plugin_terms(["{{ '-a' }}", "{{ '-b' }}"], templar, None) == ["-a", "-b"]

    # should handle list of strings, with no templating
    templar = Templar(loader=None)
    assert listify_lookup_plugin_terms(["-a", "-b"], templar, None) == ["-a", "-b"]

    # should handle list of strings, with no templating


# Generated at 2022-06-13 16:29:50.639285
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.template import Jinja2TemplateModule
    from ansible.parsing.plugin_docs import read_docstring
    from ansible.template import Templar
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.vars.manager import VariableManager

    from ansible.parsing.vault import VaultLib

    loader = DictDataLoader({})
    vault_secrets = VaultLib([])
    inventory = Inventory(loader, vault_secrets, host_list=[])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    doc_fragments = read_docstring(listify_lookup_plugin_terms, verbose=False)

# Generated at 2022-06-13 16:30:05.691077
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    import ansible.vars.manager
    import ansible.inventory.manager

    loader = DataLoader()
    variables = ansible.vars.manager.VariableManager()
    inventory = ansible.inventory.manager.InventoryManager(loader=loader, sources='')
    templar = Templar(loader=loader, variables=variables, inventory=inventory)
    assert listify_lookup_plugin_terms(["foo", "bar"], templar, loader) == ["foo", "bar"]
    assert listify_lookup_plugin_terms(["foo", "{{bar}}"], templar, loader) == ["foo", "{{bar}}"]

# Generated at 2022-06-13 16:30:16.134602
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.templating.template import Templar
    from ansible.parsing.vault import VaultLib
    vt = VaultLib([])
    t = Templar(loader=None, variables={'foo': 'a/b/c'}, vault_secrets=vt)
    assert listify_lookup_plugin_terms('{{ foo }}', t, loader=None) == ['a/b/c']
    assert listify_lookup_plugin_terms(['{{ foo }}'], t, loader=None) == ['a/b/c']
    assert listify_lookup_plugin_terms(['a/b/c', '{{ foo }}'], t, loader=None) == ['a/b/c', 'a/b/c']

# Generated at 2022-06-13 16:30:27.893920
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar
    from ansible.module_utils.facts import ModuleFacts

    # Can listify non-string, non-iterable.
    assert listify_lookup_plugin_terms(None, Templar(loader=None), None, fail_on_undefined=False) == [None]
    assert listify_lookup_plugin_terms(0, Templar(loader=None), None, fail_on_undefined=False) == [0]

    # Can listify string
    assert listify_lookup_plugin_terms("abc", Templar(loader=None), None, fail_on_undefined=False) == ["abc"]

    # Can listify templated string

# Generated at 2022-06-13 16:30:36.778988
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    templar = Templar(loader=loader)
    assert [u"foo.txt", u"bar.txt"] == listify_lookup_plugin_terms("foo.txt,bar.txt", templar, loader, convert_bare=True)
    assert [u"foo.txt", u"bar.txt"] == listify_lookup_plugin_terms(["foo.txt", "bar.txt"], templar, loader, convert_bare=True)

# Generated at 2022-06-13 16:30:44.734089
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.vars import VariableManager
    from ansible.utils.vars import combine_vars
    new_std = combine_vars(loader=AnsibleLoader(), variables=VariableManager())

    templar = Templar(loader=AnsibleLoader(), variables=new_std)
    assert listify_lookup_plugin_terms('foo', templar, AnsibleLoader()) == ['foo']
    assert listify_lookup_plugin_terms(['foo'], templar, AnsibleLoader()) == ['foo']
    assert listify_lookup_plugin_terms(['foo', 'bar'], templar, AnsibleLoader()) == ['foo', 'bar']
    assert listify_lookup_plugin_terms

# Generated at 2022-06-13 16:30:55.813227
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    test_templar = Templar(loader=None, variables={'item': ['a', 'b', 'c']})

    test_input = ['{{item}}']
    test_result = listify_lookup_plugin_terms(test_input, test_templar, None)
    assert test_result == ['a', 'b', 'c']

    test_input = '{{item}}'
    test_result = listify_lookup_plugin_terms(test_input, test_templar, None)
    assert test_result == ['a', 'b', 'c']

    test_input = ['{{item}}', 'd']
    test_result = listify_lookup_plugin_terms(test_input, test_templar, None)

# Generated at 2022-06-13 16:31:07.664468
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    ''' test_listify_lookup_plugin_terms '''

    from ansible.template import Templar

    templar = Templar(loader=None)

    # Test with convert_bare
    (expect, result) = ([], listify_lookup_plugin_terms('', templar, None))
    assert result == expect

    (expect, result) = (
        ['Hello'],
        listify_lookup_plugin_terms('Hello', templar, None, convert_bare=True)
    )
    assert result == expect

    (expect, result) = (
        ['Hello'],
        listify_lookup_plugin_terms(['Hello'], templar, None, convert_bare=True)
    )
    assert result == expect


# Generated at 2022-06-13 16:31:17.919975
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()
    jinja2_templar = Templar(loader=loader, variables=variable_manager)

    assert listify_lookup_plugin_terms("my_path", jinja2_templar, loader) == ['my_path']
    assert listify_lookup_plugin_terms(["my_path"], jinja2_templar, loader) == ['my_path']
    assert listify_lookup_plugin_terms("[1,2,3]", jinja2_templar, loader) == [1,2,3]

# Generated at 2022-06-13 16:31:27.935494
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    templar = Templar(loader=None, variables={'a': 'foo', 'b': ['foo', 'bar', 'baz']})

    assert listify_lookup_plugin_terms(terms='{{ a }}', templar=templar, loader=None) == ['foo']
    assert listify_lookup_plugin_terms(terms=['{{ a }}', '{{ b }}'], templar=templar, loader=None) == ['foo', ['foo', 'bar', 'baz']]
    assert listify_lookup_plugin_terms(terms='{{ b }}', templar=templar, loader=None, convert_bare=True) == ['foo', 'bar', 'baz']

# Generated at 2022-06-13 16:31:38.319094
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.parsing.vault import VaultLib
    from ansible.template import Templar
    from ansible.template.safe_eval import SafeEval
    from ansible.plugins import lookup_loader, lookup_finder
    from ansible.playbook.play_context import PlayContext

    context = dict(a='world', b=dict(c='hello'))
    templar = Templar(loader=None, variables=context, fail_on_undefined=True)
    templar.set_available_variables(context)

    # Test a string
    result = listify_lookup_plugin_terms('{{a}}', templar, None)
    assert result == ['world']

    # Test a list

# Generated at 2022-06-13 16:31:58.419232
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    inventory = VariableManager()

    inventory.set_variable('item', 'value')

    templar = Templar(loader=None, shared_loader_obj=None, variables=inventory)

    # Check that single items in terms (strings and non-strings) are properly converted to lists
    assert  listify_lookup_plugin_terms('{{item}}', templar, None, fail_on_undefined=True, convert_bare=False) == ['value']
    assert  listify_lookup_plugin_terms(42, templar, None, fail_on_undefined=True, convert_bare=False) == [42]

    # Check that lists are preserved
    terms = ['{{item}}', 42]
    assert  listify_lookup_

# Generated at 2022-06-13 16:32:10.573746
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible import template

    templar = template.AnsibleTemplar()
    loader = None

    # Pass string
    assert listify_lookup_plugin_terms(
        'foo, bar, baz',
        templar,
        loader
        ) == 'foo, bar, baz'.split(', ')

    # Pass iterable
    assert listify_lookup_plugin_terms(
        'foo, bar, baz'.split(', '),
        templar,
        loader
        ) == 'foo, bar, baz'.split(', ')

    # Convert bare vars:

# Generated at 2022-06-13 16:32:17.870776
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    loader = DataLoader()
    vault_secrets = VaultLib(password_file=None,
                             passwords={})
    templar = Templar(loader=loader,
                      variables=variable_manager,
                      vault_secrets=vault_secrets)

    # Test with a simple string.
    assertions = {
        'obj': 'foo',
        'expected': ['foo']
    }
    result = listify_lookup_plugin_terms(assertions['obj'], templar, loader)
    assert result == assertions['expected']

    # Test with a simple list.

# Generated at 2022-06-13 16:32:29.516855
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    my_vars = dict(name='Fred',
                   thing='foo',
                   dict_var={'a': 1, 'b': 2, 'c': 3},
                   list_var=['one', 'two', 'three'],
                   int_var=123,
                   bool_var=True)

    templar = Templar(loader=None,
                      variables=my_vars)

    assert sorted(listify_lookup_plugin_terms(u' Fred ', templar)) == sorted([u'Fred'])
    assert sorted(listify_lookup_plugin_terms(u'{{ thing }}', templar)) == sorted([u'foo'])
    assert sorted(listify_lookup_plugin_terms(u'{{ name }}', templar)) == sorted([u'Fred'])


# Generated at 2022-06-13 16:32:39.640224
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.vault import VaultLib
    from ansible.template import Templar

    from ansible.playbook import PlaybookInclude
    from ansible.vars import VariableManager

    variable_mgr = VariableManager()

    vault_pass = 'ansible'
    vault_secret_file = 'ansible-vault.txt'
    vault_id = 'test-vault-id'

# Generated at 2022-06-13 16:32:49.383353
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar

    loader = DataLoader()
    templar = Templar(loader=loader)

    assert listify_lookup_plugin_terms('foo', templar, loader) == ['foo']
    assert listify_lookup_plugin_terms(['foo'], templar, loader) == ['foo']
    assert listify_lookup_plugin_terms(['foo', 'bar'], templar, loader) == ['foo', 'bar']
    assert listify_lookup_plugin_terms('foo bar', templar, loader) == ['foo', 'bar']
    assert listify_lookup_plugin_terms('foo,bar', templar, loader) == ['foo,bar']
    assert listify_lookup_plugin_terms

# Generated at 2022-06-13 16:32:57.137451
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    templar = Templar(loader=DataLoader())
    t1 = """
- foo
- bar"""
    assert listify_lookup_plugin_terms(t1, templar, loader=DataLoader()) == ['foo', 'bar']
    t2 = "foo"
    assert listify_lookup_plugin_terms(t2, templar, loader=DataLoader()) == ['foo']
    t3 = "foo\nbar"
    assert listify_lookup_plugin_terms(t3, templar, loader=DataLoader()) == ['foo\nbar']

# Generated at 2022-06-13 16:33:04.121173
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    class TestVars(object):
        def __init__(self):
            self.key = None
        def get(self, *args, **kwargs):
            return TestVars()
        __getitem__ = get

    listify_lookup_plugin_terms('foo', Templar(loader=DataLoader()), TestVars())

# Generated at 2022-06-13 16:33:12.563363
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.templating import Templar
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    terms = [
        ("a", "b"),
        ("d,e,f", "g,h,i"),
        ("a,b,c", "d,e,f,g,h,i,j,k,l"),
        ("{{ a }}", "b", "{{ b }}", "{{ a }},{{ b }}")
    ]


# Generated at 2022-06-13 16:33:19.934958
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    t = Templar(loader=DataLoader(), variables=VariableManager(loader=DataLoader(), inventory=InventoryManager(loader=DataLoader())))
    assert listify_lookup_plugin_terms('hello', templar=t, loader=None) == ['hello']
    assert listify_lookup_plugin_terms(['hello', 'world'], templar=t, loader=None) == ['hello', 'world']
    assert listify_lookup_plugin_terms('[ hello , world]', templar=t, loader=None) == ['hello', 'world']

# Generated at 2022-06-13 16:33:49.166702
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    loader = DictDataLoader({})
    templar = Templar(loader=loader)

    # Test single item
    terms = "foo.txt"
    results = listify_lookup_plugin_terms(terms, templar, loader)
    assert(results == ['foo.txt'])

    # Test multiple items
    terms = "foo.txt, bar.txt"
    results = listify_lookup_plugin_terms(terms, templar, loader)
    assert(results == ['foo.txt', 'bar.txt'])

    # Test list of items
    terms = [ "foo.txt", "bar.txt" ]
    results = listify_lookup_plugin_terms(terms, templar, loader)
    assert(results == ['foo.txt', 'bar.txt'])

# Generated at 2022-06-13 16:33:58.170914
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    terms = 'a,b,c'
    templar = Templar(None)
    try:
        assert listify_lookup_plugin_terms(terms, templar) == [u'a', u'b', u'c']
        assert listify_lookup_plugin_terms([terms], templar) == [u'a', u'b', u'c']

        assert listify_lookup_plugin_terms([u'a', u'b', u'c'], templar) == [u'a', u'b', u'c']
    except AssertionError:
        return False

    return True

# Generated at 2022-06-13 16:34:07.940794
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.template import Templar
    from ansible.vars.unsafe_proxy import UnsafeProxy

    dl = DataLoader()
    im = InventoryManager(loader=dl)
    vm = VariableManager(loader=dl, inventory=im)
    t = Templar(loader=dl, variables=vm)

    assert listify_lookup_plugin_terms(['foo', 'bar'], t, dl) == ['foo', 'bar']
    assert listify_lookup_plugin_terms('foo:{{ foo }} bar', t, dl) == ['foo:{{ foo }} bar']

# Generated at 2022-06-13 16:34:14.537129
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    import os
    import sys
    import warnings
    import tempfile
    import yaml
    from ansible.parsing import vault

    vault_secret_file = os.path.join(os.path.dirname(__file__), '../../utils/crypto.py')
    secret = vault.read_vault_secret_file(vault_secret_file)
    if secret is False:
        warnings.warn("could not find vault secret from %s" % vault_secret_file)
    else:
        vault.set_vault_password(secret)

    from ansible.module_utils.common._collections_compat import Mutabl

# Generated at 2022-06-13 16:34:26.885846
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible import constants as C
    from ansible.module_utils.six.moves import cStringIO
    from ansible.template import Templar

    templar_loader = DictDataLoader({
        "file": ("{{ lookup('env', 'HOME') }}/this is a file.txt", {}),
        "dir": ("{{ lookup('env', 'HOME') }}/this is a directory/", {}),
        "other": ("file", {})
    })
    templar = Templar(loader=templar_loader, variables={'home': u'/home/foo'})

    # Test _terms_as_list()'s return value if the input argument is a string
    # Find the env home

# Generated at 2022-06-13 16:34:36.905612
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    import ansible.vars.manager
    from ansible.module_utils.six import string_types

    mgr = ansible.vars.manager.VariableManager()
    templar = mgr.get_vars_templar('play')
    terms = "{{ var1 }}"
    result = listify_lookup_plugin_terms(terms, templar, None)
    assert result == ["{{ var1 }}"]
    terms = [terms]
    result = listify_lookup_plugin_terms(terms, templar, None)
    assert result == ["{{ var1 }}"]
    terms = [terms, "{{ var2 }}"]
    result = listify_lookup_plugin_terms(terms, templar, None)
    assert result == [["{{ var1 }}"], "{{ var2 }}"]
    terms

# Generated at 2022-06-13 16:34:40.608234
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    # test with a string
    terms = listify_lookup_plugin_terms("{{ testvar }}", None, None, fail_on_undefined=True, convert_bare=False)
    assert isinstance(terms, list)
    assert isinstance(terms[0], string_types)

    # test with a list, should not change
    terms = listify_lookup_plugin_terms(["test", "item"], None, None, fail_on_undefined=True, convert_bare=False)
    assert isinstance(terms, list)

    # test with a non-iterable object, should only wrap in list
    terms = listify_lookup_plugin_terms(42, None, None, fail_on_undefined=True, convert_bare=False)
    assert isinstance(terms, list)

# Generated at 2022-06-13 16:34:48.347414
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    assert listify_lookup_plugin_terms('one', Templar(DataLoader()), DataLoader()) == ['one']
    assert listify_lookup_plugin_terms(['one'], Templar(DataLoader()), DataLoader()) == ['one']
    assert listify_lookup_plugin_terms('one\ntwo\nthree', Templar(DataLoader()), DataLoader()) == ['one\ntwo\nthree']
    assert listify_lookup_plugin_terms(['one', 'two', 'three'], Templar(DataLoader()), DataLoader()) == ['one', 'two', 'three']

# Generated at 2022-06-13 16:34:57.819306
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.module_utils.six.moves import StringIO
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory

    variable_manager = VariableManager()
    loader = variable_manager.get_vars_loader()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list=[])
    templar = Templar(loader=loader, variables=variable_manager.get_vars(), inventory=inventory)

    # test string input
    value = "{{ lookup('pipe', 'echo foo') }}"
    returned = listify_lookup_plugin_terms(value, templar, loader)
    assert isinstance(returned, list)
    assert len(returned) == 1
    assert returned[0] == 'foo'

    # test