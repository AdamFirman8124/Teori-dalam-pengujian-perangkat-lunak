

# Generated at 2022-06-14 03:57:57.114251
# Unit test for function curry
def test_curry():
    """
    Currying test.
    """
    def add(a, b, c):
        return a + b + c

    curried_add = curry(add)
    assert curried_add(1, 2, 3) == 6
    assert curried_add(1, 2)(3) == 6
    assert curried_add(1)(2, 3) == 6
    assert curried_add(1)(2)(3) == 6



# Generated at 2022-06-14 03:58:01.474205
# Unit test for function find
def test_find():
    print("test_find")
    assert find([1, 2, 3], eq(2)) == 2
    assert find([1, 2, 3], eq(5)) is None
    print("test_find - PASS")



# Generated at 2022-06-14 03:58:06.612483
# Unit test for function find
def test_find():
    assert find([1, 2, 3, 4], eq(5)) is None
    assert find([1, 2, 3, 4], eq(1)) is 1
    assert find([1, 2, 3, 4], eq(2)) is 2
    assert find([1, 2, 3, 4], eq(3)) is 3
    assert find([1, 2, 3, 4], eq(4)) is 4



# Generated at 2022-06-14 03:58:09.246710
# Unit test for function find
def test_find():
    assert find([1], eq(1)) == 1
    assert find([1], eq(2)) is None



# Generated at 2022-06-14 03:58:11.364480
# Unit test for function curried_map
def test_curried_map():
    curried_map_list = curried_map(lambda x: x + 1, [1, 2, 3])
    assert curried_map_list == [2, 3, 4]



# Generated at 2022-06-14 03:58:17.023481
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(increase)([1, 2, 3]) == [2, 3, 4]



# Generated at 2022-06-14 03:58:25.003373
# Unit test for function find
def test_find():
    assert find([5, 6, 7, 8, 9], lambda value: value == 7) == [7]
    assert find([5, 6, 7, 8, 9], lambda value: value > 7) == [8, 9]
    assert find([5, 6, 7, 8, 9], lambda value: value < 0) is None



# Generated at 2022-06-14 03:58:39.256242
# Unit test for function memoize
def test_memoize():
    def callableFn(x):
        return x * x + 1

    cache = []

    def spyFn(x):
        cache.append(x)
        return callableFn(x)

    memoizedFn = memoize(spyFn)
    assert memoizedFn(1) == 2
    assert memoizedFn(1) == 2
    assert cache == [1]
    assert memoizedFn(2) == 5
    assert memoizedFn(2) == 5
    assert cache == [1, 2]
    memoizedFn = memoize(spyFn, eq)
    assert memoizedFn(1) == 2
    assert memoizedFn(1) == 2
    assert cache == [1, 2, 1]
    assert memoizedFn(2) == 5
    assert memo

# Generated at 2022-06-14 03:58:44.066565
# Unit test for function curry
def test_curry():
    def add(a, b, c):
        return a + b + c

    assert curry(add)(5, 7, 8) == 20
    assert curry(add, 2)(5, 7) == 12
    assert curry(add, 2)(5)(7) == 12
    assert curry(add, 3)(5)(7)(8) == 20



# Generated at 2022-06-14 03:58:49.726034
# Unit test for function find
def test_find():
    assert find([1, 2, 3], lambda x: x == 1) == 1
    assert find([1, 2, 3], lambda x: x == 5) is None
    assert find(['a', 'b', 'c'], lambda x: x == 'a') == 'a'
    assert find(['a', 'b', 'c'], lambda x: x == 'e') is None
    assert find([1, 'a', 'b', 2, True, False], lambda x: isinstance(x, int)) == 1
    assert find([1, 'a', 'b', 2, True, False], lambda x: isinstance(x, float)) is None


# Generated at 2022-06-14 03:59:06.512528
# Unit test for function find
def test_find():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    assert (find(a, lambda x: x == 1)) == 1
    assert (find(a, lambda x: x == 5)) == 5
    assert (find(a, lambda x: x == 10)) == 10
    assert (find(a, lambda x: x == 11)) is None


# Generated at 2022-06-14 03:59:09.120969
# Unit test for function curried_filter
def test_curried_filter():
    assert [1, 2] == curried_filter(lambda x: x < 2)([1, 2, 3])

# Generated at 2022-06-14 03:59:12.725637
# Unit test for function curry
def test_curry():
    def square(x, y):
        return x**y
    square_curry = curry(square)
    assert square_curry(2)(3) == square(2, 3)



# Generated at 2022-06-14 03:59:17.984276
# Unit test for function curried_map
def test_curried_map():
    curried_map_identity = curried_map(identity)
    curried_map_increase = curried_map(increase)
    assert [identity(i) for i in range(5)] == curried_map_identity(range(5))
    assert [increase(i) for i in range(5)] == curried_map_increase(range(5))



# Generated at 2022-06-14 03:59:25.049511
# Unit test for function curried_filter
def test_curried_filter():
    # Set value of filter function
    filter_f = lambda x: x >= 3

    # Set value of filter list
    filter_l = [1, 2, 3, 4]

    # Set expected value of filter function
    filter_e = [3, 4]

    # Get result of curried_filter
    filter_r = curried_filter(filter_f, filter_l)

    # Check that result is equal to expected value
    assert filter_r == filter_e

# Generated at 2022-06-14 03:59:27.658492
# Unit test for function eq
def test_eq():
    assert eq(1, 1) == True, "first value equal second"
    assert eq(1, 2) == False, "first value not equal second"



# Generated at 2022-06-14 03:59:33.241663
# Unit test for function find
def test_find():
    """
    Unit test for function find.
    """
    assert find([1, 2, 3], lambda item: item == 2) == 2
    assert find([1, 2, 3], lambda item: True) == 1
    assert find([1, 2, 3], lambda item: False) is None



# Generated at 2022-06-14 03:59:39.107450
# Unit test for function cond
def test_cond():
    cond_result = cond([
        (lambda x: x == 0, identity),
        (lambda x: x > 0, increase),
        (lambda x: True, identity)
    ])
    assert cond_result(0) == 0
    assert cond_result(100) == 101
    assert cond_result(-100) == -100



# Generated at 2022-06-14 03:59:43.171957
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(lambda x: x + 1)([1, 2, 3]) == [2, 3, 4]
    assert curried_map([1, 2, 3])(lambda x: x + 1) == [2, 3, 4]



# Generated at 2022-06-14 03:59:45.078368
# Unit test for function find
def test_find():
    assert find([0, 1, 3, 2], eq(0)) == 0
    assert find([0, 1, 3, 2], eq(2)) == 2
    assert find([0, 1, 3, 2], eq(4)) is None

# Generated at 2022-06-14 04:00:08.695241
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(increase, [1, 2, 3]) == [2, 3, 4]
    assert curried_map(lambda x: x, [1, 2, 3]) == [1, 2, 3]
    assert curried_map(lambda x: x**2, [1, 2, 3]) == [1, 4, 9]
    assert curried_map(lambda x: x**2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144]



# Generated at 2022-06-14 04:00:15.744301
# Unit test for function memoize
def test_memoize():
    assert memoize(identity)(5) == 5
    assert memoize(identity)(5) == 5
    assert memoize(identity)(5) == 5

    assert memoize(increase)(5) == 6
    assert memoize(increase)(5) == 6
    assert memoize(increase)(5) == 6

    assert memoize(increase)(5) != 7
    assert memoize(increase)(5) != 7
    assert memoize(increase)(5) != 7



# Generated at 2022-06-14 04:00:22.012154
# Unit test for function curried_filter
def test_curried_filter():
    collection = curried_filter(lambda x: x if x % 2 == 0 else None)([1, 2, 3, 4])
    assert collection == [2, 4]
    collection = curried_filter(eq('a'), ['a', 'b', 'c'])
    assert collection == ['a']
    collection = curried_filter(eq('a'), [])
    assert collection == []



# Generated at 2022-06-14 04:00:29.816516
# Unit test for function memoize
def test_memoize():
    def multiply(a, b):
        return a * b

    # Assert function multiply is not cached
    assert multiply(1, 5) == 5
    assert multiply(1, 5) == 5
    # Assert function multiply is cached
    multiply = memoize(multiply)
    assert multiply(1, 5) == 5
    assert multiply(1, 5) == 5

# Generated at 2022-06-14 04:00:32.107130
# Unit test for function curried_filter
def test_curried_filter():
    array = [1, 2, 3, 4, 5]
    filter_fn = curried_filter(lambda x: x % 2 == 0)
    filter_result = filter_fn(array)
    ass

# Generated at 2022-06-14 04:00:34.905139
# Unit test for function find
def test_find():
    assert find([1, 2, 3], lambda x: x == 2) == 2
    assert find([1, 2, 3], lambda x: x == 4) is None



# Generated at 2022-06-14 04:00:38.863247
# Unit test for function curried_filter
def test_curried_filter():
    """
    Test curried_filter function
    """
    a = range(6)
    b = curried_filter(lambda s: s % 2 == 0, a)
    assert b == [0, 2, 4]


# Generated at 2022-06-14 04:00:41.762777
# Unit test for function eq
def test_eq():
    assert eq(1, 1)
    assert not eq(1, 2)


# Generated at 2022-06-14 04:00:49.191387
# Unit test for function curry
def test_curry():
    def sum(a, b):
        return a + b

    func = curry(sum)
    assert func(1)(2) == 3
    assert func(1, 2) == 3
    assert func(1, 2, 3) == 3

    func = curry(sum, 3)
    assert func(1, 2, 3) == 6
    assert func(1, 2)(3) == 6
    assert func(1)(2, 3) == 6
    assert func(1)(2)(3) == 6



# Generated at 2022-06-14 04:00:52.847827
# Unit test for function curried_map
def test_curried_map():
    collection = [1, 2, 3, 4]
    assert curried_map(lambda x: x * 2)(collection) == [2, 4, 6, 8]
    assert curried_map(lambda x: x * 2, collection) == [2, 4, 6, 8]



# Generated at 2022-06-14 04:01:16.731928
# Unit test for function find
def test_find():
    col = [1, 2, 3, 4, 5]
    assert find(col, lambda x: x > 2) == 3



# Generated at 2022-06-14 04:01:24.750966
# Unit test for function curried_filter
def test_curried_filter():
    assert (curried_filter(lambda x: x > 3, [1, 2, 3, 4, 5])) == [4, 5]
    assert (curried_filter(lambda x: x > 3)(
        [1, 2, 3, 4, 5])) == [4, 5]
    assert (curried_filter(lambda x: x % 2 == 0)(
        [1, 2, 3, 4, 5])) == [2, 4]
    assert (curried_filter(lambda x: x > 3)(
        [1, 2, 3, 4, 5]) == [4, 5])



# Generated at 2022-06-14 04:01:29.066652
# Unit test for function memoize
def test_memoize():
    @memoize
    def add_one_to(x):
        print("Adding 1 to", x)
        return x + 1

    print(add_one_to(3))
    print(add_one_to(3))
    print(add_one_to(3))
    print(add_one_to(3))

# Generated at 2022-06-14 04:01:37.168341
# Unit test for function eq
def test_eq():
    # Given
    first_value = 'first value'
    second_value = 'second value'
    third_value = 'first value'

    # When
    first_is_equal_to_second = eq(first_value, second_value)
    first_is_equal_to_third = eq(first_value, third_value)

    # Then
    assert not first_is_equal_to_second
    assert first_is_equal_to_third


# Generated at 2022-06-14 04:01:42.731766
# Unit test for function memoize
def test_memoize():
    def square(number):
        return number ** 2

    square_memoized = memoize(square)

    assert square_memoized(3) == 9, 'memoize: square(3) == 9'
    assert square_memoized(5) == 25, 'memoize: square(5) == 25'
    assert square_memoized(3) == 9, 'memoize: square(3) == 9'
# -----------------------------------------------



# Generated at 2022-06-14 04:01:46.949976
# Unit test for function curried_map
def test_curried_map():
    """
    Testing function curried_map.
    """
    assert curried_map(lambda x: x + 1)([1, 2, 3]) == [2, 3, 4]



# Generated at 2022-06-14 04:01:52.925017
# Unit test for function find
def test_find():
    """
    Test for function find.

    :returns: AssertionError if test failed
    :rtype: AssertionError
    """
    assert find([1, 2, 3, 4], lambda item: item == 3) == 3
    assert find([1, 2, 3, 4], lambda item: item == 5) is None



# Generated at 2022-06-14 04:02:00.045094
# Unit test for function curry
def test_curry():
    assert (curry(lambda x: x + 1)(5) == 6)
    assert (curry(lambda x, y: x + y, 2)(5, 6) == 11)
    assert (curry(lambda x, y: x + y, 2)(5)(6) == 11)
    assert (curry(lambda x, y, z: x + y + z, 3)(5)(6)(7) == 18)



# Generated at 2022-06-14 04:02:11.975989
# Unit test for function cond
def test_cond():
    def condition_one(value):
        return value == 1

    def execute_one(value):
        return value + 1

    def condition_two(value):
        return value > 2

    def execute_two(value):
        return value - 1

    def condition_three(value):
        return True

    def execute_three(value):
        return value

    cond_function = cond([
        (condition_one, execute_one),
        (condition_two, execute_two),
        (condition_three, execute_three),
    ])
    assert cond_function(1) == 2
    assert cond_function(2) == 3
    assert cond_function(3) == 2
    assert cond_function(4) == 3



# Generated at 2022-06-14 04:02:18.622038
# Unit test for function find
def test_find():
    # Unit test for function find
    personList = [
        {
            'name': 'name1',
            'surname': 'surname1',
        },
        {
            'name': 'name2',
            'surname': 'surname2',
        },
        {
            'name': 'name3',
            'surname': 'surname3',
        },
    ]
    assert find(personList, lambda item: item['name'] == 'name2') == {
        'name': 'name2',
        'surname': 'surname2',
    }
    assert find(personList, lambda item: item['name'] == 'name4') is None



# Generated at 2022-06-14 04:02:33.323180
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(identity)([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert curried_map(increase)([1, 2, 3, 4]) == [2, 3, 4, 5]
    assert curried_map(increase)(range(0, 51)) == list(range(1, 51))


# Generated at 2022-06-14 04:02:35.439898
# Unit test for function find
def test_find():
    eq_(find([1, 2, 3, 4, 5], lambda x: x % 2 == 0), 2)


# Generated at 2022-06-14 04:02:38.972414
# Unit test for function memoize
def test_memoize():
    func = lambda n: n**n

    mem_func = memoize(func)

    assert mem_func(2) == 4
    assert mem_func(2) == 4
    assert mem_func(2) == 4


# Generated at 2022-06-14 04:02:41.773023
# Unit test for function find
def test_find():
    assert None == find([], identity)
    assert 2 == find([1, 2, 3, 4], eq(2))
    assert None == find([1, 2, 3, 4], eq(99))

# Generated at 2022-06-14 04:02:44.065473
# Unit test for function find
def test_find():
    assert find([1, 2, 3], lambda x: x == 2) == 2
    assert find([1, 2, 3], lambda x: x == 5) == None

# Generated at 2022-06-14 04:02:50.544593
# Unit test for function memoize
def test_memoize():
    memoized_add = memoize(lambda x: x + 1)
    print('memoized_add(1) = ', memoized_add(1))
    print('memoized_add(2) = ', memoized_add(2))
    print('memoized_add(1) = ', memoized_add(1))
    print('memoized_add(1) = ', memoized_add(1))
    memoized_add = memoize(lambda x: x + 1, lambda x, y: True)
    print('memoized_add(1) = ', memoized_add(1))
    print('memoized_add(2) = ', memoized_add(2))
    print('memoized_add(1) = ', memoized_add(1))


test_memoize()

# Generated at 2022-06-14 04:02:52.244839
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(increase)([1, 2, 3]) == [2, 3, 4]



# Generated at 2022-06-14 04:02:55.347581
# Unit test for function memoize
def test_memoize():
    def test_fn(argument):
        return str(argument)

    result = memoize(test_fn)(1)
    print('test_memoize', result)


# Generated at 2022-06-14 04:02:57.192313
# Unit test for function curried_map
def test_curried_map():
    assert(curried_map(lambda x: x * x)([1, 2, 3]) == [1, 4, 9])



# Generated at 2022-06-14 04:03:03.201661
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x % 2 == 0, [0, 1, 2, 3]) == [0, 2]
    assert curried_filter(lambda x: x % 2 == 0)([0, 1, 2, 3]) == [0, 2]
    assert curried_filter(lambda x: x % 2 == 0)([0, 1, 2, 3]) == [0, 2]



# Generated at 2022-06-14 04:03:29.077681
# Unit test for function find
def test_find():
    assert find([1, 2, 3, 4], lambda x: x == 3) == 3
    assert find([1, 2, 3, 4], lambda x: x == 0) is None
    assert find([{'id': 1}, {'id': 2}, {'id': 3}], lambda x: x['id'] == 2) == {'id': 2}
    assert find([{'id': 1}, {'id': 2}, {'id': 3}], lambda x: x['id'] == 0) is None



# Generated at 2022-06-14 04:03:34.859477
# Unit test for function cond
def test_cond():
    # Example
    assert cond([
        (eq(1), identity),
        (eq(2), increase),
    ])(1) == 1
    assert cond([
        (eq(1), identity),
        (eq(2), increase),
    ])(2) == 3
    # Example with data

    class Person:
        def __init__(self, name):
            self.name = name

    def getName(person: Person):
        return person.name

    def isName(name: str, person: Person):
        return person.name == name

    data = [
        Person("Adam"),
        Person("John"),
        Person("Jack"),
        Person("Martin"),
        Person("James"),
        Person("Tylor"),
        Person("Mary"),
    ]


# Generated at 2022-06-14 04:03:39.066013
# Unit test for function find
def test_find():
    collection = [1, 2, 3, 4, 5]
    assert(identity(find(collection, eq(3))) == 3)
    assert(identity(find(collection, eq(100))) is None)



# Generated at 2022-06-14 04:03:42.572209
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(increase, [1, 2, 3]) == [2, 3, 4]
    assert curried_map(increase)([1, 2, 3]) == [2, 3, 4]


# Generated at 2022-06-14 04:03:46.841909
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(increase, [1, 2, 3, 4]) == [2, 3, 4, 5]
    assert curried_map(identity, [1, 2, 3, 4]) == [1, 2, 3, 4]
    assert curried_map(increase, []) == []

# Generated at 2022-06-14 04:03:51.164049
# Unit test for function find
def test_find():
    collection = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert find(collection, lambda x: x % 2 == 0) == 2
    assert find(collection, lambda x: x % 5 == 0) == 5
    assert find(collection, lambda x: x % 13 == 0) is None



# Generated at 2022-06-14 04:03:53.900814
# Unit test for function find
def test_find():
    assert find([1, 2, 3], lambda x: x % 2 == 0) == 2


# Unit tests for function compose

# Generated at 2022-06-14 04:03:55.597037
# Unit test for function curry
def test_curry():
    value = curry(lambda x, y: x + y)(1)(2)
    assert value == 3


# Generated at 2022-06-14 04:04:07.154455
# Unit test for function cond
def test_cond():
    def condition_first(a1, a2, a3):
        return a1 == 1

    def condition_second(a1, a2, a3):
        return a2 == 1

    def execute_first(a1, a2, a3):
        return 'first'

    def execute_second(a1, a2, a3):
        return 'second'

    def execute_third(a1, a2, a3):
        return 'third'

    assert cond([
        (condition_first, execute_first),
        (condition_second, execute_second),
    ])(1, 2, 3) == 'first'
    assert cond([
        (condition_first, execute_first),
        (condition_second, execute_second),
    ])(2, 3, 1) == 'second'

# Generated at 2022-06-14 04:04:12.571669
# Unit test for function curry
def test_curry():
    assert callable(curry(identity))
    assert callable(curry(identity)(1))
    assert identity(1) == curry(identity)(1)
    assert identity(1, 2) == curry(identity, 2)(1, 2)
    assert identity(1, 2, 3) == curry(identity, 3)(1, 2, 3)



# Generated at 2022-06-14 04:04:50.865134
# Unit test for function eq
def test_eq():
    assert eq('1', 1) == False


# Generated at 2022-06-14 04:04:53.061428
# Unit test for function eq
def test_eq():
    assert eq(1, 1)
    assert not eq(1, 2)


# Generated at 2022-06-14 04:04:58.629782
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(increase, [1, 2, 3]) == [2, 3, 4]
    assert curried_map(increase)([1, 2, 3]) == [2, 3, 4]
    assert curried_map(increase, [1, 2, 3, 4, 5])([]) == [2, 3, 4, 5, 6]


# Generated at 2022-06-14 04:05:00.497832
# Unit test for function eq
def test_eq():
    assert eq(1, 1)
    assert not eq(1, 2)



# Generated at 2022-06-14 04:05:12.613121
# Unit test for function curry
def test_curry():
    def add(a, b, c, d, e):
        return a + b + c + d + e

    add_c = curry(add, args_count=4)
    assert add_c(1, 2, 3, 4, 5) == 15
    add_c_1 = add_c(1)
    assert add_c_1(2, 3, 4, 5) == 15
    add_c_2 = add_c(1)(2)
    assert add_c_2(3, 4, 5) == 15
    add_c_3 = add_c(1)(2)(3)
    assert add_c_3(4, 5) == 15
    add_c_4 = add_c(1)(2)(3)(4)
    assert add_c_4(5) == 15
    assert add_c

# Generated at 2022-06-14 04:05:18.906188
# Unit test for function find
def test_find():
    assert find([], lambda x: True) is None, 'find should return None if empty collection provided'
    assert find([1, 2, 1], eq(2)) == 2, 'find should find only first element'
    assert find([1, 2, 1], eq(3)) is None, 'find should return None if can\'t find match'



# Generated at 2022-06-14 04:05:26.555356
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda item: item == 'a')(['a', 'b']) == ['a']
    assert curried_filter(lambda item: item == 'a', ['a', 'b']) == ['a']
    assert curried_filter(lambda item: item == 'a')('aba') == ['a', 'a']
    assert curried_filter(lambda item: item == 'a', 'aba') == ['a', 'a']



# Generated at 2022-06-14 04:05:29.575084
# Unit test for function curried_filter
def test_curried_filter():
    assert([2, 3] == compose(
        [1, 2, 3],
        curried_filter(lambda x: x % 2)
    ))



# Generated at 2022-06-14 04:05:39.792899
# Unit test for function cond
def test_cond():
    def always_true(condition: bool) -> bool:
        return True

    def always_false(condition: bool) -> bool:
        return False

    def always_true_lambda(condition: bool) -> bool:
        return lambda _: True

    def always_false_lambda(condition: bool) -> bool:
        return lambda _: False

    def always_true_reverse(condition: bool) -> bool:
        return not condition

    def always_false_reverse(condition: bool) -> bool:
        return not condition

    def always_true_lambda_reverse(condition: bool) -> bool:
        return lambda x: not x

    def always_false_lambda_reverse(condition: bool) -> bool:
        return lambda x: not x


# Generated at 2022-06-14 04:05:42.181630
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(lambda item: item ** item)([2, 3, 4]) == [4, 27, 256]
    assert curried_map(lambda item: item ** item, [2, 3, 4]) == [4, 27, 256]


# Generated at 2022-06-14 04:06:33.503382
# Unit test for function curried_filter
def test_curried_filter():
    """
    Check function curried_filter.
    """
    assert curried_filter(increase, [1, 2, 3, 4]) == [2, 3, 4, 5]
    assert curried_filter(lambda x: x < 3, [1, 2, 3, 4]) == [1, 2]



# Generated at 2022-06-14 04:06:40.556317
# Unit test for function memoize
def test_memoize():
    def billion_calls(x):
        return x

    zero = billion_calls(0)
    one = billion_calls(1)

    zero_memoized = memoize(billion_calls)(0)
    one_memoized = memoize(billion_calls)(1)

    assert zero == 0
    assert one == 1
    assert zero == zero_memoized
    assert one == one_memoized



# Generated at 2022-06-14 04:06:43.918271
# Unit test for function find
def test_find():
    collection = [('a', 1), ('b', 2), ('c', 3)]
    test = find(collection, lambda item: item[0] == 'a')
    assert(test == ('a', 1))


# Generated at 2022-06-14 04:06:46.934597
# Unit test for function curry
def test_curry():
    def foo(a, b, c):
        return a + b + c
    assert foo(1, 2, 3) == 6

    foo = curry(foo)
    assert foo(1)(2)(3) == 6



# Generated at 2022-06-14 04:06:52.956433
# Unit test for function find
def test_find():
    """
    Unit test for function find.
    """
    lst = [1, 2, 3, 4]

    assert find(lst, lambda x: x == 5) is None
    assert find(lst, lambda x: x == 3) == 3
    assert find(lst, lambda x: x == 4) == 4



# Generated at 2022-06-14 04:06:59.293437
# Unit test for function curried_map
def test_curried_map():
    assert curried_map([1, 2, 3, 4], increase)([1, 2, 3, 4]) == [2, 3, 4, 5]
    assert curried_map([1, 2, 3, 4], identity)([1, 2, 3, 4]) == [1, 2, 3, 4]



# Generated at 2022-06-14 04:07:01.044372
# Unit test for function eq
def test_eq():
    assert eq(1, 1) == True
    assert eq(1, 0) == False



# Generated at 2022-06-14 04:07:09.459334
# Unit test for function memoize
def test_memoize():
    def test(x: int) -> int:
        if x > 10:
            return x + 1
        return x - 1

    test2 = curry(test)
    test3 = memoize(test2)
    if test3(4) != 3 and test3(4) != 3 and test3(11) != 12 and test3(11) != 12:
        print('Unit test failed')
        return
    print('Unit test OK')


test_memoize()


# Generated at 2022-06-14 04:07:12.983010
# Unit test for function find
def test_find():
    assert find([1, 2, 3, 4], eq(3)) == 3
    assert find([1, 2, 3, 4], eq(10)) == None


# Generated at 2022-06-14 04:07:18.259187
# Unit test for function find
def test_find():
    assert find([1, 2, 3, 4, 5], lambda x: x == 4) == 4
    assert find([1, 2, 3, 4, 5], lambda x: x == 6) is None
    assert find([], lambda x: x == 6) is None
