

# Generated at 2022-06-14 03:57:55.016878
# Unit test for function eq
def test_eq():
    assert eq(1, 1)
    assert not eq(1, 2)

# Unit test fot function identity

# Generated at 2022-06-14 03:58:03.641820
# Unit test for function find
def test_find():
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __eq__(self, other):
            if isinstance(other, Point):
                return self.x == other.x and self.y == other.y
            return False

    p1 = Point(0, 0)
    p2 = Point(0, 1)
    p3 = Point(1, 1)
    p4 = Point(0, 0)

    assert find([p1, p2, p3], lambda point: point.x == 0) == p1
    assert find([p1, p2, p3], lambda point: point.x == 1) == p3
    assert find([p1, p2, p3], lambda point: point.x == 2) is None
    assert find

# Generated at 2022-06-14 03:58:06.487912
# Unit test for function find
def test_find():
    """
    Test for function find.
    """
    collection = [2, 3, 4]
    assert find(collection, lambda x: x == 2) == 2
    assert find(collection, lambda x: x == 5) is None



# Generated at 2022-06-14 03:58:12.900848
# Unit test for function curried_filter
def test_curried_filter():
    list = [1, 2, 3, 4, 5]
    assert curried_filter(lambda x: x % 2 == 0, list) == [2, 4]
    assert curried_filter(lambda x: x % 2 != 0, list) == [1, 3, 5]
    assert curried_filter(lambda x: x % 2 == 0)(list) == [2, 4]



# Generated at 2022-06-14 03:58:14.891249
# Unit test for function eq
def test_eq():
    assert eq(1, 2) == False
    assert eq(1, 1) == True
    assert eq(1)(1) == True



# Generated at 2022-06-14 03:58:23.478331
# Unit test for function memoize
def test_memoize():
    import time
    import random

    @memoize
    def my_fn(value):
        time.sleep(random.randint(10, 100) / 1000)
        return value * 2

    assert my_fn(5) == 10
    assert my_fn(5) == 10
    assert my_fn(10) == 20
    assert my_fn(10) == 20
    assert my_fn(7) == 14
    assert len(my_fn.__closure__[0].cell_contents) == 3
    assert my_fn(7) == 14

# Generated at 2022-06-14 03:58:30.268962
# Unit test for function curried_map
def test_curried_map():
    # TODO: need to write tests
    pass


# Generated at 2022-06-14 03:58:37.532057
# Unit test for function curried_filter
def test_curried_filter():
    #type checking
    assert callable(curried_filter)
    assert isinstance(curried_filter(identity, [1, 2, 3, 4, 5]), list)



# Generated at 2022-06-14 03:58:41.585636
# Unit test for function curried_filter
def test_curried_filter():
    items = [1, 2, 3, 4, 5, 6]
    to_double = lambda x: x * 2
    doubled_over_3 = curried_filter(
        curry(lambda x: x > 3),
        curried_map(to_double, items)
    )
    assert doubled_over_3 == [8, 10, 12]



# Generated at 2022-06-14 03:58:46.507115
# Unit test for function cond
def test_cond():
    zero_num = 0
    not_zero_num = 1
    list_to_int = cond([
        (eq(0), lambda: 0),
        (eq(1), lambda: 1),
        (eq(2), lambda: 2)
    ])
    assert list_to_int(zero_num) == 0
    assert list_to_int(not_zero_num) == 1
    assert list_to_int(not_zero_num+1) == 2



# Generated at 2022-06-14 03:58:57.132369
# Unit test for function memoize
def test_memoize():
    @memoize
    def factorial(n):
        if n < 2:
            return n
        return n * factorial(n-1)

    assert factorial(7) == 5040
    assert memoize(increase, eq)(1) == 2

# Generated at 2022-06-14 03:59:02.748982
# Unit test for function memoize
def test_memoize():
    assert memoize(increase)(1) == 2
    assert memoize(increase)(1) == 2
    assert memoize(increase)(2) == 3
    assert memoize(increase)(2) == 3
    assert memoize(increase)(1) == 2
    assert memoize(identity)(2) == 2
    assert memoize(identity)(1) == 1



# Generated at 2022-06-14 03:59:06.906416
# Unit test for function eq
def test_eq():
    assert eq(1, 1)
    assert not eq(1, 0)
    assert curry(lambda a, b: eq(a, b))(1)(1)
    assert not curry(lambda a, b: eq(a, b))(1)(0)



# Generated at 2022-06-14 03:59:17.153926
# Unit test for function eq
def test_eq():
    assert eq(1, 2) is not True
    assert eq(1, 2) is False
    assert eq(1, 1) is True
    assert eq(1, 1.0) is True
    assert eq(2, 1) is not True
    assert eq(2, 1) is False
    assert eq('a', 2) is not True
    assert eq('a', 2) is False
    assert eq('a', 'a') is True
    assert eq('a', 'b') is not True
    assert eq('a', 'b') is False
    assert eq((1, 2), (1, 2)) is True
    assert eq([1, 2], [1, 2]) is True
    assert eq(1, 1, 1) is False



# Generated at 2022-06-14 03:59:23.201135
# Unit test for function curry
def test_curry():
    assert curry(lambda a, b: a+b, 2)(2, 2) == 4
    assert curry(lambda x: x + 1, 1)(1) == 2
    assert curry(lambda a, b, c, d, e: a+b+c+d+e, 5)(1, 2, 3, 4, 5) == 15



# Generated at 2022-06-14 03:59:27.426928
# Unit test for function memoize
def test_memoize():
    memoized_sum = memoize(sum)
    assert memoized_sum(1, 2, 3) == sum(1, 2, 3)
    assert memoized_sum(1, 2, 3) == sum(1, 2, 3)


memoize_sum = memoize(sum)



# Generated at 2022-06-14 03:59:31.945418
# Unit test for function curry
def test_curry():
    def sum_of_numbers(a, b, c):
        return a + b + c

    assert curry(sum_of_numbers)(1, 2, 3) == 6
    assert curry(sum_of_numbers)(1)(2, 3) == 6
    assert curry(sum_of_numbers)(1, 2)(3) == 6
    assert curry(sum_of_numbers)(1)(2)(3) == 6



# Generated at 2022-06-14 03:59:43.459090
# Unit test for function curried_map
def test_curried_map():
    """
    Test curried_map function.
    """
    assert curried_map({'id': 6})([{}, {'id': 1}, {'id': 6, 'name': 'test'}, {'id': 1}, {'id': 8, 'name': 'test'}]) == [
        {}, {'id': 1}, {'id': 7}, {'id': 2}, {'id': 9}]

# Generated at 2022-06-14 03:59:45.301686
# Unit test for function memoize
def test_memoize():
    fn = memoize(lambda x: x**2)
    [fn(x) for x in range(3)]



# Generated at 2022-06-14 03:59:55.203910
# Unit test for function cond
def test_cond():
    def add_1(x):
        return x + 1

    def double(x):
        return x * 2

    def triple(x):
        return x * 3


# Generated at 2022-06-14 04:00:01.011899
# Unit test for function find
def test_find():
    assert find([1, 2, 3, 4], lambda x: x > 2) == 3



# Generated at 2022-06-14 04:00:03.604669
# Unit test for function memoize
def test_memoize():
    def add(value):
        return value + 1

    result = memoize(add)(3)
    assert result == 4


if __name__ == '__main__':
    test_memoize()

# Generated at 2022-06-14 04:00:05.973560
# Unit test for function find
def test_find():
    assert find(['a', 'b', 'c'], eq('b')) == 'b'

# Generated at 2022-06-14 04:00:11.289574
# Unit test for function curry
def test_curry():
    add = lambda x, y: x + y
    add1 = curry(add)
    add3 = add1(3)
    assert add3(4) == add(3, 4)
    assert add3(5) == add(3, 5)



# Generated at 2022-06-14 04:00:13.077670
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(lambda x: x * 2)([1, 2, 3]) == [2, 4, 6]

# Generated at 2022-06-14 04:00:23.032780
# Unit test for function cond
def test_cond():
    assert cond([
        (lambda x: x == 'foo', lambda: 'bar'),
        (lambda x: x == 'baz', lambda: 'qux'),
    ])('foo') == 'bar'
    assert cond([
        (lambda x: x == 'foo', lambda: 'bar'),
        (lambda x: x == 'baz', lambda: 'qux'),
    ])('baz') == 'qux'
    assert (cond([(lambda x: x == 'foo', lambda: 'bar'),
                  (lambda x: x == 'baz', lambda: 'qux'),
                  (lambda x: x == 'qwerty', lambda: 'uiop')])('qwerty') ==
            'uiop')

# Generated at 2022-06-14 04:00:27.969196
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x < 5, [1, 2, 3, 4, 5, 6, 7])(1) == [2, 3, 4, 5]


# Generated at 2022-06-14 04:00:39.410779
# Unit test for function eq
def test_eq():
    assert(eq(3, 3) == True)
    assert(eq(3, 4) == False)
    assert(eq(3, '3') == False)
    assert(eq('3', '3') == True)
    assert(eq(True, False) == False)
    assert(eq(True, True) == True)
    assert(eq('a', 'b') == False)
    assert(eq([1, 2], [1, 2]) == True)
    assert(eq([1, 2], [2, 1]) == False)
    assert(eq(('a', 'b'), ('a', 'b')) == True)
    assert(eq(('a', 'b'), ('b', 'a')) == False)
    assert(eq({ 1, 2}, { 1, 2} ) == True)

# Generated at 2022-06-14 04:00:51.261354
# Unit test for function memoize
def test_memoize():
    """
    Test function memoize.
    """
    import random
    import timeit

    def slow_multiply(arg):
        """
        Slow multiply function.

        :param arg:
        :type arg: Int
        :returns:
        :rtype: Int
        """
        return arg * random.randrange(1, 10)

    def multiply(arg: int) -> int:
        """
        Multiply function.

        :param arg:
        :type arg: Int
        :returns:
        :rtype: Int
        """
        return arg * 5

    memoized_multiply = memoize(multiply)

    assert multiply(5) == memoized_multiply(5)
    assert timeit.timeit(lambda: multiply(5), number=100000) > timeit.time

# Generated at 2022-06-14 04:00:55.732923
# Unit test for function curried_map
def test_curried_map():
    mapped = curried_map(lambda x: x + 1, [1, 2, 3])
    assert mapped == [2, 3, 4]


# Generated at 2022-06-14 04:01:07.371712
# Unit test for function cond
def test_cond():
    result = cond(
        [
            (eq(1), identity),
            (eq(2), increase)
        ]
    )

    assert result(1) == 1
    assert result(2) == 3



# Generated at 2022-06-14 04:01:08.849181
# Unit test for function memoize
def test_memoize():
    assert compose(identity(1), memoize)(identity)() == 1

# Generated at 2022-06-14 04:01:12.835443
# Unit test for function curried_filter
def test_curried_filter():
    l = [1, 2, 3, 4, 5, 6]
    f = curried_filter(lambda x: x % 2 == 0)
    assert f(l) == [2, 4, 6]



# Generated at 2022-06-14 04:01:25.441690
# Unit test for function curry
def test_curry():
    assert curry(lambda x, y, z: x + y + z)(1, 3, 4) == 8
    assert curry(lambda x, y, z: x + y + z)(1, 3)(4) == 8
    assert curry(lambda x, y, z: x + y + z)(1)(3, 4) == 8
    assert curry(lambda x, y, z: x + y + z)(1)(3)(4) == 8
    assert curry(lambda x, y, z: x + y + z)(1)(3, 4) == 8
    assert curry(lambda x, y, z: x + y + z)(1)(3)(4) == 8
    assert curry(lambda x, y, z: x * y * z)(1)(3)(4) == 12

# Generated at 2022-06-14 04:01:32.235512
# Unit test for function find
def test_find():
    assert find([], lambda x: False) is None
    assert find([1, 2, 3], lambda x: x == 2) == 2
    assert find([2], lambda x: x == 2) == 2
    assert find([1, 2, 3], lambda x: False) is None
    assert find([1, 2, 3], lambda x: x == 4) is None



# Generated at 2022-06-14 04:01:35.659301
# Unit test for function curried_map
def test_curried_map():
    curried_map(lambda item: item*item, [1, 2, 3])
    curried_map(lambda item: item*item)([1, 2, 3])



# Generated at 2022-06-14 04:01:44.096983
# Unit test for function memoize
def test_memoize():
    functions = [lambda x: x * x, lambda x: x + x, lambda x: x * 3]
    copy_functions = [functools.partial(function) for function in functions]

    for n in range(5000):
        for i in range(len(functions)):
            result1 = functions[i](n)
            result2 = functions[i](n)

    for n in range(5000):
        for i in range(len(copy_functions)):
            result1 = copy_functions[i](n)
            result2 = copy_functions[i](n)

    assert len(functions) != len(
        copy_functions), "Looks like you forgot to remove `lambda` from argument or forgot to make a partial application of the function."

# Generated at 2022-06-14 04:01:54.332103
# Unit test for function curried_filter
def test_curried_filter():
    assert_fn = lambda collection, filterer, expected: assert_equal(
        curried_filter(filterer)(collection),
        expected
    )

    assert_fn(
        collection=[],
        filterer=lambda x: False,
        expected=[],
    )

    assert_fn(
        collection=[1, 2, 3],
        filterer=lambda x: x > 2,
        expected=[3],
    )

    assert_fn(
        collection=[1, 2, 3],
        filterer=lambda x: x == 2,
        expected=[2],
    )



# Generated at 2022-06-14 04:01:57.666012
# Unit test for function find
def test_find():
    assert None == find([1], lambda x: x == 2)
    assert 3 == find([1, 2, 3], lambda x: x == 3)



# Generated at 2022-06-14 04:02:01.062832
# Unit test for function find
def test_find():
    assert find([], eq("a")) is None
    assert find([1, 2, 3], eq(3)) == 3
    assert find([1, 2, 3], eq(2)) == 2



# Generated at 2022-06-14 04:02:20.955061
# Unit test for function cond
def test_cond():
    def add(i):
        return i + 1

    def subtract(i):
        return i - 1

    condition_list = [
        (eq(1), add),
        (eq(2), subtract),
    ]

    assert cond(condition_list)(1) == 2
    assert cond(condition_list)(2) == 1



# Generated at 2022-06-14 04:02:24.353945
# Unit test for function find
def test_find():
    assert find([1, 2, 3, 4, 5], eq(3)) == 3
    assert find([1, 2, 3, 4, 5], eq(6)) is None
    assert find(['a', 'b', 'c'], eq('b')) == 'b'
    assert find(['a', 'b', 'c'], eq('d')) is None


test_find()



# Generated at 2022-06-14 04:02:30.116116
# Unit test for function curried_map
def test_curried_map():
    collection = [1,2,3]
    result = curried_map(increase, collection)
    assert result == [2,3,4]

    curried_map_increase = curried_map(increase)
    result = curried_map_increase(collection)
    assert result == [2,3,4]



# Generated at 2022-06-14 04:02:37.161946
# Unit test for function cond
def test_cond():
    def odd(value):
        return value % 2 == 1

    def double(value):
        return value * 2

    def triple(value):
        return value * 3

    condition_list = [
        (odd, double),
        (lambda _: True, triple)
    ]
    cond_result = cond(condition_list)

    assert cond_result(20) == 60
    assert cond_result(21) == 42
    assert cond_result(42) == 126
    assert cond_result(-1) == -3



# Generated at 2022-06-14 04:02:46.508648
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x > 3, [1, 2, 3, 4, 5, 6]) == [4, 5, 6]
    assert curried_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert curried_filter(lambda x: x > 3)([1, 2, 3, 4, 5, 6]) == [4, 5, 6]
    assert curried_filter(lambda x: x % 2 == 0)([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert curried_filter(lambda x: x > 3)([1, 2, 3, 4, 5, 6]) == [4, 5, 6]

# Generated at 2022-06-14 04:02:50.398718
# Unit test for function find
def test_find():
    test_list = [1, 2, 3, 4]
    assert find(test_list, lambda x: x == 3) == 3
    assert find(test_list, lambda x: x == 5) is None



# Generated at 2022-06-14 04:03:00.912536
# Unit test for function cond
def test_cond():

    # x < 2
    is_less_than_2 = lambda x: x < 2

    # x is 1
    is_1 = lambda x: x == 1

    # x == 2
    is_2 = lambda x: x == 2

    # x == 3
    is_3 = lambda x: x == 3

    # x = 1
    value1 = 1

    # x = 2
    value2 = 2

    # x = 3
    value3 = 3

    # x = 4
    value4 = 4

    # return x + 1 when x < 2 else x
    identity1 = lambda x: x + 1 if is_less_than_2(x) else x

    # return x + 2 when x == 1 else x
    identity2 = lambda x: x + 2 if is_1(x) else x

    # return x +

# Generated at 2022-06-14 04:03:04.436837
# Unit test for function curried_map
def test_curried_map():
    a = [1, 2, 3]
    b = curried_map(increase, a)
    if b == [2, 3, 4]:
        print('Test curried_map: Ok')
    else:
        print('Test curried_map: Fail')


# Generated at 2022-06-14 04:03:05.795594
# Unit test for function eq
def test_eq():
    assert eq(1, 1)
    assert not eq(1, 2)


# Generated at 2022-06-14 04:03:11.806279
# Unit test for function memoize
def test_memoize():
    # given
    cache_size = 3
    counter = 0
    def test_function(argument):
        nonlocal counter
        counter += 1
        return argument * argument

    memoized_test_function = memoize(test_function)

    # when
    for x in range(cache_size):
        memoized_test_function(x)
    for x in range(cache_size):
        memoized_test_function(x)
    for y in range(cache_size):
        memoized_test_function(y + cache_size)
    for y in range(cache_size):
        memoized_test_function(y + cache_size)
    for z in range(cache_size):
        memoized_test_function(z + cache_size * 2)
    for z in range(cache_size):
        memoized

# Generated at 2022-06-14 04:03:47.928700
# Unit test for function eq
def test_eq():
    assert eq(2, 1) is False
    assert eq(2, 2) is True
    assert eq(2, 3) is False
    assert eq('asd', 'asd') is True
    assert eq('asd', 'e') is False
    assert eq('d', 'f') is False
    assert eq('f', 'f') is True
    assert eq('f', 'g') is False
    assert eq((1, 2, 3), (1, 2, 3)) is True
    assert eq((1, 2, 3), (1, 2, 4)) is False
    assert eq((1, 2, 3), (1, 3, 3)) is False
    assert eq((1, 2, 3), (4, 2, 3)) is False
    assert eq((1, 2, 3), (4, 5, 6)) is False
    assert eq

# Generated at 2022-06-14 04:03:55.859240
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(lambda x: x + 1, [1, 2, 3]) == [2, 3, 4]

    assert curried_map(lambda x: x + 1)([1, 2, 3]) == [2, 3, 4]

    assert curried_map(lambda x: x + 1, [1])([2, 3]) == [2, 3, 4]

    assert curried_map(lambda x: x + 1)([1])([2, 3]) == [2, 3, 4]



# Generated at 2022-06-14 04:03:58.026000
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x % 2 == 0)([1, 2, 3, 4, 5]) == [2, 4]



# Generated at 2022-06-14 04:04:01.838481
# Unit test for function memoize
def test_memoize():
    def fn(argument):
        return argument + 1
    memoized_fn = memoize(fn)
    assert memoized_fn(1) == 2
    assert memoized_fn(1) == 2



# Generated at 2022-06-14 04:04:08.962787
# Unit test for function find
def test_find():
    input: List[str] = ["first_string", "second_string", "third_string"]
    finder: Callable[[str], bool] = lambda item: item == "second_string"
    assert find(input, finder) == "second_string"
    assert find(input, curry(lambda item, token: item == token, 'third_string')) == "third_string"



# Generated at 2022-06-14 04:04:13.924211
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(identity)([1, 2, 3]) == [1, 2, 3]
    assert curried_map(increase)([1, 2, 3]) == [2, 3, 4]
    assert curried_map(increase)([]) == []



# Generated at 2022-06-14 04:04:22.354782
# Unit test for function cond
def test_cond():
    def test_1(value: int) -> bool:
        return value % 3 == 0

    def test_2(value: int) -> bool:
        return value % 5 == 0

    # creating compose from two functions
    result = compose(
        lambda _: True,
        cond([
            (test_1, lambda _: 'Fizz'),
            (test_2, lambda _: 'Buzz'),
        ])
    )(15)

    # creating pipe from two functions
    result = pipe(
        lambda _: True,
        cond([
            (test_1, lambda _: 'Fizz'),
            (test_2, lambda _: 'Buzz'),
        ])
    )(15)

    return result

# Generated at 2022-06-14 04:04:28.032483
# Unit test for function memoize
def test_memoize():
    def add(a, b):
        return a + b
    
    memoize_add = memoize(add)
    memoize_add(1, 2)
    memoize_add(1, 2)
    memoize_add(1, 2)
    
    print(memoize_add)

# Generated at 2022-06-14 04:04:33.213459
# Unit test for function memoize
def test_memoize():
    @memoize
    def multiply(value):
        return value * 3

    assert multiply(3) == 9
    assert multiply(3) == 9
    assert multiply(4) == 12
    assert multiply(4) == 12



# Generated at 2022-06-14 04:04:39.238191
# Unit test for function memoize
def test_memoize():
    def fib(n):
        if n < 2:
            return n
        return fib(n-1) + fib(n-2)

    fib1 = memoize(fib)
    fib2 = memoize(fib)
    assert fib1(10) == fib2(10)
    assert fib1(30) == fib2(30)
    assert fib1(20) == fib2(20)


if __name__ == "__main__":
    test_memoize()

# Generated at 2022-06-14 04:06:38.686750
# Unit test for function memoize
def test_memoize():
    count = 0

    @memoize
    def foo(x):
        nonlocal count
        count += 1

        return x * 2

    assert foo(1) == 2
    assert foo(1) == 2
    assert count == 1
    assert foo(2) == 4
    assert foo(2) == 4
    assert count == 2
    assert foo(1) == 2
    assert count == 2



# Generated at 2022-06-14 04:06:40.751719
# Unit test for function eq
def test_eq():
    assert eq(1, 1)
    assert not eq(1, 2)



# Generated at 2022-06-14 04:06:50.047532
# Unit test for function memoize
def test_memoize():
    from time import time

    def time_nanoseconds() -> int:
        return int(time() * 10**9)

    def calculate_mean(x):
        def mean(numbers):
            return reduce(lambda a, b: a + b, numbers, 0) / len(numbers)

        return mean(range(x))

    calculate_mean = memoize(calculate_mean)
    start = time_nanoseconds()
    print("Calculated memozitive mean:", calculate_mean(1000000), "Time:", time_nanoseconds() - start)
    start = time_nanoseconds()
    print("Calculated memozitive mean:", calculate_mean(1000000), "Time:", time_nanoseconds() - start)

# Generated at 2022-06-14 04:06:59.811625
# Unit test for function cond
def test_cond():
    even = lambda x: x % 2 == 0
    odd = lambda x: not even(x)
    inc = lambda x: x + 1
    dec = lambda x: x - 1
    times_two = lambda x: x * 2
    times_three = lambda x: x * 3
    result = cond([
        (even, inc),
        (odd, dec)
    ])
    assert result(8) == 9
    assert result(5) == 4
    result = cond([
        (even, inc),
        (odd, dec),
        (lambda _: True, times_two),
    ])
    assert result(4) == 5
    assert result(3) == 4
    assert result(5) == 10

# Generated at 2022-06-14 04:07:06.329227
# Unit test for function memoize
def test_memoize():
    old_fibonacci_function = lambda n: n if n < 2 else memoized_fibonacci_function(n - 1) + memoized_fibonacci_function(
        n - 2)
    test_fibonacci_function = memoize(old_fibonacci_function)
    assert test_fibonacci_function(6) == old_fibonacci_function(6)
    assert test_fibonacci_function(6) == memoized_fibonacci_function(6)
    assert test_fibonacci_function(100) == old_fibonacci_function(100)
    assert test_fibonacci_function(100) == memoized_fibonacci_function(100)
    assert test_fibonacci_function(300) == old_fibon

# Generated at 2022-06-14 04:07:11.363096
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(identity)([1,2,3]) == [1,2,3]
    assert curried_map(lambda x: x*2)([1,2,3]) == [2,4,6]


# Generated at 2022-06-14 04:07:12.910426
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x > 1)([1, 2, 3]) == [2, 3]

# Generated at 2022-06-14 04:07:22.500591
# Unit test for function memoize
def test_memoize():
    old_function = identity
    memoized_function = memoize(old_function)
    assert memoized_function(1) == old_function(1)
    assert memoized_function(1) == old_function(1)
    assert memoized_function(2) == old_function(2)
    # check number of calls the old_function
    assert old_function.__code__.co_nlocals == 1
    memoized_function.__code__.co_consts

    old_function2 = increase
    memoized_function2 = memoize(old_function2)
    assert memoized_function2(1) == old_function2(1)
    assert memoized_function2(1) == old_function2(1)
    assert memoized_function2(2) == old_function2(2)
    #

# Generated at 2022-06-14 04:07:24.730361
# Unit test for function eq
def test_eq():
    assert eq('1', 1) is False
    assert eq(1, 1) is True



# Generated at 2022-06-14 04:07:29.799399
# Unit test for function memoize
def test_memoize():
    def some_function(x):
        return x + x

    memoized = memoize(some_function)
    assert(memoized(1) == 2)
    assert(memoized(2) == 4)
    assert(memoized(1) == 2)
    assert(len(memoized.__closure__[0].cell_contents) == 2)
