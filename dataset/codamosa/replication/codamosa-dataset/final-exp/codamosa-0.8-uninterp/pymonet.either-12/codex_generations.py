

# Generated at 2022-06-14 03:16:52.540447
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Unit test for method to_lazy of class Either
    """

    # Given
    value = 5
    right = Right(value)

    # When
    lazy = right.to_lazy()

    # Then
    assert lazy.get() == value

# Generated at 2022-06-14 03:16:58.655421
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Right(1) == Right(1)
    assert not Right(1) == Right(2)
    assert Left(1) == Left(1)
    assert not Left(1) == Left(2)
    assert not Right(1) == Left(1)
    assert not Left(1) == Right(1)
    assert not Right(1) == ()


# Generated at 2022-06-14 03:17:04.357842
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    # When two Either is separate instance with the same value
    # Then they are equal
    assert Right(123) == Right(123)
    assert Left(123) == Left(123)

    # When two Either is separate instance with different value
    # Then they are not equal
    assert Right(123) != Right(321)
    assert Left(123) != Left(321)

    # When two Either have the same value but different type (Right and Left)
    # Then they are not equal
    assert Right(123) != Left(123)
    assert Left(123) != Right(123)

# Generated at 2022-06-14 03:17:08.485434
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(1).to_lazy().eval() == 1
    assert Right(1).to_lazy().eval() == 1


# Generated at 2022-06-14 03:17:10.507900
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Either(10) == Either(10)

# Generated at 2022-06-14 03:17:11.824911
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(11).to_lazy().call() == 11

# Generated at 2022-06-14 03:17:15.340760
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert Left(42) == Left(42)
    assert Left(42) is not Right(42)
    assert Right(42) == Right(42)



# Generated at 2022-06-14 03:17:22.644678
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    assert not Left(4) == Right(4)
    assert not Right(4) == Left(4)
    assert Left(4) == Left(4)
    assert Right(4) == Right(4)
    assert not Left(4) == Left(5)
    assert not Right(4) == Right(5)
    assert Left(4) == 4
    assert Right(4) == 4
    assert Left(4) == [4]
    assert Right(4) == [4]

# Generated at 2022-06-14 03:17:28.821091
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    """
    :returns: None
    :rtype: None
    """
    assert Either(1) == Right(1)
    assert Either(1) == Left(1)
    assert Either(1) == Either(1)


# Generated at 2022-06-14 03:17:36.904579
# Unit test for method __eq__ of class Either
def test_Either___eq__():
    from pymonet.maybe import Maybe

    assert Either(None) != Maybe.just(None)
    assert Either(1) == Either(1)
    assert Either(None) != Either(1)
    assert Either(None) == Either(None)
    assert Left(1) == Left(1)
    assert Left(1) != Left(2)
    assert Left(None) == Left(None)
    assert Right(1) == Right(1)
    assert Right(1) != Right(2)
    assert Right(None) == Right(None)


# Generated at 2022-06-14 03:17:43.986398
# Unit test for method case of class Either
def test_Either_case():
    assert Either("foo".__eq__("bar")).case(
        error=lambda error: "Error: " + str(error),
        success=lambda success: "Success: " + str(success)
    ) == "Error: False"

    assert Either("foo".__eq__("foo")).case(
        error=lambda error: "Error: " + str(error),
        success=lambda success: "Success: " + str(success)
    ) == "Success: True"



# Generated at 2022-06-14 03:17:49.185169
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.functor import Functor
    from pymonet.monad import Monad

    assert isinstance(Right(1).to_lazy(), Lazy)
    assert isinstance(Right(1).to_lazy(), Functor)
    assert isinstance(Right(1).to_lazy(), Monad)


# Generated at 2022-06-14 03:17:52.756332
# Unit test for method case of class Either
def test_Either_case():
    is_even = lambda x: x % 2 == 0

    assert Right(2).case(error=lambda _: "error", success=is_even) == True
    assert Left(2).case(error=is_even, success=lambda _: "success") == True

# Generated at 2022-06-14 03:17:58.980271
# Unit test for method case of class Either
def test_Either_case():
    assert Either(1).case(lambda x: x*2, lambda x: x+1) == 2
    assert Either("1").case(lambda x: x*2, lambda x: x+1) == "11"
    assert Either(1).case(lambda x: x*2, lambda x: x+1) != 5

# Generated at 2022-06-14 03:18:07.158710
# Unit test for method case of class Either
def test_Either_case():
    # Given
    left = Left('error')
    right = Right(1)

    # When
    left_result = left.case(lambda err: 'error type: %s' % type(err), lambda suc: 'success')
    right_result = right.case(lambda err: 'error type: %s' % type(err), lambda suc: 'success')
    # Then
    assert left_result == 'error type: <class \'str\'>'
    assert right_result == 'success'



# Generated at 2022-06-14 03:18:14.797788
# Unit test for method case of class Either
def test_Either_case():
    """
    Either.case(error, success)

    either.case(lambda value: f'Error: {value}', lambda value: f'Success: {value}')
    """
    from pymonet.either import Left, Right
    assert Left(5).case(lambda v: f'Error: {v}', lambda v: f'Success: {v}') == 'Error: 5'
    assert Right(5).case(lambda v: f'Error: {v}', lambda v: f'Success: {v}') == 'Success: 5'

# Generated at 2022-06-14 03:18:17.366242
# Unit test for method case of class Either
def test_Either_case():
    assert Right(3).case(lambda _: 2, lambda x: x) == 3
    assert Left(3).case(lambda x: x, lambda _: 2) == 3



# Generated at 2022-06-14 03:18:20.133027
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    x = Either.Left(1).to_lazy()
    y = Either.Right(1).to_lazy()

    assert x.value() == 1
    assert y.value() == 1


# Generated at 2022-06-14 03:18:25.653642
# Unit test for method case of class Either
def test_Either_case():
    """
    Unit test for method case of class Either.
    """
    assert Right(7).case(lambda err: err / 3.0, lambda succ: succ * 2.0) == 14
    assert Left(7).case(lambda err: err / 3.0, lambda succ: succ * 2.0) == 2.3333333333333335


# Generated at 2022-06-14 03:18:30.119364
# Unit test for method case of class Either
def test_Either_case():
    def add_one(num: int) -> int:
        return num + 1

    def add_two(num: int) -> int:
        return num + 2

    assert Left(1).case(add_one, add_two) == 2
    assert Right(1).case(add_one, add_two) == 3



# Generated at 2022-06-14 03:18:52.572198
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.functor import Functor, map_function

    # Check that both Either.to_lazy() and Functor.to_lazy() returns Lazy monad with function returning stored value
    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(2).to_lazy() == Lazy(lambda: 2)
    assert Functor.to_lazy(Left(3)) == Lazy(lambda: 3)
    assert Functor.to_lazy(Right(4)) == Lazy(lambda: 4)

    # Check that lazy returned by Either.to_lazy() and Functor.to_lazy() is not evaluated
    assert Lazy(lambda: 1).case(lambda a: a, lambda a: a) == 1
    lazy

# Generated at 2022-06-14 03:18:58.415602
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Left, Right
    from pymonet.monad_try import Try

    # Test for Left
    left = Left(2)
    lazy = left.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.value == left.value

    # Test for Right
    right = Right(2)
    lazy = right.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.value == right.value



# Generated at 2022-06-14 03:19:02.419237
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(3).to_lazy().value() == 3
    assert Left(3).to_lazy().value() == 3

    assert isinstance(Right(3).to_lazy(), Lazy)
    assert isinstance(Left(3).to_lazy(), Lazy)


# Generated at 2022-06-14 03:19:07.243507
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Unit test for method to_lazy of class Either"""
    from pymonet.lazy import Lazy

    assert Right(100).to_lazy() == \
        Lazy(lambda: 100)
    assert Left(100).to_lazy() == \
        Lazy(lambda: 100)


# Generated at 2022-06-14 03:19:09.781188
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either(Right(3)).to_lazy().value() == 3
    assert Either(Left(3)).to_lazy().value() == 3


# Generated at 2022-06-14 03:19:13.107588
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Unit test for method to_lazy of class Either"""
    either = Either.right(5)

    assert either.to_lazy() == Lazy(lambda: 5)



# Generated at 2022-06-14 03:19:18.168102
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    result = Right(5).to_lazy()

    assert isinstance(result, Lazy)
    assert result.evaluate() == 5

    result = Left(5).to_lazy()

    assert isinstance(result, Lazy)
    assert isinstance(result.evaluate(), Left)
    assert result.evaluate().value == 5



# Generated at 2022-06-14 03:19:20.800989
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:19:25.424775
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Unit test for method to_lazy of class Either

    :return: nothing
    :rtype: None
    """
    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left(1).to_lazy() == Lazy(lambda: 1)

# Generated at 2022-06-14 03:19:28.624336
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Lazy(lambda: 1) == Left(1).to_lazy()
    assert Lazy(lambda: True) == Right(True).to_lazy()


# Generated at 2022-06-14 03:19:42.862266
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Unit test for method to_lazy of class Either"""

    from pymonet.lazy import Lazy

    def double(number):
        """Double a number"""
        return number * 2

    def lazy_double(lazy: Lazy[int]):
        """Double a number, which can be obtained via call of lazy.eval()"""
        return lazy.map(double).eval()

    assert lazy_double(Right(2).to_lazy()) == 4
    assert lazy_double(Left(2).to_lazy()) == 4


# Generated at 2022-06-14 03:19:54.994614
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either(10).to_lazy() == Lazy(lambda: 10)
    assert Either('test').to_lazy() == Lazy(lambda: 'test')


# Generated at 2022-06-14 03:19:59.428193
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    import pytest

    assert(Left(1).to_lazy().force() == 1)
    assert(Right(2).to_lazy().force() == 2)


# Generated at 2022-06-14 03:20:03.967542
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe
    from pymonet.monad_try import Try
    from pymonet.validation import Validation

    assert Lazy(lambda: 2) == Right(2).to_lazy()
    assert Lazy(lambda: 2) == Left(2).to_lazy()



# Generated at 2022-06-14 03:20:06.655075
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(10).to_lazy() == Lazy(lambda: 10)
    assert Right(10).to_lazy() == Lazy(lambda: 10)


# Unit tests for method ap of class Either

# Generated at 2022-06-14 03:20:11.346915
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either.case(Left(1), lambda value: value + 1, lambda value: value + 1) == 2
    assert Either.case(Left(2), lambda value: value + 1, lambda value: value + 1) == 3
    assert Either.case(Right(2), lambda value: value + 1, lambda value: value + 1) == 4
    assert Either.case(Right(3), lambda value: value + 1, lambda value: value + 1) == 5

# Generated at 2022-06-14 03:20:22.619729
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    def func(a, b):
        return a + b

    def ret_func(a):
        def ret():
            return a
        return ret

    assert Right(10).to_lazy() == Lazy(ret_func(10))
    assert Left(10).to_lazy() == Lazy(ret_func(10))

    assert Right(func)(Right(10)).to_lazy() == Lazy(ret_func(func))(Right(10).to_lazy()).bind(lambda f: f(10))
    assert Left(func)(Right(10)).to_lazy() == Lazy(ret_func(10))
    assert Right(func)(Left(10)).to_lazy() == Lazy(ret_func(10))

# Generated at 2022-06-14 03:20:26.194321
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    def fn(): pass

    assert Left(fn).to_lazy() == Lazy(fn)
    assert Right(fn).to_lazy() == Lazy(fn)


# Generated at 2022-06-14 03:20:32.262596
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(12).to_lazy() == Lazy(lambda: 12)
    assert Right(12).to_lazy() == Lazy(lambda: 12)


# Generated at 2022-06-14 03:20:35.441048
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(1).to_lazy().eval() == 1
    assert Right(1).to_lazy().eval() == 1


# Generated at 2022-06-14 03:20:45.303077
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert (Right(2)).to_lazy() == Lazy(lambda: 2)
    assert (Left(2)).to_lazy() == Lazy(lambda: 2)


# Generated at 2022-06-14 03:20:51.367791
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():

    # Given
    from pymonet.lazy import Lazy
    expected_result = Lazy(lambda: 5)
    e = Right(5)

    # When
    actual_result = e.to_lazy()

    # Then
    assert actual_result == expected_result



# Generated at 2022-06-14 03:20:54.526168
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(2).to_lazy() == Lazy(lambda: 2)
    assert Left(2).to_lazy() == Lazy(lambda: 2)


# Generated at 2022-06-14 03:20:56.796403
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    import pytest

    assert Either.to_lazy(Left('fail')) == Either.to_lazy(Right('success'))

# Generated at 2022-06-14 03:20:58.728293
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)



# Generated at 2022-06-14 03:21:01.504643
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Test to_lazy method of class Either.

    :returns: Nothing
    :rtype: None
    """
    from pymonet.lazy import Lazy
    from pymonet.box import Box

    assert Either(1).to_lazy() == Lazy(Box(1).force)


# Generated at 2022-06-14 03:21:03.893811
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    def f():
        return 42
    assert Lazy(f) == Right(42).to_lazy()


# Generated at 2022-06-14 03:21:10.646628
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    from pymonet.test.test_box import test_Box_to_lazy
    from pymonet.test.test_monad_try import test_Try_to_lazy

    result = (Left(1).to_lazy()).equals(Lazy(lambda: 1))
    assert result is True, "Either to Lazy succeded"

    result = (Right(1).to_lazy()).equals(Lazy(lambda: 1))
    assert result is True, "Either to Lazy succeded"

    test_Box_to_lazy()
    test_Try_to_lazy()



# Generated at 2022-06-14 03:21:14.338339
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    left = Either([1, 2, 3])
    right = Either()
    assert left.to_lazy() == Lazy([1, 2, 3])
    assert right.to_lazy() == Lazy(right)



# Generated at 2022-06-14 03:21:16.958091
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(2).to_lazy() == Lazy(lambda: 2)
    assert Right(3).to_lazy() == Lazy(lambda: 3)


# Generated at 2022-06-14 03:21:32.487384
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Left, Right

    assert Right(10).to_lazy() == Lazy(lambda: 10)
    assert Left(10).to_lazy() == Lazy(lambda: 10)



# Generated at 2022-06-14 03:21:37.595054
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    def test_success():
        assert (Right(1).to_lazy().force() == 1)

    def test_fail():
        assert (Left(1).to_lazy().force() == Left(1))

    def test_is_lazy():
        assert (Right(1).to_lazy().value == 1)

    test_success()
    test_fail()
    test_is_lazy()



# Generated at 2022-06-14 03:21:41.679561
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either[int](-1).to_lazy() == Lazy(lambda: -1)
    assert Either[int](1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:21:43.904795
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert isinstance(Left(1).to_lazy(), Lazy)
    assert isinstance(Left(1).to_lazy(), Lazy)



# Generated at 2022-06-14 03:21:49.091923
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Unit test for Either.to_lazy"""
    from pymonet.lazy import Lazy

    def right_to_lazy() -> Lazy[int]:
        return Right(1).to_lazy()

    assert right_to_lazy() == Lazy(lambda: 1)

    def left_to_lazy() -> Lazy[int]:
        return Left(1).to_lazy()

    assert left_to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:21:50.722979
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Either(123).to_lazy() == Lazy(lambda: 123)
    assert Either("hello").to_lazy() == Lazy(lambda: "hello")


# Generated at 2022-06-14 03:21:53.367177
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.maybe import Maybe

    assert Either(True).to_lazy() == Lazy(lambda: True)
    assert Left(True).to_lazy() == Lazy(lambda: True)
    assert Right(True).to_lazy() == Lazy(lambda: True)



# Generated at 2022-06-14 03:21:57.188864
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Either.to_lazy(Left(1)) == Lazy(lambda: 1)
    assert Either.to_lazy(Right(2)) == Lazy(lambda: 2)


# Generated at 2022-06-14 03:22:02.762785
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    class TestClass:

        def __init__(self, some_value):
            self.some_value = some_value

    value = Lazy(lambda: TestClass(1))

    right = Right(value)
    lazy = right.to_lazy()
    assert lazy.value().some_value == value.value().some_value

# Generated at 2022-06-14 03:22:09.974677
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():

    # Arrange
    from pymonet.lazy import Lazy
    lazy1 = Lazy.just(4)

    # Act
    lazy2 = Right(4).to_lazy()

    # Assert
    assert lazy1 == lazy2



# Generated at 2022-06-14 03:22:31.113978
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad_option import Option
    from pymonet.monad_list import List
    from pymonet.monad_dict import Dict
    from pymonet.monad_set import Set

    assert Left('left').to_lazy() == Lazy(lambda: 'left')
    assert Right('right').to_lazy() == Lazy(lambda: 'right')

    assert Either.to_lazy(Option('abrakadabra')) == Lazy(lambda: 'abrakadabra')
    assert Either.to_lazy(List([1, 2, 3])) == Lazy(lambda: [1, 2, 3])

# Generated at 2022-06-14 03:22:45.198512
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Create lazy monad with function return previous value.

    :returns: Lazy[Function() -> A]
    :rtype: Lazy[Function() -> A]
    """
    assert Right(5).to_lazy().get() == 5
    assert Left(5).to_lazy().get() == 5



# Generated at 2022-06-14 03:22:48.705108
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    res = print(Lazy(lambda: Either(2)).flat_map(lambda x: x.to_lazy()).get())
    assert res == 2

# Generated at 2022-06-14 03:22:52.451147
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    # Create new Right with value
    either_right = Right(1)

    # Apply method to_lazy
    lazy = either_right.to_lazy()

    # Check value in lazy
    assert lazy == Lazy(lambda: 1)

# Generated at 2022-06-14 03:22:54.144277
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(1).to_lazy().eval() == Left(1)
    assert Right(1).to_lazy().eval() == Right(1)



# Generated at 2022-06-14 03:22:58.046824
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(2).to_lazy() == Lazy(2)
    assert Left(None).to_lazy() == Lazy(None)

# Generated at 2022-06-14 03:23:06.573072
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Unit test for method to_lazy of class Either.
    """
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Lazy.unit(1) == Either.unit(1).to_lazy()
    assert Try.unit(1).get_resolved() == Either.unit(1).to_lazy().force()


# Generated at 2022-06-14 03:23:17.739663
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Right(42).to_lazy() == Lazy(lambda: 42)


# Generated at 2022-06-14 03:23:27.514850
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Unit test for method to_lazy of class Either.

    :return: None
    """
    from pymonet.lazy import Lazy
    from pymonet.funcs import lazy

    assert Lazy(lambda: 2) == Either.to_lazy(Right(2))
    assert Lazy(lambda: 2) == Either.to_lazy(Right(2)).map(lambda el: el + 1)
    assert Lazy(lambda: 1) == Either.to_lazy(Left(1))
    assert Lazy(lambda: 1) == Either.to_lazy(Left(1)).map(lambda el: el + 1)
    assert Lazy(lambda: 3) == Either.to_lazy(Right(2)).bind(lazy(lambda el: el + 1))



# Generated at 2022-06-14 03:23:30.885431
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(Just(Right("Right"))).to_lazy().value() == Just(Right("Right"))
    assert Left("Left").to_lazy().value() == "Left"
    assert Left(Right("Right")).to_lazy().value() == Right("Right")


# Generated at 2022-06-14 03:24:03.894154
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left('error').to_lazy() == Lazy(lambda: 'error')
    assert Right(5).to_lazy() == Lazy(lambda: 5)


# Generated at 2022-06-14 03:24:06.837571
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Test to_lazy method of class Either.
    """
    from pymonet.lazy import Lazy
    def function():
        return "Lazy value"
    result = Right(function).to_lazy()
    assert result == Lazy(function)

# Generated at 2022-06-14 03:24:09.480935
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # Given
    either = Either(5)

    # When
    result = either.to_lazy()

    # Then
    assert result.force() == 5


# Generated at 2022-06-14 03:24:12.645916
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(2).to_lazy() == Lazy(lambda: 2)



# Generated at 2022-06-14 03:24:15.966623
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.monad import LazyInstanceMethod

    assert LazyInstanceMethod in Lazy(lambda: Right(2)).map(lambda x: x).__class__.mro()



# Generated at 2022-06-14 03:24:19.664996
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.either import Left, Right
    from pymonet import expect

    val = Lazy(lambda: 42)
    expect(Right(42).to_lazy()).to_equal(val)

# Generated at 2022-06-14 03:24:25.131937
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(True).to_lazy() == Lazy(lambda: True)
    assert Right(1).to_lazy() == Lazy(lambda: 1)
    assert Left(True).to_lazy() == Lazy(lambda: True)
    assert Left('str').to_lazy() == Lazy(lambda: 'str')



# Generated at 2022-06-14 03:24:32.910782
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.iterable import Iterable
    from pymonet.lazy import Lazy
    from pymonet.monad_try import Try

    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)

    assert Left(Try(1, True)).to_lazy() == Lazy(lambda: Try(1, True))
    assert Right(Try(1, True)).to_lazy() == Lazy(lambda: Try(1, True))

    assert Left(Lazy(lambda: 1)).to_lazy() == Lazy(lambda: Lazy(lambda: 1))
    assert Right(Lazy(lambda: 1)).to_lazy() == Lazy(lambda: Lazy(lambda: 1))


# Generated at 2022-06-14 03:24:38.601108
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    from pymonet.functor import Functor
    from pymonet.monad_maybe import Maybe

    x1 = Either.right(5)
    assert x1.to_lazy() == Lazy(lambda: x1.value)

    x2 = Either.left(10)
    assert x2.to_lazy() == Lazy(lambda: x2.value)

    x3 = x1.to_maybe()

    assert x3 == Maybe.just(5)
    assert x3.to_lazy() == Lazy(lambda: x3.value)


# Generated at 2022-06-14 03:24:44.600030
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # Given
    lazy_left = Left(None)
    lazy_right = Right(None)

    # When
    result_left = lazy_left.to_lazy()
    result_right = lazy_right.to_lazy()

    # Then
    assert result_left.is_instance_of(lazy_class=Lazy)
    assert result_right.is_instance_of(lazy_class=Lazy)

# Generated at 2022-06-14 03:25:33.275883
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    # Given
    left = Left(1)
    right = Right(2)
    # When
    left_result = left.to_lazy()
    right_result = right.to_lazy()
    # Then
    assert left_result() == 1
    assert right_result() == 2


# Generated at 2022-06-14 03:25:38.098504
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    assert Left(1).to_lazy() == Lazy(lambda: 1)
    assert Right(1).to_lazy() == Lazy(lambda: 1)


# Generated at 2022-06-14 03:25:40.640144
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy
    def get_two() -> int:
        return 2

    get_two_lazy = Lazy(get_two)

    assert get_two_lazy == Right(2).to_lazy()


# Generated at 2022-06-14 03:25:50.055808
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    global_variable = 0

    def add(a: int, b: int) -> int:
        global global_variable
        global_variable += 1
        return a + b

    right = Right(1)
    left = Left(0)

    lazy = right.to_lazy()
    assert callable(lazy.value)
    assert lazy.value() == 1

    lazy = left.to_lazy()
    assert callable(lazy.value)
    assert lazy.value() == 0

    assert global_variable == 0
    assert add(right, right) == 2
    assert global_variable == 2
    assert add(right, left) == 1
    assert global_variable == 3
    assert add(left, right) == 1
    assert global_variable == 4
    assert add(left, left) == 0

# Generated at 2022-06-14 03:25:57.863913
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    from pymonet.lazy import Lazy

    test_value = 'test'

    def lazy_test_value() -> str:
        """Generate test value for Lazy"""
        return test_value

    assert Right(test_value).to_lazy() == Lazy(lazy_test_value)
    assert Left(test_value).to_lazy() == Lazy(lazy_test_value)



# Generated at 2022-06-14 03:25:59.309215
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Left(1).to_lazy().force() == 1
    assert Right(1).to_lazy().force() == 1


# Generated at 2022-06-14 03:26:03.368814
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """
    Either should be convertable to Lazy
    """
    assert Lazy(lambda: 'foo').equals(Either('foo').to_lazy())
    assert Lazy(lambda: 'foo').equals(Right('foo').to_lazy())
    assert Lazy(lambda: 'foo').equals(Left('foo').to_lazy())



# Generated at 2022-06-14 03:26:07.945899
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    assert Right(None).to_lazy() == Lazy(lambda: None)
    assert Left(None).to_lazy() == Lazy(lambda: None)


# Generated at 2022-06-14 03:26:14.668756
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    """Unit test for method to_lazy of class Either"""
    from pymonet.lazy import Lazy
    from pymonet.either import Left, Right

    fn = lambda: 1
    lazy1 = Lazy(fn)
    either1 = Left("error")
    either2 = Right(1)

    assert either1.to_lazy() == lazy1
    assert either2.to_lazy() == lazy1



# Generated at 2022-06-14 03:26:28.576875
# Unit test for method to_lazy of class Either
def test_Either_to_lazy():
    import pytest
    from pymonet.lazy import Lazy

    def double(x: int) -> int:
        return 2 * x

    assert Left(42).to_lazy() == Lazy(lambda: 42)
    assert Right(42).to_lazy() == Lazy(lambda: 42)
