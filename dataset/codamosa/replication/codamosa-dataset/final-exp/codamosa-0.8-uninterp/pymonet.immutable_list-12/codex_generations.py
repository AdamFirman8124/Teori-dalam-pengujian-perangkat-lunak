

# Generated at 2022-06-14 03:16:57.335588
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    empty_list = ImmutableList.empty()
    assert empty_list.find(lambda val: val == 1) is None

    int_list = ImmutableList(1)
    assert int_list.find(lambda val: val == 1) == 1

    int_list = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    assert int_list.find(lambda val: val == 1) == 1
    assert int_list.find(lambda val: val == 2) == 2
    assert int_list.find(lambda val: val == 3) == 3



# Generated at 2022-06-14 03:17:03.068572
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.empty() == ImmutableList.empty()
    assert ImmutableList(2) == ImmutableList(2)
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))) == ImmutableList(
        1, ImmutableList(2, ImmutableList(3)))
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))) \
        != ImmutableList(2, ImmutableList(2, ImmutableList(3)))



# Generated at 2022-06-14 03:17:06.485311
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    imm_list = ImmutableList.of(1, 2, 3, 4)

    assert imm_list == ImmutableList.of(1, 2, 3, 4)
    assert imm_list != ImmutableList.of(1, 2, 3)
    assert imm_list != ImmutableList.empty()


# Generated at 2022-06-14 03:17:15.490115
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 2) == 2
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 5) == None
    assert ImmutableList.of(1).find(lambda x: x == 1) == 1
    assert ImmutableList.of(1).find(lambda x: x == 2) == None

# Generated at 2022-06-14 03:17:20.892224
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    data = ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4, ImmutableList(5)))))
    assert data.filter(lambda i: i >= 3).to_list() == [3, 4, 5]
    
    

# Generated at 2022-06-14 03:17:25.250211
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    def is_positive(value):
        return value > 0

    assert ImmutableList.of(-1, 2, 0).filter(is_positive) == ImmutableList.of(2)
    assert ImmutableList.of(2, 3).filter(is_positive) == ImmutableList.of(2, 3)
    assert ImmutableList.of(-1, -2).filter(is_positive) == ImmutableList.empty()


# Generated at 2022-06-14 03:17:35.588131
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList(1) == ImmutableList(1)
    assert ImmutableList("foo") == ImmutableList("foo")
    assert ImmutableList("foo", ImmutableList("bar")) == ImmutableList("foo", ImmutableList("bar"))
    assert ImmutableList("foo", ImmutableList("bar"), ImmutableList("baz")) == ImmutableList("foo", ImmutableList("bar"), ImmutableList("baz"))
    assert ImmutableList(1) != ImmutableList(None)
    assert ImmutableList(1) != ImmutableList(None)
    assert ImmutableList(ImmutableList().append(1), ImmutableList(1)) != ImmutableList(ImmutableList().append(1), ImmutableList(1))

# Generated at 2022-06-14 03:17:42.990053
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(2, 3, 5, 7, 11).find(lambda x: x % 2 == 0) == 2
    assert ImmutableList.of(2, 3, 5, 7, 11).find(lambda x: x % 2 != 0) == 3
    assert ImmutableList.empty().find(lambda x: x % 2 == 0) is None
    assert ImmutableList.of(2, 3, 5, 7, 11).find(lambda x: x > 10) == 11


# Generated at 2022-06-14 03:17:50.605638
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():

    m_list = ImmutableList.of(1, 2, 3)
    assert m_list.find(lambda x: x == 2) == 2
    assert m_list.find(lambda x: x > 2) == 3
    assert m_list.find(lambda x: x == 5) is None
    assert m_list.find(lambda x: x < 0) is None



# Generated at 2022-06-14 03:17:57.095846
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList(1, ImmutableList(2), is_empty=False).filter(lambda value: value % 2 == 0) == ImmutableList(2, is_empty=False)
    assert ImmutableList(1, ImmutableList(2), is_empty=False).filter(lambda value: value % 2 == 0) == ImmutableList(2, is_empty=False)
    assert ImmutableList(1, ImmutableList(2), is_empty=False).filter(lambda value: value % 2 == 0) != ImmutableList(1, ImmutableList(2), is_empty=False)

# Generated at 2022-06-14 03:18:18.418265
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.empty().find(lambda x: True) == None
    assert ImmutableList(1).find(lambda x: True) == 1
    assert ImmutableList(1).find(lambda x: False) == None
    assert ImmutableList(1, ImmutableList(2)).find(lambda x: x == 1) == 1
    assert ImmutableList(1, ImmutableList(2)).find(lambda x: x == 2) == 2
    assert ImmutableList(1, ImmutableList(2)).find(lambda x: x == 3) == None
    assert ImmutableList(1, ImmutableList(2)).find(lambda x: x > 0) == 1
    assert ImmutableList(1, ImmutableList(2)).find(lambda x: x % 2 == 0) == 2

# Generated at 2022-06-14 03:18:29.429250
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.empty().filter(
        lambda x: x > 0
        ) == ImmutableList.empty()
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(
        lambda x: x > 0
        ) == ImmutableList.of(1, 2, 3, 4, 5)
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(
        lambda x: x > 2
        ) == ImmutableList.of(3, 4, 5)
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(
        lambda x: x > 5
        ) == ImmutableList.empty()


ImmutableList.of(1, 2, 3, 4, 5).filter(
    lambda x: (x > 2)
    )

# Generated at 2022-06-14 03:18:34.230418
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x > 1) == ImmutableList.of(2, 3)


test_ImmutableList_filter()

# Generated at 2022-06-14 03:18:38.695028
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    input = [1, 2, 3, 4, 5]
    list = ImmutableList.of(*input)
    filtered = list.filter(lambda x: x % 2 == 0)

    assert filtered == ImmutableList.of(2, 4)
    assert list == ImmutableList.of(*input)


# Generated at 2022-06-14 03:18:43.863475
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList(1) == ImmutableList(1)
    assert ImmutableList(1, ImmutableList(2)) == ImmutableList(1, ImmutableList(2))
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))) == ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4)))) == ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4))))
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4)))) == ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4, ImmutableList()))))

# Generated at 2022-06-14 03:18:48.073828
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    actual = ImmutableList.of('a', 'b', 'c')
    expected = ImmutableList.of('a', 'b', 'c')
    assert actual == expected


# Generated at 2022-06-14 03:18:56.359342
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.empty() == ImmutableList.empty(), 'ImmutableList: empty() should be equals to empty()'
    assert ImmutableList.empty() != ImmutableList(1), 'ImmutableList: empty() should not be equals to one element'
    assert ImmutableList.of(1) == ImmutableList(1), 'ImmutableList: one element should be equal to equal one element'
    assert ImmutableList.of(1, 2, 3) == ImmutableList.of(1, 2, 3), 'ImmutableList: of should create equal list'
    assert ImmutableList.of(1) == ImmutableList.of(1, 2, 3), 'ImmutableList: of should create equal list'



# Generated at 2022-06-14 03:19:05.483673
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list_ = ImmutableList.empty()
    assert len(list_) == 0

    list_ = list_.append(1)
    assert len(list_) == 1
    assert list_.to_list() == [1]

    list_ = list_.append(2)
    assert len(list_) == 2
    assert list_.to_list() == [1, 2]

    list_ = list_.append(3)
    assert len(list_) == 3
    assert list_.to_list() == [1, 2, 3]

    list_ = list_.unshift(0)
    assert len(list_) == 4
    assert list_.to_list() == [0, 1, 2, 3]

    list_ = list_.map(lambda x: x ** 2)

# Generated at 2022-06-14 03:19:16.230143
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.empty().filter(lambda x: True) == ImmutableList.empty()
    assert ImmutableList.of('A', 'B', 'A', 'C').filter(lambda x: x == 'A') == ImmutableList.of('A', 'A')
    assert ImmutableList.of('A', 'B', 'A', 'C').filter(lambda x: x == 'B') == ImmutableList.of('B')
    assert ImmutableList.of('A', 'B', 'A', 'C').filter(lambda x: x == 'C') == ImmutableList.of('C')
    assert ImmutableList.of('A', 'B', 'A', 'C').filter(lambda x: x != 'A') == ImmutableList.of('B', 'C')

# Generated at 2022-06-14 03:19:21.784927
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList[int].empty() == ImmutableList[int].empty()
    assert ImmutableList[int].of(1, 2, 3) == ImmutableList[int].of(1, 2, 3)
    assert ImmutableList[int].of(1, 2, 3) != ImmutableList[int].of(1, 2)

# Generated at 2022-06-14 03:19:44.560928
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    immutable_list = ImmutableList.of(1, 2, 3, 4, 5)
    assert immutable_list.find(lambda element: element % 2 == 0) == 2

# Generated at 2022-06-14 03:19:47.058465
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x > 2).to_list() == [3]



# Generated at 2022-06-14 03:19:56.070709
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.empty() == ImmutableList.empty()
    assert ImmutableList.of(1) == ImmutableList.of(1)
    assert ImmutableList.of(1, 2) == ImmutableList.of(1, 2)
    assert ImmutableList.of(4, 3, 2, 1) == ImmutableList.of(4, 3, 2, 1)
    assert ImmutableList.of(1, 2) == ImmutableList.of(1, 2)

    assert ImmutableList.of(1) != ImmutableList.of(2)
    assert ImmutableList.of(1, 2) != ImmutableList.of(1, 3)
    assert ImmutableList.of(1, 2) != ImmutableList.of(2, 1)
    assert ImmutableList.of(1, 2) != Immutable

# Generated at 2022-06-14 03:19:59.745494
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    a = ImmutableList.of(1, 2, 3, 4)
    b = ImmutableList.of(1, 2, 3, 4)
    c = ImmutableList.of(1, 2, 3)

    assert a == b
    assert a != c


# Generated at 2022-06-14 03:20:02.834793
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.empty().find(lambda x: x > 1) == None
    assert ImmutableList.of(2, 3).find(lambda x: x > 1) == 2
    assert ImmutableList.of(2, 3).find(lambda x: x > 10) == None

# Generated at 2022-06-14 03:20:08.587493
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list_ = ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4))))
    assert list_.filter(lambda x: x < 2) == ImmutableList(1)
    assert list_.filter(lambda x: x > 10) == ImmutableList.empty()
    assert list_.filter(lambda x: x < 3) == ImmutableList(1, ImmutableList(2))
    print('Test for method `filter` of class ImmutableList is successfully passed!')

test_ImmutableList_filter()


# Generated at 2022-06-14 03:20:21.715870
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(lambda x: x % 3 == 0) == ImmutableList.of(3)
    assert ImmutableList.of(1, 2, 3, 4, 5, 6, 7, 8, 9).filter(lambda x: x % 2 == 0) == ImmutableList.of(2, 4, 6, 8)
    assert ImmutableList.of(7, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1).filter(lambda x: x % 2 == 0) == ImmutableList.of(2, 4, 6, 8, 10)
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(lambda x: x % 3 == 0) != ImmutableList.of(6)
    assert ImmutableList.of

# Generated at 2022-06-14 03:20:25.947309
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(2).filter(lambda x: x == 2) == ImmutableList.of(2)
    assert ImmutableList.of(1, 2).filter(lambda x: x == 2) == ImmutableList.of(2)
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x == 2) == ImmutableList.of(2)
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x == 4) == ImmutableList.empty()
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x == 1 or x == 3) == ImmutableList.of(1, 3)
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x == 0) == ImmutableList.empty()
    assert ImmutableList

# Generated at 2022-06-14 03:20:37.733918
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.empty() == ImmutableList.empty()
    assert ImmutableList.of(1) == ImmutableList.of(1)
    assert ImmutableList.of(1) != ImmutableList.of(2)
    assert ImmutableList.of(1, 2, 3) != ImmutableList.of(1, 2)
    assert ImmutableList.of(1, 2) != ImmutableList.of(1)
    assert ImmutableList.of(1) != ImmutableList.empty()


# Generated at 2022-06-14 03:20:39.781052
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.of(1, 2) == ImmutableList.of(1, 2)
    assert ImmutableList.empty() == ImmutableList.empty()

# Generated at 2022-06-14 03:21:18.687023
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList() == ImmutableList()
    assert ImmutableList.of(1) == ImmutableList.of(1)
    assert not ImmutableList.of(1) == ImmutableList()

# Generated at 2022-06-14 03:21:22.733676
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    integers = ImmutableList.of(1, 2, 3, 4)
    filtered = integers.filter(lambda x: x >= 2)

    assert filtered.to_list() == [2, 3, 4]



# Generated at 2022-06-14 03:21:28.494157
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    a = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    b = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    c = ImmutableList(3, ImmutableList(2, ImmutableList(1)))
    assert a == b
    assert not a == c

# Generated at 2022-06-14 03:21:31.798722
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList(1, ImmutableList(2)) == ImmutableList(1, ImmutableList(2))
    assert ImmutableList(42, ImmutableList(2)) != ImmutableList(1, ImmutableList(2))


# Generated at 2022-06-14 03:21:37.025838
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # None
    assert ImmutableList().find(lambda x: x == 0) is None
    # 2
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))).find(lambda x: x == 2) == 2
    # 3
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))).find(lambda x: x == 3) == 3

test_ImmutableList_find()

# Generated at 2022-06-14 03:21:40.764459
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list_ = ImmutableList.of(1, 2, 3)
    new_list = list_.filter(lambda x: x == 2)

    assert new_list == ImmutableList.of(2)

# Generated at 2022-06-14 03:21:46.109784
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4, 5, 6).filter(lambda x: x % 2 == 0).to_list() == [2, 4, 6]
    assert ImmutableList.of(1, 2, 3, 4, 5, 6).filter(lambda x: x % 2 != 0).to_list() == [1, 3, 5]
    assert ImmutableList.empty().filter(lambda x: x % 2 != 0) == ImmutableList.empty()


# Generated at 2022-06-14 03:21:54.485613
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    il1 = ImmutableList.of(1,2,3)
    il2 = ImmutableList.of(1,2,3)
    il3 = ImmutableList.of(2,3,4)

    assert il1 == il2
    assert il2 == il1
    assert il1 != il3
    assert il3 != il1


# Generated at 2022-06-14 03:21:57.746377
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList((0, 1, 2, 3, 4)).filter(lambda x: x > 2) == ImmutableList((3, 4))



# Generated at 2022-06-14 03:22:09.225683
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList().filter(lambda d: False) == ImmutableList.empty()
    assert ImmutableList().filter(lambda d: True) == ImmutableList.empty()
    assert ImmutableList(1).filter(lambda d: True) == ImmutableList(1)
    assert ImmutableList(1).filter(lambda d: False) == ImmutableList.empty()
    assert ImmutableList(1, 2).filter(lambda d: d < 2) == ImmutableList(1)
    assert ImmutableList(1, 2, 3).filter(lambda d: True) == ImmutableList(1, 2, 3)
    assert ImmutableList(1, 2, 3).filter(lambda d: False) == ImmutableList.empty()

# Generated at 2022-06-14 03:23:28.178586
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.empty() == ImmutableList.empty()
    assert ImmutableList(1) == ImmutableList(1)
    assert ImmutableList(2, ImmutableList(3)) == ImmutableList(2, ImmutableList(3))
    assert ImmutableList(2, ImmutableList(3, ImmutableList(4))) == ImmutableList(2, ImmutableList(3, ImmutableList(4)))



# Generated at 2022-06-14 03:23:30.249949
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    a = ImmutableList.of(1)
    b = ImmutableList.of(1)

    assert a == b


# Generated at 2022-06-14 03:23:34.496528
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList(1).filter(lambda x: x > 2) == ImmutableList.empty()
    assert ImmutableList(3, ImmutableList(1)).filter(lambda x: x > 2) == ImmutableList(3)
    assert ImmutableList(3, ImmutableList(1)).filter(lambda x: x > 1) == ImmutableList(3, ImmutableList(1))
    assert ImmutableList(3, ImmutableList(1)).filter(lambda x: x > 0) == ImmutableList(3, ImmutableList(1))

# Generated at 2022-06-14 03:23:45.205601
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.empty().find(lambda x: x == 'element') == None
    assert ImmutableList.empty().find(None) == None
    assert ImmutableList.empty().find(lambda x: x == None) == None
    assert ImmutableList.empty().find(lambda x: x != 'element') == None

    assert ImmutableList.of('element').find(lambda x: x == 'element') == 'element'
    assert ImmutableList.of('element').find(lambda x: x != 'element') == None
    assert ImmutableList.of('element').find(None) == None
    assert ImmutableList.of('element').find(lambda x: x == None) == None

    assert ImmutableList.of('element', 'element').find(lambda x: x == 'element') == 'element'
    assert ImmutableList.of

# Generated at 2022-06-14 03:23:47.985121
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    test_cases = (
        ImmutableList(Head),
        ImmutableList(Tail),
    )

    for test_case in test_cases:
        assert test_case == test_case

    assert ImmutableList(Head) != ImmutableList(Tail)

# Generated at 2022-06-14 03:23:51.403261
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # Given
    def is_zero(x):
        return x == 0

    # When
    result = ImmutableList.of(
        1, 2, 3, 4, 0, 5, 6, 7, 8
    ).find(is_zero)

    # Then
    assert result == 0

# Generated at 2022-06-14 03:24:02.196431
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(lambda x: x > 2) == ImmutableList(3, 4, 5)
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(lambda x: x > 10) == ImmutableList(is_empty=True)
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(lambda x: x > 3) == ImmutableList(4, 5)
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(lambda x: x > 5) == ImmutableList(is_empty=True)

# Generated at 2022-06-14 03:24:08.333651
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))) == ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))) != ImmutableList(1, ImmutableList(3, ImmutableList(3)))
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))) != ImmutableList(1, ImmutableList(2))
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))) != ImmutableList(1, ImmutableList(2, ImmutableList(4)))

test_ImmutableList___eq__()

# Generated at 2022-06-14 03:24:19.501152
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList().__eq__(ImmutableList())
    assert not ImmutableList().__eq__(1)

    assert not ImmutableList(1, is_empty=True).__eq__(ImmutableList())

    assert ImmutableList(1).__eq__(ImmutableList(1))
    assert ImmutableList(1).__eq__(ImmutableList(1, ImmutableList(None)))
    assert ImmutableList(1, ImmutableList(2)).__eq__(ImmutableList(1, ImmutableList(2, ImmutableList(None))))
    assert ImmutableList(1).__eq__(ImmutableList(1, ImmutableList(2)).tail)
    assert ImmutableList(1).__eq__(ImmutableList(1, ImmutableList(2, ImmutableList(3))).tail.tail)

# Generated at 2022-06-14 03:24:26.177360
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of('first', 'second', 'third', 'fourth').find(lambda e: e == 'third') == 'third'
    assert ImmutableList.of(1, 2, 3).find(lambda e: e == 2) == 2
    assert ImmutableList.of(1, 2, 3).find(lambda e: e == 4) is None
    assert ImmutableList.empty().find(lambda e: e == 4) is None


# Generated at 2022-06-14 03:25:51.043880
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1).filter(lambda x: x > 1) == ImmutableList.empty()
    assert ImmutableList.of(1).filter(lambda x: x < 1) == ImmutableList.empty()
    assert ImmutableList.of(1).filter(lambda x: x == 1) == ImmutableList.of(1)
    
    assert ImmutableList.of(1, 2).filter(lambda x: x > 2) == ImmutableList.empty()
    assert ImmutableList.of(1, 2).filter(lambda x: x < 2) == ImmutableList.of(1)
    assert ImmutableList.of(1, 2).filter(lambda x: x == 2) == ImmutableList.of(2)
    

# Generated at 2022-06-14 03:25:58.099285
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1,2,3).find(lambda x: x == 3) == 3
    assert ImmutableList.of(1,2,3).find(lambda x: x == 4) is None
    assert ImmutableList.of(1,2,3).find(lambda x: x > 2) == 3
    assert ImmutableList.empty().find(lambda x: x == 1) is None


# Generated at 2022-06-14 03:26:04.893951
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    import math

    # make list of numbers from 0 to 10
    numbers = [math.floor(n) for n in [round(n * (10 / 100), 0) for n in range(100)]]

    # convert list to ImmutableList
    numbers_list = ImmutableList.of(*numbers)
    assert numbers_list.find(lambda n: n == 4) == 4
    assert numbers_list.find(lambda n: n == 'a') is None
    assert numbers_list.find(lambda n: n == 9) == 9
    assert numbers_list.find(lambda n: n == -100) is None


if __name__ == '__main__':
    test_ImmutableList_find()

# Generated at 2022-06-14 03:26:16.024852
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    test_data = [
        (ImmutableList.of(1, 2, 3, 4), lambda x: x % 2 == 0, [2, 4]),
        (ImmutableList.of(1, 2, 3, 4), lambda x: x % 2 == 1, [1, 3]),
        (ImmutableList.of(1, 2, 3, 4), lambda x: x % 3 == 0, [3]),
        (ImmutableList.of(1, 2, 3, 4), lambda x: x % 2 == 1, [1, 3]),
    ]
    for list, fn, expected_result in test_data:
        result = list.filter(fn).to_list()
        assert result == expected_result
        assert list.to_list() == [1, 2, 3, 4] # Check if list is not mutated


# Unit test

# Generated at 2022-06-14 03:26:20.557995
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4)\
        .filter(lambda x: x % 2 == 0)\
        .filter(lambda x: x > 2)\
        == ImmutableList.of(4)

    assert ImmutableList.empty()\
        .filter(lambda x: x % 2 == 0)\
        == ImmutableList.empty()



# Generated at 2022-06-14 03:26:27.471299
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.empty().filter(lambda x: x is not None) == ImmutableList.empty()
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x % 2 == 0) == ImmutableList.of(2)



# Generated at 2022-06-14 03:26:31.654168
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    number_list = ImmutableList.of(3, 5, 7, 9)

    assert number_list.filter(lambda n: n > 5) == ImmutableList.of(7, 9)
    assert number_list.filter(lambda n: n < 5) == ImmutableList.of(3)
    assert number_list.filter(lambda n: n == 5) == ImmutableList.of(5)


# Generated at 2022-06-14 03:26:44.599972
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # Arrange
    test_list = ImmutableList.of(1, 2, 3)

    # Act
    result = test_list.find(lambda x: x == 2)

    # Assert
    assert result == 2