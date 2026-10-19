

# Generated at 2022-06-14 04:11:34.075638
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.fail().to_lazy() == Lazy(lambda: None)
    assert Validation.fail('Error1', 'Error2').to_lazy() == Lazy(lambda: None)
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 04:11:37.022964
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    result = Lazy(lambda: 2).to_validation()
    assert result == Validation.success(2)


# Generated at 2022-06-14 04:11:42.429598
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    assert Validation.success(5).to_lazy() == Lazy(lambda: 5)
    assert Validation.success(None).to_lazy() == Lazy(lambda: None)
    assert Validation.fail(['error']).to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 04:11:49.662984
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    # When success Validation is converted to Lazy then Lazy value is Validation value
    value = "abc"
    validation = Validation.success(value)
    assert validation.to_lazy().value() == value
    # When fail Validation is converted to Lazy then Lazy value is None
    validation = Validation.fail(["error"])
    assert validation.to_lazy().value() is None


# Generated at 2022-06-14 04:11:56.537851
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.box import Box
    from pymonet.lazy import Lazy

    assert Validation.success(123).to_lazy() == Lazy(lambda: 123), 'This is not the same'
    assert Validation.success(123).to_lazy().to_val() == Box(123), 'This is not the same'
    assert Validation.fail(['error1']).to_lazy().to_val() == Box(None), 'This is not the same'


# Generated at 2022-06-14 04:11:59.516180
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Lazy(lambda: 'test') == Validation.success('test').to_lazy()
    assert Lazy(lambda: None) == Validation.fail(['test']).to_lazy()


# Generated at 2022-06-14 04:12:06.672567
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test to_lazy method of Validation class.
    """
    from pymonet.monad_try import Try

    def assert_to_lazy(value, expected):
        """
        Assert to_lazy method.
        """
        actual = Validation.success(value).to_lazy()
        assert isinstance(actual, Lazy)
        assert actual.value() == expected

    # Test value is a simple value
    assert_to_lazy('value', 'value')

    # Test value is a complex structure

# Generated at 2022-06-14 04:12:09.973357
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Validation.success(42).to_lazy() == Lazy(lambda: 42)
    assert Validation.fail([42, 43]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:12:15.317727
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 'Value') == Validation.success('Value').to_lazy()
    assert Lazy(lambda: None) == Validation.fail([]).to_lazy()


# Generated at 2022-06-14 04:12:21.353469
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    value = 10

    lazy = Lazy(lambda: value)
    validation = Validation.success(value)

    assert validation.to_lazy() == lazy


# Generated at 2022-06-14 04:12:29.059425
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    success_result = Validation.success(10).to_lazy()
    fail_result = Validation.fail([1, 2, 3]).to_lazy()

    assert isinstance(success_result, Lazy)
    assert isinstance(fail_result, Lazy)
    assert success_result.value() == 10
    assert fail_result.value() is None


# Generated at 2022-06-14 04:12:31.221071
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy().eval() == 1
    assert Validation.fail([1]).to_lazy().eval() is None


# Generated at 2022-06-14 04:12:35.331861
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Make all test.

    :return: True when all test are successful, otherwise False
    :rtype: Boolean
    """
    from pymonet.lazy import Lazy

    sut = Validation(Lazy(lambda: 'hello'), ['error'])
    result = sut.to_lazy().value()

    assert result == 'hello', 'Expected "hello" but got {}'.format(result)

    return True

# Generated at 2022-06-14 04:12:38.597435
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 04:12:45.668474
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation
    from pymonet.validation import Validation

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail(1).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:12:47.894579
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    v = Validation.success(2)

    assert v.to_lazy() == Lazy(lambda: 2)



# Generated at 2022-06-14 04:12:51.190954
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail(1).to_lazy() == Lazy(lambda: None)

# Unit tests for method to_try of class Validation

# Generated at 2022-06-14 04:12:56.816887
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    lazy = Lazy(lambda: 1)
    validation = Validation.success(lazy)
    assert validation.to_lazy() is lazy


# Generated at 2022-06-14 04:13:03.389490
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    validation = Validation.success(1)
    assert isinstance(validation.to_lazy(), Lazy)

    validation = Validation.fail()
    assert isinstance(validation.to_lazy(), Lazy)
    assert validation.to_lazy().get() is None


# Generated at 2022-06-14 04:13:07.124513
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    # Given
    from pymonet.lazy import Lazy

    validation = Validation.success(1)
    expected = Lazy(lambda: 1)

    # When
    actual = validation.to_lazy()

    # Then
    assert actual == expected


# Generated at 2022-06-14 04:13:12.591845
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.fail(['err', 'err2']).to_lazy() == Lazy(lambda: None) and \
           Validation.success(10).to_lazy() == Lazy(lambda: 10)



# Generated at 2022-06-14 04:13:14.529964
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test that Validation value can be get by to_lazy method.
    """
    assert Validation.success(3).to_lazy().force() == 3


# Generated at 2022-06-14 04:13:18.860881
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Validation(None, []).to_lazy() == Lazy(lambda: None)
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail(['error']).to_lazy() == Lazy(lambda: None)
    assert Validation.fail(['error']).to_lazy().unwarp_to_try() == Try(None)
    assert Validation.success([]).to_lazy().unwarp_to_try() == Try([])


# Generated at 2022-06-14 04:13:30.763224
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def func1():
        return 'x'

    def func2():
        return 'y'

    assert (Validation.success().to_lazy() ==
            Lazy(lambda: None))

    assert (Validation.success(2).to_lazy() ==
            Lazy(lambda: 2))

    # e.g. get from db
    lazy = Lazy(func1)

    assert (Validation.success(lazy).to_lazy().force(lazy) ==
            lazy.force(lazy))

    lazy = Lazy(func2)

    assert (Validation.success(lazy).to_lazy().force(lazy) ==
            lazy.force(lazy))


# Generated at 2022-06-14 04:13:35.057693
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail(['Error1']).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:13:39.227547
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Validation.success(1).to_lazy()
    assert Lazy(lambda: None) == Validation.fail([1]).to_lazy()


# Generated at 2022-06-14 04:13:42.148015
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy().force() == 1
    assert Validation.success(2).to_lazy().force() == 2
    assert Validation.success(3).to_lazy().force() == 3


# Generated at 2022-06-14 04:13:46.064525
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def square(x):
        return x * x

    assert_equals(Validation.success(2).to_lazy().fmap(square).value(), 4)
    assert_equals(Validation.fail([4]).to_lazy().fmap(square).value(), 4)

# Generated at 2022-06-14 04:13:50.535693
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail([1]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:13:53.006006
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(2).to_lazy() == Lazy(lambda: 2)



# Generated at 2022-06-14 04:14:03.671765
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test transform Validation to Lazy.
    """
    from pymonet import Lazy

    def not_lazy(value):
        assert False

    validation = Validation.success(1).to_lazy()
    assert isinstance(validation, Lazy)
    assert validation.value(not_lazy) == 1

### END OF Validation MONAD ###

# -------------------------------------------------------------------------------------------------

### Python built-in monads ###

import collections
import functools


# Generated at 2022-06-14 04:14:11.041728
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def trampoline(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            if isinstance(result, Lazy):
                return trampoline(result.run)
            return result
        return wrapper

    @trampoline
    def my_func(a, b):
        return Validation.success(a + b)

    assert my_func(1, 2) == 3


# Generated at 2022-06-14 04:14:15.213451
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    a = Validation.success().to_lazy()
    b = Lazy(lambda: None)

    assert a == b


# Generated at 2022-06-14 04:14:20.002185
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    # given
    validation_result = Validation(Success, [Error])

    # when
    lazy_result = validation_result.to_lazy()

    # then
    assert isinstance(lazy_result, Lazy)
    assert lazy_result.resolve() == Success

# Generated at 2022-06-14 04:14:27.432899
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    import pymonet.lazy as lazy

    val1 = Validation.success()
    val2 = Validation.fail(1)
    assert isinstance(val1.to_lazy(), lazy.Lazy)
    assert isinstance(val2.to_lazy(), lazy.Lazy)
    assert val2.to_lazy() == Lazy(lambda: None)
    assert val1.to_lazy().force() == None


# Generated at 2022-06-14 04:14:28.761436
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    actual = Validation.success(10).to_lazy()
    expected = Lazy(lambda: 10)
    assert actual == expected

# Generated at 2022-06-14 04:14:36.470828
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Success, Failure
    from pymonet.lazy import Lazy

    try_value = Try(10)
    assert Validation.success(try_value).to_lazy() == Lazy(lambda: Success(10))

    try_value = Try(None, is_success=False)
    assert Validation.success(try_value).to_lazy() == Lazy(lambda: Failure(None))


# Generated at 2022-06-14 04:14:40.667846
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert isinstance(Validation.success(1).to_lazy(), Lazy)
    assert isinstance(Validation.fail([]).to_lazy(), Lazy)
    assert Validation.success(1).to_lazy().value() == 1
    assert Validation.fail([]).to_lazy().value() is None
    assert Validation.success(1).to_lazy().value() == Validation.success(1).to_lazy().value()
    assert Validation.fail([]).to_lazy().value() == Validation.fail([]).to_lazy().value()


# Generated at 2022-06-14 04:14:45.056801
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(7).to_lazy() == Lazy(lambda: 7)
    assert Validation.fail(['some']).to_lazy() == Lazy(lambda: None)

# Unit tests for method to_try of class Validation

# Generated at 2022-06-14 04:14:52.268456
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    lazy_success = Validation.success('success').to_lazy()
    assert lazy_success == Lazy(lambda: 'success')

    lazy_fail = Validation.fail([1, 3, 'error']).to_lazy()
    assert lazy_fail == Lazy(lambda: None)


# Generated at 2022-06-14 04:15:00.811759
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(True).to_lazy().eval() == True
    assert Validation.success(None).to_lazy().eval() == None


# Generated at 2022-06-14 04:15:06.617705
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    assert Validation.success('success').to_lazy() == Lazy(lambda: 'success')
    assert Validation.fail(['fail']).to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 04:15:12.980337
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.typed import A, E, B

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail([1]).to_lazy() == Lazy(lambda: None)

    def to_lazy(val):
        return val.to_lazy()

    res = to_lazy.__annotations__
    assert res.get('return') == Lazy[B]
    assert res.get('val') == Validation[A, E]



# Generated at 2022-06-14 04:15:21.717732
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation
    from unittest_reinvent.support.asserts import assert_equal, assert_raises
    from unittest_reinvent.support.test_data import random_number

    value = random_number()
    lazy = Lazy(lambda: value)
    validation = Validation.success(value)

    assert_equal(lazy, validation.to_lazy())
    assert_equal(value, lazy.get())
    assert_equal(validation, lazy.to_validation())



# Generated at 2022-06-14 04:15:24.610143
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    validation = Validation.success(2)
    lazy = validation.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.run() == 2


# Generated at 2022-06-14 04:15:29.221066
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.validation import Validation
    from pymonet.lazy import Lazy

    assert Validation.fail(['not valid']).to_lazy() == Lazy(lambda: None)
    assert Validation.success('valid').to_lazy() == Lazy(lambda: 'valid')


# Generated at 2022-06-14 04:15:31.630500
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    result = Validation.fail().to_lazy()
    assert result.eval() is None

    result = Validation.success(1).to_lazy()
    assert result.eval() == 1


# Generated at 2022-06-14 04:15:34.661726
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation(None, []).to_lazy() == Lazy(lambda: None)
    assert Validation(1, []).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 04:15:36.168303
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success([1, 2]).to_lazy() == Lazy(lambda: [1, 2])
    assert Validation.fail().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:15:39.340672
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    It test to_lazy method for Validation class.
    """
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 'hello') == Validation.success('hello').to_lazy()


# Generated at 2022-06-14 04:15:49.253095
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    """
    Unit test to_lazy method of Validation.
    """
    from pymonet.lazy import Lazy

    def lazy_mapper(value):
        return Lazy(lambda: value*2)

    assert Validation.success(1).ap(lazy_mapper).value == Lazy(lambda: 2)

# Generated at 2022-06-14 04:15:58.923258
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation
    """

    assert Validation.success(2).to_lazy() == Validation.success(2).to_lazy(), 'Should be equals'
    assert Validation.fail(['error']).to_lazy() == Validation.fail(['error']).to_lazy(), 'Should be equals'
    assert Validation.success(2).to_lazy().map(lambda v: v + 1) == Lazy(lambda: 3), 'Should be equals'
    assert Validation.fail(['error']).to_lazy().map(lambda v: v + 1) == Lazy(lambda: None), 'Should be equals'


# Generated at 2022-06-14 04:16:06.177710
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():

    from pymonet.lazy import Lazy

    def foo():
        return 'bar'

    lazy_validation = Validation(foo, []).to_lazy()
    assert isinstance(lazy_validation, Lazy)
    assert lazy_validation() == 'bar'

    lazy_validation = Validation(foo, ['error']).to_lazy()
    assert isinstance(lazy_validation, Lazy)
    assert lazy_validation() == foo


# Generated at 2022-06-14 04:16:11.082943
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    # Test success
    value = 'success'
    validation = Validation.success(value)
    assert validation.value == value
    assert validation.is_success()
    assert validation.to_lazy() == Lazy(lambda: value)

    # Test failure
    value = 'fail'
    validation = Validation.fail(value)
    assert validation.value is None
    assert validation.is_fail()
    assert validation.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:16:15.306402
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def fn():
        return Validation.success(1)

    assert Validation.success(1).to_lazy() == Lazy(fn)


# Generated at 2022-06-14 04:16:19.531862
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.either import Left, Right
    from pymonet.lazy import Lazy

    assert Validation('test', []).to_lazy() == Lazy(lambda: 'test')
    assert Validation('test', ['error']).to_lazy() == Lazy(lambda: 'test')


# Generated at 2022-06-14 04:16:25.325817
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    assert Lazy(lambda: 'result') == Validation.success('result').to_lazy()
    assert Lazy(lambda: None) == Validation.fail(['error1']).to_lazy()

# Generated at 2022-06-14 04:16:30.793881
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation.
    Assert that Lazy monad has lazy value and can evaluated to value.
    """
    from pymonet.lazy import Lazy

    validation = Validation(10, [])
    assert validation.to_lazy() == Lazy(lambda: 10)
    assert validation.to_lazy().value() == 10



# Generated at 2022-06-14 04:16:41.161959
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def increment_or_none(value):
        return value + 1 if value is not None else None

    validation = Validation.success(100)

    def get_lazy_function():
        return validation.to_lazy().value()

    lazy_function = get_lazy_function()
    assert type(lazy_function) == Lazy
    assert lazy_function.value() == 100

    lazy_function = Lazy.of(increment_or_none).ap(get_lazy_function())
    assert type(lazy_function) == Lazy
    assert lazy_function.value() == 101

    validation = Validation.fail(['Error'])
    lazy_function = Lazy.of(increment_or_none).ap(get_lazy_function())

# Generated at 2022-06-14 04:16:45.391177
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert(Validation.success(('Hello', 'World')).to_lazy() == Lazy(lambda: ('Hello', 'World')))
    assert(Validation.fail(['Error!']).to_lazy() == Lazy(lambda: None))


# Generated at 2022-06-14 04:17:01.136834
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 04:17:03.935154
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test if Validation.to_lazy returns new Lazy monad with function returning Validation value
    """
    result = Validation.success(123).to_lazy()
    assert result.value() == 123


# Generated at 2022-06-14 04:17:11.853120
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.success('B').to_lazy() == Lazy(lambda: 'B')
    assert Validation.success(3.14).to_lazy() == Lazy(lambda: 3.14)
    assert Validation.success(True).to_lazy() == Lazy(lambda: True)
    assert Validation.success(None).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:17:21.309069
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.monad_try import Success
    from pymonet.monad_try import Failure
    from pymonet.lazy import Lazy


# Generated at 2022-06-14 04:17:25.228839
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    assert Validation.success(10).to_lazy() == Lazy(lambda: 10)


# Generated at 2022-06-14 04:17:32.773245
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Validation.success(42).to_lazy() == Lazy(lambda: 42)
    assert Validation.fail(['Error']).to_lazy() == Lazy(lambda: None)
    assert Validation.success(42).to_lazy().map(lambda x: x * 2) == Lazy(lambda: 42 * 2)

    assert Validation.success(42).to_lazy().flat_map(
        lambda x: Lazy(lambda: x * 2)) == Lazy(lambda: 42 * 2)
    assert Validation.fail(['Error']).to_lazy().flat_map(
        lambda x: Lazy(lambda: x * 2)) == Lazy(lambda: None)

    assert Validation.success

# Generated at 2022-06-14 04:17:41.362089
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.either import Left, Right
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    validation1 = Validation.fail([Left('Error01')])
    validation2 = Validation.fail([Right('Error01'), Right('Error02')])
    validation3 = Validation.success('Monad')
    validation4 = Validation.fail(Try(None, False))

    assert validation1.to_lazy() == Lazy(lambda: None)
    assert validation2.to_lazy() == Lazy(lambda: None)
    assert validation3.to_lazy() == Lazy(lambda: 'Monad')
    assert validation4.to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 04:17:44.931683
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.box import Box
    from pymonet.lazy import Lazy

    assert Validation.success(Box(1)).to_lazy() == Lazy(lambda: Box(1))
    assert Validation.fail([1, 2, 3]).to_lazy() == Lazy(lambda: None)

# Generated at 2022-06-14 04:17:47.017684
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    data = Validation.success(1)
    assert data.to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 04:17:52.330544
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation
    assert Lazy(lambda: 5) == Validation.success(5).to_lazy()
    assert Lazy(lambda: None) == Validation.fail([5]).to_lazy()


# Generated at 2022-06-14 04:18:10.085933
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    val = Lazy(lambda: 3).to_validation().to_lazy()

    assert (val.value() == 3)

# Generated at 2022-06-14 04:18:14.876281
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    plus_one = lambda x: x + 1
    placeholder = Lazy(plus_one)
    value = Validation.success(plus_one)
    assert type(placeholder) == type(value.to_lazy())
    assert placeholder.value() == value.to_lazy().value()

# Generated at 2022-06-14 04:18:18.614458
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test Validation.to_lazy method.
    """

    from pymonet.lazy import Lazy

    assert Validation.success('Hello').to_lazy() == Lazy(lambda: 'Hello')


# Generated at 2022-06-14 04:18:30.373548
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.exception import PymonetError

    # Validation to Lazy
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.success('test').to_lazy() == Lazy(lambda: 'test')
    assert Validation.success({'key': 'value'}).to_lazy() == Lazy(lambda: {'key': 'value'})
    assert Validation.success([]).to_lazy() == Lazy(lambda: [])
    assert Validation.success([1, 2, 3]).to_lazy() == Lazy(lambda: [1, 2, 3])

    # Validation to Try

# Generated at 2022-06-14 04:18:37.423440
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    success = Validation.success(1)
    assert isinstance(success.to_lazy(), Lazy)
    assert success.to_lazy().get() == 1

    failure = Validation.fail([Exception()])
    assert isinstance(failure.to_lazy(), Lazy)
    assert failure.to_lazy().get() is None


# Generated at 2022-06-14 04:18:41.112076
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    try:
        Validation.success('a').to_lazy()
        assert False
    except TypeError:
        pass

    assert Validation.success(2).to_lazy() == Lazy(lambda: 2)



# Generated at 2022-06-14 04:18:44.515535
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    def my_func():
        return 1 + 1

    lazy_validation = Validation.success(lazy_func)
    assert lazy_validation == Lazy(my_func)


# Generated at 2022-06-14 04:18:51.846922
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad import Monad

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail(1).to_lazy() == Lazy(lambda: None)

    assert Monad.is_instance_of(Validation.success(), Validation)
    assert Monad.is_instance_of(Validation.fail(), Validation)


# Generated at 2022-06-14 04:18:59.819880
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Checks whether to_lazy() returns a new Lazy instance with a function that returns the Validation value.

    :return: True if everything is ok, raises AssertionError otherwise
    :raises: AssertionError
    """
    from pymonet.lazy import Lazy
    validation = Validation.success(3)
    result = validation.to_lazy()
    assert isinstance(result, Lazy), \
        'Validation.to_lazy() should return a new Lazy instance'
    assert result() == 3, \
        'Lazy.force() should return the Validation value'


# Generated at 2022-06-14 04:19:03.612510
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def get_value():
        return 10

    value = Lazy(get_value)
    validation = Validation(value, [])
    assert value == validation.to_lazy()


# Generated at 2022-06-14 04:19:43.230937
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Validation.success('value').to_lazy() == Lazy(lambda: 'value')
    assert Validation.fail().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:19:46.565702
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy().value() == 1
    assert Validation.fail(['myerror']).to_lazy().value() is None


# Generated at 2022-06-14 04:19:50.687836
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    import lazy_test

    def validation_test_func():
        return Validation.success('test')

    assert Lazy.of(validation_test_func).to_validation() == Validation.success('test')

# Generated at 2022-06-14 04:19:56.154077
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try

    assert Try(9) == Validation.success(9).to_lazy().get()
    assert Try(None) == Validation.fail([1, 2, '3', 4]).to_lazy().get()

# Generated at 2022-06-14 04:19:58.569284
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(value=10).to_lazy() == Lazy(lambda: 10)
    assert Validation.fail(value=None, errors=['error1']).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:20:00.313954
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(3).to_lazy() == Lazy(lambda: 3)


# Generated at 2022-06-14 04:20:11.190025
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """Unit test for method to_lazy of class Validation"""

    def validate_int(value):
        from pymonet.either import Left, Right
        from pymonet.validation import Validation

        if not isinstance(value, int):
            return Validation.fail([
                'Value {} is not of type int'.format(value)
            ])
        return Validation.success(value)

    validation = validate_int('not int')

    def validate_positive(value):
        from pymonet.either import Left, Right
        from pymonet.validation import Validation

        if value <= 0:
            return Validation.fail([
                'Value {} is not positive'.format(value)
            ])
        return Validation.success(value)

    validation_positive = validation.ap(validate_positive)


# Generated at 2022-06-14 04:20:18.862599
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad import monad_unit
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe

    lazy = Validation.success(2).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy() == 2
    assert Validation.fail(['bad']).to_lazy().to_maybe() == Maybe.nothing()
    assert monad_unit(Validation, Lazy, 3).to_lazy() == Lazy(lambda: 3)


# Generated at 2022-06-14 04:20:21.397374
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy().value() == 1
    assert Validation.fail([]).to_lazy().value() is None


# Generated at 2022-06-14 04:20:23.989114
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Validation(5, []).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.get() == 5
