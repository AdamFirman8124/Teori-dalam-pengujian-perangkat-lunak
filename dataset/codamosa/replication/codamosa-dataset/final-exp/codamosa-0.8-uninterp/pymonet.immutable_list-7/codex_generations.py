

# Generated at 2022-06-14 03:16:58.815946
# Unit test for method filter of class ImmutableList

# Generated at 2022-06-14 03:17:07.277703
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    # Test for case when other is not instance of ImmutableList
    l1 = ImmutableList(1)
    assert l1.__eq__(1) is False, '__eq__ should return False if other is not instance'

    # Test for case when other is instance of ImmutableList and has
    # same head and tail
    l2 = ImmutableList(1)
    assert l1.__eq__(l2) is True, '__eq__ should return True if other is instance'

    # Test for case when other is instance of ImmutableList but has
    # different head
    l3 = ImmutableList(2)
    assert l1.__eq__(l3) is False, '__eq__ should return False if other is instance'

    # Test for case when other is instance of ImmutableList but has
    # different tail
    l

# Generated at 2022-06-14 03:17:16.230883
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.empty().find(lambda v: v == 'head') is None
    assert ImmutableList.of('head', 'body', 'foot').find(lambda v: v == 'head') == 'head'
    assert ImmutableList.of('head', 'body', 'foot').find(lambda v: v == 'foot') == 'foot'
    assert ImmutableList.of('head', 'body', 'foot').find(lambda v: v == 'fail') is None


# Generated at 2022-06-14 03:17:26.281538
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    all_passed = True
    def _assert(arg, result):
        nonlocal all_passed

        if arg != result:
            print('ImmutableList test failed. args: {} expected: {} result: {}'.format(arg, result, str(arg)))
            all_passed = False

    _assert(
        ImmutableList().find(lambda x: True),
        None
    )

    _assert(
        ImmutableList(None).find(lambda x: True),
        None
    )

    _assert(
        ImmutableList(1, 2, 3).find(lambda x: True),
        1
    )

    _assert(
        ImmutableList(1, 2, 3).find(lambda x: x == 2),
        2
    )


# Generated at 2022-06-14 03:17:33.208026
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.of(1) == ImmutableList.of(1)
    assert ImmutableList.of(1, 2) == ImmutableList.of(1, 2)
    assert ImmutableList.of(1, 2) != ImmutableList.of(2, 3)
    assert ImmutableList.of(1, 2) != ImmutableList.of(1, 2, 3)


# Generated at 2022-06-14 03:17:38.767005
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList(1) == ImmutableList(1)
    assert ImmutableList(1, ImmutableList(2)) == ImmutableList(1, ImmutableList(2))
    assert ImmutableList(1) != ImmutableList(2)
    assert ImmutableList(1, ImmutableList(2)) != ImmutableList(1, ImmutableList(1))
    assert ImmutableList(1, ImmutableList(2)) != ImmutableList(2, ImmutableList(1))


# Generated at 2022-06-14 03:17:44.044395
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    collection = ImmutableList.of(1, 2, 3)

    assert collection.find(lambda x: x == 1) == 1
    assert collection.find(lambda x: x == 2) == 2
    assert collection.find(lambda x: x == 3) == 3
    assert collection.find(lambda x: x == 4) == None
    assert collection.find(lambda x: x == '2') == None


# Generated at 2022-06-14 03:17:53.225598
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    actual1 = ImmutableList.of(1, 2, 3)
    expected1 = ImmutableList.of(1, 2, 3)
    assert actual1 == expected1, 'expected {}, got {}'.format(expected1, actual1)

    actual2 = ImmutableList.of(1, 2, 3)
    expected2 = ImmutableList.of(1, 3, 2)
    assert not actual2 == expected2, 'expected {}, got {}'.format(expected2, actual2)

    actual3 = ImmutableList.of(1)
    expected3 = ImmutableList.of(1, 2, 3)
    assert not actual3 == expected3, 'expected {}, got {}'.format(expected3, actual3)



# Generated at 2022-06-14 03:17:58.247664
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # when
    l1 = ImmutableList.of(1, 2, 3)
    l2 = l1.filter(lambda a: a > 2)
    
    # then
    assert l2 == ImmutableList.of(3)



# Generated at 2022-06-14 03:18:03.169068
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.of(1) == ImmutableList.of(1)
    assert ImmutableList.of(1) != ImmutableList.of(2)
    assert ImmutableList.empty() == ImmutableList.empty()

# Generated at 2022-06-14 03:18:18.922748
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # Test for empty list
    assert ImmutableList.empty().filter(lambda x: True) == ImmutableList.empty()
    assert ImmutableList.empty().filter(lambda x: False) == ImmutableList.empty()
    # Test for one-element list
    assert ImmutableList.of(1).filter(lambda x: True) == ImmutableList.of(1)
    assert ImmutableList.of(1).filter(lambda x: False) == ImmutableList.empty()
    # Test for three elements list
    assert ImmutableList.of(1, 2, 3).filter(lambda x: True) == ImmutableList.of(1, 2, 3)
    assert ImmutableList.of(1, 2, 3).filter(lambda x: False) == ImmutableList.empty()

# Generated at 2022-06-14 03:18:21.886555
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    lst = ImmutableList.of(1, 2, 3)
    assert lst.find(lambda x: x == 3) == 3


# Generated at 2022-06-14 03:18:23.884994
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    my_list = ImmutableList.of(1, 2, 3, 4, 5)
    assert my_list.filter(lambda x: x > 2) == ImmutableList.of(3, 4, 5)
    assert my_list.filter(lambda x: False) == ImmutableList.empty()
    assert my_list.filter(lambda x: True) == my_list.to_list()

# Generated at 2022-06-14 03:18:31.899881
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    test_cases = [
        ([1, 2, 3, 4, 5], lambda val: val == 2, 2),
        ([1, 2, 3, 4, 5], lambda val: val == 7, None),
        ([1, 2, 3, 4, 5], lambda val: val == 3, 3)
    ]
    for case in test_cases:
        result = ImmutableList.of(*case[0]).find(case[1])
        if result != case[2]:
            raise AssertionError(
                'ImmutableList find test failed\n' +
                'expected: {}\n'.format(case[2]) +
                'actual: {}'.format(result)
            )


# Generated at 2022-06-14 03:18:46.548655
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    my_list = ImmutableList.of(1, 2, 3, 4, 5, 6)
    assert my_list.filter(lambda e: e % 2 == 0).to_list() == [2, 4, 6]
    assert my_list.filter(lambda e: e < 2 or e == 6).to_list() == [1, 6]


# Generated at 2022-06-14 03:18:53.859744
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    def test_empty_list():
        result = ImmutableList.empty().filter(lambda x: x > 1)
        expected = ImmutableList.empty()
        assert result == expected

    def test_list_with_one_item():
        result = ImmutableList(1).filter(lambda x: x > 1)
        expected = ImmutableList.empty()
        assert result == expected

    def test_list_with_two_items():
        result = ImmutableList(1, ImmutableList(2)).filter(lambda x: x > 1)
        expected = ImmutableList(2)
        assert result == expected

    def test_list_with_three_items():
        result = ImmutableList(1, ImmutableList(2, ImmutableList(3))).filter(lambda x: x > 1)

# Generated at 2022-06-14 03:18:56.146946
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    l = ImmutableList.of(1,2,3,4)
    assert l.find(lambda value: value % 2 == 0) == 2


# Generated at 2022-06-14 03:19:00.469281
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # Arrange
    test_values = [0, 1, 2]
    test_list = ImmutableList.of(*test_values)
    raw_result = test_list.filter(lambda v: v > 1)

    # Assert
    assert len(raw_result) == 1
    assert raw_result.find(lambda v: v == 2) == 2

if __name__ == "__main__":
    test_ImmutableList_filter()

# Generated at 2022-06-14 03:19:03.899986
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    l = ImmutableList.of(1,2,3,4,5)
    l = l.filter(lambda x: x < 4)

    assert l == ImmutableList.of(1,2,3)


# Generated at 2022-06-14 03:19:07.694750
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    l = ImmutableList.of(1, 2, 3, 4, 5)
    l = l.filter(lambda x: x % 2 == 0)

    assert l.to_list() == [2, 4]


# Generated at 2022-06-14 03:19:18.014224
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list = ImmutableList.empty()
    list = list.append('a')
    list = list.append('b')
    list = list.append('c')
    list = list.append('d')

    filtered_list = list.filter(lambda el: el == 'a' or el == 'd')

    assert filtered_list is not list
    assert filtered_list == ImmutableList('a', ImmutableList('d'))

test_ImmutableList_filter()

# Generated at 2022-06-14 03:19:24.568287
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    with test(ImmutableList.filter): 
        assert ImmutableList.empty().filter(lambda x: x == 1) == ImmutableList.empty()

        assert ImmutableList.empty().filter(lambda x: x == None) == ImmutableList.empty() == ImmutableList.of(None)

        assert ImmutableList.of(1, 2, 3).filter(lambda x: x % 2 == 1) == ImmutableList.of(1, 3)

        assert ImmutableList.of(1, 2, 3).filter(lambda x: x == 2) == ImmutableList.of(2)

        assert ImmutableList.of(1, 2, 3).filter(lambda x: x == 4) == ImmutableList.empty()


# Generated at 2022-06-14 03:19:26.803025
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x == 2 or x == 3) == ImmutableList.of(2, 3)


# Generated at 2022-06-14 03:19:37.878481
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    test_ImmutableList = ImmutableList.of(
        1, 2, 3
    )

    assert test_ImmutableList.find(lambda x: x == 1) == 1
    assert test_ImmutableList.find(lambda x: x == 3) == 3
    assert test_ImmutableList.find(lambda x: x == 5) is None
    assert test_ImmutableList.find(lambda x: x == -1) is None
    assert test_ImmutableList.filter(lambda x: x == 3) == ImmutableList.of(3)
    assert test_ImmutableList.filter(lambda x: x == 3).map(lambda x: '{}!'.format(x)) == ImmutableList.of('3!')

# Generated at 2022-06-14 03:19:49.781303
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    @given(lists(integers()))
    def should_find_an_element_that_passes_a_given_predicate(
            xs: List[int]):
        immutable_list = ImmutableList.of(*xs)
        predicate = lambda x: x % 2 == 0
        even_element = immutable_list.find(predicate)
        assert even_element in xs
        assert predicate(even_element)

    @given(
        lists(integers(), min_size=1),
        lists(integers()),
        lists(integers()))
    def should_find_an_element_that_passes_a_given_predicate_starting_from_the_end(
            xs: List[int], ys: List[int], zs: List[int]):
        immutable_list = Immutable

# Generated at 2022-06-14 03:20:02.462169
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2).filter(lambda x: x < 2) == ImmutableList.of(2)
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x > 2) == ImmutableList.of(3)
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x > 3) == ImmutableList.empty()
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x > -1) == ImmutableList.of(1, 2, 3)
    assert ImmutableList.of(1).filter(lambda x: x % 2 == 0) == ImmutableList.empty()


# Generated at 2022-06-14 03:20:08.083869
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x > 4) is None
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x > 3) == 4
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x > 1) == 2
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x > 3 and x < 4) is None
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x > 0) == 1
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x < 0) is None

# Generated at 2022-06-14 03:20:21.515893
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x < 2 ) == ImmutableList.of(1)
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x > 2 ) == ImmutableList.of(3)
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x == 3 ) == ImmutableList.of(3)
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x == 1 ) == ImmutableList.of(1)
    assert ImmutableList.of(1, 2, 3).filter(lambda x: True ) == ImmutableList.of(1, 2, 3)
    assert ImmutableList.of(1, 2, 3).filter(lambda x: False ) == ImmutableList.empty()

# Generated at 2022-06-14 03:20:30.944645
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    tasks = ImmutableList\
        .of(4)\
        .append(3)\
        .append(2)\
        .append(1)

    assert tasks.filter(lambda x: x % 2 == 0).to_list() == [4, 2]
    assert tasks.filter(lambda x: x % 3 == 0).to_list() == [3]
    assert tasks.filter(lambda x: x > 0).to_list() == [4, 3, 2, 1]
    assert tasks.filter(lambda x: x > 100).to_list() == []

    assert tasks == ImmutableList\
        .of(4)\
        .append(3)\
        .append(2)\
        .append(1)



# Generated at 2022-06-14 03:20:39.559871
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    empty_list = ImmutableList.empty()
    assert empty_list.filter(lambda x: x % 2 == 0) == ImmutableList.empty()

    list_with_even_numbers = ImmutableList.of(2, 4, 6, 8, 10)
    assert list_with_even_numbers.filter(lambda x: x % 2 == 0) == list_with_even_numbers

    list_with_odd_numbers = ImmutableList.of(1, 3, 5, 7, 9)
    assert list_with_odd_numbers.filter(lambda x: x % 2 == 0) == ImmutableList.empty()

    list_mixed = ImmutableList.of(1, 2, 3, 4, 5, 6, 7, 8, 9)

# Generated at 2022-06-14 03:20:47.872948
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # Arrange
    l = ImmutableList.of(1, 2, 3, 4)

    # Act
    odd_list = l.filter(lambda e: e % 2 == 0)

    # Assert
    assert odd_list == ImmutableList.of(2, 4)



# Generated at 2022-06-14 03:20:50.696915
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of('a', 'b', 'c').find(lambda x: x == 'b') == 'b'
    assert ImmutableList.of('a', 'b', 'c').find(lambda x: x == 'd') is None

# Generated at 2022-06-14 03:20:57.721264
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    immutable_list1 = ImmutableList.of(1, 2, 3)
    assert immutable_list1.filter(lambda x: x > 2) == ImmutableList.of(3)

    immutable_list2 = ImmutableList.of(1, 2, 3, 4, 5)
    assert immutable_list2.filter(lambda x: x != 3) == ImmutableList.of(1, 2, 4, 5)

    immutable_list3 = ImmutableList.of(1, 2, 3, 4, 5)
    assert immutable_list3.filter(lambda x: x % 2 == 0) == ImmutableList.of(2, 4)

    immutable_list4 = ImmutableList.of(1, 2, 3, 4, 5, 6, 7)
    assert immutable_list4.filter(lambda x: x > 10) == Immutable

# Generated at 2022-06-14 03:20:58.812246
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x > 2).to_list() == [3]


# Generated at 2022-06-14 03:21:00.829015
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    def test_find_none():
        assert ImmutableList.empty().find(lambda el: el) is None

    def test_find_some():
        assert ImmutableList.of(1, 2, 3, 4).find(lambda el: el == 4) == 4

    test_find_none()
    test_find_some()

# Generated at 2022-06-14 03:21:09.780972
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    l = ImmutableList.empty()

    def fn(x):
        return x <= 3

    results = [
        l.filter(fn),
        l.append(1).filter(fn),
        l.append(1).append(2).filter(fn),
        l.append(1).append(2).append(3).filter(fn),
        l.append(1).append(2).append(3).append(4).filter(fn),
        l.append(1).append(2).append(3).append(4).append(5).filter(fn)
    ]


# Generated at 2022-06-14 03:21:18.441851
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # Given
    test_args = [
        (ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4, ImmutableList(5))))), lambda x: x < 3, [1, 2]),
        (ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4, ImmutableList(5))))), lambda x: x < 0, []),
        (ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4, ImmutableList(5))))), lambda x: x > 3, [4, 5]),
        (ImmutableList(), lambda x: x < 3, [])
    ]

    # When/Then
    for arg, predicate, expected in test_args:
        assert arg.filter(predicate).to_list() == expected

# Generated at 2022-06-14 03:21:26.473455
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    test_data = [
        (1, 2, 3, 4, 5),
        (1, 2, 3, 4, 5, 6, 7),
        (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
    ]

    for data in test_data:
        result_list = ImmutableList.of(data[0], *data[1:])
        assert result_list.filter(lambda value: value > 3) == \
            ImmutableList.of(4, 5)

        if len(data) > 5:
            assert result_list.filter(lambda value: value > 3) == \
                ImmutableList.of(4, 5, 6, 7)
        

# Generated at 2022-06-14 03:21:31.287086
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # Given
    test_list = ImmutableList.of(
        10, 11, 12
    )
    # When
    filtered_list = test_list.filter(lambda i: i % 2 == 0)

    # Then
    assert filtered_list == ImmutableList.of(10, 12)
    assert test_list != filtered_list



# Generated at 2022-06-14 03:21:33.017262
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    expected_list = ImmutableList(2, ImmutableList(4))
    my_list = ImmutableList.of(1, 2, 3, 4).filter(lambda x: x % 2 == 0)
    assert my_list == expected_list



# Generated at 2022-06-14 03:21:48.796733
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4, 5, 6, 7).filter(lambda x: x % 2 == 1) == ImmutableList.of(1, 3, 5, 7)
    assert ImmutableList.of().filter(lambda x: x % 2 == 1) == ImmutableList.empty()
    assert ImmutableList.of(1).filter(lambda x: x % 2 == 1) == ImmutableList.of(1)
    assert ImmutableList.of().filter(lambda x: x % 2 == 1) == ImmutableList.of()
    assert ImmutableList.empty().filter(lambda x: x % 2 == 1) == ImmutableList.empty()


# Generated at 2022-06-14 03:21:55.941535
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    # tests for true
    assert ImmutableList.of(1, 2, 3) == ImmutableList.of(1, 2, 3)
    assert ImmutableList.empty() == ImmutableList.empty()

    # tests for false
    assert ImmutableList.of(1, 2, 3) != ImmutableList.of(1, 2, 4)
    assert ImmutableList.of(1, 2, 3) != ImmutableList.of(1, 3, 2)
    assert ImmutableList.of(1, 2, 3) != ImmutableList.of(1, 2)
    assert ImmutableList.of(1, 2, 3) != ImmutableList.of(1, 2, 3, 4)
    assert ImmutableList.of(1, 2, 3) != ImmutableList.empty()

# Generated at 2022-06-14 03:22:12.230459
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # Test when list is empty
    # Test when list is not empty
    list = ImmutableList.of(1, 2, 3)
    assert list.to_list() == [1, 2, 3]

    filtered_list = list.filter(lambda x: x % 2 == 0)
    assert filtered_list.to_list() == [2]

test_ImmutableList_filter()


# Generated at 2022-06-14 03:22:30.625188
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(0,1,2,3).filter(lambda x: x > 1) == ImmutableList.of(2,3)
    assert ImmutableList.of(0,1,2,3).filter(lambda x: x < 1) == ImmutableList.of(0)
    assert ImmutableList.of(0,1,2,3).filter(lambda x: x < 5) == ImmutableList.of(0,1,2,3)
    assert ImmutableList.of(0,1,2,3).filter(lambda x: x > 5) == ImmutableList.empty()


# Generated at 2022-06-14 03:22:37.029161
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.empty().filter(lambda x: x == 1) == ImmutableList.empty()

    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))).filter(lambda x: x % 2 == 0) == ImmutableList(2)
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))).filter(lambda x: x % 2 == 1) == ImmutableList(1, ImmutableList(3))
    assert ImmutableList(
        1,
        ImmutableList(
            2,
            ImmutableList(
                3,
                ImmutableList(
                    4,
                    ImmutableList(5)
                )
            )
        )
    ).filter(lambda x: x % 2 == 0) == ImmutableList(2, ImmutableList(4))
    assert Imm

# Generated at 2022-06-14 03:22:48.100311
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.empty().filter(
        lambda x: x < 3
    ) == ImmutableList.empty()

    assert ImmutableList.empty().filter(
        lambda x: x > 3
    ) == ImmutableList.empty()

    assert ImmutableList(1).filter(
        lambda x: x < 3
    ) == ImmutableList(1)

    assert ImmutableList(1).filter(
        lambda x: x > 3
    ) == ImmutableList.empty()

    assert ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4, ImmutableList(5))))) == ImmutableList.of(1, 2, 3, 4, 5)


# Generated at 2022-06-14 03:23:00.703330
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # Arrange
    list = ImmutableList.of(1, 2, 3)
    # Act
    element = list.find(lambda x: x > 2)
    # Assert
    assert element == 3



# Generated at 2022-06-14 03:23:07.680856
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():

    numbers = ImmutableList.of(1, 2, 3, 4, 5)
    immutalbe_even_numbers = numbers.filter(lambda x: x % 2 == 0)

    # We can not mutate instance of ImmutableList
    # immutalbe_even_numbers.append(10)
    # or
    # immutalbe_even_numbers.head = 10

    # The only way is to create new instance
    even_numbers = immutalbe_even_numbers.append(10)
    # or
    even_numbers = immutalbe_even_numbers.unshift(0)

    # The result is ImmutableList with even numbers
    assert [0, 2, 4, 10] == even_numbers.to_list()



# Generated at 2022-06-14 03:23:13.398115
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # Arrange
    lst = ImmutableList(1, ImmutableList(2, ImmutableList(3)))

    # Act & Assert
    assert lst.filter(lambda x: x >= 2) == ImmutableList(2, ImmutableList(3))
    assert lst.filter(lambda x: x < 2) == ImmutableList(1)
    assert lst.filter(lambda x: x < 0) == ImmutableList(is_empty=True)


# Generated at 2022-06-14 03:23:24.301711
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # Should return this one
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))).find(lambda x: x == 2) == 2
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))).find(lambda x: x == 3) == 3
    # Should return None
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))).find(lambda x: x == 4) is None



# Generated at 2022-06-14 03:23:58.778636
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList\
        .of(1, 2, 0, 4, 5)\
        .filter(lambda x: x > 0)\
        .reduce(lambda x, y: x + y, 0) == 12

    assert ImmutableList\
        .empty()\
        .filter(lambda x: x == 2)\
        .reduce(lambda x, y: x + y, 0) == 0



# Generated at 2022-06-14 03:24:06.245158
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # Create ImmutableList
    list1 = ImmutableList.empty()
    list2 = ImmutableList.empty().append(1)
    list3 = ImmutableList.empty().append(1).append(2)
    list4 = ImmutableList.empty().append(1).append(2).append(3)
    list5 = ImmutableList.empty().append(1).append(2).append(3).append(4)

    # Call method filter
    list1_filtered = list1.filter(lambda x: x > 1)
    list2_filtered = list2.filter(lambda x: x > 1)
    list3_filtered = list3.filter(lambda x: x > 1)
    list4_filtered = list4.filter(lambda x: x > 2)
    list5_filtered = list5.filter

# Generated at 2022-06-14 03:24:13.115452
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda x: x > 2).to_list() == [3, 4,] # pragma: no cover
    assert ImmutableList.empty().filter(lambda x: x > 2).to_list() == [] # pragma: no cover
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda x: x > 4).to_list() == [] # pragma: no cover


# Generated at 2022-06-14 03:24:18.777604
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x < 4) == ImmutableList.of(1, 2, 3)
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x < 2) == ImmutableList.of(1)
    assert ImmutableList.of().filter(lambda x: x < 2) == ImmutableList.empty()



# Generated at 2022-06-14 03:24:29.715914
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    empty_list = ImmutableList.empty()
    one_element_list = ImmutableList.of('test')
    multiple_elements_list = ImmutableList.of(
        1, 'test', {'key': 'value'}, False, [1, 'test'], ImmutableList.of(
            1, 2, 'test'
        ), ImmutableList.of(), ImmutableList.empty()
    )

    assert empty_list.filter(None) == ImmutableList.empty()
    assert one_element_list.filter(None) == ImmutableList.empty()
    assert multiple_elements_list.filter(None) == ImmutableList.empty()

    assert empty_list.filter(lambda x: True) == ImmutableList.empty()
    assert one_element_list.filter(lambda x: True) == ImmutableList

# Generated at 2022-06-14 03:24:31.982487
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    list1 = ImmutableList.of(1, 2, 3, 4, 5)
    assert list1.find(lambda x: x > 4) == 5



# Generated at 2022-06-14 03:24:34.722155
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4, 5)\
        .filter(lambda x: x > 3)\
        .to_list() == [4, 5]


# Generated at 2022-06-14 03:24:38.862297
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    l = ImmutableList.of(1, 2, 3, 4, 5)
    g = ImmutableList.of(1, 2, 3, 4, 5)
    assert l.filter(lambda x: x > 3) == g.filter(lambda x: x > 3)
    assert l.filter(lambda x: x > 100) == g.filter(lambda x: x > 100)
    assert l.filter(lambda x: x < 0) == g.filter(lambda x: x < 0)

# Generated at 2022-06-14 03:24:43.381186
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    ints = ImmutableList.of(1, 2, 3, 4, 5, 6, 7)
    even = ints.filter(lambda x: x % 2 == 0)
    assert even == ImmutableList.of(2, 4, 6)


# Generated at 2022-06-14 03:24:55.231393
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert (
        ImmutableList.of(1, 'a', 2, 'b')
        .find(lambda x: isinstance(x, int)) == 1
    )

    assert (
        ImmutableList.of(1, 'a', 2, 'b')
        .find(lambda x: isinstance(x, str)) == 'a'
    )

    assert (
        ImmutableList.of(1, 'a', 2, 'b')
        .find(lambda x: x > 1) == 2
    )

    assert (
        ImmutableList.of(1, 'a', 2, 'b')
        .find(lambda x: x > 2) is None
    )

    assert (
        ImmutableList.of(1, 'a', 2, 'b').find(lambda x: False) is None
    )




# Generated at 2022-06-14 03:25:20.348033
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(
        1, 2, 3, 4, 5
    ).filter(lambda el: el == 1) == ImmutableList(1)



# Generated at 2022-06-14 03:25:23.683845
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    test_find_with(lambda: None, None)
    test_find_with(lambda: ImmutableList.empty(), None)
    test_find_with(
        lambda: ImmutableList.of(1, 2, 3, 4),
        lambda val: val == 4,
        4
    )


# Generated at 2022-06-14 03:25:27.985215
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))).filter(lambda x: x < 3) == ImmutableList(1, ImmutableList(2))
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))).filter(lambda x: x < 3) != ImmutableList(1, ImmutableList(2, ImmutableList(3)))


# Generated at 2022-06-14 03:25:39.963062
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    empty_list = ImmutableList.empty()
    assert empty_list.filter(lambda x: x == None) == ImmutableList()
    assert empty_list.filter(lambda x: x == 'test') == ImmutableList()

    list1 = ImmutableList.of(1, 2, 4, 5, 6)
    assert list1.filter(lambda x: x%2 == 0) == ImmutableList.of(2, 4, 6)

    list2 = ImmutableList.of(1, 2, 3, 4)
    assert list2.filter(lambda x: x%2 == 0) == ImmutableList.of(2, 4)

if __name__ == '__main__':
    test_ImmutableList_filter()

# Generated at 2022-06-14 03:25:44.198603
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    my_list = ImmutableList.of(1, 2, 3, 4, 5)

    filtered_list = my_list.filter(lambda elem: elem % 2 == 0)

    assert filtered_list == ImmutableList.of(2, 4)


# Generated at 2022-06-14 03:25:54.300459
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x % 2 == 0) == ImmutableList.of(2)
    assert ImmutableList.of(2, 3, 4).filter(lambda x: x % 2 == 0) == ImmutableList.of(2, 4)
    assert ImmutableList.of(1, 3, 5).filter(lambda x: x % 2 == 0) == ImmutableList.empty()



# Generated at 2022-06-14 03:25:59.668461
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    values = ImmutableList.of(1, 2, 3, 4, 5)
    assert values.find(lambda x: x == 4) == 4
    assert values.find(lambda x: x == -1) is None
    assert values.find(lambda x: True) == 1

    empty_values = ImmutableList.empty()
    assert empty_values.find(lambda x: True) is None


# Generated at 2022-06-14 03:26:05.476856
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    fn_first_odd = lambda x: x % 2

    empty_list = ImmutableList.empty()
    assert empty_list.find(fn_first_odd) is None

    one_item_list = ImmutableList.of(1)
    assert one_item_list.find(fn_first_odd) == 1

    many_items_list = ImmutableList.of(1, 2, 3)
    assert many_items_list.find(fn_first_odd) == 1

    few_items_list = ImmutableList.of(1, 2)
    assert many_items_list.find(fn_first_odd) == 1


# Generated at 2022-06-14 03:26:09.474574
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4)))).filter(lambda x: x % 2 == 0) == ImmutableList(2, ImmutableList(4))
    assert ImmutableList().filter(lambda x: x % 2 == 0) == ImmutableList(is_empty=True)

# Generated at 2022-06-14 03:26:14.352333
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1).find(lambda x: x > 1) is None
    assert ImmutableList.of(1).find(lambda x: x >= 1) == 1
    assert ImmutableList.of(1, 2, 3).find(lambda x: x > 2) == 3
    assert ImmutableList.of(1, 2, 3).find(lambda x: x > 3) is None
