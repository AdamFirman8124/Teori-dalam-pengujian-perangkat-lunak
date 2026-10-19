

# Generated at 2022-06-14 03:17:00.816637
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList(1) == ImmutableList(1)
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))) == ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    assert ImmutableList(1) == ImmutableList(1, ImmutableList.empty())
    assert ImmutableList(1, ImmutableList(2, ImmutableList.empty())) == ImmutableList(1, ImmutableList(2))
    assert ImmutableList(1, ImmutableList(2)) != ImmutableList(1, ImmutableList(3))
    assert ImmutableList(1, ImmutableList(2)) != ImmutableList(1, ImmutableList(2, ImmutableList.empty()))
    assert ImmutableList(1) != ImmutableList(2)

# Generated at 2022-06-14 03:17:03.448388
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():

    # given
    list_ = ImmutableList.of(1, 2, 3, 4)

    # when
    result = list_.find(lambda val: val == 3)

    # then
    assert result == 3

# Generated at 2022-06-14 03:17:07.766070
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    list_one = ImmutableList.of(1, 2, 3, 4, 5)
    assert list_one.find(lambda x: x % 2 == 0) == 2
    assert list_one.find(lambda x: x % 2 == 1) == 1
    assert list_one.find(lambda x: x == 5) == 5
    assert list_one.find(lambda x: x > 5) is None



# Generated at 2022-06-14 03:17:13.418916
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # Arrange
    list_class = ImmutableList

    list_value = list_class.of(1, 2, 3)

    # Act
    new_list_value = list_value.filter(lambda x: x > 1)

    # Assert
    assert new_list_value == list_class.of(2, 3), f"incorrect {new_list_value}"



# Generated at 2022-06-14 03:17:18.937043
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList('test') == ImmutableList('test')
    assert not (ImmutableList('test') == ImmutableList('test1'))


# Generated at 2022-06-14 03:17:24.975592
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))) == ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))) == ImmutableList.of(1, 2, 3)
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))) != ImmutableList(1, ImmutableList(2, ImmutableList(2)))
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))) != ImmutableList(1, ImmutableList(2))


# Generated at 2022-06-14 03:17:30.379686
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    l = ImmutableList.of(1, 2, 3, 4, 5)

    l = l.filter(lambda x: x % 2 == 0)

    assert l.to_list() == [2, 4]


# Generated at 2022-06-14 03:17:35.015722
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # Arrange
    test_list = ImmutableList.of(1, 5, 8, 4, 3, 6, 1, 3)

    # Act
    result = test_list.filter(lambda x: x == 3)

    # Assert
    assert result == ImmutableList.of(3, 3)

# Generated at 2022-06-14 03:17:38.922934
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(2, 3, 5, 10).find(lambda x: x % 2 == 0) == 2
    assert ImmutableList.empty().find(lambda x: x % 2 == 0) is None



# Generated at 2022-06-14 03:17:47.492214
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList(42) == ImmutableList(42), "ImmutableList should return True for same elements"
    assert ImmutableList(42) != ImmutableList(666), "ImmutableList should return False for different elements"
    assert ImmutableList(True, ImmutableList(False), False) == ImmutableList(True, ImmutableList(False),
                                                                             False), "ImmutableList should return True for same elements"
    assert ImmutableList(True, ImmutableList(False), False) != ImmutableList(True, ImmutableList(False),
                                                                             True), "ImmutableList should return False for different elements"



# Generated at 2022-06-14 03:17:57.363280
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x > 1) == ImmutableList.of(2, 3)
    assert ImmutableList.of(4, 6, 8).filter(lambda x: x % 2 == 0) == ImmutableList.of(4, 6, 8)
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x % 2 == 0) == ImmutableList.of(2)
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x % 2 != 0) == ImmutableList.of(1, 3)
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(lambda x: x > 5) == ImmutableList(is_empty=True)

# Generated at 2022-06-14 03:18:02.027746
# Unit test for method find of class ImmutableList
def test_ImmutableList_find(): # pragma: no cover
    def is_odd(value):
        return value % 2 != 0

    list_ = ImmutableList.of(1, 2, 3, 4, 5)
    assert list_.find(is_odd) == 1


# Generated at 2022-06-14 03:18:07.173932
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # given
    test_list = ImmutableList.of(1, 2, 3, 4)
    # when
    found = test_list.find(lambda x: x == 2)
    # then
    assert found == 2


# Generated at 2022-06-14 03:18:09.883437
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    result = ImmutableList(1, ImmutableList(2)) == ImmutableList(1, ImmutableList(2))
    assert result, 'Should be true'


# Generated at 2022-06-14 03:18:16.538038
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList(1).find(lambda x: x == 1) == 1
    assert ImmutableList(1, ImmutableList(2)).find(lambda x: x == 1) == 1
    assert ImmutableList(1, ImmutableList(2)).find(lambda x: x == 2) == 2
    assert ImmutableList(1, ImmutableList(2)).find(lambda x: x == 3) is None


# Generated at 2022-06-14 03:18:17.867554
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList() == ImmutableList(is_empty=True)


# Generated at 2022-06-14 03:18:23.145156
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # Should return first value that match predicate
    assert ImmutableList([1, 2, 3, 4, 5]).find(lambda x: x > 1) == 2

    # Should return None if no value matches predicate
    assert ImmutableList([1, 2, 3, 4, 5]).find(lambda x: x == 6) is None


# Generated at 2022-06-14 03:18:32.126954
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList(['a', 'b', 'c', 'd']) == ImmutableList.of('a', 'b', 'c', 'd')
    assert ImmutableList.of('a', 'b', 'c', 'd').filter(lambda x: 'a' in x) == ImmutableList.of('a')
    assert ImmutableList.of('a', 'b', 'c', 'd').filter(lambda x: 'a' not in x) == ImmutableList.of('b', 'c', 'd')
    assert ImmutableList.of('a', 'b', 'c', 'd').filter(lambda x: 'a' in x and 'b' in x) == ImmutableList(is_empty=True)

# Generated at 2022-06-14 03:18:44.170084
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    test_data = ImmutableList.of(1, 2, 3, 4, 5)
    assert test_data.filter(lambda x: x % 2 == 0) == ImmutableList.of(2, 4)



# Generated at 2022-06-14 03:18:47.438387
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(2, 20, 1, 4, 5).find(lambda x: x < 5) == 2
    assert ImmutableList.of(2, 20, 1, 4, 5).find(lambda x: x > 5) == 20
    assert ImmutableList.of(2, 20, 1, 4, 5).find(lambda x: x == 21) is None
    assert ImmutableList.of(2, 20, 1, 4, 5).find(lambda x: isinstance(x, int)) == 2


# Generated at 2022-06-14 03:18:57.176030
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    some_list = ImmutableList.of(1, 2, 3, 4, 5, 6)

    filtered_list = some_list.filter(lambda item: item > 3)

    assert filtered_list == ImmutableList.of(4, 5, 6)



# Generated at 2022-06-14 03:19:09.552702
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    empty_list = ImmutableList().filter(lambda x: True)

    assert empty_list.find(
        lambda x: True
    ) == None

    list_ = ImmutableList.of(1, 2, 3)
    filtered_list = list_.filter(lambda x: x % 2 == 0)
    assert filtered_list.find(
        lambda x: True
    ) == 2

    filtered_list = list_.filter(lambda x: x % 2 == 1)
    assert filtered_list.find(
        lambda x: x % 2 == 1
    ) == 1

    filtered_list = ImmutableList.of(None, 2)
    assert filtered_list.find(
        lambda x: x is None
    ) == None


# Generated at 2022-06-14 03:19:15.488213
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list_of_nums = ImmutableList.of(5, 2, 3, 2, 1, -50)
    expected = ImmutableList.of(5, 3, 1)
    assert list_of_nums.filter(lambda value: value > 0) == expected
    assert list_of_nums.filter(lambda value: value > 0) != expected.append(3)



# Generated at 2022-06-14 03:19:17.029459
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3).find(lambda x: x > 1) == 2



# Generated at 2022-06-14 03:19:20.612428
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    for_filter = [1, 2, 3, 4]
    immutable_list = ImmutableList.of(*for_filter)

    assert(immutable_list.filter(lambda x: x > 2).to_list() == [3, 4])


if __name__ == "__main__":
    test_ImmutableList_filter()

# Generated at 2022-06-14 03:19:31.963992
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    """Tests filter method of ImmutableList class"""
    assert ImmutableList.empty().filter(lambda x: x > 5) == ImmutableList.empty()

    assert ImmutableList(1, ImmutableList(2)).filter(lambda x: x > 5) == ImmutableList.empty()

    assert ImmutableList(1, ImmutableList(2)).filter(lambda x: x < 5) == ImmutableList(1, ImmutableList(2))

    assert ImmutableList(1, ImmutableList(2)).filter(lambda x: x != 2) == ImmutableList(1)

    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))).filter(lambda x: x % 2 != 0) == ImmutableList(1, ImmutableList(3))


# Generated at 2022-06-14 03:19:44.826802
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    empty = ImmutableList.empty()
    assert empty.find(lambda x: x == 10) == None

    int_list = ImmutableList.of(1, 2, 3, 4, 5)
    assert int_list.find(lambda x: x == 10) == None
    assert int_list.find(lambda x: x == 4) == 4
    assert int_list.find(lambda x: x % 2 == 0) == 2

    string_list = ImmutableList.of(1, 'hello', 3, 'world', 5)
    assert string_list.find(lambda x: isinstance(x, str)) == 'hello'
    assert string_list.find(lambda x: isinstance(x, int)) == 1
    
    string_list = ImmutableList.of('hello', 'world', 'python', 'node.js')


# Generated at 2022-06-14 03:19:49.406281
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    actual = ImmutableList.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10).filter(
        lambda x: x % 3 == 0
    )
    expected = ImmutableList.of(3, 6, 9)
    assert actual == expected


# Generated at 2022-06-14 03:19:59.344088
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # Arrange
    my_list = ImmutableList.of(0, 1, 2, 3, 4, 5, 6, 7)

    # Act
    result_even = my_list.find(lambda x: x % 2 == 0)
    result_odd = my_list.find(lambda x: x % 2 != 0)

    # Assert
    assert result_even == 0
    assert result_odd == 1

# Generated at 2022-06-14 03:20:07.665225
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda x: x % 2 == 0) == ImmutableList.of(2, 4)
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda x: x % 2 == 0).head == 2
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda x: x % 2 == 0).tail.head == 4
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda x: x % 2 == 0).tail.tail == ImmutableList.empty()
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda x: x % 2 == 0).tail.tail.head == None


# Generated at 2022-06-14 03:20:27.034221
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():

    # Test for empty list
    assert ImmutableList().find(lambda element: element == 2) == None

    # Test for cases when element exist
    assert ImmutableList.of('value', 2, 3).find(lambda element: element == 2) == 2
    assert ImmutableList.of('value', 2, 3).find(lambda element: element == 3) == 3
    assert ImmutableList.of('value', 2, 3).find(lambda element: isinstance(element, str)) == 'value'

    # Test for cases when element not exist
    assert ImmutableList.of('value', 2, 3).find(lambda element: element == 4) == None
    assert ImmutableList.of('value', 2, 3).find(lambda element: isinstance(element, int)) == 2

# Generated at 2022-06-14 03:20:33.461042
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3).find(lambda el: el % 2 == 0) == 2
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda el: el % 2 == 0) == 2
    assert ImmutableList.of(1, 3, 5, 4, 1).find(lambda el: el % 2 == 0) == 4
    assert ImmutableList.of(1, 3, 5, 5, 1).find(lambda el: el % 2 == 0) is None



# Generated at 2022-06-14 03:20:40.769365
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 1) == 1
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 2) == 2
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 3) == 3
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 4) == 4
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 5) == 5
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 0) == None
    assert ImmutableList.of(1, 2, 3, 4, 5).find

# Generated at 2022-06-14 03:20:46.644104
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda x: x % 2 == 0) == ImmutableList.of(2, 4)
    assert ImmutableList.of(1).filter(lambda x: x > 0) == ImmutableList.of(1)
    assert ImmutableList.empty().filter(lambda x: False) == ImmutableList.empty()

# Generated at 2022-06-14 03:20:50.655168
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    lst = ImmutableList(1, ImmutableList(2, ImmutableList(3)))

    assert lst.filter(lambda x: x % 2 == 1).to_list() == [1, 3]



# Generated at 2022-06-14 03:20:58.316991
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 2) == 2
    assert ImmutableList.of().find(lambda x: x == 2) is None
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 4) is None
    assert ImmutableList.of(1, 2, 3).find(lambda x: x < 2) == 1
    assert ImmutableList.of(1, 2, 3).find(lambda x: x > 2) == 3


# Generated at 2022-06-14 03:21:02.020896
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    lst = ImmutableList.of("Hello", "Hi", "Hey")
    fltered = lst.filter(lambda x: x[0] == "H")
    assert fltered == ImmutableList.of("Hello", "Hi")



# Generated at 2022-06-14 03:21:11.440186
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList()\
        .filter(lambda a: True is True)\
        .is_empty is True
    assert ImmutableList()\
        .filter(lambda a: True is False)\
        .is_empty is True
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3)))\
        .filter(lambda a: a % 2 == 1)\
        .to_list() == [1, 3]
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3)))\
        .filter(lambda a: a % 2 == 0)\
        .to_list() == [2]
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3)))\
        .filter(lambda a: a > 3)\
        .is_empty is True



# Generated at 2022-06-14 03:21:14.494035
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # when
    result = ImmutableList.of(1, 2, 3).find(lambda x: x == 2)

    # then
    assert isinstance(result, int)
    assert result == 2



# Generated at 2022-06-14 03:21:21.242461
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.empty().filter(lambda x: True) == ImmutableList.empty()
    assert ImmutableList(2, ImmutableList(4, ImmutableList(6, ImmutableList(8)))).filter(lambda x: x % 2 == 0) == ImmutableList(2, ImmutableList(4, ImmutableList(6, ImmutableList(8))))
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4)))).filter(lambda x: x % 2 == 0) == ImmutableList(2, ImmutableList(4))
    assert ImmutableList(2, ImmutableList(3, ImmutableList(4, ImmutableList(5)))).filter(lambda x: x % 2 == 0) == ImmutableList(2, ImmutableList(4))

# Generated at 2022-06-14 03:21:46.562072
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    l = ImmutableList.of(1, 2, 3, 4, 5, 6, 7, 8, 9)

    e = l.find(lambda x: x > 3)
    assert e == 4

    e = l.find(lambda x: x > 8)
    assert e is None
    
test_ImmutableList_find()

# Generated at 2022-06-14 03:21:51.539715
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list_ = ImmutableList.of(
        1, 2, 3
    )

    assert list_.filter(lambda x: x > 1).to_list() == [2, 3]

# Generated at 2022-06-14 03:21:55.566942
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(lambda x: x % 2 == 0) == ImmutableList.of(2, 4)



# Generated at 2022-06-14 03:22:14.422097
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    number_list = ImmutableList.of(1, 2, 3, 4, 5)
    string_list = ImmutableList.of('hello', 'world', '!')
    empty_list = ImmutableList.empty()

    assert number_list.find(lambda x: x > 3) == 4
    assert string_list.find(lambda x: x == 'hello') == 'hello'
    assert empty_list.find(lambda x: x == 'foo') is None
    assert number_list.find(lambda x: x == 'foo') is None


# Generated at 2022-06-14 03:22:17.867321
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():  
    # Arrange
    il = ImmutableList.of(1, 2, 3, 4, 5)
    # Act
    il = il.filter(lambda x: x == 1)
    # Assert
    assert len(il) == 1


# Generated at 2022-06-14 03:22:29.018483
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda x: x > 1) == ImmutableList.of(2, 3, 4)
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda x: x < 2) == ImmutableList.of(1)
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda x: x == 5) == ImmutableList.empty()
    # assert ImmutableList.of(1, 2, 3, 4).filter(lambda x: x > 1) == ImmutableList.of(1, 2, 3, 4)
    # assert ImmutableList.of(1, 2, 3, 4).filter(lambda x: x < 2) == ImmutableList.of(1, 2, 3, 4)
    # assert ImmutableList.of

# Generated at 2022-06-14 03:22:39.330320
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.empty().filter(lambda x: True) == ImmutableList.empty()
    assert ImmutableList.of(1, 1, 2, 3).filter(lambda x: x == 1) == ImmutableList.of(1, 1)
    assert ImmutableList.of(1, 2, 3, 5).filter(lambda x: x % 2 == 0) == ImmutableList.of(2)
    assert ImmutableList.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)\
        .filter(lambda x: x % 2 == 0)\
        .filter(lambda x: x > 7) == ImmutableList.of(8, 10)


# Generated at 2022-06-14 03:22:47.638235
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list_ = ImmutableList.of(1, 2, 3, 4, 5)
    assert list_.filter(lambda x: x > 3).to_list() == [4, 5]
    assert list_.filter(lambda x: x < 4).to_list() == [1, 2, 3]
    assert list_.filter(lambda x: x % 2 == 0).to_list() == [2, 4]
    assert list_.filter(lambda x: x > 10) == ImmutableList.empty()
    assert list_.filter(lambda x: x > 10).to_list() == []


# Generated at 2022-06-14 03:22:54.640408
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))).filter(lambda x: x % 2 == 0) == ImmutableList(2)
    assert ImmutableList(1, ImmutableList(3, ImmutableList(5))).filter(lambda x: x % 2 == 0) == ImmutableList(is_empty=True)
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))).filter(lambda x: True) == ImmutableList(1, ImmutableList(2, ImmutableList(3)))

# Generated at 2022-06-14 03:23:06.186104
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1).filter(lambda x: x != 1) == ImmutableList.empty()
    assert ImmutableList.of(1).filter(lambda x: x == 1) == ImmutableList.of(1)

    assert ImmutableList.of(1, 2).filter(lambda x: x == 1) == ImmutableList.of(1)
    assert ImmutableList.of(1, 2).filter(lambda x: x == 2) == ImmutableList.of(2)

# Generated at 2022-06-14 03:23:37.963869
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(lambda x: x % 2 == 0).to_list() == [2, 4]


# Generated at 2022-06-14 03:23:44.505141
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x % 2 == 0) == ImmutableList.of(2)
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x % 2 == 1) == ImmutableList.of(1, 3)
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(lambda x: x % 2 == 1) == ImmutableList.of(1, 3, 5)


# Generated at 2022-06-14 03:23:50.950029
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList(4).find(lambda i: i % 2 == 0) == 4
    assert ImmutableList(5).find(lambda i: i % 2 == 0) == None

    ml = ImmutableList.of(1, 2, 3, 4, 5)
    assert ml.find(lambda i: i % 2 == 0) == 2
    assert ml.find(lambda i: i % 2 == 1) == 1
    assert ml.find(lambda i: i == 6) == None



# Generated at 2022-06-14 03:24:01.829513
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.empty().filter(lambda value: True) == ImmutableList.empty()
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(lambda value: isinstance(value, int)) == ImmutableList.of(1, 2, 3, 4, 5)
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(lambda value: value % 2 == 0) == ImmutableList.of(2, 4)
    assert ImmutableList.of('a', 'b').filter(lambda value: value != 'a') == ImmutableList.of('b')

# Generated at 2022-06-14 03:24:03.558787
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3).filter(lambda x: x > 2).to_list() == [3]

# Generated at 2022-06-14 03:24:07.987124
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    lst1 = ImmutableList.of(1, 2, 3, 4)
    lst2 = ImmutableList.of(2, 3, 4, 5)

    assert lst1.find(lambda x: x == 5) is None
    assert lst1.find(lambda x: x == 4) == 4
    assert lst2.find(lambda x: x == 5) == 5
    assert lst2.find(lambda x: x == 1) is None

# Generated at 2022-06-14 03:24:15.527375
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    list_ = ImmutableList.of('a', 'b', 'c')
    found = list_.find(lambda x: x == 'b')
    assert found == 'b'

    empty_list = ImmutableList.of('a', 'b', 'c')
    found = empty_list.find(lambda x: x == 'd')
    assert found is None

    empty_list = ImmutableList.empty()
    found = empty_list.find(lambda x: True)
    assert found is None


# Generated at 2022-06-14 03:24:21.149473
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    test_list = ImmutableList.of(1, 2, 3, 4, 5)
    # filter for even numbers
    expected_list = ImmutableList.of(2, 4)
    actual_list = test_list.filter(lambda a: a % 2 == 0)
    assert actual_list == expected_list

test_ImmutableList_filter()

# Generated at 2022-06-14 03:24:31.449446
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list = ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4))))
    list_filtered = ImmutableList(2, ImmutableList(4))
    assert list.filter(lambda x: x % 2 == 0) == list_filtered

    list = ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4))))
    list_filtered = ImmutableList(2, ImmutableList(4))
    assert list.filter(lambda x: x % 2 == 0) == list_filtered

    list = ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList(4))))
    list_filtered = ImmutableList(2, ImmutableList(4))

# Generated at 2022-06-14 03:24:35.722377
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list_test = ImmutableList.of("a", "b", "c", "d", "e", "f", "g", "h")
    list_filtered = list_test.filter(lambda x: x in ["a", "b", "c"])

    assert list_filtered == ImmutableList.of("a", "b", "c")

# Generated at 2022-06-14 03:25:47.817316
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    print('Testing method filter of class ImmutableList')

    actual_1 = ImmutableList.of(1, 2, 3, 4, 5).filter(lambda x: x % 2 == 0)
    expected_1 = ImmutableList.of(2, 4)
    print('Test case 1:', actual_1, expected_1)
    assert actual_1 == expected_1


    actual_2 = ImmutableList.empty().filter(lambda x: x % 2 == 0)
    expected_2 = ImmutableList.empty()
    print('Test case 2:', actual_2, expected_2)
    assert actual_2 == expected_2

    actual_3 = ImmutableList.of(1, 2, 3, 4, 5).filter(lambda x: x % 2 == 1)

# Generated at 2022-06-14 03:25:51.771690
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    from unittest import TestCase
    from unittest.mock import Mock, patch

    mock_fn = Mock()
    mock_fn.side_effect = lambda num: num > 5

    l = ImmutableList.of(1, 2, 3, 4, 5, 6, 7)

    assert l.filter(mock_fn).to_list() == [6, 7]
    assert mock_fn.call_count == 7



# Generated at 2022-06-14 03:25:55.121313
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    t1 = ImmutableList.of(1,2,3)
    assert t1.find(lambda n: n == 1) == 1
    assert t1.find(lambda n: n == 3) == 3
    assert t1.find(lambda n: n == 4) == None
test_ImmutableList_find()



# Generated at 2022-06-14 03:25:58.803793
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list_1 = ImmutableList.of('foo', 'bar', 'baz', 'beer')
    filtered_list = list_1.filter(lambda elem: elem[0] != 'b')
    expected_result = ImmutableList.of('foo')
    assert filtered_list == expected_result

# Generated at 2022-06-14 03:26:02.175363
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 3) == 3
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 7) is None

# Generated at 2022-06-14 03:26:15.364452
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.empty() ==  ImmutableList.empty().filter(lambda x: True)
    assert ImmutableList.empty() ==  ImmutableList.of(1).filter(lambda x: False)
    assert ImmutableList.empty() ==  ImmutableList.of(1, 2).filter(lambda x: False)
    assert ImmutableList.of(2, 3) ==  ImmutableList.of(1, 2, 3).filter(lambda x: x > 1)
    assert ImmutableList.of(2, 3) ==  ImmutableList.of(1, 2, 3, 4).filter(lambda x: x > 1)
    assert ImmutableList.of(1, 2) ==  ImmutableList.of(1, 2, 3, 4).filter(lambda x: x <= 2)



# Generated at 2022-06-14 03:26:18.542763
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 2).find(lambda x: x == 2) == 2
    assert ImmutableList.of(1, 2, 3, 2).find(lambda x: x == 0) is None


# Generated at 2022-06-14 03:26:21.777396
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    seq1 = ImmutableList.of(1, 2, 3, 4)
    seq2 = seq1.filter(lambda value: value > 2)

    assert seq2.to_list() == [3, 4]
    assert seq2.is_empty == False


# Generated at 2022-06-14 03:26:27.315877
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # Arrange
    test_data = ImmutableList.of(True, False)
    # Act
    result = test_data.filter(lambda data: data)
    # Assert
    assert result == ImmutableList(True)

# Generated at 2022-06-14 03:26:44.902772
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))).filter(lambda x: x > 3) == ImmutableList.empty()
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3)))\
        .filter(lambda x: x % 2 == 0)\
        .to_list() == [2]
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3)))\
        .filter(lambda x: x == 1)\
        .to_list() == [1]
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3)))\
        .filter(lambda x: x > 1)\
        .to_list() == [2, 3]

