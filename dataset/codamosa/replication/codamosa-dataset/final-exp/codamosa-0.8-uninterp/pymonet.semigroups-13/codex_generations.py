

# Generated at 2022-06-14 03:44:27.748764
# Unit test for method concat of class Max
def test_Max_concat():
    a = Max(1)
    b = Max(1)
    assert a.concat(b).value == 1


# Generated at 2022-06-14 03:44:29.312460
# Unit test for method concat of class Max
def test_Max_concat():  # pragma: no cover
    assert Max(5).concat(Max(10)).value == 10



# Generated at 2022-06-14 03:44:38.264741
# Unit test for method concat of class Map
def test_Map_concat():
    assert Map(
        {
            'a': Sum(1),
            'b': Sum(2),
            'c': Sum(3)
        }
    ).concat(
        Map(
            {
                'a': Sum(4),
                'b': Sum(5),
                'c': Sum(6)
            }
        )
    ) == Map(
        {
            'a': Sum(5),
            'b': Sum(7),
            'c': Sum(9)
        }
    )

# Generated at 2022-06-14 03:44:46.171536
# Unit test for method concat of class Map
def test_Map_concat():
    result = Map({
        'a': Sum(1),
        'b': Sum(2),
    }).concat(Map({
        'a': Sum(3),
        'b': Sum(4),
        'c': Sum(5)
    }))
    assert str(result) == 'Map[value={\'a\': Sum[value=4], \'b\': Sum[value=6], \'c\': Sum[value=5]}]'


# Generated at 2022-06-14 03:44:47.656321
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(1).concat(Max(2)).value == 2

# Generated at 2022-06-14 03:44:57.101630
# Unit test for method concat of class Map
def test_Map_concat():
    """
    In mathematics, a semigroup is an algebraic structure
    consisting of a set together with an associative binary operation.
    A semigroup generalizes a monoid in that there might not exist an identity element.
    It also (originally) generalized a group (a monoid with all inverses)
    to a type where every element did not have to have an inverse, this the name semigroup.
    """

    assert Map({1: Sum(1), 2: Sum(2)}).concat(Map({1: Sum(1), 2: Sum(2)})) == Map({1: Sum(2), 2: Sum(4)})

# Generated at 2022-06-14 03:45:03.627459
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(2).concat(Max(1)).value == 2
    assert Max(10).concat(Max(11)).value == 11
    assert Max(100).concat(Max(100)).value == 100


# Generated at 2022-06-14 03:45:10.505465
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(1).concat(Max(2)) == Max(2)
    assert Max(1).concat(Max(1)) == Max(1)
    assert Max(2).concat(Max(1)) == Max(2)
    assert Max(-1).concat(Max(-100)) == Max(-1)
    assert Max(-1).concat(Max(-1)) == Max(-1)
    assert Max(-100).concat(Max(-1)) == Max(-1)


# Generated at 2022-06-14 03:45:17.474623
# Unit test for method concat of class Map
def test_Map_concat():
    assert Map({'a': Sum(5), 'b': All(True)}).concat(Map({'b': All(True), 'a': Sum(3)})) == Map({'a': Sum(8), 'b': All(True)})
    assert Map({'a': Sum(5), 'b': First(1)}).concat(Map({'b': First(True), 'a': Sum(3)})) == Map({'a': Sum(8), 'b': First(1)})
    assert Map({'a': Sum(5), 'b': Min(2)}).concat(Map({'b': Min(True), 'a': Sum(3)})) == Map({'a': Sum(8), 'b': Min(2)})

# Generated at 2022-06-14 03:45:26.111127
# Unit test for method concat of class Map
def test_Map_concat():
    test_map_a = Map({'a': Sum(1), 'b': Sum(2), 'c': Sum(3)})
    test_map_b = Map({'a': Sum(1), 'b': Sum(2), 'c': Sum(3)})
    result_map = test_map_a.concat(test_map_b)

    assert result_map.value['a'] == Sum(2)
    assert result_map.value['b'] == Sum(4)
    assert result_map.value['c'] == Sum(6)



# Generated at 2022-06-14 03:45:30.099533
# Unit test for method __str__ of class Map
def test_Map___str__():
    assert str(Map({1: Sum(2)})) == 'Map[value={1: Sum[value=2]}]'


# Generated at 2022-06-14 03:45:44.360455
# Unit test for method concat of class Map
def test_Map_concat():
    map_0 = Map({
        "key_0": Sum(0),
        "key_1": Sum(1),
        "key_2": Sum(2),
        "key_3": Sum(3),
        "key_4": Sum(4),
        "key_5": Sum(5),
    })
    map_1 = Map({
        "key_0": Sum(0),
        "key_1": Sum(10),
        "key_2": Sum(20),
        "key_3": Sum(30),
        "key_4": Sum(40),
        "key_5": Sum(50),
    })

    assert map_0.concat(map_1).value == map_1.concat(map_0).value
    assert map_0.concat(map_0).value == map_

# Generated at 2022-06-14 03:45:48.180353
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(4).concat(Max(2)).concat(Max(5)) == Max(5)
    assert Max(4).concat(Max(4)) == Max(4)


# Generated at 2022-06-14 03:45:49.529700
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(1)) == 'Max[value=1]'


# Generated at 2022-06-14 03:45:50.643091
# Unit test for constructor of class Map
def test_Map():
    assert Map({'key': 1}) == Map({'key': 1})



# Generated at 2022-06-14 03:45:52.408859
# Unit test for constructor of class First
def test_First():
    assert First(1).value == 1



# Generated at 2022-06-14 03:45:55.137972
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    assert str(Sum(1)) == 'Sum[value=1]'
    assert str(Sum(2)) == 'Sum[value=2]'


# Generated at 2022-06-14 03:45:58.642890
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    a = Sum(1)
    not_a = Sum(2)
    assert a.fold(lambda n: n + 1) == 2
    assert not_a.fold(lambda n: n + 1) == 3



# Generated at 2022-06-14 03:46:04.314604
# Unit test for method concat of class All
def test_All_concat():  # pragma: no cover
    assert All(True).concat(All(True)) == All(True)
    assert All(True).concat(All(False)) == All(False)
    assert All(False).concat(All(True)) == All(False)
    assert All(False).concat(All(False)) == All(False)


# Generated at 2022-06-14 03:46:06.763578
# Unit test for constructor of class All
def test_All():
    assert All(True).concat(All(False)).concat(All(True)) == All(False)
    assert All(True).concat(All(True)).concat(All(True)) == All(True)


# Generated at 2022-06-14 03:46:14.392581
# Unit test for constructor of class One
def test_One():
    assert One(1).value == 1
    assert One(0).value == 0
    assert One(True).value == True
    assert One(False).value == False
    assert One("r").value == "r"
    assert One("").value == ""


# Generated at 2022-06-14 03:46:17.359748
# Unit test for constructor of class Sum
def test_Sum():
    """
    Test for constructor of class Sum
    """
    assert Sum(1).value == 1
    assert Sum(None).value is None
    assert Sum(True).value is True
    assert Sum('Y').value == 'Y'



# Generated at 2022-06-14 03:46:20.332555
# Unit test for method __str__ of class Last
def test_Last___str__():
    value = 'foo'
    last = Last(value)
    assert last.__str__() == 'Last[value=foo]'


# Generated at 2022-06-14 03:46:24.203224
# Unit test for method concat of class Sum
def test_Sum_concat():
    a = Sum(1)
    b = Sum(2)
    c = a.concat(b)
    assert c == Sum(3)
    assert c.value == 3



# Generated at 2022-06-14 03:46:26.024485
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(5)) == 'Max[value=5]'


# Generated at 2022-06-14 03:46:27.301148
# Unit test for constructor of class Semigroup
def test_Semigroup():
    assert Semigroup(1).value == 1



# Generated at 2022-06-14 03:46:29.527788
# Unit test for method concat of class Max
def test_Max_concat():
    max_number = Max(1)
    max_number.concat(Max(2)) == Max(2)



# Generated at 2022-06-14 03:46:32.039734
# Unit test for constructor of class First
def test_First():
    assert str(First(34)) == 'Fist[value=34]'
    assert str(First('foo')) == 'Fist[value=foo]'
    assert str(First(34)) == 'Fist[value=' + str(34) + ']'
    assert str(First(34)) == 'Fist[value=' + repr(34) + ']'
    assert str(First(34)) == repr(First(34))


# Generated at 2022-06-14 03:46:33.666223
# Unit test for method __str__ of class Map
def test_Map___str__():
    assert(str(Map({"1": Sum(1)})) == "Map[value={'1': Sum[value=1]}]")

if __name__ == '__main__':
    test_Map___str__()

# Generated at 2022-06-14 03:46:35.238873
# Unit test for constructor of class Map
def test_Map():
    result = Map({'robin': Sum(1), 'max': Sum(2)})

    # test if the instance was created correctly
    assert result.value == {'robin': Sum(1), 'max': Sum(2)}



# Generated at 2022-06-14 03:46:47.337859
# Unit test for method concat of class Sum
def test_Sum_concat():
    assert Sum(1).concat(Sum(2)) == Sum(3)
    assert Sum(0).concat(Sum(0)) == Sum(0)
    assert Sum(1).concat(Sum(2)).concat(Sum(3)) == Sum(6)



# Generated at 2022-06-14 03:46:50.395636
# Unit test for constructor of class Map
def test_Map():
    assert Map({'a':First(1), 'b': First(2)}).value == {'a':First(1), 'b': First(2)}

# Generated at 2022-06-14 03:46:51.562692
# Unit test for constructor of class Min
def test_Min():
    assert Min(3) == Min(3)


# Generated at 2022-06-14 03:46:54.007969
# Unit test for method __str__ of class Min
def test_Min___str__():
    """
    Unit test for method __str__ of class Min
    """
    assert str(Min(10)) == 'Min[value=10]'


# Generated at 2022-06-14 03:46:57.744475
# Unit test for method concat of class Last
def test_Last_concat():
    """
    Test for Last.concat
    """
    a = Last(Last("a"))
    b = Last("b")
    c = a.concat(b)
    assert c == Last("b")


# Generated at 2022-06-14 03:46:59.648584
# Unit test for constructor of class Semigroup
def test_Semigroup():
    assert Semigroup(1).value == 1
    assert Semigroup("1") == Semigroup("1")
    assert Semigroup("1") != Semigroup("2")


# Generated at 2022-06-14 03:47:02.787429
# Unit test for method concat of class Max
def test_Max_concat():
    max_instance_1 = Max(1)
    max_instance_2 = Max(2)
    max_instance_3 = max_instance_1.concat(max_instance_2)
    assert max_instance_3.value == 2

# Generated at 2022-06-14 03:47:04.767614
# Unit test for method __str__ of class All
def test_All___str__():
    assert All(True).__str__() == 'All[value=True]'
    assert All(False).__str__() == 'All[value=False]'


# Generated at 2022-06-14 03:47:06.515500
# Unit test for constructor of class Sum
def test_Sum():  # pragma: no cover
    assert Sum(1).value == 1
    assert Sum(1) == Sum(1)
    assert Sum(1) != Sum(2)



# Generated at 2022-06-14 03:47:08.395604
# Unit test for method __str__ of class All
def test_All___str__():
    assert All(True).__str__() == "All[value=True]"



# Generated at 2022-06-14 03:47:23.968646
# Unit test for method __str__ of class Map
def test_Map___str__():
    assert str(Map({1: Sum(2), 3: Sum(4)})) == "Map[value={1: Sum[value=2], 3: Sum[value=4]}]"


# Generated at 2022-06-14 03:47:26.050097
# Unit test for constructor of class First
def test_First():
    assert First(1) == First(1), f"Constructor not working"


# Generated at 2022-06-14 03:47:29.791688
# Unit test for constructor of class All
def test_All():  # pragma: no cover
    all1 = All(True)
    assert all1.value == True
    all2 = All(False)
    assert all2.value == False
    assert all1 != all2


# Generated at 2022-06-14 03:47:32.301903
# Unit test for method concat of class Sum
def test_Sum_concat():
    assert Sum(1).concat(Sum(10)).fold(get) == 11
    assert Sum(7).concat(Sum(1)).fold(get) == 8



# Generated at 2022-06-14 03:47:34.825677
# Unit test for method __str__ of class Max
def test_Max___str__():
    a = Max(1)
    assert str(a) == "Max[value=1]"



# Generated at 2022-06-14 03:47:37.687910
# Unit test for method __str__ of class All
def test_All___str__():
    assert str(All(True)) == 'All[value=True]'
    assert str(All(123)) == 'All[value=123]'


# Generated at 2022-06-14 03:47:39.726616
# Unit test for constructor of class Max
def test_Max():
    """
    Unit test for constructor of class Max
    """

    assert Max(2).value == 2


# Generated at 2022-06-14 03:47:42.801975
# Unit test for method concat of class Sum
def test_Sum_concat():
    assert Sum(1).concat(Sum(2)) == Sum(3)



# Generated at 2022-06-14 03:47:46.575696
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    value = 0
    semigroup = Semigroup(value)
    assert semigroup == semigroup

# Generated at 2022-06-14 03:47:47.619876
# Unit test for constructor of class Min
def test_Min():
    assert Min(1).value == 1


# Generated at 2022-06-14 03:48:01.526527
# Unit test for method concat of class One
def test_One_concat():
    assert One(True) == One(True).concat(One(False))  # pragma: no cover


# Generated at 2022-06-14 03:48:02.662608
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    assert Semigroup(0).fold(lambda x: x if x == 0 else -1) == 0


# Generated at 2022-06-14 03:48:04.164584
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    assert str(Sum(1)) == 'Sum[value=1]'


# Generated at 2022-06-14 03:48:06.024317
# Unit test for constructor of class Sum
def test_Sum():
    sum = Sum(1)
    assert sum.value == 1


# Generated at 2022-06-14 03:48:10.844234
# Unit test for constructor of class Map
def test_Map():
    """
    Test if constructor works.
    """
    assert Map({'one': Sum(1), 'two': Sum(2), 'three': Sum(3)}) == Map({
        'one': Sum(1),
        'two': Sum(2),
        'three': Sum(3),
    })



# Generated at 2022-06-14 03:48:12.086821
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(2)) == "Max[value=2]"


# Generated at 2022-06-14 03:48:17.831951
# Unit test for method __str__ of class All
def test_All___str__():  # pragma: no cover
    assert str(All(None)) == "All[value=None]"
    assert str(All(True)) == "All[value=True]"
    assert str(All(False)) == "All[value=False]"
    assert str(All(1)) == "All[value=1]"
    assert str(All("a")) == "All[value=a]"



# Generated at 2022-06-14 03:48:21.715213
# Unit test for constructor of class Semigroup
def test_Semigroup():  # pragma: no cover
    assert Semigroup(1) == Semigroup(1)
    assert Semigroup(1) != Semigroup(2)


# Unit tests for class Sum

# Generated at 2022-06-14 03:48:25.645795
# Unit test for method concat of class Map
def test_Map_concat():
    assert Map({"a": Sum(1), "b": Sum(3)}).concat(
        Map({"b": Sum(2), "c": Sum(4)})
    ) == Map({"a": Sum(1), "b": Sum(5), "c": Sum(4)})

# Generated at 2022-06-14 03:48:27.406705
# Unit test for method __str__ of class Last
def test_Last___str__():
    last = Last(42)
    assert last.__str__() == 'Last[value=42]'



# Generated at 2022-06-14 03:48:40.912915
# Unit test for constructor of class Map
def test_Map():
    m1 = Map({'a': Sum(1), 'b': Sum(2)})
    assert m1.value == {'a': Sum(1), 'b': Sum(2)}, "Map value is incorrect"


# Generated at 2022-06-14 03:48:42.706199
# Unit test for method __str__ of class Last
def test_Last___str__():
    assert Last(4).__str__() == 'Last[value=4]'


# Generated at 2022-06-14 03:48:43.357026
# Unit test for method __str__ of class First
def test_First___str__():
    assert str(First(True)) == 'Fist[value=True]'


# Generated at 2022-06-14 03:48:55.041247
# Unit test for method concat of class Map
def test_Map_concat():
    m1 = Map({'a': Sum(1), 'b': Sum(2)})
    m2 = Map({'a': Sum(10), 'b': Sum(20)})
    assert m1.concat(m2) == Map({'a': Sum(11), 'b': Sum(22)})

    m1 = Map({'a': All(True), 'b': All(False)})
    m2 = Map({'a': All(False), 'b': All(True)})
    assert m1.concat(m2) == Map({'a': All(False), 'b': All(False)})

    m1 = Map({'a': One(False), 'b': One(True)})
    m2 = Map({'a': One(False), 'b': One(True)})
    assert m1.concat

# Generated at 2022-06-14 03:49:00.767502
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    assert Sum(1) == Sum(1) == Semigroup.neutral(Sum)
    assert not Sum(1) == Sum(2)
    assert All(True) == All(True) == Semigroup.neutral(All)
    assert not All(True) == All(False)
    assert One(True) == One(True) == Semigroup.neutral(One)
    assert not One(True) == One(False)
    assert First(1) == First(1)
    assert not First(1) == First(2)
    assert Last(1) == Last(1)
    assert not Last(1) == Last(2)
    assert Map({1: First(1)}) == Map({1: First(1)})
    assert not Map({1: First(1)}) == Map({2: First(2)})

# Generated at 2022-06-14 03:49:04.259021
# Unit test for method concat of class One
def test_One_concat():
    # Setup
    one = One(True)

    # Exercise
    actual = one.concat(One(False))

    # Assert
    assert actual.value == True


# Generated at 2022-06-14 03:49:08.845782
# Unit test for method concat of class All
def test_All_concat():
    """
    Test that the concat method of the All class works correctly.
    """
    assert All(True).concat(All(True)) == All(True)
    assert All(True).concat(All(False)) == All(False)
    assert All(False).concat(All(True)) == All(False)
    assert All(False).concat(All(False)) == All(False)



# Generated at 2022-06-14 03:49:12.842919
# Unit test for method __str__ of class All
def test_All___str__():
    assert str(All(True)) == 'All[value=True]'
    assert str(All(False)) == 'All[value=False]'



# Generated at 2022-06-14 03:49:16.844947
# Unit test for method concat of class Min
def test_Min_concat():
    """
    Min is a Monoid that will combines 2 numbers, resulting in the smallest of the two.
    """
    assert Min(1).concat(Min(2)) == Min(1)
    assert Min(1).concat(Min(0)) == Min(0)

# Generated at 2022-06-14 03:49:20.856328
# Unit test for method concat of class All
def test_All_concat():
    three_all = All(True).concat(All(True))
    two_all = three_all.concat(All(False))

    assert two_all.value == False and three_all.value == True


# Generated at 2022-06-14 03:49:47.130133
# Unit test for constructor of class One
def test_One():
    one = One(True)
    assert one.value is True


# Generated at 2022-06-14 03:49:50.884160
# Unit test for constructor of class One
def test_One():
    a = One(True)
    b = One(False)
    c = One(1)
    d = One(None)
    assert a.value == True
    assert b.value == False
    assert c.value == 1
    assert d.value == None



# Generated at 2022-06-14 03:49:56.707296
# Unit test for method concat of class Max
def test_Max_concat():
    """
    Tests the method concat of class Max
    """
    assert Max(5).concat(Max(2)) == Max(5)
    assert Max(2).concat(Max(5)) == Max(5)
    assert Max(5).concat(Max(5)) == Max(5)



# Generated at 2022-06-14 03:49:59.801228
# Unit test for constructor of class Last
def test_Last():
    # Given
    value = 'last-value'

    # When
    last = Last(value)

    # Then
    assert last.value == value


# Generated at 2022-06-14 03:50:04.980478
# Unit test for constructor of class Last
def test_Last():
    class TestClass:
        def __init__(self, value):
            self.value = value

    assert Last(TestClass(1)).concat(
        Last(TestClass(2))
    ).value.value == 2


# Generated at 2022-06-14 03:50:08.208034
# Unit test for constructor of class All
def test_All():
    assert All(True) == All(True)  # __eq__ implementation
    assert All(False) == All(False)
    assert All(True) != All(False)



# Generated at 2022-06-14 03:50:10.367484
# Unit test for constructor of class Max
def test_Max():
    assert Max(1).value == 1
# Use of the unit test
#test_Max()


# Generated at 2022-06-14 03:50:11.931366
# Unit test for constructor of class Min
def test_Min():
    assert Min(20).value == 20


# Generated at 2022-06-14 03:50:14.428575
# Unit test for method concat of class First
def test_First_concat():
    assert First("a") == First("a").concat(First("b"))



# Generated at 2022-06-14 03:50:16.565900
# Unit test for method __str__ of class Max
def test_Max___str__():
    actual = str(Max(3))
    assert actual == "Max[value=3]"


# Generated at 2022-06-14 03:50:45.485430
# Unit test for method concat of class Last
def test_Last_concat():  # pragma: no cover
    a = Last(1)
    b = Last(2)
    assert a.concat(b) == Last(2)


# Generated at 2022-06-14 03:50:47.805800
# Unit test for method __str__ of class One
def test_One___str__():
    one = One(True)
    assert str(one) == 'One[value=True]'


# Generated at 2022-06-14 03:50:49.768762
# Unit test for method __str__ of class All
def test_All___str__():
    assert str(All(True)) == 'All[value=True]'


# Generated at 2022-06-14 03:50:51.215775
# Unit test for method __str__ of class Min
def test_Min___str__():
    assert 'Min[value=0]' == str(Min(0))


# Generated at 2022-06-14 03:50:54.504650
# Unit test for method concat of class First
def test_First_concat():
    """
     Test for concat method of class First
    """
    assert First('first').concat(First('second')).value == 'first'



# Generated at 2022-06-14 03:50:58.538578
# Unit test for method concat of class Sum
def test_Sum_concat():
    """
    Given: a Sum with value 4
    When: concat with Sum with value 5
    Then: Sum with value 9 must be returned
    """
    result = Sum(4).concat(Sum(5))
    assert result == Sum(9)


# Generated at 2022-06-14 03:51:01.757559
# Unit test for method __str__ of class Min
def test_Min___str__():
    # Given
    monoid = Min(1)

    # When
    string = str(monoid)

    # Then
    assert string == "Min[value=1]"



# Generated at 2022-06-14 03:51:03.485842
# Unit test for constructor of class Min
def test_Min():  # pragma: no cover
    min1 = Min(1)
    min2 = Min(2)
    min2.concat(min1)


# Generated at 2022-06-14 03:51:04.373128
# Unit test for constructor of class Last
def test_Last():
    assert Last(5).value == 5


# Generated at 2022-06-14 03:51:06.118447
# Unit test for constructor of class Sum
def test_Sum(): # pragma: no cover
    assert Sum(5) == Sum(5)


# Generated at 2022-06-14 03:52:00.045490
# Unit test for method concat of class Last
def test_Last_concat():
    assert Last(15).concat(Last(5)) == Last(5)



# Generated at 2022-06-14 03:52:01.658350
# Unit test for method __str__ of class All
def test_All___str__():
    assert str(All(True)) == 'All[value=True]'



# Generated at 2022-06-14 03:52:04.147417
# Unit test for constructor of class Map
def test_Map():
    assert Map({1: First('a'), 2: All(False)}) == Map({1: First('a'), 2: All(False)})



# Generated at 2022-06-14 03:52:05.782797
# Unit test for method __str__ of class Max
def test_Max___str__():  # pragma: no cover
    obj = Max(5)
    assert '5' in str(obj)


# Generated at 2022-06-14 03:52:18.881517
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    """
    Given a Semigroup(s)
    The fold() method apply the function f to its value
    And return the result of the fuction
    """
    assert Sum(3).fold(lambda x: x * 4) == 12
    assert First('hello').fold(lambda x: x * 4) == 'hello'
    assert Last(2).fold(lambda x: x ** 2) == 4
    assert All('hello').fold(lambda x: x[0]) == 'h'
    assert One(2).fold(lambda x: x ** 2) == 4
    assert Map({'a': Sum(1), 'b': Sum(2)}).fold(lambda x: x.items()) == dict(a=1, b=2).items()
    assert Max(2).fold(lambda x: x ** 2) == 4
    assert Min(2).fold

# Generated at 2022-06-14 03:52:19.871206
# Unit test for constructor of class First
def test_First():
    assert First(1) == First(1)



# Generated at 2022-06-14 03:52:25.046239
# Unit test for method concat of class Map
def test_Map_concat():
    m1 = Map({"a": Sum(1), "b": Sum(2)})
    m2 = Map({"a": Sum(10), "c": Sum(20)})
    assert m1.concat(m2) == Map({"a": Sum(11), "b": Sum(2), "c": Sum(20)})



# Generated at 2022-06-14 03:52:28.499082
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    # given
    a = Semigroup(2)
    b = Semigroup(2)
    c = Semigroup(3)
    # then
    assert a.__eq__(b) is True
    assert a.__eq__(c) is False



# Generated at 2022-06-14 03:52:34.048423
# Unit test for method concat of class Last
def test_Last_concat():
    """
    :return: no return, only print testing result
    """
    try:
        assert Last(3).concat(Last(4)) == Last(4)
        print('test_Last_concat OK')
    except AssertionError as e:
        print('test_Last_concat Failed')


# Generated at 2022-06-14 03:52:44.367888
# Unit test for constructor of class One
def test_One():
    assert One(1) == One(1)
    assert str(One(1)) == 'One[value=1]'
    assert One(1).concat(One(2)) == One(1)
    assert One(0).concat(One(2)) == One(2)
    assert One(0).concat(One(0)) == One(0)
    assert One.neutral().concat(One(0)) == One(0)
    assert One.neutral().concat(One(1)) == One(1)
    assert One(1).fold(int) == 1
