

# Generated at 2022-06-14 03:57:56.760416
# Unit test for function curried_filter
def test_curried_filter():
    def greater_than_two(value):
        return value > 2

    assert curried_filter(greater_than_two, [1, 2, 3]) == [3]
    assert curried_filter(greater_than_two)([1, 2, 3]) == [3]
    assert curried_filter(greater_than_two, []) == []


# Generated at 2022-06-14 03:58:03.756951
# Unit test for function find
def test_find():
    assert find([1, 2, 3], lambda x: x == 2) == 2
    assert find([{'num': 1}, {'num': 2}, {'num': 3}], lambda x: x['num'] == 2) == {'num': 2}
    assert find([{'num': 1}, {'num': 2}, {'num': 3}], lambda x: x['num'] == 5) is None



# Generated at 2022-06-14 03:58:07.642144
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(lambda x: x ** 2)([1, 2, 3, 4]) == [1, 4, 9, 16]
    assert curried_map(lambda x: x ** 2)(range(1, 11)) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]



# Generated at 2022-06-14 03:58:08.958374
# Unit test for function eq
def test_eq():
    assert eq(1, 1)
    assert eq(1, 2)
    assert not eq(2, 3)



# Generated at 2022-06-14 03:58:13.591633
# Unit test for function find
def test_find():
    assert find([1, 2, 3, 4], lambda x: x % 2 == 0) == 2
    assert find([1, 2, 3, 5], lambda x: x % 2 == 0) is None
    assert find([0], lambda x: x % 2 == 0) == 0
    assert find([], lambda x: x % 2 == 0) is None

# Generated at 2022-06-14 03:58:15.537320
# Unit test for function memoize
def test_memoize():
    @memoize
    def expensive_function(value):
        return value ** 2

    result1 = expensive_function(10)
    result2 = expensive_function(10)
    assert eq(result1, 100)
    assert result1 is result2



# Generated at 2022-06-14 03:58:21.531795
# Unit test for function curry
def test_curry():
    @curry
    def sum_two_numbers(number1, number2):
        return number1 + number2

    assert sum_two_numbers(3)(4) == sum_two_numbers(3, 4)
    assert sum_two_numbers(3)(4) == 7
    assert sum_two_numbers(3, 4) == 7



# Generated at 2022-06-14 03:58:26.001843
# Unit test for function curried_map
def test_curried_map():
    def map_test_function(value):
        return value * value

    assert curried_map(map_test_function)([1, 2, 3, 4]) == [1, 4, 9, 16]



# Generated at 2022-06-14 03:58:30.269322
# Unit test for function eq
def test_eq():
    assert eq(1)(1)
    assert not eq(1)(2)



# Generated at 2022-06-14 03:58:37.702947
# Unit test for function curry
def test_curry():
    assert curry(lambda a, b, c: a + b + c)(1, 2, 3) == curry(lambda a, b, c: a + b + c)(1)(2)(3)



# Generated at 2022-06-14 03:58:45.034916
# Unit test for function eq
def test_eq():
    assert(eq(2, 2))


# Generated at 2022-06-14 03:58:46.350955
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(increase)([1,2,3]) == [2,3,4]


# Generated at 2022-06-14 03:58:49.681611
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(increase, [1, 2, 3, 4, 5]) == [2, 3, 4, 5, 6]



# Generated at 2022-06-14 03:58:54.256559
# Unit test for function cond
def test_cond():
    assert cond([(eq(1), identity), (eq(2), increase)]) == identity
    assert cond([(eq(2), increase), (eq(1), identity)]) == increase
    assert cond([(eq(3), increase), (eq(2), identity)]) == None


# Generated at 2022-06-14 03:59:00.092937
# Unit test for function curried_filter
def test_curried_filter():
    print('test_curried_filter')
    print(curried_filter(lambda x: x > 0, [1, 2, -2, 3, -3]) == [1, 2, 3])
    print(curried_filter(lambda x: x > 0)([1, 2, -2, 3, -3]) == [1, 2, 3])



# Generated at 2022-06-14 03:59:04.109524
# Unit test for function find
def test_find():
    assert find([1, 2, 3], eq(2)) == 2
    assert find([1, 2, 3], eq(3)) == 3
    assert find([1, 2, 3], eq(0)) is None



# Generated at 2022-06-14 03:59:12.567374
# Unit test for function memoize
def test_memoize():
    def fn(argument):
        print(f"fn was called with argument {argument}")
        return argument * 2

    cached_fn = memoize(fn)
    assert cached_fn(10) == 20
    assert cached_fn(10) == 20
    assert cached_fn(20) == 40
    assert find(cached_fn.__closure__[0].cell_contents, lambda item: item[0] == 10)[1] == 20
    assert find(cached_fn.__closure__[0].cell_contents, lambda item: item[0] == 20)[1] == 40



# Generated at 2022-06-14 03:59:17.555976
# Unit test for function cond
def test_cond():
    # Equivalent function to use cond
    def equivalent_func(a):
        return a * 2 if a is not None else 42
    # Function to test
    func = cond([
        (lambda x: x is not None, lambda x: x * 2),
        (lambda x: True, lambda x: 42),
    ])
    assert equivalent_func(1) == func(1)
    assert equivalent_func(None) == func(None)



# Generated at 2022-06-14 03:59:20.515012
# Unit test for function find
def test_find():
    find([1,2,3,4], lambda x: x%2 == 0)[0]
    return True


# Generated at 2022-06-14 03:59:24.365794
# Unit test for function curried_map
def test_curried_map():
    # Given
    collection = [1, 2, 3, 4, 5]
    mapper = lambda value: value + 1

    # When
    result = curried_map(mapper)(collection)

    # When
    assert result == [2, 3, 4, 5, 6]



# Generated at 2022-06-14 03:59:32.619001
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(identity)([1, 2, 3]) == [1, 2, 3]
    assert curried_map(increase)([1, 2, 3]) == [2, 3, 4]
    assert curried_map(lambda x: x * 2)([1, 2, 3]) == [2, 4, 6]


# Generated at 2022-06-14 03:59:42.130318
# Unit test for function find
def test_find():
    assert find([], None) is None
    assert find([], identity) is None
    assert find([1], lambda x: x == 5) is None
    assert find([1], lambda x: x == 1) == 1
    assert find([1, 2, 3], lambda x: x == 1) == 1
    assert find([1, 2, 3], lambda x: x == 2) == 2
    assert find([1, 2, 3], lambda x: x == 3) == 3
    assert find([1, 2, 3], lambda x: x == 4) is None
    assert find([1, 2, 3], lambda x: x == 5) is None



# Generated at 2022-06-14 03:59:47.987515
# Unit test for function memoize
def test_memoize():
    @memoize
    def add_memoized(a, b):
        return a + b

    def add(a, b):
        return a + b

    print(add_memoized(1, 2))
    print(add_memoized(1, 2))
    print(add(1, 3))
    print(add_memoized(1, 3))


# Generated at 2022-06-14 03:59:51.658088
# Unit test for function curried_map
def test_curried_map():
    square = lambda x: x*x
    assert curried_map(square)([1, 2, 3]) == [1, 4, 9]
    assert curried_map(square, [1, 2, 3]) == [1, 4, 9]


# Generated at 2022-06-14 03:59:56.983018
# Unit test for function memoize
def test_memoize():
    @memoize
    def add(a):
        return a + 1
    assert add("a") == add("a")
    assert add("a") != add("b")

if __name__ == "__main__":
    test_memoize()



# Generated at 2022-06-14 04:00:03.645271
# Unit test for function memoize
def test_memoize():
    """
    >>> import doctest
    >>> doctest.testmod()
    >>> def addOne(count):
    ...    return count + 1
    >>> memoizedAddOne = memoize(addOne)
    >>> memoizedAddOne(2)
    3
    >>> memoizedAddOne(2) == memoizedAddOne(2)
    True
    """
    pass

# Generated at 2022-06-14 04:00:06.556733
# Unit test for function find
def test_find():
    assert find([1, 2, 3], eq(2)) == 2
    assert find([1, 2, 3], eq(4)) is None


# Generated at 2022-06-14 04:00:09.302548
# Unit test for function eq
def test_eq():
    assert eq(1, 1)
    assert not eq(2, 1)



# Generated at 2022-06-14 04:00:15.711445
# Unit test for function cond
def test_cond():
    assert cond([(eq(1), identity), (eq(2), identity)])(2) == 2
    assert cond([(eq(1), identity), (eq(2), identity)])(1) == 1
    assert cond([(eq(1), identity), (eq(2), identity)])(3) is None
    assert cond([
        (eq(1), lambda: 'a'),
        (eq(2), lambda: 'b'),
        (eq(3), lambda: 'c')
    ])(3) == 'c'



# Generated at 2022-06-14 04:00:24.627380
# Unit test for function curried_filter
def test_curried_filter():
    collection = [1, 2, 3, 4, 5, 6, 7]
    assert curried_filter(lambda item: item > 2, collection) == [3, 4, 5, 6, 7]
    assert curried_filter(lambda item: item % 2 == 0, collection) == [2, 4, 6]

    assert curried_filter(lambda item: item > 2)(collection) == [3, 4, 5, 6, 7]
    assert curried_filter(lambda item: item % 2 == 0)(collection) == [2, 4, 6]

    even_filter = curried_filter(lambda item: item % 2 == 0)
    assert even_filter(collection) == [2, 4, 6]
    assert even_filter([1, 3, 5, 7, 9, 11]) == []



# Generated at 2022-06-14 04:00:39.924957
# Unit test for function eq
def test_eq():
    assert curry(eq, 2)(1, 1) == True
    assert eq(1, 1) == True
    assert eq(1, 2) == False
    assert eq('test', 'test') == True
    assert eq('test', 'Test') == False
    assert eq([1, 2, 3], [2, 3, 1]) == False
    assert eq([1, 2, 3], [1, 2, 3]) == True
    assert eq({'1': 1, '2': 2, '3': 3}, {'1': 1, '2': 2, '3': 3}) == True
    assert eq({'1': 1, '2': 2, '3': 3}, {'1': 1, '2': 1, '3': 3}) == False


# Generated at 2022-06-14 04:00:44.509068
# Unit test for function eq
def test_eq():
    assert eq(2, 2)
    assert eq(2)(2)
    assert eq(2, '2') is False
    assert eq(2)('2') is False
    assert eq('2', 2) is False
    assert eq('2')(2) is False
    assert eq('2', '2')
    assert eq('2')('2')
    assert eq('2', '3') is False
    assert eq('2')('3') is False



# Generated at 2022-06-14 04:00:53.429128
# Unit test for function cond
def test_cond():
    # Arrange
    is_zero = lambda a: a == 0
    is_even = lambda a: a % 2 == 0
    is_numeric = lambda a: type(a) == float or type(a) == int

    def double(a):
        return a * 2

    def quadruple(a):
        return a * 4

    def half(a):
        return a / 2

    # Act
    result = cond([
        (is_zero, lambda a: a),
        (is_even, double),
        (is_numeric, quadruple),
    ])(-1)

    # Assert
    # result should be -4
    assert result == -4



# Generated at 2022-06-14 04:00:59.863878
# Unit test for function cond
def test_cond():
    def is_zero(value: int) -> bool:
        return value == 0

    def is_odd(value: int) -> bool:
        return value % 2 == 1

    def double(value: int) -> int:
        return value * 2

    def identity(value: int) -> int:
        return value

    condition_list = (
        (is_zero, double),
        (is_odd, identity),
    )

# Generated at 2022-06-14 04:01:05.464734
# Unit test for function curried_filter
def test_curried_filter():
    def is_even(item):
        return item % 2 == 0

    test_collection = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result_collection = curried_filter(is_even, test_collection)

    assert result_collection == [2, 4, 6, 8, 10]



# Generated at 2022-06-14 04:01:13.921550
# Unit test for function cond
def test_cond():
    number = cond([
        (lambda arg: arg <= 0, lambda arg: 'lesser than or equal 0'),
        (lambda arg: arg <= 2, lambda arg: 'lesser than or equal 2'),
        (lambda arg: arg <= 5, lambda arg: 'lesser than or equal 5'),
        (lambda arg: arg <= 10, lambda arg: 'lesser than or equal 10'),
    ])
    assert number(-2) == 'lesser than or equal 0'
    assert number(0) == 'lesser than or equal 0'
    assert number(2) == 'lesser than or equal 2'
    assert number(5) == 'lesser than or equal 5'
    assert number(10) == 'lesser than or equal 10'
    assert number(11) == 'lesser than or equal 10'

# Generated at 2022-06-14 04:01:23.677804
# Unit test for function find
def test_find():
    test_list = [
        {
            'name': 'Ivan',
            'age': 15,
        },
        {
            'name': 'Boris',
            'age': 30,
        },
        {
            'name': 'Irina',
            'age': 30,
        },
        {
            'name': 'Petr',
            'age': 15,
        },
    ]

    def name_is_ivan(user):
        return user['name'] == 'Ivan'

    def age_is_30(user):
        return user['age'] == 30

    assert find(test_list, name_is_ivan) == test_list[0]
    assert find(test_list, age_is_30) == test_list[1]



# Generated at 2022-06-14 04:01:25.872556
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x % 2 == 0)([1, 2, 3, 4]) == [2, 4]



# Generated at 2022-06-14 04:01:32.091467
# Unit test for function memoize
def test_memoize():
    assert memoize(increase)(1) == 2
    assert memoize(increase)(1) == 2
    assert memoize(increase)(3) == 4
    assert memoize(increase)(3) == 4
    assert memoize(increase)(1) == 2
    assert memoize(increase)(1) == 2


# Generated at 2022-06-14 04:01:38.108573
# Unit test for function curry
def test_curry():
    assert curry(lambda x, y: x + y, args_count=2)(1, 2) == 3
    assert curry(lambda x, y: x + y, args_count=2)(1)(2) == 3
    assert curry(lambda x, y: x + y)(1, 2) == 3
    assert curry(lambda x, y, z: x + y + z)(1, 2)(3) == 6
    assert curry(lambda x, y, z: x + y + z)(1)(2)(3) == 6


# Unit tests for function increase

# Generated at 2022-06-14 04:01:51.032963
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(lambda x: x * 3)([1, 2, 3]) == [3, 6, 9]
    assert curried_map(lambda x: x * 3, [1, 2, 3]) == [3, 6, 9]



# Generated at 2022-06-14 04:01:54.897851
# Unit test for function eq
def test_eq():
    # Test if eq return true for equal int arguments
    assert eq(1, 1)

    # Test if eq return false for non equal int arguments
    assert not eq(1, 2)



# Generated at 2022-06-14 04:02:00.965172
# Unit test for function curry
def test_curry():
    assert curry(lambda x, y, z: x + y + z)(1)(2)(3) == 6
    assert curry(lambda x, y, z: x + y + z)(1)(2, 3) == 6
    assert curry(lambda x, y, z: x + y + z)(1, 2, 3) == 6


# Unit tests for function identity

# Generated at 2022-06-14 04:02:08.967430
# Unit test for function memoize
def test_memoize():
    # generate_list = lambda num: [num for _ in range(num)]
    # sum_list = lambda *args: sum(args)
    # memoized_sum_list = memoize(sum_list)

    # assert memoized_sum_list(generate_list(1000)) == 500500
    # assert memoized_sum_list(generate_list(1000)) == memoized_sum_list(generate_list(1000))
    pass



# Generated at 2022-06-14 04:02:18.213498
# Unit test for function curry
def test_curry():
    """
    currying is the technique of translating the evaluation of a function that takes multiple arguments
    (or a tuple of arguments) into evaluating a sequence of functions, each with a single argument.

    :returns: None
    """
    @curry
    def multiply(a, b):
        return a * b

    assert multiply(2)(3) == 6
    assert multiply(2, 3) == 6
    assert multiply(2)(3)(6) == 36

    @curry
    def flip(f):
        @wraps(f)
        def g(*args, **kwargs):
            return f(*reversed(args), **kwargs)
        return g

    @curry
    def subtract(a, b):
        return a - b

    assert subtract(4, 5) == -1

# Generated at 2022-06-14 04:02:24.781645
# Unit test for function eq
def test_eq():
    assert eq(1, 1)
    assert eq(2, 3) is False
    assert eq('a', 'b') is False
    assert eq('a', 'a')
    assert eq([1, 2, 3], [1, 2, 3])
    assert eq([1, 2, 3], [1, 2, 4]) is False
    assert eq((1, 2, 3), (1, 2, 3))
    assert eq((1, 2, 3), (1, 2, 4)) is False
    assert eq(
        {'a': 1, 'b': 2},
        {'a': 1, 'b': 2}
    )
    assert eq(
        {'a': 1, 'b': 2},
        {'a': 1, 'b': 3}
    ) is False



# Generated at 2022-06-14 04:02:33.180524
# Unit test for function cond
def test_cond():
    condition_list = [
        (lambda x: x % 2 == 0, lambda x: 'a'),
        (lambda x: x % 3 == 0, lambda x: 'b'),
        (lambda x: x % 5 == 0, lambda x: 'c'),
    ]
    f = cond(condition_list)

    assert f(1) == 'b'
    assert f(2) == 'a'
    assert f(9) == 'b'
    assert f(10) == 'a'
    assert f(15) == 'c'



# Generated at 2022-06-14 04:02:36.693681
# Unit test for function find
def test_find():
    assert find([], lambda _: False) is None
    assert find([1, 5], eq(1)) == 1
    assert find([1, 5], eq(2)) is None



# Generated at 2022-06-14 04:02:43.136222
# Unit test for function curry
def test_curry():
    """
    Test curry.
    """
    # Function with no arguments.
    f = curry(lambda: 1)
    assert f() == 1

    # Function with one argument.
    f = curry(lambda a: a * 2)
    assert f(2) == 4

    # Function with multiply arguments.
    f = curry(lambda a, b, c: a + b + c)
    assert f(1, 2, 3) == f(1)(2, 3) == f(1)(2)(3)



# Generated at 2022-06-14 04:02:48.377301
# Unit test for function cond
def test_cond():
    def success(value, expected_result):
        actual_result = cond(
            [
                (eq(0), increase),
                (eq(-1), identity),
                (eq(-10), increase),
            ]
        )(value)

        assert actual_result == expected_result, \
            'Error, expected "%s", but actual "%s"' % (expected_result, actual_result)

    success(0, 1)
    success(-1, -1)
    success(-10, increase(-10))


test_cond()

# Generated at 2022-06-14 04:03:09.556434
# Unit test for function curried_map
def test_curried_map():
    # Test for non-curried map
    map_function = curried_map(lambda a: {'a': a})
    assert map_function([1, 2, 3]) == [{'a': 1}, {'a': 2}, {'a': 3}]
    # Test for curried map
    map_function = curried_map(lambda a: {'a': a})
    assert map_function([1, 2, 3]) == [{'a': 1}, {'a': 2}, {'a': 3}]
    map_function = curried_map(lambda a: {'a': a})([1, 2, 3])
    assert map_function == [{'a': 1}, {'a': 2}, {'a': 3}]


# Generated at 2022-06-14 04:03:13.669427
# Unit test for function eq
def test_eq():
    """
    Function for test equality of two values.

    :returns: None
    :rtype: None
    """
    assert eq(1, 1)
    assert not eq(1, 2)

    assert eq(1)



# Generated at 2022-06-14 04:03:18.078449
# Unit test for function curry
def test_curry():
    assert curry(increase)(1), 2
    assert curry(increase, 2)(1, 1), 2
    assert curry(increase, 2)(1), curry(lambda x: increase(1, x), 1)
    assert curry(increase, 2)(1, 2), 3
    assert curry(increase, 2)(1)(2), 3

# Generated at 2022-06-14 04:03:28.963863
# Unit test for function curried_filter
def test_curried_filter():
    def is_even(number):
        return number % 2 == 0
    test_list = [1, 2, 3, 4, 5]
    test_filter_even_list = [2, 4]
    test_filter_odd_list = [1, 3, 5]
    test_filter_even_output = curried_filter(is_even)(test_list)
    test_filter_odd_output = curried_filter(lambda number: number % 2 == 1)(test_list)
    assert test_filter_even_output == test_filter_even_list
    assert test_filter_odd_output == test_filter_odd_list



# Generated at 2022-06-14 04:03:34.294347
# Unit test for function memoize
def test_memoize():
    result_dict = {}

    @memoize
    def memoized_fibonacci(value):
        if value == 0 or value == 1:
            return value
        if result_dict[value] != 0:
            return result_dict[value]
        result_dict[value] = memoized_fibonacci(value - 1) + memoized_fibonacci(value - 2)
        return result_dict[value]

    # Check for memoize functionality
    for x in range(1, 20):
        result_dict[x] = 0
        assert result_dict[x] == 0
        result = memoized_fibonacci(x)
        assert result_dict[x] == result


test_memoize()

# Generated at 2022-06-14 04:03:45.502747
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x > 1, [1, 2, 3]) == [2, 3]
    assert curried_filter(lambda x: x < 3, [1, 2, 3]) == [1, 2]
    assert curried_filter(lambda x: x % 2 == 0, range(10)) == [0, 2, 4, 6, 8]
    assert curried_filter(lambda x: x % 2 == 1, range(10)) == [1, 3, 5, 7, 9]
    assert curried_filter(lambda x: x > 10, [1, 2, 3]) == []
    assert curried_filter(lambda x: x < 0, [1, 2, 3]) == []
    assert curried_filter(lambda x: x % 2 == 0, [1, 2, 3]) == [2]
   

# Generated at 2022-06-14 04:03:48.338070
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: (x > 0))([0, 1, -2, 3, -4, 5]) == [1, 3, 5]

# Generated at 2022-06-14 04:03:49.827660
# Unit test for function eq
def test_eq():
    print(eq(1, 1))
    print(eq(2, 1))



# Generated at 2022-06-14 04:03:54.141987
# Unit test for function find
def test_find():
    assert find([1, 2, 3, 4, 5], eq(4)) == 4
    assert find([{'a': 1}, {'b': 2}], eq({'b': 2})) == {'b': 2}
    assert find([1, 2], eq(3)) is None
    assert find([1, 2], eq(3)) is None



# Generated at 2022-06-14 04:03:58.915104
# Unit test for function find
def test_find():
    collection = [1,2,3,4,5,6,7,8,9,10]
    def is_even(value):
        return value %  2 == 0
    assert find(collection, is_even) == 2
    assert find(collection, lambda value: value == 5) == 5
    assert find(collection, lambda value: value == 42) is None

# Generated at 2022-06-14 04:04:22.246010
# Unit test for function cond
def test_cond():
    cond_fn = cond(
        [(lambda value: len(value) == 0, lambda _: True),
         (lambda _: True, lambda _: False)])
    assert cond_fn('qwerty') is False
    assert cond_fn('') is True


# Generated at 2022-06-14 04:04:26.374562
# Unit test for function cond
def test_cond():
    assert cond([(eq(0),  increase), (eq(1), identity)])(0) == 1
    assert cond([(eq(0),  increase), (eq(1), identity)])(1) == 1



# Generated at 2022-06-14 04:04:28.666188
# Unit test for function curry
def test_curry():
    assert curry(lambda x: x + 1, 1)(1) == 2, "function curry not working"



# Generated at 2022-06-14 04:04:37.113565
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda item: item > 0)([1, 2, 3, -1, -2, -3]) == [1, 2, 3]
    assert curried_filter(lambda item: item > 0)([-1, -2, -3]) == []
    assert curried_filter(lambda item: item > 0)([]) == []
    assert curried_filter(lambda item: item > 0)([-1, -2, -3, 0]) == []



# Generated at 2022-06-14 04:04:39.037911
# Unit test for function curry
def test_curry():
    assert increase(5) == 6
    assert increase(6) == 7
    assert curry(increase)(6) == 7
    assert curry(increase)(6) == 7


# Generated at 2022-06-14 04:04:45.610828
# Unit test for function curried_filter
def test_curried_filter():
    print('=> test_curried_filter')
    xs = [1, 2, 3, 4, 5]
    evens = curried_filter(lambda x: x % 2 == 0)
    print('result {0}'.format(evens(xs)))
    assert evens(xs) == [2, 4]
    assert curried_filter(lambda x: x % 2 == 0)([1, 2, 3]) == [2]



# Generated at 2022-06-14 04:04:54.136008
# Unit test for function memoize
def test_memoize():
    def summation(n):
        retval = 1
        for i in range(1, n+1):
            retval *= i
        return retval

    start_time1 = time.time()
    summation_memoized = memoize(summation)
    end_time1 = time.time()
    print("time taken to calculate cached value", end_time1 - start_time1)

    start_time2 = time.time()
    summation_memoized(3)
    end_time2 = time.time()
    print("time taken without calculating", end_time2 - start_time2)


# Generated at 2022-06-14 04:05:01.218618
# Unit test for function curried_map
def test_curried_map():
    """
    Test for curried_map function.
    """
    assert curried_map(identity, [1, 2, 3]) == [1, 2, 3]
    custom_map = curried_map(identity)
    assert custom_map([1, 2, 3]) == [1, 2, 3]
    assert custom_map([4, 5, 6]) == [4, 5, 6]
    assert custom_map([7, 8, 9]) == [7, 8, 9]



# Generated at 2022-06-14 04:05:09.896990
# Unit test for function find
def test_find():
    list_of_integers = [1, 2, 3, 4]
    assert find(list_of_integers, lambda integer: integer == 1) == 1
    assert find(list_of_integers, lambda integer: integer == 2) == 2
    assert find(list_of_integers, lambda integer: integer == 3) == 3
    assert find(list_of_integers, lambda integer: integer == 4) == 4
    assert find(list_of_integers, lambda integer: integer == 5) is None



# Generated at 2022-06-14 04:05:15.810642
# Unit test for function curried_filter
def test_curried_filter():
    assert [1, 2] == curried_filter(lambda i: i > 0, [1, 2, 3, -1])(),\
        'curried_filter return wrong value'
    assert [2, 3] == curried_filter(lambda x: x > 1, list(range(10)))(),\
        'curried_filter return wrong value'
    assert [] == curried_filter(lambda i: i > 3, [1, 2, 3])(),\
        'curried_filter return wrong value'



# Generated at 2022-06-14 04:06:42.945243
# Unit test for function eq
def test_eq():
    """
    Test function eq.

    :returns: nothing
    :rtype: None
    """
    assert eq(1, 1) is True
    assert eq(2, 3) is False



# Generated at 2022-06-14 04:06:52.957223
# Unit test for function find
def test_find():
    # Test for find None
    collection = range(0, 10)
    assert find(collection, lambda x: x == 11) is None
    # Test for find first
    collection = range(0, 10)
    assert find(collection, lambda x: x < 2) == 0
    # Test for find all
    collection = range(0, 10)
    assert find(collection, lambda x: x < 20) == 0
    # Test for find last
    collection = range(0, 10)
    assert find(collection, lambda x: x > 8) == 9


# Generated at 2022-06-14 04:06:56.133355
# Unit test for function find
def test_find():
    assert find([4, 5, 6, 7, 8], lambda x: x > 3) == 4
    assert find([4, 5, 6, 7, 8], lambda x: x > 8) is None



# Generated at 2022-06-14 04:07:01.602165
# Unit test for function curry
def test_curry():
    """
    >>> add = curry(lambda a, b, c, d: a + b + c + d)
    >>> print(add(1)(2)(3)(4))
    10
    >>> print(add(1, 2)(3)(4))
    10
    >>> print(add(1)(2, 3)(4))
    10
    >>> print(add(1)(2)(3, 4))
    10
    >>> print(add(1, 2, 3, 4))
    10
    >>> add2 = curry(lambda a, b: a + b)
    >>> print(add2(1)(2))
    3
    >>> print(add2(1, 2))
    3
    """
    pass



# Generated at 2022-06-14 04:07:03.983086
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(increase, [1, 2, 3]) == [2, 3, 4]



# Generated at 2022-06-14 04:07:12.982978
# Unit test for function memoize
def test_memoize():
    def slow_function(argument):
        time.sleep(5)
        return argument

    cached_slow_function = memoize(slow_function)

    assert cached_slow_function(5) == 5
    assert cached_slow_function(5) == 5
    assert cached_slow_function(1) == 1
    assert cached_slow_function(2) == 2
    assert cached_slow_function(1) == 1
    assert cached_slow_function(2) == 2



# Generated at 2022-06-14 04:07:14.425307
# Unit test for function memoize
def test_memoize():
    assert memoize(increase)(5) == 6
    assert memoize(identity)([1, 2, 3]) == [1, 2, 3]

# Generated at 2022-06-14 04:07:21.540521
# Unit test for function memoize
def test_memoize():
    import random
    from time import time

    @memoize
    def foo(*args):
        return sum(args)

    start = time()
    for _ in range(1000000):
        foo(random.randint(0, 100), random.randint(0, 100))
    end = time()
    assert end - start < 0.05


if __name__ == '__main__':
    test_memoize()

# Generated at 2022-06-14 04:07:29.512634
# Unit test for function memoize
def test_memoize():
    def get_random_number():
        return random.randrange(0, 1000000)

    assert get_random_number() != get_random_number()

    memoized_get_random_number = memoize(get_random_number)
    assert memoized_get_random_number(1) == memoized_get_random_number(1)
    assert memoized_get_random_number(1) != memoized_get_random_number(2)
    assert memoized_get_random_number(1) == memoized_get_random_number(1)

# Generated at 2022-06-14 04:07:32.225975
# Unit test for function curried_filter
def test_curried_filter():
    assert (curried_filter(eq(2), [1, 2, 3, 2, 4, 5]) == [2, 2])
