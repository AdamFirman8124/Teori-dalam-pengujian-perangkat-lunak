

# Generated at 2022-06-13 14:13:47.003865
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret

    # secret string to be decrypted

# Generated at 2022-06-13 14:13:56.732308
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # create a test-instance
    testInstance = LookupModule()

    # list of dictionaries given, key exists in every item, should return list with all subelements
    testData = [
        {'test': 'foo'},
        {'test': 'bar'}
    ]
    subelements = testInstance.run([
        [testData, 'test'],
    ], dict())
    assert len(subelements) == 2
    assert subelements[0] == (testData[0], 'foo')
    assert subelements[1] == (testData[1], 'bar')

    # skip_missing: true, list of dictionaries given, key exists in some items, should return list with all subelements

# Generated at 2022-06-13 14:14:00.145257
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Unit test for method run of class LookupModule."""

    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.six import PY3

    # Get module
    lookup_mod = LookupModule()

    # Define module arguments and 

# Generated at 2022-06-13 14:14:10.407773
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    terms = [[{'key1': 'value1'}, {'key1': 'value1'}, {'key1': 'value1'}, {'key1': 'value1'}],
             'key1']
    result = module.run(terms=terms, variables=None)
    assert result == [('value1',), ('value1',), ('value1',), ('value1',)]

    terms = [[{'key1': 'value1'}, {'key1': 'value1'}, {'key1': 'value1'}, {'key1': 'value1'}],
             'key1', {'skip_missing': True}]
    result = module.run(terms=terms, variables=None)

# Generated at 2022-06-13 14:14:21.306412
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit tests for method run of class LookupModule
    """
    from ansible.module_utils.parsing.convert_bool import boolean

    def test_data(users):
        """
        Test data for testing the lookup module subelements
        :param users: User data
        :return: None
        """
        elements = users
        for subelement in subelements:
            elements = elements[subelement]
        return elements


# Generated at 2022-06-13 14:14:28.555093
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Test method run of class LookupModule.
    """
    class TestLookupBase(object):
        """
        Implement methods lookupbase needs to have:
        * _templar
        * _loader
        """
        def __init__(self):
            """
            Initialize templar and loader.
            """
            import sys
            from ansible.parsing.dataloader import DataLoader
            from ansible.template import Templar
            self.templar = Templar(loader=DataLoader(), variables={})
            self.loader = DataLoader()

        def _templar(self):
            """
            Return templar.
            """
            return self.templar

        def _loader(self):
            """
            Return loader.
            """
            return self.loader

    looker = Lookup

# Generated at 2022-06-13 14:14:39.258636
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:14:48.877691
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class MockTemplar(object):
        def __init__(self, *args, **kwargs):
            pass
        def template(self, *args, **kwargs):
            return args[0]

    class MockLoader(object):
        def __init__(self, *args, **kwargs):
            pass
        def load_from_file(self, *args, **kwargs):
            return args[0]

    lookup_module = LookupModule()
    lookup_module._templar = MockTemplar()
    lookup_module._loader = MockLoader()

    # test case 1 - dict with 2 subelements
    terms = [
        [
            {
                "key1": "value1",
                "key2": "value2",
            }
        ],
        "key2"
    ]
    result

# Generated at 2022-06-13 14:15:01.513077
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import json
    # json.load() doesn't return a dictionary object: it returns an object_pairs_hook list

# Generated at 2022-06-13 14:15:11.871457
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    #ansible 2.3.3.0
    #self, terms, inject=None, **kwargs

    #ansible 2.8
    #self, terms, variables=None, **kwargs

    # pylint: disable=unused-argument

    # Setup
    lookup_module = LookupModule()
    if hasattr(lookup_module,"_templar"):
        templar = lookup_module._templar
    def my_get_basedir(self, vars):
        return '/etc/ansible/my_get_basedir'
    lookup_module.get_basedir = my_get_basedir.__get__(lookup_module, LookupModule)
    lookup_module._loader = None
    lookup_module._templar = None
    lookup_module.set_options({})
   

# Generated at 2022-06-13 14:15:30.437388
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    # first test
    test_list = [
        {'authorized': ['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub']},
        {'authorized': ['/tmp/bob/id_rsa.pub']}
    ]
    test_key = "authorized"
    output = lookup_module.run([test_list, test_key], variables=None)
    assert output == ([('/tmp/alice/onekey.pub',), ('/tmp/alice/twokey.pub',), ('/tmp/bob/id_rsa.pub',)])
    # second test
    test_list = [
        {'groups': ['wheel']},
        {'groups': ['root']}
    ]

# Generated at 2022-06-13 14:15:41.926784
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import PY2
    from ansible import errors
    from ansible.templar import Templar

    templar = Templar(loader=None)

    def _assert_lookup_result(test_nbr, result, expected_result, lookup_flags=None):
        if 'skip_missing' not in lookup_flags or lookup_flags['skip_missing'] == False:
            assert result == expected_result, 'test nr %d failed' % test_nbr
        else:
            assert len(result) == len(expected_result), 'test nr %d failed' % test_nbr
            for i in range(len(expected_result)):
                assert result[i][0] == expected_result[i][0], 'test nr %d failed' % test_nbr
                assert result

# Generated at 2022-06-13 14:15:53.870995
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    # check no. of args = 2
    test_terms1 = [
        [{'skipped': False, 'name': 'alice', 'authorized': ['1234']}],  # empty list
        "authorized"
    ]
    assert lookup.run(test_terms1, {}) == [({'name': 'alice', 'authorized': ['1234']}, '1234')], "subelements lookup did not work"
    # check no. of args > 3
    test_terms2 = [
        [{'skipped': False, 'name': 'alice', 'authorized': ['1234']}],  # empty list
        "authorized",
        "flags"
    ]
    test_terms2.append({'skip_missing': False})
    lookup.run(test_terms2, {})

# Generated at 2022-06-13 14:16:04.634310
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from collections import namedtuple
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play_context import PlayContext
    from ansible.utils.vars import combine_vars

    loader = DataLoader()
    inventory = Inventory(loader=loader, variable_manager=VariableManager(), host_list=[])
    play_context = PlayContext()

    Options()
    Options.connection = 'local'
    Options.module_paths = ['/usr/share/ansible/plugins/modules']
    Options.forks = 1
    Options.become = None
    Options.become_method = None
    Options.become_user = None
    Options.verbosity = 0
    Options.check = False


# Generated at 2022-06-13 14:16:14.676915
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:16:22.338671
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import unittest

    class LookupModuleTest(unittest.TestCase):

        def test_run_empty_list(self):
            """
            Test that a lookup_plugin term without subkey doesn't fail.
            """
            lm = LookupModule()
            terms = [
                [
                    dict(foo="bar"),
                    dict(baz="qux")
                ],
                "password"
            ]
            result = lm.run(terms, dict())
            self.assertEqual(result, [])

        def test_run_with_empty_dict(self):
            """
            Test that a lookup_plugin term without subkey doesn't fail.
            """
            lm = LookupModule()
            terms = [
                dict(foo="bar"),
                "password"
            ]
            result = lm

# Generated at 2022-06-13 14:16:35.256647
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class MockLoader:
        def get_basedir(self, term):
            return '/path/to/file'

    class MockTemplar:
        def template(self, string):
            return string

    users = [{'name': 'root', 'authorized': ['/path/to/rootkey.pub']},
             {'name': 'alice', 'authorized': ['/path/to/alicekey.pub']},
             {'name': 'bob', 'authorized': ['/path/to/bobkey.pub']},
             {'name': 'carol', 'authorized': ['/path/to/carolkey.pub']},
            ]

# Generated at 2022-06-13 14:16:45.901559
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

# Generated at 2022-06-13 14:16:57.943907
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import sys
    import tempfile
    import contextlib

    (f, path) = tempfile.mkstemp()
    os.close(f)

    @contextlib.contextmanager
    def mkfile(body):
        with open(path, 'w') as f:
            f.write(body)
        try:
            yield
        finally:
            os.unlink(path)

    def run_lookup_module(**kwargs):
        lookup = LookupModule()
        return lookup.run([], {}, **kwargs)


# Generated at 2022-06-13 14:17:08.636344
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    users = [
        {"name": "alice", "authorized": ["/tmp/alice/onekey.pub", "/tmp/alice/twokey.pub"], "mysql": {"password": "mysql-password", "hosts": ["%", "127.0.0.1", "::1", "localhost"], "privs": ["*.*:SELECT", "DB1.*:ALL"]}, "groups": ["wheel"]},
        {"name": "bob", "authorized": ["/tmp/bob/id_rsa.pub"], "mysql": {"password": "other-mysql-password", "hosts": ["db1"], "privs": ["*.*:SELECT", "DB2.*:ALL"]}}
    ]
    empty = []

# Generated at 2022-06-13 14:17:33.921486
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class TestLookupModule(LookupModule):

        def __init__(self, loader=None, templar=None, **kwargs):
            self._loader = loader
            self._templar = templar

    lookup = TestLookupModule()

    # test case 1

# Generated at 2022-06-13 14:17:46.609972
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    sut = LookupModule()

    # empty elementlist
    result = sut.run([[], 'skipped'], None)
    assert result == []

    # simple structure
    result = sut.run([[{'skipped': True}], 'skipped'], None)
    assert result == []

    # simple structure with skipped item
    result = sut.run([[{'skipped': True}], 'skipped'], None)
    assert result == []

    # simple structure with multiple skipped items
    result = sut.run([[{'skipped': True}, {'skipped': True}], 'skipped'], None)
    assert result == []

    # result is skipped
    result = sut.run([{'skipped': True}, 'skipped'], None)
    assert result == []

    # result

# Generated at 2022-06-13 14:17:57.143326
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import unittest

    # 1. simple test:
    users = [{'name': 'alice', 'authorized': ['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub']}]
    terms = [users, 'authorized']

    expected_result = [({'name': 'alice', 'authorized': ['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub']}, '/tmp/alice/onekey.pub'), ({'name': 'alice', 'authorized': ['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub']}, '/tmp/alice/twokey.pub')]

    result = LookupModule().run(terms, variables={}, **{})
    assert (result == expected_result)

    #

# Generated at 2022-06-13 14:18:03.133901
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # prepare test
    x = LookupModule()
    terms = ["terms", "%Y-%m-%d %H:%M", {'skip_missing': True}]
    x._templar = None
    x._loader = None
    x.run(terms=terms, variables=dict())
    # test it
    # assert result_list == expected_list

# Generated at 2022-06-13 14:18:15.365980
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:18:23.809266
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import json
    import sys
    import os

    # prepare a dummy elementlist
    elementlist = []
    with open('/tmp/_elementlist.json', 'r') as f:
        elementlist = json.load(f)

    # resultlist should have the same content as elementlist, but one level up
    assert len(elementlist) == 5
    resultlist = []
    with open('/tmp/_resultlist.json', 'r') as f:
        resultlist = json.load(f)
    assert len(resultlist) == len(elementlist) * 2

    # Check the run method
    result = []
    subkey = "cdroms"
    flags = {}
    terms = [elementlist, subkey, flags]
    module = LookupModule()
    result = module.run(terms, None)

    assert len

# Generated at 2022-06-13 14:18:36.867907
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:18:47.642426
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test_LookupModule_run
    from ansible.module_utils.parsing.convert_bool import boolean
    def _equal(a, b):
        if isinstance(a, bool) and isinstance(b, bool):
            return boolean(a) == boolean(b)
        return a == b

    # test no terms
    from ansible.errors import AnsibleError
    try:
        LookupModule().run([], [])
    except AnsibleError:
        pass
    else:
        raise AssertionError("terms=[] should cause an AnsibleError")

    # test no flags
    lookup = LookupModule()
    result = lookup.run([['a'], 'b'], {})
    assert result == []
    result = lookup.run([{'a': 'a'}, 'b'], {})

# Generated at 2022-06-13 14:19:00.150107
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Setup test object and terms to test with
    test_obj = LookupModule()

# Generated at 2022-06-13 14:19:04.628896
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    t = [{'key': {'subkey': ['a', 'b', 'c']}}]
    r = lm.run([t, 'key.subkey'], None)
    assert r[0][1] == 'a'
    assert r[1][1] == 'b'
    assert r[2][1] == 'c'

# Generated at 2022-06-13 14:19:47.934350
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # get module
    module = LookupModule()
    my_loader = module._loader
    my_loader.set_basedir('/tmp')

    # get templar
    my_templar = module._templar

    # create test users

# Generated at 2022-06-13 14:19:59.544175
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test required arguments
    # test w/o optional arguments
    # test w/ optional arguments

    # Setup
    lookup_module = LookupModule()

# Generated at 2022-06-13 14:20:08.891403
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    import os
    import yaml

    # Adjust paths as pytest uses a different working directory
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    import plugins

    lookup = plugins.lookup.LookupModule()


# Generated at 2022-06-13 14:20:17.636999
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.parsing.yaml.objects import AnsibleUnicode

    # AnsibleUnicode is a wrapper around unicode and is only used for PyYAML compatibility.
    # It is essentially equivalent to the str constructor in Python 2, and is the same as str in Python 3
    def unicode(arg):
        return AnsibleUnicode(arg)

    LookupModule.run(None, [unicode('postgres'), unicode('mysql_users'), unicode('privs')])

    # TODO: make this test work on python 3
    # running this test on python 3 results in the following exception:
    #
    #     Traceback (most recent call last):
    #       File "/Users/jensvincke/.virtualenvs/ansible_test/lib/python2.7/site-packages/ansible/

# Generated at 2022-06-13 14:20:29.845884
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.parsing.convert_bool import boolean
    import ansible.plugins.lookup.subelements
    import ansible.module_utils._text
    class UserModule(object):
        def __init__(self):
            self.params = {}
            self.params['user'] = 'alice'
            self.params['key'] = '/tmp/alice/onekey.pub'
        def fail_json(self, msg): pass
    module = UserModule()
    templar = ansible.module_utils.basic.AnsibleModule(
        argument_spec=module.params,
        supports_check_mode=module._supports_check_mode,
        bypass_checks=module._bypass_checks
    )
    msg = "The error message should be shown."

# Generated at 2022-06-13 14:20:38.963066
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup = LookupModule()

    # test exception for invalid number of items
    assert_raises(AnsibleError, lambda: lookup.run([], {}, validate_terms=True))
    assert_raises(AnsibleError, lambda: lookup.run(["item1", "item2", "item3"], {}, validate_terms=True))
    assert_raises(AnsibleError, lambda: lookup.run(["item1", "item2", "item3", "item4"], {}, validate_terms=True))

    # test exception for invalid types of items
    assert_raises(AnsibleError, lambda: lookup.run(["item1", 5], {}, validate_terms=True))
    assert_raises(AnsibleError, lambda: lookup.run([5, "item2"], {}, validate_terms=True))


# Generated at 2022-06-13 14:20:51.617008
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    test_LookupModule_run: test the subelements lookup plugin run method
    """
    # These tests would normally be in a pytest based unit test class, but I
    # am writing these tests in such a way as to be able to run them from
    # ansible-test, which does not currently support pytest unit tests.

# Generated at 2022-06-13 14:21:01.164729
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from .__mock__ import LookupModuleTest

# Generated at 2022-06-13 14:21:13.939360
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:21:21.446936
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    element = {'name': 'bob'}
    subkey = 'mysql'
    subdict = {'password': 'other-mysql-password', 'privs': ['*.*:SELECT', 'DB2.*:ALL']}
    sublist = ['db1']

    # set subdict
    element[subkey] = subdict
    assert element[subkey] == subdict

    # set sublist
    element[subkey]['hosts'] = sublist
    assert element[subkey]['hosts'] == sublist

    lookup_module = LookupModule()

    # used from with_subelements
    terms = (element, subkey + '.hosts')
    subelements = lookup_module.run(terms, None)
    assert len(subelements) == 1
    assert subelements[0][0]

# Generated at 2022-06-13 14:22:36.962156
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.template import Templar


# Generated at 2022-06-13 14:22:50.117909
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:23:02.601444
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test with a list of dicts.
    test_terms = [
        [
            {
                "name": "Alice",
                "authorized": [
                    "/tmp/alice/onekey.pub",
                    "/tmp/alice/twokey.pub"
                ]
            },
            {
                "name": "Bob",
                "authorized": [
                    "/tmp/bob/id_rsa.pub",
                ]
            },
        ],
        "authorized",
        {}
    ]
    lookup_obj = LookupModule()

# Generated at 2022-06-13 14:23:11.487463
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['localhost'])
    variable_manager.set_inventory(inventory)

    host1 = inventory.get_host('localhost')

# Generated at 2022-06-13 14:23:23.425667
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # we need to be able to run this in python2.6, need to work around lack of ordereddict
    class OrderedDict(object):
        def __init__(self, list_of_tuples):
            self.list_of_tuples = list_of_tuples

        def __iter__(self):
            return self.list_of_tuples.__iter__()

        def items(self):
            return self.list_of_tuples

        def keys(self):
            return [x[0] for x in self.list_of_tuples]

        def values(self):
            return [x[1] for x in self.list_of_tuples]
