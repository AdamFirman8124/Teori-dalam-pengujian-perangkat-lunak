

# Generated at 2022-06-14 03:58:00.605592
# Unit test for function curried_map
def test_curried_map():
    assert (
        list(map(lambda x: x + 1, [1, 2, 3])) ==
        curried_map(lambda x: x + 1, [1, 2, 3])
    )



# Generated at 2022-06-14 03:58:06.069206
# Unit test for function curry
def test_curry():
    def reverse(collection):
        return list(reversed(collection))

    reversed_list = curry(reverse)
    assert reversed_list([]) == []
    assert reversed_list([1]) == [1]
    assert reversed_list([1, 2, 3]) == [3, 2, 1]

    assert curry(identity)(1) == 1
    assert curry(increase)(5) == 6



# Generated at 2022-06-14 03:58:09.111012
# Unit test for function eq
def test_eq():
    assert eq(2, 3) is False
    assert eq(2, 2) is True



# Generated at 2022-06-14 03:58:16.001865
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(lambda x: x + 1, [1, 2, 3]) == [2, 3, 4]
    assert curried_map(lambda x: x + 1)([1, 2, 3]) == [2, 3, 4]
    assert curried_map(lambda x: x + 1)([1, 2])([3, 4]) == [2, 3, 4, 5]
    assert curried_map(lambda x: x + 1)([1, 2]) == [2, 3]
    assert curried_map(lambda x: x + 1, [1, 2]) == [2, 3]


# Generated at 2022-06-14 03:58:19.068938
# Unit test for function eq
def test_eq():
    assert eq(1, 1)
    assert not eq(1, 2)
    assert not eq(1, 2, 3)
    assert eq(1, 1, 1)
    assert not eq(1, 1, 1, 1)
    assert not eq(1, 1, 1, 2)
    assert eq(1, 1, 1, 1, 1)


# Generated at 2022-06-14 03:58:30.903331
# Unit test for function cond
def test_cond():
    def is_zero(value):
        return value == 0

    def is_zero_or_one(value):
        return value <= 1

    def even_number(value):
        return value % 2 == 0

    def is_list(value):
        return isinstance(value, list)

    def is_none(value):
        return value is None

    def zero_operation(value):
        return 0

    def zero_or_one_operation(value):
        return value

    def even_number_operation(value):
        return value // 2

    def list_operation(value):
        return value * 2

    def none_operation(value):
        return 10

    def add(value, value1):
        return value + value1

    def double_multiply(value):
        return value * 2


# Generated at 2022-06-14 03:58:39.653077
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(lambda a: a + 1, [1, 2, 3])() == [2, 3, 4]
    assert curried_map(lambda a: a + 1)([1, 2, 3]) == [2, 3, 4]
    assert curried_map(lambda a: a + 1, [])([1, 2, 3]) == [2, 3, 4]


# Generated at 2022-06-14 03:58:41.961518
# Unit test for function curried_filter
def test_curried_filter():
    numbers = [1, 2, 3, 4, 5]
    filtered = curried_filter(lambda x: x % 2 == 0, numbers)
    assert filtered == [2, 4]



# Generated at 2022-06-14 03:58:45.952400
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x > 0, [0, 1]) == [1]
    # test with curried arguments
    curried_filter_with_lambda = curried_filter(lambda x: x > 0)
    assert curried_filter_with_lambda([0, 1]) == [1]



# Generated at 2022-06-14 03:58:52.449320
# Unit test for function curried_map
def test_curried_map():
    """
    Unit test for function curried_map
    """
    assert curried_map(lambda x: x + 1)([1, 2, 3]) == [2, 3, 4]
    assert curried_map(lambda x: x + 1)([1, 2, 3]) == [2, 3, 4]



# Generated at 2022-06-14 03:59:00.092341
# Unit test for function curried_filter
def test_curried_filter():
    even_filter = curried_filter(lambda x: x % 2 == 0)
    assert even_filter([1, 2, 3, 4, 5]) == [2, 4]



# Generated at 2022-06-14 03:59:07.451419
# Unit test for function memoize
def test_memoize():
    import time
    import random
    from typing import Dict
    from collections import namedtuple

    def log(value):
        print(value)
        return value

    def test_fn(argument_value):
        time.sleep(random.randint(0, 5))
        return argument_value

    memoized_test_fn = memoize(test_fn)
    log(memoized_test_fn(10))
    log(memoized_test_fn(10))



# Generated at 2022-06-14 03:59:12.164404
# Unit test for function find
def test_find():
    """
    Test find function.
    """
    assert find([], lambda x: False) is None
    assert find([1, 2, 3, 4], lambda x: x % 2 == 0) == 2
    assert find([1, 3, 5, 6], lambda x: x % 2 == 0) == 6



# Generated at 2022-06-14 03:59:16.005472
# Unit test for function curry
def test_curry():
    def f_1(x, y, z):
        return x + y + z

    assert curry(f_1)(1, 2, 3) == 6

    assert curry(f_1)(1)(2, 3) == 6

    assert curry(f_1)(1)(2)(3) == 6



# Generated at 2022-06-14 03:59:20.463086
# Unit test for function find
def test_find():
    assert find([1, 2, 3, 4], lambda item: item == 2) == 2
    assert find(['one', 'two', 'three'], lambda item: len(item) == 5) == 'three'



# Generated at 2022-06-14 03:59:28.674229
# Unit test for function curried_filter
def test_curried_filter():
    """
    Unit test for function curried_filter.

    :param:
    :type:
    :returns:
    :rtype:
    """
    assert curried_filter(eq(1), [1, 2, 3]) == [1]
    assert curried_filter(eq('b'), ['a', 'b', 'c']) == ['b']
    assert curried_filter(eq(True), [True, False, True]) == [True, True]

    assert curried_filter(
        eq([1, 2, 3]),
        [
            [1, 2, 3],
            [2, 3, 4]
        ]
    ) == [
        [1, 2, 3]
    ]



# Generated at 2022-06-14 03:59:35.206497
# Unit test for function curry
def test_curry():
    def add(x: int, y: int):
        return x + y

    curried_add = curry(add)
    assert curried_add(1)(2) == add(1, 2)

    curried_add_2 = curry(add, 2)
    assert curried_add(1, 2) == add(1, 2)
    assert curried_add_2(1)(2) == add(1, 2)



# Generated at 2022-06-14 03:59:39.213517
# Unit test for function find
def test_find():
    assert None is find([], identity)
    assert 1 is find([1, 2, 3], identity)
    assert None is find([1, 2, 3], increase)



# Generated at 2022-06-14 03:59:49.891141
# Unit test for function find
def test_find():
    import unittest

    class FindTestCase(unittest.TestCase):

        def test_empty_list(self):
            self.assertIsNone(find([], lambda x: True))

        def test_none_is_true(self):
            self.assertIsNone(find([], lambda x: True))

        def test_none_is_false(self):
            self.assertIsNone(find([], lambda x: False))

        def test_find_one_element_when_none_is_true(self):
            self.assertEqual(find([1], lambda x: True), 1)

        def test_find_one_element_when_none_is_false(self):
            self.assertEqual(find([1], eq(1)), 1)


# Generated at 2022-06-14 03:59:53.215109
# Unit test for function curried_filter
def test_curried_filter():
    collection = [
        'Hello',
        'world',
        '!'
    ]

    predicate = curried_filter(eq('world'))
    result = predicate(collection)

    assert result == ['world']



# Generated at 2022-06-14 04:00:02.606604
# Unit test for function eq
def test_eq():
    assert eq(10, 10)
    assert not eq(10, 20)


# Generated at 2022-06-14 04:00:05.064662
# Unit test for function eq
def test_eq():
    # when
    result = eq(1, 1)
    # then
    assert result == True


# Generated at 2022-06-14 04:00:16.415603
# Unit test for function cond
def test_cond():
    def is_even(value: int) -> bool:
        return value % 2 == 0

    def is_positive(value: int) -> bool:
        return value > 0

    def add_one(value: int) -> int:
        return value + 1

    def to_string(value: int) -> str:
        return str(value)

    def even_modify(value: int) -> int:
        return cond([
            (is_even, add_one),
            (is_positive, identity)
        ])(value)

    assert even_modify(2) == 3
    assert even_modify(3) == 3
    assert even_modify(-2) == -2


# Generated at 2022-06-14 04:00:20.261712
# Unit test for function curried_filter
def test_curried_filter():
    assert [1, 2] == curried_filter(lambda x: x % 2 == 1, [1, 2, 3, 4])
    assert [] == curried_filter(lambda x: x % 2 == 1, [2, 4, 6, 8])


# Generated at 2022-06-14 04:00:25.253683
# Unit test for function find
def test_find():
    assert find(
        [0, 1, 2],
        lambda item: item == 0
    ) == 0
    assert find(
        [0, 1, 2],
        lambda item: item == 0
    ) == 0
    assert find(
        [0, 1, 2],
        lambda item: item == 10
    ) is None


if __name__ == '__main__':
    test_find()

# Generated at 2022-06-14 04:00:29.477040
# Unit test for function eq
def test_eq():
    """
    Unit test for function eq.
    """
    print('1 == 1: ' + str(eq(1, 1)))
    print('1 == 2: ' + str(eq(1, 2)))



# Generated at 2022-06-14 04:00:32.458606
# Unit test for function curried_filter
def test_curried_filter():
    a = [1, 2, 3, 4]
    assert curried_filter(lambda item: item % 2 == 0)(a) == [2, 4]



# Generated at 2022-06-14 04:00:40.141001
# Unit test for function curried_map
def test_curried_map():
    assert list(map(lambda x: x ** 2, [1, 2, 3])) == curried_map(lambda x: x ** 2, [1, 2, 3])
    assert list(map(lambda x: x ** 2, [1, 2, 3])) == curried_map(lambda x: x ** 2)([1, 2, 3])
    assert list(map(lambda x: x ** 2, [1, 2, 3])) == curried_map(lambda x: x ** 2, [1, 2, 3])


# Generated at 2022-06-14 04:00:44.785362
# Unit test for function eq
def test_eq():
    assert eq(1, 1) == True
    assert eq(1, 2) == False  # Test False
    assert eq(1)(1) == True  # Test curried
    assert eq(1)(2) == False  # Test curried and False


# Generated at 2022-06-14 04:00:50.456597
# Unit test for function curried_filter
def test_curried_filter():
    list_ = [1, 2, 3, 4, 5]
    assert curried_filter(lambda item: item % 2 == 0)(list_) == [2, 4]
    assert curried_filter(lambda item: item % 2 == 0)([1, 3, 5]) == []
    assert curried_filter(lambda item: item % 2 == 0)([]) == []


# Generated at 2022-06-14 04:01:09.400958
# Unit test for function find
def test_find():
    assert find([], lambda x: False) is None
    assert find([1, 2, 3], lambda x: x == 2) == 2
    assert find([1, 2, 3], lambda x: x == 10) is None

test_find()

# Generated at 2022-06-14 04:01:13.861014
# Unit test for function find
def test_find():
    assert find([1, 2, 3], lambda x: x % 2 == 0) == 2
    assert find([1, 3, 5], eq(2)) == None
    assert find([1, 2, 3], eq(1)) == 1



# Generated at 2022-06-14 04:01:18.737345
# Unit test for function curried_filter
def test_curried_filter():
    is_greater_than_five = curried_filter(lambda x: x > 5)
    result = is_greater_than_five([1, 2, 3, 4, 5, 6, 7])
    assert result == [6, 7]



# Generated at 2022-06-14 04:01:21.172878
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x > 2, [1, 2, 3, 4, 5]) == [3, 4, 5]



# Generated at 2022-06-14 04:01:25.779163
# Unit test for function find
def test_find():
    test_list = [1, 2, 3, 4, 5, 6, 7]
    assert find(test_list, lambda x: x > 3) == 4
    assert find(test_list, lambda x: x > 7) is None
    assert find(test_list, lambda x: x == 3) == 3



# Generated at 2022-06-14 04:01:30.468525
# Unit test for function find
def test_find():
    assert find(
        [1, 2, 3, 4],
        lambda item: item == 2
    ) == 2
    assert find(
        [1, 2, 3, 4],
        lambda item: item == 5
    ) is None



# Generated at 2022-06-14 04:01:42.773804
# Unit test for function curry
def test_curry():
    """
    test function for function curry
    """
    assert curry(lambda x, y, z: x + y + z)(1)(2)(3) == 6
    assert curry(lambda x, y, z=3: x + y + z)(1)(2) == 6
    assert curry(lambda x, y, z=3: x + y + z)(1)(y=2, z=5) == 8
    assert curry(lambda x, y, z=3: x + y + z)(x=1, y=2) == 6

    def add(x, y, z):
        return x + y + z

    assert curry(add)(x=1)(y=2)(z=3) == 6
    assert curry(add)(1)(2)(3) == 6

# Generated at 2022-06-14 04:01:47.469086
# Unit test for function curried_filter
def test_curried_filter():
    def is_even(value):
        return value % 2 == 0

    filter_evens = curried_filter(is_even)
    assert filter_evens([1, 2, 3, 4]) == [2, 4]


# Generated at 2022-06-14 04:01:51.368660
# Unit test for function curried_filter
def test_curried_filter():
    def is_even(x):
        return x % 2 == 0
    assert curried_filter(is_even)([1, 2, 3, 4]) == [2, 4]


# Generated at 2022-06-14 04:01:54.204710
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(lambda x: x + 1)([1, 2, 3]) == [2, 3, 4]


# Generated at 2022-06-14 04:02:57.994239
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(identity, []) == []
    assert curried_map(identity, [1, 2, 3]) == [1, 2, 3]
    assert curried_map(
        lambda x: x + 1,
        []
    ) == []
    assert curried_map(
        lambda x: x + 1,
        [1, 2, 3]
    ) == [2, 3, 4]
    assert curried_map(
        lambda x: x + 1,
        [1, 2, 3]
    ) == curried_map(increase, [1, 2, 3])


# Generated at 2022-06-14 04:03:03.641121
# Unit test for function cond
def test_cond():
    condition_list = [
        (lambda x: isinstance(x, int), lambda x: x + 1),
        (lambda x: isinstance(x, str), lambda x: x),
    ]
    cond_sum_1 = cond(condition_list)
    assert cond_sum_1(1) == 2
    assert cond_sum_1('value') == 'value'



# Generated at 2022-06-14 04:03:09.064534
# Unit test for function memoize
def test_memoize():
    def sum(x: int, y: int) -> int:
        return x + y

    memoized_sum = memoize(sum)
    assert memoized_sum(2, 3) is 5
    # Test equability
    assert memoized_sum(2, 3) is memoized_sum(2, 3)  # noqa


# Unit tests for function cond

# Generated at 2022-06-14 04:03:19.277442
# Unit test for function memoize
def test_memoize():
    counter = -1

    @memoize
    def fib(n):
        nonlocal counter
        counter += 1
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n-1) + fib(n-2)

    assert counter == -1
    assert fib(7) == 13
    assert counter == 7
    counter = -1
    assert fib(7) == 13
    assert counter == 0
    assert fib(3) == 2
    assert counter == 3
    counter = -1
    assert fib(3) == 2
    assert counter == 0
    assert fib(5) == 5
    assert counter == 3
    counter = -1
    assert fib(5) == 5
    assert counter == 0



# Generated at 2022-06-14 04:03:26.748847
# Unit test for function cond
def test_cond():
    result = cond([
        (
            lambda x: x % 2 == 0,
            lambda x: x + 1
        ),
        (
            lambda x: x % 3 == 0,
            lambda x: x + 2
        ),
        (
            lambda x: True,
            lambda x: x + 3
        )
    ])(1)
    assert result == 4, 'result must be 4'



# Generated at 2022-06-14 04:03:32.310865
# Unit test for function cond
def test_cond():
    assert compose(10,
                   cond([(lambda x: x < 10, increase),
                         (lambda x: x == 10, increase),
                         (lambda x: x > 10, identity)])) == 11
    assert compose(15,
                   cond([(lambda x: x < 10, increase),
                         (lambda x: x == 10, increase),
                         (lambda x: x > 10, identity)])) == 15


test_cond()


# Generated at 2022-06-14 04:03:42.191103
# Unit test for function memoize
def test_memoize():
    empty_cache = memoize(lambda x: x + 1)
    assert empty_cache(2) == 3
    assert empty_cache(2) == 3
    assert empty_cache(2) == 3
    assert empty_cache(2) == 3
    assert empty_cache(4) == 5
    assert empty_cache(4) == 5
    assert empty_cache(4) == 5
    assert empty_cache(4) == 5
    assert empty_cache(4) == 5
    assert empty_cache(4) == 5
    assert empty_cache(2) == 3
    assert empty_cache(1) == 2
    assert empty_cache(1) == 2
    assert empty_cache(4) == 5



# Generated at 2022-06-14 04:03:45.448077
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(identity)([1, 2, 3]) == [1, 2, 3]
    assert curried_map(increase)([1, 2, 3]) == [2, 3, 4]



# Generated at 2022-06-14 04:03:57.065038
# Unit test for function cond
def test_cond():
    add = lambda x, y: x + y
    assert cond([
        (lambda x: x > 10, lambda: 'greater'),
        (lambda x: x < 10, lambda: 'less'),
        (lambda x: x == 10, lambda: 'equal'),
    ])(10) == 'equal'
    assert cond([
        (lambda x, y: x > 10, lambda x, y: x + y),
        (lambda x, y: x < 10, lambda x, y: x + y),
        (lambda x, y: x == 10, lambda x, y: x + y),
    ])(10, 20) == 30

# Generated at 2022-06-14 04:04:06.827142
# Unit test for function memoize
def test_memoize():
    """
    Test function memoize.

    :return:
    """
    def f(x):
        # 2x
        return x * 2

    # f = curry(f)
    f_m = curry(memoize(f))
    assert(f_m(2) == 4)
    assert(f_m(2) == 4)
    assert(f_m(2) == 4)


T1 = TypeVar('T1')
T2 = TypeVar('T2')
T3 = TypeVar('T3')
T4 = TypeVar('T4')
T5 = TypeVar('T5')



# Generated at 2022-06-14 04:04:51.448971
# Unit test for function curried_map
def test_curried_map():
    """
    :returns: Return true if curried_map work as expected
    :rtype: Boolean
    """
    assert curried_map(lambda x: x > 0)([-1, 2, 0, 3]) == [False, True, False, True]

# Generated at 2022-06-14 04:04:53.754429
# Unit test for function eq
def test_eq():
    assert eq(1, 1) is True
    assert eq(1, 2) is False

# Unit tests for function curried_map

# Generated at 2022-06-14 04:05:00.469711
# Unit test for function memoize
def test_memoize():
    def factorial(x):
        if x == 0:
            return 1
        return x * factorial(x - 1)

    fn = memoize(factorial)
    assert fn(5) == 120
    assert fn(6) == 720

    fn2 = memoize(
        lambda a: a + 10,
        key=lambda a, a2: a == a2
    )

    assert fn2(7) == 17
    assert fn2(7) == 17



# Generated at 2022-06-14 04:05:05.450545
# Unit test for function curried_map
def test_curried_map():
    collection = [1, 2, 3, 4]

    mapper = lambda x: x * x

    result = curried_map(mapper)(collection)

    assert result == list(map(mapper, collection))



# Generated at 2022-06-14 04:05:08.458650
# Unit test for function curried_map
def test_curried_map():
    example_array = [1, 2, 3, 4, 5]
    assert curried_map(lambda item: item * 2)(example_array) == [2, 4, 6, 8, 10]
    assert curried_map(lambda item: item * 3, example_array) == [3, 6, 9, 12, 15]
    assert curried_map(lambda item: item * 2, [1, 2, 3, 4, 5]) == [2, 4, 6, 8, 10]



# Generated at 2022-06-14 04:05:14.906006
# Unit test for function memoize
def test_memoize():
    def fn_count():
        nonlocal counter
        counter += 1

    counter = 0
    memoized = memoize(fn_count)
    assert counter == 0
    assert memoized() == 0
    assert counter == 1
    assert memoized() == 1
    assert counter == 2
    memoized = memoize(fn_count, lambda a, b: a)
    assert memoized() == 2
    memoized()
    memoized()
    memoized()
    memoized()
    memoized()
    assert counter == 3



# Generated at 2022-06-14 04:05:19.037597
# Unit test for function curry
def test_curry():
    def add2(x, y):
        return x + y

    add2_curry = curry(add2)
    assert add2_curry(1)(2) == 3



# Generated at 2022-06-14 04:05:31.061880
# Unit test for function cond
def test_cond():
    gt_5 = lambda x: x > 5
    is_5 = lambda x: x == 5
    is_2 = lambda x: x == 2

    gt_5_fun = lambda x: 'gt_5_fun'
    is_5_fun = lambda x: 'is_5_fun'
    is_2_fun = lambda x: 'is_2_fun'

    execute_with_gt_5 = cond([
        (gt_5, gt_5_fun),
        (is_5, is_5_fun),
        (is_2, is_2_fun),
    ])

    execute_with_5 = cond([
        (gt_5, gt_5_fun),
        (is_5, is_5_fun),
        (is_2, is_2_fun),
    ])

# Generated at 2022-06-14 04:05:38.276958
# Unit test for function cond
def test_cond():
    is_even = lambda x: x % 2 == 0
    is_zero = lambda x: x == 0
    double = lambda x: x * 2
    zero = lambda x: 0

    cond_test = cond([
        (is_even, double),
        (is_zero, zero)
    ])
    assert cond_test(1) == zero(1)
    assert cond_test(2) == double(2)
    assert cond_test(0) == zero(0)



# Generated at 2022-06-14 04:05:43.163544
# Unit test for function cond
def test_cond():
    def condition_function(string):
        return string == "test"

    def execute_function(string):
        return string + "_execute"

    cond_function = cond([
        (condition_function, execute_function),
    ])
    assert cond_function("test") == "test_execute"
