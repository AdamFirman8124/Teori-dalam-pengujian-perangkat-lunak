

# Generated at 2022-06-14 03:16:53.561595
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3).filter(
        lambda x: x > 2
    ) == ImmutableList.of(3)



# Generated at 2022-06-14 03:17:00.109406
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.of(1, 2, 3) == ImmutableList.of(1, 2, 3)
    assert ImmutableList.of() == ImmutableList.of()
    assert ImmutableList.of(1, 2, 3) != ImmutableList.of(1, 2, 3, 4)
    assert ImmutableList.of(1, 2) != ImmutableList.of(1, 2, 3)
    assert ImmutableList.of(1) != ImmutableList.of()


# Generated at 2022-06-14 03:17:04.499738
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    a = ImmutableList.of(1)
    b = a.append(2).append(3).append(5).append(6)

    assert b.find(lambda x: x == 3) == 3
    assert b.find(lambda x: x < 0) is None
    assert b.find(lambda x: x > 1) == 2
    assert b.find(lambda x: x > 3) == 5



# Generated at 2022-06-14 03:17:10.907557
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    # arrange
    actual = ImmutableList.of(1, 2, 3)
    expected = ImmutableList.of(1, 2, 3)
    # act
    m = actual == expected
    # assert
    assert m


# Generated at 2022-06-14 03:17:14.459491
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert \
        ImmutableList.empty() == ImmutableList.empty()
    assert \
        ImmutableList.of(1, 2, 3) == ImmutableList.of(1, 2, 3)
    assert \
        ImmutableList(1, ImmutableList(2, ImmutableList(3))) == ImmutableList.of(1, 2, 3)

test_ImmutableList___eq__()

# Generated at 2022-06-14 03:17:17.306490
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(2, 3, 4, 5).find(lambda x: x == 3) == 3
    assert ImmutableList.of(2, 3, 4, 5).find(lambda x: x == 0) == None


# Generated at 2022-06-14 03:17:24.207357
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    list1 = ImmutableList.of(1, 2, 3)
    list2 = ImmutableList.of(1, 2, 3)
    assert list1 == list2
    
    list3 = ImmutableList.of(1)
    list4 = ImmutableList.of(1, 2)
    assert list3 != list4
    list5 = ImmutableList.of(1, 2, 3)
    list6 = ImmutableList.of(2, 3)
    assert list5 != list6
    
    

# Generated at 2022-06-14 03:17:28.416598
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    list1 = ImmutableList(1, ImmutableList(2))
    list2 = ImmutableList(1, ImmutableList(2))
    assert list1 == list2


# Generated at 2022-06-14 03:17:35.268684
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    # Case when Immutable list are same
    a = ImmutableList.of(1, 2, 3, 4)
    b = ImmutableList.of(1, 2, 3, 4)
    assert a == b

    # Case when Immutable list are not same
    a = ImmutableList.of(1, 2, 3, 4)
    b = ImmutableList.of(1, 2, 3, '4')
    assert a != b


# Generated at 2022-06-14 03:17:46.573930
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    def even(val: Optional[int]) -> bool:
        if val is None:
            return False
        return val % 2 == 0

    assert ImmutableList.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10).filter(even).to_list() == [2, 4, 6, 8, 10]
    assert ImmutableList.of(2, 3).filter(even).to_list() == [2]
    assert ImmutableList.of(3, 4, 7).filter(even).to_list() == [4]
    assert ImmutableList.of(3, 7).filter(even).to_list() == []
    assert ImmutableList.of(1).filter(even).to_list() == []
    assert ImmutableList.of().filter(even).to_list() == []

#

# Generated at 2022-06-14 03:18:08.652665
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    empty_maybe = ImmutableList()
    assert empty_maybe == ImmutableList()

    maybe_of_1 = ImmutableList.of(1)
    assert maybe_of_1 == ImmutableList.of(1)

    maybe_of_1_and_2 = ImmutableList.of(1, 2)
    assert maybe_of_1_and_2 == ImmutableList.of(1, 2)

    maybe_of_1_and_2_and_3 = ImmutableList.of(1, 2, 3)
    assert maybe_of_1_and_2_and_3 == ImmutableList.of(1, 2, 3)

# Generated at 2022-06-14 03:18:13.912901
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    ls = ImmutableList.of(1, 2, 3, 4)
    assert ls.find(lambda x: x == 2) == 2, "2 was in list"
    assert ls.find(lambda x: x == 7) is None, "7 was not in list"



# Generated at 2022-06-14 03:18:16.636457
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    l1 = ImmutableList.of(1)
    l2 = ImmutableList.of(2)
    l3 = ImmutableList.of(1)

    assert l1 == l3
    assert l1 != l2
    assert l1 == ImmutableList(1, ImmutableList.empty())

# Generated at 2022-06-14 03:18:19.855890
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 2) == 2
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 4) is None


# Generated at 2022-06-14 03:18:24.453314
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    list1 = ImmutableList.of(1, 2, 3)
    list2 = ImmutableList.of(1, 2, 3)
    list3 = ImmutableList.of(1, 2, 4)
    assert list1 == list2
    assert list1 != list3

# Generated at 2022-06-14 03:18:29.259634
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    list = ImmutableList.of(1, 2, 3)
    assert list.find(lambda x: x == 2) == 2
    assert list.find(lambda x: x > 2) == 3
    assert list.find(lambda x: x == 4) is None


if __name__ == '__main__':
    test_ImmutableList_find()

# Generated at 2022-06-14 03:18:38.696098
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    test_list = ImmutableList.of(0, 1, 2, 3, 4, 5)

    # Test even numbers
    def even(n: int) -> bool:
        return n % 2 == 0

    assert test_list.filter(even) == ImmutableList.of(0, 2, 4)

    # Test lower than 4 numbers
    def lower_than_4(n: int) -> bool:
        return n < 4

    assert test_list.filter(lower_than_4) == ImmutableList.of(0, 1, 2, 3)


# Generated at 2022-06-14 03:18:48.447291
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    test_list: ImmutableList[int] = ImmutableList.empty()
    assert test_list.filter(lambda x: x == 5).to_list() == []
    assert test_list.filter(lambda x: x == 1).to_list() == []

    test_list = ImmutableList.of(1)
    assert test_list.filter(lambda x: x == 0).to_list() == []
    assert test_list.filter(lambda x: x != 1).to_list() == []
    assert test_list.filter(lambda x: x == 1).to_list() == [1]

    test_list = ImmutableList.of(1, 2, 3, 4)
    assert test_list.filter(lambda x: x == 4).to_list() == [4]

# Generated at 2022-06-14 03:18:55.109325
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():

    assert ImmutableList(1) == ImmutableList(1)
    assert ImmutableList(1, ImmutableList(2)) == ImmutableList(1, ImmutableList(2))
    assert not ImmutableList(1) == ImmutableList(1, ImmutableList(2))
    assert not ImmutableList(1) == ImmutableList(2)
    assert not ImmutableList(1) == ImmutableList(2, ImmutableList(3))
    assert not ImmutableList(1, ImmutableList(2)) == ImmutableList(1)


# Generated at 2022-06-14 03:18:59.033154
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    """
    Test if method find works properly
    """
    fn = lambda x: x == 3

    assert ImmutableList.empty().find(fn) is None
    assert ImmutableList.of(2).find(fn) is None
    assert ImmutableList.of(2, 3, 4, 5).find(fn) == 3
    assert ImmutableList.of(2, 3).find(fn) == 3


# Generated at 2022-06-14 03:19:12.913879
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    arr = ImmutableList.of(5, 7, -1, 0, 4, 9, 11)
    assert arr.filter(lambda x: x > 0) == ImmutableList.of(5, 7, 4, 9, 11)


# Generated at 2022-06-14 03:19:17.068518
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # given
    list_ = ImmutableList.of(1, 2, 3, 4, 5)
    filter_fn = lambda x: x % 2 == 0

    # when
    filtered = list_.filter(filter_fn)

    # then
    assert filtered == ImmutableList.of(2, 4)

# Generated at 2022-06-14 03:19:20.942084
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # Parameters
    list1 = ImmutableList.of(1, 2, 3, 4, 5, 6)
    def fn(el):
        return el < 4
    f = list1.filter(fn)
    elements = f.to_list()
    expected_elements = [1, 2, 3]
    assert elements == expected_elements


# Generated at 2022-06-14 03:19:25.257112
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    """
    Test case for checking correctness of method find of class ImmutableList
    """
    my_list = ImmutableList.of(1, 2, 3, 4, 5)
    
    assert my_list.find(lambda x: x > 3) == 4



# Generated at 2022-06-14 03:19:43.617916
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list_in = ImmutableList(1, ImmutableList(2, ImmutableList(3)))

    list_1 = list_in.filter(lambda x: x > 1)
    list_2 = list_in.filter(lambda x: x > 2)
    list_3 = list_in.filter(lambda x: x > 3)
    list_4 = list_in.filter(lambda x: x > 4)

    assert list_1 == ImmutableList(2, ImmutableList(3))
    assert list_2 == ImmutableList(3)
    assert list_3 == ImmutableList(is_empty=True)
    assert list_4 == ImmutableList(is_empty=True)


# Generated at 2022-06-14 03:19:47.857511
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList().filter(lambda _: True) == ImmutableList(is_empty=True), \
        'ImmutableList of empty list should return empty list'
    assert ImmutableList(1, ImmutableList(2)).filter(lambda _: True) == ImmutableList(1, ImmutableList(2)), \
        'ImmutableList should return immutable list if all elements in it pass filter check'
    assert ImmutableList(1, ImmutableList(2)).filter(lambda x: x % 2 == 0) == ImmutableList(2), \
        'ImmutableList should return list with values that pass in filter'



# Generated at 2022-06-14 03:19:49.972715
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list_ = ImmutableList.of(1, 2, 3)
    filtered_list = list_.filter(lambda x: x == 2)

    assert len(filtered_list) == 1

    assert filtered_list.head == 2
    assert filtered_list.tail is None


# Generated at 2022-06-14 03:19:53.015713
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 3) == 3

# Generated at 2022-06-14 03:19:58.147271
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    result = ImmutableList.of(1, 2, 3, 4).filter(lambda x: x%2==0)
    assert result == ImmutableList.of(2, 4)


# Generated at 2022-06-14 03:20:04.309177
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    ImmutableList.of(1, 2, 3, 4).filter(lambda x: x > 2) == ImmutableList.of(3, 4)
    ImmutableList.of(1, 2, 3, 4).filter(lambda x: x > 100) == ImmutableList.empty()
    ImmutableList.of(1, 2, 3, 4).filter(lambda x: x < 1000) == ImmutableList.of(1, 2, 3, 4)


# Generated at 2022-06-14 03:20:33.402120
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList(0, ImmutableList(1, ImmutableList(2, ImmutableList(3)))).filter(lambda x: x % 2 == 0).to_list() == [0, 2]
    assert ImmutableList().filter(lambda x: x % 2 == 0).to_list() == []

# Generated at 2022-06-14 03:20:40.747207
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    def test_simple():
        arr = ImmutableList.of(1, 2, 3, 4)

        filtered = arr.filter(lambda x: x % 2 == 0)

        assert filtered == ImmutableList.of(2, 4)

    def test_with_wrong_list():
        arr = ImmutableList.of(1, 2, 3, 4)

        filtered = arr.filter(lambda x: x % 2 == 0)

        assert filtered != ImmutableList.of(3, 4)

    def test_with_none():
        arr = ImmutableList.of(1, 2, 3, 4)

        filtered = arr.filter(lambda x: x % 2 == 0)

        assert filtered != ImmutableList.of(2, 4, None)

    def test_with_empty_list():
        arr = ImmutableList.empty()

# Generated at 2022-06-14 03:20:46.982080
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    number_list = ImmutableList.of(1, 2, 3, 4, 5)
    assert number_list.filter(lambda x: x % 2 == 0).to_list() == [2, 4]

    string_list = ImmutableList.of('a', 'b', 'c')
    assert string_list.filter(lambda x: x == 'b').to_list() == ['b']


# Generated at 2022-06-14 03:20:57.700011
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    returns = ImmutableList.of(1, 2, 3, 4, 5, 6).filter(lambda x: x % 2 != 0)
    assert returns == ImmutableList(1, ImmutableList(3, ImmutableList(5)))
    
    returns = ImmutableList.of().filter(lambda x: x % 2 != 0)
    assert returns == ImmutableList(is_empty=True)
    
    returns = ImmutableList.of(5).filter(lambda x: x % 2 != 0)
    assert returns == ImmutableList(5)
    
    returns = ImmutableList.of(2).filter(lambda x: x % 2 != 0)
    assert returns == ImmutableList(is_empty=True)



# Generated at 2022-06-14 03:21:02.910486
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x == 4) == 4
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x == 10) == None
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x == 1) == 1


# Generated at 2022-06-14 03:21:06.434983
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3).find(lambda x: x > 1) == 2
    assert ImmutableList.of(1, 2, 3).find(lambda x: x > 3) is None
    assert ImmutableList.empty().find(lambda x: False) is None

# Generated at 2022-06-14 03:21:16.013622
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1).filter(lambda x: x == 1) == ImmutableList.of(1)
    assert ImmutableList.of(1).filter(lambda x: x == 2) == ImmutableList.empty()
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x == 1) == ImmutableList.of(1)
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x == 2) == ImmutableList.of(2)
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x == 3) == ImmutableList.of(3)
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x > 1) == ImmutableList.of(2, 3)

# Generated at 2022-06-14 03:21:20.442102
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # Given
    filter_fn = lambda x: isinstance(x, int)
    source_list = [1, 2, 3.1, 4, 5.6, 6, 'test']
    expected_list = [1, 2, 4, 6]
    input_list = ImmutableList.of(*source_list)

    # When
    result_list = input_list.filter(filter_fn)

    # Then
    assert result_list.to_list() == expected_list



# Generated at 2022-06-14 03:21:25.728033
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    
    assert ImmutableList.of(1, 2, 3, 4, 5, 6).filter(lambda x: x<4) == ImmutableList.of(1, 2, 3)
    
    assert ImmutableList.of(1, 2, 3, 4, 5, 6).filter(lambda x: x>0) == ImmutableList.of(1, 2, 3, 4, 5, 6)
    
    assert ImmutableList.of(1, 2, 3, 4, 5, 6).filter(lambda x: x>100) == ImmutableList.empty()

# Generated at 2022-06-14 03:21:29.777410
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # Arrange
    immutable_list = ImmutableList.of(
        1, 2, 3
    )

    # Act
    found = immutable_list.find(
        lambda x: x == 2
    )

    # Assert
    assert found == 2


# Generated at 2022-06-14 03:22:18.931212
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.empty().find(lambda x: True) == None
    assert ImmutableList.of(1).find(lambda x: x != 1) == None
    assert ImmutableList.of(1).find(lambda x: x == 1) == 1
    assert ImmutableList.of(1, 2).find(lambda x: x == 1) == 1
    assert ImmutableList.of(1, 2).find(lambda x: x == 2) == 2
    assert ImmutableList.of(1, 2).find(lambda x: x == 3) == None
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x == 1) == 1
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x == 2) == 2

# Generated at 2022-06-14 03:22:23.676439
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # Given
    list = ImmutableList.of(1)

    # When
    result = list.filter(lambda x: x)

    # Then
    assert result == ImmutableList.of(1)


# Generated at 2022-06-14 03:22:34.717042
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.empty().filter(lambda x: x > 10) == ImmutableList.empty()
    assert ImmutableList.of(1).filter(lambda x: x > 10) == ImmutableList.empty()
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x > 1) == ImmutableList.of(2, 3)

# Generated at 2022-06-14 03:22:45.405408
# Unit test for method filter of class ImmutableList

# Generated at 2022-06-14 03:22:55.238447
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    """
    Method to test find method of class ImmutableList
    """
    test_cases = [
        (
            ImmutableList.of(10, 11, 13, 14, 15),
            lambda x: x == 10,
            10,
        ),
        (
            ImmutableList.of(10, 11, 13, 14, 15),
            lambda x: x == 12,
            None,
        ),
        (
            ImmutableList.of(10, 11, 13, 14, 15),
            lambda x: x == 15,
            15,
        ),
        (
            ImmutableList.of(10),
            lambda x: x == 10,
            10,
        ),
        (
            ImmutableList.empty(),
            lambda x: x == 10,
            None,
        )
    ]

# Generated at 2022-06-14 03:22:59.895240
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # Given
    list = ImmutableList.of(1, 2, 3, 4)
    # When
    result = list.find(lambda x: x == 3)
    # Then
    assert result == 3


# Generated at 2022-06-14 03:23:02.254257
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # arrange
    expected = 1

    list1 = ImmutableList.of(0, 1, 2, 3, 4)
    # act
    actual = list1.find(lambda x: x == expected)
    # assert
    assert expected == actual



# Generated at 2022-06-14 03:23:04.659437
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    result = ImmutableList.of(1, 2, 3).filter(lambda x: x > 1)
    expected = ImmutableList.of(2, 3)

    assert result == expected


# Generated at 2022-06-14 03:23:07.994065
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(lambda x: x % 2 == 0) == ImmutableList.of(2, 4)
    assert ImmutableList.empty().filter(lambda x: x % 2 == 0) == ImmutableList.empty()


# Generated at 2022-06-14 03:23:11.321384
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    my_list = ImmutableList.of(1, 2, 3, 4, 5)

    assert my_list.find(lambda x: x > 3) is not None
    assert my_list.find(lambda x: x > 3) == 4

# Generated at 2022-06-14 03:24:37.612022
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(
        1, 2, 3, 4, 5
    ).find(lambda x: x == 5) == 5

    assert ImmutableList.of(
        'a', 'b', 'c', 'd'
    ).find(lambda x: x == 'd') == 'd'

    assert ImmutableList.of(
        1, 2, 3, 4, 5
    ).find(lambda x: x == 8) == None

    assert ImmutableList.of(
        'a', 'b', 'c', 'd'
    ).find(lambda x: x == 'z') == None



# Generated at 2022-06-14 03:24:41.673460
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list = ImmutableList.of(1,2,3,4,5).filter(lambda x: x % 2 == 0)

    assert ImmutableList.of(2,4) == list

# Generated at 2022-06-14 03:24:46.219614
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    initial_list = ImmutableList.of(1, 2, 3, 4, 5, 6)
    filtered_list = initial_list.filter(lambda i: i % 2 == 0)
    assert filtered_list.to_list() == [2, 4, 6]



# Generated at 2022-06-14 03:24:49.808759
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(
        1, 2, 3, 4, 5, 6
    ).filter(lambda el: el > 3) == ImmutableList.of(
        4, 5, 6
    )



# Generated at 2022-06-14 03:24:52.702880
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda x: x % 2 == 0) == ImmutableList.of(2, 4)


# Generated at 2022-06-14 03:24:57.890656
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    test_cases = [
        (
            ImmutableList.of(1, 2, 3, 4),
            lambda x: x > 2,
            ImmutableList.of(3, 4)
        ),
        (
            ImmutableList.of(0, 1, 2, 3, 4, 5),
            lambda x: x > 3,
            ImmutableList.of(4, 5)
        ),
        (
            ImmutableList.of(3),
            lambda x: x > 3,
            ImmutableList.empty()
        )
    ]

    for list_, condition, expected_result in test_cases:
        result = list_.filter(condition)
        assert result == expected_result


# Generated at 2022-06-14 03:25:01.108004
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(lambda x: x < 3) == ImmutableList.of(1, 2)
    assert ImmutableList.empty().filter(lambda x: x < 3) == ImmutableList.empty()


# Generated at 2022-06-14 03:25:11.262804
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x > 2) == 3



# Generated at 2022-06-14 03:25:21.158606
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1,2,3,4,5).filter(lambda x: x < 3) == ImmutableList.of(1,2)
    assert ImmutableList.of(1,2,3,4,5).filter(lambda x: x > 3) == ImmutableList.of(4,5)
    assert ImmutableList.of(1,2,3,4,5).filter(lambda x: x == 3) == ImmutableList.of(3)
    assert ImmutableList.of(1,2,3,4,5).filter(lambda x: x == 0) == ImmutableList.empty()


# Generated at 2022-06-14 03:25:27.362257
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.empty().filter(lambda x: True) == ImmutableList.empty()
    assert ImmutableList.empty().filter(lambda x: False) == ImmutableList.empty()
    assert ImmutableList.of(0, 1, 2, 3, 4).filter(lambda x: x % 2 == 0) == ImmutableList.of(0, 2, 4)
    assert ImmutableList.of(0, 1, 2, 3, 4).filter(lambda x: True) == ImmutableList.of(0, 1, 2, 3, 4)
    assert ImmutableList.of(0, 1, 2, 3, 4).filter(lambda x: False) == ImmutableList.empty()
