

# Generated at 2022-06-13 14:02:58.257564
# Unit test for method run of class LookupModule
def test_LookupModule_run():

  assert LookupModule().run(["list"]) == ["list"]
  assert LookupModule().run(["1", "2", "3", "4"]) in ["1", "2", "3", "4"]

# Generated at 2022-06-13 14:03:05.067100
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import sys
    import datetime
    import random
    import time

    class MockModule():
        params = {}

    # set seed so we can get same result all time
    random.seed(datetime.datetime.now())
    test_instance = LookupModule(MockModule())

    term_list = ["superstition", "mystic", "etc"]
    # test with list switch
    test_instance.run(terms=term_list)
    assert test_instance.run(terms=term_list) in [["superstition"], ["mystic"], ["etc"]]

    # test with empty list
    assert test_instance.run(terms=None) is None

    # test with empty string
    assert test_instance.run(terms="") is None

    # test with single string

# Generated at 2022-06-13 14:03:14.948930
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    import os
    import unittest

    # Get ansible-runner to inject the plugin. LookupModule() is imported
    import ansible.runner.lookup_plugins.random_choice  # pylint: disable=unused-variable

    terms = ["red", "blue", "green"]

    class Test_LookupModule(unittest.TestCase):
        """ Unit test of LookupModule.run() """

        def setUp(self):
            self.test_lookup = LookupModule()

        def tearDown(self):
            pass

        def test_run_returns_1_item_from_terms(self):
            """Test that LookupModule.run() returns a list containing one item from terms """
            result = self.test_lookup.run(terms)


# Generated at 2022-06-13 14:03:17.117327
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["first value", "second value", "third value"]
    ret = LookupModule().run(terms)
    assert ret[0] in terms

# Generated at 2022-06-13 14:03:26.301404
# Unit test for method run of class LookupModule
def test_LookupModule_run():

     lookup = LookupModule()
     terms = ['a', 'b']
     result = lookup.run(terms, inject=None, **{})
     assert len(result) == 1 and result[0] in terms
     result = lookup.run(terms, inject=None, **{'plugin_name': 'random_choice'})
     assert len(result) == 1 and result[0] in terms
     result = lookup.run(terms, inject=None, **{'plugin_name': 'random_choice', 'plugin_args': 'arg1 arg2'})
     assert len(result) == 1 and result[0] in terms

# Generated at 2022-06-13 14:03:28.459323
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    result = [1,2,3]
    terms = [1,2,3]
    lookup = LookupModule()
    assert lookup.run(terms) in result

# Generated at 2022-06-13 14:03:40.534940
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    print("<----Start test_LookupModule_run---->")
    # pass list as terms
    lookup_module = LookupModule()
    terms = ["1", "2", "3"]
    assert lookup_module.run(terms) in terms

    # pass list as terms
    lookup_module = LookupModule()
    terms = {"1": "foo", "2": "bar"}
    assert lookup_module.run(terms) in terms.values()

    # pass string as terms
    lookup_module = LookupModule()
    terms = ["1", "2", "3"]
    assert lookup_module.run(terms) in terms

    # pass none as terms
    lookup_module = LookupModule()
    terms = None
    assert lookup_module.run(terms) == None


# Generated at 2022-06-13 14:03:50.482235
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Mocking class LookupBase
    class LookupBase_Mock():

        def __init__(self, loader=None, templar=None, shared_loader_obj=None, **kwargs):
            pass

    LBase = LookupBase_Mock()

    LMod = LookupModule(LBase, loader=None, templar=None, shared_loader_obj=None)

    # Mocking data
    test_terms = [1, 2, 3, 4, 5]
    test_inject = None

    # Test 1:
    # Check returned value when terms is a list
    LMod.run(terms=test_terms)
    assert(type(LMod.run(terms=test_terms)) == list)

    # Test 2:
    # Check returned value when terms is None

# Generated at 2022-06-13 14:03:56.996773
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = [1, 2, 3, 4, 5]
    expected_terms = terms[:]
    random.shuffle(expected_terms)
    for t in [1,2,3,4,5]:
        random.seed(t)
        lm = LookupModule()
        ret = lm.run(terms)
        assert ret == [expected_terms[t-1]]

# Generated at 2022-06-13 14:04:00.933046
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    terms = ["first", "second", "third"]
    returned = l.run(terms)
    assert returned in terms
    assert returned[0] in terms
    assert len(returned) == 1
    assert returned is not terms

# Generated at 2022-06-13 14:04:07.285761
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_LookupModule = LookupModule()
    assert test_LookupModule.run([[1, 2, 3, 4]]) == [[1, 2, 3, 4]]
    assert test_LookupModule.run([]) is None
    assert test_LookupModule.run(None) is None

# Generated at 2022-06-13 14:04:11.169503
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    terms = ['a', 'b', 'c']
    assert lookup_module.run(terms) == terms[:]
    for i in range(100):
        assert lookup_module.run(terms) in terms
    assert lookup_module.run([]) == []
    assert lookup_module.run(None) == None

# Generated at 2022-06-13 14:04:13.258337
# Unit test for method run of class LookupModule
def test_LookupModule_run():
  print("test_LookupModule_run")
  assert False

# Generated at 2022-06-13 14:04:16.660555
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()
    terms = ["foo", "bar"]
    ret = lookup_plugin.run(terms)
    assert ret[0] in terms

# Generated at 2022-06-13 14:04:19.493765
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_obj = LookupModule()
    terms = ['foo', 'bar', 'baz']
    terms_out = lookup_obj.run(terms)
    assert terms_out in terms

# Generated at 2022-06-13 14:04:22.663516
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["foo", "bar", "baz"]
    assert LookupModule([None, None], None, None).run(terms) in terms

# Generated at 2022-06-13 14:04:24.864605
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test if method returns the expected value
    assert LookupModule.run([1]) == [1]

# Generated at 2022-06-13 14:04:27.007335
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    args = ['a', 'b', 'c']

    lookup = LookupModule()
    result = lookup.run(args)
    assert result in args

# Generated at 2022-06-13 14:04:28.857006
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_object = LookupModule()
    result = test_object.run([''])
    assert result == ['']

# Generated at 2022-06-13 14:04:34.157896
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.common.collections import ImmutableDict
    result = LookupModule().run([1, 2, 3], inject={'_use_unsafe_shell': False}, variable_manager=None, loader=None, templar=None,
                                shared_loader_obj=None, cache=False)
    assert ImmutableDict(changed=False, _ansible_no_log=False) == result.pop()

test_LookupModule_run() # Run unit test

# Generated at 2022-06-13 14:04:42.956907
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_obj = LookupModule()
    assert test_obj.run(['NRP', 'IPP', 'MPP', 'MRP']) == ['MPP']

# Generated at 2022-06-13 14:04:47.991385
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    print("Testing LookupModule_run")
    l = LookupModule()
    result = l.run(terms=[1, 2, 3, 4])
    assert isinstance(result, list)
    assert isinstance(result[0], int)
    assert result[0] in [1, 2, 3, 4]


# Generated at 2022-06-13 14:04:53.372762
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Most of this module is tested by the integration test in test/integration/targets/lookup_plugins/tests/random_choice.yml
    assert LookupModule.run([], ["asdf", "qwer", "zxcv"], {}) == ["zxcv"]
    assert LookupModule.run([], [], {}) == []

# Generated at 2022-06-13 14:05:05.180467
# Unit test for method run of class LookupModule
def test_LookupModule_run():
  test_terms = "test_terms"
  test_inject = "test_inject"
  test_kwargs = "test_kwargs"

  # Test 1: Check to see if the random term is selected and returned correctly
  lm_run_result_1 = LookupModule.run(LookupModule, test_terms, test_inject, test_kwargs)
  assert type(lm_run_result_1) is list
  assert len(lm_run_result_1) == 1
  assert lm_run_result_1[0] == test_terms

  # Test 2: Check to see if the random term is selected and returned correctly (different value returned)
  lm_run_result_2 = LookupModule.run(LookupModule, test_terms, test_inject, test_kwargs)
 

# Generated at 2022-06-13 14:05:09.752894
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ['test1','test2','test3']
    random.seed(1)
    result = lookup.run(terms)
    random.seed(1)
    expected = random.choice(terms)
    assert result[0] == expected

# Generated at 2022-06-13 14:05:13.839965
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Test the method run
    """
    lookup_value = [
        "two",
        "three",
        "five",
        "seven"
    ]

    # Test the method run
    lookup_module = LookupModule()
    lookup_result = lookup_module.run(
        lookup_value
    )

    for i in range(len(lookup_result)):
        assert lookup_result[i] in lookup_value

# Generated at 2022-06-13 14:05:16.433601
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    result = LookupModule().run(terms=['test1', 'test2'])
    assert type(result) == list
    assert len(result) == 1
    assert result[0] in ['test1', 'test2']

# Generated at 2022-06-13 14:05:23.303023
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule().run(["first", "second", "third"]) == ["second"]
    assert LookupModule().run(["first", "second", "third"]) == ["third"]
    assert LookupModule().run(["first", "second", "third"]) == ["third"]
    assert LookupModule().run(["first", "second", "third"]) == ["second"]
    assert LookupModule().run(["first", "second", "third"]) == ["second"]
    assert LookupModule().run(["first", "second", "third"]) == ["third"]
    assert LookupModule().run(["first", "second", "third"]) == ["third"]
    assert LookupModule().run(["first", "second", "third"]) == ["first"]

# Generated at 2022-06-13 14:05:29.670248
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    assert lookup.run(terms="['a','b','c']") == ['a']
    # assert lookup.run(terms=['a','b','c']) == ['a']
    assert lookup.run(terms=[['a'],['b'],['c']]) == [['a']]
    assert lookup.run(terms=[]) == []
    assert lookup.run(terms='hello') == 'hello'

# Generated at 2022-06-13 14:05:36.042109
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create an instance of LookupModule and assign the variables

    # Define the item list
    test_list = [
        "go through the door",
        "drink from the goblet",
        "press the red button",
        "do nothing",
    ]

    # Get the result
    result = LookupModule.run(test_list)

    # Verify the result
    assert isinstance(result, list)

# Generated at 2022-06-13 14:05:49.776960
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    with pytest.raises(AnsibleError) as e:
        LookupModule().run(0)
        assert 'Unable to choose random term' in to_native(e.value)

# Generated at 2022-06-13 14:05:54.233834
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    random.seed(16)
    ret = []
    module = LookupModule()
    terms = [ 'go through the door',
              'drink from the goblet',
              'press the red button',
              'do nothing' ]

    for i in range(100):
        ret = module.run(terms)

    assert ret == [ 'drink from the goblet' ]

# Generated at 2022-06-13 14:06:05.814003
# Unit test for method run of class LookupModule
def test_LookupModule_run():
  lookup = LookupModule()
  
  # Test 1
  terms = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
  random_terms = lookup.run(terms)
  assert(len(random_terms) == 1)
  assert(random_terms[0] in terms)
  
  # Test 2
  terms = ["One", "Two", "Three"]
  random_terms = lookup.run(terms)
  assert(len(random_terms) == 1)
  assert(random_terms[0] in terms)

  # Test 3
  terms = ["One"]
  random_terms = lookup.run(terms)
  assert(len(random_terms) == 1)
  assert(random_terms[0] in terms)
  
  #

# Generated at 2022-06-13 14:06:14.362665
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    from ansible.utils.display import Display
    from ansible.utils.plugin_docs import get_lookup_plugin_docs

    # Ansible configuration
    ansible_options = {}

    # SUT:
    lookup = LookupModule(Display())

    # Expected result
    expected_result = ['b', 'c']

    # Testing
    result = lookup.run(['a', 'b', 'c'], ansible_options, **get_lookup_plugin_docs('random_choice'))

    # Assertion
    assert result == expected_result

# Generated at 2022-06-13 14:06:20.467540
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test if the method run of class LookupModule returns one of the items
    # Test if the method run of class LookupModule returns the original list
    # if the given parameter is empty
    param_list = ["Test1", "Test2"]
    lookup = LookupModule()
    lookup_result = lookup.run(["Test1", "Test2"])
    assert(lookup_result[0] in param_list)

    lookup_result = lookup.run([])
    assert(lookup_result == [])

# Generated at 2022-06-13 14:06:21.245419
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 14:06:22.985794
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    assert type(test_LookupModule_run) == type(test_LookupModule_run)

# Generated at 2022-06-13 14:06:26.536468
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    terms = ['a', 'b']
    # test for successful select random term
    result = module.run(terms=terms)
    assert result[0] in terms

    # test for error select random term
    result = module.run([])
    assert result == []

# Generated at 2022-06-13 14:06:32.153495
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    terms = ["foo", "bar", "baz"]
    assert(l.run(terms, inject=None, **{}) in terms)
    assert(l.run(terms, inject=None, **{}) in terms)
    assert(l.run(terms, inject=None, **{}) in terms)

# Generated at 2022-06-13 14:06:35.204242
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()

    terms = [
        'one',
        'two',
        'three',
    ]
    random_choice = lm.run(terms)
    assert random_choice in terms

# Generated at 2022-06-13 14:07:07.590600
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()

    # Unit test: random choose item from a list
    terms = [1, 2, 3, 4, 5]
    result = lookup_plugin.run(terms=terms)
    assert isinstance(result, list) and len(result) == 1 and result[0] in terms

    # Unit test: random choose item from a list and inject variable
    terms = [1, 2, 3, 4, 5]
    inject = {'variable': 1}
    result = lookup_plugin.run(terms=terms, inject=inject)
    assert isinstance(result, list) and len(result) == 1 and result[0] in terms

    # Unit test: return no items
    terms = []
    result = lookup_plugin.run(terms=terms)

# Generated at 2022-06-13 14:07:11.753316
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()
    result = lookup_plugin.run([1,2,3,4], inject={'ENV': 'test'})
    assert(len(result) > 0)

# Generated at 2022-06-13 14:07:13.075894
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 14:07:21.859216
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module_obj = LookupModule()
    # 1st test case
    terms = ["My", "name", "is"]
    check_run_output = lookup_module_obj.run(terms)
    assert check_run_output == ["My", "name", "is"]

    # 2nd test case
    terms = ['test', 'list']
    check_run_output = lookup_module_obj.run(terms)
    assert check_run_output == ['test', 'list']

# Generated at 2022-06-13 14:07:25.279203
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    test_terms = [
        'foo',
        'bar',
        'baz',
        'quuux'
    ]
    random_choice = lookup.run(test_terms)
    assert random_choice in test_terms

# Generated at 2022-06-13 14:07:28.537585
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    terms = ['a', 'b', 'c']
    result = lookup_module.run(terms)
    assert result in terms

# Generated at 2022-06-13 14:07:37.564790
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six.moves import StringIO
    from ansible.module_utils.six import PY3

    lookup_module = LookupModule()
    if PY3:
        def u(x):
            return x
    else:
        def u(x):
            return unicode(x, "unicode_escape")

    result = lookup_module.run([u('foo'), u('bar'), u('baz')], None)
    result_elements = list(map(str, result))

    assert result_elements[0] in [u('foo'), u('bar'), u('baz')], "The random choice choice is not correct"



# Generated at 2022-06-13 14:07:42.415835
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Prepare the test class
    lookup_module = LookupModule()

    # Test the correct generation of a random element from the list
    assert lookup_module.run(["ansible", "is", "good"]) in ["ansible", "is", "good"]


# Generated at 2022-06-13 14:07:50.360396
# Unit test for method run of class LookupModule
def test_LookupModule_run(): # pylint: disable=C0103
    '''Test the method run of class LookupModule'''
    # Given
    test_object = LookupModule()
    test_terms = ['a', 'b', 'c']

    # When
    test_value_1 = test_object.run(terms=test_terms)
    test_value_2 = test_object.run(terms=test_terms)
    test_value_3 = test_object.run(terms=test_terms)

    # Then
    assert test_value_1 in test_terms
    assert test_value_2 in test_terms
    assert test_value_3 in test_terms
    assert test_object  # pylint: disable=R0104

# Generated at 2022-06-13 14:07:52.572961
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l.run(['a','b','c','d'])


# Generated at 2022-06-13 14:08:44.293658
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Random choice always a random number
    x = LookupModule()
    assert x.run([1,2,3,4,5,6,7,8,9])
    assert x.run([1,2,3,4,5,6,7,8,9])
    assert x.run([1,2,3,4,5,6,7,8,9])
    assert x.run([1,2,3,4,5,6,7,8,9])

# Generated at 2022-06-13 14:08:51.761822
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    result = lookup.run(["a", "b", "c"])
    if not isinstance(result, list):
        raise AssertionError("List is not list")
    if len(result) != 1:
        raise AssertionError("List length is not 1")
    if not result[0] in ["a", "b", "c"]:
        raise AssertionError("Value %s is not between a, b or c" % result[0])

# Generated at 2022-06-13 14:08:52.892681
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    #TODO: Implement it
    pass

# Generated at 2022-06-13 14:08:55.487491
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    data = ["one", "two", "three", "four", "five"]
    lookup_module = LookupModule()
    result = lookup_module.run(terms=data)
    assert result[0] in data


# Generated at 2022-06-13 14:09:00.221558
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    vm = LookupModule()
    terms = ["a", "b", "c", "d", "a", "b", "c", "d", "a", "b"]
    ret = vm.run(terms)
    assert ret in terms

# Generated at 2022-06-13 14:09:07.310691
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    assert lookup_module.run(['a','b','c']) == 'a' or lookup_module.run(['a','b','c']) == 'b' or lookup_module.run(['a','b','c']) == 'c'
    assert lookup_module.run(['a','b','c']) == ['a'] or lookup_module.run(['a','b','c']) == ['b'] or lookup_module.run(['a','b','c']) == ['c']

# Generated at 2022-06-13 14:09:08.977845
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()

    l.run(["a", "b", "c"])

# Generated at 2022-06-13 14:09:14.950244
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    ret = lookup.run(['test1', 'test2', 'test3'])
    assert "test" in ret[0]
    ret = lookup.run('')
    assert ret == ''
    ret = lookup.run(None)
    assert ret is None

# Generated at 2022-06-13 14:09:19.331299
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test: with terms
    terms = ["term_0", "term_1"]
    lookup = LookupModule()
    assert len(lookup.run(terms=terms)[0]) == len(terms[0])

    # Test: without terms
    lookup = LookupModule()
    assert len(lookup.run(terms=None)[0]) == 0

# Generated at 2022-06-13 14:09:22.780535
# Unit test for method run of class LookupModule
def test_LookupModule_run(): # pylint: disable=invalid-name
    '''
    Test if run() method of class LookupModule works properly
    '''
    lookup_obj = LookupModule()
    assert lookup_obj.run(['a', 'b']) == ['a'] or lookup_obj.run(['a', 'b']) == ['b']

# Generated at 2022-06-13 14:11:06.212307
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ['a', 'b', 'c']
    # test that run returns a list
    lookup_obj = LookupModule()
    myres = lookup_obj.run(terms)
    assert isinstance(myres, list)

# Generated at 2022-06-13 14:11:08.662423
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_object = LookupModule()
    terms = [1,2,3,4]
    value = lookup_object.run(terms, inject=None)
    assert value in terms

# Generated at 2022-06-13 14:11:12.107412
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_obj = LookupModule()
    res = lookup_obj.run([['hello'], ['world'], [1,2]])
    return res

if __name__ == '__main__':
    print("Lookup module random_choice, test result: '%s'" % test_LookupModule_run())

# Generated at 2022-06-13 14:11:14.413104
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    list = ['apple', 'banana', 'orange']
    word = LookupModule().run(list)
    assert word in list

# Generated at 2022-06-13 14:11:15.005031
# Unit test for method run of class LookupModule
def test_LookupModule_run():
  pass

# Generated at 2022-06-13 14:11:15.580558
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert False

# Generated at 2022-06-13 14:11:19.570569
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    looked_up_value = lookup_module.run(terms=["A", "B", "C"])
    assert looked_up_value in ["A", "B", "C"]

# Generated at 2022-06-13 14:11:21.944317
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    test_terms = ['apple', 'banana']
    assert(lookup_module.run(test_terms) in test_terms)


# Generated at 2022-06-13 14:11:30.235526
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a test execution environment
    from ansible.utils.vars import merge_hash

# Generated at 2022-06-13 14:11:31.564178
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l.run([1, 2, 3, 4, 5], None)