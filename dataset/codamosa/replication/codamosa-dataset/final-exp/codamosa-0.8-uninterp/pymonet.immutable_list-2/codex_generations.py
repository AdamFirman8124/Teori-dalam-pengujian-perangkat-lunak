

# Generated at 2022-06-14 03:16:57.942740
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList(1, ImmutableList(2)).find(lambda x: x == 1) == 1
    assert ImmutableList(1, ImmutableList(2)).find(lambda x: x == 2) == 2
    assert ImmutableList(1, ImmutableList(2)).find(lambda x: x == 3) is None
    assert ImmutableList.empty().find(lambda x: x == 3) is None



# Generated at 2022-06-14 03:16:59.809876
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    add_true = ImmutableList.of(True, False, True, False)
    assert add_true.find(lambda item: item) is True

# Generated at 2022-06-14 03:17:04.660212
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.empty() == ImmutableList()
    assert ImmutableList(1) == ImmutableList(1)
    assert ImmutableList(1, ImmutableList(2)) == ImmutableList(1, ImmutableList(2))
    assert ImmutableList(1, ImmutableList(2)) != ImmutableList(1, ImmutableList(1))
    assert ImmutableList(1, ImmutableList(2)) != ImmutableList(2, ImmutableList(2))


# Generated at 2022-06-14 03:17:15.850366
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(0, 1, -1, -2, 3, 4, 5, 6).filter(lambda x: x > 0) == [1, 3, 4, 5, 6]
    assert ImmutableList.of(0, 1, -1, -2, 3, 4, 5, 6).filter(lambda x: x < 0) == [-1, -2]
    assert ImmutableList.of(0, 1, -1, -2, 3, 4, 5, 6).filter(lambda x: x == 4) == [4]

# Generated at 2022-06-14 03:17:21.237525
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    l1 = ImmutableList(1, ImmutableList(2))
    l2 = ImmutableList(1, ImmutableList(2))
    assert l1 == l2

    l3 = ImmutableList(2, l2)
    assert l1 != l3



# Generated at 2022-06-14 03:17:36.297442
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    def test_filter(test_items: list, test_fn: Callable[[int], bool], test_expected_items: list):
        assert ImmutableList.of(*test_items).filter(test_fn).to_list() == test_expected_items

    test_filter([], lambda x: True, [])
    test_filter([1, 2, 3, 4], lambda x: False, [])
    test_filter([1, 2, 3, 4], lambda x: x == 1, [1])
    test_filter([1, 2, 3, 4], lambda x: x == 2, [2])
    test_filter([1, 2, 3, 4], lambda x: x == 3, [3])
    test_filter([1, 2, 3, 4], lambda x: x == 4, [4])

# Generated at 2022-06-14 03:17:42.253113
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    test_list = ImmutableList.of(1, 2, 3, 4, 5, 6)
    expected_result = 4
    actual_result = test_list.find(lambda x: x == expected_result)
    assert actual_result == expected_result

test_ImmutableList_find()

# Generated at 2022-06-14 03:17:47.492120
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    test_list_1 = ImmutableList.of(1, 2, 3)
    test_list_2 = ImmutableList.of(1, 2, 3)
    test_list_3 = ImmutableList.of(2, 3)

    assert test_list_1 == test_list_2
    assert test_list_1 != test_list_3


# Generated at 2022-06-14 03:17:53.686977
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList() == ImmutableList()
    assert ImmutableList('test') == ImmutableList('test')
    assert ImmutableList(100) == ImmutableList(100)

    assert ImmutableList(100) != ImmutableList(101)
    assert ImmutableList('test') != ImmutableList()

    assert ImmutableList('test', ImmutableList()) == ImmutableList('test', ImmutableList())
    assert ImmutableList('test', ImmutableList(100)) != ImmutableList('test', ImmutableList(200))


# Generated at 2022-06-14 03:18:05.677062
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    """ method __eq__ should return True if both are Instances of ImmutableList
        and all of their fields are equal
    """
    empty1 = ImmutableList.empty()
    empty2 = ImmutableList.empty()
    assert empty1 == empty2

    linked1 = ImmutableList(1)
    linked2 = ImmutableList(1)
    assert linked1 == linked2

    linked1 = ImmutableList(1, ImmutableList(2))
    linked2 = ImmutableList(1, ImmutableList(2))
    assert linked1 == linked2

    assert linked1 != empty1
    assert linked1 != 'string'
    assert linked1 != ImmutableList(1, 2)


# Generated at 2022-06-14 03:18:20.329865
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.of(1).__eq__(ImmutableList.of(1)) is True
    assert ImmutableList.of(1).__eq__(ImmutableList.of(2)) is False
    assert ImmutableList.of(1, 2, 3).__eq__(ImmutableList.of(1, 2, 3)) is True
    assert ImmutableList.of(1, 2, 3).__eq__(ImmutableList.of(1, 2, 2)) is False
    assert ImmutableList.empty().__eq__(ImmutableList.of(1)) is False
    assert ImmutableList.empty().__eq__(ImmutableList.empty()) is True
    assert ImmutableList.of(1).__eq__(ImmutableList.empty()) is False

# Generated at 2022-06-14 03:18:24.872911
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    list_to_find = ImmutableList.of(1, 2, 3, 4)

    assert list_to_find.find(lambda x: x == 3) == 3
    assert list_to_find.find(lambda x: x == 5) is None

# Generated at 2022-06-14 03:18:28.631012
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # Arrange
    list_instance = ImmutableList.of(1, 2, 3, 4, 5)
    # Act
    result = list_instance.find(lambda e: e == 2)
    # Assert
    assert result == 2

# Generated at 2022-06-14 03:18:32.677412
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    values = [1,2,3,4,5]
    list = ImmutableList.of(values[0], *values[1:])
    fn = lambda x: x == 5
    assert list.find(fn) is not None
    assert list.find(fn) == 5
    fn = lambda x: x == 0
    assert list.find(fn) is None
    assert list == list.find(fn)

# Generated at 2022-06-14 03:18:52.671803
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1).find(lambda x: x == 1) == 1
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 3) == 3
    assert ImmutableList.of(4, 5, 6).find(lambda x: x == 1) is None
    assert ImmutableList.of(4, 5).find(lambda x: x == 1) is None
    assert ImmutableList.of(4).find(lambda x: x == 1) is None
    assert ImmutableList.of(2, 3, 4, 5, 5).find(lambda x: x == 5) == 5
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 10) is None

# Generated at 2022-06-14 03:18:59.440486
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    empty_list = ImmutableList.empty()
    second_empty_list = ImmutableList.empty()
    string_list = ImmutableList.of('one')
    second_string_list = ImmutableList.of('one')
    integer_list = ImmutableList.of(1)
    second_integer_list = ImmutableList.of(1)

    not_empty_list = ImmutableList(False)

    assert empty_list == second_empty_list
    assert string_list == second_string_list
    assert integer_list == second_integer_list

    assert empty_list != not_empty_list
    assert string_list != integer_list
  

# Generated at 2022-06-14 03:19:08.106404
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    immutable_list = ImmutableList.of(1,2,3,4)
    result = immutable_list.filter(lambda x: x%2==0)
    assert isinstance(result, ImmutableList), 'test_ImmutableList_filter: result must be instance of ImmutableList'
    assert result == ImmutableList(2, ImmutableList(4)), 'test_ImmutableList_filter: result must be instance of ImmutableList'


# Generated at 2022-06-14 03:19:25.325577
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4)\
        .filter(lambda x: x > 2)\
        .to_list() == [3, 4]

    assert ImmutableList()\
        .filter(lambda x: x > 2)\
        .to_list() == []

    assert ImmutableList(1)\
        .filter(lambda x: x > 2)\
        .to_list() == []

    assert ImmutableList(1, 2, 3)\
        .filter(lambda x: x > 2)\
        .to_list() == [3]


# Generated at 2022-06-14 03:19:30.569102
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list_ = ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4, ImmutableList(5)))))
    new_list = list_.filter(lambda x: x % 2 == 0)
    assert new_list == ImmutableList(2, ImmutableList(4))



# Generated at 2022-06-14 03:19:32.515784
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.of(1, 2, 3) == ImmutableList.of(1, 2, 3)

# Generated at 2022-06-14 03:19:48.333365
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.of(1) == ImmutableList(1)
    assert ImmutableList(1) == ImmutableList(1)
    assert ImmutableList.empty() == ImmutableList(is_empty=True)
    assert ImmutableList(is_empty=True) == ImmutableList.empty()

# Generated at 2022-06-14 03:19:51.134788
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    # Should be equal to itself
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3)), False) == ImmutableList(1, ImmutableList(2, ImmutableList(3)), False)
    # Should not be equal to another ImmutableList
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3)), False) != ImmutableList(1, ImmutableList(2, ImmutableList(4)), False)


# Generated at 2022-06-14 03:20:01.118902
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    A = ImmutableList.of(1)
    B = ImmutableList.of(1, 2)
    C = ImmutableList.of(1)
    D = ImmutableList.of(None)
    E = ImmutableList.of(None, None)
    F = ImmutableList.of(None, 2)

    assert A != B
    assert A == C
    assert A != D
    assert D != E
    assert D != F



# Generated at 2022-06-14 03:20:08.527147
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList() == ImmutableList()

    assert ImmutableList(1) == ImmutableList(1)
    assert ImmutableList(1, ImmutableList(2)) == ImmutableList(1, ImmutableList(2))
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))) == ImmutableList(1, ImmutableList(2, ImmutableList(3)))

    assert ImmutableList(1) != ImmutableList()
    assert ImmutableList(1, ImmutableList(2)) != ImmutableList(1)
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))) != ImmutableList(1, ImmutableList(2))



# Generated at 2022-06-14 03:20:19.242952
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList([1, 2, 3]) == ImmutableList([1, 2, 3])
    assert ImmutableList([1, 2, 3]) != ImmutableList([1, 2, 4])
    assert ImmutableList([1, 2, 3]) != ImmutableList([1, 2])
    assert ImmutableList([]) != ImmutableList([1, 2, 3])
    assert ImmutableList([1, 2, 3]) != ImmutableList([])
    assert ImmutableList([1, 2, 3]) != ImmutableList()

# Generated at 2022-06-14 03:20:26.656318
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # arrange
    input_list = ImmutableList.of(1,3,2,2,3,4,5,7,6,8,9,10)
    # act
    result = input_list.filter(lambda x: x % 2 == 0)
    # assert
    expected_result = ImmutableList.of(2,2,4,6,8,10)
    assertEqual(result, expected_result)

test_ImmutableList_filter()

# Generated at 2022-06-14 03:20:40.173320
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():

    # Case 1: find item in list
    list1 = ImmutableList(1)
    list2 = list1.append(2)
    list3 = list2.append(3)

    result = list3.find(lambda item: item % 3 == 0)
    test_result = 3
    assert test_result == result, 'test_ImmutableList_find: test case 1 failed'

    # Case 2: find item in list
    list1 = ImmutableList(1)
    list2 = list1.append(2)
    list3 = list2.append(3)

    result = list3.find(lambda item: item % 5 == 0)
    test_result = None
    assert test_result == result, 'test_ImmutableList_find: test case 2 failed'


# Generated at 2022-06-14 03:20:44.157529
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    a_list = ImmutableList.of(1)
    b_list = ImmutableList.of(1)

    result = a_list == b_list

    assert result is True

# Generated at 2022-06-14 03:20:50.639217
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    li1 = ImmutableList.of('1', '2', '3', '4', '5', '6', '7')
    li2 = li1.filter(lambda x: not int(x) % 2)
    assert li2.to_list() == ['2', '4', '6']
    assert li1.to_list() == ['1', '2', '3', '4', '5', '6', '7']
    assert str(li1) == 'ImmutableList[1, 2, 3, 4, 5, 6, 7]'
    assert len(li1) == 7



# Generated at 2022-06-14 03:20:57.663030
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.empty().find(F(True)) == None
    assert ImmutableList(5).find(F(True)) == 5
    assert ImmutableList(5).find(F(False)) == None
    assert ImmutableList(5, ImmutableList(4, ImmutableList(3, ImmutableList(2, ImmutableList(1))))) \
        .find(F(True)) == 5
    assert ImmutableList(0, ImmutableList(4, ImmutableList(3, ImmutableList(2, ImmutableList(1))))) \
        .find(F(True)) == 4
    assert ImmutableList(0, ImmutableList(0, ImmutableList(3, ImmutableList(2, ImmutableList(1))))) \
        .find(F(True)) == 3

# Generated at 2022-06-14 03:21:18.035093
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.empty().filter(lambda s: s is not None) == ImmutableList(is_empty=True)
    assert ImmutableList(1).filter(lambda s: s is not None) == ImmutableList(1)
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))).filter(lambda s: s is not None) == ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))).filter(None) == ImmutableList(is_empty=True)
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))).filter(lambda x: x > 2) == ImmutableList(3) 

# Generated at 2022-06-14 03:21:23.323340
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    list_ = ImmutableList.of(0, 1, 2, 3)
    assert list_.find(lambda n: n == 3) == 3
    assert list_.find(lambda n: n == 4) == None
    assert ImmutableList.empty().find(lambda n: n == 3) == None



# Generated at 2022-06-14 03:21:27.459509
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.of(1, 2, 5) == ImmutableList.of(1, 2, 5)
    assert ImmutableList.of() == ImmutableList.empty()



# Generated at 2022-06-14 03:21:30.181264
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    empty_list = ImmutableList(is_empty=True)
    one_element_list = ImmutableList(10)
    two_elements_list = ImmutableList(10, ImmutableList(20))

    assert empty_list == ImmutableList(is_empty=True), "Test failed"
    assert one_element_list == one_element_list, "Test failed"
    assert two_elements_list == two_elements_list, "Test failed"


# Generated at 2022-06-14 03:21:40.427684
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    l1 = ImmutableList.of(1, 2, 3, 4)
    l2 = ImmutableList.of(1, 2, 3, 4)
    l3 = ImmutableList.of(1, 2, 3)
    l4 = ImmutableList.of(1, 2, 3, 5)
    l5 = ImmutableList.empty()
    l6 = ImmutableList.empty()

    assert(l1 == l2)
    assert(l2 == l1)
    assert(l3 == l3)
    assert(l4 == l4)
    assert(l5 == l5)
    assert(l1 != l3)
    assert(l1 != l4)
    assert(l1 != l5)
    assert(l2 != l3)
    assert(l2 != l4)

# Generated at 2022-06-14 03:21:44.019555
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    l = ImmutableList.of(2, 3, 4, 5, 6)
    l = l.filter(lambda v: v % 2 == 0)
    assert l == ImmutableList.of(2, 4, 6)
    assert len(l) == 3

test_ImmutableList_filter()

# Generated at 2022-06-14 03:21:46.557781
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3).find(lambda x: x > 1) == 2
    assert ImmutableList.of(1, 2, 3).find(lambda x: x > 3) is None

# Generated at 2022-06-14 03:21:58.444471
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    empty_list = ImmutableList.empty()
    assert empty_list == ImmutableList.empty()

    assert ImmutableList.empty() != ImmutableList.of(1)

    assert ImmutableList.of(1, 2) == ImmutableList.of(1, 2)
    assert ImmutableList.of(1, 2) != ImmutableList.of(3, 2)
    assert ImmutableList.of(1, 2) != ImmutableList.of(1, 3)
    assert ImmutableList.of(1, 2, 3) != ImmutableList.of(1, 2)
    assert ImmutableList.of(1, 2, 3) != ImmutableList.of(1, 2, 4)


# Generated at 2022-06-14 03:22:03.247491
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.empty().filter(lambda x: x == 1) == ImmutableList.empty()
    
    list_ = ImmutableList.of(1).filter(lambda x: x == 1)
    assert list_ == ImmutableList.of(1)

    list_ = ImmutableList.of(1, 2, 3).filter(lambda x: x == 1)
    assert list_ == ImmutableList.of(1)

    list_ = ImmutableList.of(1, 1, 2, 3).filter(lambda x: x % 2 == 0)
    assert list_ == ImmutableList.of(2)
    
    list_ = ImmutableList.of(1, 1, 2, 3).filter(lambda x: x % 2 == 1)
    assert list_ == ImmutableList.of(1, 1, 3)
# Unit

# Generated at 2022-06-14 03:22:15.876907
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x > 3) == 4
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4)))).find(lambda x: x > 3) == 4
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x < 3) == 1
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x == 5) is None
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: isinstance(x, int)) == 1
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: isinstance(x, str)) is None

# Generated at 2022-06-14 03:22:43.036675
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list_of_numbers = ImmutableList.of(1, 2, 3, 4, 5)
    even_numbers = list_of_numbers.filter(lambda x: x % 2 == 0)
    assert even_numbers.to_list() == [2, 4]


# Generated at 2022-06-14 03:22:47.092679
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # Given
    initial_value = ImmutableList(1, ImmutableList(2, ImmutableList(3)))

    # When
    result = initial_value.find(lambda x: x == 2)

    # Then
    assert result == 2

# Generated at 2022-06-14 03:22:52.449990
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    list1 = ImmutableList.of(1)
    list2 = ImmutableList.of(3)
    list3 = ImmutableList.of(1)

    assert list1 == list3
    assert list1 != list2
    assert list2 != list1
    assert list2 != list3
    assert list2 != list1
    assert list3 != list1
    assert list3 != list2


# Generated at 2022-06-14 03:22:55.751540
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    l1 = ImmutableList()
    l2 = ImmutableList()
    assert l1 == l2

    l1 = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    l2 = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    assert l1 == l2


# Generated at 2022-06-14 03:23:05.234170
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.empty().find(lambda x: x > 3) == None
    assert ImmutableList.of(1, 2, 3).find(lambda x: x > 3) == None
    assert ImmutableList.of(1, 2, 3).find(lambda x: x > 1) == 2
    assert ImmutableList.of(1, 2, 3).find(lambda x: x > -1) == 1

# Generated at 2022-06-14 03:23:13.671274
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    empty_list = ImmutableList.empty()
    assert empty_list.filter(lambda x: True) == ImmutableList.empty()

    list_one_value_with_even_number = ImmutableList(2)
    assert list_one_value_with_even_number.filter(lambda x: x % 2 == 0) == ImmutableList(2)
    
    list_one_value_with_odd_number = ImmutableList(1)
    assert list_one_value_with_odd_number.filter(lambda x: x % 2 == 0) == ImmutableList.empty()

    list_few_values_with_even_numbers = ImmutableList(2, ImmutableList(4), ImmutableList(6))

# Generated at 2022-06-14 03:23:26.673736
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    sample_1 = ImmutableList.of(0, 1, 2, 3, 4)
    assert sample_1.filter(lambda x: x < 3).to_list() == [0, 1, 2]

    sample_2 = ImmutableList.of(5, 4, 3, 2, 1)
    assert sample_2.filter(lambda x: x > 3).to_list() == [5, 4]

    sample_3 = ImmutableList.of(5, 4, 3, 2, 1)
    assert sample_3.filter(lambda x: x < 5).to_list() == [4, 3, 2, 1]

    sample_4 = ImmutableList.of('a', 'b', 'ab', 'abc', 'abcd')
    assert sample_4.filter(lambda x: len(x) < 3).to_list()

# Generated at 2022-06-14 03:23:31.863615
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    a = ImmutableList()
    b = ImmutableList()
    c = ImmutableList(is_empty=True)
    d = ImmutableList(is_empty=True)

    assert (a == b)
    assert not (a == c)
    assert (c == d)
    assert (a == ImmutableList())
    assert not (a == 'test')
    assert not (a == ImmutableList(1))



# Generated at 2022-06-14 03:23:37.879039
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    l = ImmutableList.of(1, 2, 3, 4, 5)
    result = l.filter(lambda x: x % 2 == 0)
    assert result == ImmutableList.of(2, 4)


# Generated at 2022-06-14 03:23:46.447849
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    def call(head, tail, expected):
        result = ImmutableList(head, tail) == ImmutableList(head, tail)
        if result != expected:
            raise AssertionError(
                'ImmutableList(head, tail) == ImmutableList(head, tail) '
                'returned unexpected result. '
                f'expected: {expected}, result: {result}'
            )

    call([], None, True)
    call([], [], False)
    call([], ['a'], False)
    call(['a'], ['b'], False)
    call(['a'], ['a'], True)
    call(['a'], [], False)
    call(['a'], None, False)
    call([], ['b', 'c'], False)

# Generated at 2022-06-14 03:24:24.861959
# Unit test for method filter of class ImmutableList

# Generated at 2022-06-14 03:24:31.130817
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # Method filter
    # test for empty list
    assert ImmutableList.empty().filter(lambda x: False) == ImmutableList.empty()
    assert ImmutableList.empty().filter(lambda x: True) == ImmutableList.empty()

    # test for one element list
    assert ImmutableList(1).filter(lambda x: False) == ImmutableList.empty()
    assert ImmutableList(1).filter(lambda x: True) == ImmutableList(1)

    # test for many element list
    assert ImmutableList(0, 1, 2, 3, 4).filter(lambda x: x % 2 == 0) == ImmutableList(0, 2, 4)



# Generated at 2022-06-14 03:24:36.906045
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.empty().filter(lambda x: x) == ImmutableList.empty()
    assert ImmutableList(1, None).filter(lambda x: x) == ImmutableList(1, None)
    assert ImmutableList(2, ImmutableList(1, None)).filter(lambda x: x == 2) == ImmutableList(2, None)
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3, None))).filter(lambda x: x % 2 == 0) == ImmutableList(2, None)


# Generated at 2022-06-14 03:24:42.592692
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 2) == 2
    assert ImmutableList.of(1, 3, 3).find(lambda x: x == 2) is None
    assert ImmutableList.of(1, 3, 3).find(lambda x: True) == 1


# Generated at 2022-06-14 03:24:53.435891
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.empty().find(lambda x: True) is None
    assert ImmutableList.empty().find(lambda x: False) is None
    assert ImmutableList(5).find(lambda x: True) == 5
    assert ImmutableList(5).find(lambda x: False) is None
    assert ImmutableList(5, ImmutableList(10)).find(lambda x: True) == 5
    assert ImmutableList(5, ImmutableList(10)).find(lambda x: False) is None
    assert ImmutableList(5, ImmutableList(10)).find(lambda x: x == 10) == 10
    assert ImmutableList(5, ImmutableList(10)).find(lambda x: x == 15) is None

test_ImmutableList_find()

# Generated at 2022-06-14 03:24:57.833996
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.empty().find(lambda x: x % 2 == 0) == None
    assert ImmutableList.of(4, 2, 3).find(lambda x: x % 2 == 0) == 4
    assert ImmutableList.of(4, 2, 3).find(lambda x: x % 2 == 1) == 2


# Generated at 2022-06-14 03:25:02.865913
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 2) == 2
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 0) is None

# Generated at 2022-06-14 03:25:06.337219
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    l = ImmutableList.of(1, 2, 3, 4, 5, 6)
    assert l.filter(lambda x: x % 3 == 0).to_list() == [3, 6]
    assert l.filter(lambda x: x % 7 == 0).to_list() == []



# Generated at 2022-06-14 03:25:11.885309
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))).find(lambda x: x == 2) == 2
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))).find(lambda x: x == 5) is None
    assert ImmutableList(1, ImmutableList(True)).find(lambda x: x == True) == True
    assert ImmutableList(1, ImmutableList(True)).find(lambda x: x == 5) is None

test_ImmutableList_find()


# Generated at 2022-06-14 03:25:20.582495
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    int_list = ImmutableList.of(1, 2, 3, 4)
    filtered_list = int_list.filter(lambda x: x > 2)

    assert filtered_list == ImmutableList.of(3, 4)

    string_list = ImmutableList.of('1', '2', '3', '4')
    filtered_string_list = string_list.filter(lambda x: x > '2')

    assert filtered_string_list == ImmutableList.of('3', '4')


# Generated at 2022-06-14 03:26:00.821776
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList[int].of(1, 2, 3).find(lambda x: x == 2) == 2
    assert ImmutableList[int].of(1, 2, 3).find(lambda x: x == 4) is None
    assert ImmutableList[int].empty().find(lambda x: 1 == 1) is None
    assert ImmutableList[int].of(1).find(lambda x: x == 4) is None
    assert ImmutableList[int].of(1).find(lambda x: x == 1) == 1


# Generated at 2022-06-14 03:26:03.975870
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(4, 3).find(lambda x: x > 2) == 4
    assert ImmutableList.of(4, 3).find(lambda x: x > 4) == None

    assert ImmutableList.empty().find(lambda x: x > 4) == None



# Generated at 2022-06-14 03:26:15.825498
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.empty().find(lambda x: x == 3) is None
    assert ImmutableList(1).find(lambda x: x == 3) is None
    assert ImmutableList(1).find(lambda x: x == 1) == 1
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))).find(lambda x: x == 3) == 3
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))).find(lambda x: x == 2) == 2
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))).find(lambda x: x == 1) == 1
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))).find(lambda x: x == 4) is None


# Generated at 2022-06-14 03:26:18.674262
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    list = ImmutableList.of(1, 2, 3, 4)
    assert list.find(lambda x: x > 3) == 4
    assert list.find(lambda x: x <= 0) is None



# Generated at 2022-06-14 03:26:23.523415
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.empty().find(lambda x: x == 3) is None
    assert ImmutableList.of(1,2,3,4,5).find(lambda x: x == 3) == 3
    assert ImmutableList.of(1,2,3,4,5).find(lambda x: x == 5) == 5
    assert ImmutableList.of(1,2,3,4,5).find(lambda x: x == 7) is None

# Generated at 2022-06-14 03:26:35.079745
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.empty().find(lambda item: item == 1) is None
    assert ImmutableList.of(1).find(lambda item: item == 1) == 1
    assert ImmutableList.of(0).find(lambda item: item == 1) is None
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda item: item == 0) is None
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda item: item == 1) == 1
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda item: item == 10) is None
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda item: item == 4) == 4

# Generated at 2022-06-14 03:26:37.165589
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # given
    list_ = ImmutableList.of(1, 2, 3)

    # when
    result = list_.find(lambda x: x > 1)

    # then
    assert result == 2


# Generated at 2022-06-14 03:26:40.770520
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 2) == 2
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 5) is None