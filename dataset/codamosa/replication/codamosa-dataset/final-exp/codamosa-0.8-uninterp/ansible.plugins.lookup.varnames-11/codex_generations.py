

# Generated at 2022-06-13 14:45:07.560979
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup import LookupBase
    from ansible.errors import AnsibleError
    from ansible.module_utils._text import to_native
    from ansible.module_utils.six import string_types

    class TestClass(LookupBase):

        def run(self, terms, variables=None, **kwargs):
            return terms

    lookup_module = TestClass()

    terms = ["qz_.*"]
    varName = "qz_hello"
    variables = { varName : "hello"}
    assert lookup_module.run(terms, variables, direct={}) == terms

    terms = ["qz_.*"]
    variables = { varName : "hello"}
    assert lookup_module.run(terms, variables, direct={}) == terms

    terms = ["qz_.*"]
    variables = {}


# Generated at 2022-06-13 14:45:18.150043
# Unit test for method run of class LookupModule
def test_LookupModule_run():
   # mock data
   terms = [
      # regex, expected result
      ('^qz_.+', ['qz_1', 'qz_2']),
      ('.*', ['qz_1', 'qz_2', 'qa_1', 'qz_']),
      ('hosts', []),
      ('.+_zone$', []),
      ('.+_location$', []),
   ]
   variables = {
      'qz_1': 'hello',
      'qz_2': 'world',
      'qa_1': "I won't show",
      'qz_': "I won't show either",
   }

   # test
   for term, expected_result in terms:
      result = LookupModule().run(
         terms=[term],
         variables=variables
      )
     

# Generated at 2022-06-13 14:45:30.229632
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.vars import combine_vars

    lookup_instance = LookupModule()

    var_options = combine_vars(loader=None, variables={
        'qz_1': 'hello',
        'qa_1': 'world',
        'qz_2': 'world',
        'qz_3': 'world',
    })

    # Test using a simple pattern
    lookup_instance.set_options(var_options=var_options, direct={})
    assert lookup_instance.run(['^qz_.+']) == ['qz_1', 'qz_2', 'qz_3']

    # Test using a pattern that won't match nothing
    lookup_instance.set_options(var_options=var_options, direct={})

# Generated at 2022-06-13 14:45:35.664987
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['^qz_.+','^qa_.+']
    variables = {'qz_1':'hello', 'qz_2':'world', 'qa_1':"won't show", 'qz_':"won't show either"}
    expected_result = ['qz_1', 'qz_2']
    assert LookupModule().run(terms, variables) == expected_result

# Generated at 2022-06-13 14:45:45.560600
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import json
    import os
    import sys
    import tempfile
    # Set up the needed variables
    testfile = tempfile.NamedTemporaryFile()
    testfile_path = testfile.name
    testfile_name = os.path.basename(testfile_path)
    data_dict = {"test1": "test1", "test2": "test2", "test_x": "xxx"}
    test_args = json.dumps(data_dict)
    test_kwargs = json.dumps({})
    # Run the test

# Generated at 2022-06-13 14:45:56.106459
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['^qz_.+', '^qz_.+']
    variables = {'qz_1': 'hello', 'qz_2': 'world'}
    kwargs = {'var_lookup': True}
    expected_ret = ['qz_1', 'qz_2']
    lookup_module = LookupModule()
    ret = lookup_module.run(terms, variables, **kwargs)
    assert ret == expected_ret

    terms = ['^qz_.+']
    variables = {'qz_1': 'hello', 'qz_2': 'world', 'qa_1': "I won't show", 'qz_': "I won't show either"}
    kwargs = {'var_lookup': True}

# Generated at 2022-06-13 14:46:06.268763
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    variables = dict()
    variables['a_abc'] = 'abc'
    variables['b_abc'] = 'abc'
    variables['a_var'] = 'abc'
    variables['b_var'] = 'abc'
    variables['c_var'] = 'abc'

    ret = lookup.run(['a_'], variables=variables)
    assert (ret == ['a_abc', 'a_var']), "Test failed"
    ret = lookup.run(['b_'], variables=variables)
    assert (ret == ['b_abc', 'b_var']), "Test failed"
    ret = lookup.run(['c_'], variables=variables)
    assert (ret == ['c_var']), "Test failed"

# Generated at 2022-06-13 14:46:06.766125
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 14:46:17.290203
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    This unit test will test the method run of class LookupModule.
    """
    lookup_module = LookupModule()
    terms = ["^qz_.+", "^qz_.+", ".+", "hosts", ".+_zone$", ".+_location$"]
    variables = {"qz_1": "hello", "qz_2": "world", "qa_1": "I won't show", "qz_": "I won't show either", "hosts": "I will show", "host_zone1": "I will show", "host_location2": "I will show"}
    ret = lookup_module.run(terms, variables)

# Generated at 2022-06-13 14:46:25.047484
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Test run method of LookupModule
    """
    from ansible.plugins.lookup import LookupModule
    from ansible.module_utils._text import to_native

    module = LookupModule()

    # check for empty variables
    try:
        module.run(terms=['test'], variables=None)
    except AnsibleError as exception:
        assert exception.args[0] == 'No variables available to search'

    # check for invalid variables
    try:
        module.run(terms=['test'], variables={'test': 'test'})
    except AnsibleError as exception:
        assert exception.args[0] == "Invalid setting identifier, \"test\" is not a string, it is a <type 'str'>"

    # check for invalid terms

# Generated at 2022-06-13 14:46:36.034339
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    terms = [ '^qz_.+' ]
    variables = { "qa_1": "hello", "qz_1": "hi", "qz_2": "yo" }

    ret = lookup_module.run(terms, variables)
    assert 2 == len(ret)
    assert 'qz_1' in ret
    assert 'qz_2' in ret

    terms = [ '^qz_.+', '^qa_.+' ]
    variables = { "qa_1": "hello", "qz_1": "hi", "qz_2": "yo" }

    ret = lookup_module.run(terms, variables)
    assert 3 == len(ret)
    assert 'qa_1' in ret
    assert 'qz_1' in ret

# Generated at 2022-06-13 14:46:44.525790
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    # first run with no variables
    with pytest.raises(AnsibleError) as e:
        lookup_module.run(['abc'])

    assert "No variables available to search" in str(e)

    # test with variables
    lookup_module._templar = FakeTemplar()
    lookup_module._templar._available_variables = {"a": "b", "c": "d", "e": "f"}
    assert lookup_module.run(['e']) == ['e']

    # test with a bad regex
    lookup_module._templar._available_variables = {"a": "b", "c": "d", "e": "f"}

# Generated at 2022-06-13 14:46:50.086082
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    
    lookup = LookupModule()
    # Variable names with and without an underscore
    variables = {"_ENV_MY_PREFIX": "Hello",
                 "_ENV_MY_SUFFIX": "World!",
                 "ENV_MY_PREFIX": "Hello",
                 "ENV_MY_SUFFIX": "World!"}

    # Test with one regex, find only variable names with an underscore.
    terms = ['_ENV_MY_.+']
    results = lookup.run(terms, variables, 1)
    assert results == ['_ENV_MY_PREFIX', '_ENV_MY_SUFFIX']

    # Test with two regex, find only variable names with an underscore.
    terms = ['_ENV_MY_.+', 'ENV_MY_.+']

# Generated at 2022-06-13 14:47:01.841705
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Unit test variables
    test_dict = {'a':'1', 'b2':'2', 'c':'3'}


    # Creating unit test object
    lookup_test = LookupModule()

    # Testing with invalid terms
    terms = ['invalidterm1', 'invalidterm2', 'invalidterm3']
    try:
        lookup_test.run(terms=terms, variables=test_dict)
    except AnsibleError as err:
        assert err.message == "Unable to use \"invalidterm1\" as a search parameter: nothing to repeat"
    try:
        lookup_test.run(terms=terms[1], variables=test_dict)
    except AnsibleError as err:
        assert err.message == "Unable to use \"invalidterm2\" as a search parameter: nothing to repeat"
   

# Generated at 2022-06-13 14:47:09.563922
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    obj = LookupModule()
    ansible_vars = {'qz_1': 'hello', 'qz_2': 'world', 'qa_1': "I won't show", 'qz_': "I won't show either"}
    terms = ['^qz_.+']
    test1 = obj.run(terms, ansible_vars, variables=ansible_vars)
    assert (test1 == ['qz_1', 'qz_2'])

    terms = ['^qz_.+']
    test2 = obj.run(terms, ansible_vars, variables=ansible_vars)
    assert (test2 == ['qz_1', 'qz_2'])

    terms = ['.+']

# Generated at 2022-06-13 14:47:20.713194
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Create test object
    terms = ['^qz_.+']
    variables = {'qz_1':'hello', 'qz_2':'world', 'qa_1':'I wont show', 'qz_':'I wont show either'}
    lm = LookupModule()

    assert lm.run(terms, variables=variables) == ['qz_1', 'qz_2']

    # Create another test object with different variables
    terms = '.+'
    variables = {'qz_1':'hello', 'qz_2':'world', 'qa_1':'I wont show', 'qz_':'I wont show either'}
    lm = LookupModule()


# Generated at 2022-06-13 14:47:31.072400
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    # 1st test
    terms = ['^qz_.+']
    variables = {
        "qz_1": "hello",
        "qz_2": "world"
    }
    result = lookup.run(terms, variables)
    assert result == ['qz_1', 'qz_2'], '1st test failed'

    # 2nd test
    terms = ['.+']
    variables = variables
    result = lookup.run(terms, variables)
    assert result == ['qz_1', 'qz_2'], '2nd test failed'

    # 3rd test
    terms = ['hosts']
    result = lookup.run(terms, variables)
    assert result == [], '3rd test failed'

    # 4th test

# Generated at 2022-06-13 14:47:41.989029
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # pylint: disable=too-many-locals
    import os
    import tempfile

    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.collections import is_sequence

    data = {'foo': 'bar',
            'bar': 'baz',
            'json_dict': "{'foo': 'bar', 'bar': 'baz'}",
            'json_list': "['foo', 'bar', 'baz']",
            'yaml_dict': "foo: bar\nbar: baz",
            'yaml_list': "- foo\n- bar\n- baz"}

    # Create a temporary file from the data
    desc_1, tmp_filename_1 = tempfile.mkstemp(suffix='.yml')

# Generated at 2022-06-13 14:47:50.647310
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.modules.extras.cloud.doctest_helper import bs
    from ansible.module_utils.my_vars import my_vars
    from ansible.plugins.loader import lookup_loader

    lookup_plugin = lookup_loader.get('varnames')

    with bs("lookup('varnames', '^qz_.+')", my_vars()) as result:
        variable_names = list(my_vars().keys())
        terms = ['^qz_.+']
        kwargs = {}
        value = lookup_plugin.run(terms, my_vars(), **kwargs)
        assert value == ['qz_1', 'qz_2']

    with bs("lookup('varnames', '.+')", my_vars()) as result:
        variable_names

# Generated at 2022-06-13 14:48:02.484199
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # setting up the test variables
    test_varname_list = ['name', 'name_2', 'name_zone', 'name_location']
    test_variables = {varname : varname for varname in test_varname_list}

    # testing error raised when variable is None
    class object_LookupModule_run_variable_is_None:
        def run(self, terms, variables=None, **kwargs):
            assert variables is None
    test_LookupModule_run_variable_is_None = object_LookupModule_run_variable_is_None()

# Generated at 2022-06-13 14:48:11.756914
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms=['^qz_.+','abc','123','abc123']
    variables={'qz_1':'hello','qz_2':'world','qa_1':"I won't show",'qz_':"I won't show either",'abc':'found','123':'found','abc123':'found'}
    expected_results={'^qz_.+':['qz_1', 'qz_2'],'abc':['abc'],'123':['123'],'abc123':['abc123']}
    lookup = LookupModule()
    for term in terms:
        result=lookup.run([term], variables=variables)
        assert result==expected_results[term]

# Generated at 2022-06-13 14:48:20.990345
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.loader import lookup_loader

    # Generate the list of matches for our regex search
    term_matches = ['sub_one', 'sub_two', 'sub_three', 'sub_four', 'sub_five', 'sub_six']
    # Generate the list of non-matches for our regex search
    term_mismatches = ['sub_a', 'sub_b', 'sub_c', 'sub_d', 'sub_e', 'sub_f']

    # Generate a list of terms to search for
    search_terms = ['sub_', 'one', 'two', 'three', 'four', 'five', 'six']

    # Generate a dictionary of variables to search through

# Generated at 2022-06-13 14:48:42.923426
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test data
    words = ['taco', 'tacos', 'food', 'dinner', 'taco', 'tacos', 'lunch', 'breakfast', 'fruit', 'taco', 'tacos', 'taco', 'tacos']
    variables = {'names': words, 'var2': {}, 'var3': 'test', 'var4': 1234, 'var5': ['test', 'ing'], 'var6': {'test': 1}}

    # Setup
    import ansible.utils.vars as vars_utils
    import ansible.utils.unsafe_proxy as unsafe_proxy
    import ansible.plugins.loader as plugins_loader
    import os
    import sys
    import yaml

# Generated at 2022-06-13 14:48:52.980766
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Instantiate a LookupModule object
    lm = LookupModule()

    # Instantiate a dict
    variables = {'aa_1': 'hello', 'aa_2': 'world', 'bb_1': 'ciao', 'bb_2': 'mondo'}

    # Initialize the search terms. Here are all the variables that start with 'aa'
    terms = ['^aa_.+']
    result = lm.run(terms, variables=variables)
    expected_result = ['aa_1', 'aa_2']
    assert result == expected_result, "Expected result is %s, but got %s" % (expected_result, result)

    # Initialize the search terms. Here are all the variables that end with '_1'
    terms = ['.+_1$']

# Generated at 2022-06-13 14:49:00.333425
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    source = "test source"
    variables = {
        "ansible_var1": "hello",
        "ansible_var2": "world",
    }

    # Create instance of self
    class_instance = LookupModule()

    result = class_instance.run(terms=['^ansible_'], variables=variables)

    assert len(result) == 2
    assert "ansible_var1" in result
    assert "ansible_var2" in result

# Generated at 2022-06-13 14:49:10.894778
# Unit test for method run of class LookupModule
def test_LookupModule_run():
	
	print("Initializing Test Variables")
	lookup_var = {'1': 'hello', '2':'ansible'}
	lookup_var_new = {'1': 'hello1', '2':'ansible2'}
	test_module = LookupModule()
	test_module.set_options(var_options=lookup_var, direct="")
	
	print("Testing Retrieval of Varnames")
	assert test_module.run(terms=['^1'], variables=lookup_var) == ['1']
	assert test_module.run(terms=['^1','^2'], variables=lookup_var) == ['1','2']
	
	print("Testing for Non-Existent Varname")

# Generated at 2022-06-13 14:49:15.302817
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    rlm = LookupModule()
    t1 = {'k1': 'a', 'k2': 'b', 'k3': 'a'}
    l1 = rlm.run(['k[23]', 'k1'], t1)
    assert(l1 == ['k2', 'k1', 'k3'])

# Generated at 2022-06-13 14:49:27.266933
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    variables = {"test1": "test1", "test2": "test2", "test3": "test3"}
    terms = ["test1","test4"]
    result = lookup_module.run(terms,variables)
    assert result == ["test1"], "A single match is returned"
    variables["test4"] = "test4"
    result = lookup_module.run(terms,variables)
    assert result == ["test1","test4"], "Multiple matching results are returned"
    terms = [".*"]
    result = lookup_module.run(terms,variables)
    assert result == ["test1","test2","test3","test4"], "Regex is also supported"
    terms = [".*1"]
    result = lookup_module.run(terms,variables)
   

# Generated at 2022-06-13 14:49:37.985116
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import PY3

    # Load settings module
    lookup_module = LookupModule()
    settings_module = AnsibleModule(argument_spec=dict(
        _terms=dict(type='list', required=True),
    ))

    settings_module.params['_terms'] = ['.+_zone$', '.+_location$']
    settings_module.params['var'] = 'zone'
    settings_module.params['var2'] = 'location'
    settings_module.params['var3'] = 'var3'

    # Check values returned
    settings_module.params['var_options'] = settings_module.params
    settings_module.params['direct'] = {}

# Generated at 2022-06-13 14:49:44.371475
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    ansible.__version__ = '2.0.0.0'
    lookup = LookupModule()
    terms = '^qz_.+'
    variables = {'qz_1':'hello',
                 'qz_2':'world',
                 'qa_1':'I will not show',
                 'qz_':'I will not show either'}
    ret = lookup.run(terms, variables)
    assert ret == ['qz_1','qz_2']
    assert type(ret) is list

# Generated at 2022-06-13 14:50:07.779244
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ['^qz_.+']
    variables = {
        'qz_1': 'hello',
        'qz_2': 'world',
        'qa_1': "I won't show",
        'qz_': "I won't show either",
    }
    ret = lookup.run(terms=terms, variables=variables)
    assert ret == ['qz_1', 'qz_2']

    terms = ['.+']
    ret = lookup.run(terms=terms, variables=variables)
    assert ret == ['qz_1', 'qz_2', 'qa_1', 'qz_']

    terms = ['hosts']
    ret = lookup.run(terms=terms, variables=variables)
    assert ret == []


# Generated at 2022-06-13 14:50:17.911327
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    assert l.run(['^qz_.+'], {'qz_1': 'hello', 'qz_2': 'world', 'qa_1': "I won't show"}) == ['qz_1', 'qz_2']
    assert l.run(['.+'], {'qz_1': 'hello', 'qz_2': 'world', 'qa_1': "I won't show"}) == ['qz_1', 'qz_2', 'qa_1']
    assert l.run(['hosts'], {'hosts': 'hello', 'hosts_1': 'world', 'ha_1': "I won't show"}) == ['hosts', 'hosts_1']


# Generated at 2022-06-13 14:50:26.857685
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['^qz_.+', '^qz_.+']
    variables = {'qz_1': 'hello', 'qz_2': 'world', 'qa_1': "I won't show", 'qz_': "I won't show either"}
    expected = ['qz_1', 'qz_2']
    assert(LookupModule().run(terms, variables) == expected)

    terms = ['.+']
    expected = variables.keys()
    assert(LookupModule().run(terms, variables) == expected)

    terms = ['hosts']

# Generated at 2022-06-13 14:50:36.000576
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import StringIO
    from ansible.parsing.vault import VaultLib
    from ansible.plugins.loader import lookup_loader
    from ansible.utils.vault import VaultAES256
    lookup = lookup_loader.get('varnames')

    j = '$ANSIBLE_VAULT;1.1;AES256\n66303733666463623832653332626161356233353664356562346163323964356562316363353\n363031366530346435373833613366656464353934623734653638353465303966656265623361\n66346465\n'
    vault = VaultLib(VaultAES256)

# Generated at 2022-06-13 14:50:45.236305
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    input = {
        "terms": [
            '^qz_.+',
            '.+_zone$',
            '.+_location$',
        ],
        "variables": {
            'qz_1': 'hello',
            'qz_2': 'world',
            'qa_1': 'I wont show',
            'qz_': 'I wont show either',
            'zone_1': '1',
            'zone_2': '2',
            'zone_3': '3',
            'location_1': '1',
            'location_2': '2',
            'location_3': '3',
        }
    }

# Generated at 2022-06-13 14:50:48.068105
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    assert lookup.run(['.+', '.+'], {'a': 1, 'b': 2, 'c': 3}) == lookup.run(['.+'], {'a': 1, 'b': 2, 'c': 3})

# Generated at 2022-06-13 14:50:55.948326
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_instance = LookupModule()
    lookup_instance.set_loader(None)
    result = lookup_instance.run(terms=['^qz_.+'], variables={'qz_1': 'hello', 'qz_2': 'world', 'qa_1': "I won't show", 'qz_': "I won't show either"})
    assert result == ['qz_1', 'qz_2']
    result = lookup_instance.run(terms=['.+'], variables={'qz_1': 'hello', 'qz_2': 'world', 'qa_1': "I won't show", 'qz_': "I won't show either"})
    assert result == ["qz_1", "qz_2", "qa_1", "qz_"]

# Generated at 2022-06-13 14:51:03.183888
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from collections import namedtuple
    from ansible.parsing.dataloader import DataLoader
    
    lookup_module = LookupModule()
    
    # Test: Empty terms
    variables = { 'name': "Dummy var"}
    assert lookup_module.run(terms=[], variables=variables, **dict()) == []

    # Test: Check if correct error is thrown, when no variables passed as argument
    try:
        lookup_module.run(terms=["dummy"], variables=None, **dict())
        assert False
    except AnsibleError:
        pass

    # Test: Check if correct error is thrown, when terms isn't a string
    try:
        lookup_module.run(terms=[1], variables=variables, **dict())
        assert False
    except AnsibleError:
        pass

    # Test: Check

# Generated at 2022-06-13 14:51:12.283227
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import mock
    import re

    from ansible.module_utils._text import to_native
    from ansible.errors import AnsibleError

    x = LookupModule()

    # Test with no variables available
    try:
        x.run(terms="anything")
    except AnsibleError as e:
        assert "No variables available to search" in to_native(e)

    # Test with terms that is not a string
    try:
        x.run(terms=["unexpected"], variables={"a": "b"})
    except AnsibleError as e:
        assert "Invalid setting identifier, \"unexpected\" is not a string" in to_native(e)

    # Test with terms that is a string but not a valid regex

# Generated at 2022-06-13 14:51:19.626425
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    module = LookupModule()

    terms = ['^qz_.+']
    variables = {
        'qz_1': 'hello',
        'qz_2': 'world',
        'qa_1': "I won't show",
        'qz_': "I won't show either"
    }
    expected_result = ['qz_1', 'qz_2']
    assert module.run(terms, variables) == expected_result

    terms = ['^qz_.+']
    variables = {}
    expected_result = []
    assert module.run(terms, variables) == expected_result

    terms = ['^qz_.+']
    variables = {'a': 'A'}
    expected_result = []
    assert module.run(terms, variables) == expected_result

    # Test matching multiple patterns


# Generated at 2022-06-13 14:51:53.972245
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # test with invalid regex
    l = LookupModule()
    l.set_options(direct={}) # place to set specified options
    try:
        l.run(['*'], variables={})
    except Exception as e:
        assert "Unable to use" in str(e)

    # test normal work
    l = LookupModule()
    l.set_options(direct={}) # place to set specified options
    assert l.run(['.+'], variables={'a': 'a', 'b': 'b'}) == ['a', 'b']
    assert l.run(['^a'], variables={'a': 'a', 'b': 'b'}) == ['a']
    assert l.run(['^a$'], variables={'a': 'a', 'b': 'b'}) == ['a']

# Generated at 2022-06-13 14:52:03.179258
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test with terms as list of strings
    terms = ["a", "^b$"]
    variables = {'a': '1', 'b': '2', 'c': '3'}
    ret = LookupModule.run(terms, variables)
    assert len(ret) == 2

    # Test with term as string
    terms = "a"
    ret = LookupModule.run(terms, variables)
    assert len(ret) == 1

    # Test with invalid term
    try:
        LookupModule.run(1, variables)
    except AnsibleError as e:
        assert e.message == 'Invalid setting identifier, "1" is not a string, it is a <class \'int\'>'

# Generated at 2022-06-13 14:52:10.999110
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.module_utils.six import StringIO
    from ansible.utils.vars import combine_vars
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.lookup.varnames import LookupModule

    test_vars = VariableManager()
    test_loader = DataLoader()

    test_vars.set_variable('qz_1', 'hello')
    test_vars.set_variable('qz_2', 'world')
    test_vars.set_variable('qa_1', "I won't show")
    test_vars.set_variable('qz_', "I won't show either")

    # test running in basic mode
    test_plugin = LookupModule()
    result = test

# Generated at 2022-06-13 14:52:21.852597
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test case when variables are None
    lu = LookupModule()
    try:
        lu.run('test')
    except AnsibleError as e:
        assert e.message == 'No variables available to search'

    # Test case when term is not a string
    lu = LookupModule()
    try:
        lu.run([3])
    except AnsibleError as e:
        assert e.message == 'Invalid setting identifier, "3" is not a string, it is a <class \'int\'>'

    # Test case when exception raised when trying to compile regex
    lu = LookupModule()
    try:
        lu.run(['['])
    except AnsibleError as e:
        assert e.message == 'Unable to use "[" as a search parameter: nothing to repeat at position 0'

    #

# Generated at 2022-06-13 14:52:30.738667
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Setup environment for test set
    variables = {'abc': 'abc', 'def': 'def', 'ghi': 'ghi'}
    terms = []
    terms.append('abc')

    # Invoke test set
    result = LookupModule().run(terms, variables)

    # Validate test set
    assert result == ['abc']

    # Setup environment for test set
    variables = {'abc': 'abc', 'def': 'def', 'ghi': 'ghi'}
    terms = []
    terms.append('missing')

    # Invoke test set
    result = LookupModule().run(terms, variables)

    # Validate test set
    assert result == []

    # Setup environment for test set
    variables = {'abc': 'abc', 'def': 'def', 'ghi': 'ghi'}
   

# Generated at 2022-06-13 14:52:39.970010
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    """Test run() of class LookupModule"""

    # Test with variable names starting with 'qz_'
    context = {'qz_1': 'hello', 'qz_2': 'world', 'qa_1': 'I won\'t show', 'qz_': 'I won\'t show either'}
    variables = context
    terms = ['^qz_.+']

    lookup_module = LookupModule()
    result = lookup_module.run(terms, variables=variables)
    assert result == ['qz_1', 'qz_2']

    # Test with 'hosts' in their names

# Generated at 2022-06-13 14:52:47.511596
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l.set_options(var_options={'qz_1' : 'abc', 'qz_2': 'def', 'qa_1': 'def'}, direct={})
    assert l.run(['^qz_.']) == ['qz_1', 'qz_2']
    assert l.run(['^qa_2']) == []
    assert l.run(['.+']) == ['qz_1', 'qz_2', 'qa_1']
    assert l.run(['hosts']) == []

# Generated at 2022-06-13 14:52:53.441833
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Setting up the necessary variables for testing
    terms = ["^qz_.+"]
    variables = {
                'qz_1':'hello',
                'qz_2':'world',
                'qa_1':"I won't show",
                'qz_':"I won't show either"
                }
    module_utils_text = {
                'to_native': to_native
                }

    # Setup class LookupModule
    LookupModule(loader=None, templar=None, **module_utils_text).run(terms, variables)


# Generated at 2022-06-13 14:53:00.469210
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Instance setup
    c = LookupModule()

    # Mocks
    ret = []
    variable_names = list(["foo_zone", "foo_location", "bar_zone", "bar_location"])
    term = "foo"
    variable_names.append(term)

    for term in variable_names:
        if not isinstance(term, string_types):
            raise AnsibleError('Invalid setting identifier, "%s" is not a string, it is a %s' % (term, type(term)))

        try:
            name = re.compile(term)
        except Exception as e:
            raise AnsibleError('Unable to use "%s" as a search parameter: %s' % (term, to_native(e)))


# Generated at 2022-06-13 14:53:09.380217
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def add_host_vars(hostname, hostvars):
        host_instance = Host('somehost', hostvars)
        return [host_instance]


# Generated at 2022-06-13 14:54:11.375217
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup.varnames import LookupModule
    from ansible.parsing.dataloader import DataLoader

    terms = ['^qz_.+']
    variables = {'qz_1': 'hello',
                 'qz_2': 'world',
                 'qa_1': "I won't show",
                 'qz_': "I won't show either"}
    lookup = LookupModule()
    result = lookup.run(terms=terms, variables=variables)
    assert set(result) == set(['qz_1', 'qz_2'])

# Generated at 2022-06-13 14:54:15.725992
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test run of the method LookupModule.run with a list of terms.
    variables = {"qz_1": "hello", "qz_2": "world", "qa_1": "I won't show", "qz_": "I won't show either"}
    lm = LookupModule()
    lm.set_options(var_options=variables, direct=None)
    assert lm.run(["^qz_.+"]) == ["qz_1", "qz_2"]


# Generated at 2022-06-13 14:54:23.301436
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:54:32.854234
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup.varnames import LookupModule

    # Test with no matching var
    vars = {'qz_1': 'hello', 'qz_2': 'world'}
    lookup = LookupModule()
    assert lookup.run(['not_exist_var'], variables=vars) == []

    # Test with exact match
    vars = {'qz_1': 'hello', 'qz_2': 'world'}
    variables = {'qz_1': 'hello', 'qz_2': 'world'}
    lookup = LookupModule()
    assert lookup.run(['qz_1'], variables=vars) == ['qz_1']

    # Test with regex match

# Generated at 2022-06-13 14:54:41.882096
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()
    var_options = dict(
        foo_1=1,
        foo_2=dict(a=1, b=2),
        bar_1=3.14,
        bar_2="bar",
        baz_1=["a", "b", "c"],
        baz_2=None,
        baz_3=True,
        baz_4=False,
    )

    # Test run with an empty term
    assert lookup_plugin.run(terms=[], variables=var_options, direct=dict()) == []

    # Test run with a term that is not a string
    try:
        lookup_plugin.run(terms=[1], variables=var_options, direct=dict())
    except Exception as e:
        assert isinstance(e, AnsibleError)

# Generated at 2022-06-13 14:54:46.730460
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ['^qz_.+']
    variables = {
        'qz_1': 'hello',
        'qz_2': 'world',
        'qa_1': "I won't show",
        'qz_': "I won't show either",
    }

    assert lookup.run(terms, variables) == ['qz_1', 'qz_2']

# Generated at 2022-06-13 14:54:54.840412
# Unit test for method run of class LookupModule