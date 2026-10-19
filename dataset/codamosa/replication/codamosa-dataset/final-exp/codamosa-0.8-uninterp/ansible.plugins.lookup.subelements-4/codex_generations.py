

# Generated at 2022-06-13 14:13:47.041674
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:13:53.265860
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_value = [{'name': 'key1', 'mysql': {'hosts': ['db1', 'db2'], 'password': 'secret'}}]
    terms = [[test_value], 'mysql.hosts']

    # create a valid lookup module
    lookup = LookupModule()

    # test run method
    assert lookup.run(terms, None) == [(test_value[0], 'db1'), (test_value[0], 'db2')]



# Generated at 2022-06-13 14:14:00.765643
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils.parsing.splitter import parse_kv
    import yaml

    # generating test data

# Generated at 2022-06-13 14:14:10.792730
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test case 1:
    # test empty list, should not pass
    lookup_instance = LookupModule()
    assert lookup_instance.run([], {}, {}) == []

    # Test case 2:
    # test list of two items, where first item is not string or list or dict, should not pass
    # test list of two items, where second item is not string, should not pass
    lookup_instance = LookupModule()
    assert lookup_instance.run([5, 'nothing'], {}, {}) == []
    lookup_instance = LookupModule()
    assert lookup_instance.run([[], 5], {}, {}) == []

    # Test case 3:
    # test list of two items, where first item is empty list, should not pass
    # test list of two items, where second item is empty string, should not pass
    lookup

# Generated at 2022-06-13 14:14:21.573199
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import __builtin__
    # mock function, that returns the given value
    def mock_AnsibleError(*args, **kwargs):
        raise Exception

    def mock_boolean(*args, **kwargs):
        return True

    def mock_isinstance(*args, **kwargs):
        return True

    # patch ansible imports
    path_to_module = "ansible.plugins.lookup.subelements"
    lookup_module_name = "LookupModule"
    # patch the AnsibleError method
    setattr(__builtin__, "AnsibleError", mock_AnsibleError)
    # patch the boolean method of the ansible.module_utils.parsing.convert_bool module
    setattr(__builtin__, "boolean", mock_boolean)
    # patch the isinstance method of

# Generated at 2022-06-13 14:14:34.668730
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Unit test, testing method 'run' of class LookupModule"""
    # example/test data
    users = [
        {'name': 'alice', 'authorized': ['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub'], 'groups': ['wheel']},
        {'name': 'bob', 'authorized': ['/tmp/bob/id_rsa.pub'], 'groups': []},
        {'name': 'charlie', 'authorized': [], 'groups': ['wheel']}]
    groups = {'wheel': ['alice', 'charlie'], 'users': ['bob']}

    # test cases

# Generated at 2022-06-13 14:14:42.809886
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()


# Generated at 2022-06-13 14:14:51.128281
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # used to be able to use the same tests for ansible 1.x and ansible 2.x
    try:
        from ansible.module_utils.ansible.module import AnsibleModule
        module = AnsibleModule
        ansible_module_kwargs = {}
    except:
        from ansible.module_utils._text import to_text
        from ansible.module_utils.basic import AnsibleModule
        from ansible.module_utils.six.moves import cStringIO as StringIO
        module = AnsibleModule
        ansible_module_kwargs = {'_ansible_selftest': True}

    # used for initialisation of LookupModule object

# Generated at 2022-06-13 14:15:03.515402
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = [
        [
            {'user1': {'host': ['host one', 'host two']}},
            {'user2': {'host': ['host one', 'host three']}},
            {'user3': {'hosts': ['host four', 'host five']}}
        ],
        'host'
    ]
    assert len(LookupModule().run(terms=terms, variables={})) == 4
    assert len(LookupModule().run(terms=[], variables={})) == 0
    try:
        LookupModule().run(terms=[], variables={})
    except AnsibleError as e:
        assert 'subelements lookup expects a list of two or three items' in str(e)


# Generated at 2022-06-13 14:15:13.071307
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # build a mock templar
    test_module_utils_parsing_convert_bool_boolean_result = True
    from ansible.module_utils.parsing.convert_bool import boolean as mock_boolean
    def mock_test_module_utils_parsing_convert_bool_boolean(*args, **kwargs):
        if args[0] == False:
            return False
        else:
            return test_module_utils_parsing_convert_bool_boolean_result
    mock_boolean.side_effect = mock_test_module_utils_parsing_convert_bool_boolean

    lookup_module = LookupModule()
    lookup_module.set_loader({
        "some_variable": "value"
    })

    # prepare test data
    testdata_

# Generated at 2022-06-13 14:15:27.731456
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    terms = [[{'john': {'name': 'john', 'authorized': ['/home/john/.ssh/authorized_keys']}}], 'john.authorized']
    assert lookup_module.run(terms, {}) == [[{'john': {'name': 'john', 'authorized': ['/home/john/.ssh/authorized_keys']}}, '/home/john/.ssh/authorized_keys']]



# Generated at 2022-06-13 14:15:39.853476
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l.set_loader()

    # test: test 1, list of dictionaries, 1 subkey, optional flags
    terms = [
        [
            {"name": "alice", "authorized": [{"name": "key1", "read": False}, {"name": "key2", "read": True}]},
            {"name": "bob", "authorized": [{"name": "key3", "read": False}, {"name": "key4", "read": True}]},
        ],
        "authorized",
        {'skip_missing': True},
    ]
    ret = l.run(terms, {})

# Generated at 2022-06-13 14:15:52.958665
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    if sys.version_info[:2] < (2, 7) or sys.version_info[:2] in (3, 0):
        print("FATAL: Python-2.7 or higher is required for this test")
        sys.exit()


# Generated at 2022-06-13 14:16:03.889340
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible import __version__
    from ansible.utils.listify import listify_lookup_plugin_terms
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable

    class TestLookupModule(LookupModule):
        def __init__(self, terms, variables=None):
            self.__dict__.update(locals())

        def run(self, **kwargs):
            return super(TestLookupModule, self).run(terms=self.terms, variables=self.variables, **kwargs)


# Generated at 2022-06-13 14:16:13.634176
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    class FakeLookupModule(LookupModule):

        def __init__(self):
            self._loader = None
            self._templar = None
            self._available_variables = None

    lookup_module = FakeLookupModule()

    # test case successful: two items in list
    lookup_module.run([[{"key1": "value1", "key2": "value2"}, {"key1": "value3", "key2": "value4"}], "key1"], {})

    # test case successful: skip_missing on second term
    lookup_module.run([[{"key1": "value1"}, {"key1": "value3", "key2": ["value4", "value4"]}], "key2", {"skip_missing": False}], {})

    # test case successful: three item in list (1 flag)
   

# Generated at 2022-06-13 14:16:23.254859
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    assert module.run([[{"key": "value"}], "key"], {}) == [("value",)]
    assert module.run([[{"key": "value"}, {"key": "value2"}], "key"], {}) == \
           [("value",), ("value2",)]
    assert module.run([[{"key": "value"}, {"key2": "value2"}], "key"], {}) == \
           [("value",)]
    assert module.run([[{"key": {"subkey": "value"}}, {"key": "value2"}], "key.subkey"], {}) == \
           [("value",)]
    assert module.run([[{"key": "value"}, {"key": {"subkey": "value2"}}], "key"], {}) == \
           [("value",)]

# Generated at 2022-06-13 14:16:35.736743
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Unit test 1:
    # Example with list of dictionaries
    terms = [[{'name': 'Alice'}, {'name': 'Bob'}], 'name']
    lookup_plugin = LookupModule()
    ret = lookup_plugin.run(terms, None)
    assert isinstance(ret, list)
    assert len(ret) == 2
    assert isinstance(ret[0][0], dict)
    assert isinstance(ret[0][1], string_types)
    assert isinstance(ret[1][0], dict)
    assert isinstance(ret[1][1], string_types)

    # Unit test 2:
    # Example with a list of list
    terms = [[['Alice'], ['Bob']], '0']
    ret = lookup_plugin.run(terms, None)
    assert isinstance(ret, list)

# Generated at 2022-06-13 14:16:45.572232
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # mock the super class of LookupModule
    class Mock_LookupBase(object):
        def __init__(self):
            self.invoked = False
        def set_options(self, varargs, kwargs):
            pass
    class Mock_Templar(object):
        def __init__(self):
            self.invoked = False
    class Mock_Loader(object):
        def __init__(self):
            self.invoked = False

    # mock the AnsibleError class
    class Mock_AnsibleError(object):
        def __init__(self, msg):
            assert msg

    # pretend that AnsibleError is already there
    import sys
    sys.modules['ansible.errors'] = sys.modules['__main__']
    from ansible.errors import AnsibleError
    del sys.modules

# Generated at 2022-06-13 14:16:46.388523
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass


# Generated at 2022-06-13 14:16:58.670767
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test with no flags
    subelement = LookupModule()
    ret = subelement.run([[
        {'name': '1', 'authorized': ['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub'],
            'mysql': {
                'hosts': ['db1', 'db2']}},
        {'name': '2', 'authorized': ['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub'],
            'mysql': {
                'hosts': ['db1', 'db2']}}],
        'mysql.hosts'])

# Generated at 2022-06-13 14:17:25.063138
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:17:30.764466
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    results = lookup_module.run(terms=['{{ users }}', 'subkey', {'skip_missing': True}], variables=dict(users=[dict(subkey=['subvalue'], name=['subname'])]))
    assert results == [(dict(subkey=['subvalue'], name=['subname']), 'subvalue')]

# Generated at 2022-06-13 14:17:39.720382
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Load a dict and extract the 'hosts' key value as a list
    """
    terms = [[{'hosts': ['a', 'b'], 'x': 'y'}], 'hosts']
    result = LookupModule().run(terms=terms, variables=None)
    assert result == [[{'hosts': [], 'x': 'y'}, 'a'], [{'hosts': [], 'x': 'y'}, 'b']]


# Generated at 2022-06-13 14:17:51.137468
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    This is the test of method run of class LookupModule.
    """
    from ansible.module_utils.six import text_type
    from ansible.module_utils.six.moves import StringIO

    try:
        # Assume that file test_lookup_data is in the `tests` directory,
        # and then load all the data.
        file_data = open('../../../../../../tests/lookup_plugins/test_lookup_data', 'r').read()
    except (IOError, OSError) as err:
        print('Unable to open lookup test data file %s: %s' % ('../../../../../../tests/lookup_plugins/test_lookup_data',
                                                               text_type(err)),
              file=sys.stderr)
    #

# Generated at 2022-06-13 14:17:59.639856
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Unit test for method run of class LookupModule."""
    from nose.tools import ok_, eq_
    from ansible.errors import AnsibleError
    from ansible.module_utils.six import string_types

    # test for invalid number of arguments
    lookup_module = LookupModule(loader=None, templar=None, shared_loader_obj=None)
    try:
        lookup_module.run([], "")
    except AnsibleError as e:
        ok_(str(e) == "subelements lookup expects a list of two or three items, ")
    try:
        lookup_module.run(["1", "2", "3", "4"], "")
    except AnsibleError as e:
        ok_(str(e) == "subelements lookup expects a list of two or three items, ")


# Generated at 2022-06-13 14:18:11.238750
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:18:17.823899
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l.parent = {}
    l.parent['vars'] = {}
    l.parent['hostvars'] = {}
    l.parent['_hosts'] = True
    l.templar = None

    result = l.run([['a', 'b'], 'a'], {}, private=None)
    assert result == [('a', 'b')]

    result = l.run([{'_ansible_no_log': True}], {}, private=None)
    assert result == []

    result = l.run([{'_ansible_no_log': True, 'skipped': True}], {}, private=None)
    assert result == []


# Generated at 2022-06-13 14:18:22.937891
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    from ansible.module_utils.facts.system.linux import DictFactCollector
    from ansible.inventory.host import Host
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    lm = LookupModule()
    lm._templar = Templar(loader=DataLoader())
    lm._loader = DataLoader()

    # get a (random) fact and create a list of dictionaries
    facts = list(DictFactCollector().get_facts(Host()).values())
    fact_dict = facts[0]
    for fact in facts[1:]:
        fact_dict.update(fact)

# Generated at 2022-06-13 14:18:35.700816
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()
    terms = [
        [
            {"skipped": False, "dns_namespace": "ns1", "dns_zone": "z1"},
            {"skipped": False, "dns_namespace": "ns1", "dns_zone": "z2"},
            {"skipped": True, "dns_namespace": "irrelevant", "dns_zone": "z3"},
            {"skipped": False, "dns_namespace": "ns2", "dns_zone": "z4"},
        ],
        "dns_namespace",
    ]

# Generated at 2022-06-13 14:18:47.268501
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.plugins.lookup.subelements
    import pytest
    import json
    import yaml
    # test valid case
    terms = [["item1", "item2"], "subkey", {'skip_missing': True}]
    res = ansible.plugins.lookup.subelements.LookupModule().run(terms, None)
    assert res == []
    # test invalid cases
    with pytest.raises(AnsibleError) as excinfo:
        ansible.plugins.lookup.subelements.LookupModule().run(["item1", "item2"], None)
    assert "subelements lookup expects a list of two or three items" in excinfo.value.message

# Generated at 2022-06-13 14:19:28.709549
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    assert (l.run(["a"], {}) == ["a"])
    assert (l.run([], {}) == [])
    assert (l.run(["a", "b"], {}) == ["a", "b"])
    assert (l.run(["a", "b", {"skip_missing": "True"}], {}) == ["a", "b"])

    # Terms
    assert (l.run(["a"], {}) != [])
    assert (l.run(["a", "b"], {}) != [])
    assert (l.run(["a", ["c"]], {}) != [])

    # User error
    try:
        l.run(["a", "b", "c"], {})
        assert False
    except AnsibleError:
        assert True

    #

# Generated at 2022-06-13 14:19:42.151830
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:19:44.242678
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    raise SkipTest()
# vim:set ft=python sw=4 et sts=4 ts=8 :

# Generated at 2022-06-13 14:19:49.159576
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.constants as C
    from ansible.utils import plugin_docs

    # setup defaults
    C.DEFAULT_LOOKUP_PLUGIN_PATH = '../../lookup_plugins'
    C.DEFAULT_STDOUT_CALLBACK = 'default'
    C.DEFAULT_LOAD_CALLBACK_PLUGINS = True

    # setup lookup
    lookup = plugin_docs._get_lookup_plugin('subelements')

    # test 1
    users = [
        { 'name': 'alice', 'authorized': [ '/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub' ] },
        { 'name': 'bob', 'authorized': [ '/tmp/bob/id_rsa.pub' ] },
    ]

# Generated at 2022-06-13 14:20:00.939386
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # create an instance of class LookupModule
    lookup_module = LookupModule()

    # create a dictionnary
    users = [
        {
            'name': 'alice',
            'authorized': ['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub']
        },
        {
            'name': 'bob',
            'authorized': ['/tmp/bob/id_rsa.pub']
        },
        {
            'name': 'carol',
            'skipped': True,
            'authorized': ['/tmp/carol/id_rsa.pub']
        },
        {
            'skipped': True,
            'authorized': ['/tmp/carol/id_rsa.pub']
        }
    ]

    # run method run of class Lookup

# Generated at 2022-06-13 14:20:09.687325
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars import VariableManager
    class TestTemplar(Templar):
        def __init__(self, variables):
            self.variables = variables
            self._available_variables = variables

    context = PlayContext()
    templar = TestTemplar(variables=VariableManager())
    lookup = LookupModule()
    lookup._templar = templar
    result = lookup.run([], None, skip_missing=False)
    assert result == []

    result = lookup.run([], {}, skip_missing=False)
    assert result == []


# Generated at 2022-06-13 14:20:18.012036
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Mocks for LookupModule
    class LookupBaseMock:
        def __init__(self):
            self._templar = object()
            self._loader = object()

    class AnsibleErrorMock(Exception):
        def __init__(self, args, kwargs):
            self.args = args
            self.kwargs = kwargs

    # Mocks for terms
    terms = []

    def first_term(item):
        return listify_lookup_plugin_terms(item)

    listify_lookup_plugin_terms.side_effect = first_term

    # Mocks for variables
    variables = []

    # Mocks for kwargs
    kwargs = []

    # Create instance of LookupModule
    lookup_module = LookupModule()

# Generated at 2022-06-13 14:20:30.262810
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    # test_first_term_type
    try:
        lookup.run("hello", {})
        assert False, "subelements lookup requires two or three arguments separated by comma"
    except AnsibleError:
        assert True
    try:
        lookup.run("hello", {}, terms=1)
        assert False, "subelements lookup requires two or three arguments separated by comma"
    except AnsibleError:
        assert True
    # test_first_term_not_list_or_dict
    try:
        lookup.run("hello, hi", {})
        assert False, "subelements lookup expects first term to be a list or dict"
    except AnsibleError:
        assert True

# Generated at 2022-06-13 14:20:39.183133
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest


# Generated at 2022-06-13 14:20:51.833567
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    ################################################################################
    #
    # normal usecase: extract subelements from three list items
    #
    terms = [
        [{'item1': {'subelements': [1]}, 'item2': {'subelements': [2]}},
         {'item1': {'subelements': [3]}, 'item2': {'subelements': [4]}}], 'subelements']
    ret = lm.run(terms, None)

# Generated at 2022-06-13 14:22:05.511109
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()

    # direct call - test error handling
    terms = [{'a': 'b'}, 'a', {'skip_missing': True}]
    result = module.run(terms, {})
    assert len(result) == 1
    assert result[0] == ('b',)

    # direct call - test error handling
    terms = [{'a': 'b'}, 'a', {'skip_missing': False}]
    try:
        module.run(terms, {})
        assert False, "should have raised an AnsibleError"
    except AnsibleError:
        pass

    # direct call - test error handling
    terms = [{'a': ['b']}, 'a']
    result = module.run(terms, {})
    assert len(result) == 1
    assert result[0]

# Generated at 2022-06-13 14:22:20.267325
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # AnsibleError should be thrown when terms is not a list
    with pytest.raises(AnsibleError):
        LookupModule(None).run(None, None)

    # AnsibleError should be thrown when terms is not a list of at least two elements
    with pytest.raises(AnsibleError):
        LookupModule(None).run([], None)
    with pytest.raises(AnsibleError):
        LookupModule(None).run(["one"], None)

    with pytest.raises(AnsibleError):
        # AnsibleError should be thrown when terms[0] is not a list or dict
        LookupModule(None).run(["", "subkey"], {})

    # AnsibleError should be thrown when terms[1] is not a string

# Generated at 2022-06-13 14:22:31.298556
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    #
    # normal case
    #
    # construct a dict of dicts with a list inside
    lu = LookupModule()
    testdata = {'first': {'xyz': [1, 2, 3]}, 'second': {'xyz': [4, 5, 6]}}
    (ret, dummy_d1, dummy_d2) = lu.run([testdata, 'xyz'], variables=None, **{})
    assert ret == [(testdata['first'], 1), (testdata['first'], 2), (testdata['first'], 3), (testdata['second'], 4), (testdata['second'], 5), (testdata['second'], 6)]
    #
    # exception handling
    #
    # if first parameter of run is not a list, an AnsibleError is raised

# Generated at 2022-06-13 14:22:40.994719
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.parsing.yaml.dumper import AnsibleDumper

    print("TEST: subelements: test_LookupModule_run()")

    # Generate test data => two roles, with two tasks each. The first role
    # has an empty hosts list, so the task is skipped, but the second role
    # has a host, so the task is executed
    data = list()

# Generated at 2022-06-13 14:22:52.902738
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Test method run() of class LookupModule"""

    # importing modules that the LookupModule depends on, that are not automatically imported by ansible.
    # (otherwise the LookupModule would automatically import them when it is first imported by ansible)
    import os
    import re
    import sys
    import yaml
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.plugins.lookup import LookupBase
    from ansible.utils.listify import listify_lookup_plugin_terms

    # Create an instance of LookupModule for testing
    lookup_instance = LookupModule()

    # Test run() method of LookupModule with 'users' variable from documentation examples for the LookupModule

# Generated at 2022-06-13 14:22:59.089199
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # import here because this module is not available in the ansible build environment
    from ansible.module_utils.parsing.convert_bool import boolean

    def _test_run(terms, elementlist, expected_ret, expected_subelements, expected_flags, error_message=""):
        try:
            ret = LookupModule().run(terms, [], templar=None, loader=None)
            print("--> " + str(terms) + " should return: " + str(expected_ret))
            assert(ret == expected_ret)
        except AssertionError as e:
            print(str(e) + ": " + (str(ret) if ret else "no error"))
            has_error = True

# Generated at 2022-06-13 14:23:09.477491
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible.errors import AnsibleError


# Generated at 2022-06-13 14:23:21.771020
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    terms = [[{"authorized": ["/Users/alice/.ssh/id_rsa.pub", "/Users/alice/.ssh/id_dsa.pub"]}, {"authorized": ["/Users/bob/.ssh/id_rsa.pub"]}], "authorized"]
    result = module.run(terms, None)

# Generated at 2022-06-13 14:23:33.674728
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # create lookup instance
    lookup = LookupModule()

    # create a mock class instead of a dict
    class MockTemplar():
        def __init__(self):
            pass

        def template(self, term):
            if isinstance(term, list):
                newterm = []
                for item in term:
                    if isinstance(item, list):
                        newterm.append(self.template(item))
                    else:
                        newterm.append(item)
                term = newterm
            return term

    class MockLoader():
        def __init__(self):
            pass

        def get_basedir(self, hostname):
            return "."

    class EmptyClass(object):
        pass

    variables = EmptyClass()
    variables.hostname = "foohost"

    templar = MockTemplar()