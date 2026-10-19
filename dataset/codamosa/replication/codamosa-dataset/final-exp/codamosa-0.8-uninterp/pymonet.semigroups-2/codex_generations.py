

# Generated at 2022-06-14 03:44:35.996877
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(4).concat(Min(5)).concat(Min(3)) == Min(3)


# Generated at 2022-06-14 03:44:38.251962
# Unit test for method concat of class Min
def test_Min_concat():
    min1 = Min(1)
    min2 = Min(2)
    min3 = min1.concat(min2)
    assert min3.value == 1



# Generated at 2022-06-14 03:44:45.296343
# Unit test for method concat of class Map
def test_Map_concat():
    m1 = Map({'a': {'b': 1}, 'c': {'d': 2}})
    m2 = Map({'a': {'b': 3}, 'c': {'d': 6}})
    m3 = m1.concat(m2)
    m4 = Map({'a': {'b': 10}, 'c': {'d': 8}})
    assert m3.value == {'a': {'b': {'c': {'d': 2}, 'b': 1}}, 'c': {'d': {'c': {'d': 2}, 'b': 1}}}
    assert m3 == m3
    assert m3 != m4
    assert m3 != Sum(2)
    assert m3 != 1



# Generated at 2022-06-14 03:44:50.961558
# Unit test for method concat of class Min
def test_Min_concat():
    # Create two Min values holding 0 and 7
    m0, m7 = Min(0), Min(7)
    # The result is the smaller of the two values
    assert m0.concat(m7).value == 0
    # The order doesn't matter
    assert m7.concat(m0).value == 0


# Generated at 2022-06-14 03:44:52.885288
# Unit test for method concat of class Min
def test_Min_concat():
    val = Min(55)
    val.concat(Min(66)) == Min(55)



# Generated at 2022-06-14 03:44:57.444152
# Unit test for method concat of class Map
def test_Map_concat():
    value = {
        "a": Sum(1),
        "b": Sum(2)
    }

    semigroup = {
        "c": Sum(3),
        "a": Sum(10)
    }

    m = Map(value)

    result = {
        "a": Sum(11),
        "b": Sum(2),
        "c": Sum(3)
    }

    assert m.concat(Map(semigroup)).value == result

# Generated at 2022-06-14 03:44:59.746802
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(1).concat(Min(2)).value == 1


# Generated at 2022-06-14 03:45:02.673268
# Unit test for method concat of class Max
def test_Max_concat():
    max = Max(1).concat(Max(2))
    assert max.value == 2



# Generated at 2022-06-14 03:45:09.636399
# Unit test for method concat of class Map
def test_Map_concat():
    map1 = Map({
        'a': Sum(1),
        'b': Sum(2),
    })

    map2 = Map({
        'a': Sum(1),
        'b': Sum(2),
    })

    assert map1.concat(map2) == Map({
        'a': Sum(2),
        'b': Sum(4),
    })

# Generated at 2022-06-14 03:45:13.645684
# Unit test for method concat of class Map
def test_Map_concat():
    a = Map({'x': All(True), 'y': First(1), 'z': Max(0)})
    b = Map({'x': All(False), 'y': First(2), 'z': Max(1)})
    assert a.concat(b) == Map({'x': All(False), 'y': First(1), 'z': Max(1)})

# Generated at 2022-06-14 03:45:17.446314
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(1).concat(Min(2)).value == 1

    assert Min(2).concat(Min(1)).value == 1



# Generated at 2022-06-14 03:45:23.218892
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(5).concat(Min(10)) == Min(5)
    assert Min(20).concat(Min(10)) == Min(10)

"""
Here are some custom Monoids.

This is the Identity monoid.
It has a value, and when concatenated will always return the same value.
"""



# Generated at 2022-06-14 03:45:31.238141
# Unit test for method concat of class Min
def test_Min_concat():
    min_1 = Min(1)
    min_2 = Min(2)
    min_3 = Min(3)
    assert min_1.concat(min_2) == min_2.concat(min_1)
    assert min_2.concat(min_3).concat(min_1) == min_1.concat(min_2.concat(min_3))
    assert min_2.concat(min_3) == Min(2)
    assert min_2.concat(min_1) == Min(1)
    assert min_3.concat(min_2) == Min(2)
    assert min_2.concat(min_3).concat(min_3) == Min(2)

# Generated at 2022-06-14 03:45:33.883022
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(1).concat(Min(2)) == Min(1)


# Generated at 2022-06-14 03:45:36.355913
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(1).concat(Min(-1)) == Min(-1)


# Generated at 2022-06-14 03:45:41.611433
# Unit test for method concat of class Min
def test_Min_concat():
    v1 = Min(1)
    v2 = Min(2)
    v3 = Min(3)
    semigroup = v1.concat(v2)
    result = semigroup.concat(v3)
    expected = Min(1)

    assert expected.value == result.value
    assert expected.concat(result) == result.concat(expected)


# Generated at 2022-06-14 03:45:44.426434
# Unit test for method concat of class Min
def test_Min_concat():
    m = Min(1)
    m2 = Min(2)
    result = m.concat(m2)
    assert result.value == m.value
    assert result.value == 1



# Generated at 2022-06-14 03:45:46.839077
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(2).concat(Min(3)) == Min(2)

# Generated at 2022-06-14 03:45:49.946321
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(1).concat(Min(2)).value == 1
    assert Min(2).concat(Min(1)).value == 1
    assert Min(1).concat(Min(1)).value == 1



# Generated at 2022-06-14 03:45:53.025259
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(0).concat(Min(1)) == Min(0)


# Generated at 2022-06-14 03:45:57.386258
# Unit test for method __str__ of class Map
def test_Map___str__():
    assert str(Map({1: First(1), 2: Last(2)})) == 'Map[value={1: Fist[value=1], 2: Last[value=2]}]'


# Generated at 2022-06-14 03:45:58.361860
# Unit test for method __str__ of class Last
def test_Last___str__():
    assert str(Last("123")) == "Last[value=123]"


# Generated at 2022-06-14 03:46:00.623886
# Unit test for constructor of class One
def test_One():
    # Given
    element = 1

    # When
    one = One(element)

    # Then
    assert one.value == element


# Generated at 2022-06-14 03:46:01.623789
# Unit test for constructor of class Min
def test_Min():
    assert Min(3).value == 3


# Generated at 2022-06-14 03:46:04.160818
# Unit test for constructor of class Semigroup
def test_Semigroup():
    sum_semigroup = Sum(42)
    assert sum_semigroup.value == 42



# Generated at 2022-06-14 03:46:06.343298
# Unit test for constructor of class All
def test_All():
    """
    Unit test for All class constructor.
    """
    assert All(True) == All(True)



# Generated at 2022-06-14 03:46:09.299508
# Unit test for method __str__ of class Max
def test_Max___str__():
    # Arrange
    max_obj = Max(1)

    # Act
    result = str(max_obj)

    # Assert
    assert result == 'Max[value=1]'



# Generated at 2022-06-14 03:46:11.781475
# Unit test for constructor of class All
def test_All():
    assert All(True) == All(True)
    assert All(False) != All(True)


# Generated at 2022-06-14 03:46:14.914667
# Unit test for method __str__ of class Map
def test_Map___str__():
    assert str(Map({'a': Sum(1), 'b': Sum(2)})) == "Map[value={'a': Sum[value=1], 'b': Sum[value=2]}]"


# Generated at 2022-06-14 03:46:16.786995
# Unit test for method concat of class Last
def test_Last_concat():
    assert Last(1).concat(Last(2)) == Last(2)
    assert Last(1).concat(Last(1)) == Last(1)



# Generated at 2022-06-14 03:46:20.662279
# Unit test for method __str__ of class First
def test_First___str__():
    first = First(5)
    assert str(first) == 'Fist[value=5]'



# Generated at 2022-06-14 03:46:24.388037
# Unit test for constructor of class Sum
def test_Sum():
    """
    Test constructors of class Sum

    :return: None
    """
    assert Sum(2).value == 2
    assert Sum(2) == Sum(2)
    assert str(Sum(5)) == 'Sum[value=5]'


# Generated at 2022-06-14 03:46:31.181115
# Unit test for constructor of class Sum
def test_Sum():
    """
    Sum is a Monoid that will combine 2 numbers under addition.
    """
    object1 = Sum(1)
    assert object1.value == 1
    assert repr(object1) == 'Sum[value=1]'
    object2 = Sum(2)
    assert object2.value == 2
    assert repr(object2) == 'Sum[value=2]'
    object3 = Sum(3)
    assert object3.value == 3
    assert repr(object3) == 'Sum[value=3]'


# Generated at 2022-06-14 03:46:34.064225
# Unit test for constructor of class Last
def test_Last():
    assert Last(1) == Last(1)
    assert Last(1) != Last(2)
    assert Last(1) != 1
    assert Last(1) != [1]


# Generated at 2022-06-14 03:46:37.493280
# Unit test for method concat of class Last
def test_Last_concat():
    first_last = Last(1)
    second_last = Last(2)
    third_last = first_last.concat(second_last)
    assert third_last.value == 2


# Generated at 2022-06-14 03:46:39.336980
# Unit test for method __str__ of class Min
def test_Min___str__():
    assert str(Min(1)) == 'Min[value=1]'



# Generated at 2022-06-14 03:46:41.155319
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(1)) == 'Max[value=1]'



# Generated at 2022-06-14 03:46:43.630681
# Unit test for method __str__ of class Max
def test_Max___str__():  # pragma: no cover
    assert str(Max(5)) == 'Max[value=5]'



# Generated at 2022-06-14 03:46:53.817701
# Unit test for method __str__ of class Map
def test_Map___str__():
    assert str(Map({})) == "Map[{}]"
    assert str(Map({"a": Sum(1)})) == "Map[{'a': Sum[1]}]"
    assert str(Map({"a": Sum(1), "b": Sum(2)})) == "Map[{'a': Sum[1], 'b': Sum[2]}]"
    assert str(Map({"a": Sum(1), "b": Map({"b1": Sum(2)})})) == "Map[{'a': Sum[1], 'b': Map[{'b1': Sum[2]}]}]"


# Generated at 2022-06-14 03:46:56.876848
# Unit test for constructor of class All
def test_All():
    assert All(True) == All(True)
    assert All(True) != All(False)
    assert All(False) == All(False)


# Generated at 2022-06-14 03:47:00.693415
# Unit test for method concat of class Min
def test_Min_concat():
    a = Min(1)
    b = Min(2)
    assert a.concat(b) == Min(1)


# Generated at 2022-06-14 03:47:02.796781
# Unit test for constructor of class Max
def test_Max():
    assert str(Max(1)) == 'Max[value=1]'


# Generated at 2022-06-14 03:47:06.123548
# Unit test for method __str__ of class Map
def test_Map___str__():
    semigroup = Map({'one': Sum(1), 'two': Sum(2), 'three': Sum(3)})
    assert str(semigroup) == "Map[value={'one': Sum[value=1], " \
                             "'two': Sum[value=2], 'three': Sum[value=3]}]"


# Generated at 2022-06-14 03:47:09.202013
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    assert Semigroup(1) == Semigroup(1)
    assert Semigroup(0) == Semigroup(0)
    assert not (Semigroup(0) == Semigroup(1))


# Generated at 2022-06-14 03:47:12.947696
# Unit test for method __str__ of class Min
def test_Min___str__():
    min_ = Min(0)
    assert min_.__str__() == 'Min[value=0]'


# Generated at 2022-06-14 03:47:16.603458
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(1).concat(Max(3)) == Max(3)
    assert Max(1).concat(Max(1)) == Max(1)
    assert Max(3).concat(Max(1)) == Max(3)


# Generated at 2022-06-14 03:47:19.215788
# Unit test for method __str__ of class Last
def test_Last___str__():
    semigroup = Last(1)
    result = str(semigroup)
    assert 'Last[value=1]' == result



# Generated at 2022-06-14 03:47:20.800379
# Unit test for constructor of class First
def test_First():
    first = First(1)
    assert first.value == 1



# Generated at 2022-06-14 03:47:22.482986
# Unit test for method concat of class All
def test_All_concat():
    concat = All(True).concat(All(False))
    assert concat == All(False)

# Generated at 2022-06-14 03:47:25.508944
# Unit test for constructor of class One
def test_One():
    """
    Unit test for constructor of class One
    """
    assert One(True) == One(True)



# Generated at 2022-06-14 03:47:31.873240
# Unit test for constructor of class Map
def test_Map():
    x = Map({1: Sum(2), 3: Sum(4)})
    y = Map({1: Sum(2), 3: Sum(4)})
    print(x)
    print(y)
    assert x == y



# Generated at 2022-06-14 03:47:34.972649
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    assert str(Sum(4)) == "Sum[value=4]"
    assert str(Sum(-7)) == "Sum[value=-7]"



# Generated at 2022-06-14 03:47:41.288289
# Unit test for constructor of class Map
def test_Map():
    assert Map({}) == Map({})
    assert Map({'a': 1}) == Map({'a': 1})
    assert Map({'a': 1, 'b': 2}) == Map({'b': 2, 'a': 1})
    with pytest.raises(AssertionError):
        assert Map({'a': 1, 'b': 2}) == Map({'a': 1})



# Generated at 2022-06-14 03:47:43.526626
# Unit test for constructor of class Last
def test_Last():

    assert Last(5) == Last(5)
    assert Last(5) != Last(7)



# Generated at 2022-06-14 03:47:46.008273
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    assert str(Sum(10)) == 'Sum[value=10]'
    assert Sum(10) == Sum(10)



# Generated at 2022-06-14 03:47:51.212166
# Unit test for method concat of class One
def test_One_concat():
    assert One(True).concat(One(True)) == One(True)
    assert One(True).concat(One(False)) == One(True)
    assert One(False).concat(One(False)) == One(False)
    assert One(False).concat(One(True)) == One(True)


# Generated at 2022-06-14 03:47:53.147826
# Unit test for constructor of class One
def test_One():
    try:
        assert One(True).value == True
    except AssertionError:
        return AssertionError
    else:
        return

# Generated at 2022-06-14 03:47:57.862140
# Unit test for method concat of class Last
def test_Last_concat():
    a = Last(value=1)
    b = Last(value=2)
    assert a.concat(b) == b.concat(a) == Last(value=2)

# Generated at 2022-06-14 03:48:00.429583
# Unit test for method __str__ of class One
def test_One___str__():  # pragma: no cover
    assert str(One(True)) == 'One[value=True]'
    assert str(One(False)) == 'One[value=False]'


# Generated at 2022-06-14 03:48:02.907368
# Unit test for method __str__ of class Min
def test_Min___str__():
    assert Min(1).__str__() == 'Min[value=1]'


# Generated at 2022-06-14 03:48:09.393689
# Unit test for method __str__ of class Map
def test_Map___str__():
    assert str(Map({'a':Sum(1), 'b':Sum(2)})) == 'Map[value={\'a\': Sum[value=1], \'b\': Sum[value=2]}]'


# Generated at 2022-06-14 03:48:11.383737
# Unit test for method concat of class Sum
def test_Sum_concat():
    assert Sum(3).concat(Sum(2)) == Sum(5)



# Generated at 2022-06-14 03:48:12.975596
# Unit test for constructor of class Last
def test_Last():
    last = Last(25)
    assert last.value == 25



# Generated at 2022-06-14 03:48:14.923523
# Unit test for constructor of class Sum
def test_Sum():
    assert Sum(1).value == 1
    assert Sum(1).fold(lambda x: x) == 1



# Generated at 2022-06-14 03:48:16.041571
# Unit test for constructor of class One
def test_One():
    assert One(1).value == 1


# Generated at 2022-06-14 03:48:17.068340
# Unit test for constructor of class Min
def test_Min():
    assert Min(10).value == 10


# Generated at 2022-06-14 03:48:19.446269
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(1)) == 'Max[value=1]'



# Generated at 2022-06-14 03:48:25.938916
# Unit test for method concat of class Map
def test_Map_concat():
    assert Map({'a': Sum(20), 'b': Sum(30), 'c': Sum(40)}).concat(
        Map({'a': Sum(60), 'b': Sum(70), 'd': Sum(50)})) == \
        Map({'a': Sum(80), 'b': Sum(100), 'c': Sum(40), 'd': Sum(50)})



# Generated at 2022-06-14 03:48:27.357790
# Unit test for constructor of class Last
def test_Last():
    assert Last('Hello').value == 'Hello'



# Generated at 2022-06-14 03:48:29.407897
# Unit test for constructor of class Max
def test_Max():
    combined = Max(10).concat(Max(12))
    assert combined.value == 12



# Generated at 2022-06-14 03:48:38.730158
# Unit test for method __str__ of class One
def test_One___str__():
    assert str(One(True)) == 'One[value=True]'
    assert str(One(False)) == 'One[value=False]'
    assert str(One(1)) == 'One[value=1]'
    assert str(One(1.1)) == 'One[value=1.1]'
    assert str(One('A')) == 'One[value=A]'
    assert str(One([1, 2])) == 'One[value=[1, 2]]'
    assert str(One({'A': 1, 'B':2})) == "One[value={'A': 1, 'B': 2}]"


# Generated at 2022-06-14 03:48:40.826844
# Unit test for method __str__ of class Last
def test_Last___str__():
    assert str(Last(2)) == 'Last[value=2]'


# Generated at 2022-06-14 03:48:41.466124
# Unit test for constructor of class All
def test_All():
    assert All(True) == All(True)



# Generated at 2022-06-14 03:48:42.847129
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(3)) == 'Max[value=3]'


# Generated at 2022-06-14 03:48:45.638530
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    from hamcrest import assert_that, equal_to

    assert_that(Sum(1).fold(lambda x: x + 1), equal_to(2))

test_Semigroup_fold()

# Generated at 2022-06-14 03:48:47.482605
# Unit test for method __str__ of class First
def test_First___str__():
    assert str(First(10)) == 'Fist[value=10]'



# Generated at 2022-06-14 03:48:52.433585
# Unit test for method concat of class One
def test_One_concat():
    assert One(True).concat(One(False)) == One(True)
    assert One(False).concat(One(True)) == One(True)
    assert One(False).concat(One(False)) == One(False)


# Generated at 2022-06-14 03:48:55.692956
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    assert str(Sum(1)) == 'Sum[value=1]'
    assert str(Sum(2)) == 'Sum[value=2]'
    assert str(Sum(3)) == 'Sum[value=3]'


# Generated at 2022-06-14 03:48:58.895571
# Unit test for method concat of class Last
def test_Last_concat():
    assert Last(1).concat(Last(2)).value == 2
    assert Last(First(1)).concat(First(2)).value == First(2)
    assert Last(First(1)).concat(Last(2)).value == First(1)


# Generated at 2022-06-14 03:49:00.039438
# Unit test for constructor of class Semigroup
def test_Semigroup():
    assert Semigroup(1).value == 1


# Unit tests for Monoid



# Generated at 2022-06-14 03:49:06.124952
# Unit test for method concat of class Sum
def test_Sum_concat():
    assert Sum(1).concat(Sum(2)) == Sum(3)
    assert Sum(1).concat(Sum(2)).concat(Sum(3)) == Sum(6)



# Generated at 2022-06-14 03:49:08.244118
# Unit test for method concat of class Sum
def test_Sum_concat():
    assert Sum(1).concat(Sum(2)).value == 3



# Generated at 2022-06-14 03:49:11.625926
# Unit test for constructor of class Semigroup
def test_Semigroup():
    # check constructor
    s = Semigroup(10)
    assert s.value == 10



# Generated at 2022-06-14 03:49:20.279466
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    assert Sum(10).fold(lambda x: x + 10) == 10 + 10
    assert All(True).fold(lambda x: x and False) is True and False
    assert One(True).fold(lambda x: x or True) is True or True
    assert First(10).fold(lambda x: x + 10) == 10 + 10
    assert Last(10).fold(lambda x: x + 10) == 10 + 10
    assert Map({1: Sum(10), 2: Sum(20)}).fold(lambda x: x[2].value + 10) == 20 + 10
    assert Max(10).fold(lambda x: x + 10) == 10 + 10
    assert Min(10).fold(lambda x: x + 10) == 10 + 10


# Generated at 2022-06-14 03:49:29.078654
# Unit test for method concat of class Sum
def test_Sum_concat():
    assert Sum(4).concat(Sum(5)) == Sum(9)
    assert Sum(4).concat(Sum(0)) == Sum(4)
    assert Sum(0).concat(Sum(4)) == Sum(4)
    assert Sum(0).concat(Sum(0)) == Sum(0)
    assert Sum(4).concat(Sum(-5)) == Sum(-1)
    assert Sum(-5).concat(Sum(4)) == Sum(-1)
    assert Sum(-5).concat(Sum(-5)) == Sum(-10)


# Generated at 2022-06-14 03:49:32.000870
# Unit test for method __str__ of class All
def test_All___str__():
    assert str(All(False)) == "All[value=False]", "Must be All[value=False]"


# Generated at 2022-06-14 03:49:34.207169
# Unit test for method __str__ of class One
def test_One___str__():
    assert str(One(True)) == 'One[value=True]'
    assert str(One(False)) == 'One[value=False]'


# Generated at 2022-06-14 03:49:36.627525
# Unit test for method __str__ of class One
def test_One___str__():
    assert One(1).__str__() == "One[value=1]"



# Generated at 2022-06-14 03:49:39.529588
# Unit test for constructor of class Map
def test_Map():
    assert Map({0: Sum(1), 1: Sum(2)}).value == {0: Sum(1), 1: Sum(2)}

# Generated at 2022-06-14 03:49:41.290049
# Unit test for method __str__ of class Max
def test_Max___str__():
    max_1 = Max(1)
    assert str(max_1) == 'Max[value=1]'

# Generated at 2022-06-14 03:49:46.839082
# Unit test for method __str__ of class Min
def test_Min___str__():
    assert str(Min(1)) == "Min[value=1]"



# Generated at 2022-06-14 03:49:50.966952
# Unit test for method __str__ of class First
def test_First___str__():  # pragma: no cover
    actual = First('a').__str__()
    expected = "Fist[value=a]"
    assert actual == expected

    actual = First(5).__str__()
    expected = "Fist[value=5]"
    assert actual == expected


# Generated at 2022-06-14 03:49:54.309111
# Unit test for method __str__ of class One
def test_One___str__(): # pragma: no cover
    assert str(One(True)) == 'One[value=True]'



# Generated at 2022-06-14 03:49:58.352295
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    test_cases = [
        (All(True), bool(True)),
        (All(False), bool(False)),
        (Sum(1), 1),
        (Sum(0), 0),
        (Sum(-1), -1),
        (One(True), bool(True)),
        (One(False), bool(False)),
        (First(1), 1),
        (First(0), 0),
        (First(-1), -1),
        (Last(1), 1),
        (Last(0), 0),
        (Last(-1), -1),
        (Max(1), 1),
        (Max(0), 0),
        (Max(-1), -1),
        (Min(1), 1),
        (Min(0), 0),
        (Min(-1), -1),
    ]

# Generated at 2022-06-14 03:50:03.179724
# Unit test for method concat of class All
def test_All_concat():
    """
    Unit test for method concat of class All.
    """
    assert All(True).concat(All(False)).value == False



# Generated at 2022-06-14 03:50:04.808991
# Unit test for constructor of class Max
def test_Max():
    ma = Max(2)
    assert ma.value == 2

# Generated at 2022-06-14 03:50:10.010794
# Unit test for constructor of class All
def test_All():
    assert All(True)
    assert All(False)
    assert All(12)
    assert All(0)
    assert All('str')
    assert All(())
    assert All((), False)
    assert All({})
    assert All([])
    assert All([1, 2, 3])


# Generated at 2022-06-14 03:50:12.051998
# Unit test for method __str__ of class Last
def test_Last___str__():
    assert str(Last(9)) == "Last[value=9]"


# Generated at 2022-06-14 03:50:15.136856
# Unit test for constructor of class First
def test_First():
    check_constructor_and_repr(First(0))
    check_constructor_and_repr(First(1))


# Generated at 2022-06-14 03:50:23.843329
# Unit test for method concat of class Map
def test_Map_concat():
    m1 = Map({'a': Sum(1), 'b': Sum(2), 'c': Sum(3)})
    m2 = Map({'a': Sum(1), 'b': Sum(2), 'c': Sum(3), 'd': Sum(4)})

    result = m1.concat(m2)
    print(result.value)
    assert result.value == {'a': Sum(2), 'b': Sum(4), 'c': Sum(6), 'd': Sum(4)}


# Generated at 2022-06-14 03:50:28.826716
# Unit test for constructor of class Last
def test_Last():
    assert Last(10) == Last(10)



# Generated at 2022-06-14 03:50:30.451594
# Unit test for method concat of class Last
def test_Last_concat():
    assert Last(1).concat(Last(2)) == Last(2)


# Generated at 2022-06-14 03:50:34.775472
# Unit test for constructor of class Map
def test_Map():
    assert Map({
        'a': Sum(1), 'b': Sum(2)
    }) == Map({
        'a': Sum(1), 'b': Sum(2)
    })

# Generated at 2022-06-14 03:50:36.540618
# Unit test for method __str__ of class Last
def test_Last___str__():
    assert str(Last(5)) == 'Last[value=5]'


# Generated at 2022-06-14 03:50:40.587576
# Unit test for constructor of class First
def test_First(): 
    assert First(4) == First(4)
    assert First(4).value == 4
    assert First(2) != First(4)
    assert First('hi').value == 'hi'


# Generated at 2022-06-14 03:50:42.415440
# Unit test for constructor of class First
def test_First():
    assert First("a").value == "a"


# Generated at 2022-06-14 03:50:44.153246
# Unit test for constructor of class One
def test_One():
    assert One(True) == One(True)


# Generated at 2022-06-14 03:50:56.835634
# Unit test for method concat of class Map
def test_Map_concat():
    """
    Test function concat of class Map
    :return: None
    """
    map_concat = Map({})
    map_concat.concat(Map({1: Sum(1)}))
    assert map_concat.value == {1: Sum(1)}
    map_concat.concat(Map({2: All(True)}))
    assert map_concat.value == {1: Sum(1), 2: All(True)}
    map_concat.concat(Map({3: One(False)}))
    assert map_concat.value == {1: Sum(1), 2: All(True), 3: One(False)}
    map_concat.concat(Map({4: Max(5), 5: Min(8)}))

# Generated at 2022-06-14 03:50:58.735027
# Unit test for method concat of class Sum
def test_Sum_concat():
    assert Sum(2).concat(Sum(3)) == Sum(5)



# Generated at 2022-06-14 03:51:00.560761
# Unit test for method concat of class First
def test_First_concat():
    result = First(1).concat(First(2))
    assert result.value == 1
    assert result == First(1)


# Generated at 2022-06-14 03:51:08.712802
# Unit test for constructor of class Last
def test_Last():
    """
    >>> LAST = Last(42)
    >>> LAST
    Last[value=42]
    """
    pass


# Generated at 2022-06-14 03:51:10.664870
# Unit test for method concat of class Last
def test_Last_concat():
    assert Last(100).concat(Last(10)) == Last(10)


# Generated at 2022-06-14 03:51:15.599428
# Unit test for constructor of class Map
def test_Map():
    assert Map({'test': Sum(1)}).__str__() == 'Map[value={\'test\': Sum[value=1]}]'



# Generated at 2022-06-14 03:51:17.663498
# Unit test for constructor of class Sum
def test_Sum():
    assert Sum(1) == Sum(1)


# Unit tests for concat method of class Sum

# Generated at 2022-06-14 03:51:18.792133
# Unit test for constructor of class All
def test_All():  # pragma: no cover
    assert All(True).value == True


# Generated at 2022-06-14 03:51:23.368186
# Unit test for method concat of class One
def test_One_concat():
    assert One(False)  == One(False).concat(One(False))
    assert One(True)   == One(False).concat(One(True))
    assert One(True)   == One(True).concat(One(False))
    assert One(True)   == One(True).concat(One(True))


# Generated at 2022-06-14 03:51:26.891150
# Unit test for method __str__ of class All
def test_All___str__():  # pragma: no cover
    # Call method to test
    result = str(All(True))

    # Assert result
    assert result == 'All[value=True]'


# Generated at 2022-06-14 03:51:30.407448
# Unit test for method concat of class Min
def test_Min_concat():
    min = Min(7)
    min2 = Min(0)
    min3 = min.concat(min2)
    assert min3.value == 0


# Generated at 2022-06-14 03:51:33.246663
# Unit test for method __str__ of class All
def test_All___str__():
    assert str(All(True)) == 'All[value=True]'
    assert str(All(False)) == 'All[value=False]'


# Generated at 2022-06-14 03:51:35.609302
# Unit test for constructor of class First
def test_First():  # pragma: no cover
    assert First(1) == First(1)


# Generated at 2022-06-14 03:51:48.032594
# Unit test for method concat of class One
def test_One_concat():
    """
    Unit test for method concat of class One
    """
    assert One(False).concat(One(True)).value == True
    assert One(False).concat(One(False)).value == False
    assert One(True).concat(One(False)).value == True
    assert One(True).concat(One(True)).value == True


# Generated at 2022-06-14 03:51:49.569007
# Unit test for constructor of class Last
def test_Last():
    assert Last(5) == Last(5)


# Generated at 2022-06-14 03:51:50.575449
# Unit test for constructor of class Max
def test_Max():
    assert Max(1).value == 1


# Generated at 2022-06-14 03:51:54.376230
# Unit test for method concat of class One
def test_One_concat():
    assert One(1).concat(One(2)) == One(1)
    assert One('').concat(One(False)) == One('')
    assert One([]).concat(One(0)) == One([])


# Generated at 2022-06-14 03:52:05.783056
# Unit test for constructor of class Map
def test_Map():
    m = Map({'a': Sum(2), 'b': Sum(3)})
    assert 4 == m.concat(Map({'b': Sum(-5), 'c': Sum(10)})).value['b'].value
    # assert {'a': Sum[value=2], 'b': Sum[value=0], 'c': Sum[value=10]} == m.concat(Map({'b': Sum(-5), 'c': Sum(10)})).value
    assert -inf == m.concat(Map({'b': Sum(-5), 'c': Sum(10)})).value['a'].value
    assert 10 == m.concat(Map({'b': Sum(-5), 'c': Sum(10)})).value['c'].value

# Generated at 2022-06-14 03:52:11.718129
# Unit test for method concat of class One
def test_One_concat():
    assert One(True).concat(One(True)) == One(True)
    assert One(True).concat(One(False)) == One(True)
    assert One(False).concat(One(True)) == One(True)
    assert One(False).concat(One(False)) == One(False)



# Generated at 2022-06-14 03:52:15.381543
# Unit test for method concat of class Last
def test_Last_concat():
    assert Last(2).concat(Last(1)) == Last(1)
    assert Last(2).concat(First(1)) == Last(1)


# Generated at 2022-06-14 03:52:18.910460
# Unit test for method __str__ of class Map
def test_Map___str__(): assert str(Map({1: Sum(1), 2: Sum(2)})) == "Map[value={1: Sum[value=1], 2: Sum[value=2]}]"


# Generated at 2022-06-14 03:52:20.232255
# Unit test for method __str__ of class First
def test_First___str__():
    value = 'a'
    first = First(value)
    assert str(first) == 'Fist[value=a]'



# Generated at 2022-06-14 03:52:24.554278
# Unit test for constructor of class All
def test_All():  # pragma: no cover
    assert All(True).value == True
    assert All(False).value == False
    assert All(1).value == True
    assert All(0).value == False
    assert All("text").value == True
    assert All("").value == False


# Generated at 2022-06-14 03:52:43.552817
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(3).concat(Min(5)) == Min(3)
    assert Min(5).concat(Min(3)) == Min(3)
    assert Min(1).concat(Min(1)) == Min(1)



# Generated at 2022-06-14 03:52:45.806114
# Unit test for method concat of class One
def test_One_concat():
    assert One(False).concat(One(True)) == One(True)


# Generated at 2022-06-14 03:52:49.650895
# Unit test for method concat of class Last
def test_Last_concat():
    semigroup_1 = Last(1)
    semigroup_2 = Last(2)
    assert semigroup_1.concat(semigroup_2).value == 2



# Generated at 2022-06-14 03:52:50.772982
# Unit test for method __str__ of class First
def test_First___str__():
	instance = First('value')
	assert str(instance) == "Fist[value=value]"


# Generated at 2022-06-14 03:52:55.204186
# Unit test for method __str__ of class Map
def test_Map___str__():
    assert str(Map(value={'one': Sum(1), 'two': Sum(1)})) == 'Map[value={\'one\': Sum[value=1], \'two\': Sum[value=1]}]'


# Generated at 2022-06-14 03:52:59.637031
# Unit test for method concat of class One
def test_One_concat():
    assert One(1).concat(One(2)).value == True
    assert One(2).concat(One(0)).value == True
    assert One(1).concat(One(0)).value == False
    assert One(1).concat(One('string')).value == True


# Generated at 2022-06-14 03:53:01.224607
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    assert Semigroup(1).fold(lambda x: x) == 1



# Generated at 2022-06-14 03:53:05.351936
# Unit test for method concat of class One
def test_One_concat():
    value = One(True)
    other = One(False)
    assert value.concat(other).value == True



# Generated at 2022-06-14 03:53:07.282361
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(1)) == 'Max[value=1]'



# Generated at 2022-06-14 03:53:12.180464
# Unit test for method concat of class Map
def test_Map_concat():
    m = Map({'name': First('GoF'), 'count': Sum(1)})
    n = Map({'name': First('Clean Code'), 'count': Sum(3)})
    mn = m.concat(n)  # merge two maps

    assert (mn.value['name'] == First('GoF'))
    assert (mn.value['count'] == Sum(4))


# Generated at 2022-06-14 03:53:39.520002
# Unit test for constructor of class Sum
def test_Sum():
    assert Sum(1).value == 1

# Generated at 2022-06-14 03:53:41.039095
# Unit test for constructor of class Last
def test_Last():
    _l = Last(1)
    assert _l.value == 1, "value must be 1"


# Generated at 2022-06-14 03:53:43.960223
# Unit test for method concat of class First
def test_First_concat():
    element_1 = First("first")
    element_2 = First("second")
    assert element_1.concat(element_2) == First("first")



# Generated at 2022-06-14 03:53:44.941477
# Unit test for constructor of class Min
def test_Min():
    assert Min(2).value == 2



# Generated at 2022-06-14 03:53:51.547485
# Unit test for method concat of class One
def test_One_concat():
    result = One(False).concat(One(True))
    assert result == One(True)

    result = One(True).concat(One(False))
    assert result == One(True)

    result = One(False).concat(One(False))
    assert result == One(False)

    result = One(True).concat(One(True))
    assert result == One(True)


# Generated at 2022-06-14 03:53:55.451441
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(10)) == 'Max[value=10]'
    assert str(Max(-20)) == 'Max[value=-20]'
    assert str(Max(0)) == 'Max[value=0]'


# Generated at 2022-06-14 03:53:58.940762
# Unit test for method __str__ of class Map
def test_Map___str__():
    assert str(Map({'a': Sum(1), 'b': One(False), 'c': First(10)})) == "Map[value={'a': Sum[value=1], 'b': All[value=False], 'c': Fist[value=10]}]"


# Generated at 2022-06-14 03:54:00.721591
# Unit test for constructor of class Max
def test_Max():
    assert Max(1).value == 1


# Generated at 2022-06-14 03:54:13.086332
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    assert All(0).fold(bool) == False
    assert All(1).fold(bool) == True
    assert All(1).fold(str) == 'True'
    assert All(0).fold(str) == 'False'
    assert All(1).fold(lambda x: x+1) == 2
    assert All(0).fold(lambda x: x+1) == 1
    assert All(1).fold(bool) == True
    assert All(1).fold(lambda x: x+1) == 2
    assert One(0).fold(bool) == False
    assert One(1).fold(bool) == True
    assert One(0).fold(str) == 'False'
    assert One(1).fold(str) == 'True'
    assert One(0).fold(lambda x: x+1) == 1

# Generated at 2022-06-14 03:54:15.375526
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(1).concat(Max(2)) == Max(2)
