

# Generated at 2022-06-14 03:44:33.781945
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(0).concat(Min(1)) == Min(0)


# Generated at 2022-06-14 03:44:42.971863
# Unit test for method concat of class Min
def test_Min_concat():
    """
    Method test_Min_concat() is a unit test for method concat of class Min
    """
    assert Min(1).concat(Min(2)) == Min(1)
    assert Min(2).concat(Min(3)) == Min(2)
    assert Min(3).concat(Min(1)) == Min(1)
    assert Min(1).concat(Min(-2)) == Min(-2)
    assert Min(-2).concat(Min(3)) == Min(-2)
    assert Min(3).concat(Min(-1)) == Min(-1)
    assert Min(-1).concat(Min(-2)) == Min(-2)
    assert Min(-2).concat(Min(-3)) == Min(-3)
    assert Min(-3).concat(Min(-1)) == Min(-3)
   

# Generated at 2022-06-14 03:44:46.965001
# Unit test for method concat of class Map
def test_Map_concat():
    m1 = Map({'a': Sum(1)})
    m2 = Map({'a': Sum(2)})
    m3 = m1.concat(m2)
    assert m3 == Map({'a': Sum(3)})

# Generated at 2022-06-14 03:44:49.307601
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(1).concat(Min(3)) == Min(1)


# Generated at 2022-06-14 03:44:51.964858
# Unit test for method concat of class Min
def test_Min_concat():
    a = Min(2)
    b = Min(3)
    assert a.concat(b) == Min(2)

# test_Min_concat()


# Generated at 2022-06-14 03:44:56.717614
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(1).concat(Min(2)) == Min(1)
    assert Min(1).concat(Min(-2)) == Min(-2)
    assert Min(-1).concat(Min(-2)) == Min(-2)
    assert Min(-2).concat(Min(-2)) == Min(-2)



# Generated at 2022-06-14 03:45:07.466717
# Unit test for method concat of class Map
def test_Map_concat():
    m1 = Map({
        'a': Sum(10),
        'b': Min(1),
        'c': Last(1),
    })
    m2 = Map({
        'a': Sum(2),
        'b': Min(1),
        'c': Last(2),
    })
    res = m1.concat(m2)
    assert res.value == {
        'a': Sum(12),
        'b': Min(1),
        'c': Last(2),
    }

# Generated at 2022-06-14 03:45:14.361268
# Unit test for method concat of class Map
def test_Map_concat():
    assert Map({
        'a': First(2),
        'b': Sum(3),
    }).concat(Map({
        'a': Last(4),
        'b': First(7),
    })) == Map({'a': Last(4), 'b': Sum(10)})

test_Map_concat()

# Generated at 2022-06-14 03:45:28.695084
# Unit test for method concat of class Map
def test_Map_concat():
    m1 = Map({'a': All(True)})
    m2 = Map({'a': All(False), 'b': All(True)})
    m3 = m1.concat(m2)
    assert m3.value == {'a': All(False), 'b': All(True)}
    m1 = Map({'a': All(True)})
    m2 = Map({'a': All(True), 'b': All(True)})
    m3 = m1.concat(m2)
    assert m3.value == {'a': All(True), 'b': All(True)}
    m1 = Map({'a': All(True), 'b': All(True)})
    m2 = Map({'a': All(False), 'b': All(True)})

# Generated at 2022-06-14 03:45:32.701532
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(1).concat(Min(2)) == Min(1)
    assert Min(2).concat(Min(1)) == Min(1)


# Generated at 2022-06-14 03:45:35.684311
# Unit test for method concat of class Sum
def test_Sum_concat():
    assert Sum(1).concat(Sum(2)) == Sum(3)


# Generated at 2022-06-14 03:45:37.490804
# Unit test for method concat of class First
def test_First_concat():
    value = 1
    semigroup = First(value)
    assert semigroup.concat(First(2)) == First(value)



# Generated at 2022-06-14 03:45:40.404266
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    """
    Test for method fold of class Semigroup
    """
    assert Semigroup(1).fold(lambda x: x*2) == 2



# Generated at 2022-06-14 03:45:41.791764
# Unit test for method concat of class Last
def test_Last_concat():  # pragma: no cover
    assert Last(1).concat(Last(2)) == Last(2)



# Generated at 2022-06-14 03:45:43.476331
# Unit test for method concat of class Sum
def test_Sum_concat():  # pragma: no cover
    assert Sum(1).concat(Sum(2)) == Sum(3)



# Generated at 2022-06-14 03:45:45.297786
# Unit test for constructor of class Max
def test_Max():
    assert Max(2).value == 2
    assert Max(3).value == 3


# Generated at 2022-06-14 03:45:48.879046
# Unit test for constructor of class All
def test_All():
    # Tests for constructor of class All
    all_true = All(True)
    assert all_true.value == True

    all_false = All(False)
    assert all_false.value == False


# Generated at 2022-06-14 03:45:50.179386
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    assert Semigroup(1) == Semigroup(1)



# Generated at 2022-06-14 03:45:55.176806
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(1).concat(Max(3)) == Max(3)
    assert Max(3).concat(Max(3)) == Max(3)
    assert Max(3).concat(Max(2)) == Max(3)

# Generated at 2022-06-14 03:45:58.305945
# Unit test for method concat of class Max
def test_Max_concat():  # pragma: no cover
    assert Max(1).concat(Max(2)) == Max(2)
    assert Max(2).concat(Max(1)) == Max(2)



# Generated at 2022-06-14 03:46:04.886762
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(1).concat(Min(2)) == Min(1)
    assert Min(2).concat(Min(1)) == Min(1)
    assert Min(3).concat(Min(4)) == Min(3)
    assert Min(4).concat(Min(3)) == Min(3)


# Generated at 2022-06-14 03:46:09.092132
# Unit test for constructor of class Max
def test_Max():
    a = Max(1)
    b = Max(2)
    c = Max(3)
    assert a.concat(b) == Max(2)
    assert b.concat(c) == Max(3)
    assert c.concat(a) == Max(3)



# Generated at 2022-06-14 03:46:12.077243
# Unit test for method __str__ of class One
def test_One___str__():
    assert str(One(True)) == 'One[value=True]'
    assert str(One(False)) == 'One[value=False]'



# Generated at 2022-06-14 03:46:13.820258
# Unit test for constructor of class Sum
def test_Sum():
    assert Sum(2) == Sum(2)
    assert Sum(2).concat(Sum(3)) == Sum(5)


# Generated at 2022-06-14 03:46:15.128503
# Unit test for method __str__ of class First
def test_First___str__():
    assert str(First(1)) == 'Fist[value=1]'



# Generated at 2022-06-14 03:46:16.737367
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    assert Semigroup(42).fold(lambda x: x + 1) == 43


# Generated at 2022-06-14 03:46:24.166006
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(1).concat(Max(2)) == Max(2)
    assert Max(-100).concat(Max(1)) == Max(1)
    assert Max(19).concat(Max(-19)) == Max(19)
    assert Max(1.0).concat(Max(1.1)) == Max(1.1)
    assert Max(-1.1).concat(Max(-1.0)) == Max(-1.0)
    assert Max(1.0).concat(Max(1)) == Max(1.0)
    assert Max(-1.0).concat(Max(-1)) == Max(-1.0)
    assert Max(0.8).concat(Max(0.9)) == Max(0.9)
    assert Max(100).concat(Max(100)) == Max(100)

# Generated at 2022-06-14 03:46:35.263532
# Unit test for constructor of class All
def test_All():
    assert str(All("cat")) == "All[value=True]"
    assert str(All("")) == "All[value=False]"
    assert str(All("")) == "All[value=False]"
    assert All("cat").concat(All("")) == All(False)
    assert All("cat").concat(All(True)) == All(True)
    assert All("cat").concat(All("cat")) == All(True)
    assert All(False).concat(All("cat")) == All(False)
    assert All(False).concat(All(False)) == All(False)
    assert All(True).concat(All("cat")) == All(True)
    assert All(True).concat(All(True)) == All(True)
    assert All(1).concat(All(True)) == All(True)

# Generated at 2022-06-14 03:46:38.087307
# Unit test for constructor of class First
def test_First():
    # Given
    value = 'a'
    first = First(value)

    # Then
    assert value == first.value



# Generated at 2022-06-14 03:46:41.657814
# Unit test for method concat of class Max
def test_Max_concat():
    a = Max(1)
    b = Max(5)
    c = a.concat(b)
    assert a.value == 1
    assert b.value == 5
    assert c.value == 5
    assert isinstance(c, Max)


# Generated at 2022-06-14 03:46:45.817126
# Unit test for method __str__ of class First
def test_First___str__():
    first = First('first')
    assert first.__str__() == 'Fist[value=first]'



# Generated at 2022-06-14 03:46:47.075635
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(10)) == 'Max[value=10]'


# Generated at 2022-06-14 03:46:51.985851
# Unit test for method concat of class Max
def test_Max_concat():
    """
    :returns: bool
    :rtype: bool
    """
    a = Max(10)
    b = Max(200)

    return a.concat(b) == Max(200)



# Generated at 2022-06-14 03:46:57.454175
# Unit test for method concat of class All
def test_All_concat():
    assert All(False).concat(All(False)) == All(False)
    assert All(False).concat(All(True)) == All(False)
    assert All(True).concat(All(False)) == All(False)
    assert All(True).concat(All(True)) == All(True)



# Generated at 2022-06-14 03:47:00.834057
# Unit test for method concat of class One
def test_One_concat():
    assert One(True).concat(One(False)).value == True
    assert One(True).concat(One(True)).value == True
    assert One(False).concat(One(False)).value == False
    assert One(False).concat(One(True)).value == True


# Generated at 2022-06-14 03:47:03.102950
# Unit test for method concat of class Last
def test_Last_concat(): # pragma: no cover
    start = Last(1)
    end = Last(3)

    start.concat(end) == Last(3)


# Generated at 2022-06-14 03:47:05.285211
# Unit test for constructor of class Last
def test_Last():
    last = Last(4)
    assert last.value == 4



# Generated at 2022-06-14 03:47:07.069777
# Unit test for constructor of class Min
def test_Min():
    assert Min(3) == Min(3)
    assert Min(3) != Min(5)


# Generated at 2022-06-14 03:47:09.756462
# Unit test for method __str__ of class First
def test_First___str__():
    assert str(First(1)) == 'Fist[value=1]'
    assert str(First([])) == 'Fist[value=[]]'


# Generated at 2022-06-14 03:47:11.421537
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    s = Sum(1)
    assert 'Sum[value=1]' == str(s)


# Generated at 2022-06-14 03:47:22.880178
# Unit test for method concat of class All
def test_All_concat():
    assert All(True).concat(All(True)) == All(True)
    assert All(True).concat(All(False)) == All(False)
    assert All(False).concat(All(True)) == All(False)
    assert All(False).concat(All(False)) == All(False)

    assert All(1).concat(All(2)) == All(True)
    assert All(1).concat(All(0)) == All(False)
    assert All(0).concat(All(1)) == All(False)
    assert All(0).concat(All(0)) == All(False)

    assert All(1).concat(All(True)) == All(True)
    assert All(1).concat(All(False)) == All(False)

# Generated at 2022-06-14 03:47:28.738481
# Unit test for constructor of class One
def test_One():  # pragma: no cover
    """
    Test class One
    """
    assert One(True) == One(True)
    assert One(None) == One(None)
    assert One(False) == One(False)
    assert not One(True) == One(False)
    assert not One(None) == One(False)



# Generated at 2022-06-14 03:47:30.838207
# Unit test for method __str__ of class Last
def test_Last___str__():
    cls = Last(3)
    assert cls.__str__() == 'Last[value=3]'



# Generated at 2022-06-14 03:47:33.423708
# Unit test for method __str__ of class One
def test_One___str__():
    assert str(One(True)) == "One[value=True]"
    assert str(One(False)) == "One[value=False]"


# Generated at 2022-06-14 03:47:36.155016
# Unit test for constructor of class One
def test_One():
    assert One(True).value == True
    assert One(False).value == False



# Generated at 2022-06-14 03:47:37.572831
# Unit test for method __str__ of class All
def test_All___str__():
    assert 'All[value=True]' == str(All(True))



# Generated at 2022-06-14 03:47:40.843963
# Unit test for constructor of class One
def test_One():
    assert One(1) == One(1)
    assert One(1).concat(One(2)).value == 1
    assert str(One(1)) == "One[value=1]"


# Generated at 2022-06-14 03:47:45.334670
# Unit test for method concat of class One
def test_One_concat():
    assert One(True).concat(One(True)).value == True
    assert One(False).concat(One(False)).value == False
    assert One(True).concat(One(False)).value == True
    assert One(False).concat(One(True)).value == True


# Generated at 2022-06-14 03:47:49.891227
# Unit test for method concat of class Max
def test_Max_concat():
    """
    2 Max instances containing 2 and 3 are concatted. result is Max(3)
    """
    semigroup1 = Max(2)
    semigroup2 = Max(3)
    result = semigroup1.concat(semigroup2)
    assert result == Max(3)


# Generated at 2022-06-14 03:47:51.728436
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(1).concat(Max(2)) == Max(2)



# Generated at 2022-06-14 03:47:56.511523
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    assert str(Sum(1)) == 'Sum[value=1]'



# Generated at 2022-06-14 03:47:58.416494
# Unit test for method __str__ of class Min
def test_Min___str__():  # pragma: no cover
    assert str(Min(10)) == 'Min[value=10]'



# Generated at 2022-06-14 03:48:01.949444
# Unit test for constructor of class Semigroup
def test_Semigroup():
    assert Semigroup(0)
    assert Semigroup(1)
    assert Semigroup("0")
    assert Semigroup("1")
    assert Semigroup(True)
    assert Semigroup(False)
    assert Semigroup(None)
    assert Semigroup([])
    assert Semigroup({})
    assert Semigroup(())
    assert Semigroup(0.0)
    assert Semigroup(1.0)


# Generated at 2022-06-14 03:48:10.405217
# Unit test for method concat of class All
def test_All_concat():
    assert All(True).concat(All(True)) == All(True), "Test of method concat of class All has failed"
    assert All(True).concat(All(False)) == All(False), "Test of method concat of class All has failed"
    assert All(False).concat(All(True)) == All(False), "Test of method concat of class All has failed"
    assert All(False).concat(All(False)) == All(False), "Test of method concat of class All has failed"


# Generated at 2022-06-14 03:48:14.268429
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(1).concat(Max(2)) == Max(2)
    assert Max(1).concat(Max(0)) == Max(1)
    assert Max(1).concat(Max(1)) == Max(1)

Max(1).concat(Max(2)) == Max(2)


# Generated at 2022-06-14 03:48:15.267418
# Unit test for constructor of class Min
def test_Min():
    assert Min(3).value == 3


# Generated at 2022-06-14 03:48:18.258110
# Unit test for method __str__ of class Map
def test_Map___str__():
    actual = str(Map({"A": Sum(1), "B": All(True)}))
    expected = "Map[value={'A': Sum[value=1], 'B': All[value=True]}]"
    assert expected == actual



# Generated at 2022-06-14 03:48:22.615202
# Unit test for constructor of class Semigroup
def test_Semigroup():  # pragma: no cover
    x = Sum(2)
    assert type(x) == Sum
    y = Sum(4)
    assert type(y) == Sum
    assert x == y


# Generated at 2022-06-14 03:48:26.082712
# Unit test for method concat of class Last
def test_Last_concat():
    assert Last(2).concat(Last(1)) == Last(1)
    assert Last(None).concat(Last(1)) == Last(1)
    assert Last(2).concat(Last(None)) == Last(None)


# Generated at 2022-06-14 03:48:28.325635
# Unit test for method __str__ of class One
def test_One___str__():
    assert str(One(True)) == 'One[value=True]'
    assert str(One(False)) == 'One[value=False]'


# Generated at 2022-06-14 03:48:35.813812
# Unit test for method concat of class One
def test_One_concat():
    assert One(10).concat(One(20)) == One(10)



# Generated at 2022-06-14 03:48:38.267953
# Unit test for method concat of class One
def test_One_concat():
    accumulator = One(False)
    assert accumulator.concat(One(False)) == One(False)
    assert accumulator.concat(One(True)) == One(True)
    assert accumulator.concat(One(None)) == One(None)


# Generated at 2022-06-14 03:48:40.019283
# Unit test for method concat of class One
def test_One_concat():
    x = One(True)
    y = One(False)
    assert x.concat(y) == One(True)
    assert y.concat(x) == One(True)


# Generated at 2022-06-14 03:48:42.655613
# Unit test for method concat of class Min
def test_Min_concat():
    obj = Min(4)
    assert obj.concat(Min(2)) == Min(2)
    assert obj.concat(Min(5)) == Min(4)


# Generated at 2022-06-14 03:48:44.168300
# Unit test for method __str__ of class All
def test_All___str__():
    assert str(All(True)) == 'All[value=True]'



# Generated at 2022-06-14 03:48:45.114344
# Unit test for constructor of class Max
def test_Max():
    with raises(TypeError):
        Max('a')

# Generated at 2022-06-14 03:48:48.717284
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    data = [Sum(1), Sum(2)]
    expected = [Sum(3)]
    result = Semigroup.fold(data, fn=lambda x: Sum(sum(x)))
    assert result == expected



# Generated at 2022-06-14 03:48:53.698117
# Unit test for method concat of class One
def test_One_concat():
    assert One(True).concat(One(True)) == One(True)
    assert One(True).concat(One(False)) == One(True)
    assert One(False).concat(One(True)) == One(True)
    assert One(False).concat(One(False)) == One(False)



# Generated at 2022-06-14 03:48:57.249442
# Unit test for method concat of class Sum
def test_Sum_concat():
    # when
    sum_1 = Sum(1)
    sum_2 = Sum(2)
    sum_3 = Sum(3)
    # then
    assert sum_1.concat(sum_2).concat(sum_3) == Sum(6)



# Generated at 2022-06-14 03:48:59.053291
# Unit test for method __str__ of class Map
def test_Map___str__():
    assert str(Map({'test': 'value'})) == "Map[value={'test': 'value'}]"



# Generated at 2022-06-14 03:49:08.034113
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    assert Semigroup.neutral().fold(lambda x: x) == Semigroup.neutral_element



# Generated at 2022-06-14 03:49:11.338607
# Unit test for method __str__ of class First
def test_First___str__():  # pragma: no cover
    assert str(First(5)) == 'Fist[value=5]'


# Generated at 2022-06-14 03:49:16.498614
# Unit test for method __str__ of class Map
def test_Map___str__():
    map = Map({'test': Sum(1), 'test2': First(True), 'test3': Last(1)})
    assert str(map) == 'Map[value={\'test\': Sum[value=1], \'test2\': Fist[value=True], \'test3\': Last[value=1]}]'



# Generated at 2022-06-14 03:49:20.669620
# Unit test for constructor of class One
def test_One():
    """
    Test if One constructor works corectly
    :return: boolean
    :rtype: bool
    """

    return One(True) == One(True) and One(True) != One(False)


# Generated at 2022-06-14 03:49:24.326152
# Unit test for constructor of class Map
def test_Map():  # pragma: no cover
    assert Map({'a': Sum(1), 'b': Sum(2)}) == Map({'a': Sum(1), 'b': Sum(2)})



# Generated at 2022-06-14 03:49:27.724799
# Unit test for method concat of class Sum
def test_Sum_concat():
    sum_a = Sum(1)
    sum_b = Sum(2)
    assert sum_a.concat(sum_b) == Sum(3)



# Generated at 2022-06-14 03:49:30.443086
# Unit test for method concat of class All
def test_All_concat():
    assert All(True).concat(All(True)).value is True
    assert All(True).concat(All(False)).value is False
    assert All(False).concat(All(True)).value is False
    assert All(False).concat(All(False)).value is False



# Generated at 2022-06-14 03:49:34.302069
# Unit test for method __str__ of class Min
def test_Min___str__():
    v = Min(5)
    actual = str(v)
    assert actual == "Min[value=5]", "Expected '{}' but got '{}'".format("Min[value=5]", actual)


# Generated at 2022-06-14 03:49:37.568323
# Unit test for method __str__ of class Last
def test_Last___str__():
    first_value = Last('Rafael')
    assert first_value.__str__() == "Last[value=Rafael]"


# Generated at 2022-06-14 03:49:40.002388
# Unit test for method __str__ of class All
def test_All___str__():
    assert str(All(True)) == 'All[value=True]'
    assert str(All(False)) == 'All[value=False]'



# Generated at 2022-06-14 03:49:51.910332
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    assert not Sum(1) == Sum(2)
    assert Sum(1) == Sum(1)

    assert not All(1) == All(False)
    assert not All(False) == All(2)
    assert All(1) == All(1)

    assert not One(1) == One(2)
    assert One(1) == One(1)

    assert not First(1) == First(2)
    assert First(1) == First(1)

    assert not Last(1) == Last(2)
    assert Last(1) == Last(1)

    assert not Map({'a': 1}) == Map({'a': 2})
    assert Map({'a': 1}) == Map({'a': 1})

    assert not Max(1) == Max(2)
    assert Max(1) == Max(1)

# Generated at 2022-06-14 03:49:55.025851
# Unit test for method __str__ of class Max
def test_Max___str__():  # pragma: no cover
    value = Max(5)
    assert str(value) == 'Max[value=5]'


# Generated at 2022-06-14 03:49:58.500202
# Unit test for method concat of class Last
def test_Last_concat():
    assert Last(1).concat(Last(2)) == Last(2)
    assert Last(1).concat(Last(2)).concat(Last(3)) == Last(3)


# Generated at 2022-06-14 03:50:01.870371
# Unit test for constructor of class Sum
def test_Sum():
    assert Sum(3) == Sum(3)
    assert Sum(3) != Sum(4)
    assert Sum(3).fold(lambda v: v) == 3


# Generated at 2022-06-14 03:50:03.986084
# Unit test for constructor of class Semigroup
def test_Semigroup():
    assert Semigroup(1) == Semigroup(1), "Semigroup should equals by value"



# Generated at 2022-06-14 03:50:05.578639
# Unit test for method concat of class Sum
def test_Sum_concat():
    assert Sum(1).concat(Sum(3)) == Sum(4)


# Generated at 2022-06-14 03:50:09.352942
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    assert Semigroup(5).fold(lambda x: x+5) == 10
    assert Semigroup(5).fold(lambda x: x+10) == 15

# Unit tests for method concat of class Sum

# Generated at 2022-06-14 03:50:11.870242
# Unit test for constructor of class Last
def test_Last():
    last = Last(42)
    assert last.__str__() == 'Last[value=42]'


# Generated at 2022-06-14 03:50:13.439566
# Unit test for constructor of class Last
def test_Last():
    last = Last(1)
    assert last.value == 1



# Generated at 2022-06-14 03:50:17.851586
# Unit test for method __str__ of class Map
def test_Map___str__():
    map = Map({'a': Sum(10), 'b': Sum(20)})
    assert map.__str__() == 'Map[value={\'a\': Sum[value=10], \'b\': Sum[value=20]}]'



# Generated at 2022-06-14 03:50:33.238418
# Unit test for method concat of class First
def test_First_concat():
    assert First(1).concat(First(5)) is First(1)



# Generated at 2022-06-14 03:50:46.260467
# Unit test for method __str__ of class Map
def test_Map___str__():
    def _test1():
        m1 = Map({'a': Min(1), 'b': Max(2)})
        assert str(m1) == "Map[value={'a': Min[value=1], 'b': Max[value=2]}]"

    def _test2():
        m1 = Map({'a': Sum(1), 'b': All(2)})
        assert str(m1) == "Map[value={'a': Sum[value=1], 'b': All[value=2]}]"

    def _test3():
        m1 = Map({'a': Last(1), 'b': First(2)})
        assert str(m1) == "Map[value={'a': Fist[value=1], 'b': Last[value=2]}]"


# Generated at 2022-06-14 03:50:48.701843
# Unit test for constructor of class Semigroup
def test_Semigroup():
    assert type(Semigroup(1)) == Semigroup

# Unit tests for methods of class Semigroup

# Generated at 2022-06-14 03:50:51.065354
# Unit test for method concat of class First
def test_First_concat():
    """
    :returns: concat method of First class worked
    """
    assert First(1).concat(First(2)).value == 1


# Generated at 2022-06-14 03:50:54.919679
# Unit test for constructor of class Last
def test_Last():
    """
    Test check constructor of class Last
    """
    last_test: Last = Last(10)
    assert last_test.value == 10
    assert isinstance(last_test, Last)



# Generated at 2022-06-14 03:50:58.189939
# Unit test for constructor of class One
def test_One():
    assert One(True) == One(True)
    assert One(True) != One(False)
    assert One(True) != First(True)
    assert One(True).value == True



# Generated at 2022-06-14 03:51:00.097445
# Unit test for constructor of class Semigroup
def test_Semigroup():
    assert Sum(2) == Sum(2)

# Generated at 2022-06-14 03:51:02.700690
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    assert str(Sum(1)) == "Sum[value=1]"
    assert str(Sum(Sum(1)).concat(Sum(Sum(2)))) == "Sum[value=Sum[value=3]]"


# Generated at 2022-06-14 03:51:07.148860
# Unit test for method concat of class All
def test_All_concat():
    assert All(True).concat(All(True)) == All(True)
    assert All(True).concat(All(False)) == All(False)
    assert All(False).concat(All(True)) == All(False)
    assert All(False).concat(All(False)) == All(False)


# Generated at 2022-06-14 03:51:10.759951
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(8).concat(Max(5)).value == 8
    assert Max(5).concat(Max(8)).value == 8
    assert Max(5).concat(Max(5)).value == 5


# Generated at 2022-06-14 03:51:25.293307
# Unit test for constructor of class All
def test_All():
    a = All(False)
    b = All(True)
    assert a.value == False
    assert b.value == True


# Generated at 2022-06-14 03:51:30.934728
# Unit test for method concat of class Map
def test_Map_concat():
    """
    Testing of method concat for class Map
    """
    assert Map({"a": Sum(1), "b": Sum(2)}).concat(Map({"a": Sum(10), "b": Sum(20)})) == Map({"a": Sum(11), "b": Sum(22)})


# Generated at 2022-06-14 03:51:36.453855
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    semigroup_1 = Sum(1)
    semigroup_2 = Sum(1)
    semigroup_3 = Sum(2)
    assert semigroup_1 == semigroup_2
    assert semigroup_1 != semigroup_3


# Generated at 2022-06-14 03:51:39.214476
# Unit test for constructor of class Sum
def test_Sum():
    def get_sum(a, b) -> Sum:
        return Sum(a).concat(Sum(b))

    assert Sum(1).value == 1
    assert get_sum(1, 2).value == 3



# Generated at 2022-06-14 03:51:41.086573
# Unit test for constructor of class All
def test_All():
    assert All(True).value == True


# Generated at 2022-06-14 03:51:43.994372
# Unit test for method __str__ of class Last
def test_Last___str__():  # pragma: no cover
    last = Last(123)
    assert last.__str__() == "Last[value=123]"


# Generated at 2022-06-14 03:51:45.794375
# Unit test for constructor of class Sum
def test_Sum():
    """
    >>> Sum(0)
    Sum[value=0]
    """

    pass



# Generated at 2022-06-14 03:51:48.949148
# Unit test for method __str__ of class Last
def test_Last___str__():
    assert str(Last(1)) == 'Last[value=1]'
    assert str(Last('abc')) == 'Last[value=abc]'


# Generated at 2022-06-14 03:51:53.613219
# Unit test for method concat of class All
def test_All_concat():
    assert All(True).concat(All(True)).value is True
    assert All(True).concat(All(False)).value is False
    assert All(False).concat(All(True)).value is False
    assert All(False).concat(All(False)).value is False


# Generated at 2022-06-14 03:51:55.983310
# Unit test for method concat of class Min
def test_Min_concat():
    m1 = Min(10)
    m2 = Min(5)
    m3 = m1.concat(m2)
    assert m3.value == 5



# Generated at 2022-06-14 03:52:25.198082
# Unit test for constructor of class One
def test_One():
    o = One(True)
    assert o.value == True
    assert o.concat(o).value == True
    o = One(False)
    assert o.value == False
    assert o.concat(o).value == False
    


# Generated at 2022-06-14 03:52:27.621685
# Unit test for constructor of class Map
def test_Map():
    m = Map({'a': Sum(1), 'b': Sum(1)})
    assert m == Map({'a': Sum(1), 'b': Sum(1)})

# Generated at 2022-06-14 03:52:33.890428
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    assert Sum(1).fold(lambda x: x + 1) == 2
    assert All(True).fold(lambda x: x) is True
    assert One(False).fold(lambda x: x) is False
    assert First("1").fold(lambda x: x * 2) == "11"
    assert Last("1").fold(lambda x: x * 2) == "11"
    assert Max(-1).fold(lambda x: x * 2) == -2
    assert Min(-1).fold(lambda x: x * 2) == -2
    assert Map({"hello": First("world")}).fold(lambda x: len(x)) == 1



# Generated at 2022-06-14 03:52:38.737599
# Unit test for constructor of class Min
def test_Min():
    assert Min(-float("inf")).concat(Min(-1)).value == -1 == Min(-1).concat(Min(-float("inf"))).value

# Generated at 2022-06-14 03:52:44.151373
# Unit test for method concat of class All
def test_All_concat():
    assert All(True).concat(All(True)) == All(True)
    assert All(True).concat(All(False)) == All(False)
    assert All(False).concat(All(True)) == All(False)
    assert All(False).concat(All(False)) == All(False)


# Generated at 2022-06-14 03:52:46.115110
# Unit test for method concat of class Sum
def test_Sum_concat():
    assert (Sum(1).concat(Sum(2)) == Sum(3)) == True



# Generated at 2022-06-14 03:52:52.223513
# Unit test for method concat of class All
def test_All_concat():
    assert All(False).concat(All(True)) == All(False)
    assert All(True).concat(All(False)) == All(False)
    assert All(False).concat(All(False)) == All(False)
    assert All(True).concat(All(True)) == All(True)


# Generated at 2022-06-14 03:52:55.179615
# Unit test for method concat of class Sum
def test_Sum_concat():
    assert Sum(1).concat(Sum(2)) == Sum(3)



# Generated at 2022-06-14 03:52:57.534604
# Unit test for method __str__ of class First
def test_First___str__():
    inst = First(4)

    assert(str(inst) == 'Fist[value=4]')


# Generated at 2022-06-14 03:53:07.484875
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    assert All('foo') == All('foo')
    assert Sum(3) == Sum(3)
    assert One('bar') == One('bar')
    assert First('baz') == First('baz')
    assert Last('qux') == Last('qux')
    assert Map({1: Sum(1), 2: Sum(2)}) == Map({1: Sum(1), 2: Sum(2)})
    assert Max(1) == Max(1)
    assert Min(2) == Min(2)


# Generated at 2022-06-14 03:54:07.923303
# Unit test for method __str__ of class First
def test_First___str__():  # type: () -> None
    assert str(First(1)) == 'Fist[value=1]'
    assert str(First('a')) == 'Fist[value=a]'
    assert str(First([1, 2, 3])) == 'Fist[value=[1, 2, 3]]'


# Generated at 2022-06-14 03:54:09.048748
# Unit test for method __str__ of class All
def test_All___str__():
    assert str(All(True)) == 'All[value=True]'


# Generated at 2022-06-14 03:54:12.188319
# Unit test for method concat of class Map
def test_Map_concat():
    """
    method concat test
    """
    assert Map({"1": Sum(1)}).concat(Map({"1": Sum(2)})) == Map({"1": Sum(1) + Sum(2)})

# Generated at 2022-06-14 03:54:13.846070
# Unit test for method concat of class Sum
def test_Sum_concat():
    assert Sum(1).concat(Sum(2)) == Sum(3)



# Generated at 2022-06-14 03:54:18.066062
# Unit test for constructor of class All
def test_All():  # pragma: no cover
    all_true = All(True)
    assert all_true.value is True

    all_false = All(False)
    assert all_false.value is False



# Generated at 2022-06-14 03:54:20.752049
# Unit test for method __str__ of class Map
def test_Map___str__():
    assert str(Map({1: Sum(1)})) == 'Map[value={1: Sum[value=1]}]'


# Generated at 2022-06-14 03:54:22.777066
# Unit test for constructor of class One
def test_One():
    # We expect One(1) == One(1)
    assert One(1) == One(1)


# Generated at 2022-06-14 03:54:26.198446
# Unit test for constructor of class Last
def test_Last():
    v1 = Last(1)
    v2 = Last(2)
    v3 = Last(3)
    eq_(1,v1.value)
    eq_(2,v2.value)
    eq_(3,v3.value)
