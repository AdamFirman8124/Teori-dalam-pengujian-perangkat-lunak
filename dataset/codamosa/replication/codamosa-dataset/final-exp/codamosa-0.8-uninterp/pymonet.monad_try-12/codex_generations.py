

# Generated at 2022-06-14 03:44:40.472896
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test filter method of Try class.
    test_Try_filter :: Try -> Boolean
    """
    assert Try('abc', True).filter(lambda v: 'a' in v).get() == 'abc'
    assert Try('abc', True).filter(lambda v: 'b' in v).is_success is True
    assert Try('abc', True).filter(lambda v: 'd' in v).get() == 'abc'
    assert Try('abc', True).filter(lambda v: 'd' in v).is_success is False
    assert Try('abc', False).filter(lambda v: 'a' in v).is_success is False



# Generated at 2022-06-14 03:44:54.097701
# Unit test for method filter of class Try
def test_Try_filter():
    """
    For given value 5, Try[value=5, is_success=True] should have filter method called.
    Filter function should return True, when passed value is 5.
    So, after calling filter method, new Try should be created with page with value 5
    and successfully status.
    """
    monad = Try(5, True)  # monad of value 5, successfully

    def filterer(value):
        return value == 5

    assert monad.filter(filterer) == Try(5, True)

    # monad of value 5, not successfully
    monad = Try(5, False)

    # filterer returns True if value is 5
    assert monad.filter(filterer) == Try(5, False)

    # some value, successfully
    monad = Try(6, True)

    # filt

# Generated at 2022-06-14 03:44:56.673591
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(str_value):
        return str_value == 'value'

    assert Try('value', True).filter(filterer) == Try('value', True)
    assert Try('value', False).filter(filterer) == Try('value', False)

# Generated at 2022-06-14 03:45:08.835792
# Unit test for method filter of class Try
def test_Try_filter():
    @Try.of
    def div_zero():
        1/0

    @Try.of
    def div_zero_without_exception():
        1

    def filterer(value):
        return value.args[0] == 'division by zero'

    assert div_zero().filter(filterer) == Try(ZeroDivisionError('division by zero'), False)
    assert div_zero_without_exception().filter(filterer) == Try(1, True)

if __name__ == "__main__":  # pragma: no cover
    test_Try_filter()
    print('Successfully')

# Generated at 2022-06-14 03:45:13.842926
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value):
        return value > 42

    try_instance = Try(35, True)
    assert try_instance.filter(filterer).is_success is False

    try_instance = Try(55, True)
    assert try_instance.filter(filterer).is_success



# Generated at 2022-06-14 03:45:21.833486
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(3, True).filter(lambda value: value < 4) == Try(3, True)
    assert Try(3, True).filter(lambda value: value < 2) == Try(3, False)
    assert Try(3, False).filter(lambda value: value < 4) == Try(3, False)
    assert Try(3, False).filter(lambda value: value < 2) == Try(3, False)



# Generated at 2022-06-14 03:45:26.977498
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: x == 1) == Try(1, True)
    assert Try(1, True).filter(lambda x: x == 2) == Try(1, False)
    assert Try(1, False).filter(lambda x: x == 2) == Try(1, False)


# Generated at 2022-06-14 03:45:31.556407
# Unit test for method filter of class Try
def test_Try_filter():
    try_1 = Try.of(lambda: 10 / 0)
    try_2 = Try.of(lambda: 1 / 2)

    assert try_1.filter(lambda x: x > 2) == Try(ZeroDivisionError(), False)
    assert try_2.filter(lambda x: x > 2) == Try(1 / 2, False)



# Generated at 2022-06-14 03:45:40.222935
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    def sum(*args):  # type: (*int) -> int
        if len(args) < 2:
            raise Exception('Too few arguments')
        return reduce((lambda x, y: x + y), args, 0)

    def check_5(num):  # type: (int) -> bool
        return num > 5

    print('Test for filter method for successfully and not successfully Try:')

    print('\tInput: {0}'.format(Try.of(sum, 1, 2, 3, 4)))
    print('\tExpected result is Try[value=10, is_success=False]:')
    print('\tYour result is: {0}'.format(Try.of(sum, 1, 2, 3, 4).filter(check_5)))


# Generated at 2022-06-14 03:45:48.825275
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(5, True).filter(lambda x: x > 4) == Try(5, True)
    assert Try(5, True).filter(lambda x: x > 10) == Try(5, False)
    assert Try([1, 2, 3, 4], True).filter(lambda x: len(x) > 3) == Try([1, 2, 3, 4], True)
    assert Try([1, 2, 3, 4], True).filter(lambda x: len(x) > 10) == Try([1, 2, 3, 4], False)


# Generated at 2022-06-14 03:45:59.047234
# Unit test for method filter of class Try
def test_Try_filter():

    def my_filterer(value):
        return value % 2 == 0

    six_monad = Try.of(lambda: 6)

    assert six_monad.filter(my_filterer) == Try(6, True)
    assert six_monad.filter(lambda x: not my_filterer(x)) == Try(6, False)


# Generated at 2022-06-14 03:46:04.940651
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value): return value % 2 == 0
    assert Try(2, True).filter(filterer) == Try(2, True)
    assert Try(5, True).filter(filterer) == Try(5, False)
    assert Try(Exception('test'), False).filter(filterer) == Try(Exception('test'), False)


# Generated at 2022-06-14 03:46:09.488784
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    def gt_3(x):
        return True if x > 3 else False

    def lt_3(x):
        return True if x < 3 else False

    def eq_3(x):
        return True if x == 3 else False

    assert Try(4, True).filter(gt_3) == Try(4, True)
    assert Try(4, True).filter(lt_3) == Try(4, False)
    assert Try(4, True).filter(eq_3) == Try(4, False)

# Generated at 2022-06-14 03:46:15.797804
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(x: int) -> bool:
        return x < 10

    assert Try(1, True).filter(filterer) == Try(1, True)
    assert Try(11, True).filter(filterer) == Try(11, False)
    assert Try(None, False).filter(filterer) == Try(None, False)
    assert Try([], True).filter(filterer) == Try([], True)


# Generated at 2022-06-14 03:46:22.001523
# Unit test for method filter of class Try
def test_Try_filter():
    assert True == Try(1, True)\
            .filter(lambda value: value > 0)\
            .is_success

    assert False == Try(1, True)\
            .filter(lambda value: value < 0)\
            .is_success
    assert False == Try(-1, True)\
            .filter(lambda value: value > 0)\
            .is_success
    assert False == Try(-1, True)\
            .filter(lambda value: value < 0)\
            .is_success
    assert False == Try(-1, False)\
            .filter(lambda value: value > 0)\
            .is_success



# Generated at 2022-06-14 03:46:25.382984
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Unit test function for Try filter.
    """
    number = Try(1, 1)
    assert number.filter(lambda x: x == 1) == Try(1, 1)
    assert number.filter(lambda x: x == 2) == Try(1, False)


# Generated at 2022-06-14 03:46:27.440482
# Unit test for method filter of class Try
def test_Try_filter():
    fn = lambda x: x + 1
    assert Try.of(fn, 5).filter(lambda x: x > 3) == Try(6, True)
    assert Try.of(fn, 5).filter(lambda x: x > 10) == Try(6, False)


# Generated at 2022-06-14 03:46:32.708658
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try('value', True).filter(lambda value: True).get() == 'value'
    assert Try('value', True).filter(lambda value: False) == Try('value', False)
    assert Try('value', False).filter(lambda value: True) == Try('value', False)
    assert Try('value', False).filter(lambda value: False) == Try('value', False)


# Generated at 2022-06-14 03:46:35.806704
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    def is_even(value: int) -> bool:
        if value % 2 == 0:
            return True
        return False

    # test filter on successfully
    assert Try(2, True).filter(is_even) == Try(2, True)

    # test filter on not successfully
    assert Try(2, False).filter(is_even) == Try(2, False)

    # test filter on not successfully and not even
    assert Try(3, True).filter(is_even) == Try(3, False)

# Generated at 2022-06-14 03:46:41.223194
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: x == 1) == Try(1, True)
    assert Try(1, True).filter(lambda x: x == 2) == Try(1, False)
    assert Try(1, False).filter(lambda x: x == 2) == Try(1, False)

# Generated at 2022-06-14 03:46:56.460507
# Unit test for method filter of class Try
def test_Try_filter():
    a = Try('s', True)
    b = Try(1, True)
    c = Try(None, False)

    a = a.filter(lambda x: x == 's')
    assert a.get() == 's' and a.is_success is True

    b = b.filter(lambda x: x == 1)
    assert b.get() == 1 and b.is_success is True

    c = c.filter(lambda x: x == 1)
    assert c.get() is None and c.is_success is False



# Generated at 2022-06-14 03:47:03.871077
# Unit test for method filter of class Try
def test_Try_filter():
    def fn1(x):
        return x

    def fn2(x):
        return x % 2

    assert Try.of(fn1, '1') == Try('1', True)
    assert Try.of(fn2, 1) == Try(1, True)
    assert Try.of(fn1, 1).filter(fn2) == Try(1, True)
    assert Try.of(fn1, 2).filter(fn2) == Try(2, False)
    assert Try.of(fn1, 2).filter(fn2).get_or_else(3) == 3


# Generated at 2022-06-14 03:47:11.440997
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value):
        return value > 10

    # value is not greater than 10, filter return not successfully Try
    try_1 = Try(7, True).filter(filterer)
    assert try_1.is_success is False
    assert try_1 == Try(7, False)

    # value is greater than 10, filter return successfully Try
    try_2 = Try(12, True).filter(filterer)
    assert try_2.is_success is True
    assert try_2 == Try(12, True)



# Generated at 2022-06-14 03:47:14.910905
# Unit test for method filter of class Try
def test_Try_filter():
    # Positive test
    assert Try(1, True).filter(lambda x: x == 1) == Try(1, True)
    assert not Try(2, True).filter(lambda x: x == 1) == Try(2, True)
    # Negative test
    assert Try(1, False).filter(lambda x: x == 1) == Try(1, False)

# Generated at 2022-06-14 03:47:19.852465
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(5, True).filter(lambda x: x == 5) == Try(5, True)
    assert Try(5, True).filter(lambda x: x != 5) == Try(5, False)
    assert Try(Exception(), False).filter(lambda x: x == 5) == Try(Exception(), False)


# Generated at 2022-06-14 03:47:24.997507
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(2, True).filter(lambda x: x == 2) == Try(2, True)
    assert Try(2, True).filter(lambda x: x == 1) == Try(2, False)
    assert Try(2, False).filter(lambda x: x == 2) == Try(2, False)
    assert Try(2, False).filter(lambda x: x == 1) == Try(2, False)


# Generated at 2022-06-14 03:47:29.273515
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(2, True) \
        .filter(lambda value: value > 1) \
        == Try(2, True)

    assert Try(1, True) \
        .filter(lambda value: value > 1) \
        == Try(1, False)



# Generated at 2022-06-14 03:47:31.769150
# Unit test for method filter of class Try
def test_Try_filter():
    assert (Try.of(int, '111').filter(lambda x: x is not None)
            == Try(111, True))\
        , "Test method filter of class Try"

# Generated at 2022-06-14 03:47:39.456457
# Unit test for method filter of class Try
def test_Try_filter():
    """Unit test for method filter of class Try."""
    def positive_predicate(x: int) -> bool:
        return x > 0

    assert Try(1, True).filter(positive_predicate) == Try(1, True)
    assert Try(-1, True).filter(positive_predicate) == Try(-1, False)
    assert Try(1, False).filter(positive_predicate) == Try(1, False)



# Generated at 2022-06-14 03:47:46.394670
# Unit test for method filter of class Try
def test_Try_filter():
    """ Unit test for method filter of class Try """

    try_value1 = Try.of(lambda x: x + 1, 2)
    assert try_value1 == Try(3, True)

    try_value2 = Try.of(lambda x: x + 1, 2).filter(lambda x: x != 6)
    assert try_value2 == Try(3, True)

    try_value3 = Try.of(lambda x: x + 1, 2).filter(lambda x: x == 6)
    assert try_value3 == Try(3, False)

    try_value4 = Try.of(lambda x: x / 0, 2).filter(lambda x: x == 6)
    assert try_value4 == Try(ZeroDivisionError(), False)



# Generated at 2022-06-14 03:48:12.402024
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    s = Try.of(lambda x: x, 5)
    ss = s.filter(lambda x: x > 10)
    assert ss == Try(5, False)

    s = Try.of(lambda x: x, 5)
    ss = s.filter(lambda x: x < 10)
    assert ss == Try(5, True)

    s = Try(5, False)
    ss = s.filter(lambda x: x < 10)
    assert ss == Try(5, False)


# Generated at 2022-06-14 03:48:23.775125
# Unit test for method filter of class Try
def test_Try_filter():
    def _filterer(x):
        return x == 1

    data = [
        { 'try': Try(1, True), 'expected': Try(1, True) },
        { 'try': Try(1, False), 'expected': Try(1, False) },
        { 'try': Try(2, True), 'expected': Try(2, False) }
    ]

    for test_case in data:
        actual = test_case['try'].filter(_filterer)
        assert actual == test_case['expected'], 'expected: {}, actual: {}'.format(
            test_case['expected'],
            actual
        )

# Generated at 2022-06-14 03:48:27.932867
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test when filterer return True and when filterer return False
    """
    assert Try(1, True).filter(lambda x: x == 1) == Try(1, True)
    assert Try(1, True).filter(lambda x: x != 1) == Try(1, False)

# Generated at 2022-06-14 03:48:32.123347
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(5, True).filter(lambda x: x < 10) == Try(5, True)
    assert Try(5, True).filter(lambda x: x > 10) == Try(5, False)
    assert Try(5, False).filter(lambda x: x < 10) == Try(5, False)



# Generated at 2022-06-14 03:48:36.433561
# Unit test for method filter of class Try
def test_Try_filter():
    @Try.of
    def do_something(a):
        return a + 1

    assert do_something(1).filter(lambda x: x == 2).get() == 2
    assert do_something(1).filter(lambda x: x == 1).get_or_else(None) == None


# Generated at 2022-06-14 03:48:42.416207
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    assert Try.of(lambda a: 5, 2).filter(lambda n: n % 2 == 0) == Try(5, True)
    assert Try.of(lambda a: 5, 2).filter(lambda n: n % 2 != 0) == Try(5, False)

# Generated at 2022-06-14 03:48:42.994929
# Unit test for method filter of class Try
def test_Try_filter():
    actual = Tr

# Generated at 2022-06-14 03:48:47.250049
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer1(value): return value == 1
    def filterer2(value): return value == 2
    assert Try(1, True).filter(filterer1) == Try(1, True)
    assert Try(2, True).filter(filterer1) == Try(2, False)
    assert Try(2, False).filter(filterer1) == Try(2, False)


# Generated at 2022-06-14 03:48:54.144569
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(n):
        return n > 0

    assert Try(5, True).filter(filterer) == Try(5, True)
    assert Try(-5, True).filter(filterer) == Try(-5, False)
    assert Try(5, False).filter(filterer) == Try(5, False)

if __name__ == "__main__":
    test_Try_filter()

# Generated at 2022-06-14 03:49:01.263016
# Unit test for method filter of class Try
def test_Try_filter():
    # arrange
    try_obj = Try.of(lambda x, y: x + y, 1, 2)

    # act
    actual_result_1 = try_obj.filter(lambda x: x % 2 == 0)
    actual_result_2 = try_obj.filter(lambda x: x % 2 == 1)

    # assert
    assert Try(3, False) == actual_result_1
    assert try_obj == actual_result_2


# Generated at 2022-06-14 03:49:43.642235
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(s):
        return True if len(s) > 10 else False

    it = Try.of(lambda: 'abc', 4)
    it = it.filter(filterer)
    assert it.get_or_else('') == 4

    it = Try.of(lambda: 'abc'*5, 4)
    it = it.filter(filterer)
    assert it.get_or_else('') == 'abc'*5
    


# Generated at 2022-06-14 03:49:46.524446
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(17, True).filter(lambda x: x < 18) == Try(17, True)
    assert Try(17, True).filter(lambda x: x > 18) == Try(17, False)
    assert Try(Exception, False).filter(lambda x: x < 18) == Try(Exception, False)



# Generated at 2022-06-14 03:49:49.229949
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Try.filter must work successfully with filterer.
    """
    filterer = lambda val: val
    assert Try.of(lambda: 'some value', None).filter(filterer) == Try('some value', True)
    assert Try.of(lambda: None, None).filter(filterer) == Try(None, False)


# Generated at 2022-06-14 03:49:55.444642
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(x):
        return x % 2 == 0
    assert Try(2, True).filter(filterer) == Try(2, True)
    assert Try(3, True).filter(filterer) == Try(3, False)
    assert Try('hello', False).filter(str) == Try('hello', False)

# Generated at 2022-06-14 03:50:03.042015
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test for method filter of class Try.

    :returns: None
    :rtype: None
    """
    assert Try(1, True).filter(lambda v: v % 2 == 1) == Try(1, True)
    assert Try(2, True).filter(lambda v: v % 2 == 1) == Try(2, False)
    assert Try(1, False).filter(lambda v: v % 2 == 1) == Try(1, False)


# Generated at 2022-06-14 03:50:14.953419
# Unit test for method filter of class Try
def test_Try_filter():
    def get_two():
        return 2
    def div_by_two(value):
        return value / 2
    def div_by_two_safe(value):
        try:
            return value / 2
        except ZeroDivisionError:
            return 0
    def filterer(value):
        return value == 2

    # Not successfully Try, value is ZeroDivisionError, result is not successfully Try
    assert_that(Try.of(div_by_two, 0).filter(filterer), equal_to(Try(ZeroDivisionError(), False)))
    # Not successfully Try, value is ZeroDivisionError, result is not successfully Try because filterer is False
    assert_that(Try.of(div_by_two, 0).filter(lambda x: False), equal_to(Try(ZeroDivisionError(), False)))
    #

# Generated at 2022-06-14 03:50:27.253623
# Unit test for method filter of class Try
def test_Try_filter():
    try_mock = MagicMock(return_value=Try(1, False))

    # Test case when monad is successfully and filterer returns True
    success_try = Try(1, True)
    success_try.filter(lambda x: x == 1) \
        .on_success(lambda x: assertEqual(type(success_try), Success)) \
        .on_fail(lambda x: try_mock)

    # Test case when monad is successfully and filterer returns False
    failure_try = Try(1, True)
    failure_try.filter(lambda x: x == 2) \
        .on_success(lambda x: try_mock) \
        .on_fail(lambda x: assertEqual(type(failure_try), Failure))

    # Test case when monad is not successfully and filt

# Generated at 2022-06-14 03:50:34.393840
# Unit test for method filter of class Try
def test_Try_filter():
    def test_positive(a, b):
        return a == b

    def test_negative(a, b):
        return a != b

    assert Try.of(test_positive, 'a', 'a').filter(test_positive) == Try('a', True)
    assert Try.of(test_positive, 'a', 'a').filter(test_negative) == Try('a', False)

    assert Try.of(test_positive, 'a', 'b').filter(test_positive) == Try('a', False)
    assert Try.of(test_positive, 'a', 'b').filter(test_negative) == Try('a', False)


# Generated at 2022-06-14 03:50:41.962719
# Unit test for method filter of class Try
def test_Try_filter():
    def is_zero(a):
        return a == 0

    def is_str(a):
        return isinstance(a, str)

    assert Try(4, True).filter(is_zero) == Try(4, False)
    assert Try('4', True).filter(is_zero) == Try('4', True)
    assert Try('4', True).filter(is_str) == Try('4', True)


# Generated at 2022-06-14 03:50:48.390869
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(5, True).filter(lambda x: x > 4) == Try(5, True)
    assert Try(5, True).filter(lambda x: x < 4) == Try(5, False)
    assert Try(5, False).filter(lambda x: x > 4) == Try(5, False)


# Generated at 2022-06-14 03:52:18.938082
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 'Hello', ()) \
        .filter(lambda _: True) \
        == Try('Hello', True)

    assert Try.of(lambda: 'Hello', ()) \
        .filter(lambda _: False) \
        == Try('Hello', False)

    assert Try.of(lambda: 'Hello', ()) \
        .filter(lambda _: 1 == 0) \
        == Try('Hello', False)

    assert Try.of(lambda: 1, ()) \
        .filter(lambda _: True) \
        == Try(1, True)

    assert Try.of(lambda: 1, ()) \
        .filter(lambda _: False) \
        == Try(1, False)

    assert Try.of(lambda: 1, ()) \
        .filter(lambda _: 1 == 0) \
        == Try

# Generated at 2022-06-14 03:52:21.237301
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(x):
        return x > 10
    assert Try(None, False).filter(filterer) == Try(None, False)
    assert Try(10, True).filter(filterer) == Try(10, False)
    assert Try(20, True).filter(filterer) == Try(20, True)


# Generated at 2022-06-14 03:52:25.152709
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(2, True).filter(lambda x: x % 2 == 0) == Try(2, True)
    assert Try('number', True).filter(lambda x: x % 2 == 0) == Try('number', False)


# Generated at 2022-06-14 03:52:28.877196
# Unit test for method filter of class Try
def test_Try_filter():
    x = Try.of(lambda x: x, 5)
    assert x.filter(lambda x: x > 6) == Try(5, False)
    assert x.filter(lambda x: x > 3) == Try(5, True)
    assert x.filter(lambda x: x > 5) == Try(5, True)

# Generated at 2022-06-14 03:52:36.934943
# Unit test for method filter of class Try
def test_Try_filter():
    """
    >>> a = Try.of(len, 'abc')
    >>> a
    Try[value=3, is_success=True]

    >>> a.filter(lambda x: x == 3)
    Try[value=3, is_success=True]

    >>> a.filter(lambda x: x < 3)
    Try[value=3, is_success=False]

    >>> b = Try.of(int, 'abc')
    >>> b
    Try[value=<class 'ValueError'>, is_success=False]

    >>> b.filter(lambda x: x == 'abc')
    Try[value=<class 'ValueError'>, is_success=False]
    """
    pass



# Generated at 2022-06-14 03:52:43.462423
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: x == 1) == Try(1, True)
    assert Try(1, True).filter(lambda x: x == 0) == Try(1, False)
    assert Try(ZeroDivisionError, False).filter(lambda x: x.__class__.__name__ == 'ZeroDivisionError')\
        == Try(ZeroDivisionError, False)

# Generated at 2022-06-14 03:52:50.747597
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value):
        return value % 2 != 0

    monad = Try(4, True)
    assert monad.filter(filterer).is_success is False

    monad = Try(3, True)
    assert monad.filter(filterer).is_success is True

    monad = Try(4, True)
    assert monad.filter(filterer).value == 4
    assert monad.filter(filterer).is_success is False

    monad = Try(3, True)
    assert monad.filter(filterer).value == 3
    assert monad.filter(filterer).is_success is True

    monad = Try(4, False)
    assert monad.filter(filterer).value == 4
    assert monad.filter(filterer).is_success

# Generated at 2022-06-14 03:52:57.056909
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda _: True) == Try(1, True)
    assert Try(1, True).filter(lambda _: False) == Try(1, False)
    assert Try(1, False).filter(lambda _: True) == Try(1, False)
    assert Try(1, False).filter(lambda _: False) == Try(1, False)


# Generated at 2022-06-14 03:53:08.662699
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(8, True).filter(lambda value: value % 2 == 0) == Try(8, True), 'Trying to filter correct value'
    assert Try(8, True).filter(lambda value: value % 2 != 0) == Try(8, False), 'Trying to filter incorrect value'
    assert Try(9, True).filter(lambda value: value % 2 == 0) == Try(9, False), 'Trying to filter correct value'
    assert Try(9, True).filter(lambda value: value % 2 != 0) == Try(9, True), 'Trying to filter incorrect value'


# Generated at 2022-06-14 03:53:15.266448
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 1, ).filter(lambda x: x > 0).is_success == True
    assert Try.of(lambda: -1, ).filter(lambda x: x > 0).is_success == False
    assert Try.of(lambda: 1, ).filter(lambda x: x > 0).value == 1
    assert Try.of(lambda: -1, ).filter(lambda x: x > 0).value == -1

