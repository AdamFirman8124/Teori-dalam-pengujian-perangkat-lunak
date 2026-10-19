

# Generated at 2022-06-14 03:44:38.051624
# Unit test for method concat of class Map
def test_Map_concat():
    first_map = Map({
        "foo": Sum(1),
        "bar": All(False)
    })

    second_map = Map({
        "foo": Sum(2),
        "bar": All(True)
    })

    assert first_map.concat(second_map).value["foo"] == Sum(3)
    assert first_map.concat(second_map).value["bar"] == All(False)

# Generated at 2022-06-14 03:44:42.743991
# Unit test for method concat of class Max
def test_Max_concat():
    """
    We can use this function for test method concat for class Max
    """
    a = Max(5)
    b = Max(6)
    assert a.concat(b) == Max(6)


# Generated at 2022-06-14 03:44:48.818732
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(1).concat(Max(2)).value == 2
    assert Max(-1).concat(Max(-2)).value == -1
    assert Max(-2).concat(Max(-1)).value == -1
    assert Max(-1).concat(Max(1)).value == 1
    assert Max(1).concat(Max(-1)).value == 1


# Generated at 2022-06-14 03:44:50.585144
# Unit test for method concat of class Max
def test_Max_concat():
    """
    :returns: None
    :rtype: None
    """
    assert(Max(2).concat(Max(5)).value == Max(5).value)



# Generated at 2022-06-14 03:44:52.003358
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(1).concat(Max(3)).value == 3


# Generated at 2022-06-14 03:44:55.324013
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(3).concat(Max(3)) == Max(3)
    assert Max(3).concat(Max(2)) == Max(3)
    assert Max(2).concat(Max(3)) == Max(3)


# Generated at 2022-06-14 03:44:59.255203
# Unit test for method concat of class Max
def test_Max_concat():  # pragma: no cover
    assert Max(1).concat(Max(6)) == Max(6)
    assert Max(6).concat(Max(1)) == Max(6)


# Generated at 2022-06-14 03:45:02.673352
# Unit test for method concat of class Map
def test_Map_concat():
    assert Map({'A': All(True)}).concat(Map({'A': All(True)})).value == {'A': All(True)}

# Generated at 2022-06-14 03:45:06.196610
# Unit test for method concat of class Max
def test_Max_concat():
    """
    :return: None
    :rtype: None
    """
    assert (Max(8).concat(Max(6)) == Max(8))


# Generated at 2022-06-14 03:45:10.104619
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(2).concat(Max(1)) == Max(2)
    assert Max(1).concat(Max(2)) == Max(2)
    assert Max(2).concat(Max(2)) == Max(2)


# Generated at 2022-06-14 03:45:25.639964
# Unit test for method concat of class Last
def test_Last_concat():
    """
    >>> test_Last_concat()
    True
    """
    assert Last(1).concat(Last(2)) == Last(2)
    assert Last(2).concat(Last(2)) == Last(2)
    assert Last(2).concat(Last(1)) == Last(1)
    assert Last(1).concat(Last(1)) == Last(1)
    assert Last('abc').concat(Last('abc')) == Last('abc')
    assert Last('abc').concat(Last('xyz')) == Last('xyz')
    assert Last(False).concat(Last(False)) == Last(False)
    assert Last(True).concat(Last(True)) == Last(True)
    assert Last(None).concat(Last(None)) == Last(None)

# Generated at 2022-06-14 03:45:27.284229
# Unit test for constructor of class Max
def test_Max():
    assert Max(5).value == 5



# Generated at 2022-06-14 03:45:33.168077
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    assert Sum(1).fold(lambda x: x + 1) == 2
    assert First(1).fold(lambda x: x + 1) == 1
    assert Last(1).fold(lambda x: x + 1) == 1
    assert Min(2).fold(lambda x: x + 1) == 3
    assert Map({'1': Sum(1), '2': Sum(2)}).fold(lambda x: x).value == {'1': Sum(1), '2': Sum(2)}

# Generated at 2022-06-14 03:45:36.151803
# Unit test for constructor of class All
def test_All():
    assert All(True), 'all should be truthy'
    assert All(False), 'all should be falsy'



# Generated at 2022-06-14 03:45:39.016897
# Unit test for constructor of class Min
def test_Min():
    assert Min(1).value == 1
    assert Min(1) == Min(1)
    assert Min(1) != Min(2)



# Generated at 2022-06-14 03:45:42.595890
# Unit test for method concat of class First
def test_First_concat():
    assert First().concat(First(123)).value == 123
    assert First(321).concat(First()).value == 321
    assert First(321).concat(First(123)).value == 321
    assert First(321).concat(First(123)).value == 321



# Generated at 2022-06-14 03:45:44.173065
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    result = Sum(1).fold(lambda x: x + 1)
    assert result == 2

# Generated at 2022-06-14 03:45:53.185694
# Unit test for method concat of class Map
def test_Map_concat():
    assert Map({1: Sum(1), 2: First("hello")}).concat(
        Map({1: Sum(1), 2: First("World")})
    ) == Map({1: Sum(2), 2: First("hello")})
    assert Map({"a": All(True), "b": First("hello")}).concat(
        Map({"a": All(False), "b": First("World")})
    ) == Map({"a": All(True), "b": First("hello")})
    assert Map({"a": All(True), "b": First("hello")}).concat(
        Map({"a": All(False), "b": First("World"), "c": First("Hello")})
    ) == Map({"a": All(True), "b": First("hello"), "c": First("Hello")})

# Generated at 2022-06-14 03:46:04.467960
# Unit test for constructor of class All
def test_All():
    assert All(True).value == True
    assert All(False).value == False
    assert All("True").value == "True"
    assert All("False").value == "False"
    assert All("").value == ""
    assert All(" ").value == " "
    assert All("Hello").value == "Hello"
    assert All(" How are you?").value == " How are you?"
    assert All([]).value == []
    assert All([""]).value == [""]
    assert All(["True"]).value == ["True"]
    assert All(["Hello"]).value == ["Hello"]
    assert All([" How are you?"]).value == [" How are you?"]
    assert All({}).value == {}
    assert All({"": ""}).value == {"": ""}

# Generated at 2022-06-14 03:46:05.915902
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(3)) == 'Max[value=3]'


# Generated at 2022-06-14 03:46:11.694668
# Unit test for constructor of class Last
def test_Last():
    class_last = Last(1)
    assert isinstance(class_last, Last) is True


# Generated at 2022-06-14 03:46:15.170838
# Unit test for method __str__ of class Map
def test_Map___str__():
    # Arrange
    m = Map({1: Sum(1)})
    # Act
    result = m.__str__()
    # Assert
    assert result == 'Map[value={1: Sum[value=1]}]'


# Generated at 2022-06-14 03:46:17.753727
# Unit test for method __str__ of class Min
def test_Min___str__():
    """
    :returns: a test Min
    :rtype: Min[Any]
    """
    min = Min(9)
    assert min.__str__() == "Min[value=9]"



# Generated at 2022-06-14 03:46:19.564511
# Unit test for method concat of class Last
def test_Last_concat():
    assert Last(2).concat(Last(3)).value == 3



# Generated at 2022-06-14 03:46:21.964589
# Unit test for constructor of class Last
def test_Last():  # pragma: no cover
    last = Last(4)
    assert last.value == 4


# Generated at 2022-06-14 03:46:24.269472
# Unit test for constructor of class All
def test_All():
    assert All(True) == All(True)
    assert All(False) != All(True)



# Generated at 2022-06-14 03:46:26.255105
# Unit test for constructor of class Last
def test_Last():
    last = Last(2)
    assert last.value == 2
    assert last.fold(lambda x: x) == 2


# Generated at 2022-06-14 03:46:28.061308
# Unit test for constructor of class All
def test_All():
    assert All(True).value == True
    assert All(False).value == False


# Generated at 2022-06-14 03:46:31.753828
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    assert Sum(1).fold(lambda x: 2 * x) == 2
    assert Sum(5).fold(lambda x: 2 * x) == 10
    assert All(True).fold(lambda x: bool(x)) is True
    assert All(False).fold(lambda x: bool(x)) is False
    assert Last("a").fold(lambda x: x.upper()) == "A"
    assert Last("b").fold(lambda x: x.upper()) == "B"
    assert Map({1: Sum(1), 2: Sum(2)}).fold(lambda x: x[1].value) == 3


# Generated at 2022-06-14 03:46:33.546201
# Unit test for method __str__ of class Sum
def test_Sum___str__():  # pragma: no cover
    assert str(Sum(5)) == "Sum[value=5]"



# Generated at 2022-06-14 03:46:42.519794
# Unit test for constructor of class All
def test_All():
    assert All(True).concat(All(True)) == All(True)
    assert All(True).concat(All(False)) == All(False)
    assert All(False).concat(All(True)) == All(False)
    assert All(False).concat(All(False)) == All(False)


# Generated at 2022-06-14 03:46:47.403816
# Unit test for method concat of class Map
def test_Map_concat():
    assert Map({"a": Sum(1), "b": Sum(2)}).concat(Map({"a": Sum(2), "b": Sum(3)})) == Map({"a": Sum(3), "b": Sum(5)})

# Generated at 2022-06-14 03:46:54.851131
# Unit test for constructor of class First
def test_First():
    first = First(1)
    assert first.value == 1, 'This is not a first'
    first = First(0)
    assert first.value == 0, 'This is not a first'
    first = First(True)
    assert first.value == True, 'This is not a first'
    first = First(False)
    assert first.value == False, 'This is not a first'
    first = First("string")
    assert first.value == "string", 'This is not a first'

# Generated at 2022-06-14 03:46:56.759872
# Unit test for method concat of class Sum
def test_Sum_concat():
    assert Sum(1).concat(Sum(2)) == Sum(3)


# Generated at 2022-06-14 03:46:58.685087
# Unit test for constructor of class Sum
def test_Sum():
    assert Sum(1) == Sum(1)
    assert Sum(1) != Sum(2)


# Generated at 2022-06-14 03:47:01.206245
# Unit test for method concat of class Last
def test_Last_concat():
    assert Last(1).concat(Last(2)) == Last(2)
    assert Last(1).concat(Last(3)) == Last(3)



# Generated at 2022-06-14 03:47:03.947753
# Unit test for constructor of class First
def test_First():
    assert First("Hello") == First("Hello")
# test fold

# Generated at 2022-06-14 03:47:07.234923
# Unit test for method concat of class Min
def test_Min_concat():
    m1 = Min(4)
    m2 = Min(6)
    m3 = m1.concat(m2)
    assert m3.value == 4


# Generated at 2022-06-14 03:47:11.339476
# Unit test for method concat of class Map
def test_Map_concat():
    assert_equal(
        Map({"a": Sum(1), "b": Sum(2)}).concat(Map({"a": Sum(3), "b": Sum(4)})),
        Map({"a": Sum(4), "b": Sum(6)})
    )


# Generated at 2022-06-14 03:47:12.812906
# Unit test for constructor of class First
def test_First():
    test_semigroup = First(5)
    assert test_semigroup.value == 5


# Generated at 2022-06-14 03:47:17.677970
# Unit test for method __str__ of class Min
def test_Min___str__():
    assert Min("a").__str__() == "Min[value=a]"
    assert Min("a").__str__() == """Min[value=a]"""


# Generated at 2022-06-14 03:47:24.134945
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    assert Sum(1) == Sum(1)
    assert All(True) == All(True)
    assert One(True) == One(True)
    assert First(1) == First(1)
    assert Last(2) == Last(2)
    assert Map({'a': Sum(1)}) == Map({'a': Sum(1)})
    assert Max(1) == Max(1)
    assert Min(1) == Min(1)



# Generated at 2022-06-14 03:47:27.793749
# Unit test for constructor of class Sum
def test_Sum():  # pragma: no cover
    assert Sum(1).value == 1


# Generated at 2022-06-14 03:47:30.972546
# Unit test for method __str__ of class One
def test_One___str__():  # pragma: no cover
    assert str(One(True)) == 'One[value=True]'
    assert str(One(False)) == 'One[value=False]'


# Generated at 2022-06-14 03:47:32.350325
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(123)) == 'Max[value=123]'


# Generated at 2022-06-14 03:47:37.023831
# Unit test for method __str__ of class First
def test_First___str__():
    assert str(First(True)) == "Fist[value=True]"
    assert str(First("hello")) == "Fist[value=hello]"
    assert str(First("hello")) == "Fist[value=hello]"



# Generated at 2022-06-14 03:47:39.477330
# Unit test for method concat of class First
def test_First_concat():
    left = First('a')
    right = First('b')
    expected = First('a')
    actual = left.concat(right)
    assert actual == expected



# Generated at 2022-06-14 03:47:44.023990
# Unit test for constructor of class One
def test_One():
    assert One(True) == One(True)
    assert One(False) == One(False)
    assert One('value') == One('value')
    assert One([1, 2, 3]) == One([1, 2, 3])



# Generated at 2022-06-14 03:47:49.320280
# Unit test for constructor of class Map
def test_Map():
    assert Map({"a": Last(1), "b": Last(2)}).concat(
        Map({"a": Last(3), "b": Last(4)})
    ).value == {"a": Last(3), "b": Last(4)}

# Generated at 2022-06-14 03:47:51.338197
# Unit test for constructor of class First
def test_First():  # pragma: no cover
    f = First(1)
    assert f.value == 1


# Generated at 2022-06-14 03:47:59.550739
# Unit test for method concat of class One
def test_One_concat():
    assert One(True).concat(One(True)) == One(True)
    assert One(True).concat(One(False)) == One(True)
    assert One(False).concat(One(True)) == One(True)
    assert One(False).concat(One(False)) == One(False)


# Generated at 2022-06-14 03:48:01.429603
# Unit test for constructor of class Sum
def test_Sum():
    assert Sum(1) == Sum(1)
    assert Sum(1).value == 1
    assert str(Sum(1)) == 'Sum[value=1]'



# Generated at 2022-06-14 03:48:04.115683
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert Max(3).__str__() == 'Max[value=3]'



# Generated at 2022-06-14 03:48:05.975477
# Unit test for constructor of class Sum
def test_Sum():
    sum = Sum(1)
    assert sum.value == 1


# Generated at 2022-06-14 03:48:07.634873
# Unit test for method __str__ of class First
def test_First___str__():
    assert str(First(1)) == 'Fist[value=1]'



# Generated at 2022-06-14 03:48:09.232786
# Unit test for method __str__ of class All
def test_All___str__():
    assert str(All(True)) == 'All[value=True]'


# Generated at 2022-06-14 03:48:14.874470
# Unit test for method concat of class Sum
def test_Sum_concat():
    assert Sum(1).concat(Sum(2)) == Sum(3)
    assert Sum(2).concat(Sum(-1)) == Sum(1)
    assert Sum(1).concat(Sum(3)) == Sum(4)
    assert Sum(-2).concat(Sum(-1)) == Sum(-3)


# Generated at 2022-06-14 03:48:19.630187
# Unit test for method concat of class Last
def test_Last_concat():
    assert str(Last(10).concat(Last(20))) == "Last[value=20]"
    assert str(Last(10).concat(Last(0))) == "Last[value=0]"
    assert str(Last(10).concat(Last(10))) == "Last[value=10]"


# Generated at 2022-06-14 03:48:24.157086
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(0).concat(Min(1)).value == 0
    assert Min(2).concat(Min(1)).value == 1
    assert Min(1).concat(Min(1)).value == 1


# Generated at 2022-06-14 03:48:25.872712
# Unit test for method concat of class Last
def test_Last_concat():
    assert Last(1).concat(Last(4)) == Last(4)


# Generated at 2022-06-14 03:48:32.652581
# Unit test for constructor of class First
def test_First():
    w = First(3)

    @Kleisli(First.fold, w)
    def fn(xs):
        return xs ** 2

    assert w.concat(Last(4)).value == 3
    assert w.fold(fn).value == 9

# Generated at 2022-06-14 03:48:34.423964
# Unit test for method __str__ of class All
def test_All___str__():
    assert 'All[value=True]' == str(All(True))


# Generated at 2022-06-14 03:48:35.993417
# Unit test for constructor of class Sum
def test_Sum():
    assert Sum(10) == Sum(10)
    assert Sum(10) != Sum(15)


# Generated at 2022-06-14 03:48:40.777889
# Unit test for constructor of class All
def test_All():
    a = All(True)
    assert a.value == True
    assert str(a) == 'All[value=True]'



# Generated at 2022-06-14 03:48:45.566090
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    assert Sum(1) == Sum(1)
    assert All(True) == All(True)
    assert One(False) == One(False)
    assert First(1) == First(1)
    assert Last(1) == Last(1)
    assert Max(1) == Max(1)
    assert Min(1) == Min(1)


# Generated at 2022-06-14 03:48:47.479117
# Unit test for method __str__ of class All
def test_All___str__():
    assert 'All[value=False]' == str(All(False))



# Generated at 2022-06-14 03:48:58.508738
# Unit test for method concat of class Min
def test_Min_concat():
    minus_infinity = Min(-float("inf"))
    m1 = Min(-100)
    m2 = Min(-50)
    m3 = Min(-5)
    zero = Min(0)
    p1 = Min(5)
    p2 = Min(50)
    p3 = Min(100)
    infinity = Min(float("inf"))

    assert minus_infinity.concat(minus_infinity) == Min(-float("inf"))
    assert minus_infinity.concat(m1) == Min(-float("inf"))
    assert minus_infinity.concat(m2) == Min(-float("inf"))
    assert minus_infinity.concat(m3) == Min(-float("inf"))
    assert minus_infinity.concat(zero) == Min(-float("inf"))
    assert minus_infinity.con

# Generated at 2022-06-14 03:49:01.221597
# Unit test for method __str__ of class All
def test_All___str__():
    assert All(True).__str__() == "All[value=True]"
    assert All(False).__str__() == "All[value=False]"


# Generated at 2022-06-14 03:49:04.309889
# Unit test for method concat of class Min
def test_Min_concat():
    a = Min(1)
    b = Min(2)
    assert a.concat(b) == Min(1)


# Generated at 2022-06-14 03:49:11.568862
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    assert Sum(1) == Sum(1)
    assert Sum(1) != Sum(2)
    assert Sum(2) != Sum(1)
    assert All(True) == All(True)
    assert All(True) != All(False)
    assert All(False) != All(True)
    assert One(True) == One(True)
    assert One(True) != One(False)
    assert One(False) != One(True)
    assert First(1) == First(1)
    assert First(1) != First(2)
    assert First(2) != First(1)
    assert Last(1) == Last(1)
    assert Last(1) != Last(2)
    assert Last(2) != Last(1)
    assert Max(1) == Max(1)

# Generated at 2022-06-14 03:49:19.748642
# Unit test for method __str__ of class Last
def test_Last___str__():
    assert str(Last(1)) == 'Last[value=1]'


# Generated at 2022-06-14 03:49:20.761647
# Unit test for constructor of class Min
def test_Min():
    assert Min(1).value == 1



# Generated at 2022-06-14 03:49:25.317209
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    one = Min(1)
    one_1 = Min(1)
    two = Min(2)

    assert one == one
    assert one == one_1
    assert one != two
    assert not (one == two)


# Generated at 2022-06-14 03:49:26.917984
# Unit test for method __str__ of class First
def test_First___str__():
    assert str(First(1)) == 'Fist[value=1]'


# Generated at 2022-06-14 03:49:35.260155
# Unit test for constructor of class Min
def test_Min():
    assert Min(1) == Min(1)
    assert Min(1) != Min(2)
    assert Min(1).concat(Min(2)) == Min(2)
    assert Min(2).concat(Min(1)) == Min(1)
    assert Min.neutral().concat(Min(1)) == Min(1)
    assert Min(1).concat(Min.neutral()) == Min(1)
    assert Min(1).fold(lambda x: x * 2) == 2
    assert Min(2).fold(lambda x: x * 2) == 4


# Generated at 2022-06-14 03:49:39.247895
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(5).concat(Min(3)).value == 3
    assert Min(5).concat(Min(5)).value == 5
    assert Min(5).concat(Min(7)).value == 5



# Generated at 2022-06-14 03:49:41.016233
# Unit test for method __str__ of class First
def test_First___str__():
    assert str(First("dummy value")) == "Fist[value=dummy value]"



# Generated at 2022-06-14 03:49:44.483894
# Unit test for method concat of class One
def test_One_concat():
    assert One(True).concat(One(False)) == One(True)
    assert One(False).concat(One(False)) == One(False)
    assert One(False).concat(One(True)) == One(True)
    assert One(True).concat(One(True)) == One(True)


# Generated at 2022-06-14 03:49:47.220425
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    sum = Sum(99)
    assert str(sum) == "Sum[value=99]"


# Generated at 2022-06-14 03:49:50.165833
# Unit test for method concat of class Last
def test_Last_concat():
    last = Last(1)
    last_two = Last(2)
    assert last.concat(last_two) == last_two
    assert last_two.concat(last) == last_two


# Generated at 2022-06-14 03:50:06.231341
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    """Method __eq__ of class Semigroup is tested.
    """

    assert Sum(1) == Sum(1)
    assert All(False) == All(False)
    assert One(True) == One(True)
    assert First(1) == First(1)
    assert Last(1) == Last(1)
    assert Map({'test': 1}) == Map({'test': 1})
    assert Max(1) == Max(1)
    assert Min(1) == Min(1)


# Generated at 2022-06-14 03:50:07.864709
# Unit test for method __str__ of class First
def test_First___str__():
    assert str(First(7)) == "Fist[value=7]"

# Generated at 2022-06-14 03:50:10.123360
# Unit test for method __str__ of class First
def test_First___str__():  # pragma: no cover
    assert str(First(1)) == 'Fist[value=1]'


# Generated at 2022-06-14 03:50:12.174390
# Unit test for constructor of class Last
def test_Last():
    last = Last(2)
    assert last.value == 2


# Generated at 2022-06-14 03:50:13.667510
# Unit test for method concat of class Last
def test_Last_concat():
    assert Last(10).concat(Last(20)).value == 20



# Generated at 2022-06-14 03:50:21.088125
# Unit test for method concat of class One
def test_One_concat():
    assert One(True).concat(One(True)).concat(One(False)) == One(False)
    assert One(True).concat(One(False)).concat(One(True)) == One(True)
    assert One(True).concat(One(True)).concat(One(True)) == One(True)
    assert One(False).concat(One(False)).concat(One(False)) == One(False)


# Generated at 2022-06-14 03:50:26.708678
# Unit test for method concat of class One
def test_One_concat():
    assert One(True).concat(One(True)).value is True
    assert One(True).concat(One(False)).value is True
    assert One(False).concat(One(True)).value is True
    assert One(False).concat(One(False)).value is False


# Generated at 2022-06-14 03:50:31.496317
# Unit test for method concat of class Min
def test_Min_concat():
    a = Min(1)
    b = Min(2)
    assert a.concat(b) == Min(1)
    assert b.concat(a) == Min(1)
    assert a.concat(a) == Min(1)
    assert b.concat(b) == Min(2)



# Generated at 2022-06-14 03:50:36.156278
# Unit test for constructor of class First
def test_First():
    assert First(1) == First(1)
    assert First(2) != First(1)
    assert First(2).value == 2
    assert First(1) == First(2).concat(First(1))


# Generated at 2022-06-14 03:50:38.750184
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    sum = Sum(1)
    assert str(sum) == 'Sum[value=1]'


# Generated at 2022-06-14 03:50:47.416192
# Unit test for method __str__ of class First
def test_First___str__():
    assert str(First(1)) == 'Fist[value=1]'


# Generated at 2022-06-14 03:50:53.351997
# Unit test for method concat of class All
def test_All_concat():
    assert All(True).concat(All(True)).value == True
    assert All(True).concat(All(False)).value == False
    assert All(False).concat(All(True)).value == False
    assert All(False).concat(All(False)).value == False


# Generated at 2022-06-14 03:50:54.907550
# Unit test for method __str__ of class All
def test_All___str__():
    assert str(All(True)) == "All[value=True]"


# Generated at 2022-06-14 03:50:58.465157
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    assert str(Sum(1)) == 'Sum[value=1]'
    assert str(Sum(0)) == 'Sum[value=0]'
    assert str(Sum(-1)) == 'Sum[value=-1]'


# Generated at 2022-06-14 03:51:00.821991
# Unit test for method concat of class First
def test_First_concat():
    first = First(3)
    semigroup = First(2)
    concated_first = first.concat(semigroup)
    assert concated_first.value == 3


# Generated at 2022-06-14 03:51:03.489177
# Unit test for method concat of class Max
def test_Max_concat():
    """
    Test Sum concat method
    """
    assert Max(0).concat(Max(1)) == Max(1)
    assert Max(1).concat(Max(0)) == Max(1)
    assert Max(-1).concat(Max(-1)) == Max(-1)


# Generated at 2022-06-14 03:51:09.847692
# Unit test for constructor of class Map
def test_Map():
    list = [1, 2, 3, 4, 5]
    map1 = Map({1: Max(1), 2: Sum(2), 3: All(False)})
    map2 = Map({1: Max(2), 2: Sum(3), 3: All(True)})
    map3 = map1.concat(map2)
    print(map3) # Map[value={1: Max[value=2], 2: Sum[value=5], 3: All[value=False]}]

# Generated at 2022-06-14 03:51:20.148201
# Unit test for method concat of class One
def test_One_concat():
    result = One(True).concat(One(False))
    assert result == One(True)

    result = One(False).concat(One(False))
    assert result == One(False)

    result = One(True).concat(One(True))
    assert result == One(True)

    result = One(False).concat(One(False))
    assert result == One(False)

    result = One(True).concat(One(False))
    assert result == One(True)

    result = One(False).concat(One(True))
    assert result == One(True)


# Generated at 2022-06-14 03:51:26.559329
# Unit test for method __str__ of class Last
def test_Last___str__():
    assert str(Last(10)) == 'Last[value=10]'
    assert str(Last(2)) == 'Last[value=2]'
    assert str(Last(0)) == 'Last[value=0]'
    assert str(Last(-1)) == 'Last[value=-1]'


# Generated at 2022-06-14 03:51:28.903720
# Unit test for constructor of class One
def test_One():
    # Arrange
    value = False
    expected = One(value)

    # Action
    actual = One(value)

    # Assert
    assert actual == expected


# Generated at 2022-06-14 03:51:45.512197
# Unit test for method concat of class Sum
def test_Sum_concat():
    sum_a = Sum(1)
    sum_b = Sum(2)
    expect = 3
    result = sum_a.concat(sum_b)
    assert result == expect


# Generated at 2022-06-14 03:51:47.432539
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(2)) == 'Max[value=2]'



# Generated at 2022-06-14 03:51:55.573152
# Unit test for constructor of class Map
def test_Map():
    m = Map({"a": Sum(1), "b": Min(2), "c": Max(3)})

    assert m.value == {"a": Sum(1), "b": Min(2), "c": Max(3)}
    assert m.value != {"b": Min(2), "c": Max(3), "a": Sum(1)}
    assert m.value != {"b": Sum(2), "c": Max(3), "a": Min(1)}
    assert m.value != {"b": Sum(2), "c": Min(3), "a": Max(1)}


# Generated at 2022-06-14 03:52:03.621421
# Unit test for constructor of class Min
def test_Min():
    min1 = Min(1)
    min2 = Min(2)
    min3 = min1.concat(min2)
    assert min3.value == 1
    min1 = Min(1)
    min4 = Min(4)
    min5 = Min(5)
    min6 = Min(6)
    assert min1.concat(min4.concat(min5)).concat(min6).value == 1

test_Min()


# Generated at 2022-06-14 03:52:07.475210
# Unit test for method concat of class Map
def test_Map_concat():
    m1 = Map({'k1': Sum(1), 'k2': Sum(2)})
    m2 = Map({'k1': Sum(2), 'k2': Sum(3)})
    m3 = m1.concat(m2)
    assert m3 == Map({'k1': Sum(3), 'k2': Sum(5)})

# Generated at 2022-06-14 03:52:10.299076
# Unit test for method __str__ of class Last
def test_Last___str__():  # pragma: no cover
    assert Last(4.5).__str__() == 'Last[value=4.5]'


# Generated at 2022-06-14 03:52:20.525896
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    assert str(Sum(1)) == 'Sum[value=1]'
    assert str(Sum(-1)) == 'Sum[value=-1]'
    assert str(Sum(0)) == 'Sum[value=0]'
    assert str(Sum(0.34)) == 'Sum[value=0.34]'
    assert str(Sum(str('str'))) == 'Sum[value=str]'
    assert str(Sum(None)) == 'Sum[value=None]'
    assert str(Sum(float('inf'))) == 'Sum[value=inf]'
    assert str(Sum(float('nan'))) == 'Sum[value=nan]'



# Generated at 2022-06-14 03:52:24.931993
# Unit test for method concat of class Max
def test_Max_concat():
    assert(Max(3).concat(Max(1)) == Max(3))
    assert(Max(1).concat(Max(3)) == Max(3))
    assert(Max(2).concat(Max(4)) == Max(4))


# Generated at 2022-06-14 03:52:26.585384
# Unit test for method __str__ of class First
def test_First___str__():
    assert (str(First(1)) == "Fist[value=1]")



# Generated at 2022-06-14 03:52:27.966127
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    assert str(Sum(10)) == "Sum[value=10]"


# Generated at 2022-06-14 03:53:01.254692
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(1)) == 'Max[value=1]'


# Generated at 2022-06-14 03:53:07.077867
# Unit test for method __str__ of class Map
def test_Map___str__():
    assert str(Map({'a': Sum(1), 'b': First('value')})) == (
        "Map[value={'a': Sum[value=1], 'b': Fist[value=value]}]"
    )


# Generated at 2022-06-14 03:53:11.472476
# Unit test for method concat of class Sum
def test_Sum_concat():
    sum_1 = Sum(1)
    sum_2 = Sum(2)
    assert sum_1.concat(sum_2).value == 3
    assert Sum(3).concat(Sum(4)).value == 7
    assert Sum(4).concat(Sum(4)).value == 8


# Generated at 2022-06-14 03:53:14.573366
# Unit test for method concat of class Sum
def test_Sum_concat():
    result = Sum(2).concat(Sum(1))
    assert result.value == 3, result



# Generated at 2022-06-14 03:53:17.820431
# Unit test for method __str__ of class Map
def test_Map___str__():
    m = Map({1: Sum(1)})
    assert str(m) == "Map[value={1: Sum[value=1]}]"



# Generated at 2022-06-14 03:53:19.805524
# Unit test for constructor of class Last
def test_Last():
    actual = Last(4)
    expected = Last(4)
    assert actual == expected


# Generated at 2022-06-14 03:53:25.326148
# Unit test for method concat of class Map
def test_Map_concat():
    val_1 = {
        1: Sum(1),
        2: Sum(2)
    }
    val_2 = {
        1: Sum(1),
        2: Sum(3)
    }

    assert Map(val_1).concat(Map(val_2)).value == {
        1: Sum(2),
        2: Sum(5)
    }

test_Map_concat()

# Generated at 2022-06-14 03:53:31.384501
# Unit test for constructor of class Last
def test_Last():
    assert Last(0).value == 0
    assert Last(1).value == 1
    assert Last(1).concat(Last(0)).value == 0
    assert Last(0).concat(Last(1)).value == 1
    assert str(Last(0).concat(Last(1))) == 'Last[value=1]'



# Generated at 2022-06-14 03:53:36.286566
# Unit test for method __str__ of class Sum
def test_Sum___str__():  # pragma: no cover
    """
    Unit test for method __str__ of class Sum
    """
    assert str(Sum(1)) == 'Sum[value=1]'
    assert str(Sum(2)) == 'Sum[value=2]'
    assert str(Sum(3)) == 'Sum[value=3]'



# Generated at 2022-06-14 03:53:39.161369
# Unit test for method __str__ of class Map
def test_Map___str__():
    """
    Unit test for method __str__ of class Map
    """

    # When
    new_Map = Map({})

    # Then
    assert new_Map.__str__() == 'Map[value={}]'

