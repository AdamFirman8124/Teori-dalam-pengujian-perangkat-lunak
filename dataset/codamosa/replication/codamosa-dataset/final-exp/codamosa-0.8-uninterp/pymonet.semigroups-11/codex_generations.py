

# Generated at 2022-06-14 03:44:37.205678
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(1).concat(Max(2)) == Max(2)
    assert Max(3).concat(Max(2)) == Max(3)
    assert Max(2).concat(Max(2)) == Max(2)


# Generated at 2022-06-14 03:44:40.971758
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(1).concat(Max(2)) == Max(2)
    assert Max(3).concat(Max(1)) == Max(3)
    assert Max(1).concat(Max(4)) == Max(4)
    assert Max(2).concat(Max(2)) == Max(2)

# Generated at 2022-06-14 03:44:44.394289
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(1).concat(Max(2)).value == 2, 'Should be 2'
    assert Max(1).concat(Max(-2)).value == 1, 'Should be 1'


# Generated at 2022-06-14 03:44:48.581236
# Unit test for method concat of class Max
def test_Max_concat():
    """
    Check Max.concat method
    """
    assert Max(4).concat(Max(5)) == Max(5)
    assert Max(5).concat(Max(4)) == Max(5)
    assert Max(4).concat(Max(4)) == Max(4)



# Generated at 2022-06-14 03:44:51.377967
# Unit test for method concat of class Max
def test_Max_concat():
    MAX_INT = Max(1000)
    assert_that(MAX_INT.concat(Max(1001)).value, equal_to(1001))

# Generated at 2022-06-14 03:44:54.124271
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(1).concat(Max(3)) == Max(3)

# Generated at 2022-06-14 03:44:56.708867
# Unit test for method concat of class Max
def test_Max_concat():  # pragma: no cover
    assert Max(23).concat(Max(24)) == Max(24)
    assert Max(23).concat(Max(22)) == Max(23)
    assert Max(24).concat(Max(24)) == Max(24)


# Generated at 2022-06-14 03:45:00.554185
# Unit test for method concat of class Max
def test_Max_concat():  # pragma: no cover
    assert Max(1).concat(Max(2)) == Max(2)



# Generated at 2022-06-14 03:45:06.115240
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(5).concat(Max(6)).value == 6
    assert Max(-1.1).concat(Max(-0.9)).value == -0.9
    assert Max(-1.1).concat(Max(-0.9)).value == -0.9



# Generated at 2022-06-14 03:45:13.749489
# Unit test for method concat of class Max
def test_Max_concat():
    """
    In mathematics, a semigroup is an algebraic structure
    consisting of a set together with an associative binary operation.
    A semigroup generalizes a monoid in that there might not exist an identity element.
    It also (originally) generalized a group (a monoid with all inverses)
    to a type where every element did not have to have an inverse, this the name semigroup.
    """

    assert Max(22).concat(Max(23)) == Max(23)

    assert Max(22).concat(Max(20)) == Max(22)

    assert Max(0).concat(Max(-22)) == Max(0)



# Generated at 2022-06-14 03:45:20.174180
# Unit test for method concat of class Min
def test_Min_concat(): # pragma: no cover
    min_value = 5
    value_to_concat = 7
    min_value_to_concat = 4
    min_value_to_concat_2 = 5
    min_value_expected = min_value
    min_value_to_concat_expected = min_value_to_concat
    min_value_to_concat_2_expected = min_value_to_concat_2
    min_value = Min(min_value)
    min_value_to_concat = Min(min_value_to_concat)
    min_value_to_concat_2 = Min(min_value_to_concat_2)
    assert min_value.concat(Min(value_to_concat)).value == min_value_expected
    assert min_value_to

# Generated at 2022-06-14 03:45:24.495792
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(1).concat(Min(2)).value == 1
    assert Min(2).concat(Min(1)).value == 1
    assert Min(1).concat(Min(-2)).value == -2


# Generated at 2022-06-14 03:45:26.703303
# Unit test for method concat of class Min
def test_Min_concat():
    # Arrange & Act
    result = Min(1).concat(Min(2))

    # Assert
    assert result == Min(1)


# Generated at 2022-06-14 03:45:28.976438
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(5).concat(Min(9)) == Min(5)
    assert Min(9).concat(Min(5)) == Min(5)

# Generated at 2022-06-14 03:45:35.759454
# Unit test for method concat of class Min
def test_Min_concat():
    s = Min(1)
    s1 = Min(2)
    assert s.concat(s1) == Min(1)
    s2 = Min(0)
    assert s.concat(s2) == Min(0)
    s3 = Min(1)
    assert s.concat(s3) == Min(1)



# Generated at 2022-06-14 03:45:41.636292
# Unit test for method concat of class Min
def test_Min_concat():
    """
    Test of concat method of Min Semigroup
    """
    assert Min(5).concat(Min(2)) == Min(2)
    assert Min(2).concat(Min(5)) == Min(2)
    assert Min(5).concat(Min(5)) == Min(5)


# Generated at 2022-06-14 03:45:48.334897
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(3).concat(Min(4)) == Min(3)
    assert Min(4).concat(Min(3)) == Min(3)
    assert Min(3).concat(Min(3)) == Min(3)
    assert Min(-3).concat(Min(-4)) == Min(-4)
    assert Min(-4).concat(Min(-3)) == Min(-3)
    assert Min(-3).concat(Min(-3)) == Min(-3)


# Generated at 2022-06-14 03:45:50.362503
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(1) + Min(2) == Min(1)
    assert Min(2) + Min(1) == Min(1)


# Generated at 2022-06-14 03:45:56.545337
# Unit test for method concat of class Min
def test_Min_concat():
    min_1 = Min(5)
    min_2 = Min(3)
    min_3 = Min(10)
    assert min_1.concat(min_2).value == 3
    assert min_2.concat(min_3).value == 3
    assert min_3.concat(min_1).value == 3

# Generated at 2022-06-14 03:45:59.632583
# Unit test for method concat of class Min
def test_Min_concat():
    min1 = Min(2)
    min2 = Min(3)
    print(min1.concat(min2))
    assert min1.concat(min2) == Min(2)


# Generated at 2022-06-14 03:46:03.960701
# Unit test for constructor of class Last
def test_Last():
    last = Last(10)
    assert last.value == 10



# Generated at 2022-06-14 03:46:05.770279
# Unit test for method __str__ of class Max
def test_Max___str__():
    max = Max(10)
    assert "Max[value=10]" == str(max)



# Generated at 2022-06-14 03:46:07.014242
# Unit test for constructor of class Sum
def test_Sum():
    assert Sum(5) == Sum(5)
    assert Sum(5).value == 5


# Generated at 2022-06-14 03:46:08.344854
# Unit test for constructor of class First
def test_First():
    assert First(2) == First(2)



# Generated at 2022-06-14 03:46:13.584876
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(2).concat(Min(3)).fold(lambda x: x) == 2
    assert Min(3).concat(Min(3)).fold(lambda x: x) == 3
    assert Min(3).concat(Min(2)).fold(lambda x: x) == 2

# Generated at 2022-06-14 03:46:14.915070
# Unit test for method __str__ of class Last
def test_Last___str__():
    assert str(Last(1)) == 'Last[value=1]'



# Generated at 2022-06-14 03:46:19.587851
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    assert Sum(0) == Sum(0)
    assert All(True) == All(True)
    assert One(False) == One(False)
    assert First(1) == First(1)
    assert Last(1) == Last(1)
    assert Max(1) == Max(1)
    assert Min(1) == Min(1)
    assert Sum(0) != All(True)
    assert Sum(0) != One(False)
    assert Sum(0) != First(1)
    assert Sum(0) != Last(1)
    assert Sum(0) != Max(1)
    assert Sum(0) != Min(1)


# Generated at 2022-06-14 03:46:25.617968
# Unit test for method __str__ of class All
def test_All___str__():
    assert str(All(True)) == "All[value=True]"
    assert str(All(False)) == "All[value=False]"
    assert str(All(1)) == "All[value=True]"
    assert str(All(0)) == "All[value=False]"
    assert str(All("hello")) == "All[value=True]"
    assert str(All("")) == "All[value=False]"
    assert str(All(None)) == "All[value=False]"
    assert str(All([])) == "All[value=False]"
    assert str(All([0])) == "All[value=True]"
    assert str(All([1])) == "All[value=True]"


# Generated at 2022-06-14 03:46:26.476850
# Unit test for method __str__ of class All
def test_All___str__():
    assert str(All(True)) == 'All[value=True]'



# Generated at 2022-06-14 03:46:28.480538
# Unit test for constructor of class All
def test_All():
    assert All(False).value == False
    assert All(True).value == True


# Generated at 2022-06-14 03:46:31.696152
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    assert str(Sum(1)) == 'Sum[value=1]'



# Generated at 2022-06-14 03:46:33.453006
# Unit test for constructor of class First
def test_First():
    first_value = First(1)
    assert first_value.value == 1



# Generated at 2022-06-14 03:46:38.213220
# Unit test for method concat of class Map
def test_Map_concat():
    """
    :returns: True if test passed else return False
    :rtype: bool
    """
    map_empty_a = Map({})
    map_empty_b = Map({})
    map_full_a = Map({
        1: Sum(1),
        2: Sum(2),
        3: Sum(3),
        4: Sum(4),
        5: Sum(5),
    })
    map_full_b = Map({
        1: Sum(6),
        2: Sum(7),
        3: Sum(8),
        4: Sum(9),
        5: Sum(10),
    })
    map_partial_a = Map({
        1: Sum(1),
        2: Sum(2),
        3: Sum(3),
        4: Sum(4),
    })


# Generated at 2022-06-14 03:46:40.579758
# Unit test for method __str__ of class Map
def test_Map___str__():
    value = Map({'key': Sum(10)})
    assert str(value) == "Map[value={'key': Sum[value=10]}]"



# Generated at 2022-06-14 03:46:41.994548
# Unit test for method __str__ of class Min
def test_Min___str__():
    assert str(Min(1)) == "Min[value=1]"



# Generated at 2022-06-14 03:46:46.161877
# Unit test for method __str__ of class Map
def test_Map___str__():
    actual = Map({'a': Sum(1)}).__str__()
    expected = "Map[value={'a': Sum[value=1]}]"
    assert actual == expected


# Generated at 2022-06-14 03:46:56.561892
# Unit test for method concat of class All
def test_All_concat():
    a = All(True)
    assert a.concat(All(True)) == All(True)
    assert a.concat(All(False)) == All(False)
    assert a.concat(All(1)) == All(True)
    assert a.concat(All(0)) == All(False)

    a = All(False)
    assert a.concat(All(True)) == All(False)
    assert a.concat(All(False)) == All(False)
    assert a.concat(All(1)) == All(False)
    assert a.concat(All(0)) == All(False)

    a = All(1)
    assert a.concat(All(True)) == All(True)
    assert a.concat(All(False)) == All(False)
    assert a.con

# Generated at 2022-06-14 03:47:03.981406
# Unit test for method concat of class One
def test_One_concat():
    assert One(True).concat(One(False)) == One(True)
    assert One(False).concat(One(False)) == One(False)
    assert One(None).concat(One(0)) == One(None)
    assert One(None).concat(One('')) == One(None)
    assert One(None).concat(One([])) == One(None)
    assert One(None).concat(One({})) == One(None)
    assert One(None).concat(One(())) == One(None)

# Unit tests for method concat of class First

# Generated at 2022-06-14 03:47:06.052789
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    assert Sum(1) == Sum(1)



# Generated at 2022-06-14 03:47:09.547464
# Unit test for constructor of class Map
def test_Map():
    a = Map({1: Sum(0), 2: Sum(0), 3: Sum(0)})
    assert a.value == {1: Sum(0), 2: Sum(0), 3: Sum(0)}



# Generated at 2022-06-14 03:47:13.739733
# Unit test for constructor of class Map
def test_Map():
    assert Map({'a': Sum(1), 'b': Sum(1)}).fold(lambda d: d) == {'a': Sum(1), 'b': Sum(1)}



# Generated at 2022-06-14 03:47:15.270034
# Unit test for method __str__ of class Min
def test_Min___str__():
    assert str(Min(1)) == "Min[value=1]"


# Generated at 2022-06-14 03:47:16.456396
# Unit test for method concat of class Last
def test_Last_concat():
    assert Last(10).concat(Last(20)).value == 20



# Generated at 2022-06-14 03:47:17.530278
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    assert 'Sum[value=1]' == str(Sum(1))


# Generated at 2022-06-14 03:47:21.335904
# Unit test for constructor of class Last
def test_Last():
    assert Last(1).value == 1
    assert Last(2).value == 2
    assert Last(3).value == 3
    assert Last(1).value != 2
    assert Last(1).value != 3
    assert Last(2).value != 3



# Generated at 2022-06-14 03:47:24.356620
# Unit test for method __str__ of class Map
def test_Map___str__():
    assert str(Map({"a": 1, "b": "2", "c": 3.0})) == "Map[value={'a': 1, 'b': '2', 'c': 3.0}]"


# Generated at 2022-06-14 03:47:26.445262
# Unit test for constructor of class Last
def test_Last():
    with pytest.raises(TypeError):
        Last()
    assert Last(1) is not None


# Generated at 2022-06-14 03:47:30.059676
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    assert str(Sum(1)) == 'Sum[value=1]'
    assert str(Sum(2)) == 'Sum[value=2]'



# Generated at 2022-06-14 03:47:32.257551
# Unit test for method __str__ of class One
def test_One___str__():
    assert str(One(False)) == 'One[value=False]'
    assert str(One(True)) == 'One[value=True]'



# Generated at 2022-06-14 03:47:44.193788
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(3).concat(Max(5)) == Max(5)
    assert Max(5).concat(Max(3)) == Max(5)
    assert Max(3).concat(Max(-5)) == Max(3)
    assert Max(-5).concat(Max(3)) == Max(3)
    assert Max(-3).concat(Max(5)) == Max(5)
    assert Max(5).concat(Max(-3)) == Max(5)
    assert Max(-3).concat(Max(-5)) == Max(-3)
    assert Max(-5).concat(Max(-3)) == Max(-3)
    assert Max(0).concat(Max(5)) == Max(5)
    assert Max(5).concat(Max(0)) == Max(5)

# Generated at 2022-06-14 03:47:48.298584
# Unit test for constructor of class One
def test_One():
    assert One(True) == One(True)
    assert One(False) == One(False)


# Generated at 2022-06-14 03:47:50.185488
# Unit test for method __str__ of class First
def test_First___str__():
    first = First(10)
    assert str(first) == 'Fist[value=10]'



# Generated at 2022-06-14 03:47:56.590422
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    sum_ = Sum(1)
    assert sum_ == Sum(1)
    assert sum_ != Sum(2)
    assert sum_ != First(1)
    assert sum_ != '1'
    assert sum_ != 1

    all_ = All(True)
    assert all_ == All(True)
    assert all_ != All(False)
    assert all_ != First(True)
    assert all_ != 1
    assert all_ != 'True'

    first = First(True)
    assert first == First(True)
    assert first != First(False)
    assert first != All(True)
    assert first != 1
    assert first != 'True'

    last = Last(True)
    assert last == Last(True)
    assert last != Last(False)
    assert last != All(True)
    assert last != 1

# Generated at 2022-06-14 03:48:00.477479
# Unit test for method concat of class Last
def test_Last_concat():
    """
    Test method concat of class Last
    """
    assert Last(1).concat(Last(2)).value == 2
    assert Last(2).concat(Last(1)).value == 1
    assert Last(0).concat(Last(0)).value == 0


# Generated at 2022-06-14 03:48:03.011369
# Unit test for method __str__ of class Sum
def test_Sum___str__():  # pragma: no cover
    assert str(Sum(5)) == 'Sum[value=5]'



# Generated at 2022-06-14 03:48:11.549972
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    assert Sum(1).fold(lambda x: x + 2) == 3
    assert All(True).fold(lambda x: x) == True
    assert One(False).fold(lambda x: x) == False
    assert First(1).fold(lambda x: 10) == 1
    assert Last(1).fold(lambda x: 10) == 10
    assert Map({'key': Sum(4)}).fold(lambda x: x['key'].value) == 4
    assert Max(4).fold(lambda x: x) == 4
    assert Min(4).fold(lambda x: x) == 4

# Generated at 2022-06-14 03:48:16.143774
# Unit test for method __str__ of class Map
def test_Map___str__():
    assert str(Map({'foo': Sum(1), 'bar': Sum(6) , 'baz': Sum(8) })) == 'Map[value={\'foo\': Sum[value=1], \'bar\': Sum[value=6], \'baz\': Sum[value=8]}]'


# Generated at 2022-06-14 03:48:18.372969
# Unit test for method __str__ of class All
def test_All___str__():
    assert str(All(True)) == 'All[value=True]'
    assert str(All(False)) == 'All[value=False]'


# Generated at 2022-06-14 03:48:23.666844
# Unit test for constructor of class Sum
def test_Sum():
    assert Sum(5) == Sum(5)
    assert Sum(5).neutral() == Sum(5)
    assert Sum(5).fold(lambda x: x) == 5
    assert Sum(5).concat(Sum(5)) == Sum(10)



# Generated at 2022-06-14 03:48:31.239664
# Unit test for method __str__ of class Last
def test_Last___str__():
    assert str(Last(1)) == "Last[value=1]"
    assert str(Last(True)) == "Last[value=True]"
    assert str(Last(1.1)) == "Last[value=1.1]"
    assert str(Last(1+1j)) == "Last[value=(1+1j)]"
    assert str(Last("aaa")) == "Last[value=aaa]"
    assert str(Last((1, 2))) == "Last[value=(1, 2)]"
    assert str(Last([1, 2])) == "Last[value=[1, 2]]"


# Generated at 2022-06-14 03:48:40.784721
# Unit test for method __eq__ of class Semigroup
def test_Semigroup___eq__():
    """
    Check the method __eq__ of the Semigroup class,
    """
    assert (Sum(1) == Sum(1)) == True
    assert (Sum(1) == Sum(0)) == False
    assert (All(True) == All(True)) == True
    assert (All(False) == All(True)) == False
    assert (First(1) == First(1)) == True
    assert (First(0) == First(1)) == True
    assert (Last(1) == Last(1)) == True
    assert (Last(0) == Last(1)) == True
    assert (Map({'a': Sum(1)})) == Map({'a': Sum(1)})
    assert (Map({'a': Sum(1)})) != Map({'a': Sum(0)})

# Generated at 2022-06-14 03:48:42.607722
# Unit test for method concat of class Sum
def test_Sum_concat():
    assert Sum(1).concat(Sum(2)) == Sum(3)



# Generated at 2022-06-14 03:48:45.436646
# Unit test for method concat of class Min
def test_Min_concat():
    Min_1 = Min(5)
    Min_2 = Min(10)
    result = Min_1.concat(Min_2)
    assert(result == Min(5))


# Generated at 2022-06-14 03:48:51.655189
# Unit test for method concat of class One
def test_One_concat():
    assert One(True).concat(One(True)).value == One(True).value
    assert One(True).concat(One(False)).value == One(True).value
    assert One(False).concat(One(True)).value == One(True).value
    assert One(False).concat(One(False)).value == One(False).value


# Generated at 2022-06-14 03:48:55.374373
# Unit test for method concat of class Min
def test_Min_concat():
    semigroup_before_concat = Min(1)
    semigroup_after_concat = semigroup_before_concat.concat(Min(2))
    print(semigroup_after_concat.value)
    # =>
    # 1


# Generated at 2022-06-14 03:48:56.325843
# Unit test for constructor of class Max
def test_Max():
    assert Max(1).value == 1


# Generated at 2022-06-14 03:48:59.562923
# Unit test for method __str__ of class All
def test_All___str__():
    assert str(All(True)) == 'All[value=True]'
    assert str(All(1)) == 'All[value=True]'

# Generated at 2022-06-14 03:49:03.159424
# Unit test for method __str__ of class All
def test_All___str__():
    """
    Unit test for method __str__ of class All
    """
    assert str(All(True)) == "All[value=True]"
    assert str(All(False)) == "All[value=False]"



# Generated at 2022-06-14 03:49:04.684944
# Unit test for method concat of class Sum
def test_Sum_concat():  # pragma: no cover
    assert Sum(1).concat(Sum(2)).value == 3



# Generated at 2022-06-14 03:49:08.924108
# Unit test for method concat of class All
def test_All_concat():
    a1 = All(True)
    a2 = All(False)
    a3 = All(False)

    assert a1.concat(a2) == All(False)
    assert a2.concat(a3) == All(False)
    assert a1.concat(a1).concat(a2) == All(False)



# Generated at 2022-06-14 03:49:18.109491
# Unit test for constructor of class Max
def test_Max():
    semigroup = Max(10)
    assert isinstance(semigroup, Max)  # check is instance of Max

    assert semigroup.value == 10        # check the value of Max is 10


# Generated at 2022-06-14 03:49:19.797399
# Unit test for constructor of class Min
def test_Min():
    assert Min(-1) == Min(-1)


# Generated at 2022-06-14 03:49:20.806352
# Unit test for method __str__ of class Min
def test_Min___str__():
    assert Min(1).__str__()=="Min[value=1]"


# Generated at 2022-06-14 03:49:23.646577
# Unit test for constructor of class Min
def test_Min():
    min_instance = Min(3)
    assert min_instance.value == 3
    assert min_instance.neutral_element == float("inf")

# Generated at 2022-06-14 03:49:26.051630
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(1).concat(Max(2)) == Max(2)


# Generated at 2022-06-14 03:49:28.585672
# Unit test for method concat of class First
def test_First_concat():  # pragma: no cover
    assert (First(1) >> Last(2)).concat(First(3)).value == 1



# Generated at 2022-06-14 03:49:31.608528
# Unit test for method __str__ of class First
def test_First___str__():                                          # pragma: no cover
    first = First('bem')
    assert (first.__str__() == 'Fist[value=bem]')


# Generated at 2022-06-14 03:49:32.659317
# Unit test for constructor of class Sum
def test_Sum():
    sum = Sum(1)
    assert sum.value == 1



# Generated at 2022-06-14 03:49:34.068901
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    assert str(Sum(1)) == 'Sum[value=1]'


# Generated at 2022-06-14 03:49:39.578763
# Unit test for method concat of class Map
def test_Map_concat():
    a = Map({'a': Sum(1), 'b': Sum(2)})
    b = Map({'a': Sum(3), 'b': Sum(4)})
    assert a.concat(b) == Map({'a': Sum(4), 'b': Sum(6)})


# Generated at 2022-06-14 03:49:55.491943
# Unit test for method concat of class Min
def test_Min_concat():
    result = Min(1).concat(Min(0))
    expected = Min(0)
    assert result == expected


# Generated at 2022-06-14 03:49:57.146923
# Unit test for method __str__ of class Min
def test_Min___str__():
    assert str(Min(123)) == 'Min[value=123]'


# Generated at 2022-06-14 03:49:58.933088
# Unit test for method concat of class Last
def test_Last_concat():
    assert Last(2).concat(Last(1)) == Last(1)


# Generated at 2022-06-14 03:49:59.854609
# Unit test for method concat of class Last
def test_Last_concat():
    assert Last(2).concat(Last(3)) == Last(3)



# Generated at 2022-06-14 03:50:02.193923
# Unit test for constructor of class Last
def test_Last():
    temp = Last(4)
    assert temp.value == 4


# Generated at 2022-06-14 03:50:04.751173
# Unit test for method __str__ of class All
def test_All___str__():

    assert str(All(True)) == 'All[value=True]'
    assert str(All(False)) == 'All[value=False]'



# Generated at 2022-06-14 03:50:10.424776
# Unit test for method concat of class First
def test_First_concat():
    first1 = First("value1")
    first2 = First("value2")
    assert first1.concat(first2) == First("value1"), "With concat method of class First expected: First[value=value1], actual: {}".format(first1.concat(first2))

# Run unit tests
test_First_concat()

# Generated at 2022-06-14 03:50:14.926176
# Unit test for method concat of class Map
def test_Map_concat():
    map1 = Map({'a': All(True), 'b': Sum(2), 'c': Sum(3)})
    map2 = Map({'a': All(False), 'b': Sum(-1)})
    map3 = Map({'a': All.neutral(), 'b': Sum.neutral(), 'c': Sum.neutral()})
    assert map1.concat(map2) == Map({'a': All(False), 'b': Sum(1), 'c': Sum(3)}), 'Wrong result of concat'
    assert map2.concat(map1) == Map({'a': All(False), 'b': Sum(1), 'c': Sum(3)}), 'Wrong result of concat'

# Generated at 2022-06-14 03:50:18.463171
# Unit test for method __str__ of class All
def test_All___str__():  # pragma: no cover
    assert str(All(True)) == 'All[value=True]'
    assert str(All(False)) == 'All[value=False]'


# Generated at 2022-06-14 03:50:20.725868
# Unit test for constructor of class Max
def test_Max():
    """
    Unit test for constructor of class Max.
    """
    assert Max(3).value == 3



# Generated at 2022-06-14 03:50:50.115083
# Unit test for method __str__ of class Map
def test_Map___str__():
    assert Map({1:Sum(1)}).__str__() == 'Map[value={1: Sum[value=1]}]'


# Generated at 2022-06-14 03:50:52.996664
# Unit test for constructor of class Sum
def test_Sum():
    assert Sum(1) == Sum(1)
    assert Sum(1) != Sum(2)



# Generated at 2022-06-14 03:51:00.177277
# Unit test for constructor of class All
def test_All():
    result = All('hello')
    assert result.value is True
    result = All([1, 2, 3])
    assert result.value is True
    result = All(5)
    assert result.value is True
    result = All(None)
    assert result.value is False
    result = All(0)
    assert result.value is False
    result = All(-5)
    assert result.value is True
    result = All('')
    assert result.value is False
    result = All([])
    assert result.value is False



# Generated at 2022-06-14 03:51:01.796366
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():  # pragma: no cover
    assert Semigroup(1).fold(lambda x: x + 1) == 2



# Generated at 2022-06-14 03:51:03.317605
# Unit test for constructor of class Last
def test_Last():
    last_val = Last(10)
    assert last_val.value == 10


# Generated at 2022-06-14 03:51:04.688938
# Unit test for method __str__ of class Max
def test_Max___str__():
    max_class = Max(-5)
    assert max_class.__str__() == 'Max[value=-5]'

# Generated at 2022-06-14 03:51:07.549974
# Unit test for method __str__ of class Max
def test_Max___str__():
    from hamcrest import assert_that, equal_to
    assert_that(str(Max(1)), equal_to('Max[value=1]'))



# Generated at 2022-06-14 03:51:09.022568
# Unit test for constructor of class Min
def test_Min():
    assert Min(1).value == 1
    assert Min(2).value == 2


# Generated at 2022-06-14 03:51:10.567601
# Unit test for constructor of class Sum
def test_Sum():
    number = 1
    assert Sum(number).value == number



# Generated at 2022-06-14 03:51:16.013818
# Unit test for method __str__ of class Map
def test_Map___str__():
    assert str(Map({})) == 'Map[value={}]'
    assert str(Map({'t': First('t')})) == 'Map[value={\'t\': Fist[value=t]}]'



# Generated at 2022-06-14 03:52:14.036625
# Unit test for method __str__ of class All
def test_All___str__():
    """
    Test for method __str__ of class All
    """
    obj = All(True)
    assert str(obj) == "All[value=True]"


# Generated at 2022-06-14 03:52:15.718198
# Unit test for method __str__ of class One
def test_One___str__():
    assert str(One(True)) == 'One[value=True]'


# Generated at 2022-06-14 03:52:17.720541
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(1).concat(Max(2)).value == 2

# Generated at 2022-06-14 03:52:20.428684
# Unit test for constructor of class Min
def test_Min():
    minObj = Min(10)
    assert minObj.value == 10

if __name__ == '__main__':
    test_Min()

# Generated at 2022-06-14 03:52:22.182527
# Unit test for constructor of class First
def test_First():
    assert First(1) == First(1)


# Generated at 2022-06-14 03:52:30.072972
# Unit test for constructor of class Semigroup
def test_Semigroup():
    assert Sum(5) == Sum(5)
    assert All(True) == All(True)
    assert All(False) == All(False)
    assert One(True) == One(True)
    assert One(False) == One(False)
    assert First([1,2,3]) == First([1,2,3])
    assert Last([1,2,3]) == Last([1,2,3])
    assert Map({'a': Sum(1), 'b': Sum(1)}) == Map({'a': Sum(1), 'b': Sum(1)})
    assert Max(3) == Max(3)
    assert Min(3) == Min(3)


# Generated at 2022-06-14 03:52:31.443842
# Unit test for method __str__ of class First
def test_First___str__():
    assert str(First(5)) == 'Fist[value=5]'


# Generated at 2022-06-14 03:52:33.336709
# Unit test for constructor of class One
def test_One():
    assert One(True) == One(True)
    assert One(False) == One(False)



# Generated at 2022-06-14 03:52:35.207056
# Unit test for method __str__ of class Max
def test_Max___str__():
    """
    __str__ method of class Max test
    """
    assert str(Max(1)) == 'Max[value=1]'


# Generated at 2022-06-14 03:52:38.464916
# Unit test for method concat of class First
def test_First_concat():
    assert First(1).concat(First(2)).value == 1
