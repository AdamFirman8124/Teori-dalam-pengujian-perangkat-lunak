

# Generated at 2022-06-13 14:13:46.805463
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:13:56.617285
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils._text import to_text

    # prepare test data
    one = {'key1': {'key11': [{'key111': 1}, {'key111': 2}, {'key111': 3}]}}
    two = {'key1': {'key11': [{'key111': 4}, {'key111': 5}]}}

    # execute run method
    lookup_mock = LookupModule()
    result = lookup_mock.run([one, 'key1.key11.key111'])

    # test expected output
    assert len(result) == 5
    assert to_text(result[1][1]) == to_text({'key111': 3})

    # execute run method

# Generated at 2022-06-13 14:14:06.415874
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # set up module
    module = LookupModule()
    module.set_options(direct={'vars': {}})

    # basic usage
    list = module.run([['foo'], 'bar'], None)
    assert list == [('foo', 'bar')]

    # test short form of the third parm
    list = module.run([['foo'], 'bar', {'skip_missing': 'True'}], None)
    assert list == [('foo', 'bar')]

    # test skip_missing
    list = module.run([{'foo': {'bar': 'foo'}}], None)
    assert list == []

    # test skip_missing
    list = module.run([{'foo': {'bar': 'foo'}}], None)
    assert list == []

    # test nested lists
    list

# Generated at 2022-06-13 14:14:18.634678
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Unit test for method run of class LookupModule
    import json
    import pytest

    from ansible.errors import AnsibleError
    from ansible.utils.listify import listify_lookup_plugin_terms

    from ansible.module_utils.six import string_types
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.plugins.lookup import LookupBase

    class TestLookupModule(LookupModule):

        def __init__(self, loader=None, templar=None, **kwargs):
            super(TestLookupModule, self).__init__(loader=loader, templar=templar, **kwargs)

        def run_all(self, terms, variables=None, **kwargs):
            terms[0] = listify_lookup_

# Generated at 2022-06-13 14:14:28.390094
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Ensure that the LookupModule class is defined in the local space
    global LookupModule

    # import class
    import ansible.plugins.lookup.subelements

    class Test:
        def __init__(self, runner):
            self.runner = runner

        def assertEqual(self, a, b):
            assert a == b, "%r != %r" % (a, b)

    # load the class under test
    LookupModule = ansible.plugins.lookup.subelements.LookupModule

    # instantiate the test class
    test = Test(None)  # noqa: F841

    # test normal usage

# Generated at 2022-06-13 14:14:39.152470
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test with invalid arguments
    lu = LookupModule(None, None)
    try:
        lu.run([], {})
        assert False
    except AnsibleError as e:
        assert 'subelements lookup expects a list of two or three items' in str(e)

    try:
        lu.run([42], {})
        assert False
    except AnsibleError as e:
        assert 'first a dict or a list' in str(e)

    try:
        lu.run([[], 42], {})
        assert False
    except AnsibleError as e:
        assert 'second a string' in str(e)

    # Test with empty elementlist

# Generated at 2022-06-13 14:14:45.182698
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import json

    lookup_test_vars = {'users': [{'name': 'alice', 'authorized': ['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub'], 'mysql': {'password': 'mysql-password', 'hosts': ['%', '127.0.0.1', '::1', 'localhost'], 'privs': ['*.*:SELECT', 'DB1.*:ALL']}, 'groups': ['wheel']}, {'name': 'bob', 'authorized': ['/tmp/bob/id_rsa.pub'], 'mysql': {'password': 'other-mysql-password', 'hosts': ['db1'], 'privs': ['*.*:SELECT', 'DB2.*:ALL']}}]}

    # build_items
    ret_build_items

# Generated at 2022-06-13 14:14:54.338758
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Forwarding imports:
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader

    def _assert_result(terms, expected_result):
        assert expected_result == lookup_plugin.run(terms, variables=variable_manager, loader=loader, templar=None)[0]

    mock_loader = DataLoader()
    mock_inventory = Inventory(loader=mock_loader, variable_manager=VariableManager(loader=mock_loader), host_list=['host1'])
    mock_variable_manager = VariableManager(loader=mock_loader, inventory=mock_inventory)


# Generated at 2022-06-13 14:15:06.050078
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # build_items

# Generated at 2022-06-13 14:15:14.548716
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    values = {
        "one": {
            "urls": [
                "http://www.ansible.com",
                "http://www.ansibleworks.com",
                "http://docs.ansible.com"
            ],
            "ports": [443, 80]
        },
        "two": {
            "urls": [
                "http://github.com/ansible/ansible"
            ],
            "ports": [80, 443, 8080]
        }
    }

    # simple test
    assert lookup.run([values, "ports"], None) == [(values["one"], 443), (values["one"], 80), (values["two"], 80), (values["two"], 443), (values["two"], 8080)]

    # test list of keys

# Generated at 2022-06-13 14:15:36.245892
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.pytest.plugins.testutil import assert_deepequal
    module = LookupModule()


# Generated at 2022-06-13 14:15:49.209961
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    class FakeTemplar(object):

        def __init__(self, loader):
            self.loader = loader

        def template(self, data):
            return data

    class FakeLoader(object):

        def get_basedir(self, *args, **kwargs):
            return '/'

    def test_run_one_user(fake_terms, fake_flags, want_ret):
        elementlist = fake_terms[0]
        subelements = fake_terms[1]
        terms = [elementlist, subelements]
        templar = FakeTemplar(FakeLoader())
        subm = LookupModule(templar=templar, loader=FakeLoader())
        res = subm.run(terms=terms, variables={}, **fake_flags)
        assert res == want_ret

    # subelements

# Generated at 2022-06-13 14:15:58.182286
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    from ansible.module_utils.six import StringIO
    from ansible.utils.ansible_type_defaults import DEFAULTS
    from ansible.utils.hashing import checksum

    class Mock_subelements(LookupModule):
        def __init__(self, md5sum, sio):
            self._md5sum = md5sum
            self.__call_ansible_module_defaults = (  # pylint: disable=no-member
                DEFAULTS.__call__)
            self.__call_ansible_md5 = (  # pylint: disable=no-member
                checksum.__call__)
            self.__call_ansible_print = (  # pylint: disable=no-member
                print.__call__)
            self.__call_

# Generated at 2022-06-13 14:16:06.455816
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:16:18.752067
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test error handling
    from ansible.errors import AnsibleError

    # Test 1: invalid terms
    terms = [('a', 'a', 'a')]
    lm = LookupModule()
    try:
        lm.run(terms, None)
        assert False
    except AnsibleError as e:
        assert 'lookup_plugin.subelements expects a list of two or three items' in e.message

    # Test 2: invalid first term
    terms = ['a', 'a']
    lm = LookupModule()
    try:
        lm.run(terms, None)
        assert False
    except AnsibleError as e:
        assert 'subelements lookup expects a list of two or three items, first a dict or a list, second a string pointing to the subkey' in e.message

    # Test 3

# Generated at 2022-06-13 14:16:26.740788
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module_object = LookupModule()
    assert lookup_module_object.run(None, None, **{'a': 'A'}) == []
    assert lookup_module_object.run([], None, **{'a': 'A'}) == []
    assert lookup_module_object.run([{'a': 'A'}], None, **{'a': 'A'}) == [({'a': 'A'}, {'a': 'A'})]
    assert lookup_module_object.run([{'a': 'A', 'b': {'b': 'B'}}], None, **{'a': 'A'}) == [({'a': 'A', 'b': {'b': 'B'}}, {'a': 'A', 'b': {'b': 'B'}})]
    assert lookup_module

# Generated at 2022-06-13 14:16:31.376788
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    # test run without terms
    try:
        lookup_module.run([])
    except AnsibleError as e:
        assert "subelements lookup expects a list of two or three items" in str(e)
    # test run with one term
    try:
        lookup_module.run(['a'])
    except AnsibleError as e:
        assert "subelements lookup expects a list of two or three items" in str(e)
    # test run with terms with first term no list
    try:
        lookup_module.run(['a', 'b'])
    except AnsibleError as e:
        assert "subelements lookup expects a list of two or three items" in str(e)
    # test run with terms with second term no string

# Generated at 2022-06-13 14:16:41.753321
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # https://github.com/ansible/ansible/issues/19351
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.yaml.dumper import AnsibleDumper
    module = AnsibleDumper()
    lookup = LookupModule()
    # case 1: skip_missing=False

# Generated at 2022-06-13 14:16:49.585035
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def setUpModule():
        import sys, os
        sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
        global users, lookup_module

# Generated at 2022-06-13 14:17:02.315122
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import yaml
    yaml.add_constructor(u'!subelements', yaml.SafeLoader.construct_yaml_str)
    import ansible.parsing.yaml.objects
    ansible.parsing.yaml.objects.ANSIBLE_LOADER.add_constructor(u'!subelements', ansible.parsing.yaml.objects.AnsibleLoader.construct_yaml_str)


# Generated at 2022-06-13 14:17:30.939602
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = [
        [
            {
                "foo":{
                    "bar":"baz",
                    "baz":[]
                },
                "bar":{
                    "foo":{"bar":"baz"},
                    "baz":[]
                },
                "baz":{
                    "foo": "bar",
                    "bar": "baz"
                }
            },
            {
                "foo":{
                    "bar":"baz",
                    "baz":[]
                },
                "bar":{
                    "foo":{"bar":"baz"},
                    "baz":[]
                },
                "baz":{
                    "foo": "bar",
                    "bar": "baz"
                }
            }
        ],
        "foo.baz"
    ]

    loader = None
    templar = None

# Generated at 2022-06-13 14:17:43.980404
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    # First term is a list, second term is a string, third term is a dict
    # If the second term is not found, raise exception and do not return anything
    assert lookup_module.run([[{'key': ['subkey']}], 'key'], {}) == [({'key': ['subkey']}, ['subkey'])]
    assert lookup_module.run([[{'key': ['subkey1', 'subkey2']}], 'key'], {}) == [({'key': ['subkey1', 'subkey2']}, 'subkey1'), ({'key': ['subkey1', 'subkey2']}, 'subkey2')]

# Generated at 2022-06-13 14:17:50.733847
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms1 = {'users': [{'name': 'alice', 'authorized': ['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub']}]}
    terms2 = {'users': [{'name': 'bob', 'authorized': ['/tmp/bob/id_rsa.pub']}]}
    terms = [terms1, terms2]
    terms1_2 = {'users': [{'name': 'alice', 'authorized': ['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub']}, {'name': 'bob', 'authorized': ['/tmp/bob/id_rsa.pub']}]}

    # sanity check
    assert terms1 != terms2
    assert terms != terms1_2


# Generated at 2022-06-13 14:18:01.598601
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup_ret_list = [{'item1': 'val1'}, {'item1': 'val2'}]


# Generated at 2022-06-13 14:18:09.740409
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Setup
    LookupModule_instance = LookupModule()
    LookupModule_instance.set_options() # fake

    # Run
    fields = LookupModule_instance.run([
        [
            {
                'a': 'A',
                'b': {
                    'b1': 'B1'
                },
                'c': [
                    'C1',
                    'C2'
                ]
            }
        ],
        'c'
    ], {})

    # Test
    assert fields == [('C1',), ('C2',)]


# Generated at 2022-06-13 14:18:16.989596
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    q = LookupModule()

    # Test error when terms is not a list
    terms = "string"
    variables = {}
    kwargs = {}
    try:
        ret = q.run(terms,variables,**kwargs)
    except AnsibleError as e:
        assert("subelements lookup expects a list of two or three items" in e.message)

    # Test error with terms not a list of two items
    terms = [1,2,3]
    try:
        ret = q.run(terms,variables,**kwargs)
    except AnsibleError as e:
        assert("subelements lookup expects a list of two or three items" in e.message)

    # Test error with first term is not a list
    terms = ["string", "subkey"]

# Generated at 2022-06-13 14:18:17.831400
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # TODO: add unit test for method run of class LookupModule

    assert False

# Generated at 2022-06-13 14:18:22.912712
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    sys.modules['__main__'].__file__ = "/home/ansible/ansible/lookup_plugins/subelements.py"
    sys.path.append("/home/ansible/ansible/lookup_plugins/")
    import subelements
    my_object = subelements.LookupModule()
    my_object.run([{"name": "alice", "authorized": ["/tmp/alice/onekey.pub", "/tmp/alice/twokey.pub"]}, "authorized"], {})

# Generated at 2022-06-13 14:18:35.700860
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.compat.tests.mock import patch, Mock
    from ansible.errors import AnsibleError
    from ansible.plugins.lookup import LookupBase
    from ansible.utils.hashing import md5s
    from ansible.utils.display import Display
    import os

    import __main__
    __main__.display = Display()
    lookup_instance = LookupModule()

    # first test: simple usage, get a value from a dict
    test_terms = [
        [{"key1":"val1", "key2":["subval1", "subval2"], "key3":{"subkey1":"subval1"}}, "key2"]
    ]

# Generated at 2022-06-13 14:18:47.268123
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    from ansible.utils.vars import combine_vars
    from ansible.template import Templar

    vars = dict()
    vars['var1'] = dict()
    vars['var1']['subkey1'] = 'subvalue1'
    vars['var1']['sublist'] = list()
    vars['var1']['sublist'].append(dict(subsubkey='subsubvalue1'))
    vars['var1']['sublist'].append(dict(subsubkey='subsubvalue2'))

# Generated at 2022-06-13 14:19:29.627234
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test_run_1
    lookup_module = LookupModule()
    lookup_module._templar = {}
    terms = [{'test1': {'subelements_test': [100, 200, 300]},
              'test2': {'subelements_test': [101, 201, 301]},
              'test3': {'subelements_test': [102, 202, 302]}}, 'subelements_test', {'skip_missing': True}]

# Generated at 2022-06-13 14:19:42.820405
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Some vars for the tests
    param1_dic = {
        'authorized': ['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub'],
        'groups': ['wheel'],
        'mysql': {
            'hosts': ['%', '127.0.0.1', '::1', 'localhost'],
            'password': 'mysql-password',
            'privs': ['*.*:SELECT', 'DB1.*:ALL']
        },
        'name': 'alice'
    }

    param3_dic = {}

    param1_list = [param1_dic]
    param2_str = 'authorized'
    param3_dic = {}
    param3_dic['skip_missing'] = False

    param4_dic = {}

# Generated at 2022-06-13 14:19:52.682692
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = type('DummyOpts', (object,), {'module_name': 'test'})()
    lookup = LookupModule()

    # Test with two items, a list and a dictionary key
    users = [
        {
            'name': 'alice',
            'authorized': ['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub']
        },
        {
            'name': 'bob',
            'authorized': ['/tmp/bob/id_rsa.pub']
        }
    ]
    terms.terms = [[users, 'authorized']]
    results = lookup.run(terms, dict(ansible_env=dict()))
    assert len(results) == 3
    assert results[0][0] == users[0]

# Generated at 2022-06-13 14:20:04.101732
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import sys
    from ansible.module_utils.six import PY2, PY3, StringIO
    from ansible.module_utils.six.moves import builtins

    # basic test
    users = [{'name': 'alice', 'authorized': ['/tmp/alice/onekey.pub']},
             {'name': 'bob', 'authorized': ['/tmp/bob/id_rsa.pub', '/tmp/bob/id_rsa.pub']}]
    terms = [users, 'authorized']
    lm = LookupModule()

# Generated at 2022-06-13 14:20:15.152103
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    subelements = LookupModule()

# Generated at 2022-06-13 14:20:26.490715
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import collections
    # use OrderedDict for ordered comparison of dicts
    try:
        from collections import OrderedDict
    except ImportError:
        from ordereddict import OrderedDict

    lookup_plugin = LookupModule()


# Generated at 2022-06-13 14:20:37.188279
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import unittest

    class TestLookupModule(unittest.TestCase):

        def setUp(self):
            self.test_subkey = "test_subkey"
            self.test_subkey_value = "value"
            self.test_subkey_value2 = "value2"
            self.test_subkey_value3 = "value3"
            self.sub_subkey = "sub_subkey"
            self.sub_subkey_value = "subsubvalue"
            self.sub_subkey_value2 = "subsubvalue2"
            self.sub_subkey_value3 = "subsubvalue3"


# Generated at 2022-06-13 14:20:40.234162
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # module = LookupModule()
    # module.run([{'user1': {'mysql': {'hosts': ['host1'], 'privs': [['priv1']]}}}], None)
    pass

# Generated at 2022-06-13 14:20:52.878487
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_obj = LookupModule()

# Generated at 2022-06-13 14:21:01.846717
# Unit test for method run of class LookupModule
def test_LookupModule_run():

  def test_run_given_a_list_of_two_items_the_second_should_be_a_dictionary_key_and_the_first_a_list_of_dictionaries_otherwise_it_should_fail(monkeypatch):
      from ansible.errors import AnsibleError
      from ansible.plugins.lookup import LookupModule

      def mock_lookup_base_run(self, terms, variables, **kwargs):
          pass

      monkeypatch.setattr(LookupModule, 'run', mock_lookup_base_run)

      with pytest.raises(AnsibleError) as error:
          looker = LookupModule()
          looker.run('terms', 'variables')

      assert str(error.value) == 'subelements lookup expects a list of two or three items'



# Generated at 2022-06-13 14:22:21.465268
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:22:21.906756
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    pass

# Generated at 2022-06-13 14:22:34.592922
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = [{'term1': {'subterm': ['value1', 'value2']}, 'term2': {'subterm': ['value3', 'value4']}}, 'subterm']
    ret = LookupModule().run(terms=terms, variables=None)
    assert ret[0][0]['term1'] == terms[0]['term1']
    assert ret[0][1] == 'value1'
    assert ret[1][0]['term1'] == terms[0]['term1']
    assert ret[1][1] == 'value2'
    assert ret[2][0]['term2'] == terms[0]['term2']
    assert ret[2][1] == 'value3'
    assert ret[3][0]['term2'] == terms[0]['term2']

# Generated at 2022-06-13 14:22:42.525125
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # test with variable, subkey and subkey list:
    variable = {'a': {'b': [1, 2], 'c': ['x', 'y']}}
    subkey = 'b'
    terms = [variable, subkey]
    module = LookupModule()
    result = module.run(terms, None)
    assert result == [(variable['a'], 1), (variable['a'], 2)]

    # test with variable list, subkey and subkey list:
    variable = [{'a': {'b': [1, 2], 'c': ['x', 'y']}}, {'a': {'b': [3, 4], 'c': ['x', 'y']}}]
    subkey = 'b'
    terms = [variable, subkey]
    module = LookupModule()

# Generated at 2022-06-13 14:22:53.836198
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    users = [
        {'name': 'alice', 'authorized': ['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub'],
         'mysql': {'password': 'mysql-password',
                   'hosts': ['%', '127.0.0.1', '::1', 'localhost'],
                   'privs': ['*.*:SELECT', 'DB1.*:ALL']},
         'groups': ['wheel']},
        {'name': 'bob', 'authorized': ['/tmp/bob/id_rsa.pub'],
         'mysql': {'password': 'other-mysql-password',
                   'hosts': ['db1'],
                   'privs': ['*.*:SELECT', 'DB2.*:ALL']}}
    ]
    lookup = Lookup

# Generated at 2022-06-13 14:23:06.618944
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # setup
    users = [
        {'name': 'alice', 'authorized': ['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub'], 'groups': ['wheel'],
         'mysql': {'password': 'mysql-password',
                   'hosts': ['%', '127.0.0.1', '::1', 'localhost'],
                   'privs': ['*.*:SELECT', 'DB1.*:ALL']}},
        {'name': 'bob', 'authorized': ['/tmp/bob/id_rsa.pub'],
         'mysql': {'password': 'other-mysql-password',
                   'hosts': ['db1'],
                   'privs': ['*.*:SELECT', 'DB2.*:ALL']}}
    ]
    terms

# Generated at 2022-06-13 14:23:19.029314
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.lookup import LookupBase

    class DummyRunner:

        def __init__(self, loader, variable_manager, inventory, play):
            self.loader = loader
            self.variable_manager = variable_manager
            self.inventory = inventory
            self.play = play
            self.tqm = TaskQueueManager(
                inventory=inventory,
                variable_manager=variable_manager,
                loader=loader,
                update_cache=False,  # noop as no caching
            )


# Generated at 2022-06-13 14:23:31.622657
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    cls = LookupModule
    # initialise the main class and the lookup module
    lookup_module = cls()
    # powershell:ansible_powershell_shell = powershell -NoLogo -NoProfile -NonInteractive -ExecutionPolicy Bypass -InputFormat None -Command -
    # powershell:ansible_powershell_shell = cmd /c powershell.exe -NoLogo -NoProfile -NonInteractive -ExecutionPolicy Bypass -InputFormat None -Command -