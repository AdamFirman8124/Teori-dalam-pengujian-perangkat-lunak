

# Generated at 2022-06-13 16:25:12.411679
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    # If a string is passed in, it should still be a list (but of length 1)
    assert listify_lookup_plugin_terms('my_string', Templar(loader=DataLoader())) == ['my_string']

    # If a list is passed in, that list should still be a list
    assert listify_lookup_plugin_terms(['my_string'], Templar(loader=DataLoader())) == ['my_string']

    # If a list of lists is passed in, the original list should be returned
    assert listify_lookup_plugin_terms([['my_string']], Templar(loader=DataLoader())) == [['my_string']]

    # If an empty list is passed in, that empty list should be returned


# Generated at 2022-06-13 16:25:19.386552
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    terms = 'foo'
    loader = None
    templar = Templar(loader=loader)

    ret = listify_lookup_plugin_terms(terms, templar, loader)
    assert(isinstance(ret, list))
    assert(ret[0] == 'foo')

    terms = ['foo', 'bar']
    templar = Templar(loader=loader)

    ret = listify_lookup_plugin_terms(terms, templar, loader)
    assert(isinstance(ret, list))
    assert(ret[0] == 'foo')
    assert(ret[1] == 'bar')

# FIXME: need test for when terms is a string that evaluates to a list and vice versa

# Generated at 2022-06-13 16:25:26.974135
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    class MockTemplar(object):
        """
        Templar object that hard matters/returns terms
        """
        def template(self, terms, *args, **kwargs):
            return terms

    class MockLoader(object):
        """
        Loader object that hard matters/returns templar
        """
        def get_basedir(self, path):
            return path

        def get_real_file(self, path):
            return path

    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()

    templar = MockTemplar()
    # Test 1: Test template all types
    test_types = [None, 1, 1.1, [1, 2, 3], {'foo': 'bar'}, set([1, 2, 3])]

# Generated at 2022-06-13 16:25:38.174327
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.template.safe_eval import safe_eval
    from ansible.vars import VariableManager

    variable_manager = VariableManager()

    variable_manager.set_nonpersistent_facts(dict(omg='lol'))

    templar = Templar(loader=None, variable_manager=variable_manager, shared_loader_obj=None)

    assert listify_lookup_plugin_terms('{{omg}}', templar, loader=None) == ['lol']
    assert listify_lookup_plugin_terms('{{omg}}', templar, loader=None, convert_bare=True) == ['{{omg}}']

    # Test boolean short-circuit
    assert listify_lookup_plugin_terms('{{ ok and omg }}', templar, loader=None)

# Generated at 2022-06-13 16:25:50.671810
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.template import Templar
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    import os

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    play_source =  dict(
            name = "Ansible Play",
            hosts = 'localhost',
            gather_facts = 'no',
            tasks = [
                dict(action=dict(module='debug', args=dict(msg='{{value}}'))),
            ]
        )

# Generated at 2022-06-13 16:26:00.286083
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    # Import needed Ansible modules
    from ansible.template import Templar
    from ansible.template import Jinja2TemplateFile

    # Store function arguments
    terms = "{{ lookup('vars', 'inventory_hostname') }}"
    templar = Templar(loader=None, variables={'inventory_hostname': 'localhost'})

    # Call function
    result = listify_lookup_plugin_terms(terms, templar)

    # Check results
    assert result == ['localhost']

    # Store function arguments
    terms = ["{{ lookup('vars', 'inventory_hostname') }}"]
    templar = Templar(loader=None, variables={'inventory_hostname': 'localhost'})

    # Call function
    result = listify_lookup_plugin_terms(terms, templar)

    # Check results
    assert result

# Generated at 2022-06-13 16:26:11.488108
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    templar = Templar(loader=None)

    in1 = '{{a}}'
    out1 = [{'a': 1}]
    assert listify_lookup_plugin_terms(in1, templar, None, fail_on_undefined=False) == out1

    in2 = '{{a.b}}'
    out2 = [1]
    assert listify_lookup_plugin_terms(in2, templar, None, fail_on_undefined=False) == out2

    in3 = ['{{a.b}}', '{{a.c}}']
    out3 = [1,2]
    assert listify_lookup_plugin_terms(in3, templar, None, fail_on_undefined=False) == out3

# Generated at 2022-06-13 16:26:20.033719
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    loader = DictDataLoader({})
    templar = Templar(loader=loader)

    test1 = 'foo'
    expected1 = ['foo']
    assert listify_lookup_plugin_terms(test1, templar, loader) == expected1

    test2 = 42
    expected2 = [42]
    assert listify_lookup_plugin_terms(test2, templar, loader) == expected2

    test3 = [42, 'foo']
    expected3 = [42, 'foo']
    assert listify_lookup_plugin_terms(test3, templar, loader) == expected3

    test4 = {'foo': 'bar'}
    expected4 = [{'foo': 'bar'}]

# Generated at 2022-06-13 16:26:31.490595
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    templar = Templar(loader=DataLoader())

    assert listify_lookup_plugin_terms(['a', 'b', 'c'], templar, None) == ['a', 'b', 'c']
    assert listify_lookup_plugin_terms(('a', 'b', 'c'), templar, None) == ['a', 'b', 'c']
    assert listify_lookup_plugin_terms({'a': 'b', 'c': 'd'}, templar, None) == ['a', 'c']
    assert listify_lookup_plugin_terms('xyz', templar, None) == ['xyz']

# Generated at 2022-06-13 16:26:41.022409
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.template import Templar

    class FakeVarsModule(object):
        pass

    class FakeLoaderModule(object):
        pass

    fake_vars = FakeVarsModule()
    fake_vars.ansible_version = '2.3.0.0'

    fake_loader = FakeLoaderModule()
    fake_loader.get_basedir = lambda x: '/'

    templar = Templar(loader=fake_loader, variables=fake_vars)

    assert listify_lookup_plugin_terms('foo', templar, fake_loader) == ['foo']
    assert listify_lookup_plugin_terms(['foo', 'bar'], templar, fake_loader) == ['foo', 'bar']

# Generated at 2022-06-13 16:26:56.561881
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.utils.vars import combine_vars

    def _ma(namespace, **kwargs):
        """Mock module_args."""
        return combine_vars(kwargs, namespace)

    fake_loader = DummyLoader()
    templar = Templar(loader=fake_loader)

    bare_var = '{{ foo }}'

    # Check all possible inputs to terms
    for terms in [
            10,                                               # int
            1.2,                                              # float
            ['foo', '{{ bar }}', 'baz', 1, 2]                 # list
            ]:
        yield listify

# Generated at 2022-06-13 16:27:06.017826
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable

    variable_manager = VariableManager()
    loader = variable_manager.loader
    variable_manager.set_available_variables({'a': '1', 'b': '2'})

    # Test passing strings
    templar = Templar(loader=loader, variables=variable_manager)
    args = 'a'
    result = listify_lookup_plugin_terms(args, templar, loader)
    assert result == ['1']

    args = 'a,b'
    result = listify_lookup_plugin_terms(args, templar, loader)
    assert result == ['1','2']

   

# Generated at 2022-06-13 16:27:16.685185
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.template import AnsibleModuleFake
    mod = AnsibleModuleFake()
    mod.params = {}
    mod.params['test_var'] = "test var value"

    templar = Templar(loader=mod.loader, shared_loader_obj=mod._shared_loader_obj, variables=mod.params)
    templar._available_variables = mod.params

    assert listify_lookup_plugin_terms("{{test_var}}", templar, mod.loader) == ["test var value"]  # Test with a bare string term
    assert listify_lookup_plugin_terms('{{test_var}}', templar, mod.loader) == ['test var value']  # Test with a quoted string term

# Generated at 2022-06-13 16:27:26.799626
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    import ansible.errors as errors
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleSequence
    from ansible.template import Templar

    t = Templar(loader=None, variables={'var1': 'foo', 'var2': 'bar'})

    assert listify_lookup_plugin_terms(1, t) == ['1']
    assert listify_lookup_plugin_terms(None, t) == [None]
    assert listify_lookup_plugin_terms('foo', t) == ['foo']
    assert listify_lookup_plugin_terms([1, 2, 3], t) == [1, 2, 3]

# Generated at 2022-06-13 16:27:35.391258
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    class DummyLoader(object):
        def __init__(self, var_templates={}):
            self.var_templates = var_templates

    class DummyTemplar(object):
        def __init__(self, hostvars, loader, variables):
            self.hostvars = hostvars
            self.loader = loader
            self.vars = variables

        def template(self, source, convert_bare=False, fail_on_undefined=True):
            if isinstance(source, string_types):
                return self.loader.var_templates[source]
            else:
                return source

    module_vars = {
        'var1': 'a',
        'var2': 'b',
        'var3': 'c',
        }

# Generated at 2022-06-13 16:27:42.615960
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    the_templar = Templar(loader=None, variables={})

    terms = listify_lookup_plugin_terms('foo', the_templar, loader=None)
    assert terms == ['foo']

    terms = listify_lookup_plugin_terms(['foo', 'bar'], the_templar, loader=None)
    assert terms == ['foo', 'bar']

# Generated at 2022-06-13 16:27:52.026378
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.common._collections_compat import Sequence

    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import VaultLib

    # Configure vault secrets, as they are needed by some tests below
    vault_secrets = {'_ansible_vault_pass': 'test'}

    # Ensure we have a empty vault secrets file, as this can cause problems with the tests
    vault = VaultLib([])
    vault.write_file('')

    t = Templar(loader=None, variables=VariableManager(loader=None, vault_secrets=vault_secrets))


# Generated at 2022-06-13 16:27:55.870301
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    # example values
    terms = 'foo, bar'
    templar = 'templar'
    loader = 'loader'

    # Call the function
    result = listify_lookup_plugin_terms(terms, templar, loader)

    # Validate the results
    assert result == ['foo', 'bar']

# Generated at 2022-06-13 16:28:07.251594
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible import constants as C
    from ansible.plugins.loader import lookup_loader

    _loader = lookup_loader
    _templar = _loader.get('template')
    _fail_on_undefined = True
    _convert_bare = True

    # test string input
    _terms = '{{ args }}'
    assert listify_lookup_plugin_terms(_terms, _templar, _loader, _fail_on_undefined, _convert_bare) == ['foo', 'bar']

    # test unicode input
    _terms = '{{ args }}'
    assert listify_lookup_plugin_terms(_terms, _templar, _loader, _fail_on_undefined, _convert_bare) == ['foo', 'bar']

    # test list input with embedded template

# Generated at 2022-06-13 16:28:18.064733
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleUnicode

    loader = None
    templar = Templar(loader, variables={'var': AnsibleUnicode('foo,bar,baz:')})
    assert listify_lookup_plugin_terms('{{ var }}', templar, loader) == ['foo', 'bar', 'baz:']
    assert listify_lookup_plugin_terms(['{{ var }}', 'one'], templar, loader) == ['foo', 'bar', 'baz:', 'one']
    assert listify_lookup_plugin_terms(None, templar, loader) == [None]
    assert listify_lookup_plugin_terms(True, templar, loader) == [True]
    assert listify_lookup

# Generated at 2022-06-13 16:28:30.296277
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from jinja2 import Environment, StrictUndefined, DictLoader
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.dumper import AnsibleDumper

    env = Environment(undefined=StrictUndefined, loader=DictLoader({}), keep_trailing_newline=True)
    templar = Templar(loader=AnsibleLoader, shared_loader_obj=env, variables={'test': 'variable_value'}, fail_on_undefined=True)

    # pass in a list and ensure it returns a list
    terms = ['one', 'two', 'three']
    assert listify_lookup_plugin_terms(terms, templar) == terms

    # pass in a string and ensure a list is returned
    terms = 'one'
   

# Generated at 2022-06-13 16:28:38.966659
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    templar = Templar(loader=loader, variables=variable_manager)

    terms = listify_lookup_plugin_terms([1,2,3], templar, loader)
    assert terms == [1,2,3]
    terms = listify_lookup_plugin_terms('{{ foo }}', templar, loader, convert_bare=False)
    assert terms == ['{{ foo }}']
    terms = listify_lookup_plugin_

# Generated at 2022-06-13 16:28:47.445952
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar
    import jinja2

    loader = jinja2.DictLoader({'foo': 'bar', 'ansible': '{{ foo }}'})
    t = Templar(loader=loader)
    res = listify_lookup_plugin_terms('{{ foo }}', t, loader)
    assert res == ['bar']

    res = listify_lookup_plugin_terms('{{ ansible }}', t, loader)
    assert res == ['bar']

    res = listify_lookup_plugin_terms(['{{ ansible }}'], t, loader)
    assert res == ['bar']

    res = listify_lookup_plugin_terms(('{{ ansible }}', 1), t, loader)
    assert res == ['bar',1]


# Generated at 2022-06-13 16:28:59.325550
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins.loader import lookup_loader
    from ansible.vars.manager import DataLoader

    def create_dataloader(data_map=None):
        data_map = data_map or dict()

        def load_from_file(*args):
            data = data_map.get(args[1])
            if data:
                return data

            raise Exception("unexpected filename passed to load_from_file: %s" % args[1])


# Generated at 2022-06-13 16:29:05.561377
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    import ansible.template
    from ansible.parsing.yaml.objects import AnsibleUnicode

    terms = AnsibleUnicode('{{ lookup("env", "HOME") }}')
    templar = ansible.template.Templar(loader=None)
    listify_lookup_plugin_terms(terms, templar, None)

# Generated at 2022-06-13 16:29:13.654346
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    templar = Templar(loader=None)

    # Expect a string to be returned as a list
    assert listify_lookup_plugin_terms('test', templar, None) == ['test']

    # Expect a list to remain a list
    assert listify_lookup_plugin_terms(['test'], templar, None) == ['test']

    # Expect a tuple to be returned as a list
    assert listify_lookup_plugin_terms(('test',), templar, None) == ['test']

# Generated at 2022-06-13 16:29:22.013641
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib
    templar = Templar(loader=None, variables={'bar': 'foo'}, shared_loader_obj=None, vault_secrets=VaultLib())
    assert listify_lookup_plugin_terms('{{ foo }}', templar, None, fail_on_undefined=True) == ['{{ foo }}']
    assert listify_lookup_plugin_terms('{{ foo }}', templar, None, fail_on_undefined=False) == ['foo']
    assert listify_lookup_plugin_terms({'foo': 'bar'}, templar, None, fail_on_undefined=False) == [{'foo': 'bar'}]

# Generated at 2022-06-13 16:29:31.309830
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    variable_manager._extra_vars = {'role_path': 'a'}
    loader = DataLoader()
    templar = Templar(loader=loader, variable_manager=variable_manager)

    def check(input, expected):
        result = listify_lookup_plugin_terms(input, templar=templar)
        assert result == expected, '%r != %r' % (result, expected)

    # test various input types
    check('hello', ['hello'])
    check(['hello', 'world'], ['hello', 'world'])
    check('', [])
    check([''], [''])
   

# Generated at 2022-06-13 16:29:39.448296
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible import constants as C
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    class FakeVarsModule:
        def get_vars(self, loader, play, host, task):
            return dict(my_var=dict(foo='bar'))

    class FakeLoader:
        def get_basedir(self, host):
            return '/path/to/playbook'

    class FakeHost:
        def get_name(self):
            return 'my_host'

    class FakeTask:
        pass

    class FakePlay:
        pass


# Generated at 2022-06-13 16:29:50.639277
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.common._collections_compat import Mapping

    assert listify_lookup_plugin_terms(['a', 'b'], None, None) == ['a', 'b']
    assert listify_lookup_plugin_terms('a, b', None, None) == ['a', 'b']
    assert listify_lookup_plugin_terms(['a', '{{x}}', 'b'], DummyTemplar({'x': 10}), None) == ['a', 10, 'b']
    assert listify_lookup_plugin_terms('a, {{x}}, b', DummyTemplar({'x': 20}), None) == ['a', 20, 'b']
    assert listify_lookup_plugin_terms({'a': 10}, None, None) == {'a': 10}

# Generated at 2022-06-13 16:30:04.037344
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib
    import os

    lookup_plugin_terms_string = '{{ ansible_eth0.ipv4.address }}'
    lookup_plugin_terms_nested_string = '{{ (1, [2, "three"]) }}'
    lookup_plugin_terms_dict = {'a': 'b'}
    lookup_plugin_terms_list = [lookup_plugin_terms_string]
    lookup_plugin_terms_complex_list = ['a', lookup_plugin_terms_dict, lookup_plugin_terms_list, 'c']


# Generated at 2022-06-13 16:30:15.384798
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    # Import required modules for testing
    from ansible.parsing.yaml import objects
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.plugins.loader import lookup_loader

    # Create a fake playbook and templar
    fake_playbook = objects.AnsiblePlaybook()
    fake_play = Play().load(dict(name='test', hosts=['localhost'], gather_facts='no'), variable_manager=VariableManager(), loader=fake_playbook._loader)
    templar = Templar(loader=fake_playbook._loader, variables=fake_play.get_variable_manager())

    # Create a fake lookup plugin

# Generated at 2022-06-13 16:30:23.861982
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.module_utils.ansible_modlib.template import Templar

    templar = Templar(loader=None, variables={})

    assert listify_lookup_plugin_terms(terms='test_1', templar=templar, loader=None) == [u'test_1']
    assert listify_lookup_plugin_terms(terms=['test_1', 'test_2'], templar=templar, loader=None) == [u'test_1', u'test_2']

# Generated at 2022-06-13 16:30:27.978972
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    try:
        from ansible.module_utils.common._collections_compat import MutableMapping
    except:
        import collections as MutableMapping

    from ansible.module_utils.common._collections_compat import MutableSequence

    from ansible.template import Templar

    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject

    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.handler import Handler
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars import VariableManager

    class FakeTemplateVars(MutableMapping):
        def __init__(self):
            self._data = dict()



# Generated at 2022-06-13 16:30:31.255489
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    templar = Templar(loader=None)
    assert listify_lookup_plugin_terms(['1', 2, 3], templar) == ['1', 2, 3]


# Generated at 2022-06-13 16:30:42.370099
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible import constants as C
    from ansible.errors import AnsibleUndefinedVariable
    from ansible.template import Templar

    loader = DummyLoader()

    templar = Templar(loader=loader, variables={'foo': 'bar'})
    result = listify_lookup_plugin_terms('this is a string', templar, loader)
    assert(isinstance(result, list))
    assert(result == ['this is a string'])

    templar = Templar(loader=loader, variables={'foo': 'bar'})
    result = listify_lookup_plugin_terms(['this is a string'], templar, loader)
    assert(isinstance(result, list))
    assert(result == ['this is a string'])


# Generated at 2022-06-13 16:30:53.268657
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar
    from ansible import constants as C
    C.DEFAULT_HASH_BEHAVIOUR = 'replace'
    tmplar = Templar()

    assert listify_lookup_plugin_terms('{{ a }}', tmplar, None, convert_bare=True, fail_on_undefined=True) == ['{{ a }}']
    assert listify_lookup_plugin_terms(['{{ a }}'], tmplar, None, convert_bare=True, fail_on_undefined=True) == ['{{ a }}']
    assert listify_lookup_plugin_terms(['{{ a }}', '{{ b }}'], tmplar, None, convert_bare=True, fail_on_undefined=True) == ['{{ a }}', '{{ b }}']
    assert listify_

# Generated at 2022-06-13 16:31:00.581202
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    terms = ['a', '{{x}}', '{{y}}']
    my_vars = dict(
        x = 'X',
        y = ['Y1','Y2'],
    )

    loader = DataLoader()
    templar = Templar(loader=loader, variables=my_vars)
    new_terms = listify_lookup_plugin_terms(terms, templar, loader)

    assert new_terms == ['a', 'X', 'Y1', 'Y2'], \
        "listify_lookup_plugin_terms did not produce the expected result"

# Generated at 2022-06-13 16:31:08.404599
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    assert listify_lookup_plugin_terms(None, None, None) == []
    assert listify_lookup_plugin_terms('', None, None) == []
    assert listify_lookup_plugin_terms('str', None, None) == ['str']
    assert listify_lookup_plugin_terms([], None, None) == []
    assert listify_lookup_plugin_terms(['str1', 'str2'], None, None) == ['str1', 'str2']
    assert listify_lookup_plugin_terms(('str1', 'str2'), None, None) == ['str1', 'str2']

# Generated at 2022-06-13 16:31:18.301085
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    # Dummy classes
    class Dummy_AnsibleTemplate:
        def __init__(self):
            pass
        def template(self, data, *args, **kwargs):
            return data

    class Dummy_AnsibleLoader:
        pass

    # Test data
    test_data = [
        (None, 'null'),
        ('', 'empty'),
        (' ', 'a space'),
        ('a', ['a']),
        ('a,b,c', ['a', 'b', 'c']),
        ('a, b, c', ['a', 'b', 'c']),
        ('  a, b  , c ', ['a', 'b', 'c']),
        (['a', 'b', 'c'], ['a', 'b', 'c']),
    ]


# Generated at 2022-06-13 16:31:37.421185
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    templar = Templar(loader=loader)

    assert listify_lookup_plugin_terms('foo', templar, loader) == ['foo']
    assert listify_lookup_plugin_terms(['foo'], templar, loader) == ['foo']
    assert listify_lookup_plugin_terms(['foo', 'bar'], templar, loader) == ['foo', 'bar']

    assert listify_lookup_plugin_terms('foo bar', templar, loader) == ['foo bar']
    assert listify_lookup_plugin_terms(['foo bar'], templar, loader) == ['foo bar']

# Generated at 2022-06-13 16:31:48.289913
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    import os
    import pytest

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.extra_vars = {
        'user': 'root'
    }
    inventory = variable_manager.get_inventory()
    variable_manager.set_inventory(inventory)

    context = PlayContext()
    templar = Templar(loader=loader, variables=variable_manager,
                      shared_loader_obj=False, fail_on_undefined=True)

    terms = '{{ [1, 2] }}'

# Generated at 2022-06-13 16:31:56.828503
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.vault import VaultLib
    from ansible.template import Templar
    from ansible.errors import AnsibleError
    from ansible.plugins.loader import lookup_loader


# Generated at 2022-06-13 16:32:03.169083
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.parsing.yaml.loader import AnsibleLoader
    loader = AnsibleLoader(None, None)

    templar = Templar(loader=loader, variables={})

    assert listify_lookup_plugin_terms("hello", templar, loader) == ["hello"]
    assert listify_lookup_plugin_terms("hello,world", templar, loader) == ["hello,world"]

    assert listify_lookup_plugin_terms(["{{foo}}", "{{bar}}"], templar, loader) == ["{{foo}}", "{{bar}}"]

# Generated at 2022-06-13 16:32:14.121584
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    # Importing here to avoid circular import
    from ansible.template import Templar 

    templar = Templar()
    loader = None

    # Terms is None
    terms = None
    new_terms = listify_lookup_plugin_terms(terms, templar, loader)
    assert new_terms == []

    # Terms is a list
    terms = ['foo', 'bar']
    new_terms = listify_lookup_plugin_terms(terms, templar, loader)
    assert new_terms == terms

    # Terms is a string
    terms = 'foo'
    new_terms = listify_lookup_plugin_terms(terms, templar, loader)
    assert new_terms == ['foo']

    # Templates

# Generated at 2022-06-13 16:32:22.688696
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from jinja2 import Template

    class FakeTemplar:
        def __init__(self):
            pass

        def template(self, data, **kwargs):
            return Template(data).render(kwargs)

    templar = FakeTemplar()

    assert listify_lookup_plugin_terms(("{{ var }}", "{{ other_var }}"), templar, None, fail_on_undefined=True, convert_bare=False) == ["bar", "biz"]
    assert listify_lookup_plugin_terms("{{ var }}", templar, None, fail_on_undefined=True, convert_bare=False) == ["bar"]
    assert listify_lookup_plugin_terms(("foo", "bar"), templar, None, fail_on_undefined=True, convert_bare=False)

# Generated at 2022-06-13 16:32:32.445016
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    # Convert to string
    assert listify_lookup_plugin_terms(40, None, None) == '40'
    # Convert to list
    assert listify_lookup_plugin_terms(40, None, None, convert_bare=True) == [40]
    # String is already a list
    assert listify_lookup_plugin_terms('40', None, None) == ['40']
    # String is not a list
    assert listify_lookup_plugin_terms([40], None, None) == [40]
    # List is already a list
    assert listify_lookup_plugin_terms(['40'], None, None) == ['40']
    # List is already a list
    assert listify_lookup_plugin_terms([40], None, None) == [40]
    # Convert to list
    assert list

# Generated at 2022-06-13 16:32:40.832037
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    import ansible.constants as C
    C.HOST_KEY_CHECKING = False
    loader = DataLoader()
    terms = '{{hostvars[inventory_hostname]["ansible_mounts"]}}'
    myvars = {'hostvars': {'localhost': {'ansible_mounts': 'test'}}}
    templar = Templar(loader=loader, variables=myvars)
    assert listify_lookup_plugin_terms(terms, templar, loader) == ['test']
    terms = '{{hostvars[inventory_hostname]}}'
    myvars = {'hostvars': {'localhost': 'test'}}

# Generated at 2022-06-13 16:32:49.940200
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    # FIXME: this test fails if the source files containing the classes/functions
    #        are not in PYTHONPATH
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    import ansible.constants as C

    loader = DataLoader()

    inventory = InventoryManager(loader=loader, sources=C.DEFAULT_HOST_LIST)
    variable_manager = VariableManager(loader=loader, inventory=inventory)


# Generated at 2022-06-13 16:32:57.251224
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    import ansible.parsing.yaml.objects
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.template import Templar
    yaml_loader = AnsibleLoader(None, array_constructor=ansible.parsing.yaml.objects.AnsibleSequence)
    templar = Templar(loader=yaml_loader)
    assert ["foo", "bar"] == listify_lookup_plugin_terms(["foo", "bar"], templar, yaml_loader)
    assert ["foo"] == listify_lookup_plugin_terms("foo", templar, yaml_loader)

# Generated at 2022-06-13 16:33:22.556546
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    vars_mgr = VariableManager()
    loader = DataLoader()

    from ansible.template import Templar
    templar = Templar(loader=loader, variables=vars_mgr)

    from ansible.utils.vars import merge_hash
    vars_mgr._vars = merge_hash(vars_mgr._vars, {'a': 'foobar'})

    vars_mgr._vars = merge_hash(vars_mgr._vars, {'b': 'foobar'})
    vars_mgr._vars = merge_hash(vars_mgr._vars, {'c': 'foobar'})
    vars_mgr._vars = merge

# Generated at 2022-06-13 16:33:30.361074
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template.template import Templar
    from ansible.vars.manager import VariableManager
    assert listify_lookup_plugin_terms(
        terms='{ foo }',
        templar=Templar(variables=VariableManager()),
        loader=None,
    ) == ['{ foo }']

    assert listify_lookup_plugin_terms(
        terms=['{ foo }'],
        templar=Templar(variables=VariableManager()),
        loader=None,
    ) == ['{ foo }']

    assert listify_lookup_plugin_terms(
        terms=['foo', '{ bar }'],
        templar=Templar(variables=VariableManager()),
        loader=None,
    ) == ['foo', '{ bar }']

# Generated at 2022-06-13 16:33:41.189479
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
  from ansible.template.safe_eval import safe_eval
  from ansible.template import Templar
  safe_eval_env = safe_eval.copy()

  # Test list

# Generated at 2022-06-13 16:33:49.342498
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.utils.vars import combine_vars

    from io import StringIO

    # Fake variables to use in testing
    fake_inventory = """
    [webservers]
    testhost1
    testhost2
    """

    v = VariableManager()
    loader = DataLoader()
    inv = InventoryManager(loader=loader, sources=StringIO(fake_inventory))
    v.add_inventory(inv)
    play = Play().load({}, variable_manager=v, loader=loader)
    t = Templar(loader=loader, variables=v)
    v

# Generated at 2022-06-13 16:33:59.497654
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.plugins.loader import lookup_loader

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)


# Generated at 2022-06-13 16:34:09.513363
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    import ansible.template

    env = ansible.template.Environment(undefined=ansible.template.AnsibleUndefined)

    # Test single term and string
    assert listify_lookup_plugin_terms('foobar', env, None, fail_on_undefined=False) == ['foobar']
    assert listify_lookup_plugin_terms(['foobar'], env, None, fail_on_undefined=False) == ['foobar']
    assert listify_lookup_plugin_terms(['foobar', 'foobaz'], env, None, fail_on_undefined=False) == ['foobar', 'foobaz']

    # Test with undefined variable
    assert listify_lookup_plugin_terms('{{testvar}}', env, None, fail_on_undefined=False) == ['']

# Generated at 2022-06-13 16:34:16.497737
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.yaml.loader import AnsibleLoader

    loader = AnsibleLoader(None, '<string>')
    templar = Templar(loader=loader)
    terms = ['a']
    terms = listify_lookup_plugin_terms(terms, templar, loader)
    assert terms == ['a']

    terms = 'b'
    terms = listify_lookup_plugin_terms(terms, templar, loader)
    assert terms == ['b']

    terms = 'c'
    terms = listify_lookup_plugin_terms(terms, templar, loader, convert_bare=True)
    assert terms == ['c']

    terms = 'd'

# Generated at 2022-06-13 16:34:28.628167
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    templar = None

    # Create a test object to use in these tests
    class TestObject(object):

        def __init__(self):
            self.val = None

    test_value = TestObject()

    # Test single values
    assert listify_lookup_plugin_terms('one', templar, None) == ['one']
    assert listify_lookup_plugin_terms(1, templar, None) == [1]
    assert listify_lookup_plugin_terms(test_value, templar, None, fail_on_undefined=True) == [None]
    assert listify_lookup_plugin_terms(test_value, templar, None, fail_on_undefined=False) == [None]

    # Test lists and tuples
    assert listify_lookup_plugin_terms

# Generated at 2022-06-13 16:34:37.844281
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    import ansible.parsing.yaml.loader
    from ansible.template import Templar

    yaml_loader = ansible.parsing.yaml.loader.AnsibleLoader

    # string_args examples
    assert listify_lookup_plugin_terms('string_args', Templar(loader=yaml_loader)) == ['string_args']
    assert listify_lookup_plugin_terms('string_args', Templar(loader=yaml_loader), convert_bare=True) == ['string_args']
    assert listify_lookup_plugin_terms('string_args', Templar(loader=yaml_loader), fail_on_undefined=False) == ['string_args']

    # list_args examples

# Generated at 2022-06-13 16:34:46.500775
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.template import Templar

    templar = Templar(loader=None, variables={})
    assert listify_lookup_plugin_terms(['one', 'two', 'three'], templar, None) == ['one', 'two', 'three']
    assert listify_lookup_plugin_terms('one', templar, None) == ['one']
    assert listify_lookup_plugin_terms('[1, 2, 3]', templar, None) == ['[1, 2, 3]']
    assert listify_lookup_plugin_terms('one two three', templar, None) == ['one', 'two', 'three']