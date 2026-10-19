

# Generated at 2022-06-14 03:44:32.314028
# Unit test for method concat of class Map
def test_Map_concat():
    map1 = Map({'a': All(True), 'b': One('x')})
    map2 = Map({'a': All(False), 'b': One('y')})

    map3 = Map({'a':All(False), 'b':One('xy')})

    assert map1.concat(map2) == map3


# Generated at 2022-06-14 03:44:38.221724
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(10).concat(Min(100)) == Min(10)
    assert Min(10).concat(Min(1)) == Min(1)
    assert Min(1).concat(Min(10)) == Min(1)
    assert Min(10).concat(Min(10)) == Min(10)

# Generated at 2022-06-14 03:44:41.214286
# Unit test for method concat of class Min
def test_Min_concat():
    mleft = Min(10.0)
    mright = Min(20.0)
    sum_mleft_mright = mleft.concat(mright)
    assert_true(sum_mleft_mright == Min(10.0))


# Generated at 2022-06-14 03:44:46.198561
# Unit test for method concat of class Min
def test_Min_concat():
    point = Min(9)
    assert point.concat(Min(10)).value == 9
    assert point.concat(Min(8)).value == 8
    assert point.concat(Min(9)).value == 9


# Generated at 2022-06-14 03:44:50.344874
# Unit test for method concat of class Map
def test_Map_concat():
    assert Map({'a': Sum(1), 'b': Sum(2)}).concat(Map({'a': Sum(2), 'b': Sum(5)})) == Map({'a': Sum(3), 'b': Sum(7)})


# Generated at 2022-06-14 03:44:51.905097
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(2).concat(Min(1)) == Min(1)

# Generated at 2022-06-14 03:44:56.896397
# Unit test for method concat of class Map
def test_Map_concat():
    m = Map({"foo": Sum(1)})
    n = Map({"foo": Sum(2)})
    o = Map({"foo": Sum(3)})
    m_o = m.concat(n).concat(o)
    assert (m_o.value["foo"] == Sum(6))

# Generated at 2022-06-14 03:45:01.474386
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(4).concat(Min(6)).value == 4
    assert Min(4).concat(Min(2)).value == 2



# Generated at 2022-06-14 03:45:09.222129
# Unit test for method concat of class Map
def test_Map_concat():
    m1 = Map({'one': Sum(7), 'two': Sum(3)})
    m2 = Map({'one': Sum(1), 'two': Sum(2)})
    m3 = Map({'one': Sum(8), 'two': Sum(5)})
    assert m3 == m1.concat(m2)

# Generated at 2022-06-14 03:45:20.102917
# Unit test for method concat of class Map
def test_Map_concat():
    # We define two maps with some data
    map1 = Map({'a': Sum(1), 'b': Sum(1), 'c': Sum(1)})
    map2 = Map({'a': Sum(2), 'b': Sum(2), 'c': Sum(2)})

    # We concat the first map in the second
    map3 = map1.concat(map2)

    # We get the results of map3
    a = map3.value['a']
    b = map3.value['b']
    c = map3.value['c']

    # We assert the results
    assert(a.value == 3)
    assert(b.value == 3)
    assert(c.value == 3)

# Generated at 2022-06-14 03:45:24.650954
# Unit test for method concat of class Max
def test_Max_concat():
    semigroup1 = Max(1)
    semigroup2 = Max(2)
    semigroup3 = Max(3)

    assert semigroup1.concat(semigroup2) == Max(2)
    assert semigroup1.concat(semigroup3) == Max(3)
    assert semigroup2.concat(semigroup1) == Max(2)
    assert semigroup2.concat(semigroup3) == Max(3)
    assert semigroup3.concat(semigroup1) == Max(3)
    assert semigroup3.concat(semigroup2) == Max(3)


# Generated at 2022-06-14 03:45:28.066392
# Unit test for constructor of class Sum
def test_Sum():
    sum1 = Sum(10)
    sum2 = Sum(10)
    sum3 = Sum(10)
    assert(sum1.value == 10 and sum1.value == sum2.value and sum2.value == sum3.value)


# Generated at 2022-06-14 03:45:30.417210
# Unit test for method concat of class Map
def test_Map_concat():
    sum_one = Map({
        "key": Semigroup(1)
    })
    sum_two = Map({
        "key": Semigroup(2)
    })
    expected_result = Map({
        "key": Semigroup(3)
    })
    actual_result = sum_one.concat(sum_two)
    assert(expected_result == actual_result)


# Generated at 2022-06-14 03:45:34.155107
# Unit test for method __str__ of class Min
def test_Min___str__():
    # Arrange
    m = Min(5)
    # Act
    actual = str(m)
    # Assert
    expected = 'Min[value=5]'
    assert actual == expected

# Generated at 2022-06-14 03:45:35.872192
# Unit test for method concat of class Last
def test_Last_concat():
    result = Last(3).concat(Last(5))
    expected = Last(5)
    assert result == expected


# Generated at 2022-06-14 03:45:37.412656
# Unit test for constructor of class Max
def test_Max():
    assert Max(4) == Max(4)
    assert Max(3) != Max(4)


# Generated at 2022-06-14 03:45:41.088825
# Unit test for constructor of class Max
def test_Max():
    assert str(Max(1)) == 'Max[value=1]'
    assert Max(1).value == 1

    assert str(Max(10)) == 'Max[value=10]'
    assert Max(10).value == 10



# Generated at 2022-06-14 03:45:46.046370
# Unit test for method concat of class One
def test_One_concat():
    # Given
    monoid_one = One(True)
    monoid_one2 = One(True)
    # When
    result = monoid_one.concat(monoid_one2)
    # Then
    assert result == One(True)


# Generated at 2022-06-14 03:45:46.975610
# Unit test for constructor of class All
def test_All():
    assert All(1).value == 1


# Generated at 2022-06-14 03:45:50.076488
# Unit test for method __str__ of class Last
def test_Last___str__():
    result = str(Last(2/3 + 12**2))
    assert result == 'Last[value={}]'.format(2/3 + 12**2)



# Generated at 2022-06-14 03:45:54.790068
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    assert Semigroup(1).__eq__(Semigroup(1))
    assert not Semigroup(1).__eq__(Semigroup(2))



# Generated at 2022-06-14 03:45:56.448913
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    assert 'Sum[value=3]' == str(Sum(3))


# Generated at 2022-06-14 03:45:57.537593
# Unit test for method concat of class Last
def test_Last_concat():
    result = Last(1).concat(Last(2))
    assert result == Last(2)


# Generated at 2022-06-14 03:45:58.733041
# Unit test for constructor of class All
def test_All():
    assert(All(True).value == True)

    assert(All(False).value == False)



# Generated at 2022-06-14 03:46:00.185815
# Unit test for constructor of class One
def test_One():
    one = One(True)
    assert one.value == True



# Generated at 2022-06-14 03:46:08.712783
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    assert(Sum(1).fold(lambda x: x + 1) == 2)
    assert(All(False).fold(lambda x: x or True) is True)
    assert(One(True).fold(lambda x: x or False) is True)
    assert(First(10).fold(lambda x: x * 2) == 20)
    assert(Last(10).fold(lambda x: x * 2) == 20)
    assert(Max(10).fold(lambda x: x * 2) == 20)
    assert(Min(10).fold(lambda x: x * 2) == 20)



# Generated at 2022-06-14 03:46:14.968262
# Unit test for method __str__ of class Last
def test_Last___str__():
    assert str(Last(5)) == 'Last[value=5]'
    assert str(Last(10)) == 'Last[value=10]'
    assert str(Last('a')) == 'Last[value=a]'
    assert str(Last({'a': 1, 'b': 2})) == 'Last[value={\'a\': 1, \'b\': 2}]'



# Generated at 2022-06-14 03:46:17.239158
# Unit test for constructor of class Min
def test_Min():
    assert Min(1) == Min(1)
    assert Min(1).value == 1
    assert Min(1).fold(lambda x: x+1) == 2


# Generated at 2022-06-14 03:46:22.420265
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    assert Sum(1).__eq__(Sum(1)) is True
    assert Sum(1).__eq__(Sum(2)) is False
    assert Sum(1).__eq__(1) is False
    assert Sum(1).__eq__(All(True)) is False


# Generated at 2022-06-14 03:46:24.723540
# Unit test for constructor of class Last
def test_Last():
    x = Last(True)
    assert isinstance(x, Last) is True


# Generated at 2022-06-14 03:46:30.605577
# Unit test for method __str__ of class One
def test_One___str__():
    # Create an instance of One and assign to variable b
    b = One(True)
    # Create an instance of One and assign to variable c
    c = One(1)

    assert str(b) == "One[value=True]"
    assert str(c) == "One[value=1]"



# Generated at 2022-06-14 03:46:33.909840
# Unit test for method concat of class First
def test_First_concat():
    first_a = First("A")
    first_b = First("B")
    assert first_a.concat(first_b).value == "A"


# Generated at 2022-06-14 03:46:40.777622
# Unit test for method concat of class All
def test_All_concat():
    all1 = All(True)
    all2 = All(True)
    assert all1.concat(all2).value

    all1 = All(True)
    all2 = All(False)
    assert not all1.concat(all2).value

    all1 = All(False)
    all2 = All(True)
    assert not all1.concat(all2).value

    all1 = All(False)
    all2 = All(False)
    assert not all1.concat(all2).value



# Generated at 2022-06-14 03:46:54.048872
# Unit test for method concat of class Map
def test_Map_concat():
    """
    Unit test for method concat of class Map
    """
    import operator
    from functools import reduce

    items = {
        'a': All(True),
        'o': One(False),
        's': Sum(2),
        'f': First(1),
        'l': Last(2),
        'm': Max(5),
        'n': Min(1),
    }
    assert Map(items).fold(operator.attrgetter('concat')) == Map(items)
    assert reduce(lambda s, o: o.concat(s), [Map(items), Map(items)]) == Map(items).fold(
        operator.attrgetter('concat'))

# Generated at 2022-06-14 03:46:56.242714
# Unit test for method __str__ of class All
def test_All___str__():
    all = All(True)
    assert all.__str__() == 'All[value=True]'



# Generated at 2022-06-14 03:46:57.644298
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(3)) == 'Max[value=3]'



# Generated at 2022-06-14 03:47:01.595079
# Unit test for constructor of class Last
def test_Last():
    # arrange
    lst = [
        Last(1),
        Last(2),
    ]

    # act
    result = reduce(lambda acc, semigroup: acc.concat(semigroup), lst)

    # assert
    assert Last(2) == result



# Generated at 2022-06-14 03:47:06.982449
# Unit test for method concat of class Map
def test_Map_concat():
    u = Map({'a': Sum(1), 'b': Sum(1)})
    v = Map({'a': Sum(2), 'b': Sum(3)})
    map_w = u.concat(v)
    assert map_w.value['a'].value == 3
    assert map_w.value['b'].value == 4



# Generated at 2022-06-14 03:47:08.884779
# Unit test for constructor of class Min
def test_Min():
    assert Min(2).value == 2
    assert Min(3).value == 3


# Generated at 2022-06-14 03:47:12.236932
# Unit test for constructor of class Min
def test_Min():
    assert Min(13) == Min(13)


# Generated at 2022-06-14 03:47:16.787285
# Unit test for constructor of class Semigroup
def test_Semigroup():  # pragma: no cover
    assert Semigroup(1).value == 1



# Generated at 2022-06-14 03:47:17.975482
# Unit test for method __str__ of class All
def test_All___str__():
    assert str(All(False)) == 'All[value=False]'
    assert str(All(True)) == 'All[value=True]'


# Generated at 2022-06-14 03:47:21.137671
# Unit test for method concat of class Max
def test_Max_concat():
    max_ = Max(10)
    assert max_.concat(Max(20)) == Max(20)
    assert max_.concat(Max(5)) == Max(10)


# Generated at 2022-06-14 03:47:23.847235
# Unit test for method __str__ of class All
def test_All___str__():
    all_ = All(True)
    expected = 'All[value=True]'
    actual = all_.__str__()
    # print(actual)
    assert actual == expected



# Generated at 2022-06-14 03:47:27.838503
# Unit test for method concat of class One
def test_One_concat(): # pragma: no cover
    assert One(True).concat(One(True)).value == True
    assert One(False).concat(One(True)).value == True
    assert One(False).concat(One(False)).value == False


# Generated at 2022-06-14 03:47:31.495570
# Unit test for constructor of class Last
def test_Last():
    assert Last(3).fold(identity) == 3
    assert Last('3').fold(identity) == '3'
    assert Last(['3']).fold(identity) == ['3']



# Generated at 2022-06-14 03:47:34.772549
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    assert str(Sum(1)) == 'Sum[value=1]'
    assert str(Sum(2)) == 'Sum[value=2]'


# Generated at 2022-06-14 03:47:38.632007
# Unit test for method concat of class Min
def test_Min_concat():
    min1 = Min(1)
    min2 = Min(2)
    min3 = Min(3)
    min1.concat(min2).concat(min3) == Min(1)



# Generated at 2022-06-14 03:47:40.095475
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(100).concat(Max(101)).value == 101


# Generated at 2022-06-14 03:47:44.932837
# Unit test for method concat of class One
def test_One_concat():
    assert One(1).concat(One(2)) == One(1)
    assert One(1).concat(One(0)) == One(1)
    assert One(0).concat(One(1)) == One(1)
    assert One(0).concat(One(0)) == One(0)



# Generated at 2022-06-14 03:47:54.066231
# Unit test for method concat of class First
def test_First_concat():
    first = First(1)
    second = First(2)
    third = First(3)

    assert first.concat(second).concat(third) == first.concat(second.concat(third))



# Generated at 2022-06-14 03:47:59.124472
# Unit test for constructor of class Map
def test_Map():
    """
    >>> m = Map({'a': Sum(1), 'b': Last(2)})
    >>> m.value
    {'a': Sum[value=1], 'b': Last[value=2]}
    >>> m.value['b'].value
    2
    """
    pass



# Generated at 2022-06-14 03:48:00.911084
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(100).concat(Max(200)) == Max(200)


# Generated at 2022-06-14 03:48:04.588213
# Unit test for method concat of class Max
def test_Max_concat():
    # type: () -> None
    assert Max(1).concat(Max(2)) == Max(2)
    assert Max(2).concat(Max(1)) == Max(2)
    assert Max(2).concat(Max(2)) == Max(2)
    assert Max(1).concat(Sum(1)) == Max(1)
    assert Max(1).concat(All(1)) == Max(1)
    assert Max(1).concat(One(1)) == Max(1)


# Generated at 2022-06-14 03:48:06.723747
# Unit test for constructor of class One
def test_One():
    assert One(True) == One(True)
    assert One(True) != One(False)


# Generated at 2022-06-14 03:48:08.912205
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    sum1 = Sum(1)
    assert str(sum1) == 'Sum[value=1]'



# Generated at 2022-06-14 03:48:11.048676
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    assert(
        Sum(2).fold(lambda x: x + 1)
        ==
        3
    )

# Generated at 2022-06-14 03:48:13.159753
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    semigroup_one = Semigroup.neutral()
    semigroup_two = Semigroup.neutral()
    assert semigroup_one == semigroup_two



# Generated at 2022-06-14 03:48:14.678589
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(0)) == 'Max[value=0]'


# Generated at 2022-06-14 03:48:16.195890
# Unit test for constructor of class One
def test_One():
    assert repr(One(1)) == 'One[value=1]'


# Generated at 2022-06-14 03:48:23.567414
# Unit test for constructor of class All
def test_All():
    assert All(True).value == True


# Generated at 2022-06-14 03:48:24.943532
# Unit test for constructor of class Min
def test_Min():
    assert Min(4).value == 4

# Test for fold method of class Min

# Generated at 2022-06-14 03:48:26.701302
# Unit test for method concat of class Sum
def test_Sum_concat():
    assert Sum(1).concat(Sum(2)) == Sum(3)


# Generated at 2022-06-14 03:48:28.088685
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert isinstance(Max(3).__str__(), str)



# Generated at 2022-06-14 03:48:30.612996
# Unit test for method __str__ of class One
def test_One___str__():  # pragma: no cover
    assert One(1).__str__() == 'One[value=1]'



# Generated at 2022-06-14 03:48:32.117190
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    assert str(Sum(1)) == "Sum[value=1]"


# Generated at 2022-06-14 03:48:39.113743
# Unit test for constructor of class Map
def test_Map():
    map = Map({"test1": Sum(1), "test2": Sum(2), "test3": Sum(3)})
    assert map.value == {"test1": Sum(1), "test2": Sum(2), "test3": Sum(3)}

    map_bad = Map(1)
    assert map_bad.value == 1

    map2 = Map({"test1": Sum(1), "test2": Sum(2), "test3": Sum(3)})
    assert map == map2
    assert map.value == map2.value
    assert map.concat(map2) == map
    assert map.concat(map2).concat(map) == map



# Generated at 2022-06-14 03:48:43.236047
# Unit test for constructor of class First
def test_First():
    assert First(1) == First(1)
    assert str(First(1)) == 'Fist[value=1]'
    assert repr(First(1)) == 'First(1)'

# Unit tests for function concat of class First

# Generated at 2022-06-14 03:48:46.587065
# Unit test for method __str__ of class Last
def test_Last___str__():
    assert str(Last(1)) == "Last[value=1]"
    assert str(Last("Hello")) == "Last[value=Hello]"



# Generated at 2022-06-14 03:48:49.253177
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    assert str(Sum(1)) == 'Sum[value=1]'



# Generated at 2022-06-14 03:49:01.915697
# Unit test for constructor of class Semigroup
def test_Semigroup():  # pragma: no cover
    sg = Semigroup(1)



# Generated at 2022-06-14 03:49:05.775355
# Unit test for constructor of class Map
def test_Map():
    """
    Unit test constructor of class Map
    """
    m = Map({
        'a': First(True),
        'b': First(False)
    })

    assert m.value['a'].value == True
    assert m.value['b'].value == False



# Generated at 2022-06-14 03:49:08.621890
# Unit test for method concat of class Max
def test_Max_concat():
    print("\nStart test_Max_concat")

    first = Max(5)
    second = Max(18)
    assert first.concat(second).value == 18

    print("\nTest test_Max_concat passed.")



# Generated at 2022-06-14 03:49:16.054135
# Unit test for method concat of class Min
def test_Min_concat():
    a = Min(4)
    b = Min(5)
    assert a.concat(b) == Min(4)
    a = Min(5)
    b = Min(4)
    assert a.concat(b) == Min(4)
    a = Min(4)
    b = Min(4)
    assert a.concat(b) == Min(4)


# Generated at 2022-06-14 03:49:26.653689
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    assert All(True) == All(True)
    assert All(False) != All(True)
    assert All(True) != One(True)
    with pytest.raises(NotImplementedError):
        assert Last(1) == Last(2)
    with pytest.raises(NotImplementedError):
        assert First(1) == First(2)
    with pytest.raises(NotImplementedError):
        assert First(1) != First(1)
    assert Map({'a': Sum(1), 'b': Sum(2)}) == Map({'a': Sum(1), 'b': Sum(2)})
    assert Map({'a': Sum(1), 'b': Sum(2)}) != Map({'a': Sum(1), 'b': Sum(3)})
    assert Sum(1)

# Generated at 2022-06-14 03:49:27.711272
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(1)) == 'Max[value=1]'


# Generated at 2022-06-14 03:49:29.295490
# Unit test for constructor of class First
def test_First():
    assert First(3) == First(3)



# Generated at 2022-06-14 03:49:32.682527
# Unit test for constructor of class Sum
def test_Sum():
    assert Sum(1) == Sum(1)
    assert Sum(1) != Sum(2)
    assert Sum(1).fold(str) == '1'


# Generated at 2022-06-14 03:49:35.495939
# Unit test for constructor of class Semigroup
def test_Semigroup():
    semigroup = Semigroup(None)
    assert semigroup.value is None



# Generated at 2022-06-14 03:49:36.993803
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(1).concat(Max(2)) == Max(2)



# Generated at 2022-06-14 03:50:03.986260
# Unit test for constructor of class All
def test_All():
    one_all = All(1)
    assert isinstance(one_all, All)
    assert one_all.value == 1


# Generated at 2022-06-14 03:50:06.176407
# Unit test for constructor of class Last
def test_Last():
    try:
        last = Last('cat')
    except Exception as error:
        print(error)


# Generated at 2022-06-14 03:50:09.413400
# Unit test for method __str__ of class Max
def test_Max___str__():
    # Given
    obj = Max(100)

    # When
    result = str(obj)

    # Then
    assert result == 'Max[value=100]'



# Generated at 2022-06-14 03:50:12.440553
# Unit test for method __str__ of class All
def test_All___str__():
    assert str(All(True)) == 'All[value=True]'
    assert str(All(False)) == 'All[value=False]'


# Generated at 2022-06-14 03:50:14.126110
# Unit test for method __str__ of class First
def test_First___str__():
    x = First("123")
    assert str(x) == "Fist[value=123]"


# Generated at 2022-06-14 03:50:18.919920
# Unit test for method __str__ of class All
def test_All___str__():
    """
    All.__str__() method should return name of object with value
    """
    # Arrange
    expected = 'All[value=True]'
    # Act
    actual = str(All(True))
    # Assert
    assert expected == actual



# Generated at 2022-06-14 03:50:22.879578
# Unit test for method concat of class Min
def test_Min_concat():
    value_1 = Min(7)
    value_2 = Min(4)
    result = value_1.concat(value_2)
    expected = Min(4)
    assert result == expected


# Generated at 2022-06-14 03:50:24.557708
# Unit test for method __str__ of class All
def test_All___str__():
    assert 'All[value=True]' == str(All(True))



# Generated at 2022-06-14 03:50:29.602255
# Unit test for constructor of class All
def test_All():
    assert All(True).value == True
    assert All(False).value == False
    assert All(1).value == True
    assert All(0).value == False
    assert All('').value == False
    assert All('a').value == True


# Generated at 2022-06-14 03:50:31.063845
# Unit test for method __str__ of class Last
def test_Last___str__():
    assert (str(Last(1)) == 'Last[value=1]')


# Generated at 2022-06-14 03:51:24.927708
# Unit test for method __str__ of class Min
def test_Min___str__():
    assert str(Min(1)) == 'Min[value=1]'


# Generated at 2022-06-14 03:51:26.171024
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    assert str(Sum(3)) == "Sum[value=3]"



# Generated at 2022-06-14 03:51:31.780256
# Unit test for method concat of class All
def test_All_concat():
    assert All(True).concat(All(True)).value == True
    assert All(True).concat(All(False)).value == False
    assert All(False).concat(All(True)).value == False
    assert All(False).concat(All(False)).value == False


# Generated at 2022-06-14 03:51:34.692971
# Unit test for method concat of class Sum
def test_Sum_concat():
    assert Sum(1).concat(Sum(2)).value == 3


# Generated at 2022-06-14 03:51:39.603346
# Unit test for method __str__ of class First
def test_First___str__():  # pragma: no cover
    assert str(First(1)) == "Fist[value=1]"
    assert str(First("1")) == "Fist[value=1]"
    assert str(First(First(1))) == "Fist[value=Fist[value=1]]"
    assert str(First(Last(1))) == "Fist[value=Last[value=1]]"

# Generated at 2022-06-14 03:51:41.882812
# Unit test for constructor of class Max
def test_Max():
    """
    Unit test for constructor of class Max
    """
    assert Max(9) == Max(9)
    assert Max(9) != Max(10)
    assert Max(9).value == 9



# Generated at 2022-06-14 03:51:53.513022
# Unit test for method concat of class All
def test_All_concat():
    assert All(False).concat(All(True)) == All(False)
    assert All(False).concat(All(None)) == All(False)
    assert All(False).concat(All(False)) == All(False)
    assert All(False).concat(All('')) == All(False)
    assert All(False).concat(All([])) == All(False)
    assert All(False).concat(All({})) == All(False)

    assert All(True).concat(All(True)) == All(True)
    assert All(True).concat(All(False)) == All(False)
    assert All(True).concat(All(None)) == All(False)
    assert All(True).concat(All('')) == All(False)

# Generated at 2022-06-14 03:51:55.418317
# Unit test for method __str__ of class Min
def test_Min___str__():
    """
    Unit test for method __str__ of class Min
    """

    assert str(Min(1)) == 'Min[value=1]'


# Generated at 2022-06-14 03:52:02.878883
# Unit test for method concat of class One
def test_One_concat():
    result = One(5).concat(One(6))
    expected = One(5)
    assert result.value == expected.value
    result = One(False).concat(One(False))
    expected = One(False)
    assert result.value == expected.value
    result = One('').concat(One('Son'))
    expected = One('Son')
    assert result.value == expected.value


# Generated at 2022-06-14 03:52:04.471894
# Unit test for method __str__ of class Last
def test_Last___str__():
    assert str(Last(1)) == "Last[value=1]"


# Generated at 2022-06-14 03:54:03.804861
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    m = Sum(10)
    assert str(m) == 'Sum[value=10]'


# Generated at 2022-06-14 03:54:06.604894
# Unit test for constructor of class Semigroup
def test_Semigroup():
    assert Semigroup(2) == Semigroup(2)
    assert not Semigroup(2) == Semigroup(1)


# Generated at 2022-06-14 03:54:07.603493
# Unit test for method __str__ of class Sum
def test_Sum___str__():
        Sum = make_Sum(0)
        assert str(Sum) == "Sum[value=0]"


# Generated at 2022-06-14 03:54:11.462240
# Unit test for method concat of class Map
def test_Map_concat():  # pragma: no cover
    assert Map({"a": Sum(1)}).concat(
        Map({"a": Sum(1)})
    ).fold(lambda i: i["a"]) == 2



# Generated at 2022-06-14 03:54:12.554314
# Unit test for method __str__ of class First
def test_First___str__():
    assert str(First(1)) == 'Fist[value=1]'


# Generated at 2022-06-14 03:54:15.545290
# Unit test for constructor of class All
def test_All():
    assert All(True).value == True
    assert All(False).value == False
    assert All(1).value == True
    assert All(0).value == False


# Generated at 2022-06-14 03:54:18.113045
# Unit test for constructor of class Sum
def test_Sum():
    assert Sum(5) == Sum(5)
    assert Sum(5) != Sum(6)


# Generated at 2022-06-14 03:54:21.221077
# Unit test for method __str__ of class Last
def test_Last___str__():
    """
    Test for method __str__ for class Last
    """
    assert str(Last("a")) == 'Last[value="a"]'



# Generated at 2022-06-14 03:54:24.214006
# Unit test for method __str__ of class One
def test_One___str__(): # pragma: no cover
    assert str(One(True)) == 'One[value=True]'
    assert str(One(False)) == 'One[value=False]'
