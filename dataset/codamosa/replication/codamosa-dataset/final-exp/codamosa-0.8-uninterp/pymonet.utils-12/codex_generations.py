

# Generated at 2022-06-14 03:57:58.857609
# Unit test for function curried_map
def test_curried_map():
    curried_increase = curried_map(increase)
    list1 = curried_increase([1, 2, 3, 4])
    assert list1 == [2, 3, 4, 5]



# Generated at 2022-06-14 03:58:06.070118
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda value: value % 2 == 0, range(10)) == [0, 2, 4, 6, 8]
    assert curried_filter(lambda value: value % 2 == 0)(range(10)) == [0, 2, 4, 6, 8]
    assert curried_filter(lambda value: value % 2 == 0, [1, 2, 3, 4]) == [2, 4]
    assert curried_filter(lambda value: value % 2 == 0)([1, 2, 3, 4]) == [2, 4]



# Generated at 2022-06-14 03:58:11.172196
# Unit test for function curried_map
def test_curried_map():
    mapper_inc = curried_map(increase)
    assert mapper_inc([1, 2, 3]) == [2, 3, 4]
    assert mapper_inc(range(1, 11)) == list(range(2, 12))



# Generated at 2022-06-14 03:58:17.447959
# Unit test for function memoize
def test_memoize():
    assert memoize(lambda x: x * x)(2) == 4
    assert memoize(lambda x: x * x)(2) == 4



# Generated at 2022-06-14 03:58:30.901928
# Unit test for function cond
def test_cond():
    """
    Assert function cond
    docstring should be
    Function for return function depended on first function argument
    cond get list of two-item tuples,
    first is condition_function, second is execute_function.
    Returns this execute_function witch first condition_function return truly value.
    :return:
    """
    is_even = lambda value: value % 2 == 0

    assert is_even(2)
    assert not is_even(3)

    is_negative = lambda value: value < 0

    assert is_negative(-2)
    assert not is_negative(3)

    def add_3(value: int) -> int:
        return value + 3

    add_cond = cond([
        (is_even, add_3),
        (is_negative, lambda _: 0),
    ])

    assert add_cond

# Generated at 2022-06-14 03:58:36.858288
# Unit test for function find
def test_find():
    collection = [1, 2, 3, 4, 5]
    assert find(collection, lambda item: item == 3) == 3



# Generated at 2022-06-14 03:58:45.331364
# Unit test for function cond
def test_cond():
    def func_1(current: int, step: int) -> bool:
        return current + step > 20

    def func_2(current: int, step: int) -> bool:
        return current + step == 20

    def func_3(current: int, step: int) -> bool:
        return current + step < 20

    def func_4(current: int, step: int) -> int:
        return current + step

    def func_5(current: int, step: int) -> int:
        return current + step

    def func_6(current: int, step: int) -> int:
        return current + step

    condition_list = [
        (func_1, func_4),
        (func_2, func_5),
        (func_3, func_6)
    ]


# Generated at 2022-06-14 03:58:49.054721
# Unit test for function memoize
def test_memoize():
    def fib(n):
        if n == 0: return 0
        elif n == 1: return 1
        else: return fib(n - 1) + fib(n - 2)

    fib = memoize(fib)
    print(fib(20))
    print(fib(10))
    print(fib(10))
    print(fib(20))
    print(fib(15))
    print(fib(15))



# Generated at 2022-06-14 03:59:00.762602
# Unit test for function curried_map
def test_curried_map():
    """
    Test function curried_map.
    :return: None
    """
    assert curried_map(lambda x: x ** 2, [1, 2, 3]) == [1, 4, 9]
    assert curried_map(lambda x: x ** 2, 1, 2, 3, 4) == [1, 4, 9, 16]
    assert curried_map(lambda x: x ** 2, [1, 2, 3, 4]) == [1, 4, 9, 16]
    assert curried_map(lambda x: x ** 2, 1, 2, 3, 4) == [1, 4, 9, 16]
    assert curried_map(lambda x: x + 1, 1) == [2]
    assert curried_map(lambda x: x + 1, [1]) == [2]


# Generated at 2022-06-14 03:59:06.423131
# Unit test for function eq
def test_eq():
    # Test short version of curry
    eq1 = curry(eq)

    # Test correct working
    assert eq(1, 1), "Should return True"
    assert eq1(1)(1), "Should return True"
    assert not eq(1, 2), "Should return False"
    assert not eq1(1)(2), "Should return False"



# Generated at 2022-06-14 03:59:13.714429
# Unit test for function curried_filter
def test_curried_filter():
    assert [1, 4] == curried_filter(lambda x: x % 2 == 0, [0, 1, 2, 3, 4, 5])
    assert [1, 4] == curried_filter(lambda x: x % 2 == 0)([0, 1, 2, 3, 4, 5])


# Generated at 2022-06-14 03:59:19.510320
# Unit test for function find
def test_find():
    xs = [1, 2, 3, 4, 5, 6]
    assert find(xs, lambda x: x > 0) == 1

    xs = []
    assert find(xs, lambda x: x > 0) is None

    assert find(xs, lambda x: False) is None


# Generated at 2022-06-14 03:59:22.565240
# Unit test for function find
def test_find():
    assert find([1, 2, 3], eq(2)) == 2
    assert find([1, 2, 3], eq(4)) is None

# Generated at 2022-06-14 03:59:31.483880
# Unit test for function curry
def test_curry():
    assert callable(curry(lambda x: x))
    assert curry(lambda x: x)(1) == 1
    assert curry(lambda x, y: x + y)(2)(1) == 3
    assert curry(lambda x, y, z: x + y + z)(2)(1)(3) == 6
    assert curry(lambda x, y, z: x + y + z)(2)(1)(3) == 6
    assert curry(lambda x, y, z, o: x + y + z + o)(2)(1)(3)(4) == 10
    assert curry(lambda x, y, z, o, p: x + y + z + o + p)(2)(1)(3)(4)(5) == 15

# Generated at 2022-06-14 03:59:40.310809
# Unit test for function memoize
def test_memoize():
    """
    Function for test memoize function

    :returns: dict
    :rtype: dict
    """

    def add(a):
        return a + 1

    result = memoize(add)
    assert result(1) == 2
    assert result(1) == 2

    def raise_error(error, message):
        raise error(message)

    result = memoize(raise_error, curry(eq, 2))
    result(AssertionError, "First error")
    result(AssertionError, "Second error")
    result(AssertionError, "Third error")



# Generated at 2022-06-14 03:59:44.407189
# Unit test for function curried_filter
def test_curried_filter():
    # Create new list
    myList = [1, 2, 3, 4, 5]
    # Function filter items less then 5
    # filter_less_then_five = curried_filter(eq(5))
    filter_less_then_five = curried_filter(lambda x: x < 5)
    # Apply filter to list
    result = filter_less_then_five(myList)
    # Check results
    assert result == myList[0:4]

# Generated at 2022-06-14 03:59:48.815244
# Unit test for function memoize
def test_memoize():
    args = ["argument 1", "argument 2"]
    fn = memoize(lambda arg: arg + " was processed")
    for i in range(0, 5):
        for arg in args:
            fn(arg)
    assert len(fn.__closure__[0].cell_contents) == len(args)

# Generated at 2022-06-14 03:59:56.411050
# Unit test for function cond
def test_cond():
    def even(value: int) -> bool:
        """
        :param value:
        :type value: int
        :returns:
        :rtype: bool
        """
        return value % 2 == 0

    def add2(value: int) -> int:
        """
        :param value:
        :type value: int
        :returns:
        :rtype: int
        """
        return value + 2

    assert cond([
        (even, add2),
        (bool, identity),
    ])(1) == 1
    assert cond([
        (even, add2),
        (bool, identity),
    ])(2) == 4



# Generated at 2022-06-14 04:00:02.719776
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(increase, [1, 2, 3, 4]) == [2, 3, 4, 5]
    assert curried_map(increase)([1, 2, 3, 4]) == [2, 3, 4, 5]
    assert curried_map(increase, [1, 2, 3, 4]) == [2, 3, 4, 5]
    assert curried_map(increase, [1, 2, 3, 4]) == [2, 3, 4, 5]



# Generated at 2022-06-14 04:00:14.937543
# Unit test for function find
def test_find():
    """
    Function tests find function.
    :returns:
    """
    collection = [
        {
            'id': 7,
            'name': 'Michael',
            'surname': 'Jordan'
        },
        {
            'id': 8,
            'name': 'Larry',
            'surname': 'Bird'
        }
    ]

    found_element = find(collection, lambda item: item['id'] == 8)
    assert found_element is not None
    assert found_element['name'] == 'Larry'
    assert found_element['surname'] == 'Bird'

    found_element_by_name = find(collection, lambda item: item['name'] == 'Michael')
    assert found_element_by_name is not None
    assert found_element_by_name['id'] == 7


# Generated at 2022-06-14 04:00:28.691674
# Unit test for function curried_map
def test_curried_map():
    assert [i+1 for i in range(0, 30)] == curried_map(increase, [i for i in range(0, 30)])
    assert [i*2 for i in range(0, 30)] == curried_map(lambda x: x*2, [i for i in range(0, 30)])
    assert [i+10 for i in range(0, 30)] == curried_map(lambda x: x+10, [i for i in range(0, 30)])
    assert [1, 2, 3, 4] == curried_map(lambda x: x+1)([0, 1, 2, 3])
    assert [3, 4, 5, 6] == curried_map(lambda x: x+3)([0, 1, 2, 3])

# Generated at 2022-06-14 04:00:29.816022
# Unit test for function eq
def test_eq():
    assert eq(1,1)



# Generated at 2022-06-14 04:00:40.773088
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(lambda x: x + 1, [1, 2, 3, 4]) == [2, 3, 4, 5]
    assert curried_map(lambda x: x * 2, [1, 2, 3, 4, 5])([6, 7, 8, 9]) == [12, 14, 16, 18]
    assert curried_map(lambda x: x * 3, [2, 3, 4])([5, 6, 7], [8, 9, 10]) == [30, 36, 42]
    assert curried_map(lambda x: x + 1)([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]) == [11, 12, 13, 14]

# Generated at 2022-06-14 04:00:46.646721
# Unit test for function cond
def test_cond():
    def is_string(value):
        return isinstance(value, str)
    def get_length(value):
        return len(value)

    length_or_zero = cond([
        (is_string, get_length),
        (lambda value: True, identity),
    ])

    assert length_or_zero("Hello") == 5
    assert length_or_zero(6) == 6


# Generated at 2022-06-14 04:00:49.859610
# Unit test for function curried_filter
def test_curried_filter():
    list_numbers = [1, 2, 3, 4, 5]
    is_even = lambda x: not x % 2

    result = curried_filter(
        is_even,
        list_numbers
    )

    expected_result = [2, 4]
    assert result == expected_result



# Generated at 2022-06-14 04:00:53.185684
# Unit test for function find
def test_find():
    assert find([], lambda value: False) is None
    assert find([1], lambda value: True) == 1
    assert find([1, 2], lambda value: value == 1) == 1
    assert find([1, 2], lambda value: value == 2) == 2
    assert find([1, 2], lambda value: value == 3) is None



# Generated at 2022-06-14 04:01:00.619888
# Unit test for function curry
def test_curry():
    assert compose(5, lambda x: x + 1, lambda x: x * 2, lambda x: x // 2) == 6
    assert curry(lambda x, y, z: x + y + z)(1)(2)(3) == 6
    assert curry(lambda x, y, z: x + y + z)(1)(2)(3) == 6
    assert curry(lambda x, y, z: x + y + z)(1, 2)(3) == 6
    assert curry(lambda x, y, z: x + y + z)(1, 2, 3) == 6


# Generated at 2022-06-14 04:01:07.320412
# Unit test for function cond
def test_cond():
    assert cond([
        (lambda *args: args, lambda *args: args[0] + 10),
        (lambda *args: not args, lambda *args: "It's empty")
    ])(1) == 11
    assert cond([
        (lambda *args: args, lambda *args: args[0] + 10),
        (lambda *args: not args, lambda *args: "It's empty")
    ])() == "It's empty"

# Generated at 2022-06-14 04:01:10.632144
# Unit test for function curry
def test_curry():
    def sum(x, y, z):
        return x + y + z

    curried_add = curry(sum)
    assert curried_add(1)(2)(3) == sum(1, 2, 3)



# Generated at 2022-06-14 04:01:14.899432
# Unit test for function cond
def test_cond():
    @cond([
        (eq(1), increase),
        (eq(2), identity),
        (lambda *_: True, identity),
    ])
    def number(value):
        return value

    assert number(1) == 2



# Generated at 2022-06-14 04:01:22.037603
# Unit test for function eq
def test_eq():
    assert curry(eq)(1)(1)
    assert curry(eq)(1)(2) is False



# Generated at 2022-06-14 04:01:31.309003
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(increase, [1,2,3]) == [2,3,4]
    assert curried_map(increase)([1,2,3]) == [2,3,4]
    assert curried_map(increase, [1]) == [2]
    assert curried_map(increase)([1]) == [2]
    assert curried_map(increase, []) == []
    assert curried_map(increase)([]) == []
    assert curried_map(increase, [1,2,3,4,5,6,7,8,9,10]) == [2,3,4,5,6,7,8,9,10,11]

# Generated at 2022-06-14 04:01:33.153218
# Unit test for function find
def test_find():
    assert find(range(7), lambda x: x % 2 == 0) == 0



# Generated at 2022-06-14 04:01:38.843043
# Unit test for function cond
def test_cond():
    def is_even(value: int) -> bool:
        return value % 2 == 0

    def get_string(value: int) -> str:
        return f"number is: {value}"

    def get_number(value: int) -> int:
        return value

    my_cond = cond([
        (is_even, get_string),
        (eq(True), get_number)
    ])

    assert my_cond(5) == 5
    assert my_cond(6) == "number is: 6"



# Generated at 2022-06-14 04:01:42.098854
# Unit test for function curried_map
def test_curried_map():
    assert pipe(
        [1, 2, 3],
        curried_map(increase),
        curried_map(increase),
    ) == [3, 4, 5]



# Generated at 2022-06-14 04:01:45.265238
# Unit test for function cond
def test_cond():
    assert cond([
        (lambda x: x > 5, lambda x: x),
        (lambda x: x < 5, lambda x: -x),
        (lambda x: x == 5, identity),
    ])(4) == -4



# Generated at 2022-06-14 04:01:50.208701
# Unit test for function curry
def test_curry():
    adder = curry(lambda x, y: x + y)
    assert adder(1)(2) == 3
    assert adder(1, 2) == 3
    assert adder(2)(3) == 5
    assert adder(2, 3) == 5



# Generated at 2022-06-14 04:01:54.587252
# Unit test for function find
def test_find():
    list_to_search = [1, 2, 3, 4]

    assert find(list_to_search, lambda x: x == 3) == 3
    assert find(list_to_search, lambda x: x == 5) is None



# Generated at 2022-06-14 04:01:56.651879
# Unit test for function eq
def test_eq():
    assert eq(1, 1)
    assert not eq(1, 2)



# Generated at 2022-06-14 04:02:04.079307
# Unit test for function cond
def test_cond():
    addition = lambda arg: arg + 1
    subtraction = lambda arg: arg - 1
    current_res = 3
    condition_list = [
        (lambda value: value < 5, addition),
        (lambda value: value == 5, lambda _: print("END")),
        (lambda value: value > 5, subtraction),
    ]
    while True:
        current_res = cond(condition_list)(current_res)
        if current_res == 5:
            break


test_cond()

# Generated at 2022-06-14 04:02:18.117336
# Unit test for function find
def test_find():
    assert find([1, 2, 3], lambda x: x == 2) == 2
    assert find([1, 2, 3], lambda x: x == 5) is None



# Generated at 2022-06-14 04:02:20.403301
# Unit test for function eq
def test_eq():
    assert eq(1, 1) is True and eq(1, 2) is False and eq(1, 2)(3) is False


# Generated at 2022-06-14 04:02:22.976820
# Unit test for function find
def test_find():
    assert find([1, 2, 3, 4], lambda x: x == 2) == 2
    assert find([1, 2, 3, 4], lambda x: x == 5) is None

# Generated at 2022-06-14 04:02:27.356687
# Unit test for function curried_map
def test_curried_map():
    curried_double = curried_map(lambda x: 2 * x)
    assert curried_double([1, 2, 3, 4]) == [2, 4, 6, 8]



# Generated at 2022-06-14 04:02:30.397488
# Unit test for function eq
def test_eq():
    equals = eq(1)

    assert equals(1) == True, 'eq must return True'
    assert equals(2) == False, 'eq must return False'


# Generated at 2022-06-14 04:02:33.646193
# Unit test for function memoize
def test_memoize():
    zero = lambda x: 0
    res = memoize(zero)
    assert res(1) == 0
    assert res(1) == 0
    assert res(3) == 0
    assert res(3) == 0

# Generated at 2022-06-14 04:02:37.479399
# Unit test for function find
def test_find():
    assert find([1, 2, 3], eq(1)) == 1
    assert find([1, 2, 3], eq(2)) == 2
    assert find([1, 2, 3], eq(3)) == 3
    assert find([1, 2, 3], eq(4)) is None



# Generated at 2022-06-14 04:02:41.062292
# Unit test for function eq
def test_eq():
    assert True == eq(1, 1)
    assert False == eq(1, 2)

    eq_curried = eq(1)
    assert True == eq_curried(1)
    assert False == eq_curried(2)



# Generated at 2022-06-14 04:02:43.775138
# Unit test for function curried_map
def test_curried_map():
    collection = [1, 2, 3]
    curried_mapper = curried_map(increase)
    assert curried_mapper(collection) == [2, 3, 4]



# Generated at 2022-06-14 04:02:47.409891
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x > 1)([1, 2, 3]) == [2, 3]
    assert curried_filter(lambda x: x > 1, [1, 2, 3]) == [2, 3]
    assert curried_filter(eq(1), [1, 2, 3]) == [1]



# Generated at 2022-06-14 04:03:13.819361
# Unit test for function curried_filter
def test_curried_filter():
    # Test True
    assert curried_filter(lambda x: x > 0, [1, 2, 1, 2])(0) == [1, 2, 1, 2]
    # Test False
    assert curried_filter(lambda x: x > 0, [1, 2, 1, 2])(5) == []



# Generated at 2022-06-14 04:03:18.216599
# Unit test for function curried_map
def test_curried_map():
    result = curried_map(lambda x: x * x, [1, 2, 3, 4, 5])
    assert result == [1, 4, 9, 16, 25], \
        'test_curried_map_failed, expected [1, 4, 9, 16, 25], but get {0}'.format(result)



# Generated at 2022-06-14 04:03:26.270442
# Unit test for function curry
def test_curry():
    print("\n===Unit test for function curry===")
    assert curry(lambda x: x + 1)(2) == 3
    assert curry(lambda x, y: x + y)(2)(3) == 5
    assert curry(lambda x, y, z: x + y + z)(1, 2)(3) == 6
    # assert curry(lambda x, y, z: x + y + z)(1)(2)(3) == 6



# Generated at 2022-06-14 04:03:29.304513
# Unit test for function eq
def test_eq():
    assert eq(1, 1)
    assert not eq(1, 2)
    assert eq(1)(1)
    assert not eq(1)(2)


# Generated at 2022-06-14 04:03:30.626124
# Unit test for function eq
def test_eq():
    assert eq(5, 5)
    assert not eq(5, 6)



# Generated at 2022-06-14 04:03:35.902854
# Unit test for function find
def test_find():
    assert None is find([{'name': '1'}, {'name': '2'}], lambda item: item['name'] == '3')
    assert {'name': '2'} is find([{'name': '1'}, {'name': '2'}], lambda item: item['name'] == '2')



# Generated at 2022-06-14 04:03:39.935606
# Unit test for function curry
def test_curry():
    assert curry(increase)(1) == 2
    assert curry(increase, 1)(0) == 1
    assert curry(increase, 2)(1)(1) == 3
    assert curry(increase, 2)(1)(0) == 1



# Generated at 2022-06-14 04:03:49.701084
# Unit test for function memoize
def test_memoize():
    def test_func():
        global call_count
        call_count += 1
        return 'test result'

    global call_count
    call_count = 0
    memoized_test_func = memoize(test_func)
    assert memoized_test_func() == 'test result'
    assert memoized_test_func() == 'test result'
    assert memoized_test_func() == 'test result'
    assert memoized_test_func() == 'test result'
    assert memoized_test_func() == 'test result'
    assert memoized_test_func() == 'test result'
    assert memoized_test_func() == 'test result'
    assert memoized_test_func() == 'test result'
    assert call_count == 1



# Generated at 2022-06-14 04:03:56.951272
# Unit test for function cond
def test_cond():
    assert cond([
        (lambda x: x % 2 == 0, lambda x: 'even'),
        (lambda x: x % 2 == 1, lambda x: 'odd'),
    ])(2) == 'even'
    assert cond([
        (lambda x: x % 2 == 0, lambda x: 'even'),
        (lambda x: x % 2 == 1, lambda x: 'odd'),
    ])(1) == 'odd'

    # this test will show error
    # assert cond([
    #     (lambda x: x % 2 == 0, lambda x: 'even'),
    #     (lambda x: x % 2 == 1, lambda x: 'odd'),
    # ])(0) == 'one'



# Generated at 2022-06-14 04:04:00.823752
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(identity)([1, 2, 3]) == [1, 2, 3]
    assert curried_map(increase)([1, 2, 3]) == [2, 3, 4]



# Generated at 2022-06-14 04:04:56.545105
# Unit test for function curry
def test_curry():
    def simple(a, b, c=3, *args, **kwargs):
        return (a, b, c, args, kwargs)

    assert simple(1, 2, 3, 4, 5, x=6, y=7) == (1, 2, 3, (4, 5), {'x': 6, 'y': 7})
    assert simple(1, 2) == (1, 2, 3, (), {})
    assert simple(1, 2, x=6, y=7) == (1, 2, 3, (), {'x': 6, 'y': 7})

    assert curry(simple)(1)(2)(3)(4)(5)(x=6)(y=7) == (1, 2, 3, (4, 5), {'x': 6, 'y': 7})
    assert curry(simple)(1)(2)

# Generated at 2022-06-14 04:05:02.451129
# Unit test for function curry
def test_curry():
    def adder(a, b, c, d):
        return a + b + c + d

    assert curry(adder)(1, 2, 3, 4) == 10
    assert curry(adder)(1, 2)(3, 4) == 10
    assert curry(adder)(1)(2, 3, 4) == 10
    assert curry(adder)(1)(2)(3, 4) == 10
    assert curry(adder)(1, 2, 3)(4) == 10



# Generated at 2022-06-14 04:05:13.892907
# Unit test for function cond
def test_cond():
    def f():
        return 'f'

    def g():
        return 'g'

    def f_of_three(x):
        return x == 3

    def f_of_four(x):
        return x == 4

    # TODO expected f_of_three, f_of_four, f_of_four
    assert f() == cond([
        (f_of_three, f),
        (f_of_four, g),
    ])(3)
    assert g() == cond([
        (f_of_three, f),
        (f_of_four, g),
    ])(4)

    assert g() == cond([
        (f_of_three, f),
        (f_of_four, g),
    ])(4)



# Generated at 2022-06-14 04:05:25.091023
# Unit test for function cond
def test_cond():
    def true(x):
        return True

    def add(a, b):
        return a + b

    def mul(a, b):
        return a * b

    def div(a, b):
        return a / b

    assert cond([(mul, 2), (div, 3)])(1, 2) == 2
    assert cond([(true, 2), (add, 3)])(3, 2) == 3
    assert cond([(true, 2), (true, 3)])(3, 2) == 2
    assert cond([(true, 2)])(3, 2) == 2


# Generated at 2022-06-14 04:05:28.048186
# Unit test for function eq
def test_eq():
    assert eq(1, 1)
    assert not eq(1, 2)
    assert eq(1)(1)
    assert not eq(1)(2)



# Generated at 2022-06-14 04:05:34.419046
# Unit test for function memoize
def test_memoize():
    @memoize
    def fibonacci(x):
        if x <= 1: return x
        else: return fibonacci(x-1) + fibonacci(x-2)
    assert fibonacci(10) == 55
    assert fibonacci(10) == 55
    assert fibonacci(20) == 6765
    assert fibonacci(20) == 6765
    assert fibonacci(30) == 832040
    assert fibonacci(30) == 832040


# Generated at 2022-06-14 04:05:37.650516
# Unit test for function find
def test_find():
    assert find([1, 2, 3], eq(2)) == 2, 'second element is 2'
    assert find([1, 2, 3], eq(4)) is None, 'no item in list equals to 4'



# Generated at 2022-06-14 04:05:44.056696
# Unit test for function curried_filter
def test_curried_filter():
    # values = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    def is_odd_value(x):
        return x % 2

    # russian_peasant_multiplay = compose(
    #     lambda x, y: (x, y),
    #     curried_filter(is_odd_value),
    #     curried_map(increase),
    #     lambda x, y: tuple(x+y for x, y in zip(x, y)),
    # )


# Generated at 2022-06-14 04:05:50.210698
# Unit test for function curry
def test_curry():
    assert curry(lambda x, y, z: x + y + z)(1)(2)(3) == 6
    assert curry(lambda x, y, z: x + y + z)(1, 2)(3) == 6
    assert curry(lambda x, y, z: x + y + z)(1, 2, 3) == 6



# Generated at 2022-06-14 04:05:55.407092
# Unit test for function memoize
def test_memoize():
    def calculate_fibonacci(n):
        if n < 2:
            return n
        return calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)

    fib = memoize(calculate_fibonacci)
    assert fib(5) == 5
    # Next call should not do recursive call
    assert fib(5) == 5

# Generated at 2022-06-14 04:07:02.938233
# Unit test for function find
def test_find():
    collection = [
        {'id': 1},
        {'id': 2},
        {'id': 3},
        {'id': 4},
        {'id': 5},
        {'id': 6},
        {'id': 7},
    ]
    assert find(collection, lambda item: item['id'] == 2) == {'id': 2}
    assert find(collection, lambda item: item['id'] == 3) == {'id': 3}
    assert find(collection, lambda item: item['id'] == 0) is None
    assert find([], lambda item: item['id'] == 0) is None


# Generated at 2022-06-14 04:07:05.977984
# Unit test for function eq
def test_eq():
    assert eq(1, 1)
    assert not eq(1, 2)
    assert not eq("a", 1)



# Generated at 2022-06-14 04:07:12.272028
# Unit test for function curried_filter
def test_curried_filter():
    def fn(x):
        if x is 1:
            return True
        return False
    result = curried_filter(fn, [1, 2, 1])
    if result == [1, 1]:
        print("Test curried_filter is OK!")
    else:
        print("Test curried_filter is Fail!")


# Generated at 2022-06-14 04:07:19.858261
# Unit test for function find
def test_find():
    assert find([], eq(1)) == None
    assert find([1], eq(2)) == None
    assert find([1], eq(1)) == 1
    assert find([1, 1, 1], eq(1)) == 1
    assert find([2, 3, 4], eq(1)) == None
    assert find([1, 2, 3], eq(3)) == 3
    assert find([{'a': 1}, {'a': 2}, {'a': 3}], eq({'a': 3})) == {'a': 3}



# Generated at 2022-06-14 04:07:22.659987
# Unit test for function curried_map
def test_curried_map():
    """
    Check if curried_map function properly work,
    test if increase function applied to each item of list [1, 2, 3].
    """
    assert curried_map(increase)([1, 2, 3]) == [2, 3, 4]



# Generated at 2022-06-14 04:07:28.044925
# Unit test for function memoize
def test_memoize():
    test = 0
    def fn(value):
        nonlocal test
        test += 1
        return value

    memoized = memoize(fn)
    assert memoized(1) == 1
    assert memoized(2) == 2
    assert memoized(1) == 1
    assert memoized(2) == 2
    assert test == 2



# Generated at 2022-06-14 04:07:35.377398
# Unit test for function memoize
def test_memoize():
    """
    Unit test for function memoize
    """
    assert identity(1) == 1
    identity_memoized = memoize(identity)
    assert identity_memoized(1) == 1
    assert identity_memoized(1) == 1
    identity_wrong_memoized = memoize(identity, lambda x, y: False)
    assert identity_wrong_memoized(1) == 1
    assert identity_wrong_memoized(1) == 2



# Generated at 2022-06-14 04:07:41.366465
# Unit test for function find
def test_find():
    print('Unit test for function find - START')
    assert find(range(10), lambda x: x > 5) == 6
    assert find(range(10), lambda x: x > 10) == None
    assert find([1, 2, 2, 3], lambda x: x > 2) == 2
    print('Unit test for function find - SUCCESS')



# Generated at 2022-06-14 04:07:43.733746
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(increase, [1, 2, 3]) == [2, 3, 4]


# Generated at 2022-06-14 04:07:48.022121
# Unit test for function find
def test_find():
    my_list = [1, 2, 3, 4, 5]
    assert find(my_list, lambda x: x == 4) == 4
    assert find(my_list, lambda x: x == 6) is None

