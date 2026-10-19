

# Generated at 2022-06-14 03:58:07.014958
# Unit test for function curried_filter
def test_curried_filter():
    """
    Test curried_filter function.

    :returns: None
    :rtype: None
    """
    vector = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    isEven = lambda x: x % 2 == 0
    evenNumbers = curried_filter(isEven, vector)
    assert len(evenNumbers) == 4, 'not all numbers are even'
    assert find(evenNumbers, lambda x: x == 8), '8 is not even number'
    assert len(curried_filter(lambda x: True, vector)) == 9, 'some false'


# Generated at 2022-06-14 03:58:13.260911
# Unit test for function curry
def test_curry():
    assert curry(lambda x, y: x+y)(2)(3) == 5
    assert curry(lambda x, y, z: x+y+z)(2)(3)(4) == 9
    assert curry(lambda x, y, z: x+y+z)(2, 3, 4) == 9
    assert curry(lambda x, y, z: x+y+z)(2, 3)(4) == 9



# Generated at 2022-06-14 03:58:17.447901
# Unit test for function find
def test_find():
    assert find([], lambda element: False) is None
    assert find([1, 2, 3], lambda element: element == 2) == 2



# Generated at 2022-06-14 03:58:23.221354
# Unit test for function eq
def test_eq():
    # GIVEN
    first_value = 1
    second_value = 1

    # WHEN
    eq_result = eq(first_value, second_value)

    # THEN
    assert eq_result is True

test_eq()



# Generated at 2022-06-14 03:58:27.257940
# Unit test for function curry
def test_curry():
    """
    Unit test for function curry.
    """
    add = lambda a, b: a + b
    curried_add = curry(add)
    assert curried_add(1)(2) == 3
    assert curried_add(1, 2) == 3
    assert curried_add(1, 2, 3) == 3



# Generated at 2022-06-14 03:58:34.346420
# Unit test for function eq
def test_eq():
    assert eq(1)(1) == True
    assert eq(1, 1) == True
    assert eq(1)(2) == False
    assert eq(1, 2) == False
    assert eq(1, 1) == True
    assert eq(1, 1) == True
    assert eq(1, 2) == False


# Generated at 2022-06-14 03:58:38.438377
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x % 2 == 0, [1, 2, 3, 4]) == [2, 4]
    assert curried_filter(lambda x: x % 2 == 0)([1, 2, 3, 4]) == [2, 4]



# Generated at 2022-06-14 03:58:40.850355
# Unit test for function find
def test_find():
    assert find([1, 2, 3, 4], lambda x: x == 4) == 4
    assert find([1, 2, 3, 4], lambda x: x == 0) is None



# Generated at 2022-06-14 03:58:48.145571
# Unit test for function curried_map
def test_curried_map():
    assert curried_map()([1, 2, 3]) == [1, 2, 3]
    assert curried_map(increase)([1, 2, 3]) == [2, 3, 4]
    assert curried_map(increase)([1, 2, 3]) == [2, 3, 4]
    assert curried_map(increase)([1, 2, 3]) == [2, 3, 4]
    assert curried_map(increase)([1, 2, 3]) == [2, 3, 4]
    assert curried_map(increase)([1, 2, 3]) == [2, 3, 4]
    assert curried_map(increase)([1, 2, 3]) == [2, 3, 4]

# Generated at 2022-06-14 03:58:52.448628
# Unit test for function curried_filter
def test_curried_filter():
    assert (curried_filter(eq(5))([1, 5, 10, 12]) == [5])
    assert (curried_filter(eq(5), [1, 5, 10, 12]) == [5])


test_curried_filter()



# Generated at 2022-06-14 03:59:00.939869
# Unit test for function curried_map
def test_curried_map():
    test_list = [1, 2, 3]
    assert curried_map(identity)(test_list) == [1, 2, 3]
    assert curried_map(increase)(test_list) == [2, 3, 4]



# Generated at 2022-06-14 03:59:07.356387
# Unit test for function cond
def test_cond():
    fn = cond([
        (eq(True), identity),
        (eq(False), increase),
    ])

    print(
        'cond(...)(True) == identity\n',
        fn(True) == identity(True)
    )

    print(
        'cond(...)(False) == increase\n',
        fn(False) == increase(False)
    )


if __name__ == '__main__':
    test_cond()

# Generated at 2022-06-14 03:59:12.522556
# Unit test for function memoize
def test_memoize():
    serial = lambda value: value + 1
    memoized_serial = memoize(serial)
    assert memoized_serial(1) == serial(1)
    cached_serial = memoized_serial(1)
    assert cached_serial == serial(1)
    assert cached_serial == memoized_serial(1)



# Generated at 2022-06-14 03:59:14.227920
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(increase)(list(range(2))) == [1, 2]


# Generated at 2022-06-14 03:59:19.444623
# Unit test for function curried_map
def test_curried_map():
    data = [1, 2, 3, 4, 5]
    assert curried_map(increase, data) == [2, 3, 4, 5, 6]
    assert curried_map(increase)(data) == [2, 3, 4, 5, 6]


# Generated at 2022-06-14 03:59:28.672855
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(increase, [1, 2, 3]) == [2, 3, 4]
    assert curried_filter(lambda x: x % 2 == 0, [1, 2, 3]) == [2]
    assert curried_filter(lambda x: x < 0, [1, 2, 3]) == []
    assert curried_filter(lambda x: x > 0, [1, 2, 3]) == [1, 2, 3]
    assert curried_filter(lambda x: x > 0, []) == []
    assert curried_filter(lambda x: x % 2 == 0, [1, 2, 3]) == [2]
    assert curried_filter(lambda x: x % 2 == 0, [1, 3]) == []
    assert curried_filter(lambda x: x % 2 == 0, []) == []

# Generated at 2022-06-14 03:59:30.635753
# Unit test for function eq
def test_eq():
    assert(eq(True, True)() is True)
    assert(eq(True, False)() is False)


# Generated at 2022-06-14 03:59:36.432796
# Unit test for function cond
def test_cond():
    assert cond([])() is None
    assert cond([
        (lambda a, b: a > b, lambda a, b: a - b),
        (lambda a, b: b > a, lambda a, b: b - a),
        (lambda a, b: a == b, lambda a, b: a * b)
    ])(2, 1) == 1
    assert cond([
        (lambda a, b: a > b, lambda a, b: a - b),
        (lambda a, b: b > a, lambda a, b: b - a),
        (lambda a, b: a == b, lambda a, b: a * b)
    ])(1, 2) == 1

# Generated at 2022-06-14 03:59:43.314696
# Unit test for function curried_filter
def test_curried_filter():
    """
    Test function curried_filter.
    """
    assert curried_filter(lambda x: x % 2 == 0)([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert curried_filter(lambda x: x % 2 == 0)([1, 2, 3]) == [2]
    assert curried_filter(lambda x: x % 2 == 0)([1, 3]) == []



# Generated at 2022-06-14 03:59:53.551405
# Unit test for function cond
def test_cond():
    # Test function
    def test_fn(x):
        return 'x'

    # Testing execution function
    x = cond([
        (lambda x: x == 0, lambda x: '0'),
        (lambda x: x == 1, lambda x: '1'),
        (lambda x: x == 2, lambda x: '2'),
        (lambda x: x == 3, lambda x: '3'),
    ])
    assert x(0) == '0'
    assert x(1) == '1'
    assert x(2) == '2'
    assert x(3) == '3'
    assert x(4) is None

    # Testing condition function

# Generated at 2022-06-14 04:00:03.645431
# Unit test for function curried_filter
def test_curried_filter():
    even = lambda x: x % 2 == 0

    collection = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = list(curried_filter(even, collection))

    assert result == [2, 4, 6, 8]



# Generated at 2022-06-14 04:00:07.016292
# Unit test for function eq
def test_eq():
    assert eq(1, 1) == True
    assert eq(1, 2) == False
    assert eq('test', 'test') == True
    assert eq('test', 'test2') == False
    assert eq(None, None) == True
    assert eq(None, False) == False
    assert eq(False, False) == True
    assert eq(False, None) == False


# Generated at 2022-06-14 04:00:09.461228
# Unit test for function eq
def test_eq():
    """
    Test is function eq works properly.

    :param
    :type
    :returns
    :rtype
    """
    assert eq(1, 1)
    assert not eq(1, 2)
    assert not eq(2, 1)
    assert not eq('', ' ')



# Generated at 2022-06-14 04:00:16.850704
# Unit test for function find
def test_find():
    assert find([1, 2, 3], curry(lambda key, value: value == key))(1) == 1
    assert find([1, 2, 3], curry(lambda key, value: value == key))(2) == 2
    assert find([1, 2, 3], curry(lambda key, value: value == key))(3) == 3
    assert find([1, 2, 3], curry(lambda key, value: value == key))(4) is None


if __name__ == '__main__':
    import pytest
    pytest.main()

# Generated at 2022-06-14 04:00:21.308792
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x - x > 0)([]) == []
    assert curried_filter(lambda x: x % 2 == 0)([1, 2, 3, 4]) == [2, 4]
    assert curried_filter(eq(2))([1, 2, 3, 4]) == [2]



# Generated at 2022-06-14 04:00:22.983889
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(lambda x: x + 1, [1, 2]) == [2, 3]

# Generated at 2022-06-14 04:00:33.152952
# Unit test for function find
def test_find():
    arr = []
    assert find(arr, identity) is None

    arr = [1, 2, 3, 4, 5]
    assert find(arr, lambda x: x % 2 == 0) == 2

    arr = [1, 2, 3, 1, 5]
    assert find(arr, lambda x: x % 2) == 1
    assert find(arr, lambda x: x % 2 == 0) == 2
    assert find(arr, lambda x: x % 2 == 1) == 1
    assert find(arr, lambda x: x % 2 == 2) is None



# Generated at 2022-06-14 04:00:34.953521
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(increase, [0, 1]) == [1, 2]



# Generated at 2022-06-14 04:00:37.975842
# Unit test for function cond
def test_cond():
    assert cond([
        (eq(1), lambda n: n + 1),
        (eq(10), lambda n: n * 2),
        (eq(100), lambda n: n * 3),
    ])(10) == 20


# Generated at 2022-06-14 04:00:41.085001
# Unit test for function curried_map
def test_curried_map():
    print(curried_map(lambda x: x ** 2, [1, 2, 3, 4, 5]))


# Generated at 2022-06-14 04:00:59.034558
# Unit test for function find
def test_find():
    """
    search for value in collection and return it
    """
    collection = [1, 2, 3, 4, 5]

    assert find(collection, lambda x: x == 1) == 1
    assert find(collection, lambda x: x == 3) == 3
    assert find(collection, lambda x: x == 7) is None



# Generated at 2022-06-14 04:01:04.665461
# Unit test for function find
def test_find():
    assert find([1, 2, 3], lambda x: x == 1) == 1
    assert find([1, 2, 3], lambda x: x == 2) == 2
    assert find([1, 2, 3], lambda x: x == 3) == 3
    assert find([1, 2, 3], lambda x: x == 4) is None



# Generated at 2022-06-14 04:01:06.516932
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(identity, [1, 2, 3]) == [1, 2, 3]



# Generated at 2022-06-14 04:01:11.778456
# Unit test for function cond
def test_cond():
    is_number = lambda value: isinstance(value, int)
    is_string = lambda value: isinstance(value, str)
    to_string = lambda value: str(value)
    to_number = lambda value: int(value)

    print("Result of test_cond:", cond([
        (is_number, to_string),
        (is_string, to_number)
    ])(12))



# Generated at 2022-06-14 04:01:13.835203
# Unit test for function find
def test_find():
    print("test_find")
    print(find([1, 2, 3, 4], lambda v: v == 2))
    print(find([1, 2, 3, 4], lambda v: v == 0))


# Generated at 2022-06-14 04:01:16.658058
# Unit test for function curried_map
def test_curried_map():
    x = curried_map(lambda x: x + 1, [1, 2, 3])
    assert x == [2, 3, 4]



# Generated at 2022-06-14 04:01:22.690912
# Unit test for function memoize
def test_memoize():
    def expensive_function(x):
        if x == 3:
            return 'cached'
        return pipe(x, increase, increase)

    memoized_expensive_function = memoize(expensive_function, key=lambda a, b: a == b)

    assert memoized_expensive_function(3) == 'cached'
    assert memoized_expensive_function(1) == 3
    assert memoized_expensive_function(1) == 3



# Generated at 2022-06-14 04:01:31.407857
# Unit test for function curried_filter
def test_curried_filter():
    """
    Function curried_filter returns a new list with all elements that match the keys.
    If no element matches, an empty list is returned.

    :returns:
    :rtype:
    """
    assert curried_filter(eq(1), [1, 2, 3, 4, 5]) == [1]
    assert curried_filter(eq("1"), [1, 2, 3, 4, 5]) == []
    assert curried_filter(lambda x: True, [1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert curried_filter(lambda x: False, [1, 2, 3, 4, 5]) == []



# Generated at 2022-06-14 04:01:38.415899
# Unit test for function curried_filter
def test_curried_filter():
    print("Test for curried_filter")
    test_data = [
        {
            "collection": [1, 2, 3, 4, 5],
            "filter_by": 3,
            "expected": [4]
        },
        {
            "collection": [1, 2, 3, 4, 5],
            "filter_by": 6,
            "expected": []
        }
    ]
    for test in test_data:
        assert (curried_filter(eq(test["filter_by"]), test["collection"])
                == test["expected"])
    print("Test for curried_filter - OK")


# Generated at 2022-06-14 04:01:43.557228
# Unit test for function curried_map
def test_curried_map():
    """
    Curried Map Unit Test
    """
    assert curried_map(identity, [3])([]) == curried_map(identity)([3], [])
    assert curried_map(identity, [3, 4])([]) == curried_map(identity)([3, 4], [])
    assert curried_map(identity, [3, 4])([5, 6]) == curried_map(identity)([3, 4], [5, 6])
    assert curried_map(identity, [])([5, 6]) == curried_map(identity)([], [5, 6])


# Generated at 2022-06-14 04:02:12.993141
# Unit test for function eq
def test_eq():
    assert eq(1, 1) == True
    assert eq(1, 2) == False
    assert eq(1, 1, 1) == False



# Generated at 2022-06-14 04:02:19.334009
# Unit test for function memoize
def test_memoize():
    def to_string(x: str) -> str:
        return str(x)

    def multiply(x: int) -> int:
        return x * 2

    to_string_memoized = memoize(to_string)
    multiply_memoized = memoize(multiply)

    assert to_string_memoized(1) == "1"
    assert to_string_memoized(1) == "1"
    assert to_string_memoized(1) == "1"
    assert to_string_memoized(3) == "3"
    assert to_string_memoized(3) == "3"

    assert multiply_memoized(1) == 2
    assert multiply_memoized(1) == 2
    assert multiply_memoized(1) == 2
    assert multiply_

# Generated at 2022-06-14 04:02:27.437953
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(
        increase,
        []
    ) == []
    assert curried_map(
        increase,
        [1, 2, 3]
    ) == [2, 3, 4]
    assert curried_map(
        lambda x: x*2,
        [1, 2, 3]
    ) == [2, 4, 6]

    curried_lambda = lambda x: x + '!'
    assert curried_map(
        curried_lambda,
        ['first', 'second']
    ) == ['first!', 'second!']
    assert curried_map(
        curried_lambda,
        []
    ) == []

    curried_increase = curry(increase)
    assert curried_map(
        curried_increase,
        []
    ) == []
   

# Generated at 2022-06-14 04:02:31.439155
# Unit test for function memoize
def test_memoize():
    """
    Unit test for function memoize.

    :return:
    """
    memorized = memoize(lambda x: x + 1)
    assert memorized(1) == 2
    assert memorized(1) == 2



# Generated at 2022-06-14 04:02:35.262376
# Unit test for function cond
def test_cond():
    f = cond([
        (lambda x: x == 0, increase),
        (lambda x: x == 1, identity)
    ])
    assert f(0) == 1
    assert f(1) == 1
    assert f(2) is None



# Generated at 2022-06-14 04:02:38.831079
# Unit test for function find
def test_find():
    assert find([1, 2, 3], lambda value: value == 1) == 1
    assert find([1, 2, 3], lambda value: value == 5) is None


if __name__ == "__main__":
    test_find()

# Generated at 2022-06-14 04:02:42.367587
# Unit test for function find
def test_find():
    assert find([], lambda item: item) is None
    assert find([1, 2, 3], lambda item: item == 2) == 2
    assert find([1, 2, 3], lambda item: item not in [1, 2, 3]) is None



# Generated at 2022-06-14 04:02:45.941159
# Unit test for function cond
def test_cond():
    cond_function = cond([
        (curried_map(eq(0), [0]), identity),
        (curried_map(eq(1), [1]), increase)
    ])
    assert cond_function(0) == 0
    assert cond_function(1) == 2



# Generated at 2022-06-14 04:02:48.884537
# Unit test for function curried_map
def test_curried_map():
    def add1(x):
        return x+1
    assert curried_map(add1, [1, 2, 3]) == [2, 3, 4]



# Generated at 2022-06-14 04:02:53.637686
# Unit test for function memoize
def test_memoize():
    @memoize
    def func(a):
        print("func: calculating with a =", a)
        return a ** 2

    assert func(3) == 9
    assert func(3) == 9
    assert func(4) == 16
    assert func(4) == 16
    assert func(3) == 9


# Generated at 2022-06-14 04:03:48.778555
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(increase, [1, 2]) == [2, 3]



# Generated at 2022-06-14 04:03:51.945892
# Unit test for function curry
def test_curry():
    """
    Function curry should return function which return result of given function when called with all arguments.
    """
    function = curry(lambda x, y, z: x + y + z)
    assert function(1)(2)(3) == 6



# Generated at 2022-06-14 04:03:56.020244
# Unit test for function eq
def test_eq():
    assert eq(1, 1)
    assert not eq(1, 2)
    assert not eq(1, 0)
    assert not eq(1, None)
    assert not eq(None, 1)
    assert not eq(None, None)

    predicated = eq(1)
    assert predicated(1)
    assert not predicated(2)



# Generated at 2022-06-14 04:04:01.698118
# Unit test for function memoize
def test_memoize():
    def sum_to(n):
        print(n)
        return sum(range(n + 1))

    def sum_to_cache():
        return memoize(sum_to)

    assert sum_to(10) == sum_to_cache()(10)
    assert sum_to_cache()(10) == sum_to_cache()(10)



# Generated at 2022-06-14 04:04:09.182482
# Unit test for function cond
def test_cond():
    add = lambda x, y: x + y
    mult = lambda x, y: x * y
    sub = lambda x, y: x - y

    # cond([
    #     (lambda x: x < 0, add),
    #     (lambda x: x > 0, mult),
    #     (lambda x: x == 0, sub),
    # ], 1, 2)
    test_result = cond(
        [
            (lambda x: x < 0, add),
            (lambda x: x > 0, mult),
            (lambda x: x == 0, sub),
        ]
    )(1, 2)

    assert test_result == 3

    test_result = memoize(lambda x: x + 1)(2)
    assert test_result == 3


# Generated at 2022-06-14 04:04:13.784218
# Unit test for function eq
def test_eq():
    assert eq(1, 1) is True
    assert eq(1, 2) is False

    # curried
    assert eq(1)(1) is True
    assert eq(2)(1) is False
    assert eq(1, 2, 3) is False



# Generated at 2022-06-14 04:04:17.535172
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(identity)([1, 2, 3]) == [1, 2, 3]
    assert curried_map(increase)([1, 2, 3]) == [2, 3, 4]


# Generated at 2022-06-14 04:04:21.240453
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(eq(0), [0, 1, 0, 1, 0, 1])([]) == [0, 0, 0]
    assert curried_filter(lambda x: x % 2, [0, 1, 0, 1, 0, 1])([]) == [1, 1, 1]

# Generated at 2022-06-14 04:04:26.670159
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(identity)([1, 2, 3]) == [1, 2, 3], "incorrect curried_map"
    assert curried_map(increase)([1, 2, 3]) == [2, 3, 4], "incorrect curried_map"



# Generated at 2022-06-14 04:04:30.038030
# Unit test for function eq
def test_eq():
    assert eq(1, 1)
    assert not eq(1, 2)
    assert not eq(1, True)



# Generated at 2022-06-14 04:05:28.759247
# Unit test for function eq
def test_eq():
    assert eq(1, 1)
    assert eq(1, '1') is False
    assert eq(2 * 2, 4)
    assert eq(3 * 4 + 2, 14)



# Generated at 2022-06-14 04:05:31.676821
# Unit test for function curry
def test_curry():
    assert curry(lambda x, y: x + y)
    assert curry(lambda x, y, z: x + y + z)



# Generated at 2022-06-14 04:05:41.143540
# Unit test for function cond
def test_cond():
    is_even = lambda n: n % 2 == 0
    is_odd = lambda n: n % 2 != 0
    is_positive = lambda n: n > 0
    is_negative = lambda n: n < 0
    is_zero = lambda n: n == 0

    execute_even = lambda n: n
    execute_odd = lambda n: n ** 2
    execute_positive = lambda n: n ** (1 / 2)
    execute_negative = lambda n: n ** 3
    execute_zero = lambda n: n % (n + 1)

    condition_list = [
        (is_even, execute_even),
        (is_odd, execute_odd),
        (is_positive, execute_positive),
        (is_negative, execute_negative),
        (is_zero, execute_zero),
    ]


# Generated at 2022-06-14 04:05:46.073932
# Unit test for function eq
def test_eq():
    """
    Test for check if eq function return truly value when arguments are equal
    """
    equal_value = eq(5)
    assert equal_value(5) is True
    unequal_value = eq(7)
    assert unequal_value(5) is False



# Generated at 2022-06-14 04:05:53.489876
# Unit test for function curried_filter
def test_curried_filter():
    F = curried_filter
    assert F(lambda x: x % 2 == 0)([1, 2, 3, 4, 5]) == [2, 4]
    assert F(lambda x: x < 3)([1, 2, 3, 4, 5]) == [1, 2]
    assert F(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]) == [2, 4]
    return True


# Generated at 2022-06-14 04:06:01.020058
# Unit test for function curry
def test_curry():
    assert curry(lambda x: x * 2)(1) == 2
    assert curry(lambda x, y: x * y)(1)(2) == 2
    assert curry(lambda x, y, z: x * y * z)(1)(2)(3) == 6
    assert curry(lambda x, y=1: x * y)(2) == 2
    assert curry(lambda x, y, z=1: x * y * z)(4)(4) == 16
    assert curry(lambda x, y, z=1: x * y * z)(1, 2, 3) == 6
    assert curry(lambda x, y=1, z=2: x * y * z)(1) == 2
    assert curry(lambda x, y=1, z=2: x * y * z)(2, 4) == 8



# Generated at 2022-06-14 04:06:09.137289
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(increase)([0, 1, 2]) == [1, 2, 3]
    assert curried_map(increase, [0, 1, 2]) == [1, 2, 3]
    assert curried_map(increase, []) == []
    assert curried_map(identity, [1, 2, 3]) == [1, 2, 3]
    assert curried_map(lambda x: x**2, [1, 2, 3]) == [1, 4, 9]



# Generated at 2022-06-14 04:06:14.580648
# Unit test for function find
def test_find():
    def find_composer(key):
        return compose(
            identity,
            list,
            curried_filter(lambda x: x < 10),
            curried_map(lambda x: increase(x)),
            find(key=key)
        )

    assert find_composer(eq(9))(1) == 9
    assert find_composer(eq(10))(1) is None



# Generated at 2022-06-14 04:06:19.745422
# Unit test for function curried_filter
def test_curried_filter():
    assert (curried_filter(lambda x: x > 2)(range(10)) == [3, 4, 5, 6, 7, 8, 9])
    f = curried_filter(lambda x: x > 2)
    assert (f(range(10)) == [3, 4, 5, 6, 7, 8, 9])



# Generated at 2022-06-14 04:06:22.498440
# Unit test for function memoize
def test_memoize():
    fn = memoize(lambda x: x + 1)
    fn(1)
    assert len(fn.__closure__[0].cell_contents) == 1

