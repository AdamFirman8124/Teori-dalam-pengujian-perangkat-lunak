

# Generated at 2022-06-13 14:13:46.109957
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    assert l.run([[{'a': 'b', 'c': [1, 2, 3]}], 'c'], dict()) == [(1, {'a': 'b', 'c': [1, 2, 3]}), (2, {'a': 'b', 'c': [1, 2, 3]}), (3, {'a': 'b', 'c': [1, 2, 3]})]

# Generated at 2022-06-13 14:13:56.077924
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import copy
    import pytest

    def _make_params(elementlist, subelements, flags={}):
        # elementlist must be a list of dictionaries
        # subelements is a string like 'key1.key2 ... keyn'
        # flags is a string like 'skip_missing=True'
        params = [elementlist, subelements]
        if len(flags):
            params.append(flags)
        return params

    # method run of class LookupModule
    lu = LookupModule()


# Generated at 2022-06-13 14:13:56.695241
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 14:14:03.176358
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup import LookupModule

    #create an object of class LookupModule
    lookup = LookupModule()

    # create a map of arguments to pass to test method run
    # The below test case is to walk a list of hashes (aka dictionaries) and then traverse a list with a given (nested sub-)key inside of those records.
    args = {}
    terms = []

    terms.append(['path/file1', 'path/file2', 'path/file3'])  # dummy list of files
    terms.append('authorized')  # dummy subkey name
    terms.append({'skip_missing': False})  # dummy flags

    expected_result = [('path/file1', 'authorized'),
                       ('path/file2', 'authorized'),
                       ('path/file3', 'authorized')]

    # pass

# Generated at 2022-06-13 14:14:12.120852
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Arrange
    module = LookupModule()

    # Act
    # Assert
    try:
        module.run([{'a': {'b': {'c': 'd'}}}])
    except AnsibleError:
        assert True
    else:
        assert False, "unexpected success"

    try:
        module.run([{'a': {'b': {'c': 'd'}}}], {'flags': {'skip_missing': True}})
    except AnsibleError:
        assert True
    else:
        assert False, "unexpected success"

    try:
        module.run([{'a': {'b': {'c': 'd'}}}], {'flags': {'skip_missing': False}})
    except AnsibleError:
        assert True

# Generated at 2022-06-13 14:14:22.450379
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create instance of LookupModule class
    lookup = LookupModule()

    # Create valid data
    lookup.set_options(direct=dict(vars=dict(users=[
        {'name': 'alice', 'authorized': ['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub']},
        {'name': 'bob', 'authorized': ['/tmp/bob/id_rsa.pub']}
    ])))
    terms = ['{{ users }}', 'authorized']

    # Test with valid data

# Generated at 2022-06-13 14:14:35.667021
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:14:46.217394
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import simplejson as json
    L = LookupModule()
    # Run of method run with expected result
    # One subset of subelements

# Generated at 2022-06-13 14:14:57.077517
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.errors import AnsibleError
    from ansible.module_utils.six import string_types
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.plugins.lookup import LookupBase
    from ansible.utils.listify import listify_lookup_plugin_terms

    # Unit test for tests/unit/plugins/lookup/test_subelements.py
    # self = LookupModule()

    # check lookup terms - check number of terms
    def _raise_terms_error(msg=""):
        raise AnsibleError(
            "subelements lookup expects a list of two or three items, " + msg)

    # tests for run method
    # def run(self, terms, variables, **kwargs):

    # terms[0] = listify_lookup_plugin

# Generated at 2022-06-13 14:15:08.606813
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = [
        [
            {'name': 'alice'},
            {'name': 'bob'},
        ],
        'name',
    ]
    assert LookupModule().run(terms, None) == [
        ({'name': 'alice'}, 'alice'),
        ({'name': 'bob'}, 'bob'),
    ]

    terms = [
        {
            'alice': {'name': 'alice'},
            'bob': {'name': 'bob'},
        },
        'name',
    ]
    assert LookupModule().run(terms, None) == [
        ({'name': 'alice'}, 'alice'),
        ({'name': 'bob'}, 'bob'),
    ]


# Generated at 2022-06-13 14:15:27.472808
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = [
        [{"name": "alice", "authorized": ["/tmp/alice/onekey.pub", "/tmp/alice/twokey.pub"]},
           {"name": "bob", "authorized": ["/tmp/bob/id_rsa.pub"]}],
        "authorized"
    ]
    lookup = LookupModule()
    result = lookup.run(terms=terms, variables={})

# Generated at 2022-06-13 14:15:39.699814
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # setup some tests:
    tests = {}
    tests[(['foo'], "bar")] = AnsibleError
    tests[([{'foo': 'bar'}], 'foo')] = (False, [[{'foo': 'bar'}, 'bar']])
    tests[([{'foo': 'bar'}], 'bar')] = AnsibleError
    tests[([{'foo': {'bar': 'baz'}}], 'foo.bar')] = (False, [[{'foo': {'bar': 'baz'}}, 'baz']])
    tests[([{'foo': {'bar': 'baz'}}], 'foo.bar.baz')] = AnsibleError

# Generated at 2022-06-13 14:15:52.763679
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Unit test for method run of class LookupModule"""
    import os

    # Constructor
    plugin = LookupModule()
    plugin._templar = 'not relevant here'
    plugin._loader = 'not relevant here'

    # Test scenarios

# Generated at 2022-06-13 14:16:03.805984
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.errors import AnsibleUndefinedVariable
    from ansible.module_utils import basic
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    from ansible.executor import task_executor

    def get_lookup(loader=None, variable_manager=None, parameters=None):
        lookup = LookupModule(loader=loader, variable_manager=variable_manager, templar=Templar(loader=loader, variables=variable_manager))
        if parameters is not None:
            if isinstance(parameters, dict):
                # parameters are the flags
                for key in parameters:
                    lookup.set_options(**{key: parameters[key]})


# Generated at 2022-06-13 14:16:13.548768
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l.set_connection('local')  # fake local connection

    # simplest form
    assert l.run(terms=[[{'name': 'joe'}, {'name': 'bob'}], 'name']) == [('joe', 'joe'), ('bob', 'bob')]

    # simple nested subkey
    # flattens as {'name': 'joe', 'address': {'city': 'Paris'}} and {'name': 'bob', 'address': {'city': 'London'}}

# Generated at 2022-06-13 14:16:23.191495
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    subelements = LookupModule()
    assert subelements.run([{"user1": {"name": "alice", "authorized": "/tmp/alice/id_rsa.pub"}}, "authorized"], {}) == \
           [({'name': 'alice', 'authorized': '/tmp/alice/id_rsa.pub'}, '/tmp/alice/id_rsa.pub')]

# Generated at 2022-06-13 14:16:35.695199
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lu = LookupModule()

    # check lookup terms
    terms = []
    ret = lu.run(terms)
    assert isinstance(ret, list)
    assert ret == [], "expected '%s', got '%s'" % ([], ret)

    terms = [None]
    ret = lu.run(terms)
    assert isinstance(ret, list)
    assert ret == [], "expected '%s', got '%s'" % ([], ret)

    terms = [[None], None]
    ret = lu.run(terms)
    assert isinstance(ret, list)
    assert ret == [], "expected '%s', got '%s'" % ([], ret)

    terms = [[None], None, None]
    ret = lu.run(terms)
    assert isinstance(ret, list)

# Generated at 2022-06-13 14:16:46.085576
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # test setup
    lookup = LookupModule()
    users = [
        {
            "name" : "alice",
            "authorized" : ["/tmp/alice/onekey.pub", "/tmp/alice/twokey.pub"],
            "mysql" : {
                "password" : "mysql-password",
                "hosts" : ["%", "127.0.0.1", "::1", "localhost"],
                },
            "groups" : ["wheel"],
            },
        {
            "name" : "bob",
            "authorized" : ["/tmp/bob/id_rsa.pub"],
            "mysql" : {
                "password" : "other-mysql-password",
                "hosts" : ["db1"],
                },
            },
        ]
    mysql

# Generated at 2022-06-13 14:16:58.224843
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit tests for method run of class LookupModule
    """
    users_examples = [
        {'name': 'alice', 'authorized': ['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub']},
        {'name': 'bob', 'authorized': ['/tmp/bob/id_rsa.pub']}
    ]
    users_examples_dict = {'users_examples': users_examples}
    users_subelements = LookupModule()
    users_subelements.set_options(terms=['users_examples', 'authorized'], variables=users_examples_dict)

# Generated at 2022-06-13 14:17:02.761595
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

# Generated at 2022-06-13 14:17:29.997116
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup = LookupModule()
    # common vars
    users = [
        {"name": "alice", "authorized": ["/tmp/alice/onekey.pub", "/tmp/alice/twokey.pub"], "groups": ["wheel"], "mysql": {"password": "mysql-password", "hosts": ["%", "127.0.0.1", "::1", "localhost"], "privs": ["*.*:SELECT", "DB1.*:ALL"]}},
        {"name": "bob", "authorized": ["/tmp/bob/id_rsa.pub"], "mysql": {"password": "other-mysql-password", "hosts": ["db1"], "privs": ["*.*:SELECT", "DB2.*:ALL"]}}
    ]
    # name tests

# Generated at 2022-06-13 14:17:41.581784
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    user_lookup_plugin = LookupModule()

    # test with plain text password
    lookup_data = {'mysql': {'password': 'mysql-password'}}
    user_lookup_plugin.run([lookup_data, 'mysql'], {}, {})

    # test with vault encrypted password
    lookup_data = {'mysql': {'password': AnsibleVaultEncryptedUnicode('mysql-password')}}
    user_lookup_plugin.run([lookup_data, 'mysql'], {}, {})

# Generated at 2022-06-13 14:17:42.645766
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()

# Generated at 2022-06-13 14:17:53.811696
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # unit test for subelements lookup

    # Setup
    my_dict = {
        'alice': dict(name='alice', authorized=['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub'],
                        groups=['wheel']),
        'bob': dict(name='bob', authorized=['/tmp/bob/id_rsa.pub'],
                    groups=[])
    }

    # Test
    lu = LookupModule()
    ret = lu.run([
        [my_dict['alice'], my_dict['bob']],
        'groups'
    ], None)

# Generated at 2022-06-13 14:18:04.152700
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import lxml.etree as ET

    # Test setup using ElementTree
    # See: http://lxml.de/tutorial.html

# Generated at 2022-06-13 14:18:16.415631
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit test for method run of class LookupModule
    :return:
    """
    module_name = __name__.rsplit(".", 1)[1]
    if module_name == "__main__":
        import doctest

        doctest.testmod()
    else:
        # execute like a module
        import ansible.modules.lookup_plugins.subelements
        terms = [
            [{
                "name": "alice",
                "authorized": ["/tmp/alice/onekey.pub", "/tmp/alice/twokey.pub"]
            }, {
                "name": "bob",
                "authorized": ["/tmp/bob/id_rsa.pub"]
            }],
            "authorized"
        ]
        result = ansible.modules.lookup_plugins.s

# Generated at 2022-06-13 14:18:24.406975
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader

    dataloader = DataLoader()
    templar = Templar(loader=dataloader)

    users = [{'name': 'Alice', 'authorized': ['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub']}, {'name': 'Bob', 'authorized': ['/tmp/bob/id_rsa.pub']}]
    lookup = LookupModule()

    # Check number of terms
    try:
      lookup.run(terms=[], variables={}, templar=templar)
      assert False, "subelements lookup expects a list of two or three items"
    except AnsibleError:
      pass

    # Check first term

# Generated at 2022-06-13 14:18:37.174525
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test case 1 - single dictionary without flags
    # input elements
    terms = [
        {
            'a': {
                'b': ['b1', 'b2', 'b3'],
            },
            'c': {
                'c1': 'd1',
                'c2': {'d2': 'e2'},
            },
            'd': [{'d1': 'e1'}, {'d2': 'e2'}, {'d3': ['e3', 'e4', 'e5']}],
        },
        'a.b',
    ]
    # expected result

# Generated at 2022-06-13 14:18:47.850820
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # create a list of users
    user1 = {
        'name': 'Alice',
        'authorized': [
            '/tmp/alice/onekey.pub',
            '/tmp/alice/twokey.pub'
        ]
    }
    user2 = {
        'name': 'Bob',
        'authorized': [
            '/tmp/bob/id_rsa.pub'
        ]
    }
    users = [user1, user2]

    # create instance of LookupModule and run for users
    lookup = LookupModule()
    result = lookup.run([users, 'authorized'])

    # check result
    assert(len(result) == 3)
    assert(result[0] == (user1, '/tmp/alice/onekey.pub'))

# Generated at 2022-06-13 14:19:00.354393
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup import LookupBase
    from ansible.plugins.lookup.subelements import LookupModule

    # test raise terms error
    LookupModule._raise_terms_error = LookupBase._unimplemented_method
    try:
        LookupModule.run(None, [])
    except AnsibleError as error:
        assert error.args[0] == "subelements lookup expects a list of two or three items, "
    try:
        LookupModule.run(None, [1, 2, 3])
    except AnsibleError as error:
        assert error.args[0] == "subelements lookup expects a list of two or three items, first a dict or a list, second a string pointing to the subkey"

# Generated at 2022-06-13 14:19:42.261470
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    if sys.version_info < (2, 7):
        import unittest2 as unittest
    else:
        import unittest
    from ansible.module_utils.six import StringIO
    from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleSequence, AnsibleMapping

    class TestLookupModule(unittest.TestCase):

        def setUp(self):
            self._saved_stdout = sys.stdout
            sys.stdout = StringIO()

        def tearDown(self):
            sys.stdout = self._saved_stdout

        def test_run_normal(self):
            from ansible.plugins.lookup.subelements import LookupModule

# Generated at 2022-06-13 14:19:52.292192
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import unittest
    import ansible.errors
    import ansible.utils.listify
    import ansible.plugins.lookup
    import ansible.module_utils.parsing.convert_bool

    # create test case
    class testCase(unittest.TestCase):
        def setUp(self):
            self.lookupBase = ansible.plugins.lookup.LookupBase()

        def test_with_good_arguments(self):
            terms = [ [ { 'one': { 'two': [ 'first', 'second', 'third' ] } } ], 'one.two' ]
            variables = { 'param': 'value' }

            ret = ansible.plugins.lookup.LookupModule.run(self.lookupBase, terms, variables)

# Generated at 2022-06-13 14:20:03.780267
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    with pytest.raises(AnsibleError) as excinfo:
        LookupModule.run(LookupModule(), [])
    assert "subelements lookup expects a list of two or three items" in str(excinfo.value)

    with pytest.raises(AnsibleError) as excinfo:
        LookupModule.run(LookupModule(), [[], "teststring", "teststring"])
    assert "first a dict or a list, second a string pointing to the subkey" in str(excinfo.value)

    with pytest.raises(AnsibleError) as excinfo:
        LookupModule.run(LookupModule(), [[], 1, "teststring"])
    assert "first a dict or a list, second a string pointing to the subkey" in str(excinfo.value)

   

# Generated at 2022-06-13 14:20:11.349420
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Stub for templar
    class Templar:
        def __init__(self):
            pass
        def template(self, template):
            """Stub function for template"""
            return template

    # Stub for loader
    class Loader:
        def __init__(self):
            pass
        def get_basedir(self):
            """Stub function for get_basedir"""
            return ""

    # Fake AnsibleModule to make the lookup plugin run standalone
    import ansible.utils
    class module_data:
        def __init__(self):
            self.params = {}
            self.exit_json = object


# Generated at 2022-06-13 14:20:17.498302
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    LookupModule.run(None, ["users", "mysql.hosts"])
    LookupModule.run(None, ["users", "mysql.hosts", {"skip_missing": True}])
    LookupModule.run(None, ["users", "mysql.hosts", {"skip_missing_2": True}])  # type: ignore



# Generated at 2022-06-13 14:20:29.744083
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.parsing.convert_bool import boolean

    # create structure for tests

# Generated at 2022-06-13 14:20:38.521319
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    " Unit test for method run of class LookupModule "

    # Object instantiation
    l = LookupModule()

    # Create data structures

# Generated at 2022-06-13 14:20:51.007933
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # mocked flags
    terms = {
        'skip_missing': False,
        'var': 'lookup_options'
    }

    # mocked user
    users = {
        'name': 'joe',
        'authorized': '/tmp/joe/id_rsa.pub',
        'mysql': {
            'password': 'joe-pass',
            'hosts': [
                "%",
                "localhost"
            ],
            'privs': [
                "*.*:ALL"
            ]
        },
        'groups': ['wheel']
    }

    # mocked dictionary of users
    users = {
        'users': [users]
    }

    # mocked AnsibleModule object

# Generated at 2022-06-13 14:21:00.921386
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:21:13.652332
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # mock class objects and function:
    mock_class_objects = {
        'AnsibleError': AnsibleError,
        'StringTypes': string_types,
        'LookupBase': LookupBase}

    def mock_listify_lookup_plugin_terms(list_terms, templar, loader):
        return list_terms

    mock_function_objects = {
        'listify_lookup_plugin_terms': mock_listify_lookup_plugin_terms}

    module = importlib.import_module('ansible.plugins.lookup.subelements')
    reload(module)

    class_ = getattr(module, 'LookupModule')
    class_.run = MagicMock(return_value=[(1, 2)])
    class_.run.__name__ = 'run'

    # patching
   

# Generated at 2022-06-13 14:22:27.009252
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # access to protected members of class to be tested
    LookupModule_run = LookupModule.run

    # set-up object to be tested
    terms = [
        {
            'skipped': False,
            'skipped 2': False,
            'skipped 3': 'no',
            'skipped 4': 0,
            'skipped 5': [],
            'skipped 6': '',
            'skipped 7': [{'skipped': True}],
            'skipped 8': [{'skipped': False}],
        },
        'authorized',
    ]

# Generated at 2022-06-13 14:22:38.178394
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = [
        {'users':
            [
                {'name': 'alice',
                 'authorized': ['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub']},
                {'name': 'bob',
                 'authorized': ['/tmp/bob/id_rsa.pub']}
            ]
        },
        'authorized',
        {'skip_missing': True}
    ]
    ret = lookup.run(terms, None)
    assert len(ret) == 3
    assert ret[0][0]['name'] == 'alice'
    assert ret[0][1] == '/tmp/alice/onekey.pub'
    assert ret[1][0]['name'] == 'alice'

# Generated at 2022-06-13 14:22:51.265910
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import copy

    # minimal mock variables dictionary
    variables = {}

    # copy original flags list
    flags = copy.deepcopy(FLAGS)

    # test correct list with two items
    terms = [
        # first term: a list of dictionaries
        [
            {'key': ['value1', 'value2']},
            {'key': ['value1', 'value2']},
        ],
        # second term: the name of the subkey to lookup
        'key',
    ]
    lookup = LookupModule()
    result = lookup.run(terms, variables, **{'_input': '_input'})

# Generated at 2022-06-13 14:23:04.049875
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils.six import PY2
    from ansible.module_utils._text import to_text
    from ansible.parsing.ajson import AnsibleJSONEncoder

    # method run returns a list with tuples
    # each tuple holds a dictionary and an item of a subkey list

    if PY2:
        def _unicode(s):
            return to_text(s, errors='strict')

    # setup variables

# Generated at 2022-06-13 14:23:12.456114
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def _assert_result_ok(lookup, terms, expected_result):
        result = lookup.run(terms, None)
        assert result == expected_result, "expected result %s does not match actual result '%s'" % (expected_result, result)
    lookup = LookupModule()

# Generated at 2022-06-13 14:23:24.295380
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils._text import to_text

    # define parameters