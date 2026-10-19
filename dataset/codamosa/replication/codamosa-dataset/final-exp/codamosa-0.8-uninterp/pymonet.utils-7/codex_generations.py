

# Generated at 2022-06-14 03:58:05.577810
# Unit test for function memoize
def test_memoize():
    def multiply(a, b):
        return a*b

    multiply_memoized = memoize(multiply)

    assert multiply_memoized(2, 3) == 6
    assert multiply_memoized(2, 3) == 6
    assert multiply_memoized(3, 2) == 6
    assert multiply_memoized(3, 2) == 6



# Generated at 2022-06-14 03:58:11.127881
# Unit test for function find
def test_find():
    """
    Test for  find function.
    """
    collection = [
        1,
        2,
        3
    ]
    assert find(collection, lambda value: value == 1) == 1
    assert find(collection, lambda value: value == 4) is None



# Generated at 2022-06-14 03:58:15.574800
# Unit test for function find
def test_find():
    assert find([1, 2, 3], lambda x: x == 3) == 3
    assert find([1, 2, 3], lambda x: x == 4) is None



# Generated at 2022-06-14 03:58:20.047887
# Unit test for function cond
def test_cond():
    def check_negative(value):
        return value < 0

    def check_positive(value):
        return value >= 0

    def check_zero(value):
        return value == 0

    def decrease(value):
        return value - 1

    def increase(value):
        return value + 1

    def identity(value):
        return value

    cond_result = cond([
        (check_negative, decrease),
        (check_positive, increase),
        (check_zero, identity)
    ])

    assert cond_result(-1) == -2
    assert cond_result(0) == 0
    assert cond_result(1) == 2

# Generated at 2022-06-14 03:58:25.003131
# Unit test for function find
def test_find():
    assert find([2], lambda x: x == 2) == 2
    assert find([1, 2, 3], lambda x: x == 2) == 2
    assert find([1, 2, 3], lambda x: x == 4) is None
    assert find([], lambda x: x == 4) is None

test_find()



# Generated at 2022-06-14 03:58:31.543607
# Unit test for function memoize
def test_memoize():
    def add(x):
        return x + 1

    memoized_add = memoize(add)

    assert memoized_add(1) == memoized_add(1)



# Generated at 2022-06-14 03:58:39.609958
# Unit test for function find
def test_find():
    test_data = [
        {'value': 1, 'key': 2, 'expected': None},
        {'value': [1, 2, 3], 'key': 2, 'expected': 2}
    ]

    for dataset in test_data:
        result = find(dataset['value'], eq(dataset['key']))
        assert dataset['expected'] == result



# Generated at 2022-06-14 03:58:41.016481
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(lambda x: x + 1)([1]) == [2]



# Generated at 2022-06-14 03:58:48.240710
# Unit test for function curry
def test_curry():
    @curry
    def test_func(a, b, c, d=1, e=2, f=3):
        return a + b + c + d + e + f

    assert test_func(1, 2, 3) == test_func(1, 2)(3)
    assert test_func(1, 2, 3) == test_func(1)(2, 3)
    assert test_func(1, 2, 3) == test_func(1)(2)(3)
    assert test_func(1, 2, 3, 4, 5, 6) == test_func(1, 2, 3)(4, 5, 6)
    assert test_func(1, 2, 3, 4, 5, 6) == test_func(1, 2, 3)(4)(5, 6)

# Generated at 2022-06-14 03:58:49.733132
# Unit test for function eq
def test_eq():
    assert eq(1, 1)
    assert not eq(1, 2)

# Generated at 2022-06-14 03:58:58.338987
# Unit test for function curry
def test_curry():
    def curried_add_5(x):
        return x + 5

    add_5 = curry(curried_add_5)
    add_8 = curry(lambda x, y: x + y, 2)
    assert add_5(10) == 15
    assert add_8(10, -2) == 8
    assert add_8(10)(-2) == 8



# Generated at 2022-06-14 03:59:05.194236
# Unit test for function memoize
def test_memoize():
    @memoize
    def factorial(n):
        if n < 2:
            return 1
        return n * factorial(n-1)

    assert factorial(6) == 720
    assert factorial.__closure__[0].cell_contents == [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24),
        (5, 120),
        (6, 720)
    ]

# Generated at 2022-06-14 03:59:10.390610
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(lambda x: x + 1)([1, 2, 3]) == [2, 3, 4]
    assert curried_map(lambda x: x + 2)([1, 2, 3]) == [3, 4, 5]



# Generated at 2022-06-14 03:59:12.616032
# Unit test for function eq
def test_eq():
    assert eq(1, 1)
    assert not eq(1, 2)


# Generated at 2022-06-14 03:59:14.648333
# Unit test for function eq
def test_eq():
    eq1 = eq(2, 1)
    assert not eq1

    eq2 = eq(2, 2)
    assert eq2



# Generated at 2022-06-14 03:59:26.583421
# Unit test for function cond
def test_cond():
    """
    Unit test for function cond
    """
    # COND
    def is_even(number) -> bool:
        """
        Function, witch check if argument number is even

        :param number: argument to check
        :type number: Int
        :returns: True if number is even, else False
        :rtype: Boolean
        """
        return number % 2 == 0

    def is_odd(number) -> bool:
        """
        Function, witch check if argument number is odd

        :param number: argument to check
        :type number: Int
        :returns: True if number is odd, else False
        :rtype: Boolean
        """
        return number % 2 == 1


# Generated at 2022-06-14 03:59:29.663491
# Unit test for function curried_filter
def test_curried_filter():
    list1 = [1, 2, 3, 4, 5, 6]
    list2 = [4, 5, 6, 7, 8, 9]
    assert curried_filter(lambda x: x > 5, list1) == filter(lambda x: x > 5, list1)
    assert curried_filter(lambda x: x > 5, list2) == filter(lambda x: x > 5, list2)


# Generated at 2022-06-14 03:59:38.761155
# Unit test for function cond
def test_cond():
    is_string = lambda x: isinstance(x, str)
    is_number = lambda x: isinstance(x, (int, float))
    is_list = lambda x: isinstance(x, list)
    f1 = lambda value: value + ' test'
    f2 = lambda value: value + 2
    f3 = lambda value: [item for item in value]

    assert cond([
        (is_string, f1),
        (is_number, f2),
        (is_list, f3),
    ])('test') == 'test test'
    assert cond([
        (is_string, f1),
        (is_number, f2),
        (is_list, f3),
    ])(3) == 5

# Generated at 2022-06-14 03:59:42.711140
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(lambda x: x + 1)([1, 2, 3]) == [2, 3, 4]
    assert curried_map(lambda x: x + 1, [1, 2, 3]) == [2, 3, 4]



# Generated at 2022-06-14 03:59:45.693820
# Unit test for function memoize
def test_memoize():
    def memoized_fn(value):
        return value

    memoized_fn = memoize(memoized_fn)
    for value in [1, 1, 1, 2, 2, 2, 1, 2, 3, 3, 4, 1, 1]:
        assert memoized_fn(value) == value

    assert len(memoized_fn.__closure__[0].cell_contents) == 4



# Generated at 2022-06-14 03:59:53.879410
# Unit test for function memoize
def test_memoize():
    count = 0

    def counter(value):
        nonlocal count
        count += 1
        return value

    memoized_counter = memoize(counter)

    assert memoized_counter('1') == '1'
    assert count == 1
    assert memoized_counter('1') == '1'
    assert count == 1
    assert memoized_counter('2') == '2'
    assert count == 2




# Generated at 2022-06-14 04:00:05.258995
# Unit test for function memoize
def test_memoize():

    @memoize
    def get_cached_item(item):
        return item

    assert get_cached_item(1) == 1
    assert get_cached_item(2) == 2
    assert get_cached_item(1) == 1

    cache_list = [1, 2, 3]

    @memoize
    def get_cached_list(arg):
        return cache_list

    assert get_cached_list(1) == cache_list
    assert get_cached_list(2) == cache_list
    assert get_cached_list(1) == cache_list


test_memoize()


# Generated at 2022-06-14 04:00:16.654284
# Unit test for function curry
def test_curry():
    def func(a, b, c, d):
        return a + b + c + d

    curried_func = curry(func)
    curried_func1 = curry(func, 4)
    curried_func2 = curry(func, 1)
    curried_func3 = curry(func, 2)

    assert func(1, 2, 3, 4) == 10
    assert curried_func(1, 2, 3, 4) == 10
    assert curried_func1(1, 2, 3, 4) == 10
    assert curried_func2(1)(2, 3, 4) == 10
    assert curried_func3(1, 2)(3, 4) == 10
    assert curried_func3(1)(2)(3, 4) == 10

# Generated at 2022-06-14 04:00:24.661535
# Unit test for function cond
def test_cond():
    eq_one = lambda number, value: number == value
    eq_two = lambda number, value: number == value + 1
    eq_three = lambda number, value: number == value + 2

    def print_one():
        print('one')

    def print_two():
        print('two')

    def print_three():
        print('three')

    cond_function = cond([
        (eq_one, print_one),
        (eq_two, print_two),
        (eq_three, print_three),
    ])

    cond_function(1)
    cond_function(2)
    cond_function(3)



# Generated at 2022-06-14 04:00:28.434427
# Unit test for function curry
def test_curry():
    fn = lambda x, y: x + y
    curried_add = curry(fn)

    r = curried_add(2)(2)
    assert r == 4

# Generated at 2022-06-14 04:00:31.956948
# Unit test for function eq
def test_eq():
    """
    Unit test for function eq

    :returns: True if test passed and False if test failed
    :rtype: Boolean
    """
    return eq(1)(1) == True



# Generated at 2022-06-14 04:00:41.641562
# Unit test for function memoize
def test_memoize():
    counter = [0]

    @memoize
    def test_fn(argument):
        counter[0] += 1
        return counter[0]

    def test_key(argument, cached_argument):
        return argument == cached_argument

    assert test_fn(1) == 1
    assert test_fn(1) == 1
    assert test_fn(2) == 2
    assert test_fn(2) == 2
    assert test_fn(1) == 1

    assert test_fn(1, test_key) == 1
    assert test_fn(1, test_key) == 1
    assert test_fn(2, test_key) == 2
    assert test_fn(2, test_key) == 2
    assert test_fn(1, test_key) == 1



# Generated at 2022-06-14 04:00:42.642844
# Unit test for function eq
def test_eq():
    assert eq(1, 1)



# Generated at 2022-06-14 04:00:47.209568
# Unit test for function eq
def test_eq():
    eq_ = eq(1, 2)
    eq_1 = eq(1, 1)
    eq_2 = eq(1)(1)
    eq_3 = eq(1)
    eq_4 = eq(1, 1, 2)

    assert eq_ == False
    assert eq_1 == True
    assert eq_2 == True
    assert eq_3(1) == True
    assert eq_4 == False



# Generated at 2022-06-14 04:00:55.337519
# Unit test for function cond
def test_cond():
    assert cond([
        (lambda a: a == 0, lambda a: '0'),
        (lambda a: a % 2 == 0, lambda a: 'even'),
        (lambda a: a % 2 != 0, lambda a: 'odd')
    ])(10) == 'even'
    assert cond([
        (lambda a: a == 0, lambda a: '0'),
        (lambda a: a % 2 == 0, lambda a: 'even'),
        (lambda a: a % 2 != 0, lambda a: 'odd')
    ])(11) == 'odd'

# Generated at 2022-06-14 04:01:09.411997
# Unit test for function memoize
def test_memoize():
    def f(n):
        return n * n

    memoized_f = memoize(f)
    assert memoized_f(0) == 0
    assert memoized_f(1) == 1
    assert memoized_f(2) == 4
    assert memoized_f(3) == 9
    assert memoized_f(0) == 0
    assert memoized_f(1) == 1
    assert memoized_f(2) == 4
    assert memoized_f(3) == 9
    assert len(memoized_f.__closure__[0].cell_contents) == 4
    memoized_f = memoize(f)
    assert memoized_f(0) == 0
    assert memoized_f(1) == 1
    assert memoized_f(2) == 4
    assert memoized_f

# Generated at 2022-06-14 04:01:22.543742
# Unit test for function memoize
def test_memoize():
    import random
    import time
    print("Testing memoize function")
    print("========================")
    print("The function should not increase function execution time.\n" +
          "They should take more or less the same time", "\n")
    print("----------------------")

    rand = random.randint
    rand_list = lambda: [rand(1, 9) for _ in range(rand(1, 9))]
    unit_start_time = time.clock()
    for i in range(100000):
        random_fn1 = rand_list()
        random_fn2 = rand_list()
    unit_end_time = time.clock()
    un_optimized_time = unit_end_time - unit_start_time
    print("Un-optimized time", un_optimized_time, "\n")
    optimized_start

# Generated at 2022-06-14 04:01:29.187630
# Unit test for function cond
def test_cond():
    """
    Function to check work of function 'cond'

    :returns: None
    :rtype: None
    """
    f = cond([(lambda x: x == 'a', lambda x: x*2),
              (lambda x: x == 'b', lambda x: x*3),
              (lambda x: x == 'c', lambda x: x*4)])
    assert f('a') == 'aa'
    assert f('b') == 'bbb'
    assert f('c') == 'cccc'



# Generated at 2022-06-14 04:01:32.449914
# Unit test for function curried_filter
def test_curried_filter():
    """
    Function testing curried_filter function
    """
    curried_filter_func = curried_filter(lambda x: x < 5)
    assert curried_filter_func([1, 100, 20]) == [1, 20], "curried_filter should return elements lower then 5"



# Generated at 2022-06-14 04:01:34.792682
# Unit test for function curried_map
def test_curried_map():
    assert list(map(lambda x: x ** 2, range(5))) \
           == curried_map(lambda x: x ** 2)(range(5))


# Generated at 2022-06-14 04:01:37.463420
# Unit test for function find
def test_find():
    """
    Test function find.
    """
    result = find([1, 2, 3], eq(3))
    assert result == 3
    assert find([1, 2, 3], eq(4)) is None

# Generated at 2022-06-14 04:01:41.835139
# Unit test for function curried_filter
def test_curried_filter():
    curried_filter_function = curried_filter(lambda x: x > 10)

    assert curried_filter_function([1, 2, 5, 12, 15, 24, 35]) == [12, 15, 24, 35]
    assert curried_filter_function([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == []
    assert curried_filter_function([12, 13, 14, 15]) == [12, 13, 14, 15]


# Generated at 2022-06-14 04:01:46.618073
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(lambda a: a + 1, [6, 8]) == [7, 9]
    assert curried_map(lambda a: a + 1, [1, 2, 3, 4]) == [2, 3, 4, 5]

test_curried_map()


# Generated at 2022-06-14 04:01:51.046290
# Unit test for function curried_filter
def test_curried_filter():
    """
    Test for curried_filter
    """
    numbers = [1, 2, 3, 4, 5]
    assert curried_filter(lambda x: x % 2 == 0, numbers) == [2, 4]



# Generated at 2022-06-14 04:01:55.819658
# Unit test for function cond
def test_cond():
    """
    Run test cases for function cond
    """
    def square(x):
        return x*x

    def even(x):
        return x%2 == 0

    double_then_square = cond([
        (even, square),
        (identity, lambda x: x*2),
    ])

    assert(double_then_square(2) == 4)
    assert(double_then_square(1) == 2)

# Generated at 2022-06-14 04:02:06.676297
# Unit test for function memoize
def test_memoize():
    def get_current_time():
        return time()

    assert(memoize(get_current_time)() != memoize(get_current_time)())
    assert(memoize(get_current_time, eq)(2) != memoize(get_current_time, eq)(1))



# Generated at 2022-06-14 04:02:11.603881
# Unit test for function curried_map
def test_curried_map():
    collection = [1, 2, 3]

    assert curried_map(increase, collection) == [2, 3, 4]
    assert curried_map(increase)(collection) == [2, 3, 4]
    assert curried_map(increase, collection) == [2, 3, 4]


# Generated at 2022-06-14 04:02:13.458564
# Unit test for function eq
def test_eq():
    assert eq(1, 1)
    assert not eq(1, '1')



# Generated at 2022-06-14 04:02:17.237824
# Unit test for function eq
def test_eq():
    assert eq(1, 2) is False
    assert eq(1, 1) is True
    assert eq(1)(2) is False
    assert eq(1)(1) is True



# Generated at 2022-06-14 04:02:24.228847
# Unit test for function find
def test_find():
    assert find(
        collection=[],
        key=eq(value=True)
    ) is None
    assert find(
        collection=[1, 2],
        key=eq(value=True)
    ) is None
    assert find(
        collection=['a', 'b'],
        key=eq(value='a')
    ) == 'a'
    assert find(
        collection=[('a', 'b'), ('c', 'd')],
        key=compose(eq(value='b'), lambda item: item[1])
    ) == ('a', 'b')


# Generated at 2022-06-14 04:02:30.058555
# Unit test for function eq
def test_eq():
    assert not eq(1, 2)
    assert eq(2, 2)
    assert not eq(2, 3)

    eq2 = curry(eq, 2)
    assert not eq2(1, 2, 3)
    assert eq2(1, 2)
    assert eq2(2, 4)
    assert eq2(10)


# Generated at 2022-06-14 04:02:31.580985
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(eq(2), [1, 2, 3]) == [2]



# Generated at 2022-06-14 04:02:42.739097
# Unit test for function curry
def test_curry():
    """
    Test for function curry.
    """
    assert curry(lambda x, y: x + y)(1)(2) == 3
    assert curry(lambda x, y, z: x + y + z)(1)(2)(3) == 6

    assert curry(lambda x, y=1, z=2: x + y + z)(1)(1)(1) == 3
    assert curry(lambda x, y=1, z=2: x + y + z)(1)(1) == 4
    assert curry(lambda x, y=1, z=2: x + y + z)(1) == 4
    assert curry(lambda x, y=1, z=2: x + y + z)() == 3



# Generated at 2022-06-14 04:02:45.630118
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x > 3, [
        1, 2, 3, 4]) == [4]
    assert curried_filter(lambda x: x % 2 == 0, [1, 2, 3, 4]) == [2, 4]

# Generated at 2022-06-14 04:02:51.637057
# Unit test for function curried_filter
def test_curried_filter():
    """
    Perform unit test for curried_filter

    :param:
    :type:
    :returns:
    :rtype:
    """
    lst_odd = [1, 3, 5, 7, 9]
    odd = lambda value: value % 2 != 0
    is_odd = curried_filter(odd)

    assert is_odd(lst_odd) == [1, 3, 5, 7, 9]



# Generated at 2022-06-14 04:03:09.556415
# Unit test for function cond
def test_cond():
    # if
    assert cond([
        [lambda x, y: x == y, lambda x, y: x * 2],
        [lambda x, y: x != y, lambda x, y: 1],
    ])(2, 2) == 4

    # else
    assert cond([
        [lambda x, y: x >= y, lambda x, y: x * 2],
        [lambda x, y: x < y, lambda x, y: 1],
    ])(2, 3) == 1



# Generated at 2022-06-14 04:03:10.655627
# Unit test for function eq
def test_eq():
    assert eq(1, 1) == True
    assert eq(1, 0) == False



# Generated at 2022-06-14 04:03:15.073684
# Unit test for function cond
def test_cond():
    assert cond([
        (lambda x: x == 3, lambda x: x ** 2),
        (lambda x: x == 2, lambda x: x ** 3),
        (lambda x: x == 1, lambda x: x ** 4)
    ])(2) == 8



# Generated at 2022-06-14 04:03:19.235390
# Unit test for function curried_filter
def test_curried_filter():
    myFilter = curried_filter(lambda x: x % 2 == 0)
    myFilter2 = curried_filter(lambda x: x % 2 != 0)
    assert myFilter([1, 2, 3, 4]) == [2, 4]
    assert myFilter2([1, 2, 3, 4]) == [1, 3]



# Generated at 2022-06-14 04:03:23.536313
# Unit test for function memoize
def test_memoize():
    def add(x: int) -> int:
        return x + 1

    assert memoize(add)(1) == 2


if __name__ == '__main__':
    test_memoize()

# Generated at 2022-06-14 04:03:28.346000
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x > 1, [0, 1, 2, 3]) == [2, 3]
    assert curried_filter(lambda x: x > 1)([0, 1, 2, 3]) == [2, 3]



# Generated at 2022-06-14 04:03:32.953265
# Unit test for function find
def test_find():
    def should_return_first_value_which_equals():
        assert find([1, 2, 3, 2], key=eq(2)) == 2

    def should_return_none_if_not_value_matched():
        assert find([1, 2, 3], key=eq(4)) is None

    should_return_first_value_which_equals()
    should_return_none_if_not_value_matched()



# Generated at 2022-06-14 04:03:37.679306
# Unit test for function find
def test_find():
    assert find([1, 2, 3, 4], lambda x: x % 2 == 0) == 2
    assert find([1, 2, 3, 4], lambda x: x > 10) is None
    assert find(['a', 'b'], lambda x: ord(x) == 97) == 'a'



# Generated at 2022-06-14 04:03:40.686173
# Unit test for function find
def test_find():
    collection = [1, 2, 3, 6]
    assert find(collection, eq(1)) == 1
    assert find(collection, eq(7)) is None



# Generated at 2022-06-14 04:03:43.981545
# Unit test for function find
def test_find():
    print(find([1, 2, 3, 4], lambda x: x % 2 == 1))
    print(find([1, 2, 3, 4], lambda x: x > 4))



# Generated at 2022-06-14 04:04:02.589197
# Unit test for function curry
def test_curry():
    assert curry(lambda a, b, c: [a, b, c])(1)(2)(3) == [1, 2, 3]
    assert curry(lambda a, b, c: [a, b, c])(1, 2)(3) == [1, 2, 3]
    assert curry(lambda a, b, c: [a, b, c])(1)(2, 3) == [1, 2, 3]
    assert curry(lambda a, b, c: [a, b, c])(1, 2, 3) == [1, 2, 3]



# Generated at 2022-06-14 04:04:05.341522
# Unit test for function eq
def test_eq():
    assert eq(2, 2) is True
    assert eq(2, '2') is False
    assert eq(2)(2) is True


# Generated at 2022-06-14 04:04:13.617995
# Unit test for function eq
def test_eq():
    assert(True == eq('1')('1'))
    assert(False == eq('1')('2'))
    assert(True == eq('1')('1',))
    assert(False == eq('1')('2',))
    assert(True == eq(1)(1))
    assert(False == eq(1)(2))
    assert(True == eq(1)(1,))
    assert(False == eq(1)(2,))



# Generated at 2022-06-14 04:04:15.842925
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(eq(2))([1, 2, 3]) == [2]



# Generated at 2022-06-14 04:04:22.281129
# Unit test for function cond
def test_cond():
    def cond_function(argument):
        return cond([
            (lambda a: a == 1, lambda _: 'First function appropriate'),
            (lambda a: a == 2, lambda _: 'Second function appropriate'),
        ])(argument)

    assert cond_function(1) == 'First function appropriate', \
        'Error function cond. First case.'
    assert cond_function(2) == 'Second function appropriate', \
        'Error function cond. Second case.'
    assert cond_function(3) is None, \
        'Error function cond. Third case.'



# Generated at 2022-06-14 04:04:30.463383
# Unit test for function cond
def test_cond():
    condition_list = [
        (lambda i: i % 2 == 0, lambda i: i * 2),
        (lambda i: i % 2 != 0, lambda i: i * 3),
    ]
    cond_function = cond(condition_list)
    assert cond_function(1) == 3
    assert cond_function(2) == 4
    assert cond_function(3) == 9
    assert cond_function(4) == 8



# Generated at 2022-06-14 04:04:34.311157
# Unit test for function eq
def test_eq():
    """
    Test function eq.
    """
    assert eq(1, 1)
    assert not eq(1, 2)
    assert eq(3, 3)
    assert not eq(3, 4)



# Generated at 2022-06-14 04:04:37.856338
# Unit test for function cond
def test_cond():
    multiply_7 = lambda x: cond([
        (lambda value: value == 0, lambda _: 0),
        (lambda _: True, lambda value: 7 + multiply_7(value - 1))
    ])
    assert multiply_7(2) == 14

# Generated at 2022-06-14 04:04:45.762967
# Unit test for function memoize
def test_memoize():
    # Create function
    concat_list = memoize(lambda xs: reduce(lambda acc, x: acc + x, xs, []))

    # Invoke function
    actual = concat_list(['1', '2', '3']), concat_list(['1', '2', '3'])

    # Assert returned value
    assert actual == (['1', '2', '3'], ['1', '2', '3'])



# Generated at 2022-06-14 04:04:55.007772
# Unit test for function cond
def test_cond():
    def is_odd(value):
        return value % 2 == 1

    def is_even(value):
        return not is_odd(value)

    def has_four(value):
        return value == 4

    double = lambda value: value * 2
    increase = lambda value: value + 1
    to_zero = lambda value: 0
    always_true = lambda value: True

    fn = cond([
        (is_odd, double),
        (has_four, to_zero),
        (is_even, increase),
        (always_true, identity)
    ])

    assert fn(0) == 1
    assert fn(1) == 2
    assert fn(4) == 0
    assert fn(5) == 10



# Generated at 2022-06-14 04:05:10.680100
# Unit test for function eq
def test_eq():
    assert identity(1) == 1
    assert identity(None) is None
    assert identity(True) is True
    assert eq(3, 3) is True
    assert eq(3, 4) is False
    assert compose(3, eq(3)) is True
    assert pipe(3, eq(3)) is True
    assert compose(3, eq(4)) is False



# Generated at 2022-06-14 04:05:13.605679
# Unit test for function memoize
def test_memoize():
    def f(x):
        print("Invoked f()")
        return x * x

    g = memoize(f)

    assert g(3) == 9
    assert g(3) == 9



# Generated at 2022-06-14 04:05:16.061814
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(identity, [1, 2, 3]) == [1, 2, 3]



# Generated at 2022-06-14 04:05:23.854063
# Unit test for function eq
def test_eq():
    assert eq(1, 1) == True
    assert eq(1, 2) == False
    assert eq(2, 1) == False

    eq_two = curry(eq, 2)

    assert eq_two(1)(1) == True
    assert eq_two(2)(2) == True
    assert eq_two(1)(2) == False
    assert eq_two(2)(1) == False


# Generated at 2022-06-14 04:05:34.216697
# Unit test for function cond
def test_cond():
    """
    unit test for function cond.
    """
    # define array of conditions and functions
    condition_list = [
        (lambda x: x > 0, lambda x: True),
        (lambda x: x == 0, lambda x: False),
        (lambda x: True, lambda x: None),
    ]
    # get function wich decide what function should be invoked
    result_function = cond(condition_list)
    # invoke function with argument -1
    assert result_function(-1) is True
    # invoke function with argument 0
    assert result_function(0) is False
    # invoke function with argument 1
    assert result_function(1) is True

    # define array of conditions and functions

# Generated at 2022-06-14 04:05:42.172013
# Unit test for function curry
def test_curry():
    def add(x, y, z):
        return x + y + z

    add_curry = curry(add, 3)

    assert add_curry(1, 2, 3) == add(1, 2, 3)
    assert add_curry(1, 2)(3) == add(1, 2, 3)
    assert add_curry(1)(2, 3) == add(1, 2, 3)
    assert add_curry(1)(2)(3) == add(1, 2, 3)
    assert add_curry()(1)(2)(3) == add(1, 2, 3)
    assert add_curry()(1)(2, 3) == add(1, 2, 3)
    assert add_curry()(1, 2)(3) == add(1, 2, 3)
    assert add

# Generated at 2022-06-14 04:05:52.499916
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(increase, [0, 1, 2]) == [1, 2, 3]
    assert curried_filter(increase, [0, 1, 2, None]) == [1, 2, 3]
    assert curried_filter(increase, [0, 1, 2, None, '']) == [1, 2, 3]
    assert curried_filter(increase, [0, 1, 2, None, '']) == [1, 2, 3]
    assert curried_filter(increase, [0, 1, 2, None, '']) == [1, 2, 3]



# Generated at 2022-06-14 04:05:57.446743
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x % 2 == 0, []) == []
    assert curried_filter(lambda x: x % 2 == 0, [1]) == []
    assert curried_filter(lambda x: x % 2 == 0, [0, 1]) == [0]
    assert curried_filter(lambda x: x % 2 == 0, [0, 1, 2]) == [0, 2]



# Generated at 2022-06-14 04:06:03.662906
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(increase, [1, 2, 3, 4, 5]) == [2, 3, 4, 5, 6]
    curried_map_increase = curried_map(increase)
    assert curried_map_increase([1, 2, 3, 4, 5]) == [2, 3, 4, 5, 6]
    assert curried_map_increase([7, 8, 9, 10]) == [8, 9, 10, 11]


# Generated at 2022-06-14 04:06:13.821449
# Unit test for function curried_filter
def test_curried_filter():
    list1 = [1, 2, 3, 4, 5]
    list2 = ['a', 'b', 'c', 'd']
    even = lambda x: x % 2 == 0
    odd = lambda x: x % 2 == 1
    less_than_5 = lambda x: x < 5

    test1 = curried_filter(even)(list1)
    test2 = curried_filter(odd)(list1)
    test3 = curried_filter(odd)(list2)
    test4 = curried_filter(less_than_5)(list1)

    assert test1 == [2, 4]
    assert test2 == [1, 3, 5]
    assert test3 == ['a', 'c']
    assert test4 == [1, 2, 3, 4]



# Generated at 2022-06-14 04:06:31.376022
# Unit test for function find
def test_find():
    assert find([1, 2, 3], lambda x: x % 2 == 1) == 1



# Generated at 2022-06-14 04:06:33.444481
# Unit test for function eq
def test_eq():
    assert eq(1, 1) == True
    assert eq(1, 2) == False



# Generated at 2022-06-14 04:06:40.060363
# Unit test for function eq
def test_eq():
    assert eq('')('') == True
    assert eq(0)(0) == True
    assert eq(1)(1) == True
    assert eq(0)('0') == False
    assert eq(1)('1') == False
    assert eq('')('1') == False
    assert eq(0)(1) == False
    assert eq('')('0') == False



# Generated at 2022-06-14 04:06:43.232308
# Unit test for function memoize
def test_memoize():
    def sum(x, y):
        return x + y
    sum = memoize(sum)
    assert sum(1, 2) == 3
    assert sum(1, 2) == 3
    assert sum(1, 2) == 3
    assert sum(1, 2) == 3

# Generated at 2022-06-14 04:06:55.084804
# Unit test for function cond
def test_cond():
    def is_odd(x: int) -> bool:
        return x % 2 != 0

    def is_even(x: int) -> bool:
        return x % 2 == 0

    def execute_odd(x: int) -> int:
        return increase(increase(x))

    def execute_even(x: int) -> int:
        return increase(x)

    odd_even_checker = cond(
        [(is_odd, execute_odd), (is_even, execute_even)]
    )

    assert 2 == odd_even_checker(1)
    assert 3 == odd_even_checker(2)
    assert 4 == odd_even_checker(3)



# Generated at 2022-06-14 04:07:04.989505
# Unit test for function cond
def test_cond():
    def is_odd(value: int) -> bool:
        return value % 2 == 1

    def is_even(value: int) -> bool:
        return value % 2 == 0

    def is_zero(value: int) -> bool:
        return value == 0

    print(
        "First call:\n"
        f"cond([(is_odd, increase), (is_even, identity)])(5) = {cond([(is_odd, increase), (is_even, identity)])(5)}\n"
    )

    print(
        "Cache:\n"
        f"cond([(is_odd, increase), (is_even, identity)])(5) = {cond([(is_odd, increase), (is_even, identity)])(5)}\n"
    )


# Generated at 2022-06-14 04:07:09.115355
# Unit test for function eq
def test_eq():
    assert eq(1, 1) == True
    assert eq(1, 2) == False
    assert eq(1)(1) == True
    assert eq(1)(2) == False



# Generated at 2022-06-14 04:07:13.690188
# Unit test for function find
def test_find():
    collection = [3, 6, 8, 10]
    key = eq(3)
    assert find(collection, key) == 3

    key = eq(1)
    assert find(collection, key) is None



# Generated at 2022-06-14 04:07:16.578443
# Unit test for function eq
def test_eq():
    assert eq(1, 1) == True
    assert eq(1, 2) == False


# Generated at 2022-06-14 04:07:18.707143
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda a: a % 2)([1, 2, 3]) == [1, 3]


# Generated at 2022-06-14 04:07:48.197038
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x < 10)([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert curried_filter(lambda x: x < 10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert curried_filter(lambda x: x < 10)([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
   

# Generated at 2022-06-14 04:07:53.625450
# Unit test for function curried_filter
def test_curried_filter():
    """
    This is unit test for function curried_filter
    """
    collection = [1, 2, 4, 5, 6, 4, 2]
    assert curried_filter(lambda x: x % 2 == 0, collection) == [2, 4, 6, 4, 2]



# Generated at 2022-06-14 04:07:59.156758
# Unit test for function curried_filter
def test_curried_filter():
    odd = (lambda n: n % 2)
    [x] = curried_filter(odd, [1, 2, 3, 4])
    assert x == 1
    [x, _] = curried_filter(odd, [1, 2, 3, 4])
    assert x == 1
    assert curried_filter(odd)([1, 2, 3, 4]) == [1, 3]

