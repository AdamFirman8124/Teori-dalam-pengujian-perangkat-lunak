

# Generated at 2022-06-14 03:44:32.033657
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(1).concat(Max(2)) == Max(2)


# Generated at 2022-06-14 03:44:36.505778
# Unit test for method concat of class Min
def test_Min_concat():
    a = Min(2)
    b = Min(3)
    c = a.concat(b)
    assert c.value == 2



# Generated at 2022-06-14 03:44:41.043084
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(1).concat(Max(2)) == Max(2)
    assert Max(2).concat(Max(1)) == Max(2)
    assert Max(2).concat(Max(2)) == Max(2)
    assert Max(1).concat(Sum(2)).concat(Min(3)).concat(All(True)).concat(One(False)) == Max(1)



# Generated at 2022-06-14 03:44:46.219388
# Unit test for method concat of class Min
def test_Min_concat(): # pragma: no cover
    assert Min(0).concat(Min(2)) == Min(0)
    assert Min(2).concat(Min(0)) == Min(0)
    assert Min(0).concat(Min(0)) == Min(0)
    assert Min(2).concat(Min(2)) == Min(2)


# Generated at 2022-06-14 03:44:49.510810
# Unit test for method concat of class Min
def test_Min_concat():
    m1 = Min(1)
    m2 = Min(2)
    m3 = m1.concat(m2)
    assert m3 == Min(1)
    assert m3.value == 1


# Generated at 2022-06-14 03:44:53.991900
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(2).concat(Max(3)) == Max(3)
    assert Max(1).concat(Max(2)) == Max(2)
    assert Max(1).concat(Max(0)) == Max(1)
    assert Max(0).concat(Max(1)) == Max(1)



# Generated at 2022-06-14 03:44:57.219888
# Unit test for method concat of class Min
def test_Min_concat():
    a = Min(3)
    b = Min(2)
    c = Min(-1)
    d = Min(-1)
    assert a.concat(b) == b.concat(a)
    assert b.concat(c) == Min(-1)

# Generated at 2022-06-14 03:45:01.199897
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(2).concat(Min(1)) == Min(1)
    assert Min(1).concat(Min(2)) == Min(1)
    assert Min(3).concat(Min(3)) == Min(3)



# Generated at 2022-06-14 03:45:08.562995
# Unit test for method concat of class Max
def test_Max_concat():
    """

    :return: None
    """
    assert Max(1).concat(Max(2)).value == 2
    assert Max(2).concat(Max(2)).value == 2
    assert Max(2).concat(Max(1)).value == 2
    assert Max(1).concat(Max(0)).value == 1
    assert Max(0).concat(Max(1)).value == 1



# Generated at 2022-06-14 03:45:14.361372
# Unit test for method concat of class Max
def test_Max_concat():
    assert(Max(2).concat(Max(3)).fold(lambda x:x) == 3)
    assert(Max(2).concat(Max(2)).fold(lambda x:x) == 2)
    assert(Max(3).concat(Max(2)).fold(lambda x:x) == 3)


# Generated at 2022-06-14 03:45:17.570283
# Unit test for method concat of class Sum
def test_Sum_concat():  # pragma: no cover
    assert Sum(1).concat(Sum(2)) == Sum(3)



# Generated at 2022-06-14 03:45:19.113668
# Unit test for method __str__ of class Last
def test_Last___str__():

    assert str(Last(5)) == 'Last[value=5]'


# Generated at 2022-06-14 03:45:24.447298
# Unit test for constructor of class Min
def test_Min():
    assert Min(3).concat(Min(2)).value == 2
    assert Min(3).concat(Min(-3)).value == -3
    assert Min(-3).concat(Min(5)).value == -3
    assert Min(-7).concat(Min(-5)).value == -7


# Generated at 2022-06-14 03:45:26.258259
# Unit test for method __str__ of class One
def test_One___str__():  # pragma: no cover
    assert str(One(1)) == 'One[value=1]'



# Generated at 2022-06-14 03:45:27.668758
# Unit test for constructor of class Sum
def test_Sum():
    sum = Sum(10)
    assert sum.value == 10


# Generated at 2022-06-14 03:45:28.832813
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(2)) == 'Max[value=2]', "Max.__str__ method giving incorrect string representation of the class"

# Test concat method of class Max

# Generated at 2022-06-14 03:45:32.266899
# Unit test for method concat of class Max
def test_Max_concat():
    a = Max(100)
    b = Max(2)

    assert a.concat(b).value == 100


# Generated at 2022-06-14 03:45:34.361955
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    assert Semigroup(3).fold(lambda x: x * 2) == 6
    assert Semigroup("foo").fold(lambda x: x + "bar") == "foobar"


# Generated at 2022-06-14 03:45:38.276784
# Unit test for method __str__ of class Map
def test_Map___str__():
    m1 = Map({'name': 'Lion'})
    assert (str(m1) == 'Map[value={name: Semigroup[value=Lion]}]')
    m2 = Map({'name': 'Angry'})
    assert (str(m2) == 'Map[value={name: Semigroup[value=Angry]}]')


# Generated at 2022-06-14 03:45:42.110988
# Unit test for constructor of class Semigroup
def test_Semigroup():
    assert Semigroup(2) == Semigroup(Max(2))
    assert Semigroup(5.5) == Semigroup(Min(5.5))


# Generated at 2022-06-14 03:45:53.043228
# Unit test for method __str__ of class Last
def test_Last___str__():  # pragma: no cover
    assert str(Last(1)) == 'Last[value=1]'
    assert str(Last(2.2)) == 'Last[value=2.2]'
    assert str(Last('test')) == "Last[value=test]"
    assert str(Last((1,))) == 'Last[value=(1,)]'
    assert str(Last({1})) == 'Last[value={1}]'
    assert str(Last([1])) == 'Last[value=[1]]'
    assert str(Last({1: 1})) == 'Last[value={1: 1}]'
    class Temp:
        pass
    temp = Temp()
    assert str(Last(temp)) == 'Last[value={}]'.format(str(temp))
    assert str(Last(None)) == 'Last[value=None]'


# Generated at 2022-06-14 03:45:53.934100
# Unit test for constructor of class Sum
def test_Sum():
    actual = Sum(3)
    expected = Sum(3)
    assert actual == expected



# Generated at 2022-06-14 03:45:54.730584
# Unit test for constructor of class First
def test_First():
    assert First(1) == First(1)
    assert First(1).value == 1



# Generated at 2022-06-14 03:45:57.121803
# Unit test for constructor of class Map
def test_Map():
    assert Map({'a': 1, 'b': 2, 'c': 3}) == Map({'b': 2, 'c': 3, 'a': 1})



# Generated at 2022-06-14 03:45:58.543900
# Unit test for constructor of class First
def test_First():
    assert First(1) == First(1)



# Generated at 2022-06-14 03:45:59.172998
# Unit test for constructor of class Max
def test_Max():
    assert Max(1).value == 1



# Generated at 2022-06-14 03:46:02.531218
# Unit test for constructor of class Map
def test_Map():
    assert Map({1: Sum(1), 2: Sum(2)}).value == {1: Sum(1), 2: Sum(2)}



# Generated at 2022-06-14 03:46:04.516884
# Unit test for constructor of class Min
def test_Min():
    min = Min(10)
    assert min.value == 10



# Generated at 2022-06-14 03:46:06.918746
# Unit test for method concat of class First
def test_First_concat():  # pragma: no cover
    f1 = First("a")
    f2 = First("b")
    f3 = f1.concat(f2)
    assert f3.value == "a"



# Generated at 2022-06-14 03:46:09.622018
# Unit test for method concat of class Sum
def test_Sum_concat():
    sum_instance_1 = Sum(1)
    sum_instance_2 = Sum(2)
    assert sum_instance_1.concat(sum_instance_2) == Sum(3)


# Generated at 2022-06-14 03:46:13.049773
# Unit test for constructor of class Semigroup
def test_Semigroup():
    assert Semigroup("foo").value == "foo"


# Generated at 2022-06-14 03:46:14.482977
# Unit test for method __str__ of class Min
def test_Min___str__():
    assert str(Min(3)) == 'Min[value=3]'


# Generated at 2022-06-14 03:46:15.754511
# Unit test for constructor of class First
def test_First():
    f = First(42)
    assert f.value == 42



# Generated at 2022-06-14 03:46:21.110797
# Unit test for method concat of class All
def test_All_concat():
    assert id(All(True).concat(All(True))) == id(All(True)), \
        "All should return singleton true when concat with itself"
    assert id(All(True).concat(All(False))) == id(All(False)), \
        "All should return singleton false when concat with other singleton false"
    assert id(All(False).concat(All(False))) == id(All(False)), \
        "All should return singleton false when concat with itself"


# Generated at 2022-06-14 03:46:25.499331
# Unit test for method __str__ of class Last
def test_Last___str__():
    assert str(Last(1)) == 'Last[value=1]'
    assert str(Last(2)) == 'Last[value=2]'
    assert str(Last(3)) == 'Last[value=3]'


# Generated at 2022-06-14 03:46:27.301100
# Unit test for constructor of class Min
def test_Min():
    min = Min(1)
    assert min.value == 1


# Generated at 2022-06-14 03:46:36.341856
# Unit test for constructor of class Map

# Generated at 2022-06-14 03:46:38.159316
# Unit test for constructor of class Last
def test_Last():
    """
    This method tests constructor of class Last
    """
    assert Last("a").value == "a"



# Generated at 2022-06-14 03:46:39.998434
# Unit test for method __str__ of class First
def test_First___str__():
    assert str(First(1)) == 'Fist[value=1]'



# Generated at 2022-06-14 03:46:41.819092
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    assert str(Sum(1)) == "Sum[value=1]"

# Generated at 2022-06-14 03:46:46.987441
# Unit test for method __str__ of class Map
def test_Map___str__():
    assert str(Map({'a': Sum(1), 'b': Sum(2)})) == "Map[value={'a': Sum[value=1], 'b': Sum[value=2]}]"



# Generated at 2022-06-14 03:46:50.168504
# Unit test for method __str__ of class Map
def test_Map___str__():
    map1 = Map({1: Sum(1), 2: Sum(2)})
    assert str(map1) == 'Map[value={1: Sum[value=1], 2: Sum[value=2]}]'


# Generated at 2022-06-14 03:46:52.841469
# Unit test for method concat of class Min
def test_Min_concat():
    min1 = Min(1)
    min2 = Min(2)
    assert min1.concat(min2) == min1


# Generated at 2022-06-14 03:46:58.464041
# Unit test for method concat of class One
def test_One_concat():
    one_1 = One(5)
    one_2 = One(2)
    new_one = one_1.concat(one_2)
    assert new_one == One(5)
    assert one_2.concat(one_1) == One(2)



# Generated at 2022-06-14 03:47:02.186129
# Unit test for method concat of class Sum
def test_Sum_concat():
    assert Sum(1).concat(Sum(1)) == Sum(2)
    assert Sum(100).concat(Sum(-100)) == Sum(0)
    assert Sum(100500).concat(Sum(100500)) == Sum(201000)


# Generated at 2022-06-14 03:47:03.373668
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(10)) == 'Max[value=10]'


# Generated at 2022-06-14 03:47:05.996497
# Unit test for constructor of class Sum
def test_Sum():
    assert Sum(1) == Sum(1)
    assert Sum(1) != Sum(2)


# Generated at 2022-06-14 03:47:11.794126
# Unit test for method __str__ of class One
def test_One___str__():
    assert One(1).__str__() == 'One[value=1]'
    assert One(True).__str__() == 'One[value=True]'
    assert One(False).__str__() == 'One[value=False]'
    assert One(None).__str__() == 'One[value=None]'
    assert One("1").__str__() == 'One[value=1]'
    assert One("True").__str__() == 'One[value=True]'
    assert One("False").__str__() == 'One[value=False]'
    assert One("None").__str__() == 'One[value=None]'
    assert One([]).__str__() == 'One[value=[]]'
    assert One([""]).__str__() == 'One[value=[]]'
    assert One([1]).__str

# Generated at 2022-06-14 03:47:15.776267
# Unit test for constructor of class Semigroup
def test_Semigroup():
    with pytest.raises(TypeError):
        Semigroup()
    with pytest.raises(TypeError):
        Semigroup(1, 2)
    Semigroup(1)
    Semigroup("a")
    Semigroup([])


# Generated at 2022-06-14 03:47:19.124303
# Unit test for constructor of class All
def test_All():
    a = All(True)
    b = All(True)
    c = All(False)
    # This should work

    assert a == b
    assert a.concat(b) == c



# Generated at 2022-06-14 03:47:24.193321
# Unit test for constructor of class One
def test_One():
    one = One(True)
    assert one.value == True

# Generated at 2022-06-14 03:47:25.831952
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    assert str(Sum(1)) == 'Sum[value=1]'


# Generated at 2022-06-14 03:47:29.019804
# Unit test for method __str__ of class All
def test_All___str__():
    value = All(True)
    assert str(value) == 'All[value=True]'

# Generated at 2022-06-14 03:47:38.556789
# Unit test for method concat of class Map
def test_Map_concat():
    m1 = Map({'first': First(1), 'second': First(2)})
    m2 = Map({'first': First(3), 'second': First(4)})
    result = Map({'first': First(1), 'second': First(2)}).concat(Map({'first': First(3), 'second': First(4)}))
    assert result.value['first'].value == 1 and result.value['second'].value == 2
    assert m1.concat(m2).fold(lambda v: v['first'].value + v['second'].value) == 3
    assert m1.fold(lambda v: v['first'].value + v['second'].value) == 3

# Generated at 2022-06-14 03:47:41.239735
# Unit test for method __str__ of class Map

# Generated at 2022-06-14 03:47:43.032877
# Unit test for constructor of class Semigroup
def test_Semigroup():
    value = 1
    monoid = Semigroup(value)
    assert monoid.value == 1



# Generated at 2022-06-14 03:47:45.087733
# Unit test for method __str__ of class Last
def test_Last___str__():  # pragma: no cover
    assert str(Last('1')) == 'Last[value=1]'


# Generated at 2022-06-14 03:47:47.319705
# Unit test for constructor of class Last
def test_Last():
    """
    Unit test for Last
    """
    last_obj = Last("Hello")
    assert last_obj.value == "Hello"



# Generated at 2022-06-14 03:47:49.891328
# Unit test for constructor of class One
def test_One():
    one = One(True)
    assert one.value == True
    assert one.concat(One(False)) == One(True)


# Generated at 2022-06-14 03:47:51.367886
# Unit test for method __str__ of class All
def test_All___str__():
    assert str(All(True)) == 'All[value=True]'
    assert str(All(False)) == 'All[value=False]'



# Generated at 2022-06-14 03:47:55.847341
# Unit test for constructor of class Sum
def test_Sum():
    assert Sum(10).value == 10



# Generated at 2022-06-14 03:48:05.725184
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():

    # Create instances 'a' and 'b', of class Sum
    a = Sum(1)
    b = Sum(2)

    # Create a function 'add_10'
    def add_10(n):
        return Sum(n + 10)

    # Create an instance 'c' that is a result of the method fold of class Semigroup
    c = Sum(a.value).fold(add_10)

    # Check the 'assert_equals' method of the TestCase class
    assert_equals(11, c.value)

    # Check the 'assert_equals' method of the TestCase class
    assert_equals(b.fold(add_10).value, 12)

# Generated at 2022-06-14 03:48:07.428663
# Unit test for constructor of class Max
def test_Max():
    assert Max(10).value==Max(10).value



# Generated at 2022-06-14 03:48:09.446850
# Unit test for method concat of class Sum
def test_Sum_concat():
    assert Sum(5).concat(Sum(7)) == Sum(12)


# Generated at 2022-06-14 03:48:18.286438
# Unit test for method fold of class Semigroup

# Generated at 2022-06-14 03:48:23.095032
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(3).concat(Min(8)) == Min(3)
    assert Min(8).concat(Min(3)) == Min(3)
    assert Min(8).concat(Min(8)) == Min(8)



# Generated at 2022-06-14 03:48:25.909248
# Unit test for method __str__ of class Last
def test_Last___str__():
    assert str(Last(1)) == "Last[value=1]", "Error __str__ method of class Last"

# Generated at 2022-06-14 03:48:28.893524
# Unit test for method __str__ of class Map
def test_Map___str__():
    assert str(Map({'a': Min(1), 'b': Min(2)})) == "Map[value={'a': Min[value=1], 'b': Min[value=2]}]"



# Generated at 2022-06-14 03:48:31.551254
# Unit test for method __str__ of class All
def test_All___str__():
    val = True
    all_ = All(val)
    expected = 'All[value={}]'.format(val)
    assert all_.__str__() == expected


# Generated at 2022-06-14 03:48:34.413354
# Unit test for method __str__ of class Max
def test_Max___str__():
    # act
    actual = str(Max(5))

    # assert
    assert actual == 'Max[value=5]'



# Generated at 2022-06-14 03:48:41.808563
# Unit test for method concat of class Sum
def test_Sum_concat():
    assert Sum(1).concat(Sum(2)) == Sum(3)


# Generated at 2022-06-14 03:48:44.062795
# Unit test for method __str__ of class Map
def test_Map___str__():
    assert str(Map({'a': 1})) == 'Map[value={\'a\': 1}]'


# Generated at 2022-06-14 03:48:45.483750
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    assert str(Sum(0)) == "Sum[value=0]"



# Generated at 2022-06-14 03:48:47.100481
# Unit test for constructor of class Max
def test_Max():
    assert Max(2).value == 2


# Generated at 2022-06-14 03:48:50.691920
# Unit test for method __str__ of class All
def test_All___str__():
    assert 'All[value=False]' == str(All(False))
    assert 'All[value=True]' == str(All(True))


# Generated at 2022-06-14 03:48:52.224185
# Unit test for constructor of class Last
def test_Last():
    assert Last(5).value == 5


# Generated at 2022-06-14 03:48:53.836089
# Unit test for method __str__ of class Min
def test_Min___str__():
    assert str(Min(8)) == 'Min[value=8]'


# Generated at 2022-06-14 03:48:56.366043
# Unit test for method __str__ of class Map
def test_Map___str__():
    assert str(Map({'a': Sum(1)})) == 'Map[value={\'a\': Sum[value=1]}]'



# Generated at 2022-06-14 03:49:03.004734
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(1).concat(Max(2)).concat(Max(4)) == Max(4)
    assert Max(1).concat(Max(2)).concat(Max(4)).concat(Max(0.5)) == Max(4)
    assert Max(0.5).concat(Max(1)).concat(Max(2)).concat(Max(4)) == Max(4)


# Generated at 2022-06-14 03:49:07.626131
# Unit test for method concat of class Min
def test_Min_concat():
    sm1 = Min(1)
    sm2 = Min(2)
    assert sm2.concat(sm1) == sm1
    sm3 = Min(1.5)
    assert sm3.concat(sm2).concat(sm1) == sm1
    assert sm3.concat(sm2).concat(sm3) == sm3


# Generated at 2022-06-14 03:49:17.544107
# Unit test for constructor of class Semigroup
def test_Semigroup():  # pragma: no cover
    assert Semigroup(1).value == 1
    assert isinstance(Semigroup(1), Semigroup)


# Generated at 2022-06-14 03:49:20.108109
# Unit test for method __str__ of class Min
def test_Min___str__():
    assert Min(1).__str__() == 'Min[value=1]'


# Generated at 2022-06-14 03:49:23.106213
# Unit test for method __str__ of class Min
def test_Min___str__():
    # Given
    expected = "Min[value=1]"

    # When
    actual = Min(1)

    # Then
    assert str(actual) == expected

# Generated at 2022-06-14 03:49:25.947211
# Unit test for method __str__ of class All
def test_All___str__():
    result = str(All(True))
    expected = "All[value=True]"
    assert result == expected


# Generated at 2022-06-14 03:49:27.089742
# Unit test for constructor of class Min
def test_Min():
    assert Min(1).value == 1



# Generated at 2022-06-14 03:49:30.197879
# Unit test for constructor of class Last
def test_Last():  # pragma: no cover
    assert Last(1).value == 1
    assert Last(1) == Last(1)
    assert Last(1) != Last(2)


# Generated at 2022-06-14 03:49:32.872158
# Unit test for method __str__ of class All
def test_All___str__():
    assert 'All[value=True]' == str(All(True)), 'Error in All.__str__()'



# Generated at 2022-06-14 03:49:35.076617
# Unit test for constructor of class One
def test_One():
    assert One(True) == One(True)

# Generated at 2022-06-14 03:49:37.567457
# Unit test for constructor of class All
def test_All():
    assert All(True) == All(True)
    assert All(False) == All(False)


# Generated at 2022-06-14 03:49:40.604362
# Unit test for method concat of class All
def test_All_concat():  # pragma: no cover
    assert All(True).concat(All(False)) == All(False)
    assert All(42).concat(All('foo')) == All(True)


# Generated at 2022-06-14 03:49:56.312856
# Unit test for method __str__ of class Map
def test_Map___str__():
    m = Map({'foo': 1, 'bar': 2})
    assert str(m) == 'Map[value={"foo": 1, "bar": 2}]'

# Generated at 2022-06-14 03:49:59.449756
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    assert Semigroup(1).fold(lambda x: x + 3) == 4
    assert Semigroup('1').fold(lambda x: x + '3') == '13'


# Generated at 2022-06-14 03:50:02.614927
# Unit test for constructor of class Last
def test_Last():
    last_instance = Last(5)
    assert last_instance.value == 5



# Generated at 2022-06-14 03:50:05.449850
# Unit test for method __str__ of class Last
def test_Last___str__(): # pragma: no cover
    assert str(Last("foo")) == "Last[value=foo]"
    assert str(Last("bar")) == "Last[value=bar]"


# Generated at 2022-06-14 03:50:08.039931
# Unit test for method __str__ of class All
def test_All___str__():
    assert str(All(True)) == "All[value=True]"
    assert str(All(False)) == "All[value=False]"


# Generated at 2022-06-14 03:50:11.055256
# Unit test for method __str__ of class One
def test_One___str__():
    print('One.__str__():')
    print(One(False))
    print(One(True))
    print(One('False'))
    print(One('True'))


# Generated at 2022-06-14 03:50:16.387106
# Unit test for method concat of class Min
def test_Min_concat():
    """
    Unit test for method concat of class Min
    """
    assert Min(10) == Min(10)
    assert Min(10).concat(Min(1)) == Min(1)
    assert Min(10).concat(Min(10)) == Min(10)
    assert Min(10).concat(Min(20)) == Min(10)
    assert Min(10).concat(Min(5)) == Min(5)



# Generated at 2022-06-14 03:50:19.985240
# Unit test for constructor of class Map
def test_Map():
    assert Map({"a": Sum(1), "b": Sum(2)}) == Map({"a": Sum(1), "b": Sum(2)})



# Generated at 2022-06-14 03:50:22.459345
# Unit test for method __str__ of class First
def test_First___str__():
    assert str(First('abc')) == 'Fist[value=abc]'



# Generated at 2022-06-14 03:50:30.236536
# Unit test for constructor of class All
def test_All():  # pragma: no cover
    params = [
        All.neutral(),
        All(True),
        All(False),
        All(1),
        All(0),
        All({}),
        All([])
    ]

    expected = [
        True,
        True,
        False,
        True,
        False,
        True,
        False
    ]

    for param, expect in zip(params, expected):
        assert param.value == expect


# Generated at 2022-06-14 03:50:43.398893
# Unit test for constructor of class Semigroup
def test_Semigroup():
    isinstance(Semigroup(1), Semigroup)

# Generated at 2022-06-14 03:50:45.423347
# Unit test for constructor of class Min
def test_Min():
    assert Min(2) == Min(2)



# Generated at 2022-06-14 03:50:49.578103
# Unit test for constructor of class Last
def test_Last():
    assert Last(4) == Last(4)
    assert Last(4) == Last(5)
    assert Last(4).value == Last(4).value
    assert Last(4) != Last(5)


# Generated at 2022-06-14 03:50:52.607843
# Unit test for method concat of class Map
def test_Map_concat():
    assert Map({4: Sum(4), 3: Sum(3)}).concat(Map({4: Sum(4), 3: Sum(3)})) == Map({3: Sum(6), 4: Sum(8)})


# Generated at 2022-06-14 03:50:54.032266
# Unit test for constructor of class Max
def test_Max():
    assert Max(10) == Max(10)



# Generated at 2022-06-14 03:50:59.203435
# Unit test for method __str__ of class Max
def test_Max___str__():
  assert_equal(str(Max(1)), "Max[value={}]".format(1))
  assert_equal(str(Max(5)), "Max[value={}]".format(5))
  assert_equal(str(Max(7)), "Max[value={}]".format(7))
  assert_equal(str(Max(0)), "Max[value={}]".format(0))


# Generated at 2022-06-14 03:51:03.862769
# Unit test for method concat of class Sum
def test_Sum_concat():
    sum_1 = Sum(1)
    sum_2 = Sum(2)
    sum_3 = Sum(3)

    assert sum_1.concat(sum_2) == Sum(3)
    assert sum_2.concat(sum_3) == Sum(5)
    assert sum_1.concat(sum_3) == Sum(4)
    assert sum_1.concat(Sum(0)) == Sum(1)
    assert sum_1.concat(Semigroup(0)) == Sum(1)



# Generated at 2022-06-14 03:51:07.229909
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(10).concat(Max(54)).value == 54
    assert Max(10).concat(Max(-54)).value == 10
    assert Max(-10).concat(Max(-54)).value == -10


# Generated at 2022-06-14 03:51:08.998413
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(2).concat(Min(3)) == Min(2)


# Generated at 2022-06-14 03:51:11.535472
# Unit test for method __str__ of class First
def test_First___str__():
    """
    Unit test for method __str__ of class First
    """
    s = First(1)
    assert s.__str__() == "Fist[value=1]"


# Generated at 2022-06-14 03:51:27.071216
# Unit test for method __str__ of class First
def test_First___str__():
    # Arrange
    first_semigroup = First(1)

    # Act
    actual = first_semigroup.__str__()

    # Assert
    assert actual == 'Fist[value=1]'


# Generated at 2022-06-14 03:51:28.932287
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(2)) == 'Max[value=2]'


# Generated at 2022-06-14 03:51:30.804351
# Unit test for method __str__ of class One
def test_One___str__():
    assert 'One[value=True]' == str(One(True))


# Generated at 2022-06-14 03:51:36.363781
# Unit test for method concat of class First
def test_First_concat():
    assert First(1).concat(First(2)) == First(1)
    assert First(0).concat(First(2)) == First(0)
    assert First(False).concat(First(True)) == First(False)



# Generated at 2022-06-14 03:51:42.001849
# Unit test for method concat of class Min
def test_Min_concat():
    min_10 = Min(10)
    min_1 = Min(1)
    min_15 = Min(15)
    min_max_min = min_10.concat(min_1)
    assert min_max_min == Min(1)
    min_max_min = min_15.concat(min_1)
    assert min_max_min == Min(1)
    min_max_min = min_10.concat(min_15)
    assert min_max_min == Min(10)



# Generated at 2022-06-14 03:51:53.565773
# Unit test for constructor of class Max
def test_Max():
    from hypothesis import given
    from hypothesis import strategies as st
    from pymonad.Either import Left, Right
    from pymonad.Maybe import Just, Nothing
    from pymonad.List import List, Nil, Cons
    from pymonad.Reader import Reader
    from pymonad.Writer import Writer

    @given(st.floats())
    def test_Max_left(f):
        assert Max(f).concat(Left(f)).fold(lambda m, _: m) == Max(f)

    @given(st.floats())
    def test_Max_right(f):
        assert Max(f).concat(Right(f)).fold(lambda _, m: m) == Max(f)

    @given(st.floats())
    def test_Max_just(f):
        assert Max(f).concat

# Generated at 2022-06-14 03:51:55.194786
# Unit test for method concat of class Sum
def test_Sum_concat():  # pragma: no cover
    semigroup = Sum(2)
    assert semigroup.concat(Sum(3)) == Sum(5)



# Generated at 2022-06-14 03:51:59.804736
# Unit test for method __str__ of class Last
def test_Last___str__():
    actual = str(Last(2))
    expected = 'Last[value=2]'
    assert actual == expected, 'Expected calling __str__ on Last to equal {}, got {}'.format(
        expected, actual
    )


# Generated at 2022-06-14 03:52:04.941866
# Unit test for constructor of class Min
def test_Min():
    assert Min(1).concat(Min(2)) == Min(1)
    assert Min(3).concat(Min(-3)) == Min(-3)
    assert Min(-2).concat(Min(-1)) == Min(-2)
    assert Min(3).concat(Min(3)) == Min(3)



# Generated at 2022-06-14 03:52:07.020996
# Unit test for method __str__ of class Min
def test_Min___str__():
    assert Min(2).__str__() == "Min[value=2]"

# Generated at 2022-06-14 03:52:23.256645
# Unit test for method __str__ of class Last
def test_Last___str__():
    assert str(Last(5)) == 'Last[value=5]'

# Generated at 2022-06-14 03:52:25.820414
# Unit test for method concat of class First
def test_First_concat():
    actual = First("bar").concat(First("foo"))
    expected = First("bar")
    assert actual == expected


# Generated at 2022-06-14 03:52:26.535317
# Unit test for constructor of class Max
def test_Max():
    assert Max(1).value == 1



# Generated at 2022-06-14 03:52:28.535204
# Unit test for method __str__ of class One
def test_One___str__():
    fake = One(True)
    assert str(fake) == 'One[value={}]'.format(fake.value)


# Generated at 2022-06-14 03:52:31.004787
# Unit test for method __str__ of class Min
def test_Min___str__():
    assert str(Min(1)) == 'Min[value=1]'


# Generated at 2022-06-14 03:52:33.921996
# Unit test for method concat of class Last
def test_Last_concat():
    # arrange
    semigroup = Last(1)

    # act
    result = semigroup.concat(Last(2))

    # assert
    assert result == Last(2)


# Generated at 2022-06-14 03:52:40.550062
# Unit test for method concat of class All
def test_All_concat():
    All(True).concat(All(True)) == All(True)
    All(True).concat(All(False)) == All(False)
    All(False).concat(All(True)) == All(False)
    All(False).concat(All(False)) == All(False)


# Generated at 2022-06-14 03:52:48.914410
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    assert Sum(1).fold(lambda x: x + 1) == 2
    assert All(True).fold(lambda x: x) == True
    assert All(False).fold(lambda x: x and True) == False
    assert All(True).fold(lambda x: x or True) == True
    assert One(False).fold(lambda x: x or True) == True
    assert One(False).fold(lambda x: x or False) == False
    assert First(1).fold(lambda x: x + 1) == 1
    assert Last(1).fold(lambda x: x + 1) == 2
    assert Max(1).fold(lambda x: x + 1) == 2
    assert Min(1).fold(lambda x: x + 1) == 1



# Generated at 2022-06-14 03:52:51.342072
# Unit test for method __str__ of class Map
def test_Map___str__():
    assert str(Map({'numbers': Sum(10)})) == "Map[value={'numbers': Sum[value=10]}]"

# Generated at 2022-06-14 03:52:55.435496
# Unit test for method concat of class Sum
def test_Sum_concat():
    a = Sum(1)
    b = Sum(2)
    expected = Sum(3)
    actual = a.concat(b)
    assert actual == expected


# Generated at 2022-06-14 03:53:29.084075
# Unit test for method concat of class Sum
def test_Sum_concat():
  assert Sum.concat(Sum(1), Sum(2)).value == 3


# Generated at 2022-06-14 03:53:30.530531
# Unit test for method __str__ of class Min
def test_Min___str__():
    assert str(Min(1)) == 'Min[value=1]'


# Generated at 2022-06-14 03:53:35.540045
# Unit test for method concat of class First
def test_First_concat():
    A = First('a')
    B = First('b')

    assert A.concat(B) == First('a')
    assert A.concat(A) == First('a')
    assert B.concat(A) == First('b')
    assert B.concat(B) == First('b')



# Generated at 2022-06-14 03:53:38.169841
# Unit test for method __str__ of class Max
def test_Max___str__():
    result = Max(3).__str__()
    expected = 'Max[value=3]'

    assert result == expected, 'expected {} but got {}'.format(expected, result)


# Generated at 2022-06-14 03:53:39.360499
# Unit test for constructor of class First
def test_First():
    first = First("123")
    assert first.value == "123"


# Generated at 2022-06-14 03:53:41.809314
# Unit test for method concat of class Map
def test_Map_concat():
    a = Map({'a': Sum(1)})
    b = Map({'b': Sum(2)})
    assert a.concat(b).value == {'a': Sum(1), 'b': Sum(2)}

# Generated at 2022-06-14 03:53:43.576613
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert 'Max[value=0]' == str(Max(0))


# Generated at 2022-06-14 03:53:44.608583
# Unit test for constructor of class Last
def test_Last():
    assert Last(2).value == 2


# Generated at 2022-06-14 03:53:50.782266
# Unit test for method __str__ of class One
def test_One___str__():
    assert str(One(True))    == 'One[value=True]'
    assert str(One(False))   == 'One[value=False]'
    assert str(One(None))    == 'One[value=None]'
    assert str(One(4))       == 'One[value=4]'
    assert str(One("test"))  == 'One[value=test]'


# Generated at 2022-06-14 03:53:52.297080
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    assert str(Sum(10)) == 'Sum[value=10]'
