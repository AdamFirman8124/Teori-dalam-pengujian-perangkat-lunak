

# Generated at 2022-06-14 03:16:50.893536
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    test_data = ImmutableList.empty()
    test_data = test_data.append(1)
    test_data = test_data.append(2)
    test_data = test_data.append(3)
    test_data = test_data.append(4)
    test_data = test_data.append(3)
    test_data = test_data.append(2)
    test_data = test_data.append(1)
    expected = ImmutableList.empty()
    expected = expected.append(3)
    expected = expected.append(3)
    assert test_data.filter(lambda x: x == 3) == expected

# Generated at 2022-06-14 03:16:57.932314
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 2) == 2
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 5) is None
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 3) == 3
    assert ImmutableList.of(1).find(lambda x: x == 1) == 1
    assert ImmutableList.of().find(lambda x: x == 1) is None



# Generated at 2022-06-14 03:17:03.320842
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    _list = ImmutableList.of(1, 2, 3, 4, 5)
    assert _list.filter(lambda x: x % 2 == 0) == ImmutableList.of(2, 4)
    assert _list.filter(lambda x: x > 2) == ImmutableList.of(3, 4, 5)

    # Test empty ImmutableList
    assert ImmutableList.empty().filter(lambda x: x > 2) == ImmutableList.empty()



# Generated at 2022-06-14 03:17:08.378404
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    immutable_list = ImmutableList.of(
        ImmutableList.of(1, 2),
        ImmutableList.of(3, 4)
    )

    assert immutable_list == immutable_list

    another_immutable_list = ImmutableList.empty().append(
        ImmutableList.of(1, 2)
    ).append(
        ImmutableList.of(3, 4)
    )

    assert immutable_list == another_immutable_list

    assert immutable_list != []


# Generated at 2022-06-14 03:17:16.053472
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    # arrange
    head = 1
    tail = ImmutableList(2, None)
    immutable_list = ImmutableList(head, tail)

    # act
    result = immutable_list.__eq__(immutable_list)

    # assert
    assert result is True

test_ImmutableList___eq__()


# Generated at 2022-06-14 03:17:23.942683
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    list_1 = ImmutableList(1, ImmutableList(2))
    list_2 = ImmutableList(1, ImmutableList(2))
    assert list_1 == list_2

    list_1 = ImmutableList(1, ImmutableList(2))
    list_2 = ImmutableList(1, ImmutableList(3))
    assert list_1 != list_2

    list_1 = ImmutableList(1, ImmutableList(2))
    list_2 = ImmutableList(1)
    assert list_1 != list_2


# Generated at 2022-06-14 03:17:32.650346
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    sample_list = ImmutableList.of(1, 2, 3)

    assert sample_list.filter(lambda x: x % 2 == 0) == ImmutableList.of(2)
    assert sample_list.filter(lambda x: x == 1) == ImmutableList.of(1)
    assert sample_list.filter(lambda x: x == 4) == ImmutableList.empty()



# Generated at 2022-06-14 03:17:41.121157
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList(1, ImmutableList(2), is_empty=False) == ImmutableList(1, ImmutableList(2), is_empty=False)
    assert ImmutableList(1, ImmutableList(2), is_empty=False) != ImmutableList(1, ImmutableList(2), is_empty=True)
    assert ImmutableList(1, ImmutableList(2), is_empty=False) != ImmutableList(1, ImmutableList(3), is_empty=False)
    assert ImmutableList(1, ImmutableList(2), is_empty=False) != ImmutableList(2, ImmutableList(2), is_empty=False)

# Generated at 2022-06-14 03:17:51.095123
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    """
    Test case for method __eq__ of class ImmutableList
    """

    assert ImmutableList().__eq__(ImmutableList())
    assert ImmutableList().__eq__(ImmutableList(is_empty=True))
    assert ImmutableList(is_empty=True).__eq__(ImmutableList())

    assert ImmutableList(1).__eq__(ImmutableList(1))
    assert ImmutableList(1).__eq__(ImmutableList(1, ImmutableList()))
    assert ImmutableList(1).__eq__(ImmutableList(1, ImmutableList(is_empty=True)))

    assert not ImmutableList(1).__eq__(ImmutableList(2))
    assert not ImmutableList(1).__eq__(ImmutableList(2, ImmutableList()))
    assert not Immutable

# Generated at 2022-06-14 03:17:57.285016
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    """
    Test case verifies if instances of ImmutableList are equal,
    than method __eq__ returns True, otherwise returns False
    """
    instance_one = ImmutableList.of(1)
    instance_two = ImmutableList.of(1)
    assert instance_one == instance_two

    instance_one = ImmutableList.of(1)
    instance_two = ImmutableList.of(2)
    assert instance_one != instance_two

    instance_one = ImmutableList.of(1, 2, 3)
    instance_two = ImmutableList.of(1, 2, 3)
    assert instance_one == instance_two

    instance_one = ImmutableList.of(1, 2, 3)
    instance_two = ImmutableList.of(1, 2)
    assert instance_one != instance_two

# Generated at 2022-06-14 03:18:06.879083
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x == 3) == 3
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x < 5) == 1
    assert ImmutableList.of(1, 3, 4).find(lambda x: x > 5) == None

# Generated at 2022-06-14 03:18:11.906345
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # Arrange
    list_ = ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4, ImmutableList(5)))))
    # Act
    result = list_.find(lambda a: a > 3)
    # Assert
    assert result == 4


# Generated at 2022-06-14 03:18:15.572933
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    list_1 = ImmutableList.of(1, 2, 3)
    assert list_1.find(lambda x: x == 2) == 2
    assert list_1.find(lambda x: x == 10) is None
    assert ImmutableList.empty().find(lambda x: x == 10) is None

# Generated at 2022-06-14 03:18:21.691403
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4, 5, 6, 7, 8).filter(lambda x: x % 3 == 0).to_list() == [3, 6]
    assert ImmutableList.of(1, 2, 3, 4, 5, 6, 7, 8).filter(lambda x: x % 3 == 0).to_list() != [4, 6]
    assert ImmutableList.of(1, 2, 3, 4, 5, 6, 7, 8).filter(lambda x: x > 10).to_list() == []
    assert ImmutableList.of(1, 2, 3, 4, 5, 6, 7, 8).filter(lambda x: x == 6).to_list() == [6]
    assert ImmutableList.of(1, 2, 3, 4, 5, 6, 7, 8).filter

# Generated at 2022-06-14 03:18:29.259353
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.empty().filter(lambda x: False == True) == ImmutableList.empty()
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda x: x < 3) == ImmutableList.of(1, 2)
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda x: x > 3) == ImmutableList.of(4)
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda x: x == 3) == ImmutableList.of(3)


# Generated at 2022-06-14 03:18:35.679114
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # Arrange
    list_1 = ImmutableList.of(1, 2, 3, 4, 5)
    # Act
    result = list_1.filter(lambda x: x > 3)
    # Assert
    assert result == ImmutableList.of(4, 5)
    assert result != ImmutableList.of(4)

# Generated at 2022-06-14 03:18:40.785619
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.empty().filter(lambda x: x) == ImmutableList.empty()
    assert ImmutableList.of('a', 'b', 'c', 'd', 'e', 'f').filter(lambda x: x in ['a', 'c', 'e']) == ImmutableList.of('a', 'c', 'e')
test_ImmutableList_filter()

# Generated at 2022-06-14 03:18:44.414619
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list1 = ImmutableList.of(1, 2, 3)
    list1 = list1.filter(lambda x: x > 1)

    list2 = ImmutableList.of(2, 3)

    assert list1 == list2


# Generated at 2022-06-14 03:18:52.470637
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    def test1():
        assert ImmutableList(1, ImmutableList(2, ImmutableList(3)), False).filter(lambda x: x > 1) == ImmutableList(2, ImmutableList(3))
        assert ImmutableList(1, ImmutableList(2, ImmutableList(3)), False).filter(lambda x: x < 1) == ImmutableList(-1, ImmutableList(-2, ImmutableList(-3)))
    def test2():
        assert ImmutableList.of(1, 2, 3).filter(lambda x: x > 1) == ImmutableList.of(2, 3)
        assert ImmutableList.of(1, 2, 3).filter(lambda x: x < 1) == ImmutableList.of(-1, -2, -3)

    test1()
    test2()


# Generated at 2022-06-14 03:18:59.462252
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList(0, ImmutableList(1, ImmutableList(2, ImmutableList(3))))\
    .filter(lambda x: x % 2 == 0)\
        == ImmutableList(0, ImmutableList(2))

    # Defined object shouldn't be changed after calling method filter
    list_test_obj = ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4, ImmutableList(5)))))
    list_test_obj.filter(lambda x: x % 2 == 0)

    assert list_test_obj == ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4, ImmutableList(5)))))



# Generated at 2022-06-14 03:19:16.190289
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    def greater_than_3(x):
        return x > 3

    assert ImmutableList.of(1, 2, 3, 4).filter(greater_than_3).to_list() == [4]
    assert ImmutableList.of(1, 2, 3).filter(greater_than_3).is_empty
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(greater_than_3).to_list() == [4, 5]
    assert ImmutableList.of(-3, -2, -1, 0, 1, 2, 3, 4, 5).filter(greater_than_3).to_list() == [4, 5]



# Generated at 2022-06-14 03:19:17.974787
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    actual = ImmutableList.of(1, 2, 3).find(lambda x: x % 2 == 0)

    assert 2 == actual



# Generated at 2022-06-14 03:19:22.017231
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    is_even = lambda x: x % 2 == 0

    assert ImmutableList.empty().filter(is_even) == ImmutableList.empty()

    # Test filter for non empty list
    assert ImmutableList.of(1, 2, 3, 4, 5, 6, 7, 8, 9) \
        .filter(is_even) == ImmutableList.of(2, 4, 6, 8)


# Generated at 2022-06-14 03:19:28.625456
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList(1).find(lambda x: x > 1) is None
    assert ImmutableList(1).find(lambda x: x == 1) == 1
    assert ImmutableList(1, ImmutableList(2)).find(lambda x: x == 2) == 2
    assert ImmutableList(5, ImmutableList(2)).find(lambda x: x == 2) == 2


# Generated at 2022-06-14 03:19:31.579343
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda x: x % 2 == 0) == ImmutableList.of(2, 4)

# Generated at 2022-06-14 03:19:39.530027
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3).find(lambda x: x > 2) == 3
    assert ImmutableList.of(1, 2, 3).find(lambda x: x > 3) is None
    assert ImmutableList.empty().find(lambda x: x > 3) is None

test_ImmutableList_find()


# Generated at 2022-06-14 03:19:49.731994
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    def even(number):
        return number % 2 == 0

    # Create ImmutableList with all even number
    even_list = ImmutableList.of(2, 4, 6)

    # Append one odd number
    even_list = even_list.append(7)
    # Append another odd number
    even_list = even_list.append(5)

    # Filter add append only even number
    even_list = even_list.filter(even)

    # Create another ImmutableList with all even number
    another_even_list = ImmutableList.of(2, 4, 6, 7, 5).filter(even)

    assert even_list == another_even_list



# Generated at 2022-06-14 03:19:56.945939
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    list_ = ImmutableList(1)

    result = list_.find(lambda x: x %2 == 0)

    assert result is None

    list_ = ImmutableList(1, ImmutableList(2))

    result = list_.find(lambda x: x %2 == 0)

    assert result == 2


# Generated at 2022-06-14 03:20:00.445250
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.empty().filter(lambda v: v % 2 == 0) == ImmutableList()

    assert ImmutableList.of(1, 2, 3, 4, 5, 6)\
        .filter(lambda v: v % 2 == 0) == ImmutableList.of(2, 4, 6)

# Generated at 2022-06-14 03:20:14.172913
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x > 2) == 3
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x < 0) is None
    

test_ImmutableList_find()

# Generated at 2022-06-14 03:20:31.958075
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(2, 3, 4, 5).filter(lambda x: x % 2 == 0) == ImmutableList.of(2, 4)
    assert ImmutableList.of(2, 3, 4, 7, 11, 8).filter(lambda x: x % 2 == 0) == ImmutableList.of(2, 4, 8)

# Generated at 2022-06-14 03:20:37.000947
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    list = ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x % 2 == 0)
    assert list == 2

    list = ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 9)
    assert list is None


# Generated at 2022-06-14 03:20:40.227633
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    test_list = ImmutableList.of(1, 2, 3, 4, 5)

    assert test_list.find(lambda x: x == 5) == 5
    assert test_list.find(lambda x: x == 0) is None
    assert test_list.find(lambda x: x == 1) == 1
    assert test_list.find(lambda x: x == 3) == 3


# Generated at 2022-06-14 03:20:44.695064
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # Given
    list_ = ImmutableList.of(True, False, True, True)

    # When
    filtered = list_.filter(lambda x: x)

    # Then
    assert filtered == ImmutableList.of(True, True, True)

# Generated at 2022-06-14 03:20:46.772372
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3).filter(lambda n: n > 2) == ImmutableList.of(3)



# Generated at 2022-06-14 03:20:52.969543
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list_ = ImmutableList.of(1, 2, 3, 4).filter(lambda x: x % 2 == 0)

    assert list_.head == 2
    assert list_.tail.head == 4
    assert list_.tail.tail.is_empty is True

test_ImmutableList_filter()

# Unit tests for method append of class ImmutableList

# Generated at 2022-06-14 03:20:57.699431
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    empty_list = ImmutableList.empty()
    assert empty_list.find(lambda x: True) == None

    lst = ImmutableList.of(1, 2, 3, 4, 5)
    assert lst.find(lambda x: x > 3) == 4
    assert lst.find(lambda x: x > 5) == None

# Generated at 2022-06-14 03:20:58.992906
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # WHEN
    result = ImmutableList.of(3).find(lambda x: x == 3)
    # THEN
    assert result == 3

# Generated at 2022-06-14 03:21:03.294108
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # Given
    list = ImmutableList.of(10, 20, 30, 40, 50, 60)

    # When
    filtered_list = list.filter(lambda elem: elem % 2 == 0)

    # Then
    assert filtered_list == ImmutableList.of(10, 30, 50)


# Generated at 2022-06-14 03:21:09.569448
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda x: x % 2 == 1) == ImmutableList.of(1, 3)
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda x: x % 2 == 0) == ImmutableList.of(2, 4)
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda x: x > 2) == ImmutableList.of(3, 4)
    assert ImmutableList.empty().filter(lambda x: x % 2 == 1) == ImmutableList.empty()

# Generated at 2022-06-14 03:21:24.593080
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x == 2) == ImmutableList.of(2)
    assert ImmutableList.of(1).filter(lambda x: x == 2) == ImmutableList.empty()
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x > 2) == ImmutableList.of(3)
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x > 3) == ImmutableList.empty()


# Generated at 2022-06-14 03:21:31.144872
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    import pytest

    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x > 3) == 4
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x > 5) is None
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: True) == 1
    assert ImmutableList.empty().find(lambda x: True) is None


# Generated at 2022-06-14 03:21:34.379207
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    is_a_or_b = lambda c: c in ['a', 'b']
    assert ImmutableList.of('a', 'b', 'c').filter(is_a_or_b) == ImmutableList.of('a', 'b')

# Generated at 2022-06-14 03:21:44.214195
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.empty().filter(lambda x: x) == ImmutableList.empty()
    assert ImmutableList.empty().filter(lambda x: not x) == ImmutableList.empty()

    assert ImmutableList(1).filter(lambda x: x) == ImmutableList(1)
    assert ImmutableList(1).filter(lambda x: not x) == ImmutableList.empty()

    assert ImmutableList(1, ImmutableList(2)).filter(lambda x: x) == ImmutableList(1, ImmutableList(2))
    assert ImmutableList(1, ImmutableList(2)).filter(lambda x: not x) == ImmutableList.empty()


# Generated at 2022-06-14 03:21:57.795028
# Unit test for method filter of class ImmutableList

# Generated at 2022-06-14 03:22:01.177518
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    result = ImmutableList.of(1, 2, 3).filter(lambda x: x == 1)

    assert result.head == 1
    assert result.tail.head == None
    assert result.tail.tail == None

# Generated at 2022-06-14 03:22:06.836120
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():

    assert ImmutableList.of(1, 2, 3).find(lambda val: val == 3) == 3
    assert ImmutableList.of(1, 2, 3).find(lambda val: val == 5) == None
    assert ImmutableList.of(1).find(lambda val: val == 1) == 1
    assert ImmutableList.of().find(lambda val: val == 1) == None



# Generated at 2022-06-14 03:22:10.312066
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    result = ImmutableList.of(1, 2, 3, 4, 5).filter(lambda x: x % 2 == 0)

    assert result == ImmutableList.of(2, 4)


# Generated at 2022-06-14 03:22:18.183827
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1).filter(lambda x: x == 1) == ImmutableList.of(1)
    assert ImmutableList.of(1).filter(lambda x: x == 2) == ImmutableList.empty()

    assert ImmutableList.of(1, 2, 3).filter(lambda x: x == 1) == ImmutableList.of(1)
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x == 2) == ImmutableList.of(2)
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x == 3) == ImmutableList.of(3)
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x == 4) == ImmutableList.empty()

# Generated at 2022-06-14 03:22:25.535682
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    non_empty_immutable_list = ImmutableList.of(1, 2, 3)
    assert non_empty_immutable_list.find(lambda x: x > 2) == 3
    assert non_empty_immutable_list.find(lambda x: x > 7) is None
    assert ImmutableList().find(lambda x: True) is None


# Generated at 2022-06-14 03:22:34.418902
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.empty().find(lambda x: x == 1) == None
    assert ImmutableList.of(1).find(lambda x: x == 2) == None
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 2) == 2
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 4) == 4


# Generated at 2022-06-14 03:22:37.899851
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    list_ = ImmutableList.of(1, 2, 3, 4, 5, 6, 7)
    assert None == list_.find(lambda x: x > 10)
    assert 1 == list_.find(lambda x: x < 2)



# Generated at 2022-06-14 03:22:41.382619
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # given
    list = ImmutableList.of(1, 2, 3, 4, 5, 6, 7, 8)

    # when
    el = list.find(lambda el: el == 5)

    # then
    assert 5 == el

# Generated at 2022-06-14 03:22:50.820918
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    def test_it():
        def add_to_list(x, y): return add(x, y)
        l = ImmutableList(2, ImmutableList(4, ImmutableList(6, ImmutableList(8, ImmutableList(8)))))
        assert l.find(lambda s: s == 2) == 2
        assert l.find(lambda s: s == 4) == 4
        assert l.find(lambda s: s == 6) == 6
        assert l.find(lambda s: s == 8) == 8
        assert l.find(lambda s: s == 5) == None
    test_it()
print("test_ImmutableList_find() passed successfully!")

# Generated at 2022-06-14 03:22:54.087558
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 1) is 1
    assert ImmutableList.of(1, 2, 3).find(lambda x: x > 2) is 3
    assert ImmutableList.of(1, 2, 3).find(lambda x: x > 3) is None


# Generated at 2022-06-14 03:23:00.370174
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # Empty list
    assert ImmutableList.empty().find(lambda x: x == 3) is None

    # Non empty list
    assert ImmutableList.of(1, 2).find(lambda x: x == 1) == 1
    assert ImmutableList.of(1, 2).find(lambda x: x == 3) is None

test_ImmutableList_find()



# Generated at 2022-06-14 03:23:03.199931
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    immutable_list = ImmutableList.of(
        'first',
        'second',
        'third'
    )

    assert immutable_list.find(lambda x: x == 'first') == 'first'
    assert immutable_list.find(lambda x: len(x) == 7) == 'second'
    assert immutable_list.find(lambda x: x == 'fourth') is None


# Generated at 2022-06-14 03:23:08.862463
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    immutable_list = ImmutableList.of(1, 5, 10, 15)

    assert immutable_list.find(lambda x: x == 10) == 10
    assert immutable_list.find(lambda x: x > 0) == 1
    assert immutable_list.find(lambda x: x > 100) is None

    assert ImmutableList.empty().find(lambda x: x > 100) is None


# Generated at 2022-06-14 03:23:12.116796
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 3) == 3
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 6) is None



# Generated at 2022-06-14 03:23:18.057938
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.empty().find(lambda x: True) == None
    assert ImmutableList.of(3).find(lambda x: x == 3) == 3
    assert ImmutableList.of(3, 4).find(lambda x: x == 4) == 4
    assert ImmutableList.of(1, 3, 5).find(lambda x: x == 5) == 5


# Generated at 2022-06-14 03:23:34.683085
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():

    # Test if method find returns None  when list is empty
    def test_ImmutableList_find_empty():
        assert ImmutableList.empty().find(lambda x: x) == None

    # Test if method find returns None  when list do not contain proper element
    def test_ImmutableList_find_do_not_contain():
        assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x == 5) == None

    # Test if method find returns None  when list do not contain proper element
    def test_ImmutableList_find_contain():
        assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x == 3) == 3

    test_ImmutableList_find_empty()
    test_ImmutableList_find_do_not_contain()
    test_

# Generated at 2022-06-14 03:23:42.125888
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList().find(lambda x: x == 'x') == None
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 2) == 2
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 4) == None


test_ImmutableList_find()


# Generated at 2022-06-14 03:23:48.394516
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 1) == 1
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 2) == 2
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 3) == 3
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 4) is None
    
    

# Generated at 2022-06-14 03:23:54.907310
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList\
        .of(1, 2, 3, 4, None)\
        .find(lambda el: el % 2 == 0) == 2

    assert ImmutableList\
        .of(1, 2, 3, 4, None)\
        .find(lambda el: el % 2 == 1) == 1

    assert ImmutableList\
        .of(1, 2, 3, 4, None)\
        .find(lambda el: el % 2 == 0 and el > 3) == 4

    assert ImmutableList\
        .of(1, 2, 3, 4, None)\
        .find(lambda el: el % 2 == 0 and el > 5) is None


# Generated at 2022-06-14 03:24:01.348210
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 2) == 2
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 4) is None
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 1) == 1

# Generated at 2022-06-14 03:24:08.629490
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.empty().find(lambda x: x == 20) is None
    assert ImmutableList.empty().find(lambda x: x == 30) is None
    assert ImmutableList.of(4, 6, 12, 18, 20).find(lambda x: x == 20) == 20
    assert ImmutableList.of(4, 6, 12, 18, 20).find(lambda x: x == 30) is None
    assert ImmutableList.of(4, 6, 12, 18, 20).find(lambda x: x == 20) == 20
    assert ImmutableList.of(4, 6, 12, 18, 20).find(lambda x: x == 30) is None
    assert ImmutableList.of(4, 6, 12, 18, 20).find(lambda x: x == 20) == 20

# Generated at 2022-06-14 03:24:13.908216
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    test_immutable_list = ImmutableList.of(
        7,
        8,
        9,
        10
    )

    assert test_immutable_list.find(lambda x: x == 8) == 8
    assert test_immutable_list.find(lambda x: x == 6) is None


# Generated at 2022-06-14 03:24:18.824203
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 2) == 2
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 4) is None
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 3) == 3



# Generated at 2022-06-14 03:24:25.132820
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4, ImmutableList(5))))) \
        .find(lambda x: x == 3) == 3
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4, ImmutableList(5))))) \
        .find(lambda x: x == 7) == None


# Generated at 2022-06-14 03:24:29.267683
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    lines = ImmutableList.of(
        'line_one',
        'line_two',
        'line_three'
    )

    def find_line(line: str):
        return line == 'line_two'

    assert lines.find(find_line) == 'line_two'

# Generated at 2022-06-14 03:24:45.183809
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.empty().find(lambda x: x == 'foo') is None
    assert ImmutableList(3, ImmutableList(2, ImmutableList(1))).find(lambda x: x == 5) is None
    assert ImmutableList(3, ImmutableList(2, ImmutableList(1))).find(lambda x: x == 3) == 3
    assert ImmutableList(3, ImmutableList(2, ImmutableList(1))).find(lambda x: x < 4) == 'foo'



# Generated at 2022-06-14 03:24:48.313877
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    imm = ImmutableList.of(1, 2, 3, 4)

    found = imm.find(lambda x: x == 4)

    assert found == 4


# Generated at 2022-06-14 03:24:51.777951
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2).find(lambda x: x == 2) == 2
    assert ImmutableList.of(1, 2).find(lambda x: x == 3) is None


# Generated at 2022-06-14 03:24:56.030892
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    empty_list = ImmutableList.empty()

    assert empty_list.find(lambda x: x > 4) is None

    list_with_five_elements = ImmutableList.of(1, 2, 3, 4, 5)

    assert list_with_five_elements.find(lambda x: x * 2 > 5) == 3

# Generated at 2022-06-14 03:25:01.749365
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x % 2 == 0) == 2
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x % 2 == 1) == 1
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x % 7 == 0) == None
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x % 7 == 1) == None


# Generated at 2022-06-14 03:25:21.096153
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # assert len(ImmutableList(is_empty=True)) == 0
    # assert len(ImmutableList(1)) == 1
    # assert len(ImmutableList(1, ImmutableList(2))) == 2
    # assert len(ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4))))) == 4
    my_list = ImmutableList.of(1, 2, 3, 4, 5)
    assert my_list.find(lambda x: x == 1) == 1
    assert my_list.find(lambda x: x == 2) == 2
    assert my_list.find(lambda x: x == 3) == 3
    assert my_list.find(lambda x: x == 4) == 4
    assert my_list.find(lambda x: x == 5) == 5

# Generated at 2022-06-14 03:25:28.815638
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    cases = [
        {
            'case': 'returns first element of ImmutableList that passed info argument returns True',
            'args': (lambda x: x == 2,),
            'expected': 2
        },
        {
            'case': 'returns None if there are no elements in list',
            'args': (lambda x: x == 2,),
            'expected': None
        },
        {
            'case': 'returns None if argument return False for all elements',
            'args': (lambda x: x == 0,),
            'expected': None,
        },
    ]

    for test_case in cases:
        assert ImmutableList.of(1,2,3).find(*test_case['args']) == test_case['expected']


# Generated at 2022-06-14 03:25:38.286400
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(6).find(lambda x: x == 6) == 6
    assert ImmutableList.of(6, 7).find(lambda x: x == 7) == 7
    assert ImmutableList.of(6, 7, 8).find(lambda x: x == 8) == 8
    assert ImmutableList.of(6, 7, 8).find(lambda x: x == 10) is None

test_ImmutableList_find()


# Generated at 2022-06-14 03:25:45.435891
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.empty().find(lambda _: False) is None
    assert ImmutableList.of(1, 2, 3).find(lambda _: False) is None
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x % 2 == 0) == 2
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x % 2 == 1) == 1

# Generated at 2022-06-14 03:25:55.861250
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.empty().find(lambda x: x == 'x') == None
    assert ImmutableList.of('x').find(lambda x: x == 'x') == 'x'
    assert ImmutableList.of('a', 'b', 'x', 'd').find(lambda x: x == 'x') == 'x'
    assert ImmutableList.of('a', 'b', 'c', 'd').find(lambda x: x == 'x') == None



# Generated at 2022-06-14 03:26:19.177164
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    array = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    assert array.find(lambda value: value == 2) == 2
    assert array.find(lambda value: value == 4) is None



# Generated at 2022-06-14 03:26:27.288296
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.empty().find(lambda x: x is 1) is None
    assert ImmutableList.of(1).find(lambda x: x is 1) == 1
    assert ImmutableList.of(1, 2).find(lambda x: x is 1) == 1
    assert ImmutableList.of(2, 1).find(lambda x: x is 1) == 1
    assert ImmutableList.of(1, 2, 3).find(lambda x: x is 1) == 1
    assert ImmutableList.of(1, 2, 3).find(lambda x: x is 2) == 2
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x is 2) == 2
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x is 4) == 4
    

# Generated at 2022-06-14 03:26:34.633336
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    cases = [
        ((ImmutableList.of(10), lambda x: x == 10), 10),
        ((ImmutableList.of(10).append(20), lambda x: x == 10), 10),
        ((ImmutableList.of(10).append(20).append(30).append(40), lambda x: x == 20), 20),
    ]

    for case_data in cases:
        case, expected = case_data
        obj = case[0]
        fn = case[1]
        
        assert obj.find(fn) == expected

# Generated at 2022-06-14 03:26:41.716610
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # given
    string_list = ['first', 'second', 'third', 'fourth']
    # when
    functional_list = ImmutableList().of(*string_list)
    # then
    assert functional_list.find(lambda x: x == 'first') == 'first'
    assert functional_list.find(lambda x: x == 'second') == 'second'
    assert functional_list.find(lambda x: x == 'third') == 'third'
    assert functional_list.find(lambda x: x == 'fourth') == 'fourth'
    assert functional_list.find(lambda x: x == 'fifth') == None
