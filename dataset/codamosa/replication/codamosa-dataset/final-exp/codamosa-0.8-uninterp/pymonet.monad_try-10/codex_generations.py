

# Generated at 2022-06-14 03:44:37.247774
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(x):
        return True

    def filterer_false(x):
        return False

    actual = Try.filter(Try.of(lambda: 5), filterer)
    assert actual == Try(5, True)

    actual = Try.filter(Try.of(lambda: 5), filterer_false)
    assert actual == Try(5, False)


# Generated at 2022-06-14 03:44:44.394397
# Unit test for method filter of class Try
def test_Try_filter():
    def is_even(x):
        return x%2 == 0
    assert Try.of(lambda: 4).filter(is_even) == Try(4, True)
    assert Try.of(lambda: 5).filter(is_even) == Try(5, False)
    assert Try.of(lambda: 1/0).filter(is_even) == Try(ZeroDivisionError(), False)


# Generated at 2022-06-14 03:44:50.940100
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    def true_filter(value):
        return True

    def false_filter(value):
        return False

    assert Try(1, True).filter(true_filter) == Try(1, True)
    assert Try(1, True).filter(false_filter) == Try(1, False)
    assert Try(1, False).filter(true_filter) == Try(1, False)
    assert Try(1, False).filter(false_filter) == Try(1, False)


# Generated at 2022-06-14 03:44:59.341659
# Unit test for method filter of class Try
def test_Try_filter():
    """
    test_Try_filter
    """
    assert Try.of(lambda x: x, 1).filter(lambda x: x > 0) == Try(1, True)
    assert Try.of(lambda x: x, -9).filter(lambda x: x > 0) == Try(-9, False)
    assert Try.of(lambda x: x, 1).filter(lambda x: x > 0).value == 1
    assert Try.of(lambda x: x, -9).filter(lambda x: x > 0).value == -9
    assert Try.of(lambda x: x, 1).filter(lambda x: x > 0).is_success
    assert not Try.of(lambda x: x, -9).filter(lambda x: x > 0).is_success



# Generated at 2022-06-14 03:45:07.756746
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    assert Try(1, True).filter(lambda x: x == 1) == Try(1, True)
    assert Try(1, True).filter(lambda x: x == 2) == Try(1, False)
    assert Try(1, False).filter(lambda x: x == 1) == Try(1, False)
    assert Try(1, False).filter(lambda x: x == 2) == Try(1, False)



# Generated at 2022-06-14 03:45:14.229714
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(2, True).filter(lambda val: val > 1) == Try(2, True)
    assert Try(2, True).filter(lambda val: val > 10) == Try(2, False)
    assert Try(None, False).filter(lambda val: val > 1) == Try(None, False)


# Generated at 2022-06-14 03:45:19.711420
# Unit test for method filter of class Try
def test_Try_filter():
    # setup
    value = 1
    try_ = Try(value, True)
    
    # when
    try_filtered = try_.filter(lambda x: x % 2 == 0)

    # then
    assert Try(value, False) == try_filtered
# test_Try_filter()

# Generated at 2022-06-14 03:45:28.599610
# Unit test for method filter of class Try
def test_Try_filter():
    try_success = Try.of(lambda: 'It is successful',)
    try_failed = Try.of(lambda: 1 / 0,)

    try_filtered = try_success.filter(lambda x: x == 'It is successful')
    assert try_filtered.is_success == True

    try_filtered = try_success.filter(lambda x: x != 'It is successful')
    assert try_filtered.is_success == False

    try_filtered = try_failed.filter(lambda x: x != 'It is successful')
    assert try_filtered.is_success == False


# Generated at 2022-06-14 03:45:34.104341
# Unit test for method filter of class Try
def test_Try_filter():
    try_with_value = Try(True, True)
    assert try_with_value.filter(lambda x: x) == Try(True, True)
    assert try_with_value.filter(lambda x: not x) == Try(True, False)
    assert Try(False, True).filter(lambda x: not x) == Try(False, False)
    assert Try(False, True).filter(lambda x: x) == Try(False, True)


# Generated at 2022-06-14 03:45:46.765215
# Unit test for method filter of class Try
def test_Try_filter():
    assert True == Try(3, True).filter(lambda x: x == 3).is_success
    assert True == Try(3, True).filter(lambda x: x == 3).get() == 3
    assert False == Try(3, True).filter(lambda x: x == 2).is_success
    assert 2 == Try(3, True).filter(lambda x: x == 2).get()

    assert False == Try(3, False).filter(lambda x: x == 3).is_success
    assert 3 == Try(3, False).filter(lambda x: x == 3).get()
    assert False == Try(3, False).filter(lambda x: x == 2).is_success
    assert 3 == Try(3, False).filter(lambda x: x == 2).get()

# Generated at 2022-06-14 03:45:55.673535
# Unit test for constructor of class Try
def test_Try():
    print("Calling constructor of class Try")
    assert Try(3, True) == Try(3, True)
    assert Try(3, False) == Try(3, False)
    assert not Try(3, True) == Try(3, False)
    assert not Try(3, True) == Try(2, True)
    assert not Try(3, True) == Try(2, False)


# Generated at 2022-06-14 03:45:58.752723
# Unit test for method __str__ of class Try
def test_Try___str__():
    assert 'Try[value=1, is_success=True]' == str(Try(1, True))
    assert 'Try[value=Exception(), is_success=False]' == str(Try(Exception(), False))


# Generated at 2022-06-14 03:46:04.276434
# Unit test for method on_success of class Try
def test_Try_on_success():
    def double(x):
        return x * 2

    assert Try(10, True).on_success(double).get() == 20
    assert Try(20, False).on_success(double).get() == 20
    assert Try(30, True).on_success(double).is_success == True



# Generated at 2022-06-14 03:46:07.485669
# Unit test for constructor of class Try
def test_Try():
    assert Try(None, True) == Try(None, True)
    assert Try(Exception('1'), False) != Try(Exception('2'), False)
    assert Try(None, False) != Try(2, False)
    assert Try(None, True) != Try(2, True)


# Generated at 2022-06-14 03:46:13.737563
# Unit test for method get_or_else of class Try
def test_Try_get_or_else():
    # Given
    fn = lambda: 'Success'
    try_success = Try.of(fn)

    # When
    result_success = try_success.get_or_else('Default')

    # Then
    assert result_success == 'Success'

    # Given
    def except_fn():
        raise ValueError('Expected Error')
    try_fail = Try.of(except_fn)

    # When
    result_fail = try_fail.get_or_else('Default')

    # Then
    assert result_fail == 'Default'


# Generated at 2022-06-14 03:46:16.093003
# Unit test for method get_or_else of class Try
def test_Try_get_or_else():
    assert Try(42, True).get_or_else(None) == 42
    assert Try(None, False).get_or_else(42) == 42



# Generated at 2022-06-14 03:46:19.844403
# Unit test for method __eq__ of class Try
def test_Try___eq__():
    assert Try(1, True) == Try(1, True)
    assert Try(1, True) != Try(2, True)
    assert Try(1, True) != Try(1, False)
    assert Try(1, True) != Try(2, False)
    assert Try(1, False) != Try(2, True)


# Generated at 2022-06-14 03:46:22.136431
# Unit test for method __str__ of class Try
def test_Try___str__():
    sut = Try(1, True)
    actual = sut.__str__()
    expected = 'Try[value=1, is_success=True]'
    assert actual == expected


# Generated at 2022-06-14 03:46:26.219279
# Unit test for constructor of class Try
def test_Try():
    some_try = Try(True, True)
    assert some_try.value == True
    assert some_try.is_success == True

    another_try = Try(Exception(), False)
    assert another_try.value != Exception()
    assert another_try.is_success == False

test_Try()



# Generated at 2022-06-14 03:46:31.557520
# Unit test for method on_fail of class Try
def test_Try_on_fail():
    """
    Test for method on_fail of class Try
    """

    def side_effect_function(_):
        assert 1

    # Run method on_fail on successfully monad
    Try(1, True).on_fail(side_effect_function)
    # Run method on_fail on fail monad
    Try(Exception(), False).on_fail(side_effect_function)


# Generated at 2022-06-14 03:46:41.294142
# Unit test for method __str__ of class Try
def test_Try___str__():
    assert str(Try.of(lambda x: x*2, 3)) == 'Try[value=6, is_success=True]'
    assert str(Try.of(lambda x: x/0, 3)) == 'Try[value=division by zero, is_success=False]'


# Generated at 2022-06-14 03:46:46.024185
# Unit test for method __str__ of class Try
def test_Try___str__():
    assert str(Try(1, True)) == 'Try[value=1, is_success=True]'
    assert str(Try(Exception('Boom'), False)) == 'Try[value=Boom, is_success=False]'


# Generated at 2022-06-14 03:46:54.195216
# Unit test for method get_or_else of class Try
def test_Try_get_or_else():
    value = 1
    anything = 'test'
    try_ = Try.of(lambda: value, None)
    assert try_.get_or_else(anything) == value
    assert try_.map(lambda x: x + 1).get_or_else(anything) == 2
    try_ = Try.of(lambda: 1 / 0, None)
    assert try_.get_or_else(anything) == anything
    assert try_.map(lambda x: x + 1).get_or_else(anything) == anything


# Generated at 2022-06-14 03:46:59.672544
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    """
    Testing method filter of class Try.
    """
    assert Try.of(lambda x: x, 2).filter(lambda x: x > 0) == Try(2, True)
    assert Try.of(lambda x: x, -1).filter(lambda x: x > 0) == Try(-1, False)



# Generated at 2022-06-14 03:47:03.997048
# Unit test for constructor of class Try
def test_Try():
    assert Try(1, True) == Try(1, True)
    assert Try(None, False) == Try(None, False)
    assert Try(None, True) != Try(None, False)


# Generated at 2022-06-14 03:47:07.293467
# Unit test for method get of class Try
def test_Try_get():
    some_value = 'some value'
    try_instance = Try(some_value, True)
    assert try_instance.get() == some_value


# Generated at 2022-06-14 03:47:11.043720
# Unit test for method get_or_else of class Try
def test_Try_get_or_else():
    result = Try.of(lambda: '', 0)
    assert_that(result.get_or_else('default_value'), equal_to('default_value'))
    assert_that(result.get_or_else([]), equal_to([]))


# Generated at 2022-06-14 03:47:18.847799
# Unit test for method __eq__ of class Try
def test_Try___eq__():
    success = Try(10, True)
    another_success = Try(10, True)
    type_success = Try(10, False)
    value_success = Try(15, True)
    success_success = Try(10, False)

    fail = Try(10, False)
    another_fail = Try(10, False)
    type_fail = Try(10, True)
    value_fail = Try(15, False)
    success_fail = Try(10, True)

    assert success == another_success  # Equal
    assert fail == another_fail  # Equal

    assert success != type_success  # Not equal with different type
    assert success != value_success  # Not equal with different value
    assert success != success_success  # Not equal with different success value

    assert fail != type_fail  # Not equal with different type


# Generated at 2022-06-14 03:47:22.660960
# Unit test for method bind of class Try
def test_Try_bind():
    """
    Test for method bind of class Try

    :returns:
    """
    def add(a):
        return Try(a + a, True)

    assert Try(1, True).bind(add) == Try(2, True)
    assert Try('Error', False).bind(add) == Try('Error', False)



# Generated at 2022-06-14 03:47:30.791113
# Unit test for method bind of class Try
def test_Try_bind():
    a = Try(42, True).bind(lambda x: Try(x + 1, True)).get()
    assert a == 43
    b = Try(42, False).bind(lambda x: Try(x + 1, True)).get()
    assert b == 42
    c = Try(42, True).bind(lambda x: Try(x + 1, False)).get()
    assert c == 42
    d = Try(42, False).bind(lambda x: Try(x + 1, False)).get()
    assert d == 42


# Generated at 2022-06-14 03:47:45.282482
# Unit test for method __str__ of class Try
def test_Try___str__():
    assert str(Try(1, True)) == 'Try[value=1, is_success=True]'
    assert str(Try(1, False)) == 'Try[value=1, is_success=False]'
    assert str(Try(Exception('my-error'), True)) == 'Try[value=my-error, is_success=True]'
    assert str(Try(Exception('my-error'), False)) == 'Try[value=my-error, is_success=False]'


# Generated at 2022-06-14 03:47:55.394859
# Unit test for method bind of class Try
def test_Try_bind():
    def parse_int(string):
        return Try(int(string), True)

    def divide(first, second):
        return Try(first / second, True)

    def divide_with_result(first, second):
        try:
            return Try(first / second, True)
        except Exception as e:
            return Try(e, False)

    assert Try.of(parse_int, '4')\
        .bind(lambda x: divide_with_result(x, 0)) == Try(0, False)

    assert Try.of(parse_int, '4')\
        .bind(lambda x: divide_with_result(x, 2)) == Try(2, True)

    assert Try.of(parse_int, '4')\
        .bind(lambda x: divide(x, 0)) == Try(0, False)

# Generated at 2022-06-14 03:48:00.089435
# Unit test for method map of class Try
def test_Try_map():
    def add_one(value):
        return value + 1

    assert Try.of(add_one, 1).map(add_one) == Try(3, True)

    def f():
        raise BaseException()

    assert Try.of(f).map(add_one) == Try(f.__code__, False)


# Generated at 2022-06-14 03:48:02.451495
# Unit test for method on_success of class Try
def test_Try_on_success():  # pragma: no cover
    def success_callback(value):
        print(value)

    success = Try(42, True)
    fail = Try(None, False)

    success.on_success(success_callback)
    fail.on_success(success_callback)


# Generated at 2022-06-14 03:48:04.420046
# Unit test for method __str__ of class Try
def test_Try___str__():
    assert str(Try('foo', True)) == 'Try[value=foo, is_success=True]'


# Generated at 2022-06-14 03:48:11.262294
# Unit test for method on_fail of class Try
def test_Try_on_fail():
    """
    This test invoke on_fail method on not successfully Try.
    And checking if was called with same value of previous Try.
    """
    try:
        raise BaseException()
    except BaseException as e:
        try_ = Try(e, False)
    fail_callback = MagicMock()
    try_.on_fail(fail_callback)
    fail_callback.assert_called_with(try_.value)


# Generated at 2022-06-14 03:48:15.116116
# Unit test for method on_success of class Try
def test_Try_on_success():
    assert Try(1, True).on_success(lambda x: print(x)) == Try(1, True)
    assert Try(1, False).on_success(lambda x: print(x)) == Try(1, False)



# Generated at 2022-06-14 03:48:18.656790
# Unit test for constructor of class Try
def test_Try():
    assert Try(4, True) == Try(4, True)
    assert Try(4, False) == Try(4, False)
    assert Try(4, True).is_success
    assert not Try(4, False).is_success


# Generated at 2022-06-14 03:48:24.257853
# Unit test for method __str__ of class Try
def test_Try___str__():  # pragma: no cover
    assert Try(5, True).__str__() == 'Try[value=5, is_success=True]'
    assert Try(Exception('value 5 not correct'), False).__str__() == 'Try[value=value 5 not correct, is_success=False]'


# Generated at 2022-06-14 03:48:27.598969
# Unit test for method __str__ of class Try
def test_Try___str__():  # pragma: no cover
    assert str(Try(10, True)) == 'Try[value=10, is_success=True]'
    assert str(Try(10, False)) == 'Try[value=10, is_success=False]'



# Generated at 2022-06-14 03:48:44.436103
# Unit test for method on_fail of class Try
def test_Try_on_fail():
    """The Try.on_fail() method should call fail_callback when monad is not successfully else nothing"""
    mock = Mock()
    not_successful = Try(Exception(), False)
    not_successful.on_fail(mock)
    mock.assert_called_once_with(Exception())
    successful = Try('success', True)
    successful.on_fail(mock)
    assert mock.call_count == 1


# Generated at 2022-06-14 03:48:51.700688
# Unit test for method on_success of class Try
def test_Try_on_success():
    # Successful case
    result = Try(1, True) \
        .on_success(lambda value: print('Successfully case with value {}'.format(value)))
    assert result.get() == 1

    # Fail case
    result = Try(ValueError(), False) \
        .on_success(lambda value: print('Successfully case with value {}'.format(value)))
    assert result.get() == ValueError()



# Generated at 2022-06-14 03:48:54.413193
# Unit test for method get_or_else of class Try
def test_Try_get_or_else():
    assert Try(2, True).get_or_else(1) == 2
    assert Try(2, False).get_or_else(1) == 1


# Generated at 2022-06-14 03:48:57.678254
# Unit test for method bind of class Try
def test_Try_bind():
    result = Try.of(int, "42").bind(lambda x: Try.of(str, x))
    assert result == Try('42', True)

    result = Try.of(int, "abc").bind(lambda x: Try.of(str, x))
    assert result == Try(ValueError, False)


# Generated at 2022-06-14 03:49:01.426808
# Unit test for method on_success of class Try

# Generated at 2022-06-14 03:49:08.894372
# Unit test for method on_fail of class Try
def test_Try_on_fail():
    def fail_callback(value):
        assert value == 'fail_callback_test'

    monad = Try('success_callback_test', True)
    assert monad.on_fail(fail_callback).is_success == True, \
        'Successfully monad should be not call on_fail callback'

    monad = Try('fail_callback_test', False)
    assert monad.on_fail(fail_callback).is_success == False, \
        'Not successfully monad should be call on_fail callback'

    print('Try_on_fail test success')


# Generated at 2022-06-14 03:49:17.664925
# Unit test for method on_fail of class Try
def test_Try_on_fail():
    """
    Try on_fail test.

    :returns: assert test result
    :rtype: Boolean
    """
    failed_try = Try(ValueError('test'), False)

# Generated at 2022-06-14 03:49:26.143175
# Unit test for method bind of class Try
def test_Try_bind():
    # Arrange
    m1 = Try.of(lambda x: x + 1, 1)
    m2 = Try.of(lambda x: x + ' world', 'hello')
    m3 = Try.of(lambda x: x + [2], [1])
    m4 = Try.of(lambda x: x / 0, 10)
    s = lambda x: Try.of(lambda: x + 100)

    # Act
    res1 = m1.bind(s)
    res2 = m2.bind(s)
    res3 = m3.bind(s)
    res4 = m4.bind(s)

    # Assert
    True



# Generated at 2022-06-14 03:49:29.592864
# Unit test for method get of class Try
def test_Try_get():
    """
    Test method get of class Try

    :returns: None
    :rtype: None
    """
    assert Try.of(lambda: 1).get() == 1


# Generated at 2022-06-14 03:49:35.218948
# Unit test for method get of class Try
def test_Try_get():
    assert Try(1, True).get() == 1
    assert Try(1, False).get() == 1
    assert Try('A', True).get() == 'A'
    assert Try('A', False).get() == 'A'
    assert Try([1], True).get() == [1]
    assert Try([1], False).get() == [1]


# Generated at 2022-06-14 03:49:59.749399
# Unit test for method on_fail of class Try
def test_Try_on_fail():
    def on_fail_callback(value):
        print('{} is not working as expected'.format(value))

    def add_two_numbers(x, y):
        return x + y

    try1 = Try.of(add_two_numbers, 1, 2)
    assert try1.is_success
    try1.on_fail(on_fail_callback)

    try2 = Try.of(add_two_numbers, 'string', 'string2')
    assert not try2.is_success
    try2.on_fail(on_fail_callback)



# Generated at 2022-06-14 03:50:12.082052
# Unit test for method on_fail of class Try
def test_Try_on_fail():
    # Test on fail, when not raise exception
    assert Try(lambda: 1/1, True).on_fail(lambda e: print('1/1')) == Try(lambda: 1/1, True)
    assert Try(lambda: 1/0, True).on_fail(lambda e: print(e)) == Try(ZeroDivisionError('division by zero'), False)

    # Test on fail, when raise exception
    assert Try(lambda: 1/1, True).on_fail(lambda e: print(e)) == Try(lambda: 1/1, True)

# Generated at 2022-06-14 03:50:15.612180
# Unit test for method get_or_else of class Try
def test_Try_get_or_else():
    assert Try(None, False).get_or_else(1) == 1
    assert Try(1, True).get_or_else(2) == 1


# Generated at 2022-06-14 03:50:27.678787
# Unit test for method filter of class Try
def test_Try_filter():
    def generate_error():
        raise ZeroDivisionError('Division Error')

    # When error is raised, but we have false in filter,
    # we should have successfully Try
    assert\
        Try.of(generate_error).filter(lambda _: False) ==\
        Try(ZeroDivisionError('Division Error'), True)

    # When error is raised and we have true in filter,
    # we should have not successfully Try
    assert\
        Try.of(generate_error).filter(lambda _: True) ==\
        Try(ZeroDivisionError('Division Error'), False)

    # When successful Try, and we have false in filter,
    # we should have not successfully Try
    assert\
        Try.of(lambda: 1).filter(lambda _: False) ==\
        Try(1, False)

    #

# Generated at 2022-06-14 03:50:31.971574
# Unit test for method on_success of class Try
def test_Try_on_success():
    def callback(value):
        print("hello", value)

    value = 'world'
    assert Try(value, True) == Try(value, True).on_success(lambda _: callback("world"))
    assert Try(value, False) == Try(value, False).on_success(lambda _: callback("world"))



# Generated at 2022-06-14 03:50:36.234124
# Unit test for method get of class Try
def test_Try_get():
    # def test_Try_get(self):
    assert Try(True, True).get() is True
    assert Try(False, False).get() is False
    assert Try(None, True).value is None



# Generated at 2022-06-14 03:50:40.774873
# Unit test for method __str__ of class Try
def test_Try___str__():
    assert(str(Try(1, True)) == 'Try[value=1, is_success=True]')
    assert(str(Try(1, False)) == 'Try[value=1, is_success=False]')


# Generated at 2022-06-14 03:50:44.634543
# Unit test for method map of class Try
def test_Try_map():
    assert Try(42, True).map(lambda x: x + 1) == Try(43, True)
    assert Try(42, False).map(lambda x: x + 1) == Try(42, False)


# Generated at 2022-06-14 03:50:57.294233
# Unit test for method get_or_else of class Try
def test_Try_get_or_else():
    def test_get_or_else(value, default_value, expected_value, expected_is_success):
        try_ = Try(value, True)
        assert try_.get_or_else(default_value) == expected_value
        assert try_.is_success == expected_is_success

        try_ = Try(value, False)
        assert try_.get_or_else(default_value) == expected_value
        assert try_.is_success == expected_is_success

    test_get_or_else(1, 2, 1, True)
    test_get_or_else(1, 2, 2, False)
    test_get_or_else('value', 'default', 'value', True)
    test_get_or_else('value', 'default', 'default', False)
    test_get_or_else

# Generated at 2022-06-14 03:51:02.339011
# Unit test for method __eq__ of class Try
def test_Try___eq__():
    assert Try(5, True) == Try(5, True)
    assert Try(5, True) != Try(6, True)
    assert Try(5, False) != Try(6, False)
    assert Try(5, False) != Try(6, True)
    assert Try(5, True) != Try(6, False)


# Generated at 2022-06-14 03:51:41.446609
# Unit test for method get_or_else of class Try
def test_Try_get_or_else():
    assert Try(1, True).get_or_else(2) == 1
    assert Try(1, False).get_or_else(2) == 2

# Generated at 2022-06-14 03:51:45.327052
# Unit test for method on_fail of class Try
def test_Try_on_fail():
    exception = RuntimeError('Some exception')
    try_instance = Try(exception, False)

    def callback(value):
        assert value == exception

    assert try_instance.on_fail(callback) == Try(exception, False)


# Generated at 2022-06-14 03:51:48.458257
# Unit test for method get_or_else of class Try
def test_Try_get_or_else():
    assert Try(1, True).get_or_else(0) == 1
    assert Try(None, False).get_or_else(0) == 0


# Generated at 2022-06-14 03:51:53.156976
# Unit test for method on_success of class Try
def test_Try_on_success():
    def callback(x):
        print('x={}'.format(x))
    result = Try.of(lambda: 1)\
        .on_success(lambda x: print(x+1))\
        .on_success(callback)
    assert result == Try(1, True)


# Generated at 2022-06-14 03:51:58.015713
# Unit test for method get_or_else of class Try
def test_Try_get_or_else():  # pragma: no cover
    print('>>> test_Try_get_or_else <<<')
    assert Try(1, True).get_or_else(2) == 1
    assert Try('a', False).get_or_else('b') == 'b'
    assert Try('a', None).get_or_else('b') == 'b'
    assert Try(1, None).get_or_else(2) == 2


# Generated at 2022-06-14 03:52:00.786608
# Unit test for method on_fail of class Try

# Generated at 2022-06-14 03:52:07.474732
# Unit test for method on_fail of class Try
def test_Try_on_fail():
    """
    Unit test for method on_fail of class Try

    :returns:
    :rtype:
    """

    # function with exception
    def foo(x):
        return x / 0

    # attempt to call function foo
    t = Try.of(foo, 5)

    # t is not successful Try
    assert not t.is_success
    assert t.value is not None

    # check that exception is ZeroDivisionError

# Generated at 2022-06-14 03:52:11.717730
# Unit test for method on_success of class Try
def test_Try_on_success():
    assert Try(10, True).on_success(lambda x: x * 10) == Try(100, True)
    assert Try(10, False).on_success(lambda x: x * 10) == Try(10, False)



# Generated at 2022-06-14 03:52:17.135066
# Unit test for method map of class Try
def test_Try_map():
    """
    Test map function of class Try.
    """
    def mul(x):
        return x * x
    assert Try(2, True).map(mul) == Try(4, True)
    assert Try(2, False).map(mul) == Try(2, False)


# Generated at 2022-06-14 03:52:23.294812
# Unit test for method bind of class Try
def test_Try_bind():
    def fn(a):
        if a == 1:
            return Try(1, True)
        raise Exception('str')

    fn_1 = fn(1)
    assert fn_1.bind(fn).value == 1, 'Should be equal'
    assert fn_1.bind(fn).is_success, 'Should be true'

    fn_2 = fn(2)
    assert isinstance(fn_2.bind(fn).value, Exception), 'Should be instance of Exception'
    assert not fn_2.bind(fn).is_success, 'Should be false'



# Generated at 2022-06-14 03:53:09.180429
# Unit test for constructor of class Try
def test_Try():
    assert Try(1, True) == Try(1, True)
    assert Try(1, False) == Try(1, False)
    assert Try(1, True) != Try(1, False)
    assert Try(1, False) != Try(0, True)
    assert Try(1, True) != Try(0, True)
    assert Try(Exception('Error'), True) != Try(Exception('Error'), False)



# Generated at 2022-06-14 03:53:13.085185
# Unit test for method filter of class Try
def test_Try_filter():
    def test_filterer(x):
        return x == 5

    assert Try(5, True).filter(test_filterer) == Try(5, True)
    assert Try(5, False).filter(test_filterer) == Try(5, False)
    assert Try(4, True).filter(test_filterer) == Try(4, False)
    assert Try(4, False).filter(test_filterer) == Try(4, False)



# Generated at 2022-06-14 03:53:24.564108
# Unit test for method bind of class Try
def test_Try_bind():
    assert Try.of(lambda x: x, 1).map(lambda x: x + 1).get() == 2
    assert Try.of(lambda x: x, 1).bind(lambda x: Try(x + 1, True)) == Try(2, True)
    assert Try(1, True).bind(lambda x: Try(x + 1, True)) == Try(2, True)
    assert Try(1, True).bind(lambda x: Try(x + 1, False)) == Try(2, False)
    assert Try(1, False).bind(lambda x: Try(x + 1, True)) == Try(1, False)
    assert Try(1, False).bind(lambda x: Try(x + 1, False)) == Try(1, False)

# Generated at 2022-06-14 03:53:29.032338
# Unit test for method on_fail of class Try
def test_Try_on_fail():
    assert Try(1, True).on_fail(lambda x: x) == Try(1, True)
    assert Try(1, False).on_fail(lambda x: x) == Try(1, False)


# Generated at 2022-06-14 03:53:32.112156
# Unit test for method __str__ of class Try
def test_Try___str__():
    assert str(Try(1, True)) == 'Try[value=1, is_success=True]'
    assert str(Try(Exception(), False)) == 'Try[value=Exception(), is_success=False]'


# Generated at 2022-06-14 03:53:34.175456
# Unit test for method get_or_else of class Try
def test_Try_get_or_else():
    """
    >>> test_Try_get_or_else()
    """
    assert Try(10, True).get_or_else(0) == 10
    assert Try(10, False).get_or_else(0) == 0


# Generated at 2022-06-14 03:53:42.406814
# Unit test for method __eq__ of class Try
def test_Try___eq__():
    equality_test_cases = [
        [Try(123, True),
         Try(123, True)],

        [Try(123, True),
         Try(124, True)],

        [Try(123, True),
         Try(123, False)],

        [Try(123, False),
         Try(123, False)],

        [Try(123, False),
         Try(124, False)],

        [Try(123, False),
         Try(123, True)],
    ]

    for test_case in equality_test_cases:
        assert test_case[0] == test_case[1]



# Generated at 2022-06-14 03:53:46.300548
# Unit test for method map of class Try
def test_Try_map():
    assert Try.of(lambda x: x * 2, 2).map(lambda x: x + 2) == Try(6, True)
    assert Try.of(lambda x: 1 / 0).map(lambda x: x + 2) == Try(ZeroDivisionError, False)



# Generated at 2022-06-14 03:53:56.914884
# Unit test for method bind of class Try
def test_Try_bind():
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Case 1:
    #   1.1: Monad is successfully and binder return other successful Try.
    #       1.1.1: binder returns successfully Try with same value.
    #       1.1.2: binder returns successfully Try with other value.
    #   1.2: Monad is successfully and binder return not successful Try.
    #   1.3: Monad is not successful and binder return successful Try.
    #   1.4: Monad is not successful and binder return not successful Try.

    # Case 1.1.1
    first_successful_try_value = 'first_successful_try_value'
    first_successful_try = Try(first_successful_try_value, True)


# Generated at 2022-06-14 03:54:04.956237
# Unit test for method __eq__ of class Try
def test_Try___eq__():
    value = 'value'
    success = Try(value, True)
    other_success = Try(value, True)
    fail = Try(value, False)
    other_fail = Try(value, False)

    assert success == success
    assert success == other_success
    assert fail == fail
    assert fail == other_fail
    assert success != fail
    assert fail != success
    assert fail != 'fail'
    assert fail != 1
