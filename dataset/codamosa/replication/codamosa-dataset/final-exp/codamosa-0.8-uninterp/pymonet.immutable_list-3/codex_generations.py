

# Generated at 2022-06-14 03:17:00.655704
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert (
        ImmutableList() == ImmutableList.empty()
    )

    assert (
        ImmutableList(1) == ImmutableList(1)
    )

    assert (
        ImmutableList(1).append(2) == ImmutableList(1, ImmutableList(2))
    )

    assert (
        ImmutableList(1).append(2).append(3) == ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    )

    assert (
        ImmutableList(1).append(2).append(3) == ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    )

    assert (
        ImmutableList(1).append(2).append(3) == ImmutableList(1).append(2).append(3)
    )


# Generated at 2022-06-14 03:17:03.574503
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4, 5) \
            .filter(lambda x: x > 3) \
            == ImmutableList.of(4, 5)



# Generated at 2022-06-14 03:17:09.095871
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.of(1).__eq__(ImmutableList.of(1))
    assert not ImmutableList.of(1).__eq__(ImmutableList.of(2))
    assert ImmutableList.of(1, 2).__eq__(ImmutableList.of(1, 2))
    assert not ImmutableList.of(1, 2).__eq__(ImmutableList.of(1, ImmutableList.empty()))
    assert not ImmutableList.of(1, 2).__eq__(ImmutableList.of(1, 2, 3))



# Generated at 2022-06-14 03:17:11.971667
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))) == ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))) == ImmutableList(1, ImmutableList(2, ImmutableList(3)))


# Generated at 2022-06-14 03:17:14.730284
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    a = ImmutableList(1)
    b = ImmutableList(1)
    c = ImmutableList(1, ImmutableList(2))
    d = ImmutableList(1, ImmutableList(2))

    # Assert
    assert a == b
    assert d == c
    assert not a == c


# Generated at 2022-06-14 03:17:22.645261
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    actual = ImmutableList.of(
        {
            'name': 'Adam', 'age': 32
        },
        {
            'name': 'Bob', 'age': 25
        },
        {
            'name': 'Charles', 'age': 21
        }
    ).filter(lambda it: it['age'] > 25)
    expected = ImmutableList.of({
            'name': 'Adam', 'age': 32
        })

    assert actual == expected


# Generated at 2022-06-14 03:17:32.950994
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    print('Test: ImmutableList find')

    assert ImmutableList.empty().find(lambda value: True) is None
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4)))).find(lambda value: value == 3) == 3
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4)))).find(lambda value: value == 5) is None

    print('Test: ImmutableList find # PASSED')



# Generated at 2022-06-14 03:17:35.391282
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.empty() == ImmutableList.empty()
    assert ImmutableList(2) == ImmutableList(2)
    assert ImmutableList(2, ImmutableList(3)) != ImmutableList(2)
    assert ImmutableList(2, ImmutableList(3)) != ImmutableList(3, ImmutableList(2))

# Generated at 2022-06-14 03:17:46.702582
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    list_0 = ImmutableList()
    list_1 = ImmutableList()

    assert list_0 == list_1
    assert list_0.is_empty and list_1.is_empty
    assert list_0 is not list_1

    list_2 = ImmutableList(0)
    list_3 = ImmutableList(0)

    assert list_2 == list_3
    assert list_2.to_list() == [0] and list_3.to_list() == [0]
    assert list_2 is not list_3

    list_4 = ImmutableList(0)
    list_5 = ImmutableList(1)

    assert list_4 != list_5
    assert list_4.to_list() == [0] and list_5.to_list() == [1]
    assert list_4

# Generated at 2022-06-14 03:17:49.266272
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3)\
        .filter(lambda n: n>1)\
        .filter(lambda n: n<3)\
        == ImmutableList.of(2)


# Generated at 2022-06-14 03:18:01.539116
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    from fixtures import ImmutableListTestFixture

    assert ImmutableList \
        .of(1, 2, 3) \
        .filter(ImmutableListTestFixture.is_greater_than_10) == ImmutableList.empty()

    assert ImmutableList \
        .of(2, 3, 4, 5, 6) \
        .filter(ImmutableListTestFixture.is_even) == ImmutableList.of(2, 4, 6)


# Generated at 2022-06-14 03:18:04.220176
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.of(1, 2, 3) == ImmutableList(1, ImmutableList(2, ImmutableList(3)))


# Generated at 2022-06-14 03:18:08.384627
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    res = ImmutableList(2).filter(lambda x: x > 1)
    expected = ImmutableList(2)
    assert res == expected


test_ImmutableList_filter()


# Generated at 2022-06-14 03:18:16.929129
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    immutable_list = ImmutableList.of(1, 2, 3, 4, 5)
    assert immutable_list.filter(lambda x: x % 2 == 0).to_list() == [2, 4]
    assert immutable_list.filter(lambda x: x % 2 == 1).to_list() == [1, 3, 5]
    assert immutable_list.filter(lambda x: x == 0).to_list() == []
    assert immutable_list.filter(lambda x: x < 0).to_list() == []


# Generated at 2022-06-14 03:18:21.969861
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # Arrange
    list = ImmutableList.of(
        1,
        2,
        3,
        4,
        5
    )

    # Act
    filtered = list.filter(lambda x: x < 4)

    # Assert
    assert filtered == ImmutableList.of(1, 2, 3)
    

# Generated at 2022-06-14 03:18:24.915495
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    l = ImmutableList.of(1, 2, 3, 4, 5, 6)
    result = l.filter(lambda x: x == 1)
    assert result == ImmutableList.of(1)


# Generated at 2022-06-14 03:18:29.671281
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    # Arrange
    first = ImmutableList.of(10, 'abc', True)
    second = ImmutableList.of(10, 'abc', True)

    # Act
    expected = True
    actual = first == second

    # Assert
    assert expected == actual
    print('Method __eq__ passed')
    
    

# Generated at 2022-06-14 03:18:40.296982
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList() == ImmutableList()
    assert ImmutableList.of(1, 2) == ImmutableList.of(1, 2)
    assert ImmutableList.of(1, 2) != ImmutableList.of(1, 2, 3)
    assert ImmutableList.of(1, 2) != ImmutableList.of(1, 3)
    assert ImmutableList.of(1, 2) != ImmutableList.of(2, 2)
    assert ImmutableList.of(1, 2) != ImmutableList.of(1, 2, 3, 4)
    assert ImmutableList.of(1, 2) != ImmutableList.of(2, 1)

# Generated at 2022-06-14 03:18:47.836002
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 4) == 4
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 10) is None
    assert ImmutableList.empty().find(lambda x: x == 4) is None


# Generated at 2022-06-14 03:19:07.985605
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4, 5, 6).filter(lambda x: x % 2 != 0) == ImmutableList.of(1, 3, 5)
    assert ImmutableList.of(1, 2, 3, 4, 5, 6).filter(lambda x: x % 2 == 0) == ImmutableList.of(2, 4, 6)
    assert ImmutableList.of(False, False, True, False, False, True).filter(lambda x: x) == ImmutableList.of(True, True)
    assert ImmutableList.empty().filter(lambda x: True) == ImmutableList.empty()
    assert ImmutableList.of('foo', 'bar', 'baz').filter(lambda x: x in ['foo', 'bar']) == ImmutableList.of('foo', 'bar')

# Unit

# Generated at 2022-06-14 03:19:23.515973
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 2) == 2
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 3) == 3
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 1) == 1
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 5) == 5
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 6) is None
    assert ImmutableList.empty().find(lambda x: x == 1) is None


# Generated at 2022-06-14 03:19:26.932592
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 2) == 2
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x > 4) == 5


# Generated at 2022-06-14 03:19:32.848937
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1,2,3,4,5).filter(lambda x: x > 2).to_list() == [3,4,5]
    assert ImmutableList.of(1,2,3,4,5).filter(lambda x: x < 0).to_list() == []


test_ImmutableList_filter()

# Generated at 2022-06-14 03:19:38.692810
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    list_1 = ImmutableList.of(4, 3, 1, 7)
    list_2 = ImmutableList.of(4, 3, 1, 7)
    list_3 = ImmutableList.of(1, 4, 7, 3)
    list_4 = ImmutableList.of(4, 3, 1)
    assert list_1 == list_2
    assert list_1 != list_3
    assert list_1 != list_4


test_ImmutableList___eq__()



# Generated at 2022-06-14 03:19:43.931042
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list_ = ImmutableList.of(1, 2, 3, 4)
    new_list = list_.filter(lambda x: x % 2 == 0)

    assert new_list.head == 2
    assert new_list.tail.head == 4
    assert new_list.tail.tail is None



# Generated at 2022-06-14 03:19:46.907104
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    result = ImmutableList.of('a', 'b') == ImmutableList.of('a', 'b')
    expected = True
    assert result == expected



# Generated at 2022-06-14 03:19:50.724784
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    empty_list = ImmutableList(is_empty=True)
    list_with_elements = ImmutableList.of(1, 2, 3, 4, 5)
    not_equal_instace = list()

    assert empty_list == ImmutableList(is_empty=True)
    assert not empty_list == list_with_elements
    assert list_with_elements == ImmutableList.of(1, 2, 3, 4, 5)

    with pytest.raises(ValueError):
        empty_list == not_equal_instace


# Generated at 2022-06-14 03:20:00.026612
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    list1 = ImmutableList.of(1, 2)
    list2 = ImmutableList.empty()

    assert list1.find(lambda e: e == 1) == 1
    assert list1.find(lambda e: e == 3) is None
    assert list2.find(lambda e: e == 4) is None
    assert list2.find(lambda e: e == 1) is None



# Generated at 2022-06-14 03:20:04.236038
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1).find(lambda x: x == 1) == 1

    list = ImmutableList.of(1, 2, 3)
    assert list.find(lambda x: x == 2) == 2
    assert list.find(lambda x: x > 3) is None
    assert list.find(lambda x: x < 0) is None



# Generated at 2022-06-14 03:20:07.537768
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # Given
    mlist = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    # When
    n = mlist.find(lambda x: x == 2)
    # Then
    assert(n == 2)


# Generated at 2022-06-14 03:20:26.781405
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.of(1) == ImmutableList(1)
    assert ImmutableList.of(1, 2, 3, 4) == ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4))))
    assert ImmutableList.of(1, 2, 3, 4) != ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(5))))


# Generated at 2022-06-14 03:20:40.450602
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    """
    Method filter should return new Maybe with only those elements that
    passes into argument function

    :returns: None
    :rtype: None
    """
    assert ImmutableList.of(0, 1, 2, 3, 4, 5).filter(lambda x: x % 2 == 0) == \
        ImmutableList.of(0, 2, 4)
    assert ImmutableList.empty().filter(lambda x: False) == ImmutableList.empty()
    assert ImmutableList.of(0).filter(lambda x: True) == \
        ImmutableList.of(0)
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x % 2 == 0) == ImmutableList.of(2)

# Generated at 2022-06-14 03:20:47.146688
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    item1 = ImmutableList.of('Test1', 'Test2', 'Test3')
    item2 = ImmutableList.of('Test1', 'Test2', 'Test3')
    assert item1 == item2
    item1 = ImmutableList.of('Test1', 'Test2', 'Test3')
    item2 = ImmutableList.of('Test1', 'Test2', 'Test4')
    assert item1 != item2

# Generated at 2022-06-14 03:20:59.048626
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    # arrange
    empty_list = ImmutableList.of(None)
    empty_list_1 = None
    empty_list_2 = ImmutableList(is_empty=True)
    empty_list_3 = ImmutableList(is_empty=True)
    list_1 = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    list_2 = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    list_3 = ImmutableList(1, ImmutableList(2, ImmutableList(3)), is_empty=True)
    list_4 = ImmutableList(1, ImmutableList(2, ImmutableList(3)), is_empty=True)
    list_5 = ImmutableList(1, ImmutableList(2, ImmutableList(4)))
    list_6

# Generated at 2022-06-14 03:21:06.760676
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.of(1, 2, 3) == ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    assert ImmutableList.of(1, 2, 3) == ImmutableList.of(1, 2, 3)
    assert ImmutableList.of(1, 2, 3) != ImmutableList.of(3, 2, 1)
    assert ImmutableList.of(1, 2, 3) != ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4))))
    assert ImmutableList.of(1, 2, 3) != ImmutableList(1, ImmutableList(2))
    assert ImmutableList.of(1, 2, 3) != ImmutableList(1)

# Generated at 2022-06-14 03:21:16.158596
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(0, 1, -2, 3, -4, 5).filter(lambda n: n < 0) == \
        ImmutableList(-2, -4)

    assert ImmutableList.of(0, 1, -2, 3, -4, 5).filter(lambda n: n > 100) == \
        ImmutableList(is_empty=True)

    assert ImmutableList.of(0, 1, -2, 3, -4, 5).filter(lambda n: n*n < 10) == \
        ImmutableList(1, -2, 3)

    assert ImmutableList.of(0).filter(lambda n: n*n < 10) == \
        ImmutableList(0)


# Generated at 2022-06-14 03:21:22.075054
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList() == ImmutableList()
    assert ImmutableList().__eq__('any') is False
    assert ImmutableList(0, 1, 2) == ImmutableList(0, 1, 2)
    assert ImmutableList(0, 1, 2) == ImmutableList(0, 1)
    assert ImmutableList(0, 1, 2) != ImmutableList(0, 2, 1)
    assert ImmutableList(0, 1, 2) != ImmutableList(0, 2)



# Generated at 2022-06-14 03:21:33.293162
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.empty() == ImmutableList.empty()
    assert ImmutableList.of('foo') == ImmutableList.of('foo')
    assert ImmutableList.of('foo', ImmutableList.of('bar')) == ImmutableList.of('foo', ImmutableList.of('bar'))

    assert not ImmutableList.of('foo') == ImmutableList.of('bar')
    assert ImmutableList.of('foo', ImmutableList.of('bar')) != ImmutableList.of('foo', ImmutableList.of('baz'))
    assert ImmutableList.of('foo', ImmutableList.of('bar', ImmutableList.of('baz'))) != ImmutableList.of('foo', ImmutableList.of('baz'))  # noqa: E501



# Generated at 2022-06-14 03:21:43.324972
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(5,5,4,4,3,3,2,2,1,1).find(lambda x: x == 1) == 1
    assert ImmutableList.of(5,5,4,4,3,3,2,2,1,1).find(lambda x: x == 2) == 2
    assert ImmutableList.of(5,5,4,4,3,3,2,2,1,1).find(lambda x: x == 3) == 3
    assert ImmutableList.of(5,5,4,4,3,3,2,2,1,1).find(lambda x: x == 4) == 4
    assert ImmutableList.of(5,5,4,4,3,3,2,2,1,1).find(lambda x: x == 5) == 5

# Generated at 2022-06-14 03:21:47.461131
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    if ImmutableList() == ImmutableList():
        print('✔️  Success')
    else:
        print('❌ ❌ ❌  Fail')

    if isinstance(ImmutableList(1), ImmutableList) \
            and ImmutableList(1) == ImmutableList(1):
        print('✔️  Success')
    else:
        print('❌ ❌ ❌  Fail')

    if isinstance(ImmutableList(1, ImmutableList(2)), ImmutableList) \
            and ImmutableList(1, ImmutableList(2)) == ImmutableList(1, ImmutableList(2)):
        print('✔️  Success')
    else:
        print('❌ ❌ ❌  Fail')


# Generated at 2022-06-14 03:22:33.097805
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.empty() == ImmutableList.empty()
    assert ImmutableList.of(1) == ImmutableList.of(1)
    assert ImmutableList.of(1, 2) == ImmutableList.of(1, 2)
    assert ImmutableList.of(1, 2, 3) == ImmutableList.of(1, 2, 3)

    assert ImmutableList.empty() != ImmutableList.of(1)
    assert ImmutableList.empty() != ImmutableList.of(1, 2)
    assert ImmutableList.empty() != ImmutableList.of(1, 2, 3)
    assert ImmutableList.of(1) != ImmutableList.of(2)
    assert ImmutableList.of(1, 2) != ImmutableList.of(1, 3)
    assert ImmutableList.of

# Generated at 2022-06-14 03:22:36.431872
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    list_ = ImmutableList.of('a', 'b', 'c')

    assert list_.find(lambda x: x == 'c') == 'c'
    assert list_.find(lambda x: x == 'b') == 'b'
    assert list_.find(lambda x: x == 'a') == 'a'
    assert list_.find(lambda x: x == 'd') is None

# Generated at 2022-06-14 03:22:38.864622
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    l1 = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    l2 = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    assert l1 == l2



# Generated at 2022-06-14 03:22:49.167220
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # given
    test_cases = [
        {
            'input': [0, 0, 0, 1, 1, 1, 2, 2, 2],
            'expected': [0, 1, 2],
        },
        {
            'input': [0, 1, 2, 3, 4, 5, 6, 7, 8],
            'expected': [3, 5],
        }
    ]
    
    for case in test_cases:
        input_list = ImmutableList.of(*case['input'])
        expected = case['expected']
        actual = []
        for number in range(len(input_list)):
            actual.append(
                input_list.find(lambda x: x == number)
            )
        
        assert expected == actual

# Generated at 2022-06-14 03:22:54.806949
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list_immutable = ImmutableList.of(1, 2, 3, 4, 5, 6, 7, 8, 9)

    result = list_immutable.filter(lambda x: x % 2 == 0)

    assert ImmutableList.of(2, 4, 6, 8) == result

    result = list_immutable.filter(lambda x: x % 2 != 0)

    assert ImmutableList.of(1, 3, 5, 7, 9) == result



# Generated at 2022-06-14 03:23:03.093925
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    my_list = ImmutableList.of(2, 3, 4, 6, 10)
    assert my_list.find(lambda x: x % 2 == 0) == 2
    assert my_list.find(lambda x: x % 7 == 0) is None
    assert my_list.find(lambda x: x == 10) == 10


# Generated at 2022-06-14 03:23:10.132780
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList(is_empty=True) == ImmutableList(is_empty=True)  # Case when both lists are empty
    assert not ImmutableList(1) == ImmutableList(2)  # Case is head is not equal
    assert not ImmutableList(1) == ImmutableList(2, ImmutableList(1))  # Case when tail is not equal
    assert ImmutableList(1) == ImmutableList(1, ImmutableList(2))  # Case when both lists are equal
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))) == ImmutableList(1, ImmutableList(2, ImmutableList(3)))  # Case when both lists are equal


# Generated at 2022-06-14 03:23:16.031453
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(lambda x: x % 2 == 0) == ImmutableList.of(2, 4)
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(lambda x: x % 2 != 0) == ImmutableList.of(1, 3, 5)
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(lambda x: x > 0) == ImmutableList.of(1, 2, 3, 4, 5)
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(lambda x: x < 0) == ImmutableList.empty()

# Generated at 2022-06-14 03:23:25.768145
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    list1 = ImmutableList.of(1, 2)
    list2 = ImmutableList.of(1, 2)
    list3 = ImmutableList.of(1, 3)
    list4 = ImmutableList.of(2, 3)
    list5 = ImmutableList.empty()
    list6 = ImmutableList.empty()

    assert list1 == list2
    assert list1 != list3
    assert list1 != list4
    assert list5 == list6
    assert list1 != list5
    assert list1 != 1
    assert list1 != list6


# Generated at 2022-06-14 03:23:33.213618
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList(1, ImmutableList(2), ImmutableList(3)).filter(lambda x: True).to_list() == [1, 2, 3]
    assert ImmutableList(1, ImmutableList(2), ImmutableList(3)).filter(lambda x: False).to_list() == []
    assert ImmutableList(1, ImmutableList(2), ImmutableList(3)).filter(lambda x: x > 1).to_list() == [2, 3]
    assert ImmutableList(1, ImmutableList(2), ImmutableList(3)).filter(lambda x: x > 3).to_list() == []
    assert ImmutableList.empty().filter(lambda x: True).to_list() == []


# Generated at 2022-06-14 03:24:25.582798
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x == 3) == 3
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x == 5) is None
    assert ImmutableList.of(1).find(lambda x: x == 1) == 1
    assert ImmutableList(is_empty=True).find(lambda x: x == 1) is None

# Generated at 2022-06-14 03:24:30.188630
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    numbers = ImmutableList.of(10, 20, 30, 40, 50, 60)
    pick_even = lambda num: num % 2 == 0
    assert numbers.find(pick_even) == 10

    pick_even_greater_than_20 = lambda num: num % 2 == 0 and num > 20
    assert numbers.find(pick_even_greater_than_20) == 30

    assert numbers.find(lambda _: False) is None
    assert numbers.find(lambda _: True) == 10

# Generated at 2022-06-14 03:24:34.054823
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # arrange
    elements = [1, 2, 3, 4, 5]
    list_to_test = ImmutableList.of(*elements)

    # act
    result = list_to_test.find(lambda x: x == 5)

    # assert
    assert result == 5

# Generated at 2022-06-14 03:24:39.200767
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    integer_list = ImmutableList.of(1, 2, 3)

    assert integer_list.filter(lambda x: x == 1).to_list() == [1]
    assert integer_list.filter(lambda x: x > 1).to_list() == [2, 3]
    assert integer_list.filter(lambda x: x > -1).to_list() == [1, 2, 3]
    assert integer_list.filter(lambda x: x < 0).to_list() == []
    assert integer_list.filter(lambda x: x < 5).to_list() == [1, 2, 3]


# Generated at 2022-06-14 03:24:43.333572
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    immutable_list = ImmutableList.of(1, 2, 3, 4, 5)
    filtered = immutable_list.filter(lambda x: x > 3)
    assert filtered.to_list() == [4, 5]


# Generated at 2022-06-14 03:24:49.714184
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    test_list = ImmutableList.of(1, 2, 3)

    assert test_list.find(lambda x: x < 2) == 1
    assert test_list.find(lambda x: x > 4) is None
    assert test_list.find(lambda x: x % 2 == 0) == 2
    assert test_list.find(lambda x: x % 2 == 1) == 1

# Generated at 2022-06-14 03:24:56.093614
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # Given
    iList = ImmutableList.of(1, 2, 3)

    # When
    fn_filter = lambda x: x > 1
    iList_filtered = iList.filter(fn_filter)

    # Then
    assert isinstance(iList, ImmutableList)
    assert isinstance(iList_filtered, ImmutableList)
    assert iList_filtered == ImmutableList.of(2, 3)


# Generated at 2022-06-14 03:25:07.282930
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # __init__(self) -> ImmutableList
    filter_lambda = lambda x: x % 2 == 0
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    l1 = ImmutableList.of(*input_list)
    l2 = l1.filter(filter_lambda)
    assert isinstance(l2, ImmutableList)
    assert isinstance(l2, Generic)
    assert all(filter_lambda, l2)
    assert not all(lambda x: x % 2 != 0, l2)
    assert l2 == ImmutableList.of(*filter(filter_lambda, input_list))
    assert not l2 == ImmutableList.of(*filter(lambda x: x % 2 != 0, input_list))
    assert l1 != l2


# Unit test

# Generated at 2022-06-14 03:25:21.116975
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.empty().filter(lambda x: x == 1) == ImmutableList.empty()
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x == 1) == ImmutableList.of(1)
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x == 2) == ImmutableList.of(2)
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda x: x == 2) == ImmutableList.of(2)
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda x: x == 3) == ImmutableList.of(3)
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda x: x == 4) == ImmutableList.of(4)


# Unit

# Generated at 2022-06-14 03:25:26.674801
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.empty().filter(lambda x: x is not None) == ImmutableList.empty()
    assert ImmutableList(1).filter(lambda x: x is not None) != ImmutableList.empty()

    assert ImmutableList.of(1, 2, 3).filter(lambda x: x != 3) == ImmutableList.of(1, 2)
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x != 3) != ImmutableList.of(3)

test_ImmutableList_filter()

