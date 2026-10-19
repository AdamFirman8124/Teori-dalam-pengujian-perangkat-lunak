

# Generated at 2022-06-14 03:44:42.410231
# Unit test for method concat of class Min
def test_Min_concat():
    """
    :returns: list with status
    :rtype: list[(bool, str)]
    """
    tests = [
        (
            Min(5).concat(Min(2)) == Min(2),
            'Min(5).concat(Min(2)) == Min(2)'
        ),
        (
            Min(2).concat(Min(5)) == Min(2),
            'Min(2).concat(Min(5)) == Min(2)'
        ),
        (
            Min(2).concat(Min(2)) == Min(2),
            'Min(2).concat(Min(2)) == Min(2)'
        )
    ]
    for func, desc in tests:
        if not func:
            print(desc)
            return desc
    return []

# Generated at 2022-06-14 03:44:54.354975
# Unit test for method concat of class Map
def test_Map_concat():
    assert Map({}).concat(Map({})) == Map({})
    assert Map({1: First(1)}).concat(Map({1: First(2)})) == Map({1: First(1)})
    assert Map({1: Last(1)}).concat(Map({1: Last(2)})) == Map({1: Last(2)})
    assert Map({"a": Sum(1), "b": Sum(2), "c": Sum(3)}).concat(Map({"a": Sum(4), "b": Sum(5)})) == Map({"a": Sum(5), "b": Sum(7), "c": Sum(3)})

# Generated at 2022-06-14 03:44:56.816263
# Unit test for method concat of class Min
def test_Min_concat():
    one = Min(1)
    two = Min(2)
    three = Min(1)

    assert one.concat(two) == two, 'Should return larger value'
    assert one.concat(three) == one, 'Should return smaller value'


# Generated at 2022-06-14 03:44:59.747054
# Unit test for method concat of class Min
def test_Min_concat():
    Min(1).concat(Min(2)) == Min(1)


# Generated at 2022-06-14 03:45:03.237322
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(1).concat(Min(5)).value == 1
    assert Min(5).concat(Min(1)).value == 1



# Generated at 2022-06-14 03:45:10.012723
# Unit test for method concat of class Min
def test_Min_concat():
    print("Unit test for method concat of class Min")
    min_a = Min(1)
    min_b = Min(3)
    print("min_a=", min_a)
    print("min_b=", min_b)
    print("min_a.concat(min_b)=", min_a.concat(min_b))
    return
test_Min_concat()


# Generated at 2022-06-14 03:45:12.863026
# Unit test for method concat of class Min
def test_Min_concat():
    assert(Min(2).concat(Min(3)).value == 2)



# Generated at 2022-06-14 03:45:14.636138
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(1).concat(Min(2)) == Min(1)
    assert Min(1).concat(Min(0)) == Min(0)

# Generated at 2022-06-14 03:45:28.809289
# Unit test for method concat of class Map
def test_Map_concat():
    m1 = Map()
    m2 = Map()

    assert m1.concat(m2).value == {}

    m1 = Map({'a': All(), 'b': All()})

    assert m1.concat(m1).value == {'a': All(), 'b': All()}

    m2 = Map({'a': First(1), 'c': First(2)})

    assert m1.concat(m2).value == {'a': First(1), 'b': All(), 'c': First(2)}

    m1 = Map({'a': All(True), 'b': All(True)})

    assert m1.concat(m1).value == {'a': All(True), 'b': All(True)}


# Generated at 2022-06-14 03:45:35.618994
# Unit test for method concat of class Map
def test_Map_concat():
    m1 = Map({1 : Sum(1), 2 : All(True)})
    m2 = Map({1 : Sum(5), 2 : All(False)})
    x = m1.concat(m2)
    assert x.value[1].value == 6 and x.value[2].value == False


# Generated at 2022-06-14 03:45:39.685237
# Unit test for method __str__ of class All
def test_All___str__():
    all_ = All(True)
    assert str(all_) == 'All[value=True]'



# Generated at 2022-06-14 03:45:43.826177
# Unit test for method __str__ of class Max
def test_Max___str__():  # pragma: no cover
    """Test method __str__ of class Max with values of different types"""

    assert str(Max(1)) == 'Max[value=1]'
    assert str(Max('a')) == 'Max[value=a]'
    assert str(Max(Semigroup('b'))) == 'Max[value=b]'



# Generated at 2022-06-14 03:45:45.259581
# Unit test for method __str__ of class Last
def test_Last___str__():
    assert str(Last('Python')) == 'Last[value=Python]'


# Generated at 2022-06-14 03:45:47.836683
# Unit test for method __str__ of class Map
def test_Map___str__():
    assert str(Map({1: Sum(1)})) == 'Map[value={1: Sum[value=1]}]'

# Generated at 2022-06-14 03:45:49.090244
# Unit test for constructor of class One
def test_One():
    assert str(One(1)) == "One[value=1]"


# Generated at 2022-06-14 03:45:51.692115
# Unit test for constructor of class One
def test_One():
    """
    Unit test with One class instance
    :raises: AssertionError if constructor is not working by rules
    """
    one = One(True)
    assert isinstance(one, One)
    assert isinstance(one, Semigroup)
    assert isinstance(one, object)


# Generated at 2022-06-14 03:45:53.583051
# Unit test for method __str__ of class Map
def test_Map___str__():
    assert str(Map({'a': Sum(1), 'c': Sum(2)})) == 'Map[value={"a": Sum[value=1], "c": Sum[value=2]}]'


# Generated at 2022-06-14 03:45:56.545145
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(2)) == 'Max[value=2]'
    with pytest.raises(TypeError):
        Max(2.0)


# Generated at 2022-06-14 03:45:57.385909
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(5)) == 'Max[value=5]'


# Generated at 2022-06-14 03:45:58.361918
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    assert str(Sum(1)) == 'Sum[value=1]'


# Generated at 2022-06-14 03:46:05.278172
# Unit test for constructor of class All
def test_All():
  assert All(True) == All(True)
  assert All(False) == All(False)

  assert All(True) != All(False)
  assert All(False) != All(True)


# Generated at 2022-06-14 03:46:08.346226
# Unit test for constructor of class Last
def test_Last():
    assert Last(1) == Last(1)
    assert Last(2) != Last(1)
    assert First(1) != Last(1)
    assert First(1) != 1


# Generated at 2022-06-14 03:46:19.076072
# Unit test for method concat of class Last
def test_Last_concat():
    assert Last(1).concat(Last(2)) == Last(2)
    assert Last(1).concat(Last(1)) == Last(1)
    assert Last(1).concat(Last(0)) == Last(0)
    assert Last(0).concat(Last(2)) == Last(2)
    assert Last(0).concat(Last(1)) == Last(1)
    assert Last(0).concat(Last(0)) == Last(0)
    assert Last(1).concat(Last(True)) == Last(True)
    assert Last(1).concat(Last(False)) == Last(False)
    assert Last(True).concat(Last(2)) == Last(2)
    assert Last(True).concat(Last(1)) == Last(1)

# Generated at 2022-06-14 03:46:21.964125
# Unit test for method concat of class Min
def test_Min_concat():
    a = Min(3)
    b = Min(6)
    assert a.concat(b).value == 3


# Generated at 2022-06-14 03:46:22.961480
# Unit test for constructor of class Sum
def test_Sum():
    value = Sum('hello')
    assert value.value == 'hello'



# Generated at 2022-06-14 03:46:25.701978
# Unit test for constructor of class Min
def test_Min():
    assert Min(1).value == 1
    assert Min(2).value == 2
    assert Min(100).value == 100
    assert Min(200).value == 200
    assert Min(1000).value == 1000



# Generated at 2022-06-14 03:46:27.127203
# Unit test for method concat of class First
def test_First_concat():
    first = First(9)
    assert 9 == first.concat(First(8)).value
    assert 1 == first.concat(First(1)).value



# Generated at 2022-06-14 03:46:29.490217
# Unit test for method concat of class Map
def test_Map_concat():
    assert Map({3: Sum(3)}).concat(Map({3: Sum(4)})).fold(lambda x: x[3].value) == 7

# Generated at 2022-06-14 03:46:30.241372
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    assert str(Sum(10)) == "Sum[value=10]"


# Generated at 2022-06-14 03:46:33.499837
# Unit test for constructor of class Map
def test_Map():
    result = Map({'string_value': First('World'), 'int_value': Sum(1)})
    expected = Map({'string_value': First('World'), 'int_value': Sum(1)})
    assert result == expected



# Generated at 2022-06-14 03:46:50.391228
# Unit test for constructor of class Map
def test_Map():
    assert Map({'a': 1, 'b': 2}) == Map({'a': 1, 'b': 2})
    assert Map({'a': 1, 'b': 2}) != Map({'a': 1, 'b': 3})
    assert Map({'a': 1, 'b': 2}) != Map({'a': 3, 'b': 2})
    assert Map({'a': 1, 'b': 2}) != Map({'a': 1, 'b': 2, 'c': 3})
    assert Map({'a': 1, 'b': 2}) != Map({'b': 2, 'a': 1})
    assert Map({'a': 1, 'b': 2}) != Map({'a': 1})
    assert Map({'a': 1, 'b': 2}) != Map({'a': 4, 'b': 9})
    assert Map

# Generated at 2022-06-14 03:46:54.960797
# Unit test for method concat of class One
def test_One_concat():
    Onex = One(1)
    Oney = One(None)
    Onez = One(0)

    assert Onex.concat(Oney) == One(1)
    assert Onex.concat(Onez) == One(1)
    assert Oney.concat(Onez) == One(0)



# Generated at 2022-06-14 03:46:58.990548
# Unit test for method concat of class Max
def test_Max_concat():
    """
    >>> test_Max_concat()
    True
    """
    assert Max(1).concat(Max(2)) == Max(2)
    assert Max(1).concat(Max(1)) == Max(1)
    return True


# Generated at 2022-06-14 03:47:00.904192
# Unit test for method __str__ of class One
def test_One___str__():
    one = One(1)
    assert str(one) == 'One[value=1]'


# Generated at 2022-06-14 03:47:07.890820
# Unit test for method concat of class First
def test_First_concat():  # pragma: no cover
    semigroup1 = First(1)
    semigroup2 = First(2)
    semigroup3 = First("a")
    semigroup4 = First("b")
    result = semigroup1.concat(semigroup2)
    assert result.value == 1
    result = semigroup1.concat(semigroup3)
    assert result.value == 1
    result = semigroup3.concat(semigroup4)
    assert result.value == "a"



# Generated at 2022-06-14 03:47:10.382332
# Unit test for method concat of class One
def test_One_concat():  # pragma: no cover
    assert One(False).concat(One(True)).value
    assert not One(False).concat(One(False)).value
    assert One(True).concat(One(False)).value
    assert One(True).concat(One(True)).value



# Generated at 2022-06-14 03:47:12.576353
# Unit test for method __str__ of class Min
def test_Min___str__():

    assert(Min(1) == Min(1))

    str = 'Min[value=1]'

    assert(str == str(Min(1)))



# Generated at 2022-06-14 03:47:15.421146
# Unit test for constructor of class Last
def test_Last():
    assert First("a").concat(First("b")) == First("a")
    assert First(1).concat(First(2)) == First(1)



# Generated at 2022-06-14 03:47:18.009903
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(1).concat(Max(2)) == Max(2)
    assert Max(1).concat(Max(0)) == Max(1)
    assert Max(1).concat(Max(1)) == Max(1)


# Generated at 2022-06-14 03:47:20.925399
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    SumValue = Sum(1)
    assert str(SumValue) == "Sum[value=1]"



# Generated at 2022-06-14 03:47:29.118171
# Unit test for method concat of class One
def test_One_concat():
    assert One(True).concat(One(False)) == One(True)
    assert One(True).concat(One(True)) == One(True)
    assert One(False).concat(One(True)) == One(True)
    assert One(False).concat(One(False)) == One(False)



# Generated at 2022-06-14 03:47:30.800115
# Unit test for constructor of class First
def test_First():
    assert First(1) == First(1)


# Generated at 2022-06-14 03:47:33.832848
# Unit test for method concat of class Last
def test_Last_concat():
    last1 = Last(1)
    last2 = Last(2)
    result = last1.concat(last2)

    assert result == last2


# Generated at 2022-06-14 03:47:37.238166
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(1).concat(Min(3)) == Min(1)
    assert Min(3).concat(Min(1)) == Min(1)



# Generated at 2022-06-14 03:47:39.726533
# Unit test for method concat of class Map
def test_Map_concat():
    print(Map({'data': Sum(5)}).concat(Map({'data': Sum(6)})))



# Generated at 2022-06-14 03:47:41.538277
# Unit test for method __str__ of class Max
def test_Max___str__():  # pragma: no cover
    assert str(Max(3)) == 'Max[value=3]'



# Generated at 2022-06-14 03:47:42.851573
# Unit test for constructor of class Semigroup
def test_Semigroup():
    assert Semigroup(1).value == 1


# Generated at 2022-06-14 03:47:44.937069
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert "Max[value={}]".format(1) == str(Max(1))


# Generated at 2022-06-14 03:47:49.895554
# Unit test for method concat of class All
def test_All_concat():
    assert All(True).concat(All(False)) == All(False)
    assert All(False).concat(All(False)) == All(False)
    assert All(False).concat(All(True)) == All(False)
    assert All(True).concat(All(True)) == All(True)



# Generated at 2022-06-14 03:47:54.699842
# Unit test for method concat of class Max
def test_Max_concat():  # pragma: no cover
    assert Max(2).concat(Max(3)) == Max(3)
    assert Max(-2).concat(Max(3)) == Max(3)
    assert Max(2).concat(Max(-3)) == Max(2)
    assert Max(2).concat(Max(2)) == Max(2)


# Generated at 2022-06-14 03:48:06.343822
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__(): #pragma: no cover
    assert Sum(1) == Sum(1)
    assert All(True) == All(True)
    assert One(True) == One(True)
    assert First(1) == First(1)
    assert Last(1) == Last(1)
    assert Map({1: First(2)}) == Map({1: First(2)})
    assert Max(1) == Max(1)
    assert Min(1) == Min(1)


# Generated at 2022-06-14 03:48:14.839353
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    assert Sum(1) == Sum(1)
    assert Sum(1) != Sum(2)
    assert All(True) == All(True)
    assert All(True) != All(False)
    assert One(True) == One(True)
    assert One(False) != One(True)
    assert First(1) == First(1)
    assert First(1) != First(2)
    assert Last(1) == Last(1)
    assert Last(1) != Last(2)
    assert Max(1) == Max(1)
    assert Max(1) != Max(2)
    assert Min(1) == Min(1)
    assert Min(1) != Min(2)

# Generated at 2022-06-14 03:48:18.419156
# Unit test for method concat of class Sum
def test_Sum_concat():
    s1 = Sum(5)
    s2 = Sum(10)
    assert s1.concat(s2) == Sum(15)
    assert s2.concat(s1) == Sum(15)


# Generated at 2022-06-14 03:48:19.772654
# Unit test for constructor of class Max
def test_Max():
    assert Max(3).value == 3


# Generated at 2022-06-14 03:48:22.207367
# Unit test for constructor of class Last
def test_Last():
    assert Last(5) == Last(5)



# Generated at 2022-06-14 03:48:23.712587
# Unit test for method __str__ of class Last
def test_Last___str__():
    assert str(Last(0)) == 'Last[value=0]'



# Generated at 2022-06-14 03:48:27.041548
# Unit test for method concat of class Sum
def test_Sum_concat():
    assert Sum(1).concat(Sum(2)).value == 3
    assert Sum(1).concat(Sum(-2)).value == -1
    assert Sum(-1).concat(Sum(-2)).value == -3


# Generated at 2022-06-14 03:48:31.084086
# Unit test for method concat of class One
def test_One_concat():
    assert One(1).concat(One(2)).value == True
    assert One(0).concat(One(2)).value == True
    assert One(1).concat(One(0)).value == True
    assert One(False).concat(One(False)).value == False


# Generated at 2022-06-14 03:48:37.574225
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    assert Semigroup(0) == Sum(0)
    assert All(True) == All(True)
    assert One(False) == One(False)
    assert First(1) == First(1)
    assert Last(100) == Last(100)
    assert Map({'one': All(True), 'two': All(False)}) == Map({'one': All(False), 'two': All(True)})
    assert Max(100) == Max(100)
    assert Min(2) == Min(2)


# Generated at 2022-06-14 03:48:44.295811
# Unit test for method concat of class Map
def test_Map_concat():
    assert Map({"key": Sum(1)}).concat(
        Map({"key": Sum(1)})
    ) == Map({"key": Sum(2)})
    assert Map({}).concat(Map({})) == Map({})
    assert (Map({"key": Sum(1)}).concat(Map({"key": Sum(2)}))
            == Map({"key": Sum(3)}))

# Generated at 2022-06-14 03:49:07.575557
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5

    def plus_one(value):
        return value + 1

    def plus_two(value):
        return value + 2

    assert Semigroup(one).fold(plus_one) == plus_one(one)
    assert Semigroup(one).fold(plus_two) == plus_two(one)

    assert Semigroup(two).fold(plus_one) == plus_one(two)
    assert Semigroup(two).fold(plus_two) == plus_two(two)

    assert Semigroup(three).fold(plus_one) == plus_one(three)
    assert Semigroup(three).fold(plus_two) == plus_two(three)


# Generated at 2022-06-14 03:49:11.888773
# Unit test for constructor of class Min
def test_Min():
    assert Min(2) == Min(2)
    assert Min(3) == Min(3)
    assert Min(3) != Min(2)


# Generated at 2022-06-14 03:49:13.667632
# Unit test for constructor of class Last
def test_Last():
    assert Last("a") == Last("a")



# Generated at 2022-06-14 03:49:18.143553
# Unit test for method concat of class All
def test_All_concat():
    assert All(False).concat(All(True)) == All(False)
    assert All(False).concat(All(None)) == All(False)
    assert All(True).concat(All(True)) == All(True)
    assert All(True).concat(All(None)) == All(None)



# Generated at 2022-06-14 03:49:20.855473
# Unit test for constructor of class Max
def test_Max():
    m1 = Max(5)
    assert m1.value == 5
    assert m1.concat(Max(2)).value == 5

    m2 = Max(-17)
    assert m2.value == -17
    assert m2.concat(Max(15)).value == 15


# Generated at 2022-06-14 03:49:25.374557
# Unit test for method __str__ of class All
def test_All___str__():
    assert str(All(1)) == 'All[value=1]'
    assert str(All(True)) == 'All[value=True]'
    assert str(All(None)) == 'All[value=None]'


# Generated at 2022-06-14 03:49:36.424048
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    assert Sum(1) == Sum(1)
    assert Sum(1) != Sum(2)
    assert All(True) == All(True)
    assert All(False) != All(True)
    assert One(True) == One(True)
    assert One(False) != One(True)
    assert First(1) == First(1)
    assert First(1) != First(2)
    assert Last(1) == Last(1)
    assert Last(1) != Last(2)
    assert Map({1: All(True)}) == Map({1: All(True)})
    assert Map({1: All(True)}) != Map({1: All(False)})
    assert Map({1: All(True)}) != Map({})
    assert Max(1) == Max(1)

# Generated at 2022-06-14 03:49:38.933653
# Unit test for method concat of class Last
def test_Last_concat():  # pragma: no cover
    assert Last(0).concat(Last(1)).value == 1


# Generated at 2022-06-14 03:49:40.900841
# Unit test for method __str__ of class All
def test_All___str__():
    test_result = str(All(True))
    assert test_result == 'All[value=True]', 'Expected str(All(True)) == All[value=True], but got %s' % test_result


# Generated at 2022-06-14 03:49:43.470096
# Unit test for method concat of class Max
def test_Max_concat():
    f1 = Max(2)
    f2 = Max(4)
    f3 = f1.concat(f2)
    if f3.value != 4:
        raise Exception("Wrong value, it should be 4")


# Generated at 2022-06-14 03:50:11.195466
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    assert str(Sum(1)) == 'Sum[value=1]'
    assert str(Sum(0)) == 'Sum[value=0]'
    assert str(Sum(11)) == 'Sum[value=11]'


# Generated at 2022-06-14 03:50:15.931018
# Unit test for method __str__ of class First
def test_First___str__():
    value = 'some random value'
    obj = First(value)

    result = obj.__str__()  # pylint: disable=no-member

    assert result == 'Fist[value={}]'.format(value)


# Generated at 2022-06-14 03:50:17.300371
# Unit test for constructor of class Min
def test_Min():
    assert Min(1).value == 1


# Generated at 2022-06-14 03:50:18.996566
# Unit test for constructor of class All
def test_All():
    a = All(True)
    assert a.value is True



# Generated at 2022-06-14 03:50:24.858862
# Unit test for method concat of class Last
def test_Last_concat():  # pragma: no cover
    """
    Unit test for method concat of class Last
    """
    assert Last(1).concat(Last(2)) == Last(2)
    assert Last('a').concat(Last('b')) == Last('b')
    assert Last(None).concat(Last(2)) == Last(2)



# Generated at 2022-06-14 03:50:26.218055
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    assert str(Sum(5)) == 'Sum[value=5]'


# Generated at 2022-06-14 03:50:27.459329
# Unit test for constructor of class First
def test_First():
    assert First(1).value == 1



# Generated at 2022-06-14 03:50:30.119201
# Unit test for method __str__ of class Max
def test_Max___str__():
    res = Max(4).__str__()
    expected = 'Max[value=4]'
    assert res == expected



# Generated at 2022-06-14 03:50:33.238093
# Unit test for constructor of class Min
def test_Min():
    assert Min(2) == Min(2)
    assert Min(2).value == 2
    assert Min(3).value == 3


# Generated at 2022-06-14 03:50:34.927436
# Unit test for constructor of class Last
def test_Last():
    x = Last(1)
    assert x.value == 1


# Generated at 2022-06-14 03:51:31.656026
# Unit test for method __str__ of class Map
def test_Map___str__():
    map_ = Map({1: First(1), 2: Sum(100)})
    assert map_ == Map({1: First(1), 2: Sum(100)})
    assert str(map_) == 'Map[value={1: Fist[value=1], 2: Sum[value=100]}]'


# Generated at 2022-06-14 03:51:34.695133
# Unit test for constructor of class Last
def test_Last():
    Last(1)
    Last(True)
    Last(None)



# Generated at 2022-06-14 03:51:43.213092
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    assert (Sum(1) == Sum(1)) is True
    assert (Sum(1) == Sum(2)) is False

    assert (All(True) == All(True)) is True
    assert (All(True) == All(False)) is False
    assert (All(True) == All(1)) is False

    assert (One(True) == One(True)) is True
    assert (One(True) == One(False)) is False
    assert (One(True) == One(1)) is False

    assert (First(1) == First(1)) is True
    assert (First(1) == First(2)) is False

    assert (Last(1) == Last(1)) is True
    assert (Last(1) == Last(2)) is False

    assert (Max(1) == Max(1)) is True

# Generated at 2022-06-14 03:51:45.887049
# Unit test for constructor of class Min
def test_Min():
    min_1 = Min(10)
    min_2 = Min(5)
    eq_(min_1.concat(min_2).value, 5)


# Generated at 2022-06-14 03:51:48.232862
# Unit test for constructor of class First
def test_First():  # pragma: no cover
    # Check default type of attribute value
    assert First(1).value == 1


# Generated at 2022-06-14 03:51:53.320824
# Unit test for method concat of class One
def test_One_concat():
    assert One(True).concat(One(True)) == One(True)
    assert One(False).concat(One(True)) == One(True)
    assert One(True).concat(One(False)) == One(True)
    assert One(False).concat(One(False)) == One(False)




# Generated at 2022-06-14 03:52:01.107070
# Unit test for method concat of class First
def test_First_concat():
    assert First(None) == First(None)
    assert First(None).concat(First(None)) == First(None)
    assert First(None).concat(First(True)) == First(True)
    assert First(False).concat(First(None)) == First(False)
    assert First(False).concat(First(True)) == First(False)
    assert First(False).concat(First(False)) == First(False)
    assert First(True).concat(First(True)) == First(True)
    assert First(1).concat(First(1)) == First(1)
    assert First(None).concat(First(1)) == First(1)
    assert First(1).concat(First(2)) == First(1)

# Generated at 2022-06-14 03:52:03.719817
# Unit test for method __str__ of class First
def test_First___str__():
    actual = str(First('foo'))
    expected = 'Fist[value=foo]'
    assert actual == expected

# Generated at 2022-06-14 03:52:05.075914
# Unit test for method __str__ of class All
def test_All___str__():
    assert str(All(True)) == "All[value=True]"


# Generated at 2022-06-14 03:52:11.189639
# Unit test for method concat of class Map
def test_Map_concat():
    map1 = Map({1: Sum(1), 2: Sum(2)})
    map2 = Map({2: Sum(2), 3: Sum(3)})
    result = map1.concat(map2)
    assert result == Map({1: Sum(1), 2: Sum(4), 3: Sum(3)})

# Generated at 2022-06-14 03:54:18.539776
# Unit test for constructor of class First
def test_First():
    assert First(1) == First(1)
    assert First(1).concat(First(2)) == First(1)
    assert First(1).concat(First(None)) == First(1)


# Generated at 2022-06-14 03:54:22.486806
# Unit test for constructor of class One
def test_One():
    assert One(True).value is True
    assert One(False).value is False
    assert One(None).value is None
    assert One([]).value == []
    assert One({}).value == {}

# Test concat of two One instances

# Generated at 2022-06-14 03:54:25.186737
# Unit test for constructor of class Semigroup
def test_Semigroup():
    a = Semigroup(1)
    b = Semigroup(1)
    c = Semigroup(2)

    assert a == b
    assert a != c
