

# Generated at 2022-06-13 14:02:54.465148
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    term = ["test1","test2","test3"]
    res = l.run(term)
    assert len(res) == 1
    assert res[0] in term

# Generated at 2022-06-13 14:02:58.113829
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()

    res = lookup.run([1, 2, 3], None)
    assert len(res) == 1
    assert res[0] in [1, 2, 3]

    res = lookup.run([], None)
    assert res == []

# Generated at 2022-06-13 14:03:02.656600
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # TODO: mock random.choice to simulate random.choice(terms)
    # return 'john'
    #
    # call lookup
    # check result
    #
    # mock random.choice to simulate random.choice(terms)
    # return 'jeff'
    #
    # call lookup
    # check result
    pass

# Generated at 2022-06-13 14:03:13.987530
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    with pytest.raises(AnsibleError):
        lookup_module.run([{}])
    with pytest.raises(AnsibleError):
        lookup_module.run([["nested_list"]])
    assert lookup_module.run(terms=["foo", "bar", "baz"]) == ["foo"]
    assert lookup_module.run(terms=["foo", "bar", "baz"]) == ["foo"]
    assert lookup_module.run(terms=["foo", "bar", "baz"]) == ["foo"]
    assert lookup_module.run(terms=["foo", "bar", "baz"]) == ["foo"]
    assert lookup_module.run(terms=["foo", "bar", "baz"]) == ["foo"]
    assert lookup_module

# Generated at 2022-06-13 14:03:15.693059
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    l.run(["a","b","c"])
    return l

# Generated at 2022-06-13 14:03:20.524824
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup = LookupModule()

    # Test with some well-formed list
    test_terms = [ "Ethiopia", "Benin", "Isle of Man", "Cambodia"]
    choice = lookup.run(test_terms)
    assert len(choice) == 1
    assert choice[0] in test_terms

    # Test with some badly-formed list
    test_terms = []
    choice = lookup.run(test_terms)
    assert len(choice) == 0

# Generated at 2022-06-13 14:03:24.536440
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lu = LookupModule()
    lu._templar = None
    some_terms = [
        "first choice",
        "second choice",
    ]
    ret = lu.run(some_terms)
    assert ret[0] in some_terms

# Generated at 2022-06-13 14:03:27.639156
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = [ "one", "two", "three", "four" ]
    random_choice = LookupModule().run(terms=terms)
    assert isinstance( random_choice, list )
    assert len( random_choice ) == 1
    assert random_choice[0] in terms

# Generated at 2022-06-13 14:03:39.245277
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    # Test empty list
    assert lookup.run(list()) == list()
    # Test single element
    assert lookup.run(list(["a"])) == list(["a"])
    # Test 2 elements
    assert len(lookup.run(list(["a", "b"]))) == 1
    assert lookup.run(list(["a", "b"])) in (list(["a"]), list(["b"]))
    # Test multiple elements
    assert len(lookup.run(list(["a", "b", "c"]))) == 1
    assert lookup.run(list(["a", "b", "c"])) in (list(["a"]), list(["b"]), list(["c"]))

# Generated at 2022-06-13 14:03:43.250732
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.plugins.lookup.random_choice import LookupModule
    terms=[1, 2, 3]
    returned_list=LookupModule().run(terms)
    assert type(returned_list) == list
    assert type(returned_list[0]) == int
    assert returned_list[0] in terms

# Generated at 2022-06-13 14:03:48.647932
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = ["hello", "world"]
    results = lookup.run(terms, None)
    assert results == [random.choice(terms)]

# Generated at 2022-06-13 14:04:00.508074
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """
    Check that when terms is only one element long, the return value is the same terms
    Check that when terms has more than one element and contain exactly one of the keys ["_terms", "lookup_type", "lookup_args", "lookup_value"],
        the return value is a list with only one element
    :return:
    """
    lookup = LookupModule()
    # Check that when terms is only one element long, the return value is the same terms
    assert lookup.run(["love"]) == ["love"]

    # Check that when terms has more than one element and contain exactly one of the keys ["_terms", "lookup_type", "lookup_args", "lookup_value"],
    #     the return value is a list with only one element

# Generated at 2022-06-13 14:04:03.019857
# Unit test for method run of class LookupModule
def test_LookupModule_run():
  lm = LookupModule()
  assert lm.run(['go through the door','drink from goblet']) == ['go through the door','drink from goblet']

# Generated at 2022-06-13 14:04:06.528936
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    input = ["term1", "term2", "term3"]
    output = ""
    lookup = LookupModule()
    for i in range(100):
        output = lookup.run(input)
        if output != input:
            break
    assert output == ["term1"] or output == ["term2"] or output == ["term3"]

# Generated at 2022-06-13 14:04:10.572300
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    assert lookup.run(["item1", "item2"]) == ["item1"] or lookup.run(["item1", "item2"]) == ["item2"]
    assert lookup.run(["item1", "item2", "item3"]) in ["item1", "item2", "item3"]

# Generated at 2022-06-13 14:04:15.459539
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = {'ansible': 'awesome', 'verbose': 'true', 'logging': 'warning'}
    choice = LookupModule().run([terms])
    assert choice in terms.keys()

# Generated at 2022-06-13 14:04:20.361966
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    assert lm.run(terms=["a", "b"]) in (["a"], ["b"])
    assert lm.run(terms=[]) == []
    assert lm.run(terms=["a", "b", "c"]) in (["a"], ["b"], ["c"])

# Generated at 2022-06-13 14:04:22.708889
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    x = LookupModule()
    #terms = x.run(terms, inject, **kwargs)


if __name__ == "__main__":
    test_LookupModule_run()

# Generated at 2022-06-13 14:04:27.493114
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup_plugin = LookupModule()

    # Check single item in list
    assert lookup_plugin.run(
        [ "one" ]
    ) == ["one"]

    # Check multiple items in list
    assert lookup_plugin.run(
        [ "one", "two", "three" ]
    ) in [["one"], ["two"], ["three"]]

# Generated at 2022-06-13 14:04:30.645952
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_mod = LookupModule()
    ret = lookup_mod.run(['a', 'b', 'c'])
    assert ret in [['a'], ['b'], ['c']]

# Generated at 2022-06-13 14:04:39.772194
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def test_exception_path(exception, terms):
        lookup = LookupModule()
        with pytest.raises(exception) as ex_info:
            lookup.run(terms)
        assert ex_info.type == exception

    terms = ['First', 'Second']
    lookup = LookupModule()
    assert lookup.run(terms) in terms
    test_exception_path(AnsibleError, "Terms")
    test_exception_path(AnsibleError, [1, 2, 3])

# Generated at 2022-06-13 14:04:48.401099
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test when terms is a non-empty list
    lookup_obj = LookupModule()
    terms = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    result = lookup_obj.run(terms,None)
    assert result in terms
    # Test when terms is empty list
    lookup_obj1 = LookupModule()
    terms1 = []
    result1 = lookup_obj1.run(terms1,None)
    assert result1 == terms1

# Generated at 2022-06-13 14:04:58.068412
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """Check that function run of class LookupModule returns a random element of the list given as argument or an empty list if no argument was passed"""
    random_list = ["value1", "value2", "value3"]
    random_list_returned = LookupModule().run(random_list)
    assert random_list_returned in random_list
    empty_list = []
    empty_list_returned = LookupModule().run(empty_list)
    assert empty_list_returned == empty_list
    assert type(random_list_returned) == str
    assert type(empty_list_returned) == list


# Generated at 2022-06-13 14:05:01.718562
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    instance = LookupModule()
    terms = [[1,2], '3']
    random_val = instance.run(terms)
    assert(instance.run(terms) in terms)



# Generated at 2022-06-13 14:05:06.175989
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # Populate a and b with test data, the empty list
    # is the expected result.
    a = ["a", "b", "c"]
    b = []
    c = ["c"]
    d = ["a", "b", "c", "d", "e", "f"]

    # Initialize an instance of LookupModule
    lookup_module = LookupModule()

    # What is the result of run() when terms = a?
    result = lookup_module.run(terms=a)

    # Check that the result was a list
    assert isinstance(result, list)

    # Is the length of the result one?
    assert len(result) == 1

    # Is the result a member of list a?
    assert result[0] in a

    # What is the result of run() when terms = b?

# Generated at 2022-06-13 14:05:13.574051
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # mock object for class LookupModule
    class _LookupModule:
        def run(self, terms, inject=None, **kwargs):
            return self.return_value
    
    lookup_module = _LookupModule() # object of class _LookupModule
    lookup_module.return_value = [1] # expected return value of run function
    assert lookup_module.run([1, 2, 3]) == lookup_module.return_value # test case: call run method on object with input [1, 2, 3]

# Generated at 2022-06-13 14:05:21.534330
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()

    terms1 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]
    terms2 = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]

# Generated at 2022-06-13 14:05:32.460874
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    loader = DataLoader()
    variable_manager = VariableManager()
    inv = InventoryManager(loader, variable_manager)
    host = Host('myhost')
    group = Group('mygrp')
    group.add_host(host)
    inv.add_group(group)
    variable_manager.set_inventory(inv)

    results = []

# Generated at 2022-06-13 14:05:34.545881
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule().run([1, 2, 3]) in ([[1], [2], [3]])

# Generated at 2022-06-13 14:05:39.905725
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_instance = LookupModule()

    # Empty list
    result = test_instance.run([], {})
    assert result == []

    # One element
    result = test_instance.run(["test"], {})
    assert result == ["test"]

    # Two elements
    result = test_instance.run(["test1", "test2"], {})
    assert result == ["test1"] or result == ["test2"]

    # Exception
    try:
        test_instance.run(None, {})
        assert False
    except AnsibleError:
        pass

# Generated at 2022-06-13 14:05:53.631737
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # create LookupModule object
    lm = LookupModule()
    # create list for test
    terms = ["element_1", "element_2", "element_3"]
    # test random_choice feature
    assert lm.run(terms=terms) in terms



# Generated at 2022-06-13 14:05:59.562473
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    print('LookupModule test')
    # Values depends on the execution context
    lookup_instance = LookupModule()
    terms = ['value1', 'value2']
    ret = lookup_instance.run(terms)
    assert isinstance(ret,list) 
    assert len(ret) == 1
    assert ret[0] in terms

# Generated at 2022-06-13 14:06:05.216727
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    
    # test case 1:
    terms = ['1', '2', '3', '4']
    expected = 1
    actual = len(lookup_module.run(terms))
    assert actual == expected

    # test case 2:
    terms = None
    expected = None
    actual = lookup_module.run(terms)
    assert actual == expected

# Generated at 2022-06-13 14:06:13.758898
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    random.seed(6)
    lookup_module = LookupModule()
    result = lookup_module.run([ "a", "b", "c", "d", "e" ])
    assert len(result) == 1
    assert result[0] == "c"
    result = lookup_module.run(["a", "b", "c", "d", "e"])
    assert len(result) == 1
    assert result[0] == "c"
    result = lookup_module.run([])
    assert len(result) == 0


# Generated at 2022-06-13 14:06:21.473509
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    try:
        import __main__
        __main__.LookupModule = LookupModule
    except ImportError:
        pass

    lookup_plugin = LookupModule()
    assert lookup_plugin.run(terms="test") == ['test']
    assert lookup_plugin.run(terms=['test']) == ['test']
    assert lookup_plugin.run(terms=['test', 'test2']) in [['test'], ['test2']]
    assert lookup_plugin.run(terms=[1.1, 'test']) in [[1.1], ['test']]
    assert lookup_plugin.run(terms={'a':'b'}) == [{'a':'b'}]

# Generated at 2022-06-13 14:06:24.312858
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    look = LookupModule()
    try:
        look.run("")
    except Exception as e:
        assert "Unable to choose random term: %s" % to_native(e)
    

# Generated at 2022-06-13 14:06:34.178852
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()

    # we don't need to test all of the LookupModule run method, just the new code
    # test when terms is None
    assert l.run(terms=None) == []

    # test when terms is an empty array
    assert l.run(terms=[]) == []

    # test when term is an array of one string
    assert l.run(terms=['test']) == ['test']

    # test when terms is an array of multiple strings
    assert l.run(terms=['test1', 'test2', 'test3']) in ['test1', 'test2', 'test3']

# Generated at 2022-06-13 14:06:42.294064
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_source = dict(
            name = "Ansible Play",
            hosts = 'localhost',
            gather_facts = 'no',
            tasks = [
                dict(action=dict(module='debug', args=dict(msg='{{foo}}')))
            ]
        )


# Generated at 2022-06-13 14:06:45.399786
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    result = module.run([1,2,3])
    assert(result in [1,2,3])

# Generated at 2022-06-13 14:06:46.045291
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    pass

# Generated at 2022-06-13 14:07:16.159760
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_cases = [
        {
            "test_terms": [1, 2, 3],
            "test_length": 3,
            "test_fail": False
        },
        {
            "test_terms": [],
            "test_length": 0,
            "test_fail": False
        },
        {
            "test_terms": [],
            "test_length": 1,
            "test_fail": True
        }
    ]
    for test_case in test_cases:
        lm = LookupModule()
        result = lm.run(test_case['test_terms'])

# Generated at 2022-06-13 14:07:20.990804
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Given a list of numbers,
    numbers = [1, 2, 3]
    # I expect the method run to return one of the numbers,
    assert any([n in LookupModule().run(numbers) for n in numbers])

# Generated at 2022-06-13 14:07:28.107055
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=inventory)


# Generated at 2022-06-13 14:07:31.272944
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    ll = LookupModule()
    ret = ll.run(['Test', 'Something'])
    assert len(ret) == 1
    assert ret[0] in ['Test', 'Something']

# Generated at 2022-06-13 14:07:34.864370
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    randomSet = ["a", "b", "c", "d", "e"]
    result = LookupModule().run(randomSet)
    assert result in randomSet
    assert type(result) == type([])

# Generated at 2022-06-13 14:07:39.514985
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Verification of positive scenario
    terms = ['go through the door','drink from the goblet','press the red button','do nothing']
    lookup_instance = LookupModule()
    assert len(lookup_instance.run(terms)) == 1

    # Verification of negative scenario, when terms is empty
    terms = []
    lookup_instance = LookupModule()
    assert len(lookup_instance.run(terms)) == 0

# Generated at 2022-06-13 14:07:43.281699
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_obj = LookupModule()
    terms = ['a', 'b', 'c']
    ret = lookup_obj.run(terms)
    assert ret != None
    assert len(ret) == 1
    assert ret[0] in terms

# Generated at 2022-06-13 14:07:52.736071
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    import random
    random.seed(1)

    wrong_terms = [(1,), [2], 3, 'string']
    expected_result = "Unable to choose random term: %s"

    terms = [[1],[2,3],[4,5,6]] #length=3
    for term in terms:
        lookup_module = LookupModule()
        actual_result = lookup_module.run(terms=term)
        assert len(actual_result) == 1, "Should be len(term)=1"
        assert actual_result[0] in term, "Should be in term"

    lookup_module = LookupModule()
    actual_result = lookup_module.run(terms=wrong_terms)
    exp_result = "Unable to choose random term: sequence item 0: expected string, tuple found"
    assert actual_result == exp

# Generated at 2022-06-13 14:07:55.505947
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def mock_ansible_module(terms, inject=None, **kwargs):
        return random.choice(terms)

    random_choice = mock_ansible_module(["yes", "no"])

    assert random_choice in ["yes", "no"]

# Generated at 2022-06-13 14:08:00.233926
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # FIXME: pick more efficient method for asserting equality
    def assertEqual(a, b):
        assert a == b

    module = LookupModule()

    # with_random_choice
    module_input = ['foo', 'bar']
    module_output = module.run(module_input)
    assertEqual(len(module_output), 1)
    assertEqual(module_output[0], 'foo' or 'bar')

# Generated at 2022-06-13 14:08:42.563220
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    
    ret = []

    #Execute method run(terms) of class LookupModule
    lookup_instance = LookupModule()
    result = lookup_instance.run(terms, inject=None)
    
    assert result[0] in terms
    assert result[0] not in ret
    ret.append(result[0])

# Generated at 2022-06-13 14:08:52.730024
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Test 1: test method run when input is a list of length 1
    lookup = LookupModule()
    terms = ["test"]
    result = lookup.run(terms)
    assert result == ["test"]

    # Test 2: test method run when input is a list of length 5
    lookup = LookupModule()
    terms = ["test", "test2", "test3", "test4", "test5"]
    result = lookup.run(terms)
    assert result == ["test"] or result == ["test2"] or result == ["test3"] or result == ["test4"] or result == ["test5"]

test_LookupModule_run()

# Generated at 2022-06-13 14:08:57.321623
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    terms = ["go through the door",
             "drink from the goblet",
             "press the red button",
             "do nothing"]

    l = LookupModule()
    l.run(terms)

# Generated at 2022-06-13 14:09:07.220269
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Empty indexes or None indexes
    test1 = []
    test2 = None
    # None value
    test3 = None
    # Empty value
    test4 = []
    # Normal value
    test5 = ["one", "two", "three", "four", "five"]
    test6 = ["one", "two", "three", "four", "five"]
    assert LookupModule().run(test1) == test1
    assert LookupModule().run(test2) == test2
    assert LookupModule().run(test3) == test3
    assert LookupModule().run(test4) == test4
    assert LookupModule().run(test5) != test5
    assert LookupModule().run(test6) != test6

# Generated at 2022-06-13 14:09:16.334177
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    look = LookupModule()
    assert look.run(["a","b","c"]) == ["a"]
    assert look.run(["a","b","c"]) == ["a"]
    assert look.run([]) == []
    assert look.run(['a','b','c'], inject=1) == ["a"]
    assert look.run(['a','b','c'], inject=1, x=1) == ["a"]
    assert look.run('test') == ['test']
    assert look.run(['a','b','c'], inject=1, x=1) == ["a"]

# Generated at 2022-06-13 14:09:24.354671
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    # Test case 1: Random is choice is done when terms are provided
    terms = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    random_choice = lookup_module.run(terms)
    assert random_choice[0] in terms
    assert len(random_choice) == 1

    # Test case 2: Empty list is returned when terms is not provided
    terms = []

    random_choice = lookup_module.run(terms)
    assert len(random_choice) == 0


# Generated at 2022-06-13 14:09:27.296763
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    msg = "go through the door"
    terms = [msg]
    lu = LookupModule()
    result = lu.run(terms)
    assert result[0] == msg

# Generated at 2022-06-13 14:09:35.785960
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    arguments = dict()
    l = LookupModule()
    l.run(terms=['10.0.0.1','10.0.0.2','10.0.0.3','10.0.0.4','10.0.0.5','10.0.0.6','10.0.0.7','10.0.0.8','10.0.0.9','10.0.0.10'])

# Generated at 2022-06-13 14:09:37.904511
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_terms = ['hello', 'world', '!']

    lookup_module = LookupModule()
    assert lookup_module.run(test_terms)[0] in test_terms

# Generated at 2022-06-13 14:09:39.798471
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    assert LookupModule().run(["foo", "bar"]) == ["foo"] or LookupModule().run(["foo", "bar"]) == ["bar"]

# Generated at 2022-06-13 14:11:03.668375
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    # test with no arguments
    lookup_module = LookupModule()
    try:
        lookup_module.run([])
        assert False, "Exception not raised"
    except AnsibleError as e:
        assert "Unable to choose random term: " in to_native(e)

    # test with arguments
    lookup_module = LookupModule()
    try:
        lookup_module.run([1, 2, 3])
        assert True
    except:
        assert False, "Exception raised"

# Generated at 2022-06-13 14:11:08.750686
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    arguments = {'terms': [['a', 'b', 'c']], 'inject': None, 'kwargs': {}}
    lookup_plugin = LookupModule()
    response = lookup_plugin.run(**arguments)
    assert(len(response) == 1)
    assert(response[0] in ['a', 'b', 'c'])


# Generated at 2022-06-13 14:11:11.885297
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = [1, 2, 3, 4]
    l = LookupModule()
    assert (type(l.run(terms)) == list), "The type of list should be list"
    assert (len(l.run(terms)) == 1), "The length of list should be 1"

# Generated at 2022-06-13 14:11:16.346599
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    obj = LookupModule({})
    assert obj.run([]) == []
    assert obj.run(['choice1', 'choice2']) == ['choice1']
    assert obj.run(['choice1', 'choice2']) == ['choice2']
    assert obj.run(['choice1', 'choice2']) == ['choice1']

# Generated at 2022-06-13 14:11:22.349903
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    result = module.run([])
    assert result == [], "result: %s" % result

    result = module.run(['a','b'])
    assert result in (['a'],['b']), "result: %s" % result

    result = module.run([1,2,3])
    assert result in ([1], [2], [3]), "result: %s" % result

# Generated at 2022-06-13 14:11:30.477283
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    def my_choice(L):
        "A deterministic choice function for our unit test"
        return L[0]
    import unittest.mock as mock
    mock.choice = my_choice
    lu = LookupModule()
    res = lu.run([1,2,3])
    assert res == [1]
    lu.set_options({"random": True})
    res = lu.run([1,2,3])
    assert res == [1]
    lu.set_options({"random": False})
    res = lu.run([1,2,3])
    assert res == [1]
    lu.set_options({})
    res = lu.run([1,2,3])
    assert res == [1]

# Generated at 2022-06-13 14:11:31.799624
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    assert lookup_module.run([1,2,3]), [1]

# Generated at 2022-06-13 14:11:38.720524
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    lookup = LookupModule()
    result = lookup.run(terms)
    assert result[0] in terms

# Generated at 2022-06-13 14:11:40.523122
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    assert lm.run(['i', 'love', 'you'])


# Generated at 2022-06-13 14:11:43.929919
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test_object = LookupModule()
    assert test_object.run(terms=["a","b","c"]) == ["a","b","c"]