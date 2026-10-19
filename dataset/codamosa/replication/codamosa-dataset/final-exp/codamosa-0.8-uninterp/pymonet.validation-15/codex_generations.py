

# Generated at 2022-06-14 04:11:41.389921
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    import pytest

    # test for successful Validation
    success_validation = Validation.success(5)
    lazy = success_validation.to_lazy()

    # check lazy_result type
    assert isinstance(lazy.lazy_result, Lazy)
    assert isinstance(lazy.lazy_result.evaluated, Try)

    # check lazy_result value
    assert lazy.lazy_result.evaluated.value == 5
    assert lazy.lazy_result.evaluated.is_success
    assert lazy.lazy_result.evaluated.is_failure is False

    # test for failed Validation
    failed_validation = Validation.fail([42])

# Generated at 2022-06-14 04:11:45.057640
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail(1).to_lazy() == Lazy(lambda: None)


Validation.unit = Validation.success
Validation.zero = Validation.fail


# Generated at 2022-06-14 04:11:46.438585
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation(1, []).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 04:11:55.008865
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def lazy_Validation_value(x):
        def fn():
            return x
        return Lazy(fn)

    assert Validation.success(1).to_lazy() == lazy_Validation_value(1)
    assert Validation.fail([]).to_lazy() == lazy_Validation_value(None)
    assert Validation.fail(['error']).to_lazy() == lazy_Validation_value(None)
    assert Validation.fail([1]).to_lazy() == lazy_Validation_value(None)


# Generated at 2022-06-14 04:11:57.565462
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Lazy(lambda: 5) == Validation.success(5).to_lazy()
    assert Lazy(lambda: Try.success(5)) == Validation.success(5).to_lazy()



# Generated at 2022-06-14 04:12:02.480547
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.success(2).to_lazy() == Lazy(lambda: 2)
    assert Validation.fail([1]).to_lazy() == Lazy(lambda: None)
    assert Validation.fail([2]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:12:09.573844
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.success(1).to_lazy().get() == Validation.success(1).value
    assert Validation.fail([]).to_try() == Try(None, False)
    assert Validation.fail([]).to_try().is_success() == Validation.fail([]).is_success()


# Generated at 2022-06-14 04:12:14.957916
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.monad_maybe import Maybe
    from pymonet.monad_try import Try

    assert Validation.success(1).to_lazy().unwrap() == 1
    assert Validation.fail(1).to_lazy().unwrap() == None


# Generated at 2022-06-14 04:12:20.701761
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.fail().to_lazy() == Lazy(lambda: None)
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 04:12:27.058403
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    assert Validation.success(100).to_lazy() == Lazy(lambda: 100)
    assert Validation.success(100).to_lazy().value() == 100
    assert Validation.fail(['error_1']).to_lazy() == Lazy(lambda: None)
    assert Validation.fail(['error_1']).to_lazy().value() is None

# Generated at 2022-06-14 04:12:33.933567
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def validator(arg):
        return Validation.success(arg)

    # Given
    lazy_validation = validator(1).to_lazy()

    # Then
    assert lazy_validation == Lazy(lambda: 1)


# Generated at 2022-06-14 04:12:45.226909
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation.
    """
    from random import choice

    from pymonet.monad_try import Failure
    from pymonet.lazy import Lazy

    # Fail validation
    validation = Validation.fail(['one', 'two'])
    assert validation.to_lazy() == Lazy(lambda: Failure(validation))
    assert validation.to_lazy() == Lazy(lambda: validation)

    # Success Validation
    validation = Validation.success(choice(['one', 'two']))
    assert validation.to_lazy() == Lazy(lambda: validation.value)
    assert validation.to_lazy() == Lazy(lambda: validation)


# Generated at 2022-06-14 04:12:54.181679
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.box import Box
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    from pymonet.maybe import Maybe
    from pymonet.validation import Validation

    assert Validation.success(42).to_lazy() == Lazy(lambda: 42)
    assert Validation.fail(['my error']).to_lazy() == Lazy(lambda: None)

    assert Validation.success(42).to_box() == Box(42)
    assert Validation.fail(['my error']).to_box() == Box(None)

    assert Validation.success(42).to_maybe() == Maybe.just(42)
    assert Validation.fail(['my error']).to_maybe() == Maybe.nothing()


# Generated at 2022-06-14 04:13:01.566486
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def lazy_fn():
        return 15

    assert (Validation.success(lazy_fn).to_lazy() == Lazy(lambda: 15)), "Invalid Validation to Lazy mapping"
    assert (Validation.fail().to_lazy() == Lazy(lambda: None)), "Invalid Validation to Lazy mapping"

# Generated at 2022-06-14 04:13:10.452010
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.functor import fmap
    from pymonet.lazy import Lazy
    from pymonet.monad import Monad

    # Transformation to Lazy monad
    validation = Validation.success(1)
    lazy = validation.to_lazy()

    # Check validity of lazy monad
    assert isinstance(lazy, Lazy)
    assert fmap(OneToThree, lazy).run() == 3
    assert Monad.join(lazy).run() == 1

    # Check validity of validation after transformation
    assert validation.is_success()
    assert validation.value == 1
    assert validation.errors == []



# Generated at 2022-06-14 04:13:14.304932
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy
    import random

    val = random.randint(0, 100)
    validation = Validation(val, [])

    assert validation.to_lazy() == Lazy(lambda: val)


# Generated at 2022-06-14 04:13:17.210303
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    # Given:
    validation = Validation(42, [])

    # When:
    lazy_value = validation.to_lazy()

    # Then:
    assert isinstance(lazy_value, Lazy)
    assert lazy_value.get_value() == validation.value

# Generated at 2022-06-14 04:13:21.730578
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail([]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:13:26.896260
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(5).to_lazy() == Lazy(lambda: 5)
    assert Validation.fail(['error']).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:13:29.806193
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    fn = Validation.success(lambda x: x + 1) \
        .to_lazy \
        .value()

    assert fn(1) == 2


# Generated at 2022-06-14 04:13:36.123227
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert callable(Validation(1, []).to_lazy().value)
    assert Validation(1, []).to_lazy().value() == 1


# Generated at 2022-06-14 04:13:42.985605
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation
    import pytest

    with pytest.raises(AssertionError) as excinfo:
        Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert '==' in str(excinfo.value)

    with pytest.raises(AssertionError) as excinfo:
        Validation.fail([]).to_lazy() == Lazy(lambda: None)
    assert '==' in str(excinfo.value)


# Generated at 2022-06-14 04:13:50.339468
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Failure

    class Foo:
        def __init__(self, value):
            self.value = value

        def __eq__(self, other):
            return self.value == other.value

    with patch('pymonet.monad_try.Lazy') as Lazy:
        Lazy.return_value = Failure('exception')
        f = Foo(1)
        Validation.success(f).to_lazy()
        Lazy.assert_called_with(f)


# Generated at 2022-06-14 04:13:58.454915
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: None) == Validation.success().to_lazy()
    assert Lazy(lambda: []) == Validation.success([]).to_lazy()
    assert Lazy(lambda: 1) == Validation.success(1).to_lazy()
    assert Lazy(lambda: []) == Validation.fail().to_lazy()
    assert Lazy(lambda: []) == Validation.fail([]).to_lazy()
    assert Lazy(lambda: [1, 2, 3]) == Validation.fail([1, 2, 3]).to_lazy()


# Generated at 2022-06-14 04:14:02.301810
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    # Test empty list
    validation = Validation.success('hey')
    result = validation.to_lazy()
    assert result == Lazy(lambda : 'hey')

# Generated at 2022-06-14 04:14:12.641708
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Perform unit tests on Validation.to_lazy.
    """

    import unittest

    class TestValidationToLazy(unittest.TestCase):
        """
        Unit testing class for Validation.to_lazy.
        """

        def setUp(self):
            """
            Initialize shared data and instance.
            """

            self.x = 0
            self.validation = Validation.success(5)

        def test_result_is_lazy(self):
            self.assertIsInstance(self.validation.to_lazy(), Lazy)

        def test_result_is_lazy_with_correct_value(self):
            self.assertEqual(self.validation.to_lazy().map(lambda a: a).value(), 5)


# Generated at 2022-06-14 04:14:17.055718
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Asserts that method to_lazy of class Validation returns lazily evaluated value.
    """
    val = Validation.success('TEST')
    assert val.to_lazy().get() == 'TEST'

# Generated at 2022-06-14 04:14:22.009275
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def get_value():
        return "test"

    assert (Validation.success(get_value).to_lazy() == Lazy(get_value))
    assert (Validation.fail([]).to_lazy() == Lazy(None))


# Generated at 2022-06-14 04:14:25.225702
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.fail(['fail']).to_lazy().get() == None
    assert Validation.success(42).to_lazy().get() == 42


# Generated at 2022-06-14 04:14:30.717568
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Validation with value "a" and no errors can be transformed to Lazy monad that returns "a".

    :returns: True if test passes
    :rtype: Boolean
    """
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 'a') == Validation.success('a').to_lazy()
    return True


# Generated at 2022-06-14 04:14:38.686889
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 04:14:41.989096
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    actual = Validation.fail(["some error"]).to_lazy()
    expected = Lazy(lambda: None)
    assert actual == expected

# Generated at 2022-06-14 04:14:46.516588
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet import Validation
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    from pymonet.types import Success

    tmonad = Validation.success(10)
    lmonad = Lazy(lambda: 10)
    assert tmonad.to_lazy() == lmonad

# Generated at 2022-06-14 04:14:50.904204
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    l = Lazy(lambda: 10)
    assert Validation.success(10).to_lazy() == l
    assert Validation.fail([]).to_lazy().get() is None



# Generated at 2022-06-14 04:14:51.976447
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    pass



# Generated at 2022-06-14 04:14:56.641536
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    assert Validation.success(10).to_lazy() == Lazy(lambda: 10)
    assert Validation.fail(10).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:14:58.510445
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    val = Validation(1, [])
    assert val.to_lazy()._f() == 1


# Generated at 2022-06-14 04:15:03.210254
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.monad_try import Failure

    v = Validation.success(42).to_lazy()
    assert v.value() == 42

    v = Validation.fail(['error']).to_lazy()
    assert v.value() is None

# Generated at 2022-06-14 04:15:12.071122
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.success(1).to_lazy().value() == 1
    assert Validation.fail([Error('error')]).to_lazy() == Lazy(lambda: None)
    assert Validation.fail([Error('error')]).to_lazy().value() is None
    assert Validation.success(1).to_lazy().to_string() == 'Lazy[Function() -> 1]'
    assert Validation.fail([Error('error')]).to_lazy().to_string() == 'Lazy[Function() -> None]'



# Generated at 2022-06-14 04:15:16.606983
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail().to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:15:27.113326
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.monad_lazy import Lazy

    assert Validation.success(5).to_lazy() == Lazy(lambda: 5)
    assert Validation.fail([]).to_lazy() == Lazy(lambda: None)
    assert Validation.fail([1, 2]).to_lazy() == Lazy(lambda: None)
    assert Validation.fail([1, 2]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:15:33.105834
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail().to_lazy() == Lazy(lambda: None)

    # test with custom lambda
    assert Validation.success(lambda x: x+1).to_lazy().f()(1) == 2

    # test with function returning lambda
    def add_5(x):
        return lambda y: x + y

    assert Validation.success(add_5).to_lazy().f()(1) == 6



# Generated at 2022-06-14 04:15:35.728455
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    # When
    result = Validation([], []).to_lazy()

    # Then
    assert result == Lazy(lambda: [])


# Generated at 2022-06-14 04:15:43.779394
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from operator import add

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.success(10).map(lambda x: Lazy(lambda: add(x, x))).to_lazy().fmap(lambda x: x.force()) == 20
    assert Validation.fail([]).to_lazy() == Lazy(lambda: None)
    assert Validation.success(1).to_lazy().fmap(lambda x: add(x, x)) == Lazy(lambda: None)


# Generated at 2022-06-14 04:15:47.240386
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    a = Validation.fail(errors=['error'])
    assert a.to_lazy() == Lazy(lambda: a.value)

# Generated at 2022-06-14 04:15:50.425609
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    value = 3

    original_validation = Validation.success(value)

    lazy_result = original_validation.to_lazy()

    assert lazy_result.get() == value


# Generated at 2022-06-14 04:15:55.650180
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.success(None).to_lazy() == Lazy(lambda: None)
    assert Validation.fail([1, 2]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:15:58.509305
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def comp():
        return 5

    assert Validation(5, []).to_lazy() == Lazy(comp)



# Generated at 2022-06-14 04:16:05.752971
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    assert Lazy(lambda: 0) == Validation.success(0).to_lazy()
    assert Lazy(lambda: 1) == Validation.success(1).to_lazy()

    assert Lazy(lambda: None) == Validation.fail().to_lazy()
    assert Lazy(lambda: None) == Validation.fail(['error']).to_lazy()


# Generated at 2022-06-14 04:16:09.036523
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail(errors=[1, 2]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:16:27.920261
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation
    """
    from pymonet.monad_lazy import Lazy

    def _to_lazy():
        return Validation.fail().to_lazy()

    assert isinstance(_to_lazy(), Lazy)
    assert not _to_lazy().eval()


# Generated at 2022-06-14 04:16:32.701309
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test to_lazy method of Validation class.
    """
    from pymonet.lazy import Lazy
    from pymonet import Validation

    v1 = Validation.success(2)
    l1 = Lazy(lambda: 2)
    assert v1.to_lazy() == l1

    v2 = Validation.fail(4)
    l2 = Lazy(lambda: None)
    assert v2.to_lazy() == l2

# Generated at 2022-06-14 04:16:36.754539
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet import Lazy

    validation = Validation.success(1)
    lazy = validation.to_lazy()

    assert lazy.value() == 1
    assert lazy == Lazy(lambda: 1)



# Generated at 2022-06-14 04:16:41.552971
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success('OK').to_lazy().eval() == 'OK'

# Generated at 2022-06-14 04:16:46.475420
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    assert Validation.success(lambda: 2 + 2) == Validation.success(lambda: 2 + 2, []).to_lazy()
    assert Validation.fail(lambda: 2 + 2).to_lazy() == Lazy(2 + 2)

# Generated at 2022-06-14 04:16:50.524439
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Validation.success(1).to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.get() == 1


# Generated at 2022-06-14 04:16:56.934013
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    result = Validation.success(10).to_lazy()
    assert isinstance(result, Lazy) is True
    assert result.is_memoized() is False
    assert result.value() == 10

    result = Validation.fail('Validation fail!').to_lazy()
    assert isinstance(result, Lazy) is True
    assert result.is_memoized() is False
    try:
        result.value()
    except TypeError as e:
        assert str(e) == 'Validation fail!'



# Generated at 2022-06-14 04:17:01.471490
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    validation = Validation.success(value=5)
    assert validation.to_lazy() == Lazy(lambda: 5)

    validation = Validation.fail([])
    assert validation.to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 04:17:03.608755
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    import pymonet.lazy as lazy

    with Lazy(lambda: Validation.success(5)) as lazy_val:
        assert lazy_val == lazy.unit(5)

# Generated at 2022-06-14 04:17:08.065377
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    v = Validation.success(3)
    assert v.to_lazy() == Lazy(lambda: 3)

    v = Validation.fail([1, 2, 3])
    assert v.to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 04:17:37.315538
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Test that Validation.to_lazy returns Lazy with callable that returns Validation value.
    """
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 100) == Validation.success(100).to_lazy()


# Generated at 2022-06-14 04:17:39.631899
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    assert Validation.success(42).to_lazy() == Lazy(lambda: 42)
    assert Validation.fail([42, 23]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:17:43.236550
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy(): # pragma: no cover
    """
    Unit test for method to_lazy of class Validation
    """
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy(
    ) == Lazy(lambda: 1)
    assert Validation.fail(2).to_lazy(
    ) == Lazy(lambda: None)


# Generated at 2022-06-14 04:17:46.797414
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(15).to_lazy() == Lazy(lambda: 15)
    assert Validation.fail(["empty"]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:17:51.555381
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail([]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:17:54.667397
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe

    val = Validation.success('simple successful Validation')
    val.to_lazy() == Lazy(lambda: 'simple successful Validation')

    val = Validation.success(Maybe.just('simple successful Validation'))
    val.to_lazy() == Lazy(lambda: Maybe.just('simple successful Validation'))



# Generated at 2022-06-14 04:17:58.230397
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Validation.success(3).to_lazy() == Lazy(lambda: 3)
    assert Validation.fail().to_lazy() == Lazy(lambda: None)
    assert Validation.success("doc").to_lazy() == Lazy(lambda: 'doc')


# Generated at 2022-06-14 04:18:01.423318
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    def func():
        return 'value'

    validation = Validation.success('value')
    lazy = validation.to_lazy()

    assert lazy.get_value() == func()
    assert validation == lazy.get_monad()


# Generated at 2022-06-14 04:18:06.321955
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for method to_lazy of class Validation.
    """
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail([]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:18:14.056006
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.box import Box
    from pymonet.lazy import Lazy

    def test_success():
        lazy: Lazy[Box] = Validation.success(Box('yay!')).to_lazy()
        assert lazy.eval() == Box('yay!')

    def test_fail():
        lazy: Lazy[None] = Validation.fail(['boo :(']).to_lazy()
        assert lazy.eval() is None

    test_success()
    test_fail()


# Generated at 2022-06-14 04:19:15.585804
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy
    from pymonet.either import Left, Right
    from pymonet.maybe import Maybe
    from pymonet.box import Box

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail(['test']).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:19:18.074086
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    validation = Validation.success(value='value')
    assert validation.to_lazy().value() == 'value'


# Generated at 2022-06-14 04:19:21.022995
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    def f():
        return 1

    validation = Validation.success(1)
    assert validation.to_lazy() == Lazy(f)


# Generated at 2022-06-14 04:19:24.755428
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 42) == Validation.success(42).to_lazy()
    assert Lazy(lambda: None) == Validation.fail([]).to_lazy()



# Generated at 2022-06-14 04:19:34.135875
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    toml_content = '''
        [package]
        name = "pymonet"
        version = "0.0.1"
        authors = ["Anatoly Bubenkov <bubenkoff@gmail.com>"]
        '''

    lazy = Lazy(lambda: toml_content)
    try_ = Try.success(toml_content)

    try_content = lazy.bind(lambda content: Try.success(content.value)).value

    assert isinstance(try_content, Try)
    assert try_content.is_success()
    assert try_content == try_

# Generated at 2022-06-14 04:19:44.363504
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    """
    Unit test for to_lazy method of class Validation
    """

    from pymonet.lazy import Lazy

    def _to_lazy(x):
        return Lazy(lambda: x)

    assert Validation.success().to_lazy() == _to_lazy(None), 'Unit test for Validation to_lazy method has failed'
    assert Validation.success(1).to_lazy() == _to_lazy(1), 'Unit test for Validation to_lazy method has failed'
    assert Validation.fail([]).to_lazy() == _to_lazy(None), 'Unit test for Validation to_lazy method has failed'

# Generated at 2022-06-14 04:19:48.368079
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail(['error']).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:19:51.764059
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Validation.success(1).to_lazy() == Lazy(lambda: 1)
    assert Validation.fail([1]).to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 04:19:57.038831
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.monad_lazy import Lazy

    assert Try.of('str').to_lazy() == Lazy(lambda: 'str')
    assert Try.fail([]).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 04:20:01.241544
# Unit test for method to_lazy of class Validation
def test_Validation_to_lazy():  # pragma: no cover
    from pymonet.lazy import Lazy

    assert Validation.success(4).to_lazy() == Lazy(lambda: 4)
    assert Validation.fail([1, 3, 3]).to_lazy() != Lazy(lambda: 4)
