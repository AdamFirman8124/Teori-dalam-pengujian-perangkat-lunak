

# Generated at 2022-06-13 14:02:54.674184
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module.run([['abc']], 'def')
#Unit test for method _flatten of class LookupModule

# Generated at 2022-06-13 14:02:58.796522
# Unit test for method run of class LookupModule
def test_LookupModule_run():
  lookup = LookupModule()
  assert lookup.run([[{'a': 1}, {'b': 2}], [1, 2, 3]], {}) == [[{'a': 1}, 1], [{'a': 1}, 2], [{'a': 1}, 3], [{'b': 2}, 1], [{'b': 2}, 2], [{'b': 2}, 3]]

# Generated at 2022-06-13 14:03:10.229543
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Input params - initialize the class variable to test
    terms = [['a', 'b'], ['1', '2']]
    variables = None

    # Expected values
    expected = [['a', '1'], ['a', '2'], ['b', '1'], ['b', '2']]

    #
    # Test 1
    #
    # Testing with two elements of list at nested level
    #
    # Expected result from the LookupModule.run()
    result = LookupModule().run(terms, variables)
    if result != expected:
        return False

    #
    # Test 2
    #
    # Testing with three elements of list at nested level
    #
    terms = [['a', 'b'], ['1', '2'], ['a', 'b']]

    # Expected result from the

# Generated at 2022-06-13 14:03:20.132753
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    try:
        from collections import UserList
    except ImportError:
        from UserList import UserList
    module = LookupModule()


# Generated at 2022-06-13 14:03:29.296484
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
        Unit test for method run of class LookupModule
    """
    # From Ansible's test/units/plugins/lookup/test_nested.py
    # pylint: disable=import-error
    from ansible.utils import listify_lookup_plugin_terms
    lookup_module = LookupModule()

    def test_case(result, *args):
        ret = lookup_module.run(list(args), variables={}, **{'wantlist': True})
        assert ret == result

    test_case(
        [
            [1, 2],
            [1, 3],
            [1, 4],
            [2, 2],
            [2, 3],
            [2, 4]
        ],
        [1, 2],
        [2, 3, 4],
    )
    test_case

# Generated at 2022-06-13 14:03:36.461479
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    terms = [
        [
            ['www', 'nginx']
        ],
        [
            ['example', 'example.org'],
        ],
    ]
    assert lm.run(terms) == [
        ['www', 'example', 'example.org'],
        ['nginx', 'example', 'example.org'],
    ]

# Generated at 2022-06-13 14:03:44.168349
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()
    lookup_plugin = LookupModule()

    # test single list
    test_list = [["a","b"],["c","d"]]
    assert lookup_plugin.run(test_list, variable_manager) == [['a', 'c'], ['a', 'd'], ['b', 'c'], ['b', 'd']]

    # test single list with empty list
    test_list = [["a", "b"], []]
    assert lookup_plugin.run(test_list, variable_manager) == [ ]

    # test multiple lists
    test_list = [["a"],["b","c"],["d","e"]]
   

# Generated at 2022-06-13 14:03:49.862585
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible import constants as C
    from units.mock.loader import DictDataLoader

    input_data_single_list = [{'_raw': [['alice', 'bob'], ['clientdb', 'employeedb', 'providerdb']]}]
    output_data_single_list = [["['alice', 'clientdb']", "['alice', 'employeedb']", "['alice', 'providerdb']",
                                "['bob', 'clientdb']", "['bob', 'employeedb']", "['bob', 'providerdb']"]]
    lm = LookupModule()
    lm.set_loader(DictDataLoader(input_data_single_list))
    test_output = lm.run([], variables={'testv': 'test'})
   

# Generated at 2022-06-13 14:03:55.196679
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    terms = [['A'],['1','2']]
    result = l.run(terms,'')
    print(result)
    assert result == [['A', '1'], ['A', '2']]

if __name__ == '__main__':
    test_LookupModule_run()

# Generated at 2022-06-13 14:04:00.967020
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lu = LookupModule()
    # input
    terms = [ [ 'alice', 'bob' ], [ 'clientdb', 'employeedb', 'providerdb' ] ]
    # expected result
    result = lu._combine(terms[0], terms[1])
    assert result == [ ['alice', 'clientdb'], ['alice', 'employeedb'], ['alice', 'providerdb'], ['bob', 'clientdb'], ['bob', 'employeedb'], ['bob', 'providerdb'] ]

# Generated at 2022-06-13 14:04:11.441867
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def assert_run(terms, result):
        l = LookupModule()
        theresult = l.run(terms)
        assert theresult == result

    assert_run([['a','b'], ['1','2']], [['a','1'], ['a','2'], ['b','1'], ['b','2']])
    assert_run([['a','b'], ['1'], ['x', 'y']], [['a','1','x'], ['a','1','y'], ['b','1','x'], ['b','1','y']])
    assert_run([['a','b'], [1,2]], [['a',1], ['a',2], ['b',1], ['b',2]])
    assert_run([['a'], ['b']], [['a','b']])

# Generated at 2022-06-13 14:04:22.982403
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l.set_options({})
    terms = [ [ "foo", "bar" ], [ "one", "two" ] ]
    result = l.run(terms=terms)
    assert result == [
        [ "foo", "one" ],
        [ "foo", "two" ],
        [ "bar", "one" ],
        [ "bar", "two" ]
        ]

    l = LookupModule()
    l.set_options({})
    terms = [ [ "foo" ], [ "one", "two" ], [ "aaa", "bbb", "ccc" ] ]
    result = l.run(terms=terms)

# Generated at 2022-06-13 14:04:29.839493
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    LookupModule_instance = LookupModule()
    terms = [['alice', 'bob'], ['clientdb', 'employeedb', 'providerdb']]
    result = LookupModule_instance.run(terms)
    assert result == [['alice', 'clientdb'], ['alice', 'employeedb'], ['alice', 'providerdb'], ['bob', 'clientdb'],[
                      'bob', 'employeedb'], ['bob', 'providerdb']]


# Generated at 2022-06-13 14:04:39.686415
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import __builtin__ as builtins
    if hasattr(builtins, '__ACCESS_COUNTER'):  # pragma: no cover
        del builtins.__ACCESS_COUNTER  # pragma: no cover
    if hasattr(builtins, '__TEMPLATE'):  # pragma: no cover
        del builtins.__TEMPLATE  # pragma: no cover
    if hasattr(builtins, '__VARS'):  # pragma: no cover
        del builtins.__VARS  # pragma: no cover
    lm = LookupModule()
    assert lm.run([['a', 'b'], ['c', 'd']]) == [['a', 'c'], ['b', 'c'], ['a', 'd'], ['b', 'd']]
   

# Generated at 2022-06-13 14:04:50.737497
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    x = lm.run([
        [1, 2, 3],
        [ 'first', 'second'],
        ['a', 'b', 'c']
    ])

    assert type(x) == list
    assert x[0] == [1, 'first', 'a']
    assert x[1] == [1, 'first', 'b']
    assert x[2] == [1, 'first', 'c']
    assert x[3] == [1, 'second', 'a']
    assert x[4] == [1, 'second', 'b']
    assert x[5] == [1, 'second', 'c']
    assert x[6] == [2, 'first', 'a']
    assert x[7] == [2, 'first', 'b']
    assert x

# Generated at 2022-06-13 14:04:54.677818
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    my_lookup = LookupModule()
    assert my_lookup.run(["DB1", "DB2"], variables=None, **{}) == [["DB1", "DB2"]]

    assert my_lookup.run(["DB1", "DB2"], variables=None, **{}).__class__ == list



# Generated at 2022-06-13 14:05:06.739104
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    print('Testing LookupModule class.')

    # Initializing required objects
    lookup_module = LookupModule()

    terms = [['a', 'b', 'c'], [1, 2], ['i', 'j']]
    result = lookup_module.run(terms)
    result.sort()

# Generated at 2022-06-13 14:05:14.555525
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    #Test with no element in list
    lookup = LookupModule()
    result = lookup.run([])
    assert(result == None)
    #Test with one element
    result = lookup.run([["a"]])
    assert(result == [["a"]])
    #Test with two element
    result = lookup.run([["a", "b"], ["1", "2", "3"]])
    assert(result == [["a", "1"], ["a", "2"], ["a", "3"], ["b", "1"], ["b", "2"], ["b", "3"]])
    #Test with three element
    result = lookup.run(
        [["a", "b"], ["1", "2", "3"], ["A", "B", "C", "D"]])

# Generated at 2022-06-13 14:05:20.189919
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Unit test for method run of class LookupModule.
    test_input = [['a','b','c'],[1,2,3]]

    # expected output
    expected_output = [['a',1],['a',2],['a',3],['b',1],['b',2],['b',3],['c',1],['c',2],['c',3]]

    test_obj = LookupModule()
    test_result = test_obj.run(test_input)

    assert test_result == expected_output

# Generated at 2022-06-13 14:05:28.971855
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup_module = LookupModule()

    terms = [
        ["alice", "bob"],
        ["clientdb", "employeedb", "providerdb"]
    ]

    output = lookup_module.run(terms)

    assert output == [
        ["alice", "clientdb"],
        ["alice", "employeedb"],
        ["alice", "providerdb"],
        ["bob", "clientdb"],
        ["bob", "employeedb"],
        ["bob", "providerdb"]
    ]



# Generated at 2022-06-13 14:05:38.852963
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    #Create instance of class
    lookuptype = LookupModule()
    #Create the result of the method run by the class with our arguments
    #This result is a list composed of lists paring the elements of the input lists
    result = lookuptype.run(
        [
            [
                [
                    'a', 'b'
                ]
            ],
            [
                'c', 'd'
            ]
        ]
    )
    #Comparing the result of the method run with the list that we expect to get
    assert result == [['a', 'c'], ['a', 'd'], ['b', 'c'], ['b', 'd']]



# Generated at 2022-06-13 14:05:44.647465
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils import parse_kv, jsonify

    lookup = LookupModule()
    #import ansible.utils.template as t
    #t.set_loader()
    #lookup._loader = t._loader

    #teststring = "{{ foo }}"
    #val = "foo"
    #variables = {'foo': val} #, 'bar': val}

    #test = lookup.run(teststring, variables, **{})
    #print(test)
    #assert test[0] == 'foo'

    terms = [ jsonify("{{ foo }}") ]

    variables = {'foo': [ 'foo', 'bar', 'baz' ] }

    result = lookup.run(terms, variables, **{})
    #print(result)

# Generated at 2022-06-13 14:05:49.964139
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()
    test_terms = [["a", "b", "c"], [1, 2]]
    test_terms = lookup_plugin._lookup_variables(test_terms, {})
    assert lookup_plugin.run(test_terms, {}) == [['a', 1], ['a', 2], ['b', 1], ['b', 2], ['c', 1], ['c', 2]]

    test_terms = [["a", "b", "c"], [1, 2], ['A', 'B', 'C', 'D']]
    test_terms = lookup_plugin._lookup_variables(test_terms, {})

# Generated at 2022-06-13 14:05:51.682448
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    assert lookup._lookup_variables([[1,2,3],[1,2,3]]) == [[1,2,3],[1,2,3]]

# Generated at 2022-06-13 14:06:03.798089
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    class TestLookup:
        def __init__(self, list_to_test):
            self.listToTest = list_to_test

        def test_lookup_module_run(self, terms, variables=None, **kwargs):
            lookup_module = LookupModule()
            return lookup_module.run(terms, variables, **kwargs)

    # test case 1: run with empty nested lists (expected 'AnsibleError')
    list_to_test = [
        []
    ]
    t = TestLookup(list_to_test)
    try:
        result = t.test_lookup_module_run(t.listToTest)
    except:
        result = sys.exc_info()[0]
    assert isinstance(result, AnsibleError)

    # test case 2: run with nested lists

# Generated at 2022-06-13 14:06:15.912359
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    result = lookup_module.run([['a','b'],['1','2']])
    assert result == [['a', '1'], ['a', '2'], ['b', '1'], ['b', '2']]
    result = lookup_module.run([['a','b'],['1'],['2']])
    assert result == [['a', '1', '2'], ['b', '1', '2']]
    result = lookup_module.run([['a'],['1','2']])
    assert result == [['a','1'],['a','2']]
    result = lookup_module.run([[],[],['a', 'b'],['1', '2']])

# Generated at 2022-06-13 14:06:17.435026
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l.run([["a", "b"], ["1", "2"]])

# Generated at 2022-06-13 14:06:24.220186
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Create object of class LookupModule
    l = LookupModule()

    # Assign value to variable result
    result = l.run([[1], [2, 3, 4]])

    # Assert if value of result is as expected
    assert result == [[1, 2], [1, 3], [1, 4]], 'Expect result is [[1, 2], [1, 3], [1, 4]], but actually is %s' %result



# Generated at 2022-06-13 14:06:36.360774
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    t = LookupModule()
    # Initialize the test object
    t._templar = 'Templar'
    t._loader = 'Loader'
    t.run()

    # Test with simple input
    input_terms = ['one', 'two', 'three']
    terms = t._lookup_variables(input_terms, variables={'one': '1', 'two': '2', 'three': '3'})
    exp_output = [['1', '2', '3']]
    
    output = t.run(terms, variables={'one': '1', 'two': '2', 'three': '3'})
    assert exp_output == output

    # Test with nested input
    input_terms = [['one', 'two'],['three', 'four']]
    terms = t._lookup_variables

# Generated at 2022-06-13 14:06:43.607676
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_obj = LookupModule()

    terms = [
        [
            ['alice', 'bob'],
            ['clientdb', 'employeedb', 'providerdb']
        ]
    ]

    result = lookup_obj.run(terms)
    assert result == [
        ['alice', 'clientdb'],
        ['alice', 'employeedb'],
        ['alice', 'providerdb'],
        ['bob', 'clientdb'],
        ['bob', 'employeedb'],
        ['bob', 'providerdb']
    ]

    terms = [['alice', 'bob'], ['clientdb', 'employeedb', 'providerdb']]

    result = lookup_obj.run(terms)

# Generated at 2022-06-13 14:06:55.582407
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup_module = LookupModule()
    test_terms1 = [['alice', 'bob'], ['clientdb', 'employeedb', 'providerdb']]
    test_variables1 = None
    test_terms2 = [['alice', 'bob'], ['clientdb', 'employeedb', 'providerdb'], ['1', '2']]
    test_variables2 = None
    test_terms3 = [['clientdb', 'employeedb', 'providerdb'], ['alice', 'bob']]
    test_variables3 = None
    test_terms4 = [['clientdb', 'employeedb', 'providerdb'], ['alice', 'bob'], ['1', '2', '3']]
    test_variables4 = None

# Generated at 2022-06-13 14:07:06.468313
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    module = LookupModule()
    my_list = [["a", "b"], ["1", "2", "3"], ["x", "y", "z"]]
    assert module.run(my_list) == [["a1x", "a1y", "a1z", "a2x", "a2y", "a2z", "a3x", "a3y", "a3z", "b1x", "b1y", "b1z", "b2x", "b2y", "b2z", "b3x", "b3y", "b3z"]]
    my_list = [["a", "b"], ["1", "2", "3"]]

# Generated at 2022-06-13 14:07:13.247874
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Unit test for testing the run method of LookupModule class
    """
    my_lookup_module_obj = LookupModule()
    input_data = ["{{ users }}", ["clientdb", "employeedb", "providerdb"]]
    my_lookup_module_obj.run(input_data, {"users": ["alice", "bob"]})


# Generated at 2022-06-13 14:07:25.084564
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test case with exact one element in nested list
    class UnitTest1(object):
        def __init__(self):
            self.__class__.__name__ = "AnsibleModule"
            self.params = {}

    unit1 = UnitTest1()
    lookup_plugin = LookupModule()
    lookup_plugin.set_options({})
    lookup_plugin._templar = None
    lookup_plugin._loader = None
    assert len(lookup_plugin.run([["test"]], variables=None, **{})) == 1
    assert len(lookup_plugin.run(["test"], variables=None, **{})) == 1

    # Test case with multiple elements in one list

# Generated at 2022-06-13 14:07:36.577938
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = [["Alice", "Bob"], ["clientdb", "employeedb", "providerdb"]]
    assert(LookupModule(Terms=terms, Variables={}).run(terms) == [["Alice", "clientdb"], ["Alice", "employeedb"], ["Alice", "providerdb"], ["Bob", "clientdb"], ["Bob", "employeedb"], ["Bob", "providerdb"]])
    terms = [["Alice", "Bob"], ["clientdb", "employeedb", "providerdb"], ["read", "write"]]

# Generated at 2022-06-13 14:07:47.676656
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    
    l = LookupModule()
    l.run([ [1,2], [3,4] ])


    class AnsibleDummy():
        def __init__(self):
            self.ANSIBLE_VERSION = 'dummy'

    class LookupBaseDummy():
        def __init__(self):
            self.templar = AnsibleDummy()
            self.loader = AnsibleDummy()
            self.module_name = "dummy"
            self.basedir = "dummy"

    class LookupModule2(LookupBaseDummy):
        def __init__(self):
            self.LookupBase = LookupBaseDummy()
        def get_basedir(self, variables):
            return 1


# Generated at 2022-06-13 14:07:56.641349
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l._templar = "template"
    l._loader = "loader"
    result = l.run(["{{ var1 }}", "{{ var2 }}"], variables={'var1': ["item1", "item2", "item3"], 'var2': ['val1', 'val2', 'val3', 'val4']})

# Generated at 2022-06-13 14:07:57.979430
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    LookupModule.run([[1,2,3],[2,3,4]])



# Generated at 2022-06-13 14:08:06.196284
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    myLookupModule = LookupModule()
    my_list = [["name1","name2","name3"], ["id1","id2","id3"], ["color1","color2","color3"]]
    result = myLookupModule.run(terms=my_list, variables=None, **{})
    assert result == [["name1", "id1", "color1"], ["name2", "id2", "color2"], ["name3", "id3", "color3"]]


# Generated at 2022-06-13 14:08:17.451898
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    assert [["alice", "clientdb"], ["alice", "employeedb"], ["alice", "providerdb"]] == lookup_module.run(["['alice']", "['clientdb', 'employeedb', 'providerdb']"])
    assert [["alice", "clientdb"], ["bob", "clientdb"], ["alice", "employeedb"], ["bob", "employeedb"], ["alice", "providerdb"], ["bob", "providerdb"]] == lookup_module.run(["['alice', 'bob']", "['clientdb', 'employeedb', 'providerdb']"])

# Generated at 2022-06-13 14:08:33.377437
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    terms = [
        ['alice', 'bob'],
        ['clientdb', 'employeedb', 'providerdb'],
        ['read', 'write', 'create'],
    ]
    result = module.run(terms)

# Generated at 2022-06-13 14:08:44.295436
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Initialize a LookupModule object
    test_runner = LookupModule()

    # Test setup_vars method
    test_expected_result = [
            ['alice', 'clientdb'], ['alice', 'employeedb'],
            ['alice', 'providerdb'], ['bob', 'clientdb'],
            ['bob', 'employeedb'], ['bob', 'providerdb']]
    test_input = [
            ['alice', 'bob'],
            ['clientdb', 'employeedb', 'providerdb']]

    # Call run method
    test_result = test_runner.run(test_input, {})

    # Assert the result
    assert test_expected_result == test_result


# Generated at 2022-06-13 14:08:55.155312
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # Test long list
    long_list = ['one', 'two', 'three', 'four', 'five']
    term = [long_list, long_list]
    result = lookup.run(term)
    assert len(result) == 25
    assert result[0] == ['one', 'one']

    # Test simple list
    term = [['one', 'two'], ['three', 'four']]
    result = lookup.run(term)
    assert len(result) == 4
    assert result[0] == ['one', 'three']
    assert result[3] == ['two', 'four']

    # Test sublist of simple list
    term = [['one', 'two', ['three', 'four']], ['five', 'six']]
    result = lookup.run(term)

# Generated at 2022-06-13 14:09:07.040355
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest

# Generated at 2022-06-13 14:09:18.262927
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    # Testing [ "{{x}}", "{{y}}", "{{z}}" ] where x=[1,2,3] y=[4,5,6] z=[7,8,9]
    x = { u'x': [ 1, 2, 3 ], u'y': [ 4, 5, 6 ], u'z': [ 7, 8, 9 ] }
    result = lookup.run([ [ "{{x}}", "{{y}}", "{{z}}" ] ], variables = x, wantlist=True)
    assert len(result) == 9
    # Testing [ "{{x}}" ] where x="foo" (convert to list)
    x = { u'x': "foo" }
    result = lookup.run([ [ "{{x}}" ] ], variables = x, wantlist=True)

# Generated at 2022-06-13 14:09:29.418745
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    LookupModuleObj = LookupModule()

    # Test-cases for LookupModule class.

# Generated at 2022-06-13 14:09:37.572832
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    assert l.run(
        [
            [1, 2, 3],
            [4],
            [5, 6]
        ],
        dict()
    ) == [
        [1, 4, 5],
        [1, 4, 6],
        [2, 4, 5],
        [2, 4, 6],
        [3, 4, 5],
        [3, 4, 6]
    ]

    assert l.run([[1, 2], [4], [5, 6, 7]], dict()) == [
        [1, 4, 5],
        [1, 4, 6],
        [1, 4, 7],
        [2, 4, 5],
        [2, 4, 6],
        [2, 4, 7]
    ]


# Generated at 2022-06-13 14:09:42.171489
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    x = []
    x.append(['foo','bar','baz'])
    x.append(['one','two','three'])
    assert(['fooone', 'foothree', 'foonine', 'barone', 'barthree', 'barnine', 'bazone', 'bazthree', 'baznine'] == l.run(x))

# Generated at 2022-06-13 14:09:52.908329
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    ####################################################################################
    test_input_dict = { "terms": [
                                [ "alice", "bob" ],
                                [ "clientdb", "employeedb", "providerdb" ]
                           ],

                        "expected_result": [
                            [ u'alice', u'clientdb' ],
                            [ u'alice', u'employeedb' ],
                            [ u'alice', u'providerdb' ],
                            [ u'bob', u'clientdb' ],
                            [ u'bob', u'employeedb' ],
                            [ u'bob', u'providerdb' ]
                        ]
    }
    ####################################################################################

    lk = LookupModule()


# Generated at 2022-06-13 14:10:01.104095
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    sys.path.append('/vars')
    from ansible.module_utils.six import PY3
    if PY3:
        from unittest import mock
    else:
        import mock

    my_lookup = LookupModule()
    my_dict = {'A': {'A': [{'A': 'A'}, {'B': 'B'}], 'B': 'B'}, 'B': {'A': 'A', 'B': 'B'}}


# Generated at 2022-06-13 14:10:20.874958
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    MODULE = 'nested'
    LOOKUP_SPEC = dict(
        name=MODULE,
        args=dict(
            _raw=[
                ['Alice', 'Bob'],
                ['clientdb', 'employeedb'],
                ['SELECT', 'UPDATE', 'INSERT', 'DELETE'],
            ],
        ),
    )

# Generated at 2022-06-13 14:10:27.697297
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create instance of LookupModule class
    lookup_module = LookupModule()

    # Create list of lists [['red', 'green'], ['big', 'small']]
    nested_lists = [['red', 'green'], ['big', 'small']]

    # Call method run
    output = lookup_module.run(terms=nested_lists)

    # Verify if output of method run is as expected
    expected_output = [['red', 'big'], ['red', 'small'], ['green', 'big'], ['green', 'small']]
    assert sorted(output) == sorted(expected_output)

# Generated at 2022-06-13 14:10:38.571674
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    test_var = [ [['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']] ]
    test_lookup = LookupModule()
    assert test_lookup.run(test_var) == [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']]

    test_var = [ [1,2], ['a','b'] ]
    test_lookup = LookupModule()
    assert test_lookup.run(test_var) == [[1, 'a'], [1, 'b'], [2, 'a'], [2, 'b']]


# Generated at 2022-06-13 14:10:46.300680
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule.run(LookupModule, [[1,2,3], [4,5,6,7]]) == [[1, 4], [2, 4], [3, 4], [1, 5], [2, 5], [3, 5], [1, 6], [2, 6], [3, 6], [1, 7], [2, 7], [3, 7]]
    assert LookupModule.run(LookupModule, [[1,2], [3,4,5]]) == [[[1, 3], [1, 4], [1, 5]], [[2, 3], [2, 4], [2, 5]]]

# Generated at 2022-06-13 14:10:53.749383
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import os
    os.environ['ANSIBLE_NOCOLOR'] = 'true'
    
    my_ListofList = [['blue','red'],['circle','square']]
    lookup_module = LookupModule()
    result = lookup_module.run(my_ListofList)
    
    assert [result[0][0],result[0][1]] == ['blue','red']
    assert [result[1][0],result[1][1]] == ['blue','square']
    assert [result[2][0],result[2][1]] == ['red','circle']
    assert [result[3][0],result[3][1]] == ['red','square']
    assert len(result) == 4

# Generated at 2022-06-13 14:11:00.480428
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class MockClass1(object):
        def __init__(self):
            self.value = None
        def __str__(self):
            return str(self.value)
        def __getattr__(self, name):
            if name == 'value':
                value = self.value
            else:
                raise AttributeError(name)
            return value

    _loader = 'dummy'
    _templar = MockClass1()
    _templar.value = [1,2,3]


# Generated at 2022-06-13 14:11:07.736236
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    lookup_module._flatten = mock_flatten
    lookup_module._combine = mock_combine
    lookup_module._lookup_variables = mock_lookup_variables
    terms = [["f"], ["e"], ["d"], ["c"]]
    variables = None
    my_list = [["e"], ["d"], ["c"]]
    assert lookup_module.run(terms, variables) == my_list

# mock for _flatten method

# Generated at 2022-06-13 14:11:15.093409
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()
    terms = [["foo"], ["bar"]]
    ret = lookup_plugin.run(terms, None)
    assert ret == [["foo", "bar"]], ret

    terms = [["foo"], ["bar", "baz"]]
    ret = lookup_plugin.run(terms, None)
    assert ret == [["foo", "bar"], ["foo", "baz"]], ret

    terms = [["foo", "spam"], ["bar", "baz"]]
    ret = lookup_plugin.run(terms, None)
    assert ret == [["foo", "bar"], ["foo", "baz"], ["spam", "bar"], ["spam", "baz"]], ret

    terms = [["foo", "spam"], ["bar", "baz"], ["eggs", "ham"]]
   

# Generated at 2022-06-13 14:11:24.673621
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test = dict()

    terms = [['a', 'b', 'c'], ['1', '2', '3']]
    expected_terms = [['a', 'b', 'c'], ['1', '2', '3']]
    test['terms'] = terms

    from ansible.template.template import Templar
    templar = Templar(loader=None, variables=None)
    test['templar'] = templar

    lookup_result = templar.template([terms], preserve_trailing_newlines=True, convert_bare=False)
    test['lookup_result'] = lookup_result

    test_class = LookupModule()
    result = test_class.run(terms, variables=None, templar=templar)

# Generated at 2022-06-13 14:11:32.324799
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    loop = LookupModule()
    list = [
        ['server_1', 'server_2'],
        ['user_1', 'user_2'],
        ['db_1', 'db_2', 'db_3']
    ]
    loop_result = loop.run(list)

# Generated at 2022-06-13 14:11:46.866342
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:11:51.732341
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l.set_options({'_raw': [['a', 'b'], ['1', '2', '3']]})
    assert l.run() == [['a', '1'], ['a', '2'], ['a', '3'], ['b', '1'], ['b', '2'], ['b', '3']]

# Generated at 2022-06-13 14:11:59.044288
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_instance = LookupModule()
    result = lookup_instance.run([['a','b','c','d'],[1,'a',2,'b',3]],{})
    assert result == [['a', 1], ['b', 1], ['c', 1], ['d', 1], ['a', 2], ['b', 2], ['a', 3], ['b', 3]]


# Generated at 2022-06-13 14:12:09.698542
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule.run(None, [[1, 2], ["a", "b"]]) == [[1, 'a'], [1, 'b'], [2, 'a'], [2, 'b']]
    assert LookupModule.run(None, [["a", "b"], [1, 2]]) == [['a', 1], ['a', 2], ['b', 1], ['b', 2]]

# Generated at 2022-06-13 14:12:18.440089
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:12:28.559603
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    x = LookupModule()
    terms = [["a", "b"], ["x", "y", "z"]]

    assert x.run((terms)) == [['ax', 'ay', 'az'], ['bx', 'by', 'bz']]

    terms = [["a", "b"], [], ["x", "y", "z"]]
    assert x.run((terms)) == [[], [], [], [], [], []]

    terms = [[], [], []]
    assert x.run((terms)) == [[], [], []]

    terms = [["a", "b"]]
    assert x.run((terms)) == [['a'], ['b']]

    terms = []
    assert x.run((terms)) == AnsibleError

# Generated at 2022-06-13 14:12:35.741206
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    terms = ['1', '2', '3', '4', '5']
    options = {
        '_raw': terms
    }
    lookup_module.set_options(var_options=options)

    assert lookup_module._lookup_variables(terms, None) == terms

    # Test 1
    result = lookup_module.run(terms, variables={})
    assert result == [
        ['1', '2'],
        ['1', '3'],
        ['1', '4'],
        ['1', '5'],
        ['2', '3'],
        ['2', '4'],
        ['2', '5'],
        ['3', '4'],
        ['3', '5'],
        ['4', '5'],
    ]

   

# Generated at 2022-06-13 14:12:45.411419
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Check for proper creation of list of lists (without undefined variables)
    lookup_module = LookupModule()
    terms = [['a', 'b'], [1, 2]]
    assert lookup_module.run(terms) == [['a', 1], ['a', 2], ['b', 1], ['b', 2]]

    # Check for proper creation of list of lists (with undefined variables)
    lookup_module = LookupModule()
    terms = [['a', '{{x}}', 'b'], [1, 2]]
    try:
        lookup_module.run(terms)
    except AnsibleUndefinedVariable:
        pass
    else:
        assert False, 'AnsibleUndefinedVariable was not raised'



# Generated at 2022-06-13 14:12:57.076446
# Unit test for method run of class LookupModule
def test_LookupModule_run():
  # Instantiate a LookupModule with arguments for test
  my_lookup = LookupModule()
  my_lookup._templar = None
  my_lookup._loader = None
  # test return value with no arguments
  result = my_lookup.run([])
  assert result == None
  result = my_lookup.run([], variables=[])
  assert result == None
  # test return value with empty dict as first argument
  result = my_lookup.run([{}])
  assert result == None
  result = my_lookup.run([{}], variables=[])
  assert result == None
  # test return value with valid two-entry dict as first argument
  result = my_lookup.run([{'b':[1,2], 'a':[3,4]}])