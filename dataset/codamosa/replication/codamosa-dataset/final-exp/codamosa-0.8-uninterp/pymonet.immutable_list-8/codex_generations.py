

# Generated at 2022-06-14 03:16:47.399019
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    a = ImmutableList.of(1, 2, 3, 4)
    assert a.find(lambda x: x > 2) == 3

# Generated at 2022-06-14 03:16:53.777294
# Unit test for method __len__ of class ImmutableList
def test_ImmutableList___len__():
    empty_lst = ImmutableList.empty()
    assert len(empty_lst) == 0

    lst_1 = ImmutableList(1)
    assert len(lst_1) == 1

    lst_2 = ImmutableList.of(1, 2, 3, 4)
    assert len(lst_2) == 4


# Generated at 2022-06-14 03:16:57.547788
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list_to_filter = ImmutableList.of(1, 2, 3, 4, 5, 6)
    filtered = list_to_filter.filter(lambda x: True if x > 3 else False)

    assert filtered == ImmutableList.of(4, 5, 6)


# Generated at 2022-06-14 03:17:03.950401
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.of(1, 2, 3) == ImmutableList.of(1, 2, 3)
    assert ImmutableList(1, ImmutableList(2)) == ImmutableList(1, ImmutableList(2))
    assert ImmutableList.of('a', 'b') != ImmutableList.of('a', 'b', 'c')
    assert ImmutableList.of(1, 2, 3).map(lambda x: x * 2) != ImmutableList.of(1, 2, 3)
    assert ImmutableList.empty() == ImmutableList.empty()


# Generated at 2022-06-14 03:17:17.293999
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList(1) == ImmutableList(1)
    assert ImmutableList(1).__eq__(ImmutableList(1))
    assert ImmutableList(1, ImmutableList(2)) == ImmutableList(1, ImmutableList(2))
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))) == ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    assert ImmutableList(1, ImmutableList(2)) != ImmutableList(1, ImmutableList(3))
    assert ImmutableList(1) != ImmutableList(2)
    assert not ImmutableList(1, ImmutableList(2)).__eq__(ImmutableList(1, ImmutableList(3)))
    assert not ImmutableList(1).__eq__(ImmutableList(2))


# Generated at 2022-06-14 03:17:27.402822
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():

    v1 = ImmutableList.of(1,2,3,4,5)
    v2 = ImmutableList.of(1,2,3,4,5)
    assert v1 == v2

    v1 = ImmutableList.of(1,2,3,4)
    v2 = ImmutableList.of(1,2,3,4,5)
    assert v1 != v2

    v2 = ImmutableList.of(1,2,3,4,5)
    assert v1 != v2

    v1 = ImmutableList.of(1,2,3,4)
    v2 = ImmutableList.empty()
    assert v1 != v2

    v1 = ImmutableList.empty()
    v2 = ImmutableList.empty()
    assert v1 == v2

test_Imm

# Generated at 2022-06-14 03:17:35.803560
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    assert lst.find(lambda x: x == 1) == 1
    assert lst.find(lambda x: x == 2) == 2
    assert lst.find(lambda x: x == 3) == 3
    assert lst.find(lambda x: x == 4) == 4
    assert lst.find(lambda x: x == 5) == 5
    assert lst.find(lambda x: x == 6) == None
    assert lst.find(lambda x: x == 7) == None


# Generated at 2022-06-14 03:17:40.752893
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    a = ImmutableList([1, 2, 3])
    b = ImmutableList([1, 2, 3])

    assert a.__eq__(b)

    a = ImmutableList([1, 2, 3])
    b = ImmutableList([1, 2, 5])

    assert not a.__eq__(b)

    a = ImmutableList([1, 2, 3])
    b = ImmutableList(7)

    assert not a.__eq__(b)

# Generated at 2022-06-14 03:17:50.852853
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.empty() == ImmutableList.empty()
    assert ImmutableList.of(1, 2) == ImmutableList.of(1, 2)
    assert ImmutableList.of(1, 2) == ImmutableList.empty() + ImmutableList.of(1, 2)
    assert ImmutableList.of(1, 2) == ImmutableList.of(1, 2) + ImmutableList.empty()
    assert ImmutableList.of(1, 2) == ImmutableList.of(1) + ImmutableList.of(2)
    assert ImmutableList.of(1) + ImmutableList.of(2) == ImmutableList.of(1, 2)
    assert ImmutableList.of(1, 2) == ImmutableList.of(1, 2) + ImmutableList.empty()
    assert Immutable

# Generated at 2022-06-14 03:17:53.113044
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    list = ImmutableList.of(1, 2, 3, 4, 5, 6, 7)
    assert list.find(lambda x: x == 3) == 3



# Generated at 2022-06-14 03:18:07.267349
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # Create test data
    list_of_even_numbers = ImmutableList.of(1, 2, 3, 4, 5, 6, 7, 8, 9)
    expected_list = ImmutableList.of(2, 4, 6, 8)

    # Check result of filtering list
    result_list = list_of_even_numbers.filter(lambda x: x % 2 == 0)
    assert expected_list == result_list


# Generated at 2022-06-14 03:18:10.394852
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # given
    x = ImmutableList.of(1, 2, 3)

    # when
    result = x.find(lambda x: x == 2)

    # then
    assert result == 2


# Generated at 2022-06-14 03:18:16.586975
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list_not_passed = ImmutableList.of(1, 2, 3)
    list_passed = ImmutableList.of(1, 2, 3)
    assert list_not_passed.filter(lambda x: x < 3) == ImmutableList.of(1, 2)
    assert list_passed.filter(lambda x: x < 3) == ImmutableList.of(1, 2)

# Generated at 2022-06-14 03:18:19.402150
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # Given
    head = 2
    tail = ImmutableList(1)
    immutable_list = ImmutableList(head, tail)

    # When
    result = immutable_list.find(lambda x: x == 2)

    # Then
    assert result == 2


# Generated at 2022-06-14 03:18:24.033419
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list_ = ImmutableList.of(1, 2, 3, 4)
    new_list = list_.filter(lambda x: x % 2 == 0)
    assert new_list.head == 2
    assert new_list.tail.head == 4


# Generated at 2022-06-14 03:18:27.664961
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 2) == 2
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 0) is None


# Generated at 2022-06-14 03:18:31.178086
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(0, 1, 2, 3).filter(lambda x: x < 2) == ImmutableList.of(0, 1)
    assert ImmutableList.of(0, 1, 2, 3).filter(lambda x: x < 0) == ImmutableList.empty()



# Generated at 2022-06-14 03:18:46.709409
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    list_ = ImmutableList.of("a", "b", "c")
    assert list_.find(lambda value: value == "a") == "a"
    assert list_.find(lambda value: value == "b") == "b"
    assert list_.find(lambda value: value == "c") == "c"
    assert list_.find(lambda value: value == "d") is None


# Generated at 2022-06-14 03:18:51.569843
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    iterator = range(11)
    some_list = ImmutableList.of(*iterator)
    result = some_list.filter(lambda x: x % 2 == 0).to_list()
    assert result == list(filter(lambda x: x % 2 == 0, iterator))

# Generated at 2022-06-14 03:18:53.974747
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x > 1) == 2
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 4) == 4
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 1) == 1
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 100) is None


# Generated at 2022-06-14 03:19:06.812283
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4, 5, 6, 7, 8, 9).filter(lambda x: x > 4 and x % 2 == 0) == \
            ImmutableList.of(6, 8)
    assert ImmutableList.of(1, 2, 3, 4, 5, 6, 7, 8, 9).filter(lambda x: x > 0 and x % 2 == 0) == \
            ImmutableList.of(2, 4, 6, 8)
    assert ImmutableList.of(1, 2, 3, 4, 5, 6, 7, 8, 9).filter(lambda x: x > 1 and x % 2 != 0) == \
            ImmutableList.of(3, 5, 7, 9)

# Generated at 2022-06-14 03:19:15.487629
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    first_list = ImmutableList.of(1, 2, 9)
    second_list = ImmutableList.of(2, 9)
    third_list = ImmutableList.of(9)
    fourth_list = ImmutableList.of(9, 11)

    assert first_list.find(lambda a: a < 10) == 1
    assert second_list.find(lambda a: a % 2 == 0) == 2
    assert third_list.find(lambda a: a > 10) == None
    assert fourth_list.find(lambda a: a % 2 != 0) == 9


test_ImmutableList_find()

# Generated at 2022-06-14 03:19:19.982011
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # Init
    _input = ImmutableList.of(1, 2, 3, 4, 5)
    _expected = 3

    # Run
    _result = _input.find(lambda x: x == _expected)

    # Assert
    assert _result == _expected

# Generated at 2022-06-14 03:19:25.838720
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    list_ = ImmutableList.of(0, 1, 2, 3, 4, 5, 6, 7, 8)

    def is_even(value):
        return value % 2 == 0

    assert list_.find(is_even) == 0

    list_ = ImmutableList.empty()
    assert list_.find(is_even) is None


if __name__ == '__main__':
    test_ImmutableList_find()

# Generated at 2022-06-14 03:19:33.351541
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    even = lambda x: x % 2 == 0
    list_1 = ImmutableList.of(1, 3, 5, 7, 9)
    list_2 = ImmutableList.of(2, 4, 6, 8)
    list_3 = ImmutableList.empty()

    assert list_1.filter(even) == ImmutableList.empty()
    assert list_2.filter(even) == ImmutableList.of(2, 4, 6, 8)
    assert list_3.filter(even) == ImmutableList.empty()


# Generated at 2022-06-14 03:19:38.871491
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    data = ImmutableList.of(1,2,3,4,5,6)
    data = data.filter(lambda elem: elem % 2 == 0)

    assert data == ImmutableList.of(2,4,6)


# Generated at 2022-06-14 03:19:46.503170
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list_ = ImmutableList.of(1, 4, 9, 16, 25)

    assert list_.filter(lambda x: x % 2 == 0) == ImmutableList.of(4, 16)
    assert list_.filter(lambda x: x % 2 != 0) == ImmutableList.of(1, 9, 25)

    assert ImmutableList.of(7, 9, 11).filter(lambda x: x % 2 == 0) == ImmutableList.empty()



# Generated at 2022-06-14 03:19:52.876253
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    """
    Test case for method find(self, fn: Callable[[Optional[T]], bool]) -> Optional[T]
    """
    test_cases = [
        (ImmutableList.of(1, 2, 3, 4), lambda x: x > 2, 3),
        (ImmutableList.of(1, 2, 3, 4), lambda x: x > 10, None)
    ]

    for test in test_cases:
        assert test[0].find(test[1]) == test[2]

# Generated at 2022-06-14 03:19:58.742148
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # Arrange
    list_ = ImmutableList.of(1,2,3,4)
    # Act
    result = list_.find(lambda x: x == 4)
    # Assert
    assert result == 4

# Generated at 2022-06-14 03:20:02.723833
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # Arrange
    some_list = ImmutableList.of(1, 2, 3)
    condition = lambda x: x < 2

    # Act
    result = some_list.find(condition)

    # Assert
    assert result == 1


# Generated at 2022-06-14 03:20:20.901942
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    empty = ImmutableList.empty()
    assert empty.filter(lambda _: False) == ImmutableList(is_empty=True)

    one_element_list = ImmutableList(1)
    assert one_element_list.filter(lambda _: False) == ImmutableList(is_empty=True)
    assert one_element_list.filter(lambda _: True) == ImmutableList(1)

    two_elements_list = ImmutableList(1, ImmutableList(2))
    assert two_elements_list.filter(lambda _: False) == ImmutableList(is_empty=True)
    assert two_elements_list.filter(lambda x: x % 2 == 0) == ImmutableList(2)


test_ImmutableList_filter()

# Generated at 2022-06-14 03:20:31.188274
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3).filter(bool) == ImmutableList.of(1, 2, 3)
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x > 2) == ImmutableList.of(3)
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x < 2) == ImmutableList.of(1)
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x == 2) == ImmutableList.of(2)
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x == 0) == ImmutableList.empty()
    assert ImmutableList.of("hello", "world", "!").filter(bool).map(len) == ImmutableList.of(5, 5, 1)

# Generated at 2022-06-14 03:20:33.640338
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(lambda x: x % 2 == 0) == ImmutableList.of(2, 4)

test_ImmutableList_filter()

# Generated at 2022-06-14 03:20:38.490577
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(lambda n: n % 2 == 0) == ImmutableList.of(2, 4)
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(lambda n: True) == ImmutableList.of(1, 2, 3, 4, 5)
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(lambda n: False) == ImmutableList.empty()
    assert ImmutableList.empty().filter(lambda n: False) == ImmutableList.empty()


# Generated at 2022-06-14 03:20:44.157557
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list_ = ImmutableList.of(1, 2, 3, 4, 5)
    filtered_list = list_.filter(lambda x: x > 3)
    
    assert filtered_list == ImmutableList(4, ImmutableList(5))

# Generated at 2022-06-14 03:20:50.395979
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # Given
    l = ImmutableList.of(1, 2, 4, 5)
    # When
    test_list1 = l.filter(lambda x: x % 2 == 1)
    test_list2 = l.filter(lambda x: x % 2 == 0)
    test_list3 = l.filter(lambda x: x > 3)
    # Then
    assert len(test_list1) == len(l) - 1
    assert len(test_list2) == len(l) - 2
    assert len(test_list3) == 1



# Generated at 2022-06-14 03:20:58.506053
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x > 1) == ImmutableList.of(2, 3)
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x < 1) == ImmutableList()
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x == 2) == ImmutableList.of(2)
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x < 1) == ImmutableList.of(is_empty=True)


# Generated at 2022-06-14 03:21:07.912588
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList(0).filter(lambda x: x > 0) == ImmutableList(is_empty=True)
    assert ImmutableList(1, ImmutableList(2)).filter(lambda x: x > 0) == ImmutableList(1, ImmutableList(2))
    assert ImmutableList(1, ImmutableList(2), ImmutableList(1)).filter(lambda x: x > 0) == ImmutableList(1, ImmutableList(2), ImmutableList(1))
    assert ImmutableList(0, ImmutableList(2), ImmutableList(1)).filter(lambda x: x > 0) == ImmutableList(2, ImmutableList(1))

# Generated at 2022-06-14 03:21:11.480788
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(2, 3, 4, 5).find(lambda x: x == 4) == 4
    assert ImmutableList.empty().find(lambda x: x == 4) is None
    assert ImmutableList.of(2).find(lambda x: x == 2) == 2

# Generated at 2022-06-14 03:21:14.208473
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    list = ImmutableList.of(1, 2, 3, 4, 5)
    assert list.find(lambda x: x < 2) == 1


# Generated at 2022-06-14 03:21:25.150397
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # given
    given_list = ImmutableList.of(1, 2, 3, 4, 5, 6)
    given_expected_value = 6

    # when
    def test_if_value_is_six(number) -> bool:
        return number == 6

    given_found_value = given_list.find(test_if_value_is_six)

    # then
    assert given_expected_value == given_found_value



# Generated at 2022-06-14 03:21:33.818195
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda x: x < 3).to_list() == [1, 2]
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda x: x > 3).to_list() == [4]
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda x: x > 5) == ImmutableList.empty()
    assert ImmutableList.empty().filter(lambda x: x > 5) == ImmutableList.empty()
    assert ImmutableList.of(1, 2, 3, 4).filter(
        lambda x: x > 10).to_list() == []



# Generated at 2022-06-14 03:21:37.902129
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    test_list = ImmutableList.of(3, 2, 5, 7, 11)
    assert test_list.find(lambda x: x % 2 == 0) == 2
    assert test_list.find(lambda x: x % 5 == 0) == 5
    assert test_list.find(lambda x: x % 3 == 0) == 3
    assert test_list.find(lambda x: x % 13 == 0) == None
    assert test_list.find(lambda x: x % 1 == 0) == 3

test_ImmutableList_find()

# Generated at 2022-06-14 03:21:42.589669
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    list_of_integers = ImmutableList.of(1, 2, 3, 4, 5)

    assert list_of_integers.find(lambda n: n > 3) == 4

    assert list_of_integers.find(lambda n: n > 100) is None


# Generated at 2022-06-14 03:21:47.199490
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    """
    Method checks that ImmutableList.filter works correctly
    """
    assert ImmutableList.of(1, 2, 3, 4, 5, 6, 7).filter(lambda x: x % 2 == 0) == ImmutableList.of(2, 4, 6)
    assert ImmutableList.of(1, 2, 3, 4, 5, 6, 7).filter(lambda x: x < 4) == ImmutableList.of(1, 2, 3)



# Generated at 2022-06-14 03:21:56.269276
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    immutable_list = ImmutableList.of(1, 2, 3)

    assert immutable_list.find(lambda i: i == 1) == 1
    assert immutable_list.find(lambda i: i == 2) == 2
    assert immutable_list.find(lambda i: i == 3) == 3
    assert immutable_list.find(lambda i: i == 4) is None
    assert immutable_list.find(lambda i: i == 5) is None



# Generated at 2022-06-14 03:22:06.445265
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.empty().filter(lambda x: x == 3).to_list() == []
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(lambda x: x == 3).to_list() == [3]
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(lambda x: x > 3).to_list() == [4, 5]
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(lambda x: x < 3).to_list() == [1, 2]
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(lambda x: x % 2 == 0).to_list() == [2, 4]


# Generated at 2022-06-14 03:22:11.713372
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(None).find(lambda x: x is None) is None
    assert ImmutableList.of(None).find(lambda x: x is not None) is None
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 1) == 1
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 2) == 2
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 3) == 3
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 4) is None
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 5) is None

# Generated at 2022-06-14 03:22:23.232556
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    source_list = ImmutableList(0, ImmutableList(1, ImmutableList(2, ImmutableList(3))))

    assert [0, 2] == source_list.filter(lambda x: x % 2 == 0).to_list()


# Generated at 2022-06-14 03:22:29.065553
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list = ImmutableList.of(
        5, 4, 2, 1, 3,
    )
    filtered_list = list.filter(
        lambda el: el % 2 == 0
    )

    assert filtered_list == ImmutableList.of(4, 2)

# Generated at 2022-06-14 03:22:37.706794
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(lambda x: x % 2 == 0) == ImmutableList.of(2, 4)

# Generated at 2022-06-14 03:22:43.274588
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    list_of_numbers = ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4))))

    assert list_of_numbers.find(lambda x: x > 2) == 3
    assert list_of_numbers.find(lambda x: x == 2) == 2
    assert list_of_numbers.find(lambda x: x == 10) is None


# Generated at 2022-06-14 03:22:47.331063
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3).find(lambda x: x > 1) == 2
    assert ImmutableList.of(1, 2, 3).find(lambda x: x > 4) is None


# Generated at 2022-06-14 03:22:53.317388
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    f = ImmutableList.of(1, 3, 4, 5)
    g = f.filter(lambda x: x > 2)
    assert(g == ImmutableList.of(3, 4, 5))
    h = g.filter(lambda x: x > 4)
    assert(h == ImmutableList.of(5))
    i = g.filter(lambda x: x > 6)
    assert(i == ImmutableList.of(is_empty=True))


# Generated at 2022-06-14 03:22:57.155307
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x > 2).to_list() == [3]
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x < 2).to_list() == [1]
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x > 4).to_list() == []
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x > 0).to_list() == [1, 2, 3]



# Generated at 2022-06-14 03:23:04.575262
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    a = ImmutableList.of(
        1, 2, 3
    )
    b = a.filter(
        lambda value: value % 2 == 0
    )
    assert(a == ImmutableList.of(1, 2, 3))
    assert(b == ImmutableList.of(2))



# Generated at 2022-06-14 03:23:08.853061
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list = ImmutableList.of(1, 2, 3, 4, 5, 6)
    assert list.filter(lambda v: v < 3).to_list() == [1, 2]
    assert list.filter(lambda v: v > 3).to_list() == [4, 5, 6]
    assert list.filter(lambda v: v > 6).to_list() == []


# Generated at 2022-06-14 03:23:19.607580
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    alist = ImmutableList.of(1, 4, 8, 12, 16)
    assert alist.find(lambda x: x > 5) == 8

    alist = ImmutableList.of(1, 4, 8, 12, 16)
    assert alist.find(lambda x: x > 10) == 12

    alist = ImmutableList.of(1, 4, 8, 12, 16)
    assert alist.find(lambda x: x > 15) == 16

    alist = ImmutableList.of(1, 4, 8, 12, 16)
    assert alist.find(lambda x: x > 20) is None

    alist = ImmutableList.of(1, 4, 8, 12, 16)
    assert alist.find(lambda x: x > 0) == 1

    alist = ImmutableList.of

# Generated at 2022-06-14 03:23:29.184576
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1).find(lambda x: x == 1) == 1
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x == 1) == 1
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x == 2) == 2
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x == 3) == 3
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x == 4) == 4
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x == 0) is None
    assert ImmutableList.empty().find(lambda x: x == 0) is None



# Generated at 2022-06-14 03:23:31.654833
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(lambda x: x > 2) == ImmutableList.of(3, 4, 5)


test_ImmutableList_filter()

# Generated at 2022-06-14 03:23:48.544275
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # Given
    a1 = ImmutableList.of(1, 2, 3, 4, 5)

    # When
    a2 = a1.filter(lambda x: x % 2 == 0)

    # Then
    assert a2 == ImmutableList.of(2, 4)


# Generated at 2022-06-14 03:23:52.931618
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.empty().filter(lambda x: True) == ImmutableList()
    assert ImmutableList.of(1, 2, 3, 4, 5) \
        .filter(lambda x: x % 2 == 0) == ImmutableList.of(2, 4)
    assert ImmutableList.of('a', 'b', 'c') \
        .filter(lambda x: x == 'a') == ImmutableList.of('a')
    assert ImmutableList.of('a', 'b', 'a') \
        .filter(lambda x: x == 'a') == ImmutableList.of('a', 'a')

# Generated at 2022-06-14 03:24:04.042834
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x == 2).to_list() == [2]
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x == 10).to_list() == []
    assert ImmutableList.of('foo', 'bar', 'bazz').filter(lambda x: x == 'foo').to_list() == ['foo']
    assert ImmutableList.of('foo', 'bar', 'bazz').filter(lambda x: len(x) == 3).to_list() == ['foo', 'bar']
    assert ImmutableList.of('foo', 'bar', 'bazz').filter(lambda x: len(x) == 2).to_list() == []
    assert ImmutableList().filter(lambda x: x == 2).to_list() == []


#

# Generated at 2022-06-14 03:24:06.992770
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list_1 = ImmutableList.of(1, 2, 3, 4, 5)
    list_2 = ImmutableList.of(2, 4)

    assert list_1.filter(lambda x: x % 2 == 0) == list_2

# Generated at 2022-06-14 03:24:12.222066
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # arrange
    items = ImmutableList.of(1, 2, 3, 4, 5, 6)
    # act
    item = items.find(lambda item: item > 5)
    # assert
    assert(item == 6)

    item = items.find(lambda item: item > 100)
    assert(item is None)



# Generated at 2022-06-14 03:24:18.144455
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(lambda x: x % 2 == 0) == ImmutableList.of(2, 4)
    assert ImmutableList.empty().filter(lambda x: x % 2 == 0) == ImmutableList.empty()
    assert ImmutableList.of(1, 3, 5, 7, 9).filter(lambda x: x % 2 == 0) == ImmutableList.empty()


# Generated at 2022-06-14 03:24:21.437197
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList().find(lambda x: x == 2) is None
    assert ImmutableList(1).find(lambda x: x == 2) is None
    assert ImmutableList(1).find(lambda x: x == 1) == 1
    assert ImmutableList(1, ImmutableList(1)).find(lambda x: x == 1) == 1



# Generated at 2022-06-14 03:24:24.677871
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    l = ImmutableList.of(1, 2, 3, 4)
    assert l.filter(lambda x: x % 2 == 0) == ImmutableList.of(2, 4)

# Generated at 2022-06-14 03:24:27.999037
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # Given
    list = ImmutableList.of(1,2,3)
    # When
    find_one = list.find(lambda x: x == 1)
    find_five = list.find(lambda x: x == 5)
    # Then
    assert find_one == 1
    assert find_five is None
test_ImmutableList_find()


# Generated at 2022-06-14 03:24:35.578340
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4, 5) \
            .filter(lambda elem: elem > 2) == ImmutableList.of(3, 4, 5)
    assert ImmutableList.of(1, 2, 3, 4, 5) \
            .filter(lambda elem: elem % 2 == 0) == ImmutableList.of(2, 4)
    assert ImmutableList.of(1, 2, 3, 4, 5) \
            .filter(lambda elem: elem > 10) == ImmutableList.empty()
    assert ImmutableList.of(1, 2, 3, 4, 5) \
            .filter(lambda elem: elem == 1) == ImmutableList.of(1)

# Generated at 2022-06-14 03:25:06.159893
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    imm_list = ImmutableList.of(1, 2, 3, 4, 5, 6)
    assert imm_list.find(lambda val: val == 4) == 4
    assert imm_list.find(lambda val: val == 7) == None

# Generated at 2022-06-14 03:25:10.943295
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    print('Test ImmutableList.filter')
    # arrange
    list_of_ints = ImmutableList.of(1, -5, 2, 4, 8, -4, 0)
    list_of_strings = ImmutableList.of('a', 'b', 'c')
    list_of_tuples = ImmutableList.of((1, 1), (2, 2), (3, 3), (4, 4))
    list_of_None = ImmutableList.of(None, None, None)

    greater_than_zero = lambda x: x > 0
    less_than_zero = lambda x: x < 0
    is_zero = lambda x: x == 0
    is_not_None = lambda x: x is not None
    is_even = lambda x: x % 2 == 0
    is_odd = lambda x: x

# Generated at 2022-06-14 03:25:20.267301
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    list_ = ImmutableList.empty()
    assert list_.find(lambda x: True) is None

    list_ = ImmutableList.of(1)
    assert list_.find(lambda x: x==1) == 1
    assert list_.find(lambda x: x==10) is None

    list_ = ImmutableList.of(1,2,3,4)
    assert list_.find(lambda x: x==1) == 1
    assert list_.find(lambda x: x==10) is None



# Generated at 2022-06-14 03:25:23.297095
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    l = ImmutableList.of(1, 2, 3)
    assert l.find(lambda x: x > 2) == 3
    assert l.find(lambda x: x < 1) is None
    assert l.find(lambda x: x == 2) == 2

# Generated at 2022-06-14 03:25:27.007438
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    l = ImmutableList.of(1, 2, 3, 4, 5)
    print(l.filter(lambda x: x % 2 == 0).to_list())
    # [2, 4]
    print(l.filter(lambda x: x % 2 == 1).to_list())
    # [1, 3, 5]

# Generated at 2022-06-14 03:25:39.742423
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    result = ImmutableList.of(8, 3, 6, 1).find(lambda x: x % 2 == 0)
    assert result == 8, result

    result = ImmutableList.of(8, 3, 6, 1).find(lambda x: x % 2 == 1)
    assert result == 3, result

    result = ImmutableList.of(8, 3, 6, 1).find(lambda x: x > 10)
    assert result is None, result

    result = ImmutableList.empty().find(lambda x: x > 10)
    assert result is None, result

if __name__ == '__main__':
    test_ImmutableList_find()
    print("Success!")


# Generated at 2022-06-14 03:25:45.434927
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    list1 = ImmutableList.of(
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    )
    list2 = ImmutableList.empty()

    assert list1.find(lambda x: x == 3) == 3
    assert list1.find(lambda x: x == 13) == None
    assert list2.find(lambda x: x == 3) == None

# Generated at 2022-06-14 03:25:58.617197
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.empty().find(lambda x: x == 1) == None
    assert ImmutableList.of(0).find(lambda x: x == 1) == None
    assert ImmutableList.of(0).find(lambda x: x == 0) == 0
    assert ImmutableList.of(0, 1, 2, 3, 4).find(lambda x: x == 0) == 0
    assert ImmutableList.of(0, 1, 2, 3, 4).find(lambda x: x == 4) == 4
    assert ImmutableList.of(0, 1, 2, 3, 4).find(lambda x: x == 3) == 3


if __name__ == "__main__":
    test_ImmutableList_find()

# Generated at 2022-06-14 03:26:04.707978
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(lambda el: el > 1) == \
            ImmutableList.of(2, 3, 4, 5)
    assert ImmutableList.empty().filter(lambda el: el > 1) == \
            ImmutableList.empty()
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(lambda el: el > 3) == \
            ImmutableList.of(4, 5)
    assert ImmutableList.of(1).filter(lambda el: el > 3) == \
            ImmutableList.empty()


# Generated at 2022-06-14 03:26:08.186099
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))).find(lambda x: x < 3) == 1