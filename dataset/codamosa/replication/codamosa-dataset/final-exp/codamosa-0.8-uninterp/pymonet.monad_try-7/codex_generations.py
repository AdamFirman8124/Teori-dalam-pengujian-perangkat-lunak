

# Generated at 2022-06-14 03:44:42.518094
# Unit test for method filter of class Try
def test_Try_filter():
    # GIVEN
    value = ['a', 'b', 'c']
    is_success = True

    # WHEN
    try_obj = Try(value, is_success)
    filterer = lambda value: len(value) == 3
    filtered_try = try_obj.filter(filterer)

    # THEN
    assert try_obj == filtered_try

    # GIVEN
    value = ['a', 'b', 'c', 'd']

    # WHEN
    try_obj = Try(value, is_success)
    filtered_try = try_obj.filter(filterer)

    # THEN
    assert not try_obj == filtered_try
    assert not filtered_try.is_success
    assert filtered_try.get() == value



# Generated at 2022-06-14 03:44:46.965144
# Unit test for method filter of class Try
def test_Try_filter():
    # Setup
    t = Try.of(lambda: 1 + 1)
    is_even = lambda x: x % 2 == 0

    # Exercise
    result = t.filter(is_even)

    # Verify
    assert result == Try(2, True)



# Generated at 2022-06-14 03:44:56.253292
# Unit test for method filter of class Try
def test_Try_filter():
    """
    test_Try_filter
    """
    def filter_fn(value):
        return True if value > 0 else False
    test_trys = [
        Try(0, True),
        Try(1, True),
        Try('something', False),
        Try(Exception('test'), False),
        Try(Exception('test'), True),
    ]
    expected_results = [False, True, False, False, False]
    for (test_try, expected_result) in zip(test_trys, expected_results):
        result = test_try.filter(filter_fn)
        assert expected_result == result.is_success
        assert result.value == test_try.value


# Generated at 2022-06-14 03:45:06.148790
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    filterer_called = False
    filterer = lambda x: filterer_called and x % 2 == 0

    # Successfully monad
    assert Try.of(lambda x: x, 1).filter(filterer).is_success == False
    filterer_called = True
    assert Try.of(lambda x: x, 1).filter(filterer).is_success == True

    # Not successfully monad
    assert Try.of(lambda x: 1 / 0, None).filter(filterer).is_success == False



# Generated at 2022-06-14 03:45:12.402924
# Unit test for method filter of class Try
def test_Try_filter():
    def is_even(x: int) -> bool:
        return x % 2 == 0

    x, y = Try.of(lambda: 1, 1), Try.of(lambda: 2, 1)

    x_filtered = x.filter(is_even)
    assert str(x_filtered) == 'Try[value=1, is_success=False]'

    y_filtered = y.filter(is_even)
    assert str(y_filtered) == 'Try[value=2, is_success=True]'

# Generated at 2022-06-14 03:45:17.368559
# Unit test for method filter of class Try
def test_Try_filter():
    # Test case with successful Try
    def filterer(value):
        return True

    assert Try('test_Try_filter', True).filter(filterer) == Try('test_Try_filter', True)

    # Test case with not successful Try
    def filterer(value):
        return True

    assert Try('test_Try_filter', False).filter(filterer) == Try('test_Try_filter', False)

    # Test case with successful Try and filterer that returns False
    def filterer(value):
        return False

    assert Try('test_Try_filter', True).filter(filterer) == Try('test_Try_filter', False)

    # Test case with not successful Try and filterer that returns False
    def filterer(value):
        return False


# Generated at 2022-06-14 03:45:28.799327
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda x: x, 10).filter(lambda x: x == 10) == Try(10, True)
    assert Try.of(lambda x: x, 10).filter(lambda x: x > 10) == Try(10, False)
    assert Try.of(lambda x: x, 10).filter(lambda x: x > 10).filter(lambda x: x > 10) == Try(10, False)
    assert Try.of(lambda x: x, 10).filter(lambda x: x == 10).filter(lambda x: x > 10) == Try(10, False)
    assert Try.of(lambda x: x, 10).filter(lambda x: x == 10).filter(lambda x: x == 10) == Try(10, True)

# Generated at 2022-06-14 03:45:37.708302
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test for filter method.
    """
    assert Try(1, True).filter(lambda i: i > 0) == Try(1, True)
    assert Try(1, True).filter(lambda i: i < 0) == Try(1, False)
    assert Try(-1, True).filter(lambda i: i < 0) == Try(-1, False)
    assert Try(-1, False).filter(lambda i: i < 0) == Try(-1, False)



# Generated at 2022-06-14 03:45:44.165052
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(5, True).filter(lambda x: x == 5) == Try(5, True)
    assert Try(5, False).filter(lambda x: x == 5) == Try(5, False)
    assert Try(5, False).filter(lambda x: x == 5) == Try(5, False)



# Generated at 2022-06-14 03:45:49.427972
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(5, True).filter(lambda x: x > 0) == Try(5, True)
    assert Try(0, True).filter(lambda x: x > 0) == Try(0, False)
    assert Try('a', True).filter(lambda x: x > 0) == Try('a', False)


# Generated at 2022-06-14 03:45:56.220769
# Unit test for method filter of class Try
def test_Try_filter():
    def even(value):
        return value % 2 == 0

    assert Try(1, True).filter(even) == Try(1, False)
    assert Try(2, True).filter(even) == Try(2, True)


# Generated at 2022-06-14 03:46:02.064678
# Unit test for method filter of class Try
def test_Try_filter():
    try1 = Try.of(int, '42').filter(lambda x: x != 42)
    assert try1.get_or_else(None) is None
    assert try1.is_success is False

    try2 = Try.of(int, '42').filter(lambda x: x == 42)
    assert try2.get_or_else(None) is 42
    assert try2.is_success is True



# Generated at 2022-06-14 03:46:06.106369
# Unit test for method filter of class Try
def test_Try_filter():
    # Arrange
    value: Try = Try.of(lambda: 100 / 20, 0)
    # Act
    filtered: Try = value.filter(lambda x: x > 2)
    # Assert
    assert filtered == Try(5, True)

# Generated at 2022-06-14 03:46:14.873596
# Unit test for method filter of class Try

# Generated at 2022-06-14 03:46:22.899023
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Unit test for method filter of class Try

    :return: None
    """
    f = Try.of(lambda: 2 / 0)
    assert f.filter(lambda _: True) == Try(ZeroDivisionError(), False)
    assert f.filter(lambda _: False) == Try(ZeroDivisionError(), False)
    f = Try.of(lambda: 1).filter(lambda x: x % 2 == 0)
    assert f == Try(1, False)
    f = Try.of(lambda: 2).filter(lambda x: x % 2 == 0)
    assert f == Try(2, True)
    f = Try.of(lambda: 3 / 0).filter(lambda _: True)
    assert f == Try(ZeroDivisionError(), False)

# Generated at 2022-06-14 03:46:27.344188
# Unit test for method filter of class Try
def test_Try_filter():
    assert_that(Try.of(lambda: 1).filter(lambda n: n == 1),
                equal_to(Try(1, True)))
    assert_that(Try.of(lambda: 1).filter(lambda n: n != 1),
                equal_to(Try(1, False)))

    assert_that(Try.of(lambda: 1/0).filter(lambda n: n == 1),
                equal_to(Try(ZeroDivisionError(), False)))
    assert_that(Try.of(lambda: 1/0).filter(lambda n: n != 1),
                equal_to(Try(ZeroDivisionError(), False)))


# Generated at 2022-06-14 03:46:34.936483
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: "ok_value").filter(lambda value: isinstance(value, str)) == Try("ok_value", True)
    assert Try.of(lambda: "ok_value").filter(lambda value: isinstance(value, int)) == Try("ok_value", False)
    assert Try.of(lambda: "ok_value").filter(lambda value: isinstance(value, str)).get() == "ok_value"
    assert Try.of(lambda: "ok_value").filter(lambda _: False).get() is None


# Generated at 2022-06-14 03:46:48.726756
# Unit test for method filter of class Try
def test_Try_filter():

    def filterer(x):
        return x > 0

    try1 = Try(1, True)
    try2 = Try(-1, True)
    try3 = Try(1, False)

    assert filterer(1)
    assert not filterer(-1)

    assert try1.filter(filterer) == Try(1, True)
    assert try2.filter(filterer) == Try(-1, False)
    assert try3.filter(filterer) == Try(1, False)

    try1 = Try(1, True)
    try2 = Try(-1, True)
    try3 = Try(1, False)

    assert try1.filter(lambda x: x > 0) == Try(1, True)

# Generated at 2022-06-14 03:46:54.997230
# Unit test for method filter of class Try
def test_Try_filter():
    assert isinstance(Try.of(lambda :'Success').filter(lambda arg: arg == 'Success'), Try)
    assert isinstance(Try.of(lambda :2).filter(lambda arg: arg == 'Success'), Try)
    assert isinstance(Try.of(lambda :'Success').filter(lambda arg: arg == 2), Try)
    assert isinstance(Try.of(lambda :2).filter(lambda arg: arg == 2), Try)


# Generated at 2022-06-14 03:47:02.185812
# Unit test for method filter of class Try
def test_Try_filter():
    mocked_filterer = mock.MagicMock(return_value=True)

    assert Try(mock.DEFAULT, True).filter(mocked_filterer) is Try(mock.DEFAULT, True)
    mocked_filterer.assert_called_once_with(mock.DEFAULT)
    mocked_filterer.reset_mock()

    assert Try(mock.DEFAULT, False).filter(mocked_filterer) is Try(mock.DEFAULT, False)
    mocked_filterer.assert_not_called()

# Generated at 2022-06-14 03:47:09.547440
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(5, True).filter(lambda x: x > 0) == Try(5, True)
    assert Try(7, True).filter(lambda x: x > 8) == Try(7, False)
    assert Try(7, False).filter(lambda x: x > 0) == Try(7, False)


# Generated at 2022-06-14 03:47:17.988531
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Unit test for method filter of class Try

    :return:
    """
    assert Try.of(lambda x: x, 1).filter(lambda x: x == 1) == Try(1, True)
    assert Try.of(lambda x: x, 1).filter(lambda x: x == 2) == Try(1, False)
    assert Try.of(lambda x: 1 / 0, 0).filter(lambda x: x == 2) == Try(ZeroDivisionError(), False)



# Generated at 2022-06-14 03:47:22.340576
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: x % 2 == 1) == Try(1, True)
    assert Try(2, True).filter(lambda x: x % 2 == 1) == Try(2, False)
    assert Try(1, False).filter(lambda x: x % 2 == 1) == Try(1, False)

# Generated at 2022-06-14 03:47:27.677037
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: x == 2) == Try(1, False)
    assert Try(2, True).filter(lambda x: x == 2) == Try(2, True)
    assert Try(1, False).filter(lambda x: True) == Try(1, False)


# Generated at 2022-06-14 03:47:36.892873
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Run python tests.
    """
    try:
        assert Try(1, True)\
            .filter(lambda x: x == 1)\
            == Try(1, True)
    except AssertionError:
        print("Test fail: given " + str(Try(1, True).filter(lambda x: x == 1)) + " expected " + str(Try(1, True)))
        return False

    try:
        assert Try(1, True)\
            .filter(lambda x: x != 1)\
            == Try(1, False)
    except AssertionError:
        print("Test fail: given " + str(Try(1, True).filter(lambda x: x != 1)) + " expected " + str(Try(1, False)))
        return False


# Generated at 2022-06-14 03:47:47.320056
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(True, True).filter(lambda x: True) == Try(True, True)
    assert Try(True, True).filter(lambda x: False) == Try(True, False)
    assert Try(False, True).filter(lambda x: True) == Try(False, False)
    assert Try(False, True).filter(lambda x: False) == Try(False, False)
    assert Try(None, False).filter(lambda x: True) == Try(None, False)
    assert Try(None, False).filter(lambda x: False) == Try(None, False)
    assert Try(Exception(), False).filter(lambda x: True) == Try(Exception(), False)
    assert Try(Exception(), False).filter(lambda x: False) == Try(Exception(), False)



# Generated at 2022-06-14 03:47:54.464981
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    # pylint: disable=no-member
    assert Try.of(lambda: 1).filter(lambda x: x != 1) == Try(1, False)
    assert Try.of(lambda: 123).filter(lambda x: x != 1) == Try(123, True)
    assert Try.of(lambda: 1 / 0).filter(lambda x: x != 1) == Try(1, False)
    assert Try.of(lambda: 1).filter(lambda x: x == 1) == Try(1, True)



# Generated at 2022-06-14 03:48:06.428362
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Unit test for method filter of class Try

    :returns: void
    :rtype: void
    """
    # when monad is successfully and filterer returns True
    assert Try(5, True).filter(lambda x: x < 10) == Try(5, True)
    # when monad is not successfully and filterer returns False
    assert Try(5, False).filter(lambda x: x < 10) == Try(5, False)
    # when monad is successfully and filterer returns False
    assert Try(5, True).filter(lambda x: x > 10) == Try(5, False)
    # when monad is not successfully and filterer returns True
    assert Try(5, False).filter(lambda x: x > 10) == Try(5, False)


# Generated at 2022-06-14 03:48:16.446856
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(2, True).filter(lambda value: value % 2 == 0) == Try(2, True)
    assert Try(2, True).filter(lambda value: value % 2 != 0) == Try(2, False)
    assert Try(2, False).filter(lambda value: value % 2 == 0) == Try(2, False)
    assert Try(2, False).filter(lambda value: value % 2 != 0) == Try(2, False)
    assert Try(2, True).filter(lambda value: True) == Try(2, True)
    assert Try(2, True).filter(lambda value: False) == Try(2, False)
    assert Try(2, False).filter(lambda value: True) == Try(2, False)
    assert Try(2, False).filter(lambda value: False) == Try(2, False)

# Generated at 2022-06-14 03:48:28.027862
# Unit test for method filter of class Try
def test_Try_filter():
    # Positive test
    assert Try(1, True).filter(lambda x: x == 1) == Try(1, True)
    assert Try(1, True) == Try(1, True).filter(lambda x: x == 1)

    # Negative test
    assert Try(1, False) == Try(1, False).filter(lambda x: x == 1)
    assert Try(1, True) != Try(1, False).filter(lambda x: x == 1)
    assert Try(1, False) != Try(1, True).filter(lambda x: x == 1)
    assert Try(1, True).filter(lambda x: x != 1) == Try(1, False)
    assert Try(1, True) != Try(1, True).filter(lambda x: x != 1)

# Generated at 2022-06-14 03:48:37.914117
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    assert Try.of(lambda x: x, 1).filter(lambda x: x == 1) == Try(1, True)
    assert Try.of(lambda x: x, 1).filter(lambda x: x != 1) == Try(1, False)
    assert Try.of(lambda x: x / 0, 1).filter(lambda x: x != 1) == Try(1, False)



# Generated at 2022-06-14 03:48:46.615309
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test for filter method of class Try.
    """

    @pytest.mark.parametrize('filterer, value, is_success, is_equal', [
        (lambda x: True, 1, True, True),
        (lambda x: True, 1, False, False),
        (lambda x: False, 1, True, False),
        (lambda x: False, 1, False, False),
    ])
    def test_filter(filterer, value, is_success, is_equal):
        assert Try.filter(Try(value, is_success), filterer) == Try(value, is_equal)



# Generated at 2022-06-14 03:48:57.917116
# Unit test for method filter of class Try
def test_Try_filter():
    import pytest
    Try = Try
    assert Try(2, True).filter(lambda x: 2 < x) == Try(2, False)
    assert Try(2, True).filter(lambda x: x > 2) == Try(2, False)
    assert Try(2, True).filter(lambda x: 1 < x < 3) == Try(2, True)
    assert Try(2, True).filter(lambda x: 1 < x < 1.5) == Try(2, False)
    assert Try(2, False).filter(lambda x: 1 < x < 3) == Try(2, False)
    assert Try(2, False).filter(lambda x: 1 < x < 1.5) == Try(2, False)
    assert Try(2, True).filter(lambda x: False) == Try(2, False)

# Unit test

# Generated at 2022-06-14 03:49:02.622645
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 25) == Try(25, True)
    assert Try.of(lambda: 25).filter(lambda d: True) == Try(25, True)
    assert Try.of(lambda: 25).filter(lambda d: False) == Try(25, False)

# Generated at 2022-06-14 03:49:11.252070
# Unit test for method filter of class Try
def test_Try_filter():
    # Given
    try_str = Try.of(str, '1')
    try_str_fail = Try.of(str, 1)

    # When
    filtered_result = try_str.filter(lambda value: isinstance(value, str))
    filtered_result_fail = try_str_fail.filter(lambda value: isinstance(value, str))

    # Then
    assert filtered_result.is_success, 'Expected filtered result to be successful'
    assert filtered_result == try_str, 'Expected filtered result to be the same'
    assert not filtered_result_fail.is_success, 'Expected filtered fail result to be not successful'
    assert filtered_result_fail.value == TypeError("'int' object is not iterable"), 'Expected filtered result to be the same'


# Generated at 2022-06-14 03:49:19.221612
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(v):
        return v > 10

    def filterer_raise_exception(v):
        raise Exception()

    assert Try(10, True).filter(filterer) == Try(10, False)
    assert Try(11, True).filter(filterer) == Try(11, True)
    assert Try(11, True).filter(filterer_raise_exception) == Try(11, False)
    assert Try(1, False).filter(filterer) == Try(1, False)
    assert Try(1, False).filter(filterer_raise_exception) == Try(1, False)


# Generated at 2022-06-14 03:49:28.164848
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    result = Try(2, True).filter(lambda x: x < 10)
    assert result == Try(2, True)
    result = Try(2, True).filter(lambda x: x > 10)
    assert result == Try(2, False)
    result = Try(2, False).filter(lambda x: x < 10)
    assert result == Try(2, False)
    result = Try(2, False).filter(lambda x: x > 10)
    assert result == Try(2, False)
    result = Try(2, True).filter(lambda x: x < 10).filter(lambda x: x > 0)
    assert result == Try(2, True)
    result = Try(2, True).filter(lambda x: x < 0)
    assert result == Try(2, False)

# Unit

# Generated at 2022-06-14 03:49:34.021190
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value):
        return value % 2 == 0

    assert Try(2, True).filter(filterer) == Try(2, True)
    assert Try(3, True).filter(filterer) == Try(3, False)
    assert Try(2, False).filter(filterer) == Try(2, False)



# Generated at 2022-06-14 03:49:43.996121
# Unit test for method filter of class Try
def test_Try_filter():
    def square(value):
        return value * value

    def even(value):
        return value % 2 == 0

    method_failed = False

    try:
        result = Try.of(square, 2).filter(even).get()
        if result != 4:
            method_failed = True
    except Exception:
        method_failed = True

    try:
        result = Try.of(square, -2).filter(even).get()
        if result != 4:
            method_failed = True
    except Exception:
        method_failed = True

    try:
        result = Try.of(square, 3).filter(even).get()
        if result != 4:
            method_failed = True
    except Exception:
        method_failed = True

    assert not method_failed

# Generated at 2022-06-14 03:49:46.813250
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 1, ).filter(lambda x: x == 1) == Try(1, True)
    assert Try.of(lambda: 1, ).filter(lambda x: x == 2) == Try(1, False)

    assert Try(1, False).filter(lambda x: x == 1) == Try(1, False)


# Generated at 2022-06-14 03:50:04.334301
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda a: a, 1).filter(lambda a: a < 2).is_success
    assert not Try.of(lambda a: a, 1).filter(lambda a: a < 0).is_success
    assert not Try.of(lambda a: a, Exception('exception')).filter(lambda a: a < 0).is_success


# Generated at 2022-06-14 03:50:15.777125
# Unit test for method filter of class Try

# Generated at 2022-06-14 03:50:26.263856
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Unit test for method filter of class Try.

    """
    tr = Try.of(lambda: 1)
    tr_ = tr.filter(lambda x: x == 1)
    assert tr_ == Try(1, True)
    tr__ = tr.filter(lambda x: x == 2)
    assert tr__ == Try(1, False)
    tr___ = Try.of(lambda: 1/0)
    assert tr___ == Try(ZeroDivisionError('division by zero'), False)
    tr____ = tr___.filter(lambda x: x == 1)
    assert tr____ == Try(ZeroDivisionError('division by zero'), False)


# Generated at 2022-06-14 03:50:35.074958
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(i: int) -> bool:
        return i > 10

    # Call filterer on value which was created by successful Try
    try_obj = Try.of(int, '1')
    try_obj_copy = try_obj.filter(filterer)
    assert not try_obj_copy.is_success

    # Call filterer on value which was created by unsuccessful Try
    try_obj = Try.of(int, 'a')
    try_obj_copy = try_obj.filter(filterer)
    assert not try_obj_copy.is_success

    # Call filterer on value which was created by successful Try and is match filterer function
    try_obj = Try.of(int, '20')
    try_obj_copy = try_obj.filter(filterer)

# Generated at 2022-06-14 03:50:39.899281
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(x):
        return x % 2 == 0

    try_even = Try(2, True)
    assert try_even.filter(filterer) == Try(2, True)
    try_odd = Try(3, True)
    assert try_odd.filter(filterer) == Try(3, False)


# Generated at 2022-06-14 03:50:46.810798
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value):
        return value == 'test value'
    assert Try('test value', True).filter(filterer) == Try('test value', True)
    assert Try('test value', True).filter(lambda _: False) == Try('test value', False)
    assert Try('test value', False).filter(lambda _: True) == Try('test value', False)
test_Try_filter()


# Generated at 2022-06-14 03:50:58.734579
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(10, True).filter(lambda x: (x % 2) == 0) == Try(10, False)
    assert Try(11, True).filter(lambda x: (x % 2) == 0) == Try(11, True)
    assert Try(10, False).filter(lambda x: (x % 2) == 0) == Try(10, False)

t11 = Try(10, True)
print(t11)
t12 = Try.of(lambda x: x + 10, 10)
print(t12)
t13 = Try.of(lambda x: x + 10, '10')
print(t13)
t14 = t13.map(lambda x: x + 10)
print(t14)
t15 = t11.bind(lambda x: Try.of(lambda x: x + 10, x))
print

# Generated at 2022-06-14 03:51:02.003026
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    a = Try(2, True)
    b = Try(1, False)
    assert a.filter(lambda x: x > 1) == Try(2, True)
    assert b.filter(lambda x: x > 1) == Try(1, False)

# Generated at 2022-06-14 03:51:07.494185
# Unit test for method filter of class Try
def test_Try_filter():
    # ===== Setup =====
    # Define filterer function
    def filterer(value):
        return value == 'try_success_value'

    # ===== Run =====
    # Create successfully Try
    try_success: Try = Try('try_success_value', True)
    # Create not successfully Try
    try_fail: Try = Try('try_fail_value', False)

    # ===== Assert =====
    assert try_success.filter(filterer) == Try('try_success_value', True)
    assert try_success.filter(lambda v: v == 'try_fail_value') == Try('try_success_value', False)
    assert try_fail.filter(filterer) == Try('try_fail_value', False)

# Generated at 2022-06-14 03:51:19.253765
# Unit test for method filter of class Try
def test_Try_filter():
    # TODO: Плохо что тут постоянно лезет в внутренности типов. Как решить эту проблему?
    assert Try(10, True).filter(lambda x: x < 10) == Try(10, False), 'Функция должна вернуть Try[10, False]'

# Generated at 2022-06-14 03:51:42.713664
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda x: x+1, 2).filter(lambda x: x > 1) == Try(3, True)
    assert Try.of(lambda x: 1/x, 2).filter(lambda x: x > 1) == Try(ZeroDivisionError(None, None, None), False)

# Generated at 2022-06-14 03:51:53.961680
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Method filter of class Try

    :returns: True when all test passed
    :rtype: Boolean
    """
    is_test_passed = True

    # Test filter when monad has value in success state
    def filter_callback(value):
        return True

    try_state = Try(10, True)
    try_state = try_state.filter(filter_callback)
    is_test_passed = is_test_passed and try_state.is_success and try_state.get() == 10

    # Test filter when monad has value in failure state
    try_state = Try(10, False)
    try_state = try_state.filter(filter_callback)

# Generated at 2022-06-14 03:51:57.477532
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    import random

    array = [random.randint(0, 10) for _ in range(10)]

    t = Try.of(lambda a: a, array)
    m = t.filter(lambda a: 4 in a)

    assert m == Try(array, True)


# Generated at 2022-06-14 03:52:02.248792
# Unit test for method filter of class Try
def test_Try_filter():
    t = Try.of(lambda: 10, 1)
    assert(t.filter(lambda r: r == 10).is_success)
    assert(not t.filter(lambda r: r == 1).is_success)
    assert(t.filter(lambda r: r == 10).get() == 10)


# Generated at 2022-06-14 03:52:07.182591
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test behavior on method filter.
    """
    assert Try(1, True).filter(lambda x: x < 2) == Try(1, True)
    assert Try(ValueError('x'), False).filter(lambda x: x < 2) == Try(ValueError('x'), False)
    assert Try(1, True).filter(lambda x: x > 2) == Try(1, False)



# Generated at 2022-06-14 03:52:16.644860
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Unit test for method filter of class Try.
    """
    assert Try.of(lambda: 1, ).filter(lambda x: x > 0) == Try.of(lambda: 1, ).filter(lambda x: x < 0)
    assert Try.of(lambda: 1, ).map(lambda x: x + 1)\
        .filter(lambda x: x == 2).get() == 2
    assert Try.of(lambda: 1, ).map(lambda x: x + 1)\
        .filter(lambda x: x < 2).get() is None


# Generated at 2022-06-14 03:52:21.721006
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value):
        if value != 3:
            return True
        return False

    assert Try(9, True).filter(filterer) == Try(9, True)
    assert Try(3, True).filter(filterer) == Try(3, False)
    assert Try(Exception(), False).filter(filterer) == Try(Exception(), False)


# Generated at 2022-06-14 03:52:23.772735
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try('Hello Try', True).filter(lambda x: True) == Try('Hello Try', True)



# Generated at 2022-06-14 03:52:27.014559
# Unit test for method filter of class Try
def test_Try_filter():
    try_str = Try(1, True)
    assert try_str.filter(lambda x: False) == Try(1, False)
    assert try_str.filter(lambda x: True) == try_str


# Generated at 2022-06-14 03:52:31.539072
# Unit test for method filter of class Try
def test_Try_filter():
    def filter_ten(v):
        return v == 10

    ten = Try(10, True)
    fifeteen = Try(15, True)
    err = Try(Exception('Error exception'), False)

    assert ten.filter(filter_ten) == Try(10, True)
    assert fifeteen.filter(filter_ten) == Try(15, False)
    assert err.filter(filter_ten) == Try(Exception('Error exception'), False)



# Generated at 2022-06-14 03:53:18.803439
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(0, False).filter(lambda x: True) == Try(0, False)
    assert Try(0, True).filter(lambda x: True) == Try(0, True)
    assert Try(0, True).filter(lambda x: False) == Try(0, False)


# Generated at 2022-06-14 03:53:26.502222
# Unit test for method filter of class Try
def test_Try_filter():
    def should_be_true(val):
        return val

    try_int_success = Try(1, True)
    assert try_int_success.filter(should_be_true) == Try(1, True)

    try_int_fail = Try(2, False)
    assert try_int_fail.filter(should_be_true) == Try(2, False)

    exception = Exception('test')
    try_exception = Try(exception, True)
    try_filtered = try_exception.filter(should_be_true)
    assert try_filtered == Try(exception, False)
    assert try_filtered.value == exception


# Generated at 2022-06-14 03:53:29.990165
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 42).filter(lambda x: x == 42) == Try(42, True)
    assert Try.of(lambda: 1 / 0).filter(lambda x: x == 42) == Try(ZeroDivisionError('division by zero'), False)
    assert Try.of(lambda: 1 / 0).filter(lambda x: x == 42).filter(lambda x: x == 42) == Try(ZeroDivisionError('division by zero'), False)


# Generated at 2022-06-14 03:53:36.172542
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    a = Try.of(lambda x, y: x / y, 1, 0)
    b = a.filter(lambda value: isinstance(value, ZeroDivisionError))
    c = a.filter(lambda value: isinstance(value, int))

    assert b.is_success is True
    assert b.value == ZeroDivisionError()
    assert c.is_success is False
    assert c.value == ZeroDivisionError()

# Generated at 2022-06-14 03:53:43.606377
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test the filter method of Try
    """
    # Test with a success Try
    t = Try.of(lambda: 2 + 3)
    t = t.filter(lambda x: x != 5)
    assert t.value == 5
    assert t.is_success

    # Test with a Failure Try
    t = Try.of(lambda: 1 / 0)
    t = t.filter(lambda x: x != 5)
    assert t.value is not None
    assert not t.is_success

    # Test with a success Try
    t = Try.of(lambda: 2 + 3)
    t = t.filter(lambda x: x != 5)
    assert t.value == 5
    assert t.is_success


# Generated at 2022-06-14 03:53:55.148716
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 1, ())\
        .filter(lambda x: x % 2 == 0)\
        .get_or_else(0) == 0
    assert Try.of(lambda: 2, ())\
        .filter(lambda x: x % 2 == 0)\
        .get_or_else(0) == 2
    assert Try.of(lambda: 1, ())\
        .filter(lambda x: x % 2 == 0)\
        .filter(lambda x: x == 0)\
        .get_or_else(0) == 0
    assert Try.of(lambda: 1, ())\
        .filter(lambda x: x % 2 == 0)\
        .filter(lambda x: x == 1)\
        .get_or_else(0) == 0



# Generated at 2022-06-14 03:54:02.121268
# Unit test for method filter of class Try
def test_Try_filter():
    x = Try.of(lambda x: None, 0)
    x1 = x.filter(lambda v: v)
    assert x1 == Try(None, False)
    y = Try.of(lambda x: x, 5)
    y1 = y.filter(lambda v: v > 5)
    assert y1 == Try(5, False)
    z = Try.of(lambda x: x, "test")
    z1 = z.filter(lambda v: v == "test")
    assert z1 == z

# Generated at 2022-06-14 03:54:08.690028
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    result = Try.of(int, 'a').filter(lambda x: x >= 0)
    assert not result.is_success
    assert result.value

    result = Try.of(int, '10').filter(lambda x: x >= 0)
    assert result.is_success
    assert result.value == 10

    result = Try.of(int, '10').filter(lambda x: x > 0)
    assert not result.is_success
    assert result.value


# Generated at 2022-06-14 03:54:13.482036
# Unit test for method filter of class Try
def test_Try_filter():
    def is_bigger_than_5(x): return x > 5

    try_5 = Try(5, is_success=True)
    try_6 = Try(6, is_success=True)

    assert try_5.filter(is_bigger_than_5) == Try(5, is_success=False)
    assert try_6.filter(is_bigger_than_5) == Try(6, is_success=True)

    print("Test Try filter: passes")


# Generated at 2022-06-14 03:54:24.520946
# Unit test for method filter of class Try
def test_Try_filter():
    # Arrange
    def filterer(value):
        return value == 'success'
    try_value_success = Try('success', True)
    try_value_not_success = Try('not_success', True)
    try_not_success = Try('success', False)

    # Act
    try_value = try_value_success.filter(filterer)
    try_value_not = try_value_not_success.filter(filterer)
    try_not = try_not_success.filter(filterer)

    # Assert
    assert try_value.is_success
    assert not try_value_not.is_success
    assert not try_not.is_success