

# Generated at 2022-06-14 03:57:55.588388
# Unit test for function curried_map
def test_curried_map():
    mapped = curried_map(lambda x: x * 2)([1, 2, 3, 4])
    assert [2, 4, 6, 8] == mapped
# End unit test for function curried_map


# Generated at 2022-06-14 03:57:57.981655
# Unit test for function find
def test_find():
    list_for_find = [1, 2, 3]
    assert find(list_for_find, lambda x: x == 1) == 1
    assert find(list_for_find, lambda x: x == 55) is None

# Generated at 2022-06-14 03:58:02.734452
# Unit test for function eq
def test_eq():
    eq_1 = eq(1)
    eq_2 = eq(2)

    assert eq_1(1)
    assert not eq_1(2)
    assert eq_2(2)
    assert not eq_2(1)
    assert not eq_1(0)



# Generated at 2022-06-14 03:58:06.152723
# Unit test for function memoize
def test_memoize():
    test_fn = memoize(function=lambda value: value * 2)
    assert test_fn(2) == 4
    assert test_fn(2) == 4
    assert test_fn(2) == 4
    assert test_fn(2) == 4



# Generated at 2022-06-14 03:58:14.556946
# Unit test for function curried_map
def test_curried_map():
    curried_map_result_1 = curried_map(increase)([1, 2, 3])
    curried_map_result_2 = curried_map(increase, [1, 2, 3])
    curried_map_result_3 = curried_map(increase, [1, 2, 3])

    assert curried_map_result_1 == [2, 3, 4]
    assert curried_map_result_2 == [2, 3, 4]
    assert curried_map_result_3 == [2, 3, 4]



# Generated at 2022-06-14 03:58:18.180906
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda item: item < 5)([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4]



# Generated at 2022-06-14 03:58:30.903257
# Unit test for function memoize
def test_memoize():
    """
    Unit test for function memoize
    """
    def no_side_effect(argument):
        "Mock function"
        print('no_side_effect', argument)
        return argument

    no_side_effect_memoize = memoize(no_side_effect)
    no_side_effect_memoize('test')
    no_side_effect_memoize('test')

    def side_effect(argument):
        "Mock function"
        print('side_effect', argument)
        return argument

    side_effect_memoize = memoize(side_effect)
    side_effect_memoize('test')
    side_effect_memoize('test')

    def equal(value, value1):
        "Mock equality function"
        print(value, value1)

# Generated at 2022-06-14 03:58:37.211059
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x % 2 == 0)(list(range(1, 10))) == [2, 4, 6, 8]



# Generated at 2022-06-14 03:58:40.459079
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(identity)([1, 2, 3]) == [1, 2, 3]
    assert curried_map(increase)([1, 2, 3]) == [2, 3, 4]


# Generated at 2022-06-14 03:58:43.650283
# Unit test for function find
def test_find():
    collection = [1, 2, 3, 4, 5]
    assert find(collection, eq(1)) == 1
    assert find(collection, eq(3)) == 3
    assert find(collection, eq(10)) is None



# Generated at 2022-06-14 03:58:59.870582
# Unit test for function curry
def test_curry():
    assert curry(lambda x, y: x + y)(1)(2) == 3
    assert curry(lambda x, y, z: x + y + z)(1)(2)(3) == 6
    assert curry(lambda x, y, z=1: x + y + z)(7)(3) == 11
    assert curry(lambda x, y, z=1: x + y + z)(7)(3, 1) == 11



# Generated at 2022-06-14 03:59:05.623025
# Unit test for function cond
def test_cond():
    assert cond([
        (lambda x: x == 'happy', identity),
        (lambda x: True, lambda x: ':(')
    ])('happy') == 'happy'
    assert cond([
        (lambda x: x == 'happy', identity),
        (lambda x: True, lambda x: ':(')
    ])(False) == ':('


# Generated at 2022-06-14 03:59:15.061443
# Unit test for function memoize
def test_memoize():
    print(memoize(increase, identity)(5) == memoize(increase, identity)(5))  # True
    print(memoize(increase, identity)(5) == memoize(increase, identity)(6))  # False
    print(memoize(increase, identity)(5) == memoize(increase, identity)(5))  # True
    print(memoize(increase, identity)(6) == memoize(increase, identity)(6))  # True
    print(memoize(increase, identity)(5) == memoize(increase, identity)(5))  # True



# Generated at 2022-06-14 03:59:19.312802
# Unit test for function find
def test_find():
    assert(find([1, 2, 3], lambda item: item == 2) == 2)
    assert(find([1, 2, 3], lambda item: item == 0) == None)



# Generated at 2022-06-14 03:59:23.838581
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(increase, [1, 2, 3]) == [2, 3, 4]
    plus_1 = curried_map(increase)
    assert plus_1([1, 2, 3]) == [2, 3, 4]


# Generated at 2022-06-14 03:59:27.844424
# Unit test for function find
def test_find():
    print(find([1, 2, 3, 4, 5], lambda x: x > 3))
    assert find([1, 2, 3, 4, 5], lambda x: x > 3) == 4
    assert find([1, 2, 3, 4, 5], lambda x: x < 0) is None

# Generated at 2022-06-14 03:59:30.822874
# Unit test for function memoize
def test_memoize():
    def fib(n):
        if n < 2:
            return n
        else:
            return fib(n - 2) + fib(n - 1)

    fib = memoize(fib)

    assert fib(6) == 8
    assert fib(10) == 55


# Generated at 2022-06-14 03:59:33.380087
# Unit test for function eq
def test_eq():
    assert eq(1, 1)
    assert not eq(1, 2)



# Generated at 2022-06-14 03:59:39.160358
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x % 2, []) == []
    assert curried_filter(lambda x: x % 2, [1]) == [1]
    assert curried_filter(lambda x: x % 2, [1, 2, 3, 4, 5]) == [1, 3, 5]



# Generated at 2022-06-14 03:59:42.661141
# Unit test for function cond
def test_cond():
    def always_true(*args):
        return True

    result = cond([
        (always_true, lambda: 'always true'),
        (always_true, lambda: 'always true')
    ])

    assert result() == 'always true'



# Generated at 2022-06-14 04:00:00.208075
# Unit test for function cond
def test_cond():
    print('===== Unit test =====')
    print('Function cond:')
    f = cond([(lambda x: x % 2 == 0, lambda x: x),
              (lambda x: True, lambda x: x + 1)])

    print('Function f: ', f)
    print('With argument 42: ', f(42))
    print('With argument 42: ', f(43))
    print('With argument 42: ', f(44))



# Generated at 2022-06-14 04:00:06.749506
# Unit test for function curry
def test_curry():
    a = lambda x, y, z: x + y + z
    b = curry(a)
    assert b is not a and b(1) is not a
    assert b(1, 2, 3) == a(1, 2, 3)
    assert b(1)(2, 3) == b(1, 2)(3) == a(1, 2, 3)



# Generated at 2022-06-14 04:00:17.859082
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(identity, [1, 2, 3]) == [1, 2, 3]
    assert curried_map(increase, [1, 2, 3]) == [2, 3, 4]
    assert curried_map(identity)([1, 2, 3]) == [1, 2, 3]
    assert curried_map(increase)([1, 2, 3]) == [2, 3, 4]
    assert curried_map(identity, [1, 2, 3])([1, 2, 3]) == [1, 2, 3]
    assert curried_map(increase, [1, 2, 3])([1, 2, 3]) == [2, 3, 4]

# Generated at 2022-06-14 04:00:22.544072
# Unit test for function find
def test_find():
    @curry
    def eq_to(value):
        return lambda value1: value1 == value

    num_list = [1, 2, 3, 4, 5, 6]

    print(find(num_list, eq_to(5)))
    print(find(num_list, eq_to(6)))
    print(find(num_list, eq_to(0)))



# Generated at 2022-06-14 04:00:25.215980
# Unit test for function find
def test_find():
    """
    Test for function find.
    """
    assert find([1, 2, 3], eq(3)) == 3
    assert find([1, 2, 3], eq(4)) is None



# Generated at 2022-06-14 04:00:29.933869
# Unit test for function curried_filter
def test_curried_filter():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    result = curried_filter(lambda x: x % 2 == 0)(my_list)
    print(result)



# Generated at 2022-06-14 04:00:33.053828
# Unit test for function find
def test_find():
    assert None is find([1, 2, 3], lambda x: x == 0)
    assert 1 is find([1, 2, 3], lambda x: x == 1)

# Generated at 2022-06-14 04:00:39.326760
# Unit test for function cond
def test_cond():
    condition = [
        (lambda x: x > 1, lambda x: 'yay'),
        (lambda x: x % 2 == 0, lambda x: 'BOOM'),
        (lambda x: x < 5, lambda x: 'WTF')
    ]

    test_result = 0

    for i in range(10):
        test_result += cond(condition)(i)

    assert test_result == 'BOOMyayBOOMWTFBOOMyay'

# Generated at 2022-06-14 04:00:46.338431
# Unit test for function curry
def test_curry():
    test_list = [
        [5, 3, 2, 1],
        [4, 2, 1],
        [3, 1],
        [2],
    ]

    def function(a, b, c, d):
        return [a, b, c, d]

    curried_function = curry(function)
    for item in test_list:
        assert curried_function(*item) == function(*item)



# Generated at 2022-06-14 04:00:49.529132
# Unit test for function eq
def test_eq():
    res = eq(1, 1)
    if res is not True:
        print('result of eq(1, 1) should be true but', res, 'get')



# Generated at 2022-06-14 04:01:14.833920
# Unit test for function curried_filter
def test_curried_filter():
    """
    Function curried_filter is take function and collection
    and returns collection of all values that passed function filter.
    """
    odd = lambda x: x % 2 != 0
    collection = [1, 2, 3, 4, 5, 6]
    expected = [1, 3, 5]
    assert curried_filter(odd, collection) == expected

# Generated at 2022-06-14 04:01:19.237844
# Unit test for function curried_filter
def test_curried_filter():
    assert identity(True) is True
    assert identity(False) is False
    is_even = lambda value: value % 2 == 0
    assert curried_filter(is_even, [1, 2, 3]) == [2]



# Generated at 2022-06-14 04:01:21.863193
# Unit test for function eq
def test_eq():
    assert eq(1, 1)
    assert not eq(1, 2)
    assert eq(1, 1, 1)
    assert not eq(1, 1, 2)



# Generated at 2022-06-14 04:01:25.369648
# Unit test for function curry
def test_curry():
    from nose.tools import assert_equal
    assert_equal(curry(lambda x, y: x + y)(2)(2), 4)
    assert_equal(curry(lambda x, y: x + y, 1)(2), 2)



# Generated at 2022-06-14 04:01:29.534832
# Unit test for function curried_map
def test_curried_map():
    l = [1, 2, 3, 4, 5]

    def square(x): return x * x

    assert curried_map(square, l) == [1, 4, 9, 16, 25]



# Generated at 2022-06-14 04:01:33.612964
# Unit test for function find
def test_find():
    test_list = [1, 2, 3, 4, 5]
    test_list_none = [8, 6, 2]
    assert find(test_list, eq(1)) == 1
    assert find(test_list, eq(8)) is None
    assert find(test_list_none, eq(8)) == 8
    assert find(test_list_none, eq(1)) is None



# Generated at 2022-06-14 04:01:37.282054
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(lambda x: x * 2)([1, 2, 3, 4]) == [2, 4, 6, 8]
    assert curried_map(lambda x: x * 2, [1, 2, 3, 4]) == [2, 4, 6, 8]



# Generated at 2022-06-14 04:01:44.671238
# Unit test for function curried_filter
def test_curried_filter():
    collection = [1, 2, 3, 4, 5, 6]
    doubled_collection = [2, 4, 6, 8, 10, 12]
    less_than_three = curried_filter(lambda x: x < 3)

    test_result = curried_filter(lambda x: x < 3, collection)
    assert test_result == [1, 2]

    test_result = less_than_three(collection)
    assert test_result == [1, 2]
    assert collection == [1, 2, 3, 4, 5, 6]

    test_result = curried_map(lambda x: x * 2, less_than_three(collection))
    assert test_result == [2, 4]

    test_result = curried_map(lambda x: x * 2, less_than_three)(doubled_collection)

# Generated at 2022-06-14 04:01:55.207621
# Unit test for function memoize
def test_memoize():
    def sum(a, b):
        return a + b

    memoized_sum = memoize(sum)
    assert memoized_sum(1, 2) == 3
    assert memoized_sum(1, 2) == 3
    memoized_sum = memoize(sum)
    assert memoized_sum(2, 3) == 5
    assert memoized_sum(2, 3) == 5
    assert memoized_sum(1, 2) == 3
    memoized_sum = memoize(sum)
    assert memoized_sum(3, 9) == 12
    assert memoized_sum(3, 9) == 12



# Generated at 2022-06-14 04:02:01.859927
# Unit test for function curried_filter
def test_curried_filter():
    curried_less_than_five = curried_filter(lambda number: number < 5)
    assert curried_less_than_five([1, 2, 3, 4, 5, 6, 7, 8]) == [1, 2, 3, 4]
    assert curried_less_than_five([1, 7, 3, 12, 5, 6, 7, 8]) == [1, 3]



# Generated at 2022-06-14 04:03:41.851662
# Unit test for function curried_map
def test_curried_map():
    new_list = curried_map(increase)(list(range(5)))
    assert new_list == [1,2,3,4,5]


# Generated at 2022-06-14 04:03:46.639396
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x < 0, [1, 2, 3, 4, -2, -5, 1]) == [-2, -5]
    assert curried_filter(lambda x: x < 0, range(-5, 5)) == [-5, -4, -3, -2, -1]



# Generated at 2022-06-14 04:03:54.299785
# Unit test for function memoize
def test_memoize():
    from timeit import default_timer as timer

    @memoize
    def fib(n):
        if n < 2:
            return n
        return fib(n - 2) + fib(n - 1)

    t1_start = timer()
    fib(35)
    t1_stop = timer()

    t2_start = timer()
    fib(35)
    t2_stop = timer()

    assert t1_stop - t1_start > t2_stop - t2_start

    @memoize
    def multiply(a, b):
        return a * b

    result = multiply(2, 2)

    assert result == 4



# Generated at 2022-06-14 04:03:57.853052
# Unit test for function curry
def test_curry():
    def add(x, y):
        return x + y

    add2 = curry(add)
    assert add2(2)(2) == 4
    assert add2(2, 2) == 4
    assert add2(2, 1, 2) == 5


# Generated at 2022-06-14 04:04:01.593845
# Unit test for function curried_filter
def test_curried_filter():
    def even(x):
        return x % 2 == 0

    res = list(curried_filter(even)([1, 2, 3, 4, 5]))
    assert res == [2, 4]



# Generated at 2022-06-14 04:04:09.241849
# Unit test for function find
def test_find():
    list_find_test_case = [
        [
            [4, 5, 6],
            lambda x: x == 5,
            5
        ],
        [
            [0, -4, 45, -1],
            lambda x: x < 0,
            -4
        ],
        [
            [0, 4, 45, 1],
            lambda x: x < 0,
            None
        ]
    ]

    for item in list_find_test_case:
        assert find(item[0], item[1]) == item[2]



# Generated at 2022-06-14 04:04:16.222432
# Unit test for function cond
def test_cond():
    assert cond([
        (lambda x: x % 2 == 0, lambda x: "even"),
        (lambda x: x % 2 != 0, lambda x: "odd")
    ])(2) == 'even'

    assert cond([
        (lambda x: x % 2 == 0, lambda x: "even"),
        (lambda x: x % 2 != 0, lambda x: "odd")
    ])(1) == 'odd'



# Generated at 2022-06-14 04:04:26.037650
# Unit test for function curried_map
def test_curried_map():
    # test map by curried_function
    @curry
    def add(x, y):
        return x + y

    # function test
    def test_map(array, mapper):
        return curried_map(mapper, array)

    # Test with different argument
    assert test_map([1, 2, 3], add(1)) == [2, 3, 4]
    assert test_map([1, 2, 3], add(5)) == [6, 7, 8]
    assert test_map([1, 2, 3], add(3)) == [4, 5, 6]



# Generated at 2022-06-14 04:04:29.857955
# Unit test for function curried_map
def test_curried_map():
    map_ = curried_map(lambda x: x + 1)
    assert [1, 2, 3] == map_([0, 1, 2])



# Generated at 2022-06-14 04:04:41.511840
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(lambda x: x + 1, [1, 2, 3]) == [2, 3, 4]
    assert curried_map(lambda x: x + 1, []) == []
    assert curried_map(lambda x: x + 1, [3]) == [4]
    assert curried_map(lambda x: x + 1, [1, 2, 3, 4, 5]) == [2, 3, 4, 5, 6]
    assert curried_map(lambda x: x + 1, [1, 2, 3, 4, 5]) == [2, 3, 4, 5, 6]
    assert curried_map(lambda x: x + 1)([1, 2, 3]) == [2, 3, 4]
    assert curried_map(lambda x: x + 1)([]) == []
    assert cur

# Generated at 2022-06-14 04:06:13.748864
# Unit test for function cond
def test_cond():
    args_list = [
        (
            [],
            ValueError
        ),
        (
            [(lambda a: a < 50, lambda a: "less 50"),
             (lambda a: a < 100, lambda a: "less 100")],
            lambda a: a(25) == "less 50",
        ),
        (
            [(lambda a: a < 50, lambda a: "less 50"),
             (lambda a: a < 100, lambda a: "less 100")],
            lambda a: a(99) == "less 100",
        ),
        (
            [(lambda a: a > 200, lambda a: "more 200")],
            lambda a: a(100) == None
        )
    ]

    for args, result in args_list:
        assert result(cond(args))



# Generated at 2022-06-14 04:06:20.908516
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x % 2 == 0, [1, 2, 3, 4])([2, 4]) == [2, 4]
    assert curried_filter(lambda x: x % 2 == 0)([1, 2, 3, 4])([2, 4]) == [2, 4]
    assert curried_filter(lambda x: x % 2 == 0)([1, 2, 3, 4])([2, 4, 6, 8]) == [2, 4, 6, 8]

# Generated at 2022-06-14 04:06:26.702017
# Unit test for function memoize
def test_memoize():
    @memoize
    def fn(x):
        return x

    # first call
    assert fn(1) == 1
    assert fn(3) == 3
    assert fn(1) == 1
    # second call
    fn(1)
    assert fn(1) == 1
    fn(1)
    assert fn(1) == 1

    # test with additional result
    assert fn(7) == 7
    assert fn(7) == 7
    assert fn(3) == 3

# Generated at 2022-06-14 04:06:29.097174
# Unit test for function eq
def test_eq():
    assert eq(1, 1) is True
    assert eq(1, 2) is False



# Generated at 2022-06-14 04:06:39.791035
# Unit test for function cond
def test_cond():
    c1 = (lambda x: x % 15 == 0, lambda x: 'FizzBuzz')
    c2 = (lambda x: x % 3 == 0, lambda x: 'Fizz')
    c3 = (lambda x: x % 5 == 0, lambda x: 'Buzz')
    c4 = (lambda x: True, str)

    fizzbuzz = cond([c1, c2, c3, c4])

    print(fizzbuzz(1))
    print(fizzbuzz(3))
    print(fizzbuzz(5))
    print(fizzbuzz(15))


if __name__ == '__main__':
    test_cond()

# Generated at 2022-06-14 04:06:45.934389
# Unit test for function memoize
def test_memoize():
    def a(x: int) -> int:
        return x * 2

    def b(x: int) -> int:
        return x * 3

    def c(x: int) -> int:
        return x * 5

    function_to_test = cond([
        (eq(1), a),
        (eq(2), b),
        (eq(3), c),
    ])
    memoized_function = memoize(function_to_test)
    assert memoized_function(1) == 2
    assert memoized_function(2) == 6
    assert memoized_function(3) == 15



# Generated at 2022-06-14 04:06:51.865915
# Unit test for function cond
def test_cond():
    assert cond([
        (increase, lambda n: n + 1),
        (eq(0), lambda n: n + 2),
    ])(0) == 2
    assert cond([
        (increase, lambda n: n + 1),
        (eq(0), lambda n: n + 2),
    ])(1) == 2



# Generated at 2022-06-14 04:06:58.428677
# Unit test for function memoize
def test_memoize():
    """
    Runs a test for function memoize.
    """
    def fn(argument):
        print('calling function')
        return argument + 1

    m_fn = memoize(fn)

    print('checking test 1')
    assert m_fn(1) == 2
    print('checking test 2')
    assert m_fn(1) == 2

# Generated at 2022-06-14 04:07:04.142150
# Unit test for function memoize
def test_memoize():
    # Given
    def factorial(number):
        if number == 0:
            return 1
        return number * factorial(number - 1)

    memoized_factorial = memoize(factorial)

    # When
    factorial_results = [memoized_factorial(i) for i in range(10)]

    # Then
    assert factorial_results == [
        1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]




# Generated at 2022-06-14 04:07:07.368539
# Unit test for function curried_filter
def test_curried_filter():
    is_even = lambda value: value % 2 == 0
    curried_evens = curried_filter(is_even)
    values = list(range(100))

    assert curried_evens(values) == list(filter(is_even, values))

