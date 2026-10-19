

# Generated at 2022-06-14 03:16:59.810771
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    # Test data
    data = [
        dict(
            list=ImmutableList(1, ImmutableList(2, ImmutableList(3))),
            expected=ImmutableList(1, ImmutableList(2, ImmutableList(3)))
        ),
        dict(
            list=ImmutableList(1, ImmutableList(2, ImmutableList(3))),
            expected=ImmutableList(2, ImmutableList(3))
        ),
        dict(
            list=ImmutableList(1, ImmutableList(2, ImmutableList(3))),
            expected=ImmutableList()
        ),
        dict(
            list=ImmutableList(),
            expected=ImmutableList()
        ),
    ]

# Generated at 2022-06-14 03:17:06.404757
# Unit test for method __eq__ of class ImmutableList

# Generated at 2022-06-14 03:17:16.476229
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.empty().filter(lambda v: True) == ImmutableList()
    assert ImmutableList(2, 3, 4).filter(lambda v: v == 3) == ImmutableList(3)
    assert ImmutableList(2, 3, 4).filter(lambda v: v > 3) == ImmutableList(4)
    assert ImmutableList(2, 3, 4).filter(lambda v: v > 5) == ImmutableList()
    assert ImmutableList().filter(lambda v: v > 5) == ImmutableList.empty()

# Generated at 2022-06-14 03:17:22.314639
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    array = ImmutableList.of(1, 2, 3, 4, 5, 6, 7, 8, 9)
    result = array.filter(lambda x: x % 2 == 0)
    array2 = ImmutableList.of(2, 4, 6, 8)
    assert str(result) == str(array2)



# Generated at 2022-06-14 03:17:36.323534
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.of(1, 2, 3) == ImmutableList.of(1, 2, 3)
    assert ImmutableList.empty() == ImmutableList.empty()
    assert ImmutableList(1) == ImmutableList(1)
    assert ImmutableList(1, ImmutableList(2)) == ImmutableList(1, ImmutableList(2))
    assert ImmutableList.of(1, 2, 3) != ImmutableList.empty()
    assert ImmutableList.empty() != ImmutableList.of(1, 2, 3)
    assert ImmutableList(1) != ImmutableList(2)
    assert ImmutableList(1, ImmutableList(2)) != ImmutableList(1, ImmutableList(3))
    # You can add more tests here


# Generated at 2022-06-14 03:17:47.083094
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    empty_list = ImmutableList()
    assert empty_list == ImmutableList.empty(), 'First empty list equal to second one'

    empty_list = ImmutableList(False, None, True)
    assert empty_list == ImmutableList.empty(), 'Third empty list equal to second one'

    list_ = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    assert list_ == ImmutableList.of(1, 2, 3), 'ImmutableList with three elements equal to list'

    # list_ is ImmutableList.of(1, 2, 3)
    assert list_ != ImmutableList.of(2, 2, 3), 'List with first element different is not equal'

    # list_ is ImmutableList.of(1, 2, 3)

# Generated at 2022-06-14 03:17:49.609457
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(10, -10, 15, -20, -25, 20).filter(lambda x: x > 0) == ImmutableList.of(10, 15, 20)

# Generated at 2022-06-14 03:17:52.837910
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    list_ = ImmutableList.of(1, 2, 3, 4)
    new_list = list_.filter(lambda x: x > 2)
    assert new_list == ImmutableList.of(3, 4)


# Generated at 2022-06-14 03:18:05.620036
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.of(1, 2, 3) == ImmutableList.of(1, 2, 3)
    assert ImmutableList.empty() == ImmutableList.empty()
    assert ImmutableList(1) == ImmutableList(1)
    assert ImmutableList(1) != ImmutableList(2)
    assert ImmutableList.of(1, 2, 3) != ImmutableList.of(1, 2)
    assert ImmutableList(1, ImmutableList(2), False) != ImmutableList(2, ImmutableList(2), False)
    assert ImmutableList(1, None, False) != ImmutableList.of(1,2)
    assert ImmutableList.empty() != ImmutableList.of(1)

# Generated at 2022-06-14 03:18:12.387330
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    a1 = ImmutableList.of(1)
    a2 = ImmutableList.of(1)
    a3 = ImmutableList.of(1, 2)
    a4 = ImmutableList.of(1, 2)

    assert a1 == a1
    assert a1 == a2
    assert not a1 == a3
    assert not a1 == a4



# Generated at 2022-06-14 03:18:25.937978
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 4) is None
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 3) == 3
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 1) == 1
    assert ImmutableList.of(1, 2, 3).find(lambda x: True) == 1

# Generated at 2022-06-14 03:18:32.342952
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert True == ImmutableList.empty() == ImmutableList.empty()
    assert False == ImmutableList.empty() == ImmutableList.of(1)
    assert False == ImmutableList.empty() == None
    assert True == ImmutableList(1, ImmutableList(2, ImmutableList(3))) == ImmutableList.of(1, 2, 3)
    assert True == ImmutableList(1, ImmutableList(2, ImmutableList(3))) == ImmutableList.of(1, 2, 3) == ImmutableList(
        1, ImmutableList(2, ImmutableList(3)))



# Generated at 2022-06-14 03:18:45.901534
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(lambda x: x > 3) == ImmutableList.of(4, 5)
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(lambda x: x > 8) == ImmutableList.of()



# Generated at 2022-06-14 03:18:53.336538
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    l1 = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    l2 = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    assert l1 == l2
    assert not l1 != l2

    l1 = ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList.empty())))
    l2 = ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    assert not l1 == l2
    assert l1 != l2

    l1 = ImmutableList(1, ImmutableList(2, ImmutableList(3, ImmutableList.empty())))
    l2 = ImmutableList(1, ImmutableList(2, ImmutableList(4)))
    assert not l1 == l2
    assert l1

# Generated at 2022-06-14 03:18:59.663045
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    # Method immutable list eq test 1
    def test_1():
        assert ImmutableList.of(1, 2, 3) == ImmutableList.of(1, 2, 3)

    # Method immutable list eq test 2
    def test_2():
        assert ImmutableList.of(1, 2, 3, 5) == ImmutableList.of(1, 2, 3, 5)

    # Method immutable list eq test 3
    def test_3():
        assert ImmutableList.of(0) == ImmutableList.empty()

    test_1()
    test_2()
    test_3()


# Generated at 2022-06-14 03:19:09.312008
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.of(1, 2, 3, 4, 5).filter(lambda x: x > 2) == ImmutableList.of(3, 4, 5)
    assert ImmutableList.of(2, 4, 6, 8).filter(lambda x: x > 2) == ImmutableList.of(4, 6, 8)
    assert ImmutableList.of(1, 3, 5, 7).filter(lambda x: x > 5) == ImmutableList.of(7)
    assert ImmutableList.of(1, 3, 5, 7).filter(lambda x: x < 5) == ImmutableList.of(1, 3)
    assert ImmutableList.empty().filter(lambda x: True) == ImmutableList.empty()


# Generated at 2022-06-14 03:19:15.272527
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1,2,3,4,5).find(lambda x: x > 3) == 4
    assert ImmutableList.of(1,2,3,4,5).find(lambda x: x % 2 == 0) == 2
    assert ImmutableList.of(1,2,3,4,5).find(lambda x: x <= 3) == 3

# Generated at 2022-06-14 03:19:23.012168
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.empty().filter(lambda x: True) == ImmutableList(is_empty=True)
    assert ImmutableList.empty().filter(lambda x: False) == ImmutableList(is_empty=True)
    assert ImmutableList(1).filter(lambda x: True) == ImmutableList(1)
    assert ImmutableList(1).filter(lambda x: False) == ImmutableList(is_empty=True)
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))).filter(lambda x: True) == ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))).filter(lambda x: False) == ImmutableList(is_empty=True)

# Generated at 2022-06-14 03:19:33.572588
# Unit test for method filter of class ImmutableList
def test_ImmutableList_filter():
    assert ImmutableList.empty().filter(lambda x: x) == ImmutableList.empty()
    assert ImmutableList(1).filter(lambda x: x) == ImmutableList(1)
    assert ImmutableList(1).filter(lambda x: not x) == ImmutableList.empty()
    assert ImmutableList(1, ImmutableList(2)).filter(lambda x: x == 1) == ImmutableList(1)
    assert ImmutableList(1, 2).filter(lambda x: x) == ImmutableList(1, 2)
    assert ImmutableList(1, 2).filter(lambda x: not x) == ImmutableList.empty()
    assert ImmutableList(1, 2, 3).filter(lambda x: x % 2) == ImmutableList(1, 3)

# Generated at 2022-06-14 03:19:37.714020
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    list_example = ImmutableList(1, ImmutableList(2))
    assert list_example.find(lambda x: x == 1) == 1
    
    

# Generated at 2022-06-14 03:19:56.773251
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    list = ImmutableList.of(1, 2, 3)

    assert list == ImmutableList.of(1, 2, 3)
    assert ImmutableList.empty() == ImmutableList.empty()


# Generated at 2022-06-14 03:20:03.139330
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # create ImmutableList
    maybe1 = ImmutableList.of(2, 3, 5, 7, 11, 13, 17)

    # find with predicate
    result = maybe1.find(lambda x: x == 7)

    assert result == 7

    result = maybe1.find(lambda x: x % 3 == 0)

    assert result == 3

    # Unit test for method map of class ImmutableList

# Generated at 2022-06-14 03:20:10.967927
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    # Test case when head and tail are equal
    assert ImmutableList.of(1, 2, 3) == ImmutableList.of(1, 2, 3)

    # Test case when head and tail are different
    assert not ImmutableList.of(1, 2, 3) == ImmutableList.of(1, 4, 5)

    # Test case when ImmutableList.__eq__ compares to non-ImmutableList object
    assert not ImmutableList.of(1, 2, 3) == 'ImmutableList'

    # Test for empty list
    assert ImmutableList(is_empty=True) == ImmutableList(is_empty=True)
    assert not ImmutableList(is_empty=True) != ImmutableList(is_empty=True)


# Generated at 2022-06-14 03:20:17.278655
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    l = ImmutableList.of(1, 2, 3)

    assert l.find(lambda x: x == 2) == 2
    assert l.find(lambda x: x == 5) is None
    assert l.find(lambda x: x < 5) == 1

# Generated at 2022-06-14 03:20:23.363269
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    value = ImmutableList.of(0, 1, 2, 3).find(lambda x: x > 1)
    assert value == 2, 'assert value == 2'
    value = ImmutableList.of(0, 1, 2, 3).find(lambda x: x > 4)
    assert value is None, 'assert value is None'

# Generated at 2022-06-14 03:20:33.165177
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList(1, ImmutableList(2, ImmutableList(3))) == ImmutableList(1, ImmutableList(2, ImmutableList(3)))
    assert not ImmutableList(1, ImmutableList(2, ImmutableList(3))) == ImmutableList(1, ImmutableList(2, ImmutableList(4)))
    assert not ImmutableList(1, ImmutableList(2, ImmutableList(3))) == ImmutableList(1, ImmutableList(4, ImmutableList(3)))
    assert not ImmutableList(1, ImmutableList(2, ImmutableList(3))) == ImmutableList(4, ImmutableList(2, ImmutableList(3)))
    assert not ImmutableList(1, ImmutableList(2, ImmutableList(3))) == ImmutableList(1)

# Generated at 2022-06-14 03:20:42.301000
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    assert ImmutableList.of(1) == ImmutableList(1)
    assert ImmutableList.of(1, 2) == ImmutableList(1, ImmutableList.of(2))
    assert ImmutableList.of(1, 2) == ImmutableList(1, ImmutableList(2))
    assert ImmutableList.of(1, 2, 3) == ImmutableList(1, ImmutableList(2, ImmutableList.of(3)))

    assert ImmutableList.of(1) != ImmutableList.empty()
    assert ImmutableList.of(1) != ImmutableList(1, ImmutableList.empty())
    assert ImmutableList.of(1, 2) != ImmutableList(1)
    assert ImmutableList.of(1, 2) != ImmutableList(1, ImmutableList.of(3))
   

# Generated at 2022-06-14 03:20:47.105950
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert (
        ImmutableList.of(1, 2, 3).find(lambda x: x == 3) == 3
    )
    assert (
        ImmutableList.of(1, 2, 3).find(lambda x: x == 4) == None
    )
    print("ImmutableList: test find - ok")


# Generated at 2022-06-14 03:20:54.526994
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x == 2) == 2
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x > 2) == 3
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x > 10) is None
    assert ImmutableList.empty().find(lambda x: x > 10) is None


# Generated at 2022-06-14 03:20:58.801648
# Unit test for method __eq__ of class ImmutableList
def test_ImmutableList___eq__():
    l1 = ImmutableList.of(1, 2, 3)
    l2 = ImmutableList.of(1, 2, 3)
    l3 = l1
    l4 = ImmutableList.of(1, 2, 3, 4)

    assert l1 == l2
    assert l1 == l3
    assert l1 != l4
    assert l1 != ImmutableList.empty()
    assert ImmutableList.empty() == ImmutableList.empty()

# Generated at 2022-06-14 03:21:10.877518
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # Construct new ImmutableList and test method find
    test_list = ImmutableList.of('first', 'second', 'third')
    assert test_list.find(lambda x: x == 'first') == 'first'
    assert test_list.find(lambda x: x == 'second') == 'second'
    assert test_list.find(lambda x: x == 'third') == 'third'
    assert test_list.find(lambda x: x == 'fourth') is None
    # Test empty list
    test_list = ImmutableList()
    assert test_list.find(lambda x: x == 'first') is None


# Generated at 2022-06-14 03:21:14.870318
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    array = ImmutableList.of(1, 2, 3, 4, 5, 6)
    even = array.filter(lambda x: x % 2 == 0)
    assert 6 == even.reduce(lambda acc,x: x, 0)
    
    
test_ImmutableList_find()

# Generated at 2022-06-14 03:21:21.128114
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    """
    Method executes a reducer function
    on each element of the array, resulting in a single output value.

    :param fn: function to call with ImmutableList value
    :type fn: Function(A, B) -> A
    :returns: A
    """
    assert ImmutableList.of().find(lambda x: x == True) == None
    assert ImmutableList.of(1).find(lambda x: x == 1) == 1
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 4) == 4
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x == 9) == None

test_ImmutableList_find()



# Generated at 2022-06-14 03:21:23.793316
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    l = ImmutableList.of(1, 2, 3, 4, 5, 6, 7)
    assert l.find(lambda x: x % 2 == 0) == 2
    
    

# Generated at 2022-06-14 03:21:29.318995
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList(1, ImmutableList(2)).find(lambda x: x > 1) == 2
    assert ImmutableList(1, ImmutableList(2)).find(lambda x: x < 1) is None
    assert ImmutableList(1, ImmutableList(2)).find(lambda x: x == 1) == 1


# Generated at 2022-06-14 03:21:39.610119
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.empty().find(lambda x: x is not None) is None
    assert ImmutableList.of(1).find(lambda x: x is not None) == 1
    assert ImmutableList.of(1, 2).find(lambda x: x is not None) == 1
    assert ImmutableList.of(1, 2).find(lambda x: x is None) is None
    assert ImmutableList.of(1, 2).find(lambda x: x == 2) == 2

    assert ImmutableList.of(1, 2, 3).find(lambda x: x is not None) == 1
    assert ImmutableList.of(1, 2, 3).find(lambda x: x is None) is None
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 3) == 3

# Unit

# Generated at 2022-06-14 03:21:42.630447
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(10, 20, 30, 40).find(lambda x: x > 30) == 40
    assert ImmutableList.of(10, 20, 30, 40).find(lambda x: x > 40) is None



# Generated at 2022-06-14 03:21:47.157448
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.empty().find(lambda x: x if x is None else False) is None
    assert ImmutableList.of(1).find(lambda x: x if x is None else False) is None
    assert ImmutableList.of(100, 200).find(lambda x: x if x is None else False) is None
    assert ImmutableList.of(True, False).find(lambda x: x if x is None else False) is None
    assert ImmutableList.of('', '', '').find(lambda x: x if x is None else False) is None

    assert ImmutableList.empty().find(lambda x: x if x is not None else False) is None
    assert ImmutableList.of(None).find(lambda x: x if x is not None else False) is None

# Generated at 2022-06-14 03:21:58.600504
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1).find(lambda x: x == 1) == 1
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 2) == 2
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 4) is None
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 3) == 3
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 1) == 1

    assert ImmutableList.of(1).find(lambda x: x == 0) is None
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 0) is None
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 5) is None

# Generated at 2022-06-14 03:22:01.359752
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # arrange
    class1 = ImmutableList.of(1, 2, 3, 4, 5)
    class2 = ImmutableList.of(1, 2, 4, 5, 6)

    # assert
    assert class1.find(lambda x: x == 3) == 3
    assert class2.find(lambda x: x == 3) is None



# Generated at 2022-06-14 03:22:25.780999
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # Test find method
    assert ImmutableList.of(1).find(lambda x: True) == 1
    assert ImmutableList.of(1, 2).find(lambda x: x == 2) == 2
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 3) == 3



# Generated at 2022-06-14 03:22:29.223407
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    sample = ImmutableList.of(1, 2, 3)
    assert sample.find(lambda x: x % 2 == 0) == 2



# Generated at 2022-06-14 03:22:38.388269
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    element = ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x > 2)
    assert 3 == element
    element = ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x > 4)
    assert 5 == element
    element = ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x > 10)
    assert element is None
    element = ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x < 0)
    assert element is None

# Generated at 2022-06-14 03:22:48.294835
# Unit test for method find of class ImmutableList
def test_ImmutableList_find(): # pragma: no cover
    fn = lambda x: x > 2

    immutable_list = ImmutableList.of(1, 2, 3, 4)
    assert immutable_list.find(fn) == 3

    immutable_list = ImmutableList.of(4, 3, 2, 1)
    assert immutable_list.find(fn) == 4

    immutable_list = ImmutableList.of(1, 2, 3, 4)
    assert immutable_list.filter(fn) == ImmutableList.of(3, 4)

    immutable_list = ImmutableList.of(4, 3, 2, 1)
    assert immutable_list.filter(fn) == ImmutableList.of(4, 3)


# Generated at 2022-06-14 03:23:05.567839
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    list_empty = ImmutableList.empty()
    list_of_one = ImmutableList.of(1)
    list_of_many = ImmutableList.of(1, 2, 3, 4)

    def is_one(x):
        return x == 1

    assert list_empty.find(is_one) == None
    assert list_of_one.find(is_one) == 1
    assert list_of_many.find(is_one) == 1


# Generated at 2022-06-14 03:23:11.123752
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.empty().find(lambda x: x == 2) is None
    assert ImmutableList(1).find(lambda x: x == 2) is None
    assert ImmutableList(1).find(lambda x: x == 1) == 1
    assert ImmutableList(1, ImmutableList(2)).find(lambda x: x == 2) == 2
    assert ImmutableList(1, ImmutableList(2)).find(lambda x: x == 3) is None


# Generated at 2022-06-14 03:23:13.893855
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.empty().find(lambda x: x == 'any') is None
    assert ImmutableList.of('any').find(lambda x: x == 'any') == 'any'
    assert ImmutableList.of(1, 2, 3).find(lambda x: x == 3) == 3

# Generated at 2022-06-14 03:23:23.833062
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    imm_list = ImmutableList.of(0, 1, 2, 3)
    assert imm_list.find(lambda x: x == 2) == 2

    imm_list = ImmutableList.of(0, 1, 2, 3)
    assert imm_list.find(lambda x: x == 9) is None

    imm_list = ImmutableList.empty()
    assert imm_list.find(lambda x: x == 2) is None


# Generated at 2022-06-14 03:23:26.072145
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    list = ImmutableList.of(1, 2, 3, 4)
    assert list.find(lambda x: x == 2) == 2
    return True



# Generated at 2022-06-14 03:23:31.547688
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x == 1) == 1
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x == 4) == 4
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x < 5) == 1
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x < 0) is None



# Generated at 2022-06-14 03:23:59.235269
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x > 2) == 3
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x > 5) is None

test_ImmutableList_find()

# Generated at 2022-06-14 03:24:04.613741
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x > 2) == 3
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x > 10) != 10
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: x > 10) is None
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: None) is None
    assert ImmutableList.of(1, 2, 3, 4).find(lambda x: 'sample string') is None

# Generated at 2022-06-14 03:24:14.406677
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.empty().find(lambda x: True) == None

    assert ImmutableList.of(1).find(lambda x: True) == 1
    assert ImmutableList.of(1).find(lambda x: False) == None

    assert ImmutableList.of(0, 1, 2, 3, 4, 5, 6).find(lambda x: x == 3) == 3
    assert ImmutableList.of(0, 1, 2, 3, 4, 5, 6).find(lambda x: x == 6) == 6
    assert ImmutableList.of(0, 1, 2, 3, 4, 5, 6).find(lambda x: x == 7) == None
    assert ImmutableList.of(0, 1, 2, 3, 4, 5, 6).find(lambda x: x < 3) == 0
    assert ImmutableList

# Generated at 2022-06-14 03:24:19.816002
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    a = ImmutableList.of(1,2,3,4,5)
    b = ImmutableList.of(Start=1, End=2)
    assert a.find(_ == 5) == 5
    assert a.find(_ == 6) is None
    assert b.find(_ == 5) is None
    assert b.find(_ == 1) == 1

# Generated at 2022-06-14 03:24:24.122388
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():

    # Arrange
    lst = ImmutableList.of(1, 2, 3, 4, 5)

    # Act
    result = lst.find(lambda x: x == 3)

    # Assert
    assert result == 3



# Generated at 2022-06-14 03:24:29.259274
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    list1 = ImmutableList.of(1, 2, 3, 4, 5, 6)
    assert list1.find(lambda x: x % 2 == 0) == 2
    assert list1.find(lambda x: x % 2 == 1) == 1
    assert list1.find(lambda x: x > 100) is None

    list1 = ImmutableList.of(1)
    assert list1.find(lambda x: x % 2 == 0) is None
    assert list1.find(lambda x: x % 2 == 1) == 1
    assert list1.find(lambda x: x > 100) is None



# Generated at 2022-06-14 03:24:37.056026
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    test_list_1 = ImmutableList.of(1, 2, 3)
    assert test_list_1.find(lambda x: x == 3) == 3, "Test 1 for method find of class ImmutableList failed"
    
    
    test_list_2 = ImmutableList.of(1, 2, 3)
    assert test_list_2.find(lambda x: x == 4) is None, "Test 2 for method find of class ImmutableList failed"
    
    
    test_list_3 = ImmutableList.empty()
    assert test_list_3.find(lambda x: x == 1) is None, "Test 3 for method find of class ImmutableList failed"
    
# Test execution
test_ImmutableList_find()

# Generated at 2022-06-14 03:24:41.623016
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    l = ImmutableList.of(2, 9, 3, 1, 8)
    assert l.find(lambda n: n % 2 == 0) == 2
    assert l.find(lambda n: n == 5) is None



# Generated at 2022-06-14 03:24:50.435917
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList(1).find(lambda x: x == 1) == 1
    assert ImmutableList(1).find(lambda x: x == 2) is None
    assert ImmutableList(1, ImmutableList(2)).find(lambda x: x == 1) == 1
    assert ImmutableList(1, ImmutableList(2)).find(lambda x: x == 2) == 2
    assert ImmutableList(1, ImmutableList(2)).find(lambda x: x == 3) is None
    assert ImmutableList(1, ImmutableList(2)).find(lambda x: x == 0) is None
    

# Generated at 2022-06-14 03:24:54.576213
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda i: i > 3) == 4
    assert ImmutableList.of(1, 2, 3, 4, 5).find(lambda i: i > 5) is None



# Generated at 2022-06-14 03:25:55.700519
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    result = ImmutableList.of(1, 2, 3, 4).find(
        lambda x: x % 2 == 0
    )
    assert(result == 2)



# Generated at 2022-06-14 03:26:12.812892
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    # Case: find first element that bigger than 5
    assert ImmutableList.of(1, 2, 5, 10).find(lambda x: x > 5) == 10

    # Case: find first element that bigger than 5 but not exists
    assert ImmutableList.of(1, 2, 5).find(lambda x: x > 5) is None

    # Case: find first element in empty list
    assert ImmutableList.empty().find(lambda x: x > 5) is None



# Generated at 2022-06-14 03:26:15.919526
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.of('a').find(lambda x: x > 'b') is None
    assert ImmutableList.of('a', 'b', 'c', 'd').find(lambda x: x > 'b') is 'c'

# Generated at 2022-06-14 03:26:21.467490
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    v = ImmutableList.of(1, 2, 3, 4, 5)

    # we want to find value divisible by 3
    divisible_by_3 = lambda x: x % 3 == 0
    assert 3 == v.find(divisible_by_3)

    # there is no value divisible by 6
    divisible_by_6 = lambda x: x % 6 == 0
    assert None is v.find(divisible_by_6)



# Generated at 2022-06-14 03:26:32.224312
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList.empty().find(lambda x: True) == None
    assert ImmutableList.of(True).find(lambda x: True) == True
    assert ImmutableList.of(False).find(lambda x: True) == None
    assert ImmutableList.of(None, True, False).find(lambda x: True) == True
    assert ImmutableList.of(None, True, False).find(lambda x: False) == False
    assert ImmutableList.of(None, False, False).find(lambda x: False) == False



# Generated at 2022-06-14 03:26:50.772689
# Unit test for method find of class ImmutableList
def test_ImmutableList_find():
    assert ImmutableList(2, ImmutableList(2, ImmutableList(3, ImmutableList(3, ImmutableList(3, ImmutableList(3))))))\
        .find(lambda x: x != 2) == 3
    assert ImmutableList(2, ImmutableList(2, ImmutableList(2, ImmutableList(2, ImmutableList(2, ImmutableList(2))))))\
        .find(lambda x: x != 2) == None
    assert ImmutableList(2, ImmutableList(2, ImmutableList(3, ImmutableList(3, ImmutableList(3, ImmutableList(3))))))\
        .find(lambda x: x > 3) == None