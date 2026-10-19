

# Generated at 2022-06-13 14:13:43.083266
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    import os
    import tempfile
    import datetime
    import time
    import unittest
    from ansible.parsing.dataloader import DataLoader
    from ansible.module_utils.six import PY3
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager


    class TestLookupModule(unittest.TestCase):

        def setUp(self):
            """ create a fake inventory and playbook """
            self.loader = DataLoader()
            self.loader.set_basedir(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))

# Generated at 2022-06-13 14:13:51.841300
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # test with terms containing a string instead of a list or dict
    terms1 = ['foo']
    terms2 = ['users', 'authorized']
    terms3 = ['users', 'authorized', 'skip_missing']
    terms4 = ['users', 'authorized', {'skip_missing': True}]
    terms5 = ['users', 'authorized', {'skip_missing': False}]
    for terms in [terms1, terms2, terms3, terms4, terms5]:
        try:
            lookup.run(terms, None)
        except AnsibleError as e:
            continue
        print("Should raise AnsibleError: terms: %s" % terms)

    # test with a string instead of a list
    terms1 = ['users', 'authorized']

# Generated at 2022-06-13 14:13:59.991639
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    # input = '<walked-list-of-dicts>,<subkey>,[<optional-dict-with-flags>]'
    input = '[{"a": {"b": {"c": [1, 2, 3]}}}],a.b.c'
    # result is a list of tuples, with one tuple per subelement
    result = lookup.run([input], None)
    print(result)
    assert result == [({'a': {'b': {'c': [1, 2, 3]}}}, 1), ({'a': {'b': {'c': [1, 2, 3]}}}, 2), ({'a': {'b': {'c': [1, 2, 3]}}}, 3)]
    # if the dict of flags is given, these flags are taken into account

# Generated at 2022-06-13 14:14:10.285832
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    #########################################################
    #### Importing module                                 ###
    #########################################################
    from ansible.plugins.lookup.subelements import LookupModule

    class MockModule(object):
        def __init__(self):
            self.params = {}
            self.args = []
            self.result = {}

    class MockTemplar(object):
        def __init__(self):
            self.environment = []
            self.result = {}

    class MockLoader(object):
        def __init__(self):
            self.path_exists_result = True
            self.path_exists_mock = ''

        def path_exists(self, path):
            if path == '/etc/authorized_keys/bob':
                return self.path_exists_result

# Generated at 2022-06-13 14:14:21.191530
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Creation of a lookup module for testing
    lookup_module = LookupModule()

    # Test exception on bad parameters
    try:
        lookup_module.run(terms=list(), variables=dict(), **dict())
        assert False
    except AnsibleError as e:
        assert "subelements lookup expects a list of two or three items, " in e.message

    try:
        lookup_module.run(terms=list(['a', 0, 'b'],), variables=dict(), **dict())
        assert False
    except AnsibleError as e:
        assert "items, first a dict or a list, second a string pointing to the subkey" in e.message


# Generated at 2022-06-13 14:14:34.042373
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    term = [{'first_key': {'second_key': [{'third_key': 'third_value'}, {'third_key': 'third_value2'}]}}]
    subkey = "second_key.third_key"
    r = LookupModule().run([term, subkey], {})
    assert r == [({'second_key': [{'third_key': 'third_value'}, {'third_key': 'third_value2'}]}, 'third_value'),
                 ({'second_key': [{'third_key': 'third_value'}, {'third_key': 'third_value2'}]}, 'third_value2')]


# Generated at 2022-06-13 14:14:43.925666
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible.plugins.loader import lookup_loader
    LookupModule = lookup_loader._get_lookup_plugin('subelements')


# Generated at 2022-06-13 14:14:51.642837
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.parsing.convert_bool import boolean

    assert LookupModule().run([], {}, **{}) == []
    assert LookupModule().run([None], {}, **{}) == []
    assert LookupModule().run([1], {}, **{}) == []
    assert LookupModule().run([1, {}], {}, **{}) == []
    assert LookupModule().run([[], {}], {}, **{}) == []
    assert LookupModule().run([[], 'key'], {}, **{}) == []
    assert LookupModule().run([[1], 'key'], {}, **{}) == []
    assert LookupModule().run([[{'key': 'value'}], 'key'], {}, **{}) == [({'key': 'value'}, 'value')]

# Generated at 2022-06-13 14:15:03.931304
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # init
    users = [
            {'name': 'alice', 'authorized': ['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub'],
             'mysql': {'password': 'mysql-password', 'hosts': ['%', '127.0.0.1', '::1', 'localhost'],
                       'privs': ['*.*:SELECT', 'DB1.*:ALL']}, 'groups': ['wheel']},
            {'name': 'bob', 'authorized': ['/tmp/bob/id_rsa.pub'], 'mysql': {'password': 'other-mysql-password', 'hosts': ['db1'],
                    'privs': ['*.*:SELECT', 'DB2.*:ALL']}}
            ]


# Generated at 2022-06-13 14:15:13.359929
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    _templar = None
    _loader = None
    _shared_loader_obj = None
    _display = None

    lookup = LookupModule(templar=_templar, loader=_loader,
                          shared_loader_obj=_shared_loader_obj, display=_display)


# Generated at 2022-06-13 14:15:30.657246
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # the type of all parameters is checked in the class already
    # just make a list of values we expect to get back

    # test all permutations of how run may receive the arguments
    # the method will normalize it to a list of lists
    testparams = [
        [],
        [[]],
        [{}],
        [[], 1],
        [{}, 1],
        [[], '', 1],
        [{}, '', 1],
    ]

    for params in testparams:
        # py3 does not allow create a class instance without calling __init__()
        # so we just call it with dummy values
        myclass = LookupModule(loader=None, templar=None, variables=None)
        # now we can do the test and check if we get the expected result

# Generated at 2022-06-13 14:15:42.400262
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create an instance of LookupModule class
    lookup = LookupModule()

    # Set the vars of lookup module
    vars = dict()

    # Set the ansible options
    options = dict()

    # create testdata for test
    # 1. not a list
    try:
        lookup.run('test', vars, options)
        assert False, "lookup did not raise an error while expecting a list but got a string"
    except:
        # expected error, everything is fine
        pass

    # 2. a list but not the right length

# Generated at 2022-06-13 14:15:54.179854
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import pytest
    from ansible.module_utils.six import string_types as _string_types
    from ansible.module_utils.six import integer_types as _integer_types

    params = []
    with pytest.raises(AnsibleError):
        LookupModule().run(params, None)

    params = [ 'abc' ]
    with pytest.raises(AnsibleError):
        LookupModule().run(params, None)

    params = [
        [
            {
                'skipped': True,
                'other': {
                    'color': [ 'red', 'green', 'blue' ]
                }
            },
            { 'skipped': True }
        ],
        'other.color'
    ]
    assert LookupModule().run(params, None) == []


# Generated at 2022-06-13 14:16:04.808001
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.plugins.lookup.subelements
    import ansible.plugins.lookup_loader

# Generated at 2022-06-13 14:16:11.571819
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # default value for skip_missing is False
    # wrong type for skip_missing
    # skip_missing set to True
    # no dictionary in the first list item
    # no subkey in the dictionary
    # subkey points to a wrong type
    # subkey points to a list
    # one subkey level
    # two subkey levels
    # three subkey levels
    # a skip flag in the first list item
    # a skip flag in each item of the first list
    # a skip flag in the first list item and a subkey that is missing
    return None

# Generated at 2022-06-13 14:16:17.297509
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Arrange
    m = LookupModule()
    module_utils_parsing_convert_bool = m.get_option('module_utils/parsing/convert_bool')
    self.assertEqual(['subelements', 'boolean'], sorted(list(module_utils_parsing_convert_bool)))
    # Act
    # Assert

# Generated at 2022-06-13 14:16:23.641137
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:16:35.978062
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import random
    import copy

    # initialize LookupModule
    lookup_module = LookupModule()

    # define data structures

# Generated at 2022-06-13 14:16:46.233289
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    # wrong number of terms:
    # - no term
    with pytest.raises(AnsibleError) as exec_info:
        lookup_module.run([], {})
    assert "subelements lookup expects a list of two or three items" in str(exec_info)

    # - one term
    with pytest.raises(AnsibleError) as exec_info:
        lookup_module.run([[]], {})
    assert "subelements lookup expects a list of two or three items" in str(exec_info)

    # - three terms
    with pytest.raises(AnsibleError) as exec_info:
        lookup_module.run([[], '', {}], {})

# Generated at 2022-06-13 14:16:58.502808
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup.subelements import LookupModule
    kl = LookupModule()
    terms = dict(
        elementlist=[
            dict(
                a=dict(
                    b=dict(
                        c=["abc1", "abc2", "abc3"]
                    )
                )
            ),
            dict(
                a=dict(
                    b=dict(
                        c=["abc4", "abc5", "abc6"]
                    )
                )
            )
        ],
        subkey="a.b.c"
    )

# Generated at 2022-06-13 14:17:21.007639
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:17:32.152920
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Mock variables
    class MockVarsModule:
        def __init__(self, hash):
            self.hash = hash
        def __getattr__(self, item):
            return self.hash[item]


# Generated at 2022-06-13 14:17:44.844230
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """ Unit test of method ansible.plugins.lookup.subelements.LookupModule.run """
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.utils.listify import listify_lookup_plugin_terms

    print("=== subelements test ===")
    users = {
            'alice': {'authorized': ['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub'], 'blah': 'blub'},
            'bob': {'authorized': ['/tmp/bob/id_rsa.pub'], 'blah': 'blub'},
            'charlie': {'authorized': ['/tmp/charlie/ssh_key.pub'], 'blah': 'blub'}
            }
    print

# Generated at 2022-06-13 14:17:55.947007
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_subelements = LookupModule()
    assert test_subelements._templar is None
    assert test_subelements._loader is None

    # testing for a non list or dict first term
    terms = [[1, 2, 3], 'subkey']
    actual = test_subelements.run(terms, None)
    assert actual == [[1, 'subkey'], [2, 'subkey'], [3, 'subkey']]

    # testing for a non string second term
    terms = [{'subkey': [1, 2, 3]}, ['subkey']]
    try:
        actual = test_subelements.run(terms, None)
    except Exception as e:
        assert e.message == "subelements lookup expects a dictionary, got '%s'" % ['subkey']

    # testing

# Generated at 2022-06-13 14:18:05.234470
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # lookup in non-dict, non-list
    from ansible.errors import AnsibleError
    from ansible.module_utils.six import string_types
    from ansible.module_utils.parsing.convert_bool import boolean

    terms = [1, 'a']
    flags = {'skip_missing': False}
    subelements_key = 'a'

    assert isinstance(subelements_key, string_types)
    assert subelements_key == 'a'

    try:
        LookupModule().run(terms, flags)
        raise AssertionError("expected exception")
    except AnsibleError as ae:
        assert 'subelements lookup expects a list' in ae.message

    # lookup in list
    terms = [[{'a': 1}, {'a': 2}], 'a']

# Generated at 2022-06-13 14:18:17.026554
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule.run(None, [[{'foo':{'bar':[1, 2]}}], 'foo.bar']) == [[{'foo': {'bar': [1, 2]}}, 1], [{'foo': {'bar': [1, 2]}}, 2]]
    assert LookupModule.run(None, [[{'foo':{'bar':[1, 2]}}], 'foo.bar.baz']) == []

# Generated at 2022-06-13 14:18:24.794272
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test with arguments terms=[ [dict, dict], string, dict ]
    import pytest

    with pytest.raises(AnsibleError) as excinfo:
        LookupModule().run([{"a":2, "b":1}, "b", {'skip_missing': True}], {})
    assert excinfo.value.args[0] == "first a dict or a list, second a string pointing to the subkey"

    # Test with arguments terms=[ [dict, dict], string ]
    terms = [ [{"a":2, "b":1}, {"a":3, "b":2}], "a" ]
    assert LookupModule().run(terms, {}) == [ ({"a":2, "b":1},{"a":2}), ({"a":3, "b":2},{"a":3}) ]

    # Test with

# Generated at 2022-06-13 14:18:37.534703
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', "..", "lib"))
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.plugins.lookup.subelements import LookupModule
    from ansible.errors import AnsibleError

    # dictionary used in tests

# Generated at 2022-06-13 14:18:48.198434
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Create an object of class LookupModule
    object = LookupModule()

    # Create a dictionary named 'users'
    users = { "alice": {"authorized": [ '/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub' ] }, "bob": {"authorized": [ '/tmp/bob/id_rsa.pub' ]} }
    expected_result = [('alice', '/tmp/alice/onekey.pub'), ('alice', '/tmp/alice/twokey.pub'), ('bob', '/tmp/bob/id_rsa.pub')]

    # Create an array
    terms = []

    # Add element to array
    terms.append(users)
    terms.append('authorized')

    # Call method 'run' of class LookupModule

# Generated at 2022-06-13 14:19:00.721830
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # set up test data and a LookupModule instance
    data = dict(
        users=dict(
            alice=dict(
                authorized=dict(
                    keys=["'/tmp/alice/onekey.pub'", "'/tmp/alice/twokey.pub'"])),
            bob=dict(
                authorized=dict(
                    keys=["'/tmp/bob/id_rsa.pub'"]))))
    lm = LookupModule()
    # test with a single term tuple with non-existing key
    terms = [data, "users.bob.authorized.foo"]
    lm.run(terms, None)
    # test with a list of term tuples with non-existing key and skip_missing=True
    terms = []

# Generated at 2022-06-13 14:19:30.767840
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert False


# Generated at 2022-06-13 14:19:44.132534
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create ansible fake variables
    variables = {}
    # Create ansible fake loader
    loader = None
    # Create ansible fake templar
    templar = None

    # Create ansible fake lookup
    lookup = LookupModule(loader=loader, templar=templar, variables=variables)
    # Create ansible fake terms
    terms = [
        [{"name": "alice", "authorized": ["/tmp/alice/onekey.pub", "/tmp/alice/twokey.pub"], "groups": ["wheel"]},
         {"name": "bob", "authorized": ["/tmp/bob/id_rsa.pub"]}],
        "authorized",
        {"skip_missing": True}
    ]
    # The expected result after the lookup has run

# Generated at 2022-06-13 14:19:53.462406
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    terms = [
        [],
        'authorized',
        {'skip_missing': False}
    ]
    try:
        module.run(terms, [])
        assert False
    except AnsibleError as e:
        assert 'requires a list' in str(e)

    terms = [
        [
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
        'authorized',
        {'skip_missing': True}
    ]

# Generated at 2022-06-13 14:20:04.603821
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup import LookupModule

    fixtures = [{'item0': {'item1': "result"}, 'item1': "result"}, {'item0': {'item1': "result2"}, 'item1': "result2"}]

    def test_return(result, expected):
        assert_equal(result, expected, "Error in LookupModule.run")

    ###############
    ## 1 argument
    ###############
    test_return(LookupModule().run([], None), [])
    test_return(LookupModule().run([{'item0': fixtures[0], 'item1': fixtures[0]}], None), fixtures)

# Generated at 2022-06-13 14:20:15.584380
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    users = [
        {'name': 'alice', 'authorized': ['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub'], 'groups': ['wheel']},
        {'name': 'bob', 'authorized': ['/tmp/bob/id_rsa.pub']}
    ]

    lookup = LookupModule()

# Generated at 2022-06-13 14:20:26.872294
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from nose.tools import assert_equal
    from ansible.plugins.lookup import LookupBase
    from ansible.module_utils.six import string_types
    from ansible.errors import AnsibleError

    ################################################################################
    #
    # test private method _raise_terms_error
    #
    ################################################################################

    # test error message raise
    try:
        lookup = LookupModule()
        lookup._raise_terms_error("test-message")
        assert False, "Expected an exception"
    except Exception as e:
        assert_equal("subelements lookup expects a list of two or three items, " + "test-message", e.message)

    ################################################################################
    #
    # test method run
    #
    ################################################################################

    # test error message for

# Generated at 2022-06-13 14:20:35.473915
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Tests for method run of class LookupModule
    elem = {'all': '', 'changed': False, '_ansible_no_log': False, '_ansible_item_result': True, 'failed': False}
    item = {'item0': "{{ lookup('template', 'template0.j2') }}", 'item1': "{{ lookup('template', 'template1.j2') }}"}
    assert LookupModule.run(["{{ lookup('template', 'template0.j2') }}", "{{ lookup('template', 'template1.j2') }}"], elem) == item


# Generated at 2022-06-13 14:20:46.612929
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import json
    import pprint
    import sys
    import os

    def compare_with_real_file(test_file,result_file):
        filein = open(test_file)
        test_json_in = json.load(filein)
        filein.close()
        filetest = open(result_file)
        test_json_test = json.load(filetest)
        filetest.close()
        if test_json_in == test_json_test:
            print("\nTest file "+test_file+" looks OK")
        else:
            raise AssertionError("\nTest file "+test_file+" differs from result \n"+pprint.pformat(test_json_in)+"\n"+pprint.pformat(test_json_test))


# Generated at 2022-06-13 14:20:58.207069
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # First test if wrong arguments raise exception
    assert 2 <= len(sys.argv) <= 3
    terms = [ sys.argv[1], sys.argv[2] ]
    if len(sys.argv) == 4:
        terms.append(sys.argv[3])

    # Initialize LookupModule object
    init = {
        '_templar': '',
        '_loader': ''
    }
    lookup = LookupModule(**init)

    # Call run method of Class LookupModule
    res = lookup.run(terms, [])

    # Print result
    sys.stdout.write('[')
    for e in res:
        sys.stdout.write('[')
        for el in e:
            if el.__class__.__name__ == 'dict':
                sys.std

# Generated at 2022-06-13 14:21:09.348117
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.utils.listify import listify_lookup_plugin_terms

    # Test with wrong terms type
    terms = (1, 2)
    variables = {}
    lookup = LookupModule()
    try:
        lookup.run(terms, variables)
        assert False, 'Wrong terms type accepted!'
    except AnsibleError as e:
        pass

    # Test with wrong terms list lenght
    terms = (1, 2, 3, 4)
    variables = {}
    lookup = LookupModule()
    try:
        lookup.run(terms, variables)
        assert False, 'Wrong terms list lenght accepted!'
    except AnsibleError as e:
        pass

    # Test with terms of wrong type

# Generated at 2022-06-13 14:22:23.424606
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import pytest

    from ansible.utils.listify import listify_lookup_plugin_terms
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    from ansible.plugins.lookup.subelements import LookupModule

    class MockVars(object):

        def __init__(self, users):
            class MockUnsafeText(AnsibleUnsafeText):

                def __init__(self, s):
                    super(MockUnsafeText, self).__init__(s)


# Generated at 2022-06-13 14:22:36.121087
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # create instance for the unit test
    lookup_module = LookupModule()

    # create test case to test the run method of class LookupModule

# Generated at 2022-06-13 14:22:49.527010
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.module_utils.six import PY3
    from ansible.module_utils.six.moves import builtins
    import io

    if PY3:
        builtin_module = 'builtins'
    else:
        builtin_module = '__builtin__'


# Generated at 2022-06-13 14:22:50.019243
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 14:23:02.442338
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit testing for the method run of LookupModule
    """
    # fake the __init__ method
    class FakeLookupModule():
        def __init__(self):
            self._loader = None

    fake_lookup_module = FakeLookupModule()

    # fake some values

# Generated at 2022-06-13 14:23:14.003713
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Check for non-dictionary variable
    with pytest.raises(AnsibleError) as err:
        LookupModule().run(terms=[None, "foo"], variables={}, **{})
    assert err.value.message == "subelements lookup expects a dictionary, got 'None'"
    # Check for non-list variable
    with pytest.raises(AnsibleError) as err:
        LookupModule().run(terms=["foo", "bar"], variables={}, **{})
    assert err.value.message == "subelements lookup expects a dictionary, got 'foo'"
    # Check for non-list variable
    with pytest.raises(AnsibleError) as err:
        LookupModule().run(terms=[{}, None], variables={}, **{})

# Generated at 2022-06-13 14:23:26.222633
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    t = LookupModule()
    terms = [
        [{'name': 'alice', 'authorized': ['/tmp/alice/onekey.pub',
                                          '/tmp/alice/twokey.pub'], 'groups': ['wheel']},
         {'name': 'bob', 'authorized': ['/tmp/bob/id_rsa.pub']}],
        'authorized'
    ]
    ret = [
        ({'name': 'alice', 'groups': ['wheel']}, '/tmp/alice/onekey.pub'),
        ({'name': 'alice', 'groups': ['wheel']}, '/tmp/alice/twokey.pub'),
        ({'name': 'bob'}, '/tmp/bob/id_rsa.pub')
    ]
    assert t.run(terms, {})