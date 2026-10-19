

# Generated at 2022-06-14 03:44:29.006733
# Unit test for method filter of class Try
def test_Try_filter():
    class TestException(Exception):
        pass

    def fn(num) -> Try:
        """
        :returns: Successfully Try when num is greater than 0, othercase not successfully Try with exception.
        :rtype: Try
        """
        if num > 0:
            return Try(num, True)
        return Try(TestException, False)

    assert fn(0).filter(lambda x: x == 0) == Try(TestException, False)
    assert fn(1).filter(lambda x: x > 0) == Try(1, True)
    assert fn(1).filter(lambda x: x == 1) == Try(1, True)
    assert fn(0).filter(lambda x: x > 0) == Try(TestException, False)



# Generated at 2022-06-14 03:44:36.359988
# Unit test for method filter of class Try
def test_Try_filter():
    # GIVEN initialized Try with value is list and Try is successfully
    test = Try([1, 2, 3], True)
    # WHEN method filter is called with predicate len is equal 3
    result = test.filter(lambda x: len(x) == 3)
    # THEN returns Try with previous value
    assert result == Try([1, 2, 3], True)


# Generated at 2022-06-14 03:44:40.012169
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test filter method of class Try.

    :return:
    """
    assert Try.of(lambda: 1).filter(lambda x: x) == Try(1, True)
    assert Try.of(lambda: 1).filter(lambda x: not x) == Try(1, False)



# Generated at 2022-06-14 03:44:46.656432
# Unit test for method filter of class Try
def test_Try_filter():
    def f(a):
        return a > 5
    monad = Try(10, True)
    assert monad.filter(f) == Try(10, True)
    monad = Try(10, False)
    assert monad.filter(f) == Try(10, False)
    monad = Try(1, True)
    assert monad.filter(f) == Try(1, False)
test_Try_filter()

# Generated at 2022-06-14 03:44:50.335565
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: x > 0) == Try(1, True)
    assert Try(1, True).filter(lambda x: x > 1) == Try(1, False)

# Generated at 2022-06-14 03:44:59.188919
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test filter method of class Try.
    Expected:
    1. Try[value="A", is_success=True].filter(lambda x: len(x) > 0) -> Try[value="A", True]
    2. Try[value="A", is_success=True].filter(lambda x: True) -> Try[value="A", True]
    3. Try[value="A", is_success=True].filter(lambda x: False) -> Try[value="A", False]
    4. Try[value="A", is_success=False].filter(lambda x: True) -> Try[value="A", False]

    :returns: Nothing.
    :rtype: None
    """

# Generated at 2022-06-14 03:45:06.058969
# Unit test for method filter of class Try
def test_Try_filter():
    # When
    try_obj = Try(23, True)

    # Then
    assert try_obj.filter(lambda x: x < 25) == Try(23, True)
    assert try_obj.filter(lambda x: x < 23) == Try(23, False)
    assert try_obj.filter(lambda x: x > 25) == Try(23, False)

# Generated at 2022-06-14 03:45:10.963094
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(x):
        return x == 3

    assert Try(1, True).filter(filterer) == Try(1, False)
    assert Try(3, True).filter(filterer) == Try(3, True)
    assert Try(4, False).filter(filterer) == Try(4, False)



# Generated at 2022-06-14 03:45:16.395317
# Unit test for method filter of class Try
def test_Try_filter():
    def even(num):
        return num % 2 == 0

    assert_that(Try.of(lambda: 1).filter(even), equal_to(Try(1, False)))

    assert_that(Try.of(lambda: 2).filter(even), equal_to(Try(2, True)))



# Generated at 2022-06-14 03:45:18.554783
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    def is_positive(x):
        return x > 0

    assert Try(10, True).filter(is_positive) == Try(10, True)
    assert Try(10, True).filter(lambda x: x == 0) == Try(10, False)



# Generated at 2022-06-14 03:45:28.907432
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test filter method of class Try.

    :returns: true when test is successfully
    :rtype: bool
    """
    # Given
    try_val = Try.of(lambda: 5)
    # When
    try_filtered = try_val.filter(lambda x: x == 5)
    # Then
    return try_filtered == Try(5, True)



# Generated at 2022-06-14 03:45:31.429517
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(0, True).filter(lambda x: x < 10) == Try(0, True)
    assert Try(10, True).filter(lambda x: x < 10) == Try(10, False)
    assert Try(0, False).filter(lambda x: x < 10) == Try(0, False)


# Generated at 2022-06-14 03:45:37.948077
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    # Case: not successfully Try.
    def f1(x):
        return True
    assert Try(1, False).filter(f1) == Try(1, False)
    # Case: successfully Try, but filterer returns False.
    def f2(x):
        return False
    assert Try(1, True).filter(f2) == Try(1, False)
    # Case: successfully Try and filterer returns True.
    def f3(x):
        return True
    assert Try(1, True).filter(f3) == Try(1, True)



# Generated at 2022-06-14 03:45:47.326921
# Unit test for method filter of class Try
def test_Try_filter():
    from unittest.mock import MagicMock

    mocked_filterer = MagicMock(return_value=True)

    assert Try(1, True).filter(mocked_filterer) == Try(1, True)
    mocked_filterer.assert_called_once_with(1)

    mocked_filterer = MagicMock(return_value=False)

    assert Try(1, True).filter(mocked_filterer) == Try(1, False)
    mocked_filterer.assert_called_once_with(1)


# Generated at 2022-06-14 03:45:50.741526
# Unit test for method filter of class Try
def test_Try_filter():
    """
    When filterer returns True Try returns copy of self.
    """
    try_value = Try(5, True)
    result = try_value.filter(lambda x: 5 == x)
    assert result == try_value


# Generated at 2022-06-14 03:45:59.006689
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda x: x ** 2, 2).filter(lambda x: x > 10) == Try(4, True)
    assert Try.of(lambda x: x ** 2, 2).filter(lambda x: x < 10) == Try(4, False)
    assert Try.of(lambda x: "abc", 4).filter(lambda x: x == "abc") == Try("abc", True)
    assert Try.of(lambda x: 5 / 0, 4).filter(lambda x: x > 1) == Try(ZeroDivisionError(), False)

# Generated at 2022-06-14 03:46:08.585694
# Unit test for method filter of class Try
def test_Try_filter():
    class X(object):
        def __init__(self, value):
            self.value = value

        def __eq__(self, other):
            return isinstance(other, type(self))\
                and self.value == other.value

        def __str__(self):
            return 'X[value={}]'.format(self.value)
    # Case with exception
    value = Try.of(lambda: 1 / 0, None)
    value.filter(lambda x: isinstance(x, int))
    assert value == Try(ZeroDivisionError(), False)
    # Not successfully
    value = Try.of(lambda: X(2), None)
    value = value.filter(lambda x: isinstance(x, list))
    assert value == Try(X(2), False)
    # Successfully

# Generated at 2022-06-14 03:46:12.967745
# Unit test for method filter of class Try
def test_Try_filter():
    f = lambda x: x == 5
    assert Try(1, True).filter(f) == Try(1, False)
    assert Try(5, True).filter(f) == Try(5, True)

# Generated at 2022-06-14 03:46:20.961181
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 1, None) == Try(1, True)
    assert Try.of(lambda: 1 / 0, None) == Try(ZeroDivisionError('division by zero'), False)

    assert Try.of(lambda: 1, None).filter(lambda a: a == 1) == Try(1, True)
    assert Try.of(lambda: 1, None).filter(lambda a: a == 0) == Try(1, False)

    assert Try.of(lambda: 1 / 0, None).filter(lambda a: a == 1) == Try(ZeroDivisionError('division by zero'), False)
    assert Try.of(lambda: 1 / 0, None).filter(lambda a: a == 0) == Try(ZeroDivisionError('division by zero'), False)

# Generated at 2022-06-14 03:46:24.923116
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 1, None).filter(lambda x: x > 0) == Try(1, True)
    assert Try.of(lambda: -1, None).filter(lambda x: x > 0) == Try(-1, False)


# Generated at 2022-06-14 03:46:33.404494
# Unit test for method filter of class Try
def test_Try_filter():

    def filterer(value):
        if value % 2 == 0:
            return True
        return False

    assert Try(1, True).filter(filterer) == Try(1, False), 'Assertion error'
    assert Try(2, True).filter(filterer) == Try(2, True), 'Assertion error'


# Generated at 2022-06-14 03:46:37.925551
# Unit test for method filter of class Try
def test_Try_filter():
    def f1():
        def f2():
            return 3
        return Try.of(f2)
    assert f1().filter(lambda v: v % 2 == 0).is_success == False
    assert f1().filter(lambda v: v % 2 != 0).is_success == True


# Generated at 2022-06-14 03:46:40.580099
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(3, True).filter(lambda x: x > 2) == Try(3, True)
    assert Try(3, True).filter(lambda x: x < 2) == Try(3, False)


# Generated at 2022-06-14 03:46:51.583218
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test for method filter of class Try.
    """
    assert Try.of(lambda: "String", []).filter(lambda v: v == "String") == Try("String", True)
    assert Try.of(lambda e: e, [Exception("Exception")]).filter(lambda v: True) == Try(Exception("Exception"), False)
    assert Try.of(lambda: "String", []).filter(lambda v: v == "value") == Try("String", False)
    assert Try.of(lambda e: e, [Exception("Exception")]).filter(lambda v: False) == Try(Exception("Exception"), False)


# Generated at 2022-06-14 03:46:56.158881
# Unit test for method filter of class Try
def test_Try_filter():
    def filter_function(value):
        return value
    
    assert Try(1, True).filter(filter_function) == Try(1, True)
    assert Try(1, False).filter(filter_function) == Try(1, False)
    assert Try(None, False).filter(filter_function) == Try(None, False)
    assert Try(None, True).filter(filter_function) == Try(None, False)


# Generated at 2022-06-14 03:47:05.372285
# Unit test for method filter of class Try
def test_Try_filter():
    success_value = 1
    success = Try(success_value, True)

    # check identity
    assert success.filter(lambda x: True) == success

    # check empty
    assert not success.filter(lambda x: False)

    # check get
    assert success.filter(lambda x: True).get() == success_value

    # check on_success
    value_to_change = 'a'
    success = Try(value_to_change, True)

    def print_value(value):
        print(value)

    assert success.filter(lambda x: True).on_success(print_value).get() == value_to_change

    # check on_fail
    value_to_change = 'a'
    fail = Try(value_to_change, False)


# Generated at 2022-06-14 03:47:10.775157
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    def is_positive(number):
        return number > 0

    try_result = Try.of(lambda: 5)
    assert try_result.filter(is_positive) == Try(5, True)
    try_result = Try.of(lambda: -5)
    assert try_result.filter(is_positive) == Try(-5, False)


# Generated at 2022-06-14 03:47:13.752924
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: x > 0) == Try(1, True)
    assert Try(1, False).filter(lambda x: x > 0) == Try(1, False)
    assert Try(-1, True).filter(lambda x: x > 0) == Try(-1, False)
    assert Try(-1, False).filter(lambda x: x > 0) == Try(-1, False)


# Generated at 2022-06-14 03:47:16.390069
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: x > 0) == Try(1, True)
    assert Try(1, True).filter(lambda x: x < 0) == Try(1, False)
    assert Try(1, False).filter(lambda x: x < 0) == Try(1, False)
    assert Try(1, False).filter(lambda x: x != 1) == Try(1, False)

# Generated at 2022-06-14 03:47:20.957909
# Unit test for method filter of class Try
def test_Try_filter():
    try_success = Try.of(int, "10")
    assert try_success.filter(lambda v: v > 10) == Try(10, False)
    assert try_success.filter(lambda v: v <= 10) == try_success

    try_fail = Try.of(int, "hello")
    assert try_fail.filter(lambda v: isinstance(v, int)) == Try("hello", False)
    assert try_fail.filter(lambda v: type(v) == str) == try_fail

# Generated at 2022-06-14 03:47:34.703555
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Unit test for method filter of class Try

    :return:
    """
    assert Try.of(lambda: 1).filter(lambda v: type(v) == int) == \
        Try(1, True)
    assert Try.of(lambda: 1).filter(lambda v: type(v) == str) == \
        Try(1, False)
    assert Try.of(lambda: str(1)).filter(lambda v: type(v) == str) == \
        Try(ValueError(), False)

# Generated at 2022-06-14 03:47:40.247417
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: x == 1)\
        == Try(1, True)

    assert Try(1, True).filter(lambda x: x == 2)\
        == Try(1, False)

    assert Try(1, False).filter(lambda x: True)\
        == Try(1, False)

test_Try_filter()

# Generated at 2022-06-14 03:47:51.097722
# Unit test for method filter of class Try
def test_Try_filter():
    def test_filter_with_positive_value(test_value: int) -> bool:
        return test_value >= 0

    def test_filter_with_value_is_two(test_value: int) -> bool:
        return test_value == 2

    assert Try.of(Square().calculate, 5) == Try(25, True)
    assert Try.of(Square().calculate, 5) != Try(25, False)
    assert Try.of(Square().calculate, -3) == Try(OverSquareLimitException(), False)
    assert Try.of(Square().calculate, -3) != Try(OverSquareLimitException(), True)
    test_try = Try.of(Square().calculate, 5).filter(test_filter_with_positive_value)

# Generated at 2022-06-14 03:47:54.307049
# Unit test for method filter of class Try
def test_Try_filter():
    @Try.of
    def f():
        return 100

    assert f.filter(lambda x: x == 100) == Try(100, True)
    assert f.filter(lambda x: x == 200) == Try(100, False)



# Generated at 2022-06-14 03:47:57.371674
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: x + 1 == 2) == Try(1, True)
    assert Try(1, False).filter(lambda x: x + 1 == 2) == Try(1, False)
    assert Try(2, True).filter(lambda x: x + 1 == 2) == Try(2, False)
    assert Try(2, False).filter(lambda x: x + 1 == 2) == Try(2, False)


# Generated at 2022-06-14 03:48:03.525933
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    def add(a, b):
        return a+b

    try_result = Try.of(add, 1, 0)

    try_result = try_result.filter(lambda a: a == 1)
    assert try_result.is_success

    try_result = try_result.filter(lambda a: a == 2)
    assert try_result.is_success is False

    try_result = try_result.filter(lambda a: a/0)
    assert try_result.is_success is False

    def divide(a, b):
        return a/b

    try_result = Try.of(divide, 1, 0)

    try_result = try_result.filter(lambda a: a == 1)
    assert try_result.is_success is False

# Generated at 2022-06-14 03:48:10.327442
# Unit test for method filter of class Try
def test_Try_filter():
    # Given
    success_func = lambda x: x + 1

    # When
    success = Try.of(success_func, 1)
    fail = Try.of(success_func, 'error')

    # Then
    assert success.filter(lambda x: x == 2) == Try(2, True)
    assert fail.filter(lambda x: x == 'error') == Try('error', False)
test_Try_filter()



# Generated at 2022-06-14 03:48:17.881234
# Unit test for method filter of class Try
def test_Try_filter():
    @dataclass
    class Test:
        value: str

    # test for not successfully Try monad
    failure = Try.of(lambda: 1 / 0).filter(lambda v: True)
    assert failure.is_success == False
    assert failure.value is Exception

    # test for successfully Try monad
    success = Try.of(lambda: 1 / 1).filter(lambda v: True)
    assert success.is_success == True
    assert success.value == 1

    # test for filterer is not True
    failure = Try.of(lambda: 1 / 1).filter(lambda v: False)
    assert failure.is_success == False
    assert failure.value == 1

# Generated at 2022-06-14 03:48:26.089676
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    def identity(x):
        return x

    def square(x):
        return x * x

    def even(x):
        return x % 2 == 0

    assert Try.of(identity, 2).map(square).filter(even).get() == Try(4, True).value
    assert Try.of(identity, 3).map(square).filter(even).get() == Try(3, False).value

# Generated at 2022-06-14 03:48:32.648596
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Unit test for method filter of class Try
    """
    assert Try.of(lambda: 1).filter(lambda x: x == 2) == Try(1, False)
    assert Try.of(lambda: 1).filter(lambda x: x == 1) == Try(1, True)
    assert Try.of(lambda: 1).filter(lambda x: True) == Try(1, True)


if __name__ == '__main__':
    test_Try_filter()

# Generated at 2022-06-14 03:48:41.270034
# Unit test for method filter of class Try
def test_Try_filter():
    Try.of(lambda z: z).filter(lambda z: z == 100)
    Try.of(lambda z: z).filter(lambda z: z == 'test')


# Generated at 2022-06-14 03:48:48.823392
# Unit test for method filter of class Try
def test_Try_filter():
    global counter
    counter = 0

    # Try successful
    def get_value_with_exception_counter1():
        global counter
        counter += 1
        return [0, 1, 2, 3, 4]

    print('Test filter for successful Try')
    result = Try.of(get_value_with_exception_counter1) \
        .filter(lambda x: x[0] == 0) \
        .filter(lambda x: x[4] == 4)

    print('Result of filter ', result)
    assert result == Try([0, 1, 2, 3, 4], True)
    assert counter == 1

    # Try not successful
    def get_value_with_exception_counter2():
        global counter
        counter += 1
        raise Exception('Exception')

    print('Test filter for not successful Try')
    result

# Generated at 2022-06-14 03:48:53.521215
# Unit test for method filter of class Try
def test_Try_filter():
    def filter_is_even(value):
        return value % 2 == 0

    assert Try(1, True).filter(filter_is_even) == Try(1, False)
    assert Try(2, True).filter(filter_is_even) == Try(2, True)


# Generated at 2022-06-14 03:48:57.417262
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    """
    Unit test for method filter of class Try.
    """
    assert Try(17, True).filter(lambda v: v % 2 == 0) == Try(17, False)
    assert Try(42, True).filter(lambda v: v % 2 == 0) == Try(42, True)

# Generated at 2022-06-14 03:49:06.271396
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    """
    Test for method filter of class Try
    """
    assert Try.of(lambda x, y: x + y, 1, 2).filter(lambda x: x == 3) == Try(3, True)
    assert Try.of(lambda x, y: x + y, 1, 2).filter(lambda x: x == 4) == Try(3, False)
    assert Try.of(lambda x, y: x / y, 1, 0).filter(lambda x: x == 0) == Try(ZeroDivisionError, False)
    print('Method filter of class Try OK')  # pragma: no cover



# Generated at 2022-06-14 03:49:16.052931
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 1, None) \
        .map(lambda x: x + 1) \
        .filter(lambda x: True) == Try(2, True)

    assert Try.of(lambda: 1, None) \
        .map(lambda x: x + 1) \
        .filter(lambda x: False) == Try(1, False)

    assert Try.of(lambda: 1/0, None) \
        .filter(lambda x: True) == Try(ZeroDivisionError('division by zero'), False)



# Generated at 2022-06-14 03:49:19.335670
# Unit test for method filter of class Try
def test_Try_filter():
    def tfilter(value):
        return value > 0
    ttry = Try(1, True)
    assert ttry.filter(tfilter).get() == 1
    ttry2 = Try(-1, True)
    assert not ttry2.filter(tfilter).is_success


# Generated at 2022-06-14 03:49:23.055693
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 1, ()) == Try(1, True)
    assert Try.of(lambda: 1, ()).filter(lambda x: True) == Try(1, True)
    assert Try.of(lambda: 1, ()).filter(lambda x: False) == Try(1, False)


# Generated at 2022-06-14 03:49:34.913518
# Unit test for method filter of class Try
def test_Try_filter():
    value = 3
    value_when_true = 4
    value_when_false = 5

    # When filter value is even number
    fn_even_number = lambda value: (lambda value: value % 2 == 0)(value)
    when_true = Try.of(lambda x: value_when_true, value).filter(fn_even_number).get()
    when_false = Try.of(lambda x: value_when_false, value).filter(fn_even_number).get()
    assert(when_true == value_when_true)
    assert(when_false == value_when_false)

    # When filter value is odd number
    fn_odd_number = lambda value: (lambda value: value % 2 != 0)(value)

# Generated at 2022-06-14 03:49:41.552316
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 5, None).filter(lambda x: isinstance(x, int))\
        == Try(5, True)
    assert Try.of(lambda: '5', None).filter(lambda x: isinstance(x, int))\
        == Try('5', False)
    assert Try.of(lambda: eval("English"), None)\
        .filter(lambda x: isinstance(x, int)) == Try('English', False)

# Generated at 2022-06-14 03:49:54.278936
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test for method filter of class Try.
    """
    t = Try.of(lambda: 1)
    print('test1: {}'.format(t.filter(lambda x: x == 1) == Try(1, True)))
    print('test2: {}'.format(t.filter(lambda x: x == 2) == Try(1, False)))
    t = Try.of(lambda: 1/0)
    print('test3: {}'.format(t.filter(lambda x: x == 1) == Try(ZeroDivisionError, False)))


# Generated at 2022-06-14 03:49:59.726628
# Unit test for method filter of class Try
def test_Try_filter():
    age = -1
    name = 'gg'
    t = Try.of(lambda: 1 / age)
    t1 = t.filter(lambda x: x > 0)
    assert t1 == Try(-1, False)

    t2 = Try.of(lambda: 1 / age).filter(filterer=lambda x: x > 0)
    assert t2 == Try(-1, False)

    t3 = Try.of(lambda: '' if age < 0 else name).filter(lambda x: x is not None)
    assert t3 == Try('', True)

# Generated at 2022-06-14 03:50:08.997691
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    def filterer(value):
        if value % 2 == 0:
            return True
        return False

    def filterer(value):
        if value % 2 == 0:
            return True
        raise RuntimeError('filterer exception')

    assert Try(10, True).filter(filterer) == Try(10, True)
    assert Try(8, True).filter(filterer) == Try(8, True)
    assert Try(15, True).filter(filterer) == Try(15, False)


# Generated at 2022-06-14 03:50:17.857411
# Unit test for method filter of class Try
def test_Try_filter():
    result = Try.of(int, '100').filter(lambda value: value > 99)
    assert result == Try(100, True)

    result = Try.of(int, '100').filter(lambda value: value < 99)
    assert result == Try(100, False)

    result = Try.of(int, 'hello').filter(lambda value: value > 99)
    assert result == Try(value=ValueError('invalid literal for int() with base 10: \'hello\''), is_success=False)

    result = Try.of(int, 'hello').filter(lambda value: value < 99)
    assert result == Try(value=ValueError('invalid literal for int() with base 10: \'hello\''), is_success=False)

# Generated at 2022-06-14 03:50:28.089048
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(2, True).filter(lambda x: x % 2 == 0) == Try(2, True)
    assert Try(3, True).filter(lambda x: x % 2 == 0) == Try(3, False)
    assert Try(2, False).filter(lambda x: x % 2 == 0) == Try(2, False)
    assert Try(Exception(""), True).filter(lambda x: x % 2 == 0) == Try(Exception(""), False)
    assert Try(Exception(""), False).filter(lambda x: x % 2 == 0) == Try(Exception(""), False)


# Generated at 2022-06-14 03:50:31.355002
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(x):
        return x == 2

    assert Try(1, True).filter(filterer) == Try(1, False)
    assert Try(2, True).filter(filterer) == Try(2, True)

# Generated at 2022-06-14 03:50:36.973165
# Unit test for method filter of class Try
def test_Try_filter():
    """
    >>> test_Try_filter()
    None
    """
    assert Try(1, True).filter(lambda x: x == 1) == Try(1, True)
    assert Try(1, True).filter(lambda x: x != 1) == Try(1, False)



# Generated at 2022-06-14 03:50:43.596821
# Unit test for method filter of class Try
def test_Try_filter():
    def is_positive(x):
        return x > 0

    test_cases = [
        (-1, False),
        (0, False),
        (1, True),
        (2, True),
    ]

    for value, is_positive_value in test_cases:
        assert Try(value, True).filter(is_positive).is_success == is_positive_value

# Generated at 2022-06-14 03:50:51.333297
# Unit test for method filter of class Try
def test_Try_filter():
    # Checks that filter works correctly with error in apply
    assert Try.of(lambda x: 1 // x, 0).filter(lambda _: True) == Try(ArithmeticError, False)

    # Checks that filter works correctly when filter returns True
    assert Try.of(lambda x: 1 // x, 1).filter(lambda _: True) == Try(1 // 1, True)

    # Checks that filter works correctly when filter returns False
    assert Try.of(lambda x: 1 // x, 1).filter(lambda _: False) == Try(1 // 1, False)


# Generated at 2022-06-14 03:50:56.412142
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(5, True).filter(lambda x: x % 2) == Try(5, True)
    assert Try(4, True).filter(lambda x: x % 2) == Try(4, False)
    assert Try(4, False).filter(lambda x: x % 2) == Try(4, False)


# Generated at 2022-06-14 03:51:19.063109
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(42, True).filter(lambda x: x > 0) == Try(42, True)
    assert Try(42, True).filter(lambda x: x < 0) == Try(42, False)
    assert Try(Exception(), False).filter(lambda x: x > 0) == Try(Exception(), False)


# Generated at 2022-06-14 03:51:28.332796
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Method filter of class Try returns copy of monad, when monad is successfully and filterer returns True.
    Othercase returns not successfully monad with previous value.
    """
    def filterer(v):
        return v == 1

    def filterer_fail(v):
        return v == 2

    # successful values
    assert Try(1, True).filter(filterer) == Try(1, True)
    assert Try(1, True).filter(filterer_fail) == Try(1, False)
    assert Try(1, True).filter(lambda x: True) == Try(1, True)
    assert Try(1, True).filter(lambda x: False) == Try(1, False)

    # fail values
    assert Try(1, False).filter(filterer) == Try(1, False)

# Generated at 2022-06-14 03:51:34.355479
# Unit test for method filter of class Try
def test_Try_filter():
    try_ = Try.of(lambda: []).filter(lambda arr: len(arr) == 0)
    assert try_.is_success

    try_ = Try.of(lambda: []).filter(lambda arr: len(arr) == 1)
    assert not try_.is_success
    assert isinstance(try_.value, ValueError)

    try_ = Try.of(lambda: []).filter(lambda arr: len(arr) == 0)
    assert try_.is_success

    try_ = Try.of(lambda: 1 / 0).filter(lambda arr: len(arr) == 1)
    assert not try_.is_success
    assert isinstance(try_.value, ZeroDivisionError)


# Generated at 2022-06-14 03:51:42.606335
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    """
    This function tests filter method of class Try

    :returns: None
    :rtype: None
    """
    # Setup
    value = 5

    # When
    test_result = Try.of(lambda: value).filter(lambda x: x < 10)

    # Then
    assert test_result == Try(value, True)
    assert test_result != Try(value, False)

    # Setup
    value = None

    # When
    test_result = Try.of(lambda: value).filter(lambda x: x < 10)

    # Then
    assert test_result != Try(value, False)

    # Setup
    value = 20

    # When
    test_result = Try.of(lambda: value).filter(lambda x: x < 10)

    # Then
    assert test

# Generated at 2022-06-14 03:51:47.482714
# Unit test for method filter of class Try
def test_Try_filter():
    # arrange
    value = 1
    is_success = True
    expected_Try = Try(value, is_success)

    # act
    actual_Try = Try(value, is_success).filter(lambda value: isinstance(value, int))

    # assert
    assert expected_Try == actual_Try


# Generated at 2022-06-14 03:51:52.968227
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Unit test for method filter of class Try.
    """
    assert Try(1, True).filter(lambda value: value == 1) == Try(1, True)
    assert Try(1, True).filter(lambda value: value != 1) == Try(1, False)
    assert Try(1, False).filter(lambda value: True) == Try(1, False)


# Generated at 2022-06-14 03:51:58.194827
# Unit test for method filter of class Try
def test_Try_filter():
    from src.monad.try_monad import Try
    from src.monad.test_utils import assert_Try_success, assert_Try_failure
    from src.monad.test_utils import lower_than_10

    assert_Try_success(Try.of(lambda: 10).filter(lower_than_10), 10)
    assert_Try_failure(Try.of(lambda: 20).filter(lower_than_10), 20)



# Generated at 2022-06-14 03:52:08.071289
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(5, True).filter(lambda i: i % 2 == 0) == Try(5, False)
    assert Try(6, True).filter(lambda i: i % 2 == 0) == Try(6, True)
    assert Try(5, True).filter(lambda i: i % 2 == 0).get_or_else(None) is None
    assert Try(6, True).filter(lambda i: i % 2 == 0).get_or_else(None) == 6
    assert Try(5, False).filter(lambda i: i % 2 == 0) == Try(5, False)
    assert Try(6, False).filter(lambda i: i % 2 == 0) == Try(6, False)
    assert Try(5, False).filter(lambda i: i % 2 == 0).get_or_else(None) is None
   

# Generated at 2022-06-14 03:52:20.824509
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    # on successful monad
    positive_divider = lambda x: x % 2 == 0
    assert Try(12, True).filter(positive_divider).get() == 12
    assert Try(12, True).filter(positive_divider).is_success

    # on unsuccessful monad
    negative_divider = lambda x: x % 2 == 1
    assert Try(12, True).filter(negative_divider).get() == 12
    assert not Try(12, True).filter(negative_divider).is_success

    assert Try(13, True).filter(positive_divider).get() == 13
    assert not Try(13, True).filter(positive_divider).is_success

    assert Try(13, True).filter(negative_divider).get() == 13
    assert Try(13, True).filter

# Generated at 2022-06-14 03:52:25.242081
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda x: 3, 1).filter(lambda x: x == 3).get_or_else(1) == 3
    assert Try.of(lambda x: 3, 1).filter(lambda x: x != 3).get_or_else(1) == 1


# Generated at 2022-06-14 03:53:13.619031
# Unit test for method filter of class Try
def test_Try_filter():
    # Successful Try...
    try_obj = Try('abc', True)
    # ...apply filter
    try_obj = try_obj.filter(lambda x: True)
    # ...check result
    assert(Try('abc', True) == try_obj)

    # Not successfully Try...
    try_obj = Try('abc', False)
    # ...apply filter
    try_obj = try_obj.filter(lambda x: True)
    # ...check result
    assert(Try('abc', False) == try_obj)

    # Successful Try...
    try_obj = Try('abc', True)
    # ...apply filter
    try_obj = try_obj.filter(lambda x: False)
    # ...check result
    assert(Try('abc', False) == try_obj)


# Generated at 2022-06-14 03:53:21.496141
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 4).filter(lambda x: x > 2) == Try(4, True)
    assert Try.of(lambda: 4).filter(lambda x: x < 0) == Try(4, False)
    assert Try.of(lambda: 4).filter(lambda x: x < 0).get() == 4
    assert Try.of(lambda: 4).filter(lambda x: x < 0).get_or_else(6) == 6


# Generated at 2022-06-14 03:53:25.174112
# Unit test for method filter of class Try
def test_Try_filter():
    """
    #TODO
    """
    assert Try(1, True).filter(lambda x: True) == Try(1, True)
    assert Try(1, True).filter(lambda x: False) == Try(1, False)
    assert Try(1, False).filter(lambda x: True) == Try(1, False)


# Generated at 2022-06-14 03:53:31.230273
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 1, None).filter(lambda v: v == 1) == Try(1, True)
    assert Try.of(lambda: 1, None).filter(lambda v: v == 2) == Try(1, False)
    # Try.of(lambda: 1 / 0, None).filter(lambda v: True) == Try(1, False)

# Generated at 2022-06-14 03:53:32.592745
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value: int) -> bool:
        return value % 2 == 0

    assert Try.of(int, 2).filter(filterer) == Try(2, True)
    assert Try.of(int, 1).filter(filterer) == Try(1, False)

# Generated at 2022-06-14 03:53:40.210673
# Unit test for method filter of class Try
def test_Try_filter():

    def filterer1(x):
        return x > 10

    def filterer2(x):
        return x < 10

    def filterer3(x):
        return x == 0

    assert_that(Try(10, True).filter(filterer1), equal_to(Try(10, False)))
    assert_that(Try(20, True).filter(filterer3), equal_to(Try(20, True)))
    assert_that(Try(10, True).filter(filterer2), equal_to(Try(10, True)))
    assert_that(Try(10, False).filter(filterer2), equal_to(Try(10, False)))



# Generated at 2022-06-14 03:53:47.442835
# Unit test for method filter of class Try
def test_Try_filter():
    def plus_one(x):
        return x + 1

    def is_even(x):
        return x % 2 == 0

    def filterer(x):
        return x > 1

    assert Try.of(plus_one, 1).filter(filterer) == Try(2, True)
    assert Try.of(plus_one, 2).filter(filterer) == Try(3, True)
    assert Try.of(plus_one, 2).filter(is_even) == Try(3, False)


# Generated at 2022-06-14 03:53:52.390739
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: True) == Try(1, True)
    assert Try(1, True).filter(lambda x: False) == Try(1, False)
    assert Try(Exception("Error"), False).filter(lambda x: True) == Try(Exception("Error"), False)


# Generated at 2022-06-14 03:53:56.565481
# Unit test for method filter of class Try
def test_Try_filter():
    try:
        result = Try.of(lambda: 5, ())
        result.filter(lambda x: x == 6)
    except Exception:
        result = Try(None, False)

    assert result == Try(None, False)



# Generated at 2022-06-14 03:54:05.020859
# Unit test for method filter of class Try
def test_Try_filter():
    test_Try_filter.parm = 0

    def raise_exception():
        if test_Try_filter.parm == 0:
            test_Try_filter.parm = 1
            raise Exception
        return True

    def check_True(x):
        return x is True

    result = Try.of(raise_exception)
    result = result.filter(check_True)

    assert result.value is True
    assert result.is_success is True
