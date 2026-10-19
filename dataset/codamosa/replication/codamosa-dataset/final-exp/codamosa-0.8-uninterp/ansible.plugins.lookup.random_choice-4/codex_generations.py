

# Generated at 2022-06-13 14:03:02.008926
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    
    # Test 1: test if LookupModule_run() returns a list
    #    including the only one element when the input list only has one element
    local_module = LookupModule()
    ret = local_module.run([1], inject=None)
    assert type(ret) == list
    assert len(ret) == 1
    assert ret[0] == 1
    
    # Test 2: test if LookupModule_run() returns a list
    #    with multiple elements when the input list has multiple elements
    local_module = LookupModule()
    ret = local_module.run([1, 2], inject=None)
    assert type(ret) == list
    assert len(ret) == 1
    assert ret[0] in [1, 2]
    
    # Test 3: test if LookupModule_run() throws Ansible

# Generated at 2022-06-13 14:03:08.634551
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Initialize LookupModule class
    lookup_module = LookupModule()
    # Input list for function
    terms = [
        "host_foo",
        "host_bar",
        "host_baz"
    ]
    # Expected result
    ret = terms
    # Assert
    assert lookup_module.run(terms, inject=None, **{}) == ret

# Generated at 2022-06-13 14:03:17.599166
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    random_variable_terms = ["t1","t2","t3","t4","t5","t6","t7","t8","t9","t10"]
    lookup_module = LookupModule()

    for i in range(0,100):
        selected_terms = lookup_module.run(random_variable_terms)
        assert len(selected_terms) == 1, "len(selected_terms): %s" % str(len(selected_terms))
        assert selected_terms[0] in random_variable_terms, "selected_terms[0] is not one of the random variables"



# Generated at 2022-06-13 14:03:22.687626
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["Hello", "World", "Foo", "Bar"]
    lookup_module = LookupModule()
    random_terms = lookup_module.run(terms)
    assert len(random_terms) == 1
    assert random_terms[0] in terms

# Generated at 2022-06-13 14:03:25.929909
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()
    terms = ['first', 'second', 'third']
    random_choice = lookup_plugin.run(terms)
    assert random_choice in terms

if __name__ == '__main__':
    test_LookupModule_run()

# Generated at 2022-06-13 14:03:32.757346
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Importing random for random.choice
    random = __import__('random')
    # Importing random for random.choice
    random = __import__('random')
    # Importing AnsibleError from ansible.errors
    from ansible.errors import AnsibleError
    # Importing AnsibleError from ansible.errors
    from ansible.errors import AnsibleError
    # Initialising instance of class LookupModule
    instance = LookupModule()
    # Calling method run of class LookupModule with valid parameters
    # Returning 'ret'.
    ret = instance.run([random.choice(["go through the door", "drink from the goblet", "press the red button", "do nothing"])])

# Generated at 2022-06-13 14:03:36.186743
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['term1', 'term2', 'term3', 'term4']
    random.seed(1)
    assert LookupModule().run(terms) == ['term2']

# Generated at 2022-06-13 14:03:45.484069
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module_object = LookupModule()

    # Random choice from the given list
    list_random_choice = [1, 2, 3, 4, 5, 6, 7]
    list_random_choice_result = lookup_module_object.run(list_random_choice)
    assert list_random_choice_result in list_random_choice, \
        "Random choice from list test failed, random term: %s" % list_random_choice_result

    # Random choice from the empty list
    random_choice_empty_list = []
    random_choice_empty_list_result = lookup_module_object.run(random_choice_empty_list)
    assert random_choice_empty_list_result is None, \
        "Random choice from empty list failed, found random term: %s" % random_choice_empty_list_

# Generated at 2022-06-13 14:03:48.561579
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    terms = ['a','b','c']
    ret = l.run(terms, inject={}, **{})
    assert ret[0] in terms

# Generated at 2022-06-13 14:03:52.886270
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # create a LookupModule object
    lm = LookupModule()

    # create a list of cmd line args
    terms = ['open', 'backup']

    # invoke run() method of the LookupModule object
    # print the return value
    print(lm.run(terms))

# Generated at 2022-06-13 14:03:57.892187
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Test data
    terms = ['test1', 'test2', 'test3']

    # Test run
    ret = LookupModule().run(terms)

    # Test assert
    assert ret in terms

# Generated at 2022-06-13 14:04:04.373682
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    print('\nTesting LookupModule class')
    from ansible.utils.display import Display
    display = Display()
    terms = ['first', 'second', 'third']

    print('\nTest if the method returns the random term')
    display.display('\nInput : %s' % terms)
    lookup = LookupModule()
    final = lookup.run(terms)[0]
    display.display('Output : %s' % final)
    assert final in terms
    print('\nTest passed')

# Generated at 2022-06-13 14:04:08.059705
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    assert module.run(["Apple","Orange","Banana","Pear"]) in ["Apple","Orange","Banana","Pear"]
    assert module.run(["Apple","Orange","Banana","Pear"]) in ["Apple","Orange","Banana","Pear"]
    assert module.run(["Apple","Orange","Banana","Pear"]) in ["Apple","Orange","Banana","Pear"]

# Generated at 2022-06-13 14:04:09.976960
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    instance = LookupModule()
    terms = ['1', '2', '3']
    result = instance.run(terms)
    assert result in terms

# Generated at 2022-06-13 14:04:21.754578
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    terms = ["a", "b", "c", "d", "e", "f", "g"]
    # get random.choices from module random
    old_choices = random.choices
    random.choices = lambda x, k=1: old_choices(x, k)
    # store the result of choices on a list
    random_choices = []

    # build loop
    for i in range(1000):
        lkp = LookupModule()
        random_choices.append(lkp.run(terms))

    # call a function from random_choice module to check if the list random_choices is empty
    assert(not all_same(random_choices))

# function to check if all elements of list are same

# Generated at 2022-06-13 14:04:25.525902
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_ins = LookupModule()
    assert len(lookup_ins.run([4,5,6])) == 1
    assert lookup_ins.run([4,5,6])[0] in [4,5,6]

# Generated at 2022-06-13 14:04:31.343243
# Unit test for method run of class LookupModule
def test_LookupModule_run():
  # Arrange
  expected_result = ['do nothing']
  args = [
    [
      "go through the door",
      "drink from the goblet",
      "press the red button",
      "do nothing"
    ]
  ]

  # Act
  lm = LookupModule()
  actual_result = lm.run(args)

  # Assert
  assert (actual_result == expected_result)

# Generated at 2022-06-13 14:04:40.710902
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # set up
    # define Mock module for unit test
    class MockModule(object):

        def __init__(self, *args, **kwargs):
            pass

        def fail_json(self, *args, **kwargs):
            self.exception = args[0]

        def exit_json(self, *args, **kwargs):
            self.exit_args = args
            self.exit_kwargs = kwargs

        def set_fact(self, *args, **kwargs):
            self.exit_args = args
            self.exit_kwargs = kwargs

    import copy
    mock_module = MockModule()
    mock_module.exit_args = None
    mock_module.exit_kwargs = None
    mock_module.exception = None

    lookup_module = LookupModule()
   

# Generated at 2022-06-13 14:04:51.521760
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # We don't need real module injected into lookup plugin
    class TestModule(object):
        def __init__(self, **kwargs):
            self.params = kwargs

    # We don't need real templating, that makes our life easier
    class TestTemplar(object):
        def __init__(self, basedir, vault_password=None):
            pass

        @staticmethod
        def template(data):
            return data

    # Test runner
    def test_runner(terms, **kwargs):
        lookup = LookupModule(TestTemplar(None), TestModule(**kwargs))
        return lookup.run(terms, inject=None, **kwargs)

    # Test our method
    assert 'a' in test_runner(['a'])

# Generated at 2022-06-13 14:04:59.116031
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    input = [['choice_1', 'choice_2'], ['choice_1', 'choice_2', 'choice_3'], ['choice_1', 'choice_2'], ['choice_1'], []]
    expected = [['choice_1'], ['choice_1'], ['choice_1'], ['choice_1'], []]
    random_lookup = LookupModule()
    results = []
    for terms in input:
        results.append(random_lookup.run(terms))
    assert results == expected

# Generated at 2022-06-13 14:05:05.654110
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    ret = [random.choice(['test1', 'test2', 'test3', 'test4'])]
    return ret

# Generated at 2022-06-13 14:05:09.574769
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    results = LookupModule().run([1,2])
    print(results)

# Test for method run of class LookupModule
print(test_LookupModule_run.__name__)
test_LookupModule_run()

# Generated at 2022-06-13 14:05:12.223770
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    x = LookupModule()
    assert x.run([1, 2, 3])[0] in (1, 2, 3)

# Generated at 2022-06-13 14:05:15.297746
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["a", "b", "c"]
    random_choice = "a"
    random_choice_from_terms = LookupModule().run(terms,None,None)[0]
    assert random_choice == random_choice_from_terms

# Generated at 2022-06-13 14:05:20.220614
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_input = [
        ['term1', 'term2', 'term3'],
        ['term1'],
        []
    ]
    test_output = [
        ['term3'],
        ['term1'],
        []
    ]
    test_instance = LookupModule()
    for test_i in range(len(test_input)):
        res = test_instance.run(test_input[test_i])
        assert res == test_output[test_i]

# Generated at 2022-06-13 14:05:24.687231
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    with pytest.raises(AnsibleError):
        # Method run should raise an AnsibleError
        # if it fails to select a random choice
        lookup_plugin = LookupModule()
        lookup_plugin.run()

# Generated at 2022-06-13 14:05:28.094290
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["a", "b", "c"]
    lookup_plugin = LookupModule()
    assert lookup_plugin.run(terms) in terms
    assert lookup_plugin.run([]) == []

# Generated at 2022-06-13 14:05:31.354909
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    try:
        result_1 = LookupModule().run([])
        assert result_1 == []
        result_2 = LookupModule().run(['List Elements'])
        assert result_2 == ['List Elements']
    except AssertionError:
        raise

# Generated at 2022-06-13 14:05:39.933829
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Unit test for method run of class LookupModule"""
    # Unit test for run method with terms as None
    terms = None
    inject = None
    kwargs = {}
    expected_result = []
    lookup_obj = LookupModule()
    actual_result = lookup_obj.run(terms, inject, **kwargs)
    assert actual_result == expected_result, \
        'Expected Result: {}. Actual Result: {}'.format(expected_result, actual_result)
    # Unit test for run method with terms as a valid list
    terms = [1, 2, 3, 4, 5]
    expected_result = [3]
    actual_result = lookup_obj.run(terms, inject, **kwargs)

# Generated at 2022-06-13 14:05:44.633311
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    terms = ["apple", "banana", "orange", "watermelon", "kiwi"]
    actual = lookup_module.run(terms)
    assert actual in terms, \
        "LookupModule run should return the random selected item from list: %s. But it returned %s" % (terms, actual)

# Generated at 2022-06-13 14:05:59.049213
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    random.seed(1)
    lookup_random_choice = LookupModule()
    result = lookup_random_choice.run(terms=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
    assert result == [1]

# Generated at 2022-06-13 14:06:03.400190
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Test that LookupModule.run() selects a random element of a passed list
    """
    input_list = ["go through the door", "drink from the goblet", "press the red button"]

    lm = LookupModule()
    assert lm.run(terms=input_list) in input_list

# Generated at 2022-06-13 14:06:04.832326
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule
    result = module.run()
    assert result == ["test"]

# Generated at 2022-06-13 14:06:16.892928
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test with empty list
    x = LookupModule()
    result = x.run([])
    assert result == []

    # Test with list with one element
    x = LookupModule()
    result = x.run(['go through the door'])
    assert result == ['go through the door']

    # Test with list with two element
    x = LookupModule()
    result = x.run(['go through the door', 'push the button'])
    assert(result in [['go through the door'], ['push the button']])

    # Test with list with three element
    x = LookupModule()
    result = x.run(['go through the door', 'push the button', 'stop'])
    assert(result in [['go through the door'], ['push the button'], ['stop']])

    # Test

# Generated at 2022-06-13 14:06:19.892964
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    m = LookupModule()
    items = ['a','b','c']
    assert(m.run(items) in ['a', 'b', 'c'])

# Generated at 2022-06-13 14:06:23.533280
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    defList = [ 'one', 'two', 'three' ]
    terms = [ { 'list' : defList } ]
    lookup_instance = LookupModule()
    result = lookup_instance.run(terms)
    assert result in defList

# Generated at 2022-06-13 14:06:26.385187
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    set_terms = ['Darth Vader', 'Luke Skywalker']
    result = lookup_module.run(set_terms)
    assert len(result) == 1
    assert result[0] in set_terms

# Generated at 2022-06-13 14:06:30.384496
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()
    terms = ["a", "b", "c"]
    choice = lookup_plugin.run(terms)
    assert choice[0] in terms
    return True


# Generated at 2022-06-13 14:06:34.786019
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()

    # no argument
    assert l.run([]) == []

    # 1 argument
    assert l.run(["a"]) == ["a"]

    # multiple arguments
    assert l.run(["a", "b", "c"]) in [["a"], ["b"], ["c"]]

# Generated at 2022-06-13 14:06:37.079061
# Unit test for method run of class LookupModule
def test_LookupModule_run():
  if 'LookupModule' in globals() and 'LookupBase' in globals():
    lookup = LookupModule()
    result = lookup.run(["a", "b", "c"])
    assert result == "a" or result == "b" or result == "c"

# Generated at 2022-06-13 14:07:01.699617
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    terms = ['test1','test2','test3','test4','test5']
    ret = lookup_module.run(terms)
    assert isinstance(ret, list)
    assert len(ret) == 1
    assert ret[0] in terms

# Generated at 2022-06-13 14:07:04.919782
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["a", "b", "c", "d", "e"]

    results = []
    for i in range(0, 100):
        results.append(LookupModule().run(terms))

    assert sorted(terms) == sorted(results)

# Generated at 2022-06-13 14:07:09.806506
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # setup parameters
    terms = ['something', 'something', 'something', 'another thing']
    # run method
    answer = LookupModule().run(terms)
    # check result
    assert(answer in terms)

# Generated at 2022-06-13 14:07:12.909875
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['a', 'b']
    lookupModule = LookupModule()
    result = lookupModule.run(terms, inject=None, **{})
    assert result == ['a'] or result == ['b']

# Generated at 2022-06-13 14:07:20.893550
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils._text import to_text
    from ansible.module_utils.common.collections import is_sequence
    l = LookupModule()
    terms = ['apple', 'orange', 'banana']
    result = l.run(terms)
    assert is_sequence(result)
    assert len(result) == 1
    assert to_text(result[0]) in terms

# Generated at 2022-06-13 14:07:25.572387
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    random.seed(1)
    terms = [1]
    assert [random.choice(terms)] == LookupModule().run(terms)
    random.seed(2)
    terms = [1,2]
    assert [random.choice(terms)] == LookupModule().run(terms)
    random.seed(3)
    terms = [1,2,3]
    assert [random.choice(terms)] == LookupModule().run(terms)

# Generated at 2022-06-13 14:07:36.910973
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleSequence

    lookup_plug = LookupModule()


# Generated at 2022-06-13 14:07:42.612974
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_instance = LookupModule()
    assert lookup_instance.run(["foo","bar"], ["baz"]) == ["foo"]
    assert lookup_instance.run(["foo","bar"], ["baz"]) == ["bar"]
    assert lookup_instance.run(["foo","bar"], ["baz"]) in (["foo"],["bar"])

# Generated at 2022-06-13 14:07:47.676374
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    #The function test_LookupModule_run is used to test
    #the run method of class LookupModule
    dic = {'a':1,'b':2,'c':3,'d':4,'e':5}
    lst = list(dic)
    for _ in range(10):
        assert lst.index(LookupModule().run(lst))<len(lst)

# Generated at 2022-06-13 14:07:51.076149
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_LookupModule = LookupModule()
    lookup_terms = ['foo', 'bar', 'baz']
    result = test_LookupModule.run(lookup_terms)
    assert result[0] in lookup_terms

# Generated at 2022-06-13 14:08:35.442637
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    instantiator = LookupModule()
    assert isinstance(instantiator, LookupBase)
    assert isinstance(instantiator.run([3]), list)
    assert instantiator.run([3])[0] in [3]

# Generated at 2022-06-13 14:08:42.129190
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # TODO: Implement test case
    lookup = {"name": "random_choice", "args": [["foo", "bar", "baz", "quux"]]}
    task_vars = dict()

    lm = LookupModule()
    result = lm.run(lookup['args'], task_vars=task_vars)

    assert result[0] in set(lookup['args'][0])

# Generated at 2022-06-13 14:08:46.443078
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = [
        'a',
        'b',
        'c'
    ]

    test = LookupModule()
    ret = test.run(terms)
    assert ret == [random.choice(terms)]

# Generated at 2022-06-13 14:08:49.077860
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["foo", "bar", "baz"]
    result = LookupModule().run(terms)
    assert result in terms

# Generated at 2022-06-13 14:08:53.055050
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    result = [u"go through the door", u"drink from the goblet", u"press the red button", u"do nothing"]
    lambda_obj = lambda: result
    ret = LookupModule().run([result], lambda_obj)
    assert ret == result

# Generated at 2022-06-13 14:08:58.169590
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    random.seed(10)
    test_obj = LookupModule()
    terms = ['term1', 'term2', 'term3']
    ret = test_obj.run(terms)
    assert ret[0] == ['term3']

# Generated at 2022-06-13 14:09:02.425661
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    selection = lookup.run(['First', 'Second', 'Third', 'Fourth'])
    assert selection
    assert 'First' in selection
    assert 'Second' in selection
    assert 'Third' in selection
    assert 'Fourth' in selection



# Generated at 2022-06-13 14:09:04.772586
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    LookupModule().run(['a','b','c'])
    LookupModule().run(terms=['a','b','c'])

# Generated at 2022-06-13 14:09:08.201842
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['one', 'two', 'three']
    assert len(terms) == 3
    assert isinstance(terms, list)

    ret = [random.choice(terms)]
    assert len(ret) == 1
    assert isinstance(ret, list)
    assert ret[0] in terms

# Generated at 2022-06-13 14:09:15.066600
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import random
    import unittest
    from ansible.module_utils._text import to_native
    class TestLookupModule(unittest.TestCase):
        '''Unit test for LookupModule run'''
        def test_run(self):
            '''Test run method'''
            self.assertIsNotNone(random.SystemRandom())
            terms = ['a', 'b', 'c']
            self.assertNotEqual(LookupModule().run(terms, None), terms)
            self.assertTrue(LookupModule().run(terms, None, variable_start_string='{{').pop() in terms, "random item is not part of list")

    unittest.main()

if __name__ == '__main__':
    test_LookupModule_run()

# Generated at 2022-06-13 14:10:46.007972
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lm = LookupModule()
    d = ["foo", "bar", "baz"]
    r = lm.run(d)

    assert r[0] in d



# Generated at 2022-06-13 14:10:49.924082
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    '''lookup_plugins/random_choice.py:LookupModule.run()'''
    test_terms = ['one', 'two', 'three', 'four', 'five']
    assert(len(LookupModule().run(terms=test_terms)) == 1)

# Generated at 2022-06-13 14:10:52.344381
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()
    terms = [1, 2, 3, 4]
    ret = lookup_plugin.run(terms, inject=None, **{})
    assert(ret in terms)

# Generated at 2022-06-13 14:10:54.917210
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    assert LookupModule().run(terms = [1, 2, 3]) == [1, 2, 3]
    assert LookupModule().run(terms = ["a", "b", "c"]) == ["a", "b", "c"]

# Generated at 2022-06-13 14:10:58.493627
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup_module = LookupModule()
    terms = ['foo', 'bar']

    # test without terms
    assert lookup_module.run(terms=None) == None

    # test with valid terms
    for i in range(0,10):
        assert lookup_module.run(terms=terms) in terms

# Generated at 2022-06-13 14:11:02.915812
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    module = LookupModule()
    assert module.run("it is a string") == ["it is a string"]
    assert module.run([1,2,3,4]) == [4]
    assert module.run("") == ""

# Generated at 2022-06-13 14:11:12.361901
# Unit test for method run of class LookupModule
def test_LookupModule_run():

	obj = LookupModule(loader=None, templar=None, shared_loader_obj=None)

	# Test with integer values
	arr = ['7','2','9']
	ret = obj.run(terms=arr, inject=None, **{})
	assert ret == arr

	# Test with string values
	arr = ['noah_jaffe','ansible_noah','ansible_test']
	ret = obj.run(terms=arr, inject=None, **{})
	assert ret == arr

	# Test with mixed values

# Generated at 2022-06-13 14:11:14.276424
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l.run(["12", "3", "4"])

# Generated at 2022-06-13 14:11:16.302903
# Unit test for method run of class LookupModule
def test_LookupModule_run():
   l = LookupModule()
   assert isinstance(l,LookupModule)
   assert l.run([1,2,3]) == [2]

# Generated at 2022-06-13 14:11:19.872981
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ["First","Second"]
    elements = lookup.run(terms)
    for element in elements:
        assert(element in terms)