

# Generated at 2022-06-14 03:57:56.036592
# Unit test for function curried_map
def test_curried_map():
    map_function = curried_map(lambda x: x + 1)
    map_result = map_function([1, 2, 3])

    assert(map_result == [2, 3, 4])


# Generated at 2022-06-14 03:57:59.779369
# Unit test for function cond
def test_cond():
    pred1 = lambda x: x > 1
    pred2 = lambda x: x < -1
    pred3 = lambda x: True
    action1 = lambda x: x + 1
    action2 = lambda x: x - 1
    action3 = lambda x: x - 1
    action4 = lambda x: x + 1
    preds = [pred1, pred2, pred3]
    actions = [action1, action2, action3]
    conded_action = cond([(pred, action) for pred, action in zip(preds, actions)])
    assert conded_action(2) == 3
    assert conded_action(-2) == -3
    assert conded_action(0) == -1



# Generated at 2022-06-14 03:58:03.286023
# Unit test for function find
def test_find():
    assert find([], eq(5)) is None
    assert find([1, 2, 3], eq(5)) is None
    assert find([1, 2, 3], eq(2)) == 2



# Generated at 2022-06-14 03:58:06.286006
# Unit test for function find
def test_find():
    items = [1, 2, 3, 4, 5, 1, 2]
    print(find(items, eq(1)))
    assert 1 == find(items, eq(1))
    assert None == find(items, eq(10))



# Generated at 2022-06-14 03:58:12.106078
# Unit test for function curried_map
def test_curried_map():
    collection = [1,2,3]
    mapper = increase

    assert [2,3,4] == curried_map(mapper, collection)
    assert [2,3,4] == curried_map(mapper)(collection)
    assert [2,3,4] == curried_map(mapper)(collection)


# Generated at 2022-06-14 03:58:24.882482
# Unit test for function curried_filter
def test_curried_filter():
    # Empty list
    assert curried_filter(lambda x: x, []) == []
    # Not empty list
    assert curried_filter(lambda x: x, [1, 2, 3, 4, 5, 6, 7]) == [1, 2, 3, 4, 5, 6, 7]
    # Not empty list and list with false predicate
    assert curried_filter(lambda x: x > 3, [1, 2, 3, 4, 5, 6, 7]) == [4, 5, 6, 7]
    # Filter even numbers
    assert curried_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7]) == [2, 4, 6]


# Generated at 2022-06-14 03:58:35.845459
# Unit test for function cond
def test_cond():
    cond_test = cond([
        (lambda x: x == 0, lambda x: 0),
        (lambda x: x == 1, lambda x: 1),
        (lambda x: x == 2, lambda x: 2),
    ])
    assert cond_test(0) == 0
    assert cond_test(1) == 1
    assert cond_test(2) == 2
    assert cond_test(3) is None
    assert cond_test(4) is None



# Generated at 2022-06-14 03:58:44.360732
# Unit test for function curried_map
def test_curried_map():
    """
    Test function curried_map.

    :returns: no return value
    :rtype: None
    """
    assert curried_map(identity)([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert curried_map(increase)([1, 2, 3, 4]) == [2, 3, 4, 5]
    assert curried_map(lambda x: x ** 2)([1, 2, 3, 4]) == [1, 4, 9, 16]
    assert curried_map(increase, [1, 2, 3, 4]) == [2, 3, 4, 5]
    assert curried_map(lambda x: x ** 2, [1, 2, 3, 4]) == [1, 4, 9, 16]



# Generated at 2022-06-14 03:58:45.727592
# Unit test for function eq
def test_eq():
    assert eq(2, 2)
    assert eq('A', 'A')



# Generated at 2022-06-14 03:58:51.455070
# Unit test for function curried_filter
def test_curried_filter():
    """
    Currying: eq is called with first argument
    """

    positive_numbers = curried_filter(eq(1))
    assert positive_numbers([-2, -1, 0, 1, 2, 1, 2]) == [1, 1]



# Generated at 2022-06-14 03:59:00.293102
# Unit test for function find
def test_find():
    assert find([1, 2, 3, 1], eq(1)) == 1
    assert find([1, 2, 3, 1], eq(2)) == 2
    assert find([1, 2, 3, 1], eq(4)) is None



# Generated at 2022-06-14 03:59:05.193929
# Unit test for function find
def test_find():
    """
    Unit test for function find
    :returns:
    """
    collection = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    assert(find(collection, eq(9)) == 9)
    assert(find(collection, eq(11)) is None)



# Generated at 2022-06-14 03:59:12.396691
# Unit test for function memoize
def test_memoize():
    import datetime

    @memoize
    def time_consuming_function():
        time.sleep(1)
        return datetime.datetime.now().time()

    print(time_consuming_function())
    print(time_consuming_function())
    print(time_consuming_function())
    print(time_consuming_function())
    print(time_consuming_function())


# Generated at 2022-06-14 03:59:16.834005
# Unit test for function memoize
def test_memoize():
    import random
    memoize_add = memoize(lambda x: x + 1)
    old_add = lambda x: x + 1
    random_numbers = [random.randint(0, 100) for _ in range(100)]
    assert all([memoize_add(x) == old_add(x) for x in random_numbers])

test_memoize()

# Generated at 2022-06-14 03:59:23.964200
# Unit test for function find
def test_find():
    sampleList = [
        {'type': 'first', 'value': 'sample'},
        {'type': 'second', 'value': 'sample'},
    ]

    assert(find(sampleList, lambda item: item['type'] == 'first') == {'type': 'first', 'value': 'sample'})
    assert(find(sampleList, lambda item: item['type'] == 'third') is None)


# Generated at 2022-06-14 03:59:30.123629
# Unit test for function find
def test_find():
    assert find(
        collection=[1, 2, 3],
        key=eq(1)
    ) == 1

    assert find(
        collection=[1, 2, 3],
        key=eq(4)
    ) is None

    assert find(
        collection=['foo', 'bar'],
        key=eq('foo')
    ) == 'foo'

    assert find(
        collection=['foo', 'bar'],
        key=eq('baz')
    ) is None



# Generated at 2022-06-14 03:59:33.742632
# Unit test for function cond
def test_cond():
    def even(x):
        return x % 2 == 0

    def odd(x):
        return not even(x)

    def test(x):
        return x

    condition_list = [
        (even, test),
        (odd, test),
    ]
    cond_fn = cond(condition_list)
    assert cond_fn(1) == 1
    assert cond_fn(2) == 2



# Generated at 2022-06-14 03:59:41.223424
# Unit test for function find
def test_find():
    """
    Test suite for function find

    :returns: None
    :rtype: None
    """
    # For collection [1, 2, 3] and condition equal 2 we expect result 2
    assert find([1, 2, 3], eq(2)) == 2

    # For collection [1, 2, 3] and condition equal 5 we expect result None
    assert find([1, 2, 3], eq(5)) is None

    print("Test suite for find is ok")



# Generated at 2022-06-14 03:59:42.981893
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x % 2 == 0, [1, 2, 3, 4]) == [2, 4]
    assert curried_filter(lambda x: x % 2 == 0)([1, 2, 3, 4]) == [2, 4]



# Generated at 2022-06-14 03:59:44.773188
# Unit test for function find
def test_find():
    assert find([0, 1, 2, 3], lambda x: x == 1) == 1
    assert find([0, 1, 2, 3], lambda x: x == 4) == None



# Generated at 2022-06-14 03:59:55.638823
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(lambda x: x+1)([1, 2]) == [2, 3]


# Generated at 2022-06-14 03:59:57.254118
# Unit test for function eq
def test_eq():
    assert eq(1, 1)
    assert not eq(1, 2)


test_eq()


# Generated at 2022-06-14 04:00:02.265305
# Unit test for function memoize
def test_memoize():
    counter = 0

    @memoize
    def add(x):
        nonlocal counter
        counter = counter + 1
        return x + 1

    assert add(1) == 2
    assert counter == 1

    assert add(1) == 2
    assert counter == 1



# Generated at 2022-06-14 04:00:05.267833
# Unit test for function find
def test_find():
    collection = [1, 2, 3, 4, 5]
    key = eq(3)
    assert find(collection, key) == 3


# Generated at 2022-06-14 04:00:12.474207
# Unit test for function curried_map
def test_curried_map():
    # One argument per call
    assert curried_map(lambda x: x + 1)([1, 2, 3]) == [2, 3, 4], "Failed curried_map_1"

    # More than one argument per call
    assert curried_map(lambda x, y: x + y, [1, 2, 3])([1, 2, 3]) == [2, 4, 6], "Failed curried_map_2"



# Generated at 2022-06-14 04:00:14.949040
# Unit test for function curried_map
def test_curried_map():
    assert map(increase, [1, 2, 3, 4, 5]) == curried_map(increase)([1, 2, 3, 4, 5])



# Generated at 2022-06-14 04:00:24.820827
# Unit test for function memoize
def test_memoize():
    count_calls = {
        'get_id': 0,
        'get_username': 0,
    }
    user = {
        'id': 0,
        'username': 'admin'
    }

    def get_id(user):
        count_calls['get_id'] += 1
        return user['id']

    def get_username(user):
        count_calls['get_username'] += 1
        return user['username']

    cache_get_id = memoize(get_id, key=lambda x, y: x == y)
    cache_get_username = memoize(get_username, key=lambda x, y: x == y)

    for i in range(10):
        assert cache_get_id(user) == get_id(user)
        assert cache_get_username(user)

# Generated at 2022-06-14 04:00:33.255388
# Unit test for function eq
def test_eq():
    assert eq(1, 1) is True
    assert eq(1, 2) is False
    assert eq(2)(2) is True
    assert eq(1)(1) is True
    assert eq(1)(2) is False
    assert eq(1, 2)() is False
    assert eq(2)(2)() is True
    assert eq(2, 2)() is True
    assert eq(1, 2, 3)() is False
    assert eq(2, 2, 3)() is True



# Generated at 2022-06-14 04:00:39.779697
# Unit test for function memoize
def test_memoize():
    import time

    def slow_function(x):
        time.sleep(x)
        return x

    memoized_slow_function = memoize(slow_function)

    start = time.time()
    assert memoized_slow_function(0.50) == 0.50
    assert memoized_slow_function(0.50) == 0.50
    assert time.time() - start < 0.60


if __name__ == "__main__":
    test_memoize()

# Generated at 2022-06-14 04:00:41.491556
# Unit test for function eq
def test_eq():
    assert eq(1)(1)
    assert not eq(1)(2)
    assert eq(2)(2)


# Generated at 2022-06-14 04:00:56.865254
# Unit test for function eq
def test_eq():
    assert True is eq(1, 1)
    assert False is eq(1, 2)
    assert True is eq(1)(1)
    assert False is eq(1)(2)
    assert True is eq(1)(1)(1)
    assert False is eq(1)(1)(2)



# Generated at 2022-06-14 04:01:00.156774
# Unit test for function eq
def test_eq():
    eq(1, 1)
    eq({'a': 1}, {'a': 1})
    eq([1, 2], [1, 2])



# Generated at 2022-06-14 04:01:11.003587
# Unit test for function curry
def test_curry():
    add_three_numbers = lambda *args: sum(args)
    add_three_numbers_curried = curry(add_three_numbers)

    # curried function should return function, which contains some part of arguments
    assert callable(add_three_numbers_curried(1))
    # curried function should return result, when all arguments passed
    assert add_three_numbers_curried(1, 3, 5) == 9

    # curried function should return curried function, which contains some part of arguments
    assert callable(add_three_numbers_curried(1)(1))
    # curried function should return result, when all arguments passed
    assert add_three_numbers_curried(1)(2)(3) == 6

    # curried function should return curried function, which contains some part of arguments
   

# Generated at 2022-06-14 04:01:12.333632
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(increase)([1, 2, 3]) == [2, 3, 4]



# Generated at 2022-06-14 04:01:13.625007
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(identity)([1, 2, 3]) == [1, 2, 3]

# Generated at 2022-06-14 04:01:25.702128
# Unit test for function cond
def test_cond():
    def is_zero(value):
        return value == 0

    def is_odd(value):
        return value % 2 != 0

    def is_even(value):
        return value % 2 == 0

    def factorial(value):
        return 1 if value == 0 else value * factorial(value - 1)

    def error(*args):
        raise Exception('Argument is not valid: ' + ' '.join([str(arg) for arg in args]))

    condition_list = [
        (is_zero, lambda arg: 1),
        (is_odd, lambda arg: arg * factorial(arg - 1)),
        (is_even, lambda arg: factorial(arg - 1)),
        (lambda *args: True, error)
    ]

    fact = cond(condition_list)

    assert fact(0) == 1

# Generated at 2022-06-14 04:01:36.606440
# Unit test for function cond
def test_cond():
    function_one = lambda value: value == 1
    function_two = lambda value: value == 2
    function_default = lambda value: value * 3

    cond_function = cond([
        (function_one, lambda x: x),
        (function_two, lambda x: x),
        (lambda value: True, function_default),
    ])

    assert cond_function(0) == 0
    assert cond_function(1) == 1
    assert cond_function(2) == 2
    assert cond_function(3) == 9
    assert cond_function(10) == 30
    assert cond_function(-1) == -3



# Generated at 2022-06-14 04:01:42.559800
# Unit test for function curried_filter
def test_curried_filter():
    """Test curried_filter function"""
    # Iterable for test
    iterable = ['a', 'b', 'c']
    # Define curry functions
    curry_func = curry(curried_filter(eq('a')))
    # Expected result
    result = ['a']
    # Get result of test
    assert curry_func(iterable) == result



# Generated at 2022-06-14 04:01:46.303401
# Unit test for function curried_filter
def test_curried_filter():
    func = curried_filter(lambda x: x >= 3)
    result = func(range(5))
    assert list(result) == [3, 4]



# Generated at 2022-06-14 04:01:58.878797
# Unit test for function cond
def test_cond():
    # Define functions
    def is_null(value):
        return value is None

    def is_equal(value):
        return value == 3

    def is_number(value):
        return isinstance(value, int)

    def incr(value):
        return increase(value)

    def return_value(value):
        return value

    def noop():
        pass

    # Init condition list
    condition_list = [
        (is_null, noop),
        (is_equal, incr),
        (is_number, return_value),
    ]

    # Test correct execution
    assert cond(condition_list)(None) is None
    assert cond(condition_list)(3) == 4
    assert cond(condition_list)(7) == 7



# Generated at 2022-06-14 04:02:20.954513
# Unit test for function memoize
def test_memoize():
    # unit test for function memoize
    @memoize
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    assert factorial(5) == 120
    assert factorial(6) == 720



# Generated at 2022-06-14 04:02:27.794352
# Unit test for function curried_filter
def test_curried_filter():
    assert () == tuple(curried_filter(lambda x: x > 0)([-1, 0, 1, 2]))
    assert (1, 2) == tuple(curried_filter(lambda x: x > 0)([1, 2]))
    assert (2,) == tuple(curried_filter(lambda x: x > 1)([1, 2]))
    assert (1, 2) == tuple(curried_filter(lambda x: x > 0, [1, 2]))
    assert (1, 2) == tuple(curried_filter(lambda x: x > 0)((1, 2)))
    assert (1, 2) == tuple(curried_filter(lambda x: x > 0, (1, 2)))



# Generated at 2022-06-14 04:02:29.503510
# Unit test for function curried_map
def test_curried_map():
    assert [3, 4, 5] == curried_map(lambda x: x + 2, [1, 2, 3])



# Generated at 2022-06-14 04:02:38.378945
# Unit test for function memoize
def test_memoize():
    from random import random
    import time

    random_numbers_list = []

    for i in range(10):
        random_numbers_list.append(random())

    start = time.time()
    [random() for i in range(1000000)]
    end = time.time()
    
    print("Time without memoizations: {}".format(end - start))

    curried_random = memoize(random)

    start = time.time()
    [curried_random() for i in range(1000000)]
    end = time.time()

    print("Time with memoizations: {}".format(end - start))

# test_memoize()

# Generated at 2022-06-14 04:02:44.261640
# Unit test for function find
def test_find():
    assert find([1, 2, 3], lambda x: x == 1) == 1
    assert find([1, 2, 3], lambda x: x == 3) == 3
    assert find(['test', 'asd'], lambda x: x == 'test') == 'test'
    assert find(['test', 'asd'], lambda x: x == 'asd') == 'asd'



# Generated at 2022-06-14 04:02:55.050994
# Unit test for function cond
def test_cond():
    def always_true(arg):
        return True

    def always_false(arg):
        return False

    def is_even(arg: int) -> bool:
        return arg % 2 == 0

    def is_odd(arg: int) -> bool:
        return arg % 2 != 0

    def negate(arg: int) -> int:
        return arg * -1

    def identity(arg: int) -> int:
        return arg

    def double(arg: int) -> int:
        return arg * 2

    assert cond([
        (always_true, identity),
        (always_false, negate),
    ])(-1) == -1
    assert cond([
        (always_false, identity),
        (always_true, negate),
    ])(-1) == -1

# Generated at 2022-06-14 04:02:59.756562
# Unit test for function eq
def test_eq():
    assert eq(1, 1) is True
    assert eq(1, 2) is False
    assert eq(1, '1') is False
    assert eq(1, True) is False
    assert eq('', '') is True
    assert eq(None, None) is True



# Generated at 2022-06-14 04:03:03.086998
# Unit test for function curry
def test_curry():
    assert curry(lambda x, y, z: x + y + z)(1)(2)(3) == 6
    assert curry(lambda x, y, z: x + y + z)(1)(2, 3) == 6



# Generated at 2022-06-14 04:03:07.541831
# Unit test for function eq
def test_eq():
    """
    Test function eq.

    :returns: True if all tests passed, else False.
    :rtype: Boolean
    """
    return eq(1, 1) and not eq(1, 0) and eq(1, 1.0)



# Generated at 2022-06-14 04:03:13.918957
# Unit test for function memoize
def test_memoize():
    """
    Test memoize function
    """
    def test_function(argument):
        return argument * 2

    print(test_function(5))
    test_memoized_function = memoize(test_function)
    print(test_memoized_function(5))
    print(test_memoized_function(5))


if __name__ == '__main__':
    test_memoize()

# Generated at 2022-06-14 04:03:54.070609
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(identity, [1, 2, 3]) == [1, 2, 3]
    assert curried_map(increase, [1, 2, 3]) == [2, 3, 4]
    assert curried_map(lambda x:x*2, [1, 2, 3]) == [2, 4, 6]


# Generated at 2022-06-14 04:03:55.744358
# Unit test for function eq
def test_eq():
    assert eq(1, 1) is True
    assert eq(1, 2) is False


# Generated at 2022-06-14 04:04:07.295441
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x > 2, [1, 2, 3, 4, 5]) == [3, 4, 5]
    assert curried_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]) == [2, 4]
    assert curried_filter(lambda x: x % 2 != 0, [1, 2, 3, 4, 5]) == [1, 3, 5]
    assert curried_filter(lambda x: x % 2 == 0)([1, 2, 3, 4, 5]) == [2, 4]
    assert curried_filter(lambda x: x % 2 != 0)([1, 2, 3, 4, 5]) == [1, 3, 5]
    assert curried_filter(lambda x: x % 2 == 0, []) == []
    assert curried

# Generated at 2022-06-14 04:04:14.978394
# Unit test for function memoize
def test_memoize():
    """
    Test if memoize works well
    """
    def square(x):
        print(f'calculating {x} square')
        return x**2

    memoized_square = memoize(square)

    assert memoized_square(5) == 25
    assert memoized_square(5) == 25
    assert memoized_square(5) != 10
    assert memoized_square(5) != 10



# Generated at 2022-06-14 04:04:18.191284
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x % 2 == 0)(range(5)) == [0, 2, 4]



# Generated at 2022-06-14 04:04:24.143757
# Unit test for function cond
def test_cond():
    cond_fn = cond([
        (eq(0), lambda value: 'zero'),
        (eq(1), lambda value: 'one'),
        (lambda value: True, lambda value: 'unknown'),
    ])
    assert cond_fn(0) == 'zero'
    assert cond_fn(1) == 'one'
    assert cond_fn(2) == 'unknown'



# Generated at 2022-06-14 04:04:29.977395
# Unit test for function memoize
def test_memoize():
    def function_to_memoize(a):
        print('executing function')
        return a
    memoized_function = memoize(function_to_memoize)
    memoized_function(1)
    memoized_function(2)
    memoized_function(1)
    memoized_function(2)

# Generated at 2022-06-14 04:04:36.984637
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(lambda x: x + 1, [1, 2, 3]) == [2, 3, 4]
    assert curried_map(lambda x: x + 1, [])([1, 2, 3]) == [2, 3, 4]
    assert curried_map(lambda x: x + 1)([1, 2, 3]) == [2, 3, 4]



# Generated at 2022-06-14 04:04:44.564770
# Unit test for function curried_filter
def test_curried_filter():
    import unittest

    class TestFilterMethods(unittest.TestCase):
        def test_curried_filter(self):
            def filterer_function(value):
                return value % 2 == 0

            collection = [1, 2, 3, 4, 5, 6, 7, 8]
            filtered_collection = curried_filter(filterer_function, collection)
            self.assertEqual(
                [2, 4, 6, 8],
                filtered_collection,
                "Should filter collection by odd numbers"
            )

    if __name__ == '__main__':
        unittest.main()


# Generated at 2022-06-14 04:04:50.272838
# Unit test for function curry
def test_curry():
    func = curry(lambda x, y, z: x + 2 * y + 3 * z)

    assert func(2, 3, 4) == 38
    assert func(2)(3)(4) == 38
    assert func(2, 3)(4) == 38
    assert func(2)(3, 4) == 38



# Generated at 2022-06-14 04:06:02.968365
# Unit test for function curried_map
def test_curried_map():
    """
    Test curried map function.
    """
    assert curried_map(lambda x: x + 1)([1, 2, 3]) == [2, 3, 4]


# Generated at 2022-06-14 04:06:09.668543
# Unit test for function curried_map
def test_curried_map():
    map_func = lambda item: item + 1
    list_to_map = [0, 1, 2, 3, 4]

    map_func_curried = curried_map(map_func)
    map_result = map_func_curried(list_to_map)
    assert map_result == [1, 2, 3, 4, 5], "curried_map should be correct"


# Generated at 2022-06-14 04:06:15.663482
# Unit test for function cond
def test_cond():
    # example without arguments
    cond_list = [
        (lambda: True, lambda: True),
        (lambda: False, lambda: False)
    ]
    assert cond(cond_list)()

    # example with arguments
    cond_list = [
        (lambda x: x > 0, lambda x: True),
        (lambda x: x < 0, lambda x: False)
    ]
    assert cond(cond_list)(1)
    assert not cond(cond_list)(-1)



# Generated at 2022-06-14 04:06:26.512837
# Unit test for function curried_map
def test_curried_map():
    list_ = [1, 2, 3]
    curried_map1 = curried_map(lambda x: x + 1)
    curried_map2 = curried_map(lambda x: x * 2)
    curried_map3 = curried_map(lambda x: x * 3)

    assert curried_map1(list_) == [2, 3, 4]
    assert curried_map2(list_) == [2, 4, 6]
    assert curried_map3(list_) == [3, 6, 9]

    curried_map4 = curried_map(lambda x: x * 4)
    assert curried_map4(curried_map4(list_)) == [16, 32, 48]

# Generated at 2022-06-14 04:06:30.656466
# Unit test for function find
def test_find():
    array = [1, 2, 3, 4, 5]
    assert find(array, lambda number: number > 4) == 5
    assert find(array, lambda number: number > 10) is None



# Generated at 2022-06-14 04:06:35.356907
# Unit test for function find
def test_find():
    collection = [1, 2, 3, 4, 5, 6]
    assert find(collection, lambda x: x > 3) == 4
    assert find(collection, lambda x: x < 0) is None
    assert find(collection, eq(5)) == 5



# Generated at 2022-06-14 04:06:44.093609
# Unit test for function find
def test_find():
    collection = [
        {'name': 'first', 'id': 0},
        {'name': 'second', 'id': 1},
        {'name': 'third', 'id': 2},
    ]
    assert find(collection, lambda item: eq(item['id'], 0))['name'] == 'first'
    assert find(collection, lambda item: eq(item['id'], 1))['name'] == 'second'
    assert find(collection, lambda item: eq(item['id'], 2))['name'] == 'third'
    assert find(collection, lambda item: eq(item['id'], 3)) is None
    assert find(collection, lambda item: eq(item['id'], -1)) is None



# Generated at 2022-06-14 04:06:54.149613
# Unit test for function cond
def test_cond():
    # Test value
    x = 2

    # Test list of condition tuples
    def is_gt_0(x): return x > 0
    def is_lt_0(x): return x < 0
    def is_eq_0(x): return x == 0

    # Test list of execute tuples
    def print_gt_0(x): print('Greater than 0')
    def print_lt_0(x): print('Less than 0')
    def print_eq_0(x): print('Equal to 0')

    # Test condition list
    condition_list = [
        (is_gt_0, print_gt_0),
        (is_lt_0, print_lt_0),
        (is_eq_0, print_eq_0),
    ]
    # Call function cond

# Generated at 2022-06-14 04:06:58.565898
# Unit test for function memoize
def test_memoize():
    @memoize
    def factorial(n: int) -> int:
        return 1 if n <= 1 else n * factorial(n - 1)

    assert factorial(5) == 120



# Generated at 2022-06-14 04:06:59.729154
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x > 2)([1, 2, 3]) == [3]

