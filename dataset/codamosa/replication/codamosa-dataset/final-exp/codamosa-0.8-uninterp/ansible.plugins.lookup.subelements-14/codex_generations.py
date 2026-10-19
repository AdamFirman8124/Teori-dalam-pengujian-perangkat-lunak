

# Generated at 2022-06-13 14:13:47.005105
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Test for method run of class LookupModule
    """
    lookup_module = LookupModule()
    terms = [
            [
                { "name": "alice",
                  "authorized": [
                      "/tmp/alice/onekey.pub",
                      "/tmp/alice/twokey.pub"
                  ]
                },
                { "name": "bob",
                  "authorized": [
                      "/tmp/bob/id_rsa.pub"
                  ]
                }
            ],
            'authorized'
        ]
    variables = {}
    ret = lookup_module.run(terms, variables)
    assert(len(ret) == 3)

# Generated at 2022-06-13 14:13:52.857831
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # TODO: unit test runs without errors but doesn't check content
    l = LookupModule()
    l.run([
        [{'name': 'alice', 'authorized': ['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub']}, {'name': 'bob', 'authorized': ['/tmp/bob/id_rsa.pub']}],
        'authorized',
    ], variables={})

# Generated at 2022-06-13 14:14:00.546874
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import string_types
    from ansible import errors
    import json

    subelements = LookupModule()
    assert isinstance(subelements, LookupModule)

    # no terms, should throw errors.AnsibleError
    try:
        subelements.run([{}], None)
        assert False, "no terms, should throw errors.AnsibleError"
    except errors.AnsibleError:
        pass

    # only one term, should throw errors.AnsibleError
    try:
        subelements.run([{}, {}], None)
        assert False, "only one term, should throw errors.AnsibleError"
    except errors.AnsibleError:
        pass

    # wrong type of first term, should throw errors.AnsibleError

# Generated at 2022-06-13 14:14:10.639579
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test for empty dictionary
    lookup = LookupModule()
    assert lookup.run([[{}, "key"], "value"], None) == []

    # Test for empty list
    lookup = LookupModule()
    assert lookup.run([[{'key': {}}, 'value'], "key"], None) == []

    # Test for normal case
    lookup = LookupModule()
    assert lookup.run([[{'key': {'value': [1, 2, 3]}}, 'value'], "key"], None) == [(1,), (2,), (3,)]

    # Test for normal case with skip_missing False
    lookup = LookupModule()

# Generated at 2022-06-13 14:14:21.457973
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def check(terms, ret):
        lookup = LookupModule()
        assert lookup.run(terms, dict()) == ret


# Generated at 2022-06-13 14:14:34.519742
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # create lookup module
    lookup_module = LookupModule()

    # test base functionality
    string = '{"name": "Alice", "address": {"city": "Denver", "state": "CO"}}'
    terms = [string, "address.city"]
    result = lookup_module.run(terms)
    assert result == ["Denver"]

    # test a missing key
    string = '{"name": "Alice", "address": {"city": "Denver", "state": "CO"}}'
    terms = [string, "address.zip"]
    failed = False
    try:
        result = lookup_module.run(terms)
    except AnsibleError:
        failed = True
    assert failed

    # test a missing key with skip_missing set

# Generated at 2022-06-13 14:14:42.718016
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

# Generated at 2022-06-13 14:14:51.072942
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    lookup_class = LookupModule()
    variables = VariableManager()
    loader = DataLoader()

    # test subelements of an array
    return_value = lookup_class.run([1, 2, 3], variables=variables, loader=loader)
    assert return_value == [1, 2, 3]

    # test subelements of a dictionary
    data = { 'k1': {'k2': 'v3'}, 'skipped': 'skipme' }
    return_value = lookup_class.run([data, 'k2'], variables=variables, loader=loader)
    assert return_value == [('v3',)]

    # test subelements of a dictionary with a skipped primary key


# Generated at 2022-06-13 14:15:03.585267
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    import ansible.utils.plugin_docs as plugin_docs

    variable_manager = VariableManager()
    loader = DataLoader()
    
    # basic test:
    variable_manager.set_variable('users', [
      {'name': 'alice', 'authorized': ['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub']},
      {'name': 'bob', 'authorized': ['/tmp/bob/id_rsa.pub']},
    ])
    lookup_module = LookupModule()
    lookup_module._templar = None
    lookup_module._loader = None

# Generated at 2022-06-13 14:15:13.140069
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    inst = LookupModule()

    # test error raised when no terms in input
    terms = []
    variables = []
    try:
        inst.run(terms, variables)
    except AnsibleError as e:
        pass

    # test error raised when length of terms not 2 or 3
    terms = [{}, 'a']
    variables = []
    try:
        inst.run(terms, variables)
    except AnsibleError as e:
        pass

    # test error raised when first term is not a list or a dict
    terms = ['', 'a']
    variables = []
    try:
        inst.run(terms, variables)
    except AnsibleError as e:
        pass

    # test error raised when second term is not a string
    terms = [[], list()]
    variables = []

# Generated at 2022-06-13 14:15:28.940357
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Method run of class LookupModule should return a list
    # It should be [('users', 'alice'), ('users', 'bob')]
    class DummyLookupModule(LookupModule): pass
    users = [{'name': 'alice'}, {'name': 'bob'}]
    terms = [users, 'name']
    lookup = DummyLookupModule()
    results = lookup.run(terms, dict())
    assert results == [('name', 'alice'), ('name', 'bob')]


# Generated at 2022-06-13 14:15:40.735328
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from tempfile import TemporaryDirectory
    from textwrap import dedent
    from ansible.parsing.vault import VaultLib
    from ansible.parsing import vault

    # create test object
    from ansible.plugins.lookup import LookupBase
    lookupModule = LookupBase()

    # create temporary directory for test
    test_directory = TemporaryDirectory()

    # create vault secret file
    test_vault_password_file = test_directory.name + "/vault_secret_test"
    vault_test_password = "vault_test_password"
    vault_test_password_file = open(test_vault_password_file, "w")
    vault_test_password_file.write(vault_test_password)
    vault_test_password_file.close()

    # create vault secret file
   

# Generated at 2022-06-13 14:15:53.388099
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup.subelements import LookupModule
    from ansible.errors import AnsibleError
    from ansible.parsing import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar

    loader = DataLoader()
    variable_manager = VariableManager()
    templar = Templar(loader=loader, variables=variable_manager)


# Generated at 2022-06-13 14:15:59.540044
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # create parser and add 'test' option to it
    parser = argparse.ArgumentParser(description='Test the run method of LookupModule', add_help=False)

    # parse argument and store it in namespace
    args = parser.parse_args()

# start execution of test when this module is run directly
if __name__ == "__main__":
    test_LookupModule_run()

# Generated at 2022-06-13 14:16:01.479903
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # *args, **kwargs
    lookup_module = LookupModule()
    assert hasattr(lookup_module, 'run')
    assert callable(getattr(lookup_module, 'run'))
    assert 'run' in dir(lookup_module)


# Generated at 2022-06-13 14:16:13.238053
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:16:22.886861
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import inspect
    import io
    from ansible.module_utils.six import PY2
    from ansible.module_utils.parsing.convert_bool import boolean

    # load the module so we can use it
    fd, path, desc = imp.find_module('subelements', inspect.getfile(LookupModule))
    LookupModule = imp.load_module('LookupModule', fd, path, desc)

    # create a dummy PlayContext
    play_context = PlayContext()

# Generated at 2022-06-13 14:16:34.868346
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    mylookup = LookupModule()
    terms = [
        [
            {'name': 'alice', 'mysql': {'password': 'mysql-password', 'hosts': ['%', '127.0.0.1', '::1', 'localhost'], 'privs': ['*.*:SELECT', 'DB1.*:ALL']}},
            {'name': 'bob', 'mysql': {'password': 'other-mysql-password', 'hosts': ['db1'], 'privs': ['*.*:SELECT', 'DB2.*:ALL']}}
        ],
        'mysql.hosts',
        {'skip_missing': False}
    ]
    mylookup.run(terms, [], variables={})

# Generated at 2022-06-13 14:16:45.831290
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    # test basic run of lookup-module

# Generated at 2022-06-13 14:16:51.422017
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import ansible.plugins

    # import ansible.plugins.lookup.subelements
    # reload(ansible.plugins.lookup.subelements)

    import ansible.playbook
    import ansible.template
    from ansible.vars.manager import VariableManager

    pm = ansible.plugins.lookup.LookupModule()
    tt = ansible.template.Template(loader=ansible.parsing.dataloader.DataLoader())

    test = []

# Generated at 2022-06-13 14:17:17.239263
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    def my_LookupBase_get_basedir(_self, term):
        return 'None'

    # prepare patch
    LookupBase.get_basedir = my_LookupBase_get_basedir

    # data to be returned by mocked AnsibleFile.open
    class AnsibleFile(object):
        def __init__(self, data):
            self.data = data

        def read(self):
            return self.data

        def __exit__(self, exc_type, exc_value, traceback):
            return False # do not suppress exceptions

        def __enter__(self):
            return self

    class AnsibleModule(object):
        def __init__(self):
            self.params = {}


# Generated at 2022-06-13 14:17:29.669885
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.module_utils.six import PY3
    if PY3:
        long = int  # pylint: disable=redefined-builtin,invalid-name
    from ansible.module_utils.six.moves import zip

    # python2.4 does not have sorted() builtin.
    try:
        sorted
    except NameError:
        from ansible.module_utils.compat.builtins import sorted


# Generated at 2022-06-13 14:17:43.373346
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create the mock object
    lookup = LookupModule()

    # Create the dictionary mock object and specify the return value of lookup.get_basedir(terms)
    mock_loader = dict()
    mock_loader.get_basedir = lambda terms: "."

    # Execute the run method
    result = lookup.run([None, None, None], None, _loader=mock_loader, _templar=None)
    assert result == []

    #Execute the run method with a wrong number of terms and flag provided
    with pytest.raises(AnsibleError):
        result = lookup.run([None, None, None, 'invalid', None], None, _loader=mock_loader, _templar=None)

    # Execute the run method with a wrong flag provided

# Generated at 2022-06-13 14:17:52.173536
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    
    # Initialize class with empty arguments
    terms = []
    variables = None
    
    subelements = LookupModule()
    subelements.run(terms, variables, **kwargs)
    
    # instantiate LookupModule
    from os.path import expanduser
    from sys import path
    path.append(expanduser("~") + "/src/ansible/plugins/lookup")
    
    subelements = LookupModule()
    
    # call run method
    terms = ['mockTerms']
    subelements.run(terms, variables, **kwargs)

# Generated at 2022-06-13 14:18:03.260665
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class TestLookupModule(LookupModule):
        # stub out the templar, to avoid doing templating on the test variables
        def _templar(self, x):
            return x


# Generated at 2022-06-13 14:18:15.590869
# Unit test for method run of class LookupModule
def test_LookupModule_run():
  from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleSequence
  from ansible.parsing.yaml.dumper import AnsibleDumper

  def normalize(data, follow_aliases=True, dumper=AnsibleDumper):
    data = data if follow_aliases else copy.deepcopy(data)
    if isinstance(data, (AnsibleMapping, dict)):
      for key in data.keys():
        data[key] = normalize(data[key], dumper=dumper)
      return dumper.represent_dict(data)
    elif isinstance(data, (AnsibleSequence, list)):
      return dumper.represent_list(list(map(lambda i: normalize(i, dumper=dumper), data)))
    return data

 

# Generated at 2022-06-13 14:18:21.360795
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = AnsibleModule(argument_spec={})
    lookup_obj = LookupModule()
    res = lookup_obj.run([{'a.b': 2}, 'a.b'], module.params, **module.kwargs)
    assert res[0] == [({'a': {'b': 2}}, 2)]
    res = lookup_obj.run([{'a.b': 2, 'a.c': 3}, 'a.b'], module.params, **module.kwargs)
    assert res[0] == [({'a': {'b': 2, 'c': 3}}, 2)]
    res = lookup_obj.run([{'a': {'b': {'c': {'d': 4}}}}, 'a.b.c.d'], module.params, **module.kwargs)
    assert res

# Generated at 2022-06-13 14:18:27.246697
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Check if ansible.errors.AnsibleError when raised in LookupModule.run is handled correctly
    """
    from ansible.errors import AnsibleError
    from ansible.plugins.lookup import LookupModule
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.utils.listify import listify_lookup_plugin_terms
    from ansible.template import Templar

    variables = {}
    lookup = LookupModule()
    list_of_hashes = [
        {'name': 'alice', 'authorized': ['/tmp/alice/onekey.pub'], 'groups': ['wheel']},
        {'name': 'bob', 'authorized': ['/tmp/bob/id_rsa.pub'], 'groups': ['sudo']}
    ]
   

# Generated at 2022-06-13 14:18:29.909088
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # first test presence of method run
    lo = LookupModule()
    assert 'run' in dir(lo)



# Generated at 2022-06-13 14:18:41.305089
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # init LookupModule
    lm = LookupModule()

    # prepare LookupModule vars
    terms = [{'test.test_dict': {'test_list': [1, 2, 3], 'test_string': 'example'}}]
    terms = lm.run(terms=terms, variables='test_variables')[0]
    assert terms == [({'test_dict': {'test_list': [1, 2, 3], 'test_string': 'example'}}, 1), ({'test_dict': {'test_list': [1, 2, 3], 'test_string': 'example'}}, 2), ({'test_dict': {'test_list': [1, 2, 3], 'test_string': 'example'}}, 3)]

# Generated at 2022-06-13 14:19:14.465822
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ('foo.bar', 'baz', {'skip_missing': True})
    lookup = LookupModule()
    result = lookup.run(terms, None)
    assert result == []

    #TODO: more tests

# Generated at 2022-06-13 14:19:26.315461
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    def run(input, terms, **flags):
        input = eval(input)
        return LookupModule().run(terms, None, **flags)(input)

    # make sure we handle missing subelement errors correctly
    result = run("{'foo': 'bar'}", ["{{ q('subelements', foo, 'bar') }}", True])
    assert result == []

    # we should get the subelement if it's the only one
    result = run("[{'foo': {'bar': 'baz'}}]", ["{{ q('subelements', foo, 'bar') }}", True])
    assert result == [('bar', 'baz')]

    # we should get the subelement if it's the only one

# Generated at 2022-06-13 14:19:34.332402
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Source of test data: test/integration/targets/lookup_plugins/subelements.yml
    lookup_module = LookupModule()
    # default test
    test_data = "[{'name': 'alice', 'authorized': ['/tmp/alice/onekey.pub', '/tmp/alice/twokey.pub']}, {'name': 'bob', 'authorized': ['/tmp/bob/id_rsa.pub']}, {'skip': True}]"

# Generated at 2022-06-13 14:19:47.208811
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible.module_utils.six import iteritems
    from ansible.errors import AnsibleError

    from ansible.plugins.lookup.subelements import LookupModule
    lookup_plugin = LookupModule()

    # get vars for method run
    terms = []
    if '_terms' in globals():
        terms = _terms
    variables = {}
    if '_variables' in globals():
        variables = _variables

    # get expected results
    expected = []
    if '_result' in globals():
        expected = _result

    # run method
    result = lookup_plugin.run(terms, variables, **kwargs)

    # compare results

# Generated at 2022-06-13 14:19:58.328141
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    def fake_run(terms, variables=None, **kwargs):
        return LookupModule().run(terms, variables, **kwargs)

    # test required terms check
    terms = [
        None,  # missing
        None,  # missing
    ]
    try:
        fake_run(terms)
        assert False
    except AnsibleError as e:
        assert str(e) == "subelements lookup expects a list of two or three items"

    terms = [
        [],  # empty
        [],  # missing
    ]
    try:
        fake_run(terms)
        assert False
    except AnsibleError as e:
        assert str(e) == "subelements lookup expects a list of two or three items"


# Generated at 2022-06-13 14:20:08.300928
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Basic tests to ensure syntax and some basics work as intended
    # These are not full unittests, just basic tests to detect errors
    # Ensure that syntax is OK
    assert LookupModule().run([[{'key1': 1, 'key2': 'test'}, {'key1': 2}], 'key1'], {}, skip_missing=False) == [(1,), (2,)]
    assert LookupModule().run([[{'key1': {'subkey1': 1}, 'key2': 'test'}, {'key1': 2}], 'key1.subkey1'], {}, skip_missing=False) == [(1,)]

# Generated at 2022-06-13 14:20:17.422363
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import unittest
    import ansible.utils.listify
    from ansible.plugins.lookup import LookupBase
    from ansible import errors

    lookup_module = LookupModule()

    class TestImplLookupBase(LookupBase):
        def run(self, terms, variables=None, **kwargs):
            return terms

    lookup_module._templar = TestImplLookupBase()
    lookup_module._loader = TestImplLookupBase()

    # check lookup terms - check number of terms
    with unittest.TestCase("Test wrong number of terms"):
        with self.assertRaises(errors.AnsibleError):
            lookup_module.run("abcde")

# Generated at 2022-06-13 14:20:29.746019
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    nbr_of_tests = 0
    nbr_of_tests += 1
    l = LookupModule()
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
    res = l.run([users, 'authorized'], {})
    assert len(res) == 3
    assert res[0] == (users[0], '/tmp/alice/onekey.pub')
    assert res[1] == (users[0], '/tmp/alice/twokey.pub')

# Generated at 2022-06-13 14:20:38.521038
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # Test 1: An empty terms list gives an empty list as result
    terms = []
    res = lookup.run(terms, {})
    assert res == []

    # Test 2: Two terms provide
    #         - First term: list of dictionaries
    #         - Second term: dictionary key
    #       A nested list of lists is returned containing pairs of
    #       dictionary/value
    terms = [
        [
            {"key1": {"key2": [1, 2, 3]}},
            {"key1": {"key2": ["a", "b", "c"]}},
            {"key1": {"key2": ["x", "y", "z"]}}
        ],
        "key1.key2"
    ]
    res = lookup.run(terms, {})

# Generated at 2022-06-13 14:20:51.007666
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_instance = LookupModule()

    # get _terms (terms)
    terms = [
        {"ssh_key": {"file": "id_rsa.pub", "user": "root"}},
        "file",
        {}
    ]
    # call method run
    test_result = lookup_instance.run(terms, None)
    # simple test
    #assert test_result == [("ssh_key", "id_rsa.pub")]
    # extended test for some more coverage - compare by comparing the length of the result lists
    assert len(test_result) == len([("ssh_key", "id_rsa.pub")])

    # get _terms (terms)

# Generated at 2022-06-13 14:22:03.730390
# Unit test for method run of class LookupModule
def test_LookupModule_run():
  from ansible.module_utils.six import assertRegex
  from ansible.module_utils.six import PY3
  import re

  # Invoke the run method, expecting a list of tuples on return.
  lookup = LookupModule()
  users = [{'a':'b','c':{'d':'e','f':'g'}}]
  result = lookup.run([users,'c.d'],[])
  assert isinstance(result,list) and isinstance(result[0],tuple) and len(result) == 1 and result[0][1] == 'e'

  # Invoke the run method, expecting a list of tuples on return.
  lookup = LookupModule()
  users = [{'a':'b','c':{'d':'e','f':'g'}}]
  result

# Generated at 2022-06-13 14:22:11.146242
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    # check normal behaviour of run method

# Generated at 2022-06-13 14:22:23.985196
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.template import Templar

    setattr(Templar, 'is_template', lambda self: False)

    # Create a temporary file to be used as source of YAML data
    import tempfile
    fd, path = tempfile.mkstemp()

# Generated at 2022-06-13 14:22:36.512014
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import pytest
    from ansible.module_utils.six import string_types

    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.module_utils.parsing.convert_bool import BOOLEANS_TRUE, BOOLEANS_FALSE
    from ansible.plugins.lookup import LookupBase
    from ansible.utils.listify import listify_lookup_plugin_terms


# Generated at 2022-06-13 14:22:49.737026
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.plugins.loader as plugins
    import ansible.parsing.dataloader
    import ansible.vars.manager
    import ansible.template.template as template
    import os


# Generated at 2022-06-13 14:23:02.054134
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test basic run
    testterms = [
        [{'name': 'alice', 'mysql': {'password': 'mysql-password', 'privs': ['*.*:SELECT', 'DB1.*:ALL'], 'hosts': ['%', '127.0.0.1', '::1', 'localhost']}},
         {'name': 'bob', 'mysql': {'password': 'other-mysql-password', 'privs': ['*.*:SELECT', 'DB2.*:ALL'], 'hosts': ['db1']}}],
        'mysql.hosts']
    testvariables = {}
    lookup_plug = LookupModule()
    result = lookup_plug.run(testterms, testvariables)

# Generated at 2022-06-13 14:23:13.644054
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Set up the sample test data
    lookup = LookupModule()

# Generated at 2022-06-13 14:23:14.676745
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert False, "TODO"

# Generated at 2022-06-13 14:23:26.959375
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import inspect
    import sys

    class LookupModule_test(object):

        def __init__(self):
            self.variable_manager = None
            self.loader = None
            self.inventory = None
            self.variable_manager = None
            self.passwords = None

    lookup_test = LookupModule_test()
    lookup_test.loader = sys.modules[__name__].__dict__.get('_load_fixtures')()
    lookup_test.inventory = lookup_test.loader.get_inventory(loader=lookup_test.loader)

    test_class_methods = inspect.getmembers(LookupModule_test, inspect.ismethod)
    for method_name, method in test_class_methods:
        if method_name.startswith('_test_'):
            method()


