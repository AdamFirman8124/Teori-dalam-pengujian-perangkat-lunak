

# Generated at 2022-06-14 03:44:31.366395
# Unit test for method __eq__ of class Try
def test_Try___eq__():
    # Successful and successful Try
    try_ = Try('test', True)
    eq_(Try('test', True), try_)
    # Successful and not successful Try
    eq_(Try('test', False), try_, msg=None)



# Generated at 2022-06-14 03:44:36.813879
# Unit test for method __eq__ of class Try
def test_Try___eq__():  # pragma: no cover
    try_1 = Try(1, False)
    try_2 = Try(2, True)
    assert try_1 == try_1
    assert not try_1 == try_2



# Generated at 2022-06-14 03:44:44.386450
# Unit test for method __eq__ of class Try
def test_Try___eq__():
    assert Try(4, True) == Try(4, True)
    assert Try(4, False) == Try(4, False)
    assert Try('test', True) == Try('test', True)
    assert Try('test', False) == Try('test', False)
    assert Try(4, True) != Try('test', True)
    assert Try(4, False) != Try('test', False)
    assert Try(4, True) != Try(4, False)
    assert Try(4, False) != Try(4, True)
    assert Try('test', True) != Try('other_test', True)
    assert Try('test', False) != Try('other_test', False)
    assert Try('test', True) != Try('test', False)
    assert Try('test', False) != Try('test', True)

# Unit

# Generated at 2022-06-14 03:44:53.044917
# Unit test for method filter of class Try
def test_Try_filter():
    class TestException(Exception):
        pass

    def throw_exception():
        raise TestException('Test exception')

    equal(Try.of(throw_exception).filter(lambda _: True), Try(TestException('Test exception'), False))
    equal(Try.of(lambda: True).filter(lambda a: a), Try(True, True))
    equal(Try.of(lambda: True).filter(lambda a: not a), Try(True, False))
    equal(Try.of(lambda: False).filter(lambda a: a), Try(False, False))



# Generated at 2022-06-14 03:45:03.212583
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    """
     Test Try.filter method
    """

    print('test_Try_filter')

    def positive(x):
        return x > 0

    def negative(x):
        return x < 0

    # Cases when result of filterer is True
    assert Try.of(lambda: 5).filter(positive) == Try(5, True)
    assert Try.of(lambda: 5).filter(negative) == Try(5, False)
    assert Try.of(lambda: -5).filter(positive) == Try(-5, False)
    assert Try.of(lambda: -5).filter(negative) == Try(-5, True)

    # Cases when argument function raises exception
    assert Try.of(lambda: 5 / 0).filter(positive) == Try(ZeroDivisionError(), False)
    assert Try.of

# Generated at 2022-06-14 03:45:06.217421
# Unit test for method __eq__ of class Try
def test_Try___eq__():
    # expect
    assert Try(1, True) == Try(1, True)
    assert Try(1, False) != Try(1, True)    
    assert Try(1, True) != Try(2, True)
    assert Try(1, False) != Try(2, False)
    assert Try(1, True) != Try(1, False)


# Generated at 2022-06-14 03:45:15.247915
# Unit test for method filter of class Try
def test_Try_filter():
    def test_filter_filterer_returns_True():
        try_value = Try(1, True)
        assert try_value.filter(lambda x: x == 1) == Try(1, True)
    def test_filter_filterer_returns_False():
        try_value = Try(1, True)
        assert try_value.filter(lambda x: x == 2) == Try(1, False)
    def test_filter_not_successfully_filterer_returns_True():
        try_value = Try(1, False)
        assert try_value.filter(lambda x: x == 1) == Try(1, False)
    def test_filter_not_successfully_filterer_returns_False():
        try_value = Try(1, False)

# Generated at 2022-06-14 03:45:25.317860
# Unit test for method __eq__ of class Try
def test_Try___eq__(): # pragma: no cover
    assert Try(10, True) == Try(10, True)
    assert Try(10, False) == Try(10, False)
    assert Try(20, True) == Try(20, True)
    assert Try(20, False) == Try(20, False)
    assert Try(10, True) != Try(20, True)
    assert Try(10, False) != Try(20, False)
    assert Try(10, True) != Try(10, False)
    assert Try(20, False) != Try(20, True)


# Generated at 2022-06-14 03:45:29.218163
# Unit test for method __eq__ of class Try
def test_Try___eq__():
    assert Try('Some', True) == Try('Some', True)
    assert Try('Some', True) != Try('Other', True)
    assert Try(Exception(), False) != Try('Other', True)
    assert Try(Exception(), False) == Try(Exception(), False)

# Generated at 2022-06-14 03:45:31.466441
# Unit test for method __eq__ of class Try
def test_Try___eq__():
    assert (Try(1, True) == Try(1, True))



# Generated at 2022-06-14 03:45:38.842225
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    assert Try(2, True).filter(lambda x: x % 2 == 0) == Try(2, True)
    assert Try(3, True).filter(lambda x: x % 2 == 0) == Try(3, False)


if __name__ == '__main__':
    test_Try_filter()

# Generated at 2022-06-14 03:45:50.720212
# Unit test for method filter of class Try
def test_Try_filter():
    from unittest import TestCase
    from unittest.mock import Mock

    def test_OK(case):
        """
        Method filter allow us to filter monad value when monad is successfully.
        In this test we will check if filter return copy of monad when filterer return True.
        We are testing "something" which is not a Try monad.

        :params case: unittest class
        :type case: TestCase
        """

        # Prepare
        something = Try(True, True)
        filterer = Mock(return_value=True)
        expected = something
        # Execute
        actual = something.filter(filterer)
        # Check
        filterer.assert_called_once_with(True)
        case.assertTrue(actual == expected)


# Generated at 2022-06-14 03:46:02.214047
# Unit test for method filter of class Try
def test_Try_filter():
    t1 = Try(1, True).filter(lambda v: True)
    t2 = Try(1, True).filter(lambda v: False)
    t3 = Try(1, False).filter(lambda v: True)

    assert isinstance(t1, Try)
    assert t1.is_success
    assert t1.value == 1

    assert isinstance(t2, Try)
    assert not t2.is_success
    assert t2.value == 1

    assert isinstance(t3, Try)
    assert not t3.is_success
    assert t3.value == 1

    def t():
        raise Exception

    t4 = Try(t, True).filter(lambda v: True)
    t5 = Try(t, True).filter(lambda v: False)
    t6 = Try(t, False).filter

# Generated at 2022-06-14 03:46:12.505913
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test function for method filter of class Try.

    :retruns: 0 on success, otherwise 1.
    :rtype: Int
    """
    def check_first_is_string():
        """
        Function for unit test.
        """
        return lambda x: isinstance(x[0], str)

    test_true = [('test_string', 1), ('test_string2', 2)]
    test_false = [(1, 'test_string')]


# Generated at 2022-06-14 03:46:14.700738
# Unit test for method filter of class Try
def test_Try_filter():
    try_1 = Try(lambda x: x, True)
    try_2 = Try(lambda x: x, True)
    assert try_1.filter(lambda x: True).get()(lambda x: x) == try_2.filter(lambda x: True).get()(lambda x: x)



# Generated at 2022-06-14 03:46:18.534778
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value):
        return True

    def not_filterer(value):
        return False

    try_ = Try(1, True)

    assert try_.filter(filterer) == Try(1, True)
    assert try_.filter(not_filterer) == Try(1, False)



# Generated at 2022-06-14 03:46:25.563614
# Unit test for method filter of class Try
def test_Try_filter():
    result = Try.of(lambda a: a*a, 2)\
        .filter(lambda a: a != 0)\
        .get_or_else(0)
    assert result == 4

    result = Try.of(lambda a: a*a, 0)\
        .filter(lambda a: a != 0)\
        .get_or_else(0)
    assert result == 0



# Generated at 2022-06-14 03:46:27.890155
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(3, True).filter(lambda x: x % 2 == 0) == Try(3, False)
    assert Try(4, True).filter(lambda x: x % 2 == 0) == Try(4, True)
    assert Try('a', False).filter(lambda x: len(x) == 1) == Try('a', False)


# Generated at 2022-06-14 03:46:33.175915
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(5, True).filter(lambda x: x > 4) == Try(5, True)
    assert Try(4, True).filter(lambda x: x > 4) == Try(4, False)
    assert Try(None, False).filter(lambda x: False) == Try(None, False)
    assert Try(None, False).filter(lambda x: True) == Try(None, False)


# Generated at 2022-06-14 03:46:39.671872
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(int, 'a').filter(lambda x: x > 1) == Try(ValueError('invalid literal for int() with base 10: \'a\''), False)
    assert Try.of(int, '1').filter(lambda x: x > 1) == Try(ValueError('invalid literal for int() with base 10: \'1\''), False)
    assert Try.of(int, '1').filter(lambda x: x == 1) == Try(1, True)



# Generated at 2022-06-14 03:46:51.233651
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: [1,2,3]).filter(lambda xs: len(xs) < 10) == Try.of(lambda: [1,2,3])
    assert Try.of(lambda: [1,2,3]).filter(lambda xs: len(xs) < 3) == Try.of(lambda: [1,2,3])
    assert Try.of(lambda: [1,2,3]).filter(lambda xs: len(xs) > 2) == Try(None, False)

# Generated at 2022-06-14 03:46:56.299096
# Unit test for method filter of class Try
def test_Try_filter():
    print('Test Try filter')
    assert Try(12, True).filter(lambda x: x > 10) == Try(12, True)
    assert Try(12, True).filter(lambda x: x < 10) == Try(12, False)
    assert Try(12, False).filter(lambda x: x < 10) == Try(12, False)
    assert Try('smth wrong', False).filter(lambda x: x > 10) == Try('smth wrong', False)


# Generated at 2022-06-14 03:47:01.468366
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value: int) -> bool:
        return value > 42

    assert Try(43, True).filter(filterer) == Try(43, True)
    assert Try(42, True).filter(filterer) == Try(42, False)
    assert Try(43, False).filter(filterer) == Try(43, False)


# Generated at 2022-06-14 03:47:08.791699
# Unit test for method filter of class Try
def test_Try_filter():
    def add1(value):
        return value + 1

    def filterer1(value):
        return value == 1

    def add2(value):
        return value + 2

    def filterer2(value):
        return value == 3

    assert Try.of(add1, 0).filter(filterer1) == Try(1, True)
    assert Try.of(add1, 0).filter(filterer2) == Try(1, False)
    assert Try.of(add2, 0).filter(filterer2) == Try(3, True)


# Generated at 2022-06-14 03:47:16.346397
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda x: x, True).filter(lambda x: False).is_success is False
    assert Try.of(lambda x: x, True).filter(lambda x: True).is_success is True
    assert Try.of(lambda x: x, False).filter(lambda x: False).is_success is False
    assert Try.of(lambda x: x, False).filter(lambda x: True).is_success is False
    assert Try.of(lambda x, y: 1/x, 1, 0).filter(lambda x: False).is_success is False
    assert Try.of(lambda x, y: 1/x, 1, 0).filter(lambda x: True).is_success is False


# Generated at 2022-06-14 03:47:27.208715
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    from itertools import product
    from random import randint
    from operator import eq

    for _ in range(1000):
        a = randint(-10, 10)
        try_ = Try(a, True)
        test_value = try_.get()
        def plus(v):
            return v + 1

        def less_than(v):
            return v > a
        test_value = plus(test_value)
        try_ = try_.map(plus)
        assert test_value == try_.get()

        test_value = less_than(test_value)
        try_ = try_.bind(lambda x: Try(less_than(x), True))
        assert test_value == try_.get()

        is_success = False
        try_ = try_.filter(eq)
        is_

# Generated at 2022-06-14 03:47:34.888296
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    from random import randrange
    from timeit import timeit

    MAX_VALUE = 100
    NUMBER_OF_TESTS = 20
    asserts = []

    def filter_with_if(x):
        return x > randrange(MAX_VALUE)

    def filter_with_try(x):
        return Try(filter_with_if(x), True)

    for _ in range(NUMBER_OF_TESTS):
        x = randrange(MAX_VALUE)
        asserts.append((x > randrange(MAX_VALUE), filter_with_try(x).is_success))

    assert all(asserts)


# Generated at 2022-06-14 03:47:44.683319
# Unit test for method filter of class Try
def test_Try_filter():
    def positive_values(x):
        return x > 0

    def negative_values(x):
        return x < 0

    assert Try.of(lambda x: 1).filter(positive_values) == Try(1, True)
    assert Try.of(lambda x: 1).filter(negative_values) == Try(1, False)
    assert Try.of(lambda x: 1).filter(lambda _: False) == Try(1, False)
    assert Try.of(lambda x: None).filter(lambda _: False) == Try(None, False)
    assert Try.of(lambda: 1/0).filter(lambda _: False) == Try(ZeroDivisionError, False)


# Generated at 2022-06-14 03:47:49.786158
# Unit test for method filter of class Try
def test_Try_filter():
    # Given
    try_obj = Try(10, True)

    # When
    try_obj_filtered = try_obj.filter(lambda x: x > 10)

    # Then
    assert try_obj_filtered == Try(10, False)


# Generated at 2022-06-14 03:47:53.610625
# Unit test for method filter of class Try
def test_Try_filter():
    def test_filter(x):
        return x > 0

    assert Try(1, True).filter(test_filter) == Try(1, True)
    assert Try(0, True).filter(test_filter) == Try(0, False)


# Generated at 2022-06-14 03:48:10.644935
# Unit test for method filter of class Try
def test_Try_filter():
    data = [
        (Try.of(int, '42'), True),
        (Try.of(int, '42').filter(lambda x: x > 10), True),
        (Try.of(int, '-42').filter(lambda x: x > 10), False),
        (Try.of(int, '123s').filter(lambda x: x > 10), False),
        (Try.of(int, None).filter(lambda x: x > 10), False),
    ]
    for target, expected in data:
        assert target == expected


# Generated at 2022-06-14 03:48:17.114097
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 5, ()).filter(lambda x: x == 5) == Try(5, True)
    assert Try.of(lambda: 5, ()).filter(lambda x: x > 5) == Try(5, False)
    assert Try.of(lambda: 5, ()).filter(lambda x: x < 5) == Try(5, False)
    assert Try.of(lambda: int('s'), ()).filter(lambda x: x == 5) == Try(ValueError('invalid literal for int() with base 10: \'s\''), False)


# Generated at 2022-06-14 03:48:21.560855
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(8, True).filter(lambda x: x > 7) == Try(8, True)
    assert Try(7, True).filter(lambda x: x > 7) == Try(7, False)
    assert Try(7, False).filter(lambda x: x > 7) == Try(7, False)
    assert Try(7, True).filter(lambda x: x > 7).get_or_else(8) == 8
    assert Try(8, True).filter(lambda x: x > 7).get_or_else(8) == 8
    assert Try(7, False).filter(lambda x: x > 7).get_or_else(8) == 7


# Generated at 2022-06-14 03:48:27.604795
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(s):
        return len(s) > 1

    assert Try.of(lambda: 'ab')\
              .filter(filterer)\
              .is_success
    assert Try.of(lambda: 'a')\
              .filter(filterer)\
              .is_success == False
    assert Try.of(lambda: 'a')\
              .filter(filterer)\
              .value == 'a'
    

# Generated at 2022-06-14 03:48:35.879369
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    def filter(value):
        return value > 0

    res = Try.of(lambda x: x + 1, 1).filter(filter)
    assert res.is_success
    assert res.value == 2

    res = Try.of(lambda x: x + 1, 1).filter(filter).bind(lambda x: Success(x + 1))
    assert res.is_success
    assert res.value == 3

    res = Try.of(lambda x: x + 1, 1).filter(lambda x: x < 0)
    assert not res.is_success
    assert res.value == 1

    res = Try.of(lambda x: x + 1, 1).filter(lambda x: x < 0).bind(lambda x: Success(x + 1))
    assert not res.is_success
    assert res.value

# Generated at 2022-06-14 03:48:40.827323
# Unit test for method filter of class Try
def test_Try_filter():
    # Test for monad with value 1 in successfully state and filterer is lambda x: x>=0
    assert Try(1, True).filter(lambda x: x>=0) == Try(1, True)
    # Test for monad with value 1 in successfully state and filterer is lambda x: x<0
    assert Try(1, True).filter(lambda x: x<0) == Try(1, False)
    # Test for monad with value 1 in not successfully state and filterer is lambda x: x>=0
    assert Try(1, False).filter(lambda x: x>=0) == Try(1, False)
    # Test for monad with value 1 in not successfully state and filterer is lambda x: x<0

# Generated at 2022-06-14 03:48:43.142187
# Unit test for method filter of class Try
def test_Try_filter():
    x1 = Try.of(lambda: 1)
    x2 = Try.of(lambda: 1).filter(lambda x: x == 1)
    x3 = Try.of(lambda: 1).filter(lambda x: x != 1)

    assert x1 == x2
    assert x3.is_success == False
    print('test_Try_filter - Ok!')


# Generated at 2022-06-14 03:48:47.521381
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    # GIVEN
    def filterer(value):
        return value > 10

    # WHEN
    actual = (Try.of(lambda x: x, 5).filter(filterer),
              Try.of(lambda x: x, 15).filter(filterer))

    # THEN
    expected = (Try(5, False), Try(15, True))
    assert actual == expected



# Generated at 2022-06-14 03:48:55.099892
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(x):
        return x == 8

    assert Try(5, True).filter(filterer) == Try(5, False)
    assert Try(8, True).filter(filterer) == Try(8, True)
    assert Try(5, False).filter(filterer) == Try(5, False)
    print('test_Try_filter is OK')

if __name__ == "__main__":
    test_Try_filter()

# Generated at 2022-06-14 03:48:57.849171
# Unit test for method filter of class Try
def test_Try_filter():
    assert True == Try(1, True).filter(lambda x: x == 1).is_success
    assert False == Try(1, True).filter(lambda x: x == 2).is_success
    assert False == Try(1, False).filter(lambda x: x == 1).is_success

# Generated at 2022-06-14 03:49:17.628866
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test function filter method of class Try.
    """
    assert Try(1, True).filter(lambda x: x == 1) == Try(1, True)
    assert Try(1, False).filter(lambda x: True) == Try(1, False)
    assert Try(1, True).filter(lambda x: False) == Try(1, False)



# Generated at 2022-06-14 03:49:25.832884
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Unit test for method filter of class Try
    """

    def filterer(x: int) -> None:
        return x > 0

    try_with_positive_int = Try(1, True)
    try_with_negative_int = Try(-1, True)
    try_with_exception = Try(Exception, False)

    assert try_with_positive_int.filter(filterer) == Try(1, True)
    assert try_with_negative_int.filter(filterer) == Try(-1, False)
    assert try_with_exception.filter(filterer) == Try(Exception, False)



# Generated at 2022-06-14 03:49:31.608783
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(x):
        return x > 5

    assert Try(10, True).filter(filterer) == Try(10, True)
    assert Try(10, True).filter(lambda x: x < 5) == Try(10, False)
    assert Try(10, False).filter(filterer) == Try(10, False)


# Generated at 2022-06-14 03:49:40.955828
# Unit test for method filter of class Try
def test_Try_filter():
    # given
    test_try = Try.of(int, '2')

    # when
    result = test_try.filter(lambda num: int(num) > 1)

    # then
    assert type(result) is Try
    assert result.is_success
    assert result.value == 2

    # when (not successfully)
    result = test_try.filter(lambda num: int(num) == 0)

    # then (not successfully)
    assert type(result) is Try
    assert not result.is_success
    assert result.value == 2

test_Try_filter()


# Generated at 2022-06-14 03:49:45.818220
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(
        lambda: 1,
    ).filter(
        lambda x: x == 1
    ) == Try.of(
        lambda: 1,
    )

    assert Try.of(
        lambda: 1,
    ).filter(
        lambda x: x == 0
    ) == Try(
        False, False
    )

    assert Try.of(
        lambda: 1 / 0,
    ).filter(
        lambda x: x == 1
    ) == Try(
        ZeroDivisionError(), False
    )



# Generated at 2022-06-14 03:49:51.819489
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 1, None) == Try(1, True)
    assert Try.of(lambda: '1', None).filter(lambda x: x is not '1') == Try('1', False)
    assert Try.of(lambda: '1', None).filter(lambda x: x is '1') == Try('1', True)
    assert Try.of(lambda: 'a', None).filter(lambda x: x is '1') == Try('a', False)


# Generated at 2022-06-14 03:49:59.379696
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(17, False).filter(lambda x: x > 10) == Try(17, False)
    assert Try(17, False).filter(lambda x: x < 10) == Try(17, False)
    assert Try(17, True).filter(lambda x: x > 10) == Try(17, True)
    assert Try(17, True).filter(lambda x: x < 10) == Try(17, False)
    assert Try(7, True).filter(lambda x: x > 10) == Try(7, False)
    assert Try(7, True).filter(lambda x: x < 10) == Try(7, True)

# Generated at 2022-06-14 03:50:05.880006
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda x: x * x, 2)\
        .filter(lambda x: x % 2 == 0)\
        .get() == 4

    assert Try.of(lambda: 2/0)\
        .filter(lambda x: x % 2 == 0)\
        .get() == 2


# Generated at 2022-06-14 03:50:11.534687
# Unit test for method filter of class Try
def test_Try_filter():
    # Arrange
    is_even = lambda x: x % 2 == 0
    is_odd = lambda x: not is_even(x)
    # Act
    try_even = Try(2, True).filter(is_even)
    try_odd = Try(3, True).filter(is_even)
    try_odd_not_even = Try(3, True).filter(is_odd)
    # Assert
    assert try_even == Try(2, True)
    assert try_odd == Try(3, False)
    assert try_odd_not_even == Try(3, True)

# Generated at 2022-06-14 03:50:19.516459
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test for Try.filter method.

    :returns: True when all tests passed, False when not
    :rtype: Boolean
    """
    def test_1():
        """
        Test for filterer function not return True
        and Try is not unsuccessful.

        :returns: True when test passed, False when not
        :rtype: Boolean
        """
        try_ = Try(10, True)
        try_ = try_.filter(lambda x: x > 5)
        return try_.is_success\
            and try_.get() == 10

    def test_2():
        """
        Test for filterer function return True
        and Try is not unsuccessful.

        :returns: True when test passed, False when not
        :rtype: Boolean
        """
        try_ = Try(10, True)
       

# Generated at 2022-06-14 03:50:54.455200
# Unit test for method filter of class Try
def test_Try_filter():
    # Test predicate
    def is_positive(num):
        return num > 0

    # Successfully Try
    try_ = Try.of(int, '10')
    # when predicate returns true then return successfully Try
    assert try_.filter(is_positive) == Try(int('10'), True)
    # when predicate returns False then return not successfully Try
    assert try_.filter(lambda x: x < 0) == Try(int('10'), False)



# Generated at 2022-06-14 03:50:58.577406
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(9, True).filter(lambda x: x % 2 == 0) == Try(9, False)
    assert Try(10, True).filter(lambda x: x % 2 == 0) == Try(10, True)
    assert Try(10, True).filter(lambda x: x % 2 == 0).is_success == True

# Generated at 2022-06-14 03:51:03.527318
# Unit test for method filter of class Try
def test_Try_filter():
    try_number = Try(10, True)
    assert try_number.filter(lambda number: number > 5) == Try(10, True)
    assert try_number.filter(lambda number: number < 5) == Try(10, False)

    try_number = Try(10, False)
    assert try_number.filter(lambda number: number > 5) == Try(10, False)
    assert try_number.filter(lambda number: number < 5) == Try(10, False)


# Generated at 2022-06-14 03:51:09.077556
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test for method filter of class Try

    :returns: None
    :rtype: None
    """

    # test for successfully and when filterer return True
    def filterer_true():
        return True

    # test for successfully and when filterer return True
    def filterer_false():
        return False

    try_obj = Try(5, True)

    # test for successfully and when filterer return True
    assert try_obj.filter(filterer_true()) == Try(5, True)

    # test for successfully and when filterer return False
    assert try_obj.filter(filterer_false()) == Try(5, False)

    # test for not successfully, when filterer return True, should return copy of not successful

# Generated at 2022-06-14 03:51:13.651437
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: x == 1) == Try(1, True)
    assert Try(1, True).filter(lambda x: x == 2) == Try(1, False)



# Generated at 2022-06-14 03:51:23.467762
# Unit test for method filter of class Try
def test_Try_filter():
    # Successfully monad with value 12
    try_12 = Try(12, True)
    # Successfully monad with value 10
    try_10 = Try(10, True)
    # Not successfully monad
    try_exc = Try(ValueError('bad value'), False)

    # Check when all successfully when filterer function return True
    def filterer_true(value):
        return value == 12

    assert try_12.filter(filterer_true) == Try(12, True)
    assert try_10.filter(filterer_true) == Try(10, False)
    assert try_exc.filter(filterer_true) == Try(ValueError('bad value'), False)


# Generated at 2022-06-14 03:51:30.206620
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test for method filter of class Try.

    :returns: None
    :rtype: NoneType
    """
    def filterer(value):
        return value > 2

    test_obj = Try(3, True)

    expected = Try(3, True)
    actual = test_obj.filter(filterer)

    assert actual == expected


# Generated at 2022-06-14 03:51:36.776772
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    assert Try(1, True).filter(lambda x: x == 1) == Try(1, True)
    assert Try(1, True).filter(lambda x: x == 2) == Try(1, False)
    assert Try(1, False).filter(lambda x: x == 1) == Try(1, False)


# Generated at 2022-06-14 03:51:40.760332
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    def filterer(value):
        return value % 2 == 0

    assert Try.of(int, '2').filter(filterer) ==\
        Try(2, True)

    assert Try.of(int, 'e').filter(filterer) ==\
        Try('e', False)


# Generated at 2022-06-14 03:51:45.325898
# Unit test for method filter of class Try
def test_Try_filter():
    try_test = Try("test", True)
    assert try_test.filter(lambda x: x == "test") == Try("test", True)
    assert try_test.filter(lambda x: x == "test2") == Try("test", False)



# Generated at 2022-06-14 03:52:47.526575
# Unit test for method filter of class Try
def test_Try_filter():
    assert True == Try.of(lambda: 1).filter(lambda x: x == 1).is_success
    assert False == Try.of(lambda: 1).filter(lambda x: x == 2).is_success
    assert False == Try.of(lambda: 1/0).filter(lambda x: x == 2).is_success



# Generated at 2022-06-14 03:52:55.060171
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: x == 1) == Try(1, True)
    assert Try(1, True).filter(lambda x: x == 2) == Try(1, False)
    assert Try(1, False).filter(lambda x: x == 1) == Try(1, False)
    assert Try(1, False).filter(lambda x: x == 2) == Try(1, False)


# Generated at 2022-06-14 03:53:03.770983
# Unit test for method filter of class Try
def test_Try_filter():
    def _raise_exception(x):
        return x / 0

    def _is_even(x):
        return x % 2 == 0

    assert Try.of(_raise_exception, 0).filter(_is_even).get_or_else(0) == 0, 'Unexpected value'
    assert Try.of(_raise_exception, 0).filter(lambda x: x % 2 == 0).get_or_else(0) == 0, 'Unexpected value'
    assert Try.of(_raise_exception, 1).filter(lambda x: x % 2 == 0).get_or_else(0) == 0, 'Unexpected value'


# Generated at 2022-06-14 03:53:07.814070
# Unit test for method filter of class Try
def test_Try_filter():
    func = lambda x: x // 45 == 5
    assert Try(5, True).filter(func).value == 5
    assert not Try(5, True).filter(func).is_success
    assert Try(5, False).filter(func).value == 5
    assert not Try(5, False).filter(func).is_success


# Generated at 2022-06-14 03:53:12.091567
# Unit test for method filter of class Try
def test_Try_filter():

    def test_func(x):
        return x % 2 == 1

    val = 3

    t1 = Try(val, True).filter(test_func)
    t2 = Try(val, False).filter(test_func)

    assert t1 == Try(val, True)
    assert t2 == Try(val, False)

    print('Test for method filter of class Try is pass')



# Generated at 2022-06-14 03:53:23.807596
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(True, True).filter(lambda x: True) == Try(True, True)
    assert Try(True, True).filter(lambda x: False) == Try(True, False)
    assert Try(True, False).filter(lambda x: True) == Try(True, False)
    assert Try(True, False).filter(lambda x: False) == Try(True, False)
    assert Try(False, True).filter(lambda x: True) == Try(False, True)
    assert Try(False, True).filter(lambda x: False) == Try(False, False)
    assert Try(False, False).filter(lambda x: True) == Try(False, False)
    assert Try(False, False).filter(lambda x: False) == Try(False, False)



# Generated at 2022-06-14 03:53:30.836195
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(None, True).filter(lambda x: True) == Try(None, True)
    assert Try(None, True).filter(lambda x: False) == Try(None, False)
    assert Try(None, False).filter(lambda x: True) == Try(None, False)
    assert Try(None, False).filter(lambda x: False) == Try(None, False)


# Generated at 2022-06-14 03:53:36.172149
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(5, True).filter(lambda x: True) == Try(5, True)
    assert Try(5, True).filter(lambda x: False) == Try(5, False)
    assert Try(5, False).filter(lambda x: True) == Try(5, False)
    assert Try(5, False).filter(lambda x: False) == Try(5, False)


# Generated at 2022-06-14 03:53:40.014043
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 1, None).filter(lambda x: x == 1) == Try(1, True)
    assert Try.of(lambda: 2, None).filter(lambda x: x == 1) == Try(2, False)


# Generated at 2022-06-14 03:53:45.379065
# Unit test for method filter of class Try
def test_Try_filter():
    def some_function(x):
        return x == 1

    assert Try.of(lambda: 1).filter(some_function) == Try(1, True)
    assert Try.of(lambda: Exception()).filter(some_function) == Try(Exception(), False)
    assert Try.of(lambda: 0).filter(some_function) == Try(0, False)
