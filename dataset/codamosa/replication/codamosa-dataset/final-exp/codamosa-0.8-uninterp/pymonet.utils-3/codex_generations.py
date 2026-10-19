

# Generated at 2022-06-14 03:58:03.535724
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda item: item < 2, [1, 2, 3, 4])(None) == \
        curried_filter(lambda item: item < 2)([1, 2, 3, 4])(None) == [1]



# Generated at 2022-06-14 03:58:06.143407
# Unit test for function find
def test_find():
    assert find([1, 2, 3, 4, 5], lambda x: x == 3) is 3
    assert find([1, 2, 3, 4, 5], lambda x: x == 8) is None



# Generated at 2022-06-14 03:58:10.444140
# Unit test for function find
def test_find():
    assert find([1, 2, 3, 4, 5], lambda x: x == 3) == 3
    assert find([1, 2, 3, 4, 5], lambda x: x == 6) is None


# Generated at 2022-06-14 03:58:14.004020
# Unit test for function find
def test_find():
    array = ['test', 'test1']
    result = find(array, lambda x: x == 'test1')
    assert result == 'test1'

    result = find(array, lambda x: x == 'test2')
    assert result is None


# Generated at 2022-06-14 03:58:22.082584
# Unit test for function cond
def test_cond():
    multiply_by_two = lambda v: v * 2
    multiply_by_three = lambda v: v * 3
    check_even = lambda v: v % 2 == 0

    function = cond([
        (check_even, multiply_by_two),
        (identity, multiply_by_three),
    ])

    assert function(1) == 3
    assert function(10) == 20


if __name__ == "__main__":
    test_cond()

# Generated at 2022-06-14 03:58:26.402798
# Unit test for function memoize
def test_memoize():
    def sum(values):
        return reduce(lambda a, b: a + b, values)

    memoized_sum = memoize(sum)

    assert memoized_sum([1, 2, 3, 4]) == 10
    assert memoized_sum([1, 2, 3, 4]) == 10
    assert memoized_sum is not sum



# Generated at 2022-06-14 03:58:31.209504
# Unit test for function eq
def test_eq():
    assert eq(1, 1)
    assert not eq(1, 2)
    assert not eq(1, 2)



# Generated at 2022-06-14 03:58:39.730538
# Unit test for function memoize
def test_memoize():
    cache: List[Any] = []

    function = lambda x: cache.append(x)
    memoized_function = memoize(function, key=identity)

    memoized_function(1)
    memoized_function(3)
    memoized_function(1)
    memoized_function(5)
    memoized_function(3)

    assert cache == [1, 3, 5]

# Generated at 2022-06-14 03:58:46.451816
# Unit test for function cond
def test_cond():
    def is_even(number):
        return number % 2 == 0

    def is_odd(number):
        return not is_even(number)

    conditions = [
        (is_even, lambda number: {'even': True, 'odd': False}),
        (is_odd, lambda number: {'even': False, 'odd': True}),
    ]

    result_function = cond(conditions)

    assert result_function(1) == {'even': False, 'odd': True}
    assert result_function(2) == {'even': True, 'odd': False}



# Generated at 2022-06-14 03:58:52.089506
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x >= 5)([9, 1, 2]) == [9]
    list_filter = curried_filter(lambda x: x >= 5)
    assert list_filter([9, 1, 2, 3, 4, 5, 6]) == [9, 5, 6]


# Generated at 2022-06-14 03:59:01.922301
# Unit test for function curried_map
def test_curried_map():
    """
    Function for testing curried_map function

    :returns: None
    :rtype: None
    """
    assert curried_map(identity)([1, 2, 3]) == [1, 2, 3]
    assert curried_map(increase)([1, 2, 3]) == [2, 3, 4]



# Generated at 2022-06-14 03:59:04.432127
# Unit test for function eq
def test_eq():
    assert eq(2, 2)
    assert eq("x", "x")
    assert not eq("x", "y")


# Generated at 2022-06-14 03:59:12.075612
# Unit test for function find
def test_find():
    list = [0, 1, 2, 3, 4]
    not_in_list = 5

    assert find(list, lambda x: x == 0) == 0
    assert find(list, lambda x: x == 1) == 1
    assert find(list, lambda x: x == 2) == 2
    assert find(list, lambda x: x == 3) == 3
    assert find(list, lambda x: x == 4) == 4
    assert find(list, lambda x: x == not_in_list) is None



# Generated at 2022-06-14 03:59:17.768346
# Unit test for function cond
def test_cond():
    def isOdd(i):
        return i % 2 != 0

    def isEven(i):
        return i % 2 == 0

    def add(i):
        return i + 1

    def sub(i):
        return i - 1

    func = cond(
        [(isEven, add), (isOdd, sub)]
    )

    assert func(0) == 1
    assert func(1) == 0
    assert func(2) == 3
    assert func(3) == 2



# Generated at 2022-06-14 03:59:22.520266
# Unit test for function find
def test_find():
    assert None == find([], eq(1))
    assert None == find(range(10), eq(10))
    assert 9 == find(range(10), eq(9))
    assert None == find(range(10), eq(-1))



# Generated at 2022-06-14 03:59:30.558456
# Unit test for function curried_filter
def test_curried_filter():
    print("Test for function curried_filter")
    filter_odd_numbers = curried_filter(lambda x: x % 2 != 0)
    first_filtered_collection = filter_odd_numbers([1, 2, 3, 4])
    second_filtered_collection = filter_odd_numbers([1, 2, 3, 4, 5])
    third_filtered_collection = filter_odd_numbers([2, 4, 5, 6, 7])
    assert first_filtered_collection == [1, 3]
    assert second_filtered_collection == [1, 3, 5]
    assert third_filtered_collection == [5, 7]
    print("OK")



# Generated at 2022-06-14 03:59:35.877954
# Unit test for function find
def test_find():
    assert find(list(range(5)), lambda x: x % 2 == 0) == 0
    assert find(list(range(5)), lambda x: x == 4) == 4
    assert find(list(range(5)), lambda x: x > 5) is None
    assert find(list(range(5)), lambda x: x % 6 == 0) is None


# Generated at 2022-06-14 03:59:39.793309
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(eq(2), [1, 2, 3]) == [2]
    assert curried_filter(eq(5), [1, 2, 3]) == []

# Generated at 2022-06-14 03:59:43.795927
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(eq(2))([1, 2]) == [2]
    assert curried_filter(eq(2))([1, 2, 2]) == [2, 2]
    assert curried_filter(eq(2))([1]) == []



# Generated at 2022-06-14 03:59:47.933693
# Unit test for function find
def test_find():
    assert find([], lambda x: True) is None
    assert find([1, 2, 3], eq(1)) == 1
    assert find([1, 2, 3], identity) == 2
    assert find([1, 2, 3], increase) == 3



# Generated at 2022-06-14 04:00:04.046918
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(identity)([1, 2, 3]) == [1, 2, 3]
    assert curried_map(increase)([1, 2, 3]) == [2, 3, 4]



# Generated at 2022-06-14 04:00:09.459478
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(lambda x: x + 1, [1, 2, 3]) == [2, 3, 4]

    add_1 = curried_map(lambda x: x + 1)
    
    assert add_1([1, 2, 3]) == [2, 3, 4]



# Generated at 2022-06-14 04:00:19.629643
# Unit test for function eq
def test_eq():
    assert eq(1)(1) == True
    assert eq(1)(2) == False
    assert eq(1)('a') == False
    assert eq('a')('a') == True
    assert eq('a')('b') == False
    assert eq('a')(1) == False
    assert eq([])([]) == True
    assert eq([1])([1]) == True
    assert eq([1])([]) == False
    assert eq([])([1]) == False
    assert eq([])(1) == False
    assert eq(1)([]) == False
    assert eq(1)([1]) == False
    assert eq([])('a') == False
    assert eq('a')([]) == False
    assert eq([1])('a') == False

# Generated at 2022-06-14 04:00:26.530219
# Unit test for function find
def test_find():
    collection = [
        {'count': 2, 'value': 3},
        {'count': 1, 'value': 4},
        {'count': 1, 'value': 1},
        {'count': 2, 'value': 1},
        {'count': 2, 'value': 1},
    ]
    item_count_1 = find(collection, lambda item: item['count'] == 1)
    item_count_2 = find(collection, lambda item: item['count'] == 2)
    assert item_count_1['value'] == 4
    assert item_count_2['value'] == 3



# Generated at 2022-06-14 04:00:31.318612
# Unit test for function eq
def test_eq():
    print('----- TEST EQ -----')
    values = [5, 4, '5', '5', None, None]
    assert (eq(5, 5) == True), "Test eq functtion fail"
    print("Test eq function: PASS")



# Generated at 2022-06-14 04:00:34.610429
# Unit test for function curried_map
def test_curried_map():
    curried_map_increase = curried_map(increase)
    assert curried_map_increase([1, 2, 3]) == [2, 3, 4]


# Generated at 2022-06-14 04:00:37.186910
# Unit test for function curry
def test_curry():
    assert curry(lambda a, b, c: a + b + c)(1)(2)(3) == 6



# Generated at 2022-06-14 04:00:41.417038
# Unit test for function memoize
def test_memoize():
    def foo(a):
        return a * a

    memofoo = memoize(foo, key=eq)
    assert memofoo(10) == foo(10)
    assert memofoo(10) == foo(10)


# Generated at 2022-06-14 04:00:45.030172
# Unit test for function find
def test_find():
    assert find(collection=[1, 2, 3, 4], key=lambda x: x == 5) is None
    assert find(collection=[1, 2, 3, 4], key=lambda x: x == 2) == 2



# Generated at 2022-06-14 04:00:53.774855
# Unit test for function memoize
def test_memoize():
    cached_function = memoize(lambda x: x + 1)
    assert cached_function(1) == 2
    assert cached_function(2) == 3
    assert cached_function(1) == 2
    assert cached_function(2) == 3
    assert cached_function(3) == 4
    assert cached_function(1) == 2
    assert cached_function(2) == 3
    assert cached_function(3) == 4
    assert cached_function(4) == 5
    assert cached_function(1) == 2
    assert cached_function(2) == 3
    assert cached_function(3) == 4
    assert cached_function(4) == 5
    assert cached_function(5) == 6



# Generated at 2022-06-14 04:01:03.320070
# Unit test for function curried_map
def test_curried_map():
    assert curried_map([1, 2, 3], increase) == [2, 3, 4]



# Generated at 2022-06-14 04:01:07.367025
# Unit test for function curried_map
def test_curried_map():
    args = [1, 2, 3]
    result = curried_map(identity)(args)
    assert result == [1, 2, 3]
    result = curried_map(increase)(args)
    assert result == [2, 3, 4]


# Generated at 2022-06-14 04:01:10.351254
# Unit test for function memoize
def test_memoize():
    def add(x):
        print('adding')
        return x + 1

    memoized = memoize(add)

    assert memoized(1) == 2
    memoized(1)



# Generated at 2022-06-14 04:01:13.088561
# Unit test for function find
def test_find():
    assert find([1, 2, 3], eq(2)) == 2
    assert find([1, 2, 3], eq(4)) is None



# Generated at 2022-06-14 04:01:16.863690
# Unit test for function find
def test_find():
    assert None == find([], eq(-1))
    assert -1 == find([-1, 0, 1], eq(-1))
    assert 0 == find([-1, 0, 1], eq(0))
    assert 1 == find([-1, 0, 1], eq(1))



# Generated at 2022-06-14 04:01:19.713328
# Unit test for function cond
def test_cond():
    assert cond([(lambda x: x == 1, increase),
                 (lambda x: x == 2, lambda x: x + 2)])(1) == 2



# Generated at 2022-06-14 04:01:22.743176
# Unit test for function eq
def test_eq():
    assert not eq(1, 2)
    assert eq(2, 2)
    assert not eq([1], 1)
    assert not eq(1, 2, 3)
    assert not eq('', 1)


# Generated at 2022-06-14 04:01:25.733376
# Unit test for function eq
def test_eq():
    assert eq(1)(2) is False
    assert eq(1)(1) is True
    assert eq(1, 2) is False
    assert eq(1, 1) is True



# Generated at 2022-06-14 04:01:31.964937
# Unit test for function find
def test_find():
    collection = [{'name': 'Tom', 'id': 1}, {'name': 'Jack', 'id': 2}]
    assert find(collection, lambda item: item['id'] == 1) == {'name': 'Tom', 'id': 1}
    assert find(collection, lambda item: item['id'] == 3) is None



# Generated at 2022-06-14 04:01:34.338461
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(increase)([1, 2, 3]) == [2, 3, 4]



# Generated at 2022-06-14 04:01:46.812593
# Unit test for function curry
def test_curry():
    curried_fn = curry(lambda x: x)
    assert curried_fn(1) == 1
    assert curried_fn(1)(2) == 1
    assert curry(lambda x, y=1: x + y)(2)(2) == 4
    assert curry(lambda x, y=1: x + y)(2, 2) == 4



# Generated at 2022-06-14 04:01:49.687738
# Unit test for function eq
def test_eq():
    assert eq(1, 1) == True
    assert eq(1, 2) == False
    assert eq(2, 1) == False



# Generated at 2022-06-14 04:01:56.058079
# Unit test for function find
def test_find():
    x = [{'a': 1}, {'a': 10}, {'a': 11}, {'a': 14}, {'a': 17}, {'a': 17}]
    assert find(x, lambda x: x['a'] == 11) == {'a': 11}
    assert find(x, lambda x: x['a'] == 16) is None



# Generated at 2022-06-14 04:02:01.109954
# Unit test for function curry
def test_curry():
    x = curry(lambda x, y, z: x + y * z)
    x2 = x(2)(3)(4)
    x3 = x(3)(3)(3)
    assert x2 == 14
    assert x3 == x2
    assert x is not x2



# Generated at 2022-06-14 04:02:07.639543
# Unit test for function find
def test_find():
    assert find([1, 2, 3], eq(2)) == 2
    assert find(['a', 'b', 'c'], lambda x: x == 'b') == 'b'
    assert find([3, 2, 1], lambda x: x == 4) is None
    assert find(['a', 'B', 'c'], eq('c')) == 'c'


# Generated at 2022-06-14 04:02:12.028849
# Unit test for function memoize
def test_memoize():
    def add_5(x):
        print("In add_5")
        return x + 5

    m_add_5 = memoize(add_5)
    print(m_add_5(1))


if __name__ == '__main__':
    test_memoize()

# Generated at 2022-06-14 04:02:17.842005
# Unit test for function curried_map
def test_curried_map():
    # abc to Abc
    assert curried_map(lambda x: x.capitalize())(list('abc')) == list('Abc')

    # abc to Abc
    assert curried_map(lambda x: x.capitalize())('abc') == 'Abc'

    # [1, 2, 3] to [2, 3, 4]
    assert curried_map(increase)([1, 2, 3]) == [2, 3, 4]

    # (1, 2, 3) to (2, 3, 4)
    assert curried_map(increase)((1, 2, 3)) == (2, 3, 4)



# Generated at 2022-06-14 04:02:19.152404
# Unit test for function eq
def test_eq():
    assert eq(1, 1)
    assert eq(2, 2)
    assert not eq(1, 2)



# Generated at 2022-06-14 04:02:27.338290
# Unit test for function memoize
def test_memoize():
    # Tests for function

    # Case 1: function without arg
    def function_without_arg(value):
        function_without_arg.called += 1
        return value + 1

    function_without_arg.called = 0
    assert function_without_arg(1) == 2
    assert function_without_arg.called == 1
    assert function_without_arg(2) == 3
    assert function_without_arg.called == 2

    function_without_arg.called = 0
    assert memoize(function_without_arg)(1) == 2
    assert function_without_arg.called == 1
    assert memoize(function_without_arg)(1) == 2
    assert function_without_arg.called == 1
    assert memoize(function_without_arg)(2) == 3
    assert function_without_arg.called == 2



# Generated at 2022-06-14 04:02:29.480495
# Unit test for function eq
def test_eq():
    assert eq(1, 1) == True
    assert eq(1, 2) == False


# Generated at 2022-06-14 04:02:41.463802
# Unit test for function cond
def test_cond():
    assert cond([(lambda x: x == 2, identity)])(2) == 2
    assert cond([(lambda x: x == 2, identity)])(3) is None
    assert cond([(lambda x: x == 3, identity), (lambda x: x == 2, increase)])(3) == 4
    assert cond([(lambda x: x == 3, identity), (lambda x: x == 2, increase)])(2) is None

# Generated at 2022-06-14 04:02:44.791598
# Unit test for function find
def test_find():
    list_to_find = [1, 2, 3, 4, 5]
    assert find(list_to_find, lambda x: x == 2) == 2
    assert find(list_to_find, lambda x: x == 20) is None



# Generated at 2022-06-14 04:02:49.285112
# Unit test for function curried_map
def test_curried_map():
    list_of_numbers = [1, 2, 3, 4, 7, 8]
    increase_all = curried_map(increase)
    increased_list = increase_all(list_of_numbers)
    assert increased_list == [2, 3, 4, 5, 8, 9]



# Generated at 2022-06-14 04:02:50.734462
# Unit test for function eq
def test_eq():
    assert eq(1)(1)
    assert not eq(1)(2)


# Generated at 2022-06-14 04:02:52.620675
# Unit test for function curried_filter
def test_curried_filter():
    arr = [1, 2, 3, 4, 5, 6]

    def fn(x):
        return x % 2 == 1

    assert curried_filter(fn, arr) == [1, 3, 5]



# Generated at 2022-06-14 04:02:57.453174
# Unit test for function curried_filter
def test_curried_filter():
    collection = list(range(10))
    result_collection = curried_filter(lambda x: x % 3 == 0)(collection)
    assert result_collection == [0, 3, 6, 9]

    result_collection = curried_filter(lambda x: x % 3 == 0, collection)
    assert result_collection == [0, 3, 6, 9]



# Generated at 2022-06-14 04:03:02.271776
# Unit test for function find
def test_find():
    """
    >>> collection = [1, 2, 3]
    >>> find(collection, lambda x: x % 2 == 0)
    2
    >>> find(collection, lambda x: x == 4)

    """
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 04:03:07.936425
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(identity, ['a', 2, 'b']) == ['a', 2, 'b']
    assert curried_map(identity)(['a', 2, 'b']) == ['a', 2, 'b']
    assert curried_map(increase)([1, 2, 3]) == [2, 3, 4]



# Generated at 2022-06-14 04:03:11.053059
# Unit test for function curried_filter
def test_curried_filter():
    list = [1, 2, 3, 4]
    assert curried_filter(lambda x: x % 2 == 0)(list) == [2, 4]


# Generated at 2022-06-14 04:03:18.310387
# Unit test for function cond
def test_cond():
    def ids(value):
        return value

    def test(value):
        return value

    def a(value):
        return value

    def b(value):
        return value

    assert cond([
        (test, a)
    ])("ok") == "ok"

    assert cond([
        (test, a),
        (test, b)
    ])("ok") == "ok"

    assert cond([
        (ids, a),
        (test, b)
    ])("ok") == "ok"



# Generated at 2022-06-14 04:03:29.306374
# Unit test for function memoize
def test_memoize():
    def adder(number):
        print('called')
        return number + 1

    inner_func = memoize(adder)
    result = inner_func(1)
    assert result == 2

    result = inner_func(1)
    assert result == 2

# Generated at 2022-06-14 04:03:33.002629
# Unit test for function find
def test_find():
    """
    Unit test for function find
    """
    assert find([], eq(0)) is None
    assert find([], identity) is None
    assert find([1], eq(2)) is None
    assert find([0], identity) == 0
    assert find([1, 2], eq(1)) == 1
    assert find([1, 2, 3], eq(3)) == 3
    assert find([1, 2, 3], identity) == 1
    return True



# Generated at 2022-06-14 04:03:44.315609
# Unit test for function cond
def test_cond():
    assert cond([(lambda x: x < 0, lambda x: x * (-1))])(-2) == 2
    assert cond([(lambda x: x < 0, lambda x: x * (-1)),
                 (lambda x: x > 0, lambda x: x * 2)])(-2) == 2
    assert cond([(lambda x: x == 0, lambda x: x * 2),
                 (lambda x: x < 0, lambda x: x * (-1)),
                 (lambda x: x > 0, lambda x: x * 2)])(2) == 4

    assert cond([(lambda x: x < 0, lambda x: x * (-1))])(2) is None
    assert cond([(lambda x: x < 0, lambda x: x * (-1)),
                 (lambda x: x > 0, lambda x: x * 2)])(2)

# Generated at 2022-06-14 04:03:46.624947
# Unit test for function curried_filter
def test_curried_filter():
    def is_even(x):
        return x % 2 == 0

    collection = list(range(100))
    curried_filter_func = curried_filter(is_even)
    is_not_even = curried_filter(lambda x: x % 2 == 1)
    print(curried_filter_func(collection))
    print(is_not_even(collection))


# Generated at 2022-06-14 04:03:48.358369
# Unit test for function curry
def test_curry():
    assert (curry(lambda x, y: x + y)(1)(2) == 3)



# Generated at 2022-06-14 04:03:56.822403
# Unit test for function curry
def test_curry():
    """
    Unit test for function curry
    """
    assert identity(1) == 1
    assert identity(True) is True
    assert identity("abc") == "abc"
    assert identity([1, 2, 3]) == [1, 2, 3]
    assert identity({"a": "b"}) == {"a": "b"}
    assert curry(identity)(1) == 1
    assert curry(identity)(True) is True
    assert curry(identity)("abc") == "abc"
    assert curry(identity)([1, 2, 3]) == [1, 2, 3]
    assert curry(identity)({"a": "b"}) == {"a": "b"}

    assert increase(1) == 2
    assert increase(True) is 2
    assert increase("abc") is None

# Generated at 2022-06-14 04:04:00.306437
# Unit test for function memoize
def test_memoize():
    @memoize
    def calculate(n):
        if n <= 2:
            return n
        return calculate(n - 1) + calculate(n - 2)

    calculate(100)
    assert calculate(100) == 354224848179261915075
    assert calculate(50) == 12586269025



# Generated at 2022-06-14 04:04:08.893360
# Unit test for function find
def test_find():
    collection = [
        {
            "name": "den",
            "age": 12
        },
        {
            "name": "john",
            "age": 14
        },
        {
            "name": "emily",
            "age": 16
        }
    ]
    result = find(collection, lambda item: item["age"] == 25)
    assert result is None, "Function find return not None for collection without keys"

    result = find(collection, lambda item: item["age"] == 12)
    assert result["name"] == "den", "Function find return not true value"


# Generated at 2022-06-14 04:04:12.958230
# Unit test for function curried_filter
def test_curried_filter():
    a = [1,2,3,4,5]
    f = curried_filter(lambda x: x % 2 == 0)
    assert f(a) == [2, 4]


# Generated at 2022-06-14 04:04:19.665632
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(lambda item: item + 1, [1, 2, 3]) == [2, 3, 4]
    assert curried_map(lambda item: item + 1)([1, 2, 3]) == [2, 3, 4]
    assert curried_map(lambda item: item + 1, [1, 2, 3]) == [2, 3, 4]
    assert curried_map(lambda item: item + 1)([1, 2, 3]) == [2, 3, 4]



# Generated at 2022-06-14 04:04:29.098793
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(lambda x: x+7)([1, 2, 3]) == [8, 9, 10]


# Generated at 2022-06-14 04:04:36.330149
# Unit test for function curried_filter
def test_curried_filter():
    def is_even(value):
        return value % 2 == 0
    result = curried_filter(is_even)([1, 0, 2, 3, 4])
    assert result == [0, 2, 4]
    # test with more filter
    more_filter = curried_filter(is_even)
    result = more_filter([1, 0, 2, 3, 4])
    assert result == [0, 2, 4]


# Generated at 2022-06-14 04:04:38.736175
# Unit test for function memoize
def test_memoize():
    square = memoize(lambda x: x * x)
    assert square(4) == 16
    assert square(5) == 25
    assert square(4) == 16
    assert square(5) == 25

# Generated at 2022-06-14 04:04:42.376114
# Unit test for function find
def test_find():
    assert find(['a', 'b', 'c'], key=eq('a')) == 'a'
    assert find(['a', 'b', 'c'], key=eq('d')) is None



# Generated at 2022-06-14 04:04:45.910215
# Unit test for function cond
def test_cond():
    assert cond([
        (
            lambda arg: arg == 'a',
            lambda arg: arg + 'b'
        ),
        (
            lambda arg: arg == 'b',
            lambda arg: arg + 'c'
        ),
    ])('a') == 'ab'



# Generated at 2022-06-14 04:04:56.078028
# Unit test for function cond
def test_cond():
    is_even = lambda x: x % 2 == 0
    is_odd = lambda x: x % 2 != 0
    even_func = lambda x: x*2
    odd_func = lambda x: x*3
    none_func = lambda x: None
    assert cond([(is_even, even_func), (is_odd, odd_func)])(42) == 84
    assert cond([(is_even, even_func), (is_odd, odd_func)])(43) == 129
    assert cond([(is_even, even_func), (is_odd, odd_func)])(42) == 84
    assert cond([(is_even, even_func), (is_odd, odd_func)])(43) == 129
    assert cond([(is_even, even_func), (is_odd, odd_func)])(44)

# Generated at 2022-06-14 04:05:00.766983
# Unit test for function curried_filter
def test_curried_filter():
    def is_not_even(value: int) -> bool:
        return value % 2 != 0

    curried_is_not_even = curried_filter(is_not_even)
    assert curried_is_not_even([1, 2, 3, 4, 5]) == [1, 3, 5]


# Generated at 2022-06-14 04:05:12.914593
# Unit test for function cond
def test_cond():
    test_data = [
        (1, 'val 1'),
        (5, 'val 5'),
        (10, 'val 10'),
        (15, 'val 15'),
    ]

    test_data_map = [
        (x[0], x[1]) for x in test_data
    ]

    test_data_accumulator = [
        (x[0], x[1]) for x in test_data
    ]

    iterator = iter(test_data)

# Generated at 2022-06-14 04:05:15.327634
# Unit test for function eq
def test_eq():
    assert eq(1, 1) == True
    assert eq(1, 2) == False
    assert eq(2, 1) == False
    assert eq(2, 2) == True
    assert eq(1, 1, 1) == False



# Generated at 2022-06-14 04:05:18.370290
# Unit test for function eq
def test_eq():
    assert eq(1, 1)
    assert not eq(1, 2)
    assert eq(1, eq(1))



# Generated at 2022-06-14 04:05:35.459595
# Unit test for function eq
def test_eq():
    """
    Test for function eq
    """
    assert eq(3,3) == True
    assert eq(6,5) == False


# Generated at 2022-06-14 04:05:40.558934
# Unit test for function curried_filter
def test_curried_filter():
    collection = [0, 1, 2, 3, 4, 5]
    is_even = lambda x: x % 2 == 0
    assert curried_filter(is_even, collection) == [0, 2, 4]

    collection = [0, 1, 2, 3, 4, 5]
    is_even = lambda x: x % 2 == 0
    assert curried_filter(is_even)(collection) == [0, 2, 4]



# Generated at 2022-06-14 04:05:53.315455
# Unit test for function curried_filter
def test_curried_filter():
    greater_than_0 = curried_filter(lambda number: number > 0)
    lower_than_3 = curried_filter(lambda number: number < 3)
    lower_than_4 = curried_filter(lambda number: number < 4)
    greater_than_4 = curried_filter(lambda number: number > 4)

    assert [1, 2] == greater_than_0([1, 2, 3])
    assert [1, 2, 3] == greater_than_0([-10, 1, 2, -12, 3])
    assert [1] == lower_than_3([1, 2, 3])
    assert [1, 2] == lower_than_3([1, 2])
    assert [1, 2, 3] == lower_than_4([1, 2, 3])

# Generated at 2022-06-14 04:05:55.802975
# Unit test for function find
def test_find():
    lst = [1, 2, 3, 4, 5]

    assert find(lst, lambda x: x == 3) == 3
    assert find(lst, lambda x: x == 6) is None



# Generated at 2022-06-14 04:06:01.865896
# Unit test for function eq
def test_eq():
    assert eq(5, 5)
    assert not eq(5, 6)
    assert not eq(5, None)
    assert eq(5, 5, 5)
    assert not eq(5, 5, 6)
    assert not eq(5, 6, 5) \
           and not eq(6, 5, 5)



# Generated at 2022-06-14 04:06:06.628055
# Unit test for function curried_map
def test_curried_map():
    collection = [1, 2, 3]
    mapper = lambda x: x * 2
    result = [2, 4, 6]
    assert curried_map(mapper, collection) == result
    assert curried_map(mapper)(collection) == result


# Generated at 2022-06-14 04:06:16.404812
# Unit test for function cond
def test_cond():
    first_function = cond([
        (lambda value: value < 0, lambda value: value * -1),
        (lambda value: value == 0, lambda value: 0),
        (lambda value: value > 0, lambda value: value)
    ])
    second_function = cond([
        (lambda value: value < 0, lambda value: -1),
        (lambda value: value == 0, lambda value: 0),
        (lambda value: value > 0, lambda value: 1)
    ])
    third_function = cond([
        (lambda value: value < 0, lambda value: 'less then zero'),
        (lambda value: value == 0, lambda value: 'is zero'),
        (lambda value: value > 0, lambda value: 'greater then zero')
    ])
    assert first_function(1) == 1

# Generated at 2022-06-14 04:06:25.311368
# Unit test for function curried_filter
def test_curried_filter():
    def is_even(number):
        return True if number % 2 == 0 else False

    curried_filter_odd = curried_filter(curried_filter(is_even))
    assert curried_filter_odd([2, 3, 4, 6, 7, 8]) == \
                curried_filter(is_even)([2, 3, 4, 6, 7, 8]) == \
                curried_filter(is_even)(curried_filter(is_even)([2, 3, 4, 6, 7, 8])) == \
                [2, 4, 6, 8]



# Generated at 2022-06-14 04:06:26.056561
# Unit test for function eq
def test_eq():
    assert eq(0, 0), False



# Generated at 2022-06-14 04:06:28.968126
# Unit test for function find
def test_find():
    assert find([1, 2, 3], eq(2)) == 2
    assert find([1, 2, 3], eq(4)) is None



# Generated at 2022-06-14 04:07:29.085680
# Unit test for function curried_filter
def test_curried_filter():
    list_of_numbers = [1, 2, 3, 4]
    list_of_even_numbers = curried_filter(lambda x: x % 2 == 0, list_of_numbers)
    assert len(list_of_even_numbers) == 2



# Generated at 2022-06-14 04:07:35.078017
# Unit test for function memoize
def test_memoize():
    def sum_factorial(n):
        def factorial(n):
            if n == 0:
                return 1
            return n * factorial(n - 1)

        return sum(map(factorial, range(n)))

    factorial_sum: Callable[[int], int] = memoize(sum_factorial)
    print(factorial_sum(5))



# Generated at 2022-06-14 04:07:39.160459
# Unit test for function find
def test_find():
    assert find([1, 2, 3], eq(2)) == 2
    assert find([1, 2, 3], eq(5)) is None
    assert find([], eq(1)) is None



# Generated at 2022-06-14 04:07:48.167450
# Unit test for function memoize
def test_memoize():
    import random
    from operator import add, mul

    def random_func():
        return random.randint(1, 100)

    def add_one(x):
        return x + 1

    def mul_one(x):
        return x * 1

    def adder(a, b):
        return a + b

    def multiplier(a, b):
        return a * b

    memoized = memoize(random_func)
    assert memoized() == memoized()
    memoized = memoize(add_one)
    assert memoized(5) == memoized(5)
    memoized = memoize(mul_one)
    assert memoized(5) == memoized(5)
    memoized = memoize(adder, eq)
    assert memoized(5, 5) == memoized(5, 5)
    memo

# Generated at 2022-06-14 04:07:53.208096
# Unit test for function curried_map
def test_curried_map():
    curry_map = curry(curried_map)
    curry_mult_by_2 = curry_map(lambda x: x * 2)
    assert curry_mult_by_2([1, 2, 3]) == [2, 4, 6]


# Generated at 2022-06-14 04:07:56.742406
# Unit test for function memoize
def test_memoize():
    def memoized(x):
        print('memoized called')
        return x

    m = memoize(memoized)
    assert m(1) == 1
    assert m(1) == 1

