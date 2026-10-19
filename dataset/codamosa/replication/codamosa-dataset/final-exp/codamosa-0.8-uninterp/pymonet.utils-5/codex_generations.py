

# Generated at 2022-06-14 03:58:07.536746
# Unit test for function find
def test_find():
    array = [1, 2, 3, 4]
    key = lambda a: a == 5
    assert find(array, key) is None

    key = lambda a: a == 1
    assert find(array, key) == 1

    array = [
        {'id': 1, 'name': 'Alice'},
        {'id': 2, 'name': 'Bob'},
        {'id': 3, 'name': 'Charlie'},
        {'id': 4, 'name': 'Diana'}
    ]
    key = lambda a: a['id'] == 3
    assert find(array, key) == {'id': 3, 'name': 'Charlie'}


# Generated at 2022-06-14 03:58:10.150782
# Unit test for function eq
def test_eq():
    assert eq(1, 2) is False
    assert eq(1, 1) is True
    assert eq(None) is None


# Generated at 2022-06-14 03:58:12.765035
# Unit test for function find
def test_find():
    assert find([1, 2, 3], lambda x: x == 3) == 3
    assert find([1, 2, 3], lambda x: x == 4) is None



# Generated at 2022-06-14 03:58:21.481003
# Unit test for function eq
def test_eq():
    assert eq(1, 1)
    assert not eq(1, 2)
    assert eq({}, {})
    assert not eq({}, {'a': 'b'})
    assert eq((1, 2), (1, 2))
    assert not eq((1, 2), (1, 2, 3))
    assert eq([1, 2], [1, 2])
    assert not eq([1, 2], [1, 2, 3])



# Generated at 2022-06-14 03:58:33.021312
# Unit test for function cond
def test_cond():
    """
    test_cond test cond function
    """
    cond_list = [
        (lambda x: x < 0, lambda x: str(x) + " is less then 0"),
        (lambda x: x == 0, lambda x: str(x) + " is equal 0"),
        (lambda x: x > 0, lambda x: str(x) + " is greater then 0")
    ]
    _cond = cond(cond_list)

    assert _cond(5) == "5 is greater then 0"
    assert _cond(0) == "0 is equal 0"
    assert _cond(-2) == "-2 is less then 0"



# Generated at 2022-06-14 03:58:39.451376
# Unit test for function cond
def test_cond():
    assert True is cond(
        [
            (identity, lambda x: x),
            (lambda x: False, lambda x: not x),
        ]
    )(True)
    assert False is cond(
        [
            (identity, lambda x: x),
            (lambda x: False, lambda x: not x),
        ]
    )(False)

# Generated at 2022-06-14 03:58:44.596370
# Unit test for function find
def test_find():
    assert find([1, 2, 3], lambda x: x == 2) == 2
    assert find(['foo', 'bar', 'baz'], lambda x: x.startswith('b')) == 'bar'
    assert find([{'foo': 1}, {'bar': 2}, {'baz': 3}],
                lambda x: 'baz' in x) == {'baz': 3}
    assert find([{'foo': 1}, {'bar': 2}, {'baz': 3}],
                lambda x: 'qux' in x) is None



# Generated at 2022-06-14 03:58:47.489633
# Unit test for function find
def test_find():
    assert find([1, 2, 3, 4, 5], lambda x: x == 3) == 3
    assert find([1, 2, 3, 4, 5], lambda x: x == 10) == None

# Generated at 2022-06-14 03:58:50.104374
# Unit test for function find
def test_find():
    assert find([1, 2, 3], eq(2)), 2
    assert find([1, 2, 3], eq(4)) is None



# Generated at 2022-06-14 03:58:53.238406
# Unit test for function curried_filter
def test_curried_filter():
    l = [1, 2, 3, 4, 5]
    assert ([3, 4] == curried_filter(lambda x: x % 2 == 1, l))



# Generated at 2022-06-14 03:59:07.778908
# Unit test for function curried_map
def test_curried_map():
    items = [1, 2, 3, 4]
    assert eq(
        curried_map(increase)(items),
        [2, 3, 4, 5]
    )
    assert eq(
        curried_map(lambda item: item + 1)(items),
        [2, 3, 4, 5]
    )



# Generated at 2022-06-14 03:59:17.673523
# Unit test for function cond
def test_cond():
    def f1(x):
        return x % 2 == 0

    def f2(x):
        return x * x

    def f3(x):
        return x ** 3

    def f4(x):
        return x + 1

    def f5(x):
        return x + 2

    assert cond([(f1, f2), (f1, f3)]) == f2
    assert cond([(f1, f2), (f1, f3), (f1, f4), (f1, f5)]) == f2
    assert cond([(f1, f2), (f1, f3), (f1, f4), (f1, f5)], 5) == f3(5)

# Generated at 2022-06-14 03:59:22.846065
# Unit test for function curried_map
def test_curried_map():
    collection: List[int] = [1, 2, 3, 4, 5]
    mapped_collection: List[int] = curried_map(lambda x: x * 2, collection)
    assert mapped_collection == [2, 4, 6, 8, 10]



# Generated at 2022-06-14 03:59:25.821005
# Unit test for function curried_map
def test_curried_map():
    """
    Test curried_map function.
    """
    assert [0, 3, 6] == curried_map(lambda x: x * 2)([0, 1, 2, 3])



# Generated at 2022-06-14 03:59:27.610894
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(increase, [1, 2, 3]) == [2, 3, 4]



# Generated at 2022-06-14 03:59:33.558274
# Unit test for function find
def test_find():
    assert find([7, 9, 11], lambda x: x > 10) is 11
    assert find(["fun", "is", "great"], lambda s: len(s) == 5) == 'great'
    assert find({7, 9, 11}, lambda x: x > 10) is 11
    print ("Passed unit test for function 'find'")


# Generated at 2022-06-14 03:59:35.569408
# Unit test for function eq
def test_eq():
    assert eq(eq(1)(1)) == True
    assert eq(eq(1)('1')) == False



# Generated at 2022-06-14 03:59:46.638956
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x % 2 == 0)([1, 2, 3, 4]) == [2, 4]
    assert curried_filter(lambda x: x % 2 == 0, [1, 2, 3, 4]) == [2, 4]
    assert curried_filter(lambda x: x % 2 == 0)(range(10)) == [0, 2, 4, 6, 8]
    assert curried_filter(lambda x: x % 2 == 0)(range(10)) == curried_filter(lambda x: x % 2 == 0, range(10))
    assert curried_filter(lambda x: x % 2 == 0)(range(10)) != curried_filter(lambda x: x % 2 != 0, range(10))



# Generated at 2022-06-14 03:59:56.238068
# Unit test for function find
def test_find():
    collection = [1, 2, 3, 1, 5, 6]
    eq_to_two = eq(2)

    assert find(collection, eq_to_two) == 2, 'find works with simple functions'

    eq_to_one = eq(1)
    assert find(collection, eq_to_one) == 1, 'find works with some simple functions'

    collection = ['a', 'b', 'c', 'a', 'e', 'f']
    eq_to_a = eq('a')

    assert find(collection, eq_to_a) == 'a', 'find works with lists of strings'

    collection = [(1, 2, 3),{'a': 1}, (1, 2)]

# Generated at 2022-06-14 04:00:03.681847
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x % 2 == 0, range(10)) == [0, 2, 4, 6, 8]
    assert curried_filter(lambda x: x % 3 == 0, range(10)) == [0, 3, 6, 9]
    assert curried_filter(lambda x: x % 3 == 0, range(10)) == [0, 3, 6, 9]
    assert curried_filter(eq(5), range(10)) == [5]
    assert curried_filter(lambda x: x % 4 == 0, range(10)) == [0, 4, 8]



# Generated at 2022-06-14 04:00:15.705871
# Unit test for function curried_filter
def test_curried_filter():
    """
    Test for correct curried_filter work.
    """
    filter_three = curried_filter(eq(3))
    assert ([3] == filter_three([1, 2, 3, 4]))
    assert ([1, 3, 5, 7] == filter_three([1, 3, 5, 7]))
    assert ([3, 9, 12] == filter_three([3, 6, 9, 12]))
    assert ([3, 2] == filter_three([3, 2, 3]))


# Generated at 2022-06-14 04:00:25.451097
# Unit test for function curried_filter
def test_curried_filter():
    to_filter = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    fn_is_smaller_than_five = lambda x: x < 5
    fn_increase = lambda x: x + 1
    fn_is_even = lambda x: x % 2 == 0
    fn_is_seven = lambda x: x == 7
    fn_increase_if_is_even = compose(fn_is_even, fn_increase)
    fn_is_greater_than_ten = compose(eq(10), increase)
    fn_is_not_ten = lambda x: x != 10
    fn_is_seven_and_even = lambda x: fn_is_even(x) and fn_is_seven(x)

# Generated at 2022-06-14 04:00:30.603552
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(lambda x: x + 1)([1, 2, 3]) == [2, 3, 4]
    assert curried_map(lambda x: x + 1, [1, 2, 3]) == [2, 3, 4]



# Generated at 2022-06-14 04:00:32.809447
# Unit test for function eq
def test_eq():
    assert eq(5, 5) == True
    assert eq(5, 7) == False



# Generated at 2022-06-14 04:00:38.098725
# Unit test for function find
def test_find():
    print('\n# Start test for function "find"')
    assert find(['a', 'b', 'c'], lambda item: item == 'b') == 'b'
    assert find([1, 2, 3], lambda item: item > 2) == 3
    print('# Finish test for function "find"\n')



# Generated at 2022-06-14 04:00:42.155251
# Unit test for function eq
def test_eq():
    assert eq(1, 1) == True
    assert eq(1)(1) == True
    assert eq(1, 2) == False
    assert eq(1)(2) == False


# Generated at 2022-06-14 04:00:46.178075
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(lambda x: x + 1, [1, 2, 3]) == [2, 3, 4]
    assert curried_map(lambda x: x + 2, [1, 2, 3]) == [3, 4, 5]
    assert curried_map(lambda x: x + 100, [1, 2, 3]) == [101, 102, 103]



# Generated at 2022-06-14 04:00:49.043677
# Unit test for function curried_map
def test_curried_map():
    mapped = curried_map(increase, [1, 2, 3])
    assert mapped == [2, 3, 4]


# Generated at 2022-06-14 04:00:51.476664
# Unit test for function find
def test_find():
    assert find([1, 2, 3], lambda item: item < 1) is None
    assert find([1, 2, 3], lambda item: item == 2) == 2



# Generated at 2022-06-14 04:00:59.227949
# Unit test for function cond
def test_cond():
    is_big = lambda num: num > 100
    say_hi = lambda: "hi"
    say_bye = lambda: "bye"
    is_true = lambda num: num

    assert cond([(is_big, say_hi), (is_true, say_bye)], 42) == 'bye'
    assert cond([(is_big, say_hi), (is_true, say_bye)], 121) == 'hi'


# Test for function identity

# Generated at 2022-06-14 04:01:17.746386
# Unit test for function curried_filter
def test_curried_filter():
    collection = [1, 2, 3, 4, 5]
    even = lambda x: x % 2 == 0
    odd = lambda x: x % 2 != 0
    assert (curried_filter(even, collection) == [2, 4])
    assert (curried_filter(odd, collection) == [1, 3, 5])


# Generated at 2022-06-14 04:01:19.858016
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(increase)([1, 2]) == [2, 3]



# Generated at 2022-06-14 04:01:21.727693
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(increase, [1, 2, 3]) == [2, 3, 4]



# Generated at 2022-06-14 04:01:26.139305
# Unit test for function curried_map
def test_curried_map():
    assert [1, 2, 3] == curried_map(increase)([0, 1, 2])
    assert [1, 2, 3] == curried_map(increase, [0, 1, 2])
    assert [1, 2, 3] == curried_map(increase)([0, 1, 2])



# Generated at 2022-06-14 04:01:33.417061
# Unit test for function memoize
def test_memoize():
    count = 0

    @memoize
    def inc(x):
        nonlocal count
        count = count + 1
        return x + 1

    assert 1 == inc(0)
    assert 1 == count
    assert 2 == inc(1)
    assert 2 == count
    assert 1 == inc(0)
    assert 2 == count
    assert 2 == inc(1)
    assert 2 == count



# Generated at 2022-06-14 04:01:34.872840
# Unit test for function eq
def test_eq():
    assert eq(1, 1) is True
    assert eq(1, 2) is False



# Generated at 2022-06-14 04:01:38.107277
# Unit test for function find
def test_find():
    string_list = ['a', 'b', 'c']
    assert find(string_list, identity) == 'a'
    assert find(string_list, eq('b')) == 'b'
    assert find(string_list, eq('d')) is None



# Generated at 2022-06-14 04:01:39.457414
# Unit test for function find
def test_find():
    assert find(range(5), lambda x: x == 2) is 2



# Generated at 2022-06-14 04:01:42.469200
# Unit test for function find
def test_find():
    assert find([1, 2, 3, 4], eq(4)) == 4
    assert find([1, 2, 3, 4], eq(5)) is None



# Generated at 2022-06-14 04:01:49.366436
# Unit test for function find
def test_find():
    list_for_find = [('Carol', 'A'), ('Bill', 'B'), ('Cara', 'C')]
    assert find(list_for_find, lambda item: item[0] == 'Cara') == ('Cara', 'C')
    assert find(list_for_find, lambda item: item[1] == 'D') == None



# Generated at 2022-06-14 04:02:17.813339
# Unit test for function curried_filter
def test_curried_filter():
    arr = [1, 2, 3]
    assert curried_filter(lambda x: x % 2 == 0)(arr) == [2]
    list_of_numbers = [1, 2, 3, 4, 5]
    assert curried_filter(lambda x: x % 2 == 0)([]) == []
    assert curried_filter(lambda x: x % 2 == 1)(list_of_numbers) == [1, 3, 5]
    assert curried_filter(lambda x: x % 2 == 0)(list_of_numbers) == [2, 4]
    assert curried_filter(lambda x: x == 1)(list_of_numbers) == [1]
    assert curried_filter(lambda x: x == 4)(list_of_numbers) == [4]

# Generated at 2022-06-14 04:02:20.047368
# Unit test for function memoize
def test_memoize():
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    m_factorial = memoize(factorial)
    assert m_factorial(2) == 2
    assert m_factorial(2) == 2
    assert m_factorial(2) == 2

    # Unit test for function cond


# Generated at 2022-06-14 04:02:25.718545
# Unit test for function memoize
def test_memoize():
    @memoize
    def add(value):
        return value + 1

    assert add(1) == 2
    assert add(1) == 2

    memoized_curried_filter = memoize(curried_filter)

    def odd(x):
        return x % 2

    assert memoized_curried_filter(odd)([1, 2, 3, 4]) == [1, 3]
    assert memoized_curried_filter(odd)([1, 2, 3, 4]) == [1, 3]



# Generated at 2022-06-14 04:02:27.746908
# Unit test for function eq
def test_eq():
    x = eq(1, 1)
    assert x, "Function eq should return True"
    y = eq(1, 2)
    assert not y, "Function eq should return False"



# Generated at 2022-06-14 04:02:37.536014
# Unit test for function memoize
def test_memoize():
    count = 0

    @memoize
    def count_add(*args):
        nonlocal count
        count += 1
        return count

    def assert_count(count_value):
        """
        Function for test memoize function
        """
        nonlocal count
        assert count == count_value

    count_add(1)
    count_add(1)
    assert_count(1)

    count_add(2)
    count_add(2)
    assert_count(2)

    count_add('2')
    count_add('2')
    assert_count(2)

    count_add('number')
    count_add('number')
    count_add('number')
    assert_count(3)



# Generated at 2022-06-14 04:02:45.595385
# Unit test for function curried_filter
def test_curried_filter():
    assert curried_filter(lambda x: x > 1, [0, 1, 2, 3, 4, 5]) == [2, 3, 4, 5]
    assert curried_filter(lambda x: x > 1, [0, 1])([2, 3, 4, 5]) == [2, 3, 4, 5]
    assert curried_filter(lambda x: x > 1)([0, 1])([2, 3, 4, 5]) == [2, 3, 4, 5]
    assert curried_filter(lambda x: x > 1, [0, 1])([2, 3, 4, 5]) == [2, 3, 4, 5]



# Generated at 2022-06-14 04:02:47.464441
# Unit test for function eq
def test_eq():
    assert eq(1)(1)
    assert not eq(1)(2)



# Generated at 2022-06-14 04:02:52.082580
# Unit test for function find
def test_find():
    collection = [1, 2, 3, 4, 5]
    assert find(collection, lambda value: value < 2) == 1
    assert find(collection, lambda value: value == 4) == 4
    assert find(collection, lambda value: value > 4) == 5
    assert find(collection, lambda value: value == 7) is None



# Generated at 2022-06-14 04:02:57.267536
# Unit test for function curried_map
def test_curried_map():
    """
    This is unit test for function curried_map.
    """
    fn = curried_map(lambda x: x + 1)
    assert fn([1, 2, 3]) == [2, 3, 4]

    fn = curried_map(lambda x: x + 1)
    assert fn([1, 2, 3]) == [2, 3, 4]



# Generated at 2022-06-14 04:03:08.768188
# Unit test for function cond
def test_cond():
    def add(value):
        return value + 1

    def logging(value):
        print(value)
        return value

    def return_none(value):
        return None

    def raise_error(value):
        raise Exception()

    # cond without case
    assert cond([])() == None

    # first case
    assert cond([(lambda *args: True, lambda *args: 'first')])('value') == 'first'

    # first case with several argument
    assert cond([(lambda *args: True, lambda *args: 'first')])('value', 1, 'argument') == 'first'

    # first case with another function
    assert cond([(lambda *args: True, add)])(1) == 2

    # second case

# Generated at 2022-06-14 04:03:31.451356
# Unit test for function eq
def test_eq():
    assert eq(1, 1) == True
    assert eq(1, 2) == False
    assert eq(3, 3) == True
    assert eq(3, 5) == False
    assert eq(3)(3) == True
    assert eq(3)(5) == False


# Generated at 2022-06-14 04:03:42.621964
# Unit test for function cond
def test_cond():
    def is_even(value: int) -> bool: return value % 2 == 0
    def is_odd(value: int) -> bool: return not is_even(value)
    def is_gt_5(value: int) -> bool: return value > 5
    def is_lt_5(value: int) -> bool: return not is_gt_5(value)

    def add(value: int, value1: int) -> int: return value + value1
    def sub(value: int, value1: int) -> int: return value - value1

    result: Callable = cond([
        (is_even, identity),
        (is_odd, increase)
    ])

    assert result(1) == 2
    assert result(2) == 2


# Generated at 2022-06-14 04:03:44.558280
# Unit test for function eq
def test_eq():
    assert eq(1, 1) == True
    assert eq(1, 2) == False



# Generated at 2022-06-14 04:03:52.235699
# Unit test for function curried_filter
def test_curried_filter():
    data = [
        {
            "name": "Vasya",
            "age": 20
        },
        {
            "name": "Petya",
            "age": 30
        },
        {
            "name": "Kolya",
            "age": 40
        }
    ]
    curried_filter_age30 = curried_filter(lambda item: item["age"] > 30)
    curried_filter_age30_data = curried_filter_age30(data)
    curried_filter_age30_len = len(curried_filter_age30_data)
    assert curried_filter_age30_len == 1

# Generated at 2022-06-14 04:03:58.650556
# Unit test for function curried_map
def test_curried_map():
    list_a = [1, 2, 3, 4, 5]
    curried_map_a = curried_map(increase)
    assert curried_map_a(list_a) == [2, 3, 4, 5, 6]

    curried_map_b = curried_map(lambda x: x + 1)
    assert curried_map_b(list_a) == [2, 3, 4, 5, 6]

    curried_map_c = curried_map(lambda x: x * 2)
    assert curried_map_c(list_a) == [2, 4, 6, 8, 10]

    curried_map_d = curried_map(lambda x: x / 2)

# Generated at 2022-06-14 04:04:05.858209
# Unit test for function eq
def test_eq():
    assert eq(1, 2) == False
    assert eq(1, 1) == True
    assert eq('A', 'a') == False
    assert eq('A', 'A') == True
    assert eq((1, 2), (1, 2)) == True
    assert eq((1, 2, 3), (1, 2)) == False
    assert eq([1, 2, 3], [1, 2, 3]) == True



# Generated at 2022-06-14 04:04:14.595392
# Unit test for function curried_map
def test_curried_map():
    double = lambda x: x * 2
    assert curried_map(double, [1, 2, 3]) == [2, 4, 6]
    assert curried_map(double)([1, 2, 3]) == [2, 4, 6]
    assert curried_map(double, [])([1, 2, 3]) == [2, 4, 6]
    assert curried_map(double)([1, 2, 3])([1, 2]) == [2, 4, 6]



# Generated at 2022-06-14 04:04:23.558147
# Unit test for function cond
def test_cond():
    def make_add(arg1):
        def add(arg2):
            return arg1 + arg2
        return add

    def make_sub(arg1):
        def sub(arg2):
            return arg1 - arg2
        return sub

    conditions = [
        (lambda arg: arg > 0, make_add(2)),
        (lambda arg: arg == 0, lambda arg: arg),
        (lambda arg: arg <= 0, make_sub(-2)),
    ]

    result_fn_1 = cond(conditions)(1)
    result_fn_2 = cond(conditions)(0)
    result_fn_3 = cond(conditions)(-1)

    assert result_fn_1(1) == 3
    assert result_fn_2(2) == 0

# Generated at 2022-06-14 04:04:32.908211
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(lambda x: x * 2, [1, 2] * 2) == [2, 4] * 2
    assert curried_map(increase, [1, 2, 3]) == [2, 3, 4]
    assert curried_map(lambda x: x * 2)([1, 2]) == [2, 4]
    assert curried_map(lambda x: x * 2)([1, 2])([1, 2]) == [2, 4, 2, 4]



# Generated at 2022-06-14 04:04:37.292754
# Unit test for function find
def test_find():
    data = [0, 0, 0, 1, 2]
    assert find(data, lambda x: x == 0) == 0
    assert find(data, lambda x: x == 1) == 1
    assert find(data, lambda x: x == 2) == 2
    assert find(data, lambda x: x == 3) is None


# Unit tests for function compose

# Generated at 2022-06-14 04:05:22.999366
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(increase)([1, 2, 3]) == [2, 3, 4]
    assert curried_map(increase)([]) == []
    assert curried_map(increase)([1]) == [2]
    assert curried_map(lambda x: x + 1)([1, 2, 3]) == [2, 3, 4]



# Generated at 2022-06-14 04:05:29.015714
# Unit test for function memoize
def test_memoize():
    @memoize
    def factorial(n: int) -> int:
        """
        Calculate factorial of number n.

        :param n: number for calculate factorial
        :type n: Int
        :returns: result
        :rtype: Int
        """
        assert(n >= 0)
        if n == 0:
            return 1
        return n * factorial(n - 1)

    assert(factorial(0) == 1)
    assert(factorial(1) == 1)
    assert(factorial(2) == 2)
    assert(factorial(3) == 6)
    assert(factorial(4) == 24)
    assert(factorial(5) == 120)


# Generated at 2022-06-14 04:05:38.567495
# Unit test for function curried_filter
def test_curried_filter():
    """
    Test curried_filter function work
    """
    # pylint: disable=C0103
    assert curried_filter(eq(1), [1, 2, 3, 4, 5])(0) == [1]
    assert curried_filter(eq(7), [1, 2, 3, 4, 5])(1) == []
    assert curried_filter(increase, [1, 2, 3, 4, 5])(2) == [3, 4, 5]
    assert curried_filter(identity, [1, 2, 3, 4, 5])(3) == [1, 2, 3, 4, 5]



# Generated at 2022-06-14 04:05:40.710422
# Unit test for function curried_filter
def test_curried_filter():
    arr = [1, 2, 5]
    assert curried_filter(lambda x: x >= 2)(arr) == [2, 5]



# Generated at 2022-06-14 04:05:47.191824
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(identity, [1, 2, 3]) == [1, 2, 3]
    assert curried_map(increase, [1, 2, 3]) == [2, 3, 4]
    assert curried_map(increase)([1, 2, 3]) == [2, 3, 4]



# Generated at 2022-06-14 04:05:55.061114
# Unit test for function memoize
def test_memoize():
    def sum_of_two(a, b):
        return a + b

    def sum_of_two_true(a, b):
        return True

    assert memoize(sum_of_two)(2, 2) == 4
    assert memoize(sum_of_two)(2, 2) == 4
    assert memoize(sum_of_two, sum_of_two_true)(2, 3) == 5
    assert memoize(sum_of_two, sum_of_two_true)(2, 3) == 5



# Generated at 2022-06-14 04:06:02.459534
# Unit test for function find
def test_find():
    assert find([1, 2, 3], lambda x: x == 3) == 3
    assert find(['arnold', 'stalone', 'eastwood'], lambda x: x == 'arnold') == 'arnold'
    assert find(['arnold', 'stalone', 'eastwood'], lambda x: x == 'tarantino') is None
    assert find([], lambda x: x == 'tarantino') is None
    print('Tests for "find" function was passed')


# Generated at 2022-06-14 04:06:09.281045
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(increase)([1, 2, 3]) == [2, 3, 4]
    assert curried_map(increase, [1, 2, 3]) == [2, 3, 4]
    assert curried_map(increase, []) == []
    assert curried_map(identity, [1, 2, 3]) == [1, 2, 3]



# Generated at 2022-06-14 04:06:16.289852
# Unit test for function curry
def test_curry():
    def somme(a, b, c):
        return a + b + c

    assert curry(somme)(1, 2, 3) == 6
    assert curry(somme)(1)(2)(3) == 6
    assert curry(somme)(1)(2, 3) == 6
    assert curry(somme)(1, 2)(3) == 6
    assert curry(somme)(1, 2, 3, 4) == 6
    assert curry(somme)(1, 2)(3, 4) == 6
    assert curry(somme)(1)(2)(3)(4) == 6



# Generated at 2022-06-14 04:06:18.352099
# Unit test for function eq
def test_eq():
    assert eq(3, 3)


test_eq()



# Generated at 2022-06-14 04:07:11.949700
# Unit test for function memoize
def test_memoize():
    fib = memoize(lambda n: n if n < 2 else fib(n - 2) + fib(n - 1))
    assert fib(10) == 55
    assert fib(20) == 6765
    assert fib(0) == 0
    assert fib(1) == 1



# Generated at 2022-06-14 04:07:15.856097
# Unit test for function curried_map
def test_curried_map():
    assert all(
        curried_map(
            lambda item1: item1 + 1,
            [1, 2, 3]
        ) == [2, 3, 4]
    )



# Generated at 2022-06-14 04:07:18.469240
# Unit test for function find
def test_find():
    assert find([1, 2, 3], lambda item: item == 2) == 2
    assert find([1, 2, 3], lambda item: item == 5) is None



# Generated at 2022-06-14 04:07:21.941247
# Unit test for function memoize
def test_memoize():
    @memoize
    def sqr(value):
        return value ** 2
    assert sqr(3) == 9
    assert sqr(3) == 9


# Generated at 2022-06-14 04:07:23.480473
# Unit test for function eq
def test_eq():
    assert eq(1, 1) is True



# Generated at 2022-06-14 04:07:28.392843
# Unit test for function curried_map
def test_curried_map():
    test_list = [1, 2, 3]
    curried_mapper = curried_map(identity)
    test_result = [curried_mapper([item]) for item in test_list]
    assert test_result == [[1], [2], [3]]



# Generated at 2022-06-14 04:07:40.869751
# Unit test for function memoize
def test_memoize():
    # Example

    def add(a, b):
        return a + b

    memoized_add = memoize(add)

    assert memoized_add(1, 2) == 3
    assert memoized_add(1, 2) == 3
    assert memoized_add(2, 3) == 5
    assert memoized_add(2, 3) == 5

    # Test with own function
    def double(a):
        return a * 2

    memoized_double = memoize(double)

    assert memoized_double(-1) == -2
    assert memoized_double(-1) == -2
    assert memoized_double(0) == 0
    assert memoized_double(0) == 0
    assert memoized_double(1) == 2
    assert memoized_double(1) == 2



# Generated at 2022-06-14 04:07:45.005089
# Unit test for function curried_map
def test_curried_map():
    assert curried_map(lambda x: x + 1)([1, 2, 3]) == [2, 3, 4]
    assert curried_map(lambda x: x + 1)([1, 2])([3, 4]) == [2, 3]



# Generated at 2022-06-14 04:07:54.514131
# Unit test for function memoize
def test_memoize():
    @memoize
    def factory(value):
        return value

    assert factory('x') == 'x'
    assert factory('x') == 'x'

    @memoize
    def i(value):
        return value

    assert id(i(5)) == id(i(5))

    @memoize
    def i1(value):
        return value

    assert id(i1('x')) == id(i1('x'))

    @memoize
    def i2(value):
        return value

    assert id(i2(True)) == id(i2(True))

