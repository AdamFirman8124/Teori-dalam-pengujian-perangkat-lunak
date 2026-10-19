

# Generated at 2022-06-14 03:44:30.444263
# Unit test for constructor of class Sum
def test_Sum():
    assert Sum(0) == Sum.neutral()
    assert Sum(0).concat(Sum(1)) == Sum(1)
    assert Sum(0).concat(Sum(6)) == Sum(6)

    assert str(Sum(0)) == 'Sum[value=0]'
    assert str(Sum(4)) == 'Sum[value=4]'


# Generated at 2022-06-14 03:44:32.375261
# Unit test for method concat of class Sum
def test_Sum_concat():
    assert Sum(6).concat(Sum(2)) == Sum(8)


# Generated at 2022-06-14 03:44:41.839452
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    assert Sum(2).fold(lambda x: x + 2) == 4
    assert All(False).fold(lambda x: not x) is True
    assert One(True).fold(lambda x: not x) is False
    assert First(2).fold(lambda x: x + 2) == 2
    assert Last(2).fold(lambda x: x - 1) == 2
    assert Map({"1": First(2), "2": Last(2)}).fold(
        lambda x: x["1"].value + x["2"].value
    ) == 4
    assert Max(1).fold(lambda x: x - 2) == 1
    assert Min(2).fold(lambda x: x + 2) == 2

# Generated at 2022-06-14 03:44:44.896222
# Unit test for method concat of class All
def test_All_concat():
    assert All(True).concat(All(True)) == All(True)
    assert All(False).concat(All(True)) == All(False)
    assert All(False).concat(All(False)) == All(False)
    assert All(True).concat(All(False)) == All(False)


# Generated at 2022-06-14 03:44:48.363502
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    """
    >>> test_Semigroup_fold()
    True
    """
    assert(Sum(2).fold(lambda a: a + 1) == 3)



# Generated at 2022-06-14 03:44:50.345492
# Unit test for constructor of class One
def test_One():
    assert One(True)


# Generated at 2022-06-14 03:44:54.199179
# Unit test for constructor of class Map
def test_Map():
    m = Map({'a': Sum(1), 'b': Sum(2), 'c': Sum(3)})
    assert m.value == {'a': Sum(1), 'b': Sum(2), 'c': Sum(3)}


# Generated at 2022-06-14 03:44:57.416901
# Unit test for method __str__ of class Map
def test_Map___str__():
    m = Map({1: Sum(1), 2: Sum(2), 3: Sum(3)})
    assert str(m) == 'Map[value={1: Sum[value=1], 2: Sum[value=2], 3: Sum[value=3]}]'


# Generated at 2022-06-14 03:45:02.253195
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(1).concat(Min(2)) == Min(1)
    assert Min(2).concat(Min(1)) == Min(1)


# Generated at 2022-06-14 03:45:06.601741
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    """
    Unit test for method Sum.__str__()
    """
    assert str(Sum(123)) == 'Sum[value=123]'


# Generated at 2022-06-14 03:45:09.722723
# Unit test for method __str__ of class All
def test_All___str__():
    assert str(All(10)) == 'All[value=10]'


# Generated at 2022-06-14 03:45:12.377966
# Unit test for method __str__ of class All
def test_All___str__(): # pragma: no cover
    assert str(All(True)) == 'All[value=True]'
    assert str(All(False)) == 'All[value=False]'
    assert str(All(10)) == 'All[value=True]'


# Generated at 2022-06-14 03:45:14.568996
# Unit test for constructor of class Map
def test_Map():
    assert Map({'a': First('foo'), 'b': First('bar')}) == Map({'a': First('foo'), 'b': First('bar')})


# Generated at 2022-06-14 03:45:16.395469
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(3)) == "Max[value=3]"


# Generated at 2022-06-14 03:45:18.104896
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    assert Sum(3).fold(lambda x: x + 1) == 4



# Generated at 2022-06-14 03:45:26.010374
# Unit test for method __str__ of class Last
def test_Last___str__(): # pragma: no cover
    """
    Unit test for method __str__ of class Last
    """

    assert str(Last(1)) == 'Last[value=1]'
    assert str(Last('string')) == 'Last[value=string]'
    assert str(Last([])) == 'Last[value=[]]'
    assert str(Last({})) == 'Last[value={}]'
    assert str(Last(object)) == 'Last[value=<class \'object\'>]'


# Generated at 2022-06-14 03:45:28.697125
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    assert Semigroup(1) == Semigroup(1)
    assert not Semigroup(1) == Semigroup(2)
    return 'Done'


# Generated at 2022-06-14 03:45:30.872657
# Unit test for constructor of class Min
def test_Min():
    assert Min(1) == Min(1)


# Generated at 2022-06-14 03:45:33.551895
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    s1 = Sum(1)
    s2 = Sum(1)
    assert s1 == s2



# Generated at 2022-06-14 03:45:36.550968
# Unit test for constructor of class One
def test_One():
    one = One(True)
    assert one.value == True
    assert str(one) == 'One[value=True]'



# Generated at 2022-06-14 03:45:41.837388
# Unit test for constructor of class Map
def test_Map():
    assert Map({"a": Sum(1), "b": Sum(2)}).fold(lambda x: x) == {"a": Sum(1), "b": Sum(2)}


# Generated at 2022-06-14 03:45:48.400431
# Unit test for method concat of class All
def test_All_concat():
    result = All(True).concat(All(True))
    assert result == All(True)

    result = All(True).concat(All(False))
    assert result == All(False)

    result = All(False).concat(All(True))
    assert result == All(False)

    result = All(False).concat(All(False))
    assert result == All(False)



# Generated at 2022-06-14 03:45:50.102007
# Unit test for constructor of class Semigroup
def test_Semigroup():
    assert Semigroup(1).value == 1
    assert Semigroup(5.5).value == 5.5


# Generated at 2022-06-14 03:45:55.616707
# Unit test for method __str__ of class Last
def test_Last___str__():
    assert str(Last(1)) == 'Last[value=1]'
    assert str(Last(2.5)) == 'Last[value=2.5]'
    assert str(Last('qwerty')) == 'Last[value=qwerty]'


# Generated at 2022-06-14 03:45:56.481187
# Unit test for constructor of class One
def test_One():
    assert One(True).value == True


# Generated at 2022-06-14 03:45:58.689760
# Unit test for constructor of class Semigroup
def test_Semigroup():
    assert Semigroup(42).value == 42
    assert Semigroup(42).concat(Semigroup(67)) == Semigroup(109)


# Generated at 2022-06-14 03:46:00.138880
# Unit test for constructor of class One
def test_One():
    one = One(True)
    assert one.value == True


# Generated at 2022-06-14 03:46:04.616340
# Unit test for method concat of class Sum
def test_Sum_concat():
    assert Sum(3).concat(Sum(4)) == Sum(7)
    assert Sum(-4).concat(Sum(4)) == Sum(0)
    assert Sum(4).concat(Sum(4)) == Sum(8)

# Test method neutral() of class Sum

# Generated at 2022-06-14 03:46:06.389479
# Unit test for method __str__ of class Last
def test_Last___str__():
    assert '{}'.format(Last('test')) == 'Last[value=test]'


# Generated at 2022-06-14 03:46:10.568525
# Unit test for method concat of class Map
def test_Map_concat():
    assert Map({"a": Sum(1)}).concat(Map({"a": Sum(1)})) == Map({"a": Sum(2)})
    assert Map({"a": First(1)}).concat(Map({"a": Last(2)})) == Map({"a": First(1)})

# Generated at 2022-06-14 03:46:14.915269
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(0)) == 'Max[value=0]'



# Generated at 2022-06-14 03:46:16.178282
# Unit test for constructor of class Sum
def test_Sum():
    sum_ = Sum(2)
    assert sum_.value == 2


# Generated at 2022-06-14 03:46:18.608978
# Unit test for constructor of class All
def test_All():
    assert All(True) == All(True)
    assert All(True) != All(False)
    assert All(False) != All(True)
    assert All(False) == All(False)


# Generated at 2022-06-14 03:46:20.816992
# Unit test for method __str__ of class Max
def test_Max___str__():
    """
    Unit test
    """
    print('Max.__str__(): ', Max(10))  # Max.__str__():  Max[value=10]


# Generated at 2022-06-14 03:46:23.895452
# Unit test for method concat of class One
def test_One_concat():
    assert One(True).concat(One(False)) == One(True)
    assert One(False).concat(One(True)) == One(True)
    assert One(False).concat(One(False)) == One(False)
    assert One(True).concat(One(True)) == One(True)


# Generated at 2022-06-14 03:46:31.696579
# Unit test for method concat of class All
def test_All_concat():
    """
    test_All_concat
    """

    # Arrange
    all1 = All(True)
    all2 = All(True)
    all3 = All(True)
    all4 = All(False)
    all5 = All(True)

    # Act
    concated_all_true = all1.concat(all2).concat(all3)
    concated_all_false = all2.concat(all4).concat(all5)

    # Assert
    assert concated_all_true.value == True
    assert concated_all_false.value == False



# Generated at 2022-06-14 03:46:32.561781
# Unit test for constructor of class Last
def test_Last():
    assert str(Last(0).fold(str)) == "Last[value=0]"

# Generated at 2022-06-14 03:46:34.716353
# Unit test for constructor of class Semigroup
def test_Semigroup():
    """Unit test for constructor Semigroup class."""
    semigroup = Semigroup(1)
    assert semigroup.value == 1



# Generated at 2022-06-14 03:46:38.084929
# Unit test for method __str__ of class Map
def test_Map___str__():
    assert str(Map({"a": 1, "b": 2})) == "Map[value={'a': 1, 'b': 2}]"  # pragma: no cover


# Generated at 2022-06-14 03:46:39.586830
# Unit test for method __str__ of class One
def test_One___str__():
    m = One('foo')
    assert str(m) == 'One[value=foo]'


# Generated at 2022-06-14 03:46:47.603272
# Unit test for method __str__ of class All
def test_All___str__():
    assert 'All[value=True]' == str(All(True))
    assert 'All[value=None]' == str(All(None))
    assert 'All[value=False]' == str(All(False))


# Generated at 2022-06-14 03:46:49.786718
# Unit test for method concat of class Max
def test_Max_concat():
    first = Max(32)
    second = Max(54)
    assert first.concat(second) == Max(54)



# Generated at 2022-06-14 03:46:54.924167
# Unit test for constructor of class Min
def test_Min():
    """
    Min is a Monoid that will combines 2 numbers, resulting in the smallest of the two.
    """
    min_1 = Min(2)
    min_2 = Min(3)

    # test_Min = Min(min_1 + min_2)
    result = min_1.concat(min_2)

    print(result)



test_Min()

# Generated at 2022-06-14 03:47:04.594318
# Unit test for method concat of class One
def test_One_concat():
    assert One(3).concat(One(True)) == One(True)  # pragma: no cover
    assert One(0).concat(One(False)) == One(0)  # pragma: no cover
    assert One(None).concat(One(False)) == One(False)  # pragma: no cover
    assert One(None).concat(One(True)) == One(True)  # pragma: no cover
    assert One(False).concat(One(True)) == One(True)  # pragma: no cover
    assert One(True).concat(One(True)) == One(True)  # pragma: no cover
    assert One("").concat(One("")) == One("")  # pragma: no cover
    assert One("").concat(One("Foo")) == One("Foo") 

# Generated at 2022-06-14 03:47:06.553976
# Unit test for method __str__ of class All
def test_All___str__():  # pragma: no cover
    assert str(All(True)) == 'All[value=True]'



# Generated at 2022-06-14 03:47:07.893603
# Unit test for method concat of class First
def test_First_concat():
    first = First(1)
    last = Last(2)

    result = first.concat(last)

    assert first == result


# Generated at 2022-06-14 03:47:09.178260
# Unit test for constructor of class Max
def test_Max():  # pragma: no cover
    a = Max(5)
    assert a.value == 5


# Generated at 2022-06-14 03:47:12.948237
# Unit test for method concat of class First
def test_First_concat():
    assert First(1).concat(First(2)) == First(1)


# Generated at 2022-06-14 03:47:17.166003
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    assert Sum(1) == Sum(1)
    assert Min(2) == Min(2)
    assert All(True) == All(True)
    assert All(False) == All(False)
    assert First(1) == First(1)
    assert First(2) == First(2)
    assert Last(1) == Last(1)
    assert Last(2) == Last(2)



# Generated at 2022-06-14 03:47:18.777128
# Unit test for constructor of class Semigroup
def test_Semigroup():
    """
    >>> sg_test = Semigroup(2)
    >>> sg_test.value
    2

    """

testmod()

# Generated at 2022-06-14 03:47:24.240000
# Unit test for constructor of class First
def test_First():
    # GIVEN
    value = "a"

    # WHEN
    first = First(value)

    # THEN
    assert first.value == value



# Generated at 2022-06-14 03:47:25.886587
# Unit test for method __str__ of class All
def test_All___str__():
    assert str(All(True)) == 'All[value=True]'



# Generated at 2022-06-14 03:47:33.715203
# Unit test for method concat of class Sum
def test_Sum_concat():
    """
    Test for Sum.concat method
    """
    assert Sum(1).concat(Sum(2)) == Sum(3)
    assert Sum(2).concat(Sum(3)) == Sum(5)
    assert Sum(3).concat(Sum(4)) == Sum(7)
    assert Sum(4).concat(Sum(5)) == Sum(9)



# Generated at 2022-06-14 03:47:35.337962
# Unit test for method concat of class First
def test_First_concat():
    assert First(1).concat(First(2)) == First(1)

# Generated at 2022-06-14 03:47:38.048785
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    assert str(Sum(10)) == 'Sum[value=10]'



# Generated at 2022-06-14 03:47:39.609012
# Unit test for method __str__ of class Last
def test_Last___str__():
    assert str(Last(4)) == 'Last[value=4]'



# Generated at 2022-06-14 03:47:42.433829
# Unit test for method __str__ of class First
def test_First___str__():
    assert str(First(None)) == 'First[value=None]'


# Generated at 2022-06-14 03:47:44.468569
# Unit test for constructor of class Last
def test_Last():
    assert Last(100) == Last(100)
    assert Last(100) != Last(200)


# Generated at 2022-06-14 03:47:45.908809
# Unit test for constructor of class Sum
def test_Sum():
    assert Sum(0) == Sum(Sum.neutral_element)



# Generated at 2022-06-14 03:47:49.627616
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(0)) == "Max[value=0]"
    assert str(Max(1)) == "Max[value=1]"
    assert str(Max(1.1)) == "Max[value=1.1]"


# Generated at 2022-06-14 03:47:56.417484
# Unit test for constructor of class First
def test_First():
    first = First(1)
    assert first.value == 1

# Generated at 2022-06-14 03:47:59.894754
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(0).concat(Max(1)).value == 1
    assert Max(1).concat(Max(1)).value == 1
    assert Max(4).concat(Max(2)).value == 4



# Generated at 2022-06-14 03:48:01.863022
# Unit test for method __str__ of class First
def test_First___str__():
    """
    Unit test for method __str__ of class First
    """
    value = 10
    first = First(value)
    assert str(first) == 'Fist[value=10]'


# Generated at 2022-06-14 03:48:03.870363
# Unit test for method __str__ of class First
def test_First___str__():
    assert str(First(1)) == 'Fist[value=1]'


# Generated at 2022-06-14 03:48:06.140536
# Unit test for method concat of class First
def test_First_concat():  # pragma: no cover
    assert First(1).concat(First(2)) == First(1)


# Generated at 2022-06-14 03:48:07.742189
# Unit test for constructor of class Semigroup
def test_Semigroup():
    assert Semigroup(100) == Semigroup(100)



# Generated at 2022-06-14 03:48:11.849954
# Unit test for constructor of class Map
def test_Map():  # pragma: no cover
    # given
    map_value = {'name': Sum(1), 'age': Min(1)}
    map = Map(map_value)

    # when
    result = map.value

    # then
    assert result == map_value


# Generated at 2022-06-14 03:48:13.838325
# Unit test for method __str__ of class Max
def test_Max___str__():
    m = Max(2)
    assert m.__str__() == 'Max[value=2]'


# Generated at 2022-06-14 03:48:20.240938
# Unit test for method concat of class Map
def test_Map_concat():
    a = Map({'name': One('Peter'), 'id': Last(42)})
    b = Map({'name': Last('Adam'), 'id': Last(131)})
    c = a.concat(b)

    assert c.value['name'].value == 'Adam'
    assert c.value['id'].value == 131

# Generated at 2022-06-14 03:48:24.202505
# Unit test for constructor of class All
def test_All():
    assert All(True) == All(True)
    assert All(False) != All(True)
    assert All(True) != All(False)
    assert All(False) == All(False)


# Generated at 2022-06-14 03:48:37.718812
# Unit test for constructor of class Semigroup
def test_Semigroup():
    assert Semigroup(42).value == 42
    assert Semigroup(42) == Semigroup(42)
    assert Semigroup(42) != Semigroup(100500)



# Generated at 2022-06-14 03:48:41.172723
# Unit test for method __str__ of class Max
def test_Max___str__():
    max_value = Max(2)
    assert str(max_value) == "Max[value=2]"



# Generated at 2022-06-14 03:48:42.943589
# Unit test for method __str__ of class One
def test_One___str__():
    a = One(True)
    assert a.__str__() == "One[value=True]"



# Generated at 2022-06-14 03:48:46.966305
# Unit test for method concat of class All
def test_All_concat():
    assert All(True).concat(All(True)) == All(True)
    assert All(True).concat(All(False)) == All(False)
    assert All(False).concat(All(False)) == All(False)
    assert All(True).concat(All(True)).concat(All(False)) == All(False)


# Generated at 2022-06-14 03:48:51.512350
# Unit test for method concat of class Max
def test_Max_concat():
    semigroup = Max(0)
    other_semigroup = Max(1)
    expected = Max(1)
    actual = semigroup.concat(other_semigroup)
    assert expected == actual


# Generated at 2022-06-14 03:49:00.556495
# Unit test for method concat of class All
def test_All_concat():
    semigroup_all_1 = All(True)
    semigroup_all_2 = All(True)
    semigroup_all_3 = All(False)

    assert semigroup_all_1.concat(semigroup_all_2) == All(True)
    assert semigroup_all_1.concat(semigroup_all_3) == All(False)
    assert semigroup_all_3.concat(semigroup_all_1) == All(False)
    assert semigroup_all_2.concat(semigroup_all_1) == All(True)
    assert semigroup_all_1.concat(semigroup_all_1) == All(True)
    assert semigroup_all_3.concat(semigroup_all_3) == All(False)



# Generated at 2022-06-14 03:49:01.828718
# Unit test for method __str__ of class Last
def test_Last___str__():
    assert str(Last(1)) == 'Last[value=1]'


# Generated at 2022-06-14 03:49:04.562440
# Unit test for method concat of class First
def test_First_concat():
    assert First('foobar').concat(First('qux')).value == 'foobar'


# Generated at 2022-06-14 03:49:07.194078
# Unit test for constructor of class Last
def test_Last():
    assert Last(1).value == 1
    assert Last('x').value == 'x'
    assert Last(True).value is True
    assert Last(False).value is False


# Generated at 2022-06-14 03:49:13.668377
# Unit test for method concat of class One
def test_One_concat():

    def concat(a, b):
        return One(a).concat(One(b)).value
    assert concat(True, True) is True
    assert concat(True, False) is True
    assert concat(False, True) is True
    assert concat(False, False) is False



# Generated at 2022-06-14 03:49:40.985356
# Unit test for method concat of class Map
def test_Map_concat():
    assert Map({"a": Sum(1), "b": Sum(2)}).concat(Map({"a": Sum(3), "b": Sum(4)})) == Map({"a": Sum(4), "b": Sum(6)})


# Generated at 2022-06-14 03:49:44.096298
# Unit test for method concat of class All
def test_All_concat():
    assert All(True).concat(All(True)).value is True
    assert All(True).concat(All(False)).value is False
    assert All(False).concat(All(True)).value is False
    assert All(False).concat(All(False)).value is False


# Generated at 2022-06-14 03:49:47.461330
# Unit test for constructor of class Semigroup
def test_Semigroup():  # pragma: no cover
    value = 42
    semigroup = Semigroup(value)
    assert semigroup.value == value


# Generated at 2022-06-14 03:49:48.714400
# Unit test for method __str__ of class Map
def test_Map___str__():
    assert str(Map({'a': Sum(1)})) == 'Map[value={\'a\': Sum[value=1]}]'


# Generated at 2022-06-14 03:49:50.458830
# Unit test for constructor of class Min
def test_Min():
    assert Min(5).value == 5

test_Min()


# Generated at 2022-06-14 03:49:52.189224
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(1).concat(Max(2)) == Max(2)
    assert Max(10).concat(Max(2)) == Max(10)


# Generated at 2022-06-14 03:49:53.753257
# Unit test for constructor of class Sum
def test_Sum():
    assert Sum(1).value == 1


# Generated at 2022-06-14 03:49:56.797092
# Unit test for method __str__ of class Map
def test_Map___str__():
    assert str(Map({'a': Sum(1), 'b': Sum(2)})) == 'Map[value={"a": Sum[value=1], "b": Sum[value=2]}]'


# Generated at 2022-06-14 03:50:03.353181
# Unit test for method concat of class Map
def test_Map_concat():
    Map({'a': Sum(1), 'b': Sum(2), 'c': Sum(3)}).concat(Map({'a': Sum(4), 'b': Sum(5), 'c': Sum(6)})) == Map({'a': Sum(5), 'b': Sum(7), 'c': Sum(9)})

# Generated at 2022-06-14 03:50:05.950016
# Unit test for constructor of class Min
def test_Min():
    assert Min(1) == Min(1)
    assert Min(1) != Min(2)
    assert Min(1).value == 1


# Generated at 2022-06-14 03:50:55.637366
# Unit test for constructor of class Max
def test_Max():
    assert Max(1).value == 1


# Generated at 2022-06-14 03:50:57.293189
# Unit test for method concat of class First
def test_First_concat():
    assert First(1).concat(First(2)) == First(1)



# Generated at 2022-06-14 03:50:58.844156
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(0)) == 'Max[value=0]'


# Generated at 2022-06-14 03:51:03.106636
# Unit test for method concat of class Map
def test_Map_concat():
    map_a = Map({'a': Sum(1), 'b': Sum(2)})
    map_b = Map({'a': Sum(3), 'b': Sum(4)})
    assert map_a.concat(map_b) == Map({'a': Sum(4), 'b': Sum(6)})

# Generated at 2022-06-14 03:51:04.297353
# Unit test for constructor of class First
def test_First():
    f = First(1)
    assert f.value == 1, "First should have value 1"



# Generated at 2022-06-14 03:51:05.975497
# Unit test for method __str__ of class Min
def test_Min___str__():
    assert str(Min(5)) == 'Min[value=5]'


# Generated at 2022-06-14 03:51:09.300852
# Unit test for constructor of class One
def test_One():  # pragma: no cover
    result = One(True)
    assert result.value == True
test_One()


# Generated at 2022-06-14 03:51:20.490309
# Unit test for method concat of class Map
def test_Map_concat():
    values = Map({
        'one': First(1),
        'two': First(2),
        'three': First(3),
        'four': First(4),
    })
    new_values = Map({
        'five': First(5),
        'six': First(6),
        'seven': First(7),
        'eight': First(8),
    })
    new_values.concat(values)

    assert isinstance(values, Map)
    assert isinstance(new_values, Map)


# Generated at 2022-06-14 03:51:22.717056
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    assert str(Sum(5)) == 'Sum[value=5]'


# Generated at 2022-06-14 03:51:24.927238
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert 'Max[value=2]' == str(Max(2))



# Generated at 2022-06-14 03:53:19.062531
# Unit test for method __str__ of class All
def test_All___str__():
    assert All(True).__str__() == 'All[value=True]'


# Generated at 2022-06-14 03:53:22.421159
# Unit test for method concat of class First
def test_First_concat():  # pragma: no cover
    result = First(3).concat(First(2))
    expected = First(3)
    assert result == expected



# Generated at 2022-06-14 03:53:25.085125
# Unit test for constructor of class Max
def test_Max():
    x = Max(4)
    y = Max(1)

    assert x.value == 4
    assert y.value == 1

# Unit Test for method concat in class Max

# Generated at 2022-06-14 03:53:29.498938
# Unit test for method __str__ of class Map
def test_Map___str__():
    assert str(Map({'a': Sum(1), 'b': Sum(2)})) == 'Map[value={\'a\': Sum[value=1], \'b\': Sum[value=2]}]'



# Generated at 2022-06-14 03:53:31.789998
# Unit test for constructor of class Max
def test_Max():
    assert (Max(5) == Max(5)).value
    assert (Max(5) == Max(10)).value is False


# Generated at 2022-06-14 03:53:35.588446
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(1).concat(Min(2)) == Min(1)
    assert Min(2).concat(Min(1)) == Min(1)
    assert Min(10).concat(Min(1)) == Min(1)


# Generated at 2022-06-14 03:53:38.539589
# Unit test for constructor of class Map
def test_Map():
    assert Map({'a': Sum(2), 'b': Sum(0), 'c': Sum(1)}) == Map({'a': Sum(2), 'b': Sum(0), 'c': Sum(1)})


# Generated at 2022-06-14 03:53:42.587702
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(1).concat(Max(2)) == Max(2)
    assert Max(-1).concat(Max(-2)) == Max(-1)
    assert Max(-1).concat(Max(2)) == Max(2)
    assert Max(-1).concat(Max(-3)).concat(Max(-2)) == Max(-1)


# Generated at 2022-06-14 03:53:44.309823
# Unit test for method __str__ of class Last
def test_Last___str__():
    assert str(Last(1)) == 'Last[value=1]'



# Generated at 2022-06-14 03:53:47.524558
# Unit test for method concat of class All
def test_All_concat():
    assert All(True).concat(All(True)).value == All(True).value
    assert All(False).concat(All(True)).value == All(False).value

