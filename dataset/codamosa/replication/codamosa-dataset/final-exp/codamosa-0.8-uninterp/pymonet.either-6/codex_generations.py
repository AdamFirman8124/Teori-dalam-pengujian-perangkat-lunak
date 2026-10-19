

# Generated at 2022-06-14 03:16:42.249060
# Unit test for method __eq__ of class Either
def test_Either___eq__():

    assert Right(1) == Right(1)
    assert Left(1) == Left(1)
    assert Left(1) != Right(1)


# Generated at 2022-06-14 03:16:44.016835
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Unit test for method to_lazy of class Either"""

    def f():
        return 1

    assert Right(f).to_lazy() == Lazy(f)
    assert Left(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:16:50.764602
# Unit test for method case of class Either
def test_Either_case():
    from pymonet.functor import Functor

    def either_equal(left: Either[int], right: Either[int]) -> bool:
        return left.case(
            error=lambda v: right.case(error=lambda v_: v == v_, success=lambda _: False),
            success=lambda v: right.case(error=lambda _: False, success=lambda v_: v == v_))

    def test_case_True() -> bool:
        return either_equal(Left(1), Right(1)).case(error=lambda: False, success=lambda: True)

    assert test_case_True() == False

    def test_case_False() -> bool:
        return either_equal(Left(1), Right(2)).case(error=lambda: True, success=lambda: False)

    assert test_case_False

# Generated at 2022-06-14 03:16:55.972490
# Unit test for method case of class Either
def test_Either_case():
    """
    Either.case docstring describes what this function should do.
    """
    assert Right(5).case(lambda x: x + 1, lambda x: x - 1) == 4
    assert Left('abc').case(lambda x: x + '1', lambda x: x + '2') == 'abc1'



# Generated at 2022-06-14 03:16:57.004187
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Right(1) == Right(1)
    assert Right(1) != Left(1)
    assert isinstance(Right(1), Either)


# Generated at 2022-06-14 03:17:08.853061
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Left(1) == Left('a')
    assert Right(1) == Right('a')
    assert Left(1) != Right(1)



# Generated at 2022-06-14 03:17:16.827829
# Unit test for method case of class Either
def test_Either_case():
    # GIVEN
    either = Right("We can fly")
    # AND
    def error_mapper(value):
        assert 'fail' == value
        return "We are failure"
    # AND
    def success(value):
        assert 'We can fly' == value
        return "We are happy"

    # WHEN
    result = either.case(error_mapper, success)

    # THEN
    assert "We are happy" == result


# Generated at 2022-06-14 03:17:21.589990
# Unit test for method case of class Either
def test_Either_case():
    assert Right(1).case(error=lambda e: e + 1, success=lambda s: s * 3) == 3
    assert Left(1).case(error=lambda e: e + 1, success=lambda s: s * 3) == 2


# Generated at 2022-06-14 03:17:35.821613
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    t1 = Right(1)
    t2 = Right(1)
    t3 = Right(2)
    f1 = Left(1)
    f2 = Left(2)

    assert t1 == t2, 'Equality of Right'
    assert t2 == t1, 'Equality of Right'
    assert t1 != t3, 'Equality of Right'
    assert t3 != t2, 'Equality of Right'
    assert f1 == f1, 'Equality of Left'
    assert f2 == f2, 'Equality of Left'
    assert f2 != f1, 'Equality of Left'
    assert f2 != t1, 'Equality of Left'


# Generated at 2022-06-14 03:17:46.998884
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Test function for to_lazy method of class Either. It check if returned
    monad is Lazy instance and if it's value is the same as stored in Either.
    """

    @nottest
    def is_lazy(instance):
        return isinstance(instance, Lazy)

    @nottest
    def is_value_of_lazy(instance):
        return instance.value() == value

    def lte(msg):
        return "Test to_lazy method of class Either with {} failed".format(msg)

    value = 1
    left = Left(value)
    right = Right(value)

    assert_that(left.to_lazy(), satisfies(is_lazy))
    assert_that(left.to_lazy().value(), is_(value))


# Generated at 2022-06-14 03:17:54.898053
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Right(1) == Right(1)
    assert Left(1) == Left(1)
    assert Left(1) != Right(1)
    assert Left(1) != Right(2)
    assert Right(1) != Left(1)
    assert Right(1) != Left(2)
    assert not Right(1) == Left(1)
    assert not Right(1) == Left(2)
    assert not Left(1) == Right(1)
    assert not Left(1) == Right(2)


# Generated at 2022-06-14 03:17:59.324280
# Unit test for method __eq__ of class Either
def test_Either___eq__():  # TODO: Move to test
    assert Right(1) == Right(1)
    assert Left('test') == Left('test')
    assert Left('test') != Right(1)
    assert Right(1) != Left('test')
    assert Right(1) != Left(1)
    assert Left('test_1') != Left(1)
    assert Left(1) != 1

# Generated at 2022-06-14 03:18:09.358281
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Either(1) is not None
    assert Either(1).__eq__(Either(1)) is True
    assert Either(1).__eq__(Either(2)) is False
    assert Either(1).__eq__(None) is False
    assert Either(2).__eq__(Right(2)) is True
    assert Either(2).__eq__(Left(2)) is True
    assert Either(2).__eq__(Right(3)) is False
    assert Either(2).__eq__(Left(3)) is False


# Generated at 2022-06-14 03:18:13.719157
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Left(1) == Left(1)
    assert Left(2) != Left(1)
    assert Right(1) == Right(1)
    assert Left(1) != Right(1)

# Generated at 2022-06-14 03:18:22.812565
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    try:
        from pymonet.validation import Validation
        from pymonet.lazy import Lazy
        from pymonet.monad_try import Try
        from pymonet.box import Box
        from pymonet.maybe import Maybe
    except ImportError:
        return

    assert Left(1) == Left(1)
    assert Right(2) == Right(2)

    assert Left(1) == Validation.fail([1])
    assert Right(1) == Validation.success(1)

    assert Left(1) == Try(1, False)
    assert Right(1) == Try(1, True)

    assert Left(1) == Lazy(lambda: 1)

    assert Left(1) == Box(1)

    assert Left(1) == Maybe.nothing()
    assert Right(1) == Maybe

# Generated at 2022-06-14 03:18:24.872327
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 4) == Either(4).to_lazy()



# Generated at 2022-06-14 03:18:28.254048
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:18:32.238562
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Test case for method to_lazy of class Either

    :return: assertion error when function doesn't work properly.
    """
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 'lazy') == Lazy(lambda: 'lazy')
    # assert Lazy(lambda: 'lazy') == Lazy(lambda: 'lazy1')


# Generated at 2022-06-14 03:18:47.030725
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    """
    Test for method __eq__ of class Either.

    Unit test for method __eq__ of class Either.
    """
    from pymonet.box import Box

    assert Box(1) == Box(1)
    assert Box(1) != Box(2)
    assert Box(None) != Box(1)
    assert Box(None) == Box(None)



# Generated at 2022-06-14 03:18:56.751106
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    right_a: Right[int] = Right(0)
    right_b: Right[float] = Right(0.)
    right_c: Right[float] = Right(1.)
    left_a: Left[int] = Left(0)
    left_b: Left[float] = Left(0.)
    left_c: Left[float] = Left(1.)
    assert right_a == right_b
    assert right_b == right_a

    assert right_a != left_a
    assert right_a != left_a
    assert left_a != right_a
    assert left_a != right_a

    assert left_a != left_b
    assert left_b != left_a
    assert left_b != left_c
    assert left_c != left_b

    assert right_a != right_c

# Generated at 2022-06-14 03:19:03.021645
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    # Given
    left = Either(42)
    right = Either('foo')

    # When
    lazy_left = left.to_lazy()
    lazy_right = right.to_lazy()

    # Then
    assert lazy_left == Lazy(42)
    assert lazy_right == Lazy('foo')


# Generated at 2022-06-14 03:19:14.114118
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    def success_to_try(either):
        """
        Check that in case of success, to_try returns Try with value and is_success flag set to True.

        :param either: Either to check
        :type either: Either[A]
        """
        assert either.to_lazy().value() == either.value
        assert either.to_lazy().is_success

    def error_to_try(either):
        """
        Check that in case of error, to_try returns Try with value and is_success flag set to False.

        :param either: Either to check
        :type either: Either[A]
        """
        assert either.to_lazy().value() == either.value
        assert not either.to_lazy().is_success

    success_to_try(Right([1, 2, 3]))
   

# Generated at 2022-06-14 03:19:17.857607
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert isinstance(Left(1).to_lazy(), Lazy)
    assert isinstance(Right(1).to_lazy(), Lazy)
    assert Left(1).to_lazy().value() == 1
    assert Right(1).to_lazy().value() == 1


# Generated at 2022-06-14 03:19:21.086110
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    def l1() -> int:
        return 23
    def l2() -> int:
        return "error"

    assert Right(l1).to_lazy() == Lazy(l1)
    assert Left(l2).to_lazy() == Lazy(l2)


# Generated at 2022-06-14 03:19:26.761312
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(1).to_lazy().value() == 1
    assert Right(1).to_lazy().value() == 1
    assert Left(1).to_lazy() == Left(1).to_lazy()
    assert Right(1).to_lazy() == Right(1).to_lazy()
    assert Left(1).to_lazy() != Right(1).to_lazy()


# Generated at 2022-06-14 03:19:31.017406
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert isinstance(Right(12).to_lazy(), Lazy)
    assert isinstance(Left(12).to_lazy(), Lazy)


# Generated at 2022-06-14 03:19:39.079866
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try
    from pymonet.box import Box

    assert Left(5).to_lazy() == Lazy(lambda : 5)
    assert Right(5).to_lazy() == Lazy(lambda : 5)
    assert Right(Box(5)).to_lazy() == Lazy(lambda : Box(5))
    assert Right(Maybe.just(5)).to_lazy() == Lazy(lambda : Maybe.just(5))
    assert Right(Try(5)).to_lazy() == Lazy(lambda : Try(5))
    assert Left(5).to_lazy() == Lazy(lambda : 5)


# Generated at 2022-06-14 03:19:43.427120
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Maybe.just(1).to_lazy()
    assert Lazy(lambda: 1) == Maybe.nothing().to_lazy()


# Generated at 2022-06-14 03:19:46.032617
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(5).to_lazy().value() == 5
    assert Left(5).to_lazy().value() == 5


# Generated at 2022-06-14 03:19:47.058725
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    return None



# Generated at 2022-06-14 03:19:51.639449
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Unit test for method to_lazy of class Either.
    """
    assert Right(5).to_lazy().get() == 5
    assert Left(5).to_lazy().get() == 5



# Generated at 2022-06-14 03:19:56.945159
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    value = 35
    right_maybe = Right(value)
    lazy_right_maybe = right_maybe.to_lazy()

    assert lazy_right_maybe.evaluate() == value


# Generated at 2022-06-14 03:20:04.672628
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe
    from pymonet.map import Map
    import pytest

    assert Left([1, 2]).to_lazy() == Lazy(lambda: [1, 2])
    assert Right(42).to_lazy() == Lazy(lambda: 42)
    assert Left(Map(1, 2)).to_lazy() == Lazy(lambda: Map(1, 2))
    assert Left(Maybe(None)).to_lazy() == Lazy(lambda: Maybe(None))


# Generated at 2022-06-14 03:20:12.688148
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.box import Box
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    Either.to_lazy(Left(Box(2))) == Lazy(lambda: Box(2))
    Either.to_lazy(Right(Box(2))) == Lazy(lambda: Box(2))
    Either.to_lazy(Left(Try(2))) == Lazy(lambda: Try(2))
    Either.to_lazy(Right(Try(2))) == Lazy(lambda: Try(2))
    Either.to_lazy(Left(Lazy(lambda: 2))) == Lazy(lambda: Lazy(lambda: 2))
    Either.to_lazy(Right(Lazy(lambda: 2))) == Lazy(lambda: Lazy(lambda: 2))

#

# Generated at 2022-06-14 03:20:22.384344
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.box import Box

    def square(x):
        return x ** 2

    result = Either(Box(3)).to_lazy()
    assert(result.value() == 9)

    result = Left(Box(3)).to_lazy()
    assert(result.value() == 3)

    result = Either(Box(3)).to_lazy().map(square).value()
    assert(result == 81)

    result = Left(Box(3)).to_lazy().map(square).value()
    assert(result == 3)



# Generated at 2022-06-14 03:20:25.982711
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(3).to_lazy() == Lazy(lambda: 3)
    assert Left(3).to_lazy() == Lazy(lambda: 3)


# Generated at 2022-06-14 03:20:30.892686
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # given
    either = Right(40)

    # when
    actual = either.to_lazy()

    # then
    assert actual.value() == either.value

# Generated at 2022-06-14 03:20:35.897873
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 2) == Lazy(lambda: 2) == Right(2).to_lazy() == Left(2).to_lazy()


# Generated at 2022-06-14 03:20:38.280662
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():

    either = Either.right(1)
    lazy = either.to_lazy()
    assert lazy.get() == 1

# Generated at 2022-06-14 03:20:49.713178
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    from pymonet.maybe import Maybe
    from pymonet.validation import Validation
    from pymonet.box import Box

    assert Either(None).to_lazy() == Lazy(lambda: None)
    assert Either(1).to_lazy() == Lazy(lambda: 1)
    assert Either(1.0).to_lazy() == Lazy(lambda: 1.0)
    assert Either('a').to_lazy() == Lazy(lambda: 'a')
    assert Either([1,2,3]).to_lazy() == Lazy(lambda: [1,2,3])
    assert Either((1,2,3)).to_lazy() == Lazy(lambda: (1,2,3))

# Generated at 2022-06-14 03:20:55.761175
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Unit test for method to_lazy of class Either
    """
    assert Left('[Error]').to_lazy() == Lazy(lambda: '[Error]')
    assert Right(2).to_lazy() == Lazy(lambda: 2)


# Generated at 2022-06-14 03:20:59.187716
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:21:00.412656
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(10).to_lazy() == Lazy(lambda: 10)
    assert Right(10).to_lazy() == Lazy(lambda: 10)


# Generated at 2022-06-14 03:21:02.141733
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(100).to_lazy() == Lazy(100)
    assert Left("test").to_lazy() == Lazy("test")


# Generated at 2022-06-14 03:21:03.702468
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:21:05.489052
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    either = Right(5)
    assert either.to_lazy() == Lazy(5)



# Generated at 2022-06-14 03:21:09.670961
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either(10).to_lazy() == Lazy(lambda: 10)
    assert Either(20).to_lazy() == Lazy(lambda: 20)



# Generated at 2022-06-14 03:21:18.344117
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Test to_lazy of class Either.

    :returns: Nothing
    :rtype: None
    """
    from pymonet.box import Box
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe
    from pymonet.validation import Validation

    # Test for Either
    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)

    # Test for Box
    assert Box(1).to_lazy() == Lazy(lambda: 1)

    # Test for Try
    assert Try(1).to_lazy() == Lazy(lambda: 1)
    assert Try(1, is_success=True).to

# Generated at 2022-06-14 03:21:20.245633
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right([1, 2, 3]).to_lazy() == Lazy(lambda: [1, 2, 3])
    assert Left(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:21:22.654330
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either(1).to_lazy().eval() == 1
    assert Either(-1).to_lazy().eval() == -1


# Generated at 2022-06-14 03:21:29.513604
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left('foo').to_lazy() == Lazy(lambda: 'foo')
    assert Right('bar').to_lazy() == Lazy(lambda: 'bar')


# Generated at 2022-06-14 03:21:32.438457
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    right = Right('Right')
    left = Left('Left')
    assert right.to_lazy().eval() == right.value
    assert left.to_lazy().eval() == left.value


# Generated at 2022-06-14 03:21:35.184347
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either.to_lazy(Left(1)) == Lazy(lambda: 1)
    assert Either.to_lazy(Right(1)) == Lazy(lambda: 1)


# Generated at 2022-06-14 03:21:37.052577
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(5).to_lazy() == Lazy(lambda: 5)
    assert Right(5).to_lazy() == Lazy(lambda: 5)

# Generated at 2022-06-14 03:21:40.806682
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    result = Right(2).to_lazy()
    isinstance(result, Lazy)

    assert result.force() == 2


# Generated at 2022-06-14 03:21:44.363304
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(1).to_lazy().resolve() == 1
    assert isinstance(Right(1).to_lazy(), Lazy)
    assert Left(1).to_lazy().resolve() == 1
    assert isinstance(Left(1).to_lazy(), Lazy)


# Generated at 2022-06-14 03:21:50.694988
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    right_lazy = Either.Right(10).to_lazy()
    assert right_lazy == Either.Right(10).to_lazy()
    assert right_lazy.value == Either.Right(10).to_lazy().value
    assert right_lazy.value() == Either.Right(10).bind(lambda a: a)

    left_lazy = Either.Left(10).to_lazy()
    assert left_lazy == Either.Left(10).to_lazy()
    assert left_lazy.value == Either.Left(10).to_lazy().value
    assert left_lazy.value() == Either.Left(10).value



# Generated at 2022-06-14 03:21:56.877874
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Test to_lazy method of class Either.

    :returns: assertion message if test is failed
    :rtype: String
    """
    either = Right(1)
    lazy = either.to_lazy()

    assert lazy() == 1

    either = Left(1)
    lazy = either.to_lazy()

    assert lazy() == 1



# Generated at 2022-06-14 03:22:01.177293
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(2).to_lazy().flat_map(lambda x: Lazy(x ** 2)).force() == 4
    assert Left(2).to_lazy().flat_map(lambda x: Lazy(x ** 2)).force() == 2


# Generated at 2022-06-14 03:22:11.800661
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.writer import Writer
    from pymonet.writer_monad import WriterMonad
    from pymonet.monad_writer import WriterT
    from pymonet.identity import Identity
    from pymonet.moption import MNone, MJust
    from pymonet.parser import Parser, Satisfy, Many
    from pymonet.monad_state import StateT

    class Monad1(WriterMonad):

        @staticmethod
        def lift(value):
            return WriterT(Identity(Writer(value, value)))

    class Monad2(WriterMonad):

        @staticmethod
        def lift(value):
            return StateT(Identity({'value': value, 'other': 2 * value}))


# Generated at 2022-06-14 03:22:16.901116
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    t = Either(Lazy(lambda: 4))
    assert t == Lazy(lambda: 4)



# Generated at 2022-06-14 03:22:21.883473
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 2) == Right(2).to_lazy()
    assert Lazy(lambda: 2) == Left(2).to_lazy()



# Generated at 2022-06-14 03:22:26.465424
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 10) == Right(10).to_lazy()
    assert Lazy(lambda: 10) != Left(10).to_lazy()

# Generated at 2022-06-14 03:22:29.853698
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert isinstance(Right(1).to_lazy(), Lazy)



# Generated at 2022-06-14 03:22:39.470356
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Either(5).to_lazy() == Lazy(lambda: 5)
    assert Either(5).to_lazy() == Lazy(lambda: 5)
    assert Either(5).to_lazy() == Lazy(lambda: 5)
    assert Either(Try(5)).to_lazy() == Lazy(lambda: Try(5))
    assert Either(Try(5)).to_lazy() == Lazy(lambda: Try(5))
    assert Either(Try(5)).to_lazy() == Lazy(lambda: Try(5))


# Generated at 2022-06-14 03:22:42.108382
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Create new Either[String] and check if is to_lazy method returns correct Lazy[String].

    :returns: None
    :rtype: None
    """
    from pymonet.lazy import Lazy

    assert Right("abc").to_lazy().box() == Lazy(lambda: "abc").box()
    assert Left("abc").to_lazy().box() == Lazy(lambda: "abc").box()


# Generated at 2022-06-14 03:22:45.454843
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # given
    either = Right(1)

    # when, then
    assert either.to_lazy().evaluate() == 1
    assert isinstance(either.to_lazy(), Lazy)


# Generated at 2022-06-14 03:22:55.263284
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Either(2).to_lazy() == Lazy(lambda: 2)
    assert Left(2).to_lazy() == Lazy(lambda: 2)
    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Either(2) == Either(2)
    assert Either(2) != Either(3)
    assert Either(2).case(lambda x: x, lambda x: x) == 2
    assert Either(None).case(lambda x: "error", lambda x: "success") == "success"
    assert Either(2).case(lambda x: 42, lambda x: 2) == 2
    assert Either(2).case(lambda x: 2, lambda x: 42) == 2

# Generated at 2022-06-14 03:23:01.319333
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:23:06.495871
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert isinstance(Either[int](1).to_lazy(), Lazy)
    assert isinstance(Either[int](1).to_lazy().get(), int)
# -----------------------------------------------------


# Generated at 2022-06-14 03:23:21.759089
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # Given
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    try_ = Try(lambda: 10)

    # When
    either = Right(try_)
    lazy = either.to_lazy()

    # Then
    assert lazy == Lazy(lambda: try_)



# Generated at 2022-06-14 03:23:23.964326
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(1).to_lazy().value() == 1
    assert Right(1).to_lazy().value() == 1


# Generated at 2022-06-14 03:23:27.674175
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    def inc(x):
        return x + 1

    def double(x):
        return 2*x

    lazy_inc = Right(inc).to_lazy()
    lazy_double = Right(double).to_lazy()

    assert lazy_inc.bind(lazy_double).extract()(4) == 10

# Generated at 2022-06-14 03:23:32.406813
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Unit test for method to_lazy of class Either"""

    # Test case 1:
    # when Either is Left
    # return lazy monad with function returning None
    assert Left(1).to_lazy() == Lazy(lambda: None)

    # Test case 2:
    # when Either is Right
    # return lazy monad with function returning previous value
    assert Right(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:23:40.087391
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    lazy_value = Right(5).to_lazy()

    assert isinstance(lazy_value, Lazy)
    assert lazy_value.get() == 5

    lazy_value = Left('error').to_lazy()

    assert isinstance(lazy_value, Lazy)
    assert lazy_value.get() == 'error'

# Generated at 2022-06-14 03:23:45.994166
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either(33).to_lazy() == Lazy(lambda: 33)
    assert Either([1, 4, 6]).to_lazy() == Lazy(lambda: [1, 4, 6])
    assert Either(object()).to_lazy() == Lazy(lambda: object())


# Generated at 2022-06-14 03:23:49.621352
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    :returns: nothing
    :rtype: None
    """
    from pymonet.lazy import Lazy

    return_value = "return value of to_lazy"
    assert Right(return_value).to_lazy() == Lazy(lambda: return_value)
    assert Left(return_value).to_lazy() == Lazy(lambda: return_value)


# Generated at 2022-06-14 03:23:55.832273
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(5).to_lazy() == Lazy(lambda: 5)
    assert Right(5).to_lazy() == Lazy(lambda: 5)


# Generated at 2022-06-14 03:24:00.628378
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either[int](2).to_lazy() == Lazy[int](lambda: 2)
    assert Either[int](3).to_lazy() == Lazy[int](lambda: 3)



# Generated at 2022-06-14 03:24:02.827686
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert (Left(5).to_lazy().is_lazy()) == True
    assert (Right(5).to_lazy().is_lazy()) == True


# Generated at 2022-06-14 03:24:19.059459
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left(2).to_lazy() == Lazy(lambda: 2)



# Generated at 2022-06-14 03:24:22.471396
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    passed_lazy = Lazy(lambda: 1)
    passed_either = Right(1)

    assert passed_either.to_lazy() == passed_lazy


# Generated at 2022-06-14 03:24:26.030145
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:24:29.672244
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from test_monad_lazy import test_lazy_monad
    from pymonet.lazy import Lazy

    test_lazy_monad(Right(2), Lazy(lambda: 2))
    test_lazy_monad(Left(1), None)

# Generated at 2022-06-14 03:24:31.946754
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    assert isinstance(Try(1).to_lazy(), Lazy)

# Generated at 2022-06-14 03:24:34.376467
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(3).to_lazy() == Lazy(lambda: 3)
    assert Left(3).to_lazy() == Lazy(lambda: 3)

# Generated at 2022-06-14 03:24:37.788867
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():

    # When create Either with numbers
    either = Either(1)

    # Then should return resolved Lazy with previous number
    assert either.to_lazy().evaluate() == 1

    # When create Either with string
    either = Either('first string')

    # Then should return resolved Lazy with previous string
    assert either.to_lazy().evaluate() == 'first string'

# Generated at 2022-06-14 03:24:44.102179
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    left = Left(1)
    lazy_left = left.to_lazy()
    assert lazy_left.__class__ == Lazy
    assert lazy_left.force() == 1

    right = Right(2)
    lazy_right = right.to_lazy()
    assert lazy_right.__class__ == Lazy
    assert lazy_right.force() == 2


# Generated at 2022-06-14 03:24:48.257236
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    right = Right(1)
    assert right.to_lazy() == Lazy(lambda: 1)
    left = Left(5)
    assert left.to_lazy() == Lazy(lambda: 5)


# Generated at 2022-06-14 03:24:55.982225
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from random import randint
    from datetime import datetime

    random_delay = randint(1, 3)

    assert Lazy(lambda: datetime.now()) == Lazy.unit(datetime.now()) == datetime.now().to_lazy()

    lazy_sum = Lazy(lambda: datetime.now().second + random_delay).bind(lambda x: Lazy(lambda: x + random_delay))

    # Check that lazy has no side effects (even when it should).
    assert lazy_sum.value == datetime.now().second + random_delay
    assert lazy_sum.value == datetime.now().second + random_delay
    assert lazy_sum.value == datetime.now().second + random_delay

    assert Right(datetime.now()).to_l

# Generated at 2022-06-14 03:25:37.687813
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    # GIVEN
    lazy_value = Lazy(lambda: 2)

    # WHEN
    left_lazy_value = Left(lazy_value)
    right_lazy_value = Right(lazy_value)

    # THEN
    assert left_lazy_value.to_lazy() == left_lazy_value.value
    assert right_lazy_value.to_lazy() == right_lazy_value.value



# Generated at 2022-06-14 03:25:43.941653
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    left = Left(3).to_lazy()
    assert left == 3

    right = Right("monad").to_lazy()
    assert right == "monad"

    left_ = Left("left").to_lazy()
    assert left_ == "left"

    right_ = Right(3).to_lazy()
    assert right_ == 3


# Generated at 2022-06-14 03:25:49.427143
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    a = Left(8)
    assert a.to_lazy().cata(lambda _: False, lambda _: True)
    assert not a.to_lazy().value()()


# Generated at 2022-06-14 03:25:55.370734
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(10).to_lazy() == Lazy(lambda: 10)
    assert Left("asd").to_lazy() == Lazy(lambda: "asd")



# Generated at 2022-06-14 03:25:57.729290
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(2).to_lazy() == Lazy(lambda: 2)
    assert Left(2).to_lazy() == Lazy(lambda: 2)

# Generated at 2022-06-14 03:26:00.327267
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right('This is just').to_lazy() == Lazy(lambda: 'This is just')
    assert Left('This is nothing').to_lazy() == Lazy(lambda: 'This is nothing')



# Generated at 2022-06-14 03:26:07.421450
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.lazy import LazyExecResult

    left = Left(1)
    right = Right(2)

    assert isinstance(left.to_lazy(), Lazy)
    assert isinstance(right.to_lazy(), Lazy)
    assert isinstance(left.to_lazy().eval(), LazyExecResult)
    assert isinstance(right.to_lazy().eval(), LazyExecResult)
    assert left.to_lazy().eval().is_left()
    assert right.to_lazy().eval().is_right()
    assert left.to_lazy().eval().get() == left.value
    assert right.to_lazy().eval().get() == right.value

# Generated at 2022-06-14 03:26:16.405315
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert isinstance(Right(None).to_lazy(), Lazy)
    assert Right(None).to_lazy().value() is None
    assert isinstance(Left(None).to_lazy(), Lazy)
    assert Left(None).to_lazy().value() is None
    assert isinstance(Right(1).to_lazy(), Lazy)
    assert Right(1).to_lazy().value() is 1
    assert isinstance(Left(1).to_lazy(), Lazy)
    assert Left(1).to_lazy().value() is 1
    assert isinstance(Right('a').to_lazy(), Lazy)
    assert Right('a').to_lazy().value() is 'a'
    assert isinstance(Left('a').to_lazy(), Lazy)
    assert Left('a').to_l

# Generated at 2022-06-14 03:26:17.425373
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert(Right(5).to_lazy() == Lazy(lambda: 5))
    assert(Left(5).to_lazy() == Lazy(lambda: 5))

# Generated at 2022-06-14 03:26:22.650817
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.box import Box
    from pymonet.monad_try import Try
    from pymonet.lazy import Lazy

    assert Try("Success").to_lazy() == Lazy(lambda: "Success")
    assert \
        Box("Box").to_lazy() == \
        Lazy(lambda: "Box")
    assert \
        Left("Left").to_lazy() == \
        Lazy(lambda: "Left")

