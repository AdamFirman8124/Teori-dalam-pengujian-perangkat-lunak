

# Generated at 2022-06-14 03:16:47.337940
# Unit test for method case of class Either
def test_Either_case():
    assert(Left(10).case(error=lambda x: x + 1, success=lambda x: x * 10) == 11)
    assert(Right(5).case(error=lambda x: x + 1, success=lambda x: x * 10) == 50)



# Generated at 2022-06-14 03:16:51.353492
# Unit test for method case of class Either
def test_Either_case():
    assert Left(3).case(lambda x: x + 1, lambda x: x) == 4
    assert Right(3).case(lambda x: x + 1, lambda x: x) == 3


# Generated at 2022-06-14 03:17:01.330506
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Left(1) == Left(1)
    assert Left(2) == Left(2)
    assert Left(3) == Left(3)

    assert Right(1) == Right(1)
    assert Right(2) == Right(2)
    assert Right(3) == Right(3)

    assert Left(1) != Right(1)
    assert Left(2) != Right(2)
    assert Left(3) != Right(3)

    assert Left(1) != None
    assert Left(2) != None
    assert Left(3) != None

    assert Right(1) != None
    assert Right(2) != None
    assert Right(3) != None

    assert None != Left(1)
    assert None != Left(2)
    assert None != Left(3)

    assert None != Right(1)
   

# Generated at 2022-06-14 03:17:04.387004
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either(4).to_lazy() == Lazy(lambda: 4)
    assert Right(4).to_lazy() == Lazy(lambda: 4)
    assert Left(4).to_lazy() == Lazy(lambda: 4)


# Generated at 2022-06-14 03:17:11.818538
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from nose.tools import assert_equal
    from pymonet.lazy import Lazy

    assert_equal(Right(1).to_lazy(), Lazy(lambda: 1))
    assert_equal(Left(1).to_lazy(), Lazy(lambda: 1))



# Generated at 2022-06-14 03:17:20.058662
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    from pymonet.monad_try import Try

    assert Right(1) == Right(1)
    assert Left(1) == Left(1)
    assert Right(1) != Left(1)
    assert Right(1) != Right(2)
    assert Left(1) != Left(2)
    assert Right(1) != None
    assert Right(1) != True
    assert Right(1) != Try.success(1)
    assert Right(1) != Try.fail(1)



# Generated at 2022-06-14 03:17:22.593284
# Unit test for method case of class Either
def test_Either_case():
    """
    >>> assert Right(2).case(lambda _: "error", lambda _: "success") == "success"
    >>> assert Left(2).case(lambda _: "error", lambda _: "success") == "error"
    """


# Generated at 2022-06-14 03:17:34.261321
# Unit test for method case of class Either
def test_Either_case():
    def error_handler(error):
        return 'error'

    def success_handler(success):
        return 'success'

    assert Either(Either(None)).case(error_handler, success_handler) == 'error'
    assert Either(Either(Any())).case(error_handler, success_handler) == 'error'
    assert Either(Either(1)).case(error_handler, success_handler) == 'error'

    assert Either(Right(None)).case(error_handler, success_handler) == 'success'
    assert Either(Right(Any())).case(error_handler, success_handler) == 'success'
    assert Either(Right(1)).case(error_handler, success_handler) == 'success'

# Generated at 2022-06-14 03:17:38.753549
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    def add(x, y):
        return x + y

    assert Right(add).to_lazy()(2, 3) == 5
    assert Left(add).to_lazy()(2, 3) == add



# Generated at 2022-06-14 03:17:43.118928
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Left(1) == Left(1)
    assert Left(1) != Left(2)
    assert Right(1) == Right(1)
    assert Right(1) != Right(2)
    assert Left(1) != Right(1)
    assert Right(1) != Left(1)


# Generated at 2022-06-14 03:17:53.438852
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # __eq__ is not implemented in Either
    assert NotImplemented == Either(1) == Either(1)

    assert Left(1) == Left(1)
    assert NotImplemented == Left(1) == Right(1)
    assert Left(1) != Right(1)
    assert NotImplemented != Left(1) != Right(1)
    assert NotImplemented == Right(1) == Left(1)

    assert Right(1) == Right(1)
    assert Right(1) != Left(1)
    assert NotImplemented != Right(1) != Left(1)


# Generated at 2022-06-14 03:17:56.074041
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Either(None) != object()
    assert Either(None) == Either(None)



# Generated at 2022-06-14 03:18:01.699097
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Left(12) == Left(12)
    assert Left(12) != Left(11)
    assert Right(12) == Right(12)
    assert Right(12) != Right(11)
    assert Left(12) != Right(12)
    assert Left(11) != Right(11)

# Generated at 2022-06-14 03:18:09.634341
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    left_1 = Left(1)
    left_2 = Left(2)
    right_1 = Right(1)
    right_2 = Right(2)
    assert left_1 == left_1
    assert right_1 == right_1
    assert left_1 != right_1
    assert right_1 != left_1
    assert left_1 != left_2
    assert right_1 != right_2



# Generated at 2022-06-14 03:18:13.150510
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    func = lambda x: x * 2
    e = Either(func)
    e1 = Either(func)
    assert e == e1

# Generated at 2022-06-14 03:18:17.773906
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Left('a') == Left('a')
    assert Right(42) == Right(42)
    assert Left('a') != Right('a')
    assert Right(42) != Left(42)
    assert Left('a') != Right(42)
    assert Left(42) != Right('a')
    # and so on...


# Generated at 2022-06-14 03:18:28.680607
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    """
    Uit test for method __eq__ of class Either

    :returns: True if test passes, False if not
    :rtype: Boolean
    """
    from pymonet.box import Box
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    from pymonet.maybe import Maybe
    from pymonet.validation import Validation

    assert Left("Hello") == Left("Hello")
    assert not Left("Hello") == Left("World")
    assert not Left("Hello") == Right("Hello")
    assert not Left("Hello") == Box("Hello")
    assert not Left("Hello") == Lazy(lambda: "Hello")
    assert not Left("Hello") == Try("Hello", True)
    assert not Left("Hello") == Maybe("Hello")

# Generated at 2022-06-14 03:18:30.226188
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Left(1) == Left(1)
    assert Right(1) == Right(1)



# Generated at 2022-06-14 03:18:40.827373
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    left_1 = Left(1)
    left_2 = Left(2)
    right_1 = Right(1)
    right_2 = Right(2)

    assert left_1 == left_1
    assert left_2 == left_2

    assert right_1 == right_1
    assert right_2 == right_2

    assert not left_1 == left_2
    assert not left_2 == left_1

    assert not right_1 == right_2
    assert not right_2 == right_1

    assert not right_1 == left_1
    assert not left_1 == right_1

    assert not right_2 == left_2
    assert not left_2 == right_2



# Generated at 2022-06-14 03:18:51.938423
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Lazy(lambda: 1) == Either.right(1).to_lazy()

    assert Lazy(lambda: TypeError) == Either.left(TypeError).to_lazy()

    assert Lazy(lambda: 1) == Try.success(1).to_lazy()

    assert Lazy(lambda: TypeError) == Try.fail(TypeError).to_lazy()

    assert Lazy(lambda: TypeError) == Try.fail(TypeError).to_lazy()



# Generated at 2022-06-14 03:18:56.926053
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    instance = Either.to_lazy(Right(3))

    assert callable(instance.value)
    assert instance.value() == 3
    assert isinstance(instance.value(), int)

    assert callable(instance.value)

# Generated at 2022-06-14 03:19:06.421341
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try

    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)

    assert Left(1).to_lazy().map(lambda x: x + 1) == Lazy(lambda: 2)
    assert Right(1).to_lazy().map(lambda x: x + 1) == Lazy(lambda: 2)

    assert Left(1).to_lazy().ap(Lazy(lambda: lambda x: x + 1)) == Lazy(lambda: 2)

# Generated at 2022-06-14 03:19:14.879498
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    import pytest

    def test_left():
        left = Left(0)
        assert left.to_lazy() == Lazy(lambda: left.value)
        pytest.raises(AttributeError, lambda: left.to_lazy.value)

    def test_right():
        right = Right(0)
        assert right.to_lazy() == Lazy(lambda: right.value)
        pytest.raises(AttributeError, lambda: right.to_lazy.value)

    test_left()
    test_right()


# Generated at 2022-06-14 03:19:20.556931
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:19:25.171465
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(1).computed_value() == Right(1).to_lazy().computed_value()
    assert Lazy(1).computed_value() == Left(1).to_lazy().computed_value()



# Generated at 2022-06-14 03:19:43.615964
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # Given
    from pymonet.lazy import Lazy
    from random import randint
    value = randint(1, 100)
    right = Right(value)
    right_lazy = Lazy(lambda: value)
    left = Left(value)
    left_lazy = Lazy(lambda: value)

    # When
    right_result = right.to_lazy()
    left_result = left.to_lazy()

    # Then
    assert isinstance(right_result, Lazy)
    assert isinstance(left_result, Lazy)
    assert right.value == right_lazy.value()
    assert left.value == left_lazy.value()


# Generated at 2022-06-14 03:19:46.510193
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert (Either.to_lazy(Right(2)) == Lazy(lambda: 2)), 'Either to_lazy Right should return Lazy monad'
    assert (Either.to_lazy(Left('abc')) == Lazy(lambda: 'abc')), 'Either to_lazy Left should return Lazy monad'


# Generated at 2022-06-14 03:19:55.399150
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    import unittest

    from pymonet.monad_try import Try
    from pymonet.box import Box
    from pymonet.lazy import Lazy

    class EitherToLazyTest(unittest.TestCase):
        def test(self):
            self.assertEqual(Right(True).to_lazy(), Lazy(lambda: True))
            self.assertEqual(Left(False).to_lazy(), Lazy(lambda: False))
            self.assertEqual(Right(Box(True)).to_lazy(), Lazy(lambda: Box(True)))
            self.assertEqual(Right(Try(Box(True))).to_lazy(), Lazy(lambda: Try(Box(True))))

    unittest.main()


# Generated at 2022-06-14 03:19:59.927908
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation, SuccessfulValidation, FailedValidation
    assert isinstance(Right(4).to_lazy(), Lazy)
    assert Right(4).to_lazy().value() == 4
    assert Left(4).to_lazy().value() == 4


# Generated at 2022-06-14 03:20:01.310065
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Unit test for method to_lazy of class Either"""

    Either.to_lazy()


# Generated at 2022-06-14 03:20:06.724525
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    left = Left(1)
    right = Right(2)
    assert left.to_lazy() == Lazy(lambda: 1)
    assert right.to_lazy() == Lazy(lambda: 2)


# Generated at 2022-06-14 03:20:09.396562
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 2) == Left(2).to_lazy()
    assert Lazy(lambda: 3) == Right(3).to_lazy()


# Generated at 2022-06-14 03:20:15.231624
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(2).to_lazy() == Lazy(lambda : 2)
    assert Left("Left string").to_lazy() == Lazy(lambda: "Left string")


# Generated at 2022-06-14 03:20:19.132198
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert isinstance(Either.to_lazy(Right(1)), Lazy)
    assert isinstance(Either.to_lazy(Left(1)), Lazy)



# Generated at 2022-06-14 03:20:24.127036
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    import pytest

    @pytest.mark.parametrize('either, result', [
        (Left('error'), 'error'),
        (Right(42), 42),
    ])
    def to_lazy(either, result):
        assert either.to_lazy().eval() == result

# Generated at 2022-06-14 03:20:26.194169
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    either = Right(1)
    assert either.to_lazy().get() == 1



# Generated at 2022-06-14 03:20:32.262708
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Lazy(lambda: Try(3.14)) == Lazy(lambda: Try(3.14)).to_lazy()

# Generated at 2022-06-14 03:20:37.574875
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert isinstance(Right(4).to_lazy(), type(Lazy(lambda: 4)))
    assert isinstance(Left("error").to_lazy(), type(Lazy(lambda: "error")))



# Generated at 2022-06-14 03:20:46.774696
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():

    # Test for method to_lazy of class Left
    def test_Left_to_lazy():
        assert Left(1).to_lazy().execute() == 1

    # Test for method to_lazy of class Right
    def test_Right_to_lazy():
        assert Right(1).to_lazy().execute() == 1

    # Run test for method to_lazy of class Left
    test_Left_to_lazy()

    # Run test for method to_lazy of class Right
    test_Right_to_lazy()


# Generated at 2022-06-14 03:20:51.871390
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    left = Left(1)

    assert left.to_lazy() == Lazy(lambda: 1)

    right = Right(1)

    assert right.to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:20:57.690196
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Test is Either to_lazy work correctly
    """
    from pymonet.lazy import Lazy

    result = Left(10).to_lazy()
    assert result == Lazy(lambda: 10)
    assert result() == 10

    result = Right(10).to_lazy()
    assert result == Lazy(lambda: 10)
    assert result() == 10


# Generated at 2022-06-14 03:21:02.116785
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Left
    from pymonet.either import Right

    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:21:04.794677
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    def test_function(value):
        return value

    assert Lazy(lambda: test_function(5)) == Left(5).to_lazy()


# Generated at 2022-06-14 03:21:11.938305
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.box import Box
    from pymonet.monad_try import Try

    assert Right(4).to_lazy() == Lazy(lambda: 4)
    assert Left('error').to_lazy() == Lazy(lambda: 'error')
    assert Right(4).to_box() == Box(4)
    assert Left('error').to_try() == Try('error', is_success=False)



# Generated at 2022-06-14 03:21:16.522459
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    '''
    assert that Lazy monad created with value contained in Right will return the same value when call get method
    assert that Lazy monad created with value contained in Left will return the same value when call get method
    '''
    assert Right(1).to_lazy().get() == 1
    assert Left(1).to_lazy().get() == 1


# Generated at 2022-06-14 03:21:18.945083
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:21:24.751971
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    We want to verify that to_lazy on Either returns Lazy monad with lambda returning previous value.

    :returns: AssertionError if values are different, nothing if they are the same.
    """
    from pymonet.lazy import Lazy

    assert Right(5).to_lazy() == Lazy(lambda: 5)
    assert Left(5).to_lazy() == Lazy(lambda: 5)



# Generated at 2022-06-14 03:21:26.613703
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(2).to_lazy().evaluate() == 2

# Unit tests for method to_try of class Either

# Generated at 2022-06-14 03:21:27.542488
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():

    def func():
        return 3

    right = Right(func).to_lazy()

    assert right.eval() == 3



# Generated at 2022-06-14 03:21:29.828634
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    assert Lazy(lambda: 1) == Either(1).to_lazy()


# Generated at 2022-06-14 03:21:35.565564
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left(2).to_lazy() == Lazy(lambda: 2)


# Generated at 2022-06-14 03:21:37.192808
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    actual = Right(3).to_lazy()
    expected = 3
    assert actual == expected


# Generated at 2022-06-14 03:21:41.971175
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    x = Right(5)
    y = x.to_lazy()
    assert y._get_value() == 5

    x = Left(5)
    y = x.to_lazy()
    assert y._get_value() == 5

# Generated at 2022-06-14 03:21:43.556935
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    lazy_either = Either(2).to_lazy()

    assert lazy_either.force() == 2


# Generated at 2022-06-14 03:21:50.036174
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Should transform Either to Lazy.

    :returns: Nothing
    :rtype: None
    """
    from pymonet.lazy import Lazy

    assert Either(1).to_lazy() == Lazy(lambda: 1), 'Should be equal to Lazy(lambda: 1)'

    assert Either(1).to_lazy().value() == 1, 'Should be equal to 1'

    assert Either(1).to_lazy().is_same(Lazy(lambda: 1)), 'Should be equal to Lazy(lambda: 1)'

    assert Either(1).to_lazy() == Either(1).to_lazy(), 'Should be equal to Each other'



# Generated at 2022-06-14 03:21:56.067512
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either.to_lazy(Right(1)).eval() == 1, 'Right(1).to_lazy().eval() == 1'
    assert Either.to_lazy(Left(1)).eval() == 1, 'Left(1).to_lazy().eval() == 1'


# Generated at 2022-06-14 03:22:10.969893
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Unit test for method to_lazy of class Either."""
    from pymonet.lazy import Lazy

    lazy = Lazy(lambda: 1 + 1)
    right = Right(2)
    left = Left(1)
    assert right.to_lazy() == lazy
    assert left.to_lazy() == lazy

# Generated at 2022-06-14 03:22:14.237379
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: Either.right(2).value) == Either.right(2).to_lazy()
    assert Lazy(lambda: Either.left(3).value) == Either.left(3).to_lazy()

# Generated at 2022-06-14 03:22:15.461259
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:22:18.204826
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:22:27.798598
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(1).to_lazy().evaluate() == 1
    assert Left(1).to_lazy().evaluate() == 1


# Generated at 2022-06-14 03:22:32.391820
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either(5).to_lazy() == Lazy(lambda: 5)
    assert Either('test').to_lazy() == Lazy(lambda: 'test')


# Generated at 2022-06-14 03:22:35.199546
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert isinstance(Either.to_lazy(Right(5)), Lazy)
    assert isinstance(Either.to_lazy(Left(5)), Lazy)

# Generated at 2022-06-14 03:22:37.908798
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    import pytest
    from pymonet.lazy import Lazy

    def test(value):
        def func():
            return value

        return func

    assert Right(1).to_lazy() == Lazy(test(1))
    assert Left(1).to_lazy() == Lazy(test(1))


# Generated at 2022-06-14 03:22:42.941142
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.box import Box
    assert Right(None).to_lazy() == Left(None).to_lazy()
    assert Right(None).to_lazy().get() is None
    assert Right(0).to_lazy() == Left(None).to_lazy().map(lambda _: 0)
    assert Right(0).to_lazy() == Try(None).to_lazy().map(lambda _: 0)
    assert Right(0).to_lazy() == Box(None).to_lazy().map(lambda _: 0)
    assert Right(Right(0)).to_maybe() == Left(None).to_maybe().bind(lambda _: 0)
    success = Try(0)

# Generated at 2022-06-14 03:22:50.265161
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either(10).to_lazy() == Lazy(lambda: 10)
    assert Either(-10).to_lazy() == Lazy(lambda: -10)
    assert Either('qwerty').to_lazy() == Lazy(lambda: 'qwerty')
    assert Either(True).to_lazy() == Lazy(lambda: True)
    assert Either(None).to_lazy() == Lazy(lambda: None)



# Generated at 2022-06-14 03:22:53.406716
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Either

    assert Either.to_lazy(Left('Value')) == Lazy(None)
    assert Either.to_lazy(Right('Value')) == Lazy(lambda: 'Value')


# Generated at 2022-06-14 03:22:57.117056
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    lazy = Right(10).to_lazy()

    assert isinstance(lazy, Lazy)
    assert isinstance(lazy.eval(), int)
    assert lazy.eval() == 10

# Generated at 2022-06-14 03:23:03.933403
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy._unit(Left(1)).to_lazy() == Lazy._unit(Left(1))
    assert Lazy._unit(Right(1)).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:23:08.497198
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():

    assert isinstance(Either(3).to_lazy(), Lazy)
    assert isinstance(Left(3).to_lazy(), Lazy)
    assert isinstance(Right(3).to_lazy(), Lazy)
    assert Either(3).to_lazy().get() == 3
    assert Left(3).to_lazy().get() == 3
    assert Right(3).to_lazy().get() == 3



# Generated at 2022-06-14 03:23:27.202424
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(123).to_lazy().value() == 123
    assert Left(123).to_lazy().value() == 123


# Generated at 2022-06-14 03:23:31.544881
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    value = 'test'
    right_instance = Right(value)
    left_instance = Left(value)
    lazy_value = Lazy(lambda: value)

    assert right_instance.to_lazy() == lazy_value
    assert left_instance.to_lazy() == lazy_value


# Generated at 2022-06-14 03:23:36.965155
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    def test_method():
        from pymonet.lazy import Lazy

        return Either.to_lazy(Either.unit(123)) == Lazy(lambda : 123)

    assert test_method()



# Generated at 2022-06-14 03:23:43.645208
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.box import Box
    import pytest

    assert Either(Lazy(lambda: 3)).to_lazy() == Lazy(lambda: 3)
    assert Either(Box(4)).to_lazy() == Lazy(lambda: 4)

    with pytest.raises(TypeError):
        Either(1).to_lazy()


# Generated at 2022-06-14 03:23:58.779677
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either(10).to_lazy() == Lazy(lambda: 10)
    assert Either('Hello, world!').to_lazy() == Lazy(lambda: 'Hello, world!')
    assert Either({1, 2, 3, 4}).to_lazy() == Lazy(lambda: {1, 2, 3, 4})


# Generated at 2022-06-14 03:24:01.009783
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(1).to_lazy() == Lazy(lambda: 1) and\
        Right(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:24:03.781527
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Unit test for method to_lazy of class Either
    """
    assert Either(1).to_lazy().force() == 1
    assert Either(None).to_lazy().force() is None


# Generated at 2022-06-14 03:24:06.142931
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # arrange
    right_value = Right('Right value')

    # act
    lazy = right_value.to_lazy()

    # assert
    assert lazy.get() == 'Right value'



# Generated at 2022-06-14 03:24:07.874384
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(12).to_lazy() == Lazy(lambda: 12)
    assert Right(12).to_lazy() == Lazy(lambda: 12)



# Generated at 2022-06-14 03:24:14.494781
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Left(2).to_lazy() == Lazy(lambda: 2)
    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Right(3).to_lazy() == Lazy(lambda: 3)


# Generated at 2022-06-14 03:24:54.049215
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    from pymonet.box import Box

    for element in [Left(1), Right(1)]:
        lazy = element.to_lazy()
        assert isinstance(lazy, Lazy)
        assert element.value == lazy.get()



# Generated at 2022-06-14 03:24:57.259427
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either.Right(4).to_lazy() == Lazy(lambda: 4)
    assert Either.Left('error').to_lazy() == Lazy(lambda: 'error')

# Generated at 2022-06-14 03:24:59.008524
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Either(1).to_lazy()



# Generated at 2022-06-14 03:25:00.151884
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert None == None # TODO: implement test

# Generated at 2022-06-14 03:25:04.588379
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either(5).to_lazy() == Lazy(lambda: 5)
    assert Either('5').to_lazy() == Lazy(lambda: '5')


# Generated at 2022-06-14 03:25:06.963202
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:25:10.334541
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    import pytest
    from pymonet.lazy import Lazy

    either = Right(4).to_lazy()
    assert isinstance(either, Lazy)
    assert either.value() == 4


# Generated at 2022-06-14 03:25:17.169117
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Unit test for method to_lazy of class Either

    :return: None
    :rtype: None
    """
    assert Right(1).to_lazy().eval() == 1
    assert Left(1).to_lazy().eval() == 1



# Generated at 2022-06-14 03:25:25.557484
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Right
    from pymonet.either import Left

    value = Right(1).to_lazy().value()
    assert value == 1

    value = Right(None).to_lazy().value()
    assert value is None

    value = Right(False).to_lazy().value()
    assert value is False

    value = Right([1, 2, 3]).to_lazy().value()
    assert value == [1, 2, 3]

    value = Left(1).to_lazy().value()
    assert value == 1

    value = Left(None).to_lazy().value()
    assert value is None

    value = Left(False).to_lazy().value()
    assert value is False


# Generated at 2022-06-14 03:25:29.882104
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Lazy(lambda: 5)

    assert lazy.value == 5
