

# Generated at 2022-06-13 14:02:54.471821
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lu = LookupModule()
    assert lu.run(["a"]) == ["a"]
    assert lu.run(["a","b"]) != ["a"]

# Generated at 2022-06-13 14:03:00.410013
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    test_terms = ['a', 'b', 'c', 'd', 'e']
    test_terms_copy = list(test_terms)
    
    test_lookup_module = LookupModule()
    test_result = test_lookup_module.run(test_terms)
    
    # Element of test_terms are removed from test_terms_copy
    test_terms_copy.remove(test_result[0])
    test_terms_copy.remove(test_result[0])
    assert len(test_result) == 1
    assert len(test_terms_copy) == 4

# Generated at 2022-06-13 14:03:04.398878
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup_obj = LookupModule()
    
    result = lookup_obj.run(['test1', 'test2', 'test3'])

    assert result in ['test1', 'test2', 'test3']

# Generated at 2022-06-13 14:03:10.228874
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Random choice test
    my_var = [1, 2, 3, 4, 5]
    random_item1 = LookupModule().run([my_var])
    assert random_item1 in my_var
    random_item2 = LookupModule().run([my_var])
    assert random_item2 in my_var

    # Empty list
    assert LookupModule().run([[]]) == []

# Generated at 2022-06-13 14:03:13.954296
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # test fail
    # test success
    lm = LookupModule()
    assert [1] == lm.run([1, 2])
    assert [] == lm.run([])

# Generated at 2022-06-13 14:03:22.894714
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    my_obj1 = LookupModule()
    my_obj2 = LookupModule()
    my_obj3 = LookupModule()
    print("\n\n testing LookupModule.run()")
    print("\n test 1 : one value")
    test1 = my_obj1.run(["test"])
    print("\n test 2 : five value")
    test2 = my_obj2.run(["test1", "test2", "test3", "test4", "test5"])
    print("\n test 3 : no value")
    test3 = my_obj3.run([])
    if(test2 is not None and test3 is not None and test1 is not None):
        print("\n\n*** Test Passed ***")
        return 1

# Generated at 2022-06-13 14:03:29.052240
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    LookupModule_Object = LookupModule()

    # Testing the return value of run() in the case of a list with one element.
    assert(len(LookupModule_Object.run(["one"])) == 1)

    # Testing the return value of run() in the case of an empty list.
    assert(len(LookupModule_Object.run([])) == 0)

    # Testing the return value of run() in the case of a list with many elements.
    assert(len(LookupModule_Object.run(["one", "two", "three"])) == 1)

# Generated at 2022-06-13 14:03:34.509684
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    assert lookup_module.run(terms=["ansible"]) == ["ansible"]
    assert lookup_module.run(terms=["ansible", "rocks"]) == ["ansible"] or ["rocks"]

# Generated at 2022-06-13 14:03:37.329251
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    random.seed(0)
    lookup_module = LookupModule()
    result = lookup_module.run(["one", "two", "three", "four"])
    assert result == ["two"]

# Generated at 2022-06-13 14:03:37.979066
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 14:03:47.808571
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    lookup_instance = LookupModule()
    assert lookup_instance.run(["hello", "world"]) == ["world"]
    assert lookup_instance.run([u"hello", u"world"]) == [u"world"]
    assert lookup_instance.run([b"hello", b"world"]) == [b"world"]
    assert lookup_instance.run([b"hello", b"world"]) == [b"world"]
    assert lookup_instance.run([b"hello", b"world"]) == [b"world"]
    assert lookup_instance.run([b"hello", b"world"]) == [b"world"]

# Generated at 2022-06-13 14:03:50.885978
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    assert lookup_module.run(["First choice", "Second choice"])[0] in ["First choice", "Second choice"]
    assert lookup_module.run([]) is []

# Generated at 2022-06-13 14:03:55.636977
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule.run([]) == []
    assert LookupModule.run([1,2,3]) in [[1], [2], [3]]
    assert LookupModule.run([1 , 2, 3, 4]) in [[1], [2], [3], [4]]

# Generated at 2022-06-13 14:04:04.175681
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    result = lookup.run(['foo', 'bar', 'baz'], inject={'_random': lambda x: 'baz'})
    assert result == ['baz']

    result2 = lookup.run(['foo', 'bar', 'baz'])
    assert result2 in (['foo'], ['bar'], ['baz'])

    # Check that LookupError is raised when no terms is provided
    result3 = lookup.run(None, inject={'_random': lambda x: 'baz'})
    assert result3 == None

    result4 = lookup.run(None)
    assert result4 == None

# Generated at 2022-06-13 14:04:06.461617
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    assert lm.run(['a', 'b']) == ['a'] or lm.run(['a', 'b']) == ['b']

# Generated at 2022-06-13 14:04:12.735740
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Make an instance of LookupModule
    lookup_plugin = LookupModule()

    # Make an instance of AnsibleTemporaryVars
    templar = AnsibleTemporaryVars()

    # Create a list
    terms = [1, 0, 2, 'hello world']

    # Run method run of class LookupModule on the list
    # Method run returns a list
    random_choice_list = lookup_plugin.run(terms, templar._available_variables, inject=None)

    assert(len(random_choice_list) == 1)
    assert(random_choice_list[0] in terms)

# Generated at 2022-06-13 14:04:18.005010
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    
    with pytest.raises(TypeError): lookup_module.run(1)
    with pytest.raises(ValueError): lookup_module.run([])
    
    assert lookup_module.run(["a", "b", "c"]) == ["a"]

# Generated at 2022-06-13 14:04:29.438738
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    LookupM = LookupModule()

    # invalid type of argument terms
    input_terms = {'a':'a', 'b':'b', 'c':'c'}
    input_inject = None
    try:
        output = LookupM.run(terms = input_terms)
        raise AssertionError("test_LookupModule_run is failed for not returning AnsibleError for invalid type of input argument")
    except AssertionError as e:
        print('AssertionError raised: ', e)
    except AnsibleError:
        pass

    # valid type of argument terms and inject
    input_terms = ['a', 'b', 'c']
    input_inject = []
    output = LookupM.run(terms = input_terms, inject = input_inject)
    exp_output = ['a']

# Generated at 2022-06-13 14:04:33.225942
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["aaa", "bbb", "ccc"]
    result = LookupModule().run(terms)

    assert(isinstance(result, list) == True)
    assert(len(result) == 1)
    assert(result[0] in terms)

# Generated at 2022-06-13 14:04:37.314925
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import string_types
    lookup_module = LookupModule()
    assert isinstance(lookup_module.run(['a','b','c']), list)
    assert isinstance(lookup_module.run(['a','b','c'])[0], string_types)

# Generated at 2022-06-13 14:04:46.013721
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lu = LookupModule()
    assert lu.run([1, 2, 3]), [1]
    assert lu.run([1, 2, 3]), [2]
    assert lu.run([1, 2, 3]), [3]



# Generated at 2022-06-13 14:04:55.336181
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup.random_choice import LookupModule
    lookup_plugin = LookupModule()

    # test without any input
    assert lookup_plugin.run([]) == []

    # test with one input item
    first_input = ["first_input_item"]
    assert lookup_plugin.run(first_input) == first_input

    # test with one input item
    second_input = ["second_input_item"]
    assert lookup_plugin.run(second_input) == second_input

    # test with two input items
    assert lookup_plugin.run(first_input + second_input) in [first_input, second_input]

    # test with three input item
    input_three = ["third_input_item"]
    assert lookup_plugin.run(first_input + second_input + input_three)

# Generated at 2022-06-13 14:05:03.822315
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create an object of LookupModule class
    lookup_obj = LookupModule()

    words = ["foo", "bar", "baz"]
    result = lookup_obj.run(terms=words)
    assert(result == words)

    # Negative testing
    result1 = lookup_obj.run()
    assert(result1 == [])

    result2 = lookup_obj.run(["foo", "bar", "baz", "boo"])
    assert(result2 == ["foo", "bar", "baz", "boo"])

# Generated at 2022-06-13 14:05:07.513210
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['word1', 'word2', 'word3', 'word4', 'word5']
    lookup_module = LookupModule()
    random_choice = lookup_module.run(terms)
    assert(random_choice[0] in terms)

# Generated at 2022-06-13 14:05:10.114266
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    assert lm.run([]) == []
    assert lm.run(['one', 'two', 'three']) in [['one'], ['two'], ['three']]

# Generated at 2022-06-13 14:05:17.458162
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    look = LookupModule()
    #test case 1:
    list1 = [1,2,3,4]
    ret1 = look.run(list1)
    assert ret1 != [], "Expected a non-empty list. Got %s" %(ret1)
    assert ret1[0] in list1, "Expected element from list. Got %s" %(ret1[0])
    #test case 2:
    list2 = []
    ret2 = look.run(list2)
    assert ret2 == [], "Expected an empty list. Got %s" %(ret2)

# Generated at 2022-06-13 14:05:23.384812
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    print("test_LookupModule_run()")
    """
    Unit test for method run of class LookupModule
    """
    lm = LookupModule()
    assert lm.run([]) == []
    assert lm.run(['a', 'b']) in ['a', 'b']
    assert lm.run([1, 2]) in [1, 2]


# Generated at 2022-06-13 14:05:30.041333
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_ret, test_terms, test_inject = [], [], []
    lookup_module = LookupModule()
    test_ret = lookup_module.run(test_terms, test_inject)
    assert test_ret == []
    test_terms = [1, 2, 3]
    test_ret = lookup_module.run(test_terms, test_inject)
    assert test_ret == [1] or test_ret == [2] or test_ret == [3]

# Generated at 2022-06-13 14:05:36.225029
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Create the class object
    lm = LookupModule()

    # Create the list from which the random element is to be selected
    terms = [1,2,3,4,5]

    # Run the method
    selected_element = lm.run(terms)

    # Check the results
    assert(len(selected_element) == 1)
    assert(selected_element[0] in terms)

# Generated at 2022-06-13 14:05:47.700890
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a test object
    my_test = LookupModule()

    # The list of items in the variable 'terms' passed to method
    # run of class LookupModule
    test_terms = ['test1', 'test2']

    # Invoke method run of class LookupModule
    returned_values = my_test.run(terms=test_terms)

    # Check if the returned value is a list
    assert(isinstance(returned_values, list))

    # Check if the returned list has only one value (as the method
    # returns one random element from the variable 'terms')
    assert(len(returned_values) == 1)

    # Check if the returned value is present in the variable 'terms'
    assert(returned_values[0] in test_terms)

    # Check if the returned value is of type string
   

# Generated at 2022-06-13 14:06:00.633655
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test = LookupModule()
    terms = ["1", "2", "3", "4", "5"]
    results = test.run(terms)
    assert len(results) == 1
    assert results[0] in terms

# Generated at 2022-06-13 14:06:04.697159
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    term_list = ["a", "b", "c", "d"]
    result = lookup_module.run(terms=term_list)
    assert len(result) == 1
    assert result[0] in term_list

# Generated at 2022-06-13 14:06:10.720867
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import random
    obj = LookupModule()
    data = ["go through the door", "drink from the goblet", "press the red button", "do nothing"]
    random.choice = lambda self: random.choice(data)

    result = obj.run(["go through the door, drink from the goblet, press the red button, do nothing"])
    assert result == data

# Generated at 2022-06-13 14:06:16.165693
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    t = []
    look = LookupModule()
    result = look.run(t)
    assert not result

    t = ["A"]
    result = look.run(t)
    assert result == ["A"]

    t = ["A", "B"]
    result = look.run(t)
    assert result == ["A"] or result == ["B"]

# Generated at 2022-06-13 14:06:18.519591
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test = LookupModule()
    testTerms = ['a', 'b', 'c']
    randChoice = test.run(testTerms)[0]
    assert randChoice in testTerms

# Generated at 2022-06-13 14:06:21.806957
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    assert lookup_module.run([[{"foo": 1}, {"bar": 2}]], None) == [{"foo": 1}]

# Generated at 2022-06-13 14:06:28.044908
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    obj = LookupModule()
    assert ["a"] == obj.run(["a"])
    assert ["a"] == obj.run([["a"]])
    assert ["a"] == obj.run([["a", "b"]])
    expected = obj.run([["a", "b", "c", "d", "e", "f", "g", "h", "i"]])
    assert expected in [["a"],["b"],["c"],["d"],["e"],["f"],["g"],["h"],["i"]]
    assert obj.run([]) == []
    assert obj.run([[]]) == []

# Generated at 2022-06-13 14:06:31.376781
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["a", "b", "c"]
    lm = LookupModule()
    result = lm.run(terms)
    assert result in terms


# Generated at 2022-06-13 14:06:32.009573
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert True

# Generated at 2022-06-13 14:06:35.069225
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['foo', 'bar']
    lookup_module = LookupModule()
    assert lookup_module.run(terms) == ['foo'] or lookup_module.run(terms) == ['bar']

# Generated at 2022-06-13 14:06:57.886596
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    assert lookup_module
    assert lookup_module.run([1,2,3]) == [1,2,3]

# Generated at 2022-06-13 14:07:02.149479
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert list(LookupModule('').run([1, 2, 3])) == [3] or list(LookupModule('').run([1, 2, 3])) == [1] or list(LookupModule('').run([1, 2, 3])) == [2]

# Generated at 2022-06-13 14:07:09.938761
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup import get_lookup_plugins
    lookup_plugins = get_lookup_plugins()
    test_data = (
        # test for terms not as list
        {'terms': 'this is a test', 'expected': 'this is a test'},
        # test for terms as list with one element
        {'terms': ['superman'], 'expected': ['superman']},
        # test for terms as list with multiple elements
        {'terms': ['superman', 'batman', 'spiderman'], 'expected': ['superman', 'batman', 'spiderman']}
    )

    for data in test_data:
        inst = LookupModule()
        result = inst.run(data['terms'])
        assert result == data['expected']

# Generated at 2022-06-13 14:07:13.369325
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''
    Test run method of the class LookupModule
    '''
    terms = ['A', 'B', 'C']
    lookup = LookupModule()
    ret = lookup.run(terms)
    assert ret[0] in terms

# Generated at 2022-06-13 14:07:18.221922
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['a', 'b', 'c']
    random.seed(1)
    assert LookupModule(None, None).run(terms) == ['c']

# Generated at 2022-06-13 14:07:20.664575
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    t = LookupModule()
    terms = ['foo', 'bar', 'baz']
    result = t.run(terms)
    assert result in terms

# Generated at 2022-06-13 14:07:22.737278
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    assert lookup.run([u'a', u'b', u'c']) == [u'a']

# Generated at 2022-06-13 14:07:26.653193
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from random import seed
    seed(1)
    s = ['No', 'Yes', 'Maybe']
    lookup_instance = LookupModule()
    ret = lookup_instance.run(s)
    assert(ret == ['No'])
    ret = lookup_instance.run(s)
    assert(ret == ['Yes'])
    ret = lookup_instance.run(s)
    assert(ret == ['Yes'])

# Generated at 2022-06-13 14:07:37.527116
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import ansible.plugins.lookup.random_choice
    ansible_module = ansible.plugins.lookup.random_choice
    obj = ansible_module.LookupModule()

    class TestInject(object):
        def __init__(self):
            self.lookup_plugin_general_args = None

    test_inject = TestInject()
    test_value = obj.run(["a", "b", "c"], test_inject)
    assert isinstance(test_value, list)
    assert test_value != ["a", "b", "c"]
    assert test_value != ["a"]
    assert test_value != ["b"]
    assert test_value != ["c"]
    assert test_value == ["a"] or test_value == ["b"] or test_value == ["c"]

    test_

# Generated at 2022-06-13 14:07:43.138509
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    assert lm.run([]) == []
    assert lm.run([1]) == [1]
    assert lm.run([1,2,3]) == [1] or lm.run([1,2,3]) == [2] or lm.run([1,2,3]) == [3]

# Generated at 2022-06-13 14:08:31.252374
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    assert lookup_module.run([1,2,3,4,5],[]) == [5]
    assert lookup_module.run([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],[]) == [30]
    assert lookup_module.run(["cow", "chicken", "sheep"],[]) == ["sheep"]
    assert lookup_module.run(["a", "b", "c", "d"],[]) == ["b"]

# Generated at 2022-06-13 14:08:35.128565
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = [1, 2, 3]
    result = lookup.run(terms)
    assert(isinstance(result, list))
    assert(result[0] in terms)

# Generated at 2022-06-13 14:08:45.456530
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a fake AnsibleModule instance for LookupModule
    import ansible.module_utils
    module_args = {}
    module_fake = ansible.module_utils.basic.AnsibleModule(argument_spec={}, **module_args)
    # Module instance created with argument_spec={} is not supported by LookupModule
    # This can be done only with the following way
    setattr(module_fake._shared_loader_obj, 'module_commands', dict(random_choice=dict()))

    # Create a fake inventory for LookupBase
    inventory_fake = dict()

    # Create a fake loader for LookupBase
    loader_fake = dict()

    # Create a fake variable manager for LookupBase
    variable_manager_fake = dict()

    # Create a fake task vars for LookupBase
    task_vars

# Generated at 2022-06-13 14:08:49.148646
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule.run(["a","b","c"]) in ["a","b","c"]
    assert LookupModule.run([]) == []
    assert LookupModule.run(1) == [1]

# Generated at 2022-06-13 14:08:52.429560
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup_module = LookupModule()
    result = lookup_module.run(terms=['foo', 'bar', 'foobar'])

    assert result in ['foo', 'bar', 'foobar']

# Generated at 2022-06-13 14:08:56.615614
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Test LookupModule class to pick random element from list"""
    terms = ["a", "b", "c", "d", "e"]
    lu = LookupModule()
    random_choice = lu.run(terms)
    assert isinstance(random_choice, list), "Output of random_choice should be of type list"
    assert random_choice[0] in terms, "Random choice should be one of the terms given as input"

# Generated at 2022-06-13 14:09:01.342055
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    test_terms = ["one","two","three"]

    # test for given term
    for _ in range(10):
        assert lookup.run(terms=test_terms) in test_terms

    # test for empty term
    assert lookup.run(terms=None) is None

# Generated at 2022-06-13 14:09:05.312221
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test Insertion and Searching for a binary tree.
    module = LookupModule()

    terms = [1, 2, 3, 4, 5]
    result = module.run(terms)

    assert result in terms

# Test Case
test_LookupModule_run()

# Generated at 2022-06-13 14:09:08.041924
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    terms = ["one", "two", "three"]
    assert lookup_module.run(terms)
    terms = []
    assert lookup_module.run(terms)

# Generated at 2022-06-13 14:09:09.788914
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    ret = lookup.run(["1","2","3"])
    assert ret in ["1","2","3"]

# Generated at 2022-06-13 14:10:41.847816
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    # Test that a list of terms is returned with one element
    terms = ['one', 'two', 'three']
    result = lookup_module.run(terms)
    assert type(result) is list
    assert len(result) == 1
    assert result[0] in terms

    # Test that empty list returned if input list is empty
    terms = []
    result = lookup_module.run(terms)
    assert type(result) is list
    assert not result

# Generated at 2022-06-13 14:10:46.789158
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # set input data
    terms = ["1", "2", "3"]
    # create instance of class to be tested
    lookup = LookupModule()
    # call method to be tested
    res = lookup.run(terms)
    # check results
    assert res in terms

# Generated at 2022-06-13 14:10:50.131577
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    # test with empty terms
    assert lookup_module.run([]) == []
    assert lookup_module.run(["foo", "bar", "baz"]) == ["foo"]

# Generated at 2022-06-13 14:10:55.396150
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    # Initial testcase
    terms = list()
    terms.extend([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
    result = lookup.run(terms)
    print(result)
    assert(result)

    # Empty testcase
    terms = list()
    result = lookup.run(terms)
    print(result)
    assert(result)

# Test if LookupModule class may be called directly
if __name__ == "__main__":
    test_LookupModule_run()

# Generated at 2022-06-13 14:11:06.265733
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test case No.1
    # Test different instances of LookupModule object,
    #  specifying different terms
    class1 = LookupModule()
    class2 = LookupModule()
    assert class1.run(terms=["a", "b", "c"]) != class2.run(terms=["a", "b", "c"])
    # Test case No.2
    # Test one instance of LookupModule object,
    #  specifying different terms
    class1 = LookupModule()
    assert class1.run(terms=["a", "b", "c"]) != class1.run(terms=["a", "b", "c"])
    # Test case No.3
    # Test one instance of LookupModule object,
    #  specifying different terms
    class1 = LookupModule()
    assert class1.run

# Generated at 2022-06-13 14:11:10.147020
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Arrange
    terms = [ "test1", "test2", "test3" ]
    lookup = LookupModule()

    # Act
    result = lookup.run(terms)

    # Assert
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] in terms

# Generated at 2022-06-13 14:11:14.157286
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    inputs_list = ['el1', 'el2', 'el3']
    ret = module.run(inputs_list)
    assert isinstance(ret, list)
    assert len(ret) == 1
    assert ret[0] in inputs_list

# Generated at 2022-06-13 14:11:16.165035
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # initializing instance
    lookup_module = LookupModule()

    # calling run
    lookup_module.run(["1","2","3"])

# Generated at 2022-06-13 14:11:26.998758
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # 1. Error case
    lookup_mod = LookupModule()
    ret = lookup_mod.run([1, 2, 3], **{})
    assert ret == [1, 2, 3], 'test_LookupModule_run, error case fail'

    # 2. Error case
    lookup_mod = LookupModule()
    try:
        ret = lookup_mod.run(1, **{})
    except Exception as e:
        assert str(e) == 'Unable to choose random term: unhashable type: \'int\'', 'test_LookupModule_run, error case fail2'

    # 3. Normal case
    lookup_mod = LookupModule()
    ret = lookup_mod.run([1, 2, 3], **{})

# Generated at 2022-06-13 14:11:32.130393
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    terms = ["test1", "test2", "test3", ]
    try:
        for item in range(0, 100):
            random_choice = lookup_module.run(terms)
            assert len(random_choice) == 1
            assert random_choice[0] in terms
    except Exception as e:
        #TODO: Update after the exception raised at line 61 is defined in the plugin
        raise Exception('Unable to call method run of class LookupModule: %s' % to_native(e))