

# Generated at 2022-06-14 03:16:46.868636
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Left(1) != Right(1)
    assert not Left(1) == Right(1)
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)


# Generated at 2022-06-14 03:16:49.370987
# Unit test for method case of class Either
def test_Either_case():
    left = Left(1)
    right = Right(1)

    def error(x: int) -> bool:
        return False

    def success(x: int) -> bool:
        return True

    assert left.case(error, success) is False
    assert right.case(error, success) is True



# Generated at 2022-06-14 03:16:51.512138
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either(1).to_lazy().value() == 1

# Generated at 2022-06-14 03:16:55.402575
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    left = Left(1)
    right = Right(2)
    left_copy = Left(1)
    right_copy = Right(2)
    assert left != right
    assert left == left_copy
    assert right == right_copy


# Generated at 2022-06-14 03:16:58.564932
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # Test with right Either
    assert Right(10) == Right(10), 'Failed for Right Either'

    # Test with left Either
    assert Left('error') == Left('error'), 'Failed for Left Either'


# Generated at 2022-06-14 03:17:00.559550
# Unit test for method case of class Either
def test_Either_case():
    assert Left(1).case(lambda x: 'error', lambda x: 'success') == 'error'
    assert Right(1).case(lambda x: 'error', lambda x: 'success') == 'success'



# Generated at 2022-06-14 03:17:04.861439
# Unit test for method case of class Either
def test_Either_case():
    # given
    from pymonet.lazy import Lazy

    e = Either.Left(Lazy(lambda: 1 + 2))
    # and
    error_handler = lambda x: x + 10
    # and
    success_handler = lambda x: x + 20
    # when
    r = e.case(error_handler, success_handler)

    # then
    assert r == 13


# Generated at 2022-06-14 03:17:13.496945
# Unit test for method case of class Either
def test_Either_case():
    # Test for Left
    assert Left(-1).case(
        error=lambda x: x,
        success=lambda x: x
    ) == -1

    # Test for Right
    assert Right(1).case(
        error=lambda x: x,
        success=lambda x: x
    ) == 1


# Generated at 2022-06-14 03:17:25.624601
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # Given
    value = 'value'
    left = Left(value)
    right = Right(value)
    left_copy = Left(value)
    right_copy = Right(value)
    other_value = 'other value'
    other_left = Left(other_value)
    other_right = Right(other_value)

    # When
    left_eq_left = left == left
    left_eq_right = left == right
    left_eq_left_copy = left == left_copy
    left_eq_other_left = left == other_left
    right_eq_left = right == left
    right_eq_right = right == right
    right_eq_right_copy = right == right_copy
    right_eq_other_right = right == other_right
    right_eq_other_left = right

# Generated at 2022-06-14 03:17:30.752147
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Left(1) == Left(1)
    assert Left(1) != Left(2)
    assert Right(1) == Right(1)
    assert Left(1) != Right(1)
    assert Left(1) != 1



# Generated at 2022-06-14 03:17:37.088668
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

# Generated at 2022-06-14 03:17:52.239432
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    # test Lazy creation with Left
    left = Left(1)
    assert callable(left.to_lazy())
    assert left.to_lazy() == Lazy(lambda: 1)

    # test Lazy creation with Right
    right = Right(Maybe.just(2))
    assert callable(right.to_lazy())
    assert right.to_lazy() == Lazy(lambda: Maybe.just(2))

    # test Lazy creation with mapper
    assert callable(right.to_lazy(lambda x: Validation.success(x + 3)))

# Generated at 2022-06-14 03:17:57.036646
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Right

    result = Right(5).to_lazy()

    assert result == Lazy(lambda: 5)


# Generated at 2022-06-14 03:18:03.281064
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():

    left = Either.left(1)
    right = Either.right(2)

    assert isinstance(left.to_lazy(), Lazy)
    assert isinstance(right.to_lazy(), Lazy)

    assert left.to_lazy().force() == 1
    assert right.to_lazy().force() == 2



# Generated at 2022-06-14 03:18:10.927928
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # GIVEN
    either_left = Left(1)
    either_right = Right(2)

    # WHEN
    e_left_lazy = Left(1).to_lazy()
    e_right_lazy = Right(2).to_lazy()

    # THEN
    assert e_left_lazy.get() == either_left.value
    assert e_right_lazy.get() == either_right.value


# Generated at 2022-06-14 03:18:12.900890
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():

    assert Either(1).to_lazy() == 1



# Generated at 2022-06-14 03:18:17.535325
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Unit test for to_lazy method of Either class."""
    # when
    result = Left("Error").to_lazy()

    # then
    assert result.value() == "Error"

    # when
    result = Right("Result").to_lazy()

    # then
    assert result.value() == "Result"



# Generated at 2022-06-14 03:18:19.844222
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert (Right(1).to_lazy() == Lazy(lambda: 1))
    assert (Left(1).to_lazy() == Lazy(lambda: 1))



# Generated at 2022-06-14 03:18:25.406961
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Right

    def identity(value):
        return value

    assert Right(1).to_lazy() == Lazy(identity, 1)
    assert Right('string').to_lazy() == Lazy(identity, 'string')


# Generated at 2022-06-14 03:18:28.490537
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # Given
    from pymonet.box import Box
    box = Box(2)

    # When
    lazy = box.to_lazy()

    # Then
    assert lazy.get() == 2

# Generated at 2022-06-14 03:18:37.164295
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad import monad_to_lazy_test

    monad_to_lazy_test(lambda x: Either(x), lambda y: Right(y).to_lazy(), lambda y: Left(y).to_lazy(), lambda y: Lazy(lambda: y))


# Generated at 2022-06-14 03:18:40.037115
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Unit test for method to_lazy of class Either"""
    assert Right(1).to_lazy().force() == 1
    assert Left(1).to_lazy().force() == 1



# Generated at 2022-06-14 03:18:44.325599
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # Setup
    x = Right(5)

    # Exercise
    y = x.to_lazy()

    # Verify
    assert y.evaluate() == 5


# Generated at 2022-06-14 03:18:49.749266
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:18:57.956022
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # Either[T]
    assert Left(0).to_lazy() == Lazy(lambda: 0)
    assert Right(0).to_lazy() == Lazy(lambda: 0)
    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left(2).to_lazy() == Lazy(lambda: 2)
    assert Right(2).to_lazy() == Lazy(lambda: 2)
    # Either[List[T]]
    assert Left([0]).to_lazy() == Lazy(lambda: [0])
    assert Right([0]).to_lazy() == Lazy(lambda: [0])
    assert Left([1]).to_lazy() == Lazy(lambda: [1])


# Generated at 2022-06-14 03:18:59.318906
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    result = Right(2).to_lazy()
    assert isinstance(result, Lazy)



# Generated at 2022-06-14 03:19:06.010896
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Lazy(lambda: '1') == Right('1').to_lazy()
    assert Lazy(lambda: '1') == Left('1').to_lazy()
    assert Lazy(lambda: '1') == Try('1').to_lazy()
    assert Lazy(lambda: '1') == Try('1', is_success=False).to_lazy()



# Generated at 2022-06-14 03:19:24.115950
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Left, Right
    from pymonet.box import Box

    assert Left(1) == Lazy(lambda: Left(1)).value().case(error=lambda a: Left(a), success=lambda b: Right(b))
    assert Right(1) == Lazy(lambda: Right(1)).value().case(error=lambda a: Left(a), success=lambda b: Right(b))
    assert Box(1) == Lazy(lambda: Box(1)).value().case(error=lambda a: Left(a), success=lambda b: Right(b))



# Generated at 2022-06-14 03:19:26.684282
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    to_lazy = Either(1).to_lazy()

    assert to_lazy == Lazy(lambda: 1)


# Generated at 2022-06-14 03:19:37.823785
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.box import Box

    assert Lazy(lambda: Box(True)) == Either(Box(True)).to_lazy()
    assert Lazy(lambda: Box('True')) == Either(Box('True')).to_lazy()
    assert Lazy(lambda: Box(None)) == Either(Box(None)).to_lazy()
    assert Lazy(lambda: Right(Box(True))) == Either(Right(Box(True))).to_lazy()
    assert Lazy(lambda: Right(Box('True'))) == Either(Right(Box('True'))).to_lazy()
    assert Lazy(lambda: Right(Box(None))) == Either(Right(Box(None))).to_lazy()

# Generated at 2022-06-14 03:19:45.926184
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left('Error msg').to_lazy().force() == 'Error msg'
    assert Right(10).to_lazy().force() == 10
    assert Left(10).to_lazy().is_instance_of(Right)
    assert Right(10).to_lazy().is_instance_of(Right)

# Generated at 2022-06-14 03:19:49.452777
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left('2').to_lazy() == Lazy(lambda: '2')



# Generated at 2022-06-14 03:20:03.568786
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.box import Box
    from pymonet.lazy import Lazy

    assert Either(10).to_lazy().force() == Lazy(lambda: 10).force()
    assert Either(None).to_lazy().force() == Lazy(lambda: None).force()
    assert Either('test').to_lazy().force() == Lazy(lambda: 'test').force()
    assert Either(Box(10)).to_lazy().force() == Lazy(lambda: Box(10)).force()
    assert Either(Box('test')).to_lazy().force() == Lazy(lambda: Box('test')).force()
    assert Either(Lazy(lambda: 10)).to_lazy().force() == Lazy(lambda: Lazy(lambda: 10)).force()

# Generated at 2022-06-14 03:20:06.579956
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: '1') == Left(1).to_lazy()
    assert Lazy(lambda: '1') == Right(1).to_lazy()


# Generated at 2022-06-14 03:20:12.480023
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    import pytest

    right_instance = Right(1)
    lazy_right_instance = right_instance.to_lazy()

    left_instance = Left(1)
    lazy_left_instance = left_instance.to_lazy()
    assert isinstance(lazy_right_instance, lazy_left_instance.__class__)
    assert lazy_right_instance != lazy_left_instance

    assert isinstance(lazy_left_instance.to_lazy(), lazy_left_instance.__class__)
    assert lazy_left_instance.to_lazy() != lazy_left_instance


# Generated at 2022-06-14 03:20:23.187661
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Unit test for method to_lazy of class Either.

    :returns: nothing
    :rtype: None
    """
    from pymonet.lazy import Lazy
    from pymonet.monad_lazy import Value
    from pymonet.box import Box

    assert Right(23).to_lazy() == Lazy(lambda: 23)
    assert Left(23).to_lazy() == Lazy(lambda: Box(23).value)
    assert Left(23).to_lazy().value == Box(23).value
    assert Lazy(lambda: 33).value == Value(33)
    assert Left(23).to_lazy().value.get_value() == 23



# Generated at 2022-06-14 03:20:24.951491
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    lazy = Left(12).to_lazy()
    assert lazy.value() == 12

    lazy = Right(12).to_lazy()
    assert lazy.value() == 12


# Generated at 2022-06-14 03:20:27.166301
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Test if Eitther[A] is properly transformed to Lazy[Function() -> A]
    """
    from pymonet.lazy import Lazy

    assert Left("error").to_lazy() == Lazy(lambda: "error")
    assert Right("success").to_lazy() == Lazy(lambda: "success")


# Generated at 2022-06-14 03:20:32.765756
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left(2).to_lazy() == Lazy(lambda: 2)


# Generated at 2022-06-14 03:20:39.419662
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.box import Box

    box = Box(1)
    result = box.case(Lazy(lambda: 0), Lazy(lambda: 1))
    assert result == 1

    box = Box(0)
    result = box.case(Lazy(lambda: 0), Lazy(lambda: 1))
    assert result == 0

# Generated at 2022-06-14 03:20:51.872067
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Right, Left

    # Test for Right instances
    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Right(None).to_lazy() == Lazy(lambda: None)

    # Test for Left instances
    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Left(None).to_lazy() == Lazy(lambda: None)

    # Test with function as value
    assert Right(lambda: 2).to_lazy() == Lazy(lambda: 2)
    assert Left(lambda: 2).to_lazy() == Lazy(lambda: 2)


# Generated at 2022-06-14 03:21:01.166691
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.box import Box
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 'a').value() == Either('a').to_lazy().value()
    assert Lazy(lambda: 1).value() == Either(1).to_lazy().value()
    assert Lazy(lambda: []).value() == Either([]).to_lazy().value()
    assert Lazy(lambda: {}).value() == Either({}).to_lazy().value()
    assert Lazy(lambda: Box('a')).value() == Either(Box('a')).to_lazy().value()

# Generated at 2022-06-14 03:21:04.604973
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Left, Right

    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:21:08.588457
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    def _():
        return 1
    _right = Right(1)
    assert _right.to_lazy() == Lazy(_)


# Generated at 2022-06-14 03:21:10.638961
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left("test").to_lazy() == Lazy(lambda: "test")

# Generated at 2022-06-14 03:21:12.525860
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(1).to_lazy().call() == 1
    assert Left(1).to_lazy().call() == 1


# Generated at 2022-06-14 03:21:14.795736
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(1).to_lazy().eval() == 1
    assert Left(1).to_lazy().eval() == 1


# Generated at 2022-06-14 03:21:19.257242
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation

    result = Right(5).to_lazy()
    assert isinstance(result, Lazy)
    assert result.value() == 5

    result = Validation.success(5).to_lazy().map(lambda v: v + 5).flat_map(lambda v: Validation.success(v + 5))
    assert isinstance(result, Validation)



# Generated at 2022-06-14 03:21:22.486429
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(1).to_lazy().evaluate() == 1
    assert Right(1).to_lazy().evaluate() == 1


# Generated at 2022-06-14 03:21:26.406257
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    import pymonet.lazy as lazy

    assert Left(1).to_lazy() == lazy.Lazy(lambda: 1)
    assert Right(1).to_lazy() == lazy.Lazy(lambda: 1)

# Generated at 2022-06-14 03:21:39.771810
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either(1).to_lazy() == 1


# Generated at 2022-06-14 03:21:42.467960
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    either = Right(2)
    assert either.to_lazy().force() == 2
    either = Left(2)
    assert either.to_lazy().force() == 2


# Generated at 2022-06-14 03:21:47.095037
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from random import randint

    integer = randint(0, 100)
    either_instance = Right(integer)

    assert either_instance.to_lazy() == Lazy(lambda: integer)
    assert either_instance.to_lazy().force() == integer

    either_instance = Left(integer)

    assert either_instance.to_lazy() == Lazy(lambda: integer)
    assert either_instance.to_lazy().force() == integer


# Generated at 2022-06-14 03:21:50.437355
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    assert Either(42).to_lazy() == Lazy(lambda: 42)
    assert Left('Error').to_lazy() == Lazy(lambda: 'Error')
    assert Right(42).to_lazy() == Lazy(lambda: 42)


# Generated at 2022-06-14 03:21:57.487708
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(5).to_lazy() == Lazy(lambda: 5)
    assert Right(5).to_lazy().get() == 5
    # There is no way to make == for SameTypeComparator for Lazy monad with None value.
    # I can't call value() on None and can't imitate the behavior.
    # assert Left(None).to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:22:09.016878
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.box import Box
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    # test Either.to_lazy
    int_value = 1
    str_value = 'value'
    float_value = 1.0

    assert(Either(int_value).to_lazy().unit == int_value)
    assert(Either(str_value).to_lazy().unit == str_value)
    assert(Either(float_value).to_lazy().unit == float_value)

    # test Left.to_lazy
    assert(Left(int_value).to_lazy().unit == int_value)
    assert(Left(str_value).to_lazy().unit == str_value)

# Generated at 2022-06-14 03:22:10.599031
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:22:14.184883
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # Given
    from pymonet.lazy import Lazy

    value = 28
    either = Left(value)

    # When
    lazy = either.to_lazy()

    # Then
    assert isinstance(lazy, Lazy)
    assert lazy.get() == value



# Generated at 2022-06-14 03:22:17.191011
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Unit test for method to_lazy of class Either

    :return: None
    :rtype: None
    """
    e = Right(1)
    lazy = e.to_lazy()
    assert lazy.to_maybe().get() == 1



# Generated at 2022-06-14 03:22:22.350162
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Unit test for method to_lazy of class Either"""
    assert Right(13).to_lazy() == Lazy(lambda: 13)
    assert Left("error").to_lazy() == Lazy(lambda: "error")



# Generated at 2022-06-14 03:22:48.961337
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe

    assert Lazy(lambda: 42) == Right(42).to_lazy()

    assert Lazy(lambda: Maybe.just(42)) == Left(Maybe.nothing).to_lazy()

# Generated at 2022-06-14 03:22:54.936689
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    import unittest

    class TestEitherToLazy(unittest.TestCase):
        def test_Either_to_lazy(self):
            self.assertEqual(Left("Error message").to_lazy(), Lazy(lambda: "Error message"), "Should transform Either to Lazy")
            self.assertEqual(Right("Result").to_lazy(), Lazy(lambda: "Result"), "Should transform Either to Lazy")
    unittest.main()

# Generated at 2022-06-14 03:22:59.832199
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(3).to_lazy() == Lazy(lambda: 3)
    assert Left(3).to_lazy() == Lazy(lambda: 3)


# Generated at 2022-06-14 03:23:02.004108
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    monad = Right(5)
    monad2 = monad.to_lazy()
    assert monad2.__class__.__name__ == 'Lazy'
    assert monad2.value() == 5


# Generated at 2022-06-14 03:23:06.746585
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 2) == Either.right(2).to_lazy()
    assert Lazy(lambda: 2) == Either.left(2).to_lazy()

# Generated at 2022-06-14 03:23:09.786965
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    left = Left(None)
    right = Right(10)

    assert right.to_lazy() == Lazy(lambda: 10)
    assert left.to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:23:12.332765
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:23:16.440148
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(123).to_lazy() == Lazy(lambda: 123)
    assert Right(123).to_lazy() == Lazy(lambda: 123)


# Generated at 2022-06-14 03:23:19.652461
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(5).to_lazy() == Lazy(lambda: 5)
    assert Left(5).to_lazy() == Lazy(lambda: 5)


# Generated at 2022-06-14 03:23:24.164481
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert isinstance(Left(1).to_lazy(), Lazy)
    assert isinstance(Right(2).to_lazy(), Lazy)
    assert Either(1).to_lazy().eval() == 1
    assert Either(2).to_lazy().eval() == 2


# Generated at 2022-06-14 03:24:18.095960
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    actual = Either.to_lazy(Left(1))
    expected = Lazy(lambda: 1)
    assert actual.equals(expected)
    actual = Either.to_lazy(Right(1))
    expected = Lazy(lambda: 1)
    assert actual.equals(expected)



# Generated at 2022-06-14 03:24:29.132490
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.validation import Validation

    assert Either.case(Left(2),
                       lambda err: 'failed',
                       lambda suc: 'success'
                       ) == 'failed'

    assert Either.case(Right(2),
                       lambda _: 'failed',
                       lambda suc: 'success'
                       ) == 'success'

    assert Either.case(Left('error'),
                       lambda err: 'failed',
                       lambda suc: 'success'
                       ) == 'failed'

    assert Either.case(Right('suc'),
                       lambda _: 'failed',
                       lambda suc: 'success'
                       ) == 'success'

    assert Either.ap(Left(lambda x: x + 2), Right(3)) == Left(lambda x: x + 2)


# Generated at 2022-06-14 03:24:33.592028
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    _lazy = (lambda x: x * 2)  # noqa: E731

    assert Either(3).to_lazy() == Lazy(_lazy, 3)
    assert Either(1).to_lazy() == Lazy(_lazy, 1)
    assert Either(0).to_lazy() == Lazy(_lazy, 0)



# Generated at 2022-06-14 03:24:36.213782
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    assert Left("gg").to_lazy() == Lazy(lambda: "gg")
    assert Right("ff").to_lazy() == Lazy(lambda: "ff")


# Generated at 2022-06-14 03:24:45.503635
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # Given
    from pymonet.lazy import Lazy

    # test with Right Either
    img_url_either = Right('http://image.url')
    img_url_lazy = Lazy(lambda: 'http://image.url')

    # When
    result = img_url_either.to_lazy()

    # Then
    assert result == img_url_lazy

    # test with Left Either
    img_url_either = Left('http://image.url')
    img_url_lazy = Lazy(lambda: 'http://image.url')

    # When
    result = img_url_either.to_lazy()

    # Then
    assert result == img_url_lazy


# Generated at 2022-06-14 03:24:50.786218
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try, TryException

    assert Lazy(lambda: 'a') == Right('a').to_lazy()
    assert Lazy(lambda: TryException(KeyError)) == Left(TryException(KeyError)).to_lazy()



# Generated at 2022-06-14 03:24:55.932808
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    def add(x, y):
        return x + y

    def zero():
        return 0

    assert Right(5).to_lazy().map(zero).map(lambda x: add(x, 5)).eval() == Right(5).value
    assert Left(5).to_lazy().map(zero).map(lambda x: add(x, 5)).eval() == Left(5).value


# Generated at 2022-06-14 03:25:01.640049
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left('error').to_lazy() == Lazy(lambda: 'error')
    assert Right('success').to_lazy() == Lazy(lambda: 'success')


# Generated at 2022-06-14 03:25:15.154264
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 10) == Either(10).to_lazy()
    assert Lazy(lambda: 20) == Either(20).to_lazy()
    assert Lazy(lambda: 30) == Either(30).to_lazy()


# Generated at 2022-06-14 03:25:16.978004
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(10).to_lazy().force() == 10
    assert Right(10).to_lazy().force() == 10
