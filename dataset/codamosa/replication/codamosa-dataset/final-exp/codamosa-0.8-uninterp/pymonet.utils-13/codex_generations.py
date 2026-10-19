

# Generated at 2022-06-14 03:57:55.272608
# Unit test for function find
def test_find():
    assert find([], identity) is None
    assert find([1], eq(1)) == 1
    assert find([1], eq(2)) is None



# Generated at 2022-06-14 03:57:56.759801
# Unit test for function eq
def test_eq():
    assert eq(1, 1)
    assert not eq(1, 2)



# Generated at 2022-06-14 03:58:01.419293
# Unit test for function curried_filter
def test_curried_filter():
    even_pow_on_10 = lambda x: x**10 % 2 == 0
    assert curried_filter(even_pow_on_10)([1, 2, 3, 4, 5]) == [2, 4]



# Generated at 2022-06-14 03:58:06.554298
# Unit test for function memoize
def test_memoize():
    plus_one = memoize(increase)
    assert plus_one(1) == 2
    assert plus_one(1) == 2
    assert plus_one(2) == 3
    assert plus_one(2) == 3
    assert plus_one(1) == 2
    assert plus_one(1) == 2
    assert plus_one(1) == 2
    assert plus_one(1) == 2

# Generated at 2022-06-14 03:58:09.243907
# Unit test for function eq
def test_eq():
    assert eq(1, 2) == False
    assert eq(1, 1) == True


# Generated at 2022-06-14 03:58:11.127672
# Unit test for function eq
def test_eq():
    assert eq(1, 1)
    assert not eq(1, 2)



# Generated at 2022-06-14 03:58:18.283351
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(eq(1), [1, 5, 3]) == [1]
    assert curried_filter(lambda x: x == 1, [1, 5, 3]) == [1]


# Generated at 2022-06-14 03:58:22.382354
# Unit test for function eq
def test_eq():
    assert eq(1, 1)
    assert eq('test', 'test')
    assert not eq(1, 'test')
    assert not eq('test', 1)



# Generated at 2022-06-14 03:58:24.886495
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(increase)([1, 2, 3]) == [2, 3, 4]



# Generated at 2022-06-14 03:58:39.499636
# Unit test for function cond
def test_cond():
    def test_cond_success():
        def cond_arg_is_greater_than(right_value, left_value):
            return left_value > right_value

        def cond_arg_is_less_than(right_value, left_value):
            return left_value < right_value

        def ip_if_less_then_return_ip():
            return "IP"

        def ip_if_greater_then_return_ip_plus_2():
            return "IP + 2"

        def ip_if_none_of_cond_return_none():
            return "None"


# Generated at 2022-06-14 03:58:44.566393
# Unit test for function curried_map
def test_curried_map():
    def add_one(x):
        return x + 1
    a = [1, 2, 3]
    assert (curried_map(add_one, a) == [2, 3, 4])



# Generated at 2022-06-14 03:58:48.552575
# Unit test for function cond
def test_cond():
    def is_empty(collection):
        return len(collection) == 0

    def empty_collection():
        return []

    def collection_with_one_item():
        return [1]

    cond_function = cond([
        (is_empty, empty_collection),
        (identity, collection_with_one_item)
    ])

    assert cond_function([]) == empty_collection()
    assert cond_function([1]) == collection_with_one_item()



# Generated at 2022-06-14 03:58:51.125351
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(lambda x: x + 1)([1, 2, 3]) == [2, 3, 4]



# Generated at 2022-06-14 03:59:02.815721
# Unit test for function cond
def test_cond():
    first_condition = cond([
        (lambda x: x > 0, lambda x: 'x > 0'),
        (lambda x: x < 0, lambda x: 'x < 0'),
        (lambda x: x == 0, lambda x: 'x == 0'),
    ])

    second_condition = cond([
        (lambda x, y: x > y, lambda x, y: 'x > y'),
        (lambda x, y: x < y, lambda x, y: 'x < y'),
        (lambda x, y: x == y, lambda x, y: 'x == y'),
    ])

    assert first_condition(4) == 'x > 0'
    assert first_condition(-2) == 'x < 0'
    assert first_condition(0) == 'x == 0'


# Generated at 2022-06-14 03:59:12.661280
# Unit test for function cond
def test_cond():
    def a(args) -> bool:
        return args == 1

    def b(args) -> bool:
        return args == 2

    def c(args) -> bool:
        return args == 3

    def d(args) -> bool:
        return args == 4

    fun = cond([
        (a, lambda x: x + 1),
        (b, lambda x: x + 2),
        (c, lambda x: x + 3),
        (d, lambda x: x + 4),
    ])

    assert fun(1) == 2
    assert fun(2) == 4
    assert fun(3) == 6
    assert fun(4) == 8
    assert fun(5) is None



# Generated at 2022-06-14 03:59:13.739757
# Unit test for function eq
def test_eq():
    assert eq(1, 1)



# Generated at 2022-06-14 03:59:20.060953
# Unit test for function find
def test_find():
    assert find([], lambda x: x == 0) is None
    assert find([1, 2, 3], lambda x: x == 1) == 1
    assert find([1, 2, 3], lambda x: x == 5) is None
    assert find([1, 2, 3], lambda x: x == 3) == 3



# Generated at 2022-06-14 03:59:22.522182
# Unit test for function curry
def test_curry():
    result = curry(lambda x, y: x + y)
    assert result(1)(2) == 3



# Generated at 2022-06-14 03:59:28.420581
# Unit test for function eq
def test_eq():
    assert eq(1, 1) == True
    assert eq(0, -1) == False
    assert eq([1, 2, 3], [1, 2, 3]) == True
    assert eq('1', 1) == False
    assert eq('12', '12') == True
    assert eq({1:1, 2:2}, {1: 1, 2: 2}) == True
    assert eq({1:1, 2:2}, {1: 1, 2: 20}) == False



# Generated at 2022-06-14 03:59:34.928765
# Unit test for function cond
def test_cond():
    def make_equal(operand):
        def is_equal(x):
            return x == operand
        return is_equal

    def get_polite_greeting(name):
        def greeting(x):
            return "Hello, {}!".format(name)
        return greeting

    def get_welcome_back_greeting(name):
        def greeting(x):
            return "Welcome back, {}!".format(name)
        return greeting

    greeting = cond([
        (make_equal("Dima"), get_polite_greeting("Dima")),
        (make_equal("Mom"), get_polite_greeting("Mom")),
        (make_equal("Dad"), get_welcome_back_greeting("Dad")),
    ])
    assert greeting("Dima") == "Hello, Dima!"

# Generated at 2022-06-14 03:59:43.984851
# Unit test for function cond
def test_cond():
    def is_even(x):
        return x % 2 == 0

    def is_odd(x):
        return x % 2 == 1

    divide = cond([(is_even, lambda x: x // 2),
                   (is_odd, lambda x: x * 3 + 1)])

    assert divide(4) == 2
    assert divide(3) == 10

    def is_even(x):
        return x % 2 == 0

    def is_gt_3(x):
        return x > 3

    def gt_3_to_string(x):
        return str(x)

    def to_string(x):
        return str(x)

    to_str = cond([(is_even, to_string),
                   (is_gt_3, gt_3_to_string)])

    assert to_str

# Generated at 2022-06-14 03:59:46.211585
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(lambda x: x + 1)([1, 2, 3]) == [2, 3, 4]


# Generated at 2022-06-14 03:59:55.958427
# Unit test for function memoize
def test_memoize():
    """
    >>> from operator import add
    >>> from ramda import pipe, add, inc
    >>> from ramda import memoize
    >>> from functools import partial
    >>> from typing import Callable
    >>> def add_3(a, b, c):
    ...     return a + b + c
    ...
    >>> add_3_memoized = memoize(add_3)
    >>> assert add_3(1, 2, 3) == add_3_memoized(1, 2, 3)
    >>> add_3_memoized__1 = memoize(add_3, key=lambda x, y: x == y[0])
    >>> assert add_3_memoized__1(1, 2, 3) == add_3_memoized__1(1, 2, 3)
    """

# Generated at 2022-06-14 04:00:05.107616
# Unit test for function cond
def test_cond():
    def is_empty(value):
        return value == ''

    def is_zero(value):
        return value == '0'

    def is_one(value):
        return value == '1'

    def append_zero(value: str):
        return value + '0'

    def append_one(value: str):
        return value + '1'

    def append_two(value: str):
        return value + '2'

    new_append = cond([
        (is_empty, append_one),
        (is_zero, append_two),
        (is_one, append_zero),
    ])
    assert new_append('0') == '02'
    assert new_append('') == '1'
    assert new_append('1') == '10'


# Generated at 2022-06-14 04:00:08.265215
# Unit test for function eq
def test_eq():
    eq0 = curry(eq)

    assert eq0(2, 2) == True



# Generated at 2022-06-14 04:00:14.727847
# Unit test for function find
def test_find():
    # Equivalence partitioning
    arr = [1, 2, 3, 4, 5]
    assert find(arr, lambda val: val == 2) == 2
    assert find(arr, lambda val: val == 0) is None

    # Boundary value analysis
    arr = []
    assert find(arr, lambda val: val == 2) is None

    arr = [1, 2, 3, 4, 5]
    assert find(arr, lambda val: val == 5) == 5

# Generated at 2022-06-14 04:00:19.807514
# Unit test for function curried_filter
def test_curried_filter():
    curried_filter_eq = curried_filter(eq)
    assert curried_filter_eq([1, 2, 3])(1) == [1]
    assert curried_filter_eq([1, 2, 3])(2) == [2]
    assert curried_filter_eq([1, 2, 3])(3) == [3]


# Generated at 2022-06-14 04:00:24.538312
# Unit test for function find
def test_find():
    @curry
    def is_even(x: int) -> bool:
        return x % 2 == 0

    list_of_even_numbers = range(0, 10, 2)
    assert find(list_of_even_numbers, is_even(4)) == 4
    assert find(list_of_even_numbers, is_even(5)) is None



# Generated at 2022-06-14 04:00:32.015478
# Unit test for function cond
def test_cond():
    # noinspection PyRedeclaration
    cond_ = cond([
        (
            lambda value: value > 11,
            lambda _: False
        ),
        (
            lambda value: value > 10,
            lambda _: True
        ),
        (
            identity,
            lambda value: value > 10
        )
    ])

    assert cond_(11) == False
    assert cond_(12) == True
    assert cond_(9) == False

# Generated at 2022-06-14 04:00:37.917614
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert curried_filter(lambda x: x % 3 == 0, [1, 2, 3, 4, 5, 6]) == [3, 6]


if __name__ == "__main__":
    test_curried_filter()

# Generated at 2022-06-14 04:00:51.911892
# Unit test for function find
def test_find():
    assert None == find([1, 2, 3, 4, 5], lambda item: item > 7)
    assert 1 == find([1, 2, 3, 4, 5], lambda item: item == 1)
    assert 10 == find([1, 2, 3, 4, 5, 10], lambda item: item > 7)


# Generated at 2022-06-14 04:00:55.683558
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x % 2 == 0)([1, 2, 3, 4]) == [2, 4]



# Generated at 2022-06-14 04:00:59.653768
# Unit test for function eq
def test_eq():
    assert eq(1, 1) is True
    assert eq(1, 1, 10) is False
    fn = eq(1)
    assert fn(1) is True
    assert fn(2) is False



# Generated at 2022-06-14 04:01:08.805315
# Unit test for function memoize
def test_memoize():
    """
    Test function memoize.

    :returns: True if test pass, False otherwise
    :rtype: Boolean
    """
    def function(i: int) -> int:
        if i == 0:
            return i
        return function(i - 1) + 1

    memoized_function = memoize(function)
    assert memoized_function(100) == 100
    assert memoized_function(100) == 100
    assert memoized_function(42) == 42
    assert memoized_function(24) == 24
    assert memoized_function(36) == 36

    return True
# End of unit test for function memoize



# Generated at 2022-06-14 04:01:19.488202
# Unit test for function curried_map
def test_curried_map():
    """
    Unit test for function curried_map
    """
    identity_map = curried_map(identity)
    increment_map = curried_map(increase)
    assert identity_map([1, 2, 3]) == [1, 2, 3], "Identity map should return list without mapping"
    assert increment_map([1, 2, 3]) == [2, 3, 4], "Increment map should return incremented values"
    assert identity_map([]) == [], "Identity map should work with empty list"
    assert increment_map([]) == [], "Increment map should work with empty list"


# Generated at 2022-06-14 04:01:22.541280
# Unit test for function eq
def test_eq():
    assert eq(1)(1) is True
    assert eq(1, 1) is True
    assert eq(1)(2) is False
    assert eq(1, 2) is False



# Generated at 2022-06-14 04:01:24.981153
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x % 2, list(range(10))) == [1, 3, 5, 7, 9]



# Generated at 2022-06-14 04:01:27.877127
# Unit test for function eq
def test_eq():
    assert eq(1, 2) is False, "eq(1, 2) return False"
    assert eq(1, 1) is True, "eq(1, 1) return True"



# Generated at 2022-06-14 04:01:30.316687
# Unit test for function find
def test_find():
    """
    Function find gets list of 1,2,3 and key is identity
    """
    assert 1 == find([1, 2, 3], identity)



# Generated at 2022-06-14 04:01:36.137118
# Unit test for function curried_filter
def test_curried_filter():
    big_list = list(range(100))
    even_list = list(range(0, 100, 2))
    odd_list = list(range(1, 100, 2))

    even_func = curried_filter(lambda x: x % 2 == 0)
    odd_func = curried_filter(lambda x: x % 2 != 0)

    assert even_list == even_func(list(range(100)))
    assert odd_list == odd_func(list(range(100)))



# Generated at 2022-06-14 04:01:58.442775
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(lambda x: x + 10, [1, 2, 3]) == [11, 12, 13] == \
           curried_map(lambda x: x + 10)([1, 2, 3])



# Generated at 2022-06-14 04:02:00.405405
# Unit test for function eq
def test_eq():
    assert eq(1)(1)
    assert not eq(2)(1)



# Generated at 2022-06-14 04:02:03.087338
# Unit test for function eq
def test_eq():
    assert eq(5, 5) is True
    assert eq(5, 6) is False



# Generated at 2022-06-14 04:02:10.532889
# Unit test for function memoize
def test_memoize():
    def factorial(n):
        return 1 if n < 2 else n * factorial(n - 1)

    factorial_memoized = memoize(
        factorial,
        key=lambda cacheItem, argument: cacheItem[0] == argument,
    )
    assert factorial_memoized(10) == 3628800
    assert factorial(10) == 3628800
    assert factorial(30) == factorial_memoized(30)

# Generated at 2022-06-14 04:02:18.661117
# Unit test for function curried_filter
def test_curried_filter():
    curried_filter_even = curried_filter(lambda x: bool(x % 2))
    curried_filter_odd = curried_filter(lambda x: not bool(x % 2))
    assert curried_filter(lambda x: bool(x % 2), [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 3, 5, 7, 9]
    assert curried_filter_even([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [2, 4, 6, 8]
    assert curried_filter_odd([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 3, 5, 7, 9]


# Generated at 2022-06-14 04:02:21.304342
# Unit test for function curried_filter
def test_curried_filter():
    greater_3 = curried_filter(lambda value: value > 3)
    assert greater_3([1, 4, 6, 8]) == [4, 6, 8]



# Generated at 2022-06-14 04:02:24.375886
# Unit test for function curry
def test_curry():
    assert eq(
        curry(lambda x, y: x + y)(1)(2),
        3
    )
    assert eq(
        curry(lambda x, y, z: x + y + z)(1)(2)(3),
        6
    )
    assert eq(
        curry(lambda x, y, z: x + y + z)(1)(2)(3),
        6
    )



# Generated at 2022-06-14 04:02:30.568919
# Unit test for function curried_filter
def test_curried_filter():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert curried_filter(lambda i: i % 2, arr) == [2, 4, 6, 8, 10]
    assert curried_filter(lambda i: i % 2)(arr) == [2, 4, 6, 8, 10]

    # Unit test for function identity

# Generated at 2022-06-14 04:02:40.878215
# Unit test for function cond
def test_cond():
    # test for "get" function
    test_cond.get = lambda key: lambda dictionary: dictionary.get(key, None)
    # test for "is" function

# Generated at 2022-06-14 04:02:43.261863
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(
        lambda item: item > 2,
        [1, 2, 3, 4, 5]
    ) == [3, 4, 5]



# Generated at 2022-06-14 04:03:18.697033
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(increase, [1, 2, 3]) == [2, 3, 4]



# Generated at 2022-06-14 04:03:31.555008
# Unit test for function memoize
def test_memoize():
    from unittest import TestCase

    def f(value):
        return value * value

    def g(value):
        return value + 1

    def h(value):
        return value * 2

    def test_memoize(result, expected_result):
        assert result == expected_result

    memoized_f = memoize(f)
    memoized_f_1 = memoize(f)
    memoized_g = memoize(g)
    memoized_h = memoize(h)
    # all memoized functions should be equal, but different from not memoized
    test_memoize(memoized_f, memoized_f)
    test_memoize(memoized_f, memoized_f_1)
    test_memoize(memoized_f, memoized_g)
    test

# Generated at 2022-06-14 04:03:42.737162
# Unit test for function cond
def test_cond():
    def func1(a, b):
        return a + b

    def func2(a, b):
        return a - b

    def func3(a, b):
        return a * b

    def func4(a, b):
        return a / b

    apply_func = cond([
        (lambda a, b: b == 0, func4),
        (lambda a, b: a == 0, func2),
        (lambda a, b: a > 0, func1),
        (lambda a, b: a < 0, func3),
    ])

    assert apply_func(2, 3) == 5
    assert apply_func(0, 3) == -3
    assert apply_func(0, 0) == 0
    assert apply_func(3, 0) == 0
    assert apply_func(1, -1)

# Generated at 2022-06-14 04:03:45.447486
# Unit test for function curried_filter
def test_curried_filter():
    print(curried_filter(lambda x: x > 3, [1, 2, 3, 4, 5]))  # [4, 5]



# Generated at 2022-06-14 04:03:48.263500
# Unit test for function curried_filter
def test_curried_filter():
    assert(curried_filter(lambda x: x == 1, [1, 2, 3]) == [1])



# Generated at 2022-06-14 04:03:56.768856
# Unit test for function cond
def test_cond():
    assert cond([(lambda x: x != 0, lambda x: 1)])(0) is None
    assert cond([(lambda x: x != 0, lambda x: 1)])(1) == 1

    assert cond([
        (lambda x: x != 0, lambda x: 1),
        (lambda x: x != 0, lambda x: 2)
    ])(0) is None
    assert cond([
        (lambda x: x != 0, lambda x: 1),
        (lambda x: x != 0, lambda x: 2)
    ])(1) == 1

    assert cond([
        (lambda x: x > 0, lambda x: 1),
        (lambda x: x == 0, lambda x: 2),
        (lambda x: x < 0, lambda x: 3)
    ])(-1) == 3

# Generated at 2022-06-14 04:04:01.072076
# Unit test for function find
def test_find():
    collection = [
        {'id': 1, 'name': 'Alice'},
        {'id': 2, 'name': 'Bob'},
    ]

    assert(find(collection, lambda i: i['id'] == 1) == {'id': 1, 'name': 'Alice'},
           'Should return first element that match filter')
    assert(find(collection, lambda i: i['id'] == 3) is None,
           'Should return None if no elements match filter')



# Generated at 2022-06-14 04:04:06.485329
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(eq('A'))(
        ['A', 'B', 'C']
    ) == ['A']

    assert curried_filter(eq(2))([1, 2, 3]) == [2]

    assert curried_filter(eq(1), [1, 2, 3]) == [1]



# Generated at 2022-06-14 04:04:08.135657
# Unit test for function eq
def test_eq():
    assert eq(1, 1)
    assert not eq(1, 2)



# Generated at 2022-06-14 04:04:10.987586
# Unit test for function curry
def test_curry():
    assert curry(lambda a, b, c, d: a + b + c + d)(1)(2)(3)(4) == 10


# Generated at 2022-06-14 04:07:23.698962
# Unit test for function cond
def test_cond():
    assert cond([
        (lambda a: a == 1, lambda a: '1'),
        (lambda a: a == 2, lambda a: '2')
    ])(1) == '1'

    assert cond([
        (lambda a: a == 1, lambda b: '1'),
        (lambda a: a == 2, lambda b: '2')
    ])(2) == '2'

    assert cond([
        (lambda a: a == 1, lambda a: '1'),
        (lambda a: a == 2, lambda a: '2'),
    ])(3) is None



# Generated at 2022-06-14 04:07:26.418263
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x >= 2)([1, 2, 3, 4, 5]) == [2, 3, 4, 5]

# Generated at 2022-06-14 04:07:32.377864
# Unit test for function eq
def test_eq():
    assert eq(1, 1) is True
    assert eq(1, 2) is False
    assert eq("A", "A") is True
    assert eq("A", "B") is False
    assert eq([1, 2], [1, 2]) is True
    assert eq([1, 2], [1, 3]) is False
    assert eq(True, True) is True
    assert eq(True, False) is False
    assert eq("", "") is True
    assert eq("", "A") is False
    assert eq(0, 0) is True
    assert eq(0, 1) is False


# Generated at 2022-06-14 04:07:40.040871
# Unit test for function curried_filter
def test_curried_filter():
    list_of_numbers = [1, 2, 3, 4, 5]
    assert curried_filter(lambda x: x % 2 == 1, list_of_numbers) == [1, 3, 5]
    assert curried_filter(lambda x: x > 3, list_of_numbers) == [4, 5]
    assert curried_filter(lambda x: x > 10, list_of_numbers) == []
    print("curried_filter ok")



# Generated at 2022-06-14 04:07:43.393562
# Unit test for function find
def test_find():
    assert find([1, 2, 3, 4], lambda x: x % 2 == 0) == 2
    assert find([1, 2, 3, 4], lambda x: x == 5) is None



# Generated at 2022-06-14 04:07:48.109087
# Unit test for function memoize
def test_memoize():
    import time

    fun = memoize(lambda x: time.sleep(1) or x)

    start = time.time()
    fun('a')
    end = time.time()
    assert end - start > 1

    start = time.time()
    fun('b')
    end = time.time()
    assert end - start < 1

    start = time.time()
    fun('a')
    end = time.time()
    assert end - start < 1

# Generated at 2022-06-14 04:07:50.695009
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(lambda x: x ** 2)([1, 2, 3]) == [1, 4, 9]

