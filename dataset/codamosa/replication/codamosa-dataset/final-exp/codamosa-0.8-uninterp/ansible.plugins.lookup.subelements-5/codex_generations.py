

# Generated at 2022-06-13 14:13:41.330120
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    def assert_ret_result(expected, result):
        assert expected==result

    class LookupModuleUnderTest(LookupModule):
        def __init__(self):
            self._loader = Mock( )
            self._templar = Mock()
            self._loader.list_enabled_plugins = Mock(return_value=[])

    lookup_module = LookupModuleUnderTest()

    assert_ret_result([],
        lookup_module.run(['foo'], Mock()))

    users = [
        {'name': 'john'},
        {'name': 'peter'}
    ]

    assert_ret_result(
        [('john', 'alice')],
        lookup_module.run([users, 'friend'], Mock(), skip_missing=False)
    )


# Generated at 2022-06-13 14:13:49.992485
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit test of method run of class LookupModule
    """
    from units.mock.loader import DictDataLoader

    lookup_plugin = LookupModule()
    inventory = DictDataLoader({
        "hostvars": {
            "localhost": {"users": [{
                "name": "alice",
                "authorized": [
                    "/tmp/alice/onekey.pub",
                    "/tmp/alice/twokey.pub"]
            }, {
                "name": "bob",
                "authorized": [
                    "/tmp/bob/id_rsa.pub"]
            }]}}})
    lookup_plugin._loader = inventory
    result = lookup_plugin.run([
        ["localhost", "users"],
        "authorized"])

# Generated at 2022-06-13 14:13:51.634184
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # run is the only method of this class, so this is a bit stupid
    assert True

# Generated at 2022-06-13 14:13:59.857843
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:14:10.203660
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    subelements = LookupModule()

    # test with two terms
    terms = [
        [
            {'key1': {'mysql': {'hosts': ['host1']}}},
            {'key2': {'mysql': {'hosts': ['host2']}}},
            {'key3': {'mysql': {'hosts': ['host3']}}}
        ],
        'mysql.hosts'
    ]

# Generated at 2022-06-13 14:14:21.150919
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # init LookupModule object
    lookup_module = LookupModule()

    # init templar object
    templar = Templar(loader=None, variables=None)

    # init data for testing
    data = '''
        ---
        # a list of records
        - name: alice
          authorized:
            # 2 records in authorized sublist
            - /tmp/alice/onekey.pub
            - /tmp/alice/twokey.pub
        - name: bob
          authorized:
            # 1 records in authorized sublist
            - /tmp/bob/id_rsa.pub
        - name: doe
          # no authorized records
        '''

    # test simple case

# Generated at 2022-06-13 14:14:28.493448
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import BytesIO
    from ansible.module_utils._text import to_bytes
    import yaml

# Generated at 2022-06-13 14:14:39.217184
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    try:
        # import ansible.utils.display as display
        from ansible.utils.display import Display
    except ImportError:
        # we're using a test version of Ansible that doesn't have utils
        raise ImportError("missing required Ansible code, please use a more recent version")
    display = Display()


# Generated at 2022-06-13 14:14:48.839221
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Inits
    users = list()

    # Alice
    user = dict()
    user["name"] = "alice"
    user["authorized"] = list()
    user["authorized"].append("/tmp/alice/onekey.pub")
    user["authorized"].append("/tmp/alice/twokey.pub")
    user["mysql"] = dict()
    user["mysql"]["password"] = "mysql-password"
    user["mysql"]["hosts"] = list()
    user["mysql"]["hosts"].append("%")
    user["mysql"]["hosts"].append("127.0.0.1")
    user["mysql"]["hosts"].append("::1")

# Generated at 2022-06-13 14:15:01.515085
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:15:16.554895
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    LookupModule:subelements - Arbitrary String

    """

# Generated at 2022-06-13 14:15:27.489872
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:15:31.003939
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    def my_assert(cond, msg=""):
        if not cond:
            raise Exception("AssertionError: " + msg)

    my_assert(False, "Tests not yet implemented")

    # TODO: implement unit tests

    return

# Generated at 2022-06-13 14:15:42.795322
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.vars.unsafe_proxy import wrap_var


# Generated at 2022-06-13 14:15:54.437083
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import unittest
    import sys
    import os
    import warnings
    warnings.filterwarnings("ignore")
    sys.path.append(os.path.join(sys.path[0], '..', '..', '..'))
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    import ansible.constants as C

    class TestLookupModule(unittest.TestCase):
        def setUp(self):
            self.loader = DataLoader()
            self.inventory = InventoryManager(self.loader, [])

# Generated at 2022-06-13 14:16:04.931196
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:16:14.919775
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''
    A unit test for LookupModule.run()
    '''
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources="")
    variable_manager.set_inventory(inventory)

# Generated at 2022-06-13 14:16:22.504987
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Method run of class LookupModule test cases."""

    # Required modules and methods
    from ansible.plugins.lookup import LookupBase

    class AnsibleMock(object):
        """Ansible mock."""

        class AnsibleModuleMock(object):
            """Ansible module mock."""

            def __init__(self, argument_spec, **kwargs):
                """Constructor."""
                self.params = dict()

            def fail_json(self, **kwargs):
                """Fail json method."""
                self.exit_args = kwargs
                self.exit_called = True

        class AnsibleLookupBaseMock(LookupBase):
            """Ansible lookup base mock."""

            def run(self, terms, variables=None, **kwargs):
                """Run method."""
               

# Generated at 2022-06-13 14:16:35.344404
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup.subelements import LookupModule
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    # first test

# Generated at 2022-06-13 14:16:45.938093
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:17:10.592338
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup_module = LookupModule()

    # create a stub for templar
    templar = type("Templar", (object,), dict())()
    # create a stub for loader
    loader = type("Loader", (object,), dict())()

    # create a basic list of dictionaries
    globals = dict()

# Generated at 2022-06-13 14:17:19.651016
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


# Generated at 2022-06-13 14:17:31.615162
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = [
        [
            {
                "foo": {
                    "bar": [1, 2, 3]
                }
            },
            {
                "foo": {
                    "bar": [4, 5, 6]
                }
            },
            {
                "foo": {
                    "bar": [7, 8, 9]
                }
            },
        ],
        "foo.bar"
    ]
    ret = LookupModule().run(terms=terms, variables={})

# Generated at 2022-06-13 14:17:44.449977
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # use temporary empty dicts for this test
    class DummyVars(dict):
        def __init__(self, *args, **kwargs):
            for k, v in kwargs.items():
                self[k] = v

    class DummyVariables:
        def __init__(self, vars):
            self._vars = vars

        def get_vars(self, play, host, task, include_hostvars=True, include_delegate_to=True):
            return self._vars

    class DummyLoader:
        def __init__(self, vars):
            pass

    class DummyTemplar:
        def __init__(self, vars):
            pass

        def template(self, value, **kwargs):
            return value


# Generated at 2022-06-13 14:17:55.610349
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import BytesIO
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six.moves import cStringIO
    from ansible.module_utils._text import to_bytes, to_native
    from ansible.errors import AnsibleError
    import os
    import ansible.plugins.loader
    # read fixture file
    fixtures = os.path.join(os.path.dirname(__file__), 'fixtures', 'subelements.yml')
    with open(fixtures) as f:
        fixture_data = to_bytes(f.read())
    # construct LookupModule with stdin

# Generated at 2022-06-13 14:18:02.033726
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import iteritems
    import pytest

    def _check(terms, expected, elementlist):
        # instantiate lookup with test data
        l = LookupModule()
        l.set_options(direct=dict(elementlist=elementlist))
        # execute run method
        result = l.run(terms, variables=dict())

        # check result
        if len(expected) != len(result):
            return False
        zip_result = zip(result, expected)
        for item in zip_result:
            # 1st element
            # check 1st item, should be a dictionary
            if not all(isinstance(key, string_types) for key in item[0][0]):
                return False
            # check existence of skipped key and value should be false

# Generated at 2022-06-13 14:18:13.254608
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:18:22.977849
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    sys.path.append('/usr/share/ansible')
    from ansible.playbook.play_context import PlayContext
    import pytest
    from ansible.parsing.vault import VaultSecret
    from ansible.template import Templar
    from units.mock.loader import DictDataLoader


# Generated at 2022-06-13 14:18:35.755993
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:18:47.328264
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import PY2

    # Template
    template_ansible_module = '''
      - name: test string passed
        hosts: localhost
        connection: local
        gather_facts: False
        tasks:
          - name: do something
            fail:
              msg: '{{ result | to_json }}'
            with_subelements: '{{ lookup("subelements", "{}", "{}") }}'
        '''

    # Template to test skipped items

# Generated at 2022-06-13 14:19:28.615069
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create an instance of LookupModule
    lookup = LookupModule()
    # Simple subelement lookup:
    # result of first lookup should be a list of tuples (x, y)
    # where x is the elements of 'users'
    # and y is the subelements of 'authorized' key in each of the elements of 'users'
    # and 'authorized' points to a list of keys

# Generated at 2022-06-13 14:19:42.151328
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # import public API symbols
    import ansible.plugins.lookup
    _import_plugins(ansible.plugins.lookup)

    # instantiate the class
    lookup_module = LookupModule()

    # call run method
    result = lookup_module.run([{'skipped': True}])
    assert result == []

    result = lookup_module.run([{'skipped': False}])
    assert result == []

    result = lookup_module.run([{'skipped': 'other value'}])
    assert result == []

    result = lookup_module.run([])
    assert result == []

    result = lookup_module.run([{'skipped': False, 'a': 'b', 'c': 'd'}])
    assert result == []


# Generated at 2022-06-13 14:19:52.214164
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:19:57.849491
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    terms = dict()

    terms = dict()
    terms = dict()
    # test empty terms
    terms[0] = []
    ret = module.run(terms, variables=dict(), **dict())
    assert ret == []

    # test wrong number of terms
    for nterms in [1, 4]:
        terms[0] = [0] * nterms
        try:
            module.run(terms, variables=dict(), **dict())
            assert False
        except AnsibleError as e:
            assert "subelements lookup expects a list of two or three items" in "%s" % e

    # test first term as dict instead of list
    terms[0] = dict()

# Generated at 2022-06-13 14:20:08.015506
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import unittest
    import ansible
    import sys
    import os
    if sys.version_info < (3, 3):
        import mock
    else:
        from unittest import mock

    test_path = os.path.dirname(ansible.__file__)
    sys.path.append(
        os.path.join(
            test_path,
            'plugins',
            'lookup'
        )
    )

    from module_utils.facts.system.distribution.linux import distribution


# Generated at 2022-06-13 14:20:14.055031
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:20:25.354492
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lu = LookupModule()

    elementlist = [
        {
            "name": 'alice',
            "authorized": [
                "/tmp/alice/onekey.pub",
                "/tmp/alice/twokey.pub",
                ],
            },
        {
            "name": 'bob',
            "authorized": [
                "/tmp/bob/id_rsa.pub",
                ],
            "mail": [
                "alice@example.com",
                ],
            },
        ]


# Generated at 2022-06-13 14:20:32.402570
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit test for method run of class LookupModule
    """
    # test empty terms
    #
    # setup parameters
    terms = []
    variables = {}

    # execute
    lookup_module = LookupModule()
    result = lookup_module.run(terms, variables)

    # assert
    assert result == []

    # test incomplete terms
    #
    # setup parameters
    terms = [ {} ]
    variables = {}

    # execute
    lookup_module = LookupModule()
    result = lookup_module.run(terms, variables)

    # assert
    assert result == []

    # test simple terms
    #
    # setup parameters

# Generated at 2022-06-13 14:20:43.003457
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    #test if method run of class LookupModule works properly
    l = LookupModule()
    l.set_options(direct={"skip_missing": "True"})

    terms = [{'a': {'b': 'a1'}}, 'a.b']

    ret = l.run(terms,
                {},
                inject={'skip_missing': 'False'})

    assert ret == [('a1')]

    terms = [{'a': {'b': [{'c': 'a1'}, {'c': 'a2'}]}, 'd': {'b': [{'c': 'd1'}, {'c': 'd2'}]}}, 'b.c']

    ret = l.run(terms,
                {},
                inject={'skip_missing': 'True'})


# Generated at 2022-06-13 14:20:55.025464
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_item = "test_item"
    test_subelements_key = "test_subelements_key"
    test_subelements_content = "test_subelements_content"
    test_subelements_content_dict = {test_item: test_subelements_content}
    test_subelements_dict = {test_subelements_key: test_subelements_content_dict}
    lm = LookupModule()
    assert lm.run(
        terms=[test_subelements_dict, "test_subelements_key.test_item"],
        variables=None,
        **{}) == [test_subelements_content]

# test_LookupModule_run()

# Generated at 2022-06-13 14:22:07.442963
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:22:21.244414
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six.moves import builtins

    lM = LookupModule()

    terms = []
    variables = {}
    ret = lM.run(terms, variables)
    assert ret == []

    terms = ["a"]
    variables = {}
    with pytest.raises(AnsibleError):
        ret = lM.run(terms, variables)
    ret = lM.run(terms, variables, ignore_errors=True)
    assert ret == []

    terms = ["a", "b"]
    variables = {}
    with pytest.raises(AnsibleError):
        ret = lM.run(terms, variables)
    ret = lM.run(terms, variables, ignore_errors=True)
    assert ret == []

    # test with a list of dictionaries and a subkey

# Generated at 2022-06-13 14:22:21.732716
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 14:22:22.772476
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO
    pass

# Generated at 2022-06-13 14:22:35.619623
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """ LookupModule: test method run """
    # initialize a class instance for test
    lookup_module = LookupModule()

    # prepare the test data
    terms = [
        [
            # a list with three members
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
            },
            {
                'name': 'charly',
            }
        ],
        'authorized'
    ]

    # prepare the expected results

# Generated at 2022-06-13 14:22:49.099065
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from nose.tools import assert_equals, assert_raises
    from ansible.errors import AnsibleError
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.template import Templar


# Generated at 2022-06-13 14:22:49.763223
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert True


# Generated at 2022-06-13 14:23:02.054533
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:23:13.646833
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    try:
        from __main__ import display
    except ImportError:
        from ansible.utils.display import Display
        display = Display()

    lookup_module = LookupModule()


# Generated at 2022-06-13 14:23:19.252096
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Helper function to convert a string to a list of strings
    def to_list(string):
        if not string:
            return []
        return string.split()

    # create LookupModule object
    lookup_module = LookupModule()

    # Set the templar loader (not needed)
    lookup_module._templar = None

    # Create mock input data
    import copy