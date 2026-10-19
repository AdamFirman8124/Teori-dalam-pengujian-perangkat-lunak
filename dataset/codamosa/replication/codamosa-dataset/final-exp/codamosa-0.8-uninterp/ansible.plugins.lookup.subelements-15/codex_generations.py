

# Generated at 2022-06-13 14:13:40.862739
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Default
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    options = Options()
    variable_manager = VariableManager()
    loader = DataLoader()
    passwords = dict()

    # Playbook
    inventory = Inventory(loader, variable_manager, Options())
    variable_manager = VariableManager(loader=loader, inventory=inventory)

# Generated at 2022-06-13 14:13:49.643452
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import lookup_loader
    lookup = lookup_loader.get('subelements', class_only=True)()
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    from ansible.vars.manager import VariableManager
    variable_manager = VariableManager()
    import os
    fixture_path = os.path.dirname(os.path.dirname(__file__)) + '/ansible/test/unit/plugins/lookup/fixtures/subelements_lookup_plugin'
    variables = loader.load_from_file(fixture_path + '/users.yml')
    variable_manager.set_vars(variables)

# Generated at 2022-06-13 14:13:58.693246
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import json
    import sys
    from ansible.module_utils.parsing.convert_bool import boolean

    users = json.loads("""[
        {
            "name": "alice",
            "mysql": {
                "password": "mysql-password",
                "hosts": ["%", "127.0.0.1", "::1", "localhost"],
                "privs": ["*.*:SELECT", "DB1.*:ALL"]
            }
        },
        {
            "name": "bob",
            "mysql": {
                "password": "other-mysql-password",
                "hosts": ["db1"],
                "privs": ["*.*:SELECT", "DB2.*:ALL"]
            }
        }
    ]""")
    lm = LookupModule()


# Generated at 2022-06-13 14:14:10.056549
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert list(LookupModule(None, None, None).run([['skipped'], 'skipped', {'skip_missing': True}])) == []
    assert list(LookupModule(None, None, None).run(['skipped', 'skipped', {'skip_missing': True}])) == []
    assert list(LookupModule(None, None, None).run(['skipped', 'skipped'])) == []

    # single item
    assert list(LookupModule(None, None, None).run(
        [{'key1': 'value1'}, 'key1'])) == [('value1',)]

# Generated at 2022-06-13 14:14:21.041722
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # create class for unit test
    class TestLookupModule(LookupModule):
        def __init__(self):
            self._templar = None
            self._loader = None

    # define subelements dictionary

# Generated at 2022-06-13 14:14:33.768546
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:14:37.903673
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    # test that the class has the right methods
    assert callable(lookup_module.run)
    assert callable(lookup_module.run_command)
    assert callable(lookup_module.run_command_environ)


test_LookupModule_run()

# Generated at 2022-06-13 14:14:48.099170
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """ Test the run method of LookupModule """

    # create lookup object
    lu = LookupModule()
    # setup ansible context
    lu._templar = None
    lu._loader = None

    # raise AnsibleError if terms is not a list
    terms = {}
    try:
        lu.run(terms, None)
    except AnsibleError as e:
        assert 'expected list' in e.message
    else:
        assert False, 'AnsibleError not raised'

    # raise AnsibleError if terms is a list with length != 2 or 3
    terms = []
    try:
        lu.run(terms, None)
    except AnsibleError as e:
        assert 'expected list of two or three items' in e.message

# Generated at 2022-06-13 14:15:00.984897
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test dependencies
    import pytest

    # test setup
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.parsing.yaml.objects import AnsibleMapping

    # test targets
    lookup_module = LookupModule()

    # test input

# Generated at 2022-06-13 14:15:11.440839
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test 1: scan a simple list
    testterms = [
        [
            {'key1': 'value1', 'key2': [1, 2, 3]},
            {'key1': 'value2', 'key2': [4, 5, 6]}
        ],
        'key1'
    ]
    look = LookupModule()
    result = look.run(terms=testterms, variables=dict())
    assert result == [('value1',), ('value2',)]

    # Test 2: scan a simple dictionary
    testterms = [
        {
            'key1': {'key2': 'value1'},
            'key2': {'key2': 'value2'}
        },
        'key2'
    ]
    result = look.run(terms=testterms, variables=dict())

# Generated at 2022-06-13 14:15:30.610280
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    result = LookupModule().run([[{}, {"item1": []}], "item1"])
    assert result == [({},)]
    result = LookupModule().run([[{}, {"item1": []}], "item2"])
    assert result == []
    result = LookupModule().run([[{}, {"item1": []}], "item2", {'skip_missing': True}])
    assert result == []
    with raises(AssertionError):
        result = LookupModule().run([[{}, {"item1": []}], "item2", {'skip_missing': True, 'unknown_flag': 'value'}])

# Generated at 2022-06-13 14:15:42.355748
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup import LookupModule
    lookup_module = LookupModule()

    # test with default flags
    terms = [
        {'item0': [{'subkey': ['test1', 'test2']}, {'subkey': ['test3', 'test4']}]}, # terms[0]
        "subkey" # terms[1]
    ]
    result = lookup_module.run(terms, None)
    assert result[0][0] == {'subkey': ['test1', 'test2']}, "expected {'subkey': ['test1', 'test2']}, got %s" % result[0][0]

# Generated at 2022-06-13 14:15:54.142626
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible.parsing.yaml.objects import AnsibleUnicode
    lookup_module = LookupModule()

    terms = [
        {'item1': {'subitem1': ['value1', 'value2'], },
         'item2': {'subitem2': ['value3', 'value4'], },
         'item3': {'subitem3': ['value5', 'value6'], }, },
        'subitem1',
    ]

    # check number of results
    assert len(lookup_module.run(terms, {}, wantlist=True)) == 2

    # check types of results
    for result in lookup_module.run(terms, {}, wantlist=True):
        assert isinstance(result[0], dict)

# Generated at 2022-06-13 14:16:04.807676
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookups = LookupModule()

    # test first term error: not list
    with pytest.raises(AnsibleError):
        ret = lookups.run('test', None)

    # test first term error: wrong number of items
    with pytest.raises(AnsibleError):
        ret = lookups.run(['test', 'test', 'test', 'test'], None)

    # test first term error: first term not a list or a dict
    with pytest.raises(AnsibleError):
        ret = lookups.run(['test', 'test'], None)

    # test first term error: second term not a string
    with pytest.raises(AnsibleError):
        ret = lookups.run([['test'], ''], None)

    # test second term error: not a dict


# Generated at 2022-06-13 14:16:16.938645
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    def _run(terms, variables, expect, lookup=LookupModule):
        obj = lookup()
        got = obj.run(terms, variables)
        assert expect == got

    _run(['{{ a }}'], {'a': [{'b': ['1', '2']}]}, [('1',), ('2',)])
    _run([{'a': [{'b': ['1', '2']}]}], {}, [('1',), ('2',)])
    _run([{'a': [{'b': ['1', '2']}]}], {}, [('1',), ('2',)])

# Generated at 2022-06-13 14:16:25.620473
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Validate the LookupModule.run method"""
    lookup_module = LookupModule()

# Generated at 2022-06-13 14:16:30.714087
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import tempfile
    from ansible.module_utils.six import PY3
    # Note: LookupModule inherits from object (not AnsibleModule)
    # so we need to set the ansible_module=self explicitly in the tests
    # 'ansible_module' is an argument of LookupModule.run

    # define class to be used in tests
    class MockLookupModule(LookupModule):
        def __init__(self):
            self.ansible_module = None
            pass

        def run(self, terms, variables, **kwargs):
            # as MockedLookupModule inherits from LookupModule we can test this method
            # with the methods of LookupModule
            return super(MockLookupModule, self).run(terms, variables, ansible_module=self)


# Generated at 2022-06-13 14:16:43.068519
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import PY3
    from ansible.parsing.dataloader import DataLoader


# Generated at 2022-06-13 14:16:50.303324
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys, os
    sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
    from ansible.module_utils.six import PY2
    from ansible.module_utils.six.moves import builtins
    import pytest
    from ansible.errors import AnsibleError
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.template import Templar

    def _get_loader(data):
        return DataLoader(vars(builtins), variable_manager.get_vars())

    variable_manager = VariableManager()
    variable_manager.extra_vars = {'inventory_hostname': 'dummy'}


# Generated at 2022-06-13 14:17:03.407041
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''
    Unit test for method run of class LookupModule
    '''
    from ansible.plugins.lookup import LookupModule
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.utils.listify import listify_lookup_plugin_terms

    # Test function with two terms
    #
    # In this case, terms[0] is users and terms[1] is mysql.password.
    # Database password of user Alice is 'mysql-password'.
    # Database password of user Bob is 'other-mysql-password'.
    #
    # In this case, the subelements method returns password of users
    # Alice and Bob.
    #
    # The expected result is [(Alice, mysql-password),(Bob,other-mysql-password)]


# Generated at 2022-06-13 14:17:31.068461
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def raise_terms_error(msg=""):
        raise AnsibleError(
            "subelements lookup expects a list of two or three items, " + msg)

    # test for wrong number of terms
    terms = []
    if not isinstance(terms, list) or not 2 <= len(terms) <= 3:
        raise_terms_error()
    terms = ('', '')
    if not isinstance(terms, list) or not 2 <= len(terms) <= 3:
        raise_terms_error()
    terms = ('', '', '', '')
    if not isinstance(terms, list) or not 2 <= len(terms) <= 3:
        raise_terms_error()

    # test for wrong type of terms
    terms = ((), '')

# Generated at 2022-06-13 14:17:44.029836
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Module is not loaded as module, but as class
    if __name__ == "__main__":
        raise Exception("Can not run unit test directly. Run unit test via plugins/lookup/test.py")
    def _terms(terms, exp_value, exp_kwargs):
        l = LookupModule()
        l.set_options(exp_kwargs)
        return l.run(terms, None, **exp_kwargs)

    # _terms:
    #    description: tuple of list of dictionaries and dictionary key to extract
    #    required: True
    # skip_missing:
    #    description:
    #      - Lookup accepts this flag from a dictionary as optional. See Example section for more information.
    #      - If set to C(True), the lookup plugin will skip the lists items that do not contain the given subkey.

# Generated at 2022-06-13 14:17:55.274059
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import PY2, PY3
    from ansible.module_utils.six.moves import builtins
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.errors import AnsibleError
    import sys

    # Mock the open_func for the LookupBase class
    class MockLoader:
        def __init__(self, flags):
            self.flags = flags

        def get_basedir(self, task_vars):
            pass

        def is_file(self, fn):
            return fn.find('/') > 0

    lf = LookupModule(MockLoader({}))


# Generated at 2022-06-13 14:18:04.893812
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    subelements = LookupModule()
    # test different input types
    assert subelements.run(["something", "someother", "someflags"], None) == []
    assert subelements.run([], None) == []
    assert subelements.run("not a list", None) == []
    assert subelements.run(None, None) == []
    assert subelements.run(True, None) == []
    assert subelements.run(42, None) == []
    # test different subkey types
    testlist = ["something", ["another", "yetanother"], 4242]
    assert subelements.run([testlist, "something"], None) == []
    assert subelements.run([testlist, ["something"]], None) == []
    assert subelements.run([testlist, 42], None) == []

# Generated at 2022-06-13 14:18:16.798451
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    terms = [{
                 "user_foo": {"login": "foo", "password": "foo"},
                 "user_bar": {"login": "bar", "password": "bar"},
             }, "user_foo.password", {'skip_missing': True}]
    result = module.run(terms, {})
    assert result == [('foo',)]

    terms = [{
                 "user_foo": {"login": "foo", "password": "foo"},
                 "user_bar": {"login": "bar", "password": "bar"},
             }, "user_foo.unknown_item"]
    result = module.run(terms, {})
    assert result == []


# Generated at 2022-06-13 14:18:22.235463
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.utils.listify import listify_lookup_plugin_terms

    # We use a class only for test case, not for the module itself.
    class AnsibleModule(object):
        def __init__(self, argument_spec, bypass_checks=False, no_log=False,
                     mutually_exclusive=[], required_together=[], required_one_of=[], add_file_common_args=False,
                     supports_check_mode=False):
            self.params = dict()

        def fail_json(self, msg=None, **kwargs):
            raise Exception(msg)

        def exit_json(self, **kwargs):
            return kwargs

    module = AnsibleModule(
        argument_spec={})

    #

# Generated at 2022-06-13 14:18:34.727749
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    # Test case 1
    # Test successful run, with a valid terms.

# Generated at 2022-06-13 14:18:44.211990
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # create a test object
    lookup_plugin = LookupModule()

    ############################################################
    # Test with three parameters, no optional flags
    ############################################################
    elementlist = [
        {'name': 'alice',
         'authorized': ['/home/alice/.ssh/alice-key.pub']},
        {'name': 'bob',
         'authorized': ['/home/bob/.ssh/bob-key.pub']},
        {'name': 'chuck',
         'authorized': ['/home/chuck/.ssh/chuck-key.pub']}
    ]
    terms = [elementlist, 'authorized']

# Generated at 2022-06-13 14:18:50.081651
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import PY3
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.plugins.loader import lookup_loader

    # Initialise test variables

# Generated at 2022-06-13 14:19:02.250955
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # non-exact matches
    users = [
        {'name': 'alice', 'groups': ['a', 'b', 'c']},
        {'name': 'bob', 'groups': ['b', 'c', 'd']},
        {'name': 'carol', 'groups': ['c', 'd', 'e']},
        {'name': 'dave', 'groups': ['d', 'e', 'f']},
    ]

    # local_lookup_plugin = LookupModule()
    # local_lookup_plugin._loader = DictDataLoader({})
    # local_lookup_plugin._templar = Templar(loader=local_lookup_plugin._loader)

    # result = local_lookup_plugin.run([users, 'groups', {'skip_missing': True}], {})
    #

# Generated at 2022-06-13 14:19:45.698478
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:19:54.178127
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    lookup = LookupModule()
    ret = lookup.run(
      [  # terms
        [
          {"name": "alice", "authorized": ["/tmp/alice/onekey.pub","/tmp/alice/twokey.pub",]},
          {"name": "bob", "authorized": ["~/bob/id_rsa.pub"]}
        ],
        "authorized"
      ],
      [],  # variables
      {},  # kwargs
      loader=None,
      templar=None,
      shared_loader_obj=None
    )

    curpath = os.path.dirname(os.path.realpath(__file__))
    curpath = os.path.abspath(curpath)

# Generated at 2022-06-13 14:20:05.151055
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:20:15.922158
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Unit test for method run of class LookupModule"""
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    mock_loader_class = DataLoader()
    mock_loader = mock_loader_class.load_from_file
    play_context = PlayContext()
    templar = Templar(loader=mock_loader, variables=VariableManager())
    lookup_plug = LookupModule()
    lookup_plug.set_options({'_terms': [({"skip_me": True, "dont_skip_me": {"sublist": [1, 2, 3], "subdict": {}}}, "sublist"), {'skip_missing': True}]})
    lookup

# Generated at 2022-06-13 14:20:27.832705
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Initialize test
    test = LookupModule()
    test._templar = None
    test._loader = None
    test.set_options()

    # Initialize users
    users = dict()
    users['alice'] = dict()
    users['alice']['name'] = 'alice'
    users['alice']['authorized'] = ['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub']
    users['alice']['mysql'] = dict()
    users['alice']['mysql']['password'] = 'mysql-password'
    users['alice']['mysql']['hosts'] = ['%', '127.0.0.1', '::1', 'localhost']

# Generated at 2022-06-13 14:20:31.136641
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    print("test_LookupModule_run disabled")
    #test_list = [{"name": "key1", "value": 1}, {"name": "key2", "value": 2}]
    #assert(LookupModule.run(None, [test_list, "name"]) == ["key1", "key2"])

# Generated at 2022-06-13 14:20:36.421783
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    global terms, elementlist, subelements
    print(__file__)
    print(terms)
    print(elementlist)
    print(subelements)
    print(isinstance(terms, list))
    print(2 <= len(terms) <= 3)
    print(isinstance(terms[0], (list, dict)))
    print(isinstance(terms[1], string_types))
    subelements = terms[1].split(".")

# Generated at 2022-06-13 14:20:42.309764
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = [[
        {'k1': 'v1', 'k2': 'v2'},
        {'k1': 'v3', 'k2': 'v4'}], 'k1']

    class VariablesModuleDummy(object):
        pass

    variables = VariablesModuleDummy()
    lookup_obj = LookupModule()

    result = lookup_obj.run(terms, variables)
    assert result == ['v1', 'v3']

# Generated at 2022-06-13 14:20:55.181532
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.parsing.convert_bool import boolean
    
    # create LookupModule object from class LookupModule
    lookup_module = LookupModule()

    # args for method run of class LookupModule

# Generated at 2022-06-13 14:21:06.751473
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six.moves import StringIO

    # assert lookup method on returned data
    #
    # data:
    # users:
    #   - name: alice
    #     mysql:
    #         password: mysql-password
    #         hosts:
    #           - "%"
    #           - "127.0.0.1"
    #           - "::1"
    #           - "localhost"
    #           - "db1"
    #           - "db2"
    #           - "db3"
    #           - "db4"
    #           - "db5"
    #           - "db6"
    #           - "db7"
    #           - "db8"
    #           - "

# Generated at 2022-06-13 14:22:23.562335
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    users = [
        {'name': "alice", 'authorized': ['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub']},
        {'name': "bob", 'mysql':{'hosts': ['bar', 'baz'], 'password': "qwerty123"}},
        {'name': "eve", 'authorized': ['/tmp/eve/id_rsa.pub'], 'mysql': {'hosts': ['bar', 'baz'], 'password': "qwerty123"}},
    ]

    testobj = LookupModule()

    result = testobj.run([users, 'authorized'], None, skip_missing=False)
    assert len(result) == 3

# Generated at 2022-06-13 14:22:27.102706
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup = LookupModule()
    result = lookup.run(('test_input', 'list_key'))

    assert result == ['key1', 'key2', 'key3']

# Generated at 2022-06-13 14:22:38.242087
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:22:51.309439
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.listify import listify_lookup_plugin_terms

    terms = listify_lookup_plugin_terms({
        '_raw_params': ['lookup_file:tmplt1.txt'],
        '_terms': ['lookup_file:tmplt1.txt']
    }, loader=None, templar=None)


# Generated at 2022-06-13 14:22:58.222777
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    def _run_LookupModule_run(terms, expected):
        from ansible.parsing.dataloader import DataLoader
        from ansible.vars import VariableManager
        from ansible.inventory import Inventory
        variable_manager = VariableManager()
        loader = DataLoader()
        inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list=[])
        lm = LookupModule()
        lm.set_loader(loader)
        lm.set_inventory(inventory)
        lm.set_variable_manager(variable_manager)

        assert expected == lm.run(terms, variables=None)

    # Users dictionnary

# Generated at 2022-06-13 14:23:09.061634
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    test_lookup = LookupModule()
    lst = '[{"key": "value", "dict": {"key2": "value2"}}]'
    with pytest.raises(AnsibleError, match=r"2.* 3.*"):
        test_lookup.run([lst, "dict.key2"], {})
    with pytest.raises(AnsibleError, match=r"list.*string"):
        test_lookup.run([lst, ["dict.key2"]], {})
    with pytest.raises(AnsibleError, match=r"dict.*string"):
        test_lookup.run([lst, {"dict.key2": "value2"}], {})


# Generated at 2022-06-13 14:23:21.319365
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup import LookupModule
    import json
    import pytest

    with pytest.raises(AnsibleError) as exc:
        lookup_module = LookupModule()
        lookup_module.run((('hostvars', 'ansible_default_ipv4'), ), dict())
    assert "subelements lookup expects a list of two or three items, first a dict or a list, second a string pointing to the subkey" == str(exc.value)

    with pytest.raises(AnsibleError) as exc:
        lookup_module = LookupModule()
        lookup_module.run(('hostvars', 1, 'skip_missing'), dict())
    assert "subelements lookup expects a list of two or three items, first a dict or a list, second a string pointing to the subkey" == str