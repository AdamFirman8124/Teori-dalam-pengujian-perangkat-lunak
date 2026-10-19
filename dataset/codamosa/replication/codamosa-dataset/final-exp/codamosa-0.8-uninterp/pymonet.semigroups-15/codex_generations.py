

# Generated at 2022-06-14 03:44:37.396430
# Unit test for method concat of class Map
def test_Map_concat():
    expected = Map({
        "name": First("John"),
        "age": Last(30)
    })
    actual = \
        Map({
            "name": First("John"),
            "age": Last(20)
        }).concat(
            Map({
                "name": First("Mary"),
                "age": Last(30)
            }))
    assert actual == expected


# Generated at 2022-06-14 03:44:39.616888
# Unit test for method concat of class Max
def test_Max_concat():
    """
    Test for concat method of class Max
    """
    assert Max(1).concat(Max(2)) == Max(2)



# Generated at 2022-06-14 03:44:43.546108
# Unit test for method concat of class Max
def test_Max_concat():
    """
    Test definition: Assert that when 2 Max values concat, the resulting Max is the
    highest of the 2.
    """
    assert Max(1).concat(Max(2)).value == 2



# Generated at 2022-06-14 03:44:49.634462
# Unit test for method concat of class Map
def test_Map_concat():
    m1 = Map({
        'foo': Sum(3),
    })
    m2 = Map({
        'foo': Sum(5),
        'bar': Sum(2),
    })

    assert m1.concat(m2).value == {
        'foo': Sum(8),
        'bar': Sum(2),
    }



# Generated at 2022-06-14 03:44:54.470578
# Unit test for method concat of class Map
def test_Map_concat():
    m1 = Map({1: First(1), 2: First(2)})
    m2 = Map({1: First(3), 2: First(4)})
    m3 = Map({1: First(5), 2: First(6)})
    assert first(m1.concat(m2).concat(m3).fold(values)) == [1, 2, 5, 6]

# Generated at 2022-06-14 03:44:57.986160
# Unit test for method concat of class Max
def test_Max_concat():
    monoid_1 = Max(4)
    monoid_2 = Max(3)
    monoid_3 = monoid_1.concat(monoid_2)
    print(monoid_3)

# Generated at 2022-06-14 03:45:08.890563
# Unit test for method concat of class Map
def test_Map_concat():
    """
    :returns: None
    :rtype: None
    """

    map1 = Map({
        0: Sum(1),
        1: Sum(2),
        2: Sum(3)
    })
    map2 = Map({
        0: Sum(4),
        1: Sum(5),
        2: Sum(6)
    })

    assert(
        Map(
            {
                0: Sum(5),
                1: Sum(7),
                2: Sum(9)
            }
        )
        ==
        map1.concat(map2)
    )


# Generated at 2022-06-14 03:45:16.463447
# Unit test for method concat of class Map
def test_Map_concat():
    map_one = Map({'a': Sum(1), 'b': Sum(4), 'c': Sum(987)})
    map_two = Map({'a': Sum(2), 'b': Sum(5), 'c': Sum(1)})

    expected_map = Map({'a': Sum(3), 'b': Sum(9), 'c': Sum(988)})

    assert map_one.concat(map_two) == expected_map

# Generated at 2022-06-14 03:45:21.253837
# Unit test for method concat of class Map
def test_Map_concat():  # pragma: no cover
    value_one = Map({'a': Sum(1)})
    value_two = Map({'a': Sum(2)})

    assert value_one.concat(value_two) == Map({'a': Sum(3)})

# Generated at 2022-06-14 03:45:25.962710
# Unit test for method concat of class Map
def test_Map_concat():
    right = Map({1: Sum(3), 2: Sum(4)})
    left = Map({1: Sum(1), 2: Sum(2)})
    result = Map({1: Sum(4), 2: Sum(6)})
    assert left.concat(right) == result


# Generated at 2022-06-14 03:45:30.476507
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(42).concat(Min(39)).value == 39
    assert Min(42).concat(Min(42)).value == 42
    assert Min(42).concat(Min(43)).value == 42

# Generated at 2022-06-14 03:45:31.891740
# Unit test for method __str__ of class Map
def test_Map___str__(): pass  # pragma: no cover


# Generated at 2022-06-14 03:45:34.439093
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():  # pragma: no cover
    """
    :returns: __eq__ method test result
    :rtype: bool
    """
    return Sum(1) == Sum(1)


# Generated at 2022-06-14 03:45:35.530070
# Unit test for constructor of class Sum
def test_Sum():
    sum = Sum(10)
    assert sum.value == 10


# Generated at 2022-06-14 03:45:39.756475
# Unit test for constructor of class Map
def test_Map():
    semigroup = Map({'a': First(1), 'b': Min(3)})
    assert semigroup.value == {'a': First(1), 'b': Min(3)}



# Generated at 2022-06-14 03:45:41.681936
# Unit test for method __str__ of class All
def test_All___str__():
    assert str(All(True)) == 'All[value=True]'
    assert str(All(False)) == 'All[value=False]'

# Generated at 2022-06-14 03:45:42.484413
# Unit test for method concat of class Last
def test_Last_concat():
    pass



# Generated at 2022-06-14 03:45:46.882225
# Unit test for method concat of class Map
def test_Map_concat():
    assert Map({"a": Sum(1), "b": Sum(1)}).concat(Map({"a": Sum(2), "b": Sum(3)})) == Map(
        {"a": Sum(3), "b": Sum(4)}
    )

# Generated at 2022-06-14 03:45:48.835193
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():  # pragma: no cover
    assert Sum(1).fold(
        lambda acc: acc + 1
    ) == 2



# Generated at 2022-06-14 03:45:49.920950
# Unit test for constructor of class Min
def test_Min():
    assert Min(1).value == 1


# Generated at 2022-06-14 03:45:53.922561
# Unit test for constructor of class Last
def test_Last():
    assert Last(1) == Last(1)
    assert Last(1) != Last(2)


# Generated at 2022-06-14 03:45:57.675517
# Unit test for method concat of class One
def test_One_concat():
    assert One(False).concat(One(True)) == One(True)
    assert One(True).concat(One(False)) == One(True)
    assert One(False).concat(One(False)) == One(False)



# Generated at 2022-06-14 03:46:08.628393
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    assert Sum(1000) == Sum(1000)
    assert All(True) == All(True)
    assert One(True) == One(True)
    assert First(100) == First(100)
    assert Last(100) == Last(100)
    assert Map({'a': Sum(100)}) == Map({'a': Sum(100)})
    assert Max(100) == Max(100)
    assert Min(100) == Min(100)

    assert Sum(1000) != Sum(0)
    assert All(True) != All(False)
    assert One(True) != One(False)
    assert First(100) != First(1)
    assert Last(100) != Last(1)
    assert Map({'a': Sum(100)}) != Map({'a': Sum(101)})

# Generated at 2022-06-14 03:46:14.159867
# Unit test for method concat of class All
def test_All_concat():
    assert All(True).concat(All(True)) == All(True)
    assert All(True).concat(All(False)) == All(False)
    assert All(False).concat(All(True)).value is False
    assert All(False).concat(All(False)).value is False



# Generated at 2022-06-14 03:46:16.139268
# Unit test for method __str__ of class All
def test_All___str__():
    assert str(All(False)) == 'All[value=False]'
    assert str(All(True)) == 'All[value=True]'



# Generated at 2022-06-14 03:46:23.783888
# Unit test for method concat of class Map
def test_Map_concat():
    assert Map({"a": Sum(1), "b": Sum(3)}).concat(Map({"b": Sum(5), "a": Sum(2)})) == Map({"a": Sum(3), "b": Sum(8)})
    assert Map({}).concat(Map({"a": Sum(1), "b": Sum(3)})) == Map({"a": Sum(1), "b": Sum(3)})
    assert Map({"a": Sum(1), "b": Sum(3)}).concat(Map({})) == Map({"a": Sum(1), "b": Sum(3)})

# Generated at 2022-06-14 03:46:26.596548
# Unit test for method __str__ of class All
def test_All___str__():
    assert str(All(True)) == "All[value=True]"
    assert str(All(False)) == "All[value=False]"


# Generated at 2022-06-14 03:46:30.506332
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    assert Semigroup(1) == Semigroup(1)
    assert not Semigroup(1) == Semigroup(2)
    assert not Semigroup(1) == Semigroup('1')

# Generated at 2022-06-14 03:46:32.607690
# Unit test for constructor of class First
def test_First():
    # Given
    first = First('a')
    # When & Then
    assert first.value == 'a'


# Generated at 2022-06-14 03:46:34.732624
# Unit test for method __str__ of class One
def test_One___str__():
    assert str(One(True)) == 'One[value=True]'
    assert str(One(False)) == 'One[value=False]'
    assert str(One(42)) == 'One[value=42]'
    assert str(One('foo')) == 'One[value=foo]'
    assert str(One(None)) == 'One[value=None]'

# Generated at 2022-06-14 03:46:41.624310
# Unit test for method concat of class Min
def test_Min_concat():
    a = Min(-10)
    b = Min(-20)
    print(a.concat(b))
    print(b.concat(a))
    
test_Min_concat()



# Generated at 2022-06-14 03:46:51.582813
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    assert Sum(1).fold(lambda x: x + x) == 2
    assert All(True).fold(lambda x: not x) is False
    assert One(True).fold(lambda x: not x) is True
    assert First("hello").fold(lambda x: x + "!") == "hello!"
    assert Last("hello").fold(lambda x: x + "!") == "hello!"
    assert Max(5).fold(lambda x: x - 1) == 4
    assert Min(5).fold(lambda x: x - 1) == 4


# Generated at 2022-06-14 03:46:55.437750
# Unit test for constructor of class First
def test_First():
    assert First(1) == First(1)
    assert First(1) != First(2)
    assert First(1).concat(First(2)) == First(1)
    assert First(1).concat(First(None)) == First(1)
    assert First(None).concat(First(2)) == First(2)



# Generated at 2022-06-14 03:47:04.996263
# Unit test for method concat of class Map
def test_Map_concat():
    # Create container with semigroup
    test_map = {"first": Sum(1), "second": Sum(2), "third": Sum(3)}
    test_map2 = {"first": Sum(4), "second": Sum(5), "third": Sum(6)}

    # First map
    assert str(Map(test_map)) == 'Map[value={"first": Sum[value=1], "second": Sum[value=2], "third": Sum[value=3]}]'

    # Second map
    assert str(Map(test_map2)) == 'Map[value={"first": Sum[value=4], "second": Sum[value=5], "third": Sum[value=6]}]'

    # Concat two map with semigroups
    concat_maps = Map(test_map).concat(Map(test_map2))
   

# Generated at 2022-06-14 03:47:10.457715
# Unit test for constructor of class Max
def test_Max():
    assert Max(1) == Max(1)
    assert Max(1).value == 1
    assert Max(1).concat(Max(2)) == Max(2)
    assert Max(5).concat(Max(4)) == Max(5)
    assert Max(4).concat(Max(5)) == Max(5)
    assert Max(1).fold(lambda x: x) == 1


# Generated at 2022-06-14 03:47:14.567065
# Unit test for method concat of class All
def test_All_concat():
    # given
    all1 = All(True)
    all2 = All(True)

    # when
    result = all1.concat(all2)

    # then
    assert result.value



# Generated at 2022-06-14 03:47:16.084664
# Unit test for constructor of class Semigroup
def test_Semigroup():
    assert Semigroup('a') == Semigroup('a')



# Generated at 2022-06-14 03:47:20.744414
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    a = Semigroup(5)
    b = Semigroup(5)
    c = Semigroup(6)
    assert a == a
    assert a == b
    assert a != c
    assert b == a
    assert b == b
    assert b != c
    assert c == c
    assert c != a
    assert c != b


# Generated at 2022-06-14 03:47:22.028029
# Unit test for constructor of class First
def test_First():
    assert First(3) == First(3)

# Generated at 2022-06-14 03:47:23.674625
# Unit test for method __str__ of class One
def test_One___str__():  # pragma: no cover
    assert str(One(True)) == 'One[value=True]'



# Generated at 2022-06-14 03:47:32.196377
# Unit test for method __str__ of class First
def test_First___str__():  # pragma: no cover
    f = First(1)

    assert f.__str__() == 'Fist[value=1]'

# Generated at 2022-06-14 03:47:37.909254
# Unit test for method concat of class One
def test_One_concat():
    assert One(True).concat(One(True)).value is True
    assert One(True).concat(One(False)).value is True
    assert One(False).concat(One(True)).value is True
    assert One(False).concat(One(False)).value is False


# Generated at 2022-06-14 03:47:47.369488
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    # Semigroup - Sum
    assert Sum(1).fold(lambda a: a + 2) == 3
    # Semigroup - All
    assert All(True).fold(lambda a: a)
    # Semigroup - One
    assert One(False).fold(lambda a: a)
    # Semigroup - First
    assert First("hello").fold(lambda a: a) == "hello"
    # Semigroup - Last
    assert Last("world").fold(lambda a: a) == "world"
    # Semigroup - Max
    assert Max(2).fold(lambda a: a) == 2
    # Semigroup - Min
    assert Min(1).fold(lambda a: a) == 1



# Generated at 2022-06-14 03:47:49.028567
# Unit test for method concat of class All
def test_All_concat():
    """
    It should return true if both All puttro are true
    """
    assert All(True).concat(All(True)).value == True


# Generated at 2022-06-14 03:47:50.941010
# Unit test for method __str__ of class Last
def test_Last___str__():
    assert "Last[value=1]" == Last(1).__str__()


# Generated at 2022-06-14 03:47:52.732005
# Unit test for method concat of class Sum
def test_Sum_concat():
    assert Sum(1).concat(Sum(0)) == Sum(1)



# Generated at 2022-06-14 03:47:56.054081
# Unit test for method concat of class Last
def test_Last_concat():
    assert Last(1).concat(Last(2)).value == 2



# Generated at 2022-06-14 03:47:57.088903
# Unit test for method __str__ of class Min
def test_Min___str__():
    assert str(Min(1)) == 'Min[value=1]'


# Generated at 2022-06-14 03:48:05.318178
# Unit test for method concat of class First
def test_First_concat():
    f_new = First(1).concat(First(0))
    assert f_new.value == 1
    f_new = First(True).concat(First(False))
    assert f_new.value is True
    f_new = First('foo').concat(First('bar'))
    assert f_new.value == 'foo'
    f_new = First([1,2,3]).concat(First([4,5,6]))
    assert f_new.value == [1,2,3]


# Generated at 2022-06-14 03:48:10.445417
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(1).concat(Max(5)) == Max(5)
    assert Max(1).concat(Max(1)) == Max(1)
    assert Max(3).concat(Max(1)) == Max(3)
    assert Max(1).concat(Max(2)) == Max(2)

# Generated at 2022-06-14 03:48:24.943997
# Unit test for constructor of class Semigroup
def test_Semigroup():
    assert Semigroup(7) == Semigroup(7)
    assert Semigroup(3) != Semigroup(7)


# Generated at 2022-06-14 03:48:26.230969
# Unit test for method __str__ of class Min
def test_Min___str__():
    assert str(Min(1)) == 'Min[value=1]'
    assert repr(Min(1)) == 'Min[value=1]'


# Generated at 2022-06-14 03:48:26.958134
# Unit test for constructor of class One
def test_One():
    o = One(True)
    assert o.value == True



# Generated at 2022-06-14 03:48:28.747802
# Unit test for constructor of class Last
def test_Last():
    """
    >>> a = Last('foo')
    >>> a.value
    'foo'
    """



# Generated at 2022-06-14 03:48:36.710842
# Unit test for method __str__ of class One
def test_One___str__():
    assert 'One[value=True]' == str(One(True))
    assert 'One[value=False]' == str(One(False))
    assert 'One[value=0]' == str(One(0))
    assert 'One[value=1]' == str(One(1))
    assert 'One[value=0.0]' == str(One(0.0))
    assert 'One[value=1.0]' == str(One(1.0))
    assert 'One[value=None]' == str(One(None))
    assert 'One[value=1]' == str(One('1'))


# Generated at 2022-06-14 03:48:42.058814
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    assert Semigroup(10).fold(lambda x: x * 10) == 100
    assert Semigroup(0.1).fold(lambda x: x * 10) == 1
    assert Semigroup([]).fold(lambda x: x + [100]) == [100]

# Generated at 2022-06-14 03:48:43.509922
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(10)) == "Max[value=10]"


# Generated at 2022-06-14 03:48:48.358071
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    semigroup_a = Semigroup(1)
    semigroup_b = Semigroup(1)
    semigroup_c = Semigroup(2)
    assert semigroup_a == semigroup_b
    assert semigroup_a != semigroup_c


# Generated at 2022-06-14 03:48:51.371270
# Unit test for method __str__ of class Last
def test_Last___str__():
    """
    :return:
    :rtype:
    """

    assert str(Last(1)) == "Last[value=1]"



# Generated at 2022-06-14 03:48:53.520462
# Unit test for method __str__ of class All
def test_All___str__():
    assert str(All(True)) == "All[value=True]"
    assert str(All(False)) == "All[value=False]"


# Generated at 2022-06-14 03:49:20.715212
# Unit test for method concat of class Last
def test_Last_concat():
    assert Last(1).concat(Last(2)) == Last(2)
    assert Last(1).concat(Last(0)) == Last(0)


# Generated at 2022-06-14 03:49:31.211299
# Unit test for constructor of class Sum
def test_Sum():
    assert Sum(2).concat(Sum(3)).value == 5
    assert Sum(2).concat(Sum(3)).fold(lambda x: x) == 5
    assert Sum(2) == Sum(2)
    assert Sum(2) != Sum(3)
    assert not Sum(2) == Sum(3)
    assert Sum(2) != 3
    assert 3 != Sum(2)
    assert Sum(2) != 'string'
    assert 'string' != Sum(2)
    assert Sum(2) != {"key": 3}
    assert {"key": 3} != Sum(2)
    assert Sum(0) == Sum.neutral()


# Generated at 2022-06-14 03:49:33.016428
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(1)) == 'Max[value=1]'


# Generated at 2022-06-14 03:49:35.196274
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(1)) == 'Max[value=1]'


# Generated at 2022-06-14 03:49:39.532120
# Unit test for method concat of class Last
def test_Last_concat():
    assert Last(1).concat(Last(2)) == Last(2)
    assert Last(1).concat(Last(-1)) == Last(-1)
    assert Last(1).concat(Last(1)) == Last(1)


# Generated at 2022-06-14 03:49:42.226050
# Unit test for constructor of class Min
def test_Min():
    x = Min(7)
    y = Min(10)
    z = Min(3)
    assert(x.concat(y).concat(z).value == 3)


# Generated at 2022-06-14 03:49:45.875765
# Unit test for constructor of class First
def test_First():
    assert First(0).value == 0
    assert First(None).value is None
    assert First('hello').value == 'hello'
    assert First('hello').value != 'hello world'
    assert First(['hello', 'first']).value == ['hello', 'first']

    first_tuple = First(('hello', 'first'))
    assert first_tuple.value != ('hello', 'world')


# Generated at 2022-06-14 03:49:47.722354
# Unit test for method __str__ of class Min
def test_Min___str__():
    assert str(Min(0)) == 'Min[value=0]'

# Generated at 2022-06-14 03:49:49.155040
# Unit test for method __str__ of class All
def test_All___str__():
    assert str(All(False)) == 'All[value=False]'



# Generated at 2022-06-14 03:49:51.171029
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(10)) == 'Max[value=10]'
    assert str(Max(0)) == 'Max[value=0]'


# Generated at 2022-06-14 03:50:40.257165
# Unit test for constructor of class All
def test_All():
    assert All(True)



# Generated at 2022-06-14 03:50:44.092358
# Unit test for method __str__ of class Map
def test_Map___str__():
    assert str(Map({1: Sum(1), 2: Sum(2)})) == 'Map[value={1: Sum[value=1], 2: Sum[value=2]}]'


# Generated at 2022-06-14 03:50:46.260266
# Unit test for method concat of class Sum
def test_Sum_concat():  # pragma: no cover
    assert Sum(1).concat(Sum(2)).value == 3


# Generated at 2022-06-14 03:50:57.114522
# Unit test for constructor of class One
def test_One():
    class One(Semigroup):
        neutral_element = False

        def __str__(self) -> str:
            return 'One[value={}]'.format(self.value)

        def concat(self, semigroup):
            return One(self.value or semigroup.value)
    # testing assertion value
    assert One(1).value == 1
    assert One(0).value == 0
    # testing assertion class return
    assert One(1).concat(One(1)).value
    assert One(0).concat(One(1)).value
    assert One(0).concat(One(0)).value == 0
    assert One(1).concat(One(0)).value

# Generated at 2022-06-14 03:51:00.591187
# Unit test for constructor of class Max
def test_Max():
    instance = Max(1)
    assert isinstance(instance.value, int)
    assert instance.value == 1
    instance = Max(2.2)
    assert isinstance(instance.value, float)
    assert instance.value == 2.2


# Generated at 2022-06-14 03:51:08.130841
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    assert Sum(10).fold(float) == 10
    assert All(True).fold(float) == 1
    assert All(False).fold(float) == 0
    assert One(True).fold(float) == 1
    assert One(False).fold(float) == 0
    assert First(False).fold(float) == 0
    assert Last(True).fold(float) == 1
    assert Map({1: Sum(10), 1: Sum(20)}).fold(float) == {1: 30}
    assert Max(15).fold(float) == 15
    assert Min(15).fold(float) == 15


# Generated at 2022-06-14 03:51:19.938692
# Unit test for method __str__ of class Map
def test_Map___str__():
    assert str(Map({1: Sum(1), 2: Sum(2)})) == 'Map[value={1: Sum[value=1], 2: Sum[value=2]}]'
    assert str(Map({1: Sum(1), 2: All(True)})) == 'Map[value={1: Sum[value=1], 2: All[value=True]}]'
    assert str(Map({1: Sum(1), 2: First(1)})) == 'Map[value={1: Sum[value=1], 2: Fist[value=1]}]'
    assert str(Map({1: Sum(1), 2: Last(1)})) == 'Map[value={1: Sum[value=1], 2: Last[value=1]}]'

# Generated at 2022-06-14 03:51:22.112449
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    assert 'Sum[value=1]' == str(Sum(1))


# Generated at 2022-06-14 03:51:24.928015
# Unit test for method __str__ of class One
def test_One___str__():  # pragma: no cover
    assert str(One(True)) == 'One[value=True]'



# Generated at 2022-06-14 03:51:29.538010
# Unit test for method __str__ of class Sum
def test_Sum___str__():  # pragma: no cover
    assert str(Sum(0)) == 'Sum[value=0]'
    assert str(Sum(1)) == 'Sum[value=1]'
    assert str(Sum(-1)) == 'Sum[value=-1]'


# Generated at 2022-06-14 03:53:26.241211
# Unit test for constructor of class Last
def test_Last():
    assert Last(1) == Last(1)
    assert Last(2) == Last(2)
    assert Last(5) == Last(5)
    assert Last(4) == Last(4)
    assert Last(7) == Last(7)
    assert Last(1) != Last(2)
    assert Last(1) != Last(5)
    assert Last(2) != Last(4)
    assert Last(1) != Last(4)
    assert Last(5) != Last(7)


# Generated at 2022-06-14 03:53:30.580657
# Unit test for constructor of class One
def test_One():
    assert One(True) == One(True)
    assert One(True) == One(False)
    assert One(False) == One(False)
    assert One(True) == One(True)


# Generated at 2022-06-14 03:53:31.222898
# Unit test for method __str__ of class Last
def test_Last___str__():
    assert str(Last(1)) == 'Last[value=1]'


# Generated at 2022-06-14 03:53:32.904627
# Unit test for method __str__ of class Last
def test_Last___str__():
    assert str(Last(1)) == 'Last[value=1]'


# Generated at 2022-06-14 03:53:34.711413
# Unit test for method concat of class Last
def test_Last_concat():
    assert Last(False).concat(Last(False)) == Last(False)



# Generated at 2022-06-14 03:53:37.938954
# Unit test for method __str__ of class Map
def test_Map___str__():
    m1 = Map({'a': Min(1), 'b': All(True)})
    assert str(m1) == "Map[value={'a': Min[value=1], 'b': All[value=True]}]"


# Generated at 2022-06-14 03:53:40.164210
# Unit test for constructor of class One
def test_One():
    assert One('David').value == 'David'
    assert One(1).value == 1
    assert One(0).value == 0
    assert One(False).value == False


# Generated at 2022-06-14 03:53:42.173208
# Unit test for constructor of class Min
def test_Min():
    a = Min(12)
    assert type(a) == Min
    assert a.value == 12



# Generated at 2022-06-14 03:53:46.499078
# Unit test for constructor of class Map
def test_Map():
    assert Map({1: Sum(1), 2: Sum(2)}) == Map({1: Sum(1), 2: Sum(2)})
    assert Map({1: Sum(1), 2: Sum(2)}) != Map({1: Sum(2), 2: Sum(2)})


# Generated at 2022-06-14 03:53:48.094448
# Unit test for constructor of class Min
def test_Min():
    f = Min(3)
    assert f.value == 3
