

# Generated at 2022-06-13 14:45:02.744429
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test run() method of class LookupModule
    # Input data:
    #   terms - list of strings representing the terms to search
    #   variables - dictionary of dictionaries representing the variables for the current task
    # Return list of variables names that match with any of the search terms

    lu = LookupModule()

    # Test case: No variables
    # Expected result: AnsibleError exception
    try:
        lu.run(['proxy', 'http_port'], None)
    except AnsibleError as e:
        assert(e.args[0] == 'No variables available to search')

    # Test case: Empty variables
    # Expected result: Empty list
    variables = {}
    result = lu.run(['proxy', 'http_port'], variables)
    assert(result == [])

    # Test case: Not string

# Generated at 2022-06-13 14:45:13.398187
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    ll = LookupModule()
    variables = {'qz_1': 'hello', 'qz_2': 'world', 'qa_1': "I won't show", 'qz_': "I won't show either"}
    result = ll.run(['.+_zone$', '.+_location$'], variables=variables)
    assert len(result) == 0

    result = ll.run(['^qz_.+'], variables)
    assert len(result) == 3

    try:
        result = ll.run([123])
    except Exception as e:
        assert e.args[0] == 'Invalid setting identifier, "123" is not a string, it is a <class \'int\'>'

# Generated at 2022-06-13 14:45:22.264991
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ['^qz_.+', '.+']
    variables = {}
    variables['qz_1'] = 'hello'
    variables['qz_2'] = 'world'
    variables['qa_1'] = "I won't show"
    variables['qz_'] = "I won't show either"
    kwargs = {}
    # Test the first search pattern
    result = lookup.run(terms[0:1], variables, **kwargs)
    assert ['qz_1', 'qz_2'] == result
    # Test all search patterns
    result = lookup.run(terms, variables, **kwargs)

# Generated at 2022-06-13 14:45:32.981405
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Test for lookup module for looking up variables in Ansible.
    """
    lookup_var = LookupModule()
    ansible_vars = {"qz_1": "hello", "qz_2": "world", "qa_1": "I won't show", "qz_": "I won't show either"}
    test_fn = lambda actual, expected: actual == expected
    assert test_fn(lookup_var.run(['^qz_.+']), ['qz_1', 'qz_2', 'qz_'])

    test_fn = lambda actual, expected: actual == expected
    assert test_fn(lookup_var.run(['.+']), ['qz_1', 'qz_2', 'qa_1', 'qz_'])

    test_fn = lambda actual, expected: actual

# Generated at 2022-06-13 14:45:43.369152
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Define some test variables
    vars = dict()
    vars["hosts"] = "hosts"
    vars["hosts_zone"] = "hosts_zone"
    vars["hosts_hosts"] = "hosts_hosts"
    vars["hosts_location"] = "hosts_location"
    vars["hosts_zone_a"] = "hosts_zone_a"
    vars["hosts_location_b"] = "hosts_location_b"

    lookup_module = LookupModule()
    lookup_module.set_options(vars)

    # Test search with string
    terms = ["hosts"]

# Generated at 2022-06-13 14:45:51.172867
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Define variables used in testing
    variables = {'qz_1': 'hello', 'qz_2': 'world', 'qa_1': "I won't show", 'qz_': "I won't show either"}

    # Define the method args and create a plot to test
    terms = ['^qz_.+']
    qm = LookupModule()

    # Test the method run
    qm.run(terms, variables=variables)
    assert qm._values == ['qz_1', 'qz_2']

# Generated at 2022-06-13 14:45:59.808999
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup.varnames import LookupModule

    l = LookupModule()

    # test varnames lookup for variables that match qz_.+
    data = [b'^qz_.+']
    result = l.run(data, variables={'q1': 'a', 'q2': 'b', 'qz_1': 'a', 'qz_2': 'b'})
    assert len(result) == 2

    # test varnames lookup for all variables
    data = [b'.+']
    result = l.run(data, variables={'q1': 'a', 'q2': 'b', 'qz_1': 'a', 'qz_2': 'b'})
    assert len(result) == 4

    # test varnames lookup for variables that contain 'hosts' in their names


# Generated at 2022-06-13 14:46:09.387318
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''
    Test LookupModule.run() method
     - No variables available, should return AnsibleError
     - Invalid setting identifier, should return AnsibleError
     - Unable to use as a search parameter, should return AnsibleError
     - Search for a variable name
    '''

    # Test object
    test_obj = LookupModule()

    # Test no variables available
    assert isinstance(test_obj.run(terms=[]), AnsibleError)

    # Test invalid setting identifier
    assert isinstance(test_obj.run(terms=[{}]), AnsibleError)

    # Test unable to use as a search parameter
    assert isinstance(test_obj.run(terms=["^["]), AnsibleError)

    # Test search for variable name

# Generated at 2022-06-13 14:46:14.438628
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    variables = {'host': 'host', 'host1': 'host1', 'host2': 'host2', 'host3': 'host3', 'host4': 'host4', 'host5': 'host5'}
    terms = ['.+host.+']
    results = lookup.run(terms, variables=variables, expand_lists=False)
    assert len(results) == 5

# Generated at 2022-06-13 14:46:15.006236
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert True

# Generated at 2022-06-13 14:46:25.943659
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:46:32.322982
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # result of __init__
    plugin = LookupModule()

    # Mocks
    class MockVariables(object):
        def __init__(self):
            self.ansible_version = "2.8.0"
            self.ansible_group_priorities = []

    class MockRunner(object):
        def __init__(self):
            self.var = {
                'group_names': [],
                'groups': {},
                'inventory_dir': '',
                'play_basedir': '',
                'playbook_dir': '',
                'playbook_dirs': [],
                'all': MockVariables()
            }

    class MockTaskVars(object):
        def __init__(self):
            self._task = None
            self._vars = MockRunner()

    #

# Generated at 2022-06-13 14:46:42.426612
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Load test data from testcase file
    testcase_data = load_data_from_file('varnames.yaml')

    # Create object of lookup module
    varnames_lookup = LookupModule()

    # Iterate over test cases
    for case in testcase_data:

        # Generate input arguments for lookup plugin
        terms = case['test']

        # Generate expected output value
        expected_value = case['expected']

        # Lookup plugin run method returns a list of
        # variable names matching regex passed as input
        actual_value = varnames_lookup.run(terms)

        # Assert expected value is equal to actual value
        assert isinstance(actual_value, list)
        assert isinstance(expected_value, list)
        assert len(expected_value) == len(actual_value)
        assert all

# Generated at 2022-06-13 14:46:53.443908
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup import LookupModule
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils.six import string_types

    from sys import version_info
    py3 = version_info[0] > 2

    variables = dict()
    lm = LookupModule(
        loader=None,
        templar=None,
        variables=variables,
        basedir=None
    )

    variables.update({'one': 1, 'two': '2', 'true': True, 'false': False})

    ansible_dict = dict()
    ansible_dict['one'] = 1
    ansible_dict['two'] = '2'
    ansible_dict['true'] = boolean(1)
    ansible_dict['false'] = boolean

# Generated at 2022-06-13 14:47:03.816222
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    result = LookupModule(loader=None, templar=None, variables=dict(a=1, ab=2, abc=3, xy_abc=4)).run(['^a.+'])
    assert len(result) == 3
    assert 'a' in result
    assert 'ab' in result
    assert 'abc' in result

    assert len(LookupModule(loader=None, templar=None, variables=dict(a=1, ab=2, abc=3, xy_abc=4)).run(['^aaa.+'])) == 0
    assert len(LookupModule(loader=None, templar=None, variables=dict(a=1, ab=2, abc=3, xy_abc=4)).run(['^a.+', '^x.+'])) == 4
   

# Generated at 2022-06-13 14:47:10.592856
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test list variables that start with qz_
    test_args = dict(terms=['^qz_.+'],
                    variables={'qz_1': 'hello', 'qz_2': 'world', 'qa_1': "I won't show", 'qz_': "I won't show either"}
                    )
    ret = LookupModule().run(**test_args)
    assert ret == ['qz_1', 'qz_2']
    # test list all variables
    test_args = dict(terms=['.+'],
                    variables={'var1': 'hello', 'var2': 'world'}
                    )
    ret = LookupModule().run(**test_args)
    assert ret == ['var1', 'var2']
    # test list variables with 'hosts' in their names
    test_args

# Generated at 2022-06-13 14:47:21.408812
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup import LookupModule
    from ansible.module_utils.six import PY3

    lookup_module = LookupModule()

    # test matching
    variables = {
        'password' : 'abcde',
        'password_abc' : 'abc',
        'password_xyz' : 'xyz',
        'password_def' : 'def',
        'other' : 'fghi'
    }

    # simple match
    terms = ['password_def']
    results = lookup_module.run(terms, variables=variables)
    assert results == ['password_def']

    # regex match
    terms = ['password_.*']
    results = lookup_module.run(terms, variables=variables)

# Generated at 2022-06-13 14:47:31.456886
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play

    def get_test_lookup_plugin_varnames():
        lookup_plugin = LookupModule()
        lookup_plugin.set_loader('foo')
        lookup_plugin.set_inventory(Inventory(loader=None, variable_manager=None, host_list=[]))
        lookup_plugin.set_play(Play().load({}, loader=None, variable_manager=None, templar=None))
        return lookup_plugin

    lookup_plugin = get_test_lookup_plugin_varnames()

    terms = ['^qz_.+']

# Generated at 2022-06-13 14:47:37.213128
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class Variables:
        var = "abcd"
        var2 = 5
        var3 = "\nxyz\n"

    x = LookupModule()
    x.set_options(var_options={}, direct={})

    terms = ["var"]
    variables = Variables()

    ret = x.run(terms, variables)
    assert(ret == ["var"])


# Generated at 2022-06-13 14:47:45.066625
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test no variable
    varnames = LookupModule()
    results = varnames.run([])
    assert results == []

    # Test no term
    varnames = LookupModule()
    results = varnames.run(None, variables={'x1': 1, 'x2': 2})
    assert results == []

    # Test one variable
    varnames = LookupModule()
    results = varnames.run(['x1'], variables={'x1': 1, 'x2': 2})
    assert results == ['x1']

    # Test two variables
    varnames = LookupModule()
    results = varnames.run(['x1', 'x2'], variables={'x1': 1, 'x2': 2})
    assert results == ['x1', 'x2']

    # Test variable name with hyphen and slash

# Generated at 2022-06-13 14:47:56.272749
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    variables = {'var_b': '', 'var_a': '', 'var_a1': '', 'var_ax': ''}
    terms = ['^var_.+', 'var_.+x']
    assert lookup_module.run(terms, variables) == ['var_ax', 'var_a1']


# Generated at 2022-06-13 14:48:05.215391
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a dummy variables structure
    variables = {}
    variables["TEST_var_1"] = "var1"
    variables["TEST_var2"] = "var2"
    variables["var3"] = "var3"
    variables["TEST_var_local"] = "local"
    variables["TEST_var_remote"] = "remote"
    # Create a new instance of LookupModule with the dummy variables structure
    lookup_module = LookupModule()
    # Call run()
    result = lookup_module.run(["^TEST_var.+$"], variables)
    # Test the result
    assert result == ["TEST_var_1", "TEST_var_local", "TEST_var_remote", "TEST_var2"]

# Generated at 2022-06-13 14:48:11.883556
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    if sys.version_info[0] < 3:
        dict = dict

    my_vars = dict(a='aaa', b='bbb', ccc='cccc')
    my_dict = dict(
        _terms=['^b'],
        variables=my_vars,
        _variables=my_vars,
        my_vars=my_vars,
        incl_file=['/etc/hosts'],
        incl_file_secret=['/etc/shadow'],
        term_one='^a',
        term_two='^b'
    )

    my_lookup = LookupModule()
    my_lookup.set_options(my_dict)

# Generated at 2022-06-13 14:48:32.521066
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_instance = LookupModule()

    # No variables
    res = lookup_instance.run(['a'], variables=None)
    assert res == []

    # One non-regex term
    res = lookup_instance.run(['a'], variables={'a': {'a': 'a'}})
    assert res == ['a']
    res = lookup_instance.run(['a'], variables={'b': {'b': 'b'}})
    assert res == []

    # One regex term
    res = lookup_instance.run(['a'], variables={'aa': {'a': 'a'}})
    assert res == ['aa']
    res = lookup_instance.run(['a'], variables={'ab': {'a': 'a'}})
    assert res == ['ab']

# Generated at 2022-06-13 14:48:39.977132
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    LookupModule.run() Test
    """

# Generated at 2022-06-13 14:48:48.286492
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Assumed variables that the lookup plugin will be querying
    variables = {
        "qz_1": "hello",
        "qz_2": "world",
        "qa_1": "I won't show",
        "qz_": "I won't show either",
    }

    # Call the main test
    # Note: The return value of the main test is a list of dicts
    LookupModule(loader=None, variables=variables).run(terms=["^qz_.+"], variables=variables)

    # Count of tests run
    testCount = 0
    # The following tests are to see if variables are in the return value
    # Test 1: If a variable starts with qx_

# Generated at 2022-06-13 14:48:54.898167
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Arrange
    test_module = LookupModule()
    test_vars = {'qz_1': 'hello', 'qz_2': 'world', 'qa_1': "I won't show"}
    test_terms = ['^qz_.+', '.+']

    # Act
    result = test_module.run(test_terms, test_vars)

    # Assert
    expected_results = ['qz_2', 'qz_1', 'qz_1', 'qz_2', 'qa_1']
    assert result == expected_results

# Generated at 2022-06-13 14:49:04.701110
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    terms = ['^qz_.+']
    variables = {
        'qz_1': 'hello',
        'qz_2': 'world',
        'qa_1': 'I won\'t show',
        'qz_': 'I won\'t show either',
        }

    expected_result = ['qz_1', 'qz_2']
    actual_result = LookupModule().run(terms, variables=variables)
    assert actual_result == expected_result

    terms = ['.+']
    variables = {
        'qz_1': 'hello',
        'qz_2': 'world',
        'qa_1': 'I won\'t show',
        'qz_': 'I won\'t show either',
        }


# Generated at 2022-06-13 14:49:15.084074
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:49:16.085964
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    print('This is a test')

# Generated at 2022-06-13 14:49:34.908215
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Create bare-bones class
    class LookupModuleFake(LookupModule):
        def __init__(self, loader=None, templar=None, **kwargs):
            self.wc_finder = re.compile('-')
        def get_basedir(self, variables):
            return variables['playbook_dir']
        def get_vars(self, loader, variables, *args, **kwargs):
            if args[0] == 'playbook_dir':
                raise KeyError
            else:
                return variables, []
    
    # Instantiate the above class
    l = LookupModuleFake()
    # Test it

# Generated at 2022-06-13 14:49:41.419307
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class TestIter():
        def __iter__(self):
            yield 'qz_1'
            yield 'qz_2'
            yield 'qa_1'
            yield 'qz_'
    class TestVariables():
        def __init__(self):
            self.keys = TestIter()
    result = LookupModule().run(terms=['^qz_.+'], variables=TestVariables())
    assert result == ['qz_1', 'qz_2']

# Generated at 2022-06-13 14:49:42.368891
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert callable(LookupModule.run)

# Generated at 2022-06-13 14:49:53.803586
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.parsing.yaml.objects import AnsibleUnicode

    test_vars = {'var1': 'hello'}

    # Make sure that run still functions with terms = None
    lm = LookupModule()
    lm.set_options(var_options=test_vars)
    assert lm.run(None) == []

    # Make sure that run still functions with terms = AnsibleMapping (because of the 'isinstance(term, string_types)'
    # check in the run method)
    lm = LookupModule()
    lm.set_options(var_options=test_vars)

# Generated at 2022-06-13 14:50:04.059490
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest

    lookup = LookupModule()

    lookup.set_options(var_options = {"qz_1": "hello", "qz_2": "world", "qa_1": "I won't show", "qz_": "I won't show either"})

    assert lookup.run(["^qz_.+"]) == ['qz_1', 'qz_2']
    assert lookup.run([".+"]) == ['qz_1', 'qz_2', 'qa_1', 'qz_']
    assert lookup.run(["hosts"]) == []
    assert lookup.run([".+_zone$", ".+_location$"]) == []

# Generated at 2022-06-13 14:50:12.594286
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import logging
    import shutil
    import tempfile

# Generated at 2022-06-13 14:50:22.994600
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Arrange
    input_arguments = dict()
    input_arguments['_terms'] = ["^qz_.+"]
    input_arguments['_variables'] = dict()
    input_arguments['_variables']['qz_1'] = "hello"
    input_arguments['_variables']['qz_2'] = "world"
    input_arguments['_variables']['qz_3'] = "world"
    input_arguments['_variables']['qa_1'] = "I won't show"
    input_arguments['_variables']['qz_'] = "I won't show either"
    expected_output =  ['qz_1', 'qz_2', 'qz_3']


    # Act
    lookup_plugin = LookupModule

# Generated at 2022-06-13 14:50:32.865870
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # 1. Test the case when no variables are provided
    # Expected result: An error is raised
    try:
        looker = LookupModule()
        looker.run("test")
        test = False
    except AnsibleError:
        test = True

    assert test

    # 2. Test the case when variables are provided but no variable name matches
    # Expected result: List of variable names is empty
    looker = LookupModule()
    variables = {
        "test1": "test_val1",
        "test2": "test_val2",
        "test3": "test_val3"
    }
    terms = ["test"]
    test_list = looker.run(terms, variables)
    assert test_list == []

    # 3. Test the case when variables are provided and one variable name matches
    #

# Generated at 2022-06-13 14:50:36.496317
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''Tests LookupModule.run()'''
    print('Testing LookupModule.run()')
    assert 1 == 0

# Generated at 2022-06-13 14:50:37.077289
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert False

# Generated at 2022-06-13 14:51:00.511316
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    f = LookupModule()
    terms = ['^qz_.+']
    variables = {'qz_1': 'hello', 'qz_2': 'world', 'qa_1': 'I won\'t show', 'qz_': 'I won\'t show either'}
    result = f.run(terms, variables)
    assert result == ['qz_1', 'qz_2']

# Generated at 2022-06-13 14:51:06.735442
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    vars = {'hosts': 'hosts', 'host_name': 'host_name', 'host_name_ssh': 'host_name_ssh', 'host_name_manage': 'host_name_manage', 'host_name_ansible': 'host_name_ansible'}
    results = lm.run(terms=['hosts'], variables=vars)
    assert len(results) == 1
    assert results[0] == 'hosts'

# Generated at 2022-06-13 14:51:11.156597
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.vars.hostvars import HostVars
    from collections import namedtuple
    # Cannot use mock.patch because ansible.vars.hostvars.HostVars is an old style class
    # so there is no __mro__ and mock.patch.object does not work
    # Instead we use FakeHostVars
    FakeHostVars = namedtuple('HostVars', 'data')

# Generated at 2022-06-13 14:51:18.599958
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # If a python regex object is for some reason passed instead of a string, it should be handled
    __module__ = AnsibleError
    module_args = {}
    lu = LookupModule()
    # TODO: add better exception handling for test cases
    try:
        lu.run(terms=[re.compile('.+')], variables=dict())
    except Exception as e:
        assert type(e) == AnsibleError, "Exception should be of type AnsibleError"
    
    # If a list of strings is passed as search parameters, the lookup module should return a list of strings
    module_args = {'_terms': ['^a.+', 'b$', 'c$']}
    variables = {'abvba': '', 'bcd': '', 'c': ''}
    lu = LookupModule()
   

# Generated at 2022-06-13 14:51:23.929791
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_object = LookupModule()
    terms = ['^qz_.+']
    variables = {'qa_1': 'I won\'t show', 'qz_': 'I won\'t show either', 'qz_1': 'hello', 'qz_2': 'world'}
    result = lookup_object.run(terms, variables)
    assert result == ['qz_1', 'qz_2']


# Generated at 2022-06-13 14:51:30.871529
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Here we don't use a fixture because it would be inefficient
    # If a change breaks the test, more fixtures should be added in the tests/fixtures directory
    # to provide the correct context using the correct data
    #
    # Fixtures are very useful but spawn processes and are not suited for repeated data
    #
    # mock is used here
    import mock

    # We want to test that the method raise an error when 'terms' is not a string
    #
    # Here's the code from the method:
    #   if not isinstance(term, string_types):
    #      raise AnsibleError('Invalid setting identifier, "%s" is not a string, it is a %s' % (term, type(term)))
    # we
    # - mock the method to change the behavior
    # - call the method
    # - check the behavior
   

# Generated at 2022-06-13 14:51:36.695377
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Must be the same code used in LookupModule
    # and the class must be declared
    class Variables:
        qz_1 = 'hello'
        qz_2 = 'world'
        qa_1 = "I won't show"
        qz_ = "I won't show either"
    class LookupModule2:
        def __init__(self):
            self.var_options = Variables()

    # Valid call
    lm = LookupModule2()
    assert lm.run(['^qz_.+'], Variables) == ['qz_1', 'qz_2']
    assert lm.run(['.+'], Variables) == ['qz_1', 'qz_2', 'qa_1', 'qz_']

# Generated at 2022-06-13 14:51:42.927240
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_module = LookupModule()
    test_terms = [
        ['hello'],
        ['h.{2}o'],
        ['h.{2}o', 'wo.*'],
        ['^qz_.+'],
        ['.+'],
        ['hosts'],
        ['.+_zone$', '.+_location$'],
        ['^[0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}$']
    ]

# Generated at 2022-06-13 14:51:46.888172
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    terms = ['^qz_.+', '^qa_.+']
    variables = {'qz_1': 'hello', 'qz_2': 'world', 'qa_1': "I won't show", 'qz_': "I won't show either"}
    assert LookupModule().run(terms, variables) == ['qz_1', 'qz_2', 'qa_1']

# Generated at 2022-06-13 14:51:50.559333
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lu_module = LookupModule()
    lu_module.set_options(var_options={'a': 1}, direct={})
    assert lu_module.run(terms=["a"], variables={'a': 1}) == ["a"]


# Generated at 2022-06-13 14:52:35.601907
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['^qa_.+', '^qz_.+$']
    variables = {'qa_1': 'hello', 'qa_2': 'world', 'qa_a': 'hello', 'qa_b': 'hello', 'qz_': 'hello', 'qz_1': 'hello', 'qz_2': 'hello'}
    lkm = LookupModule()
    lkm.set_options(var_options=variables, direct=dict())
    assert len(lkm.run(terms)) == 7
    assert 'qz_' in lkm.run(terms)
    assert 'qa_1' in lkm.run(terms)
    assert 'qa_a' in lkm.run(terms)
    assert 'qa_b' in lkm.run(terms)
    assert 'qa_2' in lkm

# Generated at 2022-06-13 14:52:41.949392
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    vars_dictionary = {
        'qz_1': 'hello',
        'qz_2': 'world',
        'qa_1': 'I won\'t show',
        'qz_': 'I won\'t show either'
    }

    name_patterns = "^qz_.+"
    result = LookupModule().run(terms=[name_patterns], variables=vars_dictionary)
    assert result == ['qz_1', 'qz_2']

# Generated at 2022-06-13 14:52:50.388207
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible import constants
    from ansible.module_utils.six import print_

    terms = ['^qz_.+']
    variables = {'qz_1': 'hello', 'qz_2': 'world', 'qa_1': "I won't show"}

    lookup_plugin = LookupModule()
    lookup_plugin.run(terms, variables)
    assert lookup_plugin.get_options() == {'direct': {}, 'var_options': {'qz_1': 'hello', 'qz_2': 'world', 'qa_1': "I won't show"}}


if __name__ == '__main__':
    test_LookupModule_run()

# Generated at 2022-06-13 14:52:57.744355
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Testing class instantiation
    var_lookup = LookupModule()
    var_lookup.set_options()

    # Testing error cases
    test_terms = ['abc', 'abc']
    test_variables = {'abc_1': 'hello', 'abc_2': 'world'}

    # Test case: case 01
    # Error case: invalid setting identifier
    try: 
        var_lookup.run(terms=[1], variables=test_variables)
    except Exception as e:
        assert 'Invalid setting identifier' in e.args[0]

    # Test case: case 02
    # Error case: unable to use search parameter

# Generated at 2022-06-13 14:53:04.066799
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''
    Unit test for method run of class LookupModule.
    '''
    lookup_instance = LookupModule()
    variables = {'var1': 'hello',
                 'var2': 'some',
                 'var3': 'world'}
    asserted_result = ['var1',
                       'var2']
    terms = ['.+']
    result = lookup_instance.run(terms, variables=variables)
    assert asserted_result == result, 'test_LookupModule_run: %s != %s' % (asserted_result, result)

# Generated at 2022-06-13 14:53:13.597986
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import copy
    import ansible.plugins.lookup.varnames as varnames
    from ansible.plugins.lookup import LookupBase
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar

    # Create plugin for test
    lu = varnames.LookupModule()

    # Default arguments
    assert lu.run(terms=[], variables={}) == []

    # Test valid terms
    variables = {
            "qz_1": "hello",
            "qz_2": "world",
            "qa_1": "I won't show",
            "qz_": "I won't show either",
    }

# Generated at 2022-06-13 14:53:20.909613
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test conditions
    terms = ['^qz_.+', '.+_zone$', 'host']
    variable_names = ['qz_1', 'qz_2', 'qa_1', 'qz_', '1_zone', '2_zone', '3_zone']
    expected_output = ['qz_1', 'qz_2', '1_zone', '2_zone', '3_zone']

    # Test object
    lookup_module = LookupModule()

    # Run test and get result
    result = lookup_module.run(terms, variable_names)

    # Assert if test failed
    assert result == expected_output, "%s != %s" % (result, expected_output)



# Generated at 2022-06-13 14:53:30.163212
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:53:41.577049
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit tests for method run of class LookupModule
    """

    # create an instance of LookupModule
    lookup_plugin = LookupModule()

    # create vars
    terms = ["^qz_.+"]
    variables = {"qz_1": "hello"}
    variables["qz_2"] = "world"
    variables["qa_1"] = "I won't show"
    variables["qz_"] = "I won't show either"

    # test result of method run
    got = lookup_plugin.run(terms=terms, variables=variables)
    want = ['qz_1', 'qz_2']
    assert set(want) == set(got)

    # create vars
    terms = ".+_zone$"
    variables = {"zone_1": "hello"}

# Generated at 2022-06-13 14:53:47.564374
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Pre-requisite:
    # Save existing variables for test and restore afterwards
    # This is required because unit tests may call run() of LookupModule multiple times,
    # overwriting the variables and affecting other test results
    saved_variables = dict(__file__=__file__)
    for key in LookupModule.__dict__:
        saved_variables[key] = LookupModule.__dict__[key]

    # Set up test data
    variables = dict(qz_ansible="data_qz_ansible", qa_ansible="data_qa_ansible", qz_ansible_plugin="data_qz_ansible_plugin", qa_ansible_module="data_qa_ansible_module")
    # Set up test terms