

# Generated at 2022-06-14 03:17:00.626041
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    # Arrange
    base_list = ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4))))
    
    # Act
    actual_result_1 = ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4))))
    actual_result_2 = ImmutableList(10, ImmutableList(20, ImmutableList(30, ImmutableList(40))))
    actual_result_3 = ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4, ImmutableList(5)))))
    actual_result_4 = ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4, ImmutableList(5)))))

# Generated at 2022-06-14 03:17:08.718022
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    import pytest
    cases = (
        (ImmutableList.of(1, 2, 3, 4, 5), 2, 2),
        (ImmutableList.of(1, 2, 3, 4, 5), 6, None),
        (ImmutableList.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 0), 6, 6),
        (ImmutableList.of(1), 1, 1),
        (ImmutableList.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 0), 0, 0),
    )

    for case in cases:
        result = case[0].find(lambda element: element == case[1])
        

# Generated at 2022-06-14 03:17:13.873105
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # Test 1
    # Case: we have empty list, expect None
    result = ImmutableList.empty().find(lambda x: True)
    assert result == None, "find on empty ImmutableList shoud return None"

    # Test 2
    # Case: we have list with one element and predicate always returns True,
    #       expect list element
    result = ImmutableList.of(5).find(lambda x: True)
    assert result == 5, "find on ImmutableList shoud return first element of list"

    # Test 3
    # Case: we have list with one element and predicate always returns False,
    #       expect None
    result = ImmutableList.of(5).find(lambda x: False)
    assert result == None, "find on ImmutableList shoud return first element of list"

    # Test 4
    # Case:

# Generated at 2022-06-14 03:17:19.759724
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList(1) == ImmutableList(1)
    assert ImmutableList(1, ImmutableList(1)) == ImmutableList(1, ImmutableList(1))


# Generated at 2022-06-14 03:17:27.127566
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list_1 = ImmutableList.of(1, 2, 3, 4)
    list_2 = ImmutableList.of('1', '2', '3', '4')

    assert list_1.filter(lambda x: x > 2) == ImmutableList.of(3, 4)
    assert list_1.filter(lambda x: x > 4) == ImmutableList.empty()
    assert list_1.filter(lambda x: x < 0) == ImmutableList.empty()
    assert list_1.filter(lambda x: x == 1) == ImmutableList.of(1)
    assert list_1.filter(lambda x: x == 5) == ImmutableList.empty()
    assert list_2.filter(lambda x: x > '2') == ImmutableList.of('3', '4')

# Generated at 2022-06-14 03:17:36.825498
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1).filter(lambda x: x == 1) == ImmutableList.of(1)
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x > 1) == ImmutableList.of(2, 3)
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x > 3) == ImmutableList.empty()
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x > 2).filter(lambda x: x > 1) == ImmutableList.of(3)
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x > 3).filter(lambda x: x > 2) == ImmutableList.empty()


# Generated at 2022-06-14 03:17:51.948611
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.of(1, 2, 3, 4, 5) == ImmutableList.of(1, 2, 3, 4, 5)
    assert ImmutableList.of(1, 2, 3, 4) != ImmutableList.of(1, 2, 3, 4, 5)
    assert ImmutableList.of(1, 2, 3, 4, 5) != ImmutableList.of(1, 2, 3, 4)
    assert ImmutableList.of(1, 2, 5) != ImmutableList.of(1, 2, 3)
    assert ImmutableList.of(1, 2, 3) != ImmutableList.of(1, 2, 5)
    assert ImmutableList.of(1, 5) != ImmutableList.of(1, 2)
    assert ImmutableList.of(1, 2) != Immutable

# Generated at 2022-06-14 03:17:57.759169
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.of(1, 2, 3) == ImmutableList.of(1, 2, 3)
    assert ImmutableList.empty() == ImmutableList.empty()
    assert ImmutableList.of(1) == ImmutableList.of(1)


# Generated at 2022-06-14 03:18:09.986317
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    # Rule 1: Empty list equals empty list
    empty_list = ImmutableList.empty()
    empty_list_2 = ImmutableList.empty()
    assert empty_list == empty_list_2, \
        "Rule 1: Empty list equals empty list"

    # Rule 2: List with single element equals list with single element
    single_list = ImmutableList.of('one')
    single_list_2 = ImmutableList.of('one')
    assert single_list == single_list_2, \
        "Rule 2: List with single element equals list with single element"

    # Rule 3: List with multiple elements equals list with multiple elements
    multiple_list_1 = ImmutableList.of('one', 'two', 'three')
    multiple_list_2 = ImmutableList.of('one', 'two', 'three')

# Generated at 2022-06-14 03:18:18.055213
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))).filter(
        lambda a: True) == ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))).filter(
        lambda a: False).is_empty == True
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))).filter(
        lambda a: a % 2 == 0) == ImmutableList(2)



# Generated at 2022-06-14 03:18:33.060315
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))) == ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))) != ImmutableList(1, ImmutableList(2))
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))) != ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(3))))
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))) == ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(is_empty=True))))


# Generated at 2022-06-14 03:18:53.109492
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    """Test for method ImmutableList.__eq__ ."""
    assert ImmutableList.empty() == ImmutableList.empty()
    assert ImmutableList.of(1) == ImmutableList.of(1)
    assert ImmutableList.of(1, 2, 3) == ImmutableList.of(1, 2, 3)
    assert ImmutableList.of(1, 2, 3) == ImmutableList.of(1, 2, 3) and ImmutableList.of(1, 2, 3) == ImmutableList.of(1, 2, 3)
    assert ImmutableList.of(1, 2, 2) != ImmutableList.of(1, 2, 3)
    assert ImmutableList.of(1, 2, 3) != ImmutableList.of(1, 2)
    assert ImmutableList.of(1, 2)

# Generated at 2022-06-14 03:18:59.284261
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda x: x > 3) \
     == ImmutableList.of(4)
    assert ImmutableList().filter(lambda x: x > 3) \
     == ImmutableList.empty()
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(lambda x: x > 3) \
     == ImmutableList.of(4, 5)
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(lambda x: x == 1) \
     == ImmutableList.of(1)

# Generated at 2022-06-14 03:19:06.993046
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # Test1
    assert ImmutableList(0, ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4))))) \
        .find(lambda x: x == 4) == 4

    # Test2
    assert ImmutableList(0, ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4))))) \
        .find(lambda x: x == 1) == 1

    # Test3
    assert ImmutableList.empty().find(lambda x: x == 1) is None

# Generated at 2022-06-14 03:19:13.055596
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    """
    Function for testing filter method of ImmutableList
    """
    immutable_list = ImmutableList.of(1, 2, 3, 4, 5)
    assert immutable_list.filter(lambda x: x % 2 == 0) == ImmutableList.of(2, 4)
    with pytest.raises(ValueError):
        immutable_list.filter(lambda x: x % 2 == 0) == 1


# Generated at 2022-06-14 03:19:20.277095
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    # Given
    list_1 = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    list_2 = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    list_3 = ImmutableList(1, ImmutableList(3))


    # When
    result_equal_1 = list_1 == list_2
    result_equal_2 = list_1 == list_1
    result_not_equal = list_1 == list_3

    # Then
    assert result_equal_1 == True
    assert result_equal_2 == True
    assert result_not_equal == False

# Generated at 2022-06-14 03:19:23.935794
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.empty().find(lambda x: x > 1) is None

    assert ImmutableList(1).find(lambda x: x > 1) == 1

    assert ImmutableList(2, ImmutableList(1)).find(lambda x: x > 1) == 2

    assert ImmutableList(1, ImmutableList(2)).find(lambda x: x > 1) == 2



# Generated at 2022-06-14 03:19:26.898158
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    # Given
    list_ = ImmutableList.of(1, 2, 3)
    other = ImmutableList.of(1, 2, 3)

    # When
    actual = list_ == other

    # Then
    assert actual == True

# Generated at 2022-06-14 03:19:32.809561
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda i: i > 0) == 1
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda i: i > 3) == 4
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda i: i > 10) is None


# Generated at 2022-06-14 03:19:37.324861
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    immutable_list = ImmutableList.of(1,1,1,1)
    assert immutable_list.find(lambda x: x % 2 == 0) == None



# Generated at 2022-06-14 03:19:46.868950
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x > 2) == 3
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x > 5) == None


# Generated at 2022-06-14 03:19:51.007536
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    arr = ImmutableList([
        'Hello',
        'World',
        'Hello',
        'Python'
    ])

    filtered = arr.filter(lambda word: word == 'Hello')
    assert len(filtered) == 2
    assert filtered.to_list() == ['Hello', 'Hello']



# Generated at 2022-06-14 03:20:01.451481
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # Arrange
    # tl = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    tl = ImmutableList.of(1, 2, 3)

    # Act & Assert
    assert tl.find(lambda x: x == 1) is 1
    assert tl.find(lambda x: x == 2) is 2
    assert tl.find(lambda x: x == 3) is 3
    assert tl.find(lambda x: x == 4) is None



# Generated at 2022-06-14 03:20:08.776682
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    FunctionType = Callable[[Optional[int]], bool]
    # arguments
    int_list = ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4, ImmutableList(5)))))

    # expected results
    res_even = ImmutableList(2, ImmutableList(4))
    res_odd = ImmutableList(1, ImmutableList(3, ImmutableList(5)))

    # test even filter
    res = int_list.filter(lambda x: x % 2 == 0)
    assert res == res_even

    # test odd filter
    res = int_list.filter(lambda x: x % 2 == 1)
    assert res == res_odd


# Generated at 2022-06-14 03:20:19.090552
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    list_one = ImmutableList(is_empty=True)
    assert list_one.find(lambda x: True) is None

    list_two = ImmutableList.of(1, 2, 3, 4, 5)
    assert list_two.find(lambda x: x == 3) == 3

    list_three = ImmutableList.of(1, 2, 3, 4, 5, 3, 3)
    assert list_three.find(lambda x: x == 3) == 3

# Generated at 2022-06-14 03:20:25.574484
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    val = [1, 2, 3]
    list_ = ImmutableList.of(1, 2, 3, 4)
    assert list_.find(lambda x: x == 3) == 3

    assert ImmutableList.of(1).find(lambda x: True) == 1
    assert ImmutableList.empty().find(lambda x: True) == None



# Generated at 2022-06-14 03:20:32.766309
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert None is ImmutableList().find(lambda x: x > 2)
    assert 0 is ImmutableList(0).find(lambda x: x > 2)
    assert 3 is ImmutableList(0, 1, 2, 3).find(lambda x: x > 2)

# Generated at 2022-06-14 03:20:37.794355
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    test_list = ImmutableList.of(1, 4, 10, 4, 8)
    find_by_value = test_list.find(lambda x: x == 4)
    find_by_index = test_list.find(lambda x: x > 100)

    assert_equal(find_by_value, 4)
    assert_equal(find_by_index, None)

if __name__ == '__main__':
    test_ImmutableList_find()
    print('All tests for ImmutableList is OK!')


# Generated at 2022-06-14 03:20:45.762202
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list_of_test = ImmutableList.of(1,3,5,7,11,13)
    list_of_expected_elements = ImmutableList.of(3,5,7,11)

    result = list_of_test.filter(lambda x: x % 2 == 1)

    assert result == list_of_expected_elements
    assert list_of_test == ImmutableList.of(1,3,5,7,11,13)


# Generated at 2022-06-14 03:20:51.178473
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    list_ = ImmutableList.of(1, 2, 3, 4).filter(lambda x: x % 2 == 0)
    assert list_.find(lambda x: x == 2) == 2
    assert list_.find(lambda x: x == 3) is None



# Generated at 2022-06-14 03:21:11.148733
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # Given
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda x: x % 2 == 0) == ImmutableList.of(2, 4),\
        'should return ImmutableList.of(2, 4)'
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda x: x < 0) == ImmutableList.empty(),\
        'should return ImmutableList.empty()'


# Generated at 2022-06-14 03:21:15.431999
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list_of_integer = ImmutableList.of(4, True, "something", 6, False, -1, 0, False)
    filtered_list = list_of_integer.filter(lambda x: isinstance(x, int))
    assert len(filtered_list) == len(list_of_integer) - 3



# Generated at 2022-06-14 03:21:18.308377
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x > 3) == 4
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x > 10) is None



# Generated at 2022-06-14 03:21:22.152236
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
  assert ImmutableList.of(1, 2, 3).filter(lambda x: x == 2) == ImmutableList.of(2)
  assert ImmutableList.of(1, 2, 3).filter(lambda x: x == 4) == ImmutableList.empty()
  assert ImmutableList.of(1, 2, 3).filter(lambda x: x == 5) == ImmutableList.empty()
  assert ImmutableList.of(1, 2, 3).filter(lambda x: x > 2) == ImmutableList.of(3)
  
test_ImmutableList_filter()

# Generated at 2022-06-14 03:21:29.561776
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    lst = ImmutableList.of(1, 2, 3, 4, 5, 6)
    assert lst.filter(lambda x: x % 2 == 0) == ImmutableList.of(2, 4, 6)
    assert lst.filter(lambda x: x == 10) == ImmutableList.empty()
    assert lst.filter(lambda x: True) == lst
    assert lst.filter(lambda x: False) == ImmutableList.empty()


# Generated at 2022-06-14 03:21:36.786145
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    iml1 = ImmutableList.of(1, 2, 3)
    iml2 = ImmutableList.of(1, 2, 3)
    iml3 = ImmutableList.of(4, 5, 6)

    assert iml1.filter(lambda x: x > 2).to_list() == [3]
    assert iml2.filter(lambda x: x > 2).to_list() == [3]
    assert iml3.filter(lambda x: x > 2).to_list() == [4, 5, 6]


test_ImmutableList_filter()


# Generated at 2022-06-14 03:21:55.457770
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    empty_list = ImmutableList.empty()
    assert empty_list.filter(lambda x: True) == empty_list

    not_empty_list = ImmutableList.of(1, 2, 3)
    assert not_empty_list.filter(lambda x: x > 0) == not_empty_list
    assert not_empty_list.filter(lambda x: x > 1) == ImmutableList(2, ImmutableList(3))
    assert not_empty_list.filter(lambda x: x > 2) == ImmutableList(3)
    assert not_empty_list.filter(lambda x: x > 3) == ImmutableList(is_empty=True)

# Generated at 2022-06-14 03:22:15.852140
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    empty_list = ImmutableList.empty()
    assert empty_list.filter(lambda x: x > 5) == ImmutableList.empty()

    list_with_one_element = ImmutableList.of(5)
    assert list_with_one_element.filter(lambda x: x > 5) == ImmutableList.empty()
    assert list_with_one_element.filter(lambda x: x > 3) == ImmutableList.of(5)

    list_with_two_elements = ImmutableList.of(1, 2)
    assert list_with_two_elements.filter(lambda x: x > 5) == ImmutableList.empty()
    assert list_with_two_elements.filter(lambda x: x > 1) == ImmutableList.of(2)

    list_with_three_elements = Imm

# Generated at 2022-06-14 03:22:22.931147
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    list = ImmutableList.of(1, 2, 5, 6)
    assert list.find(lambda x: x > 4) == 5

    list = ImmutableList.of(1, 2, 5, 6)
    assert list.find(lambda x: x > 6) is None

    list = ImmutableList.of(1, 2, 5, 6)
    assert list.find(lambda x: x > 0) == 1

# Generated at 2022-06-14 03:22:31.126814
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # Given
    alist = ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4, ImmutableList(5, ImmutableList(6))))))
    # When
    result = alist.filter(lambda x: x > 3)
    # Then
    assert result == ImmutableList(4, ImmutableList(5, ImmutableList(6)))


# Generated at 2022-06-14 03:23:02.222740
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # Given
    l = ImmutableList.of(1, 2, 3, 4, 5)

    # When
    new_l = l.filter(lambda x: x % 2 == 0)

    # Then
    assert new_l == ImmutableList.of(2, 4)



# Generated at 2022-06-14 03:23:07.763736
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 1) == 1
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 3) == 3
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 7) is None



# Generated at 2022-06-14 03:23:10.523702
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list_ = ImmutableList.of(1, 2, 3).filter(lambda x: x % 2 == 0)
    assert list_.to_list() == [2]


# Generated at 2022-06-14 03:23:16.242621
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x == 2) == 2
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x % 2 == 0) == 2
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x == 5) == None
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x % 2 == 0) == 2
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x % 2 == 1) == 1
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x % 2 == 0) == 2

# Generated at 2022-06-14 03:23:25.849037
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    odds = ImmutableList.of(1, 3, 5, 7)
    evens = ImmutableList.of(0, 2, 4, 6)

    assert odds.filter(lambda x: x % 2 != 0).to_list() == odds.to_list()
    assert evens.filter(lambda x: x % 2 != 0).to_list() == []
    assert odds.filter(lambda x: x % 2 == 0).to_list() == []
    assert evens.filter(lambda x: x % 2 == 0).to_list() == evens.to_list()


# Generated at 2022-06-14 03:23:28.375942
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda x: x % 2 == 0) == ImmutableList.of(2, 4)
    assert ImmutableList.empty().filter(lambda x: x % 2 == 0) == ImmutableList.empty()
    assert ImmutableList.of(3, 4, 5, 6).filter(lambda x: x % 2 == 0) == ImmutableList.of(4, 6)



# Generated at 2022-06-14 03:23:31.390983
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # data = ImmutableList([1, 2, 3])
    # expected_result = ImmutableList([1, 2, 3])
    # assert data.filter(lambda x: x != 4) == expected_result
    assert 0


# Generated at 2022-06-14 03:23:42.866529
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.empty().find(lambda x: x == 0) is None

    assert ImmutableList.of(1).find(lambda x: x == 0) is None
    assert ImmutableList.of(0).find(lambda x: x == 0) == 0

    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 0) is None
    assert ImmutableList.of(1, 2, 3, 0, 5).find(lambda x: x == 0) == 0


# Generated at 2022-06-14 03:23:58.777898
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of('one', 'two', 'three', 'four', 'five').filter(lambda i: i.startswith('t')) == ImmutableList.of('two', 'three', 'two', 'three', 'two', 'three')
    assert ImmutableList.of('one', 'two', 'three', 'four', 'five').filter(lambda i: False) == ImmutableList.of()


# Generated at 2022-06-14 03:24:05.122148
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # Imports
    from random import randint
    # Generate ImmutableList with random numbers
    immutable_list = [randint(0, 10) for x in range(0,10)]
    # Create ImmutableList instance from generated numbers
    immutable_list = ImmutableList.of(*immutable_list)
    # Get only digits that are lass than five
    filtered = immutable_list.filter(lambda x: x < 5)
    # Check if the output is correct
    assert len(filtered) == len([x for x in immutable_list.to_list() if x < 5])
    # Show result
    print(filtered)


test_ImmutableList_filter()


# Generated at 2022-06-14 03:24:38.476553
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2).filter(lambda element: element < 2) == ImmutableList.of(1)
    assert ImmutableList.of(1, 2).filter(lambda element: element == 2) == ImmutableList.of(2)
    assert ImmutableList.of(1, 2).filter(lambda element: element > 1) == ImmutableList.of(2)
    assert ImmutableList.of(1, 2).filter(lambda element: element >= 2) == ImmutableList.of(2)
    assert ImmutableList.of(1, 2).filter(lambda element: element <= 2) == ImmutableList.of(1, 2)
    assert ImmutableList.of(1, 2).filter(lambda element: element > 2) == ImmutableList()


# Generated at 2022-06-14 03:24:44.776860
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))).filter(lambda x: x > 1) == ImmutableList(2, ImmutableList(3))
    assert ImmutableList().filter(lambda x: x > 1) == ImmutableList(is_empty=True)
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))).filter(lambda x: x > 3) == ImmutableList(is_empty=True)


# Generated at 2022-06-14 03:24:47.787418
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda x: x > 2) == ImmutableList.of(3, 4)
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda x: False) == ImmutableList.empty()
    assert ImmutableList.empty().filter(lambda x: False) == ImmutableList.empty()
    

# Generated at 2022-06-14 03:24:52.065200
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(2, 3, 4).filter(lambda x: x / 2 == 1) == ImmutableList.of(2)
    assert ImmutableList.empty().filter(lambda x: x / 2 == 1) == ImmutableList.empty()


# Generated at 2022-06-14 03:24:56.755919
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x % 2) == ImmutableList.of(1, 3)
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x == 1) == ImmutableList.of(1)
    # Unit test for method map of class ImmutableList

# Generated at 2022-06-14 03:25:00.255253
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 4)\
        .find(lambda v: v == 5) == None
    
    assert ImmutableList.of(1, 2, 3, 4)\
        .find(lambda v: v == 3) == 3

test_ImmutableList_find()

# Generated at 2022-06-14 03:25:04.623702
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4)))).filter(lambda x: x%2 == 0) == ImmutableList(2, ImmutableList(4))
    
    

# Generated at 2022-06-14 03:25:05.404651
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3).find(lambda x: x > 2) == 3

# Generated at 2022-06-14 03:25:08.519905
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list_one = ImmutableList.of(2, 3, 4, 5)
    list_two = list_one.filter(lambda x: x % 2 != 0)
    assert list_two.to_list() == [3, 5]
    assert list_two == ImmutableList.of(3, 5)
    assert list_one == ImmutableList.of(2, 3, 4, 5)

# Generated at 2022-06-14 03:25:12.854074
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    l = ImmutableList.of(1, 2, 3, 4, 5).find(lambda n: n > 3)
    result = 4
    assert l == result


# Generated at 2022-06-14 03:26:14.167351
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(0, 1, 2, 3, 4, 5).filter(lambda x: x > 3) == ImmutableList.of(4, 5)


# Generated at 2022-06-14 03:26:33.938654
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    il_from_empty = ImmutableList.empty()
    il_from_empty_filtered = il_from_empty.filter(lambda i: i == 7)
    assert il_from_empty_filtered == ImmutableList.empty()
    assert il_from_empty.filter(lambda i: i == '0') == ImmutableList.empty()

    il_from_list = ImmutableList.of(3, 5, 7, 9, 11)
    il_from_list_filtered = il_from_list.filter(lambda i: i % 3 == 0)
    assert il_from_list_filtered == ImmutableList.of(3, 9)

    il_from_list_filtered_2 = il_from_list.filter(lambda i: i == 11)

# Generated at 2022-06-14 03:26:42.363424
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.empty().filter(lambda x: x > 2) == ImmutableList.empty()

    assert ImmutableList.of(1).filter(lambda x: x > 2) == ImmutableList.empty()
    assert ImmutableList.of(3).filter(lambda x: x > 2) == ImmutableList.of(3)
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x > 2) == ImmutableList.of(3)
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda x: x > 2) == ImmutableList(3, ImmutableList(4))
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(lambda x: x > 2) == ImmutableList(3, ImmutableList(4, ImmutableList(5)))

# Generated at 2022-06-14 03:26:45.647179
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    l = ImmutableList.of(1, 2, 3, 4)
    assert l.find(lambda x: x > 3) == 4

