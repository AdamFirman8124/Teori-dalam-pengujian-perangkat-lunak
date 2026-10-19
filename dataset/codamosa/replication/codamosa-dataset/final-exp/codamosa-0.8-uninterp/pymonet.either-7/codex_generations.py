

# Generated at 2022-06-14 03:16:47.849832
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Left(1) == Left(1)
    assert not Left(1) == Left(2)
    assert not Left(1) == Right(1)
    assert Right(1) == Right(1)
    assert not Right(1) == Right(2)
    assert not Right(1) == Left(1)


# Generated at 2022-06-14 03:16:51.448987
# Unit test for method case of class Either
def test_Either_case():
    # Given
    either = Right(2)

    # When
    result = either.case(lambda v: v * 2, lambda v: v / 2)

    # Then
    assert result == 1


# Generated at 2022-06-14 03:16:53.677239
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    either = Left(2)
    assert either == Left(2)
    assert either != Left(3)


# Generated at 2022-06-14 03:16:57.803518
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    def func():
        return 1024

    assert Lazy(func) == Right(1024).to_lazy(), "wrong implementation of Either.to_lazy"
    assert Lazy(func) == Left(1024).to_lazy(), "wrong implementation of Either.to_lazy"

# Generated at 2022-06-14 03:16:59.682106
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left("Error").to_lazy() == Lazy(lambda: "Error")
    assert Right("Success").to_lazy() == Lazy(lambda: "Success")


# Generated at 2022-06-14 03:17:15.674056
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Left(1) == Left(1)
    assert Left('2') == Left('2')
    assert Left('') == Left('')
    assert Left(False) == Left(False)
    assert Left(None) == Left(None)
    assert Right(1) == Right(1)
    assert Right('2') == Right('2')
    assert Right('') == Right('')
    assert Right(False) == Right(False)
    assert not Right(None) == None

    assert not Right(1) == Left(1)
    assert not Right('') == Left('')
    assert not Right(False) == Left(False)
    assert not Right(None) == Left(None)
    assert not Left(1) == Right(1)
    assert not Left(1) == 2

# Generated at 2022-06-14 03:17:20.976571
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either(1).to_lazy() == Lazy(lambda: 1)
    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:17:30.363005
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    from pymonet.box import Box
    from pymonet.monad_try import Try

    assert Left(1) == Left(1)
    try:
        assert Left(1) == Left(2)
        raise Exception
    except AssertionError:
        pass

    assert Right(1) == Right(1)
    try:
        assert Right(1) == Right(2)
        raise Exception
    except AssertionError:
        pass

    assert Left(1) != Right(1)
    assert Right(1) != Left(1)

    assert Left(Box(1)) == Left(Box(1))
    try:
        assert Left(Box(1)) == Left(Box(2))
        raise Exception
    except AssertionError:
        pass

    assert Left(Try(1)) == Left(Try(1))

# Generated at 2022-06-14 03:17:36.008414
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Left(1).__eq__(Left(1))
    assert not Left(1).__eq__(Left(2))
    assert not Left(1).__eq__(Right(1))
    assert Right(1).__eq__(Right(1))
    assert not Right(1).__eq__(Right(2))
    assert not Right(1).__eq__(Left(1))


# Generated at 2022-06-14 03:17:43.377337
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert not Either(1).__eq__(1)
    assert not Either(1).__eq__(Left(2))
    assert not Either(1).__eq__(Right(2))
    assert not Left(1).__eq__(Either(2))
    assert not Right(1).__eq__(Either(2))
    assert not Left(1).__eq__(Right(1))
    assert Left(1).__eq__(Left(1))
    assert Right(1).__eq__(Left(1))



# Generated at 2022-06-14 03:17:54.452101
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try
    from pymonet.box import Box
    from pymonet.lazy import Lazy

    box_just_one = Box(1)
    try_success_one = Try(1)
    maybe_just_one = Maybe.just(1)

    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left("error").to_lazy() == Lazy(lambda: "error")
    assert Right("success").to_lazy() == Lazy(lambda: "success")
    assert Left(box_just_one).to_lazy() == Lazy(lambda: box_just_one)

# Generated at 2022-06-14 03:18:01.276205
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.monad import Functor
    from pymonet.lazy import Lazy
    from pymonet.box import Box

    assert isinstance(Left("Error").to_lazy(), Lazy)
    assert isinstance(Left("Error").to_lazy(), Functor)
    assert Right("Value").to_lazy().value() == "Value"
    assert Right("Value").to_lazy() == Lazy("Value")
    assert Left("Value").to_lazy().value() == "Value"
    assert Left("Value").to_lazy() == Lazy("Value")


# Generated at 2022-06-14 03:18:04.980216
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Lazy(lambda: 1) == Either.to_lazy(Try.success(1))



# Generated at 2022-06-14 03:18:10.860125
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert isinstance(Right(1).to_lazy(), Lazy)
    assert isinstance(Left(1).to_lazy(), Lazy)
    assert Right(1).to_lazy().value() == 1
    assert Left(1).to_lazy().value() == 1

# Unit tests for method to_try of class Either

# Generated at 2022-06-14 03:18:18.319095
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Either

    assert Either(1).to_lazy() == Lazy(lambda: 1)
    assert Either(-1).to_lazy() == Lazy(lambda: -1)
    assert Either(0).to_lazy() == Lazy(lambda: 0)
    assert Either(3.14).to_lazy() == Lazy(lambda: 3.14)
    assert Either("test").to_lazy() == Lazy(lambda: "test")


# Generated at 2022-06-14 03:18:26.118825
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Unit test for to_lazy method of class Either

    :returns: Nothing
    :rtype: None
    """
    from pymonet.lazy import Lazy

    a = Either.to_lazy(Left(1))
    b = Either.to_lazy(Right(2))

    assert(a.is_instance_of(Lazy))
    assert(a() == 1)
    assert(b.is_instance_of(Lazy))
    assert(b() == 2)


# Generated at 2022-06-14 03:18:28.448817
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    def test() -> str:
        return "test"

    assert Right(test).to_lazy().value() == "test"



# Generated at 2022-06-14 03:18:31.927781
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Test to_lazy method of class Either with Left and Right instances.
    """

    from pymonet.lazy import Lazy

    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:18:43.925993
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    lazy = Lazy(lambda: '1')
    assert lazy == Lazy(Right(1).to_lazy().eval)
    assert lazy == Lazy(Left(0).to_lazy().eval)

# Generated at 2022-06-14 03:18:47.263188
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either.to_lazy(Right(4)) == Lazy(lambda: 4)
    assert Either.to_lazy(Left(None)) == Lazy(lambda: None)


# Generated at 2022-06-14 03:19:03.875662
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(1).to_lazy().is_realized() is False
    assert Left(1).to_lazy().is_realized() is False
    assert Right(1).to_lazy().value() == 1
    assert Left(1).to_lazy().value() == 1
    assert Right(1).to_lazy() == Either(1).to_lazy()
    assert Left(1).to_lazy() == Either(1).to_lazy()


# Generated at 2022-06-14 03:19:07.682708
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(ValueError('Wrong type of value')).to_lazy() == Lazy(lambda: ValueError('Wrong type of value'))
    assert Right(10).to_lazy() == Lazy(lambda: 10)



# Generated at 2022-06-14 03:19:09.452830
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    lazy = Either(1).to_lazy()

    assert lazy() == 1


# Generated at 2022-06-14 03:19:12.300761
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert(Left(1).to_lazy().force() == 1)
    assert(Right(1).to_lazy().force() == 1)



# Generated at 2022-06-14 03:19:16.910206
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Right, Left

    right = Right(1)
    left = Left('test')

    assert right.to_lazy() == Lazy(lambda: 1)
    assert left.to_lazy() == Lazy(lambda: 'test')



# Generated at 2022-06-14 03:19:19.581261
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert type(Left("left").to_lazy()) is Lazy
    assert type(Right("right").to_lazy()) is Lazy
    print("unit test for method to_lazy of class Either: success")


# Generated at 2022-06-14 03:19:26.231756
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Right, Left
    from pymonet import io

    def run_lazy_one_time(lazy: Lazy):
        if lazy.is_cached():
            return lazy.get()
        return lazy.get()

    assert run_lazy_one_time(Right(1).to_lazy()) == 1
    assert run_lazy_one_time(Left(io.IO(lambda: 1)).to_lazy()) == 1

# Generated at 2022-06-14 03:19:32.171743
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either(10).to_lazy() == Lazy(lambda: 10)
    assert Either(10).filter(lambda x: not x).to_lazy() == Lazy(lambda: None)
    assert Either(10).filter(lambda x: x == 10).to_lazy() == Lazy(lambda: 10)


# Generated at 2022-06-14 03:19:39.524653
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Test for method to_lazy of class Either.
    """
    from pymonet.lazy import Lazy

    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left('1').to_lazy() == Lazy(lambda: '1')


# Generated at 2022-06-14 03:19:50.803909
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.validation import Validation
    from pymonet.monad_try import Try

    def try_to_int(value: Any) -> Try[int]:
        try:
            return Try.success(int(value))
        except ValueError as error:
            return Try.failure(error)

    assert Try.success(42).to_lazy().map(lambda x: x * 2) == Try.success(84).to_lazy()
    assert Try.failure(ValueError()).to_lazy().map(lambda _: 'BIG DATA') == Try.failure(ValueError()).to_lazy()

# Generated at 2022-06-14 03:20:00.452563
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    def give_right():
        return Right(None)

    def give_left():
        return Left(None)

    assert give_right().to_lazy().__class__.__name__ == 'Lazy'
    assert give_left().to_lazy().__class__.__name__ == 'Lazy'


# Generated at 2022-06-14 03:20:14.172543
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.functions import *

    assert Lazy(lambda: 1) == Right(1).to_lazy()
    assert isinstance(Right(1).to_lazy(), Lazy)


# Generated at 2022-06-14 03:20:15.716897
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either(1).to_lazy().value() == 1


# Generated at 2022-06-14 03:20:22.530757
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert str(Left('ERROR').to_lazy()) == 'Lazy(<function Either.to_lazy.<locals>.<lambda> at 0x10f7a8488>)'
    assert str(Right(10).to_lazy()) == 'Lazy(<function Either.to_lazy.<locals>.<lambda> at 0x10f7a8510>)'


# Generated at 2022-06-14 03:20:26.067066
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(2).to_lazy() == Lazy(lambda: 2)



# Generated at 2022-06-14 03:20:30.330363
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Tests for method to_lazy of class Either.
    """
    from pymonet.lazy import Lazy
    assert Left('error1') == Left('error1').to_lazy()
    assert Right('result') == Right('result').to_lazy()


# Generated at 2022-06-14 03:20:36.588073
# Unit test for method to_lazy of class Either
def test_Either_to_lazy(): # pylint: disable=R0904
    """Unit test for method to_lazy of class Either"""

    def unit_test_to_lazy() -> None:
        """
        Test to_lazy for Either
        """
        assert Right(5).to_lazy().get() == 5
        assert Left(5).to_lazy().get() == 5

    unit_test_to_lazy()


# Generated at 2022-06-14 03:20:38.487127
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.box import Box
    from pymonet.lazy import Lazy

    assert Either(Box(Lazy(lambda: 1))).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:20:47.227634
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.state import State

    assert Either(2).to_lazy() == Lazy(lambda: 2)
    assert Either(State(lambda s: (s + 2, s))).to_lazy() == Lazy(lambda: State(lambda s: (s + 2, s)))
    assert Either(State(lambda s: (s + 2, s))).to_lazy().value() == State(lambda s: (s + 2, s))


# Generated at 2022-06-14 03:20:59.141150
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    def to_lazy_test(mapper, mapper_value) -> None:
        mapper_actual = Either(mapper).to_lazy().force()
        mapper_expected = mapper_value

        assert mapper_actual == mapper_expected, '\nExpected:{0} != Actual: {1}\n'.format(mapper_actual, mapper_expected)

    to_lazy_test(mapper=10, mapper_value=10)
    to_lazy_test(mapper=10 + 20, mapper_value=30)
    to_lazy_test(mapper=[10, 20, 30], mapper_value=[10, 20, 30])
    to_lazy_test(mapper={10, 20, 30}, mapper_value={10, 20, 30})
    to_lazy

# Generated at 2022-06-14 03:21:03.596657
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    lazy_value = Lazy(lambda: 2)
    lazy_value_expected = Right(2).to_lazy()
    assert lazy_value == lazy_value_expected

# Generated at 2022-06-14 03:21:08.069325
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left('error').to_lazy() == Lazy(lambda: 'error')
    assert Right(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:21:08.939412
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    pass


# Generated at 2022-06-14 03:21:10.601346
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either(1234).to_lazy() == Lazy(lambda: 1234)


# Generated at 2022-06-14 03:21:15.455588
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.box import Box

    value = 'b'

    assert Box(value) == Either(value).to_lazy().map(lambda x: x()).to_box()
    assert Either(value).to_lazy().map(lambda x: x()).to_box() == Lazy(lambda: value).to_box()



# Generated at 2022-06-14 03:21:18.555436
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.box import Box
    from pymonet.lazy import Lazy

    lazy_either = Either[int](1).to_lazy()
    assert lazy_either == Lazy(lambda: 1)

    lazy_either.bind(lambda x: Box(x)).to_lazy()
    assert lazy_either == Lazy(lambda: Box(1))



# Generated at 2022-06-14 03:21:26.530973
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.monad_maybe import Maybe
    from pymonet.monad_try import Try
    from pymonet.monad_list import List
    from pymonet.monad_generator import Generator

    assert Left(1).to_lazy().force_eval() == 1
    assert Right(Maybe(1)).to_lazy().force_eval() == Maybe(1)
    assert Left(10).to_lazy().force_eval() == 10
    assert Right(Try(1)).to_lazy().force_eval() == Try(1)
    assert Left(10).to_lazy().force_eval() == 10
    assert Right(List(1, 2, 3)).to_lazy().force_eval() == List(1, 2, 3)
    assert Left(10).to_lazy().force_eval()

# Generated at 2022-06-14 03:21:29.778442
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    lazy = Lazy(lambda: 1)
    assert lazy == Right(1).to_lazy()
    assert lazy == Left(1).to_lazy()

# Generated at 2022-06-14 03:21:32.344988
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    # Test Right
    assert Right(10).to_lazy() == Lazy(lambda: 10)


# Generated at 2022-06-14 03:21:34.436407
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    lazy = Either.to_lazy(Right(4))
    assert isinstance(lazy, Lazy)
    assert lazy() == 4

# Generated at 2022-06-14 03:21:37.637815
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """to_lazy"""

    assert Right(1).to_lazy().force() == Left(1).to_lazy().force()



# Generated at 2022-06-14 03:21:42.673461
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Either(Try(4)).to_lazy() == Lazy(lambda: 4)
    assert Either(Try.raise_(TypeError)).to_lazy() == Lazy(lambda: Try.raise_(TypeError))


# Generated at 2022-06-14 03:21:45.046284
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Check if Either to Lazy properly returns Lazy with function returning value of Either.
    """

    def dummy_mapper(value):
        return 3

    assert Lazy(lambda: 3) == Left(1).to_lazy()
    assert Lazy(lambda: 3) == Right(1).map(dummy_mapper).to_lazy()

# Generated at 2022-06-14 03:21:55.427820
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Make test for method to_lazy of class Either

    """
    from pymonet import Box, Lazy
    from pymonet.lazy import _lazy

    def error(value) -> Box[int]:
        return Box(value)

    def success(value) -> Box[int]:
        return Box(value)

    value = Left(8).case(error, success).to_lazy().value()

    assert value == Lazy(_lazy(error, 8))

# Generated at 2022-06-14 03:22:11.506437
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Tests if both Either maps are equivalent.

    :returns: None
    :rtype: None
    """
    from pymonet.lazy import Lazy

    def func(param: int) -> int:
        return param * 2

    assert Right(2).to_lazy().map(func) == Lazy(lambda: 2).map(func)



# Generated at 2022-06-14 03:22:14.900527
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left('error').to_lazy() == Lazy(lambda: 'error')


# Generated at 2022-06-14 03:22:17.539307
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either(3).to_lazy().value() == 3
    assert Either('abc').to_lazy().value() == 'abc'
    assert Either(None).to_lazy().value() == None


# Generated at 2022-06-14 03:22:28.794134
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe

    def map_test(a) -> 'Maybe[int]':
        return Maybe.just(a + 1)

    def bind_test(a) -> 'Maybe[int]':
        return Maybe.just(a * 10)

    v = Right(2).to_lazy()
    assert (isinstance(v, Lazy) and v.get() == 2)

    v = Left(2).to_lazy()
    assert (isinstance(v, Lazy) and v.get() == 2)

    v = Left(2).to_lazy().map(map_test)
    assert (isinstance(v, Lazy) and v.get().value == 2)


# Generated at 2022-06-14 03:22:36.026390
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    five = Right(5.0).to_lazy()
    five = five.map(lambda value: value / 5)
    assert five == Lazy(5.0 / 5)

    def throw_value_error():
        raise ValueError("Value error")

    five = Lazy(five).map(throw_value_error)
    assert five == Lazy(lambda: 5.0 / 5)

# Generated at 2022-06-14 03:22:38.993745
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Unit test for method to_lazy of class Either"""
    assert Right(1).to_lazy().value() == 1
    assert Left(1).to_lazy().value() == 1


# Generated at 2022-06-14 03:22:52.125068
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    from_right = Either.right(8)
    assert from_right.to_lazy() == Lazy(lambda: 8)
    assert from_right.to_lazy().memoized is None
    assert from_right.to_lazy().force() == 8
    assert from_right.to_lazy().memoized == 8

    from_left = Either.left(8)
    assert from_left.to_lazy() == Lazy(lambda: 8)
    assert from_left.to_lazy().memoized is None
    assert from_left.to_lazy().force() == 8
    assert from_left.to_lazy().memoized == 8


# Generated at 2022-06-14 03:22:53.941157
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(42).to_lazy() == Lazy(lambda: 42), "to_lazy method should create Lazy monad successfully"



# Generated at 2022-06-14 03:22:58.569687
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.functor import Functor
    from pymonet.monad import Monad
    from pymonet.applicative import Applicative

    assert Either(7).to_lazy() == Lazy(lambda: 7)



# Generated at 2022-06-14 03:23:06.230431
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Test that Lazy contains value of Either in its function
    """
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1).equals(Right(1).to_lazy())
    assert Lazy(lambda: 1).equals(Left(1).to_lazy())



# Generated at 2022-06-14 03:23:19.099064
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # given
    either = Right(1)
    # when
    lazy_either = either.to_lazy()
    # then
    assert lazy_either().value == 1


# Generated at 2022-06-14 03:23:22.934709
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert(Left(5).to_lazy() == Lazy(lambda: 5))
    assert(Right(5).to_lazy() == Lazy(lambda: 5))


# Generated at 2022-06-14 03:23:25.482642
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    lazy_1 = Either(10).to_lazy()
    lazy_2 = Either(10).to_lazy()

    assert lazy_1 == lazy_2

# Generated at 2022-06-14 03:23:29.669524
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():

    def increment(number):
        return number + 1

    assert (Right(1).to_lazy().map(increment).map(increment).map(increment).eval()) == (4)
    assert (Left(1).to_lazy().map(increment).map(increment).map(increment).eval()) == (1)



# Generated at 2022-06-14 03:23:31.828927
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:23:40.399193
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.funcs import head

    assert Lazy(lambda: 1).map(head).value() == Lazy(lambda: 1).map(head).value()

    assert Either.unit(1).to_lazy().map(head).value() == Lazy(lambda: 1).map(head).value()


# Generated at 2022-06-14 03:23:51.550323
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    lazy: Lazy[int] = Right(2).to_lazy()

    assert lazy.map(lambda x: x * 2).force() == 4
    assert lazy.map(lambda x: x * 2).force() == 4
    assert lazy.map(lambda x: x * 2).force() == 4



# Generated at 2022-06-14 03:23:56.940199
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(123).to_lazy() == Lazy(lambda: 123)
    assert Right(123).to_lazy() == Lazy(lambda: 123)


# Generated at 2022-06-14 03:24:00.845187
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(2).to_lazy() == Lazy(lambda: 2)
    assert Left("error").to_lazy() == Lazy(lambda: "error")


# Generated at 2022-06-14 03:24:02.678218
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(None).to_lazy().eval() == None
    assert Left(None).to_lazy().eval() == None


# Generated at 2022-06-14 03:24:04.201663
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either(1).to_lazy() == Lazy(lambda: 1)

test_Either_to_lazy()



# Generated at 2022-06-14 03:24:05.229597
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    lazy = Right(10).to_lazy()
    assert lazy.resolve() == 10


# Generated at 2022-06-14 03:24:11.758942
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(4).to_lazy().__repr__() == 'Lazy(value=<function Either.__init__.<locals>.<lambda> at 0x7f8185943730>)', "expected 4"
    assert Right(4).to_lazy().__repr__() == 'Lazy(value=<function Either.__init__.<locals>.<lambda> at 0x7f8185943730>)', "expected 4"



# Generated at 2022-06-14 03:24:13.496861
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    lazy_right = Right(7).to_lazy()
    assert laz

# Generated at 2022-06-14 03:24:15.706134
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:24:20.210360
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # Given
    from pymonet.lazy import Lazy

    left = Left(1)
    right = Right(2)

    # Then
    assert left.to_lazy() == Lazy(lambda: 1)
    assert right.to_lazy() == Lazy(lambda: 2)



# Generated at 2022-06-14 03:24:35.578807
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    assert Right(10).to_lazy() == Lazy(lambda: 10)
    assert Left(10).to_lazy() == Lazy(lambda: 10)


# Generated at 2022-06-14 03:24:42.890382
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try
    from pymonet.box import Box

    assert Lazy(lambda: 2) == Either.Right(2).to_lazy()
    assert Lazy(lambda: 2) == Either.Right(Try.success(2)).to_lazy()
    assert Lazy(lambda: 2) == Either.Right(Box(2)).to_lazy()

# Generated at 2022-06-14 03:24:47.644721
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either(Left(1)).to_lazy() == Lazy(lambda: Left(1))
    assert Either(Right(1)).to_lazy() == Lazy(lambda: Right(1))



# Generated at 2022-06-14 03:24:51.540389
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    assert Left(2).to_lazy() == Lazy(lambda: 2)
    assert Right(2).to_lazy() == Lazy(lambda: 2)


# Generated at 2022-06-14 03:24:54.382904
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    def add(a, b):
        return a+b

    lazy_result = add(Right(1), Left(2)).to_lazy()
    assert lazy_result.eval() == 3

# Generated at 2022-06-14 03:24:56.639369
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:24:58.455023
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either(1).to_lazy().force() == 1
    assert Either(2).to_lazy().force() == 2



# Generated at 2022-06-14 03:25:01.320589
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 1) == Left(1).to_lazy()
    assert Lazy(lambda: 1) == Right(1).to_lazy()


# Generated at 2022-06-14 03:25:18.481624
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Unit test for method to_lazy of class Either
    """
    def succ(val):
        return val + 1

    assert isinstance(Right(1).to_lazy(), Lazy)
    assert Right(1).to_lazy().bind(succ)._thunk() == 2
    assert isinstance(Left(1).to_lazy(), Either)
    assert Left(1).to_lazy() == Left(1)


# Generated at 2022-06-14 03:25:27.883969
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(5).to_lazy().eval() == 5
    assert Right(5).to_lazy().eval() == 5



# Generated at 2022-06-14 03:26:00.866400
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either(1).to_lazy() == Lazy(lambda: 1)
    assert Either(2).to_lazy() == Lazy(lambda: 2)
    assert Either(3).to_lazy() == Lazy(lambda: 3)
    assert Either(4).to_lazy() == Lazy(lambda: 4)
    assert Either(5).to_lazy() == Lazy(lambda: 5)


# Generated at 2022-06-14 03:26:04.006825
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either(1).to_lazy() == Lazy(lambda: 1)
    assert Left(2).to_lazy() == Lazy(lambda: 2)
    assert Right(2).to_lazy() == Lazy(lambda: 2)


# Generated at 2022-06-14 03:26:06.161918
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Lazy(lambda: 5) == Either.to_lazy(Right(5))
    assert Lazy(lambda: 5) == Either.to_lazy(Left(5))



# Generated at 2022-06-14 03:26:10.229180
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    result = Either.to_lazy(Right(1))
    assert result == Lazy(lambda: 1), 'Should transform Right to Lazy with function wrapping result'

    result = Either.to_lazy(Left(1))
    assert result == Lazy(lambda: 1), 'Should transform Left to Lazy with function wrapping result'


# Generated at 2022-06-14 03:26:12.629763
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # Test Either
    assert Right(1).to_lazy().get() == 1
    assert Left(1).to_lazy().get() == 1


# Generated at 2022-06-14 03:26:14.736146
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(5).to_lazy().value() == 5
    assert Right(5).to_lazy().value() == 5


# Generated at 2022-06-14 03:26:17.838154
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(4).to_lazy() == Lazy(lambda: 4)
    assert Left(4).to_lazy() == Lazy(lambda: 4)



# Generated at 2022-06-14 03:26:20.190877
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(2).to_lazy() == Lazy(lambda: 2)
    assert Left("error").to_lazy() == Lazy(lambda: "error")


# Generated at 2022-06-14 03:26:28.654819
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Test Either to_lazy method.

    :returns: None
    :rtype: None
    """
    from pymonet.lazy import Lazy

    assert isinstance(Left(0).to_lazy(), Lazy)
    assert isinstance(Right(0).to_lazy(), Lazy)


# Generated at 2022-06-14 03:26:31.898247
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(1).to_lazy().eval() == 1
    assert Right(1).to_lazy().eval() == 1

