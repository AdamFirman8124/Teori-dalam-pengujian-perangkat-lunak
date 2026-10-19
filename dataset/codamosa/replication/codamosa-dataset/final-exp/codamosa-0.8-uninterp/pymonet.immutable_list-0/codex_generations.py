

# Generated at 2022-06-14 03:16:51.042904
# Unit test for method reduce of class ImmutableList
def test_ImmutableList_reduce():
    list_ = ImmutableList.of(1, 2, 3)
    assert list_.reduce(lambda acc, x: acc + x, 0) == 6

# Generated at 2022-06-14 03:16:57.377348
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3).filter(lambda element: element > 1) == ImmutableList.of(2, 3)
    assert ImmutableList.of(1, 2, 3).filter(lambda element: element > 3) == ImmutableList.empty()
    assert ImmutableList.of(1, 2, 3).filter(lambda element: element == 3) == ImmutableList.of(3)



# Generated at 2022-06-14 03:17:01.027816
# Unit test for method reduce of class ImmutableList
def test_ImmutableList_reduce():
    assert ImmutableList.of(1, 2, 3).reduce(lambda a, b: a + b, 0 ) == 6
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))).reduce(lambda a, b: a + b, 0 ) == 6


# Generated at 2022-06-14 03:17:03.638267
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list_ = ImmutableList.empty().append(1).append(2)

    filtered = list_.filter(lambda member: member % 2 == 0)

    assert filtered.to_list() == [2]


# Generated at 2022-06-14 03:17:07.800802
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list_to_filter = ImmutableList.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    filter_out_even = list_to_filter.filter(lambda x: x % 2 != 0)
    assert filter_out_even == ImmutableList.of(1, 3, 5, 7, 9), "ImmutableList filter return wrong value."


# Generated at 2022-06-14 03:17:15.816872
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # given
    list1 = ImmutableList.of(1, 2, 3, 4)
    list2 = ImmutableList.of(2, 4)

    # when
    res = list1.filter(lambda x: x % 2 == 0)

    # then
    assert res == list2



# Generated at 2022-06-14 03:17:19.300137
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    m = ImmutableList.of(1, 2, 3)

    assert m.find(lambda value: value == 1) == 1

# Generated at 2022-06-14 03:17:23.867948
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.empty().find(lambda x: x % 2 == 0) is None
    assert ImmutableList.of(2).find(lambda x: x % 2 == 0) is 2
    assert ImmutableList.of(1, 2).find(lambda x: x % 2 == 0) is 2
    assert ImmutableList.of(1, 3, 5, 7, 9).find(lambda x: x % 2 == 0) is None


test_ImmutableList_find()

# Generated at 2022-06-14 03:17:34.498838
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.of(1, 2, 3) == ImmutableList.of(1, 2, 3)
    assert ImmutableList.of(1, 2, 3) != ImmutableList.of(1, 2, 4)
    assert ImmutableList.of(1, 2, 3) != [1, 2, 3]
    assert ImmutableList() != ImmutableList.of(1, 2, 3)
    assert ImmutableList.empty() != ImmutableList.of(1, 2, 3)
    assert ImmutableList.of(1, 2, 3) != ImmutableList()
    assert ImmutableList.of(1, 2, 3) != ImmutableList.empty()

# Generated at 2022-06-14 03:17:43.889267
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList() == ImmutableList()
    assert ImmutableList('1') == ImmutableList('1')
    assert ImmutableList('1', ImmutableList('2')) == ImmutableList('1', ImmutableList('2'))
    assert ImmutableList('1', ImmutableList('2')) != ImmutableList('2', ImmutableList('1'))
    assert ImmutableList('1', ImmutableList('2')) != ImmutableList('1', ImmutableList('2', ImmutableList('3')))
    assert ImmutableList('2', None) == ImmutableList('2', ImmutableList())
    assert ImmutableList('1') != '1'


# Generated at 2022-06-14 03:17:52.715484
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x > 2) == ImmutableList.of(
        3
    )

    assert ImmutableList.of(1, 2, 3).filter(lambda x: x == 1) == ImmutableList.of(
        1
    )

    assert ImmutableList.of(1, 2, 3).filter(lambda x: x > 3) == ImmutableList.empty()


# Generated at 2022-06-14 03:17:57.820019
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    initial_list = ImmutableList.of(1,2,3,4)
    filtered_list = initial_list.filter(lambda x: x >= 3)
    assert filtered_list == ImmutableList.of(3,4)



# Generated at 2022-06-14 03:18:11.477978
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    # 1. Test, when head is equal
    # 1.1. When tail is empty
    assert ImmutableList.of(1) == ImmutableList.of(1)
    # 1.2. When tail isn't empty
    assert ImmutableList.of(1, 2) == ImmutableList.of(1, 2)
    # 2. Test, when head isn't equal
    # 2.1. When tail is empty
    assert ImmutableList.of(1) != ImmutableList.of(2)
    # 2.2. When tail isn't empty
    assert ImmutableList.of(1, 2) != ImmutableList.of(2, 3)
    # 3. Test, when object is other class
    assert ImmutableList.of(1) != []
    # 4. Test, when object is None

# Generated at 2022-06-14 03:18:20.371092
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    """Tests if ImmutableList.filter works well"""
    l = ImmutableList.of(
        1,
        2,
        3,
        4,
        5,
    )

    assert l != l.filter(lambda x: x > 3)

    assert l.filter(lambda x: x > 3) == ImmutableList.of(4, 5)
    assert l.filter(lambda x: x > 30) == ImmutableList.empty()

    assert l.filter(lambda x: x == 4) == ImmutableList.of(4)
    assert l.filter(lambda x: x == 3) == ImmutableList.of(3)
    assert l.filter(lambda x: x == 1) == ImmutableList.of(1)

    assert l.filter(lambda x: x % 2 == 0) == ImmutableList.of

# Generated at 2022-06-14 03:18:30.449483
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 1) == 1
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 2) == 2
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 3) == 3
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 4) == 4
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 5) == 5
    assert ImmutableList.empty().find(lambda x: x == None) == None
    

# Generated at 2022-06-14 03:18:42.155092
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList().__eq__(ImmutableList()) == True
    assert ImmutableList(2).__eq__(ImmutableList(2)) == True
    assert ImmutableList(7).__eq__(ImmutableList()) == False
    assert ImmutableList().__eq__(ImmutableList(12)) == False
    assert ImmutableList(is_empty=True).__eq__(ImmutableList(is_empty=True)) == True
    assert ImmutableList(is_empty=True).__eq__(ImmutableList()) == False
    assert ImmutableList().__eq__(ImmutableList(is_empty=True)) == False
    assert ImmutableList(is_empty=True).__eq__(ImmutableList(1)) == False

# Generated at 2022-06-14 03:18:50.838914
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    first_list = ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4, ImmutableList(5)))))
    second_list = ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4, ImmutableList(5)))))
    third_list = ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4, ImmutableList(6)))))
    forth_list = ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4, ImmutableList(5, ImmutableList(6))))))
    assert first_list == second_list
    assert first_list != third_list
    assert third_list != forth_list



# Generated at 2022-06-14 03:19:07.318692
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList() == ImmutableList()
    assert ImmutableList(1) == ImmutableList(1)
    assert ImmutableList(1, ImmutableList(2)) == ImmutableList(1, ImmutableList(2))
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))) == ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    assert ImmutableList(1) != ImmutableList(2)



# Generated at 2022-06-14 03:19:17.620490
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    dynamic_list_1 = [1, 2, 3, 4, 5]
    dynamic_list_2 = [1, 3, 5, 7, 9]

    immutable_list_1 = ImmutableList.of(*dynamic_list_1)
    immutable_list_2 = ImmutableList.of(*dynamic_list_2)

    def filter_even_values(value):
        return value % 2 == 0

    def filter_odd_values(value):
        return value % 2 != 0

    dynamic_list_1 = list(filter(filter_even_values, dynamic_list_1))
    dynamic_list_2 = list(filter(filter_odd_values, dynamic_list_2))

    immutable_list_1 = immutable_list_1.filter(filter_even_values)
    immutable_list_2 = immutable_list_

# Generated at 2022-06-14 03:19:20.277181
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    # Arrange
    a = ImmutableList.of('a', 'b', 'c')
    b = ImmutableList.of('a', 'b', 'c')

    # Act & Assert
    assert a == b



# Generated at 2022-06-14 03:19:26.550041
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(*range(10)).filter(lambda x: x > 2) == ImmutableList.of(3, 4, 5, 6, 7, 8, 9)



# Generated at 2022-06-14 03:19:33.631483
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x < 3) == 1
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x > 3) == 4
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 0) is None
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 6) is None

# Generated at 2022-06-14 03:19:44.964533
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    empty_list = ImmutableList.empty()

    simple_list = ImmutableList.of(1, 2, 3)

    complex_list = ImmutableList.of(
        ImmutableList.of(1, 2),
        ImmutableList.of(3, 4),
        ImmutableList.of(5, 6),
    )

    assert empty_list.find(lambda item: False) is None

    assert empty_list.find(lambda item: True) is None

    assert simple_list.find(lambda item: item == 2) == 2

    assert simple_list.find(lambda item: item == 5) is None

    assert complex_list.find(lambda item: len(item) == 2) == ImmutableList.of(3, 4)



# Generated at 2022-06-14 03:19:49.170801
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list_ = ImmutableList.of(1, 2, 3, 4, 5)
    assert len(list_.filter(lambda x: x < 4)) == 3
    assert list_.filter(lambda x: x < 4).find(lambda x: x > 1) == 2


# Generated at 2022-06-14 03:19:59.940962
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.empty().filter(lambda el: False) == ImmutableList.empty()

    assert ImmutableList.of(1, 2, 3, 4)\
        .filter(lambda el: el > 2) \
        == ImmutableList.of(3, 4)

    assert ImmutableList.of(1, 2, 3, 4)\
        .filter(lambda el: el < 2) \
        == ImmutableList.of(1)


# Generated at 2022-06-14 03:20:03.598099
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 5).find(lambda item: item == 0) is None
    assert ImmutableList.of(1, 2, 3, 5).find(lambda item: item == 1) == 1
    assert ImmutableList.of(1, 2, 3, 5, 123456).find(lambda item: item == 123456) == 123456

# Generated at 2022-06-14 03:20:06.578910
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    lst = ImmutableList.of(1, 2, 3)
    assert(lst.find(lambda element: element == 2) == 2)
    assert(lst.find(lambda element: element == 4) is None)



# Generated at 2022-06-14 03:20:11.540136
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(15, 10, 20, 30).filter(lambda x: x == 20) == ImmutableList.of(20)
    assert ImmutableList.of(15, 10, 20, 30).filter(lambda x: x % 10 == 0) == ImmutableList.of(10, 20, 30)
    assert ImmutableList.of(15, 10, 20, 30).filter(lambda x: x > 30) == ImmutableList.empty()


# Generated at 2022-06-14 03:20:13.989547
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    ilist = ImmutableList.of(1, 2, 3, 4, 5)
    assert ilist.find(lambda x: x % 2 == 0) == 2
    assert ilist.find(lambda x: x % 5 == 0) == 5
    assert ilist.find(lambda x: x == 6) is None



# Generated at 2022-06-14 03:20:18.961205
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 2) == 2
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 4) is None


# Generated at 2022-06-14 03:20:38.668223
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    l = ImmutableList.of(0, 4, 6, 8, 10, 12, 14, 16, 18, 20)
    assert l.filter(lambda a: a>5).to_list() == [6, 8, 10, 12, 14, 16, 18, 20]
    assert l.filter(lambda a: a<15).to_list() == [0, 4, 6, 8, 10, 12, 14]
    assert l.filter(lambda a: a>15).to_list() == [16, 18, 20]
    print("PASSED: test_ImmutableList_filter")


# Generated at 2022-06-14 03:20:43.305818
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    l = ImmutableList.of(1, 2, 3, 4).find(lambda x: x % 2 == 0)
    assert l == 2

    l = ImmutableList.of(1, 2, 3, 4).find(lambda x: x % 2 != 0)
    assert l == 1

    l = ImmutableList.of(1, 2, 3, 4).find(lambda x: x % 2 == 0)
    assert l == 2

    l = ImmutableList.of(1, 2, 3, 4).find(lambda x: x > 5)
    assert l is None

    l = ImmutableList.empty().find(lambda x: x % 2 == 0)
    assert l is None

# Generated at 2022-06-14 03:20:46.899730
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1,2,3,4,5).find(lambda x: x == 6) == None
    assert ImmutableList.of(1,2,3,4,5).find(lambda x: x == 4) == 4

# Generated at 2022-06-14 03:20:51.996549
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    numbers: ImmutableList[int] = ImmutableList()

    for i in range(0, 100):
        numbers = numbers.append(i)

    for element in numbers.to_list():
        assert numbers.find(lambda x: x == element) == element

# Generated at 2022-06-14 03:20:54.930590
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of('1', '2', '3', '4', '5').find(lambda a: a == '3') == '3'



# Generated at 2022-06-14 03:20:59.401600
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x % 2 == 0) == 2
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x % 2 == 1) == 1
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 6) is None
    assert ImmutableList.empty().find(lambda x: x % 2 == 0) is None


# Generated at 2022-06-14 03:21:01.996645
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    print('=====Test for method find of class ImmutableList=====')
    assert ImmutableList.of(1, 2, 3).find(lambda x: x > 1) == 2, 'Not passed'
    assert ImmutableList.of(1, 2, 3).find(lambda x: x > 3) is None, 'Not passed'
    assert ImmutableList.of(1, 2, 3).find(lambda x: x < 1) is None, 'Not passed'
    print('=====Test passed!=====')

# Generated at 2022-06-14 03:21:04.316924
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda x: x % 2 == 0) == ImmutableList.of(2, 4)



# Generated at 2022-06-14 03:21:06.163029
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    list_ = ImmutableList.of(1, 2, 3, 4, 5)
    assert list_.find(lambda x: x > 2) == 3

# Generated at 2022-06-14 03:21:10.326272
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    l = ImmutableList.of(1, 2, 3, 4)

    # add element to empty list
    new_l = l.filter(lambda x: x != 3)

    assert len(new_l) == 3
    assert new_l != l
    assert new_l.head == 1
    assert new_l.tail == ImmutableList.of(2, 4)



# Generated at 2022-06-14 03:21:34.330882
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    int_list = ImmutableList.of(1, 2, 3)
    assert int_list.filter(lambda x: x < 3) == ImmutableList.of(1, 2)
    assert int_list.filter(lambda x: x > 3) == ImmutableList.empty()
    assert int_list.filter(lambda x: x == 2) == ImmutableList.of(2)


# Generated at 2022-06-14 03:21:37.274709
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    lst = ImmutableList.of(1, 2, 3, 4, 5, 6, 7)
    assert lst.filter(lambda x: x % 2 == 0).to_list() == [2, 4, 6]


# Generated at 2022-06-14 03:21:44.363118
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    data = [1,2,'hello', 'world', 8]
    
    list_of = ImmutableList.of
    empty = ImmutableList.empty

    imm_list = list_of('hello',*data)
    res = imm_list.filter(lambda x: True if str(x).isdigit() else False).to_list()
    
    res2 = imm_list.filter(lambda x: True if str(x).isalpha() else False).to_list()


# Executing unit tests
test_ImmutableList_filter()

# Generated at 2022-06-14 03:21:53.027821
# Unit test for method find of class ImmutableList
def test_ImmutableList_find(): # pragma: no cover
    il = ImmutableList.of(1, 2, 3, 4).filter(lambda x: x % 2 == 0)
    assert il.find(lambda x: x > 2) == 4
    assert il.find(lambda x: x > 4) is None
    assert ImmutableList.empty().find(lambda _: True) is None


# Generated at 2022-06-14 03:22:00.606012
# Unit test for method filter of class ImmutableList

# Generated at 2022-06-14 03:22:05.606162
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    def test(fn, expected_output):
        assert ImmutableList.of(1, 2, 3, 4, 5).find(fn) == expected_output

    test(lambda x: x%2 == 0, 2)
    test(lambda x: x == 6, None)

# Unit tests for method reduce of class ImmutableList

# Generated at 2022-06-14 03:22:06.899073
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    list1 = ImmutableList(2, ImmutableList(3, ImmutableList(4)))

    assert list1.find(lambda x: x > 3) == 4
    assert list1.find(lambda x: x == 0) is None



# Generated at 2022-06-14 03:22:08.806636
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    test_ImmutableList = ImmutableList.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    assert test_ImmutableList.filter(lambda x: x % 2 == 0) == ImmutableList.of(2, 4, 6, 8, 10)

# Generated at 2022-06-14 03:22:13.547283
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list_number_positive = ImmutableList.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    list_number_negative = ImmutableList.of(-1, -2, -3, -4, -5, -6, -7, -8, -9, -10)
    list_number_mixed = ImmutableList.of(1, 2, -3, 4, -5, 6, 7, -8, 9, 10)

    assert list_number_positive.filter(lambda x: x > 3) == ImmutableList.of(4, 5, 6, 7, 8, 9, 10)
    assert list_number_negative.filter(lambda x: x < -3) == ImmutableList.of(-1, -2)

# Generated at 2022-06-14 03:22:32.515620
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    immutable_list = ImmutableList.of(1, 2, 3, 4, 5)

    # givven
    test_cases = [
        (lambda element: element % 2 == 0, lambda elements: elements == [2, 4]),
        (lambda element: element % 2 == 0, lambda elements: elements == [2, 4]),
        (lambda element: element == 5, lambda elements: elements == [5]),
        (lambda element: element == 6, lambda elements: elements == [])
    ]
    # when
    for fn, assertion in test_cases:
        result = immutable_list.filter(fn)
        # then
        assert assertion(result.to_list()) == True


test_ImmutableList_filter()


# Generated at 2022-06-14 03:23:14.436495
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    def filter_any_even(x):
        return x % 2 == 0

    assert ImmutableList.of(1, 2, 3, 4, 5).filter(filter_any_even) == ImmutableList.of(2, 4)
    assert ImmutableList.of(1, 3, 5).filter(filter_any_even) == ImmutableList.empty()
    assert ImmutableList.empty().filter(filter_any_even) == ImmutableList.empty()


# Generated at 2022-06-14 03:23:23.909464
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    words = ImmutableList.of(
        'One',
        'Two',
        'Three',
        'Four',
        'Five'
    )

    words_with_o = words.filter(
        lambda el: el[0] == 'o'
    )

    assert(
        words_with_o == ImmutableList.of('One', 'Two')
    )
test_ImmutableList_filter()

# Generated at 2022-06-14 03:23:29.781382
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 1) == 1
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 2) == 2
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 3) == 3
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 4) == None

    assert ImmutableList.empty().find(lambda x: True) == None

# Generated at 2022-06-14 03:23:32.606377
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda x: x != 2) == ImmutableList.of(1, 3, 4)
    assert ImmutableList.empty().filter(lambda x: x != 2) == ImmutableList.empty()

# Generated at 2022-06-14 03:23:40.959913
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3)\
        .filter(lambda el: el < 3)\
        .to_list() == [1, 2]

    assert ImmutableList.of(1, 2, 3, 4)\
        .filter(lambda el: el % 2 == 0)\
        .to_list() == [2, 4]


# Generated at 2022-06-14 03:23:51.035075
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4, 5, 6).filter(lambda x: x % 2 == 0).to_list() == [2, 4, 6]
    assert ImmutableList.of('a', 'b', 'c', 'd', 'e', 'f').filter(lambda x: x in ['c', 'e', 'g']).to_list() == ['c', 'e']
    assert ImmutableList.of(1, 2, 3, 4, 5, 6).filter(lambda x: x > 3).to_list() == [4, 5, 6]
    assert ImmutableList.of(1, 2, 3, 4, 5, 6).filter(lambda x: x == 10).to_list() == []
    assert ImmutableList.of(1).filter(lambda x: x == 10).is_empty


# Generated at 2022-06-14 03:23:58.355725
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    def filter_fn(x):
        return x > 3

    immutable_list = ImmutableList.of(1, 2, 3, 4, 5)
    immutable_list_with_filter = immutable_list.filter(filter_fn)

    assert [4, 5] == immutable_list_with_filter.to_list()

# Generated at 2022-06-14 03:24:03.934716
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    """
    Test case verifies if to ImmutableList instaces are equal if they have
    same elements and no elements
    """
    list_one = ImmutableList.of(1, 2, 3)
    list_two = ImmutableList.of(1, 2, 3)
    list_three = ImmutableList.of(1, 2, 3, 4)

    assert list_one == list_two
    assert list_one != list_three
    assert list_two != list_three



# Generated at 2022-06-14 03:24:05.378414
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 2) == 2, 'ImmutableList: function find returns wrong value'


# Generated at 2022-06-14 03:24:10.110337
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list = ImmutableList.of(1, 2, 3)
    assert list.filter(lambda x: x > 1) == ImmutableList.of(2, 3)
    assert list.filter(lambda x: x < 2) == ImmutableList.of(1)
    assert list.filter(lambda x: x > 3) == ImmutableList.empty()


# Generated at 2022-06-14 03:25:44.495365
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # given
    test_list = ImmutableList.of(1, 2, 3)
    expected = 2

    # when
    result = test_list.find(lambda x: x == 2)

    # then
    assert result == expected
    assert test_list == ImmutableList.of(1, 2, 3)

# Generated at 2022-06-14 03:25:51.108079
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x > 2) is 3
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 1) is 1

# Generated at 2022-06-14 03:25:54.950725
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList(val for val in range(0, 10)).find(lambda x: x == 5) == 5



# Generated at 2022-06-14 03:26:03.680810
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # Test case 1
    # Input
    list_ = ImmutableList.of(1, 2, 3)
    fn = lambda x: x > 1
    # Desired result
    desired_result = ImmutableList.of(2, 3)
    # Executing
    actual_result = list_.filter(fn)
    # Asserting
    assert actual_result == desired_result
    # Test case 2
    # Input
    list_ = ImmutableList.of(1, 2, 3)
    fn = lambda x: x < 2
    # Desired result
    desired_result = ImmutableList.of(1)
    # Executing
    actual_result = list_.filter(fn)
    # Asserting
    assert actual_result == desired_result
    # Test case 3
    # Input
    list_ = ImmutableList

# Generated at 2022-06-14 03:26:14.229418
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list1 = ImmutableList.of(1, 2, 3, 4)
    list2 = ImmutableList.of(1, 2, 3, 4)
    list3 = ImmutableList.of(4, 5, 7, 8)

    def is_even(value: int) -> bool:
        return value % 2 == 0

    list1_evens = list1.filter(is_even)
    assert list1_evens == list2.filter(is_even)
    assert ImmutableList.empty() == list3.filter(is_even)


# Generated at 2022-06-14 03:26:26.691434
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    test_list = ImmutableList.of(1, 2, 3, 4)

    filtered_list = test_list.filter(lambda e: e % 2 == 0)

    assert filtered_list == ImmutableList.of(2, 4)



# Generated at 2022-06-14 03:26:44.674009
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x > 2).to_list() == [3]
    assert ImmutableList.of(10, 4, 6, 5, 1, 8, 3, 9, 7, 2).filter(lambda x: x > 0).to_list() == [10, 4, 6, 5, 1, 8, 3, 9, 7, 2]
    assert ImmutableList.of(10, 4, 6, 5, 1, 8, 3, 9, 7, 2).filter(lambda x: x < 3).to_list() == [1, 2]
    assert ImmutableList.of(10, 4, 6, 5, 1, 8, 3, 9, 7, 2).filter(lambda x: x > 10).to_list() == []