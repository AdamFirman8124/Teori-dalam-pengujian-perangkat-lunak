

# Generated at 2022-06-14 03:57:59.607455
# Unit test for function memoize
def test_memoize():
    # empty function
    def always_return_1():
        return 1

    # function with argument
    @memoize
    def fn(argument):
        return argument

    # test
    assert fn(1) == 1
    assert fn(1) == 1
    assert fn("x") == "x"
    assert fn("x") == "x"
    assert fn("A") == "A"
    assert fn("B") == "B"
    assert fn("W") == "W"
    assert fn("W") == "W"
    assert fn("x") == "x"
    assert fn("B") == "B"



# Generated at 2022-06-14 03:58:03.965832
# Unit test for function eq
def test_eq():
    assert eq(1, 1)
    assert not eq(1, 2)
    assert eq(1)(1)
    assert not eq(1)(2)
    assert eq(1, 1)()
    assert not eq(1, 2)()



# Generated at 2022-06-14 03:58:06.419329
# Unit test for function eq
def test_eq():
    assert eq(2)(2) and not eq(2)(3)
    assert eq(3, 3) and not eq(3, 4)
    assert not eq(4, 5)



# Generated at 2022-06-14 03:58:09.097539
# Unit test for function curried_filter
def test_curried_filter():
    result = curried_filter(lambda x: x % 2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    assert result == [1, 3, 5, 7, 9]



# Generated at 2022-06-14 03:58:10.588781
# Unit test for function eq
def test_eq():
    assert eq(2, 2) is True, 'eq is not working'



# Generated at 2022-06-14 03:58:13.747018
# Unit test for function find
def test_find():
    assert find([1, 2, 3], lambda x: x == 2) == 2
    assert find([1, 2, 3], lambda x: x < 2) == 1
    assert find([] + [1, 2, 3], lambda x: x == 5) is None



# Generated at 2022-06-14 03:58:15.739397
# Unit test for function memoize
def test_memoize():
    @memoize
    def factorial(n):
        if n < 0:
            raise ValueError
        if n == 0:
            return 1
        return n * factorial(n - 1)

    assert factorial(5) == 120
    assert factorial(6) == 720



# Generated at 2022-06-14 03:58:18.838495
# Unit test for function find
def test_find():
    assert find([1, 2, 3], lambda x: x > 2) == 3
    assert find([1, 2, 3], lambda x: x > 4) is None



# Generated at 2022-06-14 03:58:27.435583
# Unit test for function cond
def test_cond():
    """
    Testing function cond
    """
    c = cond([(lambda x: x > 0, compose(lambda x: x + 1, lambda x: x * 2)),
              (lambda x: x == 0, compose(lambda x: x + 1, lambda x: x * 2)),
              (lambda x: x < 0, compose(lambda y: y * 42, lambda z: z + 1))])
    assert c(10) == 21
    assert c(0) == 1
    assert c(-10) == 42
    assert c(-10) == 42


# Unit tests for function memoize

# Generated at 2022-06-14 03:58:31.251544
# Unit test for function curried_map
def test_curried_map():
    data = [1, 2, 3]
    curried_map_inc = curried_map(increase)
    assert data == currie

# Generated at 2022-06-14 03:58:38.156276
# Unit test for function eq
def test_eq():
    assert eq(3, 3) == True
    assert eq(3, "3") == False


# Generated at 2022-06-14 03:58:39.729927
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(lambda item: item + 5, [1, 2, 3]) == [6, 7, 8]

# Generated at 2022-06-14 03:58:43.768025
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(eq(1), [1, 2, 3]) == [1]
    assert curried_filter(eq(0), [1, 2, 3]) == []
    assert curried_filter(eq(1), [])([1, 2, 3]) == [1]


# Generated at 2022-06-14 03:58:46.318807
# Unit test for function curried_filter
def test_curried_filter():
    curried_filter_ = curried_filter(lambda x: x % 2)
    collection = [1, 2, 3, 4, 5, 6]
    assert curried_filter_(collection) == [1, 3, 5]



# Generated at 2022-06-14 03:58:54.463131
# Unit test for function curried_filter
def test_curried_filter():
    """
    Unit test for function curried_filter.
    """
    assert curried_filter(eq(2), [0, 1, 2, 3])(None) == [2]
    assert curried_filter(eq(2), [0, 1, 3])(None) == []
    assert curried_filter(eq(2), [])(None) == []
    assert curried_filter(eq(2), [2])(None) == [2]



# Generated at 2022-06-14 03:58:58.536570
# Unit test for function find
def test_find():
    array = [{d: True} for d in range(10)]
    assert find(array, lambda x: x[5] is None) is None
    assert find(array, lambda x: x[3] is True) is array[3]


# Generated at 2022-06-14 03:59:00.846665
# Unit test for function curried_filter
def test_curried_filter():
    assert(curried_filter([1, 2, 3, 4])(lambda x: x % 2 == 0) == [2, 4])

# Generated at 2022-06-14 03:59:02.399048
# Unit test for function eq
def test_eq():
    assert eq(1, 1)



# Generated at 2022-06-14 03:59:06.148404
# Unit test for function curried_map
def test_curried_map():
    assert curried_map() == None
    assert curried_map(lambda x: x + 1) == None
    assert curried_map(lambda x: x + 1, [1, 2, 3]) == [2, 3, 4]


# Generated at 2022-06-14 03:59:10.333067
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(increase)([1, 2, 3]) == [2, 3, 4]
    assert curried_map(lambda x: x + 1, [1, 2, 3]) == [2, 3, 4]



# Generated at 2022-06-14 03:59:26.261052
# Unit test for function cond
def test_cond():
    def to_upper(string: str) -> str:
        return string.upper()

    def to_lower(string: str) -> str:
        return string.lower()

    def is_lower(string: str) -> bool:
        return string.islower()

    def is_upper(string: str) -> bool:
        return string.isupper()

    to_case = cond([
        (is_upper, to_lower),
        (is_lower, to_upper)
    ])

    assert to_case('AbC') == 'abc'
    assert to_case('abc') == 'ABC'
    assert to_case('ABC') == 'abc'
    assert to_case('aBc') == 'ABC'



# Generated at 2022-06-14 03:59:29.558963
# Unit test for function find
def test_find():
    assert find([1, 2, 3, 4], lambda x: x > 4) is None
    assert find([1, 2, 3, 4], lambda x: x > 1) == 2
    assert find([1, 2, 3, 4], lambda x: x > 2) == 3



# Generated at 2022-06-14 03:59:33.373445
# Unit test for function curry
def test_curry():
    assert curry(identity)(1) == 1
    assert curry(identity, 2)(1, 2) == (1, 2)
    assert curry(identity, 2)(1)(2) == (1, 2)

    assert curry(increase)(1) == 2
    assert curry(increase, 2)(1, 2) == 3
    assert curry(increase, 2)(1)(2) == 3


# Generated at 2022-06-14 03:59:39.999727
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x > 5, [1, 2, 3, 4, 5, 6, 7]) == [6, 7]
    assert curried_filter(lambda x: x > 1, [1, 2, 3, 4, 5, 6, 7])([1, 2, 3, 4, 5, 6, 7]) == [2, 3, 4, 5, 6, 7]



# Generated at 2022-06-14 03:59:41.873560
# Unit test for function eq
def test_eq():
    eq_ = eq(1)

    assert eq_(1) == True
    assert eq_(2) == False



# Generated at 2022-06-14 03:59:45.435994
# Unit test for function memoize
def test_memoize():
    @memoize
    def fibonacci(n):
        if n <= 1:
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)
    assert fibonacci(10) == 89


# Generated at 2022-06-14 03:59:55.412252
# Unit test for function curry
def test_curry():
    # to run test in PyCharm use:
    # https://www.jetbrains.com/help/pycharm/2018.3/testing-your-first-python-application.html
    # to run test in command line use:
    # pytest -s -v functions.py

    # create curried multiply function
    curried_multiply = curry(lambda x, y, z: x * y * z)
    assert curried_multiply(2, 3, 4) == 24
    assert curried_multiply(2, 3)(4) == 24
    assert curried_multiply(2)(3, 4) == 24
    assert curried_multiply(2)(3)(4) == 24

    # create curried filter function

# Generated at 2022-06-14 04:00:04.717991
# Unit test for function cond
def test_cond():
    assert cond([(eq(1), identity)])(1) == 1
    assert cond([(eq(1), identity), (eq(2), increase)])(2) == 3
    assert cond([(eq(1), increase), (eq(2), identity)])(2) == 2
    assert cond([(eq('1'), increase), (eq('2'), identity)])('2') == '2'
    assert cond([(eq('1'), increase), (eq('2'), identity)])('1') == 2
    assert cond([(eq('1'), 'str'), (eq('2'), identity)])('2') == '2'
    assert cond([(eq('1'), 'str'), (eq('2'), identity)])('1') == 'str'
    assert cond([(eq('1'), 'str'), (eq('2'), 'str2')])('2')

# Generated at 2022-06-14 04:00:07.835580
# Unit test for function curried_filter
def test_curried_filter():
    collection = [0, 1, 2, 3]

    gt_2 = curried_filter(lambda x: x > 2)
    eq_0 = curried_filter(lambda x: x == 0)

    assert gt_2(collection) == [3]
    assert eq_0(collection) == [0]


# Generated at 2022-06-14 04:00:10.704877
# Unit test for function eq
def test_eq():
    assert eq(1, 2) == False
    assert eq(1, 1) == True
    assert eq(1)(2) == False
    assert eq(1)(1) == True


# Generated at 2022-06-14 04:00:21.971318
# Unit test for function memoize
def test_memoize():

    def long_calculation(string, n):
        time.sleep(3)
        return (string + "_" + str(n))

    long_calculation_memoized = memoize(long_calculation)

    assert long_calculation_memoized("test", 1) == "test_1"
    assert long_calculation_memoized("test", 1) == "test_1"



# Generated at 2022-06-14 04:00:24.207697
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(lambda x: x + 1)([1, 2, 3]) == [2, 3, 4]
    assert curried_map(lambda x: x + 1, [1, 2, 3]) == [2, 3, 4]


# Generated at 2022-06-14 04:00:30.214751
# Unit test for function curried_filter
def test_curried_filter():
    # values for test
    collection = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
    condition = lambda item: item[0] == 1
    expected = [[1, 1, 1]]

    # actual result
    actual = curried_filter(condition)(collection)

    assert eq(expected, actual)


# Generated at 2022-06-14 04:00:32.906556
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(lambda x: x + 1, [1, 2, 3]) == [2, 3, 4]



# Generated at 2022-06-14 04:00:38.525003
# Unit test for function memoize
def test_memoize():
    def fn(x):
        time.sleep(1)
        return x**2


    print(time.time())

    memoized_fn = memoize(fn)
    print(memoized_fn(2))
    print(memoized_fn(2))
    print(memoized_fn(3))

    print(time.time())


# Generated at 2022-06-14 04:00:47.629778
# Unit test for function curried_filter
def test_curried_filter():
    """
    Test curried filter
    """
    collection = [1, 2, 3, 4, 5, 6]
    # filter_greater_three = curried_filter(lambda x: x>3)
    filter_greater_three = curried_filter(lambda x: x > 3)
    assert filter_greater_three(collection) == [4, 5, 6]
    # memoized_filter_greater_three = memoize(filter_greater_three)
    # assert memoized_filter_greater_three(collection) == [4, 5, 6]


# Generated at 2022-06-14 04:00:50.820367
# Unit test for function find
def test_find():
    assert find([1, 2, 3, 3, 4], eq(3)) == 3
    assert find([1, 2, 3, 3, 4], eq(5)) is None

# Generated at 2022-06-14 04:01:01.514061
# Unit test for function cond
def test_cond():
    assert cond([
        (eq(False), identity),
        (eq(True), increase),
        (eq(False), identity),
        (eq(True), increase),
    ])(False) == False

    assert cond([
        (eq(False), identity),
        (eq(True), increase),
        (eq(False), identity),
        (eq(True), increase),
    ])(True) == 2

    assert cond([
        (eq(False), (lambda: 1)),
        (eq(True), (lambda: 2)),
        (eq(False), (lambda: 3)),
        (eq(True), (lambda: 4)),
    ])() == 2


# Generated at 2022-06-14 04:01:11.950702
# Unit test for function memoize
def test_memoize():
    def fibWrapper(n):
        """
        Fibonacci sequence.

        :param n: position in the fibonacci sequence
        :type n: Int
        :returns: result
        :rtype: Int
        """
        def fib(n):
            if n < 2:
                return n
            return fib(n-1) + fib(n-2)
        # memoize function with key equals to first argument
        return memoize(fib, eq)(n)

    assert fibWrapper(0) == 0
    assert fibWrapper(1) == 1
    assert fibWrapper(2) == 1
    assert fibWrapper(5) == 5
    assert fibWrapper(10) == 55
    assert fibWrapper(20) == 6765
    assert fibWrapper(30) == 832040

# Generated at 2022-06-14 04:01:13.181409
# Unit test for function curry
def test_curry():
    f = curry(lambda x, y: x + y)(3)(4)
    assert f == 7


# Generated at 2022-06-14 04:01:25.063935
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(lambda x: x + 1)( [1, 2, 3] ) == [2, 3, 4]


# Generated at 2022-06-14 04:01:28.833974
# Unit test for function curry
def test_curry():
    @curry
    def sum(a, b, c):
        return a + b + c

    assert sum(1)(2)(3) == 6
    assert sum(1)(2, 3) == 6
    assert sum(1, 2, 3) == 6



# Generated at 2022-06-14 04:01:33.542926
# Unit test for function cond
def test_cond():
    condition = [
        (lambda x: x == 0, lambda x: x + 1),
        (lambda x: x < 0, lambda x: x + 1),
        (lambda x: x < 10, lambda x: x + 10)
    ]
    result = cond(condition)
    assert result(0) == 1
    assert result(-1) == 0
    assert result(9) == 19


if __name__ == "__main__":
    test_cond()

# Generated at 2022-06-14 04:01:36.658526
# Unit test for function memoize
def test_memoize():
    f = memoize(lambda x: x * x)
    assert f(1) == 1
    assert f(2) == 4
    assert f(1) == 1
    assert f(2) == 4
    assert f(4) == 16
    assert f(8) == 64



# Generated at 2022-06-14 04:01:39.878926
# Unit test for function memoize
def test_memoize():
    @memoize
    def expensive_calculation(i: int, j: int) -> int:
        return i + j

    assert expensive_calculation(1, 2) == 3
    assert expensive_calculation(1, 2) == 3



# Generated at 2022-06-14 04:01:42.473614
# Unit test for function curry
def test_curry():
    add = curry(lambda a, b, c: a + b + c)
    assert callable(add)
    assert add(1)(2)(3) == 6



# Generated at 2022-06-14 04:01:48.839481
# Unit test for function curry
def test_curry():  # TODO: fix
    def sum(a, b):
        return a + b

    curried_sum = curry(sum)

    assert curried_sum(1)(2) == 3
    assert curried_sum(1, 2) == 3
    assert curried_sum(1, 2, 3) == 3



# Generated at 2022-06-14 04:01:55.300932
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(increase, [0, 1, 2, 3, 4]) == [1, 2, 3, 4, 5]
    assert curried_map(increase)([0, 1, 2, 3, 4]) == [1, 2, 3, 4, 5]
    assert curried_map(increase, [])([0, 1, 2, 3, 4]) == [1, 2, 3, 4, 5]
    assert curried_map(increase)([0, 1, 2, 3, 4])([0, 1, 2, 3, 4]) == [1, 2, 3, 4, 5]



# Generated at 2022-06-14 04:02:05.495101
# Unit test for function eq
def test_eq():
    f = eq
    assert f(2, 3) == False
    assert f(2, 2) == True
    assert f(2, None) == False
    assert f(None, None) == True
    assert f('a', None) == False
    assert f('a', 'a') == True
    assert f('b', 'a') == False
    assert f([1], [1]) == False
    assert f([1], [1, 2]) == False
    assert f([1, 2], [1, 2]) == True
    assert f([1, 2], [1, 3]) == False
    assert f(None, [1, 2]) == False
    assert f([1, 2], None) == False

# Generated at 2022-06-14 04:02:10.526898
# Unit test for function find
def test_find():
    assert find([1, 2, 3, 4, 5], eq(2)) == 2
    assert find([1, 2, 3, 4, 5], eq(6)) is None



# Generated at 2022-06-14 04:02:40.047776
# Unit test for function curried_filter
def test_curried_filter():
    test_array = [1, 2, 3, 4, 5]
    assert [1, 2, 3] == curried_filter(lambda x: x <= 3, test_array)
    assert [2, 3] == curried_filter(lambda x: x != 1, test_array)
    assert [2] == curried_filter(lambda x: x == 2, test_array)
    assert [1, 2, 3] == curried_filter(eq(True), curried_map(lambda x: x < 4, test_array))
    assert [4, 5] == curried_filter(lambda x: not (eq(True)(x < 4)), test_array)



# Generated at 2022-06-14 04:02:42.114603
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(increase, [1, 2, 3, 4]) == [2, 3, 4, 5]



# Generated at 2022-06-14 04:02:45.394422
# Unit test for function find
def test_find():
    assert find([1, 2, 3], lambda x: x == 2) == 2
    assert find([1, 2, 3], lambda x: x == 3) == 3
    assert find([1, 2, 3], lambda x: x == 4) is None



# Generated at 2022-06-14 04:02:56.218986
# Unit test for function cond
def test_cond():
    """Test case for function cond."""
    assert cond([(lambda x: x > 0, lambda x: "more than zero"),
                 (lambda x: x < 0, lambda x: "less than zero"),
                 (lambda _: True, lambda x: "is zero")])(0) == "is zero"
    assert cond([(lambda x: x > 0, lambda x: "more than zero"),
                 (lambda x: x < 0, lambda x: "less than zero"),
                 (lambda _: True, lambda x: "is zero")])(10) == "more than zero"

# Generated at 2022-06-14 04:02:58.101700
# Unit test for function eq
def test_eq():
    assert eq(1)(1)
    assert not eq(1)(2)


# Generated at 2022-06-14 04:03:00.869930
# Unit test for function memoize
def test_memoize():
    assert memoize(lambda x: x + 1)(1) == 2
    assert memoize(lambda x: x + 1)(1) == 2


# Generated at 2022-06-14 04:03:07.587408
# Unit test for function cond
def test_cond():
    fs = [
        lambda x: x % 2 == 0,
        lambda x: x ** x,
        lambda x: x * x,
    ]
    fn = cond(
        [
            (fs[0], fs[1]),
            (fs[0], fs[2]),
        ]
    )
    assert fn(4) == 256, "4 ** 4"
    assert fn(3) == 9, "3 * 3"



# Generated at 2022-06-14 04:03:11.991552
# Unit test for function curried_map
def test_curried_map():
    assert(curried_map(identity)([1, 2, 3]) == [1, 2, 3])
    assert(curried_map(increase)([1, 2, 3]) == [2, 3, 4])


# Generated at 2022-06-14 04:03:21.130771
# Unit test for function memoize
def test_memoize():
    def pow2(number):
        print(f'Computing for: {number}')
        return number ** 2

    def times_3(number):
        print(f'Computing for: {number}')
        return number * 3

    memoized_pow2 = memoize(pow2)
    memoized_times_3 = memoize(times_3)

    assert memoized_pow2(10) == 100
    assert memoized_pow2(10) == 100
    assert memoized_times_3(10) == 30
    assert memoized_times_3(10) == 30

    memoized_pow2 = memoize(pow2, key=eq)
    memoized_times_3 = memoize(times_3)

    assert memoized_pow2(10) == 100
    assert memoized

# Generated at 2022-06-14 04:03:23.972474
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(increase)([1, 2, 3]) == [2, 3, 4]



# Generated at 2022-06-14 04:03:45.403149
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x % 2 == 0)([1, 2, 3, 4]) == [2, 4]


# Generated at 2022-06-14 04:03:48.314085
# Unit test for function curried_filter
def test_curried_filter():
    filter_function = curried_filter(lambda x: x > 0)
    assert filter_function([1, 2, 3, -1, -2]) == [1, 2, 3]


# Generated at 2022-06-14 04:03:56.799270
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(increase)([1, 2, 3]) == [2, 3, 4]
    assert curried_map(increase, [1, 2, 3]) == [2, 3, 4]
    assert curried_map(increase, curried_map(increase, [1, 2, 3])) == [3, 4, 5]
    assert [increase(item) for item in [1, 2, 3]] == curried_map(increase)([1, 2, 3])
    assert [increase(item) for item in [1, 2, 3]] == curried_map(increase, [1, 2, 3])

# Generated at 2022-06-14 04:04:03.197044
# Unit test for function memoize
def test_memoize():
    import unittest
    import datetime

    now = datetime.datetime.now

    class MemoizeTest(unittest.TestCase):
        def test_memoize(self):
            double = lambda x: x * 2

            memoized = memoize(double)
            self.assertEqual(memoized(1), 2)
            self.assertEqual(memoized(1), 2)

            stopwatch = lambda: now()
            memoized_stopwatch = memoize(stopwatch)
            time1 = memoized_stopwatch()

            for number in range(0, 100):
                _ = memoized_stopwatch()

            time2 = memoized_stopwatch()
            self.assertEqual(time1, time2)

    unittest.main()



# Generated at 2022-06-14 04:04:13.487972
# Unit test for function curried_map
def test_curried_map():
    def mapper1(value):
        return value + 1

    def mapper2(value):
        return value + 2

    collection1 = [1, 2, 3, 4]
    collection2 = [1, 2, 3, 4]
    collection3 = [2, 3, 4, 5]
    curried_mapper1 = curried_map(mapper1)
    curried_mapper2 = curried_map(mapper2)
    assert curried_mapper1(collection1) == collection3
    assert curried_mapper2(collection2) == collection3



# Generated at 2022-06-14 04:04:16.881357
# Unit test for function find
def test_find():
    assert find([1, 2, 3, 4], lambda x: x < 2) == 1
    assert find([1, 2, 3, 4], lambda x: x < 1) == None



# Generated at 2022-06-14 04:04:23.057696
# Unit test for function cond
def test_cond():
    assert cond([
        (lambda value: value == 2, lambda: 2),
        (lambda value: value == '2', lambda: 'two')
    ])(2) is 2
    assert cond([
        (lambda value: value == 2, lambda: 2),
        (lambda value: value == '2', lambda: 'two')
    ])('2') is 'two'
    assert cond([
        (lambda value: value == 2, lambda: 2),
        (lambda value: value == '2', lambda: 'two')
    ])(3) is None



# Generated at 2022-06-14 04:04:37.064125
# Unit test for function cond
def test_cond():
    def condition_1(value):
        return value == 'a'

    def condition_2(value):
        return value == 'b'

    def execute_1(value):
        return '1-{}'.format(value)

    def execute_2(value):
        return '2-{}'.format(value)

    def execute_3(value):
        return '3-{}'.format(value)

    fn = cond([
        (condition_1, execute_1),
        (condition_2, execute_2),
    ],)
    assert fn('a') == '1-a'
    assert fn('b') == '2-b'
    assert fn('c') is None


# Generated at 2022-06-14 04:04:42.755732
# Unit test for function cond
def test_cond():
    cond1 = cond([(lambda x: x > 0, lambda x: x + 1),])
    cond2 = cond([(lambda x: x > 0, lambda x: x + 1),
                  (lambda x: x == 0, lambda x: x + 1)])
    assert cond1(1) == 2
    assert cond2(0) == 1
    assert cond2(-1) is None
    assert cond2(1) == 2
    assert cond1(0) is None



# Generated at 2022-06-14 04:04:49.755230
# Unit test for function cond
def test_cond():
    """
    Test case for function cond.

    :param None
    :returns: None
    :rtype: None
    """
    assert cond([
        (lambda value: value == 1, lambda value: '123'),
        (lambda value: value == 2, lambda value: '456'),
        (lambda value: value == 3, lambda value: '789'),
        (lambda value: value == 4, lambda value: '000'),
    ])(2) == '456'



# Generated at 2022-06-14 04:05:31.035681
# Unit test for function eq
def test_eq():
    assert eq(1, 1)
    assert not eq(1, 2)



# Generated at 2022-06-14 04:05:34.164090
# Unit test for function find
def test_find():
    assert find([1, 2, 3, 4], eq(2)) == 2
    assert find([], eq(2)) is None



# Generated at 2022-06-14 04:05:41.805925
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(lambda x: x * x)([1, 2, 3]) == [1, 4, 9]
    assert curried_map(lambda x: x * x)([1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25]
    assert curried_map(lambda x: x * x)([9, 8, 7]) == [81, 64, 49]
    increment = curried_map(lambda x: x + 1)
    assert increment([1, 2, 3]) == [2, 3, 4]
    assert increment([1, 2, 3, 4, 5]) == [2, 3, 4, 5, 6]
    assert increment([9, 8, 7]) == [10, 9, 8]



# Generated at 2022-06-14 04:05:45.428050
# Unit test for function curried_map
def test_curried_map():
    assert [identity(1), identity(2), identity(3)] == curried_map(
        identity,
        [1, 2, 3]
    )



# Generated at 2022-06-14 04:05:51.594588
# Unit test for function curried_filter
def test_curried_filter():
    is_multiple_of_3 = lambda item: item % 3 == 0
    collection = [1, 2, 3, 4, 5, 6, 7]
    curried_function = curried_filter(is_multiple_of_3)
    result = curried_function(collection)
    assert result == [3, 6]



# Generated at 2022-06-14 04:06:02.381876
# Unit test for function cond
def test_cond():
    is_empty = lambda value: len(value) == 0
    first_argument = lambda *args: args[0]

    is_empty_list = lambda *args: first_argument(*args) == []
    is_list = lambda *args: isinstance(first_argument(*args), list)
    is_tuple = lambda *args: isinstance(first_argument(*args), tuple)
    is_dictionary = lambda *args: isinstance(first_argument(*args), dict)
    is_string = lambda *args: isinstance(first_argument(*args), str)

    is_none = lambda value: value is None
    is_undefined = lambda value: value is None


# Generated at 2022-06-14 04:06:05.278714
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(identity)([1, 2, 3]) == [1, 2, 3]



# Generated at 2022-06-14 04:06:15.304565
# Unit test for function memoize
def test_memoize():
    """
    Unit test for memoize.

    :returns: True if test result is success, False is test failure
    :rtype: Boolean
    """
    global test_counter
    test_counter = 0

    def counter_fn(increase_number):
        global test_counter
        test_counter += increase_number

    counter_fn(1)
    result = test_counter  # result should be 1
    counter_fn(1)
    result += test_counter  # result should be 3
    counter_fn(1)
    result += test_counter  # result should be 6

    assert result == 6, "Test failed"

    test_counter = 0

    counter_memoized_fn = memoize(counter_fn)
    counter_memoized_fn(1)
    result = test_counter  # result should be

# Generated at 2022-06-14 04:06:18.805108
# Unit test for function eq
def test_eq():
    assert(eq(1, 1) == True)
    assert(eq(1, 2) == False)
    assert(eq(curried_eq(1), 1) == True)



# Generated at 2022-06-14 04:06:20.903592
# Unit test for function eq
def test_eq():
    assert eq(2, 2) == True
    assert eq('a', 'b') == False



# Generated at 2022-06-14 04:08:00.097392
# Unit test for function cond
def test_cond():
    assert cond([
        (lambda x: x % 2 == 0, lambda x: 'even'),
        (lambda x: x % 2 == 1, lambda x: 'odd'),
        (lambda x: x % 3 != 0, lambda x: 'not multiple of 3'),
        (lambda x: True, lambda x: 'multiple of 3')
    ])(3) == 'odd'
    assert cond([
        (lambda x: x % 2 == 0, lambda x: 'even'),
        (lambda x: x % 2 == 1, lambda x: 'odd')
    ])(3) == 'odd'