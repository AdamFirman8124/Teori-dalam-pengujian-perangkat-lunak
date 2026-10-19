

# Generated at 2022-06-13 14:13:41.475142
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from mock import Mock, sentinel
    lu = LookupModule()
    lu.set_options({})
    lu._templar = Mock()
    lu._loader = Mock()
    iterable = ["/foo/bar", sentinel.other]
    result = lu.run([iterable, "groups",
                     {"skip_missing": False}], None)
    assert result == iterable


# Generated at 2022-06-13 14:13:50.085419
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()

    # not a list
    assert l.run(
        {
            'users': [
                {
                    'name': 'Alice',
                    'authorized': ['/tmp/Alice/onekey.pub', '/tmp/Alice/twokey.pub']
                },
                {
                    'name': 'Bob',
                    'authorized': ['/tmp/Bob/id_rsa.pub']
                }
            ]
        },
        None
    ) == [], "run return value of 'not a list' test changed"

    # missing subkey

# Generated at 2022-06-13 14:13:57.294344
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import mock
    module_name = 'sub_element'
    options = mock.MagicMock()
    templar = mock.MagicMock()
    loader = mock.MagicMock()

    terms = mock.MagicMock()
    terms.__len__.return_value = 2
    terms.__getitem__.side_effect = lambda x: [{
        "name": "test_user",
        "authorized": [{"abc": "def"}, {"123": "456"}],
        "a": {"b": {"c": {"d": ["e", "f", "g"]}}}
    }, "a.b.c.d"]

    lookup = LookupModule()
    ret = lookup.run(terms, {}, templar=templar, loader=loader)

# Generated at 2022-06-13 14:13:58.426648
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert False, "Missing unit tests for LookupModule.run()"

# Generated at 2022-06-13 14:14:06.708846
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import copy
    from ansible.plugins.loader import lookup_loader
    from ansible.module_utils.six import PY3

    if not PY3:
        from ansible.constants import DEFAULT_VAULT_IDENTITY_LIST
    else:
        from ansible.parsing.vault import DEFAULT_VAULT_IDENTITY_LIST

    # set defaults for module arguments
    validate_certs = True

    # set defaults for module parameters
    new_vault_password = 'p@ssw0rd'
    vault_identity = 'test@example.com'
    vault_password_file = '/tmp/vault_password.txt'
    ask_vault_pass = False
    vault_identity_list = DEFAULT_VAULT_IDENTITY_LIST
    vault_password = None

    # setup the

# Generated at 2022-06-13 14:14:18.753482
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

# Generated at 2022-06-13 14:14:28.414266
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()

    # convert dict to list test
    module.run(terms=['{{ myvar }}', 'subkey'], variables={'myvar': {'key1': 'val1', 'key2': 'val2'}})

    # with skippping
    module.run(terms=['{{ myvar }}', 'subkey', {'skip_missing': False}], variables={'myvar': [{'subkey': 'val1'}, {'key2': 'val2'}]})

    # no list, nested key test
    module.run(terms=['{{ myvar }}', 'subkey.subsubkey'], variables={'myvar': [{'subkey': {'subsubkey': 'val1'}}, {'subkey': {'subsubkey': 'val2'}}]})

    #

# Generated at 2022-06-13 14:14:36.062704
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    import textwrap


# Generated at 2022-06-13 14:14:46.877655
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    terms = [
        [
            {
                'primary': {
                    'order': [
                        "a",
                        "b"
                    ]
                },
                'secondary': {
                    'order': [
                        "c"
                    ]
                }
            },
            {
                'primary': {
                    'order': [
                        "d"
                    ]
                },
                'secondary': {
                    'order': [
                        "e"
                    ]
                }
            }
        ],
        "primary.order"
    ]

# Generated at 2022-06-13 14:14:59.241690
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    l = LookupModule()
    l.set_options({})
    with pytest.raises(AnsibleError):
        l.run([''], '')
    with pytest.raises(AnsibleError):
        l.run(['x'], '')
    with pytest.raises(AnsibleError):
        l.run(['x', 'y', 'z'], '')
    assert l.run([123], '') == []
    assert l.run(['x', 'y'], '') == []
    assert l.run([{}, 'y'], '') == []
    assert l.run([{'x': 'y'}, 'x'], '') == ['y']

# Generated at 2022-06-13 14:15:15.305122
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_mod = LookupModule()
    assert lookup_mod.run([[{"one": 1, "two": [2, 3], "four": {"five": 5}}], "two"], []) == [({"one": 1, "two": [2, 3], "four": {"five": 5}}, 2), ({"one": 1, "two": [2, 3], "four": {"five": 5}}, 3)]
    lookup_mod = LookupModule()
    assert lookup_mod.run([[{"one": 1, "two": [2, 3], "four": {"five": 5}}], "four.five"], []) == [({"one": 1, "two": [2, 3], "four": {"five": 5}}, 5)]
    lookup_mod = LookupModule()

# Generated at 2022-06-13 14:15:26.936129
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lu = LookupModule()
    
    # test input
    terms1 = [
        [
            {
                "webservers": {
                    "hosts": [
                        "web1",
                        "web2",
                        "web3"
                    ]
                },
                "dbservers": {
                    "hosts": [
                        "db1",
                        "db2",
                        "db3"
                    ]
                },
                "badsubkey": {
                    "subkey": "not a list"
                }
            },
            "hosts"
        ]
    ]
    
    # expected output

# Generated at 2022-06-13 14:15:39.279087
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    def setup_module(module):
        module.lookup_plugin = LookupModule()
        module.lookup_plugin._templar = DummyTemplar()
        module.lookup_plugin._loader = DummyLoader()

    class DummyTemplar(object):
        def __init__(self):
            pass

        def template(self, value):
            return value

    class DummyLoader(object):
        def __init__(self):
            pass


# Generated at 2022-06-13 14:15:52.189447
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lu = LookupModule()
    users = [
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
    ]
    # List of tuples,
    # the first item is a list of items to look for subelements
    # the second item is the key to extract
    # the optional third item is a dict containing flags

# Generated at 2022-06-13 14:15:59.453395
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    L = LookupModule()
    L._templar = None
    L._loader = None

    def test(terms, variables, result):
        return (L.run(terms, variables)[0] == result)

    terms = [
        {'skipped': False, 'has': 'no', 'useful': 'data'},
        ['skipped', 'has', 'useful'],
        {'skip_missing': False}]
    test(terms, None, ['skipped', 'has', 'useful'])

    terms = [
        {'skipped': False, 'has': 'no', 'useful': 'data'},
        ['skipped', 'has', 'useful'],
        {'skip_missing': True}]
    test(terms, None, ['skipped', 'has'])

# Generated at 2022-06-13 14:16:06.944367
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.loader import AnsibleLoader
    import yaml

# Generated at 2022-06-13 14:16:16.710794
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.compat.tests.mock import patch
    import ansible.module_utils.parsing.convert_bool
    isBoolean = ansible.module_utils.parsing.convert_bool.boolean

# Generated at 2022-06-13 14:16:25.468780
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Arguments of method
    terms = [{'a': [{'b': ['b0', 'b1']}]}, 'a.0.b', {'skip_missing': True}]
    variables = {}

    # Create an object of type LookupModule
    lookup_plugin = LookupModule()

    expected_value = [(
        {'a': [{'b': ['b0', 'b1']}]},
        'b0'
    ),
    (
        {'a': [{'b': ['b0', 'b1']}]},
        'b1'
    )]

    # Call method run of LookupModule
    value = lookup_plugin.run(terms, variables)

    assert type(value) == list
    assert len(value) == len(expected_value)

# Generated at 2022-06-13 14:16:36.901202
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    result = lookup_module.run(['var'], dict(
        var=[dict(name='alice', authorized=['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub']),
             dict(name='bob', authorized=['/tmp/bob/id_rsa.pub'])]
    ))
    assert result == [('alice', '/tmp/alice/onekey.pub'), ('alice', '/tmp/alice/twokey.pub'), ('bob', '/tmp/bob/id_rsa.pub')]


# Generated at 2022-06-13 14:16:46.783845
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # unit tests need access to protected attributes and methods
    # pylint: disable=protected-access

    # ---
    # subelements lookup, first example:
    #
    # create a dummy AnsibleVars containing the needed users list
    from ansible.vars import AnsibleVars
    from ansible.vars import combine_vars
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager

# Generated at 2022-06-13 14:17:11.547666
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    fake_loader = DictDataLoader({})


# Generated at 2022-06-13 14:17:13.536989
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    assert lookup._templar is not None
    # lookup.run()

# Generated at 2022-06-13 14:17:24.945284
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest

    # case - terms is either a list or a tuple of valid length
    assert isinstance(LookupModule.run(None, ('',), None, None), list)
    assert isinstance(LookupModule.run(None, ('', '',), None, None), list)
    assert isinstance(LookupModule.run(None, ('', '', {}), None, None), list)
    assert isinstance(LookupModule.run(None, [[]], None, None), list)
    assert isinstance(LookupModule.run(None, [[], ''], None, None), list)
    assert isinstance(LookupModule.run(None, [[], '', {}], None, None), list)
    assert isinstance(LookupModule.run(None, [{}], None, None), list)

# Generated at 2022-06-13 14:17:34.438699
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = [
        [
            {'name':'alice', 'authorized':['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub']},
            {'name':'bob', 'authorized':['/tmp/bob/id_rsa.pub']},
            {'name':'carol', 'authorized':['/tmp/carol/rsa.pub', '/tmp/carol/ed25519.pub']},
            {'name':'dave', 'authorized':'/tmp/dave/private.key'},
        ],
        'authorized',
    ]

    flags = {}

    elementlist = terms[0]
    subelements = terms[1].split(".")

    # build_items
    ret = []
    for item0 in elementlist:
        subvalue = item

# Generated at 2022-06-13 14:17:46.762236
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    def _assert_error(terms, error_msg):
        try:
            LookupModule().run(terms=terms, variables={})
            assert False, "AnsibleError expected"
        except AnsibleError as exception:
            assert error_msg in to_native(exception)

    # test input

# Generated at 2022-06-13 14:17:57.245685
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    def set_vars(terms, variables, **kwargs):
        lookup_module._templar = kwargs['templar']
        lookup_module._loader = kwargs['loader']

    def return_vars(*args):
        return args[1][0]

    # test non-existing 'users' key
    out = return_vars(*lookup_module.run([['users', 'missingmysql.hosts'], 'mysql.hosts', {'skip_missing': False }], True, set_vars=set_vars, templar=return_vars, loader=return_vars))
    assert(isinstance(out, list) and len(out) == 0)

    # test empty list

# Generated at 2022-06-13 14:18:09.227712
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Check returned values
    values = [
        {'name': 'alice', 'authorized': ['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub'], 'groups': ['wheel'], 'mysql': {'password': 'mysql-password', 'privs': ['*.*:SELECT', 'DB1.*:ALL'], 'hosts': ['%', '127.0.0.1', '::1', 'localhost']}},
        {'name': 'bob', 'authorized': ['/tmp/bob/id_rsa.pub'], 'mysql': {'password': 'other-mysql-password', 'privs': ['*.*:SELECT', 'DB2.*:ALL'], 'hosts': ['db1']}},
    ]

    # Expected values

# Generated at 2022-06-13 14:18:20.118338
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    import sys
    import shutil
    import tempfile
    import unittest

    ##########################################################################################################
    # Test method run() of class LookupModule
    ##########################################################################################################

    class TestLookupModule__run(unittest.TestCase):

        @classmethod
        def setUpClass(cls):
            cls.tmpdir = tempfile.mkdtemp()
            cls.test_dir = os.path.join(cls.tmpdir, 'testdir')

            cls.set_dir = os.path.join(cls.test_dir, 'setdir')
            cls.set_dir_targz = cls.set_dir + ".tar.gz"

# Generated at 2022-06-13 14:18:30.315487
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    class Options:
        def __init__(self, verbosity=0, connection=None, module_path=None, forks=None, become=None,
                     become_method=None, become_user=None, check=False, diff=False):
            self.verbosity = verbosity
            self.connection = connection
            self.remote_user = os.getenv('USER')
            self.module_path = module_path
            self.forks = forks
            self.become = become
            self.become_method = become_method
            self.become_user = become_user
            self.check = check
            self.diff = diff

        def __getattr__(self, name):
            return None

        def __getstate__(self):
            return None

        def __setstate__(self, d):
            pass

# Generated at 2022-06-13 14:18:41.638400
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import textwrap
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.plugins.lookup.subelements import LookupModule

    # for comparing with AnsibleMapping which does not care about order
    def ordered(obj):
        if isinstance(obj, dict):
            return sorted((k, ordered(v)) for k, v in obj.items())
        if isinstance(obj, list):
            return sorted(ordered(x) for x in obj)
        else:
            return obj


# Generated at 2022-06-13 14:19:23.460589
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import ansible
    from ansible.plugins.lookup.subelements import LookupModule

    # set up needed objects
    yaml = ansible.plugins.loader.get_loader('yaml')
    templar = ansible.template.Templar(loader=ansible.plugins.loader.loader)

    # set up needed vars
    variable_manager = ansible.vars.VariableManager()

# Generated at 2022-06-13 14:19:32.704786
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    def _assert_subelements(term, result, error=None):
        if error is None:
            assert result in term
        else:
            with pytest.raises(AnsibleError) as e_info:
                term.run()
            assert error in str(e_info.value)

    def _assert_subelements_tuple(term, result, error=None):
        if error is None:
            assert tuple(result) in term
        else:
            with pytest.raises(AnsibleError) as e_info:
                term.run()
            assert error in str(e_info.value)

    def _assert_subelements_list(term, result, error=None):
        if error is None:
            assert result in term

# Generated at 2022-06-13 14:19:46.024079
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # call function run with empty first parameter:
    try:
        lookup.run([], {})
    except AnsibleError as e:
        assert e.args[0] == "subelements lookup expects a list of two or three items, "
    except:
        assert False

    # call function run with string as first parameter:
    try:
        lookup.run(["a string"], {})
    except AnsibleError as e:
        assert e.args[0] == "subelements lookup expects a list of two or three items, first a dict or a list, second a string pointing to the subkey"
    except:
        assert False

    # call function run with integer as first parameter:
    try:
        lookup.run([1], {})
    except AnsibleError as e:
        assert e.args

# Generated at 2022-06-13 14:19:54.344446
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    This method tests if the method run of the class LookupModule behaves correctly.
    """
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    from ansible.utils import plugin_docs

    # Create the inventory, play and variable_manager objects
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list='tests/units/plugins/inventory/inventory_file')
    variable_manager.set_inventory(inventory)

# Generated at 2022-06-13 14:20:05.272906
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    def create_LookupModule(elementlist):
        class OptionsModule(object):
            def __init__(self, var1=None):
                self.var1 = var1

        class RunnerModule(object):
            def __init__(self, module_name=None, module_args=None, module_vars=None):
                self.module_name = module_name
                self.module_args = module_args
                self.module_vars = module_vars

        class RunnerModule(object):
            def __init__(self, module_name=None, module_args=None, module_vars=None):
                self.module_name = module_name
                self.module_args = module_args
                self.module_vars = module_vars


# Generated at 2022-06-13 14:20:15.922983
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:20:27.831994
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # setup
    from ansible.module_utils._text import to_text

    terms = [
        [
            { 'user': 'Alice',
              'access_key': { 'id': '1234', 'secret': '5678' }
            },
            { 'user': 'Bob',
              'access_key': { 'id': '4321', 'secret': '8765' }
            }
        ],
        "access_key.id"
    ]
    lookup_plugin = LookupModule()

    # execute
    result = lookup_plugin.run(terms, {}, **dict())

    assert len(result) == 2
    assert result[0][0]['user'] == 'Alice'
    assert to_text(result[0][1]) == '1234'

    # check that optional third item must be a dict with flags

# Generated at 2022-06-13 14:20:36.464497
# Unit test for method run of class LookupModule
def test_LookupModule_run():  # noqa, pylint: disable=too-many-locals,too-many-branches,too-many-statements
    from ansible.context import CLIContext
    from ansible.utils.display import Display
    from ansible.template import Templar
    import pytest
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager

    class IsolatedCLIContext(CLIContext):
        '''
        Helps to run the test in isolation
        '''
        def __init__(self, args=None, stdin_loader=None, stdout_display=None, **kwargs):
            if stdin_loader is None:
                stdin_loader = DataLoader()

# Generated at 2022-06-13 14:20:48.372766
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()


# Generated at 2022-06-13 14:20:59.088469
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import ansible.plugins.lookup.subelements as subelements
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.utils.listify import listify_lookup_plugin_terms

    class TestLookupModule(sublement.LookupModule):
        def __init__(self):
            subelement.LookupModule.__init__(self)
            self._templar = None
            self._loader = None

    lookup = TestLookupModule()

    # no test yet (coverage looks good though)
    # TODO: add test

    # test AnsibleError raised

# Generated at 2022-06-13 14:22:11.172684
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    #create LookupModule class instance
    LookupModule_instance = LookupModule()

    # create test variables
    variable_manager = {}
    variable_manager['names'] = {'dave': {'foos': ['a', 'b', 'c']}}
    variable_manager['names2'] = ['dave', {'foos': ['a', 'b', 'c']}]
    variable_manager['names3'] = 'dave'
    variable_manager['names4'] = {'dave': {'foos': 'barg'}}

    # create test terms

# Generated at 2022-06-13 14:22:24.023742
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # setup a few fake arguments
    class Arguments:
        def __init__(self, term_list, variable_dict, **kwargs):
            self.terms = term_list
            self.variables = variable_dict
            self.kwargs = kwargs

    class ArgumentDict:
        def __init__(self, dict_list):
            self.dict_list = dict_list

        def get(self, key, value=None):
            # all tests set value to None
            return self.dict_list[key]

    class Variables:
        def __init__(self, dict_list):
            if dict_list is not None:
                self.dict_list = dict_list
            else:
                self.dict_list = {}

        def __getitem__(self, key):
            return self.dict_

# Generated at 2022-06-13 14:22:36.551869
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory

    class Args:
        connection = None
        module_path = None
        passwords = None
        remote_user = None
        private_key_file = None
        sudo = False
        sudo_user = None
        ask_sudo_pass = False
        verbosity = None
        syntax = None
        check = False
        diff = False
        listhosts = None
        subset = None
        extra_vars = None

    loader = DataLoader()
    inventory = Inventory(loader=loader)
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    loader.set_basedir('tests/loader_tests/collection/')
    options = Args()
    look

# Generated at 2022-06-13 14:22:49.785331
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    class MockLookupModule(object):
        def __init__(self, templar):
            self.templar = templar

    lookup_module = LookupModule(MockLookupModule(None))

    # Test case 1: no terms
    result = lookup_module.run([], {})
    assert result == []

    # Test case 2: terms is not a list
    result = lookup_module.run("test", {})
    assert result == []

    # Test case 3: first term is not a dict
    result = lookup_module.run([1], {})
    assert result == []

    # Test case 4: first term is a dict but no second term
    result = lookup_module.run([{'key': 'value'}], {})
    assert result == []

    # Test case 5: first term is a dict

# Generated at 2022-06-13 14:23:02.117526
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    # Empty terms
    res = lookup_module.run([], {})
    assert res == [], \
        "Expect empty result when term is of type list but empty."

    # Single term
    res = lookup_module.run(["abc"], {})
    assert res == [], \
        "Expect empty result when term is a list that contains only a string."

    # Wrong type of term
    res = lookup_module.run(["abc", "def", "ghi"], {})
    assert res == [], \
        "Expect empty result when term is of type list but wrong values."

    # Right case - 2 first elements
    res = lookup_module.run([[[{'name': 'foo', 'bar': 'boo'}]], "bar"], {})

# Generated at 2022-06-13 14:23:13.696660
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # tests the LookupModule class and its run method, the example from the documentation is executed
    import os
    from ansible.errors import AnsibleError
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.six import string_types
    from ansible.plugins.lookup import LookupBase
    from ansible.module_utils.parsing.convert_bool import boolean

    # setup test
    lm = LookupModule()  # instantiate the LookupModule class
    lm.set_options({})  # set options

    # setup the users variable
    path = os.path.dirname(os.path.realpath(__file__))

# Generated at 2022-06-13 14:23:25.889123
# Unit test for method run of class LookupModule