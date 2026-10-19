

# Generated at 2022-06-14 03:44:38.365455
# Unit test for method concat of class Map
def test_Map_concat():
    """
    :returns: test result
    :rtype: bool
    """
    assert Map({'a': Min(3), 'b': First(5)}).concat(Map({'a': Min(1),
                                                        'b': First(2)})) == Map(
        {'a': Min(1), 'b': First(5)}
    )

# Generated at 2022-06-14 03:44:42.283329
# Unit test for method concat of class Min
def test_Min_concat():

    x = Min(2)
    y = Min(3)
    z = x.concat(y)

    assert z.value == 2


# Generated at 2022-06-14 03:44:52.515219
# Unit test for method concat of class Map
def test_Map_concat(): # pragma: no cover
    assert_that(
        Map({"x": "y"}).concat(Map({"x": "z"})),
        equal_to(Map({"x": "yz"}))
    )
    assert_that(
        Map({"x": "y", "z": "w"}).concat(Map({"x": "z", "z": "t"})),
        equal_to(Map({"x": "yz", "z": "wt"}))
    )

# Generated at 2022-06-14 03:45:01.220464
# Unit test for method concat of class Map
def test_Map_concat():
    m1 = {'name': Sum(1), 'age': Min(32)}
    m2 = {'name': Sum(2), 'age': Min(34)}
    m3 = {'name': Sum(3), 'age': Min(33)}
    m4 = Map(m1)
    m5 = Map(m2)
    m6 = Map(m3)
    m7 = m4.concat(m5.concat(m6))
    expected = {'name': Sum(6), 'age': Min(32)}
    assert m7.value == expected

test_Map_concat()


# Generated at 2022-06-14 03:45:05.182715
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(1).concat(Min(3)) == Min(1)
    assert Min(3).concat(Min(1)) == Min(1)


# Generated at 2022-06-14 03:45:06.813005
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(2).concat(Min(1)) == Min(1)

# Generated at 2022-06-14 03:45:10.566294
# Unit test for method concat of class Map
def test_Map_concat():
    assert Map({'a': Sum(1), 'b': Sum(1)}).concat(Map({'a': Sum(1), 'b': Sum(1)})).value == {'a': Sum(2), 'b': Sum(2)}



# Generated at 2022-06-14 03:45:13.227459
# Unit test for method concat of class Map
def test_Map_concat():
    assert Map({"a": First(1), "b": First(2)}).concat(Map({"a": First(3), "b": First(4)})).value == {"a": First(1), "b": First(2)}

# Generated at 2022-06-14 03:45:17.026954
# Unit test for method concat of class Map
def test_Map_concat():
    a = Map({'a': Sum(1), 'b': All(True)})
    b = Map({'a': Sum(2), 'b': All(True), 'c': One(False)})
    assert a.concat(b) == Map({'a': Sum(3), 'b': All(True), 'c': One(False)})


if __name__ == "__main__":
    test_Map_concat()

# Generated at 2022-06-14 03:45:24.100386
# Unit test for method concat of class Map
def test_Map_concat():
    mapSemigroup = Map({'a': First(1), 'b': First(2), 'c': First(3)})
    mapSemigroup2 = Map({'a': Last(4), 'b': Last(5), 'c': Last(6)})
    expected = Map({'a': First(1), 'b': First(2), 'c': First(3)})
    assert mapSemigroup.concat(mapSemigroup2) == expected

# Generated at 2022-06-14 03:45:27.811407
# Unit test for method concat of class First
def test_First_concat():  # pragma: no cover
    assert First('a').concat(First('b')) == First('a'), 'First always returns the first'


# Generated at 2022-06-14 03:45:34.478696
# Unit test for constructor of class All
def test_All():
    # Test for falsy values
    for v in [False, [], {}, 0, b'', '', (), None]:
        all_ = All(v)
        assert all_.value == v
        assert all_.fold(lambda x: x) == v

    # Test for truly values
    for v in [True, [1], ['1'], {1}, 1, b'1', '1', (1, )]:
        all_ = All(v)
        assert all_.value == v
        assert all_.fold(lambda x: x) == v


# Generated at 2022-06-14 03:45:37.529366
# Unit test for constructor of class All
def test_All():
    obj_1 = All(True)
    obj_2 = All(True)
    obj_3 = All(False)
    assert obj_1.__eq__(obj_2) == True
    assert obj_1.__eq__(obj_3) == False


# Generated at 2022-06-14 03:45:40.867477
# Unit test for method __str__ of class One
def test_One___str__():
    a = One(True)
    b = One(False)
    assert str(a) == "One[value=True]"
    assert str(b) == "One[value=False]"



# Generated at 2022-06-14 03:45:42.851449
# Unit test for method concat of class Last
def test_Last_concat():
    """
    Function that tests concat method of class Last.
    """
    assert Last(1).concat(Last(2)) == Last(2)



# Generated at 2022-06-14 03:45:48.334639
# Unit test for method concat of class Last
def test_Last_concat():
    assert Last(1).concat(Last(2)) == Last(2)
    assert Last(1).concat(Last(0)) == Last(0)
    assert Last([1]).concat(Last([2])) == Last([2])
    assert Last([1]).concat(Last([3])) == Last([3])


# Generated at 2022-06-14 03:45:49.897059
# Unit test for method __str__ of class Last
def test_Last___str__():
    assert 'Last[value=1]' == str(Last(1))


# Generated at 2022-06-14 03:45:52.923161
# Unit test for constructor of class Min
def test_Min():
    """Unit test to test constructor of class Min
    """
    assert Min(3) == Min(3)

# Generated at 2022-06-14 03:45:58.855221
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    assert Sum(1) == Sum(1)
    assert All(True) == All(True)
    assert One(True) == One(True)
    assert First(1) == First(1)
    assert Last(1) == Last(1)
    assert Map({}) == Map({})
    assert Min(1) == Min(1)
    assert Max(1) == Max(1)



# Generated at 2022-06-14 03:46:02.261051
# Unit test for constructor of class Map
def test_Map():
    assert Map({"key": Sum(1)}).value == {"key": Sum(1)}



# Generated at 2022-06-14 03:46:10.729741
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    # Semigroup(None) == Semigroup(None)
    assert Semigroup(None) == Semigroup(None)

    # Semigroup(1) == Semigroup(1)
    assert Semigroup(1) == Semigroup(1)

    # Semigroup("world") == Semigroup("world")
    assert Semigroup("world") == Semigroup("world")

    # Semigroup([1, 2, 3]) == Semigroup([1, 2, 3])
    assert Semigroup([1, 2, 3]) == Semigroup([1, 2, 3])



# Generated at 2022-06-14 03:46:14.656544
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    assert str(Sum(1)) == 'Sum[value=1]'
    assert str(Sum(2.2)) == 'Sum[value=2.2]'
    assert str(Sum("a")) == 'Sum[value=a]'


# Generated at 2022-06-14 03:46:15.944095
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(1).concat(Sum(5)) == Max(1)


# Generated at 2022-06-14 03:46:16.960020
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(1)) == 'Max[value=1]'


# Generated at 2022-06-14 03:46:19.502097
# Unit test for method __str__ of class First
def test_First___str__():
    first = First('foo')
    assert str(first) == 'Fist[value=foo]'


# Generated at 2022-06-14 03:46:22.940496
# Unit test for constructor of class Semigroup
def test_Semigroup():
    try:
        Semigroup("value")
    except Exception as e:
        raise AssertionError("Can't call constructor of class Semigroup") from e



# Generated at 2022-06-14 03:46:27.032585
# Unit test for method concat of class All
def test_All_concat():
    assert All(True).concat(All(False)) == All(False)
    assert All(True).concat(All(True)) == All(True)
    assert All(False).concat(All(True)) == All(False)
    assert All(False).concat(All(False)) == All(False)


# Generated at 2022-06-14 03:46:29.853804
# Unit test for constructor of class Map
def test_Map():
    """
    Unit test for constructor of class Map
    """
    assert Map({"test": Last(5)}) == Map({"test": Last(5)})



# Generated at 2022-06-14 03:46:33.503340
# Unit test for method concat of class Min
def test_Min_concat():
    min_ = Min(1)
    assert min_.concat(Min(2)).value == 1.0
    assert min_.concat(Min(1)).value == 1.0
    assert min_.concat(Min(0)).value == 0.0


# Generated at 2022-06-14 03:46:38.003906
# Unit test for constructor of class Min
def test_Min():
    min_1 = Min(1)
    min_2 = Min(2)
    assert isinstance(min_1.concat(min_2), Min)
    assert min_1.concat(min_2).value == 1
    assert min_2.concat(min_1).value == 1

# Generated at 2022-06-14 03:46:42.287964
# Unit test for constructor of class One
def test_One():
    assert One(True) == One(True)
    assert One(True) != One(False)
    assert One(False) != One(True)
    assert One(False) == One(False)



# Generated at 2022-06-14 03:46:48.726469
# Unit test for method concat of class All
def test_All_concat():
    """
    """
    fn = lambda x: x or True
    assert (All(False).concat(All(True))).fold(fn) == True
    assert (All(True).concat(All(False))).fold(fn) == False
    assert (All(False).concat(All(False))).fold(fn) == False



# Generated at 2022-06-14 03:46:52.036595
# Unit test for method __str__ of class Last
def test_Last___str__():
    l = Last(10)
    assert isinstance(l, Last)
    assert str(l) == 'Last[value=10]'


# Generated at 2022-06-14 03:47:02.973620
# Unit test for method __str__ of class Min
def test_Min___str__():
    """
    Unit test for method __str__ of class Min
    """


    assert (str(Min(1)) == 'Min[value=1]')
    assert (str(Min(2)) == 'Min[value=2]')
    assert (str(Min(3)) == 'Min[value=3]')
    assert (str(Min(4)) == 'Min[value=4]')
    assert (str(Min(5)) == 'Min[value=5]')
    assert (str(Min(6)) == 'Min[value=6]')
    assert (str(Min(7)) == 'Min[value=7]')
    assert (str(Min(8)) == 'Min[value=8]')
    assert (str(Min(9)) == 'Min[value=9]')

# Generated at 2022-06-14 03:47:05.948304
# Unit test for method __str__ of class All
def test_All___str__():
    assert str(All(True)) == 'All[value=True]'
    assert str(All(False)) == 'All[value=False]'



# Generated at 2022-06-14 03:47:07.806341
# Unit test for constructor of class Last
def test_Last():  # pragma: no cover
    assert Last(3) == Last(3)


# Generated at 2022-06-14 03:47:09.202489
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(1)) == 'Max[value=1]'


# Generated at 2022-06-14 03:47:14.721413
# Unit test for constructor of class All
def test_All():
    a = All(True)
    assert a.value is True
    assert a.fold(bool) is True

    b = All(False)
    assert b.value is False
    assert b.fold(bool) is False


# Generated at 2022-06-14 03:47:17.712792
# Unit test for constructor of class One
def test_One():
    assert One(2).value == 2
    assert One(0).value == 0
    assert One(4) == One(4)
    assert One(0) != One(1)


# Generated at 2022-06-14 03:47:19.895956
# Unit test for method __str__ of class One
def test_One___str__():
    instance = One(True)
    assert str(instance) == "One[value=True]"



# Generated at 2022-06-14 03:47:24.279609
# Unit test for method concat of class Map
def test_Map_concat():
    m1 = Map({'value': First(1)})
    m2 = Map({'value': First(2)})
    assert m1.concat(m2) == Map({'value': First(1)})


# Generated at 2022-06-14 03:47:29.940863
# Unit test for method __str__ of class One
def test_One___str__():
    sg = One(False)
    assert str(sg) == 'One[value=False]'

    sg = One(True)
    assert str(sg) == 'One[value=True]'



# Generated at 2022-06-14 03:47:39.513759
# Unit test for method concat of class Map
def test_Map_concat():
    """
    Test how Map concat 2 values
    """
    assert Map({"a": Sum(2)}).concat(Map({"a": Sum(2)})) == Map({"a": Sum(4)})
    assert Map({"a": Last("test")}).concat(Map({"a": Last("test_1")})) == Map({"a": Last("test_1")})
    assert Map({"a": First("test")}).concat(Map({"a": First("test_1")})) == Map({"a": First("test")})
    assert Map({"a": All(True)}).concat(Map({"a": All(True)})) == Map({"a": All(True)})

# Generated at 2022-06-14 03:47:40.984777
# Unit test for method __str__ of class Last
def test_Last___str__():
    assert str(Last("hello")) == 'Last[value=hello]'


# Generated at 2022-06-14 03:47:43.240581
# Unit test for method concat of class Sum
def test_Sum_concat():  # pragma: no cover
    assert Sum(1).concat(Sum(2)) == Sum(3)



# Generated at 2022-06-14 03:47:52.564655
# Unit test for method concat of class Max
def test_Max_concat():
    # Create some instances of class Max
    max1 = Max(2)
    max2 = Max(1)
    max3 = Max(3)

    # Check for equality
    assert max1.concat(max2).value == 2
    assert max2.concat(max1).value == 2
    assert max2.concat(max3).value == 3
    assert max3.concat(max1).value == 3
    assert max1.concat(max3).value == 3
    assert max3.concat(max2).value == 3



# Generated at 2022-06-14 03:47:55.170632
# Unit test for constructor of class One
def test_One():
    # Given
    semigroup = One(True)
    # When
    # Then
    assert isinstance(semigroup, One) == True
    assert semigroup.value == True


# Generated at 2022-06-14 03:47:56.612275
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(42)) == 'Max[value=42]'


# Generated at 2022-06-14 03:47:58.654289
# Unit test for constructor of class Min
def test_Min():
    assert Min(2) == Min(2)
    assert Min(4) == Min(4)
    assert Min(4) != All(4)
    assert Min(4) != Max(4)


# Generated at 2022-06-14 03:48:10.645414
# Unit test for method concat of class Max
def test_Max_concat():
    """
    Asserts every test cases of method concat
    """

    assert Max(8).concat(Max(9)) == Max(9)
    assert Max(8).concat(Max(-10)) == Max(8)
    assert Max(9.87).concat(Max(9.87)) == Max(9.87)
    assert Max(-5).concat(Max(-9)) == Max(-5)
    assert Max(-20).concat(Max(10)) == Max(10)
    assert Max(10.5).concat(Max(0.1)) == Max(10.5)
    assert Max(-99).concat(Max(-99)) == Max(-99)
    assert Max(-10).concat(Max(-10)) == Max(-10)

# Generated at 2022-06-14 03:48:13.121725
# Unit test for constructor of class Last
def test_Last():
    assert Last(3).value == 3


# Generated at 2022-06-14 03:48:17.980748
# Unit test for method concat of class Sum
def test_Sum_concat():
    sum_1 = Sum(1)
    sum_2 = Sum(2)
    sum_3 = Sum(3)
    test = sum_1.concat(sum_2).concat(sum_3)
    assert test.value == sum_1.value + sum_2.value + sum_3.value


# Generated at 2022-06-14 03:48:21.420218
# Unit test for method __str__ of class Map
def test_Map___str__():
    assert str(Map({1: 'a', 2: 'b'})) == 'Map[value={1: a, 2: b}]'


# Generated at 2022-06-14 03:48:24.123318
# Unit test for method __str__ of class One
def test_One___str__():
    one = One(1)
    assert str(one) == 'One[value=1]'


# Generated at 2022-06-14 03:48:25.148638
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    pass  # to be implemented


# Generated at 2022-06-14 03:48:28.886759
# Unit test for constructor of class Map
def test_Map():
    assert Map({}) == Map({})
    assert Map({1: Sum(1)}) == Map({1: Sum(1)})
    assert Map({1: Sum(1), 2: Sum(2)}) == Map({1: Sum(1), 2: Sum(2)})


# Generated at 2022-06-14 03:48:35.287594
# Unit test for method __str__ of class Map
def test_Map___str__():
    assert str(Map({})) == 'Map[value={}]', "Map with empty dict"
    assert str(Map({'a': 1})) == 'Map[value={\'a\': 1}]', "Map with one key"
    assert str(Map({'a': 1, 'b': 2})) == 'Map[value={\'a\': 1, \'b\': 2}]', "Map with two key"



# Generated at 2022-06-14 03:48:36.843968
# Unit test for constructor of class Map
def test_Map():
    """
    Test that Map 's constructor is working well
    """
    assert Map(1) == Map(1)


# Generated at 2022-06-14 03:48:40.875589
# Unit test for method __str__ of class Max
def test_Max___str__():  # pragma: no cover
    semigroup = Max(3)
    assert str(semigroup) == 'Max[value=3]'



# Generated at 2022-06-14 03:48:41.856994
# Unit test for constructor of class First
def test_First():
    assert First(1).value == 1


# Generated at 2022-06-14 03:48:45.673494
# Unit test for method concat of class All
def test_All_concat():
    assert All(All.neutral_element).concat(All(True)) == All(True), \
        "Method concat of class All is not correct"


# Generated at 2022-06-14 03:48:47.214534
# Unit test for constructor of class Last
def test_Last():
    try:
        Last('')
        Last(1)
        Last(None)
        Last(True)
    except Exception:
        print("Last constructor test failed")
        exit(1)
    else:
        print("Last Constructor test passed")


# Generated at 2022-06-14 03:48:49.789213
# Unit test for method __str__ of class Min
def test_Min___str__():
    assert str(Min(4)) == 'Min[value=4]'


# Generated at 2022-06-14 03:48:52.337309
# Unit test for method __str__ of class First
def test_First___str__():
    assert str(First(4)) == 'Fist[value=4]'



# Generated at 2022-06-14 03:48:53.651631
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    assert Semigroup(123) == Semigroup(123)



# Generated at 2022-06-14 03:48:57.876048
# Unit test for method concat of class All
def test_All_concat():
    assert (All(True).concat(All(False)) == All(False)), 'Returned wrong value'
    assert (All(False).concat(All(True)) == All(False)), 'Returned wrong value'
    assert (All(True).concat(All(True)) == All(True)), 'Returned wrong value'


# Generated at 2022-06-14 03:49:00.526220
# Unit test for method __str__ of class Max
def test_Max___str__():
    a = Max(5)

    assert str(a) == 'Max[value=5]'


# Generated at 2022-06-14 03:49:01.828512
# Unit test for method __str__ of class First
def test_First___str__():
    assert str(First(1)) == 'Fist[value=1]'


# Generated at 2022-06-14 03:49:04.959599
# Unit test for method __str__ of class All
def test_All___str__():
    assert str(All(True)) == 'All[value=True]'
    assert str(All(False)) == 'All[value=False]'



# Generated at 2022-06-14 03:49:07.532187
# Unit test for method __str__ of class All
def test_All___str__():  # pragma: no cover
    assert str(All(True)) == 'All[value=True]'
    assert str(All(False)) == 'All[value=False]'



# Generated at 2022-06-14 03:49:16.052295
# Unit test for method __str__ of class Max
def test_Max___str__():
    max_1 = Max(1)
    max_2 = Max(2)
    assert max_1.__str__() == "Max[value=1]"
    assert max_2.__str__() == "Max[value=2]"
    assert max_1.__str__() != max_2.__str__()


# Generated at 2022-06-14 03:49:21.262172
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(1).concat(Max(2)) == Max(2)
    assert Max(2).concat(Max(1)) == Max(2)
    assert Max(2).concat(Max(2)) == Max(2)
    # We don't need to test other cases.


# Generated at 2022-06-14 03:49:23.597904
# Unit test for constructor of class Min
def test_Min():
    assert Min(2) == Min(2)
    assert Min(2) != Min(1)


# Generated at 2022-06-14 03:49:33.925038
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    assert Sum(1).fold(lambda x: x + 1) == 2
    assert All(True).fold(lambda x: x is False) is False
    assert First(1).fold(lambda x: x + 1) == 1
    assert Last(1).fold(lambda x: x + 1) == 2
    assert Map({1: Sum(1)}).fold(lambda x: x)[1].fold(lambda x: x + 1) == 2
    assert Max(1).fold(lambda x: x + 1) == 2
    assert Min(1).fold(lambda x: x + 1) == 1
    assert Min(2).fold(lambda x: x + 1) == 2


# Generated at 2022-06-14 03:49:41.938285
# Unit test for method concat of class Map
def test_Map_concat():  # pragma: no cover
    res = Map({'a': Sum(1), 'b': Max(2), 'c': Min(3)})
    res = res.concat(Map({'a': Sum(1), 'b': Max(2), 'c': Min(3)}))
    assert res == Map({'a': Sum(2), 'b': Max(2), 'c': Min(3)})
    assert res.fold(lambda x: x) == {'a': 2, 'b': 2, 'c': 3}


# Generated at 2022-06-14 03:49:51.963634
# Unit test for method concat of class Map
def test_Map_concat():
    Map_1 = Map({'a': All(True), 'b': All(True)})
    Map_2 = Map({'a': All(True), 'b': All(False)})
    assert Map_1 is not Map_2
    assert Map_1 != Map_2
    assert Map_1.concat(Map_2).value['a'] == Map({'a': All(True), 'b': All(True)}).value['a']
    assert Map_1.concat(Map_2).value['b'] == Map({'a': All(True), 'b': All(False)}).value['b']


# Generated at 2022-06-14 03:49:56.619782
# Unit test for method concat of class Sum
def test_Sum_concat():
    assert Sum(2).concat(Sum(1)) == Sum(3)
    assert Sum(1).concat(Sum(2)) == Sum(3)
    assert Sum(1).concat(Sum(2)) == Sum(2).concat(Sum(1))


# Generated at 2022-06-14 03:49:58.752518
# Unit test for method __str__ of class Last
def test_Last___str__():
    l = Last(1)
    assert str(l) == "Last[value=1]"



# Generated at 2022-06-14 03:50:03.519203
# Unit test for method concat of class One
def test_One_concat():  # pragma: no cover
    one_true = One(True)
    one_false = One(False)
    assert one_true.concat(one_false) == One(True)
    assert one_false.concat(one_true) == One(True)


# Generated at 2022-06-14 03:50:15.266339
# Unit test for constructor of class Max
def test_Max():
    assert Max(1).value == 1
    assert Max(1).concat(Max(2)).value == 2
    assert Max(1).concat(Max(2)).concat(Max(3)).value == 3
    assert Max(1).concat(Max(2)).concat(Max(3)).concat(Max(4)).value == 4
    assert Max(1).concat(Max(2)).concat(Max(3)).concat(Max(4)).concat(Max(5)).value == 5
    assert Max(1).concat(Max(2)).concat(Max(3)).concat(Max(4)).concat(Max(5)).concat(Max(6)).value == 6

# Generated at 2022-06-14 03:50:23.300886
# Unit test for constructor of class One
def test_One():
    assert One(1) == One(1)
    assert One(1) != One(2)


# Generated at 2022-06-14 03:50:24.977626
# Unit test for method __str__ of class Min
def test_Min___str__():
    assert str(Min(5)) == 'Min[value=5]'



# Generated at 2022-06-14 03:50:26.585786
# Unit test for constructor of class Last
def test_Last():  # pragma: no cover
    result = Last(1)
    assert result.value == 1

# Generated at 2022-06-14 03:50:30.543246
# Unit test for method __str__ of class Last
def test_Last___str__():
    assert str(Last(1)) == "Last[value=1]"
    assert str(Last(True)) == "Last[value=True]"
    assert str(Last("Last")) == "Last[value=Last]"


# Generated at 2022-06-14 03:50:32.373683
# Unit test for method __str__ of class Min
def test_Min___str__():
    assert str(Min(2)) == "Min[value=2]"



# Generated at 2022-06-14 03:50:34.326936
# Unit test for constructor of class First
def test_First():  # pragma: no cover
    assert First(1)



# Generated at 2022-06-14 03:50:36.034227
# Unit test for constructor of class Min
def test_Min():
    assert Min(8) == Min(8)


# Generated at 2022-06-14 03:50:43.171850
# Unit test for method concat of class Map
def test_Map_concat():
    map1 = Map({1: Sum(1), 2: Sum(2), 4: Sum(4)})
    map2 = Map({1: Sum(1), 3: Sum(3)})
    map3 = Map({1: Sum(2), 2: Sum(4), 3: Sum(3), 4: Sum(8)})

    assert map1.concat(map2) == map3

test_Map_concat()

# Generated at 2022-06-14 03:50:45.860725
# Unit test for method __str__ of class Min
def test_Min___str__():
    assert Min(1).__str__() == 'Min[value=1]'


# Generated at 2022-06-14 03:50:47.526118
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(1).concat(Min(2)) == Min(1)



# Generated at 2022-06-14 03:51:00.650254
# Unit test for method __str__ of class Max
def test_Max___str__():  # pragma: no cover
    assert str(Max(10)) == 'Max[value=10]'



# Generated at 2022-06-14 03:51:01.758740
# Unit test for method concat of class Sum
def test_Sum_concat():
    assert Sum(1).concat(Sum(1)) == Sum(2)



# Generated at 2022-06-14 03:51:02.939051
# Unit test for method __str__ of class One
def test_One___str__():
    assert str(One(False)) == 'One[value=False]'

# Generated at 2022-06-14 03:51:08.749811
# Unit test for method concat of class One
def test_One_concat():
    one = One(1)
    two = One(2)
    three = One(3)

    assert one.concat(two).concat(three) == One(1)
    assert two.concat(three).concat(one) == One(1)
    assert three.concat(one).concat(two) == One(1)

if __name__ == "__main__":
    test_One_concat()

# Generated at 2022-06-14 03:51:11.359740
# Unit test for method __str__ of class Last
def test_Last___str__():
    assert Last(10).__str__() == "Last[value=10]", "The __str__ method of Last with value 10 should be Last[value=10]"



# Generated at 2022-06-14 03:51:17.759550
# Unit test for method concat of class One
def test_One_concat():
    c = One(False)
    c = c.concat(One(True))
    assert c == One(True)

    c = c.concat(One(False))
    assert c == One(True)

    c = c.concat(One(True))
    assert c == One(True)

    c = c.concat(One(False))
    assert c == One(True)


# Generated at 2022-06-14 03:51:19.206006
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(-5)) == 'Max[value=-5]'



# Generated at 2022-06-14 03:51:20.985371
# Unit test for constructor of class Semigroup
def test_Semigroup():
    assert Semigroup(1).value == 1
    assert Semigroup(None).value is None



# Generated at 2022-06-14 03:51:23.953914
# Unit test for method __str__ of class Map
def test_Map___str__(): # pragma: no cover
    assert str(Map({1: Sum(1), 2: Sum(2)})) == 'Map[value={1: Sum[value=1], 2: Sum[value=2]}]'


# Generated at 2022-06-14 03:51:25.067922
# Unit test for constructor of class Last
def test_Last():
    last = Last(5)

    assert last.value == 5


# Generated at 2022-06-14 03:51:51.032450
# Unit test for method __str__ of class One
def test_One___str__():
    assert str(One(True)) == "One[value=True]"
    assert str(One(False)) == "One[value=False]"


# Generated at 2022-06-14 03:51:54.794098
# Unit test for method concat of class First
def test_First_concat():
    def assert_equals(a, b):
        return a == b
    first = First('foo')
    first2 = First('bar')
    assert_equals('foo', first.concat(first2))


# Generated at 2022-06-14 03:51:58.556646
# Unit test for constructor of class Map
def test_Map():
    source = {
        '1': Sum(1),
        '2': Sum(2)
    }
    m = Map(source)
    assert m.value == source


# Generated at 2022-06-14 03:52:00.096960
# Unit test for method __str__ of class One
def test_One___str__():
    assert str(One(1)) == 'One[value=1]'


# Generated at 2022-06-14 03:52:02.678508
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(4)) == 'Max[value=4]', 'test_Max___str__() failed'


# Generated at 2022-06-14 03:52:09.655095
# Unit test for method concat of class First
def test_First_concat():
    value = []

    assert(First(1).concat(First(2)) == First(1))
    assert(First(1).concat(First("")) == First(1))
    assert(First(1).concat(First(value)) == First(1))
    assert(First("").concat(First(2)) == First(""))
    assert(First("").concat(First("")) == First(""))
    assert(First("").concat(First(value)) == First(""))
    assert(First(value).concat(First(2)) == First(value))
    assert(First(value).concat(First("")) == First(value))
    assert(First(value).concat(First(value)) == First(value))


# Generated at 2022-06-14 03:52:15.660633
# Unit test for method concat of class All
def test_All_concat():
    assert All(True).concat(All(True)) == All(True)
    assert All(True).concat(All(False)) == All(False)
    assert All(False).concat(All(True)) == All(False)
    assert All(False).concat(All(False)) == All(False)



# Generated at 2022-06-14 03:52:18.669477
# Unit test for constructor of class One
def test_One():
    assert_equal(One(0), One(0))
    assert_equal(One(0).value, 0)



# Generated at 2022-06-14 03:52:20.937722
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    # given
    foldable: List[Sum] = [Sum(1), Sum(2), Sum(3), Sum(4)]
    # when
    result = foldable.fold(lambda x: x.value)
    # then
    expected = 10
    assert result == expected



# Generated at 2022-06-14 03:52:26.826147
# Unit test for method concat of class All
def test_All_concat():
    actual = All(True).concat(All(True))
    assert actual == All(True)
    actual = All(True).concat(All(False))
    assert actual == All(False)
    actual = All(False).concat(All(True))
    assert actual == All(False)
    actual = All(False).concat(All(False))
    assert actual == All(False)


# Generated at 2022-06-14 03:53:25.568475
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(5).concat(Max(1)) == Max(5)
    assert Max(1).concat(Max(5)) == Max(5)
    assert Max(5).concat(Max(5)) == Max(5)



# Generated at 2022-06-14 03:53:29.601541
# Unit test for method __str__ of class Last
def test_Last___str__():  # pragma: no cover
    """ Test for method __str__ of class Last """
    assert str(Last(100)) == 'Last[value=100]'



# Generated at 2022-06-14 03:53:35.343987
# Unit test for constructor of class Sum
def test_Sum():  # pragma: no cover
    assert Sum(1) == Sum(1)
    assert Sum(1) != Sum(2)
    assert str(Sum(1)) == 'Sum[value=1]'
    assert Sum(1).concat(Sum(1)) == Sum(2)
    assert Sum(1).fold(lambda x:x) == 1
    assert Sum.neutral().value == 0


# Generated at 2022-06-14 03:53:36.328120
# Unit test for constructor of class First
def test_First():
    assert First(1)


# Generated at 2022-06-14 03:53:38.873717
# Unit test for method __str__ of class One
def test_One___str__():  # pragma: no cover
    value = 'test_value'
    s = One(value)

    assert s.__str__() == 'One[value={}]'.format(value)



# Generated at 2022-06-14 03:53:42.551995
# Unit test for constructor of class First
def test_First():
    assert First(3) == First(3)
    assert First(3) != First(4)
    assert First(3).concat(First(4)) == First(3)
    assert First(3).fold(lambda x: x) == 3
    assert First(3).fold(lambda x: x) == 3



# Generated at 2022-06-14 03:53:46.876052
# Unit test for method __str__ of class Map
def test_Map___str__():
    assert str(Map({
        "1": Sum(1),
        "2": Sum(1)
    })) == "Map[value={'1': Sum[value=1], '2': Sum[value=1]}]"



# Generated at 2022-06-14 03:53:48.398413
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(1).concat(Max(2)).value == 2

# Generated at 2022-06-14 03:53:49.523904
# Unit test for constructor of class Max
def test_Max():
    assert Max(7) == Max(7)

# Generated at 2022-06-14 03:53:53.622272
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    test_values = [1, 2, 3, 4, 5]

    for value in test_values:
        assert Semigroup(value) == Semigroup(value)
        assert Semigroup(value) != Semigroup(value + 1)

