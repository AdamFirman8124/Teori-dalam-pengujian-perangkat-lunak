

# Generated at 2022-06-14 03:58:01.741314
# Unit test for function eq
def test_eq():
    assert True == eq(1, 1)
    assert True == compose(eq(1), curry)(1)
    assert True == pipe(1, curry(eq))
    assert True == compose(eq(0), curry)(0)
    assert True == pipe(0, curry(eq))



# Generated at 2022-06-14 03:58:06.260359
# Unit test for function curry
def test_curry():
    def add(a, b, c, d, e):
        return (a + b) * c + d / e

    increment = curry(add, 5)(1, 5, 2, 4, 1)
    result_1 = increment(2) # 3 * 2 + 4 / 1
    result_2 = increment(5) # 6 * 2 + 4 / 1
    assert result_1 == 9
    assert result_2 == 9



# Generated at 2022-06-14 03:58:12.107753
# Unit test for function memoize
def test_memoize():
    def fibonacci(n):
        if n <= 2:
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)
    assert fibonacci(10) == 89
    memoized_fibonacci = memoize(fibonacci)
    assert memoized_fibonacci(10) == 89

# Generated at 2022-06-14 03:58:19.547887
# Unit test for function find
def test_find():
    """
    Find function unit test
    """
    list_ = [1, 2, 3, 4, 5]
    assert find(list_, identity) == 1
    assert find(list_, eq(10)) is None
    assert find(list_, eq(2)) == 2


# Generated at 2022-06-14 03:58:25.226757
# Unit test for function curried_filter
def test_curried_filter():
    array = [1, 2, 3, 4, 5]
    assert curried_filter(lambda a: a % 2 == 0, array) == [2, 4]
    assert curried_filter(lambda a: a > 3, array) == [4, 5]
    assert curried_filter(lambda a: a < 5, array) == [1, 2, 3, 4]



# Generated at 2022-06-14 03:58:28.717701
# Unit test for function eq
def test_eq():
    assert(eq(1, 1) == True)
    assert(eq(1, 2) == False)


# Generated at 2022-06-14 03:58:36.738790
# Unit test for function cond
def test_cond():
    """Test for function cond."""
    def is_even(x):
        return x % 2 == 0

    def is_odd(x):
        return not is_even(x)

    def square(x):
        return x * x

    def add(x):
        return x + x

    result = cond(
        [(is_even, square), (is_odd, add)],
    )

    assert result(3) == 6
    assert result(4) == 16



# Generated at 2022-06-14 03:58:38.776943
# Unit test for function find
def test_find():
    assert find([1, 2, 3], eq(1)) == 1
    assert find([1, 2, 3], eq(4)) is None


# Generated at 2022-06-14 03:58:42.073351
# Unit test for function find
def test_find():
    assert find([1, 2, 3, 4], lambda x: x + 3 == 6) == 3
    assert find([1, 2, 3, 4], lambda x: x == 6) is None
    assert find([1, 2, 3, 4], lambda x: x + 2 == 7) is None



# Generated at 2022-06-14 03:58:45.294384
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(lambda x: x + 1, [1, 2, 3]) == [2, 3, 4]

    double = curried_map(lambda x: x * 2)
    assert double([1, 2, 3]) == [2, 4, 6]



# Generated at 2022-06-14 03:58:52.032482
# Unit test for function eq
def test_eq():
    assert eq(1, 1)
    assert not eq(1, 2)



# Generated at 2022-06-14 03:58:57.963181
# Unit test for function memoize
def test_memoize():
    assert memoize(lambda x: x)(1) == 1
    assert memoize(lambda x: x)(1) == 1
    assert memoize(lambda x: x)(1) == 1
    assert memoize(lambda x: x)(2) == 2

    assert memoize(lambda x: x)(1) == 1
    assert memoize(lambda x: x)(2) == 2


# Generated at 2022-06-14 03:59:08.855866
# Unit test for function memoize
def test_memoize():
    """
    Test for function memoize

    :returns: True if all cases are passed, else False
    :rtype: Boolean
    """
    def fn_to_memoized():
        return fn_to_memoized.counter

    fn_to_memoized.counter = 0

    def increase_counter():
        fn_to_memoized.counter += 1

    memoized_fn = memoize(fn_to_memoized)
    memoized_fn_with_increase = memoize(fn_to_memoized, lambda x, y: x == y == increase_counter())

    return \
        memoized_fn(increase_counter()) == 1 and \
        memoized_fn(increase_counter()) == 2 and \
        memoized_fn(increase_counter()) == 3 and \
        memo

# Generated at 2022-06-14 03:59:12.885432
# Unit test for function eq
def test_eq():
    assert eq(1, 1) == True
    assert eq(1, 2) == False
    assert eq(1, '1') == False
    assert eq(0, '') == False
    assert eq(1, False) == False



# Generated at 2022-06-14 03:59:18.357700
# Unit test for function memoize
def test_memoize():
    def add(a):
        return a + 1

    add_memoize = memoize(add, key=eq)
    assert add_memoize(1) == 2
    assert add_memoize(1) == 2
    assert add_memoize(3) == 4
    assert add_memoize(3) == 4
    assert add_memoize(1) == 2
    assert add_memoize(2) == 3
    assert add_memoize(2) == 3



# Generated at 2022-06-14 03:59:25.205969
# Unit test for function curried_map
def test_curried_map():
    # curried_map(x => x + 1, [1, 2, 3, 4])
    assert curried_map(lambda x: x + 1, [1, 2, 3, 4]) == [2, 3, 4, 5]
    # curried_map(x => x + 1)([1, 2, 3])
    assert curried_map(lambda x: x + 1)([1, 2, 3]) == [2, 3, 4]



# Generated at 2022-06-14 03:59:27.474632
# Unit test for function eq
def test_eq():
    assert eq(1, 1)
    assert eq(1, 1) is not None
    assert eq(1, 2) is None


# Generated at 2022-06-14 03:59:30.521558
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x > 3)(range(5)) == [4]
    is_even = curried_filter(lambda x: x % 2 == 0)
    assert is_even(range(5)) == [0, 2, 4]



# Generated at 2022-06-14 03:59:37.679483
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(increase, [1, 2, 3]) == [2, 3, 4]
    assert curried_map(lambda x: x*2, [1, 2, 3]) == [2, 4, 6]
    assert curried_map(lambda x: reduce(lambda a,b: a+b, x), [[1,2],[3,4]]) == [3, 7]
    assert curried_map(lambda x: reduce(lambda a,b: a*b, x), [[1,2],[3,4]]) == [2, 12]


# Generated at 2022-06-14 03:59:45.068322
# Unit test for function cond
def test_cond():
    """
    Tests for function cond.
    """
    def is_even(num):
        return num % 2 == 0

    def is_odd(num):
        return not is_even(num)

    def add_10(num):
        return num + 10

    def add_20(num):
        return num + 20

    result = cond([
        (is_even, add_10),
        (is_odd, add_20)
    ])

    assert result(6) == 16
    assert result(7) == 27

# Generated at 2022-06-14 03:59:55.952505
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(eq(0))([0, 1, 0, 2, 0]) == [0, 0, 0]
    assert curried_filter(eq(0), [0, 1, 0, 2, 0]) == [0, 0, 0]


# Generated at 2022-06-14 04:00:09.423330
# Unit test for function cond
def test_cond():
    def positive_number(num: int) -> bool:
        return num > 0
    def zero(num: int) -> str:
        return 'zero'
    def positive_number_string(num: int) -> str:
        return 'positive number'
    def negative_number(num: int) -> str:
        return 'negative number'
    def negative_number_string(num: int) -> str:
        return 'negative number'
    cases = [
        (positive_number, positive_number_string),
        (eq(0), zero),
        (positive_number, negative_number),
    ]
    f = cond(cases)
    assert f(1) == 'positive number'
    assert f(0) == 'zero'
    assert f(-1) == 'negative number'


# Generated at 2022-06-14 04:00:17.719702
# Unit test for function eq
def test_eq():
    assert eq(1, 1) is True, 'eq 1 1 is True'
    assert eq(1, 2) is False, 'eq 1 2 is False'
    assert eq(1.0, 1) is True, 'eq 1.0 1 is True'
    assert eq(1, 1.0) is True, 'eq 1 1.0 is True'
    assert eq('1', 1) is False, 'eq "1" 1 is False'
    assert eq('a', 'a') is True, 'eq "a" "a" is True'
    assert eq('a', 'b') is False, 'eq "a" "b" is False'



# Generated at 2022-06-14 04:00:23.218494
# Unit test for function cond
def test_cond():
    is_even = lambda x: x % 2 == 0
    is_odd = lambda x: not is_even(x)
    inc = lambda x: x + 1
    double = lambda x: x * 2

    test_function = cond([
        (is_even, inc),
        (is_odd, double),
    ])

    assert test_function(8) == 9
    assert test_function(5) == 10


# Generated at 2022-06-14 04:00:29.873172
# Unit test for function find
def test_find():
    assert find([1, 2, 3, 4], eq(3)) == 3
    assert find(['a', 'b', 'c', 'd'], eq('a')) == 'a'
    assert find([1, 2, 3, 4], eq(5)) is None
    assert find([], eq(5)) is None



# Generated at 2022-06-14 04:00:32.413961
# Unit test for function find
def test_find():
    assert find([1, 2, 3], lambda x: x == 2) == 2
    assert find([], lambda x: False) is None



# Generated at 2022-06-14 04:00:34.808233
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]) == [2, 4]



# Generated at 2022-06-14 04:00:42.566811
# Unit test for function cond
def test_cond():
    list_values = range(10)
    list_values_len = len(list_values)

    def less_five(value):
        return value < 5

    def equals_five(value):
        return value == 5

    def more_five(value):
        return value > 5

    compare_list = [
        (less_five, decrease),
        (equals_five, identity),
        (more_five, increase)
    ]
    change_list = cond(compare_list)

    assert reduce(
        lambda list_len, _: list_len - 1,
        curried_map(change_list, list_values),
        list_values_len
    ) == 0

# Generated at 2022-06-14 04:00:50.407551
# Unit test for function memoize
def test_memoize():
    # Test for function memoize with add function
    def add(val1, val2): return val1 + val2
    mem_add = memoize(add)
    assert mem_add(5, 2) == 7
    assert mem_add(5, 2) == 7
    assert mem_add(5, 2) == 7
    assert mem_add(5, 3) == 8
    assert mem_add(5, 3) == 8

    # Test for function memoize with power function
    def power(val1, val2):
        result = 1
        for _ in range(val2):
            result = result * val1
        return result
    mem_power = memoize(power)
    assert mem_power(2, 3) == 8
    assert mem_power(2, 3) == 8

# Generated at 2022-06-14 04:00:55.433541
# Unit test for function cond
def test_cond():
    assert cond([(lambda x: x < 5, print)])(4) == None
    assert cond([(lambda x: x < 5, print)])(6) == None

# Generated at 2022-06-14 04:01:07.622867
# Unit test for function curried_map
def test_curried_map():
    assert (curried_map(increase)([1, 2, 3]) == [2, 3, 4])



# Generated at 2022-06-14 04:01:10.841176
# Unit test for function find
def test_find():
    """
    Test find function
    :return:
    """
    arr = [1, 2, 3, 4, 5]
    ret = find(arr, lambda x: x > 2)
    assert ret == 3


# Generated at 2022-06-14 04:01:14.840616
# Unit test for function curry
def test_curry():
    assert curry(increase)(5) == 6
    assert curry(lambda x, y, z: x + y + z)(1)(2)(3) == 6
    assert curry(lambda x, y, z: x + y + z)(1)(2, 3) == 6
    assert curry(lambda x, y, z: x + y + z)(1, 2)(3) == 6
    assert curry(lambda x, y, z: x + y + z)(1, 2, 3) == 6

# Generated at 2022-06-14 04:01:17.565135
# Unit test for function curried_filter
def test_curried_filter():
    assert [2, 4, 6] == curried_filter(lambda x: x % 2 == 0)([1, 2, 3, 4, 5, 6])



# Generated at 2022-06-14 04:01:22.087577
# Unit test for function cond
def test_cond():
    assert cond([(lambda _: True, lambda x: x * x), (lambda _: False, lambda x: x + x)]) == 25
    assert cond([(lambda _: False, lambda x: x * x), (lambda _: True, lambda x: x + x)]) == 25



# Generated at 2022-06-14 04:01:27.857062
# Unit test for function curried_map
def test_curried_map():
    collection = [1, 2, 3, 4, 5]
    assert curried_map(lambda x: x + 2)(collection) == [3, 4, 5, 6, 7]
    assert curried_map(lambda x: x * x)(collection) == [1, 4, 9, 16, 25]
    assert curried_map(lambda x: x - 3)(collection) == [-2, -1, 0, 1, 2]


# Generated at 2022-06-14 04:01:32.292380
# Unit test for function memoize
def test_memoize():
    def multiply(i):
        return i * i

    multiply = memoize(multiply)
    assert multiply(3) == 9
    assert multiply(-3) == 9
    assert multiply(3) == 9



# Generated at 2022-06-14 04:01:35.260708
# Unit test for function cond
def test_cond():
    """
    >>> result = cond([(eq(1), increase), (eq(5), identity)])
    >>> result(5)
    5
    >>> result(1)
    2
    >>> result(6)
    >>>
    """



# Generated at 2022-06-14 04:01:44.690854
# Unit test for function memoize
def test_memoize():
    def my_fn(x):
        print("Function called")
        return x * x

    my_fn_memoized = memoize(my_fn)
    assert my_fn_memoized(5) == my_fn(5) == 25
    assert my_fn_memoized(5) == my_fn(5) == 25
    assert my_fn_memoized(6) == my_fn(6) == 36
    assert my_fn_memoized(6) == my_fn(6) == 36
    assert my_fn_memoized(5) == my_fn(5) == 25
    assert my_fn_memoized.__name__ == my_fn.__name__

# Generated at 2022-06-14 04:01:50.284553
# Unit test for function memoize
def test_memoize():
    def my_fn(i):
        return i

    # empty cache
    my_memoized_fn = memoize(my_fn)
    assert my_memoized_fn(1) == 1
    assert my_memoized_fn(2) == 2
    # cache with 2 elements
    assert my_memoized_fn(1) == 1
    assert my_memoized_fn(2) == 2



# Generated at 2022-06-14 04:02:08.668254
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(increase, [1, 2, 3]) == [2, 3, 4]
    assert curried_map(lambda x: x * 2, [1, 2, 3]) == [2, 4, 6]
    assert curried_map(increase)([1, 2, 3]) == [2, 3, 4]
    assert curried_map(lambda x: x * 2)([1, 2, 3]) == [2, 4, 6]


# Generated at 2022-06-14 04:02:16.769071
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(eq(2), [1, 2, 3]) == [2]
    assert curried_filter(eq(2), [2, 3]) == [2]
    assert curried_filter(eq(2), [3]) == []
    assert curried_filter(eq(2))([1, 2, 3]) == [2]
    assert curried_filter(eq(2))([2, 3]) == [2]
    assert curried_filter(eq(2))([3]) == []
    assert curried_filter(eq(2))([]) == []



# Generated at 2022-06-14 04:02:25.268717
# Unit test for function memoize
def test_memoize():
    def fib(n):
        return fib(n-1) + fib(n-2) if n > 1 else n

    counted_fib = memoize(fib)

    assert counted_fib(12) == 144
    assert counted_fib.__closure__[0].__closure__[0].cell_contents == [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (8, 21),
        (9, 34),
        (10, 55),
        (11, 89),
        (12, 144)
    ]



# Generated at 2022-06-14 04:02:29.722515
# Unit test for function eq
def test_eq():
    assert eq(1, 1)
    assert not eq(0, 1)
    assert not eq(1, 0)
    assert not eq(None, 1)
    assert not eq(1, None)
    assert not eq(None, None)



# Generated at 2022-06-14 04:02:33.091135
# Unit test for function eq
def test_eq():
    """
    Unit test for function eq

    :returns: None
    :rtype: None
    """
    assert eq(1, 1) is True
    assert eq(1, 2) is False



# Generated at 2022-06-14 04:02:35.212812
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter((lambda value: value == 3) , [1, 2, 3, 4, 5]) == [3]


# Generated at 2022-06-14 04:02:43.858709
# Unit test for function memoize
def test_memoize():
    import unittest, sys

    class TestMemoize(unittest.TestCase):
        def test_memoize(self):
            def add1(n):
                return n + 1

            memoized_add1 = memoize(add1)

            self.assertEqual(memoized_add1(1), 2)
            self.assertEqual(memoized_add1(1), 2)  # from cache

            self.assertEqual(memoized_add1(1), 2)
            self.assertEqual(memoized_add1(2), 3)  # from cache

    unittest.main(module=sys.modules[__name__], exit=False)



# Generated at 2022-06-14 04:02:49.012953
# Unit test for function find
def test_find():
    assert find([], lambda x: x) is None
    assert find([1], lambda x: 1) == 1
    assert find([1], lambda x: 0) is None
    assert find([1, 2, 3], lambda x: x) == 1
    assert find([1, 2, 3], lambda x: x % 2 == 0) == 2
    assert find([1, 2, 3], lambda x: x % 2 == 1) == 1
    assert find([1, 2, 3], lambda x: x > 3) is None



# Generated at 2022-06-14 04:02:56.658951
# Unit test for function curried_filter
def test_curried_filter():
    """
    Unit test for function curried_filter

    :rtype: None
    """
    def not_empty(value):
        """
        Function to check if string is not empty
        """
        return value != ''

    def test_filter():
        """
        Unit test for function curried_filter

        :returns: None
        :rtype: None
        """
        assert curried_filter(not_empty, ['', 'TDD', 'TDD', '', '']) == \
               ['TDD', 'TDD']

    test_filter()



# Generated at 2022-06-14 04:03:00.522552
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(identity)([1]) == [1]
    assert curried_map(increase)([1]) == [2]
    assert curried_map(increase)([1, 2]) == [2, 3]


# Generated at 2022-06-14 04:03:16.639839
# Unit test for function memoize
def test_memoize():
    assert memoize(increase)(1) == increase(1)
    assert memoize(increase)(2) == increase(2)
    assert memoize(increase)(3) == increase(3)
    assert memoize(increase)(1) == increase(1)
    assert memoize(increase)(2) == increase(2)
    assert memoize(increase)(3) == increase(3)



# Generated at 2022-06-14 04:03:19.659814
# Unit test for function find
def test_find():
    """
    Unit test for function find.

    :returns:
    :rtype:
    """
    assert find(range(10), lambda x: x == 9) == 9



# Generated at 2022-06-14 04:03:26.689816
# Unit test for function cond
def test_cond():
    assert cond([
        (lambda x: x == 1, lambda x: x),
        (lambda x: x == 2, lambda x: x + 1),
    ])(1) == 1
    assert cond([
        (lambda x: x == 1, lambda x: x),
        (lambda x: x == 2, lambda x: x + 1),
    ])(2) == 3



# Generated at 2022-06-14 04:03:32.467605
# Unit test for function memoize
def test_memoize():
    def factorial(n):
        def factorial_fn(n, result):
            if n == 0:
                return result
            return factorial_fn(n - 1, n * result)
        return factorial_fn(n, 1)

    memoized_factorial = memoize(factorial)

    assert memoized_factorial(5) == 120
    assert memoized_factorial(6) == 720
    assert memoized_factorial(5) == 120



# Generated at 2022-06-14 04:03:39.982868
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x % 2 == 0, [1, 2, 3, 4]) == [2, 4]
    assert curried_filter(lambda x: x % 2 == 0)([1, 2, 3, 4]) == [2, 4]
    add_two = curry(lambda x, y: x + y, 2)
    multiply_two = curry(lambda x, y: x * y, 2)

    assert add_two(1) == 3
    assert multiply_two(3) == 6



# Generated at 2022-06-14 04:03:47.502367
# Unit test for function curry
def test_curry():
    def simple_function(a, b, c):
        return a + b + c

    curried_function = curry(simple_function)
    curried_function1 = curried_function(1)
    curried_function2 = curried_function1(2)
    curried_function3 = curried_function2(3)
    assert curried_function3 == 6
    assert curried_function2(4) == 7
    assert curried_function1(5, 6) == 12
    assert curried_function(7, 8, 9) == 24



# Generated at 2022-06-14 04:03:56.299728
# Unit test for function memoize
def test_memoize():
    import time

    @memoize
    def slow_function(num: int) -> int:
        time.sleep(1)
        return num

    # define a some args for test
    args = [1, 2, 3, 4]

    # time of measuring
    start = time.time()

    # call 4 times slow function with 4 different args
    for arg in args:
        slow_function(arg)
    # slow function will be invoked 4 times and one time for each arg
    # so time of performing all 4 calls is 4 times bigger than time of one call
    # but when slow function invoked more than one time with the same arg
    # it take result from cache
    # so time of performing all 4 calls is 4 times bigger than time of one call
    # but when slow function invoked more than one time with the same arg
    # it take result from

# Generated at 2022-06-14 04:04:03.331547
# Unit test for function curried_map
def test_curried_map():
    """
    Check if the curried_map works properly
    """
    assert curried_map(lambda x: x * 2)([1, 2]) == [2, 4]
    list1 = [1, 2]
    assert curried_map(lambda x: x * 2, list1) == [2, 4]
    f = curried_map(lambda x: x * 2)
    assert f(list1) == [2, 4]

# Generated at 2022-06-14 04:04:16.874793
# Unit test for function cond
def test_cond():
    def func_one(n):
        return n % 2 == 0

    def func_two(n):
        return n % 3 == 0

    def func_three(n):
        return n % 5 == 0

    def func_four(n):
        return n % 7 == 0

    def func_one_action(n):
        return "divisible by two"

    def func_two_action(n):
        return "divisible by three"

    def func_three_action(n):
        return "divisible by five"

    def func_four_action(n):
        return "divisible by seven"

    def func_not_action(n):
        return "not divisible"


# Generated at 2022-06-14 04:04:22.032870
# Unit test for function find
def test_find():
    assert find([1, 2, 3], lambda x: x % 2 == 0) == 2
    assert find([1, 2, 3], lambda x: x % 2 == 1) == 1
    assert find([1, 2, 3], lambda x: x == 4) is None



# Generated at 2022-06-14 04:04:37.576405
# Unit test for function curried_map
def test_curried_map():
    map_with_add_5 = curried_map(lambda x: x + 5)
    assert (map_with_add_5([1, 2]) == [6, 7])
    assert (map_with_add_5([2, 3]) == [7, 8])



# Generated at 2022-06-14 04:04:43.949684
# Unit test for function cond
def test_cond():
    def f1(value) -> bool:
        return value == 5

    def f2(value) -> bool:
        return value == 11

    def g1(value) -> int:
        return 5 + value

    def g2(value) -> int:
        return value * 3

    test_result = cond([(f1, g1), (f2, g2)])

    assert test_result(5) == g1(5)
    assert test_result(11) == g2(11)



# Generated at 2022-06-14 04:04:53.656016
# Unit test for function eq
def test_eq():
    assert eq(1)(1)
    assert not eq(2)(3)
    assert not eq(6)(3)
    assert not eq('1')(1)
    assert not eq('1')('a')
    assert not eq(1)('5')
    assert not eq(5, '2')
    assert not eq(1, '5')
    assert eq('1')('1')
    assert eq(5)(5)
    assert eq('5')('5')
    assert not eq(True, False)
    assert not eq(False, True)


# Unit tests for function compose

# Generated at 2022-06-14 04:04:58.781724
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x > 1)([1, 2, 3]) == [2, 3]
    assert curried_filter(lambda x: x > 1)([1, 2, 3]) == [2, 3]
    assert curried_filter(lambda x: x > 1, [1, 2, 3]) == [2, 3]



# Generated at 2022-06-14 04:05:00.870681
# Unit test for function eq
def test_eq():
    assert eq(2, 1) == False
    assert eq(2, 2) == True
    assert eq(None, None) == True


# Generated at 2022-06-14 04:05:03.845239
# Unit test for function curried_map
def test_curried_map():
    """
    Unit test for function curried_map.

    :returns: Nothing
    :rtype: Void
    """
    assert curried_map(lambda x: x + 2)([1, 2, 3]) == [3, 4, 5]



# Generated at 2022-06-14 04:05:11.806807
# Unit test for function curry
def test_curry():
    assert curry(lambda x: x)(10) == 10
    assert curry(lambda x, y: x + y)(10)(20) == curry(lambda y, x: x + y)(10)(20) == \
           curry(lambda x, y: x + y)(10, 20) == 30
    assert curry(lambda x, y, z: x + y + z)(10)(20)(30) == curry(lambda x, y, z: x + y + z)(10, 20, 30) == 60



# Generated at 2022-06-14 04:05:16.061930
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x > 2, range(5)) == [3, 4]
    assert curried_filter(lambda x: x > 2)(range(5)) == [3, 4]

# Generated at 2022-06-14 04:05:25.327147
# Unit test for function cond
def test_cond():
    is_even = lambda x: x % 2 == 0
    is_positive = lambda x: x > 0
    true = lambda x: True

    any_is_even = cond([
        (is_even, true),
        (is_positive, true),
    ])

    assert any_is_even(2)
    assert any_is_even(-1)

    any_is_positive = cond([
        (is_even, true),
        (is_positive, true),
    ])

    assert any_is_positive(2)
    assert any_is_positive(-1)


# Generated at 2022-06-14 04:05:29.235220
# Unit test for function curried_filter
def test_curried_filter():
    test_list = [1, 2, 3]
    curried_test_list = curried_filter(lambda x: x % 2 == 0, test_list)
    assert curried_test_list(test_list) == [2]



# Generated at 2022-06-14 04:05:59.385292
# Unit test for function cond
def test_cond():
    def f(value):
        return value + 1
    assert cond([
        (eq(1), lambda value: 1),
        (eq(2), lambda value: 2),
        (eq(3), lambda value: 3),
    ])(1) == 1
    assert cond([
        (eq(1), lambda value: 1),
        (eq(2), lambda value: 2),
        (eq(3), lambda value: 3),
    ])(2) == 2
    assert cond([
        (eq(1), lambda value: 1),
        (eq(2), lambda value: 2),
        (eq(3), lambda value: 3),
    ])(3) == 3

# Generated at 2022-06-14 04:06:02.304551
# Unit test for function eq
def test_eq():
    assert eq(1)(1) is True
    assert eq(1)(2) is False
    assert eq(1, 1) is True
    assert eq(1, 2) is False



# Generated at 2022-06-14 04:06:06.480171
# Unit test for function curried_map
def test_curried_map():
    curried_list_map = curried_map(lambda x: x + 1)
    assert curried_list_map([1, 2, 3, 4]) == [2, 3, 4, 5]

# Generated at 2022-06-14 04:06:12.796033
# Unit test for function curry
def test_curry():
    def add(x, y):
        return x + y
    assert curry(add)(10, 5) == 15
    assert curry(add)(10)(5) == 15
    assert curry(add, 1)(5) == 5
    assert curry(add, 2)(10, 20) == 30

    curried_add = curry(add)
    assert curried_add(10, 5) == 15
    assert curried_add(10)(5) == 15



# Generated at 2022-06-14 04:06:16.077085
# Unit test for function find
def test_find():
    assert find([1, 2, 3, 4], lambda x: x % 2 == 0) == 2, 'First even number'
    assert find([1, 5, 3, 7], lambda x: x % 2 == 0) is None, 'No even number'



# Generated at 2022-06-14 04:06:22.487730
# Unit test for function find
def test_find():
    """
    Unit test for function find
    """
    assert find([], lambda i: False) is None
    assert find([1], lambda i: True) == 1
    assert find([1, 2, 3], lambda i: True) == 1
    assert find([1, 2, 3], lambda i: i == 2) == 2
    assert find([1, 2, 3], lambda i: False) is None



# Generated at 2022-06-14 04:06:29.413102
# Unit test for function curried_filter
def test_curried_filter():
    def test_filter_function(value):
        if value > 2:
            return True
        return False

    def test_map_function(value):
        return value*2

    collection = [1, 2, 3, 4, 5]
    result_filter = [3, 4, 5]
    result_map = [6, 8, 10]
    filter_function = curried_filter(test_filter_function)
    map_function = curried_map(test_map_function)

    assert filter_function(collection) == result_filter

    assert map_function(collection) == result_map

    assert curried_filter(test_filter_function, collection) == result_filter

    assert curried_map(test_map_function, collection) == result_map


# Generated at 2022-06-14 04:06:32.748303
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x % 2 == 0)([1, 2, 3, 4]) == [2, 4]
'''
run pytest to run Unit test
'''

# Generated at 2022-06-14 04:06:39.412400
# Unit test for function find
def test_find():
    assert find(['a', 'b', 'c', 'd'], lambda x: x == 'c') == 'c'
    assert find([{'a': 1}, {'b': 2}], lambda x: x['b'] == 2) == {'b': 2}
    assert find([{'a': 1}, {'b': 2}], lambda x: x['b'] == 3) is None



# Generated at 2022-06-14 04:06:45.229950
# Unit test for function curry
def test_curry():
    something = lambda x, y, z: x + y + z
    curried_something = curry(something, 3)
    assert curried_something(1)(2, 3) == 6
    assert curried_something(1)(2)(3) == 6
    assert curried_something(1, 2)(3) == 6
    assert curried_something(1, 2, 3) == 6



# Generated at 2022-06-14 04:07:33.117999
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(None, []) == []
    assert curried_map(increase, [1, 2, 3]) == [2, 3, 4]



# Generated at 2022-06-14 04:07:36.966857
# Unit test for function find
def test_find():
    collection = [1, 2, 3, 4]
    assert find(collection, eq(1)) == 1
    assert find(collection, eq(8)) is None


# Generated at 2022-06-14 04:07:42.948997
# Unit test for function curry
def test_curry():
    def multiply(a, b, c):
        return a * b * c

    curried_multiply = curry(multiply)
    result = curried_multiply(2)(3)(4)
    assert result == 24

    mult = curry(multiply)(2)(3)
    assert mult(4) == 24
    assert mult(5) == 30
    assert mult(6) == 36



# Generated at 2022-06-14 04:07:49.862361
# Unit test for function eq
def test_eq():
    assert eq(1, 1) == True
    assert eq(1, 2) == False
    assert eq("a", "a") == True
    assert eq("a", "b") == False
    assert eq(True, True) == True
    assert eq(True, False) == False
    assert eq([], []) == True
    assert eq([], [1]) == False
    assert eq([1], [1]) == True
    assert eq([1], [2]) == False
    assert eq(1, 1) == True
    assert eq(1, 2) == False
    assert eq(1, 1 ) == True
    assert eq(1, 2) == False
    assert eq((), ()) == True
    assert eq((), (1,)) == False
    assert eq((1,), (1,)) == True

# Generated at 2022-06-14 04:07:51.709207
# Unit test for function eq
def test_eq():
    assert eq(1, 1)
    assert not eq(2, 3)

