

# Generated at 2022-06-14 03:16:54.646814
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.empty() != ImmutableList(1)
    assert ImmutableList(1) != ImmutableList.empty()
    assert ImmutableList(1) != ImmutableList(2)
    assert ImmutableList(1, ImmutableList(2)) == ImmutableList(1, ImmutableList(2))
    assert ImmutableList(1, ImmutableList(2)) != ImmutableList(1, ImmutableList(3))

# Generated at 2022-06-14 03:17:03.195787
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # find method should return first element of ImmutableList that passed
    # info argument returns True

    # assert that method ImmutableList.find() returns value with
    # passed to argument function
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x % 2 == 0) == 2

    # assert that method ImmutableList.find() returns first element
    # of ImmutableList that passed info argument returns True
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x % 2 == 0) == 2

    # assert that method ImmutableList.find() returns None
    # if ImmutableList is empty
    assert ImmutableList.empty().find(lambda x: x % 2 == 0) is None


# Generated at 2022-06-14 03:17:09.096051
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList(1, ImmutableList(1, ImmutableList(1))) \
        == ImmutableList(1, ImmutableList(1, ImmutableList(1)))
    assert ImmutableList(1, ImmutableList(1)) \
        != ImmutableList(1, ImmutableList(1, ImmutableList(1)))
    assert ImmutableList() \
        != ImmutableList(1, ImmutableList(1, ImmutableList(1)))
    assert ImmutableList() == ImmutableList(is_empty=True)
    assert ImmutableList() != ImmutableList()



# Generated at 2022-06-14 03:17:23.665815
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    # Given any ImmutableList[T] A
    list_A = ImmutableList.of(1, 2, 3, 4, 5, 6, 7)
    # And ImmutableList[T] B
    list_B = ImmutableList.of(1, 2, 3, 4, 5, 6, 7)
    # and ImmutableList[T] C
    list_C = ImmutableList.of(1, 2, 3, 4, 6, 7)
    # Then A == A
    assert list_A == list_A
    # and A == B
    assert list_A == list_B
    # but A != C
    assert list_A != list_C


# Generated at 2022-06-14 03:17:35.175553
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # GIVEN
    # GIVEN elements
    array = range(100)

    # GIVEN mapper function
    def filter_fn(i):
        return (i % 2) == 0

    # GIVEN empty ImmutableList
    empty_immutable_list = ImmutableList.empty()

    # GIVEN ImmutableList from array
    immutable_list = ImmutableList.of(*array)

    # WHEN
    # WHEN filtering empty list
    immutable_list_result = empty_immutable_list.filter(filter_fn)

    # WHEN filtering list with all elements passed
    immutable_list_result_2 = immutable_list.filter(filter_fn)

    # WHEN filtering list with some elements passed
    immutable_list_result_3 = immutable_list.filter(filter_fn)

    # THEN
    assert immutable_

# Generated at 2022-06-14 03:17:39.875506
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.of(1, 2, 3) == ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    assert ImmutableList.empty() == ImmutableList(is_empty=True)

    assert not ImmutableList.empty() == ImmutableList.of(1)
    assert not ImmutableList.of(1, 2, 3) == ImmutableList.of(1, 2)



# Generated at 2022-06-14 03:17:43.929580
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    array = ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4)), False), False)
    array_filtered = array.filter(lambda x: x > 2)
    assert array_filtered == ImmutableList(3, ImmutableList(4), False)


# Generated at 2022-06-14 03:17:53.739080
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # test for empty ImmutableList
    assert ImmutableList() == ImmutableList().filter(lambda x: True)

    assert ImmutableList() == ImmutableList(1).filter(lambda x: False)

    # test for one element ImmutableList
    assert ImmutableList() == ImmutableList(1).filter(lambda x: False)
    assert ImmutableList(1) == ImmutableList(1).filter(lambda x: True)

    # test for ImmutableList with more than one element
    assert ImmutableList(1, 2, 3) == ImmutableList(1, 2, 3).filter(lambda x: True)
    assert ImmutableList() == ImmutableList(1, 2, 3).filter(lambda x: False)

# Generated at 2022-06-14 03:18:04.221005
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList() == ImmutableList()
    assert ImmutableList(1) == ImmutableList(1)
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))) == ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    assert ImmutableList(1) == ImmutableList(2) == False
    assert ImmutableList(1) == ImmutableList(2, ImmutableList(3)) == False
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))) == ImmutableList(1, ImmutableList(2)) == False



# Generated at 2022-06-14 03:18:15.600856
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.of().__eq__(ImmutableList.of()) == True
    assert ImmutableList.of(1).__eq__(ImmutableList.of(1)) == True
    assert ImmutableList.of(1, 2, 3).__eq__(ImmutableList.of(1, 2, 3)) == True
    assert ImmutableList.of(1, 2, 3).__eq__(ImmutableList.of(3, 2, 1)) == False
    assert ImmutableList.of(1, 2, 3).__eq__(ImmutableList.of(1, 2, 3, 4)) == False
    assert ImmutableList.of(1, 2, 3).__eq__(ImmutableList.of(1)) == False

# Generated at 2022-06-14 03:18:28.955834
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    def fn(v):
        return v > 2
    assert ImmutableList.of(1, 2) == ImmutableList.of(1, 2).filter(fn)
    assert ImmutableList.of(3, 2) == ImmutableList.of(3, 2).filter(fn)
    assert ImmutableList.of(3, 4) == ImmutableList.of(3, 4).filter(fn)
    assert ImmutableList.empty() == ImmutableList.empty().filter(fn)
    assert ImmutableList.of(3, 4, 2) == ImmutableList.of(2, 3, 4).filter(fn)


# Generated at 2022-06-14 03:18:34.113373
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # SHOULD WORK:
    my_bad_list = ImmutableList.of(1, 2, 3, 4, 5, 6, 7)
    even_numbers = my_bad_list.filter(lambda num: num % 2 == 0)
    assert even_numbers.to_list() == [2, 4, 6]

    my_bad_list = ImmutableList.of('a', 'as', 'b', 'ba')
    two_letter_string_list = my_bad_list.filter(lambda string: len(string) == 2)
    assert two_letter_string_list.to_list() == ['as', 'ba']


# Generated at 2022-06-14 03:18:39.773180
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    list1 = ImmutableList.of(1, 2, 3)
    list2 = ImmutableList.of(1, 2, 3)
    list3 = ImmutableList.of(1, 2, 3, 4)
    list4 = ImmutableList.of(1, 2, 4)

    assert list1 == list2
    assert list1 != list3
    assert list1 != list4


# Generated at 2022-06-14 03:18:49.408143
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1).find(lambda x: x == 1) == 1

    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 2) == 2
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 3) == 3
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 4) is None

    assert ImmutableList.of(2, 3, 4).find(lambda x: x > 2) == 3
    assert ImmutableList.of(2, 3, 4).find(lambda x: x > 100) is None

    assert ImmutableList.of('a', 'b', 'c').find(lambda x: x == 'b') == 'b'

# Generated at 2022-06-14 03:19:05.993632
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.of(1) == ImmutableList.of(1)
    assert ImmutableList.of(1) == ImmutableList.of(1, 2)
    assert ImmutableList.of(1) == ImmutableList.of(2, 3)
    assert ImmutableList.of(1) != ImmutableList.of(2, 3)
    assert not ImmutableList.of(1) != ImmutableList.of(1)
    assert not ImmutableList.of(1) != ImmutableList.of(1, 2)

# Generated at 2022-06-14 03:19:18.552880
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():

    # Setup
    List = ImmutableList
    list_ = List.of(1, 2, 3, 4)

    def get_condition(value):
        return value % 2 == 0

    # Exercise
    result = list_.filter(get_condition)

    # Verify
    assert result.to_list() == [2, 4]



# Generated at 2022-06-14 03:19:25.301896
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList().filter(lambda x: True) == ImmutableList.empty()
    assert ImmutableList(8).filter(lambda x: True) == ImmutableList.of(8)
    assert ImmutableList.of(2, 4, 5, 8).filter(lambda x: x > 3) == ImmutableList.of(4, 5, 8)

# Generated at 2022-06-14 03:19:40.687864
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    a = ImmutableList.of(1, 2, 3)
    b = ImmutableList.of(3, 2, 1)
    c = ImmutableList.of(1, 2, 3, None)
    d = ImmutableList.of(1, 2)

    assert a == b
    assert a == c
    assert a != d
    assert a == ImmutableList.empty()

# Generated at 2022-06-14 03:19:48.482745
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list_of_numbers = ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4, ImmutableList(5)))))
    even_nummber_filter = lambda x: x % 2 == 0
    filtered_list = list_of_numbers.filter(even_nummber_filter)
    assert filtered_list.to_list() == [2, 4], 'Test for ImmutableList filter method failed'

test_ImmutableList_filter()

# Generated at 2022-06-14 03:19:49.824848
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert(ImmutableList(3) == ImmutableList(3))

# Generated at 2022-06-14 03:20:00.494797
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    immutable_list = ImmutableList.of(1)
    assert immutable_list.filter(lambda x: x > 0).to_list() == [1]
    assert immutable_list.filter(lambda x: x < 0).to_list() == []

# Generated at 2022-06-14 03:20:17.438010
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.empty().filter(None) == ImmutableList.empty()
    assert ImmutableList.of(3, 1, 2, 3).filter(lambda x: x > 1) == ImmutableList.of(3, 2, 3)
    assert ImmutableList.of(3, 1, 2, 3).filter((lambda x: x > 1).__ne__) == ImmutableList.of(1)
test_ImmutableList_filter()

# Generated at 2022-06-14 03:20:25.761753
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    _ImmutableList = ImmutableList.of(1, 2, 3, 4, 5)
    _ImmutableList_empty = ImmutableList.empty()

    assert _ImmutableList.filter(lambda x: x % 2 == 0) == ImmutableList.of(2, 4)
    assert _ImmutableList_empty.filter(lambda x: True) == ImmutableList.empty()
    assert _ImmutableList_empty.filter(lambda x: False) == ImmutableList.empty()


# Generated at 2022-06-14 03:20:36.522427
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x > 1) == ImmutableList.of(2, 3)
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x < 1) == ImmutableList.of()
    assert ImmutableList.of().filter(lambda x: x > 0) == ImmutableList.of()


# Unit tests for method find of class ImmutableList

# Generated at 2022-06-14 03:20:40.254342
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    list1 = ImmutableList(1)

    assert list1 == ImmutableList(1)
    assert list1 == ImmutableList() + ImmutableList(1)
    assert list1 != ImmutableList()
    assert list1 != ImmutableList(1) + ImmutableList.of(2)
    assert list1 != ImmutableList(1, None, False)
    assert list1 != ImmutableList(2)
    assert list1 != object()


# Generated at 2022-06-14 03:20:45.559270
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # test with empty list
    assert ImmutableList().filter(lambda x: x % 2 == 0).is_empty
    # test with non-empty list
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x % 2 == 0) == ImmutableList.of(2)



# Generated at 2022-06-14 03:20:54.527051
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))) == ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))) == ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4)))) != ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4), ImmutableList(5))))



# Generated at 2022-06-14 03:20:57.279838
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x > 1) == ImmutableList.of(2, 3)



# Generated at 2022-06-14 03:21:06.818305
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 1) == 1
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 3) == 3
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 5) == 5
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 100) is None
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 0) is None
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: True) == 1

# Generated at 2022-06-14 03:21:13.902818
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.empty() == ImmutableList.empty()

    assert ImmutableList.of(1) == ImmutableList(1)

    assert ImmutableList.of(1, 2) == ImmutableList(1, ImmutableList(2))

    assert ImmutableList.of(1, 2, 3) == ImmutableList(1, ImmutableList(2, ImmutableList(3)))

    assert ImmutableList.of(1, 2) != ImmutableList(1)
    assert ImmutableList.of(1, 2) != ImmutableList(2, ImmutableList(1))
    assert ImmutableList.of(1, 2) != ImmutableList(1, ImmutableList(2, ImmutableList(3)))



# Generated at 2022-06-14 03:21:32.169148
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    list_empty = ImmutableList()
    assert list_empty.find(lambda x: True) == None
    assert list_empty.find(lambda x: False) == None

    list_single = ImmutableList(1)
    assert list_single.find(lambda x: x == 2) == None
    assert list_single.find(lambda x: x == 1) == 1

    list_multi = ImmutableList(1, ImmutableList(2, ImmutableList(3)), ImmutableList(4))
    assert list_multi.find(lambda x: x == 2) == 2
    assert list_multi.find(lambda x: x == 5) == None

    print('Test for method find finished successfully')

# Generated at 2022-06-14 03:21:37.373526
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    items = ImmutableList.of(1, 2, 3, 4, 5, 6)
    assert items.to_list() == [1, 2, 3, 4, 5, 6]

    new_items = items.filter(lambda x: x % 2 == 0)
    assert new_items.to_list() == [2, 4, 6]

    new_items = items.filter(lambda x: x % 2 != 0)
    assert new_items.to_list() == [1, 3, 5]
# Unit tests for method reduce of class ImmutableList

# Generated at 2022-06-14 03:21:44.172107
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3).find(lambda value: value == 2) == 2
    assert ImmutableList.of(
        ImmutableList.of(1, 2, 3),
        ImmutableList.of(1, 2, 3),
        ImmutableList.of(5, 6, 7)
    ).find(lambda value: value.head == 5).head == 5
    assert ImmutableList.empty().find(lambda value: value.head == 5) == None



# Generated at 2022-06-14 03:21:51.377317
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    l1 = ImmutableList(1, 2, 3)
    l2 = ImmutableList(1, 2, 3)
    assert l1 == l2
    
    l1 = ImmutableList()
    l2 = ImmutableList()
    assert l1 == l2
    
    l1 = ImmutableList(5, 6, 7)
    l2 = ImmutableList(5, 6, 7)
    assert l1 == l2
    
    l1 = ImmutableList(5, 6, 7)
    l2 = ImmutableList(5, '6', 7)
    assert l1 != l2
    
    l1 = ImmutableList(6, 7, 8)
    l2 = ImmutableList(5, 6, 7)
    assert l1 != l2
    
    l1 = ImmutableList()
   

# Generated at 2022-06-14 03:22:00.144956
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1).filter(lambda e: e > 1) == ImmutableList.empty()
    assert ImmutableList.of(1).filter(lambda e: e < 1) == ImmutableList.empty()
    assert ImmutableList.of(1, 2, 3).filter(lambda e: e > 1) == ImmutableList.of(2, 3)
    assert ImmutableList.of(1, 2, 3).filter(lambda e: e < 1) == ImmutableList.empty()
    assert ImmutableList.of(1, 2, 3).filter(lambda e: e > 2) == ImmutableList.of(3)
    assert ImmutableList.of(1, 2, 3).filter(lambda e: e < 2) == ImmutableList.of(1)

# Generated at 2022-06-14 03:22:10.955582
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList(5) == ImmutableList(5)
    assert ImmutableList(5, ImmutableList(10)) == ImmutableList(5, ImmutableList(10))
    assert ImmutableList(10, ImmutableList(5)) != ImmutableList(5, ImmutableList(10))
    assert ImmutableList(10, ImmutableList(5)) != ImmutableList(10)
    assert ImmutableList(5, ImmutableList(10)) != ImmutableList(10)
    assert ImmutableList(5, ImmutableList(5)) == ImmutableList(5, ImmutableList(5))
    assert ImmutableList(5, ImmutableList('ABC', ImmutableList(False), ImmutableList(True))) == ImmutableList(5, ImmutableList('ABC', ImmutableList(False), ImmutableList(True)))
    assert Imm

# Generated at 2022-06-14 03:22:30.936678
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1).filter(lambda x: x > 0) == ImmutableList.of(1)
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x % 2 == 0) == ImmutableList.of(2)
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x % 2 == 1) == ImmutableList.of(1, 3)
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x > 3) == ImmutableList.empty()
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x < 1) == ImmutableList.empty()

# Generated at 2022-06-14 03:22:34.476300
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    def test_find(element_to_find, expected_result):
        assert ImmutableList.of(1, 2, 3).find(lambda el: el == element_to_find) == expected_result

    test_find(None, None)
    test_find(1, 1)
    test_find(3, 3)
    test_find(5, None)


# Generated at 2022-06-14 03:22:45.091232
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    import numpy as np
    from random import randint

    num_items = randint(30, 100)
    items = [randint(-100, 100) for _ in range(num_items)]
    even_items = [x for x in items if x % 2 == 0]
    odd_items = [x for x in items if x % 2 == 1]
    zero_items = [x for x in items if x == 0]
    non_zero_items = [x for x in items if x != 0]
    assert ImmutableList.of(*items).filter(lambda x: x % 2 == 0).to_list() == even_items
    assert ImmutableList.of(*items).filter(lambda x: x % 2 == 1).to_list() == odd_items

# Generated at 2022-06-14 03:22:49.419154
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    l = ImmutableList.of(1, 2, 3, 4, 5, 6, 7, 8, 9)
    l1 = l.filter(lambda x: x % 2 == 0)
    assert l1 == ImmutableList.of(2, 4, 6, 8)



# Generated at 2022-06-14 03:23:15.441305
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    list_one = ImmutableList.of(1,2,3,4,5)
    list_two = ImmutableList.of(1,2,3,4,5)

    assert True == (list_one == list_two)

    list_one = ImmutableList.of(7,8,9)
    list_two = ImmutableList.of(1,2,3)

    assert False == (list_one == list_two)

    list_one = ImmutableList.of(1,2,3)
    list_two = list_one.append(4)

    assert False == (list_one == list_two)

    list_one = ImmutableList.of(1,2,3)
    list_two = list_one.unshift(4)


# Generated at 2022-06-14 03:23:26.934462
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList(1) == ImmutableList(1)
    assert ImmutableList(1) != ImmutableList(2)
    assert ImmutableList(1, ImmutableList(2)) == ImmutableList(1, ImmutableList(2))
    assert ImmutableList(1, ImmutableList(2)) != ImmutableList(2, ImmutableList(2))
    assert ImmutableList() == ImmutableList(is_empty=True)
    assert ImmutableList(is_empty=True) != ImmutableList()
    assert ImmutableList(is_empty=True) == ImmutableList(is_empty=True)
    assert ImmutableList(1, ImmutableList(2, ImmutableList(is_empty=True))) == ImmutableList(1, ImmutableList(2, ImmutableList(is_empty=True)))

# Unit

# Generated at 2022-06-14 03:23:29.670295
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    x = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    assert x.find(lambda x: x > 1) == 2


# Unit tests for method reduce of class ImmutableList

# Generated at 2022-06-14 03:23:35.347902
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    # Case when compared lists has same elements in same order
    # given
    list1 = ImmutableList.of(1, 2, 3)
    list2 = ImmutableList.of(1, 2, 3)

    # when
    result = list1.__eq__(list2)

    # then
    assert result is True, 'Should return True'

    # Case when compared lists has not same elements in same order
    # given
    list3 = ImmutableList.of(1, 2, 3)
    list4 = ImmutableList.of(1, 3, 2)

    # when
    result = list3.__eq__(list4)

    # then
    assert result is False, 'Should return False'

# Generated at 2022-06-14 03:23:40.180929
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList().filter(lambda x: x) == ImmutableList.empty()
    assert ImmutableList.of(1, 3, 5).filter(lambda x: x % 2 == 0) == ImmutableList.empty()
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x % 2 == 0) == ImmutableList.of(2)
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x % 2 == 1) == ImmutableList.of(1, 3)
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x % 3 == 0) == ImmutableList.empty()
    assert ImmutableList.of(1, 2, 3).filter(lambda x: True) == ImmutableList.of(1, 2, 3)


test_Immutable

# Generated at 2022-06-14 03:23:48.231749
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1).filter(lambda x: x > 1) == ImmutableList.empty()

    assert ImmutableList.of(1, 2, 3).filter(lambda x: x > 1) == ImmutableList.of(2, 3)

    assert ImmutableList.of(1).filter(lambda x: x == 1) == ImmutableList.of(1)

    assert ImmutableList.of("foo", "bar").filter(lambda x: x == "foo") == ImmutableList.of("foo")
    

# Generated at 2022-06-14 03:23:53.506163
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1).find(lambda val: val == 1) == 1
    assert ImmutableList.of(1, 2).find(lambda val: val == 2) == 2
    assert ImmutableList.of("abc", "efg").find(lambda val: val == "abc") == "abc"
    assert ImmutableList.of("abc", "efg").find(lambda val: val == "efg") == "efg"
    assert ImmutableList.of("abc", "efg").find(lambda val: val == "hij") is None
    assert ImmutableList.of("abc").find(lambda val: val == "abc") == "abc"
    assert ImmutableList.of("abc").find(lambda val: val == "efg") is None

# Generated at 2022-06-14 03:23:56.305834
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList(1, 2, 3) == ImmutableList(1, 2, 3)



# Generated at 2022-06-14 03:24:04.721664
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1).filter(lambda x: x < 10) == ImmutableList.of(1)
    assert ImmutableList.of(1).filter(lambda x: x > 10) == ImmutableList.empty()
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x < 10) == ImmutableList.of(1, 2, 3)
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x > 10) == ImmutableList.empty()
    assert ImmutableList.empty().filter(lambda x: x < 10) == ImmutableList.empty()
    assert ImmutableList.empty().filter(lambda x: x > 10) == ImmutableList.empty()



# Generated at 2022-06-14 03:24:08.740378
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda x: x % 2 != 0) == ImmutableList.of(1, 3)
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda x: x % 2 == 0) == ImmutableList.of(2, 4)
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda x: x > 4) == ImmutableList.empty()


# Generated at 2022-06-14 03:24:39.874930
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    # Arrange
    # Act
    # Assert
    assert ImmutableList.of('A') == ImmutableList.of('A')
    assert ImmutableList.of('A').append('B') == ImmutableList.of('A').append('B')
    assert ImmutableList.of('A') != 'A'
    assert ImmutableList.empty() == ImmutableList.empty()
    assert ImmutableList.of('A') != ImmutableList.of('B')
    assert ImmutableList.of('A') != ImmutableList.of().append('A')
    assert ImmutableList.of('A').append('B') != ImmutableList.of().append('A')
    assert ImmutableList.of('A').append('B') != ImmutableList.of('B').append('A')

# Generated at 2022-06-14 03:24:45.989498
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(2, 3, 4, 5, 6, 7).find(lambda x: x == 5) == 5
    assert ImmutableList.of(2, 3, 4, 5, 6, 7).find(lambda x: x == 8) is None
    assert ImmutableList.of(2, 3, 4, 5, 6, 7).find(lambda x: x == 4) == 4
    assert ImmutableList.of(2, 3, 4, 5, 6, 7).find(lambda x: x == 10) is None

# Generated at 2022-06-14 03:24:47.941451
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    immutable_list_1 = ImmutableList.of(1, 2, 3)
    immutable_list_2 = ImmutableList.of(1, 2, 3)

    
    assert immutable_list_1.__eq__(immutable_list_2) is True

# Generated at 2022-06-14 03:24:51.440842
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert \
        ImmutableList(1, ImmutableList(2, ImmutableList(3)), False) == \
        ImmutableList(1, ImmutableList(2, ImmutableList(3)), False)


# Generated at 2022-06-14 03:24:58.851634
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # Given
    list_of_numbers = ImmutableList.of(10, 20, 30, 40, 50)

    # When
    result_found_element = list_of_numbers.find(lambda x: x > 40)
    result_not_found_element = list_of_numbers.find(lambda x: x > 60)
    result_from_empty_list = ImmutableList.empty().find(lambda x: x > 40)

    # Then
    assert result_found_element == 50
    assert result_not_found_element is None
    assert result_from_empty_list is None



# Generated at 2022-06-14 03:25:08.419425
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList(24).find(lambda x: x == 24) == 24
    assert ImmutableList(24).find(lambda x: x == 40) is None
    assert ImmutableList(24, ImmutableList(24, ImmutableList(24))).find(
        lambda x: x == 24) == 24
    assert ImmutableList(24, ImmutableList(24, ImmutableList(24))).find(
        lambda x: x == 40) is None
    assert ImmutableList(24, ImmutableList(40, ImmutableList(40))).find(
        lambda x: x == 40) == 40
    assert ImmutableList(24, ImmutableList(40, ImmutableList(40))).find(
        lambda x: x == 24) == 24

# Generated at 2022-06-14 03:25:19.663372
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    def test_with_a_function(
        fn: Callable[[Optional[int]], bool],
        assert_func: Callable[[ImmutableList[int], ImmutableList[int]], None]
    ):
        assert_func(
            ImmutableList.of(1, 2, 3, 4).filter(fn),
            ImmutableList.of(2, 4)
        )

    test_with_a_function(
        lambda x: x % 2 == 0,
        assert_ImmutableList_is_equal
    )



# Generated at 2022-06-14 03:25:39.180604
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    # Arrange
    l1 = ImmutableList.empty()
    l2 = ImmutableList.empty()
    l3 = ImmutableList.of(0)
    l4 = ImmutableList.of(0)

    # Act
    res1 = l1 == l2
    res2 = l1 != l2
    res3 = l1 == l3
    res4 = l3 == l4
    res5 = l3 == l2
    res6 = l3 != l4

    # Assert
    assert res1 is True
    assert res2 is False
    assert res3 is False
    assert res4 is True
    assert res5 is False
    assert res6 is False

# Generated at 2022-06-14 03:25:42.569801
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.of(1, 2, 3) == ImmutableList.of(1, 2, 3)
    assert ImmutableList.empty() == ImmutableList.empty()


# Generated at 2022-06-14 03:25:47.640685
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    a = ImmutableList.of(1, 2, 3)
    b = ImmutableList.of(1, 2, 3)
    c = ImmutableList.of(3, 2, 1)

    assert (a == a) is True
    assert (a == b) is True
    assert (b == a) is True
    assert (a == c) is False
    assert (c == a) is False

# Generated at 2022-06-14 03:26:15.850207
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList().__eq__(ImmutableList()) is True
    assert ImmutableList(None).__eq__(ImmutableList(None)) is True
    assert ImmutableList(True).__eq__(ImmutableList(False)) is False
    assert ImmutableList(False).__eq__(ImmutableList(True)) is False
    assert ImmutableList(542).__eq__(ImmutableList(543)) is False
    assert ImmutableList(543).__eq__(ImmutableList(542)) is False
    assert ImmutableList(543).__eq__(ImmutableList(543)) is True
    assert ImmutableList(543).__eq__(ImmutableList(None)) is False
    assert ImmutableList().__eq__(ImmutableList(543)) is False

# Generated at 2022-06-14 03:26:19.093276
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    l = ImmutableList.of(1, 2, 3, 4, 5)
    assert l.find(lambda x: x==3) == 3
    assert l.find(lambda x: x==10) is None


# Generated at 2022-06-14 03:26:27.222872
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    # Unit test for method __eq__ of class ImmutableList with params: head=None, tail=None, is_empty=True
    m_list1 = ImmutableList(None, None, True)
    m_list2 = ImmutableList(None, None, True)
    assert m_list1 == m_list2
    m_list1 = ImmutableList(None, ImmutableList(None, None, True), True)
    m_list2 = ImmutableList(None, ImmutableList(None, None, True), True)
    assert m_list1 == m_list2
    m_list1 = ImmutableList(1, None, True)
    m_list2 = ImmutableList(2, None, True)
    assert not m_list1 == m_list2

# Generated at 2022-06-14 03:26:30.655242
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3).find(lambda num: num == 2) == 2
    assert ImmutableList.of(1, 2, 3).find(lambda num: num == 5) is None
    assert ImmutableList.empty().find(lambda num: num == 2) is None


# Generated at 2022-06-14 03:26:42.103946
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    l = ImmutableList.of(1)
    l1 = ImmutableList.of(1)
    l2 = ImmutableList.of(2)

    assert l == l1
    assert l != l2

