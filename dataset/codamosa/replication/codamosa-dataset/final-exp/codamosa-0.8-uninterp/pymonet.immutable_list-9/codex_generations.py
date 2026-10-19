

# Generated at 2022-06-14 03:16:53.148158
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList(4).filter(lambda x: x > 2) == ImmutableList(4)
    assert ImmutableList(4).filter(lambda x: x > 42) == ImmutableList.empty()


# Generated at 2022-06-14 03:16:57.282093
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    list_a = ImmutableList.of(1)
    assert list_a == ImmutableList.of(1)
    assert list_a != ImmutableList.of(2)

# Generated at 2022-06-14 03:17:00.940394
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1).find(lambda x: x == 1) == 1
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 2) == 2
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 4) is None


# Generated at 2022-06-14 03:17:05.174936
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.empty().find(lambda x: x == 3) == None
    assert ImmutableList.of(1).find(lambda x: x == 1) == 1
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 3) == 3
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 6) == None


# Generated at 2022-06-14 03:17:17.678063
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():

    assert ImmutableList.empty() == ImmutableList.empty()
    assert ImmutableList.of(1, 2, 3) == ImmutableList.of(1, 2, 3)
    assert ImmutableList.of(1, 2, 3) != ImmutableList.of(1, 2, 4)
    assert ImmutableList.of(1, 2, 3) != ImmutableList.of(1, 2, 3, 4)

    # ensure that it is not mutable
    assert not ImmutableList.of(1, 2, 3) != ImmutableList.of(1, 2, 3)
    assert not ImmutableList.of(1, 2, 3) == ImmutableList.of(1, 2, 4)

# Generated at 2022-06-14 03:17:22.612492
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    empty_list = ImmutableList.empty()
    assert empty_list == ImmutableList.empty()
    not_empty_list = ImmutableList.of(1, 2, 3)
    assert not_empty_list == ImmutableList.of(1, 2, 3)
    assert not_empty_list != ImmutableList.of(1)

# Generated at 2022-06-14 03:17:34.288255
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    empty_list = ImmutableList.empty()
    empty_list_too = ImmutableList()
    list_one = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    other_list = ImmutableList(1, ImmutableList.empty())
    another_list = ImmutableList()

    assert empty_list == empty_list_too
    assert empty_list == ImmutableList(is_empty=True)
    assert empty_list != other_list
    assert empty_list != list_one
    assert list_one != other_list
    assert list_one == ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    assert another_list == ImmutableList()



# Generated at 2022-06-14 03:17:37.460495
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda value: value%2 == 0) == ImmutableList.of(2, 4)
    assert ImmutableList.empty().filter(lambda value: value%2 == 0) == ImmutableList.empty()

# Generated at 2022-06-14 03:17:45.934583
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list = ImmutableList.of(1, 2, 45, 0, 1)
    assert list.filter(lambda x: x <= 15) == ImmutableList.of(1, 2, 0, 1)
    assert list.filter(lambda x: x <= 1) == ImmutableList.of(1, 1)
    assert list.filter(lambda _: False) == ImmutableList.of()

test_ImmutableList_filter()

# Generated at 2022-06-14 03:17:49.567883
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    new_list = ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4))))
    new_list2 = ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4))))
    
    assert new_list == new_list2


# Generated at 2022-06-14 03:18:02.924401
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    should_equal = ImmutableList.of('a', 'b', 'c') == ImmutableList.of('a', 'b', 'c')
    should_not_equal = ImmutableList.of('a', 'b') == ImmutableList.of('a', 'b', 'c')
    should_different_types_not_equal = ImmutableList.of('a', 'b', 'c') == [1, 2, 3]
    assert should_equal
    assert not should_not_equal
    assert not should_different_types_not_equal

# Generated at 2022-06-14 03:18:15.130984
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.empty() == ImmutableList.empty(), 'Two empty Immutables are not equal'
    assert ImmutableList.of(1) == ImmutableList.of(1), 'ImmutableLists with equal head are not equal'
    assert ImmutableList.of(1, 2) == ImmutableList.of(1, 2), 'ImmutableLists with equal head and tail are not equal'
    assert ImmutableList.of(1) == ImmutableList.of(1, 2), 'ImmutableLists with equal head and different tail are equal'
    assert ImmutableList.of(1) != ImmutableList.of(2), 'ImmutableLists with different head are equal'

# Generated at 2022-06-14 03:18:18.588364
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    test_data = ImmutableList(1, ImmutableList(2, ImmutableList(3)), False)

    result = ImmutableList(2, ImmutableList(3), False)

    assert test_data.filter(lambda x: x % 2 == 0) == result



# Generated at 2022-06-14 03:18:28.534961
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList(1) == ImmutableList(1)
    assert ImmutableList(1, ImmutableList(2)) == ImmutableList(1, ImmutableList(2))
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))) == ImmutableList(1, ImmutableList(2, ImmutableList(3)))

    assert ImmutableList(1) != ImmutableList(2)
    assert ImmutableList(1, ImmutableList(2)) != ImmutableList(1, ImmutableList(3))
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))) != ImmutableList(1, ImmutableList(2, ImmutableList(4)))


# Generated at 2022-06-14 03:18:34.827288
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # TODO: create common method for testing all kind of lists
    assert ImmutableList.of('a', 'b', 'c').find(lambda x: x == 'c') == 'c'
    assert ImmutableList.empty().find(lambda x: x == 'c') is None
    assert ImmutableList.of('a').find(lambda x: x == 'c') is None
    assert ImmutableList.of('a', 'b', 'c').find(lambda x: x == 'd') is None
    assert ImmutableList.of('a', 'b', 'c').find(lambda x: x == 'a') == 'a'
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 2) == 2
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 3)

# Generated at 2022-06-14 03:18:39.631773
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    l = ImmutableList.of(1, 2, 3)
    assert l.filter(lambda x: x == 2) == ImmutableList.of(2)
    assert l.filter(lambda x: x > 2) == ImmutableList.of(3)

    assert l.filter(lambda x: x == '21') == ImmutableList()



# Generated at 2022-06-14 03:18:50.861633
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList() == ImmutableList.empty()
    assert ImmutableList(1) == ImmutableList(1)
    assert ImmutableList(1, ImmutableList(2), is_empty=False) == ImmutableList(1, ImmutableList(2), is_empty=False)
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3)), is_empty=False) \
        == ImmutableList(1, ImmutableList(2, ImmutableList(3)), is_empty=False)


# Generated at 2022-06-14 03:19:04.486941
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # given:
    list_ = ImmutableList.of(1, 2, 3)

    # when:
    result_one = list_.find(lambda x: x == 2)
    result_two = list_.find(lambda x: x == 5)

    # then:
    assert result_one == 2
    assert result_two is None


# Generated at 2022-06-14 03:19:08.285348
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(4, 2, 3, 2, 1, 2, 5).filter(lambda x: x > 3 ) == ImmutableList.of(4, 5)

test_ImmutableList_filter()

# Generated at 2022-06-14 03:19:19.466482
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.of(1, 2, 3) == ImmutableList.of(1, 2, 3)
    assert ImmutableList.empty() == ImmutableList.empty()



# Generated at 2022-06-14 03:19:32.047610
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.of(1, 2) == ImmutableList.of(1, 2)
    assert ImmutableList.of(1, 2) != ImmutableList.of(1, 2, 3)
    assert ImmutableList.of(1, 2) != (1, 2)

# Generated at 2022-06-14 03:19:42.863232
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    first_list = ImmutableList.of('a', 'b', 'c')
    second_list = ImmutableList.of('a', 'b', 'c')
    third_list = ImmutableList.of('a', 'b')

    are_equals = first_list == second_list
    are_equals = are_equals and first_list != third_list

    print('Test method __eq__ of class ImmutableList: {}'.format(
        'OK' if are_equals else 'FAIL'
    ))


# Generated at 2022-06-14 03:19:57.118815
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList() == ImmutableList()

    assert ImmutableList.of(1, 2, 3) == ImmutableList.of(1, 2, 3)

    assert ImmutableList() != ImmutableList.of(1, 2, 3)
    assert ImmutableList.of(1, 2, 3) != ImmutableList()


# Generated at 2022-06-14 03:20:07.276150
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList(1, ImmutableList(2), ImmutableList(3)).find(lambda a: a == 1) == 1
    assert ImmutableList(1, ImmutableList(2), ImmutableList(3)).find(lambda a: a == 2) == 2
    assert ImmutableList(1, ImmutableList(2), ImmutableList(3)).find(lambda a: a == 3) == 3
    assert ImmutableList(1, ImmutableList(2), ImmutableList(3)).find(lambda a: a == 4) is None
    assert ImmutableList(1, ImmutableList(2), ImmutableList(3)).find(lambda a: a == 5) is None
    assert ImmutableList(1, ImmutableList(2), ImmutableList(3)).find(lambda a: a == 6) is None

    
# Run all unit tests

# Generated at 2022-06-14 03:20:10.407359
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    input_value = ImmutableList.of(1, 2, 3)
    expected_output = ImmutableList.of(1, 2, 3) == ImmutableList.of(1, 2, 3)

    assert expected_output == True


# Generated at 2022-06-14 03:20:22.320502
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    empty_list_1 = ImmutableList(is_empty=True)
    empty_list_2 = ImmutableList(is_empty=True)
    empty_list_3 = ImmutableList.empty()
    assert empty_list_1 == empty_list_2
    assert empty_list_1 == empty_list_3
    assert empty_list_2 == empty_list_3

    list_1 = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    list_2 = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    list_3 = ImmutableList.of(1, 2, 3)
    list_4 = ImmutableList.of(1, 2, 3, 4)
    assert list_1 == list_2
    assert list_1 == list_3
   

# Generated at 2022-06-14 03:20:26.903855
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # Arrange
    to_filter = ImmutableList.of(1)
    expected_filtered = ImmutableList.of(2)

    # Act
    actual_filtered = to_filter.filter(
        lambda x: x == 2
    )

    # Assert
    assert expected_filtered == actual_filtered



# Generated at 2022-06-14 03:20:31.457929
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # Arrange
    il = ImmutableList.of(1, 2, 3, 4, 5)

    # Act
    result = il.filter(lambda el: el > 3)

    # Assert
    assert result == [4, 5], 'test_ImmutableList_filter, result = {}'.format(result)


test_ImmutableList_filter()

# Generated at 2022-06-14 03:20:38.362732
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.empty() == ImmutableList.empty()
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))) == ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))) != ImmutableList(1, ImmutableList(2, ImmutableList(3, 4)))
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))) != ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList.empty())))

    assert ImmutableList.empty() == ImmutableList(is_empty=True)
    assert ImmutableList.empty() != ImmutableList(is_empty=False)
    assert ImmutableList(is_empty=True) != Imm

# Generated at 2022-06-14 03:20:41.675772
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    head = 'first'
    tail = ImmutableList('second', ImmutableList('third', is_empty=True))

    case1 = ImmutableList(head, tail)
    case2 = ImmutableList(head=None)
    case3 = ImmutableList(head, ImmutableList(head=None))

    assert case1.find(lambda x: x == 'third') == 'third'
    assert case2.find(lambda x: x == 'third') is None
    assert case3.find(lambda x: x == 'third') is None

# Generated at 2022-06-14 03:21:06.891775
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    from unittest import TestCase, main

    def is_even(x: int) -> bool:
        return x % 2 == 0

    def is_even_or_bigger_than_five(x: int) -> bool:
        return is_even(x) or x >= 5

    class ImmutableListTest(TestCase):
        def test_filter_returns_new_instance_of_ImmutableList(self):
            list_one = ImmutableList.of(1, 2, 3)
            list_two = ImmutableList.of(3, 4, 5)
            self.assertIsNot(list_one.filter(is_even), list_two)


# Generated at 2022-06-14 03:21:11.255502
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert(ImmutableList(1).filter(lambda x: x == 3) == ImmutableList())
    assert(ImmutableList(3).filter(lambda x: x == 3) == ImmutableList(3))
    assert(ImmutableList.of(1, 2, 3, 4, 5).filter(lambda x: x%2 == 0) == ImmutableList.of(2, 4))
test_ImmutableList_filter()

# Generated at 2022-06-14 03:21:14.645607
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list = ImmutableList.of(1, 2, 3, 4, 5)
    result = list.filter(lambda x: x % 2 == 0)
    assert result == ImmutableList.of(2, 4)


# Generated at 2022-06-14 03:21:16.956567
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.of(10).__eq__(ImmutableList(10)) is True
    assert ImmutableList.of(10).__eq__(ImmutableList(11)) is False



# Generated at 2022-06-14 03:21:19.085051
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.empty() == ImmutableList(is_empty=True)
    assert ImmutableList(1, 2, 3) == ImmutableList(1, 2, 3)


# Generated at 2022-06-14 03:21:25.632894
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    fn = lambda x: x == 'Test'

    list = ImmutableList.of('Test', 'Test1', 'Test1Test', 'Test2', 'Test3Test')
    # list = ImmutableList()
    # list = ImmutableList('Test')
    # list = ImmutableList('Test', 'Test1')
    # list = ImmutableList('Test', 'Test1', 'Test1Test')
    # list = ImmutableList('Test', 'Test1', 'Test1Test', 'Test2')

    assert list.find(fn) == 'Test'


# Generated at 2022-06-14 03:21:31.237429
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    # given
    list_1 = ImmutableList(1)
    list_2 = ImmutableList(1)
    list_3 = ImmutableList(1, ImmutableList.of(2))
    list_4 = ImmutableList(1, ImmutableList.of(2))

    # then
    assert list_1 == list_2
    assert list_3 == list_4



# Generated at 2022-06-14 03:21:41.429023
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    now_empty_list = ImmutableList()
    list_one_element = ImmutableList.of(1)
    list_twelve_elements = ImmutableList.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
    list_six_elements = ImmutableList.of(1, 2, 3, 4, 5, 6)

    assert now_empty_list == ImmutableList(is_empty=True)
    assert now_empty_list != list_one_element
    assert list_one_element == ImmutableList.of(1)
    assert list_one_element != list_six_elements
    assert list_six_elements == ImmutableList.of(1, 2, 3, 4, 5, 6)
    assert list_six_elements != list_

# Generated at 2022-06-14 03:21:47.067221
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    lst = ImmutableList.of(123)
    assert lst.find(lambda x: True) == 123
    assert lst.find(lambda x: False) is None

    lst = ImmutableList.of(123, 345, False)
    assert lst.find(lambda x: x == False) == False
    assert lst.find(lambda x: x == 'test') is None

    lst = ImmutableList.of(123, 345, False, 'test', 'test')
    assert lst.find(lambda x: x == 'test') == 'test'



# Generated at 2022-06-14 03:21:58.575082
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x % 2 == 0) == ImmutableList.of(2)
    assert ImmutableList.of(*[0, 1, 1, 2, 3, 5, 8]).filter(lambda x: x != 1) == ImmutableList.of(*[0, 2, 3, 5, 8])
    assert ImmutableList.of(*[-1, -2, -3, -4, -5]).filter(lambda x: x < 0) == ImmutableList.of(*[-1, -2, -3, -4, -5])
    assert ImmutableList.of(*[1,2,3,4,5,6,8]).filter(lambda x: x == 5) == ImmutableList.of(5)

# Generated at 2022-06-14 03:22:39.282309
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    case_1_l_1 = ImmutableList.of(1, 2, 3)
    case_1_l_2 = ImmutableList.of(1, 2, 3)
    case_1_expect = True

    case_2_l_1 = ImmutableList.of(1, 2, 3)
    case_2_l_2 = ImmutableList.of(1, 2, 3, 4)
    case_2_expect = False

    case_3_l_1 = ImmutableList.of(1, 2, 3)
    case_3_l_2 = ImmutableList.of(1, 2, 4)
    case_3_expect = False

    case_4_l_1 = ImmutableList.of(1, 2, 3)

# Generated at 2022-06-14 03:22:44.668755
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # Given
    input_list = ImmutableList.of(1, 2, 3, 4, 5, 6)
    expected_list = ImmutableList.of(2, 4, 6)

    # When
    actual_list = input_list.filter(lambda x: x % 2 == 0)

    # Then
    assert actual_list == expected_list



# Generated at 2022-06-14 03:22:51.410679
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.of(1, 2, 3) == ImmutableList.of(1, 2, 3)
    assert ImmutableList.of(1, 2, 3) != ImmutableList.of(1, 2, 4)
    assert ImmutableList.of(1, 2, 3) != ImmutableList.of(2, 3)
    assert ImmutableList.of(1, 2, 3) != ImmutableList.of(1, 2, 3, 4)


# Generated at 2022-06-14 03:23:00.815621
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    _assert = Assert('ImmutableList___eq__')
    my_list = ImmutableList(1, ImmutableList(2))

# Generated at 2022-06-14 03:23:06.304598
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    # Arrange
    l = ImmutableList.of(1, 2, 3, 4)

    # Act
    equal = l == ImmutableList.of(1, 2, 3, 4)

    # Assert
    assert equal

# Generated at 2022-06-14 03:23:24.932493
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    test_cases = [
        (
            ImmutableList(1, ImmutableList(2, ImmutableList(3))),
            ImmutableList(1, ImmutableList(2, ImmutableList(3))),
            True
        ),
        (
            ImmutableList(1, ImmutableList(2, ImmutableList(3))),
            ImmutableList(1, ImmutableList(2)),
            False
        )
    ]

    for list1, list2, expected in test_cases:
        assert list1 == list2 is expected


# Generated at 2022-06-14 03:23:36.186880
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    list1 = ImmutableList.of(1, 2, 3)
    list2 = ImmutableList.of(1, 2, 3)

    assert list1 == list2

# Generated at 2022-06-14 03:23:42.896200
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.of(1, 2, 3) == ImmutableList.of(1, 2, 3)
    assert ImmutableList.of(1, 2) != ImmutableList.empty()
    assert ImmutableList.of(1, 2, 3) != ImmutableList.of('a', 'b')



# Generated at 2022-06-14 03:23:58.777979
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.empty() == ImmutableList.empty()
    assert ImmutableList.of(1) == ImmutableList.of(1)
    assert ImmutableList.of(1, 2, 3, 5) == ImmutableList.of(1, 2, 3, 5)
    assert ImmutableList.of(2, 3) != ImmutableList.of(1, 2, 3, 5)



# Generated at 2022-06-14 03:24:06.326709
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.empty() == ImmutableList.empty()
    assert ImmutableList.of(1) == ImmutableList.of(1)
    assert ImmutableList.of(1, 2) == ImmutableList.of(1, 2)
    assert ImmutableList.of(1, 2, 3) == ImmutableList.of(1, 2, 3)
    assert ImmutableList.of(1, 2, 3) != ImmutableList.of(1, 2)
    assert ImmutableList.of(1, 2, 3) != ImmutableList.of(1, 3)
    assert ImmutableList.of(1, 2, 3) != ImmutableList.of(3, 2, 1)
    assert ImmutableList.of(1, 2, 3) != ImmutableList.of(2, 3)


# Generated at 2022-06-14 03:24:59.840629
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(2, 3, 4).find(lambda x: x > 2) == 3


# Generated at 2022-06-14 03:25:06.190935
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList() == ImmutableList()
    assert ImmutableList(1) == ImmutableList(1)
    assert ImmutableList(1, ImmutableList(2)) == ImmutableList(1, ImmutableList(2))
    assert ImmutableList(1) != ImmutableList()
    assert ImmutableList(1) != '1'
    assert ImmutableList(1) != ImmutableList(1, ImmutableList(2))


# Generated at 2022-06-14 03:25:10.935339
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    # Test number 1
    a = ImmutableList(1, ImmutableList(2))
    b = ImmutableList(1, ImmutableList(2))
    assert a == b
    # Test number 2
    a = ImmutableList(1, ImmutableList(2), ImmutableList(3))
    b = ImmutableList(1, ImmutableList(2))
    assert a != b



# Generated at 2022-06-14 03:25:19.303061
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList() == ImmutableList()
    assert ImmutableList(1, ImmutableList()) == ImmutableList(1)
    assert ImmutableList(None) == ImmutableList(None)
    assert ImmutableList() != None
    assert ImmutableList() != 'ImmutableList()'
    assert ImmutableList() != ImmutableList(1)


# Generated at 2022-06-14 03:25:33.956119
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    from functools import partial

    # input
    d1 = ImmutableList.of(1, 2, 3)

    # expected output
    d2 = ImmutableList.of(1, 3)

    # testing
    assert d1.filter(partial(lambda expected_value, value: expected_value == value, 1)) == d2



# Generated at 2022-06-14 03:25:41.231147
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.of(1) == ImmutableList.of(1), "One element test"
    assert ImmutableList.of(1, 2) == ImmutableList.of(1, 2), "Two elements test"
    assert ImmutableList.of(1, 2) == ImmutableList.of(1, 2), "Three elements test"
    assert ImmutableList.of(1, 2, 3) != ImmutableList.of(1, 2), "Compare lenghts"
    assert ImmutableList.of(1, 2, 3) != ImmutableList.of(1, 2, 4), "Compare values"



# Generated at 2022-06-14 03:25:46.321907
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))) == ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))) is not ImmutableList(1, ImmutableList(2, ImmutableList(3, 4)))


# Generated at 2022-06-14 03:25:54.384298
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    first_list = ImmutableList.of(1,2,3)
    second_list = ImmutableList.of(1,2,3)
    third_list = ImmutableList.of(3,2,1)
    assert first_list == second_list
    assert not first_list == third_list


# Generated at 2022-06-14 03:26:00.016262
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # Given
    element1 = ImmutableList.of(1, 2, 3)
    element2 = ImmutableList.of(2, 3, 4)

    # When
    result1 = element1.find(lambda x: x == 5)
    result2 = element2.find(lambda x: x == 4)

    # Then
    assert result1 is None
    assert result2 == 4
test_ImmutableList_find()

# Generated at 2022-06-14 03:26:01.890297
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.of(1, 2, 3) == ImmutableList.of(1, 2, 3)

