

# Generated at 2022-06-14 03:57:58.428415
# Unit test for function curried_filter
def test_curried_filter():
    first_list = [0, 1, 2, 3, 4]
    second_list = [1, 2, 3, 4]
    third_list = [2, 3, 4]
    fourth_list = [3, 4]

    filter_odd = curried_filter(lambda x: x % 2 != 0)
    assert(filter_odd(first_list) == second_list)
    assert(filter_odd(second_list) == fourth_list)
    assert(filter_odd(third_list) == fourth_list)

    filter_even = curried_filter(lambda x: x % 2 == 0)
    assert(filter_even(first_list) == first_list)
    assert(filter_even(second_list) == [2])
    assert(filter_even(third_list) == third_list)

# Generated at 2022-06-14 03:58:05.729436
# Unit test for function eq
def test_eq():
    assert eq(1, 1) is True
    assert eq(1, 2) is False
    assert eq('a', 'a') is True
    assert eq('a', 1) is False
    assert eq('a', 'b') is False
    assert eq(1, 'a') is False
    assert eq({1, 2, 3}, {1, 2, 3}) is True
    assert eq({1, 2, 3}, {2, 3, 4}) is False
    assert eq({1}, {1, 2, 3}) is False



# Generated at 2022-06-14 03:58:14.736526
# Unit test for function curried_filter
def test_curried_filter():
    assert [2, 3, 4] == curried_filter(lambda x: x > 1)([0, 1, 2, 3, 4]), \
        "curried_filter should return list of element greater than 1 for list [0, 1, 2, 3, 4]"
    assert curried_filter(lambda x: x > 1)([0, 1, 2, 3, 4]) == curried_filter(lambda x: x > 1, [0, 1, 2, 3, 4]), \
        "curried_filter should return list of element greater than 1 for list [0, 1, 2, 3, 4]"


# Generated at 2022-06-14 03:58:17.823200
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x > 0)([-1, -2, 3, 4]) == [3, 4]



# Generated at 2022-06-14 03:58:23.231356
# Unit test for function memoize
def test_memoize():
    def factorial(n):
        return factorial(n - 1) * n if n else 1

    factorial = memoize(factorial)
    assert factorial(3) == 6
    assert factorial(3) == 6



# Generated at 2022-06-14 03:58:26.483415
# Unit test for function find
def test_find():
    assert find([], lambda el: False) is None
    assert find([1, 2, 3], lambda el: el == 1) == 1
    assert find([1, 2, 3], lambda el: el == 5) is None



# Generated at 2022-06-14 03:58:30.433969
# Unit test for function eq
def test_eq():
    assert eq(1, 1), 'eq 1 1'
    assert eq(1, 1, 1), 'eq 1 1 1'
    assert eq('hello', 'hello'), 'eq hello hello'
    assert not eq(1, 2), 'not eq 1 2'
    assert not eq('hello', 'world'), 'not eq hello world'


# Generated at 2022-06-14 03:58:36.897903
# Unit test for function eq
def test_eq():
    assert True == eq(1, 1)
    assert False == eq(1, 2)
    assert False == eq(1, "1")

# Generated at 2022-06-14 03:58:38.896297
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x > 3)([1, 2, 3, 4, 5]) == [4, 5]


# Generated at 2022-06-14 03:58:41.283391
# Unit test for function curry
def test_curry():
    curry_add = curry(lambda x, y: x + y)

    assert curry_add(1, 2) == 3
    assert curry_add(1)(2) == 3



# Generated at 2022-06-14 03:58:50.104721
# Unit test for function curried_map
def test_curried_map():
    double = lambda x: 2*x
    assert curried_map(double)([1, 2, 3]) == [2, 4, 6]



# Generated at 2022-06-14 03:58:56.642515
# Unit test for function eq
def test_eq():
    assert eq(1, 1) == True
    assert eq(2, 3) == False
    assert eq(1, 2) == False
    assert eq(1, None) == False
    assert eq(None, 1) == False
    assert eq(1, '1') == False
    assert eq(2, 3) == False
    assert eq('1234', '1234') == True


# Generated at 2022-06-14 03:59:07.996692
# Unit test for function cond
def test_cond():
    """
    Test for function cond

    :returns:
    :rtype:
    """
    multiple_of_3 = lambda x: x % 3 == 0
    multiple_of_7 = lambda x: x % 7 == 0
    multiple_of_21 = lambda x: x % 21 == 0

    # Creating function witch returns true if argument is multiple of 3, 7 or 21
    multiple_of_3_or_7_or_21 = cond([
        (multiple_of_21, lambda x: True),
        (multiple_of_3, lambda x: True),
        (multiple_of_7, lambda x: True),
        (lambda _: True, lambda x: False)
    ])

    # Creating function witch returns true if argument is multiple of 3 or 7

# Generated at 2022-06-14 03:59:17.519914
# Unit test for function cond
def test_cond():
    assert cond([
        (lambda x: x == 0, lambda x: "Zero"),
        (lambda x: x % 2, lambda x: "odd"),
        (lambda x: True, lambda x: "even")
    ])(0) == "Zero"

    assert cond([
        (lambda x: x == 0, lambda x: "Zero"),
        (lambda x: x % 2, lambda x: "odd"),
        (lambda x: True, lambda x: "even")
    ])(1) == "odd"

    assert cond([
        (lambda x: x == 0, lambda x: "Zero"),
        (lambda x: x % 2, lambda x: "odd"),
        (lambda x: True, lambda x: "even")
    ])(2) == "even"


# Generated at 2022-06-14 03:59:25.356709
# Unit test for function curried_filter
def test_curried_filter():
    naturals = [1, 2, 3, 4, 5, 6]
    odds = curried_filter(lambda x: x % 2 == 1, naturals)
    assert odds == [1, 3, 5]
    evens = curried_filter(lambda x: x % 2 == 0, naturals)
    assert evens == [2, 4, 6]
    more_evens = curried_filter(lambda x: x % 2 == 0)
    assert more_evens(naturals) == [2, 4, 6]



# Generated at 2022-06-14 03:59:30.446471
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x % 2 == 0)([2, 3, 4]) == [2, 4]
    assert curried_filter(lambda x: x > 3)([1, 2, 3, 4, 5]) == [4, 5]
    assert curried_filter(lambda x: x < 4)([3, 2, 4, 2, 5, 2]) == [3, 2, 2, 2]



# Generated at 2022-06-14 03:59:32.353911
# Unit test for function curry
def test_curry():
    assert curry(lambda x, y: x + y, 2) == (lambda x, y: x + y)
    assert curry(lambda: 1) == (lambda: 1)



# Generated at 2022-06-14 03:59:34.430722
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(lambda x: x + 1, [1, 2, 3]) == [2, 3, 4]


# Generated at 2022-06-14 03:59:39.999132
# Unit test for function curry
def test_curry():
    def add(a, b, c):
        return a + b + c

    assert curry(add, 1)(1, 1) == 3
    assert curry(add, 2)(1)(1) == 3
    assert curry(add, 3)(1, 1, 1) == 3


# Test function identity

# Generated at 2022-06-14 03:59:50.623312
# Unit test for function cond
def test_cond():
    def greater_than_3(value):
        return value > 3

    def greater_than_5(value):
        return value > 5

    def greater_than_10(value):
        return value > 10

    def action_1(value):
        return 'action_1'

    def action_2(value):
        return 'action_2'

    def action_3(value):
        return 'action_3'

    fn = cond([
        (greater_than_10, action_1),
        (greater_than_5, action_2),
        (greater_than_3, action_3),
    ])

    assert fn(10) == 'action_1'
    assert fn(5) == 'action_2'
    assert fn(3) == 'action_3'



# Generated at 2022-06-14 04:00:03.774968
# Unit test for function curry
def test_curry():
    assert curry(lambda a, b, c: a + b - c)(4, 5, 6) == 3
    assert curry(lambda a, b, c: a + b - c)(4, 5)(6) == 3
    assert curry(lambda a, b, c: a + b - c)(4)(5, 6) == 3
    assert curry(lambda a, b, c: a + b - c)(4)(5)(6) == 3

# Tests for function identity

# Generated at 2022-06-14 04:00:11.090154
# Unit test for function curried_filter
def test_curried_filter():
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    is_upper_then_4 = lambda x: x > 4
    assert curried_filter(is_upper_then_4, arr) == [5, 6, 7, 8, 9, 10]
    assert curried_filter(is_upper_then_4)(arr) == [5, 6, 7, 8, 9, 10]


# Generated at 2022-06-14 04:00:16.419403
# Unit test for function curry
def test_curry():
    curried_filter_by_greater_than_5 = curry(curried_filter, args_count=2)(lambda x: x > 5)
    assert curried_filter_by_greater_than_5([1, 2, 3, 5, 8, 13, 21]) == [8, 13, 21]



# Generated at 2022-06-14 04:00:24.782168
# Unit test for function eq
def test_eq():
    assert eq(1, 1)(1)
    assert not eq(1, 1)(2)
    assert not eq(1, 2)(1)
    assert not eq(False, True)(True)
    assert eq(False, True)(False)
    assert eq('', '')('')
    assert not eq('', '')(' ')
    assert not eq(' ', '')(' ')
    assert not eq(' ', ' ')(' ')
    assert not eq([], [])([])
    assert not eq([1, 2], [1, 2])([])
    assert eq([1, 2], [1, 2])([1, 2])
    assert not eq([], [])([1])
    assert not eq([1, 2], [1, 2])([3, 4])

# Generated at 2022-06-14 04:00:33.258217
# Unit test for function find
def test_find():
    # test on same list
    list_ = [1, 2, 3, 4, 5]
    result = find(list_, lambda x: x == 3)
    assert result == 3

    # test on empty list
    result = find([], lambda x: x == 3)
    assert result is None

    # test on different list
    list_ = [1, 2, 4, 4, 5]
    result = find(list_, lambda x: x == 3)
    assert result is None


# Generated at 2022-06-14 04:00:35.298649
# Unit test for function eq
def test_eq():
    assert eq(1, 1) == True
    assert eq(1, 2) == False


# Generated at 2022-06-14 04:00:40.366504
# Unit test for function curried_map
def test_curried_map():
    curried_mapper = curried_map(increase)
    assert curried_mapper([1, 2, 3]) == [2, 3, 4]
    assert curried_mapper([0, 0, 0]) == [1, 1, 1]
    assert curried_mapper([-1, -2, -3]) == [0, -1, -2]



# Generated at 2022-06-14 04:00:51.689675
# Unit test for function cond
def test_cond():
    def add(a, b):
        return a + b

    def sub(a, b):
        return a - b

    def mul(a, b):
        return a * b

    def div(a, b):
        return a / b

    # Test function

    def test(a, b, c, d):
        return cond([
            (eq(c), lambda *args: add(*args)),
            (eq(d), lambda *args: sub(*args)),
        ])(a, b)

    # Expected function

    def expected(a, b, c, d):
        return add(a, b) if c else sub(a, b)

    # Simple test

    assert test(1, 2, 'add', 'sub') == expected(1, 2, 'add', 'sub')



# Generated at 2022-06-14 04:00:59.863447
# Unit test for function memoize
def test_memoize():
    """
    Unit test for function memoize
    For first two calls of memoized function result equal to fn result.
    For three call result from cache.
    """
    counter = 0

    @memoize
    def function(arg):
        nonlocal counter
        counter += 1
        return arg

    first_call_result = function(1)
    second_call_result = function(1)
    third_call_result = function(1)

    assert counter == 2
    assert first_call_result == third_call_result == second_call_result == 1

# Generated at 2022-06-14 04:01:03.588821
# Unit test for function find
def test_find():
    assert find([1, 2, 3, 4, 5], lambda x: x == 3) == 3
    assert find([1, 2, 3, 4, 5], lambda x: x == 6) is None



# Generated at 2022-06-14 04:01:16.863306
# Unit test for function find
def test_find():
    collection = [{'name': 'Bob'}, {'name': 'Nick'}, {'name': 'Jim'}]
    key = lambda obj: obj['name'] == 'Jim'
    result = find(collection, key)
    assert result == {'name': 'Jim'}



# Generated at 2022-06-14 04:01:20.054682
# Unit test for function curry
def test_curry():
    curry_sum = curry(sum)
    assert curry_sum(1)(2)(3) == 6
    assert curry_sum(1)(2)(3)(4)(5)(6) == 21



# Generated at 2022-06-14 04:01:22.691096
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(lambda x: x, [1]) == [1]
    assert curried_map(lambda x: x + 1, [1]) == [2]



# Generated at 2022-06-14 04:01:26.419716
# Unit test for function find
def test_find():
    assert find([], identity) is None
    assert find([1], identity) == 1

    assert find([1, 2, 3, 4], eq(1)) == 1
    assert find([1, 2, 3, 4], eq(5)) is None



# Generated at 2022-06-14 04:01:31.572645
# Unit test for function memoize
def test_memoize():
    # define function
    @memoize
    def add(a):
        return a + 5

    # check result
    assert add(3) == 8
    assert add(3) == 8
    assert add(4) == 9
    assert add(4) == 9

# Generated at 2022-06-14 04:01:39.590893
# Unit test for function curry
def test_curry():
    assert curry(lambda x, y: x + y)(1)(2) == 3
    assert curry(lambda x, y, z: x + y + z)(1)(2)(3) == 6
    assert curry(lambda x, y, z, z2: x + y + z + z2)(1)(2)(3)(4) == 10
    assert curry(lambda x, y, z, z2: x + y + z + z2)(1, 2)(3, 4) == 10



# Generated at 2022-06-14 04:01:46.209392
# Unit test for function curried_filter
def test_curried_filter():
    a = [1, 2, 3, 4, 5]
    f = curried_filter(eq(3))
    print(f(a))
    print(f([1, 2, 3, 4, 5]))

    # Unit test for function curried_map
    def test_curried_map():
        a = [1, 2, 3, 4, 5]
        f = curried_map(increase)
        print(f(a))
        print(f([1, 2, 3, 4, 5]))

    test_curried_map()

# Generated at 2022-06-14 04:01:52.943483
# Unit test for function cond
def test_cond():
    def add_one(x):
        return x + 1

    def add_two(x):
        return x + 2

    def divide_by_two(x):
        return x / 2

    f = cond([
        (
            lambda x: x < 0,
            add_one
        ),
        (
            lambda x: x > 0,
            add_two
        ),
        (
            lambda x: True,
            divide_by_two
        ),
    ])
    assert f(-1) == 0
    assert f(0) == 0.5
    assert f(1) == 3



# Generated at 2022-06-14 04:02:04.468904
# Unit test for function memoize
def test_memoize():
    # Arrange
    # cache will be empty
    # and function will add items to it
    cache: List[Any] = []
    # use function increase for result evaluating
    fn = increase
    # use function eq for comparing arguments
    key = eq

    # Act
    # set memoized_fn
    memoized_fn = memoize(fn, key)

    # Act
    # invoke memoized_fn with argument 1
    # which will invoke increase_one, then save to cache and return result
    memoized_fn(1)
    # invoke memoized_fn with argument 1 again
    # which will read result from cache, then return result
    memoized_fn(1)
    # invoke memoized_fn with argument 2
    # which will invoke increase_one, then save to cache and return result
    memoized_fn(2)

   

# Generated at 2022-06-14 04:02:10.081142
# Unit test for function find
def test_find():
    elements = [{'id': 0}, {'id': 1}, {'id': 2}]
    assert find(elements, compose((eq(2)), lambda element: element['id'])) == {'id': 2}
    assert find(elements, compose((eq(3)), lambda element: element['id'])) is None



# Generated at 2022-06-14 04:02:44.957967
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(lambda x: x + 1, [1, 2, 3]) == [2, 3, 4]



# Generated at 2022-06-14 04:02:55.834916
# Unit test for function memoize
def test_memoize():
    # This is some expensive computation we want to cache the result of
    def expensive_add(a, b):
        time.sleep(0.0001)
        return a + b

    # Run the expensive calculation 10 times. Without memoization this
    # takes a while because we repeat almost the same calcuation 10 times
    start_time_nonmemoized = time.time()
    for i in range(10):
        expensive_add(5, 5)
    end_time_nonmemoized = time.time()

    # Run the calculation 10 times with memoization. You can see that the
    # total run time is much smaller and most of the time is spent on the
    # first call to expensive_add. Subsequent calls are almost instant.
    start_time_memoized = time.time()

# Generated at 2022-06-14 04:02:59.143796
# Unit test for function curried_map
def test_curried_map():
    collection = [1, 2, 3]
    mapper = lambda x: x * x
    assert curried_map(mapper, collection) == [1, 4, 9]



# Generated at 2022-06-14 04:03:07.123666
# Unit test for function cond
def test_cond():
    assert cond([
        (lambda x: x < 0, lambda x: 'Less then 0'),
        (lambda x: x > 0, lambda x: 'More then 0'),
        # if not functions return true,
        # return last function result
        (lambda x: x == 0, lambda x: 'Equal 0')
    ])(0) == 'Equal 0'

    assert cond([
        (lambda x: x < 0, lambda x: 'Less then 0'),
        (lambda x: x < 0, lambda x: 'Less then 0'),
        # if not functions return true,
        # return last function result
        (lambda x: x == 0, lambda x: 'Equal 0')
    ])(-1) == 'Less then 0'



# Generated at 2022-06-14 04:03:09.400294
# Unit test for function curried_filter
def test_curried_filter():
    even = curried_filter(lambda value: value % 2 == 0)

    assert even([0, 1, 2, 3, 4]) == [0, 2, 4]
    assert even([1, 3, 5]) == []



# Generated at 2022-06-14 04:03:14.302765
# Unit test for function cond
def test_cond():
    is_even = lambda x: x % 2 == 0
    is_odd = lambda x: not is_even(x)
    is_zero = lambda x: x == 0

    result = cond([
        (is_even, lambda x: "Even value"),
        (is_odd, lambda x: "Odd value"),
        (is_zero, lambda x: "Zero value")
    ])

    return (
        (result(2), "Even value"),
        (result(3), "Odd value"),
        (result(0), "Zero value")
    )



# Generated at 2022-06-14 04:03:17.939666
# Unit test for function curried_map
def test_curried_map():
    result = curried_map(increase)(range(5))
    expected_result = [1, 2, 3, 4, 5]

    assert all(map(eq(True), result))
    assert all(map(eq(True), expected_result))



# Generated at 2022-06-14 04:03:22.783172
# Unit test for function curried_filter
def test_curried_filter():
    greater_than_5 = curried_filter(lambda x: x > 5)

    assert greater_than_5([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [6, 7, 8, 9]



# Generated at 2022-06-14 04:03:27.393333
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(eq(1), [1, 2, 3]) == [1]
    assert curried_filter(eq(3), [1, 2, 1, 1, 3]) == [3]
    assert curried_filter(eq(2), []) == []



# Generated at 2022-06-14 04:03:30.989182
# Unit test for function curry
def test_curry():
    def sum(a, b, c, d):
        return a + b + c + d

    assert curry(sum)(10)(15)(20)(30) == 75, 'Should return 75'
    assert curry(sum)(10, 20)(30)(20) == 80, 'Should return 80'



# Generated at 2022-06-14 04:03:46.892173
# Unit test for function eq
def test_eq():
    eq_five = eq(5)

# Generated at 2022-06-14 04:03:54.891829
# Unit test for function cond
def test_cond():
    f1 = lambda a: a > 0
    f2 = lambda a: 'a > 0'
    g1 = lambda a: a == 0
    g2 = lambda a: 'a == 0'
    h1 = lambda a: a < 0
    h2 = lambda a: 'a < 0'
    cond_test = cond([(f1, f2), (g1, g2), (h1, h2)])
    assert cond_test(1) == f2(1)
    assert cond_test(0) == g2(0)
    assert cond_test(-1) == h2(-1)
    print("Function cond is ok!")
    print("Test cond was successful!")

test_cond()

# Generated at 2022-06-14 04:03:57.242783
# Unit test for function find
def test_find():
    """
    >>> test_find()
    123
    """
    print(find([1, 2, 3], lambda x: x == 3))



# Generated at 2022-06-14 04:04:03.594742
# Unit test for function curried_map
def test_curried_map():
    map_function = curried_map(increase)
    assert [2, 3, 4, 5] == map_function([1, 2, 3, 4])
    assert ['b', 'bb', 'bbb'] == map_function(['a', 'aa', 'aaa'])
    assert [0, 0, 0] == map_function([])



# Generated at 2022-06-14 04:04:09.026571
# Unit test for function cond
def test_cond():
    assert eq(
        cond(
            [(eq(0), identity), (eq(1), increase)]
        )(0), 0
    )
    assert eq(
        cond(
            [(eq(0), identity), (eq(1), increase)]
        )(1), 2
    )


# Generated at 2022-06-14 04:04:14.853480
# Unit test for function curried_filter
def test_curried_filter():
    # Test for correctly work
    assert curried_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]) == [2, 4]
    # Test for work with curried function
    assert curried_filter(lambda x: x % 2 == 0)([1, 2, 3, 4, 5]) == [2, 4]



# Generated at 2022-06-14 04:04:21.200727
# Unit test for function eq
def test_eq():
    assert True == eq(1, 1)
    assert False == eq(1, 2)
    assert True == eq(2, 2)
    assert False == eq('1', 1)
    assert False == eq([1, 2, 3], [4, 5, 6])
    assert True == eq([1, 2, 3], [1, 2, 3])
    assert False == eq({1, 2}, {1, 2, 3})
    assert True == eq({2, 3}, {2, 3})



# Generated at 2022-06-14 04:04:29.494543
# Unit test for function cond
def test_cond():
    """
    After run,
    this test should show `0` and `2`
    """
    cont = cond([
        (identity, lambda x: x),
        (eq(0), lambda: 0),
        (eq(1), lambda: 1),
        (eq(2), lambda: 2),
        (eq(3), lambda: 3),
        (eq(4), lambda: 4),
    ])

    print(cont(0))
    print(cont(2))

# Generated at 2022-06-14 04:04:33.213875
# Unit test for function find
def test_find():
    assert find([1, 2, 3], lambda item: item == 2) == 2
    assert find([1, 2, 3], lambda item: item == 4) is None



# Generated at 2022-06-14 04:04:37.065729
# Unit test for function curried_filter
def test_curried_filter():
    collection = range(11)

    assert list(curried_filter(lambda x: x % 2)(collection)) == list(filter(lambda x: x % 2, collection))
    assert list(curried_filter(lambda x: x % 2, collection)) == list(filter(lambda x: x % 2, collection))



# Generated at 2022-06-14 04:04:55.344630
# Unit test for function find
def test_find():
    assert find(
        [1, 2, 3],
        lambda x: x == 2
    ) == 2

    assert find(
        [1, 2, 3],
        lambda x: x == 4
    ) is None


# Generated at 2022-06-14 04:04:57.673632
# Unit test for function find
def test_find():
    assert find([1, 2, 3], eq(2)) == 2
    assert find([1, 2, 3], eq(4)) is None



# Generated at 2022-06-14 04:05:02.982524
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])(
    ) == [2, 4, 6]
    assert curried_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])([]) == []
    assert curried_filter(lambda x: x % 2 == 0, [])([]) == []


# Generated at 2022-06-14 04:05:07.725978
# Unit test for function find
def test_find():
    list_to_find = [2, 3, 4, 5, 1, 7]
    item_to_find = 7

    result = find(list_to_find, lambda x: x == item_to_find)
    assert result == item_to_find



# Generated at 2022-06-14 04:05:21.746219
# Unit test for function cond
def test_cond():
    def test_is_five(value: int) -> bool:
        return value == 5

    def test_add_five(value: int) -> int:
        return value + 5

    def test_add_ten(value: int) -> int:
        return value + 10

    assert cond([
        (test_is_five, test_add_five),
        (lambda _: True, test_add_ten),
    ])(0) == 10
    assert cond([
        (test_is_five, test_add_five),
        (lambda _: True, test_add_ten),
    ])(5) == 10
    assert cond([
        (test_is_five, test_add_five),
        (lambda _: True, test_add_ten),
    ])(6) == 16



# Generated at 2022-06-14 04:05:27.091663
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(identity)([1, 2, 3]) == [1, 2, 3]
    assert curried_map(increase)([1, 2, 3]) == [2, 3, 4]
    assert curried_map(increase, [1, 2, 3]) == [2, 3, 4]



# Generated at 2022-06-14 04:05:36.670229
# Unit test for function curried_filter
def test_curried_filter():
    fibonacci_seq = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
    print("fibonacci_seq")
    print(fibonacci_seq)
    equal_2 = eq(2)
    print("equal_2")
    print(equal_2)
    equal_2_curried_filter = curried_filter(equal_2)
    print("equal_2_curried_filter")
    print(equal_2_curried_filter)
    equal_2_curried_filter_fibonacci_seq = equal_2_curried_filter(fibonacci_seq)
    print("equal_2_curried_filter_fibonacci_seq")

# Generated at 2022-06-14 04:05:40.516080
# Unit test for function curried_filter
def test_curried_filter():
    def bigger_than_5(value):
        return value > 5

    collection = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = [6, 7, 8, 9]

    assert curried_filter(bigger_than_5)(collection) == result



# Generated at 2022-06-14 04:05:50.084440
# Unit test for function curried_map
def test_curried_map():
    list_to_map = [1, 2, 3, 4, 5]

    curried_map_increase = curried_map(increase)
    curried_map_result = curried_map_increase(list_to_map)

    results: List[bool] = []
    for (mapped_value, list_value) in zip(curried_map_result, list_to_map):
        results.append(mapped_value == list_value + 1)

    assert all(results)



# Generated at 2022-06-14 04:05:53.579494
# Unit test for function find
def test_find():
    assert find([], lambda x: True) is None
    assert find(["hello", "world"], lambda x: True) == "hello"
    assert find(["hello", "world"], lambda x: x == "world") == "world"



# Generated at 2022-06-14 04:06:14.543173
# Unit test for function curried_filter
def test_curried_filter():
    assert [2, 3] == curried_filter(lambda x: x > 1, [1, 2, 3, 4])
    assert [3, 4] == curried_filter(lambda x: x > 2)([1, 2, 3, 4])



# Generated at 2022-06-14 04:06:17.161725
# Unit test for function find
def test_find():
    assert find([1, 2, 3, 4, 5], lambda x: x == 1) == 1
    assert find([1, 2, 3, 4, 5], lambda x: x == 8) == None



# Generated at 2022-06-14 04:06:18.480884
# Unit test for function curried_filter
def test_curried_filter():
    assert([2, 3, 4] == curried_filter(lambda x: x > 1)([1, 2, 3, 4])), 'test curried_filter failed'



# Generated at 2022-06-14 04:06:24.010665
# Unit test for function cond
def test_cond():
    test_functions = [
        (lambda x: x > 10, lambda x: x + 1),
        (lambda x: x < 10, lambda x: x - 1)
    ]

    cond_function = cond(test_functions)

    assert cond_function(11) == 12, "Should return 12"
    assert cond_function(9) == 8, "Should return 8"

# Generated at 2022-06-14 04:06:28.940817
# Unit test for function eq
def test_eq():
    """
    Test function eq, it should return true when call with same arguments.
    Test function eq, it should return false when call with different arguments.
    Test function eq curried, it should return true when call with same arguments.
    Test function eq curried, it should return false when call with different arguments.

    :returns: result of all tests
    :rtype: Boolean
    """
    assert eq(1, 1) is True
    assert eq(1, 2) is False
    assert eq(1)(1) is True
    assert eq(1)(2) is False



# Generated at 2022-06-14 04:06:36.684358
# Unit test for function cond
def test_cond():
    condition = [
        (lambda a, b: a == 1, lambda a, b: a + b),
        (lambda a, b: a == 2, lambda a, b: a * b),
        (lambda a, b: a == 3, lambda a, b: a ** b),
    ]

    assert cond(condition)(1, 2) == 3
    assert cond(condition)(2, 2) == 4
    assert cond(condition)(3, 2) == 9



# Generated at 2022-06-14 04:06:40.705142
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(increase, [1, 2, 3]) == [2, 3, 4]
    assert curried_map(increase)([1, 2, 3]) == [2, 3, 4]



# Generated at 2022-06-14 04:06:42.625479
# Unit test for function memoize
def test_memoize():
    assert memoize(lambda item: item * 2)(1) == 2
    assert memoize(lambda item: item * 2)(1) == 2



# Generated at 2022-06-14 04:06:50.115730
# Unit test for function find
def test_find():
    assert None == find([], lambda item: item == 1)
    assert 1 == find([1, 2, 3], lambda item: item == 1)
    assert 2 == find([1, 2, 3], lambda item: item == 2)
    assert 3 == find([1, 2, 3], lambda item: item == 3)
    assert None == find([1, 2, 3], lambda item: item == 4)



# Generated at 2022-06-14 04:06:56.910983
# Unit test for function curried_filter
def test_curried_filter():
    assert(
        curried_filter(lambda item: item > 3)([0,1,2,3,4,5]) ==
        [4,5]
    )
    assert(
        curried_filter(lambda item: item > 3)([]) ==
        []
    )
    assert(
        curried_filter(lambda item: item > 5)([0,1,2,3,4,5]) ==
        []
    )


# Generated at 2022-06-14 04:07:40.514093
# Unit test for function eq
def test_eq():
    assert eq(2, 3) == False
    assert eq(7, 7) == True
    assert eq(7, 2) == False
    assert eq("a", "a") == True
    assert eq("a", "b") == False


# Generated at 2022-06-14 04:07:46.773938
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]) == [2, 4]
    curried_filter_by_mod2 = curried_filter(identity)
    assert curried_filter_by_mod2([1, 2, 3, 4, 5]) == [1, 3, 5]
    assert curried_filter_by_mod2([2, 4, 6, 8]) == [2, 4, 6, 8]

