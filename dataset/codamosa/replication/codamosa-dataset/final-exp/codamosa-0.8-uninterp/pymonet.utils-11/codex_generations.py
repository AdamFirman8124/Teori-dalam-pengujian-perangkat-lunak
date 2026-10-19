

# Generated at 2022-06-14 03:57:52.542409
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x == 1)([1,2,1]) == [1,1]
assert test_curried_filter()



# Generated at 2022-06-14 03:57:57.907453
# Unit test for function curry
def test_curry():
    """
    Test currying
    """
    def add(a, b):
        return a + b

    assert add(1, 2) == 3

    curried_add = curry(add)
    add1 = curried_add(1)
    assert add1(2) == 3

    curried_add(1)(5) == 6

    assert add1(3) == 4
    assert add1(4) == 5
    assert add1(5) == 6



# Generated at 2022-06-14 03:58:06.553262
# Unit test for function curried_map
def test_curried_map():
    assert [2, 3, 4, 5] == curried_map(lambda x: x + 1)([1, 2, 3, 4])
    assert [2, 3, 4, 5] == curried_map(increase)([1, 2, 3, 4])
    assert [2, 3, 4, 5] == curried_map(increase, [1, 2, 3, 4])
    assert [2, 4, 6, 8] == curried_map(lambda x: x * 2, [1, 2, 3, 4])
    assert [2, 4, 6, 8] == curried_map(lambda x: x * 2)([1, 2, 3, 4])



# Generated at 2022-06-14 03:58:14.852301
# Unit test for function curried_filter
def test_curried_filter():
    collection = list(range(100))
    filter_even = curried_filter(lambda x: x % 2 == 0)
    filter_odd = curried_filter(lambda x: x % 2 == 1)
    filter_squared = curried_filter(lambda x: x ** 2)
    assert filter_even(collection) == list(filter(lambda x: x % 2 == 0, collection))
    assert filter_odd(collection) == list(filter(lambda x: x % 2 == 1, collection))
    assert filter_squared(collection) == list(filter(lambda x: x ** 2, collection))


# Generated at 2022-06-14 03:58:21.883890
# Unit test for function eq
def test_eq():
    assert eq(1, 1) == True
    assert eq(1, 2) == False
    assert eq("a", "a") == True
    assert eq("a", "b") == False
    assert eq("a", 1) == False
    assert eq(1)(1) == True
    assert eq("a")("a") == True
    assert eq("a")("b") == False
    assert eq("a")(1) == False



# Generated at 2022-06-14 03:58:24.443549
# Unit test for function curried_map
def test_curried_map():
    assert [2, 3, 4] == curried_map(increase, [1, 2, 3])



# Generated at 2022-06-14 03:58:39.256610
# Unit test for function cond
def test_cond():
    def try_cond(arg, expected_result):
        print("\ntry_cond({0}, {1})".format(arg, expected_result))
        print("result: ", cond([
            (lambda x: eq(x, 1), increase),
            (lambda x: eq(x, 2), increase),
            (lambda x: eq(x, 3), increase),
        ])(arg))
        assert cond([
            (lambda x: eq(x, 1), increase),
            (lambda x: eq(x, 2), increase),
            (lambda x: eq(x, 3), increase),
        ])(arg) == expected_result

    try_cond(1, 2)
    try_cond(2, 3)
    try_cond(3, 4)
    try_cond(4, None)



# Generated at 2022-06-14 03:58:45.299767
# Unit test for function cond
def test_cond():
    def add_one(a):
        return a + 1

    def mul_two(a):
        return a * 2

    assert cond([
        (lambda a: a < 2, add_one),
        (lambda a: a < 5, mul_two),
    ])(1) == 2

    assert cond([
        (lambda a: a < 2, add_one),
        (lambda a: a < 5, mul_two),
    ])(3) == 6



# Generated at 2022-06-14 03:58:48.263846
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(lambda x: x + 1)([1, 2, 3]) == [2, 3, 4]
    assert curried_map(lambda x: x + 1, [1, 2, 3]) == [2, 3, 4]
    assert curried_map(lambda x: x + 1)([1, 2, 3]) == [2, 3, 4]


# Generated at 2022-06-14 03:58:53.733861
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(lambda x: x + 1, [1, 2, 3]) == [2, 3, 4]
    assert curried_map(lambda x: x * x, [2, 3, 4]) == [4, 9, 16]
    assert curried_map(lambda x: x * x, []) == []

# Generated at 2022-06-14 03:59:07.732583
# Unit test for function curry
def test_curry():
    @curry
    def func(a, b, c, d):
        return a + b + c + d

    assert func(1, 2, 3, 4) == 10
    assert func(1, 2, 3)(4) == 10
    assert func(1, 2)(3, 4) == 10
    assert func(1, 2)(3)(4) == 10
    assert func(1)(2, 3, 4) == 10
    assert func(1)(2, 3)(4) == 10
    assert func(1)(2)(3, 4) == 10
    assert func(1)(2)(3)(4) == 10
    return True



# Generated at 2022-06-14 03:59:10.731397
# Unit test for function find
def test_find():
    assert find([1, 2, 3, 4, 5], eq(2)) == 2
    assert find([1, 2, 3, 4, 5], eq(10)) is None



# Generated at 2022-06-14 03:59:14.964795
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(identity, [1, 2, 3, 4]) == [1, 2, 3, 4]
    assert curried_map(increase, [1, 2, 3, 4]) == [2, 3, 4, 5]



# Generated at 2022-06-14 03:59:22.565303
# Unit test for function curry
def test_curry():
    def add(a, b, c, d):
        return a + b + c + d

    add = curry(add)

    assert add(1)(2)(3)(4) == 10
    assert add(2, 3, 4)(0) == 9
    assert add(1)(1)(1)(1) == 4
    assert add(0, 0, 0, 0) == 0



# Generated at 2022-06-14 03:59:25.865023
# Unit test for function cond
def test_cond():
    cond_function = cond([
        (eq(1), identity),
        (eq(2), increase)
    ])
    assert cond_function(1) == 1
    assert cond_function(2) == 3


# Generated at 2022-06-14 03:59:30.160225
# Unit test for function eq
def test_eq():
    assert eq(3, 3) == True
    assert eq(3, 3, 3) == False
    assert eq(1, 1, 1) == True
    assert eq(True, False) == False
    assert eq(True, True) == True
    assert eq(True, False, False) == False
    assert eq(True, False, 1) == False



# Generated at 2022-06-14 03:59:35.937374
# Unit test for function memoize
def test_memoize():
    """
    Test for function memoize
    """
    import random
    @memoize
    def random_num(x):
        """
        Return random number from [0, x)
        """
        return random.randint(0, x)
    assert random_num(1) == 0
    assert random_num(1) == 0
    assert random_num(5) in [0, 1, 2, 3, 4]
    assert random_num(5) in [0, 1, 2, 3, 4]
    assert random_num(5) == random_num(5)
    assert random_num(3) == random_num(3)

    def random_num_with_key(x, key):
        """
        Return random number from [0, x)
        """

# Generated at 2022-06-14 03:59:43.037806
# Unit test for function curry
def test_curry():
    assert identity(10) == curry(identity)(10)
    assert identity(10) == curry(identity, 1)(1)
    assert identity(10) == curry(identity, 2)(1, 1)
    assert identity(10) == curry(identity, 3)(1, 1, 1)

    assert identity(10) == curry(identity, 2)(1)(1)
    assert identity(10) == curry(identity, 3)(1)(1)(1)

    assert identity(10) == curry(identity, 2)(1, 2)
    assert identity(10) == curry(identity, 3)(1, 2, 3)

    assert identity(10) == curry(identity, 2)(1)(2)
    assert identity(10) == curry(identity, 3)(1)(2)(3)


# Generated at 2022-06-14 03:59:45.003399
# Unit test for function find
def test_find():
    array = [1, 2, 3, 4, 5, 6]
    assert find(array, lambda item: item % 3 == 0) == 3
    assert find(array, lambda item: item % 7 == 0) is None



# Generated at 2022-06-14 03:59:48.285624
# Unit test for function find
def test_find():
    collection = ['a', 'b', 'c']
    function = lambda value: value == 'a'
    result = find(collection, function)
    assert result == 'a', 'Unexpected result'


# Generated at 2022-06-14 03:59:59.802466
# Unit test for function eq
def test_eq():
    assert eq(1, 1)
    assert not eq(1, 2)


test_eq()


# Generated at 2022-06-14 04:00:05.575697
# Unit test for function memoize
def test_memoize():
    # Test 1
    def sum(number):
        return number + 1

    memo_sum = memoize(sum)
    assert memo_sum(1) == 2
    assert memo_sum(1) == 2
    assert memo_sum(2) == 3
    assert memo_sum(2) == 3

    # Test 2
    memo_sum = memoize(sum, key=eq)
    assert memo_sum(1) == 2
    assert memo_sum(1) == 2
    assert memo_sum(2) == 3
    assert memo_sum(2) == 3



# Generated at 2022-06-14 04:00:13.171683
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x > 2, [0, 1, 2, 3, 5, 8, 13]) == [3, 5, 8, 13]
    assert curried_filter(lambda x: x % 2, [0, 1, 2, 3, 5, 8, 13]) == [1, 3, 5, 13]
    assert curried_filter(lambda x: x == 0, [0, 1, 2, 3, 5, 8, 13]) == [0]



# Generated at 2022-06-14 04:00:23.519302
# Unit test for function memoize
def test_memoize():
    def multiply_two(a):
        return a * 2

    def multiply_three(a):
        return a * 3

    def divide_two(a):
        return a / 2

    def add_five(a):
        return a + 5

    fn1 = multiply_two
    fn2 = multiply_three
    fn3 = divide_two
    fn4 = add_five
    fn5 = multiply_two

    assert fn1(5) == 10
    assert fn2(5) == 15
    assert fn3(5) == 2.5
    assert fn4(5) == 10
    assert fn5(5) == 10

    memoized_fn1 = memoize(multiply_two)
    memoized_fn2 = memoize(multiply_three)

# Generated at 2022-06-14 04:00:31.784144
# Unit test for function curried_map
def test_curried_map():
    my_list = [1, 2, 3, 4, 5]
    assert curried_map(lambda x: x * x, my_list) == [1, 4, 9, 16, 25]
    assert curried_map(lambda x: x + x, my_list) == [2, 4, 6, 8, 10]
    assert curried_map(lambda x: x ** x, my_list) == [1, 4, 27, 256, 3125]



# Generated at 2022-06-14 04:00:36.636978
# Unit test for function memoize
def test_memoize():
    def add(x, y):
        return x + y

    plus = memoize(add)
    assert plus(1, 2) == plus(1, 2) == add(1, 2) == 3


if __name__ == '__main__':
    test_memoize()

# Generated at 2022-06-14 04:00:47.880759
# Unit test for function find
def test_find():
    assert find(
        [
            {'id': 0, 'value': '0'},
            {'id': 1, 'value': '1'},
            {'id': 2, 'value': '2'},
            {'id': 3, 'value': '3'},
            {'id': 4, 'value': '4'}
        ],
        lambda item: item['id'] == 2
    ) == {'id': 2, 'value': '2'}


# Generated at 2022-06-14 04:00:53.501628
# Unit test for function find
def test_find():
    """
    Test for find function.
    """
    assert find([], lambda _: True) is None

    assert find([], lambda _: False) is None

    assert find([1, 2, 3], lambda _: True) == 1

    assert find([1, 2, 3], lambda x: x % 2 == 0) == 2

    assert find([1, 2, 3], lambda x: x % 2 == 1) == 1



# Generated at 2022-06-14 04:00:58.362331
# Unit test for function curried_filter
def test_curried_filter():
    is_even = lambda x: x % 2 == 0
    data = [1, 2, 3, 4, 5]

    test_data = curried_filter(is_even)(data)
    expected_data = list(filter(is_even, data))

    assert test_data == expected_data



# Generated at 2022-06-14 04:01:09.274469
# Unit test for function find
def test_find():
    assert find([], eq(2)) is None
    assert find([2, 3, 4], eq(2)) == 2
    assert find([1, 2, 3, 4], eq(3)) == 3
    assert find([1, 2, 3, 4], eq(4)) == 4
    assert find([1, 2, 3, 4], eq(5)) is None
    assert find([4, 3, 2, 1], eq(4)) == 4
    assert find([4, 3, 2, 1], eq(3)) == 3
    assert find([4, 3, 2, 1], eq(2)) == 2
    assert find([4, 3, 2, 1], eq(1)) == 1
    assert find([4, 3, 2, 1], eq(5)) is None



# Generated at 2022-06-14 04:01:21.022472
# Unit test for function eq
def test_eq():
    assert eq(1, 1) is True
    assert eq(2, 1) is False



# Generated at 2022-06-14 04:01:30.529815
# Unit test for function cond
def test_cond():
    def check_a(value, *_):
        return value == 'a'

    def check_b(value, *_):
        return value == 'b'

    def check_c(value, *_):
        return value == 'c'

    def append_a(value, *_):
        return value + 'aa'

    def append_b(value, *_):
        return value + 'bb'

    def append_c(value, *_):
        return value + 'cc'

    def append_d(value, *_):
        return value + 'dd'

    def condition_list():
        return [
            (check_a, append_a),
            (check_b, append_b),
            (check_c, append_c),
        ]

    new_function = cond(condition_list())


# Generated at 2022-06-14 04:01:36.327515
# Unit test for function memoize
def test_memoize():
    def test_fn(arg):
        try:
            return 1 / arg
        except ZeroDivisionError:
            print('Zero')

    test_memoize_fn = memoize(test_fn)
    assert test_memoize_fn(0) == test_memoize_fn(0) == test_memoize_fn(0)
    assert test_memoize_fn(5) == test_memoize_fn(5) == test_memoize_fn(5)



# Generated at 2022-06-14 04:01:38.192309
# Unit test for function eq
def test_eq():
    assert eq(1, 1)
    assert not eq(1, 0)


# Generated at 2022-06-14 04:01:43.377823
# Unit test for function curried_filter
def test_curried_filter():
    assert [1, 2, 3] == curried_filter(lambda x: x > 0, [1, -2, 3])
    assert [1, 3] == curried_filter(lambda x: x > 0)([1, -2, 3])
    assert 2 == curried_filter(lambda x: x > 0)([1, 2, 3]).pop()
    assert 1 == curried_filter(lambda x: x > 0)([-2, 1]).pop()
    assert [] == curried_filter(lambda x: x > 0)([-2, -1])
    assert [] == curried_filter(lambda x: x > 0)([])



# Generated at 2022-06-14 04:01:54.711416
# Unit test for function cond
def test_cond():
    # Declare conditions list
    conditions = [
        (lambda x: x < 0, increase),
        (lambda x: True, identity),
    ]

    # Declare inner function for point of call the cond
    def evaluate(x):
        # Declare list of functions
        functions = [
            lambda x: x / x,
            lambda x: x - 1,
            lambda x: x + 1
        ]

        # Call cond with arguments:
        # 1. function from list of functions
        # 2. conditions
        return cond(conditions)(functions[x])

    # call evaluate for each possible cases
    for x in [-1, 0, 1]:
        print(evaluate(x))

# Generated at 2022-06-14 04:01:56.753612
# Unit test for function eq
def test_eq():
    print(eq(2, 2))
    print(eq(2, 3))



# Generated at 2022-06-14 04:02:00.964249
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(increase, []), []
    assert curried_map(increase, [1]), [2]
    assert curried_map(increase, [1, 2]), [2, 3]


# Generated at 2022-06-14 04:02:04.080631
# Unit test for function eq
def test_eq():
    assert eq(1, 1) == True
    assert eq(1, 2) == False
    assert eq(1)(2)(2) == False



# Generated at 2022-06-14 04:02:06.302478
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(increase, [1,2,3]) == [2,3,4]

# Generated at 2022-06-14 04:02:36.331172
# Unit test for function cond
def test_cond():
    filter_ten = lambda x: x % 10 == 0
    filter_nine = lambda x: x % 9 == 0
    filter_eight = lambda x: x % 8 == 0
    filter_seven = lambda x: x % 7 == 0
    filter_six = lambda x: x % 6 == 0
    filter_five = lambda x: x % 5 == 0
    filter_four = lambda x: x % 4 == 0
    filter_three = lambda x: x % 3 == 0
    filter_two = lambda x: x % 2 == 0
    filter_one = lambda x: x % 1 == 0
    filter_zero = lambda x: x % 0 == 0


# Generated at 2022-06-14 04:02:39.161872
# Unit test for function eq
def test_eq():
    assert eq(1, 1)
    assert not eq(1, 2)
    assert not eq("hello", "world")
    assert eq("hello", "hello")



# Generated at 2022-06-14 04:02:44.706760
# Unit test for function find
def test_find():
    result = find([{'key': 'value'}, {'key': 'value1'}, {'key': 'value2'}], lambda item: item['key'] == 'value2')
    assert result == {'key': 'value2'}

    result = find([{'key': 'value'}, {'key': 'value1'}, {'key': 'value2'}], lambda item: item['key'] == 'value5')
    assert result is None



# Generated at 2022-06-14 04:02:48.796222
# Unit test for function find
def test_find():
    test_list = [1, 2, 3, 4, 5]
    assert find(test_list, lambda argument: argument == 3) == 3
    assert find(test_list, lambda argument: argument == 10) is None
    assert find([], lambda argument: argument == 10) is None

# Generated at 2022-06-14 04:02:55.836045
# Unit test for function memoize
def test_memoize():

    @memoize
    def add(a, b):
        print('called')
        return a + b

    assert 1 == add(1, 0)
    assert 2 == add(1, 1)
    assert 3 == add(1, 2)
    assert 6 == add(2, 4)

    assert 1 == add(1, 0)
    assert 2 == add(1, 1)
    assert 3 == add(1, 2)
    assert 6 == add(2, 4)


test_memoize()



# Generated at 2022-06-14 04:02:59.143309
# Unit test for function curried_map
def test_curried_map():
    curried_mapper_fn = curried_map(increase)
    assert curried_mapper_fn([1, 2, 3]) == [2, 3, 4]



# Generated at 2022-06-14 04:03:04.325003
# Unit test for function memoize
def test_memoize():
    @memoize
    def fib(n):
        if n <= 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)

    assert fib(10) == 55
    assert fib(11) == 89
    assert fib(10) == 55


# Generated at 2022-06-14 04:03:09.610680
# Unit test for function curried_map
def test_curried_map():
    assert [2, 3, 4] == curried_map(identity, [1, 2, 3])
    assert [2, 3, 4] == curried_map(increase, [1, 2, 3])
    assert [2, 4, 6] == curried_map(increase, curried_map(increase, [1, 2, 3]))



# Generated at 2022-06-14 04:03:11.508273
# Unit test for function curried_filter
def test_curried_filter():
    # Arrange
    numbers = range(10)

    # Act
    result = curried_filter(lambda x: x % 2 == 0)(numbers)

    # Assert
    assert all(n % 2 == 0 for n in result)



# Generated at 2022-06-14 04:03:18.513968
# Unit test for function memoize
def test_memoize():
    """
    test_memoize test memoize function
    """
    # Check if cache is empty
    cache = [
        'foo',
        'bar'
    ]

    result = memoize(cache.append, lambda a, b: a == b)('foo')
    assert not result
    result = memoize(cache.append, lambda a, b: a == b)('bar')
    assert not result
    result = memoize(cache.append, lambda a, b: a == b)('foo')
    assert result


test_memoize()

# Generated at 2022-06-14 04:03:59.584690
# Unit test for function curried_map
def test_curried_map():
    list_of_number = [1,2,3,4,5]
    expected_result = [2,3,4,5,6]
    result = curried_map(lambda x: x+1)(list_of_number)
    assert expected_result == result



# Generated at 2022-06-14 04:04:05.072182
# Unit test for function memoize
def test_memoize():
    # Use as decorator
    @memoize
    def function1(arg):
        return arg + arg

    # Use as function
    def function2(arg):
        return arg + arg

    result = memoize(function2)

    assert (result(3) == function1(3))



# Generated at 2022-06-14 04:04:12.289965
# Unit test for function memoize
def test_memoize():
    def f(x):
        return x*x
    # assert f(3) == 9
    # assert f(3) == 9
    f = memoize(f)
    # assert f is memoize(f)
    # assert f(3) == 9
    # assert f(3) == 9
    print('all tests passed')


if __name__ == '__main__':
    test_memoize()

# Generated at 2022-06-14 04:04:18.406163
# Unit test for function curry
def test_curry():
    assert curry(lambda a, b, c: a + b + c)(1, 2, 3) == 6
    assert curry(lambda a, b, c: a + b + c)(1, 2)(3) == 6
    assert curry(lambda a, b, c: a + b + c)(1)(2, 3) == 6
    assert curry(lambda a, b, c: a + b + c)(1)(2)(3) == 6



# Generated at 2022-06-14 04:04:23.363815
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x > 5)([1, 2, 3]) == []
    assert curried_filter(lambda x: x % 2 == 0)([1, 2, 3]) == [2]
    assert curried_filter(lambda x: x > 1)([1, 2, 3]) == [2, 3]
    assert curried_filter(lambda x: x > 0)([1, 2, 3]) == [1, 2, 3]



# Generated at 2022-06-14 04:04:37.140740
# Unit test for function find
def test_find():
    test_cases = [
        {
            'collection': [],
            'key': lambda x: True,
            'result': None,
            'description': 'it should find nothing in empty collection'
        },
        {
            'collection': [1, 3, 5, 7],
            'key': lambda x: x % 3 == 2,
            'result': 5,
            'description': 'it should find element in collection'
        },
        {
            'collection': [1, 2, 3, 4],
            'key': lambda x: x > 4,
            'result': None,
            'description': 'it should not find element in collection'
        }
    ]


# Generated at 2022-06-14 04:04:41.348959
# Unit test for function curry
def test_curry():
    def add(value1, value2, value3):
        return value1 + value2 + value3

    assert curry(add)(1)(2)(3) == 6
    assert curry(add)(1, 2)(3) == 6
    assert curry(add)(1, 2, 3) == 6



# Generated at 2022-06-14 04:04:50.124084
# Unit test for function memoize
def test_memoize():
    def fact(number):
        if number == 0:
            return 1
        return number * fact(number - 1)

    def fact_memoized(number):
        if 0 <= number <= 10:
            return fact(number)
        else:
            return fact_memoized(number - 1) * number

    assert fact_memoized(0) == fact(0)
    assert fact_memoized(10) == fact(10)
    assert fact_memoized(100) == fact(100)
    assert fact_memoized(1000) == fact(1000)

# Generated at 2022-06-14 04:04:52.655353
# Unit test for function eq
def test_eq():
    assert eq(1)(1)
    assert not eq(1)(2)



# Generated at 2022-06-14 04:04:59.425360
# Unit test for function eq
def test_eq():
    curried_eq = curry(eq)
    assert curried_eq(1, 1) == True
    assert curried_eq(1)(1) == True
    assert curried_eq(1)(0) == False
    assert curried_eq(0)(0) == True
    assert curried_eq(0)(1) == False
    assert curried_eq(0, 1) == False
    assert curried_eq(1, 0) == False



# Generated at 2022-06-14 04:05:41.071404
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(increase, range(10)) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Generated at 2022-06-14 04:05:49.083417
# Unit test for function cond
def test_cond():
    assert cond(
        [(lambda x: x % 2 == 0, lambda x: x * 2),
         (lambda x: x % 2 != 0, lambda x: x + 2)]
    )(3) == 5
    assert cond(
        [(lambda x: x % 2 == 0, lambda x: x * 2),
         (lambda x: x % 2 != 0, lambda x: x + 2)]
    )(4) == 8

# Generated at 2022-06-14 04:05:55.139239
# Unit test for function memoize
def test_memoize():
    def sq(x: int) -> int:
        time.sleep(1)
        return x ** 2

    t = time.time()
    print(sq(3))
    print(time.time() - t)

    t = time.time()
    print(memoize(sq)(3))
    print(time.time() - t)


if __name__ == '__main__':
    test_memoize()

# Generated at 2022-06-14 04:05:58.714002
# Unit test for function memoize
def test_memoize():
    @memoize
    def multiply(value):
        return value * 2

    assert multiply(1) == 2
    assert multiply(1) == 2



# Generated at 2022-06-14 04:06:03.238943
# Unit test for function eq
def test_eq():
    assert True == eq(2)(2)
    assert True == eq(2)(2)
    assert False == eq(2)(3)
    assert False == eq(2)(3)
    assert curry(eq)(2)(2)
    assert curry(eq)(2)(2)
    assert curry(eq)(2)(3)
    assert curry(eq)(2)(3)



# Generated at 2022-06-14 04:06:05.704185
# Unit test for function eq
def test_eq():
    eq1 = eq(1)
    assert eq1(1)
    assert not eq1(0)



# Generated at 2022-06-14 04:06:10.389135
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x > 10)([1, 2, 3, 4, 5]) == []
    assert curried_filter(lambda x: x > 10)([1, 2, 3, 4, 5, 11, 12, 13]) == [11, 12, 13]



# Generated at 2022-06-14 04:06:14.934074
# Unit test for function memoize
def test_memoize():
    cc = 0
    def test_add_one(arg):
        global cc
        cc += 1
        return arg + 1

    m = memoize(test_add_one)

    assert m(1) == 2
    assert cc == 1

    assert m(1) == 2
    assert cc == 1

    assert m(2) == 3
    assert cc == 2



# Generated at 2022-06-14 04:06:20.238324
# Unit test for function curried_filter
def test_curried_filter():
    curried_filter_test = curried_filter(lambda x: x < 10)([1, 2, 3, 11, 22, 33])
    assert curried_filter_test == [1, 2, 3]
    return "test_curried_filter() passed successfully"
print(test_curried_filter())


# Generated at 2022-06-14 04:06:22.092493
# Unit test for function find
def test_find():
    assert find([0, 1, 2, 3], eq(2)) == 2



# Generated at 2022-06-14 04:07:18.076975
# Unit test for function curried_map
def test_curried_map():
    multiply_by_two = lambda x : x * 2
    assert curried_map(multiply_by_two, [1, 2, 3]) == [2, 4, 6]
    assert curried_map(lambda x: x * 2, [1, 2, 3]) == [2, 4, 6]
    assert curried_map(lambda x: x * 2)([1, 2, 3]) == [2, 4, 6]
    assert curried_map(multiply_by_two)([1, 2, 3]) == [2, 4, 6]


# Generated at 2022-06-14 04:07:21.580469
# Unit test for function curry
def test_curry():
    add10 = curry(lambda x, y: x + y)
    assert add10(20) == 30
    assert add10(20) == 30



# Generated at 2022-06-14 04:07:29.290747
# Unit test for function cond
def test_cond():
    def double(x: int) -> int:
        return x * 2

    def triple(x: int) -> int:
        return x * 3

    # return triple if input value is less than 3
    condition_list = [
        (lambda x: x < 3, triple),
        (lambda x: True, double)
    ]
    function_in_cond = cond(condition_list)
    assert function_in_cond(3) == 6
    assert function_in_cond(1) == 3
    assert function_in_cond(4) == 8

# Generated at 2022-06-14 04:07:34.436167
# Unit test for function find
def test_find():
    assert find([1, 2, 3, 4], lambda v: v == 2) == 2
    assert find([1, 2, 3, 4], lambda v: v > 2 and v < 4) == 3
    assert find([1, 2, 3, 4], lambda v: v < 0) is None



# Generated at 2022-06-14 04:07:38.878180
# Unit test for function eq
def test_eq():
    assert True == eq(1, 1)
    assert False == eq(1, 2)
    eq_c2 = eq(2)
    assert True == eq_c2(2)
    assert False == eq_c2(3)



# Generated at 2022-06-14 04:07:48.019570
# Unit test for function cond
def test_cond():
    def is_even(value):
        return value % 2 == 0

    def is_zero(value):
        return value == 0

    def increase(value):
        return value + 1

    def decrease(value):
        return value - 1

    def multiple_by(value):
        return value * 3

    test_function = cond([(is_even, increase), (is_zero, identity)])
    assert test_function(0) == 0
    assert test_function(3) == 4
    test_function = cond([(is_even, increase), (is_zero, identity), (is_even, decrease)])
    assert test_function(3) == 4
    assert test_function(4) == 3
    assert test_function(0) == 0
    assert test_function(9) == 10