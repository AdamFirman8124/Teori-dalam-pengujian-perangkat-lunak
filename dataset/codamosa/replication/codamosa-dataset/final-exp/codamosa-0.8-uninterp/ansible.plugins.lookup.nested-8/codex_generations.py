

# Generated at 2022-06-13 14:03:01.006601
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible.plugins.lookup import LookupModule
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.utils.vars import combine_vars

    lm = LookupModule()
    mock_data_loader = DataLoader()
    mock_variable_manager = VariableManager()
    lm.set_loader(mock_data_loader)
    lm.set_templar(mock_variable_manager.get_vars)
    lm.set_inventory(InventoryManager(loader=mock_data_loader, sources=[]))

    # test success with a valid nested list

# Generated at 2022-06-13 14:03:12.309739
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    cm = LookupModule()
    assert [['ankur', 'bob'], ['ankur', 'jerry'], ['ankur', 'tom'], ['rick', 'bob'], ['rick', 'jerry'], ['rick', 'tom']] == cm.run([['ankur', 'rick'],['bob', 'jerry', 'tom']])
    assert [['ankur-', 'bob-'], ['ankur-', 'jerry-'], ['ankur-', 'tom-'], ['rick-', 'bob-'], ['rick-', 'jerry-'], ['rick-', 'tom-']] == cm.run([['ankur-', 'rick-'],['bob-', 'jerry-', 'tom-']])

# Generated at 2022-06-13 14:03:19.144023
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    ########################################################################################
    #   Demonstrating the use of a class that is nested in a class defined in another file
    ########################################################################################

    # Create an instance of class LookupModule
    my_lookupModule = LookupModule()

    # Expected output from 'my_list'
    my_list = [(0, 0), (0, 1), (1, 0), (1, 1)]

    # Test if method 'run' returns the expected output
    assert(my_lookupModule.run([[0, 1], [0, 1]]) == my_list)

# Generated at 2022-06-13 14:03:28.657771
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six.moves import StringIO
    try:
        from __main__ import display
    except ImportError:
        from ansible.utils.display import Display
        display = Display()

    display.verbosity = 3

    mylookup = LookupModule()
    z = mylookup.run
    # testing the example in DOCUMENTATION string above
    vars = {
        "users": [
            "alice",
            "bob",
        ]
    }
    # (the following line would be the same as using "with_nested: " in a playbook)
    result = z([[vars["users"], ["clientdb", "employeedb", "providerdb"]]], variables=vars)

# Generated at 2022-06-13 14:03:40.686002
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = [
        [
            'alice',
            'bob'
        ],
        [
            'clientdb',
            'employeedb',
            'providerdb'
        ]
    ]
    new_lookup_module = LookupModule()
    result = new_lookup_module.run(terms)

# Generated at 2022-06-13 14:03:48.521359
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils._text import to_text
    import sys
    import pytest

    my_list = [ ['localhost', 'example2.com'], ['a', 'b', 'c'] ]

    try:
        l = LookupModule()
        l.run(terms=my_list)
    except Exception:
        # Without the to_text translation, the assert will see b'...' instead
        # of '...' and fail. This happens in Python 3.
        pytest.fail("Exception raised: %s" % to_text(sys.exc_info()[1]))

# Generated at 2022-06-13 14:04:00.301917
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    l = LookupModule()
    l.set_loader()
    l.set_templar()
    with pytest.raises(AnsibleError):
        l.run(terms = [])
    assert l.run(terms = [['x'], ['y']]) == [['x', 'y']]
    assert l.run(terms = [['x', 'y'], ['z']]) == [['x', 'z'], ['y', 'z']]
    assert l.run(terms = [['x', 'y'], ['z'], ['a', 'b']]) == [['x', 'z', 'a'], ['x', 'z', 'b'], ['y', 'z', 'a'], ['y', 'z', 'b']]

# Generated at 2022-06-13 14:04:05.782383
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    # TODO: set up a mock loader
    result = lookup.run()
    if len(result) != 1:
        raise Exception('LookupModule_run() result length should be 1 but is %s' % len(result))
    if result[0] != [None, None]:
        raise Exception('LookupModule_run() result should be [None, None] but is %s' % result[0])
test_LookupModule_run()


# Generated at 2022-06-13 14:04:13.638177
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    input = [
        [
            [ 'alice', 'bob' ],
            [ 'clientdb', 'employeedb', 'providerdb' ]
        ],
        '*'
    ]
    output = lm.run(input,'')
    assert output == [['alice', 'clientdb'], ['alice', 'employeedb'], ['alice', 'providerdb'], ['bob', 'clientdb'], ['bob', 'employeedb'], ['bob', 'providerdb']]

    input = [
        [
            [ 'alice', 'bob' ],
            [ 'clientdb', 'employeedb', 'providerdb' ],
            [ 'select', 'insert', 'update' ]
        ],
        '*'
    ]

# Generated at 2022-06-13 14:04:24.856822
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    test_dict = {'fruits': ['apple','banana','cherry','durian'],'vegetables': ['artichoke','brocoli','carrot','corn']}
    terms = [['fruits','vegetables']]

    test_obj = LookupModule()
    result = test_obj.run(terms, variables=test_dict)


# Generated at 2022-06-13 14:04:35.412429
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    myL = LookupModule()

    # Case 1:
    #
    #   terms:
    #       [
    #           ['a','b','c']
    #       ]
    #   returns:
    #       [
    #           ['a'],
    #           ['b'],
    #           ['c']
    #       ]
    assert myL.run([['a','b','c']]) == [['a'],['b'],['c']]

    # Case 2:
    #
    #   terms:
    #       [
    #           ['a','b','c'],
    #           ['1','2']
    #       ]
    #   returns:
    #       [
    #           ['a','1'],
    #           ['b','1'],
    #           ['c','1

# Generated at 2022-06-13 14:04:43.643322
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    result = module.run([ [[1, 2], [3]], [4, 5] ])
    assert result == [[1, 2, 4], [1, 2, 5], [3, 4], [3, 5]]
    result = module.run([[4, 5], [6, 7], [8, 9]])
    assert result == [[4, 6, 8], [4, 6, 9], [4, 7, 8], [4, 7, 9], [5, 6, 8], [5, 6, 9], [5, 7, 8], [5, 7, 9]]
    result = module.run([[4, 5], [6, 7], [8, 9], [10, 11]])

# Generated at 2022-06-13 14:04:55.285443
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    class TestClass:
        def __init__(self, input_list, length_list, expected_list):
            self.input_list = input_list
            self.length_list = length_list
            self.expected_list = expected_list
            self.test_obj = LookupModule()

        def __str__(self):
            return """
             input_list: %s
             length_list: %s
             expected_list: %s
             """ % (self.input_list, self.length_list, self.expected_list)

        def run_test(self):
            output = self.test_obj.run(self.input_list)
            if len(output) != self.length_list:
                raise AssertionError("ERROR: Testcase failed. \nDetails:\n %s" % str(self))

# Generated at 2022-06-13 14:05:04.227189
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Preparation
    terms = [ [ 'alice', 'bob' ], [ 'clientdb', 'employeedb', 'providerdb'] ]
    lookup = LookupModule()

    # Test
    actual = lookup.run(terms)

    # Assertion
    expected = [('alice', 'clientdb'),
                ('bob', 'clientdb'),
                ('alice', 'employeedb'),
                ('bob', 'employeedb'),
                ('alice', 'providerdb'),
                ('bob', 'providerdb')]
    assert actual == expected

# Generated at 2022-06-13 14:05:15.003658
# Unit test for method run of class LookupModule
def test_LookupModule_run():
   # Creating object of class LookupModule
   lookup_module_object = LookupModule()

   # Calling run with arguments 
   # terms = [[['a1', 'a2'], ['b1', 'b2'], ['c1', 'c2']],['x', 'y', 'z']]
   # variables = None
   # kwargs = {}

   actual_result = lookup_module_object.run(terms = [[['a1', 'a2'], ['b1', 'b2'], ['c1', 'c2']],['x', 'y', 'z']], variables = None, **{})

   # Expected result 

# Generated at 2022-06-13 14:05:20.689229
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Testing empty list of lists
    lookup_module = LookupModule()
    try:
        lookup_module.run([])
    except AnsibleError as e:
        assert "with_nested requires at least one element in the nested list" == str(e)
    # Testing list of lists of length 1
    assert [['a']] == lookup_module.run([['a']])
    # Testing list of lists of length 1 with variables
    assert [['a']] == lookup_module.run([['a']], variables={})
    assert [['a'], ['b']] == lookup_module.run([['a', 'b']], variables={})
    # Testing two lists of length 1
    assert [['a', 'b']] == lookup_module.run([['a'], ['b']])

# Generated at 2022-06-13 14:05:31.684241
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Sample test case
    # All the input arguments are passed to method run as a dictionary
    args = {
        # A list of lists which are to be composed
        "terms": [ [1, 2], [3, 4] ],
    }

    # Instantiate object of class LookupModule
    lookup_obj = LookupModule()

    # Call method run of class LookupModule
    # for sample test case with
    # arguments  args
    temp_obj = lookup_obj.run(**args)

    # Expcted output of method run
    expected = [
        [1, 3],
        [1, 4],
        [2, 3],
        [2, 4]
    ]

    # Assert method run gives output as expected
    assert temp_obj == expected

# Generated at 2022-06-13 14:05:40.115438
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    test1 = [
        'first-list-element',
        ['second-list-element1', 'second-list-element2'],
        ['third-list-element1', 'third-list-element2', 'third-list-element3'],
        ['fourth-list-element1', 'fourth-list-element2', 'fourth-list-element3', 'fourth-list-element4']
    ]
    result1 = LookupModule().run(test1)


# Generated at 2022-06-13 14:05:51.477517
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    def get_first_element_of_each_list(list_of_lists):
        result = []
        for each_list in list_of_lists:
            result.append(each_list[0])
        return result


# Generated at 2022-06-13 14:06:03.794644
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    """ Unit test for method run of class LookupModule """
    from ansible.plugins.lookup.nested import LookupModule
    lookup_nested_obj = LookupModule()
    my_list = [['a','b','c','d','e'],['A','B','C','D','E'],['1','2','3','4'],
               ['alpha','beta','gamma','delta','epsilon','zeta']]

# Generated at 2022-06-13 14:06:17.515809
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    test_terms = [ [ 'alice', 'bob' ],
                   [ 'clientdb', 'employeedb', 'providerdb' ] ]
    result = lookup_module.run(test_terms)
    assert result == [ [ 'alice', 'clientdb' ], [ 'alice', 'employeedb' ], [ 'alice', 'providerdb' ],
                       [ 'bob', 'clientdb' ], [ 'bob', 'employeedb' ], [ 'bob', 'providerdb' ] ]

    test_terms = [ ['alice'], ['clientdb', 'employeedb', 'providerdb'] ]
    result = lookup_module.run(test_terms)

# Generated at 2022-06-13 14:06:27.342322
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create a list which contains the terms passed to LookupModule.run
    terms = [
        [
            "app1",
            "app2"
        ],
        [
            "db1",
            "db2"
        ],
        [
            "firewall1",
            "firewall2"
        ]
    ]
    # Create an instance of LookupModule
    l = LookupModule()
    # Call method LookupModule.run
    result = l.run(terms)
    # Assert our result

# Generated at 2022-06-13 14:06:38.248385
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    runner = CliRunner()

    # Error because empty list
    result = runner.invoke(test_cli, ['nested', '[]'])
    assert result.exit_code == 1
    assert "with_nested requires at least one element in the nested list" in result.output

    # Error because one of the nested variables is undefined
    result = runner.invoke(test_cli, ['nested', '[\'{{ undefined }}\']'])
    assert result.exit_code == 1
    assert "One of the nested variables was undefined" in result.output

    # Standard operation
    result = runner.invoke(test_cli, ['nested', '[\'a\', \'b\'],[\'1\', \'2\', \'3\']'])
    assert result.exit_code == 0

# Generated at 2022-06-13 14:06:46.617881
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    l = LookupModule()
    assert [["a", "b", "c"], ["a", "b", "d"], ["a", "e", "c"], ["a", "e", "d"], ["f", "b", "c"],
            ["f", "b", "d"], ["f", "e", "c"], ["f", "e", "d"]] == l.run([
                ["d", "c"],
                ["b", "a", "f"],
                ["e"],
            ])

# Generated at 2022-06-13 14:06:54.691020
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Setup test fixture
    lm = LookupModule()

    test_terms = [
        [
            "a",
            "b",
            "c"
        ],
        [
            "1",
            "2",
            "3"
        ],
        [
            "!",
            "@",
            "#"
        ]
    ]


# Generated at 2022-06-13 14:07:05.917787
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    # Case 1, empty arguments
    assert not module.run([], {}, {})
    # Case 2, empty terms
    assert not module.run([{}], {}, {})
    # Case 3, empty terms
    assert not module.run([{},{},{}], {}, {})
    # Case 4, 3 empty arguments
    assert not module.run([[],[]], {}, {})
    # Case 5, 1 empty argument, 2 non-empty arguments
    assert not module.run([[],['a','b'],['c']], {}, {})
    # Case 6, 1 empty argument with multiple elements, 2 non-empty arguments
    assert not module.run([[],['a','b'],['c','d']], {}, {})
    # Case 7, 1 empty argument with multiple elements,

# Generated at 2022-06-13 14:07:17.014476
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    result = lm.run([["1", "2"], ["a", "b", "c"], ["A", "B"]], variables=None, **{})
    assert result == [['1', 'a', 'A'], ['2', 'a', 'A'], ['1', 'b', 'A'], ['2', 'b', 'A'], ['1', 'c', 'A'], ['2', 'c', 'A'], ['1', 'a', 'B'], ['2', 'a', 'B'], ['1', 'b', 'B'], ['2', 'b', 'B'], ['1', 'c', 'B'], ['2', 'c', 'B']]

# Generated at 2022-06-13 14:07:23.043589
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_mod = LookupModule()
    try:
        ret = lookup_mod.run(
            [
                [["user1", "user2"], ["db1", "db2"],["p1", "p2"]],
                [["password1"], ["password2"]]
            ],
            variables=dict(
                db1 = "i_db1",
                db2 = "i_db2",
                p1 = "i_p1",
                p2 = "i_p2"
            )
        )
    except AnsibleError:
        pass
    else:
        assert len(ret) == 4
        assert (ret[0] == ['user1', 'i_db1', 'i_p1', 'password1'])

# Generated at 2022-06-13 14:07:28.692720
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = [['a','b','c'],[1,2,3]]
    result = lookup.run(terms)
    assert result == [['a',1],['a',2],['a',3],['b',1],['b',2],['b',3],['c',1],['c',2],['c',3]]

# Generated at 2022-06-13 14:07:38.842548
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_plugin = LookupModule()
    terms = [
        [ 'a', 'b' ],
        [ 'c', 'd', 'e' ],
        [ '1', '2', '3', '4', '5' ]
    ]

# Generated at 2022-06-13 14:07:51.003959
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    #Test empty list
    lookup_instance = LookupModule()
    terms = []
    try:
        result = lookup_instance.run(terms)
    except AnsibleError as e:
        assert e.message == "with_nested requires at least one element in the nested list"
    else:
        assert False

    #Test list containing one element
    lookup_instance = LookupModule()
    terms = [[1, 2, 3]]
    result = lookup_instance.run(terms)
    expected_result = [[1, 2, 3]]
    assert result == expected_result

    #Test list containing one element
    lookup_instance = LookupModule()
    terms = [[1, 2, 3], [4, 5, 6]]
    result = lookup_instance.run(terms)

# Generated at 2022-06-13 14:08:00.634234
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:08:03.837469
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    t = LookupModule()
    print(t.run([[["a", "b"], ["c", "d"]], [1, 2]]))

# Generated at 2022-06-13 14:08:11.108121
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # create mock term
    term1 = [
        ['a', 'b', 'c'],
        ['1', '2', '3', '4'],
        ['!', '@', '#'],
        ['$', '%', '^', '&'],
    ]

    # create mock variable
    variable = ['foo', 'bar']

    # create the lookup
    lu = LookupModule()

    # run the test
    result = lu.run(term1, variable)

    # check the results

# Generated at 2022-06-13 14:08:18.686757
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    my_module=LookupModule()
    test_result = my_module.run([["a", "b", "c"], ["d", "e", "f"]])
    assert test_result == [['a', 'd'], ['a', 'e'], ['a', 'f'], ['b', 'd'], ['b', 'e'], ['b', 'f'], ['c', 'd'], ['c', 'e'], ['c', 'f']]

# Generated at 2022-06-13 14:08:30.528387
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = [
        [ "client1", "client2", "client3"],
        ["d1", "d2", "d3"]
        ]
    test_obj = LookupModule()
    new_result = test_obj.run(terms)
    expected_result = [
        ["client1", "d1"],
        ["client1", "d2"],
        ["client1", "d3"],
        ["client2", "d1"],
        ["client2", "d2"],
        ["client2", "d3"],
        ["client3", "d1"],
        ["client3", "d2"],
        ["client3", "d3"]
        ]
    assert new_result == expected_result
    print("Unit test for method run of class LookupModule passed")


# Generated at 2022-06-13 14:08:42.750599
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    my_list1 = [["alice", "bob"], ["clientdb", "employeedb", "providerdb"]]
    my_list2 = [["alice", "bob"], ["clientdb", "employeedb", "providerdb"], ["admin", "monitor", "maintain"]]

    # Expected results
    result1 = [["alice", "clientdb"], ["alice", "employeedb"], ["alice", "providerdb"], ["bob", "clientdb"], ["bob", "employeedb"], ["bob", "providerdb"]]

# Generated at 2022-06-13 14:08:52.518623
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Assign
    my_test = LookupModule()

    # Arrange
    name = 'test_name'
    priv = 'test_priv'
    append_privs = 'test_append_privs'
    password = 'test_password'
    terms = [[name], [priv, '.'], [append_privs], [password]]
    expected_result = [['test_name', 'test_priv', '.', 'test_append_privs', 'test_password']]

    # Act
    result = my_test.run(terms)

    # Assert
    assert expected_result == result

# Generated at 2022-06-13 14:08:59.089492
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup_module = LookupModule()
    lookup_module._templar = MockTemplar()
    result = lookup_module.run([ ['a', 'b'], ['1', '2'] ], variables=dict())
    assert [ ["a", "1"], ["a", "2"], ["b", "1"], ["b", "2"] ] == result

    result = lookup_module.run([ ['a', 'b'], ['1', '2'] ], variables=dict())
    assert [ ["a", "1"], ["a", "2"], ["b", "1"], ["b", "2"] ] == result

    result = lookup_module.run([ ['a', 'b'], ['1', '2'], ['A', 'B'] ], variables=dict())

# Generated at 2022-06-13 14:09:08.842547
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.compat.tests.mock import patch
    from ansible.plugins.loader import lookup_loader

    with patch('ansible.parsing.dataloader.DataLoader'):
        lookup = lookup_loader.get('nested')

    base_terms = [['a', 'b', 'c'], [1, 2, 3]]

    # create actual terms from base_terms
    terms = [[y for y in x] for x in base_terms]

    for term in terms:
        for i in range(len(term)):
            term[i] = str(term[i])

    results = lookup.run(terms=terms, variables={})
    assert results == [[x, y] for x in terms[0] for y in terms[1]]

# Generated at 2022-06-13 14:09:21.083831
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Create an instance of LookupModule class
    lookupModule = LookupModule()

    # Call run method of LookupModule class
    result = lookupModule.run(
        [
            [
                'alice',
                'bob'
            ],
            [
                'clientdb',
                'employeedb',
                'providerdb'
            ]
        ],
        None
    )

    # Assert results

# Generated at 2022-06-13 14:09:32.043670
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    results = lookup.run(['alice', ['clientdb', 'employeedb', 'providerdb']], dict())
    assert results == [[u'alice', u'clientdb'], [u'alice', u'employeedb'], [u'alice', u'providerdb']]
    results = lookup.run([['alice', 'bob'], ['clientdb', 'employeedb', 'providerdb']], dict())
    assert results == [[u'alice', u'clientdb'], [u'alice', u'employeedb'], [u'alice', u'providerdb'], [u'bob', u'clientdb'], [u'bob', u'employeedb'], [u'bob', u'providerdb']]

# Generated at 2022-06-13 14:09:38.818324
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()

    test_terms = [
        [
            "apples",
            "oranges",
            "pears",
            "lemons",
            "limes"
        ], [
            1,
            2,
            3
        ]
    ]


# Generated at 2022-06-13 14:09:47.098024
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    terms = [['alice', 'bob'], ['clientdb', 'employeedb', 'providerdb']]
    lookup_plugin = LookupModule()
    result = lookup_plugin.run(terms)
    assert len(result) == 6
    assert "alice" in result[0]
    assert "clientdb" in result[0]
    assert "alice" in result[1]
    assert "employeedb" in result[1]
    assert "alice" in result[2]
    assert "providerdb" in result[2]
    assert "bob" in result[3]
    assert "clientdb" in result[3]
    assert "bob" in result[4]
    assert "employeedb" in result[4]
    assert "bob" in result[5]

# Generated at 2022-06-13 14:09:58.166401
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    lookup_module = LookupModule()
    result = lookup_module.run([[1, 2, 3], [4, 5, 6], [7, 8, 9]], variables=None, **{})

# Generated at 2022-06-13 14:10:03.299480
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module_obj = LookupModule()
    terms = [['a','b','c'], [1,2,3]]
    result = lookup_module_obj.run(terms)
    assert result == [['a', 1], ['a', 2], ['a', 3], ['b', 1], ['b', 2], ['b', 3], ['c', 1], ['c', 2], ['c', 3]]

# Generated at 2022-06-13 14:10:09.286204
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    # Specify arguments of method run of class LookupModule as input
    my_list = [['alice', 'bob'], ['clientdb', 'employeedb', 'providerdb']]
    my_result = LookupModule().run(my_list)

    # Specify expected result
    expected_result = [['alice', 'clientdb'], ['alice', 'employeedb'], ['alice', 'providerdb'], ['bob', 'clientdb'], ['bob', 'employeedb'], ['bob', 'providerdb']]

    # Compare expected result with the result of method run of class LookupModule
    assert my_result == expected_result

# Generated at 2022-06-13 14:10:17.576366
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    input_list = [['alice', 'bob'], ['clientdb', 'employeedb', 'providerdb']]
    expected_result = [['alice', 'clientdb'], ['alice', 'employeedb'], ['alice', 'providerdb'],
                       ['bob', 'clientdb'], ['bob', 'employeedb'], ['bob', 'providerdb']]
    lookup_module = LookupModule()
    result = lookup_module.run(input_list)
    assert result == expected_result
# END Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:10:26.570155
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    print("test LookupPlugin.run()")
    empty_list = []
    expected_empty_list = []
    first_list = [1, 2]
    second_list = [3, 4, 5]
    expected_list = [
        [1, 3],
        [1, 4],
        [1, 5],
        [2, 3],
        [2, 4],
        [2, 5],
    ]
    first_list_second_list = [first_list, second_list]
    second_list_first_list = [second_list, first_list]
    third_list = [6]

# Generated at 2022-06-13 14:10:33.900833
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import pytest
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.listify import listify_lookup_plugin_terms
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    from ansible.plugins.lookup.nested import LookupModule

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='')
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    terms = listify_lookup_plugin_terms(['[host1]', '[host2,host3]'])
    lookup_module = LookupModule()
    result = lookup_module.run(terms, variable_manager=variable_manager, loader=loader, templar=None)

# Generated at 2022-06-13 14:10:45.799920
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    input_list_2_dim= [
        [2, 3],
        [4, 5],
        [6, 7]
    ]
    expected_result_2_dim = [
        [2, 4, 6],
        [2, 4, 7],
        [2, 5, 6],
        [2, 5, 7],
        [3, 4, 6],
        [3, 4, 7],
        [3, 5, 6],
        [3, 5, 7]
    ]
    test_lookupModule = LookupModule()
    result = test_lookupModule.run(input_list_2_dim)
    if result == expected_result_2_dim:
        print("[PASS] 2D list test")
    else:
        print("[FAIL] 2D list test")

    input_list

# Generated at 2022-06-13 14:10:54.161303
# Unit test for method run of class LookupModule
def test_LookupModule_run():

    print("\n\n Testing method: run from  Lookup Module \n")

    # Case 1: The nested list supplied is a list of empty lists, The expected output of the method is an empty list
    test_lookup_module = LookupModule()

    test_list_1 = [[]]
    expected_result_1 = []

    result_1 = test_lookup_module.run(test_list_1)

    print("Input: ", test_list_1)

    print("Expected output: ", expected_result_1)
    print("Actual output: ", result_1)

    if expected_result_1 == result_1:
        print("Success")
    else:
        print("Failure")

    # Case 2: The nested list supplied is a list of lists of valid elements
    # The expected output of the method is the correct

# Generated at 2022-06-13 14:11:00.676097
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lm = LookupModule()
    print(lm.run([['foo', 'bar'], ['1', '2']]))
    print(lm.run([['foo', 'bar'], ['1', '2'], ['a', 'b']]))
    print(lm.run([[['foo', 'bar'], ['1', '2']], ['a', 'b']]))
    print(lm.run([[['foo', 'bar'], ['1', '2']], ['a', 'b'], ['x', 'y']]))
    print(lm.run([['foo'], ['1', '2'], ['a', 'b'], ['x', 'y']]))

# Generated at 2022-06-13 14:11:11.036284
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    import sys
    import os.path

    script_path = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(script_path + "/../")

    from ansible.module_utils.six import PY2
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.utils.vars import merge_hash

    script_path = os.path.dirname(os.path.realpath(__file__))
    test_data_path = script_path + "/../tests/test_data/"
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.utils.unsafe_proxy import Ans

# Generated at 2022-06-13 14:11:21.605284
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    obj = LookupModule()
    assert isinstance(obj, LookupModule)

# Generated at 2022-06-13 14:11:30.102763
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    terms = [
             ['alice', 'bob'],
             ['clientdb', 'employeedb', 'providerdb'],
            ]
    terms_results = module._lookup_variables(terms, None)
    assert(terms_results == [['alice', 'bob'], ['clientdb', 'employeedb', 'providerdb']])
    results = module.run(terms, None)
    expected = [
                ['alice', 'clientdb'],
                ['alice', 'employeedb'],
                ['alice', 'providerdb'],
                ['bob', 'clientdb'],
                ['bob', 'employeedb'],
                ['bob', 'providerdb'],
               ]
    assert(results == expected)

# Generated at 2022-06-13 14:11:36.951908
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    my_list = []
    l = LookupModule()
    assert my_list == l.run(my_list)
    my_list = ["a", "b"]
    assert [["a", "b"]] == l.run(my_list)
    my_list = ["a b", "c d"]
    assert [["a b", "c d"]] == l.run(my_list)
    my_list = ["a", "b", "c d", "e f"]
    assert [['a', 'b'], ['a', 'c d'], ['a', 'e f'], ['b', 'c d'], ['b', 'e f'], ['c d', 'e f']] == l.run(my_list)
    my_list = [['a', 'b'], ['b', 'c']]

# Generated at 2022-06-13 14:11:41.851284
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    print('In test_LookupModule_run')
    module = LookupModule()
    y = module.run([[1, 2], ['a', 'b']])
    print(y)
    assert y == [[1, 'a'], [1, 'b'], [2, 'a'], [2, 'b']]



# Generated at 2022-06-13 14:11:45.309445
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    module = LookupModule()
    result = module.run([[[u'test1'], [u'test2']]], variables=u'test')
    assert result == [[u'test1', u'test2']]

# Generated at 2022-06-13 14:11:54.096960
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup = LookupModule()
    terms = [
        "{{ apple }}",
        "{{ orange }}"
    ]
    apple_list = [
        "alice",
        "bob",
        "carol",
    ]
    orange_list = [
        "mary",
        "jane"
    ]
    result_list = [
        [
            "alice",
            "mary"
        ],
        [
            "alice",
            "jane"
        ],
        [
            "bob",
            "mary"
        ],
        [
            "bob",
            "jane"
        ],
        [
            "carol",
            "mary"
        ],
        [
            "carol",
            "jane"
        ]
    ]

# Generated at 2022-06-13 14:12:04.602299
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils._text import to_bytes
    lo = LookupModule()
    input_data = [["1","2"],["a","b"]]
    myvars = {'var1': 'test'}
    expected_result = [['1','a'],['1','b'],['2','a'],['2','b']]
    result = lo.run(input_data, variables=myvars)
    assert len(expected_result) == len(result)
    assert [to_bytes(x) for x in expected_result] == [to_bytes(x) for x in result]


# Generated at 2022-06-13 14:12:15.563609
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    mylookup = LookupModule()
    returned_list = mylookup.run([['a', 'b'], ['1', '2', '3']])
    assert returned_list == [[u'a', u'1'], [u'a', u'2'], [u'a', u'3'], [u'b', u'1'], [u'b', u'2'], [u'b', u'3']], \
        "with_nested error - got %s, expected %s" % (returned_list, [[u'a', u'1'], [u'a', u'2'], [u'a', u'3'], [u'b', u'1'], [u'b', u'2'], [u'b', u'3']])
    returned_list = my

# Generated at 2022-06-13 14:12:27.283152
# Unit test for method run of class LookupModule

# Generated at 2022-06-13 14:12:34.970816
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    argument_spec = {
        '_raw': dict(type='raw'),
    }
    test_LookupModule = LookupModule(None, argument_spec, None, None, None)
    assert test_LookupModule.run('[1,2,3]') == [[1], [2], [3]]
    assert test_LookupModule.run('[1,2,3]', '[4,5,6]') == [[1, 4], [1, 5], [1, 6], [2, 4], [2, 5], [2, 6], [3, 4], [3, 5], [3, 6]]

# Generated at 2022-06-13 14:12:45.037369
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    lookup_module = LookupModule()
    assert lookup_module.run([[1,2],['a','b']]) == [[1,'a'],[1,'b'],[2,'a'],[2,'b']]
    assert lookup_module.run([[1,2],[3,4]]) == [[1,3],[1,4],[2,3],[2,4]]
    assert lookup_module.run([[1,2],[3,4],['a','b']]) == [[1,3,'a'],[1,3,'b'],[1,4,'a'],[1,4,'b'],[2,3,'a'],[2,3,'b'],[2,4,'a'],[2,4,'b']]


# Generated at 2022-06-13 14:12:56.950279
# Unit test for method run of class LookupModule
def test_LookupModule_run():
    from ansible.module_utils._text import to_bytes
    import ansible.parsing.yaml.objects
    lookup_module = LookupModule()
    terms = [["1", "2"], ["3", "4"]]
    terms = ansible.parsing.yaml.objects.AnsibleMapping.construct_mapping(None, terms)
    result = lookup_module.run(terms, None, variable_start_string = '[[', variable_end_string = ']]', allow_jinja = True)
    assert result == [[b'3', b'1'], [b'3', b'2'], [b'4', b'1'], [b'4', b'2']]
    #
    lookup_module = LookupModule()