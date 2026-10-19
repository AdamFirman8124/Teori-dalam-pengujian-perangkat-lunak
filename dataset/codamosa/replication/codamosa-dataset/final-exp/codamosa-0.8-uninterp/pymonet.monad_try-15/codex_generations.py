

# Generated at 2022-06-14 03:44:37.668843
# Unit test for method filter of class Try
def test_Try_filter():
    t = Try.of(lambda: 1).filter(lambda v: True)
    assert t == Try(1, True)

    t = Try.of(lambda: 1).filter(lambda v: False)
    assert t == Try(1, False)

    t = Try.of(lambda: a).filter(lambda v: v == 1)
    assert t == Try(NameError('name "a" is not defined'), False)



# Generated at 2022-06-14 03:44:41.839968
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    def pick_integer(value):
        return isinstance(value, int)
    def throw_exception():
        raise Exception('test')

    assert Try.of(throw_exception).filter(pick_integer) == Try(Exception('test'), False)
    assert Try.of(lambda: 1).filter(pick_integer) == Try(1, True)



# Generated at 2022-06-14 03:44:49.307693
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(x):
        return x < 10

    assert Try(1, True).filter(filterer) == Try(1, True)
    assert Try(1, False).filter(filterer) == Try(1, False)
    assert Try(11, True).filter(filterer) == Try(11, False)
    assert Try(11, False).filter(filterer) == Try(11, False)
    print('SUCCESS')

# Generated at 2022-06-14 03:44:58.432519
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    def some_function():
        return Try(None, True)

    def some_other_function():
        return Try(None, False)

    def some_function_with_raise():
        raise Exception('Exception in function')

    assert Try.of(some_function).filter(lambda m: True) == Try(None, True)
    assert Try.of(some_function).filter(lambda m: False) == Try(None, False)
    assert Try.of(some_other_function).filter(lambda m: True) == Try(None, False)
    assert Try.of(some_function).filter(lambda m:True).filter(lambda m:True) == Try(None, True)

# Generated at 2022-06-14 03:45:02.038425
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 1, ()).filter(lambda x: x > 0) == Try(1, True)
    assert Try.of(lambda: 1, ()).filter(lambda x: x > 1) == Try(1, False)
    assert Try.of(lambda: 1, ()).filter(lambda x: x > 1).is_success == False

# Generated at 2022-06-14 03:45:05.949474
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(v):
        return True

    try_ = Try(1, True)
    assert try_.filter(filterer) == Try(1, True)

    try_ = Try(1, False)
    assert try_.filter(filterer) == Try(1, False)



# Generated at 2022-06-14 03:45:15.122427
# Unit test for method filter of class Try
def test_Try_filter():
    class MathError(Exception):

        def __init__(self, message) -> None:
            super().__init__(message)

    t = Try.of(lambda x: x + 1, 1)
    assert t.filter(lambda x: x != 1) == Try(2, True)
    assert t.filter(lambda x: x == 1) == Try(2, False)
    assert Try.of(lambda x: 1 / 0, None).filter(lambda x: x < 0) == Try(None, False)
    assert Try.of(lambda x: 1 / 0, None).filter(lambda x: x > 0) == Try(None, False)
    assert Try.of(lambda x: MathError('error'), None).filter(lambda x: x > 1) == Try(None, False)


# Generated at 2022-06-14 03:45:28.982075
# Unit test for method filter of class Try
def test_Try_filter():
    # Test instance of callable class
    class Test:  # pragma: no cover
        def __init__(self):
            self.value = True
        def __call__(self):
            return self.value
    test = Test()

    success = Try(1, True)
    fail = Try(Exception(), False)

    # Test class implementation
    assert success.filter(lambda x: x == 1) == Try(1, True)
    assert success.filter(lambda x: x != 1) == Try(1, False)
    assert fail.filter(lambda x: x == 1) == Try(Exception(), False)

    # Test function implementation
    assert success.filter(lambda x: x == 1) == Try(1, True)
    assert success.filter(lambda x: x != 1) == Try(1, False)

# Generated at 2022-06-14 03:45:36.294687
# Unit test for method filter of class Try
def test_Try_filter():
    try_with_value = Try(2, True)
    try_without_value = Try(2, False)

    def filterer(x):
        return x % 2 == 0

    assert try_with_value.filter(filterer) == Try(2, True)
    assert try_without_value.filter(filterer) == Try(2, False)

# Generated at 2022-06-14 03:45:42.517104
# Unit test for method filter of class Try
def test_Try_filter():
    # Test filter monad
    def filterer(value):
        if value < 20:
            return True
        return False

    # Test filter with successfully monad
    assert Try.of(lambda: 'value1').filter(filterer) == Try('value1', True)
    # Test filter with not successfully monad
    assert Try.of(lambda: 'value2', raise_Except).filter(filterer) == Try('value2', False)



# Generated at 2022-06-14 03:45:52.810090
# Unit test for method filter of class Try
def test_Try_filter():
    def is_even(x):
        return x % 2 == 0

    def is_odd(x):
        return x % 2 != 0

    assert Try(2, True).filter(is_even) == Try(2, True)
    assert Try(2, True).filter(is_odd) == Try(2, False)
    assert Try(2, False).filter(is_even) == Try(2, False)
    assert Try(2, False).filter(is_odd) == Try(2, False)



# Generated at 2022-06-14 03:46:04.213089
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda n: n > 0) == Try(1, True)
    assert Try(1, True).filter(lambda n: n < 0) == Try(1, False)
    assert Try(1, True).filter(lambda n: n == 1) == Try(1, True)
    assert Try(1, False).filter(lambda n: n != 1) == Try(1, False)
    assert Try(0, True).filter(lambda n: n) == Try(0, False)
    assert Try(0, True).filter(lambda n: not n) == Try(0, True)
    assert Try(1, True).filter(lambda n: n == 0) == Try(1, False)
    assert Try(1, True).filter(lambda n: n) == Try(1, True)

# Generated at 2022-06-14 03:46:08.491978
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value):
        return value > 2

    try1 = Try.of(lambda: 2, None)
    try2 = try1.filter(filterer)
    assert try1 == try1
    assert not try1 == try2
    assert try2.is_success is False


# Generated at 2022-06-14 03:46:12.971970
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: x == 1) == Try(1, True)
    assert Try(1, True).filter(lambda x: x != 1) == Try(1, False)



# Generated at 2022-06-14 03:46:21.548336
# Unit test for method filter of class Try
def test_Try_filter():
    t = Try.of(lambda: 1, )
    t2 = Try.of(lambda: 1, )
    t3 = Try.of(lambda: 1, )
    t4 = Try.of(lambda: 1, )
    assert t.filter(lambda value: value > 0) == t2
    assert t.filter(lambda value: value == 0) != t2
    assert t.filter(lambda value: value > 0).get() == t3.get()
    assert t.filter(lambda value: value == 0).get() != t3.get()
    assert t.filter(lambda value: value > 0) == t.filter(lambda value: value == 1)
    assert t.filter(lambda value: value > 0) != t.filter(lambda value: value == 0)
    assert t == t4

# Generated at 2022-06-14 03:46:26.188375
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    def check_value(value) -> bool:
        return value >= 20

    assert Try.of(lambda a: a, 10).filter(check_value).get_or_else('default') == 'default'

    assert Try.of(lambda a: a, 25).filter(check_value).get_or_else('default') == 25



# Generated at 2022-06-14 03:46:36.825796
# Unit test for method filter of class Try
def test_Try_filter():
    test_value = "test"
    assert Try.of(lambda: test_value).filter(lambda x: x == test_value) == Try(test_value, True)
    assert Try.of(lambda: test_value).filter(lambda x: x != test_value) == Try(test_value, False)
    assert Try.of(lambda: test_value, 1, 2) == Try(test_value, True)
    assert Try.of(lambda: test_value, 1, 2).filter(lambda x: x == test_value) == Try(test_value, True)
    assert Try.of(lambda: test_value, 1, 2).filter(lambda x: x != test_value) == Try(test_value, False)

# Generated at 2022-06-14 03:46:46.433662
# Unit test for method filter of class Try
def test_Try_filter():
    from unittest import TestCase, main
    from unittest.mock import call, patch
    from typing import Callable
    from random import randint

    class TryFilter(TestCase):

        def setUp(self):
            self.value = randint(0, 10)
            self.filterer_mock = patch('PythoMonads.Try.filterer',
                                       side_effect=lambda x: x % 2 == 0).start()
            self.success_mapper_mock = patch('PythoMonads.Try.success_mapper',
                                             side_effect=lambda x: x + 1).start()
            self.fail_mapper_mock = patch('PythoMonads.Try.fail_mapper',
                                          side_effect=lambda x: x + 1).start()



# Generated at 2022-06-14 03:46:51.270380
# Unit test for method filter of class Try
def test_Try_filter():
    def func(a):
        return a == 3

    x = Try(3, True)
    assert x.filter(func) == Try(3, True)

    y = Try(4, True)
    assert y.filter(func) == Try(4, False)

    z = Try(4, False)
    assert z.filter(func) == Try(4, False)


# Generated at 2022-06-14 03:46:55.597074
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    def filterer(value):
        return value > 5

    try_1 = Try.of(lambda: 10)
    try_2 = Try.of(lambda: 2)

    assert try_1.filter(filterer).get() == 10
    assert not try_2.filter(filterer).is_success


# Generated at 2022-06-14 03:47:08.019325
# Unit test for method filter of class Try
def test_Try_filter():
    # Test 1
    assert Try.of(lambda: 42, None).filter(lambda x: x > 0) == Try(42, True)
    # Test 2
    assert Try.of(lambda: 42, None).filter(lambda x: x < 0) == Try(42, False)
    # Test 3
    assert Try.of(lambda: 42, None).filter(lambda x: x == 0) == Try(42, False)
    # Test 4
    assert Try.of(lambda: 42, None).filter(lambda x: x == 42) == Try(42, True)
    # Test 5
    assert Try.of(lambda: 42, None).filter(lambda x: True) == Try(42, True)
    # Test 6
    assert Try.of(lambda: 42, None).filter(lambda x: False) == Try(42, False)

# Generated at 2022-06-14 03:47:11.989399
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda x: x ** 2, 2)\
        .filter(lambda x: x > 2)\
        == Try(4, False)
    assert Try.of(lambda x: x ** 2, 2)\
        .filter(lambda x: x > 1)\
        == Try(4, True)


# Generated at 2022-06-14 03:47:22.266401
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(None, False).filter(lambda a: True) == Try(None, False)  # is not successful, so copy
    assert Try(None, True).filter(lambda a: True) == Try(None, True)  # is successful, so copy
    assert Try(None, True).filter(lambda a: False) == Try(None, False)  # is not successfully, so new Try with value
    assert Try(1, True).filter(lambda v: v == 1) == Try(1, True)  # check is value equal to 1, so copy
    assert Try(1, True).filter(lambda v: v == 0) == Try(1, False)  # check is value equal to 0, so new Try with value

# Generated at 2022-06-14 03:47:27.623245
# Unit test for method filter of class Try
def test_Try_filter():
    filtered_value = Try.of(lambda: 10).filter(lambda x: x > 0)
    assert filtered_value == Try(10, True)

    filtered_value = Try.of(lambda: -10).filter(lambda x: x > 0)
    assert filtered_value == Try(-10, False)


# Generated at 2022-06-14 03:47:34.214512
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Unit test for method filter of class Try
    """
    def successful_checker(value):
        return True

    def not_successful_checker(value):
        return False

    assert Try(1, True).filter(successful_checker) == Try(1, True)
    assert Try(1, False).filter(successful_checker) == Try(1, False)

    assert Try(1, True).filter(not_successful_checker) == Try(1, False)



# Generated at 2022-06-14 03:47:43.776473
# Unit test for method filter of class Try
def test_Try_filter():
    # Given
    not_success_future = Try(Exception, False)
    success_future = Try(10, True)

    # When
    def filterer(value):
        """
        Test filterer.
        Return True when value is 10.

        :params value: value to pass by test filterer
        :type value: A
        :returns: Is value is 10
        :rtype: Boolean
        """
        return value == 10

    # Then
    assert not_success_future.filter(filterer) == Try(Exception, False)
    assert success_future.filter(filterer) == Try(10, True)


# Generated at 2022-06-14 03:47:48.901222
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value):
        return value > 2

    assert Try(1, True).filter(filterer) == Try(1, False)
    assert Try(2, True).filter(filterer) == Try(2, False)
    assert Try(3, True).filter(filterer) == Try(3, True)

# Generated at 2022-06-14 03:47:52.380100
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 1, ).filter(lambda i: i == 1).is_success == True
    assert Try.of(lambda: 1, ).filter(lambda i: i == 2).is_success == False


# Generated at 2022-06-14 03:47:58.719942
# Unit test for method filter of class Try
def test_Try_filter():
    # Case 1: Try with exception, filterer returns False
    try_list = Try.of(lambda: [1, 2, 3, 0, 4, 5], 1)
    filtered_try_list = try_list.filter(lambda xs: 0 not in xs)
    assert filtered_try_list is try_list

    # Case 2: Try with exception, filterer returns False
    try_list = Try.of(lambda: [1, 2, 3, 4, 5], 1)
    filtered_try_list = try_list.filter(lambda xs: 0 not in xs)
    assert filtered_try_list is not try_list



# Generated at 2022-06-14 03:48:04.018444
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 5, ).filter(lambda a: a == 5) == Try(5, True)
    assert Try.of(lambda: 5, ).filter(lambda a: a == 1) == Try(5, False)
    assert Try.of(lambda: 5, ).filter(lambda a: a == 1).get_or_else(0) == 0

# Generated at 2022-06-14 03:48:23.096356
# Unit test for method filter of class Try
def test_Try_filter():
    value = [1, 2]
    try_with_value = Try.of(lambda: value)
    try_filtered_value = try_with_value.filter(lambda a: len(a) == 2)
    try_not_filtered_value = Try.of(lambda: value).filter(lambda a: len(a) == 1)
    assert try_filtered_value == Try(value, True)
    assert try_not_filtered_value == Try(value, False)


# Generated at 2022-06-14 03:48:26.518661
# Unit test for method filter of class Try
def test_Try_filter():
    result = Try(1, True).filter(lambda x: x == 1)
    assert result == Try(1, True)
    result = Try(1, True).filter(lambda x: x != 1)
    assert result == Try(1, False)

# Generated at 2022-06-14 03:48:35.135913
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 1).filter(lambda a: a > 0) == Try(1, True)
    assert Try.of(lambda: 1).filter(lambda a: a < 0) == Try(1, False)
    assert Try.of(lambda: 1).filter(lambda a: a < 0).get() == 1
    assert Try.of(lambda: 1).filter(lambda a: a < 0) == Try(1, False)
    assert Try.of(lambda: 0/0).filter(lambda a: a > 0) == Try(ZeroDivisionError(), False)

    assert Try.of(lambda: 0/0).filter(lambda a: a > 0).get_or_else(lambda: 1) == 1

# Generated at 2022-06-14 03:48:38.214252
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: x == 1) == Try(1, True)
    assert Try(1, True).filter(lambda x: x == 2) == Try(1, False)
    assert Try(1, False).filter(lambda x: x == 1) == Try(1, False)


# Generated at 2022-06-14 03:48:40.130729
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 1, ).filter(lambda x: x == 1) == Try(1, True)
    assert Try.of(lambda: 1, ).filter(lambda x: x != 1) == Try(1, False)

# Generated at 2022-06-14 03:48:44.761991
# Unit test for method filter of class Try
def test_Try_filter():
    from operator import eq

    assert Try(5, True).filter(lambda x: eq(x, 5)) == Try(5, True)
    assert Try(5, True).filter(lambda x: eq(x, 4)) == Try(5, False)
    assert Try(4, True).filter(lambda x: eq(x, 5)) == Tr

# Generated at 2022-06-14 03:48:49.683278
# Unit test for method filter of class Try
def test_Try_filter():
    def foo(a):
        return a
    assert Try(100, True).filter(foo) == Try(100, True)
    assert Try(100, True).filter(lambda a: False) == Try(100, False)
    assert Try(100, False).filter(foo) == Try(100, False)


# Generated at 2022-06-14 03:48:58.679119
# Unit test for method filter of class Try
def test_Try_filter():
    def test_filter(value):
        return value >= 40

    # filter after map
    val = Try.of(int, '40')\
        .filter(test_filter)\
        .map(lambda x: x**2)

    assert val == Try(1600, True)

    # filter before map
    val = Try.of(int, '40')\
        .map(lambda x: x**2)\
        .filter(test_filter)

    assert val == Try(1600, True)

    # filter after bind
    val = Try.of(int, '40')\
        .bind(lambda x: Try(x**2, True))\
        .filter(test_filter)

    assert val == Try(1600, True)

    # filter after bind not successfully
    val = Try.of(int, '40')\
       

# Generated at 2022-06-14 03:49:07.861232
# Unit test for method filter of class Try
def test_Try_filter():
    def add_10(num):
        return num + 10

    assert Try(10, True).filter(lambda x: x % 2 == 0) == Try(10, True)
    assert Try(7, True).filter(lambda x: x % 2 == 0) == Try(7, False)
    assert Try(10, False).filter(lambda x: x % 2 == 0) == Try(10, False)
    assert Try(10, True)\
            .filter(lambda x: x % 2 == 0)\
            .map(add_10)\
            .on_success(lambda y: print('Success: {}'.format(y)))\
            .on_fail(lambda e: print('Fail: {}'.format(e))) == Try(20, True)

# Generated at 2022-06-14 03:49:16.249003
# Unit test for method filter of class Try
def test_Try_filter():
    # given
    try_1 = Try(1, True)

    # when
    try_2 = try_1.filter(lambda x: x % 2 == 0)
    try_3 = try_1.filter(lambda x: x % 2 != 0)

    # then
    assert try_2.is_success is False
    assert try_2.value == 1

    assert try_3.is_success is True
    assert try_3.value == 1


# Generated at 2022-06-14 03:49:41.782494
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Test Try filter method.
    """
    assert Try(1, True).filter(lambda value: value == 1) == Try(1, True)
    assert Try(1, True).filter(lambda value: value == 2) == Try(1, False)
    assert Try(1, False).filter(lambda value: value == 1) == Try(1, False)



# Generated at 2022-06-14 03:49:45.496636
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: x == 1) == Try(1, True)
    assert Try(None, False).filter(lambda x: x == 1) == Try(None, False)
    assert Try(1, False).filter(lambda x: x == 1) == Try(1, False)
    assert Try(None, True).filter(lambda x: x == 1) == Try(None, False)

# Generated at 2022-06-14 03:49:53.323996
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(2, True).filter(lambda x: x > 5) == Try(2, False)
    assert Try(5, True).filter(lambda x: x > 5) == Try(5, True)
    assert Try(2, True).filter(lambda x: x > 5)\
        .filter(lambda x: x < 10) == Try(2, False)
    assert Try(7, True).filter(lambda x: x > 5)\
        .filter(lambda x: x < 10) == Try(7, True)
    assert Try(2, False).filter(lambda x: x > 5) == Try(2, False)
    assert Try(7, False).filter(lambda x: x > 5) == Try(7, False)



# Generated at 2022-06-14 03:49:57.801242
# Unit test for method filter of class Try
def test_Try_filter():
    assert (Try(1, True).filter(lambda x: x == 1) == Try(1, True))
    assert (Try(1, False).filter(lambda x: x == 1) == Try(1, False))
    assert (Try(1, True).filter(lambda x: x == 2) == Try(1, False))


# Generated at 2022-06-14 03:50:10.957810
# Unit test for method filter of class Try
def test_Try_filter():
    success_try = Try(2, True)
    failure_try = Try(3, False)

    def filter_value_is_greater_then_one(value):
        return value > 1

    is_filter_raise_exception = False
    try:
        new_failure_try = failure_try.filter(filter_value_is_greater_then_one)
        is_filter_raise_exception = True
    except Exception as e:
        is_filter_raise_exception = False

    assert not is_filter_raise_exception
    assert new_failure_try == failure_try

    new_success_try = success_try.filter(filter_value_is_greater_then_one)
    assert new_success_try != success_try


# Generated at 2022-06-14 03:50:15.455509
# Unit test for method filter of class Try
def test_Try_filter():
    """
    Unit test for method filter of class Try.
    """
    def predicate(x):
        return x > 0
    assert Try.of(lambda x: x, 1).filter(predicate) == Try(1, True)
    assert Try.of(lambda x: x, -1).filter(predicate) == Try(-1, False)

# Generated at 2022-06-14 03:50:27.536803
# Unit test for method filter of class Try
def test_Try_filter():
    def test_filterer(value):
        return value == 2

    # Successfully filtered
    try_1 = Try(2, True)
    try_2 = try_1.filter(test_filterer)
    assert try_1 == try_2, 'Successfully filter not work!'

    try_1 = Try(2, False)
    try_2 = try_1.filter(test_filterer)
    assert try_1 == try_2, 'Successfully filter not work!'

    try_1 = Try(8, False)
    try_2 = try_1.filter(test_filterer)
    assert try_1 == try_2, 'Successfully filter not work!'

    try_1 = Try(8, True)
    try_2 = try_1.filter(test_filterer)

# Generated at 2022-06-14 03:50:36.320510
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 10).filter(lambda x: x > 0) == Try(10, True)
    assert Try.of(lambda: 10).filter(lambda x: x < 0) == Try(10, False)
    assert Try.of(lambda: 0).filter(lambda x: x > 0) == Try(0, False)
    assert Try.of(lambda: 10).filter(lambda x: x > 0).filter(lambda x: x > 5) == Try(10, True)
    assert Try.of(lambda: 10).filter(lambda x: x > 0).filter(lambda x: 1 / x > 5) == Try(10, False)

# Generated at 2022-06-14 03:50:39.934646
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(x):
        return x == 1
    try_with_filter_true = Try(1, True)
    try_with_filter_false = Try(2, True)

    try_with_filter_true = try_with_filter_true.filter(filterer)
    assert try_with_filter_true.get() == 1
    assert try_with_filter_true.is_success

    try_with_filter_false = try_with_filter_false.filter(filterer)
    assert try_with_filter_false.get() == 2
    assert not try_with_filter_false.is_success


# Generated at 2022-06-14 03:50:46.806447
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: x == 1) == Try(1, True)
    assert Try(1, True).filter(lambda x: x == 2) == Try(1, False)
    assert Try(1, False).filter(lambda x: x == 1) == Try(1, False)
    assert Try(1, False).filter(lambda x: x == 2) == Try(1, False)


# Generated at 2022-06-14 03:51:26.571191
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try.of(lambda: 1, 1).filter(lambda x: x == 1) == Try(1, True)
    assert Try.of(lambda: 1, 1).filter(lambda x: x == 2) == Try(1, False)


# Generated at 2022-06-14 03:51:31.700617
# Unit test for method filter of class Try
def test_Try_filter():  # pragma: no cover
    var = True
    err = Exception('Error!')
    assert Try(var, True).filter(lambda x: x) == Try(var, True)
    assert Try(var, True).filter(lambda x: x == False) == Try(var, False)
    assert Try(var, False).filter(lambda x: x) == Try(var, False)
    assert Try(err, False).filter(lambda x: x == False) == Try(err, False)



# Generated at 2022-06-14 03:51:42.030688
# Unit test for method filter of class Try
def test_Try_filter():
    unsuccess_try = Try("Ok", True)
    success_try = Try("Ok", False)
    assert unsuccess_try.filter(lambda x: len(x) > 1) == Try("Ok", False)
    assert unsuccess_try.filter(lambda x: len(x) > 2) == Try("Ok", False)
    assert success_try.filter(lambda x: len(x) > 1) == Try("Ok", False)
    assert success_try.filter(lambda x: len(x) > 2) == Try("Ok", False)
    assert unsuccess_try.filter(lambda x: len(x) == 1) == Try("Ok", True)
    assert unsuccess_try.filter(lambda x: len(x) == 2) == Try("Ok", False)

# Generated at 2022-06-14 03:51:46.538356
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: True) == Try(1, True)
    assert Try(1, False).filter(lambda x: True) == Try(1, False)
    assert Try(1, True).filter(lambda x: False) == Try(1, False)


# Generated at 2022-06-14 03:51:53.019273
# Unit test for method filter of class Try
def test_Try_filter():
    def is_short_string(s):
        return len(s) < 10

    def is_short_string_with_error(s):
        return len(s) < 10

    def is_short_string_with_exception(s):
        raise ValueError(s)

    assert Try.of(is_short_string, "short string").filter(is_short_string) == Try("short string", True)
    assert Try.of(is_short_string_with_error, "short string").filter(is_short_string) == Try("short string", True)
    assert Try.of(is_short_string_with_exception, "short string").filter(is_short_string) == Try("short string", False)

# Generated at 2022-06-14 03:51:55.417825
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value):
        return value > 0
    assert Try.of(lambda x: x, 1).filter(filterer) == Try(1, True)
    assert Try.of(lambda x: x, 0).filter(filterer) == Try(0, False)

# Generated at 2022-06-14 03:52:02.032391
# Unit test for method filter of class Try
def test_Try_filter():
    def filterer(value):
        return value == 1

    assert Try(1, True).filter(filterer) == Try(1, True)
    assert Try(10, True).filter(filterer) == Try(10, False)
    assert Try(ValueError('error'), False).filter(filterer) == Try(ValueError('error'), False)


# Generated at 2022-06-14 03:52:04.052558
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(2, True).filter(lambda x : x > 10) == Try(2, False)

# Generated at 2022-06-14 03:52:09.675687
# Unit test for method filter of class Try
def test_Try_filter():
    class CustomError(Exception):
        def __init__(self, arg):
            self.args = arg
    def test_filterer(value: int) -> bool:
        return value > 0
    try1 = Try.of(int, '-5')
    try2 = Try.of(int, '5')
    # When value of try1 not greater than 0, try1 should not be successfully
    assert try1.filter(test_filterer).is_success is False
    # When value of try1 greater than 0, try1 should be successfully
    assert try2.filter(test_filterer).is_success is True


# Generated at 2022-06-14 03:52:13.872699
# Unit test for method filter of class Try
def test_Try_filter():
    assert Try(1, True).filter(lambda x: x > 0) == Try(1, True)
    assert Try(1, True).filter(lambda x: x > 1) == Try(1, False)

# Generated at 2022-06-14 03:53:06.888125
# Unit test for method __str__ of class Try
def test_Try___str__():
    assert 'Try[value=5, is_success=True]' == str(Try(5, True))
    assert 'Try[value=None, is_success=True]' == str(Try(None, True))
    assert 'Try[value=5, is_success=False]' == str(Try(5, False))
    assert 'Try[value=None, is_success=False]' == str(Try(None, False))
    assert 'Try[value=<Exception: bad>, is_success=False]' == str(Try('bad', False))

# Unit tests for method of of class Try

# Generated at 2022-06-14 03:53:13.747609
# Unit test for method __eq__ of class Try
def test_Try___eq__():
    assert Try(1, True) == Try(1, True)
    assert Try(1, False) == Try(1, False)

    assert Try(1, True) != Try(0, True)
    assert Try(1, True) != Try(None, True)
    assert Try(1, True) != Try(None, False)
    assert Try(1, True) != Try(None, True)
    assert Try(1, False) != Try(None, False)
    assert Try(Exception(), True) != Try(None, True)
    assert Try(Exception(), True) != Try(None, False)
    assert Try(Exception(), True) != Try(Exception(), False)
    assert Try(Exception(), False) != Try(None, False)



# Generated at 2022-06-14 03:53:18.318768
# Unit test for method get_or_else of class Try
def test_Try_get_or_else():
    none_try = Try(None, False)
    assert none_try.get_or_else(1) == 1

    some_value_try = Try(2, True)
    assert some_value_try.get_or_else(1) == 2


# Generated at 2022-06-14 03:53:22.887685
# Unit test for method __str__ of class Try
def test_Try___str__():  # pragma: no cover
    assert str(Try(2, True)) == 'Try[value=2, is_success=True]'
    assert str(Try(ValueError("error"), False)) == 'Try[value=error, is_success=False]'


# Generated at 2022-06-14 03:53:34.905077
# Unit test for method bind of class Try
def test_Try_bind():
    assert Try.of(lambda: 1, ()).bind(lambda a: Try(a + 1, True)) == Try(2, True)
    assert Try.of(lambda: 1, ()).bind(lambda a: Try(a + 1, False)) == Try(1, False)
    assert Try.of(lambda: 1, ()).bind(lambda a: Try(a + 1, True)).bind(lambda a: Try(a + 2, True)) == Try(3, True)
    assert Try.of(lambda: 1, ()).bind(lambda a: Try(a + 1, True)).bind(lambda a: Try(a + 2, False)) == Try(3, False)

# Generated at 2022-06-14 03:53:39.642726
# Unit test for method bind of class Try
def test_Try_bind():
    def binder(value):
        if value == 1:
            return Try(2, True)
        return Try(1, False)

    assert Try(1, True).bind(binder) == Try(2, True)
    assert Try(2, False).bind(binder) == Try(2, False)


# Generated at 2022-06-14 03:53:44.251841
# Unit test for method filter of class Try
def test_Try_filter():
    # given
    x = Try(4, True)
    y = Try('FFF', False)
    # when
    x_mapped = x.filter(lambda x: x < 5)
    y_mapped = y.filter(lambda x: True)
    # then
    assert x_mapped.is_success == True
    assert x_mapped.value == 4
    assert y_mapped.is_success == False
    assert y_mapped.value == 'FFF'

# Generated at 2022-06-14 03:53:55.045604
# Unit test for method filter of class Try
def test_Try_filter():

    def filterer(value):  # type: ignore
        return value > 11

    def filterer_return_True(value):  # type: ignore
        return True

    def filterer_return_False(value):  # type: ignore
        return False

    assert Try.of(lambda: 10).filter(filterer_return_True) == Try(10, True)
    assert Try.of(lambda: 10).filter(filterer_return_False) == Try(10, False)
    assert Try.of(lambda: 10).filter(filterer) == Try(10, False)
    assert Try.of(lambda: 12).filter(filterer) == Try(12, True)



# Generated at 2022-06-14 03:53:58.311835
# Unit test for method __eq__ of class Try
def test_Try___eq__():
    # Assert that equal two monads
    assert Try(True, True) == Try(True, True)

    # Assert that not equal two monads
    assert not Try(True, True) == Try(True, False)


# Generated at 2022-06-14 03:54:03.294406
# Unit test for method get of class Try
def test_Try_get():
    """Test for get method."""
    assert Try(10, False).get() == 10
    assert Try(11.1, True).get() == 11.1
    assert Try('string', True).get() == 'string'
