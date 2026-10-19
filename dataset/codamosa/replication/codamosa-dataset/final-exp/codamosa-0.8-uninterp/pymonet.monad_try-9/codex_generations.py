

# Generated at 2022-06-14 03:44:37.290192
# Unit test for method __eq__ of class Try
def test_Try___eq__():
    assert Try(1, True) == Try(1, True)
    assert Try(1, False) == Try(1, False)
    assert Try(1, True) != Try(1, False)
    assert Try(1, False) != Try(1, True)
    assert Try(1, True) != Try(2, True)
    assert Try(1, False) != Try(2, False)


# Generated at 2022-06-14 03:44:42.239735
# Unit test for method __eq__ of class Try
def test_Try___eq__():
    """
    Unit test for method __eq__ of class Try
    """
    assert Try(1, True) == Try(1, True)
    assert Try(1, False) == Try(1, False)
    assert Try(1, True) != Try(2, True)
    assert Try('2', False) != Try(2, False)
    assert Try(3, True) != Try(3, False)
    assert Try(4, False) != Try(4, True)



# Generated at 2022-06-14 03:44:49.795020
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    assert Try(2, True).filter(lambda x: x > 0) == Try(2, True)
    assert Try(2, True).filter(lambda x: x < 0) == Try(2, False)
    assert Try(2, False).filter(lambda x: x >= 0) == Try(2, False)
    assert Try(-2, False).filter(lambda x: x < 0) == Try(-2, False)


# Generated at 2022-06-14 03:44:54.604833
# Unit test for method filter of class Try
def test_Try_filter():
    # Test success filter
    assert Try(1, True).filter(lambda x: x == 1) == Try(1, True)
    assert Try(1, True).filter(lambda x: x != 1) == Try(1, False)

    # Test fail filter
    assert Try(1, False).filter(lambda x: True) == Try(1, False)



# Generated at 2022-06-14 03:44:58.173425
# Unit test for method __eq__ of class Try
def test_Try___eq__():
    assert Try(1, True) == Try(1, True)
    assert Try(1, False) == Try(1, False)
    assert Try(1, True) != Try(1, False)



# Generated at 2022-06-14 03:45:05.944629
# Unit test for method __eq__ of class Try
def test_Try___eq__():  # pragma: no cover
    assert Try(1, True) == Try(1, True)
    assert not Try(1, True) == Try(2, True)
    assert not Try(1, True) == Try(1, False)
    assert not Try(1, False) == Try(2, False)
    assert not Try(5, False) == Try(2, True)



# Generated at 2022-06-14 03:45:11.454054
# Unit test for method __eq__ of class Try
def test_Try___eq__():
    assert Try(2, True) == Try(2, True)
    assert Try(2, False) == Try(2, False)
    assert Try(2, True) != Try(3, True)
    assert Try(2, False) != Try(3, False)
    assert Try(2, True) != Try(2, False)
    assert Try(2, False) != Try(2, True)


# Generated at 2022-06-14 03:45:14.779185
# Unit test for method __eq__ of class Try
def test_Try___eq__():
    assert Try(1, True) == Try(1, True)
    assert Try(1, False) == Try(1, False)

    assert Try(1, True) != Try(2, True)
    assert Try(1, False) != Try(2, False)

    assert Try(1, True) != Try(1, False)
    assert Try(1, False) != Try(1, True)

    assert Try(1, True) != Try(2, False)
    assert Try(1, False) != Try(2, True)


# Generated at 2022-06-14 03:45:18.372787
# Unit test for method __eq__ of class Try
def test_Try___eq__(): #pragma: no cover
    assert Try(1, True) == Try(1, True)
    assert Try(1, False) == Try(1, False)
    assert Try(1, True) != Try(1, False)
    assert Try(1, False) != Try(1, True)
    assert Try(1, True) != Try(2, True)
    assert Try(1, False) != Try(2, False)
    assert Try(1, True) != Try(2, False)
    assert Try(1, False) != Try(2, True)



# Generated at 2022-06-14 03:45:23.113919
# Unit test for method __eq__ of class Try
def test_Try___eq__():
    assert Try(1, True) == Try(1, True)
    assert not (Try(1, True) == Try(1, False))
    assert not (Try(Exception, True) == Try(Exception, False))


# Generated at 2022-06-14 03:45:30.708216
# Unit test for method filter of class Try
def test_Try_filter():
    result = Try.of(lambda: 1)
    assert result == Try(1, True)
    result = result.filter(lambda value: value > 0)
    assert result == Try(1, True)
    result = Try.of(lambda: 1/0)
    assert result == Try(ZeroDivisionError("division by zero"), False)
    result = result.filter(lambda value: value > 0)
    assert result == Try(ZeroDivisionError("division by zero"), False)


# Generated at 2022-06-14 03:45:41.170139
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda x: x, 1).filter(lambda x: x > 0) == Try(1, True)
    assert Try.of(lambda x: x, 1).filter(lambda x: x < 0) == Try(1, False)
    assert Try.of(lambda x: x, 1).filter(lambda x: x > 0).filter(lambda x: x < 0) == Try(1, False)
    assert Try.of(lambda x: x, 1).filter(lambda x: x > 0).filter(lambda x: x > 0) == Try(1, True)



# Generated at 2022-06-14 03:45:47.155085
# Unit test for method filter of class Try
def test_Try_filter():
    """ test_Try_filter """
    assert Try.of(lambda: 2).filter(lambda x: x % 2 == 0) == Try(2, True)
    assert Try.of(lambda: 2).filter(lambda x: x % 2 == 1) == Try(2, False)
    assert Try.of(lambda: Exception()).filter(lambda x: x % 2 == 0) == Try(Exception(), False)

# Generated at 2022-06-14 03:45:52.959035
# Unit test for method filter of class Try
def test_Try_filter():
    def test_filter(x):
        print('test_filter: {}'.format(x))
        return x > 2

    try_1 = Try.of(lambda: 1)
    try_2 = Try.of(lambda: 1).filter(test_filter)
    try_3 = Try.of(lambda: 5).filter(test_filter)

    print(try_1)  # Try[value=1, is_success=True]
    print(try_2)  # Try[value=1, is_success=False]
    print(try_3)  # Try[value=5, is_success=True]


if __name__ == "__main__":  # pragma: no cover
    test_Try_filter()

# Generated at 2022-06-14 03:45:59.766129
# Unit test for method filter of class Try
def test_Try_filter():
    # Given
    def filterer(value):
        return value == 2

    successfully_try = Try(1, True)
    not_successfully_try = Try(2, False)

    # When
    result_1 = successfully_try.filter(filterer)
    result_2 = not_successfully_try.filter(filterer)

    # Then
    assert result_1 == Try(1, False)
    assert result_2 == Try(2, False)


# Generated at 2022-06-14 03:46:06.730984
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value):
        return value.get('test') == 'test'

    call_Try = Try(
        {
            'test': 'test'
        },
        True
    )

    assert call_Try.filter(filterer) == Try({'test': 'test'}, True)

    call_Try = Try(
        {
            'test': 'test1'
        },
        True
    )

    assert call_Try.filter(filterer) == Try({'test': 'test1'}, False)



# Generated at 2022-06-14 03:46:13.769230
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Unit test for method filter of class Try.

    :returns: True if test passed, False otherwise
    :rtype: bool
    """
    def func(x):
        if x > 10:
            return True
        return False

    test_case_1 = Try(15, True).filter(func) == Try(15, True)
    test_case_2 = Try(15, False).filter(func) == Try(15, False)
    test_case_2 = Try(5, True).filter(func) == Try(5, False)

    return test_case_1 and test_case_2 and test_case_3


# Generated at 2022-06-14 03:46:22.102755
# Unit test for method filter of class Try
def test_Try_filter():
    # when predicate for filter return True
    fn1 = lambda x: x
    fn2 = lambda x: x + 1

    assert Try.of(fn1, 1).filter(lambda _: True).get() == 1
    assert Try.of(fn1, 1).filter(lambda _: True).map(fn2).get() == 2
    assert Try.of(fn1, 1).filter(lambda _: True).bind(lambda x: Try(x + 1, True)).get() == 2

    # when predicate for filter return False
    assert not Try.of(fn1, 1).filter(lambda _: False).is_success
    assert Try.of(fn1, 1).filter(lambda _: False).map(fn2).get() == 1

# Generated at 2022-06-14 03:46:25.911906
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 3, ).filter(lambda x: x > 1).get() == 3
    assert Try.of(lambda x: x * 2, 3).filter(lambda x: x > 1).get() == 6
    assert Try.of(lambda x: x, "ask").filter(lambda x: x == "ask").get() == "ask"
    assert Try.of(lambda x: int(x), "2.2").filter(lambda x: x == 2).is_success is False


# Generated at 2022-06-14 03:46:36.502388
# Unit test for method filter of class Try
def test_Try_filter():
    from random import randrange  # pragma: no cover

    def increment(arg):  # pragma: no cover
        return arg + 1

    def decrement(arg):  # pragma: no cover
        return arg - 1

    def is_even(arg):  # pragma: no cover
        return arg % 2 == 0

    def is_odd(arg):  # pragma: no cover
        return not is_even(arg)

    def random_number() -> int:  # pragma: no cover
        return randrange(0, 100)

    def not_number(arg) -> bool:  # pragma: no cover
        return type(arg) is not int

    assert Try.of(random_number)\
        .filter(is_even)\
        .bind(increment)\
        .bind(decrement)\
       

# Generated at 2022-06-14 03:46:52.880942
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(2, True).filter(lambda v: v > 1) == Try(2, True)
    assert Try(2, True).filter(lambda v: v < 1) == Try(2, False)
    assert Try(2, True).filter(lambda v: v > 3) == Try(2, False)
    assert Try(2, False).filter(lambda v: v > 1) == Try(2, False)
    assert Try(2, False).filter(lambda v: v < 1) == Try(2, False)
    assert Try(2, False).filter(lambda v: v > 3) == Try(2, False)



# Generated at 2022-06-14 03:47:00.131918
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(v: int) -> bool:
        return v > 10

    assert Try.of(lambda x: [], 1).filter(filterer) == Try([], False)
    assert Try.of(lambda x: 10, 1).filter(filterer) == Try(10, False)
    assert Try.of(lambda x: 20, 1).filter(filterer) == Try(20, True)



# Generated at 2022-06-14 03:47:04.661006
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda x: x + 1, 1)\
        .filter(lambda x: x % 3 == 0)\
        == Try(2, False)  # 2 is not multiple of 3
    assert Try.of(lambda x: x + 1, 2)\
        .filter(lambda x: x % 3 == 0)\
        == Try(3, True)  # 3 is multiple of 3


# Generated at 2022-06-14 03:47:09.704922
# Unit test for method filter of class Try
def test_Try_filter():
    # when filterer returns False, Try.filter returns not successfully monad
    assert not Try(None, True).filter(lambda x: False).is_success
    # when filterer returns True, Try.filter returns copy of Try
    assert Try(None, True).filter(lambda x: True) == Try(None, True)
    # when Try is not successfully, Try.filter returns copy of Try
    assert not Try(None, False).filter(lambda x: True).is_success
    # when filterer raise exception Try.filter returns not successfully monad
    assert not Try(None, True).filter(lambda x: 1 / 0).is_success



# Generated at 2022-06-14 03:47:14.139806
# Unit test for method filter of class Try
def test_Try_filter():
    assert True == Try.of(lambda: 1).filter(lambda x: x == 1).is_success
    assert True == Try.of(lambda: 1).filter(lambda x: x == 1).is_success
    assert False == Try.of(lambda: 1).filter(lambda x: x == 2).is_success
    assert False == Try.of(lambda: 1).filter(lambda x: x != 1).is_success

# Generated at 2022-06-14 03:47:18.325874
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda _: True) == Try(1, True)
    assert Try(2, True).filter(lambda _: False) == Try(2, False)
    assert Try(3, False).filter(lambda _: True) == Try(3, False)
    assert Try(4, False).filter(lambda _: False) == Try(4, False)



# Generated at 2022-06-14 03:47:21.892901
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(5, True).filter(lambda x: x == 5) == Try(5, True)
    assert Try(5, True).filter(lambda x: x == 6) == Try(5, False)
    assert Try(5, False).filter(lambda x: x == 5) == Try(5, False)
    assert Try(5, False).filter(lambda x: x == 6) == Try(5, False)

# Generated at 2022-06-14 03:47:31.979409
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 2, 'a').filter(lambda value: value < 5) == Try(2, True)
    assert Try.of(lambda: 2, 'a').filter(lambda value: value < 1) == Try(2, False)
    assert Try.of(lambda: None, 5).filter(lambda value: value is not None) == Try(None, False)
    assert Try.of(lambda: 2, 'a').filter(lambda value: value > 5) == Try(2, False)
    assert Try.of(lambda: 2, 'a').filter(lambda value: value >= 2) == Try(2, True)
    assert Try.of(lambda: 2, 'a').filter(lambda value: value == 2) == Try(2, True)

# Generated at 2022-06-14 03:47:42.429188
# Unit test for method filter of class Try
def test_Try_filter():
    positive_number = 1
    negative_number = -1
    zero = 0

    filterer = lambda x: x > 0

    try1 = Try(positive_number, True)
    assert try1 == try1.filter(filterer)

    try2 = Try(negative_number, True)
    assert not Try(negative_number, False) == try2.filter(filterer)

    try3 = Try(zero, True)
    assert not Try(zero, False) == try3.filter(filterer)

    try4 = Try(positive_number, False)
    assert not Try(positive_number, False) == try4.filter(filterer)



# Generated at 2022-06-14 03:47:51.680952
# Unit test for method filter of class Try
def test_Try_filter():

    def filterer(a):
        return a == 10

    assert Try(10, True).filter(filterer) == Try(10, True)
    assert Try(5, True).filter(filterer) == Try(5, False)
    assert Try(5, False).filter(filterer) == Try(5, False)

    try:
        assert (Try(5, True)
                .filter(filterer)
                .get()) == 10
    except Exception as e:
        assert False

    try:
        Try(5, False).filter(filterer).get()
        assert False
    except Exception as e:
        assert True



# Generated at 2022-06-14 03:48:08.801794
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value):
        return value > 0

    monad1 = Try.of(lambda: 10)
    monad2 = Try.of(lambda: -5)

    assert monad1.filter(filterer).get_or_else(lambda: -1) == 10
    assert monad2.filter(filterer).get() is monad2.get()


# Generated at 2022-06-14 03:48:13.944520
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    def filterer(value):
        return value % 2 == 0
    assert Try.of(lambda: 0).filter(filterer) == Try(0, True)
    assert Try.of(lambda: 1).filter(filterer) == Try(1, False)


# Generated at 2022-06-14 03:48:26.986773
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    def filterer(value):
        return value % 2 == 0

    result = Try.of(lambda x: x, 10).filter(filterer)
    assert result == Try(10, True)

    result = Try.of(lambda x: x, 11).filter(filterer)
    assert result == Try(11, False)

    result = Try.of(lambda x: x, 11).filter(filterer).on_success(lambda x: print('success value={}'.format(x)))
    assert result == Try(11, False)

    result = Try.of(lambda x: x, 10).filter(filterer).on_success(lambda x: print('success value={}'.format(x)))
    assert result == Try(10, True)


# Generated at 2022-06-14 03:48:34.601777
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(2, True).filter(lambda x: x == 2) == Try(2, True)
    assert Try(2, True).filter(lambda x: x == 17) == Try(2, False)
    assert Try(2, False).filter(lambda x: x == 17) == Try(2, False)
    assert Try.of(lambda x: 23, 0).filter(lambda x: x == 23) == Try(23, True)
    assert Try.of(lambda x: 23, 0).filter(lambda x: x == 77) == Try(23, False)
    assert Try.of(lambda x: 1 / 0, 0).filter(lambda x: x == 77) == Try(ZeroDivisionError(), False)


# Generated at 2022-06-14 03:48:40.317814
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test of Try filter method:
        * when monad is successfully and filter returns True,
            return same monad
        * when monad is not successfully, return same monad
        * when monad is successfully and filter return False,
            return not successfully monad with previous value
    """
    error = Exception()
    value = 1
    try_obj = Try(value, True)
    assert try_obj.filter(lambda x: x == value) == try_obj
    assert try_obj.filter(lambda x: x == value) == Try(value, True)

    try_obj = Try(value, False)
    assert try_obj.filter(lambda x: x == value) == try_obj
    assert try_obj.filter(lambda x: x == value) == Try(value, False)


# Generated at 2022-06-14 03:48:46.331832
# Unit test for method filter of class Try
def test_Try_filter():
    def function_to_filter(value):
        return value < 4

    t = Try.of(lambda: 4)
    assert t.filter(function_to_filter) == Try(4, False)
    assert t.filter(function_to_filter).filter(function_to_filter) == Try(4, False)
    assert str(t.filter(function_to_filter).filter(function_to_filter)) == 'Try[value=4, is_success=False]'

test_Try_filter()

# Generated at 2022-06-14 03:48:54.076985
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value):
        return True

    def filterer2(value):
        return False

    try_ = Try(None, True)
    assert try_.filter(filterer) == Try(None, True)
    assert try_.filter(filterer2) == Try(None, False)

    try_ = Try(None, False)
    assert try_.filter(filterer) == Try(None, False)
    assert try_.filter(filterer2) == Try(None, False)


# Generated at 2022-06-14 03:48:59.246045
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: x > 0) == Try(1, True)
    assert Try(2, True).filter(lambda x: x % 2 == 0) == Try(2, True)
    assert Try(2, True).filter(lambda x: x % 2 == 0).filter(lambda x: x > 1) == Try(2, True)
    assert Try(1, True).filter(lambda x: x % 2 == 0) == Try(1, False)
    assert Try(1, False).filter(lambda x: x < 0) == Try(1, False)


# Generated at 2022-06-14 03:49:03.956930
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: x > 1) == Try(1, False)
    assert Try(1, False).filter(lambda x: x < 1) == Try(1, False)
    assert Try(2, True).filter(lambda x: x < 3) == Try(2, True)

# Generated at 2022-06-14 03:49:07.704921
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    def is_even(n): return n % 2 == 0
    assert Try.of(lambda: 2).filter(is_even) == Try(2, True)
    assert Try.of(lambda: 3).filter(is_even) == Try(3, False)

# Generated at 2022-06-14 03:49:36.688911
# Unit test for method filter of class Try
def test_Try_filter():

    # Check filterer function when we expect exception
    assert Try.of(int, 'txt value').filter(lambda n: n % 2 == 0)\
        == Try(ValueError("invalid literal for int() with base 10: 'txt value'"), False)

    # Check filterer function when we expect success
    assert Try.of(int, '1').filter(lambda n: n % 2 == 0)\
        == Try(1, False)

    # Check filterer function when we expect success
    assert Try.of(int, '8').filter(lambda n: n % 2 == 0)\
        == Try(8, True)



# Generated at 2022-06-14 03:49:41.828045
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value: str) -> bool:
        return value == 'world'

    assert Try('world', True).filter(filterer) == Try('world', True)
    assert Try('world', False).filter(filterer) == Try('world', False)
    assert Try('hello', True).filter(filterer) == Try('hello', False)

# Generated at 2022-06-14 03:49:44.029809
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: x < 2) == Try(1, True)
    assert Try(1, True).filter(lambda x: x < 1) == Try(1, False)


# Generated at 2022-06-14 03:49:52.356848
# Unit test for method filter of class Try
def test_Try_filter():
    """
    try_filter_1 = Try.of(lambda: 1).filter(lambda x: x==1)

    assert try_filter_1.is_success == True
    assert try_filter_1.value == 1

    try_filter_2 = Try.of(lambda: 1).filter(lambda x: x==2)

    assert try_filter_2.is_success == False
    assert try_filter_2.value == 1

    try_filter_3 = Try.of(lambda: 1/0).filter(lambda x: x==1)

    assert try_filter_3.is_success == False
    """
    pass



# Generated at 2022-06-14 03:49:58.833270
# Unit test for method filter of class Try
def test_Try_filter():
    # Test with successfully Try and filterer returns True
    assert Try.of(lambda: 'A').filter(lambda x: True) == Try('A', True)
    # Test with successfully Try and filterer returns False
    assert Try.of(lambda: 'A').filter(lambda x: False) == Try('A', False)
    # Test with not successfully Try
    assert Try.of(lambda x: x/0, 1).filter(lambda x: True) == Try(ZeroDivisionError(), False)


# Generated at 2022-06-14 03:50:11.150078
# Unit test for method filter of class Try
def test_Try_filter():
    # scenario 1
    try_obj = Try.of(lambda x: x**2, 4)
    try_obj = try_obj.filter(lambda x: x == 16)
    assert Try(16, True) == try_obj

    # scenario 2
    try_obj = Try.of(lambda x: x**2, 4)
    try_obj = try_obj.filter(lambda x: x == 24)
    assert Try(16, False) == try_obj

    # scenario 3
    try_obj = Try.of(lambda x: x/0, 4)
    try_obj = try_obj.filter(lambda x: x == 24)
    assert Try(ZeroDivisionError(), False) == try_obj



# Generated at 2022-06-14 03:50:15.562941
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(v):
        return v % 2 == 0

    monad = Try(1, True)

    assert monad.filter(filterer) == Try(1, False)

    monad = Try(2, True)

    assert monad.filter(filterer) == Try(2, True)
# end test


# Generated at 2022-06-14 03:50:20.603406
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value):
        return value == 1

    assert Try(1, True).filter(filterer) == Try(1, True)
    assert Try(1, False).filter(filterer) == Try(1, False)



# Generated at 2022-06-14 03:50:28.772456
# Unit test for method filter of class Try
def test_Try_filter():
    def my_filterer(value):
        return value < 5
    try_1 = Try(1, True)
    try_2 = Try(6, True)
    assert try_1.filter(my_filterer) == Try(1, True)
    assert try_2.filter(my_filterer) == Try(6, False)
    assert Try(1, False).filter(my_filterer) == Try(1, False)


# Generated at 2022-06-14 03:50:36.108798
# Unit test for method filter of class Try
def test_Try_filter():
    with pytest.raises(TypeError):
        Try(1, True).filter(1)
    try:
        raise Exception('e')
    except Exception as e:
        assert Try(1, False).filter(lambda value: value == 1) == Try(1, False)
        assert Try(1, False).filter(lambda value: value) == Try(1, False)
        assert Try(1, False).filter(lambda value: True) == Try(1, False)
        assert Try(1, True).filter(lambda value: False) == Try(1, False)
        assert Try(1, True).filter(lambda value: value) == Try(1, True)
        assert Try(1, True).filter(lambda value: value == 1) == Try(1, True)

# Generated at 2022-06-14 03:50:59.257457
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(x):
        return x > 30
    assert Try.of(lambda: 40).filter(filterer) == Try(40, True)
    assert Try.of(lambda: 20).filter(filterer) == Try(20, False)

# Generated at 2022-06-14 03:51:03.163257
# Unit test for method filter of class Try

# Generated at 2022-06-14 03:51:06.715594
# Unit test for method filter of class Try
def test_Try_filter():
    try_true = Try(10, True)
    try_false_old = Try(10, False)
    try_false_new = try_true.filter(lambda x: x > 5)
    try_false_old_filtered = try_false_old.filter(lambda x: x > 5)
    assert try_false_new == try_false_old_filtered
    assert try_false_new == Try(10, False)
    assert try_false_old == Try(10, False)


# Generated at 2022-06-14 03:51:12.370938
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(2, True).filter(lambda x: x % 2 == 0)  == Try(2, True)
    assert Try(3, True).filter(lambda x: x % 2 == 0)  == Try(3, False)
    assert Try(2, False).filter(lambda x: x % 2 == 0) == Try(2, False)



# Generated at 2022-06-14 03:51:16.224458
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(10, True).filter(lambda x: x > 9)
    assert Try(0, True).filter(lambda x: x > 9) == Try(0, False)



# Generated at 2022-06-14 03:51:23.911578
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: x < 2) == Try(1, True)
    assert Try(1, True).filter(lambda x: x > 2) == Try(1, False)
    assert Try(1, False).filter(lambda x: x < 2) == Try(1, False)
    assert Try(1, True).filter(lambda x: x < 2).filter(lambda x: x > 10) == Try(1, False)
    assert Try(1, True).filter(lambda x: x < 2).filter(lambda x: x < 3) == Try(1, True)


# Generated at 2022-06-14 03:51:29.968735
# Unit test for method filter of class Try
def test_Try_filter():
    t1 = Try.of(lambda: int('123')) # Successfully Try
    success = t1.filter(lambda x: x % 2 == 1)
    assert success == Try(123, True)

    failure = t1.filter(lambda x: x % 2 == 0)
    assert failure == Try(123, True)

    t2 = Try.of(lambda: int('abc')) # Not successfully Try
    assert t2.filter(lambda x: x % 2 == 1) == t2
    assert t2.filter(lambda x: x % 2 == 0) == t2


# Generated at 2022-06-14 03:51:39.664038
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value):
        return value == 1

    try1 = Try(1, True)
    try2 = Try(2, True)

    assert filterer(1) == filterer(2)
    assert Try.of(lambda: 1, ()) == Try.of(lambda: 2, ())

    success_try = try1.filter(filterer)
    not_success_try = try2.filter(filterer)

    assert success_try.is_success
    assert not not_success_try.is_success

    assert success_try.value == 1
    assert not_success_try.value == 2



# Generated at 2022-06-14 03:51:44.898789
# Unit test for method filter of class Try
def test_Try_filter():
    test_value_1 = 'test_value'
    test_value_2 = 'test_value_2'
    assert Try.filter(Try(test_value_1, True), lambda v: v == test_value_1) == Try(test_value_1, True)
    assert Try.filter(Try(None, True), lambda v: v == test_value_1) == Try(None, False)
    assert Try.filter(Try(None, False), lambda v: v == test_value_1) == Try(None, False)
    assert Try.filter(Try(test_value_1, False), lambda v: v == test_value_1) == Try(test_value_1, False)

# Generated at 2022-06-14 03:51:50.881139
# Unit test for method filter of class Try
def test_Try_filter():
    def to_uppercase(string):
        return string.upper()

    def is_string(string):
        return isinstance(string, str)

    assert Try.of(to_uppercase, 'python').filter(is_string) == Try('PYTHON', True)
    assert Try.of(to_uppercase, 100).filter(is_string) == Try(100, False)


# Generated at 2022-06-14 03:52:36.278096
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value):
        return True
    def other_filterer(value):
        return False

    try_monad = Try(1, True)
    assert try_monad.filter(filterer) == Try(1, True)
    assert try_monad.filter(other_filterer) == Try(1, False)
    assert try_monad == Try(1, True)

    try_monad = Try(1, False)
    assert try_monad.filter(filterer) == Try(1, False)
    assert try_monad.filter(other_filterer) == Try(1, False)
    assert try_monad == Try(1, False)


# Generated at 2022-06-14 03:52:43.727835
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Unit test function for class Try method filter.

    :returns: void
    :rtype: None
    """

    def inc(value):
        return value + 1

    def is_even(value):
        return value % 2 == 0

    assert Try.of(inc, 1).filter(is_even) == Try(1, False)
    assert Try.of(inc, 2).filter(is_even) == Try(3, True)

# Generated at 2022-06-14 03:52:48.939049
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value):
        return value > 0

    successful_try = Try(3, True)
    assert successful_try.filter(filterer).is_success
    assert successful_try.filter(filterer).get() == successful_try.get()

    not_successful_try = Try(-1, True)
    assert not not_successful_try.filter(filterer).is_success

    unsuccessful_try = Try(-1, False)
    assert not unsuccessful_try.filter(filterer).is_success

# Generated at 2022-06-14 03:52:54.418343
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test function for filter method of class Try.

    :returns: True when test passed, othercase throws AssertionError
    :rtype: Boolean
    """

    # test for successfully filter with filterer function that returns True
    is_test_passed = Try(1, True)\
        .filter(lambda x: True) == Try(1, True)

    # test for successfully filter with filterer function that returns True
    is_test_passed = is_test_passed and Try(1, True)\
        .filter(lambda x: False) == Try(1, False)

    # test for not successfully filter with filterer function that returns True
    is_test_passed = is_test_passed and Try(1, False)\
        .filter(lambda x: True) == Try(1, False)

   

# Generated at 2022-06-14 03:52:58.828570
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda i: i == 1)
    assert not Try(1, True).filter(lambda i: i == 2)
    assert not Try(1, True).filter(lambda i: i == 1).filter(lambda i: i == 1).filter(lambda i: i == 2)
    assert Try(1, True).filter(lambda i: i == 1).filter(lambda i: i == 1)
    assert Try(1, False).filter(lambda _: True).get() == 1


# Generated at 2022-06-14 03:53:11.207322
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Unit test for method filter of class Try
    """

    # check simple value
    assert Try.of(lambda: 5).filter(lambda x: x > 5) == Try(5, False)
    assert Try.of(lambda: 5).filter(lambda x: x == 5) == Try(5, True)

    # check value with exception
    assert Try.of(lambda: 1/0).filter(lambda x: True) == Try(ZeroDivisionError('division by zero'), False)
    assert Try.of(lambda: 1/0).filter(lambda x: False) == Try(ZeroDivisionError('division by zero'), False)

    print('Function "test_Try_filter" runned successfully')


# Generated at 2022-06-14 03:53:17.255393
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(2, True).filter(lambda x: x > 1) == Try(2, True)
    assert Try(2, True).filter(lambda x: x < 1) == Try(2, False)
    assert Try(Exception, False).filter(lambda x: True) == Try(Exception, False)


# Generated at 2022-06-14 03:53:23.538824
# Unit test for method filter of class Try
def test_Try_filter():
    def even(x):
        return x % 2 == 0

    assert Try(10, True).filter(even) == Try(10, True)
    assert Try(11, True).filter(even) == Try(11, False)
    assert Try(11, False).filter(even) == Try(11, False)
    assert Try(Exception, False).filter(even) == Try(Exception, False)


# Generated at 2022-06-14 03:53:26.802242
# Unit test for method filter of class Try
def test_Try_filter():
    try_ = Try(1, True)
    filtered = try_.filter(lambda x: x > 10)
    assert filtered == Try(1, False)



# Generated at 2022-06-14 03:53:33.001627
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    def even(a):
        return not bool(a % 2)

    def even_or_none(a):
        return a if even(a) else None

    assert Try.of(even_or_none, 1) == Try(1, False)
    assert Try.of(even_or_none, 2).filter(even) == Try(2, True)