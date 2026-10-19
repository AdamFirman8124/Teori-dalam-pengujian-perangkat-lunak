

# Generated at 2022-06-14 03:16:47.965744
# Unit test for method reduce of class ImmutableList
def test_ImmutableList_reduce():
    assert ImmutableList.of(2, 3, 4).reduce(lambda acc, a: acc + a, 0) == 9
    assert ImmutableList.of(2, 3, 4).reduce(lambda acc, a: acc * a, 1) == 24
    assert ImmutableList.of(2, 3, 4).reduce(lambda acc, a: acc * a, 2) == 48
    assert ImmutableList.of(2, 3, 4).reduce(lambda acc, a: acc * a, 3) == 72
    assert ImmutableList.of(2, 3, 4).reduce(lambda acc, a: acc * a, 4) == 96

# Generated at 2022-06-14 03:16:57.463839
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.of(1, 2, 3) == ImmutableList.of(1, 2, 3)
    assert ImmutableList.of(1, 2, 3) != ImmutableList.of(1, 2)
    assert ImmutableList.of(1, 2, 3) != ImmutableList.of(1, 3, 4)
    assert ImmutableList.of(1, 2, 3) != ImmutableList.of(2, 2, 3)
    assert ImmutableList.of() == ImmutableList.of()
    assert ImmutableList.empty() == ImmutableList.empty()
    assert ImmutableList.of(1, 2, 3) != 1

# Generated at 2022-06-14 03:17:00.067084
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.of('foo', 'bar') == ImmutableList.of('foo', 'bar')\
        == ImmutableList('foo', ImmutableList('bar'))


# Generated at 2022-06-14 03:17:06.134094
# Unit test for method reduce of class ImmutableList
def test_ImmutableList_reduce():
    assert ImmutableList.of(1).reduce(lambda x,y: x+y , 0) == 1
    assert ImmutableList.of(1,2,3).reduce(lambda x,y: x+y , 0) == 6
    assert ImmutableList.of('a', 'b', 'c').reduce(lambda x,y: x+y, '') == 'abc'
    assert ImmutableList.of('a', 'b', 'c').reduce(lambda acc, el: acc + el*3, '') == 'aaabbbccc'
    assert ImmutableList.of().reduce(lambda x,y: x+y, 0) == 0
test_ImmutableList_reduce()

# Generated at 2022-06-14 03:17:16.405083
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.of(1) == ImmutableList.of(1)
    assert ImmutableList.empty() == ImmutableList.empty()
    assert ImmutableList.of(1, 2) == ImmutableList.of(1, 2)

    assert ImmutableList.of(1) != ImmutableList.of(2)
    assert ImmutableList.of(1) != ImmutableList.of(1, 2)
    assert ImmutableList.of(1, 2) != ImmutableList.of(5, 5, 5)



# Generated at 2022-06-14 03:17:20.007570
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    print('== test_ImmutableList___eq__ ==')
    print(ImmutableList.of(1) == ImmutableList(1))


# Generated at 2022-06-14 03:17:27.199065
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # Arrange
    list0 = ImmutableList.empty()
    list1 = ImmutableList.empty()
    list2 = ImmutableList.empty()
    list3 = ImmutableList.empty()
    list4 = ImmutableList.empty()

    list0 = list0.append(1)
    list1 = list1.append(2)
    list2 = list2.append(3)
    list3 = list3.append(4)
    list4 = list4.append(5)

    list0 = list0.append(2)
    list1 = list1.append(3)
    list2 = list2.append(4)
    list3 = list3.append(5)
    list4 = list4.append(6)

    list0 = list0.append(3)

# Generated at 2022-06-14 03:17:32.207666
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    # Given
    expected_result = True
    # When
    result = ImmutableList(1, ImmutableList(2, ImmutableList(3))) == ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    # Then
    assert result == expected_result


# Generated at 2022-06-14 03:17:34.506142
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.of(1) == ImmutableList.of(1)
    assert ImmutableList.of(1, 2) != ImmutableList.of(1)



# Generated at 2022-06-14 03:17:40.466427
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # arrange
    expected = ImmutableList(0, ImmutableList(2, ImmutableList(4, ImmutableList(6))))
    source = ImmutableList.of(0, 1, 2, 3, 4, 5, 6)

    # act
    result = source.filter(lambda x: x % 2 == 0)

    # assert
    assert result == expected



# Generated at 2022-06-14 03:17:53.981064
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4, 5, 6).filter(lambda x: x % 2 == 0) == ImmutableList.of(2, 4, 6)
    assert ImmutableList.of(1, 2, 3, 4, 5, 6).filter(lambda x: x % 2 == 1) == ImmutableList.of(1, 3, 5)
    assert ImmutableList.of(-1, 2, 3, -4, 5, -6).filter(lambda x: x < 0) == ImmutableList.of(-1, -4, -6)
    assert ImmutableList.of(-1, 2, 3, -4, 5, -6).filter(lambda x: x > 0) == ImmutableList.of(2, 3, 5)
    assert ImmutableList.empty().filter(lambda x: x > 0)

# Generated at 2022-06-14 03:17:58.527632
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    test_ImmutableList = ImmutableList.of(1, 2, 3, 4, 5)
    result_ImmutableList = test_ImmutableList.filter(lambda x: x % 2)

    assert result_ImmutableList == ImmutableList.of(1, 3, 5)

# Generated at 2022-06-14 03:18:04.864356
# Unit test for method reduce of class ImmutableList
def test_ImmutableList_reduce():
    list = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    assert list.reduce(lambda a, b: a + b, 0) == 6
    assert list.reduce(lambda a, b: a * b, 1) == 6
    assert list.reduce(lambda a, b: a / b, 6) == 1.5



# Generated at 2022-06-14 03:18:13.702569
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x % 2 == 0) == 2
    assert ImmutableList.of(1, 3, 5, 7).find(lambda x: x % 2 == 0) is None
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x % 2 == 1) == 1
    assert ImmutableList.of(2, 4, 6, 8).find(lambda x: x % 2 == 1) is None


# Generated at 2022-06-14 03:18:18.755084
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # arranges
    imm_list = ImmutableList.of(1, 2, 3)

    # acts
    new_list = imm_list.filter(lambda x: x % 2 == 1)

    # asserts
    expected = [1, 3]

    assert new_list.to_list() == expected
    assert imm_list.to_list() == [1, 2, 3]


# Generated at 2022-06-14 03:18:27.571532
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList().filter(lambda x: x) == ImmutableList.empty()
    assert ImmutableList(1).filter(lambda x: not x) == ImmutableList.empty()
    assert ImmutableList(1).filter(lambda x: x) == ImmutableList(1)
    assert ImmutableList(2, ImmutableList(1)).filter(lambda x: x > 1) == ImmutableList(2)
    assert ImmutableList(2, ImmutableList(2, ImmutableList(1))).filter(lambda x: x > 1) == ImmutableList(2, ImmutableList(2))

# Generated at 2022-06-14 03:18:32.728780
# Unit test for method reduce of class ImmutableList
def test_ImmutableList_reduce():
    assert ImmutableList.of(0, 1, 2, 3).reduce(lambda acc, x: acc + x, 0) == 6
    assert ImmutableList.of(0, 1, 2, 3).reduce(lambda acc, x: acc + x, 1) == 7
    assert ImmutableList.of(0, 1, 2, 3).reduce(lambda acc, x: acc * x, 1) == 0
    assert ImmutableList.of(1, 2, 3).reduce(lambda acc, x: acc * x, 1) == 6


# Generated at 2022-06-14 03:18:43.628288
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # Test cases for method find of class ImmutableList
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x == 1) == 1
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x == 4) == 4
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x == 3) == 3
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x == 5) is None
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x == 6) is None
    assert ImmutableList.empty().find(lambda x: x == 1) is None
    assert ImmutableList.of(5).find(lambda x: x == 1) is None
test_Immutable

# Generated at 2022-06-14 03:18:47.834562
# Unit test for method reduce of class ImmutableList
def test_ImmutableList_reduce():
    assert ImmutableList.of(10, 2, 3, 5).reduce(
        lambda sum_, element: sum_ + element, 0
    ) == 20

# Generated at 2022-06-14 03:18:51.800607
# Unit test for method reduce of class ImmutableList
def test_ImmutableList_reduce():
    list_of_numbers = ImmutableList(1, ImmutableList(2), ImmutableList(3))
    result = list_of_numbers.reduce(lambda acc, x: acc + x, 0)
    assert result == 6

# Generated at 2022-06-14 03:19:00.230622
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 4).find(lambda value: value == 2) == 2
    assert ImmutableList.of(1, 2, 3, 4).find(lambda value: value == 5) is None
    assert ImmutableList.of().find(lambda value: value == 2) is None


# Generated at 2022-06-14 03:19:09.105056
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1).find(lambda x: x == 1) == 1
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 2) == 2
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 5) == 5
    assert ImmutableList.of(2, 2, 3, 4, 5).find(lambda x: x == 1) is None
    assert ImmutableList.of(2, 2, 3, 4, 5).find(lambda x: x == 6) is None


# Generated at 2022-06-14 03:19:14.630220
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 2) == 2
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 3) == 3
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 4) == ImmutableList.empty()



# Generated at 2022-06-14 03:19:21.568775
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 4).find(lambda a: a > 3) == 4
    assert ImmutableList.of(1, 2, 3, 4).find(lambda a: a > 4) == None
    assert ImmutableList.empty().find(lambda a: True) == None



# Generated at 2022-06-14 03:19:26.511903
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    test_list = ImmutableList.of(9,7,5,2,1)
    assert test_list.find(lambda i: i == 3) is None
    assert test_list.find(lambda i: i == 1) == 1
    assert test_list.find(lambda i: i == 9) == 9


# Generated at 2022-06-14 03:19:32.131917
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list1 = ImmutableList.of(1, 2, 3, 4, 5)
    list2 = ImmutableList.empty()

    assert list1.filter(lambda x: x >= 3).to_list() == [3, 4, 5]
    assert list2.filter(lambda x: True) == ImmutableList.empty()


# Generated at 2022-06-14 03:19:38.870154
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    fn = lambda x: x > 2
    numbers = ImmutableList.of(1, 2, 3, 4, 5)
    greater_than_two = numbers.filter(fn)

    assert list(greater_than_two) == [3, 4, 5]



# Generated at 2022-06-14 03:19:50.513881
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # Define tests
    def is_positive(num) -> bool:
        return num > 0


# Generated at 2022-06-14 03:20:01.866982
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # Check if None as result of find
    assert ImmutableList.empty().find(lambda x: x) is None

    # Check if find with parameter None elements
    assert ImmutableList.empty().find(lambda x: False) is None

    # Check if find on non empty list
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 3) == 3

    # Check if find on non empty list with all elements passed
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: True) == 1



# Generated at 2022-06-14 03:20:06.727513
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x == 3) == 3, "Find first element"
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x > 2) == 3, "Find element > 2"
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x == 1001) is None, "Find element that not exists"


# Generated at 2022-06-14 03:20:14.965977
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    my_list = ImmutableList.empty()
    assert my_list.find(lambda x: x == 4) is None, 'Should return None'
    
    my_list = ImmutableList.of(2, 3, 4)
    assert my_list.find(lambda x: x == 2) == 2, 'Should return 2'
    assert my_list.find(lambda x: x == 4) == 4, 'Should return 4'
    assert my_list.find(lambda x: x == 1) is None, 'Should return None'
    


# Generated at 2022-06-14 03:20:17.158032
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x == 3) == 3

# Generated at 2022-06-14 03:20:22.479008
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    list_ = ImmutableList(5, ImmutableList(3, ImmutableList(6, ImmutableList(7))))
    assert list_.find(lambda x: x == 3) == 3
    assert list_.find(lambda x: x == 10) is None



# Generated at 2022-06-14 03:20:26.022285
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    empty_list = ImmutableList.empty()
    assert empty_list.find(lambda x: x == 1) is None
    assert empty_list.filter(lambda x: x == 1).is_empty

    lst = ImmutableList.of(1, 2, 3, 4)
    assert lst.find(lambda x: x == 1) is 1
    assert lst.find(lambda x: x == -1) is None

test_ImmutableList_find()

# Generated at 2022-06-14 03:20:31.268775
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    data = [1, 3, 5, 7]

    expected = ImmutableList.of(*data)
    actual = ImmutableList()

    for element in data:
        actual = actual.append(element)

    assert expected == actual
    assert actual.find(lambda x: x == 3) == 3
    assert actual.find(lambda x: x == 9) is None


test_ImmutableList_find()

# Generated at 2022-06-14 03:20:34.867266
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    lst = ImmutableList(2, ImmutableList(4, ImmutableList(6)))
    assert lst.find(lambda x: x % 2 == 0) == 2
    assert lst.find(lambda x: x % 3 == 0) == 6
    assert lst.find(lambda x: x > 10) is None



# Generated at 2022-06-14 03:20:39.520605
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # GIVEN
    a = ImmutableList.of(1, 2, 3, 4, 5)
    # THEN
    assert a.find(lambda x: x == 3) == 3
    assert a.find(lambda x: x == 0) is None



# Generated at 2022-06-14 03:20:44.950454
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x % 3 == 0) == 3
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x % 5 == 0) is None

# Generated at 2022-06-14 03:20:49.975246
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    a = ImmutableList.of(1, 2, 3, 4, 5)
    assert a.find(lambda x: x == 3) == 3
    assert a.find(lambda x: x == 6) is None

    b = ImmutableList.of(1, 2, 3, 4, 5)
    assert b.find(lambda x: x > 5) is None
    assert b.find(lambda x: x == 5) == 5


test_ImmutableList_find()

# Generated at 2022-06-14 03:21:00.547872
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    list_elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # test that find method return even first element of list
    to_find = ImmutableList.of(*list_elements)
    assert to_find.find(lambda x: x % 2 == 0) == 2
    # test that find method return first even element of list
    odd_head = ImmutableList(1, ImmutableList.of(*list_elements[1:]), False)
    assert odd_head.find(lambda x: x % 2 == 0) == 2
    # test that find method return None if not found
    assert odd_head.find(lambda x: x % 2 == 1) is None



# Generated at 2022-06-14 03:21:14.161869
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    im_list = ImmutableList.of(1, 2, 3)

    assert im_list.find(lambda x: x == 1) == 1
    assert im_list.find(lambda x: x == 2) == 2
    assert im_list.find(lambda x: x == 3) == 3
    assert im_list.find(lambda x: x == 4) is None


# Generated at 2022-06-14 03:21:18.079722
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3).find(lambda x: x > 1) == 2
    assert ImmutableList.of(1, 2, 3).find(lambda x: x > 2) == 3
    assert ImmutableList.of(1, 2, 3).find(lambda x: x > 3) is None
    assert ImmutableList.empty().find(lambda x: x > 1) is None

test_ImmutableList_find()

# Generated at 2022-06-14 03:21:25.931585
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.empty().find(lambda x: x) is None
    assert ImmutableList.of(1).find(lambda x: x) == 1
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 1) == 1
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 2) == 2
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 3) == 3
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 4) is None
    assert ImmutableList.of(1, 2, 3).find(lambda x: x) == 1



# Generated at 2022-06-14 03:21:28.398653
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x > 4) == 5

# Generated at 2022-06-14 03:21:31.380453
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    m = ImmutableList.of(1, 2, 3, 4, 5)
    assert m.find(lambda x: x == 4) == 4
    assert m.find(lambda x: x == 9) == None

# Generated at 2022-06-14 03:21:35.970160
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # Given
    input_list = ImmutableList.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    expected_output = 6
    test_case = lambda x: x == expected_output

    # When
    output = input_list.find(test_case)

    # Then
    assert output == expected_output


# Generated at 2022-06-14 03:21:41.059423
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # arrange
    expected_result = 10
    test_list = ImmutableList.of(
        1,
        2,
        3,
        10,
        20
    )

    # act
    result = test_list.find(lambda e: e == expected_result)

    # assert
    assert(result == expected_result)


# Generated at 2022-06-14 03:21:48.241452
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    args = [
        [ImmutableList.of(1, 2, 3, 4, 5, 6), lambda x: x % 2 == 0, 2],
        [ImmutableList.of(1, 2, 3, 4, 5, 6), lambda x: x % 2 == 1, 1],
        [ImmutableList.of(1, 2, 3, 4, 5, 6), lambda x: x % 2 == 0, 2],
        [ImmutableList.of(1, 2, 3, 4, 5, 6), lambda x: x % 2 == 1, 1],
    ]
    for arg in args:
        assert arg[0].find(arg[1]) == arg[2]

# Generated at 2022-06-14 03:21:58.923075
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    a = ImmutableList.of(1, 2, 3)
    b = ImmutableList.of('a', 'b', 'c')
    c = ImmutableList.of('a', 'b', 'c', 'd', 'e')

    assert a.find(lambda x: x == 1) == 1
    assert a.find(lambda x: x == 2) == 2
    assert a.find(lambda x: x == 3) == 3
    assert a.find(lambda x: x > 2) == 3
    assert a.find(lambda x: x < 2) == 1

    assert b.find(lambda x: x == 'a') == 'a'
    assert b.find(lambda x: x == 'b') == 'b'
    assert b.find(lambda x: x == 'c') == 'c'

# Generated at 2022-06-14 03:22:03.228104
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # initialize class
    obj = ImmutableList(1, ImmutableList(2), ImmutableList(3))
    # get we need value
    value = obj.find(lambda x: x == 1)
    # check we get we need
    assert value == 1


# Generated at 2022-06-14 03:22:23.047109
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(5, 4, 3, 2, 1).find(lambda x: x > 3) == 4

# Generated at 2022-06-14 03:22:34.263472
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # Case 1
    assert ImmutableList.of('a').find(lambda x: True) is 'a'

    # Case 2
    assert ImmutableList.of('a').find(lambda x: False) is None

    # Case 3
    assert ImmutableList.of('a', 'b').find(lambda x: True) is 'a'

    # Case 4
    assert ImmutableList.of('a', 'b').find(lambda x: x == 'a') is 'a'

    # Case 5
    assert ImmutableList.of('a', 'b').find(lambda x: x == 'b') is 'b'

    # Case 6
    assert ImmutableList.of('a', 'b').find(lambda x: x == 'c') is None


# Generated at 2022-06-14 03:22:38.513296
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1,2,3).find(lambda x: x % 2 == 0) == 2

    assert ImmutableList.of(1,2,3,4).find(lambda x: x % 2 == 0) == 2

    assert ImmutableList.of(1,2,3,4)[2] == 3

# Generated at 2022-06-14 03:22:49.672432
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # given
    def is_odd(number):
        return number % 2 != 0

    list_with_even_numbers = ImmutableList.of(2, 4, 6)

    # when
    firs_odd_number_or_none = list_with_even_numbers.find(is_odd)

    # then
    assert firs_odd_number_or_none is None

    # given
    list_with_odd_numbers = ImmutableList.of(1, 3, 5)

    # when
    first_odd_number = list_with_odd_numbers.find(is_odd)

    # then
    assert first_odd_number == 1

    # given
    list_with_odd_and_even_numbers = ImmutableList.of(1, 3, 5, 6, 7, 8)

# Generated at 2022-06-14 03:22:55.135212
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    list_one = ImmutableList.of(1, 2, 3)
    assert list_one.find(lambda x: x == 1) == 1

    list_two = ImmutableList.of(1, 2, 3)
    assert list_two.find(lambda x: x == 5) is None

    list_three = ImmutableList.of(1, 2, 3)
    assert list_three.find(lambda x: x > 2) == 3



# Generated at 2022-06-14 03:23:06.870870
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    test_data = [
        (['a', 'b', 'c'], lambda x: x == 'b', 'b'),
        (['a', 'b', 'c'], lambda x: x == 'd', None),
        (['a', 'b', 'c'], lambda x: x == 'a', 'a'),
        ([], lambda x: x == 'a', None),
    ]

    for list_data, fn, expected_result in test_data:
        assert ImmutableList.of(*list_data).find(fn) == expected_result


# Generated at 2022-06-14 03:23:10.244116
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    populated_list = ImmutableList.of(1, 2, 3, 4)
    assert populated_list.find(lambda a: a > 1) == 2

    empty_list = ImmutableList.empty()
    assert empty_list.find(lambda a: a > 1) is None

# Generated at 2022-06-14 03:23:15.440874
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(0, 1, 2).find(lambda v: v == 1) == 1
    assert ImmutableList.of(0, 1, 2).find(lambda v: v == 10) is None
    assert ImmutableList.of().find(lambda v: v == 10) is None
    
    

# Generated at 2022-06-14 03:23:21.301272
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList(1).find(lambda x: x == 1) == 1
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))).find(lambda x: x == 3) == 3
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))).find(lambda x: x == 4) is None


# Generated at 2022-06-14 03:23:25.562627
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # Setup
    il = ImmutableList.of(2, 3, 5, 7)

    # Exercise
    res = il.find(lambda x: x % 2 == 0)

    # Verify
    assert res == 2

    # Cleanup - none necessary


# Generated at 2022-06-14 03:24:09.108867
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert(ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 3) == 3)
    assert(ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 3) == 3)
    assert(ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 6) == None)
    assert(ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 7) == None)
    assert(ImmutableList.empty().find(lambda x: x == 6) == None)
    assert(ImmutableList.empty().find(lambda x: x == 7) == None)

# Generated at 2022-06-14 03:24:16.277752
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda value: value > 2) == 3
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda value: value > 5) == None
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda value: value == 1) == 1
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda value: value == 5) == 5


# Generated at 2022-06-14 03:24:20.852926
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    numbers = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    result = numbers.find(lambda x: x == 2)
    assert result == 2, \
        'Should return 2'

    result = numbers.find(lambda x: x == 3)
    assert result == 3, \
        'Should return 3'

    result = numbers.find(lambda x: x == 4)
    assert result is None, \
        'Should return None'



# Generated at 2022-06-14 03:24:24.663730
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    list1 = ImmutableList.of('a', 'b', 'c')
    assert list1.find(lambda x: x == 'a') == 'a'
    assert list1.find(lambda x: x == 'b') == 'b'
    assert list1.find(lambda x: x == 'c') == 'c'
    assert list1.find(lambda x: x == 'd') is None


# Generated at 2022-06-14 03:24:33.729041
# Unit test for method find of class ImmutableList

# Generated at 2022-06-14 03:24:44.663666
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.empty().find(lambda e: e == 1) is None
    assert ImmutableList.empty().find(lambda e: False) is None

    assert ImmutableList(1).find(lambda e: e == 1) == 1
    assert ImmutableList(0).find(lambda e: e > 0) is None

    assert ImmutableList(1, ImmutableList(2)).find(lambda e: e == 2) == 2
    assert ImmutableList(1, ImmutableList(2)).find(lambda e: e > 2) is None

    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))).find(lambda e: e == 3) == 3
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))).find(lambda e: e > 3) is None


# Unit

# Generated at 2022-06-14 03:24:48.888124
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    list_ = ImmutableList.of(1, 2, 3, 4)
    assert list_.find(lambda x: x > 2) == 3
    # assert list_.find(lambda x: 5 == 2) == None



# Generated at 2022-06-14 03:24:55.470501
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    empty_list = ImmutableList()
    number_list = ImmutableList.of(1, 2, 3, 4, 5)

    assert empty_list.find(lambda value: value < 6) is None
    assert number_list.find(lambda value: value < 6) is 1
    assert number_list.find(lambda value: value > 3) is 4
    assert number_list.find(lambda value: value > 10) is None


# Generated at 2022-06-14 03:24:57.302528
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    a = ImmutableList.of(1, 2, 3)
    assert 1 == a.find(lambda x: x > 0)



# Generated at 2022-06-14 03:25:02.611999
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 3) == 3
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 6) is None
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 5) == 5
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 1) == 1



# Generated at 2022-06-14 03:26:31.206916
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    some = ImmutableList.of(1, 2, 3, 4, 5)
    none = ImmutableList.of(1, 3, 5, 7, 9)

    assert some.find(lambda el: el % 2 == 0) == 2
    assert none.find(lambda el: el % 2 == 0) is None

# Generated at 2022-06-14 03:26:45.221420
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3).find(lambda x: x % 2 == 0) == 2

    assert ImmutableList.empty().find(lambda x: x % 2 == 0) is None

    assert ImmutableList.of(1, 2, 3).find(lambda x: x % 2 == 1) == 1