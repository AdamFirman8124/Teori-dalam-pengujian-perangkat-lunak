

# Generated at 2022-06-13 14:45:01.946687
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    terms = ['^qz_.+']
    variables = {
        'qz_1':'hello',
        'qz_2':'world',
        'qa_1': "I won't show",
        'qz_': "I won't show either"
        }
    ret = l.run(terms, variables)
    assert(ret == ['qz_1', 'qz_2'])
    terms = ['.+']
    ret = l.run(terms, variables)
    assert(ret == ['qz_1', 'qz_2', 'qa_1', 'qz_'])
    terms = ['hosts']
    ret = l.run(terms, variables)
    assert(ret == [])

# Generated at 2022-06-13 14:45:12.477161
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule().run(["^qz_.+"], {"qz_1": "hello", "qz_2": "world", "qa_1": "I won't show", "qz_": "I won't show either"}) == ["qz_1", "qz_2"]
    assert LookupModule().run([".+"], {"abc": "123", "def": "456"}) == ["abc", "def"]
    assert LookupModule().run(["hosts"], {"hosts_file": "path"}) == ["hosts_file"]

# Generated at 2022-06-13 14:45:23.039765
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils._text import to_text
    from ansible.module_utils import basic

    class Options(object):
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    options = Options(connection=None,
                      module_path=None,
                      forks=None,
                      become=None,
                      become_method=None,
                      become_user=None,
                      check=False,
                      diff=False)

    runner = basic.AnsibleRunner(
        module_name='setup',
        module_args='',
        module_vars={},
        options=options,
        connection=None
    )

    l_module = LookupModule()


# Generated at 2022-06-13 14:45:33.503607
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    result = LookupModule().run(['^qz_.+'], {
        'qz_1': 'hello',
        'qz_2': 'world',
        'qa_1': "I won't show",
        'qz_': "I won't show either",
    })
    assert result == ['qz_1', 'qz_2']

    result = LookupModule().run(['.+'], {
        'aaa': '123',
        'bbb': '456',
        'ccc': '789',
    })
    assert result == ['aaa', 'bbb', 'ccc']


# Generated at 2022-06-13 14:45:43.777983
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Mock the internal method self.get_basedir
    LookupModule.get_basedir = lambda self, variables: '.'

    # Mock the internal method self.get_vars
    class Vars:
        def __init__(self, values):
            self.values = values
        def __getitem__(self, key):
            return self.values[key]

# Generated at 2022-06-13 14:45:53.124731
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test: Simple, boolean success
    lookup_mock = LookupModule()
    lookup_mock.set_options({
        'var_options': {
            'host1': 'host1',
            'host_qz_a': 'host_qz_a',
            'host_qz_b': 'host_qz_b',
            'host_qz_c': 'host_qz_c'
        }
    })
    terms = [ 'host_qz_.+' ]
    assert lookup_mock.run(terms) == [ 'host_qz_a', 'host_qz_b', 'host_qz_c' ]

# Generated at 2022-06-13 14:45:58.300448
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Create mock variables and terms
    terms = ['.+_zone$', '.+_location$']
    variable_names = ['target_zone', 'target_location', 'hostnametest']

    # Instantiate mock lookip plugin
    mock_lookup = MockAnsibleLookup()

    # Execute test target
    results = mock_lookup.run(terms)

    # Assert results is expected
    assert(results == variable_names)


# Generated at 2022-06-13 14:46:02.767392
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Set the class lookup module
    lookup_module = LookupModule()
    # Test the lookup module run method
    assert lookup_module.run(['^1_2_'], {'1_2_d': 'test', '1_2_3d': 'test2'}) == ['1_2_d', '1_2_3d']

# Generated at 2022-06-13 14:46:09.189851
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """ Run method test of class LookupModule """
    lookup = LookupModule()
    term = '^qz_.+'
    variables = {'qz_1': 'hello',
                 'qz_2': 'world',
                 'qa_1': "I won't show",
                 'qz_': "I won't show either"}
    result = lookup.run([term], variables)
    assert(len(result) == 2)
    for i in range(0, 2):
        assert 'qz_' in result[i]

# Generated at 2022-06-13 14:46:18.611964
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class FakeVars(object):
        def __init__(self, *args, **kwargs):
            return

        def __getitem__(self, *args, **kwargs):
            return FakeVars(*args, **kwargs)

        def __contains__(self, *args, **kwargs):
            return True

        def __getattr__(self, *args, **kwargs):
            return True

    def _fake_loader(self, *args, **kwargs):
        return FakeVars()

    lookup_module = LookupModule()
    lookup_module.set_loader = _fake_loader

    assert lookup_module.run(['fake_var']) == ['fake_var']
    assert lookup_module.run(['really_fake_var']) == ['really_fake_var']
    assert lookup_module

# Generated at 2022-06-13 14:46:25.695984
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    plugin_class = LookupModule
    lookup_class_instance = plugin_class()
    # Test case 1
    terms = ["qz_.+"]
    variables = {
        "qz_1": "hello",
        "qz_2": "world",
        "qa_1": "I won't show",
        "qz_": "I won't show either"
    }
    expected_results = ["qz_1", "qz_2"]
    actual_results = lookup_class_instance.run(terms, variables)
    assert expected_results == actual_results
    # Test case 2
    terms = [".+"]

# Generated at 2022-06-13 14:46:34.570309
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup = LookupModule()

    # Test with no variables
    try:
        result = lookup.run(terms=['terms'], variables=None)
        assert result == []
    except AnsibleError:
        pass

    # Test with a list of terms
    variables = {
        'qz_1': 'hello',
        'qz_2': 'world',
        'qa_1': "I won't show",
        'qz_': "I won't show either",
    }
    result = lookup.run(terms=['^qz_.+'], variables=variables)
    assert result == ['qz_1', 'qz_2']

    # Test with match on all variables
    result = lookup.run(terms=['^.+'], variables=variables)

# Generated at 2022-06-13 14:46:43.427539
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit test to check lookup module run method.
    """
    # Test when variables is None
    lookup_module = LookupModule()
    variables = None
    terms = ["hello"]
    kwargs = {"direct": {"demo_regex_term": "hello", "demo_regex_term_two": "world"}}
    try:
        lookup_module.run(terms=terms, variables=variables, **kwargs)
    except Exception as exception_one:
        assert exception_one.args[0] == "No variables available to search"

    # Test when term is empty
    lookup_module = LookupModule()
    variables = {"demo_regex_term": "hello", "demo_regex_term_two": "world"}
    terms = []

# Generated at 2022-06-13 14:46:54.016511
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    #
    # test happy path
    #
    test_obj = LookupModule()
    test_dict = {'a': '1', 'aa': '2', 'b': '3', 'bb': '4', 'c': '5', 'cc': '6', 'ba': '7'}
    terms = ['^a', 'cc$']
    ret_list = test_obj.run(terms, test_dict)
    assert ret_list == ['a', 'aa', 'cc']

    #
    # test error handling
    #
    test_dict = {'a': '1', 'aa': '2', 'cc': '3'}
    try:
        terms = '^a'
        ret_list = test_obj.run(terms, test_dict)
    except AnsibleError as err:
        result = str

# Generated at 2022-06-13 14:47:04.191348
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['^foo.*', 'bar', '.*baz$']
    variables = {
        "foobar": "0",
        "fubar": "0",
        "bar": "0",
        "barfoo": "0",
        "foobaz": "0",
        "baz": "0",
    }
    d = {
        "var_options": variables,
        "direct": {},
    }

    lookup = LookupModule()
    lookup.set_options(var_options=variables, direct=d)
    assert lookup.run(terms, variables) == ["foobar", "bar", "foobaz", "baz"]

    # Case-sensitive test
    variables = {
        "FOOBAR": "0",
        "fooBar": "0",
    }
    assert lookup.run

# Generated at 2022-06-13 14:47:09.037740
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Description: Test to ensure that when a term is searched,
    # the correct variable names are returned

    # Setup lookup module and parameters
    lookup_module = LookupModule()
    lookup_module.set_options(var_options={'x_var': 12, 'xx_var': 12, 'xxx_var': 12, 'y': 12}, direct={})

    # Matching variable names are xxx_var, xx_var, x_var
    terms = ['^x.+']
    result = lookup_module.run(terms)

    # Ensure that all 3 matching variable names are returned
    assert len(result) == 3
    assert 'x_var' in result
    assert 'xx_var' in result
    assert 'xxx_var' in result

# Generated at 2022-06-13 14:47:20.284555
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """ Check that method run returns corretly filtered results """
    lookup_module = LookupModule()
    result = lookup_module.run(['^qz_.+'], variables={
        "qz_1": "hello",
        "qz_2": "world",
        "qa_1": "I won't show",
        "qz_": "I won't show either"})
    assert sorted(result) == ['qz_1', 'qz_2']

    result = lookup_module.run(['.+'], variables={
        "qz_1": "hello",
        "qz_2": "world",
        "qa_1": "I won't show",
        "qz_": "I won't show either"})

# Generated at 2022-06-13 14:47:30.743161
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = [
        '^qz_.+',
        '.+_zone$',
        '.+_location$'
    ]
    variables = {
        'qz_1': 'hello',
        'qz_2': 'world',
        'qa_1': "I won't show",
        'qz_': "I won't show either",
        '1': 'hello',
        '2': 'world',
        'a_1': "I won't show",
        '_': "I won't show either",
        'test_zone': 'hello',
        'test_location': 'world',
        'test_hosts': 'hello',
        'hosts_test': 'hello',
        'hosts': 'hello'
    }

# Generated at 2022-06-13 14:47:41.389303
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    ''' unit test for method run of class LookupModule '''

    lookup_module = LookupModule()

    terms = ['^qz_.+', 'world', '.+_zone$', '.+_location$']
    variables = {'qz_1': 'hello', 'qz_2': 'world', 'qa_1': 'I won\'t show', 'qz_': 'I won\'t show either', 'qz_zone': 'I will show up'}

    try:
        result = lookup_module.run(terms, variables=variables)
        assert result == ['qz_1', 'qz_2', 'qz_zone']
    except AnsibleError as e:
        assert False, 'Unexpected AnsibleError raised: %s' % str(e)

# Generated at 2022-06-13 14:47:42.149389
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 14:47:51.596455
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest

    # Test that if the variable names are not set, an exception is thrown
    lookup = LookupModule()
    with pytest.raises(AnsibleError):
        lookup.run(['network_zone'])

    # Test that if a list of terms is not set, an exception is thrown
    lookup = LookupModule()
    lookup.set_options(var_options={'network_zone': 'TEST'}, direct={})
    with pytest.raises(AnsibleError):
        lookup.run(None)

    # Test that if a search term is not a string, an exception is thrown
    lookup = LookupModule()
    lookup.set_options(var_options={'network_zone': 'TEST'}, direct={})

# Generated at 2022-06-13 14:48:03.124641
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test the run method with different number of arguments:
    # - No arguments
    # - 1 argument
    # - 2 arguments
    # - 3 arguments
    # - 4 arguments

    # Mock the LookupBase class to test the run method of the LookupModule class
    class MockLookupBase(LookupBase):
        def __init__(self, **kwargs):
            self.plugin_name = "Mock"
            self.class_name = "Mock"
            self.caller = "Mock"
            self.set_options(var_options="Mock", direct="Mock")

    # Test the run method of the LookupModule class with no arguments
    def test_LookupModule_run_no_arguments():
        instance = LookupModule()

# Generated at 2022-06-13 14:48:09.031031
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    ret = LookupModule()
    terms = ["^qz_.+"]
    variables = {"qz_1":"hello","qz_2":"world","qa_1":"I won't show","qz_":"I won't show either"}
    assert ret.run(terms,variables) == ['qz_1', 'qz_2']

test_LookupModule_run()

# Generated at 2022-06-13 14:48:16.363407
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l.set_options()
    l.run(["^qz_.+"], variables={"qz_1":"hello", "qz_2":"world", "qa_1":"I won't show"})
    assert l.run(["^qz_.+"], variables={"qz_1":"hello", "qz_2":"world", "qa_1":"I won't show"}) == ["qz_1", "qz_2"]

# Generated at 2022-06-13 14:48:27.581615
# Unit test for method run of class LookupModule
def test_LookupModule_run():
 
    # mock ansible variable
    ansible_master_address = "test_ansible_master"
    
    # mock lookup module
    lookup_module = LookupModule()

    # mock argument terms
    terms = ["test_ansible_master", "test_ansible_agent"]

    # mock variable
    variables = dict(ansible_master_address = "test_ansible_master", ansible_agent_address = "test_ansible_agent")

    # call run
    ret = lookup_module.run(terms, variables)

    # assert the result
    assert "ansible_master_address" in ret
    assert "ansible_agent_address" in ret
    assert "ansible_master_address" == ret[0]
    assert "ansible_agent_address" == ret[1]

# Generated at 2022-06-13 14:48:37.285799
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''
    Test Class LookupModule
    '''
    lp_obj = LookupModule()
    # lp_obj._templar = None
    variable_names = {"f1": "var1-value", "f2": "var2-value", "f3": "var3-value"}
    # Test case 1
    # expected_result = [u'f1', u'f2', u'f3']
    result = lp_obj.run(["."], variable_names)
    assert result == [u'f1', u'f2', u'f3']

    # Test case 2
    result = lp_obj.run(["^f.+"], variable_names)
    assert result == [u'f1', u'f2', u'f3']


    # Test case 3
   

# Generated at 2022-06-13 14:48:45.747810
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.plugins.lookup import LookupModule

    var1 = dict(var1value1="foo", var2value2="bar")
    var2 = [
        'ansible', 'python', 'varnames', 'plugins'
    ]

    #test with array of terms
    lookup_result = LookupModule().run(terms=var2, variables=var1, **{})
    assert sorted(lookup_result) == sorted(['var1value1', 'var2value2'])

    #test with string as a term
    lookup_result = LookupModule().run(terms=['var.+'], variables=var1, **{})
    assert sorted(lookup_result) == sorted(['var1value1', 'var2value2'])

    #test with a None value
    lookup_result = LookupModule

# Generated at 2022-06-13 14:48:55.247295
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test for standard use
    test_LookupModule = LookupModule()
    assert test_LookupModule.run(terms=['^qz_.+'], variables={'qz_1': 'hello', 'qz_2': 'world', 'qa_1': 'I won\'t show', 'qz_': 'I won\'t show either'}) == ['qz_1', 'qz_2']

    # Test for exceptions
    test_LookupModule = LookupModule()
    try:
        test_LookupModule.run(terms=['^qz_.+'], variables=None)
    except AnsibleError as e:
        assert str(e) == 'No variables available to search'

    test_LookupModule = LookupModule()

# Generated at 2022-06-13 14:49:04.827523
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''
    Unit tests for method LookupModule.run.
    '''

    # Test that a non-string value in terms returns error message.
    variables = {'var1': 'hello', 'var2': 'world', 'var3': 'goodbye'}
    terms = [2]
    lookup_module = LookupModule()
    run_result = lookup_module.run(terms, variables)
    assert(run_result[0] == 'Invalid setting identifier, "2" is not a string, it is a <class \'int\'>')

    # Test that a string value in terms is matched against variable name.
    terms = ['var1']
    lookup_module = LookupModule()
    run_result = lookup_module.run(terms, variables)
    assert(run_result == ['var1'])

    # Test regex pattern

# Generated at 2022-06-13 14:49:15.200709
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()
    variable_list = {"qa_1": "I won't show"}
    variable_list.update({"qz_1": "hello"})
    variable_list.update({"qz_2": "world"})
    variable_list.update({"qz_": "I won't show either"})
    variable_list.update({"qa_zone": "I won't show"})
    variable_list.update({"qz_zone": "hello"})
    variable_list.update({"qz_location": "world"})
    variable_list.update({"qz_": "I won't show either"})
    variable_list.update({"hosts_zone": "hosts match"})

# Generated at 2022-06-13 14:49:31.425191
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_object = LookupModule()

    # Test run for a single term
    terms = [
        '^qz_.',
    ]
    variables = {
        'qz_1': 'hello',
        'qz_2': 'world',
        'qa_1': "I won't show",
        'qz_': "I won't show either",
    }
    ret = lookup_object.run(terms, variables=variables)
    assert ret == ['qz_1', 'qz_2'], ret

    # Test run for multiple terms
    terms = [
        '^qz_.',
        '.+_zone$',
        '.+_location$'
    ]

# Generated at 2022-06-13 14:49:38.339824
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit test for method run of class LookupModule
    """

    # Variables to test
    variables = {
        'test_variable': 1,
        'test:variable:2': 2,
        'testvariable2': 3,
        'test': 4,
        'testvariable3': 5,
        'test_variable': 6,
        'test_variables': 7,
    }

    # Expected results
    test_expected = [
        'test_variable',
        'test:variable:2',
        'testvariable2',
        'test',
        'testvariable3',
        'test_variable',
    ]

    test = {
        '_terms': ['^test_.+$'],
        'variables': variables,
    }
    result = LookupModule().run(**test)
   

# Generated at 2022-06-13 14:49:44.201147
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_variables = {
        "qz_test_var_1": "Hello World!",
        "qz_test_var_2": "Hello World Again!",
        "test_var_1": "This will not show",
        "qa_test_var_2": "This will not show either",
        "qz_test_var": "This will not show because of trailing underscore"
    }

    lookup_module = LookupModule()
    result = lookup_module.run(["^qz_.+"], variables=test_variables)

    assert "['qz_test_var_1', 'qz_test_var_2']" == str(result)

    result = lookup_module.run([".+"], variables=test_variables)

    assert len(result) == len(test_variables.keys())

   

# Generated at 2022-06-13 14:49:52.632590
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    variables = {'qz_1': 'hello', 'qz_2': 'world', 'qa_1': "I won't show", 'qz_': "I won't show either"}
    list_of_var_names = module.run(terms=['^qz_.+'], variables=variables, **{'ANXS_VAR_NAME': 'qz_3'})
    assert list_of_var_names == ['qz_1', 'qz_2', 'qz_']

# Generated at 2022-06-13 14:50:00.745038
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # see https://docs.python.org/3/library/unittest.mock.html
    from unittest.mock import patch
    from ansible.module_utils._text import to_native

    with patch('ansible.plugins.lookup.varnames.AnsibleError', side_effect=Exception):
        terms = ['alerts\\.yml']
        variables = {'alerts.yml': '', 'hosts': '', 'hosts.yml': ''}
        try:
            lm = LookupModule()
            lm.run(terms, variables)
            assert False
        except Exception as e:
            assert 'is not a string, it is a <class' in to_native(e)


# Generated at 2022-06-13 14:50:06.221333
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    vars = {
        'qz_1': 'hello',
        'qz_2': 'world',
        'qa_1': "I won't show",
        'qz_': "I won't show either"
    }
    assert lm.run(['^qz_.+'], vars) == ['qz_1', 'qz_2']

# Generated at 2022-06-13 14:50:07.172260
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert False

# Generated at 2022-06-13 14:50:14.201885
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    lookup.set_runner(RunnerMock())
    lookup.set_loader(LoaderMock())

    assert lookup.run(terms=['host']) == ['host']
    assert lookup.run(terms=['host','group']) == ['host','group']
    assert lookup.run(terms=['h.+t']) == ['host', 'hot']
    assert lookup.run(terms=['h.+t'], variables={'host':'1', 'hot':'2', 'cold':'3'}) == ['host', 'hot']


# Generated at 2022-06-13 14:50:24.180426
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    filenames = ['blob_azure_account_key',
                 'blob_azure_sas_token',
                 'blob_data',
                 'blob_name',
                 'blob_path',
                 'bson_data',
                 'fail_on_found',
                 'fail_on_missing',
                 'search_regex',
                 'validate_certs']

    lookup_mgr = LookupModule()

    # Search using one pattern and a vars list
    result = lookup_mgr.run(terms=['^blob.+'], variables=filenames)
    assert result == ['blob_azure_account_key', 'blob_azure_sas_token', 'blob_data', 'blob_name', 'blob_path']

    # Search using one

# Generated at 2022-06-13 14:50:34.123225
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    ##############################################################################
    # Dummy variables and objects for testing method run of class LookupModule.  #
    ##############################################################################
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list=['127.0.0.1'])
    variable_manager.set_inventory(inventory)

# Generated at 2022-06-13 14:50:46.890649
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    print("Testing LookupModule.run")
    lookup = LookupModule()
    assert type(lookup.run(['.+_zone$', '.+_location$'])) == list

# Generated at 2022-06-13 14:50:54.960337
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # unit test: test failure of LookupModule.run when 'term' is not a string,
    #            testing 'term' is a list
    term = ['qz_', 'qa_']
    lookup_module = LookupModule()
    assert 'Invalid setting identifier, "%s" is not a string, it is a %s' % (term, type(term)) in lookup_module.run(term)

    # unit test: test failure of LookupModule.run when 'term' is not a string,
    #            testing 'term' is a tuple
    term = ('qz_', 'qa_')
    assert 'Invalid setting identifier, "%s" is not a string, it is a %s' % (term, type(term)) in lookup_module.run(term)

    # unit test: test failure of LookupModule.run when 'term'

# Generated at 2022-06-13 14:51:01.844106
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.vars import combine_vars
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    variables = combine_vars(dict(qz_1=AnsibleUnsafeText('hello')), dict(qz_2=AnsibleUnsafeText('world')))

    l = LookupModule()
    l.set_options(var_options=variables, direct=dict())

    assert l.run(['^qz_.+']) == ['qz_2', 'qz_1']
    assert l.run(['.+']) == ['qz_2', 'qz_1']
    assert l.run(['hosts']) == []

# Generated at 2022-06-13 14:51:10.962461
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    # Test function run
    # Testing 1st example
    terms = ['^qz_.+']
    variables = {'qz_1': 'hello', 'qz_2': 'world', 'qa_1': "I won't show", 'qz_': "I won't show either", 'qz_aaa': 'hello'}
    result = lookup_module.run(terms, variables)
    assert result == ['qz_1', 'qz_2', 'qz_aaa']

    # Testing 2nd example
    terms = ['.+']
    result = lookup_module.run(terms, variables)
    assert result == variables

    # Testing 3rd example
    terms = ['hosts']
    result = lookup_module.run(terms, variables)
    assert result == []

    variables

# Generated at 2022-06-13 14:51:17.358225
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    variables = dict(b=1, c=1, abc=1, ab=1, a=1, abcd=1, d=1, ef=1, efg=1, abe=1, f=1, efgh=1)

    expected = ['a', 'ab', 'abc', 'abcd', 'abe', 'ef', 'efg', 'efgh']

    lm = LookupModule()
    lm.run_terms = ["^[ab].+", "ef.+"]
    r = lm.run(lm.run_terms, variables=variables)

    assert r == expected, "Expected {}, got {}".format(expected, r)

# Generated at 2022-06-13 14:51:26.261072
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test sceanrio with `variables` as None
    lm = LookupModule()
    lm.set_options()
    terms = ['^qz_.+']
    try:
        lm.run(terms, variables=None)
    except AnsibleError as e:
        actual = e.message
        expected = 'No variables available to search'
        assert actual == expected

    # Test sceanrio with `term` as not string type
    lm = LookupModule()
    lm.set_options()
    terms = ['^qz_.+', 2]
    try:
        lm.run(terms, variables=None)
    except AnsibleError as e:
        actual = e.message
        expected = 'Invalid setting identifier, "2" is not a string, it is a %s' % type(2)

# Generated at 2022-06-13 14:51:36.625971
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lu = LookupModule()
    ret = lu.run(terms='^qz_.+', variables={'qz_1': 'hello', 'qz_2': 'world',
                                           'qa_1': "I won't show", 'qz_': "I won't show either"})
    assert ret == ['qz_1', 'qz_2']

    ret = lu.run(terms='.+', variables={'qz_1': 'hello', 'qz_2': 'world',
                                           'qa_1': "I won't show", 'qz_': "I won't show either"})
    assert len(ret) == 4


# Generated at 2022-06-13 14:51:41.348244
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Example of unit test for lookup varnames
    # - use a plugin to mock the variables
    # - create a list of terms
    # - create a list of expected results
    # - run the lookup plugin and validate results
    from ansible.template import Templar, AnsibleEnvironment
    from ansible.vars import VariableManager

    # Create a plugin that mocks the variables and return them
    class VariablesPlugin(object):
        def __init__(self):
            self._variables = {}

        def set_options(self, var_options=None, direct=None):
            return

        def run(self, terms, variables=None, **kwargs):
            self._variables = variables
            return self._variables

    # Prepare the list of terms

# Generated at 2022-06-13 14:51:49.084850
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    # Assert that it returns variable names if patterns match
    assert lookup_module.run(['.+'], variables={'1': 1, '2': 2}) == ['1', '2']
    assert lookup_module.run(['2'], variables={'1': 1, '2': 2}) == ['2']
    assert lookup_module.run(['1', '2'], variables={'1': 1, '2': 2}) == ['1', '2']

    # Assert that it returns variable names if one of the patterns match
    assert lookup_module.run(['2', '.+'], variables={'1': 1, '2': 2}) == ['1', '2']

# Generated at 2022-06-13 14:51:58.128038
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    # Unit test for set_options passing a variables dict
    lookup_module.set_options(var_options={'test': 'pass'}, direct={})
    # Unit test for set_options with no variables dict
    try:
        lookup_module.set_options(var_options=None, direct={})
        assert False
    except AnsibleError:
        assert True
    # Unit test for set_options with no direct
    try:
        lookup_module.set_options(var_options={'test': 'pass'}, direct=None)
        assert False
    except AnsibleError:
        assert True
    # Unit test for set_options with both variables and direct
    lookup_module.set_options(var_options={'test': 'pass'}, direct={'test2': 'pass'})


# Generated at 2022-06-13 14:52:29.049562
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    args = {
        '_terms': ['^qz_.+'],
        '_variables': {
            'qz_1': 'hello',
            'qz_2': 'world',
            'qa_1': "I won't show",
            'qz_': "I won't show either",
        },
        '_options': {},
        '_ansible_check_mode': False,
        '_ansible_debug': False,
        '_ansible_diff': False,
        '_ansible_keep_remote_files': False,
        '_ansible_no_log': False,
        '_ansible_verbosity': 3,
    }
    module = LookupModule()
    module.set_options(var_options=args['_variables'], direct=args['_options'])

# Generated at 2022-06-13 14:52:37.506165
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()
    terms = ['.+_zone$', '.+_location$']
    variables = {
        'env': 'test',
        'prod_zone': 'us-east1-b',
        'prod_location': 'us-east1',
        'test_zone': 'us-west1-b',
        'test_location': 'us-west1',
        'db_zone': 'us-west1-a',
        'db_location': 'us-west1'}
    result = lookup_plugin.run(terms, variables)
    assert result == ['prod_zone', 'prod_location', 'test_zone', 'test_location', 'db_zone', 'db_location']

# Generated at 2022-06-13 14:52:42.992034
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    variables = {'item1': 10,
                 'item2': 50}
    terms1 = ['i.+']
    return_value1 = lookup_module.run(terms1, variables)
    assert return_value1 == ['item1', 'item2']
    return_value2 = lookup_module.run(terms1, variables, item1=20)
    assert return_value2 == ['item2']

# Generated at 2022-06-13 14:52:52.445567
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory

    import ansible.constants as C
    C.DEFAULT_VAULT_ID_MATCH = '.*'

    variable_manager = VariableManager()
    variable_manager.extra_vars = {
        'qz_1': 'hello',
        'qz_2': 'world',
        'qa_1': "I won't show",
        'qz_': "I won't show either",
        'hosts': 'foo',
    }

    lm = LookupModule()

    # a lookup with a single term
    terms = ['^qz_.+']

# Generated at 2022-06-13 14:52:57.250729
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    try:
        # Test ansible.parsing.yaml.objects.AnsibleVaultEncryptedUnicode not supported
        from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
        testAnsibleVaultEncryptedUnicode = AnsibleVaultEncryptedUnicode('value')
    except ImportError:
        # Python 3
        from ansible.parsing.vault import VaultLib
        m = VaultLib(None, None)
        testAnsibleVaultEncryptedUnicode = m.encrypt('value')



# Generated at 2022-06-13 14:53:03.379873
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    var1 = {'var1': 'test'}
    var2 = {'var2': 'test'}
    var3 = {'var3': 'test'}
    var4 = {'var4': 'test'}
    var5 = {'var5': 'test'}
    var6 = {'var6': 'test'}

    l1 = LookupModule({}, var1)
    assert l1.run(['var1']) == ['var1']

    l2 = LookupModule({}, var2)
    assert l2.run(['var']) == ['var2']

    l3 = LookupModule({}, var3)
    assert l3.run(['var.+']) == ['var3']

    l4 = LookupModule({}, var4)

# Generated at 2022-06-13 14:53:13.094222
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # FixMe: After a unit test is written, move the function to test_utils/plugins/module_utils/varnames.py
    from ansible.module_utils import plugins
    from ansible.module_utils.plugins import varnames as vars_list
    import os
    import sys

    # Change current directory to ansible directory, because we need its library
    ansible_path = os.path.join(os.getcwd(), "..")
    if os.path.exists(ansible_path):
        os.chdir(ansible_path)
    ansible_path = os.path.join(os.getcwd(), "..")
    if os.path.exists(ansible_path):
        os.chdir(ansible_path)

    # Append ansible/lib to path
    ansible_

# Generated at 2022-06-13 14:53:19.020821
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class Struct:
        pass

    m = Struct()
    m.run_command = lambda *args, **kwargs: ['hello', 'world']
    m.get_bin_path = lambda *args, **kwargs: None

    pattern = re.compile('world')
    print("hello world".split())
    print("hello world".split()[0])
    print("hello world".split()[0].find("hello"))
    m.run("hello world".split())
    a = ["hello", "world"]
    if a[0].find("hello"):
        print("hello")
    elif a[0].find("world"):
        print("world")
    elif a[1].find("world"):
        print("world")
    else:
        print("exiting")


# Generated at 2022-06-13 14:53:25.389940
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    vars = {'qz_1': 'hello', 'qz_2': 'world', 'qa_1': "I won't show", 'qz_': "I won't show either"}
    terms = ['^qz_.+', '^qa_.+']
    results = lookup.run(terms, vars)
    assert(len(results) == 4)
    assert('qz_1' in results)
    assert('qz_2' in results)
    assert('qz_' in results)
    assert('qa_1' in results)
    #Test whether empty pattern is searched
    results = lookup.run([''], vars)
    assert(len(results) == 0)
    #Test whether invalid pattern is searched

# Generated at 2022-06-13 14:53:27.054743
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert(False), "No test for LookupModule.run() method"

# Generated at 2022-06-13 14:54:17.287921
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l.set_options()

    assert l.run([]) == [], "Unexpected result"

    l.set_options(var_options={'firstkey': 'firstvalue', 'secondkey': 'secondvalue'}, direct={})

    assert l.run(['firstkey']) == ['firstkey'], "Unexpected result"
    assert l.run(['firstkey', 'secondkey']) == ['firstkey', 'secondkey'], "Unexpected result"
    assert l.run(['firstkey', 'secondkey', 'thirdkey']) == ['firstkey', 'secondkey'], "Unexpected result"
    assert l.run(['secondkey', 'firstkey']) == ['firstkey', 'secondkey'], "Unexpected result"


# Generated at 2022-06-13 14:54:24.841134
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    variables = {'hosts': ['host1', 'host2', 'host3']}
    result = lookup_module.run(['hosts'], variables)
    assert result == ['hosts']

    lookup_module = LookupModule()
    variables = {'hosts': ['host1', 'host2', 'host3'], 'host': 'host'}
    result = lookup_module.run(['^h.+'], variables)
    assert result == ['host', 'hosts']

    lookup_module = LookupModule()
    variables = {'hosts': ['host1', 'host2', 'host3'], 'host': 'host'}
    result = lookup_module.run(['^h.+', 'ost'], variables)

# Generated at 2022-06-13 14:54:34.366439
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:54:43.393158
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = "^qz_.+"
    lookup_local = LookupModule()

# Generated at 2022-06-13 14:54:48.145762
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    result = set(LookupModule().run(['^qz_.+'], variables={'qz_1': 'hello', 'qz_2': 'world', 'qa_1': 'I wont show', 'qz_': 'I wont show either'}))
    expected = set(['qz_1', 'qz_2'])
    assert result == expected


# Generated at 2022-06-13 14:54:55.136983
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.plugins.lookup.varnames import LookupModule

    lookup_module = LookupModule()
    # unit test: run should return empty list if no variables available
    result = lookup_module.run(['^qz_.+'])
    assert result == []

    # unit test: run should raise AnsibleError if not passed a list
    variables = dict()
    variables['qz_1'] = 'hello'
    variables['qz_2'] = 'world'
    variables['qa_1'] = "I won't show"
    variables['qz_'] = "I won't show either"
    result = lookup_module.run(variables, variables)
    assert result == ['qz_1', 'qz_2']