

# Generated at 2022-06-14 03:44:38.222423
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(10).concat(Max(9)) == Max(10)
    assert Max(3).concat(Max(5)) == Max(5)
    assert Max(4.5).concat(Max(4.4)) == Max(4.5)
    assert Max(4).concat(Max(4)) == Max(4)



# Generated at 2022-06-14 03:44:40.516463
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(1).concat(Max(3)) == Max(3)

# Generated at 2022-06-14 03:44:54.097219
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(5).concat(Max(9)) == Max(9)
    assert Max(-3).concat(Max(-2)) == Max(-2)
    assert Max(-3).concat(Max(8)) == Max(8)
    assert Max(2).concat(Max(2)) == Max(2)
    assert Max(15).concat(Max(5)) == Max(15)
    assert Max(5).concat(Max(15)) == Max(15)
    assert Max(2).concat(Max(15)) == Max(15)
    assert Max(15).concat(Max(2)) == Max(15)
    assert Max(15).concat(Max(15)) == Max(15)
    assert Max(0).concat(Max(0)) == Max(0)


# Generated at 2022-06-14 03:44:55.704516
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(1).concat(Max(2)) == Max(2)



# Generated at 2022-06-14 03:44:58.174698
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(1).concat(Max(2)) == Max(2)


# Generated at 2022-06-14 03:45:04.049883
# Unit test for method concat of class Max
def test_Max_concat():  # pragma: no cover
    max_a = Max(12)
    max_b = Max(429)
    result = max_a.concat(max_a).concat(max_b).concat(max_b)
    assert result.value == 429



# Generated at 2022-06-14 03:45:07.100458
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(2).concat(Max(4)) == Max(4)
    assert Max(2).concat(Max(3)) == Max(3)



# Generated at 2022-06-14 03:45:11.238190
# Unit test for method concat of class Max
def test_Max_concat():
    max_value = Max(2)
    assert max_value.concat(Max(1)) == Max(2)


# Generated at 2022-06-14 03:45:12.820058
# Unit test for method concat of class Max
def test_Max_concat():
    m = Max(2)
    n = Max(3)
    assert m.concat(n) == Max(3)


# Generated at 2022-06-14 03:45:22.346788
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max.neutral() == Max(-float("inf"))
    assert Max(1).concat(Max(2)) == Max(2)
    assert Max(2).concat(Max(1)) == Max(2)
    assert Max(1).concat(Max(1)) == Max(1)
    assert Max(None).concat(Max(1)) == Max(1)
    assert Max(None).concat(Max(None)) == Max(None)
    assert Max(None).concat(Max(0)) == Max(0)

# Generated at 2022-06-14 03:45:27.173718
# Unit test for constructor of class One
def test_One():
    """
    Test for constructor of class One
    """
    one = One(0)
    assert one.value == 0


# Generated at 2022-06-14 03:45:29.395346
# Unit test for constructor of class One
def test_One():
    assert One(False) == One(False)
    assert One(True) == One(True)
    assert One(True) != One(False)

# Generated at 2022-06-14 03:45:32.920355
# Unit test for method __str__ of class One
def test_One___str__():
    val = One(True)
    assert str(val) == 'One[value={}]'.format(val.value)


# Generated at 2022-06-14 03:45:34.751161
# Unit test for method __str__ of class One
def test_One___str__():
    assert str(One(True)) == 'One[value=True]'
    assert str(One(False)) == 'One[value=False]'


# Generated at 2022-06-14 03:45:36.271193
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(1).concat(Max(0)) == Max(1)



# Generated at 2022-06-14 03:45:38.020943
# Unit test for constructor of class Sum
def test_Sum():
    assert Sum(1) == Sum(1)


# Generated at 2022-06-14 03:45:47.052854
# Unit test for constructor of class Semigroup
def test_Semigroup():
    assert Map({'a': Sum(1), 'b': Sum(2)}) == Map({'a': Sum(1), 'b': Sum(2)})
    assert Semigroup(1) == Semigroup(1)
    assert One(1) == One(1)
    assert All(1) == All(1)
    assert First(1) == First(1)
    assert Last(1) == Last(1)
    assert Max(1) == Max(1)
    assert Min(1) == Min(1)


# Generated at 2022-06-14 03:45:49.919697
# Unit test for constructor of class First
def test_First():
    # Given
    input_value = 1
    expected_result = First(input_value)
    # When
    result = First(input_value)
    # Then
    assert result == expected_result


# Generated at 2022-06-14 03:45:56.275186
# Unit test for method concat of class All
def test_All_concat():
    assert All(True).concat(All(True)) == All(True)
    assert All(True).concat(All(False)) == All(False)
    assert All(False).concat(All(True)) == All(False)
    assert All(False).concat(All(False)) == All(False)


# Generated at 2022-06-14 03:45:57.121954
# Unit test for constructor of class Last
def test_Last():
    assert Last(2) == Last(2)


# Generated at 2022-06-14 03:46:03.552028
# Unit test for method __str__ of class Map
def test_Map___str__():
    assert 'Map[value={}]' == str(Map({}))
    assert 'Map[value={"key": "value"}]' == str(Map({"key": "value"}))


# Generated at 2022-06-14 03:46:04.311035
# Unit test for method concat of class One
def test_One_concat():
    pass


# Generated at 2022-06-14 03:46:06.730263
# Unit test for constructor of class Semigroup
def test_Semigroup():  # pragma: no cover
    # arrange
    expected_value = True
    # act
    semigroup = All(expected_value)
    # assert
    assert semigroup.value == expected_value



# Generated at 2022-06-14 03:46:08.441973
# Unit test for method concat of class Last
def test_Last_concat():
    assert Last(0).concat(Last(1)) == Last(1)
    assert Last(0).concat(Last(1)) != Last(0)



# Generated at 2022-06-14 03:46:11.132927
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(6).concat(Min(1)) == Min(1)



# Generated at 2022-06-14 03:46:13.848235
# Unit test for method __str__ of class All
def test_All___str__():
    assert str(All(True)) == 'All[value=True]'
    assert str(All(False)) == 'All[value=False]'


# Generated at 2022-06-14 03:46:16.516286
# Unit test for method concat of class One
def test_One_concat():
    assert One(True).concat(One(False)) == One(True)
    assert One(False).concat(One(False)) == One(False)
    assert One(True).concat(One(True)) == One(True)
    assert One(False).concat(One(True)) == One(True)


# Generated at 2022-06-14 03:46:17.453436
# Unit test for constructor of class Last
def test_Last():
    assert Last(1).value == 1



# Generated at 2022-06-14 03:46:20.919046
# Unit test for constructor of class One
def test_One():  # pragma: no cover
    assert str(One(True)) == 'One[value=True]'
    assert str(One(False)) == 'One[value=False]'



# Generated at 2022-06-14 03:46:25.323725
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(5).concat(Max(4)) == Max(5)
    assert Max(4).concat(Max(5)) == Max(5)
    assert Max(5).concat(Max(5)) == Max(5)


# Generated at 2022-06-14 03:46:35.175654
# Unit test for constructor of class Last
def test_Last():  # pragma: no cover
    a = Last(1)
    b = Last(2)
    c = First(3)
    d = First(4)
    assert a == Last(1)
    assert b == Last(2)
    assert a.concat(b).value == 2
    assert Last(2).concat(a).value == 2
    assert a.concat(c).value == 2
    assert c.concat(a).value == 1
    assert First(1).concat(Last(2)).value == 2
    assert Last(2).concat(First(1)).value == 2



# Generated at 2022-06-14 03:46:36.930189
# Unit test for constructor of class Sum
def test_Sum():
    assert Sum(1) == Sum(1)



# Generated at 2022-06-14 03:46:38.212406
# Unit test for constructor of class Min
def test_Min():
    assert Min(1)==Min(1)



# Generated at 2022-06-14 03:46:41.465519
# Unit test for method concat of class Max
def test_Max_concat():  # pragma: no cover
    assert Max(1).concat(Max(2)).value == 2
    assert Max(2).concat(Max(1)).value == 2
    assert Max(1).concat(Max(1)).value == 1


# Generated at 2022-06-14 03:46:43.346062
# Unit test for method __str__ of class Sum
def test_Sum___str__():
    assert str(Sum(1)) == 'Sum[value=1]'


# Generated at 2022-06-14 03:46:46.434206
# Unit test for method __str__ of class All
def test_All___str__():
    assert str(All(True)) == 'All[value=True]'
    assert str(All(False)) == 'All[value=False]'


# Generated at 2022-06-14 03:46:49.230122
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    test = Sum(2)
    foo = test.fold(lambda i: i * 2)
    assert foo == 4, "method fold of class Semigroup should return 4"


# Generated at 2022-06-14 03:46:57.862027
# Unit test for method concat of class Sum
def test_Sum_concat():

    one = Sum(1)
    two = Sum(2)
    three = Sum(3)
    assert one.concat(two).concat(three) == Sum(6)  # 1 + 2 + 3

    seven = Sum(7)
    fourteen = Sum(14)
    twenty_one = Sum(21)


# Generated at 2022-06-14 03:47:01.720604
# Unit test for method concat of class All
def test_All_concat():
    t = All(True)
    f = All(False)
    assert t.concat(t) == t
    assert t.concat(f) == f
    assert f.concat(t) == f
    assert f.concat(f) == f


# Generated at 2022-06-14 03:47:03.870760
# Unit test for method concat of class Max
def test_Max_concat():
    left = Max(1)
    right = Max(4)
    result = left.concat(right)
    assert result.value == 4



# Generated at 2022-06-14 03:47:10.412133
# Unit test for method __str__ of class Min
def test_Min___str__():
    """
    Returns a string representation for a given object,
    if possible.
    """
    assert str(Min(1)) == 'Min[value=1]'

# Generated at 2022-06-14 03:47:11.989387
# Unit test for method __str__ of class Max
def test_Max___str__():  # pragma: no cover
    assert str(Max(4)) == 'Max[value=4]'



# Generated at 2022-06-14 03:47:22.266180
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    """
    For example we can use method fold for flatting structure
    >>> data = [1, 2, 3]
    >>> print(List(data).fold(Sum))
    Sum[value=6]
    """

    # check that method fold works correctly
    data = [1, 2, 3]
    assert List(data).fold(Sum) == Sum(6)
    assert Len(data).fold(Sum) == Sum(3)

    # check that method fold works correctly
    data = [True, True, True]
    assert List(data).fold(All) == All(True)
    assert Len(data).fold(All) == All(True)

    # check that method fold works correctly
    data = [True, True, True]
    assert List(data).fold(One) == One(True)
    assert Len(data).fold

# Generated at 2022-06-14 03:47:24.809876
# Unit test for constructor of class Last
def test_Last():

    value = 3

    result = Last(value)

    assert result.value == value


# Generated at 2022-06-14 03:47:26.826318
# Unit test for method concat of class Max
def test_Max_concat():
    assert Max(12).concat(Max(14)) == Max(14)


# Generated at 2022-06-14 03:47:31.179762
# Unit test for method concat of class One
def test_One_concat():
    # Arrange
    input_value_a = True
    input_value_b = False

    expected_output = False

    # Act
    output = One(input_value_a).concat(One(input_value_b))

    # Assert
    assert expected_output == output.value


# Generated at 2022-06-14 03:47:37.318425
# Unit test for method concat of class Map
def test_Map_concat():
    m1 = Map({1: Sum(1), 2: Sum(2)})
    m2 = Map({1: Sum(3), 2: Sum(4)})
    assert m1.concat(m2).value == {1: Sum(4), 2: Sum(6)}

test_Map_concat()

# Generated at 2022-06-14 03:47:40.983967
# Unit test for constructor of class Semigroup
def test_Semigroup():
    semigroup1 = Semigroup(1)
    semigroup2 = Semigroup(2)

    assert semigroup1 != semigroup2
    assert semigroup1 == Semigroup(1)
    assert semigroup1.value == 1



# Generated at 2022-06-14 03:47:44.628110
# Unit test for method __str__ of class Min
def test_Min___str__():

    # Test for method __str__ of class Min
    # Variant:
    # 1. type(self.value) == int

    x = Min(1)
    assert str(x) == "Min[value=1]"



# Generated at 2022-06-14 03:47:47.101530
# Unit test for constructor of class First
def test_First():
    # Just make sure it doesn't throw an exception
    First(123)


# Generated at 2022-06-14 03:48:01.448649
# Unit test for constructor of class Semigroup
def test_Semigroup():
    assert Sum(10) == Sum(10)
    assert All(True) == All(True)
    assert One(False) == One(False)
    assert First(1) == First(1)
    assert Last(1) == Last(1)
    assert Map({1: 1}) == Map({1: 1})
    assert Max(0) == Max(0)
    assert Min(0) == Min(0)



# Generated at 2022-06-14 03:48:03.413487
# Unit test for constructor of class One
def test_One():
    assert One(1).value == 1



# Generated at 2022-06-14 03:48:05.718391
# Unit test for constructor of class Map
def test_Map():
    map = Map({"test": 1})
    assert map.value["test"] == 1



# Generated at 2022-06-14 03:48:07.795172
# Unit test for method concat of class Sum
def test_Sum_concat():
    assert Sum(3).concat(Sum(4)) == Sum(7)



# Generated at 2022-06-14 03:48:09.393344
# Unit test for method __str__ of class Last
def test_Last___str__():
    assert str(Last(3)) == "Last[value=3]"


# Generated at 2022-06-14 03:48:15.011052
# Unit test for method concat of class Map
def test_Map_concat():
    d1 = Map({
        'a': Sum(1),
        'b': Sum(2),
        'c': Sum(3),
    })
    d2 = Map({
        'a': Sum(4),
        'b': Sum(5),
        'c': Sum(6),
    })
    print('test_Map_concat')
    print(d1)
    print(d2)
    print(d1.concat(d2))
    print('\n')


# Generated at 2022-06-14 03:48:26.749644
# Unit test for method concat of class Min
def test_Min_concat():
    assert Min(1).concat(Min(3)) == Min(1)
    assert Min(1).concat(Min(1)) == Min(1)
    assert Min(3).concat(Min(1)) == Min(1)
    assert Min(2.7).concat(Min(2.7)) == Min(2.7)
    assert Min(2.7).concat(Min(2.9)) == Min(2.7)
    assert Min(2.9).concat(Min(2.7)) == Min(2.7)
    assert Min(2).concat(Min(2)) == Min(2)
    assert Min(2).concat(Min(3)) == Min(2)
    assert Min(3).concat(Min(2)) == Min(2)

# Generated at 2022-06-14 03:48:28.215163
# Unit test for method __str__ of class Min
def test_Min___str__():
    assert str(Min(2)) == "Min[value=2]"


# Generated at 2022-06-14 03:48:32.553736
# Unit test for constructor of class Semigroup
def test_Semigroup():  # pragma: no cover
    assert Semigroup(1) == Semigroup(1)

# Generated at 2022-06-14 03:48:35.012223
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():  # pragma: no cover
    assert Semigroup(1).fold(lambda x: x * 10).value == 10



# Generated at 2022-06-14 03:48:54.790444
# Unit test for method __str__ of class Max
def test_Max___str__():
    # style issue for test function name
    # pylint: disable=C0103
    assert Max(1).__str__() == "Max[value=1]"


# Generated at 2022-06-14 03:48:59.723449
# Unit test for constructor of class All
def test_All():
    assert All(True) == All.neutral()
    assert All(False) != All.neutral()
    assert All(0) == All.neutral()
    assert All(1) == All.neutral()
    assert All('') == All.neutral()
    assert All('0') == All.neutral()
    assert All('1') == All.neutral()
    assert All('True') == All.neutral()

test_All()


# Generated at 2022-06-14 03:49:01.303971
# Unit test for constructor of class Sum
def test_Sum():
    assert Sum(1).value == 1
    assert Sum(2).value == 2


# Generated at 2022-06-14 03:49:04.411154
# Unit test for constructor of class Map
def test_Map():
    assert Map({}) == Map({})
    assert Map({'a': Sum(1)}) != Map({})


# Generated at 2022-06-14 03:49:05.284692
# Unit test for constructor of class Last
def test_Last():
    assert Last(0).value == 0



# Generated at 2022-06-14 03:49:08.035266
# Unit test for method __str__ of class All
def test_All___str__():  # pragma: no cover
    assert str(All(False)) == 'All[value=False]'


# Generated at 2022-06-14 03:49:10.660719
# Unit test for constructor of class One
def test_One():
    one = One(True)
    assert one.value == True


# Generated at 2022-06-14 03:49:13.991817
# Unit test for constructor of class One
def test_One():
    assert One(True) == One(True)
    assert One(1) == One(1)
    assert One("str") == One("str")



# Generated at 2022-06-14 03:49:15.463862
# Unit test for constructor of class Min
def test_Min():
    assert Min(5) == Min(5)


# Generated at 2022-06-14 03:49:18.212520
# Unit test for method concat of class Max
def test_Max_concat():
    a = Max(1)
    b = Max(2)
    c = a.concat(b)
    assert c.value == 2
    assert c == Max(2)


# Generated at 2022-06-14 03:49:54.853487
# Unit test for constructor of class One
def test_One():
    assert One(False) == One(False)



# Generated at 2022-06-14 03:49:56.619471
# Unit test for method concat of class Sum
def test_Sum_concat():
    assert Sum(1).concat(Sum(2)).concat(Sum(3)) == Sum(6)



# Generated at 2022-06-14 03:50:02.880184
# Unit test for constructor of class Min
def test_Min():
    min_1 = Min(1)
    min_2 = Min(2)

    assert min_1.concat(min_2).value == min_1.value

expected_error_msg = "The init parameter value should be a number."
try:
    Min("a")
except TypeError as error:
    assert error == TypeError(expected_error_msg)




# Generated at 2022-06-14 03:50:05.440006
# Unit test for constructor of class Min
def test_Min():
    min_10 = Min(10)
    min_20 = Min(20)
    assert min_10.concat(min_20).value == min_10.value


# Generated at 2022-06-14 03:50:09.712474
# Unit test for method concat of class Max
def test_Max_concat():  # pragma: no cover
    assert Max(4).concat(Max(5)).value == 5
    assert Max(4).concat(Max(4)).value == 4
    assert Max(5).concat(Max(4)).value == 5



# Generated at 2022-06-14 03:50:15.454705
# Unit test for method fold of class Semigroup
def test_Semigroup_fold():
    assert Sum(1).fold(lambda x: x + 1) == 2
    assert All(True).fold(lambda x: not x) == False
    assert First(1).fold(lambda x: x + 1) == 1
    assert Map({'a': Sum(1), 'b': Sum(2)}).fold(lambda x: x['a'].concat(x['b'])) == Sum(3)



# Generated at 2022-06-14 03:50:18.968316
# Unit test for method concat of class First
def test_First_concat():
    """
    Unit test for method concat of class First
    """
    a = First(4)
    b = First(5)

    assert a.concat(b) == a



# Generated at 2022-06-14 03:50:21.208127
# Unit test for method __str__ of class All
def test_All___str__():
    obj = All(True)
    assert obj.__str__() == 'All[value=True]'


# Generated at 2022-06-14 03:50:27.402072
# Unit test for constructor of class Map
def test_Map():
    """
    Unit test for constructor of class Map
    """
    value = Map({1: Sum(1), 2: All(True)})
    assert value.concat(Map({1: Sum(1), 3: First('test')})) == Map({1: Sum(2), 2: All(True), 3: First('test')})



# Generated at 2022-06-14 03:50:31.282805
# Unit test for method concat of class Min
def test_Min_concat():
    min_1 = Min(1)
    min_2 = Min(2)
    expected_Min_3 = Min(1)
    actual_Min_3 = min_1.concat(min_2)
    assert actual_Min_3 == expected_Min_3

# Generated at 2022-06-14 03:51:48.133567
# Unit test for constructor of class All
def test_All():
    assert All(True).value
    assert not All(False).value
    assert All(4).value
    assert not All(0).value
    assert not All("").value
    assert All("4").value


# Generated at 2022-06-14 03:51:49.382321
# Unit test for constructor of class Max
def test_Max():  # pragma: no cover
    assert Max(1).value == 1


# Generated at 2022-06-14 03:51:50.829389
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert str(Max(2)) == 'Max[value=2]'


# Generated at 2022-06-14 03:51:54.610769
# Unit test for method __str__ of class Last
def test_Last___str__():
    assert str(Last(3)) == 'Last[value=3]'
    assert str(Last(None)) == 'Last[value=None]'
    assert str(Last('test')) == 'Last[value=test]'



# Generated at 2022-06-14 03:51:55.861610
# Unit test for method __str__ of class First
def test_First___str__():
    assert str(First(5)) == 'Fist[value=5]'



# Generated at 2022-06-14 03:52:00.244846
# Unit test for constructor of class Map
def test_Map():
    # Case 1: test with input value is empty
    a = Map({})
    assert a.value == {}

    # Case 2: test with input value is not empty
    a = Map({1: 2})
    assert a.value == {1: 2}

# Generated at 2022-06-14 03:52:04.568459
# Unit test for constructor of class Map
def test_Map():
    m = Map({'a': Sum(1), 'b': Sum(2)})
    assert isinstance(m, Map)
    assert(m.value == {'a': Sum(1), 'b': Sum(2)})
    assert('a' in m)


# Generated at 2022-06-14 03:52:14.689518
# Unit test for method concat of class First
def test_First_concat():
    assert First("one").concat(First("two")).value == "one"
    assert First("one").concat(Last("two")).value == "one"
    assert First("one").concat(One("two")).value == "one"
    assert First("one").concat(All("two")).value == "one"
    assert First("one").concat(Sum(2)).value == "one"
    assert First("one").concat(Max(2)).value == "one"
    assert First("one").concat(Min(2)).value == "one"


# Generated at 2022-06-14 03:52:16.372433
# Unit test for constructor of class One
def test_One():
    assert One(True) == One(True)


# Generated at 2022-06-14 03:52:18.915571
# Unit test for method __str__ of class Max
def test_Max___str__():
    assert(str(Max(1)) == 'Max[value=1]')
