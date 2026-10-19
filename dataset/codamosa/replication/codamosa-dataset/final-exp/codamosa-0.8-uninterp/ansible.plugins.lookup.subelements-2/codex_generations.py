

# Generated at 2022-06-13 14:13:46.846128
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import unittest
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.template import Templar

    test_object = LookupModule()
    test_object.set_loader(DataLoader())
    test_object._templar = Templar(None, variables=VariableManager())
    test_object._templar.available_variables = {}
    test_object._templar.set_available_variables(test_object._templar.available_variables)

    # test with a dictionary

# Generated at 2022-06-13 14:13:55.019683
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # setup
    class fake_loader:
        def get_basedir(self, *args):
            return "/path/to/basedir"
    module_loader = fake_loader()

# Generated at 2022-06-13 14:14:05.449950
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:14:11.207061
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import unittest
    import sys
    test_classes = [
        TestSubelementsLookupModule
    ]
    suite = unittest.TestSuite(map(unittest.TestLoader().loadTestsFromTestCase, test_classes))
    unittest.TextTestRunner(verbosity=2).run(suite)



# Generated at 2022-06-13 14:14:21.872003
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.module_utils.six import PY2
    from ansible.module_utils.six.moves import StringIO

    class DummyLookupBaseClass(object):
        def __init__(self):
            self._templar = DummyVars(PY2)
            self._loader = DummyVars()

    class DummyVars(object):
        def __init__(self, PY2=False):
            self.PY2 = PY2
            self._vars = {}

        def template(self, x):
            if type(x) == dict:
                return x
            return AnsibleUnsafeText(x)

        def set_available_variables(self, variables):
            self._vars = variables



# Generated at 2022-06-13 14:14:34.988861
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    # make sure it does not crash on empty terms
    module.run([], [], [])  # empty terms
    module.run([1], [], [])  # terms that are not a list
    module.run([[]], [], [])  # terms that are a list but not of two items
    module.run([[1], []], [], [])  # second item should be a string
    module.run([[1], [1]], [], [])  # second item should be a string
    module.run([[1], ['a']], [], [])  # first item should be a list or a dict
    module.run([{}, 'a'], [], [])  # first item should be a list or a dict

# Generated at 2022-06-13 14:14:42.985067
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Setup
    lookup = LookupModule()
    lookup.set_options({'_templar': None})
    lookup.set_context({'skip_missing': False})
    lookup._templar.environment.loader.set_basedir('/tmp')
    lookup._loader.set_basedir('/tmp')

    # Run
    result = lookup.run([{
        'key1': {
            'key11': 'value11',
            'key12': [
                'value121',
                'value122'
            ]
        },
        'key2': 'value2'
    }, 'key1.key12'], {})

    # Assert

# Generated at 2022-06-13 14:14:51.233473
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.template import Templar
    from ansible.parsing.vault import VaultLib

    def evaluate_retval(terms, retval, wantlist, replacer={}):
        # transform the returned list into a dict to support easy comparison
        items = dict(retval)
        # remove skipped items
        if terms[0][0].get('skipped', False) is not False:
            del(items['item0.0'])
        if terms[0][1].get('skipped', False) is not False:
            del(items['item0.1'])
        if terms[0][1]['authorized'][0].get('skipped', False) is not False:
            del(items['item0.1.0'])
       

# Generated at 2022-06-13 14:15:03.621083
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test subelements with list of dicts
    terms = [
        [
            {
                'a': {
                    'b': [
                        'one'
                    ]
                }
            },
            {
                'a': {
                    'b': [
                        'two'
                    ]
                }
            }
        ],
        'a.b'
    ]

    ret = LookupModule().run(terms, {})
    assert type(ret) is list
    assert len(ret) == 2
    assert ret[0][0]['a']['b'][0] == 'one'
    assert ret[0][1] == 'one'
    assert ret[1][0]['a']['b'][0] == 'two'
    assert ret[1][1] == 'two'

    # test sub

# Generated at 2022-06-13 14:15:13.546020
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import iteritems
    from ansible.plugins.lookup import LookupModule

    lookup_plugin = LookupModule()

# Generated at 2022-06-13 14:15:31.533519
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    instance = LookupModule()
    # data = [{'name': 'alice', 'authorized': ['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub']}]
    terms = [{'name': 'alice', 'authorized': ['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub']}, 'authorized']
    ret = instance.run(terms, None)

# Generated at 2022-06-13 14:15:43.236256
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    lookup = LookupModule()

    hostvars = {
        'server1': {
            'ansible_ssh_host': '192.168.1.10',
            'ansible_ssh_port': 22,
            'ansible_ssh_user': 'root',
            'ansible_ssh_private_key_file': '~/.ssh/id_rsa',
        }
    }

    # Test1:
    lookup_ret = lookup.run((hostvars, 'ansible_ssh_host'), loader)
    assrt = all(isinstance(key, dict) for key in lookup_ret)
    assert assrt is True
    assrt_list = []

# Generated at 2022-06-13 14:15:51.441128
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Unit test for run method"""

    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.plugins.lookup import LookupModule
    from ansible.utils.listify import listify_lookup_plugin_terms
    import os
    import tempfile
    import pytest


# Generated at 2022-06-13 14:16:02.783219
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_instance = LookupModule()
    lookup_instance._loader = AnsibleLoader()
    lookup_instance._templar = Templar(loader=lookup_instance._loader)
    lookup_instance._find_file_in_search_path = (lambda _1, _2: 'dummy_found_file')

    # add some dummy vars, to emulate a real lookup

# Generated at 2022-06-13 14:16:13.293667
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    import yaml
    yaml.warnings({'YAMLLoadWarning': False})

    # simple dictionary
    lookup_instance = LookupModule()
    lookup_instance.run([{"a": [1, 2]}, "a"]) == [({"a": [1, 2]}, 1), ({"a": [1, 2]}, 2)]

    # nested dictionary
    lookup_instance = LookupModule()
    lookup_instance.run([{"a": {"b": [1, 2]}}, "a.b"]) == [({"a": {"b": [1, 2]}}, 1), ({"a": {"b": [1, 2]}}, 2)]

    # list of dictionaries
    lookup_instance = LookupModule()

# Generated at 2022-06-13 14:16:21.684555
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import __builtin__
    real_getattr = getattr
    def mock_getattr(obj, name, default=None):
        if name == 'skipped':
            return False
        else:
            return real_getattr(obj, name, default)
    setattr(__builtin__, 'getattr', mock_getattr)

    terms = [
        [
            {'skipped': False, 'name': 'alice', 'authorized': ['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub']},
            {'name': 'bob', 'authorized': ['/tmp/bob/id_rsa.pub']}
        ],
        'authorized'
    ]
    result = LookupModule().run(terms, {})

# Generated at 2022-06-13 14:16:35.119335
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # create object and set default values
    lookup_obj = LookupModule()

    # define return values
    dict_list = [{"name": "alice", "authorized": ["/tmp/alice/onekey.pub", "/tmp/alice/twokey.pub"],
                 "mysql": {"password": "mysql-password", "hosts": ["%", "127.0.0.1", "::1", "localhost"],
                           "privs": ["*.*:SELECT", "DB1.*:ALL"]}},
                 {"name": "bob", "authorized": ["/tmp/bob/id_rsa.pub"],
                 "mysql": {"password": "other-mysql-password", "hosts": ["db1"], "privs": ["*.*:SELECT", "DB2.*:ALL"]}}]

    # run

# Generated at 2022-06-13 14:16:45.901737
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # create the test object
    l = LookupModule()

    # the setup:
    # test the case the first term is a list containing two hashes
    # and the second term is pointing to a subkey containing a list
    # with two elements

    # first term: a list containing two hashes

# Generated at 2022-06-13 14:16:57.887994
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    def _get_fake_cli_input(terms):
        return terms

    # testing subelements lookup as standalone code (not loaded as lookup plugin)
    lookup = LookupModule(_get_fake_cli_input,None)
    # Direct list of dictionaries with 2 keys
    terms = [ [{'key1': 'val1', 'key2': 'val2'}, {'key1': 'val3', 'key2': 'val4'}], 'key1']
    res = lookup.run(terms, None, None)
    print(res)
    assert res == [('val1',), ('val3',)]
    # list of dictionaries with 2 keys and flag skip_missing

# Generated at 2022-06-13 14:17:03.972319
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    subelement_test = LookupModule()
    for item in subelement_test.run([[{"test": [{"test1": "test2"}]}], "test.test1"], None):
        assert isinstance(item, tuple)
        assert item[0] == {"test": [{"test1": "test2"}]}
        assert item[1] == "test2"

# Generated at 2022-06-13 14:17:31.815159
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test initialization of module to test
    def get_templar(*args, **kwargs):
        return None

    def get_loader(*args, **kwargs):
        return None

    lookup_module = LookupModule(loader=get_loader, templar=get_templar)

    # define data structure that is used in test

# Generated at 2022-06-13 14:17:44.653657
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # tests for method run
    lm = LookupModule()
    lm.set_options({'skip_missing': 'True'})


# Generated at 2022-06-13 14:17:55.818023
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    def run(terms, result, error=None):
        lm = LookupModule()

        if error:
            try:
                ret = lm.run(terms, None)
            except Exception as e:
                return str(e)
            raise Exception("The expected error did not occur: %s" % terms)
        else:
            ret = lm.run(terms, None)
            if ret != result:
                raise Exception("Return value does not match: %s != %s" % (ret, result))

    # Constructor

    # run(self, terms, inject=None, **kwargs):
    run([], AnsibleError("subelements lookup expects a list of two or three items, "))

# Generated at 2022-06-13 14:18:05.183348
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # struct: { ..., 'spam': [{'spam': 'foo'}, {'eggs': 'spam'}], ...}

    # case 1: empty list of dictionaries
    t = []
    s = "spam"
    r = []
    assert r == LookupModule(loader=None, templar=None).run(t, s, **{})

    # case 2: empty list of subelements
    t = [{'spam': []}]
    s = "spam"
    r = []
    assert r == LookupModule(loader=None, templar=None).run(t, s, **{})

    # case 3: list of dictionaries with no subelements
    t = [{'spam': 'eggs'}]
    s = "spam"
    r

# Generated at 2022-06-13 14:18:09.713262
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = [
        {'localhost': {'mysql': {'password': 'mysql-password'}}, 'other': {'mysql': {'password': 'other-mysql-password'}}},
        'mysql.password',
    ]
    flags = {}
    assert LookupModule(loader=None, templar=None).run(terms, variables=None, **flags) == [('localhost', 'mysql-password'), ('other', 'other-mysql-password')]

    terms = [
        [{'mysql': {'password': 'mysql-password'}}, {'mysql': {'password': 'other-mysql-password'}}],
        'mysql.password',
    ]
    assert LookupModule(loader=None, templar=None).run(terms, variables=None, **flags)

# Generated at 2022-06-13 14:18:16.970074
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import binary_type, text_type


# Generated at 2022-06-13 14:18:24.631586
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest

    lookup = LookupModule()
    lookup._templar = None
    lookup._loader = None

    #testing the normal cases (works)
    with pytest.raises(AnsibleError) as excinfo:
        lookup.run([{'first': 1}, 'second', {'skip_missing': False}], None)
    assert 'second' in str(excinfo.value)

    with pytest.raises(AnsibleError) as excinfo:
        lookup.run([{'first': 1}, ['second'], {'skip_missing': False}], None)
    assert 'list' in str(excinfo.value)

    with pytest.raises(AnsibleError) as excinfo:
        lookup.run([{'first': 1}, 'second', ['skip_missing']], None)

# Generated at 2022-06-13 14:18:29.003847
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = [
        [
            {'foo': 1},
            {'bar': 2}
        ],
        'foo.alpha',
        {'skip_missing': True},
    ]
    result = LookupModule().run(terms, None)    
    assert result == []

# Generated at 2022-06-13 14:18:40.544354
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def _assert_run_equals(inlist, subkey, expected, flags={}):
        l = LookupModule()
        ret = l.run([inlist, subkey, flags])
        assert ret == expected, "expected:\n%s\nbut got:\n%s" % (expected, ret)

    # test with a dict as first term
    _assert_run_equals(
        {'first': {'authorized': ['one', 'two']}, 'second': {'authorized': ['three']}},
        "authorized",
        [({'authorized': ['one', 'two']}, 'one'), ({'authorized': ['one', 'two']}, 'two'), ({'authorized': ['three']}, 'three')],
    )

# Generated at 2022-06-13 14:18:50.948165
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from __main__ import LookupModule
    from ansible.module_utils.six import PY2
    lu = LookupModule(basedir='.')
    v1 = [{'name': "name1", "mysql": {'hosts': ["host1", "host2"], 'privs': ["priv1", "priv2"]}},
          {'name': "name2", "mysql": {'hosts': ["host3", "host4"], 'privs': ["priv3", "priv4"]}}]
    v2 = [{'name': "name1", "mysql": {'hosts': "host1", 'privs': "priv1"}},
          {'name': "name2", "mysql": {'hosts': "host3", 'privs': "priv3"}}]

# Generated at 2022-06-13 14:19:32.769223
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:19:34.260067
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: implement test
    pass

# Generated at 2022-06-13 14:19:47.163923
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    lookup_plugin = LookupModule()
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager,  host_list='tests/inventory')
    variable_manager.set_inventory(inventory)


# Generated at 2022-06-13 14:19:58.276945
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:20:08.263924
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_instance = LookupModule()

    # Case 1 - check number of terms
    # Case 1.1 - less than two items
    # Case 1.2 - more than three items
    try:
        lookup_instance.run([])
        assert False
    except AnsibleError:
        assert True
    except Exception:
        assert False

    try:
        lookup_instance.run(['item0', 'item1', 'item2', 'item3'])
        assert False
    except AnsibleError:
        assert True
    except Exception:
        assert False

    # Case 2 - first term is a list (or dict), second is a string
    # Case 2.1 - first term is a dict
    # Case 2.1.1 - second term is not a string
    # Case 2.1.2 - second term is a string
    #

# Generated at 2022-06-13 14:20:17.393050
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module_instance = LookupModule()
    skip_missing_true_expected_result = [('db1',), ('localhost',), ('::1',),('127.0.0.1',), ('%',)]
    skip_missing_false_expected_result = [('db1',), ('localhost',), ('::1',),('127.0.0.1',), ('%',)]
    empty_expected_result = []
    expected_error_message = "subelements lookup expects a dictionary, got 'bob'"
    expected_error_message_2 = "subelements lookup expects a dictionary, got 'alice'"


# Generated at 2022-06-13 14:20:29.742783
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module_name = LookupModule.__module__
    module = __import__(module_name)
    lookup = getattr(module, module_name.split('.')[-1])

    # expected tests - input, expected output, expected error (if applicable)

# Generated at 2022-06-13 14:20:38.906623
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    sys.path.append(".")
    from UnitTest.fixtures.lookuptests import LookupTestSuite
    import UnitTest.fixtures.lookuptests

# Generated at 2022-06-13 14:20:51.555008
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.parsing.convert_bool import boolean

    users = [
        {'name': 'Alice', 'authorized': ['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub']},
        {'name': 'Bob', 'authorized': ['/tmp/bob/id_rsa.pub', '/tmp/bob/id_rsa.pub'], 'skipped': True},
        {'name': 'Clara'},
        {'name': 'Steve', 'authorized': True},
        {'name': 'Guido', 'authorized': False},
        {'name': 'Bob', 'authorized': ['/tmp/bob/id_rsa.pub'], 'skipped': True}
    ]



# Generated at 2022-06-13 14:21:01.130889
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # initialization of the LookupModule
    terms = ["0", "0"]
    variables = dict()
    lu = LookupModule()

    # test
    result = lu.run(terms, variables)
    assert result == ['0']

    # initialization of the LookupModule
    terms = [["0", "1", "2"], "0"]
    variables = dict()
    lu = LookupModule()

    # test
    result = lu.run(terms, variables)
    assert result == [('0', '1'), ('1', '2')]

    # initialization of the LookupModule
    terms = ["0", "0", {"skip_missing": True}]
    variables = dict()
    lu = LookupModule()

    # test
    result = lu.run(terms, variables)

# Generated at 2022-06-13 14:22:21.288832
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    LookupModule_run = LookupModule.run

    # Testcase 1
    # Tested method:
    #   run(terms, variables, **kwargs) of class LookupModule
    # Expected result:
    #   - expects a list of two or three items
    #   - first a dict or a list, second a string pointing to the subkey
    #   - the optional third item must be a dict with flags
    # Input:
    #   - terms = not a list of two or three items
    #   - variables = variables
    #   - kwargs = kwargs
    # Returned result:
    #   - AnsibleError
    #   - "subelements lookup expects a list of two or three items, " + msg
    terms = "not a list of two or three items"

# Generated at 2022-06-13 14:22:33.243791
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes, to_text
    import json

    module_args = dict(
        terms=json.dumps([
            {'skipped': True},
            'test.test2',
            {'skip_missing': False}
        ]))
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
    )
    lookup_args = {'module_args': module_args}

    # Define a list of return values and their expected result

# Generated at 2022-06-13 14:22:46.437433
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    look = LookupModule()
    look.set_options({'run_once': True})
    look.set_runner({})
    # no list
    assert look.run([{'a':'b'}], {}, templar=None) == [], "no list should give empty list"
    assert look.run([], {}, templar=None) == [], "empty list should give empty list"
    # list of wrong number of elements
    assert look.run([[1,2]], {}, templar=None) == [], "list with one element should give empty list"
    assert look.run([[1,2,3,4]], {}, templar=None) == [], "list with 4 element should give empty list"
    # list, but first element is not a list

# Generated at 2022-06-13 14:22:55.797808
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''
    Test that the lookup_scheme_terms gets the desired output
    '''
    #Get a lookup object of class LookupModule
    lookup_obj = LookupModule()

    #Create a dummy 'variable' object
    variable_obj = {}

    #Check output
    user_list = [{'name': 'Adam', 'password': '123', 'authorized': ['/home/abc', '/home/def'], 'role': 'admin'}, {'name': 'Ben', 'password': '456', 'authorized': ['/home/ghi', '/home/jkl'], 'role': 'manager'}]
    update_key = 'authorized'

# Generated at 2022-06-13 14:23:07.789538
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = [
        [
            {
                'name': 'alice',
                'mysql': {
                    'hosts': [
                        '%',
                        '127.0.0.1',
                        '::1',
                        'localhost',
                    ],
                },
            },
            {
                'name': 'bob',
                'mysql': {
                    'hosts': [
                        'db1',
                    ],
                },
            },
        ],
        'mysql.hosts',
    ]

# Generated at 2022-06-13 14:23:20.416900
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    values = [{'name': 'foo', 'mysql': {'hosts': ['a', 'b'], 'password': 'password', 'privs': ['X']}}]
    assert LookupModule().run([values, 'mysql.hosts']) == [({'name': 'foo', 'mysql': {'password': 'password', 'privs': ['X']}}, 'a'), ({'name': 'foo', 'mysql': {'password': 'password', 'privs': ['X']}}, 'b')]
    assert LookupModule().run([values, 'mysql.fake']) == []
    assert LookupModule().run([values, 'mysql.fake', {'skip_missing': True}]) == []
    assert LookupModule().run([values, 'mysql.fake', {'skip_missing': False}])

# Generated at 2022-06-13 14:23:32.664313
# Unit test for method run of class LookupModule