

# Generated at 2022-06-13 14:13:41.513995
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def _raise_terms_error(msg=""):
        raise AnsibleError(
            "subelements lookup expects a list of two or three items, " + msg)

    # check lookup terms - check number of terms
    if not isinstance(terms, list) or not 2 <= len(terms) <= 3:
        _raise_terms_error()

    # first term should be a list (or dict), second a string holding the subkey
    if not isinstance(terms[0], (list, dict)) or not isinstance(terms[1], string_types):
        _raise_terms_error("first a dict or a list, second a string pointing to the subkey")
    subelements = terms[1].split(".")


# Generated at 2022-06-13 14:13:50.113733
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # set up a mock lookup_loader
    class MockLoader():
        def __init__(self):
            pass

        def get_basedir(self, host):
            return ""

    class MockTemplar():
        def __init__(self):
            pass

        def template(self, value):
            return value

    lookup = LookupModule()
    lookup._loader = MockLoader()
    lookup._templar = MockTemplar()

    # test with a list of dicts
    users = [
        {
            'name': 'admin',
            'authorized': [
                '/tmp/admin/id_rsa.pub'
            ]
        }, {
            'name': 'user1',
            'authorized': [
                '/tmp/user1/id_rsa.pub'
            ]
        }
    ]


# Generated at 2022-06-13 14:13:57.295051
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # all keys should be skipped, the list of targets is empty, the lookup will skip the task
    def test_run_0():
        l = LookupModule({}, [{'skipped': True}], [None, None])
        assert l.run([], []) == []

    # both keys are skipped, each target has a single item
    def test_run_1():
        l = LookupModule({}, [{'skipped': True}, {'skipped': True}], [None, None])
        assert l.run([], []) == []

    # both keys are skipped, one target has a single item, the other a list of two items
    def test_run_2():
        l = LookupModule({}, [{'skipped': True}, {'skipped': True}], [None, None])

# Generated at 2022-06-13 14:14:06.549816
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # create class instance
    lookup = LookupModule()
    # create conf_dict
    conf_dict = {}
    conf_dict['users'] = [
        {'name': 'alice', 'authorized': ['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub'],
         'groups': ['wheel', 'others'], 'mysql': {'password': 'mysql-password', 'hosts': ['db1', 'db2'], 'privs': ['SELECT']}},
        {'name': 'bob', 'authorized': ['/tmp/bob/id_rsa.pub'], 'mysql': {'password': 'pwd', 'hosts': ['%', 'db1', 'db2', 'db3'], 'privs': ['SELECT/INSERT']}}
    ]



# Generated at 2022-06-13 14:14:14.553751
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup_module = LookupModule()

    ###################
    # test invalid input
    ###################

    # no terms
    result = lookup_module.run([], [], **{})
    assert 'expected a list of two or three items' in result[0]

    # no list/dict
    result = lookup_module.run(['this is not a list'], [], **{})
    assert 'first a dict or a list' in result[0]

    # no subkey
    result = lookup_module.run([{'this': 'is not a subkey'}], [], **{})
    assert 'second a string pointing to the subkey' in result[0]

    # invalid third term (must be a dict)

# Generated at 2022-06-13 14:14:23.557439
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test set-up
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.errors import AnsibleError
    from ansible.plugins.lookup.subelements import LookupModule

    terms = ["{{ users }}", "authorized"]
    variables = {}
    kwargs = {}


# Generated at 2022-06-13 14:14:36.124217
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import iteritems

    l = LookupModule()
    l._templar = None
    l._loader = None
    l.set_options({})
    terms = []

# Generated at 2022-06-13 14:14:46.877192
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:14:59.293404
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_instance = LookupModule()

# Generated at 2022-06-13 14:15:06.568313
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class FakeLookupModule(object):
        def __init__(self):
            self._templar = None
            self._loader = None

    lookup = LookupModule()
    lookup.set_loader(FakeLookupModule())

    # test 1
    terms = ['foo', 'bar']
    expected_list = []
    assert lookup.run(terms, None) == expected_list, 'test_LookupModule_run 1 failed'

    # test 2
    terms = [{}, 'bar']
    expected_list = []
    assert lookup.run(terms, None) == expected_list, 'test_LookupModule_run 2 failed'

    # test 3
    terms = [{}, 'bar', []]
    expected_list = []

# Generated at 2022-06-13 14:15:31.563013
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:15:37.734010
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.module_utils._text import to_text
    subelements = LookupModule()
    subelements._templar = None
    subelements._loader = None

    def raise_exception(*args, **kwargs):
        raise AnsibleError("Unexpected input: %s" % str(args))

    terms = [
        [{"a": { "b": 1, "c": [2,"3"] }, "a2": { "c": [3, "3a"] } }],
        "a.c",
        {"skip_missing": False}
    ]

# Generated at 2022-06-13 14:15:50.371441
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.listify import listify_lookup_plugin_terms
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.module_utils.six import string_types
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils._text import to_text
    from ansible.plugins.lookup import LookupBase

    # Fixme: this test is broken, the test data is not correctly loaded,
    #        e.g. users is not a list of dicts
    #        We should split the test_module into a separate test file.

    #############################################################################################
    # Error cases
    #############################################################################################

    # check lookup terms - check number of terms
   

# Generated at 2022-06-13 14:15:58.711398
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    
    from ansible.errors import AnsibleError
    from ansible.module_utils.six import string_types

    l = LookupModule()
    l._templar = None
    l._loader = None

    # test_nesting_1

# Generated at 2022-06-13 14:16:03.231932
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # === tests
    # --- 1
    lookup = LookupModule()
    # --- 2
    try:
        lookup.run([])
        assert False
    except Exception as e:
        if e.message != "subelements lookup expects a list of two or three items, ":
            raise
    # --- 3
    try:
        lookup.run([['a']])
        assert False
    except Exception as e:
        if e.message != "subelements lookup expects a list of two or three items, first a dict or a list, second a string pointing to the subkey":
            raise
    # --- 4

# Generated at 2022-06-13 14:16:14.685439
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = dict()
    terms['test_list'] = [
        {
            'test_dict1': {
                'test_key1': 'test_value1'
            },
            'test_key2': 'test_value2'
        },
        {
            'test_dict2': {
                'test_key1': 'test_value1'
            },
            'test_key2': 'test_value2'
        }
    ]
    terms['test_key1'] = 'test_dict1.test_key1'

    lookup = LookupModule()
    result = lookup.run(terms, None)

    assert(len(result) == 2)

# Generated at 2022-06-13 14:16:24.006455
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # setup test case
    items = [
        {
            "subelement_key_1":
                [
                    "subelement_value_1",
                    "subelement_value_2"
                ]
        },
        {
            "subelement_key_1":
                [
                    "subelement_value_3",
                    "subelement_value_4"
                ]
        },
        {
            "subelement_key_2":
                [
                    "subelement_value_5",
                    "subelement_value_6"
                ]
        }
    ]

# Generated at 2022-06-13 14:16:36.176547
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test vars
    elementlist = [
        {'name': 'alice', 'authorized': ['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub']},
        {'name': 'bob', 'authorized': ['/tmp/bob/id_rsa.pub']}
    ]
    # test cases
    case = {}
    case[0] = dict(
        msg="subelements lookup expects a list of two or three items",
        terms=['item1', 'item2'],
        ret=[],
    )
    case[1] = dict(
        msg="subelements lookup expects a list of two or three items",
        terms=[elementlist, 'authorized', 'item3'],
        ret=[],
    )

# Generated at 2022-06-13 14:16:46.004553
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Setup
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

# Generated at 2022-06-13 14:16:58.114855
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible import context
    from ansible.module_utils.six import PY3
    from ansible.playbook.play_context import PlayContext

    if PY3:
        long = int

    class FakeTemplar:
        def __init__(self):
            self._available_variables = variables

        def template(self, value, convert_bare=True, fail_on_undefined=True, override_vars=None, preserve_trailing_newlines=True):
            return value

    class FakeLoader:
        def __init__(self):
            self._basedir = ''

    class FakeVarManager:
        def __init__(self):
            self._extra_vars = variables

    class FakeOptions:
        def __init__(self):
            self.tags = []

# Generated at 2022-06-13 14:17:25.063067
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()
    #test normal use
    terms = [
       {'test': {'subkey': 'subvalue'}},
       'subkey',
       {'skip_missing': True}]
    ret = lookup_plugin.run(terms, {})
    assert ret == [('subvalue',)]
    #test for missing key
    terms = [
       {'test': {'subkey1': 'subvalue'}},
       'subkey2',
       {'skip_missing': False}]
    try:
        lookup_plugin.run(terms, {})
    except AnsibleError as e:
        assert "could not find 'subkey2' key in iterated item" in str(e)
    else:
        raise Exception("Expected AnsibleError not raised")
    #test for wrong type

# Generated at 2022-06-13 14:17:34.497828
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    from ansible.utils.listify import listify_lookup_plugin_terms
    from ansible.module_utils.six import binary_type

    def do_test(terms, expected, **kwargs):
        if isinstance(terms, string_types):
            terms = listify_lookup_plugin_terms(terms, loader=FakeLoader(), templar=FakeTemplar())

        ret = LookupModule().run(terms=terms, variables=FakeVars(), **kwargs)

        # the ret is a list of tuples and we have to compare those:
        if not isinstance(ret, list):
            raise AssertionError("expected a list, got %s" %
                                 binary_type(type(ret)))
        if not isinstance(expected, list):
            expected = listify_lookup_plugin_

# Generated at 2022-06-13 14:17:46.814709
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.errors import AnsibleError
    import pytest
    from itertools import izip


# Generated at 2022-06-13 14:17:57.283140
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    LookupModule.run() Test

    This is not really unit testing: the request is build with the
    following parameters, then run() is called and the result is
    checked.
    """

# Generated at 2022-06-13 14:18:09.227828
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.plugins.lookup as lookup
    lookup.PLUGIN_PATH = None

    # first term is a dict, second is a subkey
    # skip_missing is False
    terms = [{"skipped": True}, "key"]
    terms = listify_lookup_plugin_terms(terms)
    expected = []
    assert expected == LookupModule().run(terms, variables=dict())

    # first term is a dict, second is a subkey
    # skip_missing is False
    terms = [{"skipped": False, "key": None}, "key"]
    terms = listify_lookup_plugin_terms(terms)
    expected = []
    assert expected == LookupModule().run(terms, variables=dict())

    # first term is a dict, second is a subkey
    # skip_missing is False
   

# Generated at 2022-06-13 14:18:16.663085
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """ Define the tests for method run of class LookupModule.

    """
    vars = {}
    terms = [
            {
                'skipped': True
            },
            'skipped'
            ]
    expected = []
    lookup = LookupModule().run(terms, vars)
    assert lookup == expected, "Should return %s, but returned %s" % (expected, lookup)

    # create a test term valid test term
    terms = [
            [
                {
                    'skipped': True
                },
                {
                    'skipped': False,
                    'foo': 'bar'
                }
            ],
            'foo'
            ]
    expected = [('bar',)]
    lookup = LookupModule().run(terms, vars)

# Generated at 2022-06-13 14:18:22.131624
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    # load the subelements lookup module
    subelements_lookup_plugin = LookupModule()

    # set up loader and variablemanager
    loader = DataLoader()
    vars_manager = VariableManager()

    # test case
    # get mysql users from users list

# Generated at 2022-06-13 14:18:25.542079
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    The unit test provides access to the private run method of class LookupModule
    """
    lookup_obj = LookupModule()
    assert hasattr(lookup_obj, 'run')
    assert callable(lookup_obj.run)

# Generated at 2022-06-13 14:18:38.152356
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:18:48.782981
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.vars.hostvars import HostVars
    from ansible.vars.reserved import VariableManager
    from ansible.utils.vars import combine_vars

    class MyLookupBase(LookupBase):
        def run(self, terms, variables=None, **kwargs):
            return terms


# Generated at 2022-06-13 14:19:30.660193
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    lookup = LookupModule()
    print('Current directory: %s' % os.path.abspath(os.curdir))

# Generated at 2022-06-13 14:19:44.006586
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.common._collections_compat import OrderedDict
    from ansible.module_utils.parsing.convert_bool import boolean


# Generated at 2022-06-13 14:19:53.398603
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:20:04.559897
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    import pytest

    mylookup = LookupModule()


# Generated at 2022-06-13 14:20:15.546385
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    terms = [
        [   # first_term
            {'name': 'alice', 'authorized': ['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub']},
            {'name': 'bob', 'authorized': ['/tmp/bob/id_rsa.pub']},
        ],
        "authorized",    # second term
    ]
    flags = {
        'skip_missing': False,
    }

    # init class vars
    lookupmodule_obj = LookupModule()
    lookupmodule_obj._templar = ''
    lookupmodule_obj._loader = ''

    r = lookupmodule_obj.run(terms, {}, flags=flags)

    assert isinstance(r, list)
    assert len(r) == 2

# Generated at 2022-06-13 14:20:26.820242
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Success: the function run returns a list
    lookup_module = LookupModule()
    terms = [
        [
            {
                'key_0': {
                    'key_1': [
                        'key_1_leaf_0',
                        'key_1_leaf_1'
                    ]
                },
                'key_1': {
                    'key_1_key_0': {
                        'key_2': [
                            'key_2_leaf_0'
                        ]
                    }
                }
            }
        ],
        ['key_0', 'key_1', 'key_2']
    ]
    result = lookup_module.run(terms, {})

# Generated at 2022-06-13 14:20:37.411791
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.listify import listify_lookup_plugin_terms
    from ansible.errors import AnsibleError
    """subelements:
        description: traverse nested key from a list of dictionaries
        options:
          _terms:
             description: tuple of list of dictionaries and dictionary key to extract
             required: True
          skip_missing:
            default: False
            description:
              - Lookup accepts this flag from a dictionary as optional. See Example section for more information.
              - If set to C(True), the lookup plugin will skip the lists items that do not contain the given subkey.
              - If set to C(False), the plugin will yield an error and complain about the missing subkey.
    """

    # alice
    # authorized:
    #   - /tmp/alice/onekey.pub
    #   -

# Generated at 2022-06-13 14:20:49.655016
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test 1: test if subelements lookup returns a list of tuples
    users1 = [
        {
            'name': 'alice',
            'authorized': [
                '/tmp/alice/onekey.pub',
                '/tmp/alice/twokey.pub'
            ],
        },
        {
            'name': 'bob',
            'authorized': [
                '/tmp/bob/id_rsa.pub'
            ],
        }
    ]
    lookup_module = LookupModule()
    result = lookup_module.run([users1, 'authorized'], {})

# Generated at 2022-06-13 14:20:59.972940
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Test lookup method with an example from the documentation,
    """

    from ansible.executor import task_result

    users = [
        dict(name='alice', authorized=['/tmp/alice/one.pub', '/tmp/alice/two.pub']),
        dict(name='bob', authorized=['/tmp/bob/id_rsa.pub']),
        dict(name='carol'),
    ]

    # Unit test without skip_missing
    lu = LookupModule()
    assert lu.run((users, 'authorized')) == [
        (users[0], users[0]['authorized'][0]),
        (users[0], users[0]['authorized'][1]),
        (users[1], users[1]['authorized'][0]),
    ]

    # Unit test with

# Generated at 2022-06-13 14:21:12.109882
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    # smoke tests
    lm.run(['a'], [])
    lm.run([5], [])
    lm.run([1, 2, 3], [])
    lm.run({'foo': 1, 'bar': 2}, [])
    # Real tests

# Generated at 2022-06-13 14:22:27.238900
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    # test case(s)

# Generated at 2022-06-13 14:22:34.115954
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.executor.task_queue_manager import TaskQueueManager


# Generated at 2022-06-13 14:22:42.375569
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    # test subelement key not found error
    terms = [
        [{"a": {"b": [1, 2, 3]}, "c": {"b": [4, 5, 6]}}],
        "a.d"
    ]
    ret = module.run(terms, None)
    assert ret == [], "check for the KeyError in case subelement key is not found"
    # test nested subelements (a.c.b)
    terms = [
        [{"a": {"b": [1, 2, 3], "c": {"b": [4, 5, 6]}}, "d": {"b": [7, 8, 9]}}],
        "a.c.b"
    ]
    ret = module.run(terms, None)

# Generated at 2022-06-13 14:22:53.728048
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    #setup_test
    from ansible.parsing.dataloader import DataLoader

    # test
    loader = DataLoader()
    lookup_plugin = LookupModule(loader=loader)

# Generated at 2022-06-13 14:23:06.530123
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    terms = [
        [
            {'name': 'alice'},
            {'name': 'bob'},
        ],
        'name',
    ]
    flags = [
        {'skip_missing': True},
        {'skip_missing': False},
        {},
    ]

    assert lookup_module.run(terms, None) == [('alice',), ('bob',)]

    # make sure the flag is respected
    # Note that this test uses the mock_loader and mock_templar
    # which do not implement the boolean_conversion.
    # This is the reason why the lookup_module.run() test needs
    # to explicitly call the boolean() function.
    for flag in flags:
        terms[2] = flag

# Generated at 2022-06-13 14:23:18.922733
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import json
    import sys
    import os

    # create an instance of LookupModule
    lookup = LookupModule()

    # check run method without parameter
    try:
        lookup.run([])
        assert False, "should raise an exception"
    except Exception as e:
        assert e.message == "subelements lookup expects a list of two or three items, "

    # check run method with five parameters
    try:
        lookup.run([1, 2, 3, 4, 5])
        assert False, "should raise an exception"
    except Exception as e:
        assert e.message == "subelements lookup expects a list of two or three items, "

    # check run method with first parameter not being a list or dict

# Generated at 2022-06-13 14:23:31.534385
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    assert lookup.run(["{{ groups }}", 'users'], {'groups': [{'name': 'wheel', 'users': ['alice', 'bob']}]}, **dict()) == \
           [({'name': 'wheel', 'users': ['alice', 'bob']}, 'alice'), ({'name': 'wheel', 'users': ['alice', 'bob']}, 'bob')]