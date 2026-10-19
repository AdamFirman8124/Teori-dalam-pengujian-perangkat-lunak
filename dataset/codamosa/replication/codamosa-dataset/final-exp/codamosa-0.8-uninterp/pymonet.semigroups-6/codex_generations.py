

# Generated at 2022-06-14 03:44:34.176653
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(-1).concat(Min(2)) == Min(-1)
    assert Min(2).concat(Min(3)) == Min(2)


# Generated at 2022-06-14 03:44:36.163988
# Unit test for method concat of class Max
def test_Max_concat():
    a = Max(1)
    b = Max(2)
    c = a.concat(b)
    d = c.concat(a)
    assert b == c
    assert c == d

# Generated at 2022-06-14 03:44:38.515953
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(2).concat(Max(3)) == Max(3)
    assert Max(3).concat(Max(2)) == Max(3)


# Generated at 2022-06-14 03:44:41.180282
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(2).concat(Max(7)) == Max(7)
    assert Max(8).concat(Max(1)) == Max(8)
    assert Max(8).concat(Max(8)) == Max(8)

# Generated at 2022-06-14 03:44:45.152047
# Unit test for method concat of class Min
def test_Min_concat():
    semigroup1 = Min(-5)
    semigroup2 = Min(-4)
    assert semigroup1.concat(semigroup2).value == -5


# Generated at 2022-06-14 03:44:50.799697
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(3).concat(Min(1)) == Min(1)
    assert Min(4).concat(Min(4)) == Min(4)
    assert Min(4).concat(Min(1)) == Min(1)
    assert Min(4).concat(Min(5)) == Min(4)


# Generated at 2022-06-14 03:44:54.076324
# Unit test for method concat of class Min
def test_Min_concat():
    min_inst = Min(4).concat(Min(5))
    assert min_inst.concat(Min(10)).concat(Min(2)).concat(Min(30)).concat(Min(1)) == Min(1)


# Generated at 2022-06-14 03:44:58.543569
# Unit test for method concat of class Min
def test_Min_concat():
    sg1 = Min(1)
    sg2 = Min(2)
    assert sg1.concat(sg2) == Min(1)
    assert sg2.concat(sg1) == Min(1)
    assert sg1.concat(sg1) == Min(1)
    assert sg2.concat(sg2) == Min(2)


# Generated at 2022-06-14 03:45:00.553531
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(1).concat(Min(2)) == Min(1)


# Generated at 2022-06-14 03:45:08.566281
# Unit test for method concat of class Min
def test_Min_concat():
    """
    from pymonad.Monoid import Min
    import pytest
    from hypothesis import given
    from hypothesis.strategies import integers

    @given(integers(min_value=Min.neutral_element), integers(max_value=Min.neutral_element))
    def test_m_m(a, b):
        assert(Min(a).concat(Min(b)).value == b)
    """
    pass



# Generated at 2022-06-14 03:45:13.645769
# Unit test for constructor of class One
def test_One():  # pragma: no cover
    assert str(One(True)) == 'One[value=True]'
    assert One(True).concat(One(False)) == One(True)


# Generated at 2022-06-14 03:45:15.509977
# Unit test for constructor of class All
def test_All():
    """
    :returns: Passing true
    :rtype: bool
    """
    assert All(1).value == True
    return True


# Generated at 2022-06-14 03:45:16.723866
# Unit test for method __str__ of class Last
def test_Last___str__():
    assert str(Last(1)) == 'Last[value=1]'
    assert str(Last(None)) == 'Last[value=None]'


# Generated at 2022-06-14 03:45:18.553539
# Unit test for method __str__ of class One
def test_One___str__():
    obj = One(1)
    assert(str(obj) == 'One[value=1]')


# Generated at 2022-06-14 03:45:20.460793
# Unit test for constructor of class Semigroup
def test_Semigroup():  # pragma: no cover
    Semigroup(value=10)

# Generated at 2022-06-14 03:45:26.305154
# Unit test for method concat of class All
def test_All_concat():  # pragma: no cover
    a = All(True)
    assert a.concat(a) == All(True)
    assert a.concat(All(False)) == All(False)
    assert All(False).concat(All(True)) == All(False)
    assert All(False).concat(All(False)) == All(False)



# Generated at 2022-06-14 03:45:28.176266
# Unit test for method __str__ of class Max
def test_Max___str__():  # pragma: no cover
    assert str(Max(2)) == 'Max[value=2]'


# Generated at 2022-06-14 03:45:30.271601
# Unit test for constructor of class Map
def test_Map():
    assert Map({'a': Sum(1)}) == Map({'a': Sum(1)})
    assert Map({'a': Sum(1)}) != Map({'a': Sum(2)})
    assert Map({'a': Sum(1)}) != Sum(1)

# Generated at 2022-06-14 03:45:31.518192
# Unit test for method __str__ of class First
def test_First___str__():
    assert str(First(1)) == 'Fist[value=1]'



# Generated at 2022-06-14 03:45:40.197659
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    s = Sum(10)
    assert s.fold(lambda x: x + 2) == 12
    assert s.fold(lambda x: x - 2) == 8

    s = All(True)
    assert s.fold(lambda x: not x) == False

    s = One(True)
    assert s.fold(lambda x: not x) == True

    s = First(True)
    assert s.fold(lambda x: not x)

    s = Last(True)
    assert s.fold(lambda x: not x)

    s = Map({'first': First(True), 'last': Last(True)})
    s = s.fold(lambda x: not x)

    s = Max(1)
    assert s.fold(lambda x: x + 5) == 6

    s = Min(0)

# Generated at 2022-06-14 03:45:45.858071
# Unit test for method __str__ of class Last
def test_Last___str__():
    assert "Last[value=1]" == str(Last(1))



# Generated at 2022-06-14 03:45:47.921322
# Unit test for method concat of class Sum
def test_Sum_concat():
    assert Sum(1).concat(Sum(2)) == Sum(3)



# Generated at 2022-06-14 03:45:51.292587
# Unit test for method __str__ of class Min
def test_Min___str__():
    cases = [
        {"input": Min(99), "expected": "Min[value=99]"},
        {"input": Min(0), "expected": "Min[value=0]"}
    ]
    for case in cases:
        assert str(case["input"]) == case["expected"]


# Generated at 2022-06-14 03:45:59.235675
# Unit test for constructor of class Max
def test_Max():
    assert Max(5) == Max(5)
    assert Max(5).value == 5
    assert Max(5).fold(lambda x: x) == 5
    assert Max(5).concat(Max(4)) == Max(5)
    assert Max(4).concat(Max(5)) == Max(5)
    assert Max(5).concat(Max.neutral()) == Max(5)
    assert Max.neutral().concat(Max(5)) == Max(5)
    assert Max.neutral() == Max(-float("inf"))


# Generated at 2022-06-14 03:46:03.846472
# Unit test for method concat of class One
def test_One_concat():
    assert One(True).concat(One(False)) == One(True)
    assert One(False).concat(One(True)) == One(True)
    assert One(False).concat(One(False)) == One(False)


# Generated at 2022-06-14 03:46:06.059481
# Unit test for constructor of class One
def test_One():
    assert One(True).value == True
    assert One(False).value == False
    assert One(0).value == False


# Generated at 2022-06-14 03:46:08.393953
# Unit test for method __str__ of class Map
def test_Map___str__():
    assert str(Map({"a": Min(3)})) == "Map[value={'a': Min[value=3]}]"



# Generated at 2022-06-14 03:46:14.524536
# Unit test for method concat of class All
def test_All_concat():
    assert All(True).concat(All(True)) == All(True)
    assert All(True).concat(All(False)) == All(False)
    assert All(False).concat(All(True)) == All(False)
    assert All(False).concat(All(False)) == All(False)



# Generated at 2022-06-14 03:46:16.831322
# Unit test for constructor of class Sum
def test_Sum():
    assert Sum(1).value == 1
    assert str(Sum(1)) == 'Sum[value=1]'
    assert Sum(1) == Sum(1)


# Generated at 2022-06-14 03:46:21.724299
# Unit test for constructor of class Semigroup
def test_Semigroup():
    # pylint: disable=no-member
    store = Semigroup(0)
    assert store.value == 0
    store = Semigroup(1)
    assert store.value == 1
    store = Semigroup(3.14159265359)
    assert store.value == 3.14159265359
    store = Semigroup(True)
    assert store.value == True
    store = Semigroup(False)
    assert store.value == False


# Generated at 2022-06-14 03:46:30.555677
# Unit test for method __str__ of class Last
def test_Last___str__():
    assert str(Last(1)) == 'Last[value=1]'


# Generated at 2022-06-14 03:46:31.886333
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(10)) == 'Max[value=10]'



# Generated at 2022-06-14 03:46:33.130653
# Unit test for constructor of class Min
def test_Min():
    assert Min(0) == Min(-5)
    assert Min(-5) < Min(-4)
    assert Min(-4) < Min(-4)


# Generated at 2022-06-14 03:46:33.992284
# Unit test for method __str__ of class One
def test_One___str__(): # pragma: no cover
    assert str(One(True)) == 'One[value=True]'


# Generated at 2022-06-14 03:46:38.086938
# Unit test for constructor of class One
def test_One():  # pragma: no cover
    one1 = One(True)
    assert one1.value == True

    one2 = One(False)
    assert one2.value == False

    one3 = One(None)
    assert one3.value is None


# Generated at 2022-06-14 03:46:47.202340
# Unit test for constructor of class Last
def test_Last():  # pragma: no cover
    assert Last(0) == Last(0)
    assert Last(1) != Last(0)
    assert Last(0) != All(0)
    assert Last(0) != One(0)
    assert Last(0) != First(0)
    assert Last(0) != Max(0)
    assert Last(0) != Min(0)
    assert Last(0) != Sum(0)
    assert Last(0) != Map(0)



# Generated at 2022-06-14 03:46:55.286969
# Unit test for constructor of class One
def test_One():
    assert One(False) == One(False)
    assert One(True) == One(True)
    assert One(False) != One(True)

    assert One(0) == One(0)
    assert One(-1) == One(-1)
    assert One(1) == One(1)
    assert One(0) != One(1)

    assert One([]) == One([])
    assert One(['a']) == One(['a'])
    assert One(['a', 'b']) == One(['a', 'b'])
    assert One([]) != One(['a'])

    assert One({}) == One({})
    assert One({'a': 1}) == One({'a': 1})

# Generated at 2022-06-14 03:46:57.649862
# Unit test for method __str__ of class All
def test_All___str__():
    assert str(All(True)) == 'All[value=True]'
    assert str(All(False)) == 'All[value=False]'



# Generated at 2022-06-14 03:47:00.461702
# Unit test for method concat of class First
def test_First_concat():
    assert First(20).concat(First(10)) == First(20)
    assert First(None).concat(First(10)) == First(None)
    assert First('foo').concat(First('bar')) == First('foo')


# Generated at 2022-06-14 03:47:04.559586
# Unit test for constructor of class Max
def test_Max():
    assert Max(1).__eq__(Max(1))
    assert Max(1).fold(lambda value: value) == 1
    assert Max.neutral().value == -float("inf")



# Generated at 2022-06-14 03:47:21.761757
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    assert Sum(1).__eq__(Sum(1)) == True
    assert Sum(1).__eq__(Sum(2)) == False

# Generated at 2022-06-14 03:47:25.256529
# Unit test for constructor of class All
def test_All():
    assert All(True) == All(True)
    assert All(True) != All(False)
    assert All(True) != All(2)
    assert All(False) != All(2)
    assert All(None) != All(2)


# Unit test of fold function in class All

# Generated at 2022-06-14 03:47:29.140526
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(1)) == 'Max[value=1]'  # pragma: no cover


# Generated at 2022-06-14 03:47:31.943705
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(5).concat(Max(7)) == Max(7)



# Generated at 2022-06-14 03:47:34.566128
# Unit test for method concat of class Last
def test_Last_concat():  # pragma: no cover
    assert Last(9).concat(Last(8)).value == 8


# Generated at 2022-06-14 03:47:38.839251
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    assert Semigroup(1) != Semigroup(2)
    assert Semigroup(1) == Semigroup(1)
    assert Semigroup(1) != Semigroup(False)
    assert Semigroup(1) != Semigroup('1')

# Generated at 2022-06-14 03:47:40.300500
# Unit test for method concat of class Last
def test_Last_concat():
    assert Last(1).concat(Last(2)).value == 2



# Generated at 2022-06-14 03:47:43.710143
# Unit test for method concat of class Map
def test_Map_concat():
    assert Map({'a': Sum(1), 'b': Sum(2)}).concat(Map({'a': Sum(3), 'b': Sum(4)})) == Map({'a': Sum(4), 'b': Sum(6)})


# Generated at 2022-06-14 03:47:47.369981
# Unit test for method __str__ of class Max
def test_Max___str__():
    """
    :returns: True if test passed successfully, otherwise raises AssertionError exception
    :rtype: bool
    """
    assert(str(Max(1)) == 'Max[value=1]')



# Generated at 2022-06-14 03:47:50.433757
# Unit test for method concat of class Max
def test_Max_concat():
    """
    Function test_Max_concat have not argument
    """

    assert Max(1).concat(Max(2)) == Max(2)


# Generated at 2022-06-14 03:48:24.896390
# Unit test for constructor of class One
def test_One():
    assert One(True).value == True
    assert One(False).value == False
    assert One(5).value == 5
    assert One('5').value == '5'
    assert One('foo').value == 'foo'


# Generated at 2022-06-14 03:48:28.273389
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(3).concat(Max(1)) == Max(3)
    assert Max(3).concat(Max(5)) == Max(5)
    assert Max(5).concat(Max(3)) == Max(5)



# Generated at 2022-06-14 03:48:34.461697
# Unit test for method concat of class Sum
def test_Sum_concat():
    assert Sum(1).concat(Sum(2)) == Sum(3)
    assert Sum(1).concat(Sum(2)).concat(Sum(3)) == Sum(6)
    assert Sum(2).concat(Sum(1)) == Sum(3)
    assert Sum(2).concat(Sum(1)).concat(Sum(3)) == Sum(6)



# Generated at 2022-06-14 03:48:37.357277
# Unit test for method concat of class Max
def test_Max_concat():
    semigroup_1 = Max(1)
    semigroup_2 = Max(2)
    assert semigroup_1.concat(semigroup_1).value == 1
    assert semigroup_1.concat(semigroup_2).value == 2


# Generated at 2022-06-14 03:48:41.368953
# Unit test for method concat of class First
def test_First_concat():
    first1 = First(1)
    assert first1.concat(First(5)).value == 1
    assert first1.concat(First(0)).value == 1


# Generated at 2022-06-14 03:48:44.761270
# Unit test for method concat of class One
def test_One_concat():
    assert One(True).concat(One(False)).value is True
    assert One(False).concat(One(True)).value is True
    assert One(False).concat(One(False)).value is False


# Generated at 2022-06-14 03:48:47.100173
# Unit test for method __str__ of class All
def test_All___str__():
    assert str(All(True)) == 'All[value=True]'

# Generated at 2022-06-14 03:48:51.660976
# Unit test for method __str__ of class First
def test_First___str__():
    for value in (None, 1, 'a', set()):
        first = First(value)
        assert 'Fist[value={}]'.format(value) == str(first)


# Generated at 2022-06-14 03:48:54.986153
# Unit test for method concat of class First
def test_First_concat():
    assert First(1).concat(First(2)).value == 1
    assert First('abc').concat(First('def')).value == 'abc'
    assert First({}).concat(First([])).value == {}


# Generated at 2022-06-14 03:48:55.923726
# Unit test for constructor of class Last
def test_Last():
    assert Last(10) == Last(10)

# Generated at 2022-06-14 03:49:31.424939
# Unit test for constructor of class Min
def test_Min():
    x = Min(5)
    y = Min(6)

    result = x.concat(y) #test concat
    assert result.value == 5
    assert result.fold(lambda v: True) == True

    z = Min.neutral()
    assert z.value == float("inf")


# Generated at 2022-06-14 03:49:32.298193
# Unit test for constructor of class First
def test_First():
    assert First(1).value == 1


# Generated at 2022-06-14 03:49:36.229436
# Unit test for method concat of class Map
def test_Map_concat():

    a = Map({1: Sum(1), 2: Sum(2)})
    b = Map({1: Sum(2), 2: Sum(3)})

    actual = a.concat(b)
    expected = {1: Sum(3), 2: Sum(5)}

    assert actual.value == expected


# Generated at 2022-06-14 03:49:38.146093
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    assert str(Sum(42)) == "Sum[value=42]"


# Generated at 2022-06-14 03:49:41.669458
# Unit test for method __str__ of class First
def test_First___str__():
    # Arrange
    instance = First({'a': 1})
    expected = "Fist[value=a:1]"
    # Act
    actual = str(instance)
    # Assert
    assert actual == expected


# Generated at 2022-06-14 03:49:44.644754
# Unit test for constructor of class Map
def test_Map():
    a = Map({'a':Sum(1), 'b': Sum(2)})
    b = Map({'a':Sum(2)})
    assert a == {'a':Sum(1), 'b': Sum(2)}
    assert b == {'a':Sum(2)}


# Generated at 2022-06-14 03:49:45.998687
# Unit test for constructor of class Semigroup
def test_Semigroup():
    assert Semigroup(1) == Semigroup(1)

# Generated at 2022-06-14 03:49:47.816757
# Unit test for constructor of class Semigroup
def test_Semigroup():
    assert Sum(2) == Sum(2)



# Generated at 2022-06-14 03:49:50.793243
# Unit test for constructor of class Min
def test_Min():
    val = Min(5)
    assert val.value == 5
    try:
        Min(-5)
    except Exception:
        print("Exception in Min for case value < 0")

test_Min()


# Generated at 2022-06-14 03:49:56.705924
# Unit test for constructor of class First
def test_First():  # pragma: no cover
    assert First(1) == First(1)
    assert First(1) != Last(1)
    assert First(1).concat(First(2)) == First(1)
    assert First(1).concat(Last(2)) == First(1)



# Generated at 2022-06-14 03:51:03.276168
# Unit test for method concat of class Last
def test_Last_concat():
    l1 = Last('value 1')
    l2 = Last('value 2')
    l3 = Last('value 3')

    c1 = l1.concat(l2)
    c2 = c1.concat(l3)

    assert c1 == Last('value 2')
    assert c2 == Last('value 3')


# Generated at 2022-06-14 03:51:05.325362
# Unit test for method concat of class Sum
def test_Sum_concat():
    a = Sum(1)
    b = a.concat(Sum(2))
    assert b == Sum(3)



# Generated at 2022-06-14 03:51:08.405520
# Unit test for method __str__ of class Last
def test_Last___str__():
    assert str(Last(1)) == 'Last[value=1]'



# Generated at 2022-06-14 03:51:11.778546
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    assert str(Sum(2)) == 'Sum[value=2]'
    assert str(Sum('a')) == 'Sum[value=a]'
    assert str(Sum(True)) == 'Sum[value=True]'


# Generated at 2022-06-14 03:51:17.361575
# Unit test for constructor of class One
def test_One():
    assert One('a').value == 'a'
    assert One(None).value is None
    assert One(1).value == 1
    assert One(0).value == 0
    assert One([]).value == []
    assert One(()).value == ()
    assert One({}).value == {}
    assert One(True).value is True


# Generated at 2022-06-14 03:51:18.524878
# Unit test for constructor of class Last
def test_Last():
    monoid = Last(1)
    assert monoid.value == 1

# Generated at 2022-06-14 03:51:20.207940
# Unit test for constructor of class One
def test_One():
    assert One(True)
    assert One(False)
    assert not One(None)
    assert not One(0)



# Generated at 2022-06-14 03:51:27.092492
# Unit test for method concat of class All
def test_All_concat():
    assert All(True).concat(All(True)) == All(True)
    assert All(True).concat(All(False)) == All(False)
    assert All(False).concat(All(True)) == All(False)
    assert All(False).concat(All(False)) == All(False)

# Generated at 2022-06-14 03:51:29.817483
# Unit test for method __str__ of class Map
def test_Map___str__():
    m1 = Map({1: Sum(1), 2: Sum(2)})
    assert str(m1) == 'Map[value={1: Sum[value=1], 2: Sum[value=2]}]'



# Generated at 2022-06-14 03:51:31.654509
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(1)) == 'Max[value=1]'


# Generated at 2022-06-14 03:54:01.359696
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    assert(Sum(1).fold(lambda x: x + 1) == 2)
    assert(All(True).fold(lambda x: not x) is False)
    assert(Last(3).fold(lambda x: x) == 3)


# Generated at 2022-06-14 03:54:03.164727
# Unit test for constructor of class Max
def test_Max():
    assert Max(1) == Max(1)

test_Max()


# Generated at 2022-06-14 03:54:05.785611
# Unit test for constructor of class Last
def test_Last():
    assert Last(1) == Last(1)
    assert Last(2) == Last(2)
    assert Last(1) != Last(2)


# Generated at 2022-06-14 03:54:08.097185
# Unit test for constructor of class Map
def test_Map():
    Map([1, 2])
    Map({1, 2})
    Map({1: 2})



# Generated at 2022-06-14 03:54:09.858201
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(3).concat(Min(1)).value == 1
    assert Min(3).concat(Min(5)).value == 3


# Generated at 2022-06-14 03:54:12.143080
# Unit test for method __str__ of class Max
def test_Max___str__():  # pragma: no cover
    assert str(Max(5)) == 'Max[value=5]'


# Generated at 2022-06-14 03:54:14.449710
# Unit test for method __str__ of class Min
def test_Min___str__():
    actual = Min(10).__str__()
    expected = 'Min[value=10]'
    assert actual == expected


# Generated at 2022-06-14 03:54:17.564179
# Unit test for method __str__ of class One
def test_One___str__():
    assert str(One(True)) == 'One[value=True]'
    assert str(One(False)) == 'One[value=False]'


# Generated at 2022-06-14 03:54:27.272628
# Unit test for constructor of class Semigroup
def test_Semigroup():
    foo = Semigroup(3)
    assert foo.value == 3


subclasses = [Sum, All, One, First, Last, Map, Max, Min]
subclasses_name = list(map(lambda c: c.__name__, subclasses))
subclasses_value = list(map(lambda c: c.neutral_element, subclasses))
subclasses_pairs = list(zip(subclasses_name, subclassed_value))
subclasses_instances = list(
    map(
        lambda p: p[0],
        map(lambda p: p[1](p[0]), subclasses_pairs)
    )
)
subclasses_instances_concat = list(
    map(
        lambda semigroup: semigroup.concat(semigroup),
        subclassed_instances
    )
)
subclasses_inst