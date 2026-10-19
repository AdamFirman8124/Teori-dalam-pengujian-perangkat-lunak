

# Generated at 2022-06-13 16:25:12.411204
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleUnicode
    from ansible.template import Templar

    loader = AnsibleLoader(None, dict())

    # Test the output from listify_lookup_plugin_terms
    # when the input is a string
    input_string = '{{ hostname }}'
    templar = Templar(loader=loader)
    output_string = listify_lookup_plugin_terms(input_string, templar)
    assert isinstance(output_string, list)
    assert isinstance(output_string[0], string_types)

    # Test the output from listify_lookup_plugin_terms
    # when the input is a list of strings

# Generated at 2022-06-13 16:25:21.716669
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from jinja2 import Template
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop
    from ansible.utils.vars import combine_vars
    from ansible.template import Templar

    # use the data loader to mock the lookup
    lookup_loader = DictDataLoader({
        '/path/to/template.j2': "{{ item }}\n",
    })
    templar = Templar(loader=lookup_loader, variables=combine_vars(None, load_extra_vars=False), shared_loader_obj=lookup_loader)

    # test cases
    simple_strings = ['item1', 'item2']
    complex_strings = ['item1', '{{ test_var }}']

# Generated at 2022-06-13 16:25:28.455067
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.module_utils.common._collections_compat import Sequence

    from ansible.template.safe_eval import SafeEval
    from ansible.template import Templar

    from ansible.parsing.dataloader import DataLoader

    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.role.include import Include
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.task_include import TaskInclude
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager

    loader = DataLoader()

    inventory = Host(name="foobar")

# Generated at 2022-06-13 16:25:34.831202
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    templar = Templar(loader=None, variables={})

    assert listify_lookup_plugin_terms('foo', templar, None) == ['foo']
    assert listify_lookup_plugin_terms(['foo'], templar, None) == ['foo']
    assert listify_lookup_plugin_terms(['foo', 'bar'], templar, None) == ['foo', 'bar']

# Generated at 2022-06-13 16:25:43.263711
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib
    from ansible.utils.vars import combine_vars

    def get_loader(data):
        loader = DictDataLoader({'': data})
        vault_secrets = [('default', VaultLib([('default', 'secret')]))]
        loader.set_vault_secrets(vault_secrets)
        return loader

    class DictVarManager:
        def __init__(self):
            self.vars = {'a': 1, 'b': 2, 'c': 3}

        def get_vars(self, play=None, host=None, task=None, include_hostvars=False, include_delegate_to=False):
            return self.vars


# Generated at 2022-06-13 16:25:54.884549
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.errors import AnsibleUndefinedVariable
    from ansible.template import Templar

    templar = Templar(loader=None, variables={'a': 'foo', 'b': 'bar'})

    assert listify_lookup_plugin_terms('{{a}}', templar, None) == ['foo']
    assert listify_lookup_plugin_terms(['{{a}}', '{{b}}'], templar, None) == ['foo', 'bar']
    assert listify_lookup_plugin_terms({'a': '{{b}}'}, templar, None) == [{'a': 'bar'}]

    # multiple expansions

# Generated at 2022-06-13 16:26:02.672583
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    import jinja2
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    variable_manager = VariableManager()
    loader = DataLoader()

    # Setup the jinja2 environment
    variable_manager.set_inventory(loader.load_inventory('localhost,'))
    variable_manager.extra_vars = {'one': 'string'}
    play_context = PlayContext()
    jinja2_env = variable_manager.get_jinja_environment()
    templar = Templar(loader=loader, variables=variable_manager,
                      shared_loader_obj=jinja2_env)

    # Test methods with a bare variable
    assert listify

# Generated at 2022-06-13 16:26:12.988058
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar


# Generated at 2022-06-13 16:26:20.190235
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    terms = [ "{{ foo }}{{ bar }}", '{{ bam }}' ]
    templar = Templar(loader=None, variables={'foo': "Z", 'bar': "Y", 'bam': "X"})

    assert listify_lookup_plugin_terms(terms, templar, None) == ["ZY", "X"]

    terms = "{{ foo }}{{ bar }}"
    templar = Templar(loader=None, variables={'foo': "Z", 'bar': "Y"})

    assert listify_lookup_plugin_terms(terms, templar, None) == ["ZY"]



# Generated at 2022-06-13 16:26:31.642746
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext()

    t = Templar(loader=loader, variables=variable_manager, fail_on_undefined=True)

    # simple test
    assert listify_lookup_plugin_terms(["a", "b"], templar=t, loader=loader, fail_on_undefined=True, convert_bare=False) == ["a", "b"]

    # test complex data

# Generated at 2022-06-13 16:26:43.378132
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.parsing.utils.yaml import from_yaml
    from ansible.template import Templar

    data = """
        foo:
          - one
          - two
          - three

        bar:
          - a
          - b:
              c: 1
              d: 2
    """
    data = from_yaml(data)
    templar = Templar(loader=None, variables=data)

    assert listify_lookup_plugin_terms('foo', templar, None) == data["foo"]
    assert listify_lookup_plugin_terms('bar.b', templar, None) == [data["bar"][0], data["bar"][1]]

# Generated at 2022-06-13 16:26:50.521711
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.module_utils._text import to_text
    from ansible.template import Templar

    my_vars = dict(
        foo = "bar",
        list_var = ["1","2","3"],
        ansible_facts = dict(
            ansible_all_ipv4_addresses = ["192.168.2.1", "192.168.2.2"],
            ansible_hostname = "myhostname",
        )
    )

    my_loader = DictDataLoader({})
    my_templar = Templar(loader=my_loader, variables=my_vars)


# Generated at 2022-06-13 16:26:59.821943
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    MockVarsModule = {
      'bar': 'foo',
      'blah': ['alpha', 'beta']
    }

    templar = Templar(loader=None, variables=MockVarsModule)

    assert listify_lookup_plugin_terms('foo', templar, None) == ['foo']
    assert listify_lookup_plugin_terms(['foo', 'bar'], templar, None) == ['foo', 'bar']
    assert listify_lookup_plugin_terms(['foo', '{{bar}}'], templar, None) == ['foo', 'foo']
    assert listify_lookup_plugin_terms('{{blah}}', templar, None) == ['alpha', 'beta']

# Generated at 2022-06-13 16:27:07.913341
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    '''
    function listify_lookup_plugin_terms

    '''
    terms = "{{ file_contents }}"
    templar = dict()
    templar['template'] = lambda args, **kwargs : args
    loader = dict()
    fail_on_undefined = True
    convert_bare = False

    results = listify_lookup_plugin_terms(terms, templar, loader,
                                          fail_on_undefined, convert_bare)
    assert(results == "{{ file_contents }}")

    terms = ["{{ prefix }}file_names","{{ suffix }}"]
    templar = dict()
    templar['template'] = lambda args, **kwargs : args
    loader = dict()
    fail_on_undefined = True
    convert_bare = False

    results = list

# Generated at 2022-06-13 16:27:18.181578
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    variables = dict(foo='this is some string')

    templar = Templar(variables)

    # Test 1:
    # Listify a string
    test_str = 'this is a test string'
    test_str_list = listify_lookup_plugin_terms(test_str, templar, dict())
    assert isinstance(test_str_list, list)
    assert len(test_str_list) == 1
    assert 'this is a test string' == test_str_list[0]

    # Test 2:
    # Listify a string that has a newline in it
    test_str = 'this is a test string\nwith a newline in it'

# Generated at 2022-06-13 16:27:27.921770
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    # The function tested
    from ansible.module_utils.common.lookup_plugins import listify_lookup_plugin_terms

    # Input data
    data = ['{{ foo }}', '{{ bar }}', '{{ baz }}']

    # We will override the templar in this way
    class Templar:

        def template(self, terms, convert_bare=False, fail_on_undefined=True):

            # Self-test
            assert convert_bare == False, 'convert_bare parameter not ignored'
            assert fail_on_undefined == True, 'fail_on_undefined parameter not ignored'

            # {{ foo }} --> ['FOO']
            # {{ bar }} --> 'BAR'
            # {{ baz }} --> 'BAZ'

# Generated at 2022-06-13 16:27:40.393944
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    # dummy terms,
    terms = [123]
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    templar = variable_manager.get_template_class(fail_on_undefined=False)

    # no change for non-string/non-iterable non-string/iterable values
    for value in [123, [123]]:
        result = listify_lookup_plugin_terms(value, templar, loader)
        assert isinstance(result, list)
        assert result == [123]

    # non-templ

# Generated at 2022-06-13 16:27:49.398464
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.vars.unsafe_proxy import UnsafeProxy

    class DummyUnsafe(str):
        pass

    from ansible.template import Templar

    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    p = PlayContext()
    loader = None
    templar = Templar(loader=loader, variables={'other': 'value'})
    templar._available_variables = {'var1': 'Value1', 'var2': ['Value2', 'Value3'], 'list': [1, 2, 3]}
    templar.set_available_variables(variables=templar._available_variables)

    # single value

# Generated at 2022-06-13 16:28:00.860327
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    # First 3 parameters of listify_lookup_plugin_terms are not checked
    # on unit tests
    class DummyTemplar(object):
        def __init__(self):
            pass

        class DummyLoader(object):
            def __init__(self):
                pass

        def template(self, terms, fail_on_undefined=True):
            if isinstance(terms, string_types) or not isinstance(terms, Iterable):
                return [terms]
            else:
                return terms

    templar = DummyTemplar()
    loader = DummyTemplar.DummyLoader()

    assert listify_lookup_plugin_terms(None, templar, loader) == [None]
    assert listify_lookup_plugin_terms([None], templar, loader) == [None]


# Generated at 2022-06-13 16:28:06.491788
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    assert listify_lookup_plugin_terms('foo', Templar(), None) == ['foo']
    assert listify_lookup_plugin_terms('foo bar', Templar(), None) == ['foo', 'bar']
    assert listify_lookup_plugin_terms(['foo', 'bar'], Templar(), None) == ['foo', 'bar']
    assert listify_lookup_plugin_terms('{{foo}}', Templar(), None, convert_bare=True) == ['{{foo}}']
    assert listify_lookup_plugin_terms('{{"foo"}}', Templar(), None, convert_bare=True) == ['foo']

# Generated at 2022-06-13 16:28:15.591930
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager

    templar = Templar(loader=None, variables=VariableManager(), host=Host())
    results = listify_lookup_plugin_terms('foo', templar, None)
    assert results == ['foo']

    results = listify_lookup_plugin_terms([ 'foo' ], templar, None)
    assert results == ['foo']



# Generated at 2022-06-13 16:28:27.542366
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.module_utils import basic
    from ansible.template import Templar

    class Options(object):
        """ options class for testing purposes """
        def __init__(self, val=None):
            self.module_vars = dict()
            self.connection  = 'local'
            self.module_name = 'basic'
            if val:
                self.module_vars['test_val'] = val

    def load_module(name):
        return basic

    class TestVarsModule(object):
        """ vars plugin for testing purposes """
        def get(self, key, default=None, boolean=False, integer=False, floating=False, complex=False):
            return key

    templar = Templar(loader=None, variables=Options('test_val'), shared_loader_obj=None)
    templar

# Generated at 2022-06-13 16:28:37.853434
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    import ansible.template
    import ansible.vars
    import ansible.parsing.yaml.loader
    import jinja2

    my_vars = ansible.vars.VariableManager()
    my_loader = ansible.parsing.yaml.loader.AnsibleLoader(None, variable_manager=my_vars)
    my_templar = ansible.template.Template(loader=my_loader, variable_manager=my_vars)

    # test with a single value
    result = listify_lookup_plugin_terms('foo', my_templar, my_loader)
    assert result == ['foo']

    # test with a list
    result = listify_lookup_plugin_terms(['foo', 'bar'], my_templar, my_loader)
    assert result

# Generated at 2022-06-13 16:28:46.709472
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    loader = DictDataLoader({
        "test.j2": "test {{ terms }}",
    })

    templar = Templar(loader=loader, variables={
        "terms": ["simple", "list", "of", "terms"]
    })

    assert listify_lookup_plugin_terms("{{ terms }}", templar, loader) == ["simple", "list", "of", "terms"]
    assert listify_lookup_plugin_terms("{{ terms }}", templar, loader, convert_bare=True) == ["simple", "list", "of", "terms"]
    assert listify_lookup_plugin_terms(["{{ terms }}"], templar, loader) == ["simple", "list", "of", "terms"]

# Generated at 2022-06-13 16:28:53.759201
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    """
    This should return a list, but with a single string element
    """
    from ansible.utils.display import Display
    from ansible.template import Templar
    from ansible.parsing.yaml.loader import AnsibleLoader
    display = Display()
    display.verbosity = 3

    loader = AnsibleLoader(None, sort_keys=True)
    templar = Templar(loader=loader, variables={})

    # Single term
    assert listify_lookup_plugin_terms('foo', templar, loader) == ['foo']

    # A list
    assert listify_lookup_plugin_terms(['foo','bar'], templar, loader) == ['foo','bar']

    # A dict
    assert listify_lookup_plugin_terms({'foo':'bar'}, templar, loader)

# Generated at 2022-06-13 16:29:02.812536
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    # testing simple string
    test_string = "test"
    expected = ['test']
    assert expected == listify_lookup_plugin_terms(test_string, None, None)

    # testing list of strings
    test_list = ["test1", "test2"]
    expected = ['test1', 'test2']
    assert expected == listify_lookup_plugin_terms(test_list, None, None)

    # testing list with single item
    test_list = ["test1"]
    expected = ['test1']
    assert expected == listify_lookup_plugin_terms(test_list, None, None)

    # test list with empty string as last item
    test_list = ["test1", ""]
    expected = ['test1', ""]

# Generated at 2022-06-13 16:29:11.646226
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    assert listify_lookup_plugin_terms('foo') == ['foo']
    assert listify_lookup_plugin_terms(['foo']) == ['foo']
    assert listify_lookup_plugin_terms(('foo',)) == ['foo']
    assert listify_lookup_plugin_terms(('foo', 'bar')) == ['foo', 'bar']
    assert listify_lookup_plugin_terms(('foo', ['bar'])) == ['foo', 'bar']

    templar = Templar(loader=None, variables={'a': 'A', 'b': ['B1', 'B2']})
    assert listify_lookup_plugin_terms('{{a}}', templar) == ['A']

# Generated at 2022-06-13 16:29:21.043415
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    # The following tests require that the lookup plugin is initialized
    from ansible.plugins.lookup import LookupBase
    lb = LookupBase()
    lb.basedir = '.'
    lb.templar = lb._templar_class()

    assert listify_lookup_plugin_terms(1, lb.templar, lb.loader) == [1]
    assert listify_lookup_plugin_terms("1", lb.templar, lb.loader) == [1]
    assert listify_lookup_plugin_terms("foo", lb.templar, lb.loader) == ['foo']
    assert listify_lookup_plugin_terms("{{ 1 }}", lb.templar, lb.loader) == [1]

# Generated at 2022-06-13 16:29:30.853033
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    fake_loader = DictDataLoader({})
    fake_variable_manager = DictDataManager()
    fake_inventory = DictInventory()

    templar = Templar(loader=fake_loader,
                      variables=fake_variable_manager,
                      inventory=fake_inventory)

    pc = PlayContext()
    templar._set_context(pc)

    # test it works with a single string
    result = listify_lookup_plugin_terms(terms='{{key}}', templar=templar, loader=fake_loader)
    assert result == ['key']

    # test it works with a single term (unified)

# Generated at 2022-06-13 16:29:39.425963
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.vars.manager import VariableManager

    templar = Templar(loader=AnsibleLoader(None),
                      variables=VariableManager(loader=AnsibleLoader(None)))
    terms = listify_lookup_plugin_terms(terms='one', templar=templar, loader=AnsibleLoader(None))
    assert terms == ['one']

    terms = listify_lookup_plugin_terms(terms='one two', templar=templar, loader=AnsibleLoader(None))
    assert terms == ['one two']


# Generated at 2022-06-13 16:29:53.885005
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    class FakeModule:
        def __init__(self, params, ansible_module_args):
            self.params = params
            self.ansible_module_args = ansible_module_args
        def fail_json(self, **kwargs):
            raise Exception(kwargs['msg'])

    class FakeTemplar:
        def __init__(self, params_dict):
            self.params = params_dict
        def template(self, data, fail_on_undefined=True, convert_bare=False):
            return data

    test_params = ['a', 'b', 'c', None, '', 'd', ['e', 'f'], ['', 'g', 'h']]
    expected = ['a', 'b', 'c', None, '', 'd', 'e,f', 'g,h']
   

# Generated at 2022-06-13 16:30:02.920059
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    '''Assert that listify_lookup_plugin_terms converts lookup terms to a list'''
    from ansible.plugins.loader import lookup_loader
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    data = '''
    test_variable:
      - 1
      - 2
    '''

    data_loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.extra_vars = {'lookup_plugin_terms': {'test_list': [1, 2]}}
    inventory = variable_manager.get_inventory()
    variable_manager.set_inventory(inventory)

    loader = data_loader.load_from_strings(data)

# Generated at 2022-06-13 16:30:10.656665
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    templar = Templar(loader=None, variables={})

    terms = listify_lookup_plugin_terms(None, templar, None)
    assert terms == [], terms

    terms = listify_lookup_plugin_terms('a', templar, None)
    assert terms == ['a'], terms

    terms = listify_lookup_plugin_terms(['a'], templar, None)
    assert terms == ['a'], terms

    terms = listify_lookup_plugin_terms(['a', 'b'], templar, None)
    assert terms == ['a', 'b'], terms

    terms = listify_lookup_plugin_terms(['a', 'b', 'c'], templar, None)

# Generated at 2022-06-13 16:30:19.014923
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    # Just need to get some templar and loader objects
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    loader = DataLoader()
    vars = VariableManager()
    templar = Templar(loader=loader, variables=vars)

    # Test regular string input
    input_terms = "hello_world"
    expected_output = ['hello_world']
    assert listify_lookup_plugin_terms(input_terms, templar, loader) == expected_output

    # Test list input
    input_terms = ["hello_world", "goodbye_world"]
    expected_output = ['hello_world', 'goodbye_world']

# Generated at 2022-06-13 16:30:30.501319
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    terms = [
        'a',
        ['b', 'c'],
        '{{d}} e',
        ['{{f}}', '{{g}}'],
        '{{h.i}}',
        ['{{j.k}}', '{{l.m}}'],
    ]
    templar = Templar(loader=DataLoader(), variables={
        'd': 'x',
        'f': 'y',
        'g': 'z',
        'h': ['o', 'p'],
        'i': 2,
        'j': {'k': 'q'},
        'l': {'m': 'r'},
    })


# Generated at 2022-06-13 16:30:41.756242
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    # Importing modules locally to avoid dependencies when running standalone tests
    from ansible.module_utils._text import to_text
    from ansible.template import Templar

    # Importing module to get the fixture data (Test data)
    from ansible_collections.community.general.tests.unit.compat.mock import MagicMock
    from ansible_collections.community.general.tests.unit.compat.mock import patch


# Generated at 2022-06-13 16:30:52.688136
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    """
    Test if listify works
    """

    from ansible.template import Templar

    class MyVarManager:
        def get_vars(self, loader, play, host=None, task=None, include_hostvars=True, include_delegate_to=True):
            return dict(
                x=dict(
                    y=10,
                )
            )

    v = MyVarManager()
    t = Templar(loader=None, variables=v)

    terms = 3
    terms = listify_lookup_plugin_terms(terms, templar=t, loader=None)
    assert terms == [3]

    terms = ["A", "B", "C"]
    terms = listify_lookup_plugin_terms(terms, templar=t, loader=None)

# Generated at 2022-06-13 16:30:58.716578
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template.safe_eval import safe_eval
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.template import Templar

    templar = Templar(loader=None)

    yaml_data = u"""
        - foo: "{{ lookup('env','HOME') }}/foo"
        - foo:
            - "{{ lookup('env','HOME') }}/foo"
            - "{{ lookup('env','HOME') }}/bar"
        - foo: "{{ lookup('env','HOME') }}/{{lookup('env','USER')}}/foo"
    """

    results = safe_eval(yaml_data)

    for terms in results:
        assert isinstance(terms, dict)
        for k, v in terms.items():
            terms[k] = listify_lookup_plugin

# Generated at 2022-06-13 16:31:02.538994
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    assert listify_lookup_plugin_terms(['a', 'b'], None, None) == ['a', 'b']
    assert listify_lookup_plugin_terms('a,b', None, None) == ['a', 'b']
    assert listify_lookup_plugin_terms('a, b', None, None) == ['a', 'b']
    assert listify_lookup_plugin_terms('a b', None, None) == ['a b']
    assert listify_lookup_plugin_terms('a,b c', None, None) == ['a,b c']
    assert listify_lookup_plugin_terms('a b,c', None, None) == ['a b,c']

# Generated at 2022-06-13 16:31:10.157702
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    # simple strings that should be converted to lists
    assert listify_lookup_plugin_terms("test", None, None) == ["test"]
    assert listify_lookup_plugin_terms("test,test2", None, None) == ["test","test2"]

    # if the string has newlines, it should become a multiline list
    assert listify_lookup_plugin_terms("test\ntest2", None, None) == ["test", "test2"]

    # make sure a raw list gets returned as a list
    assert listify_lookup_plugin_terms(["test", "test2"], None, None) == ["test", "test2"]

# Generated at 2022-06-13 16:31:30.423789
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.vars import VariableManager
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.errors import AnsibleUndefinedVariable

    loader = DataLoader()
    variable_manager = VariableManager()

    variable_manager.set_host_variable('host1', dict())
    variable_manager.set_host_variable('host2', dict())

    variable_manager.set_host_variable(None, dict(v1=['a', 'b', 'c'], v2='v2', v3='{{v1}}'))

    templar = Templar(loader, variable_manager)

    # Same values
    assert listify_lookup_plugin_terms([1, 2, 3], templar, loader) == [1, 2, 3]
    assert list

# Generated at 2022-06-13 16:31:37.668433
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar

    templar = Templar(loader=None, variables={'var1': 'foo', 'var2': 'bar'})

    # Test string
    assert listify_lookup_plugin_terms('"{{ var1 }}"', templar, loader=None) == ['foo']

    # Test list of strings
    assert listify_lookup_plugin_terms(["bar", "{{ var1 }}"], templar, loader=None) == ['bar', 'foo']

    # Test list of mixed strings and lists
    assert listify_lookup_plugin_terms(["bar", ["baz", "{{ var2 }}"]], templar, loader=None) == ['bar', ['baz', 'bar']]

    # Test list of lists of mixed strings and lists
    assert listify_lookup_plugin_terms

# Generated at 2022-06-13 16:31:45.260945
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar
    from ansible.utils.vars import combine_vars

    def _test(t):
        var_manager = VariableManager()
        var_manager.extra_vars = combine_vars(loader=None, variables=dict())

        templar = Templar(loader=None, variables=var_manager)

        listify_lookup_plugin_terms(t, templar, loader=None)

    assert _test([u'foo', u'bar']) == [u'foo', u'bar']
    assert _test([u'foo', [u'bar', u'baz']]) == [u'foo', [u'bar', u'baz']]

# Generated at 2022-06-13 16:31:53.652513
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.vars.unsafe_proxy import UnsafeProxy, wrap_var

    class TestTemplar(object):
        def template(self, data):
            return 'templar:'+str(data)

    class TestLoader(object):
        def __init__(self):
            self.vars = dict(
                val1='val1',
                val2='val2',
                val3='val3',
                val4=[ 'list', 'of', 'things' ],
                val5=dict(
                    foo='bar',
                    biz='baz'
                )
            )
            self.vars = wrap_var(self.vars)

    t = TestTemplar()
    l = TestLoader()


# Generated at 2022-06-13 16:32:01.644836
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    assert listify_lookup_plugin_terms("a", None, None) == ["a"]
    assert listify_lookup_plugin_terms(["a"], None, None) == ["a"]
    assert listify_lookup_plugin_terms(("a",), None, None) == ["a"]
    assert listify_lookup_plugin_terms("a,b", None, None) == ["a,b"]
    assert listify_lookup_plugin_terms(["a","b"], None, None) == ["a","b"]
    assert listify_lookup_plugin_terms(("a","b"), None, None) == ["a","b"]
    assert listify_lookup_plugin_terms("a,b,c", None, None) == ["a,b,c"]

# Generated at 2022-06-13 16:32:13.042061
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.module_utils.six import PY3
    from ansible.template import Templar

    # Python 2: strings are bytes
    if not PY3:
        assert listify_lookup_plugin_terms('string') == ['string']

        assert listify_lookup_plugin_terms(b'string') == ['string']

    # Python 3: byte string is b'string' (b is byte)
    if PY3:
        assert listify_lookup_plugin_terms('string') == ['string']

        assert listify_lookup_plugin_terms(b'string') == [b'string']

    # Force python 2 to evaluate a unicode string.
    if not PY3:
        assert listify_lookup_plugin_terms(u'string') == ['string']

    # Bytes

# Generated at 2022-06-13 16:32:22.585061
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    from units.mock.loader import DictDataLoader

    from units.mock.path import mock_unfrackpath_noop
    from ansible.parsing.dataloader import DataLoader

    t = dict(
        AnsibleUnsafeText=AnsibleUnsafeText,
    )

    loader = DataLoader()
    loader.set_basedir(os.path.join(os.path.dirname(__file__), 'loader'))

    input_terms = ["foo", "bar", "{{ lookup('pipe','yes') }}"]
    expected_output = ["foo", "bar", "yes"]

    output = listify_lookup_plugin_terms(input_terms, t, loader)
    assert output == expected_output

# Generated at 2022-06-13 16:32:28.599069
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from units.mock.loader import DictDataLoader

    #mock templar class
    class TemplateClass:

        def __init__(self):
            self.loader = DictDataLoader({
                "template.j2": "{{ value }}"
            })

        def template(self, value, convert_bare=False, fail_on_undefined=True):
            #mock the templar method to return just the value
            return value

    #initialize the templar class
    templar = TemplateClass()

    #test the listify_lookup_plugin_terms function and return values

    #define the mock loader class
    loader = DictDataLoader({
        "vars/main.yml": "value: value"
    })

    #test terms as string and convert_bare=True

# Generated at 2022-06-13 16:32:39.180220
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    try:
        if not getattr(__builtins__, '__ansible_test_mock', False):
            from ansible.module_utils.common._collections_compat import Sequence
        mock = False
    except ImportError:
        from ansible.utils.unsafe_proxy import AnsibleUnsafeText
        from collections import Sequence
        AnsibleUnsafeText.mock_class("my_str")
        mock = True

    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager()

    from ansible.template import Templar
    templar=Templar(loader=loader, variables=variable_manager)


# Generated at 2022-06-13 16:32:48.471912
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.utils.lookup_plugins import LookupBase

    plugin = LookupBase()
    terms = '{{ foo }}'
    result = listify_lookup_plugin_terms(terms, plugin, plugin)
    assert result == [u'{{ foo }}']

    terms = ['{{ foo }}', '{{ bar }}']
    result = listify_lookup_plugin_terms(terms, plugin, plugin)
    assert result == [u'{{ foo }}', u'{{ bar }}']

    terms = [u'one', u'two', u'three']
    result = listify_lookup_plugin_terms(terms, plugin, plugin)
    assert result == [u'one', u'two', u'three']

# Generated at 2022-06-13 16:33:21.361368
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.template.vars import AnsibleVars
    from ansible.vars.manager import VariableManager

    '''
    check basic functionality
    '''
    templar = Templar(loader=None, variables=AnsibleVars(variable_manager=VariableManager()))
    terms = listify_lookup_plugin_terms('{{ foo }}', templar=templar, loader=None, fail_on_undefined=True)
    assert isinstance(terms, list)
    assert terms[0] == '{{ foo }}'

    '''
    check with a list
    '''
    # no need to actually template here, just checking list handling

# Generated at 2022-06-13 16:33:29.977773
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    string_result = listify_lookup_plugin_terms('{{ lookup("env", "HOME") }}', None, None, convert_bare=True, fail_on_undefined=True)
    assert isinstance(string_result, list)
    assert len(string_result) == 1

    list_result = listify_lookup_plugin_terms('{{ lookup("env", "HOME") }}, {{ lookup("env", "HOME") }}', None, None, convert_bare=True, fail_on_undefined=True)
    assert isinstance(list_result, list)
    assert len(list_result) == 2


# Generated at 2022-06-13 16:33:41.074437
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.template.safe_eval import unsafe_eval

    # Initialize the templar
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    play_context = PlayContext()
    templar = Templar(loader=None, variables=dict(a=42), shared_loader_obj=play_context)

    assert listify_lookup_plugin_terms('{{ [1, 2, 3] }}', templar, play_context) == [1, 2, 3]

# Generated at 2022-06-13 16:33:49.274512
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    string = u'1:2:3'
    string_result = [u'1', u'2', u'3']
    list = [u'1', u'2', u'3']
    list_result = [u'1', u'2', u'3']
    dict = {u'1': u'2', u'3': u'4'}
    dict_result = {u'1': u'2', u'3': u'4'}

    terms = string
    templar = Templar(loader=DataLoader(), variables=VariableManager())

# Generated at 2022-06-13 16:34:00.466083
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.template import Templar
    from ansible.parsing.tokenize import tokenize_kv
    from ansible.parsing.yaml.loader import AnsibleLoader

    # Basic test, simple string
    templar = Templar(loader=AnsibleLoader(''))
    assert listify_lookup_plugin_terms("string", templar, loader=AnsibleLoader('')) == ["string"]

    # String with spaces
    templar = Templar(loader=AnsibleLoader(''))
    assert listify_lookup_plugin_terms("string with spaces", templar, loader=AnsibleLoader('')) == ["string with spaces"]

    # String with comma
    templar = Templar(loader=AnsibleLoader(''))

# Generated at 2022-06-13 16:34:05.091639
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    x = listify_lookup_plugin_terms(['a', 'b'])
    assert len(x) == 2
    assert x[0] == 'a'
    assert x[1] == 'b'

    x = listify_lookup_plugin_terms('a,b')
    assert len(x) == 2
    assert x[0] == 'a'
    assert x[1] == 'b'

# Generated at 2022-06-13 16:34:13.414341
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    from ansible.template import Templar

    templar = Templar(loader=None)

    ##
    # Tests that return lists
    ##
    test_data = ['ansible', 'httpd', 'memcached']
    result = listify_lookup_plugin_terms(test_data, templar, None)
    assert result == test_data, result

    test_data = ['ansible', '"httpd"', '"memcached"']
    result = listify_lookup_plugin_terms(test_data, templar, None, convert_bare=True)
    assert result == test_data, result

    test_data = ['ansible', 'httpd']
    result = listify_lookup_plugin_terms(test_data, templar, None, convert_bare=True)
    assert result == test

# Generated at 2022-06-13 16:34:25.419356
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar
    from ansible.inventory.manager import InventoryManager

    dl = DataLoader()
    inv_mgr = InventoryManager(loader=dl, sources='localhost,')
    vm = VariableManager(loader=dl, inventory=inv_mgr)
    templar = Templar(loader=dl, variables=vm)

    output = listify_lookup_plugin_terms('1,2,3', templar, loader=dl, fail_on_undefined=True)
    assert output == ['1', '2', '3']


# Generated at 2022-06-13 16:34:32.116519
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    loader = DataLoader()
    templar = Templar(loader=loader)
    terms = listify_lookup_plugin_terms(terms=['foo', 'bar', 'baz'], templar=templar, loader=loader)
    assert terms == ['foo', 'bar', 'baz']

# Generated at 2022-06-13 16:34:41.135182
# Unit test for function listify_lookup_plugin_terms
def test_listify_lookup_plugin_terms():

    # This test doesn't make a ton of sense, as we don't have a working templar
    # but at least we can verify the direct results

    import pytest

    assert [] == listify_lookup_plugin_terms([], None, None)
    assert ['foo'] == listify_lookup_plugin_terms('foo', None, None)
    assert ['foo', 'bar'] == listify_lookup_plugin_terms(['foo', 'bar'], None, None)

    with pytest.raises(TypeError):
        listify_lookup_plugin_terms(12345, None, None)

    with pytest.raises(TypeError):
        listify_lookup_plugin_terms((12345,), None, None)