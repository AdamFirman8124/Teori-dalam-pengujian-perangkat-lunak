

# Generated at 2022-06-14 03:44:39.454806
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(3).concat(Min(1)) == Min(1)

    assert Min(4).concat(Min(4)) == Min(4)

    assert Min(1).concat(Min(3)) == Min(1)

    assert Min(4).concat(Min(3)) == Min(3)

    assert Min(3).concat(Min(4)) == Min(3)



# Generated at 2022-06-14 03:44:43.991283
# Unit test for method concat of class Min
def test_Min_concat():
    assert (Min(1).concat(Min(2))) == Min(1)
    assert (Min(2).concat(Min(2))) == Min(2)
    assert (Min(3).concat(Min(2))) == Min(2)

# Generated at 2022-06-14 03:44:48.308301
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(4).concat(Min(3)) == Min(3)
    assert Min(3).concat(Min(4)) == Min(3)
    assert Min(3).concat(Min(3)) == Min(3)


# Generated at 2022-06-14 03:44:50.246391
# Unit test for method concat of class Min
def test_Min_concat():
    result = Min(5).concat(Min(10))
    expected = Min(5)

    assert result == expected



# Generated at 2022-06-14 03:44:53.564056
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(5).concat(Max(3)) == Max(5)
    assert Max(3).concat(Max(5)) == Max(5)
    assert Max(5).concat(Max(5)) == Max(5)


# Generated at 2022-06-14 03:44:55.494052
# Unit test for method concat of class Max
def test_Max_concat():
    a = Max(8)
    b = Max(7)
    assert a.concat(b) == Max(8)



# Generated at 2022-06-14 03:44:59.722838
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(2).concat(Min(4)) == Min(2)
    assert Min(4).concat(Min(2)) == Min(2)
    assert Min(2).concat(Min(2)) == Min(2)



# Generated at 2022-06-14 03:45:02.673040
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(1).concat(Max(2)) == Max(2)


# Generated at 2022-06-14 03:45:08.175029
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(1).concat(Min(2)).value == 1
    assert Min(4).concat(Min(3)).value == 3
    assert Min(1).concat(Min(2)).concat(Min(3)).concat(Min(4)).value == 1



# Generated at 2022-06-14 03:45:11.757832
# Unit test for method concat of class Min
def test_Min_concat():
    min1 = Min(567)
    min2 = Min(23)

    assert min1.concat(min2) == Min(23)


# Generated at 2022-06-14 03:45:14.700506
# Unit test for constructor of class All
def test_All():
    assert All(True)
    assert All(False)



# Generated at 2022-06-14 03:45:16.348071
# Unit test for constructor of class One
def test_One():
    """
    Unit test for constructor of class One.
    """

    one_instance = One(1)
    assert one_instance.value is 1


# Generated at 2022-06-14 03:45:20.230838
# Unit test for constructor of class First
def test_First():
    assert isinstance(First(1), First), 'First object is not a First class object'
    assert isinstance(First([1]), First), 'First object is not a First class object'


# Generated at 2022-06-14 03:45:22.911891
# Unit test for constructor of class Max
def test_Max():
    assert Max(12) == Max(12)
    assert Max(12) != Max(14)


# Generated at 2022-06-14 03:45:25.105355
# Unit test for constructor of class Map
def test_Map():
    assert Map({1: Sum(1), 2: Sum(2)}).value == {1: Sum(1), 2: Sum(2)}


# Generated at 2022-06-14 03:45:28.166522
# Unit test for method __str__ of class Last
def test_Last___str__():
    # Set up fixture
    semigroup = Last('test')
    # Exercise
    value = str(semigroup)
    # Verify
    assert value == 'Last[value=test]'



# Generated at 2022-06-14 03:45:29.854424
# Unit test for constructor of class All
def test_All():
    assert All(True).value == True
    assert All(False).value == False


# Generated at 2022-06-14 03:45:34.151714
# Unit test for constructor of class Map
def test_Map():
    assert Map({'a': Sum(1), 'b': First('a')}) == Map(
        {'a': Sum(1), 'b': First('a')}
    )


# Generated at 2022-06-14 03:45:35.342890
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    assert str(Sum(1)) == 'Sum[value=1]'



# Generated at 2022-06-14 03:45:39.567732
# Unit test for method __str__ of class Map
def test_Map___str__(): # pragma: no cover
    assert str(Map({})) == 'Map[value={}]'
    assert str(Map({'a': Sum(1)})) == 'Map[value={\'a\': Sum[value=1]}]'
    assert str(Map({'a': Sum(1), 'b': Sum(2)})) == 'Map[value={\'a\': Sum[value=1], \'b\': Sum[value=2]}]'


# Generated at 2022-06-14 03:45:45.410451
# Unit test for constructor of class Semigroup
def test_Semigroup():
    assert Semigroup(10).value == 10
    assert Semigroup("asdasd").value == "asdasd"
    assert Semigroup(True).value == True
    assert Semigroup(None).value is None
    assert Semigroup([1, 2, 3]).value == [1, 2, 3]


# Generated at 2022-06-14 03:45:47.879503
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    assert str(Sum(1)) == "Sum[value=1]"

# Unit tests for method concat of class Sum

# Generated at 2022-06-14 03:45:49.571581
# Unit test for method __str__ of class Map
def test_Map___str__():
    def foo():
        return 0

    assert str(Map(foo)) == 'Map[value=0]'


# Generated at 2022-06-14 03:45:52.353762
# Unit test for constructor of class Min
def test_Min():
    min_object = Min(2)
    min_object2 = Min(3)
    assert(min_object.value == 2)
    assert(min_object2.value == 3)
    assert(min_object.concat(min_object2).value == 2)


# Generated at 2022-06-14 03:45:55.452820
# Unit test for constructor of class Map
def test_Map():
    m = Map({"a": Sum(1), "b": Sum(2)})
    assert m.value == {"a": Sum(1), "b": Sum(2)}


# Generated at 2022-06-14 03:45:56.967157
# Unit test for constructor of class Last
def test_Last():
    last = Last(1)

    assert last.value == 1


# Generated at 2022-06-14 03:45:58.757953
# Unit test for method __str__ of class First
def test_First___str__():  # pragma: no cover
    assert str(First(1)) == 'Fist[value=1]'


# Generated at 2022-06-14 03:46:03.031076
# Unit test for constructor of class All
def test_All():
    assert All(True) == All(True)
    assert All(False) == All(False)
    assert All(False) != All(True)



# Generated at 2022-06-14 03:46:06.952987
# Unit test for constructor of class One
def test_One():
    """
    Test one method.
    - Test One input is instance of object.
    - Test One input is falsey.
    """
    one = One(1)
    assert isinstance(one, One)
    assert one.value is not False
    one = One(False)
    assert isinstance(one, One)
    assert one.value is False


# Generated at 2022-06-14 03:46:09.983760
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    assert str(Sum(3)) == 'Sum[value=3]'
    assert str(Sum(0)) == 'Sum[value=0]'
    assert str(Sum(-1)) == 'Sum[value=-1]'



# Generated at 2022-06-14 03:46:13.090973
# Unit test for method __str__ of class First
def test_First___str__():
    assert str(First(1)) == 'Fist[value=1]'



# Generated at 2022-06-14 03:46:14.871551
# Unit test for constructor of class Max
def test_Max():
    assert Max(2) == Max(2)
    assert Max(10) != Max(11)


# Generated at 2022-06-14 03:46:16.831539
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    assert Semigroup(1).fold(lambda x: x + 1) == 2


# Unit tests for concat method of class Sum

# Generated at 2022-06-14 03:46:18.093792
# Unit test for method concat of class First
def test_First_concat():
    assert First(1).concat(First(2)) == First(1)


# Generated at 2022-06-14 03:46:22.484511
# Unit test for constructor of class First
def test_First():  # pragma: no cover
    assert First(1).value == 1
    assert First([1, 2]).value == [1, 2]
    assert First('string').value == 'string'
    assert First(True).value == True



# Generated at 2022-06-14 03:46:27.364235
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    assert Semigroup(1).fold(lambda x: x * 2) == 2
    assert Semigroup(4).fold(lambda x: x * 2) == 8
    assert Semigroup('x').fold(lambda x: x + 'y') == 'xy'



# Generated at 2022-06-14 03:46:28.811810
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(4)) == 'Max[value=4]'


# Generated at 2022-06-14 03:46:36.592843
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    assert Sum.neutral().fold(lambda x: x) == 0
    assert All.neutral().fold(lambda x: x) == True
    assert One.neutral().fold(lambda x: x) == False
    assert First.neutral().fold(lambda x: x) == None
    assert Last.neutral().fold(lambda x: x) == None
    assert Map.neutral().fold(lambda x: x) == {}
    assert Max.neutral().fold(lambda x: x) == float("-inf")
    assert Min.neutral().fold(lambda x: x) == float("inf")



# Generated at 2022-06-14 03:46:38.413602
# Unit test for method __str__ of class One
def test_One___str__():
    assert str(One(True)) == 'One[value=True]'


# Generated at 2022-06-14 03:46:39.909586
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(1).concat(Max(2)) == Max(2)


# Generated at 2022-06-14 03:46:53.396558
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    assert Sum(1).fold(lambda x: x + 1) == 2
    assert All(True).fold(lambda x: x is True)
    assert One(False).fold(lambda x: x is False)
    assert First('lorem').fold(lambda x: x) == 'lorem'
    assert Last('ipsum').fold(lambda x: x) == 'ipsum'
    assert Map({'a': Sum(2)}).fold(lambda x: x) == Map({'a': Sum(2)}).value
    assert Max(13).fold(lambda x: x) == 13
    assert Min(13).fold(lambda x: x) == 13


# Generated at 2022-06-14 03:46:55.450306
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(5)) == 'Max[value=5]'



# Generated at 2022-06-14 03:46:57.453788
# Unit test for method concat of class Last
def test_Last_concat():
    assert Last(1).concat(Last(2)) == Last(2)


# Generated at 2022-06-14 03:46:59.040841
# Unit test for method __str__ of class Min
def test_Min___str__():
    assert str(Min(3)) == 'Min[value=3]'


# Generated at 2022-06-14 03:47:02.613424
# Unit test for constructor of class First
def test_First():
    first1 = First('a')
    first2 = First('b')
    assert first1.value == 'a'
    assert first2.value == 'b'
    assert first1 != first2


# Generated at 2022-06-14 03:47:05.911287
# Unit test for method __str__ of class Map
def test_Map___str__():
    assert str(Map({'name': First('Petia'), 'age': Max(18)})) == 'Map[value={\'name\': Fist[value=Petia], \'age\': Max[value=18]}]'

# Generated at 2022-06-14 03:47:06.919808
# Unit test for constructor of class Max
def test_Max():
    max = Max(1)



# Generated at 2022-06-14 03:47:11.085724
# Unit test for constructor of class Max
def test_Max():
    max_test_1 = Max(1)
    max_test_2 = Max(2)
    assert max_test_1 == max_test_1
    assert max_test_1 != max_test_2
    assert max_test_1.value == 1
    assert max_test_2.value == 2


# Generated at 2022-06-14 03:47:15.038292
# Unit test for method __str__ of class All
def test_All___str__():
    assert str(All(5)) == 'All[value=5]'
    assert str(All(True)) == 'All[value=True]'
    assert str(All(False)) == 'All[value=False]'


# Generated at 2022-06-14 03:47:25.673888
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    assert not Semigroup(1).__eq__(Semigroup(2))
    assert Sum(1).__eq__(Sum(1))
    assert All(True).__eq__(All(True))
    assert not All(True).__eq__(All(False))
    assert One(False).__eq__(One(False))
    assert not One(False).__eq__(One(True))
    assert not First(1).__eq__(First(2))
    assert First(1).__eq__(First(1))
    assert not Last(1).__eq__(Last(2))
    assert Last(1).__eq__(Last(1))
    assert not Map({1: Sum(1)}).__eq__(Map({2: Sum(2)}))

# Generated at 2022-06-14 03:47:35.019602
# Unit test for constructor of class Sum
def test_Sum():
    # Sum of two numbers (2, 5) should be 7
    assert Sum(2).concat(Sum(5)) == Sum(7)  # Sum[value=7]
    # Sum of two numbers (2, 5) should not be 5
    assert Sum(2).concat(Sum(5)) != Sum(5)  # Sum[value=5]
    # Sum of two numbers (2, 0) should be 2
    assert Sum(2).concat(Sum(0)) == Sum(2)  # Sum[value=2]
    # Sum of two numbers (0, 5) should be 5
    assert Sum(0).concat(Sum(5)) == Sum(5)  # Sum[value=5]



# Generated at 2022-06-14 03:47:40.995448
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    assert First(100).fold(lambda x: x + 20) == 120
    assert Last(100).fold(lambda x: x + 20) == 120
    assert Sum(100).fold(lambda x: x + 20) == 120
    assert All(True).fold(lambda x: x and True) == True
    assert One(False).fold(lambda x: x or False) == False


# Generated at 2022-06-14 03:47:43.254132
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    assert Semigroup(1) == Semigroup(1)
    assert not Semigroup(1) == Semigroup(2)


# Generated at 2022-06-14 03:47:48.694351
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    assert str(Sum(1)) == 'Sum[value=1]'
    assert str(Sum(None)) == 'Sum[value=None]'
    assert str(Sum('a')) == 'Sum[value=a]'


# Generated at 2022-06-14 03:47:57.663186
# Unit test for method concat of class Map
def test_Map_concat():
    assert Map({"a": Sum(1), "b": Sum(2)}).concat(Map({"a": Sum(1), "b": Sum(2)})) == Map({"a": Sum(2), "b": Sum(4)})
    assert Map({"a": Sum(1), "b": Sum(2)}).concat(Map({"a": Sum(1), "b": Sum(3)})) == Map({"a": Sum(2), "b": Sum(5)})
    assert Map({"a": Sum(1), "b": Sum(2)}).concat(Map({"a": Sum(1), "b": Sum(4)})) == Map({"a": Sum(2), "b": Sum(6)})

# Generated at 2022-06-14 03:47:59.328493
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    assert not Sum(5).__eq__(All(5))
    assert Sum(3).__eq__(Sum(3))
    assert All(3).__eq__(All(3))


# Generated at 2022-06-14 03:48:04.324527
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    s = Sum(10)
    assert s.fold(lambda value: value * value) == 100

    s = All(True)
    assert s.fold(lambda value: value * value) == 1

    s = One(True)
    assert s.fold(lambda value: value * value) == 1

    s = Map({'a': First(1), 'b': First(2)})
    assert s.fold(lambda value: value['a'].value) == 1

    s = Map({'a': Last(1), 'b': Last(2)})
    assert s.fold(lambda value: value['a'].value) == 1



# Generated at 2022-06-14 03:48:10.240245
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    """
    Unit test for method __eq__ of class Semigroup
    """

    assert Sum(1) == Sum(1)

    assert All(True) == All(True)

    assert First(1) == First(1)

    assert Last(2) == Last(2)

    assert Max(2) == Max(2)

    assert Min(1) == Min(1)



# Generated at 2022-06-14 03:48:12.831629
# Unit test for constructor of class First
def test_First():
    assert First('Oracle').value == 'Oracle'



# Generated at 2022-06-14 03:48:14.423777
# Unit test for constructor of class Min
def test_Min():
    assert (Min(1).value == 1)


# Generated at 2022-06-14 03:48:18.426668
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    sum = Sum(value=10)
    assert str(sum) == 'Sum[value=10]'



# Generated at 2022-06-14 03:48:21.987484
# Unit test for constructor of class Map
def test_Map():
    value = {'a': Sum(1), 'b': One(True)}
    assert Map(value) == Map(value)


# Generated at 2022-06-14 03:48:26.017793
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(1).concat(Min(2)).fold(lambda v: v) == 1
    assert Min(2).concat(Min(1)).fold(lambda v: v) == 1


# Generated at 2022-06-14 03:48:28.609475
# Unit test for constructor of class Sum
def test_Sum():
    assert Sum(5) == Sum(5)
    assert Sum(5) != Sum(6)
    assert Sum(5).neutral() == Sum(0)


# Generated at 2022-06-14 03:48:30.378566
# Unit test for method __str__ of class All
def test_All___str__():
    assert str(All(1)) == 'All[value=1]'


# Generated at 2022-06-14 03:48:34.366281
# Unit test for method concat of class All
def test_All_concat():
    assert All(True) == All(True).concat(All(True))
    assert All(False) == All(False).concat(All(True))
    assert All(False) == All(False).concat(All(False))


# Generated at 2022-06-14 03:48:35.687944
# Unit test for method __str__ of class Min
def test_Min___str__():
    assert str(Min(1)) == 'Min[value=1]'



# Generated at 2022-06-14 03:48:36.710728
# Unit test for method __str__ of class Last
def test_Last___str__():
    assert str(Last(5)) == 'Last[value=5]'



# Generated at 2022-06-14 03:48:40.047552
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    assert Semigroup(5).fold(lambda x: x ** 2) == 25



# Generated at 2022-06-14 03:48:42.157349
# Unit test for method concat of class First
def test_First_concat():
    """
    Unit test for method concat of class First
    """
    first = First(1)
    second = First(2)
    assert first.concat(second).value == 1
    assert first.concat(first) == first
    assert first == first.concat(first)


# Generated at 2022-06-14 03:48:51.390067
# Unit test for method __str__ of class Map
def test_Map___str__():  # pragma: no cover
    assert str(Map({'test': Sum(1)})) == 'Map[value={\'test\': Sum[value=1]}]'

# Generated at 2022-06-14 03:48:52.796393
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(6)) == 'Max[value=6]'


# Generated at 2022-06-14 03:48:54.398905
# Unit test for constructor of class Max
def test_Max():
    assert Max(1) == Max(1)



# Generated at 2022-06-14 03:48:55.626017
# Unit test for constructor of class Sum
def test_Sum():
    assert Sum(1).concat(Sum(2)) == Sum(3)


# Generated at 2022-06-14 03:48:56.872805
# Unit test for method __str__ of class First
def test_First___str__():
    assert str(First(3)) == 'Fist[value=3]'


# Generated at 2022-06-14 03:49:06.788277
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(3).concat(Min(3)) == Min(3)
    assert Min(3).concat(Min(1)) == Min(1)
    assert Min(3).concat(Min(5)) == Min(3)
    assert Min(5).concat(Min(3)) == Min(3)
    assert Min(-3).concat(Min(-5)) == Min(-5)
    assert Min(-5).concat(Min(-3)) == Min(-3)
    assert Min(-5.5).concat(Min(-3.5)) == Min(-3.5)
    assert Min(-3.5).concat(Min(-5.5)) == Min(-5.5)
    assert Min(0).concat(Min(5)) == Min(0)

# Generated at 2022-06-14 03:49:08.774883
# Unit test for constructor of class Min
def test_Min(): # pragma: no cover
    assert Min(1)



# Generated at 2022-06-14 03:49:11.674828
# Unit test for method concat of class First
def test_First_concat():
    assert First(1).concat(First(2)) == First(1)

# Generated at 2022-06-14 03:49:17.487036
# Unit test for constructor of class All
def test_All():
    assert All(True) == All(True)
    assert All(True) != All(False)
    assert All(True).concat(All(False)) == All(False)
    assert All(True).concat(All(True)) == All(True)
    assert All(False).concat(All(False)) == All(False)
    assert All(False) == All.neutral()



# Generated at 2022-06-14 03:49:18.616583
# Unit test for method __str__ of class All
def test_All___str__():
    all = All(True)
    assert str(all) == "All[value=True]"


# Generated at 2022-06-14 03:49:28.756040
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(1)) == 'Max[value=1]'
    assert str(Max(1.1)) == 'Max[value=1.1]'
    assert str(Max('hello')) == 'Max[value=hello]'


# Generated at 2022-06-14 03:49:30.891843
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(4).concat(Max(7)) == Max(7)



# Generated at 2022-06-14 03:49:35.427930
# Unit test for constructor of class Max
def test_Max():
    assert Max(1).value == 1
    assert Max(1).__str__() == "Max[value=1]"
    assert Max(1) == Max(1)
    assert not Max(1) == Max(2)
    assert Max(1).fold(lambda x: x) == 1


# Generated at 2022-06-14 03:49:39.389045
# Unit test for constructor of class Map
def test_Map():
    """
    :returns: Map
    :rtype: Map[A]
    """
    return Map({'a': Sum(2), 'b': Sum(1)})


# Generated at 2022-06-14 03:49:44.063198
# Unit test for constructor of class Min
def test_Min():
    assert Min(1) == Min(1)
    assert Min(0) == Min(0)
    assert Min(1) != Min(0)
    assert Min(2.33) != Min(1)
    assert Min(1.0) == Min(1)
    assert Min(0.0) == Min(0)
    assert Min(1.0) != Min(0)
    assert Min(2.33) != Min(1)


# Generated at 2022-06-14 03:49:47.414066
# Unit test for method __str__ of class One
def test_One___str__():
    assert str(One(True)) == 'One[value=True]'
    assert str(One(False)) == 'One[value=False]'



# Generated at 2022-06-14 03:49:48.107785
# Unit test for method __str__ of class Last
def test_Last___str__():
    assert str(Last(5)) == 'Last[value=5]'


# Generated at 2022-06-14 03:49:48.921228
# Unit test for method __str__ of class One
def test_One___str__():
    assert str(One(1)) == 'One[value=1]'


# Generated at 2022-06-14 03:49:50.087404
# Unit test for method concat of class Sum
def test_Sum_concat():
    sum_instance = Sum(1)
    assert sum_instance.concat(Sum(2)) == Sum(3)



# Generated at 2022-06-14 03:49:53.255516
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():  # pragma: no cover
    assert Semigroup(1).fold(lambda x: x + 1) == 2
    assert Semigroup(2).fold(lambda x: x + 1) == 3
    assert Semigroup(2).fold(lambda x: x * 2) == 4
    assert Semigroup(3).fold(lambda x: x * 2) == 6


# Generated at 2022-06-14 03:50:01.609767
# Unit test for constructor of class Min
def test_Min():
    assert Min(1) == Min(1)

# Generated at 2022-06-14 03:50:05.649071
# Unit test for method __str__ of class Map
def test_Map___str__():
    map_ = Map({'a': Sum(1), 'b': Sum(2)})
    assert str(map_) == "Map[value={'a': Sum[value=1], 'b': Sum[value=2]}]"



# Generated at 2022-06-14 03:50:09.412345
# Unit test for constructor of class Map
def test_Map():
    assert Map({1: First(1), 2: First(2), 3: Last(3)}).value == {1: First(1), 2: First(2), 3: Last(3)}


# Generated at 2022-06-14 03:50:14.954550
# Unit test for method concat of class Map
def test_Map_concat():
    a = Map({
        1: Sum(1),
        2: Sum(2),
    })

    b = Map({
        1: Sum(3),
        2: Sum(4),
    })

    c = Map({
        1: Sum(4),
        2: Sum(6),
    })

    assert a.concat(b) == c



# Generated at 2022-06-14 03:50:16.257280
# Unit test for constructor of class Semigroup
def test_Semigroup():
    assert Semigroup(5)



# Generated at 2022-06-14 03:50:18.757478
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(1).concat(Max(3)) == Max(3)


# Generated at 2022-06-14 03:50:28.766567
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    assert Sum(5) == Sum(5) is True
    assert Sum(5) == Sum(6) is False
    assert Sum(5) == All(True) is False
    assert All(True) == All(True) is True
    assert All(True) == All(False) is False
    assert All(True) == First(True) is False
    assert First(True) == First(True) is True
    assert First(False) == First(True) is False
    assert First(False) == Last(False) is False
    assert Last(False) == Last(False) is True
    assert Last(False) == Last(True) is True
    assert Last(False) == Map({1: Sum(1), 2: All(True)}) is False

# Generated at 2022-06-14 03:50:31.802668
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    val_a = Sum(123)
    val_b = Sum(123)
    val_c = Sum(321)

    assert val_a == val_b
    assert not val_a == val_c


# Generated at 2022-06-14 03:50:34.003729
# Unit test for constructor of class Sum
def test_Sum(): # pragma: no cover
    assert Sum(2) == Sum(2)


# Generated at 2022-06-14 03:50:36.220375
# Unit test for constructor of class Min
def test_Min():
    assert Min(2) == Min(2)
    assert Min(3) != Min(4)



# Generated at 2022-06-14 03:50:47.437728
# Unit test for method concat of class All
def test_All_concat():
    assert All(True).concat(All(True)) == All(True)
    assert All(True).concat(All(False)) == All(False)
    assert All(False).concat(All(True)) == All(False)
    assert All(False).concat(All(False)) == All(False)


# Generated at 2022-06-14 03:50:52.494551
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    """
    Test fold method of class Semigroup
    """
    # Scenario 1: getting sum of numbers
    initial_value = 0
    semigroup = Sum(1)
    assert semigroup.fold(lambda x: x + 1) == 2

# Generated at 2022-06-14 03:50:54.101167
# Unit test for constructor of class Max
def test_Max():
    assert Max(1) == Max(1)


# Generated at 2022-06-14 03:50:57.136379
# Unit test for method concat of class First
def test_First_concat():  # pragma: no cover
    assert First('a').concat(First('b')).value == 'a'


# Generated at 2022-06-14 03:51:00.852478
# Unit test for constructor of class Map
def test_Map():
    cube = {
        'x': Sum(3),
        'y': Sum(4),
        'z': Sum(2)
    }

    other = Map({'x': Sum(5), 'y': Sum(6), 'z': Sum(8)})
    assert Map(cube) == other



# Generated at 2022-06-14 03:51:05.111255
# Unit test for constructor of class Map
def test_Map():
    """
    Unit test for constructor of class Map
    """

    # Test creation of list
    some = Map({1: Sum(2), 2: Sum(3)})
    assert isinstance(some, Map)
    assert isinstance(some.value.__getitem__(1), Sum)
    assert isinstance(some.value.__getitem__(2), Sum)
    assert some.value.__getitem__(1) == Sum(2)
    assert some.value.__getitem__(2) == Sum(3)



# Generated at 2022-06-14 03:51:09.383282
# Unit test for constructor of class Map
def test_Map():
    a = Map({'a': Sum(1), 'b': Sum(2)})
    b = Map({'a': Sum(3), 'b': Sum(4)})
    assert a.concat(b).value == {'a': Sum(4), 'b': Sum(6)}

# Generated at 2022-06-14 03:51:10.759088
# Unit test for method __str__ of class First
def test_First___str__():
    assert str(First(42)) == 'Fist[value=42]'



# Generated at 2022-06-14 03:51:17.780708
# Unit test for method concat of class All
def test_All_concat():
    assert All(True).concat(All(True)) == All(True)
    assert All(True).concat(All(False)) == All(False)
    assert All(False).concat(All(True)) == All(False)
    assert All(False).concat(All(False)) == All(False)



# Generated at 2022-06-14 03:51:18.940100
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(2)) == 'Max[value=2]'


# Generated at 2022-06-14 03:51:27.232495
# Unit test for method __str__ of class First
def test_First___str__():
    assert str(First(1)) == 'Fist[value=1]'



# Generated at 2022-06-14 03:51:29.134460
# Unit test for constructor of class Min
def test_Min():
    min = Min(5)
    assert min.value == 5



# Generated at 2022-06-14 03:51:32.549068
# Unit test for constructor of class Min
def test_Min():
    m1 = Min(1)
    assert m1.value == 1

    m2 = Min(2)
    assert m2.value == 2

test_Min()


# Generated at 2022-06-14 03:51:34.949517
# Unit test for method __str__ of class First
def test_First___str__():
    assert str(First(2)) == "Fist[value=2]"



# Generated at 2022-06-14 03:51:35.776175
# Unit test for method __str__ of class All
def test_All___str__():
    assert str(All(True)) == 'All[value=True]'



# Generated at 2022-06-14 03:51:37.798817
# Unit test for method __str__ of class First
def test_First___str__():
    f1 = First(1)
    print(f1)
    assert str(f1) == 'Fist[value=1]'



# Generated at 2022-06-14 03:51:40.056626
# Unit test for method __str__ of class All
def test_All___str__():  # pragma: no cover
    assert str(All(True)) == 'All[value=True]'



# Generated at 2022-06-14 03:51:43.415722
# Unit test for constructor of class First
def test_First():
    assert First(1) == First(1)
    assert First(1).concat(First(2)) == First(1)
    assert First(1).fold() == 1
    assert First.neutral() == First(False)


# Generated at 2022-06-14 03:51:46.072248
# Unit test for constructor of class Max
def test_Max():
    m1 = Max(1)
    m2 = Max(2)
    m3 = m1.concat(m2)

    assert Max(2) == m3


# Generated at 2022-06-14 03:51:48.457811
# Unit test for method __str__ of class All
def test_All___str__():
    assert str(All(True)) == 'All[value=True]', 'Test failed'



# Generated at 2022-06-14 03:51:59.509748
# Unit test for method __str__ of class All
def test_All___str__():
    expected_str = 'All[value=foo]'
    actual_str = str(All('foo'))

    assert isinstance(actual_str, str)
    assert actual_str == expected_str


# Generated at 2022-06-14 03:52:02.032042
# Unit test for method __str__ of class All
def test_All___str__():
    assert str(All(False)) == 'All[value=False]'
    assert str(All(True)) == 'All[value=True]'


# Generated at 2022-06-14 03:52:03.719700
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(5)) == "Max[value=5]"


# Generated at 2022-06-14 03:52:08.104556
# Unit test for method __str__ of class First
def test_First___str__():
    assert str(First(False)) == 'Fist[value=False]'
    assert str(First(True)) == 'Fist[value=True]'
    assert str(First(0)) == 'Fist[value=0]'
    assert str(First(1)) == 'Fist[value=1]'
    assert str(First('value')) == "Fist[value=value]"



# Generated at 2022-06-14 03:52:13.922911
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(3).concat(Min(1)) == Min(1)
    assert Min(3).concat(Min(3)) == Min(3)
    assert Min(3).concat(Min(5)) == Min(3)
    assert Min(-1).concat(Min(-5)) == Min(-1)



# Generated at 2022-06-14 03:52:15.661000
# Unit test for constructor of class Sum
def test_Sum():
    assert Sum(3) == Sum(3)



# Generated at 2022-06-14 03:52:23.479931
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    assert Sum(1).fold(lambda x: x) == 1
    assert All(True).fold(lambda x: x) is True
    assert One(False).fold(lambda x: x) is False
    assert First('value').fold(lambda x: x) == 'value'
    assert Last('value').fold(lambda x: x) == 'value'
    assert Max(1).fold(lambda x: x) == 1
    assert Min(1).fold(lambda x: x) == 1

# Generated at 2022-06-14 03:52:24.462001
# Unit test for constructor of class First
def test_First():
    assert First is Semigroup



# Generated at 2022-06-14 03:52:25.791715
# Unit test for constructor of class Sum
def test_Sum():
    assert Sum(1) == Sum(1)


# Generated at 2022-06-14 03:52:31.049618
# Unit test for method concat of class Map
def test_Map_concat():
    map1 = Map({'a': Sum(2), 'b': Sum(3)})
    map2 = Map({'a': Sum(1), 'b': Sum(2)})
    assert map1.concat(map2) == Map({'a': Sum(3), 'b': Sum(5)})

# Generated at 2022-06-14 03:52:41.811984
# Unit test for method concat of class One
def test_One_concat():
    assert One(True).concat(One(False)).value == True
    assert One(False).concat(One(True)).value == True
    assert One(False).concat(One(False)).value == False


# Generated at 2022-06-14 03:52:44.462634
# Unit test for method __str__ of class Last
def test_Last___str__():
    test = Last(123)
    expected = 'Last[value=123]'
    actual = str(test)
    assert expected == actual


# Generated at 2022-06-14 03:52:46.382213
# Unit test for method __str__ of class Max
def test_Max___str__():
    """ """
    assert str(Max(12)) == 'Max[value=12]'
    return True

# Generated at 2022-06-14 03:52:51.235289
# Unit test for method concat of class Max
def test_Max_concat():
    max_1 = Max(5)
    max_2 = Max(7)
    assert max_1.concat(max_2).value == 7
    assert max_2.concat(max_1).value == 7



# Generated at 2022-06-14 03:52:55.832655
# Unit test for method __str__ of class All
def test_All___str__():
    """ Unit test for method __str__ of class All
    """
    assert str(All(True)) == 'All[value=True]'
    assert str(All(False)) == 'All[value=False]'



# Generated at 2022-06-14 03:52:57.669131
# Unit test for constructor of class First
def test_First():
    first = First(1)
    assert first.value == 1


# Generated at 2022-06-14 03:53:01.009254
# Unit test for method concat of class Sum
def test_Sum_concat():
    assert Sum(1).concat(Sum(4)) == Sum(5)
    assert Sum(42).concat(Sum(5)) == Sum(47)



# Generated at 2022-06-14 03:53:04.604646
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(2).concat(Min(1)).value == 1

test_Min_concat()

# Generated at 2022-06-14 03:53:06.489270
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(1)) == 'Max[value=1]'



# Generated at 2022-06-14 03:53:09.711803
# Unit test for method __str__ of class First
def test_First___str__():  # pragma: no cover
    assert str(First(1)) == 'Fist[value=1]'
    assert str(First(None)) == 'Fist[value=None]'
    assert str(First('monoid')) == 'Fist[value=monoid]'



# Generated at 2022-06-14 03:53:24.761892
# Unit test for constructor of class First
def test_First():
    assert First(10).value == 10

# Generated at 2022-06-14 03:53:29.183723
# Unit test for constructor of class Max
def test_Max():
    assert Max(0).value == 0
    """
    The function test_Max() tests if the value in the Max constructor is properly assigned
    to the value variable by testing a known value.
    """



# Generated at 2022-06-14 03:53:31.435435
# Unit test for method __str__ of class Last
def test_Last___str__():
    # Given
    last = Last(4)
    # Then
    assert str(Last(4)) == 'Last[value=4]'



# Generated at 2022-06-14 03:53:34.336109
# Unit test for constructor of class All
def test_All():
    assert All(True) == All(True)
    assert All(False) == All(False)
    assert All(True) != All(False)



# Generated at 2022-06-14 03:53:37.256946
# Unit test for method concat of class First
def test_First_concat():
    f1, f2, f3 = First(1), First(2), First(3)
    assert f1.concat(f2).concat(f3).value == 1


# Generated at 2022-06-14 03:53:41.388120
# Unit test for method concat of class One
def test_One_concat():
    assert One(1).concat(One(2)).value == 1
    assert One(True).concat(One(False)).value == True
    assert One(False).concat(One(True)).value == True
    assert One(None).concat(One('value')).value == None
    assert One('value').concat(One(None)).value == 'value'


# Generated at 2022-06-14 03:53:49.675416
# Unit test for method concat of class All
def test_All_concat():
    actual = All(True).concat(All(True))
    assert actual.value == True, "All concat failed. Actual: {}".format(actual)

    actual = All(True).concat(All(False))
    assert actual.value == False, "All concat failed. Actual: {}".format(actual)

    actual = All(False).concat(All(True))
    assert actual.value == False, "All concat failed. Actual: {}".format(actual)

    actual = All(False).concat(All(False))
    assert actual.value == False, "All concat failed. Actual: {}".format(actual)


# Generated at 2022-06-14 03:53:53.830683
# Unit test for method concat of class All
def test_All_concat():
    assert All(True).concat(All(True)) == All(True)
    assert All(True).concat(All(False)) == All(False)
    assert All(False).concat(All(False)) == All(False)



# Generated at 2022-06-14 03:53:56.227018
# Unit test for method __str__ of class Last
def test_Last___str__():
    assert str(Last(1)) is 'Last[value=1]'



# Generated at 2022-06-14 03:53:58.429492
# Unit test for method __str__ of class First
def test_First___str__():
    assert str(First('hey')) == "Fist[value=hey]"

