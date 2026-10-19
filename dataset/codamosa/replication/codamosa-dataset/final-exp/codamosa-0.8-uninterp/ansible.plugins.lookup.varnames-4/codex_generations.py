

# Generated at 2022-06-13 14:45:03.592895
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    test_terms = ('^qz_.+', 'hosts', '.+_zone$', '.+_location$')
    test_variables = {'qz_1': 'hello', 'qz_2': 'world', 'qa_1': "I won't show", 'qz_': "I won't show either"}

    # Test with no variables
    try:
        ret = LookupModule.run(test_terms, variables=None)
        assert False
    except AnsibleError as error:
        assert error.message == "No variables available to search"

    ret = LookupModule.run(test_terms, variables=test_variables)
    assert isinstance(ret, list)
    assert ret == ['qz_1', 'qz_2'], 'ret: {ret}'.format(ret=ret)
    return



# Generated at 2022-06-13 14:45:08.293190
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    result = LookupModule().run(terms=['^qz_.+'], variables={'qz_1': 'hello', 'qz_2': 'world', 'qa_1': "I won't show", 'qz_': "I won't show either"})
    assert result == ['qz_1', 'qz_2']

# Generated at 2022-06-13 14:45:14.350630
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Check whether the method run() produces the same result as the command
    output on the terminal.
    """
    import json
    
    import ansible.plugins.lookup.varnames
    import ansible.vars.manager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.host import Host

    dataloader = DataLoader()
    variables = VariableManager(loader=dataloader)
    inventory = InventoryManager(loader=dataloader, sources=['./inventory'])
    host = Host(name="local")
    inventory._hosts_cache['local'] = host
    inventory.set_variable(host, 'my_var1', 'hello')
   

# Generated at 2022-06-13 14:45:22.892529
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class SearchResult():
        def search(self, term):
            # term is the regex string
            if term == "^qz_.+" :
                # returns true if the regex matches, false otherwise
                return True
            return False

    class LookupModuleMock(LookupModule):
        def __init__(self):
            pass

    def mock_re_search(search_string):
        # search_string is the regex string
        sr = SearchResult()
        return sr.search(search_string)

    #mock the re module.
    #Create a mock object of the re.search method
    #to test the return value of the run method.
    orig_search = re.search
    re.search = mock_re_search


# Generated at 2022-06-13 14:45:33.395572
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test declaration and import
    test_LookupModule_run.success = True
    test_LookupModule_run.error = ''
    import sys
    import os
    import inspect
    import re

    # AnsibleLookup/ansible/plugins/lookup/varnames.py
    modulename = 'ansible/plugins/lookup/varnames.py'

    # AnsibleLookup/ansible/plugins/lookup/
    plugin_dir = os.path.join(os.path.dirname(__file__), '..', '..', '..')

    if plugin_dir not in sys.path:
        sys.path.append(plugin_dir)

    # AnsibleLookup/ansible/plugins/

# Generated at 2022-06-13 14:45:43.707134
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Create an instance of the class LookupModule
    lookup_module = LookupModule()

    # Test without variables available to search
    res = lookup_module.run(['foo'])

    # Should return error
    assert isinstance(res, AnsibleError)

    # Test with valid names that matches against search
    res = lookup_module.run(['a'], variables={'a': 1})
    assert res == ['a']

    # Test with valid names that matches against search (multiple)
    res = lookup_module.run(['a'], variables={'a': 1, 'b': 2, 'c': 3})
    assert res == ['a']

    # Test with valid names that does not matches against search
    res = lookup_module.run(['a'], variables={'b': 2})
    assert res == []

    # Test

# Generated at 2022-06-13 14:45:49.323709
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # instantiate object under test
    lookup = LookupModule()
    # create mocks
    class mock_variables():
        def keys(self):
            return ['a', 'b', 'c']
    # call method under test
    ret =  lookup.run(['a'], mock_variables())
    # set asserts
    assert ret == ['a']


# Generated at 2022-06-13 14:45:58.567634
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    all_vars = {
        'qz_1': "hello",
        'qz_2': "world",
        'qa_1': "I won't show",
        'qz_': "I won't show either"
    }
    print("Running unittest on method run of class LookupModule ...", end='')
    module = LookupModule()
    assert module.run(['^qz_.+'], variables=all_vars) == ['qz_1', 'qz_2']
    assert len(module.run(['.+'], variables=all_vars)) == 4
    assert len(module.run(['hosts'], variables={})) == 0

# Generated at 2022-06-13 14:46:04.993214
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()
    variables = {'nagios_contacts': [{'nagios_contact_name': '', 'nagios_contact_email': 'admin@example.com', 'nagios_contact_pager': ''}]}
    terms = ['nagios_contact_name', 'nagios_contact_email']
    result = lookup_plugin.run(terms, variables)
    assert(result == ['nagios_contact_name', 'nagios_contact_email'])

# Generated at 2022-06-13 14:46:09.073806
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    my_vars = dict(
        cat="maine",
        dog="labs",
        fish="",
      )

    # Uses the __init__ method
    my_lookup = LookupModule(None, my_vars)

    my_lookup.run(terms="^cat$", variables = my_vars)

# Generated at 2022-06-13 14:46:21.990065
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={
        'terms': {'type': 'list', 'required': True},
    })

    module.params = {
        'terms': ['.+_zone$', '.+_location$'],
        'variables': {
            'aws_ec2_zone': 'test',
            'aws_ec2_location': 'test',
            'test': 'test',
        },
    }
    assert 'aws_ec2_zone' in LookupModule().run(**module.params)[0]
    assert 'aws_ec2_location' in LookupModule().run(**module.params)[0]

# Generated at 2022-06-13 14:46:29.030785
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    inventory = Inventory(loader=loader, variable_manager=VariableManager(loader=loader), host_list=[])
    vm = inventory.get_variable_manager()

    assert vm.get_vars() == {}

    # The following variables will be used in test cases
    vm.set_variable('qaz_1', 'hello')
    vm.set_variable('qaz_2', 'world')
    vm.set_variable('qaz_3', 'howdy')
    vm.set_variable('qa_1', "I won't show")
    vm.set_variable('qaz_', "I won't show either")

# Generated at 2022-06-13 14:46:38.283079
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # unit test for method run on class LookupModule
    #   def run(self, terms, variables=None, **kwargs):

    # return
    #   _value:
    #     description:
    #       - List of the variable names requested.
    #     type: list

    # parameters:
    #   terms:
    #     description: List of Python regex patterns to search for in variable names.
    #     required: True
    #     type: str or list
    #   variables:
    #     description: The variables availables to search
    #     type: dict
    #   kwargs:
    #     description: Additional keyword arguments passed to the Ansible moudle

    # test setup
    #
    # terms
    terms = ['^qz_.+', '^qa_.+', '^qz_.+']



# Generated at 2022-06-13 14:46:44.751571
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    helper = LookupModule()
    helper.set_options(var_options={'qz_1': 'hello', 'qz_2': 'world', 'qa_1': "I won't show", 'qz_': "I won't show either"})
    qz_list = helper.run(terms=['^qz_.+'], variables={'qz_1': 'hello', 'qz_2': 'world', 'qa_1': "I won't show", 'qz_': "I won't show either"}, direct={})
    assert qz_list == ['qz_2', 'qz_1']

# Generated at 2022-06-13 14:46:45.886104
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert False, "A unit test is required"

# Generated at 2022-06-13 14:46:56.471397
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test with a variable that should not match
    test_vars = {'var_should_not_match': {}}
    lookup_ret = LookupModule().run(['random_variable_name'], variables=test_vars)
    assert lookup_ret == []

    # Test with a variable that should match
    test_vars = {'testvar': {}}
    lookup_ret = LookupModule().run(['testvar'], variables=test_vars)
    assert lookup_ret == ['testvar']

    # Test with a variable that should not match
    test_vars = {'test_1': {}}
    lookup_ret = LookupModule().run(['^test_2$'], variables=test_vars)
    assert lookup_ret == []

    # Test with a variable that should match
    test_v

# Generated at 2022-06-13 14:47:05.940177
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Create a LookupModule
    lookup_module = LookupModule()

    # Set up variables
    terms = ['qz_', '^qz_.+', '^((?!z).)*$', '^((?!z).)*$', '^((?!z$).)*$']
    var_options = {
        "qz_1": "hello",
        "qz_2": "world",
        "qa_1": "I won't show",
        "qz_": "I won't show either",
        "q_1": "I will show"
    }
    variables = {"test": var_options}

    # Run the lookup_module.run(...)
    results = lookup_module.run(terms, variables)
    # Check results for each term
    assert "qz_1" in results

# Generated at 2022-06-13 14:47:11.160477
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    module = LookupModule()
    variables = {"qa_1": "I won't show",
                 "qz_1": "hello",
                 "qz_2": "world",
                 "qz_": "I won't show either"}

    assert sorted(module.run(["^qz_.+"], variables=variables)) == sorted(["qz_1", "qz_2"])
    assert sorted(module.run([".+"], variables=variables)) == sorted(variables.keys())
    assert sorted(module.run(["hosts"], variables=variables)) == []
    assert sorted(module.run([".+_zone$", ".+_location$"], variables=variables)) == []

# Generated at 2022-06-13 14:47:19.136389
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    terms = [r'.+_zone$', r'.+_location$']
    variables = {
        'azure_zone': 'azure_zone',
        'azure_location': 'azure_location',
        'amazon_zone': 'amazon_zone',
        'amazon_location': 'amazon_location'
    }

    variable_names = list(variables.keys())
    
    lookup_module = LookupModule()
    result = lookup_module.run(terms, variables)

    for i in variable_names:
        assert i in result

# Generated at 2022-06-13 14:47:29.553879
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Tests when matches exist.
    lookup = LookupModule()
    assert lookup.run(['^qz_.+'], {'qz_1':'hello', 'qz_2':'world', 'qa_1':'I won\'t show'}) == ['qz_1', 'qz_2']

    # Tests when no matches.
    lookup = LookupModule()
    assert lookup.run(['^qa_.+'], {'qz_1':'hello', 'qz_2':'world', 'qa_1':'I won\'t show', 'qz_':'I won\'t show either'}) == []

    # Tests when there are multiple matches for all terms.
    lookup = LookupModule()

# Generated at 2022-06-13 14:47:41.947679
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test parameters
    terms = ['^qz_.+', '^qa_.+']
    variables = {'qz_1': 'hello', 'qz_2': 'world', 'qa_1': 'I won\'t show', 'qz_': 'I won\'t show either'}

    # Run LookupModule(lookup='varnames')
    lookup = LookupModule()
    ret = lookup.run(terms, variables)

    # Assert result
    assert ret == ['qz_1', 'qz_2']

# Generated at 2022-06-13 14:47:50.648269
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # test_run_01: LookupModule_run test with no variables defined
    # Should raise AnsibleError: No variables available to search
    lookup = LookupModule()
    with pytest.raises(AnsibleError):
        lookup.run(['xyz'])

    # test_run_02: LookupModule_run test with no terms defined
    # Should return empty list []
    lookup = LookupModule()

# Generated at 2022-06-13 14:48:02.484409
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lu = LookupModule()

    # Comparison of a simple pattern
    ret = lu.run(terms=['^qa_.+'], variables={'qa_1': 'hello', 'qa_2': 'world', 'qb_1': 'I won\'t show'})
    assert ret == ['qa_1', 'qa_2']

    # Comparison of several patterns
    ret = lu.run(terms=['^qa_.+', '.+b$'], variables={'qa_1': 'hello', 'qa_2': 'world', 'qb_1': 'I won\'t show'})
    assert ret == ['qa_1', 'qa_2', 'qb_1']

    # Comparison of a pattern with a non string object

# Generated at 2022-06-13 14:48:03.462347
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # This is a function, not a class
    pass

# Generated at 2022-06-13 14:48:15.713821
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Unit test for method 'run' of the lookup module varnames
    assert("lorem" in LookupModule().run(['^z.+'], {'zebra': 'lorem'}))
    assert("ipsum" not in LookupModule().run(['^z.+'], {'aardvark': 'ipsum'}))

    assert("ipsum" in LookupModule().run(['^.+m$'], {'aardvark': 'ipsum'}))
    assert("dolor" not in LookupModule().run(['^.+m$'], {'aardvark': 'dolor'}))

    assert("lorem" in LookupModule().run(['^o.+'], {'zebra': 'lorem', 'rhinoceros': 'ipsum'}))

# Generated at 2022-06-13 14:48:22.743733
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Test Ansible lookup class LookupModule using the run() method.
    """

    # Test case 1
    # Inputs
    #
    # - No regex search terms
    # - No variables
    #
    # Expected results
    #
    # - Expect an Ansible error
    #
    # Test set up
    test_terms = []
    variables = {}
    expected_result = {
        'lookup_error': {
            'msg': 'No variables available to search'
        }
    }

    # Do the test
    lookup_instance = LookupModule()
    result = lookup_instance.run(terms=test_terms, variables=variables)

    # Determine if test passed
    assert result == expected_result

    # Test case 2
    # Inputs
    #
    # - Regex search

# Generated at 2022-06-13 14:48:33.956518
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup import LookupModule
    from ansible.module_utils._text import to_bytes

    terms = [to_bytes('^v.+'), to_bytes('.+_zone$'), to_bytes('.+_location$')]

# Generated at 2022-06-13 14:48:43.624523
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    def mock_template_vars(self, templar, variables, fail_on_undefined=False, depth=0):
        return variables

    variables = {'name_zone': 'toto', 'name_location': 'tata'}

    lookup_module = LookupModule()
    lookup_module.set_options = mock_template_vars

    assert lookup_module.run(['^name_.+$'], variables) == ['name_zone', 'name_location']

    # Exception handling
    lookup_module.set_options = None
    try:
        lookup_module.run(['^name_.+$'], variables)
        assert False
    except Exception as e:
        assert str(e) == 'No variables available to search'

    # Exception handling

# Generated at 2022-06-13 14:48:53.431221
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # We don't do anything fancy here, we just want to ensure that the method
    # takes the arguments we expect and returns what we expect.

    terms = ['^qz_.+', 'hosts', '.+_zone$', '_location$']
    variables = {
        'qz_1': 'hello',
        'qz_2': 'world',
        'qa_1': "I won't show",
        'qz_': "I won't show either",
        'my_hosts': 'localhost',
        'my_host_connection': 'loopback',
        'my_zone': 'my_zone',
        'my_region': 'my_region',
    }

    # Create a fake subclass of LookupBase. We do this because we just want to
    # test the run method, and don't care about anything else.

# Generated at 2022-06-13 14:49:04.076412
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import pytest

    data = {
        "disc": {
            "device": "/dev/null",
            "fstype": "tmpfs",
            "mode": "1777",
            "opts": "defaults,noatime,mode=1777",
            "owner": "root",
            "size": "100%"
        },
        "hostname": "test-vars-lookup",
        "partitions": {
            "/": {
                "device": "/dev/sda2",
                "fstype": "xfs",
                "mode": "0700",
                "opts": "defaults,noatime,usrquota",
                "owner": "root",
                "size": "100%"
            }
        }
    }

    module = LookupModule()


# Generated at 2022-06-13 14:49:23.974457
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup.varnames import LookupModule
    lookup = LookupModule()
    variables = {"host_hostname": "host01", "host_ip": "1.1.1.1", "ansible_host": "1.1.1.2"}
    result = lookup.run(terms=["host"], variables=variables)
    assert result == ["host_hostname", "host_ip", "ansible_host"]
    result = lookup.run(terms=["_host$"], variables=variables)
    assert result == ["host_hostname"]


# Generated at 2022-06-13 14:49:26.380117
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    assert lookup.run(['vars'], variables={'vars': 'blah'}) == ['vars']

# Generated at 2022-06-13 14:49:34.594440
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    assert lm.run([], {}) == []
    assert lm.run(['a'], {}) == []
    with pytest.raises(AnsibleError):
        lm.run(['a'], {'a': 1})
    assert lm.run(['a.*'], {'a': 1}) == []
    assert lm.run(['a.*'], {'a': 1, 'a1': 1}) == ['a1']
    assert lm.run(['a.*'], {'a': 1, 'a1': 1, 'a2': 1, 'b1': 1}) == ['a1', 'a2']



# Generated at 2022-06-13 14:49:41.464263
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test data
    terms = ['qz_.+$', 'abc$']
    variables = {
        "qz_1": "hello",
        "qz_2": "world",
        "qa_1": "I won't show",
        "qz_": "I won't show either",
        "abc": "I will show"
    }

    # Unit test
    m = LookupModule()
    assert m.run(terms, variables) == ["qz_1", "qz_2"]

# Generated at 2022-06-13 14:49:45.835026
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    array_var = {'hello': 'world', 'bye': 'yes'}
    ret = LookupModule().run(terms=['hello'], variables=array_var)
    assert ret == ['hello']

    array_var = {'hello': 'world', 'bye': 'yes'}
    ret = LookupModule().run(terms=['^b.+'], variables=array_var)
    assert ret == ['bye']

    array_var = {'hello': 'world', 'bye': 'yes'}
    ret = LookupModule().run(terms=['^b.+', '^h.+'], variables=array_var)
    assert len(ret) == 2 and 'bye' in ret and 'hello' in ret

    array_var = {'hello': 'world', 'bye': 'yes'}
    assert Lookup

# Generated at 2022-06-13 14:49:56.633759
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['^qz_.+']
    variables = {'qz_1': 'hello', 'qz_2': 'world', 'qa_1': "I won't show", 'qz_': "I won't show either"}
    assert LookupModule().run(terms, variables) == ['qz_1', 'qz_2']

    terms = ['hosts']
    variables = {'hosts': 'world', 'hostz': "I won't show"}
    assert LookupModule().run(terms, variables) == ['hosts']

    terms = ['.+_zone$', '.+_location$']
    variables = {'qz_zone': 'whatever', 'mem_location': 'whatever 1', 'disk_location': "whatever 2"}

# Generated at 2022-06-13 14:50:07.642419
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup_module = LookupModule()


# Generated at 2022-06-13 14:50:14.538525
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test 1:
    # Tests that provided vars are searched through to find matches for given terms.
    # The following terms are provided: ^qz_.+  .+  .+_zone  .+_location
    #   1) ^qz_.+ should match qz_1 and qz_2 but not qa_1 or qz_
    #   2) .+ should match all varnames
    #   3) .+_zone should match qz_1 and qz_2 but not qz_ or qa_1
    #   4) .+_location should NOT match any of the provided vars
    variables = {'qz_1': 'test', 'qz_2': 'test', 'qa_1': 'test', 'qz_': 'test'}

# Generated at 2022-06-13 14:50:17.251560
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: Implement
    print('TODO: Implement tests for LookupModule.run() method.')


# Generated at 2022-06-13 14:50:25.563191
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    var_lookup = LookupModule()

    term = "^qz_.+"
    variables = {"qz_1": "hello", "qz_2": "world", "qa_1": "I won't show", "qz_": "I won't show either"}
    var_lookup.set_options(var_options=variables, direct={})
    assert var_lookup.run([term]) == ["qz_1", "qz_2"]
    assert var_lookup.run([term]) != ["qz_", "qz_"]

    term = ".+"
    variables = {"qz_1": "hello", "qz_2": "world", "qa_1": "I won't show", "qz_": "I won't show either"}

# Generated at 2022-06-13 14:50:52.154551
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    terms = ['^qz_.+', '^qh_.+']
    variables = {'qz_1':'hello', 'qz_2':'world', 'qa_1':"I won't show", 'qz_':"I won't show either"}

    config = {}
    lookup = LookupModule()
    lookup.set_options(dict(var_options=variables, direct=config))

    assert lookup.run(terms, variables=variables) == ['qz_1', 'qz_2']

# Generated at 2022-06-13 14:50:57.822508
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ('^test_1.+', 'bar')
    variables = {'test_01': 'hello', 'bar': 'world', 'test_02': 'hello'}

    # test with no variable available
    try:
        LookupModule().run(terms)
        raise AssertionError('expected AnsibleError')
    except AnsibleError:
        pass

    result = sorted(LookupModule().run(terms, variables))
    assert result == ['bar', 'test_01', 'test_02']

# Generated at 2022-06-13 14:51:04.347462
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookupModule = LookupModule()
    terms = ['.+_zone$', '.+_location$']
    variables = {'global_zone': 'global', 'local_zone': 'local', 'global_location': 'global', 'local_location': 'local'}

    found_vars = lookupModule.run(terms, variables=variables)

    # The variables of interest should be returned
    assert found_vars == ['local_zone', 'local_location', 'global_zone', 'global_location']

    # The lookup module should have access to the variables
    assert lookupModule.get_options()['var_options'] == variables

    # The lookup module should be able to access the variables by name
    assert lookupModule.get_option('local_zone') == 'local'

    # The lookup module should be able to access the variables by fqname

# Generated at 2022-06-13 14:51:13.002194
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Test the run method of LookupModule.

    This is an internal module method.

    """
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    module = LookupModule()

    # Make sure we hit the missing variables exception
    with pytest.raises(AnsibleError):
        module.run(terms=[])

    # Make sure we hit the invalid regex error
    with pytest.raises(AnsibleError):
        module.run(terms=['['], variables={'abc': 'def'})

    # Make sure we can find the variable names we have

# Generated at 2022-06-13 14:51:17.688237
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class TestClass:
        pass
    test = TestClass()
    setattr(test, '_templar', None)
    setattr(test, '_loader', None)
    setattr(test, 'basedir', '.')

    kwargs = {'wantlist': False}
    result = LookupModule.run(test, ['^qz_.+'], {}, **kwargs)
    assert result == ['qz_1', 'qz_2']

# Generated at 2022-06-13 14:51:18.244169
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert True

# Generated at 2022-06-13 14:51:19.172739
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert False, "Unimplemented test"

# Generated at 2022-06-13 14:51:27.603735
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    Term = ''

# Generated at 2022-06-13 14:51:37.341333
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ast
    
    # This test uses ast to parse the docstring which it has been converted to a string. We then use
    # the resulting tree to extract the docstring and it's contents for testing.
    docstring_tree = ast.parse(LookupModule.run.__doc__)
    docstring_field = [node for node in docstring_tree.body if isinstance(node, ast.Expr)][0]
    parsed_docstring = ast.literal_eval(docstring_field.value)

    # Test the content of example
    assert len(parsed_docstring) == 3
    assert parsed_docstring['description'] == 'Retrieves a list of matching Ansible variable names.'

# Generated at 2022-06-13 14:51:40.630056
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_instance = LookupModule()

    # Test invalid parameters
    test_instance.run([])

    # Test valid parameters
    test_instance.run(['INVALID FORMAT'])
    test_instance.run(['INVALID FORMAT'], variables={'key': 'value'})
    test_instance.run(['INVALID FORMAT'], variables={'key': 'value'}, ansible_check_mode=True)

# Generated at 2022-06-13 14:52:31.317322
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.vault import VaultLib
    from ansible.utils.vault import VaultEditor
    import os
    import shutil
    import tempfile

    def _prepare_vars(path):
        ansible_vault_password_file = os.path.join(path, 'vault_password.txt')
        with open(ansible_vault_password_file, 'w') as f:
            f.write('Pr@gmaP@ssw0rd')
        return {'ANSIBLE_VAULT_PASSWORD_FILE': ansible_vault_password_file}

    def _prepare_vault(path):
        fd, tmpfile = tempfile.mkstemp(dir=path)

# Generated at 2022-06-13 14:52:36.057852
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['^qz_.+', '^qz_.+']
    variables= {'qz_1': 'hello', 'qz_2': 'world', 'qa_1': 'I wont show', 'qz_': "I won't show either"}

    expectedResult = ['qz_1', 'qz_2']

    result = LookupModule.run(terms, variables)

    assert result == expectedResult

# Generated at 2022-06-13 14:52:46.509462
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Create test data
    testing_vars = {
        'hosts': 'host1, host2, host3, host4',
        'zone_1': 'us-east-1',
        'zone_2': 'us-west-1',
        'zone_3': 'eu-west-1',
        'zone_4': 'ap-southeast-1'
    }

    # Create testing class

# Generated at 2022-06-13 14:52:54.816072
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()
    # Testing successful response with valid lookup parameters.
    assert lookup_plugin.run(['.+_zone$', '.+_location$'], {'aws_key_id': '1234', 'aws_zone': 'asd'}) == ['aws_zone']
    # Testing failure scenario with invalid lookup parameters.
    try: 
        assert lookup_plugin.run(['aws_key_id', 'aws_zone'], {'aws_key_id': '1234', 'aws_zone': 'asd'}) == ['aws_key_id', 'aws_zone']
    except AssertionError:
        assert True
    assert lookup_plugin.run(['aws_key_id', 'aws_zone'], {'aws_key_id': '1234', 'aws_zone': 'asd'})

# Generated at 2022-06-13 14:53:01.442213
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Create vars to test against
    vars = {
        "a_1": "This var should match",
        "b_2": "This var should not match",
        "c_3": "This var should match",
        "d_4": "This var should match"
    }

    # Create I/O parms, with var_options having all vars and direct=vars
    params = {
        '_terms': ['^[a-c].+'],
        'var_options': vars,
        'direct': vars,
        '_orig_basename': None
    }

    # Create object
    obj = LookupModule()

    # Call run method
    result = obj.run(**params)

    # Assert result equals expected
    assert result == ["a_1", "c_3"]



# Generated at 2022-06-13 14:53:10.799418
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    my_lookup = LookupModule()
    mydict = {'_fact': 'qz_1', 'qz_1': 'hello', 'qz_2': 'world', 'qa_1': 'I won\'t show', 'qz_': 'I won\'t show either'}
    # test first usecase
    my_lookup.run(['^qz_.+'], mydict)
    assert my_lookup.result() == ['qz_1', 'qz_2']
    # test second usecase
    my_lookup.run(['.+'], mydict)
    assert my_lookup.result() == ['_fact', 'qz_1', 'qz_2', 'qa_1']
    # test third usecase
    my_lookup.run(['hosts'], mydict)

# Generated at 2022-06-13 14:53:19.384340
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    def test_run_exception_missing_var(variables=None):
        lookup = LookupModule()
        terms = ['term1', 'term2']
        with pytest.raises(AnsibleError) as ex:
            lookup.run(terms=terms, variables=variables)
        assert 'No variables available to search' in str(ex.value)

    def test_run_exception_non_string(variables=None):
        lookup = LookupModule()
        terms = [1, 2]
        with pytest.raises(AnsibleError) as ex:
            lookup.run(terms=terms, variables=variables)
        assert 'Invalid setting identifier' in str(ex.value)

    def test_run_exception_re_exception(variables=None):
        lookup = LookupModule()


# Generated at 2022-06-13 14:53:28.210177
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class TestLookupModule(LookupModule):
        pass

    terms = TestLookupModule()
    variables = {'result_passes': 10, 'result_fails': 5, 'log_file': '/var/log/long_file.log'}

    ret = terms.run(['result_.+', 'log_file'], variables, **{})
    assert set(ret) == set(['result_passes', 'result_fails', 'log_file'])

    ret = terms.run(['result_passes'], variables, **{})
    assert set(ret) == set([])

    ret = terms.run(['result_.+'], variables, **{})
    assert set(ret) == set(['result_passes', 'result_fails'])


# Generated at 2022-06-13 14:53:39.867197
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create an empty object of class LookupModule
    # This object will be used to call the run method
    # As it does not inherite from "object" it does not
    # have a constructor.
    lookup_obj = LookupModule()
    # Testing the run method
    assert lookup_obj.run(terms=['^qz_.+'], variables=dict(qz_1='hello', qz_2='world')) == ['qz_1', 'qz_2']
    assert lookup_obj.run(terms=['^qz_.+'], variables=dict()) == []
    assert lookup_obj.run(terms=['^qz_.+'], variables=dict(qa_1='hello', qz_2='world')) == ['qz_2']

# Generated at 2022-06-13 14:53:40.834239
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert(LookupModule.run(1, 2)) == 0