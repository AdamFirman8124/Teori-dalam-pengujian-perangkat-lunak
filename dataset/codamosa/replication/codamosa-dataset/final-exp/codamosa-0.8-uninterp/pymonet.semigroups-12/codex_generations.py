

# Generated at 2022-06-14 03:44:30.482993
# Unit test for method concat of class Map
def test_Map_concat():
    result = Map({'a': Sum(1), 'b': Sum(1)}).concat(Map({'a': Sum(3), 'b': Sum(2)}))
    assert result == Map({'a': Sum(4), 'b': Sum(3)})


# Generated at 2022-06-14 03:44:33.844212
# Unit test for method concat of class Min
def test_Min_concat():
    min1 = Min(5)
    min2 = Min(2)
    assert min2.concat(min1).value == min2.value

# Generated at 2022-06-14 03:44:40.244144
# Unit test for method concat of class Min
def test_Min_concat():
    semigroup_A = Min(5)
    semigroup_B = Min(10)
    semigroup_result_expected = Min(5)
    semigroup_result = semigroup_A.concat(semigroup_B)
    assert semigroup_result == semigroup_result_expected, "assert semigroup_A.concat(semigroup_B) == semigroup_result_expected failed!"
    print("PASSED: test_Min_concat()")


# Generated at 2022-06-14 03:44:43.880171
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(1).concat(Min(2)).value == 1
    assert Min(5).concat(Min(4)).value == 4
    assert Min(4).concat(Min(4)).value == 4

# Generated at 2022-06-14 03:44:48.188734
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(2).concat(Min(2)) == Min(2)
    assert Min(2).concat(Min(0)) == Min(0)
    assert Min(0).concat(Min(2)) == Min(0)

# Generated at 2022-06-14 03:44:54.378418
# Unit test for method concat of class Map
def test_Map_concat():
    assert Map({"a": Sum(1)}).concat(Map({"a": Sum(2)})) == Map({"a": Sum(3)})
    assert Map({"a": Sum(1)}).concat(Map({"a": Sum(2), "b": Sum(3)})) == Map(
        {"a": Sum(3), "b": Sum(3)}
    )
    assert Map({"a": Sum(1), "b": Sum(3)}).concat(Map({"a": Sum(2), "b": Sum(3)})) == Map(
        {"a": Sum(3), "b": Sum(6)}
    )

# Generated at 2022-06-14 03:44:55.543430
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(2).concat(Min(1)).value == 1



# Generated at 2022-06-14 03:45:00.555782
# Unit test for method concat of class Map
def test_Map_concat():
    assert isinstance(Map({'a': Min(15)}).concat(Map({'a': Min(3)})), Map)
    assert Map({'a': Min(15)}).concat(Map({'a': Min(3)})) == Map({'a': Min(3)})


# Generated at 2022-06-14 03:45:11.414553
# Unit test for method concat of class Map
def test_Map_concat():
    map_1 = Map({
        'key_1': Sum(1),
        'key_2': Sum(2),
        'key_3': Sum(3),
        'key_4': Sum(4),
    })
    map_2 = Map({
        'key_1': Sum(10),
        'key_3': Sum(30),
        'key_4': Sum(40),
    })
    result = Map({
        'key_1': Sum(11),
        'key_2': Sum(2),
        'key_3': Sum(33),
        'key_4': Sum(44),
    })

    assert map_1.concat(map_2) == result



# Generated at 2022-06-14 03:45:13.820699
# Unit test for method concat of class Map
def test_Map_concat():
    map1 = Map({1: Sum(2)})
    map2 = Map({1: Sum(3)})

    assert map1.concat(map2) == Map({1: Sum(5)})


# Generated at 2022-06-14 03:45:17.274598
# Unit test for constructor of class All
def test_All():
    """
    Unit test for constructor of class All
    """
    a1 = All(True)
    a2 = All(False)

    assert a1.value
    assert not a2.value


# Generated at 2022-06-14 03:45:18.018539
# Unit test for constructor of class Min
def test_Min():
    assert Min.neutral().concat(Min(2)).value == 2

# Generated at 2022-06-14 03:45:19.612065
# Unit test for method concat of class First
def test_First_concat():
    assert First(1).concat(First(2)).value == 1



# Generated at 2022-06-14 03:45:21.563336
# Unit test for constructor of class Semigroup
def test_Semigroup():  # pragma: no cover
    assert Semigroup(2).value == 2



# Generated at 2022-06-14 03:45:24.693671
# Unit test for method concat of class All
def test_All_concat():
    sg = All(True)
    sg2 = All(False)
    assert sg.concat(sg2) == All(False)


# Generated at 2022-06-14 03:45:28.249389
# Unit test for method __str__ of class All
def test_All___str__():
    assert str(All(True)) == 'All[value=True]'
    assert str(All(False)) == 'All[value=False]'

# Generated at 2022-06-14 03:45:36.952275
# Unit test for constructor of class Max
def test_Max():
    """
    Unit test for class Max
    """
    print("\nStarting testing for class Max")

    # Create instance Max
    instance_class_Max = Max(4)
    assert instance_class_Max.value == 4
    print("Successfully tested for __init__")

    # Test str method
    assert str(instance_class_Max) == 'Max[value=4]'
    print("Successfully tested for __str__")

    # Test repr method
    assert repr(instance_class_Max) == 'Max[value=4]'
    print("Successfully tested for __repr__")

    # Create another instance
    another_instance_class_Max = Max(5)

    # Test eq method
    assert instance_class_Max.__eq__(another_instance_class_Max) == False

# Generated at 2022-06-14 03:45:41.768627
# Unit test for method __str__ of class One
def test_One___str__():
    assert str(One(10)) == 'One[value=10]'
    assert str(One(True)) == 'One[value=True]'
    assert str(One(False)) == 'One[value=False]'



# Generated at 2022-06-14 03:45:47.462031
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():  # pragma: no cover
    assert Sum(1) == Sum(1)
    assert All(True) == All(True)
    assert One(False) == One(False)
    assert Last(1) == Last(1)
    assert First(1) == First(1)
    assert Map({1:Sum(1)}) == Map({1:Sum(1)})



# Generated at 2022-06-14 03:45:49.984517
# Unit test for method __str__ of class All
def test_All___str__():  # pragma: no cover
    assert 'All[value=True]' == str(All(True))


# Generated at 2022-06-14 03:45:53.484659
# Unit test for constructor of class Max
def test_Max():
    assert type(Max(1)) == Max


# Generated at 2022-06-14 03:45:55.619913
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(1).concat(Max(2)) == Max(2)


# Generated at 2022-06-14 03:46:01.919510
# Unit test for constructor of class Sum
def test_Sum():
    assert Sum(None) == Sum(None)
    assert Sum(None).value is not None
    assert Sum(1) == Sum(1)
    assert Sum(1.1) == Sum(1.1)
    assert Sum(True) == Sum(True)
    assert Sum('string') == Sum('string')
    assert Sum([1]) == Sum([1])
    assert Sum({'key': 'value'}) == Sum({'key': 'value'})



# Generated at 2022-06-14 03:46:04.006408
# Unit test for method __str__ of class One
def test_One___str__():
    assert str(One(True)) == "One[value=True]"


# Generated at 2022-06-14 03:46:05.819882
# Unit test for method __str__ of class Last
def test_Last___str__():
    result = Last('2')
    assert str(result) == "Last[value=2]"



# Generated at 2022-06-14 03:46:09.674908
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    assert Sum(2) == Sum(2)
    assert All(True) == All(True)
    assert One(False) == One(False)
    assert First(2) == First(2)
    assert Last(2) == Last(2)
    assert Map({1: Sum(1), 2: Sum(2)}) == Map({1: Sum(1), 2: Sum(2)})
    assert Max(1) == Max(1)
    assert Min(0) == Min(0)


# Generated at 2022-06-14 03:46:12.886882
# Unit test for constructor of class First
def test_First():
    assert First(1) == First(1)
    assert First(1) != First(2)
    assert First(1).fold(lambda x: x) == 1



# Generated at 2022-06-14 03:46:21.474993
# Unit test for constructor of class Semigroup
def test_Semigroup():  # pragma: no cover
    from hypothesis import given, assume
    from hypothesis.strategies import integers, lists
    from pymonad import Just, Nothing
    from pymonad.list import List
    from pymonad.maybe import Maybe, Nothing
    from pymonad.tuple import Tuple3

    @given(integers())
    def test_Sum(a):  # pragma: no cover
        assert Sum(a) == Sum(a)

    @given(integers())
    def test_All(a):  # pragma: no cover
        assert All(a) == All(a)

    @given(integers())
    def test_First(a):  # pragma: no cover
        assert First(a) == First(a)


# Generated at 2022-06-14 03:46:24.383289
# Unit test for method __str__ of class All
def test_All___str__():
    assert All(1) == All(True)
    assert str(All(1)) == 'All[value=True]'
    assert str(All(0)) == 'All[value=False]'


# Generated at 2022-06-14 03:46:25.381924
# Unit test for method __str__ of class First
def test_First___str__():
    assert "Fist[value=foo]" == str(First("foo"))


# Generated at 2022-06-14 03:46:29.019522
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(45).concat(Max(5)) == Sum(50)



# Generated at 2022-06-14 03:46:36.081615
# Unit test for method concat of class Map
def test_Map_concat():  # pragma: no cover
    assert Map({
        'a': Sum(1),
        'b': Max(4),
        'c': First('hello'),
    }).concat(
        Map({
            'a': Sum(2),
            'b': Max(3),
            'c': First('world'),
        }),
    ) == Map({
        'a': Sum(3),
        'b': Max(4),
        'c': First('hello'),
    })


# Generated at 2022-06-14 03:46:43.209017
# Unit test for method concat of class Min
def test_Min_concat():
    print('\n### UNIT TEST FOR Min CLASS concat METHOD ###')
    instance1 = Min(3)
    instance2 = Min(1)
    instance3 = instance1.concat(instance2)
    print('Min(3).concat(Min(1)) = {}'.format(instance3))
    assert instance3 == Min(1)
    print('PASSED: Min.concat test')



# Generated at 2022-06-14 03:46:48.074040
# Unit test for constructor of class All
def test_All():
    """
    Unit test for constructor of class All
    """

    true_all = All(True)
    false_all = All(False)
    assert true_all.value is True
    assert false_all.value is False



# Generated at 2022-06-14 03:46:55.957196
# Unit test for method __str__ of class Map
def test_Map___str__():
    inst = Map({
        'first': Sum(1),
        'second': Sum(5),
        'third': Sum(3),
    })
    print(
        'Map[value={\n'
        '\tfirst: {}\n'
        '\tsecond: {}\n'
        '\tthird: {}\n'
        '}]'.format(
            Sum(1),
            Sum(5),
            Sum(3),
        )
    )
    print(inst)
    if __name__ == '__main__':
        test_Map___str__()



# Generated at 2022-06-14 03:47:05.210440
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    """
    :return: None
    """
    assert Sum(1).fold(lambda x: x + 1) == 2, 'fold should be 2'
    assert All(True).fold(lambda x: not x) == False, 'fold should be False'
    assert One(True).fold(lambda x: not x) == True, 'fold should be True'
    assert First("a").fold(lambda x: x + "b") == "ab", 'fold should be "ab"'
    assert Last("a").fold(lambda x: x + "b") == "b", 'fold should be "b"'

# Generated at 2022-06-14 03:47:06.603726
# Unit test for method __str__ of class All
def test_All___str__():
    assert str(All(True)) == 'All[value=True]'


# Generated at 2022-06-14 03:47:09.248041
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    assert Semigroup(4).__eq__(Semigroup(4))
    assert not Semigroup(4).__eq__(Semigroup(5))


# Generated at 2022-06-14 03:47:16.033564
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    f = lambda x: x ** 2
    assert 3 ** 2 == Semigroup(3).fold(f)
    assert None is Semigroup(None).fold(f)
    assert None is Semigroup(None).fold(lambda x: x.blabla())
    assert Semigroup(None).fold(lambda x: None) is None



# Generated at 2022-06-14 03:47:17.400786
# Unit test for method __str__ of class Min
def test_Min___str__():
    assert str(Min(1)) == 'Min[value=1]'


# Generated at 2022-06-14 03:47:25.995097
# Unit test for constructor of class Last
def test_Last():
    last = Last(3)
    assert last.concat(Last(4)).value == 4
    assert last.value == 3


# Generated at 2022-06-14 03:47:29.511021
# Unit test for method concat of class First
def test_First_concat():
    assert First(1).concat(First(2)) == First(1)


# Generated at 2022-06-14 03:47:33.330768
# Unit test for method concat of class All
def test_All_concat():
    assert All(True).concat(All(True)) == All(True)
    assert All(True).concat(All(False)) == All(False)
    assert All(False).concat(All(True)) == All(False)
    assert All(False).concat(All(False)) == All(False)


# Generated at 2022-06-14 03:47:36.048124
# Unit test for method concat of class Last
def test_Last_concat():
    assert Last(1).concat(Last(2)) == Last(2)


# Generated at 2022-06-14 03:47:41.464974
# Unit test for method concat of class Sum
def test_Sum_concat():
    """
    Unit test for method concat of class Sum
    """

    assert Sum(2) == Sum(2)
    assert Sum(2).concat(3) == Sum(5)
    assert Sum(2).concat(Sum(3)) == Sum(5)
    assert Sum([2, 3]).concat(Sum([3, 4])) == Sum([2, 3, 3, 4])
    assert Sum([2, 3]).concat([3, 4]) == Sum([2, 3, 3, 4])
    assert Sum([2, 3]).concat(Sum(3)) == Sum([2, 3, 3])
    assert Sum(2).concat([3, 4]) == Sum([2, 3, 4])
    assert Sum(2).concat(3) == Sum(5)


# Generated at 2022-06-14 03:47:47.145248
# Unit test for method concat of class One
def test_One_concat():
    assert One(True).concat(One(False)) == One(True)
    assert One(False).concat(One(True)) == One(True)
    assert One(False).concat(One(False)) == One(False)
    try:
        assert One([]).concat(One({}))
    except Exception:
        pass
    else:
        assert False


# Generated at 2022-06-14 03:47:51.728686
# Unit test for method concat of class One
def test_One_concat():
    a = One(True)
    b = One(False)
    c = One(False)
    assert a.concat(b) == One(True)
    assert b.concat(c) == One(False)
    assert a.concat(c) == One(True)


# Generated at 2022-06-14 03:47:53.860496
# Unit test for constructor of class Sum
def test_Sum():
    sum1 = Sum(1)

    assert(isinstance(sum1, Sum))
    assert(sum1.value == 1)


# Generated at 2022-06-14 03:47:56.561572
# Unit test for method __str__ of class Max
def test_Max___str__():  # pragma: no cover
    assert str(Max(5)) == 'Max[value=5]'



# Generated at 2022-06-14 03:48:01.199526
# Unit test for method concat of class All
def test_All_concat():
    assert All(True).concat(All(True)) == All(True)
    assert All(False).concat(All(True)) == All(False)
    assert All(True).concat(All(False)) == All(False)
    assert All(False).concat(All(False)) == All(False)



# Generated at 2022-06-14 03:48:11.384870
# Unit test for method concat of class First
def test_First_concat():
    assert First(1).concat(First(2)) == First(1)
    assert First(1).concat(First('foo')) == First(1)
    assert First(1).concat(First(2)).value == 1


# Generated at 2022-06-14 03:48:12.975960
# Unit test for constructor of class Last
def test_Last():
    last = Last(13)
    assert last.value == 13


# Generated at 2022-06-14 03:48:14.530901
# Unit test for constructor of class Last
def test_Last():
    result = Last(True)
    assert result.value == True


# Generated at 2022-06-14 03:48:18.089670
# Unit test for constructor of class Map
def test_Map():
    mp = Map({1: Sum(100), 2: Sum(100), 3: Sum(100)})
    assert(mp.value == {1: Sum(100), 2: Sum(100), 3: Sum(100)})



# Generated at 2022-06-14 03:48:22.898164
# Unit test for method __str__ of class Min
def test_Min___str__():
    # arrange
    expected: str = 'Min[value=0]'
    semigroup: Min = Min(0)
    # act
    actual: str = str(semigroup)
    # assert
    assert expected == actual


# Generated at 2022-06-14 03:48:25.148971
# Unit test for method __str__ of class Map
def test_Map___str__():
    assert str(Map({"a": Sum(5)})) == "Map[value={'a': Sum[value=5]}]"


# Generated at 2022-06-14 03:48:26.782370
# Unit test for constructor of class All
def test_All():
    assert All(1) == All(1)
    assert All(True) == All(True)
    assert All(1) != All(True)
    assert All(0) != All(True)


# Generated at 2022-06-14 03:48:35.306790
# Unit test for constructor of class Map
def test_Map():
    """
    :returns: test Map constructor
    :rtype: Map[A]
    """
    # assert Map({'a': Sum(1), 'b': Sum(2)}) == Map({'a': Sum(1), 'b': Sum(2)})
    # assert Map({'a': Sum(1), 'b': Sum(2)}).value == {'a': Sum(1), 'b': Sum(2)}
    # assert Map({'a': Sum(1), 'b': Sum(2)}).value['a'] == Sum(1)
    # assert Map({'a': Sum(1), 'b': Sum(2)}).value['b'] == Sum(2)
    assert Map({'a': Sum(1), 'b': Sum(2)}).value['a'] == Sum(1)

# Generated at 2022-06-14 03:48:38.487161
# Unit test for method concat of class Map
def test_Map_concat():
    m = Map({
        "a": Sum(1),
        "b": Sum(2)
    })

    y = Map({
        "a": Sum(2),
        "b": Sum(1)
    })

    n = Map({
        "a": Sum(3),
        "b": Sum(3)
    })

    assert m.concat(y) == n

# Generated at 2022-06-14 03:48:40.778281
# Unit test for method __str__ of class Min
def test_Min___str__():
    assert str(Min(100)) == 'Min[value=100]'



# Generated at 2022-06-14 03:48:49.208097
# Unit test for constructor of class Min
def test_Min():
    assert Min(5) == Min(5)


# Generated at 2022-06-14 03:48:50.882243
# Unit test for method concat of class Sum
def test_Sum_concat():
    assert Sum(3).concat(Sum(4)).value == 7


# Generated at 2022-06-14 03:48:52.655317
# Unit test for constructor of class Min
def test_Min():
    assert Min(1) == Min(1)


# Generated at 2022-06-14 03:48:54.317876
# Unit test for constructor of class Sum
def test_Sum():
    assert isinstance(Sum(2).value, int)
    assert Sum(2).value == 2



# Generated at 2022-06-14 03:48:56.086734
# Unit test for constructor of class One
def test_One():  # pragma: no cover
    """
    Test 1.1 for class One
    """
    assert One(True).value == True
    assert One(False).value == False



# Generated at 2022-06-14 03:48:59.527627
# Unit test for method concat of class Map
def test_Map_concat():
    map_a = Map({'a': 1, 'b': 2, 'c': 3})
    map_b = Map({'a': 4, 'b': 3, 'c': 2})

    assert map_a.concat(map_b) == Map({'a': 5, 'b': 5, 'c': 5})

# Generated at 2022-06-14 03:49:03.491390
# Unit test for method __str__ of class First
def test_First___str__():
    instance = First(1)
    expected = 'Fist[value=1]'
    actual = str(instance)
    assert actual == expected, 'Expected "{0}", got "{1}"'.format(expected, actual)



# Generated at 2022-06-14 03:49:07.029601
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    """
    :returns: True if test is passed
    :rtype: bool
    """
    def test_function(value):
        return not value

    assert Semigroup([1, 2, 3, 4]).fold(test_function) == [False, False, False, False]



# Generated at 2022-06-14 03:49:16.549287
# Unit test for method concat of class Map
def test_Map_concat():
    """
    Testing Map concat method
    """
    semigroup_1 = Map({
        "1": Sum(1),
        "2": Sum(2)
    })
    semigroup_2 = Map({
        "1": Sum(3),
        "2": Sum(4),
        "3": Sum(5)
    })
    assert semigroup_1.concat(semigroup_2) == Map({
        "1": Sum(4),
        "2": Sum(6),
        "3": Sum(5)
    })



# Generated at 2022-06-14 03:49:18.559199
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(5)) == 'Max[value=5]'



# Generated at 2022-06-14 03:49:26.654020
# Unit test for method concat of class Sum
def test_Sum_concat():
    assert Sum(1).concat(Sum(2)) == Sum(3)



# Generated at 2022-06-14 03:49:29.134776
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    assert Semigroup(1).fold(lambda x: x + 1) == 2

# Unit tests for method concat of class Sum

# Generated at 2022-06-14 03:49:34.787945
# Unit test for method concat of class One
def test_One_concat():  # pragma: no cover
    assert One(1).concat(One(1)) == One(1)
    assert One(1).concat(One(None)) == One(1)
    assert One(None).concat(One(1)) == One(1)
    assert One(None).concat(One(None)) == One(None)


# Generated at 2022-06-14 03:49:37.034544
# Unit test for method __str__ of class All
def test_All___str__():
    test = All(True)
    assert isinstance(test, All)
    assert test.__str__() == 'All[value=True]'


# Generated at 2022-06-14 03:49:42.262616
# Unit test for constructor of class Map
def test_Map():
    data1 = {1: Sum(1), 2: Sum(2), 3: Sum(3)}
    data2 = {1: Sum(1), 2: Sum(2), 3: Sum(3)}
    assert isinstance(Map(data1), Map) == True
    assert Map(data1).concat(Map(data2)).value == {1: Sum(2), 2: Sum(4), 3: Sum(6)}

# Generated at 2022-06-14 03:49:45.906017
# Unit test for constructor of class Max
def test_Max():
    assert Max(1) == Max(1)
    assert Max(2) != Max(1)



# Generated at 2022-06-14 03:49:47.769531
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(42)) == 'Max[value=42]'


# Generated at 2022-06-14 03:49:49.199420
# Unit test for method __str__ of class Min
def test_Min___str__():
    assert str(Min(5)) == "Min[value=5]"


# Generated at 2022-06-14 03:49:49.970913
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    assert str(Sum(1)) == 'Sum[value=1]'


# Generated at 2022-06-14 03:49:51.530959
# Unit test for constructor of class Sum
def test_Sum():
    a = Sum(1)
    b = Sum(2)
    assert a != b
    assert str(a) == 'Sum[value=1]'
    assert str(b) == 'Sum[value=2]'



# Generated at 2022-06-14 03:50:05.348832
# Unit test for method __str__ of class Map
def test_Map___str__():
    assert str(Map({'a': 1})) == 'Map[value={\'a\': 1}]'


# Generated at 2022-06-14 03:50:07.513294
# Unit test for method __str__ of class Last
def test_Last___str__():
    last = Last(None)
    assert last.__str__() == 'Last[value=None]'


# Generated at 2022-06-14 03:50:08.684916
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    assert str(Sum(1)) == 'Sum[value=1]'


# Generated at 2022-06-14 03:50:12.043797
# Unit test for constructor of class Map
def test_Map():
    m1 = Map({'one': First(1), 'two': First(2)})
    m2 = Map({'one': Last(1), 'two': Last(2)})
    assert m1.value['one'] == First(1)
    assert m1.value['two'] == First(2)
    assert m2.value['one'] == Last(1)
    assert m2.value['two'] == Last(2)


# Generated at 2022-06-14 03:50:16.057368
# Unit test for constructor of class Sum
def test_Sum():
    assert Sum(1) == Sum(1)
    assert Sum(1) != Sum(2)
    assert Sum(1).value == 1

#Unit test for function fold(fn) of class Sum

# Generated at 2022-06-14 03:50:29.459813
# Unit test for constructor of class Max
def test_Max():
    Max(1)
    Max(-1)
    Max(0)
    Max(-0)
    assert Max(float('-inf')) == Max(-float('inf'))

test_Max()

test_Map = Map({1:Sum(1), 2:Sum(100), 3:Sum(200)})
test_Map2 = Map({1:Sum(1), 2:Sum(100), 3:Sum(2)})
test_Map_Min = Map({1:Min(1), 2:Min(100), 3:Min(200)})
test_Map2_Min = Map({1:Min(1), 2:Min(100), 3:Min(2)})
test_Map3_Min = Map({1:Min(1), 2:Min(100), 3:Min(float('-inf'))})

# Generated at 2022-06-14 03:50:32.689243
# Unit test for method __str__ of class All
def test_All___str__():
    # Arrange
    all = All(False)
    # Act
    result = str(all)
    # Assert
    assert result == "All[value=False]"



# Generated at 2022-06-14 03:50:43.644591
# Unit test for method concat of class All
def test_All_concat():
    """
    1. In the semigroup All:
        All is true if and only if all values are true
        All(True) + All(True) = All(True)
        All(True) + All(False) = All(False)
        All(False) + All(True) = All(False)
        All(False) + All(False) = All(False)
    :return:
    """
    all_true_true = All(True).concat(All(True))
    assert all_true_true.value is True
    all_false_true = All(False).concat(All(True))
    assert all_false_true.value is False
    all_true_false = All(True).concat(All(False))
    assert all_true_false.value is False
    all_false_false = All

# Generated at 2022-06-14 03:50:46.300001
# Unit test for method concat of class Max
def test_Max_concat():
    f = Max(5)
    g = Max(7)
    assert f.concat(g) == Max(7)


# Generated at 2022-06-14 03:50:47.690662
# Unit test for constructor of class Min
def test_Min():  # pragma: no cover
    result = Min(2)
    assert result.value == 2


# Generated at 2022-06-14 03:51:04.159370
# Unit test for constructor of class Map
def test_Map():
    """
    test_Map(value={'a': 1, 'b': 2, 'c': 3}) == Map[value={'a': 1, 'b': 2, 'c': 3}]:
    """
    assert Map({'a': 1, 'b': 2, 'c': 3}) == Map({'a': 1, 'b': 2, 'c': 3})


# Generated at 2022-06-14 03:51:06.282542
# Unit test for constructor of class Max
def test_Max():
    assert Max(3) == Max(3)
    assert Max(3).value == 3


# Generated at 2022-06-14 03:51:11.684732
# Unit test for method concat of class One
def test_One_concat():

    assert One(False).concat(One(True)) == One(True)
    assert One(False).concat(One(False)) == One(False)
    assert One(True).concat(One(True)) == One(True)
    assert One(True).concat(One(False)) == One(True)


# Generated at 2022-06-14 03:51:17.315687
# Unit test for method __str__ of class First
def test_First___str__():
    assert str(First(1)) == "Fist[value=1]"
    assert str(First(None)) == "Fist[value=None]"
    assert str(First(True)) == "Fist[value=True]"
    assert str(First('abcd')) == "Fist[value=abcd]"


# Generated at 2022-06-14 03:51:20.761117
# Unit test for constructor of class Max
def test_Max():
    f = Max(3)
    g = Max(4)
    h = Max(5)
    assert isinstance(f, Max)
    assert isinstance(g, Max)
    assert isinstance(h, Max)



# Generated at 2022-06-14 03:51:22.993725
# Unit test for method __str__ of class Map
def test_Map___str__():
    assert str(Map({1: 2, 3: 4})) == "Map[value={1: 2, 3: 4}]"



# Generated at 2022-06-14 03:51:27.910436
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    assert str(Sum(0)) == 'Sum[value=0]'
    assert str(Sum(1)) == 'Sum[value=1]'
    assert str(Sum(2)) == 'Sum[value=2]'



# Generated at 2022-06-14 03:51:33.929795
# Unit test for constructor of class Min
def test_Min():
    assert Min(6) == Min(6)
    assert Min(6) == Min(6)
    assert Min(6).value == 6
    assert Min(6) != Min(5)
    assert str(Min(6)) == 'Min[value=6]'
    assert isinstance(Min(6), Semigroup)


# Generated at 2022-06-14 03:51:39.339417
# Unit test for method concat of class First
def test_First_concat():
    assert First(2).concat(First(10)) == First(2)
    assert First(1).concat(First(None)) == First(1)
    assert First(1).concat(First(2)) == First(1)
    assert First([1, 2, 3]).concat(First({1: "one", 2: "two"})) == First([1, 2, 3])


# Generated at 2022-06-14 03:51:41.577348
# Unit test for constructor of class First
def test_First():
    assert First('first').value == 'first'


# Generated at 2022-06-14 03:52:10.594593
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    assert Semigroup(1) == Semigroup(1)
    assert Semigroup(2) != Semigroup(1)


# Generated at 2022-06-14 03:52:18.938200
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    assert Sum(2) == Sum(2)
    assert All(True) == All(True)
    assert One(True) == One(True)
    assert First(True) == First(True)
    assert Last(True) == Last(True)
    assert Max(2) == Max(2)
    assert Min(2) == Min(2)
    assert Map({'test': Sum(1)}) == Map({'test': Sum(1)})


# Test for method fold of class Semigroup

# Generated at 2022-06-14 03:52:20.554166
# Unit test for constructor of class Max
def test_Max():
    x = Max(1)
    assert x.value == 1


# Generated at 2022-06-14 03:52:23.773299
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():

    assert Sum(1) == Sum(1)
    assert not Sum(1) == Sum(2)
    assert not Sum(1) == Max(1)



# Generated at 2022-06-14 03:52:26.404964
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    assert Sum(2) == Sum(2)
    assert not Sum(2) == Sum(3)
    assert not Sum(2) == Sum(None)
    assert not Sum(2) == None


# Generated at 2022-06-14 03:52:27.388373
# Unit test for constructor of class Semigroup
def test_Semigroup():
    assert Semigroup(1).value == 1


# Generated at 2022-06-14 03:52:28.915420
# Unit test for constructor of class First
def test_First():
    assert First(1) == First(1)
    assert First(1) != First(2)



# Generated at 2022-06-14 03:52:31.055365
# Unit test for method __str__ of class First
def test_First___str__():
    assert str(First(1)) == 'Fist[value=1]'



# Generated at 2022-06-14 03:52:32.953539
# Unit test for constructor of class First
def test_First():
    assert First(1).value == 1
    assert First("hello").value == "hello"

# Generated at 2022-06-14 03:52:34.167738
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max.neutral()) == 'Max[value=-inf]'



# Generated at 2022-06-14 03:53:07.462577
# Unit test for constructor of class One
def test_One():
    assert(One(True).value == True)
    assert(One(False).value == False)
    assert(One(1).value == True)
    assert(One(0).value == False)

# Generated at 2022-06-14 03:53:09.361528
# Unit test for method __str__ of class All
def test_All___str__():
    assert str(All(True)) == 'All[value=True]'
    assert str(All(False)) == 'All[value=False]'



# Generated at 2022-06-14 03:53:11.067186
# Unit test for method __str__ of class All
def test_All___str__():  # pragma: no cover
    assert str(All(False)) == 'All[value=False]', 'All should return string with value'


# Generated at 2022-06-14 03:53:12.686977
# Unit test for constructor of class First
def test_First():
    assert str(First(5)) == '5', \
        'Returned {0} instead of 5'.format(str(First(5)))

# Generated at 2022-06-14 03:53:19.318719
# Unit test for constructor of class Map
def test_Map():
    """
    Unit test for constructor of class Map
    """
    map_semigroup = Map({
        'one': First('one'),
        'two': Last('two'),
        'three': Sum(1)
    })
    assert str(map_semigroup) == "Map[value={'one': Fist[value=one], 'two': Last[value=two], 'three': Sum[value=1]}]"



# Generated at 2022-06-14 03:53:21.885371
# Unit test for method __str__ of class Last
def test_Last___str__():
    result = Last(1).__str__()
    assert result == 'Last[value=1]'



# Generated at 2022-06-14 03:53:23.612987
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    sumStr = str(Sum(5))
    assert sumStr == "Sum[value=5]"


# Generated at 2022-06-14 03:53:25.243723
# Unit test for constructor of class Semigroup
def test_Semigroup():
    assert Semigroup(1) == Semigroup(1)


# Generated at 2022-06-14 03:53:29.648690
# Unit test for constructor of class Map
def test_Map():
    assert Map({
        'a': Sum(1),
        'b': Sum(2)
    }).value == {'a': Sum(1), 'b': Sum(2)}



# Generated at 2022-06-14 03:53:35.448096
# Unit test for method concat of class All
def test_All_concat():
    assert All(True).concat(All(False)).value is False, "all concat False"
    assert All(False).concat(All(True)).value is False, "all concat True"
    assert All(True).concat(All(True)).value is True, "all concat True"
    assert All(False).concat(All(False)).value is False, "all concat False"


# Generated at 2022-06-14 03:54:08.614853
# Unit test for constructor of class Max
def test_Max():
    Max(1)


# Generated at 2022-06-14 03:54:14.420506
# Unit test for method __str__ of class All
def test_All___str__():  # pragma: no cover
    assert_equal(str(All(True)), "All[value=True]")
    assert_equal(str(All(False)), "All[value=False]")
    assert_equal(str(All(1)), "All[value=True]")
    assert_equal(str(All(0)), "All[value=False]")
    assert_equal(str(All(None)), "All[value=False]")
    assert_equal(str(All([1, 2, 3])), "All[value=True]")
    assert_equal(str(All([])), "All[value=False]")


# Generated at 2022-06-14 03:54:24.355899
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    assert Sum(10) == Sum(10)
    assert All(True) == All(True)
    assert One(False) == One(False)
    assert First(10) == First(10)
    assert Last(20) == Last(20)
    assert Map({10: Sum(10), 20: All(False)}) == Map({10: Sum(10), 20: All(False)})
    assert Max(10) == Max(10)
    assert Min(20) == Min(20)
    assert Sum(10) != All(True)
    assert Map({10: Sum(10), 20: All(False)}) != Last(20)
