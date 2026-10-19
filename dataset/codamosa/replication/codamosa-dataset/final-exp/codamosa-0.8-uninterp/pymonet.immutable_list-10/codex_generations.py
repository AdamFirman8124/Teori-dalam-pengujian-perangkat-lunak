

# Generated at 2022-06-14 03:16:54.547481
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda x: x%2 == 0) == ImmutableList.of(2, 4)


# Generated at 2022-06-14 03:17:04.082895
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter(): # pragma: no cover
    assert(
        ImmutableList([
            ImmutableList(1).filter(lambda x: x > 1), 
            ImmutableList().filter(lambda x: x > 1),
            ImmutableList(1, 2, 3).filter(lambda x: x > 1)
        ]) ==
        ImmutableList([
            ImmutableList(is_empty=True),
            ImmutableList(is_empty=True),
            ImmutableList(2, 3)
        ])
    )


# Generated at 2022-06-14 03:17:12.575263
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():

    assert ImmutableList.of(1).find(lambda x: x == 2) is None
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 2) == 2
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == "foo") is None


# Generated at 2022-06-14 03:17:23.132207
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # given
    immutable_list = ImmutableList.of(1, 2, 3, 4, 5)

    # when
    result = immutable_list.filter(lambda x: x > 2)

    # then
    assert result == ImmutableList.of(3, 4, 5)



# Generated at 2022-06-14 03:17:33.572527
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    def is_odd(num: int) -> bool:
        return bool(num % 2)

    assert ImmutableList.empty().filter(is_odd).to_list() == []
    assert ImmutableList.of(1).filter(is_odd).to_list() == [1]
    assert ImmutableList.of(1, 2, 3).filter(is_odd).to_list() == [1, 3]
    assert ImmutableList.of(1, 2, 3, 4).filter(is_odd).to_list() == [1, 3]

# Generated at 2022-06-14 03:17:44.914207
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    class A:
        def __init__(self, a):
            self.a = a

        def __eq__(self, other):
            return self.a == other.a

    class B:
        def __init__(self, b):
            self.b = b

        def __eq__(self, other):
            return self.b == other.b

    assert ImmutableList.of(A(1)) == ImmutableList.of(A(1))
    assert ImmutableList.of(A(1), A(2)) == ImmutableList.of(A(1), A(2))
    assert ImmutableList.of(A(1), A(2), B(3)) == ImmutableList.of(A(1), A(2), B(3))

# Generated at 2022-06-14 03:17:50.681758
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x % 2 == 0) == 2
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x > 10) is None


# Generated at 2022-06-14 03:17:57.118596
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    # Test for equality
    assert ImmutableList(1) == ImmutableList(1)
    assert ImmutableList(1, ImmutableList(2)) == ImmutableList(1, ImmutableList(2))
    assert ImmutableList(1) == ImmutableList(1, ImmutableList.empty())
    assert ImmutableList(1, ImmutableList.empty()) == ImmutableList(1)
    assert ImmutableList(1, ImmutableList(2)) == ImmutableList(1, ImmutableList(2, ImmutableList.empty()))
    assert ImmutableList(1, ImmutableList(2, ImmutableList.empty())) == ImmutableList(1, ImmutableList(2))

# Generated at 2022-06-14 03:18:10.352160
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList(1) == ImmutableList(1)
    assert ImmutableList(1, ImmutableList(2)) == ImmutableList(1, ImmutableList(2))
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))) != ImmutableList(1, ImmutableList(2))
    assert ImmutableList(1, ImmutableList(3)) != ImmutableList(1, ImmutableList(2))
    assert ImmutableList(1, ImmutableList(3, ImmutableList(4))) != ImmutableList(1, ImmutableList(2))
    assert ImmutableList(1, ImmutableList(2, ImmutableList(4))) != ImmutableList(1, ImmutableList(2, ImmutableList(3)))

# Generated at 2022-06-14 03:18:18.102664
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList(1).find(lambda x: x > 1) is None
    assert ImmutableList(1, ImmutableList(2)).find(lambda x: x > 1) == 2
    assert ImmutableList(1).find(lambda x: x > 0) == 1
    assert ImmutableList(1, ImmutableList(2)).find(lambda x: x > 0) == 1
    assert ImmutableList(1, ImmutableList(2), ImmutableList(3)).find(lambda x: x > 2) == 3


# Generated at 2022-06-14 03:18:30.149112
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.of(1, 2) == ImmutableList.of(1, 2)
    assert ImmutableList.empty() == ImmutableList.empty()
    assert ImmutableList.of(1) != ImmutableList.of(1, 2)
    assert ImmutableList.of(1) != ImmutableList.empty()

# Generated at 2022-06-14 03:18:42.117348
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    x = ImmutableList.of(1,2,3)
    y = ImmutableList.of(1,2,3)
    z = x
    assert (x == y) == False, "ImmutableList__eq__: test 1 failed"
    assert (x == z) == True, "ImmutableList__eq__: test 2 failed"
    assert (x == 1) == False, "ImmutableList__eq__: test 3 failed"
    assert (x == ImmutableList.of(1,2,3)) == True , "ImmutableList__eq__: test 4 failed"
    assert (x == ImmutableList.of(1,2)) == False , "ImmutableList__eq__: test 5 failed"
    print("All test passed!")
test_ImmutableList___eq__()


# Generated at 2022-06-14 03:18:50.964282
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    """
    Method for testing filter method of class ImmutableList
    """
    lst = ImmutableList.of(1, 2, 3, 4, 5)
    true_result = ImmutableList.of(2, 4)

    def is_even(x: int) -> bool:
        return True if x % 2 == 0 else False
    
    assert lst.filter(is_even) == true_result


# Generated at 2022-06-14 03:18:58.881572
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    empty_list = ImmutableList.empty()
    assert empty_list.filter(lambda x: x > 0) == ImmutableList.empty()

    single_elem_list = ImmutableList.of(1)
    assert single_elem_list.filter(lambda x: x > 0) == single_elem_list
    assert single_elem_list.filter(lambda x: x < 0) == ImmutableList.empty()

    even_number_list = ImmutableList.of(2, 4, 6, 8)
    odd_number_list = ImmutableList.of(1, 3, 5, 7)
    assert even_number_list.filter(lambda x: x % 2 == 0) == even_number_list
    assert even_number_list.filter(lambda x: x % 2 == 1) == ImmutableList.empty

# Generated at 2022-06-14 03:19:03.070272
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.of(3, 2, 1) == ImmutableList.of(3, 2, 1)
    assert ImmutableList.of() == ImmutableList.of()
    assert ImmutableList.empty() == ImmutableList.empty() is True
    assert ImmutableList.empty() == ImmutableList.of(3) is False

# Generated at 2022-06-14 03:19:14.178354
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    # case0:
    l1 = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    l2 = ImmutableList(1, ImmutableList(2, ImmutableList(3)))

    assert l1 == l2

    # case1:
    l1 = ImmutableList(1, ImmutableList(2, None))
    l2 = ImmutableList(1, ImmutableList(2, None))

    assert l1 == l2

    # case2:
    l1 = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    l2 = ImmutableList(1, ImmutableList(2, ImmutableList(2)))

    assert l1 != l2

    # case3:
    l1 = ImmutableList(1, ImmutableList(2, None))
    l

# Generated at 2022-06-14 03:19:16.273549
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 3) == 3
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 100) is None

# Generated at 2022-06-14 03:19:19.279928
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    list_ = ImmutableList.of(1, 2, 3, 4)
    assert list_.find(lambda x: x > 2) == 3
    assert list_.find(lambda x: x < 2) == 1
    assert list_.find(lambda x: x == 5) == None

# Generated at 2022-06-14 03:19:25.851502
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    immutableList = ImmutableList.of(5, 4, 3, 2, 1)
    assert immutableList.find(lambda x: x == 1) == 1
    assert immutableList.find(lambda x: x == 5) == 5
    assert immutableList.find(lambda x: x == 6) is None
    assert immutableList.find(lambda x: x > 3) == 4
    assert immutableList.find(lambda x: x < 4) == 5


# Generated at 2022-06-14 03:19:37.160660
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(
        10, 20, 30, 40, 50
    ).filter(lambda n: n % 10 == 0) == ImmutableList.of(
        10, 20, 30, 40, 50
    )

    assert ImmutableList.of(
        10, 20, 30, 40, 50
    ).filter(lambda _: False) == ImmutableList.empty()

    assert ImmutableList.of(
        10, 20, 30, 40, 50
    ).filter(lambda n: n > 100) == ImmutableList.empty()

    assert ImmutableList.of(
        10, 20, 30, 40, 50
    ).filter(lambda n: n > 30) == ImmutableList.of(
        40, 50
    )

    assert ImmutableList.empty().filter(lambda n: n > 30) == ImmutableList

# Generated at 2022-06-14 03:20:00.918376
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(20).find(lambda x: x == 20) is 20
    assert ImmutableList.of(20).find(lambda x: x == 10) is None
    assert ImmutableList.of(10, 20, 30).find(lambda x: x == 20) is 20
    assert ImmutableList.of(10, 20, 30).find(lambda x: x == 50) is None


# Generated at 2022-06-14 03:20:12.866211
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    m = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    assert m.filter(lambda x: x > 1) == ImmutableList(2, ImmutableList(3))


# Generated at 2022-06-14 03:20:17.470484
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list = ImmutableList.of(1, 2, 3, 4, 5)
    results = list.filter(lambda val: val % 2 == 0)
    assert len(results) == 2
    assert results.head == 2
    assert results.tail.head == 4
    assert results.tail.tail is None


# Generated at 2022-06-14 03:20:22.768673
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    list_1 = ImmutableList.of(1, 2, 3, 4)
    list_2 = ImmutableList.of(1, 2, 3, 4)
    assert list_1 == list_2, "List1 and List2 aren't equal"



# Generated at 2022-06-14 03:20:27.035511
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # given
    list_ = ImmutableList.of(1, 2, 3, 4, 5)

    # when
    filtered_list = list_.filter(lambda x: x % 2 == 0)

    # then
    assert filtered_list.to_list() == [2, 4]




# Generated at 2022-06-14 03:20:34.588334
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.of('a', 'b', 'd') == ImmutableList.of('a', 'b', 'd')
    assert ImmutableList.of(1, 2, 3, 4) == ImmutableList.of(1, 2, 3, 4)
    assert ImmutableList.empty() == ImmutableList.empty()

# Generated at 2022-06-14 03:20:39.653786
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    a = ImmutableList(1, ImmutableList(2, ImmutableList(3, None)))
    b = ImmutableList(1, ImmutableList(2, ImmutableList(3, None)))
    c = ImmutableList()

    assert a == b
    assert a != c

# Generated at 2022-06-14 03:20:48.574621
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.of(1) == ImmutableList.of(1)
    assert ImmutableList.of(1, 2, 3) == ImmutableList.of(1, 2, 3)
    assert ImmutableList.of(1, 2, 3) == ImmutableList.of(1, ImmutableList.of(2, ImmutableList.of(3)))
    assert ImmutableList.of(1, 2, 3) != ImmutableList.of(1, 2, 4)
    assert ImmutableList.of(1, 2, 3) != ImmutableList.of(1, ImmutableList.of(2, 4))



# Generated at 2022-06-14 03:21:00.174080
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.of(1) == ImmutableList.of(1)
    assert ImmutableList.of(1) != ImmutableList.of(2)
    assert ImmutableList.of(1) != ImmutableList.of(1, 2)
    assert ImmutableList.of(1, 2) != ImmutableList.of(1)
    assert ImmutableList.of(1, 2) == ImmutableList.of(1, 2)
    assert ImmutableList.of(1, 2) != ImmutableList.of(1, 2, 3)
    assert ImmutableList.of(1, 2, 3) != ImmutableList.of(1, 2)
    assert ImmutableList.of(1, 2, 3) != ImmutableList.of(2, 3)

# Generated at 2022-06-14 03:21:06.723385
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    list = ImmutableList(
        {'name': 'James'},
        ImmutableList(
            {'name': 'James'},
            ImmutableList(
                {'name': 'James'},
                ImmutableList(
                    {'name': 'James'},
                    ImmutableList({'name': 'James'})
                )
            )
        )
    )

    def fn(x: dict) -> bool:
        return x['name'] == 'James'

    assert list.find(fn) == {'name': 'James'}

# Generated at 2022-06-14 03:21:47.494603
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.of(1, 2, 3) != ImmutableList.of(1, 2)
    assert ImmutableList.of(1, 2, 3) == ImmutableList.of(1, 2, 3)



# Generated at 2022-06-14 03:21:58.700671
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.of(1) == ImmutableList.of(1), \
        'ImmutableList(1) != ImmutableList(1)'
    assert ImmutableList.of(1, 2) != ImmutableList.of(1, 3), \
        'ImmutableList(1, 2) == ImmutableList(1, 3)'
    assert ImmutableList.of(1, 2, 3) != ImmutableList.of(1, 2), \
        'ImmutableList(1, 2, 3) == ImmutableList(1, 2)'
    assert ImmutableList.of(1, 2, 3) != ImmutableList.of(1, 2, 3, 4), \
        'ImmutableList(1, 2, 3) == ImmutableList(1, 2, 3, 4)'
    assert ImmutableList.empty() != Immutable

# Generated at 2022-06-14 03:22:00.365482
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.of(1, 2, 3, 4) == ImmutableList.of(
        1, 2, 3, 4), 'Should be equal'



# Generated at 2022-06-14 03:22:03.988586
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList(1, ImmutableList(2)) == ImmutableList(1, ImmutableList(2))
    assert ImmutableList(1, ImmutableList(2)) != ImmutableList(2, ImmutableList(1))


# Generated at 2022-06-14 03:22:12.350750
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(5, 3, 6, 5, 2, 8).find(lambda x: x > 5) == 6
    assert ImmutableList.of(5, 3, 6, 5, 2, 8).find(lambda x: x == 5) == 5
    assert ImmutableList.of(5, 3, 6, 5, 2, 8).find(lambda x: x > 10) is None
    assert ImmutableList.of(5, 3, 6, 5, 2, 8).find(lambda x: x == 1) is None
    assert ImmutableList.empty().find(lambda x: x == 1) is None


# Generated at 2022-06-14 03:22:15.584088
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    bag = ImmutableList.of(1, 2, 3, 4, 5)
    assert bag.find(lambda x: x > 8) is None
    assert bag.find(lambda x: x < 10) == 1
    assert bag.find(lambda x: x > 2) == 3


# Generated at 2022-06-14 03:22:27.168327
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.empty().filter(lambda v: True) == ImmutableList.empty()

    assert ImmutableList.of(0, 1, 2, 3, 4).filter(lambda v: v > 3).to_list() == [4]
    assert ImmutableList.of(0, 1, 2, 3, 4).filter(
        lambda v: v > 3
    ).filter(
        lambda v: v < 5
    ).to_list() == [4]
    assert ImmutableList.of(0, 1, 2, 3, 4).filter(lambda v: True).to_list() == [0, 1, 2, 3, 4]
    assert ImmutableList.of(0, 1, 2, 3, 4).filter(
        lambda v: True
    ).filter(
        lambda v: v >= 3
    ).to_list

# Generated at 2022-06-14 03:22:32.495662
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    initial_data = [1, 2, 3, 4, 5]
    even_filter = lambda x: x % 2 == 0

    filtered_list = ImmutableList(*initial_data).filter(even_filter)

    assert ImmutableList(2, 4).to_list() == filtered_list.to_list()

# Generated at 2022-06-14 03:22:43.035860
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3).filter(lambda i: i == 1) == ImmutableList.of(1)
    assert ImmutableList.of(1, 2, 3).filter(lambda i: i == 2) == ImmutableList.of(2)
    assert ImmutableList.of(1, 2, 3).filter(lambda i: i == 3) == ImmutableList.of(3)

    assert ImmutableList.of(1, 2, 3).filter(lambda i: i > 1) == ImmutableList.of(2, 3)
    assert ImmutableList.of(1, 2, 3).filter(lambda i: i > 2) == ImmutableList.of(3)
    assert ImmutableList.of(1, 2, 3).filter(lambda i: i > 3) == ImmutableList.empty()




# Generated at 2022-06-14 03:22:53.675544
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.of(1, 2, 3) == ImmutableList.of(1, 2, 3)
    assert ImmutableList.of(1, 2, 3) != ImmutableList.of(1, 2, 4)
    assert ImmutableList.empty() == ImmutableList.empty()
    assert ImmutableList.of(1, 2, 3) != [1, 2, 3]
    assert ImmutableList.empty() != 1
    assert ImmutableList.of(1, 2, 3) != ImmutableList.of(1)
    assert ImmutableList.of(1, 2) != ImmutableList.of(1, 2, 3)
    assert ImmutableList.of(1, 2, 3) != ImmutableList.of(1, 2)
    assert ImmutableList.of(1, 2, 3) is not Imm

# Generated at 2022-06-14 03:24:06.764510
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    """
    Define all unit tests for ImmutableList.__eq__
    """
    assert ImmutableList(is_empty=True) == ImmutableList(is_empty=True)
    assert ImmutableList(1) == ImmutableList(1)
    assert ImmutableList(1, ImmutableList(2)) == ImmutableList(1, ImmutableList(2))
    assert ImmutableList(1, ImmutableList(23, ImmutableList(20, ImmutableList(22)))) == ImmutableList(1, ImmutableList(23, ImmutableList(20, ImmutableList(22))))
    assert ImmutableList() == ImmutableList()
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))) != ImmutableList(1, ImmutableList(2))
    assert ImmutableList(1) != 2
   

# Generated at 2022-06-14 03:24:13.065225
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList('some') == ImmutableList('some')
    assert ImmutableList() == ImmutableList(is_empty=True)
    assert ImmutableList('some') == ImmutableList('some', None)
    assert ImmutableList('some') == ImmutableList('some', None)
    assert ImmutableList('something', 'else', 'maybe') == ImmutableList('something', ImmutableList('else', ImmutableList('maybe')))



# Generated at 2022-06-14 03:24:16.887161
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # Arrange
    list_ = ImmutableList.of(1, 2, 3, 4, 5)
    # Act
    result = list_.find(lambda x: x == 4)
    # Assert
    assert 4 == result
    
    

# Generated at 2022-06-14 03:24:23.241769
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    immutable_list = ImmutableList.of(1, 2, 3, 4, 5)

    assert immutable_list.find(lambda x: x == 3) == 3
    assert immutable_list.find(lambda x: x == 0) == None

    empty_immutable_list = ImmutableList.empty()
    assert empty_immutable_list.find(lambda x: x == 3) == None


# Generated at 2022-06-14 03:24:29.178570
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    print("Test test_ImmutableList___eq__")

    list1 = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    list2 = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    list3 = ImmutableList(1, ImmutableList(2, ImmutableList(4)))

    assert list1 == list2
    assert list2 == list1
    assert list1 != list3

# Generated at 2022-06-14 03:24:33.087033
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # Setup
    list_instance = ImmutableList.of(1, 2, 3, 4)
    expected = ImmutableList.of(2, 4)

    # Exercise
    actual = list_instance.filter(lambda x: x % 2 == 0)

    # Verify
    assert expected == actual

    # Cleanup - none necessary


# Generated at 2022-06-14 03:24:36.388918
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # Given
    my_list = ImmutableList.of(1,2,3,4,5)

    # When
    res = my_list.filter(lambda a: a % 2 == 0)

    # Then
    assert res == ImmutableList.of(2,4)

    # When
    res2 = my_list.filter(lambda a: a % 2 == 1)

    # Then
    assert res2 == ImmutableList.of(1,3,5)


# Generated at 2022-06-14 03:24:42.294879
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():  # pragma: no cover
    list = ImmutableList.of(
        1,
        2,
        3,
        4,
        5
    )
    result = list.filter(lambda x: x % 2 == 0)
    assert result == ImmutableList(
        2,
        ImmutableList(4)
    )


# Generated at 2022-06-14 03:24:49.980760
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 4, 5, 6).find(lambda x: x % 2 == 0) == 2
    assert ImmutableList.of(1, 2, 3, 4, 5, 6).find(lambda x: x % 2 == 1) == 1
    assert ImmutableList.empty().find(lambda x: x % 2 == 0) is None
    assert ImmutableList.empty().find(lambda x: x % 2 == 1) is None
test_ImmutableList_find()


# Generated at 2022-06-14 03:24:53.819777
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 4, 5).find(_ > 3) == 4
    assert ImmutableList.of(1, 2, 3, 4, 5).find(_ > 5) is None
