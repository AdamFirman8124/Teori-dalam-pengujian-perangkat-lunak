

# Generated at 2022-06-14 03:44:35.251060
# Unit test for method concat of class Min
def test_Min_concat():
    try:
        Min(1).concat(Min(2))
        assert False
    except Exception as e:
        assert e.__class__.__name__ == 'TypeError'


# Generated at 2022-06-14 03:44:38.551537
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(1).concat(Min(2)) == Min(1)
    assert Min(2).concat(Min(2)) == Min(2)
    assert Min(2).concat(Min(1)) == Min(1)


# Generated at 2022-06-14 03:44:42.457153
# Unit test for method concat of class Min
def test_Min_concat():
    newMin = Min(200)
    newMin1 = Min(300)
    assert newMin.concat(newMin1).value == newMin1.value



# Generated at 2022-06-14 03:44:47.382371
# Unit test for method concat of class Min
def test_Min_concat():
    # Given
    min_instance_1 = Min(1)
    min_instance_2 = Min(2)
    expected = Min(1)

    # When
    actual = min_instance_1.concat(min_instance_2)

    # Then
    assert actual == expected


# Generated at 2022-06-14 03:44:49.897885
# Unit test for method concat of class Min
def test_Min_concat():
    import pytest
    result = Min(1).concat(Min(2))
    expected = Min(1)
    assert result == expected, 'should be right'



# Generated at 2022-06-14 03:44:52.916816
# Unit test for method concat of class Min
def test_Min_concat():
    min_a = Min(1)
    min_b = Min(2)
    min_c = min_a.concat(min_b)
    assert min_c.value == 1


# Generated at 2022-06-14 03:44:54.845605
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(-1).concat(Min(-2)) == Min(-2)
    assert Min(-1).concat(Min(-0.1)) == Min(-1)


# Generated at 2022-06-14 03:44:57.417559
# Unit test for method concat of class Min
def test_Min_concat():
    """
    Test concat value with current Sum instance
    """
    assert Min(1).concat(Min(2)).value == 1



# Generated at 2022-06-14 03:45:03.440801
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(3).concat(Min(4)) == Min(3)
    assert Min(4).concat(Min(3)) == Min(3)
    assert Min(4).concat(Min(4)) == Min(4)


# Generated at 2022-06-14 03:45:05.295180
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(1).concat(Min(3)).value == 1



# Generated at 2022-06-14 03:45:08.943962
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    assert 'Sum' in str(Sum(3))



# Generated at 2022-06-14 03:45:11.209403
# Unit test for constructor of class All
def test_All():  # pragma: no cover
    assert(All(True).value == True)
    assert(All(False).value == False)


# Generated at 2022-06-14 03:45:17.179331
# Unit test for method __str__ of class One
def test_One___str__():
    assert One(1).__str__() == "One[value=1]"
    assert One(0).__str__() == "One[value=0]"
    assert One(False).__str__() == "One[value=False]"
    assert One(True).__str__() == "One[value=True]"


# Generated at 2022-06-14 03:45:18.992984
# Unit test for constructor of class Last
def test_Last():
    last = Last(1)
    assert last.value == 1



# Generated at 2022-06-14 03:45:20.663598
# Unit test for method __str__ of class Last
def test_Last___str__():
    assert str(Last(1)) == "Last[value=1]"

# Generated at 2022-06-14 03:45:21.978735
# Unit test for method concat of class One
def test_One_concat():
    assert One(True).concat(One(False)) == True
    assert One(False).concat(One(True)) == True
    assert One(False).concat(One(False)) == False



# Generated at 2022-06-14 03:45:23.894161
# Unit test for method __str__ of class One
def test_One___str__():
    assert str(One(True)) == 'One[value=True]'



# Generated at 2022-06-14 03:45:32.629601
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():  # pragma: no cover
    assert Semigroup(1).fold(lambda x: x + 1) == 2
    assert Semigroup(1).fold(lambda x: x - 1) == 0
    assert Semigroup(2).fold(lambda x: x * 2) == 4
    assert Semigroup(6).fold(lambda x: x / 3) == 2
    assert Semigroup(1).fold(lambda x: x ** 2) == 1
    assert Semigroup("string").fold(lambda x: x[1:]) == "tring"
    assert Semigroup("string").fold(lambda x: len(x)) == 6
    assert Semigroup([1, 2, 3]).fold(lambda x: x[0]) == 1



# Generated at 2022-06-14 03:45:34.569094
# Unit test for method __str__ of class Last
def test_Last___str__():
    assert str(Last(1)) == 'Last[value=1]'



# Generated at 2022-06-14 03:45:35.684252
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(5)) == 'Max[value=5]'



# Generated at 2022-06-14 03:45:43.589622
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(10).concat(Min(20)).value == 10
    assert Min(10).concat(Min(5)).value == 5
    assert Min(20).concat(Min(10)).value == 10
    assert Min(5).concat(Min(10)).value == 5


# Generated at 2022-06-14 03:45:44.879382
# Unit test for constructor of class Max
def test_Max():
    assert Max(3).value == 3


# Generated at 2022-06-14 03:45:47.154709
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    assert Semigroup(1) == Semigroup(1)



# Generated at 2022-06-14 03:45:49.174583
# Unit test for method __str__ of class Min
def test_Min___str__():
    a = Min(1)
    assert str(a) == 'Min[value=1]'


# Generated at 2022-06-14 03:45:53.024900
# Unit test for method concat of class Last
def test_Last_concat():
    """
    It will test method concat of class Last
    """
    first = Last(1)
    second = Last(2)
    result = first.concat(second)
    expected = Last(2)
    assert result == expected


# Generated at 2022-06-14 03:45:57.360567
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    assert S(23) == S(23)
    assert First(23) == First(23)
    assert Map({'first': S(23), 'second': S(42)}) == Map({'first': S(23), 'second': S(42)})



# Generated at 2022-06-14 03:46:03.404931
# Unit test for constructor of class First
def test_First():
    assert First(10) == First(10)
    assert First(10) != Sum(10)
    assert First(10) != All(10)
    assert First(10) != One(10)
    assert First(10) != Last(10)
    assert First(10) != Map({'a': 1})
    assert First(10) != Max(10)
    assert First(10) != Min(10)



# Generated at 2022-06-14 03:46:04.488623
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    assert Min(1).fold(lambda x: x + 1) == 2


# Generated at 2022-06-14 03:46:06.094126
# Unit test for method __str__ of class Last
def test_Last___str__():
    assert (str(Last(1)) == 'Last[value=1]')


# Generated at 2022-06-14 03:46:08.392626
# Unit test for method concat of class Sum
def test_Sum_concat():
    for a, b in EXAMPLES:
        assert Sum(a).concat(Sum(b)) == Sum(a + b)



# Generated at 2022-06-14 03:46:14.651157
# Unit test for method concat of class Min
def test_Min_concat():
    val = Min(1).concat(Min(2))
    assert val == Min(1)
    val = Min(2).concat(Min(1))
    assert val == Min(1)


# Generated at 2022-06-14 03:46:15.928190
# Unit test for constructor of class Semigroup
def test_Semigroup():
    assert Semigroup(3) == Semigroup(3)


# Generated at 2022-06-14 03:46:17.157011
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(2).concat(Min(3)).value == 2


# Generated at 2022-06-14 03:46:22.875761
# Unit test for method concat of class First
def test_First_concat():
    assert First(1).concat(First(2)).value == 1
    assert First(1).concat(First(0)).value == 1
    assert First(2).concat(First(0)).value == 2
    assert First(2).concat(First(3)).value == 2


# Generated at 2022-06-14 03:46:24.656679
# Unit test for method concat of class First
def test_First_concat():
    assert First(1).concat(First(2)).value == 1


# Generated at 2022-06-14 03:46:26.467797
# Unit test for constructor of class Max
def test_Max():
    assert Max(2.0) == Max(2.0)



# Generated at 2022-06-14 03:46:27.745361
# Unit test for constructor of class First
def test_First():
    assert First("2") == First("2")

# Generated at 2022-06-14 03:46:29.333839
# Unit test for constructor of class Min
def test_Min():
    assert Min(1) == Min(1)

# Generated at 2022-06-14 03:46:39.230470
# Unit test for method concat of class Map
def test_Map_concat():
    m1 = Map({1: First(1), 2: First(2), 3: First(3)})
    m2 = Map({1: Last(10), 2: Last(20), 3: Last(30)})
    m3 = Map({1: First(1), 2: Last(20), 3: First(3)})
    m4 = Map({1: First(1), 2: First(2), 3: Last(30)})
    m5 = Map({1: Last(10), 2: First(2), 3: First(3)})
    m6 = Map({1: First(1), 2: Last(20), 3: Last(30)})

    m1_m2 = m1.concat(m2)
    m1_m7 = m1.concat(m1)
    m1_m3 = m1

# Generated at 2022-06-14 03:46:42.147497
# Unit test for method concat of class Last
def test_Last_concat():  # pragma: no cover
    a = Last("ABC")
    b = Last("DEF")
    c = a.concat(b)
    assert c.value == "DEF"



# Generated at 2022-06-14 03:46:47.124453
# Unit test for method __str__ of class Min
def test_Min___str__():
    assert str(Min(10)) == 'Min[value=10]'


# Generated at 2022-06-14 03:46:52.399171
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    assert Semigroup(1).fold(lambda x: x) == 1, "The test_Semigroup_fold method is failed"
    assert Semigroup(2).fold(lambda x: x) == 2, "The test_Semigroup_fold method is failed"
    assert Semigroup("a").fold(lambda x: x) == "a", "The test_Semigroup_fold method is failed"
    print("The test_Semigroup_fold method is passed")



# Generated at 2022-06-14 03:46:59.370155
# Unit test for method concat of class Map
def test_Map_concat():
    assert DeepMap.concat({"a":All(1),"b":All(2)})({"a":All(3),"b":All(4)}) == Map({"a":All(1),"b":All(2)})

    assert Map({"a":All(1),"b":All(2)}).concat(Map({"a":All(3),"b":All(4)})) == Map({"a":All(1),"b":All(2)})

# Generated at 2022-06-14 03:47:01.220759
# Unit test for method concat of class First
def test_First_concat():
    assert First('Bla').concat(First('Bla')) == First('Bla')



# Generated at 2022-06-14 03:47:03.947491
# Unit test for constructor of class Sum
def test_Sum():
    assert Sum(4) == Sum(4)



# Generated at 2022-06-14 03:47:05.992244
# Unit test for method concat of class Last
def test_Last_concat():
    assert Last(1).concat(Last(2)) == Last(2)

# Generated at 2022-06-14 03:47:10.638057
# Unit test for method concat of class One
def test_One_concat():
    assert One(False).concat(One(False)) == One(False)
    assert One(False).concat(One(True)) == One(True)
    assert One(True).concat(One(False)) == One(True)
    assert One(True).concat(One(True)) == One(True)


# Generated at 2022-06-14 03:47:16.647848
# Unit test for method __str__ of class Map
def test_Map___str__():  # pragma: no cover
    m = Map({
        'zero': Sum(0),
        'one': Sum(1),
        'two': Sum(2),
    })
    assert str(m) == "Map[value={'zero': Sum[value=0], 'two': Sum[value=2], 'one': Sum[value=1]}]"



# Generated at 2022-06-14 03:47:17.951823
# Unit test for method concat of class First
def test_First_concat():
    assert First(1).concat(First(2)).value == 1



# Generated at 2022-06-14 03:47:22.302719
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    assert Semigroup(1).fold(lambda x: x + 1) == 2
    assert Semigroup(4).fold(lambda x: x + 1) == 5
    assert Semigroup(7).fold(lambda x: x + 1) == 8
    assert Semigroup(10).fold(lambda x: x + 1) == 11


# Generated at 2022-06-14 03:47:31.836835
# Unit test for method concat of class Min
def test_Min_concat():
    min_number = Min(10).concat(Min(5))
    assert min_number.value == 5  # => True

# Generated at 2022-06-14 03:47:39.456784
# Unit test for method concat of class Sum
def test_Sum_concat():
    assert Sum(1).concat(Sum(2)) == Sum(3)
    assert Sum(2).concat(Sum(1)) == Sum(3)
    assert Sum(2).concat(Sum(3)) == Sum(5)
    assert Sum(4).concat(Sum(1)) == Sum(5)
    s = Sum(0).concat(Sum(1))
    assert s.value == 1



# Generated at 2022-06-14 03:47:45.606707
# Unit test for method __str__ of class Map
def test_Map___str__():
    with pytest.raises(AttributeError):
        Map({'key1': Sum(1), 'key2': Sum(2), 'key3': Sum(3), 'key4': Sum(4), 'key5': Sum(5)})
        Map({'key1': Sum(1), 'key2': Sum(2), 'key3': Sum(3), 'key4': Sum(4), 'key5': Sum(5)}).__str__()


# Generated at 2022-06-14 03:47:47.861527
# Unit test for constructor of class One
def test_One():

    one = One(False)
    assert one.value == False


# Generated at 2022-06-14 03:47:52.027958
# Unit test for method concat of class Max
def test_Max_concat():
    m = Max(0)
    assert m.concat(Max(0)) == Max(0)
    assert m.concat(Max(1)) == Max(1)
    assert m.concat(Max(-1)) == Max(0)



# Generated at 2022-06-14 03:47:54.146879
# Unit test for method __str__ of class Last
def test_Last___str__():  # pragma: no cover
    l = Last(10)

    assert str(l) == 'Last[value=10]'


# Generated at 2022-06-14 03:47:59.500784
# Unit test for method concat of class One
def test_One_concat():
    assert One(True).concat(One(0)) == One(True)
    assert One(0).concat(One(True)) == One(True)
    assert One(0).concat(One(False)) == One(False)
    assert One(False).concat(One(0)) == One(False)


# Generated at 2022-06-14 03:48:05.318590
# Unit test for method concat of class Map
def test_Map_concat():
    m1 = Map({1: All(True), 2: Min(100)})
    m2 = Map({1: All(False), 2: Min(200), 3: Sum(1000)})
    assert m1.concat(m2) == Map({1: All(False), 2: Min(100), 3: Sum(1000)})


# Generated at 2022-06-14 03:48:07.429235
# Unit test for constructor of class First
def test_First():
    first_one = First(1)
    assert first_one.value == 1


# Generated at 2022-06-14 03:48:09.877103
# Unit test for method __str__ of class One
def test_One___str__():
    assert str(One("red")) == "One[value=red]", "Method __str__ of class One doesn't work"


# Generated at 2022-06-14 03:48:17.783170
# Unit test for method __str__ of class All
def test_All___str__():
    assert str(All(True)) == 'All[value=True]'
    assert str(All(False)) == 'All[value=False]'


# Generated at 2022-06-14 03:48:22.514138
# Unit test for method concat of class Sum
def test_Sum_concat():
    assert Sum(2).concat(Sum(3)) == Sum(5)
    assert Sum(3).concat(Sum(3)) == Sum(6)
    assert Sum(1).concat(Sum(0)) == Sum(1)


# Generated at 2022-06-14 03:48:24.013571
# Unit test for method __str__ of class One
def test_One___str__():
    assert str(One(True)) == 'One[value=True]'


# Generated at 2022-06-14 03:48:28.607457
# Unit test for method concat of class One
def test_One_concat():
    assert One(1).concat(One(2)) == One(True)
    assert One(0).concat(One(0)) == One(False)
    assert One(0).concat(One(1)) == One(True)
    assert One(1).concat(One(0)) == One(True)


# Generated at 2022-06-14 03:48:32.021379
# Unit test for method concat of class Last
def test_Last_concat():
    """
    Expected result:
    Last object with value = 1
    :=
    Last object with value = 2
    """

    assert Last(1).concat(Last(2))



# Generated at 2022-06-14 03:48:33.890246
# Unit test for constructor of class Max
def test_Max():
    assert Max(4) == Max(4)


# Generated at 2022-06-14 03:48:35.203770
# Unit test for method __str__ of class All
def test_All___str__():
    all_ = All(True)
    assert str(all_) == 'All[value=True]'



# Generated at 2022-06-14 03:48:36.307686
# Unit test for method __str__ of class One
def test_One___str__():
    assert str(One(True)) == 'One[value=True]'



# Generated at 2022-06-14 03:48:39.997678
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(1)) == 'Max[value=1]'


# Generated at 2022-06-14 03:48:42.608244
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert(str(Max(0)) == "Max[value=0]")
    assert(str(Max(1)) == "Max[value=1]")


# Generated at 2022-06-14 03:48:59.070831
# Unit test for constructor of class Map
def test_Map():
    """
    Test that the constructor of Map will initialize with the correct value.
    """
    m = Map({"a": Sum(5), "b": All(True)})
    assert m.value == {"a": Sum(5), "b": All(True)}


# Generated at 2022-06-14 03:49:01.653222
# Unit test for method concat of class First
def test_First_concat():
    # arrange
    s = First(100)
    s2 = First(10)
    # act
    result = s.concat(s2)
    # assert
    assert result.value == 100


# Generated at 2022-06-14 03:49:04.007802
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(10).concat(Max(20)).value == 20

# Generated at 2022-06-14 03:49:09.618263
# Unit test for method concat of class All
def test_All_concat():
    assert All(True).concat(All(True)) == All(True)
    assert All(False).concat(All(True)) == All(False)
    assert All(True).concat(All(False)) == All(False)
    assert All(False).concat(All(False)) == All(False)
    assert All(False).concat(All(False)) == All(False)
    assert All(All(True)).concat(All(All(False))) == All(All(False))


# Generated at 2022-06-14 03:49:12.577514
# Unit test for method __str__ of class One
def test_One___str__():
    one = One(True)
    assert __str__(one) == 'One[value=True]'


# Generated at 2022-06-14 03:49:15.799731
# Unit test for method __str__ of class Map
def test_Map___str__():  # pragma: no cover
    assert str(Map({'a': Sum(1)})) == 'Map[value={\'a\': Sum[value=1]}]'  # pragma: no cover



# Generated at 2022-06-14 03:49:19.643213
# Unit test for constructor of class One
def test_One():
    assert One("1").value == "1"
    assert One("2").value == "2"
    assert str(One("1")) == "One[value=1]"



# Generated at 2022-06-14 03:49:24.371118
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    # Given
    semigroup1 = Semigroup(10)
    semigroup2 = Semigroup(10)
    semigroup3 = Semigroup(20)

    # When
    result1 = semigroup1 == semigroup2
    result2 = semigroup1 == semigroup3
    result3 = semigroup1 == First(10)

    # Then
    assert result1 is True
    assert result2 is False
    assert result3 is False



# Generated at 2022-06-14 03:49:28.904784
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():  # pragma: no cover
    assert 0 == Sum(0).fold(lambda v: v)
    assert All(True).fold(lambda v: v)
    assert First(1).fold(lambda v: v) == 1
    assert Min(1).fold(lambda v: v) == 1
    assert Map({}).fold(lambda v: v) == {}



# Generated at 2022-06-14 03:49:32.682157
# Unit test for method concat of class First
def test_First_concat():
    """
    :returns: pyrtype.utils.Semigroup.First
    """
    return First('Hello').concat(First('World'))
first_test = test_First_concat()


# Generated at 2022-06-14 03:49:52.841438
# Unit test for method concat of class Map
def test_Map_concat():
    d1 = {1: First(1), 2: First(2)}
    d2 = {1: First(3), 2: First(4)}
    assert Map(d1).concat(Map(d2)).value[1].value == 3
    assert Map(d1).concat(Map(d2)).value[2].value == 4
    assert Map(d1).concat(Map(d2)).value[1].value == Map(d2).concat(Map(d1)).value[1].value
    assert Map(d1).concat(Map(d2)).value[2].value == Map(d2).concat(Map(d1)).value[2].value


# Generated at 2022-06-14 03:49:55.085886
# Unit test for method concat of class Last
def test_Last_concat():
    last = Last(1)
    assert last.concat(Last(2)) == Last(2)



# Generated at 2022-06-14 03:49:57.092436
# Unit test for method __str__ of class First
def test_First___str__():
    first = First('test')
    assert str(first) == "Fist[value=test]"


# Generated at 2022-06-14 03:50:01.404175
# Unit test for constructor of class Sum
def test_Sum():
    """
    Test for constructor of class Sum
    """
    assert type(Sum(1)) == Sum
    assert type(Sum(2)) == Sum
    assert Sum(1).value == 1
    assert Sum(2).value == 2


# Generated at 2022-06-14 03:50:07.693098
# Unit test for method concat of class All
def test_All_concat():
    assert All(True).concat(All(True)).value == All(True).value
    assert All(True).concat(All(False)).value == All(False).value
    assert All(False).concat(All(False)).value == All(False).value
    assert All(False).concat(All(True)).value == All(False).value


# Generated at 2022-06-14 03:50:10.008740
# Unit test for method __str__ of class First
def test_First___str__():  # pragma: no cover
    assert str(First(1)) == 'Fist[value=1]'



# Generated at 2022-06-14 03:50:12.050677
# Unit test for constructor of class One
def test_One():
    one = One(True)
    assert one.value == True


# Generated at 2022-06-14 03:50:25.429855
# Unit test for method concat of class One
def test_One_concat():  # pragma: no cover
    from datetime import datetime
    start = datetime.now()
    end = start.replace(second=start.second + 1)

    assert One("foobar").concat(One("fizzbuzz")) == One("foobar")
    assert One("foobar").concat(One(1)) == One("foobar")
    assert One(start).concat(One(end)) == One(start)

    assert One("foobar").concat(One("")) == One("foobar")
    assert One("foobar").concat(One(0)) == One("foobar")
    assert One("foobar").concat(One(None)) == One("foobar")

    assert One("foobar").concat(One([1, 2, 3])) == One("foobar")

# Generated at 2022-06-14 03:50:28.142669
# Unit test for constructor of class All
def test_All():
    assert All(False) != All(True)
    assert All(True) == All(True)



# Generated at 2022-06-14 03:50:30.198345
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(100)) == 'Max[value=100]'

# Unit tests for method concat of class Max

# Generated at 2022-06-14 03:50:45.861486
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(1)) == 'Max[value=1]'


# Generated at 2022-06-14 03:50:47.526946
# Unit test for method concat of class Sum
def test_Sum_concat():
    assert Sum(2).concat(Sum(2)).value == 4



# Generated at 2022-06-14 03:50:50.401624
# Unit test for method __str__ of class Max
def test_Max___str__():
    from vkinder.functional.Monoid import Max

    assert Max(1).__str__() == 'Max[value=1]'



# Generated at 2022-06-14 03:50:53.300966
# Unit test for method concat of class Last
def test_Last_concat():
    assert Last(10).concat(Last(20)) == Last(20)



# Generated at 2022-06-14 03:50:54.856593
# Unit test for constructor of class One
def test_One():
    One(True)
    One(False)


# Generated at 2022-06-14 03:50:56.543509
# Unit test for method __str__ of class First
def test_First___str__():
    assert "Fist[value=Hello World]" == str(First("Hello World"))



# Generated at 2022-06-14 03:50:59.105889
# Unit test for method concat of class Max
def test_Max_concat():  # pragma: no cover
    actual = Max(2).concat(Max(3))
    expected = Max(3)
    assert actual == expected


# Generated at 2022-06-14 03:51:00.816278
# Unit test for constructor of class Sum
def test_Sum():  # pragma: no cover
    assert Sum(1).value == 1


# Generated at 2022-06-14 03:51:03.026515
# Unit test for constructor of class Map
def test_Map():
    assert Map({'sum': Sum(1), 'all': All(False)}) == Map({'sum': Sum(1), 'all': All(False)})


# Generated at 2022-06-14 03:51:04.579305
# Unit test for constructor of class Semigroup
def test_Semigroup():
    semigroup = Semigroup(10)
    assert semigroup.value == 10



# Generated at 2022-06-14 03:51:18.864711
# Unit test for constructor of class Sum
def test_Sum():
    assert Sum(2) == Sum(2)



# Generated at 2022-06-14 03:51:20.715059
# Unit test for method __str__ of class One
def test_One___str__():
    assert str(One(1)) == "One[value=1]"

# Usage test for method concat of class One

# Generated at 2022-06-14 03:51:22.386514
# Unit test for constructor of class Min
def test_Min():
    assert Min(10).value == 10


# Generated at 2022-06-14 03:51:24.652856
# Unit test for constructor of class Max
def test_Max():
    s = Max(1)
    assert s.value == 1



# Generated at 2022-06-14 03:51:27.639687
# Unit test for constructor of class Min
def test_Min():
    a = Min(1)
    assert 1 == a.value
    assert Min.neutral_element == Min.neutral().value


# Generated at 2022-06-14 03:51:30.071150
# Unit test for constructor of class One
def test_One():  # pragma: no cover

    one = One(1)
    assert one.value == 1


# Generated at 2022-06-14 03:51:32.421146
# Unit test for constructor of class Last
def test_Last():
    t_semigroup = Last(1)
    assert t_semigroup.value == 1


# Generated at 2022-06-14 03:51:36.868452
# Unit test for constructor of class Map
def test_Map():  # pragma: no cover

    map = Map({'name': Sum(1), 'surname': Sum(2)})

    assert map.value['name'].value == 1
    assert map.value['surname'].value == 2


# Generated at 2022-06-14 03:51:38.914427
# Unit test for method __str__ of class Last
def test_Last___str__():
    assert str(Last(4)) == 'Last[value=4]', '__str__ should return a "Last[value=4]" here'


# Generated at 2022-06-14 03:51:41.577130
# Unit test for constructor of class Sum
def test_Sum():
    assert Sum(1).value == 1
    assert Sum(2).value == 2


# Generated at 2022-06-14 03:51:58.757729
# Unit test for method __str__ of class Last
def test_Last___str__():
    # given
    last_semigroup = Last(100)
    # then
    assert str(last_semigroup) == "Last[value=100]"


# Generated at 2022-06-14 03:52:08.431186
# Unit test for method concat of class One
def test_One_concat():
    one = One("a")
    one2 = One("b")
    one3 = One("c")
    assert one.concat(one2).concat(one3).value == "a"
    assert one.concat(one2.concat(one3)).value == "a"
    assert one2.concat(one).concat(one3).value == "b"
    assert one.concat(one3).concat(one2).value == "a"
    assert one3.concat(one).concat(one2).value == "c"

    one4 = One(None)
    one5 = One(None)
    one6 = One("x")
    assert one4.concat(one5).concat(one6).value == None

# Generated at 2022-06-14 03:52:15.092575
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    # Given
    value = 1
    semigroup = Sum(value)
    expected_str_result = 'Sum[value={}]'.format(value)
    # When
    result = str(semigroup)
    # Then
    assert result == expected_str_result, "Expected is {} but got {}".format(expected_str_result, result)


# Generated at 2022-06-14 03:52:19.029040
# Unit test for method concat of class First
def test_First_concat():
    first = First(1)
    second = First(2)
    assert first.concat(second) == First(1)
    assert second.concat(first) == First(2)



# Generated at 2022-06-14 03:52:23.077091
# Unit test for method concat of class Map
def test_Map_concat():
    x = Map({'a': Sum(1), 'b': Sum(2), 'c': Sum(3)})
    y = Map({'a': Sum(4), 'b': Sum(5), 'c': Sum(6)})
    z = Map({'a': Sum(5), 'b': Sum(7), 'c': Sum(9)})
    assert x.concat(y) == z



# Generated at 2022-06-14 03:52:25.290389
# Unit test for method __str__ of class Min
def test_Min___str__():
    # Assert that the method __str__ of class Min returns correct value
    assert str(Min(1)) == "Min[value=1]"


# Generated at 2022-06-14 03:52:29.295282
# Unit test for method concat of class All
def test_All_concat():
    assert All(True).concat(All(False)) == All(False)
    assert All(True).concat(All(True)) == All(True)
    assert All(False).concat(All(True)) == All(False)
    assert All(False).concat(All(False)) == All(False)


# Generated at 2022-06-14 03:52:31.097224
# Unit test for method __str__ of class Min
def test_Min___str__():
    assert str(Min(1)) == 'Min[value=1]'


# Generated at 2022-06-14 03:52:33.337775
# Unit test for method concat of class Sum
def test_Sum_concat():  # pragma: no cover
    sum_result = Sum(1).concat(Sum(2))
    assert sum_result.value == 3


# Generated at 2022-06-14 03:52:35.464580
# Unit test for constructor of class Last
def test_Last():
    """
    It should return instance of Last
    """
    actual = Last(1)
    expected = Last(1)
    assert actual == expected



# Generated at 2022-06-14 03:53:08.405074
# Unit test for method __str__ of class Map
def test_Map___str__():
    semigroup = Map({1: 1, 2: 2})
    assert str(semigroup) == 'Map[value={1: 1, 2: 2}]'


# Generated at 2022-06-14 03:53:10.884549
# Unit test for method __str__ of class Max
def test_Max___str__():
    # Arrange
    m = Max(10)
    excepted = 'Max[value=10]'

    # Act
    result = str(m)

    # Assert
    assert result == excepted



# Generated at 2022-06-14 03:53:13.839182
# Unit test for method concat of class One
def test_One_concat():
    assert One(False).concat(One(False)) == One(False)
    assert One(False).concat(One(True)) == One(True)
    assert One(True).concat(One(False)) == One(True)
    assert One(True).concat(One(True)) == One(True)


# Generated at 2022-06-14 03:53:15.378831
# Unit test for constructor of class Map
def test_Map():
    assert Map({'a': Sum(1), 'b': Sum(2)}).value == {'a': Sum(1), 'b': Sum(2)}


# Generated at 2022-06-14 03:53:16.043882
# Unit test for method __str__ of class One
def test_One___str__():
    pass

# Generated at 2022-06-14 03:53:18.425192
# Unit test for constructor of class Min
def test_Min():
    assert type(Min(2)) is Min
    assert Min(2).value == 2


# Generated at 2022-06-14 03:53:20.318910
# Unit test for constructor of class First
def test_First():
    """
    To test constructor of class First
    """
    assert(First(1).value == 1)



# Generated at 2022-06-14 03:53:23.114105
# Unit test for method __str__ of class Last
def test_Last___str__():
    assert str(Last(1)) == "Last[value=1]", "We expect Last[value=1], we got " + str(Last(1))

# Generated at 2022-06-14 03:53:26.396625
# Unit test for method __str__ of class One
def test_One___str__():
    x = One(10)
    y = One(20)
    assert x.__str__() == 'One[value=10]'
    assert y.__str__() == 'One[value=20]'


# Generated at 2022-06-14 03:53:30.230029
# Unit test for constructor of class Min
def test_Min():
    min_value = Min(2)
    assert min_value.value == 2
    assert min_value.neutral_element == float("inf")



# Generated at 2022-06-14 03:54:12.941449
# Unit test for method concat of class Map
def test_Map_concat():
    assert Map({'a': Sum(1)}).concat(Map({'a': Sum(2)})).value == {
        'a': Sum(3)}
    assert Map({'a': All(True), 'b': All(False)}).concat(
        Map({'a': All(False), 'b': All(False)})).value == {
            'a': All(False),
            'b': All(False)
        }
    assert Map({'a': One(True)}).concat(Map({'a': One(True)})).value == {
        'a': One(True)}

# Generated at 2022-06-14 03:54:14.831496
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(5)) == "Max[value=5]" 


# Generated at 2022-06-14 03:54:25.905435
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    """
    fold :: (a -> b) -> Semigroup a -> b
    :returns: a new Semigroup of type b
    :rtype: Semigroup[b]
    """

    assert Sum(1).fold(lambda x: x + 1) == 2
    assert Sum(1).fold(lambda x: x * 3) == 3
    assert Sum(1).fold(lambda x: "hello") == "hello"

    assert All(True).fold(lambda x: x) == True
    assert All(True).fold(lambda x: "hello") == "hello"
    assert All(False).fold(lambda x: "hello") == False

    assert First(1).fold(lambda x: x + 1) == 1
    assert First(1).fold(lambda x: x * 3) == 1

# Generated at 2022-06-14 03:54:37.405525
# Unit test for method concat of class Map
def test_Map_concat():
    assert type(Map([1, 2, 3]).concat(Map([1, 2]))) == Map
    assert type(Map([1, 2, 3]).concat(Sum(1))) == Map
    assert type(Map([1, 2, 3]).concat(All(True))) == Map
    assert type(Map([1, 2, 3]).concat(One(True))) == Map
    assert type(Map([1, 2, 3]).concat(First(1))) == Map
    assert type(Map([1, 2, 3]).concat(Last(1))) == Map
    assert type(Map([1, 2, 3]).concat(Max(3))) == Map
    assert type(Map([1, 2, 3]).concat(Min(3))) == Map
