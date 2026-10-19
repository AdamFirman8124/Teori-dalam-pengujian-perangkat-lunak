

# Generated at 2022-06-13 14:13:47.003509
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # use first term as list
    lookup_module = LookupModule()
    terms = {
        0: [
          {
            'name': 'alice',
            'authorized': [
              '/tmp/alice/onekey.pub',
              '/tmp/alice/twokey.pub'
            ]
          },
          {
            'name': 'bob',
            'authorized': [
              '/tmp/bob/id_rsa.pub'
            ]
          }
        ],
        1: 'authorized'
    }

# Generated at 2022-06-13 14:13:56.732916
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    print("Test_LookupModule_run")
    def _test(terms, result, error=None):
        lookup_obj = LookupModule()
        if error:
            try:
                lookup_obj.run(terms, None)
            except Exception as e:
                assert str(e) == error, "unexpected error message %s" % e
        else:
            assert lookup_obj.run(terms, None) == result, "unexpected result %s" % lookup_obj.run(terms, None)

    # wrong number of terms
    _test(["a"], None, "subelements lookup expects a list of two or three items")
    _test(["a", "b", "c", "d"], None, "subelements lookup expects a list of two or three items")
    # first item not a list or dict
    _test

# Generated at 2022-06-13 14:14:03.207268
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=None)
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    playbook_path ='../../../tests/unit/lookup_plugins/subelements/subelements.yml'

# Generated at 2022-06-13 14:14:16.414926
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import io

# Generated at 2022-06-13 14:14:24.451499
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import StringIO
    import sys, os

    # Python 2:
    if sys.version_info[0] < 3:
        builtins_module = '__builtin__'
    # Python 3:
    else:
        builtins_module = 'builtins'

    # Mock modules:

# Generated at 2022-06-13 14:14:36.339922
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={'a': dict(type='list', elements='dict'), 'b': dict(type='list', elements='dict'), 'c': dict(type='list')})

    # test function given list of dicts and key which exists in all subelements
    terms = [
        [
          {"key0": "val0"},
          {"key1": "val1", "key2": "val2"},
          {"key3": "val3", "key4": "val4", "key5": "val5"},
          {"key6": "val6", "key7": "val7", "key8": "val8", "key9": "val9"}
        ], "key8"
    ]

# Generated at 2022-06-13 14:14:47.092784
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # test a list of strings as the input term
    lookup_module = LookupModule()
    terms = [
        [
            {
                "name": "test1",
                "value": [
                    "/tmp/test1.key",
                    "/tmp/test1.pub"
                ]
            },
            {
                "name": "test2",
                "value": [
                    "/tmp/test2.key",
                    "/tmp/test2.pub"
                ]
            }
        ],
        "value"
    ]
    result = lookup_module.run(terms, [])
    assert 2 == len(result)
    assert result[0] == ({'name': 'test1', 'value': ['/tmp/test1.key', '/tmp/test1.pub']}, '/tmp/test1.key')

# Generated at 2022-06-13 14:14:59.719038
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    #setup
    module = LookupModule()
    terms = [
        [{
            'id': 1,
            'name': '1',
            'nested': {
                'id': 1,
                'name': '1.1'
            }
        }, {
            'id': 2,
            'name': '2',
            'nested': {
                'id': 2,
                'name': '2.1'
            }
        }],
        'nested.id'
    ]

# Generated at 2022-06-13 14:15:00.754609
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # No tests yet

# Generated at 2022-06-13 14:15:11.242323
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # check for invalid subelements:
    # -------
    # invalid number of sub_terms (1)
    subterms = ["sub_terms"]
    l = LookupModule()
    try:
        l.run(subterms, {})
        assert False
    except AnsibleError:
        pass

    # invalid number of sub_terms (3)
    subterms = ["sub_terms", "sub_terms", "sub_terms"]
    l = LookupModule()
    try:
        l.run(subterms, {})
        assert False
    except AnsibleError:
        pass

    # invalid first sub_term (not dict or list)
    subterms = [42, "sub_terms"]
    l = LookupModule()

# Generated at 2022-06-13 14:15:30.276090
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.errors import AnsibleLookupError
    from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleSequence, AnsibleMapping
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    lookup_module = LookupModule()
    templar = Templar(loader=None, variables=VariableManager())

    # Basic instantiation
    lookup_module.set_loader(None)
    lookup_module._templar = templar


# Generated at 2022-06-13 14:15:41.795625
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import json
    import pytest

    # arg 'flags'
    #
    # skip_missing
    #
    terms = [
        [
            {'k1': 'v1'},
        ],
        'k2',
        {
            'skip_missing': True,
        }
    ]
    result = LookupModule().run(terms, None)
    assert isinstance(result, list)
    assert len(result) == 0

    terms = [
        [
            {'k1': 'v1'},
        ],
        'k2',
        {
            'skip_missing': False,
        }
    ]
    with pytest.raises(AnsibleError) as error:
        result = LookupModule().run(terms, None)

# Generated at 2022-06-13 14:15:53.792655
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # invoke lookup in lookup module
    terms = ['{{ test_list }}', 'key2', {'skip_missing': True}]
    # initialize lookup module
    lookup_mod = LookupModule()
    # get template engine and data loader
    templar = lookup_mod._templar
    loader = lookup_mod._loader
    # if templating needed:
    terms[0] = templar.template(terms[0])
    terms[0] = loader.load_from_file(terms[0])
    # Test run method and get final result

# Generated at 2022-06-13 14:16:04.580608
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule(None, None)

    # Test #1: no params given
    assert_exception('subelements:: requires 2 or 3 parameters, lookups get 2 or 3 items, the first should be a list or dict,', lookup.run)

    # Test #2: empty params given
    assert_exception('subelements:: first a dict or a list, second a string pointing to the subkey',lookup.run, [])

    # Test #2_2: params given, but non-list
    assert_exception('subelements lookup expects a list of two or three items, first a dict or a list, second a string pointing to the subkey',lookup.run, 'not a list')

    # Test #3: first param not a list/dict

# Generated at 2022-06-13 14:16:14.630135
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()
    # with_subelements - extract subkey (1) and skip if missing
    terms = [{
        'item': {
            'name': 'alice',
            'ssh': {
                'pubkeys': [
                    '/tmp/alice/onekey.pub',
                    '/tmp/alice/twokey.pub'
                ]
            }
        }
    }]
    ret = lookup_plugin.run(terms, None)

# Generated at 2022-06-13 14:16:15.576066
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    raise NotImplementedError()

# Generated at 2022-06-13 14:16:16.894602
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # method run() not implemented
    pass


# Generated at 2022-06-13 14:16:25.591203
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:16:36.925404
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = [
        [
            {
                'name': 'alice',
                'authorized': [
                    '/tmp/alice/onekey.pub',
                    '/tmp/alice/twokey.pub',
                ],
                'mysql': {
                    'password': 'mysql-password',
                    'hosts': [
                        '%',
                        '127.0.0.1',
                        '::1',
                        'localhost',
                    ],
                    'privs': [
                        '*.*:SELECT',
                        'DB1.*:ALL',
                    ],
                },
                'groups': [
                    'wheel',
                ],
            },
        ],
        'authorized',
    ]
    result = LookupModule().run(terms = terms, variables = {})

# Generated at 2022-06-13 14:16:46.774698
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.errors import AnsibleError
    from ansible.module_utils.six import string_types
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.plugins.lookup import LookupBase

    fl = LookupModule()

# Generated at 2022-06-13 14:17:12.047390
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import BytesIO
    from ansible.errors import AnsibleError
    from ansible.playbook.play_context import PlayContext
    from ansible.module_utils._text import to_bytes

    class MockTemplar(object):

        def __init__(self, loader):
            self._loader = loader

        def template(self, value, convert_bare=False):
            return value

    class MockVarManager(object):

        def __init__(self):
            self.vars = dict(foo="bar")

    class MockLoader(object):

        def __init__(self):
            self.vars = MockVarManager()

        def get_basedir(self, host):
            return "."

    class MockPlayContext(object):

        def __init__(self):
            self

# Generated at 2022-06-13 14:17:20.433358
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    subelements = LookupModule()

# Generated at 2022-06-13 14:17:31.923549
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import unittest
    import pprint

    class TestLookupModule_run(unittest.TestCase):
        PRESET = dict(
            var1=[
                dict(key1=1),
                dict(key2=2, subkey=[dict(item='one'), dict(item='two')], key3=[dict(item='three')]),
                dict(key2=2),
                dict(key2=2, subkey=dict(item='four')),
            ]
        )

        def setUp(self):
            equal = self.assertEqual
            setattr(self, 'assertEqual', lambda x, y: True)
            self.lookup = LookupModule()
            setattr(self, 'assertEqual', equal)

# Generated at 2022-06-13 14:17:44.742657
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test is skipped if no pytest is available

    from pytest import mark, skip
    from ansible.module_utils.six import PY3
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor


# Generated at 2022-06-13 14:17:55.867256
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    lookup = LookupModule()

    # make sure the first term is a dict or a list
    terms = ('/path/to/files', 'varkey')
    result = lookup._templar._available_variables.copy()
    result.update(dict(
        TERM='/path/to/files',
        varkey='varvalue',
    ))
    with pytest.raises(AnsibleError) as exc:
        list(lookup.run(terms, variables=result))
    assert "subelements lookup expects a dict or a list" in str(exc)

    # make sure the second term is a string
    terms = ([{'varkey': 'varvalue'}], 12)
    result = lookup._templar._available_variables.copy()

# Generated at 2022-06-13 14:18:02.194652
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    data = [{'subelement': [1, 2, 3]}, {'subelement': [4, 5]}, {'subelement': [6, 7, 8]}]
    lu = LookupModule()
    results = lu.run([data, 'subelement'], dict())
    assert results == [(item, subitem) for item in data for subitem in item['subelement']]

    data = [{'subelement': [1, 2, 3]}, {'subelement': [4, 5]}, {'subelement': [6, 7, 8]}]
    lu = LookupModule()
    results = lu.run([data, 'subelement', {'skip_missing': True}], dict())

# Generated at 2022-06-13 14:18:13.410997
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class Options():
        def __init__(self, var1, var2):
            self.vars = {'var1': var1, 'var2': var2}

    class Runner():
        def __init__(self, my_vars):
            self.my_vars = my_vars

        def get_vars(self):
            return self.my_vars


# Generated at 2022-06-13 14:18:23.088595
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Unit test for method run of class LookupModule"""

    # get a lookup module instance to test
    subelements_lookup = LookupModule()

    # test valid inputs
    # a valid lookup input consists of two or three items, the first item being a list in all cases.
    # If the first item is not a list, the lookup should raise an error
    inputList = [
        {'name': 'user1', 'authorized': ['key1', 'key2'], 'groups': ['group1']},
        {'name': 'user2', 'authorized': ['key1']},
        {'name': 'user3', 'authorized': ['key1', 'key3', 'key4'], 'groups': ['group1', 'group2', 'group3']}
    ]
    # in this test, we will try to get the authorized keys from

# Generated at 2022-06-13 14:18:35.969226
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup.subelements import LookupModule
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils.six import string_types
    from ansible.module_utils.six.moves import range
    import pytest

    def _boolean(s):
        return boolean(s, strict=False) if isinstance(s, string_types) else s


# Generated at 2022-06-13 14:18:47.378146
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def _run_test(terms, elementlist, exp_ret, check_exp_msg, flags=None):
        # build mock object
        if flags is None:
            flags = {}
        mock_self = type('obj', (object,), {
            '_templar': None,
            '_loader': None
        })()
        for flag in FLAGS:
            if flag in flags:
                mock_self._templar = type('obj', (object,), {
                    'template': lambda s: flags[flag]
                })()
                break

        # run method and check result
        ret = LookupModule.run(mock_self, terms, {})
        if ret != exp_ret:
            _, _, tb = sys.exc_info()

# Generated at 2022-06-13 14:19:30.134300
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.parsing.convert_bool import BOOLEANS_TRUE
from ansible.module_utils.parsing.convert_bool import BOOLEANS_FALSE

    # Check for expected error when two list are given as parameters

# Generated at 2022-06-13 14:19:43.385912
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Initialize AnsibleModule object for use with LookupModule
    class AnsibleModule:
        class ArgSpec:
            def __init__(self):
                self.argument_spec = dict(
                    name = dict(),
                    foo = dict(),
                    bar = dict()
                )
        def __init__(self):
            self.params = dict()
            self.args = dict()
            self.argspec = self.ArgSpec()
    ansible_module = AnsibleModule()

    # Initialize empty variables
    variables = dict()

    # Declare test input terms
    terms = [
        [
            dict(name='alice', group='wheel', host='db1'),
            dict(name='bob', group='admin', host='db2')
        ],
        'name'
    ]

    # Declare correct output


# Generated at 2022-06-13 14:19:53.061890
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # simple example
    _terms = [
        [
            {'skipped': False, 'authorized': ['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub'], 'name': 'alice'},
            {'skipped': False, 'authorized': ['/tmp/bob/id_rsa.pub'], 'name': 'bob'}
        ],
        'authorized'
    ]

# Generated at 2022-06-13 14:20:04.336332
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:20:15.353718
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit test for method LookupModule.run
    """
    # run setup
    setup_module(sys.modules[__name__])

    print('')
    print('--- test_LookupModule: unit test method LookupModule.run')
    print('')

    lookup_plugin = LookupModule()
    # setup data
    terms = [[{"dummy": {"key": ["test1", "test2", "test3"]}}], "dummy.key", {}]

    # run test
    result = lookup_plugin.run(terms, None)

    # assert result
    assert (isinstance(result, list))
    assert (len(result) == 3)
    for item in result:
        assert (isinstance(item, tuple))
        assert (len(item) == 2)

# Generated at 2022-06-13 14:20:26.531766
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.compat.six as six

    lookup_module = LookupModule()

    assert lookup_module.run([], None) == []

    assert lookup_module.run([{"skipped": True}], None) == []

    assert lookup_module.run([[{"skipped": True}]], None) == []

    # make sure the module will not accept wrong number of terms
    try:
        lookup_module.run([["testlist"]], None)
        raise Exception("ansible.errors.AnsibleError was not raised")
    except ansible.errors.AnsibleError as e:
        assert "subelements lookup expects a list of two or three items" in six.text_type(e)


# Generated at 2022-06-13 14:20:37.219023
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # given
    lm = LookupModule()

# Generated at 2022-06-13 14:20:49.523616
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import unittest
    from mock import MagicMock, patch, Mock

    class MockRunner(object):

        def __init__(self):
            self.runner = Mock()
            self.runner.lookup_loader = Mock()
            self.runner.lookup_loader.get_basedir.return_value = '.'

    class TestLookupModule(unittest.TestCase):
        def setUp(self):
            self.runner = MockRunner()
            self.runner.runner.lookup_loader.get_basedir.return_value = '.'


# Generated at 2022-06-13 14:20:59.895723
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()

    facts = dict(
        users=[
            dict(
                name='alice',
                email='alice@example.com',
                authorized=['a1', 'a2'],
                mysql=dict(
                    hosts=['h1'],
                    privs=['p1']
                )
            ),
            dict(
                name='bob',
                email='bob@example.com',
                authorized=['b1', 'b2'],
                mysql=dict(
                    hosts=['h1', 'h2'],
                    privs=['p1', 'p2']
                )
            )
        ]
    )
    result = module.run([facts, 'users'], dict(), variable_manager={}, loader=None, templar=None)

# Generated at 2022-06-13 14:21:12.057915
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:22:27.870812
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''
    Unit tests
    '''

    # Test the second param being a dictionary
    example_data_dict = {
        'users':{
            'name': 'alice',
            'authorized': ['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub'],
            'groups': ['wheel'],
            'mysql':{
                'password': 'mysql-password',
                'hosts': ['%', '127.0.0.1', '::1', 'localhost'],
                'privs': ['*.*:SELECT', 'DB1.*:ALL']
            }
        }
    }
    lookup_module = LookupModule()


# Generated at 2022-06-13 14:22:38.559630
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible.plugins.lookup import LookupModule
    from ansible.utils.listify import listify_lookup_plugin_terms

    def _raise_terms_error(msg=""):
        raise AnsibleError(
            "subelements lookup expects a list of two or three items, " + msg)

    integer_list = [1,2,3,4,5]
    string_list = ["a", "b", "c"]
    dictionary = {"a":{"b":{"c":"d"}}, "e":5}
    dictionary_with_skipped = {"a":{"skipped": True}, "b":[], "c":{"d":"e"}}
    dictionary_with_skipped_in_list = [{"a":{"skipped": True}}, {"b":[]}, {"c":{"d":"e"}}]

    lookup_

# Generated at 2022-06-13 14:22:40.881369
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test without flags
    # Test with flag 'skip_missing'
    pass

# Generated at 2022-06-13 14:22:52.824507
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''Test the run method of the LookupModule class.'''
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils._text import to_text
    from ansible.utils.listify import listify_lookup_plugin_terms
    from ansible.plugins.lookup import LookupBase
    from ansible.template import Templar
    import pytest


# Generated at 2022-06-13 14:23:05.773740
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import lookup_loader

    print("TEST: subelements lookup plugin")
    lookup = lookup_loader.get('subelements')
    assert lookup is not None
    assert hasattr(lookup, 'run')
    assert hasattr(lookup.run, '__call__')

    # the users var is defined in the example section of the docs

# Generated at 2022-06-13 14:23:18.170343
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    try:
        from ansible.module_utils.common.collections import ImmutableDict
    except ImportError:
        from collections import ImmutableDict
    def _dict(base, **kwargs):
        base.update(kwargs)
        return ImmutableDict(base)

    from ansible.parsing import vault
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.playbook.play_context import PlayContext

    # Some tests need secret to decrypt vaults
    secret = 'secret'
    vault_ids = {'test_1': secret}
    vault.VaultLib.setup(True, 1, None, None, None, None, vault_ids)

    # Initiate lookup_module
    lookup_module = LookupModule()

    # Initiate templar
    templ

# Generated at 2022-06-13 14:23:30.975081
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # create an instance of LookupModule
    l = LookupModule()

    # create a dict with a list that is to be flattened
    test_data_dict = {
        "some": {
            "deeply": {
                "nested": [
                    "nested_a",
                    "nested_b",
                    "nested_c"
                ]
            }
        }
    }

    # test the method run (with a dict)
    result = l.run([test_data_dict, "some.deeply.nested"], None, skip_missing=False)

    assert isinstance(result, list)
    assert result == [('nested_a',), ('nested_b',), ('nested_c',)]

    # test the method run (with a list)